# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

from .math_questions import test_math_1, test_math_2, test_math_3, test_math_4


PRACTICES = [
    {
        'title': 'Aralash matematika — 1-test (oʻrta)',
        'description': (
            'EKUB va EKUK, boʻlinish alomatlari, boʻluvchilar soni va yigʻindisi, '
            'oʻzaro tub sonlar, kasrlar ustida amallar hamda tezlik-vaqt-masofa '
            'masalalari. Har bir savol uchun toʻliq yechim izohi bor.'
        ),
        'level': 'medium',
        'questions': test_math_1,
    },
    {
        'title': 'Aralash matematika — 2-test (oʻrta)',
        'description': (
            'EKUB/EKUK amaliy masalalari, 8 va 12 ga boʻlinish alomatlari, '
            'boʻluvchilar yigʻindisi, kasrlarni taqqoslash va harakat masalalari.'
        ),
        'level': 'medium',
        'questions': test_math_2,
    },
    {
        'title': 'Aralash matematika — 3-test (qiyin)',
        'description': (
            'Qoldiqli EKUB/EKUK masalalari, boʻluvchilar mantigʻi, murakkab kasr '
            'ifodalari, oʻrtacha tezlik va poyezd masalalari. Mantiq talab qilinadi.'
        ),
        'level': 'hard',
        'questions': test_math_3,
    },
    {
        'title': 'Aralash matematika — 4-test (qiyin)',
        'description': (
            'Olimpiada uslubidagi savollar: EKUB/EKUK mantigʻi, boʻlinish isbotlari, '
            'egizak tub sonlar, davriy kasrlar, daryo va kechikish masalalari.'
        ),
        'level': 'hard',
        'questions': test_math_4,
    },
]


class Command(BaseCommand):
    help = 'Create 4 mixed math practice tests (2 medium + 2 hard) in Uzbek'

    def add_arguments(self, parser):
        parser.add_argument('--master', required=True, help='Username of the master to assign practices to')
        parser.add_argument('--republish', action='store_true',
                            help='Rebuild questions of practices that already exist')

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
            name='Matematika',
            defaults={
                'description': 'Matematika boʻyicha amaliy testlar',
                'color': '#0ea5e9',
                'icon': 'bi-calculator',
            },
        )

        for practice_data in PRACTICES:
            questions = practice_data['questions']

            practice, created = Practice.objects.get_or_create(
                title=practice_data['title'],
                master=master,
                defaults={
                    'description': practice_data['description'],
                    'subject': subject,
                    'level': practice_data['level'],
                    'is_free': True,
                    'is_published': True,
                    'is_available_for_all': True,
                    'time_limit': 40,
                    'pass_score': 60,
                    'max_attempts': 0,
                    'show_answers_after': True,
                },
            )

            if not created:
                if not options['republish']:
                    self.stdout.write(self.style.WARNING(
                        f"Practice '{practice.title}' already exists (id={practice.pk}). Skipping."
                    ))
                    continue

                practice.description = practice_data['description']
                practice.subject = subject
                practice.level = practice_data['level']
                practice.save()
                practice.questions.all().delete()

            for i, q in enumerate(questions, start=1):
                question = PracticeQuestion.objects.create(
                    practice=practice,
                    question_text=q['text'],
                    explanation=q['explanation'],
                    order=i,
                    points=1,
                    made_by=master,
                )
                for choice_text in q['choices']:
                    PracticeChoice.objects.create(
                        question=question,
                        text=choice_text,
                        is_correct=(choice_text == q['correct']),
                    )

            verb = 'Rebuilt' if not created else 'Created'
            self.stdout.write(self.style.SUCCESS(
                f"{verb} '{practice.title}' [{practice_data['level']}] "
                f"with {len(questions)} questions (id={practice.pk})."
            ))
