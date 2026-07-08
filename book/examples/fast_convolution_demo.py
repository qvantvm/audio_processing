#!/usr/bin/env python3
"""Fast convolution vs direct convolution timing demo."""

from pathlib import Path
import time

import matplotlib.pyplot as plt
import numpy as np

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)


def main() -> None:
    fs = 48000
    rng = np.random.default_rng(1)
    x = rng.standard_normal(fs)  # 1 s noise
    ir_len = 48000  # 1 s synthetic RIR
    h = rng.standard_normal(ir_len) * np.exp(-np.linspace(0, 8, ir_len))

    t0 = time.perf_counter()
    y_direct = np.convolve(x, h, mode="full")
    t_direct = time.perf_counter() - t0

    n_fft = 1 << int(np.ceil(np.log2(len(x) + len(h) - 1)))
    t0 = time.perf_counter()
    Y = np.fft.rfft(x, n_fft) * np.fft.rfft(h, n_fft)
    y_fft = np.fft.irfft(Y)[: len(x) + len(h) - 1]
    t_fft = time.perf_counter() - t0

    err = np.max(np.abs(y_direct - y_fft))

    fig, axes = plt.subplots(1, 2, figsize=(9, 4))
    axes[0].bar(["Direct", "FFT"], [t_direct * 1000, t_fft * 1000], color=["#5c6bc0", "#26a69a"])
    axes[0].set_ylabel("Time [ms]")
    axes[0].set_title("Convolution CPU (1 s IR @ 48 kHz)")
    axes[0].grid(True, axis="y", alpha=0.3)
    axes[1].plot(y_fft[:2000], alpha=0.8)
    axes[1].set_title(f"FFT result (max error vs direct: {err:.2e})")
    axes[1].set_xlabel("Sample")
    axes[1].grid(True, alpha=0.3)
    out = FIG / "fast_convolution.png"
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
