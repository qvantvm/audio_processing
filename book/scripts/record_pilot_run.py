#!/usr/bin/env python3
"""Record external teaching pilot Run 1 results after a real cohort completes.

This script updates log tables in ``TEACHING_PILOT.md``, ``TEACHING_PILOT_RUN1.md``, and
``EXTERNAL_REVIEW.md``. It does **not** substitute for running a cohort — pass real values only.

Example::

    python book/scripts/record_pilot_run.py \\
        --date 2026-09-15 \\
        --instructor "Jane Doe" \\
        --institution "Example University" \\
        --participants 8 \\
        --completion-rate "7/8" \\
        --mean-rating 4.2 \\
        --issues "Session 5 STFT hop confused two participants"
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]


def _replace_table_field(text: str, field: str, value: str) -> str:
    pattern = rf"(\| {re.escape(field)} \|)[^\n]*"
    replacement = rf"\1 {value} |"
    new_text, n = re.subn(pattern, replacement, text, count=1)
    if n != 1:
        raise ValueError(f"Could not update field '{field}' in markdown table")
    return new_text


def _update_fields(path: Path, fields: dict[str, str]) -> None:
    text = path.read_text(encoding="utf-8")
    for field, value in fields.items():
        text = _replace_table_field(text, field, value)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Record teaching pilot Run 1 cohort results")
    parser.add_argument("--date", required=True, help="Cohort date or date range")
    parser.add_argument("--instructor", required=True)
    parser.add_argument("--institution", default="")
    parser.add_argument("--participants", type=int, required=True)
    parser.add_argument("--completion-rate", default="", help='e.g. "7/8"')
    parser.add_argument("--mean-rating", type=float, required=True, help="Mean 1–5 across Q1–Q6")
    parser.add_argument("--issues", default="none reported")
    parser.add_argument("--sign-off", default="pending", choices=["pending", "approved"])
    args = parser.parse_args()

    if args.participants < 1:
        raise SystemExit("participants must be >= 1 for an external cohort log")

    completion = args.completion_rate or str(args.participants)
    sign_off = f"**{args.sign_off}**"
    cohort_summary = (
        f"{args.date} — n={args.participants}, completion {completion}, "
        f"mean rating {args.mean_rating:.1f}/5"
    )

    _update_fields(
        BOOK / "TEACHING_PILOT_RUN1.md",
        {
            "Status": "**cohort completed**",
            "Date(s)": args.date,
            "Instructor": args.instructor,
            "Institution": args.institution or "—",
            "Participants (n)": str(args.participants),
            "Completion rate": completion,
            "Mean rating Q1–Q6 (1–5)": f"{args.mean_rating:.1f}",
            "Blocking issues": args.issues,
            "Sign-off": sign_off,
        },
    )

    _update_fields(
        BOOK / "TEACHING_PILOT.md",
        {
            "Status": f"**cohort completed** — {cohort_summary}",
            "Sign-off": sign_off,
        },
    )

    _update_fields(
        BOOK / "EXTERNAL_REVIEW.md",
        {
            "Run 1 (external)": cohort_summary,
            "Sign-off": f"{sign_off} external cohort",
        },
    )

    print("Recorded Run 1 cohort results.")
    print("Review TEACHING_PILOT.md, TEACHING_PILOT_RUN1.md, EXTERNAL_REVIEW.md before committing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
