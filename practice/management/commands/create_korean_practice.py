from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice
QUESTIONS = [
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>어제 저녁에 불고기를 ___.</strong></p>',
        'hint': '<p>문장에 있는 시간 부사를 잘 확인해 보세요.</p>',
        'explanation': '<p><strong>먹었어요</strong>: "어제"는 지나간 시간을 의미합니다. 따라서 동사도 과거 시제 형태를 사용해야 합니다.</p>',
        'correct': '먹었어요',
        'choices': ['먹어요', '먹을 거예요', '먹었어요', '먹겠어요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>내일은 친구들과 함께 도서관에 ___.</strong></p>',
        'hint': '<p>아직 일어나지 않은 일에 대해 말할 때 쓰는 표현입니다.</p>',
        'explanation': '<p><strong>갈 거예요</strong>: "내일"은 앞으로 다가올 시간입니다. 따라서 미래 시제를 나타내는 표현이 필요합니다.</p>',
        'correct': '갈 거예요',
        'choices': ['갔어요', '가요', '갑니다', '갈 거예요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>민수 씨는 지금 무엇을 ___?</strong></p>',
        'hint': '<p>현재 진행 중이거나 지금 하는 행동을 묻는 질문입니다.</p>',
        'explanation': '<p><strong>합니까</strong>: "지금" 일어나는 일이므로 현재 시제를 씁니다. 정중하게 묻는 의문형입니다.</p>',
        'correct': '합니까',
        'choices': ['합니까', '했습니까', '할 겁니까', '하겠습니까'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>지난 주말에 제주도에 ___?</strong></p>',
        'hint': '<p>이미 끝난 일에 대해 물어볼 때 사용하는 형태를 찾아보세요.</p>',
        'explanation': '<p><strong>갔어요</strong>: "지난 주말"은 과거를 나타냅니다. 따라서 과거 시제 의문형을 사용해야 합니다.</p>',
        'correct': '갔어요',
        'choices': ['가요', '갈 거예요', '갔어요', '갑니다'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>이 일은 제가 먼저 ___.</strong></p>',
        'hint': '<p>말하는 사람의 굳은 의지나 앞으로의 계획을 나타내는 표현입니다.</p>',
        'explanation': '<p><strong>하겠습니다</strong>: "먼저 하겠다"는 화자의 의지를 담은 미래 표현인 "-겠-"을 사용하는 것이 자연스럽습니다.</p>',
        'correct': '하겠습니다',
        'choices': ['했습니다', '합니다', '하겠습니다', '해요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>저는 매일 아침 8시에 학교로 ___.</strong></p>',
        'hint': '<p>반복되는 일상이나 규칙적인 습관을 나타내는 시제를 고르세요.</p>',
        'explanation': '<p><strong>출발합니다</strong>: "매일" 일어나는 규칙적인 일이므로 현재 시제를 사용합니다.</p>',
        'correct': '출발합니다',
        'choices': ['출발했습니다', '출발할 겁니다', '출발합니다', '출발하겠어요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>작년에 처음으로 한국에 ___.</strong></p>',
        'hint': '<p>지나간 연도를 나타내는 단어가 힌트입니다.</p>',
        'explanation': '<p><strong>왔습니다</strong>: "작년"은 과거의 시간이므로, 동사도 과거형을 써야 합니다.</p>',
        'correct': '왔습니다',
        'choices': ['옵니다', '올 겁니다', '왔습니다', '와요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>보통 주말에는 주로 몇 시에 ___?</strong></p>',
        'hint': '<p>평소의 습관이나 패턴을 물어보는 문장입니다.</p>',
        'explanation': '<p><strong>일어나요</strong>: "보통"이라는 단어는 일상적인 패턴을 묻기 때문에 현재 시제가 적절합니다.</p>',
        'correct': '일어나요',
        'choices': ['일어났어요', '일어날 거예요', '일어나요', '일어났습니까'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>어제는 비가 와서 날씨가 많이 ___.</strong></p>',
        'hint': '<p>어제 느꼈던 날씨 상태를 표현하는 형태를 생각해보세요.</p>',
        'explanation': '<p><strong>추웠어요</strong>: "어제"의 상태를 설명하므로 ㅂ 불규칙 형용사의 과거형을 사용합니다.</p>',
        'correct': '추웠어요',
        'choices': ['추워요', '추울 거예요', '추웠어요', '춥습니다'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>이번 여름 방학에는 무엇을 ___?</strong></p>',
        'hint': '<p>앞으로 다가올 시간에 대한 계획을 묻는 질문입니다.</p>',
        'explanation': '<p><strong>할 거예요</strong>: 앞으로 있을 "이번 방학"의 계획을 묻고 있으므로 미래 시제가 필요합니다.</p>',
        'correct': '할 거예요',
        'choices': ['해요', '했어요', '할 거예요', '합니까'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>저는 지금 조용한 음악을 ___.</strong></p>',
        'hint': '<p>현재 하고 있는 행동과 ㄷ 불규칙 활용에 주의하세요.</p>',
        'explanation': '<p><strong>들어요</strong>: "지금" 일어나는 일이므로 현재 시제입니다. 동사 "듣다"는 모음 앞에서 "들-"로 바뀝니다.</p>',
        'correct': '들어요',
        'choices': ['들어요', '들었어요', '들을 거예요', '듣어요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>저는 어렸을 때 부산에서 ___.</strong></p>',
        'hint': '<p>아주 예전의 경험이나 과거의 상태를 말할 때 쓰는 시제입니다.</p>',
        'explanation': '<p><strong>살았습니다</strong>: "어렸을 때"는 과거의 시간입니다. ㄹ 받침 탈락을 주의하여 과거형을 만듭니다.</p>',
        'correct': '살았습니다',
        'choices': ['삽니다', '살았습니다', '살 겁니다', '살아습니다'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>손님, 어떤 음료를 ___?</strong></p>',
        'hint': '<p>상대방의 의사를 정중하게 물어보는 형태입니다.</p>',
        'explanation': '<p><strong>드시겠습니까</strong>: 카페나 식당에서 손님이 앞으로 먹을 것을 물어볼 때 "-겠-"을 사용해 정중하게 묻습니다.</p>',
        'correct': '드시겠습니까',
        'choices': ['먹습니까', '먹었습니까', '드시겠습니까', '드십니다'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>저희 어머니는 지금 부엌에서 요리를 ___.</strong></p>',
        'hint': '<p>눈앞에서 바로 벌어지고 있는 일입니다.</p>',
        'explanation': '<p><strong>해요</strong>: "지금" 이루어지는 동작이므로 현재 시제를 사용합니다.</p>',
        'correct': '해요',
        'choices': ['했어요', '할 거예요', '해요', '하겠어요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>며칠 전에 고향에 있는 가족에게 편지를 ___.</strong></p>',
        'hint': '<p>이미 완료된 행동을 나타내는 동사 형태와 "으" 탈락을 생각하세요.</p>',
        'explanation': '<p><strong>썼어요</strong>: "며칠 전"은 과거입니다. 동사 "쓰다"의 과거형은 "으"가 탈락하여 "썼어요"가 됩니다.</p>',
        'correct': '썼어요',
        'choices': ['써요', '쓸 거예요', '썼어요', '쓰겠어요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>피곤해서 이번 주말에는 집에서 그냥 ___.</strong></p>',
        'hint': '<p>다가오는 주말의 개인적인 계획을 나타냅니다.</p>',
        'explanation': '<p><strong>쉴 거예요</strong>: "이번 주말"의 계획이므로 미래를 표현하는 "-을 거예요"를 사용합니다.</p>',
        'correct': '쉴 거예요',
        'choices': ['쉬어요', '쉬었어요', '쉴 거예요', '쉽니다'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>저는 매운 음식을 아주 ___.</strong></p>',
        'hint': '<p>일반적인 사실이나 개인의 기호를 나타내는 시제입니다.</p>',
        'explanation': '<p><strong>좋아합니다</strong>: 평소의 식성이나 기호를 말할 때는 현재 시제를 사용합니다.</p>',
        'correct': '좋아합니다',
        'choices': ['좋아했습니다', '좋아할 겁니다', '좋아합니다', '좋아하겠어요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>어제 선생님이 내주신 숙제를 다 ___?</strong></p>',
        'hint': '<p>이미 지나간 시간에 완료된 일인지 확인하는 질문입니다.</p>',
        'explanation': '<p><strong>했습니까</strong>: "어제" 내주신 숙제를 완료했는지 묻고 있으므로 과거형 의문문이 맞습니다.</p>',
        'correct': '했습니까',
        'choices': ['합니까', '했습니까', '할 겁니까', '하겠습니까'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>일기예보를 보니 내일은 비가 ___.</strong></p>',
        'hint': '<p>앞으로 일어날 날씨에 대한 예상이나 추측을 고르세요.</p>',
        'explanation': '<p><strong>올 거예요</strong>: "내일"의 날씨를 예상하는 문장이므로 미래형 시제를 사용해야 합니다.</p>',
        'correct': '올 거예요',
        'choices': ['왔어요', '와요', '올 거예요', '옵니다'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>오늘 아침에 빵을 먹고 우유를 ___.</strong></p>',
        'hint': '<p>오늘 아침에 이미 끝난 동작을 나타냅니다.</p>',
        'explanation': '<p><strong>마셨어요</strong>: "오늘 아침"에 이미 일어난 과거의 일이므로 과거형이 필요합니다.</p>',
        'correct': '마셨어요',
        'choices': ['마셔요', '마실 거예요', '마셨어요', '마시겠어요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>집에서 회사까지 시간이 얼마나 ___?</strong></p>',
        'hint': '<p>평소에 시간이 대략 얼마나 소요되는지 묻는 질문입니다.</p>',
        'explanation': '<p><strong>걸려요</strong>: 일반적으로 걸리는 시간을 물어볼 때는 현재 시제를 씁니다.</p>',
        'correct': '걸려요',
        'choices': ['걸렸어요', '걸릴 거예요', '걸려요', '걸겠어요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>어젯밤에 배가 너무 ___.</strong></p>',
        'hint': '<p>어제 느꼈던 통증이나 상태, 그리고 "으" 불규칙을 생각하세요.</p>',
        'explanation': '<p><strong>아팠어요</strong>: "어젯밤"의 상태를 나타내므로 과거형입니다. "아프다"는 과거형으로 "아팠어요"가 됩니다.</p>',
        'correct': '아팠어요',
        'choices': ['아파요', '아플 거예요', '아팠어요', '아프겠어요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>회의가 끝난 후에 다시 ___.</strong></p>',
        'hint': '<p>나중에 하겠다는 약속이나 다짐을 담은 표현입니다.</p>',
        'explanation': '<p><strong>연락하겠습니다</strong>: "끝난 후에" 할 행동, 즉 미래의 다짐과 의지를 나타내므로 "-겠습니다"가 어울립니다.</p>',
        'correct': '연락하겠습니다',
        'choices': ['연락합니다', '연락했습니다', '연락하겠습니다', '연락해요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>저기 창문 밖으로 큰 산이 ___.</strong></p>',
        'hint': '<p>지금 눈에 들어오는 상태를 표현하는 단어입니다.</p>',
        'explanation': '<p><strong>보여요</strong>: "저기"라고 가리키며 현재 눈에 보이는 상태를 말하므로 현재 시제를 씁니다.</p>',
        'correct': '보여요',
        'choices': ['보였어요', '보일 거예요', '보여요', '보겠습니다'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>아까 복도에서 누구하고 ___?</strong></p>',
        'hint': '<p>조금 전(과거)에 했던 행동을 묻는 질문입니다.</p>',
        'explanation': '<p><strong>이야기했어요</strong>: "아까"는 조금 전의 과거를 나타내는 부사이므로, 동사도 과거형을 사용해야 합니다.</p>',
        'correct': '이야기했어요',
        'choices': ['이야기해요', '이야기할 거예요', '이야기했어요', '이야기하겠습니다'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>이따가 저녁으로 무엇을 ___?</strong></p>',
        'hint': '<p>잠시 후에 할 행동이나 계획을 묻고 있습니다.</p>',
        'explanation': '<p><strong>먹을 거예요</strong>: "이따가"는 조금 뒤의 미래를 의미하므로 미래 시제로 묻는 것이 맞습니다.</p>',
        'correct': '먹을 거예요',
        'choices': ['먹어요', '먹었어요', '먹을 거예요', '먹습니다'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>오늘은 바람도 불고 날씨가 아주 ___.</strong></p>',
        'hint': '<p>오늘의 상태를 설명하는 형용사 형태입니다.</p>',
        'explanation': '<p><strong>시원합니다</strong>: "오늘"의 날씨 상태를 묘사하는 문장이므로 현재 시제가 적절합니다.</p>',
        'correct': '시원합니다',
        'choices': ['시원했습니다', '시원할 겁니다', '시원합니다', '시원하겠어요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>파티에서 친구들과 함께 신나게 춤을 ___.</strong></p>',
        'hint': '<p>이미 끝난 행사에 대해 말하는 동사의 형태를 고르세요.</p>',
        'explanation': '<p><strong>췄어요</strong>: 파티에서의 지난 일을 설명하므로 과거형 "추었어요(췄어요)"를 써야 합니다.</p>',
        'correct': '췄어요',
        'choices': ['춰요', '출 거예요', '췄어요', '추겠습니다'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>공항에 도착하면 바로 전화를 ___.</strong></p>',
        'hint': '<p>특정 상황이 벌어진 후에 하겠다는 화자의 의지입니다.</p>',
        'explanation': '<p><strong>하겠습니다</strong>: 미래에 어떤 조건이 충족되었을 때의 행동 의지를 나타내므로 미래/의지 시제가 쓰입니다.</p>',
        'correct': '하겠습니다',
        'choices': ['해요', '했어요', '하겠습니다', '합니다'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>요즘 배우고 있는 한국어 공부가 재미___?</strong></p>',
        'hint': '<p>현재의 느낌이나 상태를 묻는 질문입니다.</p>',
        'explanation': '<p><strong>있습니까</strong>: "요즘" 겪고 있는 감정이나 상태를 묻고 있으므로 현재 시제를 사용해야 합니다.</p>',
        'correct': '있습니까',
        'choices': ['있습니까', '있었습니까', '있을 겁니까', '있겠습니까'],
    }
]
class Command(BaseCommand):
    help = 'Create a Korean grammar particle practice test (Tenses)'

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
            title='한국어 Tenses Practice',
            master=master,
            defaults={
                'description': '한국어의 시제를 연습하는 테스트예요.',
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
            self.stdout.write(self.style.WARNING(
                f"Practice '{practice.title}' already exists (id={practice.pk}). Skipping."
            ))
            return

        for i, q in enumerate(QUESTIONS, start=1):
            question = PracticeQuestion.objects.create(
                practice=practice,
                question_text=q['text'],
                hint=q['hint'],
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
