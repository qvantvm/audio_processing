#!/usr/bin/env python3
"""Export hearable WAV demos for key DSP artifacts (Chapters 02–11).

Run from book/:
    python examples/export_audio_demos.py

Writes short clips to audio_demos/ — use headphones at low volume.
"""

from pathlib import Path
import sys

import numpy as np

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))

from audio_toolkit.effects import DelayLine
from audio_toolkit.io import write_wav
from audio_toolkit.osc import PhaseOscillator, sine_block
from audio_toolkit.synthesis import naive_saw

OUT = BOOK / "audio_demos"
OUT.mkdir(parents=True, exist_ok=True)
FS = 48_000
DUR = 0.5


def demo_aliasing() -> None:
    """3500 Hz tone at 4 kHz sample rate folds to 500 Hz."""
    fs = 4000.0
    f0 = 3500.0
    n = np.arange(int(fs * DUR))
    x = 0.8 * np.sin(2 * np.pi * f0 * n / fs).astype(np.float32)
    write_wav(OUT / "aliasing_3500hz_at_4kfs.wav", x, int(fs))
    print(f"aliasing: {f0} Hz at fs={fs} Hz → perceived fold near {fs - f0} Hz")


def demo_phase_click() -> None:
    """Block resets cause clicks; phase continuity does not."""
    f0 = 440.0
    block = 1024
    bad = np.concatenate(
        [sine_block(FS, f0, block, n_start=0), sine_block(FS, f0, block, n_start=0)]
    )
    osc = PhaseOscillator(FS, f0, amplitude=0.8)
    good = np.concatenate([osc.render(block), osc.render(block)])
    write_wav(OUT / "phase_click_bad.wav", bad, int(FS))
    write_wav(OUT / "phase_click_good.wav", good, int(FS))
    print("phase: compare phase_click_bad.wav vs phase_click_good.wav")


def demo_naive_saw_aliasing() -> None:
    """High saw note — harsh aliasing (Ch 18)."""
    y = naive_saw(FS, 2200.0, int(FS * DUR), amplitude=0.5)
    write_wav(OUT / "naive_saw_2200hz.wav", y, int(FS))
    print("saw: naive_saw_2200hz.wav — listen for harsh high-frequency buzz")


def demo_leakage_beating() -> None:
    """Two close tones — hear roughness; spectral analysis shows leakage (Ch 07)."""
    f1, f2 = 440.0, 444.0
    n = np.arange(int(FS * DUR))
    x = 0.4 * (np.sin(2 * np.pi * f1 * n / FS) + np.sin(2 * np.pi * f2 * n / FS))
    write_wav(OUT / "leakage_two_tone_440_444.wav", x.astype(np.float32), int(FS))
    print("leakage: leakage_two_tone_440_444.wav — 4 Hz beating; analyze with rect vs Hann window")


def demo_comb_filter() -> None:
    """Impulse through feedback comb — metallic resonance."""
    delay_samples = 60
    feedback = 0.85
    n = int(FS * DUR)
    x = np.zeros(n, dtype=np.float32)
    x[0] = 1.0
    dl = DelayLine(delay_samples)
    y = np.zeros(n, dtype=np.float32)
    for i in range(n):
        delayed = dl.read(delay_samples)
        sample = x[i] + feedback * delayed
        dl.write(sample)
        y[i] = sample
    peak = np.max(np.abs(y))
    if peak > 0:
        y /= peak
    write_wav(OUT / "comb_resonator.wav", y, int(FS))
    print(f"comb: comb_resonator.wav — delay={delay_samples}, feedback={feedback}")


def main() -> None:
    demo_aliasing()
    demo_phase_click()
    demo_naive_saw_aliasing()
    demo_leakage_beating()
    demo_comb_filter()
    print(f"All demos written to {OUT}/")


if __name__ == "__main__":
    main()
