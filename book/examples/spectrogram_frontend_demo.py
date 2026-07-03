#!/usr/bin/env python3
"""Classical spectrogram front-end demo (Chapter 20).

Contrasts waveform samples vs STFT magnitude — the representation neural
models often inherit. No PyTorch required.

Run from book/:
    python examples/spectrogram_frontend_demo.py
"""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))

from audio_toolkit.io import write_wav
from audio_toolkit.spectral import stft
from audio_toolkit.synthesis import wavetable_osc

FS = 48_000
DUR = 0.4
y = wavetable_osc(FS, 440.0, int(DUR * FS))
y += 0.3 * wavetable_osc(FS, 880.0, len(y))

s, freqs, times = stft(y, FS, n_fft=1024, hop=256)

fig, axes = plt.subplots(2, 1, figsize=(8, 5))
t = np.arange(len(y)) / FS
axes[0].plot(t, y, linewidth=0.6)
axes[0].set_ylabel("x[n]")
axes[0].set_title("Waveform representation (samples)")
axes[0].grid(True, alpha=0.3)

im = axes[1].pcolormesh(times, freqs, 20 * np.log10(np.abs(s) + 1e-8), shading="auto")
axes[1].set_ylabel("Hz")
axes[1].set_xlabel("Time (s)")
axes[1].set_title("STFT magnitude (classical front-end for many neural models)")
axes[1].set_ylim(0, 5000)
fig.colorbar(im, ax=axes[1], label="dB")
fig.tight_layout()

fig_dir = BOOK / "figures"
fig_dir.mkdir(parents=True, exist_ok=True)
fig.savefig(fig_dir / "spectrogram_frontend.png", dpi=150)

audio_dir = BOOK / "audio_demos"
audio_dir.mkdir(parents=True, exist_ok=True)
write_wav(audio_dir / "two_tone_for_stft.wav", y, FS)
print(f"Wrote {fig_dir / 'spectrogram_frontend.png'}")
print(f"Wrote {audio_dir / 'two_tone_for_stft.wav'}")
