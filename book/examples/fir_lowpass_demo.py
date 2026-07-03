#!/usr/bin/env python3
"""FIR lowpass filter demo (Chapter 10).

Run from book/: python examples/fir_lowpass_demo.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)

FS = 48_000
fc = 2000.0
numtaps = 101
n = np.arange(numtaps)
M = numtaps - 1
# Windowed sinc lowpass
h = (2 * fc / FS) * np.sinc(2 * fc * (n - M / 2) / FS)
h *= np.hanning(numtaps)
h /= np.sum(h)

# Test signal: low + high sine
t = np.arange(FS // 10) / FS
x = 0.5 * np.sin(2 * np.pi * 500 * t) + 0.5 * np.sin(2 * np.pi * 8000 * t)
y = np.convolve(x, h, mode="same")

H = np.fft.rfft(h, n=4096)
f = np.fft.rfftfreq(4096, d=1 / FS)
mag_db = 20 * np.log10(np.maximum(np.abs(H), 1e-12))

fig, axes = plt.subplots(2, 1, figsize=(8, 6))
axes[0].plot(f, mag_db)
axes[0].axvline(fc, color="C3", linestyle="--", label=f"fc={fc} Hz")
axes[0].set_xlim(0, 10000)
axes[0].set_ylabel("Magnitude (dB)")
axes[0].set_title("FIR lowpass magnitude response")
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].plot(t[:2000] * 1000, x[:2000], alpha=0.6, label="Input")
axes[1].plot(t[:2000] * 1000, y[:2000], label="Filtered")
axes[1].set_xlabel("Time (ms)")
axes[1].set_ylabel("Amplitude")
axes[1].legend()
axes[1].grid(True, alpha=0.3)
fig.tight_layout()
out = FIG / "fir_lowpass.png"
fig.savefig(out, dpi=150)
print(f"Wrote {out}")
