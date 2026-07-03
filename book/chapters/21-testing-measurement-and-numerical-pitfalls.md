# Testing, Measurement, and Numerical Pitfalls {#ch-21-testing-pitfalls}

## Purpose

Correct DSP code still fails from **numerical issues**, **wrong assumptions**, and **untested edge cases**. This chapter collects practices for verifying filters, transforms, levels, and implementations— essential before shipping audio software or publishing measurements.

## Learning Objectives

By the end of this chapter, the reader should be able to:

1. Design **unit tests** for LTI systems (impulse, sine, energy)
2. Detect **aliasing**, **clipping**, and **DC offset** in pipelines
3. Apply **Parseval** and round-trip FFT/STFT checks
4. Measure **THD+N**, frequency response, and group delay experimentally
5. Avoid **denormals**, coefficient quantization, and intersample peaks

## Main Concepts

### Impulse and sine tests

Feed $\delta[n]$ → capture $h[n]$ ([Convolution and Impulse Responses](#ch-09-convolution)). Feed sine at bin center → measure gain/phase vs $H(\Omega)$ prediction ([Filters: FIR, IIR, and the Z-Transform](#ch-10-filters)).

### Round-trip tests

`ifft(fft(x)) ≈ x` ([DFT, FFT, and Spectral Analysis](#ch-06-dft-fft)). STFT with COLA synthesis window → reconstruct within tolerance ([STFT, Spectrograms, and Time–Frequency Analysis](#ch-08-stft)).

### Level safety

Peak, RMS, true-peak (oversampled) meters; headroom before integer export ([Envelopes, Loudness, and Dynamics](#ch-13-envelopes-loudness)).

### THD+N (concept)

Sine through system; notch fundamental; measure remaining power— harmonic distortion + noise floor.

### Common numerical pitfalls

| Issue | Symptom | Mitigation |
|-------|---------|------------|
| Denormals | CPU spikes on silence | flush-to-zero, DC offset |
| IIR limit cycles | idle tone | dither states, higher precision |
| Circular convolution | echo wrap | pad FFT convolution ([Convolution and Impulse Responses](#ch-09-convolution)) |
| Intersample peaks | clip after "safe" peak meter | true-peak oversampling |
| Aliasing | wrong spectra / timbre | band-limit; verify $f_s$ ([Sampling, Quantization, and Digital Audio](#ch-03-sampling-quantization)) |
| Wrong $f_s$ | pitch/filter wrong | assert metadata |

### Regression testing audio

Store small golden WAV + expected spectra/features; CI compares SNR/ max diff thresholds (not bitwise float equality).

### Listening tests

ABX for perceptual changes algorithms miss— compression artifacts, pre-ringing, phasing.

## Mathematical Formulation

Parseval check (NumPy):

$$
\sum_n |x[n]|^2 \stackrel{?}{\approx} \frac{1}{N}\sum_k |X[k]|^2.
$$

Relative error threshold e.g. $<10^{-10}$ for float64 FFT of moderate $N$.

## Audio Interpretation

**Mastering chain:** verify true-peak $< -1$ dBTP for streaming specs.

**Filter plugin:** sweep sine log-spaced, compare $|H(\Omega)|$ to design.

**ML inference:** silent input should not produce NaNs or full-scale buzz.

## Implementation Notes

```python
import numpy as np
def test_parseval(x):
    X = np.fft.fft(x)
    err = np.sum(np.abs(x)**2) - np.sum(np.abs(X)**2)/len(x)
    assert np.abs(err) < 1e-8 * np.sum(np.abs(x)**2)
```

Use `pytest`, property-based tests (`hypothesis`) for random small vectors.

## Worked Example

**Problem:** `ifft(fft(x))` max error $10^{-3}$ on float32 length 8192. Acceptable?

**Answer:** Often no for production DSP— investigate scaling convention or promote to float64 for critical paths; error may grow with $N$.

## Common Pitfalls

1. **Testing only silence/DC.**
2. **Single-frequency tests missing wideband behavior.**
3. **Ignoring stereo coupling/crosstalk.**
4. **Comparing plots by eye without metrics.**

## Exercises

1. Write impulse test verifying `convolve(x,h)` vs `firwin` design.
2. Measure group delay of your FIR lowpass vs theory (`examples/fir_lowpass_demo.py`, [Filters: FIR, IIR, and the Z-Transform](#ch-10-filters)).
3. Inject DC; high-pass at 20 Hz; verify removal.
4. Design CI golden file test for STFT feature shape.

## Further Reading

- Steiglitz [@steiglitz1996dsp]
- Oppenheim & Schafer numerical topics [@oppenheim2010discrete]

**Next chapter:** [Building a Small Audio DSP Toolkit](#ch-22-dsp-toolkit).