#!/usr/bin/env python3
"""Comb and all-pass structure diagrams (Chapter 11)."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)

fig, axes = plt.subplots(1, 2, figsize=(10, 3))

# Feedforward comb
ax = axes[0]
ax.set_xlim(0, 6)
ax.set_ylim(0, 3)
ax.axis("off")
ax.set_title("Feedforward comb: y = x + g·delay(x)")
for x, label in [(0.3, "x[n]"), (2.0, "z^{-D}"), (3.5, "Σ"), (4.8, "y[n]")]:
    ax.add_patch(FancyBboxPatch((x, 1.1), 0.9, 0.7, boxstyle="round", fc="#e8f0fe"))
    ax.text(x + 0.45, 1.45, label, ha="center", va="center", fontsize=9)
ax.text(1.2, 2.0, "g", fontsize=10)
ax.annotate("", xy=(2.0, 1.45), xytext=(1.2, 1.45), arrowprops=dict(arrowstyle="->"))
ax.annotate("", xy=(3.5, 1.45), xytext=(1.2, 1.45), arrowprops=dict(arrowstyle="->"))
ax.annotate("", xy=(3.5, 1.45), xytext=(2.9, 1.45), arrowprops=dict(arrowstyle="->"))
ax.annotate("", xy=(4.8, 1.45), xytext=(4.4, 1.45), arrowprops=dict(arrowstyle="->"))

# All-pass
ax = axes[1]
ax.set_xlim(0, 6)
ax.set_ylim(0, 3)
ax.axis("off")
ax.set_title("All-pass: |H| ≈ 1, phase varies")
ax.add_patch(FancyBboxPatch((0.3, 1.1), 0.9, 0.7, boxstyle="round", fc="#e8f0fe"))
ax.text(0.75, 1.45, "x[n]", ha="center", va="center", fontsize=9)
ax.add_patch(FancyBboxPatch((2.2, 1.0), 1.6, 0.9, boxstyle="round", fc="#fff3e0"))
ax.text(3.0, 1.45, "AP filter", ha="center", va="center", fontsize=9)
ax.add_patch(FancyBboxPatch((4.5, 1.1), 0.9, 0.7, boxstyle="round", fc="#e8f5e9"))
ax.text(4.95, 1.45, "y[n]", ha="center", va="center", fontsize=9)
ax.annotate("", xy=(2.2, 1.45), xytext=(1.2, 1.45), arrowprops=dict(arrowstyle="->"))
ax.annotate("", xy=(4.5, 1.45), xytext=(3.8, 1.45), arrowprops=dict(arrowstyle="->"))
ax.text(3.0, 0.4, "|H(e^{jΩ})| ≈ 1", ha="center", fontsize=8)

out = FIG / "comb_allpass_structures.png"
fig.tight_layout()
fig.savefig(out, dpi=150)
print(f"Wrote {out}")
