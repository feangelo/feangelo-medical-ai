"""Foundation-level package tests."""

from medical_ai_lab import __version__


def test_package_version() -> None:
    """The package exposes the initial semantic version."""
    assert __version__ == "0.1.0"

