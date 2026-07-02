# Notation Guide

This file tracks symbols used across the book. Before introducing new notation in a chapter, check here and extend this list if needed.

## Time and Sampling

| Symbol | Meaning | Notes |
|--------|---------|-------|
| $t$ | Continuous time | Usually in seconds |
| $n$ | Discrete sample index | Integer; $n \in \mathbb{Z}$ or a finite range |
| $f_s$ | Sampling rate | Samples per second (Hz) |
| $T_s$ | Sample period | $T_s = 1/f_s$ seconds |
| $N$ | Number of samples | In a finite buffer or DFT length |
| $T$ | Duration | $T = N/f_s$ for a length-$N$ segment |

## Signals

| Symbol | Meaning | Notes |
|--------|---------|-------|
| $x(t)$ | Continuous-time signal | Real- or complex-valued |
| $x[n]$ | Discrete-time signal | Sequence indexed by $n$ |
| $y[n]$ | Output signal | After processing |
| $\hat{x}[n]$ | Estimated or reconstructed signal | Context-dependent |
| $x[n] \leftrightarrow X[k]$ | DFT pair | See Frequency Domain |

## Amplitude, Energy, and Level

| Symbol | Meaning | Notes |
|--------|---------|-------|
| $A$ | Peak amplitude | Often for sinusoids |
| $|x[n]|$ | Magnitude of sample or complex value | Not the same as spectral magnitude |
| $20\log_{10}(\cdot)$ | Decibel conversion | For amplitude ratios |
| $\mathrm{RMS}$ | Root mean square level | See Chapter 13 |

**Convention:** We distinguish **amplitude** (instantaneous or peak value), **magnitude** (absolute value of a complex spectrum or transfer function), and **power/energy** (squared magnitude integrated or summed). Do not use these interchangeably.

## Frequency

| Symbol | Meaning | Notes |
|--------|---------|-------|
| $f$ | Cyclic frequency | Hertz (Hz); cycles per second |
| $\omega$ | Angular frequency (continuous) | rad/s; $\omega = 2\pi f$ |
| $\Omega$ | Normalized angular frequency (discrete) | rad/sample |
| $\omega_k$ | DFT bin center frequency | Depends on $f_s$ and $N$ |
| $k$ | Frequency-bin index | $k \in \{0, 1, \ldots, N-1\}$ for length-$N$ DFT |

**Convention:** In discrete-time sections, $\Omega = 2\pi f / f_s$ unless stated otherwise. We avoid using $\omega$ for both continuous rad/s and discrete rad/sample in the same section without explicit clarification.

## Fourier and Z-Transform

| Symbol | Meaning | Notes |
|--------|---------|-------|
| $X(f)$ | Continuous Fourier transform | Of $x(t)$ |
| $X[k]$ | $N$-point DFT | Of finite sequence $x[n]$ |
| $X(\Omega)$ | Discrete-time Fourier transform (DTFT) | For sequences; $2\pi$-periodic in $\Omega$ |
| $H(z)$ | Z-domain transfer function | $z$ complex variable |
| $h[n]$ | Impulse response | Discrete-time LTI system |
| $H(\Omega)$ | Frequency response | $H(e^{j\Omega})$ on unit circle |
| $*$ | Convolution | $(x * h)[n] = \sum_m x[m]\,h[n-m]$ |

## Windows and STFT

| Symbol | Meaning | Notes |
|--------|---------|-------|
| $w[n]$ | Analysis window | Length $M$ |
| $m$ | Frame index | STFT frame counter |
| $R$ | Hop size | Samples between STFT frames |
| $X_m[k]$ | STFT coefficient | Frequency bin $k$ in frame $m$ |

## Filters and Difference Equations

| Symbol | Meaning | Notes |
|--------|---------|-------|
| $b_k$ | FIR numerator coefficients | |
| $a_k$ | IIR denominator coefficients | Usually $a_0 = 1$ |
| $z^{-1}$ | Unit delay operator | |

## Complex Numbers and Sinusoids

| Symbol | Meaning | Notes |
|--------|---------|-------|
| $j$ | Imaginary unit | Engineering convention ($j^2 = -1$) |
| $e^{j\Omega n}$ | Complex exponential sequence | Basis for DTFT/DFT |
| $\Re\{\cdot\}$, $\Im\{\cdot\}$ | Real and imaginary parts | |

## Vectors and Matrices (later chapters)

| Symbol | Meaning | Notes |
|--------|---------|-------|
| $\mathbf{x}$ | Column vector | Bold lowercase |
| $\mathbf{W}$ | Matrix | Bold uppercase |

## Reserved / Avoid

- Do not use $i$ for imaginary unit (use $j$).
- Do not use $n$ for frequency bin when $k$ is already the bin index in the same chapter.
- Do not write "frequency content" without specifying **which representation** (DFT bin, DTFT, STFT cell, etc.).
