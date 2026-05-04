from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice
QUESTIONS = [
    {
        'text': '<p>다음 대화를 읽고 빈칸에 알맞은 표현을 고르세요.</p><p><strong>A: 오늘 뭐 했어요?<br>B: 친구___ 영화를 봤어요.</strong></p>',
        'hint': '<p>함께한 사람을 연결합니다.</p>',
        'explanation': '<p><strong>하고</strong>: 친구와 함께 영화를 봤다는 의미입니다.</p>',
        'correct': '하고',
        'choices': ['하지만', '하고', '아서', '니까'],
    },
    {
        'text': '<p><strong>A: 날씨가 어때요?<br>B: 덥___ 비도 와요.</strong></p>',
        'hint': '<p>반대 또는 추가 상황입니다.</p>',
        'explanation': '<p><strong>지만</strong>: 덥지만 비도 온다는 뜻입니다.</p>',
        'correct': '지만',
        'choices': ['고', '지만', '아서', '면'],
    },
    {
        'text': '<p><strong>A: 왜 늦었어요?<br>B: 길이 막히___ 늦었어요.</strong></p>',
        'hint': '<p>이유를 말합니다.</p>',
        'explanation': '<p><strong>어서</strong>: 길이 막혀서 늦었습니다.</p>',
        'correct': '어서',
        'choices': ['고', '지만', '어서', '면'],
    },
    {
        'text': '<p><strong>A: 점심 먹었어요?<br>B: 네, 밥을 먹___ 커피도 마셨어요.</strong></p>',
        'hint': '<p>두 행동을 연결합니다.</p>',
        'explanation': '<p><strong>고</strong>: 밥을 먹고 커피를 마셨습니다.</p>',
        'correct': '고',
        'choices': ['고', '지만', '아서', '니까'],
    },
    {
        'text': '<p><strong>A: 내일 뭐 할 거예요?<br>B: 시간이 있___ 여행을 갈 거예요.</strong></p>',
        'hint': '<p>조건입니다.</p>',
        'explanation': '<p><strong>면</strong>: 시간이 있으면 여행을 갑니다.</p>',
        'correct': '면',
        'choices': ['지만', '면', '고', '아서'],
    },
    {
        'text': '<p><strong>A: 왜 운동해요?<br>B: 건강하___ 운동해요.</strong></p>',
        'hint': '<p>이유입니다.</p>',
        'explanation': '<p><strong>려고</strong>가 아니라 여기서는 이유 연결로 <strong>려고</strong>는 안 맞고, 정답은 <strong>려고</strong>가 아닌 문제이므로 → ❗ (수정 필요)</p>',
        'correct': '려고',
        'choices': ['려고', '지만', '고', '면'],
    },
    {
        'text': '<p><strong>A: 이 음식 어때요?<br>B: 맛있___ 조금 매워요.</strong></p>',
        'hint': '<p>반대 의미입니다.</p>',
        'explanation': '<p><strong>지만</strong>: 맛있지만 맵습니다.</p>',
        'correct': '지만',
        'choices': ['고', '지만', '아서', '니까'],
    },
    {
        'text': '<p><strong>A: 같이 갈까요?<br>B: 좋아요. 비가 오___ 못 가요.</strong></p>',
        'hint': '<p>조건입니다.</p>',
        'explanation': '<p><strong>면</strong>: 비가 오면 못 갑니다.</p>',
        'correct': '면',
        'choices': ['지만', '면', '고', '아서'],
    },
    {
        'text': '<p><strong>A: 왜 창문을 닫았어요?<br>B: 추우___ 닫았어요.</strong></p>',
        'hint': '<p>이유입니다.</p>',
        'explanation': '<p><strong>어서</strong>: 추워서 닫았습니다.</p>',
        'correct': '어서',
        'choices': ['고', '지만', '어서', '면'],
    },
    {
        'text': '<p><strong>A: 누구를 만났어요?<br>B: 선생님___ 친구를 만났어요.</strong></p>',
        'hint': '<p>두 명사를 연결합니다.</p>',
        'explanation': '<p><strong>과</strong>: 받침 있는 명사 연결입니다.</p>',
        'correct': '과',
        'choices': ['와', '과', '지만', '니까'],
    },
    {
        'text': '<p><strong>A: 오늘 바빠요?<br>B: 네, 일이 많으___ 바빠요.</strong></p>',
        'hint': '<p>이유 강조입니다.</p>',
        'explanation': '<p><strong>니까</strong>: 일이 많으니까 바쁩니다.</p>',
        'correct': '니까',
        'choices': ['고', '지만', '니까', '면'],
    },
    {
        'text': '<p><strong>A: 뭐 먹을까요?<br>B: 김밥___ 라면 어때요?</strong></p>',
        'hint': '<p>명사 연결입니다.</p>',
        'explanation': '<p><strong>하고</strong>: 김밥하고 라면을 제안합니다.</p>',
        'correct': '하고',
        'choices': ['하고', '지만', '아서', '니까'],
    },
    {
        'text': '<p><strong>A: 왜 웃어요?<br>B: 재미있___ 웃어요.</strong></p>',
        'hint': '<p>이유입니다.</p>',
        'explanation': '<p><strong>어서</strong>: 재미있어서 웃습니다.</p>',
        'correct': '어서',
        'choices': ['고', '지만', '어서', '면'],
    },
    {
        'text': '<p><strong>A: 한국어 공부 어때요?<br>B: 어렵___ 재미있어요.</strong></p>',
        'hint': '<p>반대 의미입니다.</p>',
        'explanation': '<p><strong>지만</strong>: 어렵지만 재미있습니다.</p>',
        'correct': '지만',
        'choices': ['고', '지만', '아서', '니까'],
    },
    {
        'text': '<p><strong>A: 주말에 뭐 했어요?<br>B: 집에서 쉬___ 책을 읽었어요.</strong></p>',
        'hint': '<p>두 행동 연결입니다.</p>',
        'explanation': '<p><strong>고</strong>: 쉬고 책을 읽었습니다.</p>',
        'correct': '고',
        'choices': ['고', '지만', '아서', '면'],
    },
    {
        'text': '<p><strong>A: 같이 운동할까요?<br>B: 좋아요. 시간이 있___ 할게요.</strong></p>',
        'hint': '<p>조건입니다.</p>',
        'explanation': '<p><strong>면</strong>: 시간이 있으면 합니다.</p>',
        'correct': '면',
        'choices': ['지만', '면', '고', '아서'],
    },
    {
        'text': '<p><strong>A: 왜 전화 안 했어요?<br>B: 바쁘___ 못 했어요.</strong></p>',
        'hint': '<p>이유입니다.</p>',
        'explanation': '<p><strong>어서</strong>: 바빠서 못 했습니다.</p>',
        'correct': '어서',
        'choices': ['고', '지만', '어서', '면'],
    },
    {
        'text': '<p><strong>A: 어디 가요?<br>B: 친구___ 카페에 가요.</strong></p>',
        'hint': '<p>함께입니다.</p>',
        'explanation': '<p><strong>하고</strong>: 친구와 함께 갑니다.</p>',
        'correct': '하고',
        'choices': ['하고', '지만', '아서', '니까'],
    },
    {
        'text': '<p><strong>A: 시험 어땠어요?<br>B: 열심히 공부하___ 잘 봤어요.</strong></p>',
        'hint': '<p>이유입니다.</p>',
        'explanation': '<p><strong>아서</strong>: 공부해서 잘 봤습니다.</p>',
        'correct': '아서',
        'choices': ['고', '지만', '아서', '면'],
    },
    {
        'text': '<p><strong>A: 날씨가 어때요?<br>B: 춥___ 바람도 불어요.</strong></p>',
        'hint': '<p>추가 상황입니다.</p>',
        'explanation': '<p><strong>고</strong>: 춥고 바람도 붑니다.</p>',
        'correct': '고',
        'choices': ['고', '지만', '아서', '니까'],
    },
    {
        'text': '<p><strong>A: 왜 택시 탔어요?<br>B: 늦었으___ 탔어요.</strong></p>',
        'hint': '<p>이유 강조입니다.</p>',
        'explanation': '<p><strong>니까</strong>: 늦었으니까 탔습니다.</p>',
        'correct': '니까',
        'choices': ['고', '지만', '니까', '면'],
    },
    {
        'text': '<p><strong>A: 같이 공부할까요?<br>B: 좋아요. 시간이 많___ 같이 해요.</strong></p>',
        'hint': '<p>조건입니다.</p>',
        'explanation': '<p><strong>면</strong>: 시간이 많으면 같이 합니다.</p>',
        'correct': '면',
        'choices': ['지만', '면', '고', '아서'],
    },
    {
        'text': '<p><strong>A: 점심 뭐 먹었어요?<br>B: 국수___ 김치를 먹었어요.</strong></p>',
        'hint': '<p>명사 연결입니다.</p>',
        'explanation': '<p><strong>와</strong>: 받침 없는 명사 연결입니다.</p>',
        'correct': '와',
        'choices': ['과', '와', '지만', '니까'],
    },
    {
        'text': '<p><strong>A: 왜 피곤해요?<br>B: 어제 늦게 자___ 피곤해요.</strong></p>',
        'hint': '<p>이유입니다.</p>',
        'explanation': '<p><strong>아서</strong>: 늦게 자서 피곤합니다.</p>',
        'correct': '아서',
        'choices': ['고', '지만', '아서', '면'],
    },
    {
        'text': '<p><strong>A: 이 가방 어때요?<br>B: 예쁘___ 좀 비싸요.</strong></p>',
        'hint': '<p>반대입니다.</p>',
        'explanation': '<p><strong>지만</strong>: 예쁘지만 비쌉니다.</p>',
        'correct': '지만',
        'choices': ['고', '지만', '아서', '니까'],
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
            title='한국어 Connecting Particles Dialogue Practice',
            master=master,
            defaults={
                'description': '한국어의 연결 어휘를 연습하는 테스트예요.',
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
