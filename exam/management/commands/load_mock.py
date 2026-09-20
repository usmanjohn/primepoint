"""
Load a mock exam (modules + passages + questions) from a Python data file.

Usage:
    python manage.py load_mock exam/data/mock1_reading.py
    python manage.py load_mock exam/data/sat1_rw1.py --expect-questions=27
    python manage.py load_mock exam/data/sat1_math1.py --dry-run

The data file defines:

    EXAM_META = {              # identifies / creates the Exam row
        'title': 'Digital SAT — PrimePoint Mock 1',
        'language': 'english',
        'exam_format': 'sat',          # 'topik' (default) or 'sat'
        'exam_number': 201,
        'is_published': True,
    }

    MODULES = [                # one timed run of questions each (ExamModule)
        {'code': 'rw1', 'kind': 'rw', 'stage': 1, 'order': 1,
         'label': 'Reading and Writing — Module 1', 'label_uz': 'Oʻqish va yozish — 1-modul',
         'minutes': 32, 'route_threshold': 18},
        {'code': 'rw2h', 'kind': 'rw', 'stage': 2, 'difficulty': 'hard', 'order': 1,
         'label': '...', 'minutes': 32, 'break_minutes': 10},
    ]

    PASSAGES = [               # optional: one box shared by a RANGE of questions
        {'section': 'reading', 'from': 1, 'to': 3, 'text': '<b>※ [1~3] ...</b>'},
    ]

    QUESTIONS = [
        {'section': 'rw1', 'number': 1,
         'passage': '<p>...</p>',             # optional: this question's own stimulus
         'question_text': '...',              # HTML allowed
         'choices': ['a', 'b', 'c', 'd'],     # omit for grid-in / essay
         'correct': 2,                        # 1-based index into choices
         'answer_type': 'mcq',                # 'mcq' | 'grid' | 'essay'
         'accepted': ['2/3', '0.667'],        # grid-in only
         'skill': 'Words in Context',         # domain, for the score report
         'difficulty': 'medium',
         'explanation': 'Uzbekcha izoh...'},  # required on SAT exams
    ]

Modules are update_or_create'd. Passages for the file's sections are wiped and
rebuilt every run; questions are update_or_create'd with their choices, so
re-running a file is always safe.
"""
import importlib.util
import os

from django.core.management.base import BaseCommand, CommandError

from exam.gridin import parse as parse_grid
from exam.models import Exam, ExamModule, ExamPassage, ExamQuestion, ExamChoice


class Command(BaseCommand):
    help = 'Load a mock exam module (EXAM_META + MODULES + QUESTIONS) from a data file'

    def add_arguments(self, parser):
        parser.add_argument('datafile', help='Path to the data .py file')
        parser.add_argument('--dry-run', action='store_true', help='Preview without saving')
        parser.add_argument('--expect-questions', type=int, default=None,
                            help='Refuse the file unless it holds exactly this many questions')

    # ── loading ────────────────────────────────────────────────────────
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

    # ── the gate ───────────────────────────────────────────────────────
    def _validate(self, meta, modules, questions):
        """Refuse anything that would ship a broken exam. Loud, before any write."""
        errors = []
        is_sat = meta.get('exam_format', 'topik') == 'sat'
        codes = {m['code'] for m in modules}

        for m in modules:
            if m.get('stage') == 2 and not m.get('difficulty'):
                errors.append(f"module {m['code']}: a stage-2 module needs difficulty easy/hard")

        seen = set()
        for q in questions:
            where = f"Q{q.get('number')} [{q.get('section')}]"
            section = q.get('section')
            if modules and section not in codes:
                # Only a warning: a file may load questions for a module another
                # file in the same mock defines.
                self.stdout.write(self.style.WARNING(
                    f'  {where}: section is not among this file\'s MODULES'))
            key = (section, q.get('number'))
            if key in seen:
                errors.append(f'{where}: duplicate question number')
            seen.add(key)

            answer_type = q.get('answer_type', 'essay' if q.get('is_writing') else 'mcq')
            if answer_type == 'mcq':
                choices = q.get('choices', [])
                if len(choices) != 4:
                    errors.append(f'{where}: needs exactly 4 choices, got {len(choices)}')
                if q.get('correct') not in (1, 2, 3, 4):
                    errors.append(f'{where}: correct must be 1–4')
                if len(set(choices)) != len(choices):
                    errors.append(f'{where}: two choices are identical')
            elif answer_type == 'grid':
                accepted = q.get('accepted', [])
                if not accepted:
                    errors.append(f'{where}: a grid-in needs at least one accepted answer')
                for value in accepted:
                    if parse_grid(value) is None:
                        errors.append(f'{where}: accepted answer {value!r} is not a legal entry')
                if q.get('choices'):
                    errors.append(f'{where}: a grid-in cannot have choices')

            if is_sat and answer_type != 'essay' and not q.get('explanation', '').strip():
                errors.append(f'{where}: every SAT question needs an Uzbek explanation')
            # A shuffled choice list makes "Choice B" meaningless, and the SAT
            # explanations quote the choice text anyway — catch the habit early.
            explanation = q.get('explanation', '')
            for bad in ('Choice A', 'Choice B', 'Choice C', 'Choice D', 'variant A)'):
                if bad in explanation:
                    errors.append(f'{where}: explanation cites a choice letter ({bad!r}) — quote the text')

        if errors:
            for e in errors:
                self.stdout.write(self.style.ERROR(f'  {e}'))
            raise CommandError(f'{len(errors)} problem(s) — nothing was saved.')

    # ── main ───────────────────────────────────────────────────────────
    def handle(self, **options):
        module = self._load_module(options['datafile'])
        meta = module.EXAM_META
        modules = getattr(module, 'MODULES', [])
        passages = getattr(module, 'PASSAGES', [])
        questions = module.QUESTIONS
        dry = options['dry_run']
        tag = '[DRY RUN] ' if dry else ''

        expected = options['expect_questions']
        if expected is not None and len(questions) != expected:
            raise CommandError(
                f'Expected {expected} questions, file holds {len(questions)} — nothing was saved.')

        sections = sorted({q['section'] for q in questions} | {p['section'] for p in passages})
        self.stdout.write(
            f'{tag}Exam: {meta["title"]} (#{meta["exam_number"]}, '
            f'{meta.get("exam_format", "topik")}) — sections: {", ".join(sections)}')
        self.stdout.write(f'{tag}  {len(modules)} modules, {len(passages)} passages, '
                          f'{len(questions)} questions')

        self._validate(meta, modules, questions)

        if dry:
            for q in questions:
                text = (q.get('question_text') or '').replace('\n', ' ')[:60]
                kind = q.get('answer_type', 'mcq')
                self.stdout.write(f'  Q{q["number"]:>3} [{q["section"]}] ({kind}) {text}')
            self.stdout.write(f'{tag}Nothing saved. Remove --dry-run to load.')
            return

        exam, created = Exam.objects.update_or_create(
            exam_number=meta['exam_number'],
            language=meta.get('language', 'korean'),
            defaults={k: v for k, v in meta.items() if k not in ('exam_number', 'language')},
        )
        self.stdout.write(self.style.SUCCESS(
            f'  {"Created" if created else "Updated"} exam (id={exam.id})'))

        for m in modules:
            ExamModule.objects.update_or_create(
                exam=exam, code=m['code'],
                defaults={
                    'kind': m['kind'],
                    'stage': m.get('stage', 1),
                    'difficulty': m.get('difficulty', ''),
                    'label': m['label'],
                    'label_uz': m.get('label_uz', ''),
                    'minutes': m.get('minutes', 30),
                    'order': m.get('order', 1),
                    'route_threshold': m.get('route_threshold'),
                    'break_minutes': m.get('break_minutes', 0),
                    'calculator': m.get('calculator', False),
                    'reference_sheet': m.get('reference_sheet', False),
                },
            )
        if modules:
            self.stdout.write(f'  Wrote {len(modules)} modules')

        deleted, _ = ExamPassage.objects.filter(exam=exam, section__in=sections).delete()
        if deleted:
            self.stdout.write(f'  Cleared {deleted} old passages')
        for p in passages:
            ExamPassage.objects.create(
                exam=exam, section=p['section'],
                question_from=p['from'], question_to=p['to'], text=p.get('text', ''),
            )
        # A question's own stimulus is a passage bound to that one number.
        inline = 0
        for q in questions:
            if q.get('passage'):
                ExamPassage.objects.create(
                    exam=exam, section=q['section'],
                    question_from=q['number'], question_to=q['number'], text=q['passage'],
                )
                inline += 1
        self.stdout.write(f'  Created {len(passages)} grouped + {inline} per-question passages')

        created_q = updated_q = 0
        for q in questions:
            answer_type = q.get('answer_type', 'essay' if q.get('is_writing') else 'mcq')
            question, q_created = ExamQuestion.objects.update_or_create(
                exam=exam, section=q['section'], number=q['number'],
                defaults={
                    'question_text': q.get('question_text', ''),
                    'is_writing': answer_type == 'essay',
                    'answer_type': answer_type,
                    'accepted_answers': '\n'.join(q.get('accepted', [])),
                    'explanation': q.get('explanation', ''),
                    'skill': q.get('skill', ''),
                    'difficulty': q.get('difficulty', ''),
                },
            )
            if q_created:
                created_q += 1
            else:
                updated_q += 1
                question.choices.all().delete()
            for i, text in enumerate(q.get('choices', []), start=1):
                ExamChoice.objects.create(
                    question=question, text=text, is_correct=(i == q.get('correct')))

        self.stdout.write(self.style.SUCCESS(
            f'Done — questions created: {created_q}, updated: {updated_q}'))
