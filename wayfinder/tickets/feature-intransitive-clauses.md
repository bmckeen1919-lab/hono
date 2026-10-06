---
title: Build intransitive (one-argument) clauses
label: wayfinder:task
status: closed
assignee: opencode
blocked-by: []

---

## Question

Extend the `conlang` tool so a generated language can predicate a **single** participant — one-argument clauses — and have the model represent them. Today `build_clause` requires subject *and* object (`syntax/__init__.py`), so reach-51 sentences like *the sun was rising*, *Iain stood*, *the path wound* are unbuildable. Implement in `C:\Users\bmcke\conlang`; keep the model the source of truth; update lint/render/CONTEXT as needed; then regenerate Hono's spec/model.

## Resolution

Implemented in `C:\Users\bmcke\conlang`, agent-driven (2026-10-05).

**Design.** `build_clause` now takes an optional `object_`; when it is `None` the clause is intransitive. The single argument takes `intransitive_case(alignment)` — `NOM` under accusative, `ABS` under ergative — the S = O pivot; the verb still agrees 3SG. Intransitive clauses take obliques like transitive ones. Verbs carry **no valency**; a verb lexeme may be used with one argument or two. `linearize` accepts an objectless clause. No schema change.

**Files.** `syntax/__init__.py` (`intransitive_case`; objectless `linearize`/`build_clause`); `render/markdown.py` (intransitive example); `CONTEXT.md` (Clause row); ADR decision 14.

**Tests.** `tests/test_intransitive_clauses.py` (6 new); `ruff`/`mypy` clean; **131 passed**. The model is unchanged (clauses build on demand), so no golden refresh and no Hono re-freeze — regenerating Hono reproduces the identical language.