# audio_processing

Technical book: **Audio Signal Representation and Processing** — from samples to spectra, filters, and features.

## Book contents

Manuscript lives in [`book/`](book/):

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

Planning docs: `book/BOOK_PLAN.md`, `book/NOTATION.md`, `book/GLOSSARY.md`, `book/REVIEW_NOTES.md`.

## Examples

From `book/` after installing dependencies:

```bash
pip install -r requirements.txt
python examples/a440_sine_wave.py
python examples/dft_bin_spacing.py
# see book/examples/ for full list
```

## Build (Pandoc)

```bash
cd book
make html   # or pdf, epub — requires pandoc; pdf also needs LaTeX
```

## Status

All chapters 00–22 are **draft** quality: structurally complete with exercises and references; polish/review pass tracked in `REVIEW_NOTES.md`.
