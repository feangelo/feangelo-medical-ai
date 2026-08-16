# Lesson 11 – Medical Image Geometry, Resampling and Interpolation

**Learning path:** 3D Slicer  
**Date:** 2026-08-15  
**Status:** Learning record  
**Scope:** Scientific learning documentation; no clinical data or patient-specific conclusions

## Objectives

- Distinguish voxel index from physical position and matrix size from physical size.
- Understand how spacing, origin, direction, and orientation define image geometry in physical or world space.
- Introduce RAS and LPS coordinate conventions without implying that a convention changes patient anatomy.
- Distinguish isotropic from anisotropic voxels.
- Separate acquisition, reconstruction, and resampling conceptually.
- Understand resampling and linear and nearest-neighbor interpolation.
- Match interpolation choices to continuous image intensities and categorical label maps.
- Recognize partial-volume considerations and limitations in small-structure representation.
- Evaluate geometry consistency between an image and its segmentation.
- Understand error propagation, failure modes, and worst-case performance.
- Distinguish computational success from scientific validity and plausibility from anatomical truth.
- Connect image geometry with quantitative imaging, radiomics, and Medical AI.
- Continue scientific English development without claiming language proficiency.

## Scientific Background

### Voxel index and physical position

> Voxel index is not the same as physical position.

A voxel index identifies a location in an array, such as `[100, 100, 100]`. Physical position describes where that sample is located in patient or world coordinates. Conceptually, physical position depends on the index together with spacing, origin, and direction or orientation.

Consider this educational example:

```text
Image A
Matrix:  512 × 512 × 300
Spacing: 1 × 1 × 1 mm
Origin:  (0, 0, 0)

Image B
Matrix:  512 × 512 × 300
Spacing: 1 × 1 × 1 mm
Origin:  (0, 0, 50 mm)
```

Although both arrays have the same matrix and spacing, voxel `[100, 100, 100]` does not necessarily represent the same physical position because their origins differ. Direction also matters, even when the other attributes match.

> Matrix size does not determine physical position.

Matrix size describes the number of samples along each dimension. Approximate physical extent also depends on spacing; physical placement additionally depends on origin and direction. These concepts are introduced without advanced matrix mathematics at this stage.

### Components of image geometry

- **Spacing:** physical distance represented between neighboring voxel centers along each axis.
- **Origin:** physical coordinate assigned to the reference point of the image grid.
- **Direction or orientation:** relationship between image axes and anatomical or world axes.
- **Physical or world space:** coordinate system in which images, segmentations, landmarks, and transformations can be spatially related.

Correct array dimensions alone do not establish correct geometry.

### RAS and LPS

RAS names positive coordinate directions as Right, Anterior, and Superior. LPS names them as Left, Posterior, and Superior. Software ecosystems may use different conventions to represent the same anatomy.

A correct coordinate-system conversion changes the numerical representation while preserving the intended anatomical relationship. An intentional geometric transformation deliberately changes the representation or spatial pose for a justified purpose. Incorrect or lost orientation metadata can instead cause data to be interpreted in the wrong anatomical space.

> A transformed representation can preserve geometry while changing anatomical coordinates.

A consistent reflection may preserve quantities such as volume and distances while changing anatomical coordinates or laterality. The scientific problem arises when transformed or incorrectly oriented data are interpreted as if they remained in the original or correct anatomical space. Different coordinate conventions do not mean that patient anatomy itself has changed.

### Isotropic and anisotropic voxels

Isotropic voxels have similar spacing in all three directions, such as `1 × 1 × 1 mm`. Anisotropic voxels have unequal spacing, such as `0.7 × 0.7 × 5 mm`. Anisotropy can limit through-plane representation even when the in-plane image appears detailed.

### Acquisition, reconstruction, and resampling

- **Acquisition:** measurement of data by the imaging system.
- **Reconstruction:** creation of an image representation from acquired measurements using defined methods and parameters.
- **Resampling:** evaluation of an existing image on a different spatial grid.

These are related but not equivalent processes.

> More slices do not necessarily mean more acquired information.

> Resampling can standardize voxel spacing, but it cannot recover information that was not acquired.

> Interpolation estimates information; acquisition measures information.

> Processing may transform the representation of medical imaging data, but the information relevant to the scientific question must be preserved, quantified, and validated.

The requirement is not to prohibit legitimate transformation. It is to avoid losing or misrepresenting biologically or anatomically relevant information and to evaluate whether the transformed representation remains suitable for the intended scientific task.

### Matrix size and physical extent

Consider:

```text
Image A: 512 × 512 × 300 at 1 × 1 × 1 mm
Image B: 256 × 256 × 150 at 2 × 2 × 2 mm
```

These images may cover approximately the same physical extent despite different matrices. If Image B is resampled to `1 × 1 × 1 mm`, the resulting grid contains more voxels, but no new anatomical measurement was acquired.

> Standardized voxel spacing does not imply standardized image information.

### Small-lesion and partial-volume considerations

In an educational example, an approximately 6 mm lesion is represented in data with spacing near `0.7 × 0.7 × 5 mm`. Through-plane sampling may intersect the lesion only sparsely, and individual voxels may combine signals from the lesion and neighboring tissue through partial-volume effects.

Resampling this image to `1 × 1 × 1 mm` creates a denser grid, but it does not make the source equivalent to an acquisition or reconstruction that originally preserved sufficiently fine information in that direction. Interpolation can alter how boundaries and intensities are represented, with possible consequences for volume, shape, intensity, and other quantitative measurements. It should not be described simplistically as automatically adding healthy tissue.

### Interpolation of continuous intensities

Interpolation estimates values on a new grid from existing samples. For a simplified CT example:

```text
20 HU ---- ? ---- 40 HU
```

Linear interpolation may estimate approximately `30 HU` between the two source samples. That value was computed from existing measurements; it was not newly measured from the patient.

Medical-image intensities are commonly treated as continuous quantities for interpolation, but the appropriate method still depends on modality, task, processing assumptions, and validation.

### Interpolation of categorical labels

Consider a label map:

```text
0 = background
1 = liver
2 = tumor
```

Linear interpolation can generate intermediate numerical values that do not correspond to any defined class. Nearest-neighbor interpolation selects the spatially nearest source voxel and copies its label.

Nearest neighbor does **not** mean rounding a numerical value such as `1.9` to `2`. It refers to spatial proximity, not numerical proximity.

For categorical label maps, nearest neighbor can preserve the discrete label set. However:

> Correct labels do not guarantee correct geometry.

> Preserving labels does not guarantee preserving anatomy perfectly.

Boundary placement can still change when a mask is evaluated on a different grid. Image and segmentation must share the intended physical-space correspondence, not merely compatible array shapes.

### Numbers as data

A number may represent a continuous quantity, an ordinal category, or a nominal/categorical label. Mathematical operations must respect what the number means. Averaging nearby continuous intensity samples may be meaningful under appropriate assumptions; averaging arbitrary class identifiers generally is not.

### Geometry consistency between image and segmentation

A segmentation can have valid class values and still be spatially incorrect if spacing, origin, direction, or coordinate interpretation is inconsistent with its source image. Visual overlay, physical-space metadata, anatomical location, and quantitative comparisons should therefore be reviewed together.

### Multicenter radiomics learning example

Consider Hospital A with approximately 1 mm data and Hospital B with approximately 5 mm data, including small lesions around 5–10 mm. These values define an educational scenario, not a dataset that was analyzed and not universal clinical thresholds.

Simply resampling both centers to `1 × 1 × 1 mm` does not make the originally acquired information equivalent. A future experimental robustness strategy could:

1. Analyze each center under its original condition.
2. Establish baseline or reference-condition results.
3. Test controlled transformations.
4. Where scientifically appropriate, degrade higher-resolution data to study information loss.
5. Resample lower-resolution data and quantify interpolation-related changes in measurements or features.
6. Compare original and transformed conditions.
7. Investigate which features remain robust.
8. Stratify results by relevant variables such as lesion size.
9. Only then decide how preprocessing or harmonization should enter the final study.

An original image is not automatically Ground Truth. **Reference condition** or **baseline condition** is more accurate unless an actual task reference standard exists.

No radiomics dataset, feature-robustness experiment, or harmonization pipeline was implemented during this lesson.

### Reconstruction, enhancement, and anatomical truth

A visually cleaner image may result from acquisition improvements, reconstruction choices, denoising, iterative reconstruction, deep-learning reconstruction, or other processing. No vendor or model is assigned a particular method here.

If a structure becomes visible only after AI-based enhancement or super-resolution, researchers must determine whether the output is supported by acquired data rather than merely anatomically plausible. A **hallucination** is an output that appears plausible but is not adequately supported by the input evidence. A **failure mode** describes a way in which a system can fail; **worst-case performance** examines behavior in especially difficult or consequential conditions.

> Better image quality does not automatically mean greater anatomical truth.

> Plausibility does not equal truth.

> A successful computation does not guarantee a scientifically valid result.

Overall metrics may look strong while a subgroup—such as very small or low-contrast lesions—performs poorly. Educational lesion-size groups such as `<5 mm`, `5–10 mm`, and `>10 mm` can illustrate stratification, but they are not universal clinical cutoffs and no results are claimed.

> Global metrics can hide important local or subgroup errors.

### Anonymized professional imaging reflections

The following observations are learning context from professional imaging experience. They are not scientific evidence, formal experiments, clinical guidance, or procedural instructions.

#### CT-guided biopsy reflection

During CT-guided procedures, a larger reference acquisition may initially help localize a lesion, while smaller repeated acquisitions may be used as needle progression is assessed. Respiration or patient movement can change spatial correspondence, and a new wider reference acquisition may be obtained when the previous spatial reference is no longer reliable.

This reflection illustrates only that the same patient does not guarantee the same physical correspondence over time.

#### Temporal-bone and ear CT reflection

Dedicated temporal-bone or ear CT protocols can use very thin reconstructions and task-specific reconstruction characteristics because relevant anatomy includes very small structures. Attempting to produce ear-like thin reconstructions from examinations acquired or reconstructed for another purpose, such as general head or sinus imaging, may produce visually inadequate results.

This observation illustrates `Acquisition ≠ Reconstruction ≠ Resampling` and that more slices do not necessarily mean more acquired information. It makes no vendor-specific claim.

#### Different CT generations reflection

Images from an older CT system and a newer system may look substantially different. The scientific question is whether the newer or cleaner appearance reflects improved anatomical information, different reconstruction or processing, or a combination. Validation is required rather than assuming either `older = truth` or `newer = truth`.

All institution, vendor, and patient references remain generic and anonymized.

### Error propagation

```text
scientific question
    ↓
protocol
    ↓
acquisition
    ↓
reconstruction
    ↓
preprocessing
    ↓
segmentation
    ↓
registration / spatial correspondence
    ↓
radiomics
    ↓
AI / statistics
    ↓
final result
```

An error or bias introduced early can propagate downstream even when every later software step executes successfully. Scientific validity therefore requires more than computational completion.

### Scientific English vocabulary

Terms introduced or practiced included: voxel index, physical position, physical space, world space, spacing, origin, direction, orientation, coordinate system, RAS, LPS, isotropic, anisotropic, resampling, interpolation, linear interpolation, nearest neighbor, continuous intensity, categorical label, label map, partial volume, image geometry, spatial correspondence, reference condition, baseline condition, error propagation, failure mode, worst-case performance, hallucination, and scientific validity.

Sentences practiced during this learning session included:

> Voxel index is not the same as physical position.

> Resampling can standardize voxel spacing, but it cannot recover information that was not acquired.

> Interpolation estimates information; acquisition measures information.

> Correct labels do not guarantee correct geometry.

> Plausibility does not equal truth.

These terms and sentences document scientific English practice; they do not imply English-language proficiency.

## Practical Workflow

A conceptual geometry-aware resampling workflow is:

```text
Define the scientific question
    ↓
Inspect matrix, spacing, origin, and direction
    ↓
Confirm coordinate convention and physical-space interpretation
    ↓
Assess source resolution, anisotropy, and partial-volume risk
    ↓
Define the justified target grid
    ↓
Select interpolation by data meaning
    ├── image intensity → appropriate intensity interpolation
    └── categorical mask → appropriate label-preserving interpolation
    ↓
Resample image and mask consistently
    ↓
Verify geometry and physical correspondence
    ↓
Compare original and transformed representations
    ↓
Evaluate downstream quantitative sensitivity
    ↓
ACCEPT / REVIEW / REJECT
```

No production resampling pipeline or quantitative experiment was implemented during this lesson.

## Quality Checklist

After `CT → appropriate intensity interpolation` and `Mask → appropriate label-preserving interpolation`, do not accept the result merely because software reports success.

- [ ] Scientific question and target representation are defined.
- [ ] Source matrix and physical extent are understood.
- [ ] Expected spacing is verified.
- [ ] Origin is verified.
- [ ] Direction and orientation are verified.
- [ ] Coordinate convention is understood.
- [ ] Physical-space correspondence is verified.
- [ ] Image and mask remain aligned.
- [ ] Anatomical location and laterality are reviewed.
- [ ] Visual overlay is inspected.
- [ ] Lesion and small-structure representation are reviewed.
- [ ] Volume before and after transformation is compared.
- [ ] Shape and boundary changes are assessed.
- [ ] Intensity changes are assessed when relevant.
- [ ] Partial-volume and anisotropy limitations are documented.
- [ ] Interpolation matches the meaning of the data.
- [ ] Downstream quantitative sensitivity is evaluated when relevant.
- [ ] Processing limitations and failure modes are documented.
- [ ] Scientific validity is assessed separately from computational success.

## Lessons Learned

1. Voxel index is not the same as physical position.
2. Matrix size does not determine physical position or physical extent by itself.
3. Spacing, origin, and direction jointly define image geometry.
4. RAS and LPS can represent the same anatomy using different coordinate conventions.
5. Correct coordinate conversion differs from intentional transformation and lost orientation metadata.
6. A reflection can preserve distances and volume while changing anatomical coordinates or laterality.
7. Isotropic resampling does not make originally anisotropic information equivalent to isotropic acquisition.
8. Acquisition, reconstruction, and resampling are distinct processes.
9. More slices do not necessarily mean more acquired information.
10. Resampling standardizes a grid but cannot recover information that was not acquired.
11. Linear interpolation estimates continuous values rather than measuring new patient data.
12. Nearest neighbor refers to spatial proximity, not numerical rounding.
13. Label-preserving interpolation does not guarantee perfect anatomical boundary preservation.
14. Correct labels do not guarantee correct geometry.
15. Mathematical operations must respect whether numbers are continuous, ordinal, or categorical.
16. Standardized voxel spacing does not imply standardized image information.
17. Small structures can be especially sensitive to sparse sampling, partial volume, and interpolation.
18. An original image is not automatically Ground Truth.
19. Better appearance does not automatically establish greater anatomical truth.
20. Global metrics can hide important local or subgroup errors.
21. Plausibility does not equal truth.
22. Computational success does not guarantee scientific validity.
23. Early geometry or preprocessing errors can propagate through downstream analysis.
24. Processing may transform representation, but scientifically relevant information must be preserved, quantified, and validated.

## Future Learning Directions

- Implement physical-coordinate calculations using index, spacing, origin, and direction.
- Study affine matrices and homogeneous coordinates after the conceptual foundation is secure.
- Compare RAS and LPS handling across 3D Slicer, DICOM, NIfTI, and SimpleITK.
- Perform controlled image and label-map resampling exercises in 3D Slicer and Python.
- Compare linear, nearest-neighbor, B-spline, and other interpolation methods for appropriate tasks.
- Quantify volume, surface, boundary, and intensity changes after resampling.
- Study partial-volume modeling and small-lesion measurement uncertainty.
- Design controlled multicenter robustness experiments with baseline and transformed conditions.
- Investigate radiomics feature stability without assuming that common spacing creates equivalent information.
- Study reconstruction and enhancement validation, hallucination risk, and worst-case performance.
- Examine uncertainty propagation across segmentation, registration, radiomics, and AI pipelines.
- Make no claim of implementation proficiency until practical work and validation provide supporting evidence.
