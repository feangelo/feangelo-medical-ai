# Lesson 13 – Measurement Reliability, Percentage Change and Agreement

**Learning path:** 3D Slicer
**Date:** 2026-08-21
**Status:** Learning record
**Scope:** Conceptual and mathematical learning documentation; no clinical data, implemented experiment, or patient-specific conclusion

## Objectives

- Continue from the Coefficient of Variation checkpoint established in Lesson 12.
- Interpret an observed change relative to the expected variability of its measurement.
- Reinforce that quality control precedes statistical interpretation.
- Calculate percentage change using the initial value as the reference.
- Distinguish absolute difference from relative change.
- Introduce Bland–Altman analysis conceptually through means and paired differences.
- Introduce mean difference, systematic bias, and Limits of Agreement (LoA).
- Recognize that zero mean bias does not guarantee close agreement.
- Separate the amount of disagreement from its acceptability for an intended use.
- Interpret an absolute measurement error in relation to measurement magnitude.
- Consolidate relevant Scientific English without claiming language proficiency.

## Scientific Background

### Continuity from measurement variability

Lesson 12 introduced quantitative imaging, measurement variability, repeatability,
reproducibility, test-retest design, feature robustness, agreement versus consistency,
ICC at an introductory level, possible biological change versus technical variability, and
the Coefficient of Variation. This lesson used those foundations without repeating them.

Consider the following educational scenario:

| Measurement | Illustrative test-retest CV | Post-treatment change |
|---|---:|---:|
| Tumor volume | approximately 4% | -20% |
| Feature X | approximately 8% | -20% |
| Feature Y | approximately 35% | -25% |

The largest percentage change is not automatically the most convincing evidence of change
beyond expected variability. The volume change of approximately 20% is large relative to its
illustrative variability of approximately 4%. By contrast, Feature Y changed by 25%, but its
illustrative variability was approximately 35%.

> The observed change must be interpreted relative to measurement variability.

This comparison does not demonstrate biological response. Its interpretation still depends on
the validity of the complete measurement pipeline. No treatment-response experiment, feature
extraction, or dataset analysis was performed.

### Quality control before statistical interpretation

The reasoning sequence reinforced during the lesson was:

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
feature extraction
    ↓
statistical interpretation
```

Slice thickness, respiratory differences, segmentation differences, preprocessing, and
acquisition or reconstruction inconsistencies may influence a quantitative difference. A large
numerical change does not remove the need to review these sources.

> QC comes before statistical interpretation.

### Percentage change

Percentage change was consolidated before advancing further into agreement analysis:

```text
percentage change = (final value - initial value) / initial value × 100
```

The calculation follows three steps:

1. subtract the initial value from the final value;
2. divide the result by the initial value;
3. multiply by 100.

The initial value is the reference. If the final value is greater than the initial value, the
percentage is positive and represents an increase. If the final value is smaller, the percentage
is negative and represents a decrease.

| Change | Difference | Division by initial value | Percentage change |
|---|---:|---:|---:|
| 20 → 22 cm³ | 22 - 20 = 2 | 2 / 20 = 0.10 | +10% |
| 40 → 50 cm³ | 50 - 40 = 10 | 10 / 40 = 0.25 | +25% |
| 50 → 40 cm³ | 40 - 50 = -10 | -10 / 50 = -0.20 | -20% |
| 80 → 100 cm³ | 100 - 80 = 20 | 20 / 80 = 0.25 | +25% |
| 120 → 90 cm³ | 90 - 120 = -30 | -30 / 120 = -0.25 | -25% |
| 200 → 150 cm³ | 150 - 200 = -50 | -50 / 200 = -0.25 | -25% |
| 60 → 75 cm³ | 75 - 60 = 15 | 15 / 60 = 0.25 | +25% |

The changes `40 → 50` and `50 → 40` have the same absolute difference of 10 units, but
they are not symmetric percentages:

```text
40 → 50: 10 / 40 × 100 = +25%
50 → 40: -10 / 50 × 100 = -20%
```

> The same absolute difference can represent different percentage changes depending on the
> initial value.

### Absolute and relative difference

The following examples separate absolute difference from relative change:

| Change | Absolute difference | Relative change |
|---|---:|---:|
| 10 → 11 | 1 | 10% |
| 50 → 55 | 5 | 10% |
| 100 → 110 | 10 | 10% |

The absolute difference increases with measurement magnitude while the relative change remains
constant. This distinction prepared the introduction to agreement analysis.

### Bland–Altman: conceptual introduction

Bland–Altman analysis was introduced through the question:

> When the same quantity is measured twice or by two methods, how much do the measurements
> disagree?

For each measurement pair, the mean is placed conceptually on the horizontal axis and the
difference on the vertical axis. The convention used in the exercises was `Retest - Test`.

```text
Test = 10
Retest = 12

Mean       = (10 + 12) / 2 = 11
Difference = 12 - 10 = +2

Bland–Altman point = (11, +2)
```

The complete educational example was:

| Patient | Test | Retest | Mean | Difference |
|---|---:|---:|---:|---:|
| A | 10 | 12 | 11 | +2 |
| B | 20 | 22 | 21 | +2 |
| C | 30 | 32 | 31 | +2 |
| D | 40 | 42 | 41 | +2 |

The differences are always `+2`, so the mean difference, or bias, is `+2`. In this conceptual
example, the retest systematically produces values two units above the test:

> The retest systematically overestimates the measurement by two units.

This introduces **bias**, **systematic bias**, and **mean difference** without presenting
Bland–Altman analysis as mastered or implemented.

### Zero mean bias and dispersion

In a second scenario, the differences were:

```text
+1, -2, +2, -1
```

Their mean is zero because positive and negative differences cancel. Individual measurements
still disagree, so bias near zero does not establish perfect agreement.

| Method | Differences | Mean bias |
|---|---|---:|
| A | +1, -1, +1, -1 | 0 |
| B | +20, -20, +20, -20 | 0 |

Method B has much wider differences even though both methods have zero mean bias.

> Mean bias alone is insufficient to characterize agreement.

### Statistical agreement and acceptability

Two questions were distinguished:

1. How much do the measurements disagree?
2. Is that disagreement acceptable for the intended scientific or clinical use?

Acceptability depends on the scientific question, measurement magnitude, intended purpose, and
previously justified limits. No universal clinical threshold was defined, and no clinical
decision was made.

> A statistically reliable measurement is not automatically a clinically meaningful
> measurement.

### Limits of Agreement: introduction only

Limits of Agreement were introduced conceptually with the classical approximation:

```text
Upper LoA ≈ bias + 1.96 × SD of differences
Lower LoA ≈ bias - 1.96 × SD of differences
```

Under appropriate assumptions, LoA describe an approximate range in which most paired
differences are expected to occur. The value `1.96`, normal distributions, confidence intervals,
and statistical inference were not studied in depth.

| Method | Bias | Limits of Agreement |
|---|---:|---:|
| A | 0 | -2 to +2 |
| B | 0 | -20 to +20 |

Although both methods have zero bias, Method B has a much wider range of disagreement. Bias alone
does not describe agreement.

### Magnitude-dependent interpretation

The final concept studied was an illustrative volume method with `LoA = -2 to +2 cm³`:

| Lesion volume | Absolute disagreement considered | Relative importance |
|---:|---:|---:|
| 5 cm³ | 2 cm³ | 2 / 5 × 100 = 40% |
| 100 cm³ | 2 cm³ | 2 / 100 × 100 = 2% |

The same possible absolute disagreement has very different relative importance for the two
measurement magnitudes.

> The measurement error must be interpreted in relation to the magnitude of the measurement.

This magnitude-dependent interpretation is the exact endpoint of the lesson.

### Scientific English

Vocabulary introduced or practiced included: measurement, measurement variability, measurement
error, initial value, final value, percentage change, increase, decrease, absolute difference,
relative difference, mean, difference, agreement, bias, systematic bias, mean difference, Limits
of Agreement, overestimate, underestimate, magnitude, reliability, test, and retest.

| Scientific English reviewed | PT-BR meaning |
|---|---|
| The observed change must be interpreted relative to measurement variability. | A mudança observada deve ser interpretada em relação à variabilidade da medição. |
| A statistically reliable measurement is not automatically a clinically meaningful measurement. | Uma medida estatisticamente confiável não é automaticamente uma medida clinicamente significativa. |
| The retest systematically overestimates the measurement by two units. | O reteste superestima sistematicamente a medida em duas unidades. |
| The same absolute difference can represent different percentage changes depending on the initial value. | A mesma diferença absoluta pode representar mudanças percentuais diferentes dependendo do valor inicial. |
| The measurement error must be interpreted in relation to the magnitude of the measurement. | O erro de medição deve ser interpretado em relação à magnitude da medida. |
| The tumor volume increased by 25%. | O volume tumoral aumentou 25%. |
| The tumor volume decreased by 25%. | O volume tumoral diminuiu 25%. |

These correct sentences are revision material, not evidence of English fluency. Future interactive
practice should introduce vocabulary and structure progressively, request the learner's attempt
before providing a complete answer, correct that attempt, and then repeat the practice.

## Practical Workflow

The learning process followed this progression:

```text
problem
    ↓
learner reasoning
    ↓
correction
    ↓
simpler example when necessary
    ↓
mathematical foundation
    ↓
medical imaging interpretation
    ↓
scientific concept
```

A cautious conceptual workflow for interpreting paired quantitative measurements is:

```text
Define the measurement and intended use
    ↓
Review the complete imaging pipeline and QC
    ↓
Calculate change relative to the initial value
    ↓
Compare observed change with expected variability
    ↓
For paired measurements, calculate each mean and difference
    ↓
Examine mean difference and spread conceptually
    ↓
Interpret disagreement relative to measurement magnitude and intended use
    ↓
State limitations without claiming biological or clinical conclusions
```

No patient data, dataset, Bland–Altman plot, statistical software, LoA calculation from empirical
data, ICC analysis, radiomics experiment, or clinical validation was performed.

## Quality Checklist

- [ ] The initial value is used as the denominator for percentage change.
- [ ] Positive and negative changes are labeled as increase and decrease correctly.
- [ ] Absolute difference is distinguished from relative change.
- [ ] Observed change is compared with the measurement's expected variability.
- [ ] The complete imaging and measurement pipeline is reviewed before interpretation.
- [ ] QC is not bypassed because a numerical change appears large.
- [ ] The paired-difference convention is stated and applied consistently.
- [ ] Mean difference is not treated as a complete description of agreement.
- [ ] Zero mean bias is not interpreted automatically as perfect agreement.
- [ ] Limits of Agreement are presented as an introduction under appropriate assumptions.
- [ ] Statistical disagreement is separated from acceptability for an intended use.
- [ ] Absolute error is interpreted in relation to measurement magnitude.
- [ ] Educational examples are not presented as patient data or experimental results.
- [ ] No universal clinical threshold or biological response is inferred.
- [ ] Bland–Altman, ICC, radiomics, and statistical proficiency are not claimed.

## Lessons Learned

1. Observed change must be interpreted relative to expected measurement variability.
2. The largest percentage change is not automatically the strongest evidence of change beyond variability.
3. Quality control precedes statistical interpretation.
4. Percentage change uses the initial value as its reference.
5. The same absolute difference can produce asymmetric percentage changes in opposite directions.
6. Different absolute differences can represent the same relative change.
7. A Bland–Altman point uses the pair mean and paired difference.
8. A consistent nonzero mean difference can indicate systematic bias.
9. Positive and negative errors may cancel and produce zero mean bias.
10. Zero mean bias does not guarantee close agreement.
11. Mean bias alone is insufficient to characterize agreement.
12. Limits of Agreement describe the spread of disagreement conceptually, under appropriate assumptions.
13. Statistical disagreement and acceptability for an intended use are different questions.
14. The same absolute measurement error can have different relative importance at different magnitudes.
15. Percentage change was consolidated before advancing further into agreement analysis.

## Future Learning Directions

- Study proportional bias formally only in a future lesson.
- Study logarithmic transformation and percentage Bland–Altman methods later.
- Examine Bland–Altman assumptions, confidence intervals, and the role of `1.96` in depth later.
- Continue ICC study with models, designs, and assumptions before any implementation claim.
- Practice agreement analysis later with approved synthetic, public, or open data.
- Continue interactive Scientific English practice by eliciting an attempt before correction.
- Do not claim reliability-statistics, Bland–Altman, radiomics, or clinical interpretation proficiency until implementation and evidence support it.
