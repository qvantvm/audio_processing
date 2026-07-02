# Preface

## Why this book exists

Audio appears simple at first: a waveform, a spectrum, a filter. In practice, audio signal processing is a stack of **representations**—each valid in its domain, each with its own units, pitfalls, and implementation details. Confusion usually comes not from missing a formula, but from mixing representations: treating a DFT bin index as if it were a continuous frequency without checking bin spacing; reporting "amplitude" when the code computed spectral magnitude; designing a filter in Hz without remembering the sample rate.

This book is for readers who want to **implement** algorithms, **read** papers and standards, and **debug** real audio systems with confidence. We emphasize mathematical clarity, audio-specific interpretation, and practical notes grounded in code.

## Who should read this

You should get value from this book if you:

- Program in Python (or can translate pseudocode) and want correct DSP implementations
- Understand basic calculus and complex numbers but want discrete-time audio made precise
- Build tools for analysis, synthesis, effects, or machine-learning features on audio

We assume you can read equations and code. We do not assume prior DSP coursework, but we move quickly toward rigorous definitions.

## What this book covers

The arc runs from **samples** to **spectra**, **filters**, **time–frequency analysis**, **musical and synthesis representations**, **features**, and **implementation/testing**. A full chapter list and status tracker lives in `BOOK_PLAN.md`.

Topics include sampling and quantization; Fourier analysis and the DFT/FFT; windowing and leakage; the STFT; convolution and impulse responses; FIR/IIR filters and the z-transform; delay-based structures; phase and group delay; loudness and dynamics; resampling; pitch and onset analysis; spectral descriptors; and an overview of neural audio representations. Later chapters focus on numerical pitfalls and assembling a small DSP toolkit.

## How to read it

- **Sequential reading** builds concepts in dependency order (see the dependency diagram in `BOOK_PLAN.md`).
- **Reference reading** is supported by `NOTATION.md` and `GLOSSARY.md`.
- **Hands-on learning**: run scripts in `examples/` alongside the chapter sections that reference them.

Each chapter follows a common template: purpose, learning objectives, concepts, math, audio interpretation, implementation notes, worked examples, pitfalls, exercises, and further reading.

## Conventions

- **Math:** LaTeX inline $x[n]$ and display equations; symbols defined in `NOTATION.md`.
- **Code:** Python with NumPy/SciPy/Matplotlib unless noted; snippets should be readable and runnable.
- **Citations:** Pandoc form `[@key]`; bibliography in `bibliography.bib`. We prefer canonical texts such as [@smith2010physical; @oppenheim2010discrete; @roads1996computer].
- **Status:** Early chapters are drafts; stubs are marked in the book plan until filled in.

## Acknowledgments

This book synthesizes standard material from the audio DSP literature. Primary influences include the online books by Julius O. Smith [@smith2010physical; @smith2011spectral], classical discrete-time signal processing texts [@oppenheim2010discrete], and computer music references [@roads1996computer; @puckette2007electronic].

## A note on listening

Equations and plots are not a substitute for ears. Where exercises suggest listening tests, use headphones or calibrated monitors at **safe levels**. Many phenomena—leakage, phase artifacts, pre-ringing from filters—are easier to trust after you have heard them once.

---

*This is a living manuscript. See `REVIEW_NOTES.md` for open issues and `BOOK_PLAN.md` for authoring status.*
