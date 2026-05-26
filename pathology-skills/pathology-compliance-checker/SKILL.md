---
name: pathology-compliance-checker
description: Validates surgical pathology cancer reports against CAP (College of American Pathologists) and ICCR (International Collaboration on Cancer Reporting) guidelines with severity-based compliance scoring (0-100) and automatic pT/pN/margin cross-validation. Use whenever the user pastes or uploads a pathology report (.pdf, .docx, .txt) and asks to "check compliance", "validate against CAP", "score this report", "audit this synoptic", "find missing elements", or "verify pT/pN consistency". Supports breast, colorectal, pancreas, and gastric carcinoma in English and Turkish.
license: MIT
metadata:
  version: 1.3.0
  author: Serdar Balci
---

# Compliance Checker

Validate pathology reports against CAP/ICCR protocols with comprehensive scoring and cross-validation.

## When to Use This Skill

Use this skill for:
- Quality assurance of pathology reports
- Department compliance monitoring
- CAP accreditation preparation
- Report validation before sign-out
- Trainee report review

## Supported Tumor Types

- Breast invasive carcinoma (CAP Breast.Invasive, ICCR Invasive Carcinoma of the Breast)
- Colorectal resection (CAP ColoRectal, ICCR Colorectal Cancer)
- Exocrine pancreas carcinoma (CAP Panc.Exo, ICCR Carcinoma of the Exocrine Pancreas)
- Gastric carcinoma (CAP Stomach, ICCR Gastric Carcinoma)

## Key Features

1. **Element Completeness Check**: Validates all required, conditional, and recommended elements
2. **Severity-Based Scoring**: Critical (-15), Major (-5), Minor (-2) point deductions
3. **Cross-Validation**: pT vs tumor size, pN vs node count, stage group consistency
4. **Threshold Grading**: 90-100 (Compliant), 70-89 (Minor), 50-69 (Major), <50 (Critical)

## Reference Files

Reference on-demand (DO NOT load at startup):
- Tumor-specific: `references/diagnosis/{tumor}_*.md`
- Tumor-specific macroscopy: `references/macroscopy/{tumor}_macroscopy.md`
- Cross-validation: `../../shared-references/staging/tnm_stage_calculator.md`
- Common checks: `../../shared-references/common/cross_validation.md`

## Usage Examples

```bash
# Check report compliance
claude "Check this report using compliance-checker" < report.txt

# QA batch of reports
claude "Validate compliance using compliance-checker" < batch_report.txt
```

## Processing Instructions

1. **Auto-detect tumor type** from report content
2. **Load appropriate protocol** (CAP/ICCR for that tumor type)
3. **Check element presence**: Required, conditional, recommended
4. **Calculate score** using severity weights
5. **Cross-validate**: pT/pN/stage consistency
6. **Output**: Score, missing elements, inconsistencies, recommendations

## Compliance Scoring Formula

Starting score: 100

- **Critical elements missing/incorrect**: -15 each (tumor size, grade, margins, nodes, biomarkers)
- **Major elements missing/incorrect**: -5 each (LVI, PNI, special features)
- **Minor elements missing/incorrect**: -2 each (optional fields, tumor location)

## Language Support

Auto-detects English or Turkish from report content.

---

**Note**: Minimal skill definition. References loaded on-demand during processing only.
