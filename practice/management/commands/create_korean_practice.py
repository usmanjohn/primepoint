from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice
QUESTIONS = [
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>저는 매일 아침 7시 ___ 일어납니다.</strong></p>',
        'hint': '<p>시간을 나타내는 명사 뒤에 붙는 조사를 고르세요.</p>',
        'explanation': '<p><strong>에</strong>: 시간이나 날짜 뒤에 붙어서 어떤 일이 일어나는 때를 나타냅니다.</p>',
        'correct': '에',
        'choices': ['에', '에서', '부터', '까지'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>주말에 친구하고 영화관 ___ 영화를 봤어요.</strong></p>',
        'hint': '<p>어떤 동작이나 행동이 일어나는 장소를 나타내는 조사를 고르세요.</p>',
        'explanation': '<p><strong>에서</strong>: 동작이 이루어지는 장소를 나타낼 때 사용합니다. "영화를 보다"라는 행동이 일어나는 곳이므로 "에서"가 맞습니다.</p>',
        'correct': '에서',
        'choices': ['에', '에서', '부터', '까지'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>한국어 수업은 오후 1시 ___ 3시까지입니다.</strong></p>',
        'hint': '<p>시간의 시작점을 나타내는 조사를 고르세요.</p>',
        'explanation': '<p><strong>부터</strong>: 어떤 일이나 상태가 시작되는 시간이나 장소를 나타냅니다. "까지"와 함께 자주 쓰입니다.</p>',
        'correct': '부터',
        'choices': ['에', '에서', '부터', '하고'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>서울역에서 명동 ___ 어떻게 가요?</strong></p>',
        'hint': '<p>도착점이나 끝나는 지점을 나타내는 조사를 고르세요.</p>',
        'explanation': '<p><strong>까지</strong>: 장소나 시간의 끝나는 점을 나타냅니다. "에서"와 함께 출발점과 도착점을 나타낼 때 자주 씁니다.</p>',
        'correct': '까지',
        'choices': ['에', '에서', '부터', '까지'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>제 책은 가방 안 ___ 없어요.</strong></p>',
        'hint': '<p>사물이나 사람이 있는(또는 없는) 위치를 나타내는 조사를 고르세요.</p>',
        'explanation': '<p><strong>에</strong>: 사람이나 사물이 존재하는 장소를 나타냅니다. "있다/없다"와 함께 쓰입니다.</p>',
        'correct': '에',
        'choices': ['에', '에서', '가', '를'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>저는 작년에 베트남 ___ 왔습니다.</strong></p>',
        'hint': '<p>출발지나 고향 등을 나타낼 때 쓰는 조사를 고르세요.</p>',
        'explanation': '<p><strong>에서</strong>: 출발점을 나타낼 때 사용합니다. "오다", "출발하다" 등의 동사와 함께 쓰입니다.</p>',
        'correct': '에서',
        'choices': ['에', '에서', '으로', '부터'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>이 숙제는 내일 ___ 꼭 내야 해요.</strong></p>',
        'hint': '<p>어떤 일의 기한이나 끝나는 시간을 나타내는 조사를 고르세요.</p>',
        'explanation': '<p><strong>까지</strong>: 동작이나 상태가 계속되다가 끝나는 시간을 나타냅니다.</p>',
        'correct': '까지',
        'choices': ['에', '에서', '부터', '까지'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>오늘 오후에 친구 집 ___ 갈 거예요.</strong></p>',
        'hint': '<p>이동하는 목적지를 나타내는 조사를 고르세요.</p>',
        'explanation': '<p><strong>에</strong>: "가다", "오다", "다니다"와 같은 이동 동사와 함께 쓰여 목적지를 나타냅니다.</p>',
        'correct': '에',
        'choices': ['을', '에서', '에', '가'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>이 식당은 오전 11시 ___ 문을 엽니다.</strong></p>',
        'hint': '<p>시작하는 시간을 나타내는 조사를 고르세요.</p>',
        'explanation': '<p><strong>부터</strong>: 시간의 시작점을 나타냅니다.</p>',
        'correct': '부터',
        'choices': ['에', '에서', '부터', '까지'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>도서관 ___ 떠들면 안 됩니다.</strong></p>',
        'hint': '<p>어떤 행동을 하는 장소를 나타내는 조사를 고르세요.</p>',
        'explanation': '<p><strong>에서</strong>: 어떤 행동이나 일이 일어나는 장소를 나타냅니다. "떠들다"라는 행동이 일어나는 장소이므로 "에서"를 씁니다.</p>',
        'correct': '에서',
        'choices': ['에', '에서', '은', '를'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>이번 주 일요일 ___ 만날까요?</strong></p>',
        'hint': '<p>요일이나 날짜 뒤에 붙어 시간을 나타내는 조사를 고르세요.</p>',
        'explanation': '<p><strong>에</strong>: 특정한 때나 시간을 나타냅니다. (단, 오늘, 내일, 어제, 지금 등에는 쓰지 않습니다.)</p>',
        'correct': '에',
        'choices': ['에', '에서', '을', '가'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>공항 ___ 호텔까지 택시를 타고 갑시다.</strong></p>',
        'hint': '<p>이동의 출발점을 나타내는 조사를 고르세요.</p>',
        'explanation': '<p><strong>에서</strong>: 장소의 출발점을 나타냅니다. 도착점을 나타내는 "까지"와 호응하여 쓰였습니다.</p>',
        'correct': '에서',
        'choices': ['에', '에서', '부터', '하고'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>어제 밤 11시 ___ 텔레비전을 봤어요.</strong></p>',
        'hint': '<p>동작이 지속되다가 끝나는 시간을 나타내는 조사를 고르세요.</p>',
        'explanation': '<p><strong>까지</strong>: 어떤 행동이 끝나는 시간적 한계를 나타냅니다.</p>',
        'correct': '까지',
        'choices': ['에', '에서', '부터', '까지'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>우리는 보통 학생 식당 ___ 점심을 먹습니다.</strong></p>',
        'hint': '<p>밥을 먹는 장소를 나타내는 조사를 고르세요.</p>',
        'explanation': '<p><strong>에서</strong>: "밥을 먹다"라는 구체적인 행동이 이루어지는 장소이므로 "에서"가 맞습니다.</p>',
        'correct': '에서',
        'choices': ['에', '에서', '으로', '를'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>먼저 손 ___ 씻고 밥을 드세요.</strong></p>',
        'hint': '<p>순서상 먼저 시작해야 하는 대상을 나타낼 때도 쓰는 조사를 고르세요.</p>',
        'explanation': '<p><strong>부터</strong>: 시간의 시작점뿐만 아니라, 어떤 일의 순서상 가장 먼저 함을 나타낼 때도 쓰입니다.</p>',
        'correct': '부터',
        'choices': ['에', '에서', '부터', '까지'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>지하철역은 은행 옆 ___ 있습니다.</strong></p>',
        'hint': '<p>어떤 장소가 위치한 곳을 나타내는 조사를 고르세요.</p>',
        'explanation': '<p><strong>에</strong>: 존재나 위치를 나타내는 동사 "있다, 없다"와 함께 쓰여 위치를 나타냅니다.</p>',
        'correct': '에',
        'choices': ['을', '가', '에', '에서'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>이 버스는 서울역 ___ 갑니까?</strong></p>',
        'hint': '<p>이동의 목적지나 한계점을 강조할 때 쓰는 표현을 고르세요.</p>',
        'explanation': '<p><strong>까지</strong>: 도착하는 끝 지점을 나타냅니다. ("에"도 가능하지만 보기 중에서는 목적지까지 도달함을 나타내는 "까지"가 알맞게 쓰일 수 있습니다.)</p>',
        'correct': '까지',
        'choices': ['에서', '부터', '까지', '은'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>백화점 ___ 예쁜 옷을 샀어요.</strong></p>',
        'hint': '<p>물건을 사는 행동이 일어난 장소를 나타내는 조사를 고르세요.</p>',
        'explanation': '<p><strong>에서</strong>: 물건을 사는 동작이 이루어지는 장소를 나타내므로 "에서"를 사용합니다.</p>',
        'correct': '에서',
        'choices': ['에', '에서', '부터', '가'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>월요일 ___ 금요일까지 회사에서 일해요.</strong></p>',
        'hint': '<p>기간의 시작을 나타내는 조사를 고르세요.</p>',
        'explanation': '<p><strong>부터</strong>: 일하는 기간의 시작점을 나타냅니다. "까지"와 호응합니다.</p>',
        'correct': '부터',
        'choices': ['에', '에서', '부터', '하고'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>내 생일 파티는 토요일 ___ 할 거예요.</strong></p>',
        'hint': '<p>요일을 나타내는 명사 뒤에 붙는 조사를 고르세요.</p>',
        'explanation': '<p><strong>에</strong>: 시간, 날짜, 요일 명사 뒤에 붙어 어떤 일이 일어나는 때를 나타냅니다.</p>',
        'correct': '에',
        'choices': ['에', '에서', '부터', '까지'],
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
            title='한국어 Location&Time Particles Practice',
            master=master,
            defaults={
                'description': '한국어의 기본 위치와 시간 조사를 연습하는 테스트예요.',
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
