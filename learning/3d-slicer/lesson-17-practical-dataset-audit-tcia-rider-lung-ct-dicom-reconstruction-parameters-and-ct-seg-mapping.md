# Lesson 17 – Practical Dataset Audit: TCIA RIDER-LUNG-CT, DICOM Reconstruction Parameters and CT–SEG Mapping

**Learning path:** 3D Slicer
**Date:** 2026-08-27
**Status:** Learning record
**Scope:** Practical audit of public dataset documentation, metadata, and selected DICOM headers; no full dataset download, quantitative experiment, metric calculation, radiomics, AI training, or patient-specific conclusion

## Objectives

- Begin the practical phase using a real public dataset without presenting exploration as a completed experiment.
- Evaluate RIDER-LUNG-CT as a candidate for the planned slice-thickness study.
- Inspect TCIA collection documentation, the metadata spreadsheet, NBIA series, and selected DICOM tags.
- Distinguish CT acquisition measurements, image reconstruction, reconstructed CT series, and visualization.
- Investigate the structural relationship between DICOM CT and DICOM SEG.
- Use Study Instance UID, Series Instance UID, and Series Number appropriately during the audit.
- Locate Slice Thickness and Convolution Kernel in real public DICOM metadata.
- Identify comparable reconstruction thicknesses while recognizing reconstruction kernel as a potential confounder.
- Prepare the future systematic CT–SEG mapping and pilot-series selection without performing them.

## Scientific Background

### Continuity from Lessons 15–16

Lessons 15–16 developed a conceptual protocol connecting slice thickness, segmentation,
volumetric measurement, and lesion size. Lesson 17 moved from planning to the practical audit of
a real public candidate: **RIDER-LUNG-CT**, hosted by The Cancer Imaging Archive (TCIA). The work
examined public documentation, a metadata spreadsheet, NBIA organization, and selected DICOM
headers. It did not perform the planned quantitative experiment.

The planned conditions in Lesson 16 were 1 mm as the operational reference, optional 1.5 mm, and
3 and 5 mm comparisons. The candidate dataset instead documents 1.25, 2.5, and 5 mm
reconstructions. This is not a planning error. It illustrates the scientific sequence:

```text
planned protocol
    ↓
dataset audit
    ↓
feasibility assessment
    ↓
justified protocol refinement, if necessary
```

No definitive protocol change was made. Reconstruction completeness, segmentation availability,
lesion characteristics, lesion-size distribution, and suitability for the small-lesion question
remain to be assessed systematically.

### Acquisition and reconstruction

CT acquisition refers to the collection of physical measurements by the scanner detector system.
Those acquisition measurements are not the same as the axial images later reviewed. Reconstruction
algorithms use acquisition data to produce CT image series for visualization and analysis.

Depending on the protocol and available acquisition data, one acquisition may support multiple
reconstructions with different slice thicknesses, reconstruction kernels, reconstruction
diameters or fields of view, and other parameters. Images appearing automatically on a scanner
console after acquisition may be automatically reconstructed for review or *Auto View*; immediate
display does not mean that raw projection data are being viewed.

```text
acquisition / raw projection data
    ↓
reconstruction
    ↓
CT image series
    ↓
visualization, PACS, or DICOM analysis
```

The availability of raw projection data in RIDER-LUNG-CT was not established or claimed.

### DICOM CT, DICOM SEG, and identifiers

A CT series contains reconstructed computed-tomography images. A DICOM SEG object contains
segmentation information associated with source images. During the audit, CT series contained
dozens or hundreds of images, while a SEG series could display `Image Count = 1`. This does not
mean that only one slice was segmented: one DICOM SEG object can contain multiple frames
representing segmentation across a volume.

**Study Instance UID** identifies the DICOM study context. **Series Instance UID** identifies a
specific series. A Series Number alone should not be used to correlate series from different
studies.

The dataset documentation *Correlation Between DICOM Image Series and DICOM SEG Segmentation*
states that the corresponding CT and SEG series in this collection share a Series Number within
the same Study Instance UID. The dataset-specific audit rule was therefore:

```text
same Study Instance UID
    +
same Series Number
    ↓
documented CT–SEG correspondence in RIDER-LUNG-CT
```

One public example was checked manually: a CT series with Series Number 2 and a SEG series with
Series Number 2 inside the same Study Instance UID. This rule is recorded only as documented for
this collection and is not generalized to unrelated datasets.

### Dataset provenance and scope

The official TCIA collection page was inspected with the following observed information:

| Field | Observed value |
|---|---|
| Collection | RIDER-LUNG-CT / RIDER Lung CT |
| Version | 3 |
| Updated | 2024-06-25 |
| DOI | `10.7937/K9/TCIA.2015.U1X8A5NR` |
| Anatomy | Chest |
| Disease context | Lung cancer / NSCLC context |
| Relevant data types | CT and SEG |
| Image format | DICOM |
| Subjects | 32 |
| Studies | 100 |
| Series | 936 |
| Images | 81,548 |
| Image-data size | 43.01 GB |
| Image-data license | CC BY 4.0 |

The page reports reconstruction combinations using slice thicknesses of 1.25, 2.5, and 5 mm
with LUNG and STANDARD kernels. The audit did not establish that every subject has every
combination without missing or unsuitable series.

Licensing was treated per resource rather than as one universal license. The image data were
listed as CC BY 4.0, lesion notes as CC BY 3.0, and the CT–SEG correlation document as CC BY 4.0.
Future reuse must retain appropriate attribution and recheck the terms applying to each resource.

The official dataset citation is:

> Zhao, B., Schwartz, L. H., Kris, M. G., & Riely, G. J. (2015). *Coffee-break lung
> CT collection with scan images reconstructed at multiple imaging parameters* (Version 3)
> [Dataset]. The Cancer Imaging Archive. https://doi.org/10.7937/k9/tcia.2015.u1x8a5nr

Sources reviewed:

- [RIDER-LUNG-CT official collection page](https://www.cancerimagingarchive.net/collection/rider-lung-ct/)
- [Correlation Between DICOM Image Series and DICOM SEG Segmentation](https://www.cancerimagingarchive.net/tcia-downloads/rider-lung-ct-da-other-2/riderlungct_correlation-between-dicom-image-series-and-dicom-seg-segmentation/)

### Metadata spreadsheet audit

The TCIA file `RIDER-Lung-CT_v3_20240625-nbia-digest.xlsx` was opened during the session. Fields
observed included Patient ID, Study Instance UID, Series Instance UID, Modality, Series Number,
Manufacturer, Manufacturer Model Name, Software Versions, Image Count, and license or
administrative metadata.

No explicit Slice Thickness column was found during the manual spreadsheet inspection. Series
with approximately 60, 120–130, and 250–260 images suggested that image count might help locate
candidate reconstruction groups, but the suggestion was not accepted as confirmation.

> Image Count is a clue, not direct evidence of Slice Thickness.

Slice thickness was subsequently checked in the appropriate DICOM tag through NBIA.

### Practical NBIA and DICOM-header investigation

The practical navigation performed was:

```text
TCIA RIDER-LUNG-CT collection page
    ↓
Browse / Search
    ↓
NBIA Data Browser
    ↓
RIDER Lung CT collection and patient
    ↓
Study and individual series
    ↓
DICOM metadata
    ↓
selected DICOM tags
```

The public dataset identifier `RIDER-1129164940`, also used in the supplied CT–SEG correlation
documentation, was inspected. The reviewed study was dated 2006-09-05 and had Study Instance UID
`1.3.6.1.4.1.14519.5.2.1.295526028989915648257590762384148204592`. These are public,
de-identified dataset identifiers; no additional identity information was introduced.

One inspected CT series showed:

| DICOM or NBIA field | Observed value |
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
| Pixel Spacing | 0.835938 × 0.835938 mm |
| Rescale Intercept | -1024 |
| Rescale Slope | 1 |
| Rescale Type | HU |
| Single Collimation Width | 1.25 mm |
| Patient Identity Removed | YES |

The simultaneous values `Slice Thickness = 2.5 mm` and `Single Collimation Width = 1.25 mm`
provided a concrete distinction:

> Single Collimation Width is not Slice Thickness.

The 1.25 mm collimation value must not be used to label that reconstructed series as having
1.25 mm slice thickness. The appropriate Slice Thickness tag explicitly indicated 2.5 mm.

### Thickness groups and reconstruction kernel

Within the manually inspected study, STANDARD-kernel reconstructions were confirmed at 1.25,
2.5, and 5 mm. Approximate image counts were 250 for 1.25 mm, 131 for 2.5 mm, and 63 for 5 mm.
These counts describe observations in that study, not a universal mapping. Thickness was
determined from DICOM metadata rather than inferred from Image Count.

Reconstruction kernel was recognized as a potential confounder. To investigate slice thickness,
comparing `1.25 mm STANDARD`, `2.5 mm STANDARD`, and `5 mm STANDARD` is conceptually cleaner than
mixing a `5 mm LUNG` series into the comparison. If thickness and kernel both change, differences
may reflect thickness, kernel, or their interaction.

Kernel can influence sharpness, noise characteristics, edge appearance, local intensity
distribution, and texture. It may consequently affect segmentation, volumetric measurements,
and radiomic features. No feature extraction or empirical kernel effect was measured in this
lesson.

### Candidate status and segmentation provenance

RIDER-LUNG-CT is currently a **strong candidate dataset under practical evaluation**, not the
accepted final dataset. The original small-lesion question remains open:

> Does RIDER-LUNG-CT contain a sufficient number and distribution of small lesions for the
> planned study?

The collection provides DICOM SEG and correlation documentation, but a ready-made segmentation
is not automatically ground truth. Before quantitative use, the available segmentation method,
annotator expertise, manual or automated components, review or consensus, segmentation
condition, QC procedure, and relationship to reconstruction conditions must be documented where
available. **Reference segmentation** remains the appropriate cautious term unless stronger
evidence justifies another status.

## Practical Workflow

### Work actually completed

- Opened the official RIDER-LUNG-CT collection page and accessed NBIA browsing.
- Inspected the Version 3 metadata spreadsheet and its available fields.
- Navigated one public de-identified patient, study, and multiple series.
- Opened real public DICOM headers and located acquisition and reconstruction metadata.
- Distinguished Slice Thickness from Single Collimation Width in an inspected series.
- Identified 1.25, 2.5, and 5 mm CT reconstructions using STANDARD kernel in one study.
- Reviewed the collection-specific CT–SEG correlation document.
- Manually verified at least one CT/SEG Series Number match within one Study Instance UID.
- Recognized reconstruction kernel as a variable requiring control in the future experiment.

### Reproducibility notes and planned schemas

Future automated metadata extraction should capture, when available:

```text
patient_id
study_instance_uid
series_instance_uid
series_number
modality
slice_thickness_mm
convolution_kernel
manufacturer
manufacturer_model
software_version
rows
columns
pixel_spacing_x_mm
pixel_spacing_y_mm
image_count
segmentation_series_uid
segmentation_series_number
qc_status
notes
```

The potential future analysis table remains a planned schema, not a populated dataset:

```text
case_id
study_instance_uid
ct_series_uid
seg_series_uid
series_number
thickness_mm
kernel
lesion_size_ref_mm
volume_cm3
absolute_volume_change
percentage_volume_change
dice
asd_mm
hd95_mm
qc_notes
included
exclusion_reason
```

### Lesson 17 checkpoint

**Completed:**

- real public dataset exploration;
- TCIA and NBIA navigation;
- metadata spreadsheet inspection;
- selected real public DICOM-header inspection;
- CT and SEG structural investigation;
- identification of 1.25, 2.5, and 5 mm CT reconstructions in one inspected study;
- identification of STANDARD reconstruction kernel;
- recognition of reconstruction kernel as a potential confounder;
- manual verification of at least one documented CT–SEG Series Number correspondence.

**Not yet completed:**

- full dataset download;
- systematic cohort extraction;
- complete CT–SEG mapping;
- lesion-size analysis;
- final dataset acceptance;
- quantitative segmentation experiment;
- volume or percentage volume-change calculations;
- Dice, ASD, HD95, or Bland–Altman analysis;
- statistical modeling;
- radiomics;
- AI model training.

## Quality Checklist

- [x] Dataset provenance reviewed on the official TCIA collection page.
- [x] TCIA collection and dataset DOI identified.
- [x] Dataset version and update date recorded.
- [x] Image format and image-data license identified.
- [x] Auxiliary-resource licenses distinguished from the image-data license.
- [x] Metadata spreadsheet inspected.
- [x] Public Patient ID structure inspected without adding identifying information.
- [x] Study Instance UID, Series Instance UID, and Series Number inspected.
- [x] CT and SEG modalities identified.
- [x] Dataset-specific CT–SEG correlation rule reviewed.
- [x] Selected real public DICOM header inspected.
- [x] Slice Thickness and Convolution Kernel tags located.
- [x] Manufacturer, scanner model, and software version recorded for the inspected series.
- [x] Pixel spacing inspected.
- [x] Slice Thickness distinguished from Single Collimation Width.
- [x] 1.25, 2.5, and 5 mm STANDARD series identified in the inspected study.
- [x] Reconstruction kernel recognized as a potential confounder.
- [ ] Complete CT–SEG correspondence mapped systematically.
- [ ] Reconstruction completeness audited across subjects.
- [ ] Segmentation provenance fully documented.
- [ ] Dataset suitability for small lesions established.
- [ ] Full dataset downloaded.
- [ ] Quantitative experiment executed.
- [ ] Volume, percentage volume change, Dice, ASD, or HD95 calculated.

## Lessons Learned

1. CT acquisition and CT reconstruction are not synonymous.
2. Images visible on scanner consoles or PACS are reconstructed images, not necessarily raw projection data.
3. A single acquisition may support multiple reconstruction series.
4. DICOM metadata are essential for quantitative imaging research.
5. Image Count alone cannot establish Slice Thickness.
6. Slice Thickness should be verified with the appropriate DICOM metadata.
7. Slice Thickness and Single Collimation Width are different concepts.
8. Study Instance UID provides study-level context.
9. Series Instance UID identifies an individual series.
10. In RIDER-LUNG-CT, Series Number can be combined with Study Instance UID to correlate CT and SEG according to the supplied documentation.
11. A DICOM SEG series may appear as one object while representing segmentation across a volume.
12. Reconstruction kernel is an important potential confounder.
13. Thickness comparisons should preferably hold kernel constant when the question aims to isolate thickness.
14. A theoretically ideal protocol may require revision after real-world dataset auditing.
15. Protocol adaptation must be scientifically justified and transparently documented.
16. Public availability does not remove the need to verify provenance, licensing, and segmentation methodology.
17. Dataset selection must be driven by the scientific question rather than convenience.
18. RIDER-LUNG-CT remains a candidate until reconstruction, segmentation, and lesion suitability are audited systematically.

## Future Learning Directions

- Map CT series systematically to their corresponding DICOM SEG series.
- Determine which reconstruction conditions have valid corresponding segmentations.
- Audit 1.25, 2.5, and 5 mm reconstruction completeness across subjects.
- Separate STANDARD and LUNG kernel conditions and predefine a kernel-control strategy.
- Inspect lesion notes and available segmentation-provenance documentation.
- Determine lesion-size distribution and evaluate whether enough small lesions are available.
- Select a small pilot sample before downloading large amounts of data.
- Download only the series required for that pilot.
- Import paired CT and DICOM SEG data into 3D Slicer and perform visual correspondence QC.
- Construct the quantitative analysis table before calculating volume and percentage volume change.
- Add Dice and visual QC, then consider ASD and HD95 progressively when justified.
- Expand toward radiomics only after the basic quantitative workflow is understood and reviewed.
- Continue Scientific English through contextual practice without treating technical vocabulary as conversational proficiency.
