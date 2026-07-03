"""Phase-continuous oscillators."""

from __future__ import annotations

import numpy as np


class PhaseOscillator:
    """Sine oscillator with carried phase for block-wise synthesis."""

    def __init__(self, fs: float, f0: float, amplitude: float = 1.0, phase: float = 0.0):
        self.fs = float(fs)
        self.f0 = float(f0)
        self.amplitude = float(amplitude)
        self._phase = float(phase)

    @property
    def phase(self) -> float:
        return self._phase

    def render(self, num_samples: int) -> np.ndarray:
        n = np.arange(num_samples, dtype=np.float64)
        inc = 2.0 * np.pi * self.f0 / self.fs
        x = self.amplitude * np.cos(self._phase + inc * n)
        self._phase = (self._phase + inc * num_samples) % (2.0 * np.pi)
        return x.astype(np.float32)


def sine_block(
    fs: float,
    f0: float,
    num_samples: int,
    amplitude: float = 1.0,
    phase: float = 0.0,
    n_start: int = 0,
) -> np.ndarray:
    """Generate a sine block with explicit phase continuity at n_start."""
    n = n_start + np.arange(num_samples, dtype=np.float64)
    return (amplitude * np.cos(2.0 * np.pi * f0 * n / fs + phase)).astype(np.float32)
