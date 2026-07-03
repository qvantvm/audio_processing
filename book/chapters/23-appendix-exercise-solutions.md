# Appendix: Selected Exercise Solutions {#ch-23-exercise-solutions}

This appendix provides worked solutions for exercises in chapters **01–15**. Try each exercise
yourself first; use these solutions to check arithmetic, conventions, and reasoning.

---

## [Chapter 1](#ch-01-what-is-asp) — What Is Audio Signal Processing?

### Exercise 1.1

**Problem:** A stereo file runs at $f_s = 44100\,\mathrm{Hz}$ for 3 minutes. How many samples per
channel?

**Solution:** Duration in seconds is $3 \times 60 = 180\,\mathrm{s}$. Samples per channel:

$$
N_{\mathrm{ch}} = f_s \cdot T = 44100 \times 180 = 7{,}938{,}000.
$$

The interleaved stereo buffer would contain $2 \times N_{\mathrm{ch}} = 15{,}876{,}000$ samples
total.

### Exercise 1.2

**Problem:** Name one task better suited to time-domain processing and one better suited to
frequency-domain processing.

**Solution (example answers):**

- **Time domain:** Sample-by-sample dynamics processing (e.g., a soft clipper or a simple delay line) naturally operates on $x[n]$ as it arrives. Causal, low-latency rules are easy to express without transforming the whole buffer.

- **Frequency domain:** Graphic equalization that boosts or cuts fixed bands is often implemented with FFT overlap-add or as a bank of filters designed from a magnitude mask. The frequency view makes “cut 3 dB at 2 kHz” explicit.

Other valid pairs (convolution reverb vs. pitch shifting via phase vocoder, etc.) are acceptable if
the representation match is justified.

### Exercise 1.3

**Problem:** For $f_s = 48000\,\mathrm{Hz}$ and $N = 2048$, compute $\Delta f$. Which bin index is
closest to 1000 Hz?

**Solution:**

$$
\Delta f = \frac{f_s}{N} = \frac{48000}{2048} = 23.4375\,\mathrm{Hz}.
$$

Bin index (nearest integer):

$$
k = \mathrm{round}\!\left(\frac{1000}{\Delta f}\right) = \mathrm{round}(42.67) = 43.
$$

Center frequency of bin 43: $43 \times 23.4375 = 1007.8125\,\mathrm{Hz}$— close to 1000 Hz but not
exact. Peak-picking without interpolation would bias the estimate.

### Exercise 1.4

**Problem:** Explain why a snare transient challenges pure sinusoidal modeling.

**Solution:** A snare hit is **short in time** and **broadband in frequency**. A sum of a few
sustained sinusoids models periodic or quasi-periodic tones well, but a transient contains energy
spread across many frequencies that **decay quickly** and are not harmonically locked to a single
$f_0$. Sinusoidal models need many partials with rapidly changing amplitudes—or a separate
transient/noise layer—to match the attack; a single global sinusoidal fit smears the hit in time or
misses noisy shell and broadband buzz.

### Exercise 1.5

**Problem:** Sketch a block diagram of a product you use.

**Solution:** No single correct diagram. A credible **reverb plugin** might show: input buffer
$\rightarrow$ predelay line $\rightarrow$ parallel comb filters $\rightarrow$ all-pass diffusion
$\rightarrow$ wet/dry mix $\rightarrow$ output buffer, with an FFT-based analyzer optional for
metering only. Label where **buffers** (I/O blocks), **FFTs** (if any spectral meter), and
**parameters** (decay time, mix) appear. The goal is to connect product behavior to representations
from this chapter.

---

## [Chapter 2](#ch-02-signals-time-samples) — Signals, Time, and Samples

### Exercise 2.1

**Problem:** At $f_s = 44100\,\mathrm{Hz}$, how many samples span exactly 50 ms? Is the answer an
integer?

**Solution:**

$$
N = f_s \cdot T = 44100 \times 0.05 = 2205.
$$

Yes—**2205** is an integer because $0.05\,\mathrm{s}$ is an exact multiple of the sample period
$1/44100\,\mathrm{s}$.

### Exercise 2.2

**Problem:** Derive $\Omega$ for $f_0 = 1000\,\mathrm{Hz}$ at $f_s = 48000\,\mathrm{Hz}$.

**Solution:**

$$
\Omega = \frac{2\pi f_0}{f_s} = \frac{2\pi \cdot 1000}{48000} = \frac{\pi}{24} \approx
0.1309\,\mathrm{rad/sample}.
$$

### Exercise 2.3

**Problem:** A peak-normalized float sine peaks at $-3\,\mathrm{dBFS}$. What is its peak amplitude
$A$?

**Solution:** For a sine, peak equals amplitude $A$. With $0\,\mathrm{dBFS}$ at peak $= 1$:

$$
-3 = 20\log_{10}(A) \quad\Rightarrow\quad A = 10^{-3/20} \approx 0.708.
$$

### Exercise 2.4

**Problem:** Modify `a440_sine_wave.py` to plot two cycles using $\lceil 2P \rceil$ samples.

**Solution:** Period in samples at A440 and $f_s = 48000\,\mathrm{Hz}$:

$$
P = \frac{f_s}{f_0} = \frac{48000}{440} \approx 109.0909.
$$

Smallest integer spanning at least two cycles:

$$
N = \lceil 2P \rceil = \lceil 218.18\ldots \rceil = 219.
$$

Set `num_samples = 219` (or `int(np.ceil(2 * FS / F0))`). When looping the buffer, expect a **seam
discontinuity** unless $2P$ is an integer— the waveform does not close exactly at sample 219 because
A440 is not harmonically related to 48 kHz.

### Exercise 2.5

**Problem:** Stereo interleaved buffer length 96000 at $f_s = 48000\,\mathrm{Hz}$. Samples per
channel and duration?

**Solution:** Interleaved stereo: 96000 total samples $\Rightarrow$ **48000 samples per channel**.
Duration:

$$
T = \frac{48000}{48000} = 1\,\mathrm{s}.
$$

---

## [Chapter 3](#ch-03-sampling-quantization) — Sampling, Quantization, and Digital Audio

### Exercise 3.1

**Problem:** $f_s = 22050\,\mathrm{Hz}$. What frequency aliases with $12000\,\mathrm{Hz}$?

**Solution:** Nyquist is $f_s/2 = 11025\,\mathrm{Hz}$. Since $12000 > 11025$, the component folds:

$$
f_{\mathrm{alias}} = f_s - 12000 = 22050 - 12000 = 10050\,\mathrm{Hz}.
$$

(Equivalently, reflect about $f_s/2$ into the baseband $[0, f_s/2]$.)

### Exercise 3.2

**Problem:** One second of stereo 16-bit PCM at $44100\,\mathrm{Hz}$: samples and bytes?

**Solution:**

- **Samples:** $44100$ per channel per second $\Rightarrow$ **88200** interleaved samples per second.
- **Bytes:** 16 bits $= 2$ bytes per sample $\Rightarrow$ $88200 \times 2 = \mathbf{176{,}400}$ bytes per second (excluding WAV/RIFF header).

### Exercise 3.3

**Problem:** Quantization levels and $\Delta$ for $B$ bits on $[-1, 1]$; value for $B = 16$.

**Solution:** Uniform $B$-bit PCM uses $2^B$ levels across width 2:

$$
\Delta = \frac{2}{2^B} = 2^{1-B}.
$$

For $B = 16$:

$$
\Delta = \frac{2}{65536} = \frac{1}{32768} \approx 3.05 \times 10^{-5}.
$$

### Exercise 3.4

**Problem:** `aliasing_demo.py` with $f_{\mathrm{true}} = 1500\,\mathrm{Hz}$, $f_s =
4000\,\mathrm{Hz}$— aliasing?

**Solution:** Nyquist $= 2000\,\mathrm{Hz}$. Since $1500 < 2000$, the tone lies **below Nyquist**
and is **not aliased** in the ideal band-limited model. The recorded discrete sinusoid oscillates at
1500 Hz; reconstruction (with ideal low-pass) recovers 1500 Hz. Compare with the default demo
($3500\,\mathrm{Hz}$ at $4000\,\mathrm{Hz}$), which folds to $500\,\mathrm{Hz}$.

### Exercise 3.5

**Problem:** Why does clipping before low-pass filtering risk aliasing on downsampling?

**Solution:** **Clipping is a nonlinear operation.** It creates new spectral content (harmonics and
intermodulation) that may extend **above the new Nyquist** after downsampling. If you downsample
without first **low-pass filtering** to the new band limit, that high-frequency energy **folds**
into the baseband as aliasing. Correct order: band-limit (anti-alias filter) $\rightarrow$ then
reduce rate; avoid hard clipping on full-band material before either step.

---

## [Chapter 4](#ch-04-sinusoids-complex) — Sinusoidal Signals and Complex Numbers

### Exercise 4.1

$x[n] = \sin(\Omega n) = \Im\{e^{j\Omega n}\}$.

### Exercise 4.2

$z[n] = 2 e^{j(\pi/8) n}$. At $n=10$: $|z[10]| = 2$, $\angle z[10] = 10\pi/8 = 5\pi/4$ rad.

### Exercise 4.3

$\Re\{e^{j\Omega n}\} = \cos(\Omega n) = \cos(-\Omega n) = \Re\{e^{-j\Omega n}\}$ because cosine is
even.

### Exercise 4.4

$\phi = \pi/2$ shifts cosine to sine: $x[0] = A\sin(0)=0$ instead of peak at $n=0$.

### Exercise 4.5

When $\Omega_1 \approx \Omega_2$, phasors rotate at nearly the same rate and their vector sum
**beats**— slow amplitude modulation at $\approx |f_1-f_2|$.

---

## [Chapter 5](#ch-05-fourier) — Fourier Representation

### Exercise 5.1

$T_0=5\,\mathrm{ms}$ → $f_0=200\,\mathrm{Hz}$. Harmonics: $200, 400, 600\,\mathrm{Hz}$.

### Exercise 5.2

Even square wave is symmetric about time origin → only **cosine** (even) Fourier terms; sine (odd)
coefficients are zero.

### Exercise 5.3

For $x(t)=\cos(2\pi f_0 t)$ over one period, only $c_{\pm 1}$ are non-zero ($\tfrac{1}{2}$ each in
common normalizations).

### Exercise 5.4

Doubling odd harmonics in `fourier_series_square_wave.py` reduces Gibbs ringing— RMS error vs ideal
square **decreases**.

### Exercise 5.5

$f_0=150\,\mathrm{Hz}$: $700/150 \approx 4.67$ → $k=5$ ($750\,\mathrm{Hz}$); $1200/150=8$ → $k=8$
($1200\,\mathrm{Hz}$).

---

## [Chapter 6](#ch-06-dft-fft) — DFT, FFT, and Spectral Analysis

### Exercise 6.1

$\Delta f = 44100/4096 \approx 10.766\,\mathrm{Hz}$. Bin $k=100$: $100 \cdot \Delta f \approx
1076.7\,\mathrm{Hz}$.

### Exercise 6.2

For real $x[n]$, $X[0]=\sum_n x[n]$ is real (sum of reals).

### Exercise 6.3

440 Hz at 48 kHz, $N=1024$: peak at $k=9$, center $9 \cdot 48000/1024 = 421.875\,\mathrm{Hz}$ —
**not** exactly 440 Hz.

### Exercise 6.4

Zero-padding to $4N$ **refines the frequency grid** ($\Delta f$ quarters) but does **not** improve
true resolution from a fixed time window.

### Exercise 6.5

Manual bin $k$: $X[k]=\sum_n x[n] e^{-j2\pi kn/N}$ should match `np.fft.fft(x)[k]` within floating
error.

---

---

## [Chapter 7](#ch-07-windowing) — Windowing, Leakage, and Resolution

### Exercise 7.1

Hann coherent gain ≈ mean of window = **0.5** for length 1024 (`np.mean(np.hanning(1024))`).

### Exercise 7.2

Using $N-1$ in the cosine denominator keeps the window **symmetric** about its center for finite
$N$.

### Exercise 7.3

Blackman main lobe wider than Hann; rectangular narrowest main lobe but highest sidelobes — measure
−3 dB width in your plot.

### Exercise 7.4

Drum transients are **short**; long $N$ smears attack time in time–frequency view even if $\Delta f$
is finer.

---

## [Chapter 8](#ch-08-stft) — STFT, Spectrograms, and Time–Frequency Analysis

### Exercise 8.1

$M=2048$, $R=512$ at 48 kHz: overlap $= (M-R)/M = \mathbf{75\%}$. Frames per second $= f_s/R =
48000/512 = \mathbf{93.75}$.

### Exercise 8.2

Two tones at different onsets appear as **separate ridges** in time on a spectrogram; overlap in
frequency if both sound together.

### Exercise 8.3

$M=256$: better time resolution, worse frequency resolution; $M=4096$: opposite — classic
time–frequency tradeoff.

### Exercise 8.4

Formants need **moderate** bandwidth — not as wide as a drum window, not as narrow as a multi-second
pitch analysis window.

---

## [Chapter 9](#ch-09-convolution) — Convolution and Impulse Responses

### Exercise 9.1

$[1,2,1]*[1,1] = [1, 3, 3, 1]$.

### Exercise 9.2

$\delta[n]*h[n]=h[n]$ because only $n=0$ picks $h[n]$.

### Exercise 9.3

1 s IR at 48 kHz has length 48000; block FFT size 512 ⇒ about $48000/512 \approx 94$ blocks per
second of processing in a block scheme — each block needs $O(L\log L)$ FFT work.

### Exercise 9.4

**Overlap-add** lets infinite streams be processed in fixed blocks while matching linear convolution
within overlap regions.

---

## [Chapter 10](#ch-10-filters) — Filters: FIR, IIR, and the Z-Transform

### Exercise 10.1

$y[n]=0.5x[n]+0.5x[n-1]$ ⇒ $H(z)=0.5+0.5z^{-1}$. At $\Omega=0$: $|H|=1$. At $\Omega=\pi$: $|H|=0$.
**Yes — a simple two-point averager is a lowpass.**

### Exercise 10.2

Pole at $z=0.9$: **stable** ($|z|<1$). Pole at $z=1.05$: **unstable** for causal IIR.

### Exercise 10.3

Use `design_fir_lowpass(44100, 1000, num_taps=101)`; passband near 500 Hz should be near unity;
stopband near 10 kHz should be strongly attenuated.

### Exercise 10.4

Minimum-phase IIR achieves a magnitude target with **less total delay / less pre-ringing** than
linear-phase FIR of similar order — important for mastering where latency and transient smear matter.

---

## [Chapter 11](#ch-11-delay-comb-allpass) — Delay Lines, Comb Filters, and All-Pass Filters

### Exercise 11.1

Feedforward comb $H(z)=1+g z^{-D}$ with $g=0.7$, $D=100$ has peaks at $\Omega_k = 2\pi k/D$ —
periodic resonances in frequency.

### Exercise 11.2

All-pass has $|H(\Omega)|\approx 1$ but **frequency-dependent phase** → different partials delayed
differently → transient smear.

### Exercise 11.3

Incommensurate delays (e.g. 97, 113, 137 samples) avoid a single shared repetition rate in the
combined response — smoother reverb tail.

### Exercise 11.4

Faster LFO on delay time → faster notches/peaks sweep → **faster flanger motion**.

---

## [Chapter 12](#ch-12-phase-group-delay) — Phase, Group Delay, and Minimum Phase

### Exercise 12.1

Peaking biquad at high $Q$ shows **bump in group delay** near the center frequency — energy at that
band is delayed more.

### Exercise 12.2

Linear-phase FIR satisfies $h[n]=h[N-1-n]$ (symmetry) ⇒ phase linear in $\Omega$.

### Exercise 12.3

Same magnitude, linear-phase vs minimum-phase: linear-phase adds **symmetric pre/post ringing**;
minimum-phase concentrates energy causally (listening exercise).

### Exercise 12.4

Top/bottom snare mics see opposite polarity on some modes → **cancellation** when summed without
polarity correction.

---

---

## [Chapter 13](#ch-13-envelopes-loudness) — Envelopes, Loudness, and Dynamics

### Exercise 13.1

Sine crest factor $= 20\log_{10}(\sqrt{2}) \approx 3.01$ dB. Snare hits typically much higher.

### Exercise 13.2

Attack $\tau = 10$ ms at $f_s = 48000$: $\alpha = e^{-1/(\tau f_s)} \approx 0.998$.

### Exercise 13.3

Input $-8$ dBFS, threshold $-20$ dBFS → input **below** threshold → **no compression** → output
$\approx -8$ dBFS.

### Exercise 13.4

**K-weighting** approximates head-related sensitivity so LUFS correlates better with perceived
loudness than unweighted RMS.

---

## [Chapter 14](#ch-14-resampling) — Resampling and Sample-Rate Conversion

### Exercise 14.1

Upsample ×2 inserts zeros → spectra repeat at multiples of original; low-pass removes images.

### Exercise 14.2

**Polyphase** splits filter into sub-filters per phase → only compute non-zero stuffed positions.

### Exercise 14.3

$44100 \to 48000$ via ratio $160/147$; 440 Hz tone peak should remain $\approx 440$ Hz (verify with
FFT).

### Exercise 14.4

**Asynchronous SRC** when clock domains drift (different interfaces, wireless link, DAW vs interface
not locked).

---

## [Chapter 15](#ch-15-features) — Audio Features and Descriptors

### Exercise 15.1

Spectrum magnitudes $[1,2,1]$ at $[100,200,300]$ Hz → centroid $= (100+400+300)/4 = 200$ Hz.

### Exercise 15.2

Spectral flux peaks at frame boundaries with large magnitude increases (onsets / hand claps).

### Exercise 15.3

Voiced speech: lower ZCR; unvoiced/fricatives: higher ZCR (more zero crossings).

### Exercise 15.4

Log compresses dynamic range before DCT so **multiplicative** spectral shapes become **additive**
(roughly), matching auditory scale and improving MFCC stability.

---

*Numeric answers for ch 01–15 verified by `solutions/ch01_verify.py` … `ch15_verify.py` (`python
solutions/run_verifications.py`).*
