#!/usr/bin/env python3
"""Modal resonator bank diagram (Chapter 19)."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(9, 3))
ax.set_xlim(0, 9)
ax.set_ylim(0, 3)
ax.axis("off")
ax.set_title("Modal synthesis: sum of damped resonators")

ax.add_patch(FancyBboxPatch((0.2, 1.1), 0.9, 0.7, boxstyle="round", fc="#e8f0fe"))
ax.text(0.65, 1.45, "excitation", ha="center", va="center", fontsize=8)

for i, (x, label) in enumerate([(2.0, "mode 1"), (3.6, "mode 2"), (5.2, "mode 3")]):
    ax.add_patch(FancyBboxPatch((x, 0.8), 1.2, 1.2, boxstyle="round", fc="#fff3e0"))
    ax.text(x + 0.6, 1.4, f"{label}\nresonator", ha="center", va="center", fontsize=8)
    ax.add_patch(FancyArrowPatch((1.1, 1.45), (x, 1.45), arrowstyle="->", mutation_scale=8))
    ax.add_patch(FancyArrowPatch((x + 1.2, 1.45), (6.8, 1.45), arrowstyle="->", mutation_scale=8))

ax.add_patch(FancyBboxPatch((6.8, 1.1), 0.9, 0.7, boxstyle="round", fc="#e8f5e9"))
ax.text(7.25, 1.45, "Σ", ha="center", va="center", fontsize=12)
ax.add_patch(FancyBboxPatch((8.0, 1.1), 0.8, 0.7, boxstyle="round", fc="#e8f5e9"))
ax.text(8.4, 1.45, "y[n]", ha="center", va="center", fontsize=9)
ax.annotate("", xy=(8.0, 1.45), xytext=(7.7, 1.45), arrowprops=dict(arrowstyle="->"))

out = FIG / "modal_bank.png"
fig.tight_layout()
fig.savefig(out, dpi=150)
print(f"Wrote {out}")
