"""Rebuild every master's cached rating and contribution score.

Everything this writes is derived from other tables (reviews, published
content, pupil progress), so it is safe to run at any time and safe to run
twice. Run it after a bulk content import — the importers write tutorials,
lessons and readings straight into the DB without touching the author's
Master row, so contribution scores go stale until this runs.

    python manage.py recalc_master_stats
    railway run python manage.py recalc_master_stats
"""
from django.core.management.base import BaseCommand

from masters.models import Master


class Command(BaseCommand):
    help = "Recalculate student ratings and contribution scores for all masters."

    def add_arguments(self, parser):
        parser.add_argument('--master', type=int, default=None,
                            help='Only this master id.')
        parser.add_argument('--quiet', action='store_true',
                            help='Print the summary line only.')

    def handle(self, *args, **options):
        qs = Master.objects.all()
        if options['master']:
            qs = qs.filter(pk=options['master'])

        for master in qs:
            master.recalc_stats()
            if not options['quiet']:
                self.stdout.write(
                    f'{master.name:<28} '
                    f'rating {master.avg_rating}/10 ({master.review_count}) '
                    f'· contribution {master.contribution_score} '
                    f'· {master.content_count} items · {master.learner_count} pupils'
                )

        self.stdout.write(self.style.SUCCESS(f'Recalculated {qs.count()} master(s).'))
