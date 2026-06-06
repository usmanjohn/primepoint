from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

from .russian_questions import (
    QUESTIONS_chast_31,
    QUESTIONS_chast_32,
    QUESTIONS_chast_33,
    QUESTIONS_chast_34,
    QUESTIONS_chast_35,
    QUESTIONS_chast_36,
    QUESTIONS_chast_37,
    QUESTIONS_chast_38,
    QUESTIONS_chast_39,
    QUESTIONS_chast_40,
    QUESTIONS_chast_41,
    QUESTIONS_chast_42,
    QUESTIONS_mixed_parts_31_42)

PRACTICES = [
    {
        'title': 'Часть 31: Виды глагола (Введение)',
        'description': 'Практика использования совершенного и несовершенного вида глаголов (решать/решить, писать/написать).',
        'questions': QUESTIONS_chast_31,
    },
    {
        'title': 'Часть 32: Практика видов глагола в прошедшем времени',
        'description': 'Amaliy test. Выбор правильного вида глагола в прошедшем времени в зависимости от результата или процесса.',
        'questions': QUESTIONS_chast_32,
    },
    {
        'title': 'Часть 33: Будущее время: Сложное и простое',
        'description': 'Разница между "я буду делать" (процесс) и "я сделаю" (результат) в будущем времени.',
        'questions': QUESTIONS_chast_33,
    },
    {
        'title': 'Часть 34: Глаголы движения: Идти / Ходить',
        'description': 'Amaliy test. Использование глаголов движения пешком (однонаправленные и разнонаправленные).',
        'questions': QUESTIONS_chast_34,
    },
    {
        'title': 'Часть 35: Глаголы движения: Ехать / Ездить',
        'description': 'Практика использования глаголов движения на транспорте в разных временах и ситуациях.',
        'questions': QUESTIONS_chast_35,
    },
    {
        'title': 'Часть 36: Лексика: Городской транспорт и направления',
        'description': 'Словарный запас: названия транспорта, остановки, ориентирование в городе (направо, налево, прямо).',
        'questions': QUESTIONS_chast_36,
    },
    {
        'title': 'Часть 37: Указательные местоимения (Этот, тот)',
        'description': 'Amaliy test. Согласование местоимений "этот", "эта", "это", "эти" с существительными в разных падежах.',
        'questions': QUESTIONS_chast_37,
    },
    {
        'title': 'Часть 38: Сравнительная степень прилагательных и наречий',
        'description': 'Образование и использование сравнительной степени (лучше, хуже, больше, быстрее, сложнее).',
        'questions': QUESTIONS_chast_38,
    },
    {
        'title': 'Часть 39: Превосходная степень прилагательных',
        'description': 'Практика превосходной степени с использованием слова "самый" и суффиксов "-ейш- / -айш-".',
        'questions': QUESTIONS_chast_39,
    },
    {
        'title': 'Часть 40: Лексика: Погода, времена года и климат',
        'description': 'Amaliy test. Словарный запас для описания погоды (дождь, снег, жарко, холодно, ясно) и времен года.',
        'questions': QUESTIONS_chast_40,
    },
    {
        'title': 'Часть 41: Возвратные глаголы (-ся / -сь)',
        'description': 'Спряжение возвратных глаголов (учиться, встречаться, начинаться) в настоящем и прошедшем времени.',
        'questions': QUESTIONS_chast_41,
    },
    {
        'title': 'Часть 42: Краткие формы прилагательных',
        'description': 'Использование кратких прилагательных состояний: готов, занят, свободен, должен, прав, рад.',
        'questions': QUESTIONS_chast_42,
    },
    {
        'title': 'Смешанный тест: Фаза 3 (Части 31-42)',
        'description': 'Глобальная проверка Фазы 3: виды глаголов, глаголы движения, степени сравнения, возвратные глаголы и лексика.',
        'questions': QUESTIONS_mixed_parts_31_42,
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