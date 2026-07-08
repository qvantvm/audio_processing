#!/usr/bin/env python3
"""Karplus–Strong plucked string demo (Chapter 19).

Run from book/:
    python examples/karplus_strong_demo.py

Uses audio_toolkit.effects.karplus_strong and writes figures/karplus_strong.png.
"""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))

from audio_toolkit.effects import karplus_strong

FS = 48_000
F0 = 220.0
DURATION = 0.8

y = karplus_strong(FS, F0, DURATION, decay=0.995)
t = np.arange(len(y)) / FS

fig, axes = plt.subplots(2, 1, figsize=(8, 4), sharex=True)
axes[0].plot(t, y, linewidth=0.8)
axes[0].set_ylabel("Amplitude")
axes[0].set_title(f"Karplus–Strong string: f0={F0} Hz, fs={FS} Hz")
axes[0].grid(True, alpha=0.3)

win = int(0.05 * FS)
env = np.convolve(np.abs(y), np.ones(win) / win, mode="same")
axes[1].plot(t, 20 * np.log10(env + 1e-6))
axes[1].set_xlabel("Time (s)")
axes[1].set_ylabel("Envelope (dB, rough)")
axes[1].grid(True, alpha=0.3)

out_dir = Path(__file__).resolve().parent.parent / "figures"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "karplus_strong.png"
fig.tight_layout()
fig.savefig(out_path, dpi=150)
print(f"Generated {len(y)} samples ({DURATION} s)")
print(f"Wrote {out_path}")
