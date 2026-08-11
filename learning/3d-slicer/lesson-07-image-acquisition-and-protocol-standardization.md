# Lesson 07 – Image Acquisition and Protocol Standardization for Quantitative Medical Imaging

**Learning path:** 3D Slicer  
**Date:** 2026-08-11  
**Status:** Learning record  
**Scope:** Scientific learning documentation; no clinical data or patient-specific conclusions

## Objectives

- Understand that medical image analysis begins during image acquisition, before segmentation.
- Identify introductory CT acquisition and reconstruction parameters that may influence quantitative analysis.
- Explain why protocol standardization supports reproducibility in multicenter studies.
- Recognize sources of variability that exist before segmentation begins.
- Connect acquisition quality with segmentation, Ground Truth generation, radiomics, and future AI workflows.
- Document acquisition differences instead of assuming that images from different institutions are equivalent.
- Apply clinical reasoning to distinguish possible acquisition artifacts from true anatomical findings.
- Record scientific English vocabulary related to acquisition and protocol standardization.

## Scientific Background

### Moving one step earlier in the imaging pipeline

Previous lessons focused on segmentation, quality control, validation metrics, and observer variability. This lesson moves one step earlier in the imaging pipeline. Medical image analysis starts before segmentation; it starts during image acquisition.

The image presented to an observer or algorithm is shaped by the acquisition and reconstruction process. Understanding that process is fundamental for segmentation and for future study of radiomics, machine learning, deep learning, and digital twins. These later topics remain learning goals and are not presented as current competencies.

### Tube voltage

Tube voltage, expressed in kilovolts or kV, influences X-ray photon energy, image contrast, penetration, and radiation exposure. Different kV settings can change CT attenuation values and the visual relationship between tissues, which may affect thresholds and quantitative features.

### Tube current

Tube current and exposure time are commonly represented through mAs. They influence the number of X-ray photons used during acquisition. Lower photon counts may increase image noise, while exposure choices also relate to radiation dose. Noise differences can affect boundary visibility and measurement stability.

### Slice thickness and slice increment

Slice thickness describes the reconstructed thickness represented by each image slice. Thicker slices may reduce visible noise but increase partial-volume effects and reduce detail along the slice direction.

Slice increment describes the distance between reconstructed slice positions. It may be equal to, smaller than, or larger than slice thickness. Overlapping or gapped reconstructions change sampling and can affect three-dimensional analysis.

### Pixel spacing, matrix size, and Field of View

Pixel spacing describes the physical distance represented by adjacent pixels in the image plane. Matrix size describes the number of rows and columns used to represent the image. Field of View, or FOV, describes the physical area included in the reconstructed image.

Together, matrix size and FOV influence in-plane pixel dimensions. A larger FOV represented by the same matrix generally produces larger pixels and less in-plane spatial detail.

### Voxel size

A voxel is the three-dimensional image element formed by the in-plane pixel dimensions and the slice-direction spacing or thickness relevant to the reconstruction. Voxel size influences spatial resolution, partial-volume effects, volume measurements, segmentation boundaries, and quantitative feature stability.

### Reconstruction algorithms and kernels

The reconstruction algorithm converts acquired projection data into CT images. Different algorithm families and settings may change noise, resolution, and image texture.

The reconstruction kernel controls the balance between edge detail and image smoothness. A sharper kernel may improve edge appearance while increasing noise; a smoother kernel may reduce noise while reducing fine detail. These changes can influence segmentation and quantitative features even when the patient and acquisition are otherwise similar.

### Contrast phase

Contrast phase describes the timing of image acquisition relative to contrast administration. Arterial, venous, delayed, and other phases can produce different enhancement patterns. Comparing structures across different phases without documentation may introduce important variability.

### Scanner manufacturer, model, and software version

Scanner manufacturer, scanner model, detector and reconstruction technology, and software version may influence acquisition options and reconstructed image properties. Multicenter datasets can therefore contain technical variation even when institutions use protocols with similar names.

### Sources of variability before segmentation

Differences in kV, mAs, slice thickness, increment, pixel spacing, FOV, voxel size, reconstruction, kernel, contrast phase, scanner, and software can alter the image before an observer or model begins segmentation. Patient positioning, motion, body habitus, incomplete coverage, and artifacts add further variability.

This means that a segmentation difference is not always caused by the segmentation method alone. The image-generation process must be considered when interpreting results.

### Protocol standardization in multicenter studies

Multicenter studies attempt to use the same acquisition protocol whenever possible. When complete standardization is not feasible, differences should be documented so their possible influence can be evaluated.

Standardized protocols reduce avoidable variation and improve the comparability of images, segmentations, and quantitative measurements. Harmonization may later be used to address remaining differences, but it does not replace accurate acquisition documentation.

A standardized imaging protocol increases scientific reliability by establishing a clearer basis for reproducibility across institutions. Protocol adherence and deviations should be monitored rather than assumed.

### Relationship with Ground Truth

Ground Truth quality depends indirectly on acquisition quality. Noise, artifacts, poor contrast timing, thick slices, incomplete coverage, or limited spatial resolution can make anatomical boundaries more difficult to identify.

Expert review cannot recover information that was not adequately acquired. A reference segmentation should therefore be interpreted together with image quality, acquisition metadata, annotation protocol, and uncertainty.

### Relationship with AI and quantitative imaging

AI models learn from the images and labels provided to them. Acquisition and reconstruction differences can change image appearance and may influence model performance across scanners or institutions. Before attributing a performance difference to the model, researchers should examine whether acquisition conditions differ from the development or validation conditions.

Radiomics and other quantitative methods may also respond to changes in voxel size, noise, reconstruction, and contrast phase. These relationships require separate study and should not be reduced to a single acquisition rule.

### Clinical experience reflection

During routine experience with CT pulmonary angiography, a suspected pulmonary embolism appeared on the acquisition workstation. After the examination was reviewed on the diagnostic workstation with the radiologist, the finding was no longer considered consistent with true embolism; image noise or an acquisition or reconstruction artifact was considered a more plausible explanation.

This is an anonymized learning reflection, not a published case, research result, or independent diagnostic claim. It illustrates an important scientific principle: not every visual finding represents true pathology. Acquisition artifacts can influence both human interpretation and AI systems.

Practical CT experience contributed to understanding why scientific image analysis must consider the complete imaging pipeline. Familiarity with acquisition conditions can help identify plausible technical explanations without replacing formal review or validation.

### Scientific English vocabulary

| Term | Introductory meaning in this lesson |
|---|---|
| Acquisition | The process used to obtain image data. |
| Protocol | A defined set of acquisition or analysis instructions. |
| Reconstruction | The process that converts acquired data into images. |
| Kernel | A reconstruction setting that influences noise and spatial detail. |
| Voxel | A three-dimensional image element with physical dimensions. |
| Field of View | The physical area represented in the reconstructed image. |
| Pixel spacing | The physical distance represented between adjacent in-plane pixels. |
| Slice thickness | The reconstructed thickness represented by an image slice. |
| Reproducibility | The ability to obtain comparable results under documented conditions. |
| Standardization | The reduction of avoidable procedural differences through defined rules. |
| Multicenter study | A study conducted across more than one institution or center. |
| Ground Truth | The best available reviewed reference, not an absolute truth. |

Corrected scientific sentences from this lesson:

> Medical image acquisition parameters influence the quality of quantitative image analysis.

> A standardized imaging protocol improves reproducibility across multiple centers.

## Practical Workflow

### 1. Identify the intended quantitative task

Define whether the image will support segmentation, measurement, radiomics research, model development, or another documented objective. Different tasks may have different acquisition requirements.

### 2. Confirm the examination and series

Verify anatomy, acquisition phase, image coverage, orientation, and series description. Avoid combining or comparing series solely because their names appear similar.

### 3. Record acquisition parameters

Document available kV, mAs, slice thickness, slice increment, pixel spacing, matrix, FOV, and contrast phase. Record missing metadata explicitly rather than estimating it.

### 4. Record reconstruction information

Document the reconstruction algorithm, kernel, scanner manufacturer, model, and software version when available. Confirm whether multiple reconstructions exist from the same acquisition.

### 5. Review image quality

Inspect noise, motion, positioning, incomplete anatomy, contrast timing, and visible artifacts. Record limitations that may affect boundaries or quantitative measurements.

### 6. Compare institutional protocols

Before comparing segmentations across centers, identify which acquisition and reconstruction settings are equivalent and which differ. Check protocol adherence and document deviations.

### 7. Review Ground Truth conditions

Record how acquisition quality may have affected annotation difficulty. Link the reference method, reviewer process, image quality, and uncertainty.

### 8. Interpret segmentation or AI results in context

Investigate acquisition and reconstruction variation before attributing every difference to an observer, segmentation method, or AI model. Maintain anatomical and clinical review alongside technical analysis.

### 9. Preserve scientific documentation

Store protocol versions, metadata definitions, center information, preprocessing, segmentation method, reviewer information, and limitations with the analysis record.

## Quality Checklist

Before comparing segmentations between institutions:

- [ ] Acquisition protocols were identified and compared.
- [ ] Scanner manufacturer and model were documented.
- [ ] Reconstruction algorithm was documented.
- [ ] Reconstruction kernel was documented.
- [ ] Slice thickness and slice increment were reviewed.
- [ ] Pixel spacing, matrix, FOV, and voxel size were reviewed.
- [ ] Contrast phase and timing were documented.
- [ ] Image preprocessing was identified.
- [ ] Ground Truth generation and review were documented.
- [ ] Manual, semi-automatic, or automatic segmentation methods were identified.
- [ ] Reviewer experience and roles were documented appropriately.
- [ ] Image quality, noise, motion, artifacts, and coverage were reviewed.
- [ ] Protocol deviations and missing metadata were recorded.
- [ ] Scientific conclusions considered the entire imaging pipeline.

Common errors to avoid:

- beginning segmentation comparison without reviewing acquisition differences;
- treating slice thickness and slice increment as interchangeable;
- ignoring reconstruction kernel or contrast phase;
- assuming that similar protocol names guarantee equivalent images;
- attributing every visual finding to pathology;
- attributing every performance difference directly to AI failure;
- considering Ground Truth independently from image quality;
- estimating missing acquisition parameters instead of reporting them as unavailable;
- claiming harmonization or feature stability before those methods are studied and evaluated.

## Lessons Learned

- Medical image analysis begins before segmentation.
- Acquisition and reconstruction parameters shape the image available for analysis.
- Protocol standardization reduces unnecessary variability.
- Good acquisition and clear documentation improve reproducibility.
- Ground Truth quality is influenced by the quality and limitations of the source image.
- Multicenter comparison requires investigation of scanner, protocol, reconstruction, contrast, and preprocessing differences.
- Clinical experience helps identify possible acquisition and reconstruction artifacts.
- Not every visual finding represents true pathology.
- AI and quantitative results should be interpreted in the context of the complete imaging pipeline.
- Scientific conclusions depend on acquisition, reconstruction, preprocessing, segmentation, review, and intended application.

## Future Learning Directions

- Introduce image harmonization only after its objectives, assumptions, and limitations are studied.
- Study ComBat as a future statistical harmonization topic without implying current proficiency.
- Examine relevant DICOM metadata in a later lesson.
- Develop future material on preprocessing and image normalization.
- Study feature stability across acquisition and reconstruction settings.
- Explore multicenter AI only after the required data-governance and validation foundations are established.
- Use synthetic or appropriately licensed examples when comparing protocol effects.
- Add no claim of competence in these future methods until study and evidence support it.
