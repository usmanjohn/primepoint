"""
Bulk-import tutorials from a Python data file.

The data file must expose a ``TUTORIALS`` list of dicts, e.g.::

    TUTORIALS = [
        {
            "title":    "Korean Particles 은/는",
            "category": "korean",          # one of CATEGORY_CHOICES
            "summary":  "Short card blurb (optional, <=300 chars).",
            "content":  "<h2>...</h2><p>...</p>",   # full HTML body
            # optional:
            # "practices": ["Practice title", 12],  # titles or ids
            # "playlist":  "My Playlist",           # must already exist for the author
            # "order":     1,
        },
        ...
    ]

Usage::

    python manage.py import_tutorials path/to/_tutorials_korean.py --author=<username>
    python manage.py import_tutorials path/to/_tutorials_korean.py --author=<username> --republish
"""

import importlib.util
import os

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.db import transaction

from masters.models import Master
from practice.models import Practice
from tutorial.models import (
    Tutorial,
    TutorialPlaylist,
    PlaylistTutorial,
    CATEGORY_CHOICES,
)

VALID_CATEGORIES = {code for code, _label in CATEGORY_CHOICES}


class Command(BaseCommand):
    help = "Bulk-create tutorials from a Python data file exposing a TUTORIALS list."

    def add_arguments(self, parser):
        parser.add_argument(
            "datafile",
            help="Path to a Python file exposing a TUTORIALS list.",
        )
        parser.add_argument(
            "--author",
            required=True,
            help="Username of the author (must be staff or an approved Master).",
        )
        parser.add_argument(
            "--republish",
            action="store_true",
            help="Update content of tutorials that already exist (default: skip them).",
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
                f"so they cannot create tutorials."
            )
        if not master.is_approved:
            raise CommandError(
                f"Master '{username}' is not approved, so they cannot create tutorials."
            )
        return user

    def _load_tutorials(self, datafile):
        if not os.path.isfile(datafile):
            raise CommandError(f"Data file not found: {datafile}")

        spec = importlib.util.spec_from_file_location("_tutorials_data", datafile)
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
        except Exception as exc:  # noqa: BLE001 - surface the real error to the user
            raise CommandError(f"Failed to import '{datafile}': {exc}")

        tutorials = getattr(module, "TUTORIALS", None)
        if not isinstance(tutorials, list):
            raise CommandError(
                f"'{datafile}' must define a TUTORIALS list (found {type(tutorials).__name__})."
            )
        return tutorials

    def _link_practices(self, tut, refs, author):
        """Attach practices by title or id. Unknown refs are warned about, not fatal."""
        matched = []
        for ref in refs:
            if isinstance(ref, int):
                qs = Practice.objects.filter(pk=ref)
            else:
                qs = Practice.objects.filter(title=ref)
            practice = qs.first()
            if practice:
                matched.append(practice)
            else:
                self.stdout.write(self.style.WARNING(f"    practice not found: {ref!r}"))
        tut.practices.set(matched)

    def _assign_playlist(self, tut, title, order, author):
        playlist = TutorialPlaylist.objects.filter(title=title, author=author).first()
        if not playlist:
            self.stdout.write(self.style.WARNING(
                f"    playlist not found for author: {title!r} (skipped)"
            ))
            return
        PlaylistTutorial.objects.filter(tutorial=tut).delete()
        PlaylistTutorial.objects.create(tutorial=tut, playlist=playlist, order=order or 0)

    # ── main ────────────────────────────────────────────────────────────────

    def handle(self, *args, **options):
        author = self._resolve_author(options["author"])
        tutorials = self._load_tutorials(options["datafile"])
        republish = options["republish"]

        created = updated = skipped = 0

        for i, data in enumerate(tutorials, start=1):
            title = (data.get("title") or "").strip()
            if not title:
                raise CommandError(f"Tutorial #{i} is missing a 'title'.")

            content = data.get("content")
            if not content:
                raise CommandError(f"Tutorial '{title}' is missing 'content'.")

            category = data.get("category", "other")
            if category not in VALID_CATEGORIES:
                raise CommandError(
                    f"Tutorial '{title}' has invalid category '{category}'. "
                    f"Valid: {', '.join(sorted(VALID_CATEGORIES))}."
                )

            summary = (data.get("summary") or "")[:300]

            with transaction.atomic():
                tut, was_created = Tutorial.objects.get_or_create(
                    title=title,
                    author=author,
                    defaults={
                        "category": category,
                        "summary": summary,
                        "content": content,
                        "is_published": True,
                    },
                )

                if was_created:
                    created += 1
                    self.stdout.write(self.style.SUCCESS(f"[{i}] created: {title}"))
                elif republish:
                    tut.category = category
                    tut.summary = summary
                    tut.content = content
                    tut.is_published = True
                    tut.save()
                    updated += 1
                    self.stdout.write(self.style.SUCCESS(f"[{i}] updated: {title}"))
                else:
                    skipped += 1
                    self.stdout.write(self.style.WARNING(
                        f"[{i}] exists, skipped (use --republish to update): {title}"
                    ))
                    continue

                if data.get("practices"):
                    self._link_practices(tut, data["practices"], author)
                if data.get("playlist"):
                    self._assign_playlist(tut, data["playlist"], data.get("order"), author)

        self.stdout.write(self.style.SUCCESS(
            f"\nDone. {created} created, {updated} updated, {skipped} skipped "
            f"(author: {author.username})."
        ))
