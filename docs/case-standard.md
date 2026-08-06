# Case Standard

## Naming

Future case directories use `CaseNNN_MODALITY_Anatomy`, for example `Case001_CT_Thorax`. The number is unique and three digits. Names contain no patient or institutional identifiers.

## Required metadata

`case.yaml` is the structured source of truth. It records identity, status, data classification, modality, anatomy, provenance, license, privacy review, tools, outputs, and limitations.

## Required documentation

- `README.md` explains objective, methods, results, metrics, limitations, and next steps.
- `CHECKLIST.md` documents governance, processing, quality control, and publication review.
- Evidence must support any transition from Planned to Validated or Published.

## Artifact policy

Large and sensitive artifacts remain outside Git by default. Each published file needs a purpose, documented origin, license compatibility, and privacy review. Derived screenshots and models require the same scrutiny as source data.

