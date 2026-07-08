"""Peak, RMS, and dBFS helpers."""

from __future__ import annotations

import numpy as np


def peak_amplitude(x: np.ndarray) -> float:
    return float(np.max(np.abs(x)))


def rms(x: np.ndarray) -> float:
    return float(np.sqrt(np.mean(np.square(x.astype(np.float64)))))


def linear_to_dbfs(amplitude: float, eps: float = 1e-12) -> float:
    return 20.0 * np.log10(max(abs(amplitude), eps))


def dbfs_to_linear(dbfs: float) -> float:
    return float(10.0 ** (dbfs / 20.0))
