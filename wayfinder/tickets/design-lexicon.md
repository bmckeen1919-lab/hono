---
title: Design the Hono lexicon
label: wayfinder:grilling
status: closed
assignee: opencode
blocked-by: [concept-inventory, freeze-base-language]

---

## Question

Decide how Hono covers the concept inventory with the tool's model: which concepts become **pinned roots**, which are **derived** or **compounded**, and how missing senses are paraphrased. Produce the pinned lexicon plan and the readable lexicon render. Blocked on the concept inventory and the frozen base.

## Resolution

Resolved with the learner (2026-10-05): **Q1a** append to Hono's explicit lexicon; **Q2a** paraphrase compounds (coin only simplex concepts); **Q3a** add function words as invariable entries; **Q4a** build now.

**Built.** Parsed the growth list from `research/concept-inventory.md` (sections 2a–2f) → ~282 content concepts, plus 55 function words (pronouns, determiners, numerals > three, subordinators, modals, adverbs, degree) = **337 new lexemes**. Each got a collision-free root generated from the seed's per-item label (`lex:<gloss>`) and was pinned into the spec's `lexicon`. Compounds (*mirror-like, woodsmoke, doorway, …*) are **paraphrased**, not coined.

**Result.** Hono grows **199 → 536 lexemes** (268 noun, 109 adj, 76 verb, 20 adp, 21 adv, 10 num, 8 det, 7 pron, 6 mod, 5 sub, 4 conj, 1 cop, 1 part) and **3577 word forms**, lint `valid`. `spec/hono.yaml` + `out/hono.json` re-frozen; `reference/hono-lexicon.md` (gloss/pos/root) and a refreshed `reference/hono-grammar.md` rendered; committed (`feat: build the Hono lexicon`).

**Note.** The story's *gull* resolved to *seagull* (the research row's first alternative); a distinct `gull` gloss can be added later if wanted.