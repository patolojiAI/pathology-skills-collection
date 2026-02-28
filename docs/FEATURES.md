# Feature Documentation

Detailed documentation for all skill features beyond basic compliance checking.

---

## Template Generation Mode

Generate blank CAP-style synoptic templates using `references/templates/synoptic_templates.md`.

### Trigger Phrases

- "Generate a synoptic template for..."
- "Give me a blank CAP template for..."
- "Create a breast/colorectal/pancreas/gastric report template"
- "I need a Whipple specimen template"
- "Meme lumpektomi için sinoptik şablon oluştur" (Turkish)

### Workflow

1. **Identify tumor type** from user request
2. **Identify specimen type** if specified (lumpectomy, Whipple, gastrectomy, etc.)
3. **Load template** from references
4. **Pre-fill values** if user provides any (size, grade, type)
5. **Return formatted template** ready for use

### Template Features

| Feature | Description |
|---------|-------------|
| **Field markers** | `*` = Required, `+` = Conditional, `°` = Optional |
| **Response types** | `(_)` = Single choice, `[ ]` = Multiple choice, `___` = Free text |
| **All CAP elements** | Core + Conditional + Recommended fields |
| **Staging section** | AJCC 8th edition pTNM with checkboxes |
| **Biomarkers** | Tumor-specific (ER/PR/HER2, MMR, etc.) |

### Available Templates

| Tumor Type | Specimen Types |
|------------|----------------|
| Breast | Lumpectomy, Mastectomy |
| Colorectal | Colectomy, LAR, APR |
| Pancreas | Whipple, Distal pancreatectomy |
| Gastric | Partial gastrectomy, Total gastrectomy |

### Language Options

- **English**: `references/templates/synoptic_templates.md`
- **Turkish**: `references/templates/synoptic_templates_tr.md`

---

## Tumor Board Summary Mode

Generate concise 3-5 line MDT summaries using `references/summaries/tumor_board_summary.md`.

### Trigger Phrases

**English:**
- "Generate a tumor board summary"
- "Create an MDT summary"
- "Summarize for tumor board"

**Turkish:**
- "Tümör kurulu özeti oluştur"
- "MDT özeti yaz"

### Output Format

```
[Age][Sex] with [TUMOR TYPE] of the [SITE/LOCATION].
[PROCEDURE]: [SIZE] [HISTOLOGIC TYPE], [GRADE], [STAGE (pTNM)].
Margins: [STATUS]. LVI: [+/-]. PNI: [+/-]. Nodes: [X/Y positive].
Biomarkers: [KEY RESULTS].
```

### Examples

**Breast:**
```
58F with invasive carcinoma of the left breast, upper outer quadrant.
Lumpectomy: 2.3 cm invasive ductal carcinoma, Grade 2, pT2 N1a M0 (Stage IIB).
Margins: Negative (closest 3mm anterior). LVI: Present. Nodes: 2/15 positive.
ER 95%/PR 80%/HER2 negative/Ki-67 25%.
```

**Colorectal:**
```
67M with adenocarcinoma of the sigmoid colon.
Sigmoid colectomy: 4.5 cm mod diff adenocarcinoma, pT3 N1b M0 (Stage IIIB).
Margins: Negative (CRM 8mm). LVI: Present. PNI: Absent. Nodes: 3/18 positive.
MMR intact. KRAS G12D mutation.
```

**Pancreas:**
```
72F with adenocarcinoma of the pancreatic head.
Whipple: 3.2 cm mod diff ductal adenocarcinoma, pT2 N1 M0 (Stage IIB).
Margins: R1 (SMA 0.5mm). LVI: Present. PNI: Present. Nodes: 2/14 positive.
```

**Gastric:**
```
55M with adenocarcinoma of the gastric antrum.
Subtotal gastrectomy: 5.0 cm poorly cohesive carcinoma, pT3 N2 M0 (Stage IIIA).
Margins: Negative. LVI: Present. PNI: Present. Nodes: 4/22 positive.
HER2 negative. Lauren diffuse type.
```

---

## Free-Text to Synoptic Converter

Convert narrative reports to structured CAP format using `references/converters/freetext_to_synoptic.md`.

### Trigger Phrases

**English:**
- "Convert this report to synoptic format"
- "Transform to CAP format"
- "Free-text to synoptic"

**Turkish:**
- "Bu raporu sinoptik formata dönüştür"
- "CAP formatına çevir"

### Workflow

1. **Identify tumor type** from report content
2. **Extract elements** using pattern matching
3. **Map to synoptic fields** using terminology tables
4. **Calculate staging** from extracted data
5. **Generate synoptic output**

### Extraction Patterns

| Element | English Pattern | Turkish Pattern |
|---------|-----------------|-----------------|
| Size | "X cm tumor", "X x Y x Z cm" | "X cm tümör" |
| Grade | "grade 1/2/3", "well/mod/poorly diff" | "derece 1/2/3" |
| Margins | "margins negative", "closest X mm" | "sınırlar negatif" |
| Nodes | "X of Y nodes positive" | "X/Y lenf nodu pozitif" |
| LVI | "LVI present/absent" | "LVI var/yok" |
| PNI | "PNI present/absent" | "PNI var/yok" |

### Example

**Input:**
```
Left breast, lumpectomy: Invasive ductal carcinoma, moderately 
differentiated, measuring 2.3 cm. Margins negative, closest 3mm 
anterior. LVI present. 2/15 nodes positive.
```

**Output:**
```
SYNOPTIC REPORT
═══════════════════════════════════════════════════════════════
TUMOR
Histologic Type: Invasive carcinoma of no special type (ductal)
Histologic Grade: Grade 2 - Moderately differentiated
Tumor Size: 2.3 cm

MARGINS
Status: Uninvolved
Closest Margin: Anterior, 3 mm

LYMPH NODES
Total Examined: 15
Total Positive: 2

STAGING: pT2 pN1a M0 (Stage IIB)
═══════════════════════════════════════════════════════════════
```

---

## Auto-Fill Suggestions

Suggest values for missing fields using `references/autofill/autofill_suggestions.md`.

### Trigger Phrases

**English:**
- "Suggest values for this report"
- "Auto-fill staging"
- "What should pT be for this tumor?"
- "Suggest pTNM"

**Turkish:**
- "Bu rapor için değerler öner"
- "Evrelemeyi otomatik doldur"
- "pTNM öner"

### Suggestion Types

| Category | Input → Suggestion |
|----------|-------------------|
| **Size → pT** | 2.3 cm breast → pT2 |
| **Nodes → pN** | 2/15 axillary → pN1a |
| **pTNM → Stage** | pT2 N1a M0 → Stage IIB |
| **Grade** | "moderately differentiated" → G2 |
| **Margins** | CRM 0.8mm → Positive (≤1mm) |
| **HER2** | IHC 2+ → Equivocal (FISH required) |
| **MMR** | MLH1/PMS2 loss → Deficient |

### Example Output

```
AUTO-FILL SUGGESTIONS
═══════════════════════════════════════════════════════════════

1. pT Category
   Current: Not specified
   Suggested: pT2
   Rationale: Tumor size 2.8 cm, confined to pancreas (>2 cm)
   Confidence: High

2. Stage Group
   Suggested: Stage IIB
   Rationale: pT2 N1 M0 → Stage IIB (AJCC 8th)
   Confidence: High

═══════════════════════════════════════════════════════════════
```

### Confidence Levels

| Level | Meaning |
|-------|---------|
| **High** | Clear criteria, apply directly |
| **Medium** | Minor ambiguity, apply with note |
| **Low** | Incomplete data, flag for review |

---

## Amendment Generator

Generate amendment text for corrections using `references/amendments/amendment_generator.md`.

### Trigger Phrases

**English:**
- "Generate an amendment for this report"
- "Create an addendum for missing staging"
- "Write a correction for margin status"

**Turkish:**
- "Bu rapor için düzeltme oluştur"
- "Eksik evreleme için ek rapor yaz"

### Amendment Types

| Type | Use Case |
|------|----------|
| **Addendum** | New info (biomarkers, deeper levels) |
| **Correction** | Error in original (typo, measurement) |
| **Amended Report** | Significant changes (staging, margins) |

### Template Categories

| Category | Example |
|----------|---------|
| Missing staging | Add pTNM and stage group |
| Staging error | Correct pT3 → pT2 |
| Margin revision | Negative → Positive |
| Node count | 2/15 → 4/18 |
| Biomarker addition | ER/PR/HER2/Ki-67 results |
| Typographical error | Right → Left breast |

### Example Output

```
AMENDED REPORT
═══════════════════════════════════════════════════════════════

Original Report Date: December 28, 2024
Amendment Date: December 29, 2024
Reason: Correction of pathologic stage

ORIGINAL STAGING:
   pT: pT3  pN: pN0  Stage: IIA

CORRECTED STAGING:
   pT: pT2  pN: pN0  Stage: IB

RATIONALE:
Review confirms tumor confined to pancreas, 2.8 cm. Per AJCC 
8th edition, tumors >2 cm confined to pancreas = pT2.

CLINICAL IMPACT:
Stage changed from IIA to IB. Recommend oncology review.

All other findings remain unchanged.
═══════════════════════════════════════════════════════════════
```

---

## TNM Stage Calculator

Calculate stage groups using `references/staging/tnm_stage_calculator.md`.

### Trigger Phrases

- "Calculate TNM stage for pT2 N1 M0 breast cancer"
- "What stage is pT3 N1b colorectal cancer?"
- "Verify the staging in this report"
- "pT2 N1 M0 meme kanseri için evreyi hesapla" (Turkish)

### Input

- pT category (e.g., pT2, pT3, pT4a)
- pN category (e.g., pN0, pN1, pN2)
- pM category (e.g., M0, M1)
- Tumor type (breast, colorectal, pancreas, gastric)

### Output

```
TNM STAGE CALCULATION
═══════════════════════════════════════════════════════════════
Input:
  pT: pT2 (tumor >2 cm but ≤5 cm)
  pN: pN1a (metastases in 1-3 axillary nodes)
  pM: M0 (no distant metastasis)
  Tumor: Breast

Calculated Stage: IIB (AJCC 8th Edition)
═══════════════════════════════════════════════════════════════
```

---

## SNOMED CT / ICD-O-3 Coding

Suggest codes using `references/coding/snomed_ct_codes.md`.

### Trigger Phrases

- "What's the SNOMED code for invasive ductal carcinoma?"
- "Give me ICD-O-3 codes for this tumor"
- "Code this report with SNOMED CT"
- "İnvaziv duktal karsinom için SNOMED kodu nedir?" (Turkish)

### Output

```
SNOMED CT CODING
═══════════════════════════════════════════════════════════════
Morphology:
  Code: 8500/3
  Term: Invasive ductal carcinoma

Topography:
  Code: C50.4
  Term: Upper outer quadrant of breast

Grade:
  Code: G2
  Term: Moderately differentiated

Combined ICD-O-3: 8500/3 - C50.4
═══════════════════════════════════════════════════════════════
```
