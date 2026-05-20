from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice
QUESTIONS = [
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>I am studying for my final exams ___.</strong></p>',
        'explanation': '<p><strong>right now</strong> is correct. The Present Continuous tense ("am studying") indicates an action happening at the moment of speaking.</p>',
        'correct': 'right now',
        'choices': ['right now', 'yesterday', 'tomorrow', 'every day'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>We go to the local farmer\'s market to buy fresh vegetables ___.</strong></p>',
        'explanation': '<p><strong>on weekends</strong> is correct. The Present Simple tense ("go") is used for repeated actions, habits, or routines.</p>',
        'correct': 'on weekends',
        'choices': ['on weekends', 'last week', 'right now', 'since 2010'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>Did you see that amazing wildlife documentary on TV ___?</strong></p>',
        'explanation': '<p><strong>last night</strong> is correct. The Past Simple tense ("Did you see") requires a finished, specific time in the past.</p>',
        'correct': 'last night',
        'choices': ['last night', 'tomorrow', 'lately', 'usually'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>A: How is Sarah? B: I don\'t know, I haven\'t spoken to her ___.</strong></p>',
        'explanation': '<p><strong>lately</strong> is correct. The Present Perfect tense ("haven\'t spoken") pairs well with "lately" or "recently" to talk about the time leading up to now.</p>',
        'correct': 'lately',
        'choices': ['lately', 'yesterday', 'next week', 'usually'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>Take an umbrella with you. I think it will rain ___.</strong></p>',
        'explanation': '<p><strong>later today</strong> is correct. The Future Simple tense ("will rain") requires a future time expression.</p>',
        'correct': 'later today',
        'choices': ['yesterday', 'ago', 'every day', 'later today'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>I can\'t go out with you guys tonight. I haven\'t finished my homework ___.</strong></p>',
        'explanation': '<p><strong>yet</strong> is correct. We use "yet" with the Present Perfect in negative sentences and questions to talk about something expected to happen.</p>',
        'correct': 'yet',
        'choices': ['yet', 'already', 'just', 'yesterday'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>They moved to a new house in the suburbs two months ___.</strong></p>',
        'explanation': '<p><strong>ago</strong> is correct. "Ago" is used with the Past Simple ("moved") to show how far back in the past an event happened.</p>',
        'correct': 'ago',
        'choices': ['ago', 'since', 'for', 'before'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>Mr. Davis is very experienced. He has worked at this company ___ 2015.</strong></p>',
        'explanation': '<p><strong>since</strong> is correct. The Present Perfect tense ("has worked") uses "since" to indicate the starting point of an ongoing action.</p>',
        'correct': 'since',
        'choices': ['since', 'for', 'in', 'ago'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>We are celebrating a big milestone. We have been married ___ ten years.</strong></p>',
        'explanation': '<p><strong>for</strong> is correct. The Present Perfect uses "for" to show the duration or length of time an action has been happening.</p>',
        'correct': 'for',
        'choices': ['for', 'since', 'ago', 'during'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>I was cooking dinner ___ when the power suddenly went out.</strong></p>',
        'explanation': '<p><strong>at 7 PM yesterday</strong> is correct. The Past Continuous ("was cooking") describes an action in progress at a specific moment in the past.</p>',
        'correct': 'at 7 PM yesterday',
        'choices': ['at 7 PM yesterday', 'tomorrow night', 'lately', 'right now'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>This time ___, I will be relaxing on a sunny beach in Hawaii.</strong></p>',
        'explanation': '<p><strong>next week</strong> is correct. The Future Continuous ("will be relaxing") describes an action that will be in progress at a specific time in the future.</p>',
        'correct': 'next week',
        'choices': ['next week', 'last week', 'recently', 'usually'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>She ___ forgets her keys; she is very disorganized.</strong></p>',
        'explanation': '<p><strong>always</strong> is correct. Adverbs of frequency like "always" are used with the Present Simple to describe habits or persistent traits.</p>',
        'correct': 'always',
        'choices': ['always', 'never', 'yesterday', 'right now'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>Watch out! Don\'t step there, I have ___ washed the floor.</strong></p>',
        'explanation': '<p><strong>just</strong> is correct. We use "just" with the Present Perfect to express that an action was completed a very short time ago.</p>',
        'correct': 'just',
        'choices': ['just', 'yet', 'yesterday', 'tomorrow'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>We are flying to Paris ___. We already have our hotel booked.</strong></p>',
        'explanation': '<p><strong>next Monday</strong> is correct. The Present Continuous can be used with a future time expression to talk about fixed future plans or arrangements.</p>',
        'correct': 'next Monday',
        'choices': ['next Monday', 'last Monday', 'usually', 'since Monday'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>The technology company was officially founded ___.</strong></p>',
        'explanation': '<p><strong>in 1998</strong> is correct. The Past Simple ("was founded") is used with "in + year" for a completed past event.</p>',
        'correct': 'in 1998',
        'choices': ['in 1998', 'since 1998', 'for 1998', 'tomorrow'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>A: Have you ___ eaten Thai food? B: Yes, many times!</strong></p>',
        'explanation': '<p><strong>ever</strong> is correct. We use "ever" with the Present Perfect in questions to ask about life experiences.</p>',
        'correct': 'ever',
        'choices': ['ever', 'never', 'recently', 'yesterday'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>The dentist advised him to brush his teeth twice ___.</strong></p>',
        'explanation': '<p><strong>a day</strong> is correct. "Twice a day" shows frequency, which pairs perfectly with the routine implied in the sentence.</p>',
        'correct': 'a day',
        'choices': ['a day', 'tomorrow', 'ago', 'yet'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>Please take a seat. The doctor will see you ___.</strong></p>',
        'explanation': '<p><strong>soon</strong> is correct. "Will see" is Future Simple, and "soon" is an adverb indicating a short time from now into the future.</p>',
        'correct': 'soon',
        'choices': ['soon', 'yesterday', 'lately', 'ago'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>I love this author. I have read three of her books ___ this month.</strong></p>',
        'explanation': '<p><strong>so far</strong> is correct. The Present Perfect is used with unfinished time periods ("this month") and "so far" to count achievements up to now.</p>',
        'correct': 'so far',
        'choices': ['so far', 'yesterday', 'next', 'ago'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>I met him ___ I was living in Tokyo.</strong></p>',
        'explanation': '<p><strong>when</strong> is correct. "When" introduces a time clause in the past, linking the Past Simple ("met") to the Past Continuous background ("was living").</p>',
        'correct': 'when',
        'choices': ['when', 'since', 'for', 'tomorrow'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>I am living with my parents ___ until I can find my own apartment.</strong></p>',
        'explanation': '<p><strong>at the moment</strong> is correct. The Present Continuous ("am living") is used for temporary situations happening around now.</p>',
        'correct': 'at the moment',
        'choices': ['at the moment', 'yesterday', 'next year', 'usually'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>A: When did you buy that nice car? B: I bought it a few days ___.</strong></p>',
        'explanation': '<p><strong>ago</strong> is correct. "Ago" means "before now" and is always used with the Past Simple tense.</p>',
        'correct': 'ago',
        'choices': ['ago', 'since', 'yet', 'recently'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>There have been a lot of changes in the office management ___.</strong></p>',
        'explanation': '<p><strong>recently</strong> is correct. The Present Perfect ("have been") pairs with "recently" to talk about events happening in the period closely leading up to now.</p>',
        'correct': 'recently',
        'choices': ['recently', 'tomorrow', 'last year', 'ago'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>I promise I will finish the financial report ___.</strong></p>',
        'explanation': '<p><strong>in two days</strong> is correct. The Future Simple ("will finish") uses "in + time period" to say how long from now something will happen.</p>',
        'correct': 'in two days',
        'choices': ['in two days', 'two days ago', 'since two days', 'yesterday'],
    },
    {
        'text': '<p>Choose the correct time expression.</p><p><strong>I was working in the garden ___ so I didn\'t hear the phone ring.</strong></p>',
        'explanation': '<p><strong>all day yesterday</strong> is correct. The Past Continuous ("was working") emphasizes the duration of an action in the past.</p>',
        'correct': 'all day yesterday',
        'choices': ['all day yesterday', 'tomorrow', 'right now', 'usually'],
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
            title='English Basic Choosing timeline based on tenses',
            master=master,
            defaults={
                'description': 'Prtice using the correct form of timeline and tenses in various contexts.',
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