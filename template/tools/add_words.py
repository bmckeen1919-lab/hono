"""Grow a frozen spec's lexicon with translation-driven vocabulary.

Run with the toolkit interpreter::

    python template/tools/add_words.py --spec spec\\veshtari.yaml --words words.json

``words.json`` is a list of ``[gloss, pos]`` pairs, or a ``{gloss: pos}`` map.
Each new gloss gets a collision-free root (seeded per item, so existing words
never shift), pinned into the spec; the spec is then re-frozen.

Reserved pos (``adp``, ``cop``, ``conj``) belong to generated classes and cannot
be added this way.
"""

from __future__ import annotations

import argparse
import json
import pathlib

from conlang.lexicon.generate import _unique_root
from conlang.model import Inventory
from conlang.pipeline import generate
from conlang.sampling.defaults import make_templates
from conlang.sampling.rng import Rng
from conlang.spec import LexemeSpec, dump_spec, load_spec, to_spec

RESERVED = {"adp", "cop", "conj"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec", required=True)
    parser.add_argument("--words", required=True, help="JSON list/map of gloss -> pos")
    parser.add_argument("--out", default=None, help="model JSON path (default <workspace>/out/<id>.json)")
    args = parser.parse_args()

    spec = load_spec(args.spec)
    assert spec.phonology is not None, "the spec must pin a phonology"
    data = json.loads(pathlib.Path(args.words).read_text(encoding="utf-8"))
    items = list(data.items()) if isinstance(data, dict) else [(g, pos) for g, pos in data]

    existing = {entry.gloss for entry in spec.lexicon}
    taken = {entry.root for entry in spec.lexicon}
    inventory = Inventory(
        consonants=list(spec.phonology.consonants), vowels=list(spec.phonology.vowels)
    )
    templates = make_templates(list(spec.syllables or []))

    added: list[LexemeSpec] = []
    skipped: list[str] = []
    for gloss, pos in items:
        if pos in RESERVED:
            skipped.append(f"{gloss} ({pos})")
            continue
        if gloss in existing:
            continue
        existing.add(gloss)
        rng = Rng(spec.seed or 0, f"lex:{gloss}")
        root = _unique_root(rng, inventory, templates, taken, spec.onsets)
        taken.add(root)
        added.append(LexemeSpec(gloss=gloss, root=root, pos=pos, locked=True))

    spec = spec.model_copy(update={"lexicon": [*spec.lexicon, *added]})
    language = generate(spec)
    frozen = to_spec(language)

    pathlib.Path(args.spec).write_text(dump_spec(frozen), encoding="utf-8", newline="\n")
    out = (
        pathlib.Path(args.out)
        if args.out
        else pathlib.Path(args.spec).resolve().parents[1] / "out" / f"{language.id}.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(language.model_dump_json(indent=2), encoding="utf-8", newline="\n")

    print(f"added {len(added)} -> {[(entry.gloss, entry.root) for entry in added]}")
    if skipped:
        print(f"skipped reserved pos: {skipped}")
    print(f"{language.id}: {len(language.lexemes)} lexemes, {len(language.words)} word forms")
    print(f"wrote {args.spec} and {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
