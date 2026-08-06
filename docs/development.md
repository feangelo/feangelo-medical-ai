# Development Guide

## Environment

The project targets Python 3.12. Phase 1 contains no runtime medical-imaging or deep-learning dependencies.

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev,docs]"
```

## Quality checks

```bash
ruff check .
ruff format --check .
pytest
mkdocs build --strict
```

## Conventions

- Use English for code, comments, paths, and technical documentation.
- Keep reusable logic under `src/medical_ai_lab/`.
- Add type hints and focused tests.
- Never overwrite case artifacts silently.
- File operations must support a dry-run mode and log important actions.
- Avoid introducing heavy dependencies without an architecture decision and a demonstrated use case.

## Branch and release policy

The initial local branch is `main`. A remote workflow will be designed only after owner review. Releases will follow Semantic Versioning and must update the changelog.

