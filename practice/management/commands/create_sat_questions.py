from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

from .sat_questions import (
    questions_sat_math_13,
    questions_sat_math_14,
    questions_sat_math_15,
    questions_sat_math_16,
    questions_sat_math_17,
    questions_sat_math_18,
    questions_sat_math_19,
    questions_sat_math_20,
    questions_sat_math_21
)
PRACTICES = [
    {
        'title': 'Class 13: Solving Multi-Step Linear Inequalities',
        'description': 'Mastering inequality properties, variable isolation, and the essential rule of flipping signs when multiplying or dividing by negative numbers.',
        'questions': questions_sat_math_13,
    },
    {
        'title': 'Class 14: Graphing Linear Inequalities on the Coordinate Plane',
        'description': 'Visualizing inequalities using dashed vs. solid boundary lines and identifying correct shading directions (above vs. below).',
        'questions': questions_sat_math_14,
    },
    {
        'title': 'Class 15: Modeling Real-World Scenarios with Inequalities',
        'description': 'Translating critical contextual limit keywords like "at most," "at least," and "no more than" into algebraic expressions.',
        'questions': questions_sat_math_15,
    },
    {
        'title': 'Class 16: Systems of Linear Equations: Substitution Method',
        'description': 'Developing speed and precision using algebraic substitution when variables are easily isolated.',
        'questions': questions_sat_math_16,
    },
    {
        'title': 'Class 17: Systems of Linear Equations: Elimination Method',
        'description': 'Using row operations to eliminate variables quickly in standard system configurations.',
        'questions': questions_sat_math_17,
    },
    {
        'title': 'Class 18: Word Problems Involving Systems of Linear Equations',
        'description': 'Deconstructing situational real-world prompts (value vs. quantity) into fully operational multi-variable systems.',
        'questions': questions_sat_math_18,
    },
    {
        'title': 'Class 19: Systems with Infinite Solutions (Identical Lines)',
        'description': 'Recognizing and solving special system cases where graphs perfectly overlap, leading to infinitely many solutions.',
        'questions': questions_sat_math_19,
    },
    {
        'title': 'Class 20: Systems with No Solution (Parallel Lines)',
        'description': 'Mastering parallel line systems that share identical variable slopes but feature different constants.',
        'questions': questions_sat_math_20,
    },
    {
        'title': 'Class 21: Systems of Linear Inequalities and Bounded Regions',
        'description': 'Verifying coordinate solutions inside complex, multi-layered overlapping shaded regions on a grid.',
        'questions': questions_sat_math_21}]


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