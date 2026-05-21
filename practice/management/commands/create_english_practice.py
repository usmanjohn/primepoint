from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
    {
        'text': '<p>Choose the correct option.</p><p><strong>I need to buy some new ___ for my living room.</strong></p>',
        'explanation': '<p><strong>furniture</strong> is correct. "Furniture" is an uncountable noun and cannot be made plural with an "-s".</p>',
        'correct': 'furniture',
        'choices': ['furniture', 'furnitures', 'piece of furnitures', 'a furniture'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>The ___ are playing happily in the backyard.</strong></p>',
        'explanation': '<p><strong>children</strong> is correct. It is the irregular plural form of "child".</p>',
        'correct': 'children',
        'choices': ['childs', 'childrens', 'children', 'childes'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>Could you give me ___ about the upcoming exam?</strong></p>',
        'explanation': '<p><strong>some advice</strong> is correct. "Advice" is uncountable, so it cannot be used with the article "an" or made plural.</p>',
        'correct': 'some advice',
        'choices': ['an advice', 'advices', 'some advices', 'some advice'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>The police ___ investigating the cause of the accident.</strong></p>',
        'explanation': '<p><strong>are</strong> is correct. "Police" is a collective noun that is always treated as plural and takes a plural verb.</p>',
        'correct': 'are',
        'choices': ['is', 'are', 'was', 'has'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>I bought two ___ of bread from the local bakery.</strong></p>',
        'explanation': '<p><strong>loaves</strong> is correct. Nouns ending in "-f" or "-fe" like "loaf" usually change to "-ves" in the plural form.</p>',
        'correct': 'loaves',
        'choices': ['loafs', 'loaves', 'loafes', 'loaf'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>Mathematics ___ my least favorite subject in high school.</strong></p>',
        'explanation': '<p><strong>is</strong> is correct. Academic disciplines ending in "-ics" (like mathematics, physics) are singular and take a singular verb.</p>',
        'correct': 'is',
        'choices': ['is', 'are', 'were', 'have been'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>We had to pack a lot of ___ for our flight to Paris.</strong></p>',
        'explanation': '<p><strong>luggage</strong> is correct. "Luggage" is an uncountable noun and does not take a plural "-s".</p>',
        'correct': 'luggage',
        'choices': ['luggages', 'luggage', 'piece of luggages', 'a luggage'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>A large flock of ___ flew over the lake this morning.</strong></p>',
        'explanation': '<p><strong>geese</strong> is correct. "Geese" is the irregular plural form of "goose".</p>',
        'correct': 'geese',
        'choices': ['gooses', 'geeses', 'geese', 'goose'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>There ___ very little traffic on the highway today.</strong></p>',
        'explanation': '<p><strong>was</strong> is correct. "Traffic" is an uncountable noun, which requires a singular verb form.</p>',
        'correct': 'was',
        'choices': ['were', 'was', 'are', 'have been'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>The dentist told him that two of his ___ had cavities.</strong></p>',
        'explanation': '<p><strong>teeth</strong> is correct. "Teeth" is the irregular plural form of "tooth".</p>',
        'correct': 'teeth',
        'choices': ['tooths', 'teeths', 'teethes', 'teeth'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>I poured ___ into the recipe instead of sugar by mistake.</strong></p>',
        'explanation': '<p><strong>too much salt</strong> is correct. "Salt" is an uncountable noun, so it must be modified by "much", not "many".</p>',
        'correct': 'too much salt',
        'choices': ['too many salts', 'too much salt', 'too much salts', 'too many salt'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>Several ___ were seen drinking water from the river.</strong></p>',
        'explanation': '<p><strong>deer</strong> is correct. "Deer" has the exact same form for both its singular and plural numbers.</p>',
        'correct': 'deer',
        'choices': ['deers', 'deeres', 'deer', 'deerses'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>No news ___ good news, according to the old saying.</strong></p>',
        'explanation': '<p><strong>is</strong> is correct. "News" looks plural because of the "-s", but it is grammatically an uncountable singular noun.</p>',
        'correct': 'is',
        'choices': ['is', 'are', 'were', 'have'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>The laboratory researchers analyzed the ___ carefully.</strong></p>',
        'explanation': '<p><strong>data</strong> is correct. In academic and scientific English, "data" serves as the plural form of "datum".</p>',
        'correct': 'data',
        'choices': ['datas', 'datums', 'data', 'dataes'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>How ___ did you get on your biology assignment?</strong></p>',
        'explanation': '<p><strong>much homework</strong> is correct. "Homework" is an uncountable noun, which requires the modifier "much".</p>',
        'correct': 'much homework',
        'choices': ['many homeworks', 'much homeworks', 'many homework', 'much homework'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>The farmer noticed that three ___ were missing from the pen.</strong></p>',
        'explanation': '<p><strong>sheep</strong> is correct. "Sheep" is an irregular noun that remains identical in both singular and plural forms.</p>',
        'correct': 'sheep',
        'choices': ['sheeps', 'sheepes', 'sheep', 'ship'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>These scissors ___ sharp enough to cut through this thick cardboard.</strong></p>',
        'explanation': '<p><strong>aren\'t</strong> is correct. Tools consisting of two joined parts (like scissors, glasses, pants) are always plural.</p>',
        'correct': "aren't",
        'choices': ["isn't", "aren't", 'not', 'wasn\'t'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>You need to show ___ when learning a musical instrument.</strong></p>',
        'explanation': '<p><strong>patience</strong> is correct. Abstract nouns like "patience" are uncountable and do not use plural endings or "a/an".</p>',
        'correct': 'patience',
        'choices': ['a patience', 'patiences', 'patience', 'some patiences'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>A group of ___ volunteered to help clean up the local park.</strong></p>',
        'explanation': '<p><strong>women</strong> is correct. It is the irregular plural spelling of the singular noun "woman".</p>',
        'correct': 'women',
        'choices': ['womans', 'womens', 'women', 'womene'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>The chef needs three more ___ of garlic for the pasta sauce.</strong></p>',
        'explanation': '<p><strong>cloves</strong> is correct. To count specific units of garlic, we use the countable phrase "cloves of garlic".</p>',
        'correct': 'cloves',
        'choices': ['garlics', 'cloves', 'pieces of garlics', 'head of garlics'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>Gymnastics ___ excellent for developing balance and core strength.</strong></p>',
        'explanation': '<p><strong>is</strong> is correct. Sports and physical activities ending in "-ics" are singular nouns and take a singular verb.</p>',
        'correct': 'is',
        'choices': ['is', 'are', 'were', 'being'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>The heavy winds blew several ___ off the neighborhood trees.</strong></p>',
        'explanation': '<p><strong>leaves</strong> is correct. The plural of "leaf" changes the "-f" to "-v" and adds "-es".</p>',
        'correct': 'leaves',
        'choices': ['leafs', 'leafes', 'leaves', 'lefs'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>Could you pass me ___ to wipe down the kitchen counter?</strong></p>',
        'explanation': '<p><strong>a piece of paper</strong> is correct. "Paper" as a material is uncountable, so we count it using "a piece of".</p>',
        'correct': 'a piece of paper',
        'choices': ['a paper', 'papers', 'a piece of paper', 'a piece of papers'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>The house was infested with ___ before the exterminator arrived.</strong></p>',
        'explanation': '<p><strong>mice</strong> is correct. "Mice" is the irregular plural form of "mouse".</p>',
        'correct': 'mice',
        'choices': ['mouses', 'mices', 'mice', 'mousers'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>My new jeans ___ fitting comfortably around the waist line.</strong></p>',
        'explanation': '<p><strong>are</strong> is correct. The noun "jeans" is always plural because it describes a garment with two legs, requiring a plural verb.</p>',
        'correct': 'are',
        'choices': ['is', 'are', 'was', 'has been'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>He has acquired extensive ___ throughout his long career in tech.</strong></p>',
        'explanation': '<p><strong>knowledge</strong> is correct. "Knowledge" is an uncountable abstract noun and cannot take an "-s".</p>',
        'correct': 'knowledge',
        'choices': ['knowledges', 'knowledge', 'a knowledge', 'many knowledges'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>There are many distinct ___ of fish living in this coral reef.</strong></p>',
        'explanation': '<p><strong>species</strong> is correct. The word "species" has the exact same spelling in both its singular and plural forms.</p>',
        'correct': 'species',
        'choices': ['species', 'specie', 'specieses', 'species\''],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>The room was filled with too much ___ to hear the speaker.</strong></p>',
        'explanation': '<p><strong>noise</strong> is correct. When referring to loud sound in general, "noise" functions as an uncountable noun.</p>',
        'correct': 'noise',
        'choices': ['noises', 'noise', 'a noise', 'many noises'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>Our old wooden kitchen table is being destroyed by ___.</strong></p>',
        'explanation': '<p><strong>termites</strong> is correct. Regular plural nouns ending in "-e" simply add an "-s" to form the plural.</p>',
        'correct': 'termites',
        'choices': ['termite', 'termites', 'termitees', 'termiten'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>She drank two large ___ of water after finishing her morning run.</strong></p>',
        'explanation': '<p><strong>glasses</strong> is correct. To count liquid, we use a countable container like "glasses" in the plural form.</p>',
        'correct': 'glasses',
        'choices': ['glass', 'glasses', 'glasser', 'glasses of'],
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
            title='English Grammar: Plural and Uncountable Nouns Practice',
            master=master,
            defaults={
                'description': 'Practice test focusing on plural forms and uncountable nouns in English grammar.',
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