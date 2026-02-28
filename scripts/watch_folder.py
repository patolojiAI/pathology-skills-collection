#!/usr/bin/env python3
"""
Pathology Report Watch Folder
Monitors a directory for new reports and automatically processes them for CAP/ICCR compliance.

Usage:
    python watch_folder.py /path/to/watch --output /path/to/results
    python watch_folder.py /path/to/watch --output /path/to/results --interval 30
    python watch_folder.py /path/to/watch --output /path/to/results --mode synoptic

Requirements:
    pip install anthropic watchdog openpyxl

Features:
    - Monitors folder for new files (txt, pdf, docx, images)
    - Processes new reports automatically
    - Generates QA reports, synoptic conversions, or summaries
    - Logs all activity
    - Supports multiple output formats
"""

import os
import sys
import time
import json
import logging
import argparse
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, List, Set

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler, FileCreatedEvent
    WATCHDOG_AVAILABLE = True
except ImportError:
    WATCHDOG_AVAILABLE = False

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


# Supported file extensions
SUPPORTED_EXTENSIONS = {
    '.txt', '.md',           # Plain text
    '.pdf',                   # PDF documents
    '.docx', '.doc',          # Word documents
    '.jpg', '.jpeg', '.png',  # Scanned images
    '.tiff', '.tif'           # TIFF images
}


class ProcessedFilesTracker:
    """Track processed files to avoid reprocessing."""
    
    def __init__(self, tracker_path: Path):
        self.tracker_path = tracker_path
        self.processed: Dict[str, str] = {}  # filename -> hash
        self._load()
    
    def _load(self):
        """Load processed files from disk."""
        if self.tracker_path.exists():
            try:
                with open(self.tracker_path, 'r') as f:
                    self.processed = json.load(f)
            except Exception as e:
                logger.warning(f"Could not load tracker file: {e}")
                self.processed = {}
    
    def _save(self):
        """Save processed files to disk."""
        try:
            with open(self.tracker_path, 'w') as f:
                json.dump(self.processed, f, indent=2)
        except Exception as e:
            logger.error(f"Could not save tracker file: {e}")
    
    def get_file_hash(self, filepath: Path) -> str:
        """Get MD5 hash of file contents."""
        hasher = hashlib.md5()
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                hasher.update(chunk)
        return hasher.hexdigest()
    
    def is_processed(self, filepath: Path) -> bool:
        """Check if file has already been processed."""
        filename = str(filepath)
        if filename not in self.processed:
            return False
        # Check if file has changed
        current_hash = self.get_file_hash(filepath)
        return self.processed[filename] == current_hash
    
    def mark_processed(self, filepath: Path):
        """Mark file as processed."""
        self.processed[str(filepath)] = self.get_file_hash(filepath)
        self._save()


class ReportProcessor:
    """Process pathology reports using Claude API."""
    
    def __init__(self, mode: str = 'compliance', model: str = 'claude-sonnet-4-20250514'):
        self.mode = mode
        self.model = model
        self.client = anthropic.Anthropic() if ANTHROPIC_AVAILABLE else None
        
        # Mode-specific prompts
        self.prompts = {
            'compliance': self._get_compliance_prompt(),
            'synoptic': self._get_synoptic_prompt(),
            'summary': self._get_summary_prompt(),
            'autofill': self._get_autofill_prompt()
        }
    
    def _get_compliance_prompt(self) -> str:
        return """Analyze this pathology report for CAP/ICCR compliance.

For each required element, check if it is:
- PRESENT: Element found with value
- MISSING: Element not mentioned
- EMPTY: Element label exists but value blank

Classify issues by severity:
- CRITICAL: Required for staging/treatment (pT, pN, margins, grade, receptors)
- MAJOR: Core prognostic elements (LVI, PNI, tumor size, node counts)
- MINOR: Recommended elements (focality, gross details)

Calculate compliance score:
Score = 100 - (Critical × 15) - (Major × 5) - (Minor × 2)

Output format:
1. TUMOR TYPE IDENTIFIED
2. COMPLIANCE SCORE
3. MISSING ELEMENTS (by severity)
4. CROSS-VALIDATION ISSUES
5. RECOMMENDATIONS

Report text:
"""

    def _get_synoptic_prompt(self) -> str:
        return """Convert this free-text pathology report to CAP-compliant synoptic format.

Extract all available elements and format as:

SYNOPTIC REPORT
═══════════════════════════════════════════════════════════════

SPECIMEN
Procedure: ____
Laterality: ____ (if applicable)

TUMOR
Histologic Type: ____
Histologic Grade: ____
Tumor Size: ____ cm

MARGINS
Status: ____
Closest Margin: ____ Distance: ____ mm

LYMPH NODES
Total Examined: ____
Total Positive: ____

PATHOLOGIC STAGING (AJCC 8th Edition)
pT: ____  pN: ____  pM: ____
Stage Group: ____

ADDITIONAL FINDINGS
Lymphovascular Invasion: ____
Perineural Invasion: ____

BIOMARKERS
[Tumor-specific fields]

═══════════════════════════════════════════════════════════════

Mark any elements not found as "Not specified".

Report text:
"""

    def _get_summary_prompt(self) -> str:
        return """Generate a concise 3-5 line tumor board summary from this pathology report.

Format:
[Age][Sex] with [TUMOR TYPE] of the [SITE/LOCATION].
[PROCEDURE]: [SIZE] [HISTOLOGIC TYPE], [GRADE], [STAGE (pTNM)].
Margins: [STATUS]. LVI: [+/-]. PNI: [+/-]. Nodes: [X/Y positive].
Biomarkers: [KEY RESULTS].

Report text:
"""

    def _get_autofill_prompt(self) -> str:
        return """Analyze this pathology report and suggest values for any missing staging elements.

For each suggestion, provide:
- Field name
- Suggested value
- Rationale based on report findings
- Confidence level (High/Medium/Low)

Focus on:
1. pT category (based on tumor size/depth)
2. pN category (based on node counts)
3. Stage group (based on pTNM)
4. Grade (based on differentiation)

Report text:
"""

    def process(self, report_text: str) -> Dict:
        """Process a report and return results."""
        if not self.client:
            return {
                'success': False,
                'error': 'Anthropic client not available. Set ANTHROPIC_API_KEY.',
                'mode': self.mode
            }
        
        prompt = self.prompts.get(self.mode, self.prompts['compliance'])
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4096,
                messages=[
                    {
                        'role': 'user',
                        'content': prompt + report_text
                    }
                ]
            )
            
            return {
                'success': True,
                'mode': self.mode,
                'result': response.content[0].text,
                'model': self.model,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'mode': self.mode
            }


class ReportHandler(FileSystemEventHandler):
    """Handle new file events in watched directory."""
    
    def __init__(self, processor: ReportProcessor, output_dir: Path, 
                 tracker: ProcessedFilesTracker):
        self.processor = processor
        self.output_dir = output_dir
        self.tracker = tracker
        self.processing_queue: Set[str] = set()
    
    def on_created(self, event):
        """Handle new file creation."""
        if event.is_directory:
            return
        
        filepath = Path(event.src_path)
        
        # Check extension
        if filepath.suffix.lower() not in SUPPORTED_EXTENSIONS:
            return
        
        # Avoid duplicate processing
        if str(filepath) in self.processing_queue:
            return
        
        # Wait for file to be fully written
        time.sleep(1)
        
        self.process_file(filepath)
    
    def process_file(self, filepath: Path):
        """Process a single file."""
        # Check if already processed
        if self.tracker.is_processed(filepath):
            logger.info(f"Skipping already processed: {filepath.name}")
            return
        
        self.processing_queue.add(str(filepath))
        logger.info(f"Processing: {filepath.name}")
        
        try:
            # Read file content
            report_text = self._read_file(filepath)
            
            if not report_text:
                logger.warning(f"Could not read content from: {filepath.name}")
                return
            
            # Process with Claude
            result = self.processor.process(report_text)
            
            # Save result
            self._save_result(filepath, result)
            
            # Mark as processed
            self.tracker.mark_processed(filepath)
            
            if result['success']:
                logger.info(f"Completed: {filepath.name}")
            else:
                logger.error(f"Failed: {filepath.name} - {result.get('error', 'Unknown error')}")
                
        except Exception as e:
            logger.error(f"Error processing {filepath.name}: {e}")
        finally:
            self.processing_queue.discard(str(filepath))
    
    def _read_file(self, filepath: Path) -> Optional[str]:
        """Read content from various file types."""
        suffix = filepath.suffix.lower()
        
        if suffix in {'.txt', '.md'}:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        
        elif suffix == '.pdf':
            try:
                import pypdf
                reader = pypdf.PdfReader(filepath)
                text = ''
                for page in reader.pages:
                    text += page.extract_text() + '\n'
                return text
            except ImportError:
                logger.warning("pypdf not installed. Cannot read PDF files.")
                return None
        
        elif suffix in {'.docx', '.doc'}:
            try:
                import docx
                doc = docx.Document(filepath)
                return '\n'.join([para.text for para in doc.paragraphs])
            except ImportError:
                logger.warning("python-docx not installed. Cannot read Word files.")
                return None
        
        elif suffix in {'.jpg', '.jpeg', '.png', '.tiff', '.tif'}:
            # For images, return placeholder - would need OCR or vision API
            logger.info(f"Image file detected: {filepath.name} - requires vision processing")
            return f"[Image file: {filepath.name} - content extraction not implemented]"
        
        return None
    
    def _save_result(self, source_file: Path, result: Dict):
        """Save processing result to output directory."""
        # Create output filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        mode = result.get('mode', 'unknown')
        output_name = f"{source_file.stem}_{mode}_{timestamp}.txt"
        output_path = self.output_dir / output_name
        
        # Format output
        output_lines = [
            "=" * 70,
            f"PATHOLOGY REPORT ANALYSIS",
            "=" * 70,
            f"Source File: {source_file.name}",
            f"Processing Mode: {mode}",
            f"Timestamp: {result.get('timestamp', 'N/A')}",
            f"Model: {result.get('model', 'N/A')}",
            f"Status: {'Success' if result['success'] else 'Failed'}",
            "=" * 70,
            ""
        ]
        
        if result['success']:
            output_lines.append(result['result'])
        else:
            output_lines.append(f"ERROR: {result.get('error', 'Unknown error')}")
        
        # Write output
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(output_lines))
        
        logger.info(f"Result saved: {output_path.name}")


def process_existing_files(watch_dir: Path, handler: ReportHandler):
    """Process any existing files in the watch directory."""
    logger.info("Checking for existing files...")
    
    for filepath in watch_dir.iterdir():
        if filepath.is_file() and filepath.suffix.lower() in SUPPORTED_EXTENSIONS:
            if not handler.tracker.is_processed(filepath):
                handler.process_file(filepath)


def run_polling_mode(watch_dir: Path, handler: ReportHandler, interval: int):
    """Run in polling mode without watchdog."""
    logger.info(f"Running in polling mode (interval: {interval}s)")
    
    processed_files: Set[str] = set()
    
    try:
        while True:
            for filepath in watch_dir.iterdir():
                if filepath.is_file() and filepath.suffix.lower() in SUPPORTED_EXTENSIONS:
                    file_key = f"{filepath}:{filepath.stat().st_mtime}"
                    if file_key not in processed_files:
                        if not handler.tracker.is_processed(filepath):
                            handler.process_file(filepath)
                        processed_files.add(file_key)
            
            time.sleep(interval)
            
    except KeyboardInterrupt:
        logger.info("Polling stopped by user")


def main():
    parser = argparse.ArgumentParser(
        description='Watch folder for pathology reports and process automatically'
    )
    parser.add_argument(
        'watch_dir',
        type=str,
        help='Directory to watch for new reports'
    )
    parser.add_argument(
        '--output', '-o',
        type=str,
        default=None,
        help='Output directory for results (default: watch_dir/results)'
    )
    parser.add_argument(
        '--mode', '-m',
        type=str,
        choices=['compliance', 'synoptic', 'summary', 'autofill'],
        default='compliance',
        help='Processing mode (default: compliance)'
    )
    parser.add_argument(
        '--interval', '-i',
        type=int,
        default=10,
        help='Polling interval in seconds (default: 10)'
    )
    parser.add_argument(
        '--model',
        type=str,
        default='claude-sonnet-4-20250514',
        help='Claude model to use (default: claude-sonnet-4-20250514)'
    )
    parser.add_argument(
        '--process-existing',
        action='store_true',
        help='Process existing files in directory on startup'
    )
    parser.add_argument(
        '--no-watch',
        action='store_true',
        help='Process existing files only, do not watch for new files'
    )
    
    args = parser.parse_args()
    
    # Validate watch directory
    watch_dir = Path(args.watch_dir)
    if not watch_dir.exists():
        logger.error(f"Watch directory does not exist: {watch_dir}")
        sys.exit(1)
    
    # Setup output directory
    output_dir = Path(args.output) if args.output else watch_dir / 'results'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Setup tracker
    tracker_path = output_dir / '.processed_files.json'
    tracker = ProcessedFilesTracker(tracker_path)
    
    # Setup processor
    if not ANTHROPIC_AVAILABLE:
        logger.error("anthropic package not installed. Run: pip install anthropic")
        sys.exit(1)
    
    if not os.environ.get('ANTHROPIC_API_KEY'):
        logger.error("ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
    
    processor = ReportProcessor(mode=args.mode, model=args.model)
    handler = ReportHandler(processor, output_dir, tracker)
    
    logger.info(f"Watch directory: {watch_dir}")
    logger.info(f"Output directory: {output_dir}")
    logger.info(f"Processing mode: {args.mode}")
    
    # Process existing files if requested
    if args.process_existing or args.no_watch:
        process_existing_files(watch_dir, handler)
    
    # Exit if no-watch mode
    if args.no_watch:
        logger.info("Processing complete (no-watch mode)")
        return
    
    # Start watching
    if WATCHDOG_AVAILABLE:
        logger.info("Starting file watcher...")
        observer = Observer()
        observer.schedule(handler, str(watch_dir), recursive=False)
        observer.start()
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Stopping watcher...")
            observer.stop()
        observer.join()
    else:
        logger.warning("watchdog package not installed. Using polling mode.")
        run_polling_mode(watch_dir, handler, args.interval)


if __name__ == '__main__':
    main()
