from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
    {
        "text": "<p>Eng kichik natural sonni toping.</p>",
        "hint": "<p>Sanoq sonlarning eng birinchisini eslang.</p>",
        "explanation": "<p><strong>1</strong>: Natural sonlar qatorida 1 eng kichik natural sondir. 0 natural son emas.</p>",
        "correct": "1",
        "choices": ["0", "1", "10", "Eng kichik natural son yo'q"]
    },
    {
        "text": "<p>Natural sonlarni yozishda nechta raqam ishlatiladi?</p>",
        "hint": "<p>0 dan 9 gacha bo'lgan raqamlarni sanab chiqing.</p>",
        "explanation": "<p><strong>10 ta</strong>: Har qanday natural sonni o'nta (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) raqamlar bilan yozish mumkin.</p>",
        "correct": "10 ta",
        "choices": ["9 ta", "10 ta", "Cheksiz ko'p", "100 ta"]
    },
    {
        "text": "<p><strong>0</strong> raqami natural son hisoblanadimi?</p>",
        "hint": "<p>Natural sonlar narsalarni sanashda ishlatilishini yodda tuting.</p>",
        "explanation": "<p><strong>Yo'q</strong>: Narsalarni sanashda ishlatiladigan sonlar natural sonlardir. 0 natural son emas.</p>",
        "correct": "Yo'q",
        "choices": ["Ha", "Yo'q", "Faqat manfiy bo'lmaganda", "Ba'zan"]
    },
    {
        "text": "<p>Ikki va undan ortiq xonali sonlar qanday ataladi?</p>",
        "hint": "<p>Raqamlar soniga qarab nomlanishini eslang.</p>",
        "explanation": "<p><strong>Ko'p xonali sonlar</strong>: Yozuvida ikkita va undan ko'p raqam qatnashgan sonlar ko'p xonali sonlar deyiladi.</p>",
        "correct": "Ko'p xonali sonlar",
        "choices": ["Katta sonlar", "Ko'p xonali sonlar", "Juft sonlar", "Murakkab sonlar"]
    },
    {
        "text": "<p>99 999 sonidan keyin keluvchi natural sonni aniqlang.</p>",
        "hint": "<p>Berilgan songa 1 ni qo'shing.</p>",
        "explanation": "<p><strong>100 000</strong>: Har qanday natural songa 1 ni qo'shsak, undan keyin keluvchi navbatdagi son hosil bo'ladi.</p>",
        "correct": "100 000",
        "choices": ["10 000", "99 998", "1 000 000", "100 000"]
    },
    {
        "text": "<p>A va B nuqtalarni nechta kesma bilan tutashtirish mumkin?</p>",
        "hint": "<p>Tekislikda ikki nuqta orasidagi eng qisqa masofani ko'z oldingizga keltiring.</p>",
        "explanation": "<p><strong>Bitta</strong>: Istalgan ikki nuqtani faqat bitta kesma bilan tutashtirish mumkin.</p>",
        "correct": "Bitta",
        "choices": ["Bitta", "Ikkita", "Uchta", "Istalgancha"]
    },
    {
        "text": "<p>Kesmaning uzunligini o'lchash deganda nima tushuniladi?</p>",
        "hint": "<p>Chizg'ich yordamida o'lchash jarayonini eslang.</p>",
        "explanation": "<p><strong>Unga birlik kesma necha marta joylashishini aniqlash</strong>: Kesmaning uzunligini o'lchash - unga birlik kesma necha marta joylashishini aniqlashdan iborat.</p>",
        "correct": "Unga birlik kesma necha marta joylashishini aniqlash",
        "choices": ["Kesmani chizish", "Unga birlik kesma necha marta joylashishini aniqlash", "Kesmani teng ikkiga bo'lish", "Nuqtalarni sanash"]
    },
    {
        "text": "<p>1 detsimetr (dm) necha santimetrga (sm) teng?</p>",
        "hint": "<p>Uzunlik o'lchov birliklari jadvallarini eslang.</p>",
        "explanation": "<p><strong>10 sm</strong>: 1 dm = 10 sm ga teng.</p>",
        "correct": "10 sm",
        "choices": ["100 sm", "10 sm", "1000 sm", "1 sm"]
    },
    {
        "text": "<p>1 kilometr (km) necha metrga (m) teng?</p>",
        "hint": "<p>Kilo so'zi qanday ma'noni anglatishini yodga oling.</p>",
        "explanation": "<p><strong>1000 m</strong>: 1 km = 1000 m ga teng.</p>",
        "correct": "1000 m",
        "choices": ["100 m", "10 m", "1000 m", "10 000 m"]
    },
    {
        "text": "<p>Uchburchak tomonlari uzunliklari yig'indisi nima deb ataladi?</p>",
        "hint": "<p>Shaklning barcha tashqi chegaralari yig'indisini anglatuvchi atamani toping.</p>",
        "explanation": "<p><strong>Perimetr</strong>: Ko'pburchak (jumladan uchburchak) tomonlari uzunliklari yig'indisi uning perimetri deb ataladi.</p>",
        "correct": "Perimetr",
        "choices": ["Yuz", "Hajm", "Perimetr", "Diametr"]
    },
    {
        "text": "<p>Ikki nuqtadan nechta to'g'ri chiziq o'tkazish mumkin?</p>",
        "hint": "<p>Chizg'ichni ikki nuqtaga qo'yib ko'ring.</p>",
        "explanation": "<p><strong>Bitta</strong>: Har qanday ikki nuqtadan faqat bitta to'g'ri chiziq o'tkazish mumkin.</p>",
        "correct": "Bitta",
        "choices": ["Bitta", "Ikkita", "Uchta", "Cheksiz ko'p"]
    },
    {
        "text": "<p>To'g'ri chiziqning oxiri bormi?</p>",
        "hint": "<p>To'g'ri chiziq va kesma o'rtasidagi farqni eslang.</p>",
        "explanation": "<p><strong>Yo'q, u cheksiz</strong>: To'g'ri chiziqning cheki (oxiri) yo'q. U har ikki uchi tomonga cheksiz davom etadi.</p>",
        "correct": "Yo'q, u cheksiz",
        "choices": ["Ha, ikki tomondan", "Yo'q, u cheksiz", "Faqat bir tomondan cheklangan", "Nuqtada cheklanadi"]
    },
    {
        "text": "<p>To'g'ri chiziqda olingan nuqta uni qanday shakllarga ajratadi?</p>",
        "hint": "<p>Boshi bor, lekin oxiri yo'q bo'lgan shaklni eslang.</p>",
        "explanation": "<p><strong>Nurlarga</strong>: To'g'ri chiziqda olingan nuqta uni ikki bo'lakka ajratadi va ularning har biri nur deb ataladi.</p>",
        "correct": "Nurlarga",
        "choices": ["Kesmalarga", "Nurlarga", "Yoylarga", "Uchburchaklarga"]
    },
    {
        "text": "<p>Ikki to'g'ri chiziq umumiy nuqtaga ega bo'lsa, ular...</p>",
        "hint": "<p>To'g'ri chiziqlar ustma-ust tushmasa, faqat qanday holat bo'lishi mumkin?</p>",
        "explanation": "<p><strong>Kesishadi</strong>: Agar ikki to'g'ri chiziq bitta umumiy nuqtaga ega bo'lsa, ular bu nuqtada kesishadi deyiladi.</p>",
        "correct": "Kesishadi",
        "choices": ["Paralel bo'ladi", "Kesishadi", "Birlashadi", "Nur hosil qiladi"]
    },
    {
        "text": "<p>Sonlar nurida qaysi son chaproqda joylashgan bo'lsa, u qanday bo'ladi?</p>",
        "hint": "<p>Nolga yaqinroq bo'lgan sonning qiymati qanday bo'ladi?</p>",
        "explanation": "<p><strong>Kichik</strong>: Ikki natural sondan qaysi biri sonlar nurida chapda joylashgan bo'lsa, o'sha son kichik bo'ladi.</p>",
        "correct": "Kichik",
        "choices": ["Katta", "Kichik", "Teng", "Manfiy"]
    },
    {
        "text": "<p>5612 va 963 sonlaridan qaysi biri katta?</p>",
        "hint": "<p>Xonalar sonini sanang.</p>",
        "explanation": "<p><strong>5612</strong>: Turli xonali sonlarni taqqoslaganda qaysi birining xonalari ko'p bo'lsa, o'shanisi katta bo'ladi. 4 xonali son doim 3 xonali sondan katta.</p>",
        "correct": "5612",
        "choices": ["5612", "963", "Ular teng", "Taqqoslab bo'lmaydi"]
    },
    {
        "text": "<p>Qo'shishning o'rin almashtirish qonuni qaysi ifodada to'g'ri ko'rsatilgan?</p>",
        "hint": "<p>Qo'shiluvchilar o'rnini almashtirish yig'indiga ta'sir qilmaydi.</p>",
        "explanation": "<p><strong>a + b = b + a</strong>: Qo'shiluvchilarning o'rnini almashtirgan bilan yig'indi o'zgarmaydi.</p>",
        "correct": "a + b = b + a",
        "choices": ["a + b = b + a", "a + (b + c) = (a + b) + c", "a - b = b - a", "a * b = b * a"]
    },
    {
        "text": "<p>Har qanday songa 0 (nol) qo'shilganda nima hosil bo'ladi?</p>",
        "hint": "<p>Nol - hech narsa qo'shilmasligini bildiradi.</p>",
        "explanation": "<p><strong>O'sha sonning o'zi</strong>: Ikki qo'shiluvchidan biri nol bo'lsa, yig'indi ikkinchi qo'shiluvchiga teng bo'ladi.</p>",
        "correct": "O'sha sonning o'zi",
        "choices": ["Nol", "O'sha sonning o'zi", "Bir", "O'n"]
    },
    {
        "text": "<p>Ayirish amali natijasi nima deb ataladi?</p>",
        "hint": "<p>Qo'shish natijasi yig'indi, ayirishniki-chi?</p>",
        "explanation": "<p><strong>Ayirma</strong>: Ayiriladigan son ayiriluvchi, ayiriluvchi ayriladigan son kamayuvchi va ayirish amali natijasi ayirma deb ataladi.</p>",
        "correct": "Ayirma",
        "choices": ["Yig'indi", "Ayirma", "Ko'paytma", "Bo'linma"]
    },
    {
        "text": "<p>Sondan yig'indini ayirish qoidasi qaysi javobda to'g'ri berilgan?</p>",
        "hint": "<p>Qavslarni ochish xossasini eslang.</p>",
        "explanation": "<p><strong>a - (b + c) = a - b - c</strong>: Sondan yig'indini ayirish uchun oldin kamayuvchidan biror qo'shiluvchini ayirish, so'ng ayirmadan ikkinchi qo'shiluvchini ayirish kifoya.</p>",
        "correct": "a - (b + c) = a - b - c",
        "choices": ["a - (b + c) = a - b - c", "a - (b + c) = a + b - c", "a - (b + c) = a - b + c", "a - (b + c) = a + b + c"]
    },
    {
        "text": "<p>Sondan nol (0) ayirilganda ayirma nimaga teng bo'ladi?</p>",
        "hint": "<p>Hech narsa ayirilmasa nima qoladi?</p>",
        "explanation": "<p><strong>O'sha sonning o'ziga</strong>: Sondan nol ayirilganda ayirma o'sha sonning o'zi bo'ladi.</p>",
        "correct": "O'sha sonning o'ziga",
        "choices": ["Nolga", "O'sha sonning o'ziga", "Birga", "Manfiy songa"]
    },
    {
        "text": "<p>Tenglama ildizi deb nimaga aytiladi?</p>",
        "hint": "<p>Tenglikni to'g'ri qilish uchun kerak bo'ladigan qiymatga e'tibor qarating.</p>",
        "explanation": "<p><strong>Noma'lum harfning tenglamani to'g'ri tenglikka aylantiradigan qiymatiga</strong>: Noma'lum harfning tenglamani to'g'ri sonli tenglikka aylantiradigan qiymati tenglamaning ildizi (yechimi) deb ataladi.</p>",
        "correct": "Noma'lum harfning tenglamani to'g'ri tenglikka aylantiradigan qiymatiga",
        "choices": ["Noma'lum harfga", "Harfli ifodaga", "Noma'lum harfning tenglamani to'g'ri tenglikka aylantiradigan qiymatiga", "Tenglik belgisiga"]
    },
    {
        "text": "<p>Noma'lum qo'shiluvchini topish uchun nima qilish kerak?</p>",
        "hint": "<p>Yig'indi va ma'lum qo'shiluvchi orasidagi bog'liqlikni eslang.</p>",
        "explanation": "<p><strong>Yig'indidan ma'lum qo'shiluvchini ayirish</strong>: Noma'lum qo'shiluvchini topish uchun yig'indidan ma'lum qo'shiluvchini ayirish kerak.</p>",
        "correct": "Yig'indidan ma'lum qo'shiluvchini ayirish",
        "choices": ["Yig'indiga ma'lum qo'shiluvchini qo'shish", "Yig'indidan ma'lum qo'shiluvchini ayirish", "Ikkala qo'shiluvchini ayirish", "Ma'lum qo'shiluvchidan yig'indini ayirish"]
    },
    {
        "text": "<p><strong>x + 23 = 57</strong> tenglamaning ildizini toping.</p>",
        "hint": "<p>Noma'lum qo'shiluvchini topish uchun yig'indidan ma'lum qo'shiluvchini ayiring.</p>",
        "explanation": "<p><strong>34</strong>: x = 57 - 23, demak x = 34.</p>",
        "correct": "34",
        "choices": ["80", "34", "44", "24"]
    },
    {
        "text": "<p>Noma'lum kamayuvchini topish uchun qanday amal bajariladi?</p>",
        "hint": "<p>Kamayuvchi eng katta son bo'ladi.</p>",
        "explanation": "<p><strong>Ayiriluvchini ayirmaga qo'shish</strong>: Noma'lum kamayuvchini topish uchun ayiriluvchini ayirmaga qo'shish kerak.</p>",
        "correct": "Ayiriluvchini ayirmaga qo'shish",
        "choices": ["Ayirmadan ayiriluvchini ayirish", "Ayiriluvchini ayirmaga qo'shish", "Kamayuvchini ayirmaga qo'shish", "Ayiriluvchiga nol qo'shish"]
    },
    {
        "text": "<p><strong>y - 9 = 16</strong> tenglamani yeching.</p>",
        "hint": "<p>Noma'lum kamayuvchini topish amalini bajaring.</p>",
        "explanation": "<p><strong>25</strong>: y = 16 + 9, demak y = 25.</p>",
        "correct": "25",
        "choices": ["25", "7", "15", "27"]
    },
    {
        "text": "<p>Noma'lum ayiriluvchini topish uchun nima qilish kerak?</p>",
        "hint": "<p>Kamayuvchi va ayirma orasidagi munosabatni o'ylab ko'ring.</p>",
        "explanation": "<p><strong>Kamayuvchidan ayirmani ayirish</strong>: Noma'lum ayiriluvchini topish uchun kamayuvchidan ayirmani ayirish kerak.</p>",
        "correct": "Kamayuvchidan ayirmani ayirish",
        "choices": ["Kamayuvchiga ayirmani qo'shish", "Kamayuvchidan ayirmani ayirish", "Ayirmadan kamayuvchini ayirish", "Ikkalasini ko'paytirish"]
    },
    {
        "text": "<p><strong>38 - z = 12</strong> tenglamadagi z ning qiymatini toping.</p>",
        "hint": "<p>Noma'lum ayiriluvchini topish amalidan foydalaning.</p>",
        "explanation": "<p><strong>26</strong>: z = 38 - 12, demak z = 26.</p>",
        "correct": "26",
        "choices": ["50", "26", "16", "36"]
    },
    {
        "text": "<p>Sonlar, arifmetik amallar va qavslardan tuzilgan ifodalar qanday ataladi?</p>",
        "hint": "<p>Faqat sonlar ishtirok etishiga e'tibor qarating.</p>",
        "explanation": "<p><strong>Sonli ifodalar</strong>: Sonlar, arifmetik amallar va qavslardan tuzilgan ifodalar sonli ifodalar deb ataladi.</p>",
        "correct": "Sonli ifodalar",
        "choices": ["Harfli ifodalar", "Sonli ifodalar", "Tenglamalar", "Tengsizliklar"]
    },
    {
        "text": "<p>Harflar ham ishtirok etgan ifoda qanday nomlanadi?</p>",
        "hint": "<p>Harflar va sonlar birgalikda kelsa nima deyiladi?</p>",
        "explanation": "<p><strong>Harfli ifoda</strong>: Sonlar, arifmetik amallar, qavslar bilan bir qatorda harflar ham ishtirok etgan ifoda harfli yoki harfiy ifoda deb ataladi.</p>",
        "correct": "Harfli ifoda",
        "choices": ["Sonli ifoda", "Tenglama", "Harfli ifoda", "Qonun"]
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