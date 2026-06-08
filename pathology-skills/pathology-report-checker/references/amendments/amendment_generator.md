# Amendment Generator

Generate standardized amendment text for pathology reports requiring corrections or additions.

## Purpose

Create professional amendment language for:
- Missing required elements
- Incorrect staging
- Updated biomarker results
- Typographical errors
- Additional findings
- Margin or node count revisions

---

## Amendment Types

| Type | Use Case | Priority |
|------|----------|----------|
| **Addendum** | New information, additional studies | Routine |
| **Correction** | Error in original report | Urgent |
| **Amended Report** | Significant changes affecting diagnosis/staging | Critical |

### When to Use Each

| Scenario | Type |
|----------|------|
| IHC results now available | Addendum |
| Additional deeper levels reviewed | Addendum |
| Tumor size measurement error | Correction |
| Wrong laterality stated | Correction |
| pT/pN category incorrect | Amended Report |
| Margin status changed | Amended Report |
| Node count revised | Amended Report |
| Biomarker interpretation changed | Amended Report |

---

## Standard Amendment Structure

### Header Format

```
═══════════════════════════════════════════════════════════════
AMENDED REPORT / ADDENDUM / CORRECTION
═══════════════════════════════════════════════════════════════

Original Report Date: [DATE]
Amendment Date: [DATE]
Amendment Time: [TIME]
Amended By: [PATHOLOGIST NAME], MD
Reason for Amendment: [CATEGORY]

═══════════════════════════════════════════════════════════════
```

### Body Format

```
SUMMARY OF CHANGES:
[Brief 1-2 sentence summary of what changed]

ORIGINAL TEXT:
"[Exact text being corrected]"

AMENDED TEXT:
"[Corrected text]"

RATIONALE:
[Explanation of why change was made]

CLINICAL IMPACT:
[Statement about whether staging/treatment affected]
```

### Footer Format

```
═══════════════════════════════════════════════════════════════
All other findings in the original report remain unchanged.
═══════════════════════════════════════════════════════════════
```

---

## Amendment Templates by Category

### 1. Missing Staging Elements

**Template:**
```
ADDENDUM

Original Report Date: ___________
Addendum Date: ___________

REASON: Addition of pathologic staging

ADDED INFORMATION:

Pathologic Stage (AJCC 8th Edition):
   pT: ___
   pN: ___
   pM: ___
   Stage Group: ___

RATIONALE:
Staging was not included in the original synoptic report. 
This addendum provides the pathologic stage based on the 
findings documented in the original report.

All other findings remain unchanged.
```

**Example:**
```
ADDENDUM

Original Report Date: December 28, 2024
Addendum Date: December 29, 2024

REASON: Addition of pathologic staging

ADDED INFORMATION:

Pathologic Stage (AJCC 8th Edition):
   pT: pT2 (tumor >2 cm but ≤5 cm)
   pN: pN1a (metastases in 1-3 axillary lymph nodes)
   pM: Not applicable
   Stage Group: IIB

RATIONALE:
Pathologic staging was inadvertently omitted from the original 
synoptic report. Based on the 2.3 cm tumor size and 2 of 15 
positive axillary lymph nodes, the stage is pT2 N1a M0, Stage IIB.

All other findings remain unchanged.
```

### 2. Staging Error Correction

**Template:**
```
AMENDED REPORT

Original Report Date: ___________
Amendment Date: ___________

REASON: Correction of pathologic stage

ORIGINAL STAGING:
   pT: ___  pN: ___  Stage: ___

CORRECTED STAGING:
   pT: ___  pN: ___  Stage: ___

RATIONALE:
[Explanation of error and correct interpretation]

CLINICAL IMPACT:
[Statement about treatment implications]

All other findings remain unchanged.
```

**Example:**
```
AMENDED REPORT

Original Report Date: December 28, 2024
Amendment Date: December 29, 2024

REASON: Correction of pathologic stage

ORIGINAL STAGING:
   pT: pT3  pN: pN0  Stage: IIA

CORRECTED STAGING:
   pT: pT2  pN: pN0  Stage: IB

RATIONALE:
The original report incorrectly stated pT3. Review confirms the 
tumor is confined to the pancreas (no extension beyond pancreatic 
parenchyma), measuring 2.8 cm. Per AJCC 8th edition criteria, 
tumors >2 cm confined to pancreas are classified as pT2.

CLINICAL IMPACT:
Stage changed from IIA to IB. Recommend oncology review for 
treatment planning implications.

All other findings remain unchanged.
```

### 3. Margin Status Revision

**Template:**
```
AMENDED REPORT

Original Report Date: ___________
Amendment Date: ___________

REASON: Revision of margin status

ORIGINAL MARGIN STATUS:
[Original statement]

CORRECTED MARGIN STATUS:
[Corrected statement]

RATIONALE:
[Explanation - deeper levels, re-review, measurement error, etc.]

CLINICAL IMPACT:
[Re-excision consideration, radiation planning, etc.]

All other findings remain unchanged.
```

**Example:**
```
AMENDED REPORT

Original Report Date: December 28, 2024
Amendment Date: December 29, 2024

REASON: Revision of margin status

ORIGINAL MARGIN STATUS:
"All margins negative; closest margin anterior at 2 mm"

CORRECTED MARGIN STATUS:
"Anterior margin positive for invasive carcinoma (focal, <4 mm extent)"

RATIONALE:
Review of additional deeper levels reveals invasive carcinoma 
at the inked anterior margin. The tumor focus at margin measures 
2 mm and is classified as focal involvement.

CLINICAL IMPACT:
Positive margin status. Recommend surgical consultation regarding 
re-excision versus radiation boost to tumor bed.

All other findings remain unchanged.
```

### 4. Lymph Node Count Revision

**Template:**
```
AMENDED REPORT

Original Report Date: ___________
Amendment Date: ___________

REASON: Revision of lymph node count

ORIGINAL COUNT:
___ of ___ lymph nodes with metastatic carcinoma

CORRECTED COUNT:
___ of ___ lymph nodes with metastatic carcinoma

pN CATEGORY CHANGE:
Original: pN___  →  Corrected: pN___

RATIONALE:
[Explanation - additional nodes found, re-review, etc.]

CLINICAL IMPACT:
[If pN category changed, note staging implications]

All other findings remain unchanged.
```

**Example:**
```
AMENDED REPORT

Original Report Date: December 28, 2024
Amendment Date: December 29, 2024

REASON: Revision of lymph node count

ORIGINAL COUNT:
2 of 15 lymph nodes with metastatic carcinoma

CORRECTED COUNT:
4 of 18 lymph nodes with metastatic carcinoma

pN CATEGORY CHANGE:
Original: pN1a  →  Corrected: pN2a

RATIONALE:
Re-examination of the axillary fat pad identified 3 additional 
lymph nodes, 2 of which contain metastatic carcinoma. The total 
count is now 4 positive of 18 examined.

CLINICAL IMPACT:
pN category changed from pN1a to pN2a. Stage upgraded from IIB to 
IIIA. Recommend oncology review for adjuvant therapy planning.

All other findings remain unchanged.
```

### 5. Biomarker Results Addition

**Template:**
```
ADDENDUM

Original Report Date: ___________
Addendum Date: ___________

REASON: Addition of biomarker results

BIOMARKER RESULTS:

[MARKER]: ___________
   Result: ___________
   Interpretation: ___________

CLINICAL SIGNIFICANCE:
[Treatment implications]

All other findings remain unchanged.
```

**Example (Breast):**
```
ADDENDUM

Original Report Date: December 28, 2024
Addendum Date: December 29, 2024

REASON: Addition of immunohistochemistry and molecular results

BIOMARKER RESULTS:

Estrogen Receptor (ER): Positive
   Proportion Score: 95%
   Intensity: Strong (3+)
   Allred Score: 8/8

Progesterone Receptor (PR): Positive
   Proportion Score: 80%
   Intensity: Moderate (2+)
   Allred Score: 7/8

HER2: Negative
   IHC Score: 1+ (incomplete, faint membrane staining)

Ki-67 Proliferation Index: 25%

CLINICAL SIGNIFICANCE:
Tumor is hormone receptor-positive, HER2-negative. Patient is 
candidate for endocrine therapy. Ki-67 of 25% is in the 
intermediate range.

All other findings remain unchanged.
```

**Example (Colorectal):**
```
ADDENDUM

Original Report Date: December 28, 2024
Addendum Date: December 29, 2024

REASON: Addition of molecular and immunohistochemistry results

BIOMARKER RESULTS:

Mismatch Repair (MMR) Protein Expression:
   MLH1: Intact (nuclear staining present)
   PMS2: Intact (nuclear staining present)
   MSH2: Intact (nuclear staining present)
   MSH6: Intact (nuclear staining present)
   Interpretation: MMR Intact (pMMR)

KRAS Mutation Analysis:
   Result: KRAS G12D mutation detected
   Method: PCR-based assay

BRAF Mutation Analysis:
   Result: No BRAF V600E mutation detected
   Method: PCR-based assay

CLINICAL SIGNIFICANCE:
- MMR intact: No evidence of microsatellite instability; Lynch 
  syndrome unlikely based on this result
- KRAS mutation present: Patient NOT eligible for anti-EGFR 
  therapy (cetuximab, panitumumab)

All other findings remain unchanged.
```

### 6. Tumor Size Correction

**Template:**
```
CORRECTION

Original Report Date: ___________
Correction Date: ___________

REASON: Correction of tumor size

ORIGINAL SIZE:
___ x ___ x ___ cm

CORRECTED SIZE:
___ x ___ x ___ cm

STAGING IMPACT:
pT category: [unchanged / changed from ___ to ___]
Stage group: [unchanged / changed from ___ to ___]

RATIONALE:
[Measurement error / re-review / gross-micro correlation]

All other findings remain unchanged.
```

### 7. Typographical/Clerical Error

**Template:**
```
CORRECTION

Original Report Date: ___________
Correction Date: ___________

REASON: Correction of typographical error

ORIGINAL TEXT:
"[Incorrect text]"

CORRECTED TEXT:
"[Correct text]"

This correction does not affect the diagnosis, staging, or 
clinical management.

All other findings remain unchanged.
```

**Example:**
```
CORRECTION

Original Report Date: December 28, 2024
Correction Date: December 29, 2024

REASON: Correction of typographical error

ORIGINAL TEXT:
"Right breast, lumpectomy"

CORRECTED TEXT:
"Left breast, lumpectomy"

RATIONALE:
The specimen was received labeled as "left breast" per the 
requisition form. The laterality was incorrectly transcribed 
in the original report.

This correction is critical for surgical planning and 
treatment records.

All other findings remain unchanged.
```

### 8. Additional Findings

**Template:**
```
ADDENDUM

Original Report Date: ___________
Addendum Date: ___________

REASON: Additional findings on extended review

ADDITIONAL FINDINGS:

[New findings not in original report]

CLINICAL SIGNIFICANCE:
[Impact on diagnosis/staging/treatment]

All other findings remain unchanged.
```

**Example:**
```
ADDENDUM

Original Report Date: December 28, 2024
Addendum Date: December 29, 2024

REASON: Additional findings on extended review

ADDITIONAL FINDINGS:

Review of additional levels from block B3 reveals lymphovascular 
invasion (LVI) in the peritumoral breast tissue. This finding 
was not identified on the initial sections.

Lymphovascular Invasion: Present

CLINICAL SIGNIFICANCE:
LVI is an adverse prognostic factor and may influence decisions 
regarding adjuvant systemic therapy and radiation field planning.

All other findings remain unchanged.
```

---

## Language Options

### English Header
```
AMENDED REPORT
Original Report Date: [DATE]
Amendment Date: [DATE]
Reason for Amendment: [REASON]
```

### Turkish (Türkçe) Header
```
DÜZELTİLMİŞ RAPOR
Orijinal Rapor Tarihi: [TARİH]
Düzeltme Tarihi: [TARİH]
Düzeltme Nedeni: [NEDEN]
```

### Turkish Amendment Types

| English | Turkish |
|---------|---------|
| Amended Report | Düzeltilmiş Rapor |
| Addendum | Ek Rapor |
| Correction | Düzeltme |
| Original Text | Orijinal Metin |
| Corrected Text | Düzeltilmiş Metin |
| Rationale | Gerekçe |
| Clinical Impact | Klinik Etki |
| All other findings remain unchanged | Diğer tüm bulgular değişmemiştir |

### Turkish Example
```
DÜZELTİLMİŞ RAPOR

Orijinal Rapor Tarihi: 28 Aralık 2024
Düzeltme Tarihi: 29 Aralık 2024

NEDEN: Patolojik evreleme düzeltmesi

ORİJİNAL EVRELEME:
   pT: pT3  pN: pN0  Evre: IIA

DÜZELTİLMİŞ EVRELEME:
   pT: pT2  pN: pN0  Evre: IB

GEREKÇE:
Orijinal raporda pT3 yanlışlıkla belirtilmiştir. İnceleme, 
tümörün pankreasa sınırlı olduğunu (pankreas parankimi dışına 
yayılım yok), 2.8 cm ölçüldüğünü doğrulamaktadır. AJCC 8. 
edisyon kriterlerine göre, pankreasa sınırlı >2 cm tümörler 
pT2 olarak sınıflandırılır.

KLİNİK ETKİ:
Evre IIA'dan IB'ye değişmiştir. Tedavi planlaması için 
onkoloji değerlendirmesi önerilir.

Diğer tüm bulgular değişmemiştir.
```

---

## Trigger Phrases

### English
```
Generate an amendment for this report
Create an addendum for missing staging
Write a correction for margin status
Draft amendment for node count change
Prepare amended report text
Fix this staging error
```

### Turkish
```
Bu rapor için düzeltme oluştur
Eksik evreleme için ek rapor yaz
Sınır durumu düzeltmesi hazırla
Lenf nodu sayısı değişikliği için düzeltme
Düzeltilmiş rapor metni hazırla
```

---

## Workflow

### Step 1: Identify Amendment Type

| Finding | → | Amendment Type |
|---------|---|----------------|
| Missing element (no error) | → | Addendum |
| Incorrect value | → | Correction |
| Staging/diagnosis change | → | Amended Report |

### Step 2: Gather Information

Required for all amendments:
- [ ] Original report date
- [ ] Original text (verbatim)
- [ ] Corrected/added text
- [ ] Reason for change
- [ ] Clinical impact assessment

### Step 3: Generate Amendment

Use appropriate template based on:
- Type of change
- Element affected
- Clinical significance

### Step 4: Review Checklist

- [ ] Original and corrected text clearly distinguished
- [ ] Rationale documented
- [ ] Clinical impact stated
- [ ] Staging recalculated if needed
- [ ] "All other findings unchanged" statement included
- [ ] Dates and pathologist name included

---

## Integration

### With Compliance Checker
1. Run compliance check
2. Identify missing/incorrect elements
3. Generate amendment for each issue
4. Provide complete amendment package

### With Auto-Fill Suggestions
1. Identify missing staging
2. Calculate suggested values
3. Generate addendum with calculated staging

### With Free-Text Converter
1. Convert original free-text
2. Identify discrepancies with synoptic
3. Generate corrections as needed

---

## Best Practices

### Do
- Use exact quotes from original report
- Be specific about what changed
- State clinical significance clearly
- Include staging impact if applicable
- Date and sign all amendments

### Don't
- Leave original text ambiguous
- Omit rationale for changes
- Forget to assess clinical impact
- Issue multiple amendments when one comprehensive amendment would suffice
- Delay critical corrections

### Timing Recommendations

| Change Type | Recommended Timing |
|-------------|-------------------|
| Critical error (laterality, diagnosis) | Same day |
| Staging correction | Within 24 hours |
| Biomarker addition | Within 48 hours |
| Minor typographical | Within 1 week |
