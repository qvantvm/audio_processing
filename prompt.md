You are helping me create a high-quality technical book on audio signal representation and processing.

The book is written as a collection of Markdown files using Pandoc Markdown extensions. The final output should be suitable for conversion to PDF, HTML, and EPUB through Pandoc.

Your job is not to write everything in one pass. Your job is to run an iterative authoring loop that plans, writes, reviews, improves, and maintains consistency across the book.

Goal

Create a clear, rigorous, pedagogical book that teaches audio signal representation and processing from first principles to practical implementation.

The target reader is a technically strong programmer, researcher, or engineer who wants to understand audio DSP deeply enough to implement algorithms, read papers, and build systems.

The tone should be precise, research-oriented, and practical. Avoid hand-wavy explanations. Prefer mathematical clarity, intuition, diagrams, examples, and executable code snippets where appropriate.

Book Format

Use Pandoc-flavored Markdown.

Use:

* Markdown headings
* LaTeX math with $...$ and $$...$$
* Cross-references where appropriate
* Figures with captions
* Tables
* Code fences
* Admonition-style blocks when useful
* Bibliography citations in Pandoc form, for example [@smith2010physical]

The book should be organized as multiple Markdown files, for example:

book/
  metadata.yaml
  bibliography.bib
  chapters/
    00-preface.md
    01-signals-and-systems.md
    02-digital-audio.md
    03-frequency-representation.md
    ...
  figures/
  examples/
  Makefile

Do not create a monolithic single file unless explicitly required.

Core Subject

The book should cover audio signal representation and processing, including but not limited to:

1. Continuous-time and discrete-time signals
2. Sampling, quantization, aliasing, reconstruction
3. Audio file formats, PCM, bit depth, sample rate, normalization
4. Time-domain representation
5. Frequency-domain representation
6. Fourier series, Fourier transform, DFT, FFT
7. Windowing and spectral leakage
8. STFT and spectrograms
9. Time-frequency tradeoffs
10. Filter basics
11. FIR and IIR filters
12. Z-transform and transfer functions
13. Convolution and impulse responses
14. Delay lines, comb filters, all-pass filters
15. Envelopes, RMS, loudness, dynamic range
16. Phase, group delay, minimum phase, linear phase
17. Resampling and interpolation
18. Modulation
19. Wavetable and oscillator representations
20. Additive, subtractive, FM, granular, and modal representations
21. Physical-modeling representations where relevant
22. Audio feature extraction
23. Pitch detection and onset detection
24. Spectral descriptors
25. Mel scale, MFCCs, chroma, constant-Q transform
26. Neural/audio ML representations where useful
27. Practical implementation patterns in Python
28. Numerical pitfalls and testing strategies

Authoring Loop

Work iteratively. Follow this loop:

1. Inspect

Before editing, inspect the current repository structure.

Look for:

* Existing book outline
* Existing chapters
* Existing bibliography
* Existing figures
* Existing examples
* Existing build scripts
* Existing style conventions

Do not overwrite existing work blindly.

2. Plan

Maintain a high-level book plan in:

book/BOOK_PLAN.md

This file should contain:

* Book thesis
* Target audience
* Chapter list
* Learning objectives per chapter
* Dependencies between chapters
* Missing sections
* Status of each chapter: stub, draft, reviewed, polished

Before major changes, update the plan.

3. Write Small Units

Work in small, reviewable chunks.

A good unit is:

* One section
* One subsection
* One figure explanation
* One worked example
* One code example
* One glossary entry

Do not generate huge chapters in a single pass unless the file is empty and the structure is already clear.

4. Maintain Pedagogical Quality

Each important concept should generally include:

* Definition
* Intuition
* Mathematical formulation
* Audio-specific interpretation
* Practical implementation note
* Common mistake or pitfall
* Small example

For example, when explaining the DFT, include:

* What problem it solves
* How it maps samples to frequency bins
* The formula
* Meaning of magnitude and phase
* Bin spacing
* Leakage
* Windowing
* Short Python example
* What can go wrong

5. Maintain Mathematical Consistency

Use consistent notation across the book.

Maintain a notation file:

book/NOTATION.md

Track symbols such as:

x[n]       discrete-time signal
x(t)       continuous-time signal
f_s        sampling rate
N          number of samples
k          frequency-bin index
\omega     normalized angular frequency
X[k]       DFT of x[n]
h[n]       impulse response
H(z)       z-domain transfer function

Before introducing new notation, check whether it already exists.

6. Maintain a Glossary

Maintain:

book/GLOSSARY.md

Each entry should be concise but technically correct.

Example:

## Spectral leakage
Spectral leakage is the spreading of energy from one frequency component into nearby DFT bins caused by observing a finite-length segment of a signal.

7. Maintain Examples

Create executable examples when useful under:

book/examples/

Prefer Python with NumPy, SciPy, and Matplotlib.

Example files should be self-contained and have clear names, such as:

examples/dft_bin_spacing.py
examples/window_leakage_demo.py
examples/fir_lowpass_demo.py
examples/stft_spectrogram_demo.py

When adding code examples in the book, prefer code that is short enough to read but accurate enough to run.

8. Maintain Figures

When a concept benefits from a figure, add a placeholder or generate a simple figure script.

Use:

book/figures/

For generated figures, place the source script in:

book/examples/

and the rendered figure in:

book/figures/

Figures should explain concepts visually, not decorate the book.

Useful figures include:

* Sampling and aliasing
* Quantization
* Sine wave phase
* DFT bin spacing
* Windowing and leakage
* STFT time-frequency tiling
* FIR convolution
* IIR feedback
* Comb filter response
* Spectrogram examples
* Filter magnitude and phase response

9. Review

After writing or modifying a section, review it for:

* Correctness
* Clarity
* Missing assumptions
* Broken notation
* Missing definitions
* Inconsistent terminology
* Too much abstraction without audio intuition
* Too much intuition without math
* Code that does not run
* Claims that need citations

Create or update:

book/REVIEW_NOTES.md

Record open issues and future improvements.

10. Build Awareness

If a build system exists, use it. Otherwise create a simple one.

Prefer a Makefile such as:

pdf:
	pandoc metadata.yaml chapters/*.md --bibliography bibliography.bib -o audio_signal_processing.pdf
html:
	pandoc metadata.yaml chapters/*.md --bibliography bibliography.bib -o audio_signal_processing.html
epub:
	pandoc metadata.yaml chapters/*.md --bibliography bibliography.bib -o audio_signal_processing.epub

Do not assume LaTeX packages that are not necessary.

Quality Bar

The book should not read like shallow documentation. It should read like a serious technical text.

For every chapter, aim for:

* Clear motivation
* Conceptual progression
* Correct equations
* Audio-domain examples
* Practical implementation guidance
* Exercises or questions
* References for deeper study

Avoid:

* Buzzwords
* Unexplained formulas
* Long walls of text
* Vague descriptions like “frequency content” without defining what representation is being used
* Treating FFT as magic
* Confusing amplitude, magnitude, power, and energy
* Confusing Hz, radians/sample, and bin index
* Confusing continuous-time and discrete-time notation
* Ignoring phase
* Ignoring numerical details

Suggested Book Structure

Use this as the initial structure unless the repository already contains a better one.

00-preface.md
01-what-is-audio-signal-processing.md
02-signals-time-and-samples.md
03-sampling-quantization-and-digital-audio.md
04-sinusoidal-signals-and-complex-numbers.md
05-fourier-representation.md
06-dft-fft-and-spectral-analysis.md
07-windowing-leakage-and-resolution.md
08-stft-spectrograms-and-time-frequency-analysis.md
09-convolution-and-impulse-responses.md
10-filters-fir-iir-and-z-transform.md
11-delay-lines-comb-filters-and-allpass-filters.md
12-phase-group-delay-and-minimum-phase.md
13-envelopes-loudness-and-dynamics.md
14-resampling-interpolation-and-sample-rate-conversion.md
15-audio-features-and-descriptors.md
16-pitch-onsets-and-rhythm.md
17-musical-signal-representations.md
18-synthesis-representations.md
19-physical-modeling-representations.md
20-neural-audio-representations.md
21-testing-measurement-and-numerical-pitfalls.md
22-building-a-small-audio-dsp-toolkit.md

Chapter Template

When creating a new chapter, use this structure:

# Chapter Title
## Purpose
Explain what the chapter teaches and why it matters.
## Learning Objectives
By the end of this chapter, the reader should be able to:
1. ...
2. ...
3. ...
## Main Concepts
...
## Mathematical Formulation
...
## Audio Interpretation
...
## Implementation Notes
...
## Worked Example
...
## Common Pitfalls
...
## Exercises
...
## Further Reading
...

Style Rules

Use precise language.

Prefer:

A discrete-time signal is a sequence of values indexed by an integer sample index.

Avoid:

Audio is basically just numbers.

Prefer:

The DFT represents a finite sequence as a weighted sum of complex sinusoids whose frequencies lie exactly on the DFT bin grid.

Avoid:

The FFT tells us what frequencies are inside the sound.

Use examples grounded in audio:

* A440 sine wave
* Piano note decay
* Snare transient
* Vocal vowel spectrum
* Room impulse response
* Echo and delay
* Low-pass filtering
* Aliasing from a naive oscillator

Citation Policy

When making historical, scientific, or nontrivial claims, add citations.

Use book/bibliography.bib.

Prefer canonical references, such as:

* Julius O. Smith, Physical Audio Signal Processing
* Julius O. Smith, Spectral Audio Signal Processing
* Oppenheim and Schafer, Discrete-Time Signal Processing
* Roads, The Computer Music Tutorial
* Zölzer, DAFX
* Puckette, The Theory and Technique of Electronic Music
* Rabiner and Schafer, speech/audio processing references
* Allen and Rabiner, STFT-related references where appropriate

Do not invent citations. If unsure, leave a clear TODO: citation needed.

Exercises

Each chapter should eventually include exercises.

Use a mix of:

* Conceptual questions
* Mathematical derivations
* Small coding exercises
* Listening exercises
* Debugging exercises

Example:

## Exercises
1. Generate a 440 Hz sine wave at 48 kHz. What is its period in samples?
2. Compute the DFT of a 1024-sample sine wave that does not land exactly on a bin. What do you observe?
3. Change the analysis window from rectangular to Hann. How does the spectrum change?

The Cursor Loop

Repeatedly perform the following process:

1. Inspect current files.
2. Identify the highest-value missing or weak section.
3. Make a small, coherent edit.
4. Update BOOK_PLAN.md if structure or status changed.
5. Update NOTATION.md if notation changed.
6. Update GLOSSARY.md if terminology changed.
7. Add or update examples if the section benefits from code.
8. Add TODOs for citations or figures when needed.
9. Run available checks/builds if possible.
10. Summarize exactly what changed and what should happen next.

Important Constraints

Do not rewrite the whole book unnecessarily.

Do not delete existing content unless it is clearly wrong, duplicated, or superseded.

Do not introduce notation casually.

Do not create disconnected explanations.

Do not create code that is inconsistent with the text.

Do not pretend a chapter is polished if it is only a stub.

Do not add fake references.

Do not optimize for volume. Optimize for correctness, coherence, and usefulness.

First Task

Start by inspecting the repository.

Then create or update:

book/BOOK_PLAN.md
book/NOTATION.md
book/GLOSSARY.md
book/REVIEW_NOTES.md
book/metadata.yaml
book/bibliography.bib
book/chapters/00-preface.md
book/chapters/01-what-is-audio-signal-processing.md

If these files already exist, improve them rather than replacing them.

After the first pass, report:

1. Files created or modified
2. Current book structure
3. Most important missing sections
4. Next recommended authoring step
