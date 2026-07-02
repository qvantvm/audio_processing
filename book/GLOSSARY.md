# Glossary

Concise definitions of terms used across the book. See also `NOTATION.md` for symbols.

## Acoustic pressure

A physical quantity describing local variation in air pressure around ambient pressure, typically measured in pascals (Pa). Microphones transduce acoustic pressure (or related particle velocity) into an electrical signal.

## Aliasing

The appearance of frequency components in a sampled signal at incorrect frequencies, caused by sampling below the Nyquist rate or by nonlinear processing that creates energy above the Nyquist limit without adequate band-limiting. A tone at frequency $f$ may fold to $f_a = |f - k f_s|$ within $[0, f_s/2]$.

## Amplitude

The instantaneous value or peak magnitude of a signal in its **time-domain** representation. For a sinusoid $A\cos(\omega n + \phi)$, $A$ is the peak amplitude. Amplitude is not the same as spectral magnitude or loudness.

## Anti-aliasing filter

A low-pass filter applied before sampling to attenuate energy above the Nyquist frequency $f_s/2$, preventing out-of-band content from folding into the audible band as aliases.

## Audio signal processing (ASP)

The study and practice of representing, transforming, analyzing, and synthesizing audio using mathematical models and algorithms—typically starting from sampled sequences in digital systems.

## Bandwidth

The extent of nonzero (or significant) energy in a signal's spectrum. In discrete-time systems, usable bandwidth is limited by the sampling rate.

## Bin (frequency bin)

An index $k$ labeling a discrete frequency grid point in a DFT or STFT. Bin spacing depends on window length and sample rate.

## Bit depth

The number of bits $B$ used per PCM sample, determining the number of quantization levels (up to $2^B$ for uniform encoding) and approximate dynamic range.

## Complex sinusoid

A sequence $z[n] = A e^{j(\Omega n + \phi)}$ whose real part is a cosine wave. Represented as a rotating phasor of radius $A$ in the complex plane.

## Conjugate symmetry

For a real sequence $x[n]$, DFT coefficients satisfy $X[k] = X^*[N-k]$, reflecting equal contribution from positive and negative frequency phasors.

## Continuous-time signal

A function $x(t)$ defined for real time $t$, used to model analog waveforms before sampling.

## Decibel (dB)

A logarithmic measure of a ratio. For amplitude ratios, $20\log_{10}(r)$; for power ratios, $10\log_{10}(r)$.

## dBFS (decibels relative to full scale)

Digital level measured against nominal full scale in a fixed-point or floating-point PCM convention. Peak at full scale is $0\,\mathrm{dBFS}$; values are typically negative for headroom. Not equivalent to dB SPL.

## Digital full scale

The maximum representable amplitude in a digital PCM format before clipping; often mapped to $1.0$ in floating-point workflows or to the largest integer code in fixed-point PCM.

## Digital signal

A signal represented as a sequence of discrete values, usually uniformly spaced in time after sampling and quantization.

## Discrete-time signal

A sequence $x[n]$ indexed by integer sample index $n$.

## DFT (discrete Fourier transform)

A transform mapping a length-$N$ complex sequence $x[n]$ to frequency coefficients $X[k]$ on a grid of exactly $N$ equally spaced frequencies.

## Dither

Low-level noise added before quantization to decorrelate quantization error from the signal, reducing harmonic distortion on quiet passages at the cost of a slightly raised noise floor.

## Dynamic range

The span between the smallest and largest representable or meaningful signal levels in a system, often limited by noise floor and clipping.

## Euler's formula

The identity $e^{j\theta} = \cos\theta + j\sin\theta$, linking complex exponentials to real sinusoids.

## FFT (fast Fourier transform)

An efficient algorithm for computing the DFT and its inverse; mathematically equivalent to the DFT up to floating-point rounding.

## Frequency response

The complex gain $H(\Omega)$ of a linear time-invariant system as a function of frequency, describing magnitude and phase of the output sinusoid relative to the input.

## Impulse response

The output $h[n]$ of a discrete-time LTI system when the input is a unit impulse $\delta[n]$.

## Linear time-invariant (LTI) system

A system whose output is convolution of the input with an impulse response, and whose behavior does not change over time.

## Magnitude

The absolute value $|X|$ of a complex spectrum value or transfer function at a given frequency. Magnitude describes how much a sinusoidal component is scaled; phase describes its shift.

## Nyquist frequency

Half the sampling rate, $f_s/2$. Frequencies above this cannot be represented unambiguously without band-limiting.

## PCM (pulse-code modulation)

A digital representation storing uniformly sampled, quantized amplitude values— the common form of raw audio in WAV and similar formats.

## Phase

The angle of a complex spectral value or sinusoid relative to a reference. Phase affects waveform shape and timing of components; it is often ignored in naive feature extraction but matters for synthesis and filtering.

## Phasor

A complex number $Ae^{j\theta}$ represented as a vector in the complex plane; rotation by $e^{j\Omega n}$ models sinusoidal evolution over sample index $n$.

## Quantization

Mapping continuous or high-precision amplitudes to a finite set of discrete levels, introducing rounding error and a finite resolution limit.

## Quantization noise

The error signal $e[n] = Q(x[n]) - x[n]$ introduced by quantization, often modeled as approximately white noise for analysis.

## Reconstruction

The process of converting a discrete-time sampled sequence back to a continuous-time signal, ideally using band-limited interpolation; implemented approximately by DACs and analog filters.

## Sample index

The integer $n$ labeling position in a discrete-time sequence $x[n]$. Convert to time via $t_n = n/f_s$.

## Sample rate ($f_s$)

The number of samples per second used to represent a digital signal, in hertz (Hz).

## Sampling

The process of obtaining a discrete-time sequence from a continuous-time signal, usually at uniform intervals $T_s = 1/f_s$. Requires band-limiting to avoid aliasing.

## Signal-to-quantization-noise ratio (SQNR)

The ratio of signal power to quantization noise power. For a full-scale sinusoid and uniform quantizer, often approximated as $\mathrm{SQNR} \approx 6.02 B + 1.76$ dB for $B$ bits.

## Spectral leakage

Spreading of energy from a true frequency component into neighboring DFT bins when analyzing a finite segment, especially when the component does not align with a bin center.

## Spectrogram

A visual representation of magnitude (or power) of STFT coefficients over time and frequency.

## STFT (short-time Fourier transform)

A time–frequency representation computed by applying a windowed DFT to successive overlapping frames of a signal.

## Transfer function

The Z-transform ratio $H(z) = Y(z)/X(z)$ of an LTI system, encoding poles and zeros that determine frequency response and stability.

## Window function

A finite sequence $w[n]$ applied to multiply a signal segment before spectral analysis to control leakage and sidelobe tradeoffs.
