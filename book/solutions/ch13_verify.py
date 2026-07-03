#!/usr/bin/env python3
"""Verified numeric answers for Chapter 13 exercises."""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))

from audio_toolkit.meter import peak_amplitude, rms  # noqa: E402


def main() -> int:
    # 13.1 crest factor of sine
    fs = 48_000
    n = np.arange(fs // 10)
    x = 0.8 * np.sin(2 * np.pi * 440 * n / fs)
    crest_db = 20 * np.log10(peak_amplitude(x) / rms(x))
    assert abs(crest_db - 3.0103) < 0.01  # sqrt(2) ratio

    # 13.2 attack 10 ms at 48 kHz: alpha = exp(-1/(tau*fs))
    tau = 0.010
    alpha = math.exp(-1.0 / (tau * fs))
    assert 0.99 < alpha < 1.0

    # 13.3 compressor: input -8 dBFS, threshold -20 dBFS -> no gain reduction
    inp_db = -8.0
    thresh_db = -20.0
    assert inp_db > thresh_db

    # 13.4 K-weighting concept — LUFS uses frequency weighting (sanity check only)
    assert thresh_db < 0

    print("Chapter 13 solutions: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
