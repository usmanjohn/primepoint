from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
    {
        'text': '<p><strong>A: 요즘 한국어 공부가 어때요?<br>B: 문법이 조금 ________.</strong></p>',
        'hint': '<p>"요즘"은 현재 상태를 나타냅니다.</p>',
        'explanation': '<p><strong>어려워요</strong>: "어렵다"는 ㅂ 불규칙 형용사입니다.</p>',
        'correct': '어려워요',
        'choices': ['어렵어요', '어려워요', '어려웠어요', '어려울 거예요'],
    },
    {
        'text': '<p><strong>A: 방금 왜 물을 마셨어요?<br>B: 음식이 너무 ________.</strong></p>',
        'hint': '<p>"방금"은 과거 상황입니다.</p>',
        'explanation': '<p><strong>매웠어요</strong>: "맵다"의 과거형입니다.</p>',
        'correct': '매웠어요',
        'choices': ['매워요', '매웠어요', '맵고 있어요', '매울 거예요'],
    },
    {
        'text': '<p><strong>A: 요즘 운동 자주 해요?<br>B: 네, 그래서 몸이 많이 ________.</strong></p>',
        'hint': '<p>현재 변화 상태입니다.</p>',
        'explanation': '<p><strong>가벼워요</strong>: "가볍다"는 ㅂ 불규칙입니다.</p>',
        'correct': '가벼워요',
        'choices': ['가볍어요', '가벼워요', '가벼웠어요', '가벼울 거예요'],
    },
    {
        'text': '<p><strong>A: 아까 왜 창문을 열었어요?<br>B: 방 안이 너무 ________.</strong></p>',
        'hint': '<p>과거 이유입니다.</p>',
        'explanation': '<p><strong>더웠어요</strong>: "덥다"의 과거형입니다.</p>',
        'correct': '더웠어요',
        'choices': ['더워요', '더웠어요', '덥고 있어요', '더울 거예요'],
    },
    {
        'text': '<p><strong>A: 보통 몇 시에 자요?<br>B: 보통 일찍 ________.</strong></p>',
        'hint': '<p>"보통"은 습관입니다.</p>',
        'explanation': '<p><strong>자요</strong>: 현재 습관 표현입니다.</p>',
        'correct': '자요',
        'choices': ['자요', '잤어요', '자고 있어요', '잘 거예요'],
    },
    {
        'text': '<p><strong>A: 곧 시험이 있죠?<br>B: 네, 그래서 요즘 아주 ________.</strong></p>',
        'hint': '<p>현재 상태입니다.</p>',
        'explanation': '<p><strong>바빠요</strong>: "바쁘다"는 ㅡ 탈락 활용입니다.</p>',
        'correct': '바빠요',
        'choices': ['바쁘어요', '바빠요', '바빴어요', '바쁠 거예요'],
    },
    {
        'text': '<p><strong>A: 조금 전에 누구를 만났어요?<br>B: 공원에서 선생님을 ________. (만나다)</strong></p>',
        'hint': '<p>"조금 전에"는 과거입니다.</p>',
        'explanation': '<p><strong>만났어요</strong>: 과거형입니다.</p>',
        'correct': '만났어요',
        'choices': ['만나요', '만났어요', '만나고 있어요', '만날 거예요'],
    },
    {
        'text': '<p><strong>A: 요즘 날씨가 어때요?<br>B: 아침에는 조금 ________.</strong></p>',
        'hint': '<p>현재 상태입니다.</p>',
        'explanation': '<p><strong>추워요</strong>: "춥다"의 현재형입니다.</p>',
        'correct': '추워요',
        'choices': ['춥어요', '추워요', '추웠어요', '추울 거예요'],
    },
    {
        'text': '<p><strong>A: 이 가방 어때요?<br>B: 조금 ________ 그래도 좋아요.</strong></p>',
        'hint': '<p>현재 상태입니다.</p>',
        'explanation': '<p><strong>무거워요</strong>: "무겁다"는 ㅂ 불규칙입니다.</p>',
        'correct': '무거워요',
        'choices': ['무겁어요', '무거워요', '무거웠어요', '무거울 거예요'],
    },
    {
        'text': '<p><strong>A: 나중에 같이 여행 갈까요?<br>B: 좋아요! 저는 제주도에 꼭 ________ 거예요. (가다)</strong></p>',
        'hint': '<p>"나중에"는 미래 표현입니다.</p>',
        'explanation': '<p><strong>갈</strong>: 미래 관형형입니다.</p>',
        'correct': '갈',
        'choices': ['가요', '갔어요', '가고 있어요', '갈'],
    },
    {
        'text': '<p><strong>A: 요즘 왜 그렇게 행복해 보여요?<br>B: 회사 일이 많이 ________.</strong></p>',
        'hint': '<p>현재 상태 변화입니다.</p>',
        'explanation': '<p><strong>쉬워요</strong>: "쉽다"의 활용입니다.</p>',
        'correct': '쉬워요',
        'choices': ['쉽어요', '쉬워요', '쉬웠어요', '쉬울 거예요'],
    },
    {
        'text': '<p><strong>A: 방금 뭐 들었어요?<br>B: 재미있는 이야기를 ________. (듣다)</strong></p>',
        'hint': '<p>"방금"은 과거입니다.</p>',
        'explanation': '<p><strong>들었어요</strong>: "듣다"는 ㄷ 불규칙입니다.</p>',
        'correct': '들었어요',
        'choices': ['듣어요', '들었어요', '듣고 있어요', '들을 거예요'],
    },
    {
        'text': '<p><strong>A: 요즘 회사까지 어떻게 가요?<br>B: 가끔 회사까지 ________. (걷다)</strong></p>',
        'hint': '<p>"가끔"은 습관 표현입니다.</p>',
        'explanation': '<p><strong>걸어요</strong>: "걷다"는 ㄷ 불규칙입니다.</p>',
        'correct': '걸어요',
        'choices': ['걷어요', '걸어요', '걸었어요', '걸을 거예요'],
    },
    {
        'text': '<p><strong>A: 이 음식 자주 먹어요?<br>B: 아니요, 너무 ________.</strong></p>',
        'hint': '<p>현재 상태입니다.</p>',
        'explanation': '<p><strong>매워요</strong>: "맵다"의 현재형입니다.</p>',
        'correct': '매워요',
        'choices': ['맵어요', '매워요', '매웠어요', '매울 거예요'],
    },
    {
        'text': '<p><strong>A: 이따가 뭐 할 거예요?<br>B: 친구를 ________ 거예요. (돕다)</strong></p>',
        'hint': '<p>"이따가"는 미래입니다.</p>',
        'explanation': '<p><strong>도울</strong>: "돕다"의 미래형입니다.</p>',
        'correct': '도울',
        'choices': ['도와요', '도왔어요', '돕고 있어요', '도울'],
    },
    {
        'text': '<p><strong>A: 요즘 피곤해 보여요.<br>B: 네, 일이 너무 ________.</strong></p>',
        'hint': '<p>현재 상태입니다.</p>',
        'explanation': '<p><strong>많아요</strong>: 현재 상태 표현입니다.</p>',
        'correct': '많아요',
        'choices': ['많아요', '많았어요', '많고 있어요', '많을 거예요'],
    },
    {
        'text': '<p><strong>A: 조금 전에 왜 웃었어요?<br>B: 친구 이야기가 정말 ________.</strong></p>',
        'hint': '<p>과거 상황입니다.</p>',
        'explanation': '<p><strong>재미있었어요</strong>: 과거 상태 표현입니다.</p>',
        'correct': '재미있었어요',
        'choices': ['재미있어요', '재미있었어요', '재미있고 있어요', '재미있을 거예요'],
    },
    {
        'text': '<p><strong>A: 요즘 학교까지 멀어요?<br>B: 아니요, 지금은 아주 ________.</strong></p>',
        'hint': '<p>현재 상태입니다.</p>',
        'explanation': '<p><strong>가까워요</strong>: 현재 상태 표현입니다.</p>',
        'correct': '가까워요',
        'choices': ['가깝어요', '가까워요', '가까웠어요', '가까울 거예요'],
    },
    {
        'text': '<p><strong>A: 아까 누구를 불렀어요?<br>B: 동생을 ________. (부르다)</strong></p>',
        'hint': '<p>"아까"는 과거입니다.</p>',
        'explanation': '<p><strong>불렀어요</strong>: 르 불규칙 활용입니다.</p>',
        'correct': '불렀어요',
        'choices': ['불러요', '불렀어요', '부르고 있어요', '부를 거예요'],
    },
    {
        'text': '<p><strong>A: 보통 주말에 뭐 해요?<br>B: 집에서 음악을 ________. (듣다)</strong></p>',
        'hint': '<p>"보통"은 습관입니다.</p>',
        'explanation': '<p><strong>들어요</strong>: "듣다"의 현재형입니다.</p>',
        'correct': '들어요',
        'choices': ['듣어요', '들어요', '들었어요', '들을 거예요'],
    },
    {
        'text': '<p><strong>A: 곧 출발할 거예요?<br>B: 네, 지금 준비하고 ________.</strong></p>',
        'hint': '<p>현재 진행입니다.</p>',
        'explanation': '<p><strong>있어요</strong>: 진행형 표현입니다.</p>',
        'correct': '있어요',
        'choices': ['있어요', '있었어요', '있고 있어요', '있을 거예요'],
    },
    {
        'text': '<p><strong>A: 요즘 한국 생활이 어때요?<br>B: 처음에는 힘들었지만 지금은 많이 ________.</strong></p>',
        'hint': '<p>현재 상태 변화입니다.</p>',
        'explanation': '<p><strong>쉬워요</strong>: "쉽다"의 현재형입니다.</p>',
        'correct': '쉬워요',
        'choices': ['쉽어요', '쉬워요', '쉬웠어요', '쉬울 거예요'],
    },
    {
        'text': '<p><strong>A: 방금 왜 문을 닫았어요?<br>B: 밖이 너무 ________.</strong></p>',
        'hint': '<p>과거 이유입니다.</p>',
        'explanation': '<p><strong>시끄러웠어요</strong>: 과거 상태입니다.</p>',
        'correct': '시끄러웠어요',
        'choices': ['시끄러워요', '시끄러웠어요', '시끄럽고 있어요', '시끄러울 거예요'],
    },
    {
        'text': '<p><strong>A: 자주 요리해요?<br>B: 네, 요즘 김치찌개를 자주 ________. (만들다)</strong></p>',
        'hint': '<p>"자주"는 습관입니다.</p>',
        'explanation': '<p><strong>만들어요</strong>: 현재 습관 표현입니다.</p>',
        'correct': '만들어요',
        'choices': ['만들어요', '만들었어요', '만들고 있어요', '만들 거예요'],
    },
    {
        'text': '<p><strong>A: 나중에 어떤 집에서 살고 싶어요?<br>B: 조용하고 ________ 집에서 살고 싶어요.</strong></p>',
        'hint': '<p>현재 희망 표현입니다.</p>',
        'explanation': '<p><strong>넓은</strong>: 관형사형 표현입니다.</p>',
        'correct': '넓은',
        'choices': ['넓은', '넓었어요', '넓고 있어요', '넓을 거예요'],
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
            title='2. 불규칙 (Noto‘g‘ri fe’llar)',
            master=master,
            defaults={
                'description': '한국어 불규칙 활용 연습 2.',
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
