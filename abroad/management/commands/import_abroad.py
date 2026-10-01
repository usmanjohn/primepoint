"""
Bulk-import Study-abroad content from a Python data file.

The file may expose any of:

    SCHOLARSHIPS = [{slug, name, country, country_uz, …, official_url, last_checked}]
    DEADLINES    = [{scholarship: <slug>, label, label_uz, closes, source_url, last_checked, …}]
    GUIDES       = [{slug, order, category, icon, minutes, title, title_uz, summary, summary_uz, body, body_uz}]
    SAMPLES      = [{slug, kind, scholarship: <slug|None>, title, title_uz, letter, notes, prompts, …}]
    UNIVERSITIES = [{name, city, country, url, strengths, strengths_uz, …}]
    CHECKLISTS   = {"gks-u": [{text, text_uz, hint, hint_uz}], …}

Dates are "YYYY-MM-DD" strings.

    python manage.py import_abroad abroad/management/commands/_abroad_<part>.py --author=prime
    python manage.py import_abroad <file> --author=prime --republish

The importer REFUSES:
  · anything missing its English or its Uzbek side — the section is bilingual;
  · a deadline or scholarship without an official source and a last-checked
    date — a confident wrong date is worse than none;
  · an http:// source (official pages are https; a typo'd scheme is a smell).

Guides, samples and scholarships are skipped if they exist, unless
--republish. Deadlines, universities and checklists are always synced.
"""
import datetime
import os

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from abroad.models import (
    ChecklistItem, Deadline, Guide, Sample, Scholarship, University,
)

PAIRS = {
    'GUIDES': [('title', 'title_uz'), ('summary', 'summary_uz'), ('body', 'body_uz')],
    'SCHOLARSHIPS': [('country', 'country_uz'), ('summary', 'summary_uz')],
    'DEADLINES': [('label', 'label_uz')],
    'SAMPLES': [('title', 'title_uz')],
    'UNIVERSITIES': [('strengths', 'strengths_uz')],
}


def load(path):
    if not os.path.exists(path):
        raise CommandError(f'No such file: {path}')
    namespace = {'__file__': path, '__name__': '_abroad_data'}
    with open(path, encoding='utf-8') as fh:
        exec(compile(fh.read(), path, 'exec'), namespace)
    return namespace


def _date(value, where):
    try:
        return datetime.date.fromisoformat(value)
    except (TypeError, ValueError):
        raise CommandError(f'{where}: bad date {value!r} (want YYYY-MM-DD)')


def validate(data):
    problems = []
    for key, pairs in PAIRS.items():
        for i, row in enumerate(data.get(key, []), 1):
            tag = f"{key}[{i}] {row.get('slug') or row.get('label') or row.get('name') or ''}"
            for en, uz in pairs:
                if not (row.get(en) or '').strip():
                    problems.append(f'{tag}: missing {en}')
                if not (row.get(uz) or '').strip():
                    problems.append(f'{tag}: missing {uz}')
            # a filled English optional field needs its Uzbek twin, and vice versa
            for field in list(row):
                if field.endswith('_uz'):
                    base = field[:-3]
                    if bool((row.get(base) or '').strip()) != bool((row.get(field) or '').strip()):
                        problems.append(f'{tag}: {base} and {field} must both be filled or both empty')
    for i, row in enumerate(data.get('SCHOLARSHIPS', []), 1):
        tag = f"SCHOLARSHIPS[{i}] {row.get('slug')}"
        if not str(row.get('official_url', '')).startswith('https://'):
            problems.append(f'{tag}: official_url must be https')
        if not row.get('last_checked'):
            problems.append(f'{tag}: last_checked is required')
    for i, row in enumerate(data.get('DEADLINES', []), 1):
        tag = f"DEADLINES[{i}] {row.get('label')}"
        if not str(row.get('source_url', '')).startswith('https://'):
            problems.append(f'{tag}: source_url must be https')
        for f in ('closes', 'last_checked'):
            if not row.get(f):
                problems.append(f'{tag}: {f} is required')
        if row.get('opens') and row.get('closes') and row['opens'] > row['closes']:
            problems.append(f'{tag}: opens after it closes')
    for i, row in enumerate(data.get('SAMPLES', []), 1):
        tag = f"SAMPLES[{i}] {row.get('slug')}"
        from abroad.views import letter_paragraphs
        count = len(letter_paragraphs(row.get('letter', '')))
        for n in row.get('notes', []):
            if not (n.get('en') and n.get('uz') and n.get('para')):
                problems.append(f'{tag}: every note needs para, en and uz')
            elif not 1 <= n['para'] <= count:
                # A note pointing past the last paragraph is never shown.
                problems.append(f"{tag}: note para {n['para']} but the letter has {count} paragraphs")
        for p in row.get('prompts', []):
            if not (p.get('en') and p.get('uz')):
                problems.append(f'{tag}: every prompt needs en and uz')
    for target, items in (data.get('CHECKLISTS') or {}).items():
        for i, item in enumerate(items, 1):
            if not (item.get('text') and item.get('text_uz')):
                problems.append(f'CHECKLISTS[{target}][{i}]: needs text and text_uz')
    return problems


class Command(BaseCommand):
    help = 'Import Study-abroad content (guides, scholarships, deadlines, samples, universities, checklists).'

    def add_arguments(self, parser):
        parser.add_argument('datafile')
        parser.add_argument('--author', help='Accepted for symmetry with the other importers.')
        parser.add_argument('--republish', action='store_true')

    def handle(self, *args, **opts):
        data = load(opts['datafile'])
        problems = validate(data)
        if problems:
            raise CommandError('Refusing to import:\n  ' + '\n  '.join(problems))
        self.republish = opts['republish']
        with transaction.atomic():
            for row in data.get('SCHOLARSHIPS', []):
                row = dict(row, last_checked=_date(row['last_checked'], row['slug']))
                self._upsert(Scholarship, {'slug': row.pop('slug')}, row)
            for row in data.get('DEADLINES', []):
                row = dict(row)
                sch = Scholarship.objects.filter(slug=row.pop('scholarship')).first()
                if sch is None:
                    raise CommandError(f"Deadline {row['label']!r}: unknown scholarship")
                for f in ('opens', 'closes', 'last_checked'):
                    if row.get(f):
                        row[f] = _date(row[f], row['label'])
                Deadline.objects.update_or_create(scholarship=sch, label=row.pop('label'), defaults=row)
                self.stdout.write(f'  deadline  {sch.slug}: {row["closes"]}')
            for row in data.get('GUIDES', []):
                row = dict(row)
                self._upsert(Guide, {'slug': row.pop('slug')}, row)
            for row in data.get('SAMPLES', []):
                row = dict(row)
                slug = row.pop('scholarship', None)
                row['scholarship'] = Scholarship.objects.filter(slug=slug).first() if slug else None
                self._upsert(Sample, {'slug': row.pop('slug')}, row)
            for order, row in enumerate(data.get('UNIVERSITIES', []), 1):
                row = dict(row, order=row.get('order', order))
                University.objects.update_or_create(name=row.pop('name'), defaults=row)
            if data.get('UNIVERSITIES'):
                self.stdout.write(f"  universities: {len(data['UNIVERSITIES'])}")
            for target, items in (data.get('CHECKLISTS') or {}).items():
                for order, item in enumerate(items, 1):
                    ChecklistItem.objects.update_or_create(target=target, order=order, defaults=item)
                # Ticks on removed rows go with them; kept rows keep their ticks.
                ChecklistItem.objects.filter(target=target, order__gt=len(items)).delete()
                self.stdout.write(f'  checklist {target}: {len(items)} items')
        self.stdout.write(self.style.SUCCESS('Done.'))

    def _upsert(self, model, key, fields):
        obj = model.objects.filter(**key).first()
        if obj and not self.republish:
            self.stdout.write(f'  skip  {model.__name__} {key} (exists; --republish to update)')
            return
        if obj is None:
            obj = model(**key)
        for k, v in fields.items():
            setattr(obj, k, v)
        obj.save()
        self.stdout.write(self.style.SUCCESS(f'  ok    {model.__name__} {key}'))
