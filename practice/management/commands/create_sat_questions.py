from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

from .sat_questions import (
    questions_sat_math_22,
    questions_sat_math_23,
    questions_sat_math_24,
    questions_sat_math_25,
    questions_sat_math_26,
    questions_sat_math_27,
    questions_sat_math_28,
    questions_sat_math_29,
    questions_sat_math_30,
)

PRACTICES = [
    {
        'title': 'Class 22: Absolute Value Inequalities on the Number Line',
        'description': 'Mastering bounded sandwich ranges and diverging outward intervals for complex absolute value inequalities.',
        'questions': questions_sat_math_22,
    },
    {
        'title': 'Class 23: Laws of Exponents: Core Operations',
        'description': 'Applying product, quotient, and power-to-power exponent rules to simplify advanced algebraic systems.',
        'questions': questions_sat_math_23,
    },
    {
        'title': 'Class 24: Negative and Fractional Exponents',
        'description': 'Demystifying radical indices, reciprocal inverting, and non-standard fractional powers.',
        'questions': questions_sat_math_24,
    },
    {
        'title': 'Class 25: Simplifying Radical Expressions',
        'description': 'Extracting perfect square multiples and simplifying variable parameters from square and cube roots.',
        'questions': questions_sat_math_25,
    },
    {
        'title': 'Class 26: Rationalizing Denominators',
        'description': 'Eliminating irrational square roots from fractions using simple root matching and conjugate products.',
        'questions': questions_sat_math_26,
    },
    {
        'title': 'Class 27: Introduction to Polynomials: Adding and Subtracting',
        'description': 'Grouping algebraic terms by exponent magnitude while avoiding negative distribution sign traps.',
        'questions': questions_sat_math_27,
    },
    {
        'title': 'Class 28: Multiplying Polynomials (FOIL and beyond)',
        'description': 'Expanding binomial and trinomial combinations systematically without missing middle terms.',
        'questions': questions_sat_math_28,
    },
    {
        'title': 'Class 29: Factoring: Greatest Common Factor (GCF) and Grouping',
        'description': 'Extracting numerical and variable common factors and executing four-term grouping splits.',
        'questions': questions_sat_math_29,
    },
    {
        'title': 'Class 30: Factoring: Special Polynomial Patterns',
        'description': 'Instantly recognizing and collapsing difference of squares and perfect square trinomial architectures.',
        'questions': questions_sat_math_30,
    }
]

class Command(BaseCommand):
    help = 'Create SAT math practice tests'

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
            name='Sat Math',
            defaults={'description': 'SAT Math practice tests'},
        )

        for practice_data in PRACTICES:
            practice, created = Practice.objects.get_or_create(
                title=practice_data['title'],
                master=master,
                defaults={
                    'description': practice_data['description'],
                    'subject': subject,
                    'level': 'easy',
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