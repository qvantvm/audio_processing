# Equalizers, Fast Convolution, and Filter Banks {#ch-27-equalizers}

## Purpose

**Equalizers** are the most common audio filters in production. This chapter unifies **recursive
(IIR) parametric EQ**, **non-recursive (FIR) EQ via fast convolution**, **frequency-sampling
design**, **multi-complementary filter banks**, and **delay-based effects**— extending
[Filters: FIR, IIR, and the Z-Transform](#ch-10-filters) and [Convolution](#ch-09-convolution).

## Learning Objectives

By the end of this chapter, the reader should be able to:

1. Design **parametric peaking/shelf** biquads and assess **coefficient quantization**
2. Implement **fast convolution** (overlap-add/save) for long FIR EQ
3. Build **FIR by frequency sampling** from a target $|H(\Omega)|$
4. Explain **multi-complementary** filter banks (sum of bandpasses ≈ allpass)
5. Relate **delay-based effects** (chorus, flanger) to EQ/filter paths

## Main Concepts

### Recursive (IIR) audio filters

**Parametric EQ:** cascade biquads with continuous gain/frequency/Q controls. **Quantization** of
$a_k,b_k$ causes limit cycles and zipper noise when automating— use **double-precision design**,
**single-precision runtime**, or **stable parameter interpolation**.

### Non-recursive (FIR) and fast convolution

Long FIR EQ (linear-phase mastering) needs **FFT convolution**:

$$
y = \text{IFFT}(\text{FFT}(x)\cdot \text{FFT}(h)).
$$

**Overlap-add** segments input; **overlap-save** uses circular convolution blocks. For IRs $>$
few ms at 48 kHz, FFT methods dominate direct convolution ([Convolution and Impulse
Responses](#ch-09-convolution)).

```bash
python examples/fast_convolution_demo.py
python examples/equalizer_filters_demo.py
```

### Frequency-sampling FIR design

Sample desired $|H_d[k]|$ on DFT grid, inverse FFT → $h[n]$, window/truncate for causal FIR. Good
for arbitrary graphic-EQ curves; watch **Gibbs ripple** without smoothing.

### Multi-complementary filter bank

Bands $H_m(z)$ satisfy $\sum_m |H_m(e^{j\Omega})|^2 \approx 1$ (energy partition). **Eight-band**
example: crossovers for multiband compression ([Dynamic Range Control](#ch-29-dynamic-range)).

### Delay-based audio effects

Short modulated delays implement **chorus/flanger/phaser**— complementary to recursive shelving;
see [Delay Lines, Comb Filters, and All-Pass Filters](#ch-11-delay-comb-allpass).

## Common Pitfalls

1. **IIR automation** without smoothing — zipper noise.
2. **FFT block size** too small — circular wrap artifacts in overlap-add.
3. **Phase mismatch** summing parallel EQ paths.

## Exercises

1. Design peaking biquad +3 dB at 1 kHz, Q=2, $f_s=48$ kHz.
2. Compare direct vs FFT convolution CPU for $N=10^5$ tap IR.
3. Why frequency-sampling needs windowing?
4. Sketch eight-band complementary magnitudes summing flat.

## Further Reading

- Zölzer [@zoelzer2011dafx]
- Smith [@smith2010physical]

**Next chapter:** [Room Simulation and Reverberation](#ch-28-room-simulation).
