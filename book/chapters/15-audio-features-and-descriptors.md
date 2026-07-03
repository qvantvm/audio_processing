# Audio Features and Descriptors {#ch-15-features}

## Purpose

Machine listening and music informatics reduce waveforms to **feature vectors**: timbral, temporal, and spectral summaries for classification, search, and MIR. This chapter surveys common descriptors— spectral centroid, rolloff, flux, MFCC preview— and how STFT ([STFT, Spectrograms, and Time–Frequency Analysis](#ch-08-stft)) choices affect them.

## Learning Objectives

By the end of this chapter, the reader should be able to:

1. Compute frame-wise **spectral centroid**, **bandwidth**, **rolloff**
2. Define **spectral flux** and **zero-crossing rate**
3. Outline **MFCC** pipeline (Mel filterbank + DCT)
4. Relate feature stability to STFT/window parameters
5. Evaluate features for invariance (level, pitch shift) at high level

## Main Concepts

### Frame-based pipeline

STFT ([STFT, Spectrograms, and Time–Frequency Analysis](#ch-08-stft)) → $|X_m[k]|$ → per-frame scalar or vector features → time series or aggregated statistics [@muller2015fundamentals].

### Spectral centroid

Center of mass of magnitude spectrum:

$$
C_m = \frac{\sum_k f_k |X_m[k]|}{\sum_k |X_m[k]|}.
$$

Correlates with "brightness."

### Spectral rolloff

Frequency below which e.g. 85% of frame energy lies— timbre/sharpness cue.

### Spectral flux

$$
\mathrm{flux}_m = \sum_k \bigl||X_m[k]| - |X_{m-1}[k]|\bigr|^2
$$

(onset/harmonic change indicator).

### Zero-crossing rate

Count sign changes per frame— noisy/unvoiced speech cue; crude pitch period hint at low frequencies.

### MFCC (outline)

1. Power spectrum $|X_m[k]|^2$
2. **Mel filterbank** ([Musical Signal Representations](#ch-17-musical-reps) Mel scale)
3. Log compress
4. **DCT** → decorrelated coefficients

Widely used in speech/music ML; not magically perceptual— know limitations.

### Chroma / constant-Q (preview)

**Chroma:** energy folded onto 12 pitch classes— harmony analysis ([Musical Signal Representations](#ch-17-musical-reps)).

**CQT:** log-spaced frequency resolution for music [@muller2015fundamentals].

## Mathematical Formulation

Mel scale (approx):

$$
\mathrm{mel} = 2595 \log_{10}\left(1 + \frac{f}{700}\right).
$$

Feature vector $\mathbf{f}_m \in \mathbb{R}^d$ per frame; temporal delta $\Delta \mathbf{f}_m$ often appended for ASR.

## Audio Interpretation

**Bright hi-hat:** high centroid, high rolloff.

**Bass note:** low centroid; flux low during sustain.

**Onset:** flux peak; used in beat tracking front-ends.

## Implementation Notes

```python
import librosa
cent = librosa.feature.spectral_centroid(y=x, sr=fs)
mfcc = librosa.feature.mfcc(y=x, sr=fs, n_mfcc=13)
```

Document `n_fft`, `hop_length` with published features— reproducibility matters.

## Worked Example

**Problem:** Two frames same level; frame A energy concentrated at 4 kHz, frame B at 500 Hz. Which has higher centroid?

**Answer:** Frame A.

## Common Pitfalls

1. **Features without level normalization** when comparing clips.
2. **Different STFT settings** invalidating cross-dataset comparison.
3. **Treating MFCC as pitch-invariant** (not fully).
4. **Confusing power vs magnitude** before log.

## Exercises

1. Compute centroid manually from small synthetic spectrum.
2. Plot flux on recording with hand claps; locate onsets.
3. Compare ZCR on voiced vs unvoiced speech (if available).
4. Why log before DCT in MFCC?

## Further Reading

- Müller [@muller2015fundamentals]
- Rabiner & Schafer speech features [@rabiner2010theory]

**Next chapter:** [Pitch, Onsets, and Rhythm](#ch-16-pitch-onsets).