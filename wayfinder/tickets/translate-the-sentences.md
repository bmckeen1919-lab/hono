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
- **Batch 2 (rows 11–20)** — done. Lexicon grew by *burst, expanse, own, feel,
  click, lace, startle, disturb, gull* (and `down`/`age`, tried as `adp`, were
  rejected by the reserved adposition class and paraphrased). Validator:
  **20/111 translated · 2 slots · 0 errors**.
- **Batch 3 (rows 21–30)** — done. Lexicon grew by *all, claim, everyone, help,
  keep, offer, place, predict, set, sort, town, use, weekend*. Validator:
  **30/111 translated · 2 slots · 0 errors**.
- **Batch 4 (rows 31–40)** — done. Lexicon grew by *center, city, change, live,
  moment, recognize, require, scrawl, single, slanted, solve, try, some, just*.
  Validator: **40/111 translated · 2 slots · 0 errors**.
- **Batch 5 (rows 41–50)** — done. Lexicon grew by *dance, fit, follow, groan,
  kitchen, mechanism, object, pile, retreat, room, rush, sink, stack, sunlight,
  swing, tightness*. Validator: **50/111 translated · 2 slots · 0 errors**.
- **Batch 6 (rows 51–60)** — done. Lexicon grew by *argue, collect, focus,
  ground, intricate, last, learn, line, map, murmur, nearby, need, pick, roll,
  start, touch, transform, way, wood*. Validator: **60/111 translated · 2 slots ·
  0 errors**.
- **Batch 7 (rows 61–70)** — done. Lexicon grew by *arrive, chase, coat,
  gleam, musty, piece, punctuate, replace, rest, tap*. Validator: **70/111
  translated · 2 slots · 0 errors**.
- **Batch 8 (rows 71–80)** — done. Lexicon grew by *break, callous, labor,
  launch, only, realize, reflect, right*. Validator: **80/111 translated · 2
  slots · 0 errors**.
- **Batch 9 (rows 81–90)** — done. Lexicon grew by *aim, constant, creak,
  destination, east, gap, get, landmark, navigate, pass, plague, point, school,
  tiny*. Validator: **90/111 translated · 2 slots · 0 errors**.
- Next: batch 10 (rows 91–100).
