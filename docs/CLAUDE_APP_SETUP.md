# Using these skills in the Claude app (browser / desktop)

For colleagues who use **claude.ai** in a browser or the **Claude desktop app** —
not the Claude Code CLI. No terminal, no git, no admin rights needed.

The desktop and web Claude app does not yet support installing Claude Code skills
directly. The reliable workaround is to set up one **Claude Project** per skill
you want, paste the skill instructions into the Project, and attach any reference
files. From then on, conversations inside that Project get the skill's full
behavior.

This takes about **5 minutes per skill**.

---

## What you need

- A Claude account (Free, Pro, or Team — Projects is available on Free with limits)
- A web browser, OR the Claude desktop app
- That's it. No GitHub account, no installs.

---

## Step-by-step (worked example: breast-pathology-specialist)

### 1. Create the Project

1. Open **[claude.ai](https://claude.ai)** and sign in.
2. In the left sidebar click **Projects** → **Create project**.
3. Name it: `Breast Pathology Specialist` (or whatever you'll recognize).
4. Description (optional): `CAP/ICCR compliance, TNM staging, biomarker review for breast cancer reports.`
5. Click **Create**.

### 2. Copy the skill instructions into the Project

1. Open the skill's `SKILL.md` file on GitHub:
   **https://github.com/sbalci/pathology-skills-collection/blob/master/pathology-skills/breast-pathology-specialist/SKILL.md**
2. Click the **Raw** button (top right of the file view) to get plain text.
3. Select all (`Ctrl+A` / `Cmd+A`), copy.
4. Back in your Claude Project, click **Set custom instructions** (sometimes
   labeled **Project knowledge** → **Add instructions**).
5. Paste the entire SKILL.md content into the instructions box.
6. **Delete the top `--- name: ... description: ... ---` block** (the YAML
   frontmatter). It's metadata Claude doesn't need inside a Project.
7. Click **Save**.

### 3. Attach the reference files

The breast specialist references several files. From the GitHub repo, download
or copy-paste these into the Project's **Knowledge** panel (drag-and-drop the
`.md` files, or paste their content as text files):

- `pathology-skills/breast-pathology-specialist/references/diagnosis/breast_invasive_carcinoma.md`
- `pathology-skills/breast-pathology-specialist/references/macroscopy/breast_macroscopy.md`
- `shared-references/staging/tnm_stage_calculator.md`
- `shared-references/templates/synoptic_templates.md`
- `shared-references/biomarkers/BIOMARKERS_INDEX.md`
- `shared-references/coding/snomed_ct_codes.md`

To download a file directly, open it on GitHub, click **Raw**, then save the
page (`Ctrl+S` / `Cmd+S`).

> **Tip:** Free accounts have a knowledge size limit. If you hit it, attach only
> the references you'll actually use (e.g., skip the SNOMED codes file if you
> only do compliance checking).

### 4. Use it

Inside the Project, start a new chat and paste a pathology report:

```text
Check this breast report for CAP/ICCR compliance:

[paste report here]
```

The Project's instructions kick in automatically — you don't need to mention
the skill name. Claude follows the SKILL.md workflow and references the
attached files on demand.

You can also attach a PDF/DOCX directly to the message; Claude reads it.

---

## Repeat for each skill you want

The exact same recipe works for every skill in the collection. For each one:

1. Create a new Project named after the skill.
2. Paste its `SKILL.md` (minus YAML frontmatter) into the custom instructions.
3. Attach any files listed under the skill's **Reference files** section.

Recommended starter set if you only want to set up a few:

| Project name | SKILL.md path on GitHub | Best for |
|---|---|---|
| **Compliance Checker** | `pathology-skills/pathology-compliance-checker/SKILL.md` | Generic CAP/ICCR compliance across tumor types |
| **TNM Stage Calculator** | `pathology-skills/tnm-stage-calculator/SKILL.md` | Quick pT/pN/M → stage lookups (AJCC 8th) |
| **Tumor Board Summary** | `pathology-skills/pathology-tumor-board-summary/SKILL.md` | 3-5 line MDT summaries from full reports |
| **Statistical Methods Reviewer** | `pathology-skills/statistical-methods-reviewer/SKILL.md` | Auditing statistics in research papers |
| **Reference Verifier** | `pathology-skills/reference-verifier/SKILL.md` | 4-level citation audit for manuscripts |
| **Scientific Similarity Checker** | `pathology-skills/scientific-similarity-checker/SKILL.md` | Plagiarism / duplicate publication screening |

---

## Limitations vs the CLI

Honest tradeoffs of the Project approach:

| Feature | CLI install | Claude.ai Project |
|---|---|---|
| Install effort | One command | ~5 min per skill |
| Updates when the repo changes | `/plugin update` or rerun `install.sh` | Manual: re-copy SKILL.md |
| Python helper scripts (`batch_checker.py`, `watch_folder.py`) | Yes | No — Projects can't run scripts |
| File-output features (md / html / bib written to disk) | Yes — files land in your folder | Claude shows the file contents in chat; you copy/save manually |
| Batch processing many reports | Yes | One report per conversation |
| Works offline | No (both need Anthropic API) | No |
| Cost | Anthropic API usage | Counts against your Claude.ai message quota |

**Bottom line:** Projects are great for one-report-at-a-time clinical use. For
batch QA of dozens of reports, or for the scripted automation in `scripts/`,
you'll still want the CLI install (`./install.sh`).

---

## Sharing a Project with colleagues

Claude.ai Team and Enterprise plans let you share a Project with everyone in
your workspace — set it up once, and the whole department uses it. On Free / Pro,
each colleague needs to set up their own Project (the recipe is the same; they
can also clone yours by exporting your custom instructions and re-pasting).

---

## Troubleshooting

**Claude isn't following the skill's workflow.**
The YAML frontmatter (the top `--- ... ---` block) wasn't deleted, or the
SKILL.md wasn't fully pasted. Re-check the custom instructions field.

**"Knowledge limit reached" when uploading reference files.**
Free / Pro tiers have a per-Project knowledge cap. Attach only the references
the skill actively needs — most skills work fine with just the SKILL.md in
instructions and 1–2 key references.

**Claude says it can't find a file like `references/diagnosis/breast_invasive_carcinoma.md`.**
The SKILL.md text refers to file paths that exist in the GitHub repo, not in
the Project. As long as you've attached the file content (under any filename)
to the Project knowledge, Claude will use it. You can edit the SKILL.md text
inside the custom instructions to remove the `references/…` paths if it makes
things clearer.

**I want to use a different language (e.g., Turkish).**
The skills auto-detect language from your input. Just write the prompt and
paste the report in Turkish; the response will be in Turkish.

---

## Future: native skill support in the app

Anthropic is actively expanding plugin support across surfaces. When the
desktop / web app gains native skill installation, this Project workaround will
become unnecessary — but until then, this recipe gets your non-CLI colleagues
the same clinical behavior.
