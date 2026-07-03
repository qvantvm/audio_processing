"""FIR filter design and application."""

from __future__ import annotations

import numpy as np
from scipy import signal


def design_fir_lowpass(fs: float, cutoff_hz: float, num_taps: int = 101) -> np.ndarray:
    """Linear-phase FIR low-pass; cutoff_hz must be < fs/2."""
    nyq = fs / 2.0
    if not 0 < cutoff_hz < nyq:
        raise ValueError(f"cutoff_hz must be in (0, {nyq})")
    return signal.firwin(num_taps, cutoff_hz / nyq, window="hamming")


def apply_fir(x: np.ndarray, h: np.ndarray) -> np.ndarray:
    """Apply FIR via scipy.signal.lfilter."""
    return signal.lfilter(h, [1.0], x).astype(np.float32)


def frequency_response(h: np.ndarray, fs: float, n_fft: int = 4096) -> tuple[np.ndarray, np.ndarray]:
    """Return (freqs_hz, |H|) for FIR coefficients h."""
    w, h_resp = signal.freqz(h, worN=n_fft, fs=fs)
    return w, np.abs(h_resp)
