# Multi-Format File Support Guide
## Pathology Skills Collection

**Last Updated:** 2026-01-17

---

## Overview

All pathology skills in this collection now support processing reports in multiple file formats:
- Plain text (`.txt`, `.md`)
- Excel spreadsheets (`.xlsx`, `.xls`) - batch and structured modes
- CSV files (`.csv`)
- PDF documents (`.pdf`) - with Claude Vision API
- Images (`.jpg`, `.png`, `.tiff`) - scanned reports via Vision API
- Word documents (`.docx`)

---

## Quick Start

### Process a Single PDF
```bash
cd /path/to/pathology-skills-collection
python scripts/process_skill.py --skill colorectal-pathology-specialist report.pdf --output results/
```

### Process Excel Batch List
```bash
python scripts/process_skill.py --skill breast-pathology-specialist reports.xlsx --output results/
```

### Process Directory with Mixed Formats
```bash
python scripts/process_skill.py --skill pathology-compliance-checker input_dir/ --output results/
```

---

## Supported Input Formats

### 1. Plain Text Files (`.txt`, `.md`)
**Best for:** Interactive use, single reports, copy-paste

**Usage:**
```bash
claude "Check this report using pathology-colorectal-pathology-specialist" < report.txt
```

**Pros:**
- Fastest processing
- No dependencies
- Works offline

---

### 2. Excel Batch Lists (`.xlsx`, `.xls`)
**Best for:** Processing multiple reports from a database or LIS export

**Required columns:**
- `report_text` (required): Full pathology report text
- `patient_id` (optional): Patient/case identifier
- `tumor_type` (optional): breast, colorectal, gastric, pancreas

**Example Excel structure:**

| report_text | patient_id | tumor_type |
|-------------|------------|------------|
| PATHOLOGY REPORT<br>Specimen: Total mastectomy...<br>Tumor size: 2.3 cm... | P12345 | breast |
| PATHOLOGY REPORT<br>Specimen: Right hemicolectomy...<br>Tumor size: 4.5 cm... | P12346 | colorectal |
| PATHOLOGY REPORT<br>Specimen: Whipple procedure...<br>Tumor size: 3.2 cm... | P12347 | pancreas |

**Usage:**
```bash
python scripts/process_skill.py --skill pathology-compliance-checker batch_reports.xlsx --output results/
```

**Output:**
- Individual QA text files for each report
- Combined Excel workbook with:
  - Summary sheet (statistics)
  - All Results sheet (per-report scores)
  - Gap Analysis sheet (common missing elements)
  - Details sheet (full analysis text)

**Pros:**
- Process hundreds of reports at once
- Easy database export
- Structured output for tracking

---

### 3. Excel Structured Reports (`.xlsx`, `.xls`)
**Best for:** LIS exports with pre-filled fields, structured data entry

**Format:** Two-column layout
- Column A: Field names
- Column B: Values

**Example:**

| Field | Value |
|-------|-------|
| Procedure | Total mastectomy |
| Tumor Site | Upper outer quadrant |
| Tumor Size | 2.3 cm |
| Histologic Type | Invasive ductal carcinoma |
| Histologic Grade | G2 |
| Surgical Margins | Negative (>5mm all margins) |
| ER Status | Positive (95%) |
| PR Status | Positive (80%) |
| HER2 Status | Negative |
| pT Category | pT2 |
| pN Category | pN1a |

**Auto-detection:** The skill automatically detects this format (2 columns, field-value pairs)

**Usage:**
```bash
python scripts/process_skill.py --skill breast-pathology-specialist structured_report.xlsx --output results/
```

---

### 4. CSV Files (`.csv`)
**Best for:** Database exports, compatibility with non-Excel systems

**Same format as Excel batch lists** (with `report_text` column)

**Usage:**
```bash
python scripts/process_skill.py --skill pancreas-pathology-specialist reports.csv --output results/
```

---

### 5. PDF Files (`.pdf`)
**Best for:** Digital pathology reports, exported from LIS/EMR, scanned documents

**Processing:**
1. **Fast extraction** (pypdf): For clean, digital PDFs
2. **Vision API fallback**: For scanned or complex PDFs where text extraction fails

**Usage:**
```bash
# Interactive
claude "Analyze this colorectal PDF using pathology-colorectal-pathology-specialist" < report.pdf

# Batch
python scripts/process_skill.py --skill gastric-pathology-specialist report.pdf --output results/
```

**Pros:**
- Handles both digital and scanned PDFs
- Automatic fallback to vision API
- Multi-page support

**Notes:**
- Vision API costs ~$0.045 per page (Claude Sonnet 4)
- Clean PDFs use free pypdf extraction when possible

---

### 6. Images (`.jpg`, `.png`, `.tiff`)
**Best for:** Scanned paper reports, mobile phone photos of reports

**Processing:** Claude Vision API extracts text from images

**Supported:**
- Typed/printed text (high accuracy)
- Clear scans or photos
- Standard pathology report layouts

**Not recommended:**
- Handwritten reports (lower accuracy)
- Very low quality images
- Complex layouts with tables/diagrams

**Usage:**
```bash
# Interactive
claude "Extract and check this scanned report" < scan.jpg

# Batch
python scripts/process_skill.py --skill breast-pathology-specialist scanned_reports/ --output results/
```

**Pros:**
- No scanner software needed
- Works with phone photos
- Preserves formatting context

**Costs:**
- ~$0.045 per image (Claude Sonnet 4, typical pathology report)

---

### 7. Word Documents (`.docx`)
**Best for:** Office-generated reports, editable documents

**Processing:** Extracts paragraphs using python-docx library

**Usage:**
```bash
python scripts/process_skill.py --skill pathology-compliance-checker report.docx --output results/
```

---

## Installation

### Core Dependencies (Required)
```bash
pip install anthropic pandas openpyxl
```

### Enhanced Features (Optional)
```bash
pip install pypdf python-docx watchdog tqdm pillow
```

### All Dependencies
```bash
cd pathology-skills-collection
pip install -r requirements.txt
```

---

## CLI Tool Usage

### Basic Syntax
```bash
python scripts/process_skill.py --skill SKILL_NAME INPUT_PATH [OPTIONS]
```

### Available Skills
- `breast-pathology-specialist` - Breast cancer pathology
- `colorectal-pathology-specialist` - Colorectal cancer pathology
- `gastric-pathology-specialist` - Gastric cancer pathology
- `pancreas-pathology-specialist` - Pancreatic cancer pathology
- `pathology-compliance-checker` - Multi-tumor CAP/ICCR compliance
- `pathology-template-generator` - Synoptic template generation
- `tnm-stage-calculator` - TNM staging calculator
- `pathology-tumor-board-summary` - Tumor board summary generator
- `pathology-coder` - SNOMED/ICD-O-3 coding
- `report-converter` - Free-text to synoptic converter

### Options
- `--output DIR` - Output directory (default: `results/`)
- `--api-key KEY` - Anthropic API key (or set `ANTHROPIC_API_KEY` env var)

### Examples

**Single file:**
```bash
python scripts/process_skill.py --skill breast-pathology-specialist report.pdf --output qa_results/
```

**Excel batch:**
```bash
python scripts/process_skill.py --skill colorectal-pathology-specialist batch.xlsx --output qa_results/
```

**Directory (all formats):**
```bash
python scripts/process_skill.py --skill pathology-compliance-checker input_dir/ --output qa_results/
```

**With custom API key:**
```bash
python scripts/process_skill.py --skill pancreas-pathology-specialist report.jpg --api-key sk-ant-...
```

---

## Output Formats

### For Single Reports
- `{filename}_qa.txt` - Detailed compliance analysis

### For Batch Processing
- `{filename}_row{N}_{patient_id}_qa.txt` - Individual QA reports
- `{filename}_batch_results.xlsx` - Multi-sheet Excel workbook:
  - **Summary**: Overall statistics, compliance distribution
  - **All Results**: Per-report compliance scores and gaps
  - **Gap Analysis**: Most common missing elements ranked by frequency
  - **Details**: Full analysis text for each report

### For Directory Processing
- Individual QA reports for each file
- `{dirname}_all_results.xlsx` - Combined results from all files

---

## Performance & Costs

### Processing Speed
| Format | Speed | Notes |
|--------|-------|-------|
| Text | ~1 sec/report | Fastest |
| Excel (batch) | ~2 sec/report | Batch efficiency |
| PDF (pypdf) | ~2 sec/report | Fast text extraction |
| PDF (vision) | ~5 sec/report | Vision API processing |
| Images | ~5 sec/report | Vision API processing |

**Throughput:** ~100 mixed-format reports in <10 minutes

### Claude API Costs (Sonnet 4)
| Format | Cost per Report | Notes |
|--------|----------------|-------|
| Text | ~$0.01 | Baseline |
| Excel | ~$0.01 | Same as text |
| PDF (pypdf) | ~$0.01 | Free extraction + analysis |
| PDF (vision) | ~$0.05 | Vision tokens + analysis |
| Images | ~$0.05 | Vision tokens + analysis |

**Cost optimization:**
- pypdf extracts text for free (clean PDFs)
- Vision API only for poor extractions
- Batch processing shares reference loading

---

## Troubleshooting

### "anthropic package not installed"
```bash
pip install anthropic
```

### "pandas required for Excel support"
```bash
pip install pandas openpyxl
```

### "Claude client required for image processing"
**Cause:** Vision API needs authenticated client

**Solution:** Set API key
```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

### "Excel must have 'report_text' column"
**Cause:** Batch Excel missing required column

**Solution:** Add `report_text` column with report text, or use structured format (2 columns)

### Vision API Errors
**Cause:** Network issues, invalid API key, file too large

**Solutions:**
- Check API key: `echo $ANTHROPIC_API_KEY`
- Check internet connection
- Reduce image file size (<5MB recommended)
- Check image format (use .jpg, .png, .tiff)

---

## Advanced Usage

### Batch Excel with Auto-Detect Tumor Type
**Excel file:**
| report_text | patient_id |
|-------------|------------|
| ...mastectomy...invasive ductal... | P001 |
| ...hemicolectomy...adenocarcinoma... | P002 |

**Processing:**
```bash
python scripts/process_skill.py --skill pathology-compliance-checker auto_detect.xlsx --output results/
```

The skill will auto-detect "breast" for P001 and "colorectal" for P002.

### Process Only Images from Directory
```bash
# Manual filtering
mkdir images_only
cp input_dir/*.jpg input_dir/*.png images_only/
python scripts/process_skill.py --skill breast-pathology-specialist images_only/ --output results/
```

### Combine Results from Multiple Skills
Process same reports with different skills:
```bash
python scripts/process_skill.py --skill breast-pathology-specialist reports.xlsx --output results/breast/
python scripts/process_skill.py --skill pathology-compliance-checker reports.xlsx --output results/compliance/
python scripts/process_skill.py --skill pathology-template-generator reports.xlsx --output results/templates/
```

---

## API Integration

### Python Script Example
```python
import sys
sys.path.append('/path/to/pathology-skills-collection')

from shared_scripts.file_readers import read_file_content
import anthropic

# Initialize client
client = anthropic.Anthropic(api_key="your-api-key")

# Read any format
content = read_file_content(
    filepath="report.pdf",
    client=client,
    use_vision=True
)

# Process with skill
# (load skill references, analyze with Claude API...)
```

---

## FAQ

**Q: Can I process handwritten reports?**
A: Vision API can attempt it, but accuracy is lower. Typed/printed text recommended.

**Q: What's the maximum file size?**
A: Images: ~5MB. PDFs: ~25 pages. Excel: ~1000 rows.

**Q: Do I need pypdf installed?**
A: No, but recommended for faster PDF processing. Vision API is fallback.

**Q: Can I process .doc (old Word format)?**
A: Use .docx. Convert .doc to .docx first.

**Q: How do I reduce vision API costs?**
A: Use text files when possible, ensure PDFs are clean (pypdf extraction), batch process for efficiency.

**Q: Can skills process reports in Turkish?**
A: Yes, all skills support English and Turkish.

---

## Updates and Changelog

### 2026-01-17: Multi-Format Support Added
- ✅ Added Excel batch processing
- ✅ Added Excel structured report support
- ✅ Added PDF support (pypdf + vision fallback)
- ✅ Added image support (vision API)
- ✅ Added CSV support
- ✅ Created `scripts/process_skill.py`
- ✅ Created `scripts/` library (file_readers, excel_handler)
- ✅ Updated all 10 skill SKILL.md files

---

## Support

For issues or questions:
1. Check [Troubleshooting](#troubleshooting) section
2. Review [examples/](../examples/) for sample files
3. Open GitHub issue with:
   - File format used
   - Error message
   - Sample input (de-identified)

---

Complete multi-format support for all pathology skills!
