# Musical Signal Representations

## Purpose

Music-specific representations exploit **harmonicity**, **pitch classes**, and **log-frequency** hearing. This chapter covers sinusoidal modeling, chroma, Mel and constant-Q transforms, and sparse partial tracking— bridges between spectral analysis and synthesis/analysis of pitched audio.

## Learning Objectives

By the end of this chapter, the reader should be able to:

1. Represent steady tones as **sinusoidal partials** $(A_k, f_k, \phi_k)$
2. Compute **chroma** features folding Hz onto 12 pitch classes
3. Explain **Mel** scale motivation and filterbank construction
4. Contrast **STFT** vs **CQT** frequency grids for music
5. Identify when sinusoidal models break (noise, transients)

## Main Concepts

### Sinusoidal model

$$
x[n] \approx \sum_k A_k[n] \cos\bigl(2\pi f_k[n] n / f_s + \phi_k[n]\bigr).
$$

**Peak tracking** across STFT frames → partial trajectories [@serra1990sms].

### Harmonic series

For pitch $f_0$, partials at $k f_0$ (approximately for many instruments). **Inharmonicity** (piano strings) stretches partial spacing.

### Chroma

Collapse STFT bins to 12 bins (C, C#, …, B) via mapping $f \mapsto \text{pitch class}$— **chord and key** features, octave-invariant.

### Mel filterbank

Triangular filters spaced on Mel scale approximate auditory spacing; used in MFCC (Chapter 15) and some timbre models.

### Constant-Q transform (CQT)

Center frequencies $f_k = f_{\min} 2^{k/Q}$; bandwidth proportional to center— better note resolution in bass than fixed STFT [@muller2015fundamentals].

### Spectral modeling synthesis (SMS)

Sinusoids + noise residual for analysis/resynthesis— hybrid representation.

## Mathematical Formulation

Mel:

$$
m = 2595 \log_{10}(1 + f/700).
$$

Chroma vector $\mathbf{c} \in \mathbb{R}^{12}$ from weighted sum of $|X_m[k]|$ by pitch class mapping.

## Audio Interpretation

**Piano note:** many harmonics; piano-specific inharmonicity model improves resynthesis.

**Guitar chord:** multiple $f_0$; chroma strong, monophonic pitch fails.

**Orchestral tutti:** dense partials + noise; sparse models struggle without segmentation.

## Implementation Notes

```python
import librosa
chroma = librosa.feature.chroma_stft(y=x, sr=fs)
C = librosa.cqt(x, sr=fs, fmin=librosa.note_to_hz('C1'))
```

Sinusoidal analysis: `sweep`/`tracker` research code; commercial spectral editors.

## Worked Example

**Problem:** $f_0=440$ Hz. Write first four harmonic frequencies.

**Answer:** 440, 880, 1320, 1760 Hz (ideal harmonic; real strings deviate slightly).

## Common Pitfalls

1. **Applying chroma to unpitched percussion**— weak semantics.
2. **STFT for bass note separation**— poor frequency resolution at low $f$.
3. **Ignoring transient segment** in sinusoidal-only model.
4. **Confusing MIDI note number** with $f_0$ conversion ($440 \cdot 2^{(n-69)/12}$).

## Exercises

1. Convert MIDI note 69 to Hz; note 81?
2. Build 12-bin chroma from synthetic major triad spectrum sketch.
3. Compare STFT vs CQT bin spacing at 100 Hz and 2000 Hz (same $f_s$).
4. When does additive sinusoidal resynthesis fail audibly?

## Further Reading

- Roads [@roads1996computer]
- Müller [@muller2015fundamentals]
- Serra & Smith, spectral modeling synthesis [@serra1990sms]

**Next chapter:** Chapter 18 — *Synthesis Representations*.
