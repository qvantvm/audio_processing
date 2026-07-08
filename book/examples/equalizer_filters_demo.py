#!/usr/bin/env python3
"""Parametric EQ biquad magnitude response demo."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import iirpeak, freqz

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)


def main() -> None:
    fs = 48000
    f0 = 1000.0
    q = 2.0
    b, a = iirpeak(f0 / (fs / 2), q)
    w, h = freqz(b, a, worN=4096, fs=fs)
    mag_db = 20 * np.log10(np.abs(h) + 1e-12)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(w, mag_db, color="#1565c0")
    ax.set_xlim(20, 20000)
    ax.set_xscale("log")
    ax.set_xlabel("Frequency [Hz]")
    ax.set_ylabel("Magnitude [dB]")
    ax.set_title(f"Parametric peaking EQ: {f0:.0f} Hz, Q={q}")
    ax.grid(True, which="both", alpha=0.3)
    out = FIG / "parametric_eq_response.png"
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
