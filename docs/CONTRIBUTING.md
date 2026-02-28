# Contributing to Pathology Skills Collection

Thank you for your interest in contributing to the Pathology Skills Collection! This document provides guidelines for contributing new skills, tumor types, features, and improvements.

## 🎯 Ways to Contribute

### 1. Add New Tumor Types
Expand existing skills to support additional tumor types (lung, prostate, uterine, ovarian, skin, kidney, etc.)

### 2. Create New Skills
- Molecular pathology skills (NGS, MSI/MMR, HER2 FISH, PD-L1)
- Cytopathology skills (Pap smear, thyroid FNA, body fluids)
- Laboratory management tools (QA tracking, TAT monitoring)

### 3. Improve Existing Skills
- Enhance validation logic
- Add cross-validation rules
- Update clinical guidelines
- Fix bugs

### 4. Add Language Support
- Translate templates and references to additional languages
- Currently supporting: English (EN), Turkish (TR)
- Needed: Spanish (ES), French (FR), German (DE), Chinese (ZH)

### 5. Improve Documentation
- Add examples and use cases
- Clarify installation instructions
- Create video tutorials

---

## 📋 Getting Started

### Prerequisites

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/pathology-skills-collection.git
   cd pathology-skills-collection
   ```
3. **Set up local development**:
   ```bash
   ./setup_local.sh
   pip install -r requirements.txt
   ```
4. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

---

## 🛠️ Adding a New Skill

### Step 1: Create Skill Directory

```bash
mkdir -p pathology-skills/your-skill-name
cd pathology-skills/your-skill-name
```

### Step 2: Create SKILL.md

Use this template structure:

```markdown
---
name: pathology-your-skill-name
description: Detailed description of what this skill does, when to use it, and what it supports
---

# Your Skill Name

Brief introduction to the skill.

## Supported Tumor Types
List supported tumors

## Supported Input Formats
- Text (.txt, .md)
- Excel (.xlsx, .xls)
- PDF (.pdf)
- Images (.jpg, .png, .tiff)

## Reference Files
List reference files used

## Usage Examples
Provide clear examples

## Output Format
Describe output structure
```

### Step 3: Add Reference Files

Create tumor-specific references:

```bash
mkdir -p references/diagnosis
mkdir -p references/macroscopy

# Add your reference markdown files
```

Reference files should follow CAP/ICCR/AJCC/WHO guidelines. Include:
- Required elements
- Optional elements
- Validation rules
- Staging criteria

### Step 4: Update marketplace.json

Add your skill to the `skills` array:

```json
{
  "name": "your-skill-name",
  "displayName": "Your Skill Display Name",
  "description": "Brief description",
  "path": "pathology-skills/your-skill-name",
  "entryPoint": "SKILL.md",
  "tumors": ["breast", "colorectal"],
  "features": ["validation", "staging"],
  "tags": ["CAP", "TNM"]
}
```

### Step 5: Test Your Skill

```bash
# Test with Claude CLI
claude "Test query using your-skill-name" < test-report.txt

# Test with batch processing
python scripts/process_skill.py --skill your-skill-name test.xlsx --output results/
```

### Step 6: Add Examples

Create example files in `examples/your-skill-name/`:
- Sample input reports
- Expected outputs
- Test cases

---

## 📚 Adding a New Tumor Type

To add support for a new tumor type to existing skills:

### 1. Add CAP/ICCR Reference

Create `pathology-skills/[skill-name]/references/diagnosis/[tumor]_carcinoma.md`:

```markdown
# [Tumor Type] Carcinoma - CAP Protocol

## Required Elements (Critical)
- Element 1
- Element 2

## Required Elements (Major)
- Element 3

## Optional Elements
- Element 4

## Validation Rules
- Cross-validation rule 1

## Scoring
- Critical: -15 points each
- Major: -5 points each
```

### 2. Add Macroscopy Guidelines

Create `pathology-skills/[skill-name]/references/macroscopy/[tumor]_macroscopy.md` following AAPA guidelines.

### 3. Add TNM Staging

Update `shared-references/staging/tnm_stage_calculator.md` with AJCC 8th edition staging tables.

### 4. Add Templates

Update `shared-references/templates/synoptic_templates.md` with CAP synoptic template.

### 5. Test Thoroughly

Test with real clinical cases for the new tumor type.

---

## 🌍 Adding Language Support

### 1. Translate Templates

Create language-specific template files:
- `synoptic_templates_[lang].md`
- `tumor_board_summary_[lang].md`

### 2. Update SKILL.md

Add language detection and reference file loading for new language.

### 3. Test Both Languages

Verify both English and the new language work correctly.

---

## ✅ Code Quality Guidelines

### Reference File Standards

1. **Follow clinical guidelines exactly**
   - CAP 2024 protocols
   - ICCR 2nd edition
   - AJCC 8th edition
   - WHO 5th edition

2. **Use clear markdown formatting**
   - Tables for element lists
   - Bullet lists for rules
   - Code blocks for examples

3. **Include validation logic**
   - Cross-validation rules
   - Consistency checks
   - Scoring weights

### Python Code Standards (for batch processing)

1. **Follow PEP 8** style guidelines
2. **Add docstrings** to all functions
3. **Handle errors gracefully** with try/except
4. **Use type hints** where applicable
5. **Add logging** for debugging

### Testing Requirements

1. **Test with real data** - Use actual pathology reports
2. **Test all formats** - Text, Excel, PDF, images
3. **Test edge cases** - Incomplete reports, missing data
4. **Verify cross-validation** - pT/pN/stage consistency
5. **Check both languages** - EN and TR (if applicable)

---

## 📝 Commit Guidelines

### Commit Message Format

```
type(scope): Brief description

Detailed explanation of changes (if needed)

Fixes #issue_number (if applicable)
```

**Types:**
- `feat`: New feature or skill
- `fix`: Bug fix
- `docs`: Documentation changes
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(breast-pathology-specialist): Add HER2 FISH reporting

docs(README): Update installation instructions

fix(compliance-checker): Correct pT3 validation for gastric

refactor(file_readers): Improve PDF extraction logic
```

---

## 🔄 Pull Request Process

### Before Submitting

- [ ] Code follows style guidelines
- [ ] All tests pass locally
- [ ] Documentation updated
- [ ] Examples added for new features
- [ ] CHANGELOG.md updated (if significant change)
- [ ] marketplace.json updated (if new skill)

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] New skill
- [ ] New tumor type support
- [ ] Bug fix
- [ ] Documentation update
- [ ] New language support

## Testing
- [ ] Tested with text files
- [ ] Tested with Excel/CSV
- [ ] Tested with PDF/images
- [ ] Tested with real pathology reports
- [ ] Both EN and TR languages work (if applicable)

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have commented complex code
- [ ] I have updated documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests
- [ ] All tests pass

## Screenshots (if UI changes)
[Add screenshots]

## Clinical Guidelines Verification
- [ ] Follows CAP 2024 protocols
- [ ] Follows AJCC 8th edition (if staging-related)
- [ ] References validated against official sources
```

### Review Process

1. **Automated checks** run on your PR
2. **Maintainer review** - typically within 3-5 days
3. **Revisions** if needed
4. **Approval and merge** when ready

---

## 🏆 Recognition

Contributors are recognized in:
- README.md contributors section
- CHANGELOG.md for their contributions
- GitHub contributors page

Significant contributors may be invited to become maintainers.

---

## 📞 Getting Help

- **Questions**: Open a [Discussion](https://github.com/sbalci/pathology-skills-collection/discussions)
- **Bugs**: Open an [Issue](https://github.com/sbalci/pathology-skills-collection/issues)
- **Ideas**: Start a [Discussion](https://github.com/sbalci/pathology-skills-collection/discussions)
- **Urgent**: Email serdarbalci@gmail.com

---

## 📖 Additional Resources

### Clinical Guidelines
- [CAP Cancer Protocols](https://www.cap.org/protocols-and-guidelines)
- [ICCR Datasets](https://www.iccr-cancer.org/)
- [AJCC Staging Manual](https://www.cancerstaging.org/)
- [SNOMED CT](https://www.snomed.org/)

### Development
- [Claude Skills Documentation](https://docs.anthropic.com/claude/docs)
- [MCP Protocol](https://modelcontextprotocol.io/)
- [Python Best Practices](https://docs.python-guide.org/)

---

## 📜 Code of Conduct

### Our Pledge

We pledge to make participation in this project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

**Positive behavior:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Unacceptable behavior:**
- Trolling, insulting/derogatory comments, personal or political attacks
- Public or private harassment
- Publishing others' private information without permission
- Other conduct which could reasonably be considered inappropriate

### Enforcement

Project maintainers are responsible for clarifying standards and will take appropriate action in response to unacceptable behavior.

### Reporting

Report violations to serdarbalci@gmail.com. All reports will be reviewed and investigated.

---

## 🙏 Thank You!

Your contributions help pathologists worldwide provide better patient care through standardized, high-quality pathology reporting.

Every contribution, no matter how small, makes a difference! 🎉
