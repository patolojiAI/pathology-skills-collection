# Scoring Rubric — 9 Aspects × 0–2 Points

Use this reference when scoring each aspect of a paper's statistical methods.
Total ranges 0–18. Overall badge: 🟢 Robust (15–18) · 🟡 Moderate (8–14) · 🔴 Weak (0–7).

---

## 1. Design–Method Alignment

**2 (🟢)** — Every test matches the study design, the measurement scale, and the
dependence structure of the data. Paired data analyzed with paired tests. Clustered
data analyzed with mixed models or GEE. Ordinal outcomes analyzed with ordinal models
or appropriate non-parametric tests. Time-to-event analyzed with survival methods.

**1 (🟡)** — Mostly aligned with one questionable choice (e.g., chose Mann-Whitney
when t-test would have been fine, or vice versa, but the conclusion is unaffected).

**0 (🔴)** — A primary test is fundamentally wrong for the design. Examples:
unpaired t-test on paired data; chi-square on dependent proportions; Pearson
correlation on ordinal data; ignoring clustering in cluster-randomized trials.

---

## 2. Assumptions & Diagnostics

**2 (🟢)** — Key assumptions explicitly stated **and** checked with evidence (figures,
test statistics, or sensitivity analyses). Normality assessed before parametric tests,
PH tested for Cox, multicollinearity (VIF) reported for multivariable models,
homoscedasticity for ANOVA, etc.

**1 (🟡)** — Assumptions are mentioned but only superficially checked, or only some
key assumptions are addressed.

**0 (🔴)** — Assumptions never discussed. Violations are likely material and would
change the inference if addressed.

---

## 3. Sample Size & Power

**2 (🟢)** — A priori sample size calculation with stated effect size, α level,
power, and dropout rate. For non-trial designs, precision (CI width) targets are
reported.

**1 (🟡)** — Post-hoc justification only, or no formal calculation but observed
precision (CI widths) is adequate for the claims made.

**0 (🔴)** — Clearly underpowered with no justification. CIs are wide and the paper
nonetheless makes definitive negative claims (absence of evidence ≠ evidence of
absence).

---

## 4. Multiplicity Control

**2 (🟢)** — Pre-specified correction matching the analysis plan (e.g., Bonferroni
for confirmatory family of hypotheses; BH-FDR for omics screens). Number of tests
in the family is stated. Hierarchical/gatekeeping is used where appropriate.

**1 (🟡)** — Some correction applied but inconsistent across tables, or correction
applied to only part of the multiple-comparison problem.

**0 (🔴)** — Many p-values, no correction. "Fishing" is plausible. Subgroup analyses
treated as confirmatory without correction.

---

## 5. Model Specification & Confounding

**2 (🟢)** — Pre-specified covariates with biological/clinical rationale. Functional
forms justified (splines for non-linear, interactions tested where prior knowledge
suggests). EPV (events per variable) ≥10 for regression. DAGs or causal framework
where appropriate.

**1 (🟡)** — Data-driven variable selection but with internal validation (bootstrap,
cross-validation) and shrinkage. Some confounders may be missing but the main ones
are addressed.

**0 (🔴)** — Stepwise selection with no validation, "significant in univariable so
included in multivariable" filtering, or known major confounders ignored. EPV <10
without acknowledgement.

---

## 6. Missing Data Handling

**2 (🟢)** — Missingness mechanism discussed (MCAR / MAR / MNAR). Multiple imputation
(MICE) or another principled method used. Sensitivity analyses under alternative
assumptions (e.g., tipping-point, pattern-mixture).

**1 (🟡)** — Complete-case analysis with explicit acknowledgement of the limitation
and comparison of completers vs non-completers.

**0 (🔴)** — Missing data ignored or single-imputation (LOCF, mean imputation) used
without sensitivity analysis. Missingness pattern undisclosed.

---

## 7. Effect Sizes & CIs

**2 (🟢)** — Effect sizes with confidence intervals reported throughout. p-values
are supportive, not the primary inference. Clinically meaningful thresholds discussed.

**1 (🟡)** — Mixed reporting — some tables have effect sizes + CIs, others only
p-values.

**0 (🔴)** — p-values only. Conclusions framed around p < 0.05 thresholds. No
estimate of magnitude or precision.

---

## 8. Validation & Calibration

Applies primarily to prediction / diagnostic / prognostic models.

**2 (🟢)** — Internal validation (cross-validation or bootstrap with optimism
correction) **plus** external validation in an independent cohort. Calibration slope
and intercept reported, plus a calibration plot. Discrimination (C-index / AUC) with
CI. Decision curve analysis where applicable.

**1 (🟡)** — Internal validation only, or discrimination reported without calibration,
or external validation in a non-independent split.

**0 (🔴)** — Apparent performance only (training-data AUC/accuracy). No validation,
no calibration. Risk of severe optimism.

---

## 9. Reproducibility & Transparency

**2 (🟢)** — Code publicly available (GitHub / Zenodo). Data available or with
clear access mechanism. Random seeds reported. Package versions stated. Pre-registered
analysis plan or protocol citation.

**1 (🟡)** — Package versions stated and code/data available on reasonable request.
No pre-registration but methods are well-described.

**0 (🔴)** — No code, no data, no seeds, no versions. Methods description too vague
to reproduce.

---

## Scoring tips

- When in doubt between two scores, choose the lower one. It's easier to argue up
  than down.
- A score of 0 on any aspect means a major concern that should appear in the Red
  Flags section.
- Score based on what is **reported**, not on what the authors might have done.
  Reporting is part of the methods quality.
