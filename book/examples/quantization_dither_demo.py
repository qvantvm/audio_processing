#!/usr/bin/env python3
"""Quantization, dither, and first-order noise shaping demo."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)


def quantize_midtread(x: np.ndarray, bits: int, full_scale: float = 1.0) -> np.ndarray:
    """Round-to-nearest uniform mid-tread quantizer on [-full_scale, full_scale)."""
    levels = 2**bits
    delta = 2 * full_scale / levels
    x_clip = np.clip(x, -full_scale, full_scale - delta / 2)
    return delta * np.round(x_clip / delta)


def tpdf_dither(n: int, lsb: float) -> np.ndarray:
    """Triangular PDF dither: sum of two independent RPDF, peak-to-peak 2*lsb."""
    return (np.random.rand(n) - np.random.rand(n)) * lsb


def first_order_noise_shape(
    x: np.ndarray, bits: int, full_scale: float = 1.0
) -> tuple[np.ndarray, np.ndarray]:
    """Non-subtractive first-order noise-shaped quantizer."""
    delta = 2 * full_scale / (2**bits)
    y = np.zeros_like(x)
    err_state = 0.0
    for i in range(len(x)):
        target = x[i] - err_state
        q = quantize_midtread(np.array([target]), bits, full_scale)[0]
        e = q - target
        err_state = e
        y[i] = q
    return y, y - x


def spectrum(sig: np.ndarray, fs: float) -> tuple[np.ndarray, np.ndarray]:
    w = np.hanning(len(sig))
    X = np.fft.rfft(sig * w)
    freqs = np.fft.rfftfreq(len(sig), 1 / fs)
    mag = 20 * np.log10(np.abs(X) + 1e-12)
    return freqs, mag


def plot_spectra() -> None:
    fs = 48000
    n = 65536
    t = np.arange(n) / fs
    f0 = 997.0  # off-bin to avoid bin-centered leakage dominating
    amplitude = 10 ** (-90 / 20)  # -90 dBFS RMS sine
    x = amplitude * np.sqrt(2) * np.sin(2 * np.pi * f0 * t)

    bits = 16
    full_scale = 1.0
    delta = 2 * full_scale / (2**bits)

    q_plain = quantize_midtread(x, bits, full_scale)
    err_plain = q_plain - x

    d = tpdf_dither(n, delta)
    q_tpdf = quantize_midtread(x + d, bits, full_scale)
    err_tpdf = q_tpdf - x  # non-subtractive: dither stays in signal

    q_shaped, err_shaped = first_order_noise_shape(x, bits, full_scale)

    cases = [
        ("Undithered 16-bit", err_plain),
        ("TPDF dither", err_tpdf),
        ("First-order noise-shaped", err_shaped),
    ]

    fig, axes = plt.subplots(1, 3, figsize=(12, 4), sharey=True)
    for ax, (title, err) in zip(axes, cases):
        f, m = spectrum(err, fs)
        ax.plot(f, m, lw=0.6, color="C0")
        ax.set_xlim(0, 12000)
        ax.set_ylim(-140, -50)
        ax.set_title(title)
        ax.set_xlabel("Frequency [Hz]")
        ax.set_ylabel("Error magnitude [dB]")
        ax.grid(True, alpha=0.3)

    fig.suptitle(
        "Quantization error spectra: -90 dBFS sine, 16-bit, fs = 48 kHz",
        fontsize=11,
    )
    fig.tight_layout()
    out = FIG / "quantization_dither.png"
    fig.savefig(out, dpi=150)
    plt.close(fig)
    print(f"Wrote {out}")


def plot_staircase_3bit() -> None:
    n_show = 80
    t = np.arange(n_show) / 48
    x = 0.6 * np.sin(2 * np.pi * 5 * t)
    q = quantize_midtread(x, bits=3)

    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(t, x, "C0", lw=1.5, label="Input sine")
    ax.step(t, q, "C1", where="mid", lw=1.5, label="3-bit quantized")
    ax.set_xlabel("Time [ms]")
    ax.set_ylabel("Amplitude")
    ax.set_title("3-bit mid-tread quantization — visible stair-steps")
    ax.legend(loc="upper right")
    ax.grid(True, alpha=0.3)
    ax.set_xlim(t[0], t[-1])
    out = FIG / "quantization_staircase_3bit.png"
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)
    print(f"Wrote {out}")


def main() -> None:
    plot_spectra()
    plot_staircase_3bit()


if __name__ == "__main__":
    main()
