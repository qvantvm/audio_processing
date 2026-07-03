#!/usr/bin/env python3
"""Verified checks for Chapter 22 capstone exercises."""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

import numpy as np

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))

from audio_toolkit.effects import DelayLine, karplus_strong  # noqa: E402
from audio_toolkit.io import read_wav, write_wav  # noqa: E402


def _wav_snr(x: np.ndarray, y: np.ndarray) -> float:
    err = np.linalg.norm(x - y)
    sig = np.linalg.norm(x)
    return float(20 * np.log10(sig / (err + 1e-12)))


def _parallel_comb_tail(fs: float, n: int, delays_ms: list[float], feedback: float) -> np.ndarray:
    """Parallel comb bank (Schroeder-style building block)."""
    impulse = np.zeros(n, dtype=np.float32)
    impulse[0] = 1.0
    mix = np.zeros(n, dtype=np.float64)
    for delay_ms in delays_ms:
        delay = max(1, int(fs * delay_ms / 1000.0))
        line = DelayLine(delay + 8)
        branch = np.zeros(n, dtype=np.float64)
        for i in range(n):
            delayed = line.read(delay)
            y = impulse[i] + feedback * delayed
            line.write(y)
            branch[i] = y
        mix += branch
    return (mix / len(delays_ms)).astype(np.float32)


def main() -> int:
    fs = 48_000.0
    n = int(fs * 0.5)
    x = (0.5 * np.sin(2 * np.pi * 440 * np.arange(n) / fs)).astype(np.float32)

    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "roundtrip.wav"
        write_wav(path, x, int(fs))
        y, fs2 = read_wav(path)
        assert fs2 == int(fs)
        snr = _wav_snr(x, y)
        assert snr > 40.0, f"WAV SNR {snr} dB"

    # Schroeder-style parallel combs: incommensurate ms delays, ~1 s decay on impulse
    tail = _parallel_comb_tail(fs, int(fs * 1.2), [29, 37, 41, 43], feedback=0.72)
    early = np.sum(tail[: int(fs * 0.1)] ** 2)
    late = np.sum(tail[-int(fs * 0.1) :] ** 2)
    assert early > late * 4

    pluck = karplus_strong(fs, 220.0, 0.25, decay=0.995)
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "pluck.wav"
        write_wav(path, pluck, int(fs))
        back, fs3 = read_wav(path)
        assert fs3 == int(fs) and len(back) == len(pluck)
        assert np.max(np.abs(back - pluck)) < 0.02

    print("Chapter 22 solutions: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
