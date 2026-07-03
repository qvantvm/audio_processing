"""Sample-rate conversion (pedagogical minimal implementation).

Uses ``scipy.signal.resample_poly`` for rational ratios. For production SRC use
libsamplerate/SoX; this module is for teaching and tests.
"""

from __future__ import annotations

from fractions import Fraction

import numpy as np
from scipy.signal import resample_poly


def resample(
    x: np.ndarray,
    fs_in: float,
    fs_out: float,
    max_denominator: int = 1000,
) -> tuple[np.ndarray, float]:
    """Resample ``x`` from ``fs_in`` to ``fs_out`` Hz.

    Returns (y, fs_out). Uses rational approximation ``L/M`` for ``resample_poly``.
    """
    if fs_in <= 0 or fs_out <= 0:
        raise ValueError("sample rates must be positive")
    if fs_in == fs_out:
        return x.astype(np.float32), float(fs_out)
    frac = Fraction(fs_out / fs_in).limit_denominator(max_denominator)
    y = resample_poly(x.astype(np.float64), frac.numerator, frac.denominator)
    return y.astype(np.float32), float(fs_out)


def midi_to_hz(midi_note: int, a4_hz: float = 440.0, a4_midi: int = 69) -> float:
    """Equal-temperament frequency from MIDI note number."""
    return float(a4_hz * (2.0 ** ((midi_note - a4_midi) / 12.0)))
