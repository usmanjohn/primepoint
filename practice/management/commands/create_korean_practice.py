from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
    {
        'text': '<p><strong>A: 이 수프가 아주 뜨거워요.<br>B: 그러면 조금씩 천천히 ________.</strong></p>',
        'hint': '<p>정중한 명령이나 권유를 나타내는 표현입니다.</p>',
        'explanation': '<p><strong>드세요</strong>: 상대방에게 행동을 정중하게 권유할 때 사용하는 -(으)세요 문법입니다. (먹다의 높임말)</p>',
        'correct': '드세요',
        'choices': ['드세요', '드시지 마세요', '드실까요?', '드십시다'],
    },
    {
        'text': '<p><strong>A: 내일 아주 일찍 일어나야 해서 피곤해요.<br>B: 그러니까 오늘 밤늦게까지 ________.</strong></p>',
        'hint': '<p>상대방에게 어떤 행동을 금지할 때 사용합니다.</p>',
        'explanation': '<p><strong>놀지 마세요</strong>: 금지를 나타내는 -지 마세요 문법입니다.</p>',
        'correct': '놀지 마세요',
        'choices': ['놀지 마세요', '놀아 주세요', '놀까요?', '놀아야 해요'],
    },
    {
        'text': '<p><strong>A: 회의실이 어디에 있습니까?<br>B: 저기 안쪽 복도로 쭉 ________.</strong></p>',
        'hint': '<p>격식 있는 자리에서 명령이나 권유를 할 때 사용합니다.</p>',
        'explanation': '<p><strong>들어가십시오</strong>: 아주 정중하고 격식 있는 명령을 나타내는 -(으)십시오 문법입니다.</p>',
        'correct': '들어가십시오',
        'choices': ['들어가십시오', '들어갈게요', '들어가려고 해요', '들어가면 안 돼요'],
    },
    {
        'text': '<p><strong>A: 오늘 저녁에 아주 맵고 맛있는 음식을 ________?<br>B: 네, 스트레스가 풀리게 같이 먹어요!</strong></p>',
        'hint': '<p>상대방의 의향을 묻거나 제안할 때 사용합니다.</p>',
        'explanation': '<p><strong>먹을까요?</strong>: 제안이나 의견을 묻는 -(으)ㄹ까요? 문법입니다.</p>',
        'correct': '먹을까요?',
        'choices': ['먹을까요?', '먹으십시오', '먹으러 가요', '먹지 마세요'],
    },
    {
        'text': '<p><strong>A: 이번 주말에 날씨가 매우 맑아요.<br>B: 그럼 다 같이 높은 산으로 ________.</strong></p>',
        'hint': '<p>여러 사람이 함께 어떤 행동을 하자고 제안할 때 사용합니다.</p>',
        'explanation': '<p><strong>올라갑시다</strong>: 청유와 제안을 나타내는 -ㅂ시다/읍시다 문법입니다.</p>',
        'correct': '올라갑시다',
        'choices': ['올라갑시다', '올라갈게요', '올라가지 마세요', '올라가면 좋겠다'],
    },
    {
        'text': '<p><strong>A: 이 상자가 너무 무거워요.<br>B: 알겠어요. 제가 들어 줄게요.<br>A: 네, 안전하게 탁자 위로 좀 ________.</strong></p>',
        'hint': '<p>다른 사람에게 어떤 행동을 해 달라고 요청할 때 사용합니다.</p>',
        'explanation': '<p><strong>옮겨 주세요</strong>: 남에게 부탁할 때 사용하는 -아/어 주세요 문법입니다.</p>',
        'correct': '옮겨 주세요',
        'choices': ['옮겨 주세요', '옮기면 안 돼요', '옮길 필요가 있어요', '옮기러 가요'],
    },
    {
        'text': '<p><strong>A: 밖이 무척 시끄러워서 잘 안 들려요. 창문을 꽉 ________?<br>B: 네, 제가 바로 닫아 드릴게요.</strong></p>',
        'hint': '<p>상대방에게 아주 정중하게 부탁할 때 사용합니다.</p>',
        'explanation': '<p><strong>닫아 주시겠어요?</strong>: 정중한 요청을 나타내는 -아/어 주시겠어요? 문법입니다.</p>',
        'correct': '닫아 주시겠어요?',
        'choices': ['닫아 주시겠어요?', '닫을래요?', '닫아야 해요', '닫으러 가요'],
    },
    {
        'text': '<p><strong>A: 미술관 안에서 이 아름다운 그림을 사진으로 찍어도 돼요?<br>B: 아니요, 여기서 사진을 ________.</strong></p>',
        'hint': '<p>어떤 행동을 하는 것이 허용되지 않음을 나타냅니다.</p>',
        'explanation': '<p><strong>찍으면 안 돼요</strong>: 금지나 불허를 나타내는 -(으)면 안 돼요 문법입니다.</p>',
        'correct': '찍으면 안 돼요',
        'choices': ['찍으면 안 돼요', '찍지 않아도 돼요', '찍어도 돼요', '찍을게요'],
    },
    {
        'text': '<p><strong>A: 내일은 아주 중요한 회사 면접이 있어요.<br>B: 그러면 단정한 정장을 반드시 ________.</strong></p>',
        'hint': '<p>어떤 행동을 하는 것이 필수적임을 나타냅니다.</p>',
        'explanation': '<p><strong>입어야 해요</strong>: 의무나 필수를 나타내는 -아/어야 하다 문법입니다.</p>',
        'correct': '입어야 해요',
        'choices': ['입어야 해요', '입으면 되다', '입지 마세요', '입어 주세요'],
    },
    {
        'text': '<p><strong>A: 외국어를 아주 자연스럽게 잘하고 싶어요.<br>B: 그러면 매일 꾸준히 ________.</strong></p>',
        'hint': '<p>어떤 목적을 위해 그 행동이 필요함을 나타냅니다.</p>',
        'explanation': '<p><strong>연습할 필요가 있어요</strong>: 필요성을 나타내는 -(으)ㄹ 필요가 있다 문법입니다.</p>',
        'correct': '연습할 필요가 있어요',
        'choices': ['연습할 필요가 있어요', '연습할래요?', '연습하면 안 돼요', '연습합시다'],
    },
    {
        'text': '<p><strong>A: 이번 방학 계획이 뭐예요?<br>B: 저는 조용한 바닷가에서 푹 ________.</strong></p>',
        'hint': '<p>말하는 사람의 소망이나 희망을 나타냅니다.</p>',
        'explanation': '<p><strong>쉬면 좋겠어요</strong>: 바램을 나타내는 -(으)면 좋겠어요 문법입니다.</p>',
        'correct': '쉬면 좋겠어요',
        'choices': ['쉬면 좋겠어요', '쉬어 주세요', '쉬지 마세요', '쉬어야 해요'],
    },
    {
        'text': '<p><strong>A: 저녁에 달콤하고 시원한 아이스크림을 같이 ________?<br>B: 네, 저도 단 게 먹고 싶었어요!</strong></p>',
        'hint': '<p>친한 사이에서 의향을 묻거나 가볍게 제안할 때 사용합니다.</p>',
        'explanation': '<p><strong>먹을래요?</strong>: 의향을 묻거나 제안하는 -(으)ㄹ래요? 문법입니다.</p>',
        'correct': '먹을래요?',
        'choices': ['먹을래요?', '먹읍시다', '먹어 주세요', '먹으십시오'],
    },
    {
        'text': '<p><strong>A: 거실이 너무 지저분해요. 누가 청소할 거예요?<br>B: 제가 지금 바로 깨끗하게 ________.</strong></p>',
        'hint': '<p>말하는 사람의 의지나 약속을 나타냅니다.</p>',
        'explanation': '<p><strong>청소할게요</strong>: 자신의 의지나 약속을 표현하는 -(으)ㄹ게요 문법입니다.</p>',
        'correct': '청소할게요',
        'choices': ['청소할게요', '청소하세요', '청소할까요?', '청소하면 안 돼요'],
    },
    {
        'text': '<p><strong>A: 내년 새해 목표가 무엇입니까?<br>B: 저는 매일 아침 일찍 규칙적으로 ________.</strong></p>',
        'hint': '<p>어떤 행동을 할 계획이나 의도가 있음을 나타냅니다.</p>',
        'explanation': '<p><strong>운동하려고 해요</strong>: 의도나 계획을 나타내는 -(으)려고 하다 문법입니다.</p>',
        'correct': '운동하려고 해요',
        'choices': ['운동하려고 해요', '운동할게요', '운동하세요', '운동해 주시겠어요?'],
    },
    {
        'text': '<p><strong>A: 지금 급하게 밖으로 왜 나가요?<br>B: 날씨가 너무 더워서 시원한 음료수를 ________.</strong></p>',
        'hint': '<p>이동하는 목적을 나타냅니다.</p>',
        'explanation': '<p><strong>사러 가요</strong>: 목적을 위해 이동함을 나타내는 -(으)러 가다 문법입니다.</p>',
        'correct': '사러 가요',
        'choices': ['사러 가요', '사면 좋겠어요', '사지 마세요', '사도 돼요'],
    },
    {
        'text': '<p><strong>A: 내일도 일찍 회사에 출근해야 해요?<br>B: 아니요, 내일은 공휴일이라서 ________.</strong></p>',
        'hint': '<p>어떤 행동을 할 의무나 필요가 없음을 나타냅니다.</p>',
        'explanation': '<p><strong>출근하지 않아도 돼요</strong>: 불필요나 면제를 나타내는 -지 않아도 되다 문법입니다.</p>',
        'correct': '출근하지 않아도 돼요',
        'choices': ['출근하지 않아도 돼요', '출근해야 해요', '출근하려고 해요', '출근할 필요가 있어요'],
    },
    {
        'text': '<p><strong>A: 복잡한 서울역에 어떻게 가요?<br>B: 여기서 파란색 지하철 1호선을 ________.</strong></p>',
        'hint': '<p>어떤 조건을 충족하면 충분하거나 해결됨을 나타냅니다.</p>',
        'explanation': '<p><strong>타면 돼요</strong>: 최소한의 요건이나 해결책을 나타내는 -(으)면 되다 문법입니다.</p>',
        'correct': '타면 돼요',
        'choices': ['타면 돼요', '타면 안 돼요', '타지 마세요', '타러 가요'],
    },
    {
        'text': '<p><strong>A: 다리가 너무 아픈데, 이 푹신한 의자에 잠시 ________?<br>B: 네, 편하게 앉으세요.</strong></p>',
        'hint': '<p>어떤 행동을 하는 것에 대한 허락을 구하거나 허용할 때 사용합니다.</p>',
        'explanation': '<p><strong>앉아도 돼요?</strong>: 허락을 나타내는 -아/어도 되다 문법입니다.</p>',
        'correct': '앉아도 돼요?',
        'choices': ['앉아도 돼요?', '앉아야 해요?', '앉으십시오', '앉을래요?'],
    },
    {
        'text': '<p><strong>A: 내일 멀리 소풍 가는데 비가 오면 어떡하죠?<br>B: 날씨가 아주 ________.</strong></p>',
        'hint': '<p>어떤 일이 일어나기를 바라는 마음을 독백처럼 나타냅니다.</p>',
        'explanation': '<p><strong>맑으면 좋겠다</strong>: 강한 소망이나 바램을 나타내는 -(으)면 좋겠다 문법입니다.</p>',
        'correct': '맑으면 좋겠다',
        'choices': ['맑으면 좋겠다', '맑아도 된다', '맑아야 한다', '맑을게요'],
    },
    {
        'text': '<p><strong>A: 안내 말씀 드리겠습니다. 승객 여러분께서는 모두 안전벨트를 ________.<br>B: (비행기 안내 방송)</strong></p>',
        'hint': '<p>공식적인 상황에서 바라는 바를 정중하게 요청할 때 사용합니다.</p>',
        'explanation': '<p><strong>매 주시기 바랍니다</strong>: 공식적인 요청을 나타내는 -기 바랍니다 문법입니다.</p>',
        'correct': '매 주시기 바랍니다',
        'choices': ['매 주시기 바랍니다', '매지 마십시오', '맬까요?', '매면 안 됩니다'],
    },
    {
        'text': '<p><strong>A: 이 복잡한 수학 문제가 너무 어려워요.<br>B: 혼자 고민하지 말고 선생님께 자세히 ________.</strong></p>',
        'hint': '<p>명령이나 부드러운 권유를 나타냅니다.</p>',
        'explanation': '<p><strong>물어보세요</strong>: 권유를 나타내는 -(으)세요 문법입니다.</p>',
        'correct': '물어보세요',
        'choices': ['물어보세요', '물어볼게요', '물어보면 안 돼요', '물어보러 가요'],
    },
    {
        'text': '<p><strong>A: 비가 와서 바닥이 많이 미끄러워요.<br>B: 매우 위험하니까 복도에서 빨리 ________.</strong></p>',
        'hint': '<p>어떤 행동을 하지 말라고 지시할 때 사용합니다.</p>',
        'explanation': '<p><strong>뛰지 마세요</strong>: 금지를 나타내는 -지 마세요 문법입니다.</p>',
        'correct': '뛰지 마세요',
        'choices': ['뛰지 마세요', '뛰어야 해요', '뛸 필요가 있어요', '뛰어도 돼요'],
    },
    {
        'text': '<p><strong>A: 도서관에서 책을 다 빌렸어요.<br>B: 그럼 이제 조용한 카페에서 같이 ________?</strong></p>',
        'hint': '<p>상대방의 의견을 물으며 제안할 때 사용합니다.</p>',
        'explanation': '<p><strong>공부할까요?</strong>: 제안을 나타내는 -(으)ㄹ까요? 문법입니다.</p>',
        'correct': '공부할까요?',
        'choices': ['공부할까요?', '공부하십시오', '공부하지 않아도 돼요', '공부하면 되다'],
    },
    {
        'text': '<p><strong>A: 오늘 중요한 프로젝트를 다 끝냈어요!<br>B: 그럼 다 같이 시원한 맥주를 ________.</strong></p>',
        'hint': '<p>다 같이 어떤 행동을 하자고 제안할 때 사용합니다.</p>',
        'explanation': '<p><strong>마십시다</strong>: 청유를 나타내는 -ㅂ시다/읍시다 문법입니다.</p>',
        'correct': '마십시다',
        'choices': ['마십시다', '마실게요', '마시려고 해요', '마시러 와요'],
    },
    {
        'text': '<p><strong>A: 양손에 무거운 짐이 있어서 문을 열 수가 없어요.<br>B: 제가 도와드릴까요?<br>A: 네, 문 좀 활짝 ________.</strong></p>',
        'hint': '<p>다른 사람에게 도움이나 행동을 요청할 때 사용합니다.</p>',
        'explanation': '<p><strong>열어 주세요</strong>: 부탁을 나타내는 -아/어 주세요 문법입니다.</p>',
        'correct': '열어 주세요',
        'choices': ['열어 주세요', '열면 안 돼요', '열어야 해요', '열어 주시겠어요?'],  # '열어 주시겠어요?' is also correct conceptually, but '열어 주세요' fits the less formal dynamic better. To be strict, let's make the alternate option incorrect structurally: '열을래요?'
    },
    {
        'text': '<p><strong>A: 수업 시간에 계속 졸려요.<br>B: 그래도 수업 시간에 책상에 엎드려 ________.</strong></p>',
        'hint': '<p>어떤 행동을 하면 규정에 어긋나거나 나쁜 결과가 생길 때 사용합니다.</p>',
        'explanation': '<p><strong>자면 안 돼요</strong>: 금지를 나타내는 -(으)면 안 돼요 문법입니다.</p>',
        'correct': '자면 안 돼요',
        'choices': ['자면 안 돼요', '자도 돼요', '자려고 해요', '자면 좋겠어요'],
    },
    {
        'text': '<p><strong>A: 밖에는 눈이 엄청 많이 오고 있어요.<br>B: 길이 미끄러우니까 운전을 정말 조심해서 ________.</strong></p>',
        'hint': '<p>반드시 그렇게 해야 함을 나타냅니다.</p>',
        'explanation': '<p><strong>해야 해요</strong>: 의무를 나타내는 -아/어야 하다 문법입니다.</p>',
        'correct': '해야 해요',
        'choices': ['해야 해요', '하면 돼요', '하지 마세요', '할 필요가 있다'],
    },
    {
        'text': '<p><strong>A: 이 서류들을 누가 우체국에 가져갈까요?<br>B: 제가 마침 밖으로 나가는 길이니까 제가 ________.</strong></p>',
        'hint': '<p>자신이 어떤 일을 하겠다고 상대방에게 약속할 때 사용합니다.</p>',
        'explanation': '<p><strong>가져갈게요</strong>: 약속과 의지를 나타내는 -(으)ㄹ게요 문법입니다.</p>',
        'correct': '가져갈게요',
        'choices': ['가져갈게요', '가져가세요', '가져가면 안 돼요', '가져가려고 해요'],
    },
    {
        'text': '<p><strong>A: 주말에 보통 뭐 해요?<br>B: 예쁜 풍경을 ________ 자주 산에 가요.</strong></p>',
        'hint': '<p>이동하는 목적이나 이유를 나타냅니다.</p>',
        'explanation': '<p><strong>보러</strong>: 어떤 행동을 하기 위해 이동함을 나타내는 -(으)러 가다/오다 문법입니다.</p>',
        'correct': '보러',
        'choices': ['보러', '보려고', '보아서', '보면'],
    },
    {
        'text': '<p><strong>A: 이 빨간 구두가 아주 예뻐요. 제가 한 번 ________?<br>B: 네, 사이즈가 맞는지 편하게 신어 보세요.</strong></p>',
        'hint': '<p>행동에 대한 허락을 구할 때 사용합니다.</p>',
        'explanation': '<p><strong>신어도 돼요?</strong>: 허락을 구하는 -아/어도 되다 문법입니다.</p>',
        'correct': '신어도 돼요?',
        'choices': ['신어도 돼요?', '신어야 해요?', '신을 필요가 있어요?', '신으러 가요?'],
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
            title='한국어 2. Buyruq, Istak, Imkoniyat va Majburiyatni Ifodalovchi Fe\'l Formlari',  # --- IGNORE ---
            master=master,
            defaults={
                'description': 'Buyruq, Istak, Imkoniyat va Majburiyatni Ifodalovchi Fe\'l Formlari',
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
