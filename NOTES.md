# Notes

## Status

**Destination reached.** All **111 sentences** of *The Quiet Morning* are
translated in `the_quiet_morning_hono.csv`; the validator reports
`111/111 translated · 0 slots · 0 errors`. Hono grew to **680 lexemes**
(5175 word forms), lint `valid`. Both slots are resolved (see
`reference/hono-slots.md`). The map (`wayfinder/map.md`) is complete.

## Hipke (a second language, same story)

**The same 111 sentences are translated into Hipke**, a language with a
deliberately *different* grammar: **SOV, accusative** (`NOM`/`ACC`),
postpositions, modifiers before the head — versus Hono's SVO/ergative. Hipke's
inventory is **IPA** (`phonology.ipa: true`), so the tool derives a romanised
orthography alongside the phonemic forms.

- **Translation**: `the_quiet_morning_hipke.csv`
  (`index,english,hipke,romanization`) — `111/111 translated · 0 slots · 0 errors`.
- **Authored gloss script**: `the_quiet_morning_hipke.tsv` — the hand translation
  written in Hipke order/case, so the composed text is reproducible.
- **Model / spec**: `out/hipke.json` · `spec/hipke.yaml` (**579 lexemes**).
- **Vocabulary**: grown to cover the story with `add_words.py`
  (`template/words_all.json`, then `template/hipke_missing.json`).

Because Hipke's grammar differs from Hono's, this was **not** a straight port of
the Hono gloss: the Hono translation was the *meaning* guide, and each sentence
was rebuilt in Hipke order/case and composed through the model (method Q4a).

## Charting constraints (Q1–Q12)

- **Q1b** — generated core, deliberately extended: sample a base with the tool,
  then grow lexicon and grammar to cover the story.
- **Q2a** — deliverable is the `index,english,hono` CSV only.
- **Q3a** — this dedicated workspace.
- **Q4a** — the agent translates by hand; the tool produces and validates the
  language.
- **Q5a** — name `hono`, from the sampled root `hono` "sea".
- **Q6a** — pin inventory `p t k m n s l r w h` / `a e i o u` and syllables
  `CV, CVC`; fix the seed; sample morphology/syntax; freeze with `accept`.
- **Q7a** — the lexicon lives in the tool's spec/model; render a readable copy.
- **Q8c** — audit gaps first, decide per gap: default **paraphrase**, extend the
  tool only for wide reach.
- **Q9a** — method: English → Hono lookup, verify back, paraphrase, quarantine
  `[slot]`, normalize dialogue quotes.
- **Q10a** — mirror the sibling workspaces.
- **Q11a** — adapt personal names; calque/compound place names.
- **Q12a** — definition of done: 111 rows, legal forms, consistent gloss, slots
  marked, checked by a validator.

## Tooling notes

- Author text files with the Write tool only (clean UTF-8); avoid PowerShell
  text round-trips (they mis-encode non-ASCII).
- Regenerate the model from the spec:
  `C:\Users\bmcke\conlang\.venv\Scripts\python -m conlang.cli generate --spec spec\hono.yaml --out out\hono.json`.
- **Morphology is pinned in the frozen spec.** A change to the tool's verb/noun
  affixes (e.g. a new category) does *not* reach Hono on a plain regenerate: the
  affix list must be re-derived (regenerate with `affixes`/`category_order`
  unpinned, lexicon kept) and re-`accept`ed. See the *Build aspect* ticket.
- Hono's grammar sketch and dictionary are rendered to `reference/hono-grammar.md`.
- Validate the translation:
  `C:\Users\bmcke\conlang\.venv\Scripts\python.exe tools\validate_hono.py` —
  checks the 111-row shape, that every Hono token is phonotactically legal, and
  that slots are marked; an empty cell reports as *untranslated*, not an error.
- Compose a hand translation from a gloss script (works for any language):
  `template/tools/compose_translation.py --model out\hipke.json --glosses the_quiet_morning_hipke.tsv --sentences the_quiet_morning_sentences.csv --out the_quiet_morning_hipke.csv`
  — it appends a `romanization` column automatically when the model has an
  orthography map. Validate the result with
  `template/tools/validate.py --csv <csv> --model <model> --rows 111 --column hipke`
  (add `--header index,english,hipke,romanization` when the romanisation column
  is present).

## References

- Workspace map: `wayfinder/map.md`
- **Translation method & slot policy**: `reference/hono-translation-method.md`
- Slot log: `reference/hono-slots.md`
- Lexicon: `reference/hono-lexicon.md` · grammar: `reference/hono-grammar.md`
- Glossary: `GLOSSARY.md`
- Research findings: `research/grammar-gaps.md`, `research/concept-inventory.md`

## Optional extras

- **Glossed parallel text**: `the_quiet_morning_hono_gloss.csv`
  (`index,english,hono,gloss`) — the gloss column is auto-derived from the model's
  exact word forms and affix surface forms.
- **Word document**: `the_quiet_morning_hono.docx` — the parallel text (English,
  Hono, gloss) as a `.docx` (built directly as OOXML; `python-docx` is not
  installed).
- **Recall deck**: `reference/hono-deck.html` — a self-contained flashcard deck
  (gloss → root/pos) for all 680 lexemes.

### Hipke extras

- **Glossed parallel text**: `the_quiet_morning_hipke_gloss.csv`
  (`index,english,hipke,romanization,gloss`) — the gloss and romanisation are
  auto-derived from the model.
- **Word document**: `the_quiet_morning_hipke.docx` — the parallel text (English,
  romanised spelling, phonemic Hipke, gloss).
- **Recall deck**: `reference/hipke-deck.html` — 579 lexemes, card backs showing
  the romanised spelling beside the phonemic root.
