# Audio Signal Representation and Processing

Technical book manuscript with **tested code**, not just prose. Chapter status reflects *actual*
editorial maturity (see `book/BOOK_PLAN.md`).

## Book contents

Manuscript: [`book/`](book/)

| Chapters | Topic |
|----------|--------|
| 00–01 | Scope, signals, representations |
| 02–03 | Samples, sampling, quantization |
| 04–06 | Sinusoids, Fourier, DFT/FFT |
| 07–08 | Windowing, STFT, spectrograms |
| 09–12 | Convolution, filters, delay, phase |
| 13–14 | Loudness, resampling |
| 15–17 | Features, pitch, musical representations |
| 18–20 | Synthesis, physical modeling, neural audio |
| 21–22 | Testing, toolkit capstone |
| App. | Exercise solutions (ch 01–22, verified scripts) |

Planning and governance: `book/BOOK_PLAN.md`, `book/NOTATION.md`, `book/GLOSSARY.md`,
`book/REVIEW_NOTES.md`, `book/EXTERNAL_REVIEW.md`, `book/TEACHING_PILOT.md`,
`book/TEACHING_PILOT_RUN1.md`, `book/TEACHING_PILOT_RECRUIT.md`.

## Code

### Examples (plots + WAV demos)

```bash
cd book
pip install -r requirements.txt
python tests/run_examples.py
python examples/export_audio_demos.py   # hearable clips in audio_demos/
```

### `audio_toolkit` package

```bash
cd book
python tests/test_correctness.py        # 15 invariants (FFT, STFT, FIR, capstone, CLI, …)
python solutions/run_verifications.py   # ch 01–22 exercise numeric checks
python -m audio_toolkit tone out.wav --f0 440 --duration 1
python -m audio_toolkit analyze out.wav
python -m audio_toolkit filter in.wav out_lp.wav --cutoff 1000
```

Layout: `book/audio_toolkit/` (`io`, `osc`, `spectral`, `filters`, `effects`, `meter`, `synthesis`,
`resample`, `__main__`).

## Build (Pandoc)

```bash
cd book
make html    # single-file HTML
make pdf     # requires LaTeX (see CI artifacts)
make epub
```

CI builds all three formats on each push; download artifacts from the Actions run (`book-html`,
`book-pdf`, `book-epub`).

## Chapter status (honest)

| Status | Meaning |
|--------|---------|
| `stub` | Outline only |
| `draft` | Prose present; not fully vetted |
| `technically reviewed` | Equations, examples, citations checked |
| `pedagogically reviewed` | Teaching clarity, exercises, pitfalls reviewed |
| `polished` | Publication-ready (external review + teaching pilot required) |

**No chapter is `polished` yet.** Chapters **01–12** are `pedagogically reviewed`; **00, 13–22**,
and the appendix are `technically reviewed`. External teaching pilot Run 1 is **seeking an
instructor** (`TEACHING_PILOT_RECRUIT.md`).

## Teaching pilot

- **Run 0:** internal automated dry-run (CI + solution scripts)
- **Run 1:** external cohort — pre-flight in CI; instructor kit in `TEACHING_PILOT_RUN1.md`;
  **recruitment call** in `TEACHING_PILOT_RECRUIT.md` (cohort not yet run)
- After a real cohort: `python book/scripts/record_pilot_run.py --help`

## CI

On push/PR touching `book/**`:

| Job | Checks |
|-----|--------|
| `format` | `black`, `ruff`, `check_formatting.py`, `check_representation_lens.py` |
| `examples` | example smoke tests, 15 correctness tests, ch 01–22 verifications, pilot pre-flight, governance tests |
| `html` / `pdf` / `epub` | Pandoc builds + artifact upload |

## Formatting (before PR)

```bash
pip install -r book/requirements-dev.txt
python -m black book/
python -m ruff check book/ --fix
python book/scripts/check_formatting.py
python book/scripts/wrap_markdown.py   # if prose lines exceed limits
```

Files use **LF** line endings (`.gitattributes`). `requirements.txt` is one package per line.
