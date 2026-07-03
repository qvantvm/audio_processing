# Building a Small Audio DSP Toolkit {#ch-22-dsp-toolkit}

## Purpose

This capstone chapter documents the **`audio_toolkit/`** package shipped with the book— importable
modules for I/O, oscillators, spectra, filters, effects, and metering, with correctness tests in
`tests/test_correctness.py`. It is the executable backbone tying prior chapters to tested code.

## Representation lens

| Module | Representation | Preserves / discards |
|--------|----------------|----------------------|
| `io` | PCM samples + $f_s$ metadata | Waveform; file header semantics |
| `osc` | Phase state + sinusoid params | Phase continuity across blocks |
| `spectral` | STFT complex matrix | Time–frequency energy; phase optional |
| `filters` | FIR $h[n]$ | LTI frequency shaping |
| `effects` | Delay-line / waveguide state | Resonance, echo, pluck decay |
| `meter` | Scalar levels (peak, RMS, dBFS) | Loudness proxies; not SPL |

## Learning Objectives

By the end of this chapter, the reader should be able to:

1. Import and use `audio_toolkit` modules with explicit `fs`
2. Run correctness tests (FFT round-trip, Parseval, STFT reconstruction, FIR response)
3. Build a pipeline: synthesize or load → filter → meter → write WAV
4. Extend one component (reverb, pitch tracker) with tests first
5. Relate each module to the representation comparison matrix ([Chapter 1](#ch-01-what-is-asp))

## Package layout

The following modules exist in the repository (not a sketch):

```text
book/audio_toolkit/
  __init__.py
  io.py          # read_wav / write_wav (scipy.io.wavfile)
  osc.py         # PhaseOscillator, sine_block
  spectral.py    # stft, istft, coherent_gain
  filters.py     # design_fir_lowpass, apply_fir, frequency_response
  effects.py     # DelayLine, karplus_strong
  meter.py       # peak, RMS, dBFS conversions
  synthesis.py   # wavetable_osc, naive_saw (artifact)
  resample.py    # resample(), midi_to_hz (pedagogical SRC)
book/tests/
  test_correctness.py   # FFT, Parseval, STFT, FIR, phase, dBFS, Karplus, capstone pipeline
book/solutions/
  ch01_verify.py …      # tested numeric exercise answers
```

Run tests from `book/`:

```bash
python tests/test_correctness.py
python solutions/run_verifications.py
python tests/run_examples.py
```

## IO layer (`audio_toolkit.io`)

```python
from audio_toolkit.io import read_wav, write_wav

x, fs = read_wav("input.wav")   # float32 in [-1, 1]
write_wav("output.wav", x, fs)
```

Never assume hard-coded rate downstream— pass `fs` to every time-based function.

## Oscillators (`audio_toolkit.osc`)

`PhaseOscillator` carries phase across blocks to avoid seam clicks ([Chapter 2](#ch-02-signals-time-
samples)):

```python
from audio_toolkit.osc import PhaseOscillator

osc = PhaseOscillator(fs=48_000, f0=440.0, amplitude=0.8)
block_a = osc.render(512)
block_b = osc.render(512)  # phase continues
```

## Spectral layer (`audio_toolkit.spectral`)

```python
from audio_toolkit.spectral import stft, istft

s, freqs, times = stft(x, fs, n_fft=1024, hop=256)
y = istft(s, fs, n_fft=1024, hop=256, length=len(x))
```

Document `n_fft`, `hop`, and window; verify reconstruction with `test_correctness.py`.

## Filters (`audio_toolkit.filters`)

```python
from audio_toolkit.filters import design_fir_lowpass, apply_fir

h = design_fir_lowpass(fs, cutoff_hz=1000.0, num_taps=101)
y = apply_fir(x, h)
```

## Effects (`audio_toolkit.effects`)

`DelayLine` supports comb/all-pass chains; `karplus_strong` implements the [Chapter
19](#ch-19-physical-modeling) waveguide loop.

## Metering (`audio_toolkit.meter`)

```python
from audio_toolkit.meter import peak_amplitude, rms, linear_to_dbfs

pk = peak_amplitude(x)
level_dbfs = linear_to_dbfs(pk)
```

## Integration example pipeline

```python
from audio_toolkit.filters import apply_fir, design_fir_lowpass
from audio_toolkit.io import read_wav, write_wav
from audio_toolkit.meter import linear_to_dbfs, peak_amplitude

x, fs = read_wav("input.wav")
h = design_fir_lowpass(fs, 80.0)
y = apply_fir(x, h)
peak = peak_amplitude(y)
if peak > 0:
    y = 0.89 * y / peak  # ~−1 dBFS headroom
write_wav("output.wav", y, fs)
print("peak dBFS:", linear_to_dbfs(peak_amplitude(y)))
```

## Worked Example

**Project:** `analyze_note.py` using toolkit modules— report $f_0$ (autocorrelation), spectral
centroid, crest factor on a monophonic WAV; ground-truth test on synthetic 440 Hz sine from
`PhaseOscillator`.

**Verification:** `tests/test_correctness.py` must pass before adding chain complexity.

## Common Pitfalls

1. **Monolithic scripts** without importable modules— hard to test.
2. **Implicit globals** for $f_s$.
3. **Smoke tests only**— add invariants (Parseval, round-trip STFT).
4. **Copy-paste FFT** with inconsistent window normalization.

## Exercises

1. Round-trip a WAV through `read_wav`/`write_wav`; estimate SNR.
2. Add Schroeder reverb using `DelayLine`; tune comb delays for ~1 s RT60.
3. Wire `karplus_strong_demo.py` output through `write_wav` and listen.
4. Add a CLI entry point: `python -m audio_toolkit` (optional packaging exercise).

*Selected solutions: [Appendix — Exercise Solutions](#ch-23-exercise-solutions).*

## Further Reading

- [Signals, Time, and Samples](#ch-02-signals-time-samples) through [Testing, Measurement, and Numerical Pitfalls](#ch-21-testing-pitfalls)
- SciPy signal tutorial
- Smith online books [@smith2010physical; @smith2011spectral]

**Epilogue:** Extend the toolkit along your application axis— MIR features, live DSP, or neural
front-ends— while keeping representations and units explicit.
