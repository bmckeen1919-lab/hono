---
title: Author the translation method and slot policy
label: wayfinder:task
status: closed
assignee: opencode
blocked-by: []

---

## Question

Write Hono's working method into `NOTES.md` / `reference/`: the lookup → verify → paraphrase discipline (Q9a), the documented paraphrase strategies, and the **slot** quarantine policy for untranslatable items. Model it on `learn_kah` LR 0039 and `muna/translation-gaps.md`.

## Resolution

Authored (AFK), modelled on Kah LR 0039 and the Muna gap log.

**`reference/hono-translation-method.md`** — the per-sentence loop (segment →
look up root in the lexicon → verify the gloss → assemble a clause with the
toolkit builders → join with parataxis/conjunctions → set tense/aspect from the
verb's paradigm → paraphrase → quarantine → record); Hono's expressive range;
the documented **paraphrase strategies** (passive→active, relatives/reported
speech→parataxis, non-finites→clauses, analytic comparatives, compounds→word
sequences, existential→locative, light verbs, optional articles); the CSV format;
and two worked examples from the real model (`howiw wurrutlop mukmenup lulus`).

**`reference/hono-slots.md`** — the running `[slot]` quarantine log (empty by
design; the language was grown to cover the story first).

**Note captured.** The toolkit's clause builders apply *case and agreement* only;
tense/aspect are taken from the verb's model forms — the method documents this
explicitly.

`NOTES.md` updated; committed (`docs: author the translation method and slot policy`).