# Learning

This area documents a progressive learning journey. Lessons record what was studied, the questions considered, practical observations, limitations, and next steps. They are learning records, not claims of expertise, research authority, or clinical competence.

Concepts are added incrementally and should reflect the order in which they were learned. Every entry should record its objective, source, date when known, practice performed, unresolved questions, and next steps. Only public or synthetic data may be used.

Content should be committed only after it has been checked for consistency with the corresponding lesson or exercise and reviewed for unsupported claims. In this context, “checked” does not mean peer-reviewed scientific validation, clinical validation, or demonstrated professional proficiency. Those statuses require separate evidence and must be stated explicitly if they are ever reached.

## Learning paths

### 3D Slicer

- [Lesson 01 — Introduction to 3D Slicer](3d-slicer/lesson-01-introduction-to-3d-slicer.md)
- [Lesson 02 — First Lung Segmentation](3d-slicer/lesson-02-first-lung-segmentation.md)
- [Lesson 03 — Segmentation Pipeline](3d-slicer/lesson-03-segmentation-pipeline.md)
- [Lesson 04 — Quality Control and Manual Editing](3d-slicer/lesson-04-quality-control-and-manual-editing.md)
- [Lesson 05 — Segmentation Validation and Quality Metrics](3d-slicer/lesson-05-segmentation-validation-and-quality-metrics.md)
- [Lesson 06 — Observer Variability and Scientific Reproducibility](3d-slicer/lesson-06-observer-variability-and-scientific-reproducibility.md)
- [Lesson 07 — Image Acquisition and Protocol Standardization](3d-slicer/lesson-07-image-acquisition-and-protocol-standardization.md)
- [Lesson 08 — Image Preprocessing and Harmonization](3d-slicer/lesson-08-image-preprocessing-and-harmonization.md)
- [Lesson 09 — DICOM Metadata, Geometry, and Data Quality Control](3d-slicer/lesson-09-dicom-metadata-geometry-and-data-quality-control.md)
- [Lesson 10 — Image Registration and Spatial Validation](3d-slicer/lesson-10-image-registration-and-spatial-validation.md)
- [Lesson 11 — Medical Image Geometry, Resampling and Interpolation](3d-slicer/lesson-11-image-geometry-resampling-and-interpolation.md)
- [Lesson 12 — Quantitative Imaging, Measurement Variability and Reliability](3d-slicer/lesson-12-quantitative-imaging-measurement-variability-and-reliability.md)
- [Lesson 13 — Measurement Reliability, Percentage Change and Agreement](3d-slicer/lesson-13-measurement-reliability-percentage-change-and-agreement.md)
- [Lesson 14 — Magnitude-Dependent Agreement, Proportional Bias and Heteroscedasticity](3d-slicer/lesson-14-magnitude-dependent-agreement-proportional-bias-and-heteroscedasticity.md)
- [Lesson 15 — Study Design, Data Provenance and Quantitative Segmentation Planning](3d-slicer/lesson-15-study-design-data-provenance-and-quantitative-segmentation-planning.md)
- [Lesson 16 — Dataset Requirements, Segmentation Metrics and Practical Study Protocol](3d-slicer/lesson-16-dataset-requirements-segmentation-metrics-and-practical-study-protocol.md)
- [Lesson template](3d-slicer/TEMPLATE.md)

Create a future lesson with a non-destructive preview first:

```bash
python scripts/create_lesson.py --number 15 --title "Lesson title" --dry-run
```
