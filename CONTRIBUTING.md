# Contributing

Thank you for considering a contribution to FAMAI Lab. The project is currently a personal learning and portfolio laboratory, so contribution scope may remain limited while its foundations are established.

## Before contributing

1. Open an issue describing the problem or proposal.
2. Do not attach clinical data, DICOM files, identifiable images, credentials, or restricted datasets.
3. Confirm that any sample data are synthetic, public, or from an open dataset with documented permission.
4. Keep claims proportional to available evidence.

## Development principles

- Target Python 3.12.
- Use English for code, comments, filenames, and technical documentation.
- Add tests for behavior changes.
- Use type hints for public interfaces.
- Keep functions focused and avoid unnecessary dependencies.
- Run `ruff check .`, `ruff format --check .`, and `pytest` before submitting work.
- Update documentation and the changelog when behavior changes.

## Case contributions

Every case must use the case template, provide `case.yaml`, declare an allowed data classification, document provenance and licensing, and complete the privacy checklist. A valid classification does not by itself make data safe to publish.

## Pull requests

Describe the change, motivation, tests, privacy impact, limitations, and related issue. Maintainers may request removal of files that create privacy, licensing, scientific-validity, or maintainability risks.

