# Reporting Standards — When Each Applies and What to Check

Match each study to the relevant reporting guideline. Flag the 2–3 most
consequential gaps for each applicable guideline.

---

## CONSORT — Randomized Controlled Trials

**Apply when**: study reports a randomized comparison of interventions.

**Key items to check**:
- Trial registration (ClinicalTrials.gov or equivalent) reported with ID
- Sample size calculation pre-specified
- Random sequence generation method described
- Allocation concealment mechanism described
- Blinding (who was blinded) clearly stated
- CONSORT flow diagram (enrolled → randomized → analyzed)
- Intention-to-treat analysis as primary
- Per-protocol as sensitivity, not as primary
- Adverse events reported by arm
- Primary outcome change between protocol and paper flagged

**Reference**: Schulz KF, Altman DG, Moher D. CONSORT 2010 Statement. BMJ 2010;340:c332.

---

## STROBE — Observational Studies

**Apply when**: cohort, case-control, or cross-sectional design.

**Key items to check**:
- Study design clearly stated in title or abstract
- Setting, locations, dates clearly specified
- Eligibility criteria, sources and methods of selection
- Variables defined: outcomes, exposures, predictors, confounders, effect modifiers
- Bias sources discussed
- Sample size rationale
- Quantitative variables: handling (categorized? splines?) explained
- Statistical methods: confounder control approach explained
- Missing data addressed
- Sensitivity analyses where appropriate
- Generalizability discussed

**Reference**: von Elm E et al. STROBE Statement. PLoS Med 2007;4(10):e296.

---

## STARD — Diagnostic Accuracy Studies

**Apply when**: study estimates the accuracy of a diagnostic test against a
reference standard.

**Key items to check**:
- Study question framed in terms of diagnostic accuracy in a defined population
- Eligibility criteria for participants
- Recruitment method (consecutive, random, convenience) stated
- Index test and reference standard described in enough detail to replicate
- Blinding between index and reference test results
- 2×2 table of index vs reference outcomes
- Sensitivity, specificity with 95% CIs
- Indeterminate / missing results reported
- Flow diagram of participants
- Time interval between index and reference
- Verification bias addressed
- Spectrum bias addressed (recruitment from relevant clinical population)

**Reference**: Bossuyt PM et al. STARD 2015. BMJ 2015;351:h5527.

---

## TRIPOD — Prognostic / Diagnostic Prediction Models

**Apply when**: study develops, validates, or updates a multivariable prediction
model.

**Key items to check**:
- Type clearly stated: development only, development with internal validation,
  external validation, or update
- Source of data and dates
- Outcome definition and how it was assessed (blinded to predictors)
- Predictors fully defined including timing of measurement
- Sample size rationale (EPV ≥10 for development)
- Missing data handling (multiple imputation preferred)
- Variable selection method described
- Internal validation: bootstrap or cross-validation with optimism correction
- External validation: independent dataset, calibration slope and intercept reported
- Calibration plot
- Discrimination (C-index / AUC) with 95% CI
- Clinical utility (decision curve analysis or net benefit) where applicable
- Limitations of generalizability discussed

**Reference**: Collins GS et al. TRIPOD. Ann Intern Med 2015;162:55-63.
TRIPOD-AI extension: Collins GS et al. BMJ 2024;385:e078378.

---

## PRISMA — Systematic Reviews and Meta-Analyses

**Apply when**: paper synthesizes evidence across multiple studies.

**Key items to check**:
- Protocol registered (PROSPERO or equivalent) with date and ID
- PICO question stated
- Search strategy (at least one database with full search string) provided
- Eligibility criteria pre-specified
- Risk of bias assessment for each included study (Cochrane RoB 2, ROBINS-I,
  QUADAS-2, etc.)
- PRISMA flow diagram
- Heterogeneity quantified (I², τ²)
- Random-effects vs fixed-effects model justified
- Publication bias assessed (funnel plot, Egger's test) when ≥10 studies
- Sensitivity / subgroup analyses reported
- Certainty of evidence (GRADE) for primary outcomes

**Reference**: Page MJ et al. PRISMA 2020 Statement. BMJ 2021;372:n71.

---

## REMARK — Tumor Marker Prognostic Studies

**Apply when**: study evaluates the prognostic or predictive value of a tumor
marker (IHC, molecular, imaging-derived) in cancer patients.

**Key items to check**:
- Marker assay method described in detail (antibody, clone, dilution, scoring)
- Inter-observer / inter-laboratory reliability assessed
- Cut-points pre-specified (not data-driven)
- Patient selection clearly described
- Outcome definition consistent (OS, DSS, DFS, PFS, RFS — define each)
- Multivariable adjustment for known prognostic factors
- Reporting of HR with 95% CI
- Subgroup analyses pre-specified
- Validation in independent cohort

**Reference**: McShane LM et al. REMARK. J Natl Cancer Inst 2005;97(16):1180-4.

---

## ARRIVE — Animal Research

**Apply when**: in vivo animal experiments.

**Key items to check**:
- Species, strain, sex, age, weight, source
- Housing and husbandry conditions
- Sample size justification (formal calculation)
- Randomization and blinding methods
- Outcome measures pre-specified
- Statistical methods appropriate for the design
- Ethical approval and protocol number

**Reference**: Percie du Sert N et al. ARRIVE 2.0. PLoS Biol 2020;18(7):e3000410.

---

## How to use this reference in a review

1. From the article's design, pick the applicable guidelines (sometimes more than one).
2. For each, identify the **2–3 most consequential gaps** — not every missing item
   is worth flagging.
3. Tie each flagged gap to a concrete recommendation (e.g., "REMARK 7: cut-point
   was data-driven; recommend pre-specifying based on prior published cut-points").
