# Work

<p class="page-intro">Public work is added only when its source, method, limitations, and status can be documented. The current portfolio demonstrates repository engineering and scientific learning infrastructure; no medical imaging case study has been published yet.</p>

## Reproducible case standard

**Type:** Repository engineering · **Status:** In progress

The repository contains a governed template for future medical imaging cases. It separates source references, segmentations, models, measurements, statistics, radiomics, reports, and publication material while requiring explicit data classification and privacy review.

The standard currently provides:

- a structured `case.yaml` source of truth;
- privacy and provenance requirements for synthetic, open-dataset, or public data;
- reproducibility and segmentation-quality checklists;
- explicit status boundaries between planned, validated, and published work;
- reserved future-analysis areas that do not imply completed capability.

[Read the case standard](case-standard.md){ .portfolio-button .portfolio-button--small }

**Limitations:** The structure has been designed and documented, but no public case has yet completed the full workflow.

## Learning documentation automation

**Type:** Python tooling · **Status:** Implemented and tested

The `create_lesson.py` command creates consistently named lesson records from the repository template. It supports a non-destructive preview and refuses to overwrite an existing lesson. Focused tests cover title-to-filename conversion, dry-run behavior, creation, and overwrite protection.

This is lightweight documentation automation, not a medical image-processing pipeline.

[Review the development approach](development.md){ .portfolio-button .portfolio-button--small }

## Quality and publication pipeline

**Type:** DevOps and documentation · **Status:** Implemented

GitHub Actions validates Python code, Ruff formatting, tests, and the MkDocs site in strict mode. A separate least-privilege workflow builds the static site and publishes the reviewed artifact to GitHub Pages.

This infrastructure supports traceability and maintenance. It does not validate scientific or clinical performance.

[View the repository](https://github.com/feangelo/feangelo-medical-ai){ .portfolio-button .portfolio-button--small target="_blank" rel="noopener" }

## Future case records

When publishable work becomes available, each case entry will report:

| Scientific record | Required information |
|---|---|
| Problem | Specific technical question and intended use |
| Data | Modality, anatomy, provenance, license, and classification |
| Method | Tools, versions, parameters, corrections, and decisions |
| Result | Measured outputs without unsupported interpretation |
| Validation | Reference standard, quality checks, uncertainty, and metrics |
| Limitations | Data, method, scope, and generalization boundaries |
| Reproducibility | Configuration, code, versions, and repeatable instructions |

No placeholder project is presented as completed work.
