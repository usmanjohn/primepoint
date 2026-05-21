from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [{'text': "72 va 96 sonlarining eng katta umumiy bo'luvchisini (EKUB) toping.",'explanation': "Sonlarni tub ko'paytuvchilarga ajratamiz: 72 = 2³ * 3², 96 = 2⁵ * 3. EKUBni topish uchun umumiy tub ko'paytuvchilarning kichik darajalari ko'paytiriladi: EKUB(72, 96) = 2³ * 3 = 8 * 3 = 24.",'correct': "24",'choices': ["12", "24", "48", "124"]},{'text': "18 va 24 sonlarining eng kichik umumiy karralisini (EKUK) toping.",'explanation': "Sonlarni tub ko'paytuvchilarga ajratamiz: 18 = 2 * 3², 24 = 2³ * 3. EKUKni topish uchun barcha tub ko'paytuvchilarning eng katta darajalari ko'paytiriladi: EKUK(18, 24) = 2³ * 3² = 8 * 9 = 72.",'correct': "72",'choices': ["48", "54", "72", "96"]},{'text': "Sardor bo'yi 45 sm va eni 30 sm bo'lgan to'g'ri to'rtburchak shaklidagi kartondan eng katta o'lchamli teng kvadratlar qirqib olmoqchi. Kvadratning tomoni necha sm bo'ladi?",'explanation': "Kartonni isrofsiz teng kvadratlarga bo'lish uchun kvadrat tomoni 45 va 30 sonlarining EKUBiga teng bo'lishi kerak. EKUB(45, 30) = 15 sm.",'correct': "15 sm",'choices': ["5 sm", "10 sm", "15 sm", "30 sm"]},{'text': "Ikki avtobus birinchi bekatdan bir vaqtda yo'lga chiqdi. Birinchi avtobus har 20 daqiqada, ikkinchisi esa har 25 daqiqada shu bekatga qaytib keladi. Ular necha daqiqadan keyin yana shu bekatda uchrashishadi?",'explanation': "Avtobuslarning qayta uchrashish vaqti 20 va 25 sonlarining EKUKiga teng bo'ladi. EKUK(20, 25) = 100 daqiqa.",'correct': "100 daqiqa",'choices': ["50 daqiqa", "100 daqiqa", "120 daqiqa", "200 daqiqa"]},{'text': "O'qituvchi maktab tadbiri uchun 48 ta olma va 72 ta konfetni o'quvchilarga teng taqsimlab, bir xil sovg'alar tayyorladi. Eng ko'pi bilan nechta bir xil sovg'a tayyorlash mumkin?",'explanation': "Meva va shirinliklarni teng bo'lish va eng ko'p sovg'a tayyorlash uchun 48 va 72 sonlarining EKUBini topamiz. EKUB(48, 72) = 24.",'correct': "24",'choices': ["12", "16", "24", "48"]},{'text': "Durdona gullarni har 4 tadan yoki har 6 tadan qilib dasta ko'targanda har safar 1 ta gul ortib qoladi. Durdonada eng kamida nechta gul bor?",'explanation': "Gullar soni 4 va 6 ga bo'linganda 1 qoldiq berishi kerak. Avval 4 va 6 ning EKUKini topamiz: EKUK(4, 6) = 12. Keyin qoldiqni qo'shamiz: 12 + 1 = 13 ta gul.",'correct': "13 ta",'choices': ["11 ta", "13 ta", "25 ta", "37 ta"]},{'text': "Uzunligi 120 metr va 180 metr bo'lgan ikki arqon teng bo'laklarga bo'linishi kerak. Bo'laklarning uzunligi eng ko'pi bilan necha metr bo'lishi mumkin?",'explanation': "Arqonlarni teng va eng uzun bo'laklarga ajratish uchun 120 va 180 ning EKUBini topamiz. EKUB(120, 180) = 60 metr.",'correct': "60 m",'choices': ["20 m", "30 m", "60 m", "90 m"]},{'text': "Stol ustidagi daftarlarni 8 tadan ham, 12 tadan ham guruhlash mumkin. Stol ustida eng kamida nechta daftar bor?",'explanation': "Daftarlar soni ham 8 ga, ham 12 ga qoldiqsiz bo'linishi kerak. Demak, biz 8 va 12 sonlarining EKUKini topamiz: EKUK(8, 12) = 24.",'correct': "24 ta",'choices': ["16 ta", "24 ta", "48 ta", "96 ta"]},{'text': "36 va 60 sonlarining eng katta umumiy bo'luvchisini toping.",'explanation': "36 = 2² * 3², 60 = 2² * 3 * 5. Umumiy ko'paytuvchilarning kichik darajalari ko'paytmasi: EKUB(36, 60) = 2² * 3 = 12.",'correct': "12",'choices': ["6", "12", "18", "30"]},{'text': "15 va 20 sonlarining eng kichik umumiy karralisini toping.",'explanation': "15 = 3 * 5, 20 = 2² * 5. EKUK(15, 20) = 2² * 3 * 5 = 4 * 3 * 5 = 60.",'correct': "60",'choices': ["30", "45", "60", "120"]},{'text': "Do'konga bo'yi 16 sm, eni 12 sm bo'lgan to'rtburchak kafel kirdi. Usta ulardan foydalanib eng kichik kvadrat shaklidagi maydonni qoplamoqchi. Kvadratning tomoni necha sm bo'ladi?",'explanation': "Kafellar yordamida kvadrat hosil qilish uchun kvadrat tomoni 16 va 12 sonlarining eng kichik umumiy karralisi (EKUK) bo'lishi kerak. EKUK(16, 12) = 48 sm.",'correct': "48 sm",'choices': ["24 sm", "32 sm", "48 sm", "64 sm"]},{'text': "Sinfdagi o'quvchilarga 5 tadan yoki 7 tadan qalam tarqatilsa, hech qanday qalam ortib qolmaydi. Bu sinfda eng kamida nechta o'quvchi bor?",'explanation': "O'quvchilar soni 5 va 7 ga qoldiqsiz bo'linishi kerak. 5 va 7 o'zaro tub sonlar bo'lgani uchun ularning EKUKi ko'paytmasiga teng: 5 * 7 = 35.",'correct': "35 ta",'choices': ["15 ta", "25 ta", "35 ta", "70 ta"]},{'text': "Ikkita sim berilgan: birining uzunligi 56 metr, ikkinchisiniki 84 metr. Ularni o'lchovli teng bo'laklarga bo'lish uchun eng ko'p necha metrdan qirqish kerak?",'explanation': "Simlarni eng uzun va teng bo'laklarga ajratish uchun 56 va 84 sonlarining EKUBini topamiz. EKUB(56, 84) = 28 metr.",'correct': "28 m",'choices': ["14 m", "28 m", "42 m", "56 m"]},{'text': "Portda uchta kema uchrashdi. Birinchi kema har 12 kunda, ikkinchisi har 18 kunda, uchinchisi esa har 24 kunda shu portga keladi. Ular yana necha kundan keyin portda uchrashishadi?",'explanation': "Kemalarning qayta uchrashish muddati 12, 18 va 24 sonlarining EKUKiga teng. EKUK(12, 18, 24) = 72 kundan keyin.",'correct': "72 kundan keyin",'choices': ["36 kundan keyin", "48 kundan keyin", "72 kundan keyin", "144 kundan keyin"]},{'text': "Omborda 90 kg guruch va 135 kg grechka bor. Ularni og'irligi teng bo'lgan qoplarga aralashtirmasdan qadoqlash kerak. Qoplarning eng katta sig'imi necha kg bo'lishi mumkin?",'explanation': "Guruch va grechkani teng sig'imli qoplarga isrofsiz joylash uchun 90 va 135 ning EKUBini topamiz. EKUB(90, 135) = 45 kg.",'correct': "45 kg",'choices': ["15 kg", "30 kg", "45 kg", "90 kg"]},{'text': "42 va 70 sonlarining eng katta umumiy bo'luvchisini toping.",'explanation': "42 = 2 * 3 * 7, 70 = 2 * 5 * 7. Umumiy tub ko'paytuvchilar ko'paytmasi: EKUB(42, 70) = 2 * 7 = 14.",'correct': "14",'choices': ["7", "14", "21", "35"]},{'text': "25 va 35 sonlarining eng kichik umumiy karralisini toping.",'explanation': "25 = 5², 35 = 5 * 7. EKUK(25, 35) = 5² * 7 = 25 * 7 = 175.",'correct': "175",'choices': ["70", "125", "175", "250"]},{'text': "Gulasal bog'dan tergan gullarini 9 tadan yoki 15 tadan qilib dasta qila oladi. Gulasal eng kamida nechta gul tergan?",'explanation': "Gullarning eng kam miqdori 9 va 15 sonlarining eng kichik umumiy karralisiga (EKUK) teng bo'ladi. EKUK(9, 15) = 45.",'correct': "45 ta",'choices': ["30 ta", "45 ta", "60 ta", "90 ta"]},{'text': "Sinf rahbari 54 ta daftar va 81 ta ruchkani o'quvchilarga teng taqsimladi. Sinfda eng ko'pi bilan nechta o'quvchi bo'lishi mumkin?",'explanation': "Daftar va ruchkalar sonini teng bo'lish mumkin bo'lgan maksimal odamlar soni 54 va 81 sonlarining EKUBiga teng. EKUB(54, 81) = 27.",'correct': "27",'choices': ["9", "18", "27", "54"]},{'text': "Zavoddagi ikkita signal moslamasidan biri har 45 soniyada, ikkinchisi har 60 soniyada ovoz chiqaradi. Ular bir vaqtda ovoz chiqargandan so'ng, yana necha soniyadan keyin birga ovoz beradi?",'explanation': "Ushbu moslamalarning birga ovoz berish vaqti 45 va 60 sonlarining EKUKi yordamida topiladi. EKUK(45, 60) = 180 soniya.",'correct': "180 soniya",'choices': ["90 soniya", "120 soniya", "180 soniya", "240 soniya"]},{'text': "O'g'il bola qadamining uzunligi 60 sm, otasining qadami esa 80 sm. Ular bir joydan boshlab qadam tashlashni boshlashsa, qanday eng qisqa masofada ularning qadamlari yana mos keladi?",'explanation': "Qadamlarning qayta mos kelishi uchun masofa 60 va 80 sonlarining EKUKiga teng bo'lishi kerak. EKUK(60, 80) = 240 sm (yoki 2,4 metr).",'correct': "240 sm",'choices': ["120 sm", "160 sm", "240 sm", "480 sm"]},{'text': "80 va 120 sonlarining eng katta umumiy bo'luvchisini toping.",'explanation': "80 = 2⁴ * 5, 120 = 2³ * 3 * 5. EKUB(80, 120) = 2³ * 5 = 8 * 5 = 40.",'correct': "40",'choices': ["20", "30", "40", "60"]},{'text': "32 va 48 sonlarining eng kichik umumiy karralisini toping.",'explanation': "32 = 2⁵, 48 = 2⁴ * 3. EKUK(32, 48) = 2⁵ * 3 = 32 * 3 = 96.",'correct': "96",'choices': ["64", "80", "96", "144"]},{'text': "Tikuvchilik sexida 64 metr ko'k va 96 metr qizil mato bor. Ulardan bir xil o'lchamdagi eng uzun bo'laklar kesib olinishi kerak. Har bir bo'lak uzunligi necha metr bo'ladi?",'explanation': "Matolarni teng va eng uzun qismlarga bo'lish uchun 64 va 96 ning EKUBini hisoblaymiz. EKUB(64, 96) = 32 metr.",'correct': "32 m",'choices': ["16 m", "24 m", "32 m", "48 m"]},{'text': "Bir qush har 6 daqiqada, ikkinchisi har 9 daqiqada daraxtga kelib qo'nadi. Agar ular hozir birga qo'ngan bo'lsa, eng kamida necha daqiqadan keyin yana daraxtda uchrashishadi?",'explanation': "Qushlarning uchrashish vaqti 6 va 9 sonlarining EKUKi orqali aniqlanadi. EKUK(6, 9) = 18 daqiqa.", 'correct': "18 daqiqa",'choices': ["12 daqiqa", "15 daqiqa", "18 daqiqa", "36 daqiqa"]}]



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
            title='EKUB, EKUK savollari',
            master=master,
            defaults={
                'description': 'EKUB va EKUK testlar jamlanmasi.',
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