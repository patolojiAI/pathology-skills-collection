# Batch Processing Guide

Complete guide to processing multiple pathology reports at once using this skills collection.

---

## ⚠️ Critical Understanding

There are **TWO completely different approaches** to batch processing:

| Approach | Auth Required | LLM Intelligence | Use When |
|----------|--------------|------------------|----------|
| **Claude CLI** | Already authenticated | ✅ Full LLM analysis | You have Claude CLI (RECOMMENDED) |
| **Python API Script** | API key required | ✅ Full LLM analysis | No Claude CLI or programmatic integration |

**⚠️ Common Mistake:** Asking Claude to "generate a Python script" creates **regex-only** code with **NO LLM intelligence**.

---

## Method 1: Claude CLI (RECOMMENDED)

### Prerequisites

- Claude Code CLI installed ([claude.ai/code](https://claude.ai/code))
- Skills installed: `./install.sh`
- **NO API key needed** - you're already authenticated!

### Single Conversation Batch Processing

**Best for: 10-100 reports in Excel/CSV**

```bash
claude "I have reports.xlsx with 100 colorectal pathology reports in Turkish.

Use the colorectal-pathology-specialist skill to analyze EACH report with full LLM intelligence:
- Check CAP/ICCR compliance
- Calculate compliance scores
- Identify missing elements
- Validate pT/pN/stage consistency
- Provide recommendations

Export results to colorectal_compliance_results.xlsx with columns:
- Case ID
- Compliance Score
- Missing Elements
- Cross-validation Issues
- Recommendations

Begin analysis now."
```

**What happens:**
1. Claude reads the Excel file
2. For each report, Claude applies the skill's CAP/ICCR guidelines
3. **LLM contextually understands** each report (not just keyword matching)
4. Generates comprehensive Excel output

### Using the Helper Script

```bash
./batch_process_cli.sh reports.xlsx colorectal-pathology-specialist results/
```

### File-by-File Processing Loop

**Best for: Large batches (100+) or rate limiting**

```bash
# Create output directory
mkdir -p batch_results

# Process each report
for i in {1..100}; do
  echo "Processing report $i..."

  claude "Read row $i from reports.xlsx and analyze using breast-pathology-specialist. Save result to batch_results/report_${i}.txt"

  sleep 2  # Rate limiting
done

# Combine results
claude "Combine all files in batch_results/ into summary Excel file"
```

### PDF/Image Batch Processing

```bash
# Process all PDFs in a directory
claude "Analyze all PDF files in scanned_reports/ using pathology-compliance-checker. Use vision API to extract text from each PDF, then analyze with LLM intelligence. Export results to compliance_summary.xlsx"

# Process scanned images
claude "Process all .jpg images in pathology_images/ using breast-pathology-specialist. Extract text with OCR, analyze each with skill, export to Excel."
```

---

## Method 2: Python API Script

### When to Use This

- You DON'T have Claude CLI installed
- You need programmatic integration (CI/CD, automated workflows)
- You're building a web service or automation

### Prerequisites

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Get API key from console.anthropic.com
export ANTHROPIC_API_KEY="sk-ant-api03-..."

# 3. Verify it's set
echo $ANTHROPIC_API_KEY
```

### Usage

```bash
# Single Excel file
python scripts/process_skill.py \
  --skill colorectal-pathology-specialist \
  reports.xlsx \
  --output results/

# Directory of PDFs
python scripts/process_skill.py \
  --skill compliance-checker \
  pdf_reports/ \
  --output results/

# Single PDF
python scripts/process_skill.py \
  --skill breast-pathology-specialist \
  report.pdf \
  --output results/
```

### Cost Estimation

Each report analysis costs approximately:
- Input: ~4,000 tokens (skill references + report)
- Output: ~2,000 tokens (analysis)
- **~$0.05 per report** (Claude Sonnet 4)

**Example:** 100 reports = ~$5.00

---

## Method 3: What NOT to Do ❌

### DON'T Ask Claude to Generate a Script

**❌ WRONG:**
```bash
claude "Write a Python script to evaluate 100 colorectal reports for compliance"
```

**Why this is bad:**
- Claude generates a **regex-based** script
- **NO LLM intelligence** - just keyword matching
- Can't understand context, variations, or nuances
- Defeats the purpose of having intelligent skills

**Example of what you get (BAD):**
```python
# Regex-only - no intelligence
if 'adenokarsinom' in text:
    score += 15
if re.search(r'\d+\s*cm', text):
    score += 15
```

**✅ CORRECT:**
```bash
claude "Use colorectal-pathology-specialist to analyze these reports with full LLM intelligence"
```

This uses Claude's contextual understanding!

---

## Comparison: Regex vs LLM Intelligence

### Regex Approach (Generated Script - BAD)

```
Report: "Tümör 1.2cm, grade 2, pT3 N1 M0"

Regex analysis:
✓ Found "cm" - tumor size present (+15)
✓ Found "pT3" - staging present (+15)
✓ Found "N1" - nodes present (+15)
Score: 100/100 ✅ COMPLIANT

BUT MISSED: pT3 requires tumor >5cm, not 1.2cm!
This is a staging ERROR that regex can't catch.
```

### LLM Approach (Using Skill - GOOD)

```
Report: "Tümör 1.2cm, grade 2, pT3 N1 M0"

LLM analysis:
✓ Tumor size: 1.2cm documented
✓ Grade: 2 documented
✗ INCONSISTENCY: pT3 requires tumor invasion beyond
  muscularis propria OR size >5cm. Report shows 1.2cm
  which should be pT1, not pT3.

Score: 75/100 ⚠️ MAJOR ISSUE
Recommendation: Verify pT category against actual
invasion depth and tumor size.
```

**LLM understands context and catches errors!**

---

## Excel File Format Requirements

### Batch Mode (One Report Per Row)

| report_text | patient_id | tumor_type |
|-------------|------------|------------|
| PATHOLOGY REPORT<br>Specimen: Right hemicolectomy<br>... | P12345 | colorectal |
| PATHOLOGY REPORT<br>Specimen: Sigmoid resection<br>... | P12346 | colorectal |

**Required column:** `report_text`
**Optional columns:** `patient_id`, `tumor_type`, `case_no`

### Structured Mode (Field-Value Pairs)

| Field | Value |
|-------|-------|
| Specimen Type | Right hemicolectomy |
| Tumor Site | Cecum |
| Tumor Size | 4.5 cm |
| Grade | G2 |
| pT Category | pT3 |

Auto-detected based on column layout.

---

## Output Formats

### Excel Output Structure

```
compliance_results.xlsx
├─ Sheet: Summary
│  ├─ Total Reports Processed
│  ├─ Average Compliance Score
│  ├─ Reports by Category
│  └─ Common Missing Elements
│
├─ Sheet: Detailed Results
│  ├─ Case ID
│  ├─ Compliance Score
│  ├─ Status (Compliant/Minor/Major/Critical)
│  ├─ Missing Elements
│  ├─ Cross-validation Issues
│  ├─ Recommendations
│  └─ Full Analysis
│
└─ Sheet: Failed Reports
   └─ Reports that couldn't be processed
```

### Text Output (Individual Files)

```
results/
├─ report_001_analysis.txt
├─ report_002_analysis.txt
├─ ...
└─ summary.xlsx
```

---

## Performance Guidelines

### Claude CLI

- **Small batches (1-50):** Single conversation
- **Medium batches (50-100):** Single conversation with checkpoints
- **Large batches (100+):** File-by-file loop with rate limiting

### Python API Script

- **Rate limit:** ~50 requests/minute (default)
- **Parallel processing:** Not recommended (respect rate limits)
- **Cost monitoring:** Check console.anthropic.com/usage

---

## Troubleshooting

### "I got a regex script instead of LLM analysis"

**Problem:** You asked Claude to "write a script" instead of "use the skill"

**Solution:**
```bash
# ❌ Wrong
claude "Write a Python script to check compliance"

# ✅ Right
claude "Use compliance-checker skill to analyze these reports"
```

### "API key not found" error with Python script

**Problem:** Environment variable not set

**Solution:**
```bash
export ANTHROPIC_API_KEY="sk-ant-api03-..."
# Add to ~/.bashrc or ~/.zshrc for persistence
```

### "Output is just keyword matching"

**Problem:** Not using the skill correctly

**Solution:** Explicitly mention the skill name in your prompt:
```bash
claude "Using breast-pathology-specialist skill, analyze..."
```

### Excel file not reading properly

**Problem:** Wrong format or missing column

**Solution:** Ensure Excel has either:
- `report_text` column (batch mode), OR
- Two-column field-value layout (structured mode)

---

## Best Practices

1. **Use Claude CLI for most cases** - It's simpler and free (already authenticated)
2. **Be explicit about using skills** - Mention skill name in prompt
3. **Request structured output** - Ask for Excel export explicitly
4. **Handle errors gracefully** - Some reports may fail (malformed, empty)
5. **Validate results** - Spot-check a few reports to ensure quality
6. **Monitor costs** - If using API script, track usage

---

## Examples by Use Case

### Quality Assurance Department

```bash
# Weekly QA check of all colorectal reports
claude "Analyze weekly_colorectal_reports.xlsx using colorectal-pathology-specialist. Generate QA dashboard with:
- Compliance rate by pathologist
- Most common missing elements
- Trending issues
Export to QA_dashboard_week_XX.xlsx"
```

### Research/Retrospective Study

```bash
# Analyze historical reports for study
claude "Process historical_breast_cases.xlsx (500 reports from 2020-2024) using breast-pathology-specialist. Focus on:
- ER/PR/HER2 reporting completeness
- TNM staging accuracy
- Biomarker documentation trends
Export to research_analysis.xlsx"
```

### Training/Education

```bash
# Review resident reports for teaching
claude "Evaluate resident_reports_month.xlsx using pathology-compliance-checker. For each report:
- Identify learning opportunities
- Suggest improvements
- Rate report quality
Export to resident_feedback.xlsx"
```

---

**Bottom Line:** Use Claude CLI directly for batch processing - it's simpler, free, and uses full LLM intelligence. Only use Python API scripts if you don't have Claude CLI.
