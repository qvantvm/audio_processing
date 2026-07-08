#!/usr/bin/env python3
"""Ensure markdown files end with newline and wrap long prose lines."""

from __future__ import annotations

import textwrap
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
WIDTH = 100


def should_wrap(line: str, in_code: bool) -> bool:
    if in_code:
        return False
    s = line.strip()
    if not s:
        return False
    if s.startswith("#") or s.startswith("|") or s.startswith("```"):
        return False
    if s.startswith("!") or s.startswith(">") or s.startswith("- ") or s.startswith("* "):
        return False
    if s.startswith("$$") or s.endswith("$$"):
        return False
    if len(line) <= WIDTH:
        return False
    return True


def process(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    in_code = False
    out: list[str] = []
    changed = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            out.append(line)
            continue
        if should_wrap(line, in_code):
            wrapped = textwrap.fill(line, width=WIDTH)
            if wrapped != line:
                changed = True
            out.append(wrapped)
        else:
            out.append(line)
    new_text = "\n".join(out) + "\n"
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        return True
    return changed


def main() -> None:
    count = 0
    for path in sorted(BOOK.rglob("*.md")):
        if process(path):
            count += 1
            print(f"wrapped {path.relative_to(BOOK.parent)}")
    readme = BOOK.parent / "README.md"
    if readme.exists() and process(readme):
        count += 1
        print("wrapped README.md")
    print(f"done ({count} files updated)")


if __name__ == "__main__":
    main()
