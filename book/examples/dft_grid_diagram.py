#!/usr/bin/env python3
"""DFT frequency grid diagram (Chapter 06)."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)

fs, n = 48_000, 1024
df = fs / n
k = np.arange(n // 2 + 1)
freqs = k * df

fig, ax = plt.subplots(figsize=(9, 3))
ax.stem(freqs, np.ones_like(freqs), linefmt="C0-", markerfmt="C0o", basefmt=" ")
ax.set_xlim(0, 5000)
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("DFT bin centers")
ax.set_title(f"DFT grid: Δf = f_s/N = {df:.2f} Hz (N={n}, f_s={fs} Hz)")
ax.grid(True, alpha=0.3)
for f_mark in (440, 1000):
    k_near = int(round(f_mark / df))
    ax.axvline(freqs[k_near], color="red", alpha=0.4, linestyle="--")
    ax.text(freqs[k_near], 1.05, f"k={k_near}", ha="center", fontsize=8, color="red")

out = FIG / "dft_grid.png"
fig.tight_layout()
fig.savefig(out, dpi=150)
print(f"Wrote {out}")
