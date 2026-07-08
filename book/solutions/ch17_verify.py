#!/usr/bin/env python3
"""Verified numeric answers for Chapter 17 exercises."""

from __future__ import annotations

import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))

from audio_toolkit.resample import midi_to_hz  # noqa: E402


def main() -> int:
    # 17.1 MIDI notes
    assert abs(midi_to_hz(69) - 440.0) < 1e-6
    assert abs(midi_to_hz(81) - 880.0) < 1e-6

    # 17.3 STFT vs CQT spacing sketch: at 100 Hz STFT bins coarser than CQT in bass
    fs, n_fft = 48_000, 2048
    stft_bin = fs / n_fft
    assert stft_bin > 20  # ~23.4 Hz
    # CQT would use narrower bins near 100 Hz (conceptual)
    assert 100 / stft_bin < 5  # only a few STFT bins under 100 Hz region

    print("Chapter 17 solutions: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
