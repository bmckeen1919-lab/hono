# Grammar-gap audit — *The Quiet Morning* → a `conlang`-generated language

Reach-ranked log of what the `conlang` tool can and cannot express, found by
reading the tool and translating `C:\Users\bmcke\hono\the_quiet_morning_sentences.csv`
(111 sentences) against it. Base language pinned to inventory
`p t k m n s l r w h` / `a e i o u`, syllables `CV, CVC`; morphology and syntax are
sampled by the tool.

## How to read this

- **Reach** = the number of the 111 sentences the gap touches. It is a coverage
  count, not a cost estimate. It is **not comparable to the Muna log's reach**
  (`C:\Users\bmcke\muna\translation-gaps.md`), where the largest open gap was 8:
  that tool was a near-complete language with a handful of holes. This tool is a
  v1 that models **one clause shape**, so its reach numbers are dozens and the
  whole story is out of reach as-is. That is the finding, not a bug in the count.
- **Structural** rows are missing grammar; they block whole classes of sentence
  and are the reason the lexical rows cannot simply be filled in.
- **Lexical** rows are missing words. The tool supports pinning any number of
  lexicon entries (`Spec.lexicon`, `spec.py:63`; `pipeline._resolve_concepts`),
  so lexical gaps need no new mechanism — only entries.
- **Misdiagnosed** rows are English constructions that look like missing
  machinery but are already expressible by paraphrase. Following the Muna
  precedent (LR 0044/0045), each is flagged rather than filed as a defect.
- Reach counts for the structural matrix were computed from a per-sentence tag
  table; adverb reach is marked *approx.* where judgment was involved.

## Method

Inspected `README.md`, `CONTEXT.md`, and `src/conlang/{syntax/__init__.py,
morphology/generate.py, model/__init__.py, pipeline.py, spec.py,
lexicon/generate.py, sampling/concepts.py, sampling/defaults.py,
render/markdown.py, lint/__init__.py, phonology/syllable.py}`. Ran
`python -m conlang.cli generate` on a pinned base spec and read the rendered
grammar sketch to confirm what is actually emitted (not just declared).

## Baseline — what a generated language can express

| capability | status | source |
| --- | --- | --- |
| Word order | SOV / SVO / VSO, weighted toward SOV/SVO; sampled | `syntax/__init__.py:19-21`, `25-29`; README "Syntax" |
| Alignment / case | accusative (`NOM`/`ACC`) or ergative (`ERG`/`ABS`) on subject & object only | `syntax/__init__.py:53-61`; `morphology/generate.py:56`, `232-254` |
| Subject agreement | **3SG only**, fixed | `morphology/generate.py:58`; `syntax/__init__.py:62-63` |
| Clause shape | exactly one finite **transitive** clause: subject, verb, object (3 constituents) | `syntax/__init__.py:32-71`; `model/__init__.py:101-105` |
| Noun inflection | plural / diminutive / augmentative, 2 declensions | `morphology/generate.py:28-33`, `46` |
| Verb inflection | past (suffix), future (prefix), 2 conjugations | `morphology/generate.py:39-41` |
| Numerals | lexemes `one/two/three`; ordinal affix | `sampling/concepts.py:186-188`; `morphology/generate.py:42` |
| Lexicon | 160-item Swadesh-style core; arbitrary entries can be pinned | `sampling/concepts.py:6-191`; `spec.py:56-70` |

Everything else the prompt asks about — intransitive clauses, embedding,
adpositions, copulas, aspect, negation, questions, relativization, coordination,
comparatives, passives, existentials, quotation, conditionals — is absent. The
syntax module says so itself: "This is the small end of syntax"
(`syntax/__init__.py:3`), and `linearize` accepts and returns exactly three
constituents (`syntax/__init__.py:32-38`).

## A. Structural gaps — ranked by reach

| gap | reach | where it bites (sentences) | note |
|---|---|---|---|
| **No adposition / oblique / place-direction grammar** | **95** | nearly all; e.g. 1 *above*, 4 *in*, 8 *into*, 14 *into*, 45 *into*, 63 *from…to*, 71 *with*, 89 *toward*, 94 *against* | No adposition POS exists in the lexicon core or any PP rule. Place and direction are 95 sentences of this text. Largest single gap. |
| **No NP modification** (adjective, possessive, apposition, PP-in-NP, noun+noun) | **81** | 2 *large blue mirror*, 6 *his elderly neighbor*, 10 *his neighbor's old cottage*, 11 *whitewashed walls*, 32 *a lone gannet*, 72 *the launch line* | `build_clause` takes bare lexemes; there is no rule joining adjective to noun, no possessive, no apposition. A "noun phrase" is one word. |
| **No clause embedding** (subordination, complementation, non-finite/participial clauses) | **63** | 6 *who used to say that…when…*, 15 *to open…*, 32 *watching…glide*, 40 *try to calm*, 54 *who needed to learn*, 67 *was punctuated by…measuring*, 111 *needing to escape* | The single biggest *kind* of gap: relatives, complements, purpose, participial adjuncts, gerunds and infinitives all reduce to embedding, none of which exists. Rows 8–9 are facets. |
| **No intransitive (one-argument) clause** | **51** | 1 *the sun was rising*, 3 *Iain stood*, 7 *smiled*, 8 *the path wound*, 46 *the door swung*, 77 *the boat floated*, 101 *boots crunched* | `build_clause` requires a subject **and** an object (`syntax/__init__.py:41-65`); there is no one-argument path. Intransitive predication is unreachable. |
| **No copula / predicate nominal or adjective / existential** | **41** | 2 *water was calm*, 13 *noise felt still*, 20 *I'm Clara*, 74 *She's ready*, 75 *the tide is perfect*, 91 *There's a spot*, 103 *was something* | No `be` lexeme; no adjective-predicate or existential rule. Predicate adjectives/nominals cannot be predicated at all. |
| **No adverbial / adjunct class or placement** *(approx.)* | **~35** | 9 *rhythmically*, 19 *softly*, 26 *faintly*, 32 *effortlessly*, 42 *suddenly*, 63 *slowly*, 76 *smoothly* | No adverb POS and no adjunct slot. Excludes directional (row 1) and degree (row 12). |
| **No clause / VP coordination** ("and" is a bare lexeme, no rule) | **31** | 7 *smiled and continued*, 11 *…but the garden…*, 40 semicolon, 46 *clicked open, and…*, 67 listing, 101 *gravel and mortar* | `and` exists in the concept list (`concepts.py:189`) but no combinator ever uses it. Neither clause nor noun coordination is buildable. |
| **No aspect, nor tense beyond one PST/FUT slot** (progressive, perfect, pluperfect, habitual) | **29** | 1 *was rising*, 6 *used to say / will be*, 14 *had left*, 30 *were coming*, 52 *hadn't…left*, 73 *had carried / had lifted*, 111 *had been planning* | Only `past` and `future` affixes are generated (`morphology/generate.py:39-41`). No aspect tier, no anteriority, no habitual. |
| **No relative clause** | **18** | 6, 10, 32, 54, 63, 69, 73, 81, 88, 97, 102, 107 | Facet of embedding (row 3). No relativizer and no way to attach a clause to a noun. |
| **No reported speech / quotative / clausal complement of "say"** | **18** | 6, 19, 25, 27, 28, 35, 36, 37, 54, 59, 65, 74, 89, 105, 106, 107 | Facet of embedding (row 3). `say/tell` cannot take a clause or a second object. |
| **No numeral system beyond one–three; no measures/scales** | **17** | 11 *decades*, 13 *months*, 64 *miles*, 65 *months*, 69 *six months*, 72 *half a year*, 81 *three miles*, 106 *fifty years* | `one/two/three` and the ordinal affix exist; anything above three and every measure noun does not. Partly misdiagnosed (below). |
| **No passive / voice** | **13** | 11, 40, 51, 56, 64, 67, 73, 88, 96, 98, 103, 109 | Misdiagnosed as a voice gap — see §C. Agentless passives still stall on other rows. |
| **No 1st/2nd-person agreement** (3SG only) | **~11** | 19 *I didn't*, 20 *I'm*, 21 *I used*, 30 *I heard*, 62 *I can*, 65 *I'm*, 107 *I think* | Agreement is fixed `3SG` (`morphology/generate.py:58`). "I/you" subjects have no agreeing form. |
| **No comparative / equative / superlative / degree** | **10** | 9 *louder*, 13 *as still as*, 59 *best*, 65 *clearer than*, 69 *as calm as*, 84 *smaller*, 93 *stronger*, 98 *cooler* | `category_order` advertises `comparative > superlative` (`morphology/generate.py:31`) but no such affix is ever generated — a trap. See §C. |
| **No negation syntax** ("not" is a lexeme, no rule) | **9** | 2 *without movement*, 19 *didn't*, 40 *no*, 44 *no urge*, 52 *hadn't*, 59 *doesn't*, 68 *wasn't*, 80 *hadn't*, 109 *not just* | `not` exists in the concept list (`concepts.py:190`) but no rule places it. Presence ≠ support. |
| **No ditransitive / oblique case** (only `NOM/ACC` or `ERG/ABS`) | **~10** | 14 *left him*, 15 *let…in*, 35 *told me to give you*, 43 *giving him*, 52 *left him*, 54 *told me*, 106 *told me* | Case is only subject/object (`syntax/__init__.py:53-61`); recipient/benefactive has no mark and no second-object slot. |
| **No modality** (can/could/need/used to) | **5** | 21, 27, 37, 61, 62 | No modal class or construction. |
| **No imperative** | **2** | 41 *Give yourself permission*, 90 *Aim for the gap* | No imperative morphology or clause type. |
| **No reflexive** | **1** | 41 *yourself* | No reflexive pronoun or binding rule. |
| **No conditional** | **1** | 62 *if you're ready* | No conditional marker or protasis construction. |
| **No question syntax/morphology** | **0** | — | **Phantom gap**: the story contains no questions. Recorded to show a capability that is absent but costs nothing here. |

## B. Lexical gaps (missing words) — grouped, by reach

The built-in lexicon is a 160-item Swadesh core (`sampling/concepts.py`); a
literary story needs hundreds of content words it does not contain. Because
lexicon entries can simply be pinned (`Spec.lexicon`, `spec.py:24-30`), these are
**not structural** — but they are numerous, and filling them does not help until
§A is addressed, because the words have nowhere to attach.

| field | reach *(approx.)* | examples (sentences) |
|---|---|---|
| Place / sea / landscape nouns | ~45 | shore (3), bay (6,12,69,74), ridge/crest (10,80,84,97), cliff (8,97), tide (44,89,100), current (89), sandbar (85), surf (94), beacon (81,91,97,99,102), ruins (102), island (81,97) |
| Body / artifact / tool nouns | ~40 | pocket & jacket (14), brass key (14,45), boots & laces (17,29), tote (17,33), ledger (33), leather (38), palm (38), page (39), plank (50,52,58,78), tool (50), latch (16), gate (16), shutter (15,48), oar (78,79,82) |
| Nature nouns | ~25 | breeze (3,21), dew (8), grass (8,29,66), rosemary (11,25,66), thyme (98), cicada (9), stonechat (9), gannet (32), sand eel (87), moss (104), lavender (47) |
| Abstract / mind nouns | ~30 | memory (6), noise (13), silence (19), moment (32), burden (36,73), future/present (37), permission (41), mood (27), chance (28), understanding (32), grief (56), exhaustion (56), history (31) |
| Verbs (motion, perception, speech, change) | ~50 | rise (1), smile (7), continue (7), wind/curve (8), blend (9), nod (22,43,92), pause (12,86), claim (27), predict (27), sort through (30), glide (32), scrape (94), unwrap (110), keep alive (25) |
| Adjectives / qualities | ~40 | elderly (6), wet (8), rhythmic (9), melodic (9), motionless (26), welcoming (22), faint (26), wild (11), sharp/slanted (39), glassy (12,79,82), rusted (96,103,108), oiled (45) |
| Numerals / measures | ~7 | decade (11), months (13,65), miles (64), six months (69), half a year (72), three miles (81), fifty years (106) |
| Adverbs | ~35 | see structural row (no adverb class) |

Proper names (*Iain*, *Clara*, *Gull Island*) are **not** counted here: they are
ordinary lexicon rows pinned with inventory-legal roots, exactly as Muna closed
its name gap (LR 0043). They are a lex/adaptation task, not a mechanism.

## C. Misdiagnosed gaps — English constructions already expressible by paraphrase

| looks like | verdict | how it is actually said |
|---|---|---|
| **Passive** (11, 40, 51, 56, …) | **Not a voice gap** | Every passive recasts to the tool's native active transitive clause with the same case/agreement machinery: "the walls were weathered by salt and wind" → *salt and wind weathered the walls*. Only agentless passives (*transformed into*, *replaced by*) still stall, and they stall on rows 1/3/4, not on voice. |
| **Relativization** (18) | **Misdiagnosed mechanism** | A relative clause is parataxis: "the old man gave me the key. He had left it." No relativizer is needed; the true blocker is row 7 (no coordination/parataxis), not a missing relative marker. |
| **Reported speech** (18) | **Misdiagnosed mechanism** | Direct quotation is juxtaposition ("Clara said: I am ready"); no complementizer or quotative is required. Again the real blocker is parataxis (row 7), not a missing speech construction. |
| **Existential *there is/was*** (40, 91, 103) | **Misdiagnosed construction** | Recasts to a locative/predicate clause ("a note lay on the table"). No existential idiom is needed; it fails only because there is no copula or locative verb (rows 1/5). |
| **Comparative / equative / superlative** (10) | **Partly misdiagnosed** | Analytic paraphrase (separate degree word: "the hum was more loud"; equality "the water is quiet and the mind is quiet") removes the need for degree morphology. Caution: the grammar sketch *lists* `comparative > superlative` in slot order although no affix is generated — do not read that line as support. |
| **Negation** (9) | **Trap, not free** | `not` is in the built-in concept list but no rule places it; presence of the lexeme is not a negation system. Real reach is small (9). |
| **Articles *the/a*** | **Not a gap** | A language may have no articles; the content is unchanged. Do not file the pervasive *the/a* as a defect. |
| **Numerals one–three + ordinal** | **Partly present** | `one/two/three` and an ordinal affix are generated (`concepts.py:186-188`; `morphology/generate.py:42`); only >3 and measures are missing (row 12). |
| **Questions, conditionals, reflexives** (0, 1, 1) | **Phantom for this text** | All are absent capabilities, but they touch 0–1 sentences. Low priority for *this* story even though they are real holes. |

## D. Consequence

No single sentence of the story is renderable by the tool as generated: every
sentence needs at least one of rows 1–7. The actionable order is therefore
**rows 1–7 first** (they unlock the bulk of the text), then the lexical batch in
§B, then the narrow structural rows (12, 14–17). The passives, quotation, and
comparative "gaps" should not be scheduled as grammar at all until §C is heeded.
