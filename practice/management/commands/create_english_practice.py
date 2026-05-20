from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice
QUESTIONS = [
    {
        'text': '<p>Choose the correct article.</p><p><strong>I saw ___ old man walking in the park.</strong></p>',
        'explanation': '<p><strong>an</strong> is correct. We use "an" before a singular count noun starting with a vowel sound ("old").</p>',
        'correct': 'an',
        'choices': ['a', 'an', 'the', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>___ sun is shining brightly today.</strong></p>',
        'explanation': '<p><strong>The</strong> is correct. We use "the" for unique things (things that are the only one of their kind).</p>',
        'correct': 'The',
        'choices': ['A', 'An', 'The', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>My brother works as ___ engineer.</strong></p>',
        'explanation': '<p><strong>an</strong> is correct. We use "a/an" to mention someone\'s job.</p>',
        'correct': 'an',
        'choices': ['a', 'an', 'the', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>Where are ___ children? I can\'t hear them.</strong></p>',
        'explanation': '<p><strong>the</strong> is correct. We use "the" when the listener knows which specific children we are referring to.</p>',
        'correct': 'the',
        'choices': ['a', 'an', 'the', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>I have ___ bad headache today.</strong></p>',
        'explanation': '<p><strong>a</strong> is correct. The phrase "have a headache" uses the indefinite article.</p>',
        'correct': 'a',
        'choices': ['a', 'an', 'the', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>I love listening to ___ music.</strong></p>',
        'explanation': '<p><strong>Ø</strong> is correct. We do not use an article when speaking about uncountable nouns (like music) in general.</p>',
        'correct': 'Ø',
        'choices': ['a', 'an', 'the', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>She went to ___ hospital to visit her friend who is a patient there.</strong></p>',
        'explanation': '<p><strong>the</strong> is correct. In this context, it refers to a specific building being visited, not for receiving treatment.</p>',
        'correct': 'the',
        'choices': ['a', 'an', 'the', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>___ history is my favorite subject at school.</strong></p>',
        'explanation': '<p><strong>Ø</strong> is correct. We do not use an article for school subjects.</p>',
        'correct': 'Ø',
        'choices': ['a', 'an', 'the', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>I need ___ pen to write this note. Any color will do.</strong></p>',
        'explanation': '<p><strong>a</strong> is correct. We use "a" for non-specific singular countable nouns.</p>',
        'correct': 'a',
        'choices': ['a', 'an', 'the', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>He is ___ most intelligent student in our class.</strong></p>',
        'explanation': '<p><strong>the</strong> is correct. We use "the" with superlative adjectives.</p>',
        'correct': 'the',
        'choices': ['a', 'an', 'the', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>I usually have ___ breakfast at 7 a.m.</strong></p>',
        'explanation': '<p><strong>Ø</strong> is correct. We do not use an article before names of meals.</p>',
        'correct': 'Ø',
        'choices': ['a', 'an', 'the', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>___ apple a day keeps the doctor away.</strong></p>',
        'explanation': '<p><strong>An</strong> is correct. "An" is used before a singular countable noun starting with a vowel sound.</p>',
        'correct': 'An',
        'choices': ['A', 'An', 'The', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>___ Nile is the longest river in the world.</strong></p>',
        'explanation': '<p><strong>The</strong> is correct. We use "the" before the names of rivers.</p>',
        'correct': 'The',
        'choices': ['A', 'An', 'The', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>He plays ___ guitar very well.</strong></p>',
        'explanation': '<p><strong>the</strong> is correct. We use "the" before musical instruments when talking about playing them.</p>',
        'correct': 'the',
        'choices': ['a', 'an', 'the', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>They live in ___ beautiful house near the lake.</strong></p>',
        'explanation': '<p><strong>a</strong> is correct. "A" is used because it is a singular countable noun being mentioned for the first time.</p>',
        'correct': 'a',
        'choices': ['a', 'an', 'the', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>___ honesty is an important character trait.</strong></p>',
        'explanation': '<p><strong>Ø</strong> is correct. We do not use articles with abstract nouns when talking about them in general terms.</p>',
        'correct': 'Ø',
        'choices': ['a', 'an', 'the', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>Paris is ___ capital of France.</strong></p>',
        'explanation': '<p><strong>the</strong> is correct. We use "the" because France has only one capital city, making it specific and unique.</p>',
        'correct': 'the',
        'choices': ['a', 'an', 'the', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>Can you pass me ___ salt, please?</strong></p>',
        'explanation': '<p><strong>the</strong> is correct. We use "the" for specific things on the table that both speakers can see.</p>',
        'correct': 'the',
        'choices': ['a', 'an', 'the', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>She wants to visit ___ Alps next summer.</strong></p>',
        'explanation': '<p><strong>the</strong> is correct. We use "the" before names of mountain ranges.</p>',
        'correct': 'the',
        'choices': ['a', 'an', 'the', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>He travels to work by ___ train.</strong></p>',
        'explanation': '<p><strong>Ø</strong> is correct. We do not use an article in the prepositional phrase "by + mode of transport".</p>',
        'correct': 'Ø',
        'choices': ['a', 'an', 'the', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>It took us ___ hour to get home.</strong></p>',
        'explanation': '<p><strong>an</strong> is correct. "Hour" starts with a silent "h", so it begins with a vowel sound.</p>',
        'correct': 'an',
        'choices': ['a', 'an', 'the', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>My uncle is ___ honest man.</strong></p>',
        'explanation': '<p><strong>an</strong> is correct. "Honest" starts with a silent "h", making the initial sound a vowel.</p>',
        'correct': 'an',
        'choices': ['a', 'an', 'the', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>They are studying ___ European history.</strong></p>',
        'explanation': '<p><strong>Ø</strong> is correct. School and academic subjects do not take an article, even with a regional modifier.</p>',
        'correct': 'Ø',
        'choices': ['a', 'an', 'the', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>She wants to become ___ university professor.</strong></p>',
        'explanation': '<p><strong>a</strong> is correct. "University" starts with a consonant "y" sound (/juː/), so we use "a" instead of "an".</p>',
        'correct': 'a',
        'choices': ['a', 'an', 'the', 'Ø'],
    },
    {
        'text': '<p>Choose the correct article.</p><p><strong>We had a great time at ___ Pacific Ocean.</strong></p>',
        'explanation': '<p><strong>the</strong> is correct. We use "the" before names of oceans.</p>',
        'correct': 'the',
        'choices': ['a', 'an', 'the', 'Ø'],
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
            title='English Grammar: Articles Practice',
            master=master,
            defaults={
                'description': 'Practice on using articles (a, an, the, Ø) correctly in various contexts.',
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
                #hint=q['hint'],
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