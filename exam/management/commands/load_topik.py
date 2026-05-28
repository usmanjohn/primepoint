"""
Load TOPIK exam questions from exam/data/topik_questions.py

Edit exam/data/topik_questions.py, then run:
    python manage.py load_topik
    python manage.py load_topik --clear      # wipe questions first, then reload
    python manage.py load_topik --dry-run    # preview without saving
"""
from django.core.management.base import BaseCommand
from exam.models import Exam, ExamQuestion, ExamChoice
from exam.data.topik_questions import EXAM_META, QUESTIONS


class Command(BaseCommand):
    help = 'Bulk-create TOPIK exam questions from exam/data/topik_questions.py'

    def add_arguments(self, parser):
        parser.add_argument('--clear', action='store_true', help='Delete existing questions for this exam first')
        parser.add_argument('--dry-run', action='store_true', help='Show what would be created without saving')

    def handle(self, **options):
        dry = options['dry_run']
        tag = '[DRY RUN] ' if dry else ''

        # ── Exam ─────────────────────────────────────────────────
        self.stdout.write(f'{tag}Exam: {EXAM_META["title"]} (#{EXAM_META["exam_number"]})')

        if not dry:
            exam, created = Exam.objects.update_or_create(
                exam_number=EXAM_META['exam_number'],
                language=EXAM_META['language'],
                defaults={k: v for k, v in EXAM_META.items() if k not in ('exam_number', 'language')},
            )
            self.stdout.write(self.style.SUCCESS(f'  {"Created" if created else "Updated"} exam (id={exam.id})'))
        else:
            exam = None

        # ── Clear ────────────────────────────────────────────────
        if options['clear']:
            if not dry:
                deleted, _ = ExamQuestion.objects.filter(exam=exam).delete()
                self.stdout.write(f'  Cleared {deleted} existing questions')
            else:
                self.stdout.write(f'{tag}  Would clear existing questions')

        # ── Questions ─────────────────────────────────────────────
        created_count = updated_count = skipped_count = 0

        for q in QUESTIONS:
            section    = q.get('section', 'reading')
            number     = q.get('number')
            passage    = q.get('passage', '')
            q_text     = q.get('question_text', '')
            is_writing = q.get('is_writing', False)
            correct    = q.get('correct', '')
            choices    = q.get('choices', [])

            if not number or not q_text:
                self.stdout.write(self.style.WARNING('  Skipping entry: missing number or question_text'))
                skipped_count += 1
                continue

            short = q_text[:55].replace('\n', ' ')
            self.stdout.write(f'{tag}  Q{number:>3} [{section}] {short}…')

            if not dry:
                question, q_created = ExamQuestion.objects.update_or_create(
                    exam=exam,
                    section=section,
                    number=number,
                    defaults={
                        'passage': passage,
                        'question_text': q_text,
                        'is_writing': is_writing,
                    },
                )
                if q_created:
                    created_count += 1
                else:
                    updated_count += 1
                    question.choices.all().delete()

                for text in choices:
                    if text:
                        ExamChoice.objects.create(
                            question=question,
                            text=text,
                            is_correct=(text == correct),
                        )

        # ── Summary ──────────────────────────────────────────────
        self.stdout.write('')
        if not dry:
            self.stdout.write(self.style.SUCCESS(
                f'Done — created: {created_count}, updated: {updated_count}, skipped: {skipped_count}'
            ))
        else:
            self.stdout.write(f'{tag}Would process {len(QUESTIONS)} questions. Remove --dry-run to save.')
