# Pitch, Onsets, and Rhythm {#ch-16-pitch-onsets}

## Purpose

**Pitch** (periodicity), **onsets** (note/event starts), and **tempo** (pulse rate) are fundamental
mid-level representations between samples and semantics. This chapter covers autocorrelation/YIN-
style pitch, spectral peak picking refinements, onset detection from flux, and beat tracking
overview.

## Representation lens

| Question | Pitch/onset answer |
|----------|----------------------|
| **What is the representation?** | Curves $\hat{f}_0[n]$, onset times, beat periods |
| **What does it preserve?** | Periodic pitch contour; event timing |
| **What does it discard?** | Timbre detail; polyphony without multi-pitch models |
| **Maps in/out via** | Autocorrelation, YIN, spectral peak picking, onset strength envelopes |
| **Numerical mistakes** | Bin spacing too coarse; octave/doubling errors |
| **Audible artifacts** | Robotic pitch correction; missed/flammed onsets |

## Learning Objectives

By the end of this chapter, the reader should be able to:

1. Relate pitch $f_0$ to period $P = f_s/f_0$ samples
2. Implement naive **autocorrelation** pitch estimate
3. Improve frequency estimates via **parabolic interpolation** on DFT peaks
4. Detect onsets using **spectral flux** or high-frequency content
5. Outline autocorrelation / comb-filter **tempo** estimation

## Main Concepts

### Pitch as fundamental frequency

Monophonic periodic signal: $f_0$ in Hz; harmonics at $k f_0$. **Polyphonic** pitch estimation is
harder (multiple $f_0$).

### Time-domain: autocorrelation

$$
R[\tau] = \sum_n x[n] x[n+\tau].
$$

Peak at $\tau \approx P$ indicates period. Normalization (AMDF, YIN) reduces octave errors
[@muller2015fundamentals].

### Frequency-domain peak picking

From $|X[k]|$, find peak bin $k_{\max}$, interpolate:

$$
k^\* = k_{\max} + \frac{|X[k_{\max}+1]| - |X[k_{\max}-1]|}{2\bigl(2|X[k_{\max}]| - |X[k_{\max}+1]| -
|X[k_{\max}-1]|\bigr)}.
$$

Then $f_0 \approx k^\* \Delta f$— fixes coarse bin error from [DFT, FFT, and Spectral
Analysis](#ch-06-dft-fft).

### Onset detection

Functions: spectral flux ([Audio Features and Descriptors](#ch-15-features)), complex domain
deviation, HFC. **Peak picking** on onset strength envelope with adaptive threshold.

**Audio:** pick note starts for transcription, slicing, rhythm analysis.

### Beat and tempo

Periodic structure in onset envelope or tempogram; autocorrelation at lag corresponding to 60–180
BPM common range.

## Mathematical Formulation

Period–frequency:

$$
f_0 = \frac{f_s}{P}, \qquad \Omega_0 = \frac{2\pi f_0}{f_s}.
$$

Onset strength $o[m]$ per frame; peaks when $o[m] > \theta[m]$.

## Audio Interpretation

**A440 tuning:** $P \approx 109$ samples at 48 kHz— autocorrelation peak there.

**Snare hit:** broadband onset, weak $f_0$.

**Kick drum:** low $f_0$ burst + onset; tempo track from kick/snare pattern.

## Implementation Notes

```python
f0, voiced_flag, voiced_probs = librosa.pyin(x, fmin=80, fmax=400, sr=fs)
onset_frames = librosa.onset.onset_detect(y=x, sr=fs)
```

Validate on monophonic instruments before polyphonic material.

## Worked Example

**Problem:** DFT peak at $k=10$, $\Delta f=46.875$ Hz, parabolic offset $+0.3$ bin. Refined $f_0$?

**Answer:** $f_0 \approx (10.3)(46.875) \approx 482.8$ Hz.

## Common Pitfalls

1. **Octave errors** in autocorrelation (harmonic stronger than fundamental).
2. **Short windows** failing low pitch.
3. **Onset double-triggering** from vibrato.
4. **Confusing tempo with meter** (time signature).

## Exercises

1. Estimate $f_0$ of synthetic 220 Hz sine with/without interpolation.
2. Generate click track; detect onsets and compare to ground truth times.
3. Why YIN uses cumulative mean normalized difference?
4. Plot tempogram sketch for 120 BPM quarter-note clicks.

*Selected solutions: [Appendix — Exercise Solutions](#ch-23-exercise-solutions).*

## Further Reading

- Müller [@muller2015fundamentals]
- de Cheveigné & Kawahara, YIN pitch estimator [@decheveigne2002yin]

**Next chapter:** [Musical Signal Representations](#ch-17-musical-reps).
