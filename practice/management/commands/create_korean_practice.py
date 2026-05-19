from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
    {
        'text': "<p><strong>A: 어제 파티에 왜 안 왔어요?<br>B: 갑자기 배가 너무 아파서 ________.</strong></p>",
        'explanation': "<p><strong>가지 못했어요</strong>: Kasallik tufayli bora olmaslik (imkoniyat yo'qligi) <code>-지 못하다</code> bilan o'tgan zamonda ifodalanadi.</p>",
        'correct': "가지 못했어요",
        'choices': ["가지 않았어요", "안 갔어요", "가지 못했어요", "가지 않아요"]
    },
    {
        'text': "<p><strong>A: 이 구두 살 거예요?<br>B: 아니요, 디자인은 예쁜데 가격이 너무 비싸서 ________.</strong></p>",
        'explanation': "<p><strong>안 살 거예요</strong>: O'z xohishi/qarori bilan sotib olmaslik <code>안 V</code> yoki <code>-지 않다</code> orqali beriladi.</p>",
        'correct': "안 살 거예요",
        'choices': ["못 살 거예요", "안 살 거예요", "사지 못해요", "사지 않아요"]
    },
    {
        'text': "<p><strong>A: 요즘도 매일 운동하세요?<br>B: 아니요, 최근에 회사 일이 너무 바빠서 아예 운동을 ________.</strong></p>",
        'explanation': "<p><strong>못 해요</strong>: Vaqt yo'qligi sababli mashq qila olmaslik <code>못 V</code> bilan yoziladi.</p>",
        'correct': "못 해요",
        'choices': ["못 해요", "안 해요", "하지 않아요", "하지 않았어요"]
    },
    {
        'text': "<p><strong>A: 한국어 뉴스를 다 알아들어요?<br>B: 아니요, 말이 너무 빨라서 아직 완벽하게 ________.</strong></p>",
        'explanation': "<p><strong>이해하지 못해요</strong>: Qobiliyat yoki bilim yetishmasligi sababli tushuna olmaslik <code>-지 못하다</code> orqali yasaladi.</p>",
        'correct': "이해하지 못해요",
        'choices': ["이해하지 않아요", "안 이해해요", "이해하지 않았어요", "이해하지 못해요"]
    },
    {
        'text': "<p><strong>A: 겨울인데 날씨가 춥지 않네요.<br>B: 네, 올해 겨울은 예년보다 별로 ________.</strong></p>",
        'explanation': "<p><strong>춥지 않아요</strong>: Sifatlarni (춥다 - sovuq) inkor qilishda faqat <code>안</code> yoki <code>-지 않다</code> ishlatiladi. Sifatlar bilan '못' qo'llanmaydi.</p>",
        'correct': "춥지 않아요",
        'choices': ["춥지 못해요", "춥지 않아요", "못 추워요", "안 추웠어요"]
    },
    {
        'text': "<p><strong>A: 내일 아침 회의에 참석할 수 있어요?<br>B: 죄송해요. 내일 오전에 병원에 가야 해서 ________.</strong></p>",
        'explanation': "<p><strong>참석하지 못해요</strong>: Boshqa reja sababli qatnasha olmaslik (imkoniyat yo'qligi) <code>-지 못하다</code> bilan aytiladi.</p>",
        'correct': "참석하지 못해요",
        'choices': ["참석하지 않아요", "안 참석해요", "참석하지 못해요", "참석하지 않았어요"]
    },
    {
        'text': "<p><strong>A: 출근할 때 운전해서 가요?<br>B: 아니요, 아침에 차가 막히는 게 싫어서 평소에 운전을 아예 ________.</strong></p>",
        'explanation': "<p><strong>안 해요</strong>: Tirbandlikni yoqtirmagani uchun o'z xohishi bilan mashina haydamaslik <code>안 V</code> (oddiy inkor) orqali beriladi.</p>",
        'correct': "안 해요",
        'choices': ["안 해요", "못 해요", "하지 못해요", "하지 못했어요"]
    },
    {
        'text': "<p><strong>A: 아까 전화 왜 안 받았어요?<br>B: 회의 중이라서 휴대폰 소리를 전혀 ________.</strong></p>",
        'explanation': "<p><strong>듣지 못했어요</strong>: Majlisda bo'lgani uchun ovozni eshitishga imkon bo'lmagani (tashqi sabab) <code>-지 못하다</code> qolipiga tushadi.</p>",
        'correct': "듣지 못했어요",
        'choices': ["듣지 않았어요", "안 들었어요", "듣지 않아요", "듣지 못했어요"]
    },
    {
        'text': "<p><strong>A: 이 가방 어때요? 무거워 보여요.<br>B: 아니요, 보기보다 별로 ________.</strong></p>",
        'explanation': "<p><strong>무겁지 않아요</strong>: '무겁다' (og'ir) sifat bo'lib, holatni inkor qilish uchun <code>-지 않다</code> ishlatamiz.</p>",
        'correct': "무겁지 않아요",
        'choices': ["무겁지 못해요", "못 무거워요", "무겁지 않아요", "안 무거웠어요"]
    },
    {
        'text': "<p><strong>A: 삼겹살 좀 드시겠어요?<br>B: 저는 채식주의자라서 고기를 절대 ________.</strong></p>",
        'explanation': "<p><strong>먹지 않아요</strong>: E'tiqod yoki qat'iy qaror tufayli go'sht yemaslik <code>-지 않다</code> bilan ifodalanadi.</p>",
        'correct': "먹지 않아요",
        'choices': ["먹지 않아요", "먹지 못해요", "못 먹어요", "안 먹었어요"]
    },
    {
        'text': "<p><strong>A: 어제 밤에 일찍 주무셨어요?<br>B: 아니요, 커피를 너무 많이 마셔서 새벽까지 ________.</strong></p>",
        'explanation': "<p><strong>자지 못했어요</strong>: Qahva ta'sirida uxlash imkoniyati yo'qolgani <code>-지 못하다</code> orqali o'tgan zamonda beriladi.</p>",
        'correct': "자지 못했어요",
        'choices': ["자지 않았어요", "자지 못했어요", "안 잤어요", "자지 않아요"]
    },
    {
        'text': "<p><strong>A: 저녁 식사 다 하셨어요?<br>B: 아니요, 입맛이 없어서 밥을 반도 ________.</strong></p>",
        'explanation': "<p><strong>못 먹었어요</strong>: Ishtaha yo'qligi sababli yeya olmaslik holati <code>못 V</code> orqali ko'rsatiladi.</p>",
        'correct': "못 먹었어요",
        'choices': ["안 먹었어요", "먹지 않았어요", "먹지 않아요", "못 먹었어요"]
    },
    {
        'text': "<p><strong>A: 컴퓨터 수리를 다 끝내셨나요?<br>B: 아니요, 부품이 없어서 아직 ________.</strong></p>",
        'explanation': "<p><strong>고치지 못했어요</strong>: Qism (detal) yo'qligi tufayli ta'mirlay olmaslik qobiliyat/imkoniyat cheklanganligini bildiradi.</p>",
        'correct': "고치지 못했어요",
        'choices': ["고치지 않아요", "안 고쳤어요", "고치지 못했어요", "고치지 못해요"]
    },
    {
        'text': "<p><strong>A: 새 집은 마음에 들어요?<br>B: 방은 넓은데 거실이 생각보다 ________.</strong></p>",
        'explanation': "<p><strong>넓지 않아요</strong>: '넓다' (keng) sifatini inkor qilishda <code>-지 않다</code> qo'llaniladi.</p>",
        'correct': "넓지 않아요",
        'choices': ["넓지 못해요", "넓지 않아요", "못 넓어요", "안 넓었어요"]
    },
    {
        'text': "<p><strong>A: 오늘 저녁에 같이 영화 볼래요?<br>B: 미안해요. 내일 시험이 있어서 오늘은 ________.</strong></p>",
        'explanation': "<p><strong>못 가요</strong>: Imtihon sababli bora olmaslik (imkoniyat yo'qligi) <code>못 V</code> yordamida yoziladi.</p>",
        'correct': "못 가요",
        'choices': ["못 가요", "안 가요", "가지 않아요", "가지 않았어요"]
    },
    {
        'text': "<p><strong>A: 길에서 우연히 옛날 친구를 만났는데, 그 친구가 저를 ________.<br>B: 정말요? 서운했겠네요.</strong></p>",
        'explanation': "<p><strong>알아보지 못했어요</strong>: Taniy olmaslik (qobiliyat/imkoniyat yo'qligi) '알아보다' fe'li bilan <code>-지 못하다</code> shaklida keladi.</p>",
        'correct': "알아보지 못했어요",
        'choices': ["알아보지 않았어요", "안 알아봤어요", "알아보지 못해요", "알아보지 못했어요"]
    },
    {
        'text': "<p><strong>A: 이 국이 많이 짠가요?<br>B: 아니요, 간이 딱 맞아서 하나도 ________.</strong></p>",
        'explanation': "<p><strong>짜지 않아요</strong>: '짜다' (sho'r) sifatiga inkor shakli <code>-지 않다</code> yoki <code>안</code> qo'shiladi.</p>",
        'correct': "짜지 않아요",
        'choices': ["짜지 못해요", "짜지 않아요", "못 짜요", "안 짰어요"]
    },
    {
        'text': "<p><strong>A: 한국 노래를 부를 줄 알아요?<br>B: 아니요, 가사를 몰라서 아직 한 곡도 ________.</strong></p>",
        'explanation': "<p><strong>부르지 못해요</strong>: Matnni bilmagani uchun kuylay olmaslik imkoniyatsizligi <code>-지 못하다</code> bilan ko'rsatiladi.</p>",
        'correct': "부르지 못해요",
        'choices': ["부르지 않아요", "안 불러요", "부르지 못해요", "부르지 않았어요"]
    },
    {
        'text': "<p><strong>A: 일요일에 항상 등산하세요?<br>B: 아니요, 비가 오는 날에는 위험해서 아예 ________.</strong></p>",
        'explanation': "<p><strong>안 가요</strong>: Xavfli bo'lgani uchun o'z qarori bilan toqqa chiqmasligi <code>안 V</code> bilan aytiladi.</p>",
        'correct': "안 가요",
        'choices': ["안 가요", "못 가요", "가지 못해요", "가지 못했어요"]
    },
    {
        'text': "<p><strong>A: 어제 보낸 이메일 확인하셨어요?<br>B: 죄송해요. 인터넷이 끊겨서 아직 ________.</strong></p>",
        'explanation': "<p><strong>확인하지 못했어요</strong>: Internet tarmog'i yo'qligi sababli tekshira olmaslik <code>-지 못하다</code> orqali beriladi.</p>",
        'correct': "확인하지 못했어요",
        'choices': ["확인하지 않았어요", "안 확인했어요", "확인하지 않아요", "확인하지 못했어요"]
    },
    {
        'text': "<p><strong>A: 새로 산 치마를 왜 한 번도 안 입었어요?<br>B: 사이즈가 너무 작아서 저한테 ________.</strong></p>",
        'explanation': "<p><strong>맞지 않아요</strong>: Kiyimning o'ziga mos kelmasligi (맞다) holatni bildiradi, shuning uchun <code>-지 않다</code> ishlatiladi.</p>",
        'correct': "맞지 않아요",
        'choices': ["맞지 못해요", "맞지 않아요", "못 맞아요", "안 맞았어요"]
    },
    {
        'text': "<p><strong>A: 어제 약속 시간에 왜 늦었어요?<br>B: 길을 잃어버려서 제시간에 ________.</strong></p>",
        'explanation': "<p><strong>도착하지 못했어요</strong>: Adashib qolganlik sababli manzilga vaqtida bora olmaslik <code>-지 못하다</code> qolipiga kiradi.</p>",
        'correct': "도착하지 못했어요",
        'choices': ["도착하지 않았어요", "안 도착했어요", "도착하지 못했어요", "도착하지 않아요"]
    },
    {
        'text': "<p><strong>A: 수영을 꽤 잘하시네요! 어렸을 때 배웠어요?<br>B: 아니요, 어릴 때는 물이 무서워서 전혀 ________.</strong></p>",
        'explanation': "<p><strong>하지 못했어요</strong>: Bolalikdagi suvdan qo'rqish sababli suza olmaslikni o'tgan zamonda <code>-지 못하다</code> bilan ifodalaymiz.</p>",
        'correct': "하지 못했어요",
        'choices': ["하지 못했어요", "하지 않았어요", "안 했어요", "하지 않아요"]
    },
    {
        'text': "<p><strong>A: 그 식당 음식은 어때요? 맛있어요?<br>B: 소문이 많이 났는데, 막상 먹어보니 별로 ________.</strong></p>",
        'explanation': "<p><strong>맛있지 않았어요</strong>: '맛있다' (mazali) sifati inkor qilinganda odatda <code>-지 않다</code> shaklidan foydalaniladi.</p>",
        'correct': "맛있지 않았어요",
        'choices': ["맛있지 못했어요", "못 맛있어요", "안 맛있었어요", "맛있지 않았어요"]
    },
    {
        'text': "<p><strong>A: 이메일 비밀번호를 잊어버렸어요?<br>B: 네, 아무리 생각해도 도무지 ________.</strong></p>",
        'explanation': "<p><strong>생각나지 않아요</strong>: Eslay olmaslik '생각나다' fe'li bilan <code>-지 않다</code> (o'z-o'zidan sodir bo'lmayotgan holat) sifatida ko'p ishlatiladi.</p>",
        'correct': "생각나지 않아요",
        'choices': ["생각나지 못해요", "생각나지 않아요", "못 생각나요", "안 생각났어요"]
    },
    {
        'text': "<p><strong>A: 담배 피우세요?<br>B: 아니요, 건강을 위해서 3년 전부터 아예 ________.</strong></p>",
        'explanation': "<p><strong>피우지 않아요</strong>: O'z xohishi bilan chekishni tashlagani <code>-지 않다</code> bilan ifodalanadi.</p>",
        'correct': "피우지 않아요",
        'choices': ["피우지 못해요", "피우지 못했어요", "피우지 않아요", "안 피웠어요"]
    },
    {
        'text': "<p><strong>A: 부모님께 자주 전화하세요?<br>B: 최근에 야근이 너무 많아서 거의 ________.</strong></p>",
        'explanation': "<p><strong>못 했어요</strong>: Haddan tashqari ko'p ishlagani sababli qo'ng'iroq qila olmaslik <code>못 V</code> bilan ko'rsatiladi.</p>",
        'correct': "못 했어요",
        'choices': ["못 했어요", "안 했어요", "하지 않았어요", "하지 않아요"]
    },
    {
        'text': "<p><strong>A: 아까 산 신발을 왜 환불했어요?<br>B: 디자인은 마음에 드는데, 신어보니까 전혀 ________.</strong></p>",
        'explanation': "<p><strong>편하지 않았어요</strong>: '편하다' (qulay) sifati inkor qilinganda <code>-지 않다</code> orqali aytiladi.</p>",
        'correct': "편하지 않았어요",
        'choices': ["편하지 못했어요", "못 편했어요", "안 편해요", "편하지 않았어요"]
    },
    {
        'text': "<p><strong>A: 이 책을 다 읽으셨나요?<br>B: 아니요, 내용이 너무 어려워서 끝까지 ________.</strong></p>",
        'explanation': "<p><strong>읽지 못했어요</strong>: Qiyinligi sababli o'qishni tugata olmaslik qobiliyatsizligi <code>-지 못하다</code> orqali beriladi.</p>",
        'correct': "읽지 못했어요",
        'choices': ["읽지 않았어요", "읽지 못했어요", "안 읽었어요", "읽지 않아요"]
    },
    {
        'text': "<p><strong>A: 지갑을 잃어버렸다고요? 찾으셨어요?<br>B: 온 집안을 다 뒤졌는데도 결국 ________.</strong></p>",
        'explanation': "<p><strong>찾지 못했어요</strong>: Har qancha qidirsa ham topa olmaslik natijasi <code>-지 못하다</code> orqali bildiriladi.</p>",
        'correct': "찾지 못했어요",
        'choices': ["찾지 않았어요", "안 찾았어요", "찾지 못했어요", "찾지 않아요"]
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
            title='Negatives: ~지 않다 / 안 V / ~지 못하다 / 못 V',  # --- IGNORE ---
            master=master,
            defaults={
                'description': 'Practice using various negative forms in Korean grammar, including ~지 않다, 안 V, ~지 못하다, and 못 V.',
                'subject': subject,
                'level': 'medium',
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
