---
title: Build copula, predicate-adjective, and existential
label: wayfinder:task
status: closed
assignee: opencode
blocked-by: []

---

## Question

Extend the `conlang` tool with a **copula / predicate-nominal / predicate-adjective** and an **existential** construction, represented in the model. Today there is no `be` and no adjective-predicate rule, so reach-41 sentences like *the water was calm*, *I'm Clara*, *the tide is perfect*, *there's a spot* cannot be predicated. Implement in `C:\Users\bmcke\conlang`; then regenerate Hono's spec/model.

## Resolution

Implemented in `C:\Users\bmcke\conlang`, agent-driven (2026-10-05).

**Design.** Every language now generates one **copula** (`be`, pos `cop`) that draws verb morphology by sharing the verb classes, so predicate adjectives and nominals take tense and agreement: subject + copula + bare complement. New `build_predication(...)` linearises it (subject in `intransitive_case`, complement bare, copula agrees). Existential *there is* is **paraphrased** as this shape plus a locative oblique (Q3a) — no dedicated construction. No schema field.

**Files.** `lexicon/generate.py` (`generate_copula`, `COPULA_GLOSS`); `morphology/generate.py` (verb affixes now reach `cop`; the copula shares verb classes); `pipeline.py` (generate the copula; exclude it from the concept list); `syntax/__init__.py` (`build_predication`, `_copula`, `_obliques`); `render/markdown.py` (copula line + predicate example); `CONTEXT.md`; ADR decision 15.

**Tests.** `tests/test_predication.py` (6 new); two fixtures updated; `tests/golden.json` refreshed. `ruff`/`mypy` clean; **137 passed**.

**Hono.** Re-frozen — `spec/hono.yaml` + `out/hono.json`: **196 lexemes** (175 content + 20 adpositions + copula), **1031 word forms**, lint `valid`. Copula `husew`; example `rewiw husew nomirte` — "water.ABS be.3SG big".