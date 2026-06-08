# Auto-Fill Suggestions

Suggest appropriate values for synoptic report fields based on provided context and extracted data.

## Purpose

Provide intelligent suggestions for:
- pT/pN/pM staging based on tumor characteristics
- Grade based on differentiation descriptors
- Biomarker interpretations
- Margin status based on distances
- Stage group based on pTNM

---

## Tumor Size → pT Suggestions

### Breast

| Size | Suggested pT | Confidence |
|------|--------------|------------|
| ≤1 mm | pT1mi (microinvasion) | High |
| >1 mm and ≤5 mm | pT1a | High |
| >5 mm and ≤10 mm | pT1b | High |
| >10 mm and ≤20 mm | pT1c | High |
| >20 mm and ≤50 mm | pT2 | High |
| >50 mm | pT3 | High |
| Skin ulceration/satellite nodules | pT4b | High |
| Inflammatory carcinoma | pT4d | High |
| Chest wall invasion | pT4a | High |

**Example:**
```
Input: "2.3 cm invasive ductal carcinoma"
Suggestion: pT2 (tumor >2 cm but ≤5 cm)
Confidence: High
```

### Colorectal

| Invasion Depth | Suggested pT | Confidence |
|----------------|--------------|------------|
| Lamina propria / muscularis mucosae | pTis | High |
| Submucosa | pT1 | High |
| Muscularis propria | pT2 | High |
| Through muscularis propria (pericolorectal tissues) | pT3 | High |
| Visceral peritoneum penetration | pT4a | High |
| Adjacent organ invasion | pT4b | High |

**Example:**
```
Input: "Tumor invades through muscularis propria into pericolonic fat"
Suggestion: pT3
Confidence: High
```

### Pancreas

| Size / Extent | Suggested pT | Confidence |
|---------------|--------------|------------|
| ≤2 cm, confined to pancreas | pT1 | High |
| >2 cm, confined to pancreas | pT2 | High |
| Extends beyond pancreas (no celiac/SMA) | pT3 | High |
| Celiac axis or SMA involvement | pT4 | High |

**Size-based (if confined):**
| Size | Suggested pT |
|------|--------------|
| ≤0.5 cm | pT1a |
| >0.5 cm and ≤1 cm | pT1b |
| >1 cm and ≤2 cm | pT1c |
| >2 cm and ≤4 cm | pT2 |
| >4 cm | pT3 |

**Example:**
```
Input: "2.8 cm ductal adenocarcinoma limited to pancreas"
Suggestion: pT2 (>2 cm, confined to pancreas)
Confidence: High
```

### Gastric

| Invasion Depth | Suggested pT | Confidence |
|----------------|--------------|------------|
| Lamina propria / muscularis mucosae | pT1a | High |
| Submucosa | pT1b | High |
| Muscularis propria | pT2 | High |
| Subserosa (no peritoneum/adjacent organs) | pT3 | High |
| Serosa (visceral peritoneum) | pT4a | High |
| Adjacent structures | pT4b | High |

**Example:**
```
Input: "Tumor invades muscularis propria"
Suggestion: pT2
Confidence: High
```

---

## Lymph Node Count → pN Suggestions

### Breast

| Positive Nodes | Location | Suggested pN |
|----------------|----------|--------------|
| 0 | - | pN0 |
| 1-3 | Axillary | pN1a |
| 1-3 | Internal mammary (clinically detected) | pN1b |
| 1-3 | Both axillary + internal mammary | pN1c |
| 4-9 | Axillary | pN2a |
| Internal mammary (clinically detected, no axillary) | - | pN2b |
| ≥10 | Axillary | pN3a |
| Infraclavicular | - | pN3a |
| Internal mammary + axillary | - | pN3b |
| Supraclavicular | - | pN3c |

**Micrometastasis:**
| Finding | Suggested pN |
|---------|--------------|
| ITC only (≤0.2 mm) | pN0(i+) |
| Micrometastasis (>0.2 mm, ≤2 mm) | pN1mi |

**Example:**
```
Input: "2 of 15 axillary lymph nodes with metastatic carcinoma"
Suggestion: pN1a (1-3 positive axillary nodes)
Confidence: High
```

### Colorectal

| Positive Nodes | Suggested pN |
|----------------|--------------|
| 0 | pN0 |
| 1 | pN1a |
| 2-3 | pN1b |
| Tumor deposits only (no nodes) | pN1c |
| 4-6 | pN2a |
| ≥7 | pN2b |

**Example:**
```
Input: "3 of 18 lymph nodes positive"
Suggestion: pN1b (2-3 positive regional nodes)
Confidence: High
```

### Pancreas

| Positive Nodes | Suggested pN |
|----------------|--------------|
| 0 | pN0 |
| 1-3 | pN1 |
| ≥4 | pN2 |

**Example:**
```
Input: "2 of 14 lymph nodes with metastatic adenocarcinoma"
Suggestion: pN1 (1-3 positive regional nodes)
Confidence: High
```

### Gastric

| Positive Nodes | Suggested pN |
|----------------|--------------|
| 0 | pN0 |
| 1-2 | pN1 |
| 3-6 | pN2 |
| 7-15 | pN3a |
| ≥16 | pN3b |

**Example:**
```
Input: "4 of 22 lymph nodes positive"
Suggestion: pN2 (3-6 positive regional nodes)
Confidence: High
```

---

## pTNM → Stage Group Suggestions

### Breast

| pT | pN | pM | Suggested Stage |
|----|----|----|-----------------|
| Tis | N0 | M0 | 0 |
| T1 | N0 | M0 | IA |
| T0-T1 | N1mi | M0 | IB |
| T2 | N0 | M0 | IIA |
| T0-T1 | N1 | M0 | IIA |
| T2 | N1 | M0 | IIB |
| T3 | N0 | M0 | IIB |
| T0-T2 | N2 | M0 | IIIA |
| T3 | N1-N2 | M0 | IIIA |
| T4 | N0-N2 | M0 | IIIB |
| Any T | N3 | M0 | IIIC |
| Any T | Any N | M1 | IV |

**Example:**
```
Input: pT2 N1a M0
Suggestion: Stage IIB
Confidence: High
```

### Colorectal

| pT | pN | pM | Suggested Stage |
|----|----|----|-----------------|
| Tis | N0 | M0 | 0 |
| T1-T2 | N0 | M0 | I |
| T3 | N0 | M0 | IIA |
| T4a | N0 | M0 | IIB |
| T4b | N0 | M0 | IIC |
| T1-T2 | N1/N1c | M0 | IIIA |
| T1 | N2a | M0 | IIIA |
| T3-T4a | N1/N1c | M0 | IIIB |
| T2-T3 | N2a | M0 | IIIB |
| T1-T2 | N2b | M0 | IIIB |
| T4a | N2a | M0 | IIIC |
| T3-T4a | N2b | M0 | IIIC |
| T4b | N1-N2 | M0 | IIIC |
| Any T | Any N | M1a | IVA |
| Any T | Any N | M1b | IVB |
| Any T | Any N | M1c | IVC |

**Example:**
```
Input: pT3 N1b M0
Suggestion: Stage IIIB
Confidence: High
```

### Pancreas

| pT | pN | pM | Suggested Stage |
|----|----|----|-----------------|
| Tis | N0 | M0 | 0 |
| T1 | N0 | M0 | IA |
| T2 | N0 | M0 | IB |
| T3 | N0 | M0 | IIA |
| T1-T3 | N1 | M0 | IIB |
| T1-T3 | N2 | M0 | III |
| T4 | Any N | M0 | III |
| Any T | Any N | M1 | IV |

**Example:**
```
Input: pT2 N1 M0
Suggestion: Stage IIB
Confidence: High
```

### Gastric

| pT | pN | pM | Suggested Stage |
|----|----|----|-----------------|
| Tis | N0 | M0 | 0 |
| T1 | N0 | M0 | IA |
| T1 | N1 | M0 | IB |
| T2 | N0 | M0 | IB |
| T1 | N2 | M0 | IIA |
| T2 | N1 | M0 | IIA |
| T3 | N0 | M0 | IIA |
| T1 | N3a | M0 | IIB |
| T2 | N2 | M0 | IIB |
| T3 | N1 | M0 | IIB |
| T4a | N0 | M0 | IIB |
| T2 | N3a | M0 | IIIA |
| T3 | N2 | M0 | IIIA |
| T4a | N1-N2 | M0 | IIIA |
| T4b | N0-N1 | M0 | IIIA |
| T3 | N3a | M0 | IIIB |
| T4a | N3a | M0 | IIIB |
| T4b | N2-N3a | M0 | IIIB |
| T4a-T4b | N3b | M0 | IIIC |
| Any T | Any N | M1 | IV |

**Example:**
```
Input: pT3 N2 M0
Suggestion: Stage IIIA
Confidence: High
```

---

## Grade Suggestions

### From Differentiation Descriptors

| Descriptor | Suggested Grade |
|------------|-----------------|
| Well differentiated | G1 |
| Moderately differentiated | G2 |
| Poorly differentiated | G3 |
| Undifferentiated | G4 (if applicable) |
| Low grade | G1 |
| Intermediate grade | G2 |
| High grade | G3 |

### Breast Nottingham Score

| Total Score | Suggested Grade |
|-------------|-----------------|
| 3-5 | Grade 1 |
| 6-7 | Grade 2 |
| 8-9 | Grade 3 |

**Component scoring:**
| Component | Score 1 | Score 2 | Score 3 |
|-----------|---------|---------|---------|
| Tubule formation | >75% | 10-75% | <10% |
| Nuclear pleomorphism | Mild | Moderate | Marked |
| Mitotic count | 0-5/10 HPF | 6-10/10 HPF | >10/10 HPF |

**Example:**
```
Input: "Nottingham score 7/9 (tubules 3, nuclear 2, mitoses 2)"
Suggestion: Grade 2
Confidence: High
```

---

## Margin Suggestions

### Distance-Based Status

| Tumor Type | Distance | Suggested Status |
|------------|----------|------------------|
| Breast (invasive) | 0 mm (ink on tumor) | Positive |
| Breast (invasive) | >0 mm | Negative |
| Breast (DCIS) | 0 mm | Positive |
| Breast (DCIS) | <2 mm | Close |
| Breast (DCIS) | ≥2 mm | Negative |
| Colorectal (CRM) | ≤1 mm | Positive |
| Colorectal (CRM) | >1 mm | Negative |
| Pancreas | 0 mm | Positive (R1) |
| Pancreas | >0 mm | Negative (R0) |

### R Classification

| Finding | Suggested R |
|---------|-------------|
| All margins negative | R0 |
| Microscopic positive margin | R1 |
| Gross residual tumor | R2 |

**Example:**
```
Input: "Circumferential margin 0.8 mm"
Suggestion: CRM Positive (≤1 mm)
Confidence: High
```

---

## Biomarker Interpretation Suggestions

### Breast ER/PR

| Result | Suggested Interpretation |
|--------|--------------------------|
| ≥1% positive | Positive |
| <1% positive | Negative |
| 0% | Negative |

### Breast HER2

| IHC Score | FISH | Suggested Status |
|-----------|------|------------------|
| 0 | - | Negative |
| 1+ | - | Negative |
| 2+ | Amplified | Positive |
| 2+ | Not amplified | Negative |
| 2+ | Not done | Equivocal (FISH required) |
| 3+ | - | Positive |

### Colorectal MMR/MSI

| IHC Pattern | Suggested Status |
|-------------|------------------|
| All 4 proteins retained | MMR Intact / MSS |
| MLH1/PMS2 loss | MMR Deficient (suggest MLH1 methylation testing) |
| MSH2/MSH6 loss | MMR Deficient (Lynch syndrome likely) |
| PMS2 loss only | MMR Deficient |
| MSH6 loss only | MMR Deficient |

**Example:**
```
Input: "MLH1 and PMS2 loss, MSH2 and MSH6 retained"
Suggestion: MMR Deficient - Recommend MLH1 promoter methylation testing
Confidence: High
```

---

## Lymph Node Adequacy Suggestions

| Tumor Type | Minimum Nodes | Suggestion if Below |
|------------|---------------|---------------------|
| Breast (axillary) | 10 | "Consider additional node sampling" |
| Colorectal | 12 | "Suboptimal node harvest - re-examine specimen" |
| Pancreas | 12-15 | "Node count below CAP recommendation" |
| Gastric | 16 | "Suboptimal for accurate N staging" |

**Example:**
```
Input: "8 lymph nodes examined, all negative"
Tumor: Colorectal
Suggestion: ⚠️ Suboptimal node count (8/12 minimum). Consider re-examination or note in report.
```

---

## Context-Aware Suggestions

### Neoadjuvant Therapy

If report mentions prior chemotherapy/radiation:
- Use "yp" prefix (ypT, ypN)
- Suggest tumor regression grade (TRG) assessment
- Note that lower node counts are acceptable

**Example:**
```
Input: "Post-neoadjuvant chemoradiation, no residual tumor identified"
Suggestions:
- ypT0 (complete pathologic response)
- Consider documenting treatment effect grade
```

### Multiple Tumors

For multifocal/multicentric disease:
- Use largest tumor for T staging
- Note "(m)" suffix option
- Document all tumor sizes

**Example:**
```
Input: "Two tumor foci: 2.3 cm and 0.8 cm"
Suggestions:
- pT2 based on largest focus (2.3 cm)
- Consider pT2(m) notation
- Document both sizes in report
```

---

## Output Format

### Single Suggestion
```
FIELD: [Field name]
CURRENT VALUE: [Extracted or stated value]
SUGGESTED VALUE: [Recommendation]
RATIONALE: [Brief explanation]
CONFIDENCE: High / Medium / Low
```

### Multiple Suggestions
```
AUTO-FILL SUGGESTIONS
═══════════════════════════════════════════════════════════════

1. pT Category
   Current: Not specified
   Suggested: pT2
   Rationale: Tumor size 2.3 cm (>2 cm, ≤5 cm)
   Confidence: High

2. pN Category
   Current: Not specified
   Suggested: pN1a
   Rationale: 2 positive axillary nodes (1-3 range)
   Confidence: High

3. Stage Group
   Current: Not specified
   Suggested: Stage IIB
   Rationale: pT2 N1a M0 → Stage IIB (AJCC 8th)
   Confidence: High

4. HER2 Status
   Current: "2+"
   Suggested: Equivocal - FISH testing required
   Rationale: IHC 2+ requires ISH confirmation
   Confidence: High

═══════════════════════════════════════════════════════════════
```

---

## Trigger Phrases

### English
```
Suggest values for this report
Auto-fill staging
What should pT be for this tumor?
Calculate stage from these findings
Fill in missing fields
Suggest pTNM
```

### Turkish
```
Bu rapor için değerler öner
Evrelemeyi otomatik doldur
Bu tümör için pT ne olmalı?
Bu bulgulardan evreyi hesapla
Eksik alanları doldur
pTNM öner
```

---

## Confidence Levels

| Level | Definition | Action |
|-------|------------|--------|
| **High** | Clear criteria met, unambiguous | Apply directly |
| **Medium** | Criteria likely met, minor ambiguity | Apply with note |
| **Low** | Incomplete data, multiple interpretations | Flag for review |

### Factors Reducing Confidence

- Incomplete tumor size measurement
- Unclear invasion depth description
- Missing node location
- Ambiguous margin distance
- Post-treatment changes
- Conflicting information

---

## Integration

### With Compliance Checker
1. Check report for missing elements
2. Generate auto-fill suggestions for missing fields
3. Present both compliance gaps and suggested values

### With Free-text Converter
1. Extract values from narrative
2. Apply auto-fill for any gaps
3. Generate complete synoptic output

### With Template Generator
1. Generate blank template
2. Pre-fill known values
3. Suggest remaining values based on context
