#!/usr/bin/env python3
"""Verified numeric answers for Chapter 02 exercises."""

from __future__ import annotations

import math
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))

from audio_toolkit import meter  # noqa: E402


def main() -> int:
    # 2.1
    assert 44100 * 0.05 == 2205
    # 2.2
    omega = 2 * math.pi * 1000 / 48000
    assert abs(omega - math.pi / 24) < 1e-12
    # 2.3
    a = meter.dbfs_to_linear(-3.0)
    assert abs(a - 0.707945784384381) < 1e-6
    # 2.4
    fs, f0 = 48000, 440.0
    p = fs / f0
    n = math.ceil(2 * p)
    assert n == 219
    # 2.5
    assert 96000 // 2 == 48000
    assert 48000 / 48000 == 1.0
    print("Chapter 02 solutions: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
