# Lesson 15 – Study Design, Data Provenance and Quantitative Segmentation Planning

**Learning path:** 3D Slicer
**Date:** 2026-08-23
**Status:** Learning record
**Scope:** Conceptual study planning only; no dataset selection, download, segmentation, experiment, statistical analysis, or patient-specific conclusion

## Objectives

- Transition from interpreting quantitative results to planning how a future study should produce them.
- Understand data provenance and the responsible use of publicly available imaging data.
- Define cohort selection transparently through pre-specified inclusion and exclusion criteria.
- Introduce selection bias, representativeness, external validity, and generalizability conceptually.
- Formulate a focused future research question about reconstruction or slice thickness and small-lesion measurement.
- Define reference and comparison conditions without treating an operational reference as ground truth.
- Plan independent, standardized segmentations and complementary quantitative comparisons.
- Interpret Dice in relation to lesion size, geometry, and small boundary differences.

## Scientific Background

### From analysis to study design

Lessons 12–14 developed reasoning about measurement variability, repeatability, reproducibility,
agreement, bias, Limits of Agreement, magnitude-dependent interpretation, proportional bias, and
heteroscedasticity. This lesson moved upstream. Instead of starting with results and asking
“Can we trust this result?”, it began asking:

- Can these data legitimately be used?
- What exactly are the data, where did they come from, and how were they produced?
- What population do they represent?
- What scientific question should be answered?
- How should the study be designed before measurement begins?

This was planning for a future practical study, not an executed study.

### Data provenance and responsible public-data use

Data provenance describes the origin and history of data. Before downloading, segmenting, or
measuring a future dataset, the planned review should examine its source, institution, original
purpose and study design, population, pathologies, acquisition, equipment, protocol,
reconstruction, organization, file structure, case identifiers, available labels or
segmentations, and accompanying documentation.

Public availability does not automatically grant permission to redistribute data. A future
dataset must be evaluated under its actual license, terms of use, redistribution policy,
attribution requirements, and source-specific restrictions. No universal permission rule was
assumed, and no dataset was selected or downloaded in this lesson.

Scientific case identifiers can preserve relationships without exposing real patient identity:

```text
Case_001
├── image
├── segmentation
└── associated measurements
```

Appropriate de-identification or anonymization depends on context. Identifiable information
should not be retained unnecessarily, and an internal research identifier must not be confused
with a patient's identity. This is a scientific data-governance principle, not legal or
regulatory advice.

### Transparent cohort selection

A hypothetical dataset of 500 CT examinations illustrated why reporting only “We used Dataset
X” would be insufficient if a subset were analyzed. Reproducible selection would require the
dataset version, cases considered, selection procedure and rationale, inclusion criteria,
exclusion criteria, and final number analyzed.

One educational example began with 500 examinations, identified 120 with the pathology of
interest, then excluded 15 with severe artifacts, 10 with incomplete required coverage, and 15
without required information or segmentation, leaving 80 hypothetical cases. These values are
didactic only. They do not describe a real dataset or selected cohort.

Reproducibility makes the route to a result inspectable. It does not require every researcher to
obtain an identical result; it allows others to reproduce, compare, validate, question, and
understand how the result was obtained.

### Selection bias and consequences of exclusion

Selection bias was introduced through a hypothetical case in which a researcher retained 80
favorable cases and excluded 40 only because they worsened the desired conclusion. Exclusion is
not automatically wrong. A pre-specified criterion such as excluding examinations with severe
motion that prevents reliable segmentation may be defensible; excluding cases because their
results are inconvenient is scientifically problematic.

Even a technically justified exclusion can change the analyzed population. If 15 examinations
with severe artifacts are excluded and those examinations disproportionately contain large
tumors, the final sample may contain many small and medium lesions but few large lesions. Invalid
images need not be reintroduced, but the change in sample composition should be investigated,
documented, and considered during interpretation.

### Representativeness, center effects, and external validity

Representativeness asks whether the analyzed sample adequately represents the population about
which the study intends to draw conclusions. It can be influenced by the source population,
selection criteria, image quality, hospital characteristics, equipment, protocols, acquisition
completion, and lesion characteristics.

A conceptual comparison considered Hospital A, with predominantly small and medium tumors, and
Hospital B, with predominantly large tumors. If performance differs between centers, lesion size
alone should not immediately be declared causal. Scanner, software, acquisition, reconstruction,
slice thickness, contrast, artifacts, patient conditions, segmentation, observer conditions,
center effects, and population distribution may co-vary. No such factor was empirically found in
this lesson.

A study may deliberately restrict its population, for example to Hospital A. Its conclusion must
then remain within that evaluated domain. External validity and generalizability concern how far
a result obtained in one sample, center, scanner, or population may apply elsewhere. A method
tested only in one setting should not be called universally robust; performance elsewhere remains
unevaluated.

### Focused future research question

The broad question “How does image quality or acquisition affect the measurement of small
tumors?” was narrowed to one technical factor: slice thickness. Two conceptual formulations were:

> How does reconstruction or slice thickness affect volumetric measurement and segmentation
> stability in small lesions?

> Does the effect of reconstruction thickness on volumetric measurement increase as lesion size
> decreases?

Slice thickness connects spatial and z-axis resolution, partial volume, lesion size,
segmentation, volumetric measurement, and measurement variability. These questions remain
unanswered plans for future work.

### Acquisition, reconstruction, and reference conditions

Three separate acquisitions at 1, 3, and 5 mm could introduce respiration, movement,
positioning, contrast timing, acquisition differences, and potentially CT dose considerations.
When technically and scientifically appropriate, a cleaner conceptual design would use the same
acquisition with multiple reconstruction conditions, reducing unrelated variation.

Real reconstruction at a target thickness must not automatically be treated as equivalent to
simple resampling. Controlled aggregation from thin to thicker data may be appropriate in some
designs, but interpolation from thick to thin data cannot recover spatial information that was
not originally represented.

The proposed future conditions were:

| Role | Planned condition |
|---|---:|
| Operational reference condition | 1 mm |
| Comparison condition | 3 mm |
| Comparison condition | 5 mm |

The 1 mm condition was deliberately called a **reference condition**, not ground truth. It may be
an operational comparator without perfectly representing the true anatomy.

### Planned measurements and lesion-size stratification

Both absolute and relative volume change were considered. A didactic example used volumes of
`0.80 cm³`, `0.92 cm³`, and `1.15 cm³` at 1, 3, and 5 mm. Relative to 1 mm, the illustrative
changes were `+0.12 cm³` or `15%` and `+0.35 cm³` or `43.75%`. These are not experimental
results. They show why a small absolute difference may be a large relative change for a small
lesion.

Stratification by lesion size was planned conceptually because pooling all lesions may hide
magnitude-dependent behavior. Example ranges of `<5 mm`, `5–10 mm`, and `>10 mm` were discussed
only as possible study strata, not universal clinical thresholds. Final strata and their
justification belong to the future protocol.

### Independent segmentation and observer conditions

The future design favored independently segmenting each 1, 3, and 5 mm condition rather than
copying and transforming the 1 mm mask. This better addresses how the lesion appears and can be
segmented at each thickness. A transformed mask would answer a different question about mask
transformation.

Only one observer is currently available, so the future study would need to declare a
single-observer design. It could examine within-observer behavior across conditions but could not
estimate interobserver variability. Possible controls discussed included randomizing case order,
concealing the reference label where feasible, not reusing masks, and separating sessions to
reduce recall effects.

A standardized semiautomatic threshold method with the same HU interval across conditions was
proposed. Leaving each mask as produced by the fixed protocol, without manual beautification,
would study the sensitivity of that protocol to thickness. Allowing condition-specific manual
optimization would answer a different question. The exact executable rules remain to be defined
before practice.

### Volume and spatial overlap answer different questions

Volume change describes how much mask size changes; Dice describes spatial overlap. Similar
volumes can coexist with different location, contour, or shape. Dice ranges conceptually from 0,
no overlap, to 1, perfect overlap, but no universal acceptable threshold was defined.

Dice must be interpreted in relation to object size and geometry. In a very small lesion, one or
two changed boundary voxels may represent a large fraction of the mask and substantially reduce
Dice even when masks remain visually close. The same Dice value in a large lesion may reflect a
different geometric situation. A low Dice should therefore not be labeled automatically as
segmentation failure without reviewing size, boundary differences, volume, and task context.

The question “How does lesion size affect Dice sensitivity to small boundary differences?” was
identified as a possible future investigation, not answered in this lesson.

## Practical Workflow

Only a conceptual planning workflow was developed:

```text
Verify provenance, license, terms, and privacy conditions
    ↓
Define the target population and scientific question
    ↓
Pre-specify inclusion, exclusion, and cohort-accounting rules
    ↓
Assess possible selection effects and intended generalization domain
    ↓
Confirm whether same-acquisition reconstruction conditions are available
    ↓
Define 1 mm as reference and 3/5 mm as comparisons
    ↓
Pre-specify independent segmentation, observer, order, and threshold rules
    ↓
Pre-specify absolute volume, relative volume, Dice, and size-stratified analyses
    ↓
Document limitations before any measurement begins
```

No practical step in this workflow was executed. No repository dataset structure, case list,
image, mask, threshold, 3D Slicer scene, measurement table, Dice calculation, or result was
created. Practice begins only in Lesson 16 after a suitable protocol and lawful data source are
confirmed.

## Quality Checklist

- [ ] The future dataset's provenance and original purpose are documented.
- [ ] License, terms, attribution, and redistribution conditions are verified from the source.
- [ ] Privacy and internal case-identification procedures are appropriate to the context.
- [ ] Dataset version and complete cohort-selection flow are recorded.
- [ ] Inclusion and exclusion criteria are defined before results are inspected.
- [ ] Exclusions are justified scientifically rather than by outcome favorability.
- [ ] Effects of exclusions on sample composition are examined.
- [ ] Representativeness and the intended target population are stated.
- [ ] Center, scanner, protocol, acquisition, and population co-variation are considered.
- [ ] Conclusions remain within the evaluated setting and population.
- [ ] The research question isolates a defined technical factor.
- [ ] Reconstruction is distinguished from simple resampling.
- [ ] The 1 mm condition is called a reference condition, not ground truth.
- [ ] Segmentations are independent and follow one pre-specified protocol.
- [ ] The single-observer limitation and recall controls are documented.
- [ ] Threshold and manual-correction rules match the precise study question.
- [ ] Absolute and relative volume changes are both considered.
- [ ] Lesion-size strata are justified rather than treated as universal thresholds.
- [ ] Dice is interpreted with lesion size, geometry, boundary differences, and volume.
- [ ] Hypothetical numbers are not presented as empirical findings.
- [ ] No experiment, dataset selection, segmentation, result, or clinical claim is implied.

## Lessons Learned

1. Study validity begins before data download or measurement.
2. Data provenance is necessary to understand what a dataset represents and how it was produced.
3. Public availability does not automatically permit redistribution.
4. Internal case identifiers can preserve scientific linkage without representing patient identity.
5. Transparent cohort accounting is essential when only part of a dataset is analyzed.
6. Reproducibility exposes how a result was produced; it does not force identical conclusions.
7. Exclusion may be justified while still changing the population ultimately analyzed.
8. Selection criteria should not be chosen to manufacture a favorable result.
9. Representativeness depends on both the source population and the selection process.
10. Center, equipment, protocol, population, and lesion size may co-vary.
11. Conclusions should not extend beyond the setting and population actually evaluated.
12. A focused study question is easier to test and interpret than a broad imaging-quality question.
13. Same-acquisition reconstruction conditions may isolate thickness better than separate acquisitions.
14. Thin-to-thick processing and thick-to-thin interpolation are not informationally symmetric.
15. An operational reference condition is not automatically ground truth.
16. Relative change can reveal the importance of a small absolute change in a small lesion.
17. Size stratification can expose magnitude-dependent behavior hidden by pooled summaries.
18. Independent segmentation at each condition answers a different question from mask transformation.
19. A single-observer study can be valid within scope but cannot estimate interobserver variability.
20. A fixed threshold without manual beautification studies protocol sensitivity, not best achievable segmentation.
21. Volume and Dice provide complementary size and spatial-overlap information.
22. Dice is sensitive to object size and should not be interpreted from a universal cutoff alone.
23. A scientifically useful result need not be favorable; limitations and unexpected behavior must be reported.

## Future Learning Directions

- Begin Lesson 16 by converting this conceptual design into a written, executable protocol.
- Select data only after verifying provenance, license, terms, privacy, technical suitability, and redistribution limits.
- Define cohort accounting, final lesion-size strata, reconstruction conditions, case identifiers, and folder structure before analysis.
- Specify the 3D Slicer version, independent-segmentation sequence, fixed threshold range, observer controls, and permitted corrections.
- Predefine volume, percentage-change, Dice, quality-control, missing-data, and limitation reporting procedures.
- Do not treat the proposed 1/3/5 mm conditions, example strata, or numerical examples as completed work.
- Do not claim dataset suitability, segmentation performance, measurement stability, generalizability, or clinical validity until supported by future evidence.
