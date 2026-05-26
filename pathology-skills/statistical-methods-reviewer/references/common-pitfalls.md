# Common Statistical Pitfalls — Misuse Catalogue

When reviewing a paper, scan for these patterns. Each entry gives: the pattern,
why it's wrong, and what the authors should have done instead.

---

## Comparison of two groups

### Unpaired test on paired data
- **Pattern**: Two-sample t-test or Mann–Whitney U on measurements that are
  intrinsically paired (pre/post, left/right, twin pairs, matched cases).
- **Why wrong**: Ignores within-pair correlation → inflated SE → loss of power
  and incorrect inference.
- **Fix**: Paired t-test (parametric) or Wilcoxon signed-rank (non-parametric).

### t-test on heavily skewed data with small N
- **Pattern**: Parametric test with N<30 per group and visibly non-normal data.
- **Why wrong**: CLT does not rescue small-N inference when skewness is severe.
- **Fix**: Mann–Whitney U or bootstrap CIs. Report median (IQR), not mean (SD).

### Chi-square with low expected counts
- **Pattern**: Chi-square or Fisher applied where any expected cell count is <5,
  with no continuity correction.
- **Why wrong**: Chi-square approximation breaks down; p-values are anti-conservative.
- **Fix**: Fisher's exact test, or Mid-P test for sparse tables.

---

## Three+ group comparisons

### Multiple unadjusted pairwise tests
- **Pattern**: Three or more groups → all pairwise t-tests or Mann–Whitney U
  with raw p-values.
- **Why wrong**: Familywise error rate inflates to ~14% (3 groups) or ~30%
  (5 groups) at nominal α=0.05.
- **Fix**: Omnibus test first (ANOVA / Kruskal–Wallis), then post-hoc with
  correction. Tukey HSD if variances equal; Games–Howell if not. Dunn's test
  for non-parametric.

### Welch ANOVA results presented without acknowledging unequal variances
- **Pattern**: One-way ANOVA used despite Levene p<0.05.
- **Fix**: Welch's ANOVA with Games–Howell post-hoc, or non-parametric Kruskal–Wallis.

---

## Regression and modeling

### Stepwise regression as the final model
- **Pattern**: "Variables with p<0.1 in univariable were entered into multivariable
  using stepwise selection; final model shown."
- **Why wrong**: Stepwise inflates effect estimates, biases p-values, picks noise.
  CIs are not nominal.
- **Fix**: Pre-specified covariates from prior knowledge or DAG. If selection is
  unavoidable, use penalized regression (LASSO / elastic net) with cross-validation,
  and report shrinkage.

### Univariable filtering before multivariable
- **Pattern**: "Variables significant at p<0.1 in univariable were entered."
- **Why wrong**: Misses confounders that have no marginal association but matter
  conditionally. Bias amplification possible.
- **Fix**: Choose covariates from theory, not from the data.

### Events-per-variable (EPV) too low
- **Pattern**: Logistic regression with 8 events and 6 predictors.
- **Why wrong**: Overfitting, unstable estimates, optimistic apparent performance.
- **Fix**: Require EPV ≥10 (some recent work says 20 is safer). Otherwise use
  penalization (Firth correction for logistic; ridge / LASSO for general models).

### Dichotomizing continuous predictors
- **Pattern**: Age dichotomized at median; biomarker at "high vs low".
- **Why wrong**: Loses information, creates artificial threshold effects, reduces
  power, biases estimates.
- **Fix**: Keep continuous with restricted cubic splines or fractional polynomials.
  If clinical thresholds exist, justify them externally, not data-driven.

### Categorical with ordinal information treated as nominal
- **Pattern**: Tumor grade 1/2/3 entered as three dummies in logistic regression.
- **Why wrong**: Loses ordering information; reduces power; misses linear trend.
- **Fix**: Linear or polynomial scoring; ordinal logistic regression; Cochran–
  Armitage trend test for proportions.

---

## Survival analysis

### Cox PH assumption never tested
- **Pattern**: Cox model with HRs reported, no PH assumption check.
- **Fix**: Schoenfeld residuals test + visualization. If violated: stratified Cox,
  time-dependent covariate, time-stratified analysis, restricted mean survival time
  (RMST), or accelerated failure time (AFT) model.

### Immortal time bias
- **Pattern**: Exposure defined by an event that can only happen after time zero
  (e.g., "patients who received chemo" when chemo can only be given to those who
  survived long enough).
- **Fix**: Landmark analysis or time-dependent covariate for the exposure.

### Competing risks ignored
- **Pattern**: Cause-specific Kaplan–Meier used in the presence of competing
  events (e.g., cancer-specific mortality with non-cancer deaths censored).
- **Why wrong**: Overestimates cumulative incidence.
- **Fix**: Cumulative incidence function (CIF) for non-parametric; Fine–Gray
  subdistribution hazard or cause-specific Cox for regression.

### Log-rank with non-proportional hazards
- **Pattern**: KM curves cross; log-rank p still reported.
- **Why wrong**: Log-rank has low power when hazards are non-proportional.
- **Fix**: RMST difference, weighted log-rank (Fleming–Harrington), or piecewise
  exponential.

---

## Diagnostic / prognostic models

### AUC alone
- **Pattern**: Reports "AUC = 0.85" with no CI, no calibration, no decision
  curve.
- **Fix**: AUC with 95% CI; calibration plot with slope and intercept; net benefit
  via decision curve analysis (DCA); clinically relevant thresholds with
  sensitivity/specificity/PPV/NPV reported.

### Apparent (training) performance only
- **Pattern**: Model built on full dataset and AUC reported on the same data.
- **Fix**: Optimism-corrected bootstrap (Harrell), repeated cross-validation, or
  external validation in an independent cohort.

### Verification bias
- **Pattern**: Diagnostic study where the gold-standard test is applied only to
  index-positive cases.
- **Fix**: Apply gold standard to a random sample of negatives, or use
  multiple imputation / latent class models. Report STARD-compliant flow.

### Spectrum bias
- **Pattern**: Diagnostic accuracy estimated in "obviously sick vs healthy"
  comparison.
- **Fix**: Recruit consecutive patients from the relevant clinical population.

---

## Reliability / agreement

### Cohen's kappa on ordinal data
- **Pattern**: 4-grade tumor classification compared with unweighted kappa.
- **Why wrong**: Treats "grade 1 vs grade 4" disagreement same as "grade 1 vs
  grade 2".
- **Fix**: Weighted kappa (quadratic weights) or ICC (two-way random, absolute
  agreement).

### Bland–Altman without repeated measures handling
- **Pattern**: Multiple measurements per subject pooled into a single Bland–Altman
  plot.
- **Fix**: Bland–Altman with repeated measures (variance components decomposition),
  or random-effects approach (Bland & Altman 2007).

### Pearson correlation for method comparison
- **Pattern**: "Methods correlated r=0.95, therefore equivalent."
- **Why wrong**: High correlation does not imply agreement. Two methods with a
  constant offset have r=1.0.
- **Fix**: Bland–Altman or Deming regression. Concordance correlation
  coefficient (CCC).

---

## Multiple testing in -omics / high-throughput

### Bonferroni on 20,000 genes
- **Pattern**: Bonferroni applied to whole-transcriptome screen.
- **Why wrong**: Overly conservative; few discoveries.
- **Fix**: Benjamini–Hochberg FDR. State FDR threshold (typically 0.05 or 0.1).

### No correction for sub-study tests
- **Pattern**: 50 subgroup analyses, "two were significant".
- **Fix**: Pre-specify hypotheses or apply FDR. Report all comparisons performed.

---

## Reporting

### p-values without effect sizes
- **Pattern**: "Group A vs B, p=0.03"; no estimate of the difference.
- **Fix**: Report point estimate + 95% CI as the primary inference. p-value is
  supportive.

### Significant subgroup without interaction test
- **Pattern**: "Treatment worked in women (p=0.01) but not men (p=0.18)."
- **Why wrong**: This is a comparison of significance, not a test of difference.
- **Fix**: Test the treatment × sex interaction term.

### "Trend toward significance"
- **Pattern**: p=0.07 described as "marginal" or "approaching significance".
- **Why wrong**: Either the prior threshold was meaningful or it wasn't. Picking
  one direction post-hoc is selective interpretation.
- **Fix**: Report estimate + CI and let the reader judge.

---

## Meta-analysis

### Fixed-effects model with high heterogeneity
- **Pattern**: I² = 75%, fixed-effects pooled estimate reported.
- **Fix**: Random-effects model. Investigate heterogeneity (meta-regression,
  subgroup analysis). Consider whether pooling is appropriate at all.

### No funnel plot / publication bias check
- **Pattern**: ≥10 studies, no funnel plot or Egger's test.
- **Fix**: Funnel plot, Egger's regression for asymmetry, trim-and-fill where
  appropriate.
