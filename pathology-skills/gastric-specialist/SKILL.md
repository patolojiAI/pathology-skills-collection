---
name: gastric-pathology-specialist
description: Comprehensive gastric cancer pathology analysis including CAP/ICCR compliance validation, synoptic template generation, TNM staging (AJCC 8th), Lauren classification, WHO histologic typing, HER2 testing interpretation, tumor board summaries, and SNOMED coding for gastric carcinoma specimens.
---

# Gastric Pathology Specialist

Complete gastric cancer pathology workflow toolkit combining compliance checking, staging, HER2 reporting, and coding.

## When to Use This Skill

Use this skill for:
- Gastric cancer pathology report validation
- Gastric carcinoma specimens (gastrectomy, endoscopic resection)
- CAP/ICCR compliance checking with severity scoring
- TNM staging calculation (AJCC 8th edition)
- Lauren classification (intestinal/diffuse/mixed)
- WHO histologic typing
- HER2 testing interpretation (IHC/FISH)
- Tumor board summary generation
- SNOMED CT coding assistance

## Supported Specimen Types

- Total gastrectomy
- Subtotal/partial gastrectomy
- Proximal gastrectomy
- Endoscopic mucosal resection (EMR)
- Endoscopic submucosal dissection (ESD)
- Wedge resection

## Key Features

1. **Compliance Checking**: Validates against CAP Stomach and ICCR Gastric Carcinoma protocols
2. **TNM Staging**: AJCC 8th edition gastric cancer staging with pT/pN/M calculation
3. **Lauren Classification**: Intestinal, diffuse, mixed, or indeterminate type
4. **WHO Typing**: Tubular, papillary, mucinous, poorly cohesive, mixed adenocarcinoma
5. **HER2 Reporting**: IHC scoring (0/1+/2+/3+) and FISH interpretation per Trastuzumab guidelines
6. **Template Generation**: Gastrectomy and endoscopic resection synoptic templates
7. **Tumor Board Summaries**: Concise 3-5 line MDT presentation format
8. **SNOMED Coding**: Gastric-specific code suggestions

## Reference Files

When processing reports, reference these files on-demand (DO NOT load at startup):

- **Diagnosis guidelines**: `references/diagnosis/gastric_carcinoma.md`
- **Macroscopy guidelines**: `references/macroscopy/gastric_macroscopy.md`
- **TNM staging**: `../../shared-references/staging/tnm_stage_calculator.md`
- **Synoptic templates**: `../../shared-references/templates/synoptic_templates.md`
- **Biomarkers**: `../../shared-references/biomarkers/BIOMARKERS_INDEX.md`
- **SNOMED codes**: `../../shared-references/coding/snomed_ct_codes.md`

## Usage Examples

```bash
# Validate report compliance
claude "Check this gastric report using gastric-pathology-specialist" < report.txt

# Generate staging
claude "What stage is pT3 N2 M0 for gastric using gastric-pathology-specialist"

# Create template
claude "Generate total gastrectomy template using gastric-pathology-specialist"

# HER2 interpretation
claude "Interpret HER2 IHC 2+ and FISH ratio 2.3 using gastric-pathology-specialist"
```

## Processing Instructions

When analyzing gastric pathology reports:

1. **Identify request type** (compliance check, staging, template, HER2 interpretation, summary, coding)
2. **Read relevant reference file** on-demand based on request
3. **Process the report** using appropriate guidelines
4. **Generate output** in requested format
5. **DO NOT load all reference files** upfront

## Compliance Scoring

Use severity-based weighting:
- Critical elements (tumor size, grade, depth, margins, nodes, HER2): -15 points each
- Major elements (LVI, PNI, Lauren type, WHO type): -5 points each
- Minor elements (tumor location, distance from margins): -2 points each

Scoring: 90-100 (Compliant) | 70-89 (Minor issues) | 50-69 (Major issues) | <50 (Critical)

## Cross-Validation Checks

Always validate:
- pT category vs invasion depth (mucosa/submucosa/muscularis propria/serosa)
- pN category vs positive node count
- Stage group vs pT/pN/M combination
- Margin status vs R classification
- HER2 IHC vs FISH correlation (2+ requires FISH)

## Language Support

Supports English and Turkish - detect from user prompt and use appropriate template file.

---

**Note**: This is a minimal skill definition. Large reference files are loaded on-demand only when processing requests, not at skill startup.
