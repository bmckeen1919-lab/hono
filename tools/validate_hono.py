"""Validate `the_quiet_morning_hono.csv` against the frozen Hono model.

Run with the toolkit's interpreter (it needs ``conlang``)::

    C:\\Users\\bmcke\\conlang\\.venv\\Scripts\\python.exe tools\\validate_hono.py

Checks: the CSV has the exact shape (header ``index,english,hono``, 111 rows,
index sequence), each English cell is present, and every Hono token is
phonotactically legal under Hono's inventory and constraints. A ``[slot]`` cell
is accepted as a quarantined item; an **empty** Hono cell is reported as
*untranslated*, not as an error, so the file validates as translation proceeds.

Gloss → root consistency is a *reading* check (the lexicon is arbitrary, so the
gloss is the anchor) and is not automated here.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

from conlang.model import Language
from conlang.phonology.syllable import is_legal_word

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "the_quiet_morning_hono.csv"
MODEL_PATH = ROOT / "out" / "hono.json"
EXPECTED_ROWS = 111
STRIP = " \t.,;:!?\"'()[]"


def main() -> int:
    language = Language.model_validate_json(MODEL_PATH.read_text(encoding="utf-8"))
    with CSV_PATH.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    errors: list[str] = []
    if rows and list(rows[0].keys()) != ["index", "english", "hono"]:
        errors.append(f"header is {list(rows[0].keys())!r}, expected ['index','english','hono']")
    if len(rows) != EXPECTED_ROWS:
        errors.append(f"expected {EXPECTED_ROWS} rows, found {len(rows)}")

    translated = 0
    slots = 0
    for position, row in enumerate(rows, start=1):
        index = (row.get("index") or "").strip()
        english = (row.get("english") or "").strip()
        hono = (row.get("hono") or "").strip()
        if index != str(position):
            errors.append(f"row {position}: index {index!r}, expected {position!r}")
        if not english:
            errors.append(f"row {position}: empty english")
        if not hono:
            continue
        if hono == "[slot]":
            slots += 1
            continue
        translated += 1
        for token in hono.split():
            if token.startswith("[") and token.endswith("]"):
                slots += 1  # an inline quarantined item
                continue
            word = token.strip(STRIP)
            if not word:
                continue
            if not is_legal_word(
                word, language.inventory, language.syllable_templates, language.constraints
            ):
                errors.append(f"row {position}: illegal form {word!r}")

    for error in errors[:50]:
        print(error)
    print(f"translated {translated}/{len(rows)} · slots {slots} · errors {len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
