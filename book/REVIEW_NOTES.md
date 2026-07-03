# Review Notes

Open issues, review findings, and planned improvements.

## Pass 28 — Pedagogy ch 10–12, Pilot Issue Template (2026-07-03)

### Completed

- **Pedagogical review** — ch **10–12** promoted (FIR/IIR, delay/comb, phase/group delay)
- **GitHub issue template** — `.github/ISSUE_TEMPLATE/teaching_pilot_report.yml` for cohort reporting
- Optional pilot extension sessions 9–10 (ch 10–12) in `TEACHING_PILOT_RECRUIT.md`

### Remaining gaps

- [ ] External teaching cohort Run 1 with **real participants**
- [ ] No chapter `polished` without `EXTERNAL_REVIEW.md` **approved** sign-off

---

## Pass 27 — Pedagogy ch 07–09, Recruitment Call (2026-07-03)

### Completed

- **Pedagogical review** — ch **07–09** promoted (representation lens, exercises, solutions, examples,
  pitfalls verified)
- **`TEACHING_PILOT_RECRUIT.md`** — external instructor recruitment one-pager
- **Glossary** — coherent gain entry
- Optional pilot extension sessions 7–8 (ch 07–08) documented

### Remaining gaps

- [ ] External teaching cohort Run 1 with **real participants** (recruitment doc published; not run)
- [ ] No chapter `polished` without `EXTERNAL_REVIEW.md` **approved** sign-off

---

## Pass 26 — Foundation Representation Lens, Governance CI (2026-07-03)

### Completed

- **Representation lens** tables added to ch **02–06** and **21** (complete ch 02–22 coverage)
- **`check_representation_lens.py`** — CI gate for lens sections (ch 01 exempt: comparison matrix)
- **`test_governance.py`** — smoke test for `record_pilot_run.py` on temp copy + lens checker
- **HTML build** — `--standalone --self-contained` for portable artifact; `make all-formats` target

### Remaining gaps

- [ ] External teaching cohort Run 1 with **real participants** (cannot be simulated)
- [ ] Broadcast-grade SRC (libsamplerate/SoX) — out of scope for in-repo toolkit

---

## Pass 25 — HTML Artifact, Filter CLI, Pilot Log Helper (2026-07-03)

### Completed

- **HTML CI artifact** — `book-html` upload alongside PDF/EPUB
- **`audio_toolkit filter`** — FIR lowpass subcommand; extended `test_audio_toolkit_cli`
- **`record_pilot_run.py`** — instructor CLI to log real Run 1 cohort results (no fake data)
- **README** — honest chapter status, CI artifact table, CLI examples, teaching pilot notes

### Remaining gaps

- [ ] External teaching cohort Run 1 with **real participants** (use `record_pilot_run.py` after)
- [ ] Broadcast-grade SRC (libsamplerate/SoX) — out of scope for in-repo toolkit

---

## Pass 24 — EPUB CI, Resample Quality Tiers, Run 1 Kit (2026-07-03)

### Completed

- **EPUB CI** — `epub` job with figure generation, `make epub`, artifact upload
- **`resample(..., quality=ImplQuality)`** — `PEDAGOGICAL` (default) vs `RECOMMENDED` (stronger Kaiser)
- **`TEACHING_PILOT_RUN1.md`** — session agendas, feedback questionnaire, Run 1 log template
- `run_pilot_preflight.py` checks instructor kit exists
- `test_resample_recommended_quality` in correctness suite (15 tests)

### Remaining gaps

- [ ] External teaching cohort Run 1 with **real participants** (kit ready; cohort not executed)
- [ ] HTML artifact upload in CI (optional)
- [ ] Broadcast-grade SRC (libsamplerate/SoX) — out of scope for in-repo toolkit

---

## Pass 23 — PDF CI, Toolkit CLI, Pilot Pre-flight (2026-07-03)

### Completed

- **PDF CI** — GitHub Actions `pdf` job: TeX Live + figure generation + `make pdf` + artifact upload
- **`audio_toolkit.__main__`** — `analyze` and `tone` subcommands; tested in `test_audio_toolkit_cli`
- **`run_pilot_preflight.py`** — automated Run 1 materials check (ch 01–06); runs in CI
- Makefile `--resource-path=.:chapters:figures` for Pandoc image resolution
- HTML CI now generates figures before build (fixes missing images)

### Remaining gaps

- [ ] External teaching cohort Run 1 with **real participants** (pre-flight ≠ cohort)
- [ ] EPUB CI (optional)
- [ ] Production resampling in `audio_toolkit`

---

## Pass 22 — Capstone Solutions, Integration Test (2026-07-03)

### Completed

- Exercise solutions appendix for **ch 22** (capstone toolkit)
- `ch22_verify.py` — WAV SNR, Schroeder comb tail decay, Karplus WAV round-trip
- **`test_toolkit_capstone_pipeline`** — synthesize → filter → meter → STFT → WAV in correctness suite
- Appendix + `run_verifications.py` now cover **ch 01–22**

### Remaining gaps

- [ ] External teaching cohort Run 1 execution
- [ ] PDF CI (LaTeX)
- [ ] Optional `audio_toolkit.__main__` CLI (ex 22.4)

---

## Pass 21 — Solutions ch 18–21, Wavetable Diagram (2026-07-03)

### Completed

- Exercise solutions + verify scripts for **ch 18–21** (all non-capstone chapters with exercises)
- `wavetable_structure.png` diagram in ch 18
- Teaching pilot Run 1 marked **ready for recruitment** with checklist
- Appendix covers **ch 01–21**

### Remaining gaps

- [ ] ch 22 capstone exercise solutions
- [ ] External teaching cohort Run 1 execution
- [ ] PDF CI (LaTeX)

---

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
