#!/usr/bin/env python3
"""Verified numeric answers for Chapter 05 exercises."""

from __future__ import annotations

import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))


def main() -> int:
    t0 = 0.005
    f0 = 1.0 / t0
    assert abs(f0 - 200.0) < 1e-9
    harmonics = [f0, 2 * f0, 3 * f0]
    assert harmonics == [200.0, 400.0, 600.0]
    # vowel formants 700, 1200 at f0=150 -> k nearest
    for target in (700, 1200):
        k = round(target / 150)
        assert k in (5, 8)
    print("Chapter 05 solutions: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
