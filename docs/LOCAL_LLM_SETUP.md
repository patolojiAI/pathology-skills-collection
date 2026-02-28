# Using Local LLMs for Pathology Report Checking

Run pathology report compliance checks locally without sending data to the cloud.

    python scripts/check_report.py -p lmstudio "Check compliance" < samples/colorectal_complete_en.txt
    python scripts/check_report.py -p ollama "Check compliance" < samples/breast_complete_en.txt



**Available Scripts:**
- `check_report.py` - Single report analysis
- `batch_checker.py` - Batch processing multiple reports

---

## Prerequisites

- Python 3.8+
- `openai` package: `pip install openai`
- One of: **Ollama** or **LM Studio**

---

## Option A: Ollama Setup

### 1. Install Ollama

Download from https://ollama.com/download

### 2. Download a Model

```bash
ollama pull qwen2.5:3b          # Small (~2GB)
ollama pull llama3.1:8b         # Medium (~5GB)
ollama pull qwen2.5:14b         # Large (~9GB)
```

### 3. Run

```bash
# Single report
python scripts/check_report.py -p ollama -m qwen2.5:3b "Check compliance" < report.txt

# Batch processing
python scripts/batch_checker.py reports/ output/ -p ollama -m qwen2.5:3b
```

> **Model selection with Ollama:** You must specify the model with `-m` since Ollama can serve any downloaded model on demand. Use `ollama list` or `--list-models` to see what's available.

---

## Option B: LM Studio Setup

### 1. Install LM Studio

Download from https://lmstudio.ai

### 2. Download a Model

- Open LM Studio
- Search for `Qwen2.5-3B-Instruct-GGUF` or similar
- Download a `Q4_K_M` or `Q5_K_M` quantization

### 3. Configure Context Length

**Important:** The skill requires ~17,000 tokens context.

1. Go to **Local Server** tab
2. Set **Context Length** to `32768`
3. **Load the model** (this is what makes it available to the API)
4. Click **Start Server**

### 4. Run

```bash
# Single report
python scripts/check_report.py -p lmstudio "Check compliance" < report.txt

# Batch processing
python scripts/batch_checker.py reports/ output/ -p lmstudio
```

### How Model Selection Works in LM Studio

LM Studio's local server only responds with models that are **loaded into memory** — not just downloaded to disk. The script auto-detects which model(s) are loaded:

| Scenario | What happens |
|---|---|
| **One model loaded** | Auto-detected and used automatically |
| **Multiple models loaded** | First model is used; a warning lists all available models |
| **No model loaded** | Error with instructions to load a model |

To target a specific model when multiple are loaded:

```bash
python scripts/check_report.py -p lmstudio -m "qwen2.5-3b-instruct" "Check compliance" < report.txt
```

---

## Listing Available Models

Check which models are available before running:

```bash
# List models loaded in LM Studio
python scripts/check_report.py -p lmstudio --list-models
python scripts/batch_checker.py -p lmstudio --list-models

# List models available in Ollama
python scripts/check_report.py -p ollama --list-models
python scripts/batch_checker.py -p ollama --list-models
```

---

## Single Report Examples (check_report.py)

```bash
# Basic compliance check
python scripts/check_report.py -p lmstudio "Check compliance" < report.txt

# Specify tumor type
python scripts/check_report.py -p ollama -m qwen2.5:3b -t breast "Check compliance" < report.txt

# Specify a particular LM Studio model
python scripts/check_report.py -p lmstudio -m "qwen2.5-3b-instruct" "Check compliance" < report.txt

# Output to file
python scripts/check_report.py -p lmstudio "Check compliance" < report.txt > result.txt

# Quiet mode (no progress messages)
python scripts/check_report.py -p lmstudio -q "Check compliance" < report.txt

# Use file argument instead of stdin
python scripts/check_report.py -p lmstudio --file report.txt "Check compliance"
```

---

## Batch Processing Examples (batch_checker.py)

Process multiple reports in a directory:

```bash
# Basic batch processing
python scripts/batch_checker.py /path/to/reports /path/to/output -p lmstudio

# With Ollama and specific model
python scripts/batch_checker.py reports/ output/ -p ollama -m qwen2.5:3b

# Specify tumor type for all reports
python scripts/batch_checker.py reports/ output/ -p lmstudio -t breast

# With specific LM Studio model
python scripts/batch_checker.py reports/ output/ -p lmstudio -m "qwen2.5-3b-instruct"
```

### Batch Output Files

After batch processing, the output directory contains:

```
output/
├── individual_reports/     # Per-report QA results
│   ├── report1_qa.txt
│   ├── report2_qa.txt
│   └── ...
├── summary_report.txt      # Overall statistics
├── compliance_data.csv     # Structured data (spreadsheet)
├── compliance_data.xlsx    # Excel workbook (if openpyxl installed)
└── trend_history.json      # Historical tracking data
```

### Batch Processing Performance

Local LLMs are slower than cloud APIs. Expected processing times per report:

| Model Size | Time per Report | 20 Reports |
|------------|-----------------|------------|
| 3B (Qwen2.5-3B) | 1-3 minutes | 20-60 min |
| 8B (Llama-3.1-8B) | 2-5 minutes | 40-100 min |
| 14B+ | 3-8 minutes | 60-160 min |

> **Tip:** For large batches, consider running overnight or using a larger/faster GPU.

---

## Environment Variables

Set defaults to avoid typing flags:

```bash
# Windows
set LLM_PROVIDER=lmstudio
set LMSTUDIO_MODEL=qwen2.5-3b-instruct
set OLLAMA_MODEL=qwen2.5:3b

# Linux/Mac
export LLM_PROVIDER=lmstudio
export LMSTUDIO_MODEL=qwen2.5-3b-instruct
export OLLAMA_MODEL=qwen2.5:3b

# Then just run:
python scripts/check_report.py "Check compliance" < report.txt
python scripts/batch_checker.py reports/ output/
```

---

## Recommended Models

| Model | Size | RAM Needed | Quality | Speed |
|---|---|---|---|---|
| Qwen2.5-3B-Instruct | ~2GB | 8GB | Acceptable | Fast |
| Llama-3.1-8B-Instruct | ~5GB | 12GB | Good | Medium |
| Qwen2.5-14B-Instruct | ~9GB | 20GB | Very Good | Slow |
| Qwen2.5-32B-Instruct | ~20GB | 40GB | Excellent | Very Slow |

For batch processing, balance quality vs. time based on your needs.

---

## Troubleshooting

### "Model not found"

```
Error: model 'llama3.1:70b' not found
```

**Fix:** Download the model first or specify the correct model name:

```bash
ollama list                    # See available models
ollama pull qwen2.5:3b         # Download model

# Or list models programmatically:
python scripts/check_report.py -p ollama --list-models
```

### "No models loaded in LM Studio"

```
Error: No models loaded in LM Studio.
```

**Fix:** Open LM Studio → Local Server tab → Load a model → Start Server.

### "Multiple models loaded" warning

```
Multiple models available in lmstudio:
  1. qwen2.5-3b-instruct
  2. llama-3.1-8b-instruct
Using first available model: qwen2.5-3b-instruct
```

**Fix:** Specify which model to use with `-m`:

```bash
python scripts/check_report.py -p lmstudio -m "llama-3.1-8b-instruct" "Check compliance" < report.txt
```

### "Context length too small"

```
Error: context length of only 4096 tokens
```

**Fix:** Increase context length to 32768 in LM Studio settings, then reload the model.

### "openai package not installed"

```
Error: openai package not installed
```

**Fix:** Install the package:

```bash
pip install openai
```

### "Connection refused"

```
Error: Connection refused
```

**Fix:**
- **Ollama:** Ensure Ollama is running (`ollama serve`)
- **LM Studio:** Start the Local Server (Local Server tab → Start Server)

### "JSON parse error" during batch processing

```
Warning: Failed to parse JSON response
```

This can happen with smaller models. The report will be marked as ERROR and processing continues. Consider using a larger model for better reliability.

---

## Privacy Note

With Ollama or LM Studio:

- All processing happens on your machine
- No data is sent to external servers
- Models are downloaded once, then work offline
- Your pathology reports remain completely private
