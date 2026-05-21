from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

from .korean_questions import (
    quest_joy_vaqt_olmosh,
    quest_yonalish_vosita_olmosh,
    quest_harakat_qaratilgan_olmosh,
    quest_qoshish_yuklama,
    quest_taqqoslash_yuklama,
)

PRACTICES = [
    {
        'title': '5-dars: Joy va vaqt yuklamalari (에/에서/부터/까지)',
        'description': "Joy va vaqt yuklamalari (에 vs 에서, 부터, 까지) mavzusidagi amaliy test.",
        'questions': quest_joy_vaqt_olmosh,
    },
    {
        'title': '6-dars: Yo\'nalish va vosita yuklamasi (으로/로)',
        'description': "Yo'nalish va vosita yuklamasi (으로/로) mavzusidagi amaliy test.",
        'questions': quest_yonalish_vosita_olmosh,
    },
    {
        'title': '7-dars: Harakat qaratilgan yuklamalar (한테/에게/께/마다)',
        'description': "Harakat qaratilgan yuklamalar (한테, 에게, 께, 마다) mavzusidagi amaliy test.",
        'questions': quest_harakat_qaratilgan_olmosh,
    },
    {
        'title': '8-dars: Qo\'shimcha yuklamalar (도/만/밖에/쯤)',
        'description': "Qo'shimcha yuklamalar (도, 만, 밖에, 쯤) mavzusidagi amaliy test.",
        'questions': quest_qoshish_yuklama,
    },
    {
        'title': '9-dars: Taqqoslash yuklamalari (이나/나/처럼/같이/보다)',
        'description': "Taqqoslash yuklamalari (이나/나, 처럼, 같이, 보다) mavzusidagi amaliy test.",
        'questions': quest_taqqoslash_yuklama,
    },
]


class Command(BaseCommand):
    help = 'Create Korean grammar particle practice tests (lessons 5–9)'

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
            name='한국어',
            defaults={'description': '한국어 문법 및 어휘 연습'},
        )

        for practice_data in PRACTICES:
            practice, created = Practice.objects.get_or_create(
                title=practice_data['title'],
                master=master,
                defaults={
                    'description': practice_data['description'],
                    'subject': subject,
                    'level': 'hard',
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
