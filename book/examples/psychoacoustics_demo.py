#!/usr/bin/env python3
"""Psychoacoustic absolute threshold and simplified masking demo."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)


def ath(freq_hz: np.ndarray) -> np.ndarray:
    """Approximate absolute threshold of hearing [dB SPL], Fletcher-like."""
    f_khz = np.maximum(freq_hz, 20) / 1000.0
    return (
        3.64 * (f_khz ** -0.8)
        - 6.5 * np.exp(-0.6 * (f_khz - 3.3) ** 2)
        + (f_khz / 1000.0) ** 4
    )


def main() -> None:
    freqs = np.logspace(np.log10(20), np.log10(20000), 500)
    ath_db = ath(freqs)

    masker_hz = 1000.0
    spread = 0.02 * (freqs - masker_hz) ** 2
    masking = 40 - spread  # simplified V-shaped mask around 40 dB masker

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.semilogx(freqs, ath_db, label="Absolute threshold (approx.)", color="#424242")
    ax.semilogx(freqs, masking, label="Masking spread @ 1 kHz, 40 dB", color="#c62828")
    ax.set_xlabel("Frequency [Hz]")
    ax.set_ylabel("Level [dB SPL]")
    ax.set_title("Psychoacoustic hearing threshold and masking (schematic)")
    ax.set_xlim(20, 20000)
    ax.set_ylim(-10, 90)
    ax.legend()
    ax.grid(True, which="both", alpha=0.3)
    out = FIG / "psychoacoustics_masking.png"
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
