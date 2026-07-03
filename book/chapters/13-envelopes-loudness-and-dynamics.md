# Envelopes, Loudness, and Dynamics {#ch-13-envelopes-loudness}

## Purpose

Sample values oscillate quickly; **perception** responds to slower **envelopes**, **level**, and **loudness**. Dynamics processors (compressors, limiters) operate on envelope followers. This chapter defines RMS/peak metering, introduces loudness standards preview, and connects digital dBFS to perceptual level.

## Learning Objectives

By the end of this chapter, the reader should be able to:

1. Compute **peak**, **RMS**, and smoothed **envelope** of a signal
2. Distinguish **dBFS**, **dB SPL**, and **LUFS** (conceptual)
3. Sketch a feed-forward **compressor** (threshold, ratio, attack, release)
4. Explain crest factor and headroom
5. Avoid clipping while maximizing perceived loudness in mastering context

## Main Concepts

### Peak and RMS

Peak: $\max_n |x[n]|$. RMS:

$$
\mathrm{RMS} = \sqrt{\frac{1}{N}\sum_{n=0}^{N-1} x[n]^2}.
$$

Sine peak $A$ → RMS $A/\sqrt{2}$. **Crest factor** = peak/RMS (dB difference).

### Envelope followers

Rectify ($|x[n]|$ or $x[n]^2$), low-pass or peak-hold smoothing:

$$
e[n] = \alpha e[n-1] + (1-\alpha)|x[n]|.
$$

Attack/release times set $\alpha$ from time constants and $f_s$.

### Compressor

If level $e[n] > T$, apply gain reduction with ratio $R$:

$$
g[n] = \begin{cases}
1 & e[n] \le T \\
\left(\frac{e[n]}{T}\right)^{1/R - 1} & e[n] > T
\end{cases}
$$

(simplified; implementations vary). **Limiter** → high ratio, low threshold.

### Loudness (LUFS preview)

ITU-R BS.1770 and EBU R128 define **K-weighting**, gating, and integrated loudness in **LUFS** for broadcast and streaming loudness matching [@itu2015bs1770; @ebu2011r128].

Not identical to RMS or peak; includes frequency weighting.

### dBFS vs SPL

dBFS references digital full scale. SPL requires acoustic calibration chain. No fixed conversion without sensitivity and gain staging.

## Mathematical Formulation

Decibels:

$$
L_{\mathrm{dBFS,peak}} = 20\log_{10}\left(\frac{\max |x[n]|}{1.0}\right).
$$

Power average:

$$
L_{\mathrm{dBFS,RMS}} = 20\log_{10}(\mathrm{RMS}).
$$

## Audio Interpretation

**Vocal compression:** reduce crest factor, raise average level, control peaks.

**Mastering limiter:** cap true peak (intersample peaks need oversampling check— [Testing, Measurement, and Numerical Pitfalls](#ch-21-testing-pitfalls)).

**Podcast:** target −16 LUFS mono / −14 LUFS stereo (platform norms vary).

## Implementation Notes

```python
rms = np.sqrt(np.mean(x**2))
peak = np.max(np.abs(x))
# envelope
alpha = np.exp(-1/(tau * fs))
e = np.zeros_like(x)
for n in range(1, len(x)):
    e[n] = alpha * e[n-1] + (1-alpha) * abs(x[n])
```

Libraries: `pyloudnorm`, DAW meters.

## Worked Example

**Problem:** Peak −3 dBFS sine. RMS in dBFS?

**Answer:** Peak linear $10^{-3/20}\approx0.708$; RMS $0.708/\sqrt{2}$ → $20\log_{10}(0.501)\approx -6.02$ dBFS.

## Common Pitfalls

1. **Confusing peak and loudness** for complex music.
2. **Fast attack** crushing transients; **slow release** pumping.
3. **Clipping after limiter** without true-peak detection.
4. **Applying SPL labels** to uncalibrated digital buffers.

## Exercises

1. Measure crest factor of speech vs snare hit (use sample file or synthetic).
2. Design envelope follower with 10 ms attack at 48 kHz ($\alpha$?).
3. Compressor threshold −20 dBFS, ratio 4:1, input −8 dBFS— output level sketch?
4. Why K-weighting for LUFS?

## Further Reading

- Zölzer, *DAFX* dynamics chapter [@zoelzer2011dafx]
- ITU-R BS.1770 loudness measurement [@itu2015bs1770]
- EBU R128 loudness normalisation [@ebu2011r128]

**Next chapter:** [Resampling, Interpolation, and Sample-Rate Conversion](#ch-14-resampling).