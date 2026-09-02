"""Post practice questions to the channel as native Telegram quiz polls.

    python manage.py post_daily_quiz --dry-run       # print, send nothing
    python manage.py post_daily_quiz                 # one, today's subject
    python manage.py post_daily_quiz --each-subject  # one per subject (what cron does)
"""
import time

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from telegrambot import api, content, pick
from telegrambot.content import ROTATION
from telegrambot.models import TelegramPost

# Telegram throttles a burst to one chat; a beat between polls keeps the five
# arriving in order instead of being queued or dropped.
GAP_SECONDS = 3


class Command(BaseCommand):
    help = 'Send the daily quiz poll to the Telegram channel.'

    def add_arguments(self, parser):
        parser.add_argument('--dry-run', action='store_true',
                            help='Build the post and print it without sending.')
        parser.add_argument('--subject', default=None,
                            help="Override the rotation, e.g. --subject='한국어'.")
        parser.add_argument('--force', action='store_true',
                            help='Send even if a quiz already went out today.')
        parser.add_argument('--each-subject', action='store_true',
                            help='Send one question per subject instead of one in total.')

    def handle(self, *args, **options):
        today = timezone.localdate()

        if options['each_subject'] and not options['subject']:
            self.post_each_subject(today, options)
            return

        already = TelegramPost.objects.filter(kind=TelegramPost.QUIZ,
                                              posted_at__date=today).exists()
        if already and not options['force']:
            self.stdout.write(self.style.WARNING(
                f'A quiz already went out on {today}; nothing sent. Use --force to override.'))
            return

        question, subject = pick.pick_question(today, options['subject'])
        if question is None:
            raise CommandError('No unposted, poll-shaped question left for any subject.')

        self.deliver(question, subject, options)

    def post_each_subject(self, today, options):
        """One question per subject, in rotation order, skipping any already sent today."""
        done = set() if options['force'] else pick.subjects_posted_on(today)
        sent = skipped = 0

        for name, label, _emoji in ROTATION:
            if name in done:
                self.stdout.write(f'{label}: already sent today, skipping.')
                skipped += 1
                continue
            question, _ = pick.pick_question(today, name)
            if question is None:
                self.stdout.write(self.style.WARNING(f'{label}: no question left, skipping.'))
                skipped += 1
                continue
            self.deliver(question, name, options)
            sent += 1
            if not options['dry_run'] and sent < len(ROTATION):
                time.sleep(GAP_SECONDS)

        self.stdout.write(self.style.SUCCESS(f'{sent} sent, {skipped} skipped.'))
        if not sent and not skipped:
            raise CommandError('No unposted, poll-shaped question left for any subject.')

    def deliver(self, question, subject, options):
        text, choices, correct, explanation, buttons = content.build_quiz(question)

        if options['dry_run']:
            self.stdout.write(self.style.MIGRATE_HEADING(f'\n[{subject}] question #{question.id}'))
            self.stdout.write(text)
            for i, choice in enumerate(choices):
                self.stdout.write(f'  {"✅" if i == correct else "  "} {choice}')
            self.stdout.write(self.style.HTTP_INFO(f'\nIzoh: {explanation or "— (yoʻq)"}'))
            self.stdout.write(f'Tugma: {buttons[0][0]} → {buttons[0][1]}')
            self.stdout.write(self.style.SUCCESS('Dry run — nothing was sent.'))
            return

        if not api.is_configured():
            raise CommandError('TELEGRAM_BOT_TOKEN / TELEGRAM_CHANNEL are not set.')
        try:
            api.refuse_local_database()
        except api.LocalDatabaseRefused as exc:
            raise CommandError(str(exc)) from exc

        result = api.send_quiz(text, choices, correct, explanation, buttons=buttons)
        TelegramPost.objects.create(
            kind=TelegramPost.QUIZ,
            object_id=question.id,
            chat_id=str(result.get('chat', {}).get('id', '')),
            message_id=result.get('message_id'),
        )
        self.stdout.write(self.style.SUCCESS(
            f'Sent [{subject}] question #{question.id} → message {result.get("message_id")}'))
