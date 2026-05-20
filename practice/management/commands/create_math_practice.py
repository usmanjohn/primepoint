from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice


QUESTIONS = [{'text': "43 281 sonini o'nliklargacha yaxlitlang.",'explanation': "O'nliklar xonasida 8 raqami turibdi. Undan keyingi raqam esa 1 (5 dan kichik). Shuning uchun 8 o'zgarmaydi va keyingi raqam 0 ga aylanadi: 43 280.",'correct': "43 280",'choices': ["43 200", "43 280", "43 290", "43 300"]},{'text': "8 764 sonini yuzliklargacha yaxlitlang.",'explanation': "Yuzliklar xonasida 7 raqami turibdi. Undan keyingi raqam 6 (5 yoki undan katta). Shuning uchun 7 raqami 1 taga ortib 8 bo'ladi, qolgan raqamlar 0 ga aylanadi: 8 800.",'correct': "8 800",'choices': ["8 700", "8 760", "8 800", "9 000"]},{'text': "154 912 sonini mingliklargacha yaxlitlang.",'explanation': "Mingliklar xonasida 4 raqami turibdi. Undan keyingi raqam 9 (5 dan katta). Shuning uchun 4 raqami 1 taga ortib 5 bo'ladi, undan keyingi barcha raqamlar nolga aylanadi: 155 000.",'correct': "155 000",'choices': ["154 000", "154 900", "155 000", "150 000"]},{'text': "14,28 sonini ondalar (verguldan keyingi birinchi xona) xonasigacha yaxlitlang.",'explanation': "Ondalar xonasida 2 raqami turibdi. Undan keyingi raqam 8 (5 dan katta) bo'lgani uchun 2 raqami 1 taga ortib 3 bo'ladi: 14,3.",'correct': "14,3",'choices': ["14,2", "14,3", "14,0", "14,28"]},{'text': "3,641 sonini yuzdan birlar (verguldan keyingi ikkinchi xona) xonasigacha yaxlitlang.",'explanation': "Yuzdan birlar xonasida 4 raqami turibdi. Undan keyingi raqam 1 (5 dan kichik) bo'lgani uchun 4 raqami o'zgarmaydi: 3,64.",'correct': "3,64",'choices': ["3,60", "3,64", "3,65", "3,70"]},{'text': "0,5782 sonini mingdan birlar (verguldan keyingi uchinchi xona) xonasigacha yaxlitlang.",'explanation': "Mingdan birlar xonasida 8 raqami turibdi. Undan keyingi raqam 2 (5 dan kichik) bo'lgani uchun 8 raqami o'zgarmaydi: 0,578.",'correct': "0,578",'choices': ["0,578", "0,579", "0,580", "0,570"]},{'text': "89,63 sonini birliklargacha (butun qismigacha) yaxlitlang.",'explanation': "Birliklar xonasida 9 raqami turibdi. Verguldan keyingi birinchi raqam esa 6 (5 dan katta). Shuning uchun 89 soni 1 taga ortib 90 bo'ladi.",'correct': "90",'choices': ["89", "89,6", "90", "100"]},{'text': "296 345 sonini o'n mingliklargacha yaxlitlang.",'explanation': "O'n mingliklar xonasida 9 raqami turibdi. Undan keyingi raqam 6 (5 dan katta). 9 raqami 1 taga ortganda keyingi xonaga o'tadi, natijada 29 soni 30 ga aylanadi: 300 000.",'correct': "300 000",'choices': ["290 000", "296 000", "296 300", "300 000"]},{'text': "0,075 sonini yuzdan birlargacha yaxlitlang.",'explanation': "Yuzdan birlar xonasida 7 raqami turibdi. Undan keyingi raqam 5 ga teng bo'lgani uchun 7 raqami 1 taga ortadi va 8 bo'ladi: 0,08.",'correct': "0,08",'choices': ["0,07", "0,08", "0,10", "0,075"]},{'text': "5,4197 sonini mingdan birlargacha yaxlitlang.",'explanation': "Mingdan birlar xonasida 9 raqami turibdi. Undan keyingi raqam 7 (5 dan katta). 9 raqami 1 taga ortganda o'zidan oldingi 1 raqamini 2 ga aylantiradi: 5,420 (yoki 5,42).",'correct': "5,420",'choices': ["5,419", "5,420", "5,410", "5,430"]},{'text': "1 245 sonini yuzliklargacha yaxlitlang.",'explanation': "Yuzliklar xonasida 2 raqami turibdi. Undan keyingi raqam 4 (5 dan kichik). Shuning uchun 2 o'zgarmaydi va qolgan raqamlar nolga aylanadi: 1 200.",'correct': "1 200",'choices': ["1 200", "1 240", "1 250", "1 300"]},{'text': "0,91 sonini ondalar xonasigacha yaxlitlang.",'explanation': "Ondalar xonasida 9 raqami turibdi. Undan keyingi raqam 1 (5 dan kichik) bo'lgani uchun 9 raqami o'zgarmaydi: 0,9.",'correct': "0,9",'choices': ["0,9", "1,0", "0,91", "0,8"]},{'text': "74 982 sonini o'nliklargacha yaxlitlang.",'explanation': "O'nliklar xonasida 8 raqami turibdi. Undan keyingi raqam 2 (5 dan kichik) bo'lgani uchun 8 raqami o'zgarmaydi, oxirgi raqam 0 ga aylanadi: 74 980.",'correct': "74 980",'choices': ["74 900", "74 980", "74 990", "75 000"]},{'text': "123,456 sonini birliklargacha yaxlitlang.",'explanation': "Birliklar xonasida 3 raqami turibdi. Verguldan keyingi birinchi raqam esa 4 (5 dan kichik). Shuning uchun butun qism o'zgarmaydi: 123.",'correct': "123",'choices': ["123", "124", "123,5", "123,4"]},{'text': "9 999 sonini yuzliklargacha yaxlitlang.",'explanation': "Yuzliklar xonasida 9 raqami turibdi. Undan keyingi raqam 9 (5 dan katta). Shuning uchun yuzliklar xonasi 1 taga ortadi va zanjirsimon tarzda butun son 10 000 ga aylanadi.",'correct': "10 000",'choices': ["9 900", "9 990", "10 000", "10 100"]}]




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
            title='Yahlitlash savollari',
            master=master,
            defaults={
                'description': 'Yahlitlash savollarini o\'z ichiga olgan amaliy test.',
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