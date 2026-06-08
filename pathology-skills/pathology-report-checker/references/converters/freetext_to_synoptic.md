# Free-Text to Synoptic Converter

Convert narrative/prose pathology reports into structured CAP-compliant synoptic format.

## Purpose

Transform unstructured pathology reports into standardized synoptic format for:
- Cancer registry submission
- Tumor board presentation
- Quality assurance compliance
- Electronic health record integration

---

## Workflow

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Free-Text      │ ──► │  Extract &       │ ──► │  Synoptic       │
│  Report         │     │  Map Elements    │     │  Output         │
└─────────────────┘     └──────────────────┘     └─────────────────┘
```

### Step 1: Identify Report Type

Detect tumor type from report content:

| Keywords (English) | Keywords (Turkish) | Type |
|-------------------|-------------------|------|
| breast, mastectomy, lumpectomy, ductal, lobular | meme, mastektomi, lumpektomi, duktal, lobüler | Breast |
| colon, rectum, colectomy, adenocarcinoma | kolon, rektum, kolektomi, adenokarsinom | Colorectal |
| pancreas, Whipple, pancreatectomy, ductal | pankreas, Whipple, pankreatektomi, duktal | Pancreas |
| stomach, gastric, gastrectomy | mide, gastrik, gastrektomi | Gastric |

### Step 2: Extract Elements

Parse free-text to identify values for each required field.

### Step 3: Generate Synoptic Output

Format extracted data into CAP-compliant synoptic structure.

---

## Extraction Patterns

### Tumor Size

**English patterns:**
```
- "X cm tumor" / "tumor measuring X cm"
- "X x Y x Z cm mass"
- "greatest dimension X cm"
- "X cm in maximum diameter"
```

**Turkish patterns:**
```
- "X cm tümör" / "X cm çaplı tümör"
- "X x Y x Z cm kitle"
- "en büyük çap X cm"
- "maksimum çap X cm"
```

**Extraction rule:** Capture all numeric dimensions; use largest for T staging

### Histologic Type

**Breast:**
| Free-text | Synoptic Value |
|-----------|----------------|
| "invasive ductal carcinoma", "IDC", "ductal carcinoma NOS" | Invasive carcinoma of no special type |
| "invasive lobular carcinoma", "ILC" | Invasive lobular carcinoma |
| "mucinous carcinoma", "colloid" | Mucinous carcinoma |
| "invaziv duktal karsinom" | İnvaziv karsinom, özel tip değil |
| "invaziv lobüler karsinom" | İnvaziv lobüler karsinom |

**Colorectal:**
| Free-text | Synoptic Value |
|-----------|----------------|
| "adenocarcinoma", "adenoca", "colonic adenocarcinoma" | Adenocarcinoma |
| "mucinous adenocarcinoma", "mucinous carcinoma" | Mucinous adenocarcinoma |
| "signet ring cell", "signet ring carcinoma" | Signet ring cell carcinoma |
| "adenokarsinom" | Adenokarsinom |
| "müsinöz adenokarsinom" | Müsinöz adenokarsinom |

**Pancreas:**
| Free-text | Synoptic Value |
|-----------|----------------|
| "ductal adenocarcinoma", "pancreatic adenocarcinoma" | Ductal adenocarcinoma |
| "acinar cell carcinoma" | Acinar cell carcinoma |
| "IPMN with invasion", "invasive IPMN" | Carcinoma arising in IPMN |
| "duktal adenokarsinom" | Duktal adenokarsinom |

**Gastric:**
| Free-text | Synoptic Value |
|-----------|----------------|
| "tubular adenocarcinoma" | Tubular adenocarcinoma |
| "papillary adenocarcinoma" | Papillary adenocarcinoma |
| "poorly cohesive", "signet ring", "diffuse type" | Poorly cohesive carcinoma |
| "tübüler adenokarsinom" | Tübüler adenokarsinom |
| "taşlı yüzük hücreli" | Az koheziv karsinom |

### Grade

**Patterns:**
| Free-text | Synoptic Value |
|-----------|----------------|
| "well differentiated", "grade 1", "G1", "low grade" | G1 - Well differentiated |
| "moderately differentiated", "grade 2", "G2", "intermediate" | G2 - Moderately differentiated |
| "poorly differentiated", "grade 3", "G3", "high grade" | G3 - Poorly differentiated |
| "iyi diferansiye", "derece 1" | G1 - İyi diferansiye |
| "orta diferansiye", "derece 2" | G2 - Orta diferansiye |
| "az diferansiye", "derece 3" | G3 - Az diferansiye |

**Breast Nottingham Grade:**
| Free-text | Extraction |
|-----------|------------|
| "Nottingham grade 2 (score 6)" | Grade 2, Score 6/9 |
| "tubule formation 3, nuclear grade 2, mitoses 1" | Components: 3+2+1=6 |
| "total score 7/9" | Score 7, Grade 2 |

### Margins

**Patterns:**
```
English:
- "margins negative" / "margins uninvolved" / "margins free"
- "closest margin X mm" / "X mm to [margin name]"
- "margin positive" / "margin involved" / "ink on tumor"
- "R0 resection" / "R1 resection"

Turkish:
- "sınırlar negatif" / "sınırlar temiz" / "sınırlara ulaşmıyor"
- "en yakın sınır X mm" / "[sınır adı]'na X mm"
- "sınır pozitif" / "sınır tutulmuş"
```

**Extraction:**
| Free-text | Synoptic Output |
|-----------|-----------------|
| "All margins negative, closest 3mm anterior" | Status: Uninvolved, Closest: Anterior 3mm |
| "Posterior margin positive for invasive carcinoma" | Status: Involved, Margin: Posterior |
| "CRM 1.5mm" | Circumferential margin: 1.5mm (Negative) |
| "CRM 0.8mm" | Circumferential margin: 0.8mm (Positive, ≤1mm) |

### Lymph Nodes

**Patterns:**
```
English:
- "X of Y lymph nodes positive" / "X/Y nodes involved"
- "Y lymph nodes examined, X with metastasis"
- "sentinel node negative" / "SLN positive"
- "no lymph node metastasis (0/Y)"

Turkish:
- "X/Y lenf nodu pozitif" / "Y lenf nodunun X'i tutulmuş"
- "Y lenf nodu incelendi, X metastatik"
- "sentinel lenf nodu negatif"
```

**Extraction:**
| Free-text | Synoptic Output |
|-----------|-----------------|
| "2 of 18 lymph nodes positive" | Positive: 2, Total: 18 |
| "Metastatic carcinoma in 3/15 nodes" | Positive: 3, Total: 15 |
| "No metastasis in 22 lymph nodes" | Positive: 0, Total: 22 |
| "18 lenf nodunun 2'si pozitif" | Pozitif: 2, Toplam: 18 |

### Lymphovascular Invasion (LVI)

**Patterns:**
| Free-text | Synoptic Value |
|-----------|----------------|
| "LVI present", "lymphovascular invasion identified" | Present |
| "LVI absent", "no lymphovascular invasion" | Not identified |
| "vascular invasion present" | Present |
| "LVI var", "lenfovasküler invazyon mevcut" | Var |
| "LVI yok", "lenfovasküler invazyon izlenmedi" | İzlenmedi |

### Perineural Invasion (PNI)

**Patterns:**
| Free-text | Synoptic Value |
|-----------|----------------|
| "PNI present", "perineural invasion identified" | Present |
| "PNI absent", "no perineural invasion" | Not identified |
| "PNI var", "perinöral invazyon mevcut" | Var |
| "PNI yok", "perinöral invazyon izlenmedi" | İzlenmedi |

### pTNM Staging

**Direct extraction:**
```
- "pT2 N1 M0" / "pT2N1M0" / "pT2, pN1, pM0"
- "Stage IIB" / "Evre IIB"
```

**Derived from text:**
If explicit staging not stated, derive from:
- Tumor size → pT
- Node count → pN
- Metastasis mention → pM

---

## Biomarker Extraction

### Breast (ER/PR/HER2/Ki-67)

**ER/PR patterns:**
```
- "ER positive (95%)" → ER: Positive, 95%
- "ER: 90%, strong" → ER: Positive, 90%, Strong intensity
- "PR negative" → PR: Negative
- "ER %85 pozitif" → ER: Pozitif, %85
```

**HER2 patterns:**
```
- "HER2 negative (score 1+)" → HER2: Negative, IHC 1+
- "HER2 equivocal (2+), FISH positive" → HER2: Positive (FISH amplified)
- "HER2 3+" → HER2: Positive, IHC 3+
- "HER2 negatif (skor 0)" → HER2: Negatif, IHC 0
```

**Ki-67 patterns:**
```
- "Ki-67: 25%" → Ki-67: 25%
- "Ki-67 proliferation index 30%" → Ki-67: 30%
- "Ki-67 %15" → Ki-67: %15
```

### Colorectal (MMR/MSI/KRAS/BRAF)

**MMR/MSI patterns:**
```
- "MMR intact" / "MMR proteins retained" → MMR: Intact
- "MLH1/PMS2 lost" → MMR: Deficient (MLH1/PMS2 loss)
- "MSI-high" / "MSI-H" → MSI: High
- "MSS" / "MSI-stable" → MSI: Stable
```

**KRAS/BRAF patterns:**
```
- "KRAS wild-type" → KRAS: Wild-type
- "KRAS G12D mutation" → KRAS: Mutated (G12D)
- "BRAF V600E positive" → BRAF: Mutated (V600E)
- "KRAS mutasyonu saptanmadı" → KRAS: Vahşi tip
```

### Gastric (HER2/Lauren)

**HER2 patterns:** Same as breast

**Lauren classification:**
```
- "intestinal type" / "Lauren intestinal" → Lauren: Intestinal
- "diffuse type" / "Lauren diffuse" → Lauren: Diffuse
- "mixed type" → Lauren: Mixed
- "intestinal tip" → Lauren: İntestinal
- "diffüz tip" → Lauren: Diffüz
```

---

## Output Format

### Standard Synoptic Template

```
SYNOPTIC REPORT
═══════════════════════════════════════════════════════════════

SPECIMEN
Procedure: ____________________
Specimen Integrity: ____________________

TUMOR
Histologic Type: ____________________
Histologic Grade: ____________________
Tumor Size: ____ x ____ x ____ cm
Tumor Site: ____________________

MARGINS
Status: ____________________
Closest Margin: ____________________ Distance: ____ mm
Specify Positive Margin(s): ____________________

LYMPH NODES
Total Examined: ____
Total Positive: ____
Size of Largest Metastasis: ____ mm
Extranodal Extension: ____________________

PATHOLOGIC STAGING (AJCC 8th Edition)
pT: ____  pN: ____  pM: ____
Stage Group: ____________________

ADDITIONAL FINDINGS
Lymphovascular Invasion: ____________________
Perineural Invasion: ____________________

BIOMARKERS
[Tumor-specific fields]

═══════════════════════════════════════════════════════════════
```

### Tumor-Specific Biomarker Sections

**Breast:**
```
BIOMARKERS
Estrogen Receptor: ____ (____%)
Progesterone Receptor: ____ (____%)
HER2: ____ (IHC: ____, FISH: ____)
Ki-67: ____%
```

**Colorectal:**
```
BIOMARKERS
Mismatch Repair (MMR): ____________________
Microsatellite Instability: ____________________
KRAS: ____________________
NRAS: ____________________
BRAF: ____________________
```

**Gastric:**
```
BIOMARKERS
HER2: ____ (IHC: ____, FISH: ____)
Lauren Classification: ____________________
MSI/MMR: ____________________
```

---

## Conversion Examples

### Example 1: Breast (English → Synoptic)

**Free-text input:**
```
Left breast, lumpectomy: Invasive ductal carcinoma, moderately 
differentiated (Nottingham grade 2, score 6/9), measuring 2.3 x 1.8 x 
1.5 cm. The tumor is located in the upper outer quadrant. All surgical 
margins are negative; the closest margin is the anterior margin at 3mm. 
Lymphovascular invasion is present. No perineural invasion identified. 
Two of fifteen axillary lymph nodes contain metastatic carcinoma (2/15), 
largest deposit 4mm, no extranodal extension. ER positive (95%, strong), 
PR positive (80%, moderate), HER2 negative (IHC 1+), Ki-67 25%.
```

**Synoptic output:**
```
SYNOPTIC REPORT
═══════════════════════════════════════════════════════════════

SPECIMEN
Procedure: Lumpectomy
Laterality: Left
Specimen Integrity: Not specified

TUMOR
Histologic Type: Invasive carcinoma of no special type (ductal)
Histologic Grade: Grade 2 (Nottingham score 6/9)
  - Tubule formation: Not specified
  - Nuclear grade: Not specified
  - Mitotic count: Not specified
Tumor Size: 2.3 x 1.8 x 1.5 cm
Tumor Site: Upper outer quadrant

MARGINS
Status: Uninvolved by invasive carcinoma
Closest Margin: Anterior
Distance to Closest Margin: 3 mm

LYMPH NODES
Total Examined: 15
Total Positive: 2
Size of Largest Metastasis: 4 mm
Extranodal Extension: Not identified

PATHOLOGIC STAGING (AJCC 8th Edition)
pT: pT2 (tumor >2 cm but ≤5 cm)
pN: pN1a (metastases in 1-3 axillary nodes)
pM: Not applicable
Stage Group: IIB

ADDITIONAL FINDINGS
Lymphovascular Invasion: Present
Perineural Invasion: Not identified

BIOMARKERS
Estrogen Receptor: Positive (95%, strong)
Progesterone Receptor: Positive (80%, moderate)
HER2: Negative (IHC 1+)
Ki-67: 25%

═══════════════════════════════════════════════════════════════
```

### Example 2: Colorectal (Turkish → Synoptic)

**Free-text input:**
```
Sigmoid kolon, anterior rezeksiyon: 4.5 x 3.2 x 2.8 cm boyutlarında 
orta diferansiye adenokarsinom. Tümör muskularis propriayı aşarak 
perikolik yağ dokusuna invaze olmuştur. Proksimal ve distal cerrahi 
sınırlar temizdir (proksimal 8cm, distal 5cm). Çevresel sınır 6mm. 
Lenfovasküler invazyon mevcut, perinöral invazyon izlenmedi. 
İncelenen 22 lenf nodunun 3'ünde metastatik adenokarsinom saptandı 
(3/22). MMR proteinleri intakt (MLH1, PMS2, MSH2, MSH6 korunmuş). 
KRAS G12V mutasyonu pozitif.
```

**Synoptic output:**
```
SİNOPTİK RAPOR
═══════════════════════════════════════════════════════════════

MATERYAL
İşlem: Anterior rezeksiyon
Lokalizasyon: Sigmoid kolon

TÜMÖR
Histolojik Tip: Adenokarsinom
Histolojik Derece: G2 - Orta diferansiye
Tümör Boyutu: 4.5 x 3.2 x 2.8 cm
İnvazyon Derinliği: Perikolik yağ dokusu (muskularis propria ötesi)

CERRAHİ SINIRLAR
Durum: Negatif
Proksimal Sınır: 8 cm
Distal Sınır: 5 cm
Çevresel (Radyal) Sınır: 6 mm (Negatif, >1mm)

LENF NODLARI
Toplam İncelenen: 22
Toplam Pozitif: 3
Ekstranodal Yayılım: Belirtilmemiş

PATOLOJİK EVRELEME (AJCC 8. Edisyon)
pT: pT3 (muskularis propria ötesine invazyon)
pN: pN1b (2-3 pozitif lenf nodu)
pM: Uygulanamaz
Evre Grubu: IIIB

EK BULGULAR
Lenfovasküler İnvazyon: Var
Perinöral İnvazyon: İzlenmedi

BİYOBELİRTEÇLER
MMR Durumu: İntakt (MLH1, PMS2, MSH2, MSH6 korunmuş)
KRAS: Mutant (G12V)
BRAF: Belirtilmemiş

═══════════════════════════════════════════════════════════════
```

---

## Handling Ambiguity

### Missing Information

| Scenario | Action |
|----------|--------|
| Element not mentioned | Mark as "Not specified" or "Cannot be determined" |
| Conflicting information | Flag for review, use most specific value |
| Incomplete data | Extract what's available, note gaps |

### Uncertain Extraction

When confidence is low:
```
Tumor Size: 2.3 cm [?]
  └─ Note: "approximately 2cm" in source text
```

### Multiple Tumors

For multifocal/multicentric:
```
TUMOR (Focus 1)
Size: 2.3 cm
Location: Upper outer quadrant

TUMOR (Focus 2)
Size: 0.8 cm
Location: Upper outer quadrant
Distance from Focus 1: 1.5 cm
```

---

## Trigger Phrases

### English
```
Convert this report to synoptic format
Generate synoptic report from this text
Transform to CAP format
Create structured report
Extract synoptic data
Free-text to synoptic
```

### Turkish
```
Bu raporu sinoptik formata dönüştür
Sinoptik rapor oluştur
CAP formatına çevir
Yapılandırılmış rapor oluştur
Serbest metinden sinoptik çıkar
```

---

## Quality Checks

After conversion, verify:

- [ ] All required elements extracted or marked as not specified
- [ ] pT/pN categories consistent with extracted data
- [ ] Stage group matches pTNM
- [ ] Margin status consistent with distances
- [ ] Node ratio matches total/positive counts
- [ ] Biomarkers complete for tumor type
- [ ] No conflicting information

---

## Integration with Other Features

### With Compliance Checker
1. Convert free-text → synoptic
2. Run compliance check on synoptic output
3. Report both conversion and compliance results

### With Tumor Board Summary
1. Convert free-text → synoptic
2. Generate tumor board summary from synoptic
3. Provide both outputs

### With SNOMED Coding
1. Convert free-text → synoptic
2. Add SNOMED CT codes based on extracted values
3. Include coding section in output
