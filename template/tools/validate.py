"""Validate a translation CSV against a frozen language model.

Run with the toolkit interpreter::

    python template/tools/validate.py --csv the_quiet_morning.csv --model out\\veshtari.json --rows 111

Checks the shape (header, row count, index sequence), that each English cell is
present, and that every surface token is phonotactically legal under the model's
inventory/constraints. ``[slot]`` cells (whole or inline) are accepted; empty
cells report as *untranslated*, not errors, so the file validates as you go.
"""

from __future__ import annotations

import argparse
import csv
import pathlib

from conlang.model import Language
from conlang.phonology.syllable import is_legal_word

STRIP = " \t.,;:!?\"'()[]"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--rows", type=int, default=0, help="expected row count (0 = any)")
    parser.add_argument("--column", default="hono", help="the language column (default: hono)")
    parser.add_argument(
        "--header", default=None, help="expected header, comma-separated (default: index,english,<column>)"
    )
    args = parser.parse_args()

    language = Language.model_validate_json(pathlib.Path(args.model).read_text(encoding="utf-8"))
    with pathlib.Path(args.csv).open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    header = args.header.split(",") if args.header else ["index", "english", args.column]
    errors: list[str] = []
    if rows and list(rows[0].keys()) != header:
        errors.append(f"header is {list(rows[0].keys())!r}, expected {header!r}")
    if args.rows and len(rows) != args.rows:
        errors.append(f"expected {args.rows} rows, found {len(rows)}")

    translated = 0
    slots = 0
    for position, row in enumerate(rows, start=1):
        if (row.get("index") or "").strip() != str(position):
            errors.append(f"row {position}: index {(row.get('index') or '')!r}")
        if not (row.get("english") or "").strip():
            errors.append(f"row {position}: empty english")
        cell = (row.get(args.column) or "").strip()
        if not cell:
            continue
        if cell == "[slot]":
            slots += 1
            continue
        translated += 1
        for token in cell.split():
            if token.startswith("[") and token.endswith("]"):
                slots += 1
                continue
            word = token.strip(STRIP)
            if word and not is_legal_word(
                word, language.inventory, language.syllable_templates, language.constraints
            ):
                errors.append(f"row {position}: illegal form {word!r}")

    for error in errors[:50]:
        print(error)
    print(f"translated {translated}/{len(rows)} · slots {slots} · errors {len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
