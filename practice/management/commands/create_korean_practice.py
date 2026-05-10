from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice
QUESTIONS = [
    {
        'text': '<p><strong>A: 주말에 뭐 하고 싶어요?<br>B: 친구들하고 제주도에 ________.</strong></p>',
        'hint': '<p>희망 표현입니다.</p>',
        'explanation': '<p><strong>가고 싶어요</strong>: 하고 싶은 일을 말할 때 사용합니다.</p>',
        'correct': '가고 싶어요',
        'choices': ['가고 싶어요', '갈 수 있어요', '가러 가요', '가 봤어요'],
    },
    {
        'text': '<p><strong>A: 한국 음식을 잘 먹어요?<br>B: 네, 매운 음식도 잘 ________.</strong></p>',
        'hint': '<p>능력을 나타냅니다.</p>',
        'explanation': '<p><strong>먹을 수 있어요</strong>: 가능/능력 표현입니다.</p>',
        'correct': '먹을 수 있어요',
        'choices': ['먹고 싶어요', '먹을 수 있어요', '먹으러 가요', '먹어 줘요'],
    },
    {
        'text': '<p><strong>A: 지금 어디에 가요?<br>B: 친구를 ________ 학교에 가요.</strong></p>',
        'hint': '<p>목적 표현입니다.</p>',
        'explanation': '<p><strong>만나러</strong>: 어떤 목적을 가지고 이동할 때 사용합니다.</p>',
        'correct': '만나러',
        'choices': ['만나고 싶어요', '만날 수 있어요', '만나러', '만나 봤어요'],
    },
    {
        'text': '<p><strong>A: 불고기 먹어 봤어요?<br>B: 네, 지난주에 처음 ________.</strong></p>',
        'hint': '<p>경험 표현입니다.</p>',
        'explanation': '<p><strong>먹어 봤어요</strong>: 경험을 나타냅니다.</p>',
        'correct': '먹어 봤어요',
        'choices': ['먹고 싶어요', '먹을 수 있어요', '먹으러 가요', '먹어 봤어요'],
    },
    {
        'text': '<p><strong>A: 숙제가 너무 어려워요.<br>B: 제가 조금 ________.</strong></p>',
        'hint': '<p>도움을 주는 표현입니다.</p>',
        'explanation': '<p><strong>도와줄게요</strong>: 상대를 도와줄 때 사용합니다.</p>',
        'correct': '도와줄게요',
        'choices': ['돕고 싶어요', '도울 수 있어요', '도우러 가요', '도와줄게요'],
    },
    {
        'text': '<p><strong>A: 요즘 왜 바빠요?<br>B: 한국어를 더 열심히 ________ 학원에 다녀요.</strong></p>',
        'hint': '<p>목적 표현입니다.</p>',
        'explanation': '<p><strong>배우러</strong>: 배우는 목적입니다.</p>',
        'correct': '배우러',
        'choices': ['배우고 싶어요', '배울 수 있어요', '배우러', '배워 줘요'],
    },
    {
        'text': '<p><strong>A: 피아노 칠 수 있어요?<br>B: 네, 어릴 때 조금 ________.</strong></p>',
        'hint': '<p>능력 표현입니다.</p>',
        'explanation': '<p><strong>칠 수 있었어요</strong>: 과거의 능력을 말합니다.</p>',
        'correct': '칠 수 있었어요',
        'choices': ['치고 싶었어요', '칠 수 있었어요', '치러 갔어요', '쳐 봤어요'],
    },
    {
        'text': '<p><strong>A: 요즘 어떤 영화 보고 싶어요?<br>B: 사람들이 자주 이야기하는 영화를 ________.</strong></p>',
        'hint': '<p>희망 표현입니다.</p>',
        'explanation': '<p><strong>보고 싶어요</strong>: 원하는 행동입니다.</p>',
        'correct': '보고 싶어요',
        'choices': ['보고 싶어요', '볼 수 있어요', '보러 가요', '봐 줘요'],
    },
    {
        'text': '<p><strong>A: 방금 뭐 했어요?<br>B: 친구 숙제를 조금 ________.</strong></p>',
        'hint': '<p>도움을 준 행동입니다.</p>',
        'explanation': '<p><strong>도와줬어요</strong>: 다른 사람을 도와준 상황입니다.</p>',
        'correct': '도와줬어요',
        'choices': ['돕고 싶었어요', '도울 수 있었어요', '도우러 갔어요', '도와줬어요'],
    },
    {
        'text': '<p><strong>A: 제주도에 가 봤어요?<br>B: 아니요, 하지만 꼭 ________.</strong></p>',
        'hint': '<p>희망 표현입니다.</p>',
        'explanation': '<p><strong>가 보고 싶어요</strong>: 경험을 해 보고 싶은 마음입니다.</p>',
        'correct': '가 보고 싶어요',
        'choices': ['가 보고 싶어요', '갈 수 있어요', '가러 가요', '가 줘요'],
    },
    {
        'text': '<p><strong>A: 오늘 같이 운동하러 갈래요?<br>B: 미안해요. 오늘은 시간이 없어서 ________.</strong></p>',
        'hint': '<p>불가능 표현입니다.</p>',
        'explanation': '<p><strong>갈 수 없어요</strong>: 상황상 불가능합니다.</p>',
        'correct': '갈 수 없어요',
        'choices': ['가고 싶어요', '갈 수 없어요', '가러 가요', '가 봤어요'],
    },
    {
        'text': '<p><strong>A: 왜 서점에 가요?<br>B: 한국어 책을 ________ 가요.</strong></p>',
        'hint': '<p>목적 표현입니다.</p>',
        'explanation': '<p><strong>사러</strong>: 책을 사는 목적입니다.</p>',
        'correct': '사러',
        'choices': ['사고 싶어요', '살 수 있어요', '사러', '사 줘요'],
    },
    {
        'text': '<p><strong>A: 이 문제를 이해할 수 있어요?<br>B: 아니요, 너무 어려워서 잘 ________.</strong></p>',
        'hint': '<p>불가능 표현입니다.</p>',
        'explanation': '<p><strong>이해할 수 없어요</strong>: 이해가 어렵다는 뜻입니다.</p>',
        'correct': '이해할 수 없어요',
        'choices': ['이해하고 싶어요', '이해할 수 없어요', '이해하러 가요', '이해해 줘요'],
    },
    {
        'text': '<p><strong>A: 김치를 만들어 봤어요?<br>B: 네, 지난달에 처음 ________.</strong></p>',
        'hint': '<p>경험 표현입니다.</p>',
        'explanation': '<p><strong>만들어 봤어요</strong>: 처음 경험했다는 뜻입니다.</p>',
        'correct': '만들어 봤어요',
        'choices': ['만들고 싶어요', '만들 수 있어요', '만들러 가요', '만들어 봤어요'],
    },
    {
        'text': '<p><strong>A: 지금 어디 가요?<br>B: 친구를 ________ 역에 가요.</strong></p>',
        'hint': '<p>목적 표현입니다.</p>',
        'explanation': '<p><strong>배웅하러</strong>: 배웅하는 목적입니다.</p>',
        'correct': '배웅하러',
        'choices': ['배웅하고 싶어요', '배웅할 수 있어요', '배웅하러', '배웅해 줘요'],
    },
    {
        'text': '<p><strong>A: 이따가 시간 있어요?<br>B: 네, 그래서 같이 영화 ________.</strong></p>',
        'hint': '<p>희망 표현입니다.</p>',
        'explanation': '<p><strong>보고 싶어요</strong>: 원하는 행동입니다.</p>',
        'correct': '보고 싶어요',
        'choices': ['보고 싶어요', '볼 수 있어요', '보러 가요', '봐 줘요'],
    },
    {
        'text': '<p><strong>A: 한국어로 이야기할 수 있어요?<br>B: 아직 잘 못하지만 조금씩 ________.</strong></p>',
        'hint': '<p>능력 표현입니다.</p>',
        'explanation': '<p><strong>할 수 있어요</strong>: 점점 가능해진다는 의미입니다.</p>',
        'correct': '할 수 있어요',
        'choices': ['하고 싶어요', '할 수 있어요', '하러 가요', '해 줘요'],
    },
    {
        'text': '<p><strong>A: 곧 시험인데 뭐 하고 있어요?<br>B: 친구가 문제를 설명해 ________.</strong></p>',
        'hint': '<p>도움을 받는 표현입니다.</p>',
        'explanation': '<p><strong>주고 있어요</strong>: 상대가 도움을 주고 있는 상황입니다.</p>',
        'correct': '주고 있어요',
        'choices': ['주고 싶어요', '줄 수 있어요', '주러 가요', '주고 있어요'],
    },
    {
        'text': '<p><strong>A: 한복 입어 봤어요?<br>B: 네, 작년에 한국에서 한 번 ________.</strong></p>',
        'hint': '<p>경험 표현입니다.</p>',
        'explanation': '<p><strong>입어 봤어요</strong>: 경험을 나타냅니다.</p>',
        'correct': '입어 봤어요',
        'choices': ['입고 싶어요', '입을 수 있어요', '입으러 가요', '입어 봤어요'],
    },
    {
        'text': '<p><strong>A: 왜 그렇게 기뻐 보여요?<br>B: 드디어 혼자 김치찌개를 만들 ________.</strong></p>',
        'hint': '<p>능력 표현입니다.</p>',
        'explanation': '<p><strong>수 있게 됐어요</strong>: 가능하게 된 상태입니다.</p>',
        'correct': '수 있게 됐어요',
        'choices': ['싶게 됐어요', '수 있게 됐어요', '러 가게 됐어요', '봐 주게 됐어요'],
    },
    {
        'text': '<p><strong>A: 요즘 왜 자주 도서관에 가요?<br>B: 조용히 공부 ________ 가요.</strong></p>',
        'hint': '<p>목적 표현입니다.</p>',
        'explanation': '<p><strong>하러</strong>: 공부 목적입니다.</p>',
        'correct': '하러',
        'choices': ['하고 싶어요', '할 수 있어요', '하러', '해 줘요'],
    },
    {
        'text': '<p><strong>A: 이 음식 먹어 볼래요?<br>B: 네! 전에 한 번도 못 먹어 봐서 꼭 ________.</strong></p>',
        'hint': '<p>희망 + 경험 표현입니다.</p>',
        'explanation': '<p><strong>먹어 보고 싶어요</strong>: 경험해 보고 싶은 마음입니다.</p>',
        'correct': '먹어 보고 싶어요',
        'choices': ['먹어 보고 싶어요', '먹을 수 있어요', '먹으러 가요', '먹어 줘요'],
    },
    {
        'text': '<p><strong>A: 컴퓨터를 고칠 수 있어요?<br>B: 간단한 문제는 제가 ________.</strong></p>',
        'hint': '<p>능력 표현입니다.</p>',
        'explanation': '<p><strong>고칠 수 있어요</strong>: 가능한 능력입니다.</p>',
        'correct': '고칠 수 있어요',
        'choices': ['고치고 싶어요', '고칠 수 있어요', '고치러 가요', '고쳐 줘요'],
    },
    {
        'text': '<p><strong>A: 방금 왜 은행에 갔어요?<br>B: 돈을 ________ 갔어요.</strong></p>',
        'hint': '<p>목적 표현입니다.</p>',
        'explanation': '<p><strong>찾으러</strong>: 돈을 찾는 목적입니다.</p>',
        'correct': '찾으러',
        'choices': ['찾고 싶어요', '찾을 수 있어요', '찾으러', '찾아 줘요'],
    },
    {
        'text': '<p><strong>A: 숙제가 너무 어려워요.<br>B: 제가 같이 ________.</strong></p>',
        'hint': '<p>도움을 주는 표현입니다.</p>',
        'explanation': '<p><strong>해 줄게요</strong>: 상대를 도와주겠다는 뜻입니다.</p>',
        'correct': '해 줄게요',
        'choices': ['하고 싶어요', '할 수 있어요', '하러 가요', '해 줄게요'],
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
            title='고 싶다, -을 수 있다, -러 가다 등 불규칙 활용 연습',
            master=master,
            defaults={
                'description': '고 싶다, -을 수 있다, -러 가다 등 불규칙 활용 연습입니다. 다양한 상황에서 올바른 활용을 선택해 보세요.',
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
