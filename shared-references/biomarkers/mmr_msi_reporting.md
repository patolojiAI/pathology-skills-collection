# MMR/MSI Reporting Guidelines

**Version:** CAP/NCCN 2024 Update
**Application:** Colorectal and Other Solid Tumors
**Last Updated:** January 2026

---

## Testing Indications

### When to Order MMR/MSI Testing

**Required for (Universal Testing):**
- **All colorectal carcinomas** (regardless of age or family history) - CAP/NCCN recommendation
- **All endometrial carcinomas** - NCCN guideline recommendation
- Tumors with clinical suspicion of Lynch syndrome:
  - Patient age <50 years at diagnosis
  - Family history meeting Amsterdam II criteria
  - Personal history of Lynch-associated cancers

**Consider for:**
- Gastric adenocarcinoma
- Small bowel adenocarcinoma
- Pancreatic adenocarcinoma (if clinical Lynch syndrome suspicion)
- Sebaceous neoplasms
- Urothelial carcinoma (upper tract)
- Ovarian carcinoma (non-mucinous)
- Brain tumors (glioblastoma) in Lynch syndrome-associated families

**Clinical Utility:**
- **Lynch syndrome screening:** Identify patients needing genetic counseling
- **Prognostic marker:** MSI-high tumors have better prognosis in early-stage CRC
- **Predictive marker:** MSI-high predicts lack of benefit from 5-FU chemotherapy in stage II CRC
- **Immunotherapy eligibility:** MSI-high/dMMR tumors respond to PD-1 inhibitors (pembrolizumab, nivolumab)

---

## Testing Methodologies

### Mismatch Repair (MMR) Immunohistochemistry

**Proteins Tested (4-antibody panel):**
1. **MLH1** - MutL homolog 1
2. **PMS2** - PMS1 homolog 2 (binds to MLH1)
3. **MSH2** - MutS homolog 2
4. **MSH6** - MutS homolog 6 (binds to MSH2)

**Heterodimer Pairs:**
- MLH1/PMS2 (one heterodimer)
- MSH2/MSH6 (second heterodimer)

**Key Principle:** Loss of one protein in a pair leads to loss of its partner

---

### Microsatellite Instability (MSI) PCR Testing

**Methodology:**
- PCR amplification of microsatellite markers
- **Bethesda panel** (NCI 1997): 5 markers
  - BAT-25, BAT-26 (mononucleotide repeats)
  - D5S346, D2S123, D17S250 (dinucleotide repeats)

**Alternative panels:**
- **Promega panel:** 5 mononucleotide markers (BAT-25, BAT-26, NR-21, NR-24, MONO-27)
- **Pentaplex panel:** 5 quasimonomorphic markers

---

### Next-Generation Sequencing (NGS)

**Computational MSI Detection:**
- Analyze instability across hundreds of microsatellite loci
- Provides MSI-high, MSI-low, or MSS (microsatellite stable) classification
- **Advantage:** Can be determined from tumor-only sequencing
- **Limitation:** Requires adequate tumor content (≥20%)

---

## Interpretation Thresholds

### MMR IHC Interpretation

#### **MMR-Deficient (dMMR) = Abnormal:**
- **Complete loss** of nuclear staining in tumor cells for one or more MMR proteins
- Internal positive control (normal cells) must show retained staining

**Common Loss Patterns:**
1. **MLH1/PMS2 loss:**
   - Most common pattern (~60% of dMMR CRC)
   - Sporadic CRC (MLH1 promoter hypermethylation) **OR** Lynch syndrome (MLH1 germline mutation)
   - **Reflex testing:** MLH1 promoter methylation analysis or BRAF V600E mutation

2. **PMS2 loss only:**
   - Rare (~10% of dMMR CRC)
   - Usually Lynch syndrome (PMS2 germline mutation)
   - MLH1 retained

3. **MSH2/MSH6 loss:**
   - Moderately common (~20% of dMMR CRC)
   - Usually Lynch syndrome (MSH2 germline mutation)

4. **MSH6 loss only:**
   - Uncommon (~10% of dMMR CRC)
   - Lynch syndrome (MSH6 germline mutation)
   - MSH2 retained

#### **MMR-Proficient (pMMR) = Normal:**
- **Intact nuclear staining** in tumor cells for all 4 MMR proteins (MLH1, PMS2, MSH2, MSH6)
- Staining intensity equal to or greater than internal controls

---

### MSI PCR Interpretation

**MSI-High (MSI-H):**
- ≥2 of 5 markers show instability (Bethesda panel)
- ≥2 of 5 markers unstable (Promega panel)
- **Correlation:** ~95% concordance with dMMR by IHC

**MSI-Low (MSI-L):**
- 1 of 5 markers shows instability
- **Clinical significance:** Treat as MSS (microsatellite stable)
- Rare; often technical artifact

**Microsatellite Stable (MSS):**
- 0 of 5 markers show instability
- **Correlation:** ~95% concordance with pMMR by IHC

---

### NGS MSI Score Interpretation

**MSI-High:**
- Score threshold varies by platform (e.g., >10 on some systems, >20% on others)
- Consult platform-specific thresholds

**MSI-Stable:**
- Below threshold for MSI-high

---

## Quality Control

### IHC Quality Acceptance Criteria

**Internal Positive Controls:**
- **Normal colonic mucosa:** Should show intact nuclear staining for all 4 proteins
- **Lymphocytes:** Nuclear staining expected for all MMR proteins
- **Stromal cells:** Nuclear staining expected

**Technical Adequacy:**
- Nuclear staining only (cytoplasmic staining is non-specific)
- Adequate tumor present for evaluation
- Background/stromal cells serve as internal control

**Common Pitfalls:**
- **Weak staining:** Repeat with fresh section or different antibody clone
- **Cytoplasmic staining:** Not interpretable - repeat
- **No internal control:** Cannot interpret - repeat with control tissue

---

### PCR MSI Quality Criteria

**Tumor Content:**
- Minimum 20% tumor cellularity required
- Consider macrodissection if <20%

**Normal Tissue Control:**
- Paired normal tissue (non-neoplastic mucosa or blood) recommended
- Allows comparison of microsatellite lengths

**Amplification Quality:**
- All 5 markers must amplify successfully
- Clear peaks without artifacts

---

## Reflex Testing Logic

### Algorithmic Approach for Colorectal Carcinoma

```
Universal Screening: All CRC cases
      ↓
   MMR IHC (4 proteins)
      ↓
      ├─ pMMR (all 4 proteins retained) → MSS
      │     ↓
      │  No Lynch syndrome
      │  Standard chemotherapy
      │  Not eligible for PD-1 inhibitor monotherapy
      │
      └─ dMMR (loss of 1+ proteins)
            ↓
            ├─ MLH1/PMS2 loss → REFLEX TO:
            │     ↓
            │  1. MLH1 promoter methylation
            │     ├─ Methylated → Sporadic CRC (no Lynch syndrome)
            │     └─ Unmethylated → Suspect Lynch, refer to genetics
            │  OR
            │  2. BRAF V600E mutation
            │     ├─ Mutated → Sporadic CRC (no Lynch syndrome)
            │     └─ Wild-type → Suspect Lynch, refer to genetics
            │
            ├─ PMS2 loss only → Refer to genetic counseling (likely Lynch)
            ├─ MSH2/MSH6 loss → Refer to genetic counseling (likely Lynch)
            └─ MSH6 loss only → Refer to genetic counseling (likely Lynch)

All dMMR cases → Consider immunotherapy eligibility (PD-1 inhibitors)
```

---

## Reporting Template

### MMR IHC Report Format

```
MISMATCH REPAIR (MMR) PROTEIN EXPRESSION
(Immunohistochemistry)

Antibodies: MLH1, PMS2, MSH2, MSH6

Results:
  MLH1:  ☐ Retained  ☐ Lost
  PMS2:  ☐ Retained  ☐ Lost
  MSH2:  ☐ Retained  ☐ Lost
  MSH6:  ☐ Retained  ☐ Lost

Interpretation:
[Select one]
  ☐ MMR-PROFICIENT (pMMR)
     - Intact nuclear staining for all four MMR proteins (MLH1, PMS2, MSH2, MSH6) in tumor cells
     - Internal controls (normal colonic mucosa, lymphocytes) show appropriate staining

  ☐ MMR-DEFICIENT (dMMR)
     - Loss of nuclear staining for [specify proteins] in tumor cells
     - Internal controls show retained staining (appropriate)
     - Pattern suggests: [Select one]
       • Sporadic CRC (if MLH1/PMS2 loss with MLH1 hypermethylation or BRAF mutation)
       • Possible Lynch syndrome (germline testing recommended)

Comment:
- Universal screening per CAP/NCCN guidelines for Lynch syndrome detection
- dMMR tumors are eligible for PD-1 inhibitor immunotherapy (pembrolizumab, nivolumab)
- [If MLH1/PMS2 loss] Reflex testing for MLH1 promoter methylation or BRAF V600E recommended
- [If other protein loss] Genetic counseling referral recommended for Lynch syndrome evaluation
```

### MSI PCR Report Format

```
MICROSATELLITE INSTABILITY (MSI) ANALYSIS
(PCR-based)

Method: [Bethesda panel / Promega panel / Other]
Markers Tested: [List 5 markers]

Results:
  BAT-25:   ☐ Stable  ☐ Unstable
  BAT-26:   ☐ Stable  ☐ Unstable
  [Additional markers...]

  Unstable Markers: [X] of 5

Interpretation:
  ☐ MSI-HIGH (MSI-H): ≥2 of 5 markers unstable
  ☐ MSI-LOW (MSI-L): 1 of 5 markers unstable (treat as MSS)
  ☐ MICROSATELLITE STABLE (MSS): 0 of 5 markers unstable

Comment:
- MSI-H tumors correlate with MMR deficiency
- MSI-H is associated with better prognosis in early-stage CRC
- MSI-H predicts lack of benefit from 5-FU chemotherapy in stage II CRC
- MSI-H tumors are eligible for PD-1 inhibitor immunotherapy
- [If MSI-H] Recommend genetic counseling for Lynch syndrome evaluation
```

---

## Lynch Syndrome Screening Algorithm

### MLH1 Promoter Methylation Testing

**Indication:**
- dMMR with MLH1/PMS2 loss

**Interpretation:**
- **Methylated:** Sporadic CRC (somatic hypermethylation)
  - No Lynch syndrome
  - No germline testing needed
- **Unmethylated:** Suspicious for Lynch syndrome
  - Refer to genetic counseling for germline testing

---

### BRAF V600E Mutation Testing

**Indication:**
- dMMR with MLH1/PMS2 loss (alternative to MLH1 methylation)

**Interpretation:**
- **BRAF V600E mutated:** Sporadic CRC
  - >90% of BRAF-mutant CRC have sporadic MLH1 hypermethylation
  - Low likelihood of Lynch syndrome
- **BRAF wild-type:** Suspicious for Lynch syndrome
  - Refer to genetic counseling

**Note:** BRAF mutation and MLH1 methylation are highly correlated; either test is acceptable

---

## Special Scenarios

### Endometrial Carcinoma MMR Testing

**Indications:**
- Universal screening recommended per NCCN guidelines
- Same 4-antibody panel (MLH1, PMS2, MSH2, MSH6)

**Interpretation:**
- Same loss patterns as colorectal carcinoma
- MLH1/PMS2 loss common in sporadic endometrial cancer (MLH1 hypermethylation)
- Reflex MLH1 methylation testing recommended if MLH1/PMS2 lost

---

### Gastric Carcinoma MSI Testing

**Indications:**
- Consider in patients with family history of Lynch syndrome
- MSI-H found in ~20% of gastric cancers (often EBV-associated)

**Interpretation:**
- MSI-H gastric cancer may be sporadic or Lynch-associated
- Reflex testing (MLH1 methylation/BRAF) if MLH1/PMS2 loss

---

### Advanced/Metastatic CRC: MSI for Immunotherapy Eligibility

**Testing Indication:**
- All advanced/metastatic CRC to determine PD-1 inhibitor eligibility

**FDA-Approved Immunotherapies for MSI-H/dMMR:**
- **Pembrolizumab** (Keytruda): First-line or refractory
- **Nivolumab** (Opdivo): Refractory CRC (± ipilimumab combination)

**Reporting:** Explicitly state immunotherapy eligibility in report

---

## Common Pitfalls

### Pre-Analytical
- **Insufficient tumor:** <20% tumor cellularity may cause false-negative MSI
- **Poor fixation:** May cause false loss of staining by IHC

### Analytical
- **Suboptimal staining:** Weak or cytoplasmic staining is not interpretable
- **Failure to use internal controls:** Essential for IHC interpretation
- **Wrong tissue tested:** Test invasive carcinoma, not adenoma or in situ component

### Interpretive
- **Misinterpreting weak staining as loss:** Repeat with fresh section
- **Not recognizing heterogeneous loss:** Some areas may retain, some lose - score as lost if any tumor area lost
- **Failure to reflex test MLH1/PMS2 loss:** MLH1 methylation or BRAF required to distinguish sporadic from Lynch

---

## Quality Assurance

### Internal QA
- Annual proficiency testing for MMR IHC interpretation
- Quarterly review of dMMR cases to ensure reflex testing performed
- Monitor concordance between MMR IHC and MSI PCR when both performed

### External QA
- Participate in CAP proficiency testing programs
- External review of equivocal cases
- Track Lynch syndrome detection rates

---

## References

1. **Shia J, et al.** Immunohistochemistry versus microsatellite instability testing for screening colorectal cancer patients at risk for hereditary nonpolyposis colorectal cancer syndrome. *J Mol Diagn.* 2008;10(4):293-300.

2. **Giardiello FM, et al.** Guidelines on genetic evaluation and management of Lynch syndrome. *Gastroenterology.* 2014;147(2):502-526.

3. **CAP Colorectal Cancer Protocol** (Version 4.3.0.2, June 2023) - MMR/MSI testing recommendations

4. **NCCN Clinical Practice Guidelines: Genetic/Familial High-Risk Assessment: Colorectal** (Version 2.2024)

5. **Le DT, et al.** PD-1 Blockade in Tumors with Mismatch-Repair Deficiency. *N Engl J Med.* 2015;372(26):2509-2520.

---

**Document Control:**
- Created: January 2026
- Based on: CAP/NCCN 2024 MMR/MSI Testing Guidelines
- Next Review: Annually or upon guideline update
