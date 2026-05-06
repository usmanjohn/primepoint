from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice
QUESTIONS = [
    {
        'text': '<p><strong>저는 ___ 친구를 만났어요.</strong></p>',
        'hint': '<p>과거 시제입니다.</p>',
        'explanation': '<p><strong>어제</strong>: "만났어요"는 과거이므로 어제가 자연스럽습니다.</p>',
        'correct': '어제',
        'choices': ['지금', '어제', '내일', '매일'],
    },
    {
        'text': '<p><strong>저는 ___ 밥을 먹고 있어요.</strong></p>',
        'hint': '<p>지금 진행 중입니다.</p>',
        'explanation': '<p><strong>지금</strong>: "먹고 있어요"는 현재 진행입니다.</p>',
        'correct': '지금',
        'choices': ['어제', '지금', '내일', '지난주'],
    },
    {
        'text': '<p><strong>저는 ___ 여행을 갈 거예요.</strong></p>',
        'hint': '<p>미래입니다.</p>',
        'explanation': '<p><strong>내일</strong>: "갈 거예요"는 미래입니다.</p>',
        'correct': '내일',
        'choices': ['어제', '지금', '내일', '아까'],
    },
    {
        'text': '<p><strong>저는 ___ 학교에 가요.</strong></p>',
        'hint': '<p>습관입니다.</p>',
        'explanation': '<p><strong>매일</strong>: 현재형은 반복 습관과 잘 어울립니다.</p>',
        'correct': '매일',
        'choices': ['어제', '내일', '매일', '아까'],
    },
    {
        'text': '<p><strong>저는 ___ 영화를 봤어요.</strong></p>',
        'hint': '<p>과거입니다.</p>',
        'explanation': '<p><strong>조금 전에</strong>: 과거 시제와 잘 맞습니다.</p>',
        'correct': '조금 전에',
        'choices': ['지금', '내일', '조금 전에', '매일'],
    },
    {
        'text': '<p><strong>저는 ___ 책을 읽고 있어요.</strong></p>',
        'hint': '<p>진행 중입니다.</p>',
        'explanation': '<p><strong>지금</strong>: 진행형과 자연스럽습니다.</p>',
        'correct': '지금',
        'choices': ['어제', '지금', '내일', '지난달'],
    },
    {
        'text': '<p><strong>저는 ___ 운동을 했어요.</strong></p>',
        'hint': '<p>과거입니다.</p>',
        'explanation': '<p><strong>아침에</strong>: 이미 지난 시간입니다.</p>',
        'correct': '아침에',
        'choices': ['지금', '아침에', '내일', '매일'],
    },
    {
        'text': '<p><strong>저는 ___ 친구를 만날 거예요.</strong></p>',
        'hint': '<p>미래입니다.</p>',
        'explanation': '<p><strong>내일</strong>: 미래 계획입니다.</p>',
        'correct': '내일',
        'choices': ['어제', '아까', '내일', '지금'],
    },
    {
        'text': '<p><strong>저는 ___ 음악을 듣고 있어요.</strong></p>',
        'hint': '<p>현재 진행입니다.</p>',
        'explanation': '<p><strong>지금</strong>: 듣고 있는 상황입니다.</p>',
        'correct': '지금',
        'choices': ['어제', '내일', '지금', '작년'],
    },
    {
        'text': '<p><strong>저는 ___ 한국어를 공부했어요.</strong></p>',
        'hint': '<p>과거입니다.</p>',
        'explanation': '<p><strong>지난주</strong>: 과거 시점입니다.</p>',
        'correct': '지난주',
        'choices': ['지금', '내일', '지난주', '매일'],
    },
    {
        'text': '<p><strong>저는 ___ 밥을 먹어요.</strong></p>',
        'hint': '<p>습관입니다.</p>',
        'explanation': '<p><strong>매일</strong>: 반복 행동입니다.</p>',
        'correct': '매일',
        'choices': ['어제', '매일', '내일', '아까'],
    },
    {
        'text': '<p><strong>저는 ___ 친구와 이야기하고 있어요.</strong></p>',
        'hint': '<p>진행 중입니다.</p>',
        'explanation': '<p><strong>지금</strong>: 현재 진행 상황입니다.</p>',
        'correct': '지금',
        'choices': ['어제', '지금', '내일', '지난달'],
    },
    {
        'text': '<p><strong>저는 ___ 영화를 볼 거예요.</strong></p>',
        'hint': '<p>미래입니다.</p>',
        'explanation': '<p><strong>오늘 저녁에</strong>: 앞으로의 계획입니다.</p>',
        'correct': '오늘 저녁에',
        'choices': ['어제', '지금', '오늘 저녁에', '아까'],
    },
    {
        'text': '<p><strong>저는 ___ 숙제를 했어요.</strong></p>',
        'hint': '<p>과거입니다.</p>',
        'explanation': '<p><strong>어제</strong>: 과거 시점입니다.</p>',
        'correct': '어제',
        'choices': ['지금', '내일', '어제', '매일'],
    },
    {
        'text': '<p><strong>저는 ___ TV를 보고 있어요.</strong></p>',
        'hint': '<p>현재 진행입니다.</p>',
        'explanation': '<p><strong>지금</strong>: 현재 상황입니다.</p>',
        'correct': '지금',
        'choices': ['어제', '내일', '지금', '지난주'],
    },
    {
        'text': '<p><strong>저는 ___ 여행을 갔어요.</strong></p>',
        'hint': '<p>과거입니다.</p>',
        'explanation': '<p><strong>작년</strong>: 이미 지난 시간입니다.</p>',
        'correct': '작년',
        'choices': ['지금', '내일', '작년', '매일'],
    },
    {
        'text': '<p><strong>저는 ___ 친구를 만날 거예요.</strong></p>',
        'hint': '<p>미래입니다.</p>',
        'explanation': '<p><strong>다음 주</strong>: 미래 시점입니다.</p>',
        'correct': '다음 주',
        'choices': ['어제', '지금', '다음 주', '아까'],
    },
    {
        'text': '<p><strong>저는 ___ 밥을 먹었어요.</strong></p>',
        'hint': '<p>과거입니다.</p>',
        'explanation': '<p><strong>아까</strong>: 조금 전 과거입니다.</p>',
        'correct': '아까',
        'choices': ['지금', '내일', '아까', '매일'],
    },
    {
        'text': '<p><strong>저는 ___ 공부를 하고 있어요.</strong></p>',
        'hint': '<p>진행입니다.</p>',
        'explanation': '<p><strong>지금</strong>: 진행형과 자연스럽습니다.</p>',
        'correct': '지금',
        'choices': ['어제', '지금', '내일', '작년'],
    },
    {
        'text': '<p><strong>저는 ___ 운동을 할 거예요.</strong></p>',
        'hint': '<p>미래입니다.</p>',
        'explanation': '<p><strong>내일</strong>: 미래 계획입니다.</p>',
        'correct': '내일',
        'choices': ['어제', '지금', '내일', '아까'],
    },
    {
        'text': '<p><strong>저는 ___ 학교에 갔어요.</strong></p>',
        'hint': '<p>과거입니다.</p>',
        'explanation': '<p><strong>아침에</strong>: 이미 지난 시간입니다.</p>',
        'correct': '아침에',
        'choices': ['지금', '아침에', '내일', '매일'],
    },
    {
        'text': '<p><strong>저는 ___ 친구와 이야기해요.</strong></p>',
        'hint': '<p>습관입니다.</p>',
        'explanation': '<p><strong>매일</strong>: 반복 행동입니다.</p>',
        'correct': '매일',
        'choices': ['어제', '매일', '내일', '아까'],
    },
    {
        'text': '<p><strong>저는 ___ 책을 읽었어요.</strong></p>',
        'hint': '<p>과거입니다.</p>',
        'explanation': '<p><strong>지난달</strong>: 과거 시점입니다.</p>',
        'correct': '지난달',
        'choices': ['지금', '내일', '지난달', '매일'],
    },
    {
        'text': '<p><strong>저는 ___ 음악을 들을 거예요.</strong></p>',
        'hint': '<p>미래입니다.</p>',
        'explanation': '<p><strong>오늘 밤에</strong>: 미래 계획입니다.</p>',
        'correct': '오늘 밤에',
        'choices': ['어제', '지금', '오늘 밤에', '아까'],
    },
    {
        'text': '<p><strong>저는 ___ 밥을 먹고 있어요.</strong></p>',
        'hint': '<p>진행입니다.</p>',
        'explanation': '<p><strong>지금</strong>: 현재 진행 상황입니다.</p>',
        'correct': '지금',
        'choices': ['어제', '지금', '내일', '작년'],
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
            title='시간 및 시제 연습',
            master=master,
            defaults={
                'description': '한국어의 시간 및 시제를 연습하는 테스트.',
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
