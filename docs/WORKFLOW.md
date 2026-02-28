# Compliance Checking Workflow

Detailed step-by-step workflow for analyzing pathology reports.

---

## Step 1: Determine Report Type

From the report content, identify:

1. **Organ**: Breast, Colon/Rectum, Pancreas, or Stomach
2. **Specimen type**: Resection, biopsy, local excision
3. **Tumor type**: Invasive carcinoma, DCIS, adenocarcinoma, etc.

If unclear, ask the user to clarify.

---

## Step 2: Load Appropriate Reference

Based on report type, read the corresponding reference file:

| Report Type | Diagnosis Reference | Macroscopy Reference |
|-------------|--------------------|-----------------------|
| Breast invasive carcinoma | `references/diagnosis/breast_invasive_carcinoma.md` | `references/macroscopy/breast_macroscopy.md` |
| Colorectal resection | `references/diagnosis/colorectal_resection.md` | `references/macroscopy/colorectal_macroscopy.md` |
| Exocrine pancreas carcinoma | `references/diagnosis/exocrine_pancreas.md` | `references/macroscopy/pancreas_macroscopy.md` |
| Gastric carcinoma | `references/diagnosis/gastric_carcinoma.md` | `references/macroscopy/gastric_macroscopy.md` |

**Key macroscopy highlights:**

| Organ | Special Requirements |
|-------|---------------------|
| Breast | Pre-analytic (cold ischemic ≤1hr, fixation 6-72hr), margin extent (focal/moderate/extensive), LN processing (ITC/micro/macro) |
| Colorectal | Mesorectal grading (complete/nearly complete/incomplete), CRM positive if ≤1mm, tumor deposits (pN1c) |
| Pancreas | SMA/uncinate/retroperitoneal margin clarification, 6 margin protocol for Whipple, PanIN at margins |
| Gastric | HER2 fixation (8-48 hours), radial = omental margins, T3 vs T4 for ligament/omentum |

---

## Step 3: Extract Report Elements

Parse the report text to identify present elements:

- Reports may be in any language (Turkish, English, etc.)
- Use terminology equivalents table in reference files
- Recognize common abbreviations and synonyms
- Account for free-text vs synoptic formats

---

## Step 4: Compare Against Guidelines

### 4a: Element Checking

For each required element category:

| Category | Action if Not Found |
|----------|---------------------|
| **CORE/REQUIRED** | Flag as MISSING |
| **CONDITIONAL** | Flag as MISSING only if applicable |
| **RECOMMENDED** | Note as SUGGESTED |

**Field Status Detection:**

| Status | Description | Example |
|--------|-------------|---------|
| **MISSING** | Field not present at all | No mention of perineural invasion |
| **EMPTY** | Label exists but value blank | "Histolojik Derece: ___" |

**Severity Levels:**

| Severity | Definition | Elements | Score Impact |
|----------|------------|----------|--------------|
| 🔴 **CRITICAL** | Required for staging/treatment | pT, pN, margins, grade, receptors | -15 |
| 🟠 **MAJOR** | Core prognostic elements | LVI, PNI, tumor size, node counts | -5 |
| 🟡 **MINOR** | Recommended elements | Focality, gross details | -2 |

**Compliance Score:**

```
Score = 100 - (Critical × 15) - (Major × 5) - (Minor × 2)

90-100: COMPLIANT
70-89:  INCOMPLETE - MINOR
50-69:  INCOMPLETE - MAJOR  
<50:    INCOMPLETE - CRITICAL
```

### 4b: Cross-Validation Checks

Automatically validate internal consistency:

| Validation | Rule | Example Issue |
|------------|------|---------------|
| **pT vs Size** | pT must match tumor dimensions | 2.8cm reported as pT3 (should be pT2) |
| **pN vs Nodes** | pN must match positive count | pN0 with 2 positive nodes |
| **Margin vs R** | R classification must match distance | R0 with 0.5mm margin (should be R1) |
| **Node Adequacy** | Minimum nodes for staging | 8 nodes (need ≥12 for colorectal) |

Issue classification:
- ❌ **ERROR**: Definite inconsistency requiring correction
- ⚠️ **WARNING**: Potential issue or suboptimal practice

### 4c: Quality Metrics

Calculate four quality dimensions:

| Metric | Weight | Measures |
|--------|--------|----------|
| **Completeness** | 40% | Presence of required elements (weighted by severity) |
| **Clarity** | 20% | Synoptic format, section headers, explicit values |
| **Consistency** | 40% | Cross-validation results (errors/warnings) |
| **Overall Quality** | - | Weighted average of above |

### 4d: Macroscopy/Gross Description Check

Compare gross description against microscopic diagnosis.

**Gross Description Completeness:**

| Element Category | Examples |
|------------------|----------|
| Specimen ID | Type, laterality, site, orientation |
| Measurements | Overall size, tumor size |
| Margins | Distance to each margin, ink colors |
| Lymph nodes | Number found, sizes, appearance |
| Additional findings | Polyps, other lesions |

**Gross vs Diagnosis Cross-Validation:**

| Check | Discrepancy Type | Severity |
|-------|------------------|----------|
| Tumor size | Gross vs microscopic differs >20% | Warning |
| Margin status | Gross "close" but micro "positive" | Error |
| Lymph node count | Gross count ≠ micro count | Warning |
| Tumor extent | Gross "confined" but micro shows extension | Error |
| Location | Gross site ≠ diagnosis site | Error |
| Perforation | Noted in gross, missing in diagnosis | Error |

**Specimen-Specific Requirements:**

| Specimen | Special Requirements |
|----------|---------------------|
| TME (rectal) | Mesorectal grading (complete/near complete/incomplete) |
| Whipple | All margins: pancreatic neck, bile duct, uncinate, posterior |
| Mastectomy | Skin, nipple, axillary tail, pectoralis if present |
| Gastrectomy | Minimum 16 lymph nodes, omentum status |

---

## Step 5: Generate QA Report

Produce a structured actionable report:

```
═══════════════════════════════════════════════════════════════
PATHOLOGY REPORT COMPLIANCE CHECK
═══════════════════════════════════════════════════════════════

REPORT TYPE: [e.g., Breast Invasive Carcinoma - Resection]
GUIDELINES: CAP + ICCR
DATE CHECKED: [date]

───────────────────────────────────────────────────────────────
COMPLIANCE SCORE
───────────────────────────────────────────────────────────────
SCORE: [XX]/100
STATUS: [COMPLIANT / INCOMPLETE - MINOR / MAJOR / CRITICAL]

Gap Summary:
  🔴 Critical: X elements
  🟠 Major: Y elements  
  🟡 Minor: Z elements

Field Status:
  ⬜ Missing fields: X
  ⬚ Empty fields: Y

───────────────────────────────────────────────────────────────
CRITICAL GAPS (Severity: 🔴)
───────────────────────────────────────────────────────────────
1. [Element name]
   - Status: MISSING | EMPTY
   - Guideline: CAP + ICCR core
   - Required for: [staging/treatment/prognosis]
   - Expected: [what should be reported]

───────────────────────────────────────────────────────────────
MAJOR GAPS (Severity: 🟠)
───────────────────────────────────────────────────────────────
1. [Element name]
   - Status: MISSING | EMPTY
   - Guideline: [source]
   - Expected: [what should be reported]

───────────────────────────────────────────────────────────────
MINOR GAPS (Severity: 🟡)
───────────────────────────────────────────────────────────────
1. [Element name]
   - Status: MISSING | EMPTY
   - Guideline: [CAP optional / ICCR non-core]

───────────────────────────────────────────────────────────────
PRESENT ELEMENTS (Verified ✓)
───────────────────────────────────────────────────────────────
✓ [Element]: [value if extracted]
...

───────────────────────────────────────────────────────────────
CROSS-VALIDATION
───────────────────────────────────────────────────────────────
❌ ERROR: [description]
⚠️ WARNING: [description]

───────────────────────────────────────────────────────────────
NOTES
───────────────────────────────────────────────────────────────
- [Any observations about report quality, formatting, etc.]
```

---

## Step 6: TNM Stage Verification

When pT, pN, and pM categories are present, verify stage calculation.

### Process

1. **Extract TNM values** from report:
   - pT category (e.g., pT2, pT3, pT4a)
   - pN category (e.g., pN0, pN1, pN2)
   - pM category (e.g., M0, M1, pM1)
   - ypTNM prefix if post-neoadjuvant

2. **Look up stage group** using `references/staging/tnm_stage_calculator.md`

3. **Compare with reported stage** (if present)

4. **Flag discrepancies**:
   - Stage in report ≠ calculated stage → Error
   - Stage missing from report → Warning
   - Invalid TNM combination → Error

### Quick Reference Tables

**Breast:**
| | N0 | N1 | N2 | N3 |
|---|---|---|---|---|
| T1 | IA | IIA | IIIA | IIIC |
| T2 | IIA | IIB | IIIA | IIIC |
| T3 | IIB | IIIA | IIIA | IIIC |
| T4 | IIIB | IIIB | IIIB | IIIC |

**Colorectal:**
| | N0 | N1 | N2 |
|---|---|---|---|
| T1-2 | I | IIIA | IIIA-B |
| T3 | IIA | IIIB | IIIB-C |
| T4a | IIB | IIIB | IIIC |
| T4b | IIC | IIIC | IIIC |

**Pancreas:**
| | N0 | N1 | N2 |
|---|---|---|---|
| T1 | IA-IB | IIB | III |
| T2 | IB | IIB | III |
| T3 | IIA | IIB | III |
| T4 | III | III | III |

**Gastric:**
| | N0 | N1 | N2 | N3a | N3b |
|---|---|---|---|---|---|
| T1 | IA | IB | IIA | IIB | IIIB |
| T2 | IB | IIA | IIB | IIIA | IIIB |
| T3 | IIA | IIB | IIIA | IIIB | IIIC |
| T4a | IIB | IIIA | IIIA | IIIB | IIIC |
| T4b | IIIA | IIIB | IIIB | IIIC | IIIC |

**Any M1 = Stage IV**

### Output Format

```
───────────────────────────────────────────────────────────────
TNM STAGE VERIFICATION
───────────────────────────────────────────────────────────────
Extracted from report:
  pT: pT3 (tumor >4cm or extends beyond pancreas)
  pN: pN1 (1-3 positive nodes)
  pM: M0 (no distant metastasis)

Calculated Stage: IIB (AJCC 8th Edition)
Reported Stage: [Stage from report or "Not stated"]

Status: ✓ MATCHES | ⚠️ DISCREPANCY | ❌ ERROR

If discrepancy:
  Expected: Stage IIB
  Reported: Stage IIA
  Action: Verify pT, pN, pM categories and recalculate
```

---

## Step 7: SNOMED CT Coding (Optional)

When requested, suggest SNOMED CT codes using `references/coding/snomed_ct_codes.md`.

### Process

1. **Extract histologic type** → Map to morphology code (M-code)
2. **Extract anatomic site** → Map to topography code (T-code)
3. **Determine behavior** → Add behavior suffix
4. **Extract grade** → Map to grade code
5. **Identify procedure** → Map to procedure code

### Output Format

```
═══════════════════════════════════════════════════════════════
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

Procedure:
  Term: Lumpectomy
  SNOMED CT: 392021009

Combined ICD-O-3: 8500/3 - C50.4
───────────────────────────────────────────────────────────────
```
