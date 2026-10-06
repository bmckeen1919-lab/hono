# Mission: translate *The Quiet Morning* into Hono

## The reason

**Hono** is a constructed language produced by the `conlang` toolkit: a seeded
base (inventory and syllable shapes) that is generated and then deliberately
extended. This project translates a fixed 111-sentence English story, *The Quiet
Morning*, into Hono — a stress test of what the language can and cannot say.

## Why this matters

- **A complete parallel text** (`the_quiet_morning_hono.csv`) exercises Hono's
  phonology, morphology, and syntax sentence by sentence.
- The **same story** is already translated into sibling languages (Kah, Muna,
  Volapük), so Hono joins a comparable set — the point of using one story.
- The **tool is the source of truth**: the translation may use only forms the
  model licenses, and anything the language cannot yet say is documented, not
  hidden.

## Success measures

- All **111 sentences** translated, one per row, in `the_quiet_morning_hono.csv`
  (`index,english,hono`).
- Every form is **legal** under Hono's inventory and phonotactics; untranslatable
  items are quarantined as `[slot]`.
- The **gaps** the tool cannot yet express are logged rather than worked around
  silently.

## Sources of truth

- The generated model — `out/hono.json`; the frozen spec — `spec/hono.yaml`.
- The toolkit — `C:\Users\bmcke\conlang` (distribution `conlanggen`).
- The wayfinding map — `wayfinder/map.md`.
