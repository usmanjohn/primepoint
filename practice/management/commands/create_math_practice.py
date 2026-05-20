from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
{
'text': "Qaysi son 3 ga ham, 5 ga ham qoldıqsiz bo'linadi?",
'hint': "3 va 5 ga bo'linish belgilarini eslang: oxirgi raqami 0 yoki 5 bo'lishi va raqamlar yig'indisi 3 ga bo'linishi kerak.",
'explanation': "135 sonining oxirgi raqami 5, demak u 5 ga bo'linadi. Raqamlar yig'indisi: 1 + 3 + 5 = 9. 9 soni 3 ga bo'linadi. Demak, 135 soni ham 3 ga, ham 5 ga bo'linadi.",
'correct': "135",
'choices': ["135", "124", "250", "311"]
},
{
'text': "45 284 sonini yuzliklargacha yaxlitlang.",
'hint': "Yuzliklar xonasidagi raqamdan keyingi raqamga e'tibor bering. Agar u 5 yoki undan katta bo'lsa, yuzliklar bittaga ortadi.",
'explanation': "45 284 sonida yuzliklar xonasida 2 raqami turibdi. Undan keyingi raqam 8 (5 dan katta). Shuning uchun 2 raqami 1 taga ortib 3 bo'ladi, qolgan raqamlar nolga aylanadi: 45 300.",
'correct': "45 300",
'choices': ["45 200", "45 300", "45 000", "46 000"]
},
{
'text': "Velosipedchi 12 km/h tezlik bilan 3 soatda qancha masofani bosib o'tadi?",
'hint': "Masofani topish uchun tezlikni vaqtga ko'paytiring.",
'explanation': "Masofa formulasi: S = v * t. Bu yerda v = 12 km/h, t = 3 soat. S = 12 * 3 = 36 km.",
'correct': "36 km",
'choices': ["36 km", "15 km", "4 km", "48 km"]
},
{
'text': "Quyidagi sonlardan qaysi biri 4 ga qoldıqsiz bo'linadi?",
'hint': "Sonning oxirgi ikkita raqamidan tuzilgan son 4 ga bo'linishi kerak.",
'explanation': "516 sonining oxirgi ikkita raqami 16. 16 soni 4 ga qoldıqsiz bo'linadi (16 : 4 = 4). Demak, 516 soni 4 ga bo'linadi.",
'correct': "516",
'choices': ["514", "516", "510", "519"]
},
{
'text': "874 192 sonini mingliklargacha yaxlitlang.",
'hint': "Mingliklar xonasidagi raqamdan keyingi raqamga qarang. U 1 ga teng, ya'ni 5 dan kichik.",
'explanation': "874 192 sonida mingliklar xonasida 4 turibdi. Undan keyin 1 kelgani uchun 4 o'zgarmaydi, keyingi barcha raqamlar nolga aylanadi: 874 000.",
'correct': "874 000",
'choices': ["874 000", "875 000", "870 000", "880 000"]
},
{
'text': "Avtomobil 240 km masofani 4 soatda bosib o'tdi. Uning tezligini toping.",
'hint': "Tezlikni topish uchun masofani vaqtga bo'ling.",
'explanation': "Tezlik formulasi: v = S / t. Bu yerda S = 240 km, t = 4 soat. v = 240 / 4 = 60 km/h.",
'correct': "60 km/h",
'choices': ["50 km/h", "60 km/h", "70 km/h", "80 km/h"]
},
{
'text': "Berilgan sonlardan qaysi biri 9 ga qoldıqsiz bo'linadi?",
'hint': "Sonning raqamlar yig'indisi 9 ga bo'linishi kerak.",
'explanation': "729 sonining raqamlar yig'indisi: 7 + 2 + 9 = 18. 18 soni 9 ga bo'linadi (18 : 9 = 2). Demak, 729 soni 9 ga bo'linadi.",
'correct': "729",
'choices': ["723", "726", "729", "731"]
},
{
'text': "O'nli kasrni yaxlitlang: 12,38 sonini ondalar (yondosh) xonasigacha yaxlitlang.",
'hint': "Verguldan keyingi birinchi raqamdan keyin kelayotgan raqamga qarang.",
'explanation': "12,38 sonida ondalar xonasida 3 turibdi. Undan keyingi raqam 8 bo'lgani uchun 3 raqami 1 taga ortadi: 12,4.",
'correct': "12,4",
'choices': ["12,3", "12,4", "12,0", "13,0"]
},
{
'text': "Tezyurar poyezd 90 km/h tezlik bilan 450 km masofani necha soatda bosib o'tadi?",
'hint': "Vaqtni topish uchun masofani tezlikka bo'lish kerak.",
'explanation': "Vaqt formulasi: t = S / v. Bu yerda S = 450 km, v = 90 km/h. t = 450 / 90 = 5 soat.",
'correct': "5 soat",
'choices': ["4 soat", "5 soat", "6 soat", "7 soat"]
},
{
'text': "Qaysi son 6 ga qoldıqsiz bo'linadi?",
'hint': "6 ga bo'linishi uchun son bir vaqtda ham 2 ga (juft son), ham 3 ga bo'linishi kerak.",
'explanation': "144 juft son bo'lgani uchun 2 ga bo'linadi. Raqamlar yig'indisi: 1 + 4 + 4 = 9. 9 soni 3 ga bo'lingani uchun 144 ham 3 ga bo'linadi. Demak, u 6 ga bo'linadi.",
'correct': "144",
'choices': ["144", "142", "145", "148"]
},
{
'text': "3,721 sonini yuzdan birlar xonasigacha yaxlitlang.",
'hint': "Verguldan keyingi ikkinchi raqamdan keyin turgan raqamga e'tibor bering.",
'explanation': "Yuzdan birlar xonasida 2 turibdi. Undan keyingi raqam 1 (5 dan kichik). Shuning uchun 2 o'zgarmaydi: 3,72.",
'correct': "3,72",
'choices': ["3,70", "3,72", "3,73", "3,80"]
},
{
'text': "Ikki shahar o'rtasidagi masofa 350 km. Avtobus bu masofani 70 km/h tezlik bilan necha soatda bosib o'tadi?",
'hint': "Masofani tezlikka bo'lib vaqtni toping.",
'explanation': "t = S / v poydevoriga ko'ra: t = 350 / 70 = 5 soat.",
'correct': "5 soat",
'choices': ["4 soat", "5 soat", "6 soat", "5.5 soat"]
},
{
'text': "Quyidagi sonlardan qaysi biri 8 ga qoldıqsiz bo'linadi?",
'hint': "Sonning oxirgi uchta raqamidan tuzilgan son 8 ga bo'linishi kerak.",
'explanation': "1248 sonining oxirgi uchta raqami 248. 248 : 8 = 31. Demak, 1248 soni 8 ga qoldıqsiz bo'linadi.",
'correct': "1248",
'choices': ["1244", "1246", "1248", "1250"]
},
{
'text': "682 sonini o'nliklargacha yaxlitlang.",
'hint': "O'nliklar xonasida 8 turibdi, undan keyingi raqam esa 2.",
'explanation': "Oxirgi raqam 2 bo'lgani uchun u 5 dan kichik, o'nliklar xonasi o'zgarmaydi va oxirgi raqam 0 bo'ladi: 680.",
'correct': "680",
'choices': ["680", "690", "700", "670"]
},
{
'text': "Sardor 4 m/s tezlik bilan 2 daqiqa yugurdi. U qancha masofaga yugurgan?",
'hint': "Daqiqani soniyaga o'tkazib oling: 1 daqiqa = 60 soniya.",
'explanation': "2 daqiqa = 120 soniya. Masofa: S = v * t = 4 * 120 = 480 metr.",
'correct': "480 m",
'choices': ["400 m", "480 m", "500 m", "240 m"]
},
{
'text': "Qaysi son 12 ga qoldıqsiz bo'linadi?",
'hint': "12 ga bo'linishi uchun son bir vaqtda ham 3 ga, ham 4 ga bo'linishi shart.",
'explanation': "156 sonining oxirgi ikki raqami 56 (4 ga bo'linadi). Raqamlar yig'indisi: 1 + 5 + 6 = 12 (3 ga bo'linadi). Demak, 156 soni 12 ga bo'linadi.",
'correct': "156",
'choices': ["152", "154", "156", "158"]
},
{
'text': "9 995 sonini mingliklargacha yaxlitlang.",
'hint': "Mingliklar xonasidan keyingi raqam 9 ga teng.",
'explanation': "Yaxlitlanayotgan xonadan keyin 9 turgani uchun mingliklar 1 taga ortadi: 9 + 1 = 10. Natija: 10 000.",
'correct': "10 000",
'choices': ["9 000", "9 900", "10 000", "10 100"]
},
{
'text': "Kema 25 km/h tezlik bilan 4 soat, keyin esa 30 km/h tezlik bilan 2 soat yurdi. Kema jami qancha masofani o'tgan?",
'hint': "Har bir bosqichdagi masofani alohida topib, keyin qo'shing.",
'explanation': "1-bosqich: 25 * 4 = 100 km. 2-bosqich: 30 * 2 = 60 km. Jami masofa: 100 + 60 = 160 km.",
'correct': "160 km",
'choices': ["140 km", "150 km", "160 km", "170 km"]
},
{
'text': "Quyidagi sonlardan qaysi biri 24 ga qoldıqsiz bo'linadi?",
'hint': "24 ga bo'linadigan son ham 3 ga, ham 8 ga bo'linishi kerak.",
'explanation': "168 soni 8 ga bo'linadi (168 : 8 = 21). Raqamlar yig'indisi: 1 + 6 + 8 = 15 (3 ga bo'linadi). Demak, 168 soni 24 ga bo'linadi.",
'correct': "168",
'choices': ["164", "168", "172", "160"]
},
{
'text': "0,846 sonini yuzdan birlargacha yaxlitlang.",
'hint': "Yuzdan bir xonasida 4 raqami bor, undan keyin esa 6 turibdi.",
'explanation': "Keyingi raqam 6 (5 dan katta) bo'lgani uchun 4 raqami 1 taga ko'payadi: 0,85.",
'correct': "0,85",
'choices': ["0,84", "0,85", "0,80", "0,90"]
},
{
'text': "Mototsiklchi 60 km/h tezlik bilan 2 soatda bosib o'tgan masofani, piyoda 5 km/h tezlik bilan necha soatda bosib o'tadi?",
'hint': "Avval mototsiklchi bosib o'tgan masofani toping, keyin uni piyodaning tezligiga bo'ling.",
'explanation': "Masofa: S = 60 * 2 = 120 km. Piyodaning vaqti: t = 120 / 5 = 24 soat.",
'correct': "24 soat",
'choices': ["20 soat", "22 soat", "24 soat", "26 soat"]
},
{
'text': "Qaysi son 10 ga ham, 9 ga ham qoldıqsiz bo'linadi?",
'hint': "Sonning oxiri 0 bilan tugashi va raqamlari yig'indisi 9 ga bo'linishi kerak.",
'explanation': "540 sonining oxirgi raqami 0 (10 ga bo'linadi). Raqamlar yig'indisi: 5 + 4 + 0 = 9 (9 ga bo'linadi). Demak, javob 540.",
'correct': "540",
'choices': ["500", "530", "540", "549"]
},
{
'text': "2 345 sonini o'nliklargacha yaxlitlang.",
'hint': "O'nliklar xonasida 4 turibdi, keyingi raqam esa 5.",
'explanation': "Keyingi raqam 5 bo'lgani uchun o'nliklar xonasidagi 4 raqami 1 taga ortadi: 2 350.",
'correct': "2 350",
'choices': ["2 340", "2 350", "2 300", "2 400"]
},
{
'text': "Ikki qishloqdan bir-biriga qarab bir vaqtda ikki piyoda yo'lga chiqdi. Ulardan birining tezligi 4 km/h, ikkinchisiniki 5 km/h. Agar ular 3 soatdan keyin uchrashgan bo'lsa, qishloqlar aro masofani toping.",
'hint': "Yaqinlashish tezligini topish uchun piyodalarning tezliklarini qo'shing.",
'explanation': "Yaqinlashish tezligi: 4 + 5 = 9 km/h. Umumiy masofa: S = 9 * 3 = 27 km.",
'correct': "27 km",
'choices': ["24 km", "25 km", "27 km", "30 km"]
},
{
'text': "Quyidagi sonlardan qaysi biri 3 ga bo'linadi, lekin 9 ga bo'linmaydi?",
'hint': "Raqamlar yig'indisi 3 ga bo'linsin, lekin 9 ga bo'linmasin.",
'explanation': "111 sonining raqamlar yig'indisi: 1 + 1 + 1 = 3. 3 soni 3 ga bo'linadi, lekin 9 ga bo'linmaydi.",
'correct': "111",
'choices': ["111", "117", "126", "108"]
},
{
'text': "15,75 sonini birliklargacha (butun qismigacha) yaxlitlang.",
'hint': "Birliklar xonasida 5 turibdi, verguldan keyingi birinchi raqam esa 7.",
'explanation': "Verguldan keyin 7 (5 dan katta) kelgani uchun birliklar xonasidagi 5 raqami 1 taga ortadi: 16.",
'correct': "16",
'choices': ["15", "15,7", "16", "17"]
},
{
'text': "Eshon 80 km/h tezlikda harakatlanayotgan avtomobilda 4 soat yo'l yurdi. Mo'ljallangan joyga yetib borish uchun yana 20 km qoldi. Jami masofa qancha bo'lgan?",
'hint': "Bosib o'tilgan masofaga qolgan masofani qo'shing.",
'explanation': "Bosib o'tilgan masofa: 80 * 4 = 320 km. Jami masofa: 320 + 20 = 340 km.",
'correct': "340 km",
'choices': ["320 km", "340 km", "300 km", "360 km"]
},
{
'text': "Quyidagi sonlardan qaysi biri ham 2 ga, ham 3 ga, ham 5 ga qoldıqsiz bo'linadi?",
'hint': "Son juft bo'lishi, 0 bilan tugashi va raqamlar yig'indisi 3 ga bo'linishi kerak.",
'explanation': "120 soni 0 bilan tugaydi (2 va 5 ga bo'linadi). Raqamlar yig'indisi: 1 + 2 + 0 = 3 (3 ga bo'linadi).",
'correct': "120",
'choices': ["115", "120", "124", "130"]
},
{
'text': "0,0067 sonini mingdan birlar xonasigacha yaxlitlang.",
'hint': "Mingdan birlar xonasida (verguldan keyingi uchinchi raqam) 6 turibdi.",
'explanation': "6 dan keyingi raqam 7 bo'lgani uchun 6 raqami 1 taga ortadi va 0,007 hosil bo'ladi.",
'correct': "0,007",
'choices': ["0,006", "0,007", "0,010", "0,001"]
},
{
'text': "Tezligi 15 km/h bo'lgan velosipedchi 4 soatda bosib o'tgan masofani, tezligi 60 km/h bo'lgan avtomobil qancha vaqtda bosib o'tadi?",
'hint': "Velosipedchi bosib o'tgan masofani hisoblang va uni avtomobil tezligiga bo'ling.",
'explanation': "Masofa: S = 15 * 4 = 60 km. Avtomobil vaqti: t = 60 / 60 = 1 soat.",
'correct': "1 soat",
'choices': ["1 soat", "2 soat", "0.5 soat", "1.5 soat"]
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
            title='Bo\'lish qoidalari, yahlitlash hamda masofaga oid savollar',
            master=master,
            defaults={
                'description': 'Practice on divisibility rules, rounding, and distance/speed/time problems.',
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