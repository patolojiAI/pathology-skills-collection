# Tumor Board Summary Generator

Generate concise 3-5 line multidisciplinary team (MDT) summaries from pathology reports.

## Purpose

Provide a standardized, concise summary suitable for:
- Tumor board / MDT meetings
- Oncology referrals
- Clinical chart notes
- Case presentations

---

## Output Format

### Standard Template (3-5 lines)

```
[Age][Sex] with [TUMOR TYPE] of the [SITE/LOCATION].
[PROCEDURE]: [SIZE] [HISTOLOGIC TYPE], [GRADE], [STAGE (pTNM)].
Margins: [STATUS]. LVI: [+/-]. PNI: [+/-]. Nodes: [X/Y positive].
Biomarkers: [KEY RESULTS].
[ADDITIONAL CRITICAL FINDINGS if any].
```

### Example Outputs

**Breast:**
```
58F with invasive carcinoma of the left breast, upper outer quadrant.
Lumpectomy: 2.3 cm invasive ductal carcinoma, Grade 2, pT2 N1a M0 (Stage IIB).
Margins: Negative (closest 3mm anterior). LVI: Present. Nodes: 2/15 positive.
ER 95%/PR 80%/HER2 negative/Ki-67 25%.
```

**Colorectal:**
```
67M with adenocarcinoma of the sigmoid colon.
Sigmoid colectomy: 4.5 cm moderately differentiated adenocarcinoma, pT3 N1b M0 (Stage IIIB).
Margins: Negative (CRM 8mm). LVI: Present (venous). PNI: Absent. Nodes: 3/18 positive.
MSI-stable (MMR intact). KRAS G12D mutation detected.
```

**Pancreas:**
```
72F with adenocarcinoma of the pancreatic head.
Whipple: 3.2 cm moderately differentiated ductal adenocarcinoma, pT2 N1 M0 (Stage IIB).
Margins: R1 (SMA margin 0.5mm). LVI: Present. PNI: Present. Nodes: 2/14 positive.
Post-neoadjuvant (partial response). Background PanIN-2.
```

**Gastric:**
```
55M with adenocarcinoma of the gastric antrum.
Subtotal gastrectomy: 5.0 cm poorly cohesive carcinoma (signet ring), pT3 N2 M0 (Stage IIIA).
Margins: Negative (proximal 4cm, distal 3cm). LVI: Present. PNI: Present. Nodes: 4/22 positive.
HER2 negative (IHC 1+). Lauren diffuse type.
```

---

## Required Elements by Tumor Type

### All Tumors (Universal)

| Element | Format |
|---------|--------|
| Age/Sex | ##M or ##F |
| Diagnosis | Tumor type + site |
| Procedure | Specimen type |
| Size | cm, largest dimension |
| Histologic type | WHO classification |
| Grade | G1/G2/G3 or well/mod/poorly diff |
| pTNM | Individual categories |
| Stage group | AJCC 8th edition |
| Margins | Positive/Negative + distance |
| LVI | Present/Absent |
| PNI | Present/Absent |
| Nodes | Positive/Total |

### Breast-Specific

| Element | Format |
|---------|--------|
| Laterality | Left/Right |
| Quadrant/Location | UOQ, UIQ, LOQ, LIQ, central, etc. |
| Nottingham grade | Grade 1/2/3 (score X/9) |
| DCIS component | Present/Absent, % if present |
| ER | % positive + intensity |
| PR | % positive + intensity |
| HER2 | Negative/Equivocal/Positive (IHC score, FISH if done) |
| Ki-67 | % |
| Oncotype/MammaPrint | Score if available |

### Colorectal-Specific

| Element | Format |
|---------|--------|
| Location | Cecum → Rectum |
| CRM | Distance in mm (rectal) |
| Mesorectal quality | Complete/Nearly complete/Incomplete |
| Tumor deposits | Number if present |
| MMR/MSI | Intact/Deficient or Stable/High |
| KRAS/NRAS/BRAF | Wild-type or mutation specified |
| Neoadjuvant response | If applicable (TRG) |

### Pancreas-Specific

| Element | Format |
|---------|--------|
| Location | Head/Uncinate/Body/Tail |
| R status | R0/R1/R2 |
| Closest margin | Which margin + distance |
| Major vessel involvement | If present |
| PanIN | Grade if present |
| Treatment effect | If neoadjuvant given |

### Gastric-Specific

| Element | Format |
|---------|--------|
| Location | Cardia/Fundus/Body/Antrum/Pylorus |
| Lauren classification | Intestinal/Diffuse/Mixed |
| Borrmann type | I-V if applicable |
| HER2 | IHC score + FISH if 2+ |
| MSI/MMR | Status |
| PD-L1 CPS | Score if available |

---

## Extraction Rules

### From Report Text

1. **Demographics**: Extract age and sex from header/clinical info
2. **Procedure**: From specimen description or procedure field
3. **Tumor details**: From diagnosis/microscopic sections
4. **Stage**: From pathologic staging section; calculate if not stated
5. **Margins**: From margin section; note R status for pancreas
6. **Nodes**: X positive / Y total examined
7. **Biomarkers**: From ancillary studies section

### Handling Missing Data

| Scenario | Action |
|----------|--------|
| Age/Sex unknown | Use "[Age unknown]" or omit |
| Stage not stated | Calculate from pTNM if possible, or "[Stage pending]" |
| Biomarkers pending | State "[Biomarkers pending]" |
| Data not applicable | Omit element |

### Abbreviations (Acceptable)

| Full Term | Abbreviation |
|-----------|--------------|
| Invasive ductal carcinoma | IDC |
| Invasive lobular carcinoma | ILC |
| Ductal carcinoma in situ | DCIS |
| Adenocarcinoma | Adenoca |
| Moderately differentiated | Mod diff |
| Poorly differentiated | Poorly diff |
| Lymphovascular invasion | LVI |
| Perineural invasion | PNI |
| Circumferential resection margin | CRM |
| Mismatch repair | MMR |
| Microsatellite instability | MSI |

---

## Language Options

### English (Default)

```
58F with invasive carcinoma of the left breast, upper outer quadrant.
Lumpectomy: 2.3 cm invasive ductal carcinoma, Grade 2, pT2 N1a M0 (Stage IIB).
Margins: Negative (closest 3mm anterior). LVI: Present. Nodes: 2/15 positive.
ER 95%/PR 80%/HER2 negative/Ki-67 25%.
```

### Turkish (Türkçe)

```
58 yaşında kadın, sol meme üst dış kadran invaziv karsinom.
Lumpektomi: 2.3 cm invaziv duktal karsinom, Grade 2, pT2 N1a M0 (Evre IIB).
Sınırlar: Negatif (en yakın 3mm anterior). LVİ: Var. Lenf nodları: 2/15 pozitif.
ER %95/PR %80/HER2 negatif/Ki-67 %25.
```

### Turkish Abbreviations

| English | Turkish |
|---------|---------|
| LVI | LVİ (Lenfovasküler invazyon) |
| PNI | PNİ (Perinöral invazyon) |
| Present | Var |
| Absent | Yok |
| Negative | Negatif |
| Positive | Pozitif |
| Stage | Evre |
| Nodes | Lenf nodları |
| Margins | Sınırlar |

---

## Trigger Phrases

### English

```
Generate a tumor board summary
Create an MDT summary
Summarize for tumor board
Give me a case summary
Write a brief oncology summary
```

### Turkish

```
Tümör kurulu özeti oluştur
MDT özeti yaz
Onkoloji konsültasyon özeti
Vaka özeti hazırla
Kısa patoloji özeti
```

---

## Special Scenarios

### Neoadjuvant Therapy

Add treatment response:
```
Post-neoadjuvant (NACT): [Response grade or description].
ypT1 ypN0 → Pathologic complete response (pCR) vs. residual disease.
```

### Multifocal/Multicentric Disease

```
Multifocal disease: 2.3 cm + 1.1 cm invasive ductal carcinoma (same quadrant).
Largest focus used for T staging.
```

### Synchronous Tumors

```
Synchronous bilateral breast carcinoma.
Right: 1.8 cm IDC Grade 2, pT1c N0.
Left: 2.5 cm ILC Grade 2, pT2 N1a.
```

### Recurrent Disease

```
Recurrent adenocarcinoma at anastomotic site.
rT3 N1 M0. Compare to original diagnosis [date].
```

---

## Quality Checklist

Before finalizing summary, verify:

- [ ] Age and sex included
- [ ] Tumor type and site specified
- [ ] Procedure stated
- [ ] Size documented
- [ ] Histologic type + grade included
- [ ] pTNM categories stated
- [ ] Stage group calculated/verified
- [ ] Margin status summarized
- [ ] LVI and PNI status included
- [ ] Lymph node ratio included
- [ ] Key biomarkers included
- [ ] No extraneous details
- [ ] 3-5 lines maximum
- [ ] Clinically actionable information prioritized

---

## Examples by Complexity

### Simple Case (3 lines)

```
45F with invasive carcinoma of the right breast.
Mastectomy: 1.5 cm invasive ductal carcinoma, Grade 1, pT1c N0 M0 (Stage IA).
Margins: Negative. LVI: Absent. ER 99%/PR 95%/HER2 neg/Ki-67 10%.
```

### Moderate Case (4 lines)

```
62M with adenocarcinoma of the rectum.
LAR with TME: 3.8 cm moderately differentiated adenocarcinoma, pT3 N1a M0 (Stage IIIB).
Margins: Negative (CRM 5mm, distal 2.5cm). Mesorectum: Complete. LVI: Present. PNI: Absent. Nodes: 1/16.
MMR intact. Tumor deposits: 2.
```

### Complex Case (5 lines)

```
71F with adenocarcinoma of the pancreatic head.
Whipple (post-neoadjuvant): 2.8 cm moderately differentiated ductal adenocarcinoma, ypT2 N1 M0 (Stage IIB).
Margins: R0 (SMA 2mm, posterior 3mm, bile duct/pancreatic negative). LVI: Present. PNI: Extensive.
Nodes: 3/21 positive. Treatment effect: Moderate response (40% viable tumor).
Background chronic pancreatitis and PanIN-2 at pancreatic margin.
```

---

## Integration with Report Checker

When generating tumor board summary:

1. First extract all required elements using diagnosis reference files
2. Verify pTNM staging using `references/staging/tnm_stage_calculator.md`
3. Confirm biomarker interpretation using `references/biomarkers/BIOMARKERS_INDEX.md`
4. Generate summary in requested language
5. Flag any missing critical elements

---

## Output Formatting

### Plain Text (Default)

```
58F with invasive carcinoma of the left breast, upper outer quadrant.
Lumpectomy: 2.3 cm invasive ductal carcinoma, Grade 2, pT2 N1a M0 (Stage IIB).
Margins: Negative (closest 3mm anterior). LVI: Present. Nodes: 2/15 positive.
ER 95%/PR 80%/HER2 negative/Ki-67 25%.
```

### Structured (Optional)

```
TUMOR BOARD SUMMARY
═══════════════════════════════════════════════════════════════
Patient: 58F
Diagnosis: Invasive ductal carcinoma, left breast (UOQ)
Procedure: Lumpectomy
Tumor: 2.3 cm, Grade 2
Stage: pT2 N1a M0 (Stage IIB)
Margins: Negative (closest 3mm anterior)
LVI/PNI: LVI present, PNI absent
Nodes: 2/15 positive (13%)
Biomarkers: ER 95%, PR 80%, HER2 neg, Ki-67 25%
───────────────────────────────────────────────────────────────
```
