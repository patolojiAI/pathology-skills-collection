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

### Option 3: Claude.ai App (browser / desktop) — upload `.skill` files

Each release publishes a standalone `.skill` file for every skill (self-contained
zip, no shared dependencies). Upload one through the Claude.ai web app or the
Claude desktop app:

1. Open the latest release: **[Releases page](https://github.com/sbalci/pathology-skills-collection/releases/latest)**
2. Download the `.skill` file(s) you want from the **Assets** section.
3. In claude.ai, open **Settings → Capabilities → Skills → Upload skill** and
   select the downloaded file. Repeat for each skill.

No terminal, no git, no admin rights needed. Updates: download the new
release's `.skill` file and re-upload.

> **Older alternative (still works):** the [Claude.ai Project setup](docs/CLAUDE_APP_SETUP.md)
> walkthrough — paste SKILL.md into a Project's custom instructions. Use this
> if your account doesn't yet have the **Settings → Capabilities → Skills**
> upload UI.

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
claude "Generate blank Whipple template using pathology-template-generator"

# Tumor board summary
claude "Create tumor board summary using pathology-tumor-board-summary" < report.txt

# SNOMED coding
claude "SNOMED code for invasive ductal carcinoma grade 2 using pathology-coder"
```

### Batch Processing Multiple Reports

**✅ RECOMMENDED: Use Claude CLI directly (no API key needed)**

```bash
# Process Excel file with 100 reports - Claude analyzes each with LLM intelligence
claude "Read reports.xlsx and use breast-pathology-specialist to analyze each report. Provide compliance scores and export results to Excel."

# Process all reports in a directory
claude "Analyze all .txt files in reports_dir/ using pathology-compliance-checker and create summary Excel."

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

## Skills

13 skills in three groups: **clinical workflow tools** for daily report QA,
**all-in-one specialist skills** that handle a tumor type end-to-end, and
**research-integrity skills** for manuscripts and statistical reviews.

| # | Skill | Group | One-liner |
|---|---|---|---|
| 1 | [`pathology-compliance-checker`](#1-pathology-compliance-checker) | Clinical · single-purpose | CAP/ICCR scoring + pT/pN/margin cross-validation |
| 2 | [`pathology-template-generator`](#2-pathology-template-generator) | Clinical · single-purpose | Blank or pre-filled CAP synoptic templates |
| 3 | [`tnm-stage-calculator`](#3-tnm-stage-calculator) | Clinical · single-purpose | AJCC 8th pT/pN/pM → stage group, with consistency checks |
| 4 | [`pathology-coder`](#4-pathology-coder) | Clinical · single-purpose | SNOMED CT and ICD-O-3 morphology/topography lookups |
| 5 | [`pathology-tumor-board-summary`](#5-pathology-tumor-board-summary) | Clinical · single-purpose | 3–5 line MDT summary from a full report |
| 6 | [`report-converter`](#6-report-converter) | Clinical · single-purpose | Free-text → CAP synoptic; addenda / amendments |
| 7 | [`breast-pathology-specialist`](#7-breast-pathology-specialist) | Clinical · all-in-one | End-to-end breast cancer workflow |
| 8 | [`colorectal-pathology-specialist`](#8-colorectal-pathology-specialist) | Clinical · all-in-one | End-to-end colorectal workflow incl. MSI/MMR + TME |
| 9 | [`pancreas-pathology-specialist`](#9-pancreas-pathology-specialist) | Clinical · all-in-one | End-to-end pancreas workflow incl. 6 Whipple margins |
| 10 | [`gastric-pathology-specialist`](#10-gastric-pathology-specialist) | Clinical · all-in-one | End-to-end gastric workflow incl. Lauren / WHO / HER2 |
| 11 | [`scientific-similarity-checker`](#11-scientific-similarity-checker) | Research integrity | Multi-DB literature scan + tiered misconduct warnings |
| 12 | [`reference-verifier`](#12-reference-verifier) | Research integrity | 4-level citation audit (existence → metadata → topic → context) |
| 13 | [`statistical-methods-reviewer`](#13-statistical-methods-reviewer) | Research integrity | Statistical-methods audit on a 0–18 scored rubric |

> All 13 skills auto-detect English and Turkish input. The four tumor specialists
> share the four core clinical workflows (compliance, staging, templates, summaries)
> with the single-purpose skills — pick the **specialist** when you want one
> skill to own a whole case, or the **single-purpose skills** when you want them
> usable across tumor types.

---

### Clinical workflow — single-purpose

#### 1. `pathology-compliance-checker`

Validates surgical pathology cancer reports against CAP (College of American
Pathologists) and ICCR (International Collaboration on Cancer Reporting)
protocols. Performs element-completeness checking, severity-weighted scoring
(Critical −15, Major −5, Minor −2 per missing element), and automatic
cross-validation of pT vs tumor size, pN vs node count, margins vs R
classification, and stage-group consistency.

- **Triggers:** "check compliance", "validate against CAP", "score this report", "audit this synoptic", "find missing elements", "verify pT/pN consistency"
- **Output:** compliance score 0–100, missing-element list, cross-validation flags, prioritized recommendations
- **Tumor types:** breast, colorectal, pancreas, gastric · **Languages:** EN / TR

```bash
claude "Check this report using pathology-compliance-checker" < report.txt
```

#### 2. `pathology-template-generator`

Generates blank or pre-filled CAP-compliant synoptic report templates with every
required, conditional, and recommended data element listed. Useful for
standardizing department reporting, training residents on synoptic structure,
or pre-filling templates before dictation.

- **Triggers:** "generate a synoptic template", "create a CAP report skeleton", "blank breast lumpectomy template", "Whipple specimen template", "pre-fill template"
- **Output:** markdown synoptic template with `[___]` placeholders or pre-filled values
- **Specimen types:** mastectomy, lumpectomy, colectomy, LAR, APR, Whipple, distal pancreatectomy, gastrectomy, EMR/ESD, polypectomy, sentinel / axillary LND · **Languages:** EN / TR

```bash
claude "Generate blank Whipple template using pathology-template-generator"
claude "Pre-fill breast template with 2.3cm Grade 2 IDC using pathology-template-generator"
```

#### 3. `tnm-stage-calculator`

Fast TNM stage-group calculation from pT, pN, pM categories using AJCC 8th
edition criteria. Flags inconsistencies (tumor-size-vs-pT, node-count-vs-pN),
validates the pT/pN/pM combination actually exists in AJCC 8th, and gives
brief prognostic context.

- **Triggers:** "what stage is pT2 N1 M0", "calculate TNM stage", "stage group for pT3 N1b breast", "is pT2 N0 M0 stage I or II"
- **Output:** stage group (0, I, IIA, IIB, IIIA, IIIB, IIIC, IV) with one-line prognostic note
- **Tumor types:** breast, colorectal, pancreas, gastric (uses pathologic stage groups, AJCC 8th 2017)

```bash
claude "What stage is pT2 N1a M0 for breast using tnm-stage-calculator"
```

#### 4. `pathology-coder`

Suggests SNOMED CT and ICD-O-3 morphology / topography codes for pathology
diagnoses, procedures, and biomarkers. Includes hierarchical parent / child
relationships and synonyms so you can pick the right specificity for LIS
integration, tumor-registry reporting, or billing support.

- **Triggers:** "SNOMED code for [diagnosis]", "ICD-O-3 code for [tumor type]", "code this diagnosis", "morphology code for"
- **Output:** SNOMED CT code + preferred term + hierarchy; ICD-O-3 morphology/behavior + topography
- **Coverage:** breast, colorectal, pancreas, gastric, prostate, lung, lymphoma, GIST + common procedures and biomarkers

```bash
claude "SNOMED code for invasive ductal carcinoma grade 2 using pathology-coder"
```

#### 5. `pathology-tumor-board-summary`

Distills full pathology reports into concise 3–5 line summaries for
multidisciplinary tumor board (MDT) meetings. Extracts diagnosis, TNM stage,
margins, lymph nodes, and key biomarkers — only the data points that drive
MDT decisions.

- **Triggers:** "create a tumor board summary", "MDT summary", "oncology consult summary", "3-line summary for the MDT"
- **Output:** 3–5 line paragraph or bulleted summary
- **Use cases:** MDT preparation, oncology consults, referral letters, case presentations

```bash
claude "Create tumor board summary using pathology-tumor-board-summary" < report.txt
```

#### 6. `report-converter`

Two-in-one skill: converts free-text narrative pathology reports into structured
CAP synoptic format **and** generates professional amendments, addenda, or
corrections for previously-issued reports. Helps clean up legacy reports and
supports proper documentation when biomarker results arrive late or errors
need correcting.

- **Triggers:** "convert to synoptic", "convert to CAP format", "structure this report", "generate an amendment", "add an addendum", "issue a corrected report"
- **Output:** CAP synoptic version of the original report OR a professional addendum / amendment block
- **Coverage:** breast, colorectal, pancreas, gastric, general carcinomas

```bash
claude "Convert to synoptic format using report-converter" < narrative_report.txt
claude "Create addendum for HER2 results using report-converter" < original_report.txt
```

---

### Clinical workflow — all-in-one specialists

The specialist skills combine compliance, staging, templates, biomarkers,
summaries, and coding for a specific tumor type into a single skill. Pick a
specialist when you want one tool to handle every part of a case end-to-end.

#### 7. `breast-pathology-specialist`

Comprehensive breast cancer pathology workflow combining compliance checking
(CAP Breast.Invasive, ICCR), TNM staging (AJCC 8th), synoptic templates,
biomarker reporting (ER / PR / HER2 / Ki-67 per ASCO/CAP guidelines), tumor
board summaries, and SNOMED coding.

- **Triggers:** "check breast report", "validate breast pathology", "stage this breast cancer", "interpret ER/PR/HER2", "generate breast template"
- **Output:** depends on request — score, stage, biomarker interpretation, template, or summary
- **Specimens:** mastectomy, lumpectomy, wide local excision, re-excision, sentinel LN biopsy, axillary LND · **Languages:** EN / TR

```bash
claude "Check this breast report using breast-pathology-specialist" < report.txt
```

#### 8. `colorectal-pathology-specialist`

Comprehensive colorectal cancer pathology workflow with compliance checking
(CAP ColoRectal, ICCR), AJCC 8th staging, MSI/MMR testing interpretation
(MLH1, PMS2, MSH2, MSH6 patterns and Lynch-syndrome implications), MERCURY
mesorectal-excision quality grading (complete / nearly complete / incomplete),
tumor board summaries, and SNOMED coding.

- **Triggers:** "check colorectal report", "validate CAP ColoRectal", "stage this colorectal cancer", "interpret MSI/MMR", "assess TME quality"
- **Output:** score, stage, MMR interpretation, TME grade, template, or summary
- **Specimens:** colectomy, low anterior resection, abdominoperineal resection, polypectomy, transanal excision · **Languages:** EN / TR

```bash
claude "Check this colorectal report using colorectal-pathology-specialist" < report.txt
```

#### 9. `pancreas-pathology-specialist`

Comprehensive pancreatic cancer pathology workflow for **exocrine pancreas
carcinoma**. Covers Whipple / distal-pancreatectomy specimen dissection
guidance, axial slicing protocol, the six margin assessments (SMA, SMV,
posterior, anterior, pancreatic neck, bile duct), AJCC 8th staging (CAP
Panc.Exo, ICCR), compliance scoring, and SNOMED coding.

- **Triggers:** "check pancreas report", "validate CAP Panc.Exo", "stage this pancreatic cancer", "assess Whipple margins"
- **Output:** score, stage, margin interpretation, R classification, template, or summary
- **Specimens:** Whipple (pancreaticoduodenectomy), distal pancreatectomy, total pancreatectomy, biopsy · **Languages:** EN / TR

```bash
claude "Check this Whipple report for all margins using pancreas-pathology-specialist" < report.txt
```

#### 10. `gastric-pathology-specialist`

Comprehensive gastric cancer pathology workflow covering Lauren classification
(intestinal / diffuse / mixed), WHO histologic typing, HER2 IHC / FISH
interpretation per ASCO/CAP, MSI/MMR status, AJCC 8th staging (CAP Stomach,
ICCR), compliance scoring, tumor board summaries, and SNOMED coding.

- **Triggers:** "check gastric report", "validate CAP Stomach", "stage this gastric cancer", "interpret Lauren", "interpret HER2 IHC/FISH"
- **Output:** score, stage, HER2 interpretation, Lauren type, template, or summary
- **Specimens:** total / subtotal / proximal gastrectomy, esophagogastrectomy, EMR / ESD · **Languages:** EN / TR

```bash
claude "Check this gastric report, ensure Lauren type specified using gastric-pathology-specialist" < report.txt
```

---

### Research integrity

These three skills work on **research manuscripts**, not clinical reports.
They save their outputs as markdown files in the current working directory
(HTML on request) so you can review them outside the chat.

#### 11. `scientific-similarity-checker`

Academic-integrity / literature-discovery tool. Takes a scientific article
(PDF, image, or plain text) and searches PubMed, OpenAlex, Semantic Scholar,
IEEE, arXiv, Crossref, and the web for similar work. Detects similarity by
abstract content, topic overlap, author network, and journal / venue, then
issues tiered warnings (🔴 likely misconduct · 🟡 needs investigation ·
🟢 normal practice · ℹ️ informational) for self-plagiarism, duplicate
publication, salami slicing, or related-work blind spots.

- **Triggers:** "check this paper for similar work", "duplicate publication check", "misconduct screening", "novelty check", "plagiarism screen", "find the authors' other work"
- **Output:** `<author>-<year>-<title>.md` (similarity report) saved in cwd, optional HTML, plus the verdict badge in chat
- **Use cases:** pre-submission self-check, journal pre-screening, integrity review, literature surveillance

```bash
claude "Use scientific-similarity-checker on this paper" < manuscript.pdf
```

#### 12. `reference-verifier`

Four-level citation auditor for manuscripts.

| Level | Question |
|---|---|
| 1 — Existence | Does the cited reference actually exist? (Crossref / PubMed / Scholar Gateway) |
| 2 — Metadata | Are the authors, year, journal, volume, pages correct? |
| 3 — Topical relevance | Does the cited paper actually cover the topic it's cited for? |
| 4 — Contextual accuracy | Does the source genuinely support / contradict / stay neutral to the claim? |

Catches fake or hallucinated references and citations that misrepresent the
source's findings.

- **Triggers:** "audit references", "verify citations", "check the bibliography", "generate a .bib file", "detect fake references", "verify citation context"
- **Output:** `<stem>_audit.md` markdown audit + `<stem>_refs.bib` cleaned BibTeX (HTML optional), saved in cwd
- **Best for:** biomedical / PubMed-indexed manuscripts, but works for any discipline

```bash
claude "Audit references using reference-verifier" < manuscript.pdf
```

#### 13. `statistical-methods-reviewer`

Critically reviews the statistical methods of a research article against a
9-aspect rubric scored 0–2 each (total /18):

1. Design–method alignment
2. Assumptions & diagnostics
3. Sample size & power
4. Multiplicity control
5. Model specification & confounding
6. Missing-data handling
7. Effect sizes & confidence intervals
8. Validation & calibration
9. Reproducibility & transparency

Also checks the paper against a curated red-flag catalogue (chi-square with
expected counts <5, stepwise regression without validation, Cox PH never
tested, AUC alone with no calibration, immortal-time bias, dichotomized
continuous predictors, etc.) and recommends concrete alternative analyses
where the rubric flags issues. Cross-references CONSORT / STROBE / STARD /
TRIPOD / PRISMA / REMARK / ARRIVE compliance when applicable.

- **Triggers:** "review the stats", "check the statistical methods", "audit the analysis", "are these tests correct", "score this paper's statistics"
- **Output:** `<slug>-stats-review.md` saved in cwd (HTML optional). Includes Overall Rating (🟢 Robust 15–18 / 🟡 Moderate 8–14 / 🔴 Weak 0–7), scored rubric table, red-flag list, and recommendations table

```bash
claude "Review the stats in this paper using statistical-methods-reviewer" < paper.pdf
```

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
