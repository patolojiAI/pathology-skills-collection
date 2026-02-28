# Sample Reports

Synthetic/anonymized pathology reports for testing and demonstration.

## Quick Reference

| File | Type | Language | Expected Score | Key Features |
|------|------|----------|----------------|--------------|
| `breast_complete_en.txt` | Breast | EN | 100 (Compliant) | All elements present |
| `breast_incomplete_en.txt` | Breast | EN | ~70 (Major) | Missing pT, pN, Stage, Ki-67 |
| `breast_complete_tr.txt` | Breast | TR | 100 (Compliant) | Turkish language |
| `colorectal_complete_en.txt` | Colorectal | EN | 100 (Compliant) | Full MMR, KRAS |
| `colorectal_errors_en.txt` | Colorectal | EN | ~55 (Critical) | CRM error, pN error, Stage error |
| `colorectal_incomplete_tr.txt` | Colorectal | TR | ~65 (Major) | Missing MMR, KRAS |
| `pancreas_complete_en.txt` | Pancreas | EN | 100 (Compliant) | All 6 margins, R1 |
| `pancreas_staging_error_en.txt` | Pancreas | EN | ~70 (Major) | pT3 should be pT2 |
| `gastric_complete_en.txt` | Gastric | EN | 100 (Compliant) | Lauren, HER2, Borrmann |
| `gastric_incomplete_tr.txt` | Gastric | TR | ~55 (Critical) | Missing Lauren, HER2, pN |

---

## Test Categories

### 1. Complete/Compliant Reports
Test that the checker correctly identifies compliant reports:
- `breast_complete_en.txt`
- `breast_complete_tr.txt`
- `colorectal_complete_en.txt`
- `pancreas_complete_en.txt`
- `gastric_complete_en.txt`

### 2. Incomplete Reports (Missing Elements)
Test gap detection:
- `breast_incomplete_en.txt` - Missing staging elements
- `colorectal_incomplete_tr.txt` - Missing MMR/molecular
- `gastric_incomplete_tr.txt` - Missing Lauren, HER2, inadequate nodes

### 3. Cross-Validation Errors
Test error detection:
- `colorectal_errors_en.txt` - CRM error, pN error, Stage error
- `pancreas_staging_error_en.txt` - pT category error

### 4. Turkish Language
Test bilingual support:
- `breast_complete_tr.txt`
- `colorectal_incomplete_tr.txt`
- `gastric_incomplete_tr.txt`

---

## Expected Outputs

The `expected_outputs/` folder contains sample QA reports:
- `breast_complete_en_output.txt` - Shows compliant report format
- `colorectal_errors_en_output.txt` - Shows error detection and amendment template

---

## Usage

### Claude.ai / Claude CLI
```bash
# Test single sample
claude "Check this report for CAP compliance" < samples/breast_complete_en.txt

# Expected: Score 100, COMPLIANT

claude "Check this report for CAP compliance" < samples/colorectal_errors_en.txt

# Expected: Score ~55, CRITICAL with 3 errors
```

### Batch Testing
```bash
# Test all samples
claude "Analyze all reports in samples/ folder and summarize compliance"
```

---

## Sample Report Structure

Each sample includes:
1. **Header comment** with expected result
2. **Clinical history** (anonymized)
3. **Gross description** (for macroscopy testing)
4. **Microscopic diagnosis** (main content)
5. **Staging** (for cross-validation)
6. **Biomarkers** (tumor-specific)

---

## Creating New Samples

When adding new samples:
1. Use realistic but synthetic data
2. Include header comment with expected score
3. Add to this README table
4. Create expected output if demonstrating specific features
5. Test with the checker before committing

---

## Notes

- All patient identifiers are marked [ANONYMIZED]
- Reports are based on CAP/ICCR templates
- Errors are intentionally included for testing
- Turkish reports use standard Turkish medical terminology
