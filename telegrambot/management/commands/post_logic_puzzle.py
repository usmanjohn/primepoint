"""Announce a Logic Arena puzzle when it opens, and its solution when it reveals.

    python manage.py post_logic_puzzle --dry-run
    python manage.py post_logic_puzzle

Safe to run every day: it posts only what is due and not yet posted.
"""
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from logic.models import LogicPuzzle
from telegrambot import api, content
from telegrambot.models import TelegramPost


class Command(BaseCommand):
    help = 'Post any newly opened Logic Arena puzzle, and any solution now revealed.'

    def add_arguments(self, parser):
        parser.add_argument('--dry-run', action='store_true')

    def handle(self, *args, **options):
        now = timezone.now()
        dry = options['dry_run']
        sent = 0

        posted_puzzles = set(TelegramPost.objects.filter(kind=TelegramPost.PUZZLE)
                             .values_list('object_id', flat=True))
        posted_solutions = set(TelegramPost.objects.filter(kind=TelegramPost.SOLUTION)
                               .values_list('object_id', flat=True))

        # ── puzzles that have opened but were never announced ───────────────
        opened = (LogicPuzzle.objects
                  .filter(is_published=True, opens_at__lte=now)
                  .exclude(id__in=posted_puzzles)
                  .order_by('opens_at'))
        for puzzle in opened:
            # Only announce something still worth answering — never a puzzle
            # whose reveal has already passed while the bot was off.
            if puzzle.reveal_at <= now:
                continue
            text, buttons = content.build_puzzle(puzzle)
            sent += self._send(TelegramPost.PUZZLE, puzzle, text, buttons, dry)

        # ── solutions now due, for puzzles we did announce ──────────────────
        revealed = (LogicPuzzle.objects
                    .filter(is_published=True, reveal_at__lte=now, id__in=posted_puzzles)
                    .exclude(id__in=posted_solutions)
                    .order_by('reveal_at'))
        for puzzle in revealed:
            text, buttons = content.build_solution(puzzle)
            sent += self._send(TelegramPost.SOLUTION, puzzle, text, buttons, dry)

        if not sent:
            self.stdout.write('Nothing due.')

    def _send(self, kind, puzzle, text, buttons, dry):
        if dry:
            self.stdout.write(self.style.MIGRATE_HEADING(f'\n[{kind}] puzzle #{puzzle.number}'))
            self.stdout.write(text)
            self.stdout.write(f'Tugma: {buttons[0][0]} → {buttons[0][1]}')
            return 1
        if not api.is_configured():
            raise CommandError('TELEGRAM_BOT_TOKEN / TELEGRAM_CHANNEL are not set.')
        result = api.send_message(text, buttons=buttons)
        TelegramPost.objects.create(
            kind=kind, object_id=puzzle.id,
            chat_id=str(result.get('chat', {}).get('id', '')),
            message_id=result.get('message_id'),
        )
        self.stdout.write(self.style.SUCCESS(
            f'Sent {kind} for puzzle #{puzzle.number} → message {result.get("message_id")}'))
        return 1
