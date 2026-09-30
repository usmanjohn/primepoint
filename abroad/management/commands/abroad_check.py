"""
What needs re-checking in the Study-abroad section.

    python manage.py abroad_check            # stale (> 1 year) or already-closed facts
    python manage.py abroad_check --days 180 # stricter

This is the to-do list for "update the abroad deadlines": every row names
the official source to re-read. Closed deadlines are listed because the next
cycle's dates are what a pupil now needs.
"""
from django.core.management.base import BaseCommand
from abroad.models import Deadline, Scholarship, today as tashkent_today


class Command(BaseCommand):
    help = 'List Study-abroad facts that are stale or whose deadline has passed.'

    def add_arguments(self, parser):
        parser.add_argument('--days', type=int, default=365)

    def handle(self, *args, **opts):
        today = tashkent_today()
        n = 0
        for s in Scholarship.objects.order_by('order'):
            age = (today - s.last_checked).days
            if age > opts['days']:
                n += 1
                self.stdout.write(f'STALE  scholarship {s.slug:<12} checked {age} days ago → {s.official_url}')
        for d in Deadline.objects.select_related('scholarship').order_by('closes'):
            age = (today - d.last_checked).days
            if age > opts['days']:
                n += 1
                self.stdout.write(f'STALE  {d.label} (checked {age} days ago) → {d.source_url}')
            elif d.closes < today:
                n += 1
                self.stdout.write(f'CLOSED {d.label} closed {d.closes} — add the next cycle → {d.source_url}')
            elif d.is_estimate:
                n += 1
                self.stdout.write(f'ESTIM  {d.label} closes {d.closes} (estimate) — confirm when announced → {d.source_url}')
        self.stdout.write(self.style.SUCCESS(f'{n} item(s) to look at.'))
