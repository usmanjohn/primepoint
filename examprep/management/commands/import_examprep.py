"""
Bulk-import examprep lessons from a Python data file.

The data file must expose a ``TRACK`` dict and a ``LESSONS`` list, e.g.::

    TRACK = {
        "name":    "TOPIK",                      # ExamTrack identity (matched by name)
        "summary": "Korean proficiency exam prep.",
        "icon":    "bi-flag",                    # Bootstrap-icons class
        "color":   "#6366f1",
    }

    LESSONS = [
        {
            "skill":   "reading",                # one of SKILL_CHOICES
            "title":   "TOPIK Reading 1: Skimming for the Main Idea",
            "summary": "Short card blurb (optional, <=300 chars).",
            "order":   1,                        # position within track+skill
            "blocks": [
                # A plain explanation block:
                {"rich_text": "<h2>...</h2><p>...</p>"},
                # An image block (image path is relative to MEDIA_ROOT):
                {"image": "examprep/blocks/passage1.png", "caption": "Sample passage"},
                # An inline practice question (rich_text = prompt, choices => MCQ):
                {
                    "rich_text":   "<p>What is the main idea?</p>",
                    "choices": [
                        {"text": "Option A", "is_correct": False},
                        {"text": "Option B", "is_correct": True},
                    ],
                    "explanation": "<p>Shown after the student answers.</p>",
                },
            ],
        },
        ...
    ]

Usage::

    python manage.py import_examprep path/to/_lessons_topik_reading.py --author=<username>
    python manage.py import_examprep path/to/_lessons_topik_reading.py --author=<username> --republish
"""

import importlib.util
import os

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.db import transaction

from masters.models import Master
from examprep.models import (
    ExamTrack,
    Lesson,
    LessonBlock,
    BlockChoice,
    SKILL_CHOICES,
)

VALID_SKILLS = {code for code, _label in SKILL_CHOICES}


class Command(BaseCommand):
    help = "Bulk-create examprep lessons from a Python data file exposing TRACK + LESSONS."

    def add_arguments(self, parser):
        parser.add_argument(
            "datafile",
            help="Path to a Python file exposing a TRACK dict and a LESSONS list.",
        )
        parser.add_argument(
            "--author",
            required=True,
            help="Username of the author (must be staff or an approved Master).",
        )
        parser.add_argument(
            "--republish",
            action="store_true",
            help="Update lessons that already exist, rebuilding their blocks "
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
                f"so they cannot create lessons."
            )
        if not master.is_approved:
            raise CommandError(
                f"Master '{username}' is not approved, so they cannot create lessons."
            )
        return user

    def _load_module(self, datafile):
        if not os.path.isfile(datafile):
            raise CommandError(f"Data file not found: {datafile}")

        spec = importlib.util.spec_from_file_location("_examprep_data", datafile)
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
        except Exception as exc:  # noqa: BLE001 - surface the real error to the user
            raise CommandError(f"Failed to import '{datafile}': {exc}")

        track = getattr(module, "TRACK", None)
        if not isinstance(track, dict) or not track.get("name"):
            raise CommandError(
                f"'{datafile}' must define a TRACK dict with at least a 'name'."
            )

        lessons = getattr(module, "LESSONS", None)
        if not isinstance(lessons, list):
            raise CommandError(
                f"'{datafile}' must define a LESSONS list "
                f"(found {type(lessons).__name__})."
            )
        return track, lessons

    def _upsert_track(self, track):
        """Get or create the ExamTrack, refreshing its presentation metadata."""
        obj, created = ExamTrack.objects.get_or_create(
            name=track["name"],
            defaults={
                "summary": track.get("summary", ""),
                "icon":    track.get("icon", "bi-mortarboard"),
                "color":   track.get("color", "#6366f1"),
                "order":   track.get("order", 0),
                "is_published": True,
            },
        )
        if not created:
            # Keep card metadata in sync with the data file on every run.
            for field in ("summary", "icon", "color", "order"):
                if field in track:
                    setattr(obj, field, track[field])
            obj.save()
        verb = "created" if created else "exists"
        self.stdout.write(self.style.SUCCESS(f"Track {verb}: {obj.name}"))
        return obj

    def _build_blocks(self, lesson, blocks):
        """Create LessonBlock + BlockChoice rows for a lesson, in order."""
        for b_order, block in enumerate(blocks, start=1):
            lb = LessonBlock.objects.create(
                lesson=lesson,
                order=block.get("order", b_order),
                image=block.get("image") or None,
                caption=block.get("caption", ""),
                rich_text=block.get("rich_text") or None,
                explanation=block.get("explanation") or None,
            )
            for c_order, choice in enumerate(block.get("choices", []), start=1):
                BlockChoice.objects.create(
                    block=lb,
                    text=choice["text"],
                    is_correct=bool(choice.get("is_correct")),
                    order=choice.get("order", c_order),
                )

    # ── main ────────────────────────────────────────────────────────────────

    def handle(self, *args, **options):
        author = self._resolve_author(options["author"])
        track_data, lessons = self._load_module(options["datafile"])
        republish = options["republish"]

        track = self._upsert_track(track_data)

        created = updated = skipped = 0

        for i, data in enumerate(lessons, start=1):
            title = (data.get("title") or "").strip()
            if not title:
                raise CommandError(f"Lesson #{i} is missing a 'title'.")

            skill = data.get("skill", "reading")
            if skill not in VALID_SKILLS:
                raise CommandError(
                    f"Lesson '{title}' has invalid skill '{skill}'. "
                    f"Valid: {', '.join(sorted(VALID_SKILLS))}."
                )

            blocks = data.get("blocks") or []
            if not blocks:
                raise CommandError(f"Lesson '{title}' has no 'blocks'.")

            summary = (data.get("summary") or "")[:300]
            order = data.get("order", 0)

            with transaction.atomic():
                lesson, was_created = Lesson.objects.get_or_create(
                    track=track,
                    skill=skill,
                    title=title,
                    defaults={
                        "summary": summary,
                        "order": order,
                        "author": author,
                        "is_published": True,
                    },
                )

                if was_created:
                    self._build_blocks(lesson, blocks)
                    created += 1
                    self.stdout.write(self.style.SUCCESS(f"[{i}] created: {title}"))
                elif republish:
                    lesson.summary = summary
                    lesson.order = order
                    lesson.author = author
                    lesson.is_published = True
                    lesson.save()
                    lesson.blocks.all().delete()   # rebuild ordered children cleanly
                    self._build_blocks(lesson, blocks)
                    updated += 1
                    self.stdout.write(self.style.SUCCESS(f"[{i}] updated: {title}"))
                else:
                    skipped += 1
                    self.stdout.write(self.style.WARNING(
                        f"[{i}] exists, skipped (use --republish to update): {title}"
                    ))

        self.stdout.write(self.style.SUCCESS(
            f"\nDone. {created} created, {updated} updated, {skipped} skipped "
            f"(track: {track.name}, author: {author.username})."
        ))
