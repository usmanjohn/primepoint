"""
Bulk-import Logic Arena puzzles from a Python data file.

The data file exposes an optional ``SCHEDULE`` dict and a ``PUZZLES`` list::

    SCHEDULE = {
        "start":  "2026-07-13 09:00",   # when round 1 opens (project timezone)
        "days":   7,                    # one round per week
        "window": 7,                    # a round stays sealed this many days
    }

    PUZZLES = [
        {
            "number":     1,
            "round":      1,                    # -> opens_at / reveal_at
            "category":   "weighing",
            "difficulty": 2,
            "title":      "The Lighter Coin",
            "title_uz":   "Yengil tanga",
            "teaser":     "Nine coins, one balance, two weighings.",
            "teaser_uz":  "Toʻqqiz tanga, bitta tarozi, ikki urinish.",
            "body":       "<p>…</p>",           # English, inline SVG figures
            "body_uz":    "<p>…</p>",           # Uzbek
            "hint":       "Three is the magic number.",
            "hint_uz":    "Uchga boʻling.",
            "answer_key": "2",
            "accepted":   ["2 weighings", "ikki", "2 marta"],
            "answer_hint":    "a number",
            "answer_hint_uz": "son",
            "solution":    "<ol class='lg-steps'>…</ol>",
            "solution_uz": "<ol class='lg-steps'>…</ol>",
        },
        ...
    ]

Rounds, not hand-written dates: a puzzle says which round it belongs to and the
schedule turns that into ``opens_at`` / ``reveal_at``, so the whole season can be
moved by editing one line. A puzzle may still state explicit ``opens_at`` /
``reveal_at`` strings, which win over the schedule.

Usage::

    python manage.py import_logic logic/management/commands/_puzzles_logic_01_16.py --author=prime
    python manage.py import_logic <file> --author=prime --republish
"""
import datetime
import importlib.util
import os

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.db import transaction
from django.utils import timezone

from logic.models import CATEGORY_MAP, LogicPuzzle


BILINGUAL = ('title', 'teaser', 'body', 'hint', 'answer_hint', 'solution')
DATE_FORMATS = ('%Y-%m-%d %H:%M', '%Y-%m-%d')


class Command(BaseCommand):
    help = 'Bulk-create Logic Arena puzzles from a Python data file exposing PUZZLES.'

    def add_arguments(self, parser):
        parser.add_argument('datafile', help='Python file exposing PUZZLES (and optionally SCHEDULE).')
        parser.add_argument('--author', required=True,
                            help='Username the puzzles are credited to (must be staff).')
        parser.add_argument('--republish', action='store_true',
                            help='Overwrite puzzles that already exist (matched by number).')
        parser.add_argument('--draft', action='store_true',
                            help='Import with is_published=False, for previewing before a season starts.')

    # ── helpers ─────────────────────────────────────────────────────────────

    def _resolve_author(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise CommandError(f"User '{username}' not found.")
        if not user.is_staff:
            raise CommandError(f"User '{username}' is not staff, so they cannot publish puzzles.")
        return user

    def _load_module(self, datafile):
        if not os.path.isfile(datafile):
            raise CommandError(f'Data file not found: {datafile}')
        spec = importlib.util.spec_from_file_location('_logic_data', datafile)
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
        except Exception as exc:  # noqa: BLE001 — surface the real error
            raise CommandError(f'Could not read {datafile}: {exc}')
        if not hasattr(module, 'PUZZLES'):
            raise CommandError(f'{datafile} does not define PUZZLES.')
        return module

    def _parse(self, value):
        """'2026-07-13 09:00' -> an aware datetime in the project timezone."""
        for fmt in DATE_FORMATS:
            try:
                naive = datetime.datetime.strptime(value, fmt)
            except ValueError:
                continue
            return timezone.make_aware(naive, timezone.get_current_timezone())
        raise CommandError(f'Unreadable date: {value!r} (use "YYYY-MM-DD HH:MM").')

    def _dates(self, entry, schedule):
        """(opens_at, reveal_at) from explicit dates or from the round number."""
        if entry.get('opens_at') and entry.get('reveal_at'):
            return self._parse(entry['opens_at']), self._parse(entry['reveal_at'])
        if 'round' not in entry:
            raise CommandError(
                f"Puzzle #{entry.get('number')} has neither a 'round' nor explicit dates.")
        if not schedule:
            raise CommandError('The data file uses rounds but defines no SCHEDULE.')

        start = self._parse(schedule['start'])
        every = schedule.get('days', 7)
        window = schedule.get('window', every)
        opens = start + datetime.timedelta(days=every * (entry['round'] - 1))
        return opens, opens + datetime.timedelta(days=window)

    def _validate(self, entry):
        for field in ('number', 'title', 'body', 'answer_key', 'solution'):
            if not entry.get(field):
                raise CommandError(f'Puzzle {entry.get("number", "?")} is missing "{field}".')
        if entry.get('category') not in CATEGORY_MAP:
            raise CommandError(
                f'Puzzle #{entry["number"]}: unknown category {entry.get("category")!r}. '
                f'Known: {", ".join(CATEGORY_MAP)}.')
        if not 1 <= entry.get('difficulty', 0) <= 5:
            raise CommandError(f'Puzzle #{entry["number"]}: difficulty must be 1-5.')
        # A puzzle whose Uzbek half is missing would silently fall back to
        # English for an Uzbek reader, which is exactly the bug that is hard to
        # notice later — so refuse it here.
        missing = [f for f in ('title_uz', 'body_uz', 'solution_uz') if not entry.get(f)]
        if missing:
            raise CommandError(
                f'Puzzle #{entry["number"]} has no Uzbek {", ".join(missing)}. '
                f'Every puzzle ships in both languages.')

    # ── the work ────────────────────────────────────────────────────────────

    @transaction.atomic
    def handle(self, *args, **options):
        author = self._resolve_author(options['author'])
        module = self._load_module(options['datafile'])
        schedule = getattr(module, 'SCHEDULE', None)
        republish = options['republish']

        created = updated = skipped = 0

        for entry in module.PUZZLES:
            self._validate(entry)
            number = entry['number']
            existing = LogicPuzzle.objects.filter(number=number).first()

            if existing and not republish:
                self.stdout.write(self.style.WARNING(
                    f'  skip  #{number} {existing.title} (already exists — use --republish)'))
                skipped += 1
                continue

            opens_at, reveal_at = self._dates(entry, schedule)
            fields = {
                'category':   entry['category'],
                'difficulty': entry['difficulty'],
                'answer_key': entry['answer_key'],
                'accepted':   '\n'.join(entry.get('accepted', [])),
                'opens_at':   opens_at,
                'reveal_at':  reveal_at,
                'points':     entry.get('points', 0),
                'author':     author,
                'is_published': not options['draft'],
            }
            for base in BILINGUAL:
                fields[base] = entry.get(base, '')
                fields[f'{base}_uz'] = entry.get(f'{base}_uz', '')

            if existing:
                for key, value in fields.items():
                    setattr(existing, key, value)
                # points=0 means "derive from difficulty", and save() only fills
                # a falsy value — so clear it first or a re-import keeps the old
                # number after the difficulty changed.
                if not entry.get('points'):
                    existing.points = 0
                existing.save()
                updated += 1
                self.stdout.write(f'  edit  #{number} {existing.title}')
            else:
                puzzle = LogicPuzzle.objects.create(number=number, **fields)
                created += 1
                self.stdout.write(self.style.SUCCESS(f'  new   #{number} {puzzle.title}'))

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS(
            f'Done — {created} created, {updated} updated, {skipped} skipped.'))

        now = timezone.now()
        live = LogicPuzzle.objects.filter(is_published=True, opens_at__lte=now,
                                          reveal_at__gt=now).count()
        soon = LogicPuzzle.objects.filter(is_published=True, opens_at__gt=now).count()
        self.stdout.write(f'Open right now: {live}. Waiting to open: {soon}.')
