# Repeat this with a new generated language

A runbook for producing another language with the [`conlang` toolkit](https://github.com/bmckeen1919-lab/conlanggen)
and translating *The Quiet Morning* into it — the process that produced Hono.

The toolkit already ships the whole **predication tier + aspect**, so a new
language inherits the syntax; you only choose a spec, grow a lexicon, and
translate. Scripts live in `template/tools/`. Run them with the toolkit's
interpreter, e.g. `C:\Users\bmcke\conlang\.venv\Scripts\python.exe`.

## 1. Freeze a base language

```powershell
python template/tools/new_language.py --name Veshtari --seed 42 `
  --consonants p,t,k,m,n,s,l,r,v,sh --vowels a,e,i,o,u --syllables CV,CVC,V --out .
```

Writes `spec/<id>.yaml` (frozen, fully explicit) and `out/<id>.json` (the model).
The model is the source of truth from here on.

## 2. Build the lexicon to cover the text

Extract the text's concept inventory (gloss + rough pos), then add the missing
words in small batches:

```powershell
python template/tools/add_words.py --spec spec\veshtari.yaml --words template\words.example.json
```

`words.json` is a list of `[gloss, pos]` pairs (or a `{gloss: pos}` map). The
script generates a **collision-free root** per gloss (seeded per item, so existing
words never shift), pins it into the spec, and regenerates + re-freezes.

> **`pos` is one of:** `noun, verb, adj, num, part, pron, det, mod, sub, adv`.
> **`adp`, `cop`, `conj` are reserved** for generated classes — a lexicon entry
> with one of those is silently dropped. Use the generated class, or paraphrase.

## 3. Write the method and build the validator

- Copy `reference/hono-translation-method.md` and reword the language-specific
  bits (inventory, syllable rule, paraphrase strategies).
- Copy `tools/validate_hono.py`, or use the generalized
  `template/tools/validate.py`:

```powershell
python template/tools/validate.py --csv the_quiet_morning.csv --model out\veshtari.json --rows 111
```

## 4. Translate in batches

Compose each clause from the model with `template/tools/compose.py` (so every
inflected form is accurate), paraphrase what the language can't say, and mark
irreducible items `[slot]`:

```python
from template.tools.compose import Composer
c = Composer(r"out\veshtari.json")
sentence = [c.noun("sun", "ABS"), c.verb("rise", ("PST", "PROG")), c.root("above"), c.root("ocean")]
print(" ".join(sentence))          # surface words
print(c.gloss(sentence))           # interlinear gloss
```

A sentence is a list of tokens; `c.noun(g, case)` marks case, `c.verb(g, tags)`
applies tense/aspect plus 3SG agreement, `c.root(g)` is a bare word (adjectives,
obliques, function words), `c.ordinal()` is "first". Join clauses with a
conjunction root or juxtaposition.

Run the validator after each batch; keep a slot log.

## 5. Resolve slots, then extras

Add the missing roots (`add_words.py`) and clear the slot log. Optionally render
a **gloss column**, a **`.docx`**, and a **recall deck** (all derived from the
model — see the Hono workspace for examples).

## 6. Docs and repo

`MISSION.md`, `NOTES.md`, `RESOURCES.md`, `GLOSSARY.md`, a `README.md`, then
`git init` + a remote + push.

## Gotchas that cost time (so they don't next time)

- **Frozen specs pin the affixes.** A toolkit change to the morphology is *not*
  picked up by a plain regenerate: re-derive the affix list (regenerate with
  `affixes`/`category_order` unpinned, lexicon kept) and re-`accept`.
- **Agreement is a clause affix**, not part of a verb's stored forms — compose
  verbs as *model form + the 3SG form* (the `Composer.verb` helper does this).
- **Pronouns don't take case**; use them bare. **Names** are ordinary nouns,
  adapted to the phonology.
- **Use the same story** as your other languages — that is what makes the
  translations comparable.
