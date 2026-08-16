# Learning Log

This log records progress without treating study activity as proof of validated competence.

## Entry template

### YYYY-MM-DD — Topic

**What I learned**

- Add concise, verifiable notes.

**Difficulties**

- Record unresolved questions, limitations, or misconceptions corrected.

**Evidence or practice**

- Link to a public exercise, note, test, or case when available.

**Next steps**

- Define the next small, measurable action.

---

### Date not recorded — Introduction to 3D Slicer

**What I learned**

- Identified the main 3D Slicer interface areas and navigated axial, coronal, and sagittal views.
- Connected anatomical orientation labels with patient directions and learned the basic concepts of voxels and segmentation.

**Difficulties**

- Maintaining anatomical orientation while moving between different layouts and planes.
- Distinguishing image navigation, segmentation masks, and three-dimensional representations.

**Evidence or practice**

- [Lesson 01 — Introduction to 3D Slicer](learning/3d-slicer/lesson-01-introduction-to-3d-slicer.md)

**Next steps**

- Use Segment Editor to document the first lung-segmentation exercise.

### Date not recorded — First lung segmentation

**What I learned**

- Used Segment Editor, Threshold, Paint, and Grow from Seeds to organize the right lung, left lung, body, and trachea as separate segments.
- Distinguished Preview, Auto Update, and Apply and observed volume, voxel count, and mean HU in Segment Statistics.

**Difficulties**

- Placing representative seeds while maintaining separation between neighboring regions.
- Interpreting quantitative outputs without treating them as independent proof of segmentation quality.

**Evidence or practice**

- [Lesson 02 — First Lung Segmentation](learning/3d-slicer/lesson-02-first-lung-segmentation.md)

**Next steps**

- Organize Threshold and post-processing tools into a standardized, reproducible segmentation pipeline.

### 2026-08-06 — 3D Slicer segmentation pipeline

**What I learned**

- Structured the relationship between Threshold, Islands, Logical Operators, Margin, and Smoothing as a reviewable segmentation pipeline.
- Examined how operation order and parameters can affect geometry and quantitative outputs.

**Difficulties**

- Defining when geometric cleanup improves usability without removing relevant anatomical detail.
- Separating visually plausible output from evidence of quantitative or clinical validity.

**Evidence or practice**

- [Lesson 03 — Segmentation Pipeline](learning/3d-slicer/lesson-03-segmentation-pipeline.md)

**Next steps**

- Repeat the workflow with approved synthetic or open data and record exact software versions, parameters, and quality-control observations.

### 2026-08-07 — Quality control and manual editing in 3D Slicer

**What I learned**

- Structured quality control as a protocol-driven review across slice views and the 3D representation.
- Examined when Paint, Erase, Scissors, Smoothing, and Grow from Seeds are appropriate for correction or refinement.
- Connected observer variability and mask editing decisions to AI label quality and radiomics reproducibility.

**Difficulties**

- Distinguishing a limited, defensible correction from a segmentation that should be restarted.
- Balancing geometric regularity with preservation of relevant anatomical detail and quantitative stability.

**Evidence or practice**

- [Lesson 04 — Quality Control and Manual Editing](learning/3d-slicer/lesson-04-quality-control-and-manual-editing.md)

**Next steps**

- Apply the checklist to an approved synthetic or open-data exercise and record the exact 3D Slicer version, parameters, corrections, and review findings.

### 2026-08-09 — Segmentation validation and quality metrics

**What I learned**

- Distinguished overlap and boundary metrics from anatomical, visual, and clinical validation.
- Examined Ground Truth as the best available reviewed reference rather than an absolute truth.
- Connected acquisition protocols, scanners, reconstruction, segmentation methods, and preprocessing with reproducibility.
- Considered how SOPs and protocol adherence influence the interpretation of multicenter AI performance.

**Difficulties**

- Interpreting a high overlap score without overlooking small but important anatomical errors.
- Separating model limitations from acquisition, protocol, population, and operator differences between centers.

**Evidence or practice**

- [Lesson 05 — Segmentation Validation and Quality Metrics](learning/3d-slicer/lesson-05-segmentation-validation-and-quality-metrics.md)

**Next steps**

- Use approved synthetic masks to compare Dice, IoU, and boundary differences while documenting geometry, protocol, visual findings, and limitations.

### 2026-08-09 — Observer variability and scientific reproducibility

**What I learned**

- Distinguished intraobserver variability from interobserver variability in medical image segmentation.
- Examined how human factors, anatomical ambiguity, acquisition conditions, and protocol adherence influence annotations.
- Understood expert consensus as a documented process for creating a more robust reference rather than absolute truth.
- Connected SOPs, training, parameter recording, and protocol consistency with scientific reproducibility.

**Difficulties**

- Distinguishing acceptable expert variation from avoidable protocol-related inconsistency.
- Interpreting disagreement according to anatomy and application rather than assuming that one mask must be incorrect.

**Evidence or practice**

- [Lesson 06 — Observer Variability and Scientific Reproducibility](learning/3d-slicer/lesson-06-observer-variability-and-scientific-reproducibility.md)

**Next steps**

- Study introductory agreement and reliability methods before applying ICC, Cohen's Kappa, Bland–Altman, or reader-study designs.

### 2026-08-11 — Image acquisition and protocol standardization

**What I learned**

- Identified introductory CT acquisition and reconstruction parameters that may influence quantitative image analysis.
- Connected protocol standardization and acquisition documentation with reproducibility across institutions.
- Examined how image quality and acquisition conditions indirectly affect segmentation and Ground Truth quality.
- Applied practical CT experience to the interpretation of possible artifacts without treating a visual finding as confirmed pathology.

**Difficulties**

- Separating acquisition, reconstruction, preprocessing, segmentation, and model-related sources of variability.
- Interpreting multicenter differences without assuming that similarly named protocols produce equivalent images.

**Evidence or practice**

- [Lesson 07 — Image Acquisition and Protocol Standardization](learning/3d-slicer/lesson-07-image-acquisition-and-protocol-standardization.md)

**Next steps**

- Review approved, non-identifiable acquisition metadata examples before studying harmonization, normalization, or multicenter AI methods.

### 2026-08-12 — Image preprocessing and harmonization

**What I learned**

- Distinguished spatial standardization through resampling from equivalence of original image information.
- Connected partial-volume effects, feature robustness, confounding, and shortcut learning with multicenter technical variability.
- Distinguished normalization from harmonization and considered the need to preserve biological information while reducing unwanted technical variation.
- Examined overcorrection risk and the importance of retaining patient, disease, center, scanner, acquisition, reconstruction, and Ground Truth metadata.
- Connected professional CT-guided biopsy experience with spatial consistency and lesion-conspicuity considerations without treating the observation as formal evidence.

**Difficulties**

- Separating technical center effects from genuine biological or population differences when they are confounded.
- Selecting preprocessing decisions according to the scientific question without assuming that standardized grids are equivalent.

**Evidence or practice**

- [Lesson 08 — Image Preprocessing and Harmonization](learning/3d-slicer/lesson-08-image-preprocessing-and-harmonization.md)

**Next steps**

- Study approved metadata examples, interpolation principles, and feature-stability methods before applying harmonization or multicenter AI workflows.

### 2026-08-13 — DICOM metadata, geometry, and imaging quality control

**What I learned**

- Understood DICOM as pixel data combined with metadata, hierarchy, geometry, and contextual information.
- Distinguished Series Description from image-based verification and Slice Thickness from inter-slice spacing.
- Connected voxel geometry, spatial continuity, interpolation, motion, task-specific quality, and registration with pre-segmentation QC.
- Introduced false positives, false negatives, sensitivity, specificity, decision thresholds, confidence scores, and human review conceptually.
- Examined de-identification, pseudonymization, re-identification risk, and longitudinal linkage at a high level.

**Difficulties**

- Distinguishing incomplete-series warning signals from evidence about the underlying cause.
- Integrating metadata, spatial geometry, actual image content, privacy, and task-specific quality into one traceable QC decision.

**Evidence or practice**

- [Lesson 09 — DICOM Metadata, Geometry, and Data Quality Control](learning/3d-slicer/lesson-09-dicom-metadata-geometry-and-data-quality-control.md)

**Next steps**

- Study approved, non-identifiable DICOM metadata examples before implementing pydicom extraction, geometry checks, registration, or automated QC.

### 2026-08-14 — Image registration and spatial validation

**What I learned**

- Distinguished rigid, affine, and deformable registration conceptually and connected transformation flexibility with validation responsibility.
- Connected anatomical landmarks, TRE, Dice, Hausdorff Distance, and HD95 with complementary global, local, overlap, and distance-based evaluation.
- Examined why biologically meaningful longitudinal change should not be removed by an inappropriate transformation.
- Introduced similarity metrics, optimization, regularization, external-center validation, domain shift, fine-tuning, and domain adaptation conceptually.
- Developed root-cause reasoning for cross-center AI performance degradation without claiming implementation or experimental validation.

**Difficulties**

- Separating technical spatial differences from biological anatomical changes when defining a registration objective.
- Interpreting strong global metrics when a small but scientifically important target may remain locally misaligned.

**Evidence or practice**

- [Lesson 10 — Image Registration and Spatial Validation](learning/3d-slicer/lesson-10-image-registration-and-spatial-validation.md)

**Next steps**

- Perform future registration exercises in 3D Slicer before claiming practical proficiency, then study task-specific landmark and distance-based validation.

### 2026-08-15 — Medical image geometry, resampling, and interpolation

**What I learned**

- Distinguished voxel index, matrix size, and physical position through spacing, origin, and direction.
- Connected RAS/LPS conventions, isotropic and anisotropic voxels, and physical-space consistency with image-mask alignment.
- Distinguished acquisition, reconstruction, resampling, linear interpolation, and nearest-neighbor interpolation conceptually.
- Examined partial-volume effects, small-structure representation, error propagation, and the limits of computational success.
- Connected geometry and resampling decisions with future multicenter radiomics and Medical AI validation.

**Difficulties**

- Separating a denser resampled grid from genuinely finer information acquired or reconstructed from source measurements.
- Distinguishing visually plausible enhancement from anatomical information supported by acquired data.

**Evidence or practice**

- [Lesson 11 — Medical Image Geometry, Resampling and Interpolation](learning/3d-slicer/lesson-11-image-geometry-resampling-and-interpolation.md)

**Next steps**

- Perform controlled resampling exercises in 3D Slicer and Python before claiming implementation proficiency, then quantify geometry and measurement changes.

### 2026-08-16 — Quantitative imaging, measurement variability, and reliability

**What I learned**

- Understood why equal quantitative imaging values do not establish biological equivalence.
- Distinguished repeatability, reproducibility, relative consistency, and absolute agreement conceptually.
- Connected multicenter confounding, center effects, test-retest design, and feature robustness with cautious interpretation.
- Introduced ICC as a family of reliability coefficients without studying model selection or formulas.
- Related observed change to expected measurement variability and introduced the Coefficient of Variation.

**Difficulties**

- Separating possible biological change from technical and measurement variability.
- Interpreting preserved ranking when absolute measurements are not interchangeable across scanners.

**Evidence or practice**

- [Lesson 12 — Quantitative Imaging, Measurement Variability and Reliability](learning/3d-slicer/lesson-12-quantitative-imaging-measurement-variability-and-reliability.md)

**Next steps**

- Reinforce reliability concepts through controlled examples before implementing test-retest, ICC, or radiomics robustness analyses.
