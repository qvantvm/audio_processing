# Review Notes

Open issues, review findings, and planned improvements. Update after each authoring pass.

## Pass 1 — Initial Scaffold (2026-07-02)

### Completed

- Created book directory structure and build Makefile
- Added `BOOK_PLAN.md`, `NOTATION.md`, `GLOSSARY.md`, `REVIEW_NOTES.md`
- Added Pandoc `metadata.yaml` and starter `bibliography.bib`
- Drafted `00-preface.md` and `01-what-is-audio-signal-processing.md`

### Correctness / Clarity

- [ ] Chapter 01: Add cross-reference links once Chapter 02–03 exist
- [ ] Preface: Confirm title and author metadata before publication
- [ ] Verify all bibliography keys resolve when cited chapters grow

### Missing Content (High Priority)

- [ ] Chapter 02 draft: discrete-time signals, units, normalization
- [ ] Executable example: `examples/a440_sine_wave.py`
- [ ] Figure: discrete samples of A440 sine (`figures/a440_samples.png`)
- [ ] Diagram: representation domains (time, frequency, time–frequency, parametric)

### Notation / Terminology

- [ ] Add STFT and z-transform sections to `NOTATION.md` as those chapters are written
- [ ] Align decibel conventions (dBFS, dB SPL) in Chapter 13; flag in glossary when added

### Citations

- [ ] Chapter 01 uses general references; add specific citations when making historical claims
- [ ] TODO: citation needed for loudness standards (EBU R128 / ITU-R BS.1770) in later chapters

### Build / Tooling

- [ ] Test `make html` in CI or locally on each major pass
- [ ] PDF build requires LaTeX; document optional dependency in README

### Code / Examples

- [ ] No runnable examples yet; next pass should add at least one verified script

### Style

- Chapter 01 follows template; subsequent chapters should match section headings for consistency

## Future Review Checklist (per section)

When editing any section, verify:

1. Definitions precede use
2. Math symbols appear in `NOTATION.md`
3. New terms appear in `GLOSSARY.md`
4. Audio intuition accompanies formulas
5. Pitfalls section names a common mistake explicitly
6. Code runs without undeclared dependencies beyond NumPy/SciPy/Matplotlib
