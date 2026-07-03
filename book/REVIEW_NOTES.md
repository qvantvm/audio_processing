# Review Notes

Open issues, review findings, and planned improvements.

## Pass 13 — Exercise Solutions Appendix; Foundation Polish (2026-07-03)

### Completed

- New appendix: `23-appendix-exercise-solutions.md` with worked solutions for **ch 01–03** (15 exercises)
- Cross-links from exercise sections and preface to appendix
- Promoted chapters **00–03** to **`polished`**
- HTML build verified with appendix included

### Correctness / Clarity

- [ ] Proofread HTML output; math warnings mostly cosmetic without LaTeX engine
- [ ] Optional: expand ch 18–20 with more runnable synthesis examples

### Examples / CI

- [x] Example smoke tests
- [x] Pandoc HTML build in CI
- [ ] PDF build (needs LaTeX)

### Reviewed chapters

**Polished:** 00–03 | **Reviewed:** 04–22, appendix A

---

## Pass 12 — Cross-Reference Fix; Foundation Chapter Links (2026-07-03)

### Completed

- Converted **83** `@sec:ch-...` references to Pandoc Markdown links `[title](#ch-id)` across chapters 01–22
- HTML build: **no citeproc `sec:ch-...` citation warnings**
- Foundation block (ch 00–06): plain "Chapter N" refs → internal links
- Preface status line updated (all chapters `reviewed`)
- Trimmed redundant duplicate titles on "Next chapter" lines

### Correctness / Clarity

- [x] Fix `@sec:` cross-refs (citeproc conflict resolved)
- [x] Cross-ref sweep in chapters 00–06
- [ ] Proofread HTML output; math warnings mostly cosmetic without LaTeX engine
- [ ] Optional: expand ch 18–20 with more runnable synthesis examples

### Examples / CI

- [x] Example smoke tests
- [x] Pandoc HTML build in CI
- [ ] PDF build (needs LaTeX)

### Reviewed chapters

**All:** 00–22

---

## Pass 11 — Chapters 18–22 Review; Manuscript Complete (2026-07-03)

### Completed

- Cross-references in chapters 18–22 (synthesis → toolkit capstone)
- Promoted chapters **18–22** to **reviewed**
- **All 23 chapters (00–22) now at `reviewed` status**
- CI: Pandoc HTML build job added (`make html`)

### Correctness / Clarity

- [x] Fix `@sec:` cross-refs: citeproc treats them as citations— convert to `[text](#ch-id)` links (Pass 12)
- [ ] Proofread HTML output; math warnings mostly cosmetic without LaTeX engine
- [ ] Optional: expand ch 18–20 with more runnable synthesis examples

### Examples / CI

- [x] Example smoke tests
- [x] Pandoc HTML build in CI
- [ ] PDF build (needs LaTeX)

### Reviewed chapters

**All:** 00–22

---

## Pass 10 — Chapters 13–17 Review (2026-07-03)

## Pass 9 — Chapters 07–12 Review (2026-07-03)

## Pass 8 — Chapters 00–06 Review (2026-07-02)

## Status Promotion Criteria

**reviewed** → **polished:** external review, teaching pilot, or dedicated proofread pass.

## Future Review Checklist (per section)

1. Definitions precede use
2. Math symbols in `NOTATION.md`
3. New terms in `GLOSSARY.md`
4. Audio intuition + math balanced
5. Pitfalls name real mistakes
6. Code runs (NumPy/SciPy/Matplotlib)
