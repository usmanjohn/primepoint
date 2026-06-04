from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

from .russian_questions import (
    QUESTIONS_chast_21,
    QUESTIONS_chast_22,
    QUESTIONS_chast_23,
    QUESTIONS_chast_24,
    QUESTIONS_chast_25,
    QUESTIONS_chast_26,
    QUESTIONS_chast_27,
    QUESTIONS_chast_28,
    QUESTIONS_chast_29,
    QUESTIONS_chast_30,
    QUESTIONS_mixed_parts_20_29)

PRACTICES = [
    {
        'title': 'Часть 21: Родительный падеж: Отрицание',
        'description': 'Практика использования родительного падежа с конструкцией "у меня нет...".',
        'questions': QUESTIONS_chast_21,
    },
    {
        'title': 'Часть 22: Родительный падеж: Принадлежность и предлог "Из"',
        'description': 'Amaliy test. Выражение принадлежности и использование предлогов "из" и "от".',
        'questions': QUESTIONS_chast_22,
    },
    {
        'title': 'Часть 23: Числительные от 20 до 100 и подсчет предметов',
        'description': 'Практика круглых чисел и согласования слов "год/года/лет" с числительными.',
        'questions': QUESTIONS_chast_23,
    },
    {
        'title': 'Часть 24: Лексика: Еда, напитки и заказ в кафе',
        'description': 'Словарный запас для ресторанов: меню, счёт, названия блюд и столовых приборов.',
        'questions': QUESTIONS_chast_24,
    },
    {
        'title': 'Часть 25: Дательный падеж: Косвенный объект',
        'description': 'Amaliy test. Использование дательного падежа (кому? чему?) с глаголами звонить, помогать, отправить.',
        'questions': QUESTIONS_chast_25,
    },
    {
        'title': 'Часть 26: Дательный падеж: Выражение возраста и состояния',
        'description': 'Конструкции "мне 25 лет", "мне холодно", "ему нужно" и другие безличные предложения.',
        'questions': QUESTIONS_chast_26,
    },
    {
        'title': 'Часть 27: Творительный падеж: Инструменты и профессия',
        'description': 'Практика творительного падежа для профессий (работать кем?) и инструментов (писать чем?).',
        'questions': QUESTIONS_chast_27,
    },
    {
        'title': 'Часть 28: Творительный падеж: Совместность с предлогом "С"',
        'description': 'Amaliy test. Использование предлога "с" (с молоком, с друзьями, со мной).',
        'questions': QUESTIONS_chast_28,
    },
    {
        'title': 'Часть 29: Наречия времени и частотности',
        'description': 'Словарный запас: обычно, никогда, часто, редко, недавно, скоро и другие наречия.',
        'questions': QUESTIONS_chast_29,
    },
    {
        'title': 'Смешанный тест: Фаза 2 (Части 20-29)',
        'description': 'Глобальная проверка: падежи (родительный, дательный, творительный), числительные, прилагательные и лексика.',
        'questions': QUESTIONS_mixed_parts_20_29,
    },
    {
        'title': 'Часть 30: Прошедшее время глаголов',
        'description': 'Образование и употребление глаголов в прошедшем времени с учетом рода и числа (делал, делала, делали).',
        'questions': QUESTIONS_chast_30,
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