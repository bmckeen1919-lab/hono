"""Scaffold and freeze a new generated language.

Run with the toolkit interpreter::

    python template/tools/new_language.py --name Veshtari --seed 42 \
      --consonants p,t,k,m,n,s,l,r,v,sh --vowels a,e,i,o,u --syllables CV,CVC,V --out .

Writes ``<out>/spec/<id>.yaml`` (frozen, fully explicit) and
``<out>/out/<id>.json`` (the model).
"""

from __future__ import annotations

import argparse
import pathlib

from conlang.pipeline import generate
from conlang.spec import PhonologySpec, Spec, dump_spec, to_spec


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", required=True)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--consonants", required=True, help="comma-separated")
    parser.add_argument("--vowels", required=True, help="comma-separated")
    parser.add_argument("--syllables", required=True, help="comma-separated, e.g. CV,CVC,V")
    parser.add_argument("--out", default=".", help="workspace root (default: .)")
    args = parser.parse_args()

    spec = Spec(
        name=args.name,
        seed=args.seed,
        phonology=PhonologySpec(
            consonants=args.consonants.split(","), vowels=args.vowels.split(",")
        ),
        syllables=args.syllables.split(","),
    )
    language = generate(spec)
    frozen = to_spec(language)

    out = pathlib.Path(args.out)
    spec_path = out / "spec" / f"{language.id}.yaml"
    model_path = out / "out" / f"{language.id}.json"
    spec_path.parent.mkdir(parents=True, exist_ok=True)
    model_path.parent.mkdir(parents=True, exist_ok=True)
    spec_path.write_text(dump_spec(frozen), encoding="utf-8", newline="\n")
    model_path.write_text(language.model_dump_json(indent=2), encoding="utf-8", newline="\n")

    print(f"{language.id}: {len(language.lexemes)} lexemes, {len(language.words)} word forms")
    print(f"wrote {spec_path}")
    print(f"wrote {model_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
