from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
    {
        'text': "<p>Omborda 345 t kartoshka bor edi[cite: 1]. Birinchi haftada 27 t, ikkinchi haftada esa birinchi haftaga qaraganda 8 t kam kartoshka sotuvga chiqarildi[cite: 1]. Omborda necha tonna kartoshka qoldi?[cite: 1]</p>",
        'hint': "<p>Amallarni bosqichma-bosqich bajaring.</p>",
        'explanation': "<p>Ikkinchi haftada 27 - 8 = 19 t sotilgan[cite: 1]. Jami sotilgani: 27 + 19 = 46 t[cite: 1]. Omborda qolgani: 345 - 46 = 299 t[cite: 1].</p>",
        'correct': "299 t",
        'choices': ["310 t", "299 t", "291 t", "318 t"]
    },
    {
        'text': "<p>AB kesmani C va D nuqtalar ketma-ket kelgan AC, CD va DB qismlarga ajratadi[cite: 1]. Agar AC kesma uzunligi 34 mm, CD kesma AC kesmadan 12 mm qisqa, DB kesma esa AD dan 25 mm qisqa bo'lsa, AB kesma uzunligini toping[cite: 1].</p>",
        'hint': "<p>Har bir kesma qismining uzunligini alohida toping.</p>",
        'explanation': "<p>CD = 34 - 12 = 22 mm[cite: 1]. AD = AC + CD = 34 + 22 = 56 mm[cite: 1]. DB = 56 - 25 = 31 mm[cite: 1]. Umumiy uzunlik AB = 34 + 22 + 31 = 87 mm[cite: 1].</p>",
        'correct': "87 mm",
        'choices': ["75 mm", "87 mm", "92 mm", "101 mm"]
    },
    {
        'text': "<p>Tenglamani yeching: (x + 43) - 23 = 52[cite: 1].</p>",
        'hint': "<p>Noma'lum qatnashgan qavsni yaxlit deb oling.</p>",
        'explanation': "<p>Tenglamaning chap qismini soddalashtiramiz: x + 43 - 23 = x + 20[cite: 1]. Bundan x + 20 = 52 kelib chiqadi[cite: 1]. x = 52 - 20 = 32[cite: 1].</p>",
        'correct': "32",
        'choices': ["25", "32", "72", "45"]
    },
    {
        'text': "<p>Botir bir son o'yladi[cite: 1]. Agar unga 74 ni qo'shib, hosil bo'lgan yig'indiga yana 21 qo'shilsa, 142 hosil bo'ladi[cite: 1]. Botir qaysi sonni o'ylagan?[cite: 1]</p>",
        'hint': "<p>Teskari amallar yordamida yeching.</p>",
        'explanation': "<p>Tenglama tuzamiz: x + 74 + 21 = 142[cite: 1]. Soddalashtirsak: x + 95 = 142. Bundan x = 142 - 95 = 47[cite: 1].</p>",
        'correct': "47",
        'choices': ["57", "37", "47", "63"]
    },
    {
        'text': "<p>Quyidagi ikkita sondan qaysi biri katta? 6 877 500 600 yoki 6 876 999 999[cite: 1].</p>",
        'hint': "<p>Sonlarni xonalar bo'yicha taqqoslang.</p>",
        'explanation': "<p>Millionlar sinfidagi raqamlarni taqqoslaganda 6877 million 6876 milliondan kattaligi ko'rinadi[cite: 1]. Demak, birinchi son katta.</p>",
        'correct': "6 877 500 600",
        'choices': ["6 876 999 999", "6 877 500 600", "Ikkalasi teng", "Aniqlab bo'lmaydi"]
    },
    {
        'text': "<p>Amallarni bajaring: 314 - (114 + 77)[cite: 1].</p>",
        'hint': "<p>Sondan yig'indini ayirish xossasidan foydalaning.</p>",
        'explanation': "<p>Qoida bo'yicha: 314 - 114 - 77 = 200 - 77 = 123[cite: 1].</p>",
        'correct': "123",
        'choices': ["277", "123", "200", "133"]
    },
    {
        'text': "<p>Hadichaning 2500 so'm puli bor edi[cite: 1]. U 500 so'mga daftar va 600 so'mga muzqaymoq sotib oldi[cite: 1]. Hadichaning yana qancha puli qoldi?</p>",
        'hint': "<p>Jami xarajatni topib, umumiy puldan ayiring.</p>",
        'explanation': "<p>Xarid jami: 500 + 600 = 1100 so'm[cite: 1]. Qolgan pul: 2500 - 1100 = 1400 so'm[cite: 1].</p>",
        'correct': "1400 so'm",
        'choices': ["1100 so'm", "1500 so'm", "1400 so'm", "1000 so'm"]
    },
    {
        'text': "<p>Tenglamani yeching: (122 + x) - 291 = 157[cite: 1].</p>",
        'hint': "<p>Avval qavs ichidagi yig'indini toping.</p>",
        'explanation': "<p>Noma'lum kamayuvchini topish uchun ayiriluvchini ayirmaga qo'shamiz: 122 + x = 157 + 291 = 448[cite: 1]. x = 448 - 122 = 326[cite: 1].</p>",
        'correct': "326",
        'choices': ["326", "236", "418", "168"]
    },
    {
        'text': "<p>Asqar Samarqanddan Toshkentga tezligi 100 km/soat bo'lgan yengil avtomashinada 3 soatda yetib keldi[cite: 1]. Toshkentdan Samarqandga tezligi 75 km/soat bo'lgan avtobusda qaytdi[cite: 1]. Asqar necha soatda Toshkentdan Samarqandga yetib kelgan?[cite: 1]</p>",
        'hint': "<p>Avval shaharlar orasidagi masofani hisoblang.</p>",
        'explanation': "<p>Masofa S = v * t = 100 * 3 = 300 km[cite: 1]. Qaytishdagi vaqt t = S / v = 300 / 75 = 4 soat[cite: 1].</p>",
        'correct': "4 soatda",
        'choices': ["2.5 soatda", "3 soatda", "4 soatda", "5 soatda"]
    },
    {
        'text': "<p>Kattalikni grammda ifodalang: 2 sr 20 kg 349 g[cite: 1].</p>",
        'hint': "<p>1 sentner necha kilogramm ekanligini yodga oling.</p>",
        'explanation': "<p>1 sr = 100 kg = 100 000 g, 1 kg = 1000 g[cite: 1]. 2 sr = 200 000 g, 20 kg = 20 000 g[cite: 1]. Jami: 200 000 + 20 000 + 349 = 220 349 g[cite: 1].</p>",
        'correct': "220 349 g",
        'choices': ["20 349 g", "220 349 g", "2 200 349 g", "202 349 g"]
    },
    {
        'text': "<p>Hadicha gulzorga kirib, birinchi kuni 56 ta tuvakdagi gullarga suv quydi[cite: 1]. Ikkinchi kuni esa birinchi kundan p dona ko'p gulga suv quydi[cite: 1]. Hadicha jami nechta gulga suv quygan? p = 34 bo'lganda hisoblang[cite: 1].</p>",
        'hint': "<p>Ikkinchi kundagi gullar sonini toping.</p>",
        'explanation': "<p>Ikkinchi kuni 56 + 34 = 90 ta gul sug'organ[cite: 1]. Jami sug'orilgan gullar: 56 + 90 = 146 ta[cite: 1].</p>",
        'correct': "146 ta",
        'choices': ["90 ta", "126 ta", "146 ta", "166 ta"]
    },
    {
        'text': "<p>To'g'ri to'rtburchak shaklidagi maktab hovlisining bo'yi 216 m, eni esa bo'yidan 45 m qisqa[cite: 1]. Maktab hovlisining perimetrini hisoblang[cite: 1].</p>",
        'hint': "<p>Perimetr formulasidan foydalaning.</p>",
        'explanation': "<p>Eni b = 216 - 45 = 171 m[cite: 1]. Perimetr P = 2(a + b) = 2 * (216 + 171) = 2 * 387 = 774 m[cite: 1].</p>",
        'correct': "774 m",
        'choices': ["387 m", "774 m", "864 m", "684 m"]
    },
    {
        'text': "<p>Tenglamani yeching: 542 - (y - 307) = 148[cite: 1].</p>",
        'hint': "<p>Yig'indidan sonni ayirish xossasini yoki noma'lum qavsni topish qoidasini qo'llang.</p>",
        'explanation': "<p>Noma'lum ayiriluvchini topamiz: y - 307 = 542 - 148 = 394[cite: 1]. Bundan y = 394 + 307 = 701[cite: 1].</p>",
        'correct': "701",
        'choices': ["601", "701", "394", "501"]
    },
    {
        'text': "<p>Uchta javonda 47 ta kitob bor[cite: 1]. Ikkinchi javonda birinchisidan 4 ta kam, uchinchi javondan esa 2 ta ko'p kitob bor[cite: 1]. Birinchi javonda nechta kitob bor?[cite: 1]</p>",
        'hint': "<p>Tenglashtirish usulidan foydalaning.</p>",
        'explanation': "<p>Agar 1-javonda x kitob bo'lsa, 2-sida x - 4[cite: 1]. 2-sida 3-sidan 2 ta ko'p bo'lsa, 3-sida x - 6 bo'ladi. Tenglama: x + x - 4 + x - 6 = 47 => 3x - 10 = 47 => 3x = 57 => x = 19[cite: 1].</p>",
        'correct': "19 ta",
        'choices': ["15 ta", "19 ta", "13 ta", "21 ta"]
    },
    {
        'text': "<p>Qafasda tustovuq va quyonlar boqilmoqda[cite: 1]. Ularning jami boshi 35 ta, jami oyoqlari esa 94 ta[cite: 1]. Qafasda nechta tustovuq va nechta quyon bor?[cite: 1]</p>",
        'hint': "<p>Barcha hayvonlarni 2 oyoqli deb faraz qilib ko'ring.</p>",
        'explanation': "<p>Faraz qilaylik barchasi qush (2 oyoq). U holda 35 * 2 = 70 oyoq bo'lardi[cite: 1]. Qolgan 94 - 70 = 24 oyoq quyonlarning qo'shimcha oyoqlari[cite: 1]. Demak, 24 / 2 = 12 ta quyon va 35 - 12 = 23 ta tustovuq[cite: 1].</p>",
        'correct': "23 ta tustovuq va 12 ta quyon",
        'choices': ["20 ta tustovuq va 15 ta quyon", "23 ta tustovuq va 12 ta quyon", "12 ta tustovuq va 23 ta quyon", "25 ta tustovuq va 10 ta quyon"]
    },
    {
        'text': "<p>Dono singlisi Nargizadan 7 yosh katta[cite: 1]. Uning yoshi otasining yoshidan 3 marta kichik[cite: 1]. Agar Nargiza 5 yoshda bo'lsa, Dononing otasi yoshini toping[cite: 1].</p>",
        'hint': "<p>Avval Dononing yoshini toping.</p>",
        'explanation': "<p>Dononing yoshi: 5 + 7 = 12 yosh[cite: 1]. Otasining yoshi: 12 * 3 = 36 yosh[cite: 1].</p>",
        'correct': "36 yosh",
        'choices': ["32 yosh", "36 yosh", "42 yosh", "28 yosh"]
    },
    {
        'text': "<p>Amallarni bajaring: (1269 + 1261) : 115[cite: 1].</p>",
        'hint': "<p>Avval qavs ichini hisoblang.</p>",
        'explanation': "<p>Qavs ichidagi yig'indi: 1269 + 1261 = 2530[cite: 1]. Bo'linma: 2530 : 115 = 22[cite: 1].</p>",
        'correct': "22",
        'choices': ["20", "22", "24", "26"]
    },
    {
        'text': "<p>Tenglamani yeching: 107 * x = 4815[cite: 1].</p>",
        'hint': "<p>Noma'lum ko'paytuvchini topish uchun bo'lishdan foydalaning.</p>",
        'explanation': "<p>Ko'paytmani ma'lum ko'paytuvchiga bo'lamiz: x = 4815 : 107 = 45[cite: 1].</p>",
        'correct': "45",
        'choices': ["35", "45", "55", "40"]
    },
    {
        'text': "<p>Qulay usul bilan hisoblang: 4 * 2 * 25 * 5 * 8 * 125[cite: 1].</p>",
        'hint': "<p>Guruhlash qonunidan foydalaning.</p>",
        'explanation': "<p>Ko'paytuvchilarni guruhlaymiz: (4 * 25) * (2 * 5) * (8 * 125) = 100 * 10 * 1000 = 1 000 000[cite: 1].</p>",
        'correct': "1 000 000",
        'choices': ["100 000", "1 000 000", "10 000 000", "10 000"]
    },
    {
        'text': "<p>Uzunligi 240 m bo'lgan simning 5/6 qismi qirqib olindi[cite: 1]. Necha metr sim qirqib olingan?[cite: 1]</p>",
        'hint': "<p>Kasrning qismini topish qoidasidan foydalaning.</p>",
        'explanation': "<p>240 m ni 6 ga bo'lib 5 ga ko'paytiramiz: 240 : 6 * 5 = 40 * 5 = 200 m[cite: 1].</p>",
        'correct': "200 m",
        'choices': ["180 m", "200 m", "220 m", "150 m"]
    },
    {
        'text': "<p>To'g'ri to'rtburchak shaklidagi yer maydonining o'lchamlari 750 m va 440 m[cite: 1]. Uning yuzini toping va gektarda ifodalang[cite: 1].</p>",
        'hint': "<p>1 gektar necha kvadrat metr ekanligini yodga oling.</p>",
        'explanation': "<p>Yuzasi S = 750 * 440 = 330 000 m<sup>2</sup>[cite: 1]. 1 gektar 10 000 m<sup>2</sup> bo'lgani uchun: 330 000 / 10 000 = 33 ga[cite: 1].</p>",
        'correct': "33 ga",
        'choices': ["33 ga", "330 ga", "3,3 ga", "3300 ga"]
    },
    {
        'text': "<p>Tenglamani yeching: 3x + 5x + 96 = 1568[cite: 1].</p>",
        'hint': "<p>Tenglamani ixchamlang va ishlashda davom eting.</p>",
        'explanation': "<p>Ifodani soddalashtiramiz: 8x + 96 = 1568[cite: 1]. 8x = 1568 - 96 = 1472[cite: 1]. x = 1472 : 8 = 184[cite: 1].</p>",
        'correct': "184",
        'choices': ["192", "184", "174", "168"]
    },
    {
        'text': "<p>Beton qorishmasi tayyorlash uchun 3 hissa qumga 2 hissa sement aralashtiriladi[cite: 1]. 60 kg beton qorishmasi tayyorlash uchun necha kilogramm qum va necha kilogramm sement olish kerak?[cite: 1]</p>",
        'hint': "<p>Umumiy hissalar sonini toping.</p>",
        'explanation': "<p>Jami hissalar soni: 3 + 2 = 5 hissa[cite: 1]. 1 hissa massasi: 60 : 5 = 12 kg[cite: 1]. Qum: 3 * 12 = 36 kg, Sement: 2 * 12 = 24 kg[cite: 1].</p>",
        'correct': "36 kg qum, 24 kg sement",
        'choices': ["30 kg qum, 30 kg sement", "36 kg qum, 24 kg sement", "40 kg qum, 20 kg sement", "42 kg qum, 18 kg sement"]
    },
    {
        'text': "<p>Ifodadagi amallarni bajarish tartibini aniqlang va uning qiymatini toping: 762 - 413 + 381 - 256[cite: 1].</p>",
        'hint': "<p>Qavssiz ifodalarda bir xil darajali amallar chapdan o'ngga bajariladi.</p>",
        'explanation': "<p>Ketma-ket bajaramiz: 762 - 413 = 349[cite: 1]. 349 + 381 = 730[cite: 1]. 730 - 256 = 474[cite: 1].</p>",
        'correct': "474",
        'choices': ["464", "474", "574", "384"]
    },
    {
        'text': "<p>Kater daryo oqimi bo'yicha suzmoqda[cite: 1]. Daryo oqimining tezligi 3 km/soat[cite: 1]. Agar katerning o'z (turg'un suvdagi) tezligi 18 km/soat bo'lsa, u 2 soatda qancha masofani bosib o'tadi?[cite: 1]</p>",
        'hint': "<p>Avval katerning oqim bo'yicha tezligini toping.</p>",
        'explanation': "<p>Oqim bo'yicha tezlik: 18 + 3 = 21 km/soat[cite: 1]. Masofa: 21 * 2 = 42 km[cite: 1].</p>",
        'correct': "42 km",
        'choices': ["36 km", "30 km", "42 km", "48 km"]
    },
    {
        'text': "<p>O'lchamlari 12 dm, 21 dm va 14 dm bo'lgan to'g'ri burchakli parallelepiped sirtining yuzini hisoblang[cite: 1].</p>",
        'hint': "<p>Sirt yuzasi formulasi: S = 2(ab + bc + ac).</p>",
        'explanation': "<p>S = 2 * (12*21 + 21*14 + 12*14) = 2 * (252 + 294 + 168) = 2 * 714 = 1428 dm<sup>2</sup>[cite: 1].</p>",
        'correct': "1428 dm2",
        'choices': ["1248 dm2", "1428 dm2", "1824 dm2", "714 dm2"]
    },
    {
        'text': "<p>O'nli kasrlarni ayiring: 4,5 - 1,451[cite: 1].</p>",
        'hint': "<p>Kamayuvchiga kerakli nollarni qo'shib ustun shaklida ayiring.</p>",
        'explanation': "<p>4,500 qilib tekislaymiz[cite: 1]. 4,500 - 1,451 = 3,049[cite: 1].</p>",
        'correct': "3,049",
        'choices': ["3,149", "3,049", "2,949", "3,059"]
    },
    {
        'text': "<p>Tenglamani yeching: 8,2x - 4,4x = 38,38[cite: 1].</p>",
        'hint': "<p>Noma'lum qatnashgan hadlarni soddalashtiring.</p>",
        'explanation': "<p>8,2x - 4,4x = 3,8x[cite: 1]. 3,8x = 38,38 tenglamasi hosil bo'ladi[cite: 1]. x = 38,38 : 3,8 = 10,1[cite: 1].</p>",
        'correct': "10,1",
        'choices': ["11,1", "10,1", "9,1", "1,01"]
    },
    {
        'text': "<p>Sayohatchi 4 soat 2,7 m/s tezlik bilan, so'ng esa 5 soat 1,8 m/s tezlik bilan yurdi[cite: 1]. Sayohatchining o'rtacha tezligi qancha?[cite: 1]</p>",
        'hint': "<p>Umumiy masofani umumiy vaqtga bo'ling.</p>",
        'explanation': "<p>Jami bosib o'tilgan yo'l: 4 * 2,7 + 5 * 1,8 = 10,8 + 9,0 = 19,8 km[cite: 1]. Jami vaqt: 4 + 5 = 9 soat[cite: 1]. O'rtacha tezlik: 19,8 : 9 = 2,2 m/s[cite: 1].</p>",
        'correct': "2,2 m/s",
        'choices': ["2,0 m/s", "2,2 m/s", "2,4 m/s", "2,5 m/s"]
    },
    {
        'text': "<p>Asakadagi avtomobil zavodi bir haftada 840 ta avtomobil ishlab chiqardi[cite: 1]. Ularning 20 foizi Spark avtomobilidir[cite: 1]. Zavod bir haftada nechta Spark avtomobili ishlab chiqargan?[cite: 1]</p>",
        'hint': "<p>Sonning foizini topish uchun foiz miqdorini 100 ga bo'lib ko'paytiring.</p>",
        'explanation': "<p>840 ning 1 foizi 8,4 ga teng[cite: 1]. 20 foizni topish uchun: 8,4 * 20 = 168 ta[cite: 1].</p>",
        'correct': "168 ta",
        'choices': ["148 ta", "168 ta", "180 ta", "158 ta"]
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
            title='Mathematics Basic: Natural Numbers and Basic Operations',
            master=master,
            defaults={
                'description': 'Practice basic operations with natural numbers.',
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