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

- Use Segment Editor to create the first guided lung segmentation.

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
