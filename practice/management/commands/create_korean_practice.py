from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

questions = [
    {
        'text': "<p>A: 아까 흐엉 씨가 전화해서 뭐라고 했어요?<br>B: 오늘 날씨가 <u>너무</u> <strong>좋아서</strong> 한강으로 산책을 ________.</p>",
        'explanation': "<p><strong>가자고 했어요</strong>: 흐엉 씨가 '같이 가요'라고 제안(청유)한 내용을 다른 사람에게 전달할 때는 '-자고 하다'를 사용합니다.</p>",
        'correct': "가자고 했어요",
        'choices': ["가라고 했어요", "간다고 했어요", "가자고 했어요", "가냐고 했어요"]
    },
    {
        'text': "<p>A: 의사 선생님께서 건강 검진 결과표를 보시며 뭐라고 말씀하셨나요?<br>B: 건강을 위해서 담배를 <u>당장</u> <strong>끊고</strong> 매일 <u>꾸준히</u> ________.</p>",
        'explanation': "<p><strong>운동하라고 하셨어요</strong>: 의사 선생님의 지시나 명령, 강력한 권유('운동하세요')를 간접적으로 전달할 때는 '-라고 하다'를 사용합니다.</p>",
        'correct': "운동하라고 하셨어요",
        'choices': ["운동하자고 하셨어요", "운동하라고 하셨어요", "운동한다고 하셨어요", "운동하냐고 하셨어요"]
    },
    {
        'text': "<p>A: 민우 씨가 아까 회의실에서 <u>심각한</u> 표정으로 뭘 물어봤어요?<br>B: 이번 주말에 시작하는 프로젝트 준비가 <u>벌써</u> 다 ________.</p>",
        'explanation': "<p><strong>끝났냐고 했어요</strong>: 과거의 사실에 대한 질문('끝났어요?')을 다른 사람에게 간접적으로 전달할 때는 아/었에 '-냐고 하다'를 붙여 사용합니다.</p>",
        'correct': "끝났냐고 했어요",
        'choices': ["끝났냐고 했어요", "끝나자고 했어요", "끝났다고 했어요", "끝나라고 했어요"]
    },
    {
        'text': "<p>A: 웨이 씨가 고향으로 돌아가기 전에 친구들에게 뭐라고 인사했나요?<br>B: 나중에 <u>꼭</u> 자기 고향에 놀러 ________.</p>",
        'explanation': "<p><strong>오라고 했어요</strong>: '오세요'라는 상대방의 명령이나 요청을 간접 화법으로 바꿀 때는 '-라고 하다'를 사용합니다.</p>",
        'correct': "오라고 했어요",
        'choices': ["온다고 했어요", "오자고 했어요", "오냐고 했어요", "오라고 했어요"]
    },
    {
        'text': "<p>A: 아까 선생님께서 진수 씨를 <u>따로</u> 부르셔서 무슨 말씀을 하셨어요?<br>B: 내일 오전까지 숙제를 <u>반드시</u> ________.</p>",
        'explanation': "<p><strong>제출하라고 하셨어요</strong>: 선생님의 지시나 명령('제출하세요')을 제삼자에게 전달할 때 쓰이는 표현은 '-라고 하다'입니다.</p>",
        'correct': "제출하라고 하셨어요",
        'choices': ["제출한다고 하셨어요", "제출하라고 하셨어요", "제출하자고 하셨어요", "제출하냐고 하셨어요"]
    },
    {
        'text': "<p>A: 수미 씨가 주말에 맛있는 음식을 먹으러 가자며 전화했네요.<br>B: 네, 새로 오픈한 시내 레스토랑의 파스타가 <u>정말</u> ________.</p>",
        'explanation': "<p><strong>맛있다고 하더라고요</strong>: 평서문('맛있어요')의 내용을 간접적으로 전달하면서 자신이 들은 사실을 회상하여 말할 때는 '-다고 하다'를 사용합니다.</p>",
        'correct': "맛있다고 하더라고요",
        'choices': ["맛있냐고 하더라고요", "맛있자고 하더라고요", "맛있으라고 하더라고요", "맛있다고 하더라고요"]
    },
    {
        'text': "<p>A: 부장님께서 퇴근 시간에 <u>갑자기</u> 직원들을 부르신 이유가 뭐예요?<br>B: 오늘 저녁에 <u>다 함께</u> <u>기분 좋게</u> 회식을 ________.</p>",
        'explanation': "<p><strong>하자고 하셨어요</strong>: '회식합시다'라는 부장님의 청유/제안을 높임의 대상으로서 간접 전달할 때는 '-자고 하시다'를 사용합니다.</p>",
        'correct': "하자고 하셨어요",
        'choices': ["한다고 하셨어요", "하냐고 하셨어요", "하자고 하셨어요", "하라고 하셨어요"]
    },
    {
        'text': "<p>A: 영민 씨가 <u>아까부터</u> 지갑을 계속 뒤적이던데 무슨 일이 있대요?<br>B: <u>어제</u> 산 지갑이 <u>아무리</u> 찾아도 안 보인다고 하면서 혹시 ________.</p>",
        'explanation': "<p><strong>봤냐고 물어봤어요</strong>: 상대방에게 물어본 의문문('봤어요?')을 다른 사람에게 전달할 때는 '-냐고 하다/물어보다'를 사용합니다.</p>",
        'correct': "봤냐고 물어봤어요",
        'choices': ["봤다고 물어봤어요", "봤냐고 물어봤어요", "보자고 물어봤어요", "보라고 물어봤어요"]
    },
    {
        'text': "<p>A: 마크 씨가 한국 요리 수업을 신청하려다가 망설이고 있더라고요.<br>B: 맞아요, 저한테도 한국 음식을 만드는 것이 <u>많이</u> ________.</p>",
        'explanation': "<p><strong>어려우냐고 물어봤어요</strong>: 형용사의 의문문('어려워요?')을 간접 화법으로 바꿀 때는 받침 여부와 관계없이 '-(으)냐고 하다/물어보다'를 사용합니다.</p>",
        'correct': "어려우냐고 물어봤어요",
        'choices': ["어렵자고 물어봤어요", "어렵다고 물어봤어요", "어려우냐고 물어봤어요", "어려우라고 물어봤어요"]
    },
    {
        'text': "<p>A: 동생이 아침에 일어나자마자 <u>밖을</u> 내다보며 뭐라고 하던가요?<br>B: 지금 밖에 눈이 <u>펑펑</u> ________.</p>",
        'explanation': "<p><strong>온다고 했어요</strong>: 현재 일어나는 사실이나 상태를 평서문('눈이 와요')으로 전달할 때는 동사 어간에 '-ㄴ/는다고 하다'를 사용합니다.</p>",
        'correct': "온다고 했어요",
        'choices': ["오라고 했어요", "온다고 했어요", "오자고 했어요", "오냐고 했어요"]
    },
    {
        'text': "<p>A: 어머니께서 시장에 가시기 전에 <u>방에 있는</u> 저에게 뭐라고 하셨어요?<br>B: 집에서 <u>조용히</u> 책을 읽으면서 동생을 <u>잘</u> ________.</p>",
        'explanation': "<p><strong>돌보고 있으라고 하셨어요</strong>: '돌보고 있으렴/있어라'라는 어머니의 명령 및 당부를 간접적으로 전달할 때는 '-라고 하다'를 사용합니다.</p>",
        'correct': "돌보고 있으라고 하셨어요",
        'choices': ["돌보고 있으라고 하셨어요", "돌보고 있다고 하셨어요", "돌보고 있자고 하셨어요", "돌보고 있냐고 하셨어요"]
    },
    {
        'text': "<p>A: 서우 씨가 이번 방학에 <u>특별한</u> 계획이 있다고 자랑하더니 뭐래요?<br>B: 이번에는 친구들과 <u>다 같이</u> 제주도로 배낭여행을 ________.</p>",
        'explanation': "<p><strong>갈 거라고 했어요</strong>: 미래의 계획이나 예정된 일('갈 거예요')을 평서문으로 간접 전달할 때는 '-(으)ㄹ 거라고 하다'를 사용합니다.</p>",
        'correct': "갈 거라고 했어요",
        'choices': ["가자고 했어요", "가냐고 했어요", "가라고 했어요", "갈 거라고 했어요"]
    },
    {
        'text': "<p>A: 길을 가다가 <u>낯선</u> 사람이 다가와서 <u>갑자기</u> 말을 걸었어요.<br>B: 그 사람이 서우 씨에게 무슨 서류를 보여주며 혹시 ________?</p>",
        'explanation': "<p><strong>외국인이냐고 물어봤어요</strong>: 명사의 의문문('외국인이에요?')을 간접 화법으로 바꿀 때는 명사 뒤에 '-(이)냐고 하다/물어보다'를 붙입니다.</p>",
        'correct': "외국인이냐고 물어봤어요",
        'choices': ["외국인이라고 물어봤어요", "외국인이냐고 물어봤어요", "외국인이자고 물어봤어요", "외국인이라고 하라고 물어봤어요"]
    },
    {
        'text': "<p>A: 아까 미팅 시간에 지수 씨가 김 대리님께 <u>부탁하듯이</u> 말하더군요.<br>B: 네, 이번 주말 바이어 미팅 자료를 <u>조금만</u> <u>빨리</u> ________.</p>",
        'explanation': "<p><strong>달라고 했어요</strong>: 말하는 사람이 듣는 사람에게 자신을 위해 무언가를 해 주거나 달라고 요청('주세요')할 때는 '-달라고 하다'로 변경하여 전달합니다.</p>",
        'correct': "달라고 했어요",
        'choices': ["주라고 했어요", "달라고 했어요", "주자고 했어요", "주냐고 했어요"]
    },
    {
        'text': "<p>A: 사장님께서 <u>오후</u> 회의가 끝난 후에 비서에게 지시를 내리셨나요?<br>B: 네, 거래처 사장님께 연락해서 다음 주 일정을 <u>다시</u> ________.</p>",
        'explanation': "<p><strong>확인해 주라고 하셨어요</strong>: 부탁의 내용이 제삼자(거래처 사장님)를 위한 행동('확인해 주세요')일 때는 '-주라고 하다'를 사용하여 전달합니다.</p>",
        'correct': "확인해 주라고 하셨어요",
        'choices': ["확인해 달라고 하셨어요", "확인해 주자고 하셨어요", "확인해 주라고 하셨어요", "확인해 준다고 하셨어요"]
    },
    {
        'text': "<p>A: 아까 요리 동호회 모임에서 회장님이 회원들에게 제안을 하더라고요.<br>B: 네, 다음 주말에 <u>다 함께</u> 한국 전통 음식을 ________.</p>",
        'explanation': "<p><strong>만들자고 했어요</strong>: '만듭시다/만들어요'라는 제안 및 청유의 표현을 간접 화법으로 나타낼 때는 '-자고 하다'를 사용합니다.</p>",
        'correct': "만들자고 했어요",
        'choices': ["만든다고 했어요", "만들냐고 했어요", "만들라고 했어요", "만들자고 했어요"]
    },
    {
        'text': "<p>A: 유키 씨가 한국 생활에 대해 <u>자주</u> 이야기하곤 하죠?<br>B: 네, 고향을 떠나 <u>타국에서</u> 혼자 사는 것이 <u>가끔</u> <u>무척</u> ________.</p>",
        'explanation': "<p><strong>외롭다고 했어요</strong>: 형용사의 평서문('외로워요')을 간접적으로 전달할 때는 어간 뒤에 그대로 '-다고 하다'를 붙여 사용합니다.</p>",
        'correct': "외롭다고 했어요",
        'choices': ["외롭자고 했어요", "외롭다고 했어요", "외로우냐고 했어요", "외로우라고 했어요"]
    },
    {
        'text': "<p>A: 어제 서점에서 만난 친구가 책을 고르면서 나에게 진지하게 물어봤다.<br>B: 무슨 책인데? 너에게 요즘 <u>주로</u> 어떤 분야의 책을 ________?</p>",
        'explanation': "<p><strong>읽느냐고 물어봤어</strong>: 동사의 현재 시제 의문문('읽어요?')을 간접적으로 나타낼 때는 어간 뒤에 '-느냐고 하다/물어보다'를 사용합니다.</p>",
        'correct': "읽느냐고 물어봤어",
        'choices': ["읽느냐고 물어봤어", "읽자고 물어봤어", "읽으라고 물어봤어", "읽는다고 물어봤어"]
    },
    {
        'text': "<p>A: 선생님께서 시험을 앞둔 학생들에게 <u>크게</u> 강조하며 말씀하셨어요.<br>B: 시험을 볼 때 모르는 문제가 나와도 <u>절대</u> 포기하지 ________.</p>",
        'explanation': "<p><strong>말라고 하셨어요</strong>: 금지의 명령문('하지 마세요')을 간접적으로 전달할 때는 '-지 말라고 하다' 문형을 활용합니다.</p>",
        'correct': "말라고 하셨어요",
        'choices': ["말자고 하셨어요", "말라고 하셨어요", "마냐고 하셨어요", "말았다고 하셨어요"]
    },
    {
        'text': "<p>A: 인호 씨 부모님께서 고향 집 소식을 전해 주시며 전화하셨대요.<br>B: 네, 올해 고향 집 앞마당에 감나무를 <u>새로</u> ________.</p>",
        'explanation': "<p><strong>심었다고 하셨어요</strong>: 과거에 완료된 일('심었어요')에 대한 평서문을 간접 화법으로 전달할 때는 았/었 뒤에 '-다고 하다'를 결합합니다.</p>",
        'correct': "심었다고 하셨어요",
        'choices': ["심자고 하셨어요", "심으라고 하셨어요", "심었냐고 하셨어요", "심었다고 하셨어요"]
    },
    {
        'text': "<p>A: 투이 씨가 <u>아까부터</u> 가방을 메고 서성거리며 문 앞을 서성이네요.<br>B: 네, 밖의 날씨가 <u>너무</u> 추우니까 <u>얼른</u> 안으로 ________.</p>",
        'explanation': "<p><strong>들어가자고 하더라고요</strong>: 상대방에게 '들어갑시다'라고 청유하는 상황을 간접 화법으로 표현할 때는 '-자고 하다'를 사용합니다.</p>",
        'correct': "들어가자고 하더라고요",
        'choices': ["들어가라고 하더라고요", "들어간다고 하더라고요", "들어가자고 하더라고요", "들어가냐고 하더라고요"]
    },
    {
        'text': "<p>A: 도서관 사서 선생님이 <u>지나치게</u> 큰 소리로 떠드는 아이들에게 다가갔어요.<br>B: 다른 사람들이 조용히 공부하고 있으니 <u>좀</u> <u>조용히</u> ________.</p>",
        'explanation': "<p><strong>하라고 하셨어요</strong>: 상대방의 행동을 통제하거나 지시하는 명령문('조용히 하세요')의 간접 전달은 '-라고 하다'를 씁니다.</p>",
        'correct': "하라고 하셨어요",
        'choices': ["하냐고 하셨어요", "하자고 하셨어요", "한다고 하셨어요", "하라고 하셨어요"]
    },
    {
        'text': "<p>A: 제이슨 씨가 한국 친구 집을 <u>처음</u> 방문하기 전에 무엇을 물어봤어요?<br>B: 한국에서는 집에 들어갈 때 신발을 <u>꼭</u> <strong>벗어야</strong> ________.</p>",
        'explanation': "<p><strong>하냐고 물어봤어요</strong>: 동사의 의문문('해야 해요?')을 간접적으로 전달할 때는 어간 뒤에 '-냐고 하다/물어보다'를 결합합니다.</p>",
        'correct': "하냐고 물어봤어요",
        'choices': ["하자고 물어봤어요", "하냐고 물어봤어요", "한다고 물어봤어요", "하라고 물어봤어요"]
    },
    {
        'text': "<p>A: 지민 씨가 주말에 약속이 있느냐는 내 질문에 뭐라고 답변했나요?<br>B: 이번 주말에는 고향에서 가족들이 올라와서 <u>무척</u> ________.</p>",
        'explanation': "<p><strong>바쁘다고 했어요</strong>: 형용사의 평서문('바빠요')을 다른 사람에게 전달하는 간접 화법 문형은 '-다고 하다'입니다.</p>",
        'correct': "바쁘다고 했어요",
        'choices': ["바쁘냐고 했어요", "바쁘자고 했어요", "바쁘라고 했어요", "바쁘다고 했어요"]
    },
    {
        'text': "<p>A: 야구 경기장에 같이 간 친구가 갑자기 매점으로 달려가더라고요.<br>B: 네, 날씨가 <u>워낙</u> 더우니까 <u>시원한</u> 음료수를 <u>좀</u> 사 ________.</p>",
        'explanation': "<p><strong>오자고 했어요</strong>: '사 옵시다'라는 같이 행동하자는 제안(청유문)을 전달하는 형식이므로 '-자고 하다'가 맞습니다.</p>",
        'correct': "오자고 했어요",
        'choices': ["온다고 했어요", "오냐고 했어요", "오자고 했어요", "오라고 했어요"]
    },
    {
        'text': "<p>A: 주말에 백화점에 가니까 안내원이 마이크로 <u>크게</u> 방송을 하고 있었어요.<br>B: 어린아이를 동반한 고객님들은 아이의 손을 <u>꼭</u> 잡고 ________.</p>",
        'explanation': "<p><strong>다니라고 하더군요</strong>: 공공장소에서의 지시사항이나 요구사항('다니세요')을 간접적으로 전할 때는 '-라고 하다'를 사용합니다.</p>",
        'correct': "다니라고 하더군요",
        'choices': ["다닌다고 하더군요", "다니라고 하더군요", "다니자고 하더군요", "다니냐고 하더군요"]
    },
    {
        'text': "<p>A: 민호 씨가 내일 여행을 떠나기 전에 준비물을 확인하느라 전화를 했어요.<br>B: 네, 저한테 카메라를 <u>내일까지</u> <u>꼭</u> 챙겨 ________.</p>",
        'explanation': "<p><strong>오라고 했어요</strong>: 상대방이 나에게 어떤 행동을 요구('가져오세요/챙겨오세요')하는 명령문을 간접적으로 전달할 때는 '-라고 하다'가 쓰입니다.</p>",
        'correct': "오라고 했어요",
        'choices': ["오자고 했어요", "오라고 했어요", "온다고 했어요", "오냐고 했어요"]
    },
    {
        'text': "<p>A: 진아 씨가 새로 취직한 직장 생활에 대해 <u>매우</u> 만족해하고 있나요?<br>B: 네, 회사 동료들도 <u>모두</u> <u>친절하고</u> 분위기도 <u>참</u> ________.</p>",
        'explanation': "<p><strong>좋다고 하더라고요</strong>: 상태나 성질을 나타내는 형용사의 평서문('좋아요')을 간접적으로 다른 사람에게 전달할 때는 '-다고 하다'를 씁니다.</p>",
        'correct': "좋다고 하더라고요",
        'choices': ["좋냐고 하더라고요", "좋자고 하더라고요", "좋으라고 하더라고요", "좋다고 하더라고요"]
    },
    {
        'text': "<p>A: 수지 씨가 아까 백화점에서 <u>예쁜</u> 모자를 보고 한참을 망설였어요.<br>B: 맞아요, 디자인은 <u>아주</u> 마음에 드는데 가격이 너무 ________.</p>",
        'explanation': "<p><strong>비싸다고 하대요</strong>: 다른 사람의 평서문 의견('비싸요')을 간접적으로 전달할 때 사용하는 문형은 '-다고 하다'입니다.</p>",
        'correct': "비싸다고 하대요",
        'choices': ["비싸다고 하대요", "비싸자고 하대요", "비싸냐고 하대요", "비싸라고 하대요"]
    },
    {
        'text': "<p>A: 정우 씨가 이번 공모전에 참여할 파트너를 <u>급하게</u> 찾고 있어요.<br>B: 네, 저에게 찾아와서 이번 공모전에 <u>같이</u> 팀을 구성해서 ________.</p>",
        'explanation': "<p><strong>나가자고 제안했어요</strong>: '같이 나갑시다'라는 상대방의 청유를 간접적으로 전달하는 문형은 '-자고 하다'를 기본으로 삼습니다.</p>",
        'correct': "나가자고 제안했어요",
        'choices': ["나간다고 제안했어요", "나가냐고 제안했어요", "나가라고 제안했어요", "나가자고 제안했어요"]
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
            title='Takrorlash 3, 라고, 다, 자고 하다',  # --- IGNORE ---
            master=master,
            defaults={
                'description': 'Tarixdan o\'rganamiz',
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

        for i, q in enumerate(questions, start=1):
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
            f"Created practice '{practice.title}' with {len(questions)} questions (id={practice.pk})."
        ))
