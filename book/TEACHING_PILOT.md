# Teaching Pilot — Foundation Block (Chapters 01–06)

Pilot outline for a **6-session** short course using this manuscript. Goal: validate
pedagogy before any chapter is promoted to `polished`.

## Prerequisites

- Python 3.11+, `pip install -r book/requirements.txt`
- Comfort with basic calculus and complex numbers

## Session map

| Session | Chapters | Core representation | Runnable artifacts |
|---------|----------|---------------------|-------------------|
| 1 | 01–02 | Time samples $x[n]$, $f_s$ | `a440_sine_wave.py`, `phase_click` WAV demos |
| 2 | 03 | Sampling / quantization | `aliasing_demo.py`, `aliasing_*.wav` |
| 3 | 04–05 | Complex sinusoids, Fourier series | `complex_sinusoid_demo.py`, `fourier_series_square_wave.py` |
| 4 | 06 | DFT grid, bins vs Hz | `dft_bin_spacing.py`, `dft_grid.png` |
| 5 | 07–08 | Windowing, STFT | `window_leakage_demo.py`, `stft_spectrogram_demo.py` |
| 6 | Review | Representation comparison matrix | `tests/test_correctness.py`, `solutions/run_verifications.py` |

## Learning outcomes (pilot)

After six sessions, participants should:

1. Convert between sample index, seconds, and Hz without off-by-$f_s$ errors
2. Explain aliasing and bin spacing in their own words
3. Run and interpret at least **three** book examples
4. Pass `solutions/ch01_verify.py` through `ch06_verify.py` (self-check)

## Assessment

- **In-session:** exercises from ch 01–06 (solutions in appendix)
- **Take-home:** modify `a440_sine_wave.py` to plot two cycles (ex 2.4)
- **Optional listening:** compare `phase_click_bad.wav` vs `phase_click_good.wav`

## Pilot log

| Field | Value |
|-------|-------|
| Status | **template** — not yet run with external cohort |
| Instructor | — |
| Date | — |
| Participants | — |
| Chapters promoted | none (remain pedagogically reviewed) |

Record results in `EXTERNAL_REVIEW.md` after first real cohort.

## Instructor notes

- Emphasize the **representation lens** table from ch 01 at the start of each session
- Do not skip `$f_s$` on every slide — it is the #1 source of student bugs
- Use `audio_toolkit` only after session 4; earlier sessions use raw NumPy intentionally
