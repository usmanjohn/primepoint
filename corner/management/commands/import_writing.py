"""
Bulk-import Corner writing-practice drills from a Python data file.

The data file must expose a ``SUBJECT`` dict and a ``PRACTICES`` list, e.g.::

    SUBJECT = {
        "name":    "Korean",                 # Subject identity (matched by name)
        "summary": "Koreys tili resurslari.",
        "icon":    "bi-translate",
        "color":   "#d97706",
    }

    PRACTICES = [
        {
            "qtype":         "53",           # 51 / 52 / 53 / 54
            "title":         "53-1: 1인 가구 증가",
            "summary":       "Card blurb in Uzbek (optional, <=300 chars).",
            "order":         1,
            "prompt":        "<p>다음을 참고하여 ... 200~300자로 쓰시오.</p>",
            "chart":         '<p class="wp-chart-title">...</p><svg ...>...</svg>',
            "template_body": '<p>... <span class="wp-blank" data-answer="증가"></span> ...</p>',
            "model_answer":  "<p>...full answer with cn-word spans...</p>",
            "tips":          "<ul><li>Uzbek strategy notes...</li></ul>",
        },
        ...
    ]

Template expressions are marked with the same
``<span class="cn-word" data-pos="..." data-tr="uzbek">한국어</span>`` spans stories
use (in ``template_body`` and ``model_answer``); the flashcard word list is rebuilt
from those spans on every save. Blanks in ``template_body`` are
``<span class="wp-blank" data-answer="정답" data-alt="alt1|alt2"></span>``.

Usage::

    python manage.py import_writing path/to/_writing_topik53_1_5.py --author=<username>
    python manage.py import_writing path/to/_writing_topik53_1_5.py --author=<username> --republish
"""

import importlib.util
import os

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.db import transaction

from masters.models import Master
from corner.models import Subject, WritingPractice

VALID_QTYPES = {code for code, _label in WritingPractice.QTYPE_CHOICES}


class Command(BaseCommand):
    help = "Bulk-create Corner writing-practice drills from a Python data file exposing SUBJECT + PRACTICES."

    def add_arguments(self, parser):
        parser.add_argument(
            "datafile",
            help="Path to a Python file exposing a SUBJECT dict and a PRACTICES list.",
        )
        parser.add_argument(
            "--author",
            required=True,
            help="Username of the author (must be staff or an approved Master).",
        )
        parser.add_argument(
            "--republish",
            action="store_true",
            help="Update drills that already exist, rebuilding their word list "
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
                f"so they cannot create writing drills."
            )
        if not master.is_approved:
            raise CommandError(
                f"Master '{username}' is not approved, so they cannot create writing drills."
            )
        return user

    def _load_module(self, datafile):
        if not os.path.isfile(datafile):
            raise CommandError(f"Data file not found: {datafile}")

        spec = importlib.util.spec_from_file_location("_writing_data", datafile)
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

        practices = getattr(module, "PRACTICES", None)
        if not isinstance(practices, list):
            raise CommandError(
                f"'{datafile}' must define a PRACTICES list "
                f"(found {type(practices).__name__})."
            )
        return subject, practices

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
            for field in ("summary", "icon", "color", "order"):
                if field in subject:
                    setattr(obj, field, subject[field])
            obj.save()
        verb = "created" if created else "exists"
        self.stdout.write(self.style.SUCCESS(f"Subject {verb}: {obj.name}"))
        return obj

    # ── main ────────────────────────────────────────────────────────────────

    def handle(self, *args, **options):
        author = self._resolve_author(options["author"])
        subject_data, practices = self._load_module(options["datafile"])
        republish = options["republish"]

        subject = self._upsert_subject(subject_data)

        created = updated = skipped = 0

        for i, data in enumerate(practices, start=1):
            title = (data.get("title") or "").strip()
            if not title:
                raise CommandError(f"Practice #{i} is missing a 'title'.")

            qtype = str(data.get("qtype") or "53").strip()
            if qtype not in VALID_QTYPES:
                raise CommandError(f"Practice '{title}' has invalid qtype '{qtype}'.")

            model_answer = (data.get("model_answer") or "").strip()
            if not model_answer:
                raise CommandError(f"Practice '{title}' has no 'model_answer'.")

            prompt = (data.get("prompt") or "").strip()
            if not prompt:
                raise CommandError(f"Practice '{title}' has no 'prompt'.")

            fields = {
                "qtype":         qtype,
                "summary":       (data.get("summary") or "")[:300],
                "prompt":        prompt,
                "chart":         (data.get("chart") or "").strip(),
                "template_body": (data.get("template_body") or "").strip(),
                "model_answer":  model_answer,
                "tips":          (data.get("tips") or "").strip(),
                "order":         data.get("order", 0),
                "author":        author,
                "is_published":  True,
            }

            with transaction.atomic():
                practice, was_created = WritingPractice.objects.get_or_create(
                    subject=subject, title=title, defaults=fields,
                )
                if was_created:
                    created += 1
                    self.stdout.write(self.style.SUCCESS(
                        f"[{i}] created: {title} ({practice.words.count()} expressions)"))
                elif republish:
                    for field, value in fields.items():
                        setattr(practice, field, value)
                    practice.save()   # save() re-syncs the word rows
                    updated += 1
                    self.stdout.write(self.style.SUCCESS(
                        f"[{i}] updated: {title} ({practice.words.count()} expressions)"))
                else:
                    skipped += 1
                    self.stdout.write(self.style.WARNING(
                        f"[{i}] exists, skipped (use --republish to update): {title}"
                    ))

        self.stdout.write(self.style.SUCCESS(
            f"\nDone. {created} created, {updated} updated, {skipped} skipped "
            f"(subject: {subject.name}, author: {author.username})."
        ))
