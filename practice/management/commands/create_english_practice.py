from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice
QUESTIONS = [
    {
        'text': '<p>Choose the correct option.</p><p><strong>Sarah is my best friend. ___ lives next door.</strong></p>',
        'explanation': '<p><strong>She</strong> is correct. "She" is the subject pronoun used for a singular female noun.</p>',
        'correct': 'She',
        'choices': ['She', 'Her', 'Hers', 'Herself'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>I can\'t find my keys. Have you seen ___?</strong></p>',
        'explanation': '<p><strong>them</strong> is correct. "Them" is the object pronoun replacing the plural noun "keys".</p>',
        'correct': 'them',
        'choices': ['it', 'they', 'them', 'their'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>That book is not mine, it is ___.</strong></p>',
        'explanation': '<p><strong>hers</strong> is correct. "Hers" is a possessive pronoun used to show ownership without a following noun.</p>',
        'correct': 'hers',
        'choices': ['her', 'hers', 'she', 'herself'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>The children cleaned the room all by ___.</strong></p>',
        'explanation': '<p><strong>themselves</strong> is correct. "Themselves" is the reflexive pronoun for "the children" (plural).</p>',
        'correct': 'themselves',
        'choices': ['themself', 'themselves', 'them', 'theirselves'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>This is the girl ___ won the competition.</strong></p>',
        'explanation': '<p><strong>who</strong> is correct. "Who" is a relative pronoun used to refer to a person as the subject of the clause.</p>',
        'correct': 'who',
        'choices': ['which', 'who', 'whose', 'whom'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>___ am going to the movies tonight.</strong></p>',
        'explanation': '<p><strong>I</strong> is correct. "I" is the subject pronoun.</p>',
        'correct': 'I',
        'choices': ['Me', 'I', 'Myself', 'Mine'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>Is this laptop ___?</strong></p>',
        'explanation': '<p><strong>yours</strong> is correct. "Yours" is the possessive pronoun replacing "your laptop".</p>',
        'correct': 'yours',
        'choices': ['you', 'your', 'yours', 'yourself'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>My brother hurt ___ while playing soccer.</strong></p>',
        'explanation': '<p><strong>himself</strong> is correct. "Himself" is the reflexive pronoun when the subject and object are the same.</p>',
        'correct': 'himself',
        'choices': ['him', 'himself', 'he', 'his'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>The dog wagged ___ tail happily.</strong></p>',
        'explanation': '<p><strong>its</strong> is correct. "Its" is the possessive adjective for a singular animal/object.</p>',
        'correct': 'its',
        'choices': ['it', 'its', 'it\'s', 'its\''],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>The teacher gave John and ___ a special task.</strong></p>',
        'explanation': '<p><strong>me</strong> is correct. "Me" is the object pronoun after the verb "gave".</p>',
        'correct': 'me',
        'choices': ['I', 'me', 'myself', 'mine'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>The house ___ I bought is very small.</strong></p>',
        'explanation': '<p><strong>that</strong> is correct. "That" or "which" is a relative pronoun for a thing.</p>',
        'correct': 'that',
        'choices': ['who', 'that', 'whose', 'whom'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>___ do you want to invite?</strong></p>',
        'explanation': '<p><strong>Whom</strong> is correct. "Whom" is the object pronoun for people, used as the object of "do you want to invite".</p>',
        'correct': 'Whom',
        'choices': ['Who', 'Whom', 'Whose', 'Which'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>That car is ___.</strong></p>',
        'explanation': '<p><strong>ours</strong> is correct. "Ours" is the possessive pronoun.</p>',
        'correct': 'ours',
        'choices': ['our', 'ours', 'us', 'ourself'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>You should trust ___.</strong></p>',
        'explanation': '<p><strong>yourself</strong> is correct. "Yourself" is the reflexive pronoun.</p>',
        'correct': 'yourself',
        'choices': ['you', 'yourself', 'your', 'yours'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>They often visit their grandparents, and ___ visit them too.</strong></p>',
        'explanation': '<p><strong>they</strong> is correct. "They" is the subject pronoun referring to the grandparents.</p>',
        'correct': 'they',
        'choices': ['them', 'they', 'their', 'themselves'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>This is the man ___ car was stolen.</strong></p>',
        'explanation': '<p><strong>whose</strong> is correct. "Whose" is the possessive relative pronoun.</p>',
        'correct': 'whose',
        'choices': ['who', 'which', 'whose', 'whom'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>___ of the answers is correct?</strong></p>',
        'explanation': '<p><strong>Which</strong> is correct. "Which" is used to ask for a choice among a specific set.</p>',
        'correct': 'Which',
        'choices': ['What', 'Who', 'Which', 'Whose'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>My mother bought a new dress for ___.</strong></p>',
        'explanation': '<p><strong>herself</strong> is correct. "Herself" is the reflexive pronoun.</p>',
        'correct': 'herself',
        'choices': ['she', 'her', 'herself', 'hers'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>Those shoes are ___.</strong></p>',
        'explanation': '<p><strong>theirs</strong> is correct. "Theirs" is the possessive pronoun.</p>',
        'correct': 'theirs',
        'choices': ['them', 'their', 'theirs', 'themselves'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>Can I have a word with you and ___?</strong></p>',
        'explanation': '<p><strong>her</strong> is correct. "Her" is the object pronoun used after the preposition "with".</p>',
        'correct': 'her',
        'choices': ['she', 'her', 'hers', 'herself'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>He is the student ___ I mentioned earlier.</strong></p>',
        'explanation': '<p><strong>whom</strong> is correct. "Whom" is the object relative pronoun.</p>',
        'correct': 'whom',
        'choices': ['who', 'whom', 'whose', 'which'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>___ are my favorite games.</strong></p>',
        'explanation': '<p><strong>These</strong> is correct. "These" is the demonstrative pronoun for nearby plural items.</p>',
        'correct': 'These',
        'choices': ['This', 'These', 'That', 'Them'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>You can keep the money, it is all ___.</strong></p>',
        'explanation': '<p><strong>yours</strong> is correct. "Yours" is the possessive pronoun.</p>',
        'correct': 'yours',
        'choices': ['you', 'your', 'yours', 'yourself'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>She always speaks highly of ___.</strong></p>',
        'explanation': '<p><strong>herself</strong> is correct. "Herself" is the reflexive pronoun.</p>',
        'correct': 'herself',
        'choices': ['she', 'her', 'herself', 'hers'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>___ knows the answer to this question?</strong></p>',
        'explanation': '<p><strong>Who</strong> is correct. "Who" is the interrogative pronoun for the subject.</p>',
        'correct': 'Who',
        'choices': ['Whom', 'Who', 'Whose', 'Which'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>My sister and I made this cake ___.</strong></p>',
        'explanation': '<p><strong>ourselves</strong> is correct. "Ourselves" is the reflexive pronoun for "my sister and I" (plural).</p>',
        'correct': 'ourselves',
        'choices': ['ourselves', 'ourself', 'us', 'ours'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>Is this chair ___?</strong></p>',
        'explanation': '<p><strong>his</strong> is correct. "His" is the possessive pronoun.</p>',
        'correct': 'his',
        'choices': ['him', 'his', 'he', 'himself'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>I love the city ___ I live in.</strong></p>',
        'explanation': '<p><strong>where</strong> is correct. "Where" is the relative adverb used to refer to a place.</p>',
        'correct': 'where',
        'choices': ['who', 'which', 'where', 'whose'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>Between you and ___, I think he is lying.</strong></p>',
        'explanation': '<p><strong>me</strong> is correct. "Me" is the object pronoun used after the preposition "between".</p>',
        'correct': 'me',
        'choices': ['I', 'me', 'myself', 'mine'],
    },
    {
        'text': '<p>Choose the correct option.</p><p><strong>___ was a very sunny day.</strong></p>',
        'explanation': '<p><strong>It</strong> is correct. "It" is the impersonal pronoun for weather.</p>',
        'correct': 'It',
        'choices': ['That', 'It', 'There', 'They'],
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
            title='English Grammar: Pronouns',
            master=master,
            defaults={
                'description': 'Test your understanding of English pronouns with this practice on subject, object, possessive, reflexive, and relative pronouns.',
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