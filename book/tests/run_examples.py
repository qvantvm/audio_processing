#!/usr/bin/env python3
"""Run all book examples (smoke test)."""

import subprocess
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))

EXAMPLES = [
    "a440_sine_wave.py",
    "aliasing_demo.py",
    "complex_sinusoid_demo.py",
    "dft_bin_spacing.py",
    "fourier_series_square_wave.py",
    "window_leakage_demo.py",
    "stft_spectrogram_demo.py",
    "fir_lowpass_demo.py",
    "representation_domains.py",
    "karplus_strong_demo.py",
    "wavetable_demo.py",
    "export_audio_demos.py",
    "spectrogram_frontend_demo.py",
    "stft_framing_diagram.py",
    "adc_dac_diagram.py",
    "fir_iir_diagram.py",
    "dft_grid_diagram.py",
    "comb_allpass_diagram.py",
    "phase_group_delay_diagram.py",
    "modal_bank_diagram.py",
    "neural_pipeline_diagram.py",
    "wavetable_diagram.py",
]

failures = []
for name in EXAMPLES:
    path = BOOK / "examples" / name
    if not path.exists():
        failures.append(f"missing {name}")
        continue
    r = subprocess.run([sys.executable, str(path)], cwd=BOOK, capture_output=True, text=True)
    if r.returncode != 0:
        failures.append(f"{name}: {r.stderr or r.stdout}")
    else:
        print(r.stdout.strip())

if failures:
    print("FAILURES:", *failures, sep="\n")
    sys.exit(1)
print("All examples OK")
