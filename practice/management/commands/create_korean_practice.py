from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice


QUESTIONS = [
    {
        'text': "<p><strong>A: 민수 씨는 아침에 무엇을 해요?<br>B: 아주 일찍 운동________ 샤워를 합니다.</strong></p>",
        'explanation': "<p><strong>한 후에</strong>: 첫 번째 행동이 끝난 다음 다른 행동을 할 때 <code>V-(으)ㄴ 후에</code>를 사용합니다. 여기서는 운동하다 → 운동한 후에 입니다.</p>",
        'correct': "한 후에",
        'choices': ["한 후에", "하기 전에", "하면서", "하자마자"]
    },
    {
        'text': "<p><strong>A: 자기 전에 보통 무엇을 해요?<br>B: 따뜻한 차를 마시________ 조용히 음악을 들어요.</strong></p>",
        'explanation': "<p><strong>기 전에</strong>: 어떤 행동을 하기 이전 상황을 나타낼 때 <code>V-기 전에</code>를 사용합니다. 마시다 → 마시기 전에 입니다.</p>",
        'correct': "기 전에",
        'choices': ["고 나서", "는 동안", "기 전에", "자마자"]
    },
    {
        'text': "<p><strong>A: 언제 가장 행복해요?<br>B: 가족들과 맛있는 음식을 먹________ 정말 행복해요.</strong></p>",
        'explanation': "<p><strong>을 때</strong>: 어떤 행동이나 상태가 일어나는 시간을 나타낼 때 <code>A/V-(으)ㄹ 때</code>를 사용합니다. 먹다 → 먹을 때 입니다.</p>",
        'correct': "을 때",
        'choices': ["은 후에", "을 때", "는 동안", "으면서"]
    },
    {
        'text': "<p><strong>A: 어떤 학생을 좋아하세요?<br>B: 항상 열심히 공부________ 학생을 좋아합니다.</strong></p>",
        'explanation': "<p><strong>하는</strong>: 현재 진행되거나 반복되는 행동으로 명사를 꾸밀 때 <code>V-는</code>을 사용합니다. 공부하다 → 공부하는 학생 입니다.</p>",
        'correct': "하는",
        'choices': ["한", "하는", "할", "하던"]
    },
    {
        'text': "<p><strong>A: 어제 본 드라마가 어땠어요?<br>B: 정말 슬프________ 드라마였어요.</strong></p>",
        'explanation': "<p><strong>고 재미있는</strong>: 형용사와 관형사형 표현을 사용해 명사를 꾸밀 수 있습니다. 재미있다 → 재미있는 드라마 입니다.</p>",
        'correct': "고 재미있는",
        'choices': ["고 재미있는", "고 재미있을", "고 재미있은", "고 재미있던"]
    },
    {
        'text': "<p><strong>A: 주말에 무엇을 할 거예요?<br>B: 친구와 같이 읽________ 책을 도서관에서 빌릴 거예요.</strong></p>",
        'explanation': "<p><strong>을</strong>: 앞으로 할 행동이 명사를 꾸밀 때 <code>V-(으)ㄹ</code> 형태를 사용합니다. 읽다 → 읽을 책 입니다.</p>",
        'correct': "을",
        'choices': ["은", "는", "을", "던"]
    },
    {
        'text': "<p><strong>A: 요즘 어떻게 공부해요?<br>B: 잔잔한 음악을 들으________ 집중해서 공부해요.</strong></p>",
        'explanation': "<p><strong>면서</strong>: 같은 사람이 두 가지 행동을 동시에 할 때 <code>V-(으)면서</code>를 사용합니다. 듣다 → 들으면서 입니다.</p>",
        'correct': "면서",
        'choices': ["자마자", "고 나서", "면서", "는 동안"]
    },
    {
        'text': "<p><strong>A: 기다리는 동안 무엇을 했어요?<br>B: 친구를 기다리________ 재미있는 소설을 읽었어요.</strong></p>",
        'explanation': "<p><strong>는 동안</strong>: 어떤 행동이 계속되는 시간 동안 다른 일이 일어날 때 <code>V-는 동안</code>을 사용합니다. 기다리다 → 기다리는 동안 입니다.</p>",
        'correct': "는 동안",
        'choices': ["은 후에", "기 전에", "는 동안", "자마자"]
    },
    {
        'text': "<p><strong>A: 숙제를 다 했어요?<br>B: 네, 숙제를 다 하________ 편안하게 쉬었어요.</strong></p>",
        'explanation': "<p><strong>고 나서</strong>: 첫 번째 행동이 완전히 끝난 후 다음 행동을 할 때 <code>V-고 나서</code>를 사용합니다.</p>",
        'correct': "고 나서",
        'choices': ["자마자", "고 나서", "는 동안", "은 후에"]
    },
    {
        'text': "<p><strong>A: 어제 왜 그렇게 피곤했어요?<br>B: 집에 들어오________ 바로 침대에서 잠들었어요.</strong></p>",
        'explanation': "<p><strong>자마자</strong>: 첫 번째 행동 직후 바로 다음 행동이 일어날 때 <code>V-자마자</code>를 사용합니다. 들어오다 → 들어오자마자 입니다.</p>",
        'correct': "자마자",
        'choices': ["고 나서", "는 동안", "기 전에", "자마자"]
    },
    {
        'text': "<p><strong>A: 한국어를 공부한 지 얼마나 되었어요?<br>B: 한국어를 배우________ 거의 2년이 되었어요.</strong></p>",
        'explanation': "<p><strong>운 지</strong>: 어떤 행동을 시작한 후 지난 시간을 나타낼 때 <code>V-(으)ㄴ 지</code>를 사용합니다. 배우다 → 배운 지 입니다.</p>",
        'correct': "운 지",
        'choices': ["는 동안", "고 나서", "운 지", "기 전에"]
    },
    {
        'text': "<p><strong>A: 비가 많이 올 때 무엇을 해요?<br>B: 따뜻한 커피를 마시________ 조용히 책을 읽어요.</strong></p>",
        'explanation': "<p><strong>면서</strong>: 같은 사람이 동시에 두 행동을 할 때 <code>V-(으)면서</code>를 사용합니다.</p>",
        'correct': "면서",
        'choices': ["면서", "자마자", "고 나서", "은 후에"]
    },
    {
        'text': "<p><strong>A: 어떤 음식을 좋아하세요?<br>B: 어머니가 정성스럽게 만드________ 음식을 아주 좋아해요.</strong></p>",
        'explanation': "<p><strong>는</strong>: 현재 진행되거나 반복되는 행동으로 명사를 꾸밀 때 <code>V-는</code>을 사용합니다. 만들다 → 만드는 음식 입니다.</p>",
        'correct': "는",
        'choices': ["는", "은", "을", "던"]
    },
    {
        'text': "<p><strong>A: 회사에 가기 전에 무엇을 했어요?<br>B: 급하게 아침을 먹________ 서둘러 나갔어요.</strong></p>",
        'explanation': "<p><strong>은 후에</strong>: 어떤 행동이 끝난 다음 다른 행동이 이어질 때 <code>V-(으)ㄴ 후에</code>를 사용합니다. 먹다 → 먹은 후에 입니다.</p>",
        'correct': "은 후에",
        'choices': ["기 전에", "자마자", "은 후에", "는 동안"]
    },
    {
        'text': "<p><strong>A: 언제 가장 바빠요?<br>B: 시험이 있________ 정말 정신이 없어요.</strong></p>",
        'explanation': "<p><strong>을 때</strong>: 특정 상황이나 시간을 나타낼 때 <code>A/V-(으)ㄹ 때</code>를 사용합니다. 있다 → 있을 때 입니다.</p>",
        'correct': "을 때",
        'choices': ["은 후에", "을 때", "는 동안", "자마자"]
    },
    {
        'text': "<p><strong>A: 점심을 먹은 후에 무엇을 했어요?<br>B: 시원한 카페에 가________ 친구와 재미있게 이야기했어요.</strong></p>",
        'explanation': "<p><strong>ㄴ 후에</strong>: 첫 번째 행동이 끝난 뒤 다음 행동이 이어질 때 <code>V-(으)ㄴ 후에</code>를 사용합니다. 가다 → 간 후에 입니다.</p>",
        'correct': "간 후에",
        'choices': ["가기 전에", "가는 동안", "간 후에", "가자마자"]
    },
    {
        'text': "<p><strong>A: 시험 보기 전에 무엇을 해요?<br>B: 조용한 곳에서 깊게 숨을 쉬________ 마음을 편하게 해요.</strong></p>",
        'explanation': "<p><strong>기 전에</strong>: 어떤 행동 이전의 상황을 말할 때 <code>V-기 전에</code>를 사용합니다. 쉬다 → 쉬기 전에 입니다.</p>",
        'correct': "기 전에",
        'choices': ["은 후에", "고 나서", "기 전에", "자마자"]
    },
    {
        'text': "<p><strong>A: 언제 음악을 자주 들어요?<br>B: 버스를 타________ 밝은 음악을 자주 들어요.</strong></p>",
        'explanation': "<p><strong>ㄹ 때</strong>: 어떤 행동이 일어나는 시간을 나타낼 때 <code>A/V-(으)ㄹ 때</code>를 사용합니다. 타다 → 탈 때 입니다.</p>",
        'correct': "ㄹ 때",
        'choices': ["는 동안", "ㄹ 때", "은 후에", "고 나서"]
    },
    {
        'text': "<p><strong>A: 어떤 커피를 좋아하세요?<br>B: 향기가 진하________ 커피를 좋아해요.</strong></p>",
        'explanation': "<p><strong>ㄴ</strong>: 형용사가 명사를 꾸밀 때 <code>A-(으)ㄴ</code>을 사용합니다. 진하다 → 진한 커피 입니다.</p>",
        'correct': "ㄴ",
        'choices': ["는", "ㄹ", "ㄴ", "던"]
    },
    {
        'text': "<p><strong>A: 지금 무엇을 찾고 있어요?<br>B: 내일 중요한 모임에 입________ 옷을 찾고 있어요.</strong></p>",
        'explanation': "<p><strong>을</strong>: 미래에 할 행동으로 명사를 꾸밀 때 <code>V-(으)ㄹ</code>을 사용합니다. 입다 → 입을 옷 입니다.</p>",
        'correct': "을",
        'choices': ["은", "는", "을", "던"]
    },
    {
        'text': "<p><strong>A: 요즘 어떻게 운동해요?<br>B: 신나는 음악을 들으________ 열심히 달려요.</strong></p>",
        'explanation': "<p><strong>으면서</strong>: 같은 사람이 동시에 두 행동을 할 때 <code>V-(으)면서</code>를 사용합니다. 듣다 → 들으면서 입니다.</p>",
        'correct': "으면서",
        'choices': ["자마자", "고 나서", "으면서", "는 동안"]
    },
    {
        'text': "<p><strong>A: 어머니가 요리하는 동안 무엇을 했어요?<br>B: 저는 깨끗하게 방을 청소하________ 있었어요.</strong></p>",
        'explanation': "<p><strong>고</strong>: 두 행동을 자연스럽게 연결할 때 <code>-고</code>를 사용할 수 있습니다.</p>",
        'correct': "고",
        'choices': ["자마자", "고", "으면서", "기 전에"]
    },
    {
        'text': "<p><strong>A: 퇴근하고 나서 보통 무엇을 해요?<br>B: 따뜻하게 샤워를 하________ 편하게 쉬어요.</strong></p>",
        'explanation': "<p><strong>고 나서</strong>: 첫 번째 행동이 완전히 끝난 뒤 다음 행동이 이어질 때 사용합니다.</p>",
        'correct': "고 나서",
        'choices': ["는 동안", "자마자", "고 나서", "기 전에"]
    },
    {
        'text': "<p><strong>A: 학교에 도착하자마자 무엇을 했어요?<br>B: 바로 교실에 들어가________ 선생님께 인사했어요.</strong></p>",
        'explanation': "<p><strong>서</strong>: 연결된 행동을 자연스럽게 이어 줄 때 사용합니다. 들어가서 인사했어요.</p>",
        'correct': "서",
        'choices': ["고", "서", "지만", "는데"]
    },
    {
        'text': "<p><strong>A: 한국에 온 지 얼마나 되었어요?<br>B: 한국에서 생활한 지 벌써 3년이 넘________.</strong></p>",
        'explanation': "<p><strong>어요</strong>: 기간 표현 뒤에 자연스럽게 연결되는 표현입니다. 넘었어요가 완성형입니다.</p>",
        'correct': "었어요",
        'choices': ["겠어요", "었어요", "지요", "네요"]
    },
    {
        'text': "<p><strong>A: 언제 산책하는 것을 좋아하세요?<br>B: 날씨가 맑________ 공원에서 천천히 산책해요.</strong></p>",
        'explanation': "<p><strong>을 때</strong>: 특정 상황이나 시간에 하는 행동을 나타낼 때 사용합니다. 맑다 → 맑을 때 입니다.</p>",
        'correct': "을 때",
        'choices': ["은 후에", "자마자", "을 때", "는 동안"]
    },
    {
        'text': "<p><strong>A: 어떤 영화를 좋아해요?<br>B: 감동적이________ 따뜻한 영화를 좋아해요.</strong></p>",
        'explanation': "<p><strong>고</strong>: 형용사를 연결해 동시에 여러 특징을 설명할 때 <code>-고</code>를 사용합니다.</p>",
        'correct': "고",
        'choices': ["지만", "고", "거나", "는데"]
    },
    {
        'text': "<p><strong>A: 아침 운동을 한 후에 기분이 어때요?<br>B: 몸이 가볍________ 아주 상쾌해요.</strong></p>",
        'explanation': "<p><strong>고</strong>: 두 가지 상태를 연결할 때 자연스럽게 사용합니다.</p>",
        'correct': "고",
        'choices': ["지만", "거나", "고", "는데"]
    },
    {
        'text': "<p><strong>A: 수업이 시작되기 전에 학생들은 무엇을 해요?<br>B: 조용히 자리에 앉________ 책을 읽어요.</strong></p>",
        'explanation': "<p><strong>아서</strong>: 순차적인 행동을 자연스럽게 연결할 때 사용합니다. 앉아서 읽어요.</p>",
        'correct': "아서",
        'choices': ["지만", "아서", "거나", "는데"]
    },
    {
        'text': "<p><strong>A: 휴가 때 어디에 가고 싶어요?<br>B: 조용하고 아름답________ 바다에 가고 싶어요.</strong></p>",
        'explanation': "<p><strong>은</strong>: 형용사가 명사를 꾸밀 때 <code>A-(으)ㄴ</code>을 사용합니다. 아름답다 → 아름다운 바다 입니다.</p>",
        'correct': "은",
        'choices': ["는", "은", "을", "던"]
    },
    {
        'text': "<p><strong>A: 친구를 기다리는 동안 무엇을 했어요?<br>B: 따뜻한 커피를 마시________ 휴대폰을 봤어요.</strong></p>",
        'explanation': "<p><strong>면서</strong>: 같은 사람이 동시에 두 행동을 할 때 사용합니다.</p>",
        'correct': "면서",
        'choices': ["고 나서", "자마자", "면서", "은 후에"]
    },
    {
        'text': "<p><strong>A: 집에 오자마자 왜 샤워했어요?<br>B: 날씨가 너무 덥________ 바로 씻고 싶었어요.</strong></p>",
        'explanation': "<p><strong>어서</strong>: 이유를 설명할 때 <code>-아서/어서</code>를 사용합니다.</p>",
        'correct': "어서",
        'choices': ["지만", "거나", "어서", "는데"]
    },
    {
        'text': "<p><strong>A: 어떤 사람을 존경하세요?<br>B: 항상 성실하게 일하________ 사람을 존경해요.</strong></p>",
        'explanation': "<p><strong>는</strong>: 현재 반복되는 행동으로 명사를 꾸밀 때 사용합니다.</p>",
        'correct': "는",
        'choices': ["은", "는", "을", "던"]
    },
    {
        'text': "<p><strong>A: 발표를 하기 전에 긴장했어요?<br>B: 네, 너무 떨리________ 계속 연습했어요.</strong></p>",
        'explanation': "<p><strong>어서</strong>: 이유를 설명하는 표현입니다. 떨리어서 → 떨려서 로 줄어듭니다.</p>",
        'correct': "어서",
        'choices': ["어서", "지만", "고", "거나"]
    },
    {
        'text': "<p><strong>A: 시험이 끝난 후에 무엇을 하고 싶어요?<br>B: 맛있는 음식을 먹________ 푹 쉬고 싶어요.</strong></p>",
        'explanation': "<p><strong>고</strong>: 두 행동을 연결할 때 사용하는 표현입니다.</p>",
        'correct': "고",
        'choices': ["고", "지만", "거나", "는데"]
    },
    {
        'text': "<p><strong>A: 비 오는 날에는 무엇을 해요?<br>B: 조용한 카페에서 따뜻한 차를 마시________ 책을 읽어요.</strong></p>",
        'explanation': "<p><strong>면서</strong>: 동시에 두 행동을 할 때 사용하는 표현입니다.</p>",
        'correct': "면서",
        'choices': ["은 후에", "고 나서", "면서", "자마자"]
    },
    {
        'text': "<p><strong>A: 한국어를 배운 지 얼마나 되었어요?<br>B: 진지하게 공부한 지 아직 1년이 안 되________.</strong></p>",
        'explanation': "<p><strong>어요</strong>: 기간 표현과 함께 자주 쓰이는 형태입니다. 안 되었어요가 자연스럽습니다.</p>",
        'correct': "었어요",
        'choices': ["겠어요", "었어요", "지요", "네요"]
    },
    {
        'text': "<p><strong>A: 어떤 음악을 자주 들어요?<br>B: 조용하________ 부드러운 음악을 좋아해요.</strong></p>",
        'explanation': "<p><strong>고</strong>: 형용사를 연결해서 여러 특징을 설명합니다.</p>",
        'correct': "고",
        'choices': ["거나", "고", "지만", "는데"]
    },
    {
        'text': "<p><strong>A: 여행을 가기 전에 무엇을 준비해요?<br>B: 필요한 물건을 꼼꼼하게 챙기________ 계획을 세워요.</strong></p>",
        'explanation': "<p><strong>고</strong>: 순차적인 행동을 연결할 때 사용합니다.</p>",
        'correct': "고",
        'choices': ["지만", "고", "거나", "는데"]
    },
    {
        'text': "<p><strong>A: 어떤 계절을 가장 좋아하세요?<br>B: 하늘이 맑고 바람이 시원하________ 가을을 좋아해요.</strong></p>",
        'explanation': "<p><strong>ㄴ</strong>: 형용사가 명사를 꾸밀 때 사용합니다. 시원하다 → 시원한 가을 입니다.</p>",
        'correct': "ㄴ",
        'choices': ["는", "ㄹ", "ㄴ", "던"]
    },
    {
        'text': "<p><strong>A: 수업을 듣는 동안 졸리지 않았어요?<br>B: 교수님 설명이 너무 재미있________ 전혀 졸리지 않았어요.</strong></p>",
        'explanation': "<p><strong>어서</strong>: 이유를 설명하는 표현입니다.</p>",
        'correct': "어서",
        'choices': ["지만", "어서", "거나", "는데"]
    },
    {
        'text': "<p><strong>A: 아침에 일어나자마자 무엇을 해요?<br>B: 창문을 열________ 신선한 공기를 마셔요.</strong></p>",
        'explanation': "<p><strong>고</strong>: 순차적인 행동을 연결하는 표현입니다.</p>",
        'correct': "고",
        'choices': ["고", "지만", "거나", "는데"]
    },
    {
        'text': "<p><strong>A: 어떤 도시에서 살고 싶어요?<br>B: 조용하________ 자연이 아름다운 도시에서 살고 싶어요.</strong></p>",
        'explanation': "<p><strong>고</strong>: 형용사를 연결해 여러 특징을 설명합니다.</p>",
        'correct': "고",
        'choices': ["고", "지만", "거나", "는데"]
    },
    {
        'text': "<p><strong>A: 친구를 만난 후에 어디에 갔어요?<br>B: 근처 식당에 가________ 맛있는 저녁을 먹었어요.</strong></p>",
        'explanation': "<p><strong>서</strong>: 장소 이동 후 이어지는 행동을 자연스럽게 연결합니다.</p>",
        'correct': "서",
        'choices': ["고", "서", "지만", "는데"]
    },
    {
        'text': "<p><strong>A: 언제 가장 기분이 좋아요?<br>B: 좋아하는 사람들과 함께 이야기하________ 정말 행복해요.</strong></p>",
        'explanation': "<p><strong>ㄹ 때</strong>: 특정 상황이나 시간을 나타낼 때 사용합니다. 이야기하다 → 이야기할 때 입니다.</p>",
        'correct': "ㄹ 때",
        'choices': ["은 후에", "는 동안", "자마자", "ㄹ 때"]
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
            title='12-dars: Ketma ketlik',  # --- IGNORE ---
            master=master,
            defaults={
                'description': 'Ketma-ketlik  bog\'lovchilarini o\'rganish uchun amaliy test.',
                'subject': subject,
                'level': 'hard',
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
