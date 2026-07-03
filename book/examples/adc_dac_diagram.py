#!/usr/bin/env python3
"""ADC/DAC capture-playback chain diagram."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(11, 2.5))
ax.set_xlim(0, 11)
ax.set_ylim(0, 2.5)
ax.axis("off")

labels = [
    "Acoustic\nsource",
    "Microphone\nx(t)",
    "Anti-alias\nLPF",
    "ADC\nsample",
    "x[n] DSP",
    "y[n]",
    "DAC\nhold",
    "Recon\nLPF",
    "Speaker",
]
xs = [0.2, 1.2, 2.3, 3.4, 4.6, 5.7, 6.8, 7.9, 9.0]
for x, label in zip(xs, labels):
    ax.add_patch(
        FancyBboxPatch((x, 0.7), 0.85, 0.9, boxstyle="round,pad=0.04", fc="#f5f5f5", ec="#333")
    )
    ax.text(x + 0.425, 1.15, label, ha="center", va="center", fontsize=8)

for x0, x1 in zip(xs[:-1], xs[1:]):
    ax.add_patch(FancyArrowPatch((x0 + 0.9, 1.15), (x1, 1.15), arrowstyle="->", mutation_scale=10))

ax.set_title("Digital audio chain: continuous ↔ discrete representations")
out = FIG / "adc_dac_chain.png"
fig.tight_layout()
fig.savefig(out, dpi=150)
print(f"Wrote {out}")
