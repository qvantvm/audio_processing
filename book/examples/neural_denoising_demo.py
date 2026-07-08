#!/usr/bin/env python3
"""STFT-domain spectral gate — numpy-only denoising demo."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)


def stft_gate(x: np.ndarray, fs: int, thresh_db: float = -35.0) -> np.ndarray:
    n_fft = 1024
    hop = 256
    window = np.hanning(n_fft)
    out = np.zeros_like(x)
    norm = np.zeros_like(x)
    for start in range(0, len(x) - n_fft, hop):
        frame = x[start : start + n_fft] * window
        X = np.fft.rfft(frame)
        mag = np.abs(X)
        ref = np.max(mag) + 1e-12
        mask = 20 * np.log10(mag / ref) > thresh_db
        Y = X * mask
        y_frame = np.fft.irfft(Y, n=n_fft) * window
        out[start : start + n_fft] += y_frame
        norm[start : start + n_fft] += window**2
    norm = np.maximum(norm, 1e-8)
    return out / norm


def main() -> None:
    fs = 48000
    t = np.arange(fs) / fs
    clean = 0.4 * np.sin(2 * np.pi * 440 * t)
    noise = 0.15 * np.random.standard_normal(len(t))
    noisy = clean + noise
    denoised = stft_gate(noisy, fs, thresh_db=-32)

    fig, axes = plt.subplots(3, 1, figsize=(9, 6), sharex=True)
    for ax, sig, title in zip(
        axes,
        [noisy, denoised, clean],
        ["Noisy input", "STFT magnitude gate", "Clean reference"],
    ):
        ax.plot(t[:2000], sig[:2000], lw=0.6)
        ax.set_ylabel("Amp")
        ax.set_title(title)
        ax.grid(True, alpha=0.3)
    axes[-1].set_xlabel("Time [s]")
    out = FIG / "neural_denoising_gate.png"
    fig.suptitle("Classical spectral gate (numpy STFT)")
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
