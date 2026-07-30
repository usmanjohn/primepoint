"""
Bulk-import practice tests from a Python data file.

The data file must expose a ``PRACTICES`` list of dicts, e.g.::

    PRACTICES = [
        {
            "title":       "PE-1 Practice: What Is a Sentence? Subject + Verb",
            "description": "20 savol — ...",
            "tutorial":    "PE-1:",        # optional: links the practice to that tutorial
            "subject":     "English",      # optional, defaults to SUBJECT / "English"
            "level":       "easy",         # easy | medium | hard
            "questions": [
                {
                    "text":        "<p>Choose the correct option.</p><p><strong>...</strong></p>",
                    "choices":     ["a", "b", "c", "d"],
                    "correct":     "b",
                    "explanation": "<p><strong>b</strong> is correct. ... <em>(Uzbek ...)</em></p>",
                    # optional: "hint": "<p>...</p>", "points": 1
                },
                ...
            ],
        },
        ...
    ]

The file may ALSO expose file-level defaults, all optional::

    SUBJECT  = {"name": "English", "description": "...", "color": "#...", "icon": "bi-..."}
    DEFAULTS = {"level": "easy", "pass_score": 60, "max_attempts": 0, "time_limit": None}

The ``tutorial`` key is matched against ``Tutorial.title`` — first an exact match,
then a ``startswith`` match, so ``"PE-1:"`` finds ``"PE-1: What Is a Sentence? …"``
without repeating the whole title.  The practice is *added* to that tutorial's
``practices`` set (never replacing links that are already there), which is what
makes the Practice button show up on the lesson page.

Usage::

    python manage.py import_practices path/to/_practice_pe_1_5.py --master=prime
    python manage.py import_practices path/to/_practice_pe_1_5.py --master=powerty --republish

``--republish`` updates an existing practice (same title + master) and REBUILDS
all of its questions.  Without it, existing practices are skipped.
"""

import importlib.util
import os

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.db import transaction

from masters.models import Master
from practice.models import (
    Subject,
    Practice,
    PracticeQuestion,
    PracticeChoice,
    LEVEL_CHOICES,
)
from tutorial.models import Tutorial

VALID_LEVELS = {code for code, _label in LEVEL_CHOICES}

PRACTICE_DEFAULTS = {
    "level":                "medium",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,       # unlimited
    "show_answers_after":   True,
    "time_limit":           None,
}


class Command(BaseCommand):
    help = "Bulk-create practice tests from a Python data file exposing a PRACTICES list."

    def add_arguments(self, parser):
        parser.add_argument(
            "datafile",
            help="Path to a Python file exposing a PRACTICES list.",
        )
        parser.add_argument(
            "--master",
            required=True,
            help="Username of the master who owns the practices.",
        )
        parser.add_argument(
            "--republish",
            action="store_true",
            help="Update practices that already exist and rebuild their questions.",
        )

    # ── helpers ─────────────────────────────────────────────────────────────

    def _resolve_master(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise CommandError(f"User '{username}' not found.")
        try:
            return Master.objects.get(profile__user=user)
        except Master.DoesNotExist:
            raise CommandError(f"No Master profile found for user '{username}'.")

    def _load_data(self, datafile):
        if not os.path.isfile(datafile):
            raise CommandError(f"Data file not found: {datafile}")

        spec = importlib.util.spec_from_file_location("_practice_data", datafile)
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
        except Exception as exc:  # noqa: BLE001 - surface the real error
            raise CommandError(f"Failed to import '{datafile}': {exc}")

        practices = getattr(module, "PRACTICES", None)
        if not isinstance(practices, list):
            raise CommandError(
                f"'{datafile}' must define a PRACTICES list "
                f"(found {type(practices).__name__})."
            )

        subject_meta = getattr(module, "SUBJECT", None)
        if subject_meta is not None and not isinstance(subject_meta, dict):
            raise CommandError(f"'{datafile}' defines SUBJECT but it is not a dict.")

        defaults = getattr(module, "DEFAULTS", None) or {}
        if not isinstance(defaults, dict):
            raise CommandError(f"'{datafile}' defines DEFAULTS but it is not a dict.")

        return practices, subject_meta, defaults

    def _ensure_subject(self, name, meta):
        subject, created = Subject.objects.get_or_create(
            name=name,
            defaults={
                "description": (meta or {}).get("description", ""),
                "color":       (meta or {}).get("color", "#6366f1"),
                "icon":        (meta or {}).get("icon", "bi-journal-bookmark-fill"),
            },
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"subject created: {name}"))
        return subject

    def _find_tutorial(self, ref):
        """Exact title match first, then a startswith match ('PE-1:')."""
        tut = Tutorial.objects.filter(title=ref).first()
        if tut:
            return tut
        matches = list(Tutorial.objects.filter(title__startswith=ref)[:2])
        if len(matches) == 1:
            return matches[0]
        if len(matches) > 1:
            self.stdout.write(self.style.WARNING(
                f"    tutorial ref {ref!r} is ambiguous ({len(matches)}+ matches) — not linked"
            ))
        return None

    def _validate(self, practice_title, questions):
        if not questions:
            raise CommandError(f"Practice '{practice_title}' has no questions.")
        for n, q in enumerate(questions, start=1):
            where = f"'{practice_title}' Q{n}"
            if not (q.get("text") or "").strip():
                raise CommandError(f"{where} is missing 'text'.")
            choices = q.get("choices") or []
            if len(choices) < 2:
                raise CommandError(f"{where} needs at least 2 choices.")
            if len(set(choices)) != len(choices):
                raise CommandError(f"{where} has duplicate choices: {choices}")
            correct = q.get("correct")
            correct_list = correct if isinstance(correct, (list, tuple)) else [correct]
            for c in correct_list:
                if c not in choices:
                    raise CommandError(
                        f"{where} has correct answer {c!r} which is not among its choices."
                    )
            if not (q.get("explanation") or "").strip():
                raise CommandError(f"{where} is missing 'explanation'.")

    def _build_questions(self, practice, questions, master):
        for i, q in enumerate(questions, start=1):
            question = PracticeQuestion.objects.create(
                practice=practice,
                question_text=q["text"],
                explanation=q["explanation"],
                hint=q.get("hint") or "",
                order=i,
                points=q.get("points", 1),
                made_by=master,
            )
            correct = q["correct"]
            correct_set = set(correct if isinstance(correct, (list, tuple)) else [correct])
            for choice_text in q["choices"]:
                PracticeChoice.objects.create(
                    question=question,
                    text=choice_text,
                    is_correct=choice_text in correct_set,
                )

    # ── main ────────────────────────────────────────────────────────────────

    def handle(self, *args, **options):
        master     = self._resolve_master(options["master"])
        republish  = options["republish"]
        practices, subject_meta, file_defaults = self._load_data(options["datafile"])

        default_subject_name = (subject_meta or {}).get("name", "English")

        created = updated = skipped = 0
        total_questions = 0

        for i, data in enumerate(practices, start=1):
            title = (data.get("title") or "").strip()
            if not title:
                raise CommandError(f"Practice #{i} is missing a 'title'.")

            questions = data.get("questions") or []
            self._validate(title, questions)

            level = data.get("level", file_defaults.get("level", PRACTICE_DEFAULTS["level"]))
            if level not in VALID_LEVELS:
                raise CommandError(
                    f"Practice '{title}' has invalid level '{level}'. "
                    f"Valid: {', '.join(sorted(VALID_LEVELS))}."
                )

            subject = self._ensure_subject(
                data.get("subject", default_subject_name), subject_meta
            )

            fields = dict(PRACTICE_DEFAULTS)
            fields.update({k: v for k, v in file_defaults.items() if k in PRACTICE_DEFAULTS})
            fields.update({
                "description": (data.get("description") or "").strip(),
                "subject":     subject,
                "level":       level,
            })
            for key in ("pass_score", "max_attempts", "time_limit",
                        "is_free", "is_published", "is_available_for_all",
                        "show_answers_after"):
                if key in data:
                    fields[key] = data[key]

            with transaction.atomic():
                practice = Practice.objects.filter(title=title, master=master).first()

                if practice and not republish:
                    self.stdout.write(self.style.WARNING(
                        f"skip   {title} (already exists, id={practice.pk})"
                    ))
                    skipped += 1
                    continue

                if practice:
                    for key, value in fields.items():
                        setattr(practice, key, value)
                    practice.save()
                    practice.questions.all().delete()
                    self._build_questions(practice, questions, master)
                    updated += 1
                    verb = "update"
                else:
                    practice = Practice.objects.create(title=title, master=master, **fields)
                    self._build_questions(practice, questions, master)
                    created += 1
                    verb = "create"

                total_questions += len(questions)

                tut_ref = data.get("tutorial")
                linked = ""
                if tut_ref:
                    tutorial = self._find_tutorial(tut_ref)
                    if tutorial:
                        tutorial.practices.add(practice)
                        linked = f" → {tutorial.title[:40]}"
                    else:
                        self.stdout.write(self.style.WARNING(
                            f"    tutorial not found: {tut_ref!r}"
                        ))

            self.stdout.write(self.style.SUCCESS(
                f"{verb} {title} — {len(questions)} questions (id={practice.pk}){linked}"
            ))

        self.stdout.write(self.style.SUCCESS(
            f"\ndone: {created} created, {updated} updated, {skipped} skipped "
            f"({total_questions} questions written)"
        ))
