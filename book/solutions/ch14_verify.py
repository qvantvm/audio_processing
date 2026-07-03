#!/usr/bin/env python3
"""Verified numeric answers for Chapter 14 exercises."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from scipy.signal import resample_poly

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))


def main() -> int:
    fs_in, fs_out = 44_100, 48_000
    duration = 1.0
    n_in = int(fs_in * duration)
    n = np.arange(n_in)
    f0 = 440.0
    x = np.sin(2 * np.pi * f0 * n / fs_in).astype(np.float64)

    # 44100 -> 48000 is ratio 160/147
    y = resample_poly(x, 160, 147)
    assert abs(len(y) - fs_out * duration) < 2

    # peak frequency via FFT
    spec = np.abs(np.fft.rfft(y))
    freqs = np.fft.rfftfreq(len(y), d=1.0 / fs_out)
    peak_f = freqs[int(np.argmax(spec[1:])) + 1]  # skip DC
    assert abs(peak_f - f0) < 1.0, f"resampled peak {peak_f} Hz"

    print("Chapter 14 solutions: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
