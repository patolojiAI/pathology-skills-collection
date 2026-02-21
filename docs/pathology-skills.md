# Pathology Skills Reference

Comprehensive documentation for all 10 skills in the pathology skills collection.

---

## Table of Contents

### Core Functional Skills
1. [Compliance Checker](#1-compliance-checker)
2. [Template Generator](#2-template-generator)
3. [TNM Stage Calculator](#3-tnm-stage-calculator)
4. [Pathology Coder](#4-pathology-coder)
5. [Tumor Board Summary](#5-tumor-board-summary)
6. [Report Converter](#6-report-converter)

### Specialist All-in-One Skills
7. [Breast Specialist](#7-breast-specialist)
8. [Colorectal Specialist](#8-colorectal-specialist)
9. [Pancreas Specialist](#9-pancreas-specialist)
10. [Gastric Specialist](#10-gastric-specialist)

---

## Core Functional Skills

## 1. Compliance Checker

**Skill name:** `pathology-compliance-checker`

### Purpose
Validate surgical pathology cancer reports against CAP (College of American Pathologists) and ICCR (International Collaboration on Cancer Reporting) guidelines with severity-based scoring.

### When to Use
- Pre-sign-out quality checks
- Department quality assurance audits
- CAP accreditation preparation
- Resident training on synoptic reporting
- Identifying common reporting gaps

### Supported Tumor Types
- Breast invasive carcinoma (CAP Breast.Invasive)
- Colorectal resection (CAP ColoRectal)
- Exocrine pancreas carcinoma (CAP Panc.Exo)
- Gastric carcinoma (CAP Stomach)

### Key Features
- **Severity-Based Scoring**: Critical (−15), Major (−5), Minor (−2) point deductions
- **Cross-Validation**: Automatic checking of pT vs. size, pN vs. nodes, margins vs. R classification
- **Macroscopy Validation**: Gross vs. microscopic concordance
- **Biomarker Quality**: ER/PR/HER2 compliance for breast, MSI/MMR for colorectal

### Example Usage

**Basic compliance check:**
```bash
claude "Check this breast report for CAP compliance using pathology-compliance-checker" < report.txt
```

**Batch processing:**
```bash
for file in reports/*.txt; do
  claude "Check compliance using pathology-compliance-checker" < "$file" > "${file%.txt}_qa.txt"
done
```

### Output Format
```
COMPLIANCE ANALYSIS
Score: 85/100 (INCOMPLETE - MINOR)

MISSING ELEMENTS (3):
🔴 CRITICAL (1): ER/PR/HER2 status (-15 points)
🟠 MAJOR (2): LVI status (-5), PNI status (-5)

CROSS-VALIDATION:
✅ pT2 consistent with 2.3cm tumor
✅ pN1a consistent with 2 positive nodes

RECOMMENDATIONS:
1. Add ER/PR/HER2 biomarkers (CRITICAL)
2. Document LVI and PNI status (MAJOR)
```

### Severity Classification

**CRITICAL Elements (−15 points each):**
- pT category, pN category
- Margins, margin distance
- Histologic grade, histologic type
- ER/PR/HER2 (breast)
- Tumor size

**MAJOR Elements (−5 points each):**
- LVI, PNI status
- Tumor focality
- MSI/MMR status (colorectal)
- Biomarker quality

**MINOR Elements (−2 points each):**
- Gross description details
- Background pathology
- Additional findings

### Related Skills
- Use **template-generator** to fill missing elements
- Use **tnm-stage-calculator** to verify staging
- Use **breast/colorectal/pancreas/gastric-specialist** for tumor-specific compliance

---

## 2. Template Generator

**Skill name:** `pathology-template-generator`

### Purpose
Generate blank or pre-filled CAP-style synoptic report templates for surgical pathology specimens.

### When to Use
- Creating new pathology reports
- Training residents on synoptic reporting
- Standardizing department templates
- Pre-filling known values for faster dictation

### Supported Templates
- **Breast**: Lumpectomy, partial mastectomy, total mastectomy, modified radical mastectomy
- **Colorectal**: Colon resection, rectal resection (LAR/APR)
- **Pancreas**: Whipple, distal pancreatectomy, total pancreatectomy
- **Gastric**: Total gastrectomy, partial gastrectomy, wedge resection

### Languages
- English (EN)
- Turkish (TR)

### Key Features
- **Blank Templates**: All CAP-required, conditional, and recommended elements
- **Pre-fill Capability**: Auto-populate known values (size, grade, type)
- **Auto-Suggest**: Suggest pT/pN categories based on size/nodes
- **Field Markers**: `*` (required), `+` (conditional), `°` (recommended)

### Example Usage

**Blank template:**
```bash
claude "Generate a blank breast lumpectomy template using template-generator"
```

**Pre-filled template:**
```bash
claude "Generate breast lumpectomy template for 2.3cm Grade 2 invasive ductal carcinoma using template-generator"
```

**Turkish template:**
```bash
claude "Türkçe kolon rezeksiyon şablonu oluştur using template-generator"
```

### Auto-Fill Examples

**Tumor size → pT category:**
- 1.5 cm → pT1c suggested (>1–2cm)
- 2.3 cm → pT2 suggested (>2–5cm)
- 5.5 cm → pT3 suggested (>5cm)

**Node count → pN category:**
- 0 positive → pN0 suggested
- 2 positive → pN1a suggested (breast: 1-3 nodes)
- 5 positive → pN2a suggested (breast: 4-9 nodes)

### Output Format
```
═══════════════════════════════════════
BREAST - INVASIVE CARCINOMA
Synoptic Report Template
═══════════════════════════════════════

CLINICAL INFORMATION
───────────────────────────────────────
Clinical History: _______________
Laterality: (_) Right  (_) Left

SPECIMEN
───────────────────────────────────────
*Procedure:
  (_) Excision (lumpectomy)
  (_) Total mastectomy
...
```

### Related Skills
- Use **compliance-checker** to validate completed template
- Use **breast/colorectal/pancreas/gastric-specialist** for tumor-specific templates

---

## 3. TNM Stage Calculator

**Skill name:** `tnm-stage-calculator`

### Purpose
Calculate TNM stage groups from pT, pN, pM categories using AJCC 8th edition staging criteria.

### When to Use
- Quick staging lookups during sign-out
- Teaching TNM staging to residents
- Verifying report staging accuracy
- Prospective staging from clinical information

### Supported Tumor Types
- Breast cancer (AJCC 8th)
- Colorectal cancer (AJCC 8th)
- Pancreatic exocrine cancer (AJCC 8th)
- Gastric cancer (AJCC 8th)

### Key Features
- **Quick Lookup**: Fast stage group calculation
- **pT/pN Definitions**: Detailed category criteria
- **Stage Tables**: Complete staging tables included
- **Validation Mode**: Check report staging accuracy
- **Teaching Mode**: Expanded explanations for education

### Example Usage

**Calculate stage:**
```bash
claude "What stage is pT2 N1 M0 for breast cancer using tnm-stage-calculator?"
```

**Validate staging:**
```bash
claude "Verify staging: pT3 N2a M0 should be Stage IIIC for colorectal using tnm-stage-calculator"
```

**Teaching mode:**
```bash
claude "Explain pT categories for pancreatic cancer using tnm-stage-calculator"
```

### Output Format
```
BREAST CANCER STAGING (AJCC 8TH)

pT2 (tumor >2cm, ≤5cm: 2.3cm)
+ N1 (1-3 positive nodes: 2 nodes)
+ M0 (no distant metastasis)
= Stage IIB

Prognostic Factors:
- Tumor size: 2.3cm (T2)
- Nodal involvement: Limited (1-3 nodes)
- Overall: Intermediate risk

Treatment Implications:
- Adjuvant chemotherapy: Likely
- Endocrine therapy: If ER/PR+
- Radiation: Post-lumpectomy with nodes
```

### Stage Group Tables (Included)

**Breast:**
- Stage IA: T1 N0 M0
- Stage IB: T0-1 N1mi M0
- Stage IIA: T0-1 N1 M0, T2 N0 M0
- Stage IIB: T2 N1 M0, T3 N0 M0
- Stage IIIA: T0-2 N2 M0, T3 N1-2 M0
- Stage IIIB: T4 N0-2 M0
- Stage IIIC: Any T N3 M0
- Stage IV: Any T Any N M1

**Colorectal, Pancreas, Gastric:** See skill documentation for complete tables.

### Related Skills
- Use **compliance-checker** to validate pTNM in reports
- Use **breast/colorectal/pancreas/gastric-specialist** for tumor-specific staging

---

## 4. Pathology Coder

**Skill name:** `pathology-coder`

### Purpose
Suggest SNOMED CT and ICD-O-3 codes for pathology diagnoses, procedures, and biomarkers.

### When to Use
- LIS integration and database coding
- Tumor registry reporting
- Billing support (CPT codes)
- Standardizing terminology

### Supported Code Systems
- **SNOMED CT**: Morphology, topography, procedures
- **ICD-O-3**: Morphology codes with behavior (/0, /1, /2, /3, /6)
- **CPT**: Procedure billing codes (88305, 88307, 88309, 88360)

### Key Features
- **Morphology Codes**: Histologic type coding
- **Topography Codes**: Anatomic site coding
- **Procedure Codes**: Surgical pathology levels
- **Biomarker Codes**: ER/PR/HER2, MSI/MMR testing
- **Hierarchical Relationships**: SNOMED parent-child codes

### Example Usage

**Get diagnosis codes:**
```bash
claude "What's the SNOMED code for invasive ductal carcinoma using pathology-coder?"
```

**Get complete coding:**
```bash
claude "Code this: Grade 2 invasive lobular carcinoma, left breast, ER positive, HER2 negative using pathology-coder"
```

**Get procedure codes:**
```bash
claude "What CPT code for breast lumpectomy with margins using pathology-coder?"
```

### Output Format
```
SNOMED CT AND ICD-O-3 CODES

Morphology:
  SNOMED CT: 408643008 - Infiltrating duct carcinoma
  ICD-O-3: 8500/3 - Infiltrating duct carcinoma, NOS

Topography:
  SNOMED CT: T-04000 - Breast structure
  ICD-O-3: C50.9 - Breast, unspecified

Combined ICD-O-3: 8500/3 - C50.9

Procedures:
  CPT: 88307 - Level V, Breast excision with margins

Biomarkers:
  ER: CPT 88360, SNOMED CT 416053008
  HER2: CPT 88360, SNOMED CT 398991006
```

### Common Code Mappings

**Breast:**
- IDC: SNOMED 408643008, ICD-O-3 8500/3
- ILC: SNOMED 415380003, ICD-O-3 8520/3
- DCIS: SNOMED 399935008, ICD-O-3 8500/2

**Colorectal:**
- Adenocarcinoma NOS: SNOMED 443961001, ICD-O-3 8140/3
- Mucinous: SNOMED 72495009, ICD-O-3 8480/3
- Signet ring: SNOMED 87737001, ICD-O-3 8490/3

**Pancreas:**
- PDAC: SNOMED 254587008, ICD-O-3 8500/3

**Gastric:**
- Intestinal type: SNOMED 413102007, ICD-O-3 8144/3
- Diffuse type: SNOMED 413103002, ICD-O-3 8145/3

### Related Skills
- Use **compliance-checker** to verify all codeable elements are present
- Use **breast/colorectal/pancreas/gastric-specialist** for tumor-specific codes

---

## 5. Tumor Board Summary

**Skill name:** `pathology-tumor-board-summary`

### Purpose
Generate concise 3-5 line tumor board summaries from surgical pathology reports for MDT meetings.

### When to Use
- Multidisciplinary tumor board meetings
- Oncology consults
- Clinical summaries for referring physicians
- Case presentations

### Supported Formats
- Breast cancer summary (3-5 lines)
- Colorectal cancer summary (3-5 lines)
- Pancreatic cancer summary (3-5 lines)
- Gastric cancer summary (3-5 lines)

### Key Features
- **Concise Format**: Maximum 5 lines
- **Clinical Focus**: Treatment-relevant information only
- **Standard Structure**: Consistent format across tumor types
- **Abbreviations**: Standard medical abbreviations
- **Treatment Implications**: Key recommendations included

### Example Usage

**Generate summary:**
```bash
claude "Generate tumor board summary from this report using tumor-board-summary" < report.txt
```

**Batch summaries for MDT:**
```bash
for case in mdt_cases/*.txt; do
  claude "Generate tumor board summary using tumor-board-summary" < "$case"
done > mdt_summaries.txt
```

### Output Format

**Breast:**
```
52F with invasive breast carcinoma, left upper outer quadrant.
Lumpectomy: 2.3cm Grade 2 invasive ductal carcinoma, pT2 N1a M0 (Stage IIB).
Margins: Negative (closest 3mm). LVI present. Nodes: 2/15 positive.
Receptors: ER 90%, PR 70%, HER2 negative. Ki-67: 18%.
Resection: R0. Recommend Oncotype DX for chemotherapy decision.
```

**Colorectal:**
```
68M with sigmoid colon adenocarcinoma.
Sigmoid colectomy: 4.5cm moderately differentiated adenocarcinoma, pT3 N1b M0 (Stage IIIB).
Margins: Negative. LVI present. Nodes: 3/18 positive. MMR intact.
Resection: R0. Recommend adjuvant chemotherapy (FOLFOX or CAPOX).
```

**Pancreas:**
```
71M with pancreatic ductal adenocarcinoma, head of pancreas.
Whipple: 3.1cm moderately differentiated adenocarcinoma, pT2 N1 M0 (Stage IIB).
Margins: Negative (posterior 1.5mm). LVI present. PNI present. Nodes: 3/18.
Resection: R0. Recommend adjuvant FOLFIRINOX or gemcitabine + capecitabine.
```

**Gastric:**
```
63F with gastric adenocarcinoma, gastric body.
Total gastrectomy: 5.2cm intestinal type adenocarcinoma, pT3 N2 M0 (Stage IIIA).
Margins: Negative. LVI present. Nodes: 5/24 positive. HER2 positive (IHC 3+).
Resection: R0. HER2-positive (trastuzumab indication if metastatic).
```

### Summary Structure
```
Line 1: [Age][Sex] with [diagnosis], [location]
Line 2: [Specimen]: [Size]cm [grade] [type], pT[X] N[X] M0 (Stage [group])
Line 3: Margins: [status]. [LVI, PNI, deposits]. Nodes: [pos]/[total]
Line 4: [Biomarkers if applicable]
Line 5: Resection: R[X]. [Treatment implications]
```

### Related Skills
- Use **compliance-checker** before generating summary (ensure completeness)
- Use **tnm-stage-calculator** to verify staging in summary
- Use **breast/colorectal/pancreas/gastric-specialist** for tumor-specific summaries

---

## 6. Report Converter

**Skill name:** `pathology-report-converter`

### Purpose
Convert free-text narrative pathology reports to CAP synoptic format and generate amendments for existing reports.

### When to Use
- Legacy report migration to synoptic format
- Standardizing narrative reports
- Creating addenda for late results
- Generating corrections or amended reports

### Dual Functionality

**1. Free-Text to Synoptic Conversion**
- Extracts diagnostic elements from narrative prose
- Maps to CAP template fields
- Flags missing or ambiguous information
- Returns synoptic format with quality metrics

**2. Amendment Generation**
- Addendum: Add new information (late biomarkers, additional testing)
- Correction: Fix errors (wrong measurement, incorrect stage)
- Amended Report: Major changes (diagnosis revision, significant findings)

### Example Usage

**Convert narrative to synoptic:**
```bash
claude "Convert this report to synoptic format using report-converter" < narrative_report.txt
```

**Generate addendum:**
```bash
claude "Generate addendum for late HER2 FISH results using report-converter"
```

**Generate correction:**
```bash
claude "Create correction notice: tumor size should be 2.3cm not 3.2cm using report-converter"
```

### Conversion Output Format
```
═══════════════════════════════════════
CONVERTED SYNOPTIC REPORT
═══════════════════════════════════════
[Full synoptic report]

CONVERSION NOTES
═══════════════════════════════════════
Successfully Extracted (14 elements):
✅ Tumor size, type, grade, margins
✅ Nodes, pT, pN, stage, ER/PR/HER2

Missing from Original (6 elements):
⚠️ LVI status - MAJOR
⚠️ Ki-67 - RECOMMENDED

Conversion Quality: 70% (14/20)
```

### Amendment Output Format
```
═══════════════════════════════════════
ADDENDUM to Surgical Pathology Report
Case: S24-12345
═══════════════════════════════════════
Original Report Date: January 15, 2026
Addendum Date: January 18, 2026

HER2 FISH RESULTS:
HER2/CEP17 Ratio: 1.2
Interpretation: NOT AMPLIFIED

All other findings from original report remain unchanged.

Electronically signed by:
Dr. Jane Smith, MD
January 18, 2026
```

### Related Skills
- Use **compliance-checker** after conversion to validate quality
- Use **template-generator** to fill gaps in converted reports
- Use **breast/colorectal/pancreas/gastric-specialist** for tumor-specific conversion

---

## Specialist All-in-One Skills

## 7. Breast Specialist

**Skill name:** `pathology-breast-specialist`

### Purpose
Comprehensive breast cancer pathology toolkit combining all features focused exclusively on invasive breast carcinoma.

### When to Use
- Breast cancer centers
- Dedicated breast pathologists
- High-volume breast pathology practices
- Breast pathology fellowship training

### All Features Included
✅ CAP/ICCR compliance checking (breast-specific)
✅ Synoptic template generation (all breast specimens)
✅ TNM staging (AJCC 8th breast tables)
✅ Biomarker reporting (ER/PR/HER2/Ki-67 guidelines)
✅ Tumor board summaries (breast format)
✅ Report conversion (breast-specific)
✅ SNOMED coding (breast codes)

### Supported Specimens
- Lumpectomy / Partial mastectomy
- Re-excision (complete or select)
- Total mastectomy (simple)
- Modified radical mastectomy
- Skin-sparing mastectomy
- Nipple-sparing mastectomy

### Key Breast-Specific Features
- **Margin Assessment**: 6 margins (superior, inferior, medial, lateral, anterior, posterior/deep)
- **Biomarker Guidelines**: ASCO/CAP 2020 (ER/PR), ASCO/CAP 2018 (HER2)
- **Low Positive ER**: Special handling for 1-10% ER-positive
- **HER2 Equivocal**: Reflex to ISH per guidelines
- **Ki-67 Interpretation**: Correlation with Oncotype DX
- **Oncotype DX Correlation**: Predict recurrence score from biomarkers

### Example Usage

**Complete breast workflow:**
```bash
# Check compliance
claude "Check this breast lumpectomy report using breast-specialist" < report.txt

# Generate template
claude "Generate breast lumpectomy template for 2.3cm Grade 2 IDC using breast-specialist"

# Calculate staging
claude "Stage pT2 N1a M0 breast cancer using breast-specialist"

# Create summary
claude "Generate breast tumor board summary using breast-specialist" < report.txt
```

### Advantages Over Core Skills
- All breast features in one skill (no switching)
- Breast-specific biomarker guidance (ER/PR/HER2/Ki-67)
- Faster (no need to specify tumor type)
- Comprehensive breast workflows

### Related Skills
- Use **tnm-stage-calculator** for quick staging-only lookups
- Use **compliance-checker** if checking mixed tumor types

---

## 8. Colorectal Specialist

**Skill name:** `pathology-colorectal-specialist`

### Purpose
Comprehensive colorectal cancer pathology toolkit combining all features focused exclusively on colorectal carcinoma.

### When to Use
- GI pathology practices
- Dedicated GI pathologists
- Colorectal cancer programs
- GI pathology fellowship training

### All Features Included
✅ CAP/ICCR compliance checking (colorectal-specific)
✅ Synoptic template generation (colon and rectal specimens)
✅ TNM staging (AJCC 8th colorectal tables)
✅ MSI/MMR reporting (Lynch syndrome screening)
✅ Tumor board summaries (colorectal format)
✅ Report conversion (colorectal-specific)
✅ SNOMED coding (colorectal codes)

### Supported Specimens
- Right hemicolectomy
- Transverse colectomy
- Left hemicolectomy
- Sigmoid colectomy
- Low anterior resection (LAR)
- Abdominoperineal resection (APR)
- Total colectomy
- Polypectomy with invasion

### Key Colorectal-Specific Features
- **Circumferential Resection Margin (CRM)**: For rectal specimens (critical if ≤1mm)
- **Mesorectal Excision Quality**: Complete, nearly complete, incomplete (rectal)
- **MSI/MMR Testing**: Universal testing guidelines (NCCN)
- **Lynch Syndrome Screening**: MLH1 methylation algorithm
- **Tumor Deposits**: pN1c classification
- **Minimum 12 Nodes**: CAP adequacy requirement

### Example Usage

**Complete colorectal workflow:**
```bash
# Check compliance with CRM assessment
claude "Check this rectal LAR report using colorectal-specialist" < report.txt

# Generate rectal template
claude "Generate rectal LAR template using colorectal-specialist"

# MSI/MMR interpretation
claude "Interpret MMR IHC: Loss of MLH1/PMS2 using colorectal-specialist"

# Stage with node adequacy check
claude "Stage pT3 N1b M0 with 10 nodes examined using colorectal-specialist"
```

### Advantages Over Core Skills
- CRM and mesorectal excision assessment (rectal)
- MSI/MMR testing and Lynch screening guidance
- Tumor deposit classification
- Node adequacy validation (minimum 12)

### Related Skills
- Use **tnm-stage-calculator** for quick staging-only lookups
- Use **compliance-checker** if checking mixed tumor types

---

## 9. Pancreas Specialist

**Skill name:** `pathology-pancreas-specialist`

### Purpose
Comprehensive pancreatic cancer pathology toolkit combining all features focused exclusively on exocrine pancreas carcinoma.

### When to Use
- HPB (hepatopancreatobiliary) pathology
- Dedicated HPB pathologists
- Pancreatic cancer programs
- HPB surgery centers

### All Features Included
✅ CAP/ICCR compliance checking (pancreas-specific)
✅ Synoptic template generation (Whipple, distal, total pancreatectomy)
✅ TNM staging (AJCC 8th pancreas tables)
✅ Margin assessment (all 7 margins for Whipple)
✅ Tumor board summaries (pancreas format)
✅ Report conversion (pancreas-specific)
✅ SNOMED coding (pancreas codes)

### Supported Specimens
- Whipple (pancreaticoduodenectomy)
- Distal pancreatectomy
- Total pancreatectomy
- Enucleation

### Key Pancreas-Specific Features
- **Seven Margins for Whipple**: Superior, inferior, posterior, anterior, bile duct, pancreatic neck, duodenal
- **Vascular Involvement**: SMA, SMV, portal vein assessment
- **PNI Universality**: >90% of PDAC have PNI (flag if absent)
- **Lymph Node Ratio**: Prognostic significance (LNR >0.2)
- **Minimum 15 Nodes**: AJCC 8th recommendation
- **R0 vs R1**: Margin status critical (median survival difference ~8-10 months)

### Example Usage

**Complete pancreas workflow:**
```bash
# Check all 7 Whipple margins
claude "Check this Whipple report for all margins using pancreas-specialist" < report.txt

# Generate Whipple template
claude "Generate Whipple template using pancreas-specialist"

# Assess margin status
claude "Evaluate margins: posterior 1.5mm, superior 2mm, others >5mm using pancreas-specialist"

# Calculate LNR
claude "Calculate lymph node ratio: 3 positive out of 18 examined using pancreas-specialist"
```

### Advantages Over Core Skills
- All 7 Whipple margins explicitly checked
- Vascular involvement assessment (SMA, SMV, portal vein)
- PNI extent (focal vs. extensive)
- Lymph node ratio calculation and interpretation
- R0 vs R1 implications emphasized

### Related Skills
- Use **tnm-stage-calculator** for quick staging-only lookups
- Use **compliance-checker** if checking mixed tumor types

---

## 10. Gastric Specialist

**Skill name:** `pathology-gastric-specialist`

### Purpose
Comprehensive gastric cancer pathology toolkit combining all features focused exclusively on gastric carcinoma.

### When to Use
- Upper GI pathology practices
- Dedicated GI pathologists
- Gastric cancer programs
- GI pathology fellowship training

### All Features Included
✅ CAP/ICCR compliance checking (gastric-specific)
✅ Synoptic template generation (total, partial, wedge gastrectomy)
✅ TNM staging (AJCC 8th gastric tables)
✅ Lauren classification (intestinal/diffuse/mixed)
✅ HER2 testing guidelines (advanced disease)
✅ Tumor board summaries (gastric format)
✅ Report conversion (gastric-specific)
✅ SNOMED coding (gastric codes)

### Supported Specimens
- Total gastrectomy
- Partial/subtotal gastrectomy
- Proximal gastrectomy (with GEJ)
- Wedge resection
- Endoscopic resection (EMR/ESD)

### Key Gastric-Specific Features
- **Lauren Classification**: Intestinal, diffuse, mixed (CRITICAL element)
- **Borrmann Type**: Gross appearance types 1-4 (prognostic)
- **GEJ Distance**: Distance from gastroesophageal junction
- **Siewert Classification**: For GEJ tumors (Type I, II, III)
- **HER2 Testing**: Trastuzumab indication (metastatic disease)
- **Minimum 16 Nodes**: AJCC 8th requirement for pN3 substaging
- **Hereditary Diffuse Gastric Cancer**: CDH1 screening for young patients

### Example Usage

**Complete gastric workflow:**
```bash
# Check Lauren classification
claude "Check this gastric report, ensure Lauren type specified using gastric-specialist" < report.txt

# Generate total gastrectomy template
claude "Generate total gastrectomy template using gastric-specialist"

# Classify Lauren type
claude "Classify this as intestinal, diffuse, or mixed type using gastric-specialist"

# HER2 interpretation
claude "Interpret HER2: IHC 3+ in intestinal type adenocarcinoma using gastric-specialist"

# GEJ tumor classification
claude "Tumor 3cm from GEJ, classify using Siewert system using gastric-specialist"
```

### Advantages Over Core Skills
- Lauren classification guidance (mandatory)
- Borrmann type documentation
- GEJ distance and Siewert classification
- HER2 testing for gastric cancer (different scoring than breast)
- Hereditary diffuse gastric cancer screening
- pN3 substaging with 16-node requirement

### Related Skills
- Use **tnm-stage-calculator** for quick staging-only lookups
- Use **compliance-checker** if checking mixed tumor types

---

## Skill Selection Matrix

| Need | Core Skill | Specialist Skill | Best Choice |
|------|-----------|------------------|-------------|
| **Check breast report** | compliance-checker | breast-specialist | Specialist (biomarker guidance) |
| **Check colorectal report** | compliance-checker | colorectal-specialist | Specialist (CRM, MSI/MMR) |
| **Check pancreas report** | compliance-checker | pancreas-specialist | Specialist (7 margins) |
| **Check gastric report** | compliance-checker | gastric-specialist | Specialist (Lauren, HER2) |
| **Mixed caseload QA** | compliance-checker | N/A | Core (handles all types) |
| **Generate any template** | template-generator | Specialist | Either (similar functionality) |
| **Quick staging lookup** | tnm-stage-calculator | Specialist | Core (faster, focused) |
| **SNOMED codes only** | pathology-coder | Specialist | Core (faster, focused) |
| **Tumor board summaries** | tumor-board-summary | Specialist | Either (similar functionality) |
| **Convert old reports** | report-converter | N/A | Core (conversion-focused) |
| **Complete breast workflow** | Multiple core skills | breast-specialist | Specialist (all-in-one) |

---

## Common Workflows

### Workflow 1: New Report Sign-Out
```
1. Generate template (template-generator or specialist)
2. Dictate/fill report
3. Check compliance (compliance-checker or specialist)
4. Calculate stage (tnm-stage-calculator or specialist)
5. Get codes (pathology-coder or specialist)
6. Generate summary (tumor-board-summary or specialist)
```

### Workflow 2: Department QA
```
1. Batch check reports (compliance-checker)
2. Export scores to Excel
3. Identify common gaps
4. Generate improvement recommendations
5. Track trends over time
```

### Workflow 3: Resident Training
```
1. Show blank template (template-generator)
2. Have resident fill from case
3. Check completeness (compliance-checker)
4. Teach staging (tnm-stage-calculator)
5. Introduce coding (pathology-coder)
```

---

## Performance Comparison

| Skill | Size | Speed | Complexity | Token Usage |
|-------|------|-------|------------|-------------|
| compliance-checker | ~18 KB | Fast | Medium | ~5K tokens |
| template-generator | ~25 KB | Fast | Low | ~3K tokens |
| tnm-stage-calculator | ~12 KB | Very Fast | Low | ~2K tokens |
| pathology-coder | ~8 KB | Very Fast | Low | ~2K tokens |
| tumor-board-summary | ~5 KB | Very Fast | Low | ~1K tokens |
| report-converter | ~12 KB | Medium | High | ~8K tokens |
| breast-specialist | ~20 KB | Medium | Medium | ~7K tokens |
| colorectal-specialist | ~22 KB | Medium | Medium | ~7K tokens |
| pancreas-specialist | ~21 KB | Medium | Medium | ~7K tokens |
| gastric-specialist | ~23 KB | Medium | Medium | ~7K tokens |

---

Ready to use the skills! See [examples.md](examples.md) for complete workflow examples.
