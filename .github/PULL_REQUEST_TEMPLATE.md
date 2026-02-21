## Description

Brief description of changes made in this pull request.

Fixes #(issue_number)

## Type of Change

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] New skill
- [ ] New tumor type support
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Language translation
- [ ] Test/example update

## Skill/Tumor Type Details (if applicable)

- **Skill Name**: [e.g., lung-specialist]
- **Tumor Types**: [e.g., lung, NSCLC, SCLC]
- **Clinical Guidelines**: [CAP Lung 2024, AJCC 8th Ed]

## Changes Made

### Added
- List new features, files, or functionality added

### Changed
- List modifications to existing features

### Fixed
- List bug fixes

### Removed
- List deprecated or removed features

## Testing Performed

### Test Environment
- **OS**: [e.g., macOS 14.2]
- **Python Version**: [if applicable]
- **Claude CLI Version**: [if applicable]

### Test Cases

- [ ] Tested with text files
- [ ] Tested with Excel/CSV batch processing
- [ ] Tested with PDF files
- [ ] Tested with images
- [ ] Tested with real pathology reports
- [ ] Tested English language
- [ ] Tested Turkish language (if applicable)
- [ ] Cross-validation working correctly
- [ ] Staging calculation accurate
- [ ] Compliance scoring correct

### Test Results

```
Paste test output or summary here
```

## Clinical Guidelines Verification

- [ ] Follows CAP 2024 protocols
- [ ] Follows ICCR 2nd Edition datasets
- [ ] Follows AJCC 8th Edition staging (if applicable)
- [ ] Follows AAPA 3rd Edition macroscopy guidelines (if applicable)
- [ ] References validated against official sources

**Sources Consulted:**
- [List clinical guideline sources with links]

## Code Quality

- [ ] My code follows the style guidelines (see CONTRIBUTING.md)
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in complex areas
- [ ] I have updated the documentation (README, SKILL.md, etc.)
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published

## Documentation Updates

- [ ] README.md updated (if needed)
- [ ] SKILL.md created/updated
- [ ] marketplace.json updated (if new skill)
- [ ] CHANGELOG.md updated
- [ ] Example files added
- [ ] Reference files added/updated

## Files Changed

List key files added or modified:

```
pathology-skills/new-skill/SKILL.md
pathology-skills/new-skill/references/diagnosis/new_tumor.md
shared-references/staging/tnm_stage_calculator.md
marketplace.json
CHANGELOG.md
```

## Breaking Changes

Describe any breaking changes and migration steps (if applicable):

**Breaking:**
- None

OR

- [Describe breaking change]
- **Migration**: [How users should update their usage]

## Screenshots / Examples

If applicable, add screenshots or example outputs:

```
Example output from testing:

COMPLIANCE ANALYSIS - Lung Cancer
Score: 95/100 (COMPLIANT)
...
```

## Checklist Before Requesting Review

- [ ] PR title follows format: `type(scope): description` (e.g., `feat(lung-specialist): Add lung cancer support`)
- [ ] I have linked related issues
- [ ] I have updated all relevant documentation
- [ ] All tests pass
- [ ] Clinical guidelines are properly cited
- [ ] No real patient data included
- [ ] Examples use synthetic data only
- [ ] Code is ready for review

## Additional Notes

Add any additional context for reviewers here.

---

## For Reviewers

### Review Focus

Please pay special attention to:
- [ ] Clinical accuracy of guidelines implementation
- [ ] Cross-validation logic correctness
- [ ] Code quality and maintainability
- [ ] Documentation completeness
- [ ] Test coverage

### Approval Checklist

- [ ] Code review completed
- [ ] Clinical guidelines verified
- [ ] Tests pass
- [ ] Documentation adequate
- [ ] Ready to merge
