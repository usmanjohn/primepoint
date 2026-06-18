from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

from .sat_questions import (questions_sat_math_1, questions_sat_math_2, questions_sat_math_3, questions_sat_math_4, questions_sat_math_5, questions_sat_math_6, questions_sat_math_7, questions_sat_math_8, questions_sat_math_9, questions_sat_math_10, questions_sat_math_11, questions_sat_math_12)
PRACTICES = [
    {
        'title': 'Class 1: Linear Equations & Distribution Basics',
        'description': 'Mastering basic linear equations, distributing coefficients, and isolating variables efficiently.',
        'questions': questions_sat_math_1,
    },
    {
        'title': 'Class 2: Combining Like Terms & Simplifying Expressions',
        'description': 'Grouping variables and constants to simplify multi-step algebraic expressions rapidly.',
        'questions': questions_sat_math_2,
    },
    {
        'title': 'Class 3: Multi-Step Variable Isolation',
        'description': 'Solving complex linear equations requiring operations on both sides of the equals sign.',
        'questions': questions_sat_math_3,
    },
    {
        'title': 'Class 4: Rational Equations & Cross-Multiplication',
        'description': 'Clearing fractions and solving rational linear algebraic setups systematically.',
        'questions': questions_sat_math_4,
    },
    {
        'title': 'Class 5: Checking Solutions & Identities',
        'description': 'Distinguishing between equations with one solution, no solution, or infinitely many solutions.',
        'questions': questions_sat_math_5,
    },
    {
        'title': 'Class 6: Harder Linear Equations & Fractional Steps',
        'description': 'Advanced isolated variable mechanics featuring dense fractional and decimal coefficients.',
        'questions': questions_sat_math_6,
    },
    {
        'title': 'Class 7: Slope-Intercept Form (y = mx + b) in Depth',
        'description': 'Decoding, manipulating, and identifying slopes and y-intercepts across varied representations.',
        'questions': questions_sat_math_7,
    },
    {
        'title': 'Class 8: Standard Form (Ax + By = C) & Intercept Tracking',
        'description': 'Finding x-intercepts, y-intercepts, and slope values quickly directly from standard linear forms.',
        'questions': questions_sat_math_8,
    },
    {
        'title': 'Class 9: Modeling Word Problems with Linear Equations',
        'description': 'Translating real-world descriptive paragraphs into working slope-intercept equations.',
        'questions': questions_sat_math_9,
    },
    {
        'title': 'Class 10: Interpreting Slopes & Intercepts in Context',
        'description': 'Decoding word problems to explain exactly what variable coefficients and constants represent in practice.',
        'questions': questions_sat_math_10,
    },
    {
        'title': 'Class 11: Parallel Lines & Equal Slopes',
        'description': 'Identifying parallel systems and matching identical slopes across various coordinate equations.',
        'questions': questions_sat_math_11,
    },
    {
        'title': 'Class 12: Perpendicular Lines & Negative Reciprocals',
        'description': 'Calculating perpendicular trajectories using negative reciprocal slope relationships.',
        'questions': questions_sat_math_12,
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