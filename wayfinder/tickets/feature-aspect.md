---
title: Build aspect (progressive, perfect, pluperfect)
label: wayfinder:task
status: closed
assignee: opencode
blocked-by: []

---

## Question

Extend the `conlang` tool with an **aspect** tier alongside the existing past/future: **progressive** (*was rising*), **perfect**, and **pluperfect** (*had left*, *had been planning*). Reach **29** — essential because the narrative is told in past-tense progressives and anteriority. Today only `past`/`future` affixes are generated (`morphology/generate.py`); there is no aspect and no second tense. Implement in `C:\Users\bmcke\conlang`; then regenerate Hono's spec/model.

## Resolution

Implemented in `C:\Users\bmcke\conlang`, agent-driven (2026-10-05).

**Design.** Verbs gain two stacked aspect categories — **progressive** (`PROG`) and **perfect** (`PERF`) — beside past/future; pluperfect composes as `past + perfect` and "had been …-ing" as `past + perfect + progressive`, reusing category stacking. Aspect affixes are class-specific **suffixes** and reach the copula too (shared verb morphology). No schema field, no lexeme change.

**Files.** `morphology/generate.py` (`CATEGORY_DEFS` gains `prg`/`prf`; `DEFAULT_CATEGORY_ORDER["verb"]` gains `progressive`, `perfect`); `CONTEXT.md` (Aspect row); ADR decision 17.

**Tests.** `tests/test_aspect.py` (4 new); `tests/golden.json` refreshed. `ruff`/`mypy` clean; **147 passed**.

**Hono — wrinkle.** Hono's spec *pins its affixes*, so a plain regenerate kept the old morphology. Its affixes were **re-derived** (spec regenerated with the affix list unpinned, the lexicon still pinned) and re-frozen: **18 affixes** (PROG `lop`; PERF `mu`/`koh`), **1409 word forms**, 199 lexemes, lint `valid`. E.g. `wowlerukrut` (say.PST) → `wowlerukrutmu` (had said) → `wowlerukrutlopmu` (had been saying). *A future session adding a morphology category must re-derive Hono's affixes the same way.*