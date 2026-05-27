# Getting Started with Pathology Skills Collection

Complete guide to installing, configuring, and using the pathology skills collection for surgical pathology quality assurance and workflow optimization.

---

## 💡 Usage Modes Overview

### Single Report (Primary Use - No Python!) ✅

**Most users will only need the Claude CLI** - no Python, no scripting, no setup:

```bash
# Check a report - just pipe the file!
claude "Check this breast report for CAP compliance using breast-pathology-specialist" < report.txt

# Generate a template - just ask!
claude "Generate colorectal resection template using pathology-template-generator"

# Calculate staging - simple question!
claude "What stage is pT2 N1 M0 for pancreas cancer using tnm-stage-calculator?"
```

This is the **recommended workflow** for:
- Pathologists checking individual reports
- Residents learning CAP guidelines
- Quick template generation
- Pre-sign-out validation

---

### Batch Processing Multiple Reports

**✅ RECOMMENDED: Claude CLI Direct (No API key needed)**

```bash
# Process Excel with 100 reports - Claude analyzes each with LLM intelligence
claude "Read reports.xlsx and use colorectal-pathology-specialist to analyze each report. Export results to Excel with compliance scores."

# Process all files in directory
claude "Analyze all .txt files in reports_dir/ using pathology-compliance-checker and export to summary.xlsx"

# Use helper script
./batch_process_cli.sh reports.xlsx breast-pathology-specialist results/
```

**Key Points:**
- Uses your existing Claude CLI authentication (no API key)
- Full LLM intelligence (not regex matching)
- Ask Claude to use the skill - don't ask it to generate a script!

**⚠️ ALTERNATIVE: Python API Script (Requires ANTHROPIC_API_KEY)**

Only if you DON'T have Claude CLI:
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
python scripts/process_skill.py --skill pathology-compliance-checker reports.xlsx
```

**See [BATCH_PROCESSING.md](BATCH_PROCESSING.md) for complete guide.**

---

## Table of Contents

- [Installation Methods](#installation-methods)
  - [Method 1: Local Setup (Fastest)](#method-1-local-setup-fastest---recommended-for-development-)
  - [Method 2: Claude Code CLI Marketplace](#method-2-claude-code-cli-marketplace-future)
  - [Method 3: Clone from GitHub](#method-3-clone-from-github)
  - [Method 4: Cursor IDE Integration](#method-4-cursor-ide-integration)
  - [Method 5: MCP Server](#method-5-mcp-server-coming-soon)
- [Skill Selection Guide](#skill-selection-guide)
- [Quick Start Examples](#quick-start-examples)
- [Batch Processing Setup](#batch-processing-setup)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)

💡 **Quick Reference:** See [QUICK_START_LOCAL.md](../QUICK_START_LOCAL.md) for local usage examples and common commands.

---

## Installation Methods

### Method 1: Local Setup (Fastest - Recommended for Development) ⚡

**If you already have the repository cloned locally:**

#### Automated Setup (Easiest)

```bash
# Navigate to collection
cd /path/to/pathology-skills-collection

# Run one-time setup script
./setup_local.sh
```

**What this does:**
- ✅ Creates symlink: `~/.claude/skills/pathology-skills-collection`
- ✅ Verifies all 10 skills are present
- ✅ Checks shared references exist
- ✅ Runs a test to confirm it works
- ✅ Lets you use skills from any directory

**After setup, use from anywhere:**
```bash
cd ~/Desktop
claude "Check this colorectal report using colorectal-pathology-specialist" < report.txt
```

---

#### Manual Setup (If You Prefer)

```bash
# Create Claude skills directory if needed
mkdir -p ~/.claude/skills

# Create symlink to your collection
ln -s /path/to/pathology-skills-collection ~/.claude/skills/pathology-skills-collection

# Verify the link
ls -la ~/.claude/skills/
```

**Now use from any directory:**
```bash
cd ~/anywhere
claude "Check report using colorectal-pathology-specialist" < report.txt
```

---

#### No Setup Required (Simplest)

Don't want to create a symlink? Just navigate to the collection:

```bash
# Navigate to collection directory
cd /path/to/pathology-skills-collection

# Use skills directly
claude "Check using colorectal-pathology-specialist" < report.txt
```

**This works immediately** - no setup needed!

---

### Method 2: Claude Code CLI Marketplace (Future)

**Prerequisites:**
- Claude Code CLI installed
- Active Anthropic API account

**Installation:**
```bash
# Add this collection to your Claude Code marketplace
/plugin marketplace add yourusername/pathology-skills-collection

# Install entire collection (all 10 skills)
/plugin install pathology-skills@pathology-skills-collection

# Or install specific skills individually
/plugin install pathology-compliance-checker@pathology-skills-collection
/plugin install breast-pathology-specialist@pathology-skills-collection
```

**Updating later:**
```bash
/plugin update          # pull the latest version from the marketplace
/reload-plugins         # apply the update to the current session
```

`/plugin update` only downloads — it does not activate the new version in
your current session. Run `/reload-plugins` afterwards to pick up the
changes (skills, agents, hooks, plugin MCP servers) without restarting
Claude Code. A new Claude Code session loads updates automatically.

**Verify installation:**
```bash
# List installed skills
claude skills list

# Should show:
# - pathology-compliance-checker
# - pathology-template-generator
# - tnm-stage-calculator
# - pathology-coder
# - pathology-tumor-board-summary
# - pathology-report-converter
# - breast-pathology-specialist
# - colorectal-pathology-specialist
# - pancreas-pathology-specialist
# - gastric-pathology-specialist
```

---

### Method 3: Clone from GitHub

**Step 1: Clone Repository**
```bash
cd ~/Documents
git clone https://github.com/yourusername/pathology-skills-collection.git
```

**Step 2: Copy to Claude Skills Directory**
```bash
# Create skills directory if it doesn't exist
mkdir -p ~/.claude/skills

# Option A: Copy entire collection
cp -r pathology-skills-collection ~/.claude/skills/

# Option B: Create symlink (recommended for development)
ln -s ~/Documents/pathology-skills-collection ~/.claude/skills/pathology-skills
```

**Step 3: Verify Installation**
```bash
# Check that skills are recognized
claude skills list

# Or test a skill directly
claude "Check this report for compliance using pathology-compliance-checker" < sample_report.txt
```

---

### Method 4: Cursor IDE Integration

**Step 1: Open Cursor Settings**
- Launch Cursor IDE
- Go to Settings (Cmd+, on Mac, Ctrl+, on Windows)
- Navigate to "Claude Skills" section

**Step 2: Add Skills Path**
- Click "Add Skills Directory"
- Browse to: `/path/to/pathology-skills-collection/pathology-skills/`
- Click "Add"

**Step 3: Reload Claude**
- Restart Cursor or reload Claude integration
- Skills should appear in Claude sidebar

**Step 4: Test Skills**
- Open a pathology report file
- Right-click → "Ask Claude" → Select skill from dropdown
- Or use inline chat: `@pathology-compliance-checker check this report`

---

### Method 5: MCP Server (Coming Soon)

Hosted MCP server endpoint will allow skills to be accessed without local installation.

**Preview usage:**
```bash
# Add MCP server
claude mcp add pathology-skills https://mcp.pathology-skills.example.com

# Use skills via MCP
claude "Check compliance" --mcp pathology-skills
```

---

## Skill Selection Guide

### Decision Tree: Which Skill Should I Use?

```
START: What do you want to do?

├─ Check report quality/compliance?
│  ├─ General (any tumor type) → pathology-compliance-checker
│  ├─ Breast only → breast-pathology-specialist
│  ├─ Colorectal only → colorectal-pathology-specialist
│  ├─ Pancreas only → pancreas-pathology-specialist
│  └─ Gastric only → gastric-pathology-specialist
│
├─ Generate synoptic template?
│  ├─ Blank template → pathology-template-generator
│  ├─ Pre-filled template → pathology-template-generator (with values)
│  └─ Tumor-specific → Use specialist skill
│
├─ Calculate TNM stage?
│  └─ Quick lookup → tnm-stage-calculator
│
├─ Get SNOMED/ICD-O-3 codes?
│  └─ Any diagnosis → pathology-coder
│
├─ Create tumor board summary?
│  └─ MDT meeting → pathology-tumor-board-summary
│
├─ Convert narrative to synoptic?
│  └─ Old reports → pathology-report-converter
│
└─ All features for one tumor type?
   ├─ Breast → breast-pathology-specialist
   ├─ Colorectal → colorectal-pathology-specialist
   ├─ Pancreas → pancreas-pathology-specialist
   └─ Gastric → gastric-pathology-specialist
```

---

### Skill Comparison Matrix

| Feature | Core Skills | Specialist Skills |
|---------|-------------|-------------------|
| **Compliance Checking** | pathology-compliance-checker (all tumors) | breast/colorectal/pancreas/gastric-pathology-specialist |
| **Template Generation** | pathology-template-generator (all tumors) | breast/colorectal/pancreas/gastric-pathology-specialist |
| **TNM Staging** | tnm-stage-calculator (quick lookup) | breast/colorectal/pancreas/gastric-pathology-specialist |
| **SNOMED Coding** | pathology-coder (all diagnoses) | breast/colorectal/pancreas/gastric-pathology-specialist |
| **Tumor Board Summaries** | pathology-tumor-board-summary (all tumors) | breast/colorectal/pancreas/gastric-pathology-specialist |
| **Report Conversion** | pathology-report-converter (all tumors) | Not included in specialists |
| **Tumor-Specific Focus** | General purpose | Highly specialized |
| **Best For** | Mixed caseload, flexibility | Dedicated pathologists, high volume |

---

### Use Case Recommendations

#### Scenario 1: General Pathology Department
**Recommended skills:** All 6 core skills
```bash
/plugin install pathology-compliance-checker@pathology-skills-collection
/plugin install pathology-template-generator@pathology-skills-collection
/plugin install tnm-stage-calculator@pathology-skills-collection
/plugin install pathology-coder@pathology-skills-collection
/plugin install pathology-tumor-board-summary@pathology-skills-collection
/plugin install pathology-report-converter@pathology-skills-collection
```

**Why:** Handles all tumor types, flexible for diverse caseload

---

#### Scenario 2: Breast Cancer Center
**Recommended skills:** breast-pathology-specialist + tnm-stage-calculator
```bash
/plugin install breast-pathology-specialist@pathology-skills-collection
/plugin install tnm-stage-calculator@pathology-skills-collection
```

**Why:** Comprehensive breast toolkit, quick staging lookup

---

#### Scenario 3: GI Pathology Fellowship
**Recommended skills:** colorectal-pathology-specialist + gastric-pathology-specialist + pancreas-pathology-specialist
```bash
/plugin install colorectal-pathology-specialist@pathology-skills-collection
/plugin install gastric-pathology-specialist@pathology-skills-collection
/plugin install pancreas-pathology-specialist@pathology-skills-collection
```

**Why:** All GI tumor types covered, excellent for training

---

#### Scenario 4: Pathology Resident Training
**Recommended skills:** All 10 skills (entire collection)
```bash
/plugin install pathology-skills@pathology-skills-collection
```

**Why:** Learn all features, practice with different tumor types

---

## Quick Start Examples

### Example 1: Check Breast Report Compliance

```bash
# Save your report to a file
cat > breast_report.txt << 'EOF'
FINAL DIAGNOSIS:
Left breast, lumpectomy:
- Invasive ductal carcinoma, Grade 2
- Tumor size: 2.3 cm
- Margins negative, closest 3mm anterior
- Sentinel lymph nodes: 2/15 positive
- ER positive (90%), PR positive (70%), HER2 negative
- Stage: pT2 N1a M0 (Stage IIB)
EOF

# Run compliance check
claude "Check this breast report for CAP compliance using pathology-compliance-checker" < breast_report.txt
```

**Expected output:**
```
BREAST CANCER COMPLIANCE ANALYSIS
Score: 85/100 (INCOMPLETE - MINOR)

MISSING ELEMENTS:
🟠 MAJOR (2):
  - LVI status (-5 points)
  - Ki-67 proliferation index (-5 points)

🟡 MINOR (1):
  - Tumor focality (-2 points)

CROSS-VALIDATION:
✅ pT2 consistent with 2.3cm tumor
✅ pN1a consistent with 2 positive nodes
✅ ER/PR/HER2 reported per ASCO/CAP

RECOMMENDATIONS:
1. Add LVI status (MAJOR)
2. Add Ki-67 for treatment planning
```

---

### Example 2: Generate Blank Template

```bash
# Generate blank lumpectomy template
claude "Generate a blank breast lumpectomy synoptic template using pathology-template-generator"
```

**Expected output:**
```
═══════════════════════════════════════
BREAST - INVASIVE CARCINOMA
Synoptic Report Template
═══════════════════════════════════════

CLINICAL INFORMATION
───────────────────────────────────────
Clinical History: _______________
Laterality: (_) Right  (_) Left
...
[Full template]
```

---

### Example 3: Calculate TNM Stage

```bash
# Quick staging lookup
claude "What stage is pT2 N1 M0 for breast cancer using tnm-stage-calculator?"
```

**Expected output:**
```
BREAST CANCER STAGING (AJCC 8TH)

pT2 (tumor >2cm, ≤5cm)
+ N1 (1-3 positive nodes)
+ M0 (no distant metastasis)
= Stage IIB

Treatment Implications:
- Adjuvant chemotherapy likely
- Endocrine therapy if ER/PR+
- Radiation post-lumpectomy
```

---

### Example 4: Get SNOMED Codes

```bash
# Get codes for diagnosis
claude "What's the SNOMED code for invasive ductal carcinoma using pathology-coder?"
```

**Expected output:**
```
SNOMED CT AND ICD-O-3 CODES

Morphology:
  SNOMED CT: 408643008 - Infiltrating duct carcinoma
  ICD-O-3: 8500/3

Topography:
  ICD-O-3: C50.9 - Breast, unspecified

Combined: 8500/3 - C50.9
```

---

### Example 5: Generate Tumor Board Summary

```bash
# Create MDT summary
claude "Generate tumor board summary from this report using pathology-tumor-board-summary" < breast_report.txt
```

**Expected output:**
```
52F with invasive breast carcinoma, left breast.
Lumpectomy: 2.3cm Grade 2 invasive ductal carcinoma, pT2 N1a M0 (Stage IIB).
Margins: Negative (closest 3mm). Nodes: 2/15 positive.
Receptors: ER 90%, PR 70%, HER2 negative.
Resection: R0.
```

---

## Configuration

### Environment Variables

Set these in your shell profile (`~/.bashrc`, `~/.zshrc`, etc.):

```bash
# Anthropic API key (required for batch processing)
export ANTHROPIC_API_KEY="sk-ant-..."

# Default tumor type (optional)
export PATHOLOGY_DEFAULT_TUMOR_TYPE="breast"

# Default language (optional)
export PATHOLOGY_DEFAULT_LANGUAGE="en"  # or "tr" for Turkish
```

---

### Custom Skill Settings

Create `~/.claude/pathology-skills-config.json`:

```json
{
  "default_skill": "pathology-compliance-checker",
  "compliance_threshold": 90,
  "auto_suggest_staging": true,
  "preferred_language": "en",
  "tumor_type_hints": true,
  "verbose_output": false
}
```

---

### Batch Processing Setup (Optional - Advanced Users Only)

⚠️ **Most users don't need this!** For single reports, just use: `claude "Check using [skill]" < report.txt`

For processing **many reports** (50+), choose based on your needs:

---

#### Option A: Simple Bash Loop (Recommended for Batch)

**No Python required** - just use a simple bash loop:

```bash
#!/bin/bash
# batch_check.sh

# Process all reports in a directory
for report in /path/to/reports/*.txt; do
  echo "Processing $(basename $report)..."
  claude "Check CAP compliance using pathology-compliance-checker" < "$report" \
    > "results/$(basename $report .txt)_analysis.txt"
done

echo "Done! Results saved to results/"
```

**Run it:**
```bash
chmod +x batch_check.sh
./batch_check.sh
```

**Benefits:**
- ✅ Simple, no dependencies
- ✅ Works with any Claude CLI installation
- ✅ Easy to understand and modify
- ✅ Each report gets individual analysis

**Limitations:**
- ❌ No aggregate statistics (average score, gap frequency)
- ❌ No Excel export
- ❌ No trend analysis

---

#### Option B: Python for Advanced Analytics (Optional)

**Only use if you need:** aggregate statistics, Excel export, trend analysis, custom reporting

**Step 1: Install Dependencies**
```bash
pip install anthropic openpyxl pandas
```

**Step 2: Use Example Script**
See `tests/test_colorectal_excel_analysis.py` for a complete example, or see `docs/examples.md` for more batch processing templates.

**Step 3: Set API Key**
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

**Benefits:**
- ✅ Aggregate statistics (average score, gap frequency)
- ✅ Excel/CSV export
- ✅ Trend analysis over time
- ✅ Custom dashboards

**Complexity:**
- ❌ Requires Python programming
- ❌ More setup and dependencies
- ❌ Overkill for most use cases

---

## Troubleshooting

### Issue: Skills Not Recognized

**Symptoms:**
```bash
$ claude skills list
Error: No skills found
```

**Solutions:**

1. **Check installation path:**
   ```bash
   ls ~/.claude/skills/
   # Should show pathology-skills or individual skill folders
   ```

2. **Verify SKILL.md files exist:**
   ```bash
   find ~/.claude/skills -name "SKILL.md"
   # Should list all skill definition files
   ```

3. **Check YAML frontmatter:**
   ```bash
   head -n 5 ~/.claude/skills/pathology-skills-collection/pathology-skills/pathology-compliance-checker/SKILL.md
   # Should show:
   # ---
   # name: pathology-compliance-checker
   # description: ...
   # ---
   ```

4. **Reload Claude:**
   ```bash
   claude reload
   ```

---

### Issue: Skill Errors During Execution

**Symptoms:**
```
Error: Cannot find reference file
Error: Invalid template
```

**Solutions:**

1. **Check shared-references exists:**
   ```bash
   ls ~/.claude/skills/pathology-skills-collection/shared-references/
   ```

2. **Verify relative paths:**
   ```bash
   # Skills should be at same level as shared-references
   ~/.claude/skills/pathology-skills-collection/pathology-skills/
   ├── pathology-compliance-checker/
   ├── pathology-template-generator/
   └── ...
   ~/.claude/skills/pathology-skills-collection/shared-references/
   ├── staging/
   ├── templates/
   └── ...
   ```

3. **Re-install with correct structure:**
   ```bash
   # Remove old installation
   rm -rf ~/.claude/skills/pathology-skills-collection

   # Clone fresh copy to home directory
   cd ~
   git clone https://github.com/sbalci/pathology-skills-collection.git
   ln -s ~/pathology-skills-collection ~/.claude/skills/pathology-skills-collection
   ```

---

### Issue: Turkish Language Not Working

**Symptoms:**
- Templates always in English
- Turkish terminology not recognized

**Solutions:**

1. **Specify language explicitly:**
   ```bash
   claude "Türkçe meme lumpektomi şablonu oluştur using pathology-template-generator"
   ```

2. **Check Turkish template files exist:**
   ```bash
   ls ~/.claude/skills/pathology-skills-collection/shared-references/templates/
   # Should show synoptic_templates_tr.md
   ```

3. **Use Turkish skill name if available:**
   ```bash
   # Use Turkish terms in request
   claude "Şu raporu CAP uyumluluğu için kontrol et" < rapor.txt
   ```

---

### Issue: Batch Processing Fails

**Symptoms:**
- API errors
- Rate limiting
- Timeout errors

**Solutions:**

1. **Check API key:**
   ```bash
   echo $ANTHROPIC_API_KEY
   # Should show: sk-ant-...
   ```

2. **Add rate limiting:**
   ```python
   import time

   for report in reports:
       process_report(report)
       time.sleep(1)  # Wait 1 second between requests
   ```

3. **Handle timeouts:**
   ```python
   from anthropic import Anthropic

   client = Anthropic(
       api_key=os.environ["ANTHROPIC_API_KEY"],
       timeout=120.0  # 2 minutes
   )
   ```

---

### Issue: Compliance Scores Too Low

**Symptoms:**
- Reports score <70% but appear complete
- Missing elements flagged incorrectly

**Solutions:**

1. **Check terminology mapping:**
   - Skill recognizes standard CAP terminology
   - Synonyms are mapped (e.g., "IDC" = "invasive ductal carcinoma")
   - Non-standard terms may not be recognized

2. **Review reference files:**
   ```bash
   # Check what terms are recognized
   cat ~/.claude/skills/.../references/diagnosis/breast_invasive_carcinoma.md
   ```

3. **Use standardized terminology:**
   - "Invasive ductal carcinoma" instead of "IDC"
   - "Lymphovascular invasion" instead of "vascular invasion"
   - Full CAP-compliant phrasing

---

## Next Steps

1. **Read [Skill Reference](pathology-skills.md)** for detailed documentation of each skill
2. **Review [Examples](examples.md)** for complete workflow examples
3. **Check [Migration Guide](migration-guide.md)** if upgrading from legacy skill
4. **Explore individual SKILL.md files** in each skill directory for advanced features

---

## Support

- **Issues:** https://github.com/yourusername/pathology-skills-collection/issues
- **Discussions:** https://github.com/yourusername/pathology-skills-collection/discussions
- **Email:** pathology-skills@example.com

---

Ready to transform your pathology workflow!
