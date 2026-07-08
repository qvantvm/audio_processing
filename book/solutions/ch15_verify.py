#!/usr/bin/env python3
"""Verified numeric answers for Chapter 15 exercises."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))


def spectral_centroid(freqs: np.ndarray, mag: np.ndarray) -> float:
    m = np.abs(mag)
    s = m.sum()
    if s <= 0:
        return 0.0
    return float(np.sum(freqs * m) / s)


def main() -> int:
    # 15.1 manual centroid
    freqs = np.array([100.0, 200.0, 300.0])
    mag = np.array([1.0, 2.0, 1.0])
    c = spectral_centroid(freqs, mag)
    assert abs(c - 200.0) < 1e-9

    # spectral flux: L1 norm of positive magnitude difference
    a = np.array([1.0, 2.0, 1.0])
    b = np.array([1.0, 3.0, 0.5])
    flux = np.sum(np.maximum(b - a, 0.0))
    assert flux == 1.0

    print("Chapter 15 solutions: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
