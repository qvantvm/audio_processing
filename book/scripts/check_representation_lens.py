#!/usr/bin/env python3
"""Verify representation-lens sections exist in teaching chapters.

Ch 01 uses a comparison matrix instead of the lens table; ch 00 and appendix are exempt.
Run from repo root: python book/scripts/check_representation_lens.py
"""

from __future__ import annotations

import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
CHAPTERS = BOOK / "chapters"

EXEMPT = {
    "00-preface.md",
    "01-what-is-audio-signal-processing.md",
    "23-appendix-exercise-solutions.md",
}

REQUIRED_MARKER = "## Representation lens"


def main() -> int:
    failures: list[str] = []
    for path in sorted(CHAPTERS.glob("*.md")):
        if path.name in EXEMPT:
            continue
        text = path.read_text(encoding="utf-8")
        if REQUIRED_MARKER not in text:
            failures.append(f"{path.name}: missing '{REQUIRED_MARKER}' section")

    if failures:
        print("Representation lens check FAILED:")
        for msg in failures:
            print(f"  - {msg}")
        return 1

    print("Representation lens check OK (ch 02–22)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
