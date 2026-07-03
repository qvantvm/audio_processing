# Hearable artifact demos

Short WAV clips for listening exercises. **Not committed** — generate locally:

```bash
cd book
python examples/export_audio_demos.py
python examples/wavetable_demo.py
python examples/spectrogram_frontend_demo.py
```

| File | Chapter | Artifact |
|------|---------|----------|
| `aliasing_3500hz_at_4kfs.wav` | 03 | Aliasing fold |
| `phase_click_bad.wav` / `phase_click_good.wav` | 02 | Block boundary clicks |
| `naive_saw_2200hz.wav` | 18 | Aliased sawtooth |
| `comb_resonator.wav` | 11 | Comb resonance |
| `leakage_two_tone_440_444.wav` | 07 | Beating pair for leakage analysis |
| `two_tone_for_stft.wav` | 20 | Input for STFT front-end |

Use headphones at **low volume**.
