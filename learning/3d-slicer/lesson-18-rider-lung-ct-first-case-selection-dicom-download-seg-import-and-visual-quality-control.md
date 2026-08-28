# Lesson 18 – RIDER-LUNG-CT: First Case Selection, DICOM Download, SEG Import and Visual Quality Control

**Learning path:** 3D Slicer
**Date:** 2026-08-28
**Status:** Learning record
**Scope:** Practical single-case pilot covering series audit, selective download, DICOM import, SEG visualization, and anatomical/provenance quality control; no slice-thickness experiment, quantitative metric, radiomics analysis, or patient-specific conclusion

## Objectives

- Continue the practical RIDER-LUNG-CT evaluation developed in Lessons 15–17.
- Select one public, de-identified pilot case and audit its reconstruction series manually.
- Control reconstruction kernel while identifying 1.25, 2.5, and 5 mm comparison candidates.
- Download only the CT and DICOM SEG series needed for the first pilot.
- Import the selected data into 3D Slicer 5.10.0 and verify CT–SEG association.
- Perform visual anatomical quality control before any quantitative measurement.
- Document an unresolved discrepancy without converting an observation into an anatomical or provenance conclusion.

## Scientific Background

### Continuity from Lessons 15–17

Lessons 15–16 planned a study of how CT reconstruction conditions, particularly slice thickness,
may affect segmentation and derived quantitative measurements. Lesson 17 began the real-data
audit of **RIDER-LUNG-CT**. The initially planned conditions were approximately 1, optional 1.5,
3, and 5 mm. The available native reconstructions identified in this collection instead use
1.25, 2.5, and 5 mm with STANDARD and LUNG kernels.

The protocol was not silently rewritten to fit the available data. Lesson 18 records the first
practical pilot using the observed native conditions while preserving the difference between the
original plan and dataset reality. No quantitative slice-thickness comparison was performed.

### Dataset and pilot case

The public dataset was **RIDER-LUNG-CT**, hosted by The Cancer Imaging Archive (TCIA), DOI
[`10.7937/k9/tcia.2015.u1x8a5nr`](https://doi.org/10.7937/k9/tcia.2015.u1x8a5nr). Collection-level
documentation reviewed previously describes 32 subjects in an NSCLC/lung-cancer context,
same-day repeat CT acquisitions, multiple reconstruction settings, and CT and DICOM SEG objects.
This lesson does not imply that every reconstruction or segmentation in the collection has been
audited.

The first manually investigated pilot was:

| Field | Observed value |
|---|---|
| Patient ID | `RIDER-1129164940` |
| Study date | 2006-09-05 |
| Study Instance UID | `1.3.6.1.4.1.14519.5.2.1.295526028989915648257590762384148204592` |
| Series shown in NBIA | 9 |

This public, de-identified case was used to understand dataset organization before any
large-scale or quantitative analysis.

### Reconstruction metadata and kernel control

The manual audit inspected fields including Slice Thickness, Convolution Kernel, Series Number,
Series Instance UID, Study Instance UID, KVP, reconstruction and collection diameters, Image
Position and Orientation (Patient), Frame of Reference UID, Software Version, Patient Position,
Single Collimation Width, Pixel Spacing, Rows, Columns, and rescale parameters.

The practical observation reinforced that **Single Collimation Width is not automatically the
reconstructed Slice Thickness**. For example, `Single Collimation Width = 1.25 mm` does not make
a series with `Slice Thickness = 2.5 mm` a 1.25 mm reconstruction. Slice Thickness was used to
classify reconstructed thickness.

Both STANDARD and LUNG kernels were present. Because kernel may affect noise, sharpness, edge
definition, voxel intensities, segmentation boundaries, quantitative measurements, and future
radiomics features, the pilot direction keeps STANDARD constant whenever possible.

### DICOM SEG correlation and provenance

Two Tumor Segmentation objects were identified manually: one with Series Number 2 and another
with Series Number 3. The corresponding CT series were verified as 2.5 mm STANDARD and 2.5 mm
LUNG, respectively. No direct same-Series-Number SEG was identified during this inspection for
the 1.25 or 5 mm reconstructions.

This is a finding from one manually inspected study and must not be generalized to the entire
collection. Series Number was useful under the collection-specific documentation, but deeper
inspection of Referenced Series Sequence, Source Image Sequence, referenced SOP Instance UIDs,
and Frame of Reference UID may still be required.

## Practical Workflow

### 1. Manual series audit

The final mapping established during the practical inspection was:

| Series | Slice Thickness | Kernel | Images | SEG identified | Pilot use |
|---|---:|---|---:|---|---|
| 100 | 1.25 mm | STANDARD | 262 | No direct same-number SEG identified | Planned comparison |
| 103 | 1.25 mm | LUNG | approximately 250 | No direct same-number SEG identified | Not selected |
| 2 | 2.5 mm | STANDARD | 131 | SEG Series 2 | Reference/pilot |
| 3 | 2.5 mm | LUNG | 125 | SEG Series 3 | Not selected initially |
| 101 | 5 mm | STANDARD | 64 | No direct same-number SEG identified | Planned comparison |
| 104 | 5 mm | LUNG | 64 | No direct same-number SEG identified | Not selected |

This table describes only the manually audited study. A small CT series containing approximately
two images was also present and was not selected for the pilot comparison.

### 2. Selective NBIA download

Four series were placed in the NBIA cart rather than downloading the collection's tens of
gigabytes:

1. CT Series 100 — 1.25 mm, STANDARD, 262 images.
2. CT Series 101 — 5 mm, STANDARD, 64 images.
3. CT Series 2 — 2.5 mm, STANDARD, 131 images.
4. Tumor Segmentation — DICOM SEG associated with Series Number 2, one DICOM SEG object.

NBIA displayed an approximate cart size of 241 MB. The manifest was opened in NBIA Data
Retriever, all four selected items reached 100% with status **Complete**, and the local download
contained the RIDER Lung CT directory and `metadata.csv`. The entire dataset was not downloaded.

### 3. Import into 3D Slicer

The practical session used **3D Slicer 5.10.0**. The DICOM module initially reported that no
valid database existed at the default location, so a new DICOM database was created. Importing
the downloaded files reported:

- 1 patient;
- 1 study;
- 4 series;
- 458 instances.

The database showed CT Series 2, 100, and 101 plus Tumor Segmentation / SEG Series 2.

### 4. QuantitativeReporting extension

During import, this Slicer installation detected a segmentation object and suggested that
**QuantitativeReporting** might help work with it. The extension was found in Extensions Manager,
installed, and Slicer was restarted as requested. The DICOM database remained available after
restart. This observation does not establish that QuantitativeReporting is universally required
for modern Slicer DICOM SEG workflows.

### 5. Loading CT Series 2 and its SEG

The 2.5 mm STANDARD CT series and corresponding Tumor Segmentation object were loaded. The
segment was named `lung`. Slicer displayed:

```text
Source geometry: 2: Unnamed Series
Segmentation: Tumor Segmentation
Source volume: 2: Unnamed Series
```

This provided practical evidence that Slicer associated the imported segmentation geometry with
CT Series 2.

### 6. Visualization troubleshooting

Initially, changing segment visibility did not reveal an obvious overlay in the reviewed CT
slices, and Show 3D produced no obvious visible change. Several views and the initially expected
thoracic lesion region were inspected. Rather than assuming successful anatomical correspondence,
the workflow moved into quality-control investigation.

After using view-centering controls, a small beige structure became visible in the 3D view and
then as an axial CT overlay. This confirmed that the imported segmentation was not empty, had
geometric content, and could be displayed relative to the CT.

### 7. Unresolved anatomical/provenance discrepancy

The visible segmentation did **not** appear to correspond to the pulmonary lesion initially
expected. It appeared in the upper abdomen, apparently within or near the hepatic region, and
remained associated with that region while scrolling through the CT volume.

This is an unresolved visual observation, not a definitive anatomical identification. It does
not establish that the segment is a liver tumor, that the RIDER annotation is wrong, or that the
segmentation was created incorrectly. The anatomical identity and provenance of the segment
require further investigation, and possible explanations were not tested in this lesson.

```text
import annotation
    ↓
verify geometry and visibility
    ↓
perform visual anatomical QC
    ↓
observe unexpected anatomical location
    ↓
stop before quantitative measurement
    ↓
investigate segmentation provenance
```

This checkpoint demonstrates why filenames, dataset names, segment labels, metadata labels, and
successful automated loading are insufficient by themselves. A SEG can import, contain voxels,
produce a 3D representation, and align geometrically with a CT series while still requiring
anatomical and provenance verification before measurements are trusted.

### Scientific status at the end of the lesson

The project has progressed from conceptual study design to a real-data pilot workflow. Its exact
status is:

> **Dataset audit + case selection + download + DICOM import + segmentation provenance/QC investigation.**

No slice-thickness quantitative experiment or comparison between 1.25, 2.5, and 5 mm was
completed. No lesion volume, absolute or percentage volume change, Dice, ASD, HD95, radiomics,
statistical analysis, segmentation-accuracy result, or AI result was generated.

## Quality Checklist

- [x] Selected one real RIDER-LUNG-CT pilot case.
- [x] Audited reconstruction parameters in NBIA.
- [x] Identified 1.25, 2.5, and 5 mm reconstructions.
- [x] Distinguished STANDARD and LUNG kernels.
- [x] Identified relevant Series Numbers.
- [x] Selected STANDARD reconstructions for the pilot.
- [x] Selected the native DICOM SEG associated with Series 2.
- [x] Downloaded only the required pilot series.
- [x] Created and configured a Slicer DICOM database.
- [x] Imported 1 patient, 1 study, 4 series, and 458 instances.
- [x] Installed QuantitativeReporting after Slicer suggested it.
- [x] Loaded CT Series 2 and its corresponding DICOM SEG.
- [x] Verified Source geometry and Source volume as Series 2.
- [x] Confirmed that the segmentation contains visible geometry.
- [x] Observed a three-dimensional representation.
- [x] Performed visual anatomical QC.
- [x] Identified an unresolved anatomical/provenance discrepancy.
- [ ] Definitively identify the anatomical structure represented by the segment.
- [ ] Verify segmentation provenance internally in the DICOM SEG.
- [ ] Inspect source/reference sequences and SOP Instance UIDs if necessary.
- [ ] Verify whether the SEG corresponds to the intended pulmonary target.
- [ ] Independently segment the 1.25 mm reconstruction.
- [ ] Independently segment the 5 mm reconstruction.
- [ ] Calculate lesion volumes or volume changes.
- [ ] Calculate Dice, ASD, or HD95.
- [ ] Perform radiomics, multi-patient analysis, or statistical analysis.

## Lessons Learned

1. Real datasets frequently differ from an idealized study protocol.
2. DICOM metadata inspection is essential before quantitative analysis.
3. Slice Thickness and detector/collimation parameters must not be confused.
4. Reconstruction kernel is a potentially important confounding variable.
5. Series Number can assist CT–SEG correlation, but internal DICOM references may require verification.
6. One DICOM SEG object can encode a multiframe segmentation; one object does not mean one segmented slice.
7. Successful DICOM import does not prove that the intended anatomical target was identified.
8. A segment label such as `lung` should not be accepted blindly as anatomical truth.
9. Visual quality control is mandatory before quantitative measurements.
10. Unexpected observations should be documented rather than hidden or forced into the initial hypothesis.
11. A small pilot download can validate the workflow before committing to an entire large dataset.
12. Dataset and segmentation provenance are part of the scientific experiment, not administrative details.

## Future Learning Directions

- Begin the next lesson from the unresolved anatomical/provenance discrepancy.
- Inspect Referenced Series Sequence, Source Image Sequence, Frame of Reference UID, and referenced SOP Instance UIDs.
- Determine what anatomical target the `lung` segment actually represents.
- Verify whether the selected SEG is appropriate for the intended pulmonary-lesion experiment.
- Inspect the Series 3 SEG if it is relevant to resolving the mapping or provenance question.
- If the native annotation is unsuitable, choose transparently among another lesion or case, another annotation, independent segmentation under a predefined protocol, or reassessment of dataset suitability.
- Begin quantitative comparison only after anatomical identity and provenance are resolved.
- Preserve the possible future comparison of 1.25 mm STANDARD versus 2.5 mm STANDARD versus 5 mm STANDARD with kernel controlled.
- Treat volume, absolute and percentage volume difference, Dice, visual QC, ASD, and HD95 strictly as future work.
- Continue Scientific English through DICOM documentation, paper reading, GitHub writing, professional communication, and discussion of the QC decision.
- Do not present this educational investigation as validated medical software, a diagnostic tool, or a clinical service.
