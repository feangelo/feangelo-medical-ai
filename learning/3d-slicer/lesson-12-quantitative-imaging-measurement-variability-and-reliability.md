# Lesson 12 – Quantitative Imaging, Measurement Variability and Reliability

**Learning path:** 3D Slicer  
**Date:** 2026-08-16  
**Status:** Learning record  
**Scope:** Scientific learning documentation; no clinical data or patient-specific conclusions

## Objectives

- Understand that converting a medical image into numbers does not guarantee that those numbers represent biological differences.
- Connect acquisition, reconstruction, geometry, preprocessing, segmentation, observer or method, measurement, and interpretation.
- Recognize potential confounding in multicenter quantitative imaging.
- Introduce batch effects, domain shift, and shortcut learning conceptually.
- Distinguish within-center from pooled multicenter associations.
- Understand why the same patient and lesion may produce different measurements under different imaging conditions.
- Distinguish repeatability from reproducibility conceptually.
- Introduce feature robustness and scientifically valuable negative robustness results.
- Distinguish relative consistency from absolute agreement.
- Introduce the Intraclass Correlation Coefficient (ICC) as a family of reliability coefficients without studying its models or formulas.
- Separate possible biological change from technical and measurement variability.
- Introduce test-retest experiments and organize sources of imaging-measurement variability.
- Interpret a feature change relative to that feature's expected variability.
- Introduce the Coefficient of Variation (CV) and its basic calculation.
- Continue scientific English development without claiming language proficiency.

## Scientific Background

### From medical image to quantitative data

The central reasoning chain developed during this lesson was:

```text
patient
    ↓
acquisition
    ↓
reconstruction
    ↓
image geometry
    ↓
preprocessing
    ↓
segmentation
    ↓
observer / method
    ↓
quantitative measurement
    ↓
scientific interpretation
```

> A successful computation or measurement does not automatically imply a scientifically valid biological conclusion.

Consider this conceptual example:

```text
Patient A
Lesion volume = 10 cm³
Mean HU      = 45

Patient B
Lesion volume = 10 cm³
Mean HU      = 45
```

Equal volume and mean attenuation do not establish that two lesions are biologically equivalent. They may differ in disease type, treatment status, morphology, patient condition, respiration, movement, acquisition parameters, reconstruction, scanner, institution, preprocessing, segmentation method, or observer. Benign and malignant disease were discussed only as possible differing contexts, not as classifications derived from these measurements.

Volume and mean HU represent only part of the available information. A quantitative value must be interpreted in relation to how it was produced and the scientific question it is intended to address. No patients, lesions, or datasets were analyzed during this lesson; all numerical scenarios are educational examples.

### Multicenter imaging and confounding

In a conceptual comparison of Hospital A and Hospital B, an imaging feature appeared strongly associated with survival when data from both centers were combined. Before interpreting the feature as a marker of biology or prognosis, the discussion considered whether the centers could differ in:

- patient populations;
- tumor size or aggressiveness;
- treatment patterns;
- scanner characteristics;
- acquisition and reconstruction protocols.

**Confounding** occurs conceptually when an additional factor is related to both the measured feature and the outcome, making interpretation of their apparent relationship difficult. **Batch effects** are systematic differences associated with groups or processing batches, such as centers, scanners, or protocols. **Domain shift** describes a change in data distribution between development and target conditions. **Shortcut learning** describes a model using an easier but scientifically unintended signal instead of the intended biological information.

These concepts were introduced at a foundation level. No confounding analysis, batch correction, model training, or survival study was performed.

### Within-center analysis

If a feature shows a strong association when Hospitals A and B are pooled but loses that association when each hospital is analyzed separately, this is a warning sign. A center-related characteristic may be influencing the pooled result.

This pattern does not automatically prove causality or identify the responsible factor. It motivates examination of population, treatment, acquisition, reconstruction, annotation, processing, and other center-specific differences.

### Same patient, different scanners

The same patient and the same lesion do not automatically guarantee comparable measurements across scanners or institutions. Relevant considerations include:

- acquisition parameters and actual protocol execution;
- reconstruction method and kernel;
- slice thickness;
- contrast phase and timing;
- artifacts and motion;
- respiratory state and positioning;
- segmentation method and observer;
- preprocessing.

A comparison of 1 mm and 5 mm slice thickness was discussed conceptually. Thickness differences can influence partial-volume effects, lesion-boundary representation, apparent volume, intensity measurements, and texture or radiomic features. This is not evidence that every measurement will change by a specific amount; the effect depends on the data, structure, feature, and pipeline.

### Repeatability and reproducibility

**Repeatability** concerns measurement consistency under very similar conditions. A conceptual example is the same scanner, same protocol, short interval, and same lesion.

**Reproducibility** concerns consistency when relevant conditions vary, potentially including scanner, institution, protocol, or observer, depending on the experimental design.

The exact meaning of “same” and “different” conditions must be defined by the study. These terms are not interchangeable, and their interpretation depends on the measurement procedure and research question.

### Feature robustness

In an educational exercise, Feature X produced similar values on Scanner A and Scanner B, while Feature Y produced large differences. Feature X might be more suitable for some multicenter uses, but only if the experiment validly represents the intended conditions and controls relevant sources of variation.

Instability does not necessarily mean that an experiment failed. A valid conclusion may be:

> The feature is not reproducible under the tested conditions.

> A negative robustness result can still be a valuable scientific result.

Such a result can prevent inappropriate use of a feature and guide future methodology. No feature extraction or scanner comparison was performed during this lesson.

### Relative consistency and absolute agreement

Consider the illustrative values:

```text
Scanner A: 0.20, 0.40, 0.60, 0.80
Scanner B: 0.40, 0.80, 1.20, 1.60
```

The patient ordering is preserved, but the absolute values do not agree: Scanner B gives approximately twice the Scanner A values. This introduces the distinction between **relative consistency**, in which ranking is preserved, and **absolute agreement**, in which measurements are sufficiently close in value.

The scale analogy discussed during the lesson is similar: two scales may rank people in the same order while one consistently reports twice the value. Ranking alone does not make the values interchangeable.

This matters for a hypothetical decision rule:

```text
Feature X > 0.60 → high risk

Same patient:
Scanner A = 0.50
Scanner B = 1.00
```

The same cutoff would produce different classifications. This is an educational measurement example, not a validated risk model or clinical threshold. A feature may preserve ranking while failing to support interchangeable absolute values across scanners.

### Intraclass Correlation Coefficient: introduction only

The **Intraclass Correlation Coefficient (ICC)** was introduced as a family of coefficients used to study reliability or agreement of quantitative measurements. ICC is not one universal calculation with one universal interpretation.

Future study will need to distinguish agreement from consistency, single from average measurements, and different ICC designs or models. Formulas, model selection, assumptions, and interpretation were not studied in this lesson, and no ICC was calculated.

### Measurement variability and biological change

Conceptually:

```text
observed change
    =
possible biological change
    +
measurement / technical variability
```

In one hypothetical example, tumor volume changed from `10.0 cm³` to `10.5 cm³`, a `+5%` difference. If expected method variability is approximately `±10%`, this result alone cannot establish real biological growth.

In a second example, volume changed from `10.0 cm³` to `14.0 cm³`, a `+40%` difference. This is much larger than the illustrative `10%` variability and therefore provides stronger evidence that a real change may have occurred. However, the complete pipeline still requires review. A large change does not eliminate the need for quality control, and imaging measurement alone does not establish a clinical conclusion.

All values are hypothetical. They were not derived from patient data or an implemented measurement study.

### Test-retest

A conceptual test-retest experiment included 100 patients with pulmonary nodules:

```text
CT1
    ↓
patient leaves the table
    ↓
repositioning
    ↓
CT2
```

No treatment occurs between the scans. The objective is to estimate how much a measurement can vary when no relevant biological change is expected over that short interval. The number of patients and scenario are illustrative; no study was conducted.

### Sources of measurement variability

Sources discussed during the lesson were organized as follows:

| Category | Examples considered |
|---|---|
| Patient and positioning | Arms up or down, decubitus, head-first or feet-first orientation, centering, clothing, and metal objects |
| Respiration and motion | Inspiration depth, expiration, inadequate breath-hold, and motion |
| Coverage | Correct anatomical coverage and inclusion of the beginning and end of the organ or region |
| Acquisition | kVp, mAs, pitch, slice thickness, FOV, dose, contrast, and timing |
| Reconstruction | Kernel, reconstruction method, and slice parameters |
| Geometry | Spacing, origin, orientation or direction, resampling, and image-mask correspondence |
| Segmentation | Manual, semi-automatic, and automatic methods |
| Observer | Intra-observer and inter-observer variability |
| Processing | Preprocessing, interpolation, resampling, and quantitative-feature extraction |

“Same protocol” should not be treated only as an assumption. The protocol that was actually executed and the relevant metadata should be verified when required by the scientific question.

### Feature variability and observed change

Consider two educational examples:

```text
Feature A
Test-retest variability ≈ ±3%
Post-treatment change    = 10%

Feature B
Test-retest variability ≈ ±25%
Post-treatment change    = 15%
```

Feature A's observed change is larger relative to its own illustrative variability, making it a more convincing possible signal of real change. Feature B's `15%` change lies within an illustrative variability of approximately `±25%`.

This does not prove that Feature B had no biological change. It means that, under those conditions, the measurement cannot confidently distinguish biological change from measurement variability. No treatment-response analysis or feature experiment was performed.

### Scientific English

Vocabulary introduced or practiced included: quantitative imaging, measurement variability, repeatability, reproducibility, test-retest, agreement, consistency, confounder, batch effect, domain shift, feature robustness, coefficient of variation, mean, standard deviation, biological change, and measurement error.

| Scientific English practiced | PT-BR meaning |
|---|---|
| A quantitative measurement is only useful if we understand its variability. | Uma medida quantitativa só é útil se entendermos sua variabilidade. |
| A change in the measurement does not necessarily represent a biological change. | Uma mudança na medida não representa necessariamente uma mudança biológica. |
| We need to distinguish biological change from measurement variability. | Precisamos distinguir mudança biológica de variabilidade da medição. |
| This feature showed good repeatability in the test-retest experiment. | Esta feature apresentou boa repetibilidade no experimento test-retest. |
| The result may be influenced by acquisition and reconstruction parameters. | O resultado pode ser influenciado pelos parâmetros de aquisição e reconstrução. |
| The same patient can produce different measurements under different imaging conditions. | O mesmo paciente pode produzir medidas diferentes sob diferentes condições de imagem. |
| The coefficient of variation measures variability relative to the mean. | O coeficiente de variação mede a variabilidade em relação à média. |
| Before interpreting the result, we should review the entire imaging pipeline. | Antes de interpretar o resultado, devemos revisar todo o pipeline de imagem. |

These sentences document technical-language practice; they do not imply English-language proficiency or completed experiments.

### Coefficient of Variation: introduction

The **Coefficient of Variation (CV)** expresses standard deviation relative to the mean:

```text
CV = SD / Mean × 100%
```

First conceptual example:

```text
Feature X
Mean = 100
SD   = 5
CV   = 5%

Feature Y
Mean = 10
SD   = 5
CV   = 50%
```

The same absolute standard deviation can represent very different relative variability.

Final example studied:

```text
Feature A
Mean = 200
SD   = 10
CV   = 5%

Feature B
Mean = 20
SD   = 4
CV   = 20%
```

The values `200` and `20` are feature means, not sample sizes. Feature B does not have a higher CV because a “sample is smaller.” Its standard deviation represents a larger proportion of its mean. These calculations are educational examples; no empirical feature distribution was analyzed.

## Practical Workflow

A conceptual reasoning workflow for quantitative imaging is:

```text
Define the scientific question
    ↓
Define the quantitative measurement and intended interpretation
    ↓
Review patient, population, and center context
    ↓
Verify acquisition and reconstruction actually performed
    ↓
Verify image geometry and preprocessing
    ↓
Document segmentation method and observer conditions
    ↓
Define repeatability or reproducibility conditions
    ↓
Estimate measurement variability with an appropriate design
    ↓
Compare observed change with expected variability
    ↓
Investigate center effects and possible confounders
    ↓
Interpret cautiously with limitations
```

The reasoning style developed was:

```text
clinical / imaging observation
    ↓
question
    ↓
hypothesis
    ↓
possible confounders
    ↓
technical verification
    ↓
quantitative analysis
    ↓
cautious interpretation
```

No quantitative extraction, test-retest experiment, ICC analysis, CV analysis of a dataset, radiomics pipeline, or survival model was implemented during this lesson.

## Quality Checklist

- [ ] The scientific question and intended interpretation are defined.
- [ ] The quantitative measurement is defined with units and method.
- [ ] Biological equivalence is not inferred from equal values alone.
- [ ] Patient and population context is considered.
- [ ] Center and scanner effects are considered.
- [ ] The executed acquisition protocol is verified when relevant.
- [ ] Reconstruction parameters are documented.
- [ ] Slice thickness and partial-volume implications are considered.
- [ ] Geometry and image-mask correspondence are checked.
- [ ] Preprocessing and interpolation are documented.
- [ ] Segmentation method and observer conditions are documented.
- [ ] Repeatability and reproducibility are distinguished according to study design.
- [ ] Agreement and consistency are not treated as interchangeable.
- [ ] Potential confounding and batch effects are investigated.
- [ ] Within-center behavior is examined when relevant.
- [ ] Test-retest variability is considered before interpreting change.
- [ ] Feature variability is compared with observed change.
- [ ] Negative robustness results are reported rather than hidden.
- [ ] Large changes still undergo complete pipeline quality control.
- [ ] Scientific conclusions remain within the evidence provided by the measurement design.

## Lessons Learned

1. Quantification does not automatically produce biological truth.
2. Equal volume and mean HU do not establish biological equivalence.
3. Every quantitative value depends on an imaging and measurement pipeline.
4. Multicenter associations can be influenced by center-related differences.
5. Within-center analysis can reveal warning signs hidden by pooled results.
6. The same patient does not guarantee comparable measurements across imaging conditions.
7. Slice thickness can influence boundaries, apparent volume, intensity, and texture features.
8. Repeatability and reproducibility answer different questions and depend on study design.
9. Feature robustness must be evaluated under conditions relevant to intended use.
10. A negative robustness result can still be scientifically valuable.
11. Relative consistency does not guarantee absolute agreement.
12. A preserved ranking does not make scanner values interchangeable for a cutoff.
13. ICC is a family of coefficients whose design and interpretation require further study.
14. Observed change combines possible biological change with technical and measurement variability.
15. Test-retest experiments help characterize variability without intended biological intervention.
16. A change within expected variability cannot confidently demonstrate biological change.
17. This uncertainty does not prove that biological change was absent.
18. A large observed change provides stronger evidence but does not remove the need for QC.
19. CV relates standard deviation to the mean.
20. A feature mean is not a sample size.
21. Cautious interpretation requires reviewing the entire imaging pipeline.

## Future Learning Directions

- Reinforce repeatability, reproducibility, agreement, and consistency through controlled examples.
- Study ICC designs, assumptions, and model selection before calculating or interpreting ICC.
- Design a future test-retest exercise using approved synthetic, public, or open data.
- Practice calculating CV only after defining the measurement, experimental unit, and data provenance.
- Explore feature-robustness experiments without treating instability as an unsuccessful study.
- Study approaches to multicenter confounding and batch effects in later lessons without claiming current mastery.
- Make no claim of quantitative-imaging, radiomics, reliability-statistics, or Medical AI proficiency until implementation and evidence support it.
