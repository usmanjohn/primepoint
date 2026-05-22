from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
    {
        'text': "<p><strong>A: 지민 씨, 혹시 넓은 바다에서 혼자 수영________?<br>B: 네, 저는 어릴 때부터 수영을 배워서 아주 잘해요.</strong></p>",
        'explanation': "<p><strong>할 수 있어요</strong>: 수영을 할 수 있는 능력을 물어보는 상황이므로 <code>V-(으)ㄹ 수 있다</code>를 사용합니다. 하다 → 할 수 있어요 입니다.</p>",
        'correct': "할 수 있어요",
        'choices': ["할 줄 몰라요", "할 수 없어요", "할 수 있어요", "하는 동안"]
    },
    {
        'text': "<p><strong>A: 아름다운 클래식 피아노를 직접 ________?<br>B: 아니요, 한 번도 배운 적이 없어서 전혀 못 해요.</strong></p>",
        'explanation': "<p><strong>칠 줄 알아요</strong>: 피아노를 치는 방법이나 기술을 아는지 물어볼 때 <code>V-(으)ㄹ 줄 알다</code>를 사용합니다. 치다 → 칠 줄 알아요 입니다.</p>",
        'correct': "칠 줄 알아요",
        'choices': ["친 후에", "칠 줄 알아요", "칠 수 없어요", "치기 전에"]
    },
    {
        'text': "<p><strong>A: 떡볶이가 아주 매운데 괜찮으시겠어요?<br>B: 죄송하지만 저는 매운 음식을 전혀 ________. 다른 것을 주문할게요.</strong></p>",
        'explanation': "<p><strong>먹을 수 없어요</strong>: 매운 것을 먹을 능력이 안 된다는 의미로 <code>V-(으)ㄹ 수 없다</code>를 사용합니다. 먹다 → 먹을 수 없어요 입니다.</p>",
        'correct': "먹을 수 없어요",
        'choices': ["먹을 줄 알아요", "먹으면서", "먹자마자", "먹을 수 없어요"]
    },
    {
        'text': "<p><strong>A: 두 발 자전거를 안전하게 ________?<br>B: 네, 주말마다 한강 공원에서 자주 타요.</strong></p>",
        'explanation': "<p><strong>탈 줄 알아요</strong>: 자전거를 타는 방법을 알고 있는지 묻는 것이므로 <code>V-(으)ㄹ 줄 알다</code>를 사용합니다. 타다 → 탈 줄 알아요 입니다.</p>",
        'correct': "탈 줄 알아요",
        'choices': ["탈 줄 알아요", "타는 중이에요", "탈 수 없어요", "탄 지"]
    },
    {
        'text': "<p><strong>A: 이 두꺼운 한국어 신문을 혼자서 ________?<br>B: 한자가 너무 많아서 아직은 혼자 무리예요.</strong></p>",
        'explanation': "<p><strong>읽을 수 있어요</strong>: 신문을 읽을 수 있는 능력이나 가능성을 물어볼 때 <code>V-(으)ㄹ 수 있다</code>를 사용합니다. 읽다 → 읽을 수 있어요 입니다.</p>",
        'correct': "읽을 수 있어요",
        'choices': ["읽을 줄 몰라요", "읽을 수 있어요", "읽기 전에", "읽으면서"]
    },
    {
        'text': "<p><strong>A: 이번 주말에 제주도에서 렌터카를 운전할 사람이 필요해요.<br>B: 걱정 마세요! 제가 안전하게 운전________.</strong></p>",
        'explanation': "<p><strong>할 줄 알아요</strong>: 운전하는 방법을 알고 있다는 의미로 <code>V-(으)ㄹ 줄 알다</code>를 사용합니다. 하다 → 할 줄 알아요 입니다.</p>",
        'correct': "할 줄 알아요",
        'choices': ["할 수 없어요", "하는 동안", "할 줄 알아요", "하고 나서"]
    },
    {
        'text': "<p><strong>A: 자기 이름을 복잡한 한자로 ________?<br>B: 아니요, 쓰는 방법이 너무 어려워서 한글로만 써요.</strong></p>",
        'explanation': "<p><strong>쓸 줄 몰라요</strong>: 한자를 쓰는 방법을 모른다는 의미이므로 <code>V-(으)ㄹ 줄 모르다</code>를 사용합니다. 쓰다 → 쓸 줄 몰라요 입니다. (질문 형태에 대한 대답으로 부정형 사용)</p>",
        'correct': "쓸 줄 몰라요",
        'choices': ["쓸 줄 몰라요", "쓸 수 있어요", "쓰자마자", "쓴 후에"]
    },
    {
        'text': "<p><strong>A: 이 무거운 짐을 혼자서 2층까지 들고 갈 수 있어요?<br>B: 아니요, 너무 무거워서 혼자서는 절대 ________. 도와주세요.</strong></p>",
        'explanation': "<p><strong>들 수 없어요</strong>: 짐을 들 능력이 안 된다는 의미로 <code>V-(으)ㄹ 수 없다</code>를 사용합니다. 들다('ㄹ' 불규칙) → 들 수 없어요 입니다.</p>",
        'correct': "들 수 없어요",
        'choices': ["들 줄 알아요", "드는 중이에요", "들기 전에", "들 수 없어요"]
    },
    {
        'text': "<p><strong>A: 오늘 저녁에 맛있는 김치찌개를 직접 ________?<br>B: 네, 유튜브 영상을 보고 배워서 아주 맛있게 요리해요.</strong></p>",
        'explanation': "<p><strong>끓일 줄 알아요</strong>: 요리하는 방법을 아는지 묻는 상황이므로 <code>V-(으)ㄹ 줄 알다</code>를 사용합니다. 끓이다 → 끓일 줄 알아요 입니다.</p>",
        'correct': "끓일 줄 알아요",
        'choices': ["끓일 수 없어요", "끓일 줄 알아요", "끓이면서", "끓인 지"]
    },
    {
        'text': "<p><strong>A: 저렇게 높고 험한 산을 하루 만에 ________?<br>B: 네, 체력이 좋아서 충분히 가능합니다.</strong></p>",
        'explanation': "<p><strong>오를 수 있어요</strong>: 산에 오를 수 있는 가능성이나 능력을 묻는 상황이므로 <code>V-(으)ㄹ 수 있다</code>를 사용합니다. 오르다 → 오를 수 있어요 입니다.</p>",
        'correct': "오를 수 있어요",
        'choices': ["오른 후에", "오를 줄 몰라요", "오를 수 있어요", "오르는 동안"]
    },
    {
        'text': "<p><strong>A: 겨울 방학에 스키장에서 하얀 눈 위를 멋지게 스키 ________?<br>B: 네, 작년에 기초부터 열심히 배워서 넘어지지 않아요.</strong></p>",
        'explanation': "<p><strong>탈 줄 알아요</strong>: 스키를 타는 기술을 알고 있는지 묻는 상황이므로 <code>V-(으)ㄹ 줄 알다</code>를 사용합니다. 타다 → 탈 줄 알아요 입니다.</p>",
        'correct': "탈 줄 알아요",
        'choices': ["탈 줄 알아요", "탈 수 없어요", "타기 전에", "타자마자"]
    },
    {
        'text': "<p><strong>A: 명절 기차표를 미리 예매했어요?<br>B: 아니요, 표가 순식간에 다 팔려서 아쉽게도 ________.</strong></p>",
        'explanation': "<p><strong>예매할 수 없었어요</strong>: 예매할 수 있는 가능성이 없었다는 의미이므로 <code>V-(으)ㄹ 수 없다</code>의 과거형을 사용합니다. 예매하다 → 예매할 수 없었어요 입니다.</p>",
        'correct': "예매할 수 없었어요",
        'choices': ["예매할 줄 알았어요", "예매하면서", "예매하기 전에", "예매할 수 없었어요"]
    },
    {
        'text': "<p><strong>A: 파티에서 신나게 통기타를 ________?<br>B: 아니요, 음악 학원에 다닌 적이 없어서 코드를 잡을 줄 몰라요.</strong></p>",
        'explanation': "<p><strong>칠 줄 몰라요</strong>: 기타 치는 기술을 모른다는 뜻이므로 <code>V-(으)ㄹ 줄 모르다</code>를 사용합니다. 치다 → 칠 줄 몰라요 입니다.</p>",
        'correct': "칠 줄 몰라요",
        'choices': ["칠 수 있어요", "칠 줄 몰라요", "친 후에", "치는 동안"]
    },
    {
        'text': "<p><strong>A: 내일 중요한 시험이 있어서 오늘 밤을 새워야 해요.<br>B: 저는 졸음이 너무 많아서 밤을 새워서 공부________.</strong></p>",
        'explanation': "<p><strong>할 수 없어요</strong>: 밤을 새워 공부할 능력이 안 된다는 뜻이므로 <code>V-(으)ㄹ 수 없다</code>를 사용합니다. 공부하다 → 공부할 수 없어요 입니다.</p>",
        'correct': "할 수 없어요",
        'choices': ["할 줄 알아요", "하는 중이에요", "할 수 없어요", "하기 전에"]
    },
    {
        'text': "<p><strong>A: 달콤하고 부드러운 딸기 케이크를 오븐에 ________?<br>B: 네, 제과제빵 자격증이 있어서 아주 예쁘게 만들어요.</strong></p>",
        'explanation': "<p><strong>구울 줄 알아요</strong>: 케이크를 굽는 방법을 아는지 묻고 있으므로 <code>V-(으)ㄹ 줄 알다</code>를 사용합니다. 굽다('ㅂ' 불규칙) → 구울 줄 알아요 입니다.</p>",
        'correct': "구울 줄 알아요",
        'choices': ["구울 줄 알아요", "구울 수 없어요", "구우면서", "구운 지"]
    },
    {
        'text': "<p><strong>A: 이 오래되고 고장 난 벽시계를 직접 ________?<br>B: 아니요, 부품이 너무 복잡해서 전문가가 아니면 고치기 힘들어요.</strong></p>",
        'explanation': "<p><strong>고칠 줄 몰라요</strong>: 시계를 고치는 방법을 모른다는 의미이므로 <code>V-(으)ㄹ 줄 모르다</code>를 사용합니다. 고치다 → 고칠 줄 몰라요 입니다.</p>",
        'correct': "고칠 줄 몰라요",
        'choices': ["고칠 수 있어요", "고치는 중이에요", "고치기 전에", "고칠 줄 몰라요"]
    },
    {
        'text': "<p><strong>A: 영어를 아주 유창하게 하시네요! 외국인과 자유롭게 대화________?<br>B: 네, 10년 동안 꾸준히 연습해서 문제없어요.</strong></p>",
        'explanation': "<p><strong>할 수 있어요</strong>: 외국인과 대화할 수 있는 능력을 묻고 있으므로 <code>V-(으)ㄹ 수 있다</code>를 사용합니다. 대화하다 → 대화할 수 있어요 입니다.</p>",
        'correct': "할 수 있어요",
        'choices': ["할 줄 몰라요", "할 수 있어요", "한 후에", "하자마자"]
    },
    {
        'text': "<p><strong>A: 외국인인데 한국 식당에서 쇠젓가락을 능숙하게 ________?<br>B: 네, 한국 친구들에게 정확한 방법을 열심히 배웠거든요.</strong></p>",
        'explanation': "<p><strong>사용할 줄 알아요</strong>: 젓가락을 사용하는 방법을 알고 있다는 뜻이므로 <code>V-(으)ㄹ 줄 알다</code>를 사용합니다. 사용하다 → 사용할 줄 알아요 입니다.</p>",
        'correct': "사용할 줄 알아요",
        'choices': ["사용할 수 없어요", "사용하기 전에", "사용할 줄 알아요", "사용한 지"]
    },
    {
        'text': "<p><strong>A: 매운 고추가 듬뿍 들어간 제육볶음을 ________?<br>B: 네, 저는 매운 음식을 사랑해서 매일매일 먹고 싶어요.</strong></p>",
        'explanation': "<p><strong>먹을 수 있어요</strong>: 매운 음식을 먹을 수 있는 능력을 묻고 있으므로 <code>V-(으)ㄹ 수 있다</code>를 사용합니다. 먹다 → 먹을 수 있어요 입니다.</p>",
        'correct': "먹을 수 있어요",
        'choices': ["먹을 수 있어요", "먹을 줄 몰라요", "먹자마자", "먹으면서"]
    },
    {
        'text': "<p><strong>A: 복잡한 데스크톱 컴퓨터 본체를 직접 ________?<br>B: 아니요, 기계에 대해 전혀 몰라서 설명서를 봐도 못 해요.</strong></p>",
        'explanation': "<p><strong>조립할 줄 몰라요</strong>: 컴퓨터를 조립하는 방법을 모른다는 뜻이므로 <code>V-(으)ㄹ 줄 모르다</code>를 사용합니다. 조립하다 → 조립할 줄 몰라요 입니다.</p>",
        'correct': "조립할 줄 몰라요",
        'choices': ["조립할 수 있어요", "조립한 후에", "조립하는 동안", "조립할 줄 몰라요"]
    },
    {
        'text': "<p><strong>A: 이번 주말에 다 같이 깊은 계곡으로 수영하러 갈까요?<br>B: 저는 물을 너무 무서워해서 깊은 곳에서는 수영________.</strong></p>",
        'explanation': "<p><strong>할 수 없어요</strong>: 수영할 수 있는 능력이 없다는 뜻이므로 <code>V-(으)ㄹ 수 없다</code>를 사용합니다. 하다 → 할 수 없어요 입니다.</p>",
        'correct': "할 수 없어요",
        'choices': ["할 줄 알아요", "할 수 없어요", "하기 전에", "하는 중이에요"]
    },
    {
        'text': "<p><strong>A: 내일 면접을 위해 깔끔한 정장 넥타이를 혼자 ________?<br>B: 네, 아버지가 친절하게 가르쳐 주셔서 완벽하게 해요.</strong></p>",
        'explanation': "<p><strong>맬 줄 알아요</strong>: 넥타이를 매는 방법을 안다는 뜻이므로 <code>V-(으)ㄹ 줄 알다</code>를 사용합니다. 매다 → 맬 줄 알아요 입니다.</p>",
        'correct': "맬 줄 알아요",
        'choices': ["맬 수 없어요", "맨 지", "맬 줄 알아요", "매자마자"]
    },
    {
        'text': "<p><strong>A: 스마트폰 지도 앱 없이 낯선 골목길을 정확히 ________?<br>B: 네, 저는 방향 감각이 뛰어나서 한 번 간 길은 다 기억해요.</strong></p>",
        'explanation': "<p><strong>찾을 수 있어요</strong>: 길을 찾을 수 있는 능력을 묻고 있으므로 <code>V-(으)ㄹ 수 있다</code>를 사용합니다. 찾다 → 찾을 수 있어요 입니다.</p>",
        'correct': "찾을 수 있어요",
        'choices': ["찾을 수 있어요", "찾을 줄 몰라요", "찾는 동안", "찾기 전에"]
    },
    {
        'text': "<p><strong>A: 아이들에게 예쁜 색종이로 아름다운 종이학을 접어줄 수 있어요?<br>B: 미안해요, 어릴 때 안 해봐서 저는 종이접기를 전혀 ________.</strong></p>",
        'explanation': "<p><strong>할 줄 몰라요</strong>: 종이접기 하는 방법을 모른다는 뜻이므로 <code>V-(으)ㄹ 줄 모르다</code>를 사용합니다. 하다 → 할 줄 몰라요 입니다.</p>",
        'correct': "할 줄 몰라요",
        'choices': ["할 수 있어요", "한 후에", "하면서", "할 줄 몰라요"]
    },
    {
        'text': "<p><strong>A: 헬스장에서 저렇게 무거운 100kg 바벨을 번쩍 ________?<br>B: 네, 1년 동안 매일 근력 운동을 해서 이제는 충분히 가능해요.</strong></p>",
        'explanation': "<p><strong>들 수 있어요</strong>: 무거운 것을 들 수 있는 능력을 묻고 있으므로 <code>V-(으)ㄹ 수 있다</code>를 사용합니다. 들다('ㄹ' 불규칙) → 들 수 있어요 입니다.</p>",
        'correct': "들 수 있어요",
        'choices': ["들 줄 몰라요", "들 수 있어요", "들기 전에", "드는 중이에요"]
    }
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
            title='12-dars: Qobiliyat va Imkoniyat',  # --- IGNORE ---
            master=master,
            defaults={
                'description': 'Qobiliyat va Imkoniyat tushunchalarini o\'rganish uchun amaliy test.',
                'subject': subject,
                'level': 'medium',
                'is_free': True,
                'is_published': True,
                'is_available_for_all': True,
                'pass_score': 70,
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
