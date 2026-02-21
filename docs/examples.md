# Workflow Examples

Complete use case examples for common pathology workflows using the skills collection.

## ⚠️ IMPORTANT: How to Use These Examples

**✅ CORRECT WAY (Claude CLI with LLM intelligence):**
```bash
claude "Use colorectal-pathology-specialist to analyze reports.xlsx and export results"
```

**❌ WRONG WAY (Generates regex-only script):**
```bash
claude "Write a Python script to check compliance"
```

All examples below use Claude CLI directly with full LLM intelligence. See [BATCH_PROCESSING.md](BATCH_PROCESSING.md) for detailed guidance.

---

## Table of Contents

1. [Department Quality Assurance](#1-department-quality-assurance)
2. [Resident Training Program](#2-resident-training-program)
3. [LIS Integration](#3-lis-integration)
4. [Tumor Board Preparation](#4-tumor-board-preparation)
5. [Legacy Report Migration](#5-legacy-report-migration)
6. [Breast Cancer Center Workflow](#6-breast-cancer-center-workflow)
7. [GI Pathology Fellowship](#7-gi-pathology-fellowship)
8. [Post-Neoadjuvant Assessment](#8-post-neoadjuvant-assessment)

---

## 1. Department Quality Assurance

### Scenario
Weekly QA review of 50 signed-out cancer reports to identify common gaps and track compliance trends over time.

### Requirements
- Batch processing capability
- Excel export for tracking
- Trend analysis
- Summary statistics

### Implementation

**Step 1: Setup Directory Structure**
```bash
mkdir -p ~/pathology-qa/
cd ~/pathology-qa/

# Create subdirectories
mkdir -p input output reports trends
```

**Step 2: Collect Reports**
```bash
# Copy signed-out reports from LIS export
# Assuming reports are text files
cp /lis/export/week_of_2026_01_13/*.txt input/
```

**Step 3: Batch Processing with Claude CLI**

```bash
# Process all reports in one conversation - LLM analyzes each
claude "I have 50 pathology reports in ~/pathology-qa/input/ directory (text files).

Use compliance-checker skill to analyze each report with full LLM intelligence:
- Check CAP/ICCR compliance
- Calculate scores
- Identify missing elements
- Cross-validate pT/pN/staging

Export comprehensive results to ~/pathology-qa/output/qa_week_2026_01_13.xlsx with:
- Case ID
- Compliance Score
- Status (Compliant/Minor/Major/Critical)
- Missing Elements
- Recommendations
- Summary statistics

Begin analysis now."
            for i, part in enumerate(parts):
                if '/100' in part:
                    score = part.split('/')[0]
                    return int(score)
    return None

def categorize_status(score):
    """Categorize based on score"""
    if score >= 90:
        return 'COMPLIANT'
    elif score >= 70:
        return 'INCOMPLETE - MINOR'
    elif score >= 50:
        return 'INCOMPLETE - MAJOR'
    else:
        return 'INCOMPLETE - CRITICAL'

def main():
    input_dir = Path('input')
    output_dir = Path('output')
    trends_dir = Path('trends')

    # Results tracking
    results = []

    print(f"Processing reports from {input_dir}...")

    for report_file in input_dir.glob('*.txt'):
        print(f"  Checking {report_file.name}...")

        # Run compliance check
        output = check_report_compliance(report_file)

        # Save full output
        output_file = output_dir / f"{report_file.stem}_qa.txt"
        output_file.write_text(output)

        # Extract score
        score = parse_compliance_score(output)
        status = categorize_status(score) if score else 'UNKNOWN'

        # Track result
        results.append({
            'file': report_file.name,
            'score': score,
            'status': status,
            'date': datetime.now().isoformat()
        })

        print(f"    Score: {score}/100 - {status}")

    # Save results as JSON
    results_file = trends_dir / f"qa_results_{datetime.now().strftime('%Y%m%d')}.json"
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)

    # Generate summary statistics
    total = len(results)
    compliant = sum(1 for r in results if r['score'] and r['score'] >= 90)
    minor = sum(1 for r in results if r['score'] and 70 <= r['score'] < 90)
    major = sum(1 for r in results if r['score'] and 50 <= r['score'] < 70)
    critical = sum(1 for r in results if r['score'] and r['score'] < 50)

    avg_score = sum(r['score'] for r in results if r['score']) / total if total > 0 else 0

    print("\n" + "="*50)
    print("QA SUMMARY")
    print("="*50)
    print(f"Total reports: {total}")
    print(f"Compliant (≥90): {compliant} ({compliant/total*100:.1f}%)")
    print(f"Minor issues (70-89): {minor} ({minor/total*100:.1f}%)")
    print(f"Major issues (50-69): {major} ({major/total*100:.1f}%)")
    print(f"Critical issues (<50): {critical} ({critical/total*100:.1f}%)")
    print(f"\nAverage score: {avg_score:.1f}/100")
    print("="*50)

    # Save summary
    summary_file = trends_dir / f"summary_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(summary_file, 'w') as f:
        f.write(f"QA Summary for {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write(f"Total: {total}, Compliant: {compliant}, Minor: {minor}, Major: {major}, Critical: {critical}\n")
        f.write(f"Average score: {avg_score:.1f}/100\n")

if __name__ == '__main__':
    main()
```

**Step 4: Run Batch QA**
```bash
chmod +x batch_qa.py
python3 batch_qa.py
```

**Step 5: Generate Excel Report**

Create `export_to_excel.py`:
```python
#!/usr/bin/env python3
"""Export QA results to Excel"""

import json
import pandas as pd
from pathlib import Path
from datetime import datetime

def load_all_results():
    """Load all JSON result files"""
    trends_dir = Path('trends')
    all_results = []

    for json_file in sorted(trends_dir.glob('qa_results_*.json')):
        with open(json_file) as f:
            data = json.load(f)
            all_results.extend(data)

    return all_results

def export_to_excel(results):
    """Export results to Excel with formatting"""
    df = pd.DataFrame(results)

    # Convert date strings to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Sort by date
    df = df.sort_values('date')

    # Create Excel writer
    output_file = f"QA_Report_{datetime.now().strftime('%Y%m%d')}.xlsx"
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        # Write main data
        df.to_excel(writer, sheet_name='All Results', index=False)

        # Create summary by status
        summary = df.groupby('status').agg({
            'file': 'count',
            'score': 'mean'
        }).rename(columns={'file': 'count', 'score': 'avg_score'})
        summary.to_excel(writer, sheet_name='Summary by Status')

        # Create trend over time
        df['week'] = df['date'].dt.isocalendar().week
        weekly_trend = df.groupby('week').agg({
            'score': ['mean', 'min', 'max', 'count']
        })
        weekly_trend.to_excel(writer, sheet_name='Weekly Trends')

    print(f"Excel report saved: {output_file}")

if __name__ == '__main__':
    results = load_all_results()
    export_to_excel(results)
```

**Step 6: Run Excel Export**
```bash
pip install pandas openpyxl
python3 export_to_excel.py
```

### Expected Outputs

**Console Output:**
```
Processing reports from input...
  Checking breast_lumpectomy_S2601234.txt...
    Score: 95/100 - COMPLIANT
  Checking colon_resection_S2601235.txt...
    Score: 82/100 - INCOMPLETE - MINOR
  ...

==================================================
QA SUMMARY
==================================================
Total reports: 50
Compliant (≥90): 35 (70.0%)
Minor issues (70-89): 12 (24.0%)
Major issues (50-69): 3 (6.0%)
Critical issues (<50): 0 (0.0%)

Average score: 87.4/100
==================================================
```

**Excel Report (columns):**
- File name
- Score
- Status
- Date
- Tumor type (if parsed)
- Missing elements (if parsed)

---

## 2. Resident Training Program

### Scenario
Teaching pathology fellows proper synoptic reporting using CAP templates and real-time feedback.

### Training Workflow

**Week 1: Introduction to Synoptic Reporting**

**Exercise 1: Generate and Review Blank Templates**
```bash
# Have resident generate templates for different specimens
claude "Generate blank breast lumpectomy template using pathology-template-generator" > templates/breast_lumpectomy.txt
claude "Generate blank colon resection template using pathology-template-generator" > templates/colon_resection.txt
claude "Generate blank Whipple template using pathology-template-generator" > templates/whipple.txt
claude "Generate blank total gastrectomy template using pathology-template-generator" > templates/total_gastrectomy.txt

# Review each template, discuss required vs. conditional vs. recommended elements
```

**Exercise 2: Practice Filling Templates**
```bash
# Provide resident with a case (e.g., breast lumpectomy)
# Have them fill the template manually
# Then check their work

claude "Check this completed breast report using pathology-compliance-checker" < resident_breast_report.txt
```

**Week 2: TNM Staging Practice**

**Exercise 3: Staging Calculations**
```bash
# Quiz: Calculate stages for various pTNM combinations
claude "What stage is pT1c N0 M0 for breast cancer using tnm-stage-calculator?"
claude "What stage is pT3 N1b M0 for colorectal cancer using tnm-stage-calculator?"
claude "What stage is pT2 N1 M0 for pancreatic cancer using tnm-stage-calculator?"
claude "What stage is pT3 N3a M0 for gastric cancer using tnm-stage-calculator?"

# Have resident explain the components and prognostic implications
```

**Week 3: Biomarker Interpretation**

**Exercise 4: Breast Biomarkers**
```bash
# Teach ER/PR/HER2 interpretation
claude "How do I interpret ER 8% positive using breast-pathology-specialist?"
claude "What does HER2 IHC 2+ mean using breast-pathology-specialist?"
claude "When is Ki-67 useful using breast-pathology-specialist?"
```

**Exercise 5: MSI/MMR Testing**
```bash
# Teach Lynch syndrome screening
claude "Interpret MLH1/PMS2 loss using colorectal-pathology-specialist"
claude "What's the next step if MLH1 is lost using colorectal-pathology-specialist?"
claude "How do I screen for Lynch syndrome using colorectal-pathology-specialist?"
```

**Week 4: Complete Case Sign-Out**

**Exercise 6: Full Workflow**
```bash
# Assign complete case, have resident:
# 1. Generate template
claude "Generate breast lumpectomy template for 2.1cm Grade 2 IDC using breast-pathology-specialist"

# 2. Fill in all findings from microscopic review

# 3. Check their report
claude "Check this completed report using breast-pathology-specialist" < resident_complete_report.txt

# 4. Calculate staging
claude "Calculate stage from this report using breast-pathology-specialist" < resident_complete_report.txt

# 5. Generate tumor board summary
claude "Generate tumor board summary using breast-pathology-specialist" < resident_complete_report.txt

# 6. Get SNOMED codes
claude "Get SNOMED codes for this diagnosis using breast-pathology-specialist" < resident_complete_report.txt
```

### Training Assessment Rubric

Track resident progress:
```
Skill Assessment Checklist:
□ Can generate appropriate template for specimen type
□ Identifies all required CAP elements
□ Correctly stages tumors (pTNM → stage group)
□ Interprets biomarkers (ER/PR/HER2, MSI/MMR)
□ Creates compliant synoptic reports (score ≥90)
□ Generates appropriate tumor board summaries
□ Uses correct SNOMED terminology
```

---

## 3. LIS Integration

### Scenario
Automatically suggest SNOMED codes and validate staging in LIS during case sign-out.

### Implementation

**Step 1: LIS Hook Configuration**

Configure LIS to call Claude API when pathologist signs out case:
```python
# lis_hook.py
"""
LIS integration hook for real-time coding suggestions
"""

import os
from anthropic import Anthropic

def get_snomed_codes(diagnosis_text):
    """Get SNOMED codes for diagnosis"""
    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"Get SNOMED codes for: {diagnosis_text} using pathology-coder"
        }]
    )

    return message.content[0].text

def validate_staging(report_text):
    """Validate staging in report"""
    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=2048,
        messages=[{
            "role": "user",
            "content": f"Check staging consistency using tnm-stage-calculator:\n\n{report_text}"
        }]
    )

    return message.content[0].text

# Example usage when pathologist signs out
diagnosis = "Invasive ductal carcinoma, Grade 2, left breast"
codes = get_snomed_codes(diagnosis)
print(codes)

# Auto-populate LIS code fields
# lis.set_morphology_code("408643008")
# lis.set_icd_o3_code("8500/3")
# lis.set_topography_code("C50.9")
```

**Step 2: Real-Time Validation**

When pathologist enters pTNM, validate against tumor size and node count:
```python
def validate_ptnm_on_entry(pt_category, pn_category, tumor_size_cm, nodes_positive, nodes_total):
    """Validate pTNM as pathologist enters data"""

    # Check pT vs size
    if pt_category == "pT1c" and not (1.0 < tumor_size_cm <= 2.0):
        return {
            'valid': False,
            'error': f"pT1c requires tumor >1-2cm, but size is {tumor_size_cm}cm"
        }

    if pt_category == "pT2" and not (2.0 < tumor_size_cm <= 5.0):
        return {
            'valid': False,
            'error': f"pT2 requires tumor >2-5cm, but size is {tumor_size_cm}cm"
        }

    # Check pN vs nodes
    if pn_category == "pN0" and nodes_positive > 0:
        return {
            'valid': False,
            'error': f"pN0 requires 0 positive nodes, but {nodes_positive} positive"
        }

    if pn_category == "pN1a" and not (1 <= nodes_positive <= 3):
        return {
            'valid': False,
            'error': f"pN1a requires 1-3 positive nodes, but {nodes_positive} positive"
        }

    return {'valid': True}

# In LIS, when pathologist enters pTNM:
result = validate_ptnm_on_entry("pT2", "pN1a", 2.3, 2, 15)
if not result['valid']:
    # Show warning dialog
    print(f"⚠️ WARNING: {result['error']}")
```

**Step 3: Auto-Fill Suggestions**

When pathologist enters tumor size, suggest pT:
```python
def suggest_pt_category(tumor_size_cm, tumor_type="breast"):
    """Suggest pT category based on size"""

    if tumor_type == "breast":
        if tumor_size_cm <= 0.1:
            return "pTmi (microinvasion)"
        elif tumor_size_cm <= 0.5:
            return "pT1a"
        elif tumor_size_cm <= 1.0:
            return "pT1b"
        elif tumor_size_cm <= 2.0:
            return "pT1c"
        elif tumor_size_cm <= 5.0:
            return "pT2"
        else:
            return "pT3"

    # Add other tumor types...

    return None

# In LIS, when tumor size field changes:
size = float(lis.get_field("tumor_size"))
suggestion = suggest_pt_category(size, "breast")
lis.suggest_field("pt_category", suggestion)  # Show in UI as suggestion
```

---

## 4. Tumor Board Preparation

### Scenario
Weekly MDT meeting with 20 cases - generate concise summaries for all cases.

### Workflow

**Step 1: Collect Cases for This Week**
```bash
mkdir -p ~/tumor-board/2026-01-20/cases
mkdir -p ~/tumor-board/2026-01-20/summaries

# Export cases from LIS that will be discussed
cp /lis/tumor_board/week_2026_01_20/*.txt ~/tumor-board/2026-01-20/cases/
```

**Step 2: Generate Summaries**

Create `generate_summaries.sh`:
```bash
#!/bin/bash

CASES_DIR="cases"
SUMMARIES_DIR="summaries"

echo "Generating tumor board summaries..."

for case_file in "$CASES_DIR"/*.txt; do
    basename=$(basename "$case_file" .txt)
    echo "  Processing $basename..."

    claude "Generate tumor board summary using pathology-tumor-board-summary" < "$case_file" > "$SUMMARIES_DIR/${basename}_summary.txt"
done

# Combine all summaries into single file
cat "$SUMMARIES_DIR"/*.txt > all_summaries.txt

echo "Done! All summaries saved to all_summaries.txt"
```

**Step 3: Run Summary Generation**
```bash
cd ~/tumor-board/2026-01-20
chmod +x generate_summaries.sh
./generate_summaries.sh
```

**Step 4: Create Presentation Slides**

Convert summaries to PowerPoint format:
```python
# create_slides.py
from pptx import Presentation
from pptx.util import Inches, Pt
from pathlib import Path

def create_tumor_board_presentation(summaries_dir):
    """Create PowerPoint from summaries"""
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    # Title slide
    title_slide = prs.slides.add_slide(prs.slide_layouts[0])
    title = title_slide.shapes.title
    subtitle = title_slide.placeholders[1]
    title.text = "Tumor Board"
    subtitle.text = "January 20, 2026"

    # Add slide for each case
    for summary_file in sorted(Path(summaries_dir).glob('*_summary.txt')):
        slide = prs.slides.add_slide(prs.slide_layouts[1])

        # Case title
        title = slide.shapes.title
        title.text = summary_file.stem.replace('_summary', '').replace('_', ' ').title()

        # Summary content
        content = summary_file.read_text()
        text_box = slide.placeholders[1]
        text_frame = text_box.text_frame
        text_frame.text = content

        # Format text
        for paragraph in text_frame.paragraphs:
            paragraph.font.size = Pt(18)

    # Save presentation
    output_file = "Tumor_Board_2026_01_20.pptx"
    prs.save(output_file)
    print(f"Presentation saved: {output_file}")

if __name__ == '__main__':
    create_tumor_board_presentation('summaries')
```

**Step 5: Generate Presentation**
```bash
pip install python-pptx
python3 create_slides.py
```

### Expected Output

**Slide for Case 1 (Breast):**
```
S26-01234: Breast Lumpectomy

52F with invasive breast carcinoma, left upper outer quadrant.
Lumpectomy: 2.3cm Grade 2 invasive ductal carcinoma, pT2 N1a M0 (Stage IIB).
Margins: Negative (closest 3mm). LVI present. Nodes: 2/15 positive.
Receptors: ER 90%, PR 70%, HER2 negative. Ki-67: 18%.
Resection: R0. Recommend Oncotype DX for chemotherapy decision.
```

---

## 5. Legacy Report Migration

### Scenario
Converting 5000 old narrative reports to synoptic format for database searchability and standardization.

### Workflow

**Step 1: Export Legacy Reports**
```bash
# Export all old reports from LIS
# Assume exported as text files to legacy_reports/

mkdir -p ~/migration/legacy_reports
mkdir -p ~/migration/converted
mkdir -p ~/migration/review_needed
```

**Step 2: Batch Conversion Script**

Create `convert_legacy.py`:
```python
#!/usr/bin/env python3
"""
Convert legacy narrative reports to synoptic format
"""

import subprocess
from pathlib import Path
import json

def convert_report(report_file):
    """Convert single narrative report to synoptic"""
    cmd = f'claude "Convert this report to synoptic format using pathology-report-converter" < {report_file}'
    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    )
    return result.stdout

def extract_conversion_quality(output):
    """Extract conversion quality percentage"""
    for line in output.split('\n'):
        if 'Conversion Quality:' in line:
            # Extract percentage
            parts = line.split(':')
            if len(parts) > 1:
                pct_str = parts[1].strip().split('%')[0].strip()
                try:
                    return int(pct_str)
                except:
                    pass
    return None

def main():
    legacy_dir = Path('legacy_reports')
    converted_dir = Path('converted')
    review_dir = Path('review_needed')

    results = []

    for report_file in legacy_dir.glob('*.txt'):
        print(f"Converting {report_file.name}...")

        # Convert report
        output = convert_report(report_file)

        # Extract quality score
        quality = extract_conversion_quality(output)

        # Save converted report
        if quality and quality >= 75:
            # Good conversion, save to converted/
            output_file = converted_dir / f"{report_file.stem}_synoptic.txt"
        else:
            # Poor conversion, needs manual review
            output_file = review_dir / f"{report_file.stem}_synoptic.txt"

        output_file.write_text(output)

        results.append({
            'file': report_file.name,
            'quality': quality,
            'needs_review': quality is None or quality < 75
        })

        print(f"  Quality: {quality}% - {'REVIEW NEEDED' if quality < 75 else 'OK'}")

    # Save summary
    summary = {
        'total': len(results),
        'good_conversion': sum(1 for r in results if not r['needs_review']),
        'need_review': sum(1 for r in results if r['needs_review']),
        'results': results
    }

    with open('conversion_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)

    print(f"\nConversion complete:")
    print(f"  Total: {summary['total']}")
    print(f"  Good: {summary['good_conversion']} ({summary['good_conversion']/summary['total']*100:.1f}%)")
    print(f"  Need review: {summary['need_review']} ({summary['need_review']/summary['total']*100:.1f}%)")

if __name__ == '__main__':
    main()
```

**Step 3: Run Conversion**
```bash
python3 convert_legacy.py
```

**Step 4: Manual Review Queue**

For reports needing review (quality <75%), create review workflow:
```bash
# List all reports needing review
ls -1 review_needed/ > review_queue.txt

# Assign to pathologists
split -l 50 review_queue.txt review_batch_

# Each pathologist gets a batch to review and complete manually
```

---

## 6. Breast Cancer Center Workflow

### Scenario
High-volume breast cancer center processing 30-40 breast specimens per week with comprehensive biomarker testing.

### Daily Workflow

**Morning: New Cases**
```bash
# For each new breast case, generate pre-filled template
claude "Generate breast lumpectomy template for 1.8cm Grade 2 IDC, 2 positive sentinel nodes using breast-pathology-specialist"

# Pathologist completes remaining fields (margins, LVI, etc.)
```

**Afternoon: Biomarker Results**
```bash
# ER/PR results arrive
claude "Interpret ER 95%, PR 85% using breast-pathology-specialist"

# HER2 results arrive
claude "Interpret HER2 IHC 2+, what's next step using breast-pathology-specialist"

# If HER2 2+, reflex to FISH
# Next day: FISH results
claude "Interpret HER2 FISH: ratio 1.2, not amplified using breast-pathology-specialist"

# Generate addendum
claude "Generate addendum for HER2 FISH results: ratio 1.2, not amplified using breast-pathology-specialist"
```

**End of Day: Final Sign-Out**
```bash
# Check compliance before signing
claude "Final compliance check before sign-out using breast-pathology-specialist" < completed_breast_report.txt

# If score ≥90, proceed with sign-out
# If score <90, fix gaps first

# Generate tumor board summary for weekly conference
claude "Generate breast tumor board summary using breast-pathology-specialist" < final_breast_report.txt

# Get SNOMED codes for LIS
claude "Get SNOMED codes for this breast case using breast-pathology-specialist" < final_breast_report.txt
```

### Weekly Tumor Board

**Tuesday Morning: Prepare Summaries**
```bash
# Generate summaries for all cases to be discussed
cd ~/breast-tumor-board/week-of-2026-01-13/

for case in cases/*.txt; do
  claude "Generate tumor board summary using breast-pathology-specialist" < "$case" > "summaries/$(basename $case .txt)_summary.txt"
done

# Combine into presentation
cat summaries/*.txt > all_breast_summaries.txt
```

### Monthly QA

**First Monday of Month: Department QA**
```bash
# Check all breast cases from last month
for case in /archive/2026-01/*.txt; do
  claude "Check compliance using breast-pathology-specialist" < "$case" >> monthly_qa_2026_01.txt
done

# Generate Excel report with trends
python3 export_to_excel.py monthly_qa_2026_01.txt
```

---

## 7. GI Pathology Fellowship

### Scenario
GI pathology fellow rotating through colorectal, pancreas, and gastric pathology.

### Rotation Schedule

**Weeks 1-4: Colorectal Pathology**

Day 1-2: Learn templates
```bash
claude "Generate blank colon resection template using colorectal-pathology-specialist"
claude "Generate blank rectal LAR template using colorectal-pathology-specialist"
```

Day 3-5: Mesorectal excision assessment
```bash
claude "How do I assess mesorectal excision quality using colorectal-pathology-specialist?"
claude "What is circumferential resection margin using colorectal-pathology-specialist?"
claude "Show me CRM measurement technique using colorectal-pathology-specialist"
```

Day 6-10: MSI/MMR testing
```bash
claude "When should I order MSI testing using colorectal-pathology-specialist?"
claude "Interpret MLH1/PMS2 loss using colorectal-pathology-specialist"
claude "What's the Lynch syndrome screening algorithm using colorectal-pathology-specialist?"
```

Day 11-20: Complete case sign-outs with attending supervision

**Weeks 5-8: Pancreatic Pathology**

Day 1-2: Learn Whipple anatomy
```bash
claude "What are the 7 margins of Whipple using pancreas-pathology-specialist?"
claude "Which margin is most important using pancreas-pathology-specialist?"
```

Day 3-5: Margin assessment practice
```bash
claude "How do I measure posterior margin using pancreas-pathology-specialist?"
claude "What is R0 vs R1 resection using pancreas-pathology-specialist?"
```

Day 6-10: Vascular involvement
```bash
claude "How do I assess SMA involvement using pancreas-pathology-specialist?"
claude "What does pT4 mean for pancreas using pancreas-pathology-specialist?"
```

**Weeks 9-12: Gastric Pathology**

Day 1-2: Lauren classification
```bash
claude "What is Lauren classification using gastric-pathology-specialist?"
claude "How do I distinguish intestinal from diffuse type using gastric-pathology-specialist?"
```

Day 3-5: GEJ tumors
```bash
claude "What is Siewert classification using gastric-pathology-specialist?"
claude "How do I measure distance from GEJ using gastric-pathology-specialist?"
```

Day 6-10: HER2 testing
```bash
claude "When do I order HER2 testing for gastric cancer using gastric-pathology-specialist?"
claude "How is HER2 scoring different in gastric vs breast using gastric-pathology-specialist?"
```

### Fellowship Assessment

Track fellow's progress with skills:
```
Competency Checklist:

Colorectal:
□ Can generate appropriate colorectal template
□ Assesses mesorectal excision quality correctly
□ Measures CRM accurately
□ Orders MSI/MMR testing appropriately
□ Interprets MMR IHC correctly
□ Stages colorectal cancer accurately (AJCC 8th)

Pancreas:
□ Identifies all 7 Whipple margins
□ Measures margins accurately
□ Classifies R0 vs R1 correctly
□ Assesses vascular involvement
□ Calculates lymph node ratio
□ Stages pancreatic cancer accurately

Gastric:
□ Applies Lauren classification correctly
□ Uses Siewert classification for GEJ tumors
□ Measures distance from GEJ
□ Applies Borrmann typing
□ Orders HER2 testing appropriately
□ Stages gastric cancer accurately
```

---

## 8. Post-Neoadjuvant Assessment

### Scenario
Assessing treatment response in post-neoadjuvant resection specimens (breast, rectal, pancreatic).

### Breast Post-Neoadjuvant

**Case: Status Post AC-T + Trastuzumab**

```bash
# Generate template with treatment effect section
claude "Generate post-neoadjuvant mastectomy template using breast-pathology-specialist"

# Assess treatment response
# If no residual tumor:
claude "How do I report pathologic complete response using breast-pathology-specialist?"

# If residual tumor:
claude "How do I calculate residual cancer burden (RCB) using breast-pathology-specialist?"

# Stage as ypTNM
claude "What does ypT0 ypN0 mean using breast-pathology-specialist?"
```

**Template Output Includes:**
```
TREATMENT EFFECT (POST-NEOADJUVANT)
───────────────────────────────────────
Neoadjuvant Therapy: AC-T + trastuzumab

Response Assessment:
  (_) Pathologic complete response (pCR): No residual invasive carcinoma
  (_) Residual invasive carcinoma present

If residual tumor:
  Tumor bed size: ___ cm
  Residual tumor size: ___ cm
  CAP Regression Score:
    (_) Score 0: No viable tumor cells (pCR)
    (_) Score 1: Only scattered tumor cells
    (_) Score 2: Residual tumor with therapy effect
    (_) Score 3: No definite therapy effect

  Residual Cancer Burden (RCB):
    Cellularity: ___%
    RCB Score: ___ (RCB-0, RCB-I, RCB-II, RCB-III)
```

### Rectal Post-Neoadjuvant

**Case: Status Post Long-Course Chemoradiation**

```bash
# Generate template with treatment effect
claude "Generate post-neoadjuvant rectal APR template using colorectal-pathology-specialist"

# Assess tumor regression grade
claude "How do I grade tumor regression using colorectal-pathology-specialist?"

# Special considerations
claude "Does mesorectal excision quality matter after neoadjuvant therapy using colorectal-pathology-specialist?"
```

---

## Summary of Use Cases

| Use Case | Primary Skills Used | Frequency | Automation Level |
|----------|-------------------|-----------|------------------|
| Department QA | compliance-checker | Weekly | High (batch scripts) |
| Resident Training | template-generator, tnm-stage-calculator | Daily | Low (interactive) |
| LIS Integration | pathology-coder, tnm-stage-calculator | Per case | High (API hooks) |
| Tumor Board | tumor-board-summary | Weekly | High (batch scripts) |
| Legacy Migration | report-converter | One-time project | Medium (semi-automated) |
| Breast Center | breast-specialist | Daily | Medium (templates + checks) |
| GI Fellowship | colorectal/pancreas/gastric-specialist | Rotation | Low (learning tool) |
| Post-Neoadjuvant | Specialist skills | Per case | Low (complex assessment) |

---

Ready to implement these workflows in your practice!
