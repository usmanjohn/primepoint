from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice


QUESTIONS = [
    # ── 이/가 (subject marker) ──────────────────────────────────────────
    {
        'text': '<p>빈칸에 알맞은 조사를 고르세요.</p><p><strong>저___ 학생이에요.</strong></p>',
        'hint': '<p>앞 단어가 모음으로 끝나면 <strong>가</strong>, 받침이 있으면 <strong>이</strong>를 써요.</p>',
        'explanation': '<p><strong>가</strong>: \'저\'는 모음 \'ㅓ\'로 끝나므로 주격 조사 <strong>가</strong>를 사용해요. → "저가 학생이에요."</p>',
        'correct': '가',
        'choices': ['이', '가', '은', '는'],
    },
    {
        'text': '<p>빈칸에 알맞은 조사를 고르세요.</p><p><strong>이 책___ 누구 것이에요?</strong></p>',
        'hint': '<p>\'책\'의 마지막 글자에 받침이 있나요? 받침이 있으면 <strong>이</strong>를 써요.</p>',
        'explanation': '<p><strong>이</strong>: \'책\'은 받침 \'ㄱ\'으로 끝나므로 주격 조사 <strong>이</strong>를 사용해요. → "이 책이 누구 것이에요?"</p>',
        'correct': '이',
        'choices': ['이', '가', '을', '를'],
    },
    {
        'text': '<p>빈칸에 알맞은 조사를 고르세요.</p><p><strong>오늘은 날씨___ 정말 좋아요.</strong></p>',
        'hint': '<p>\'날씨\'의 마지막 글자 \'씨\'에 받침이 있나요?</p>',
        'explanation': '<p><strong>가</strong>: \'날씨\'는 모음 \'ㅣ\'로 끝나므로 주격 조사 <strong>가</strong>를 사용해요. → "날씨가 정말 좋아요."</p>',
        'correct': '가',
        'choices': ['이', '가', '만', '도'],
    },
    {
        'text': '<p>빈칸에 알맞은 조사를 고르세요.</p><p><strong>제 친구___ 노래를 잘해요.</strong></p>',
        'hint': '<p>\'친구\'의 마지막 글자 \'구\'에 받침이 있나요?</p>',
        'explanation': '<p><strong>가</strong>: \'친구\'는 모음 \'ㅜ\'로 끝나므로 주격 조사 <strong>가</strong>를 사용해요. → "제 친구가 노래를 잘해요."</p>',
        'correct': '가',
        'choices': ['이', '가', '의', '는'],
    },
    # ── 은/는 (topic marker) ────────────────────────────────────────────
    {
        'text': '<p>빈칸에 알맞은 조사를 고르세요.</p><p><strong>저___ 매일 운동해요.</strong></p>',
        'hint': '<p>주제를 나타내는 보조사예요. 앞 단어가 모음으로 끝나면 <strong>는</strong>, 받침이 있으면 <strong>은</strong>을 써요.</p>',
        'explanation': '<p><strong>는</strong>: \'저\'는 모음으로 끝나므로 주제 보조사 <strong>는</strong>을 사용해요. → "저는 매일 운동해요."</p>',
        'correct': '는',
        'choices': ['이', '가', '은', '는'],
    },
    {
        'text': '<p>빈칸에 알맞은 조사를 고르세요.</p><p><strong>오늘___ 학교에 안 가요.</strong></p>',
        'hint': '<p>\'오늘\'의 마지막 글자 \'늘\'에 받침이 있나요? 받침이 있으면 <strong>은</strong>을 써요.</p>',
        'explanation': '<p><strong>은</strong>: \'오늘\'은 받침 \'ㄹ\'으로 끝나므로 주제 보조사 <strong>은</strong>을 사용해요. → "오늘은 학교에 안 가요."</p>',
        'correct': '은',
        'choices': ['은', '는', '이', '가'],
    },
    {
        'text': '<p>빈칸에 알맞은 조사를 고르세요.</p><p><strong>한국어___ 정말 재미있어요.</strong></p>',
        'hint': '<p>\'한국어\'의 마지막 글자 \'어\'에 받침이 있나요?</p>',
        'explanation': '<p><strong>는</strong>: \'한국어\'는 모음 \'ㅓ\'로 끝나므로 주제 보조사 <strong>는</strong>을 사용해요. → "한국어는 정말 재미있어요."</p>',
        'correct': '는',
        'choices': ['은', '는', '을', '를'],
    },
    # ── 을/를 (object marker) ───────────────────────────────────────────
    {
        'text': '<p>빈칸에 알맞은 조사를 고르세요.</p><p><strong>저는 밥___ 먹어요.</strong></p>',
        'hint': '<p>목적격 조사예요. \'밥\'에 받침이 있으면 <strong>을</strong>, 없으면 <strong>를</strong>을 써요.</p>',
        'explanation': '<p><strong>을</strong>: \'밥\'은 받침 \'ㅂ\'으로 끝나므로 목적격 조사 <strong>을</strong>을 사용해요. → "저는 밥을 먹어요."</p>',
        'correct': '을',
        'choices': ['이', '가', '을', '를'],
    },
    {
        'text': '<p>빈칸에 알맞은 조사를 고르세요.</p><p><strong>저는 음악___ 들어요.</strong></p>',
        'hint': '<p>\'음악\'의 마지막 글자 \'악\'에 받침 \'ㄱ\'이 있어요. 받침이 있으면 어떤 조사를 쓸까요?</p>',
        'explanation': '<p><strong>을</strong>: \'음악\'은 받침 \'ㄱ\'으로 끝나므로 목적격 조사 <strong>을</strong>을 사용해요. → "저는 음악을 들어요."</p>',
        'correct': '을',
        'choices': ['은', '는', '을', '를'],
    },
    {
        'text': '<p>빈칸에 알맞은 조사를 고르세요.</p><p><strong>저는 한국어___ 공부해요.</strong></p>',
        'hint': '<p>\'한국어\'의 마지막 글자 \'어\'에 받침이 있나요?</p>',
        'explanation': '<p><strong>를</strong>: \'한국어\'는 모음 \'ㅓ\'로 끝나므로 목적격 조사 <strong>를</strong>을 사용해요. → "저는 한국어를 공부해요."</p>',
        'correct': '를',
        'choices': ['이', '가', '을', '를'],
    },
    {
        'text': '<p>빈칸에 알맞은 조사를 고르세요.</p><p><strong>아이가 물___ 마셔요.</strong></p>',
        'hint': '<p>\'물\'의 마지막 글자에 받침 \'ㄹ\'이 있어요. 받침이 있으면 <strong>을</strong>을 써요.</p>',
        'explanation': '<p><strong>을</strong>: \'물\'은 받침 \'ㄹ\'으로 끝나므로 목적격 조사 <strong>을</strong>을 사용해요. → "아이가 물을 마셔요."</p>',
        'correct': '을',
        'choices': ['을', '를', '만', '도'],
    },
    # ── -만 (only) ──────────────────────────────────────────────────────
    {
        'text': '<p>빈칸에 알맞은 조사를 고르세요.</p><p><strong>저는 커피___ 마셔요. 다른 음료는 마시지 않아요.</strong></p>',
        'hint': '<p>"오직 그것뿐"이라는 의미로 다른 것을 제외할 때 쓰는 보조사예요.</p>',
        'explanation': '<p><strong>만</strong>: \'-만\'은 한정을 나타내는 보조사예요. "커피만 마셔요" = 커피를 마시고 다른 음료는 마시지 않아요.</p>',
        'correct': '만',
        'choices': ['만', '도', '의', '은'],
    },
    {
        'text': '<p>빈칸에 알맞은 조사를 고르세요.</p><p><strong>저는 한국어___ 배워요. 다른 언어는 배우지 않아요.</strong></p>',
        'hint': '<p>특정 하나만을 강조하고 나머지를 제외할 때 쓰는 보조사예요.</p>',
        'explanation': '<p><strong>만</strong>: \'-만\'은 "오직 ~뿐"이라는 의미예요. "한국어만 배워요" = 한국어를 배우고 다른 언어는 배우지 않아요.</p>',
        'correct': '만',
        'choices': ['만', '도', '를', '의'],
    },
    {
        'text': '<p>빈칸에 알맞은 조사를 고르세요.</p><p><strong>오늘___ 쉬고 싶어요. 내일부터 다시 열심히 할 거예요.</strong></p>',
        'hint': '<p>"오늘 하루만"이라는 시간 한정의 의미가 필요해요.</p>',
        'explanation': '<p><strong>만</strong>: \'-만\'은 시간에도 쓸 수 있어요. "오늘만 쉬고 싶어요" = 오늘 하루만 쉬고, 내일부터는 다시 일해요.</p>',
        'correct': '만',
        'choices': ['은', '만', '도', '의'],
    },
    # ── -도 (also / too) ────────────────────────────────────────────────
    {
        'text': '<p>빈칸에 알맞은 조사를 고르세요.</p><p><strong>저는 사과를 좋아해요. 바나나___ 좋아해요.</strong></p>',
        'hint': '<p>"~도 마찬가지", "게다가 ~도"라는 의미를 나타내는 보조사예요.</p>',
        'explanation': '<p><strong>도</strong>: \'-도\'는 첨가를 나타내요. "바나나도 좋아해요" = 사과를 좋아하고, 게다가 바나나도 좋아해요.</p>',
        'correct': '도',
        'choices': ['만', '도', '의', '이'],
    },
    {
        'text': '<p>빈칸에 알맞은 조사를 고르세요.</p><p><strong>오빠가 한국어를 배워요. 저___ 한국어를 배워요.</strong></p>',
        'hint': '<p>앞에서 언급한 것과 같은 행동이나 상태를 나타낼 때 써요.</p>',
        'explanation': '<p><strong>도</strong>: \'-도\'는 "마찬가지로"라는 의미예요. "저도 배워요" = 오빠처럼 나도 한국어를 배워요.</p>',
        'correct': '도',
        'choices': ['만', '도', '는', '가'],
    },
    {
        'text': '<p>빈칸에 알맞은 조사를 고르세요.</p><p><strong>한국어가 어려워요. 일본어___ 어려워요.</strong></p>',
        'hint': '<p>"이것 역시"라는 의미를 나타내는 보조사예요.</p>',
        'explanation': '<p><strong>도</strong>: \'-도\'는 앞서 언급한 것에 더해 이것도 포함됨을 나타내요. "일본어도 어려워요" = 한국어처럼 일본어도 어려워요.</p>',
        'correct': '도',
        'choices': ['만', '도', '를', '의'],
    },
    # ── -의 (possessive) ────────────────────────────────────────────────
    {
        'text': '<p>빈칸에 알맞은 조사를 고르세요.</p><p><strong>이것은 제 친구___ 가방이에요.</strong></p>',
        'hint': '<p>소유나 소속 관계를 나타내는 조사예요. 영어의 <em>\'s</em>와 비슷해요.</p>',
        'explanation': '<p><strong>의</strong>: \'-의\'는 소유격 조사예요. "친구의 가방" = 친구가 소유한 가방이에요.</p>',
        'correct': '의',
        'choices': ['가', '이', '의', '는'],
    },
    {
        'text': '<p>빈칸에 알맞은 조사를 고르세요.</p><p><strong>우리나라___ 음식은 정말 맛있어요.</strong></p>',
        'hint': '<p>"~에 속하는", "~의 것"이라는 소속 관계를 나타내요.</p>',
        'explanation': '<p><strong>의</strong>: \'-의\'는 소속 관계를 나타내요. "우리나라의 음식" = 우리나라에 속하는 음식이에요.</p>',
        'correct': '의',
        'choices': ['의', '를', '이', '가'],
    },
    {
        'text': '<p>빈칸에 알맞은 조사를 고르세요.</p><p><strong>이 사진은 선생님___ 것이에요.</strong></p>',
        'hint': '<p>누구의 것인지를 나타내는 조사예요.</p>',
        'explanation': '<p><strong>의</strong>: \'-의\'는 소유를 나타내는 조사예요. "선생님의 것" = 선생님이 소유한 것이에요.</p>',
        'correct': '의',
        'choices': ['만', '도', '의', '이'],
    },
]


class Command(BaseCommand):
    help = 'Create a Korean grammar particle practice test (이/가, 은/는, 을/를, -만, -도, -의)'

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
            title='한국어 조사 연습 (이/가, 은/는, 을/를, -만, -도, -의)',
            master=master,
            defaults={
                'description': '한국어의 기본 조사 이/가, 은/는, 을/를, -만, -도, -의를 연습하는 테스트예요.',
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
