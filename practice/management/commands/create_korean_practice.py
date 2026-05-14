from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice


QUESTIONS = [
    {
        'text': "<p><strong>A: 하늘이 갑자기 어두워졌어요.<br>B: 네, 하늘이 어두워지________ 갑자기 굵은 비가 쏟아졌어요.</strong></p>",
        'explanation': "<p><strong>어두워지자마자</strong>: <code>-자마자</code> qo'shimchasi biror holat sodir bo'lgan zahoti darhol keyingisi yuz berganini ifodalaydi.</p>",
        'correct': "어두워지자마자",
        'choices': ["어두워지자마자", "어두워지는 동안", "어두워진 후에", "어두워지면서"]
    },
    {
        'text': "<p><strong>A: 한국어 실력이 정말 훌륭해요! 한국에 오신 지 얼마나 되셨어요?<br>B: 한국에 ________ 벌써 5년이 넘었어요.</strong></p>",
        'explanation': "<p><strong>온 지</strong>: <code>-(으)ㄴ 지</code> qo'shimchasi vaqt hisobini bildiradi. '오다' fe'li unliga tugagani uchun '-ㄴ 지' qo'shiladi.</p>",
        'correct': "온 지",
        'choices': ["온 지", "오기 전에", "오면서", "올 때"]
    },
    {
        'text': "<p><strong>A: 이 독한 감기약은 언제 먹어야 합니까?<br>B: 머리가 심하게 ________ 식사와 상관없이 바로 한 알씩 드세요.</strong></p>",
        'explanation': "<p><strong>아플 때</strong>: <code>-(으)ㄹ 때</code> qo'shimchasi vaqtni bildiradi. '아프다' unliga tugagani uchun '-ㄹ 때' qo'shiladi.</p>",
        'correct': "아플 때",
        'choices': ["아플 때", "아프기 전에", "아픈 후에", "아프면서"]
    },
    {
        'text': "<p><strong>A: 방이 너무 지저분해요. 언제 청소할 거예요?<br>B: 이 재미있는 드라마를 다 ________ 깨끗하게 청소할게요.</strong></p>",
        'explanation': "<p><strong>보고 나서</strong>: <code>-고 나서</code> harakatning to'liq yakunlanib, so'ngra keyingi ish boshlanishini bildiradi.</p>",
        'correct': "보고 나서",
        'choices': ["보고 나서", "보는 동안", "보기 전에", "보자마자"]
    },
    {
        'text': "<p><strong>A: 운전 중에는 휴대전화를 사용하면 절대 안 됩니다.<br>B: 죄송합니다. 앞으로는 운전________ 절대 통화하지 않겠습니다.</strong></p>",
        'explanation': "<p><strong>하면서</strong>: <code>-(으)면서</code> bir vaqtning o'zida bo'layotgan ikkita harakatni bog'laydi.</p>",
        'correct': "하면서",
        'choices': ["하면서", "한 후에", "하기 전에", "하는 동안"]
    },
    {
        'text': "<p><strong>A: 제가 잠깐 외출한 사이에 귀여운 강아지가 신발을 심하게 물어뜯었네요.<br>B: 네, 수미 씨가 밖에서 쇼핑하________ 강아지가 많이 심심했던 것 같아요.</strong></p>",
        'explanation': "<p><strong>는 동안</strong>: <code>-는 동안</code> davomiylikni bildiradi va ko'pincha turli shaxslarning harakatlarida ishlatiladi.</p>",
        'correct': "는 동안",
        'choices': ["는 동안", "면서", "기 전에", "ㄴ 후에"]
    },
    {
        'text': "<p><strong>A: 이 중요한 서류들은 어떻게 할까요?<br>B: 회의가 완전히 ________ 부장님께 직접 전달해 주세요.</strong></p>",
        'explanation': "<p><strong>끝난 후에</strong>: <code>-(으)ㄴ 후에</code> ishning tugashini va keyingisi boshlanishini ko'rsatadi.</p>",
        'correct': "끝난 후에",
        'choices': ["끝난 후에", "끝나기 전에", "끝날 때", "끝나면서"]
    },
    {
        'text': "<p><strong>A: 비행기 탑승 시간이 정말 얼마 안 남았어요.<br>B: 비행기에 ________ 면세점에서 화장품을 빨리 사야 해요.</strong></p>",
        'explanation': "<p><strong>타기 전에</strong>: <code>-기 전에</code> biron ishni qilishdan oldingi vaqtni bildiradi.</p>",
        'correct': "타기 전에",
        'choices': ["타기 전에", "타고 나서", "탈 때", "타자마자"]
    },
    {
        'text': "<p><strong>A: 저기 저 식당은 항상 사람이 많고 줄이 엄청 길어요.<br>B: 네, 저기가 우리 동네에서 가장 맛있는 매운 냉면을 ________ 식당이거든요.</strong></p>",
        'explanation': "<p><strong>파는</strong>: <code>-는</code> hozirgi zamon sifatdoshidir. '팔다' (sotmoq) fe'lidagi 'ㄹ' tushib qolib, '파는' bo'ladi.</p>",
        'correct': "파는",
        'choices': ["파는", "판", "팔", "팔면서"]
    },
    {
        'text': "<p><strong>A: 어제 백화점에서 비싸게 산 가방 어때요?<br>B: 디자인은 아주 예쁜데, 어제 ________ 가방이 생각보다 조금 무거워요.</strong></p>",
        'explanation': "<p><strong>산</strong>: <code>-(으)ㄴ</code> o'tgan zamon sifatdoshidir. '사다' fe'liga '-ㄴ' qo'shiladi.</p>",
        'correct': "산",
        'choices': ["산", "사는", "살", "사면서"]
    },
    {
        'text': "<p><strong>A: 이번 주말에 친구들과 즐거운 캠핑을 가기로 했어요.<br>B: 와, 신나겠네요! 가서 다 같이 ________ 고기와 신선한 채소는 모두 준비했어요?</strong></p>",
        'explanation': "<p><strong>먹을</strong>: <code>-(으)ㄹ</code> kelasi zamon sifatdoshidir. '먹다' undosh bilan tugagani uchun '-을' qo'shiladi.</p>",
        'correct': "먹을",
        'choices': ["먹을", "먹는", "먹은", "먹고 나서"]
    },
    {
        'text': "<p><strong>A: 나중에 어떤 집으로 이사하고 싶어요?<br>B: 저는 창문이 크고 햇빛이 잘 들어오는 아주 ________ 집에서 살고 싶어요.</strong></p>",
        'explanation': "<p><strong>밝은</strong>: <code>-(으)ㄴ</code> sifatlarga qo'shilib aniqlovchi yasaydi. '밝다' undoshga tugagani uchun '-은' qo'shiladi.</p>",
        'correct': "밝은",
        'choices': ["밝은", "밝는", "밝을", "밝으면서"]
    },
    {
        'text': "<p><strong>A: 오늘 아침에 많이 피곤해 보였어요.<br>B: 네, 어젯밤에 너무 피곤해서 푹신한 침대에 ________ 깊은 잠이 들었어요.</strong></p>",
        'explanation': "<p><strong>눕자마자</strong>: <code>-자마자</code> harakatning darhol ketma-ketligini bildiradi.</p>",
        'correct': "눕자마자",
        'choices': ["눕자마자", "누운 후에", "눕기 전에", "누울 때"]
    },
    {
        'text': "<p><strong>A: 집이 엄청 조용하네요. 아이들은 뭐 해요?<br>B: 아이들이 방에서 편안하게 낮잠을 ________ 저는 거실을 조용히 치웠어요.</strong></p>",
        'explanation': "<p><strong>자는 동안</strong>: <code>-는 동안</code> ikki xil shaxsning harakatlari bir vaqtda bo'layotganini ifodalash uchun juda mos.</p>",
        'correct': "자는 동안",
        'choices': ["자는 동안", "자면서", "자고 나서", "자기 전에"]
    },
    {
        'text': "<p><strong>A: 저녁 맛있게 먹고 우리 산책할까요?<br>B: 네, 시원한 밤바람을 ________ 넓은 공원을 천천히 걸어요.</strong></p>",
        'explanation': "<p><strong>맞으면서</strong>: <code>-(으)면서</code> qo'shimchasi. '맞다' undoshga tugagani uchun '-으면서' ulanadi.</p>",
        'correct': "맞으면서",
        'choices': ["맞으면서", "맞는 동안", "맞고 나서", "맞기 전에"]
    },
    {
        'text': "<p><strong>A: 수미 씨와 언제부터 그렇게 친해졌어요?<br>B: 우리가 서로 ________ 벌써 10년이 다 되어가요. 정말 소중한 친구예요.</strong></p>",
        'explanation': "<p><strong>안 지</strong>: <code>-(으)ㄴ 지</code> qo'shimchasi. '알다' (bilmoq/tanimoq) fe'lidagi 'ㄹ' harfi tushib qoladi va '-ㄴ 지' qo'shiladi.</p>",
        'correct': "안 지",
        'choices': ["안 지", "알기 전에", "알면서", "아는 동안"]
    },
    {
        'text': "<p><strong>A: 이 냄새나는 쓰레기들은 언제 버릴까요?<br>B: 식사를 모두 ________ 한꺼번에 모아서 밖에 버립시다.</strong></p>",
        'explanation': "<p><strong>하고 나서</strong>: <code>-고 나서</code> ovqatlanish jarayoni butunlay tugagach, tozalashga o'tishни bildiradi.</p>",
        'correct': "하고 나서",
        'choices': ["하고 나서", "하기 전에", "하면서", "할 때"]
    },
    {
        'text': "<p><strong>A: 외국 생활을 하면서 고향이 가장 그리울 때가 언제예요?<br>B: 저는 혼자 좁은 방에 있는데 몸이 많이 ________ 따뜻한 가족들이 가장 보고 싶어요.</strong></p>",
        'explanation': "<p><strong>아플 때</strong>: <code>-(으)ㄹ 때</code> kasal bo'lgan paytni bildiradi.</p>",
        'correct': "아플 때",
        'choices': ["아플 때", "아프기 전에", "아픈 후에", "아프면서"]
    },
    {
        'text': "<p><strong>A: 언제 교수님께 다시 연락을 드릴까요?<br>B: 내일 오전 복잡한 수업을 모두 ________ 교수님 연구실로 조용히 찾아가 보세요.</strong></p>",
        'explanation': "<p><strong>마친 후에</strong>: <code>-(으)ㄴ 후에</code> dars tugaganidan keyingi vaqtni bildiradi.</p>",
        'correct': "마친 후에",
        'choices': ["마친 후에", "마치기 전에", "마칠 때", "마치면서"]
    },
    {
        'text': "<p><strong>A: 밖에 눈이 펑펑 오고 있어요.<br>B: 길이 많이 미끄러우니까, 외출________ 꼭 따뜻한 겨울 신발을 신으세요.</strong></p>",
        'explanation': "<p><strong>하기 전에</strong>: <code>-기 전에</code> uydan chiqishdan oldingi vaqtni ko'rsatadi.</p>",
        'correct': "하기 전에",
        'choices': ["하기 전에", "한 후에", "할 때", "하면서"]
    },
    {
        'text': "<p><strong>A: 도서관에서 어떤 책을 그렇게 집중해서 찾고 있어요?<br>B: 제가 요즘 자주 ________ 한국어 고급 문법 책을 찾고 있어요.</strong></p>",
        'explanation': "<p><strong>읽는</strong>: <code>-는</code> hozirgi zamon sifatdoshidir. '읽다' fe'liga '-는' ulanadi.</p>",
        'correct': "읽는",
        'choices': ["읽는", "읽은", "읽을", "읽기 전에"]
    },
    {
        'text': "<p><strong>A: 식탁 위에 있는 이 달콤한 딸기 케이크는 누가 샀어요?<br>B: 아, 그거 제가 아침에 유명한 빵집에서 ________ 케이크예요. 맛있게 드세요!</strong></p>",
        'explanation': "<p><strong>사 온</strong>: <code>-(으)ㄴ</code> o'tgan zamon sifatdoshidir. '사 오다' (sotib olib kelmoq) fe'liga '-ㄴ' qo'shilgan.</p>",
        'correct': "사 온",
        'choices': ["사 온", "사 오는", "사 올", "사 오고 나서"]
    },
    {
        'text': "<p><strong>A: 다음 주 워크숍에서 무엇을 주로 논의하나요?<br>B: 내년 새로운 글로벌 프로젝트에 대해 ________ 내용이 아주 많습니다.</strong></p>",
        'explanation': "<p><strong>발표할</strong>: <code>-(으)ㄹ</code> kelasi zamon sifatdoshidir. '발표하다' (taqdimot qilmoq) fe'liga '-ㄹ' ulanadi.</p>",
        'correct': "발표할",
        'choices': ["발표할", "발표하는", "발표한", "발표하면서"]
    },
    {
        'text': "<p><strong>A: 수미 씨가 만나는 남자친구는 어떤 사람이에요?<br>B: 성격이 정말 착하고 남을 배려하는 마음이 ________ 사람이에요.</strong></p>",
        'explanation': "<p><strong>따뜻한</strong>: <code>-(으)ㄴ</code> sifatga qo'shilib aniqlovchi yasaydi. '따뜻하다' (issiq/mehribon) + '-ㄴ'.</p>",
        'correct': "따뜻한",
        'choices': ["따뜻한", "따뜻하는", "따뜻할", "따뜻하면서"]
    },
    {
        'text': "<p><strong>A: 매일 아침에 일찍 일어나서 보통 제일 먼저 뭐 해요?<br>B: 저는 아침에 눈을 ________ 시원한 생수를 꿀꺽꿀꺽 한 잔 마셔요.</strong></p>",
        'explanation': "<p><strong>뜨자마자</strong>: <code>-자마자</code> ko'zni ochish bilan suv ichish harakati ketma-ket yuz berganini bildiradi.</p>",
        'correct': "뜨자마자",
        'choices': ["뜨자마자", "뜬 후에", "뜨는 동안", "뜨기 전에"]
    },
    {
        'text': "<p><strong>A: 밥 먹을 때 스마트폰을 계속 보면 건강에 매우 안 좋대요.<br>B: 맞아요. 저도 이제 밥을 ________ 스마트폰을 절대 보지 않으려고 해요.</strong></p>",
        'explanation': "<p><strong>먹으면서</strong>: <code>-(으)면서</code> ovqatlanish va telefon ko'rish harakatlarining bir vaqtda sodir bo'lishiga ishora qiladi.</p>",
        'correct': "먹으면서",
        'choices': ["먹으면서", "먹기 전에", "먹고 나서", "먹은 지"]
    },
    {
        'text': "<p><strong>A: 제가 잠깐 우체국에 다녀올게요.<br>B: 알겠습니다. 민수 씨가 우체국에 ________ 저는 여기서 중요한 서류를 빨리 복사할게요.</strong></p>",
        'explanation': "<p><strong>다녀오는 동안</strong>: <code>-는 동안</code> bir kishi pochitada bo'lgan vaqt davomida boshqa kishi hujjat nusxalayotganini bildiradi.</p>",
        'correct': "다녀오는 동안",
        'choices': ["다녀오는 동안", "다녀오면서", "다녀오기 전에", "다녀온 후에"]
    },
    {
        'text': "<p><strong>A: 클래식 기타를 정말 멋지게 잘 치시네요! 얼마나 연습하셨어요?<br>B: 기타를 ________ 꽤 오래됐어요. 중학생 때부터 매일 꾸준히 쳤거든요.</strong></p>",
        'explanation': "<p><strong>배운 지</strong>: <code>-(으)ㄴ 지</code> gitara o'rganishni boshlagan vaqtdan beri qancha o'tganini ko'rsatadi.</p>",
        'correct': "배운 지",
        'choices': ["배운 지", "배우기 전에", "배우면서", "배우자마자"]
    },
    {
        'text': "<p><strong>A: 손과 옷이 너무 더러워요. 밖에서 대체 뭐 했어요?<br>B: 흙바닥에서 열심히 축구를 ________ 옷을 빨리 깨끗하게 갈아입어야 해요.</strong></p>",
        'explanation': "<p><strong>하고 나서</strong>: <code>-고 나서</code> futbol o'ynab bo'lgandan keyin kiyim almashtirish kerakligini bildiradi.</p>",
        'correct': "하고 나서",
        'choices': ["하고 나서", "하기 전에", "하면서", "할 때"]
    },
    {
        'text': "<p><strong>A: 이번 주말에 볼 액션 영화 표를 언제 예매할까요?<br>B: 좋은 자리가 다 ________ 지금 당장 빨리 예매합시다.</strong></p>",
        'explanation': "<p><strong>팔리기 전에</strong>: <code>-기 전에</code> chiptalar sotilib ketishidan oldin degan ma'noni beradi.</p>",
        'correct': "팔리기 전에",
        'choices': ["팔리기 전에", "팔린 후에", "팔릴 때", "팔리자마자"]
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
            title='한국어 V-(으)ㄴ 후에, 기 전에',  # --- IGNORE ---
            master=master,
            defaults={
                'description': '기 전에, ㄴ 후에, -(으)면서 등 다양한 한국어 문법 입자들을 활용하여 문장 완성하기 연습입니다.',
                'subject': subject,
                'level': 'medium',
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
