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
- [Lesson template](3d-slicer/TEMPLATE.md)

Create a future lesson with a non-destructive preview first:

```bash
python scripts/create_lesson.py --number 10 --title "Lesson title" --dry-run
```
