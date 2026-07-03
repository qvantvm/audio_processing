# Appendix: Selected Exercise Solutions {#ch-23-exercise-solutions}

This appendix provides worked solutions for exercises in the foundation chapters (01–03). Try each exercise yourself first; use these solutions to check arithmetic, conventions, and reasoning.

---

## [Chapter 1](#ch-01-what-is-asp) — What Is Audio Signal Processing?

### Exercise 1.1

**Problem:** A stereo file runs at $f_s = 44100\,\mathrm{Hz}$ for 3 minutes. How many samples per channel?

**Solution:** Duration in seconds is $3 \times 60 = 180\,\mathrm{s}$. Samples per channel:

$$
N_{\mathrm{ch}} = f_s \cdot T = 44100 \times 180 = 7{,}938{,}000.
$$

The interleaved stereo buffer would contain $2 \times N_{\mathrm{ch}} = 15{,}876{,}000$ samples total.

### Exercise 1.2

**Problem:** Name one task better suited to time-domain processing and one better suited to frequency-domain processing.

**Solution (example answers):**

- **Time domain:** Sample-by-sample dynamics processing (e.g., a soft clipper or a simple delay line) naturally operates on $x[n]$ as it arrives. Causal, low-latency rules are easy to express without transforming the whole buffer.

- **Frequency domain:** Graphic equalization that boosts or cuts fixed bands is often implemented with FFT overlap-add or as a bank of filters designed from a magnitude mask. The frequency view makes “cut 3 dB at 2 kHz” explicit.

Other valid pairs (convolution reverb vs. pitch shifting via phase vocoder, etc.) are acceptable if the representation match is justified.

### Exercise 1.3

**Problem:** For $f_s = 48000\,\mathrm{Hz}$ and $N = 2048$, compute $\Delta f$. Which bin index is closest to 1000 Hz?

**Solution:**

$$
\Delta f = \frac{f_s}{N} = \frac{48000}{2048} = 23.4375\,\mathrm{Hz}.
$$

Bin index (nearest integer):

$$
k = \mathrm{round}\!\left(\frac{1000}{\Delta f}\right) = \mathrm{round}(42.67) = 43.
$$

Center frequency of bin 43: $43 \times 23.4375 = 1007.8125\,\mathrm{Hz}$— close to 1000 Hz but not exact. Peak-picking without interpolation would bias the estimate.

### Exercise 1.4

**Problem:** Explain why a snare transient challenges pure sinusoidal modeling.

**Solution:** A snare hit is **short in time** and **broadband in frequency**. A sum of a few sustained sinusoids models periodic or quasi-periodic tones well, but a transient contains energy spread across many frequencies that **decay quickly** and are not harmonically locked to a single $f_0$. Sinusoidal models need many partials with rapidly changing amplitudes—or a separate transient/noise layer—to match the attack; a single global sinusoidal fit smears the hit in time or misses noisy shell and broadband buzz.

### Exercise 1.5

**Problem:** Sketch a block diagram of a product you use.

**Solution:** No single correct diagram. A credible **reverb plugin** might show: input buffer $\rightarrow$ predelay line $\rightarrow$ parallel comb filters $\rightarrow$ all-pass diffusion $\rightarrow$ wet/dry mix $\rightarrow$ output buffer, with an FFT-based analyzer optional for metering only. Label where **buffers** (I/O blocks), **FFTs** (if any spectral meter), and **parameters** (decay time, mix) appear. The goal is to connect product behavior to representations from this chapter.

---

## [Chapter 2](#ch-02-signals-time-samples) — Signals, Time, and Samples

### Exercise 2.1

**Problem:** At $f_s = 44100\,\mathrm{Hz}$, how many samples span exactly 50 ms? Is the answer an integer?

**Solution:**

$$
N = f_s \cdot T = 44100 \times 0.05 = 2205.
$$

Yes—**2205** is an integer because $0.05\,\mathrm{s}$ is an exact multiple of the sample period $1/44100\,\mathrm{s}$.

### Exercise 2.2

**Problem:** Derive $\Omega$ for $f_0 = 1000\,\mathrm{Hz}$ at $f_s = 48000\,\mathrm{Hz}$.

**Solution:**

$$
\Omega = \frac{2\pi f_0}{f_s} = \frac{2\pi \cdot 1000}{48000} = \frac{\pi}{24} \approx 0.1309\,\mathrm{rad/sample}.
$$

### Exercise 2.3

**Problem:** A peak-normalized float sine peaks at $-3\,\mathrm{dBFS}$. What is its peak amplitude $A$?

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

Set `num_samples = 219` (or `int(np.ceil(2 * FS / F0))`). When looping the buffer, expect a **seam discontinuity** unless $2P$ is an integer— the waveform does not close exactly at sample 219 because A440 is not harmonically related to 48 kHz.

### Exercise 2.5

**Problem:** Stereo interleaved buffer length 96000 at $f_s = 48000\,\mathrm{Hz}$. Samples per channel and duration?

**Solution:** Interleaved stereo: 96000 total samples $\Rightarrow$ **48000 samples per channel**. Duration:

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

**Problem:** `aliasing_demo.py` with $f_{\mathrm{true}} = 1500\,\mathrm{Hz}$, $f_s = 4000\,\mathrm{Hz}$— aliasing?

**Solution:** Nyquist $= 2000\,\mathrm{Hz}$. Since $1500 < 2000$, the tone lies **below Nyquist** and is **not aliased** in the ideal band-limited model. The recorded discrete sinusoid oscillates at 1500 Hz; reconstruction (with ideal low-pass) recovers 1500 Hz. Compare with the default demo ($3500\,\mathrm{Hz}$ at $4000\,\mathrm{Hz}$), which folds to $500\,\mathrm{Hz}$.

### Exercise 3.5

**Problem:** Why does clipping before low-pass filtering risk aliasing on downsampling?

**Solution:** **Clipping is a nonlinear operation.** It creates new spectral content (harmonics and intermodulation) that may extend **above the new Nyquist** after downsampling. If you downsample without first **low-pass filtering** to the new band limit, that high-frequency energy **folds** into the baseband as aliasing. Correct order: band-limit (anti-alias filter) $\rightarrow$ then reduce rate; avoid hard clipping on full-band material before either step.

---

*Solutions for later chapters will be added in future passes. Numeric answers for ch 01–03 are verified by `solutions/ch01_verify.py` … `ch03_verify.py` (run `python solutions/run_verifications.py`).*
