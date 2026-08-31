# Lesson 19 – RIDER-LUNG-CT: DICOM SEG Source Verification and Quality Control

**Learning path:** 3D Slicer
**Date:** 2026-08-31
**Status:** Learning record
**Scope:** Practical single-case DICOM SEG source, metadata, geometry, semantic-label, and visual quality-control audit; no quantitative slice-thickness comparison, segmentation modification, metric calculation, radiomics, registration, resampling, or AI analysis

## Objectives

- Continue the unresolved DICOM SEG provenance investigation from Lesson 18.
- Verify the acquisition and reconstruction metadata of CT Series 2.
- Inspect the SEG metadata, Segment Sequence, frame count, geometry, and segmentation method.
- Investigate internal DICOM references rather than inferring association from Series Number alone.
- Distinguish Series Instance UID from SOP Instance UID in the practical source-image workflow.
- Compare the SEG semantic description with its visually observed anatomical location.
- Stop before quantitative analysis while semantic/anatomical consistency remains unresolved.

## Scientific Background

### Continuity from Lesson 18

Lesson 18 selected and downloaded a small public RIDER-LUNG-CT pilot, imported three CT series
and one DICOM SEG into 3D Slicer 5.10.0, and visualized the SEG with CT Series 2. Visual quality
control suggested that the segmented structure was in the hepatic region rather than in the lung
parenchyma expected from the segment label `lung`. The observation remained unresolved.

Lesson 19 investigated the SEG internally. The broader project still asks how reconstruction
parameters, especially slice thickness, may affect segmentation and derived quantitative
measurements. RIDER-LUNG-CT includes native 1.25, 2.5, and 5 mm reconstructions with STANDARD
and LUNG kernels. A future controlled pilot is intended to compare STANDARD reconstructions so
that reconstruction kernel is not intentionally mixed with slice thickness. That comparison was
not performed in this lesson.

### Reference segmentation and provenance

Availability in a public dataset does not make a segmentation perfect anatomical ground truth.
Before a mask is used for volume, Dice, ASD, HD95, radiomics, machine learning, or model
validation, its source images, geometry, semantic labels, segmentation method, provenance,
metadata consistency, and anatomical plausibility should be reviewed.

**Reference segmentation** remains the cautious term for this object. The audit verified several
technical relationships, but it did not resolve whether the semantic label and visual anatomical
location are consistent.

### DICOM identifiers used in the audit

**Series Instance UID** identifies a DICOM series. **SOP Instance UID** identifies one DICOM
instance. In a conventional CT series, individual images have distinct SOP Instance UIDs even
though they belong to the same Series Instance UID. A SEG can therefore identify a source series
and also reference a specific source image through its SOP Instance UID.

Equal Series Numbers alone were not treated as proof of association. This lesson inspected the
SEG's internal series and source-image references.

## Practical Workflow

### Dataset and case

The practical audit used the public, de-identified **RIDER-LUNG-CT** collection from The Cancer
Imaging Archive (TCIA), DOI
[`10.7937/k9/tcia.2015.u1x8a5nr`](https://doi.org/10.7937/k9/tcia.2015.u1x8a5nr).

| Item | Verified value |
|---|---|
| Dataset | RIDER-LUNG-CT |
| Patient research ID | `RIDER-1129164940` |
| Study date | 2006-09-05 |
| Study Instance UID | `1.3.6.1.4.1.14519.5.2.1.295526028989915648257590762384148204592` |
| 3D Slicer version | 5.10.0 |

No DICOM files were added to the repository.

### Loading CT and SEG

CT Series 2 and the DICOM SEG named **Tumor Segmentation** were loaded in 3D Slicer. The segment
appeared in Subject Hierarchy as `lung`. It was initially difficult to identify in the 2D views.
After activating Show 3D, a small beige structure became visible; navigation to the corresponding
location then revealed the mask in the axial, coronal, and sagittal views.

The dataset was not corrected or modified. The mask was not edited, propagated, or renamed.

### CT metadata verification

The metadata of CT Series 2 were opened and inspected directly:

| CT field | Verified value |
|---|---|
| Modality | CT |
| Manufacturer | GE MEDICAL SYSTEMS |
| Manufacturer Model Name | LightSpeed16 |
| Software Versions | 06MW03.5 |
| Series Number | 2 |
| Image Count | 131 |
| Slice Thickness | 2.5 mm |
| KVP | 120 |
| Convolution Kernel | STANDARD |
| Rows × Columns | 512 × 512 |
| Pixel Spacing | approximately 0.835938 × 0.835938 mm |
| Single Collimation Width | 1.25 mm |
| Rescale Intercept | -1024 |
| Rescale Slope | 1 |
| Rescale Type | HU |

`Single Collimation Width = 1.25 mm` does not classify this reconstruction as 1.25 mm. The
verified reconstructed **Slice Thickness is 2.5 mm**.

### SEG metadata verification

The DICOM SEG object was opened directly and the following values were observed:

| SEG field | Verified value |
|---|---|
| Modality | SEG |
| Series Description | Tumor Segmentation |
| Series Number | 2 |
| Rows × Columns | 512 × 512 |
| Segmentation Type | BINARY |
| Number of Frames | 1 |

This specific SEG object contained one segmentation frame. It was therefore not interpreted as a
complete volumetric lung segmentation. This single-frame observation applies to the inspected
object and was not generalized to all DICOM SEG objects or all RIDER-LUNG-CT annotations.

### Segment Sequence

The inspected `SegmentSequence` contained:

| Segment field | Observed value |
|---|---|
| Segment Number | 1 |
| Segment Label | `lung` |
| Segment Description | `lung` |
| Segmentation Algorithm Type | SEMIAUTOMATIC |
| Segmentation Algorithm Name | Weasis |
| Segmented Property Category | Type of Tumor |
| Segmented Property Type | `lung` |
| Recommended Display CIELab Value | `[45910, 35126, 36686]` |

The `lung` terminology was encoded in the DICOM SEG rather than created by 3D Slicer. This
documents the object's semantic metadata; it does not independently prove anatomical identity.

### Source image verification

The practical audit followed the SEG references through:

```text
PerFrameFunctionalGroupsSequence
    → DerivationImageSequence
        → SourceImageSequence
            → Referenced SOP Instance UID
```

A Referenced SOP Instance UID was present, demonstrating an explicit reference to a CT source
image used for the segmentation operation. `ReferencedSeriesSequence` was also investigated.
The referenced Series Instance UID was compared with the Series Instance UID of CT Series 2.

This supported the association:

```text
DICOM SEG
    → referenced CT Series 2
        → Slice Thickness 2.5 mm
        → Convolution Kernel STANDARD
```

The conclusion was based on internal DICOM references together with the CT metadata, not solely
on the shared Series Number.

### Geometry verification

The SEG metadata included:

| Geometry field | Observed value |
|---|---|
| Slice Thickness | 2.5 mm |
| Spacing Between Slices | 2.5 mm |
| Pixel Spacing | approximately 0.835938 × 0.835938 mm |
| Image Position (Patient), inspected frame | approximately `[-202, -214, -272.5]` |

These values were coherent with a mask positioned spatially within the CT volume. Geometric
placement did not, by itself, resolve semantic or anatomical correctness.

### Visual quality control

The main QC comparison was:

| QC item | Status |
|---|---|
| CT series identified | Verified |
| Slice thickness | 2.5 mm, verified |
| Reconstruction kernel | STANDARD, verified |
| SEG source association | Verified from internal DICOM references |
| Segment semantic label | `lung` |
| Visual anatomical location | Appeared in the hepatic region |
| Semantic/anatomical consistency | Unresolved |
| Quantitative analysis | Not performed |

> Visual inspection suggested that the segmented structure was located in the hepatic region
> rather than within the lung parenchyma.

This was recorded as a **potential semantic/anatomical inconsistency identified during visual
QC**. It was not interpreted as proof that the dataset, annotation, segmentation, or 3D Slicer
was wrong, and the structure was not diagnosed or definitively identified as a hepatic lesion.

### Key findings

- CT Series 2 was verified as a 2.5 mm STANDARD reconstruction with 131 images.
- The inspected SEG was binary, contained one frame, and encoded `lung` in its own segment metadata.
- The SEG recorded a semiautomatic method and Weasis as the algorithm name.
- Internal DICOM references supported the SEG-to-CT-Series-2 association.
- The SEG geometry was spatially compatible with the CT volume.
- Semantic metadata and visual anatomical location remained apparently discordant and unresolved.
- No quantitative conclusion was produced.

## Quality Checklist

- [x] Used only a public, de-identified research case.
- [x] Loaded CT Series 2 and Tumor Segmentation in 3D Slicer 5.10.0.
- [x] Verified CT modality, scanner, software, reconstruction, geometry, and rescale metadata.
- [x] Distinguished Single Collimation Width from reconstructed Slice Thickness.
- [x] Verified SEG modality, description, type, matrix, and Number of Frames.
- [x] Inspected Segment Sequence terminology and algorithm metadata.
- [x] Inspected ReferencedSeriesSequence and SourceImageSequence.
- [x] Distinguished Series Instance UID from SOP Instance UID.
- [x] Supported the SEG-to-CT-Series-2 association using internal DICOM references.
- [x] Compared semantic metadata with the visually observed anatomical location.
- [x] Recorded the discrepancy without changing the mask or asserting an error or diagnosis.
- [ ] Resolve the semantic/anatomical discrepancy.
- [ ] Establish whether this reference segmentation is suitable for the intended experiment.
- [ ] Systematically verify all metadata for the three planned STANDARD reconstructions.
- [ ] Perform independent segmentation or any quantitative comparison.

## Lessons Learned

1. A shared Series Number can be a useful clue but should not replace inspection of internal DICOM references.
2. Series Instance UID identifies a series; SOP Instance UID identifies an individual DICOM instance.
3. SourceImageSequence can preserve an explicit reference from a SEG frame to a source image.
4. ReferencedSeriesSequence supports verification of the source-series relationship.
5. Semantic terms displayed by software may originate in the DICOM object itself.
6. A one-frame DICOM SEG is not automatically a complete volumetric organ segmentation.
7. Compatible geometry and successful loading do not establish semantic or anatomical correctness.
8. Visual QC remains necessary after technical metadata checks succeed.
9. A public segmentation should be treated as a reference segmentation until its provenance and suitability justify stronger language.
10. An unresolved discrepancy is a reason to stop before measurement, not a reason to force the expected interpretation.

## Future Learning Directions

### Limitations at this checkpoint

- The audit covered one DICOM SEG object from one public research case.
- The structure's anatomical identity was not definitively established.
- The apparent semantic/anatomical inconsistency was not explained.
- No claim was generalized to other RIDER-LUNG-CT subjects or segmentations.
- No lesion volume, Dice, ASD, Hausdorff Distance, HD95, radiomics, statistical analysis, or AI training was performed.
- No independent segmentation, registration, resampling, mask propagation, or quantitative slice-thickness comparison was performed.
- No DICOM files or screenshots were versioned in the repository.

### Next Lesson

**Objective:** Build the first controlled slice-thickness comparison using native STANDARD
reconstructions from the same RIDER-LUNG-CT case.

Before quantitative measurement, the next lesson should:

1. Definitively identify the 1.25, 2.5, and 5 mm STANDARD reconstructions.
2. Record Series Number, Series Instance UID, Slice Thickness, Pixel Spacing, Image Count,
   Convolution Kernel, Frame of Reference UID, and relevant geometry metadata for each series.
3. Confirm that the reconstructions are appropriate comparisons from the same study.
4. Load all three conditions in 3D Slicer and locate the same structure or lesion.
5. Define a protocol for independent segmentation.
6. Begin quantitative measurement only after those checks are complete.

The 2.5 mm STANDARD condition is verified as Series 2 with 131 images. The other STANDARD
conditions still require systematic confirmation for the next experiment. The Series 2 mask
must not be assumed to transfer directly to 1.25 or 5 mm. Any future registration, resampling,
or propagation must be documented separately and must not be described as independent
segmentation.

Scientific English should continue through DICOM standard terminology, paper and documentation
reading, GitHub writing, professional communication, and oral explanation of the QC decision.
This educational portfolio is not validated medical software, a diagnostic tool, or a clinical
service.
