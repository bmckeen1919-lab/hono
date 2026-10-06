---
title: Scaffold the Hono workspace
label: wayfinder:task
status: closed
assignee: opencode
blocked-by: []

---

## Question

Stand up the Hono workspace to mirror the sibling translation projects (`learn_kah`, `muna`, `volapuk`): `MISSION.md`, `NOTES.md`, `RESOURCES.md`, `reference/`, `learning-records/`. `the_quiet_morning_sentences.csv` is already copied in. Record the charting constraints (Q1–Q12) in `NOTES.md`, write the first learning record, and commit the frozen base spec + model once `freeze-base-language` resolves.

## Resolution

Scaffolded the workspace (AFK), mirroring the siblings.

**Created:** `MISSION.md` (the translation brief); `NOTES.md` (the Q1–Q12 charting constraints plus tooling notes, including the pinned-morphology caveat); `RESOURCES.md` (primary sources, knowledge, siblings, communities); `reference/hono-grammar.md` (the model's rendered grammar sketch + dictionary, 82 KB); `learning-records/0001-quiet-morning-hono-kickoff.md`; `.gitignore`.

**Repo:** `git init` + initial commit (`chore: scaffold the Hono workspace`) carrying the frozen `spec/hono.yaml` + `out/hono.json` (199 lexemes, 1409 word forms, lint `valid`) and the whole `wayfinder/` map. The local git identity was set to match the sibling repos.