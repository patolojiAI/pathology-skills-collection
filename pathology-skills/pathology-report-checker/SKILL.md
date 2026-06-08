---
name: pathology-report-checker
description: Analyzes surgical pathology cancer reports for compliance with CAP (College of American Pathologists) and ICCR (International Collaboration on Cancer Reporting) guidelines. Validates pTNM staging (AJCC 8th edition), checks required element completeness with severity-based scoring, generates blank or pre-filled CAP synoptic templates, creates 3-5 line tumor board summaries, suggests SNOMED CT and ICD-O-3 codes, converts free-text narratives to structured synoptic format, and drafts amendments/addenda. Use when the user pastes or uploads a pathology report (txt, pdf, docx, image, xlsx) and asks to "check CAP compliance", "verify staging", "generate synoptic template", "tumor board summary", "convert to synoptic", "calculate TNM stage", or "code with SNOMED" for breast invasive carcinoma, colorectal resection, exocrine pancreas carcinoma, or gastric carcinoma. Supports English and Turkish. Do NOT use for non-cancer pathology (inflammatory, infectious), cytology, or unsupported tumor types.
license: MIT
metadata:
  author: Serdar Balci, MD, Pathologist
  version: 1.4.0
  guidelines: CAP 2024, ICCR 2nd edition, AJCC 8th edition, AAPA 3rd edition, WHO 5th edition
---

# Pathology Report Compliance Checker

Analyze surgical pathology cancer reports against CAP (College of American Pathologists), ICCR (International Collaboration on Cancer Reporting), and AAPA (American Association of Pathology Assistants) guidelines.

## Performance Notes

CRITICAL: Always read the relevant reference file BEFORE producing analysis or templates. The skill's value comes from grounded clinical guidelines, not memorized knowledge.

- Take time to load the correct diagnosis + macroscopy reference files
- Quality of structured output matters more than speed
- Do not skip cross-validation (pT vs size, pN vs nodes, margins vs R)
- Match the report's language (English/Turkish) in the output

## Trigger Phrases

| Action | English | Turkish |
|--------|---------|---------|
| Compliance Check | "Check this report for CAP compliance" | "Bu raporu CAP uyumluluğu için kontrol et" |
| Synoptic Template | "Generate breast synoptic template" | "Meme sinoptik şablonu oluştur" |
| Tumor Board Summary | "Generate tumor board summary" | "Tümör kurulu özeti oluştur" |
| Free-text → Synoptic | "Convert to synoptic format" | "Sinoptik formata dönüştür" |
| Auto-fill | "Suggest pTNM staging" | "pTNM evrelemesi öner" |
| Amendment | "Generate amendment for this" | "Düzeltme oluştur" |
| SNOMED Coding | "What's the SNOMED code for..." | "... için SNOMED kodu nedir?" |
| TNM Calculator | "Calculate stage for pT2 N1 M0" | "pT2 N1 M0 için evreyi hesapla" |

## Mode Selection

Determine the task before reading any references:

- Compliance checking → follow **Compliance Check Workflow** below
- Template generation → follow **Template Generation Workflow** below
- Tumor board summary → follow **Summary Generation Workflow** below
- Staging calculation only → read `references/staging/tnm_stage_calculator.md`
- SNOMED/ICD-O-3 codes → read `references/coding/snomed_ct_codes.md`
- Free-text conversion → read `references/converters/freetext_to_synoptic.md`
- Auto-fill suggestions → read `references/autofill/autofill_suggestions.md`
- Amendment drafting → read `references/amendments/amendment_generator.md`

## Supported Report Types

| Type | CAP Protocol | ICCR Dataset |
|------|--------------|--------------|
| Breast invasive carcinoma | Breast.Invasive | Invasive Carcinoma of the Breast |
| Colorectal primary resection | ColoRectal | Colorectal Cancer |
| Exocrine pancreas carcinoma | Panc.Exo | Carcinoma of the Exocrine Pancreas |
| Gastric carcinoma | Stomach | Gastric Carcinoma |

## Reference Files

### Diagnosis (CAP/ICCR required elements)

| Tumor | File |
|-------|------|
| Breast | `references/diagnosis/breast_invasive_carcinoma.md` |
| Colorectal | `references/diagnosis/colorectal_resection.md` |
| Pancreas | `references/diagnosis/exocrine_pancreas.md` |
| Gastric | `references/diagnosis/gastric_carcinoma.md` |

### Macroscopy (AAPA-integrated)

| Tumor | File |
|-------|------|
| Common | `references/macroscopy/MACROSCOPY_COMMON.md` |
| Breast | `references/macroscopy/breast_macroscopy.md` |
| Colorectal | `references/macroscopy/colorectal_macroscopy.md` |
| Pancreas | `references/macroscopy/pancreas_macroscopy.md` |
| Gastric | `references/macroscopy/gastric_macroscopy.md` |

### Other references

| Feature | File |
|---------|------|
| TNM Staging | `references/staging/tnm_stage_calculator.md` |
| Synoptic Templates (EN) | `references/templates/synoptic_templates.md` |
| Synoptic Templates (TR) | `references/templates/synoptic_templates_tr.md` |
| SNOMED CT / ICD-O-3 | `references/coding/snomed_ct_codes.md` |
| Tumor Board Summary | `references/summaries/tumor_board_summary.md` |
| Free-text Converter | `references/converters/freetext_to_synoptic.md` |
| Auto-fill Suggestions | `references/autofill/autofill_suggestions.md` |
| Amendment Generator | `references/amendments/amendment_generator.md` |
| Biomarker Index | `references/biomarkers/BIOMARKERS_INDEX.md` |

## Quick Search Patterns

For large reference files, use grep to find specific content quickly instead of loading the entire file.

Find tumor-type template (saves ~3,300 tokens vs full file):

```bash
grep -A 80 "## Breast Invasive" references/templates/synoptic_templates.md
grep -A 80 "## Colorectal" references/templates/synoptic_templates.md
grep -A 80 "## Pancreas" references/templates/synoptic_templates.md
grep -A 80 "## Gastric" references/templates/synoptic_templates.md
```

Find specific staging table:

```bash
grep -A 20 "Breast Cancer Stage" references/staging/tnm_stage_calculator.md
grep -A 20 "Colorectal Stage" references/staging/tnm_stage_calculator.md
grep -A 20 "Pancreas Stage" references/staging/tnm_stage_calculator.md
grep -A 20 "Gastric Stage" references/staging/tnm_stage_calculator.md
```

Find SNOMED / ICD-O-3 code:

```bash
grep -i "ductal carcinoma" references/coding/snomed_ct_codes.md
grep -i "adenocarcinoma" references/coding/snomed_ct_codes.md
```

Find amendment template:

```bash
grep -A 15 "Addendum Template" references/amendments/amendment_generator.md
grep -A 15 "Correction Template" references/amendments/amendment_generator.md
```

## Workflows

### Compliance Check Workflow

1. **Determine report type**: From report content identify organ, specimen type, tumor type, and language (English/Turkish).
2. **Load reference files**: Read the matching diagnosis and macroscopy files from `references/`.
3. **Extract elements**: Parse the report using the EN/TR terminology equivalents listed inside each reference file.
4. **Analyze**:
   - 4a. Check missing/empty elements by severity (CRITICAL / MAJOR / MINOR).
   - 4b. Cross-validate: pT vs tumor size, pN vs positive node count, margins vs R classification, node count vs adequacy threshold (12 colorectal, 15 breast, etc.).
   - 4c. Compute quality metrics: Completeness (40%) + Clarity (20%) + Consistency (40%).
   - 4d. Check macroscopy/gross description for completeness and gross-vs-microscopic concordance.
5. **Generate output**: Produce a QA report with compliance score, status, listed gaps grouped by severity, and recommendations.
6. **Verify staging**: Cross-check pTNM categories against the AJCC 8th edition stage group using `references/staging/tnm_stage_calculator.md`.

### Template Generation Workflow

1. Identify tumor type and specimen type from the request.
2. Use grep to load only the relevant section of `references/templates/synoptic_templates.md` (or `synoptic_templates_tr.md` for Turkish).
3. Optionally pre-fill with user-provided values (e.g., "2.3 cm Grade 2 IDC", "pT2 N1a").
4. Return a formatted template containing every required CAP element with placeholders for the rest.

### Summary Generation Workflow

1. Extract key findings: patient age/sex, diagnosis, procedure, pT/pN/pM, stage group, margins, node ratio, biomarkers.
2. Read format examples from `references/summaries/tumor_board_summary.md`.
3. Produce a 3-5 line MDT-ready summary in the report's language.

## Severity Levels

| Level | Elements | Score Impact |
|-------|----------|--------------|
| CRITICAL | pT, pN, margins, grade, receptors | -15 each |
| MAJOR | LVI, PNI, tumor size, node counts | -5 each |
| MINOR | Focality, gross details | -2 each |

**Score formula:** `100 - (Critical × 15) - (Major × 5) - (Minor × 2)`

| Score | Status |
|-------|--------|
| 90-100 | COMPLIANT |
| 70-89 | INCOMPLETE - MINOR |
| 50-69 | INCOMPLETE - MAJOR |
| <50 | INCOMPLETE - CRITICAL |

## Supported Input Formats

| Format | Extensions | Use Case |
|--------|------------|----------|
| Plain Text | `.txt`, `.md` | Interactive CLI, direct paste |
| PDF | `.pdf` | Scanned or digital reports |
| Word | `.docx` | Office documents |
| Excel/CSV | `.xlsx`, `.xls`, `.csv` | Batch processing, LIS exports |
| Images | `.jpg`, `.png`, `.tiff` | Scanned paper reports (Claude Vision) |

### Excel batch format

Expected columns:

- `report_text` (required): Full pathology report text
- `patient_id` (optional): Case identifier
- `tumor_type` (optional): `breast`, `colorectal`, `gastric`, or `pancreas` (auto-detected if absent)

## Example Outputs

### Compliance check (breast, English)

```
COMPLIANCE ANALYSIS
Tumor: Breast invasive carcinoma
Protocol: CAP Breast.Invasive

COMPLIANCE SCORE: 82/100
STATUS: INCOMPLETE - MINOR

MISSING ELEMENTS (3):
CRITICAL (1):
  - ER/PR/HER2 receptor studies (-15)
MAJOR (2):
  - Lymphovascular invasion status (-5)
  - Perineural invasion status (-5)

CROSS-VALIDATION:
- pT2 consistent with 2.3 cm tumor size (AJCC 8th)
- pN1a consistent with 2 positive nodes
- Margins negative (5 mm) -> R0 correct

RECOMMENDATIONS:
1. Add IHC results for ER, PR, HER2
2. Document LVI presence/absence
3. Document PNI presence/absence
```

### Tumor board summary

```
58F with invasive ductal carcinoma of the left breast.
Lumpectomy: 2.3 cm IDC, Grade 2, pT2 N1a M0 (Stage IIB).
Margins negative. LVI present. Nodes 2/15 positive.
ER 95% / PR 80% / HER2 negative / Ki-67 25%.
```

## Important Notes

1. Always read the matching reference file before analyzing — do not rely on memory.
2. Cross-validate pT/pN/stage against size, nodes, and margins for every report.
3. Check macroscopy for gross-vs-microscopic discordance (>20% size mismatch is a flag).
4. Match the report language: English in → English out; Turkish in → Turkish out.
5. Severity matters: prioritize CRITICAL gaps in the summary; MINOR gaps go at the end.
6. This skill assists with QA only. Do not replace clinical judgment; pathologist sign-out is final.

## When Not To Use

- Non-cancer pathology (inflammatory, infectious, autoimmune)
- Cytology specimens (FNA, brushings, fluids)
- Tumor types other than breast invasive, colorectal, exocrine pancreas, or gastric
- Hematopathology, dermatopathology, neuropathology
- Frozen-section/intra-operative consultations
