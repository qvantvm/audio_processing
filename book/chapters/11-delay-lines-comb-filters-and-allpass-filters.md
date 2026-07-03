# Delay Lines, Comb Filters, and All-Pass Filters {#ch-11-delay-comb-allpass}

## Purpose

**Delay** is elemental in audio: echo, chorus, flanger, reverb, physical modeling. A **delay line** stores past samples; **comb** and **all-pass** filters combine delayed copies to create coloration and diffusion. This chapter builds the delay-based representations used in effects and reverberators.

## Learning Objectives

By the end of this chapter, the reader should be able to:

1. Implement a **delay line** with integer and fractional delay
2. Analyze feedforward and feedback **comb filters**
3. Explain **all-pass** filters and their phase-only effect
4. Connect comb peaks/notches to delay time and gain
5. Sketch a simple Schroeder reverberator structure

## Main Concepts

### Delay line

$$
y[n] = x[n-D] + \cdots
$$

Circular buffer of length $L \ge D$ stores $D$ samples of history. **Fractional delay** uses interpolation (@sec:ch-14-resampling).

Delay time $\tau = D/f_s$ seconds.

### Feedforward comb

$$
y[n] = x[n] + g\, x[n-D].
$$

Frequency response has **notches** at $f = k f_s/D$ for integer relationship— **comb** spectrum.

### Feedback comb

$$
y[n] = x[n] + g\, y[n-D].
$$

Pole locations create **peaks**; $|g|<1$ for stability. Building block of reverberation.

### All-pass filter

$$
H(z) = \frac{z^{-D} + g}{1 + g z^{-D}} \quad \text{or related forms}.
$$

$|H(\Omega)| \approx 1$ (unity magnitude), **nonlinear phase**— spreads energy in time without changing magnitude spectrum of steady signals; used in diffusion networks.

### Schroeder reverberator (classic)

Parallel **feedback comb filters** + series **all-pass sections** [@zoelzer2011dafx]— crude but historically foundational.

## Mathematical Formulation

Comb magnitude (feedforward, $g=0.5$, delay $D$):

$$
|H(\Omega)| = \left|1 + g e^{-j\Omega D}\right| = \sqrt{1 + g^2 + 2g\cos(\Omega D)}.
$$

Notches when $\cos(\Omega D)=-1$ → $\Omega D = \pi(2k+1)$.

## Audio Interpretation

**Echo:** single delay tap audible as repetition.

**Flanger:** short modulated delay ($<$20 ms) → comb sweeping.

**Reverb:** dense late field from many combs/all-pass.

## Implementation Notes

```python
# Circular buffer delay
buf = np.zeros(L)
idx = 0
# read buf[(idx-D) % L], write new sample at buf[idx]
```

Modulated delay: interpolate read pointer for chorus/flanger.

## Worked Example

**Problem:** $D=240$ at $f_s=48000$. Delay ms? First notch above DC approximately?

**Answers:** $\tau=5$ ms. Notches near $f_s/(2D)=100$ Hz and harmonics if feedforward comb.

## Common Pitfalls

1. **Unstable feedback** when $|g|\ge 1$.
2. **Click on delay time change** without crossfade.
3. **Integer delay only** causes pitch artifacts in modulated effects— need interpolation.
4. **Confusing comb spacing** formula— depends on feedforward vs feedback sign.

## Exercises

1. Plot $|H(\Omega)|$ for feedforward comb $g=0.7$, $D=100$.
2. Why does all-pass preserve magnitude but smear transients?
3. Design 3 parallel combs with incommensurate delays to avoid periodic metallic ringing.
4. Relate flanger LFO rate to perceived sweep speed.

## Further Reading

- Zölzer, *DAFX* [@zoelzer2011dafx]
- Puckette [@puckette2007electronic]
- Smith, *Physical Audio Signal Processing* [@smith2010physical]

**Next chapter:** @sec:ch-12-phase-group-delay — *Phase, Group Delay, and Minimum Phase*.
