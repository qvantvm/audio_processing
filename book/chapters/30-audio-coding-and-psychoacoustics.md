# Audio Coding and Psychoacoustics {#ch-30-audio-coding}

## Purpose

**Audio coding** compresses PCM for storage and streaming. This chapter covers **lossless** and
**lossy** coding, **psychoacoustic masking**, and codec families from **MPEG-1 Layer III** through
**AAC**, **MPEG-4**, **SBR**, and **CELT/Opus-style** transform coding— enough to read bitstream
docs and design preprocessing chains.

## Learning Objectives

By the end of this chapter, the reader should be able to:

1. Contrast **lossless** (FLAC, ALAC) vs **lossy** perceptual coding
2. Explain **critical bands**, **absolute threshold of hearing**, and **masking**
3. Outline **MPEG-1 Audio** filter bank + psycho model + bit allocation
4. Describe **AAC** improvements and **SBR** bandwidth extension
5. Relate **CELT** gain/shape split to MDCT coefficients

## Main Concepts

### Lossless audio coding

Predictive + entropy coding (FLAC: LPC residual + Rice codes). Bit-exact recovery; ~50–60% of PCM
size on music.

### Lossy audio coding

Discard information deemed **inaudible** via psychoacoustic model— irreversible but low bitrate.

### Psychoacoustics

**Critical bands:** auditory filter roughly constant-Q above 500 Hz.

**Absolute threshold:** quietest audible level vs frequency (ATH curve).

**Masking:** strong tone raises hearing threshold nearby— **simultaneous masking** in frequency,
**temporal masking** across time.

```bash
python examples/psychoacoustics_demo.py
```

Plots ATH and simplified masking spread function.

### MPEG-1 Audio (Layer I–III)

**Filter bank:** 32-subband polyphase (Layer I/II) or hybrid MDCT (Layer III / MP3).

**Psychoacoustic model:** signal-to-mask ratio per band → **bit allocation**.

**Coding:** quantize scalefactors + samples; Huffman coding of symbols.

### MPEG-2 / AAC

**AAC:** MDCT with finer resolution, noiseless coding, optional **LTP** for speech-like material.

**MPEG-4 Audio:** object coding, **BSAC**, parametric extensions.

### Spectral Band Replication (SBR)

Transmit low band + **guidance** to replicate high band— efficient for low bitrates.

### CELT / transform gain-shape coding

**Gain quantization** per band; **shape** (PVQ or similar) for spectral detail; **range coding**
entropy; decoder inverse MDCT — basis of Opus **CELT** mode.

## Common Pitfalls

1. **Heavy limiting before encoder** — confuses psycho model, causes pre-echo.
2. **Wrong sample rate** in SBR — doubled band misalignment.
3. **Treating MP3 as archival** — generation loss.

## Exercises

1. Why MDCT for Layer III vs polyphase for Layer I?
2. Sketch simultaneous masking: masker at 1 kHz affects which bands?
3. Compare FLAC vs AAC use cases in production.
4. What does SBR save at 64 kb/s stereo?

## Further Reading

- Painter & Spanias, perceptual coding [@painter2000perceptual]
- ISO/IEC MPEG standards (overview)
- Opus RFC 6716

**Next chapter:** [Nonlinear Processing and Virtual Analog](#ch-31-nonlinear-processing).
