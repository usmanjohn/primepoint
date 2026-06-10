from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

from .russian_questions import (
    QUESTIONS_chast_61, QUESTIONS_chast_62, QUESTIONS_chast_63, QUESTIONS_chast_64, QUESTIONS_chast_65
)
PRACTICES = [
    {
        'title': 'Часть 61: Действительные причастия',
        'description': 'Образование и использование действительных причастий настоящего и прошедшего времени (пишущий, сделавший).',
        'questions': QUESTIONS_chast_61,
    },
    {
        'title': 'Часть 62: Страдательные причастия',
        'description': 'Практика страдательных причастий (созданный, читаемый) для описания предметов, над которыми совершается действие.',
        'questions': QUESTIONS_chast_62,
    },
    {
        'title': 'Часть 63: Краткие причастия и пассивный залог',
        'description': 'Использование кратких форм страдательных причастий (написан, установлена, закрыто) для образования пассивного залога.',
        'questions': QUESTIONS_chast_63,
    },
    {
        'title': 'Часть 64: Деепричастия несовершенного вида (Что делая?)',
        'description': 'Amaliy test. Выражение дополнительных параллельных действий с помощью деепричастий (работая, читая, проверяя).',
        'questions': QUESTIONS_chast_64,
    },
    {
        'title': 'Часть 65: Деепричастия совершенного вида (Что сделав?)',
        'description': 'Amaliy test. Обозначение завершенных действий, предшествующих главному глаголу (написав, закончив, вернувшись).',
        'questions': QUESTIONS_chast_65,
    }
]

class Command(BaseCommand):
    help = 'Create Russian grammar particle practice tests'

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
            name='Russian',
            defaults={'description': 'Russian grammar and vocabulary practice'},
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