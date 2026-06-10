from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

from .russian_questions import (
    QUESTIONS_chast_51,
QUESTIONS_chast_52,
QUESTIONS_chast_53,
QUESTIONS_chast_54,
QUESTIONS_chast_55,
QUESTIONS_chast_56,
QUESTIONS_chast_57,
QUESTIONS_chast_58,
QUESTIONS_chast_59,
QUESTIONS_chast_60,
QUESTIONS_mixed_parts_51_60


)
PRACTICES = [
    {
        'title': 'Часть 51: Глаголы движения с приставками: По-, При-, У-',
        'description': 'Практика использования приставок для обозначения прибытия, ухода и начала движения.',
        'questions': QUESTIONS_chast_51,
    },
    {
        'title': 'Часть 52: Глаголы движения с приставками: В-, Вы-, Под-, От-',
        'description': 'Amaliy test. Использование приставок для входа, выхода, приближения и отдаления.',
        'questions': QUESTIONS_chast_52,
    },
    {
        'title': 'Часть 53: Глаголы движения с приставками: Пере-, До-, Про-, За-',
        'description': 'Глаголы движения для пересечения, достижения цели, прохождения мимо и попутного захода.',
        'questions': QUESTIONS_chast_53,
    },
    {
        'title': 'Часть 54: Лексика: Путешествия, вокзалы и аэропорты',
        'description': 'Словарный запас для путешественников: регистрация, багаж, посадочный талон, рейс и таможня.',
        'questions': QUESTIONS_chast_54,
    },
    {
        'title': 'Часть 55: Неопределенные местоимения (Кто-то, что-нибудь)',
        'description': 'Amaliy test. Разница между суффиксами "-то" (конкретное, но неизвестное) и "-нибудь" (любое).',
        'questions': QUESTIONS_chast_55,
    },
    {
        'title': 'Часть 56: Отрицательные местоимения (Никто, ничто)',
        'description': 'Использование двойного отрицания, а также предлогов с отрицательными местоимениями (ни у кого, ни с кем).',
        'questions': QUESTIONS_chast_56,
    },
    {
        'title': 'Часть 57: Падежные формы множественного числа: Именительный и Родительный',
        'description': 'Образование множественного числа существительных в именительном и родительном падежах (включая исключения).',
        'questions': QUESTIONS_chast_57,
    },
    {
        'title': 'Часть 58: Падежные формы множественного числа: Дательный, Винительный, Творительный, Предложный',
        'description': 'Amaliy test. Склонение существительных во множественном числе по всем косвенным падежам.',
        'questions': QUESTIONS_chast_58,
    },
    {
        'title': 'Часть 59: Численные сочетания с существительными во множественном числе',
        'description': 'Правила согласования числительных (1, 2-4, 5+) с существительными в правильном падеже.',
        'questions': QUESTIONS_chast_59,
    },
    {
        'title': 'Часть 60: Лексика: Здоровье, тело и визит к врачу',
        'description': 'Словарный запас: названия частей тела, симптомы болезней (кашель, насморк), визит в больницу и аптеку.',
        'questions': QUESTIONS_chast_60,
    },
    {
        'title': 'Смешанный тест: Фаза 4 (Части 51-60)',
        'description': 'Глобальная проверка Фазы 4: глаголы движения с приставками, сложные местоимения, множественное число и лексика.',
        'questions': QUESTIONS_mixed_parts_51_60,
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