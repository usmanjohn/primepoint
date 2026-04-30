from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
    # 1. present continuous (-고 있다)
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>민수 씨는 지금 도서관에서 책을 읽고 ___.</strong></p>',
        'hint': '<p>\'지금\' 하고 있는 행동을 나타내는 표현을 고르세요.</p>',
        'explanation': '<p><strong>있어요</strong>: "-고 있다"는 현재 진행형입니다. "읽고 있어요"는 지금 읽는 중이라는 뜻입니다.</p>',
        'correct': '있어요',
        'choices': ['있어요', '했어요', '거예요', '보세요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>버스를 10분 동안 기다리고 ___.</strong></p>',
        'hint': '<p>진행 중인 동작(~ing)을 완성해 보세요.</p>',
        'explanation': '<p><strong>있어요</strong>: 기다리는 동작이 계속되고 있으므로 "-고 있어요"가 적절합니다.</p>',
        'correct': '있어요',
        'choices': ['있어요', '싶어요', '이에요', '했어요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>동생은 방에서 공부를 ___ 있어요.</strong></p>',
        'hint': '<p>\'공부하다\'의 진행형은 어떻게 만들까요?</p>',
        'explanation': '<p><strong>하고</strong>: 동사 어간 뒤에 "-고 있다"를 붙여 진행을 나타냅니다.</p>',
        'correct': '하고',
        'choices': ['해', '하고', '해서', '하면'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>지금 사과를 ___ 있어요.</strong></p>',
        'hint': '<p>\'먹다\'를 진행형으로 바꿔보세요.</p>',
        'explanation': '<p><strong>먹고</strong>: "먹다"의 어간 "먹-"에 "-고 있어요"를 연결합니다.</p>',
        'correct': '먹고',
        'choices': ['먹어', '먹고', '먹지', '먹은'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>친구에게 편지를 ___ 있어요.</strong></p>',
        'hint': '<p>\'쓰다\'의 진행형 표현을 찾아보세요.</p>',
        'explanation': '<p><strong>쓰고</strong>: "쓰다"의 어간 "쓰-"에 "-고"를 붙여 진행형을 만듭니다.</p>',
        'correct': '쓰고',
        'choices': ['쓰고', '써서', '쓰면', '썼고'],
    },

    # 2. Future Tense (-(으)ㄹ 거예요)
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>주말에 친구를 ___ 거예요.</strong></p>',
        'hint': '<p>\'만나다\'의 미래 계획을 표현해 보세요.</p>',
        'explanation': '<p><strong>만날</strong>: 받침이 없는 동사 뒤에는 "-ㄹ 거예요"를 사용합니다.</p>',
        'correct': '만날',
        'choices': ['만나', '만나는', '만날', '만났'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>저녁에 비빔밥을 ___ 거예요.</strong></p>',
        'hint': '<p>\'먹다\'에 받침이 있나요?</p>',
        'explanation': '<p><strong>먹을</strong>: 받침이 있는 동사 뒤에는 "-을 거예요"를 사용합니다.</p>',
        'correct': '먹을',
        'choices': ['먹', '먹는', '먹을', '먹은'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>내일 학교에 ___ 거예요.</strong></p>',
        'hint': '<p>\'가다\'의 미래형을 고르세요.</p>',
        'explanation': '<p><strong>갈</strong>: "가다"는 받침이 없으므로 "갈 거예요"가 됩니다.</p>',
        'correct': '갈',
        'choices': ['가', '갈', '갔', '가는'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>내일은 집에서 숙제를 ___ 거예요.</strong></p>',
        'hint': '<p>\'하다\'의 미래형은 무엇일까요?</p>',
        'explanation': '<p><strong>할</strong>: "하다"는 "할 거예요"로 바뀝니다.</p>',
        'correct': '할',
        'choices': ['해', '할', '한', '하고'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>곧 손님이 ___ 거예요.</strong></p>',
        'hint': '<p>\'오다\'의 미래형을 찾아보세요.</p>',
        'explanation': '<p><strong>올</strong>: "오다"는 받침이 없으므로 "올 거예요"가 맞습니다.</p>',
        'correct': '올',
        'choices': ['와', '올', '오는', '와서'],
    },

    # 3. Present Tense (-아요/어요)
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>저는 매일 한국어를 ___.</strong></p>',
        'hint': '<p>\'공부하다\'의 현재형(해요체)은?</p>',
        'explanation': '<p><strong>공부해요</strong>: "-하다" 동사는 "-해요"로 바뀝니다.</p>',
        'correct': '공부해요',
        'choices': ['공부해요', '공부해', '공부하세요', '공부했어요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>동생이 밥을 ___.</strong></p>',
        'hint': '<p>\'먹다\'는 \'아\'가 아니므로 무엇이 올까요?</p>',
        'explanation': '<p><strong>먹어요</strong>: "먹다"의 어간에 "어"가 오므로 "먹어요"가 됩니다.</p>',
        'correct': '먹어요',
        'choices': ['먹아요', '먹어요', '먹해요', '먹요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>학교에 ___.</strong></p>',
        'hint': '<p>\'가다\'를 자연스러운 현재형으로 바꿔보세요.</p>',
        'explanation': '<p><strong>가요</strong>: "가다 + 아요"는 축약되어 "가요"가 됩니다.</p>',
        'correct': '가요',
        'choices': ['가요', '가어요', '가해요', '가이요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>수학이 조금 ___.</strong></p>',
        'hint': '<p>\'어렵다\'의 현재형은?</p>',
        'explanation': '<p><strong>어려워요</strong>: "어렵다"는 "어려워요"로 바뀝니다.</p>',
        'correct': '어려워요',
        'choices': ['어렵아요', '어려워요', '어렵해요', '어렵요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>공책에 이름을 ___.</strong></p>',
        'hint': '<p>\'적다\'의 현재형을 고르세요.</p>',
        'explanation': '<p><strong>적어요</strong>: 어간 "적-"에 "-어요"가 붙습니다.</p>',
        'correct': '적어요',
        'choices': ['적아요', '적어요', '적해요', '적요'],
    },

    # 4. Past Tense (-았/었/했어요)
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>어제 친구를 ___.</strong></p>',
        'hint': '<p>\'만나다\'의 과거형을 찾아보세요.</p>',
        'explanation': '<p><strong>만났어요</strong>: "만나다"의 과거형은 "만났어요"입니다.</p>',
        'correct': '만났어요',
        'choices': ['만나요', '만나겠어요', '만났어요', '만나고 있어요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>아까 밥을 ___.</strong></p>',
        'hint': '<p>\'먹다\'의 과거형은 무엇일까요?</p>',
        'explanation': '<p><strong>먹었어요</strong>: 어간 "먹-" 뒤에 "-었어요"가 붙습니다.</p>',
        'correct': '먹었어요',
        'choices': ['먹어요', '먹었어요', '먹겠어요', '먹고 있어요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>지난주에 시험 공부를 ___.</strong></p>',
        'hint': '<p>\'하다\'의 과거형을 고르세요.</p>',
        'explanation': '<p><strong>했어요</strong>: "-하다"의 과거형은 "-했어요"입니다.</p>',
        'correct': '했어요',
        'choices': ['해요', '했어요', '할 거예요', '하고 있어요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>어제 학교에 안 ___.</strong></p>',
        'hint': '<p>\'가다\'의 과거형을 고르세요.</p>',
        'explanation': '<p><strong>갔어요</strong>: "가다"의 과거형은 "갔어요"입니다.</p>',
        'correct': '갔어요',
        'choices': ['가요', '갔어요', '갈 거예요', '가고 있어요'],
    },
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>어제 집에서 책을 ___.</strong></p>',
        'hint': '<p>\'읽다\'의 과거형을 고르세요.</p>',
        'explanation': '<p><strong>읽었어요</strong>: "읽다"의 어간에 "-었어요"를 붙입니다.</p>',
        'correct': '읽었어요',
        'choices': ['읽어요', '읽었어요', '읽을 거예요', '읽고 있어요'],
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
            defaults={'description': '한국어 문법 및 어휘 연습-tenses'},
        )

        practice, created = Practice.objects.get_or_create(
            title='한국어 tenses',
            master=master,
            defaults={
                'description': '한국어의 기본 tenses를 연습하는 테스트예요.',
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
