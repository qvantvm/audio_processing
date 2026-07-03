#!/usr/bin/env python3
"""Wavetable oscillator demo (Chapter 18).

Run from book/:
    python examples/wavetable_demo.py

Writes figures/wavetable_a440.png and audio_demos/wavetable_a440.wav.
"""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))

from audio_toolkit.io import write_wav
from audio_toolkit.synthesis import wavetable_osc

FS = 48_000
F0 = 440.0
DURATION = 0.05

y = wavetable_osc(FS, F0, int(DURATION * FS))
n = np.arange(len(y))

fig, ax = plt.subplots(figsize=(8, 3))
show = min(len(y), int(FS / F0 * 2))
ax.plot(n[:show], y[:show], linewidth=0.9)
ax.set_xlabel("Sample index n")
ax.set_ylabel("x[n]")
ax.set_title(f"Wavetable A440 (~{FS/F0:.1f} samples/period)")
ax.grid(True, alpha=0.3)
fig.tight_layout()

fig_dir = BOOK / "figures"
fig_dir.mkdir(parents=True, exist_ok=True)
fig.savefig(fig_dir / "wavetable_a440.png", dpi=150)

audio_dir = BOOK / "audio_demos"
audio_dir.mkdir(parents=True, exist_ok=True)
wav_path = audio_dir / "wavetable_a440.wav"
write_wav(wav_path, y, FS)
print(f"Period ≈ {FS/F0:.2f} samples")
print(f"Wrote {fig_dir / 'wavetable_a440.png'}")
print(f"Wrote {wav_path}")
