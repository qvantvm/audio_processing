#!/usr/bin/env python3
"""Run all verified exercise solution checks."""

import subprocess
import sys
from pathlib import Path

SOLUTIONS = [
    "ch01_verify.py",
    "ch02_verify.py",
    "ch03_verify.py",
    "ch04_verify.py",
    "ch05_verify.py",
    "ch06_verify.py",
    "ch07_verify.py",
    "ch08_verify.py",
    "ch09_verify.py",
    "ch10_verify.py",
    "ch11_verify.py",
    "ch12_verify.py",
    "ch13_verify.py",
    "ch14_verify.py",
    "ch15_verify.py",
    "ch16_verify.py",
    "ch17_verify.py",
    "ch18_verify.py",
    "ch19_verify.py",
    "ch20_verify.py",
    "ch21_verify.py",
    "ch22_verify.py",
]
book = Path(__file__).resolve().parent.parent
failures = []
for name in SOLUTIONS:
    path = book / "solutions" / name
    r = subprocess.run([sys.executable, str(path)], cwd=book, capture_output=True, text=True)
    if r.returncode != 0:
        failures.append(f"{name}: {r.stderr or r.stdout}")
    else:
        print(r.stdout.strip())

if failures:
    print("FAILURES:", *failures, sep="\n")
    sys.exit(1)
print("All solution verifications OK")
