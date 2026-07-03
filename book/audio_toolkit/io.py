"""WAV I/O with explicit sample-rate metadata."""

from __future__ import annotations

from pathlib import Path
from typing import Tuple, Union

import numpy as np
from scipy.io import wavfile

PathLike = Union[str, Path]


def read_wav(path: PathLike) -> Tuple[np.ndarray, int]:
    """Read a WAV file to float32 in [-1, 1].

    Returns (samples, fs). Mono is 1-D; stereo is (n_samples, 2).
    """
    fs, data = wavfile.read(path)
    if data.dtype == np.int16:
        x = data.astype(np.float32) / 32768.0
    elif data.dtype == np.int32:
        x = data.astype(np.float32) / 2147483648.0
    elif np.issubdtype(data.dtype, np.floating):
        x = data.astype(np.float32)
    else:
        raise ValueError(f"Unsupported WAV dtype: {data.dtype}")
    return x, int(fs)


def write_wav(path: PathLike, x: np.ndarray, fs: int) -> None:
    """Write float audio to 16-bit PCM WAV."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    peak = np.max(np.abs(x))
    if peak > 1.0:
        x = x / peak
    pcm = np.clip(x * 32767.0, -32768, 32767).astype(np.int16)
    wavfile.write(path, fs, pcm)
