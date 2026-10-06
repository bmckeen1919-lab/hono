---
title: Translate the 111 sentences
label: wayfinder:task
status: in-progress
assignee: opencode
blocked-by: []
---

## Question

Fill the 111 rows of `the_quiet_morning_hono.csv` by translating each English
sentence with `reference/hono-translation-method.md` — the lookup → verify →
paraphrase loop, tense/aspect from the verb's paradigm, `[slot]` quarantine logged
in `reference/hono-slots.md`. Work in batches; run
`C:\Users\bmcke\conlang\.venv\Scripts\python.exe tools\validate_hono.py` after each
batch until it reports **111 translated (plus any slots) with no errors**.

This is the map's execution hand-off: the decisions are settled, so this ticket
*does* rather than decides. A batch is a contiguous run of sentences (e.g. 1–10),
resolved when those rows are filled and the validator is clean.

## Progress

- **Batch 1 (rows 1–10)** — done. Two lexicon words added en route (*iain*,
  *clara*, *neighbor*, *smell*, *light*, *return*, *move*, *sing*, *leave*,
  *blend*, *whistle*, *again*). Validator: **10/111 translated · 2 slots · 0
  errors**. Slots: *cicada*, *stonechat* (logged in `reference/hono-slots.md`).
- Next: batch 2 (rows 11–20).
