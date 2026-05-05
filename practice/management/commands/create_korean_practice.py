from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
    {
        'text': '<p><strong>학교에 ___ 친구를 만났어요.</strong></p>',
        'hint': '<p>장소 이동 후 결과입니다.</p>',
        'explanation': '<p><strong>가서</strong>: 학교에 가서 그곳에서 친구를 만났습니다.</p>',
        'correct': '가서',
        'choices': ['가서', '가니까', '가면', '갔어요'],
    },
    {
        'text': '<p><strong>밥을 ___ 이를 닦아요.</strong></p>',
        'hint': '<p>두 행동의 순서입니다.</p>',
        'explanation': '<p><strong>먹고</strong>: 밥을 먹고 나서 이를 닦습니다.</p>',
        'correct': '먹고',
        'choices': ['먹고', '먹으니까', '먹으면', '먹었어요'],
    },
    {
        'text': '<p><strong>비가 ___ 우산을 가져가세요.</strong></p>',
        'hint': '<p>이유 + 명령문입니다.</p>',
        'explanation': '<p><strong>오니까</strong>: 비가 오니까 우산을 가져가세요.</p>',
        'correct': '오니까',
        'choices': ['오니까', '오면', '와서', '왔어요'],
    },
    {
        'text': '<p><strong>시간이 ___ 같이 영화 봐요.</strong></p>',
        'hint': '<p>조건입니다.</p>',
        'explanation': '<p><strong>있으면</strong>: 시간이 있으면 같이 봅니다.</p>',
        'correct': '있으면',
        'choices': ['있으면', '있으니까', '있어서', '있어요'],
    },
    {
        'text': '<p><strong>어제 늦게 ___ 피곤해요.</strong></p>',
        'hint': '<p>이유입니다.</p>',
        'explanation': '<p><strong>자서</strong>: 늦게 자서 피곤합니다.</p>',
        'correct': '자서',
        'choices': ['자서', '자니까', '자면', '잤어요'],
    },
    {
        'text': '<p><strong>이 음식은 ___ 좀 짜요.</strong></p>',
        'hint': '<p>반대 의미입니다.</p>',
        'explanation': '<p><strong>맛있지만</strong>: 맛있지만 짭니다.</p>',
        'correct': '맛있지만',
        'choices': ['맛있지만', '맛있어서', '맛있으니까', '맛있으면'],
    },
    {
        'text': '<p><strong>돈이 ___ 여행을 갈 거예요.</strong></p>',
        'hint': '<p>조건입니다.</p>',
        'explanation': '<p><strong>있으면</strong>: 돈이 있으면 여행을 갑니다.</p>',
        'correct': '있으면',
        'choices': ['있으면', '있으니까', '있어서', '있어요'],
    },
    {
        'text': '<p><strong>버스를 ___ 회사에 갔어요.</strong></p>',
        'hint': '<p>방법입니다.</p>',
        'explanation': '<p><strong>타고</strong>: 버스를 타고 갔습니다.</p>',
        'correct': '타고',
        'choices': ['타고', '타니까', '타면', '탔어요'],
    },
    {
        'text': '<p><strong>길이 ___ 늦었어요.</strong></p>',
        'hint': '<p>이유입니다.</p>',
        'explanation': '<p><strong>막혀서</strong>: 길이 막혀서 늦었습니다.</p>',
        'correct': '막혀서',
        'choices': ['막혀서', '막히니까', '막히면', '막혔어요'],
    },
    {
        'text': '<p><strong>한국어를 열심히 공부하___ 잘하고 싶어요.</strong></p>',
        'hint': '<p>두 행동 연결입니다.</p>',
        'explanation': '<p><strong>고</strong>: 공부하고 잘하고 싶습니다.</p>',
        'correct': '고',
        'choices': ['고', '아서', '니까', '면'],
    },
    {
        'text': '<p><strong>날씨가 ___ 산책을 했어요.</strong></p>',
        'hint': '<p>이유입니다.</p>',
        'explanation': '<p><strong>좋아서</strong>: 날씨가 좋아서 산책했습니다.</p>',
        'correct': '좋아서',
        'choices': ['좋아서', '좋으니까', '좋으면', '좋아요'],
    },
    {
        'text': '<p><strong>피곤하___ 먼저 잘게요.</strong></p>',
        'hint': '<p>이유 + 의지입니다.</p>',
        'explanation': '<p><strong>니까</strong>: 피곤하니까 먼저 자겠습니다.</p>',
        'correct': '니까',
        'choices': ['고', '아서', '니까', '면'],
    },
    {
        'text': '<p><strong>아침을 ___ 학교에 갔어요.</strong></p>',
        'hint': '<p>순서입니다.</p>',
        'explanation': '<p><strong>먹고</strong>: 먹고 나서 갔습니다.</p>',
        'correct': '먹고',
        'choices': ['먹고', '먹으니까', '먹으면', '먹었어요'],
    },
    {
        'text': '<p><strong>비가 ___ 집에 있었어요.</strong></p>',
        'hint': '<p>이유입니다.</p>',
        'explanation': '<p><strong>와서</strong>: 비가 와서 집에 있었습니다.</p>',
        'correct': '와서',
        'choices': ['와서', '오니까', '오면', '왔어요'],
    },
    {
        'text': '<p><strong>시간이 ___ 택시를 탔어요.</strong></p>',
        'hint': '<p>이유입니다.</p>',
        'explanation': '<p><strong>없어서</strong>: 시간이 없어서 택시를 탔습니다.</p>',
        'correct': '없어서',
        'choices': ['없어서', '없으니까', '없으면', '없어요'],
    },
    {
        'text': '<p><strong>친구를 ___ 같이 밥을 먹었어요.</strong></p>',
        'hint': '<p>순서 + 결과입니다.</p>',
        'explanation': '<p><strong>만나서</strong>: 만나서 같이 먹었습니다.</p>',
        'correct': '만나서',
        'choices': ['만나서', '만나니까', '만나면', '만났어요'],
    },
    {
        'text': '<p><strong>시험이 ___ 잘 못 봤어요.</strong></p>',
        'hint': '<p>이유입니다.</p>',
        'explanation': '<p><strong>어려워서</strong>: 시험이 어려워서 잘 못 봤습니다.</p>',
        'correct': '어려워서',
        'choices': ['어렵고', '어려워서', '어려우니까', '어려우면'],
    },
    {
        'text': '<p><strong>지금 바쁘___ 나중에 전화할게요.</strong></p>',
        'hint': '<p>이유입니다.</p>',
        'explanation': '<p><strong>니까</strong>: 바쁘니까 나중에 전화하겠습니다.</p>',
        'correct': '니까',
        'choices': ['고', '어서', '니까', '면'],
    },
    {
        'text': '<p><strong>돈을 많이 벌___ 집을 사고 싶어요.</strong></p>',
        'hint': '<p>조건입니다.</p>',
        'explanation': '<p><strong>면</strong>: 많이 벌면 사고 싶습니다.</p>',
        'correct': '면',
        'choices': ['고', '어서', '니까', '면'],
    },
    {
        'text': '<p><strong>운동을 ___ 건강해졌어요.</strong></p>',
        'hint': '<p>이유/결과입니다.</p>',
        'explanation': '<p><strong>해서</strong>: 운동을 해서 건강해졌습니다.</p>',
        'correct': '해서',
        'choices': ['하고', '해서', '하니까', '하면'],
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
            title='한국어 연결 어휘 연습',
            master=master,
            defaults={
                'description': '한국어의 연결 어휘를 연습하는 테스트.',
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
