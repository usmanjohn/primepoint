"""The one command the Railway cron service runs, once a day.

The time lives in Railway's cron field, not here: `0 17 * * *` = 22:00 Tashkent.

It is deliberately the only scheduled entry point: the Logic Arena check runs
first (a puzzle opening or revealing is the bigger news), then the daily quiz.
A failure in one does not stop the other, and every outcome is printed so the
Railway log of a run reads as a report.
"""
import time

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import OperationalError, connection

from telegrambot import api, pick

# Railway's private network (postgres.railway.internal) takes a moment to come
# up after a container starts. A web server never notices — it is up for hours —
# but a cron job that connects the instant it boots loses the race and dies with
# "could not translate host name". So wait for the database before doing work.
DB_WAIT_SECONDS = 60
DB_RETRY_DELAY = 2


class Command(BaseCommand):
    help = 'Everything the channel posts on a normal day. Run by cron.'

    def add_arguments(self, parser):
        parser.add_argument('--dry-run', action='store_true')

    def wait_for_db(self):
        """Block until the database answers, or give up after DB_WAIT_SECONDS."""
        deadline = time.monotonic() + DB_WAIT_SECONDS
        attempt = 0
        while True:
            attempt += 1
            try:
                connection.ensure_connection()
                if attempt > 1:
                    self.stdout.write(f'Database reachable after {attempt} attempts.')
                return True
            except OperationalError as exc:
                connection.close()
                if time.monotonic() >= deadline:
                    self.stderr.write(self.style.ERROR(
                        f'Database unreachable after {DB_WAIT_SECONDS}s: {exc}'))
                    return False
                time.sleep(DB_RETRY_DELAY)

    def handle(self, *args, **options):
        if not self.wait_for_db():
            raise SystemExit(1)

        dry = options['dry_run']
        extra = ['--dry-run'] if dry else []
        failures = []

        # One question per subject — Ingliz tili, Koreys tili, Matematika,
        # Rus tili and Matematika (SAT) each get their own poll every day.
        jobs = [('post_logic_puzzle', []), ('post_daily_quiz', ['--each-subject'])]

        for command, args in jobs:
            self.stdout.write(self.style.MIGRATE_HEADING(f'── {command} ──'))
            try:
                call_command(command, *args, *extra, stdout=self.stdout, stderr=self.stderr)
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
