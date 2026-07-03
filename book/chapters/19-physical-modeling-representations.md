# Physical-Modeling Representations {#ch-19-physical-modeling}

## Purpose

**Physical modeling** simulates vibrating structures and acoustic coupling: strings, tubes, membranes, excitations. Representations are often **partial differential equations** discretized (FDTD, waveguides) or **compact resonator banks** (modal). This chapter orients readers to delay-line/waveguide models and excitation–resonance–radiation framing.

## Learning Objectives

By the end of this chapter, the reader should be able to:

1. Sketch **excitation → resonator → radiation** pipeline
2. Explain **digital waveguide** string model (bi-directional delays + filters)
3. Contrast ** lumped modal** vs **distributed waveguide** approaches
4. Relate **impedance** and boundary conditions to filter coefficients (conceptual)
5. Identify stability and tuning issues in discretized models

## Main Concepts

### Excitation–resonance–radiation

**Excitation:** bow, pick, breath noise. **Resonator:** string/bore modes. **Radiation:** body filter (often extra delay/FIR) [@smith2010physical]. Builds on delay lines ([Delay Lines, Comb Filters, and All-Pass Filters](#ch-11-delay-comb-allpass)) and filters ([Filters: FIR, IIR, and the Z-Transform](#ch-10-filters)).

### Digital waveguide string

Two delay lines (forward/backward traveling waves), loop filters for loss/dispersion, fractional delay tuning:

$$
y^+[n] = \text{filter}\bigl(y^+[n-1], y^-[n]\bigr), \quad \text{similar for } y^-.
$$

Output sum at bridge/end point.

### Waveguide acoustic tube (wind)

Cylindrical bore sections as delays; junctions as scattering matrices (Kelly–Lochbaum); reed/lip excitation nonlinear.

### Modal synthesis

Sum of damped sinusoids:

$$
y[n] = \sum_k r_k^n \sin(\Omega_k n + \phi_k)
$$

or parallel second-order resonators— efficient for struck objects (bars, bowls).

### Finite difference (FDTD)

Discretize wave equation on grid— flexible geometry, higher CPU; stability requires Courant condition $\Delta t \le \Delta x / c$.

### Nonlinearities

Bow friction, reed threshold, valve— make model expressive; complicate analysis and aliasing control ([Sampling, Quantization, and Digital Audio](#ch-03-sampling-quantization)).

## Mathematical Formulation

1D wave equation:

$$
\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}.
$$

Discrete traveling-wave decomposition $u = y^+ + y^-$ motivates waveguides.

## Audio Interpretation

**Plucked string:** burst excitation + decaying harmonics with inharmonicity optional.

**Brass:** bore resonances + lip buzz; bore length sets pitch.

**Percussion plate:** dense modal partials with inharmonic ratios.

## Implementation Notes

Start with Smith's `stk` or Julius O. Smith tutorials for waveguide primitives. Modal: design bank of biquads from measured partial frequencies/decays.

## Worked Example

**Problem:** String delay line round-trip $D=200$ samples at $f_s=48000$. Fundamental approximately?

**Answer:** Two delays (there and back) relate to period; simplified monolithic delay $D$ gives $f_0 \approx f_s/D = 240$ Hz (exact tuning uses dispersion filters and fractional delay).

## Common Pitfalls

1. **Unstable loop gain** in waveguide filters.
2. **Aliasing from nonlinear excitation** without oversampling.
3. **Tuning drift** with temperature simulated poorly (dispersion error).
4. **Confusing physical units** in FDTD ($c$, grid spacing).

## Exercises

1. Draw waveguide string block diagram with loop filter.
2. Modal: three partials at 400, 1020, 1840 Hz with different decays— describe timbre.
3. Why fractional delay needed for accurate pitch? ([Resampling, Interpolation, and Sample-Rate Conversion](#ch-14-resampling))
4. Compare CPU: 10-modal vs 1-waveguide string note.

## Further Reading

- Smith, *Physical Audio Signal Processing* [@smith2010physical]
- Roads [@roads1996computer]

**Next chapter:** [Neural Audio Representations](#ch-20-neural-audio).