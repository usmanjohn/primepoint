"""
Load exam questions from a JSON file into the database.

Usage:
    python manage.py load_exam exam/data/topik_reading_sample.json

Options:
    --clear     Delete all existing questions for this exam before loading.
    --dry-run   Print what would be created without saving anything.

JSON format:  see exam/data/topik_reading_sample.json
"""
import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from exam.models import Exam, ExamQuestion, ExamChoice


class Command(BaseCommand):
    help = 'Bulk-create exam questions from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON data file')
        parser.add_argument('--clear', action='store_true', help='Delete existing questions for this exam first')
        parser.add_argument('--dry-run', action='store_true', help='Show what would be created without saving')

    def handle(self, **options):
        path = Path(options['json_file'])
        if not path.exists():
            raise CommandError(f'File not found: {path}')

        data = json.loads(path.read_text(encoding='utf-8'))
        exam_data = data.get('exam', {})
        questions_data = data.get('questions', [])

        dry = options['dry_run']
        prefix = '[DRY RUN] ' if dry else ''

        # ── Find or create the exam ──────────────────────────
        exam_defaults = {
            'title':               exam_data.get('title', 'TOPIK II'),
            'language':            exam_data.get('language', 'korean'),
            'listening_minutes':   exam_data.get('listening_minutes', 60),
            'reading_minutes':     exam_data.get('reading_minutes', 70),
            'writing_minutes':     exam_data.get('writing_minutes', 50),
            'allow_audio_replay':  exam_data.get('allow_audio_replay', True),
            'allow_audio_pause':   exam_data.get('allow_audio_pause', True),
            'is_published':        exam_data.get('is_published', False),
        }
        exam_number = exam_data.get('exam_number', 0)

        self.stdout.write(f'{prefix}Exam: {exam_defaults["title"]} (#{exam_number})')

        if not dry:
            exam, created = Exam.objects.update_or_create(
                exam_number=exam_number,
                language=exam_defaults['language'],
                defaults=exam_defaults,
            )
            action = 'Created' if created else 'Updated'
            self.stdout.write(self.style.SUCCESS(f'  {action} exam (id={exam.id})'))
        else:
            exam = None

        # ── Optionally clear existing questions ──────────────
        if options['clear'] and not dry:
            deleted, _ = ExamQuestion.objects.filter(exam=exam).delete()
            self.stdout.write(f'  Cleared {deleted} existing questions')
        elif options['clear'] and dry:
            self.stdout.write('[DRY RUN]  Would clear existing questions')

        # ── Load questions ───────────────────────────────────
        created_q = 0
        updated_q = 0
        skipped_q = 0

        for q_data in questions_data:
            section   = q_data.get('section', 'reading')
            number    = q_data.get('number')
            passage   = q_data.get('passage', '')
            q_text    = q_data.get('question_text', '')
            is_writing = q_data.get('is_writing', False)
            choices_data = q_data.get('choices', [])

            if not number or not q_text:
                self.stdout.write(self.style.WARNING(f'  Skipping entry with missing number or question_text'))
                skipped_q += 1
                continue

            self.stdout.write(f'{prefix}  Q{number} [{section}] {q_text[:60]}…')

            if not dry:
                question, q_created = ExamQuestion.objects.update_or_create(
                    exam=exam,
                    section=section,
                    number=number,
                    defaults={
                        'passage':    passage,
                        'question_text': q_text,
                        'is_writing': is_writing,
                    },
                )
                if q_created:
                    created_q += 1
                else:
                    updated_q += 1
                    # Clear old choices so we re-create them cleanly
                    question.choices.all().delete()

                for c_data in choices_data:
                    text       = c_data.get('text', '')
                    is_correct = c_data.get('is_correct', False)
                    if text:
                        ExamChoice.objects.create(
                            question=question,
                            text=text,
                            is_correct=is_correct,
                        )
            else:
                self.stdout.write(f'      choices: {[c.get("text","") for c in choices_data]}')

        # ── Summary ──────────────────────────────────────────
        if not dry:
            self.stdout.write('')
            self.stdout.write(self.style.SUCCESS(
                f'Done. Questions created: {created_q}, updated: {updated_q}, skipped: {skipped_q}'
            ))
        else:
            self.stdout.write('')
            self.stdout.write(f'[DRY RUN] Would process {len(questions_data)} questions. Run without --dry-run to save.')
