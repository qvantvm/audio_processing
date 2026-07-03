#!/usr/bin/env python3
"""Verify pedagogically reviewed chapters have exercise verify scripts.

Parses `BOOK_PLAN.md` status table; chapters marked pedagogically reviewed must have
`solutions/chNN_verify.py`. Run from repo root.
"""

from __future__ import annotations

import re
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
PLAN = BOOK / "BOOK_PLAN.md"
SOLUTIONS = BOOK / "solutions"

ROW = re.compile(
    r"^\|\s*(\d{2}|A)\s*\|\s*`[^`]+`\s*\|\s*[^|]+\|\s*pedagogically reviewed\s*\|",
    re.MULTILINE,
)


def main() -> int:
    text = PLAN.read_text(encoding="utf-8")
    chapters = [m.group(1) for m in ROW.finditer(text)]
    failures: list[str] = []
    for ch in chapters:
        if ch == "A":
            continue
        script = SOLUTIONS / f"ch{ch}_verify.py"
        if not script.is_file():
            failures.append(f"ch {ch}: missing {script.name}")

    if failures:
        print("Pedagogy verify coverage FAILED:")
        for msg in failures:
            print(f"  - {msg}")
        return 1

    print(f"Pedagogy verify coverage OK ({len(chapters)} pedagogically reviewed chapters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
