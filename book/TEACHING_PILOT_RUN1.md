# Teaching Pilot Run 1 — Instructor Kit

Companion to `TEACHING_PILOT.md`. Use this document when recruiting and running the **external**
foundation-block cohort (ch 01–06). Automated pre-flight (`scripts/run_pilot_preflight.py`) verifies
materials; this kit guides live instruction and feedback capture.

## Recruitment checklist

- [ ] Confirm participants have Python 3.11+ and can run `pip install -r book/requirements.txt`
- [ ] Share repository link and `TEACHING_PILOT.md` prerequisites
- [ ] Schedule six 90-minute sessions (or three 3-hour blocks)
- [ ] Run `python book/scripts/run_pilot_preflight.py` the day before session 1
- [ ] Generate fresh WAV demos: `python book/examples/export_audio_demos.py`

## Session agendas (90 minutes each)

### Session 1 — Time samples and $f_s$ (ch 01–02)

| Block | Minutes | Activity |
|-------|---------|----------|
| Opening | 10 | Representation lens table (ch 01); define $x[n]$, $f_s$, $T_s$ |
| Demo | 20 | Run `examples/a440_sine_wave.py`; discuss period in samples |
| Listening | 15 | `phase_click_bad.wav` vs `phase_click_good.wav` |
| Exercise | 30 | ch 01 ex 1.1–1.2, ch 02 ex 2.1 in pairs |
| Close | 15 | Self-check: `solutions/ch01_verify.py`, `ch02_verify.py` |

**Discussion prompts:** Why is peak normalization not the same as loudness? What breaks if $f_s$ is
wrong in a filter coefficient?

### Session 2 — Sampling and aliasing (ch 03)

| Block | Minutes | Activity |
|-------|---------|----------|
| Review | 10 | Nyquist inequality; fold formula |
| Demo | 25 | `examples/aliasing_demo.py` + `aliasing_3500hz_at_4kfs.wav` |
| Exercise | 35 | ch 03 exercises; work quantization SNR estimate |
| Close | 20 | `solutions/ch03_verify.py`; recap aliasing as representation failure |

### Session 3 — Complex sinusoids and Fourier series (ch 04–05)

| Block | Minutes | Activity |
|-------|---------|----------|
| Demo | 25 | `complex_sinusoid_demo.py`, `fourier_series_square_wave.py` |
| Board | 20 | Phasor view; orthogonal sinusoids; Gibbs ringing intuition |
| Exercise | 30 | ch 04–05 selected exercises |
| Close | 15 | `solutions/ch04_verify.py`, `ch05_verify.py` |

### Session 4 — DFT bins vs Hz (ch 06)

| Block | Minutes | Activity |
|-------|---------|----------|
| Demo | 30 | `dft_bin_spacing.py`, inspect `figures/dft_grid.png` |
| Exercise | 40 | Bin spacing, leakage preview, Parseval sanity check |
| Close | 20 | `solutions/ch06_verify.py` |

### Session 5 — Windowing and STFT (ch 07–08)

| Block | Minutes | Activity |
|-------|---------|----------|
| Demo | 25 | `window_leakage_demo.py`, `leakage_two_tone_440_444.wav` |
| Demo | 25 | `stft_spectrogram_demo.py`; hop vs time resolution |
| Exercise | 25 | ch 07–08 conceptual exercises |
| Close | 15 | Optional: run `solutions/ch07_verify.py` if time |

### Session 6 — Review and assessment (ch 01–06)

| Block | Minutes | Activity |
|-------|---------|----------|
| Review | 20 | Representation comparison matrix; student teach-back |
| Lab | 40 | Take-home variant: plot two cycles in `a440_sine_wave.py` |
| Tests | 20 | Walk through `tests/test_correctness.py` (what each invariant checks) |
| Feedback | 10 | Distribute questionnaire below |

## Participant feedback questionnaire

Rate 1 (strongly disagree) – 5 (strongly agree).

1. I can convert between samples, seconds, and Hz without help.
2. I can explain aliasing and why it is a representation error.
3. I can relate DFT bin index $k$ to frequency in Hz.
4. The runnable examples helped more than prose alone.
5. Exercise difficulty was appropriate for my background.
6. I would recommend this foundation block to a colleague.

**Open response:** What single concept was hardest? What should we add or cut?

**Open response:** Which demo or exercise should stay mandatory for Run 2?

## Run 1 log (instructor fills after cohort)

| Field | Value |
|-------|-------|
| Status | **pending** — external cohort not yet run |
| Date(s) | |
| Instructor | |
| Institution | |
| Participants (n) | |
| Completion rate | |
| Mean rating Q1–Q6 (1–5) | |
| Blocking issues | |
| Chapters promoted | none until sign-off |
| Sign-off | **pending** |

After the cohort, copy summary rows into `TEACHING_PILOT.md` (Run 1 section) and
`EXTERNAL_REVIEW.md` (Teaching pilot block). No chapter advances to `polished` without **approved**
external sign-off.

## Post-pilot actions

1. File GitHub issue or `REVIEW_NOTES.md` entry for each blocking pedagogical issue
2. Update appendix solutions if cohort found numeric or notation errors
3. Re-run `run_pilot_preflight.py` and full CI before Run 2
