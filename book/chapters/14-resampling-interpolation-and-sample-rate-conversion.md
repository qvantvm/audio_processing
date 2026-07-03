# Resampling, Interpolation, and Sample-Rate Conversion {#ch-14-resampling}

## Purpose

Real systems mix sample rates: 44.1 kHz files on 48 kHz hardware, half-speed processing, varispeed. **Resampling** reconstructs (conceptually) and re-samples with a new $f_s$. This chapter covers interpolation, anti-imaging, and practical SRC quality tradeoffs.

## Learning Objectives

By the end of this chapter, the reader should be able to:

1. State steps of **ideal sample-rate conversion** (filter + interpolate/decimate)
2. Explain **imaging** and **aliasing** in upsampling/downsampling
3. Implement naive vs filtered **integer ratio** conversion conceptually
4. Choose between **polyphase** and **FFT SRC** at high level
5. Apply band-limiting before **downsampling**

## Main Concepts

### Upsampling by $L$

Insert $L-1$ zeros between samples → **images** at multiples of original spectrum. Low-pass **interpolation filter** removes images, fills smooth values.

### Downsampling by $M$

Low-pass to $< f_s/new/2$ then keep every $M$-th sample— prevents aliasing ([Sampling, Quantization, and Digital Audio](#ch-03-sampling-quantization)).

### Arbitrary ratio $f_{s2}/f_{s1}$

Rational approximation $L/M$ or asynchronous SRC with time-varying fractional delay (Farrow structure).

### Fractional delay

Output at non-integer $n$ via **Lagrange**, **sinc**, or **all-pass** interpolation— used in pitch shifting and delay modulation ([Delay Lines, Comb Filters, and All-Pass Filters](#ch-11-delay-comb-allpass)).

### Quality metrics

Stopband rejection, passband ripple, group delay— audibility on transient-rich material ([Phase, Group Delay, and Minimum Phase](#ch-12-phase-group-delay)). **SoX**, **libsamplerate** are reference implementations.

## Mathematical Formulation

Ideal band-limited interpolation:

$$
x(t) = \sum_n x[n]\, \mathrm{sinc}\!\left(\frac{t - nT_s}{T_s}\right), \quad
x[m T_{s2}] \text{ sample at new rate}.
$$

Practical filters approximate sinc with finite length.

## Audio Interpretation

**44.1 → 48 kHz:** common in video workflows; poor SRC causes dullness or aliasing shimmer.

**Half-speed playback:** resample or read buffer slower— different semantics (pitch drops unless compensated).

## Implementation Notes

```python
from scipy.signal import resample_poly
y = resample_poly(x, up=160, down=147)  # example ratio components
```

`librosa.resample`, `soxr` preferred for quality. Always document SRC used in datasets.

## Worked Example

**Problem:** Downsample 48 kHz → 16 kHz by $M=3$. Cutoff frequency before decimation?

**Answer:** Nyquist of output 8 kHz; low-pass below ~7.2 kHz (guard band) before keeping every 3rd sample.

## Common Pitfalls

1. **Decimate without filter** → aliasing.
2. **Upsample zeros without filter** → images audible as high hiss/metallic tone.
3. **Confusing resample with playback speed change.**
4. **Repeated SRC** degrading quality in production chains.

## Exercises

1. Sketch spectra: original, zero-stuffed ×2, filtered.
2. Why polyphase implementation saves computation?
3. Convert 1 s of 440 Hz tone 44.1→48 kHz; verify frequency unchanged (within numerical error).
4. When does asynchronous SRC arise (DAW drift)?

## Further Reading

- Oppenheim & Schafer [@oppenheim2010discrete]
- Smith, resampling topics [@smith2010physical]

**Next chapter:** [Audio Features and Descriptors](#ch-15-features).