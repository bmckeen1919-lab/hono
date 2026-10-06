# Hono translation method — *The Quiet Morning*

How each English sentence becomes a Hono sentence. The **model is the authority**:
use only forms it licenses, and mark — never hide — what the language cannot say.
Modelled on the Kah translation (LR 0039) and the Muna gap log.

## The loop, per sentence

1. **Segment** the English into clauses: find the predicate(s), the arguments, and
   any adjuncts.
2. **Look up** each content word's Hono **root** in `reference/hono-lexicon.md`
   (gloss → root). Function words (pronouns, determiners, numerals, modals,
   subordinators, conjunctions, adpositions) have roots too.
3. **Verify** the root is the sense you mean — Hono roots are arbitrary, so the
   **gloss is the anchor**, not the spelling. Confirm the assembled form is legal
   (inventory `p t k m n s l r w h` / `a e i o u`; syllables `CV, CVC`).
4. **Assemble a clause** with the toolkit's builders:
   - transitive → `build_clause(subject, verb, object)`
   - intransitive → `build_clause(subject, verb)` (single argument takes the
     **alignment pivot**: `NOM` if accusative, `ABS` if ergative)
   - copular → `build_predication(subject, complement)` (subject + copula `be` +
     bare complement)
   - noun phrases → `NounPhrase(head, adjectives=…, possessor=…, appositive=…, pp=…)`
     (modifiers **post-nominal**; Hono is head-initial `SVO`)
   - obliques → pass `(adposition_id, noun)` pairs to the clause builder.
5. **Join clauses** with `build_sentence([clause, …], connectives=None)` —
   juxtaposition (parataxis) or a conjunction.
6. **Set tense & aspect** from the verb's paradigm: the clause builders apply
   *case and agreement* only, so take the verb's inflected form from the model
   (`out/hono.json` `words`) for the tense/aspect you need — e.g. `PST+PROG`
   ("was …-ing"), `PST+PERF` (pluperfect; "had done"), `PST+PERF+PROG` ("had
   been …-ing").
7. **Paraphrase** anything the language cannot express (below).
8. **Quarantine** the irreducible as `[slot]` and log it (below).
9. **Record** the row `index,english,hono`.

## What Hono can say

- **Clauses:** transitive, intransitive, copular predication, obliques; sentences
  by parataxis + conjunctions (`and/but/then/so`) and subordinators
  (`while/when/where/because/until`).
- **Noun phrase:** head + adjective / possessor / apposition / adpositional phrase.
- **Verb:** past / future; progressive and perfect (stacked); 3SG agreement; **no
  valency** — any verb may be used with one argument or two.
- **Function words:** pronouns, articles/determiners (`the`, `a`, `this`, …),
  numerals > three, modals (`can/could/would/should/must/will`), adverbs.

## Paraphrase strategies

- **Passive → active.** *the walls were weathered by salt* → "salt weathered the
  walls."
- **Relatives & reported speech → parataxis.** New clause in sequence: *the man
  who gave me the key* → "the man gave me the key. he …"; direct speech is
  juxtaposition: *Clara said, "I'm ready."* → "clara said. i ready."
- **Non-finite clauses (participles/gerunds) → clauses.** *taking in the breeze*
  → "he took in the breeze", or a `while`/`when` clause.
- **Comparatives & equatives → analytic.** *louder* → "more loud"; *as still as*
  → "same still as"; *best* → use the `best` root / "most good".
- **Compounds → word sequences** (no compounding): *woodsmoke* → "smoke of wood";
  *doorway* → "way of the door"; *sea pink* → "flower of the sea".
- **Existential *there is* → predication/locative.** *there's a spot* → "a spot
  is (here)" / "a spot lies …".
- **Light-verb idioms → verb + adposition.** *take in the breeze* → "breathe";
  *sort through* → "look … through".
- **Articles.** Optional: use `the`/`a`, or drop them — definiteness rides on
  context.
- **Modality & adverbs.** Use the modal and adverb roots directly.

## Slot policy

- **When:** a concept has no root *and* cannot be paraphrased without distorting
  the sense beyond recognition.
- **How:** put `[slot]` in the Hono column, and log the row in
  `reference/hono-slots.md` (`sentence | english | why | proposed fix`).
- **Never fudge silently.** An approximate, unmarked translation is worse than a
  marked slot: a slot is data about what the language lacks.
- **Resolution:** the slot log is the queue for later lexicon growth — add a root,
  or a documented paraphrase, then clear the slot.

## The CSV

- Columns exactly `index,english,hono`; one row per sentence (111 rows).
- Normalize dialogue quotation marks out of the **English** column so the file
  parses cleanly (the Kah precedent); keep the Hono column free of commas or
  quote it.
- English is the fixed source; only the `hono` column is authored.

## Worked examples

**1. *The sun was rising above the ocean.***
Subject `sun` (`ho`) takes `ABS` (intransitive pivot) → `howiw`; verb `rise`
(`wur`) in `PST+PROG` → `wurrutlop`; oblique `above` (`mukmenup`) + `ocean`
(`lulus`), post-object.

> `howiw wurrutlop mukmenup lulus` — sun.ABS rise.PST.PROG above ocean

**2. *The water was calm, without movement, like a large blue mirror.***
Predication: `water` (`re`) + copula `be` (`husew`) in `PST` (`husewrut`) +
complement `calm` (`mekhotup`) → `rewiw husewrut mekhotup`. Then paraphrase the
two adjuncts: *without movement* → "not move"; *like a large blue mirror* →
"same-as a mirror large blue" (modifiers post-nominal, `same` for the equative).

> `rewiw husewrut mekhotup …` — water.ABS be.PST calm …

## Definition of done

111 rows, one translation each; every form legal under Hono's inventory and
phonotactics; a consistent gloss → root mapping; `[slot]` marked; checked by the
validator (see the *Build the Hono CSV validator* ticket).
