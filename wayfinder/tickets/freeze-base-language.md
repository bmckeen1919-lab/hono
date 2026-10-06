---
title: Freeze the Hono base language
label: wayfinder:grilling
status: closed
assignee: opencode
blocked-by: []

---

## Question

Finalize the Hono base spec and freeze it. Confirm the name `hono` (sampled root `hono` = "sea"), seed `1`, pinned inventory `p t k m n s l r w h` / `a e i o u`, syllables `[CV, CVC]`. Decide whether the sampled morphology (inflection classes) and syntax (word order / alignment) are acceptable or need re-seeding, then run `accept` and store `spec/hono.yaml` + `out/hono.json` in this workspace. The frozen model becomes the authority for every later ticket.

## Resolution

Resolved with the learner (2026-10-05): **accept the sampled morphology** (Q1a), **accept `SVO + ergative`** (Q2a), **freeze via `accept` with the full default lexicon** (Q3a).

Artifacts:
- `spec/hono.yaml` — frozen, fully-explicit spec (name `Hono`, seed 1; pinned inventory `p t k m n s l r w h` / `a e i o u`, syllables `CV, CVC`; **175 pinned lexemes; 14 affixes**; sampled morphology + syntax now pinned).
- `out/hono.json` — the model (175 lexemes, **1010 word forms**, schema 0.1, lint `valid`).

Verified: regenerating from `spec/hono.yaml` reproduces **identical word forms and affixes**. The frozen model is now the authority for every later ticket. Unblocks `design-lexicon` and `csv-validator`.