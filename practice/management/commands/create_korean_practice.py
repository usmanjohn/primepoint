from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
    {
        'text': "<p><strong>A: 손을 언제 씻을까요?<br>B: 맛있는 저녁 식사를 ________ 깨끗하게 비누로 손을 씻으세요.</strong></p>",
        'explanation': "<p><strong>하기 전에</strong>: 어떤 행동을 하기 이전의 상황을 나타낼 때 <code>V-기 전에</code>를 사용합니다. 하다 → 하기 전에 입니다.</p>",
        'correct': "하기 전에",
        'choices': ["한 후에", "하기 전에", "하는 동안", "하자마자"]
    },
    {
        'text': "<p><strong>A: 땀을 너무 많이 흘렸어요.<br>B: 격렬한 운동을 ________ 시원한 얼음물을 마시면 아주 좋습니다.</strong></p>",
        'explanation': "<p><strong>한 후에</strong>: 어떤 행동이 완전히 끝난 다음을 나타낼 때 <code>V-(으)ㄴ 후에</code>를 사용합니다. 하다 → 한 후에 입니다.</p>",
        'correct': "한 후에",
        'choices': ["하기 전에", "하면서", "한 후에", "하는 중"]
    },
    {
        'text': "<p><strong>A: 어려운 숙제를 드디어 다 끝냈어요!<br>B: 숙제를 완벽하게 ________ 재미있는 영화를 보러 갑시다.</strong></p>",
        'explanation': "<p><strong>하고 나서</strong>: 앞선 행동이 완전히 완료되고 나서 다음 행동을 할 때 <code>V-고 나서</code>를 사용합니다. 하다 → 하고 나서 입니다.</p>",
        'correct': "하고 나서",
        'choices': ["하는 중", "하고 나서", "할 때", "하자마자"]
    },
    {
        'text': "<p><strong>A: 주말에 친한 친구와 무엇을 했어요?<br>B: 시내에서 친구를 ________ 분위기 좋은 예쁜 카페에 갔어요.</strong></p>",
        'explanation': "<p><strong>만나서</strong>: 시간의 순서대로 앞의 행동(친구를 만남)이 뒤의 행동(카페에 감)보다 먼저 일어났을 때 <code>V-아/어서</code>를 사용합니다. 만나다 → 만나서 입니다.</p>",
        'correct': "만나서",
        'choices': ["만나는 동안", "만나기 전에", "만나서", "만난 지"]
    },
    {
        'text': "<p><strong>A: 기분이 우울할 때 어떻게 스트레스를 풀어요?<br>B: 마음이 너무 ________ 조용한 클래식 음악을 깊이 들어요.</strong></p>",
        'explanation': "<p><strong>슬플 때</strong>: 어떤 상태나 행동이 일어나는 시점을 나타낼 때 <code>A/V-(으)ㄹ 때</code>를 사용합니다. 슬프다 → 슬플 때 입니다.</p>",
        'correct': "슬플 때",
        'choices': ["슬픈 후에", "슬프면서", "슬프자마자", "슬플 때"]
    },
    {
        'text': "<p><strong>A: 샤워실에서 노래 소리가 크게 들리네요.<br>B: 네, 저는 보통 따뜻한 물로 샤워를 ________ 즐겁게 노래를 불러요.</strong></p>",
        'explanation': "<p><strong>하면서</strong>: 두 가지 행동을 동시에 진행할 때 <code>V-(으)면서</code>를 사용합니다. 하다 → 하면서 입니다.</p>",
        'correct': "하면서",
        'choices': ["하기 전에", "하면서", "하고 나서", "한 지"]
    },
    {
        'text': "<p><strong>A: 사장님과 지금 당장 통화할 수 있을까요?<br>B: 죄송합니다. 사장님께서는 지금 아주 중요한 회의를 ________이십니다.</strong></p>",
        'explanation': "<p><strong>하시는 중</strong>: 어떤 행동이 현재 진행되고 있음을 강조할 때 <code>V-는 중</code>을 사용합니다. 하시다(높임말) → 하시는 중 입니다.</p>",
        'correct': "하시는 중",
        'choices': ["하시는 동안", "하신 지", "하시는 중", "하시자마자"]
    },
    {
        'text': "<p><strong>A: 어제 밤에 일찍 주무셨어요?<br>B: 네, 너무 피곤해서 푹신한 침대에 ________ 깊은 잠에 푹 빠졌어요.</strong></p>",
        'explanation': "<p><strong>눕자마자</strong>: 앞의 행동이 끝나고 아주 짧은 시간 안에 다음 행동이 바로 일어날 때 <code>V-자마자</code>를 사용합니다. 눕다 → 눕자마자 입니다.</p>",
        'correct': "눕자마자",
        'choices': ["누운 후에", "눕기 전에", "누운 지", "눕자마자"]
    },
    {
        'text': "<p><strong>A: 아름다운 제주도 여행은 어땠어요?<br>B: 아쉽게도 제가 제주도를 여행하는 ________ 비가 계속 세차게 내렸어요.</strong></p>",
        'explanation': "<p><strong>동안</strong>: 어떤 행동이나 상태가 계속되는 시간을 나타낼 때 <code>N 동안 / V-는 동안</code>을 사용합니다. 여행하는 → 여행하는 동안 입니다.</p>",
        'correct': "동안",
        'choices': ["후에", "동안", "전에", "때"]
    },
    {
        'text': "<p><strong>A: 한국어를 정말 유창하게 잘하시네요!<br>B: 감사합니다. 복잡한 한국어 문법을 처음 ________ 벌써 5년이 훌쩍 넘었어요.</strong></p>",
        'explanation': "<p><strong>배운 지</strong>: 어떤 행동을 한 후부터 지금까지의 시간을 나타낼 때 <code>V-(으)ㄴ 지</code>를 사용합니다. 배우다 → 배운 지 입니다.</p>",
        'correct': "배운 지",
        'choices': ["배우기 전에", "배우면서", "배운 지", "배운 후에"]
    },
    {
        'text': "<p><strong>A: 비행기 타러 가기 전에 뭐 확인해야 해요?<br>B: 먼 여행을 ________ 반드시 여권을 꼼꼼하게 확인해야 합니다.</strong></p>",
        'explanation': "<p><strong>출발하기 전에</strong>: 어떤 행동 이전의 시점을 나타낼 때 <code>V-기 전에</code>를 사용합니다. 출발하다 → 출발하기 전에 입니다.</p>",
        'correct': "출발하기 전에",
        'choices': ["출발한 후에", "출발하자마자", "출발하기 전에", "출발하는 동안"]
    },
    {
        'text': "<p><strong>A: 매운 떡볶이를 먹은 다음에는 뭘 먹을까요?<br>B: 아주 매운 음식을 ________ 달콤하고 시원한 아이스크림을 먹으면 최고예요.</strong></p>",
        'explanation': "<p><strong>먹은 후에</strong>: 한 행동이 끝난 이후를 나타낼 때 <code>V-(으)ㄴ 후에</code>를 사용합니다. 먹다 → 먹은 후에 입니다.</p>",
        'correct': "먹은 후에",
        'choices': ["먹으면서", "먹기 전에", "먹을 때", "먹은 후에"]
    },
    {
        'text': "<p><strong>A: 밖에서 신나게 뛰어놀았어요!<br>B: 더러운 흙바닥에서 놀고 집에 ________ 꼭 비누로 깨끗이 손을 씻으렴.</strong></p>",
        'explanation': "<p><strong>들어오고 나서</strong>: 앞선 행동을 완전히 마치고 나서 다음 행동을 할 때 <code>V-고 나서</code>를 사용합니다. 들어오다 → 들어오고 나서 입니다.</p>",
        'correct': "들어오고 나서",
        'choices': ["들어오기 전에", "들어오고 나서", "들어오는 중", "들어온 지"]
    },
    {
        'text': "<p><strong>A: 오늘 저녁 메뉴는 뭐예요?<br>B: 가까운 시장에 가서 신선한 채소를 ________ 맛있는 김치찌개를 펄펄 끓일 거예요.</strong></p>",
        'explanation': "<p><strong>사서</strong>: 시간의 흐름에 따라 첫 번째 행동(채소를 삼)이 일어나고 그 다음 행동(찌개를 끓임)이 이어질 때 <code>V-아/어서</code>를 사용합니다. 사다 → 사서 입니다.</p>",
        'correct': "사서",
        'choices': ["사는 동안", "산 지", "사서", "사자마자"]
    },
    {
        'text': "<p><strong>A: 언제 가장 기분이 좋고 행복해요?<br>B: 전혀 예상하지 못한 깜짝 선물을 ________ 정말 세상을 다 가진 것처럼 행복해요.</strong></p>",
        'explanation': "<p><strong>받을 때</strong>: 어떤 일이 일어나는 바로 그 시점을 나타낼 때 <code>V-(으)ㄹ 때</code>를 사용합니다. 받다 → 받을 때 입니다.</p>",
        'correct': "받을 때",
        'choices': ["받은 지", "받을 때", "받기 전에", "받는 중"]
    },
    {
        'text': "<p><strong>A: 눈이 왜 그렇게 심하게 빨개요?<br>B: 어제 밤에 너무 슬픈 로맨스 영화를 ________ 눈물을 펑펑 흘렸어요.</strong></p>",
        'explanation': "<p><strong>보면서</strong>: 영화를 보는 행동과 우는 행동이 동시에 일어날 때 <code>V-(으)면서</code>를 사용합니다. 보다 → 보면서 입니다.</p>",
        'correct': "보면서",
        'choices': ["본 후에", "보기 전에", "보면서", "보자마자"]
    },
    {
        'text': "<p><strong>A: 요즘 어떻게 바쁘게 지내세요?<br>B: 다음 달에 있을 아주 어려운 한국어 능력 시험을 열심히 ________입니다.</strong></p>",
        'explanation': "<p><strong>준비하는 중</strong>: 현재 활발히 진행 중인 동작을 나타낼 때 <code>V-는 중</code>을 사용합니다. 준비하다 → 준비하는 중 입니다.</p>",
        'correct': "준비하는 중",
        'choices': ["준비하기 전에", "준비한 지", "준비하자마자", "준비하는 중"]
    },
    {
        'text': "<p><strong>A: 상쾌한 아침에 일어나면 제일 먼저 무엇을 하세요?<br>B: 저는 맑은 아침에 눈을 ________ 신선한 공기로 환기를 위해 창문을 활짝 엽니다.</strong></p>",
        'explanation': "<p><strong>뜨자마자</strong>: 앞 행동이 끝나고 지체 없이 바로 다음 행동을 할 때 <code>V-자마자</code>를 사용합니다. 뜨다 → 뜨자마자 입니다.</p>",
        'correct': "뜨자마자",
        'choices': ["뜬 후에", "뜨자마자", "뜨는 동안", "뜨기 전에"]
    },
    {
        'text': "<p><strong>A: 백화점에서 저를 오래 기다리셨어요?<br>B: 아니요, 친구가 예쁜 옷을 신중하게 고르는 ________ 저는 편안한 소파에 앉아서 흥미로운 책을 읽었어요.</strong></p>",
        'explanation': "<p><strong>동안</strong>: 행동이나 상태가 시작되어 끝날 때까지의 시간을 나타낼 때 <code>V-는 동안</code>을 사용합니다. 고르다 → 고르는 동안 입니다.</p>",
        'correct': "동안",
        'choices': ["후에", "전에", "동안", "때"]
    },
    {
        'text': "<p><strong>A: 이 한적한 동네에 언제 이사 오셨어요?<br>B: 시끄러운 복잡한 도시를 떠나 평화롭고 조용한 시골로 ________ 벌써 세 달이 빠르게 지났습니다.</strong></p>",
        'explanation': "<p><strong>이사 온 지</strong>: 이사를 한 시점부터 지금까지의 경과 시간을 나타낼 때 <code>V-(으)ㄴ 지</code>를 사용합니다. 이사 오다 → 이사 온 지 입니다.</p>",
        'correct': "이사 온 지",
        'choices': ["이사 오기 전에", "이사 오면서", "이사 온 후에", "이사 온 지"]
    },
    {
        'text': "<p><strong>A: 밖이 추운데 갑자기 뛰면 다칠 수 있어요.<br>B: 네, 맞아요. 무리하게 ________ 꼼꼼하게 전신 스트레칭을 꼭 해야 해요.</strong></p>",
        'explanation': "<p><strong>달리기 전에</strong>: 어떤 행동 이전의 시간을 나타낼 때 <code>V-기 전에</code>를 사용합니다. 달리다 → 달리기 전에 입니다.</p>",
        'correct': "달리기 전에",
        'choices': ["달린 후에", "달리기 전에", "달리는 중", "달리자마자"]
    },
    {
        'text': "<p><strong>A: 아까 달콤한 초콜릿 케이크를 잔뜩 먹었어요.<br>B: 단 것을 많이 ________ 충치가 생기지 않게 구석구석 양치질을 깨끗이 하세요.</strong></p>",
        'explanation': "<p><strong>먹은 후에</strong>: 식사가 끝난 이후의 상황을 나타낼 때 <code>V-(으)ㄴ 후에</code>를 사용합니다. 먹다 → 먹은 후에 입니다.</p>",
        'correct': "먹은 후에",
        'choices': ["먹으면서", "먹기 전에", "먹은 후에", "먹자마자"]
    },
    {
        'text': "<p><strong>A: 오늘 하루도 정말 수고 많으셨습니다.<br>B: 고된 하루 업무를 모두 완벽하게 ________ 시원하고 차가운 맥주를 한잔 마시고 싶네요.</strong></p>",
        'explanation': "<p><strong>마치고 나서</strong>: 어떤 일을 끝마친 다음 순서로 이어질 때 <code>V-고 나서</code>를 사용합니다. 마치다 → 마치고 나서 입니다.</p>",
        'correct': "마치고 나서",
        'choices': ["마치는 동안", "마치기 전에", "마친 지", "마치고 나서"]
    },
    {
        'text': "<p><strong>A: 라면을 어떻게 끓여야 쫄깃하고 맛있나요?<br>B: 먼저 냄비에 물을 팔팔 ________ 맛있는 라면 면발과 매콤한 스프를 한 번에 넣으세요.</strong></p>",
        'explanation': "<p><strong>끓여서</strong>: 물을 끓이는 선행 동작이 있어야 라면을 넣을 수 있으므로 시간적 순서를 나타내는 <code>V-아/어서</code>를 사용합니다. 끓이다 → 끓여서 입니다.</p>",
        'correct': "끓여서",
        'choices': ["끓인 지", "끓일 때", "끓여서", "끓이는 중"]
    },
    {
        'text': "<p><strong>A: 내일 날씨가 영하로 떨어지고 아주 춥대요.<br>B: 네, 하얀 눈이 펑펑 ________ 아주 따뜻하고 푹신한 두꺼운 외투를 꼭 챙겨 입어야 해요.</strong></p>",
        'explanation': "<p><strong>내릴 때</strong>: 눈이 내리는 특정 시간이나 상황을 나타낼 때 <code>V-(으)ㄹ 때</code>를 사용합니다. 내리다 → 내릴 때 입니다.</p>",
        'correct': "내릴 때",
        'choices': ["내리면서", "내리기 전에", "내릴 때", "내린 지"]
    },
    {
        'text': "<p><strong>A: 주말에 보통 연인과 무엇을 하면서 시간을 보내세요?<br>B: 우리는 꽃이 피어있는 조용한 공원을 다정하게 산책________ 무척 즐거운 대화를 나눕니다.</strong></p>",
        'explanation': "<p><strong>하면서</strong>: 산책하는 것과 대화하는 두 가지 동작이 동시에 일어날 때 <code>V-(으)면서</code>를 사용합니다. 하다 → 하면서 입니다.</p>",
        'correct': "하면서",
        'choices': ["하자마자", "한 후에", "하면서", "하기 전에"]
    },
    {
        'text': "<p><strong>A: 제 컴퓨터가 오늘따라 왜 이렇게 답답하게 느려요?<br>B: 지금 새롭고 무거운 프로그램을 시스템에 계속 복잡하게 설치하________이라서 그렇습니다.</strong></p>",
        'explanation': "<p><strong>는 중</strong>: 설치 작업이 현재 끝나지 않고 계속 진행되고 있을 때 <code>V-는 중</code>을 사용합니다. 설치하다 → 설치하는 중 입니다.</p>",
        'correct': "는 중",
        'choices': ["는 동안", "는 중", "기 전에", "자마자"]
    },
    {
        'text': "<p><strong>A: 비가 오는데 우산을 안 가져오셨네요?<br>B: 네, 하늘이 화창했는데 현관문을 열고 집 밖으로 ________ 갑자기 무서운 소나기가 마구 쏟아졌어요.</strong></p>",
        'explanation': "<p><strong>나가자마자</strong>: 집 밖으로 나간 직후에 바로 비가 왔음을 나타낼 때 <code>V-자마자</code>를 사용합니다. 나가다 → 나가자마자 입니다.</p>",
        'correct': "나가자마자",
        'choices': ["나간 지", "나가는 동안", "나가자마자", "나간 후에"]
    },
    {
        'text': "<p><strong>A: 좁은 베란다에 있는 초록색 식물들이 정말 아름답고 싱싱하네요!<br>B: 네, 제가 무려 한 달 ________ 매일매일 정성스럽게 물을 주고 예쁘게 가꿨거든요.</strong></p>",
        'explanation': "<p><strong>동안</strong>: 한 달이라는 명사 뒤에 붙어서 계속된 시간의 길이를 나타낼 때 <code>N 동안</code>을 사용합니다. 한 달 → 한 달 동안 입니다.</p>",
        'correct': "동안",
        'choices': ["후에", "전에", "동안", "때"]
    },
    {
        'text': "<p><strong>A: 두 분은 언제 이렇게 예쁜 결혼식장에서 결혼하셨어요?<br>B: 아름답고 사랑스러운 아내와 행복한 결혼식을 ________ 벌써 10년이라는 긴 시간이 훌쩍 넘었네요.</strong></p>",
        'explanation': "<p><strong>올린 지</strong>: 결혼식을 올린 과거의 시점부터 현재까지 얼마나 시간이 흘렀는지 나타낼 때 <code>V-(으)ㄴ 지</code>를 사용합니다. 올리다 → 올린 지 입니다.</p>",
        'correct': "올린 지",
        'choices': ["올리기 전에", "올리면서", "올린 지", "올린 후에"]
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
            title='12-dars: Vaqt ifodalari',  # --- IGNORE ---
            master=master,
            defaults={
                'description': 'Vaqt ifodalarini o\'rganish uchun amaliy test.',
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
