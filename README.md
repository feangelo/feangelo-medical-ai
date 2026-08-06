# Felipe Angelo Medical AI Lab

**FAMAI Lab** — Medical Imaging, 3D Segmentation, Radiomics and AI Engineering Portfolio

> This project is in active development. Its current purpose is to document a transparent, reproducible learning path and establish the engineering foundation for future public work.

[Português](README.pt-BR.md) · [Vision](VISION.md) · [Roadmap](ROADMAP.md) · [Documentation](docs/index.md)

## About

My name is Felipe Angelo. I am a Biomedical Scientist with experience working with CT and MRI imaging. I am developing skills in medical image segmentation, quantitative imaging, radiomics, medical AI, and digital twins.

FAMAI Lab is a long-term public portfolio and technical laboratory. It will be used to document learning, build reproducible workflows, and publish carefully reviewed projects based only on synthetic, public, or appropriately licensed open datasets.

This repository does not contain clinical claims, diagnostic software, or private patient data.

## Current status

The repository foundation is **In Progress**. Case studies, pipelines, validation results, publications, and deployed applications remain planned until evidence is available. See the [roadmap](ROADMAP.md) for the authoritative status.

## Focus areas

- Medical image segmentation with an initial focus on CT and MRI
- Quantitative imaging and reproducible measurements
- Radiomics methodology and feature reproducibility
- Python engineering for medical imaging workflows
- Medical AI fundamentals and model evaluation
- 3D models, centerlines, visualization, and digital twins
- Privacy-conscious scientific communication

## Planned technology ecosystem

The architecture is designed for future integration with 3D Slicer, SimpleITK, ITK, VTK, PyRadiomics, MONAI, nnU-Net, TotalSegmentator, Open3D, Blender, Jupyter, MkDocs, and GitHub Pages. These integrations are planned; their presence here does not imply implementation or validation.

## Repository structure

| Path | Purpose |
|---|---|
| `.github/` | Continuous integration, templates, and repository automation. |
| `assets/` | Public visual assets that are safe to distribute. |
| `career/` | Evidence-based career materials and competency mapping. |
| `cases/` | Public, synthetic, or open-dataset case studies. |
| `configs/` | Shared, non-secret configuration files. |
| `content/` | Drafts for public educational and portfolio content. |
| `docs/` | Technical documentation and future MkDocs website. |
| `learning/` | Structured learning records and exercises. |
| `notebooks/` | Reproducible notebooks without private data. |
| `publications/` | Publication records and manuscripts when available. |
| `reports/` | Cross-project public reports. |
| `scripts/` | Safe command-line utilities and maintenance scripts. |
| `src/medical_ai_lab/` | Reusable Python package source. |
| `tests/` | Automated tests and validation fixtures. |
| `tools/` | Lightweight developer tooling and documented integrations. |

## Data policy

Private clinical DICOM, identifiable images, protected health information, credentials, and re-identification keys are prohibited. Every case must declare one of these classifications in `case.yaml`:

- `synthetic`
- `open-dataset`
- `public`

`open-dataset` and `public` cases must document provenance, license, and usage restrictions. Repository safeguards reduce risk but do not replace a manual privacy review before every commit and publication. See the [data governance policy](docs/data-governance.md).

## Getting started

The project targets Python 3.12. No medical-imaging or deep-learning dependencies are configured in Phase 1.

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev,docs]"
pytest
ruff check .
```

Installation is optional during the foundation phase. The commands describe the intended future developer setup.

## Cases

No portfolio case has been published yet. `cases/Case_Template/` defines the governance and documentation requirements for future work.

## Learning Journey

The learning journey records concepts, questions, limitations, and next steps without presenting study activity as validated expertise. Progress is also summarized in [LEARNING_LOG.md](LEARNING_LOG.md).

### 3D Slicer

| Lesson | Topic | Status |
|---|---|---|
| [Lesson 03](learning/3d-slicer/lesson-03-segmentation-pipeline.md) | Segmentation Pipeline: Threshold, Islands, Logical Operators, Margin, and Smoothing | Learning record |

Future lesson files can be prepared safely from the [lesson template](learning/3d-slicer/TEMPLATE.md):

```bash
python scripts/create_lesson.py --number 4 --title "Lesson title" --dry-run
python scripts/create_lesson.py --number 4 --title "Lesson title"
```

The first command previews the destination. The second creates it only when no file already exists. Projects and results will be added only after implementation, review, and supporting evidence exist.

## Roadmap

Work is tracked using four states: `Planned`, `In Progress`, `Validated`, and `Published`. A feature is never marked as validated or published without documented evidence.

## Contributing

The laboratory is currently a personal portfolio, but constructive issues and future contributions are welcome under [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md).

## Security and responsible use

Do not report sensitive medical data in a public issue. Follow [SECURITY.md](SECURITY.md) for responsible disclosure. Nothing in this repository is intended for diagnosis, treatment decisions, or clinical deployment without appropriate validation and regulatory review.

## Contact

Professional contact links will be added after Felipe has reviewed and approved the public profiles to be listed. No contact details are inferred or published automatically.

## License

Code and original documentation are released under the [MIT License](LICENSE), unless a file states otherwise. Third-party datasets and assets retain their own licenses. The MIT License does not grant rights to clinical data or third-party content.
