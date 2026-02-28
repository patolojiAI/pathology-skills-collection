#!/usr/bin/env python3
"""
Multi-format pathology report processor for pathology-skills-collection.

⚠️  WARNING: This script requires ANTHROPIC_API_KEY and makes direct API calls.
⚠️  If you have Claude CLI, use it directly instead (no API key needed):
⚠️
⚠️    claude "Use colorectal-pathology-specialist to analyze reports.xlsx"
⚠️
⚠️  See docs/BATCH_PROCESSING.md for guidance.

Process reports in any format (text, Excel, CSV, PDF, images) using any skill.

Usage:
    # Requires: export ANTHROPIC_API_KEY="sk-ant-..."
    python scripts/process_skill.py --skill breast-pathology-specialist report.pdf
    python scripts/process_skill.py --skill colorectal-pathology-specialist reports.xlsx --output results/
    python scripts/process_skill.py --skill compliance-checker input_dir/ --output results/
"""

import argparse
import sys
import os
from pathlib import Path
from typing import List, Dict, Any
import logging

# Add parent directory to path for imports
REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / 'scripts'))

from file_readers import read_file_content, is_supported_file, get_supported_extensions
from excel_handler import export_results_to_excel, create_simple_excel

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_skill_references(skill_path: Path) -> str:
    """Load all reference files for a skill."""
    references_text = []

    # Load skill SKILL.md
    skill_md = skill_path / 'SKILL.md'
    if skill_md.exists():
        references_text.append(f"=== SKILL DEFINITION ===\n{skill_md.read_text()}\n")

    # Load local references
    references_dir = skill_path / 'references'
    if references_dir.exists():
        for ref_file in references_dir.rglob('*.md'):
            references_text.append(
                f"=== {ref_file.relative_to(skill_path)} ===\n{ref_file.read_text()}\n"
            )

    # Load shared references (common to all skills)
    shared_refs = skill_path.parent.parent / 'shared-references'
    if shared_refs.exists():
        # Load key shared files
        for shared_file in shared_refs.rglob('*.md'):
            # Limit to essential files to avoid token overflow
            if any(key in shared_file.name.lower() for key in ['tnm', 'template', 'biomarker', 'coding']):
                references_text.append(
                    f"=== SHARED: {shared_file.relative_to(shared_refs)} ===\n{shared_file.read_text()}\n"
                )

    return '\n\n'.join(references_text)


def analyze_with_skill(report_text: str, skill_name: str, skill_path: Path, client) -> str:
    """Analyze a single report using the specified skill."""
    # Load skill and references
    references = load_skill_references(skill_path)

    # Build comprehensive prompt
    prompt = f"""You are a pathology quality assurance specialist using the {skill_name} skill.

{references}

INSTRUCTIONS:
Analyze the following pathology report according to the skill guidelines above.
Perform comprehensive compliance checking, identify missing elements, validate staging,
and provide recommendations.

PATHOLOGY REPORT TO ANALYZE:
{report_text}

Provide a detailed compliance analysis following the skill's format and scoring system.
"""

    logger.info(f"Analyzing report with {skill_name} (prompt: {len(prompt)} chars)")

    # Call Claude API
    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=8000,
            messages=[{"role": "user", "content": prompt}]
        )

        analysis = response.content[0].text
        return analysis

    except Exception as e:
        logger.error(f"Analysis failed: {e}")
        return f"ERROR: Analysis failed - {str(e)}"


def parse_analysis_for_excel(analysis_text: str, filename: str) -> Dict[str, Any]:
    """
    Parse analysis text to extract structured data for Excel export.

    Looks for compliance score, gaps, recommendations, etc.
    """
    result = {
        'filename': filename,
        'compliance_score': 0,
        'status': 'Unknown',
        'gaps': [],
        'analysis': analysis_text,
        'recommendations': ''
    }

    # Try to extract compliance score
    import re

    score_match = re.search(r'COMPLIANCE SCORE:?\s*(\d+)/?100', analysis_text, re.IGNORECASE)
    if score_match:
        result['compliance_score'] = int(score_match.group(1))

    # Extract status
    if result['compliance_score'] >= 90:
        result['status'] = 'Compliant'
    elif result['compliance_score'] >= 70:
        result['status'] = 'Minor Issues'
    elif result['compliance_score'] >= 50:
        result['status'] = 'Major Issues'
    else:
        result['status'] = 'Critical Issues'

    # Extract missing elements / gaps
    gaps_section = re.search(
        r'MISSING ELEMENTS.*?:(.*?)(?=\n\n[A-Z]|\nCROSS-VALIDATION|\nRECOMMENDATIONS|\Z)',
        analysis_text,
        re.DOTALL | re.IGNORECASE
    )

    if gaps_section:
        gaps_text = gaps_section.group(1)
        # Find bullet points or numbered items
        gap_lines = re.findall(r'[-•\*]\s*(.+)', gaps_text)
        result['gaps'] = [g.strip() for g in gap_lines if g.strip()]

    # Extract recommendations
    rec_match = re.search(
        r'RECOMMENDATIONS?:?(.*?)(?=\Z)',
        analysis_text,
        re.DOTALL | re.IGNORECASE
    )

    if rec_match:
        result['recommendations'] = rec_match.group(1).strip()

    return result


def process_single_file(filepath: Path, skill_name: str, skill_path: Path, client, output_dir: Path):
    """Process a single file of any format."""
    logger.info(f"Processing {filepath.name}")

    # Read file content
    try:
        content = read_file_content(filepath, client, use_vision=True)
    except Exception as e:
        logger.error(f"Failed to read {filepath.name}: {e}")
        return None

    # Handle batch Excel/CSV
    if isinstance(content, list):
        logger.info(f"Detected batch mode: {len(content)} reports in {filepath.name}")

        results = []
        for idx, row in enumerate(content, start=1):
            report_text = row.get('report_text', '')
            patient_id = row.get('patient_id', f'Row_{idx}')

            logger.info(f"  Processing row {idx}/{len(content)}: {patient_id}")

            analysis = analyze_with_skill(report_text, skill_name, skill_path, client)
            result = parse_analysis_for_excel(analysis, f"{filepath.stem}_row{idx}_{patient_id}")

            results.append(result)

            # Save individual report
            output_file = output_dir / f"{filepath.stem}_row{idx}_{patient_id}_qa.txt"
            output_file.write_text(analysis)

        # Export to Excel
        excel_path = output_dir / f"{filepath.stem}_batch_results.xlsx"
        export_results_to_excel(results, excel_path, skill_name)

        logger.info(f"✅ Batch processing complete: {len(results)} reports → {excel_path}")

        return results

    else:  # Single report
        analysis = analyze_with_skill(content, skill_name, skill_path, client)

        # Save individual text report
        output_file = output_dir / f"{filepath.stem}_qa.txt"
        output_file.write_text(analysis)

        logger.info(f"✅ Analysis saved to {output_file}")

        # Parse for structured data
        result = parse_analysis_for_excel(analysis, filepath.name)

        return [result]


def process_directory(input_dir: Path, skill_name: str, skill_path: Path, client, output_dir: Path):
    """Process all supported files in a directory."""
    # Find all supported files
    all_files = []

    for ext_list in get_supported_extensions().values():
        for ext in ext_list:
            all_files.extend(input_dir.glob(f"*{ext}"))

    if not all_files:
        logger.warning(f"No supported files found in {input_dir}")
        return

    logger.info(f"Found {len(all_files)} files to process")

    all_results = []

    for filepath in all_files:
        results = process_single_file(filepath, skill_name, skill_path, client, output_dir)
        if results:
            all_results.extend(results)

    # Create combined Excel report
    if all_results:
        combined_excel = output_dir / f"{input_dir.name}_all_results.xlsx"
        export_results_to_excel(all_results, combined_excel, skill_name)

        logger.info(f"✅ Combined results: {len(all_results)} reports → {combined_excel}")


def main():
    parser = argparse.ArgumentParser(
        description='Process pathology reports in any format using specified skill',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Single PDF
  python scripts/process_skill.py --skill breast-specialist report.pdf

  # Excel batch
  python scripts/process_skill.py --skill colorectal-specialist reports.xlsx --output results/

  # Image
  python scripts/process_skill.py --skill pancreas-specialist scan.jpg

  # Directory
  python scripts/process_skill.py --skill compliance-checker input_dir/ --output results/

Supported formats:
  - Text: .txt, .md
  - Excel: .xlsx, .xls (batch or structured)
  - CSV: .csv
  - PDF: .pdf (vision API)
  - Images: .jpg, .png, .tiff (vision API)
  - Word: .docx
        """
    )

    parser.add_argument('input', help='Input file or directory')
    parser.add_argument('--skill', required=True,
                        help='Skill name (breast-specialist, colorectal-specialist, etc.)')
    parser.add_argument('--output', default='results/',
                        help='Output directory (default: results/)')
    parser.add_argument('--api-key',
                        help='Anthropic API key (or set ANTHROPIC_API_KEY env var)')

    args = parser.parse_args()

    # Get API key
    api_key = args.api_key or os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        logger.error("API key required. Set ANTHROPIC_API_KEY or use --api-key")
        sys.exit(1)

    # Initialize Anthropic client
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
    except ImportError:
        logger.error("anthropic package required. Install with: pip install anthropic")
        sys.exit(1)

    # Validate skill
    skills_dir = Path(__file__).parent.parent / 'pathology-skills'
    skill_path = skills_dir / args.skill

    if not skill_path.exists():
        logger.error(f"Skill not found: {args.skill}")
        logger.info(f"Available skills: {[d.name for d in skills_dir.iterdir() if d.is_dir()]}")
        sys.exit(1)

    # Create output directory
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Process input
    input_path = Path(args.input)

    if not input_path.exists():
        logger.error(f"Input not found: {input_path}")
        sys.exit(1)

    logger.info(f"Starting processing with skill: {args.skill}")

    if input_path.is_file():
        process_single_file(input_path, args.skill, skill_path, client, output_dir)
    else:
        process_directory(input_path, args.skill, skill_path, client, output_dir)

    logger.info("✅ Processing complete!")


if __name__ == '__main__':
    main()
