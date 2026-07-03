#!/usr/bin/env python3
"""Verified numeric answers for Chapter 18 exercises."""

from __future__ import annotations

import math
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))

from audio_toolkit.synthesis import wavetable_osc  # noqa: E402


def main() -> int:
    fs = 48_000.0
    f0_a440 = 440.0
    period = fs / f0_a440
    assert 108 < period < 110

    # Worked example in ch 18: f0 = 1000 Hz phase increment
    inc = 2 * math.pi * 1000.0 / fs
    assert abs(inc - 0.1309) < 0.001

    # granular: 50 ms grains, 50% overlap -> hop 25 ms -> 40 grains/s
    grain_s, overlap = 0.05, 0.5
    hop_s = grain_s * (1 - overlap)
    grains_per_sec = 1.0 / hop_s
    assert abs(grains_per_sec - 40.0) < 1e-9

    y = wavetable_osc(fs, f0_a440, 512)
    assert len(y) == 512

    print("Chapter 18 solutions: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
