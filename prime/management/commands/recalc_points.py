"""Backfill practice rating_points, then recalculate every panda's rating.

`PracticeAttempt.rating_points` was added in May 2026 with a default of 0, but
attempts completed before then were never scored — 18 of them, which is why the
leaderboard showed every student on 0 despite real activity. This applies the
same formula `practice.views.finish_practice` uses to any completed attempt
still sitting at zero, then re-runs `recalc_rating` so ratings pick up the
libraries that only started awarding points later (exam prep, tutorials, exams).

    python manage.py recalc_points            # backfill + recalculate
    python manage.py recalc_points --dry-run  # report only, change nothing
"""
from django.core.management.base import BaseCommand
from django.db import transaction

# Kept in step with practice.views.finish_practice.
LEVEL_MULTIPLIER = {'easy': 1.0, 'medium': 1.5, 'hard': 2.0}


def score_to_points(score, level):
    return round((score / 100) * 10 * LEVEL_MULTIPLIER.get(level, 1.0) + 2, 1)


class Command(BaseCommand):
    help = "Backfill unscored practice attempts and recalculate all panda ratings."

    def add_arguments(self, parser):
        parser.add_argument('--dry-run', action='store_true',
                            help='Report what would change without writing.')

    def handle(self, *args, **options):
        from panda.models import Panda
        from practice.models import PracticeAttempt

        dry = options['dry_run']

        stale = list(
            PracticeAttempt.objects
            .filter(status='completed', rating_points=0)
            .select_related('practice')
        )
        self.stdout.write(f'Unscored completed attempts: {len(stale)}')

        # A dry run still writes, then rolls the whole transaction back. Skipping
        # the writes would make the rating preview meaningless, because
        # recalc_rating reads the very rows the backfill just fixed.
        with transaction.atomic():
            for attempt in stale:
                points = score_to_points(attempt.score, attempt.practice.level)
                self.stdout.write(
                    f'  {attempt.panda.profile.user.username:12s} '
                    f'{attempt.practice.title[:34]:36s} '
                    f'score={attempt.score:5.1f} -> {points} pts'
                )
                attempt.rating_points = points
                attempt.save(update_fields=['rating_points'])

            self.stdout.write('')
            changed = 0
            for panda in Panda.objects.select_related('profile__user'):
                before = panda.rating
                panda.recalc_rating()
                if before != panda.rating:
                    changed += 1
                    self.stdout.write(
                        f'  {panda.profile.user.username:12s} {before:5d} -> '
                        f'{panda.rating:5d} ({panda.rank})'
                    )

            if dry:
                transaction.set_rollback(True)

        verb = 'would change' if dry else 'changed'
        self.stdout.write(self.style.SUCCESS(
            f'{len(stale)} attempts scored, {changed} panda ratings {verb}.'
        ))
        if dry:
            self.stdout.write(self.style.WARNING('Dry run — nothing was saved.'))
