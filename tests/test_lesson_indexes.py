"""Keep every public lesson index synchronized with canonical lesson files."""

from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
LESSONS_DIRECTORY = REPOSITORY_ROOT / "learning" / "3d-slicer"
INDEX_FILES = (
    REPOSITORY_ROOT / "README.md",
    REPOSITORY_ROOT / "learning" / "README.md",
    REPOSITORY_ROOT / "docs" / "learning.md",
    REPOSITORY_ROOT / "mkdocs.yml",
)


def test_every_lesson_is_listed_in_every_public_index() -> None:
    """A new canonical lesson must be discoverable from every maintained lesson index."""
    lesson_filenames = sorted(path.name for path in LESSONS_DIRECTORY.glob("lesson-*.md"))

    assert lesson_filenames, "No canonical lesson files were found."

    for index_path in INDEX_FILES:
        index_text = index_path.read_text(encoding="utf-8")
        missing = [filename for filename in lesson_filenames if filename not in index_text]
        assert not missing, f"{index_path.relative_to(REPOSITORY_ROOT)} is missing: {missing}"
