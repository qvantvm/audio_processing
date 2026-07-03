#!/usr/bin/env python3
"""STFT framing block diagram (Chapter 08).

Run from book/: python examples/stft_framing_diagram.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(10, 3))
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis("off")

boxes = [
    (0.3, 1.2, 1.4, 0.9, "x[n]\ninput"),
    (2.2, 1.2, 1.6, 0.9, "× w[n]\nwindow"),
    (4.3, 1.2, 1.6, 0.9, "FFT\nper frame"),
    (6.4, 1.2, 1.8, 0.9, "X_m[k]\nSTFT"),
    (8.6, 1.2, 1.2, 0.9, "|X_m[k]|\noptional"),
]
for x, y, w, h, label in boxes:
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05", fc="#e8f0fe", ec="#333"))
    ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=9)

for x0, x1 in [(1.7, 2.2), (3.8, 4.3), (5.9, 6.4), (8.2, 8.6)]:
    ax.add_patch(FancyArrowPatch((x0, 1.65), (x1, 1.65), arrowstyle="->", mutation_scale=12))

ax.text(5, 0.4, "hop R samples between frames; overlap = (M−R)/M", ha="center", fontsize=9)
ax.set_title("STFT analysis chain (representation: time → time–frequency)")

out = FIG / "stft_framing.png"
fig.tight_layout()
fig.savefig(out, dpi=150)
print(f"Wrote {out}")
