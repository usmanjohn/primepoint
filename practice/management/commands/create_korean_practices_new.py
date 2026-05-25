from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

from .korean_questions import (
    QUESTIONS_18,
    QUESTIONS_19,
    QUESTIONS_20,
    QUESTIONS_21,
    QUESTIONS_22,
    QUESTIONS_23,
    QUESTIONS_24,
    QUESTIONS_25,
    QUESTIONS_26,
    QUESTIONS_27,
    QUESTIONS_28,
    QUESTIONS_29,
    QUESTIONS_30,
    QUESTIONS_31    
    )

PRACTICES = [
    {
        'title': '18-dars',
        'description': "amaliy test.",
        'questions': QUESTIONS_18,
    },
    {
        'title': '19-dars',
        'description': "amaliy test.",
        'questions': QUESTIONS_19,
    },
    {
        'title': '20-dars',
        'description': "amaliy test.",
        'questions': QUESTIONS_20,
    },
    {
        'title': '21-dars',
        'description': "amaliy test.",
        'questions': QUESTIONS_21,
    },
    {
        'title': '22-dars',
        'description': "amaliy test.",
        'questions': QUESTIONS_22,
    },
    {
        'title': '23-dars',
        'description': "amaliy test.",
        'questions': QUESTIONS_23,
    },
    {
        'title': '24-dars',
        'description': "amaliy test.",
        'questions': QUESTIONS_24,
    },
    {
        'title': '25-dars',
        'description': "amaliy test.",
        'questions': QUESTIONS_25,
    },
    {
        'title': '26-dars',
        'description': "amaliy test.",
        'questions': QUESTIONS_26,
    },
    {
        'title': '27-dars',
        'description': "amaliy test.",
        'questions': QUESTIONS_27,
    },
    {
        'title': '28-dars',
        'description': "amaliy test.",
        'questions': QUESTIONS_28,
    },
    {
        'title': '29-dars',
        'description': "amaliy test.",
        'questions': QUESTIONS_29,
    },
    {
        'title': '30-dars',
        'description': "amaliy test.",
        'questions': QUESTIONS_30,
    },
    {
        'title': '31-dars',
        'description': "amaliy test.",
        'questions': QUESTIONS_31,
    }

]

class Command(BaseCommand):
    help = 'Create Korean grammar particle practice tests (lessons 5–9)'

    def add_arguments(self, parser):
        parser.add_argument('--master', required=True, help='Username of the master to assign practices to')

    def handle(self, *args, **options):
        try:
            user = User.objects.get(username=options['master'])
        except User.DoesNotExist:
            raise CommandError(f"User '{options['master']}' not found.")

        try:
            master = Master.objects.get(profile__user=user)
        except Master.DoesNotExist:
            raise CommandError(f"No Master profile found for user '{options['master']}'.")

        subject, _ = Subject.objects.get_or_create(
            name='한국어',
            defaults={'description': '한국어 문법 및 어휘 연습'},
        )

        for practice_data in PRACTICES:
            practice, created = Practice.objects.get_or_create(
                title=practice_data['title'],
                master=master,
                defaults={
                    'description': practice_data['description'],
                    'subject': subject,
                    'level': 'medium',
                    'is_free': True,
                    'is_published': True,
                    'is_available_for_all': True,
                    'pass_score': 60,
                    'max_attempts': 0,
                    'show_answers_after': True,
                },
            )

            if not created:
                self.stdout.write(self.style.WARNING(
                    f"Practice '{practice.title}' already exists (id={practice.pk}). Skipping."
                ))
                continue

            questions = practice_data['questions']
            for i, q in enumerate(questions, start=1):
                question = PracticeQuestion.objects.create(
                    practice=practice,
                    question_text=q['text'],
                    explanation=q['explanation'],
                    order=i,
                    points=1,
                )
                for choice_text in q['choices']:
                    PracticeChoice.objects.create(
                        question=question,
                        text=choice_text,
                        is_correct=(choice_text == q['correct']),
                    )

            self.stdout.write(self.style.SUCCESS(
                f"Created '{practice.title}' with {len(questions)} questions (id={practice.pk})."
            ))
