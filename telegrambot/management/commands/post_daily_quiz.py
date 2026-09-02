"""Post one practice question to the channel as a native Telegram quiz poll.

    python manage.py post_daily_quiz --dry-run     # print it, send nothing
    python manage.py post_daily_quiz               # send today's
"""
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from telegrambot import api, content, pick
from telegrambot.models import TelegramPost


class Command(BaseCommand):
    help = 'Send the daily quiz poll to the Telegram channel.'

    def add_arguments(self, parser):
        parser.add_argument('--dry-run', action='store_true',
                            help='Build the post and print it without sending.')
        parser.add_argument('--subject', default=None,
                            help="Override the rotation, e.g. --subject='한국어'.")
        parser.add_argument('--force', action='store_true',
                            help='Send even if a quiz already went out today.')

    def handle(self, *args, **options):
        today = timezone.localdate()

        already = TelegramPost.objects.filter(kind=TelegramPost.QUIZ,
                                              posted_at__date=today).exists()
        if already and not options['force']:
            self.stdout.write(self.style.WARNING(
                f'A quiz already went out on {today}; nothing sent. Use --force to override.'))
            return

        question, subject = pick.pick_question(today, options['subject'])
        if question is None:
            raise CommandError('No unposted, poll-shaped question left for any subject.')

        text, choices, correct, explanation, buttons = content.build_quiz(question)

        if options['dry_run']:
            self.stdout.write(self.style.MIGRATE_HEADING(f'\n[{subject}] question #{question.id}'))
            self.stdout.write(text)
            for i, choice in enumerate(choices):
                self.stdout.write(f'  {"✅" if i == correct else "  "} {choice}')
            self.stdout.write(self.style.HTTP_INFO(f'\nIzoh: {explanation or "— (yoʻq)"}'))
            self.stdout.write(f'Tugma: {buttons[0][0]} → {buttons[0][1]}')
            self.stdout.write(self.style.SUCCESS('\nDry run — nothing was sent.'))
            return

        if not api.is_configured():
            raise CommandError('TELEGRAM_BOT_TOKEN / TELEGRAM_CHANNEL are not set.')

        result = api.send_quiz(text, choices, correct, explanation, buttons=buttons)
        TelegramPost.objects.create(
            kind=TelegramPost.QUIZ,
            object_id=question.id,
            chat_id=str(result.get('chat', {}).get('id', '')),
            message_id=result.get('message_id'),
        )
        self.stdout.write(self.style.SUCCESS(
            f'Sent [{subject}] question #{question.id} → message {result.get("message_id")}'))
