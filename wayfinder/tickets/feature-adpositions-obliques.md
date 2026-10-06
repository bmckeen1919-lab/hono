---
title: Build adpositions, obliques, and place/direction
label: wayfinder:task
status: closed
assignee: opencode
blocked-by: []

---

## Question

Extend the `conlang` tool with an **adposition/oblique** class and **place/direction** phrases, represented in the model. This is the **largest gap** (reach 95): no adposition POS or PP rule exists, and place/direction saturates the text (*above*, *in*, *into*, *from…to*, *toward*, *against*). Implement in `C:\Users\bmcke\conlang`; decide pre- vs post-position from Hono's head-final/modifier facts; then regenerate Hono's spec/model.

## Resolution

Implemented in `C:\Users\bmcke\conlang`, agent-driven (2026-10-05).

**Design.** Adpositions are a generated closed class (`pos="adp"`, invariable), one per place/direction sense; position is **derived from word order** (VO → preposition, OV → postposition), so no new sampled field. Clauses take optional `(adposition_id, noun_id)` obliques, realised as adposition + bare noun and placed by `linearize` (after the object for SVO/VSO, before the final verb for SOV). No schema change; `SCHEMA_VERSION` stays `0.1`.

**Files.** `lexicon/generate.py` (`ADPOSITION_GLOSSES`, `generate_adpositions`); `pipeline.py` (generate adpositions; exclude them from the concept list so `accept` round-trips); `syntax/__init__.py` (`is_prepositional`; obliques in `linearize`/`build_clause`); `render/markdown.py` (sketch line); `CONTEXT.md`; ADR decision 12.

**Bonus fix.** The new RNG exposed a latent generator bug: two adjacent emitted symbols could **fuse** (`…e`+`h…` → `eh`) and shift the `C`/`V` skeleton. `generate_root` now re-rolls any form that does not re-tokenise to its intended symbols.

**Tests.** `tests/test_adpositions.py` (8 new); updated `test_invariants.py` and `test_lint_invariants.py` for the always-present class; refreshed `tests/golden.json`. `ruff`/`mypy` clean; **119 passed**.

**Hono.** Regenerated and re-frozen — `spec/hono.yaml` + `out/hono.json`: **195 lexemes** (175 content + 20 adpositions), **1030 word forms**, lint `valid`; the render lists Hono's prepositions.