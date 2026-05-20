from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
    {
        'text': "<p><strong>A: 이 컴퓨터를 산 지 꽤 오래된 것 같아요.<br>B: 네, 대학교에 ________ 벌써 5년이 넘었네요.</strong></p>",
        'explanation': "<p><strong>입학한 지</strong>: <code>-(으)ㄴ 지</code>는 어떤 일이 일어난 후부터 지금까지 경과한 시간을 나타낼 때 사용합니다.</p>",
        'correct': "입학한 지",
        'choices': ["입학할 때", "입학한 지", "입학하기 전에", "입학하면서"]
    },
    {
        'text': "<p><strong>A: 주말에 보통 뭐 하세요?<br>B: 아내가 거실을 ________ 저는 보통 아이들과 밖에서 뛰어놀아요.</strong></p>",
        'explanation': "<p><strong>청소하는 동안</strong>: <code>-는 동안</code>은 어떤 일이 진행되는 시간을 뜻하며, 두 가지 행동을 서로 다른 사람이 할 때 자연스럽게 쓰입니다.</p>",
        'correct': "청소하는 동안",
        'choices': ["청소하자마자", "청소한 후에", "청소하면서", "청소하는 동안"]
    },
    {
        'text': "<p><strong>A: 민수 씨는 스트레스를 어떻게 풀어요?<br>B: 저는 주로 조용한 음악을 ________ 따뜻한 차를 마셔요.</strong></p>",
        'explanation': "<p><strong>들으면서</strong>: <code>-(으)면서</code>는 한 사람이 두 가지 이상의 동작을 동시에 할 때 사용합니다. '듣다'는 불규칙 동사이므로 '들으면서'가 됩니다.</p>",
        'correct': "들으면서",
        'choices': ["듣기 전에", "듣는 동안", "들으면서", "들은 지"]
    },
    {
        'text': "<p><strong>A: 저기 창문 옆에서 조용히 책을 ________ 사람이 누구인지 알아요?<br>B: 아, 새로 오신 마케팅 팀장님이세요.</strong></p>",
        'explanation': "<p><strong>읽는</strong>: 현재 진행 중인 동작을 명사(사람)와 연결할 때는 동사 현재형 관형사형 어미 <code>-는</code>을 사용합니다.</p>",
        'correct': "읽는",
        'choices': ["읽는", "읽은", "읽을", "읽으면서"]
    },
    {
        'text': "<p><strong>A: 내일 오전에 회의 자료를 보내드릴까요?<br>B: 아니요, 내일 점심 식사를 ________ 회의실에서 같이 확인해 봅시다.</strong></p>",
        'explanation': "<p><strong>마친 후에</strong>: <code>-(으)ㄴ 후에</code>는 앞의 행동이 끝난 다음 다른 행동을 시작함을 나타냅니다.</p>",
        'correct': "마친 후에",
        'choices': ["마치는 동안", "마친 후에", "마치기 전에", "마칠 때"]
    },
    {
        'text': "<p><strong>A: 중요한 발표가 있어서 너무 긴장돼요.<br>B: 무대에 ________ 심호흡을 크게 세 번 해 보세요.</strong></p>",
        'explanation': "<p><strong>올라가기 전에</strong>: <code>-기 전에</code>는 어떤 일이 일어나거나 행동을 하기 앞서 다른 행동을 먼저 함을 나타냅니다.</p>",
        'correct': "올라가기 전에",
        'choices': ["올라간 후에", "올라가자마자", "올라가면서", "올라가기 전에"]
    },
    {
        'text': "<p><strong>A: 언제 가장 고향에 가고 싶어요?<br>B: 타지에서 혼자 갑자기 ________ 가족들이 정말 많이 생각나요.</strong></p>",
        'explanation': "<p><strong>아플 때</strong>: <code>-(으)ㄹ 때</code>는 어떤 상태나 행동이 지속되는 시간이나 경우를 뜻합니다. 형용사 '아프다'에 붙어 상황을 설명합니다.</p>",
        'correct': "아플 때",
        'choices': ["아플 때", "아프기 전에", "아픈 지", "아프면서"]
    },
    {
        'text': "<p><strong>A: 이 서류들은 언제 팀장님께 결재를 올릴까요?<br>B: 내용을 꼼꼼하게 다시 한번 ________ 올리도록 하세요.</strong></p>",
        'explanation': "<p><strong>확인하고 나서</strong>: <code>-고 나서</code>는 한 가지 행동이 완전히 마무리된 후 다음 행동이 이어짐을 강하게 표현할 때 사용합니다.</p>",
        'correct': "확인하고 나서",
        'choices': ["확인하는 동안", "확인하기 전에", "확인하고 나서", "확인할 때"]
    },
    {
        'text': "<p><strong>A: 오늘 퇴근하고 뭐 할 거예요?<br>B: 요새 야근을 많이 해서 너무 피곤해요. 집에 ________ 바로 잘 거예요.</strong></p>",
        'explanation': "<p><strong>도착하자마자</strong>: <code>-자마자</code>는 앞의 동작이 끝나자마자 시간 간격 없이 바로 다음 동작이 이어짐을 나타냅니다.</p>",
        'correct': "도착하자마자",
        'choices': ["도착하기 전에", "도착하자마자", "도착할 때", "도착하는 동안"]
    },
    {
        'text': "<p><strong>A: 내일 소개팅한다면서요? 어떤 사람을 만나고 싶어요?<br>B: 저는 성격이 밝고 마음이 ________ 사람을 만났으면 좋겠어요.</strong></p>",
        'explanation': "<p><strong>따뜻한</strong>: 형용사의 현재 상태를 명사(사람)와 연결할 때는 형용사 관형사형 어미 <code>-(으)ㄴ</code>을 사용합니다.</p>",
        'correct': "따뜻한",
        'choices': ["따뜻할", "따뜻하는", "따뜻하면서", "따뜻한"]
    },
    {
        'text': "<p><strong>A: 두 분이 정말 친해 보이네요. 언제 처음 만나셨어요?<br>B: 우리가 서로 ________ 벌써 10년이 다 되어 가요.</strong></p>",
        'explanation': "<p><strong>알고 지낸 지</strong>: 과거부터 지금까지 이어져 온 시간을 말할 때 <code>-(으)ㄴ 지</code>를 씁니다.</p>",
        'correct': "알고 지낸 지",
        'choices': ["알고 지내기 전에", "알고 지낼 때", "알고 지낸 지", "알고 지내면서"]
    },
    {
        'text': "<p><strong>A: 제가 잠깐 편의점에 다녀올게요.<br>B: 그럼 수진 씨가 편의점에 ________ 제가 여기서 짐을 꼼꼼히 지키고 있을게요.</strong></p>",
        'explanation': "<p><strong>다녀오는 동안</strong>: 두 사람이 각자 다른 행동을 같은 시간대에 하고 있으므로 <code>-는 동안</code>이 가장 적절합니다.</p>",
        'correct': "다녀오는 동안",
        'choices': ["다녀오는 동안", "다녀오면서", "다녀온 후에", "다녀오기 전에"]
    },
    {
        'text': "<p><strong>A: 이번 주말에 친구들하고 파티하기로 했어요.<br>B: 우와, 재밌겠네요! 그럼 파티에서 ________ 옷은 벌써 다 샀어요?</strong></p>",
        'explanation': "<p><strong>입을</strong>: 미래에 발생할 일이나 예정을 명사와 연결할 때는 미래형 관형사형 어미 <code>-(으)ㄹ</code>을 사용합니다.</p>",
        'correct': "입을",
        'choices': ["입는", "입을", "입은", "입자마자"]
    },
    {
        'text': "<p><strong>A: 운전 중에는 휴대폰을 사용하면 안 되는 거 아시죠?<br>B: 죄송합니다. 운전을 ________ 통화하는 게 얼마나 위험한지 깜빡했어요.</strong></p>",
        'explanation': "<p><strong>하면서</strong>: 한 사람이 운전과 통화를 동시에 하는 상황이므로 <code>-(으)면서</code>를 사용해야 합니다.</p>",
        'correct': "하면서",
        'choices': ["하는 동안", "한 후에", "하기 전에", "하면서"]
    },
    {
        'text': "<p><strong>A: 밀린 청소는 다 했어요?<br>B: 네, 방금 다 끝냈어요. 이제 이 드라마를 다 ________ 푹 쉬려고요.</strong></p>",
        'explanation': "<p><strong>보고 나서</strong>: 드라마를 다 보는 행위가 먼저 완전히 끝난 뒤에 쉰다는 의미이므로 <code>-고 나서</code>가 적절합니다.</p>",
        'correct': "보고 나서",
        'choices': ["보고 나서", "보기 전에", "볼 때", "보면서"]
    },
    {
        'text': "<p><strong>A: 어제 지훈 씨가 많이 화가 났나 봐요.<br>B: 네, 제 얼굴을 ________ 아무 말 없이 그냥 밖으로 나가 버렸어요.</strong></p>",
        'explanation': "<p><strong>보자마자</strong>: 얼굴을 본 그 순간 직후에 바로 행동(나감)이 일어났음을 나타내기 위해 <code>-자마자</code>를 씁니다.</p>",
        'correct': "보자마자",
        'choices': ["보기 전에", "보는 동안", "보자마자", "볼 때"]
    },
    {
        'text': "<p><strong>A: 요즘 날씨가 많이 쌀쌀해졌어요. 감기 조심하세요.<br>B: 네, 특히 밤에 창문을 열어 놓고 ________ 찬 바람이 많이 들어오더라고요.</strong></p>",
        'explanation': "<p><strong>잘 때</strong>: 잠을 자고 있는 상태나 그 시간 상황을 묘사하므로 <code>-(으)ㄹ 때</code>를 사용합니다.</p>",
        'correct': "잘 때",
        'choices': ["자기 전에", "잘 때", "잔 후에", "자면서"]
    },
    {
        'text': "<p><strong>A: 이 약은 언제 먹어야 하나요?<br>B: 하루에 세 번, 식사를 ________ 30분 뒤에 드시면 됩니다.</strong></p>",
        'explanation': "<p><strong>하신 후에</strong>: 식사가 끝난 뒤를 의미하므로 동사 과거형 어미인 <code>-(으)ㄴ 후에</code>를 결합해야 합니다.</p>",
        'correct': "하신 후에",
        'choices': ["하시기 전에", "하실 때", "하시는 동안", "하신 후에"]
    },
    {
        'text': "<p><strong>A: 비행기 출발 시간이 언제예요?<br>B: 오후 3시 비행기니까 비행기가 ________ 최소 두 시간 일찍 도착해야 해요.</strong></p>",
        'explanation': "<p><strong>출발하기 전에</strong>: 비행기가 출발하는 시점보다 앞선 시간을 말하므로 <code>-기 전에</code>가 맞습니다.</p>",
        'correct': "출발하기 전에",
        'choices': ["출발하기 전에", "출발한 후에", "출발하자마자", "출발하면서"]
    },
    {
        'text': "<p><strong>A: 아까 회의실 책상에 ________ 서류 못 봤어요?<br>B: 아, 제가 바람에 날아갈까 봐 서랍 안에 잘 정리해 두었어요.</strong></p>",
        'explanation': "<p><strong>놓아둔</strong>: 이미 과거에 놓아둔 상태를 명사와 연결해야 하므로 과거형 관형사형 어미 <code>-(으)ㄴ</code>을 씁니다.</p>",
        'correct': "놓아둔",
        'choices': ["놓아두는", "놓아둘", "놓아둔", "놓아두면서"]
    },
    {
        'text': "<p><strong>A: 피아노를 정말 잘 치시네요! 얼마나 배우셨어요?<br>B: 감사합니다. 하지만 피아노를 ________ 아직 1년밖에 안 됐어요.</strong></p>",
        'explanation': "<p><strong>배운 지</strong>: 배움을 시작한 시점부터 현재까지 흐른 시간을 표현할 때 <code>-(으)ㄴ 지</code>를 사용합니다.</p>",
        'correct': "배운 지",
        'choices': ["배울 때", "배운 지", "배우기 전에", "배우는 동안"]
    },
    {
        'text': "<p><strong>A: 어제 밤에 왜 이렇게 전화를 안 받았어요?<br>B: 정말 미안해요. 제가 따뜻한 물로 샤워를 ________ 휴대폰 벨소리를 못 들었어요.</strong></p>",
        'explanation': "<p><strong>하는 동안</strong>: 샤워가 진행되는 그 시간적 길이 안에서 전화가 왔음을 나타내므로 <code>-는 동안</code>이 자연스럽습니다.</p>",
        'correct': "하는 동안",
        'choices': ["하면서", "한 후에", "하기 전에", "하는 동안"]
    },
    {
        'text': "<p><strong>A: 오늘 아침에 왜 그렇게 급하게 뛰어갔어요?<br>B: 늦잠을 자서 빵을 ________ 정류장까지 정신없이 뛰었거든요.</strong></p>",
        'explanation': "<p><strong>먹으면서</strong>: 빵을 먹는 동작과 뛰는 동작을 주어가 동시에 수행했으므로 <code>-(으)면서</code>를 사용합니다.</p>",
        'correct': "먹으면서",
        'choices': ["먹는 동안", "먹은 후에", "먹으면서", "먹기 전에"]
    },
    {
        'text': "<p><strong>A: 선생님, 이 단어의 뜻을 잘 모르겠어요.<br>B: 사전을 먼저 꼼꼼히 ________ 그래도 모르면 다시 질문하세요.</strong></p>",
        'explanation': "<p><strong>찾아보고 나서</strong>: 사전을 찾는 행위를 완전히 끝맺은 후에 다음 행동을 하라는 의미에서 <code>-고 나서</code>가 자연스럽습니다.</p>",
        'correct': "찾아보고 나서",
        'choices': ["찾아보고 나서", "찾아보기 전에", "찾아볼 때", "찾아보면서"]
    },
    {
        'text': "<p><strong>A: 어제 축구 경기 결과 어떻게 됐어요?<br>B: 전반전이 ________ 비가 갑자기 쏟아져서 경기가 아예 취소됐어요.</strong></p>",
        'explanation': "<p><strong>시작되자마자</strong>: 시작된 바로 그 시점에 비가 왔다는 긴박함을 나타내기 위해 <code>-자마자</code>를 씁니다.</p>",
        'correct': "시작되자마자",
        'choices': ["시작되기 전에", "시작되자마자", "시작되는 동안", "시작될 때"]
    },
    {
        'text': "<p><strong>A: 한국어 문법이 너무 어려워서 포기하고 싶어요.<br>B: 누구나 처음엔 그래요. 너무 ________ 잠시 쉬었다가 다시 해 보세요.</strong></p>",
        'explanation': "<p><strong>힘들 때</strong>: 힘들다고 느끼는 그런 상황이나 시기를 지칭하므로 <code>-(으)ㄹ 때</code>를 결합합니다.</p>",
        'correct': "힘들 때",
        'choices': ["힘들기 전에", "힘든 후에", "힘들면서", "힘들 때"]
    },
    {
        'text': "<p><strong>A: 저희 언제쯤 다시 연락할까요?<br>B: 제가 이번 프로젝트를 무사히 ________ 다시 연락드리겠습니다.</strong></p>",
        'explanation': "<p><strong>끝낸 후에</strong>: 프로젝트 완료라는 선행 동작이 이루어진 뒤를 의미하므로 <code>-(으)ㄴ 후에</code>를 씁니다.</p>",
        'correct': "끝낸 후에",
        'choices': ["끝낸 후에", "끝내기 전에", "끝낼 때", "끝내는 동안"]
    },
    {
        'text': "<p><strong>A: 저기 벤치에서 커피를 조용히 ________ 남자가 제 첫사랑이에요.<br>B: 정말요? 아직도 많이 좋아하시나 봐요.</strong></p>",
        'explanation': "<p><strong>마시는</strong>: 남자가 지금 커피를 마시고 있는 동작을 명사로 수식해야 하므로 현재 관형사형 <code>-는</code>이 들어갑니다.</p>",
        'correct': "마시는",
        'choices': ["마신", "마실", "마시는", "마시면서"]
    },
    {
        'text': "<p><strong>A: 밖에 비가 많이 오는데 우산 챙겼어요?<br>B: 앗, 깜빡할 뻔했네요. 집 밖으로 ________ 꼭 챙길게요.</strong></p>",
        'explanation': "<p><strong>나가기 전에</strong>: 나가는 행동을 하기 앞서 우산을 챙긴다는 의미이므로 <code>-기 전에</code>가 맞습니다.</p>",
        'correct': "나가기 전에",
        'choices': ["나간 후에", "나가기 전에", "나가자마자", "나가면서"]
    },
    {
        'text': "<p><strong>A: 주말에 해외로 여행 가는데 무슨 가방을 가져갈까요?<br>B: 짐이 많으니까 최대한 가볍고 ________ 가방으로 챙기세요.</strong></p>",
        'explanation': "<p><strong>튼튼한</strong>: '튼튼하다'라는 형용사가 명사(가방)의 상태를 설명해야 하므로 관형사형 어미 <code>-(으)ㄴ</code>을 사용합니다.</p>",
        'correct': "튼튼한",
        'choices': ["튼튼할", "튼튼하는", "튼튼하면서", "튼튼한"]
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
            title='Sifatdosh / Hozirgi va oʻtgan zamon aniqlovchilari',  # --- IGNORE ---
            master=master,
            defaults={
                'description': '1. V-(으)ㄴ 후에 (Keyin) 2. V-기 전에 (Oldin) 3. A/V-(으)ㄹ 때 (Paytda / -ganda) 4. A/V-ㄴ/은/는',
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
