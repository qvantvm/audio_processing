#!/usr/bin/env python3
"""Verified numeric answers for Chapter 09 exercises."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))


def main() -> int:
    x = np.array([1.0, 2.0, 1.0])
    h = np.array([1.0, 1.0])
    y = np.convolve(x, h)
    assert np.allclose(y, [1.0, 3.0, 3.0, 1.0])
    delta = np.array([1.0])
    assert np.allclose(np.convolve(delta, h), h)
    print("Chapter 09 solutions: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
