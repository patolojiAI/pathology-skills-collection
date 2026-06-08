---
title: Pathology Skills Collection
description: 15 specialized Claude skills for surgical pathology QA, staging, coding, synoptic reporting, and research integrity.
---

**A modular collection of 15 Claude skills** for clinical pathologists, QA teams,
and researchers — CAP/ICCR compliance checking, synoptic templates, TNM staging,
SNOMED CT / ICD-O-3 coding, tumor-board summaries, and research-integrity tools —
in **English and Turkish**.

[💻 Source on GitHub](https://github.com/patolojiAI/pathology-skills-collection){: .btn }
&nbsp;
[⬇️ Download `.skill` files](https://github.com/patolojiAI/pathology-skills-collection/releases/latest){: .btn }

---

## Install (Claude Code)

```text
/plugin marketplace add patolojiAI/pathology-skills-collection
/plugin install pathology-skills@pathology-skills-collection
```

Installs all 15 skills at once. Prefer scripts, or the Claude.ai app with `.skill`
files? See the [installation guide](https://github.com/patolojiAI/pathology-skills-collection#installation).

📺 **New to Claude?** This short video walks through installing the Claude
desktop app and adding a skill:

<div style="max-width:760px; margin:1rem 0;">
  <div style="position:relative; padding-bottom:56.25%; height:0; overflow:hidden; border-radius:6px;">
    <iframe src="https://www.youtube.com/embed/pXIkpDMyTG4" style="position:absolute; top:0; left:0; width:100%; height:100%; border:0;" title="Install the Claude desktop app and add a skill" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
</div>

---

## What's inside

**Pathology QA & reporting**

- `pathology-compliance-checker` — CAP/ICCR completeness checking
- `pathology-template-generator` — synoptic templates with optional pre-fill
- `tnm-stage-calculator` — AJCC 8th-edition staging
- `pathology-coder` — SNOMED CT / ICD-O-3 coding
- `pathology-tumor-board-summary` — concise MDT summaries
- `report-converter` — free-text → synoptic conversion
- `pathology-report-checker` — all-in-one: compliance + staging + templates + summary + coding in one skill

**Tumor-type specialists**

- `breast-pathology-specialist`, `colorectal-pathology-specialist`,
  `pancreas-pathology-specialist`, `gastric-pathology-specialist`

**Research integrity & tooling**

- `scientific-similarity-checker` — plagiarism / duplicate-publication screening
- `reference-verifier` — 4-level citation auditor
- `statistical-methods-reviewer` — 9-aspect methods rubric
- `qupath-guide` — digital-pathology / Groovy scripting guidance

---

## Related

- **Pathology Report Checker** — the standalone QA skill and its ECDP2026 study:
  [reportskill.patoloji.dev](https://reportskill.patoloji.dev/) — [live demo](https://reportskill.patoloji.app/) · [Hugging Face](https://huggingface.co/spaces/patolojiai/pathology-report-checker-skill)
- **Issues & Discussions:**
  [GitHub](https://github.com/patolojiAI/pathology-skills-collection/issues)

---

*MIT licensed. Built by [Serdar Balcı, MD](https://github.com/sbalci) and contributors.*
