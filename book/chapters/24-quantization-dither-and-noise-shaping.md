# Quantization, Dither, and Noise Shaping {#ch-24-quantization-dither}

## Purpose

[Chapter 3](#ch-03-sampling-quantization) introduced uniform quantization and SQNR. This chapter
goes deeper: **quantization error statistics**, **dither** that decorrelates error from the signal,
**noise shaping** that pushes quantization noise out of the audible band, and **fixed- vs floating-
point** number formats that govern real-time DSP.

## Learning Objectives

By the end of this chapter, the reader should be able to:

1. State the **classical quantization model** and when SQNR formulas apply
2. Explain **dither** (rectangular, triangular, noise-shaped) and its audibility tradeoffs
3. Sketch a **first-order noise shaper** loop for oversampled converters
4. Compare **fixed-point Q-format** vs **IEEE float** for audio algorithms
5. Predict **format-conversion** artifacts (truncation, rounding, clipping)

## Main Concepts

### Classical quantization model

Uniform mid-tread quantizer with step $\Delta$ and $B$ bits:

$$
Q(x) = \Delta \left\lfloor \frac{x}{\Delta} + \frac{1}{2} \right\rfloor.
$$

For large signals, SQNR $\approx 6.02B + 1.76$ dB (sinusoid, full scale). **Quantization error**
$e[n]=Q(x[n])-x[n]$ is bounded in $[-\Delta/2,\Delta/2]$ for mid-tread.

### Quantization theorem and error statistics

Bennett / Widrow results: without dither, error can be **signal-dependent** (harmonic distortion on
low-level tones). With **wide-sense** conditions, error approximates **white noise** of variance
$\Delta^2/12$ when proper dither is added.

### Dither

Add wide-sense dither $d[n]$ before quantize, subtract statistically (or use non-subtractive for
one-pass):

$$
y[n] = Q(x[n] + d[n]).
$$

| Dither type | PDF | Effect |
|-------------|-----|--------|
| Rectangular | uniform $\pm\Delta/2$ | First moment decorrelated |
| Triangular | $\pm\Delta$ | Second moment decorrelated |
| Shaped | filtered noise | Noise moved to high $f$ |

**Tradeoff:** dither raises the noise floor slightly to eliminate **correlated distortion**—
preferred on re-quantization to 16-bit PCM in mastering.

### Noise shaping

In **oversampled** loops (see [AD/DA Conversion and Delta-Sigma](#ch-25-ad-da-conversion)), a
filter $H(z)$ shapes quantization noise $E(z)$:

$$
Y(z) = X(z) + E(z) H(z).
$$

Choose $H(z)$ so $|H(e^{j\Omega})|$ is small in audio band, large at high $\Omega$. **First-order**
shaper: $H(z)=1-z^{-1}$ (differentiation of noise).

### Number representation

**Fixed-point** $Qm.n$: $m$ integer + $n$ fractional bits; multiply accumulates in wider word.
**Floating-point** (IEEE 754): exponent + mantissa; wide dynamic range, nonlinear quantization
steps.

| Format | Pros | Cons |
|--------|------|------|
| int16 PCM | Simple I/O | Limited headroom |
| Q31 on DSP | Deterministic, fast MAC | Scale tracking |
| float32 | Easy prototyping | Denormals, non-associative sums |

**Format conversion:** float→int requires dither + correct scaling; int→float is exact; repeated
round-trip without dither causes **granular distortion** on fades.

## Implementation Notes

Interactive exploration (replaces JS applet):

```bash
python examples/quantization_dither_demo.py
```

Plots spectra of: bare quantization, rectangular dither, triangular dither, and first-order shaped
noise on a low-level sine.

## Worked Example

**Problem:** 24-bit float master truncated to 16-bit without dither on a $-90$ dBFS tone. What
do you hear?

**Answer:** Harmonic lines from signal-dependent quantization— dither would spread error to
broadband hiss near $-96$ dBFS theoretical floor.

## Common Pitfalls

1. **Truncation vs rounding** — asymmetric error bias.
2. **Dither after limiter** — wrong order; dither before final quantize.
3. **Ignoring noise shaping** when analyzing $\Delta\Sigma$ ADCs.

## Exercises

1. Compute SQNR for 8-, 16-, and 24-bit uniform quantizers.
2. Why is triangular dither preferred over rectangular for critical mastering?
3. Sketch $|1-e^{-j\Omega}|$ and explain auditory benefit.
4. When is float32 insufficient for long FIR accumulation?

## Further Reading

- Lipshitz & Wannamaker, dither [@lipshitz1992dither]
- Oppenheim & Schafer [@oppenheim2010discrete]
- Zölzer, *DAFX* [@zoelzer2011dafx]

**Next chapter:** [AD/DA Conversion and Delta-Sigma](#ch-25-ad-da-conversion).
