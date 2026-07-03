"""Implementation quality labels for teaching vs production code."""

from __future__ import annotations

from enum import Enum


class ImplQuality(str, Enum):
    """How to interpret an audio_toolkit symbol in prose and tests."""

    RECOMMENDED = "recommended"  # correct minimal implementation for reuse
    PEDAGOGICAL = "pedagogical"  # simplified for teaching clarity
    ARTIFACT = "artifact"  # intentional flaw for hearing/plotting demos


# Functions that deliberately produce audible numerical artifacts.
ARTIFACT_FUNCTIONS = frozenset(
    {
        "naive_saw",
    }
)
