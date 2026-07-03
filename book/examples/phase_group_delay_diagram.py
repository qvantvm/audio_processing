#!/usr/bin/env python3
"""Phase and group delay diagram (Chapter 12)."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)

fs = 48_000
h_lin = signal.firwin(51, 500.0 / (fs / 2), window="hamming")
w, h = signal.freqz(h_lin, worN=2048, fs=fs)
phase = np.unwrap(np.angle(h))
gd = -np.diff(phase) / np.diff(w) * (fs / (2 * np.pi))  # samples approx

fig, axes = plt.subplots(2, 1, figsize=(8, 4), sharex=True)
axes[0].plot(w, phase)
axes[0].set_ylabel("Phase (rad)")
axes[0].set_title("Linear-phase FIR: phase vs frequency")
axes[0].grid(True, alpha=0.3)
axes[1].plot(w[:-1], gd)
axes[1].set_xlabel("Frequency (Hz)")
axes[1].set_ylabel("Group delay (samples, approx)")
axes[1].grid(True, alpha=0.3)

out = FIG / "phase_group_delay.png"
fig.tight_layout()
fig.savefig(out, dpi=150)
print(f"Wrote {out}")
