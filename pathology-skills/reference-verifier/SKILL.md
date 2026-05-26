---
name: reference-verifier
description: Comprehensive academic reference auditor that performs four levels of verification on citations in uploaded manuscripts (.pdf, .docx). Level 1 checks if references actually exist. Level 2 verifies metadata accuracy (authors, year, journal, volume, pages). Level 3 checks whether the cited paper actually covers the topic it is cited for. Level 4 analyzes whether each citation is used correctly in context — confirming if the cited source truly supports, contradicts, or is neutral toward the claim being made. Saves a BibTeX file (.bib) and a markdown audit report (HTML optional) in the current working directory. Use whenever the user uploads a manuscript and asks to check, verify, validate, or audit references, citations, or bibliography, generate a .bib file, detect fake or hallucinated references, check citation accuracy, verify citation context, or audit a reference list. Especially tuned for biomedical/PubMed-indexed literature but works for any discipline.
license: MIT
metadata:
  version: 1.3.0
  author: Serdar Balci
---

# Reference Verifier & Citation Auditor

Performs a comprehensive 4-level audit of academic references in uploaded manuscripts. Goes beyond simple existence checks to verify metadata accuracy, topical relevance, and contextual correctness of each citation.

## The Four Verification Levels

### Level 1: Existence Verification
> Does this reference actually exist as a real publication?

### Level 2: Metadata Verification
> Are the authors, title, year, journal, volume, issue, and pages correct?

### Level 3: Topical Relevance
> Does the cited paper actually discuss the topic it is being cited for?

### Level 4: Contextual Accuracy
> Is the citation used correctly? Does the source truly support, contradict, or remain neutral toward the claim made in the manuscript — matching how it is presented?

---

## Workflow

### Step 0: Parse the Manuscript

1. Read the uploaded document from `/mnt/user-data/uploads/`
2. Extract TWO things:
   a. **The reference list** (bibliography section at the end)
   b. **The full manuscript text with in-text citations preserved** — this is critical for Levels 3-4

For each in-text citation, identify:
- The citation marker (e.g., `[1]`, `[Smith 2023]`, superscript number)
- The surrounding sentence/paragraph (the **citation context**)
- What claim is being made at that point
- How the citation is framed (e.g., "Smith et al. demonstrated...", "consistent with previous findings [3]", "in contrast to earlier reports [7]")

Build a **citation map**: a structured list linking each reference to every place it is cited in the manuscript with its context.

Use Python with appropriate libraries:
- For PDF: `pymupdf` (fitz) or `pdfplumber`
- For DOCX: `python-docx`
- Install with `pip install --break-system-packages`

### Step 1: Level 1 — Existence Verification

For each reference, attempt to find it in databases:

#### 1a. DOI Check (if DOI present)
- Use `web_fetch` on `https://api.crossref.org/works/{DOI}`
- Valid response = reference exists

#### 1b. PubMed Search
- Use `PubMed:search_articles` to search by title keywords and first author
- If found, use `PubMed:get_article_metadata` to get full details
- Use `PubMed:convert_article_ids` to get DOI/PMCID if missing

#### 1c. CrossRef Title Search (fallback)
- Use `web_fetch` on `https://api.crossref.org/works?query.bibliographic={encoded_title}&rows=3`
- Check if any result matches

#### 1d. Scholar Gateway (additional fallback)
- Use `Scholar Gateway:semanticSearch` with the reference title as query
- Check if returned results match

**Status assignment:**
- `EXISTS` — Found in at least one database
- `NOT_FOUND` — Not found in any database (possible fabrication)

### Step 2: Level 2 — Metadata Verification

For references that exist, compare the manuscript's reference entry against database records:

| Field | Match criteria |
|-------|---------------|
| Title | ≥85% fuzzy similarity |
| First author | Last name match |
| Author list | All authors present (order may vary) |
| Year | Exact match |
| Journal name | Fuzzy match (abbreviations differ) |
| Volume | Exact match |
| Pages | Start page match at minimum |
| DOI | Exact match if both present |

Use the `scripts/ref_utils.py` helper for fuzzy matching.

**Status assignment:**
- `METADATA_CORRECT` — All fields match
- `METADATA_MINOR_ERRORS` — 1-2 minor discrepancies (e.g., page range off by one, journal abbreviation difference)
- `METADATA_MAJOR_ERRORS` — Significant mismatches (wrong year, wrong journal, wrong first author)

For each error, record exactly which fields are wrong and what the correct values are.

### Step 3: Level 3 — Topical Relevance Check

For each citation, determine whether the cited paper actually covers the topic it is cited for.

#### 3a. Retrieve the cited paper's content
Try in this order:
1. **Full text via PMC**: Use `PubMed:convert_article_ids` to get PMCID, then `PubMed:get_full_text_article`
2. **Abstract via PubMed**: Use `PubMed:get_article_metadata` (always has abstract)
3. **Scholar Gateway**: Use `Scholar Gateway:semanticSearch` with a query combining the paper's title and the topic it's cited for
4. **bioRxiv/medRxiv**: If it's a preprint, use `bioRxiv:get_preprint`

#### 3b. Identify the cited topic
From the citation map (Step 0), determine what specific topic/claim the manuscript cites this reference for. For example:
- Manuscript says: "The incidence of NEC is approximately 7% in VLBW infants [12]."
- Cited topic: NEC incidence rate in VLBW infants

#### 3c. Check topical coverage
Analyze the retrieved content (full text or abstract) to determine:
- Does the cited paper discuss this specific topic?
- Is the topic a central focus or just briefly mentioned?

**Status assignment:**
- `TOPIC_CONFIRMED` — The cited paper clearly covers the cited topic
- `TOPIC_PERIPHERAL` — The paper mentions the topic but it is not a main focus
- `TOPIC_NOT_FOUND` — The paper does not appear to discuss the cited topic at all
- `TOPIC_UNVERIFIABLE` — Could not retrieve enough content to assess (only title available)

### Step 4: Level 4 — Contextual Accuracy Check

The most critical level. Determine whether the citation is used correctly in the manuscript context.

#### 4a. Classify citation usage in the manuscript
Read how the citation is used and classify the **manuscript's claim**:
- **SUPPORTS**: The manuscript presents the citation as supporting/confirming a claim
  - Phrases: "as shown by", "consistent with", "demonstrated that", "confirmed by", "in agreement with"
- **CONTRADICTS**: The manuscript presents the citation as opposing/contradicting
  - Phrases: "in contrast to", "unlike", "however, X found that", "contradicts", "despite findings by"
- **NEUTRAL**: Citation is used for background, definition, or without directional claim
  - Phrases: "has been reported", "reviewed by", "defined as", "according to"
- **METHODOLOGICAL**: Citation is used to justify a method or approach
  - Phrases: "as described by", "following the protocol of", "using the method of"
- **QUANTITATIVE**: Citation is used to cite a specific number, rate, or statistic
  - Phrases: "reported a rate of X%", "found that N=", "estimated at"

#### 4b. Verify against source content
Using the retrieved content from Level 3, check:
- Does the cited paper actually say what the manuscript claims it says?
- If a specific statistic is cited, does the source contain that number?
- If the manuscript says "Smith et al. found X", did they actually find X?
- Is the directionality correct (support vs. contradict)?

**Status assignment:**
- `CITATION_CORRECT` — The source supports the way it is cited
- `CITATION_MISLEADING` — The source is real and relevant, but the manuscript misrepresents its findings (e.g., claims support when the source actually found the opposite)
- `CITATION_EXAGGERATED` — The source partially supports the claim but the manuscript overstates it
- `CITATION_IMPRECISE` — Minor inaccuracies in how the source is represented (e.g., slightly wrong statistic)
- `CITATION_UNVERIFIABLE` — Cannot retrieve enough content to verify contextual accuracy
- `CITATION_METHOD_ONLY` — Cited for methodology; cannot assess claim accuracy

For each non-correct status, provide a specific explanation of the discrepancy.

---

## Output Generation

### Output 1: `verified_references.bib`

BibTeX file containing all references that passed Level 1 (existence), with corrected metadata from Level 2. Use `scripts/ref_utils.py` for generation.

```bibtex
@article{Smith2024,
  author    = {Smith, John and Doe, Jane},
  title     = {Corrected Title From Database},
  journal   = {Correct Journal Name},
  year      = {2024},
  volume    = {10},
  number    = {2},
  pages     = {100--110},
  doi       = {10.xxxx/xxxxx},
  pmid      = {12345678},
}
```

### Output 2: `reference_audit_report.md`

Comprehensive markdown report organized as follows:

```markdown
# Reference Audit Report

## Executive Summary
- Total references: N
- Level 1 (Existence): X verified, Y not found
- Level 2 (Metadata): X correct, Y with errors
- Level 3 (Topical): X confirmed, Y questionable
- Level 4 (Context): X correct, Y problematic

## Critical Issues (Action Required)
[References with NOT_FOUND, TOPIC_NOT_FOUND, CITATION_MISLEADING, or METADATA_MAJOR_ERRORS]

## Detailed Audit by Reference

### Reference [1]: Smith et al. (2024)
**Level 1 — Existence**: ✅ EXISTS (PMID: 12345678)
**Level 2 — Metadata**: ⚠️ MINOR ERRORS
  - Year in manuscript: 2023 → Correct: 2024
  - Pages in manuscript: 100-108 → Correct: 100-110
**Level 3 — Topical Relevance**:
  - Cited for: NEC incidence in preterm infants
  - Assessment: ✅ TOPIC_CONFIRMED — The paper's primary focus is NEC epidemiology
**Level 4 — Contextual Accuracy**:
  - Citation 1: "Smith et al. reported a NEC incidence of 7% [1]"
    - Usage type: QUANTITATIVE
    - Assessment: ⚠️ CITATION_IMPRECISE — Source reports 6.8%, manuscript rounds to 7%
    - Recommendation: Consider citing the exact figure (6.8%)
  - Citation 2: "These findings support early intervention [1]"
    - Usage type: SUPPORTS
    - Assessment: ✅ CITATION_CORRECT — Source concludes early intervention improves outcomes

[Repeat for each reference]

## Metadata Corrections Table
| Ref # | Field | In Manuscript | Correct Value |
|-------|-------|--------------|---------------|
| [3]   | Year  | 2023         | 2024          |
| [7]   | Pages | 45-50        | 45-52         |

## References Not Found
[Details on references that could not be verified]
```

### Where to write the files

Write both outputs to the user's **current working directory** (not
`/mnt/user-data/outputs/` — that path only exists in the Claude.ai web
sandbox and will not work in local CLI installs).

- `reference_audit_report.md` — the markdown report shown above
- `verified_references.bib` — the cleaned BibTeX

If the input manuscript file is named e.g. `paper.pdf`, prefix the outputs
with the manuscript stem: `paper_audit.md` and `paper_refs.bib`. Otherwise
fall back to the generic names.

### Optional: HTML report

If the user asks for HTML (phrases like "as html", "html report", "open in
browser"), also produce `<stem>_audit.html` next to the markdown. Use the
first method that works:

1. **pandoc** (preferred):
   ```bash
   pandoc <stem>_audit.md -o <stem>_audit.html --standalone --metadata title="Reference Audit"
   ```
2. **Python `markdown` library** (fallback — `pip install --break-system-packages markdown`):
   ```bash
   python3 -c "import markdown; h=markdown.markdown(open('<stem>_audit.md').read(),extensions=['tables','fenced_code']); print('<!DOCTYPE html><html><head><meta charset=\"utf-8\"><title>Reference Audit</title><style>body{font-family:system-ui,sans-serif;max-width:900px;margin:2em auto;padding:0 1em;line-height:1.5}table{border-collapse:collapse}td,th{border:1px solid #ccc;padding:6px 10px}code{background:#f4f4f4;padding:2px 4px}</style></head><body>'+h+'</body></html>')" > <stem>_audit.html
   ```

### After writing

In the chat reply, output:
- A one-line summary (e.g. "Saved audit → `paper_audit.md`, `paper_refs.bib`")
- The absolute path of every file written
- The Executive Summary block from the report (counts only)
- Highlight any **critical** issues (NOT_FOUND / CITATION_MISLEADING /
  METADATA_MAJOR_ERRORS / RETRACTED)

Do **not** dump the full per-reference detail into chat after writing —
point the user at the file.

---

## Processing Strategy

### For small reference lists (≤15 references)
Process all four levels for each reference sequentially. Give a progress update every 5 references.

### For large reference lists (>15 references)
1. Run Level 1 (existence) for ALL references first
2. Run Level 2 (metadata) for all existing references
3. Ask the user which references to deep-audit at Levels 3-4, or do all if they request comprehensive audit
4. Levels 3-4 require fetching content for each cited paper — this is the slowest step

### Rate limiting
- Add 0.5s delays between PubMed API calls
- Add 1s delays between CrossRef API calls
- Process in batches if needed

## Important Notes

- **Full text availability**: Not all papers have full text in PMC. When only abstracts are available, Level 3-4 assessments are less certain — always note this limitation clearly.
- **Citation context extraction**: Pay careful attention to surrounding text. A single reference may be cited multiple times in different contexts — check ALL occurrences separately.
- **Multiple citations in one bracket**: When a manuscript cites `[3-5]` or `[2,7,12]`, each reference needs its own contextual assessment.
- **Preprints**: Check bioRxiv/medRxiv for preprints. Note if a preprint has since been published in final form — the published version may differ.
- **Non-English references**: Flag for manual review if content cannot be retrieved in English.
- **Self-citation**: Note when the manuscript's authors cite their own work (not an error, but useful metadata).
- **Retracted papers**: If a cited paper has been retracted, flag this prominently as a **CRITICAL** issue.
- **Review articles vs. primary sources**: Note if a citation points to a review article when the context implies a primary source finding.

## Dependencies

- Python packages: `pymupdf`, `python-docx`, `pdfplumber` (install as needed)
- Tools: PubMed MCP tools, Scholar Gateway, bioRxiv tools, web_fetch (for CrossRef API)
- Helper script: `scripts/ref_utils.py` — fuzzy matching, BibTeX generation, report formatting
