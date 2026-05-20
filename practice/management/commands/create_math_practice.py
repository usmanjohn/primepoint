from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
{
'text': "Quyidagi sonlardan qaysi biri 2 ga qoldiqsiz bo'linadi?",
'explanation': "Juft sonlar (oxirgi raqami 0, 2, 4, 6, 8 bilan tugaydigan sonlar) 2 ga qoldiqsiz bo'linadi. 458 juft son bo'lgani uchun 2 ga bo'linadi.",
'correct': "458",
'choices': ["453", "455", "458", "459"]
},
{
'text': "Qaysi son 3 ga qoldiqsiz bo'linadi?",
'explanation': "Raqamlar yig'indisi 3 ga bo'linadigan sonlar 3 ga qoldiqsiz bo'linadi. 2 + 3 + 4 = 9. 9 soni 3 ga bo'lingani uchun 234 soni 3 ga bo'linadi.",
'correct': "234",
'choices': ["232", "233", "234", "235"]
},
{
'text': "Quyidagi sonlardan qaysi biri 4 ga qoldiqsiz bo'linadi?",
'explanation': "Sonning oxirgi ikkita raqamidan tuzilgan son 4 ga bo'linishi kerak. 724 sonining oxirgi ikki raqami 24 bo'lib, u 4 ga bo'linadi.",
'correct': "724",
'choices': ["714", "722", "724", "725"]
},
{
'text': "Qaysi son 5 ga qoldiqsiz bo'linadi?",
'explanation': "Oxirgi raqami 0 yoki 5 bilan tugaydigan sonlar 5 ga qoldiqsiz bo'linadi. 865 soni 5 bilan tugagani uchun javob 865.",
'correct': "865",
'choices': ["861", "864", "865", "869"]
},
{
'text': "Quyidagi sonlardan qaysi biri 6 ga qoldiqsiz bo'linadi?",
'explanation': "Ham 2 ga (juft son), ham 3 ga (raqamlar yig'indisi 3 ga bo'linadigan) bo'lingan son 6 ga bo'linadi. 312 juft son va raqamlar yig'indisi 3 + 1 + 2 = 6 (3 ga bo'linadi).",
'correct': "312",
'choices': ["311", "312", "314", "316"]
},
{
'text': "Qaysi son 8 ga qoldiqsiz bo'linadi?",
'explanation': "Sonning oxirgi uchta raqamidan tuzilgan son 8 ga bo'linishi kerak. 3120 sonining oxirgi uchta raqami 120 bo'lib, u 8 ga bo'linadi (120 : 8 = 15).",
'correct': "3120",
'choices': ["3110", "3116", "3120", "3124"]
},
{
'text': "Quyidagi sonlardan qaysi biri 9 ga qoldiqsiz bo'linadi?",
'explanation': "Raqamlar yig'indisi 9 ga bo'linadigan sonlar 9 ga qoldiqsiz bo'linadi. 5 + 4 + 9 = 18. 18 soni 9 ga bo'lingani uchun 549 soni 9 ga bo'linadi.",
'correct': "549",
'choices': ["543", "546", "549", "551"]
},
{
'text': "Qaysi son 10 ga qoldiqsiz bo'linadi?",
'explanation': "Oxirgi raqami faqat 0 bilan tugaydigan sonlar 10 ga qoldiqsiz bo'linadi. 1290 soni 0 bilan tugagani uchun javob 1290.",
'correct': "1290",
'choices': ["1295", "1290", "1292", "1203"]
},
{
'text': "Quyidagi sonlardan qaysi biri 12 ga qoldiqsiz bo'linadi?",
'explanation': "Bir vaqtning o'zida ham 3 ga, ham 4 ga bo'linadigan sonlar 12 ga bo'linadi. 216 sonining oxirgi ikki raqami 16 (4 ga bo'linadi) va raqamlar yig'indisi 2 + 1 + 6 = 9 (3 ga bo'linadi).",
'correct': "216",
'choices': ["210", "214", "216", "218"]
},
{
'text': "Qaysi son 24 ga qoldiqsiz bo'linadi?",
'explanation': "Bir vaqtning o'zida ham 3 ga, ham 8 ga bo'linadigan sonlar 24 ga bo'linadi. 360 soni 8 ga bo'linadi (360 : 8 = 45) va raqamlar yig'indisi 3 + 6 + 0 = 9 (3 ga bo'linadi).",
'correct': "360",
'choices': ["340", "350", "360", "370"]
},
{
'text': "Quyidagi sonlardan qaysi biri 3 ga ham, 5 ga ham qoldiqsiz bo'linadi?",
'explanation': "Son 5 bilan tugashi (5 ga bo'linishi) va raqamlar yig'indisi 3 ga bo'linishi kerak. 165 sonining raqamlar yig'indisi 1 + 6 + 5 = 12 (3 ga bo'linadi).",
'correct': "165",
'choices': ["160", "165", "170", "175"]
},
{
'text': "Qaysi son 4 ga ham, 6 ga ham qoldiqsiz bo'linadi?",
'explanation': "144 soni 4 ga bo'linadi (oxirgi ikki raqami 44). Shuningdek u juft va raqamlar yig'indisi 1 + 4 + 4 = 9 bo'lgani uchun 3 ga (demak 6 ga ham) bo'linadi.",
'correct': "144",
'choices': ["140", "144", "146", "150"]
},
{
'text': "Quyidagi sonlardan qaysi biri 15 ga qoldiqsiz bo'linadi?",
'explanation': "15 ga bo'linishi uchun son ham 3 ga, ham 5 ga bo'linishi kerak. 225 soni 5 bilan tugaydi va raqamlar yig'indisi 2 + 2 + 5 = 9 (3 ga bo'linadi).",
'correct': "225",
'choices': ["220", "225", "232", "235"]
},
{
'text': "Qaysi son 18 ga qoldiqsiz bo'linadi?",
'explanation': "18 ga bo'linishi uchun son ham 2 ga (juft), ham 9 ga bo'linishi kerak. 162 juft son va raqamlar yig'indisi 1 + 6 + 2 = 9 (9 ga bo'linadi).",
'correct': "162",
'choices': ["156", "160", "162", "164"]
},
{
'text': "Quyidagi sonlardan qaysi biri 9 ga bo'linadi, lekin 10 ga bo'linmaydi?",
'explanation': "171 sonining raqamlar yig'indisi 1 + 7 + 1 = 9 (9 ga bo'linadi), lekin oxiri 0 bilan tugamaganligi uchun 10 ga bo'linmaydi.",
'correct': "171",
'choices': ["170", "171", "180", "190"]
},
{
'text': "Qaysi son 20 ga qoldiqsiz bo'linadi?",
'explanation': "20 ga bo'linadigan sonning oxirgi raqami 0 bo'lishi va oxirgi ikkita raqamidan tuzilgan son 4 ga bo'linishi kerak. 480 sonida 80 soni 4 ga bo'linadi.",
'correct': "480",
'choices': ["430", "450", "470", "480"]
},
{
'text': "Quyidagi sonlardan qaysi biri 8 ga ham, 9 ga ham qoldiqsiz bo'linadi?",
'explanation': "720 soni 8 ga bo'linadi (720 : 8 = 90) va raqamlar yig'indisi 7 + 2 + 0 = 9 bo'lib, 9 ga ham bo'linadi.",
'correct': "720",
'choices': ["710", "718", "720", "728"]
},
{
'text': "Qaysi son ham 2 ga, ham 3 ga, ham 5 ga qoldiqsiz bo'linadi?",
'explanation': "300 soni 0 bilan tugagani uchun 2 va 5 ga bo'linadi. Raqamlar yig'indisi 3 + 0 + 0 = 3 bo'lgani uchun 3 ga ham bo'linadi.",
'correct': "300",
'choices': ["250", "285", "300", "310"]
},
{
'text': "Quyidagi sonlardan qaysi biri 12 ga bo'linadi, lekin 24 ga bo'linmaydi?",
'explanation': "180 soni 12 ga qoldiqsiz bo'linadi (180 : 12 = 15), lekin 24 ga bo'linganda qoldiq qoladi (180 : 24 = 7, qoldiq 12).",
'correct': "180",
'choices': ["120", "144", "168", "180"]
},
{
'text': "Qaysi son 36 ga qoldiqsiz bo'linadi?",
'explanation': "36 ga bo'linishi uchun son ham 4 ga, ham 9 ga bo'linishi shart. 252 sonining oxirgi ikki raqami 52 (4 ga bo'linadi) va raqamlar yig'indisi 2 + 5 + 2 = 9 (9 ga bo'linadi).",
'correct': "252",
'choices': ["240", "250", "252", "260"]
}
]




class Command(BaseCommand):
    help = 'Create a math practice test'

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
            name='Mathematics',
            defaults={'description': 'Mathematics practice'},
        )

        # Create or get the practice and ensure it is published
        practice, created = Practice.objects.get_or_create(
            title='Bo\'lish qoidalari',
            master=master,
            defaults={
                'description': 'Practice on divisibility rules for various numbers, helping students quickly determine if a number is divisible by another without performing full division.',
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