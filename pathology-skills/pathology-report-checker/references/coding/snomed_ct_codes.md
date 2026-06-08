# SNOMED CT Coding Reference

Suggest SNOMED CT morphology and topography codes for pathology reports.

## Overview

SNOMED CT (Systematized Nomenclature of Medicine - Clinical Terms) provides standardized codes for:
- **Morphology (M codes)**: Tumor histologic type and behavior
- **Topography (T codes)**: Anatomic site/location
- **Procedure codes**: Specimen type

### Code Structure

**Morphology codes**: M-####/# format
- First 4 digits: Histologic type
- After slash: Behavior code
  - /0 = Benign
  - /1 = Uncertain behavior
  - /2 = Carcinoma in situ
  - /3 = Malignant, primary
  - /6 = Malignant, metastatic
  - /9 = Malignant, uncertain primary or metastatic

**Topography codes**: C##.# format (ICD-O-3 compatible)

---

## Breast Carcinoma Codes

### Morphology Codes

| Histologic Type | SNOMED CT Code | ICD-O-3 |
|-----------------|----------------|---------|
| **Invasive carcinoma, NST (ductal)** | 82113 | 8500/3 |
| Invasive lobular carcinoma | 82013 | 8520/3 |
| Invasive lobular carcinoma, classic | 85203 | 8520/3 |
| Invasive lobular carcinoma, pleomorphic | 85243 | 8524/3 |
| Mucinous carcinoma | 84803 | 8480/3 |
| Tubular carcinoma | 82113 | 8211/3 |
| Cribriform carcinoma | 82013 | 8201/3 |
| Invasive micropapillary carcinoma | 85073 | 8507/3 |
| Invasive papillary carcinoma | 85033 | 8503/3 |
| Metaplastic carcinoma | 85753 | 8575/3 |
| Metaplastic carcinoma, squamous | 85703 | 8570/3 |
| Metaplastic carcinoma, spindle cell | 80323 | 8032/3 |
| Medullary carcinoma | 85103 | 8510/3 |
| Secretory carcinoma | 85023 | 8502/3 |
| Adenoid cystic carcinoma | 82003 | 8200/3 |
| Apocrine carcinoma | 84013 | 8401/3 |
| Neuroendocrine carcinoma | 82463 | 8246/3 |
| Mixed carcinoma | 85233 | 8523/3 |
| **DCIS (ductal carcinoma in situ)** | 85002 | 8500/2 |
| LCIS (lobular carcinoma in situ) | 85202 | 8520/2 |
| Paget disease of nipple | 85403 | 8540/3 |

### Topography Codes

| Site | SNOMED CT | ICD-O-3 |
|------|-----------|---------|
| Breast, NOS | T-04000 | C50.9 |
| Nipple | T-04100 | C50.0 |
| Central portion | T-04200 | C50.1 |
| Upper inner quadrant | T-04300 | C50.2 |
| Lower inner quadrant | T-04400 | C50.3 |
| Upper outer quadrant | T-04500 | C50.4 |
| Lower outer quadrant | T-04600 | C50.5 |
| Axillary tail | T-04700 | C50.6 |
| Overlapping | T-04800 | C50.8 |

### Grade Codes

| Grade | SNOMED CT |
|-------|-----------|
| Grade 1, well differentiated | 61026006 |
| Grade 2, moderately differentiated | 62459000 |
| Grade 3, poorly differentiated | 399415002 |

---

## Colorectal Carcinoma Codes

### Morphology Codes

| Histologic Type | SNOMED CT Code | ICD-O-3 |
|-----------------|----------------|---------|
| **Adenocarcinoma, NOS** | 81403 | 8140/3 |
| Adenocarcinoma, well differentiated | 81403 | 8140/3 |
| Adenocarcinoma, moderately differentiated | 81403 | 8140/3 |
| Adenocarcinoma, poorly differentiated | 81403 | 8140/3 |
| Mucinous adenocarcinoma | 84803 | 8480/3 |
| Signet ring cell carcinoma | 84903 | 8490/3 |
| Medullary carcinoma | 85103 | 8510/3 |
| Micropapillary carcinoma | 82653 | 8265/3 |
| Serrated adenocarcinoma | 84413 | 8441/3 |
| Adenosquamous carcinoma | 85603 | 8560/3 |
| Squamous cell carcinoma | 80703 | 8070/3 |
| Undifferentiated carcinoma | 80203 | 8020/3 |
| Neuroendocrine carcinoma | 82463 | 8246/3 |
| Mixed adenoneuroendocrine carcinoma | 82443 | 8244/3 |
| **Adenocarcinoma in situ** | 81402 | 8140/2 |
| High-grade dysplasia | 81481 | 8148/1 |
| Adenoma with high-grade dysplasia | 82101 | 8210/1 |

### Topography Codes

| Site | SNOMED CT | ICD-O-3 |
|------|-----------|---------|
| Colon, NOS | T-59000 | C18.9 |
| Cecum | T-59100 | C18.0 |
| Appendix | T-59200 | C18.1 |
| Ascending colon | T-59300 | C18.2 |
| Hepatic flexure | T-59400 | C18.3 |
| Transverse colon | T-59500 | C18.4 |
| Splenic flexure | T-59600 | C18.5 |
| Descending colon | T-59700 | C18.6 |
| Sigmoid colon | T-59800 | C18.7 |
| Overlapping colon | T-59900 | C18.8 |
| Rectosigmoid junction | T-59950 | C19.9 |
| Rectum | T-68000 | C20.9 |
| Anus | T-69000 | C21.0 |

---

## Pancreatic Carcinoma Codes

### Morphology Codes

| Histologic Type | SNOMED CT Code | ICD-O-3 |
|-----------------|----------------|---------|
| **Ductal adenocarcinoma** | 85003 | 8500/3 |
| Ductal adenocarcinoma, well differentiated | 85003 | 8500/3 |
| Ductal adenocarcinoma, moderately differentiated | 85003 | 8500/3 |
| Ductal adenocarcinoma, poorly differentiated | 85003 | 8500/3 |
| Adenosquamous carcinoma | 85603 | 8560/3 |
| Colloid carcinoma (mucinous noncystic) | 84803 | 8480/3 |
| Hepatoid carcinoma | 85763 | 8576/3 |
| Medullary carcinoma | 85103 | 8510/3 |
| Signet ring cell carcinoma | 84903 | 8490/3 |
| Undifferentiated carcinoma | 80203 | 8020/3 |
| Undifferentiated with osteoclast-like giant cells | 80353 | 8035/3 |
| Acinar cell carcinoma | 85503 | 8550/3 |
| Pancreatoblastoma | 89713 | 8971/3 |
| Intraductal papillary mucinous neoplasm with invasion | 84533 | 8453/3 |
| Mucinous cystic neoplasm with invasion | 84703 | 8470/3 |
| Solid pseudopapillary neoplasm | 84523 | 8452/3 |
| Neuroendocrine carcinoma | 82463 | 8246/3 |
| **PanIN-3 / High-grade dysplasia** | 81482 | 8148/2 |
| IPMN with high-grade dysplasia | 84532 | 8453/2 |

### Topography Codes

| Site | SNOMED CT | ICD-O-3 |
|------|-----------|---------|
| Pancreas, NOS | T-65000 | C25.9 |
| Head of pancreas | T-65100 | C25.0 |
| Body of pancreas | T-65200 | C25.1 |
| Tail of pancreas | T-65300 | C25.2 |
| Pancreatic duct | T-65400 | C25.3 |
| Islets of Langerhans | T-65500 | C25.4 |
| Overlapping pancreas | T-65800 | C25.8 |
| Ampulla of Vater | T-64700 | C24.1 |
| Extrahepatic bile duct | T-64500 | C24.0 |

---

## Gastric Carcinoma Codes

### Morphology Codes

| Histologic Type | SNOMED CT Code | ICD-O-3 |
|-----------------|----------------|---------|
| **Tubular adenocarcinoma** | 82113 | 8211/3 |
| Papillary adenocarcinoma | 82603 | 8260/3 |
| Mucinous adenocarcinoma | 84803 | 8480/3 |
| Poorly cohesive carcinoma | 84903 | 8490/3 |
| Signet ring cell carcinoma | 84903 | 8490/3 |
| Mixed adenocarcinoma | 82553 | 8255/3 |
| Adenosquamous carcinoma | 85603 | 8560/3 |
| Squamous cell carcinoma | 80703 | 8070/3 |
| Hepatoid adenocarcinoma | 85763 | 8576/3 |
| Carcinoma with lymphoid stroma | 85123 | 8512/3 |
| Micropapillary adenocarcinoma | 82653 | 8265/3 |
| Undifferentiated carcinoma | 80203 | 8020/3 |
| Neuroendocrine carcinoma | 82463 | 8246/3 |
| Mixed adenoneuroendocrine carcinoma | 82443 | 8244/3 |
| **High-grade dysplasia** | 81482 | 8148/2 |
| Adenocarcinoma in situ | 81402 | 8140/2 |

### Topography Codes

| Site | SNOMED CT | ICD-O-3 |
|------|-----------|---------|
| Stomach, NOS | T-63000 | C16.9 |
| Cardia | T-63100 | C16.0 |
| Fundus | T-63200 | C16.1 |
| Body (corpus) | T-63300 | C16.2 |
| Gastric antrum | T-63400 | C16.3 |
| Pylorus | T-63500 | C16.4 |
| Lesser curvature, NOS | T-63600 | C16.5 |
| Greater curvature, NOS | T-63700 | C16.6 |
| Overlapping stomach | T-63800 | C16.8 |
| Esophagogastric junction | T-62900 | C16.0 |

### Laurén Classification Codes

| Type | SNOMED CT |
|------|-----------|
| Intestinal type | 87737001 |
| Diffuse type | 44401000 |
| Mixed type | 128883000 |

---

## Behavior Codes

| Behavior | Code | Description |
|----------|------|-------------|
| Benign | /0 | Non-cancerous |
| Uncertain | /1 | Borderline, uncertain malignant potential |
| In situ | /2 | Non-invasive, confined to epithelium |
| Malignant, primary | /3 | Invasive cancer, primary site |
| Malignant, metastatic | /6 | Cancer spread from another site |
| Malignant, uncertain | /9 | Unknown if primary or metastatic |

---

## Grade/Differentiation Codes

| Grade | SNOMED CT Code | Description |
|-------|----------------|-------------|
| G1 | 54102005 | Well differentiated |
| G2 | 1663004 | Moderately differentiated |
| G3 | 61026006 | Poorly differentiated |
| G4 | 258245003 | Undifferentiated |
| GX | 60815008 | Cannot be assessed |

---

## Procedure/Specimen Codes

### Breast Specimens

| Procedure | SNOMED CT |
|-----------|-----------|
| Lumpectomy | 392021009 |
| Wide local excision | 64368001 |
| Mastectomy | 172043006 |
| Modified radical mastectomy | 384723003 |
| Sentinel lymph node biopsy | 396487001 |
| Axillary lymph node dissection | 234262008 |

### Colorectal Specimens

| Procedure | SNOMED CT |
|-----------|-----------|
| Right hemicolectomy | 26925003 |
| Left hemicolectomy | 80294005 |
| Sigmoid colectomy | 43075005 |
| Low anterior resection | 265340005 |
| Abdominoperineal resection | 26390003 |
| Total colectomy | 23968004 |
| Transanal excision | 265459006 |
| Polypectomy | 274031008 |

### Pancreatic Specimens

| Procedure | SNOMED CT |
|-----------|-----------|
| Pancreaticoduodenectomy (Whipple) | 68471007 |
| Pylorus-preserving pancreaticoduodenectomy | 265486001 |
| Distal pancreatectomy | 69036001 |
| Total pancreatectomy | 33149006 |
| Central pancreatectomy | 440383008 |

### Gastric Specimens

| Procedure | SNOMED CT |
|-----------|-----------|
| Partial gastrectomy | 26452001 |
| Subtotal gastrectomy | 287816003 |
| Total gastrectomy | 53442002 |
| Proximal gastrectomy | 287817007 |
| Wedge resection | 65801008 |
| Endoscopic mucosal resection (EMR) | 450437008 |
| Endoscopic submucosal dissection (ESD) | 713278001 |

---

## Usage Instructions

### For Report Analysis

When analyzing a report, extract:
1. **Tumor histologic type** → Map to morphology code
2. **Anatomic site** → Map to topography code
3. **Behavior** (in situ vs invasive) → Add behavior suffix
4. **Grade** → Add grade code
5. **Procedure** → Add procedure code

### Output Format

```
═══════════════════════════════════════════════════════════════
SNOMED CT CODING
═══════════════════════════════════════════════════════════════
Morphology:
  Code: 8500/3
  Term: Invasive ductal carcinoma
  SNOMED CT: 82113

Topography:
  Code: C50.4
  Term: Upper outer quadrant of breast
  SNOMED CT: T-04500

Grade:
  Code: G2
  Term: Moderately differentiated
  SNOMED CT: 1663004

Procedure:
  Term: Lumpectomy
  SNOMED CT: 392021009

Combined ICD-O-3: 8500/3 - C50.4
───────────────────────────────────────────────────────────────
```

### Auto-Suggestion Logic

From report text, identify:

1. **Keywords for histologic type:**
   - "invasive ductal" / "invaziv duktal" → 8500/3
   - "lobular" / "lobüler" → 8520/3
   - "mucinous" / "müsinöz" → 8480/3
   - "signet ring" / "taşlı yüzük" → 8490/3

2. **Keywords for site:**
   - "upper outer" / "üst dış" → C50.4
   - "sigmoid" → C18.7
   - "head of pancreas" / "pankreas başı" → C25.0
   - "antrum" → C16.3

3. **Keywords for behavior:**
   - "invasive" / "invaziv" → /3
   - "in situ" → /2
   - "metastatic" / "metastatik" → /6

---

## Turkish Terminology Mapping

### Histologic Types

| Turkish | English | Code |
|---------|---------|------|
| İnvaziv duktal karsinom | Invasive ductal carcinoma | 8500/3 |
| İnvaziv lobüler karsinom | Invasive lobular carcinoma | 8520/3 |
| Müsinöz adenokarsinom | Mucinous adenocarcinoma | 8480/3 |
| Taşlı yüzük hücreli karsinom | Signet ring cell carcinoma | 8490/3 |
| Az koheziv karsinom | Poorly cohesive carcinoma | 8490/3 |
| Tübüler adenokarsinom | Tubular adenocarcinoma | 8211/3 |
| Papiller adenokarsinom | Papillary adenocarcinoma | 8260/3 |
| Medüller karsinom | Medullary carcinoma | 8510/3 |
| Adenoskuamöz karsinom | Adenosquamous carcinoma | 8560/3 |
| İndiferansiye karsinom | Undifferentiated carcinoma | 8020/3 |
| Duktal adenokarsinom | Ductal adenocarcinoma | 8500/3 |
| Asiner hücreli karsinom | Acinar cell carcinoma | 8550/3 |
| Nöroendokrin karsinom | Neuroendocrine carcinoma | 8246/3 |

### Anatomic Sites

| Turkish | English | Code |
|---------|---------|------|
| Meme | Breast | C50.9 |
| Üst dış kadran | Upper outer quadrant | C50.4 |
| Üst iç kadran | Upper inner quadrant | C50.2 |
| Alt dış kadran | Lower outer quadrant | C50.5 |
| Alt iç kadran | Lower inner quadrant | C50.3 |
| Meme başı | Nipple | C50.0 |
| Çekum | Cecum | C18.0 |
| Çıkan kolon | Ascending colon | C18.2 |
| Transvers kolon | Transverse colon | C18.4 |
| İnen kolon | Descending colon | C18.6 |
| Sigmoid kolon | Sigmoid colon | C18.7 |
| Rektum | Rectum | C20.9 |
| Pankreas başı | Head of pancreas | C25.0 |
| Pankreas gövdesi | Body of pancreas | C25.1 |
| Pankreas kuyruğu | Tail of pancreas | C25.2 |
| Mide | Stomach | C16.9 |
| Kardiya | Cardia | C16.0 |
| Fundus | Fundus | C16.1 |
| Korpus | Body | C16.2 |
| Antrum | Antrum | C16.3 |
| Pilor | Pylorus | C16.4 |
| Küçük kurvatur | Lesser curvature | C16.5 |
| Büyük kurvatur | Greater curvature | C16.6 |

### Differentiation

| Turkish | English | Code |
|---------|---------|------|
| İyi diferansiye | Well differentiated | G1 |
| Orta diferansiye | Moderately differentiated | G2 |
| Az diferansiye | Poorly differentiated | G3 |
| İndiferansiye | Undifferentiated | G4 |

---

## Cross-Reference Tables

### Breast - Complete Coding

| Diagnosis | Morphology | Site Example | Full Code |
|-----------|------------|--------------|-----------|
| IDC, UOQ, G2 | 8500/3 | C50.4 | 8500/3-C50.4-G2 |
| ILC, central, G2 | 8520/3 | C50.1 | 8520/3-C50.1-G2 |
| DCIS, LOQ | 8500/2 | C50.5 | 8500/2-C50.5 |
| Mucinous, UIQ, G1 | 8480/3 | C50.2 | 8480/3-C50.2-G1 |

### Colorectal - Complete Coding

| Diagnosis | Morphology | Site | Full Code |
|-----------|------------|------|-----------|
| Adenoca, sigmoid, G2 | 8140/3 | C18.7 | 8140/3-C18.7-G2 |
| Mucinous, cecum, G2 | 8480/3 | C18.0 | 8480/3-C18.0-G2 |
| Signet ring, rectum, G3 | 8490/3 | C20.9 | 8490/3-C20.9-G3 |

### Pancreas - Complete Coding

| Diagnosis | Morphology | Site | Full Code |
|-----------|------------|------|-----------|
| Ductal adenoca, head, G2 | 8500/3 | C25.0 | 8500/3-C25.0-G2 |
| Ductal adenoca, tail, G3 | 8500/3 | C25.2 | 8500/3-C25.2-G3 |
| Acinar cell, body, G2 | 8550/3 | C25.1 | 8550/3-C25.1-G2 |

### Gastric - Complete Coding

| Diagnosis | Morphology | Site | Full Code |
|-----------|------------|------|-----------|
| Tubular adenoca, antrum, G2 | 8211/3 | C16.3 | 8211/3-C16.3-G2 |
| Signet ring, body, G3 | 8490/3 | C16.2 | 8490/3-C16.2-G3 |
| Mucinous, cardia, G2 | 8480/3 | C16.0 | 8480/3-C16.0-G2 |

---

## Validation Rules

| Check | Rule |
|-------|------|
| Morphology matches histologic type | Must correspond |
| Behavior code matches invasion status | /2 for in situ, /3 for invasive |
| Topography matches stated site | Must correspond |
| Grade code matches stated grade | Must correspond |

---

## References

- SNOMED CT International Edition
- ICD-O-3 (International Classification of Diseases for Oncology, 3rd Edition)
- WHO Classification of Tumours, 5th Edition
- CAP Cancer Protocols
