# Review Notes

Open issues, review findings, and planned improvements.

## Pass 20 — Solutions ch 16–17, resample Module, Pilot Dry-Run (2026-07-03)

### Completed

- **`audio_toolkit.resample`** — `resample()`, `midi_to_hz()`; ch 14 + ch 22 docs
- Exercise solutions + verify scripts for **ch 16–17**
- Teaching pilot **Run 0** internal dry-run logged (`TEACHING_PILOT.md`, `EXTERNAL_REVIEW.md`)
- Correctness test: `test_resample_preserves_tone`

### Remaining gaps

- [ ] Exercise solutions ch 18+
- [ ] External teaching cohort (Run 1)
- [ ] PDF CI (LaTeX)

---

## Pass 19 — Solutions ch 13–15, Diagrams, Teaching Pilot (2026-07-03)

### Completed

- Exercise solutions + verify scripts for **ch 13–15** (loudness, SRC, features)
- Diagrams: `modal_bank.png` (ch 19), `neural_audio_pipeline.png` (ch 20)
- **`TEACHING_PILOT.md`** — 6-session outline for ch 01–06 foundation block

### Remaining gaps

- [ ] Exercise solutions ch 16+
- [ ] Run teaching pilot with external cohort; log in `EXTERNAL_REVIEW.md`
- [ ] Production resampling in `audio_toolkit`
- [ ] PDF CI (LaTeX)

---

## Pass 18 — Solutions ch 10–12, External Review Log, Diagrams (2026-07-03)

### Completed

- Exercise solutions appendix + verify scripts for **ch 10–12**
- **`EXTERNAL_REVIEW.md`** — per-chapter review log (all sign-offs pending external)
- Block diagrams: `dft_grid.png`, `comb_allpass_structures.png`, `phase_group_delay.png`
- Cross-links from ch 10–12 exercises to appendix

### Remaining gaps

- [ ] Exercise solutions ch 13+
- [ ] External reviewer sign-off in `EXTERNAL_REVIEW.md`
- [ ] PDF CI (LaTeX)
- [ ] Modal bank / neural pipeline diagrams

---

## Pass 17 — Formatting Discipline & Engineering Hygiene (2026-07-03)

### Response to formatting critique

Git objects already stored multi-line files with LF newlines; `requirements.txt` has one
package per line. The **raw-view “single line” problem** was partly long unwrapped prose
paragraphs (500+ chars). This pass adds enforcement:

1. **`pyproject.toml`** — black (100 cols) + ruff
2. **`book/scripts/check_formatting.py`** — fails on single-line corruption, bad requirements, missing final newlines, extreme prose lines
3. **`book/scripts/wrap_markdown.py`** — wraps prose to 100 columns
4. **`.gitattributes`** — `text=auto eol=lf`
5. **CI `format` job** — `black --check`, `ruff`, structure check (gates examples/html)
6. **Artifact labeling** — `naive_saw` / `naive_saw_artifact` marked `ImplQuality.ARTIFACT`
7. **Tighter tests** — STFT RMSE 0.04, COLA L2 test, WAV round-trip SNR
8. **Diagrams** — `adc_dac_chain.png`, `fir_iir_structures.png`

### Completed earlier (Pass 16)

- Representation lens in ch **07–17**
- Exercise solutions ch **01–09**

### Remaining gaps

- [ ] Exercise solutions ch 10+
- [ ] External / second-model review log per chapter
- [ ] PDF CI (LaTeX)
- [ ] Production-quality resampling module (vs pedagogical)

---

## Pass 16 — Representation Lens ch 07–17, Solutions 07–09 (2026-07-03)

### Completed

- **Representation lens** tables added to chapters **07–17** (11 chapters)
- **Exercise solutions** — appendix + verify scripts for ch 07–09
- **WAV demo** — `leakage_two_tone_440_444.wav` in `export_audio_demos.py`
- **Block diagram** — `stft_framing.png` via `stft_framing_diagram.py`; referenced in ch 08

### Remaining gaps

- [ ] Exercise solutions ch 10+
- [ ] More block diagrams (ADC/DAC, FIR/IIR)
- [ ] PDF CI (LaTeX)
- [ ] External / second-model review per chapter

### Chapter status summary

| Status | Chapters |
|--------|----------|
| pedagogically reviewed | 01–06 |
| technically reviewed | 00, 07–22, appendix A |

---

## Pass 15 — ch 18/20 Depth, WAV Demos, Solutions 04–06 (2026-07-03)

### Completed

- **`audio_toolkit.synthesis`** — wavetable + naive saw oscillators
- **WAV audio demos** — `export_audio_demos.py` (aliasing, phase clicks, saw, comb); `audio_demos/README.md`
- **Ch 18** — representation lens, wavetable demo + figure; promoted to `technically reviewed`
- **Ch 20** — representation lens, `spectrogram_frontend_demo.py`; promoted to `technically reviewed`
- **Exercise solutions** — appendix + verify scripts for ch 04–06; appendix promoted to `technically reviewed`
- **Tests** — wavetable pitch test; new examples in CI smoke suite

### Remaining gaps

- [ ] Representation lens sections in ch 07–17
- [ ] More block diagrams
- [ ] Exercise solutions ch 07+
- [ ] PDF CI (LaTeX)
- [ ] External / second-model review per chapter

### Chapter status summary

| Status | Chapters |
|--------|----------|
| pedagogically reviewed | 01–06 |
| technically reviewed | 00, 07–22, appendix A |

---

## Pass 14 — Honest Status, audio_toolkit, Correctness Tests (2026-07-03)

### Response to external critique

The manuscript previously overclaimed `reviewed` / `polished` status. This pass:

1. **Status model** — `stub` → `draft` → `technically reviewed` → `pedagogically reviewed` →
`polished`
2. **Demotions** — ch 18, 20 → `draft`; removed false `polished` from 00–03; no chapter is
`polished`
3. **`audio_toolkit/`** — importable package (`io`, `osc`, `spectral`, `filters`, `effects`,
`meter`)
4. **Correctness tests** — `tests/test_correctness.py` (FFT, Parseval, STFT, FIR, phase, dBFS,
Karplus)
5. **`solutions/`** — `ch01_verify.py` … `ch03_verify.py` with tested numeric answers
6. **Chapter depth** — ch 01 representation matrix; ch 02 code completeness; ch 19 Karplus–Strong
demo; ch 22 documents real package
7. **Governance** — README + BOOK_PLAN rules for status promotion
8. **CI** — correctness tests + solution verifications added

### Markdown formatting

Raw files in this repo use normal newlines (verified locally). `.editorconfig` added for consistent
editing. If a viewer shows single-line files, re-normalize with a line-based editor before editing.

### Remaining gaps

- [ ] ch 18, 20 still `draft` — need runnable examples and representation lens
- [ ] Audio WAV demos (not only PNG plots)
- [ ] More block diagrams in `figures/`
- [ ] Exercise solutions for ch 04+
- [ ] PDF CI (LaTeX)
- [ ] External / second-model review pass per chapter

### Chapter status summary

| Status | Chapters |
|--------|----------|
| pedagogically reviewed | 01–06 |
| technically reviewed | 00, 07–17, 19, 21–22 |
| draft | 18, 20, appendix A |

---

## Pass 13 — Exercise Solutions Appendix; Foundation Polish (2026-07-03)

(Superseded status claims — see Pass 14 demotions.)

---

## Pass 12 — Cross-Reference Fix; Foundation Chapter Links (2026-07-03)

### Completed

- Converted **83** `@sec:ch-...` references to Pandoc Markdown links
- HTML build: no citeproc `sec:ch-...` citation warnings
- Foundation block (ch 00–06): plain "Chapter N" refs → internal links

---

## Status Promotion Criteria

**technically reviewed** requires: examples run, notation consistent, citations resolve, second
review logged.

**pedagogically reviewed** requires: exercises checked, pitfalls grounded, teaching clarity pass.

**polished** requires: external review, teaching pilot, or dedicated publication proofread.

## Future Review Checklist (per section)

1. Definitions precede use
2. Math symbols in `NOTATION.md`
3. New terms in `GLOSSARY.md`
4. Representation lens: what / preserves / discards / maps / mistakes / artifacts
5. Pitfalls name real mistakes
6. Code runs and correctness tests cover claims
