# TNM Stage Calculator

Calculate AJCC 8th Edition stage groups from pT, pN, and pM categories.

## Usage

Provide pT, pN, and pM (or cM) categories to calculate the stage group.

**Input format:**
- pT category: pTis, pT1, pT1a, pT1b, pT2, pT3, pT4, pT4a, pT4b
- pN category: pN0, pN1, pN1a, pN1b, pN2, pN2a, pN2b, pN3, pN3a, pN3b
- pM category: pM0, pM1, cM0, cM1

**Example:**
```
Input: pT2, pN1, M0
Tumor: Gastric carcinoma
Output: Stage IIA
```

---

## Breast Invasive Carcinoma (AJCC 8th Edition)

### Anatomic Stage Groups

| Stage | T | N | M |
|-------|---|---|---|
| **0** | Tis | N0 | M0 |
| **IA** | T1 | N0 | M0 |
| **IB** | T0-T1 | N1mi | M0 |
| **IIA** | T0-T1 | N1 | M0 |
| | T2 | N0 | M0 |
| **IIB** | T2 | N1 | M0 |
| | T3 | N0 | M0 |
| **IIIA** | T0-T2 | N2 | M0 |
| | T3 | N1-N2 | M0 |
| **IIIB** | T4 | N0-N2 | M0 |
| **IIIC** | Any T | N3 | M0 |
| **IV** | Any T | Any N | M1 |

### pT Categories

| Category | Size/Extent |
|----------|-------------|
| pTis | DCIS or Paget without invasion |
| pT1mi | ≤1 mm |
| pT1a | >1 mm to ≤5 mm |
| pT1b | >5 mm to ≤10 mm |
| pT1c | >10 mm to ≤20 mm |
| pT2 | >20 mm to ≤50 mm |
| pT3 | >50 mm |
| pT4a | Chest wall invasion |
| pT4b | Skin ulceration/satellite nodules/edema |
| pT4c | Both T4a and T4b |
| pT4d | Inflammatory carcinoma |

### pN Categories

| Category | Definition |
|----------|------------|
| pN0 | No regional metastasis |
| pN0(i+) | ITCs only (≤0.2 mm) |
| pN1mi | Micrometastasis (>0.2 mm to ≤2 mm) |
| pN1a | 1-3 axillary nodes |
| pN1b | Internal mammary with sentinel |
| pN1c | 1-3 axillary + internal mammary |
| pN2a | 4-9 axillary nodes |
| pN2b | Internal mammary clinically detected |
| pN3a | ≥10 axillary or infraclavicular |
| pN3b | Axillary + internal mammary clinically |
| pN3c | Supraclavicular |

### Stage Calculation Logic (Breast)

```
function calculate_breast_stage(pT, pN, pM):
    if pM == "M1": return "IV"
    
    if pN == "N3" or pN in ["N3a", "N3b", "N3c"]: return "IIIC"
    
    if pT == "T4" or pT in ["T4a", "T4b", "T4c", "T4d"]:
        if pN in ["N0", "N1", "N2"]: return "IIIB"
    
    if pN == "N2" or pN in ["N2a", "N2b"]:
        if pT in ["T0", "T1", "T2"]: return "IIIA"
        if pT == "T3": return "IIIA"
    
    if pT == "T3":
        if pN in ["N1", "N1a", "N1b", "N1c"]: return "IIIA"
        if pN == "N0": return "IIB"
    
    if pT == "T2":
        if pN in ["N1", "N1a", "N1b", "N1c"]: return "IIB"
        if pN == "N0": return "IIA"
    
    if pT in ["T0", "T1", "T1mi", "T1a", "T1b", "T1c"]:
        if pN in ["N1", "N1a", "N1b", "N1c"]: return "IIA"
        if pN == "N1mi": return "IB"
        if pN == "N0": return "IA"
    
    if pT == "Tis" and pN == "N0": return "0"
    
    return "Cannot determine"
```

---

## Colorectal Carcinoma (AJCC 8th Edition)

### Stage Groups

| Stage | T | N | M |
|-------|---|---|---|
| **0** | Tis | N0 | M0 |
| **I** | T1-T2 | N0 | M0 |
| **IIA** | T3 | N0 | M0 |
| **IIB** | T4a | N0 | M0 |
| **IIC** | T4b | N0 | M0 |
| **IIIA** | T1-T2 | N1/N1c | M0 |
| | T1 | N2a | M0 |
| **IIIB** | T3-T4a | N1/N1c | M0 |
| | T2-T3 | N2a | M0 |
| | T1-T2 | N2b | M0 |
| **IIIC** | T4a | N2a | M0 |
| | T3-T4a | N2b | M0 |
| | T4b | N1-N2 | M0 |
| **IVA** | Any T | Any N | M1a |
| **IVB** | Any T | Any N | M1b |
| **IVC** | Any T | Any N | M1c |

### pT Categories

| Category | Definition |
|----------|------------|
| pTis | Carcinoma in situ, intramucosal |
| pT1 | Submucosa |
| pT2 | Muscularis propria |
| pT3 | Through muscularis into pericolorectal tissues |
| pT4a | Penetrates visceral peritoneum |
| pT4b | Directly invades adjacent organs/structures |

### pN Categories

| Category | Definition |
|----------|------------|
| pN0 | No regional metastasis |
| pN1a | 1 regional node |
| pN1b | 2-3 regional nodes |
| pN1c | Tumor deposits without nodes |
| pN2a | 4-6 regional nodes |
| pN2b | ≥7 regional nodes |

### pM Categories

| Category | Definition |
|----------|------------|
| M0 | No distant metastasis |
| M1a | One site/organ (not peritoneum) |
| M1b | Two or more sites/organs (not peritoneum) |
| M1c | Peritoneal metastasis ± other sites |

### Stage Calculation Logic (Colorectal)

```
function calculate_colorectal_stage(pT, pN, pM):
    if pM == "M1c": return "IVC"
    if pM == "M1b": return "IVB"
    if pM == "M1a" or pM == "M1": return "IVA"
    
    if pT == "T4b":
        if pN in ["N1", "N1a", "N1b", "N1c", "N2", "N2a", "N2b"]: return "IIIC"
        if pN == "N0": return "IIC"
    
    if pN == "N2b":
        if pT in ["T3", "T4a"]: return "IIIC"
        if pT in ["T1", "T2"]: return "IIIB"
    
    if pN == "N2a":
        if pT == "T4a": return "IIIC"
        if pT in ["T2", "T3"]: return "IIIB"
        if pT == "T1": return "IIIA"
    
    if pN in ["N1", "N1a", "N1b", "N1c"]:
        if pT in ["T3", "T4a"]: return "IIIB"
        if pT in ["T1", "T2"]: return "IIIA"
    
    if pN == "N0":
        if pT == "T4b": return "IIC"
        if pT == "T4a": return "IIB"
        if pT == "T3": return "IIA"
        if pT in ["T1", "T2"]: return "I"
        if pT == "Tis": return "0"
    
    return "Cannot determine"
```

---

## Exocrine Pancreas Carcinoma (AJCC 8th Edition)

### Stage Groups

| Stage | T | N | M |
|-------|---|---|---|
| **0** | Tis | N0 | M0 |
| **IA** | T1a | N0 | M0 |
| **IB** | T1b-T1c | N0 | M0 |
| | T2 | N0 | M0 |
| **IIA** | T3 | N0 | M0 |
| **IIB** | T1-T3 | N1 | M0 |
| **III** | T1-T3 | N2 | M0 |
| | T4 | Any N | M0 |
| **IV** | Any T | Any N | M1 |

### pT Categories

| Category | Definition |
|----------|------------|
| pTis | Carcinoma in situ, PanIN-3 |
| pT1a | ≤0.5 cm |
| pT1b | >0.5 cm to <1 cm |
| pT1c | 1 to <2 cm |
| pT2 | 2 to ≤4 cm |
| pT3 | >4 cm |
| pT4 | Celiac axis, SMA, or common hepatic artery |

### pN Categories

| Category | Definition |
|----------|------------|
| pN0 | No regional metastasis |
| pN1 | 1-3 positive regional nodes |
| pN2 | ≥4 positive regional nodes |

### Stage Calculation Logic (Pancreas)

```
function calculate_pancreas_stage(pT, pN, pM):
    if pM == "M1": return "IV"
    
    if pT == "T4": return "III"
    
    if pN == "N2": return "III"
    
    if pN == "N1":
        if pT in ["T1", "T1a", "T1b", "T1c", "T2", "T3"]: return "IIB"
    
    if pN == "N0":
        if pT == "T3": return "IIA"
        if pT == "T2": return "IB"
        if pT in ["T1b", "T1c"]: return "IB"
        if pT == "T1a": return "IA"
        if pT == "Tis": return "0"
    
    return "Cannot determine"
```

---

## Gastric Carcinoma (AJCC 8th Edition)

### Stage Groups

| Stage | T | N | M |
|-------|---|---|---|
| **0** | Tis | N0 | M0 |
| **IA** | T1 | N0 | M0 |
| **IB** | T1 | N1 | M0 |
| | T2 | N0 | M0 |
| **IIA** | T1 | N2 | M0 |
| | T2 | N1 | M0 |
| | T3 | N0 | M0 |
| **IIB** | T1 | N3a | M0 |
| | T2 | N2 | M0 |
| | T3 | N1 | M0 |
| | T4a | N0 | M0 |
| **IIIA** | T2 | N3a | M0 |
| | T3 | N2 | M0 |
| | T4a | N1-N2 | M0 |
| | T4b | N0 | M0 |
| **IIIB** | T1-T2 | N3b | M0 |
| | T3-T4a | N3a | M0 |
| | T4b | N1-N2 | M0 |
| **IIIC** | T3-T4a | N3b | M0 |
| | T4b | N3a-N3b | M0 |
| **IV** | Any T | Any N | M1 |

### pT Categories

| Category | Definition |
|----------|------------|
| pTis | Carcinoma in situ / high-grade dysplasia |
| pT1a | Lamina propria or muscularis mucosae |
| pT1b | Submucosa |
| pT2 | Muscularis propria |
| pT3 | Subserosa without serosal/adjacent organ invasion |
| pT4a | Perforates serosa (visceral peritoneum) |
| pT4b | Invades adjacent structures |

### pN Categories

| Category | Definition |
|----------|------------|
| pN0 | No regional metastasis |
| pN1 | 1-2 regional nodes |
| pN2 | 3-6 regional nodes |
| pN3a | 7-15 regional nodes |
| pN3b | ≥16 regional nodes |

### Stage Calculation Logic (Gastric)

```
function calculate_gastric_stage(pT, pN, pM):
    if pM == "M1": return "IV"
    
    # N3b cases
    if pN == "N3b":
        if pT in ["T3", "T4a"]: return "IIIC"
        if pT == "T4b": return "IIIC"
        if pT in ["T1", "T1a", "T1b", "T2"]: return "IIIB"
    
    # N3a cases
    if pN == "N3a":
        if pT == "T4b": return "IIIC"
        if pT in ["T3", "T4a"]: return "IIIB"
        if pT == "T2": return "IIIA"
        if pT in ["T1", "T1a", "T1b"]: return "IIB"
    
    # T4b cases
    if pT == "T4b":
        if pN in ["N1", "N2"]: return "IIIB"
        if pN == "N0": return "IIIA"
    
    # T4a cases
    if pT == "T4a":
        if pN in ["N1", "N2"]: return "IIIA"
        if pN == "N0": return "IIB"
    
    # T3 cases
    if pT == "T3":
        if pN == "N2": return "IIIA"
        if pN == "N1": return "IIB"
        if pN == "N0": return "IIA"
    
    # T2 cases
    if pT == "T2":
        if pN == "N2": return "IIB"
        if pN == "N1": return "IIA"
        if pN == "N0": return "IB"
    
    # T1 cases
    if pT in ["T1", "T1a", "T1b"]:
        if pN == "N2": return "IIA"
        if pN == "N1": return "IB"
        if pN == "N0": return "IA"
    
    # Tis
    if pT == "Tis" and pN == "N0": return "0"
    
    return "Cannot determine"
```

---

## Quick Reference Tables

### Breast - Quick Lookup

| | N0 | N1mi | N1 | N2 | N3 |
|---|---|---|---|---|---|
| **Tis** | 0 | - | - | - | - |
| **T1** | IA | IB | IIA | IIIA | IIIC |
| **T2** | IIA | IIA | IIB | IIIA | IIIC |
| **T3** | IIB | IIB | IIIA | IIIA | IIIC |
| **T4** | IIIB | IIIB | IIIB | IIIB | IIIC |

### Colorectal - Quick Lookup

| | N0 | N1 | N2a | N2b |
|---|---|---|---|---|
| **Tis** | 0 | - | - | - |
| **T1** | I | IIIA | IIIA | IIIB |
| **T2** | I | IIIA | IIIB | IIIB |
| **T3** | IIA | IIIB | IIIB | IIIC |
| **T4a** | IIB | IIIB | IIIC | IIIC |
| **T4b** | IIC | IIIC | IIIC | IIIC |

### Pancreas - Quick Lookup

| | N0 | N1 | N2 |
|---|---|---|---|
| **Tis** | 0 | - | - |
| **T1a** | IA | IIB | III |
| **T1b-c** | IB | IIB | III |
| **T2** | IB | IIB | III |
| **T3** | IIA | IIB | III |
| **T4** | III | III | III |

### Gastric - Quick Lookup

| | N0 | N1 | N2 | N3a | N3b |
|---|---|---|---|---|---|
| **Tis** | 0 | - | - | - | - |
| **T1** | IA | IB | IIA | IIB | IIIB |
| **T2** | IB | IIA | IIB | IIIA | IIIB |
| **T3** | IIA | IIB | IIIA | IIIB | IIIC |
| **T4a** | IIB | IIIA | IIIA | IIIB | IIIC |
| **T4b** | IIIA | IIIB | IIIB | IIIC | IIIC |

---

## Validation Rules

### Input Validation

1. pT must be valid for tumor type
2. pN must be valid for tumor type
3. pM must be M0 or M1 (with subcategories where applicable)
4. Warn if ypTNM prefix detected (post-treatment staging)

### Cross-Validation with Report

| Check | Expected |
|-------|----------|
| Stage in report matches calculated | Must match |
| pT consistent with tumor size | Per AJCC criteria |
| pN consistent with node count | Per AJCC criteria |
| M1 requires documented metastasis | Must be pathologically confirmed |

### Output Format

```
═══════════════════════════════════════════════════════════════
TNM STAGE CALCULATION
═══════════════════════════════════════════════════════════════
Tumor Type: Gastric Carcinoma
AJCC Edition: 8th (2017)

Input:
  pT: pT3 (Tumor penetrates subserosa)
  pN: pN2 (3-6 positive regional nodes)
  pM: M0 (No distant metastasis)

Calculated Stage: IIIA

Stage Group Definition:
  Stage IIIA includes: T2N3a, T3N2, T4aN1-2, T4bN0

Prognosis Note:
  5-year survival Stage IIIA: ~20-30%
───────────────────────────────────────────────────────────────
```

---

## Error Handling

| Error | Response |
|-------|----------|
| Invalid pT | "pT category not recognized for [tumor type]" |
| Invalid pN | "pN category not recognized for [tumor type]" |
| Missing data | "Cannot calculate stage: [missing element]" |
| Conflicting data | "Stage calculation conflict: verify pT, pN, pM" |

---

## Post-Neoadjuvant Staging (ypTNM)

For patients receiving neoadjuvant therapy:
- Use "yp" prefix (ypT, ypN)
- Same staging tables apply
- ypT0N0 = complete pathologic response
- Document treatment effect grade separately

---

## Turkish Terminology

| English | Turkish |
|---------|---------|
| Stage | Evre |
| Stage group | Evre grubu |
| Staging | Evreleme |
| Primary tumor | Primer tümör |
| Regional lymph nodes | Bölgesel lenf nodları |
| Distant metastasis | Uzak metastaz |
| Cannot be assessed | Değerlendirilemiyor |
| No evidence | Kanıt yok |
| Carcinoma in situ | Karsinoma in situ |
| Invasion | İnvazyon |
| Serosa | Seroza |
| Adjacent structures | Komşu yapılar |
