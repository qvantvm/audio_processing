# Teaching Pilot Run 1 — Recruitment Call

The foundation block (ch **01–06**) is **ready for an external instructor-led cohort**. Automated
pre-flight passes in CI; this document is for humans who can teach six 90-minute sessions.

## Who we need

- Instructor with DSP or audio programming background (graduate TA, workshop lead, or engineer)
- **3–12 participants** comfortable with Python and basic calculus
- Six sessions over 2–4 weeks (in-person or remote)

## What you get

| Resource | Location |
|----------|----------|
| Session agendas + timing | `TEACHING_PILOT_RUN1.md` |
| Pilot overview | `TEACHING_PILOT.md` |
| Exercise solutions | `chapters/23-appendix-exercise-solutions.md` |
| Runnable demos | `examples/`, `audio_demos/` (generate via `export_audio_demos.py`) |
| Pre-flight checker | `scripts/run_pilot_preflight.py` |

## Before session 1

```bash
git clone https://github.com/qvantvm/audio_processing.git
cd audio_processing
pip install -r book/requirements.txt
python book/scripts/run_pilot_preflight.py   # must pass
python book/examples/export_audio_demos.py   # fresh WAV demos
```

## After the cohort

1. Collect feedback using the questionnaire in `TEACHING_PILOT_RUN1.md`
2. Log results:

```bash
python book/scripts/record_pilot_run.py \
  --date "2026-MM-DD" \
  --instructor "Your Name" \
  --institution "Your Org" \
  --participants 8 \
  --completion-rate "7/8" \
  --mean-rating 4.1 \
  --issues "Describe any blocking pedagogical issues"
```

3. Open a PR or issue with the updated log files for maintainer review
4. **Do not** mark chapters `polished` until `EXTERNAL_REVIEW.md` has **approved** sign-off

Use the GitHub issue template **Teaching pilot report** (label `teaching-pilot`) when filing results.

## Optional extension (sessions 7–8)

After the foundation block, ch **07–08** (windowing, STFT) are `pedagogically reviewed` and can
extend the pilot for participants who want spectrogram depth. Use `window_leakage_demo.py` and
`stft_spectrogram_demo.py`.

Further optional sessions **9–10** cover ch **10–12** (FIR/IIR, delay lines, group delay) for
participants continuing past the foundation block. Sessions **11–12** may cover ch **13–15**
(loudness, resampling, features) for MIR-oriented cohorts.

## Contact / reporting

Report interest or completed runs via GitHub issue on the repository with label `teaching-pilot`
(template: **Teaching pilot report**). Include participant count (not names), mean ratings, and
blocking issues only.

## Current status

| Item | Status |
|------|--------|
| Materials | **ready** (Pass 26 pre-flight) |
| External cohort | **not yet run** |
| Chapters `polished` | **none** |
