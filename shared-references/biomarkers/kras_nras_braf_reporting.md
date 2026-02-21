# KRAS/NRAS/BRAF Reporting Guidelines

**Version:** NCCN/CAP 2024 Update
**Application:** Colorectal Carcinoma (Primary Application)
**Last Updated:** January 2026

---

## Overview

RAS (KRAS/NRAS) and BRAF mutation testing guides targeted therapy selection in metastatic colorectal cancer (mCRC). These mutations predict resistance or sensitivity to specific therapies.

---

## Testing Indications

### Colorectal Carcinoma (Primary Use)

**When to Order:**
- **All metastatic/advanced colorectal carcinomas** (stage IV)
- **Recurrent colorectal cancer** being considered for anti-EGFR therapy
- **Stage II-III CRC:** May be tested for prognostic information (institutional discretion)

**Timing:**
- Ideally at diagnosis of metastatic disease
- Before initiation of anti-EGFR therapy (cetuximab, panitumumab)

**Tissue Source:**
- Primary tumor or metastasis acceptable
- Fresh tissue preferred, but FFPE archival tissue acceptable

---

### Other Tumor Types (Secondary Applications)

- **Melanoma:** BRAF testing for vemurafenib/dabrafenib eligibility
- **Lung adenocarcinoma:** KRAS testing (less common, KRAS G12C inhibitors emerging)
- **Thyroid carcinoma:** BRAF testing for papillary thyroid cancer
- **Hairy cell leukemia:** BRAF V600E testing

---

## Clinical Significance

### Anti-EGFR Therapy Eligibility (Colorectal Cancer)

**Anti-EGFR Monoclonal Antibodies:**
- **Cetuximab (Erbitux)**
- **Panitumumab (Vectibix)**

**Eligibility Requirements:**
- **RAS wild-type** (KRAS and NRAS exons 2, 3, 4) = ELIGIBLE
- **RAS mutant** (any KRAS or NRAS mutation) = NOT ELIGIBLE (resistance predicted)

**Why RAS Matters:**
- RAS mutations cause constitutive EGFR pathway activation
- Anti-EGFR therapy ineffective if downstream RAS is mutated
- ~50-60% of mCRC have RAS mutations (primarily KRAS)

---

### BRAF V600E Mutation

**Clinical Significance in CRC:**
- **Poor prognostic marker:** BRAF V600E associated with worse survival
- **Predicts lack of benefit from anti-EGFR therapy** (even if RAS wild-type)
- **Associated with sporadic CRC:** Highly correlated with MLH1 hypermethylation (MSI-high)

**Targeted Therapy:**
- **Encorafenib + cetuximab + binimetinib:** FDA-approved for BRAF V600E mCRC (2020)

**Lynch Syndrome Screening:**
- BRAF V600E mutation suggests sporadic CRC (not Lynch syndrome) if MLH1/PMS2 loss present

---

## Testing Methodologies

### Next-Generation Sequencing (NGS) **[Preferred]**

**Advantages:**
- Simultaneous detection of KRAS, NRAS, BRAF, and other mutations
- Detects all clinically relevant exons/codons
- Comprehensive genomic profiling (may include PIK3CA, HER2, etc.)

**Panels:**
- Solid tumor panels (50-500 genes)
- Colorectal-focused panels (10-20 genes)

**Sensitivity:** High (≥5% variant allele frequency)

---

### PCR-Based Methods

**Real-Time PCR (qPCR):**
- Targets specific hotspot mutations (e.g., KRAS G12/G13, BRAF V600E)
- Rapid turnaround (1-2 days)
- High sensitivity

**Pyrosequencing:**
- Semi-quantitative
- Detects known and unknown mutations in targeted regions

**Limitation:** May miss rare mutations outside tested codons

---

### Sanger Sequencing **[Historical]**

- Less sensitive than NGS or PCR (~20% variant allele frequency)
- Detects unknown mutations in sequenced region
- Largely replaced by NGS

---

## Genes and Hotspot Mutations

### KRAS (Most Common - ~40% of CRC)

**Exon 2 (Codons 12-13):**
- G12D, G12V, G12C, G12S, G12A, G12R
- G13D

**Exon 3 (Codons 59-61):**
- A59T, Q61H, Q61L, Q61R

**Exon 4 (Codons 117-146):**
- K117N, A146T, A146V

**Most common:** G12D (15%), G12V (10%), G13D (7%)

---

### NRAS (~5-8% of CRC)

**Exon 2 (Codons 12-13):**
- G12D, G12V, G12C, G13R

**Exon 3 (Codons 59-61):**
- Q61K, Q61R, Q61L, Q61H

**Exon 4 (Codons 117-146):**
- A146T

---

### BRAF (~10% of CRC)

**Exon 15:**
- **V600E** (>95% of BRAF mutations in CRC)
- V600K, V600R, V600M (rare)

**Non-V600 mutations:** Less common in CRC, significance uncertain

---

## Reporting Template

```
RAS/BRAF MUTATION ANALYSIS

Tumor Type: Colorectal Adenocarcinoma [or other]
Specimen: [Primary tumor / Metastasis - specify site]
Method: [NGS / PCR / Pyrosequencing]
Tumor Content: ___% (minimum 20% required)

KRAS (exons 2, 3, 4):
  ☐ Wild-type (no mutations detected)
  ☐ Mutant: [Specify mutation, e.g., G12D, G12V, G13D]
     - Exon 2: [Wild-type / Mutation]
     - Exon 3: [Wild-type / Mutation]
     - Exon 4: [Wild-type / Mutation]

NRAS (exons 2, 3, 4):
  ☐ Wild-type (no mutations detected)
  ☐ Mutant: [Specify mutation, e.g., Q61K]
     - Exon 2: [Wild-type / Mutation]
     - Exon 3: [Wild-type / Mutation]
     - Exon 4: [Wild-type / Mutation]

BRAF (exon 15):
  ☐ Wild-type (no V600E or other mutations detected)
  ☐ Mutant: [Specify mutation, e.g., V600E]

RAS Status Summary:
  ☐ RAS WILD-TYPE (KRAS and NRAS wild-type)
     → Anti-EGFR therapy (cetuximab, panitumumab) may be considered
  ☐ RAS MUTANT (KRAS and/or NRAS mutation detected)
     → Anti-EGFR therapy NOT recommended (resistance predicted)

BRAF Status:
  ☐ BRAF wild-type
  ☐ BRAF V600E mutant
     → Poor prognostic marker; consider encorafenib + cetuximab + binimetinib
     → If MLH1/PMS2 loss: Suggests sporadic CRC (not Lynch syndrome)

Comment:
- Testing performed per NCCN guidelines for metastatic colorectal cancer
- [If RAS wild-type]: Anti-EGFR therapy eligibility confirmed; BRAF status also relevant
- [If RAS mutant]: Anti-EGFR therapy not recommended
- [If BRAF V600E]: Associated with poor prognosis; targeted therapy available
- Method sensitivity: [Specify, e.g., ≥5% variant allele frequency for NGS]
```

---

## Interpretation

### Therapeutic Decision Algorithm (mCRC)

```
RAS/BRAF Testing
   ↓
   ├─ RAS WILD-TYPE + BRAF WILD-TYPE
   │     → Anti-EGFR therapy ELIGIBLE (cetuximab, panitumumab)
   │     → Good prognosis
   │
   ├─ RAS WILD-TYPE + BRAF V600E MUTANT
   │     → Anti-EGFR therapy generally NOT recommended
   │     → Consider encorafenib + cetuximab + binimetinib (FDA-approved)
   │     → Poor prognosis
   │
   └─ RAS MUTANT (any KRAS or NRAS mutation)
         → Anti-EGFR therapy NOT ELIGIBLE (resistance predicted)
         → BRAF status less critical for anti-EGFR decision
         → Consider alternative chemotherapy regimens
```

---

### Prognostic Implications

**KRAS Mutations:**
- Modest negative prognostic impact in some studies
- Codon 13 (G13D) may have slightly better prognosis than codon 12

**BRAF V600E:**
- **Strong negative prognostic marker** (median survival ~12-18 months in mCRC)
- Associated with right-sided tumors, mucinous histology, MSI-high

**RAS/BRAF Wild-Type:**
- Best prognosis in mCRC
- Eligible for all treatment options

---

## Quality Control

### Pre-Analytical Requirements

**Tumor Content:**
- Minimum 20% tumor cellularity required
- Macrodissection recommended if <50% tumor

**Specimen Type:**
- FFPE tissue acceptable (archival or fresh)
- Primary tumor or metastasis (results generally concordant)

**Fixation:**
- Standard formalin fixation (6-72 hours)

---

### Analytical Quality

**Sensitivity:**
- NGS: Detects ≥5% variant allele frequency
- PCR methods: Variable (5-10%)
- Sanger sequencing: ~20% (inadequate for clinical use)

**Controls:**
- Positive control (known mutation)
- Negative control (wild-type)
- No-template control

---

## Special Scenarios

### Discordant Primary vs. Metastasis

**Frequency:** Rare (<5%)

**Approach:**
- If discordant, test additional tissue if available
- Use most recent biopsy (tumor evolution possible)
- Consider technical issues (low tumor content, fixation)

---

### Post-Treatment Testing

**Re-testing indications:**
- Initial test >2 years old
- Clinical progression on anti-EGFR therapy (acquired resistance)
- New metastatic site

**Acquired Resistance:**
- Rare emergence of RAS mutations after anti-EGFR therapy
- Consider repeat biopsy if progression on anti-EGFR therapy

---

### Multiple RAS Mutations (Rare)

**Interpretation:**
- Report all mutations detected
- Any RAS mutation = anti-EGFR resistance

---

## Common Pitfalls

**Pre-Analytical:**
- Insufficient tumor content (<20%)
- Wrong tissue tested (adenoma instead of carcinoma)

**Analytical:**
- Testing only KRAS exon 2 (outdated): Must test KRAS exons 2/3/4 and NRAS exons 2/3/4
- Low-sensitivity method missing low-frequency mutations

**Reporting:**
- Failure to provide clear anti-EGFR eligibility statement
- Not specifying which exons were tested
- Reporting "KRAS wild-type" when only exon 2 tested (incomplete)

---

## References

1. **Sepulveda AR, et al.** Molecular Biomarkers for the Evaluation of Colorectal Cancer: Guideline from the American Society for Clinical Pathology, College of American Pathologists, Association for Molecular Pathology, and American Society of Clinical Oncology. *J Mol Diagn.* 2017;19(2):187-225.

2. **NCCN Clinical Practice Guidelines: Colon Cancer** (Version 1.2024)

3. **Karapetis CS, et al.** K-ras Mutations and Benefit from Cetuximab in Advanced Colorectal Cancer. *N Engl J Med.* 2008;359(17):1757-1765.

4. **Kopetz S, et al.** Encorafenib, Binimetinib, and Cetuximab in BRAF V600E-Mutated Colorectal Cancer. *N Engl J Med.* 2019;381(17):1632-1643.

---

**Document Control:**
Created: January 2026
Based on: NCCN/CAP 2024 RAS/BRAF Testing Guidelines
Next Review: Annually or upon guideline update
