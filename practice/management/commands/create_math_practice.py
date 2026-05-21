from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice
QUESTIONS = [
    {
        'text': "$\frac{3}{8} + \frac{1}{4}$ yig'indisini hisoblang.",
        'explanation': "Kastlarni qo'shish uchun umumiy maxrajga keltiramiz. $\frac{1}{4}$ kasrning surat va maxrajini 2 ga ko'paytiramiz: $\frac{2}{8}$. Yig'indi: $\frac{3}{8} + \frac{2}{8} = \frac{5}{8}$.",
        'correct': "5/8",
        'choices': ["1/3", "4/12", "5/8", "7/8"]
    },
    {
        'text': "$\frac{7}{10} - \frac{2}{5}$ ayirmani hisoblang.",
        'explanation': "Umumiy maxraj 10 bo'ladi. $\frac{2}{5}$ kasrni 2 ga ko'paytirsak, $\frac{4}{10}$ bo'ladi. Ayirma: $\frac{7}{10} - \frac{4}{10} = \frac{3}{10}$.",
        'correct': "3/10",
        'choices': ["5/5", "3/10", "1/2", "9/10"]
    },
    {
        'text': "$\frac{5}{6}$ va $\frac{3}{4}$ kasrlarini taqqoslang.",
        'explanation': "Umumiy maxraj 12 ga keltiramiz: $\frac{5}{6} = \frac{10}{12}$ va $\frac{3}{4} = \frac{9}{12}$. Surati katta kasr katta bo'ladi, ya'ni $\frac{10}{12} > \frac{9}{12}$, demak $\frac{5}{6} > \frac{3}{4}$.",
        'correct': "5/6 > 3/4",
        'choices': ["5/6 < 3/4", "5/6 > 3/4", "5/6 = 3/4", "Taqqoslab bo'lmaydi"]
    },
    {
        'text': "$\frac{17}{5}$ noto'g'ri kasrni aralash kasr ko'rinishida yozing.",
        'explanation': "17 ni 5 ga bo'lamiz: to'liqsiz bo'linma 3, qoldiq 2 bo'ladi. Demak, $3\frac{2}{5}$.",
        'correct': "3 butun 2/5",
        'choices': ["2 butun 3/5", "3 butun 2/5", "5 butun 2/3", "3 butun 1/5"]
    },
    {
        'text': "$4\frac{2}{3}$ aralash kasrni noto'g'ri kasrga aylantiring.",
        'explanation': "Butun qismni maxrajga ko'paytirib, suratni qo'shamiz va maxrajning o'zini qoldiramiz: $4 \cdot 3 + 2 = 14$. Natija: $\frac{14}{3}$.",
        'correct': "14/3",
        'choices': ["11/3", "14/3", "12/3", "8/3"]
    },
    {
        'text': "$\frac{4}{9} \cdot \frac{3}{8}$ ko'paytmani hisoblang.",
        'explanation': "Surat va maxrajlarni ko'paytirishdan oldin qisqartiramiz: 4 va 8 qisqarib maxrajda 2 qoladi, 3 va 9 qisqarib maxrajda 3 qoladi. Natija: $\frac{1 \cdot 1}{3 \cdot 2} = \frac{1}{6}$.",
        'correct': "1/6",
        'choices': ["12/72", "7/17", "1/6", "2/9"]
    },
    {
        'text': "$\frac{5}{12} : \frac{10}{3}$ bo'linmani hisoblang.",
        'explanation': "Bo'lish uchun birinchi kasrni ikkinchi kasrning teskarisiga ko'paytiramiz: $\frac{5}{12} \cdot \frac{3}{10}$. 5 bilan 10 qisqaradi (2 qoladi), 3 bilan 12 qisqaradi (4 qoladi). Natija: $\frac{1}{4 \cdot 2} = \frac{1}{8}$.",
        'correct': "1/8",
        'choices': ["1/8", "25/18", "50/36", "1/4"]
    },
    {
        'text': "$2\frac{1}{2} + 1\frac{1}{3}$ yig'indisini hisoblang.",
        'explanation': "Aralash kasrlarni noto'g'ri kasrga aylantiramiz: $\frac{5}{2} + \frac{4}{3}$. Umumiy maxraj 6: $\frac{15}{6} + \frac{8}{6} = \frac{23}{6} = 3\frac{5}{6}$.",
        'correct': "3 butun 5/6",
        'choices': ["3 butun 2/5", "3 butun 5/6", "4 butun 1/6", "3 butun 1/3"]
    },
    {
        'text': "$5 - 2\frac{3}{7}$ ayirmani hisoblang.",
        'explanation': "5 butun sonni $4\frac{7}{7}$ ko'rinishida yozamiz. Ayirma: $4\frac{7}{7} - 2\frac{3}{7} = 2\frac{4}{7}$.",
        'correct': "2 butun 4/7",
        'choices': ["3 butun 4/7", "2 butun 3/7", "2 butun 4/7", "3 butun 3/7"]
    },
    {
        'text': "$1\frac{3}{5} \cdot 2\frac{1}{2}$ ko'paytmani hisoblang.",
        'explanation': "Kasrlarni noto'g'ri kasrga aylantiramiz: $\frac{8}{5} \cdot \frac{5}{2}$. 5 lar qisqarib ketadi, 8 ni 2 ga bo'lsak 4 kelib chiqadi.",
        'correct': "4",
        'choices': ["2 butun 3/10", "3", "4", "3 butun 4/5"]
    },
    {
        'text': "$3\frac{3}{4} : 1\frac{1}{4}$ bo'linmani hisoblang.",
        'explanation': "Noto'g'ri kasrga aylantiramiz: $\frac{15}{4} : \frac{5}{4}$. Ko'paytirishga o'tamiz: $\frac{15}{4} \cdot \frac{4}{5}$. 4 lar qisqaradi, 15 ni 5 ga bo'lsak 3 chiqadi.",
        'correct': "3",
        'choices': ["2", "3", "4", "3 butun 1/2"]
    },
    {
        'text': "$\frac{45}{60}$ kasrni qisqartirib, eng sodda ko'rinishga keltiring.",
        'explanation': "45 va 60 sonlarining eng katta umumiy bo'luvchisi (EKUB) 15 dir. Surat va maxrajni 15 ga bo'lamiz: $\frac{45:15}{60:15} = \frac{3}{4}$.",
        'correct': "3/4",
        'choices': ["9/12", "5/6", "3/4", "15/20"]
    },
    {
        'text': "Quyidagi kasrlardan qaysi biri to'g'ri kasr hisoblanadi?",
        'explanation': "Surati maxrajidan kichik bo'lgan kasr to'g'ri kasr deyiladi. $\frac{8}{9}$ kasrda $8 < 9$, shuning uchun u to'g'ri kasr.",
        'correct': "8/9",
        'choices': ["9/8", "8/9", "5/5", "11/7"]
    },
    {
        'text': "Quyidagi kasrlardan qaysi biri noto'g'ri kasr hisoblanadi?",
        'explanation': "Surati maxrajiga teng yoki undan katta bo'lgan kasr noto'g'ri kasr deyiladi. $\frac{7}{6}$ kasrda $7 > 6$.",
        'correct': "7/6",
        'choices': ["5/6", "1/2", "7/6", "3/4"]
    },
    {
        'text': "Maftuna kitobning $\frac{2}{7}$ qismini dushanba kuni, $\frac{3}{7}$ qismini seshanba kuni o'qidi. Kitobning qancha qismi o'qilmay qoldi?",
        'explanation': "O'qilgan qism: $\frac{2}{7} + \frac{3}{7} = \frac{5}{7}$. Butun kitob 1 ga teng, ya'ni $\frac{7}{7}$. Qolgan qism: $\frac{7}{7} - \frac{5}{7} = \frac{2}{7}$.",
        'correct': "2/7",
        'choices': ["5/7", "2/7", "1/7", "4/7"]
    },
    {
        'text': "Sonning $\frac{3}{4}$ qismi 60 ga teng. Shu sonning o'zini toping.",
        'explanation': "Qismi bo'yicha sonni topish uchun berilgan qiymatni kasrning suratiga bo'lib, maxrajiga ko'paytiramiz: $60 : 3 \cdot 4 = 20 \cdot 4 = 80$.",
        'correct': "80",
        'choices': ["45", "60", "80", "120"]
    },
    {
        'text': "120 sonining $\frac{2}{5}$ qismini toping.",
        'explanation': "Sonning qismini topish uchun sonni kasrga ko'paytiramiz: $120 \cdot \frac{2}{5} = (120 : 5) \cdot 2 = 24 \cdot 2 = 48$.",
        'correct': "48",
        'choices': ["24", "48", "60", "72"]
    },
    {
        'text': "$\frac{1}{2} + \frac{1}{3} + \frac{1}{6}$ ifodaning qiymatini toping.",
        'explanation': "Umumiy maxraj 6 bo'ladi. Kasrlarni keltiramiz: $\frac{3}{6} + \frac{2}{6} + \frac{1}{6} = \frac{6}{6} = 1$.",
        'correct': "1",
        'choices': ["1/11", "5/6", "1", "1 butun 1/6"]
    },
    {
        'text': "$3\frac{1}{2} - 1\frac{3}{4}$ ayirmani hisoblang.",
        'explanation': "Noto'g'ri kasrga aylantiramiz: $\frac{7}{2} - \frac{7}{4}$. Umumiy maxraj 4: $\frac{14}{4} - \frac{7}{4} = \frac{7}{4} = 1\frac{3}{4}$.",
        'correct': "1 butun 3/4",
        'choices': ["2 butun 1/4", "1 butun 3/4", "1 butun 1/2", "2 butun 1/2"]
    },
    {
        'text': "$6 : \frac{3}{4}$ bo'linmani hisoblang.",
        'explanation': "Butun sonni kasrga bo'lish uchun uni teskari kasrga ko'paytiramiz: $6 \cdot \frac{4}{3} = (6 : 3) \cdot 4 = 2 \cdot 4 = 8$.",
        'correct': "8",
        'choices': ["4/18", "4.5", "8", "9"]
    },
    {
        'text': "$\frac{x}{8} = \frac{15}{24}$ bo'lsa, x ning qiymatini toping.",
        'explanation': "Proporsiya xossasidan foydalanamiz yoki maxrajlarni solishtiramiz. 24 soni 8 dan 3 marta katta. Demak x ni topish uchun 15 ni 3 ga bo'lamiz: $15 : 3 = 5$.",
        'correct': "5",
        'choices': ["3", "5", "10", "15"]
    },
    {
        'text': "$\frac{7}{9}$ kasrga qanday kasr qo'shilsa, 2 hosil bo'ladi?",
        'explanation': "Noma'lum kasrni topish uchun 2 dan $\frac{7}{9}$ ni ayiramiz: $2 - \frac{7}{9} = 1\frac{9}{9} - \frac{7}{9} = 1\frac{2}{9} = \frac{11}{9}$.",
        'correct': "11/9",
        'choices': ["2/9", "11/9", "5/9", "16/9"]
    },
    {
        'text': "$(\frac{1}{2})^3$ ifodaning qiymatini toping.",
        'explanation': "Kasrni kubga ko'tarish uchun uning surati va maxrajini alohida kubga ko'taramiz: $\frac{1^3}{2^3} = \frac{1}{8}$.",
        'correct': "1/8",
        'choices': ["1/6", "1/8", "3/6", "3/2"]
    },
    {
        'text': "$2\frac{2}{3}$ soniga teskari bo'lgan sonni toping.",
        'explanation': "Dastlab aralash kasrni noto'g'ri kasrga aylantiramiz: $2\frac{2}{3} = \frac{8}{3}$. Unga teskari son surat va maxrajining o'rni almashgan holatidir, ya'ni $\frac{3}{8}$.",
        'correct': "3/8",
        'choices': ["-2 butun 2/3", "3/8", "8/3", "2/8"]
    },
    {
        'text': "Kvadratning perimetri $\frac{4}{5}$ metrga teng. Uning yuzini toping.",
        'explanation': "Kvadratning tomonini topamiz: $a = P : 4 = \frac{4}{5} : 4 = \frac{1}{5}$ metr. Yuzi: $S = a^2 = (\frac{1}{5})^2 = \frac{1}{25}$ m².",
        'correct': "1/25",
        'choices': ["1/5", "1/25", "16/25", "4/25"]
    },
    {
        'text': "$\frac{3}{5}$ qismi $\frac{9}{10}$ ga teng bo'lgan sonni toping.",
        'explanation': "Sonni topish uchun $\frac{9}{10}$ ni $\frac{3}{5}$ ga bo'lamiz: $\frac{9}{10} \cdot \frac{5}{3} = \frac{9 \cdot 5}{10 \cdot 3} = \frac{3 \cdot 1}{2 \cdot 1} = \frac{3}{2} = 1\frac{1}{2}$.",
        'correct': "1 butun 1/2",
        'choices': ["27/50", "1 butun 1/2", "2/3", "2"]
    },
    {
        'text': "Idishning $\frac{3}{8}$ qismi suv bilan to'ldirilgan. Idishni to'ldirish uchun yana 15 litr suv kerak. Idishning umumiy hajmi necha litr?",
        'explanation': "Bo'sh qismi: $1 - \frac{3}{8} = \frac{5}{8}$ qism. Demak, idishning $\frac{5}{8}$ qismi 15 litrga teng. Umumiy hajm: $15 : 5 \cdot 8 = 24$ litr.",
        'correct': "24",
        'choices': ["24", "32", "40", "48"]
    },
    {
        'text': "$2\frac{1}{5} \cdot \frac{5}{11} - \frac{1}{2}$ ifodaning qiymatini toping.",
        'explanation': "Birinchi ko'paytirishni bajaramiz: $2\frac{1}{5} = \frac{11}{5}$. $\frac{11}{5} \cdot \frac{5}{11} = 1$. Keyin ayiramiz: $1 - \frac{1}{2} = \frac{1}{2}$.",
        'correct': "1/2",
        'choices': ["0", "1/2", "1", "1 butun 1/2"]
    },
    {
        'text': "Quyidagi kasrlardan qaysi biri eng katta?",
        'explanation': "Maxrajlari bir xil bo'lgan kasrlarning surati kattasi katta bo'ladi. $\frac{8}{11}$ ning surati eng katta.",
        'correct': "8/11",
        'choices': ["3/11", "5/11", "8/11", "7/11"]
    },
    {
        'text': "$\frac{2}{3}$ va $\frac{3}{4}$ kasrlari orasida joylashgan kasrni toping.",
        'explanation': "Kasrlarni maxraji 24 bo'lgan ko'rinishga keltiramiz: $\frac{2}{3} = \frac{16}{24}$ va $\frac{3}{4} = \frac{18}{24}$. Ularning orasida $\frac{17}{24}$ kasri bor.",
        'correct': "17/24",
        'choices': ["5/12", "13/24", "17/24", "19/24"]
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
            title='Kasrlar va Aralash Kasrlar Amaliy Testi',
            master=master,
            defaults={
                'description': 'Kasrlar, aralash kasrlarni ichiga olgan amaliy test.',
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