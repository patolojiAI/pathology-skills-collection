# Pathology Skills Collection

**Comprehensive clinical pathology toolkit for Claude** - 13 specialized skills for surgical pathology quality assurance, template generation, staging, coding, clinical workflow optimization, and research integrity.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues](https://img.shields.io/github/issues/sbalci/pathology-skills-collection)](https://github.com/sbalci/pathology-skills-collection/issues)
[![GitHub stars](https://img.shields.io/github/stars/sbalci/pathology-skills-collection)](https://github.com/sbalci/pathology-skills-collection/stargazers)

![Version](https://img.shields.io/badge/version-1.3.0-blue)
![Skills](https://img.shields.io/badge/skills-13-blue)
![Tumor Types](https://img.shields.io/badge/tumor%20types-4-green)
![Languages](https://img.shields.io/badge/languages-EN%2FTR-orange)

---

## What This Provides

A modular collection of Claude skills for clinical pathologists, QA teams, and researchers:

- ✅ **Compliance checking** against CAP and ICCR guidelines
- 📋 **Synoptic template generation** with optional pre-fill
- 🔢 **TNM staging calculation** (AJCC 8th edition)
- 🏥 **SNOMED CT / ICD-O-3 coding** suggestions
- 📊 **Tumor board summaries** for MDT meetings
- 🔄 **Free-text to synoptic conversion** for legacy reports
- 🔍 **Scientific similarity checking** for academic integrity / plagiarism screening
- 📚 **Reference verification** (4-level citation auditor) for manuscripts

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

Pick the option that matches how your colleagues use Claude.

### Option 1: Plugin Marketplace — Recommended for Claude Code users

Works in **Claude Code** (terminal CLI, VS Code extension, or JetBrains plugin).
No cloning, no scripts, two slash commands inside a Claude Code session:

```text
/plugin marketplace add sbalci/pathology-skills-collection
/plugin install pathology-skills@pathology-skills-collection
```

That installs all 13 skills at once. To update later: `/plugin update`.

### Option 2: Clone + install.sh — for Claude Code users who prefer scripts

```bash
git clone https://github.com/sbalci/pathology-skills-collection.git
cd pathology-skills-collection
./install.sh

# Test
claude "What stage is pT2 N0 M0 for breast using tnm-stage-calculator"
```

Symlinks all 13 skills into `~/.claude/skills/`. Uninstall with `./uninstall.sh`.

### Option 3: Claude.ai App (browser / desktop) — for colleagues who don't use the CLI

The desktop and web Claude app doesn't support `/plugin install` yet, but you can
get the same behavior by setting up one **Project per skill**. Walkthrough in
[**docs/CLAUDE_APP_SETUP.md**](docs/CLAUDE_APP_SETUP.md) — 5 minutes per skill, no
terminal required.

### Option 4: Community Marketplace (auto-discovery after 5⭐)

Once this repo reaches 5+ GitHub stars it's auto-listed on
[claudemarketplaces.com](https://claudemarketplaces.com/) within 24 hours, which
gives a browse-and-install UI. The two-line `/plugin marketplace add ...` in
Option 1 works **right now** without waiting.

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
python scripts/process_skill.py --skill breast-pathology-specialist reports.xlsx
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

### Research Integrity Skills

| Skill | Purpose | Usage |
|-------|---------|-------|
| **scientific-similarity-checker** | Multi-database literature/plagiarism scan (PubMed, OpenAlex, Semantic Scholar, arXiv, Crossref, web) with tiered misconduct warnings | `claude "Check this paper for similar work using scientific-similarity-checker" < paper.pdf` |
| **reference-verifier** | 4-level citation audit: existence, metadata accuracy, topical relevance, contextual correctness | `claude "Audit references in this manuscript using reference-verifier" < manuscript.pdf` |
| **statistical-methods-reviewer** | Critical review of statistical methods with 9-aspect scoring rubric (0–18), red-flag detection, and concrete alternatives | `claude "Review the stats in this paper using statistical-methods-reviewer" < paper.pdf` |

---

## Documentation

- **[Getting Started Guide](docs/getting-started.md)** - Installation and setup
- **[Claude App Setup (browser/desktop)](docs/CLAUDE_APP_SETUP.md)** - 5-min recipe for colleagues who don't use the CLI
- **[Quick Reference](docs/QUICK_REFERENCE.md)** - 1-page trigger phrases and reference card
- **[Features](docs/FEATURES.md)** - Full feature documentation
- **[Workflow Guide](docs/WORKFLOW.md)** - Step-by-step compliance workflow
- **[Batch Processing Guide](docs/BATCH_PROCESSING.md)** - How to process multiple reports correctly
- **[Local LLM Setup](docs/LOCAL_LLM_SETUP.md)** - Ollama/LM Studio setup for offline use
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
├── scripts/                   # Python tools (batch, single, watch, file readers)
├── samples/                   # Sample reports with expected outputs
├── examples/                  # Example inputs/outputs
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
