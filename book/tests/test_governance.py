#!/usr/bin/env python3
"""Tests for governance scripts (pilot logging, representation lens)."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
ROOT = BOOK.parent


def test_record_pilot_run_updates_temp_copy() -> None:
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        tbook = Path(tmp) / "book"
        shutil.copytree(
            BOOK, tbook, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "audio_demos")
        )
        # Patch script BOOK path by running from copied tree
        r = subprocess.run(
            [
                sys.executable,
                str(tbook / "scripts" / "record_pilot_run.py"),
                "--date",
                "2026-10-01",
                "--instructor",
                "Test Instructor",
                "--participants",
                "5",
                "--mean-rating",
                "4.5",
                "--issues",
                "none (smoke test)",
            ],
            cwd=tbook,
            capture_output=True,
            text=True,
        )
        assert r.returncode == 0, r.stderr or r.stdout
        pilot = (tbook / "TEACHING_PILOT_RUN1.md").read_text(encoding="utf-8")
        assert "**cohort completed**" in pilot
        assert "Test Instructor" in pilot
        assert "4.5" in pilot


def test_representation_lens_script() -> None:
    r = subprocess.run(
        [sys.executable, str(BOOK / "scripts" / "check_representation_lens.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert r.returncode == 0, r.stderr or r.stdout


def test_pedagogy_verify_script() -> None:
    r = subprocess.run(
        [sys.executable, str(BOOK / "scripts" / "check_pedagogy_verify.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert r.returncode == 0, r.stderr or r.stdout


TESTS = [test_record_pilot_run_updates_temp_copy, test_representation_lens_script, test_pedagogy_verify_script]


def main() -> int:
    failures = []
    for test in TESTS:
        name = test.__name__
        try:
            test()
            print(f"OK  {name}")
        except Exception as exc:
            failures.append(f"FAIL {name}: {exc}")
            print(failures[-1])
    if failures:
        return 1
    print(f"All {len(TESTS)} governance tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
