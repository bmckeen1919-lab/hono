"""Render a translation's optional extras from the model.

Run with the toolkit interpreter::

    python template/tools/build_extras.py --csv the_quiet_morning_kesh.csv --model out\\kesh.json

Writes, next to the CSV:

- ``<stem>_gloss.csv`` — the parallel text with an auto-derived interlinear gloss
- ``<stem>.docx`` — the parallel text (English / language / gloss) as OOXML
- ``<out-dir>/reference/<id>-deck.html`` — a flippable recall deck of the lexicon
"""

from __future__ import annotations

import argparse
import csv
import json
import pathlib
import sys
import zipfile
from html import escape

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from template.tools.compose import Composer  # noqa: E402

from conlang.phonology.romanize import romanize  # noqa: E402


def _para(text: str, bold: bool = False) -> str:
    rpr = "<w:rPr><w:b/></w:rPr>" if bold else ""
    return f'<w:p><w:r>{rpr}<w:t xml:space="preserve">{escape(text)}</w:t></w:r></w:p>'


def _docx(path: pathlib.Path, title: str, rows: list[dict], column: str, romanizes: bool) -> None:
    body = [_para(title, bold=True)]
    for row in rows:
        body.append(_para(f"{row['index']}. {row['english']}"))
        if romanizes:
            body.append(_para(f"   {row['romanization']}"))
        body.append(_para(f"   {row[column]}"))
        body.append(_para(f"   {row['gloss']}"))
    document = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        f"<w:body>{''.join(body)}<w:sectPr/></w:body></w:document>"
    )
    content_types = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/word/document.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        "</Types>"
    )
    rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" '
        'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
        'Target="word/document.xml"/></Relationships>'
    )
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", rels)
        z.writestr("word/document.xml", document)


def _deck(path: pathlib.Path, language, lang_id: str) -> int:
    cards = sorted(language.lexemes, key=lambda x: (x.pos, x.gloss))
    romanizes = bool(language.inventory.orthography)

    def _card(card) -> list[str]:
        if not romanizes:
            return [card.gloss, card.root, card.pos]
        spelling = romanize(card.root, language.inventory, language.inventory.orthography)
        return [card.gloss, card.root, card.pos, spelling]

    html = (
        "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
        f"<title>{lang_id} recall deck</title><style>"
        "body{font-family:Georgia,serif;background:#fdfcf9;color:#1a1a1a;max-width:40rem;margin:0 auto;padding:2rem}"
        "h1{font-weight:normal}.card{border:1px solid #d8d4cc;border-radius:8px;padding:2rem;text-align:center;min-height:8rem;"
        "display:flex;flex-direction:column;justify-content:center;cursor:pointer;background:#fff}"
        ".front{font-size:1.6rem}.back{font-size:1.3rem;color:#7a3e2e;margin-top:1rem;display:none}"
        ".back.show{display:block}button{font:inherit;margin:0 .3rem;padding:.4rem .9rem;border:1px solid #d8d4cc;"
        "border-radius:6px;background:#f3ece7;cursor:pointer}.bar{text-align:center;margin:1rem 0}small{color:#5c5c5c}"
        "</style></head><body>"
        f"<h1>{lang_id} recall deck</h1>"
        f"<p><small>Click the card to flip; arrows to move; shuffle to randomise. {len(cards)} lexemes.</small></p>"
        "<div class='bar'><button onclick='prev()'>←</button><span id='pos'></span>"
        "<button onclick='next()'>→</button><button onclick='shuffle()'>shuffle</button></div>"
        "<div class='card' id='card' onclick='flip()'>"
        "<div class='front' id='front'></div><div class='back' id='back'></div></div>"
        "<script>const cards="
        + json.dumps([_card(c) for c in cards])
        + ";let i=0;const f=document.getElementById('front'),b=document.getElementById('back'),p=document.getElementById('pos');"
        "function show(){f.textContent=cards[i][0];"
        "b.textContent=(cards[i].length>3?cards[i][3]+'  ['+cards[i][1]+']':cards[i][1])+'  ('+cards[i][2]+')';"
        "b.classList.remove('show');p.textContent=(i+1)+' / '+cards.length;}"
        "function flip(){b.classList.toggle('show');}function next(){i=(i+1)%cards.length;show();}"
        "function prev(){i=(i-1+cards.length)%cards.length;show();}"
        "function shuffle(){cards.sort(()=>Math.random()-0.5);i=0;show();}show();</script></body></html>"
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    return len(cards)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--column", default="hono", help="the language column (default: hono)")
    parser.add_argument("--out-dir", default=None, help="default: the CSV's directory")
    parser.add_argument("--deck", default=None, help="deck path (default <out-dir>/reference/<id>-deck.html)")
    args = parser.parse_args()

    composer = Composer(args.model)
    language = composer.lang
    romanizes = bool(language.inventory.orthography)
    csv_path = pathlib.Path(args.csv)
    out_dir = pathlib.Path(args.out_dir) if args.out_dir else csv_path.parent
    with csv_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    def _romanize(surface: str) -> str:
        inventory = language.inventory
        return " ".join(romanize(t, inventory, inventory.orthography) for t in surface.split())

    glossed: list[dict] = []
    for row in rows:
        surface = row.get(args.column) or ""
        entry = {**row, "gloss": composer.gloss(surface.split())}
        if romanizes:
            entry["romanization"] = _romanize(surface)
        glossed.append(entry)

    fieldnames = ["index", "english", args.column]
    if romanizes:
        fieldnames.append("romanization")
    fieldnames.append("gloss")
    gloss_path = out_dir / f"{csv_path.stem}_gloss.csv"
    with gloss_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(glossed)

    docx_path = out_dir / f"{csv_path.stem}.docx"
    _docx(docx_path, f"{language.id}", glossed, args.column, romanizes)

    deck_path = (
        pathlib.Path(args.deck)
        if args.deck
        else out_dir / "reference" / f"{composer.lang.id}-deck.html"
    )
    cards = _deck(deck_path, composer.lang, composer.lang.id)

    print(f"gloss CSV: {gloss_path}")
    print(f"docx:      {docx_path}")
    print(f"deck:      {deck_path} ({cards} cards)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
