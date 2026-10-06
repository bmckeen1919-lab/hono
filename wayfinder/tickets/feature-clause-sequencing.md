---
title: Build clause sequencing (parataxis / coordination)
label: wayfinder:task
status: closed
assignee: opencode
blocked-by: []

---

## Question

Extend the `conlang` tool so a sentence can hold **more than one clause** via **parataxis / coordination** (juxtaposition and `and`/`but`), represented in the model. Reach **31** directly, and it is the enabler for the "misdiagnosed" rows: **relative clauses, reported speech, and clause coordination become parataxis** rather than new machinery (Q3a). Today `and` is a bare lexeme with no combinator. Implement in `C:\Users\bmcke\conlang`; then regenerate Hono's spec/model.

## Resolution

Implemented in `C:\Users\bmcke\conlang`, agent-driven (2026-10-05).

**Design.** Clauses are sequenced on demand by **parataxis** (juxtaposition) or a connective. Connectives are a generated closed class (`and`, `but`, `then`, `so`; pos `conj`); `and` moved out of the concept list into it. New `build_sentence(language, clauses, connectives=None)` joins built clauses, taking a `conj` id per gap (`None`/absent ⇒ juxtaposition) — the parataxis that will carry relatives and reported speech. VP coordination is out of scope (repeat the subject). No persisted `Sentence` model, no schema change.

**Files.** `sampling/concepts.py` (drop the `and` concept); `lexicon/generate.py` (`CONJUNCTION_GLOSSES`, `generate_conjunctions`); `pipeline.py` (generate conjunctions; exclude them from concepts, including older frozen specs, by gloss); `syntax/__init__.py` (`build_sentence`); `render/markdown.py` (conjunctions line + two-clause example); `CONTEXT.md`; ADR decision 16.

**Tests.** `tests/test_clause_sequencing.py` (6 new); two fixtures updated; `tests/golden.json` refreshed. `ruff`/`mypy` clean; **143 passed**.

**Hono.** Re-frozen — `spec/hono.yaml` + `out/hono.json`: **199 lexemes** (174 content + 20 adpositions + copula + 4 conjunctions), **1034 word forms**, lint `valid`. Conjunctions: `and masalek`, `but kilpow`, `then mupe`, `so salener`.