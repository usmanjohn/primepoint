"""
Bulk-import vocabulary-bank entries (and their root families) from a Python data file.

The data file exposes a ``TRACK`` dict, an optional ``ROOTS`` list and a ``WORDS``
list, e.g.::

    TRACK = {"name": "TOPIK", "icon": "bi-flag", "color": "#3b82f6"}

    ROOTS = [
        {
            "syllable": "출",
            "hanja":    "出",
            "meaning":  "chiqmoq — chiqish, tashqariga",
            "note":     "<p>Deyarli doim 'ichkaridan tashqariga' harakati.</p>",
            "order":    100,
        },
    ]

    WORDS = [
        {
            "word":        "출구",
            "hanja":       "出口",
            "roots":       ["출"],          # by syllable; "경(境)" when ambiguous
            "pos":         "noun",          # see VOCAB_POS_CHOICES
            "topic":       "place",         # see VOCAB_TOPIC_CHOICES
            "level":       2,
            "freq":        3,
            "meaning":     "chiqish joyi, chiqaverish",
            "collocation": "출구를 찾다 · 비상 출구",
            "note":        "<p>Teskarisi 입구 (kirish).</p>",
            "examples":    [("비상 출구는 어디에 있습니까?", "Favqulodda chiqish qayerda?")],
            "synonyms":    [],
            "antonyms":    [("입구", "kirish joyi — 出↔入")],
            "related":     [("출입", "kirish-chiqish")],
        },
    ]

``roots`` names are matched against ``ROOTS`` in the same file **or** roots already
in the database, so a later file can hang new words off an existing family. Where two
roots share a syllable (경(經) "iqtisod" vs 경(境) "chegara"), name the one you mean as
``"경(境)"`` — the bare syllable is rejected as ambiguous rather than guessed at.
``synonyms`` / ``antonyms`` / ``related`` are ``(word, note)`` tuples; a note that
names a word which is itself in the bank is cross-linked automatically, in a second
pass over the whole track (so file A can point at a word imported later in file B).

Existing words are matched by ``(track, word)``. Without ``--republish`` they are
left alone; with it, the word is updated and its examples, roots and relations are
rebuilt from the file.

Usage::

    python manage.py import_vocab examprep/management/commands/_vocab_topik_roots.py --author=prime
    python manage.py import_vocab <file> --author=prime --republish
"""

import importlib.util
import os

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.db import transaction

from examprep.models import (ExamTrack, VocabRoot, VocabEntry, VocabExample,
                             VocabRelation, VOCAB_POS_CHOICES, VOCAB_TOPIC_CHOICES)

VALID_POS = {p for p, _l in VOCAB_POS_CHOICES}
VALID_TOPICS = {t for t, _l in VOCAB_TOPIC_CHOICES}

# (data-file key, VocabRelation.kind)
RELATION_KEYS = [('synonyms', 'syn'), ('antonyms', 'ant'), ('related', 'rel')]


class Command(BaseCommand):
    help = "Bulk-create vocabulary entries and root families from a Python data file."

    def add_arguments(self, parser):
        parser.add_argument("datafile",
                            help="Path to a Python file exposing TRACK, optional ROOTS, and WORDS.")
        parser.add_argument("--author", required=False,
                            help="Username to attribute the import to (optional — vocab entries "
                                 "have no author field; accepted so the command matches the others).")
        parser.add_argument("--republish", action="store_true",
                            help="Update words that already exist, rebuilding their examples, "
                                 "roots and relations (default: skip them).")

    # ── helpers ─────────────────────────────────────────────────────────────

    def _load_module(self, path):
        if not os.path.exists(path):
            raise CommandError(f"Data file not found: {path}")
        spec = importlib.util.spec_from_file_location("_vocab_data", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for attr in ("TRACK", "WORDS"):
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

    def _sync_roots(self, track, roots_spec, republish):
        """Create or update the file's roots.

        Returns ``(index, ambiguous)`` — a lookup of every root in the track by
        syllable and by "syllable(hanja)", plus the set of syllables claimed by
        more than one root.
        """
        created_n = updated_n = 0
        for i, data in enumerate(roots_spec or []):
            syllable = (data.get("syllable") or "").strip()
            if not syllable:
                raise CommandError(f"ROOTS[{i}]: 'syllable' is required.")
            if not (data.get("meaning") or "").strip():
                raise CommandError(f"ROOTS[{i}] ({syllable}): 'meaning' is required.")
            fields = {
                "hanja":        data.get("hanja", ""),
                "meaning":      data["meaning"].strip(),
                "note":         data.get("note", ""),
                "order":        data.get("order", i),
                "is_published": data.get("is_published", True),
            }
            root = VocabRoot.objects.filter(track=track, syllable=syllable,
                                            hanja=fields["hanja"]).first()
            if root is None:
                VocabRoot.objects.create(track=track, syllable=syllable, **fields)
                created_n += 1
            elif republish:
                for key, value in fields.items():
                    setattr(root, key, value)
                root.save()
                updated_n += 1
        if created_n or updated_n:
            self.stdout.write(f"  roots: {created_n} created, {updated_n} updated")

        # Index every root in the track, not just this file's — a later file
        # can attach words to a family defined in an earlier one.
        #
        # Homophone roots are the reason this is not a plain {syllable: root}
        # dict: 경(經) "iqtisod" and 경(境) "chegara" are different families
        # that share a syllable, and so are 소(所)/소(消) and 정(定)/정(政).
        # A word may therefore name a root either as "경" (only when that is
        # unambiguous) or as "경(境)".
        index, ambiguous = {}, set()
        for root in track.vocab_roots.all():
            if root.hanja:
                index[f'{root.syllable}({root.hanja})'] = root
            if root.syllable in index:
                ambiguous.add(root.syllable)
            index[root.syllable] = root
        return index, ambiguous

    def _validate(self, data, index):
        where = f"WORDS[{index}] ({data.get('word', '?')})"
        if not (data.get("word") or "").strip():
            raise CommandError(f"{where}: 'word' is required.")
        if not (data.get("meaning") or "").strip():
            raise CommandError(f"{where}: 'meaning' is required.")
        pos = data.get("pos", "noun")
        if pos not in VALID_POS:
            raise CommandError(f"{where}: unknown pos '{pos}'. Valid: {', '.join(sorted(VALID_POS))}")
        topic = data.get("topic", "daily")
        if topic not in VALID_TOPICS:
            raise CommandError(f"{where}: unknown topic '{topic}'. "
                               f"Valid: {', '.join(sorted(VALID_TOPICS))}")
        level = int(data.get("level", 3))
        if not 1 <= level <= 6:
            raise CommandError(f"{where}: level must be 1–6, got {level}.")
        return pos, topic, level

    def _write_children(self, entry, data, root_index, ambiguous, index):
        """Rebuild examples, root links and relations — all derived from the file."""
        entry.examples.all().delete()
        VocabExample.objects.bulk_create([
            VocabExample(entry=entry, korean=ko, uz=uz, order=i)
            for i, (ko, uz) in enumerate(data.get("examples", []))
        ])

        roots = []
        for name in data.get("roots", []):
            # Loud, not silent: a typo'd or ambiguous root would quietly drop
            # the word out of the family view, which is the point of the page.
            if name in ambiguous:
                candidates = ', '.join(
                    f"'{key}'" for key in sorted(root_index)
                    if key.startswith(f'{name}(')
                )
                raise CommandError(
                    f"WORDS[{index}] ({data['word']}): root '{name}' is ambiguous — "
                    f"several roots share that syllable. Name one of: {candidates}.")
            root = root_index.get(name)
            if root is None:
                raise CommandError(
                    f"WORDS[{index}] ({data['word']}): root '{name}' is not defined "
                    f"in ROOTS or in the database.")
            roots.append(root)
        entry.roots.set(roots)

        entry.relations.all().delete()
        rows, order = [], 0
        for key, kind in RELATION_KEYS:
            for word, note in data.get(key, []):
                rows.append(VocabRelation(entry=entry, kind=kind, word=word,
                                          note=note, order=order))
                order += 1
        VocabRelation.objects.bulk_create(rows)

    def _link_relations(self, track):
        """Second pass: point each relation row at the real entry it names."""
        by_word = {}
        for e in track.vocab_entries.all():
            by_word.setdefault(e.word.strip(), e)

        linked = 0
        rows = (VocabRelation.objects.filter(entry__track=track)
                .select_related('entry'))
        for row in rows:
            target = by_word.get(row.word.strip())
            # Never link a word to itself.
            if target and target.id == row.entry_id:
                target = None
            if row.related_id != (target.id if target else None):
                row.related = target
                row.save(update_fields=['related'])
            if target:
                linked += 1
        return linked

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
        root_index, ambiguous = self._sync_roots(track, getattr(module, "ROOTS", []), republish)

        self.stdout.write(f"Importing {len(module.WORDS)} words into '{track.name}'…")
        created_n = updated_n = skipped_n = 0
        for i, data in enumerate(module.WORDS):
            pos, topic, level = self._validate(data, i)
            word = data["word"].strip()

            fields = {
                "hanja":        data.get("hanja", ""),
                "pos":          pos,
                "topic":        topic,
                "level":        level,
                "meaning":      data["meaning"].strip(),
                "note":         data.get("note", ""),
                "collocation":  data.get("collocation", ""),
                "freq":         max(1, min(3, int(data.get("freq", 2)))),
                "order":        data.get("order", i),
                "is_published": data.get("is_published", True),
            }

            entry = VocabEntry.objects.filter(track=track, word=word).first()
            if entry is None:
                entry = VocabEntry.objects.create(track=track, word=word, **fields)
                self._write_children(entry, data, root_index, ambiguous, i)
                created_n += 1
            elif republish:
                for key, value in fields.items():
                    setattr(entry, key, value)
                entry.save()
                self._write_children(entry, data, root_index, ambiguous, i)
                updated_n += 1
            else:
                skipped_n += 1

        linked = self._link_relations(track)

        self.stdout.write(self.style.SUCCESS(
            f"Done: {created_n} created, {updated_n} updated, {skipped_n} skipped. "
            f"{linked} relation cross-links resolved. "
            f"Track now holds {track.vocab_entries.count()} words in "
            f"{track.vocab_roots.count()} root families."
        ))
