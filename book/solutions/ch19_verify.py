#!/usr/bin/env python3
"""Verified numeric answers for Chapter 19 exercises."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))

from audio_toolkit.effects import karplus_strong  # noqa: E402


def main() -> int:
    fs = 48_000.0
    d = 200
    f0_approx = fs / d
    assert abs(f0_approx - 240.0) < 1e-9

    y_hi = karplus_strong(fs, 220.0, 0.5, decay=0.99)
    y_lo = karplus_strong(fs, 220.0, 0.5, decay=0.995)
    tail_hi = y_hi[-int(fs // 10) :]
    tail_lo = y_lo[-int(fs // 10) :]
    assert np.sum(tail_lo**2) > np.sum(tail_hi**2)

    print("Chapter 19 solutions: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
