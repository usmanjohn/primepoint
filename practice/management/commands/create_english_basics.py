# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

from .english_basic_questions import test_english_1, test_english_2, test_english_3


PRACTICES = [
    {
        'title': 'English Mixed — Test 1 (easy)',
        'description': (
            "Boshlangʻich daraja: to be, Present Simple va Continuous, artikllar (a/an/the), "
            "koʻplik shakllari, sonlar, olmoshlar, predloglar va soʻz tartibi. "
            "Har bir savolda inglizcha va oʻzbekcha izoh bor."
        ),
        'level': 'easy',
        'questions': test_english_1,
    },
    {
        'title': 'English Mixed — Test 2 (easy)',
        'description': (
            "Boshlangʻich daraja: Past Simple (toʻgʻri va notoʻgʻri fe'llar), kelasi zamon "
            "(will / be going to), gerundiy va infinitiv, much/many, some/any, orttirma daraja, "
            "soat va narxlar, modal fe'llar hamda soʻroq gaplar."
        ),
        'level': 'easy',
        'questions': test_english_2,
    },
    {
        'title': 'English Mixed — Test 3 (medium)',
        'description': (
            "Oʻrta daraja: Present Perfect va for/since, gerundiy/infinitiv ma'no farqi "
            "(remember, stop), artikllarning qiyin holatlari, used to, too/enough, so/such, "
            "question tags, relative pronouns, 1-shart gap, few/little, yillarni oʻqish va majhul nisbat."
        ),
        'level': 'medium',
        'questions': test_english_3,
    },
]


class Command(BaseCommand):
    help = 'Create 3 mixed English practice tests (2 easy + 1 medium)'

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
            name='English',
            defaults={'description': 'English grammar and vocabulary practice'},
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
                    'time_limit': 30,
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
