"""Study-abroad deadlines on the channel.

    python manage.py post_abroad_deadlines --dry-run
    python manage.py post_abroad_deadlines

Two kinds of post, both safe to attempt every day:

  · the MONTHLY DIGEST — the first run of each month (Tashkent date) lists the
    deadlines of the next DIGEST_DAYS days. Estimates are marked, never counted
    down; stale or closed facts are left out.
  · the LAST CALL — once, when a confirmed, open deadline is REMIND_DAYS away.

The same rule as the site holds: a pupil is never shown a confident wrong
date, so nothing stale is ever posted.
"""
import datetime

from django.core.management.base import BaseCommand, CommandError

from abroad.models import Deadline, today as tashkent_today
from telegrambot import api, content
from telegrambot.models import TelegramPost

DIGEST_DAYS = 60
REMIND_DAYS = 7


def digest_deadlines(day):
    horizon = day + datetime.timedelta(days=DIGEST_DAYS)
    rows = (Deadline.objects.select_related('scholarship')
            .filter(scholarship__is_published=True, closes__gte=day, closes__lte=horizon)
            .order_by('closes'))
    return [d for d in rows if d.state in ('open', 'upcoming', 'estimate')]


def reminder_deadlines(day):
    rows = (Deadline.objects.select_related('scholarship')
            .filter(scholarship__is_published=True, is_estimate=False,
                    closes__gte=day, closes__lte=day + datetime.timedelta(days=REMIND_DAYS)))
    return [d for d in rows if d.state == 'open']


class Command(BaseCommand):
    help = 'Post the monthly study-abroad deadlines, and a reminder 7 days before each.'

    def add_arguments(self, parser):
        parser.add_argument('--dry-run', action='store_true')
        parser.add_argument('--force-digest', action='store_true',
                            help='Send the digest even if this month already has one.')

    def handle(self, *args, **options):
        day = tashkent_today()
        dry = options['dry_run']
        sent = 0

        month_key = day.year * 100 + day.month
        month_done = TelegramPost.objects.filter(
            kind=TelegramPost.ABROAD_MONTH, object_id=month_key).exists()
        if options['force_digest'] or not month_done:
            rows = digest_deadlines(day)
            if rows:
                text, buttons = content.build_abroad_digest(rows, day)
                sent += self._send(TelegramPost.ABROAD_MONTH, month_key, text, buttons, dry)
            else:
                self.stdout.write('No deadlines in the next %d days — no digest.' % DIGEST_DAYS)

        reminded = set(TelegramPost.objects.filter(kind=TelegramPost.ABROAD_REMINDER)
                       .values_list('object_id', flat=True))
        for d in reminder_deadlines(day):
            if d.id in reminded:
                continue
            text, buttons = content.build_abroad_reminder(d)
            sent += self._send(TelegramPost.ABROAD_REMINDER, d.id, text, buttons, dry)

        if not sent:
            self.stdout.write('Nothing due.')

    def _send(self, kind, object_id, text, buttons, dry):
        if dry:
            self.stdout.write(self.style.MIGRATE_HEADING(f'\n[{kind}] {object_id}'))
            self.stdout.write(text)
            self.stdout.write(f'Tugma: {buttons[0][0]} → {buttons[0][1]}')
            return 1
        if not api.is_configured():
            raise CommandError('TELEGRAM_BOT_TOKEN / TELEGRAM_CHANNEL are not set.')
        try:
            api.refuse_local_database()
        except api.LocalDatabaseRefused as exc:
            raise CommandError(str(exc)) from exc
        result = api.send_message(text, buttons=buttons)
        TelegramPost.objects.create(
            kind=kind, object_id=object_id,
            chat_id=str(result.get('chat', {}).get('id', '')),
            message_id=result.get('message_id'),
        )
        self.stdout.write(self.style.SUCCESS(f'Sent {kind} {object_id} → message {result.get("message_id")}'))
        return 1
