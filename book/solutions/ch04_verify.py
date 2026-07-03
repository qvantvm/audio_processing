#!/usr/bin/env python3
"""Verified numeric answers for Chapter 04 exercises."""

from __future__ import annotations

import math
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))


def main() -> int:
    omega = math.pi / 8
    n = 10
    re = 2 * math.cos(omega * n)
    im = 2 * math.sin(omega * n)
    assert abs(math.hypot(re, im) - 2.0) < 1e-9
    assert abs(re - 2 * math.cos(5 * math.pi / 4)) < 1e-9
    assert abs(im - 2 * math.sin(5 * math.pi / 4)) < 1e-9
    print("Chapter 04 solutions: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
