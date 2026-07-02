# Review Notes

Open issues, review findings, and planned improvements.

## Pass 8 — Editorial & Bibliography (2026-07-02)

### Completed

- Added bibliography: Harris windows, YIN, SMS, DDSP, WaveNet, ITU BS.1770, EBU R128
- Resolved TODO citations in chapters 7, 13, 16, 17, 20
- Pandoc section IDs on chapters 00–07; cross-refs in Ch 01, 06
- Promoted chapters **00–06** to **reviewed** in `BOOK_PLAN.md`
- Added `.github/workflows/book-examples.yml` (smoke tests)

### Correctness / Clarity

- [ ] Review chapters 07–12 (spectral + filter block) → promote to reviewed
- [ ] Extend `@sec:` IDs to chapters 08–22
- [ ] Full notation audit for chapters 10–12 (poles, group delay symbols)

### Examples / CI

- [x] `tests/run_examples.py` smoke harness
- [x] GitHub Actions workflow for examples
- [ ] Pandoc `make html` CI (needs pandoc on runner)

### Bibliography

- [x] Harris, YIN, SMS, DDSP, WaveNet, BS.1770, EBU R128 added
- [ ] Verify all in-text cite keys on second full read

---

## Pass 7 — Complete Manuscript Draft (2026-07-02)

- Drafted chapters 07–22; nine examples; all chapters initially **draft**

## Status Promotion Criteria

Promote **draft** → **reviewed** when:

1. Second-pass edit complete
2. All cited keys resolve in `bibliography.bib`
3. Referenced examples run
4. Exercises spot-checked

**Reviewed (Pass 8):** 00, 01, 02, 03, 04, 05, 06

## Future Review Checklist (per section)

1. Definitions precede use
2. Math symbols in `NOTATION.md`
3. New terms in `GLOSSARY.md`
4. Audio intuition + math balanced
5. Pitfalls name real mistakes
6. Code runs (NumPy/SciPy/Matplotlib)
