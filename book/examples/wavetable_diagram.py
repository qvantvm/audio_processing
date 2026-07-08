#!/usr/bin/env python3
"""Wavetable oscillator block diagram (Chapter 18)."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(10, 3))
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis("off")
ax.set_title("Wavetable synthesis: phase pointer reads interpolated table")

boxes = [
    (0.2, "phase\naccumulator"),
    (2.0, "table index\n+ interp"),
    (4.0, "wavetable\none period"),
    (6.0, "× amplitude"),
    (7.8, "y[n]"),
]
for x, label in boxes:
    ax.add_patch(
        FancyBboxPatch((x, 0.9), 1.3, 1.0, boxstyle="round,pad=0.04", fc="#e8f0fe", ec="#333")
    )
    ax.text(x + 0.65, 1.4, label, ha="center", va="center", fontsize=8)

xs = [b[0] for b in boxes]
for x0, x1 in zip(xs[:-1], xs[1:]):
    ax.add_patch(FancyArrowPatch((x0 + 1.35, 1.4), (x1, 1.4), arrowstyle="->", mutation_scale=10))

ax.text(
    5.0,
    0.25,
    "inc = f0/fs per sample; table stores band-limited cycle template",
    ha="center",
    fontsize=8,
)

out = FIG / "wavetable_structure.png"
fig.tight_layout()
fig.savefig(out, dpi=150)
print(f"Wrote {out}")
