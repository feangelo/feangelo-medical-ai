# Architecture

## Design goals

The repository favors privacy, traceability, reproducibility, testability, and low maintenance overhead. New tools are introduced only when a real workflow requires them.

## Boundaries

- `src/medical_ai_lab/` contains reusable Python behavior.
- `scripts/` contains thin operational entry points, not duplicated business logic.
- `cases/` contains public-facing case documentation and approved artifacts.
- `configs/` stores non-secret shared settings.
- `notebooks/` supports exploration; reusable logic must move into `src/`.
- `docs/` is the source for the future public website.
- `learning/`, `career/`, and `content/` separate development records, evidence-based career materials, and public communication drafts.

## Data flow for future cases

1. Select an allowed synthetic, open, or public source.
2. Document provenance, license, checksum, and restrictions.
3. Complete privacy and publication review.
4. Process data locally with reproducible configuration.
5. Validate outputs and document limitations.
6. Publish only explicitly approved artifacts.

Large data should live outside Git. The repository should contain metadata, acquisition instructions, checksums, code, and small approved illustrations when licensing permits.

## Versioning

Project releases follow Semantic Versioning. Case artifacts use explicit versions and must not be silently replaced. The changelog records user-visible changes.

