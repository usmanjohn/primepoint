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
            # "stories":   ["Story title", 34],     # Corner readings, titles or ids
            # "playlist":  "My Playlist",           # overrides the file-level PLAYLIST
            # "order":     1,                       # position inside the playlist
        },
        ...
    ]

The file may ALSO expose an optional ``PLAYLIST`` dict.  When present, the
playlist is created for the author if it does not exist yet, and every tutorial
in the file is added to it (at its ``order``), so a fresh database — e.g.
production on Railway — ends up with the same playlist as local dev::

    PLAYLIST = {
        "title":       "Prime English",
        "category":    "english",
        "description": "Short blurb for the playlist card.",
    }

Usage::

    python manage.py import_tutorials path/to/_tutorials_korean.py --author=<username>
    python manage.py import_tutorials path/to/_tutorials_korean.py --author=<username> --republish
"""

import importlib.util
import os

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.db import transaction

from corner.models import Story
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

        playlist_meta = getattr(module, "PLAYLIST", None)
        if playlist_meta is not None and not isinstance(playlist_meta, dict):
            raise CommandError(
                f"'{datafile}' defines PLAYLIST but it is not a dict "
                f"(found {type(playlist_meta).__name__})."
            )
        return tutorials, playlist_meta

    def _ensure_playlist(self, meta, author):
        """Create (or refresh) the file-level playlist. Returns its title or None."""
        title = (meta.get("title") or "").strip()
        if not title:
            raise CommandError("PLAYLIST is missing a 'title'.")

        playlist, was_created = TutorialPlaylist.objects.get_or_create(
            title=title,
            author=author,
            defaults={
                "category":    meta.get("category", "other"),
                "description": (meta.get("description") or "")[:300],
                "is_published": True,
            },
        )
        if was_created:
            self.stdout.write(self.style.SUCCESS(f"playlist created: {title}"))
        else:
            self.stdout.write(f"playlist exists: {title}")
        return playlist.title

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

    def _link_stories(self, tut, refs, author):
        """Attach Corner stories by title or id. Unknown refs are warned about, not
        fatal — the reading is usually imported after the tutorial, so a first pass
        may legitimately find nothing."""
        matched = []
        for ref in refs:
            if isinstance(ref, int):
                qs = Story.objects.filter(pk=ref)
            else:
                qs = Story.objects.filter(title=ref)
            story = qs.first()
            if story:
                matched.append(story)
            else:
                self.stdout.write(self.style.WARNING(f"    story not found: {ref!r}"))
        tut.stories.set(matched)

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
        tutorials, playlist_meta = self._load_tutorials(options["datafile"])
        republish = options["republish"]

        default_playlist = None
        if playlist_meta:
            default_playlist = self._ensure_playlist(playlist_meta, author)

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

                if (was_created or republish) and data.get("practices"):
                    self._link_practices(tut, data["practices"], author)

                if (was_created or republish) and data.get("stories"):
                    self._link_stories(tut, data["stories"], author)

                # Playlist membership is re-applied even for skipped tutorials, so a
                # re-run always leaves the playlist complete and correctly ordered.
                playlist_title = data.get("playlist") or default_playlist
                if playlist_title:
                    self._assign_playlist(tut, playlist_title, data.get("order"), author)

        self.stdout.write(self.style.SUCCESS(
            f"\nDone. {created} created, {updated} updated, {skipped} skipped "
            f"(author: {author.username})."
        ))
