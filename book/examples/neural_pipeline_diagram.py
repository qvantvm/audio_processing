#!/usr/bin/env python3
"""Neural audio pipeline diagram (Chapter 20)."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(11, 2.8))
ax.set_xlim(0, 11)
ax.set_ylim(0, 2.8)
ax.axis("off")
ax.set_title("Typical neural audio pipeline (spectrogram-domain)")

boxes = [
    (0.2, "WAV\nx[n]"),
    (1.5, "STFT /\nmel"),
    (3.0, "Encoder\n(CNN/U-Net)"),
    (4.8, "Latent /\nmask"),
    (6.5, "Decoder /\nvocoder"),
    (8.2, "mel /\nwaveform"),
    (9.5, "WAV\nŷ[n]"),
]
xs = [b[0] for b in boxes]
for x, label in boxes:
    ax.add_patch(
        FancyBboxPatch((x, 0.9), 1.0, 0.9, boxstyle="round,pad=0.04", fc="#f3e5f5", ec="#333")
    )
    ax.text(x + 0.5, 1.35, label, ha="center", va="center", fontsize=8)

for x0, x1 in zip(xs[:-1], xs[1:]):
    ax.add_patch(FancyArrowPatch((x0 + 1.05, 1.35), (x1, 1.35), arrowstyle="->", mutation_scale=10))

ax.text(
    5.5,
    0.25,
    "Phase / resampling / sample-rate mismatches are common failure points",
    ha="center",
    fontsize=8,
)

out = FIG / "neural_audio_pipeline.png"
fig.tight_layout()
fig.savefig(out, dpi=150)
print(f"Wrote {out}")
