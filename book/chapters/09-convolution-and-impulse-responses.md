# Convolution and Impulse Responses {#ch-09-convolution}

## Purpose

Filtering, reverberation, and equalization are often implemented as **convolution** of an input
signal with an **impulse response (IR)**. This chapter defines discrete convolution, connects it to
LTI systems, and explains why IRs are a central audio representation— from cabinet modeling to
algorithmic reverb.

## Representation lens

| Question | Impulse-response answer |
|----------|-------------------------|
| **What is the representation?** | Discrete impulse response $h[n]$ of an LTI system |
| **What does it preserve?** | Complete LTI behavior: every input mapped by same $h[n]$ |
| **What does it discard?** | Non-LTI effects (compression, saturation); time-varying systems |
| **Maps in/out via** | Convolution $y=x*h$; frequency domain $Y=HX$ |
| **Numerical mistakes** | Circular vs linear convolution; wrong `mode` at edges |
| **Audible artifacts** | Wraparound echoes; pre-ringing from linear-phase IRs |

## Learning Objectives

By the end of this chapter, the reader should be able to:

1. Compute discrete convolution $(x * h)[n]$ and interpret its length
2. Explain the impulse response $h[n]$ of an LTI system
3. Relate convolution in time to multiplication in frequency (DTFT/DFT view)
4. Implement FIR filtering via `np.convolve` and via FFT overlap-add (concept)
5. Recognize when convolution is impractical and **partitioned** methods are needed

## Main Concepts

### Discrete convolution

$$
y[n] = (x * h)[n] = \sum_{m=-\infty}^{\infty} x[m]\, h[n-m].
$$

For finite sequences of length $N_x$, $N_h$, output length $N_x + N_h - 1$ (full convolution).
**Same** mode truncates to input length (common in streaming filters).

### Impulse response

Unit impulse $\delta[n]$ (1 at $n=0$, else 0) yields output $h[n]$. Any input is sum of scaled
shifted impulses; LTI output is sum of scaled shifted $h[n]$ → convolution.

**Room IR:** balloon pop → recorded $h[n]$; convolving dry speech with $h$ places speech in that
room.

### Frequency domain

$$
Y(\Omega) = H(\Omega)\, X(\Omega)
$$

Circular convolution via DFT multiplies $X[k] H[k]$; linear convolution requires sufficient zero-
padding or overlap-add.

### FIR vs IIR

**FIR:** $h[n]$ finite length— always stable, linear phase possible. **IIR:** recursive; $h[n]$
infinite but parameterized compactly ([Filters: FIR, IIR, and the Z-Transform](#ch-10-filters)).

## Mathematical Formulation

Circular convolution length $N$:

$$
y[n] = \sum_{m=0}^{N-1} x[m]\, h[(n-m) \bmod N].
$$

Linear via zero-pad to $N \ge N_x + N_h - 1$ before DFT multiply.

## Audio Interpretation

**Guitar cab IR:** captures speaker/mic color as $h[n]$; plugin convolves guitar DI signal.

**Reverb:** long $h[n]$ (seconds → millions of samples at 48 kHz)— FFT convolution or partitioned
convolution required.

**Echo:** sparse $h[n]$ with peaks at delay taps.

## Implementation Notes

```python
y = np.convolve(x, h, mode="same")
# FFT: pad, multiply rfft, irfft
```

For long IRs: uniform partitioned convolution (UPC) splits IR into blocks— standard in reverb
plugins.

## Worked Example

**Problem:** $x[n]$ length 1000, $h[n]$ length 501. Full convolution length? At $f_s=48000$, IR
duration?

**Answers:** $1000+501-1=1500$ samples; IR duration $501/48000 \approx 10.4$ ms.

## Common Pitfalls

1. **Using circular convolution** without padding → wraparound artifacts.
2. **`mode='full'` vs `'same'`** confusion at buffer edges.
3. **Convolving mono IR with stereo** without per-channel policy.
4. **Assuming IR is minimum-phase** ([Phase, Group Delay, and Minimum Phase](#ch-12-phase-group-
delay))— linear-phase IR adds pre-ringing.

## Exercises

1. Manually convolve $x=[1,2,1]$, $h=[1,1]$.
2. Show $\delta[n]*h[n]=h[n]$.
3. Estimate FFT cost for 1 s IR at 48 kHz with 512-sample blocks.
4. Why does reverb on infinite input use overlap-add?

*Selected solutions: [Appendix — Exercise Solutions](#ch-23-exercise-solutions).*

## Further Reading

- Oppenheim & Schafer [@oppenheim2010discrete]
- Smith, *Physical Audio Signal Processing* [@smith2010physical]
- Zölzer, *DAFX* [@zoelzer2011dafx]

**Next chapter:** [Filters: FIR, IIR, and the Z-Transform](#ch-10-filters).
