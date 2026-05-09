from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice
QUESTIONS = [
    {
        'text': '<p>다음 대화를 읽고 알맞은 표현을 고르세요.</p><p><strong>A: 어제 저녁에 뭐 했어요?<br>B: 음악을 ________. (듣다)</strong></p>',
        'hint': '<p>"어제 저녁"은 과거 표현입니다.</p>',
        'explanation': '<p><strong>들었어요</strong>: "듣다"는 ㄷ 불규칙입니다.</p>',
        'correct': '들었어요',
        'choices': ['듣어요', '들었어요', '듣고 있어요', '들을 거예요'],
    },
    {
        'text': '<p><strong>A: 지금 뭐 해요?<br>B: 공원에서 ________ 있어요. (걷다)</strong></p>',
        'hint': '<p>"지금"은 현재 진행입니다.</p>',
        'explanation': '<p><strong>걷고</strong>: 진행형에서는 "걷고 있어요"를 사용합니다.</p>',
        'correct': '걷고',
        'choices': ['걸어요', '걸었어요', '걷고', '걸을 거예요'],
    },
    {
        'text': '<p><strong>A: 내일 선생님께 질문할 거예요?<br>B: 네, 내일 꼭 ________. (묻다)</strong></p>',
        'hint': '<p>"내일"은 미래 표현입니다.</p>',
        'explanation': '<p><strong>물을 거예요</strong>: "묻다"는 ㄷ 불규칙입니다.</p>',
        'correct': '물을 거예요',
        'choices': ['물어요', '물었어요', '묻고 있어요', '물을 거예요'],
    },
    {
        'text': '<p><strong>A: 요즘 날씨가 어때요?<br>B: 정말 ________.</strong></p>',
        'hint': '<p>현재 상태입니다.</p>',
        'explanation': '<p><strong>추워요</strong>: "춥다"는 ㅂ 불규칙입니다.</p>',
        'correct': '추워요',
        'choices': ['춥어요', '추워요', '추웠어요', '추울 거예요'],
    },
    {
        'text': '<p><strong>A: 어제 음식이 어땠어요?<br>B: 너무 ________.</strong></p>',
        'hint': '<p>"어제"는 과거입니다.</p>',
        'explanation': '<p><strong>매웠어요</strong>: "맵다"는 ㅂ 불규칙입니다.</p>',
        'correct': '매웠어요',
        'choices': ['매워요', '매웠어요', '맵고 있어요', '매울 거예요'],
    },
    {
        'text': '<p><strong>A: 지금 뭐 만들어요?<br>B: 집을 ________ 있어요. (짓다)</strong></p>',
        'hint': '<p>현재 진행입니다.</p>',
        'explanation': '<p><strong>짓고</strong>: 진행형에서는 "짓고 있어요"를 사용합니다.</p>',
        'correct': '짓고',
        'choices': ['지어요', '지었어요', '짓고', '지을 거예요'],
    },
    {
        'text': '<p><strong>A: 조금 전에 왜 병원에 갔어요?<br>B: 머리가 아파서 약을 ________. (짓다)</strong></p>',
        'hint': '<p>"조금 전에"는 과거입니다.</p>',
        'explanation': '<p><strong>지었어요</strong>: "짓다"의 과거형입니다.</p>',
        'correct': '지었어요',
        'choices': ['지어요', '지었어요', '짓고 있어요', '지을 거예요'],
    },
    {
        'text': '<p><strong>A: 다음 달에 뭐 할 거예요?<br>B: 새로운 컴퓨터를 ________. (팔다)</strong></p>',
        'hint': '<p>"다음 달"은 미래입니다.</p>',
        'explanation': '<p><strong>팔 거예요</strong>: ㄹ 탈락이 일어납니다.</p>',
        'correct': '팔 거예요',
        'choices': ['팔아요', '팔았어요', '팔고 있어요', '팔 거예요'],
    },
    {
        'text': '<p><strong>A: 오늘 아침에 뭐 했어요?<br>B: 동생을 ________. (부르다)</strong></p>',
        'hint': '<p>"오늘 아침"은 과거입니다.</p>',
        'explanation': '<p><strong>불렀어요</strong>: 르 불규칙입니다.</p>',
        'correct': '불렀어요',
        'choices': ['불러요', '불렀어요', '부르고 있어요', '부를 거예요'],
    },
    {
        'text': '<p><strong>A: 지금 뭐 써요?<br>B: 숙제를 ________ 있어요. (쓰다)</strong></p>',
        'hint': '<p>현재 진행입니다.</p>',
        'explanation': '<p><strong>쓰고</strong>: 진행형입니다.</p>',
        'correct': '쓰고',
        'choices': ['써요', '썼어요', '쓰고', '쓸 거예요'],
    },
    {
        'text': '<p><strong>A: 어제 왜 울었어요?<br>B: 너무 ________.</strong></p>',
        'hint': '<p>과거 감정입니다.</p>',
        'explanation': '<p><strong>슬펐어요</strong>: "슬프다"는 ㅡ 탈락입니다.</p>',
        'correct': '슬펐어요',
        'choices': ['슬퍼요', '슬펐어요', '슬프고 있어요', '슬플 거예요'],
    },
    {
        'text': '<p><strong>A: 요즘 한국어 공부가 어때요?<br>B: 아직 조금 ________.</strong></p>',
        'hint': '<p>현재 상태입니다.</p>',
        'explanation': '<p><strong>어려워요</strong>: ㅂ 불규칙입니다.</p>',
        'correct': '어려워요',
        'choices': ['어렵어요', '어려워요', '어려웠어요', '어려울 거예요'],
    },
    {
        'text': '<p><strong>A: 지금 뭐 하고 있어요?<br>B: 불을 ________ 있어요. (끄다)</strong></p>',
        'hint': '<p>진행형입니다.</p>',
        'explanation': '<p><strong>끄고</strong>: 진행형에서는 기본형을 사용합니다.</p>',
        'correct': '끄고',
        'choices': ['꺼요', '껐어요', '끄고', '끌 거예요'],
    },
    {
        'text': '<p><strong>A: 어제 운동했어요?<br>B: 네, 공원에서 많이 ________. (걷다)</strong></p>',
        'hint': '<p>"어제"는 과거입니다.</p>',
        'explanation': '<p><strong>걸었어요</strong>: ㄷ 불규칙입니다.</p>',
        'correct': '걸었어요',
        'choices': ['걸어요', '걸었어요', '걷고 있어요', '걸을 거예요'],
    },
    {
        'text': '<p><strong>A: 내년에 한국에 갈 거예요?<br>B: 네, 한국어를 더 ________ 거예요. (배우다)</strong></p>',
        'hint': '<p>"내년"은 미래입니다.</p>',
        'explanation': '<p><strong>배울</strong>: 미래형입니다.</p>',
        'correct': '배울',
        'choices': ['배워요', '배웠어요', '배우고 있어요', '배울'],
    },
    {
        'text': '<p><strong>A: 아까 왜 창문을 닫았어요?<br>B: 너무 ________.</strong></p>',
        'hint': '<p>과거 이유입니다.</p>',
        'explanation': '<p><strong>더웠어요</strong>: "덥다"의 과거형입니다.</p>',
        'correct': '더웠어요',
        'choices': ['더워요', '더웠어요', '덥고 있어요', '더울 거예요'],
    },
    {
        'text': '<p><strong>A: 지금 누구를 도와줘요?<br>B: 친구를 ________ 있어요. (돕다)</strong></p>',
        'hint': '<p>현재 진행입니다.</p>',
        'explanation': '<p><strong>돕고</strong>: 진행형입니다.</p>',
        'correct': '돕고',
        'choices': ['도와요', '도왔어요', '돕고', '도울 거예요'],
    },
    {
        'text': '<p><strong>A: 방금 뭐 했어요?<br>B: 이메일을 ________. (쓰다)</strong></p>',
        'hint': '<p>"방금"은 과거입니다.</p>',
        'explanation': '<p><strong>썼어요</strong>: ㅡ 탈락 과거형입니다.</p>',
        'correct': '썼어요',
        'choices': ['써요', '썼어요', '쓰고 있어요', '쓸 거예요'],
    },
    {
        'text': '<p><strong>A: 다음 주에 뭐 살 거예요?<br>B: 가벼운 가방을 ________ 거예요.</strong></p>',
        'hint': '<p>미래 계획입니다.</p>',
        'explanation': '<p><strong>살</strong>: 미래 관형형입니다.</p>',
        'correct': '살',
        'choices': ['사요', '샀어요', '살고 있어요', '살'],
    },
    {
        'text': '<p><strong>A: 요즘 왜 바빠요?<br>B: 프로젝트를 ________ 있어요. (만들다)</strong></p>',
        'hint': '<p>진행형입니다.</p>',
        'explanation': '<p><strong>만들고</strong>: 진행형입니다.</p>',
        'correct': '만들고',
        'choices': ['만들어요', '만들었어요', '만들고', '만들 거예요'],
    },
    {
        'text': '<p><strong>A: 지난달에 무엇을 배웠어요?<br>B: 새로운 사실을 많이 ________. (깨닫다)</strong></p>',
        'hint': '<p>과거 경험입니다.</p>',
        'explanation': '<p><strong>깨달았어요</strong>: ㄷ 불규칙입니다.</p>',
        'correct': '깨달았어요',
        'choices': ['깨달아요', '깨달았어요', '깨닫고 있어요', '깨달을 거예요'],
    },
    {
        'text': '<p><strong>A: 오늘 저녁에 뭐 먹을 거예요?<br>B: 엄마가 김치를 ________ 거예요. (짓다)</strong></p>',
        'hint': '<p>미래입니다.</p>',
        'explanation': '<p><strong>지을</strong>: "짓다"의 미래형입니다.</p>',
        'correct': '지을',
        'choices': ['지어요', '지었어요', '짓고 있어요', '지을'],
    },
    {
        'text': '<p><strong>A: 지금 뭐 입고 있어요?<br>B: 조금 ________ 옷을 입고 있어요.</strong></p>',
        'hint': '<p>현재 상태입니다.</p>',
        'explanation': '<p><strong>무거운</strong>: "무겁다" 활용입니다.</p>',
        'correct': '무거운',
        'choices': ['무거운', '무거웠어요', '무겁고 있어요', '무거울 거예요'],
    },
    {
        'text': '<p><strong>A: 어제 숙제가 많았어요?<br>B: 네, 정말 ________.</strong></p>',
        'hint': '<p>과거 상태입니다.</p>',
        'explanation': '<p><strong>바빴어요</strong>: ㅡ 탈락 과거형입니다.</p>',
        'correct': '바빴어요',
        'choices': ['바빠요', '바빴어요', '바쁘고 있어요', '바쁠 거예요'],
    },
    {
        'text': '<p><strong>A: 지금 무엇을 배우고 있어요?<br>B: 피아노를 ________ 있어요. (배우다)</strong></p>',
        'hint': '<p>진행형입니다.</p>',
        'explanation': '<p><strong>배우고</strong>: 진행형입니다.</p>',
        'correct': '배우고',
        'choices': ['배워요', '배웠어요', '배우고', '배울 거예요'],
    },
    {
        'text': '<p><strong>A: 내일 누구를 만날 거예요?<br>B: 한국에서 ________ 친구를 만날 거예요. (살다)</strong></p>',
        'hint': '<p>관형형입니다.</p>',
        'explanation': '<p><strong>사는</strong>: ㄹ 탈락 관형형입니다.</p>',
        'correct': '사는',
        'choices': ['살아요', '살았어요', '살고 있어요', '사는'],
    },
    {
        'text': '<p><strong>A: 요즘 기분이 어때요?<br>B: 아주 ________.</strong></p>',
        'hint': '<p>현재 상태입니다.</p>',
        'explanation': '<p><strong>고마워요</strong>: ㅂ 불규칙입니다.</p>',
        'correct': '고마워요',
        'choices': ['고맙어요', '고마워요', '고마웠어요', '고마울 거예요'],
    },
    {
        'text': '<p><strong>A: 아까 왜 약을 먹었어요?<br>B: 배가 너무 ________.</strong></p>',
        'hint': '<p>과거 상태입니다.</p>',
        'explanation': '<p><strong>아팠어요</strong>: ㅡ 탈락 과거형입니다.</p>',
        'correct': '아팠어요',
        'choices': ['아파요', '아팠어요', '아프고 있어요', '아플 거예요'],
    },
    {
        'text': '<p><strong>A: 다음 달에 어디에서 살 거예요?<br>B: 서울에서 ________ 거예요. (살다)</strong></p>',
        'hint': '<p>미래입니다.</p>',
        'explanation': '<p><strong>살</strong>: 미래형입니다.</p>',
        'correct': '살',
        'choices': ['사요', '살았어요', '살고 있어요', '살'],
    },
    {
        'text': '<p><strong>A: 지금 왜 웃어요?<br>B: 영화가 정말 ________.</strong></p>',
        'hint': '<p>현재 상태입니다.</p>',
        'explanation': '<p><strong>재미있어요</strong>: 현재형입니다.</p>',
        'correct': '재미있어요',
        'choices': ['재미있어요', '재미있었어요', '재미있고 있어요', '재미있을 거예요'],
    },
    {
        'text': '<p><strong>A: 지난주에 뭐 샀어요?<br>B: 조금 ________ 컴퓨터를 샀어요.</strong></p>',
        'hint': '<p>형용사 활용입니다.</p>',
        'explanation': '<p><strong>무거운</strong>: "무겁다" 활용입니다.</p>',
        'correct': '무거운',
        'choices': ['무거운', '무거웠어요', '무겁고 있어요', '무거울 거예요'],
    },
    {
        'text': '<p><strong>A: 지금 뭐 골라요?<br>B: 옷을 ________ 있어요. (고르다)</strong></p>',
        'hint': '<p>진행형입니다.</p>',
        'explanation': '<p><strong>고르고</strong>: 진행형입니다.</p>',
        'correct': '고르고',
        'choices': ['골라요', '골랐어요', '고르고', '고를 거예요'],
    },
    {
        'text': '<p><strong>A: 어제 왜 늦었어요?<br>B: 길이 너무 ________.</strong></p>',
        'hint': '<p>과거 상태입니다.</p>',
        'explanation': '<p><strong>멀었어요</strong>: "멀다"의 과거형입니다.</p>',
        'correct': '멀었어요',
        'choices': ['멀어요', '멀었어요', '멀고 있어요', '멀 거예요'],
    },
    {
        'text': '<p><strong>A: 지금 누구를 알아요?<br>B: 한국에서 ________ 사람을 알아요. (살다)</strong></p>',
        'hint': '<p>관형형입니다.</p>',
        'explanation': '<p><strong>사는</strong>: 관형형입니다.</p>',
        'correct': '사는',
        'choices': ['살아요', '살았어요', '살고 있어요', '사는'],
    },
    {
        'text': '<p><strong>A: 내일 뭐 할 거예요?<br>B: 친구를 ________ 거예요. (돕다)</strong></p>',
        'hint': '<p>미래 표현입니다.</p>',
        'explanation': '<p><strong>도울</strong>: "돕다"의 미래형입니다.</p>',
        'correct': '도울',
        'choices': ['도와요', '도왔어요', '돕고 있어요', '도울'],
    },
    {
        'text': '<p><strong>A: 방금 왜 물을 마셨어요?<br>B: 음식이 너무 ________.</strong></p>',
        'hint': '<p>과거 상태입니다.</p>',
        'explanation': '<p><strong>매웠어요</strong>: "맵다"의 과거형입니다.</p>',
        'correct': '매웠어요',
        'choices': ['매워요', '매웠어요', '맵고 있어요', '매울 거예요'],
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
