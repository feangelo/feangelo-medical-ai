# Lesson 20 – RIDER-LUNG-CT: First Experimental Lesion Segmentation

**Learning path:** 3D Slicer
**Date:** 2026-09-01
**Status:** Learning record
**Scope:** First practical lesion segmentation in the RIDER-LUNG-CT pilot using the 1.25 mm STANDARD reconstruction; no cross-thickness comparison, quantitative metric, radiomics analysis, statistical inference, or clinical conclusion

## Objectives

- Perform the first practical lesion segmentation in the RIDER-LUNG-CT pilot.
- Evaluate the lesion-specific limitations of a global HU threshold.
- Examine how mask connectivity affects connected-component filtering with Islands.
- Apply Grow from Seeds as an interactive semiautomatic segmentation strategy.
- Perform multi-planar visual quality control before accepting the preview.
- Save the segmentation with a reproducible case-and-condition naming convention.
- Recognize segmentation-method variability as a potential confounder in the planned slice-thickness experiment.

## Scientific Background

### Continuity from Lessons 15–19

Lessons 15–16 developed a study design for investigating how CT reconstruction conditions,
especially slice thickness, may affect lesion segmentation and quantitative measurements.
Lessons 17–19 audited RIDER-LUNG-CT, selected a public pilot case, imported CT and SEG data,
verified the source association of the dataset-provided SEG, and documented an unresolved
semantic/anatomical discrepancy in that reference segmentation.

Lesson 20 began independent practical segmentation on a native CT reconstruction. It did not
complete the planned experiment.

### Dataset, case, and controlled reconstruction design

The public **RIDER-LUNG-CT** collection is hosted by The Cancer Imaging Archive (TCIA), DOI
[`10.7937/k9/tcia.2015.u1x8a5nr`](https://doi.org/10.7937/k9/tcia.2015.u1x8a5nr). The practical
pilot continued with the public, de-identified research case `RIDER-1129164940`, study date
2006-09-05, Study Instance UID
`1.3.6.1.4.1.14519.5.2.1.295526028989915648257590762384148204592`.

The larger experimental question remains:

> How much does reconstructed CT slice thickness affect the measured volume and spatial
> segmentation of the same pulmonary lesion when reconstruction kernel and segmentation
> protocol are controlled?

To avoid deliberately mixing kernel and thickness effects, the working pilot design uses native
STANDARD reconstructions:

```text
1.25 mm STANDARD
    versus
2.5 mm STANDARD
    versus
5 mm STANDARD
```

The local NBIA manifest and the previously documented audit identify the loaded 1.25 mm STANDARD
condition as **Series 100**, with 262 images. Series 101 is the 5 mm STANDARD reconstruction and
was not segmented in this lesson. The dataset-provided SEG associated with 2.5 mm STANDARD may
support future localization and comparison, but it is not treated as unquestionable ground truth.
Copying or propagating that mask would not constitute independent segmentation.

### Intensity, anatomy, and segmentation variability

Overlapping HU values do not imply identical anatomy. A global threshold may include the target
and multiple nontarget tissues when their attenuation ranges overlap. Islands then operates on
the topology of the thresholded mask: if target and nontarget anatomy remain connected through
selected voxels, retaining one connected component may not isolate the lesion.

Grow from Seeds is semiautomatic rather than automatic. Foreground and background seed placement,
anatomical judgment, iterative preview review, and quality control influence its result. In a
slice-thickness experiment, inconsistent seed strategies could become a confounder alongside the
reconstruction condition itself.

## Practical Workflow

### 1. Loading the pilot condition

The 1.25 mm STANDARD reconstruction of `RIDER-1129164940` was loaded in **3D Slicer 5.10.0**.
A new segmentation was created with the target segment named:

```text
Lesion_1p25mm_STANDARD
```

The investigated target was a relatively large pulmonary lesion or mass in the right lung, with
irregular morphology and close contact with surrounding structures. No diagnosis beyond the
public dataset context was inferred.

### 2. Exploratory intensity sampling

Image intensity values were sampled manually at different points before segmentation. Examples
recorded during exploration included:

```text
8, 16, 70, 50
-700, -100, -910
-9, 35, -20
```

These values were used only to explore the lesion, lung, and surrounding tissues. They do not
represent a formal lesion HU distribution, region-of-interest statistic, or quantitative result.

### 3. Threshold exploration

Threshold was tested as an initial semiautomatic strategy. One explored interval was
approximately `-50 HU to +150 HU`; a broader upper bound near `+300 HU` was also inspected
visually.

The preview selected substantial nontarget thoracic soft tissue, including portions of
mediastinal, chest-wall, and other soft-tissue structures. For this lesion and this image, a
simple global HU threshold did not provide adequate lesion-specific isolation. This observation
is data- and target-specific; it is not a universal failure of Threshold.

### 4. Islands exploration

Islands, including **Keep selected island**, was explored to separate the lesion from other
threshold-selected structures. It did not reliably isolate the target because selected lesion
voxels could remain connected to adjacent structures within the chosen intensity range.

This practical observation reinforced that connected-component filtering depends on the
connectivity of the input mask. If unwanted anatomy is connected to the target, retaining the
selected island cannot necessarily separate them.

### 5. Foreground and background seed creation

The workflow changed to **Grow from Seeds**. `Lesion_1p25mm_STANDARD` served as the foreground
class, and a second segment named `Background` was created.

Paint was used to place foreground seeds inside the lesion and background seeds in surrounding
nontarget tissues. Seeds were placed across multiple slices and planes. Axial, coronal, and
sagittal views were used to add spatial information and to identify areas requiring refinement.

### 6. Iterative Grow from Seeds workflow

Grow from Seeds was initialized, with Auto-update enabled during part of the workflow. The
preview was not accepted immediately. It was reviewed across multiple slices, particularly near:

- pleural and chest-wall interfaces;
- mediastinal structures;
- vessels and bronchovascular structures;
- superior and inferior lesion margins;
- boundaries where lesion and adjacent soft tissue had similar attenuation.

Additional foreground or background seeds were added where the preview was inadequate:

```text
seed placement
    → preview
    → visual inspection
    → additional or corrected seeds
    → updated preview
    → multi-planar quality control
```

### 7. Multi-planar visual quality control

The lesion extent was reviewed by scrolling through axial, coronal, and sagittal views. The
qualitative inspection looked for leakage, missing lesion portions, inappropriate inclusion of
neighboring structures, boundary errors, superior or inferior extent problems, and difficulties
at soft-tissue interfaces.

The irregular morphology and contact with surrounding anatomy made the boundary challenging.
No formal quantitative QC metric was calculated.

### 8. Applying and saving the segmentation

After visual review and seed refinement, **Apply** was used to accept the Grow from Seeds preview.
The resulting target remained named `Lesion_1p25mm_STANDARD`.

The save workflow included the MRML scene, source volume, and segmentation. The local filesystem
was checked after the session and confirmed the segmentation file:

```text
RIDER_1129164940_1p25mm_STANDARD_Lesion.seg.nrrd
```

The segmentation artifact remains outside the public repository. No DICOM, MRML scene, source
volume, or `.seg.nrrd` file was added to GitHub.

### Lesson 20 checkpoint

**Work completed:** one interactive semiautomatic segmentation of the 1.25 mm STANDARD condition,
including intensity exploration, Threshold and Islands experiments, Grow from Seeds refinement,
multi-planar visual QC, preview acceptance, and local save.

**Qualitative observations:** simple global thresholding was not sufficiently lesion-specific;
mask connectivity limited Islands; iterative foreground/background seed placement improved the
Grow from Seeds preview; the lesion boundary remained anatomically challenging.

**Methodological decision:** future conditions should use an increasingly standardized seed and
QC protocol so that segmentation-method variation is not silently confounded with slice-thickness
variation.

**Not completed:** segmentation of the 2.5 or 5 mm STANDARD conditions, formal geometry
comparison, quantitative measurement, repeatability assessment, radiomics, or statistical
analysis.

## Quality Checklist

- [x] Public dataset and de-identified research case selected.
- [x] Reconstruction condition identified as 1.25 mm STANDARD.
- [x] STANDARD kernel retained in the working pilot design.
- [x] Target lesion identified in the loaded reconstruction.
- [x] Exploratory HU/intensity sampling performed.
- [x] Threshold tested with more than one visual range.
- [x] Islands and Keep selected island explored.
- [x] Grow from Seeds used.
- [x] Foreground and background segments created.
- [x] Seeds placed and refined across multiple planes and slices.
- [x] Axial, coronal, and sagittal visual QC performed.
- [x] Preview accepted with Apply.
- [x] Segmentation saved locally with a reproducible filename.
- [ ] Segment the 2.5 mm STANDARD reconstruction.
- [ ] Segment the 5 mm STANDARD reconstruction.
- [ ] Verify geometry and correspondence across reconstruction series formally.
- [ ] Measure lesion volume or percentage volume change.
- [ ] Calculate Dice, ASD, Hausdorff Distance, or HD95.
- [ ] Assess intraobserver or interobserver variability.
- [ ] Expand to a larger cohort or perform statistical analysis.
- [ ] Extract radiomics features.

## Lessons Learned

1. The same or overlapping HU values do not imply the same anatomy.
2. A global threshold may have useful intensity sensitivity but insufficient anatomical specificity.
3. Threshold ranges are data- and target-dependent and should not be transferred automatically.
4. Islands depends on connected components in the input mask.
5. Connected nontarget anatomy may prevent Keep selected island from isolating a lesion.
6. Grow from Seeds remains dependent on user-provided foreground and background information.
7. Semiautomatic segmentation still requires anatomical knowledge, review, correction, and QC.
8. A segmentation that appears acceptable in one axial slice can remain incorrect elsewhere.
9. Multi-planar and full-extent review is essential near irregular boundaries and adjacent tissues.
10. Seed placement can introduce segmentation variability into a reconstruction comparison.
11. Optimizing each thickness with undocumented, substantially different manual strategies could confound method variability with slice-thickness variability.
12. Saving with a case-and-condition naming convention improves traceability but does not establish validation.

## Future Learning Directions

- Continue with the same RIDER case and create the corresponding 2.5 mm STANDARD lesion segmentation.
- Standardize lesion identification, foreground seeds, background seeds, preview refinement, multi-planar QC, naming, and data recording before comparing conditions.
- Address the 5 mm STANDARD reconstruction after the 2.5 mm condition.
- Verify Frame of Reference UID, Image Position (Patient), Image Orientation (Patient), Pixel Spacing, slice spacing, reconstruction geometry, and correspondence before interpreting voxel-wise metrics.
- Do not assume that native reconstruction series are voxel-aligned or that registration is unnecessary.
- Keep independent segmentation distinct from mask propagation, registration, or resampling.
- Measure volume, absolute and percentage volume differences, Dice, and potentially ASD and HD95 only after all required segmentations and geometry checks are complete.
- Treat all proposed metrics as future work; no numerical result was produced in this lesson.
- Continue Scientific English through segmentation terminology, documentation and paper reading, GitHub writing, professional communication, and spoken explanation of the methodological choices.
- Do not infer clinical performance, diagnosis, validation, or generalizability from this single-case educational pilot.
