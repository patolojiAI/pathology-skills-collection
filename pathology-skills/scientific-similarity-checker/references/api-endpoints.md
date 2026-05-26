# API Endpoint Reference — Scientific Databases

## 1. PubMed / NCBI E-utilities

Base URL: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/`

### ESearch — Find PMIDs
```
GET esearch.fcgi?db=pubmed&term={query}&retmax={n}&retmode=json
```
Key field tags:
- `[ti]` — title only
- `[tiab]` — title or abstract
- `[au]` — author (Last FI format)
- `[1au]` — first author only
- `[dp]` — date published (YYYY or YYYY:YYYY)
- `[ta]` — journal title abbreviation
- `[mh]` — MeSH term
- `[la]` — language (e.g., `french[la]`)
- `[pmid]` — PubMed ID
- `[doi]` — DOI

Example:
```
term="machine learning"[tiab] AND "deep learning"[tiab] AND 2022:2024[dp]
```

### EFetch — Get Records
```
GET efetch.fcgi?db=pubmed&id={pmid1,pmid2,...}&rettype=abstract&retmode=text
GET efetch.fcgi?db=pubmed&id={pmid}&rettype=xml&retmode=xml
```

### ESummary — Lightweight Summary
```
GET esummary.fcgi?db=pubmed&id={pmid1,pmid2}&retmode=json
```

### ELink — Related Articles
```
GET elink.fcgi?dbfrom=pubmed&db=pubmed&id={pmid}&cmd=neighbor_score&retmode=json
```

Rate limits: 3 req/sec without key, 10 req/sec with API key.

---

## 2. OpenAlex (Completely Free, No API Key Required)

Base URL: `https://api.openalex.org/`

### Search Works by Title/Abstract
```
GET /works?search={query}&per_page=10&sort=relevance_score:desc
GET /works?search={query}&filter=publication_year:2020-2024&per_page=10
```

### Filter by DOI
```
GET /works/https://doi.org/{doi}
GET /works?filter=doi:{doi}
```

### Filter by Author
```
GET /authors?search={author_name}&per_page=5
GET /works?filter=author.id:{openalex_author_id}&per_page=20&sort=publication_year:desc
```

### Filter by Journal/Source
```
GET /sources?search={journal_name}&per_page=5
GET /works?filter=primary_location.source.id:{source_id}&per_page=15&sort=publication_year:desc
```

### Filter by Institution
```
GET /institutions?search={institution_name}&per_page=5
GET /works?filter=institutions.id:{institution_id}&per_page=15
```

### Related Works (Concept-based)
```
GET /concepts?search={topic_keyword}&per_page=5
GET /works?filter=concepts.id:{concept_id}&sort=cited_by_count:desc&per_page=15
```

### Full Text Search (title + abstract)
```
GET /works?search={phrase}&filter=type:article&per_page=10
```

Fields available in response: `id, doi, title, display_name, publication_year, publication_date,
primary_location, open_access, authorships, cited_by_count, concepts, abstract_inverted_index`

To reconstruct abstract from `abstract_inverted_index`:
```python
def reconstruct_abstract(inverted_index):
    if not inverted_index:
        return ""
    positions = {}
    for word, pos_list in inverted_index.items():
        for pos in pos_list:
            positions[pos] = word
    return " ".join(positions[k] for k in sorted(positions.keys()))
```

Rate limit: Polite pool (with email): 100k/day; anonymous: 10 req/sec.
Add `mailto=youremail@example.com` to requests to join polite pool.

---

## 3. Semantic Scholar

Base URL: `https://api.semanticscholar.org/graph/v1/`

### Paper Search
```
GET /paper/search?query={encoded_query}&limit=10&fields=title,authors,year,abstract,externalIds,citationCount,venue,referenceCount,openAccessPdf
```

### Paper by DOI
```
GET /paper/DOI:{doi}?fields=title,authors,year,abstract,citations,references
```

### Paper by ArXiv ID
```
GET /paper/arXiv:{arxiv_id}?fields=title,authors,year,abstract
```

### Author Search
```
GET /author/search?query={author_name}&limit=5&fields=name,paperCount,hIndex,papers
```

### Author's Papers
```
GET /author/{author_id}/papers?limit=20&fields=title,year,venue,citationCount&sort=year:desc
```

### Citation Graph
```
GET /paper/{paper_id}/citations?limit=20&fields=title,authors,year,venue
GET /paper/{paper_id}/references?limit=20&fields=title,authors,year,venue
```

### Batch Paper Lookup
```
POST /paper/batch
Body: {"ids": ["DOI:10.xxx", "arXiv:xxxx", "PMID:123456"]}
```

Rate limit: 100 req/sec unauthenticated; 1000 req/sec with API key.

---

## 4. arXiv API

Base URL: `https://export.arxiv.org/api/`

### Search by Title
```
GET query?search_query=ti:{title_words}&max_results=10&sortBy=relevance
```

### Search by Author
```
GET query?search_query=au:{last_name}&max_results=20&sortBy=submittedDate&sortOrder=descending
```

### Combined Search
```
GET query?search_query=ti:{keyword1}+AND+au:{author}&max_results=10
GET query?search_query=abs:{keyword1}+AND+abs:{keyword2}&max_results=10
```

### Specific Category
```
GET query?search_query=cat:cs.AI+AND+ti:{title_words}&max_results=10
```

Categories: cs.AI, cs.LG, cs.CV, q-bio, stat.ML, math, physics, econ, eess

Response is Atom XML. Key fields: `title`, `author/name`, `summary` (=abstract),
`published`, `updated`, `arxiv:doi`, `link href` (full paper URL).

Parse with Python's `xml.etree.ElementTree` or `feedparser`.

---

## 5. Crossref

Base URL: `https://api.crossref.org/`

### Lookup by DOI (most reliable)
```
GET /works/{doi}
```

### Title Search
```
GET /works?query.title={encoded_title}&rows=5&select=DOI,title,author,published,container-title,type,abstract
```

### Author Search
```
GET /works?query.author={author_name}&rows=10&select=DOI,title,author,published,container-title
```

### Journal Works
```
GET /journals/{issn}/works?rows=10&sort=published&order=desc
```

Response fields: `DOI`, `title`, `author` (array of `{given, family}`), `published`,
`container-title` (journal name), `abstract` (not always present), `type`, `is-referenced-by-count`

Rate limit: Polite pool with `mailto` in User-Agent header. Fast pool available.
User-Agent: `MyTool/1.0 (mailto:user@example.com)`

---

## 6. IEEE Xplore (Web Search Only — no free API without institutional key)

Use web_search with these patterns:
```
"{paper title}" site:ieeexplore.ieee.org
{author_name} {keyword} IEEE {year}
"{title}" IEEE Transactions
{topic} IEEE conference {year}
```

Use web_fetch on ieeexplore.ieee.org result pages to get metadata.
Abstract and metadata are visible without login; full PDF requires access.

---

## 7. DOAJ (Directory of Open Access Journals)

```
GET https://doaj.org/api/search/articles/{query}?pageSize=10
GET https://doaj.org/api/search/articles/bibjson.title:{title}
GET https://doaj.org/api/search/articles/bibjson.author.name:{author}
```

Useful for verifying if a journal is legitimate (predatory journal detection).

---

## 8. Retraction Watch / iThenticate-compatible

No public API. Use web_search:
```
"{title}" retracted
"{author_name}" retraction
site:retractionwatch.com {author_name}
```

---

## 9. Europe PMC (broader than PubMed, includes preprints)

```
GET https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={query}&format=json&resultType=core&pageSize=10
GET https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=AUTH:{author_name}&format=json&pageSize=20
GET https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:{title_words}&format=json&pageSize=10
```

Covers: PubMed, PMC, EuropePMC preprints, patents, and agricultural literature.

---

## Query Encoding Notes

Always URL-encode search terms:
- Spaces → `+` or `%20`
- Quotes → `%22`
- Colons → `%3A`

In Python: `urllib.parse.quote(query, safe='')` or `urllib.parse.urlencode({'query': query})`
