"""
Bulk-import grammar-bank entries from a Python data file.

The data file must expose a ``TRACK`` dict and a ``POINTS`` list, e.g.::

    TRACK = {
        "name":    "TOPIK",                  # ExamTrack identity (matched by name)
        "summary": "Koreys tili imtihoniga tayyorgarlik.",
        "icon":    "bi-translate",
        "color":   "#d97706",
    }

    POINTS = [
        {
            "pattern":   "-(으)니까",
            "category":  "connective",       # see GRAMMAR_CATEGORY_CHOICES
            "function":  "reason",           # see GRAMMAR_FUNCTION_CHOICES
            "level":     2,                  # TOPIK 1-6
            "freq":      3,                  # 1-3 stars
            "register":  "both",
            "meaning":   "sabab — chunki, shuning uchun",
            "attach":    "동사/형용사 + -(으)니까",
            "form_rule": "받침 yo'q → -니까, 받침 bor → -으니까",
            "note":      "<p>Buyruq va taklif bilan ishlatiladi.</p>",
            "mistake":   "<p>❌ 늦어서 미안합니다 o'rniga 늦으니까 ...</p>",
            "examples":  [
                ("배가 아프니까 병원에 갑시다.", "Qornim og'riyapti, shifoxonaga boraylik."),
            ],
            "synonyms":  [
                ("-아서/어서", "sabab, lekin buyruq/taklif bilan ishlatilmaydi"),
            ],
        },
        ...
    ]

``examples`` items are ``(korean, uzbek)`` tuples; ``synonyms`` items are
``(pattern, farqi)`` tuples. Synonym patterns that name another point in the
same track are cross-linked automatically, so the table becomes a web you can
navigate from either side. Because that linking needs every point to exist
first, it runs as a second pass over the whole track once the file is loaded.

Existing points are matched by ``(track, pattern)``. Without ``--republish``
they are left alone; with it, the point is updated and its examples and
synonyms are rebuilt from the file.

Usage::

    python manage.py import_grammar examprep/management/commands/_grammar_topik_connectives.py --author=prime
    python manage.py import_grammar <file> --author=prime --republish
"""

import importlib.util
import os

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.db import transaction

from examprep.models import (ExamTrack, GrammarPoint, GrammarExample, GrammarSynonym,
                             GRAMMAR_CATEGORY_CHOICES, GRAMMAR_FUNCTION_CHOICES,
                             GRAMMAR_REGISTER_CHOICES)

VALID_CATEGORIES = {c for c, _l in GRAMMAR_CATEGORY_CHOICES}
VALID_FUNCTIONS = {f for f, _l in GRAMMAR_FUNCTION_CHOICES}
VALID_REGISTERS = {r for r, _l in GRAMMAR_REGISTER_CHOICES}


import itertools
import re

_PAREN_RE = re.compile(r'\(([^)]*)\)')
# Separates whole alternatives: "-고 나서 / -(으)ㄴ 후에", "안 / -지 않다 · 못 …"
_ALT_RE = re.compile(r'\s+/\s+|\s+·\s+')
# A bare slash inside one alternative: "-아야/어야 하다" — the choice is between
# the word chunks either side of it, and whatever follows is shared.
_SLASH_RE = re.compile(r'(\S*?)/(\S*)')


def normalize_pattern(pattern):
    """Loosened form of a pattern: no leading dash, no spaces, no trailing '?'."""
    return (pattern or '').strip().rstrip('?').lstrip('-').replace(' ', '')


def pattern_keys(pattern):
    """Every spelling of `pattern` a writer might plausibly use.

    Grammar patterns are written with two kinds of optional material, and a
    synonym note rarely spells them the same way the point's own `pattern`
    field does:

      * alternatives — "-고 나서 / -(으)ㄴ 후에", "드리다 / 여쭙다 / 뵙다"
      * optional morphemes in parentheses — "-기 위해(서)", "-(으)로 인해(서)"

    So expand both: split on the alternative separators, then for each
    alternative emit one key per combination of keeping / dropping each
    parenthesised group. "-(으)로 인해(서)" yields 로인해, 로인해서, 으로인해,
    으로인해서 — which is enough for the synonym "(으)로 인해" to find it.

    Matching is done as key-set intersection, so both sides get expanded and
    neither has to guess the other's spelling.
    """
    def expand_slashes(text, depth=0):
        """"-아야/어야 하다" → "-아야 하다", "어야 하다" (shared tail kept)."""
        match = _SLASH_RE.search(text)
        if not match or depth >= 3:
            return [text]
        left, right = match.group(1), match.group(2)
        head, tail = text[:match.start()], text[match.end():]
        out = []
        for branch in (left, right):
            out.extend(expand_slashes(f'{head}{branch}{tail}', depth + 1))
        return out

    keys = set()
    for alternative in _ALT_RE.split(pattern or ''):
        for part in expand_slashes(alternative.strip()):
            part = part.strip()
            if not part:
                continue
            groups = _PAREN_RE.findall(part)
            # Bound the expansion: 4 optional groups is already 16 variants, and
            # no real pattern has more.
            for keep in itertools.product([True, False], repeat=min(len(groups), 4)):
                i = iter(keep)
                variant = _PAREN_RE.sub(
                    lambda m: m.group(1) if next(i, True) else '', part)
                key = normalize_pattern(variant)
                # A lone jamo ("ㄴ" left over from "-(으)ㄴ") identifies nothing;
                # a lone syllable ("던") does, so keep those.
                if key and not (len(key) == 1 and not '가' <= key <= '힣'):
                    keys.add(key)
    return keys


class Command(BaseCommand):
    help = "Bulk-create grammar-bank entries from a Python data file exposing TRACK + POINTS."

    def add_arguments(self, parser):
        parser.add_argument(
            "datafile",
            help="Path to a Python file exposing a TRACK dict and a POINTS list.",
        )
        parser.add_argument(
            "--author",
            required=False,
            help="Username to attribute the import to (optional — grammar points "
                 "have no author field; accepted so the command matches the others).",
        )
        parser.add_argument(
            "--republish",
            action="store_true",
            help="Update points that already exist, rebuilding their examples and "
                 "synonyms (default: skip them).",
        )

    # ── helpers ─────────────────────────────────────────────────────────────

    def _load_module(self, path):
        if not os.path.exists(path):
            raise CommandError(f"Data file not found: {path}")
        spec = importlib.util.spec_from_file_location("_grammar_data", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for attr in ("TRACK", "POINTS"):
            if not hasattr(module, attr):
                raise CommandError(f"{path} does not define {attr}.")
        return module

    def _get_track(self, spec):
        name = (spec.get("name") or "").strip()
        if not name:
            raise CommandError("TRACK needs a 'name'.")
        track, created = ExamTrack.objects.get_or_create(
            name=name,
            defaults={
                "summary": spec.get("summary", ""),
                "icon":    spec.get("icon", "bi-mortarboard"),
                "color":   spec.get("color", "#6366f1"),
                "order":   spec.get("order", 0),
            },
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"  + track '{track.name}'"))
        return track

    def _validate(self, data, index):
        """Fail loudly on a bad choice value rather than silently storing junk
        that would quietly vanish from every filter on the page."""
        where = f"POINTS[{index}] ({data.get('pattern', '?')})"
        if not (data.get("pattern") or "").strip():
            raise CommandError(f"{where}: 'pattern' is required.")
        if not (data.get("meaning") or "").strip():
            raise CommandError(f"{where}: 'meaning' is required.")
        category = data.get("category", "expression")
        if category not in VALID_CATEGORIES:
            raise CommandError(f"{where}: unknown category '{category}'. "
                               f"Valid: {', '.join(sorted(VALID_CATEGORIES))}")
        function = data.get("function", "reason")
        if function not in VALID_FUNCTIONS:
            raise CommandError(f"{where}: unknown function '{function}'. "
                               f"Valid: {', '.join(sorted(VALID_FUNCTIONS))}")
        register = data.get("register", "both")
        if register not in VALID_REGISTERS:
            raise CommandError(f"{where}: unknown register '{register}'. "
                               f"Valid: {', '.join(sorted(VALID_REGISTERS))}")
        level = int(data.get("level", 3))
        if not 1 <= level <= 6:
            raise CommandError(f"{where}: level must be 1–6, got {level}.")
        return category, function, register, level

    def _write_children(self, point, data):
        """Rebuild examples + synonyms from the file (they are derived data)."""
        point.examples.all().delete()
        GrammarExample.objects.bulk_create([
            GrammarExample(point=point, korean=ko, uz=uz, order=i)
            for i, (ko, uz) in enumerate(data.get("examples", []))
        ])
        point.synonyms.all().delete()
        GrammarSynonym.objects.bulk_create([
            GrammarSynonym(point=point, pattern=pat, note=note, order=i)
            for i, (pat, note) in enumerate(data.get("synonyms", []))
        ])

    def _link_synonyms(self, track):
        """Second pass: point every synonym row at the real GrammarPoint it
        names, when the bank has one. Runs over the whole track so a synonym
        written in file A can resolve to a point imported later in file B."""
        points = list(track.grammar_points.all())

        # Exact spelling wins; the loosened variant keys are the fallback. A
        # variant key claimed by two different points is dropped rather than
        # guessed at — a wrong cross-link is worse than a missing one.
        exact, variants, ambiguous = {}, {}, set()
        for p in points:
            exact.setdefault(normalize_pattern(p.pattern), p)
            for key in pattern_keys(p.pattern):
                if key in variants and variants[key].id != p.id:
                    ambiguous.add(key)
                variants.setdefault(key, p)
        for key in ambiguous:
            variants.pop(key, None)

        def resolve(text):
            hit = exact.get(normalize_pattern(text))
            if hit:
                return hit
            for key in pattern_keys(text):
                if key in variants:
                    return variants[key]
            return None

        linked, cleared = 0, 0
        rows = GrammarSynonym.objects.filter(point__track=track).select_related('point')
        for row in rows:
            target = resolve(row.pattern)
            # Never link a point to itself — that would render as a link back
            # to the page you are already on.
            if target and target.id == row.point_id:
                target = None
            if row.related_id != (target.id if target else None):
                row.related = target
                row.save(update_fields=['related'])
                linked += 1 if target else 0
                cleared += 0 if target else 1
        return linked, cleared

    # ── main ────────────────────────────────────────────────────────────────

    @transaction.atomic
    def handle(self, *args, **options):
        path = options["datafile"]
        republish = options["republish"]
        module = self._load_module(path)

        author = options.get("author")
        if author and not User.objects.filter(username=author).exists():
            raise CommandError(f"User '{author}' not found.")

        track = self._get_track(module.TRACK)
        self.stdout.write(f"Importing {len(module.POINTS)} grammar points into '{track.name}'…")

        created_n = updated_n = skipped_n = 0
        for i, data in enumerate(module.POINTS):
            category, function, register, level = self._validate(data, i)
            pattern = data["pattern"].strip()

            fields = {
                "category":     category,
                "function":     function,
                "register":     register,
                "level":        level,
                "meaning":      data["meaning"].strip(),
                "reading":      data.get("reading", ""),
                "attach":       data.get("attach", ""),
                "form_rule":    data.get("form_rule", ""),
                "note":         data.get("note", ""),
                "mistake":      data.get("mistake", ""),
                "freq":         max(1, min(3, int(data.get("freq", 2)))),
                "order":        data.get("order", i),
                "is_published": data.get("is_published", True),
            }

            point = GrammarPoint.objects.filter(track=track, pattern=pattern).first()
            if point is None:
                point = GrammarPoint.objects.create(track=track, pattern=pattern, **fields)
                self._write_children(point, data)
                created_n += 1
                self.stdout.write(self.style.SUCCESS(f"  + {pattern}"))
            elif republish:
                for key, value in fields.items():
                    setattr(point, key, value)
                point.save()
                self._write_children(point, data)
                updated_n += 1
                self.stdout.write(f"  ~ {pattern} (updated)")
            else:
                skipped_n += 1
                self.stdout.write(self.style.WARNING(f"  = {pattern} (exists, skipped)"))

        linked, _cleared = self._link_synonyms(track)

        self.stdout.write(self.style.SUCCESS(
            f"Done: {created_n} created, {updated_n} updated, {skipped_n} skipped. "
            f"{linked} synonym cross-links resolved."
        ))
