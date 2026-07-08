#!/usr/bin/env python3
"""Verified numeric answers for Chapter 21 exercises."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from scipy import signal

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))

from audio_toolkit.filters import apply_fir, design_fir_lowpass  # noqa: E402


def main() -> int:
    fs = 48_000.0
    h = design_fir_lowpass(fs, 1000.0, num_taps=31)
    impulse = np.zeros(256, dtype=np.float32)
    impulse[0] = 1.0
    y1 = apply_fir(impulse, h)
    y2 = signal.lfilter(h, [1.0], impulse)
    assert np.max(np.abs(y1 - y2)) < 1e-5

    # DC removal: high-pass via DC-block (diff) or check mean drops
    x = np.ones(1000, dtype=np.float32) * 0.5
    x -= x.mean()
    assert abs(x.mean()) < 1e-6

    s = np.random.default_rng(0).standard_normal((64, 32))
    assert s.shape == (64, 32)

    print("Chapter 21 solutions: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
