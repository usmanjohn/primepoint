"""The one command the Railway cron service runs, every day at 14:00 UTC
(19:00 Tashkent).

It is deliberately the only scheduled entry point: the Logic Arena check runs
first (a puzzle opening or revealing is the bigger news), then the daily quiz.
A failure in one does not stop the other, and every outcome is printed so the
Railway log of a run reads as a report.
"""
from django.core.management import call_command
from django.core.management.base import BaseCommand

from telegrambot import api, pick


class Command(BaseCommand):
    help = 'Everything the channel posts on a normal day. Run by cron.'

    def add_arguments(self, parser):
        parser.add_argument('--dry-run', action='store_true')

    def handle(self, *args, **options):
        dry = options['dry_run']
        extra = ['--dry-run'] if dry else []
        failures = []

        for command in ('post_logic_puzzle', 'post_daily_quiz'):
            self.stdout.write(self.style.MIGRATE_HEADING(f'── {command} ──'))
            try:
                call_command(command, *extra, stdout=self.stdout, stderr=self.stderr)
            except Exception as exc:                      # noqa: BLE001 — a cron run reports, never crashes
                failures.append(f'{command}: {exc}')
                self.stderr.write(self.style.ERROR(f'{command} failed: {exc}'))

        remaining = pick.remaining_by_subject()
        self.stdout.write('Qolgan savollar: ' +
                          ', '.join(f'{k} {v}' for k, v in remaining.items()))
        if not api.is_configured() and not dry:
            self.stderr.write(self.style.ERROR('TELEGRAM_BOT_TOKEN / TELEGRAM_CHANNEL are not set.'))
        if failures:
            # Non-zero exit so a failed run is visible in Railway, not silent.
            raise SystemExit(1)
