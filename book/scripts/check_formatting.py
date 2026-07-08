#!/usr/bin/env python3
"""Fail if repository text files lose physical line structure.

Guards against single-line corruption that breaks review, diffs, and agents.
Run from repo root: python book/scripts/check_formatting.py
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BOOK = ROOT / "book"

FAILURES: list[str] = []
MAX_PY_LINE = 120
MAX_MD_PROSE_LINE = 320  # allow tables/code; flag extreme prose blobs


def check_requirements(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        FAILURES.append(f"{path}: missing final newline")
    for i, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.strip().startswith("#"):
            continue
        if " " in line.strip() and not line.strip().startswith("-"):
            FAILURES.append(
                f"{path}:{i}: multiple packages on one line — use one requirement per line"
            )


def check_python(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        FAILURES.append(f"{path}: missing final newline")
    lines = text.splitlines()
    if len(lines) < 5 and len(text) > 400:
        FAILURES.append(f"{path}: suspiciously few lines ({len(lines)}) for file size")
    for i, line in enumerate(lines, 1):
        if len(line) > MAX_PY_LINE:
            FAILURES.append(f"{path}:{i}: line length {len(line)} > {MAX_PY_LINE}")


def check_markdown(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        FAILURES.append(f"{path}: missing final newline")
    lines = text.splitlines()
    if len(lines) < 3 and len(text) > 500:
        FAILURES.append(f"{path}: suspiciously few lines ({len(lines)}) for file size")
    in_code = False
    for i, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code or line.strip().startswith("|") or line.strip().startswith(">"):
            continue
        if len(line) > MAX_MD_PROSE_LINE:
            FAILURES.append(
                f"{path}:{i}: prose line length {len(line)} > {MAX_MD_PROSE_LINE} — wrap paragraph"
            )


def main() -> int:
    check_requirements(BOOK / "requirements.txt")
    check_requirements(BOOK / "requirements-dev.txt")

    for path in sorted(BOOK.rglob("*.py")):
        if "__pycache__" in path.parts:
            continue
        check_python(path)

    for path in sorted(BOOK.rglob("*.md")):
        check_markdown(path)

    readme = ROOT / "README.md"
    if readme.exists():
        check_markdown(readme)

    if FAILURES:
        print("Formatting check FAILED:\n")
        for msg in FAILURES:
            print(f"  - {msg}")
        return 1

    print("Formatting structure check OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
