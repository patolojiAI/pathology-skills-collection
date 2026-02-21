# Example Files for Testing Pathology Skills

This directory contains sample pathology reports in various formats for testing the skills collection.

## 📁 Directory Structure

```
examples/
├── README.md                    # This file
├── text/                        # Plain text reports
│   ├── breast_lumpectomy.txt
│   ├── colorectal_resection.txt
│   ├── pancreas_whipple.txt
│   └── gastric_gastrectomy.txt
├── excel/                       # Excel batch and structured formats
│   ├── batch_reports.xlsx       # Multiple reports (one per row)
│   ├── structured_breast.xlsx   # Single report (field-value pairs)
│   └── template_batch.xlsx      # Template for batch processing
├── csv/                         # CSV batch format
│   └── batch_reports.csv
└── sample-inputs/               # Additional samples
```

## 🧪 Testing Each Format

### Text Files (`.txt`)

```bash
# Test single text report
claude "Check this breast report using breast-specialist" < examples/text/breast_lumpectomy.txt

# Test compliance checking
claude "Validate this colorectal report using compliance-checker" < examples/text/colorectal_resection.txt
```

### Excel Batch (`.xlsx` - one report per row)

```bash
# Batch process multiple reports
python cli-tools/process_skill.py --skill compliance-checker examples/excel/batch_reports.xlsx --output results/

# Process with specific skill
python cli-tools/process_skill.py --skill breast-specialist examples/excel/batch_reports.xlsx --output results/
```

### Excel Structured (`.xlsx` - field-value pairs)

```bash
# Process single structured report
python cli-tools/process_skill.py --skill breast-specialist examples/excel/structured_breast.xlsx --output results/
```

### CSV Batch (`.csv`)

```bash
# Process CSV batch
python cli-tools/process_skill.py --skill colorectal-specialist examples/csv/batch_reports.csv --output results/
```

### PDF Files (requires vision API or pypdf)

```bash
# Process PDF report
python cli-tools/process_skill.py --skill pancreas-specialist examples/pdf/pancreas_report.pdf --output results/
```

### Images (requires vision API)

```bash
# Process scanned report image
python cli-tools/process_skill.py --skill gastric-specialist examples/images/gastric_scan.jpg --output results/
```

## 📝 Sample Report Types

### Breast Cancer
- **Lumpectomy**: Invasive ductal carcinoma, partial mastectomy
- **Mastectomy**: Total mastectomy with axillary dissection
- **Sentinel node biopsy**: With or without metastases

### Colorectal Cancer
- **Right hemicolectomy**: Cecal/ascending colon carcinoma
- **Left hemicolectomy**: Descending/sigmoid colon carcinoma
- **Anterior resection**: Rectal carcinoma with TME
- **Polypectomy**: For smaller lesions

### Pancreas Cancer
- **Whipple procedure**: Pancreaticoduodenectomy for head tumors
- **Distal pancreatectomy**: For body/tail tumors
- **Biopsy**: Core or FNA specimens

### Gastric Cancer
- **Total gastrectomy**: For proximal or diffuse tumors
- **Partial gastrectomy**: For distal tumors
- **Biopsy**: Endoscopic biopsy specimens

## 🔧 Creating Your Own Test Files

### Text File Format

```
PATHOLOGY REPORT

Patient: [ID/Name]
Specimen: [Procedure type]

FINAL DIAGNOSIS:
- [Main diagnosis]
- Tumor size: [measurements]
- Histologic type: [type]
- Grade: [grading]
- Margins: [margin status]
- Lymph nodes: [node status]
- [Additional findings]

STAGING: pT[X] pN[X] pM[X]
```

### Excel Batch Format

| report_text | patient_id | tumor_type |
|-------------|------------|------------|
| Full report text here... | P001 | breast |
| Full report text here... | P002 | colorectal |

### Excel Structured Format

| Field | Value |
|-------|-------|
| Procedure | Total mastectomy |
| Tumor Size | 2.3 cm |
| Histologic Type | Invasive ductal carcinoma |
| Grade | G2 |
| ER Status | Positive (95%) |
| PR Status | Positive (80%) |
| HER2 Status | Negative (IHC 1+) |

## ⚠️ Privacy Notice

**All example files contain fictional data only.**

- No real patient information
- Synthetic clinical data
- For testing purposes only

**Never commit real patient data to this repository!**

## 📖 Additional Resources

- [Getting Started Guide](../docs/getting-started.md)
- [Skills Reference](../docs/pathology-skills.md)
- [Examples & Workflows](../docs/examples.md)
- [Quick Start Local](../QUICK_START_LOCAL.md)
