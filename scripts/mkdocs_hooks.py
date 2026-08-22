"""MkDocs hooks for canonical learning records and page metadata."""

from pathlib import Path

from mkdocs.structure.files import File, Files

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
LESSONS_DIRECTORY = REPOSITORY_ROOT / "learning" / "3d-slicer"

PAGE_DESCRIPTIONS = {
    "index.md": (
        "Felipe Angelo's scientific learning portfolio in medical imaging, 3D segmentation, "
        "quantitative imaging, radiomics foundations, and Medical AI foundations."
    ),
    "about.md": (
        "About Felipe Angelo and FAMAI Lab, a public portfolio documenting a careful technical "
        "progression from medical imaging toward quantitative analysis and Medical AI."
    ),
    "work.md": (
        "Review implemented repository engineering, learning documentation, and quality "
        "infrastructure in the FAMAI Lab medical imaging portfolio."
    ),
    "learning.md": (
        "Explore FAMAI Lab learning records in 3D Slicer, segmentation, image geometry, "
        "quantitative imaging, agreement, and scientific validation."
    ),
    "research-notes.md": (
        "Scientific engineering notes from FAMAI Lab on medical image geometry, validation, "
        "measurement, reproducibility, and responsible interpretation."
    ),
    "vision.md": "The evidence-led vision and development boundaries of the FAMAI Lab portfolio.",
    "roadmap.md": "The staged, evidence-based development roadmap for the FAMAI Lab portfolio.",
    "architecture.md": (
        "Repository architecture for reproducible, privacy-conscious medical imaging work in "
        "the FAMAI Lab portfolio."
    ),
    "data-governance.md": (
        "Data governance, privacy, provenance, and publication rules for FAMAI Lab work."
    ),
    "case-standard.md": (
        "The reproducible case structure and scientific evidence requirements used by FAMAI Lab."
    ),
    "development.md": (
        "Development environment, quality checks, and contribution conventions for FAMAI Lab."
    ),
    "wiki/index.md": (
        "A curated technical reference index for the FAMAI Lab medical imaging learning journey."
    ),
}


def on_files(files: Files, config) -> Files:
    """Expose canonical lesson sources as public pages without copying them into docs/."""
    for lesson_path in sorted(LESSONS_DIRECTORY.glob("lesson-*.md")):
        virtual_file = File.generated(
            config,
            f"lessons/{lesson_path.name}",
            content=lesson_path.read_text(encoding="utf-8"),
        )
        files.append(virtual_file)
    return files


def on_page_markdown(markdown: str, page, **kwargs) -> str:
    """Assign a truthful, page-specific description before templates are rendered."""
    description = PAGE_DESCRIPTIONS.get(page.file.src_uri)
    if description is None and page.file.src_uri.startswith("lessons/"):
        description = (
            f"{page.title}, a FAMAI Lab scientific learning record documenting studied concepts, "
            "limitations, quality checks, and future learning directions."
        )
    if description is not None:
        page.meta["description"] = description
    return markdown
