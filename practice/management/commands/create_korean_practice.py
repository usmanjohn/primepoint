from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice
questions = [
    {
        'text': "<p>A: 새로 이사한 아파트는 살기에 좀 어때요?<br>B: 지하철역이 <u>바로</u> 앞이라 교통이 <strong>편리한</strong> ________ 집값이 <u>너무</u> 비싸서 부담돼요.</p>",
        'explanation': "<p><strong>반면에</strong>: 앞 주장의 긍정적인 사실('편리하다')과 뒤 주장의 상반된 부정적 사실('비싸다')을 대조하여 연결할 때 사용합니다.</p>",
        'correct': "반면에",
        'choices': ["뿐만 아니라", "데다가", "반면에", "바람에"]
    },
    {
        'text': "<p>A: 민수 씨는 주말마다 <u>항상</u> 바쁜 것 같아요.<br>B: 네, 민수 씨는 주말에 대학교 대학원에 <strong>다닐</strong> ________ 회사 업무 관련 학원까지 다닌대요.</p>",
        'explanation': "<p><strong>뿐만 아니라</strong>: 이미 대학교 대학원에 다닌다는 사실에 더해, 학원까지 다닌다는 심화된 추가 사실을 나타냅니다.</p>",
        'correct': "뿐만 아니라",
        'choices': ["반면에", "뿐만 아니라", "데다가", "탓에"]
    },
    {
        'text': "<p>A: 오늘 아침 출근길은 <u>정말</u> 끔찍했어요.<br>B: 맞아요. 안개가 <u>지나치게</u> <strong>짙게 낀</strong> ________ 갑자기 비까지 <u>세차게</u> 내리는 바람에 차가 <u>엄청</u> 막혔지요.</p>",
        'explanation': "<p><strong>데다가</strong>: '안개가 짙게 끼다'라는 안 좋은 상황에 '비까지 내리다'라는 부정적인 상황이 겹쳐 가중되었음을 나타냅니다.</p>",
        'correct': "데다가",
        'choices': ["데다가", "반면에", "뿐만 아니라", "셈이라"]
    },
    {
        'text': "<p>A: 이번에 새로 개봉한 영화를 보셨어요? 어때요?<br>B: 스토리가 <u>매우</u> <strong>탄탄한</strong> ________ 배우들의 연기력도 <u>무척</u> 뛰어난 덕분에 관객들에게 <u>엄청난</u> 호평을 받고 있어요.</p>",
        'explanation': "<p><strong>데다가</strong>: 영화의 좋은 점(탄탄한 스토리)에 또 다른 좋은 점(뛰어난 연기력)이 더해지는 상황의 가중을 표현합니다.</p>",
        'correct': "데다가",
        'choices': ["반면에", "척하느라", "데다가", "뻔해서"]
    },
    {
        'text': "<p>A: 정우 씨는 운동을 <u>참</u> 좋아하는 것 같아요.<br>B: 맞아요. 정우 씨는 축구를 <u>자주</u> <strong>할</strong> ________ 테니스 실력도 선수 못지않게 <u>상당히</u> 뛰어나대요.</p>",
        'explanation': "<p><strong>뿐만 아니라</strong>: 축구를 한다는 사실에 더해 테니스 실력도 뛰어나다는 사실을 점층적으로 추가하여 설명합니다.</p>",
        'correct': "뿐만 아니라",
        'choices': ["뿐만 아니라", "반면에", "데다가", "바람에"]
    },
    {
        'text': "<p>A: 이 식당은 손님이 <u>항상</u> 바글바글하네요.<br>B: 네, 이곳은 음식이 <u>아주</u> <strong>맛있는</strong> ________ 직원들도 <u>모두</u> <u>지나치게</u> 불친절해서 다시는 가고 싶지 않아요.</p>",
        'explanation': "<p><strong>반면에</strong>: 음식이 맛있다는 긍정적인 특징과 직원이 불친절하다는 부정적인 특징을 대조할 때 쓰입니다.</p>",
        'correct': "반면에",
        'choices': ["데다가", "반면에", "뿐만 아니라", "통에"]
    },
    {
        'text': "<p>A: 요즘 날씨가 <u>갑자기</u> <u>너무</u> 쌀쌀해진 것 같아요.<br>B: 네, 기온이 <u>뚝</u> <strong>떨어진</strong> ________ 바람까지 <u>강하게</u> 부니까 <u>훨씬</u> 더 춥게 느껴지네요.</p>",
        'explanation': "<p><strong>데다가</strong>: 기온이 떨어진 상황에 강한 바람이라는 또 다른 상황이 더해져 추위가 가중되었음을 뜻합니다.</p>",
        'correct': "데다가",
        'choices': ["뿐만 아니라", "반면에", "데다가", "마찬가지로"]
    },
    {
        'text': "<p>A: 진우 씨는 성격이 <u>무척</u> 활발하고 사교적인가 봐요.<br>B: 맞아요. <u>처음 보는</u> 사람과도 <u>쉽게</u> <strong>친해지는</strong> ________ 유머 감각도 <u>상당히</u> 풍부해서 주변에 늘 친구들이 많아요.</p>",
        'explanation': "<p><strong>뿐만 아니라</strong>: 사람들과 쉽게 친해진다는 장점에 더해 유머 감각까지 풍부하다는 긍정적 사실을 추가합니다.</p>",
        'correct': "뿐만 아니라",
        'choices': ["반면에", "뿐만 아니라", "데다가", "뻔하게"]
    },
    {
        'text': "<p>A: 지수 씨가 다니는 회사는 분위기가 어때요?<br>B: 연봉이 <u>상당히</u> <strong>높은</strong> ________ 야근이 <u>워낙</u> 잦고 업무 강도가 <u>지나치게</u> 높아서 힘들어해요.</p>",
        'explanation': "<p><strong>반면에</strong>: 연봉이 높다는 경제적 장점과 야근이 잦다는 직무적 단점을 상반되게 대조합니다.</p>",
        'correct': "반면에",
        'choices': ["반면에", "데다가", "뿐만 아니라", "셈 치고"]
    },
    {
        'text': "<p>A: 컴퓨터를 <u>오래</u> 사용하면 눈이 <u>많이</u> 피로해지지요?<br>B: 네, 눈이 <u>자주</u> <strong>침침해지는</strong> ________ 시력도 <u>급격히</u> 나빠질 수 있으니 <u>가끔</u> 쉬어 주어야 해요.</p>",
        'explanation': "<p><strong>뿐만 아니라</strong>: 눈이 침침해지는 부정적 현상에 시력이 나빠진다는 추가적인 부작용을 더해 강조합니다.</p>",
        'correct': "뿐만 아니라",
        'choices': ["반면에", "데다가", "뿐만 아니라", "다름없이"]
    },
    {
        'text': "<p>A: 어제 산 스마트폰은 사용하기에 <u>좀</u> 편리한가요?<br>B: 디자인이 <u>아주</u> <u>세련되고</u> <strong>가벼운</strong> ________ 배터리가 <u>너무</u> <u>빨리</u> 달아서 <u>여간</u> 불편한 게 아니에요.</p>",
        'explanation': "<p><strong>반면에</strong>: 외관과 무게의 장점과 배터리 수명의 단점이라는 서로 상반된 사실을 연결합니다.</p>",
        'correct': "반면에",
        'choices': ["데다가", "반면에", "뿐만 아니라", "일수록"]
    },
    {
        'text': "<p>A: 오늘 길에서 지갑을 잃어버려서 기분이 <u>정말</u> 우울해요.<br>B: 아이고, 속상하시겠어요. 지갑에 현금이 <u>많이</u> <strong>들어 있었던</strong> ________ 중요한 카드와 신분증까지 다 들어 있었나요?</p>",
        'explanation': "<p><strong>데다가</strong>: 현금이 많았다는 속상한 사실에 카드/신분증 손실이라는 부정적 상황이 더해지는 맥락입니다.</p>",
        'correct': "데다가",
        'choices': ["데다가", "반면에", "뿐만 아니라", "버려서"]
    },
    {
        'text': "<p>A: 이번 전통 시장 살리기 축제는 성과가 어땠나요?<br>B: 전통 시장을 찾는 방문객 수가 <u>부쩍</u> <strong>늘어난</strong> ________ 상인들의 매출도 <u>크게</u> 증가하여 성공적으로 끝났습니다.</p>",
        'explanation': "<p><strong>뿐만 아니라</strong>: 방문객 수 증가라는 성과에 상인들의 매출 증가라는 또 하나의 긍정적 성과를 누적하여 나타냅니다.</p>",
        'correct': "뿐만 아니라",
        'choices': ["반면에", "뿐만 아니라", "데다가", "다름없게"]
    },
    {
        'text': "<p>A: 수미 씨 동생은 형제가 어떻게 되나요?<br>B: 남동생은 공부를 <u>무척</u> <strong>잘하는</strong> ________ 여동생은 운동 분야에서 <u>상당한</u> 재능을 보이고 있어요.</p>",
        'explanation': "<p><strong>반면에</strong>: 남동생의 특징(공부)과 여동생의 특징(운동)을 서로 다르게 대조하여 기술합니다.</p>",
        'correct': "반면에",
        'choices': ["데다가", "뿐만 아니라", "반면에", "셈이라"]
    },
    {
        'text': "<p>A: 독감이 <u>유행이라더니</u> 몸 상태가 <u>무척</u> 안 좋아 보여요.<br>B: 네, 기침을 <u>심하게</u> <strong>하는</strong> ________ 고열까지 <u>동반되어</u> 나서 <u>도저히</u> 움직일 수가 없네요.</p>",
        'explanation': "<p><strong>데다가</strong>: 기침이라는 증상에 고열이라는 악재가 겹쳐서 일어난 상황의 중첩(가중)을 의미합니다.</p>",
        'correct': "데다가",
        'choices': ["데다가", "반면에", "뿐만 아니라", "뻔해서"]
    },
    {
        'text': "<p>A: 한국의 여름 날씨는 외국인들이 적응하기에 어때요?<br>B: 온도가 <u>매우</u> <strong>높은</strong> ________ 습도까지 <u>지나치게</u> 높아서 <u>조금만</u> 걸어도 땀이 <u>비 오듯</u> 흘러요.</p>",
        'explanation': "<p><strong>데다가</strong>: 높은 기온에 높은 습도라는 한국 여름 특유의 설상가상 상황을 가중하여 설명합니다.</p>",
        'correct': "데다가",
        'choices': ["반면에", "데다가", "뿐만 아니라", "마찬가지라"]
    },
    {
        'text': "<p>A: 이번에 새로 장만한 블루투스 이어폰은 어때요?<br>B: 음질이 <u>기대 이상으로</u> <strong>깨끗한</strong> ________ 가격도 <u>상당히</u> 저렴해서 가성비가 <u>정말</u> 최고예요.</p>",
        'explanation': "<p><strong>뿐만 아니라</strong>: 음질이 좋다는 장점에 더하여 가격마저 착하다는 장점을 추가적으로 나열합니다.</p>",
        'correct': "뿐만 아니라",
        'choices': ["뿐만 아니라", "반면에", "데다가", "수록"]
    },
    {
        'text': "<p>A: 요즘 대도시의 주거 환경 문제는 어떤가요?<br>B: 편의 시설은 <u>사방에</u> <u>잘</u> <strong>갖춰진</strong> ________ 녹지 공간이 <u>턱없이</u> 부족해서 <u>가끔</u> 답답함을 느껴요.</p>",
        'explanation': "<p><strong>반면에</strong>: 편의 시설(장점)과 녹지 공간 부족(단점)이라는 상반되는 도시의 두 모습을 대조합니다.</p>",
        'correct': "반면에",
        'choices': ["데다가", "뿐만 아니라", "반면에", "통에"]
    },
    {
        'text': "<p>A: 정우 씨는 회사에서 <u>아주</u> 인정을 많이 받는 분위기예요.<br>B: 맡은 일을 <u>완벽하게</u> <strong>처리할</strong> ________ 대인 관계도 <u>무척</u> 원만해서 동료들에게 인기가 많거든요.</p>",
        'explanation': "<p><strong>뿐만 아니라</strong>: 일 처리가 완벽하다는 사실에 인간관계도 좋다는 장점을 점층적으로 누적하여 표현합니다.</p>",
        'correct': "뿐만 아니라",
        'choices': ["반면에", "뿐만 아니라", "데다가", "뻔하게"]
    },
    {
        'text': "<p>A: 프로젝트 마감일이 내일인데 준비는 다 끝났어요?<br>B: 아니요, 해야 할 과제가 <u>산더미처럼</u> <strong>남은</strong> ________ 컴퓨터까지 <u>갑자기</u> 고장 나서 <u>정말</u> 미치겠어요.</p>",
        'explanation': "<p><strong>데다가</strong>: 일이 많이 남은 부정적 상태에서 컴퓨터 고장이라는 나쁜 일이 엎친 데 덮친 격으로 가중됨을 나타냅니다.</p>",
        'correct': "데다가",
        'choices': ["데다가", "반면에", "뿐만 아니라", "버려서"]
    },
    {
        'text': "<p>A: 유키 씨는 고향에 자주 내려가는 편인가요?<br>B: 고향 집이 <u>너무</u> <strong>먼</strong> ________ 비행기 표값도 <u>지나치게</u> 비싸서 1년에 한 번 가기도 힘들어요.</p>",
        'explanation': "<p><strong>데다가</strong>: 거리가 멀다는 제약 조건에 비용이 비싸다는 부정적 조건이 겹치는 상황의 가중입니다.</p>",
        'correct': "데다가",
        'choices': ["반면에", "데다가", "뿐만 아니라", "것이나 마찬가지로"]
    },
    {
        'text': "<p>A: 백화점 세일 기간이라 사람이 <u>엄청나게</u> 많았겠어요.<br>B: 물건 가격이 <u>대폭</u> <strong>할인된</strong> ________ 구매 고객에게 사은품까지 <u>푸짐하게</u> 줘서 발 디딜 틈이 없었어요.</p>",
        'explanation': "<p><strong>뿐만 아니라</strong>: 가격 할인이라는 혜택에 사은품 증정이라는 또 다른 추가 혜택이 이어짐을 나타냅니다.</p>",
        'correct': "뿐만 아니라",
        'choices': ["뿐만 아니라", "반면에", "데다가", "바람에"]
    },
    {
        'text': "<p>A: 형과 남동생의 성격은 보통 비슷한 편인가요?<br>B: 아니요, 형은 성격이 <u>매우</u> <strong>차분한</strong> ________ 동생은 <u>활달하고</u> <u>성격이 급한</u> 편이라 <u>많이</u> 달라요.</p>",
        'explanation': "<p><strong>반면에</strong>: 차분한 성격과 활달하고 급한 성격이라는 서로 반대되는 특성을 대조하여 설명합니다.</p>",
        'correct': "반면에",
        'choices': ["데다가", "뿐만 아니라", "반면에", "조차"]
    },
    {
        'text': "<p>A: 가을철에는 산불 사고를 <u>특별히</u> 조심해야 해요.<br>B: 맞아요. 가을에는 기후가 <u>무척</u> <strong>건조한</strong> ________ 낙엽이 <u>많이</u> 쌓여 있어서 <u>작은</u> 불씨도 큰 불로 번지기 쉽거든요.</p>",
        'explanation': "<p><strong>데다가</strong>: 건조한 기후 환경에 낙엽이 쌓여 있는 조건이 더해져 위험성이 중첩(가중)됨을 뜻합니다.</p>",
        'correct': "데다가",
        'choices': ["데다가", "반면에", "뿐만 아니라", "일 뻔해서"]
    },
    {
        'text': "<p>A: 이번에 새로 들어온 신입사원은 업무 능력이 어때요?<br>B: 외국어를 <u>유창하게</u> <strong>구사할</strong> ________ 컴퓨터 활용 능력도 <u>상당히</u> 뛰어나서 <u>다들</u> 기대를 많이 하고 있어요.</p>",
        'explanation': "<p><strong>뿐만 아니라</strong>: 외국어 구사 능력이라는 장점에 컴퓨터 능력이라는 또 다른 스펙이 추가되는 점층적 표현입니다.</p>",
        'correct': "뿐만 아니라",
        'choices': ["반면에", "뿐만 아니라", "데다가", "셈치고"]
    },
    {
        'text': "<p>A: 제주도는 사계절 내내 관광객들이 <u>참</u> 많이 찾는 것 같아요.<br>B: 자연경관이 <u>아주</u> <strong>아름다운</strong> ________ 육지보다 교통 요금이 <u>다소</u> 비싸서 여행 비용이 <u>많이</u> 들어요.</p>",
        'explanation': "<p><strong>반면에</strong>: 아름다운 경관(장점)과 비싼 교통 요금(단점)이라는 상반된 사실을 매끄럽게 대조합니다.</p>",
        'correct': "반면에",
        'choices': ["데다가", "반면에", "뿐만 아니라", "통에"]
    },
    {
        'text': "<p>A: 어제 회식 자리에서 술을 <u>너무</u> 많이 마셨나 봐요.<br>B: 네, 속이 <u>정말</u> <u>쓰리고</u> <strong>아픈</strong> ________ 머리까지 <u>깨질 것처럼</u> 지독하게 아파서 타이레놀을 먹었어요.</p>",
        'explanation': "<p><strong>데다가</strong>: 속이 아픈 증상에 두통까지 겹쳐서 숙취의 고통이 가중되고 심해진 상태를 나타냅니다.</p>",
        'correct': "데다가",
        'choices': ["데다가", "반면에", "뿐만 아니라", "나 다름없이"]
    },
    {
        'text': "<p>A: 요즘 집에서 요리해 드시는 분들이 <u>부쩍</u> 줄어든 것 같아요.<br>B: 마트의 식재료 물가가 <u>너무</u> <strong>오른</strong> ________ 1인 가구가 <u>늘어나면서</u> 배달 음식을 시켜 먹는 게 편리하니까요.</p>",
        'explanation': "<p><strong>뿐만 아니라</strong>: 물가 상승이라는 원인과 더불어 1인 가구 증가라는 또 다른 사회적 원인이 누적되어 추가됨을 뜻합니다.</p>",
        'correct': "뿐만 아니라",
        'choices': ["반면에", "뿐만 아니라", "데다가", "것이나 마찬가지라"]
    },
    {
        'text': "<p>A: 진아 씨가 새로 장만한 자동차는 승차감이 어때요?<br>B: 내부 공간이 <u>무척</u> <u>넓고</u> <strong>쾌적한</strong> ________ 연비가 <u>상당히</u> 나쁜 편이라 주유비가 <u>많이</u> 깨져요.</p>",
        'explanation': "<p><strong>반면에</strong>: 넓고 쾌적한 내부(장점)와 나쁜 연비(단점)라는 상반되는 두 가지 사실을 대조합니다.</p>",
        'correct': "반면에",
        'choices': ["데다가", "뿐만 아니라", "반면에", "척하느라고"]
    },
    {
        'text': "<p>A: 이번 기획서 작성이 <u>거의</u> 끝나 가는데 검토 <u>좀</u> 부탁드립니다.<br>B: 아이디어 구성이 <u>매우</u> <strong>독창적인</strong> ________ 통계 자료의 분석도 <u>상당히</u> 정확하게 잘 <u>정리되어</u> 있네요.</p>",
        'explanation': "<p><strong>뿐만 아니라</strong>: 독창적인 아이디어라는 기존의 칭찬 포인트에 통계 분석의 정확성이라는 장점을 하나 더 추가하여 극찬하는 맥락입니다.</p>",
        'correct': "뿐만 아니라",
        'choices': ["뿐만 아니라", "반면에", "데다가", "날 뻔하게"]
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
            title='반면에, 뿐만 아니라, 데다가',  # --- IGNORE ---
            master=master,
            defaults={
                'description': '이 연습문제는 한국어 문법에서 자주 사용되는 연결어미와 표현들을 연습하는 데 도움이 됩니다. 각 문제를 통해 문맥에 맞는 표현을 선택하고, 그 의미와 용법을 이해할 수 있습니다.',
                'subject': subject,
                'level': 'hard',
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

        for i, q in enumerate(questions, start=1):
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
            f"Created practice '{practice.title}' with {len(questions)} questions (id={practice.pk})."
        ))
