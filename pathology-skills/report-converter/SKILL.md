---
name: report-converter
description: Converts free-text narrative pathology reports into structured CAP synoptic format and generates amendments/addenda/corrections for previously-issued reports. Use when the user uploads or pastes a narrative pathology report (.pdf, .docx, .txt) and asks to "convert to synoptic", "convert to CAP format", "structure this report", "make this synoptic", "generate an amendment", "add an addendum", or "issue a corrected report". Extracts diagnostic elements (tumor type, grade, size, stage, margins, nodes, biomarkers) and maps them to CAP data elements.
license: MIT
metadata:
  version: 1.3.0
  author: Serdar Balci
---

# Report Converter

Transform narrative pathology reports into structured CAP synoptic format and generate professional amendments.

## When to Use This Skill

Use this skill for:
- Converting legacy free-text reports to synoptic format
- Report standardization projects
- Creating addenda for biomarker results
- Generating amendment reports
- Training on synoptic reporting

## Dual Functionality

1. **Free-text to Synoptic**: Convert narrative reports to CAP format
2. **Amendment Generation**: Create addenda and corrections

## Key Features

1. **Text Parsing**: Extract diagnostic elements from prose
2. **CAP Mapping**: Map findings to CAP data elements
3. **Structured Output**: Generate CAP synoptic format
4. **Amendment Format**: Professional addendum/correction templates
5. **Completeness Check**: Flag missing required elements

## Reference Files

Reference on-demand (DO NOT load at startup):
- Conversion guidelines: `../../shared-references/common/freetext_to_synoptic.md`
- Amendment templates: `../../shared-references/common/amendment_generator.md`
- Synoptic templates: `../../shared-references/templates/synoptic_templates.md`

## Usage Examples

```bash
# Convert free-text report
claude "Convert to synoptic format using report-converter" < narrative_report.txt

# Generate addendum
claude "Create addendum for HER2 results using report-converter" < original_report.txt

# Generate amendment
claude "Create amendment correcting tumor size using report-converter"
```

## Processing Instructions

### For Free-text Conversion:
1. **Parse narrative report**: Extract all diagnostic findings
2. **Identify tumor type**: Breast, colorectal, pancreas, gastric
3. **Load appropriate CAP template**
4. **Map findings to CAP elements**
5. **Flag missing elements**: Highlight what's incomplete
6. **Output**: Structured synoptic report

### For Amendment Generation:
1. **Identify amendment type**: Addendum (addition) vs correction
2. **Load amendment template**
3. **Format professional amendment** with date, reason, updated information
4. **Output**: Ready-to-sign addendum

## Supported Report Types

- Breast carcinoma reports
- Colorectal carcinoma reports
- Pancreas carcinoma reports
- Gastric carcinoma reports
- General carcinoma reports

## Amendment Types

- **Addendum**: Add new information (biomarkers, special stains)
- **Correction**: Fix errors (tumor size, grade, margins)
- **Supplemental**: Additional findings after review

---

**Note**: Minimal skill definition. References loaded on-demand during processing only.
