#!/usr/bin/env python3
"""Verified checks for Chapter 20 exercises (conceptual + pipeline smoke)."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))

from audio_toolkit.spectral import stft  # noqa: E402


def main() -> int:
    fs = 16_000.0
    n = np.arange(int(fs))
    x = np.sin(2 * np.pi * 440 * n / fs).astype(np.float32)
    s, freqs, times = stft(x, fs, n_fft=512, hop=128)
    assert s.shape[0] == len(freqs)
    assert s.shape[1] == len(times)
    assert freqs[-1] <= fs / 2

    print("Chapter 20 solutions: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
