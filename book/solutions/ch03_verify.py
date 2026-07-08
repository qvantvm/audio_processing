#!/usr/bin/env python3
"""Verified numeric answers for Chapter 03 exercises."""

from __future__ import annotations

import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))


def main() -> int:
    # 3.1
    fs = 22050
    f_true = 12000
    assert fs - f_true == 10050
    # 3.2
    samples_per_sec = 44100 * 2
    bytes_per_sec = samples_per_sec * 2
    assert samples_per_sec == 88200
    assert bytes_per_sec == 176400
    # 3.3
    b = 16
    delta = 2 / (2**b)
    assert abs(delta - 1 / 32768) < 1e-15
    # 3.4 — no aliasing when f < fs/2
    assert 1500 < 4000 / 2
    print("Chapter 03 solutions: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
