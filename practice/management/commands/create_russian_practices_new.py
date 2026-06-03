from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

from .russian_questions import (
    QUESTIONS_chast_4,
    QUESTIONS_chast_5,
    QUESTIONS_chast_6,
    QUESTIONS_chast_7,
    QUESTIONS_chast_8,
    QUESTIONS_chast_9,
    QUESTIONS_chast_10,
    QUESTIONS_chast_11,
    QUESTIONS_chast_12,
    QUESTIONS_chast_13,
    QUESTIONS_chast_14,
    QUESTIONS_chast_15,
    QUESTIONS_chast_16,
    QUESTIONS_chast_17,
    QUESTIONS_chast_18,
    QUESTIONS_chast_19,
    QUESTIONS_chast_20)

PRACTICES = [
    {
        'title': 'Часть 4: Приветствия и первые фразы знакомства',
        'description': 'Практика базовых приветствий и вежливых фраз для общения в офисе и повседневной жизни.',
        'questions': QUESTIONS_chast_4,
    },
    {
        'title': 'Часть 5: Личные местоимения и базовые вопросы',
        'description': 'Amaliy test. Личные местоимения (я, ты, он, она) и вопросительные слова (кто, что, где, как).',
        'questions': QUESTIONS_chast_5,
    },
    {
        'title': 'Часть 6: Существительные: Грамматический род',
        'description': 'Определение мужского, женского и среднего рода существительных и согласование с прилагательными.',
        'questions': QUESTIONS_chast_6,
    },
    {
        'title': 'Часть 7: Существительные: Единственное и множественное число',
        'description': 'Amaliy test. Образование множественного числа существительных, включая слова-исключения.',
        'questions': QUESTIONS_chast_7,
    },
    {
        'title': 'Часть 8: Числительные от 1 до 20 и базовый счет',
        'description': 'Практика количественных числительных и базовая математика на русском языке.',
        'questions': QUESTIONS_chast_8,
    },
    {
        'title': 'Часть 9: Глагол "Быть" в настоящем, прошедшем и будущем времени',
        'description': 'Amaliy test. Использование глагола "быть" во всех временах и формах.',
        'questions': QUESTIONS_chast_9,
    },
    {
        'title': 'Часть 10: Простые конструкции: "У меня есть..."',
        'description': 'Конструкции обладания с предлогом "У" и правильное использование родительного падежа.',
        'questions': QUESTIONS_chast_10,
    },
    {
        'title': 'Смешанный тест: Фаза 1 (Части 1-10)',
        'description': 'Универсальный amaliy test для проверки знаний первой фазы: алфавит, база и первые фразы.',
        'questions': QUESTIONS_mixed_chapter_1,
    },
    {
        'title': 'Часть 11: Настоящее время глаголов: Первое спряжение',
        'description': 'Практика глаголов первого спряжения (работать, читать, делать, понимать).',
        'questions': QUESTIONS_chast_11,
    },
    {
        'title': 'Часть 12: Настоящее время глаголов: Второе спряжение',
        'description': 'Amaliy test. Спряжение глаголов на -ить (говорить, смотреть, звонить, помнить).',
        'questions': QUESTIONS_chast_12,
    },
    {
        'title': 'Часть 13: Введение в падежную систему: Общий обзор',
        'description': 'Базовое понимание падежей: именительный, винительный, предложный, дательный, творительный, родительный.',
        'questions': QUESTIONS_chast_13,
    },
    {
        'title': 'Часть 14: Предложный падеж: Местоположение (Где?)',
        'description': 'Amaliy test. Использование предлогов В и НА с предложным падежом.',
        'questions': QUESTIONS_chast_14,
    },
    {
        'title': 'Часть 15: Лексика: Мой дом и комнаты',
        'description': 'Словарный запас по теме мебели, комнат и предметов быта.',
        'questions': QUESTIONS_chast_15,
    },
    {
        'title': 'Часть 16: Винительный падеж: Неодушевленные существительные (Что?)',
        'description': 'Винительный падеж для неодушевленных объектов (книгу, воду, код, проект).',
        'questions': QUESTIONS_chast_16,
    },
    {
        'title': 'Часть 17: Винительный падеж: Одушевленные существительные (Кого?)',
        'description': 'Amaliy test. Винительный падеж для людей и животных (брата, коллегу, менеджера).',
        'questions': QUESTIONS_chast_17,
    },
    {
        'title': 'Часть 18: Лексика: Семья и родственники',
        'description': 'Словарный запас по теме семьи и поколений (родители, братья, сёстры, бабушка, дедушка).',
        'questions': QUESTIONS_chast_18,
    },
    {
        'title': 'Часть 19: Притяжательные местоимения (Мой, твой, наш)',
        'description': 'Согласование притяжательных местоимений с существительными в роде и числе.',
        'questions': QUESTIONS_chast_19,
    },
    {
        'title': 'Часть 20: Прилагательные: Согласование в роде и числе',
        'description': 'Amaliy test. Правила согласования базовых прилагательных (большой, новый, старый, хороший).',
        'questions': QUESTIONS_chast_20,
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