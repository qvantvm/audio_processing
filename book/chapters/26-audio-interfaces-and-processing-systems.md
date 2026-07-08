# Audio Interfaces and Processing Systems {#ch-26-audio-interfaces}

## Purpose

Algorithms run on **hardware** connected by **interfaces**. This chapter surveys **DSP
processors**, **digital audio transports** (AES/EBU, MADI, HDMI, USB, Ethernet AVB/Dante), and
**two- vs multi-channel** system topologies— the context in which buffer sizes, clock domains, and
latency budgets are set.

## Learning Objectives

By the end of this chapter, the reader should be able to:

1. Contrast **fixed-point** vs **floating-point** DSP architectures for audio
2. Describe **AES/EBU** two-channel serial audio and **MADI** multichannel bundles
3. Explain **computer audio** (USB class-compliant, driver buffer sizing)
4. Outline **network audio** (packet timing, redundancy)
5. Sketch a **stereo** vs **5.1/7.1** processing graph with shared $f_s$

## Main Concepts

### Digital signal processors

Audio DSPs emphasize **MAC throughput**, **DMA**, and **low-latency I/O**:

| Type | Numeric mode | Typical role |
|------|--------------|--------------|
| Fixed-point DSP | Q31 arithmetic | Hearables, embedded FX |
| Floating-point DSP | IEEE SP | Live consoles, radar-class SHARC |
| General SoC + NEON | float/int hybrid | Mobile, plugins |

**Fixed-point** needs explicit scaling; **float** simplifies prototyping but watch denormals
([Testing, Measurement, and Numerical Pitfalls](#ch-21-testing-pitfalls)).

### Digital audio interfaces

**AES3 / AES/EBU:** serial stereo (or dual mono), 24-bit payload in 32-bit subframe, embedded
clock.

**MADI:** multiplex many AES-like channels on fiber/coax— broadcast and large consoles.

**HDMI / SPDIF:** consumer carriers; compressed formats optional.

**USB Audio Class:** isochronous or bulk; buffer size × $f_s$ sets latency.

**Ethernet (AVB, Dante, AES67):** packetized PCM; **PTP** clock sync; redundancy for live sound.

### Two-channel systems

Minimal graph: ADC → DSP → DAC with ring buffers; **full-duplex** for monitoring; **ASIO/CoreAudio**
buffer sizes 64–1024 samples trade CPU vs latency.

### Multi-channel systems

**5.1/7.1/Atmos** beds add routing matrices, per-channel EQ/DRC, and bass management (LFE low-pass).
**Ambisonics** uses spherical harmonic channels— different pan law than speaker beds.

Clock **master/slave** relationships prevent sample slip; asynchronous SRC ([Chapter
14](#ch-14-resampling)) bridges domains when needed.

## Implementation Notes

```python
# Conceptual: interleaved 5.1 buffer layout (L, R, C, LFE, Ls, Rs)
channels = 6
frame = np.zeros((block_size, channels))  # planar alternative: list of 1-D arrays
```

Document $f_s$, channel map, and **dBFS headroom** in every multi-channel module.

## Common Pitfalls

1. **Channel order mismatch** (LFE index) between DAW and renderer.
2. **Ignoring network jitter** — causes periodic clicks without adequate buffer.
3. **Assuming stereo plugins** on surround beds without downmix policy.

## Exercises

1. AES frame rate at 48 kHz— how many subframes per second?
2. Estimate one-way latency: buffer=256, $f_s=48$ kHz.
3. Why MADI on fiber for 64×64 splits?
4. Draw clock tree: internal crystal master, external word clock slave.

## Further Reading

- Pohlmann [@pohlmann2010principles]
- AES standards (AES3, AES67 overview)

**Next chapter:** [Equalizers, Fast Convolution, and Filter Banks](#ch-27-equalizers).
