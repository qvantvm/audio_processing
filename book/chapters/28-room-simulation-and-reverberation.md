# Room Simulation and Reverberation {#ch-28-room-simulation}

## Purpose

**Room simulation** places sources in space via **room impulse responses (RIRs)** and **algorithmic
reverb**. This chapter covers acoustics basics, **measured vs modeled** RIRs, **early reflections**
(Ando, Gerzon), **late reverberation** (Schroeder, FDN), and **RIR approximation**— extending
[Delay Lines, Comb Filters, and All-Pass Filters](#ch-11-delay-comb-allpass) and
[Convolution](#ch-09-convolution).

## Learning Objectives

By the end of this chapter, the reader should be able to:

1. Relate **room acoustics** (RT60, early decay) to RIR structure
2. Contrast **image-source**, **ray**, and **convolution** RIR approaches
3. Implement **early reflection** taps from geometry or measurements
4. Build **Schroeder** and **feedback-delay-network** late reverbs
5. Approximate long RIRs with **parametric + noise** tails

## Main Concepts

### Room impulse responses

RIR $h[n]$ encodes direct path, early reflections, and diffuse tail. **Measurement:** swept sine or
impulse + deconvolution. **Simulation:** image method (simple shoebox), geometric acoustics, or
hybrid.

Convolution reverb: $y[n]=x[n]*h[n]$ — high quality, costly for long halls
([Convolution and Impulse Responses](#ch-09-convolution)).

### Early reflections

**Ando's** psychoacoustic work links early energy pattern to **spaciousness**. **Gerzon** algorithms
place discrete early taps with interaural level/time cues for stereo/binaural rendering.

### Subsequent reverberation

**Schroeder** architecture: parallel combs → series all-pass — classic algorithmic tail
([Delay Lines, Comb Filters, and All-Pass Filters](#ch-11-delay-comb-allpass)).

**General feedback systems / FDN:** unitary feedback matrix + delay lines — dense late field with
controllable modal density.

### Approximation of RIRs

Truncate early part exactly; model tail as **exponentially decaying noise** filtered per band—
reduces memory for games/VR. Neural estimators predict late tail parameters from early RIR snippet
([Neural Audio Representations](#ch-20-neural-audio)).

```bash
python examples/fast_convolution_demo.py   # long RIR convolution
```

## Common Pitfalls

1. **Non-minimum-phase early RIR** — pre-ringing if linear-phase EQ applied wrongly.
2. **Comb filter coloration** from periodic early taps.
3. **Nyquist IR length** — 3 s at 48 kHz is 144k samples per channel.

## Exercises

1. Estimate RT60 from Schroeder integral of $h^2[n]$.
2. Why incommensurate comb delays in Schroeder reverb?
3. Compare measured vs algorithmic CPU at 48 kHz stereo.
4. List Gerzon early-reflection parameters for stereo width.

## Further Reading

- Schroeder [@schroeder1962natural]
- Gerzon [@gerzon1972binaural]
- Zölzer [@zoelzer2011dafx]

**Next chapter:** [Dynamic Range Control](#ch-29-dynamic-range).
