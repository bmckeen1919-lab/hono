# Notes

## Status

Workspace scaffolded; the language is built — **536 lexemes / 3577 word forms**,
lint `valid` — and the working method is written. The destination — translate all
111 sentences of *The Quiet Morning* into Hono — and the route are charted in
`wayfinder/map.md`. Remaining: the CSV validator, then the translation batches.

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

## References

- Workspace map: `wayfinder/map.md`
- **Translation method & slot policy**: `reference/hono-translation-method.md`
- Slot log: `reference/hono-slots.md`
- Lexicon: `reference/hono-lexicon.md` · grammar: `reference/hono-grammar.md`
- Glossary: `GLOSSARY.md`
- Research findings: `research/grammar-gaps.md`, `research/concept-inventory.md`
