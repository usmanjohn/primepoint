from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice
QUESTIONS = [
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>I ___ my keys yesterday, so I had to call a locksmith.</strong></p>',
        'explanation': '<p><strong>lost</strong> is correct. The Past Simple is used for completed actions at a specific time in the past ("yesterday").</p>',
        'correct': 'lost',
        'choices': ['lose', 'am losing', 'have lost', 'lost'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>While I ___ a book, the telephone rang.</strong></p>',
        'explanation': '<p><strong>was reading</strong> is correct. The Past Continuous is used for a longer background action that was interrupted by a shorter action in the Past Simple.</p>',
        'correct': 'was reading',
        'choices': ['read', 'was reading', 'am reading', 'have read'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>She ___ in this neighborhood since she was a child.</strong></p>',
        'explanation': '<p><strong>has lived</strong> is correct. The Present Perfect connects the past to the present, showing an action that started in the past and continues today, especially with "since".</p>',
        'correct': 'has lived',
        'choices': ['lives', 'lived', 'has lived', 'was living'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>By the time we arrived at the cinema, the movie ___.</strong></p>',
        'explanation': '<p><strong>had started</strong> is correct. The Past Perfect is used to show that one past action happened before another past action.</p>',
        'correct': 'had started',
        'choices': ['started', 'has started', 'had started', 'starts'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>William Shakespeare ___ many famous plays and sonnets.</strong></p>',
        'explanation': '<p><strong>wrote</strong> is correct. The Past Simple is used for actions completed by people who are no longer living.</p>',
        'correct': 'wrote',
        'choices': ['writes', 'wrote', 'has written', 'had written'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>I usually ___ coffee in the morning, but today I am drinking tea.</strong></p>',
        'explanation': '<p><strong>drink</strong> is correct. The Present Simple is used for regular habits and routines.</p>',
        'correct': 'drink',
        'choices': ['drink', 'drank', 'have drunk', 'am drinking'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>What ___ at 8:00 PM last night?</strong></p>',
        'explanation': '<p><strong>were you doing</strong> is correct. The Past Continuous is used to ask about an action that was in progress at a specific time in the past.</p>',
        'correct': 'were you doing',
        'choices': ['did you do', 'were you doing', 'have you done', 'are you doing'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>They ___ their project two days ago.</strong></p>',
        'explanation': '<p><strong>finished</strong> is correct. "Two days ago" points to a specific, completed time in the past, requiring the Past Simple.</p>',
        'correct': 'finished',
        'choices': ['finish', 'have finished', 'finished', 'had finished'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>I ___ sushi before. This is my first time!</strong></p>',
        'explanation': '<p><strong>have never eaten</strong> is correct. The Present Perfect is used to talk about life experiences (or lack thereof) up to the present moment.</p>',
        'correct': 'have never eaten',
        'choices': ['never ate', 'am never eating', 'have never eaten', 'had never eaten'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>He ___ a shower when the hot water suddenly stopped.</strong></p>',
        'explanation': '<p><strong>was taking</strong> is correct. The Past Continuous describes the ongoing action that was interrupted.</p>',
        'correct': 'was taking',
        'choices': ['took', 'takes', 'has taken', 'was taking'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>Look outside! It ___ quite heavily.</strong></p>',
        'explanation': '<p><strong>is snowing</strong> is correct. The Present Continuous is used for actions happening right now, at the moment of speaking.</p>',
        'correct': 'is snowing',
        'choices': ['snows', 'snowed', 'is snowing', 'was snowing'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>I ___ dinner by the time my roommates got home.</strong></p>',
        'explanation': '<p><strong>had already cooked</strong> is correct. The Past Perfect shows the cooking was completed before the roommates arrived.</p>',
        'correct': 'had already cooked',
        'choices': ['already cooked', 'have already cooked', 'had already cooked', 'was already cooking'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>The Earth ___ around the sun.</strong></p>',
        'explanation': '<p><strong>goes</strong> is correct. The Present Simple is used for general truths and scientific facts.</p>',
        'correct': 'goes',
        'choices': ['went', 'goes', 'is going', 'has gone'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>How long ___ for the bus? You look freezing!</strong></p>',
        'explanation': '<p><strong>have you been waiting</strong> is correct. The Present Perfect Continuous emphasizes the duration of an action that started in the past and continues up to now.</p>',
        'correct': 'have you been waiting',
        'choices': ['are you waiting', 'did you wait', 'have you been waiting', 'had you waited'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>We ___ to a fantastic restaurant last weekend.</strong></p>',
        'explanation': '<p><strong>went</strong> is correct. The Past Simple is required because "last weekend" is a specific finished time.</p>',
        'correct': 'went',
        'choices': ['go', 'have gone', 'went', 'were going'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>He ___ his glasses while he was washing the dishes.</strong></p>',
        'explanation': '<p><strong>dropped</strong> is correct. The Past Simple is used for the short, completed action that interrupted the longer background action.</p>',
        'correct': 'dropped',
        'choices': ['drops', 'dropped', 'was dropping', 'has dropped'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>I ___ three cups of coffee so far today.</strong></p>',
        'explanation': '<p><strong>have drunk</strong> is correct. The Present Perfect is used for unfinished time periods ("so far today") to show how much has been completed.</p>',
        'correct': 'have drunk',
        'choices': ['drank', 'drink', 'was drinking', 'have drunk'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>When he was a child, he ___ soccer every afternoon.</strong></p>',
        'explanation': '<p><strong>played</strong> is correct. The Past Simple is used to describe past habits or repeated actions in the past.</p>',
        'correct': 'played',
        'choices': ['plays', 'played', 'has played', 'had played'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>Sorry, I can\'t talk right now. I ___ into a meeting.</strong></p>',
        'explanation': '<p><strong>am walking</strong> is correct. The Present Continuous describes an action happening at this exact moment.</p>',
        'correct': 'am walking',
        'choices': ['walk', 'walked', 'am walking', 'was walking'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>They ___ each other since they met at university in 2015.</strong></p>',
        'explanation': '<p><strong>have known</strong> is correct. "Know" is a stative verb, so we use the Present Perfect (not continuous) with "since" for a state continuing up to the present.</p>',
        'correct': 'have known',
        'choices': ['know', 'knew', 'have known', 'have been knowing'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>I realized I ___ my wallet at home when I went to pay for the groceries.</strong></p>',
        'explanation': '<p><strong>had left</strong> is correct. The Past Perfect indicates that leaving the wallet happened before realizing it at the store.</p>',
        'correct': 'had left',
        'choices': ['leave', 'left', 'have left', 'had left'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>She always ___ her keys. It drives me crazy!</strong></p>',
        'explanation': '<p><strong>is always losing</strong> is correct. The Present Continuous with "always" expresses annoyance at a repeated habit.</p>',
        'correct': 'is always losing',
        'choices': ['always loses', 'is always losing', 'has always lost', 'always lost'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>My grandparents ___ married for 50 years. They are celebrating their anniversary today.</strong></p>',
        'explanation': '<p><strong>have been</strong> is correct. The Present Perfect shows a state that began in the past and continues into the present.</p>',
        'correct': 'have been',
        'choices': ['were', 'are', 'have been', 'had been'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>Last night, while my sister was watching TV, I ___ for my exams.</strong></p>',
        'explanation': '<p><strong>was studying</strong> is correct. The Past Continuous is used to describe two parallel actions happening at the same time in the past.</p>',
        'correct': 'was studying',
        'choices': ['study', 'studied', 'was studying', 'have studied'],
    },
    {
        'text': '<p>Choose the correct verb form.</p><p><strong>Oh no! I ___ my phone screen. Can you see the crack?</strong></p>',
        'explanation': '<p><strong>have broken</strong> is correct. The Present Perfect connects a past action to a visible present result.</p>',
        'correct': 'have broken',
        'choices': ['broke', 'break', 'was breaking', 'have broken'],
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
            title='English Basic: Past vs Present Tense',
            master=master,
            defaults={
                'description': 'Practice using the correct form of the Tenses in various contexts.',
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