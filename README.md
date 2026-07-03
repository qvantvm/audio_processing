# Audio Signal Representation and Processing

Technical book manuscript with **tested code**, not just prose. The repo is a living scaffold: chapter status reflects *actual* editorial maturity.

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
| App. | Exercise solutions (pilot: ch 01–03) |

Planning: `book/BOOK_PLAN.md`, `book/NOTATION.md`, `book/GLOSSARY.md`, `book/REVIEW_NOTES.md`.

## Code

### Examples (plots)

```bash
cd book
pip install -r requirements.txt
python tests/run_examples.py
```

### `audio_toolkit` package

Importable modules used by the capstone chapter and demos:

```bash
cd book
python tests/test_correctness.py      # FFT, Parseval, STFT, FIR, phase, dBFS
python solutions/run_verifications.py # tested exercise numeric answers
```

Layout: `book/audio_toolkit/` (`io`, `osc`, `spectral`, `filters`, `effects`, `meter`).

## Build (Pandoc)

```bash
cd book
make html   # pdf/epub need extra tooling (pdf needs LaTeX)
```

## Chapter status (honest)

Statuses (see `BOOK_PLAN.md` for per-chapter table):

| Status | Meaning |
|--------|---------|
| `stub` | Outline only |
| `draft` | Prose present; not fully vetted |
| `technically reviewed` | Equations, examples, citations checked; may need pedagogy pass |
| `pedagogically reviewed` | Teaching clarity, exercises, pitfalls reviewed |
| `polished` | Publication-ready (requires external review or teaching pilot) |

**No chapter is `polished` yet.** Foundation chapters (01–06) are `pedagogically reviewed`; several later survey chapters (18, 20) remain `draft`.

### Governance rule

A chapter may advance to `technically reviewed` only when:

1. Example scripts for that chapter run in CI (if applicable)
2. Equations and variables are defined consistently with `NOTATION.md`
3. Citations resolve in Pandoc build
4. A second review pass (human or independent agent) is recorded in `REVIEW_NOTES.md`

Promotion to `pedagogically reviewed` or `polished` additionally requires exercise review and teaching clarity checks.

## CI

On push/PR touching `book/**`:

- Example smoke tests
- `audio_toolkit` correctness tests
- Exercise solution verifications
- Pandoc HTML build
