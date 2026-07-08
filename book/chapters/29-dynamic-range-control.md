# Dynamic Range Control {#ch-29-dynamic-range}

## Purpose

[Chapter 13](#ch-13-envelopes-loudness) introduced envelopes and basic compression. This chapter
treats **dynamic range control (DRC)** comprehensively: **static curves**, **level measurement**,
**attack/release**, **limiter/compressor/expander/noise gate**, **multiband** and **dynamic EQ**,
**source-filter DRC**, and stereo-linked processing.

## Learning Objectives

By the end of this chapter, the reader should be able to:

1. Draw **compressor/limiter/expander** static curves with threshold, ratio, knee
2. Implement **feed-forward** level detection with attack/release time constants
3. Build **multiband DRC** with crossover filter bank
4. Explain **dynamic equalizers** and **source-filter** loudness methods
5. Handle **stereo linking** and **true-peak** aware limiting

## Main Concepts

### Static curve

**Compressor:** above threshold $T$, output level grows as input to power $1/R$ (ratio $R$).
**Limiter:** large $R$, fast attack. **Expander** increases dynamic range below threshold.
**Noise gate:** hard expander to $-\infty$ dB.

### Dynamic behavior

**Level measurement:** peak, RMS, or **true peak** (oversampled) detectors
([Testing, Measurement, and Numerical Pitfalls](#ch-21-testing-pitfalls)).

**Gain smoothing:**

$$
g[n] = \alpha_a g[n-1] + (1-\alpha_a) g_{\text{target}}[n] \quad \text{(attack)}
$$

Separate $\alpha_a,\alpha_r$ for attack vs release — asymmetry prevents pumping.

### Implementation variants

| Processor | Role |
|-----------|------|
| Limiter | Peak protection, mastering ceiling |
| Compressor | Reduce crest factor |
| Expander | Restore dynamics after compression |
| Noise gate | Remove bleed between phrases |

**Combination systems** chain gate → compressor → limiter in broadcast chains.

### Multiband DRC

Split with [multi-complementary filter bank](#ch-27-equalizers); independent detectors per band;
recombine. Controls **spectral pumping** (bass triggers treble gain reduction).

### Dynamic equalizers

EQ gain tracks envelope— e.g. de-ess when 5–8 kHz energy exceeds threshold.

### Source-filter DRC

Separate **source** (excitation) from **filter** (spectral envelope) in speech/music models;
apply DRC to source envelope while preserving timbral filter— reduces **breath pumping** in speech
enhancement.

```bash
python examples/dynamic_range_control_demo.py
```

## Realization aspects

**Sampling-rate reduction** for sidechain saves CPU; **curve approximation** via lookup tables;
**stereo processing** via max(L,R) or mean-linked detection.

## Common Pitfalls

1. **Release too fast** on full-band compressor — audible pumping.
2. **No true-peak limiter** before lossy codec — intersample peaks clip.
3. **Independent L/R detection** — image shifts.

## Exercises

1. Plot I/O curve: threshold −20 dBFS, ratio 4:1, soft knee 3 dB.
2. Convert attack 5 ms to $\alpha$ at 48 kHz.
3. Why multiband on broadcast dialog?
4. Sketch source-filter block diagram for speech DRC.

## Further Reading

- Zölzer [@zoelzer2011dafx]
- ITU/EBU loudness standards [@itu2015bs1770; @ebu2011r128]

**Next chapter:** [Audio Coding and Psychoacoustics](#ch-30-audio-coding).
