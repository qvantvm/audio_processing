"""CLI entry point: run from ``book/`` with ``python -m audio_toolkit``."""

from __future__ import annotations

import argparse

from .io import read_wav, write_wav
from .meter import linear_to_dbfs, peak_amplitude, rms
from .osc import PhaseOscillator


def _cmd_analyze(args: argparse.Namespace) -> int:
    x, fs = read_wav(args.wav)
    if x.ndim > 1:
        x = x[:, 0]
    pk = peak_amplitude(x)
    r = rms(x)
    print(f"file: {args.wav}")
    print(f"fs: {fs} Hz")
    print(f"samples: {len(x)}")
    print(f"peak: {pk:.6f} ({linear_to_dbfs(pk):.2f} dBFS)")
    print(f"rms: {r:.6f} ({linear_to_dbfs(r):.2f} dBFS)")
    return 0


def _cmd_tone(args: argparse.Namespace) -> int:
    osc = PhaseOscillator(args.fs, args.f0, amplitude=args.amplitude)
    n = max(1, int(round(args.duration * args.fs)))
    y = osc.render(n)
    write_wav(args.output, y, args.fs)
    print(f"Wrote {args.output}: {args.f0} Hz, {args.duration}s at {args.fs} Hz")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="audio_toolkit", description="Book toolkit CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    analyze = sub.add_parser("analyze", help="Report peak and RMS on a WAV file")
    analyze.add_argument("wav", help="Input WAV path")
    analyze.set_defaults(func=_cmd_analyze)

    tone = sub.add_parser("tone", help="Write a phase-continuous sine tone WAV")
    tone.add_argument("output", help="Output WAV path")
    tone.add_argument("--f0", type=float, default=440.0, help="Frequency in Hz")
    tone.add_argument("--duration", type=float, default=1.0, help="Duration in seconds")
    tone.add_argument("--fs", type=int, default=48_000, help="Sample rate in Hz")
    tone.add_argument("--amplitude", type=float, default=0.8, help="Peak amplitude")
    tone.set_defaults(func=_cmd_tone)

    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
