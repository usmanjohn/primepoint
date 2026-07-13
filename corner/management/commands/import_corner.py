"""
Bulk-import Corner stories from a Python data file.

The data file must expose ``SUBJECT`` and ``COLLECTION`` dicts and a
``STORIES`` list, e.g.::

    SUBJECT = {
        "name":    "Korean",                     # Subject identity (matched by name)
        "summary": "Koreys tili resurslari.",
        "icon":    "bi-translate",               # Bootstrap-icons class
        "color":   "#d97706",
    }

    COLLECTION = {
        "title":       "Keimyung Korean Readings",   # matched by (subject, title)
        "description": "Qisqa hikoyalar toʻplami.",
        "order":       1,
    }

    STORIES = [
        {
            "title":   "첫 만남",
            "summary": "Short card blurb in Uzbek (optional, <=300 chars).",
            "order":   1,
            "body":    '<p>... <span class="cn-word" data-pos="verb" data-tr="uchrashmoq">만나다</span> ...</p>',
            "questions": [                       # optional — 0-3 inference MCQs
                {
                    "text":        "이 글의 중심 생각은 무엇입니까?",
                    "choices":     ["...", "...", "..."],
                    "answer":      1,            # 0-based index of the correct choice
                    "explanation": "Nega toʻgʻri — oʻzbekcha izoh.",
                },
            ],
        },
        ...
    ]

Vocabulary is marked inline in the body as
``<span class="cn-word" data-pos="verb" data-tr="uzbek translation">한국어</span>``
(``data-pos`` is optional: verb / adj / adv, else neutral) — the word list and
flashcards are rebuilt from those spans on every save. Comprehension questions
come from the optional ``questions`` list and are rebuilt on every import.

Usage::

    python manage.py import_corner path/to/_stories_keimyung_1_5.py --author=<username>
    python manage.py import_corner path/to/_stories_keimyung_1_5.py --author=<username> --republish
"""

import importlib.util
import os

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.db import transaction

from masters.models import Master
from corner.models import Subject, Collection, Story


class Command(BaseCommand):
    help = "Bulk-create Corner stories from a Python data file exposing SUBJECT + COLLECTION + STORIES."

    def add_arguments(self, parser):
        parser.add_argument(
            "datafile",
            help="Path to a Python file exposing SUBJECT and COLLECTION dicts and a STORIES list.",
        )
        parser.add_argument(
            "--author",
            required=True,
            help="Username of the author (must be staff or an approved Master).",
        )
        parser.add_argument(
            "--republish",
            action="store_true",
            help="Update stories that already exist, rebuilding their word list "
                 "(default: skip them).",
        )

    # ── helpers ─────────────────────────────────────────────────────────────

    def _resolve_author(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise CommandError(f"User '{username}' not found.")

        if user.is_staff:
            return user

        try:
            master = Master.objects.get(profile__user=user)
        except Master.DoesNotExist:
            raise CommandError(
                f"User '{username}' is not staff and has no Master profile, "
                f"so they cannot create stories."
            )
        if not master.is_approved:
            raise CommandError(
                f"Master '{username}' is not approved, so they cannot create stories."
            )
        return user

    def _load_module(self, datafile):
        if not os.path.isfile(datafile):
            raise CommandError(f"Data file not found: {datafile}")

        spec = importlib.util.spec_from_file_location("_corner_data", datafile)
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
        except Exception as exc:  # noqa: BLE001 - surface the real error to the user
            raise CommandError(f"Failed to import '{datafile}': {exc}")

        subject = getattr(module, "SUBJECT", None)
        if not isinstance(subject, dict) or not subject.get("name"):
            raise CommandError(
                f"'{datafile}' must define a SUBJECT dict with at least a 'name'."
            )

        collection = getattr(module, "COLLECTION", None)
        if not isinstance(collection, dict) or not collection.get("title"):
            raise CommandError(
                f"'{datafile}' must define a COLLECTION dict with at least a 'title'."
            )

        stories = getattr(module, "STORIES", None)
        if not isinstance(stories, list):
            raise CommandError(
                f"'{datafile}' must define a STORIES list "
                f"(found {type(stories).__name__})."
            )
        return subject, collection, stories

    def _upsert_subject(self, subject):
        """Get or create the Subject, refreshing its presentation metadata."""
        obj, created = Subject.objects.get_or_create(
            name=subject["name"],
            defaults={
                "summary": subject.get("summary", ""),
                "icon":    subject.get("icon", "bi-stars"),
                "color":   subject.get("color", "#d97706"),
                "order":   subject.get("order", 0),
                "is_published": True,
            },
        )
        if not created:
            # Keep card metadata in sync with the data file on every run.
            for field in ("summary", "icon", "color", "order"):
                if field in subject:
                    setattr(obj, field, subject[field])
            obj.save()
        verb = "created" if created else "exists"
        self.stdout.write(self.style.SUCCESS(f"Subject {verb}: {obj.name}"))
        return obj

    def _upsert_collection(self, subject, collection):
        obj, created = Collection.objects.get_or_create(
            subject=subject,
            title=collection["title"],
            defaults={
                "description": collection.get("description", ""),
                "order":       collection.get("order", 0),
                "is_published": True,
            },
        )
        if not created:
            for field in ("description", "order"):
                if field in collection:
                    setattr(obj, field, collection[field])
            obj.save()
        verb = "created" if created else "exists"
        self.stdout.write(self.style.SUCCESS(f"Collection {verb}: {obj.title}"))
        return obj

    # ── main ────────────────────────────────────────────────────────────────

    def handle(self, *args, **options):
        author = self._resolve_author(options["author"])
        subject_data, collection_data, stories = self._load_module(options["datafile"])
        republish = options["republish"]

        subject = self._upsert_subject(subject_data)
        collection = self._upsert_collection(subject, collection_data)

        created = updated = skipped = 0

        for i, data in enumerate(stories, start=1):
            title = (data.get("title") or "").strip()
            if not title:
                raise CommandError(f"Story #{i} is missing a 'title'.")

            body = (data.get("body") or "").strip()
            if not body:
                raise CommandError(f"Story '{title}' has no 'body'.")

            summary = (data.get("summary") or "")[:300]
            order = data.get("order", 0)

            with transaction.atomic():
                story, was_created = Story.objects.get_or_create(
                    collection=collection,
                    title=title,
                    defaults={
                        "summary": summary,
                        "body": body,
                        "order": order,
                        "author": author,
                        "is_published": True,
                    },
                )

                if was_created:
                    story.sync_questions(data.get("questions"))
                    created += 1
                    nq = story.questions.count()
                    self.stdout.write(self.style.SUCCESS(f"[{i}] created: {title} ({nq} questions)"))
                elif republish:
                    story.summary = summary
                    story.body = body
                    story.order = order
                    story.author = author
                    story.is_published = True
                    story.save()   # save() re-syncs StoryWord rows from the body
                    story.sync_questions(data.get("questions"))
                    updated += 1
                    nq = story.questions.count()
                    self.stdout.write(self.style.SUCCESS(f"[{i}] updated: {title} ({nq} questions)"))
                else:
                    skipped += 1
                    self.stdout.write(self.style.WARNING(
                        f"[{i}] exists, skipped (use --republish to update): {title}"
                    ))

        self.stdout.write(self.style.SUCCESS(
            f"\nDone. {created} created, {updated} updated, {skipped} skipped "
            f"(collection: {collection.title}, author: {author.username})."
        ))
