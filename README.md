# Hono

A constructed language produced by the [`conlang`](https://github.com/bmckeen1919-lab/conlanggen)
generator, **generated then deliberately extended** — and a complete parallel-text
translation of the 111-sentence English story *The Quiet Morning*.

> **The model is the source of truth.** `out/hono.json` (reproducible from
> `spec/hono.yaml`) is canonical; the dictionary, grammar sketch, and glossed text
> are all rendered or derived from it.

## The translation

`the_quiet_morning_hono.csv` — all **111 sentences**, one per row
(`index,english,hono`). Every form is phonotactically legal under Hono's inventory
and constraints; the validator reports `111/111 translated · 0 slots · 0 errors`.

Optional renderings of the same text:

| file | what |
| --- | --- |
| `the_quiet_morning_hono.csv` | the parallel text — **the deliverable** |
| `the_quiet_morning_hono_gloss.csv` | the parallel text with an interlinear `gloss` column |
| `the_quiet_morning_hono.docx` | the parallel text as a Word document |

## The language

Hono is a small, head-initial (`SVO`) **ergative** language. `spec/hono.yaml`
pins its sound system and syllable shapes, samples the rest, and freezes
everything with the toolkit's `accept`; the lexicon and grammar were then grown
(predication tier + aspect + a story-sized vocabulary) to cover the text.

- **Inventory:** `p t k m n s l r w h` / `a e i o u`; syllables `CV, CVC`.
- **Morphology:** noun plural/diminutive/augmentative; verb past/future,
  progressive/perfect (pluperfect = `past + perfect`); 3SG agreement; a copula.
- **Syntax:** transitive/intransitive/copular clauses, adpositions and obliques,
  noun phrases (adjectives, possessor, apposition, PP), and clause sequencing
  (parataxis + conjunctions).
- **Size:** **680 lexemes / 5175 word forms**, lint `valid`.

`reference/hono-grammar.md` holds the rendered grammar sketch and dictionary;
`reference/hono-lexicon.md` is the lexicon (gloss / pos / root);
`reference/hono-deck.html` is a recall deck.

## Working with it

```powershell
# regenerate the model from the frozen spec
C:\Users\bmcke\conlang\.venv\Scripts\python -m conlang.cli generate --spec spec\hono.yaml --out out\hono.json

# check the translation (111 rows, legal forms, [slot] marking)
C:\Users\bmcke\conlang\.venv\Scripts\python tools\validate_hono.py
```

> **Note:** morphology is pinned in the frozen spec, so a toolkit change to the
> affixes is *not* picked up by a plain regenerate — the affix list must be
> re-derived (regenerate with `affixes`/`category_order` unpinned, lexicon kept)
> and re-`accept`ed.

## Layout

```text
spec/hono.yaml                 the frozen, fully-explicit spec
out/hono.json                  the model (source of truth)
the_quiet_morning_sentences.csv   the English source
the_quiet_morning_hono*.csv/docx  the translation(s)
reference/                     grammar, lexicon, method, slots, recall deck
research/                      gap audit and concept inventory
tools/                         the CSV validator
wayfinder/                     the plan (map + decision tickets)
MISSION.md · NOTES.md · RESOURCES.md · GLOSSARY.md
```

## How the translation was made

By hand, against the model as the authority, following the method in
`reference/hono-translation-method.md`: look up each word's root, verify the
sense, assemble clauses, and **paraphrase** what the language cannot say
(passive → active; relatives/reported speech → parataxis; non-finite clauses →
clauses; analytic comparatives; compounds → word sequences; existential →
locative), quarantining anything irreducible as a logged `[slot]`.

*The Quiet Morning* is also translated into sibling languages (Kah, Muna,
Volapük), which is why one fixed story is used.

## License

Code and generated language under MIT. The `conlang` toolkit lives at
[bmckeen1919-lab/conlanggen](https://github.com/bmckeen1919-lab/conlanggen).
