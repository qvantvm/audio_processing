# Review Notes

Open issues, review findings, and planned improvements.

## Pass 10 — Chapters 13–17 Review (2026-07-03)

### Completed

- Pandoc `@sec:` IDs on chapters 13–17 (and 18–22 for forward references)
- Cross-references in chapters 13–17 (loudness, SRC, features, pitch, musical reps)
- Bidirectional links: Ch 15 ↔ Ch 17 (Mel, chroma, MFCC); Ch 16 → Ch 06, Ch 15
- GLOSSARY: chroma, crest factor, MFCC, spectral centroid, spectral flux
- Promoted chapters **13–17** to **reviewed**

### Correctness / Clarity

- [ ] Review chapters 18–22 (synthesis, modeling, neural, testing, toolkit)
- [ ] Replace plain "Chapter N" in chapters 18–22
- [ ] Pandoc `make html` CI

### Reviewed chapters (cumulative)

00–17 (18 chapters)

---

## Pass 9 — Chapters 07–12 Review (2026-07-03)

- Cross-refs spectral/filter block; chapters 07–12 reviewed

## Pass 8 — Editorial & Bibliography (2026-07-02)

- Chapters 00–06 reviewed; bibliography; CI workflow

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
