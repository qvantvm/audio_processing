#!/usr/bin/env python3
"""Oversampling vs Nyquist-rate quantization SNR demo."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)


def quantize_1bit(x: np.ndarray) -> np.ndarray:
    return np.where(x >= 0, 1.0, -1.0)


def main() -> None:
    fs = 48000
    osr = 64
    n = np.arange(8192 * osr)
    f0 = 440.0
    x_os = 0.5 * np.sin(2 * np.pi * f0 * n / (fs * osr))

    # First-order sigma-delta style
    y = np.zeros_like(x_os)
    integrator = 0.0
    for i in range(len(x_os)):
        integrator += x_os[i] - y[i]
        y[i] = quantize_1bit(integrator)

    # Decimate (naive box average)
    y_dec = y.reshape(-1, osr).mean(axis=1)
    x_ref = 0.5 * np.sin(2 * np.pi * f0 * np.arange(len(y_dec)) / fs)
    err = y_dec - x_ref
    snr = 10 * np.log10(np.var(x_ref) / (np.var(err) + 1e-18))

    fig, axes = plt.subplots(2, 1, figsize=(9, 5))
    axes[0].plot(n[:400] / (fs * osr), x_os[:400], label="input")
    axes[0].plot(n[:400] / (fs * osr), y[:400], label="1-bit output", alpha=0.7)
    axes[0].legend()
    axes[0].set_title(f"Oversampled 1-bit loop (OSR={osr})")
    axes[0].set_xlabel("Time [s]")
    axes[0].grid(True, alpha=0.3)
    axes[1].plot(err[:512], color="#c62828")
    axes[1].set_title(f"Decimated error (approx SNR = {snr:.1f} dB)")
    axes[1].set_xlabel("Sample")
    axes[1].grid(True, alpha=0.3)
    out = FIG / "oversampling_quantization.png"
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
