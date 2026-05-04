from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>I usually ___ to the gym before work.</strong></p>',
        'explanation': '<p><strong>go</strong> is correct. We use the Present Simple for habits and daily routines, often paired with frequency adverbs like "usually".</p>',
        'correct': 'go',
        'choices': ['go', 'am going', 'have gone', 'have been going'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>Quiet please! The baby ___ right now.</strong></p>',
        'explanation': '<p><strong>is sleeping</strong> is correct. The Present Continuous is used for actions happening at the exact moment of speaking.</p>',
        'correct': 'is sleeping',
        'choices': ['sleeps', 'is sleeping', 'has slept', 'sleep'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>___ you ever ___ to Australia?</strong></p>',
        'explanation': '<p><strong>Have / been</strong> is correct. The Present Perfect is used to ask about life experiences from the past up to the present moment.</p>',
        'correct': 'Have / been',
        'choices': ['Do / go', 'Are / going', 'Have / been', 'Has / been'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>I ___ what you are trying to say.</strong></p>',
        'explanation': '<p><strong>understand</strong> is correct. "Understand" is a stative verb (a verb of the mind/thoughts) and is generally not used in the continuous form.</p>',
        'correct': 'understand',
        'choices': ['am understanding', 'understand', 'have understood', 'understands'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>We can go out now. I ___ my homework.</strong></p>',
        'explanation': '<p><strong>have finished</strong> is correct. The Present Perfect is used for a past action that has a visible and relevant result in the present.</p>',
        'correct': 'have finished',
        'choices': ['finish', 'am finishing', 'have finished', 'finishes'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>They ___ with their friends until they find a new apartment.</strong></p>',
        'explanation': '<p><strong>are staying</strong> is correct. We use the Present Continuous for temporary, non-permanent situations.</p>',
        'correct': 'are staying',
        'choices': ['stay', 'are staying', 'have stayed', 'stays'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>Hurry up! The train ___ at 9:00 AM.</strong></p>',
        'explanation': '<p><strong>leaves</strong> is correct. The Present Simple is used for scheduled events and timetables, even if the event takes place in the future.</p>',
        'correct': 'leaves',
        'choices': ['is leaving', 'has left', 'leave', 'leaves'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>She ___ her best friend since they were in kindergarten.</strong></p>',
        'explanation': '<p><strong>has known</strong> is correct. "Know" is a stative verb. We use the Present Perfect with "since" to show a state that started in the past and continues to the present.</p>',
        'correct': 'has known',
        'choices': ['knows', 'is knowing', 'has known', 'have known'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>Because of global warming, the winters ___ warmer each year.</strong></p>',
        'explanation': '<p><strong>are getting</strong> is correct. The Present Continuous is used to describe changing, developing, or evolving situations.</p>',
        'correct': 'are getting',
        'choices': ['get', 'are getting', 'have got', 'gets'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>Water ___ at 100 degrees Celsius.</strong></p>',
        'explanation': '<p><strong>boils</strong> is correct. The Present Simple is used to express general truths, facts, and scientific laws.</p>',
        'correct': 'boils',
        'choices': ['is boiling', 'has boiled', 'boil', 'boils'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>Look at the sky! It ___ absolutely beautiful tonight.</strong></p>',
        'explanation': '<p><strong>looks</strong> is correct. Here, "look" is a stative verb meaning "appears," so we use the Present Simple.</p>',
        'correct': 'looks',
        'choices': ['is looking', 'has looked', 'look', 'looks'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>I ___ my keys. I can\'t get into my apartment!</strong></p>',
        'explanation': '<p><strong>have lost</strong> is correct. The Present Perfect connects a past action (losing the keys) to a direct present consequence (cannot enter the apartment).</p>',
        'correct': 'have lost',
        'choices': ['lose', 'am losing', 'have lost', 'has lost'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>Why ___ you always ___ my clothes without asking? It\'s so annoying!</strong></p>',
        'explanation': '<p><strong>are / taking</strong> is correct. The Present Continuous is used with "always" or "constantly" to express irritation or annoyance at a repeated action.</p>',
        'correct': 'are / taking',
        'choices': ['do / take', 'are / taking', 'have / taken', 'has / taken'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>How many emails ___ today?</strong></p>',
        'explanation': '<p><strong>have you sent</strong> is correct. The Present Perfect is used with unfinished time periods (like "today" or "this week") to talk about the quantity of things completed so far.</p>',
        'correct': 'have you sent',
        'choices': ['do you send', 'are you sending', 'have you sent', 'has you sent'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>Don\'t eat that meat! It ___ terrible.</strong></p>',
        'explanation': '<p><strong>smells</strong> is correct. "Smell" is a verb of the senses and is typically used in the Present Simple to describe a state.</p>',
        'correct': 'smells',
        'choices': ['is smelling', 'smells', 'has smelled', 'smell'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>He can\'t come to the phone right now. He ___ a shower.</strong></p>',
        'explanation': '<p><strong>is having</strong> is correct. "Have" is used here as an action verb (experiencing/taking a shower), and it is happening exactly at the moment of speaking.</p>',
        'correct': 'is having',
        'choices': ['has', 'is having', 'has had', 'have'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>We ___ Mary since she moved to London.</strong></p>',
        'explanation': '<p><strong>haven\'t seen</strong> is correct. The Present Perfect is used with "since" to indicate an action that hasn\'t occurred from a specific point in the past up to now.</p>',
        'correct': "haven't seen",
        'choices': ["don't see", "aren't seeing", "haven't seen", "hasn't seen"],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>I ___ to help you with your presentation tomorrow.</strong></p>',
        'explanation': '<p><strong>promise</strong> is correct. Verbs of declaration or communication, like "promise", "agree", "refuse", or "apologize", are used in the Present Simple.</p>',
        'correct': 'promise',
        'choices': ['am promising', 'promise', 'have promised', 'promises'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>___ the boss yet? She is waiting for your report.</strong></p>',
        'explanation': '<p><strong>Have you called</strong> is correct. The Present Perfect is used with "yet" in questions to ask if an expected action has happened by the present moment.</p>',
        'correct': 'Have you called',
        'choices': ['Do you call', 'Are you calling', 'Have you called', 'Has you called'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>They ___ to Paris next Friday. They already bought the tickets.</strong></p>',
        'explanation': '<p><strong>are flying</strong> is correct. The Present Continuous is often used for fixed, planned future arrangements.</p>',
        'correct': 'are flying',
        'choices': ['fly', 'are flying', 'have flown', 'flies'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>First, you chop the onions, and then you ___ them in a pan.</strong></p>',
        'explanation': '<p><strong>fry</strong> is correct. The Present Simple is used when giving a sequence of instructions, directions, or a recipe.</p>',
        'correct': 'fry',
        'choices': ['are frying', 'have fried', 'fry', 'fries'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>My brother ___ as a software engineer for three years.</strong></p>',
        'explanation': '<p><strong>has worked</strong> is correct. The Present Perfect is used with "for" to describe an action or state that started in the past and continues into the present.</p>',
        'correct': 'has worked',
        'choices': ['works', 'is working', 'has worked', 'have worked'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>Look at the chef! He ___ the soup to see if it needs more salt.</strong></p>',
        'explanation': '<p><strong>is tasting</strong> is correct. "Taste" is an action verb here (the chef is deliberately performing the action), so it takes the Present Continuous for an action happening now.</p>',
        'correct': 'is tasting',
        'choices': ['tastes', 'is tasting', 'has tasted', 'taste'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>This soup ___ delicious! What did you put in it?</strong></p>',
        'explanation': '<p><strong>tastes</strong> is correct. Here, "taste" is a stative verb (having a specific flavor or quality), so it takes the Present Simple.</p>',
        'correct': 'tastes',
        'choices': ['is tasting', 'tastes', 'has tasted', 'taste'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>No, thanks, I don\'t want anything to eat. I ___ already ___ lunch.</strong></p>',
        'explanation': '<p><strong>have / had</strong> is correct. The Present Perfect is used with "already" for an action that happened sooner than expected, which has an effect on the present.</p>',
        'correct': 'have / had',
        'choices': ['do / have', 'am / having', 'have / had', 'has / had'],
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