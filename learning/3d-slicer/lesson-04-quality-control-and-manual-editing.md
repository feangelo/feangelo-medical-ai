# Lesson 04 – Quality Control and Manual Editing

**Learning path:** 3D Slicer  
**Date:** 2026-08-07  
**Status:** Learning record  
**Scope:** Scientific learning documentation; no clinical data or patient-specific conclusions

## Objectives

- Understand quality control as a required stage of segmentation rather than a final visual check.
- Identify common mask defects in two-dimensional views and three-dimensional representations.
- Decide when a local manual correction is appropriate and when restarting is safer.
- Apply Paint, Erase, Scissors, Smoothing, and Grow from Seeds intentionally.
- Recognize how editing decisions affect measurements, radiomics, and AI datasets.
- Develop a standardized pre-export review process suitable for research workflows.

## Scientific Background

### Why quality control matters

A segmentation mask is an interpretation of image information. Even when it is produced by an automatic or semi-automatic method, it can contain leakage into adjacent anatomy, missing regions, holes, disconnected islands, implausible boundaries, or geometry errors. A visually convincing three-dimensional surface can hide defects that remain evident in axial, coronal, or sagittal slices.

Quality control should therefore evaluate the mask against a defined objective. A mask prepared for visualization may have different acceptance criteria from one intended for volume measurement, radiomics, model training, surgical planning research, or mesh generation. Passing one use case does not automatically make a mask suitable for another.

### Interobserver variability

Different observers may interpret the same boundary differently because of image noise, partial-volume effects, pathology, anatomical ambiguity, display settings, experience, or differences in the written protocol. The same observer may also produce different results at different times.

This variability should be managed rather than ignored. Useful controls include a written segmentation protocol, standardized display settings, anatomical inclusion and exclusion rules, reviewer training, blinded repeat review when appropriate, and documented agreement metrics. Consensus review can resolve disagreements, but the method used to reach consensus must also be reported.

### When to correct a mask

Local manual correction is appropriate when the intended segmentation remains fundamentally valid and the defect is limited, explainable, and reviewable. Examples include a small region of leakage, an isolated missing boundary, a disconnected artifact, or a contour that needs a targeted adjustment because the automated method did not follow the defined anatomical rule.

Every correction should have a reason. Editing only to make a surface look smoother can introduce bias or remove relevant detail. When quantitative outputs matter, the effect of the correction should be considered and, when feasible, compared with the preceding version.

### When to restart a segmentation

Restarting is often safer when errors are systematic or when the provenance of the mask can no longer be reconstructed. Warning signs include:

- incorrect source volume, orientation, or segmentation geometry;
- inappropriate threshold or initialization affecting most slices;
- widespread leakage or omission;
- incorrect anatomical inclusion rules;
- extensive edits that make the original workflow impossible to reproduce;
- operations applied to the wrong segment;
- a mask created under a protocol that does not match the intended analysis.

Continuing to patch a fundamentally incorrect mask can take longer than restarting and may conceal methodological problems. The decision should consider scope, reproducibility, intended use, and the ability to explain the complete workflow.

### Impact on artificial intelligence

Segmentation masks used as labels influence what an AI model learns. Inconsistent boundaries, missing structures, systematic leakage, and differing observer conventions can become label noise or encode unwanted biases. A model may reproduce annotation habits rather than the intended anatomy.

AI dataset quality therefore requires more than a final visual inspection. It benefits from annotation guidelines, reviewer roles, versioned labels, disagreement management, representative quality sampling, and documented acceptance criteria. Train, validation, and test labels should follow compatible rules, while test-set review should avoid introducing information leakage into model development.

### Impact on radiomics

Radiomics features depend on both the image and the region of interest. Boundary changes can affect shape, volume, intensity distributions, and texture features. Small editing differences may have a larger effect on small lesions, irregular structures, or features sensitive to discretization and resampling.

The segmentation method, observer process, correction rules, software version, and post-processing steps should be documented. Reproducibility studies may evaluate feature stability across observers, repeated segmentations, perturbations, or alternative processing settings. Manual refinement does not guarantee more stable or clinically meaningful features.

### Importance of standardization

Standardization reduces avoidable variation and makes decisions easier to audit. A practical standard should define:

- the source series and required image checks;
- anatomical boundaries and inclusion/exclusion rules;
- software version and segmentation geometry;
- permitted tools and parameter ranges;
- review planes and display conventions;
- correction, restart, and escalation criteria;
- reviewer responsibilities;
- naming, versioning, and export requirements;
- acceptance criteria for the intended use.

A protocol should be specific enough to guide consistent work while still documenting justified deviations. Standardization supports reproducibility; it does not replace anatomical expertise or validation.

## Practical Workflow

### 1. Confirm the review context

Before editing, confirm the correct source image, orientation, spacing, segment, visibility settings, and intended output. Review the mask in axial, coronal, and sagittal planes. Use the 3D view to detect global shape or topology problems, but do not rely on it alone.

### 2. Paint

Use **Paint** for controlled addition of missing voxels when the target boundary can be identified locally. It is useful for small omissions, slice-specific corrections, and deliberate boundary completion.

Review brush diameter, slice orientation, interpolation behavior, and whether editing is limited to the active slice. Avoid long sequences of undocumented freehand painting when a reproducible semi-automatic method would be more appropriate.

### 3. Erase

Use **Erase** to remove localized leakage, artifacts, or regions that violate the anatomical protocol. Verify the correction in adjacent slices and orthogonal planes because a region that appears isolated in one view may be connected in another.

Large amounts of erasing may indicate that initialization or segmentation geometry is incorrect. In that situation, reassess whether restarting would be more reliable.

### 4. Scissors

Use **Scissors** when a clearly defined region must be removed or retained efficiently. The tool is useful for separating unwanted anatomy, trimming a segment with a controlled contour, or applying a cut across a selected projection.

The selected operation, view, and slice behavior matter. A cut based on a 3D projection can affect more anatomy than expected, so the result must be inspected throughout the volume.

### 5. Smoothing

Use **Smoothing** only after identifying the type of irregularity and the intended downstream use. Select the method and parameter relative to voxel spacing and anatomical scale.

Compare before and after results. Confirm that smoothing did not close valid openings, remove thin structures, merge nearby regions, or materially change quantitative outputs. Preserve enough information to reproduce the unsmoothed result when the workflow requires it.

### 6. Grow from Seeds

Use **Grow from Seeds** when multiple regions can be represented by carefully placed foreground and background seeds and their image characteristics support competitive region growing. Seeds should cover representative areas without crossing uncertain boundaries.

After previewing the result, refine seeds rather than accepting a poor boundary and relying entirely on manual cleanup. Check all relevant segments because changing one seed region can affect neighboring regions. Record the initialization logic and any subsequent manual corrections.

### 7. Perform a final independent review

After editing, hide and reveal segments, inspect boundaries in all planes, review the 3D representation, and compare the mask with the source image. When the intended use or protocol requires it, obtain a second review and document disagreements and resolutions.

## Quality Checklist

Complete this checklist before export:

- [ ] The approved segmentation protocol was followed.
- [ ] The correct source image, orientation, spacing, and segmentation geometry were confirmed.
- [ ] The intended anatomy is included according to the defined boundary rules.
- [ ] No unintended structures or obvious leakage remain.
- [ ] No unexplained holes remain inside the target mask.
- [ ] No unexplained disconnected islands remain.
- [ ] Boundaries were reviewed in axial, coronal, and sagittal planes.
- [ ] The 3D representation was reviewed for global shape and topology problems.
- [ ] Thin structures and clinically or scientifically relevant details were not removed inadvertently.
- [ ] Volume and other measurements are plausible for the image and defined use case.
- [ ] Manual corrections, tool parameters, and justified deviations were documented.
- [ ] Smoothing or margin operations were assessed for quantitative impact.
- [ ] The mask meets the predefined acceptance criteria for research use.
- [ ] Privacy, provenance, naming, versioning, and export requirements were checked.
- [ ] The mask is ready for the intended research workflow; no clinical-use claim is implied.

## Lessons Learned

- Quality control begins with a defined protocol and intended use, not with visual preference.
- Manual editing is a technical decision that should be limited, justified, and documented.
- A plausible 3D surface can conceal slice-level errors.
- Repeated local corrections may indicate that the segmentation should be restarted.
- Observer variability can propagate into measurements, radiomics features, and AI labels.
- Standardized tools and parameters improve consistency but do not eliminate anatomical ambiguity.
- Paint, Erase, and Scissors are best used for targeted problems rather than rescuing a fundamentally incorrect mask.
- Grow from Seeds is most useful when seed placement represents the relevant regions well and the preview is reviewed iteratively.
- Smoothing can improve regularity while simultaneously changing scientific measurements.
- A research-ready mask requires documented acceptance criteria, provenance, and review evidence.

## Future Learning Directions

- Document quality control before export so review remains part of the default workflow.
- Use synthetic or appropriately licensed examples containing leakage, holes, islands, missing boundaries, and geometry errors.
- Document the same defect in 2D and 3D to show why both views are necessary.
- Include a decision exercise comparing targeted correction with a complete restart.
- Document Paint, Erase, and Scissors with explicit examples of appropriate and inappropriate use.
- Show how seed placement changes Grow from Seeds results and neighboring segments.
- Compare volume and surface changes before and after Smoothing.
- Add an interobserver exercise with a short written protocol and a structured disagreement review.
- Connect segmentation variability to future learning topics on radiomics robustness and AI label quality.
- Provide a version-controlled, non-clinical quality checklist and a segmentation-review form.
- Record the exact 3D Slicer version and verified references when producing the scientific learning documentation.
- Keep all documented examples free of private clinical data and clearly separate learning workflows from clinical validation.
