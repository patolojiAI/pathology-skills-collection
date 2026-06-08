# Synoptic Template Generator

Generate blank CAP-style synoptic report templates with all required fields for each tumor type.

## Contents

- [Usage](#usage)
- [Template Format Standards](#template-format-standards)
- [Breast Invasive Carcinoma Template](#breast-invasive-carcinoma-template)
  - Lumpectomy / Partial Mastectomy
  - Total Mastectomy / Modified Radical Mastectomy
- [Colorectal Resection Template](#colorectal-resection-template)
  - Colon Resection
  - Rectal Resection (Anterior/Low Anterior Resection)
- [Exocrine Pancreas Carcinoma Template](#exocrine-pancreas-carcinoma-template)
  - Whipple (Pancreaticoduodenectomy)
  - Distal Pancreatectomy
- [Gastric Carcinoma Template](#gastric-carcinoma-template)
  - Total Gastrectomy
  - Partial/Subtotal Gastrectomy

---

## Usage

When user requests a template:
1. Identify tumor type and specimen type
2. Use grep to find the appropriate template section (see Quick Search below)
3. Return formatted template with all required fields
4. Optionally pre-fill known values if provided

**Quick Search:**
```bash
grep -A 100 "## Breast Invasive" references/templates/synoptic_templates.md
grep -A 100 "## Colorectal" references/templates/synoptic_templates.md
grep -A 100 "## Exocrine Pancreas" references/templates/synoptic_templates.md
grep -A 100 "## Gastric" references/templates/synoptic_templates.md
```

**Example requests:**
- "Generate a blank synoptic template for breast lumpectomy"
- "Give me a CAP template for Whipple specimen"
- "Create a gastric carcinoma report template for 2.5cm Grade 2 adenocarcinoma" (with pre-fill)

---

## Template Format Standards

### CAP Synoptic Format Requirements

1. **Data element on separate line** from its response
2. **Responses immediately follow** their data elements
3. **Consistent formatting** throughout
4. **All required elements** included even if blank
5. **Conditional elements** included with applicability notes

### Field Markers

| Marker | Meaning |
|--------|---------|
| `___` | Free text field |
| `[ ]` | Checkbox (select one or more) |
| `(_)` | Radio button (select exactly one) |
| `#` | Numeric value |
| `*` | Required/Core element |
| `+` | Conditional element |
| `°` | Optional/Recommended element |

---

## Breast Invasive Carcinoma Template

### Lumpectomy / Partial Mastectomy

```
═══════════════════════════════════════════════════════════════
BREAST - INVASIVE CARCINOMA
Synoptic Report Template (CAP Protocol)
═══════════════════════════════════════════════════════════════

CLINICAL INFORMATION
───────────────────────────────────────────────────────────────
Clinical History: _______________________________________________
Laterality: (_) Right  (_) Left  (_) Bilateral
Neoadjuvant Therapy: (_) No  (_) Yes, specify: _________________

SPECIMEN
───────────────────────────────────────────────────────────────
*Procedure:
  (_) Excision (less than total mastectomy)
  (_) Total mastectomy
  (_) Other: ___________________________________________________

*Specimen Integrity:
  (_) Intact
  (_) Fragmented

Specimen Size: ___ x ___ x ___ cm
Specimen Weight: ___ g

TUMOR
───────────────────────────────────────────────────────────────
*Tumor Site:
  [ ] Upper outer quadrant
  [ ] Lower outer quadrant
  [ ] Upper inner quadrant
  [ ] Lower inner quadrant
  [ ] Central
  [ ] Clock position: ___ o'clock

*Tumor Size (Invasive Component):
  Greatest dimension: ___ cm
  Additional dimensions: ___ x ___ cm

*Tumor Focality:
  (_) Unifocal
  (_) Multifocal (multiple foci in same quadrant)
  (_) Multicentric (foci in different quadrants)

+If multifocal/multicentric:
  Number of foci: ___
  Size of largest focus: ___ cm
  Size of other foci: ___________________________________________

HISTOLOGIC TYPE
───────────────────────────────────────────────────────────────
*Histologic Type (WHO Classification):
  (_) Invasive carcinoma of no special type (ductal)
  (_) Invasive lobular carcinoma
  (_) Invasive carcinoma with mixed features
  (_) Mucinous carcinoma
  (_) Tubular carcinoma
  (_) Invasive micropapillary carcinoma
  (_) Invasive papillary carcinoma
  (_) Invasive cribriform carcinoma
  (_) Metaplastic carcinoma, specify: __________________________
  (_) Other: ___________________________________________________

HISTOLOGIC GRADE (Nottingham)
───────────────────────────────────────────────────────────────
*Glandular/Tubular Differentiation:
  (_) Score 1 (>75% tubule formation)
  (_) Score 2 (10-75% tubule formation)
  (_) Score 3 (<10% tubule formation)

*Nuclear Pleomorphism:
  (_) Score 1 (small, uniform nuclei)
  (_) Score 2 (moderate variation)
  (_) Score 3 (marked variation)

*Mitotic Count (per 10 HPF):
  (_) Score 1 (≤7 mitoses)
  (_) Score 2 (8-14 mitoses)
  (_) Score 3 (≥15 mitoses)

*Overall Grade:
  (_) Grade 1 (score 3-5)
  (_) Grade 2 (score 6-7)
  (_) Grade 3 (score 8-9)

MARGINS
───────────────────────────────────────────────────────────────
*Margin Status (Invasive Carcinoma):
  (_) All margins negative
  (_) Margin(s) positive
  (_) Cannot be assessed

+If positive, specify margin(s): ________________________________

*Distance to Closest Margin:
  Distance: ___ mm
  Closest margin: ______________________________________________

*Margin Status (DCIS):
  (_) All margins negative
  (_) Margin(s) positive
  (_) Cannot be assessed
  (_) No DCIS present

LYMPHOVASCULAR INVASION
───────────────────────────────────────────────────────────────
*Lymphovascular Invasion:
  (_) Not identified
  (_) Present
  (_) Cannot be determined

PERINEURAL INVASION
───────────────────────────────────────────────────────────────
°Perineural Invasion:
  (_) Not identified
  (_) Present
  (_) Cannot be determined

ASSOCIATED FINDINGS
───────────────────────────────────────────────────────────────
*DCIS Component:
  (_) Not identified
  (_) Present
    Extent: (_) Minimal  (_) Moderate  (_) Extensive
    Nuclear grade: (_) Low  (_) Intermediate  (_) High
    Architecture: [ ] Solid  [ ] Cribriform  [ ] Papillary  [ ] Micropapillary  [ ] Comedo
    Necrosis: (_) Not identified  (_) Present

°Lobular Carcinoma In Situ (LCIS):
  (_) Not identified
  (_) Present

LYMPH NODES
───────────────────────────────────────────────────────────────
*Lymph Node Status:
  (_) No lymph nodes submitted
  (_) Lymph nodes submitted

+If submitted:
  *Number of Sentinel Nodes Examined: ___
  *Number of Sentinel Nodes with Macrometastases (>2mm): ___
  *Number of Sentinel Nodes with Micrometastases (0.2-2mm): ___
  *Number of Sentinel Nodes with Isolated Tumor Cells (≤0.2mm): ___

  *Number of Non-Sentinel Nodes Examined: ___
  *Number of Non-Sentinel Nodes Positive: ___

  *Total Number of Nodes Examined: ___
  *Total Number of Nodes Positive: ___

+Extranodal Extension:
  (_) Not identified
  (_) Present

PATHOLOGIC STAGING (AJCC 8th Edition)
───────────────────────────────────────────────────────────────
*Primary Tumor (pT):
  (_) pTX   (_) pT0   (_) pTis  (_) pT1mi  (_) pT1a
  (_) pT1b  (_) pT1c  (_) pT2   (_) pT3    (_) pT4a
  (_) pT4b  (_) pT4c  (_) pT4d

*Regional Lymph Nodes (pN):
  (_) pNX  (_) pN0  (_) pN0(i+)  (_) pN1mi  (_) pN1a
  (_) pN1b (_) pN1c (_) pN2a     (_) pN2b   (_) pN3a
  (_) pN3b (_) pN3c

+Distant Metastasis (pM):
  (_) Not applicable
  (_) pM1, specify site: _______________________________________

*AJCC Stage Group: ___________

BIOMARKERS (Report Separately or Below)
───────────────────────────────────────────────────────────────
*Estrogen Receptor (ER):
  (_) Positive (≥1% nuclear staining)
     Percentage positive: ___%
     Intensity: (_) Weak  (_) Moderate  (_) Strong
  (_) Negative (<1% nuclear staining)
  (_) Cannot be determined

*Progesterone Receptor (PR):
  (_) Positive (≥1% nuclear staining)
     Percentage positive: ___%
     Intensity: (_) Weak  (_) Moderate  (_) Strong
  (_) Negative (<1% nuclear staining)
  (_) Cannot be determined

*HER2 Status (IHC):
  (_) 0 (Negative)
  (_) 1+ (Negative)
  (_) 2+ (Equivocal) - FISH required
  (_) 3+ (Positive)
  (_) Cannot be determined

+HER2 FISH (if IHC 2+):
  HER2/CEP17 ratio: ___
  Average HER2 signals per cell: ___
  Interpretation: (_) Negative  (_) Positive  (_) Equivocal

*Ki-67 Proliferation Index: ___%

ADDITIONAL FINDINGS
───────────────────────────────────────────────────────────────
°Additional findings: __________________________________________
____________________________________________________________
____________________________________________________________

COMMENT
───────────────────────────────────────────────────────────────
____________________________________________________________
____________________________________________________________

───────────────────────────────────────────────────────────────
Pathologist: _________________________  Date: ________________
```

---

## Colorectal Carcinoma Template

### Colectomy / Anterior Resection

```
═══════════════════════════════════════════════════════════════
COLON AND RECTUM - ADENOCARCINOMA
Synoptic Report Template (CAP Protocol)
═══════════════════════════════════════════════════════════════

CLINICAL INFORMATION
───────────────────────────────────────────────────────────────
Clinical History: _______________________________________________
Neoadjuvant Therapy: (_) No  (_) Yes, specify: _________________

SPECIMEN
───────────────────────────────────────────────────────────────
*Procedure:
  (_) Right hemicolectomy
  (_) Transverse colectomy
  (_) Left hemicolectomy
  (_) Sigmoid colectomy
  (_) Low anterior resection
  (_) Abdominoperineal resection
  (_) Total colectomy
  (_) Total proctocolectomy
  (_) Segmental resection, specify: ____________________________
  (_) Other: ___________________________________________________

Specimen Length: ___ cm

TUMOR
───────────────────────────────────────────────────────────────
*Tumor Site:
  (_) Cecum
  (_) Ascending colon
  (_) Hepatic flexure
  (_) Transverse colon
  (_) Splenic flexure
  (_) Descending colon
  (_) Sigmoid colon
  (_) Rectosigmoid junction
  (_) Rectum
  (_) Other: ___________________________________________________

*Tumor Size:
  Greatest dimension: ___ cm
  Additional dimensions: ___ x ___ cm

*Tumor Configuration:
  (_) Polypoid/Fungating
  (_) Ulcerating
  (_) Annular/Constricting
  (_) Infiltrating
  (_) Other: ___________________________________________________

HISTOLOGIC TYPE
───────────────────────────────────────────────────────────────
*Histologic Type (WHO Classification):
  (_) Adenocarcinoma, NOS
  (_) Mucinous adenocarcinoma (>50% mucinous)
  (_) Signet ring cell carcinoma (>50% signet ring)
  (_) Medullary carcinoma
  (_) Micropapillary carcinoma
  (_) Serrated adenocarcinoma
  (_) Adenosquamous carcinoma
  (_) Undifferentiated carcinoma
  (_) Other: ___________________________________________________

*Histologic Grade:
  (_) G1: Well differentiated
  (_) G2: Moderately differentiated
  (_) G3: Poorly differentiated
  (_) G4: Undifferentiated
  (_) GX: Cannot be assessed

TUMOR EXTENSION
───────────────────────────────────────────────────────────────
*Depth of Invasion:
  (_) Lamina propria
  (_) Muscularis mucosae
  (_) Submucosa
  (_) Muscularis propria
  (_) Through muscularis propria into pericolorectal tissues
  (_) Penetrates to surface of visceral peritoneum (serosa)
  (_) Directly invades adjacent organs/structures
       Specify: ________________________________________________

*Tumor Perforation:
  (_) Not identified
  (_) Present

MARGINS
───────────────────────────────────────────────────────────────
*Proximal Margin:
  (_) Uninvolved by invasive carcinoma
      Distance: ___ cm
  (_) Involved by invasive carcinoma
  (_) Cannot be assessed

*Distal Margin:
  (_) Uninvolved by invasive carcinoma
      Distance: ___ cm
  (_) Involved by invasive carcinoma
  (_) Cannot be assessed

*Circumferential (Radial) Margin:
  (_) Uninvolved by invasive carcinoma
      Distance: ___ mm
  (_) Involved by invasive carcinoma
  (_) Cannot be assessed
  (_) Not applicable

+Mesorectal Excision Quality (Rectal specimens):
  (_) Complete (intact mesorectum)
  (_) Nearly complete (minor irregularities)
  (_) Incomplete (defects to muscularis propria)
  (_) Cannot be assessed

LYMPHOVASCULAR INVASION
───────────────────────────────────────────────────────────────
*Lymphatic (Small Vessel) Invasion:
  (_) Not identified
  (_) Present
  (_) Cannot be determined

*Venous (Large Vessel) Invasion:
  (_) Not identified
  (_) Present (intramural)
  (_) Present (extramural)
  (_) Cannot be determined

PERINEURAL INVASION
───────────────────────────────────────────────────────────────
*Perineural Invasion:
  (_) Not identified
  (_) Present
  (_) Cannot be determined

TUMOR DEPOSITS
───────────────────────────────────────────────────────────────
*Tumor Deposits (discontinuous extramural extension):
  (_) Not identified
  (_) Present
      Number: ___

LYMPH NODES
───────────────────────────────────────────────────────────────
*Number of Lymph Nodes Examined: ___

*Number of Lymph Nodes Positive: ___

+Extranodal Tumor Extension:
  (_) Not identified
  (_) Present

TREATMENT EFFECT (if neoadjuvant therapy)
───────────────────────────────────────────────────────────────
+Tumor Regression Grade:
  (_) Grade 0: Complete response (no viable tumor)
  (_) Grade 1: Near complete (single cells or rare small groups)
  (_) Grade 2: Partial response (residual cancer with regression)
  (_) Grade 3: Poor/No response (minimal or no regression)
  (_) Cannot be determined

PATHOLOGIC STAGING (AJCC 8th Edition)
───────────────────────────────────────────────────────────────
*Primary Tumor (pT):
  (_) pTX   (_) pT0   (_) pTis  (_) pT1   (_) pT2
  (_) pT3   (_) pT4a  (_) pT4b

*Regional Lymph Nodes (pN):
  (_) pNX   (_) pN0   (_) pN1a  (_) pN1b  (_) pN1c
  (_) pN2a  (_) pN2b

+Distant Metastasis (pM):
  (_) Not applicable
  (_) pM1a (one site)
  (_) pM1b (two or more sites)
  (_) pM1c (peritoneum)
  Site(s): _____________________________________________________

*AJCC Stage Group: ___________

ADDITIONAL FINDINGS
───────────────────────────────────────────────────────────────
°Polyps:
  (_) None identified
  (_) Present
      Type(s): _________________________________________________
      Number: ___

°Other findings: _______________________________________________

BIOMARKERS
───────────────────────────────────────────────────────────────
*Mismatch Repair (MMR) Status:
  MLH1: (_) Intact  (_) Loss of expression  (_) Cannot be determined
  PMS2: (_) Intact  (_) Loss of expression  (_) Cannot be determined
  MSH2: (_) Intact  (_) Loss of expression  (_) Cannot be determined
  MSH6: (_) Intact  (_) Loss of expression  (_) Cannot be determined

  MMR Status: (_) Proficient (pMMR)  (_) Deficient (dMMR)

+If MLH1/PMS2 loss:
  MLH1 Promoter Methylation: (_) Present  (_) Absent  (_) Not tested

°KRAS/NRAS/BRAF (if applicable): _______________________________

COMMENT
───────────────────────────────────────────────────────────────
____________________________________________________________

───────────────────────────────────────────────────────────────
Pathologist: _________________________  Date: ________________
```

---

## Exocrine Pancreas Carcinoma Template

### Pancreaticoduodenectomy (Whipple)

```
═══════════════════════════════════════════════════════════════
PANCREAS - EXOCRINE CARCINOMA
Synoptic Report Template (CAP Protocol)
═══════════════════════════════════════════════════════════════

CLINICAL INFORMATION
───────────────────────────────────────────────────────────────
Clinical History: _______________________________________________
Neoadjuvant Therapy: (_) No  (_) Yes, specify: _________________

SPECIMEN
───────────────────────────────────────────────────────────────
*Procedure:
  (_) Pancreaticoduodenectomy (Whipple)
  (_) Pylorus-preserving pancreaticoduodenectomy
  (_) Distal pancreatectomy
  (_) Total pancreatectomy
  (_) Other: ___________________________________________________

Specimen Components:
  [ ] Pancreas (dimensions: ___ x ___ x ___ cm)
  [ ] Duodenum (length: ___ cm)
  [ ] Stomach/Pylorus (if present)
  [ ] Common bile duct
  [ ] Gallbladder
  [ ] Spleen (if present)

TUMOR
───────────────────────────────────────────────────────────────
*Tumor Site:
  (_) Head of pancreas
  (_) Uncinate process
  (_) Body of pancreas
  (_) Tail of pancreas
  (_) Ampulla of Vater
  (_) Distal bile duct
  (_) Other: ___________________________________________________

*Tumor Size:
  Greatest dimension: ___ cm
  Additional dimensions: ___ x ___ cm

HISTOLOGIC TYPE
───────────────────────────────────────────────────────────────
*Histologic Type (WHO Classification):
  (_) Ductal adenocarcinoma
  (_) Adenosquamous carcinoma
  (_) Colloid carcinoma (mucinous noncystic)
  (_) Hepatoid carcinoma
  (_) Medullary carcinoma
  (_) Signet ring cell carcinoma
  (_) Undifferentiated carcinoma
  (_) Undifferentiated carcinoma with osteoclast-like giant cells
  (_) Invasive carcinoma arising from IPMN
  (_) Invasive carcinoma arising from MCN
  (_) Acinar cell carcinoma
  (_) Pancreatoblastoma
  (_) Other: ___________________________________________________

*Histologic Grade:
  (_) G1: Well differentiated
  (_) G2: Moderately differentiated
  (_) G3: Poorly differentiated
  (_) GX: Cannot be assessed

TUMOR EXTENSION
───────────────────────────────────────────────────────────────
*Extent of Invasion:
  [ ] Confined to pancreas
  [ ] Extends beyond pancreas
  [ ] Duodenum
  [ ] Ampulla
  [ ] Common bile duct
  [ ] Peripancreatic soft tissue
  [ ] Stomach
  [ ] Spleen
  [ ] Colon
  [ ] Adrenal gland
  [ ] Other: ___________________________________________________

*Major Vessel Involvement:
  (_) Not identified
  (_) Present
      [ ] Superior mesenteric artery
      [ ] Celiac axis
      [ ] Common hepatic artery
      [ ] Superior mesenteric vein
      [ ] Portal vein

MARGINS
───────────────────────────────────────────────────────────────
*Pancreatic Neck (Transection) Margin:
  (_) Uninvolved
  (_) Involved by invasive carcinoma
  (_) Cannot be assessed

*Bile Duct Margin:
  (_) Uninvolved
  (_) Involved by invasive carcinoma
  (_) Cannot be assessed

*Superior Mesenteric Artery (Uncinate) Margin:
  (_) Uninvolved
      Distance to margin: ___ mm
  (_) Involved by invasive carcinoma
  (_) Cannot be assessed

*Posterior (Retroperitoneal) Margin:
  (_) Uninvolved
      Distance to margin: ___ mm
  (_) Involved by invasive carcinoma
  (_) Cannot be assessed

*Proximal (Gastric/Duodenal) Margin:
  (_) Uninvolved
  (_) Involved
  (_) Cannot be assessed

*Distal (Duodenal/Jejunal) Margin:
  (_) Uninvolved
  (_) Involved
  (_) Cannot be assessed

LYMPHOVASCULAR INVASION
───────────────────────────────────────────────────────────────
*Lymphovascular Invasion:
  (_) Not identified
  (_) Present
  (_) Cannot be determined

PERINEURAL INVASION
───────────────────────────────────────────────────────────────
*Perineural Invasion:
  (_) Not identified
  (_) Present
  (_) Cannot be determined

LYMPH NODES
───────────────────────────────────────────────────────────────
*Number of Lymph Nodes Examined: ___

*Number of Lymph Nodes Positive: ___

TREATMENT EFFECT (if neoadjuvant therapy)
───────────────────────────────────────────────────────────────
+Tumor Regression Grade:
  (_) Grade 0: Complete response (no viable tumor)
  (_) Grade 1: Near complete (single cells or rare small groups)
  (_) Grade 2: Partial response (residual cancer with regression)
  (_) Grade 3: Poor/No response (minimal or no regression)

PATHOLOGIC STAGING (AJCC 8th Edition)
───────────────────────────────────────────────────────────────
*Primary Tumor (pT):
  (_) pTX   (_) pT0   (_) pTis  (_) pT1a  (_) pT1b
  (_) pT1c  (_) pT2   (_) pT3   (_) pT4

*Regional Lymph Nodes (pN):
  (_) pNX   (_) pN0   (_) pN1   (_) pN2

+Distant Metastasis (pM):
  (_) Not applicable
  (_) pM1, specify site: _______________________________________

*AJCC Stage Group: ___________

ADDITIONAL FINDINGS
───────────────────────────────────────────────────────────────
°Pancreatic Intraepithelial Neoplasia (PanIN):
  (_) Not identified
  (_) Present, grade: __________________________________________

°IPMN/MCN:
  (_) Not identified
  (_) Present, specify: ________________________________________

°Chronic pancreatitis:
  (_) Not identified
  (_) Present

°Other: ________________________________________________________

COMMENT
───────────────────────────────────────────────────────────────
____________________________________________________________

───────────────────────────────────────────────────────────────
Pathologist: _________________________  Date: ________________
```

---

## Gastric Carcinoma Template

### Gastrectomy

```
═══════════════════════════════════════════════════════════════
STOMACH - ADENOCARCINOMA
Synoptic Report Template (CAP Protocol)
═══════════════════════════════════════════════════════════════

CLINICAL INFORMATION
───────────────────────────────────────────────────────────────
Clinical History: _______________________________________________
Neoadjuvant Therapy: (_) No  (_) Yes, specify: _________________

SPECIMEN
───────────────────────────────────────────────────────────────
*Procedure:
  (_) Partial gastrectomy (distal/subtotal)
  (_) Partial gastrectomy (proximal)
  (_) Total gastrectomy
  (_) Local excision
  (_) Other: ___________________________________________________

Specimen Dimensions:
  Greater curvature length: ___ cm
  Lesser curvature length: ___ cm

TUMOR
───────────────────────────────────────────────────────────────
*Tumor Site:
  [ ] Cardia
  [ ] Fundus
  [ ] Body (corpus)
  [ ] Antrum
  [ ] Pylorus
  [ ] Lesser curvature
  [ ] Greater curvature
  [ ] Anterior wall
  [ ] Posterior wall

*Distance from Esophagogastric Junction (EGJ): ___ cm

*Tumor Size:
  Greatest dimension: ___ cm
  Additional dimensions: ___ x ___ cm

*Tumor Configuration (Borrmann):
  (_) Type I - Polypoid/fungating
  (_) Type II - Ulcerated with raised borders
  (_) Type III - Ulcerated with infiltrating borders
  (_) Type IV - Diffusely infiltrating (linitis plastica)
  (_) Type V - Unclassifiable

HISTOLOGIC TYPE
───────────────────────────────────────────────────────────────
*Histologic Type (WHO Classification):
  (_) Tubular adenocarcinoma
  (_) Papillary adenocarcinoma
  (_) Mucinous adenocarcinoma (>50% mucinous)
  (_) Poorly cohesive carcinoma (including signet ring cell)
  (_) Mixed adenocarcinoma
  (_) Adenosquamous carcinoma
  (_) Squamous cell carcinoma
  (_) Hepatoid adenocarcinoma
  (_) Carcinoma with lymphoid stroma
  (_) Micropapillary adenocarcinoma
  (_) Undifferentiated carcinoma
  (_) Other: ___________________________________________________

*Histologic Grade:
  (_) G1: Well differentiated (>95% glands)
  (_) G2: Moderately differentiated (50-95% glands)
  (_) G3: Poorly differentiated (<50% glands)
  (_) GX: Cannot be assessed

°Laurén Classification:
  (_) Intestinal type
  (_) Diffuse type
  (_) Mixed type
  (_) Indeterminate

TUMOR EXTENSION
───────────────────────────────────────────────────────────────
*Depth of Invasion:
  (_) Lamina propria or muscularis mucosae (pT1a)
  (_) Submucosa (pT1b)
  (_) Muscularis propria (pT2)
  (_) Subserosa without serosal penetration (pT3)
  (_) Penetrates serosa/visceral peritoneum (pT4a)
  (_) Invades adjacent structures (pT4b)
       Specify: ________________________________________________

MARGINS
───────────────────────────────────────────────────────────────
*Proximal Margin:
  (_) Uninvolved
      Distance: ___ cm
  (_) Involved by invasive carcinoma
  (_) Cannot be assessed

*Distal Margin:
  (_) Uninvolved
      Distance: ___ cm
  (_) Involved by invasive carcinoma
  (_) Cannot be assessed

*Radial (Omental) Margin:
  (_) Uninvolved
  (_) Involved
  (_) Cannot be assessed
  (_) Not applicable

LYMPHOVASCULAR INVASION
───────────────────────────────────────────────────────────────
*Lymphovascular Invasion:
  (_) Not identified
  (_) Present
  (_) Cannot be determined

*Venous Invasion:
  (_) Not identified
  (_) Present
  (_) Cannot be determined

PERINEURAL INVASION
───────────────────────────────────────────────────────────────
*Perineural Invasion:
  (_) Not identified
  (_) Present
  (_) Cannot be determined

LYMPH NODES
───────────────────────────────────────────────────────────────
*Number of Lymph Nodes Examined: ___

*Number of Lymph Nodes Positive: ___

+Extranodal Extension:
  (_) Not identified
  (_) Present

°Lymph Node Stations Examined (if specified):
  ____________________________________________________________

TREATMENT EFFECT (if neoadjuvant therapy)
───────────────────────────────────────────────────────────────
+Tumor Regression Grade:
  (_) Grade 0: Complete response (no viable tumor)
  (_) Grade 1: Near complete (single cells or rare small groups)
  (_) Grade 2: Partial response (residual cancer with regression)
  (_) Grade 3: Poor/No response (minimal or no regression)

PATHOLOGIC STAGING (AJCC 8th Edition)
───────────────────────────────────────────────────────────────
*Primary Tumor (pT):
  (_) pTX   (_) pT0   (_) pTis  (_) pT1a  (_) pT1b
  (_) pT2   (_) pT3   (_) pT4a  (_) pT4b

*Regional Lymph Nodes (pN):
  (_) pNX   (_) pN0   (_) pN1   (_) pN2   (_) pN3a  (_) pN3b

+Distant Metastasis (pM):
  (_) Not applicable
  (_) pM1, specify site: _______________________________________

*AJCC Stage Group: ___________

BIOMARKERS
───────────────────────────────────────────────────────────────
*HER2 Status (for advanced/metastatic disease):
  IHC Score: (_) 0  (_) 1+  (_) 2+  (_) 3+
  
  +FISH (if IHC 2+):
    HER2/CEP17 ratio: ___
    Interpretation: (_) Negative  (_) Positive

*Mismatch Repair (MMR) / Microsatellite Instability (MSI):
  MLH1: (_) Intact  (_) Loss  (_) Not tested
  PMS2: (_) Intact  (_) Loss  (_) Not tested
  MSH2: (_) Intact  (_) Loss  (_) Not tested
  MSH6: (_) Intact  (_) Loss  (_) Not tested
  
  Status: (_) pMMR/MSS  (_) dMMR/MSI-H

°PD-L1 (CPS Score): ___

ADDITIONAL FINDINGS
───────────────────────────────────────────────────────────────
°Helicobacter pylori:
  (_) Not identified
  (_) Present

°Intestinal metaplasia:
  (_) Not identified
  (_) Present

°Chronic gastritis:
  (_) Not identified
  (_) Present

°Other: ________________________________________________________

COMMENT
───────────────────────────────────────────────────────────────
____________________________________________________________

───────────────────────────────────────────────────────────────
Pathologist: _________________________  Date: ________________
```

---

## Template Usage Instructions

### For Claude

When generating a template:
1. Identify the tumor type from user request
2. Select appropriate template from above
3. If specimen type specified, use that variant
4. Optionally pre-fill any values provided by user
5. Add header with date and institution if requested

### Pre-filling Values

If user provides some information, fill in those fields:

**User says:** "Generate a breast template for a 2.3cm Grade 2 IDC"

**Pre-fill:**
- Histologic Type: Invasive carcinoma of no special type (ductal) ✓
- Greatest dimension: 2.3 cm
- Overall Grade: Grade 2 ✓

### Language Adaptation

For Turkish reports, translate field labels:
- "Tumor Size" → "Tümör Boyutu"
- "Histologic Type" → "Histolojik Tip"
- "Margin Status" → "Cerrahi Sınır Durumu"

Provide both English and Turkish versions if requested.

---

## Quick Reference - Required Elements by Tumor

### Breast (Minimum Required)
- Procedure, Tumor size, Histologic type, Grade, Margins, LVI, Nodes, pTNM, ER, PR, HER2

### Colorectal (Minimum Required)
- Procedure, Site, Tumor size, Histologic type, Grade, Depth, Margins, LVI, PNI, Nodes, pTNM, MMR

### Pancreas (Minimum Required)
- Procedure, Site, Tumor size, Histologic type, Grade, Extension, All margins, LVI, PNI, Nodes, pTNM

### Gastric (Minimum Required)
- Procedure, Site, Tumor size, Histologic type, Grade, Depth, Margins, LVI, PNI, Nodes, pTNM, HER2, MMR
