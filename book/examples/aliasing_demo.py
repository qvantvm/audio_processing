#!/usr/bin/env python3
"""Demonstrate aliasing and uniform quantization (Chapter 03 examples).

Run from the book/ directory:
    python examples/aliasing_demo.py

Writes:
    figures/aliasing_fold.png
    figures/quantization_staircase.png
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

FIG_DIR = Path(__file__).resolve().parent.parent / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def alias_frequency(f: float, fs: float) -> float:
    """Return the unique frequency in [0, fs/2] indistinguishable from f after sampling."""
    f = abs(f) % fs
    if f > fs / 2:
        f = fs - f
    return f


def plot_aliasing() -> None:
    fs = 4_000  # Hz — low rate makes aliasing easy to see
    f_true = 3_500  # Hz — above Nyquist (fs/2 = 2000)
    f_alias = alias_frequency(f_true, fs)
    duration_s = 0.02
    n = np.arange(int(duration_s * fs))
    x = 0.9 * np.cos(2 * np.pi * f_true * n / fs)

    # High-rate reference showing the intended continuous-time frequency
    fs_ref = 200_000
    t_ref = np.linspace(0, duration_s, int(duration_s * fs_ref), endpoint=False)
    x_ref = 0.9 * np.cos(2 * np.pi * f_true * t_ref)

    fig, axes = plt.subplots(2, 1, figsize=(8, 5), sharex=False)

    axes[0].plot(t_ref * 1000, x_ref, color="0.7", label="3.5 kHz tone (reference)")
    axes[0].stem(
        n / fs * 1000, x, linefmt="C0-", markerfmt="C0o", basefmt=" ", label="Sampled at 4 kHz"
    )
    axes[0].set_xlim(0, 5)
    axes[0].set_xlabel("Time (ms)")
    axes[0].set_ylabel("Amplitude")
    axes[0].set_title(f"Aliasing: {f_true} Hz sampled at f_s = {fs} Hz")
    axes[0].legend(loc="upper right")
    axes[0].grid(True, alpha=0.3)

    # Spectrum of sampled sequence (positive frequencies only)
    n_fft = 4096
    X = np.fft.rfft(x, n=n_fft)
    freqs = np.fft.rfftfreq(n_fft, d=1 / fs)
    mag_db = 20 * np.log10(np.maximum(np.abs(X), 1e-12))

    axes[1].plot(freqs, mag_db, color="C0")
    axes[1].axvline(f_alias, color="C3", linestyle="--", label=f"Alias at {f_alias:.0f} Hz")
    axes[1].axvline(fs / 2, color="0.5", linestyle=":", label=f"Nyquist {fs/2:.0f} Hz")
    axes[1].set_xlim(0, fs / 2)
    axes[1].set_xlabel("Frequency (Hz)")
    axes[1].set_ylabel("Magnitude (dB)")
    axes[1].set_title("DFT of sampled sequence — energy appears at alias frequency")
    axes[1].legend(loc="upper right")
    axes[1].grid(True, alpha=0.3)

    fig.tight_layout()
    out = FIG_DIR / "aliasing_fold.png"
    fig.savefig(out, dpi=150)
    plt.close(fig)
    print(f"Aliasing: {f_true} Hz -> {f_alias} Hz at f_s = {fs} Hz")
    print(f"Wrote {out}")


def plot_quantization() -> None:
    bits = 4
    levels = 2**bits
    # Uniform quantizer on [-1, 1]
    x = np.linspace(-1, 1, 500)
    delta = 2 / levels
    x_q = delta * np.round(x / delta)
    x_q = np.clip(x_q, -1 + delta / 2, 1 - delta / 2)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, x, color="0.6", label="Input")
    ax.step(x, x_q, where="mid", color="C0", label=f"{bits}-bit uniform quantizer")
    ax.set_xlabel("Input amplitude")
    ax.set_ylabel("Quantized output")
    ax.set_title(f"Uniform quantization ({levels} levels)")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    out = FIG_DIR / "quantization_staircase.png"
    fig.savefig(out, dpi=150)
    plt.close(fig)

    # SNR for full-scale sine (well-known approximation)
    snr_db = 6.02 * bits + 1.76
    print(f"Quantization: {bits} bits -> {levels} levels, approx. sine SNR ~ {snr_db:.1f} dB")
    print(f"Wrote {out}")


if __name__ == "__main__":
    plot_aliasing()
    plot_quantization()
