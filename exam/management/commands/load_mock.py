"""
Load a full mock exam (questions + passages) from a Python data file.

Usage:
    python manage.py load_mock exam/data/mock1_listening.py
    python manage.py load_mock exam/data/mock1_reading.py --dry-run

The data file must define:

    EXAM_META = {              # identifies / creates the Exam row
        'title': 'TOPIK II — 모의고사 1회 (PrimePoint)',
        'language': 'korean',
        'exam_number': 1,
        'listening_minutes': 60, 'reading_minutes': 70, 'writing_minutes': 50,
        'allow_audio_replay': True, 'allow_audio_pause': True,
        'is_published': True,
    }

    PASSAGES = [               # shared instruction boxes / texts (ExamPassage)
        {'section': 'listening', 'from': 1, 'to': 3, 'text': '<b>※ [1~3] ...</b>'},
    ]

    QUESTIONS = [
        {'section': 'listening', 'number': 1,
         'question_text': '',                 # HTML allowed ('' if none)
         'choices': ['a', 'b', 'c', 'd'],     # [] for writing questions
         'correct': 2,                        # 1-based index into choices
         'is_writing': False},
    ]

Passages for the file's sections are wiped and recreated on every run;
questions are update_or_create'd (choices rebuilt), so re-running is safe.
"""
import importlib.util
import os

from django.core.management.base import BaseCommand, CommandError

from exam.models import Exam, ExamPassage, ExamQuestion, ExamChoice


class Command(BaseCommand):
    help = 'Load a mock exam section (EXAM_META + PASSAGES + QUESTIONS) from a data file'

    def add_arguments(self, parser):
        parser.add_argument('datafile', help='Path to the data .py file')
        parser.add_argument('--dry-run', action='store_true', help='Preview without saving')

    def _load_module(self, path):
        if not os.path.isfile(path):
            raise CommandError(f'Data file not found: {path}')
        spec = importlib.util.spec_from_file_location('_mock_exam_data', path)
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
        except Exception as exc:  # noqa: BLE001
            raise CommandError(f'Failed to import {path}: {exc}')
        for attr in ('EXAM_META', 'QUESTIONS'):
            if not hasattr(module, attr):
                raise CommandError(f'{path} must define {attr}')
        return module

    def handle(self, **options):
        module = self._load_module(options['datafile'])
        meta = module.EXAM_META
        passages = getattr(module, 'PASSAGES', [])
        questions = module.QUESTIONS
        dry = options['dry_run']
        tag = '[DRY RUN] ' if dry else ''

        sections = sorted({q['section'] for q in questions} | {p['section'] for p in passages})
        self.stdout.write(f'{tag}Exam: {meta["title"]} (#{meta["exam_number"]}) — sections: {", ".join(sections)}')
        self.stdout.write(f'{tag}  {len(passages)} passages, {len(questions)} questions')

        if dry:
            for q in questions:
                text = (q.get('question_text') or '').replace('\n', ' ')[:60]
                self.stdout.write(f'  Q{q["number"]:>3} [{q["section"]}] {text}')
            self.stdout.write(f'{tag}Nothing saved. Remove --dry-run to load.')
            return

        exam, created = Exam.objects.update_or_create(
            exam_number=meta['exam_number'],
            language=meta.get('language', 'korean'),
            defaults={k: v for k, v in meta.items() if k not in ('exam_number', 'language')},
        )
        self.stdout.write(self.style.SUCCESS(f'  {"Created" if created else "Updated"} exam (id={exam.id})'))

        # Rebuild passages for the sections present in this file.
        deleted, _ = ExamPassage.objects.filter(exam=exam, section__in=sections).delete()
        if deleted:
            self.stdout.write(f'  Cleared {deleted} old passages')
        for p in passages:
            ExamPassage.objects.create(
                exam=exam,
                section=p['section'],
                question_from=p['from'],
                question_to=p['to'],
                text=p.get('text', ''),
            )
        self.stdout.write(f'  Created {len(passages)} passages')

        created_q = updated_q = 0
        for q in questions:
            choices = q.get('choices', [])
            correct = q.get('correct')
            is_writing = q.get('is_writing', False)
            if not is_writing:
                if len(choices) != 4:
                    raise CommandError(f'Q{q["number"]} [{q["section"]}]: needs exactly 4 choices')
                if correct not in (1, 2, 3, 4):
                    raise CommandError(f'Q{q["number"]} [{q["section"]}]: correct must be 1–4')

            question, q_created = ExamQuestion.objects.update_or_create(
                exam=exam,
                section=q['section'],
                number=q['number'],
                defaults={
                    'question_text': q.get('question_text', ''),
                    'is_writing': is_writing,
                },
            )
            if q_created:
                created_q += 1
            else:
                updated_q += 1
                question.choices.all().delete()
            for i, text in enumerate(choices, start=1):
                ExamChoice.objects.create(question=question, text=text, is_correct=(i == correct))

        self.stdout.write(self.style.SUCCESS(
            f'Done — questions created: {created_q}, updated: {updated_q}'
        ))
