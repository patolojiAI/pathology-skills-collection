# HER2 Reporting Guidelines

**Version:** ASCO/CAP 2018 Update
**Application:** Breast Carcinoma
**Last Updated:** January 2026

---

## Testing Indications

### When to Order HER2 Testing

**Required for:**
- All newly diagnosed invasive breast carcinomas
- Recurrent breast cancer (if not previously tested or if >5 years since original diagnosis)
- Metastatic disease from breast primary

**May be deferred for:**
- Pure ductal carcinoma in situ (DCIS) without invasion
- Microinvasive carcinoma (<1mm invasion) - institutional discretion

**Reflex testing indications:**
- IHC 2+ (equivocal) → Reflex to FISH
- IHC result discordant with clinical presentation → Consider FISH

---

## Interpretation Thresholds

### HER2 Immunohistochemistry (IHC)

**Scoring Criteria (ASCO/CAP 2018):**

**Positive (IHC 3+):**
- Strong, complete membrane staining
- >10% of invasive tumor cells
- Circumferential staining resembling "chicken-wire" pattern
- **Clinical Action:** HER2-targeted therapy indicated

**Equivocal (IHC 2+):**
- Weak-to-moderate, complete membrane staining
- >10% of invasive tumor cells
- OR strong, complete membrane staining in ≤10% of cells
- **Clinical Action:** Reflex to FISH testing required

**Negative (IHC 1+):**
- Incomplete, faint/barely perceptible membrane staining
- >10% of invasive tumor cells
- **Clinical Action:** HER2-targeted therapy not indicated

**Negative (IHC 0):**
- No staining or membrane staining in <10% of tumor cells
- **Clinical Action:** HER2-targeted therapy not indicated

---

### HER2 Fluorescence In Situ Hybridization (FISH)

**Updated Interpretation Criteria (ASCO/CAP 2018):**

#### **Positive (Amplified):**
- HER2/CEP17 ratio ≥2.0, **OR**
- Average HER2 copy number ≥6.0 signals/cell

#### **Negative (Not Amplified):**
- HER2/CEP17 ratio <2.0 **AND** average HER2 <4.0 signals/cell

#### **Equivocal (ISH Group 2):**
- HER2/CEP17 ratio <2.0 **BUT** average HER2 ≥4.0 and <6.0 signals/cell
- **Clinical Action:** Recount on same specimen, test alternative specimen, or consider IHC if FISH was initial test

#### **Equivocal (ISH Group 4):**
- HER2/CEP17 ratio ≥2.0 **BUT** average HER2 <4.0 signals/cell (rare)
- **Clinical Action:** Recount, test alternative specimen, or reflex to IHC

---

## Quality Control

### IHC Quality Acceptance Criteria

**External Controls:**
- **Positive control:** Known HER2 3+ breast carcinoma
- **Negative control:** Known HER2 0 or 1+ breast carcinoma
- Both controls must show expected results

**Internal Controls:**
- Normal ductal epithelium: 0 or 1+ staining expected
- Myoepithelial cells: Negative expected

**Technical Adequacy:**
- Fixation: 6-72 hours in 10% neutral buffered formalin
- Time to fixation: <1 hour from excision (ideally)
- Avoid decalcification with strong acids

---

### FISH Quality Acceptance Criteria

**Signal Quality:**
- ≥20 evaluable cells counted per case
- ≥2 observers or double-count if equivocal
- Clear, distinct signals with minimal background

**Control Probes:**
- HER2 probe (orange/red)
- CEP17 probe (green) - centromere of chromosome 17

**Technical Adequacy:**
- Adequate tissue preservation
- Minimal autofluorescence
- Distinct nuclear borders visible

---

## Reflex Testing Logic

### Algorithmic Approach

```
Initial Test: IHC
   ↓
   ├─ IHC 3+ → POSITIVE (HER2-targeted therapy)
   ├─ IHC 0 or 1+ → NEGATIVE (no HER2-targeted therapy)
   └─ IHC 2+ → REFLEX TO FISH
              ↓
              ├─ FISH Positive → POSITIVE (HER2-targeted therapy)
              ├─ FISH Negative → NEGATIVE (no HER2-targeted therapy)
              └─ FISH Equivocal → Recount/alternative specimen/IHC on FISH block
```

### Alternative: FISH-First Approach

For institutions using FISH as primary test:
```
Initial Test: FISH
   ↓
   ├─ FISH Positive → POSITIVE (HER2-targeted therapy)
   ├─ FISH Negative → NEGATIVE (no HER2-targeted therapy)
   └─ FISH Equivocal → REFLEX TO IHC or recount
```

---

## Reporting Template

### IHC Report Format

```
HER2 PROTEIN EXPRESSION (Immunohistochemistry)

Method: [Antibody clone, vendor, platform]
Result: [Select one]
  ☐ POSITIVE (IHC 3+)
  ☐ EQUIVOCAL (IHC 2+) - FISH recommended
  ☐ NEGATIVE (IHC 1+)
  ☐ NEGATIVE (IHC 0)

Interpretation:
[IHC 3+]: Strong, complete membrane staining in >10% of invasive tumor cells.
[IHC 2+]: Weak-to-moderate, complete membrane staining in >10% of invasive tumor cells.
[IHC 1+]: Incomplete, faint membrane staining in >10% of invasive tumor cells.
[IHC 0]: No staining or membrane staining in <10% of invasive tumor cells.

Comment:
- Testing performed per ASCO/CAP 2018 guidelines
- [For IHC 2+] Reflex FISH testing is recommended for definitive classification
```

### FISH Report Format

```
HER2 GENE AMPLIFICATION (Fluorescence In Situ Hybridization)

Method: [Probe system, vendor]
Cells Counted: [Number] invasive tumor cells

Results:
  HER2/CEP17 Ratio: [X.XX]
  Average HER2 Signals/Cell: [X.X]
  Average CEP17 Signals/Cell: [X.X]

Interpretation: [Select one]
  ☐ POSITIVE for HER2 gene amplification (ISH Group 1 or 5)
  ☐ NEGATIVE for HER2 gene amplification (ISH Group 3)
  ☐ EQUIVOCAL for HER2 gene amplification (ISH Group 2 or 4)

[POSITIVE]: HER2/CEP17 ratio ≥2.0 and/or average HER2 signals ≥6.0/cell.
[NEGATIVE]: HER2/CEP17 ratio <2.0 and average HER2 signals <4.0/cell.
[EQUIVOCAL]: HER2/CEP17 ratio <2.0 but average HER2 signals ≥4.0 and <6.0/cell (ISH Group 2).

Comment:
- Testing performed per ASCO/CAP 2018 guidelines
- [For EQUIVOCAL] Recommend recount, alternative specimen, or IHC correlation
- [For POSITIVE] HER2-targeted therapy may be considered
```

---

## Special Scenarios

### Heterogeneous HER2 Expression

**Definition:** Mix of HER2-positive and HER2-negative populations in same tumor

**Reporting Approach:**
- Report percentage of tumor with each HER2 score
- Example: "IHC 3+ in 40% of tumor, IHC 0 in 60%"
- Overall classification based on highest score (if >10% of cells)
- Consider FISH if heterogeneity creates uncertainty

**Clinical Significance:** Heterogeneous cases may have variable response to HER2-targeted therapy

---

### Post-Neoadjuvant HER2 Testing

**Considerations:**
- Tumor biology may change after neoadjuvant therapy
- Recommend repeat HER2 testing on residual tumor if:
  - >10% residual invasive carcinoma present
  - Original HER2 status uncertain or equivocal
  - Clinical trial enrollment consideration

**Reporting:** Indicate "post-neoadjuvant" status in comment

---

### Metastatic/Recurrent Disease HER2 Testing

**Indications for re-testing:**
- Original HER2 status unknown
- Original test >5 years ago
- Discordance between clinical behavior and HER2 status
- Access to HER2-targeted therapy for metastatic disease

**Reporting:** Compare to prior HER2 status if available

---

## Common Pitfalls

### Pre-Analytical Issues
- **Under-fixation:** False negative IHC (weak staining)
- **Over-fixation:** False negative IHC (antigen destruction)
- **Delayed fixation:** Variable results
- **Decalcification:** May cause false negative IHC

### Analytical Issues
- **Edge artifact:** Avoid scoring peripheral tumor edges (cautery artifact)
- **Cytoplasmic staining:** Do not score - only membrane staining counts
- **In situ component:** Score only invasive carcinoma
- **Chromosome 17 polysomy:** May cause low HER2/CEP17 ratio despite HER2 amplification (use average HER2 copy number)

### Reporting Issues
- **Failure to reflex test IHC 2+:** ASCO/CAP requires FISH for equivocal IHC
- **Scoring DCIS instead of invasive carcinoma:** Ensure invasive component is evaluated
- **Failure to comment on technical adequacy:** Note fixation quality

---

## Quality Assurance Recommendations

### Internal QA
- Annual proficiency testing for IHC and FISH interpreters
- Monitor reflex testing compliance (IHC 2+ → FISH)
- Quarterly review of equivocal cases
- Track concordance between IHC and FISH when both performed

### External QA
- Participate in CAP/ASCO HER2 proficiency testing programs
- Submit to external quality assurance schemes
- Benchmark turnaround times and error rates

---

## References

1. **Wolff AC, et al.** Human Epidermal Growth Factor Receptor 2 Testing in Breast Cancer: American Society of Clinical Oncology/College of American Pathologists Clinical Practice Guideline Focused Update. *J Clin Oncol.* 2018;36(20):2105-2122.

2. **ASCO/CAP HER2 Testing Guideline 2018** - Full update available at www.cap.org and www.asco.org

3. **CAP Breast Biomarker Reporting Template** (Version 4.3.0.0, October 2023)

4. **FDA-Approved HER2 Testing Systems** - Consult current FDA listings for validated assays

---

**Document Control:**
- Created: January 2026
- Based on: ASCO/CAP 2018 HER2 Testing Guidelines
- Next Review: Annually or upon guideline update
