#!/usr/bin/env python3
"""Verified numeric answers for Chapter 16 exercises."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))


def estimate_f0_autocorr(
    x: np.ndarray, fs: float, f_min: float = 80.0, f_max: float = 1000.0
) -> float:
    """Naive autocorrelation pitch estimate."""
    x = x.astype(np.float64)
    x -= x.mean()
    lag_min = int(fs / f_max)
    lag_max = int(fs / f_min)
    best_lag, best_val = lag_min, -1.0
    for lag in range(lag_min, lag_max):
        r = np.dot(x[:-lag], x[lag:])
        if r > best_val:
            best_val = r
            best_lag = lag
    return fs / best_lag


def main() -> int:
    fs = 48_000.0
    f0_true = 220.0
    n = np.arange(int(fs * 0.5))
    x = np.sin(2 * np.pi * f0_true * n / fs)
    est = estimate_f0_autocorr(x, fs)
    assert abs(est - f0_true) < 2.0, f"autocorr f0 {est}"

    # 120 BPM -> 2 Hz pulse rate
    bpm = 120
    pulse_hz = bpm / 60.0
    assert abs(pulse_hz - 2.0) < 1e-9

    print("Chapter 16 solutions: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
