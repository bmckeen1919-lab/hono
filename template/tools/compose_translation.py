"""Compose a translation into a frozen model from a hand-authored gloss script.

Run with the toolkit interpreter::

    python template/tools/compose_translation.py --model out\\hipke.json \\
        --glosses the_quiet_morning_hipke.tsv --sentences the_quiet_morning_sentences.csv \\
        --out the_quiet_morning_hipke.csv

The gloss script is a TSV of ``index<TAB>gloss``. Each gloss is a space-separated
sequence of tokens ``gloss[.TAG...]``; a multi-word gloss joins its words with
``~`` (e.g. ``sea~pink.NOM``). A token is realised by the :class:`Composer`:

- a core-case tag (NOM/ACC/ERG/ABS, read from the model) -> an inflected noun
- ``ORD`` -> the ordinal
- a tense/aspect tag (PST/FUT/PROG/PERF) and/or ``3SG`` -> an inflected verb
- no tags -> a bare word (adjective, oblique, function word)

Every index in the sentence list gets a row; an index with no authored gloss is
left empty (the validator reports it as *untranslated*, not an error).
"""

from __future__ import annotations

import argparse
import csv
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from template.tools.compose import Composer  # noqa: E402

from conlang.phonology.romanize import romanize  # noqa: E402

TENSES = {"PST", "FUT", "PROG", "PERF"}


def _read_glosses(path: pathlib.Path) -> dict[str, str]:
    glosses: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        index, _, gloss = line.partition("\t")
        glosses[index.strip()] = gloss.strip()
    return glosses


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True)
    parser.add_argument("--glosses", required=True, help="TSV of index<TAB>gloss")
    parser.add_argument("--sentences", required=True, help="CSV of index,sentence")
    parser.add_argument("--out", required=True)
    parser.add_argument("--column", default=None, help="output column name (default: the model id)")
    args = parser.parse_args()

    composer = Composer(args.model)
    language = composer.lang
    column = args.column or language.id
    case_labels = {
        a.gloss for a in language.affixes if a.gloss in {"NOM", "ACC", "ERG", "ABS"}
    }
    romanizes = bool(language.inventory.orthography)

    def romanize_surface(surface: str) -> str:
        if not romanizes or not surface:
            return ""
        inventory = language.inventory
        return " ".join(romanize(t, inventory, inventory.orthography) for t in surface.split())

    def token(spec: str) -> str:
        gloss, *tags = spec.split(".")
        gloss = gloss.replace("~", " ")
        for tag in tags:
            if tag in case_labels:
                return composer.noun(gloss, tag)
        if "ORD" in tags:
            return composer.ordinal()
        verb_tags = tuple(t for t in tags if t in TENSES)
        if verb_tags or "3SG" in tags:
            return composer.verb(gloss, verb_tags, agreement="3SG" in tags)
        return composer.root(gloss)

    authored = _read_glosses(pathlib.Path(args.glosses))
    sentences = list(
        csv.DictReader(pathlib.Path(args.sentences).read_text(encoding="utf-8").splitlines())
    )

    problems: list[str] = []
    rows: list[dict[str, str]] = []
    for row in sentences:
        index = row["index"]
        gloss = authored.get(index, "")
        surface = ""
        if gloss:
            words: list[str] = []
            for spec in gloss.split():
                try:
                    words.append(token(spec))
                except Exception as error:  # noqa: BLE001 - report, don't crash
                    problems.append(f"row {index}: {spec!r} -> {error}")
                    words.append("?")
            surface = " ".join(words)
        row_out = {"index": index, "english": row["sentence"], column: surface}
        if romanizes:
            row_out["romanization"] = romanize_surface(surface)
        rows.append(row_out)

    fieldnames = ["index", "english", column] + (["romanization"] if romanizes else [])
    out = pathlib.Path(args.out)
    with out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    translated = sum(1 for r in rows if r[column])
    print(f"{language.id}: {translated}/{len(rows)} translated -> {out}")
    for problem in problems:
        print(f"  problem: {problem}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
