---
title: Resolve each structural gap (extend vs paraphrase)
label: wayfinder:grilling
status: closed
assignee: opencode
blocked-by: [grammar-gap-audit]
---

## Question

Apply the Q8 policy to the audit: for each structural gap, decide **extend the tool** or **paraphrase outside it** (default paraphrase; extend only for high-reach gaps). Record the decision and rationale per gap, and graduate a ticket for each feature we choose to build. Blocked until the audit closes.

## Resolution

Resolved with the learner (2026-10-05): **Q1c** — extend the tool for the **predication tier + aspect**; **Q2a** — numerals/measures via **lexicon** (no tool change); **Q3a** — adopt the audit's misdiagnosed verdict (paraphrase passive / relatives / reported speech / existential / comparative / wh-questions).

Per-gap decision:

| gap | reach | decision |
| --- | --- | --- |
| adpositions / oblique / place-direction | 95 | **build** → *Build adpositions, obliques, and place/direction* |
| NP modification | 81 | **build** → *Build NP modification (adjective, possessive, apposition)* |
| clause embedding | 63 | **paraphrase** via parataxis (no dedicated embedding) |
| intransitive clause | 51 | **build** → *Build intransitive (one-argument) clauses* |
| copula / predicate / existential | 41 | **build** → *Build copula, predicate-adjective, and existential* |
| adverbial / adjunct | ~35 | **paraphrase** (lean on copula + parataxis) |
| clause / VP coordination | 31 | **build** → *Build clause sequencing (parataxis / coordination)* |
| aspect / tense tier | 29 | **build** → *Build aspect (progressive, perfect, pluperfect)* |
| relative clause | 18 | **paraphrase** via parataxis |
| reported speech | 18 | **paraphrase** via juxtaposition |
| numerals / measures | 17 | **lexicon** (pinned measures; analytic composition) |
| passive | 13 | **paraphrase** as active |
| 1st / 2nd-person agreement | ~11 | **paraphrase** (pronouns as lexicon; no new agreement) |
| ditransitive | ~10 | **paraphrase** |
| comparative / degree | 10 | **paraphrase** (analytic degree word) |
| negation | 9 | **paraphrase** (ad-hoc particle) |
| modality | 5 | **paraphrase** |
| imperative / reflexive / conditional | ≤2 | **paraphrase** |
| question | 0 | n/a |

**Graduated build tickets:** *Build intransitive (one-argument) clauses* · *Build copula, predicate-adjective, and existential* · *Build adpositions, obliques, and place/direction* · *Build NP modification (adjective, possessive, apposition)* · *Build clause sequencing (parataxis / coordination)* · *Build aspect (progressive, perfect, pluperfect)*.

Builds happen in the tool repo `C:\Users\bmcke\conlang`; after each, Hono's `spec/hono.yaml` + `out/hono.json` are regenerated so the model stays authoritative. The numerals/measures decision feeds `design-lexicon`.
