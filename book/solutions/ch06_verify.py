#!/usr/bin/env python3
"""Verified numeric answers for Chapter 06 exercises."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))


def main() -> int:
    fs, n = 44100, 4096
    delta_f = fs / n
    assert abs(delta_f - 44100 / 4096) < 1e-9
    k = 100
    assert abs(k * delta_f - 100 * fs / 4096) < 1e-6
    # 3. 440 Hz sine peak bin
    fs2, n2, f0 = 48000, 1024, 440.0
    n_arr = np.arange(n2)
    x = np.sin(2 * np.pi * f0 * n_arr / fs2)
    X = np.fft.rfft(x)
    k_peak = int(np.argmax(np.abs(X)))
    bin_hz = k_peak * fs2 / n2
    assert k_peak == 9
    assert abs(bin_hz - 421.875) < 1e-9
    # 4. zero pad grid
    delta_f4 = fs2 / (4 * n2)
    assert delta_f4 < fs2 / n2
    print("Chapter 06 solutions: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
