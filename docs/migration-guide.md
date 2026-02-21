# Migration Guide

Guide for migrating from the legacy `pathology-report-checker` skill (v1.1.0) to the new `pathology-skills-collection` (v1.0.0+).

---

## Table of Contents

- [Why Migrate?](#why-migrate)
- [What Changed](#what-changed)
- [Skill Name Mapping](#skill-name-mapping)
- [Migration Paths](#migration-paths)
- [Breaking Changes](#breaking-changes)
- [Gradual Migration Strategy](#gradual-migration-strategy)
- [FAQ](#faq)

---

## Why Migrate?

### Benefits of the New Collection

**1. Modular Architecture**
- Old: Single comprehensive skill (~90K tokens)
- New: 10 focused skills (5-25K tokens each)
- **Result**: Faster loading, lower token usage per operation

**2. Specialized Skills**
- Old: Generic compliance checker for all tumor types
- New: Dedicated breast, colorectal, pancreas, gastric specialists
- **Result**: Tumor-specific features (HER2 for breast, MSI/MMR for colorectal, 7 margins for pancreas, Lauren for gastric)

**3. Better Organization**
- Old: All features in one skill
- New: Separate skills for different workflows (compliance, templates, staging, coding, summaries, conversion)
- **Result**: Easier to find and use specific features

**4. Shared Resources**
- Old: Duplicated reference files in single skill
- New: Shared-references architecture
- **Result**: Easier maintenance, consistent updates

**5. Marketplace Ready**
- Old: Single skill installation
- New: Install collection or individual skills
- **Result**: Flexibility to install only what you need

---

## What Changed

### Repository Structure

**Old (pathology-report-checker-skill):**
```
pathology-report-checker-skill/
├── SKILL.md (comprehensive, all features)
├── references/
│   ├── diagnosis/ (4 tumor types)
│   ├── macroscopy/ (4 tumor types)
│   ├── staging/
│   ├── templates/
│   ├── coding/
│   ├── summaries/
│   ├── converters/
│   ├── autofill/
│   ├── amendments/
│   └── biomarkers/
└── scripts/
    ├── batch_checker.py
    └── watch_folder.py
```

**New (pathology-skills-collection):**
```
pathology-skills-collection/
├── .claude-plugin/
│   └── marketplace.json (skill registry)
├── pathology-skills/ (10 separate skills)
│   ├── compliance-checker/
│   ├── template-generator/
│   ├── tnm-stage-calculator/
│   ├── pathology-coder/
│   ├── tumor-board-summary/
│   ├── report-converter/
│   ├── breast-pathology-specialist/
│   ├── colorectal-pathology-specialist/
│   ├── pancreas-pathology-specialist/
│   └── gastric-pathology-specialist/
├── shared-references/ (universal content)
│   ├── staging/
│   ├── templates/
│   ├── coding/
│   ├── biomarkers/
│   ├── common/
│   └── macroscopy/
└── docs/ (comprehensive documentation)
```

---

## Skill Name Mapping

### Old Skill → New Skills

| Old Skill (v1.1.0) | New Skill(s) (v1.0.0+) | Notes |
|--------------------|------------------------|-------|
| `pathology-report-checker` (compliance mode) | `pathology-compliance-checker` | Core compliance checking |
| `pathology-report-checker` (template mode) | `pathology-template-generator` | Template generation |
| `pathology-report-checker` (staging mode) | `tnm-stage-calculator` | Quick staging lookup |
| `pathology-report-checker` (all breast features) | `pathology-breast-pathology-specialist` | All-in-one breast toolkit |
| `pathology-report-checker` (all colorectal) | `pathology-colorectal-pathology-specialist` | All-in-one colorectal toolkit |
| `pathology-report-checker` (all pancreas) | `pathology-pancreas-pathology-specialist` | All-in-one pancreas toolkit |
| `pathology-report-checker` (all gastric) | `pathology-gastric-pathology-specialist` | All-in-one gastric toolkit |
| N/A (new feature) | `pathology-coder` | SNOMED/ICD-O-3 coding |
| N/A (new feature) | `pathology-tumor-board-summary` | Standalone summaries |
| N/A (new feature) | `pathology-report-converter` | Free-text conversion + amendments |

---

## Migration Paths

### Path 1: Full Migration (Recommended)

Install entire collection and switch completely.

**Step 1: Install New Collection**
```bash
# Uninstall old skill (optional, can keep during transition)
claude skills uninstall pathology-report-checker

# Install new collection
/plugin marketplace add yourusername/pathology-skills-collection
/plugin install pathology-skills@pathology-skills-collection
```

**Step 2: Update Scripts/Workflows**

Replace old skill invocations:
```bash
# Old
claude "Check this report" < report.txt

# New
claude "Check this report using compliance-checker" < report.txt
```

**Step 3: Test All Workflows**
- Run test cases
- Verify outputs match expected
- Update documentation

**Step 4: Decommission Old Skill**
```bash
# Archive old skill
mv ~/.claude/skills/pathology-report-checker ~/.claude/skills/ARCHIVED_pathology-report-checker

# Or fully uninstall
claude skills uninstall pathology-report-checker
```

**Timeline:** 1-2 weeks for full migration

---

### Path 2: Gradual Migration

Keep old skill, test new skills alongside.

**Week 1: Install and Test**
```bash
# Install new collection (keep old skill)
/plugin install pathology-skills@pathology-skills-collection

# Test new skills on known cases
claude "Check this breast report using breast-pathology-specialist" < test_breast_report.txt
claude "Check same report using pathology-report-checker" < test_breast_report.txt

# Compare outputs
```

**Week 2-3: Parallel Usage**
```bash
# Use old skill for production
claude "Check this report using pathology-report-checker" < production_report.txt

# Use new skills for new workflows
claude "Generate template using template-generator"
claude "Calculate stage using tnm-stage-calculator"
```

**Week 4-6: Phase-In New Skills**
```bash
# Start using new skills for specific tumor types
# Breast cases → breast-pathology-specialist
# Colorectal cases → colorectal-pathology-specialist
# Continue using old skill for other cases
```

**Week 7+: Complete Transition**
```bash
# Full switch to new collection
# Uninstall old skill
```

**Timeline:** 6-8 weeks for gradual migration

---

### Path 3: Selective Migration

Install only specific new skills you need.

**Scenario: Only Need Compliance Checking**
```bash
# Install just compliance-checker
/plugin install compliance-checker@pathology-skills-collection

# Keep using old skill for other features
```

**Scenario: Breast Pathologist Only**
```bash
# Install breast-pathology-specialist
/plugin install breast-pathology-specialist@pathology-skills-collection

# Don't need colorectal/pancreas/gastric skills
```

**Scenario: Need Coding Feature (New)**
```bash
# Install pathology-coder (didn't exist in old skill)
/plugin install pathology-coder@pathology-skills-collection

# Keep old skill for compliance checking
```

**Timeline:** Ongoing, as needed

---

## Breaking Changes

### 1. Skill Invocation Syntax

**Old:**
```bash
claude "Check this breast report" < report.txt
```

**New:**
```bash
# Must specify skill name
claude "Check this breast report using compliance-checker" < report.txt

# Or use specialist skill
claude "Check this breast report using breast-pathology-specialist" < report.txt
```

**Migration:** Update all invocations to include `using <skill-name>`

---

### 2. Reference File Paths

**Old:**
```
pathology-report-checker-skill/references/diagnosis/breast_invasive_carcinoma.md
```

**New:**
```
# Core skills
pathology-skills-collection/pathology-skills/compliance-checker/references/diagnosis/breast_invasive_carcinoma.md

# Specialist skills
pathology-skills-collection/pathology-skills/breast-pathology-specialist/references/diagnosis/breast_invasive_carcinoma.md

# Shared references
pathology-skills-collection/shared-references/staging/tnm_stage_calculator.md
```

**Migration:** Update any hardcoded paths in scripts

---

### 3. Batch Processing Scripts

**Old (`batch_checker.py`):**
```python
# Load skill file
skill_content = load_skill_file("pathology-report-checker-skill/SKILL.md")
```

**New:**
```python
# Load appropriate skill
skill_content = load_skill_file("pathology-skills-collection/pathology-skills/compliance-checker/SKILL.md")

# Or use specialist skill
skill_content = load_skill_file("pathology-skills-collection/pathology-skills/breast-pathology-specialist/SKILL.md")
```

**Migration:** Update batch scripts to use new paths and skill names

---

### 4. Feature Access

**Old:**
All features accessible through single skill.

**New:**
Features split across multiple skills.

| Feature | Old | New |
|---------|-----|-----|
| Compliance checking | Included | Use `compliance-checker` or specialist |
| Template generation | Included | Use `template-generator` or specialist |
| Staging calculation | Included | Use `tnm-stage-calculator` or specialist |
| Coding suggestions | **Not available** | Use `pathology-coder` (NEW) |
| Tumor board summaries | Included | Use `tumor-board-summary` or specialist |
| Report conversion | Included | Use `report-converter` (separate skill) |

**Migration:** Update workflows to call appropriate skill for each feature

---

## Gradual Migration Strategy

### Phase 1: Preparation (Week 1)

**Tasks:**
- [ ] Read migration guide
- [ ] Install new collection alongside old skill
- [ ] Test new skills on known cases
- [ ] Document current usage patterns

**Validation:**
```bash
# Verify both skills work
claude skills list | grep pathology

# Should show:
# - pathology-report-checker (old)
# - pathology-compliance-checker (new)
# - pathology-breast-pathology-specialist (new)
# ... etc.
```

---

### Phase 2: Testing (Weeks 2-3)

**Tasks:**
- [ ] Run parallel tests (old vs new)
- [ ] Compare outputs for consistency
- [ ] Identify any discrepancies
- [ ] Update scripts to use new skill names

**Test Script:**
```bash
#!/bin/bash
# test_migration.sh

echo "Testing old skill..."
claude "Check this report using pathology-report-checker" < test_report.txt > old_output.txt

echo "Testing new skill..."
claude "Check this report using compliance-checker" < test_report.txt > new_output.txt

echo "Comparing outputs..."
diff old_output.txt new_output.txt

echo "Done! Review differences."
```

---

### Phase 3: Selective Adoption (Weeks 4-6)

**Tasks:**
- [ ] Start using specialist skills for high-volume tumor types
- [ ] Use new utility skills (coder, staging) for quick lookups
- [ ] Continue using old skill for less common tumor types
- [ ] Gather user feedback

**Example Adoption:**
```bash
# High-volume breast cases → Use breast-pathology-specialist
if [[ $tumor_type == "breast" ]]; then
  claude "Check report using breast-pathology-specialist" < "$report"
else
  # Fall back to old skill for now
  claude "Check report using pathology-report-checker" < "$report"
fi
```

---

### Phase 4: Full Migration (Week 7+)

**Tasks:**
- [ ] Switch all workflows to new skills
- [ ] Update documentation
- [ ] Train staff on new skill names
- [ ] Uninstall old skill
- [ ] Monitor for issues

**Final Cutover:**
```bash
# Remove old skill
claude skills uninstall pathology-report-checker

# Verify new skills work
claude skills list | grep pathology

# Update production scripts
sed -i 's/pathology-report-checker/compliance-checker/g' *.sh
```

---

## FAQ

### Q: Can I keep using the old skill?

**A:** Yes, the old skill will continue to work, but it won't receive updates. We recommend migrating to the new collection for:
- Bug fixes and improvements
- New features (coding, enhanced biomarker reporting)
- Better performance (modular architecture)
- Long-term support

**Timeline:**
- v1.1.0 (legacy): Supported until June 2026
- After June 2026: Legacy skill deprecated, no support

---

### Q: Do I have to install all 10 skills?

**A:** No. You can:
1. Install entire collection: `/plugin install pathology-skills@pathology-skills-collection`
2. Install only skills you need: `/plugin install breast-pathology-specialist@pathology-skills-collection`

Choose based on your practice:
- General pathology department → Install all core skills
- Breast cancer center → Install breast-pathology-specialist only
- GI pathology practice → Install colorectal/pancreas/gastric specialists

---

### Q: Will my old scripts still work?

**A:** Not without modification. You'll need to:
1. Update skill names in invocations
2. Update reference file paths
3. Update batch processing scripts

See [Breaking Changes](#breaking-changes) section for details.

---

### Q: What if I find a bug or regression?

**A:** Report issues at:
- GitHub: https://github.com/yourusername/pathology-skills-collection/issues
- Include:
  - Skill name and version
  - Input report (anonymized)
  - Expected vs. actual output
  - Migration context (old skill behavior vs. new)

We prioritize migration-related bugs and regressions.

---

### Q: Can I migrate gradually?

**A:** Yes! See [Path 2: Gradual Migration](#path-2-gradual-migration). Recommended timeline:
- Week 1: Install and test
- Weeks 2-3: Parallel usage
- Weeks 4-6: Phase-in new skills
- Week 7+: Complete transition

This allows testing without disrupting production workflows.

---

### Q: What happened to the batch processing scripts?

**A:** They're not included in the new collection, but you can:

**Option 1: Use examples from documentation**
- See `docs/examples.md` for updated batch processing scripts
- Python scripts using Anthropic API

**Option 2: Adapt old scripts**
- Update skill names
- Update file paths
- Use new skill invocation syntax

**Option 3: Request inclusion**
- If many users need batch scripts, we can add them to the collection
- Open a GitHub discussion

---

### Q: Are there new features I should know about?

**A:** Yes, several new features:

**1. SNOMED Coding Skill**
- Dedicated skill for SNOMED CT and ICD-O-3 codes
- Not available in old skill
- Use for LIS integration, tumor registry

**2. Enhanced Biomarker Reporting**
- Breast: Detailed ER/PR/HER2/Ki-67 guidelines
- Colorectal: MSI/MMR with Lynch syndrome algorithm
- Gastric: HER2 testing for advanced disease
- More comprehensive than old skill

**3. Specialist Skills**
- Tumor-specific workflows
- All features in one skill for your tumor type
- More convenient than switching between features

**4. Improved Documentation**
- Comprehensive docs/ folder
- getting-started.md, pathology-skills.md, examples.md
- Better than single README in old skill

---

### Q: How do I report the same case with both skills for comparison?

**A:**
```bash
# Test case
cat > test_report.txt << 'EOF'
[Your test report here]
EOF

# Run with old skill
claude "Check this report using pathology-report-checker" < test_report.txt > old_output.txt

# Run with new skill
claude "Check this report using compliance-checker" < test_report.txt > new_output.txt

# Compare
diff old_output.txt new_output.txt

# Or use vimdiff for side-by-side
vimdiff old_output.txt new_output.txt
```

---

### Q: Will the new collection work with my current LIS integration?

**A:** Likely yes, with updates:

**1. Update API Calls**
```python
# Old
client.messages.create(
    messages=[{"role": "user", "content": "Check this report using pathology-report-checker"}]
)

# New
client.messages.create(
    messages=[{"role": "user", "content": "Check this report using compliance-checker"}]
)
```

**2. Update Parsing Logic**
- Output format is similar but may have minor differences
- Test with sample reports
- Update parsers if needed

**3. Test Integration**
- Run integration tests with new skills
- Verify all LIS hooks work correctly
- Update error handling if needed

---

## Summary: Quick Migration Checklist

- [ ] **Week 1**: Install new collection, test alongside old skill
- [ ] **Week 2**: Update scripts with new skill names
- [ ] **Week 3**: Test parallel usage (old vs new)
- [ ] **Week 4**: Start using specialist skills for high-volume types
- [ ] **Week 5**: Use new utility skills (coder, staging)
- [ ] **Week 6**: Phase in remaining workflows
- [ ] **Week 7**: Complete cutover, uninstall old skill
- [ ] **Week 8**: Monitor for issues, gather feedback

---

## Support During Migration

**Resources:**
- Migration Guide: This document
- Getting Started: `docs/getting-started.md`
- Skill Reference: `docs/pathology-skills.md`
- Examples: `docs/examples.md`

**Help:**
- GitHub Issues: https://github.com/yourusername/pathology-skills-collection/issues
- GitHub Discussions: https://github.com/yourusername/pathology-skills-collection/discussions
- Tag issues with `migration` label for priority support

**Migration Assistance:**
- We offer 1-on-1 migration support for large departments
- Contact: pathology-skills@example.com
- Include: Department size, current usage, timeline requirements

---

Successful migration to the new collection!
