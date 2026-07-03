"""STFT and ISTFT with documented window normalization."""

from __future__ import annotations

from typing import Optional, Tuple

import numpy as np


def _window(name: str, n_fft: int) -> np.ndarray:
    if name == "hann":
        return np.hanning(n_fft).astype(np.float64)
    if name == "rect":
        return np.ones(n_fft, dtype=np.float64)
    raise ValueError(f"Unknown window: {name}")


def stft(
    x: np.ndarray,
    fs: float,
    n_fft: int = 1024,
    hop: Optional[int] = None,
    window: str = "hann",
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Short-time Fourier transform.

    Returns (S, freqs, times) where S has shape (n_freq, n_frames).
    """
    hop = hop or n_fft // 4
    w = _window(window, n_fft)
    frames = []
    for i in range(0, len(x) - n_fft + 1, hop):
        frames.append(np.fft.rfft(x[i : i + n_fft] * w))
    if not frames:
        freqs = np.fft.rfftfreq(n_fft, d=1.0 / fs)
        return np.zeros((len(freqs), 0), dtype=np.complex128), freqs, np.array([])
    s = np.array(frames).T
    times = np.arange(len(frames)) * hop / fs
    freqs = np.fft.rfftfreq(n_fft, d=1.0 / fs)
    return s, freqs, times


def istft(
    s: np.ndarray,
    fs: float,
    n_fft: int = 1024,
    hop: Optional[int] = None,
    window: str = "hann",
    length: Optional[int] = None,
) -> np.ndarray:
    """Inverse STFT with overlap-add and COLA scaling for Hann window."""
    hop = hop or n_fft // 4
    w = _window(window, n_fft)
    n_frames = s.shape[1]
    out_len = hop * (n_frames - 1) + n_fft if n_frames else 0
    if length is not None:
        out_len = length
    y = np.zeros(out_len, dtype=np.float64)
    norm = np.zeros(out_len, dtype=np.float64)
    for i in range(n_frames):
        frame = np.fft.irfft(s[:, i], n=n_fft) * w
        start = i * hop
        y[start : start + n_fft] += frame
        norm[start : start + n_fft] += w * w
    mask = norm > 1e-12
    y[mask] /= norm[mask]
    if length is not None:
        return y[:length].astype(np.float32)
    return y.astype(np.float32)


def coherent_gain(window: str, n_fft: int) -> float:
    """Mean window value (coherent gain for peak of unit sinusoid)."""
    return float(np.mean(_window(window, n_fft)))
