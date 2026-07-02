# Neural Audio Representations

## Purpose

Deep learning adds **learned representations**: encoder networks map waveforms or spectrograms to embeddings; generative models synthesize in latent or spectral domains. This chapter situates neural methods relative to classical DSP— when they replace, complement, or inherit STFT-based pipelines.

## Learning Objectives

By the end of this chapter, the reader should be able to:

1. Contrast **waveform**, **spectrogram**, and **learned latent** model inputs/outputs
2. Describe encoder–decoder and **VAE/autoencoder** embeddings for audio
3. Explain **differentiable STFT** layers bridging classical and neural views
4. Identify pitfalls: phase, aliasing in vocoders, dataset bias
5. Evaluate hybrid systems (neural enhancer + classical SRC)

## Main Concepts

### Representation choices

| Domain | Examples | Pros / cons |
|--------|----------|-------------|
| Waveform | WaveNet, SampleRNN | End-to-end; long receptive field costly |
| Spectrogram | U-Net vocoders, diffusion on mel | Leverages STFT intuition; phase challenge |
| Latent | VAE, RVQ codecs (EnCodec) | Compact; may lose fine detail |
| Hybrid | DDSP, neural + sinusoidal | Interpretable partials + learned residuals |

### Learned features

CNN on log-mel → embedding for classification/tagging— replaces hand-crafted MFCCs when data abundant; still needs careful STFT front-end often.

### Generative audio

**GAN vocoders, diffusion, autoregressive** models generate mel or waveform. **Griffin–Lim**-class phase estimation largely superseded but phase remains issue in naive pipelines.

### Differentiable DSP

STFT/ISTFT inside network (torchaudio, nnAudio)— gradients flow to analysis parameters; risk of committing same window/leakage mistakes as classical chain.

### Codecs as representations

Neural codecs (Lyra, EnCodec, DAC) learn discrete codes for low-bitrate speech/music— representation for transmission and ML.

## Mathematical Formulation

Autoencoder:

$$
\mathbf{z} = E_\theta(x), \quad \hat{x} = D_\phi(\mathbf{z}), \quad \mathcal{L} = \|x-\hat{x}\|^2 + \lambda \|\mathbf{z}\|_1 \ldots
$$

Mel loss common: $\|\text{Mel}(x)-\text{Mel}(\hat{x})\|_1$— perceptually weighted but incomplete.

## Audio Interpretation

**Source separation (Demucs):** time-domain U-Net learns masks— classical STFT mask learning related.

**Voice conversion:** content embedding + pitch + timbre disentanglement (idealized).

**Style transfer on timbre:** swap embeddings while preserving F0 contour (hard).

## Implementation Notes

```python
import torchaudio
spec = torchaudio.transforms.MelSpectrogram(sample_rate=fs, n_fft=1024)
```

Reproducibility: fix weights, sample rate, mel config; report SI-SDR, PESQ, listening tests (Chapter 21).

## Worked Example

**Problem:** Model trains on 16 kHz mono log-mel. Deploy on 48 kHz stereo field recording— what breaks?

**Answer:** Bandwidth/sample rate mismatch, channel layout, noise domain shift; need resample/mono policy and likely fine-tune.

## Common Pitfalls

1. **Training on mel, inferring waveform** without strong vocoder.
2. **Ignoring causal latency** for real-time models.
3. **Overfitting small datasets** with huge models.
4. **Treating embeddings as perceptually linear** without validation.

## Exercises

1. Sketch pipeline: WAV → mel → U-Net → mel → Griffin–Lim → WAV; list failure modes.
2. Why DDSP keeps explicit $f_0$ control?
3. Compare param count: MFCC+SVM vs small CNN on same task (conceptual).
4. When is classical STFT feature pipeline still preferable?

## Further Reading

- Dieleman et al., neural audio generation surveys (TODO citation)
- Engel et al., DDSP (TODO citation)
- Smith + STFT differentiable layers cross-ref [@smith2011spectral]

**Next chapter:** Chapter 21 — *Testing, Measurement, and Numerical Pitfalls*.
