# PD-L1 Reporting Guidelines

**Version:** FDA/CAP 2024 Recommendations
**Application:** Multiple Solid Tumors
**Last Updated:** January 2026

---

## Overview

PD-L1 (Programmed Death-Ligand 1) testing is a companion or complementary diagnostic for immune checkpoint inhibitor therapy. Multiple assays exist with tumor-specific scoring algorithms and cutoffs.

---

## Testing Indications by Tumor Type

### Non-Small Cell Lung Cancer (NSCLC)
- **FDA-approved assays:** 22C3, 28-8, SP263, SP142
- **Indications:** All advanced/metastatic NSCLC for immunotherapy eligibility

### Gastric/Gastroesophageal Junction Adenocarcinoma
- **FDA-approved assay:** 22C3 (pembrolizumab)
- **Scoring:** Combined Positive Score (CPS)

### Urothelial Carcinoma
- **FDA-approved assays:** 22C3, SP263, SP142
- **Indications:** Advanced urothelial carcinoma

### Triple-Negative Breast Cancer (TNBC)
- **FDA-approved assay:** SP142 (atezolizumab + chemotherapy)
- **Scoring:** Immune Cell (IC) score

### Other Tumors
- Head & neck squamous cell carcinoma (22C3)
- Cervical cancer (22C3)
- Esophageal squamous cell carcinoma (22C3)

---

## Scoring Methods

### Tumor Proportion Score (TPS)

**Definition:** Percentage of viable tumor cells with partial or complete membrane staining

**Calculation:**
```
TPS = (Number of PD-L1+ tumor cells / Total viable tumor cells) × 100
```

**Interpretation (NSCLC with 22C3):**
- **High expression:** TPS ≥50% (pembrolizumab monotherapy, first-line)
- **Positive expression:** TPS ≥1% (pembrolizumab + chemotherapy)
- **Negative:** TPS <1%

**Used for:** NSCLC, urothelial carcinoma

---

### Combined Positive Score (CPS)

**Definition:** Number of PD-L1+ cells (tumor + lymphocytes + macrophages) divided by total viable tumor cells × 100

**Calculation:**
```
CPS = (PD-L1+ tumor cells + PD-L1+ immune cells) / Total viable tumor cells × 100
```

**Interpretation (Gastric/GEJ with 22C3):**
- **CPS ≥1:** Pembrolizumab eligible (combined with chemotherapy)
- **CPS ≥10:** Enhanced benefit

**Used for:** Gastric, head & neck, cervical, esophageal

**Key Difference from TPS:** Includes immune cells in numerator

---

### Immune Cell (IC) Score

**Definition:** Percentage of tumor area occupied by PD-L1+ immune cells (tumor-infiltrating lymphocytes, macrophages)

**Scoring (SP142 for TNBC):**
- **IC3:** ≥10% immune cell staining (atezolizumab eligible)
- **IC2:** ≥5% to <10%
- **IC1:** ≥1% to <5%
- **IC0:** <1%

**Used for:** Triple-negative breast cancer (SP142), urothelial carcinoma

---

## FDA-Approved PD-L1 Assays

### 22C3 pharmDx (Dako/Agilent)

**Companion diagnostic for:**
- **Pembrolizumab (Keytruda)**
  - NSCLC (TPS ≥1%, ≥50%)
  - Gastric/GEJ (CPS ≥1)
  - Head & neck SCC (CPS ≥1)
  - Urothelial (CPS ≥10)
  - Cervical (CPS ≥1)
  - Esophageal SCC (CPS ≥10)

**Scoring:** TPS or CPS (tumor-dependent)

---

### 28-8 pharmDx (Dako/Agilent)

**Complementary diagnostic for:**
- **Nivolumab (Opdivo):** NSCLC

**Scoring:** TPS (≥1%, ≥5%, ≥10%)

---

### SP263 (Ventana/Roche)

**Complementary diagnostic for:**
- **Durvalumab (Imfinzi):** NSCLC, urothelial
- **Atezolizumab (Tecentriq):** NSCLC, urothelial

**Scoring:** TPS (≥25% for NSCLC) or IC (urothelial)

---

### SP142 (Ventana/Roche)

**Companion diagnostic for:**
- **Atezolizumab (Tecentriq):** Triple-negative breast cancer, urothelial

**Scoring:** IC score (≥10% for TNBC)

---

## Reporting Template

```
PD-L1 EXPRESSION (Immunohistochemistry)

Tumor Type: [NSCLC / Gastric / Urothelial / TNBC / Other]
Assay: [22C3 / 28-8 / SP263 / SP142]
Platform: [Dako Autostainer / Ventana BenchMark]

Scoring Method: [TPS / CPS / IC]

Result:
[For TPS]
  Tumor Proportion Score (TPS): ____%
  Interpretation:
    ☐ High expression (TPS ≥50%)
    ☐ Positive expression (TPS ≥1%)
    ☐ Negative (TPS <1%)

[For CPS]
  Combined Positive Score (CPS): ___
  Interpretation:
    ☐ CPS ≥10 (high expression)
    ☐ CPS ≥1 (positive expression)
    ☐ CPS <1 (negative)

[For IC]
  Immune Cell (IC) Score:
    ☐ IC3 (≥10%)
    ☐ IC2 (≥5% to <10%)
    ☐ IC1 (≥1% to <5%)
    ☐ IC0 (<1%)

Adequacy:
  ☐ Adequate (≥100 viable tumor cells evaluated)
  ☐ Insufficient tumor (<100 viable cells) - see comment

Comment:
- Testing performed per FDA-approved assay [22C3/28-8/SP263/SP142]
- [Drug name] eligibility: [Eligible / Not eligible / See threshold]
- PD-L1 expression is a dynamic biomarker; clinical context required
- [If inadequate]: Recommend testing on alternative specimen
```

---

## Quality Control

### Pre-Analytical Requirements

**Specimen:**
- Formalin-fixed, paraffin-embedded (FFPE)
- Adequate tumor content (≥100 viable tumor cells minimum)
- Fresh tissue preferred over archived (PD-L1 may degrade over time)

**Fixation:**
- 10% neutral buffered formalin
- Fixation time: 6-72 hours
- Avoid over-fixation (may reduce staining)

---

### Analytical Quality

**Controls:**
- **Positive control:** Tonsil (surface epithelium shows PD-L1+ staining)
- **Negative control:** Negative reagent control

**Staining Pattern:**
- Membrane staining (partial or complete circumferential)
- Cytoplasmic staining is NOT scored

**Adequacy:**
- Minimum 100 viable tumor cells required for scoring
- If <100 cells, report as "insufficient for PD-L1 evaluation"

---

## Interpretation Challenges

### Tumor Heterogeneity
- PD-L1 expression can be heterogeneous within tumor
- Score entire tumor area represented on slide
- If multiple slides, score slide with highest expression (per FDA guidance)

### Immune Cell Infiltration
- Dense immune infiltrate may obscure tumor cells
- Carefully distinguish tumor from immune cells
- CD45 or cytokeratin IHC may help if needed

### Cytoplasmic Staining
- Only membrane staining counts
- Cytoplasmic staining without membrane component = negative

### Decalcified Specimens
- Decalcification may reduce PD-L1 staining
- Use EDTA (not acid) if decalcification required
- Note decalcification in report

---

## Special Scenarios

### NSCLC Resection vs Biopsy
- PD-L1 can be tested on small biopsies or resections
- Results generally concordant
- If discordant, consider tumor heterogeneity

### Repeat Testing After Therapy
- PD-L1 expression may change after chemotherapy/radiation
- Consider re-testing if clinical scenario warrants

### Multiple Assays Available
- Assays show high concordance for high TPS (≥50%)
- Moderate concordance at lower cutoffs (1-49%)
- Use FDA-approved assay for specific drug

---

## Common Pitfalls

- **Scoring cytoplasmic staining:** Only membrane staining is valid
- **Scoring necrotic tumor:** Count only viable tumor cells
- **Insufficient tumor:** <100 cells invalidates result
- **Wrong scoring method:** Use TPS for NSCLC (22C3), CPS for gastric (22C3)
- **Ignoring immune cells in CPS:** CPS includes PD-L1+ lymphocytes/macrophages

---

## References

1. **Hirsch FR, et al.** PD-L1 Immunohistochemistry Assays for Lung Cancer: Results from Phase 1 of the Blueprint PD-L1 IHC Assay Comparison Project. *J Thorac Oncol.* 2017;12(2):208-222.

2. **Büttner R, et al.** Programmed Death-Ligand 1 Immunohistochemistry Testing: A Review of Analytical Assays and Clinical Implementation in Non-Small-Cell Lung Cancer. *J Clin Oncol.* 2017;35(34):3867-3876.

3. **FDA Guidance:** Principles for Codevelopment of an In Vitro Companion Diagnostic Device with a Therapeutic Product (2016)

4. **CAP/IASLC/AMP PD-L1 Testing Guideline** (2021 Update)

---

**Document Control:**
Created: January 2026
Based on: FDA/CAP 2024 PD-L1 Testing Guidelines
Next Review: Annually or upon guideline update
