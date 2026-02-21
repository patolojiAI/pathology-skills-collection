---
name: tumor-board-summary
description: Generates concise 3-5 line tumor board summaries from pathology reports with key clinical elements (diagnosis, TNM stage, margins, nodes, biomarkers). For MDT meetings and oncology consults.
---

# Tumor Board Summary Generator

Convert detailed pathology reports into concise 3-5 line summaries for multidisciplinary tumor boards.

## When to Use This Skill

Use this skill for:
- Multidisciplinary tumor board (MDT) meetings
- Oncology consultations
- Clinical case presentations
- Referral summaries
- Quick pathology review

## Supported Tumor Types

All cancer types (breast, colorectal, pancreas, gastric, and general carcinomas)

## Key Features

1. **Concise Format**: 3-5 lines maximum
2. **Key Elements**: Patient, diagnosis, stage, margins, nodes, biomarkers
3. **Clinical Focus**: Only clinically actionable information
4. **Ready for Presentation**: No formatting needed

## Reference Files

Reference on-demand (DO NOT load at startup):
- Summary guidelines: `../../shared-references/common/tumor_board_summary.md`

## Usage Examples

```bash
# Generate summary
claude "Create tumor board summary using tumor-board-summary" < report.txt

# Quick MDT summary
claude "Summarize for tumor board using tumor-board-summary" < breast_report.txt
```

## Processing Instructions

1. **Extract key elements** from pathology report:
   - Patient demographics (age, sex)
   - Diagnosis (tumor type, grade)
   - TNM stage
   - Margins status
   - Lymph node status
   - Key biomarkers (ER/PR/HER2/MSI/HER2)

2. **Format concisely**: 3-5 lines, bullet or paragraph format

3. **Output**: Clinical summary ready for MDT presentation

## Summary Format Template

**Line 1**: Patient demographics + specimen type
**Line 2**: Diagnosis with grade and size
**Line 3**: TNM stage with margins
**Line 4**: Lymph node status
**Line 5**: Biomarkers (if applicable)

## Example Output

```
52F, right total mastectomy + ALND
Invasive ductal carcinoma, grade 2, 2.3 cm, pT2
Margins negative (>10mm), Stage IIA (pT2 N0 M0)
Lymph nodes: 0/15 positive
ER 95%+, PR 80%+, HER2 neg (IHC 1+), Ki-67 20%
```

---

**Note**: Minimal skill definition. Guidelines loaded on-demand during processing only.
