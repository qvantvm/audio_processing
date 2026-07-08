#!/usr/bin/env python3
"""Generate a discrete A440 sine wave and plot samples (Chapter 02 example).

Run from the book/ directory:
    python examples/a440_sine_wave.py

Writes figures/a440_samples.png and prints basic timing facts.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# --- Parameters (declare explicitly in real code) ---
F0 = 440.0  # Hz, concert A
FS = 48_000  # samples per second
DURATION_S = 0.005  # show 5 ms — a few cycles at 440 Hz
AMPLITUDE = 0.8  # peak amplitude, linear (not dBFS yet)

# --- Build discrete-time signal x[n] ---
num_samples = int(round(DURATION_S * FS))
n = np.arange(num_samples)
x = AMPLITUDE * np.cos(2 * np.pi * F0 * n / FS)

# --- Derived quantities ---
sample_period_s = 1.0 / FS
period_samples = FS / F0  # samples per cycle (generally non-integer)
duration_s = num_samples / FS

print(f"Sample rate f_s = {FS} Hz  (T_s = {sample_period_s*1e6:.3f} µs)")
print(f"Frequency f_0 = {F0} Hz")
print(f"Period = {period_samples:.4f} samples  ({1/F0*1000:.4f} ms)")
print(f"Buffer length N = {num_samples}  (duration = {duration_s*1000:.3f} ms)")
print(f"Peak amplitude = {AMPLITUDE}  ({20*np.log10(AMPLITUDE):.2f} dBFS)")

# --- Figure: stem plot of first ~1.5 cycles ---
show_samples = min(num_samples, int(round(1.5 * period_samples)))
fig, ax = plt.subplots(figsize=(8, 3))
markerline, stemlines, baseline = ax.stem(
    n[:show_samples], x[:show_samples], linefmt="C0-", markerfmt="C0o", basefmt=" "
)
plt.setp(stemlines, linewidth=0.8)
plt.setp(markerline, markersize=4)
ax.set_xlabel("Sample index n")
ax.set_ylabel("x[n]")
ax.set_title(f"A440 at f_s = {FS} Hz (first ~1.5 periods)")
ax.grid(True, alpha=0.3)
fig.tight_layout()

out_dir = Path(__file__).resolve().parent.parent / "figures"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "a440_samples.png"
fig.savefig(out_path, dpi=150)
print(f"Wrote {out_path}")
