---
title: Build the Hono CSV validator
label: wayfinder:task
status: closed
assignee: opencode
blocked-by: [freeze-base-language]

---

## Question

Write a small validator for `the_quiet_morning_hono.csv`: exactly 111 rows, one translation per sentence, **every form legal under Hono's inventory and phonotactics**, `[slots]` marked, and a consistent gloss → root mapping. Blocked until the base language is frozen (it needs the inventory and phonotactics).

## Resolution

Built (AFK).

**`tools/validate_hono.py`** — loads `out/hono.json` and checks `the_quiet_morning_hono.csv`: header `index,english,hono`, exactly 111 rows, the index sequence, non-empty English, and every Hono token **phonotactically legal** via the toolkit's `is_legal_word`. `[slot]` cells are accepted (counted); **empty** cells report as *untranslated*, not errors, so the file validates incrementally. Run with the toolkit interpreter:
`C:\Users\bmcke\conlang\.venv\Scripts\python.exe tools\validate_hono.py`.
Verified: `translated 0/111 · slots 0 · errors 0`, and a spot check confirmed legal forms pass while `zzq`/`xyz` fail.

**`the_quiet_morning_hono.csv`** — the 111-row skeleton (header + normalized English, empty Hono column), ready to translate into.

Committed (`feat: Hono CSV validator + translation skeleton`).

**Note.** Gloss → root consistency is a *reading* check (the lexicon is arbitrary, so the gloss is the authority); it is documented in the method, not automated.