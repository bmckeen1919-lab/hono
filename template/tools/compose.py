"""Compose surface forms for a frozen model, and gloss them back.

Run-time helper for hand translation; import it in a translation script::

    from template.tools.compose import Composer
    c = Composer(r"out\\veshtari.json")
    sentence = [c.noun("sun", "ABS"), c.verb("rise", ("PST", "PROG")),
                c.root("above"), c.root("ocean")]
    " ".join(sentence)     # -> surface words
    c.gloss(sentence)      # -> interlinear gloss

A sentence is a list of tokens. ``noun`` marks core case; ``verb`` applies
tense/aspect (from the model) plus 3SG agreement; ``root`` is a bare word;
``ordinal`` is "first". Join clauses with a conjunction root, or juxtapose them.
"""

from __future__ import annotations

import pathlib

from conlang.model import Language
from conlang.morphology.generate import inflect_form


class Composer:
    def __init__(self, model_path: str | pathlib.Path) -> None:
        self.lang = Language.model_validate_json(pathlib.Path(model_path).read_text(encoding="utf-8"))
        self.by = {lex.gloss: lex for lex in self.lang.lexemes}
        self.by_id = {lex.id: lex for lex in self.lang.lexemes}
        self._agree = next(
            (a.form for a in self.lang.affixes if a.gloss == "3SG" and "verb" in a.applies_to),
            "",
        )
        # reverse maps for glossing
        self._rootmap = {lex.root: lex.gloss for lex in self.lang.lexemes}
        self._wordforms = {
            w.form: (self.by_id[w.lexeme_id].gloss, list(w.tags))
            for w in self.lang.words
            if w.tags != ["CIT"]
        }
        self._case = {
            "se": "ERG", "ser": "ERG", "pe": "ERG", "ke": "ERG",
            "wiw": "ABS", "pon": "ABS", "lum": "ABS", "ti": "ABS",
        }

    def root(self, gloss: str) -> str:
        return self.by[gloss].root

    def noun(self, gloss: str, case: str) -> str:
        return inflect_form(
            self.by[gloss], case, self.lang.affixes, self.lang.inventory, self.lang.syllable_templates
        )

    def verb(self, gloss: str, tags: tuple[str, ...] = (), agreement: bool = True) -> str:
        lex = self.by[gloss]
        if tags:
            base = next(
                w.form for w in self.lang.words if w.lexeme_id == lex.id and set(w.tags) == set(tags)
            )
        else:
            base = lex.root
        return base + (self._agree if agreement else "")

    def ordinal(self) -> str:
        return inflect_form(
            self.by["one"], "ORD", self.lang.affixes, self.lang.inventory, self.lang.syllable_templates
        )

    def gloss_token(self, token: str) -> str:
        tags: list[str] = []
        t = token
        if self._agree and t.endswith(self._agree) and (
            t[: -len(self._agree)] in self._wordforms or t[: -len(self._agree)] in self._rootmap
        ):
            t = t[: -len(self._agree)]
            tags.append("3SG")
        if t in self._wordforms:
            gloss, tg = self._wordforms[t]
            return ".".join([gloss, *tg, *tags])
        if t in self._rootmap:
            return ".".join([self._rootmap[t], *tags]) if tags else self._rootmap[t]
        for suffix, case in self._case.items():
            if t.endswith(suffix) and t[: -len(suffix)] in self._rootmap:
                return ".".join([self._rootmap[t[: -len(suffix)]], case, *tags])
        return "?"

    def gloss(self, sentence: list[str]) -> str:
        return " ".join(self.gloss_token(token) for token in sentence)
