#!/usr/bin/env python3
"""Verified numeric answers for Chapter 12 exercises."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from scipy import signal

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))


def main() -> int:
    # 12.2 linear-phase FIR symmetry
    h = signal.firwin(31, 0.2, window="hamming")
    assert np.allclose(h, h[::-1], atol=1e-10)

    # group delay of symmetric FIR is constant (approx) — check variance small
    w, gd = signal.group_delay((h, [1.0]))
    mid = gd[len(gd) // 4 : 3 * len(gd) // 4]
    assert np.std(mid) < 0.5

    print("Chapter 12 solutions: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
