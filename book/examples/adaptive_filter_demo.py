#!/usr/bin/env python3
"""LMS adaptive filter — system identification demo."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)


def lms(x: np.ndarray, d: np.ndarray, num_taps: int = 16, mu: float = 0.05):
    w = np.zeros(num_taps)
    y = np.zeros_like(d)
    e = np.zeros_like(d)
    for n in range(num_taps, len(x)):
        xv = x[n - num_taps : n][::-1]
        y[n] = w @ xv
        e[n] = d[n] - y[n]
        w += mu * e[n] * xv
    return y, e, w


def main() -> None:
    rng = np.random.default_rng(0)
    n = 4000
    x = rng.standard_normal(n)
    h_true = np.array([0.2, -0.5, 0.3, 0.1])
    d = np.convolve(x, h_true, mode="same")
    y, e, w = lms(x, d, num_taps=16, mu=0.02)

    fig, axes = plt.subplots(2, 1, figsize=(8, 5))
    axes[0].stem(np.arange(len(h_true)), h_true, linefmt="C0-", markerfmt="C0o", basefmt=" ")
    axes[0].stem(np.arange(len(w)), w, linefmt="C1--", markerfmt="C1s", basefmt=" ")
    axes[0].set_title("True vs learned FIR taps")
    axes[0].legend(["True", "LMS estimate"])
    axes[0].grid(True, alpha=0.3)
    axes[1].plot(e**2)
    axes[1].set_title("Squared error (learning curve)")
    axes[1].set_xlabel("Sample")
    axes[1].grid(True, alpha=0.3)
    out = FIG / "adaptive_filter_lms.png"
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
