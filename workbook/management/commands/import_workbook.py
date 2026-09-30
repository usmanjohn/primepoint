"""
Bulk-import workbooks (a Prime lesson's fourth leg) from a Python data file.

The data file exposes a ``WORKBOOKS`` list, one dict per lesson::

    WORKBOOKS = [
        {
            "tutorial": "PK-9: Salomlashish, xayrlashish va oʻzini tanishtirish",
            "intro":    "<p>…</p>",                      # optional
            "tasks": [
                {
                    "section":     "B",                  # A B C D E
                    "kind":        "gap",                # see workbook.models.KINDS
                    "title":       "Oyoqqa qarang",      # optional
                    "instruction": "<p>…</p>",           # Uzbek
                    "stars":       1,                    # 1-3, optional
                    "items": [
                        {"stem": "저는 학생___.", "answers": ["입니다"],
                         "explanation": "<p>…</p>", "size": "s"},
                    ],
                },
            ],
        },
    ]

Item keys: stem, answers, model_answer, explanation, words (build/copy),
options (pick), checklist (write), size (s/m/l).

Usage::

    python manage.py import_workbook <file> --author=prime --expect-items=87
    python manage.py import_workbook <file> --author=prime --republish --expect-items=87

``--republish`` updates in place — tasks matched by (section, position),
items by position — so the answers pupils have already typed survive a
correction. Only tasks or items that no longer exist are deleted.

``--expect-items`` is the total number of items in the file. A file that
silently lost an item still imports and is quietly wrong, so give it.
"""
import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from tutorial.models import Tutorial
from workbook import grading
from workbook.models import AUTO_KINDS, KINDS, SECTIONS, Task, TaskItem, Workbook
from workbook.pdfs import data_hash

VALID_KINDS = {k for k, _l in KINDS}
VALID_SECTIONS = {s for s, _l in SECTIONS}
ITEM_KEYS = {'stem', 'answers', 'model_answer', 'explanation', 'words',
             'options', 'checklist', 'size'}
TASK_KEYS = {'section', 'kind', 'title', 'instruction', 'stars', 'items'}


def load(path):
    if not os.path.exists(path):
        raise CommandError(f'No such file: {path}')
    # Compiled from source every time, never through importlib: a data file
    # edited within the same second at the same byte size would otherwise be
    # read from a stale __pycache__ entry and import the old answers.
    namespace = {'__file__': path, '__name__': '_workbook_data'}
    with open(path, encoding='utf-8') as fh:
        exec(compile(fh.read(), path, 'exec'), namespace)
    if 'WORKBOOKS' not in namespace:
        raise CommandError(f'{path} has no WORKBOOKS list.')
    return namespace['WORKBOOKS']


def validate(entry):
    """Every problem with one workbook dict, as readable strings."""
    problems = []
    where = entry.get('tutorial', '?')
    tasks = entry.get('tasks') or []
    if not tasks:
        problems.append(f'{where}: no tasks')
    for t_i, task in enumerate(tasks, 1):
        tag = f"{where} task {t_i} ({task.get('section')}/{task.get('kind')})"
        extra = set(task) - TASK_KEYS
        if extra:
            problems.append(f'{tag}: unknown keys {sorted(extra)}')
        if task.get('section') not in VALID_SECTIONS:
            problems.append(f'{tag}: bad section')
        kind = task.get('kind')
        if kind not in VALID_KINDS:
            problems.append(f'{tag}: bad kind')
        if not (task.get('instruction') or '').strip():
            problems.append(f'{tag}: no instruction')
        items = task.get('items') or []
        if not items:
            problems.append(f'{tag}: no items')
        for i_i, item in enumerate(items, 1):
            itag = f'{tag} item {i_i}'
            extra = set(item) - ITEM_KEYS
            if extra:
                problems.append(f'{itag}: unknown keys {sorted(extra)}')
            answers = item.get('answers') or []
            if kind in AUTO_KINDS:
                if not answers or not all(isinstance(a, str) and a.strip() for a in answers):
                    problems.append(f'{itag}: an auto-marked item needs answers')
                if kind in ('gap', 'conj') and '___' not in (item.get('stem') or ''):
                    problems.append(f'{itag}: a {kind} stem needs a ___ gap')
                if kind == 'build' and not item.get('words'):
                    problems.append(f'{itag}: build needs words')
                if kind == 'pick':
                    options = item.get('options') or []
                    if len(options) < 2:
                        problems.append(f'{itag}: pick needs 2+ options')
                    if answers and answers[0] not in options:
                        problems.append(f'{itag}: pick answer is not among the options')
                    if len(set(options)) != len(options):
                        problems.append(f'{itag}: duplicate options')
                # The key must pass its own marker — a normalisation surprise
                # here would mark the right answer wrong for every pupil.
                for a in answers:
                    if grading.mark(a, answers, grading.IGNORE_FOR_KIND.get(kind, '')) != grading.RIGHT:
                        problems.append(f'{itag}: answer {a!r} fails its own marker')
            if kind == 'write' and not (item.get('model_answer') or '').strip():
                problems.append(f'{itag}: write needs a model_answer')
            if kind == 'copy' and not item.get('words'):
                problems.append(f'{itag}: copy needs words')
            if kind in ('mission', 'write') and not (item.get('stem') or '').strip():
                problems.append(f'{itag}: {kind} needs a stem')
            if item.get('size', 'm') not in ('s', 'm', 'l'):
                problems.append(f'{itag}: size must be s/m/l')
    return problems


class Command(BaseCommand):
    help = 'Bulk-import workbooks (fourth leg) from a Python data file exposing WORKBOOKS.'

    def add_arguments(self, parser):
        parser.add_argument('datafile')
        parser.add_argument('--author', help='Username recorded as the creator.')
        parser.add_argument('--republish', action='store_true',
                            help='Update workbooks that already exist (in place).')
        parser.add_argument('--expect-items', type=int,
                            help='Total number of items the file must contain.')

    def handle(self, *args, **opts):
        entries = load(opts['datafile'])

        problems = []
        for entry in entries:
            problems.extend(validate(entry))
        if problems:
            raise CommandError('Refusing to import:\n  ' + '\n  '.join(problems))

        total = sum(len(t['items']) for e in entries for t in e['tasks'])
        if opts['expect_items'] is not None and total != opts['expect_items']:
            raise CommandError(f'Expected {opts["expect_items"]} items, the file has {total}.')

        author = None
        if opts['author']:
            author = User.objects.filter(username=opts['author']).first()
            if author is None:
                raise CommandError(f'No user {opts["author"]!r}.')

        made = updated = skipped = 0
        for entry in entries:
            tutorial = Tutorial.objects.filter(title=entry['tutorial']).first()
            if tutorial is None:
                raise CommandError(f'No tutorial titled {entry["tutorial"]!r} — import it first.')
            workbook = Workbook.objects.filter(tutorial=tutorial).first()
            if workbook and not opts['republish']:
                skipped += 1
                self.stdout.write(f'  skip  {tutorial.title} (exists; --republish to update)')
                continue
            with transaction.atomic():
                if workbook is None:
                    workbook = Workbook.objects.create(tutorial=tutorial, created_by=author)
                    made += 1
                else:
                    updated += 1
                workbook.intro = entry.get('intro', '')
                workbook.data_hash = data_hash(entry)
                workbook.is_published = True
                workbook.save()
                self._sync_tasks(workbook, entry['tasks'])
                for attempt in workbook.attempts.all():
                    attempt.rescore()
                    attempt.save()
            n = sum(len(t['items']) for t in entry['tasks'])
            self.stdout.write(self.style.SUCCESS(
                f'  ok    {tutorial.title} — {len(entry["tasks"])} tasks, {n} items'))

        self.stdout.write(self.style.SUCCESS(
            f'Done: {made} created, {updated} updated, {skipped} skipped, {total} items in file.'))

    def _sync_tasks(self, workbook, tasks):
        existing = {(t.section, t.order): t for t in workbook.tasks.all()}
        keep = set()
        position = {}
        for data in tasks:
            section = data['section']
            position[section] = position.get(section, 0) + 1
            key = (section, position[section])
            task = existing.get(key) or Task(workbook=workbook, section=section, order=key[1])
            task.kind = data['kind']
            task.title = data.get('title', '')
            task.instruction = data['instruction']
            task.stars = data.get('stars', 1)
            task.save()
            keep.add(task.pk)
            self._sync_items(task, data['items'])
        workbook.tasks.exclude(pk__in=keep).delete()

    def _sync_items(self, task, items):
        existing = {i.order: i for i in task.items.all()}
        keep = set()
        for order, data in enumerate(items, 1):
            item = existing.get(order) or TaskItem(task=task, order=order)
            item.stem = data.get('stem', '')
            item.answers = data.get('answers', [])
            item.model_answer = data.get('model_answer', '')
            item.explanation = data.get('explanation', '')
            item.words = data.get('words', [])
            item.options = data.get('options', [])
            item.checklist = data.get('checklist', [])
            item.size = data.get('size', 'm')
            item.save()
            keep.add(item.pk)
            # Re-mark what pupils already typed against the (possibly new) key.
            for response in item.responses.all():
                if task.kind in AUTO_KINDS:
                    response.regrade()
                    response.save(update_fields=['verdict', 'is_correct', 'updated_at'])
        task.items.exclude(pk__in=keep).delete()
