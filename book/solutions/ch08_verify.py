#!/usr/bin/env python3
"""Verified numeric answers for Chapter 08 exercises."""

from __future__ import annotations

import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))


def main() -> int:
    m, r, fs = 2048, 512, 48_000
    overlap = (m - r) / m
    assert abs(overlap - 0.75) < 1e-9
    frames_per_sec = fs / r
    assert abs(frames_per_sec - 93.75) < 1e-9
    print("Chapter 08 solutions: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
