#!/usr/bin/env python3
"""Create a learning record from a Markdown template without overwriting files."""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEMPLATE = REPOSITORY_ROOT / "learning" / "3d-slicer" / "TEMPLATE.md"


def slugify(value: str) -> str:
    """Return a conservative ASCII slug for a public filename."""
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii").lower()
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_text).strip("-")
    if not slug:
        raise ValueError("The title must contain at least one letter or number.")
    return slug


def render_template(
    template_text: str,
    *,
    lesson_number: int,
    lesson_title: str,
    learning_path: str,
    lesson_date: str,
) -> str:
    """Replace lesson-level placeholders while preserving content prompts."""
    replacements = {
        "{{LESSON_NUMBER}}": f"{lesson_number:02d}",
        "{{LESSON_TITLE}}": lesson_title.strip(),
        "{{LEARNING_PATH}}": learning_path.strip(),
        "{{DATE}}": lesson_date,
    }
    rendered = template_text
    for placeholder, value in replacements.items():
        rendered = rendered.replace(placeholder, value)
    return rendered


def parse_iso_date(value: str) -> str:
    """Validate an ISO 8601 calendar date and return it unchanged."""
    return date.fromisoformat(value).isoformat()


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""
    parser = argparse.ArgumentParser(
        description="Create a new learning lesson from TEMPLATE.md.",
    )
    parser.add_argument("--number", type=int, required=True, help="Positive lesson number")
    parser.add_argument("--title", required=True, help="Public lesson title")
    parser.add_argument(
        "--learning-path",
        default="3D Slicer",
        help="Learning path displayed in the document",
    )
    parser.add_argument(
        "--date",
        default=date.today().isoformat(),
        type=parse_iso_date,
        help="Lesson date in YYYY-MM-DD format",
    )
    parser.add_argument(
        "--directory",
        type=Path,
        default=DEFAULT_TEMPLATE.parent,
        help="Destination directory; defaults to learning/3d-slicer",
    )
    parser.add_argument(
        "--template",
        type=Path,
        default=DEFAULT_TEMPLATE,
        help="Template path; defaults to learning/3d-slicer/TEMPLATE.md",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report the intended operation without creating a file",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the safe lesson-generation workflow."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.number < 1:
        parser.error("--number must be a positive integer")

    template = args.template.expanduser().resolve()
    destination_directory = args.directory.expanduser().resolve()
    destination = destination_directory / f"lesson-{args.number:02d}-{slugify(args.title)}.md"

    if not template.is_file():
        parser.error(f"template not found: {template}")
    if destination.exists():
        parser.error(f"destination already exists; no file was changed: {destination}")

    rendered = render_template(
        template.read_text(encoding="utf-8"),
        lesson_number=args.number,
        lesson_title=args.title,
        learning_path=args.learning_path,
        lesson_date=args.date,
    )

    operation = "DRY RUN" if args.dry_run else "CREATE"
    print(f"[{operation}] template: {template}")
    print(f"[{operation}] destination: {destination}")

    if args.dry_run:
        print("[DRY RUN] no directory or file was created")
        return 0

    destination_directory.mkdir(parents=True, exist_ok=True)
    destination.write_text(rendered, encoding="utf-8", newline="\n")
    print("[CREATE] lesson created successfully")
    return 0


if __name__ == "__main__":
    sys.exit(main())
