---
name: template-generator
description: Generates blank or pre-filled CAP-compliant synoptic pathology report templates with all required elements. Supports breast, colorectal, pancreas, and gastric carcinoma in English and Turkish.
---

# Template Generator

Generate standardized CAP synoptic report templates - blank or pre-filled with known values.

## When to Use This Skill

Use this skill for:
- Creating new synoptic reports
- Standardizing department templates
- Training residents on synoptic reporting
- Pre-filling templates for dictation
- Converting free-text to structured format

## Supported Templates

- **Breast**: Mastectomy, lumpectomy, excision, sentinel node, axillary dissection
- **Colorectal**: Colectomy, sigmoid, rectal (TME), polypectomy
- **Pancreas**: Whipple, distal pancreatectomy, total pancreatectomy
- **Gastric**: Total gastrectomy, subtotal, endoscopic resection

## Key Features

1. **Blank Templates**: All CAP required/conditional elements with [___] placeholders
2. **Pre-filled Templates**: Populate known fields, leave unknowns blank
3. **Language Options**: English or Turkish based on user request
4. **CAP Compliance**: Follows latest CAP Cancer Protocol structure

## Reference Files

Reference on-demand (DO NOT load at startup):
- Templates: `../../shared-references/templates/synoptic_templates.md` (English)
- Templates Turkish: `../../shared-references/templates/synoptic_templates_tr.md`

## Usage Examples

```bash
# Generate blank template
claude "Generate blank breast lumpectomy template using template-generator"

# Generate pre-filled template
claude "Generate breast template with 2.3cm IDC grade 2 using template-generator"

# Turkish template
claude "Meme lumpektomi şablonu oluştur using template-generator"
```

## Processing Instructions

1. **Identify specimen type** from user request
2. **Detect language** (English or Turkish)
3. **Load appropriate template** from shared-references
4. **If pre-fill requested**: Populate known values, leave rest as [___]
5. **If blank requested**: Return template with all [___] placeholders
6. **Output**: Formatted synoptic template ready for use

## Template Format

All templates include:
- **Required elements** (always present)
- **Conditional elements** (based on specimen type)
- **Recommended elements** (optional but encouraged)
- **Clear section headers** and proper formatting

---

**Note**: Minimal skill definition. Templates loaded on-demand during processing only.
