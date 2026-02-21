---
name: tnm-stage-calculator
description: Fast TNM stage group calculation from pT, pN, pM categories using AJCC 8th edition criteria. Supports breast, colorectal, pancreas, and gastric carcinoma. Validates staging consistency.
---

# TNM Stage Calculator

Quick and accurate TNM stage group calculation based on AJCC 8th edition staging manual.

## When to Use This Skill

Use this skill for:
- Quick stage group lookup from pT/pN/pM
- Teaching TNM staging to residents
- Verifying report staging accuracy
- Calculating stage from pathologic findings
- Tumor board preparation

## Supported Tumor Types

- Breast invasive carcinoma (AJCC 8th pathologic stage groups)
- Colorectal carcinoma (AJCC 8th pathologic stage groups)
- Exocrine pancreas carcinoma (AJCC 8th pathologic stage groups)
- Gastric carcinoma (AJCC 8th pathologic stage groups)

## Key Features

1. **Stage Group Calculation**: Input pT/pN/pM → Output stage group (0, I, IIA, IIB, IIIA, etc.)
2. **Validation**: Checks if pT/pN/pM combination is valid
3. **Prognostic Info**: Provides stage group meaning
4. **Fast Lookup**: Lightweight skill optimized for speed

## Reference Files

Reference on-demand (DO NOT load at startup):
- Staging tables: `../../shared-references/staging/tnm_stage_calculator.md`

## Usage Examples

```bash
# Calculate stage
claude "What stage is pT2 N1 M0 for breast using tnm-stage-calculator"

# Quick lookup
claude "Stage pT3 N1b M0 colorectal using tnm-stage-calculator"

# Verify staging
claude "Is pT1c N0 M0 stage IA for breast using tnm-stage-calculator"
```

## Processing Instructions

1. **Parse input**: Extract pT, pN, pM categories and tumor type
2. **Load staging table** for specific tumor type
3. **Look up stage group** from pT/pN/pM combination
4. **Validate**: Check if combination exists in AJCC 8th
5. **Output**: Stage group with brief prognostic interpretation

## Important Notes

- Uses **pathologic stage groups** (pTNM), not clinical stage groups (cTNM)
- Based on **AJCC 8th edition** (2017)
- For breast, does not include anatomic stage groups (uses prognostic stage groups where applicable)
- For colorectal, includes post-neoadjuvant treatment modifications (ypTNM)

## Input Format Examples

- "pT2 N1a M0 for breast"
- "What is the stage for pT3 N1b M0 colorectal?"
- "Calculate stage: pT2 N1 M0 pancreas"
- "Stage group for gastric pT3 N2 M0"

---

**Note**: Lightweight skill. Staging table loaded on-demand during processing only.
