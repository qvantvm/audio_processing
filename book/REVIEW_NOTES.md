# Review Notes

Open issues, review findings, and planned improvements.

## Pass 7 — Complete Manuscript Draft (2026-07-02)

### Completed

- Drafted chapters **07–22** (full template: purpose through further reading)
- Added examples: `window_leakage_demo.py`, `stft_spectrogram_demo.py`, `fir_lowpass_demo.py`, `representation_domains.py`
- Added figures: `window_leakage.png`, `stft_chirp_spectrogram.png`, `fir_lowpass.png`, `representation_domains.png`
- Added `requirements.txt`, `tests/run_examples.py`, updated `README.md`
- All chapters 00–22 marked **draft** in `BOOK_PLAN.md`

### Correctness / Clarity (Polish Backlog)

- [ ] Full read-through for math/notation consistency across 23 chapters
- [ ] Add missing bibliography entries (Harris, YIN, DDSP, BS.1770, SMS)
- [ ] Replace TODO citation placeholders in Ch 7, 13, 17, 20
- [ ] Pandoc `@sec:` cross-references between chapters
- [ ] Chapter 20 neural section: add verified citations only

### Examples / CI

- [x] Nine example scripts present
- [x] `tests/run_examples.py` smoke harness
- [ ] Run `make html` in CI when Pandoc available
- [ ] Optional: WAV I/O in toolkit chapter with `soundfile`

### Status Promotion Criteria

Promote chapter from **draft** → **reviewed** when:

1. Second-pass edit complete
2. All cited keys resolve in `bibliography.bib`
3. Referenced examples run
4. Exercises spot-checked

Promote **reviewed** → **polished** after external review or teaching pilot.

---

## Earlier Passes (summary)

| Pass | Focus |
|------|--------|
| 1 | Scaffold, preface, Ch 01 |
| 2 | Ch 02, A440 example |
| 3 | Ch 03, aliasing/quantization |
| 4 | Ch 04, complex sinusoids |
| 5 | Ch 05, Fourier series |
| 6 | Ch 06, DFT/bin spacing |

## Future Review Checklist (per section)

1. Definitions precede use
2. Math symbols in `NOTATION.md`
3. New terms in `GLOSSARY.md`
4. Audio intuition + math balanced
5. Pitfalls name real mistakes
6. Code runs (NumPy/SciPy/Matplotlib)
