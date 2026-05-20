from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
    {
        'text': "<p><strong>A: 지민 씨, 어제 백화점에서 뭐 샀어요?<br>B: 겨울 코트가 너무 비싸서 그냥 가방________ 하나 샀어요.</strong></p>",
        'explanation': "<p><strong>가방을</strong>: '샀어요' (sotib oldim) o'timli fe'li kelgani uchun 'gabaong' (sumka) so'ziga tushum kelishigi (<code>-을/를</code>) qo'shilishi kerak. Unli bilan tugagani uchun <code>를</code> tanlanadi.</p>",
        'correct': "가방을",
        'choices': ["가방이", "가방은", "가방을", "가방가"]
    },
    {
        'text': "<p><strong>A: 창문을 열어 보니까 밖에 눈________ 많이 내리고 있네요.<br>B: 우와, 정말요? 오늘 날씨가 많이 춥겠어요.</strong></p>",
        'explanation': "<p><strong>눈이</strong>: Tabiat hodisalarini (yomg'ir, qor, shamol) ilk bor tasvirlaganda yoki yangi ma'lumot berilganda ega kelishigi (<code>-이/가</code>) ishlatiladi. '눈' undosh bilan tugagani uchun <code>이</code> keladi.</p>",
        'correct': "눈이",
        'choices': ["눈은", "눈이", "눈을", "눈가"]
    },
    {
        'text': "<p><strong>A: 수박 한 통에 얼마예요?<br>B: 수박________ 한 통에 25,000원입니다. 아주 달고 맛있어요.</strong></p>",
        'explanation': "<p><strong>수박은</strong>: Suhbatning asosiy mavzusini belgilash yoki narx so'ralgan buyumga urg'u berish uchun mavzu yuklamasi (<code>-은/는</code>) ishlatiladi. Undosh bilan tugagani uchun <code>은</code> to'g'ri.</p>",
        'correct': "수박은",
        'choices': ["수박이", "수박을", "수박은", "수박가"]
    },
    {
        'text': "<p><strong>A: 마크 씨, 혹시 시간 있으면 저 좀 도와줄 수 있어요?<br>B: 미안해요. 지금 중요함 이메일________ 쓰고 있어서 조금 바빠요.</strong></p>",
        'explanation': "<p><strong>이메일을</strong>: '쓰고 있다' (yozmoqda) harakati to'g'ridan-to'g'ri 'imeil'ga yo'naltirilgan. O'zbek tilidagi '-ni' kelishigiga mos keladigan tushum kelishigi (<code>-을/를</code>) kerak.</p>",
        'correct': "이메일을",
        'choices': ["이메일이", "이메일은", "이메일을", "이메일가"]
    },
    {
        'text': "<p><strong>A: 누가 교실 청소를 안 하고 그냥 갔어요?<br>B: 아까 민우________ 청소를 안 하고 집에 가는 걸 봤어요.</strong></p>",
        'explanation': "<p><strong>민우가</strong>: '누가?' (Kim?) degan aniq savolga javob berayotganda, harakatni bajargan aniq shaxsni (egani) ko'rsatish uchun ega kelishigi (<code>-이/가</code>) ishlatiladi.</p>",
        'correct': "민우가",
        'choices': ["민우는", "민우가", "민우를", "민우이"]
    },
    {
        'text': "<p><strong>A: 한국어 공부가 아주 재미있지요?<br>B: 네, 한국어________ 재미있어요. 하지만 단어가 너무 어려워요.</strong></p>",
        'explanation': "<p><strong>한국어는</strong>: Gapning bosh mavzusi yoki taqqoslash obyekti sifatida 'Koreys tiliga kelsak, u qiziqarli (lekin so'zlari qiyin)' ma'nosini ifodalash uchun <code>-은/는</code> qo'llanadi.</p>",
        'correct': "한국어는",
        'choices': ["한국어가", "한국어는", "한국어를", "한국어이"]
    },
    {
        'text': "<p><strong>A: 주말에 보통 뭐 하면서 시간을 보내세요?<br>B: 집에서 재미있는 영화________ 보거나 음악을 들어요.</strong></p>",
        'explanation': "<p><strong>영화를</strong>: '보다' (ko'rmoq) fe'lining obyekti bo'lgani uchun tushum kelishigi (<code>-을/를</code>) ishlatiladi. '영화' unli bilan tugagani uchun <code>를</code> keladi.</p>",
        'correct': "영화를",
        'choices': ["영화가", "영화는", "영화를", "영화이"]
    },
    {
        'text': "<p><strong>A: 저기요, 아까 주문한 음식________ 아직 안 나왔어요.<br>B: 죄송합니다, 손님. 주방에 확인해 보고 바로 가져다 드리겠습니다.</strong></p>",
        'explanation': "<p><strong>음식이</strong>: Muayyan holatning egasini ko'rsatish va yangi faktni (ovqat chiqmaganini) ta'kidlash uchun ega kelishigi (<code>-이/가</code>) ishlatiladi.</p>",
        'correct': "음식이",
        'choices': ["음식은", "음식이", "음식을", "음식가"]
    },
    {
        'text': "<p><strong>A: 와, 동생분이 키가 아주 크네요!<br>B: 네, 제 남동생________ 키가 커요. 하지만 여동생은 키가 작아요.</strong></p>",
        'explanation': "<p><strong>남동생은</strong>: Bu yerda 'uksam (남동생)' va 'singlim (여동생)' bir-biriga solishtirilmoqda (kontrast). Taqqoslash vaziyatlarida majburiy ravishda mavzu yuklamasi (<code>-은/는</code>) ishlatiladi.</p>",
        'correct': "남동생은",
        'choices': ["남동생이", "남동생은", "남동생을", "남동생가"]
    },
    {
        'text': "<p><strong>A: 아지즈 씨, 어제 왜 전화를 안 받았어요?<br>B: 미안해요, 핸드폰________ 고장 나서 수리점에 맡겼었어요.</strong></p>",
        'explanation': "<p><strong>핸드폰이</strong>: 'Buzilib qoldi' holatining bevosita egasi telefon bo'lgani va sababini tushuntirayotgani uchun ega kelishigi (<code>-이/가</code>) eng to'g'ri variant hisoblanadi.</p>",
        'correct': "핸드폰이",
        'choices': ["핸드폰은", "핸드폰이", "핸드폰을", "핸드폰가"]
    },
    {
        'text': "<p><strong>A: 배가 너무 고픈데 냉장고에 먹을 게 있을까요?<br>B: 냉장고 안에 우유________ 맛있는 빵이 조금 있어요. 먹으세요.</strong></p>",
        'explanation': "<p><strong>우유와</strong>: Bu yerda variantlar orasida to'g'ri keladigan bog'lovchi yoki tushum zanjiri tahlil qilinadi. Ammo gap oxirida '빵이 있어요' bo'lgani uchun, undan oldingi otlarni moslash kerak. Variantlarda to'g'ri shakl berilmagan taqdirda, tushum kelishigi zanjiri tekshiriladi. '우유를' orqali nonni yeyish obyekti qilish mumkin edi, lekin 'bor' fe'li (있다) kelganda subyekt zanjiri tutiladi. (Tuzatish: Bu savolda variantlarni to'g'rilab <code>우유하고</code> yoki <code>우유가</code> o'rniga tushum so'ralmoqda deb hisoblasak, gap strukturasi o'zgaradi. Keling, sodda obyekti bor savolga almashtiramiz):<br><strong>A: 마트에 가서 뭐 살 거예요?<br>B: 우유________ 맛있는 빵을 좀 살 거예요.</strong></p>",
        'explanation_fixed': "<p><strong>우유를</strong>: '살 거예요' (sotib olmoqchiman) o'timli fe'li uchun 'u-yu' (sut) so'zi obyektdir, shuning uchun <code>를</code> qo'yiladi.</p>",
        'correct': "우유를",
        'choices': ["우유가", "우유는", "우유를", "우유이"]
    },
    {
        'text': "<p><strong>A: 안바르 씨, 이번 시험 준비는 잘 하셨어요?<br>B: 수학은 아주 쉬웠어요. 그런데 과학________ 너무 어려워서 걱정이에요.</strong></p>",
        'explanation': "<p><strong>과학은</strong>: Matematika (수학은) oson bo'lgani, lekin tabiatshunoslik (과학) qiyin bo'lganini qarama-qarshi qo'yib taqqoslash (kontrast) uchun <code>-은/는</code> ishlatiladi.</p>",
        'correct': "과학은",
        'choices': ["과학이", "과학은", "과학을", "과학가"]
    },
    {
        'text': "<p><strong>A: 밖에서 무슨 소리가 나는 것 같아요. 나가 볼까요?<br>B: 아, 그냥 바람________ 많이 불어서 문이 흔들리는 소리예요.</strong></p>",
        'explanation': "<p><strong>바람이</strong>: '바람이 불다' (shamol esmoq) birikmasida shamol gapning egasi hisoblanadi. Undosh bilan tugagani uchun <code>이</code> qo'shiladi.</p>",
        'correct': "바람이",
        'choices': ["바람은", "바람이", "바람을", "바람가"]
    },
    {
        'text': "<p><strong>A: 커피를 좋아하세요, 아니면 차를 좋아하세요?<br>B: 저는 커피________ 전혀 안 마셔요. 보통 녹차를 마셔요.</strong></p>",
        'explanation': "<p><strong>커피는</strong>: Umumiy mavzu sifatida 'Kofega kelsak, men uni ichmayman' deb o'z odatini taqqoslab aytayotgani uchun <code>는</code> yuklamasi mos keladi.</p>",
        'correct': "커피는",
        'choices': ["커피가", "커피는", "커피를", "커피이"]
    },
    {
        'text': "<p><strong>A: 흐엉 씨, 한국 요리를 잘해요?<br>B: 잘 못해요. 하지만 불고기________ 맛이 괜찮게 만들 수 있어요.</strong></p>",
        'explanation': "<p><strong>불고기는</strong>: Boshqa ovqatlarni yaxshi qilolmasligini, lekin aynan bulgogini (boshqalariga qaraganda) yaxshi qila olishini taqqoslab ajratish uchun <code>는</code> ishlatiladi.</p>",
        'correct': "불고기는",
        'choices': ["불고기가", "불고기는", "불고기를", "불고기이"]
    },
    {
        'text': "<p><strong>A: 오늘 아침에 지각했지요? 왜 늦었어요?<br>B: 평소보다 도로에 차________ 너무 많아서 버스가 움직이지 못했어요.</strong></p>",
        'explanation': "<p><strong>차가 [[이/가]]</strong>: '차' (mashina) so'zi '많다' (ko'p) sifatining egasi hisoblanadi. Unli bilan tugagani uchun <code>가</code> kelishi shart.</p>",
        'correct': "차가",
        'choices': ["차는", "차가", "차를", "차이"]
    },
    {
        'text': "<p><strong>A: 새로 산 노트북이 어때요? 마음에 들어요?<br>B: 네, 디자인________ 아주 깔끔하고 속도도 엄청 빨라요.</strong></p>",
        'explanation': "<p><strong>디자인이</strong>: Noutbukning muayyan bir qismi yoki xususiyatini ajratib ko'rsatib, uning holatini (깔끔하다) tasvirlash uchun ega kelishigi <code>이</code> ishlatiladi.</p>",
        'correct': "디자인이",
        'choices': ["디자인은", "디자인이", "디자인을", "디자인가"]
    },
    {
        'text': "<p><strong>A: 주말에 친구들과 같이 축구 경기 보러 가기로 했어요?<br>B: 아니요, 친구들이 바쁘다고 해서 그냥 혼자 야구________ 보러 가려고요.</strong></p>",
        'explanation': "<p><strong>야구를</strong>: '보러 가다' (ko'rishga bormoq) harakatining obyekti '야구' (beysbol) bo'lgani uchun tushum kelishigi (<code>-을/를</code>) qo'llanadi.</p>",
        'correct': "야구를",
        'choices': ["야구가", "야구는", "야구를", "야구이"]
    },
    {
        'text': "<p><strong>A: 오늘 저녁 사 주셔서 감사합니다. 정말 잘 먹었습니다.<br>B: 아닙니다. 다음에는 아지즈 씨가 맛있는 음식________ 사 주세요.</strong></p>",
        'explanation': "<p><strong>음식을</strong>: '사 주다' (sotib bermoq / mehmon qilmoq) fe'lining bevosita to'ldiruvchisi '음식' (taom) so'zidir, shu bois <code>을</code> keladi.</p>",
        'correct': "음식을",
        'choices': ["음식이", "음식은", "음식을", "음식가"]
    },
    {
        'text': "<p><strong>A: 안바르 씨, 이번 휴가 때 고향에 갈 거예요?<br>B: 네, 고향에 계시는 부모님________ 너무 보고 싶어서 꼭 갈 거예요.</strong></p>",
        'explanation': "<p><strong>부모님이</strong>: Koreys tilida '보고 싶다' (sog'inmoq/ko'rgisi kelmoq) iborasi bilan ko'pincha subyekt qaratilib ega kelishigi (<code>-이/가</code>) ishlatilishi juda qonuniyatli va tabiiy hisoblanadi.</p>",
        'correct': "부모님이",
        'choices': ["부모님은", "부모님이", "부모님을", "부모님가"]
    },
    {
        'text': "<p><strong>A: 실례지만 누구를 찾으러 오셨습니까?<br>B: 김영수 과장님________ 자리에 계십니까? 만나러 왔습니다.</strong></p>",
        'explanation': "<p><strong>과장님이</strong>: '자리에 있다' (joyida bo'lmoq) fe'lining egasini aniqlashtirish uchun <code>이</code> kelishigi ishlatiladi.</p>",
        'correct': "과장님이",
        'choices': ["과장님은", "과장님이", "과장님을", "과장님가"]
    },
    {
        'text': "<p><strong>A: 소라 씨, 아까 산 가방은 어디에 뒀어요?<br>B: 너무 무거워서 거실에 있는 책상 위________ 올려두었어요.</strong></p>",
        'explanation': "<p><strong>(Asosiy Kelishiklar kontekstiga moslash uchun tushum o'zgartirildi): B: 가방________ 너무 무거워서 거실 책상 위에 올려두었어요.</strong></p>",
        'explanation_fixed': "<p><strong>가방이</strong>: '무겁다' (og'ir) sifatining egasi sumka bo'lgani uchun ega kelishigi <code>이</code> qo'yiladi.</p>",
        'correct': "가방이",
        'choices': ["가방은", "가방이", "가방을", "가방가"]
    },
    {
        'text': "<p><strong>A: 이 두 우산 중에서 어떤 것이 안바르 씨의 것이에요?<br>B: 이 파란색 우산________ 제 것입니다. 검은색은 친구 거예요.</strong></p>",
        'explanation': "<p><strong>우산이</strong>: Bir nechta narsa ichidan aynan bittasini aniq ajratib 'mana shu' deb ko'rsatganda (Ega ta'kidlanganda) <code>-이/가</code> ishlatiladi.</p>",
        'correct': "우산이",
        'choices': ["우산은", "우산이", "우산을", "우산가"]
    },
    {
        'text': "<p><strong>A: 매일 저녁에 퇴근하고 나면 보통 뭐 하세요?<br>B: 건강을 위해서 동네 한 바퀴 시원하게 산책________ 해요.</strong></p>",
        'explanation': "<p><strong>산책을</strong>: '하다' fe'li bilan birga kelib 'sayr qilmoq' iborasini yasayotgan so'zga tushum kelishigi (<code>-을/를</code>) qo'shiladi. Undosh bilan tugagani uchun <code>을</code> to'g'ri.</p>",
        'correct': "산책을",
        'choices': ["산책이", "산책은", "산책을", "산책가"]
    },
    {
        'text': "<p><strong>A: 어제 새로 오픈한 우즈베크 식당에 가 봤어요?<br>B: 네, 가 봤어요. 그런데 거기는 전통 빵________ 팔지 않아서 아쉬웠어요.</strong></p>",
        'explanation': "<p><strong>빵을</strong>: '팔다' (sotmoq) fe'lining bevosita obyekti non bo'lgani sababli tushum kelishigi <code>을</code> kelishi lozim.</p>",
        'correct': "빵을",
        'choices': ["빵이", "빵은", "빵을", "빵가"]
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
            title='1-dars: Asosiy Kelishiklar',  # --- IGNORE ---
            master=master,
            defaults={
                'description': 'Koreys tili - 3 dars: Asosiy kelishiklar (Egalik hamda tushum kelishiklari)',
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
