---
name: pathology-coder
description: Suggests SNOMED CT and ICD-O-3 morphology/topography codes for pathology diagnoses, procedures, and biomarkers, with hierarchical parent/child relationships and synonyms. Use when the user asks "SNOMED code for [diagnosis]", "ICD-O-3 code for [tumor type]", "what's the code for invasive ductal carcinoma", "code this diagnosis", "morphology code for", or any pathology-coding lookup. Supports common cancer diagnoses (breast, colorectal, pancreas, gastric, prostate, lung, lymphoma, GIST) and standard pathology procedures.
license: MIT
metadata:
  version: 1.3.0
  author: Serdar Balci
---

# Pathology Coder

SNOMED CT and ICD-O-3 coding suggestions for pathology reports with clinical context.

## When to Use This Skill

Use this skill for:
- LIS integration and coding
- Tumor registry reporting
- Billing support
- Standardizing terminology
- Teaching pathology coding

## Supported Code Systems

- **SNOMED CT**: Morphology, topography, procedures, qualifiers
- **ICD-O-3**: Morphology codes with behavior, topography codes

## Key Features

1. **Diagnosis Coding**: Tumor type, grade, behavior codes
2. **Procedure Coding**: Specimen types, special stains, IHC
3. **Biomarker Coding**: ER/PR/HER2/MSI/MMR codes
4. **Hierarchical Relationships**: Parent concepts, synonyms
5. **Multi-code Support**: Combined diagnoses and qualifiers

## Reference Files

Reference on-demand (DO NOT load at startup):
- Code tables: `../../shared-references/coding/snomed_ct_codes.md`

## Usage Examples

```bash
# Code diagnosis
claude "SNOMED code for invasive ductal carcinoma grade 2 using pathology-coder"

# Code procedure
claude "What is the code for HER2 immunohistochemistry using pathology-coder"

# Multiple codes
claude "Code breast lumpectomy with IDC and DCIS using pathology-coder"
```

## Processing Instructions

1. **Parse diagnosis/procedure** from user input
2. **Load code table** from shared-references
3. **Look up SNOMED CT code** and ICD-O-3 if applicable
4. **Provide hierarchical context**: Parent concepts, synonyms
5. **Output**: Code(s) with descriptions and relationships

## Common Tumor Type Codes

Loaded on-demand from reference file when needed:
- Breast carcinoma codes
- Colorectal carcinoma codes
- Pancreas carcinoma codes
- Gastric carcinoma codes

## Output Format

For each code suggestion:
- **SNOMED CT**: [Code] | [Preferred term] | [Hierarchy]
- **ICD-O-3**: [Morphology/Behavior] | [Topography] | [Description]

---

**Note**: Minimal skill definition. Code tables loaded on-demand during processing only.
