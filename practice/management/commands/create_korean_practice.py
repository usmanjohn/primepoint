from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice


QUESTIONS = [
    {
        'text': "<p><strong>A: 마크 씨, 지금 바쁘세요?<br>B: 네, 중요한 보고서를 ________ 조금만 기다려 주세요.</strong></p>",
        'explanation': "<p><strong>작성하고 있어요</strong>: 현재 행동이 계속 진행 중임을 강조하는 진행 시제(<code>-고 있다</code>)가 가장 자연스럽습니다.</p>",
        'correct': "작성하고 있어요",
        'choices': ["작성했었어요", "작성할 거예요", "작성하고 있어요", "작성합니다"]
    },
    {
        'text': "<p><strong>A: 와, 오늘 하늘이 정말 맑고 예쁘네요!<br>B: 네, 바람도 시원하고 날씨가 무척 ________.</strong></p>",
        'explanation': "<p><strong>좋습니다</strong>: 현재의 상태를 공식적이거나 정중하게 표현할 때 격식체인 <code>-(스)ㅂ니다</code>를 사용합니다.</p>",
        'correct': "좋습니다",
        'choices': ["좋았습니다", "좋을 거예요", "좋고 있었어요", "좋습니다"]
    },
    {
        'text': "<p><strong>A: 리사 씨는 예전에도 머리가 짧았어요?<br>B: 아니요, 고등학생 때는 머리가 아주 ________. 지금은 단발머리지만요.</strong></p>",
        'explanation': "<p><strong>길었었어요</strong>: 과거에는 그랬지만 현재는 그렇지 않은 단절된 과거 상태를 나타내므로 과거 완료 시제(<code>-았었었어요</code>)가 올바릅니다.</p>",
        'correct': "길었었어요",
        'choices': ["길어요", "길고 있어요", "길었었어요", "길 거예요"]
    },
    {
        'text': "<p><strong>A: 이번 주말에 특별한 계획이 있으신가요?<br>B: 네, 가족들과 함께 제주도로 여행을 ________. 항공권도 벌써 예매했어요.</strong></p>",
        'explanation': "<p><strong>갈 거예요</strong>: 미래의 확실한 계획이나 예정된 일정을 나타낼 때는 미래 시제(<code>-(으)ㄹ 거예요</code>)를 씁니다.</p>",
        'correct': "갈 거예요",
        'choices': ["갑니다", "갔었어요", "갈 거예요", "가고 있어요"]
    },
    {
        'text': "<p><strong>A: 어제 퇴근하고 뭐 하셨어요?<br>B: 너무 피곤해서 집에 오자마자 바로 ________.</strong></p>",
        'explanation': "<p><strong>잤어요</strong>: '어제' 일어난 과거의 완료된 행동을 나타내므로 일반 과거 시제(<code>-았/었어요</code>)가 정답입니다.</p>",
        'correct': "잤어요",
        'choices': ["자요", "잤어요", "잘 거예요", "자고 있어요"]
    },
    {
        'text': "<p><strong>A: 안바르 씨, 혹시 지금 음악을 ________?<br>B: 아, 죄소합니다. 소리가 너무 컸나요? 바로 줄일게요.</strong></p>",
        'explanation': "<p><strong>듣고 있어요</strong>: 대화 시점에 상대방이 행동을 실시간으로 진행 중인지 묻고 있으므로 진행 시제(<code>-고 있다</code>)를 사용합니다.</p>",
        'correct': "듣고 있어요",
        'choices': ["들었어요", "듣겠습니다", "듣고 있어요", "들었었어요"]
    },
    {
        'text': "<p><strong>A: 새로 개봉한 영화 봤어요?<br>B: 아니요, 아직 안 봤어요. 오늘 퇴근한 후에 극장에 ________.</strong></p>",
        'explanation': "<p><strong>갈 거예요</strong>: 오늘 퇴근 후라는 미래의 행동 계획을 이야기하고 있으므로 미래 시제(<code>-(으)ㄹ 거예요</code>)가 적절합니다.</p>",
        'correct': "갈 거예요",
        'choices': ["갔었어요", "갔었어요", "갈 거예요", "가고 있어요"]
    },
    {
        'text': "<p><strong>A: 흐엉 씨는 매운 음식을 잘 먹어요?<br>B: 고향에 있을 때는 잘 ________, 한국에 온 뒤로는 전혀 못 먹어요.</strong></p>",
        'explanation': "<p><strong>먹었었어요</strong>: 과거에는 잘 먹었으나 현재는 못 먹는, 현재와 상반되는 과거의 사실을 강조하기 위해 uzoq o'tgan zamon(<code>-았었었어요</code>)을 씁니다.</p>",
        'correct': "먹었었어요",
        'choices': ["먹어요", "먹을 거예요", "먹고 있어요", "먹었었어요"]
    },
    {
        'text': "<p><strong>A: 안드레이 씨, 주말에 보통 뭐 해요?<br>B: 저는 일요일마다 집 근처 공원에서 자전거를 ________.</strong></p>",
        'explanation': "<p><strong>타요</strong>: 반복적인 습관이나 일상적인 행동을 친근하고 공손하게 말할 때는 현재 시제 해요체(<code>-아/어요</code>)가 가장 자연스럽습니다.</p>",
        'correct': "타요",
        'choices': ["탔어요", "타요", "탔었어요", "탈 거예요"]
    },
    {
        'text': "<p><strong>A: 안녕하십니까? 처음 뵙겠습니다.<br>B: 반갑습니다. 저는 우즈베키스탄에서 온 아지즈라고 ________.</strong></p>",
        'explanation': "<p><strong>합니다</strong>: 처음 만난 사람에게 정중하게 자기소개를 하는 비즈니스/격식 상황이므로 격식체 현재형(<code>-(스)ㅂ니다</code>)이 맞습니다.</p>",
        'correct': "합니다",
        'choices': ["해요", "합니다", "했었습니다", "할 거예요"]
    },
    {
        'text': "<p><strong>A: 밖에 비가 많이 와요?<br>B: 아니요, 지금은 비가 그치고 시원한 바람이 ________.</strong></p>",
        'explanation': "<p><strong>불어요</strong>: 현재의 날씨 상태를 자연스럽게 묘사하는 아/어요 형이 들어가야 합니다.</p>",
        'correct': "불어요",
        'choices': ["불었어요", "불었었어요", "불 거예요", "불어요"]
    },
    {
        'text': "<p><strong>A: 소라 씨, 아까 낮에 전화했는데 왜 안 받았어요?<br>B: 미안해요, 그때 마침 헬스장에서 운동을 ________.</strong></p>",
        'explanation': "<p><strong>하고 있었어요</strong>: 과거의 특정 시점('아까 낮에')에 행동이 진행 중이었음을 나타내므로 과거 진행형(<code>-고 있었다</code>)을 사용합니다.</p>",
        'correct': "하고 있었어요",
        'choices': ["해요", "하고 있었어요", "할 거예요", "했었어요"]
    },
    {
        'text': "<p><strong>A: 이번 방학에 고향에 내려가실 건가요?<br>B: 네, 방학이 시작되자마자 부모님을 뵈러 고향에 ________.</strong></p>",
        'explanation': "<p><strong>갈 거예요</strong>: 미래의 확고한 개인적 예정이나 의지를 표현하는 Kelasi zamon shakli(<code>-(으)ㄹ 거예요</code>)가 적절합니다.</p>",
        'correct': "갈 거예요",
        'choices': ["갔어요", "갈 거예요", "갔었어요", "가고 있어요"]
    },
    {
        'text': "<p><strong>A: 자밀 씨, 담배 피우세요?<br>B: 아니요, 몇 년 전에는 많이 ________ 지금은 완전히 끊었어요.</strong></p>",
        'explanation': "<p><strong>피웠었어요</strong>: '지금은 완전히 끊었다'는 사실로 보아 과거의 행동이 현재와 완전히 단절되었음을 알 수 있으므로 <code>-았었었어요</code>가 가장 적절합니다.</p>",
        'correct': "피웠었어요",
        'choices': ["피워요", "피우고 있어요", "피웠었어요", "피울 거예요"]
    },
    {
        'text': "<p><strong>A: 지금 시장에 같이 갈래요?<br>B: 죄송해요. 저는 지금 저녁을 ________ 시장에 갈 시간이 없어요.</strong></p>",
        'explanation': "<p><strong>만들고 있어서</strong>: 현재 요리를 하는 중(진행)이라는 이유를 대야 하므로 진행 시제(<code>-고 있다</code>)의 변형이 알맞습니다.</p>",
        'correct': "만들고 있어서",
        'choices': ["만들어서", "만들었어서", "만들고 있어서", "만들 거라서"]
    },
    {
        'text': "<p><strong>A: 우즈베키스탄 날씨는 보통 어때요?<br>B: 여름에는 아주 무덥고 겨울에는 눈이 많이 ________.</strong></p>",
        'explanation': "<p><strong>내립니다</strong>: 일반적인 자연 현상이나 사실을 정중하고 격식 있게 설명할 때 격식체 현재형(<code>-(스)ㅂ니다</code>)을 사용합니다.</p>",
        'correct': "내립니다",
        'choices': ["내렸습니다", "내리겠습니다", "내립니다", "내리고 있었습니다"]
    },
    {
        'text': "<p><strong>A: 수진 씨, 얼굴색이 안 좋네요. 어디 아파요?<br>B: 네, 어제 밤부터 배가 너무 ________.</strong></p>",
        'explanation': "<p><strong>아파요</strong>: '어제 밤부터 시작해서 지금까지 계속 아픈 현재 상태'를 친근하게 나타내므로 현재형 해요체가 알맞습니다.</p>",
        'correct': "아파요",
        'choices': ["아팠었어요", "아파요", "아플 거예요", "아프고 있었어요"]
    },
    {
        'text': "<p><strong>A: 민우 씨, 아까 동방신기 노래 부르던데 팬이에요?<br>B: 중학생 때는 정말 많이 ________, 지금은 다른 가수를 더 좋아해요.</strong></p>",
        'explanation': "<p><strong>좋아했었어요</strong>: 과거(중학생 때)의 취향이 현재에는 완전히 바뀌었음을 나타내는 과거 완료 문맥입니다.</p>",
        'correct': "좋아했었어요",
        'choices': ["좋아해요", "좋아하고 있어요", "좋아할 거예요", "좋아했었어요"]
    },
    {
        'text': "<p><strong>A: 내일 백화점 세일 마지막 날이래요.<br>B: 그래요? 그럼 내일 사람이 아주 ________. 일찍 가야겠어요.</strong></p>",
        'explanation': "<p><strong>많을 거예요</strong>: 미래 상황에 대한 추측(Mire taxmini)을 나타낼 때는 형용사 뒤에 <code>-(으)ㄹ 거예요</code>를 씁니다.</p>",
        'correct': "많을 거예요",
        'choices': ["많아요", "많았습니다", "많을 거예요", "많고 있어요"]
    },
    {
        'text': "<p><strong>A: 지난주 토요일에 왜 동호회 모임에 안 왔어요?<br>B: 회사에 급한 일이 생겨서 주말에도 출근을 ________.</strong></p>",
        'explanation': "<p><strong>했어요</strong>: 이미 지난주에 완료된 객관적 사실을 말하므로 일반 과거 시제(<code>-았/었어요</code>)가 정답입니다.</p>",
        'correct': "했어요",
        'choices': ["해요", "했어요", "할 거예요", "하고 있어요"]
    },
    {
        'text': "<p><strong>A: 영민 씨, 지금 어디예요? 약속 시간이 지났어요.<br>B: 정말 미안해요! 지금 지하철을 ________ 조금만 더 기다려 주세요.</strong></p>",
        'explanation': "<p><strong>타고 있어요</strong>: 실시간 이동 중인 상태를 명확하게 전달하기 위해 현재 진행형(<code>-고 있다</code>)을 사용합니다.</p>",
        'correct': "타고 있어요",
        'choices': ["탔어요", "탔었어요", "탈 거예요", "타고 있어요"]
    },
    {
        'text': "<p><strong>A: 켈리 씨, 한국어 실력이 정말 유창하시네요!<br>B: 아닙니다. 아직 많이 ________. 더 열심히 노력하겠습니다.</strong></p>",
        'explanation': "<p><strong>부족합니다</strong>: 칭찬에 겸손하게 답하며 격식 있는 대화 자리이므로 격식체 현재형(<code>-습니다</code>)이 완벽합니다.</p>",
        'correct': "부족합니다",
        'choices': ["부족했습니다", "부족합니다", "부족할 거예요", "부족했었습니다"]
    },
    {
        'text': "<p><strong>A: 이 옷 예전에는 자주 입더니 요즘은 왜 안 입어요?<br>B: 살이 많이 쪄서 이제는 이 옷이 너무 ________.</strong></p>",
        'explanation': "<p><strong>작아요</strong>: 현재 몸에 맞지 않는 옷의 상태(현재 사실)를 묘사하므로 해요체 현재 시제가 옵니다.</p>",
        'correct': "작아요",
        'choices': ["작았어요", "작아요", "작을 거예요", "작았었어요"]
    },
    {
        'text': "<p><strong>A: 내일 오후에 날씨가 흐리다고 하네요.<br>B: 그래요? 그럼 우산을 꼭 ________ 나가야겠네요.</strong></p>",
        'explanation': "<p><strong>챙겨서</strong>: '내일'이라는 미래 예측 하에 행동을 전제하므로 기본 연결어미가 오지만, 전체 맥락은 미래의 상황에 대처하는 문맥입니다. 여기서는 문맥상 단순 동사 연결어미 형태로 보이지만 보기가 시제를 묻는다면 챙길 거예요 와 연관됩니다. (시제 변형 지문으로 대체 가능: '내일 우산을 ________.' -> 챙길 거예요)</p>",
        'correct': "챙길 거예요",
        'choices': ["챙겼어요", "챙기고 있어요", "챙길 거예요", "챙겼었어요"]
    },
    {
        'text': "<p><strong>A: 옛날에 이 공원에 자주 왔었어요?<br>B: 네, 10년 전에는 매일 여기서 운동을 ________, 지금은 멀리 이사해서 안 와요.</strong></p>",
        'explanation': "<p><strong>했었어요</strong>: 10년 전이라는 먼 과거의 단절된 습관적 행동을 강조하기 때문에 uzoq o'tgan zamon(<code>-았었었어요</code>)이 정답입니다.</p>",
        'correct': "했었어요",
        'choices': ["해요", "하고 있어요", "했었어요", "할 거예요"]
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
            title='1-dars: Zamonlar',  # --- IGNORE ---
            master=master,
            defaults={
                'description': 'Koreys tili - 1 dars: Zamonlar va ularning aniqlovchilari bilan bogʻliq savollar toʻplami.',
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
