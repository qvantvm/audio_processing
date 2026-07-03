#!/usr/bin/env python3
"""Visualize complex sinusoids and phasors (Chapter 04 example).

Run from the book/ directory:
    python examples/complex_sinusoid_demo.py

Writes figures/complex_phasor.png
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

FIG_DIR = Path(__file__).resolve().parent.parent / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# A440 at 48 kHz — same convention as Chapter 02
F0 = 440.0
FS = 48_000
OMEGA = 2 * np.pi * F0 / FS  # rad/sample
PHI = np.pi / 6  # initial phase (30 degrees)
A = 0.8

# Show a few milliseconds — enough to see rotation in the phasor view
duration_s = 0.006
n = np.arange(int(duration_s * FS))
z = A * np.exp(1j * (OMEGA * n + PHI))
x = np.real(z)

fig, axes = plt.subplots(1, 2, figsize=(9, 4))

# --- Phasor trajectory in the complex plane (subsample for clarity) ---
step = max(1, len(n) // 40)
idx = np.arange(0, len(n), step)
axes[0].plot(np.real(z), np.imag(z), color="0.85", linewidth=1)
axes[0].scatter(np.real(z[idx]), np.imag(z[idx]), c=n[idx], cmap="viridis", s=18, zorder=3)
axes[0].annotate(
    "",
    xy=(np.real(z[0]), np.imag(z[0])),
    xytext=(0, 0),
    arrowprops=dict(arrowstyle="->", color="C3", lw=1.5),
)
axes[0].set_xlim(-A * 1.2, A * 1.2)
axes[0].set_ylim(-A * 1.2, A * 1.2)
axes[0].set_aspect("equal")
axes[0].axhline(0, color="0.5", linewidth=0.5)
axes[0].axvline(0, color="0.5", linewidth=0.5)
axes[0].set_xlabel("Re")
axes[0].set_ylabel("Im")
axes[0].set_title(r"Phasor $Ae^{j(\Omega n + \phi)}$ in the complex plane")
axes[0].grid(True, alpha=0.3)

# --- Real part vs time ---
t_ms = n / FS * 1000
axes[1].plot(t_ms, x, color="C0", label=r"$\Re\{Ae^{j(\Omega n+\phi)}\}$")
axes[1].set_xlabel("Time (ms)")
axes[1].set_ylabel("Amplitude")
axes[1].set_title(f"Real sinusoid at {F0:.0f} Hz (A440)")
axes[1].grid(True, alpha=0.3)
axes[1].legend(loc="upper right")

fig.tight_layout()
out = FIG_DIR / "complex_phasor.png"
fig.savefig(out, dpi=150)
plt.close(fig)

mag = np.abs(z[0])
phase_deg = np.angle(z[0], deg=True)
print(f"Complex sinusoid: A={A}, Omega={OMEGA:.6f} rad/sample, phi={PHI:.4f} rad")
print(f"Sample z[0]: magnitude={mag:.4f}, phase={phase_deg:.2f} deg")
print(f"Real peak check: max|x|={np.max(np.abs(x)):.4f} (expect {A})")
print(f"Wrote {out}")
