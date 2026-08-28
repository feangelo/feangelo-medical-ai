# Learning Lab

<p class="page-intro">Structured technical notes documenting progression through medical image analysis. Each record distinguishes concepts studied, practical observations, limitations, and future work. These lessons document learning—not expertise, research validation, or clinical competence.</p>

## Learning path

<div class="learning-path" role="list">
  <div class="learning-stage" role="listitem"><span>01</span><div><strong>Foundations</strong><p>3D Slicer interface, anatomical planes, voxels, and segmentation concepts.</p></div></div>
  <div class="learning-stage" role="listitem"><span>02</span><div><strong>3D segmentation</strong><p>Thresholding, region methods, manual editing, quality control, and metrics.</p></div></div>
  <div class="learning-stage" role="listitem"><span>03</span><div><strong>Scientific reproducibility</strong><p>Observer variability, protocol standardization, and preprocessing decisions.</p></div></div>
  <div class="learning-stage" role="listitem"><span>04</span><div><strong>Spatial analysis</strong><p>DICOM geometry, registration, resampling, interpolation, and validation.</p></div></div>
  <div class="learning-stage learning-stage--future" role="listitem"><span>05</span><div><strong>Quantitative imaging and Medical AI</strong><p>Future implementation after the required image-analysis foundations are established.</p></div></div>
</div>

## 3D Slicer and medical image analysis

The lesson files remain canonical in the repository's `learning/3d-slicer/` directory and are rendered directly into the public site during the documentation build. This avoids maintaining duplicate copies while giving each learning record a stable, crawlable page.

| Record | Topic |
|---|---|
| [Lesson 01](lessons/lesson-01-introduction-to-3d-slicer.md) | Introduction to 3D Slicer |
| [Lesson 02](lessons/lesson-02-first-lung-segmentation.md) | First lung segmentation |
| [Lesson 03](lessons/lesson-03-segmentation-pipeline.md) | Segmentation pipeline |
| [Lesson 04](lessons/lesson-04-quality-control-and-manual-editing.md) | Quality control and manual editing |
| [Lesson 05](lessons/lesson-05-segmentation-validation-and-quality-metrics.md) | Segmentation validation and quality metrics |
| [Lesson 06](lessons/lesson-06-observer-variability-and-scientific-reproducibility.md) | Observer variability and reproducibility |
| [Lesson 07](lessons/lesson-07-image-acquisition-and-protocol-standardization.md) | Image acquisition and protocol standardization |
| [Lesson 08](lessons/lesson-08-image-preprocessing-and-harmonization.md) | Image preprocessing and harmonization |
| [Lesson 09](lessons/lesson-09-dicom-metadata-geometry-and-data-quality-control.md) | DICOM metadata, geometry, and data quality control |
| [Lesson 10](lessons/lesson-10-image-registration-and-spatial-validation.md) | Image registration and spatial validation |
| [Lesson 11](lessons/lesson-11-image-geometry-resampling-and-interpolation.md) | Image geometry, resampling, and interpolation |
| [Lesson 12](lessons/lesson-12-quantitative-imaging-measurement-variability-and-reliability.md) | Quantitative imaging, measurement variability, and reliability |
| [Lesson 13](lessons/lesson-13-measurement-reliability-percentage-change-and-agreement.md) | Measurement reliability, percentage change, and agreement |
| [Lesson 14](lessons/lesson-14-magnitude-dependent-agreement-proportional-bias-and-heteroscedasticity.md) | Magnitude-dependent agreement, proportional bias, and heteroscedasticity |
| [Lesson 15](lessons/lesson-15-study-design-data-provenance-and-quantitative-segmentation-planning.md) | Study design, data provenance, and quantitative segmentation planning |
| [Lesson 16](lessons/lesson-16-dataset-requirements-segmentation-metrics-and-practical-study-protocol.md) | Dataset requirements, segmentation metrics, and practical study protocol |
| [Lesson 17](lessons/lesson-17-practical-dataset-audit-tcia-rider-lung-ct-dicom-reconstruction-parameters-and-ct-seg-mapping.md) | Practical RIDER-LUNG-CT dataset audit, DICOM reconstruction metadata, and CT–SEG mapping |

## Documentation standard

A learning record is committed only after its terminology, scope, limitations, and unsupported claims have been reviewed. “Learning record” does not mean peer-reviewed evidence, validated competence, or clinical readiness.

[View the complete learning source](https://github.com/feangelo/feangelo-medical-ai/tree/main/learning){ .portfolio-button .portfolio-button--small target="_blank" rel="noopener" }
