#!/usr/bin/env python3
"""Verified numeric answers for Chapter 07 exercises."""

from __future__ import annotations

import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))

from audio_toolkit.spectral import coherent_gain  # noqa: E402


def main() -> int:
    n_fft = 1024
    cg = coherent_gain("hann", n_fft)
    assert 0.49 < cg < 0.51, cg
    print("Chapter 07 solutions: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
