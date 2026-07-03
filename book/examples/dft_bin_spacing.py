#!/usr/bin/env python3
"""DFT bin spacing and off-bin sinusoid leakage (Chapter 06 example).

Run from the book/ directory:
    python examples/dft_bin_spacing.py

Writes figures/dft_bin_spacing.png
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

FIG_DIR = Path(__file__).resolve().parent.parent / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

FS = 48_000
N = 1024
F0_OFF = 440.0  # A440 — generally not on the DFT bin grid
DELTA_F = FS / N

# Nearest bin center (for reference)
K_NEAREST = int(round(F0_OFF / DELTA_F))
F_BIN_NEAREST = K_NEAREST * DELTA_F

n = np.arange(N)
window = np.ones(N)  # rectangular — leakage preview for Chapter 07


def dft_magnitude_db(x: np.ndarray, n_fft: int) -> tuple[np.ndarray, np.ndarray]:
    X = np.fft.rfft(x, n=n_fft)
    freqs = np.fft.rfftfreq(n_fft, d=1 / FS)
    mag_db = 20 * np.log10(np.maximum(np.abs(X), 1e-12))
    return freqs, mag_db


x_off = 0.8 * np.cos(2 * np.pi * F0_OFF * n / FS)
x_on = 0.8 * np.cos(2 * np.pi * F_BIN_NEAREST * n / FS)

freqs_off, mag_off = dft_magnitude_db(x_off * window, N)
freqs_on, mag_on = dft_magnitude_db(x_on * window, N)

fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True)

axes[0].plot(freqs_off, mag_off, color="C0")
axes[0].axvline(F0_OFF, color="C3", linestyle="--", label=f"True f0 = {F0_OFF} Hz")
axes[0].set_xlim(300, 600)
axes[0].set_ylabel("Magnitude (dB)")
axes[0].set_title(f"Off-bin A440: N={N}, f_s={FS} Hz, Δf={DELTA_F:.3f} Hz")
axes[0].legend(loc="upper right")
axes[0].grid(True, alpha=0.3)

# Mark a few bin centers near 440 Hz
for k in range(K_NEAREST - 2, K_NEAREST + 4):
    if k < 0:
        continue
    f_k = k * DELTA_F
    if 300 <= f_k <= 600:
        axes[0].axvline(f_k, color="0.85", linewidth=0.8, zorder=0)

axes[1].plot(freqs_on, mag_on, color="C1")
axes[1].axvline(
    F_BIN_NEAREST,
    color="C3",
    linestyle="--",
    label=f"On-bin f = {F_BIN_NEAREST:.3f} Hz (k={K_NEAREST})",
)
axes[1].set_xlim(300, 600)
axes[1].set_xlabel("Frequency (Hz)")
axes[1].set_ylabel("Magnitude (dB)")
axes[1].set_title("On-bin sinusoid at nearest bin center — energy concentrated")
axes[1].legend(loc="upper right")
axes[1].grid(True, alpha=0.3)

fig.tight_layout()
out = FIG_DIR / "dft_bin_spacing.png"
fig.savefig(out, dpi=150)
plt.close(fig)

mask = (freqs_off >= 300) & (freqs_off <= 600)
peak_off = freqs_off[mask][np.argmax(mag_off[mask])]

print(f"Bin spacing Δf = f_s/N = {DELTA_F:.6f} Hz")
print(f"Nearest bin to 440 Hz: k={K_NEAREST}, center={F_BIN_NEAREST:.3f} Hz")
print(f"Off-bin peak (rect window): {peak_off:.3f} Hz (biased vs true {F0_OFF} Hz)")
print(f"Wrote {out}")
