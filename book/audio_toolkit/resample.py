"""Sample-rate conversion with explicit quality tiers.

- ``ImplQuality.PEDAGOGICAL``: fast rational-ratio wrapper (default, teaching)
- ``ImplQuality.RECOMMENDED``: higher-ratio approximation + stronger Kaiser window

For broadcast-grade SRC use libsamplerate/SoX; these tiers are in-repo teaching tools.
"""

from __future__ import annotations

from fractions import Fraction

import numpy as np
from scipy.signal import resample_poly

from audio_toolkit._quality import ImplQuality


def resample(
    x: np.ndarray,
    fs_in: float,
    fs_out: float,
    max_denominator: int = 1000,
    quality: ImplQuality = ImplQuality.PEDAGOGICAL,
) -> tuple[np.ndarray, float]:
    """Resample ``x`` from ``fs_in`` to ``fs_out`` Hz.

    Returns (y, fs_out). Uses rational approximation ``L/M`` for ``resample_poly``.
    """
    if fs_in <= 0 or fs_out <= 0:
        raise ValueError("sample rates must be positive")
    if fs_in == fs_out:
        return x.astype(np.float32), float(fs_out)

    denom_limit = max_denominator
    window: str | tuple[str, float] = ("kaiser", 5.0)
    padtype = "constant"
    if quality == ImplQuality.RECOMMENDED:
        denom_limit = max(max_denominator, 10_000)
        window = ("kaiser", 8.0)
        padtype = "line"

    frac = Fraction(fs_out / fs_in).limit_denominator(denom_limit)
    y = resample_poly(
        x.astype(np.float64),
        frac.numerator,
        frac.denominator,
        window=window,
        padtype=padtype,
    )
    return y.astype(np.float32), float(fs_out)


def midi_to_hz(midi_note: int, a4_hz: float = 440.0, a4_midi: int = 69) -> float:
    """Equal-temperament frequency from MIDI note number."""
    return float(a4_hz * (2.0 ** ((midi_note - a4_midi) / 12.0)))
