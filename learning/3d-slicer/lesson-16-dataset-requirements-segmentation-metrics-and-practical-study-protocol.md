# Lesson 16 – Dataset Requirements, Segmentation Metrics and Practical Study Protocol

**Learning path:** 3D Slicer
**Date:** 2026-08-25
**Status:** Learning record
**Scope:** Conceptual protocol refinement only; no dataset selection, download, image analysis, segmentation, metric calculation, experiment, or patient-specific conclusion

## Objectives

- Refine the conceptual study design developed in Lesson 15 before evaluating real datasets.
- Define initial dataset, reconstruction, metadata, and segmentation-provenance requirements.
- Distinguish originally thin reconstruction from interpolation of originally thick data.
- Define complementary roles for lesion diameter, segmented volume, overlap, surface distance, and visual quality control.
- Introduce Average Surface Distance, Hausdorff Distance, and HD95 at a conceptual level.
- Define traceable cohort accounting and an initial master-table design.
- Keep the first practical study progressive and limited to variables that answer defined scientific questions.

## Scientific Background

### Continuity from Lesson 15

Lesson 15 planned a future study connecting slice thickness, segmentation, volumetric
measurement, and lesion size. It proposed a verified public dataset, same-acquisition
reconstructions when possible, a 1 mm reference condition, 3 and 5 mm comparisons, independent
single-observer segmentations, a standardized semiautomatic threshold, volume change, Dice, and
lesion-size stratification. Lesson 16 refined that protocol conceptually. It did not execute it.

### Dataset and reconstruction requirements

A dataset containing only CT images originally reconstructed at 5 mm would not support the main
planned comparison if the intention were to derive equivalent 1, 3, and 5 mm reconstruction
conditions from those images alone. Interpolating a thick reconstruction onto a finer grid does
not recover anatomical information that was not preserved in the original representation.

The initial criteria for evaluating a future candidate dataset are:

- CT data appropriate to the scientific question;
- the same acquisition with multiple reconstruction conditions when possible;
- an originally thin reconstruction, preferably approximately 1 mm for the reference condition;
- small lesions relevant to the planned magnitude-dependent investigation;
- sufficient acquisition, reconstruction, and lesion documentation;
- verified provenance, license, terms of use, and redistribution conditions;
- documented segmentation information when masks are available.

These are search and evaluation criteria only. No dataset was selected or evaluated.

Partial volume effect was revisited as a reason thickness may affect apparent boundaries,
measured intensity, lesion representation, and segmentation behavior. In thicker sections,
different tissues may contribute to the value represented in one voxel. No partial-volume effect
was measured in this lesson.

### Segmentation provenance and reference status

An available mask should not automatically be accepted as ground truth. Its provenance should be
investigated when documented, including whether segmentation was manual, semiautomatic, or
automatic; observer number and expertise; review or consensus process; software and protocol;
reconstruction condition; quality control; and available interobserver or intraobserver
information.

A mask may serve as a **reference segmentation** without representing anatomical **ground
truth**. Similarly, the proposed 1 mm image is an operational **reference condition**, not true
anatomy. Future findings should therefore be described as differences relative to the 1 mm
reference condition unless a separate, justified external reference exists.

### DICOM, NIfTI, metadata, and the data dictionary

DICOM and NIfTI were introduced only at the level needed for later dataset evaluation. DICOM is
widely used in medical imaging and can associate images with extensive acquisition and
reconstruction metadata. NIfTI is widely used in research for volumes and masks and is not
automatically unsuitable. A DICOM-to-NIfTI conversion may, however, omit some original metadata.
The practical question is:

> Do the available files and documentation preserve the information required to answer the
> scientific question?

Missing metadata should be identified, investigated for possible recovery, and judged according
to whether it is essential to the study question before a dataset is accepted or rejected.
Missing information directly related to the principal variable may make a dataset unsuitable.

A **data dictionary** was introduced as documentation of field meaning. For fields such as
`case_id`, `recon_thickness`, `manufacturer`, `kernel`, and `lesion_size`, the definition, unit,
possible values, origin, and calculation method must be understood before use.

### Interpreting lesion size

The isolated value `lesion_size = 8` is scientifically insufficient. Its meaning depends on
whether it represents diameter or volume, which diameter, the unit, measurement method, source,
and time point. Current size and change across time points answer different questions; a change
from 30 to 8 does not make the current value itself a change variable.

When `lesion_size` is defined as maximum axial diameter in millimeters, diameter could be used for
size stratification while segmented volume in cubic centimeters could be an outcome. Diameter
and volume are not interchangeable: lesions with equal maximum diameter can have different
geometry and volume.

The conceptual protocol fixes the lesion-size stratum using the 1 mm reference condition. The
stratum then remains unchanged across thickness comparisons so that a thickness-related change
in apparent size is not mixed with reassignment of the analysis group. When appropriate, the
original dataset measurement should be retained as provenance while the study-specific measure
is independently derived from the 1 mm condition under the future protocol. No measurement was
recalculated here.

### Reconstruction conditions and comparisons

The refined conceptual design is:

| Role | Proposed thickness |
|---|---:|
| Operational reference condition | 1 mm |
| Optional comparison, if technically justified | 1.5 mm |
| Comparison condition | 3 mm |
| Comparison condition | 5 mm |

The 1.5 mm condition was added because reconstruction protocols near 1–1.5 mm may provide a
useful smaller transition. Its definitive inclusion depends on the future dataset and the ability
to obtain methodologically comparable conditions; it was neither produced nor validated.

Potential comparisons against the reference are `1 vs 1.5 mm`, `1 vs 3 mm`, and `1 vs 5 mm`.
Potential adjacent comparisons are `1 vs 1.5 mm`, `1.5 vs 3 mm`, and `3 vs 5 mm`. Reference
comparisons describe accumulated differences from 1 mm; adjacent comparisons may show where a
larger transition appears. No linear or nonlinear behavior can be inferred before data exist.

### Quantitative outcomes and complementary interpretation

The retained core outcomes are segmented volume, absolute volume change, percentage volume
change, and Dice Similarity Coefficient. Volume describes how measured mask size changes; Dice
describes spatial overlap. Similar volume and relatively high Dice can still coexist with a
localized surface discrepancy, motivating future surface-distance measures.

**Average Surface Distance (ASD)** was introduced as an approximate summary of how far apart two
segmentation surfaces are on average. Lower ASD initially indicates surfaces closer on average;
higher ASD indicates greater average separation. No universal threshold was defined.

**Hausdorff Distance (HD)** was introduced as a measure sensitive to the farthest or most extreme
surface discrepancy. Most surfaces may be close while one localized extension produces a large
HD, even when ASD remains relatively low.

**HD95** was introduced as a percentile-based surface-distance summary that is less dominated by
a single extreme point than classical HD. It is a predefined methodological metric, not a license
to remove inconvenient observations, and its mathematical implementation was not studied.

The didactic comparison `ASD = 0.4 mm, HD95 = 0.9 mm` versus `ASD = 0.4 mm, HD95 = 6.0 mm`
illustrated equal average surface distance with a much larger localized discrepancy in the second
case. These numbers were hypothetical and were not calculated from data.

Surface-distance interpretation must also consider lesion magnitude. An HD95 of 2 mm may have a
different relative importance for a lesion approximately 5 mm across than for one approximately
50 mm across. No new percentage surface-distance metric was defined.

Metrics do not establish their own causes. The intended reasoning is:

```text
metric
    ↓
locate the discrepancy
    ↓
inspect image and mask
    ↓
investigate plausible causes
    ↓
interpret with the protocol and lesion magnitude
```

A localized discrepancy should prompt review for segmentation error, artifact, isolated region,
partial volume, boundary-representation change, reconstruction-thickness effect, or another
methodological cause. It should not be discarded merely because it worsens a metric.

### Visual quality control, scope, and cohort traceability

Future standardized overlays or screenshots should accompany volume, Dice, ASD, and HD95 when
technically appropriate. No visual record was produced here. The first pilot should remain
manageable: volume, percentage volume change, Dice, and visual QC may form the initial core, with
ASD and HD95 added progressively after the basic workflow is understood and operational.

The initial conceptual master table contains:

| Field | Intended role |
|---|---|
| `case_id` | Traceable research identifier |
| `thickness_mm` | Reconstruction condition |
| `lesion_size_ref_mm` | Fixed size measure from the 1 mm reference condition |
| `volume_cm3` | Segmented volume |
| `absolute_volume_change` | Absolute difference from the defined comparator |
| `percentage_volume_change` | Relative difference from the defined comparator |
| `dice` | Spatial overlap |
| `asd_mm` | Average surface distance when added |
| `hd95_mm` | 95th-percentile surface-distance summary when added |
| `qc_notes` | Standardized visual-review observations |
| `included` | Inclusion status |
| `exclusion_reason` | Predefined reason when excluded |

No fictitious rows were created. Excluded cases should remain traceable through `case_id`, status,
and reason. A didactic flow of 50 evaluated, 4 excluded, and 46 analyzed showed how cohort
accounting preserves reproducibility. If excluded cases share characteristics, such as all being
very small lesions, the analyzed distribution and representativeness may change. The numbers were
hypothetical. This connects exclusion criteria with selection bias, representativeness, and
reproducibility.

Scientific English appeared through contextual terminology including *dataset*, *data
provenance*, *data dictionary*, *slice thickness*, *reference condition*, *reference
segmentation*, *ground truth*, *surface distance*, *included*, *excluded*, and *quality control*.
No separate English exercise or conversational competence was completed or claimed.

## Practical Workflow

The protocol at the end of Lesson 16 remained under development:

```text
verified public dataset candidate
    ↓
provenance, license, terms, and privacy review
    ↓
acquisition/reconstruction metadata and segmentation-provenance review
    ↓
data-dictionary and missing-information review
    ↓
predefined inclusion/exclusion criteria and traceable cohort accounting
    ↓
same acquisition and originally thin reconstruction when possible
    ↓
1 mm reference; optional 1.5 mm; 3 mm and 5 mm comparisons
    ↓
fixed lesion-size stratum derived from the reference condition
    ↓
standardized independent segmentation protocol
    ↓
volume, absolute and percentage volume change, and Dice
    ↓
progressive ASD and HD95 addition
    ↓
visual QC and magnitude-aware interpretation
    ↓
reproducible master table with documented exclusions
```

This workflow was defined but not executed. No dataset, medical image, segmentation, screenshot,
measurement, surface, metric, table row, or experimental result was produced.

## Quality Checklist

- [ ] Candidate CT data answer the defined scientific question.
- [ ] Provenance, license, terms, privacy, and redistribution conditions are verified.
- [ ] Originally thin reconstruction is distinguished from interpolation of thick data.
- [ ] Same-acquisition reconstruction conditions are preferred when appropriate.
- [ ] Partial-volume implications are considered without claiming they were measured.
- [ ] Small-lesion availability and intended population are documented.
- [ ] Segmentation method, observers, review, software, protocol, reconstruction, and QC are reviewed.
- [ ] Reference segmentation and reference condition are not called ground truth.
- [ ] DICOM or NIfTI suitability is judged by required information, not file extension alone.
- [ ] Missing metadata are identified, investigated, and assessed against the main question.
- [ ] Data-dictionary definitions, units, values, origins, and calculation methods are reviewed.
- [ ] Current lesion size is distinguished from temporal change.
- [ ] Diameter and volume are assigned distinct, justified roles.
- [ ] Size strata are derived from 1 mm and kept fixed across comparisons.
- [ ] Original and independently derived lesion measurements remain distinguishable.
- [ ] The optional 1.5 mm condition is included only if technically justified.
- [ ] Reference and adjacent comparisons are predefined without assuming a trend.
- [ ] Volume and Dice are interpreted as complementary outcomes.
- [ ] ASD, HD, and HD95 remain introductory concepts without universal thresholds.
- [ ] Surface-distance metrics are interpreted with visual QC and lesion magnitude.
- [ ] Extreme discrepancies are investigated rather than removed for result favorability.
- [ ] The pilot remains limited to variables with explicit scientific roles.
- [ ] Every evaluated case retains inclusion status and any exclusion reason.
- [ ] Effects of exclusions on selection bias and representativeness are reviewed.
- [ ] All numerical examples remain explicitly hypothetical.
- [ ] No dataset selection, download, analysis, segmentation, metric, or validation is implied.
- [ ] No private data, PHI, patient name, or clinical identifier is present.

## Lessons Learned

1. A thick reconstruction cannot be assumed to contain recoverable fine spatial information.
2. Finer interpolation and originally finer reconstruction are not equivalent.
3. Partial volume can affect boundary, intensity, lesion representation, and segmentation behavior.
4. Same-acquisition reconstructions may reduce unrelated variation in a thickness study.
5. Small lesions are central because fixed spatial differences may have greater relative importance.
6. Segmentation provenance must be reviewed before a mask is used as a reference.
7. A reference segmentation and an operational reference condition are not anatomical ground truth.
8. DICOM and NIfTI must be judged by whether required information remains available.
9. Missing metadata should be investigated before automatic dataset rejection.
10. A data dictionary is necessary to interpret variable definition, unit, source, and method.
11. `lesion_size` does not explain its measurement type, unit, method, or time point by itself.
12. Current size and temporal change answer different questions.
13. Diameter may support stratification while volume measures a different quantitative property.
14. Fixing strata from the 1 mm reference avoids thickness-dependent group reassignment.
15. Original dataset measurements and project-derived measurements should remain traceable.
16. The 1.5 mm condition is optional and depends on future technical suitability.
17. Reference and adjacent comparisons answer complementary questions.
18. Volume and Dice do not fully describe localized boundary differences.
19. ASD summarizes average surface behavior; HD is sensitive to a farthest discrepancy.
20. HD95 reduces single-point dominance but is not arbitrary outlier removal.
21. Average and localized surface behavior may tell different parts of the same case.
22. Metric discrepancies require visual and methodological investigation before causal interpretation.
23. Equal absolute surface distance may have different importance across lesion magnitudes.
24. A first pilot benefits from progressive metrics rather than uncontrolled complexity.
25. Excluded cases must remain traceable so cohort flow and possible selection effects are visible.
26. No dataset, experiment, result, or validated protocol was produced in this lesson.

## Future Learning Directions

- Begin Lesson 17 with practical evaluation of candidate public datasets against the requirements
  defined in Lessons 15–16.
- Review official provenance, license, terms, population, reconstruction conditions, segmentation
  provenance, metadata, and data dictionaries before selecting or downloading data.
- Determine whether any candidate can support methodologically comparable 1, optional 1.5, 3,
  and 5 mm conditions.
- Refine the master-table fields, comparator definitions, inclusion rules, and visual-QC record
  only after candidate documentation has been assessed.
- Add ASD and HD95 progressively after the core volume, percentage-change, Dice, and visual-QC
  workflow is understood.
- Continue Scientific English separately through contextual, attempt-first professional practice.
- Do not claim dataset suitability, protocol validation, segmentation robustness,
  generalizability, surface-distance competence, or clinical validity without future evidence.
