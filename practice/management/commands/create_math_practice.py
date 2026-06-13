from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
    {
        'text': '<p>Hisoblang:</p><p><strong>42 va 60 sonlarining eng katta umumiy boʻluvchisini (EKUB) toping.</strong></p>',
        'explanation': '<p><strong>6</strong> toʻgʻri javob. Sonlarni tub koʻpaytuvchilarga ajratamiz: 42 = 2 * 3 * 7 va 60 = 2 * 2 * 3 * 5. Umumiy tub koʻpaytuvchilarning eng kichik darajalari koʻpaytmasi EKUBni beradi: 2 * 3 = 6.</p>',
        'correct': '6',
        'choices': ['6', '12', '2', '420']
    },
    {
        'text': '<p>Hisoblang:</p><p><strong>12 va 15 sonlarining eng kichik umumiy karralisini (EKUK) toping.</strong></p>',
        'explanation': '<p><strong>60</strong> toʻgʻri javob. Sonlarni tub koʻpaytuvchilarga ajratamiz: 12 = 2^2 * 3 va 15 = 3 * 5. EKUKni topish uchun barcha tub koʻpaytuvchilarning eng katta darajalarini koʻpaytiramiz: 2^2 * 3 * 5 = 4 * 3 * 5 = 60.</p>',
        'correct': '60',
        'choices': ['30', '45', '60', '180']
    },
    {
        'text': '<p>Masalani yeching:</p><p><strong>72 sonining nechta natural boʻluvchisi bor?</strong></p>',
        'explanation': '<p><strong>12</strong> toʻgʻri javob. 72 sonini tub koʻpaytuvchilarga ajratamiz: 72 = 2^3 * 3^2. Natural boʻluvchilar sonini topish uchun darajaga 1 qoʻshib koʻpaytiramiz: (3 + 1) * (2 + 1) = 4 * 3 = 12.</p>',
        'correct': '12',
        'choices': ['8', '10', '12', '6']
    },
    {
        'text': '<p>Boʻlinish alomatlari:</p><p><strong>Quyidagi sonlardan qaysi biri ham 3 ga, ham 5 ga qoldiqsiz boʻlinadi?</strong></p>',
        'explanation': '<p><strong>135</strong> toʻgʻri javob. 5 ga boʻlinishi uchun oxirgi raqam 0 yoki 5 boʻlishi kerak. 3 ga boʻlinishi uchun raqamlar yigʻindisi 3 ga boʻlinishi kerak. 135 sonining raqamlar yigʻindisi 1+3+5=9 (3 ga boʻlinadi) va oxiri 5 bilan tugaydi.</p>',
        'correct': '135',
        'choices': ['125', '135', '230', '303']
    },
    {
        'text': '<p>Boʻlinish alomatlari:</p><p><strong>Berilgan sonlardan qaysi biri 4 ga qoldiqsiz boʻlinadi?</strong></p>',
        'explanation': '<p><strong>724</strong> toʻgʻri javob. Sonning oxirgi ikkita raqamidan tashkil topgan son 4 ga boʻlinsa, u son 4 ga qoldiqsiz boʻlinadi. 24 soni 4 ga boʻlingani uchun 724 ham 4 ga boʻlinadi.</p>',
        'correct': '724',
        'choices': ['514', '622', '724', '809']
    },
    {
        'text': '<p>Harakatga doir masala:</p><p><strong>Tezligi 15 km/sh boʻlgan velosipedchi 3 soatda qancha masofani (km) bosib oʻtadi?</strong></p>',
        'explanation': '<p><strong>45</strong> toʻgʻri javob. Masofani topish formulasi: S = v * t. Bu yerda tezlik (v) = 15 km/sh, vaqt (t) = 3 soat. Masofa: 15 * 3 = 45 km.</p>',
        'correct': '45',
        'choices': ['5', '18', '30', '45']
    },
    {
        'text': '<p>Harakatga doir masala:</p><p><strong>Avtomobil 240 km masofani 4 soatda bosib oʻtdi. Avtomobilning tezligini toping.</strong></p>',
        'explanation': '<p><strong>60</strong> toʻgʻri javob. Tezlikni topish formulasi: v = S / t. Masofa (S) = 240 km, vaqt (t) = 4 soat. Tezlik: 240 / 4 = 60 km/sh.</p>',
        'correct': '60',
        'choices': ['50', '60', '70', '80']
    },
    {
        'text': '<p>Oddiy kasrlar ustida amallar:</p><p><strong>Yigʻindini hisoblang: 2/7 + 3/7</strong></p>',
        'explanation': '<p><strong>5/7</strong> toʻgʻri javob. Maxrajlari bir xil boʻlgan kasrlarni qoʻshganda, ularning suratlari qoʻshiladi va maxraj oʻzi qoldiriladi: (2 + 3) / 7 = 5/7.</p>',
        'correct': '5/7',
        'choices': ['5/14', '5/7', '6/7', '1/7']
    },
    {
        'text': '<p>Oddiy kasrlar ustida amallar:</p><p><strong>Ayirmani hisoblang: 4/5 - 1/2</strong></p>',
        'explanation': '<p><strong>3/10</strong> toʻgʻri javob. Kasrlarga umumiy maxraj beramiz. Umumiy maxraj 10 boʻladi. Birinchi kasrni 2 ga, ikkinchisini 5 ga koʻpaytiramiz: 8/10 - 5/10 = 3/10.</p>',
        'correct': '3/10',
        'choices': ['3/5', '3/10', '5/10', '1/3']
    },
    {
        'text': '<p>Boʻlinish alomatlari:</p><p><strong>Quyidagi sonlardan qaysi biri 9 ga qoldiqsiz boʻlinadi?</strong></p>',
        'explanation': '<p><strong>459</strong> toʻgʻri javob. Sonning raqamlar yigʻindisi 9 ga boʻlinsa, u son 9 ga qoldiqsiz boʻlinadi. 459 sonida: 4 + 5 + 9 = 18. 18 soni 9 ga boʻlinadi.</p>',
        'correct': '459',
        'choices': ['123', '236', '459', '555']
    },
    {
        'text': '<p>Harakatga doir murakkab masala:</p><p><strong>Avtomobil 4 soatda maʼlum masofani oʻtishi kerak edi. U 3 soat davomida belgilangan 80 km/sh tezlikda yurdi. Qolgan masofani 30 minutda bosib oʻtishi uchun tezligini necha km/sh ga oshirishi kerak?</strong></p>',
        'explanation': '<p><strong>16</strong> toʻgʻri javob. Umumiy vaqt 4 soat boʻlishi kerak edi. Jami masofa: 80 * 4 = 320 km. Avtomobil 3 soatda 80 * 3 = 240 km yurdi. Qolgan masofa: 320 - 240 = 80 km. Uni 30 minutda (0.5 soatda) oʻtishi uchun kerakli tezlik: 80 / 0.5 = 160 km/sh. Tezlikni 160 - 80 = 80 km/sh ga oshirish kerak.</p>',
        'correct': '80',
        'choices': ['40', '60', '80', '100']
    },
    {
        'text': '<p>Mantiqiy-harakat masalasi:</p><p><strong>Poyezd reja boʻyicha 6 soatda 480 km yoʻl yurishi kerak edi. Yoʻlning yarmida u 1 soat toʻxtab qoldi. Poyezd manzilga oʻz vaqtida yetib borishi uchun qolgan yoʻlda tezligini qanchaga oshirishi kerak?</strong></p>',
        'explanation': '<p><strong>20</strong> toʻgʻri javob. Asl tezlik 480 / 6 = 80 km/sh. Yarim yoʻl 240 km, unga 3 soat ketadi. 1 soat toʻxtab qolganidan keyin qolgan 240 km masofa uchun 3 - 1 = 2 soat vaqt qoladi. Demak, yangi tezlik 240 / 2 = 120 km/sh boʻlishi kerak. Tezlikni oshirish miqdori: 120 - 80 = 40 km/sh.</p>',
        'correct': '40',
        'choices': ['20', '30', '40', '50']
    },
    {
        'text': '<p>Hisoblang:</p><p><strong>24, 36 va 48 sonlarining eng katta umumiy boʻluvchisini (EKUB) toping.</strong></p>',
        'explanation': '<p><strong>12</strong> toʻgʻri javob. 24 = 2^3 * 3, 36 = 2^2 * 3^2, 48 = 2^4 * 3. Umumiy koʻpaytuvchilarning kichik darajalari: 2^2 * 3 = 4 * 3 = 12.</p>',
        'correct': '12',
        'choices': ['6', '12', '24', '144']
    },
    {
        'text': '<p>Hisoblang:</p><p><strong>8, 12 va 18 sonlarining eng kichik umumiy karralisini (EKUK) toping.</strong></p>',
        'explanation': '<p><strong>72</strong> toʻgʻri javob. 8 = 2^3, 12 = 2^2 * 3, 18 = 2 * 3^2. EKUK uchun eng katta darajalar olinadi: 2^3 * 3^2 = 8 * 9 = 72.</p>',
        'correct': '72',
        'choices': ['36', '48', '72', '144']
    },
    {
        'text': '<p>Masalani yeching:</p><p><strong>120 sonining nechta tub boʻluvchisi bor?</strong></p>',
        'explanation': '<p><strong>3</strong> toʻgʻri javob. 120 sonini tub koʻpaytuvchilarga ajratamiz: 120 = 2^3 * 3 * 5. Tub boʻluvchilari faqat tub sonlarning oʻzi, yaʼni 2, 3 va 5. Jami 3 ta.</p>',
        'correct': '3',
        'choices': ['3', '5', '16', '8']
    },
    {
        'text': '<p>Masalani yeching:</p><p><strong>100 sonining barcha natural boʻluvchilari yigʻindisini toping.</strong></p>',
        'explanation': '<p><strong>217</strong> toʻgʻri javob. 100 = 2^2 * 5^2. Boʻluvchilar yigʻindisi formulasi: (2^0+2^1+2^2)*(5^0+5^1+5^2) = (1+2+4)*(1+5+25) = 7 * 31 = 217.</p>',
        'correct': '217',
        'choices': ['117', '200', '217', '242']
    },
    {
        'text': '<p>Boʻlinish alomatlari:</p><p><strong>34X2 toʻrt xonali son X ning qanday qiymatida 6 ga qoldiqsiz boʻlinadi?</strong></p>',
        'explanation': '<p><strong>3</strong> toʻgʻri javob. Son 6 ga boʻlinishi uchun u ham 2 ga, ham 3 ga boʻlinishi shart. Son juft (oxiri 2), demak 2 ga boʻlinadi. 3 ga boʻlinishi uchun raqamlar yigʻindisi (3+4+X+2 = 9+X) 3 ga boʻlinishi kerak. Berilgan variantlar orasidan faqat 3 (9+3=12) bu shartni qanoatlantiradi.</p>',
        'correct': '3',
        'choices': ['1', '2', '3', '5']
    },
    {
        'text': '<p>Boʻlinish alomatlari:</p><p><strong>Quyidagi sonlardan qaysi biri 8 ga qoldiqsiz boʻlinadi?</strong></p>',
        'explanation': '<p><strong>3128</strong> toʻgʻri javob. Agar sonning oxirgi uchta raqamidan tashkil topgan son 8 ga boʻlinsa, u son 8 ga boʻlinadi. 128 / 8 = 16 (qoldiqsiz), demak 3128 soni 8 ga boʻlinadi.</p>',
        'correct': '3128',
        'choices': ['2118', '3128', '4204', '5062']
    },
    {
        'text': '<p>Boʻlinish alomatlari:</p><p><strong>5A74 toʻrt xonali son A ning qanday qiymatlarida 9 ga qoldiqsiz boʻlinadi?</strong></p>',
        'explanation': '<p><strong>2</strong> toʻgʻri javob. 9 ga boʻlinish qoidasiga koʻra raqamlar yigʻindisi 9 ga boʻlinishi kerak: 5 + A + 7 + 4 = 16 + A. 16 ga faqat 2 qoʻshilsa 18 boʻladi va 9 ga boʻlinadi.</p>',
        'correct': '2',
        'choices': ['1', '2', '5', '7']
    },
    {
        'text': '<p>Boʻlinish alomatlari:</p><p><strong>Quyidagi sonlardan qaysi biri 12 ga qoldiqsiz boʻlinadi?</strong></p>',
        'explanation': '<p><strong>432</strong> toʻgʻri javob. 12 ga boʻlinadigan son ham 3 ga, ham 4 ga boʻlinishi kerak. 432 sonining oxirgi ikki raqami (32) 4 ga boʻlinadi. Raqamlar yigʻindisi (4+3+2=9) 3 ga boʻlinadi.</p>',
        'correct': '432',
        'choices': ['412', '422', '432', '442']
    },
    {
        'text': '<p>Harakatga doir masala:</p><p><strong>Ikki shahar oʻrtasidagi masofa 360 km. Avtomobil bu masofani 90 km/sh tezlik bilan bosib oʻtdi va orqaga 60 km/sh tezlik bilan qaytdi. Avtomobil butun yoʻlga necha soat vaqt sarflagan?</strong></p>',
        'explanation': '<p><strong>10</strong> toʻgʻri javob. Borishga ketgan vaqt: 360 / 90 = 4 soat. Qaytishga ketgan vaqt: 360 / 60 = 6 soat. Jami vaqt: 4 + 6 = 10 soat.</p>',
        'correct': '10',
        'choices': ['8', '9', '10', '12']
    },
    {
        'text': '<p>Harakatga doir masala:</p><p><strong>Tezligi 70 km/sh boʻlgan yuk mashinasi yoʻlga chiqdi. 2 soatdan keyin uning ortidan tezligi 90 km/sh boʻlgan yengil avtomobil yoʻlga chiqdi. Yengil avtomobil yuk mashinasini necha soatda quvib yetadi?</strong></p>',
        'explanation': '7 toʻgʻri javob. Yuk mashinasi 2 soatda 70 * 2 = 140 km oldinga ketadi. Yaqinlashish tezligi: 90 - 70 = 20 km/sh. Quvib yetish vaqti: 140 / 20 = 7 soat.','correct': '7','choices': ['5', '6', '7', '8']},
        {'text': 'Kasrlar ustida amallar:Amalni bajaring: 5/6 - 1/4 + 1/3','explanation': '11/12 toʻgʻri javob. Umumiy maxraj topamiz, u 12 ga teng. Kasrlarni kengaytiramiz: (10/12) - (3/12) + (4/12) = 11/12.','correct': '11/12','choices': ['7/12', '9/12', '11/12', '5/6']},{'text': 'Kasrlar ustida amallar:Koʻpaytirishni bajaring: (3/4) * (8/9)','explanation': '2/3 toʻgʻri javob. Suratlari va maxrajlarini oʻzaro qisqartiramiz. 3 va 9 qisqarib maxrajda 3 qoladi, 4 va 8 qisqarib suratda 2 qoladi. Natija: 2/3.','correct': '2/3','choices': ['5/12', '2/3', '6/7', '24/36']},{'text': 'Kasrlar ustida amallar:Boʻlishni bajaring: (5/8) / (15/16)','explanation': '2/3 toʻgʻri javob. Birinchi kasrni ikkinchi kasrning teskarisiga koʻpaytiramiz: (5/8) * (16/15). 5 bilan 15 qisqarib 3 qoladi, 8 bilan 16 qisqarib 2 qoladi. Natija: 2/3.','correct': '2/3','choices': ['1/2', '2/3', '3/4', '5/6']},{'text': 'Mantiqiy masala:Sinfdagi oʻquvchilar soni 3 ga ham, 4 ga ham qoldiqsiz boʻlinadi. Agar oʻquvchilar soni 20 va 30 ning orasida boʻlsa, sinfda nechta oʻquvchi bor?','explanation': '24 toʻgʻri javob. Son 3 va 4 ga boʻlingani uchun ularning EKUKiga, yaʼni 12 ga ham boʻlinishi kerak. 20 va 30 orasidagi 12 ga karrali yagona son bu 24 dir.','correct': '24','choices': ['21', '24', '28', '36']},{'text': 'Kasr masalalari:Kitobning 3/5 qismi oʻqildi. Agar oʻqilmagan 24 sahifa qolgan boʻlsa, kitob jami necha sahifadan iborat?','explanation': '60 toʻgʻri javob. Kitobning qolgan qismi: 1 - 3/5 = 2/5 qism. Demak, kitobning 2/5 qismi 24 sahifaga teng. Jami sahifalar soni: 24 / 2 * 5 = 60.','correct': '60','choices': ['40', '50', '60', '80']},{'text': 'Mantiqiy-harakat masalasi:Chiroq har 4 minutda, ikkinchi chiroq esa har 6 minutda yonib-ochadi. Ular soat 12:00 da birga yongan boʻlsa, keyingi safar soat nechada yana birga yonadi?','explanation': '12:12 toʻgʻri javob. Ular qayta birga yonishi uchun ketadigan vaqt 4 va 6 sonlarining EKUKiga teng boʻladi. EKUK(4, 6) = 12 minut. Demak, 12:00 dan keyin 12:12 da yana birga yonadi.','correct': '12:12','choices': ['12:06', '12:10', '12:12', '12:24']},{'text': 'Kasrlar ustida amallar:1 sonidan 3/8 va 1/4 ning yigʻindisini ayiring.','explanation': '3/8 toʻgʻri javob. Avval yigʻindini hisoblaymiz: 3/8 + 1/4 = 3/8 + 2/8 = 5/8. Keyin 1 dan ayiramiz: 1 - 5/8 = 3/8.','correct': '3/8','choices': ['1/8', '3/8', '5/8', '7/8']},{'text': 'Harakatga doir masala:Velosipedchi 2 soat davomida 12 km/sh tezlikda yurdi. Keyingi 1 soatda esa tezligini 15 km/sh ga oshirdi (yangi tezligi 15 km/sh boʻldi). U jami necha kilometr masofani bosib oʻtdi?','explanation': '39 toʻgʻri javob. Dastlabki 2 soatda: 12 * 2 = 24 km. Keyingi 1 soatda: 15 * 1 = 15 km. Jami masofa: 24 + 15 = 39 km.','correct': '39','choices': ['27', '36', '39', '42']},{'text': 'Boʻlinish alomatlari:Quyidagi sonlardan qaysi biri 10 ga boʻlinganda 3 qoldiq qoladi?','explanation': '253 toʻgʻri javob. Son 10 ga boʻlinganda oxirgi raqami qoldiq boʻlib qoladi. 253 sonining oxirgi raqami 3 boʻlgani uchun qoldiq ham 3 boʻladi.','correct': '253','choices': ['230', '253', '300', '350']},{'text': 'Kasr masalalari:Savatdagi olmalarning 1/3 qismi qizil, 2/5 qismi koʻk va qolganlari yashil. Yashil olmalar savatdagi barcha olmalarning qaysi qismini tashkil qiladi?','explanation': '4/15 toʻgʻri javob. Qizil va koʻk olmalarning qismini qoʻshamiz: 1/3 + 2/5 = 5/15 + 6/15 = 11/15. Yashil olmalarni topish uchun butundan (1 dan) ayiramiz: 1 - 11/15 = 4/15.','correct': '4/15','choices': ['3/15', '4/15', '7/15', '11/15']},{'text': 'Masalani yeching:A va B sonlarining EKUBi 6 ga, EKUKi esa 72 ga teng. Agar A soni 18 ga teng boʻlsa, B sonini toping.','explanation': '24 toʻgʻri javob. Matematik qoidaga koʻra: A * B = EKUB(A, B) * EKUK(A, B). Shundan kelib chiqib, 18 * B = 6 * 72. 18 * B = 432. B = 432 / 18 = 24.','correct': '24','choices': ['12', '24', '36', '48']},{'text': 'Harakatga doir masala:Katerning turgʻun suvdagi tezligi 20 km/sh, daryo oqimining tezligi esa 3 km/sh. Kater oqimga qarshi 2 soatda qancha masofani bosib oʻtadi?','explanation': '34 toʻgʻri javob. Oqimga qarshi tezlik: 20 - 3 = 17 km/sh. 2 soatda bosib oʻtilgan masofa: 17 * 2 = 34 km.','correct': '34','choices': ['34', '40', '43', '46']},{'text': 'Mantiqiy-kasr masalasi:Idishning 3/4 qismi suv bilan toʻla. Idishga yana 5 litr suv quyilsa, u butunlay toʻladi. Idish jami necha litr suv sigʻdiradi?','explanation': '20 toʻgʻri javob. Idishning boʻsh qismi: 1 - 3/4 = 1/4 qism. Demak, 1/4 qism 5 litrga teng. Idishning umumiy hajmi: 5 * 4 = 20 litr.','correct': '20','choices': ['15', '20', '25', '30']}]



class Command(BaseCommand):
    help = 'Create a Korean grammar particle practice test'

    def add_arguments(self, parser):
        parser.add_argument('--master', required=True, help='Username of the master to assign this practice to')

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
            name='math',  # --- IGNORE ---
            defaults={'description': 'Math practice problems'},
        )

        practice, created = Practice.objects.get_or_create(
            title='Takrorlash 2.',  # --- IGNORE ---
            master=master,
            defaults={
                'description': 'Let\'s practice some math problems to improve your skills.',  # --- IGNORE ---
                'subject': subject,
                'level': 'medium',
                'is_free': True,
                'is_published': True,
                'is_available_for_all': True,
                'pass_score': 70,
                'max_attempts': 0,
                'show_answers_after': True,
            },
        )

        if not created:
            self.stdout.write(self.style.WARNING(
                f"Practice '{practice.title}' already exists (id={practice.pk}). Skipping."
            ))
            return

        for i, q in enumerate(QUESTIONS, start=1):
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
            f"Created practice '{practice.title}' with {len(QUESTIONS)} questions (id={practice.pk})."
        ))
