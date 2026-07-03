"""Delay lines and physical-modeling primitives."""

from __future__ import annotations

import numpy as np


class DelayLine:
    """Circular delay buffer."""

    def __init__(self, max_delay: int):
        self.buffer = np.zeros(max_delay + 1, dtype=np.float32)
        self.max_delay = max_delay
        self.write_pos = 0

    def read(self, delay: int) -> float:
        delay = int(np.clip(delay, 0, self.max_delay))
        idx = (self.write_pos - delay) % len(self.buffer)
        return float(self.buffer[idx])

    def write(self, sample: float) -> None:
        self.buffer[self.write_pos] = sample
        self.write_pos = (self.write_pos + 1) % len(self.buffer)


def karplus_strong(
    fs: float,
    f0: float,
    duration_s: float,
    decay: float = 0.996,
    excitation: str = "noise",
) -> np.ndarray:
    """Karplus–Strong plucked-string synthesis.

    Representation: traveling waves in a closed delay loop + averaging filter.
    decay in (0, 1] controls energy loss per round trip (higher = longer ring).
    """
    period = max(2, int(round(fs / f0)))
    n_out = int(round(duration_s * fs))
    if excitation == "noise":
        buf = np.random.uniform(-1.0, 1.0, period).astype(np.float64)
    else:
        buf = np.zeros(period, dtype=np.float64)
        buf[0] = 1.0
    out = np.zeros(n_out, dtype=np.float64)
    for i in range(n_out):
        y = buf[0]
        out[i] = y
        avg = decay * 0.5 * (buf[0] + buf[1])
        buf = np.roll(buf, -1)
        buf[-1] = avg
    peak = np.max(np.abs(out))
    if peak > 0:
        out /= peak
    return out.astype(np.float32)
