# Quick Reference Card

## Trigger Phrases

| Action | English | Turkish |
|--------|---------|---------|
| **Compliance Check** | "Check this report for CAP compliance" | "Bu raporu CAP uyumluluğu için kontrol et" |
| **Synoptic Template** | "Generate breast synoptic template" | "Meme sinoptik şablonu oluştur" |
| **Tumor Board Summary** | "Generate tumor board summary" | "Tümör kurulu özeti oluştur" |
| **Free-text → Synoptic** | "Convert to synoptic format" | "Sinoptik formata dönüştür" |
| **Auto-fill** | "Suggest pTNM staging" | "pTNM evrelemesi öner" |
| **Amendment** | "Generate amendment for this" | "Düzeltme oluştur" |
| **SNOMED Coding** | "What's the SNOMED code for..." | "... için SNOMED kodu nedir?" |
| **TNM Calculator** | "Calculate stage for pT2 N1 M0" | "pT2 N1 M0 için evreyi hesapla" |

---

## Supported Tumor Types

| Tumor | Diagnosis | Macroscopy | Templates |
|-------|-----------|------------|-----------|
| Breast invasive | ✅ | ✅ | EN + TR |
| Colorectal | ✅ | ✅ | EN + TR |
| Pancreas | ✅ | ✅ | EN + TR |
| Gastric | ✅ | ✅ | EN + TR |

---

## Processing Modes

| Mode | Output | Use Case |
|------|--------|----------|
| `compliance` | QA report with score | Check existing reports |
| `synoptic` | Structured CAP format | Convert narrative → structured |
| `summary` | 3-5 line MDT summary | Tumor board prep |
| `autofill` | Suggested values | Fill missing staging |
| `amendment` | Correction text | Fix report errors |

---

## Reference File Locations

```
references/
├── diagnosis/           # CAP/ICCR required elements
│   ├── breast_invasive_carcinoma.md
│   ├── colorectal_resection.md
│   ├── exocrine_pancreas.md
│   └── gastric_carcinoma.md
├── macroscopy/          # AAPA gross description
│   ├── MACROSCOPY_COMMON.md
│   ├── breast_macroscopy.md
│   ├── colorectal_macroscopy.md
│   ├── pancreas_macroscopy.md
│   └── gastric_macroscopy.md
├── staging/             # TNM calculator
│   └── tnm_stage_calculator.md
├── templates/           # Synoptic templates
│   ├── synoptic_templates.md
│   └── synoptic_templates_tr.md
├── coding/              # SNOMED CT / ICD-O-3
│   └── snomed_ct_codes.md
├── summaries/           # Tumor board
│   └── tumor_board_summary.md
├── converters/          # Format conversion
│   └── freetext_to_synoptic.md
├── autofill/            # Value suggestions
│   └── autofill_suggestions.md
├── amendments/          # Amendment templates
│   └── amendment_generator.md
└── biomarkers/          # Biomarker index
    └── BIOMARKERS_INDEX.md
```

---

## Severity Levels

| Level | Elements | Score Impact |
|-------|----------|--------------|
| 🔴 **CRITICAL** | pT, pN, margins, grade, receptors | -15 each |
| 🟠 **MAJOR** | LVI, PNI, tumor size, node counts | -5 each |
| 🟡 **MINOR** | Focality, gross details | -2 each |

**Score:** `100 - (Critical × 15) - (Major × 5) - (Minor × 2)`

| Score | Status |
|-------|--------|
| 90-100 | ✅ COMPLIANT |
| 70-89 | 🟡 INCOMPLETE - MINOR |
| 50-69 | 🟠 INCOMPLETE - MAJOR |
| <50 | 🔴 INCOMPLETE - CRITICAL |

---

## Cross-Validation Rules

| Check | Rule | Severity |
|-------|------|----------|
| pT vs Size | Must match tumor dimensions | Error |
| pN vs Nodes | Must match positive count | Error |
| Margin vs R | R0 requires negative margins | Error |
| Node Count | Minimum nodes for staging | Warning |

---

## Usage Quick Reference

| Method | API Key? | Command |
|--------|----------|---------|
| Claude.ai | ❌ No | Paste report + trigger phrase |
| Claude CLI | ❌ No | `claude "Check this report..." < report.txt` |
| Batch script | ✅ Yes | `python scripts/batch_checker.py /in /out` |
| Watch folder | ✅ Yes | `python scripts/watch_folder.py /dir` |

---

## Output Formats

**Compliance Report:**
```
SCORE: 85/100
STATUS: INCOMPLETE - MINOR
🔴 Critical: 0 | 🟠 Major: 1 | 🟡 Minor: 3
```

**Tumor Board Summary:**
```
58F with invasive ductal carcinoma of the left breast.
Lumpectomy: 2.3 cm IDC, Grade 2, pT2 N1a M0 (Stage IIB).
Margins: Negative. LVI: Present. Nodes: 2/15 positive.
ER 95%/PR 80%/HER2 neg/Ki-67 25%.
```

**Amendment:**
```
AMENDED REPORT
Original: pT3  →  Corrected: pT2
Rationale: Tumor 2.8cm confined to pancreas = pT2
```
