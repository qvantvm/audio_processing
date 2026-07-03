#!/usr/bin/env python3
"""Automated pre-flight for teaching pilot Run 1 (ch 01–06 foundation block).

This is NOT a substitute for an external human cohort — it verifies that instructor
materials (examples, demos, solutions ch 01–06) run cleanly before recruitment.

Run from repo root: python book/scripts/run_pilot_preflight.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
PILOT_EXAMPLES = [
    "a440_sine_wave.py",
    "aliasing_demo.py",
    "complex_sinusoid_demo.py",
    "fourier_series_square_wave.py",
    "dft_bin_spacing.py",
    "window_leakage_demo.py",
    "stft_spectrogram_demo.py",
]
PILOT_SOLUTIONS = [f"ch{i:02d}_verify.py" for i in range(1, 7)]
PILOT_WAV_DEMOS = [
    "phase_click_bad.wav",
    "phase_click_good.wav",
    "aliasing_3500hz_at_4kfs.wav",
]


def _run(cmd: list[str], *, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)


def main() -> int:
    failures: list[str] = []

    for name in PILOT_EXAMPLES:
        path = BOOK / "examples" / name
        if not path.exists():
            failures.append(f"missing example {name}")
            continue
        r = _run([sys.executable, str(path)], cwd=BOOK)
        if r.returncode != 0:
            failures.append(f"{name}: {r.stderr or r.stdout}")

    export = BOOK / "examples" / "export_audio_demos.py"
    r = _run([sys.executable, str(export)], cwd=BOOK)
    if r.returncode != 0:
        failures.append(f"export_audio_demos: {r.stderr or r.stdout}")

    demos_dir = BOOK / "audio_demos"
    for name in PILOT_WAV_DEMOS:
        if not (demos_dir / name).is_file():
            failures.append(f"missing demo WAV {name}")

    for name in PILOT_SOLUTIONS:
        path = BOOK / "solutions" / name
        r = _run([sys.executable, str(path)], cwd=BOOK)
        if r.returncode != 0:
            failures.append(f"{name}: {r.stderr or r.stdout}")

    figures = [
        "representation_domains.png",
        "a440_samples.png",
        "aliasing_fold.png",
        "dft_grid.png",
        "window_leakage.png",
        "stft_chirp_spectrogram.png",
    ]
    for name in figures:
        if not (BOOK / "figures" / name).is_file():
            failures.append(f"missing figure {name}")

    if failures:
        print("Pilot pre-flight FAILED:")
        for msg in failures:
            print(f"  - {msg}")
        return 1

    print("Pilot pre-flight OK (ch 01–06 materials verified)")
    print("Note: external human cohort still required for polished promotion.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
