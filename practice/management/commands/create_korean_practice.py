from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice
QUESTIONS = [
    {
        'text': '<p>빈칸에 알맞은 표현을 고르세요.</p><p><strong>저는 사과___ 바나나를 샀어요.</strong></p>',
        'hint': '<p>명사와 명사를 연결할 때 사용합니다.</p>',
        'explanation': '<p><strong>하고</strong>: "사과"와 "바나나" 두 명사를 자연스럽게 연결합니다.</p>',
        'correct': '하고',
        'choices': ['하지만', '하고', '어서', '니까'],
    },
    {
        'text': '<p>비가 오___ 집에 있었어요.</p>',
        'hint': '<p>이유를 나타내는 표현입니다.</p>',
        'explanation': '<p><strong>아서</strong>: 비가 온 이유로 집에 있었다는 뜻입니다.</p>',
        'correct': '아서',
        'choices': ['지만', '아서', '고', '면'],
    },
    {
        'text': '<p><strong>한국어는 재미있___ 조금 어려워요.</strong></p>',
        'hint': '<p>앞뒤 내용이 반대일 때 사용합니다.</p>',
        'explanation': '<p><strong>지만</strong>: 재미있지만 어렵다는 반대 의미를 연결합니다.</p>',
        'correct': '지만',
        'choices': ['고', '지만', '아서', '니까'],
    },
    {
        'text': '<p><strong>시간이 없으___ 택시를 탔어요.</strong></p>',
        'hint': '<p>이유를 강조할 때 사용합니다.</p>',
        'explanation': '<p><strong>니까</strong>: 시간이 없어서 택시를 탔다는 이유를 강조합니다.</p>',
        'correct': '니까',
        'choices': ['고', '지만', '니까', '면'],
    },
    {
        'text': '<p><strong>학교에 가___ 친구를 만났어요.</strong></p>',
        'hint': '<p>두 동작이 순서대로 일어납니다.</p>',
        'explanation': '<p><strong>다가</strong>는 아니고, 여기서는 단순 연결이므로 <strong>고</strong>가 맞습니다.</p>',
        'correct': '고',
        'choices': ['고', '지만', '아서', '니까'],
    },
    {
        'text': '<p><strong>돈이 많으___ 여행을 갈 거예요.</strong></p>',
        'hint': '<p>조건을 나타냅니다.</p>',
        'explanation': '<p><strong>면</strong>: 돈이 많을 경우 여행을 간다는 조건입니다.</p>',
        'correct': '면',
        'choices': ['고', '지만', '면', '어서'],
    },
    {
        'text': '<p><strong>책___ 연필을 주세요.</strong></p>',
        'hint': '<p>받침이 있는 명사입니다.</p>',
        'explanation': '<p><strong>과</strong>: "책"은 받침이 있어서 "과"를 사용합니다.</p>',
        'correct': '과',
        'choices': ['와', '과', '하고', '지만'],
    },
    {
        'text': '<p><strong>커피___ 우유를 마셨어요.</strong></p>',
        'hint': '<p>받침이 없는 명사입니다.</p>',
        'explanation': '<p><strong>와</strong>: "커피"는 받침이 없어서 "와"를 사용합니다.</p>',
        'correct': '와',
        'choices': ['과', '와', '지만', '니까'],
    },
    {
        'text': '<p><strong>배가 아프___ 병원에 갔어요.</strong></p>',
        'hint': '<p>이유를 나타냅니다.</p>',
        'explanation': '<p><strong>아서</strong>: 배가 아파서 병원에 갔다는 이유입니다.</p>',
        'correct': '아서',
        'choices': ['고', '지만', '아서', '면'],
    },
    {
        'text': '<p><strong>내일 비가 오___ 집에 있을 거예요.</strong></p>',
        'hint': '<p>조건입니다.</p>',
        'explanation': '<p><strong>면</strong>: 비가 올 경우 집에 있겠다는 뜻입니다.</p>',
        'correct': '면',
        'choices': ['지만', '면', '고', '니까'],
    },
    {
        'text': '<p><strong>아침을 먹___ 학교에 갔어요.</strong></p>',
        'hint': '<p>두 행동의 순서입니다.</p>',
        'explanation': '<p><strong>고</strong>: 먹고 나서 학교에 갔습니다.</p>',
        'correct': '고',
        'choices': ['고', '지만', '아서', '면'],
    },
    {
        'text': '<p><strong>춥___ 창문을 닫았어요.</strong></p>',
        'hint': '<p>이유입니다.</p>',
        'explanation': '<p><strong>아서</strong>: 추워서 창문을 닫았습니다.</p>',
        'correct': '아서',
        'choices': ['지만', '고', '아서', '면'],
    },
    {
        'text': '<p><strong>이 옷은 예쁘___ 너무 비싸요.</strong></p>',
        'hint': '<p>반대 의미입니다.</p>',
        'explanation': '<p><strong>지만</strong>: 예쁘지만 비싸다는 반대 관계입니다.</p>',
        'correct': '지만',
        'choices': ['고', '지만', '아서', '니까'],
    },
    {
        'text': '<p><strong>집에 가___ 쉬고 싶어요.</strong></p>',
        'hint': '<p>두 행동을 연결합니다.</p>',
        'explanation': '<p><strong>고</strong>: 가고 쉬고 싶다는 연결입니다.</p>',
        'correct': '고',
        'choices': ['고', '지만', '아서', '면'],
    },
    {
        'text': '<p><strong>친구___ 영화를 봤어요.</strong></p>',
        'hint': '<p>명사 연결입니다.</p>',
        'explanation': '<p><strong>하고</strong>: 친구와 함께라는 의미입니다.</p>',
        'correct': '하고',
        'choices': ['하고', '지만', '아서', '니까'],
    },
    {
        'text': '<p><strong>시간이 있___ 같이 가요.</strong></p>',
        'hint': '<p>조건입니다.</p>',
        'explanation': '<p><strong>면</strong>: 시간이 있을 경우 함께 가자는 뜻입니다.</p>',
        'correct': '면',
        'choices': ['지만', '면', '고', '아서'],
    },
    {
        'text': '<p><strong>피곤하___ 먼저 잘게요.</strong></p>',
        'hint': '<p>이유 + 말하는 사람의 의지입니다.</p>',
        'explanation': '<p><strong>니까</strong>: 이유를 말하면서 결정을 표현합니다.</p>',
        'correct': '니까',
        'choices': ['고', '지만', '니까', '면'],
    },
    {
        'text': '<p><strong>밥을 먹___ 이를 닦아요.</strong></p>',
        'hint': '<p>순서입니다.</p>',
        'explanation': '<p><strong>고</strong>: 먹고 나서 이를 닦습니다.</p>',
        'correct': '고',
        'choices': ['고', '지만', '아서', '니까'],
    },
    {
        'text': '<p><strong>버스를 타___ 회사에 갔어요.</strong></p>',
        'hint': '<p>이유 또는 방법입니다.</p>',
        'explanation': '<p><strong>아서</strong>: 버스를 타서 갔다는 자연스러운 연결입니다.</p>',
        'correct': '아서',
        'choices': ['지만', '고', '아서', '면'],
    },
    {
        'text': '<p><strong>날씨가 좋___ 산책을 했어요.</strong></p>',
        'hint': '<p>이유입니다.</p>',
        'explanation': '<p><strong>아서</strong>: 날씨가 좋아서 산책했습니다.</p>',
        'correct': '아서',
        'choices': ['지만', '아서', '고', '면'],
    },
    {
        'text': '<p><strong>학생___ 선생님이 있습니다.</strong></p>',
        'hint': '<p>두 명사를 연결합니다.</p>',
        'explanation': '<p><strong>과</strong>: 받침 있는 명사 연결입니다.</p>',
        'correct': '과',
        'choices': ['와', '과', '하지만', '니까'],
    },
    {
        'text': '<p><strong>공부를 열심히 하___ 시험을 잘 봤어요.</strong></p>',
        'hint': '<p>이유입니다.</p>',
        'explanation': '<p><strong>아서</strong>: 공부를 열심히 해서 결과가 좋았습니다.</p>',
        'correct': '아서',
        'choices': ['고', '지만', '아서', '면'],
    },
    {
        'text': '<p><strong>배가 고프___ 밥을 먹어요.</strong></p>',
        'hint': '<p>일반적인 조건입니다.</p>',
        'explanation': '<p><strong>면</strong>: 배가 고플 때 밥을 먹습니다.</p>',
        'correct': '면',
        'choices': ['지만', '면', '고', '아서'],
    },
    {
        'text': '<p><strong>어제 친구___ 만났어요.</strong></p>',
        'hint': '<p>함께라는 의미입니다.</p>',
        'explanation': '<p><strong>하고</strong>: 친구와 만났다는 의미입니다.</p>',
        'correct': '하고',
        'choices': ['하고', '지만', '아서', '니까'],
    },
    {
        'text': '<p><strong>비가 오___ 우산을 가져가세요.</strong></p>',
        'hint': '<p>이유 + 명령문입니다.</p>',
        'explanation': '<p><strong>니까</strong>: 이유를 말하며 권유/명령을 합니다.</p>',
        'correct': '니까',
        'choices': ['고', '지만', '니까', '면'],
    },
    {
        'text': '<p><strong>영화를 보___ 울었어요.</strong></p>',
        'hint': '<p>이유입니다.</p>',
        'explanation': '<p><strong>아서</strong>: 영화를 보고 울었습니다.</p>',
        'correct': '아서',
        'choices': ['고', '지만', '아서', '면'],
    },
    {
        'text': '<p><strong>이 음식은 맛있___ 조금 짜요.</strong></p>',
        'hint': '<p>반대 의미입니다.</p>',
        'explanation': '<p><strong>지만</strong>: 맛있지만 짠 음식입니다.</p>',
        'correct': '지만',
        'choices': ['고', '지만', '아서', '니까'],
    },
    {
        'text': '<p><strong>일을 끝내___ 집에 갈 거예요.</strong></p>',
        'hint': '<p>순서입니다.</p>',
        'explanation': '<p><strong>고</strong>: 일을 끝내고 집에 갑니다.</p>',
        'correct': '고',
        'choices': ['고', '지만', '아서', '면'],
    },
    {
        'text': '<p><strong>지금 바쁘___ 나중에 전화할게요.</strong></p>',
        'hint': '<p>이유입니다.</p>',
        'explanation': '<p><strong>니까</strong>: 바쁜 이유로 나중에 전화합니다.</p>',
        'correct': '니까',
        'choices': ['고', '지만', '니까', '면'],
    },
    {
        'text': '<p><strong>시간이 없___ 못 갔어요.</strong></p>',
        'hint': '<p>이유입니다.</p>',
        'explanation': '<p><strong>어서</strong>: 시간이 없어서 못 갔습니다.</p>',
        'correct': '어서',
        'choices': ['지만', '고', '어서', '면'],
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
            title='한국어 Connecting Particles Practice',
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
