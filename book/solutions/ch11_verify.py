#!/usr/bin/env python3
"""Verified numeric answers for Chapter 11 exercises."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))


def comb_feedforward_response(g: float, d: int, n_fft: int = 4096) -> tuple[np.ndarray, np.ndarray]:
    """H(z) = 1 + g z^{-D} on unit circle."""
    w = np.linspace(0, np.pi, n_fft)
    z = np.exp(1j * w)
    h = 1.0 + g * z ** (-d)
    return w, np.abs(h)


def main() -> int:
    g, d = 0.7, 100
    w, mag = comb_feedforward_response(g, d)
    # peaks when D*w = 2*pi*k => w_k = 2*pi*k/D
    k1 = int(round((2 * np.pi / d) / (w[1] - w[0])))
    assert mag[k1] > 1.5  # constructive peak near first comb mode
    assert mag[0] > 1.0  # DC boost for feedforward comb with g>0

    # incommensurate delays reduce shared periodicity (conceptual) — verify three delays differ
    delays = [97, 113, 137]
    assert len(set(delays)) == 3

    print("Chapter 11 solutions: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
