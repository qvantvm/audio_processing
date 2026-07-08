# Nonlinear Processing and Virtual Analog {#ch-31-nonlinear-processing}

## Purpose

**Nonlinear processing** creates harmonics, saturation, and timbral color— intentionally (overdrive,
tape) or as artifacts to control. This chapter covers **waveshaping**, **nonlinear filters**,
**aliasing in nonlinear loops**, and **virtual analog** methods including **wave digital filters
(WDF)** and **state-space** discretizations— complementing [Synthesis
Representations](#ch-18-synthesis) and [Physical-Modeling Representations](#ch-19-physical-modeling).

## Learning Objectives

By the end of this chapter, the reader should be able to:

1. Model **overdrive, distortion, clipping** with memoryless and dynamic nonlinearities
2. Analyze **harmonic generation** and **intermodulation**
3. Explain **aliasing** in nonlinear feedback and mitigate via oversampling
4. Sketch **WDF** discretization of a simple R/C network
5. Contrast **state-space** virtual analog vs naive Euler on stiff ODEs

## Main Concepts

### Fundamentals

Nonlinear system: $y[n]=f(x[n],x[n-1],\ldots)$ — no single $H(z)$ applies globally. **Volterra**
series generalizes convolution to multiple orders (rarely implemented fully in real time).

### Overdrive, distortion, clipping

Memoryless curves: $\tanh$, cubic soft clip, asymmetric diode models. **Hard clip** at $\pm 1$
generates odd harmonics; **asymmetric** curves add even harmonics (tube-like warmth).

### Nonlinear filters

State-dependent filters (e.g. **wah** with LFO + resonance) or **feedback** around nonlinearity
(guitar amp): $y = \mathcal{N}(H(z) y + x)$.

### Aliasing and mitigation

Discontinuities and polynomial folds create **above-Nyquist** harmonics that **fold** into audio
band. Mitigations:

- **Oversampling** nonlinear stage ×2–×16
- **BLEP/BLIT** for discontinuous waveforms ([Synthesis Representations](#ch-18-synthesis))
- **Antialiasing filters** before decimation

### Virtual analog modeling

**Wave digital filters:** bilinear transform on **wave variables**; passive networks stay stable as
digital waveguides.

**State-space approaches:** discretize ODEs of analog prototypes (trapezoidal, TPT methods)—
better stiff stability than forward Euler.

```python
import numpy as np

def soft_clip(x, drive=2.0):
    return np.tanh(drive * x) / np.tanh(drive)

# Oversample wrapper
def oversampled_nonlin(x, fs, nonlin, osr=4):
    from scipy.signal import resample_poly
    x_up = resample_poly(x, osr, 1)
    y_up = nonlin(x_up)
    return resample_poly(y_up, 1, osr)
```

## Common Pitfalls

1. **Single-rate tanh** on rich input — metallic aliasing.
2. **Unstable feedback** around saturating gain > 1.
3. **Confusing WDF** with generic biquad — port resistances matter.

## Exercises

1. Spectrum of hard-clipped sine — which harmonics dominate?
2. Why oversample only the nonlinearity, not entire mix?
3. Draw WDF one-port resistor adaptor.
4. Compare Euler vs trapezoidal on stiff RC at 48 kHz.

## Further Reading

- Zölzer [@zoelzer2011dafx]
- Pakarinen & Yeh, virtual analog [@pakarinen2009virtual]
- Smith, WDF topics [@smith2010physical]

**Next chapter:** [Physical-Modeling Representations](#ch-19-physical-modeling).
