#!/usr/bin/env python3
"""Correctness tests for audio_toolkit (not just smoke tests)."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK))

from audio_toolkit import effects, filters, meter, osc, spectral  # noqa: E402


def test_fft_roundtrip() -> None:
    rng = np.random.default_rng(0)
    x = rng.standard_normal(1024).astype(np.float32)
    y = np.fft.ifft(np.fft.fft(x)).real.astype(np.float32)
    err = np.max(np.abs(x - y))
    assert err < 1e-5, f"FFT round-trip error {err}"


def test_parseval() -> None:
    rng = np.random.default_rng(1)
    x = rng.standard_normal(512).astype(np.float64)
    x -= x.mean()
    X = np.fft.fft(x)
    time_energy = np.sum(x * x)
    freq_energy = np.sum(np.abs(X) ** 2) / len(x)
    rel = abs(time_energy - freq_energy) / time_energy
    assert rel < 1e-10, f"Parseval relative error {rel}"


def test_stft_istft_reconstruction() -> None:
    fs = 48000.0
    t = np.arange(4800) / fs
    x = (0.5 * np.sin(2 * np.pi * 440 * t)).astype(np.float32)
    n_fft = 512
    hop = 128
    s, _, _ = spectral.stft(x, fs, n_fft=n_fft, hop=hop)
    y = spectral.istft(s, fs, n_fft=n_fft, hop=hop, length=len(x))
    err = np.sqrt(np.mean((x - y) ** 2))
    assert err < 0.04, f"STFT/ISTFT RMSE {err} (tightened from smoke 0.05)"


def test_stft_istft_cola_energy() -> None:
    """Hann with 75% overlap should preserve energy within tight tolerance."""
    fs = 48000.0
    rng = np.random.default_rng(2)
    x = rng.standard_normal(4096).astype(np.float32)
    n_fft, hop = 512, 128
    s, _, _ = spectral.stft(x, fs, n_fft=n_fft, hop=hop)
    y = spectral.istft(s, fs, n_fft=n_fft, hop=hop, length=len(x))
    rel = np.linalg.norm(x - y) / np.linalg.norm(x)
    assert rel < 0.02, f"COLA relative L2 error {rel}"


def test_wav_io_roundtrip() -> None:
    import tempfile

    from audio_toolkit.io import read_wav, write_wav

    fs = 48_000
    x = np.sin(2 * np.pi * 440 * np.arange(fs // 10) / fs).astype(np.float32) * 0.5
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "roundtrip.wav"
        write_wav(path, x, fs)
        y, fs2 = read_wav(path)
        assert fs2 == fs
        snr = 20 * np.log10(np.linalg.norm(x) / (np.linalg.norm(x - y) + 1e-12))
        assert snr > 40, f"WAV round-trip SNR {snr} dB"


def test_fir_lowpass_attenuates_high() -> None:
    fs = 48000.0
    h = filters.design_fir_lowpass(fs, 1000.0, num_taps=127)
    freqs, mag = filters.frequency_response(h, fs)
    pass_gain = (
        mag[freqs == 500.0][0] if np.any(freqs == 500.0) else mag[np.argmin(np.abs(freqs - 500))]
    )
    stop_gain = mag[np.argmin(np.abs(freqs - 10000.0))]
    assert pass_gain > 0.8 and stop_gain < 0.2, f"FIR response pass={pass_gain}, stop={stop_gain}"


def test_oscillator_phase_continuity() -> None:
    fs = 48000.0
    f0 = 440.0
    osc_obj = osc.PhaseOscillator(fs, f0, amplitude=0.8)
    a = osc_obj.render(1000)
    b = osc_obj.render(1000)
    joined = np.concatenate([a, b])
    single = osc.sine_block(fs, f0, 2000, amplitude=0.8)
    rmse = np.sqrt(np.mean((joined - single) ** 2))
    assert rmse < 1e-4, f"phase-continuous blocks RMSE {rmse}"


def test_window_coherent_gain() -> None:
    n_fft = 1024
    cg = spectral.coherent_gain("hann", n_fft)
    assert 0.4 < cg < 0.6, f"Hann coherent gain {cg} (expect ~0.5)"


def test_dbfs_conversions() -> None:
    a = meter.dbfs_to_linear(-3.0)
    assert abs(a - 10 ** (-3 / 20)) < 1e-9
    assert abs(meter.linear_to_dbfs(a) - (-3.0)) < 1e-9


def test_karplus_strong_decay() -> None:
    fs = 48000.0
    y = effects.karplus_strong(fs, 220.0, 0.5, decay=0.995)
    w = int(fs // 10)
    energy_early = np.sum(y[:w] ** 2)
    energy_late = np.sum(y[-w:] ** 2)
    assert energy_early > energy_late * 2, "Karplus-Strong should decay"


def test_resample_preserves_tone() -> None:
    from audio_toolkit.resample import resample

    fs_in, f0 = 44_100.0, 440.0
    n = np.arange(int(fs_in))
    x = np.sin(2 * np.pi * f0 * n / fs_in).astype(np.float32)
    y, fs_out = resample(x, fs_in, 48_000.0)
    spec = np.abs(np.fft.rfft(y))
    freqs = np.fft.rfftfreq(len(y), d=1.0 / fs_out)
    peak_f = freqs[int(np.argmax(spec[1:])) + 1]
    assert abs(peak_f - f0) < 1.0


def test_resample_recommended_quality() -> None:
    from audio_toolkit._quality import ImplQuality
    from audio_toolkit.resample import resample

    fs_in, f0 = 44_100.0, 1000.0
    n = np.arange(int(fs_in * 2))
    x = np.sin(2 * np.pi * f0 * n / fs_in).astype(np.float32)
    y, fs_out = resample(x, fs_in, 48_000.0, quality=ImplQuality.RECOMMENDED)
    spec = np.abs(np.fft.rfft(y))
    freqs = np.fft.rfftfreq(len(y), d=1.0 / fs_out)
    peak_f = freqs[int(np.argmax(spec[1:])) + 1]
    assert abs(peak_f - f0) < 0.25, f"recommended SRC peak {peak_f} Hz vs {f0}"


def test_wavetable_pitch() -> None:
    from audio_toolkit.synthesis import wavetable_osc

    fs = 48_000.0
    f0 = 440.0
    y = wavetable_osc(fs, f0, int(fs * 0.1))
    corr = np.correlate(y, y, mode="full")
    corr = corr[len(y) - 1 :]
    lag_min, lag_max = int(fs / f0) - 5, int(fs / f0) + 5
    peak_lag = lag_min + int(np.argmax(corr[lag_min:lag_max]))
    est_f0 = fs / peak_lag
    assert abs(est_f0 - f0) < 20, f"wavetable pitch estimate {est_f0} vs {f0}"


def test_toolkit_capstone_pipeline() -> None:
    """Synthesize → filter → meter → STFT → WAV round-trip (Chapter 22)."""
    import tempfile

    from audio_toolkit.io import read_wav, write_wav

    fs = 48_000.0
    tone = osc.PhaseOscillator(fs, 440.0, amplitude=0.6).render(int(fs * 0.2))
    h = filters.design_fir_lowpass(fs, 2000.0, num_taps=31)
    filtered = filters.apply_fir(tone, h)
    pk = meter.peak_amplitude(filtered)
    assert 0.0 < pk <= 0.6

    s, freqs, times = spectral.stft(filtered, fs, n_fft=512, hop=128)
    assert s.shape[0] == len(freqs) and s.shape[1] == len(times)

    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "capstone.wav"
        write_wav(path, filtered, int(fs))
        y, fs2 = read_wav(path)
        assert fs2 == int(fs)
        rmse = float(np.sqrt(np.mean((filtered - y) ** 2)))
        assert rmse < 0.01, f"capstone WAV RMSE {rmse}"


def test_audio_toolkit_cli() -> None:
    import subprocess
    import tempfile

    book = Path(__file__).resolve().parent.parent
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "cli_tone.wav"
        r = subprocess.run(
            [
                sys.executable,
                "-m",
                "audio_toolkit",
                "tone",
                str(out),
                "--f0",
                "440",
                "--duration",
                "0.05",
            ],
            cwd=book,
            capture_output=True,
            text=True,
        )
        assert r.returncode == 0, r.stderr or r.stdout
        assert out.is_file()
        analyze = subprocess.run(
            [sys.executable, "-m", "audio_toolkit", "analyze", str(out)],
            cwd=book,
            capture_output=True,
            text=True,
        )
        assert analyze.returncode == 0, analyze.stderr or analyze.stdout
        assert "peak:" in analyze.stdout

        filtered = Path(tmp) / "cli_filtered.wav"
        filt = subprocess.run(
            [
                sys.executable,
                "-m",
                "audio_toolkit",
                "filter",
                str(out),
                str(filtered),
                "--cutoff",
                "200",
                "--taps",
                "31",
            ],
            cwd=book,
            capture_output=True,
            text=True,
        )
        assert filt.returncode == 0, filt.stderr or filt.stdout
        assert filtered.is_file()


TESTS = [
    test_fft_roundtrip,
    test_parseval,
    test_stft_istft_reconstruction,
    test_stft_istft_cola_energy,
    test_wav_io_roundtrip,
    test_fir_lowpass_attenuates_high,
    test_oscillator_phase_continuity,
    test_window_coherent_gain,
    test_dbfs_conversions,
    test_karplus_strong_decay,
    test_resample_preserves_tone,
    test_resample_recommended_quality,
    test_wavetable_pitch,
    test_toolkit_capstone_pipeline,
    test_audio_toolkit_cli,
]


def main() -> int:
    failures = []
    for test in TESTS:
        name = test.__name__
        try:
            test()
            print(f"OK  {name}")
        except Exception as exc:
            failures.append(f"FAIL {name}: {exc}")
            print(failures[-1])
    if failures:
        return 1
    print(f"All {len(TESTS)} correctness tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
