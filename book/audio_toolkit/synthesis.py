"""Synthesis representations: wavetable and naive oscillators."""

from __future__ import annotations

import numpy as np


def wavetable_osc(
    fs: float,
    f0: float,
    num_samples: int,
    table: np.ndarray | None = None,
    amplitude: float = 1.0,
    phase: float = 0.0,
) -> np.ndarray:
    """Wavetable oscillator with linear interpolation.

    Representation: one stored period + phase pointer — preserves pitch and
    stored waveform shape; discards time-varying spectra unless table morphs.
    """
    if table is None:
        t = np.linspace(0, 2 * np.pi, 512, endpoint=False)
        table = np.sin(t).astype(np.float64)
    table = np.asarray(table, dtype=np.float64)
    table_len = len(table)
    inc = f0 / fs
    out = np.zeros(num_samples, dtype=np.float64)
    p = (phase / (2 * np.pi)) % 1.0
    for i in range(num_samples):
        idx = p * table_len
        i0 = int(idx) % table_len
        frac = idx - int(idx)
        i1 = (i0 + 1) % table_len
        out[i] = amplitude * ((1 - frac) * table[i0] + frac * table[i1])
        p = (p + inc) % 1.0
    return out.astype(np.float32)


def naive_saw(
    fs: float,
    f0: float,
    num_samples: int,
    amplitude: float = 1.0,
) -> np.ndarray:
    """Naive rising sawtooth — aliases on high notes (demo artifact)."""
    inc = f0 / fs
    phase = 0.0
    out = np.zeros(num_samples, dtype=np.float64)
    for i in range(num_samples):
        out[i] = amplitude * (2.0 * phase - 1.0)
        phase = (phase + inc) % 1.0
    return out.astype(np.float32)
