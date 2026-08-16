# Research Notes

<p class="page-intro">Concise principles and durable references emerging from the technical learning journey. These notes frame questions for future implementation; they are not published research findings.</p>

## Scientific engineering principles

### Geometry before metrics

Array dimensions do not establish physical correspondence. Spacing, origin, direction, orientation, and coordinate convention must be understood before comparing images, masks, measurements, or model outputs.

### Plausibility is not Ground Truth

A visually convincing segmentation, registration, reconstruction, or AI-enhanced image is not automatically anatomically correct. The reference standard and validation strategy must match the intended task.

### Computation and scientific validity are different checks

Software can complete every processing step while preserving an incorrect assumption introduced earlier. Validation must examine the scientific question, source data, geometry, transformation, measurement, and downstream interpretation.

### Acquisition, reconstruction, and resampling are not equivalent

Resampling can standardize a grid but cannot create information that was not acquired. Reconstruction and interpolation choices may change representation and require task-specific evaluation.

## Durable documentation

The repository wiki is reserved for references that outgrow a single lesson. New notes must distinguish established sources, practical observations, hypotheses, and unresolved questions.

[Open the technical wiki](wiki/index.md){ .portfolio-button .portfolio-button--small }
