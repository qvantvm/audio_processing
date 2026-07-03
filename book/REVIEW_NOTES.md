# Review Notes

Open issues, review findings, and planned improvements.

## Pass 14 — Honest Status, audio_toolkit, Correctness Tests (2026-07-03)

### Response to external critique

The manuscript previously overclaimed `reviewed` / `polished` status. This pass:

1. **Status model** — `stub` → `draft` → `technically reviewed` → `pedagogically reviewed` → `polished`
2. **Demotions** — ch 18, 20 → `draft`; removed false `polished` from 00–03; no chapter is `polished`
3. **`audio_toolkit/`** — importable package (`io`, `osc`, `spectral`, `filters`, `effects`, `meter`)
4. **Correctness tests** — `tests/test_correctness.py` (FFT, Parseval, STFT, FIR, phase, dBFS, Karplus)
5. **`solutions/`** — `ch01_verify.py` … `ch03_verify.py` with tested numeric answers
6. **Chapter depth** — ch 01 representation matrix; ch 02 code completeness; ch 19 Karplus–Strong demo; ch 22 documents real package
7. **Governance** — README + BOOK_PLAN rules for status promotion
8. **CI** — correctness tests + solution verifications added

### Markdown formatting

Raw files in this repo use normal newlines (verified locally). `.editorconfig` added for consistent editing. If a viewer shows single-line files, re-normalize with a line-based editor before editing.

### Remaining gaps

- [ ] ch 18, 20 still `draft` — need runnable examples and representation lens
- [ ] Audio WAV demos (not only PNG plots)
- [ ] More block diagrams in `figures/`
- [ ] Exercise solutions for ch 04+
- [ ] PDF CI (LaTeX)
- [ ] External / second-model review pass per chapter

### Chapter status summary

| Status | Chapters |
|--------|----------|
| pedagogically reviewed | 01–06 |
| technically reviewed | 00, 07–17, 19, 21–22 |
| draft | 18, 20, appendix A |

---

## Pass 13 — Exercise Solutions Appendix; Foundation Polish (2026-07-03)

(Superseded status claims — see Pass 14 demotions.)

---

## Pass 12 — Cross-Reference Fix; Foundation Chapter Links (2026-07-03)

### Completed

- Converted **83** `@sec:ch-...` references to Pandoc Markdown links
- HTML build: no citeproc `sec:ch-...` citation warnings
- Foundation block (ch 00–06): plain "Chapter N" refs → internal links

---

## Status Promotion Criteria

**technically reviewed** requires: examples run, notation consistent, citations resolve, second review logged.

**pedagogically reviewed** requires: exercises checked, pitfalls grounded, teaching clarity pass.

**polished** requires: external review, teaching pilot, or dedicated publication proofread.

## Future Review Checklist (per section)

1. Definitions precede use
2. Math symbols in `NOTATION.md`
3. New terms in `GLOSSARY.md`
4. Representation lens: what / preserves / discards / maps / mistakes / artifacts
5. Pitfalls name real mistakes
6. Code runs and correctness tests cover claims
