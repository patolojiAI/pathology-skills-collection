---
name: colorectal-pathology-specialist
description: Comprehensive colorectal cancer pathology workflow combining CAP/ICCR compliance validation, synoptic template generation, TNM staging (AJCC 8th edition), MSI/MMR testing interpretation, mesorectal excision quality (MERCURY) grading, tumor board summaries, and SNOMED coding. Use when the user uploads or pastes a colorectal pathology report (colectomy, low anterior resection, abdominoperineal resection, polypectomy) and asks to "check colorectal report", "validate CAP ColoRectal protocol", "stage this colorectal cancer", "interpret MSI/MMR", "assess TME quality", or any colorectal-cancer-specific pathology task. Supports .pdf, .docx, .txt input in English and Turkish.
license: MIT
metadata:
  version: 1.3.0
  author: Serdar Balci
---

# Colorectal Pathology Specialist

Complete colorectal cancer pathology workflow toolkit combining compliance checking, staging, MSI/MMR reporting, and coding.

## When to Use This Skill

Use this skill for:
- Colorectal cancer pathology report validation
- Colon and rectal carcinoma specimens (colectomy, polypectomy, TEM)
- CAP/ICCR compliance checking with severity scoring
- TNM staging calculation (AJCC 8th edition)
- MSI/MMR testing interpretation
- Mesorectal excision quality grading (rectal specimens)
- Tumor board summary generation
- SNOMED CT coding assistance

## Supported Specimen Types

- Right hemicolectomy (cecum, ascending colon)
- Left hemicolectomy (descending colon)
- Sigmoid colectomy
- Low anterior resection (rectal)
- Abdominoperineal resection (rectal)
- Total mesorectal excision (TME)
- Polypectomy specimens
- Transanal excision (TEM/TAMIS)

## Key Features

1. **Compliance Checking**: Validates against CAP ColoRectal and ICCR Colorectal Cancer protocols
2. **TNM Staging**: AJCC 8th edition colorectal staging with pT/pN/M calculation
3. **MSI/MMR Reporting**: Microsatellite instability and mismatch repair interpretation
4. **Mesorectal Quality**: TME quality grading (complete/nearly complete/incomplete)
5. **Template Generation**: Colon and rectal specimen synoptic templates
6. **Tumor Board Summaries**: Concise 3-5 line MDT presentation format
7. **SNOMED Coding**: Colorectal-specific code suggestions

## Reference Files

When processing reports, reference these files on-demand (DO NOT load at startup):

- **Diagnosis guidelines**: `references/diagnosis/colorectal_resection.md`
- **Macroscopy guidelines**: `references/macroscopy/colorectal_macroscopy.md`
- **TNM staging**: `../../shared-references/staging/tnm_stage_calculator.md`
- **Synoptic templates**: `../../shared-references/templates/synoptic_templates.md`
- **SNOMED codes**: `../../shared-references/coding/snomed_ct_codes.md`

## Usage Examples

```bash
# Validate report compliance
claude "Check this colorectal report using colorectal-pathology-specialist" < report.txt

# Generate staging
claude "What stage is pT3 N1b M0 for colorectal using colorectal-pathology-specialist"

# Create template
claude "Generate rectal TME template using colorectal-pathology-specialist"

# MSI interpretation
claude "Interpret MLH1 loss, PMS2 loss, MSH2 intact, MSH6 intact using colorectal-pathology-specialist"
```

## Processing Instructions

When analyzing colorectal pathology reports:

1. **Identify request type** (compliance check, staging, template, MSI interpretation, summary, coding)
2. **Read relevant reference file** on-demand based on request
3. **Process the report** using appropriate guidelines
4. **Generate output** in requested format
5. **DO NOT load all reference files** upfront

## Compliance Scoring

Use severity-based weighting:
- Critical elements (tumor size, grade, margins, CRM, nodes, MSI): -15 points each
- Major elements (LVI, PNI, tumor deposits, perforation): -5 points each
- Minor elements (tumor location, distance from margins): -2 points each

Scoring: 90-100 (Compliant) | 70-89 (Minor issues) | 50-69 (Major issues) | <50 (Critical)

## Cross-Validation Checks

Always validate:
- pT category vs tumor invasion depth
- pN category vs positive node count
- Stage group vs pT/pN/M combination
- CRM status (rectal) vs margin measurements
- MSI status vs MMR immunohistochemistry pattern

## Language Support

Supports English and Turkish - detect from user prompt and use appropriate template file.

---

**Note**: This is a minimal skill definition. Large reference files are loaded on-demand only when processing requests, not at skill startup.
