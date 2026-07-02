#!/usr/bin/env python3
"""Compare rectangular vs Hann window leakage (Chapter 07).

Run from book/: python examples/window_leakage_demo.py
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)

FS, N, F0 = 48_000, 4096, 440.0
n = np.arange(N)
x = 0.8 * np.cos(2 * np.pi * F0 * n / FS)

def spectrum(w):
    X = np.fft.rfft(x * w, n=N)
    f = np.fft.rfftfreq(N, d=1 / FS)
    return f, 20 * np.log10(np.maximum(np.abs(X), 1e-12))

rect = np.ones(N)
hann = np.hanning(N)
f1, m1 = spectrum(rect)
f2, m2 = spectrum(hann)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(f1, m1, label="Rectangular", alpha=0.9)
ax.plot(f2, m2, label="Hann", alpha=0.9)
ax.set_xlim(0, 2000)
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Magnitude (dB)")
ax.set_title(f"Off-bin {F0} Hz tone: window leakage comparison (N={N})")
ax.legend()
ax.grid(True, alpha=0.3)
fig.tight_layout()
out = FIG / "window_leakage.png"
fig.savefig(out, dpi=150)
print(f"Wrote {out}")
