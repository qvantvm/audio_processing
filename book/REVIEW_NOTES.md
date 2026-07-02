# Review Notes

Open issues, review findings, and planned improvements. Update after each authoring pass.

## Pass 4 — Chapter 04, Complex Sinusoids (2026-07-02)

### Completed

- Drafted `04-sinusoidal-signals-and-complex-numbers.md`
- Added `examples/complex_sinusoid_demo.py` (verified runnable)
- Generated `figures/complex_phasor.png`
- Updated `BOOK_PLAN.md`, `NOTATION.md`, `GLOSSARY.md`

### Correctness / Clarity

- [ ] Chapter 04: Hilbert/analytic signal preview is forward reference only— expand in Chapter 12
- [ ] Add explicit note on `np.unwrap` for STFT phase plots when Chapter 8 is written

### Missing Content (High Priority)

- [ ] Chapter 05 draft: Fourier series and orthogonal sinusoid decomposition
- [ ] Figure: representation domains overview diagram
- [ ] `examples/fourier_series_square_wave.py`

### Code / Examples

- [x] `complex_sinusoid_demo.py` runs and writes figure
- [ ] Smoke-test all examples in one script

---

## Pass 3 — Chapter 03, Aliasing and Quantization (2026-07-02)

### Completed

- Drafted `03-sampling-quantization-and-digital-audio.md`
- Added `examples/aliasing_demo.py` (verified runnable)
- Generated `figures/aliasing_fold.png`, `figures/quantization_staircase.png`
- Updated `BOOK_PLAN.md`, `NOTATION.md`, `GLOSSARY.md`

### Correctness / Clarity

- [ ] Chapter 03: Expand reconstruction (sinc interpolation) when Chapter 14 covers resampling
- [ ] Chapter 03: WAV byte packing (24-bit in 3 bytes) varies by format— add caveat if file I/O chapter added
- [ ] Dither section is brief; expand in dynamics chapter or dedicated sidebar

### Missing Content (High Priority)

- [ ] Chapter 04 draft: complex sinusoids, Euler form, phasor plot
- [ ] Figure: representation domains overview diagram
- [ ] `examples/complex_sinusoid_demo.py`

### Citations

- [x] Shannon and Oppenheim cited in Chapter 03
- [ ] Verify brandenburg1999mp3 entry if compression chapter expands

### Code / Examples

- [x] `aliasing_demo.py` runs and writes both figures
- [ ] Smoke-test all examples in one script

---

## Pass 2 — Chapter 02 and A440 Example (2026-07-02)

### Completed

- Drafted `02-signals-time-and-samples.md` (full chapter template)
- Added `examples/a440_sine_wave.py` (verified runnable)
- Generated `figures/a440_samples.png`
- Updated `BOOK_PLAN.md`, `NOTATION.md`, `GLOSSARY.md`

### Correctness / Clarity

- [ ] Chapter 02: Clarify duration convention ($N/f_s$ vs. $(N-1)/f_s$) when linking to specific libraries (NumPy, librosa, JUCE)
- [ ] Chapter 02: Optional listening exercise needs a tiny WAV writer or scipy dependency note
- [ ] Add cross-reference from Chapter 01 worked example to Chapter 02 sinusoid section

### Missing Content (High Priority)

- [x] Chapter 03 draft: sampling theorem, aliasing, quantization
- [x] Figure: aliasing (`figures/aliasing_fold.png`)
- [x] Figure: quantization staircase
- [x] `examples/aliasing_demo.py`

### Notation / Terminology

- [ ] dBFS and SPL fully developed in Chapter 13; glossary entries are introductory only
- [ ] Add block/frame index notation when STFT chapter is drafted

### Citations

- [ ] Chapter 03 may cite Shannon sampling; verify bib entry usage

### Build / Tooling

- [ ] Test `make html` when Pandoc available
- [ ] Consider `requirements.txt` for examples (numpy, matplotlib)

### Code / Examples

- [x] `a440_sine_wave.py` runs and writes figure
- [ ] Add minimal smoke test script or CI job for examples

### Style

- Chapter 02 matches Chapter 01 section template

---

## Pass 1 — Initial Scaffold (2026-07-02)

### Completed

- Created book directory structure and build Makefile
- Added `BOOK_PLAN.md`, `NOTATION.md`, `GLOSSARY.md`, `REVIEW_NOTES.md`
- Added Pandoc `metadata.yaml` and starter `bibliography.bib`
- Drafted `00-preface.md` and `01-what-is-audio-signal-processing.md`

### Correctness / Clarity

- [x] Chapter 02 exists — partial address of Chapter 01 cross-ref TODO
- [ ] Preface: Confirm title and author metadata before publication
- [ ] Verify all bibliography keys resolve when cited chapters grow

### Missing Content (from Pass 1 — status updated)

- [x] Chapter 02 draft
- [x] `examples/a440_sine_wave.py`
- [x] `figures/a440_samples.png`
- [ ] Diagram: representation domains (time, frequency, time–frequency, parametric)

## Future Review Checklist (per section)

When editing any section, verify:

1. Definitions precede use
2. Math symbols appear in `NOTATION.md`
3. New terms appear in `GLOSSARY.md`
4. Audio intuition accompanies formulas
5. Pitfalls section names a common mistake explicitly
6. Code runs without undeclared dependencies beyond NumPy/SciPy/Matplotlib
