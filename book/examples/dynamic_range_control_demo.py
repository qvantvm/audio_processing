#!/usr/bin/env python3
"""Feed-forward compressor static curve demo."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)


def compressor_curve(x_db: np.ndarray, threshold: float = -20.0, ratio: float = 4.0) -> np.ndarray:
    y_db = x_db.copy()
    above = x_db > threshold
    y_db[above] = threshold + (x_db[above] - threshold) / ratio
    return y_db


def main() -> None:
    x_db = np.linspace(-60, 0, 500)
    y_db = compressor_curve(x_db, threshold=-20, ratio=4)

    fig, ax = plt.subplots(figsize=(6, 5))
    ax.plot(x_db, x_db, "k--", alpha=0.4, label="Unity")
    ax.plot(x_db, y_db, color="#1565c0", lw=2, label="Compressor 4:1 @ -20 dBFS")
    ax.set_xlabel("Input level [dBFS]")
    ax.set_ylabel("Output level [dBFS]")
    ax.set_title("Dynamic range control — static curve")
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_aspect("equal")
    out = FIG / "compressor_curve.png"
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
