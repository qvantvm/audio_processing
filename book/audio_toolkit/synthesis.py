"""Synthesis representations: wavetable and naive oscillators.

Implementation quality (see ``audio_toolkit._quality.ImplQuality``):

- ``wavetable_osc`` — **recommended** minimal band-limited-friendly oscillator.
- ``naive_saw`` — **artifact** demo; intentionally aliases for teaching/hearing.
"""

from __future__ import annotations

import numpy as np

from audio_toolkit._quality import ARTIFACT_FUNCTIONS, ImplQuality

__all__ = ["wavetable_osc", "naive_saw", "naive_saw_artifact", "NAIVE_SAW_QUALITY"]

NAIVE_SAW_QUALITY = ImplQuality.ARTIFACT


def wavetable_osc(
    fs: float,
    f0: float,
    num_samples: int,
    table: np.ndarray | None = None,
    amplitude: float = 1.0,
    phase: float = 0.0,
) -> np.ndarray:
    """Wavetable oscillator with linear interpolation (recommended minimal impl).

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
    """**ARTIFACT / anti-example** — naive sawtooth that aliases on high notes.

    Use only for demos (`export_audio_demos.py`, listening exercises).
    Do not use in production synthesis chains.
    """
    return naive_saw_artifact(fs, f0, num_samples, amplitude)


def naive_saw_artifact(
    fs: float,
    f0: float,
    num_samples: int,
    amplitude: float = 1.0,
) -> np.ndarray:
    """Intentionally flawed sawtooth for aliasing demonstrations."""
    assert "naive_saw" in ARTIFACT_FUNCTIONS
    inc = f0 / fs
    phase = 0.0
    out = np.zeros(num_samples, dtype=np.float64)
    for i in range(num_samples):
        out[i] = amplitude * (2.0 * phase - 1.0)
        phase = (phase + inc) % 1.0
    return out.astype(np.float32)
