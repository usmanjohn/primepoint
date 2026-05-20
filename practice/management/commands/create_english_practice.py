from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
    {
        'text': '<p>Choose the correct option.</p><p><strong>This shirt is too big. Do you have it in ___ sizes?</strong></p>',
        'explanation': '<p><strong>other</strong> is correct. "Other" is used before plural nouns ("sizes") to mean alternative or different types.</p>',
        'correct': 'other',
        'choices': ['other', 'another', 'the other', 'others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>I finished my coffee. Can I please have ___ cup?</strong></p>',
        'explanation': '<p><strong>another</strong> is correct. "Another" means "one more" or "an additional" singular countable item.</p>',
        'correct': 'another',
        'choices': ['other', 'another', 'the other', 'others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>I have two close friends. One is a teacher, and ___ is an artist.</strong></p>',
        'explanation': '<p><strong>the other</strong> is correct. When choosing between exactly two options, we use "one... and the other" for the second specific choice.</p>',
        'correct': 'the other',
        'choices': ['other', 'another', 'the other', 'others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>Some people prefer traveling by train, while ___ enjoy driving.</strong></p>',
        'explanation': '<p><strong>others</strong> is correct. "Others" is a plural pronoun that replaces "other people" or "other groups".</p>',
        'correct': 'others',
        'choices': ['other', 'another', 'the other', 'others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>Where is ___ shoe? I can only find the left one.</strong></p>',
        'explanation': '<p><strong>the other</strong> is correct. Shoes come in a pair of two, so the remaining specific shoe is "the other".</p>',
        'correct': 'the other',
        'choices': ['other', 'another', 'the other', 'others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>We need to find ___ way to solve this math problem. This way is too complicated.</strong></p>',
        'explanation': '<p><strong>another</strong> is correct. "Another" can mean "a different" one when followed by a singular countable noun.</p>',
        'correct': 'another',
        'choices': ['other', 'another', 'the other', 'others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>I have invited Sarah and David, but I haven\'t called ___ yet.</strong></p>',
        'explanation': '<p><strong>the others</strong> is correct. "The others" functions as a plural pronoun meaning "the remaining specific people in our group".</p>',
        'correct': 'the others',
        'choices': ['other', 'another', 'the other', 'the others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>Are there any ___ questions before we finish the meeting?</strong></p>',
        'explanation': '<p><strong>other</strong> is correct. "Other" modifies plural nouns ("questions") when asking about additional options.</p>',
        'correct': 'other',
        'choices': ['other', 'another', 'the other', 'others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>The doctor told me to wait for ___ three days before exercising.</strong></p>',
        'explanation': '<p><strong>another</strong> is correct. We use "another" before plural expressions of time, money, or distance when treated as a single block.</p>',
        'correct': 'another',
        'choices': ['other', 'another', 'the other', 'others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>One of my brothers lives in London, and ___ lives in New York.</strong></p>',
        'explanation': '<p><strong>the other</strong> is correct. If I have exactly two brothers, the remaining one is specific: "the other".</p>',
        'correct': 'the other',
        'choices': ['other', 'another', 'the other', 'others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>This computer is broken. I\'ll have to use ___ one.</strong></p>',
        'explanation': '<p><strong>another</strong> is correct. "Another one" means a different singular computer from an undefined group.</p>',
        'correct': 'another',
        'choices': ['other', 'another', 'the other', 'others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>I don\'t like these shoes. Do you have any ___ options?</strong></p>',
        'explanation': '<p><strong>other</strong> is correct. "Other" follows words like "any", "some", or "no" when paired with a plural noun.</p>',
        'correct': 'other',
        'choices': ['other', 'another', 'the other', 'others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>Two runners finished the race early, but ___ are still running.</strong></p>',
        'explanation': '<p><strong>the others</strong> is correct. It is a pronoun that refers to the specific remaining group of runners.</p>',
        'correct': 'the others',
        'choices': ['other', 'another', 'the other', 'the others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>Can I borrow your pen? I lost my ___ one.</strong></p>',
        'explanation': '<p><strong>other</strong> is correct. "Other" is placed after a possessive adjective ("my", "your", "his") before a singular noun.</p>',
        'correct': 'other',
        'choices': ['other', 'another', 'the other', 'others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>They love each ___. They have been married for fifty years.</strong></p>',
        'explanation': '<p><strong>other</strong> is correct. "Each other" is a set phrase used for reciprocal actions between two people.</p>',
        'correct': 'other',
        'choices': ['other', 'another', 'the other', 'others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>I will take this book, and you can take ___ ones.</strong></p>',
        'explanation': '<p><strong>the other</strong> is correct. "The other" modifies the plural noun "ones" to mean the rest of a specific set.</p>',
        'correct': 'the other',
        'choices': ['other', 'another', 'the other', 'others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>Please pass me ___ piece of cake. It is delicious!</strong></p>',
        'explanation': '<p><strong>another</strong> is correct. "Another" is used with singular countable nouns to ask for one more item.</p>',
        'correct': 'another',
        'choices': ['other', 'another', 'the other', 'others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>This road is closed. We must go ___ way.</strong></p>',
        'explanation': '<p><strong>another</strong> is correct. "Another" acts as an adjective meaning "an alternative" for a singular countable noun.</p>',
        'correct': 'another',
        'choices': ['other', 'another', 'the other', 'others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>Some students passed the exam, but many ___ failed.</strong></p>',
        'explanation': '<p><strong>others</strong> is correct. "Others" acts as a plural pronoun to stand in for "other students".</p>',
        'correct': 'others',
        'choices': ['other', 'another', 'the other', 'others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>I have three cars. One is blue, and ___ ones are red.</strong></p>',
        'explanation': '<p><strong>the other</strong> is correct. "The other" is used as an adjective with plural nouns to designate the entire remainder of a specific set.</p>',
        'correct': 'the other',
        'choices': ['other', 'another', 'the other', 'others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>He drank his water and quickly asked for ___ glass.</strong></p>',
        'explanation': '<p><strong>another</strong> is correct. "Another" means one more additional singular item.</p>',
        'correct': 'another',
        'choices': ['other', 'another', 'the other', 'others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>Mr. Smith is busy, but ___ teachers are available to help you.</strong></p>',
        'explanation': '<p><strong>other</strong> is correct. We use "other" without "the" when talking about alternative plural nouns in general terms.</p>',
        'correct': 'other',
        'choices': ['other', 'another', 'the other', 'others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>One day I like my job, and ___ day I want to quit.</strong></p>',
        'explanation': '<p><strong>another</strong> is correct. The structure "one day... another day" shows contrast between non-specific alternating days.</p>',
        'correct': 'another',
        'choices': ['other', 'another', 'the other', 'others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>The store is on ___ side of the street. Just cross over here.</strong></p>',
        'explanation': '<p><strong>the other</strong> is correct. A street has exactly two sides, so the opposite side is specific: "the other side".</p>',
        'correct': 'the other',
        'choices': ['other', 'another', 'the other', 'others'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>They have to help one ___ during the project.</strong></p>',
        'explanation': '<p><strong>another</strong> is correct. "One another" is a set phrase similar to "each other," used for reciprocal actions among a group.</p>',
        'correct': 'another',
        'choices': ['other', 'another', 'the other', 'others'],
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
            title='English Grammar: Others, Another, The Other, Other',
            master=master,
            defaults={
                'description': 'Practice on the correct usage of "other", "another", "the other", and "others" in various contexts, helping students understand the differences and apply them correctly in sentences.',
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