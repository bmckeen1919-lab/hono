# Hono slot log

Running list of what **Hono cannot say** yet, found while translating
`the_quiet_morning_sentences.csv`. Each row is a `[slot]` marked in the Hono
column of `the_quiet_morning_hono.csv`.

A slot is **data**, not failure: it is the queue for later lexicon growth. When a
slot is resolved (a root added, or a paraphrase documented in
`reference/hono-translation-method.md`), fill the *resolution* column and clear
the `[slot]` in the CSV.

| # | english | why (no root / no construction) | resolution |
| --- | --- | --- | --- |
| 9 | cicada | no root — fine-grained fauna | **resolved** — root `kelupre` added |
| 9 | stonechat | false positive — the root existed as `pamwu` | **resolved** — `pamwu` used |

**No open slots.** The translation is `111/111` with `0` slots.
