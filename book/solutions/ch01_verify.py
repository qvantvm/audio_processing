#!/usr/bin/env python3
"""Verified numeric answers for Chapter 01 exercises."""

from __future__ import annotations

import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))


def exercise_1_1() -> int:
    fs = 44100
    minutes = 3
    return fs * minutes * 60  # 7_938_000


def exercise_1_3() -> tuple[float, int, float]:
    fs = 48000
    n = 2048
    delta_f = fs / n
    k = round(1000 / delta_f)
    center = k * delta_f
    return delta_f, k, center


def main() -> int:
    n_samples = exercise_1_1()
    assert n_samples == 7_938_000, n_samples
    delta_f, k, center = exercise_1_3()
    assert abs(delta_f - 23.4375) < 1e-9
    assert k == 43
    assert abs(center - 1007.8125) < 1e-9
    print("Chapter 01 solutions: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
