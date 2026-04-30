from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice
QUESTIONS = [
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ is your name?</strong></p>',
        'explanation': '<p><strong>What</strong> is used to ask for information about something (in this case, a name).</p>',
        'correct': 'What',
        'choices': ['Who', 'What', 'Where', 'When'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ are you from?</strong></p>',
        'explanation': '<p><strong>Where</strong> is used to ask about a place or location.</p>',
        'correct': 'Where',
        'choices': ['Why', 'What', 'Where', 'Who'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ old are you?</strong></p>',
        'explanation': '<p><strong>How</strong> is used with adjectives like "old" to ask about degree or quantity.</p>',
        'correct': 'How',
        'choices': ['What', 'How', 'Which', 'Why'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ is your birthday?</strong></p>',
        'explanation': '<p><strong>When</strong> is used to ask about a time or a date.</p>',
        'correct': 'When',
        'choices': ['Where', 'Who', 'When', 'What'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ is that man standing over there?</strong></p>',
        'explanation': '<p><strong>Who</strong> is used to ask about a person.</p>',
        'correct': 'Who',
        'choices': ['What', 'Who', 'Which', 'Whose'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ do you want to learn English?</strong></p>',
        'explanation': '<p><strong>Why</strong> is used to ask for a reason or purpose.</p>',
        'correct': 'Why',
        'choices': ['Why', 'Where', 'Who', 'Which'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ color do you prefer, red or blue?</strong></p>',
        'explanation': '<p><strong>Which</strong> is used when asking someone to make a choice between a limited number of options.</p>',
        'correct': 'Which',
        'choices': ['What', 'Which', 'Where', 'Who'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ jacket is this? Is it yours?</strong></p>',
        'explanation': '<p><strong>Whose</strong> is used to ask about possession or ownership.</p>',
        'correct': 'Whose',
        'choices': ['Who', 'Whom', 'Whose', 'Which'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ much does this shirt cost?</strong></p>',
        'explanation': '<p><strong>How</strong> (in "How much") is used to ask about price or an uncountable quantity.</p>',
        'correct': 'How',
        'choices': ['What', 'How', 'Why', 'Where'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ many siblings do you have?</strong></p>',
        'explanation': '<p><strong>How</strong> (in "How many") is used to ask about a countable quantity.</p>',
        'correct': 'How',
        'choices': ['How', 'What', 'Who', 'Which'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ often do you go to the gym?</strong></p>',
        'explanation': '<p><strong>How</strong> (in "How often") is used to ask about the frequency of an action.</p>',
        'correct': 'How',
        'choices': ['When', 'What', 'How', 'Why'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ time is it right now?</strong></p>',
        'explanation': '<p><strong>What</strong> is used with "time" to ask for the current hour.</p>',
        'correct': 'What',
        'choices': ['When', 'Where', 'How', 'What'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ did you get to work today? By bus?</strong></p>',
        'explanation': '<p><strong>How</strong> is used to ask about the method or manner of doing something.</p>',
        'correct': 'How',
        'choices': ['What', 'Where', 'How', 'Why'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ is the capital of France?</strong></p>',
        'explanation': '<p><strong>What</strong> is used to ask for specific factual information.</p>',
        'correct': 'What',
        'choices': ['Where', 'What', 'Which', 'How'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ are you crying? What happened?</strong></p>',
        'explanation': '<p><strong>Why</strong> asks for the cause or reason behind an action or feeling.</p>',
        'correct': 'Why',
        'choices': ['Who', 'When', 'Why', 'Where'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ did you put my car keys?</strong></p>',
        'explanation': '<p><strong>Where</strong> asks for the location or placement of an object.</p>',
        'correct': 'Where',
        'choices': ['What', 'Where', 'How', 'Which'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ of these books is yours? The green one or the red one?</strong></p>',
        'explanation': '<p><strong>Which</strong> is used when choosing from a specific set of items.</p>',
        'correct': 'Which',
        'choices': ['What', 'Which', 'Whose', 'Who'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ long does the movie last?</strong></p>',
        'explanation': '<p><strong>How</strong> (in "How long") is used to ask about duration or length.</p>',
        'correct': 'How',
        'choices': ['What', 'When', 'How', 'Why'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ is calling me at this hour?</strong></p>',
        'explanation': '<p><strong>Who</strong> is used as the subject of the sentence to ask about a person.</p>',
        'correct': 'Who',
        'choices': ['Whose', 'Who', 'What', 'Where'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ did you do last weekend?</strong></p>',
        'explanation': '<p><strong>What</strong> is used to ask about an action or activity.</p>',
        'correct': 'What',
        'choices': ['Where', 'When', 'What', 'How'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ bag is on the chair? I need to move it.</strong></p>',
        'explanation': '<p><strong>Whose</strong> asks who owns the bag.</p>',
        'correct': 'Whose',
        'choices': ['Who', 'Whom', 'What', 'Whose'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ does the train leave?</strong></p>',
        'explanation': '<p><strong>When</strong> is used to ask for a time of departure.</p>',
        'correct': 'When',
        'choices': ['Where', 'How', 'When', 'Which'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ far is the airport from the hotel?</strong></p>',
        'explanation': '<p><strong>How</strong> (in "How far") is used to ask about distance.</p>',
        'correct': 'How',
        'choices': ['What', 'Where', 'How', 'When'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ kind of music do you like?</strong></p>',
        'explanation': '<p><strong>What</strong> is used with "kind" or "type" to ask for a category of something.</p>',
        'correct': 'What',
        'choices': ['Which', 'What', 'How', 'Who'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ tall is your older brother?</strong></p>',
        'explanation': '<p><strong>How</strong> is used with adjectives like "tall" to ask for a specific measurement.</p>',
        'correct': 'How',
        'choices': ['What', 'How', 'Which', 'Why'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ is cooking dinner tonight?</strong></p>',
        'explanation': '<p><strong>Who</strong> asks for the identity of the person performing the action.</p>',
        'correct': 'Who',
        'choices': ['What', 'Whose', 'Who', 'Where'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ route should we take, the highway or the scenic road?</strong></p>',
        'explanation': '<p><strong>Which</strong> is used when there are limited, specific options available.</p>',
        'correct': 'Which',
        'choices': ['What', 'Where', 'Which', 'How'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ shoes are these? They look brand new.</strong></p>',
        'explanation': '<p><strong>Whose</strong> is used to find out who the shoes belong to.</p>',
        'correct': 'Whose',
        'choices': ['Who', 'What', 'Which', 'Whose'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ were you late to the meeting?</strong></p>',
        'explanation': '<p><strong>Why</strong> asks for the reason someone was late.</p>',
        'correct': 'Why',
        'choices': ['When', 'What', 'Why', 'Who'],
    },
    {
        'text': '<p>Choose the correct question word.</p><p><strong>___ did you talk to at the party?</strong></p>',
        'explanation': '<p><strong>Who</strong> (or Whom) is used to ask about the person receiving the action.</p>',
        'correct': 'Who',
        'choices': ['Who', 'What', 'Where', 'Which'],
    }
]
class Command(BaseCommand):
    help = 'Create an English grammar practice test (wh?)'

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
            title='English Basic: WH questions',
            master=master,
            defaults={
                'description': 'Practice using the correct form of the WH question words (what, where, when, who, why, how, which, whose) in various contexts.',
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