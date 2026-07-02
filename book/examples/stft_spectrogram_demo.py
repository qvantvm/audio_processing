#!/usr/bin/env python3
"""STFT spectrogram of a chirp (Chapter 08).

Run from book/: python examples/stft_spectrogram_demo.py
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)

FS = 22_050
duration = 1.0
n = np.arange(int(FS * duration))
# Linear chirp 200 Hz -> 4000 Hz
f0, f1 = 200.0, 4000.0
phase = 2 * np.pi * (f0 * n / FS + (f1 - f0) * n**2 / (2 * len(n) * FS))
x = 0.7 * np.sin(phase)

win = 1024
hop = 256
window = np.hanning(win)
frames = []
for start in range(0, len(x) - win, hop):
    frames.append(np.fft.rfft(x[start:start + win] * window))
S = np.array(frames).T
S_db = 20 * np.log10(np.maximum(np.abs(S), 1e-10))

fig, ax = plt.subplots(figsize=(9, 4))
extent = [0, duration, 0, FS / 2]
ax.imshow(S_db, origin="lower", aspect="auto", extent=extent, cmap="magma")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Frequency (Hz)")
ax.set_title("STFT spectrogram (Hann, win=1024, hop=256)")
fig.tight_layout()
out = FIG / "stft_chirp_spectrogram.png"
fig.savefig(out, dpi=150)
print(f"Wrote {out}")
