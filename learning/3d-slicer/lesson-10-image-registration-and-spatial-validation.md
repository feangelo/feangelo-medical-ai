# Lesson 10 – Image Registration and Spatial Validation

**Learning path:** 3D Slicer  
**Date:** 2026-08-14  
**Status:** Learning record  
**Scope:** Scientific learning documentation; no clinical data or patient-specific conclusions

## Objectives

- Understand why longitudinal images cannot be compared solely by slice number and introduce spatial correspondence and image registration.
- Distinguish Fixed and Moving images and rigid, affine, and deformable registration conceptually.
- Understand degrees of freedom and why increasing transformation flexibility increases validation requirements.
- Recognize that registration should preserve biologically meaningful differences when they are the study target.
- Understand why visual alignment alone does not establish valid registration.
- Introduce anatomical landmarks, Target Registration Error (TRE), and observer variability in landmark placement.
- Distinguish global from local registration performance and connect Dice with surface- and distance-based evaluation.
- Introduce Hausdorff Distance, HD95, Mean Squared Error, Mutual Information, optimizers, and regularization conceptually.
- Understand why multimodal registration may require a different similarity strategy from same-modality registration.
- Connect registration validation with task-specific validation and AI segmentation evaluation.
- Introduce external validation, multicenter generalization, domain shift, fine-tuning, domain adaptation, and leave-one-center-out evaluation.
- Develop root-cause reasoning for Medical AI performance degradation across hospitals.
- Continue scientific English development without claiming language proficiency.

## Scientific Background

> The images must be aligned before quantitative comparison.

Images from the same patient at different time points are not automatically spatially equivalent. Positioning, rotation, respiration, motion, organ deformation, anatomical or treatment-related changes, acquisition geometry, field of view (FOV), voxel spacing, and orientation can differ.

> Same slice number does not mean same anatomical location.

This extends Lesson 09: DICOM geometry and image position are necessary context, but longitudinal quantitative comparison also requires appropriate spatial correspondence.

### Image registration

Image registration conceptually establishes spatial correspondence between two or more images:

```text
Fixed Image
    +
Moving Image
    ↓
Transformation
    ↓
Spatial alignment
```

The Fixed Image provides the reference space; the Moving Image is transformed toward that space. Registration changes the spatial representation used for comparison, not the patient's actual biology.

### Rigid registration

Rigid registration primarily permits translation and rotation while preserving shape and distances. In three dimensions, it can be understood conceptually as:

```text
3 translations + 3 rotations = 6 degrees of freedom
```

In a hypothetical learning exercise, two head CT examinations differed by approximately 7 degrees and a small displacement, without a major expected anatomical change. Rigid registration was selected conceptually because rotation and translation could address the positioning difference without intentionally deforming anatomy. No registration was performed and the value was not an experimental result.

### Affine registration

Affine registration adds global flexibility through translation, rotation, scaling, and shear. Transformation matrices are not studied in depth here. Additional geometric freedom requires methodological justification because the transformation may alter global shape and scale.

### Deformable registration

Deformable registration permits local spatial transformations. A conceptual comparison of lung CT at deep inspiration and expiration illustrates why translation and rotation alone may not establish regional correspondence when an organ actually deforms. Deformable registration may therefore be appropriate, but its transformation still requires evaluation and validation.

> More complex does not always mean better.

```text
Rigid      → limited freedom
Affine     → greater global freedom
Deformable → local deformation freedom
```

Increasing transformation flexibility generally increases the need for appropriate constraints, justification, and validation. Rigid registration is not always safer, and deformable registration is not always superior.

### Biological change versus registration

In a hypothetical longitudinal example, a liver tumor measured 4.0 cm at baseline and 2.5 cm at follow-up. An overly aggressive deformable transformation made the tumor regions appear nearly equivalent. This is scientifically problematic when tumor change is the target: registration should not automatically force biologically meaningful differences to disappear.

The baseline-to-follow-up difference may be exactly what the study intends to evaluate. Imaging changes may be associated with treatment response, but imaging measurements alone do not automatically establish clinical treatment efficacy. These values are illustrative; no patient, dataset, or experiment was analyzed.

Technical or spatial differences may include translation, rotation, positioning, and respiratory state. Biological or anatomical differences may include tumor-size change, disease-related organ displacement, and treatment-related anatomical change. Separating these sources can be difficult. Consistent with Lesson 08, a difference should not be removed before understanding whether it is technical or biological.

In another hypothetical example, a liver tumor decreased while a nearby vessel changed position. A deformable algorithm attempted to force the vessel to its former location. The displacement might partly represent real anatomical change rather than positioning error. The learner proposed avoiding uncontrolled deformation in the biological region of interest and evaluating it carefully. This was reasoning practice, not a validated clinical method.

### Registration validation and landmarks

> Good visual alignment does not guarantee valid registration.

Visual assessment—potentially including alternating images or split views—is useful but insufficient. Validation may combine visual inspection, anatomical landmarks, quantitative measures, local assessment, and task-specific evaluation.

Anatomical landmarks are reproducible corresponding points, such as appropriate vascular bifurcations or osseous references. Their relevance depends on anatomy and the scientific question.

Target Registration Error (TRE) describes residual spatial discrepancy between corresponding target points after registration. In an illustrative example, discrepancy changed from 12 mm before registration to 2 mm afterward. These values demonstrate the concept only and are not experimental findings.

Another hypothetical exercise compared Registration A, which looked excellent but had mean TRE of 8 mm, with Registration B, which looked less impressive but had mean TRE of 2 mm. Lower TRE may be favorable, but interpretation requires examining landmark placement, anatomical relevance, landmark distribution, the region of interest, and observer variability. These values are illustrative. A metric is useful only if it measures something relevant to the scientific question.

Excellent alignment of osseous landmarks does not automatically demonstrate accurate liver registration because bone behaves relatively rigidly compared with deformable abdominal soft tissue. An illustrative osseous TRE of 0.8 mm could coexist with inadequate hepatic correspondence.

> Validation must reflect the intended task.

Landmark placement can vary between observers and within the same observer. **Inter-observer variability** describes differences between observers, while **intra-observer variability** describes differences when the same observer repeats placement. A strong strategy may therefore include multiple anatomically relevant landmarks, clear placement criteria, more than one observer when appropriate, observer-variability assessment, visual inspection, quantitative metrics, and region-specific analysis.

### Global and local performance

> Excellent global registration metrics do not guarantee accurate local registration.

In a hypothetical liver exercise, Method A produced global liver Dice of 0.97 but a 6 mm local error near an 8 mm tumor. Method B produced global Dice of 0.91 and a 1 mm local error near the tumor. Because the tumor is small relative to the liver, global overlap may remain excellent despite a locally important discrepancy. All values are hypothetical.

Dice measures overlap and can evaluate correspondence between segmented structures, but high Dice does not guarantee small local spatial errors. Large structures can dominate global overlap.

Hausdorff Distance and HD95 address spatial discrepancy rather than overlap. HD95 is commonly used to reduce sensitivity to isolated extreme discrepancies compared with maximum Hausdorff Distance. In an illustrative comparison, Method A had Dice 0.95 and HD95 12 mm, while Method B had Dice 0.92 and HD95 2 mm. Neither metric is universally superior; they describe different performance aspects.

### Small-lesion performance and critical paper reading

A hypothetical AI segmentation paper reported liver Dice 0.98, Dice 0.91 for tumors larger than 5 cm, 0.76 for tumors of 1–2 cm, and 0.48 for tumors smaller than 1 cm. These are invented learning values, not published or experimental results. They illustrate how aggregate metrics may hide subgroup failures and how small structures may be disproportionately affected by boundary errors.

Relevant concepts include subgroup analysis, stratification, and distribution; confidence intervals remain future learning. Questions for critical paper reading include:

- What structure was segmented, and how was aggregate Dice calculated?
- Was the summary a mean or median, and what was the patient-level distribution?
- How did performance change with lesion size, and what were the surface errors?
- Was there external validation, and how was Ground Truth defined?
- Which centers, scanners, and protocols were represented?

A high headline metric does not replace methodological evaluation.

### Similarity metrics, transformations, and optimization

Registration algorithms require a criterion for correspondence. Mean Squared Error (MSE) and Mutual Information (MI) are introduced conceptually, without formulas.

For CT-to-CT registration, corresponding voxel intensities may have a more direct relationship than in PET-to-CT registration. PET and CT represent different functional or physical properties; therefore, the same anatomy does not imply equal intensities across modalities. MI can be useful in multimodal contexts because it does not simply require equal values, but it is not universally superior.

```text
Fixed Image + Moving Image
           ↓
Transform + Similarity Metric + Optimizer
           ↓
Registered Image
```

- **Transform:** defines permitted spatial changes.
- **Similarity metric:** scores correspondence under the selected objective.
- **Optimizer:** searches transformation parameters to improve that objective.

Conceptually, an optimizer may rotate slightly, evaluate, translate slightly, evaluate, and continue according to improvement or worsening. Actual methods are more sophisticated.

> Optimizing the metric does not necessarily mean solving the scientific problem.

If a metric rewards alignment of most of the liver while a small tumor remains poorly aligned, the optimizer may correctly optimize the objective it received even though the objective is insufficient for the task.

Regularization conceptually constrains or controls deformable transformation behavior. Greater freedom may improve correspondence but can also permit unrealistic or scientifically undesirable deformation. Mathematical implementation is deferred.

Different modality does not automatically mean different anatomy. In a PET/CT exercise, the learner rejected the claim that different modalities make deformable registration mandatory. Modality relationships influence similarity strategy; anatomical and geometric differences influence transformation requirements. These decisions are related but distinct.

### External validation, multicenter AI, and domain shift

Registration validation principles connect with task-specific AI model validation. In a hypothetical dataset, Hospitals A, B, C, and D contributed 4,000, 1,000, 800, and 500 patients, respectively, for a total of 6,300. A pooled random split of 80% training, 10% validation, and 10% test could place patients from every center in each partition. It does not by itself strongly demonstrate generalization to an unseen hospital.

A stronger conceptual external-center design could use Hospitals A, B, and C for training and validation while keeping Hospital D entirely outside development for external testing. This offers stronger evidence about a center not represented during development.

Leave-one-center-out evaluation can be conceptualized as:

```text
Train B+C+D → Test A
Train A+C+D → Test B
Train A+B+D → Test C
Train A+B+C → Test D
```

It may reveal center-specific degradation, although it is not always the required or optimal design.

Domain shift occurs conceptually when a model encounters a meaningfully different target distribution. Possible contributors include hospital type, population, disease prevalence, lesion-size distribution, scanner manufacturer/model/software, acquisition parameters, slice thickness, spacing, kernel, contrast phase and timing, body habitus, quality, motion, artifacts, positioning, incomplete transfer, Ground Truth methodology, annotation protocol, observer variability, and preprocessing. These factors do not necessarily cause domain shift in every study.

In a hypothetical exercise, initial external Hospital D Dice was 0.62. After Hospital D data were used for adaptation or fine-tuning, Dice was 0.88 on held-out Hospital D patients. The first value evaluates performance before exposure; the second evaluates performance after adaptation. The latter should not replace the former as evidence of untouched external generalization. Both questions may be valuable. All values are hypothetical.

Fine-tuning means continuing model training with additional data after initial development. Domain adaptation refers broadly to strategies intended to improve performance when the target domain differs. Implementation is not taught here.

### Root-cause analysis of model failure

In the final hypothetical exercise, a model performed substantially worse at Hospital D. Before changing the model, the learner proposed investigating:

- **Center and population:** hospital profile, specialties, population, disease prevalence, lesion distribution, body habitus, and relevant permitted comorbidities.
- **Scanner and protocol:** manufacturer, model, software, acquisition parameters, thickness, spacing, reconstruction, contrast timing and phase, and series-naming differences.
- **Image quality:** motion, respiratory and other artifacts, positioning, completeness, transfer failures, and anatomical coverage.
- **Ground Truth:** annotation method, annotators and their relevant experience, review or adjudication when appropriate, observer variability, and protocol.
- **Validation:** task-appropriate metrics, local versus global performance, anatomical plausibility, and deformation when registration is involved.

Landmarks are particularly relevant when spatial correspondence is part of the problem; they are not mandatory for every segmentation failure investigation.

> Before changing the model, investigate what changed in the data.

### Scientific English vocabulary

Vocabulary introduced or practiced included: registration, alignment, aligned, Fixed Image, Moving Image, rigid, affine, deformable, translation, rotation, scaling, shear, degrees of freedom, landmark, Target Registration Error, global, local, valid, validation, reflect, intended, task, similarity, metric, optimizer, regularization, overlap, distance, Hausdorff Distance, HD95, external validation, generalization, domain shift, fine-tuning, domain adaptation, subgroup, stratification, distribution, can, hide, more complex, always, mean, and better.

Sentences practiced during the learning session:

> The images must be aligned before quantitative comparison.

> Good visual alignment does not guarantee valid registration.

> Validation must reflect the intended task.

> Excellent global registration metrics do not guarantee accurate local registration.

> Global metrics can hide important local errors.

> More complex does not always mean better.

> Same slice number does not mean same anatomical location.

> Optimizing the metric does not necessarily mean solving the scientific problem.

> Before changing the model, investigate what changed in the data.

These are scientific English terms and sentences practiced during this learning session; they do not imply English-language proficiency.

## Practical Workflow

The conceptual registration decision workflow developed during the lesson was:

```text
Define scientific question
    ↓
Identify Fixed and Moving images
    ↓
Assess modalities
    ↓
Assess expected anatomical change
    ↓
Determine what differences should be corrected
    ↓
Determine what biological differences must be preserved
    ↓
Start with the least complex transformation appropriate to the task
    ↓
Select appropriate similarity strategy
    ↓
Perform registration
    ↓
Visual QC
    ↓
Landmark / target-region QC when appropriate
    ↓
Global metrics
    ↓
Local metrics
    ↓
Biological plausibility
    ↓
PASS / REVIEW / REJECT
```

No registration experiment was executed during this lesson. No production registration pipeline was implemented.

## Quality Checklist

- [ ] Scientific question defined.
- [ ] Fixed Image and Moving Image defined.
- [ ] Modalities identified.
- [ ] Anatomical and technical changes considered.
- [ ] Biological differences identified.
- [ ] Transformation complexity justified.
- [ ] Rigid registration considered before unnecessary deformation when appropriate.
- [ ] Affine and deformable use justified when applicable.
- [ ] Similarity metric appropriate to modality and task.
- [ ] Optimizer objective understood conceptually.
- [ ] Registration visually reviewed.
- [ ] Relevant anatomical regions reviewed.
- [ ] Landmarks appropriate to the task when used.
- [ ] Landmark distribution and observer variability considered.
- [ ] TRE interpreted in anatomical context.
- [ ] Global overlap and local performance reviewed.
- [ ] Distance-based metrics considered when relevant.
- [ ] Small structures evaluated separately when relevant.
- [ ] Biologically meaningful changes preserved.
- [ ] Unreasonable deformation investigated.
- [ ] Final registration validated for the intended task.

## Lessons Learned

1. Registration establishes spatial correspondence; it is not merely image overlay.
2. Fixed and Moving images have distinct roles.
3. Rigid registration preserves shape while correcting translation and rotation.
4. Affine registration introduces additional global geometric freedom.
5. Deformable registration allows local transformations.
6. More complex does not always mean better.
7. Increased transformation flexibility increases validation responsibility.
8. Registration should not erase biologically meaningful differences that are the study target.
9. Good visual alignment does not guarantee valid registration.
10. Landmarks must be anatomically relevant to the intended task.
11. Low TRE in bone does not automatically prove accurate soft-tissue registration.
12. Landmark placement itself may contain observer variability.
13. Global metrics can hide important local errors.
14. Dice measures overlap but does not fully describe spatial error.
15. Distance-based metrics provide complementary information.
16. Small lesions need specific attention because global metrics may hide poor local performance.
17. Similarity metrics must suit the modalities being registered.
18. Different PET and CT modalities do not automatically require deformable registration.
19. Optimizing a metric does not necessarily solve the scientific problem.
20. Validation must reflect the intended task.
21. Multicenter training does not automatically prove external generalization.
22. A truly unseen center provides stronger evidence about external generalization.
23. Fine-tuning after exposure to an external center changes the scientific question.
24. Domain shift should be investigated before blindly modifying a model.
25. Data, Ground Truth, acquisition, population, and validation methodology can all contribute to apparent model failure.

## Future Learning Directions

- Perform practical registration in 3D Slicer.
- Study transformation matrices, coordinate systems, RAS/LPS, resampling, and interpolation methods.
- Study SimpleITK registration and later consider elastix or other registration frameworks when appropriate.
- Implement anatomical landmarks, TRE calculation, surface distance, Hausdorff Distance, and HD95.
- Study deformation fields, Jacobian determinants, regularization methods, inverse consistency, and registration uncertainty.
- Study Mutual Information mathematics and optimization algorithms.
- Develop longitudinal imaging pipelines and investigate PET/CT, PET/MRI, and other multimodal registration contexts.
- Study external-validation design, multicenter AI, leave-one-center-out validation, and domain-shift detection.
- Study domain adaptation and fine-tuning without confusing adaptation results with untouched external validation.
- Learn statistical confidence intervals, subgroup analysis, and model calibration.
- Make no claim of practical registration proficiency until future implementation and validation provide supporting evidence.
