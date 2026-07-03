#!/usr/bin/env python3
"""FIR direct form and IIR biquad structure diagrams."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)

fig, axes = plt.subplots(1, 2, figsize=(10, 3))

# FIR direct form
ax = axes[0]
ax.set_xlim(0, 6)
ax.set_ylim(0, 3)
ax.axis("off")
ax.set_title("FIR: feedforward only")
ax.add_patch(FancyBboxPatch((0.2, 1.2), 0.8, 0.6, boxstyle="round", fc="#e8f0fe"))
ax.text(0.6, 1.5, "x[n]", ha="center", va="center", fontsize=9)
for i, b in enumerate(["b₀", "b₁", "b₂"]):
    y = 2.2 - i * 0.5
    ax.add_patch(FancyBboxPatch((1.5, y - 0.2), 0.6, 0.4, boxstyle="round", fc="#fff3e0"))
    ax.text(1.8, y, b, ha="center", va="center", fontsize=9)
    ax.add_patch(FancyArrowPatch((1.0, 1.5), (1.5, y), arrowstyle="->", mutation_scale=8))
ax.add_patch(FancyBboxPatch((3.0, 1.2), 0.8, 0.6, boxstyle="round", fc="#e8f5e9"))
ax.text(3.4, 1.5, "y[n]", ha="center", va="center", fontsize=9)

# IIR biquad
ax = axes[1]
ax.set_xlim(0, 6)
ax.set_ylim(0, 3)
ax.axis("off")
ax.set_title("IIR biquad: feedforward + feedback")
ax.add_patch(FancyBboxPatch((0.2, 1.2), 0.8, 0.6, boxstyle="round", fc="#e8f0fe"))
ax.text(0.6, 1.5, "x[n]", ha="center", va="center", fontsize=9)
ax.add_patch(FancyBboxPatch((2.5, 1.2), 1.2, 0.6, boxstyle="round", fc="#fce4ec"))
ax.text(3.1, 1.5, "Σ + delays", ha="center", va="center", fontsize=9)
ax.add_patch(FancyBboxPatch((4.5, 1.2), 0.8, 0.6, boxstyle="round", fc="#e8f5e9"))
ax.text(4.9, 1.5, "y[n]", ha="center", va="center", fontsize=9)
ax.add_patch(FancyArrowPatch((1.0, 1.5), (2.5, 1.5), arrowstyle="->", mutation_scale=8))
ax.add_patch(FancyArrowPatch((3.7, 1.5), (4.5, 1.5), arrowstyle="->", mutation_scale=8))
ax.annotate("", xy=(2.8, 0.6), xytext=(4.2, 0.6), arrowprops=dict(arrowstyle="->"))
ax.text(3.5, 0.35, "a₁, a₂ feedback", ha="center", fontsize=8)

out = FIG / "fir_iir_structures.png"
fig.tight_layout()
fig.savefig(out, dpi=150)
print(f"Wrote {out}")
