"""Tests for the safe lesson generator."""

import importlib.util
from pathlib import Path

import pytest

SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "create_lesson.py"
SPEC = importlib.util.spec_from_file_location("create_lesson", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
create_lesson = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(create_lesson)


def test_slugify_is_ascii_and_filesystem_safe() -> None:
    """Titles become stable, lowercase ASCII filename components."""
    assert create_lesson.slugify("Segmentação: Tórax & MRI") == "segmentacao-torax-mri"


def test_render_template_replaces_lesson_metadata() -> None:
    """Metadata placeholders are replaced while content prompts remain."""
    rendered = create_lesson.render_template(
        "# Lesson {{LESSON_NUMBER}} — {{LESSON_TITLE}}\n{{LEARNING_PATH}} {{DATE}} {{QUESTION}}",
        lesson_number=4,
        lesson_title="Geometry",
        learning_path="3D Slicer",
        lesson_date="2026-08-06",
    )
    assert rendered == "# Lesson 04 — Geometry\n3D Slicer 2026-08-06 {{QUESTION}}"


def test_dry_run_creates_nothing(tmp_path: Path) -> None:
    """Dry-run mode reports intent without creating the destination."""
    template = tmp_path / "TEMPLATE.md"
    template.write_text("# {{LESSON_NUMBER}} {{LESSON_TITLE}}", encoding="utf-8")
    destination_directory = tmp_path / "lessons"

    result = create_lesson.main(
        [
            "--number",
            "4",
            "--title",
            "Geometry",
            "--template",
            str(template),
            "--directory",
            str(destination_directory),
            "--dry-run",
        ]
    )

    assert result == 0
    assert not destination_directory.exists()


def test_existing_lesson_is_never_overwritten(tmp_path: Path) -> None:
    """An existing lesson causes a parser error and remains unchanged."""
    template = tmp_path / "TEMPLATE.md"
    template.write_text("# {{LESSON_NUMBER}} {{LESSON_TITLE}}", encoding="utf-8")
    destination = tmp_path / "lesson-04-geometry.md"
    destination.write_text("preserve me", encoding="utf-8")

    with pytest.raises(SystemExit):
        create_lesson.main(
            [
                "--number",
                "4",
                "--title",
                "Geometry",
                "--template",
                str(template),
                "--directory",
                str(tmp_path),
            ]
        )

    assert destination.read_text(encoding="utf-8") == "preserve me"

