from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
    {
        'text': '<p><strong>A: 오늘 날씨가 정말 추워요.<br>B: 그러면 따뜻한 옷을 ________.</strong></p>',
        'hint': '<p>정중한 명령 표현입니다.</p>',
        'explanation': '<p><strong>입으세요</strong>: 상대에게 정중하게 권유하거나 명령할 때 사용합니다.</p>',
        'correct': '입으세요',
        'choices': ['입으세요', '입지 마세요', '입을까요?', '입읍시다'],
    },
    {
        'text': '<p><strong>A: 도서관이에요.<br>B: 큰 소리로 이야기하지 ________.</strong></p>',
        'hint': '<p>금지 표현입니다.</p>',
        'explanation': '<p><strong>마세요</strong>: 어떤 행동을 하지 말라고 할 때 사용합니다.</p>',
        'correct': '마세요',
        'choices': ['으세요', '마세요', '을까요?', '읍시다'],
    },
    {
        'text': '<p><strong>A: 조금 피곤한데 커피 한잔 ________?<br>B: 좋아요!</strong></p>',
        'hint': '<p>같이 하자는 제안입니다.</p>',
        'explanation': '<p><strong>마실까요</strong>: 함께 행동을 제안할 때 사용합니다.</p>',
        'correct': '마실까요',
        'choices': ['마시세요', '마시지 마세요', '마실까요', '마십시다'],
    },
    {
        'text': '<p><strong>A: 오늘 저녁에 시간이 있어요?<br>B: 네, 같이 운동________.</strong></p>',
        'hint': '<p>함께 하자는 표현입니다.</p>',
        'explanation': '<p><strong>합시다</strong>: 같이 행동을 제안할 때 사용합니다.</p>',
        'correct': '합시다',
        'choices': ['하세요', '하지 마세요', '할까요?', '합시다'],
    },
    {
        'text': '<p><strong>A: 내일까지 숙제를 꼭 ________.</strong></p>',
        'hint': '<p>의무 표현입니다.</p>',
        'explanation': '<p><strong>해야 해요</strong>: 반드시 해야 하는 상황입니다.</p>',
        'correct': '해야 해요',
        'choices': ['하고 싶어요', '할 수 있어요', '해야 해요', '하면 안 돼요'],
    },
    {
        'text': '<p><strong>A: 요즘 건강이 안 좋아요.<br>B: 매일 아침에 운동을 ________.</strong></p>',
        'hint': '<p>권유 표현입니다.</p>',
        'explanation': '<p><strong>하세요</strong>: 건강을 위해 권유하고 있습니다.</p>',
        'correct': '하세요',
        'choices': ['하세요', '하지 마세요', '할까요?', '합시다'],
    },
    {
        'text': '<p><strong>A: 방이 너무 더워요.<br>B: 창문을 좀 ________ 주세요.</strong></p>',
        'hint': '<p>부탁 표현입니다.</p>',
        'explanation': '<p><strong>열어</strong>: 도움이나 부탁을 할 때 사용합니다.</p>',
        'correct': '열어',
        'choices': ['열고', '열어', '열지', '열을'],
    },
    {
        'text': '<p><strong>A: 지금 너무 늦었어요.<br>B: 그러면 밖에 나가지 ________.</strong></p>',
        'hint': '<p>금지 표현입니다.</p>',
        'explanation': '<p><strong>마세요</strong>: 하지 말라는 뜻입니다.</p>',
        'correct': '마세요',
        'choices': ['으세요', '마세요', '을까요?', '읍시다'],
    },
    {
        'text': '<p><strong>A: 곧 시험이 시작돼요.<br>B: 이제 조용히 ________.</strong></p>',
        'hint': '<p>정중한 명령입니다.</p>',
        'explanation': '<p><strong>하세요</strong>: 시험 전 조용히 하라고 말합니다.</p>',
        'correct': '하세요',
        'choices': ['하세요', '하지 마세요', '할까요?', '합시다'],
    },
    {
        'text': '<p><strong>A: 오늘 저녁에 뭐 먹을까요?<br>B: 맛있는 불고기를 ________.</strong></p>',
        'hint': '<p>함께 하자는 표현입니다.</p>',
        'explanation': '<p><strong>먹읍시다</strong>: 함께 먹자는 의미입니다.</p>',
        'correct': '먹읍시다',
        'choices': ['먹으세요', '먹지 마세요', '먹을까요?', '먹읍시다'],
    },
    {
        'text': '<p><strong>A: 아까부터 머리가 아파요.<br>B: 오늘은 일찍 ________.</strong></p>',
        'hint': '<p>권유 표현입니다.</p>',
        'explanation': '<p><strong>주무세요</strong>: 상대에게 쉬라고 권유합니다.</p>',
        'correct': '주무세요',
        'choices': ['주무세요', '주무시지 마세요', '주무실까요?', '주무십시다'],
    },
    {
        'text': '<p><strong>A: 지금 뭐 해야 해요?<br>B: 먼저 이름을 ________.</strong></p>',
        'hint': '<p>정중한 지시입니다.</p>',
        'explanation': '<p><strong>쓰세요</strong>: 순서대로 해야 할 행동입니다.</p>',
        'correct': '쓰세요',
        'choices': ['쓰세요', '쓰지 마세요', '쓸까요?', '씁시다'],
    },
    {
        'text': '<p><strong>A: 날씨가 정말 추워졌어요.<br>B: 감기에 걸리지 않게 조심________.</strong></p>',
        'hint': '<p>정중한 부탁/권유입니다.</p>',
        'explanation': '<p><strong>하세요</strong>: 조심하라고 권유합니다.</p>',
        'correct': '하세요',
        'choices': ['하세요', '하지 마세요', '할까요?', '합시다'],
    },
    {
        'text': '<p><strong>A: 이 음식이 너무 매워요.<br>B: 그럼 천천히 ________.</strong></p>',
        'hint': '<p>권유 표현입니다.</p>',
        'explanation': '<p><strong>드세요</strong>: 천천히 먹으라는 의미입니다.</p>',
        'correct': '드세요',
        'choices': ['드세요', '드시지 마세요', '드실까요?', '드십시다'],
    },
    {
        'text': '<p><strong>A: 내일 아침 일찍 출발해야 해요.<br>B: 오늘 늦게 자면 안 돼요. 일찍 ________.</strong></p>',
        'hint': '<p>의무/권유 표현입니다.</p>',
        'explanation': '<p><strong>자야 해요</strong>: 꼭 해야 하는 행동입니다.</p>',
        'correct': '자야 해요',
        'choices': ['자고 싶어요', '잘 수 있어요', '자야 해요', '자면 안 돼요'],
    },
    {
        'text': '<p><strong>A: 방금 전화 왔어요?<br>B: 네, 이따가 다시 전화________고 했어요.</strong></p>',
        'hint': '<p>약속/의무 표현입니다.</p>',
        'explanation': '<p><strong>해야 한다</strong>: 다시 전화할 필요가 있다는 뜻입니다.</p>',
        'correct': '해야 한다',
        'choices': ['하고 싶다', '할 수 있다', '해야 한다', '하면 안 된다'],
    },
    {
        'text': '<p><strong>A: 요즘 왜 그렇게 피곤해요?<br>B: 매일 늦게 자지 말고 일찍 ________.</strong></p>',
        'hint': '<p>권유 표현입니다.</p>',
        'explanation': '<p><strong>주무세요</strong>: 건강을 위한 권유입니다.</p>',
        'correct': '주무세요',
        'choices': ['주무세요', '주무시지 마세요', '주무실까요?', '주무십시다'],
    },
    {
        'text': '<p><strong>A: 가끔 너무 늦게까지 게임해요.<br>B: 건강에 안 좋으니까 너무 오래 하지 ________.</strong></p>',
        'hint': '<p>금지 표현입니다.</p>',
        'explanation': '<p><strong>마세요</strong>: 하지 말라는 뜻입니다.</p>',
        'correct': '마세요',
        'choices': ['으세요', '마세요', '을까요?', '읍시다'],
    },
    {
        'text': '<p><strong>A: 오늘 점심은 뭘 먹을까요?<br>B: 근처 식당에 가서 김치찌개를 ________.</strong></p>',
        'hint': '<p>함께 하자는 표현입니다.</p>',
        'explanation': '<p><strong>먹읍시다</strong>: 제안 표현입니다.</p>',
        'correct': '먹읍시다',
        'choices': ['먹으세요', '먹지 마세요', '먹을까요?', '먹읍시다'],
    },
    {
        'text': '<p><strong>A: 조금 전에 비가 왔어요.<br>B: 길이 미끄러우니까 천천히 ________.</strong></p>',
        'hint': '<p>권유 표현입니다.</p>',
        'explanation': '<p><strong>걸으세요</strong>: 안전을 위한 권유입니다.</p>',
        'correct': '걸으세요',
        'choices': ['걸으세요', '걷지 마세요', '걸을까요?', '걸읍시다'],
    },
    {
        'text': '<p><strong>A: 항상 숙제를 늦게 해요.<br>B: 앞으로는 미리 ________.</strong></p>',
        'hint': '<p>권유 표현입니다.</p>',
        'explanation': '<p><strong>하세요</strong>: 미리 하라고 권유합니다.</p>',
        'correct': '하세요',
        'choices': ['하세요', '하지 마세요', '할까요?', '합시다'],
    },
    {
        'text': '<p><strong>A: 요즘 한국어가 너무 어려워요.<br>B: 걱정하지 말고 매일 조금씩 공부________.</strong></p>',
        'hint': '<p>함께 하는 느낌의 권유입니다.</p>',
        'explanation': '<p><strong>합시다</strong>: 같이 노력하자는 의미입니다.</p>',
        'correct': '합시다',
        'choices': ['하세요', '하지 마세요', '할까요?', '합시다'],
    },
    {
        'text': '<p><strong>A: 나중에 시간 있으면 같이 카페 갈까요?<br>B: 좋아요!</strong></p>',
        'hint': '<p>제안 표현입니다.</p>',
        'explanation': '<p><strong>갈까요</strong>: 함께 하자는 제안입니다.</p>',
        'correct': '갈까요',
        'choices': ['가세요', '가지 마세요', '갈까요', '갑시다'],
    },
    {
        'text': '<p><strong>A: 오늘 너무 바빠요.<br>B: 그래도 점심은 꼭 ________.</strong></p>',
        'hint': '<p>권유/조언 표현입니다.</p>',
        'explanation': '<p><strong>드세요</strong>: 식사를 권유합니다.</p>',
        'correct': '드세요',
        'choices': ['드세요', '드시지 마세요', '드실까요?', '드십시다'],
    },
    {
        'text': '<p><strong>A: 곧 버스가 와요.<br>B: 빨리 ________ 해요.</strong></p>',
        'hint': '<p>의무 표현입니다.</p>',
        'explanation': '<p><strong>가야</strong>: 지금 바로 가야 하는 상황입니다.</p>',
        'correct': '가야',
        'choices': ['가고 싶어', '갈 수 있어', '가야', '가면 안 돼'],
    },
    {
        'text': '<p><strong>A: 도서관에서는 휴대전화를 크게 사용하지 ________.</strong></p>',
        'hint': '<p>금지 표현입니다.</p>',
        'explanation': '<p><strong>마세요</strong>: 공공장소 예절 표현입니다.</p>',
        'correct': '마세요',
        'choices': ['으세요', '마세요', '을까요?', '읍시다'],
    },
    {
        'text': '<p><strong>A: 오늘 날씨가 정말 좋아요.<br>B: 공원에 산책하러 ________?</strong></p>',
        'hint': '<p>제안 표현입니다.</p>',
        'explanation': '<p><strong>갈까요</strong>: 함께 가자는 의미입니다.</p>',
        'correct': '갈까요',
        'choices': ['가세요', '가지 마세요', '갈까요', '갑시다'],
    },
    {
        'text': '<p><strong>A: 방금 만든 음식이에요.<br>B: 와, 정말 맛있겠네요! 빨리 ________.</strong></p>',
        'hint': '<p>권유 표현입니다.</p>',
        'explanation': '<p><strong>드세요</strong>: 음식을 권할 때 자주 사용합니다.</p>',
        'correct': '드세요',
        'choices': ['드세요', '드시지 마세요', '드실까요?', '드십시다'],
    },
    {
        'text': '<p><strong>A: 항상 건강하려면 어떻게 해야 해요?<br>B: 물을 많이 마시고 운동도 자주 ________.</strong></p>',
        'hint': '<p>의무/조언 표현입니다.</p>',
        'explanation': '<p><strong>해야 해요</strong>: 꼭 필요한 행동입니다.</p>',
        'correct': '해야 해요',
        'choices': ['하고 싶어요', '할 수 있어요', '해야 해요', '하면 안 돼요'],
    },
    {
        'text': '<p><strong>A: 지금 너무 시끄러워요.<br>B: 모두 조금만 조용히 ________.</strong></p>',
        'hint': '<p>정중한 요청입니다.</p>',
        'explanation': '<p><strong>하세요</strong>: 조용히 하라고 부탁합니다.</p>',
        'correct': '하세요',
        'choices': ['하세요', '하지 마세요', '할까요?', '합시다'],
    },
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
            title='한국어 1. Buyruq, Istak, Imkoniyat va Majburiyatni Ifodalovchi Fe\'l Formlari',  # --- IGNORE ---
            master=master,
            defaults={
                'description': 'Buyruq, Istak, Imkoniyat va Majburiyatni Ifodalovchi Fe\'l Formlari',
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
