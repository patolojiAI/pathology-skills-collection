# Pathology Skills Collection

**Comprehensive clinical pathology toolkit for Claude** - 10 specialized skills for surgical pathology quality assurance, template generation, staging, coding, and clinical workflow optimization.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues](https://img.shields.io/github/issues/sbalci/pathology-skills-collection)](https://github.com/sbalci/pathology-skills-collection/issues)
[![GitHub stars](https://img.shields.io/github/stars/sbalci/pathology-skills-collection)](https://github.com/sbalci/pathology-skills-collection/stargazers)

![Skills](https://img.shields.io/badge/skills-10-blue)
![Tumor Types](https://img.shields.io/badge/tumor%20types-4-green)
![Languages](https://img.shields.io/badge/languages-EN%2FTR-orange)

---

## What This Provides

A modular collection of Claude skills for clinical pathologists and QA teams:

- ✅ **Compliance checking** against CAP and ICCR guidelines
- 📋 **Synoptic template generation** with optional pre-fill
- 🔢 **TNM staging calculation** (AJCC 8th edition)
- 🏥 **SNOMED CT / ICD-O-3 coding** suggestions
- 📊 **Tumor board summaries** for MDT meetings
- 🔄 **Free-text to synoptic conversion** for legacy reports

---

## Supported Tumor Types

- 🎀 **Breast** invasive carcinoma (CAP Breast.Invasive)
- 🔬 **Colorectal** resection (CAP ColoRectal)
- 🫁 **Pancreas** exocrine carcinoma (CAP Panc.Exo)
- 🫀 **Gastric** carcinoma (CAP Stomach)

---

## Prerequisites

**Required:** [Claude Code CLI](https://claude.ai/code)

```bash
# Verify installation
claude --version
```

**Optional** (for batch processing): Python 3.8+ with dependencies:

```bash
pip install -r requirements.txt
```

---

## Installation

### Option 1: Community Marketplace (Coming Soon - Auto-Listed After 5⭐)

Once listed on [Claude Marketplaces](https://claudemarketplaces.com/) (after getting 5+ GitHub stars):

1. Browse to https://claudemarketplaces.com/
2. Search for "pathology-skills-collection"
3. Install all 10 skills directly from the marketplace

**Note:** Automatic discovery happens within 24 hours after getting 5+ stars!

### Option 2: Quick Install (Available Now)

```bash
# Clone repository
git clone https://github.com/sbalci/pathology-skills-collection.git
cd pathology-skills-collection

# Run installer
./install.sh

# Test
claude "What stage is pT2 N0 M0 for breast using tnm-stage-calculator"
```

### Option 3: Manual Install

```bash
# Clone repository
git clone https://github.com/sbalci/pathology-skills-collection.git
cd pathology-skills-collection

# Individual skill symlinks (see install.sh for details)
mkdir -p ~/.claude/skills
# Run install.sh or create symlinks manually

# Test
claude "List available pathology skills"
```

---

## How to Use

### Single Report Analysis

```bash
# Compliance checking
claude "Check this breast report using breast-pathology-specialist" < report.txt

# TNM staging
claude "What stage is pT3 N1b M0 for colorectal using tnm-stage-calculator"

# Template generation
claude "Generate blank Whipple template using template-generator"

# Tumor board summary
claude "Create tumor board summary using tumor-board-summary" < report.txt

# SNOMED coding
claude "SNOMED code for invasive ductal carcinoma grade 2 using pathology-coder"
```

### Batch Processing Multiple Reports

**✅ RECOMMENDED: Use Claude CLI directly (no API key needed)**

```bash
# Process Excel file with 100 reports - Claude analyzes each with LLM intelligence
claude "Read reports.xlsx and use breast-pathology-specialist to analyze each report. Provide compliance scores and export results to Excel."

# Process all reports in a directory
claude "Analyze all .txt files in reports_dir/ using compliance-checker and create summary Excel."

# Use the helper script
./batch_process_cli.sh reports.xlsx colorectal-pathology-specialist results/
```

**⚠️ ALTERNATIVE: Python API script (requires ANTHROPIC_API_KEY)**

Only use this if you DON'T have Claude CLI or need programmatic integration:

```bash
# Requires: export ANTHROPIC_API_KEY="your-key-here"
pip install -r requirements.txt
python cli-tools/process_skill.py --skill breast-pathology-specialist reports.xlsx
```

**🚫 DON'T:** Ask Claude to "generate a Python script" - it will create regex-only code without LLM intelligence!

---

## Skills Directory

### Functional Skills (Single Purpose)

| Skill | Purpose | Usage |
|-------|---------|-------|
| **compliance-checker** | CAP/ICCR validation with scoring | `claude "Check report using compliance-checker" < report.txt` |
| **template-generator** | Blank or pre-filled synoptic templates | `claude "Generate breast lumpectomy template using template-generator"` |
| **tnm-stage-calculator** | AJCC 8th edition staging | `claude "Stage pT2 N1 M0 breast using tnm-stage-calculator"` |
| **pathology-coder** | SNOMED CT / ICD-O-3 codes | `claude "SNOMED code for adenocarcinoma using pathology-coder"` |
| **tumor-board-summary** | 3-5 line MDT summaries | `claude "Tumor board summary using tumor-board-summary" < report.txt` |
| **report-converter** | Free-text to synoptic conversion | `claude "Convert to synoptic using report-converter" < narrative.txt` |

### Specialist Skills (All-in-One by Tumor Type)

| Skill | Tumor Type | Usage |
|-------|------------|-------|
| **breast-pathology-specialist** | Breast carcinoma | `claude "Check breast report using breast-pathology-specialist" < report.txt` |
| **colorectal-pathology-specialist** | Colorectal carcinoma | `claude "Check colorectal report using colorectal-pathology-specialist" < report.txt` |
| **pancreas-pathology-specialist** | Pancreatic carcinoma | `claude "Check pancreas report using pancreas-pathology-specialist" < report.txt` |
| **gastric-pathology-specialist** | Gastric carcinoma | `claude "Check gastric report using gastric-pathology-specialist" < report.txt` |

---

## Documentation

- **[Getting Started Guide](docs/getting-started.md)** - Installation and setup
- **[Batch Processing Guide](docs/BATCH_PROCESSING.md)** - **NEW!** How to process multiple reports correctly
- **[Examples](docs/examples.md)** - Common use cases
- **[Multi-Format Guide](docs/MULTI_FORMAT_GUIDE.md)** - PDF, Excel, images support
- **[Skills Reference](docs/pathology-skills.md)** - Detailed skill documentation
- **[Contributing Guide](docs/CONTRIBUTING.md)** - How to contribute

---

## Project Structure

```
pathology-skills-collection/
├── pathology-skills/          # 10 individual skills
├── shared-references/         # Common guidelines (TNM, codes, templates)
├── cli-tools/                 # Batch processing scripts
├── shared-scripts/            # Python utilities
├── examples/                  # Sample inputs/outputs
├── docs/                      # Documentation
├── install.sh                 # Installation script
├── uninstall.sh              # Uninstallation script
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── CLAUDE.md                  # Development guide
└── LICENSE                    # MIT license
```

---

## Contributing

Contributions welcome! See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

---

## License

MIT License - see [LICENSE](LICENSE) for details.

---

## Support

- **Issues**: [GitHub Issues](https://github.com/sbalci/pathology-skills-collection/issues)
- **Discussions**: [GitHub Discussions](https://github.com/sbalci/pathology-skills-collection/discussions)

---

**Built for clinical pathologists by pathologists** 🔬
