# Lesson 09 – DICOM Metadata, Image Geometry, and Medical Imaging Data Quality Control

**Learning path:** 3D Slicer  
**Date:** 2026-08-13  
**Status:** Learning record  
**Scope:** Scientific learning documentation; no clinical data or patient-specific conclusions

## Objectives

- Understand that DICOM contains image data, metadata, and spatial and contextual information.
- Introduce DICOM tags and the Patient, Study, Series, and Instance hierarchy conceptually.
- Explain why correct series selection is essential and why Series Description alone may be insufficient.
- Connect acquisition metadata with actual image content and image-based quality control.
- Introduce confidence scores and human-in-the-loop review conceptually.
- Recognize warning signs for incomplete series, spatial gaps, and inconsistent geometry.
- Introduce Image Position (Patient), Image Orientation (Patient), Pixel Spacing, and voxel geometry.
- Distinguish Slice Thickness from inter-slice spacing and isotropic from anisotropic voxels.
- Understand implications for multiplanar reconstruction, segmentation, 3D analysis, interpolation, and smoothing.
- Introduce motion-artifact quality control, false positives, false negatives, sensitivity, specificity, and decision thresholds.
- Understand that image quality is task-specific.
- Introduce image registration and longitudinal image comparison.
- Explain why slice number alone does not establish anatomical correspondence.
- Introduce DICOM de-identification, anonymization, pseudonymization, and re-identification risk at a high level.
- Develop a conceptual pre-segmentation QC pipeline for multicenter imaging datasets.
- Continue scientific English development without claiming language proficiency.

## Scientific Background

### DICOM is more than a pixel matrix

A medical image should not be treated merely as a matrix of pixels. Conceptually:

```text
DICOM = image or pixel data + metadata + spatial and contextual information
```

Depending on the DICOM object and modality, metadata may describe modality, manufacturer, scanner model, acquisition and reconstruction parameters, slice thickness, pixel spacing, kVp, exposure-related information, reconstruction kernel, protocol and contrast information, study and series organization, image position and orientation, identifiers, dates, times, and other attributes.

Not every field is always present, complete, consistent, or reliable. Metadata should be checked against the research task, other related attributes, and the actual image content.

### DICOM tags

A DICOM tag identifies an attribute, and that attribute may have a value. Conceptually:

```text
Tag → attribute → value
```

Examples include:

| Tag | Attribute |
|---|---|
| `(0010,0010)` | Patient's Name |
| `(0008,0060)` | Modality |
| `(0008,0070)` | Manufacturer |
| `(0008,103E)` | Series Description |
| `(0018,0050)` | Slice Thickness |
| `(0018,0060)` | KVP |
| `(0028,0030)` | Pixel Spacing |

Memorizing tag numbers is not required at this stage. Future Python workflows may read attributes programmatically. The following snippet is illustrative only; it was not implemented or validated during this lesson:

```python
import pydicom

ds = pydicom.dcmread("image.dcm")

print(ds.Manufacturer)
print(ds.SliceThickness)
print(ds.PixelSpacing)
```

Python implementation and safe handling of missing or variant attributes will be learned progressively in future lessons.

### Patient, Study, Series, and Instance hierarchy

Conceptually, DICOM information may be organized as:

```text
Patient
  ↓
Study
  ↓
Series
  ↓
Instances
```

A Study Instance UID identifies a study, a Series Instance UID identifies a series within a study, and a SOP Instance UID identifies an individual DICOM object. UID implementation is not covered in depth here.

Correct grouping matters when thousands of files are processed. Filenames and folder locations alone do not reliably define the DICOM hierarchy.

### Series selection

An abdominal CT study may contain a scout or localizer, non-contrast, arterial, portal venous, delayed, axial thin and thick reconstructions, coronal and sagittal reconstructions, MIP images, and other derived series.

If the research objective is portal venous phase liver analysis, the intended series should be selected consistently. Possible Series Description values might include `VENOSA`, `PORTAL`, `ABD VEN`, `FASE 2`, `ABD 70 SEC`, or `SERIE 5`.

Series Description is useful, but it should not automatically be treated as Ground Truth for contrast phase. Local naming conventions, manual entry, language, and protocol execution can vary.

### Metadata and image content

> Metadata tells us about acquisition. Image content tells us about the resulting image.

Protocol labels and timing describe intended acquisition conditions. Actual enhancement and image appearance may also be influenced by cardiac function and circulation, contrast timing and administration, body size, venous access, motion, breathing, collateral circulation, protocol execution, and overall image quality. These factors were discussed as possibilities, not deterministic explanations.

The learner's professional reasoning was that a series labeled portal or venous may still require image-based verification when the research question depends on actual enhancement. This is a learning reflection, not a validated classification method.

### Contrast-phase classification as a future concept

A conceptual future system could combine:

```text
DICOM metadata
        +
image characteristics
        ↓
contrast-phase classification
        ↓
confidence score
        ↓
high confidence → automated processing
low confidence  → human review
```

Hypothetical outputs might be `Portal venous: 96%` or `Uncertain: 58% → human review`. These percentages are examples only. No classifier was developed, tested, or validated during this lesson.

A confidence score expresses a system's assigned confidence under its design; it is not automatically a calibrated probability. Calibration remains a future learning topic. Human-in-the-loop review introduces qualified human assessment when automated confidence or QC criteria indicate uncertainty.

### Incomplete series and spatial continuity

Consider Series A with 320 images and Series B with 187 images, both with similar Series Description and Slice Thickness. Image count alone is a warning signal, not proof that Series B is incomplete.

The learner proposed reviewing expected anatomical coverage, beginning and end of the study region, apparent image count, reconstruction completeness, transfer problems, and possible acquisition or reconstruction coverage problems. Detecting a possible incomplete series is different from determining its cause.

Spatial continuity can be examined through physical positions. A simplified regular sequence might be:

```text
z = -200 mm
z = -199 mm
z = -198 mm
```

An unexpected spatial jump may indicate a gap or another geometry issue requiring investigation. Physical position can reveal information that filenames or instance numbers may not reliably provide.

### Image Position and Image Orientation

Image Position (Patient) and Image Orientation (Patient) help describe physical location and orientation in patient coordinates. They support reconstruction of spatial relationships between images.

> File order is not anatomical geometry.

Coordinate transformations are not taught mathematically here. LPS and RAS coordinate systems remain future learning topics.

### Slice Thickness and inter-slice spacing

Consider this simplified example:

```text
Slice Thickness = 1 mm

Image centers:
Z = 0 mm
Z = 2 mm
Z = 4 mm
Z = 6 mm
```

Slice Thickness and the distance between image positions are related concepts, but they are not automatically equivalent. Blindly using Slice Thickness as the complete description of through-plane geometry can be misleading.

> Slice thickness and spacing between slices are not always the same.

Actual geometry should be derived appropriately from the relevant DICOM spatial information.

### Pixel Spacing and voxel geometry

Pixel Spacing describes physical sampling within the image plane. Consider two conceptual examples:

```text
Series A:
Pixel Spacing = 0.7 × 0.7 mm
Slice Thickness = 1 mm
Conceptual dimensions: 0.7 × 0.7 × 1 mm

Series B:
Pixel Spacing = 0.7 × 0.7 mm
Slice Thickness = 5 mm
Conceptual dimensions: 0.7 × 0.7 × 5 mm
```

These examples illustrate the concept only. Actual volume geometry should be derived from appropriate DICOM spatial attributes and should not be inferred blindly from one tag.

### Isotropic and anisotropic voxels

Conceptually:

```text
0.6 × 0.6 × 0.6 mm → isotropic
0.6 × 0.6 × 5 mm   → anisotropic
```

Isotropic sampling has similar dimensions along each axis. Anisotropic sampling has substantially different dimensions along one or more axes. Anisotropic data may look excellent in the original acquisition plane while having lower through-plane resolution.

Voxel geometry can affect multiplanar reconstruction, coronal and sagittal appearance, visibility of small structures, segmentation, 3D models, centerlines, and quantitative measurement. The practical importance depends on the anatomy and intended task.

### Interpolation, smoothing, and 3D models

Lesson 08 introduced the principle that interpolation can estimate intermediate values but cannot recover anatomical information that was not originally preserved. A visually smooth reconstruction is not proof of recovered anatomical resolution.

The conceptual chain is:

```text
acquisition
    ↓
voxel geometry
    ↓
interpolation
    ↓
segmentation
    ↓
smoothing
    ↓
3D model
    ↓
measurement
```

A visually smooth 3D model does not prove that the underlying anatomy was acquired at equivalent resolution. Smoothing may improve appearance without restoring missing anatomical information.

### Motion-artifact quality control

As an anonymized professional learning reflection, the learner described recognizing possible motion or breathing artifacts through discontinuities between neighboring images, apparent vibration, altered anatomical continuity, degraded airway appearance, and differences that became particularly visible under certain reconstruction or display conditions. Experience sometimes supported an approximate impression of where motion began within a series.

This observation is not scientific evidence, a diagnostic conclusion, an implemented detector, or a medical recommendation. The physical mechanism should not be inferred from appearance alone.

Future computational approaches could investigate inter-slice similarity, edges, gradients, spatial continuity, registration consistency, and other image features. No motion-detection algorithm was implemented in this lesson.

### Automated QC and GIGO

A conceptual QC pipeline developed during the discussion was:

```text
DICOM received
    ↓
Series completeness
    ↓
Spatial continuity
    ↓
Spacing consistency
    ↓
Anatomical coverage
    ↓
Motion and artifact assessment
    ↓
Contrast-phase suitability
    ↓
Protocol compatibility
    ↓
PASS / WARNING / HUMAN REVIEW
```

Garbage In, Garbage Out (GIGO) expresses that sophisticated downstream analysis cannot automatically compensate for poor or inappropriate input data.

### False positives, false negatives, and thresholds

In a motion-QC scenario:

- **False positive:** the algorithm reports motion when the image is acceptable or has no relevant motion.
- **False negative:** the algorithm reports no motion when relevant motion is present.

Sensitivity asks how many truly problematic cases were detected. Specificity asks how many truly acceptable cases were correctly recognized. This lesson introduces these ideas conceptually rather than teaching statistical evaluation in depth.

Consider two hypothetical systems. System A has high sensitivity and sends 2,500 studies for human review. System B sends only 500, but more problematic studies may enter the accepted dataset. For a research QC scenario, the learner preferred System A because unnoticed problematic images could undermine confidence in the supposedly accepted dataset.

A decision threshold changes sensitivity, specificity, false positives, false negatives, and human workload. PPV, NPV, ROC curves, and calibration remain future learning directions.

### Task-specific image quality

A conceptual motion-severity scale might be:

```text
0 — no relevant motion
1 — mild motion
2 — moderate motion
3 — severe motion / potentially unsuitable
```

This is not a validated scale. Image quality should be judged relative to the intended task. An image potentially adequate for measuring a large-organ volume may not be adequate for radiomics of a very small lesion.

### Image registration

Image registration estimates spatial correspondence between images. PET and CT provide an introductory example: the same patient does not guarantee perfect spatial correspondence.

Differences may involve positioning, breathing, motion, FOV, matrix, voxel size, orientation, and acquisition time. Rigid, affine, and deformable registration are introduced only as categories. Their algorithms are not taught here.

Visually pleasing alignment does not prove quantitatively valid registration. Landmarks, similarity metrics, registration error, and Target Registration Error (TRE) remain future learning topics.

### Longitudinal imaging

Consider CT before treatment and CT three months after treatment. Slice 125 at baseline is not automatically anatomically equivalent to Slice 125 at follow-up.

> Same slice number does not mean same anatomical location.

The learner proposed checking anatomy, positioning, lesion location, anatomical landmarks, contrast phase, motion, artifacts, surgical material, lesion boundaries, volume, and enhancement. Longitudinal comparison requires appropriate anatomical correspondence and sufficiently comparable imaging conditions.

### DICOM privacy and de-identification

Removing Patient Name alone is insufficient. Depending on the DICOM object, potentially identifying information may include Patient Name, Patient ID, birth date, accession number, institution, physician information, dates and times, identifiers, private tags, burned-in text, and other metadata.

The exact de-identification process depends on applicable governance, research protocol, institutional requirements, and law. This learning record does not provide legal advice.

### Re-identification risk

In a hypothetical public-person scenario, a combination such as hospital, date, time, modality, anatomical region, and a publicly known hospitalization could increase re-identification risk even without an explicit name.

Identifiability does not depend only on one name field. As a professional reflection, the learner noted that patient labels in the clinical environment are disposed of through protected destruction procedures because apparently simple labels can contain identifying information. No institution or patient is identified here.

### Identification in image content

Identifying information may exist in image content, not only metadata. Examples can include burned-in annotations and facial anatomy in some head-imaging contexts. Defacing is introduced as a future concept, not an implemented method.

Altering pixels can also affect future analysis and therefore requires an appropriate, validated methodology.

### De-identification, anonymization, and pseudonymization

- **De-identification:** a broad process of removing or transforming identifying information to reduce identification risk.
- **Anonymization:** used generally for data intended to no longer be reasonably attributable to an individual under the applicable standard and context.
- **Pseudonymization:** direct identifiers are replaced by a code while a protected linkage may still exist separately.

A longitudinal analytical dataset might use:

```text
PATIENT_037
├── Baseline
├── 3 months
├── 6 months
└── 12 months
```

This can preserve longitudinal identity without exposing the patient's name. The linkage key must remain separate, protected, and access-controlled. These are high-level concepts rather than jurisdiction-specific legal conclusions.

### Multicenter pre-segmentation QC

The final conceptual challenge involved 2,000 abdominal CT examinations from four hospitals for a small liver-lesion study. No dataset was accessed or analyzed. Before segmentation, the learner reasoned that a research workflow should:

1. Confirm the privacy, de-identification, or pseudonymization strategy.
2. Define the scientific question and intended contrast phase.
3. Understand participating centers and patient populations.
4. Preserve permitted patient and disease metadata.
5. Document scanner manufacturers, models, software, and reconstruction information.
6. Review kV, mAs or exposure information, FOV, thickness, spacing, pixel spacing, voxel geometry, kernel, and contrast information.
7. Select the intended series without trusting Series Description alone.
8. Evaluate actual image quality and contrast behavior.
9. Check anatomical coverage, missing images, and spatial gaps.
10. Assess motion, breathing, positioning, arms-down artifacts, and metal or surgical artifacts when relevant.
11. Determine whether quality is appropriate for small-lesion analysis.
12. Define Ground Truth methodology.
13. Release only appropriate data for segmentation.

The conceptual sequence is:

```text
Privacy
    ↓
Scientific question
    ↓
Population
    ↓
Scanner and protocol
    ↓
Series selection
    ↓
Geometry
    ↓
Image quality
    ↓
Contrast phase
    ↓
QC flags
    ↓
Ground Truth methodology
    ↓
Segmentation release
```

### Ground Truth clarification

Ground Truth is not simply a “high-quality reference image.” It refers to the reference annotation, segmentation, label, or other reference standard used for evaluation, depending on the research task.

Image quality and Ground Truth quality are related but distinct concepts. Poor image quality may increase annotation uncertainty, while Ground Truth quality also depends on methodology, reviewers, consensus, and documentation.

### Scientific English vocabulary

| Term | Meaning or use in this learning context |
|---|---|
| DICOM metadata | Attributes associated with a DICOM object. |
| provides | Supplies or makes information available. |
| contains | Holds or includes information. |
| about | Indicates the subject of information. |
| acquired | Obtained during image acquisition. |
| was acquired | Singular past-passive acquisition expression. |
| were acquired | Plural past-passive acquisition expression. |
| protocol | Defined acquisition or analysis instructions. |
| planned | Intended before execution. |
| actually | Refers to what occurred in practice. |
| happened | Describes what occurred. |
| Study | A DICOM grouping associated with an imaging study. |
| Series | A related grouping of DICOM instances. |
| Instance | An individual DICOM object. |
| confidence score | A system output expressing assigned confidence. |
| human-in-the-loop | A workflow incorporating human review or decisions. |
| motion | Patient or anatomical movement affecting image appearance. |
| detected | Identified by an observer or system. |
| false positive | A positive output when the target condition is absent. |
| false negative | A negative output when the target condition is present. |
| sensitivity | Proportion of true problematic cases detected conceptually. |
| specificity | Proportion of true acceptable cases recognized conceptually. |
| threshold | Decision boundary affecting classification behavior. |
| Pixel Spacing | Physical sampling distance within the image plane. |
| Slice Thickness | Reconstructed thickness represented by an image slice. |
| Image Position | Physical location information in patient coordinates. |
| Image Orientation | Direction information in patient coordinates. |
| isotropic | Having similar voxel dimensions along all axes. |
| anisotropic | Having unequal voxel dimensions across axes. |
| interpolation | Estimation of values between available samples. |
| aligned | Placed in corresponding spatial positions. |
| analyzed | Examined systematically. |
| before | Earlier than another step. |
| between | Expresses a relationship involving two or more entities. |
| same | Equivalent in a specified respect. |
| registration | Estimation of spatial correspondence between images. |
| data | Recorded information used in analysis. |
| date | Calendar information that may be identifying. |
| data sharing | Controlled provision of data to another party or environment. |
| patient identifiers | Information that may identify an individual. |
| removed | Deleted or excluded according to an approved process. |
| protected | Safeguarded through technical and organizational controls. |
| pseudonymization | Replacement of direct identifiers by a code with separate protected linkage. |

Scientific English sentences practiced during this learning session:

> DICOM metadata provides information about how a medical image was acquired.

> The protocol describes what was planned, but the image shows what actually happened.

> The algorithm detected motion in the image.

> Slice thickness and spacing between slices are not always the same.

> File order is not anatomical geometry.

> Interpolation cannot recover information that was not acquired.

> The images must be aligned before quantitative comparison.

> Same slice number does not mean same anatomical location.

> DICOM metadata contains information about image acquisition.

> Patient identifiers must be removed or protected before data sharing.

> Metadata tells us about acquisition. Image content tells us about the resulting image.

These are vocabulary and sentences practiced during the learning session; they do not imply English-language proficiency.

## Practical Workflow

### 1. Receive the DICOM dataset in an authorized environment

Confirm that access, storage, and processing are permitted under the applicable governance and research protocol.

### 2. Review de-identification or pseudonymization

Check metadata and image-content risks using an approved process. Keep any linkage key separate and protected.

### 3. Organize Study, Series, and Instance relationships

Use DICOM hierarchy and UIDs conceptually rather than relying on filenames or folders alone.

### 4. Extract relevant metadata

Collect center, scanner, acquisition, reconstruction, contrast, geometry, and hierarchy attributes required by the scientific question. Record missing or inconsistent fields.

### 5. Identify candidate series

Use metadata to narrow candidates, then verify the intended image content, phase, reconstruction, anatomy, and coverage.

### 6. Validate spatial geometry

Review Pixel Spacing, Image Position, Image Orientation, Slice Thickness, and derived inter-image relationships. Do not assume file order defines anatomy.

### 7. Check completeness and gaps

Assess physical continuity, expected coverage, repeated or missing positions, and possible transfer or reconstruction problems. Separate detection from causal conclusions.

### 8. Assess anatomical coverage

Confirm that the region required by the scientific question is included sufficiently.

### 9. Assess contrast phase

Compare protocol metadata with actual image characteristics. Assign uncertainty for human review rather than forcing an unsupported automatic decision.

### 10. Assess motion and other artifacts

Review inter-slice continuity, anatomy, noise, motion, metal, positioning, and other task-relevant limitations.

### 11. Assess task-specific suitability

Determine whether quality is suitable for the intended segmentation or measurement rather than assigning a universal quality label.

### 12. Assign a QC status

Use a documented status such as `PASS`, `WARNING`, `REVIEW`, or `EXCLUDE`, with reasons and reviewer criteria.

### 13. Define or confirm Ground Truth workflow

Document reference annotation, reviewers, consensus, uncertainty, and relation to source-image quality.

### 14. Release accepted data for segmentation

Release only data that satisfy privacy, geometry, content, quality, and task-specific criteria.

The conceptual workflow is:

```text
Receive DICOM dataset
    ↓
Confirm authorized data environment
    ↓
De-identification / pseudonymization check
    ↓
Organize Study / Series / Instance relationships
    ↓
Extract metadata
    ↓
Identify candidate series
    ↓
Validate spatial geometry
    ↓
Check completeness and gaps
    ↓
Assess anatomical coverage
    ↓
Assess contrast phase
    ↓
Assess motion and artifacts
    ↓
Assess task-specific suitability
    ↓
PASS / WARNING / REVIEW / EXCLUDE
    ↓
Document QC decision
    ↓
Define or confirm Ground Truth workflow
    ↓
Release accepted data for segmentation
```

No automated production QC system was implemented during this lesson.

## Quality Checklist

Before releasing medical imaging data for segmentation:

- [ ] The scientific question is defined.
- [ ] The authorized research environment is confirmed.
- [ ] The privacy strategy is defined.
- [ ] De-identification or pseudonymization is reviewed.
- [ ] Study, Series, and Instance organization is checked.
- [ ] Relevant metadata are preserved.
- [ ] Center is documented appropriately.
- [ ] Scanner manufacturer and model are documented.
- [ ] Software and reconstruction information are documented when available.
- [ ] Acquisition and reconstruction parameters are documented.
- [ ] Contrast information is documented.
- [ ] The intended series is identified.
- [ ] Series Description is verified rather than blindly trusted.
- [ ] Slice Thickness and Pixel Spacing are checked.
- [ ] Spatial positions and orientation are checked.
- [ ] Inter-slice continuity is assessed.
- [ ] Missing-image and gap risk is assessed.
- [ ] Anatomical coverage is assessed.
- [ ] Motion and other artifacts are assessed.
- [ ] Contrast-phase suitability is assessed.
- [ ] Task-specific image quality is assessed.
- [ ] Potential confounders are documented.
- [ ] A QC status is assigned with reasons.
- [ ] Human-review criteria are defined.
- [ ] Ground Truth methodology is defined.
- [ ] Data are approved before segmentation.

Common errors to avoid:

- treating DICOM as pixel data without context;
- assuming every metadata field is present or correct;
- selecting a series by description alone;
- using image count as proof of completeness;
- sorting anatomy by filenames or instance numbers alone;
- treating Slice Thickness as complete through-plane geometry;
- interpreting smooth interpolation or models as recovered resolution;
- using confidence scores as automatically calibrated probabilities;
- evaluating QC without a task-specific definition;
- assuming the same slice number gives longitudinal correspondence;
- removing Patient Name while leaving other identifying information unreviewed;
- treating a professional observation as scientific validation.

## Lessons Learned

1. DICOM is more than an image file.
2. Metadata helps explain how an image was produced.
3. Metadata should not automatically be assumed complete or correct.
4. Series selection is a scientific QC problem.
5. Protocol labels describe intent, while image content helps assess the actual result.
6. Image count alone does not establish series completeness.
7. File order is not anatomical geometry.
8. Slice Thickness and inter-slice spacing are not necessarily equivalent.
9. Pixel spacing and through-plane sampling jointly influence voxel geometry.
10. Isotropic and anisotropic voxels have different implications for 3D analysis.
11. Interpolation cannot recreate missing anatomical information.
12. Visually smooth models do not guarantee accurate underlying spatial information.
13. Motion QC can be framed as a measurable computational problem.
14. False positives and false negatives matter when designing automated QC.
15. Threshold selection changes both scientific risk and human workload.
16. Image quality is task-specific.
17. Registration is required when spatial correspondence cannot be assumed.
18. Same slice number does not mean same anatomical location.
19. Removing Patient Name alone does not guarantee adequate de-identification.
20. Pseudonymization can preserve longitudinal linkage while limiting direct identity exposure.
21. Data quality must be assessed before segmentation, radiomics, or AI.
22. Clinical imaging experience can generate useful QC hypotheses, but those hypotheses still require scientific validation.

Additional conclusions include:

- Ground Truth is a reference annotation or standard, not merely a high-quality image.
- Image quality and Ground Truth quality are related but distinct.
- Identifiability can arise from combinations of metadata and image content.
- Automated QC should support traceable decisions and human review rather than hide uncertainty.

## Future Learning Directions

- Study pydicom and Python loops and functions for safe DICOM processing.
- Develop automated metadata extraction with missing-field handling.
- Study DICOM dictionaries, private tags, and transfer syntax.
- Study DICOM coordinate systems, LPS and RAS, affine transformations, and resampling.
- Compare interpolation methods without assuming recovered information.
- Implement and validate rigid, affine, and deformable registration in future stages.
- Study registration landmarks, error measures, and Target Registration Error.
- Explore automated anatomical-coverage and motion detection.
- Study contrast-phase classification and confidence calibration.
- Introduce ROC curves, PPV, NPV, and threshold optimization.
- Develop automated QC systems only after establishing reference labels and validation methods.
- Study applicable de-identification standards and defacing methodology.
- Investigate longitudinal imaging analysis and multimodal PET/CT and PET/MRI analysis.
- Make no claim of proficiency until future study and evidence support it.

