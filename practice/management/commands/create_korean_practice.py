from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
    {
        'text': "<p><strong>A: 아지즈 씨, 어제 시장에서 뭐 샀어요?<br>B: 시장에서 사과________ 바나나를 샀어요. 과일이 아주 싱싱해요.</strong></p>",
        'explanation': "<p><strong>사과와</strong>: '사과' unli bilan tugagani uchun rasmiy/yozma bog'lovchi yuklama <code>-와</code> to'g'ri keladi. Variantlar ichida eng to'g'ri grammatik juftlikdir.</p>",
        'correct': "사과와",
        'choices': ["사과과", "사과와", "사과이랑", "사과하고랑"]
    },
    {
        'text': "<p><strong>A: 주말에 보통 혼자 쇼핑을 해요?<br>B: 아니요, 저는 주말마다 친구________ 같이 쇼핑몰에 가요.</strong></p>",
        'explanation': "<p><strong>친구하고</strong>: Kimdir bilan birgalikda (같이) harakat qilishni ifodalashda neytral <code>-하고</code> yuklamasi juda keng qo'llaniladi.</p>",
        'correct': "친구하고",
        'choices': ["친구과", "친구하고", "친구이랑", "친구은"]
    },
    {
        'text': "<p><strong>A: 안바르 씨, 방에 책상이 있어요?<br>B: 네, 제 방에는 책상________ 침대가 모두 있습니다.</strong></p>",
        'explanation': "<p><strong>책상과</strong>: '책상' undosh (pochim) bilan tugagani uchun va gap '습니다' rasmiy uslubida bo'lgani sababli <code>-과</code> yuklamasi eng to'g'ri javobdir.</p>",
        'correct': "책상과",
        'choices': ["책상와", "책상과", "책상랑", "책상을"]
    },
    {
        'text': "<p><strong>A: 동생, 내일 나________ 같이 도서관에 갈래?<br>B: 응, 좋아! 내일 아침에 일찍 만나서 같이 가자.</strong></p>",
        'explanation': "<p><strong>랑</strong>: Yaqin insonlar o'rtasidagi norasmiy og'zaki nutqda (반말) unli bilan tugagan '나' (men) so'ziga <code>-랑</code> yuklamasi qo'shiladi.</p>",
        'correct': "랑",
        'choices': ["과", "이랑", "랑", "하고과"]
    },
    {
        'text': "<p><strong>A: 비빔밥에 보통 무슨 재료가 들어가요?<br>B: 여러 가지 야채________ 고기가 들어가서 아주 영양이 풍부해요.</strong></p>",
        'explanation': "<p><strong>야채하고</strong>: Ikki mahsulotni bir-biriga bog'lash uchun unli/undosh ajratmaydigan <code>-하고</code> yuklamasi muloqotda juda tabiiy eshitiladi.</p>",
        'correct': "야채하고",
        'choices': ["야채과", "야채하고", "야채이랑", "야채를"]
    },
    {
        'text': "<p><strong>A: 켈리 씨, 어제 퇴근하고 뭐 하셨어요?<br>B: 회사 동료들________ 함께 식당에서 삼겹살을 먹었어요.</strong></p>",
        'explanation': "<p><strong>동료들과</strong>: '함께' (birgalikda) so'zi bilan rasmiy tarzda ishlatilganda, undosh bilan tugagan '동료들' so'ziga <code>-과</code> qo'shiladi.</p>",
        'correct': "동료들과",
        'choices': ["동료들와", "동료들과", "동료들랑", "동료들하고랑"]
    },
    {
        'text': "<p><strong>A: 우즈베키스탄 전통 음식 중에서 뭐가 제일 유명해요?<br>B: 기름밥________ 샤실릭이 제일 인기가 많고 맛있어요.</strong></p>",
        'explanation': "<p><strong>기름밥이랑</strong>: '기름밥' undosh bilan tugagani uchun kundalik og'zaki nutq shakli bo'lgan <code>-이랑</code> yuklamasi variantlar orasida to'g'ri keladi.</p>",
        'correct': "기름밥이랑",
        'choices': ["기름밥랑", "기름밥이랑", "기름밥와", "기름밥과"]
    },
    {
        'text': "<p><strong>A: 오늘 아침 메뉴는 무엇이었습니까?<br>B: 간단하게 구운 빵________ 따뜻한 커피를 마셨습니다.</strong></p>",
        'explanation': "<p><strong>빵과</strong>: Gap '습니다' (rasmiy yozma uslub) bilan tugagani uchun, undosh bilan tugagan '빵' so'ziga <code>-과</code> yuklamasini qo'shish eng to'g'ri yechimdir.</p>",
        'correct': "빵과",
        'choices': ["빵와", "빵과", "빵랑", "빵하고랑"]
    },
    {
        'text': "<p><strong>A: 소라 씨, 이번 방학 때 누구하고 여행을 갈 거예요?<br>B: 고향에 있는 가족들________ 같이 제주도에 갈 계획이에요.</strong></p>",
        'explanation': "<p><strong>가족들하고</strong>: Savolda '누구하고' deb so'ralgani sababli, javobda ham unga mos ravishda <code>-하고</code> yuklamasidan foydalanish suhbatni ravon qiladi.</p>",
        'correct': "가족들하고",
        'choices': ["가족들와", "가족들하고", "가족들랑", "가족들을"]
    },
    {
        'text': "<p><strong>A: 수진아, 오늘 저녁에 김치찌개________ 불고기 중에서 뭘 먹을까?<br>B: 음, 나는 매콤한 김치찌개가 더 먹고 싶어.</strong></p>",
        'explanation': "<p><strong>찌개랑</strong>: Bir-biri bilan yaqin munosabatdagi og'zaki savolda unli bilan tugagan '찌개' so'zidan so'ng <code>-랑</code> yuklamasi keladi.</p>",
        'correct': "찌개랑",
        'choices': ["찌개과", "찌개랑", "찌개이랑", "찌개하고랑"]
    },
    {
        'text': "<p><strong>A: 한국의 겨울 날씨는 보통 어때요?<br>B: 눈이 많이 내리고 강한 바람________ 같이 찾아와서 아주 춥습니다.</strong></p>",
        'explanation': "<p><strong>바람과</strong>: Rasmiy tushuntirish berish jarayonida undosh bilan tugagan '바람' so'ziga <code>-과</code> yuklamasi qo'shiladi.</p>",
        'correct': "바람과",
        'choices': ["바람와", "바람과", "바람랑", "바람을"]
    },
    {
        'text': "<p><strong>A: 내일 학교에 갈 때 무엇을 가져가야 해요?<br>B: 교과서________ 필기도구를 꼭 챙겨오셔야 합니다.</strong></p>",
        'explanation': "<p><strong>교과서와</strong>: '교과서' unli bilan tugagani va jumlada rasmiy ohang (합니다) borligi bois <code>-와</code> yuklamasi mos keladi.</p>",
        'correct': "교과서와",
        'choices': ["교과서과", "교과서와", "교과서이랑", "교과서를"]
    },
    {
        'text': "<p><strong>A: 어제 마트에서 우유를 샀어요?<br>B: 아니요, 우유는 안 사고 주스________ 생수만 몇 병 샀어요.</strong></p>",
        'explanation': "<p><strong>주스하고</strong>: Ikki ichimlik nomini o'zaro bog'lashda <code>-하고</code> yuklamasidan foydalanish kundalik hayotda eng ommabop usuldir.</p>",
        'correct': "주스하고",
        'choices': ["주스과", "주스하고", "주스이랑", "주스가"]
    },
    {
        'text': "<p><strong>A: 이번 프로젝트는 누구랑 같이 담당하게 되었어요?<br>B: 마케팅 팀의 영수 씨________ 같이 일하게 되었어요.</strong></p>",
        'explanation': "<p><strong>씨하고</strong>: Inson ismlari va unvonlaridan keyin (씨, 부장님) birgalikda ishlash ma'nosini neytral yoki og'zaki ifodalashda <code>-하고</code> juda to'g'ri keladi.</p>",
        'correct': "씨하고",
        'choices': ["씨과", "씨하고", "씨이랑", "씨를"]
    },
    {
        'text': "<p><strong>A: 지민아, 마트에 가면 뭐 사올까?<br>B: 내가 먹을 초콜릿________ 동생이 먹을 사탕 좀 사다 줘.</strong></p>",
        'explanation': "<p><strong>초콜릿이랑</strong>: Og'zaki suhbatda (사다 줘) undosh bilan tugagan '초콜릿' so'zi ortidan <code>-이랑</code> yuklamasi ishlatiladi.</p>",
        'correct': "초콜릿이랑",
        'choices': ["초콜릿랑", "초콜릿이랑", "초콜릿와", "초콜릿하고과"]
    },
    {
        'text': "<p><strong>A: 외국어를 배울 때는 무엇이 중요합니까?<br>B: 꾸준한 문법 공부________ 끊임없는 말하기 연습이 필요합니다.</strong></p>",
        'explanation': "<p><strong>공부와</strong>: Rasmiy ma'ruzaviy nutqda unli bilan tugagan '공부' so'zini keyingi otga bog'lash uchun <code>-와</code> ishlatiladi.</p>",
        'correct': "공부와",
        'choices': ["공부과", "공부와", "공부이", "공부랑"]
    },
    {
        'text': "<p><strong>A: 안드레이 씨, 한국에서 어떤 스포츠를 자주 해요?<br>B: 저는 주로 회사 동료들________ 축구나 테니스를 쳐요.</strong></p>",
        'explanation': "<p><strong>동료들하고</strong>: Hamkasblar bilan birga sport o'ynashni oddiy va samimiy tushuntirish uchun <code>-하고</code> qo'llaniladi.</p>",
        'correct': "동료들하고",
        'choices': ["동료들와", "동료들하고", "동료들랑", "동료들을"]
    },
    {
        'text': "<p><strong>A: 인형이 아주 귀엽네요. 누구한테 선물할 거예요?<br>B: 제 조카________ 제 친구 딸에게 주려고 두 개 샀어요.</strong></p>",
        'explanation': "<p><strong>조카하고</strong>: Ikki qabul qiluvchi shaxsni (조카, 친구 딸) ketma-ket bog'lab ko'rsatish uchun <code>-하고</code> to'g'ri keladi.</p>",
        'correct': "조카하고",
        'choices': ["조카과", "조카하고", "조카랑하고", "조카를"]
    },
    {
        'text': "<p><strong>A: 가방 안에 무엇이 들어 있습니까?<br>B: 여권________ 외국인등록증이 들어 있습니다. 중요한 물건입니다.</strong></p>",
        'explanation': "<p><strong>여권과</strong>: Hujjatlarni sanab ko'rsatishda va rasmiy gap (들어 있습니다) ohangida undoshli '여권' so'ziga <code>-과</code> mos keladi.</p>",
        'correct': "여권과",
        'choices': ["여권와", "여권과", "여권랑", "여권을"]
    },
    {
        'text': "<p><strong>A: 자밀 씨, 이번 주말에 약속이 있어요?<br>B: 고향에서 온 친척________ 같이 서울 구경을 하기로 했어요.</strong></p>",
        'explanation': "<p><strong>친척하고</strong>: Qarindosh (친척) bilan birga sayr qilishni ifodalashda keng qo'llaniladigan neytral <code>-하고</code> yuklamasi variantlar ichida to'g'ridir.</p>",
        'correct': "친척하고",
        'choices': ["친척과와", "친척하고", "친척랑", "친척을"]
    },
    {
        'text': "<p><strong>A: 식당에서 주문할 때 김밥________ 라면을 같이 시켰어요?<br>B: 네, 분식집에서는 그 두 가지를 같이 먹어야 맛있거든요.</strong></p>",
        'explanation': "<p><strong>김밥하고</strong>: Kundalik taomlanish mavzusidagi dialogda 'kimbap va ramen' birikmasini hosil qilish uchun <code>-하고</code> eng tabiiy shakldir.</p>",
        'correct': "김밥하고",
        'choices': ["김밥와", "김밥하고", "김밥랑하고", "김밥이"]
    },
    {
        'text': "<p><strong>A: 어머니 생신 선물로 무얼 준비하면 좋을까요?<br>B: 예쁜 화장품________ 따뜻한 스카프를 선물해 보세요. 좋아하실 거예요.</strong></p>",
        'explanation': "<p><strong>화장품과</strong>: Tavsiya berish jarayonida bir oz vazminlik va rasmiylikni saqlash maqsadida undosh bilan tugagan '화장품' so'ziga <code>-과</code> ulanadi.</p>",
        'correct': "화장품과",
        'choices': ["화장품와", "화장품과", "화장품랑", "화장품하고과"]
    },
    {
        'text': "<p><strong>A: 민우야, 너 어제 누구________ 하루 종일 있었어?<br>B: 하루 종일 집에서 강아지사랑 놀았어.</strong></p>",
        'explanation': "<p><strong>지랑</strong>: Unli bilan tugagan '누구' (kim) so'zi norasmiy suhbatda kelganda, unga <code>-랑</code> yuklamasi ulanishi qoidaga mos keladi (누구랑).</p>",
        'correct': "지랑",
        'choices': ["지과", "지이랑", "지랑", "지하고과"]
    },
    {
        'text': "<p><strong>A: 컴퓨터를 사려고 하는데 모니터________ 본체를 따로 사야 해요?<br>B: 요즘은 일체형 컴퓨터도 많지만, 보통은 따로 사는 게 성능이 좋아요.</strong></p>",
        'explanation': "<p><strong>모니터와</strong>: Texnik jihozlarni tushuntirish va o'zaro solishtirishda unli bilan tugagan '모니터' so'ziga yozma/rasmiy uslubdagi <code>-와</code> mos keladi.</p>",
        'correct': "모니터와",
        'choices': ["모니터과", "모니터와", "모니터랑", "모니터를"]
    },
    {
        'text': "<p><strong>A: 한국 생활 중에서 가장 적응하기 힘든 게 뭐예요?<br>B: 매운 음식________ 빠른 속도의 문화가 조금 힘들었어요. 지금은 괜찮아요.</strong></p>",
        'explanation': "<p><strong>음식과</strong>: '음식' (taom) so'zi undosh bilan tugagani va o'z tajribasini jiddiy tushuntirayotgani uchun rasmiy yozma uslubdagi <code>-과</code> yuklamasi to'g'ri bo'ladi.</p>",
        'correct': "음식과",
        'choices': ["음식와", "음식과", "음식랑", "음식을"]
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
            title='4-dars: Va/bilan',  # --- IGNORE ---
            master=master,
            defaults={
                'description': 'Va/bilan bog\'lovchi yuklamalar (과/와, 이랑/랑, 하고) mavzusidagi amaliy test.',
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
