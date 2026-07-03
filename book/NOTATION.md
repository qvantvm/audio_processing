# Notation Guide

This file tracks symbols used across the book. Before introducing new notation in a chapter, check here and extend this list if needed.

## Time and Sampling

| Symbol | Meaning | Notes |
|--------|---------|-------|
| $t$ | Continuous time | Usually in seconds |
| $n$ | Discrete sample index | Integer; $n \in \mathbb{Z}$ or a finite range |
| $f_s$ | Sampling rate | Samples per second (Hz) |
| $T_s$ | Sample period | $T_s = 1/f_s$ seconds |
| $f_{\mathrm{Nyq}}$ | Nyquist frequency | $f_s/2$ |
| $f_a$ | Alias frequency | Folded into $[0, f_s/2]$ |
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
| $f_0$ | Sinusoid frequency | Hz; specific tone frequency |
| $\phi$ | Initial phase | Radians at $n=0$ unless stated |
| $|x[n]|$ | Magnitude of sample or complex value | Not the same as spectral magnitude |
| $L_{\mathrm{dBFS}}$ | Level in dBFS | $20\log_{10}$ of amplitude vs. digital full scale |
| $20\log_{10}(\cdot)$ | Decibel conversion | For amplitude ratios |
| $B$ | Bit depth | PCM bits per sample |
| $\Delta$ | Quantizer step size | Uniform spacing between levels |
| $Q(x)$ | Quantizer mapping | Rounds $x$ to nearest level |
| $e[n]$ | Quantization error | $Q(x[n]) - x[n]$ |
| $\mathrm{SQNR}$ | Signal-to-quantization-noise ratio | Often $\approx 6.02B + 1.76$ dB for sine |
| $\mathrm{RMS}$ | Root mean square level | See Chapter 13 |

**Convention:** We distinguish **amplitude** (instantaneous or peak value), **magnitude** (absolute value of a complex spectrum or transfer function), and **power/energy** (squared magnitude integrated or summed). Do not use these interchangeably.

## Frequency

| Symbol | Meaning | Notes |
|--------|---------|-------|
| $f$ | Cyclic frequency | Hertz (Hz); cycles per second |
| $\omega$ | Angular frequency (continuous) | rad/s; $\omega = 2\pi f$ |
| $\Omega$ | Normalized angular frequency (discrete) | rad/sample |
| $\Delta f$ | DFT bin spacing | $f_s/N$ hertz |
| $f_k$ | Bin center frequency | $k f_s/N$ |
| $\|X[k]\|$ | DFT magnitude at bin $k$ | Not peak time-domain amplitude |
| $\omega_k$ | DFT bin center frequency | Depends on $f_s$ and $N$ |
| $k$ | Frequency-bin index | $k \in \{0, 1, \ldots, N-1\}$ for length-$N$ DFT |

**Convention:** In discrete-time sections, $\Omega = 2\pi f / f_s$ unless stated otherwise. We avoid using $\omega$ for both continuous rad/s and discrete rad/sample in the same section without explicit clarification.

## Fourier and Z-Transform

| Symbol | Meaning | Notes |
|--------|---------|-------|
| $X(f)$ | Continuous Fourier transform | Of $x(t)$ |
| $c_k$ | Fourier series coefficient | Harmonic $k$ of periodic $x(t)$ |
| $f_0$ | Fundamental frequency | $1/T_0$ for period $T_0$ |
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
| $M$ | Window / STFT length | Samples per frame; $\Delta f \approx f_s/M$ |
| $R$ | Hop size | Samples between STFT frames |
| $X_m[k]$ | STFT coefficient | Frequency bin $k$ in frame $m$ |
| $C_m$ | Spectral centroid | Hz; center of mass of $|X_m[k]|$ |
| $\mathrm{flux}_m$ | Spectral flux | Frame-to-frame spectral change metric |
| $\text{CG}$ | Coherent gain | Window amplitude correction factor |

## Phase and Frequency Response

| Symbol | Meaning | Notes |
|--------|---------|-------|
| $\tau_g(\Omega)$ | Group delay | $-\frac{d}{d\Omega}\angle H(\Omega)$; seconds via $\tau_g/f_s$ |
| $\angle H(\Omega)$ | Phase response | Argument of $H(e^{j\Omega})$ |

## Filters and Difference Equations

| Symbol | Meaning | Notes |
|--------|---------|-------|
| $b_k$ | FIR numerator coefficients | |
| $a_k$ | IIR denominator coefficients | Usually $a_0 = 1$ |
| $z^{-1}$ | Unit delay operator | |
| $D$ | Delay in samples | Integer or fractional delay-line length |

## Complex Numbers and Sinusoids

| Symbol | Meaning | Notes |
|--------|---------|-------|
| $j$ | Imaginary unit | Engineering convention ($j^2 = -1$) |
| $z[n]$ | Complex sinusoid | Often $A e^{j(\Omega n + \phi)}$ |
| $|z|$, $\angle z$ | Magnitude and phase | Polar form of complex value |
| $z^*$ | Complex conjugate | Flip sign of imaginary part |
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
