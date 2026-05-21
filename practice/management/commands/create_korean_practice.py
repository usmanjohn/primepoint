from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice
QUESTIONS = [
    {
        'text': "<p><strong>A: 지민 씨, 제주도 날씨가 어때요?<br>B: 바람이 많이 ________ 아주 춥습니다.</strong></p>",
        'explanation': "<p><strong>불고</strong>: Sharoitlarni ketma-ket qo'shib ifodalash uchun Fe'l o'zagiga (불다) <code>-고</code> bog'lovchisi qo'shiladi.</p>",
        'correct': "불고",
        'choices': ["불고", "불거나", "부는데", "불지만"]
    },
    {
        'text': "<p><strong>A: 한국 요리는 보통 어때요?<br>B: 조금 매________ 아주 맛있습니다.</strong></p>",
        'explanation': "<p><strong>우나</strong>: Bu yerda qarama-qarshilik ma'nosidagi <code>-지만</code> grammatikasi to'g'ri keladi (매우다 + 지만 = 매웁지만 -> 매우+지만 = 매지만).</p>",
        'correct': "매워요",
        'choices': ["맵고", "맵거나", "맵지만", "매운데"]
    },
    {
        'text': "<p><strong>A: 주말에 보통 뭐 하세요?<br>B: 집에서 책을 일________ 음악을 들어요.</strong></p>",
        'explanation': "<p><strong>읽거나</strong>: Ikki harakatdan birini tanlash ('yoki') ma'nosida faqat fe'llarga qo'shiladigan <code>-거나</code> ishlatiladi.</p>",
        'correct': "읽거나",
        'choices': ["읽고", "읽거나", "읽지만", "읽는데"]
    },
    {
        'text': "<p><strong>A: 이 백화점 물건들은 어때요?<br>B: 디자인은 예________ 가격이 너무 비싸요.</strong></p>",
        'explanation': "<p><strong>쁜데</strong>: Sifatlar bilan (예쁘다) kontekst yaratish yoki yumshoq qarama-qarshilik bildirish uchun <code>-(으)는데</code> (예쁜데) ishlatiladi.</p>",
        'correct': "예쁜데",
        'choices': ["예쁘고", "예쁘거나", "예쁜데", "예쁘지만"]
    },
    {
        'text': "<p><strong>A: 요즘 날씨가 어때요?<br>B: 낮에는 따뜻하________ 밤에는 꽤 쌀쌀해요.</strong></p>",
        'explanation': "<p><strong>지만</strong>: Kunduzi va kechasi o'rtasidagi yaqqol qarama-qarshilikni ko'rsatish uchun <code>-지만</code> eng ma'qul variantdir.</p>",
        'correct': "지만",
        'choices': ["고", "거나", "지만", "는데"]
    },
    {
        'text': "<p><strong>A: 소라 씨, 지금 뭐 해요?<br>B: 친구를 기다리________ 지루해서 미치겠어요.</strong></p>",
        'explanation': "<p><strong>는데</strong>: Hozirgi holatni tushuntirib, unga zamin yaratish (kontekst) uchun fe'lga <code>-는데</code> qo'shiladi.</p>",
        'correct': "기다리는데",
        'choices': ["기다리고", "기다리거나", "기다리지만", "기다리는데"]
    },
    {
        'text': "<p><strong>A: 이 신발은 어때요?<br>B: 굽이 높________ 발이 전혀 아프지 않아요.</strong></p>",
        'explanation': "<p><strong>지만</strong>: 'To'pig'i baland, lekin oyoq og'rimaydi' degan keskin qarama-qarshilikni ifodalash uchun <code>-지만</code> kerak.</p>",
        'correct': "높지만",
        'choices': ["높고", "높거나", "높지만", "높은데"]
    },
    {
        'text': "<p><strong>A: 목이 너무 아파요.<br>B: 따뜻한 물을 마시________ 약을 드세요.</strong></p>",
        'explanation': "<p><strong>거나</strong>: Ikki maslahatdan birini bajarish tanlovini ko'rsatish uchun fe'lga <code>-거나</code> qo'shiladi.</p>",
        'correct': "마시거나",
        'choices': ["마시고", "마시거나", "마시지만", "마시는데"]
    },
    {
        'text': "<p><strong>A: 새로 이사한 집은 어때요?<br>B: 조용하________ 넓어서 아주 마음에 들어요.</strong></p>",
        'explanation': "<p><strong>고</strong>: Ijobiy sifatlarni ketma-ket sanab o'tish uchun sifat o'zagiga <code>-고</code> ulangan.</p>",
        'correct': "조용하고",
        'choices': ["조용하고", "조용하거나", "조용하지만", "조용 한데"]
    },
    {
        'text': "<p><strong>A: 어제 산 가방은 잘 들고 다녀요?<br>B: 크기는 작________ 수납공간이 많아서 편해요.</strong></p>",
        'explanation': "<p><strong>은데</strong>: Sifat (작다) unli bilan tugamagan (받침 bor), shuning uchun fon yaratish ma'nosida <code>-은데</code> shakli to'g'ri bo'ladi.</p>",
        'correct': "작은데",
        'choices': ["작고", "작거나", "작은데", "작지만"]
    },
    {
        'text': "<p><strong>A: 주말에 영화를 볼까요?<br>B: 제가 지금 좀 바________ 내일 보면 안 될까요?</strong></p>",
        'explanation': "<p><strong>쁜데</strong>: O'zining bandligini sabab/fon qilib ko'rsatib, rad javobini silliq ifodalashda <code>-ㄴ데</code> (바쁜데) ishlatiladi.</p>",
        'correct': "바쁜데",
        'choices': ["바쁘고", "바쁘거나", "바쁜데", "바쁘지만"]
    },
    {
        'text': "<p><strong>A: 이 옷은 어때요?<br>B: 색상이 밝________ 가볍고 시원해 보여요.</strong></p>",
        'explanation': "<p><strong>고</strong>: 'Yorqin va yengil' ma'nosida ikkita ijobiy sifatni bog'lash uchun <code>-고</code> to'g'ri tanlovdir.</p>",
        'correct': "밝고",
        'choices': ["밝고", "밝거나", "밝지만", "밝은데"]
    },
    {
        'text': "<p><strong>A: 스트레스를 받으면 어떻게 해요?<br>B: 매운 음식을 먹________ 소리를 크게 질러요.</strong></p>",
        'explanation': "<p><strong>거나</strong>: Stressdan xalos bo'lishning ikki variantidan birini tanlashni ifodalash uchun fe'lga <code>-거나</code> ulanadi.</p>",
        'correct': "먹거나",
        'choices': ["먹고", "먹거나", "먹지만", "먹는데"]
    },
    {
        'text': "<p><strong>A: 한국 생활이 힘들지 않아요?<br>B: 처음에는 외롭________ 지금은 친구가 많아서 괜찮아요.</strong></p>",
        'explanation': "<p><strong>았지만</strong>: O'tmishdagi holat (외로웠다) bilan hozirgi holatni qarama-qarshi qo'yish uchun o'tgan zamon o'zagiga <code>-지만</code> qo'shilgan.</p>",
        'correct': "외로웠지만",
        'choices': ["외롭고", "외롭거나", "외로웠지만", "외로운데"]
    },
    {
        'text': "<p><strong>A: 민수 씨, 지금 시간 있어요?<br>B: 숙제를 하________ 어려운 부분이 있어서요. 좀 도와줄래요?</strong></p>",
        'explanation': "<p><strong>는데</strong>: Vaziyat haqida ma'lumot berib, yordam so'rashga zamin hozirlash uchun fe'lga <code>-는데</code> qo'shiladi.</p>",
        'correct': "하는데",
        'choices': ["하고", "하거나", "하지만", "하는데"]
    },
    {
        'text': "<p><strong>A: 저 가수가 누구예요?<br>B: 얼굴은 잘생기________ 노래는 별로 못해요.</strong></p>",
        'explanation': "<p><strong>지만</strong>: Tashqi ko'rinish va qobiliyat o'rtasidagi zidlikni ko'rsatish uchun <code>-지만</code> ishlatiladi.</p>",
        'correct': "잘생겼지만",
        'choices': ["잘생기고", "잘생기거나", "잘생겼지만", "잘생기는데"]
    },
    {
        'text': "<p><strong>A: 감기에 걸려서 머리가 너무 아파요.<br>B: 집에 가서 푹 쉬________ 병원에 꼭 가 보세요.</strong></p>",
        'explanation': "<p><strong>거나</strong>: Ikki harakatdan birini tanlash tavsiya etilganda fe'lga <code>-거나</code> qo'shiladi.</p>",
        'correct': "쉬거나",
        'choices': ["쉬고", "쉬거나", "쉬지만", "쉬는데"]
    },
    {
        'text': "<p><strong>A: 이 노트북 어때요?<br>B: 가볍________ 성능이 아주 좋아서 인기가 많아요.</strong></p>",
        'explanation': "<p><strong>고</strong>: Noutbukning yaxshi jihatlarini (yengil va kuchli) birgalikda sanash uchun <code>-고</code> ishlatiladi.</p>",
        'correct': "가볍고",
        'choices': ["가볍고", "가볍거나", "가볍지만", "가벼운데"]
    },
    {
        'text': "<p><strong>A: 혹시 마트 가세요?<br>B: 네, 가 마트에 가________ 필요한 거 있어요?</strong></p>",
        'explanation': "<p><strong>는데</strong>: Ma'lum bir harakatni bajarayotganini aytib, suhbatdoshdan ehtiyojini so'rash fonini yaratish uchun <code>-는데</code> qo'shiladi.</p>",
        'correct': "가는데",
        'choices': ["가고", "가거나", "가지만", "가는데"]
    },
    {
        'text': "<p><strong>A: 어제 본 영화는 어땠어요?<br>B: 조금 유치하________ 영상미가 무척 아름다웠어요.</strong></p>",
        'explanation': "<p><strong>지만</strong>: Salbiy jihat (yosh bolalarcha) va ijobiy jihat (vizual go'zallik) o'rtasidagi qarama-qarshilikni ko'rsatish uchun <code>-지만</code> ishlatiladi.</p>",
        'correct': "유치하지만",
        'choices': ["유치하고", "유치하거나", "유치하지만", "유치한데"]
    },
    {
        'text': "<p><strong>A: 길이 너무 막히네요.<br>B: 지하철을 타________ 버스를 타는 게 빠를 것 같아요.</strong></p>",
        'explanation': "<p><strong>거나</strong>: Transport vositalarini tanlash imkoniyatini ko'rsatish uchun fe'l o'zagiga <code>-거나</code> ulanadi.</p>",
        'correct': "타거나",
        'choices': ["타고", "타거나", "타지만", "탄데"]
    },
    {
        'text': "<p><strong>A: 김치찌개가 많이 매워요?<br>B: 외관은 매워 보이________ 생각보다 맵지 않아요.</strong></p>",
        'explanation': "<p><strong>지만</strong>: Ko'rinishi va haqiqiy ta'mi o'rtasidagi zidlikni aniq ifodalash uchun <code>-지만</code> grammatikasi qo'llaniladi.</p>",
        'correct': "보이지만",
        'choices': ["보이고", "보이거나", "보이지만", "보이는데"]
    },
    {
        'text': "<p><strong>A: 이 카페는 항상 사람이 많네요.<br>B: 분위기가 좋________ 커피 맛도 훌륭하거든요.</strong></p>",
        'explanation': "<p><strong>고</strong>: Kafening afzalliklarini ketma-ket qo'shib ta'riflash uchun <code>-고</code> to'g'ri keladi.</p>",
        'correct': "좋고",
        'choices': ["좋고", "좋거나", "좋지만", "좋은데"]
    },
    {
        'text': "<p><strong>A: 저 옷을 사고 싶은데 돈이 부족해요.<br>B: 돈을 더 모으________ 아르바이트를 시작해 보세요.</strong></p>",
        'explanation': "<p><strong>거나</strong>: Muammoni hal qilish uchun taklif etilayotgan ikki yo'ldan biri nazarda tutilgani uchun fe'lga <code>-거나</code> qo'shiladi.</p>",
        'correct': "모으거나",
        'choices': ["모으고", "모으거나", "모으지만", "모으는데"]
    },
    {
        'text': "<p><strong>A: 한국말을 왜 이렇게 잘해요?<br>B: 매일 연습하________ 아직 발음이 많이 서툴러요.</strong></p>",
        'explanation': "<p><strong>지만</strong>: Harakat (har kuni mashq qilish) va natija (talaffuzning xomligi) o'rtasidagi qarama-qarshilikni ko'rsatish uchun <code>-지만</code> ishlatiladi.</p>",
        'correct': "연습하지만",
        'choices': ["연습하고", "연습하거나", "연습하지만", "연습하는데"]
    },
    {
        'text': "<p><strong>A: 배가 고픈데 냉장고에 먹을 게 없네요.<br>B: 제가 라면을 끓이________ 같이 먹을래요?</strong></p>",
        'explanation': "<p><strong>는데</strong>: Keyingi taklifga zamin yaratuvchi holatni tushuntirish uchun fe'lga <code>-는데</code> qo'shiladi.</p>",
        'correct': "끓이는데",
        'choices': ["끓이고", "끓이거나", "끓이지만", "끓이는데"]
    },
    {
        'text': "<p><strong>A: 시험 준비는 잘 돼 가요?<br>B: 밤을 새워 공부하________ 성적이 잘 안 나와서 속상해요.</strong></p>",
        'explanation': "<p><strong>지만</strong>: Qilingan mehnat (tunni tunga ulab o'qish) va kutilmagan salbiy natija o'rtasidagi keskin farq uchun <code>-지만</code> qo'llaniladi.</p>",
        'correct': "공부하지만",
        'choices': ["공부하고", "공부하거나", "공부하지만", "공부하는데"]
    },
    {
        'text': "<p><strong>A: 이 스마트폰은 어떤가요?<br>B: 화질이 선명하________ 배터리가 오래가서 아주 좋습니다.</strong></p>",
        'explanation': "<p><strong>고</strong>: Telefonning ikki xil ijobiy sifatini (tiniq tasvir va uzoqqa yetadigan batareya) birlashtirish uchun <code>-고</code> to'g'ri variantdir.</p>",
        'correct': "선명하고",
        'choices': ["선명하고", "선명하거나", "선명하지만", "선명한데"]
    },
    {
        'text': "<p><strong>A: 주말에 주로 집에서 쉬나요?<br>B: 네, 잠을 자________ 하루 종일 게임을 해요.</strong></p>",
        'explanation': "<p><strong>거나</strong>: Dam olish kunidagi ikki xil mashg'ulotdan birini tanlab bajarish ma'nosida fe'lga <code>-거나</code> ulangan.</p>",
        'correct': "자거나",
        'choices': ["자고", "자거나", "자지만", "자는데"]
    },
    {
        'text': "<p><strong>A: 지수 씨한테 연락해 봤어요?<br>B: 전화를 하________ 전화를 받지 않네요. 무슨 일 있을까요?</strong></p>",
        'explanation': "<p><strong>는데</strong>: Qo'ng'iroq qilganlik holatini fon qilib ko'rsatib, uning oqibatini aytish uchun fe'lga <code>-는데</code> qo'shiladi.</p>",
        'correct': "하는데",
        'choices': ["하고", "하거나", "하지만", "하는데"]
    }
]




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
            name='한국어',
            defaults={'description': '한국어 문법 및 어휘 연습'},
        )

        practice, created = Practice.objects.get_or_create(
            title='11-dars: Gaplarni bog\'lash',  # --- IGNORE ---
            master=master,
            defaults={
                'description': 'Gaplarni bog\'lovchi yuklamalar.',
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
