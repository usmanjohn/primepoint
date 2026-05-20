from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS_PART2 = [
    {
        'text': "<p><strong>A: 아지즈 씨, 지금 어디에 가고 있어요?<br>B: 내일 시험이 있어서 공부하러 도서관________ 가고 있어요.</strong></p>",
        'explanation': "<p><strong>도서관에</strong>: '가다' (bormoq) yo'nalish fe'li kelganda, harakat yo'nalgan joyga <code>-에</code> kelishigi qo'shiladi.</p>",
        'correct': "도서관에",
        'choices': ["도서관에서", "도서관에", "도서관부터", "도서관까지"]
    },
    {
        'text': "<p><strong>A: 주말에 보통 어디에서 친구를 만나요?<br>B: 주말에는 보통 조용한 카페________ 만나서 커피를 마셔요.</strong></p>",
        'explanation': "<p><strong>카페에서</strong>: '만나다' (chrashmoq) kabi dinamik ish-harakat sodir bo'layotgan joyni ifodalash uchun o'rin-payt kelishigi (<code>-에서</code>) ishlatilishi kerak.</p>",
        'correct': "카페에서",
        'choices': ["카페에", "카페에서", "카페부터", "카페까지"]
    },
    {
        'text': "<p><strong>A: 회사 근무 시간이 어떻게 되나요?<br>B: 오전 9시________ 오후 6시까지 일합니다. 주말에는 쉽니다.</strong></p>",
        'explanation': "<p><strong>9시부터</strong>: Vaqtning boshlanish nuqtasini ko'rsatish uchun <code>-부터</code> yuklamasi ishlatiladi. '오후 6시까지' (soat 6-gacha) iborasi bilan juftlik hosil qiladi.</p>",
        'correct': "9시부터",
        'choices': ["9시에", "9시에서", "9시부터", "9시까지"]
    },
    {
        'text': "<p><strong>A: 안바르 씨의 고향은 어디예요?<br>B: 저는 우즈베키스탄________ 왔습니다. 만나서 반갑습니다.</strong></p>",
        'explanation': "<p><strong>우즈베키스탄에서</strong>: Kelib chiqish mamlakati yoki harakatning boshlanish joyini '오다' (kelmoq) fe'li bilan ifodalashda <code>-에서</code> ishlatiladi.</p>",
        'correct': "우즈베키스탄에서",
        'choices': ["우즈베키스탄에", "우즈베키스탄에서", "우즈베키스탄부터", "우즈베키스탄까지"]
    },
    {
        'text': "<p><strong>A: 집이 학교하고 가깝습니까?<br>B: 네, 아주 가깝습니다. 집________ 학교까지 걸어서 5분밖에 안 걸려요.</strong></p>",
        'explanation': "<p><strong>집에서</strong>: Joylar orasidagi masofa haqida gap ketganda, boshlanish joyiga <code>-에서</code>, tugash joyiga esa '까지' qo'shiladi.</p>",
        'correct': "집에서",
        'choices': ["집에", "집에서", "집부터", "집까지"]
    },
    {
        'text': "<p><strong>A: 마크 씨, 혹시 지금 방에 책상이 있어요?<br>B: 네, 방________ 침대하고 책상이 모두 있어요.</strong></p>",
        'explanation': "<p><strong>방에</strong>: Shaxs yoki narsaning ma'lum bir joyda mavjudligini (<code>있다/없다</code>) ko'rsatish uchun joy so'ziga <code>-에</code> qo'shiladi.</p>",
        'correct': "방에",
        'choices': ["방에", "방에서", "방부터", "방까지"]
    },
    {
        'text': "<p><strong>A: 한국 대학교는 보통 몇 월________ 첫 학기가 시작돼요?<br>B: 한국은 보통 3월에 새 학기가 시작됩니다.</strong></p>",
        'explanation': "<p><strong>월에</strong>: Muayyan vaqtni (yil, oy, kun, soat) ko'rsatish uchun vaqt so'zidan keyin har doim <code>-에</code> payt kelishigi qo'yiladi.</p>",
        'correct': "월에",
        'choices': ["월에", "월에서", "월부터", "월까지"]
    },
    {
        'text': "<p><strong>A: 어제 저녁에 왜 전화를 안 받았어요?<br>B: 미안해요. 그때 극장________ 친구하고 영화를 보고 있었어요.</strong></p>",
        'explanation': "<p><strong>극장에서</strong>: '영화를 보다' (kino ko'rmoq) dinamik harakati sodir bo'layotgan aniq joyni ifodalash uchun <code>-에서</code> talab qilinadi.</p>",
        'correct': "극장에서",
        'choices': ["극장에", "극장에서", "극장부터", "극장까지"]
    },
    {
        'text': "<p><strong>A: 겨울 방학이 언제까지예요?<br>B: 이번 주 금요일________ 방학이고 다음 주 월요일에 개학해요.</strong></p>",
        'explanation': "<p><strong>금요일까지</strong>: Vaqt yoki muddatning oxirgi tugash nuqtasini belgilash uchun <code>-까지</code> (gacha) yuklamasi qo'shiladi.</p>",
        'correct': "금요일까지",
        'choices': ["금요일에", "금요일에서", "금요일부터", "금요일까지"]
    },
    {
        'text': "<p><strong>A: 흐엉 씨, 한국에 언제 오셨어요?<br>B: 저는 지난주 토요일________ 한국에 도착했습니다.</strong></p>",
        'explanation': "<p><strong>토요일에</strong>: 'Geenhanju toyoil' (O'tgan hafta shanba) aniq vaqtni anglatgani uchun unga payt kelishigi <code>-에</code> biriktiriladi.</p>",
        'correct': "토요일에",
        'choices': ["토요일에", "토요일에서", "토요일부터", "토요일까지"]
    },
    {
        'text': "<p><strong>A: 매일 저녁 몇 시에 운동을 하세요?<br>B: 퇴근하고 보통 밤 8시________ 9시까지 헬스장에서 운동해요.</strong></p>",
        'explanation': "<p><strong>8시부터</strong>: Orqasidan '9시까지' kelgani sababli, vaqtning boshlanish chegarasini bildiruvchi <code>-부터</code> eng to'g'ri variantdir.</p>",
        'correct': "8시부터",
        'choices': ["8시에", "8시에서", "8시부터", "8시까지"]
    },
    {
        'text': "<p><strong>A: 안드레이 씨, 주말에 공원________ 뭐 했어요?<br>B: 날씨가 좋아서 자전거를 탔어요.</strong></p>",
        'explanation': "<p><strong>공원에서</strong>: 공원 (bog') ichida '자전거를 타다' (velosiped uchmoq) harakati bajarilgani sababli o'rin-payt kelishigi <code>-에서</code> qo'yiladi.</p>",
        'correct': "공원에서",
        'choices': ["공원에", "공원에서", "공원부터", "공원까지"]
    },
    {
        'text': "<p><strong>A: 실례지만 시청에 가려면 어디________ 내려야 합니까?<br>B: 다음 버스 정류장에서 내리시면 됩니다.</strong></p>",
        'explanation': "<p><strong>어디에서</strong>: '내리다' (tushmoq) harakati bajariladigan joy so'ralayotgani uchun <code>어디에서</code> (qayerda) shakli to'g'ri bo'ladi.</p>",
        'correct': "어디에서",
        'choices': ["어디에", "어디에서", "어디부터", "어디까지"]
    },
    {
        'text': "<p><strong>A: 수진 씨, 이번 휴가 때 어디________ 갈 거예요?<br>B: 가족들과 함께 제주도에 가려고 해요.</strong></p>",
        'explanation': "<p><strong>어디에</strong>: '갈 거예요' (bormoqchiman) yo'nalish fe'li bilan ishlatilganda, so'roq so'zi bo'lgan 'eodi' (qayer) ga <code>-에</code> qo'shiladi.</p>",
        'correct': "어디에",
        'choices': ["어디에", "어디에서", "어디부터", "어디까지"]
    },
    {
        'text': "<p><strong>A: 이 백화점은 몇 시에 문을 닫아요?<br>B: 밤 10시________ 영업이 끝납니다. 서두르세요.</strong></p>",
        'explanation': "<p><strong>10시에</strong>: Vaqt aniq ko'rsatilganda va o'sha vaqtda biror holat yuz berganda <code>-에</code> ishlatiladi.</p>",
        'correct': "10시에",
        'choices': ["10시에", "10시에서", "10시부터", "10시까지"]
    },
    {
        'text': "<p><strong>A: 서울역________ 인천공항까지 지하철로 얼마나 걸려요?<br>B: 급행열차를 타면 50분쯤 걸려요.</strong></p>",
        'explanation': "<p><strong>서울역에서</strong>: '인천공항까지' bilan bog'lanib, masofaning boshlanish nuqtasini ko'rsatgani uchun joy nomi ortidan <code>-에서</code> kelishi shart.</p>",
        'correct': "서울역에서",
        'choices': ["서울역에", "서울역에서", "서울역부터", "서울역까지"]
    },
    {
        'text': "<p><strong>A: 자밀 씨, 어제 쇼핑몰________ 옷을 많이 샀어요?<br>B: 아니요, 구경만 하고 아무것도 안 샀어요.</strong></p>",
        'explanation': "<p><strong>쇼핑몰에서</strong>: '옷을 사다' (kiyim sotib olmoq) yoki '구경하다' (tomosha qilmoq) harakatlari bajarilgan joyni anglatish uchun <code>-에서</code> mos keladi.</p>",
        'correct': "쇼핑몰에서",
        'choices': ["쇼핑몰에", "쇼핑몰에서", "쇼핑몰부터", "쇼핑몰까지"]
    },
    {
        'text': "<p><strong>A: 혹시 지갑을 어디에 두었는지 기억나요?<br>B: 아! 아까 거실 탁자 위________ 올려놓은 것 같아요. 가 보세요.</strong></p>",
        'explanation': "<p><strong>탁자 위에</strong>: Narsani ma'lum bir nuqtaga qo'yib qo'yish (올려놓다, 두다, 놓다) yo'nalishli joylashuvni bildirgani uchun <code>-에</code> bilan qo'llanadi.</p>",
        'correct': "탁자 위에",
        'choices': ["탁자 위에", "탁자 위에서", "탁자 위부터", "탁자 위까지"]
    },
    {
        'text': "<p><strong>A: 은행 업무는 보통 몇 시에 끝나요?<br>B: 오후 4시________ 은행 문을 닫으니까 그 전에 가셔야 해요.</strong></p>",
        'explanation': "<p><strong>4시에</strong>: Ish-harakat (bank yopilishi) sodir bo'ladigan aniq vaqt momentini ko'rsatgani uchun <code>-에</code> to'g'ri keladi.</p>",
        'correct': "4시에",
        'choices': ["4시에", "4시에서", "4시부터", "4시까지"]
    },
    {
        'text': "<p><strong>A: 오늘 한국어 수업은 몇 시부터예요?<br>B: 오후 2시________ 시작하니까 늦지 않게 오세요.</strong></p>",
        'explanation': "<p><strong>부터</strong>: Darsning boshlanish vaqt chegarasini ta'kidlayotgani va savolda '몇 시부터예요?' deb so'ralgani uchun javobda ham <code>-부터</code> ishlatiladi.</p>",
        'correct': "부터",
        'choices': ["에", "에서", "부터", "까지"]
    },
    {
        'text': "<p><strong>A: 식당 코너는 몇 층________ 있어요?<br>B: 건물 5층에 있으니까 엘리베이터를 타세요.</strong></p>",
        'explanation': "<p><strong>층에</strong>: '있다' (bor) fe'li bilan birga kelib, qavatning joylashuv o'rnini ko'rsatgani uchun <code>-에</code> qo'shiladi.</p>",
        'correct': "층에",
        'choices': ["층에", "층에서", "층부터", "층까지"]
    },
    {
        'text': "<p><strong>A: 소라 씨는 회사에 다녀요?<br>B: 아니요, 회사에 안 다녀요. 지금은 집________ 재택근무를 하고 있어요.</strong></p>",
        'explanation': "<p><strong>집에서</strong>: '재택근무를 하다' (uyda turib ishlamoq) harakat fe'li bo'lgani sababli harakat bajarilayotgan joyni ko'rsatuvchi <code>-에서</code> tanlanadi.</p>",
        'correct': "집에서",
        'choices': ["집에", "집에서", "집부터", "집까지"]
    },
    {
        'text': "<p><strong>A: 여름 휴가는 언제부터 언제까지예요?<br>B: 8월 1일부터 8월 5일________ 휴가예요.</strong></p>",
        'explanation': "<p><strong>5일까지</strong>: '8월 1일부터' (1-avgustdan) iborasi bilan bog'lanib, ta'til tugaydigan oxirgi muddat chegarasini ko'rsatish uchun <code>-까지</code> kerak.</p>",
        'correct': "5일까지",
        'choices': ["5일에", "5일에서", "5일부터", "5일까지"]
    },
    {
        'text': "<p><strong>A: 한국 여행을 가고 싶은데 어디가 좋아요?<br>B: 서울도 좋지만 제주도________ 꼭 가 보세요. 정말 아름다워요.</strong></p>",
        'explanation': "<p><strong>제주도에</strong>: '가 보다' (borib ko'rmoq) yo'nalishli fe'li bo'lgani sababli boriladigan manzilga <code>-에</code> qo'shiladi.</p>",
        'correct': "제주도에",
        'choices': ["제주도에", "제주도에서", "제주도부터", "제주도까지"]
    },
    {
        'text': "<p><strong>A: 한국어 말하기 대회가 어디________ 열립니까?<br>B: 대학교 본관 대강당에서 열릴 예정입니다.</strong></p>",
        'explanation': "<p><strong>어디에서</strong>: '열리다' (o'tkazilmoq/ochilmoq) tadbiri sodir bo'ladigan joy so'ralayotgani uchun <code>어디에서</code> qo'llanilishi lozim.</p>",
        'correct': "어디에서",
        'choices': ["어디에", "어디에서", "어디부터", "어디까지"]
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
            title='4-dars: Vaqt/Joy Kelishiklari',  # --- IGNORE ---
            master=master,
            defaults={
                'description': 'Koreys tili - 4 dars: Vaqt/Joy kelishiklari haqida testlar',
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
