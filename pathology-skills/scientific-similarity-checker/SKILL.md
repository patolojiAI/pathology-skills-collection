---
name: scientific-similarity-checker
description: >
  Analyze a scientific article (PDF, image, or text) to find similar work across PubMed,
  OpenAlex, Semantic Scholar, IEEE, arXiv, Crossref, and the web. Detects similarity by
  content/abstract, topic, authors, and journal. Issues tiered warnings when similarity
  levels suggest potential self-plagiarism, duplicate publication, or research misconduct.
  Use this skill whenever a user uploads or pastes a scientific article, manuscript, preprint,
  or abstract and asks to find related work, check for overlap, detect plagiarism, validate
  originality, perform a literature review, or investigate a paper's context. Also triggers for
  phrases like "check this paper", "find similar studies", "is this published elsewhere",
  "duplicate publication check", "misconduct screening", "novelty check", or "find the authors'
  other work". Always use this skill when academic integrity checking is implied, even implicitly.
---

# Scientific Similarity Checker

A multi-source literature search and academic integrity tool that analyzes a scientific article
against global databases to surface similar work and flag potential misconduct.

---

## Phase 1 — Extract Article Metadata

Before searching anything, extract as much metadata as possible from the input. The input may be:
- **PDF**: Use pdf-reading skill if available; otherwise read with bash `pdftotext` or similar
- **Image**: Read visually — extract title, authors, abstract from the image
- **Text/paste**: Parse directly

Extract these fields (mark each as `found` or `inferred` or `missing`):

```
title:          (full title)
authors:        (list: Last FM, Last FM, ...)
year:           (publication or submission year)
journal:        (journal/conference/preprint server name)
doi:            (if present)
pmid:           (if present)
abstract:       (full abstract text)
keywords:       (author-provided or extracted from abstract)
institution:    (author affiliations if visible)
funding:        (funding sources if visible)
corresponding:  (corresponding author email/name)
```

For the abstract, if not explicitly labeled, look for the structured paragraph immediately after
author affiliations. Keywords may appear at the end of the abstract or in a separate section.

If the DOI is present, use it immediately to do a Crossref lookup (Phase 2a) — this often
resolves all metadata at once.

---

## Phase 2 — Multi-Database Search Strategy

Run these searches. The order matters: start with exact lookups, then broaden.

### 2a. Exact DOI / PMID Lookup (if available)

If a DOI is found:
```
GET https://api.crossref.org/works/{DOI}
```
If a PMID is found:
```
GET https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={PMID}&retmode=json
```
These anchor the article definitively and may reveal if it is already published.

### 2b. PubMed Search (use PubMed MCP if connected, else REST API)

Run **3 separate queries**, collect top 10 results each:

1. **Title search**: `"{short_title}"[ti]` (use first 8-10 significant words)
2. **Author search**: `{first_author_last}[au] AND {year-2}:{year+1}[dp]`
3. **Topic search**: `{keyword1}[tiab] AND {keyword2}[tiab] AND {keyword3}[tiab]`

See `references/api-endpoints.md` for full PubMed syntax reference.

### 2c. OpenAlex Search (free, no API key needed)

Run **3 queries**:

1. **Title similarity**:
   `GET https://api.openalex.org/works?search={url_encoded_title}&per_page=10`

2. **Author's works**:
   First resolve author: `GET https://api.openalex.org/authors?search={first_author_name}&per_page=5`
   Then: `GET https://api.openalex.org/works?filter=author.id:{author_id}&per_page=20&sort=publication_year:desc`

3. **Journal/venue scan**:
   `GET https://api.openalex.org/works?filter=primary_location.source.display_name.search:{journal_name}&search={keyword1}+{keyword2}&per_page=10`

### 2d. Semantic Scholar Search

1. **Title search**:
   `GET https://api.semanticscholar.org/graph/v1/paper/search?query={encoded_title}&limit=10&fields=title,authors,year,abstract,externalIds,citationCount,venue`

2. **Author search** (resolve author first):
   `GET https://api.semanticscholar.org/graph/v1/author/search?query={author_name}&limit=5&fields=name,papers`
   Then fetch the author's recent papers.

### 2e. arXiv Search (for preprints, CS, physics, math, biology)

```
GET https://export.arxiv.org/api/query?search_query=ti:{title_words}+AND+au:{first_author}&max_results=10
```

Also search by abstract keywords:
```
GET https://export.arxiv.org/api/query?search_query=abs:{keyword1}+AND+abs:{keyword2}&max_results=10
```

### 2f. Web Search (IEEE, Google Scholar, general)

Use `web_search` tool for:
- `"{title}" IEEE` — catches IEEE Xplore papers
- `"{title}" site:scholar.google.com`
- `{first_author} {keyword1} {keyword2} {year} preprint`
- `"{title}" filetype:pdf`

IEEE has no free API; web search is the reliable path. Read full result pages
with `web_fetch` when snippets suggest strong relevance.

---

## Phase 3 — Similarity Scoring

For each retrieved article, compute a similarity profile across four dimensions.

### 3a. Content Similarity (Abstract/Body)

Compare the input abstract against each retrieved abstract using textual overlap reasoning:
- Identify shared phrases ≥ 5 words (verbatim or near-verbatim)
- Note shared sentences or heavily paraphrased sentences
- Estimate overall semantic overlap: **Low / Moderate / High / Very High**

Thresholds:
- **Low**: topic overlap only, different methods/conclusions
- **Moderate**: same topic, some shared framing/language
- **High**: substantial paragraph-level overlap, same methodology
- **Very High**: near-identical abstracts — strong misconduct signal

### 3b. Topic Similarity

Compare keywords, MeSH terms, and subject matter:
- Fully same topic + same methodology = **Highly Similar**
- Same topic, different methodology = **Related**
- Adjacent topic, different field = **Loosely Related**

### 3c. Author Overlap

Count authors in common:
- All authors match: **Identical authorship** → self-plagiarism risk
- Majority match: **Substantial overlap** → check for salami slicing
- First/last author same: **Core team reuse** → note it
- No overlap: **Independent** (still flag if content is near-identical)

### 3d. Journal/Venue Similarity

Note if the same group has published in:
- The **same journal** within ±3 years → possible duplicate submission
- **Closely related journals** from the same publisher
- A **preprint server** version of what appears to be a published paper → check if properly cited

---

## Phase 4 — Misconduct Assessment

Apply these tiered warning rules. Issue warnings prominently in the report.

### 🔴 RED FLAG — Likely Misconduct
Trigger when ANY of the following:
- Abstract similarity ≥ Very High AND author overlap ≥ 50% → **Duplicate publication**
- Title is identical or near-identical to an existing published paper with same authors → **Verbatim duplicate**
- Same data/results appear to be published in ≥2 journals without cross-reference → **Salami slicing**
- Unpublished manuscript matches a published article with same abstract → **Plagiarism of own prior work**

### 🟡 AMBER WARNING — Requires Investigation
- High content similarity (≥2 shared paragraphs or methods section) with author overlap
- Author has 3+ papers with highly similar titles/topics in same year
- Paper appears in a preprint server but introduction does not acknowledge the preprint
- Journal submission period overlaps with another identical submission (dual submission)

### 🟢 GREEN — Normal Academic Practice
- Self-citation of prior work with clear differentiation
- Same author team working on a research program (related but distinct studies)
- Preprint → journal pipeline (same paper, standard practice)
- Topic similarity without content similarity (normal scientific progress)

### ℹ️ INFORMATIONAL — Context
- Other authors working in the same area (independent parallel research)
- Different language versions of same work (may be legitimate translation)

---

## Phase 5 — Report Format

Always produce a structured report. Use this exact template:

```
# Scientific Similarity Analysis Report

## 📄 Article Analyzed
- **Title**: [extracted title]
- **Authors**: [list]
- **Year / Venue**: [year] | [journal/conference]
- **DOI**: [if found] | **PMID**: [if found]
- **Status**: [Published / Preprint / Unpublished manuscript]

---

## 🔍 Search Coverage
| Database | Queries Run | Results Found |
|---|---|---|
| PubMed | 3 | N |
| OpenAlex | 3 | N |
| Semantic Scholar | 2 | N |
| arXiv | 2 | N |
| IEEE/Web | 2 | N |
| Crossref (DOI) | 1 | N |
| **Total unique articles reviewed** | | **N** |

---

## ⚠️ Misconduct Assessment

[Insert RED FLAG / AMBER WARNING / GREEN / INFORMATIONAL badges here with explanations]

If no flags: "✅ No similarity patterns consistent with academic misconduct were detected."

---

## 📚 Similar Articles by Category

### By Content (Abstract / Methodology Overlap)
[List top 5, highest similarity first]
- **[Title]** — [Authors] — [Journal, Year] — [DOI/link]
  - Similarity: [High/Moderate/Low] | [Brief note on what overlaps]

### By Topic / Keywords
[List top 5-8 thematically related papers]

### By Authors (Other Work from Same Team)
[List recent papers by the same first/last author]

### By Journal / Venue
[List recent papers from same journal on related topics]

---

## 🧭 Research Landscape Summary
[2-3 sentences: Where does this paper sit in the literature? Is it consistent with a research 
program? Any unusual patterns in the publication record?]

---

## 🔗 Recommended Follow-Up
- [Any specific papers or authors worth deeper investigation]
- [Suggested searches the user could run manually]
- [Links to databases for manual review if needed]
```

---

## Handling Edge Cases

**Very common topic (thousands of papers)**: Prioritize recency (last 5 years) and exact phrase
matches in title. Note that high volume is expected — focus on near-identical abstracts only.

**No abstract visible**: Work from title and keywords. State clearly that abstract-level
similarity could not be assessed and recommend manual review of full text.

**Preprint without authors**: Search by title only. Flag that author-level analysis was not
possible.

**Non-English article**: Detect the language, search in that language on PubMed (use `[la]` tag)
and OpenAlex, and note that cross-language duplicate detection is limited.

**Image input only (photo of paper)**: Extract as much text as possible visually. If abstract
is partially cut off, note it and work with what's available.

**User wants only research tool mode (no misconduct check)**: Skip Phase 4 entirely and focus
on delivering a comprehensive related-work landscape for the topic.

---

## Tips for High-Quality Output

- Always **deduplicate** results across databases before the final report (same paper may appear
  in PubMed, OpenAlex, and Semantic Scholar)
- When abstract similarity is ambiguous, **quote the specific overlapping phrase** so the user
  can judge
- For author disambiguation (common names like "Wang J"), use institution + year to narrow
- OpenAlex has the broadest coverage across all fields — prioritize it for topic searches
- PubMed is best for biomedicine; arXiv for STEM preprints; IEEE for engineering/CS
- Semantic Scholar is strong on citation graphs and has good CS/AI coverage

---

## Reference Files

- `references/api-endpoints.md` — Full API endpoint reference for all databases with parameters
- `references/misconduct-taxonomy.md` — Detailed taxonomy of publication misconduct types,
  definitions, and authoritative sources (COPE, ORI, Retraction Watch)
