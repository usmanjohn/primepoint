from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

from .russian_questions import (
    QUESTIONS_chast_43,
    QUESTIONS_chast_44,
    QUESTIONS_chast_45,
    QUESTIONS_chast_46,
    QUESTIONS_chast_47,
    QUESTIONS_chast_48,
    QUESTIONS_chast_49,
    QUESTIONS_chast_50,
    QUESTIONS_mixed_parts_31_50)

PRACTICES = [
    {
        'title': 'Часть 43: Модальные слова: Должен, нужно, можно, нельзя',
        'description': 'Практика выражения долженствования, необходимости, разрешения и запретов в различных ситуациях.',
        'questions': QUESTIONS_chast_43,
    },
    {
        'title': 'Часть 44: Лексика: Покупки, магазины и одежда',
        'description': 'Amaliy test. Словарный запас для покупок: размеры, примерочные, касса, скидки и названия элементов одежды.',
        'questions': QUESTIONS_chast_44,
    },
    {
        'title': 'Часть 45: Сложные предлоги места (Под, над, за, перед)',
        'description': 'Использование пространственных предлогов с винительным (направление) и творительным (местоположение) падежами.',
        'questions': QUESTIONS_chast_45,
    },
    {
        'title': 'Часть 46: Порядковые числительные и обозначение дат',
        'description': 'Amaliy test. Образование порядковых числительных и правильное построение дат ("какого числа?", "в каком году?").',
        'questions': QUESTIONS_chast_46,
    },
    {
        'title': 'Часть 47: Выражение времени: Который час? В каком часу?',
        'description': 'Использование предлогов и падежей для указания точного времени (половина, четверть, "без двадцати пять").',
        'questions': QUESTIONS_chast_47,
    },
    {
        'title': 'Часть 48: Лексика: Рабочий день и распорядок дня',
        'description': 'Amaliy test. Описание повседневных дел программиста и офисной рутины от утреннего подъёма до конца рабочего дня.',
        'questions': QUESTIONS_chast_48,
    },
    {
        'title': 'Часть 49: Сослагательное наклонение (Частица "Бы")',
        'description': 'Конструирование гипотетических условий, желаний и вежливых просьб с помощью частицы "бы" и прошедшего времени.',
        'questions': QUESTIONS_chast_49,
    },
    {
        'title': 'Часть 50: Повелительное наклонение: Просьбы и приказы',
        'description': 'Amaliy test. Образование форм императива для "ты" и "вы" в утвердительных и отрицательных предложениях.',
        'questions': QUESTIONS_chast_50,
    },
    {
        'title': 'Смешанный тест: Фаза 3 (Части 31-50)',
        'description': 'Глобальный amaliy test для закрепления всей третьей фазы: от видов глагола и глаголов движения до сослагательного наклонения.',
        'questions': QUESTIONS_mixed_parts_31_50,
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