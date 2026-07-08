#!/usr/bin/env python3
"""Continuous-time convolution demo (syllabus 1.1)."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)


def main() -> None:
    fs_vis = 2000
    t = np.linspace(0, 0.5, int(0.5 * fs_vis), endpoint=False)
    dt = t[1] - t[0]
    x = np.sin(2 * np.pi * 5 * t) * np.exp(-4 * t)
    h = np.exp(-30 * np.abs(t - 0.04))
    h /= np.sum(h) * dt
    y = np.convolve(x, h, mode="same") * dt

    fig, axes = plt.subplots(3, 1, figsize=(8, 6), sharex=True)
    axes[0].plot(t, x, color="#1565c0")
    axes[0].set_ylabel("x(t)")
    axes[0].set_title("Continuous-time convolution")
    axes[1].plot(t, h, color="#2e7d32")
    axes[1].set_ylabel("h(t)")
    axes[2].plot(t, y, color="#c62828")
    axes[2].set_ylabel("y(t)")
    axes[2].set_xlabel("Time [s]")
    for ax in axes:
        ax.grid(True, alpha=0.3)
    out = FIG / "continuous_convolution.png"
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
