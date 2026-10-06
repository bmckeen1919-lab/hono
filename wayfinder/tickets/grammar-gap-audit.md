---
title: Grammar-gap audit of the 111 sentences
label: wayfinder:research
status: closed
assignee:
blocked-by: []

---

## Question

Audit all 111 sentences of *The Quiet Morning* against the `conlang` tool's grammar and semantics, and produce a **reach-ranked gap table** at `research/grammar-gaps.md` (method: `muna/translation-gaps.md`). For each construction the tool cannot express today, record: what the gap is, which sentences it bites, and its **reach** (how many of the 111 sentences it touches). This lets `resolve-structural-gaps` rank fixes by cost. AFK — run as a research subagent.

## Resolution

Resolved AFK by a research subagent (2026-10-05). Findings: `../../research/grammar-gaps.md`.

The tool expresses exactly **one finite transitive clause** (S-V-O, NOM/ACC or ERG/ABS, fixed 3SG agreement; noun PL/DIM/AUG, verb PST/FUT, ordinals), so **0 of 111** sentences render as-is. Top gaps by **reach**: oblique/place/direction (95), NP modification (81), clause embedding/subordination (63), intransitive clause (51), copula / predicate-adjective / existential (41); then adverbials (35), coordination (31), aspect/pluperfect (29), numerals >3 (17). **Misdiagnoses to not build**: passive, relativization, reported speech, comparative, and wh-questions (reach 0) are reachable by paraphrase. Feeds `resolve-structural-gaps`.