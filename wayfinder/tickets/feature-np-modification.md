---
title: Build NP modification (adjective, possessive, apposition)
label: wayfinder:task
status: closed
assignee: opencode
blocked-by: []

---

## Question

Extend the `conlang` tool so a noun phrase can be more than one word: **adjective, possessive, apposition** (and, if cheap, PP-in-NP). Reach **81** — *a large blue mirror*, *his elderly neighbor*, *whitewashed walls*, *the launch line*. Today `build_clause` takes bare lexemes. Implement in `C:\Users\bmcke\conlang`, fixing modifier order against Hono's head direction; then regenerate Hono's spec/model.

## Resolution

Implemented in `C:\Users\bmcke\conlang`, agent-driven (2026-10-05).

**Design.** A noun phrase is a value (`NounPhrase`), not a stored artifact; `build_clause` and oblique nouns accept `str | NounPhrase`. Modifiers — adjectives, possessor, apposition, and a PP — sit on the head's side by **head direction** (VO ⇒ after the head; OV ⇒ before), the same parameter that orders adpositions. A possessive is **bare juxtaposition** (no marker). The subject/object head takes its core case; modifiers take none. No schema change.

**Files.** `syntax/__init__.py` (`is_head_initial`; `NounPhrase`; `build_noun_phrase`; `linearize`/`build_clause` accept phrases); `render/markdown.py` (modifier-order line + NP example); `CONTEXT.md`; ADR decision 13.

**Tests.** `tests/test_noun_phrases.py` (6 new); `ruff`/`mypy` clean; **125 passed**. The model is *unchanged* — NP building is on-demand — so there is no golden refresh and **no Hono re-freeze**: regenerating Hono reproduces the identical language (word forms, affixes, and lexemes verified).