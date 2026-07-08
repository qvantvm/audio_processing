#!/usr/bin/env python3
"""Quantization, dither, and first-order noise shaping demo."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)


def quantize(x: np.ndarray, bits: int = 8) -> np.ndarray:
    levels = 2**bits - 1
    return np.round(x * levels) / levels


def main() -> None:
    fs = 48000
    n = np.arange(4096)
    f0 = 997.0
    x = 0.01 * np.sin(2 * np.pi * f0 * n / fs)  # quiet tone

    q_plain = quantize(x, bits=8)
    d_rect = (np.random.rand(len(x)) - 0.5) / (2**8)
    q_dither = quantize(x + d_rect, bits=8) - d_rect

    err_shaped = np.zeros_like(x)
    y_shaped = np.zeros_like(x)
    for i in range(1, len(x)):
        err_shaped[i] = err_shaped[i - 1] + (quantize(x[i], 8) - x[i])
        y_shaped[i] = x[i] - 0.5 * err_shaped[i - 1]
    q_shaped = quantize(y_shaped, bits=8)

    def spectrum(sig: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        w = np.hanning(len(sig))
        X = np.fft.rfft(sig * w)
        freqs = np.fft.rfftfreq(len(sig), 1 / fs)
        mag = 20 * np.log10(np.abs(X) + 1e-12)
        return freqs, mag

    fig, axes = plt.subplots(2, 2, figsize=(10, 6))
    cases = [
        ("Plain quantization", q_plain - x),
        ("Rectangular dither", q_dither - x),
        ("Noise-shaped loop", q_shaped - x),
    ]
    for ax, (title, err) in zip(axes.flat[:3], cases):
        f, m = spectrum(err)
        ax.plot(f, m, lw=0.8)
        ax.set_xlim(0, 8000)
        ax.set_ylim(-100, -20)
        ax.set_title(title)
        ax.set_xlabel("Frequency [Hz]")
        ax.set_ylabel("Error [dB]")
        ax.grid(True, alpha=0.3)
    axes[1, 1].axis("off")
    axes[1, 1].text(
        0.0,
        0.6,
        "Low-level sine at -40 dBFS\n8-bit quantizer\n"
        "Shaping pushes error to high frequencies",
        fontsize=11,
        va="top",
    )
    out = FIG / "quantization_dither.png"
    fig.suptitle("Quantization error spectra")
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
