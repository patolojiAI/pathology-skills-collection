---
name: breast-pathology-specialist
description: Comprehensive breast cancer pathology workflow combining CAP/ICCR compliance validation, synoptic template generation, TNM staging (AJCC 8th edition), biomarker reporting (ER/PR/HER2/Ki-67) per ASCO/CAP guidelines, tumor board summaries, and SNOMED coding for invasive breast carcinoma. Use when the user uploads or pastes a breast pathology report (mastectomy, lumpectomy, wide local excision, sentinel/axillary lymph node biopsy) and asks to "check breast report", "validate breast pathology", "stage this breast cancer", "interpret ER/PR/HER2", "generate breast template", or any breast-cancer-specific pathology task. Supports .pdf, .docx, .txt input in English and Turkish.
license: MIT
metadata:
  version: 1.3.0
  author: Serdar Balci
---

# Breast Pathology Specialist

Complete breast cancer pathology workflow toolkit combining compliance checking, staging, biomarker reporting, and coding.

## When to Use This Skill

Use this skill for:
- Breast cancer pathology report validation
- Invasive breast carcinoma specimens (mastectomy, lumpectomy, excision)
- CAP/ICCR compliance checking with severity scoring
- TNM staging calculation (AJCC 8th edition)
- Biomarker interpretation (ER/PR/HER2/Ki-67)
- Tumor board summary generation
- SNOMED CT coding assistance

## Supported Specimen Types

- Total mastectomy
- Partial mastectomy / Lumpectomy
- Wide local excision
- Re-excision specimens
- Sentinel lymph node biopsy
- Axillary lymph node dissection

## Key Features

1. **Compliance Checking**: Validates against CAP Breast.Invasive and ICCR Invasive Carcinoma of the Breast protocols
2. **TNM Staging**: AJCC 8th edition breast cancer staging with pT/pN/M calculation
3. **Biomarker Reporting**: ER/PR/HER2/Ki-67 validation per ASCO/CAP guidelines
4. **Template Generation**: Pre-filled or blank synoptic templates
5. **Tumor Board Summaries**: Concise 3-5 line MDT presentation format
6. **SNOMED Coding**: Breast-specific code suggestions

## Reference Files

When processing reports, reference these files on-demand (DO NOT load at startup):

- **Diagnosis guidelines**: `references/diagnosis/breast_invasive_carcinoma.md`
- **Macroscopy guidelines**: `references/macroscopy/breast_macroscopy.md`
- **TNM staging**: `../../shared-references/staging/tnm_stage_calculator.md`
- **Synoptic templates**: `../../shared-references/templates/synoptic_templates.md`
- **Biomarkers**: `../../shared-references/biomarkers/BIOMARKERS_INDEX.md`
- **SNOMED codes**: `../../shared-references/coding/snomed_ct_codes.md`

## Usage Examples

```bash
# Validate report compliance
claude "Check this breast report using breast-pathology-specialist" < report.txt

# Generate staging
claude "What stage is pT2 N1a M0 for breast using breast-pathology-specialist"

# Create template
claude "Generate blank breast lumpectomy template using breast-pathology-specialist"

# Tumor board summary
claude "Create tumor board summary using breast-pathology-specialist" < report.txt
```

## Processing Instructions

When analyzing breast pathology reports:

1. **Identify request type** (compliance check, staging, template, summary, coding)
2. **Read relevant reference file** on-demand based on request
3. **Process the report** using appropriate guidelines
4. **Generate output** in requested format
5. **DO NOT load all reference files** upfront

## Compliance Scoring

Use severity-based weighting:
- Critical elements (tumor size, grade, margins, nodes, ER/PR/HER2): -15 points each
- Major elements (LVI, PNI, ductal carcinoma in situ): -5 points each
- Minor elements (Ki-67, oncotype, tumor location): -2 points each

Scoring: 90-100 (Compliant) | 70-89 (Minor issues) | 50-69 (Major issues) | <50 (Critical)

## Cross-Validation Checks

Always validate:
- pT category vs tumor size consistency
- pN category vs positive node count
- Stage group vs pT/pN/M combination
- Margin status vs R classification
- ER/PR/HER2 vs molecular subtype

## Language Support

Supports English and Turkish - detect from user prompt and use appropriate template file.

---

**Note**: This is a minimal skill definition. Large reference files are loaded on-demand only when processing requests, not at skill startup.
