---
name: pancreas-pathology-specialist
description: Comprehensive pancreatic cancer pathology workflow combining CAP/ICCR compliance validation, synoptic template generation, TNM staging (AJCC 8th edition for exocrine pancreas), Whipple/distal-pancreatectomy specimen dissection guidance, axial slicing and margin assessment (SMA, SMV, posterior, anterior, pancreatic neck, bile duct), tumor board summaries, and SNOMED coding. Use when the user uploads or pastes a pancreatic pathology report (Whipple, distal pancreatectomy, total pancreatectomy, pancreatic biopsy) and asks to "check pancreas report", "validate CAP Panc.Exo protocol", "stage this pancreatic cancer", "assess Whipple margins", or any pancreatic-cancer-specific pathology task. Supports .pdf, .docx, .txt input in English and Turkish.
license: MIT
metadata:
  version: 1.3.0
  author: Serdar Balci
---

# Pancreatic Pathology Specialist

Complete pancreatic cancer pathology workflow toolkit combining compliance checking, staging, margin assessment, and coding.

## When to Use This Skill

Use this skill for:
- Pancreatic cancer pathology report validation
- Exocrine pancreas carcinoma specimens (Whipple, distal pancreatectomy, total pancreatectomy)
- CAP/ICCR compliance checking with severity scoring
- TNM staging calculation (AJCC 8th edition)
- Complex margin assessment (anterior/posterior surface, SMA, portal vein, bile duct)
- Whipple specimen dissection guidance
- Tumor board summary generation
- SNOMED CT coding assistance

## Supported Specimen Types

- Whipple procedure (pancreaticoduodenectomy)
- Distal pancreatectomy
- Total pancreatectomy
- Enucleation
- Core needle biopsy

## Key Features

1. **Compliance Checking**: Validates against CAP Panc.Exo and ICCR Carcinoma of the Exocrine Pancreas protocols
2. **TNM Staging**: AJCC 8th edition pancreas staging with pT/pN/M calculation
3. **Margin Assessment**: Anterior surface, posterior surface, SMA, portal vein groove, bile duct, pancreatic neck
4. **Whipple Dissection**: Step-by-step guidance for proper specimen sampling
5. **Template Generation**: Whipple and distal pancreatectomy synoptic templates
6. **Tumor Board Summaries**: Concise 3-5 line MDT presentation format
7. **SNOMED Coding**: Pancreas-specific code suggestions

## Reference Files

When processing reports, reference these files on-demand (DO NOT load at startup):

- **Diagnosis guidelines**: `references/diagnosis/exocrine_pancreas.md`
- **Macroscopy guidelines**: `references/macroscopy/pancreas_macroscopy.md`
- **TNM staging**: `../../shared-references/staging/tnm_stage_calculator.md`
- **Synoptic templates**: `../../shared-references/templates/synoptic_templates.md`
- **SNOMED codes**: `../../shared-references/coding/snomed_ct_codes.md`

## Usage Examples

```bash
# Validate report compliance
claude "Check this pancreas report using pancreas-pathology-specialist" < report.txt

# Generate staging
claude "What stage is pT2 N1 M0 for pancreas using pancreas-pathology-specialist"

# Create template
claude "Generate Whipple specimen template using pancreas-pathology-specialist"

# Margin interpretation
claude "How to report anterior surface margin 0.5mm using pancreas-pathology-specialist"
```

## Processing Instructions

When analyzing pancreatic pathology reports:

1. **Identify request type** (compliance check, staging, template, margin interpretation, summary, coding)
2. **Read relevant reference file** on-demand based on request
3. **Process the report** using appropriate guidelines
4. **Generate output** in requested format
5. **DO NOT load all reference files** upfront

## Compliance Scoring

Use severity-based weighting:
- Critical elements (tumor size, grade, margins, SMA margin, nodes): -15 points each
- Major elements (LVI, PNI, surface involvement, bile duct margin): -5 points each
- Minor elements (tumor location, distance from margins): -2 points each

Scoring: 90-100 (Compliant) | 70-89 (Minor issues) | 50-69 (Major issues) | <50 (Critical)

## Cross-Validation Checks

Always validate:
- pT category vs tumor size and extension
- pN category vs positive node count
- Stage group vs pT/pN/M combination
- R status vs margin measurements
- SMA margin vs arterial involvement

## Language Support

Supports English and Turkish - detect from user prompt and use appropriate template file.

---

**Note**: This is a minimal skill definition. Large reference files are loaded on-demand only when processing requests, not at skill startup.
