# Lesson 08 – Image Preprocessing and Harmonization in Multicenter Medical Imaging

**Learning path:** 3D Slicer  
**Date:** 2026-08-12  
**Status:** Learning record  
**Scope:** Scientific learning documentation; no clinical data or patient-specific conclusions

## Objectives

- Understand why images from different hospitals cannot automatically be treated as equivalent.
- Understand preprocessing in quantitative medical imaging.
- Understand the purpose and limitations of resampling.
- Relate voxel spacing to spatial standardization.
- Explain why resampling cannot recreate anatomical information lost from the original reconstruction.
- Understand partial-volume effects in thicker voxels.
- Distinguish standardization from equivalence.
- Introduce normalization and harmonization without claiming practical proficiency.
- Distinguish technical variability from biological variability.
- Introduce confounding, shortcut learning, multicenter generalization, and feature robustness.
- Recognize the risk of overcorrection during harmonization.
- Explain why patient, disease, center, scanner, acquisition, and reconstruction metadata should remain traceable.
- Connect professional CT acquisition experience with quantitative-imaging methodology.

## Scientific Background

### Multicenter imaging scenario

Consider a hypothetical multicenter dataset with the following technical characteristics:

| Center | Scanner | Tube voltage | Reconstruction | Additional characteristic |
|---|---|---:|---|---|
| Hospital A | Siemens | 120 kV | 1 mm | Relatively smooth kernel |
| Hospital B | GE | 100 kV | 2.5 mm | Different reconstruction characteristics |
| Hospital C | Philips | 120 kV | 5 mm | Different Field of View |

Simply combining these images into one dataset may introduce technical variability. Differences can arise from the center, scanner manufacturer and model, acquisition settings, reconstruction settings, image geometry, contrast phase, software version, and local workflow.

The origin of every image should remain traceable. Relevant metadata may include:

- center and institution identifier permitted by the study;
- scanner manufacturer and model;
- acquisition parameters;
- reconstruction parameters and software version;
- slice thickness and slice increment;
- pixel spacing and voxel spacing;
- Field of View;
- reconstruction kernel;
- contrast phase;
- appropriately governed patient characteristics;
- disease characteristics and prevalence;
- Ground Truth methodology;
- segmentation method and reviewer process.

Traceability makes it possible to investigate whether an observed difference is technical, biological, procedural, or a combination of these factors.

### Preprocessing

Preprocessing includes transformations applied before a quantitative analysis, segmentation workflow, feature extraction, or model-development stage. Its purpose should be defined by the scientific question rather than by a generic rule.

Possible preprocessing goals include making spatial representation more consistent, reducing known technical variation, or preparing inputs for a defined method. Every transformation can also alter the data. Original characteristics, parameters, software, operation order, and limitations should therefore be preserved in metadata and documentation.

### Resampling and spatial standardization

Resampling represents image data on a new spatial grid. It may be used to create a common voxel spacing before segmentation, feature extraction, or model input.

Consider the conceptual example:

- Original A: `1 × 1 × 1 mm`
- Original B: `1 × 1 × 5 mm`
- Resampled B: `1 × 1 × 1 mm`

The resampled grid for B may have 1 mm spacing, but B does not acquire the same original spatial information as an image genuinely reconstructed at 1 mm. Interpolation estimates intermediate values from the available data. It cannot retrospectively recover anatomical information that was not preserved in the original reconstruction.

> Standardization does not guarantee equivalence.

The interpolation method, target spacing, image type, and treatment of discrete segmentation labels should be documented when applicable. Detailed comparison of interpolation methods remains a future learning topic.

### Partial-volume effect

A thick voxel may contain multiple tissue types. For example, one voxel may contain both normal liver and part of a lesion. Its resulting intensity can represent a mixture rather than either tissue in isolation.

Partial-volume effects may influence lesion conspicuity, visible boundaries, segmentation, quantitative measurements, and radiomic features. The degree and practical importance of these effects depend on anatomy, lesion size, image quality, reconstruction, and the intended analysis. A change in voxel dimensions does not necessarily produce a clinically meaningful difference in every situation.

### Standardization trade-off

Consider a hypothetical comparison:

- Hospital A: 1 mm reconstruction
- Hospital B: 5 mm reconstruction

One proposal is to convert all data to 5 mm. A potential benefit is increased consistency in spatial representation. A potential cost is loss of spatial detail from images originally reconstructed at thinner slices.

The appropriate decision depends on the scientific question. A small-lesion radiomics study may have different spatial requirements from an analysis of total lung volume. Preprocessing should not be chosen solely because one target spacing is convenient.

### Feature robustness

Feature robustness describes whether a quantitative feature remains sufficiently stable under relevant technical variation. As a hypothetical investigation, the same feature could be evaluated under reconstructions or representations at 1 mm, 2 mm, 3 mm, and 5 mm.

Some features may remain relatively stable, while others may vary substantially. Extracting hundreds of radiomic features does not automatically make every feature reliable. Future analysis should investigate stability, reproducibility, and fitness for the intended purpose. No feature-robustness experiment is claimed in this learning record.

### Confounding and shortcut learning

Consider another hypothetical dataset:

- Hospital A contains predominantly 1 mm images and 90% cancer cases.
- Hospital B contains predominantly 5 mm images and 90% non-cancer cases.

Center and technical protocol are associated with disease status in this scenario. An AI model might learn scanner, reconstruction, or hospital-related differences instead of biological characteristics of cancer.

This is an example of confounding: an additional variable is associated with both the input characteristics and the outcome, complicating interpretation. Shortcut learning occurs when a model relies on an easier unintended signal instead of the intended biological information.

A model could accidentally learn a “hospital signature” instead of a disease signature. High apparent performance does not guarantee that it learned the intended biological signal.

### Generalization and external centers

Multicenter diversity can be valuable because different scanners, protocols, populations, and institutions challenge a model under varied conditions. Diversity alone, however, does not guarantee generalization.

A conceptual design might use Hospital A and Hospital B for development and Hospital C for external testing. External validation evaluates performance on data not used for model development. Leave-one-center-out validation can conceptually repeat this separation while holding out one center at a time. These methods were not performed here and remain future learning topics.

### Normalization and harmonization

Normalization refers to processes intended to make data representation or intensity characteristics more comparable, depending on modality and analysis. MRI intensity values require particular consideration because they do not have the same universal physical intensity scale as CT Hounsfield Units.

Harmonization refers to processes intended to reduce unwanted systematic technical differences between centers, scanners, or protocols while preserving relevant biological information.

Harmonization does not mean making every dataset artificially identical. Its assumptions, target variables, retained metadata, and possible consequences require scientific justification and validation.

### Technical and biological variability

The key principle is:

> We should preserve biological information while reducing technical variability.

Suppose Hospital A has a younger population and Hospital B has an older population. If a feature differs between hospitals, the difference may reflect scanner or protocol effects, age, disease prevalence, other patient characteristics, biological differences, or combinations of these factors.

Automatically removing every center-associated difference could destroy meaningful biological information. Technical and biological variability should be investigated separately where possible, while recognizing that they may be confounded.

### Overcorrection

Overcorrection occurs when a preprocessing or harmonization procedure removes more variation than intended. If technical and biological differences are confounded, aggressive correction may remove genuine biological signal.

Before correcting a difference, researchers should investigate its likely origin, preserve relevant metadata, define which variation is unwanted, and evaluate whether the corrected data still support the scientific question.

### Controlled-experiment reasoning

The learning discussion proposed investigating how quantitative results behave under different technical conditions rather than immediately discarding features. In scientific terms, this reasoning involves:

- varying controlled technical conditions when scientifically and ethically appropriate;
- observing feature stability;
- preserving patient and biological metadata;
- comparing plausible technical and biological effects;
- investigating whether features remain associated with disease under relevant conditions.

This does not imply that prospective patient scanning should be modified solely for experimentation. Appropriate technical investigations may use existing reconstructions, phantoms, approved datasets, or properly designed and governed research protocols.

### Clinical experience reflection: CT-guided biopsy

The learner reported professional participation in many CT-guided biopsy workflows. A typical workflow described in the discussion included an initial upper-abdominal acquisition, lesion localization, reduction of the repeatedly acquired procedural region, possible reduction of tube current because multiple acquisitions were required, and maintenance of consistent reconstruction parameters during repeated localization.

A practical observation was that changing slice thickness during sequential biopsy imaging could change lesion conspicuity and spatial reference. Small lesions could appear in only a limited number of slices and become more difficult to identify when reconstruction characteristics changed. In some situations, another acquisition or reconstruction with thinner slices was used to improve localization.

This is an anonymized learning reflection, not scientific evidence, a published case, a formal experiment, or procedural medical guidance. Slice thickness alone should not be presented as the cause of every apparent disappearance. Motion, positioning, noise, contrast, partial volume, lesion characteristics, reconstruction, display, and other factors may influence conspicuity and localization.

The reflection illustrates connections between partial-volume effects, lesion conspicuity, spatial consistency, acquisition and reconstruction consistency, and procedural reference. It shows why consistent imaging parameters matter during repeated image-guided workflows without establishing a universal protocol.

### Connection with the previous clinical reflection

Lesson 07 documented an anonymized reflection about a suspected pulmonary embolism appearance on an acquisition workstation that was not supported after diagnostic review. Together, the reflections reinforce that image appearance can be influenced by acquisition, reconstruction, display, noise, and artifacts. Not every visual difference represents biological change.

### Scientific English vocabulary

| Term | Meaning in this learning context |
|---|---|
| Preprocessing | Transformations performed before a defined analysis stage. |
| Harmonization | Reduction of unwanted systematic technical variation while preserving relevant information. |
| Dataset | An organized collection of data with documented provenance and governance. |
| Resampling | Representation of image data on a different spatial grid. |
| Standardize | Apply defined rules to reduce avoidable procedural differences. |
| Voxel spacing | Physical distance represented between voxel positions. |
| Recover | Obtain information again; interpolation cannot recover information that was not preserved. |
| Acquired | Obtained during the image-acquisition process. |
| Slice thickness | Reconstructed thickness represented by an image slice. |
| Between | Expresses a relationship involving two or more groups or conditions. |
| With | Expresses association or use of a specified condition. |
| Instead of | Indicates replacement or an unintended alternative. |
| Image quality | Properties affecting the visibility and interpretation of image information. |
| Reproducibility | Ability to obtain comparable results under documented conditions. |
| Feature | A measured characteristic derived from data. |
| Feature robustness | Stability of a feature under relevant variation. |
| Generalization | Performance under data conditions beyond those used for development. |
| Confounding | Mixing of effects that complicates causal or predictive interpretation. |
| Shortcut learning | Reliance on an unintended easier signal rather than the intended information. |
| Biological | Related to patient, anatomy, physiology, or disease. |
| Technical | Related to acquisition, reconstruction, processing, or equipment. |
| Preserve | Retain information intentionally. |
| While | Indicates simultaneous or contrasting conditions. |
| Reducing | Making an unwanted effect smaller rather than necessarily eliminating it. |
| Consistency | Degree of procedural or representational agreement. |
| Overcorrection | Removal of meaningful variation through excessive correction. |

Scientific English sentences practiced during this lesson:

> Different acquisition protocols can affect image quality and segmentation results.

> Variations in slice thickness may affect the reproducibility of radiomic features.

> Resampling can standardize voxel spacing, but it cannot recover information that was not acquired.

> Standardization does not guarantee equivalence.

> The model may learn differences between hospitals instead of learning the biological characteristics of the disease.

> The difference between Hospital A and Hospital B is the slice thickness.

> The images were acquired with different slice thicknesses.

> Thicker slices may reduce image detail but improve consistency between datasets.

> We must separate biological differences from technical differences.

> We should preserve biological information while reducing technical variability.

## Practical Workflow

### 1. Define the scientific question

Specify the biological or technical question, intended quantitative output, population, and acceptance criteria before selecting preprocessing operations.

### 2. Preserve patient and disease metadata

Retain appropriate, permitted, and governed characteristics that may explain biological variability. Protect privacy and document missing or unavailable variables.

### 3. Preserve center identification

Maintain a traceable center variable suitable for evaluating center effects without exposing prohibited identifiers.

### 4. Record scanner metadata

Document manufacturer, model, software version, and other relevant equipment information when available.

### 5. Record acquisition parameters

Document kV, mAs, contrast phase, coverage, and other protocol parameters relevant to the scientific question.

### 6. Record reconstruction parameters

Document slice thickness, increment, pixel and voxel spacing, FOV, matrix, kernel, reconstruction algorithm, and version where available.

### 7. Perform quality assessment

Review noise, motion, artifacts, incomplete anatomy, contrast timing, and other limitations before transformation or segmentation.

### 8. Define and justify preprocessing

Specify each transformation, target representation, interpolation method when applicable, software version, parameter, and scientific rationale. Preserve original image characteristics in metadata.

### 9. Document segmentation and Ground Truth

Record the segmentation method, annotation protocol, reviewer process, software, quality controls, and uncertainty.

### 10. Extract features only under a defined method

Record feature definitions, configuration, image and mask inputs, preprocessing dependencies, and software versions. Feature extraction is a future implementation area and is not claimed here.

### 11. Investigate robustness

Evaluate whether relevant outputs remain sufficiently stable under justified technical variation. Distinguish planned analysis from completed evidence.

### 12. Apply harmonization only when justified

Investigate likely technical and biological sources before choosing a harmonization method. Define which variation should be reduced and how relevant biological information will be assessed.

### 13. Develop models with confounding controls

Examine center, scanner, protocol, population, and disease associations that could support shortcut learning. Model development remains a future learning stage.

### 14. Plan external validation

Identify an independent center or suitable multicenter strategy before interpreting generalization. External and leave-one-center-out validation are future methodological topics.

### 15. Interpret the complete pipeline

Interpret results in the context of patient biology, acquisition, reconstruction, quality, preprocessing, Ground Truth, feature robustness, center effects, and limitations.

The conceptual sequence is:

```text
Scientific question
    ↓
Patient and disease metadata
    ↓
Center identification
    ↓
Scanner metadata
    ↓
Acquisition parameters
    ↓
Reconstruction parameters
    ↓
Quality assessment
    ↓
Preprocessing
    ↓
Segmentation / Ground Truth
    ↓
Feature extraction
    ↓
Robustness analysis
    ↓
Harmonization if justified
    ↓
Model development
    ↓
External validation
    ↓
Interpretation
```

Preprocessing should not be a blind automated step. Every transformation requires a scientific justification and a record of its expected benefit, possible cost, and limitations.

## Quality Checklist

Before preprocessing multicenter imaging data:

- [ ] The scientific question is clearly defined.
- [ ] Center information is preserved in an appropriate governed form.
- [ ] Patient metadata are preserved when appropriate and permitted.
- [ ] Disease characteristics and prevalence are documented when relevant.
- [ ] Scanner manufacturer is documented.
- [ ] Scanner model and software version are documented when available.
- [ ] Acquisition protocol is documented.
- [ ] Reconstruction parameters are documented.
- [ ] Slice thickness and slice increment are documented.
- [ ] Pixel spacing and voxel spacing are documented.
- [ ] FOV, matrix, and kernel are documented when applicable.
- [ ] Contrast phase is documented when applicable.
- [ ] Ground Truth methodology is documented.
- [ ] Segmentation methodology and reviewer process are documented.
- [ ] The resampling strategy is scientifically justified.
- [ ] The interpolation method is documented when applicable.
- [ ] Original image characteristics are preserved in metadata.
- [ ] Potential confounders are investigated.
- [ ] Technical and biological variability are considered separately where possible.
- [ ] The risk of shortcut learning is considered.
- [ ] Feature robustness is evaluated when relevant.
- [ ] Harmonization is scientifically justified rather than automatic.
- [ ] The risk of overcorrection is considered.
- [ ] An external-validation strategy is considered.
- [ ] No preprocessing step is presented as recovering unavailable anatomical information.

Common errors to avoid:

- treating images from different centers as automatically equivalent;
- resampling without preserving original spacing and reconstruction metadata;
- assuming that a 1 mm output grid proves 1 mm original information;
- selecting target spacing without reference to the scientific question;
- combining center and disease effects without examining confounding;
- interpreting apparent model performance without checking for hospital signatures;
- treating every extracted feature as robust;
- harmonizing data without evaluating relevant biological variation;
- overcorrecting center differences that may contain biological signal;
- modifying prospective clinical acquisitions solely for an unapproved technical experiment;
- presenting professional observations as formal evidence or universal clinical guidance.

## Lessons Learned

1. Images from different centers should not automatically be treated as equivalent.
2. Resampling can standardize spatial representation but cannot recover lost anatomical information.
3. Standardization does not guarantee equivalence.
4. Thicker reconstructions may increase partial-volume effects and reduce spatial detail.
5. Preprocessing must be driven by the scientific question.
6. Technical diversity can improve the evaluation of generalization when properly controlled.
7. AI may learn scanner or hospital differences instead of disease biology.
8. Metadata are essential for identifying potential confounding.
9. Harmonization should reduce unwanted technical variability while preserving biological information.
10. Overcorrection can remove meaningful biological signal.
11. Clinical imaging experience can help identify sources of technical variability, but observations must still be tested scientifically.

Additional conclusions from this lesson include:

- Ground Truth and segmentation quality are influenced by the source image and its reconstruction.
- Feature extraction at scale does not establish feature reliability.
- Multicenter diversity and external testing are valuable only when methods and differences remain traceable.
- Consistent imaging parameters support spatial reference during repeated image-guided workflows.
- Not every visual difference represents biological change.

## Future Learning Directions

- Study DICOM metadata extraction and data-governance requirements.
- Compare interpolation methods for continuous images and discrete masks.
- Study modality-appropriate image normalization.
- Examine phantom studies as a future method for controlled technical investigation.
- Investigate radiomic feature stability and appropriate reliability measures such as ICC.
- Study ComBat, batch effects, and statistical confounder control without assuming universal suitability.
- Introduce domain shift and domain adaptation after the required AI foundations are established.
- Study external validation and leave-one-center-out validation conceptually and practically in later stages.
- Explore multicenter AI only with appropriate metadata, governance, and validation design.
- Evaluate harmonization methods for both reduction of technical variation and preservation of biological signal.
- Make no claim of proficiency in these methods until future study and evidence support it.

