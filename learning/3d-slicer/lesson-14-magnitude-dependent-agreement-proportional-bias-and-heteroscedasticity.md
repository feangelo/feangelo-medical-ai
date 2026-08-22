# Lesson 14 – Magnitude-Dependent Agreement, Proportional Bias and Heteroscedasticity

**Learning path:** 3D Slicer
**Date:** 2026-08-22
**Status:** Learning record
**Scope:** Conceptual learning documentation; no clinical data, implemented experiment, formal statistical test, or patient-specific conclusion

## Objectives

- Continue from the magnitude-dependent interpretation checkpoint established in Lesson 13.
- Compare the relative meaning of the same absolute difference at different measurement magnitudes.
- Distinguish an approximately constant absolute difference from a difference that changes with magnitude.
- Introduce proportional bias as a conceptual and visual pattern, without formal testing.
- Introduce heteroscedasticity as a conceptual and visual pattern, without formal testing.
- Distinguish systematic direction from changing spread across measurement magnitude.
- Recognize that proportional bias and heteroscedasticity may occur separately, together, or not at all.
- Reinforce why small mean bias does not guarantee close individual agreement.
- Interpret global summaries cautiously when variability may depend on measurement magnitude.

## Scientific Background

### Continuity from Lesson 13

Lesson 13 ended with an illustrative method whose Limits of Agreement were `-2 to +2 cm³`.
An absolute disagreement of `2 cm³` represented 40% of a `5 cm³` lesion but only 2% of a
`100 cm³` lesion. The exact starting point for this lesson was therefore:

> The same absolute measurement error can have very different relative importance depending on
> measurement magnitude.

The question was extended to whether the same absolute limit should be accepted automatically
for both small and large lesions. In a new conceptual comparison:

| Lesion volume | Absolute difference | Relative difference |
|---:|---:|---:|
| 10 cm³ | 2 cm³ | 2 / 10 × 100 = 20% |
| 100 cm³ | 2 cm³ | 2 / 100 × 100 = 2% |

The same absolute difference does not necessarily have the same relative importance across
measurement magnitudes. This observation does not define a universal clinical threshold.

### Constant absolute difference and magnitude-related difference

Two educational test-retest patterns were contrasted:

| Test | Retest | Difference | Approximate relative change |
|---:|---:|---:|---:|
| 10 | 11 | +1 | +10% |
| 20 | 22 | +2 | +10% |
| 50 | 55 | +5 | +10% |
| 100 | 110 | +10 | +10% |

Here, the absolute difference increases with measurement magnitude while the relative change
remains approximately constant. This differs from an approximately constant absolute pattern:

```text
10 → 12   = +2
20 → 22   = +2
50 → 52   = +2
100 → 102 = +2
```

These examples were used only to distinguish conceptual patterns. They were not derived from a
dataset or formal analysis.

### Proportional bias: conceptual introduction

Proportional bias was introduced as a possible systematic tendency in which differences change
with measurement magnitude. A simplified pattern was:

```text
small measurement  → small positive difference
medium measurement → larger positive difference
large measurement  → still larger positive difference
```

For example, differences of `+1`, `+2`, `+5`, and `+10` across increasing magnitudes suggest a
directional pattern worth investigating. Isolated numbers are not enough to establish
proportional bias formally, and no regression or hypothesis test was studied or performed.

In a conceptual Bland–Altman view, points that begin near zero and become increasingly positive
as magnitude increases form a ramp-like pattern. The primary concern is a systematic direction
of the differences related to magnitude.

### Heteroscedasticity: conceptual introduction

Heteroscedasticity was introduced as a possible change in the spread or variability of
differences across measurement magnitude:

| Measurement magnitude | Illustrative differences |
|---|---|
| Small | -1, 0, +1 |
| Medium | -5, 0, +5 |
| Large | -20, 0, +20 |

The center can remain approximately near zero while the spread increases. In a conceptual
Bland–Altman view, a narrow spread at small magnitudes that opens progressively above and below
zero at larger magnitudes suggests heteroscedasticity.

Homoscedasticity appeared only as a contrast: an approximately constant spread of differences
across magnitudes. It was not studied in depth.

### Direction versus spread

The central distinction was:

| Pattern | Initial conceptual suspicion |
|---|---|
| Differences move increasingly in one direction as magnitude increases | Proportional bias |
| Differences spread increasingly to both sides as magnitude increases | Heteroscedasticity |

The teaching heuristic was: **direction** suggests proportional bias; **spread** suggests
heteroscedasticity. This is an initial visual distinction, not a statistical decision rule.

The two behaviors are not mutually exclusive. A dataset may potentially show proportional bias,
heteroscedasticity, both, or neither. No formal modeling of these possibilities was introduced.

### Manual and automatic segmentation example

A hypothetical comparison used Method A for manual segmentation and Method B for automatic
segmentation:

| Tumor magnitude | Method A | Method B | Difference B - A |
|---|---:|---:|---:|
| Small | 10 cm³ | 10.5 cm³ | +0.5 cm³ |
| Medium | 50 cm³ | 55 cm³ | +5 cm³ |
| Large | 100 cm³ | 120 cm³ | +20 cm³ |

These three pairs primarily show an increasingly positive direction. The initial conceptual
suspicion is proportional bias, not heteroscedasticity. Investigating heteroscedasticity would
require examining the spread of differences from multiple cases across measurement magnitudes.
The scenario was hypothetical; no segmentation experiment was conducted.

### Why small mean bias is not enough

An illustrative summary was considered:

```text
Bias = +1 cm³
LoA  = -18 to +20 cm³
```

The statement “The bias is small, therefore the method has good agreement” is not supported by
mean bias alone. Positive and negative individual differences may cancel in the average. For
example:

```text
-20, -10, 0, +10, +20
```

These differences have a mean near zero but substantial individual spread. Therefore, mean bias
must be interpreted together with the spread of differences, Limits of Agreement, and behavior
across measurement magnitude.

> A small mean bias can coexist with substantial individual disagreement.

A single global summary may also hide different variability across the measurement range.
Statistical output does not produce an automatic scientific conclusion, and no universal
threshold for “good” or “excellent” agreement was defined.

### Scientific English session status

Scientific terms arose naturally in the technical discussion: proportional bias,
heteroscedasticity, homoscedasticity, measurement magnitude, difference, spread, variability,
agreement, mean bias, Limits of Agreement, manual segmentation, and automatic segmentation.

The incomplete language exercise from this session is not evidence of acquired conversational
competence and is not recorded as completed learning. Future Scientific English practice should
return to contextual professional situations, active translation, learner attempts, contextual
correction, explanation of vocabulary and structure, and deliberate reuse of learned terms.
That is a future pedagogical direction, not scientific content or a language-proficiency claim.

## Practical Workflow

The conceptual learning process followed this progression:

```text
scientific scenario
    ↓
learner reasoning
    ↓
pattern identification
    ↓
correction when necessary
    ↓
comparison with a contrasting pattern
    ↓
repeated conceptual discrimination
    ↓
scientific interpretation
```

A cautious conceptual review of magnitude-dependent agreement is:

```text
State the paired-difference convention
    ↓
Inspect differences across measurement magnitude
    ↓
Ask whether the differences change systematically in direction
    ↓
Ask whether the spread changes with magnitude
    ↓
Distinguish proportional bias from heteroscedasticity conceptually
    ↓
Review mean bias, spread, and Limits of Agreement together
    ↓
State limitations without a formal statistical or clinical conclusion
```

No patient data, dataset, Bland–Altman plot generated from empirical data, regression test,
hypothesis test, transformation, ICC analysis, radiomics analysis, or clinical validation was
performed.

## Quality Checklist

- [ ] Absolute differences are interpreted relative to measurement magnitude.
- [ ] A fixed absolute limit is not treated automatically as equally meaningful at all magnitudes.
- [ ] Constant absolute difference is distinguished from magnitude-related difference.
- [ ] Direction of differences is distinguished from spread of differences.
- [ ] Proportional bias is presented as a conceptual suspicion, not a formally tested finding.
- [ ] Heteroscedasticity is presented as a conceptual suspicion, not a formally tested finding.
- [ ] Homoscedasticity is used only as a brief contrast.
- [ ] Several cases across magnitude are required before reasoning about changing spread.
- [ ] Proportional bias and heteroscedasticity are not treated as mutually exclusive.
- [ ] Mean bias is not interpreted as a complete description of agreement.
- [ ] Small mean bias is not equated automatically with good individual agreement.
- [ ] Spread, Limits of Agreement, and magnitude-dependent behavior are considered together.
- [ ] Hypothetical examples are not presented as real datasets or experiments.
- [ ] No universal clinical threshold or patient-specific conclusion is inferred.
- [ ] No statistical, Bland–Altman, radiomics, or English-language mastery is claimed.

## Lessons Learned

1. The same absolute difference may have different relative importance at different magnitudes.
2. A fixed absolute limit should not be accepted automatically without considering magnitude.
3. Absolute differences can increase while relative change remains approximately constant.
4. A systematic direction across magnitude raises an initial conceptual suspicion of proportional bias.
5. Increasing spread across magnitude raises an initial conceptual suspicion of heteroscedasticity.
6. Direction and spread answer different questions.
7. A ramp-like Bland–Altman pattern differs conceptually from a progressively opening pattern.
8. Homoscedasticity means approximately constant spread here and was used only as a contrast.
9. Proportional bias and heteroscedasticity may potentially coexist.
10. A few directional pairs do not demonstrate changing variability.
11. Positive and negative differences may cancel and produce a small mean bias.
12. Small mean bias does not guarantee close individual agreement.
13. Spread, Limits of Agreement, and behavior across magnitude should accompany mean bias interpretation.
14. A global statistical summary can hide magnitude-dependent structure.
15. Statistical results require scientific interpretation rather than automatic acceptance.

## Future Learning Directions

- Continue only from this lesson's checkpoint in a future lesson, without treating the introduced
  visual patterns as formal statistical findings.
- Practice the concepts later with approved synthetic, public, or open data before making any
  implementation or evidence claim.
- Resume Scientific English through contextual, attempt-first professional practice.
- Do not claim agreement-statistics, Bland–Altman, radiomics, clinical interpretation, or English proficiency without supporting implementation and evidence.
