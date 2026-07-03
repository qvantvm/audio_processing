# Review Notes

Open issues, review findings, and planned improvements.

## Pass 9 — Chapters 07–12 Review (2026-07-03)

### Completed

- Pandoc `@sec:` IDs on chapters 08–12
- Cross-references updated in chapters 07–12 (replaced plain "Chapter N" with `@sec:` links)
- Ch 08 links back to @sec:ch-06-dft-fft and @sec:ch-07-windowing
- NOTATION: group delay $\tau_g$, coherent gain CG, delay $D$; restored $w[n]$, $m$, $z^{-1}$
- GLOSSARY: COLA, comb filter, group delay
- Promoted chapters **07–12** to **reviewed**

### Correctness / Clarity

- [ ] Review chapters 13–17 (production + analysis block)
- [ ] Extend `@sec:` IDs to chapters 13–22
- [ ] Add forward refs from Ch 13 to Ch 21 (true-peak) with @sec when IDs exist

### Examples / CI

- [x] Example smoke tests pass
- [x] GitHub Actions workflow
- [ ] Pandoc `make html` CI

### Reviewed chapters (cumulative)

00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12

---

## Pass 8 — Editorial & Bibliography (2026-07-02)

- Bibliography entries; TODO citations resolved in Ch 7, 13, 16, 17, 20
- Chapters 00–06 promoted to reviewed; CI workflow added

## Pass 7 — Complete Manuscript Draft (2026-07-02)

- Drafted chapters 07–22

## Status Promotion Criteria

Promote **draft** → **reviewed** when:

1. Second-pass edit complete
2. All cited keys resolve in `bibliography.bib`
3. Referenced examples run
4. Exercises spot-checked

## Future Review Checklist (per section)

1. Definitions precede use
2. Math symbols in `NOTATION.md`
3. New terms in `GLOSSARY.md`
4. Audio intuition + math balanced
5. Pitfalls name real mistakes
6. Code runs (NumPy/SciPy/Matplotlib)
