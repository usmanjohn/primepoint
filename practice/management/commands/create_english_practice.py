from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
    {
        'text': '<p>Choose the correct verb.</p><p><strong>I ___ a student.</strong></p>',
        'hint': '<p>With "I", we use "am".</p>',
        'explanation': '<p><strong>am</strong> is the correct form for "I".</p>',
        'correct': 'am',
        'choices': ['am', 'is', 'are', 'be'],
    },
    {
        'text': '<p>Choose the correct verb.</p><p><strong>He ___ a doctor.</strong></p>',
        'hint': '<p>With singular subjects like "he", "she", "it", we use "is".</p>',
        'explanation': '<p><strong>is</strong> is correct for "he".</p>',
        'correct': 'is',
        'choices': ['am', 'is', 'are', 'be'],
    },
    {
        'text': '<p>Choose the correct verb.</p><p><strong>They ___ happy.</strong></p>',
        'hint': '<p>With plural subjects like "we", "you", "they", we use "are".</p>',
        'explanation': '<p><strong>are</strong> is correct for "they".</p>',
        'correct': 'are',
        'choices': ['am', 'is', 'are', 'be'],
    },
    {
        'text': '<p>Choose the correct verb.</p><p><strong>We ___ friends.</strong></p>',
        'hint': '<p>With "we", we use "are".</p>',
        'explanation': '<p><strong>are</strong> is correct for "we".</p>',
        'correct': 'are',
        'choices': ['am', 'is', 'are', 'be'],
    },
    {
        'text': '<p>Choose the correct verb.</p><p><strong>She ___ my sister.</strong></p>',
        'hint': '<p>With "she", we use "is".</p>',
        'explanation': '<p><strong>is</strong> is correct for "she".</p>',
        'correct': 'is',
        'choices': ['am', 'is', 'are', 'be'],
    },
    {
        'text': '<p>Choose the correct verb.</p><p><strong>It ___ a sunny day.</strong></p>',
        'hint': '<p>With "it", we use "is".</p>',
        'explanation': '<p><strong>is</strong> is correct for "it".</p>',
        'correct': 'is',
        'choices': ['am', 'is', 'are', 'be'],
    },
    {
        'text': '<p>Choose the correct verb.</p><p><strong>You ___ very tall.</strong></p>',
        'hint': '<p>With "you", we use "are".</p>',
        'explanation': '<p><strong>are</strong> is correct for "you".</p>',
        'correct': 'are',
        'choices': ['am', 'is', 'are', 'be'],
    },
    {
        'text': '<p>Choose the correct verb.</p><p><strong>The dog ___ barking.</strong></p>',
        'hint': '<p>"The dog" is singular (it), so we use "is".</p>',
        'explanation': '<p><strong>is</strong> is correct for a singular subject.</p>',
        'correct': 'is',
        'choices': ['am', 'is', 'are', 'be'],
    },
    {
        'text': '<p>Choose the correct verb.</p><p><strong>The cats ___ sleeping.</strong></p>',
        'hint': '<p>"The cats" is plural (they), so we use "are".</p>',
        'explanation': '<p><strong>are</strong> is correct for a plural subject.</p>',
        'correct': 'are',
        'choices': ['am', 'is', 'are', 'be'],
    },
    {
        'text': '<p>Choose the correct verb.</p><p><strong>I ___ not tired.</strong></p>',
        'hint': '<p>With "I", we always use "am".</p>',
        'explanation': '<p><strong>am</strong> is correct for "I".</p>',
        'correct': 'am',
        'choices': ['am', 'is', 'are', 'be'],
    },
    {
        'text': '<p>Choose the correct verb.</p><p><strong>___ he your brother?</strong></p>',
        'hint': '<p>This is a question. What verb goes with "he"?</p>',
        'explanation': '<p><strong>Is</strong> is correct because the subject is "he".</p>',
        'correct': 'Is',
        'choices': ['Am', 'Is', 'Are', 'Be'],
    },
    {
        'text': '<p>Choose the correct verb.</p><p><strong>___ they coming?</strong></p>',
        'hint': '<p>This is a question. What verb goes with "they"?</p>',
        'explanation': '<p><strong>Are</strong> is correct because the subject is "they".</p>',
        'correct': 'Are',
        'choices': ['Am', 'Is', 'Are', 'Be'],
    },
    {
        'text': '<p>Choose the correct verb.</p><p><strong>___ I late?</strong></p>',
        'hint': '<p>This is a question. What verb goes with "I"?</p>',
        'explanation': '<p><strong>Am</strong> is correct because the subject is "I".</p>',
        'correct': 'Am',
        'choices': ['Am', 'Is', 'Are', 'Be'],
    },
    {
        'text': '<p>Choose the correct verb.</p><p><strong>John and Mary ___ here.</strong></p>',
        'hint': '<p>"John and Mary" is plural (they).</p>',
        'explanation': '<p><strong>are</strong> is correct because the subject is plural.</p>',
        'correct': 'are',
        'choices': ['am', 'is', 'are', 'be'],
    },
    {
        'text': '<p>Choose the correct verb.</p><p><strong>The book ___ on the table.</strong></p>',
        'hint': '<p>"The book" is singular (it).</p>',
        'explanation': '<p><strong>is</strong> is correct because "the book" is singular.</p>',
        'correct': 'is',
        'choices': ['am', 'is', 'are', 'be'],
    },
    {
        'text': '<p>Choose the correct verb.</p><p><strong>My parents ___ at home.</strong></p>',
        'hint': '<p>"My parents" is plural (they).</p>',
        'explanation': '<p><strong>are</strong> is correct for plural subjects.</p>',
        'correct': 'are',
        'choices': ['am', 'is', 'are', 'be'],
    },
    {
        'text': '<p>Choose the correct verb.</p><p><strong>The car ___ red.</strong></p>',
        'hint': '<p>"The car" is singular (it).</p>',
        'explanation': '<p><strong>is</strong> is correct for a singular subject.</p>',
        'correct': 'is',
        'choices': ['am', 'is', 'are', 'be'],
    },
    {
        'text': '<p>Choose the correct verb.</p><p><strong>We ___ ready for the test.</strong></p>',
        'hint': '<p>With "we", we use "are".</p>',
        'explanation': '<p><strong>are</strong> is correct for "we".</p>',
        'correct': 'are',
        'choices': ['am', 'is', 'are', 'be'],
    },
    {
        'text': '<p>Choose the correct verb.</p><p><strong>She ___ not a teacher.</strong></p>',
        'hint': '<p>With "she", we use "is".</p>',
        'explanation': '<p><strong>is</strong> is correct for "she".</p>',
        'correct': 'is',
        'choices': ['am', 'is', 'are', 'be'],
    },
    {
        'text': '<p>Choose the correct verb.</p><p><strong>I ___ from London.</strong></p>',
        'hint': '<p>With "I", we always use "am".</p>',
        'explanation': '<p><strong>am</strong> is correct for "I".</p>',
        'correct': 'am',
        'choices': ['am', 'is', 'are', 'be'],
    }
]

class Command(BaseCommand):
    help = 'Create an English grammar practice test (am/is/are)'

    def add_arguments(self, parser):
        parser.add_argument('--master', default='powerty', help='Username of the master to assign this practice to')

    def handle(self, *args, **options):
        master_username = options['master']
        try:
            user = User.objects.get(username=master_username)
        except User.DoesNotExist:
            raise CommandError(f"User '{master_username}' not found.")

        try:
            master = Master.objects.get(profile__user=user)
        except Master.DoesNotExist:
            raise CommandError(f"No Master profile found for user '{master_username}'.")

        subject, _ = Subject.objects.get_or_create(
            name='English',
            defaults={'description': 'English grammar and vocabulary practice'},
        )

        # Create or get the practice and ensure it is published
        practice, created = Practice.objects.get_or_create(
            title='English Basic: am / is / are',
            master=master,
            defaults={
                'description': 'Practice using the correct form of the verb "to be" (am, is, are).',
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
            # If it already exists, update it to make sure it is published
            practice.is_published = True
            practice.save()
            self.stdout.write(self.style.WARNING(
                f"Practice '{practice.title}' already exists (id={practice.pk}). Set to published."
            ))
            # Delete old questions to replace with fresh ones if needed, or simply return.
            # Returning to avoid duplicates, assuming it's already populated.
            return

        for i, q in enumerate(QUESTIONS, start=1):
            question = PracticeQuestion.objects.create(
                practice=practice,
                question_text=q['text'],
                hint=q['hint'],
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

        self.stdout.write(self.style.SUCCESS(
            f"Created and published practice '{practice.title}' with {len(QUESTIONS)} questions (id={practice.pk})."
        ))