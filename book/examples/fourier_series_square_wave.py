#!/usr/bin/env python3
"""Fourier series partial sums converging to a square wave (Chapter 05 example).

Run from the book/ directory:
    python examples/fourier_series_square_wave.py

Writes figures/fourier_series_square_wave.png
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

FIG_DIR = Path(__file__).resolve().parent.parent / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

F0 = 100.0  # fundamental Hz — low enough to see harmonics on plot
FS = 48_000
DURATION_S = 0.04
t = np.arange(int(DURATION_S * FS)) / FS

# Target square wave: period 1/f0, values in {-1, +1}
phase = np.mod(t, 1 / F0) * F0  # cycles within period -> [0,1)
square = np.where(phase < 0.5, 1.0, -1.0)


def square_wave_partial(t: np.ndarray, f0: float, num_odd_harmonics: int) -> np.ndarray:
    """Real Fourier series partial sum using odd harmonics only."""
    x = np.zeros_like(t)
    for k in range(num_odd_harmonics):
        n = 2 * k + 1  # 1, 3, 5, ...
        x += (4 / (n * np.pi)) * np.sin(2 * np.pi * n * f0 * t)
    return x


harmonic_counts = [1, 3, 7, 21]
colors = ["C0", "C1", "C2", "C3"]

fig, axes = plt.subplots(2, 1, figsize=(9, 6), gridspec_kw={"height_ratios": [2, 1]})

for count, color in zip(harmonic_counts, colors):
    approx = square_wave_partial(t, F0, count)
    label = f"{2 * count - 1} terms (odd harmonics through {2 * count - 1})"
    axes[0].plot(t * 1000, approx, color=color, alpha=0.85, label=label)

axes[0].plot(t * 1000, square, color="0.2", linewidth=1.2, linestyle="--", label="Ideal square")
axes[0].set_xlim(0, 10)
axes[0].set_xlabel("Time (ms)")
axes[0].set_ylabel("Amplitude")
axes[0].set_title(f"Fourier series partial sums (f0 = {F0:.0f} Hz)")
axes[0].legend(loc="upper right", fontsize=8)
axes[0].grid(True, alpha=0.3)

# Magnitude of non-zero coefficients |c_k| for odd k (decays as 1/k)
max_k = 21
ks = np.arange(1, max_k + 1, 2)
coeff_mag = 4 / (ks * np.pi)
axes[1].stem(ks * F0, coeff_mag, linefmt="C4-", markerfmt="C4o", basefmt=" ")
axes[1].set_xlabel("Frequency (Hz)")
axes[1].set_ylabel(r"$|c_k|$ (scale)")
axes[1].set_title("Non-zero Fourier coefficients decay as 1/k for an odd square wave")
axes[1].grid(True, alpha=0.3)

fig.tight_layout()
out = FIG_DIR / "fourier_series_square_wave.png"
fig.savefig(out, dpi=150)
plt.close(fig)

# Simple error metric for the richest partial sum
approx = square_wave_partial(t, F0, harmonic_counts[-1])
rms_error = np.sqrt(np.mean((approx - square) ** 2))
print(f"Fundamental f0 = {F0} Hz; partial sum with {2 * harmonic_counts[-1] - 1} harmonics")
print(f"RMS error vs ideal square = {rms_error:.4f}")
print(f"Wrote {out}")
