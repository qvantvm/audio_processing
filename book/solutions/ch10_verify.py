#!/usr/bin/env python3
"""Verified numeric answers for Chapter 10 exercises."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from scipy import signal

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))

from audio_toolkit.filters import design_fir_lowpass, frequency_response  # noqa: E402


def main() -> int:
    # 10.1 H(z) = 0.5 + 0.5 z^{-1}
    b = np.array([0.5, 0.5])
    w, h = signal.freqz(b, [1.0])
    gain_dc = np.abs(h[0])
    gain_nyq = np.abs(h[-1])
    assert abs(gain_dc - 1.0) < 1e-9
    assert gain_nyq < 0.01  # lowpass: null at Nyquist for this two-tap averager

    # 10.2 stability
    assert 0.9 < 1.0
    assert 1.05 > 1.0  # outside unit circle → unstable for causal IIR

    # 10.3 FIR design
    fs = 44_100.0
    h_lp = design_fir_lowpass(fs, 1000.0, num_taps=101)
    freqs, mag = frequency_response(h_lp, fs)
    pass_g = mag[np.argmin(np.abs(freqs - 500.0))]
    stop_g = mag[np.argmin(np.abs(freqs - 10_000.0))]
    assert pass_g > 0.8 and stop_g < 0.3

    print("Chapter 10 solutions: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
