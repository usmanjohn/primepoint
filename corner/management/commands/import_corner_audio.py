"""
Bulk-attach narration audio to Corner stories.

Point this at a folder of audio files named by the story's ``order`` number within a
collection — the leading number in each filename decides which story it belongs to::

    1.mp3            -> story with order 1
    01.mp3           -> story with order 1
    1_음식.mp3        -> story with order 1
    14 - 춤을 추는 아이.m4a -> story with order 14

Audio is optional and decoupled from the story text data files (``_stories_*.py``); this
command only fills the ``Story.audio`` field. Files are stored via the project's configured
storage (local ``MEDIA_ROOT`` in dev, the Railway bucket in production) — no code difference.

Usage::

    python manage.py import_corner_audio path/to/folder --collection="Keimyung Short Readings"
    python manage.py import_corner_audio path/to/folder --collection="Keimyung Short Readings" --republish
"""

import os
import re

from django.core.files import File
from django.core.management.base import BaseCommand, CommandError

from corner.models import Collection, Story


AUDIO_EXTS = {".mp3", ".m4a", ".ogg", ".wav", ".aac"}
_LEADING_NUM_RE = re.compile(r"^\s*0*(\d+)")


class Command(BaseCommand):
    help = ("Attach audio files (named by story order) from a folder to the stories of a "
            "Corner collection.")

    def add_arguments(self, parser):
        parser.add_argument(
            "folder",
            help="Directory containing audio files named by the story's order number.",
        )
        parser.add_argument(
            "--collection",
            required=True,
            help="Exact title of the Collection whose stories to attach audio to.",
        )
        parser.add_argument(
            "--republish",
            action="store_true",
            help="Replace audio on stories that already have some (default: skip them).",
        )

    def handle(self, *args, **options):
        folder = options["folder"]
        if not os.path.isdir(folder):
            raise CommandError(f"Folder not found: {folder}")

        try:
            collection = Collection.objects.get(title=options["collection"])
        except Collection.DoesNotExist:
            raise CommandError(f"Collection '{options['collection']}' not found.")
        except Collection.MultipleObjectsReturned:
            raise CommandError(
                f"More than one collection is titled '{options['collection']}'. "
                f"Rename one so the title is unique."
            )

        # order -> Story, for quick lookup.
        stories = {s.order: s for s in collection.stories.all()}
        republish = options["republish"]

        attached = replaced = skipped = unmatched = 0

        for name in sorted(os.listdir(folder)):
            path = os.path.join(folder, name)
            if not os.path.isfile(path):
                continue
            ext = os.path.splitext(name)[1].lower()
            if ext not in AUDIO_EXTS:
                continue

            m = _LEADING_NUM_RE.match(name)
            if not m:
                self.stdout.write(self.style.WARNING(
                    f"skip (no leading order number): {name}"))
                unmatched += 1
                continue
            order = int(m.group(1))

            story = stories.get(order)
            if story is None:
                self.stdout.write(self.style.WARNING(
                    f"skip (no story with order {order} in '{collection.title}'): {name}"))
                unmatched += 1
                continue

            had_audio = bool(story.audio)
            if had_audio and not republish:
                skipped += 1
                self.stdout.write(self.style.WARNING(
                    f"[{order}] already has audio, skipped (use --republish): {story.title}"))
                continue

            # Store under a clean, order-based name so re-runs overwrite predictably.
            stored_name = f"{collection.slug}-{order}{ext}"
            with open(path, "rb") as fh:
                story.audio.save(stored_name, File(fh), save=True)

            if had_audio:
                replaced += 1
                verb = "replaced"
            else:
                attached += 1
                verb = "attached"
            self.stdout.write(self.style.SUCCESS(f"[{order}] {verb}: {story.title}  <-  {name}"))

        self.stdout.write(self.style.SUCCESS(
            f"\nDone. {attached} attached, {replaced} replaced, {skipped} skipped, "
            f"{unmatched} unmatched (collection: {collection.title})."
        ))
