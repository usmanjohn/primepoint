# -*- coding: utf-8 -*-
"""Remove Russian stress marks (ударение) from Corner stories.

The combining acute U+0301 is a teaching aid: it tells a beginner which
vowel carries the stress, which in Russian decides how every unstressed
vowel is pronounced. Prime Russian used it in the readings from the
start; in August 2026 the user asked for the readings to look like real
Russian instead, so the marks were removed from the story sources and
this command clears them out of an existing database.

The Prime Russian TUTORIALS keep their marks — a lesson is where you
first meet the word, a reading is where you meet it in the wild.

    python manage.py strip_stress --dry-run
    python manage.py strip_stress
    python manage.py strip_stress --collection="Prime Russian Readings"

Never touches ё (a separate character, always stressed) and never
touches the Uzbek glosses, which carry no acute.
"""

from django.core.management.base import BaseCommand
from django.db import transaction

from corner.models import Story

ACUTE = '́'          # combining acute accent


def clean(value):
    """Strip the acute from a str, or from every str inside a list."""
    if isinstance(value, str):
        return value.replace(ACUTE, '')
    if isinstance(value, list):
        return [clean(v) for v in value]
    return value


class Command(BaseCommand):
    help = 'Remove Russian stress marks (U+0301) from Corner stories.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--collection', action='append', dest='collections', default=None,
            help='Collection title to clean. Repeatable. Default: every collection.',
        )
        parser.add_argument(
            '--dry-run', action='store_true',
            help='Report what would change without writing anything.',
        )

    def handle(self, *args, **opts):
        dry = opts['dry_run']
        qs = Story.objects.select_related('collection').order_by('collection__title', 'order')
        if opts['collections']:
            qs = qs.filter(collection__title__in=opts['collections'])

        stories = grammar = questions = marks = 0

        with transaction.atomic():
            for story in qs:
                before = (story.title + story.summary + story.body).count(ACUTE)
                g_rows = list(story.grammar.all())
                q_rows = list(story.questions.all())
                before += sum(
                    (g.pattern + g.meaning + ''.join(g.examples or [])).count(ACUTE)
                    for g in g_rows
                )
                before += sum(
                    (q.text + q.explanation + ''.join(q.choices or [])).count(ACUTE)
                    for q in q_rows
                )
                if not before:
                    continue

                stories += 1
                marks += before
                self.stdout.write(
                    f'  [{story.collection.title}] {story.order}. '
                    f'{clean(story.title)} — {before} marks'
                )
                grammar += sum(1 for g in g_rows
                               if (g.pattern + g.meaning + ''.join(g.examples or [])).count(ACUTE))
                questions += sum(1 for q in q_rows
                                 if (q.text + q.explanation + ''.join(q.choices or [])).count(ACUTE))
                if dry:
                    continue

                story.title = clean(story.title)
                story.summary = clean(story.summary)
                story.body = clean(story.body)
                # save() re-runs _sync_words(), so the tappable vocabulary
                # and the end-of-story flashcards are rebuilt unstressed too.
                story.save()

                for g in g_rows:
                    g.pattern, g.meaning = clean(g.pattern), clean(g.meaning)
                    g.examples = clean(g.examples)
                    g.save()

                for q in q_rows:
                    q.text, q.explanation = clean(q.text), clean(q.explanation)
                    q.choices = clean(q.choices)
                    q.save()

            if dry:
                transaction.set_rollback(True)

        verb = 'would clean' if dry else 'cleaned'
        self.stdout.write(self.style.SUCCESS(
            f'\n{verb}: {stories} stories, {grammar} grammar rows, '
            f'{questions} questions — {marks} stress marks total.'
        ))
        if dry:
            self.stdout.write('(dry run — nothing was written)')
