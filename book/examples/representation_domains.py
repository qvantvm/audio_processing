#!/usr/bin/env python3
"""Representation domains overview diagram (book figure).

Run from book/: python examples/representation_domains.py
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")

boxes = [
    (0.5, 3.5, "Time domain\n$x[n]$ samples"),
    (2.8, 3.5, "Frequency domain\n$|X[k]|$, $\\angle X[k]$"),
    (5.1, 3.5, "Time–frequency\nSTFT $|X_m[k]|$"),
    (7.4, 3.5, "Parametric\npartials, MFCC, latent"),
]
for x, y, label in boxes:
    rect = mpatches.FancyBboxPatch((x, y), 2.0, 1.6, boxstyle="round,pad=0.05", fc="#e8f0fe", ec="#3366cc")
    ax.add_patch(rect)
    ax.text(x + 1.0, y + 0.8, label, ha="center", va="center", fontsize=9)

arrows = [(2.5, 4.3, 2.8, 4.3), (4.8, 4.3, 5.1, 4.3), (7.1, 4.3, 7.4, 4.3)]
for x1, y1, x2, y2 in arrows:
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="->", color="0.4"))

ax.text(5, 2.2, "Transforms & models link representations (DFT, filters, features, ML)", ha="center", fontsize=10)
ax.text(5, 5.3, "Audio signal representation domains", ha="center", fontsize=12, fontweight="bold")

out = FIG / "representation_domains.png"
fig.savefig(out, dpi=150, bbox_inches="tight")
print(f"Wrote {out}")
