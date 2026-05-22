from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
    # --- 1-bo'lim. Zamonlar (Tenses) ---
    {
        'text': "<p><strong>A: 지수 씨는 보통 주말에 무엇을 하십니까?<br>B: 저는 주로 공원에서 음악을 ________.</strong></p>",
        'explanation': "<p><strong>듣습니다</strong>: '듣다' (eshitmoq) ㄷ-noto'g'ri fe'li, lekin <code>-습니다</code> kabi undosh qo'shimchalar oldidan ㄷ harfi o'zgarmaydi. Hozirgi zamon rasmiy uslubi.</p>",
        'correct': "듣습니다",
        'choices': ["들습니다", "듣습니다", "들어요", "듣어요"]
    },
    {
        'text': "<p><strong>A: 요즘 날씨가 어때요?<br>B: 겨울이라서 바람이 많이 불고 무척 ________.</strong></p>",
        'explanation': "<p><strong>추워요</strong>: '춥다' (sovuq bo'lmoq) ㅂ-noto'g'ri sifat. <code>-아/어요</code> qo'shilganda ㅂ harfi 우 ga aylanadi. 춥다 → 추워요.</p>",
        'correct': "추워요",
        'choices': ["춥어요", "추워요", "추와요", "추웠어요"]
    },
    {
        'text': "<p><strong>A: 어제 저녁에 친구를 만났어요?<br>B: 네, 만나서 같이 맛있는 불고기를 ________.</strong></p>",
        'explanation': "<p><strong>먹었어요</strong>: Savol kechagi kun (어제) haqida bo'lgani uchun o'tgan zamon <code>-았/었어요</code> ishlatiladi. 먹다 → 먹었어요.</p>",
        'correct': "먹었어요",
        'choices': ["먹어요", "먹을 거예요", "먹고 있어요", "먹었어요"]
    },
    {
        'text': "<p><strong>A: 내일 방학인데 뭐 할 거예요?<br>B: 저는 가족들과 제주도로 여행을 ________.</strong></p>",
        'explanation': "<p><strong>갈 거예요</strong>: Ertangi kun (내일) rejalari haqida gap ketganda kelasi zamon <code>-(으)ㄹ 거예요</code> ishlatiladi. 가다 → 갈 거예요.</p>",
        'correct': "갈 거예요",
        'choices': ["갔어요", "가고 있어요", "갈 거예요", "갑니다"]
    },
    {
        'text': "<p><strong>A: 지금 도서관에서 무엇을 해요?<br>B: 내일 시험이 있어서 한국어를 ________.</strong></p>",
        'explanation': "<p><strong>공부하고 있어요</strong>: Hozirgi ayni paytdagi (지금) harakatni bildirish uchun davomiy zamon <code>-고 있다</code> ishlatiladi.</p>",
        'correct': "공부하고 있어요",
        'choices': ["공부했어요", "공부할 거예요", "공부하고 있어요", "공부해요"]
    },
    {
        'text': "<p><strong>A: 이 식당에 와 본 적이 있어요?<br>B: 네, 작년에 한 번 ________. 그런데 맛이 기억이 안 나요.</strong></p>",
        'explanation': "<p><strong>왔었어요</strong>: O'tgan yili (작년) sodir bo'lgan va hozirgi paytga aloqasi yo'q bo'lgan tugallangan harakat uchun uzoq o'tgan zamon <code>-았/었었어요</code> ishlatiladi.</p>",
        'correct': "왔었어요",
        'choices': ["왔어요", "오고 있어요", "올 거예요", "왔었어요"]
    },
    {
        'text': "<p><strong>A: 수진 씨, 머리가 많이 기네요.<br>B: 네, 머리를 계속 ________.</strong></p>",
        'explanation': "<p><strong>기르고 있어요</strong>: '기르다' (o'stirmoq) 르-noto'g'ri fe'li, lekin <code>-고 있다</code> qo'shilganda o'zak o'zgarmaydi.</p>",
        'correct': "기르고 있어요",
        'choices': ["길러요", "기르고 있어요", "길렀어요", "기를 거예요"]
    },
    {
        'text': "<p><strong>A: 이번 주말에 약속이 있어요?<br>B: 네, 친구를 ________.</strong></p>",
        'explanation': "<p><strong>만날 거예요</strong>: Kelayotgan dam olish kunidagi reja haqida gapirilgani uchun kelasi zamon <code>-(으)ㄹ 거예요</code> ishlatiladi.</p>",
        'correct': "만날 거예요",
        'choices': ["만났어요", "만나고 있어요", "만날 거예요", "만나요"]
    },
    {
        'text': "<p><strong>A: 어제 산 책이 어땠어요?<br>B: 내용이 아주 ________.</strong></p>",
        'explanation': "<p><strong>좋았어요</strong>: O'tmishdagi holat (kechagi kitob) haqida so'ralmoqda. '좋다' sifati uchun o'tgan zamon <code>-았/었어요</code> ishlatiladi.</p>",
        'correct': "좋았어요",
        'choices': ["좋아요", "좋고 있어요", "좋을 거예요", "좋았어요"]
    },
    {
        'text': "<p><strong>A: 민수 씨는 지금 어디에 있습니까?<br>B: 방에서 잠을 ________.</strong></p>",
        'explanation': "<p><strong>잡니다</strong>: Hozirgi zamon rasmiy uslubi <code>-(스)ㅂ니다</code>. 자다 + ㅂ니다 = 잡니다.</p>",
        'correct': "잡니다",
        'choices': ["잘 겁니다", "잤습니다", "잡니다", "자고 있습니다"]
    },

    # --- 2-bo'lim. Inkor ifodalari (Negative Expressions) ---
    {
        'text': "<p><strong>A: 고기를 좋아하세요?<br>B: 아니요, 저는 고기를 ________. 채소만 먹어요.</strong></p>",
        'explanation': "<p><strong>안 먹어요</strong>: Harakatni bajarmaslik xohishini yoki odatni bildiradi. <code>안 A/V-아/어요</code> qisqa inkori ishlatiladi.</p>",
        'correct': "안 먹어요",
        'choices': ["못 먹어요", "안 먹어요", "먹지 않아요", "안 먹었어요"]
    },
    {
        'text': "<p><strong>A: 어제 밤에 잠을 잘 잤어요?<br>B: 아니요, 밖이 너무 시끄러워서 한숨도 ________.</strong></p>",
        'explanation': "<p><strong>못 잤어요</strong>: Tashqi sabablarga ko'ra (shovqin) uxlash imkoni bo'lmaganligi uchun <code>못 V-아/어요</code> ishlatiladi.</p>",
        'correct': "못 잤어요",
        'choices': ["안 잤어요", "못 잤어요", "자지 않았어요", "안 자요"]
    },
    {
        'text': "<p><strong>A: 이 가방이 무거워요?<br>B: 아니요, 생각보다 ________.</strong></p>",
        'explanation': "<p><strong>무겁지 않아요</strong>: Sifatlar uchun '못' inkor yuklamasi ishlatilmaydi, uning o'rniga '안' yoki uzun inkor <code>-지 않다</code> ishlatiladi.</p>",
        'correct': "무겁지 않아요",
        'choices': ["무겁지 않아요", "못 무거워요", "무겁지 못해요", "무거웠어요"]
    },
    {
        'text': "<p><strong>A: 피아노를 칠 줄 알아요?<br>B: 아니요, 한 번도 배운 적이 없어서 ________.</strong></p>",
        'explanation': "<p><strong>치지 못해요</strong>: Qobiliyat yo'qligini bildiradi. Uzun inkor shakli <code>-지 못하다</code> ishlatiladi.</p>",
        'correct': "치지 못해요",
        'choices': ["안 쳐요", "치지 않아요", "치지 못해요", "못 쳤어요"]
    },
    {
        'text': "<p><strong>A: 오늘 회의에 참석할 수 있어요?<br>B: 죄송해요. 일이 너무 많아서 참석하지 ________.</strong></p>",
        'explanation': "<p><strong>못해요</strong>: Ish ko'pligi sababli qatnasha olmaslikni (imkonsizlikni) bildirish uchun <code>V-지 못하다</code> ishlatiladi.</p>",
        'correct': "못해요",
        'choices': ["않아요", "못해요", "안 해요", "없어요"]
    },
    {
        'text': "<p><strong>A: 지민 씨는 대학생이에요?<br>B: 아니요, 저는 대학생이 ________. 직장인이에요.</strong></p>",
        'explanation': "<p><strong>아니에요</strong>: Otlarni inkor qilish uchun <code>N이/가 아니다</code> ishlatiladi.</p>",
        'correct': "아니에요",
        'choices': ["안 이에요", "못 이에요", "없어요", "아니에요"]
    },
    {
        'text': "<p><strong>A: 그 치마가 예뻐요?<br>B: 아니요, 디자인이 별로 ________.</strong></p>",
        'explanation': "<p><strong>예쁘지 않아요</strong>: '예쁘다' sifati. Sifatni inkor qilish uchun <code>-지 않다</code> mos keladi.</p>",
        'correct': "예쁘지 않아요",
        'choices': ["예쁘지 못해요", "안 예뻐서", "예쁘지 않아요", "예쁘지 않아요"]
    },
    {
        'text': "<p><strong>A: 내일 파티에 갈 거예요?<br>B: 아니요, 피곤해서 ________.</strong></p>",
        'explanation': "<p><strong>안 갈 거예요</strong>: O'z xohishi bilan bormaslik rejasini bildirish uchun <code>안</code> ishlatiladi.</p>",
        'correct': "안 갈 거예요",
        'choices': ["못 가요", "안 갈 거예요", "가지 못해요", "안 갔어요"]
    },
    {
        'text': "<p><strong>A: 커피를 자주 마셔요?<br>B: 아니요, 건강을 위해서 마시지 ________.</strong></p>",
        'explanation': "<p><strong>않아요</strong>: Odatni inkor qilish uchun uzun shakl <code>-지 않다</code>.</p>",
        'correct': "않아요",
        'choices': ["않아요", "못해요", "마셔요", "없어요"]
    },
    {
        'text': "<p><strong>A: 이 한자를 읽을 수 있어요?<br>B: 아니요, 너무 어려워서 전혀 ________.</strong></p>",
        'explanation': "<p><strong>못 읽어요</strong>: Qobiliyat yo'qligi va qiyinligi sabab o'qiy olmaslikni bildirish uchun <code>못</code> ishlatiladi.</p>",
        'correct': "못 읽어요",
        'choices': ["안 읽어요", "못 읽어요", "읽지 않아요", "읽을 줄 몰라요"]
    },

    # --- 3-bo'lim. Qo'shimchalar (Particles) ---
    {
        'text': "<p><strong>A: 밖에 비가 와요?<br>B: 아니요, 지금은 비가 안 오고 ________ 와요.</strong></p>",
        'explanation': "<p><strong>눈이</strong>: Ob-havo hodisalari bilan odatda ega qo'shimchasi <code>이/가</code> ishlatiladi. '눈' undosh bilan tugagani uchun '이' qo'shiladi.</p>",
        'correct': "눈이",
        'choices': ["눈은", "눈을", "눈이", "눈도"]
    },
    {
        'text': "<p><strong>A: 직업이 무엇입니까?<br>B: ________ 한국어 선생님입니다.</strong></p>",
        'explanation': "<p><strong>저는</strong>: O'zini tanishtirish yoki asosiy mavzuni belgilash uchun <code>은/는</code> ishlatiladi. '저' unli bilan tugagani uchun '는'.</p>",
        'correct': "저는",
        'choices': ["내가", "저를", "저는", "제가"]
    },
    {
        'text': "<p><strong>A: 도서관에서 무엇을 빌렸어요?<br>B: 재미있는 역사 ________ 빌렸어요.</strong></p>",
        'explanation': "<p><strong>책을</strong>: Tushum kelishigi qo'shimchasi <code>을/를</code>. '책' undosh bilan tugagani uchun '을' ishlatiladi.</p>",
        'correct': "책을",
        'choices': ["책이", "책은", "책을", "책에"]
    },
    {
        'text': "<p><strong>A: 빵집에서 무엇을 샀어요?<br>B: 케이크________ 우유를 샀어요.</strong></p>",
        'explanation': "<p><strong>와</strong>: Otlarni bog'lashda 'va' ma'nosida <code>와/과</code> ishlatiladi. '케이크' unli bilan tugagani uchun '와' bo'ladi.</p>",
        'correct': "와",
        'choices': ["과", "와", "이나", "에"]
    },
    {
        'text': "<p><strong>A: 이 우산은 누구의 것이에요?<br>B: 제 ________ 우산이에요.</strong></p>",
        'explanation': "<p><strong>친구의</strong>: Qaratqich kelishigi <code>의</code> (ning) egalikni bildiradi.</p>",
        'correct': "친구의",
        'choices': ["친구가", "친구를", "친구의", "친구에"]
    },
    {
        'text': "<p><strong>A: 보통 언제 운동을 해요?<br>B: 저는 매일 아침________ 운동해요.</strong></p>",
        'explanation': "<p><strong>에</strong>: Vaqtni bildiruvchi so'zlarga (아침, 1시 va hk) harakat qachon sodir bo'lishini ko'rsatish uchun <code>에 1</code> qo'shiladi.</p>",
        'correct': "에",
        'choices': ["에서", "은", "를", "에"]
    },
    {
        'text': "<p><strong>A: 내일 어디에 가요?<br>B: 친구를 만나러 명동________ 가요.</strong></p>",
        'explanation': "<p><strong>에</strong>: Yo'nalish/manzilni bildiruvchi <code>에 2</code> qo'shimchasi 가다, 오다 kabi fe'llar bilan ishlatiladi.</p>",
        'correct': "에",
        'choices': ["을", "에서", "에", "까지"]
    },
    {
        'text': "<p><strong>A: 주말에 어디에서 데이트를 했어요?<br>B: 영화관________ 영화를 보고 밥을 먹었어요.</strong></p>",
        'explanation': "<p><strong>에서</strong>: Harakat sodir bo'layotgan joyni ko'rsatish uchun <code>에서</code> ishlatiladi.</p>",
        'correct': "에서",
        'choices': ["에", "에서", "으로", "까지"]
    },
    {
        'text': "<p><strong>A: 회의는 언제 시작해요?<br>B: 오후 2시________ 4시까지 해요.</strong></p>",
        'explanation': "<p><strong>부터</strong>: Vaqt oralig'ini bildiruvchi <code>부터</code> (dan) qo'shimchasi <code>까지</code> (gacha) bilan birga keladi.</p>",
        'correct': "부터",
        'choices': ["에서", "부터", "에", "까지"]
    },
    {
        'text': "<p><strong>A: 집에서 학교까지 얼마나 걸려요?<br>B: 버스로 30분 ________ 걸려요.</strong></p>",
        'explanation': "<p><strong>쯤</strong>: <code>쯤</code> qo'shimchasi taxminan miqdor yoki vaqtni (atrofida, chasi) bildiradi.</p>",
        'correct': "쯤",
        'choices': ["만", "쯤", "도", "밖에"]
    },
    {
        'text': "<p><strong>A: 누구에게 편지를 썼어요?<br>B: 고향에 계신 부모님________ 썼어요.</strong></p>",
        'explanation': "<p><strong>께</strong>: <code>에게/한테</code> ning hurmat shakli <code>께</code> hisoblanadi. Ota-onaga nisbatan hurmat yuzasidan ishlatiladi.</p>",
        'correct': "께",
        'choices': ["에게", "한테", "께", "에서"]
    },
    {
        'text': "<p><strong>A: 수진 씨는 사과를 좋아해요?<br>B: 네, 사과를 좋아해요. 그리고 포도________ 좋아해요.</strong></p>",
        'explanation': "<p><strong>도</strong>: <code>도</code> qo'shimchasi 'ham' ma'nosini bildiradi va 이/가 yoki 을/를 o'rnida keladi.</p>",
        'correct': "도",
        'choices': ["를", "는", "만", "도"]
    },
    {
        'text': "<p><strong>A: 교실에 학생이 많아요?<br>B: 아니요, 오늘은 비가 와서 5명________ 안 왔어요.</strong></p>",
        'explanation': "<p><strong>밖에</strong>: <code>밖에</code> (dan boshqa/faqat) qo'shimchasi har doim inkor fe'llari (안, 못, 없다) bilan birga keladi.</p>",
        'correct': "밖에",
        'choices': ["만", "밖에", "도", "쯤"]
    },
    {
        'text': "<p><strong>A: 서울에서 부산까지 어떻게 가요?<br>B: 보통 KTX(기차)________ 가요.</strong></p>",
        'explanation': "<p><strong>로</strong>: Vosita yoki transport turini bildirish uchun <code>(으)로</code> ishlatiladi. '기차' unli bilan tugagani uchun '로' bo'ladi.</p>",
        'correct': "로",
        'choices': ["으로", "로", "에서", "에"]
    },
    {
        'text': "<p><strong>A: 목이 마른데 마실 것 좀 있어요?<br>B: 물________ 주스 중에 뭐 드릴까요?</strong></p>",
        'explanation': "<p><strong>이나</strong>: Otlar orasida tanlovni (yoki) bildirish uchun <code>(이)나 1</code> ishlatiladi. '물' undosh bilan tugagani uchun '이나' bo'ladi.</p>",
        'correct': "이나",
        'choices': ["나", "이나", "도", "만"]
    },
    {
        'text': "<p><strong>A: 어제 술을 많이 마셨어요?<br>B: 네, 맥주를 5병________ 마셨어요.</strong></p>",
        'explanation': "<p><strong>이나</strong>: Miqdorning kutilganidan ko'pligini ifodalash uchun <code>(이)나 2</code> ishlatiladi.</p>",
        'correct': "이나",
        'choices': ["이나", "밖에", "쯤", "만"]
    },
    {
        'text': "<p><strong>A: 지민 씨는 얼굴이 정말 작네요.<br>B: 네, 주먹________ 작아요.</strong></p>",
        'explanation': "<p><strong>처럼</strong>: O'xshatish ma'nosida <code>처럼</code> (kabi/dek) ishlatiladi (mushtdek kichkina).</p>",
        'correct': "처럼",
        'choices': ["처럼", "보다", "에", "에서"]
    },
    {
        'text': "<p><strong>A: 지하철이 빨라요, 버스가 빨라요?<br>B: 서울에서는 지하철이 버스________ 훨씬 빨라요.</strong></p>",
        'explanation': "<p><strong>보다</strong>: Ikki narsani solishtirishda <code>보다</code> (-ga qaraganda/dan ko'ra) ishlatiladi.</p>",
        'correct': "보다",
        'choices': ["처럼", "까지", "보다", "부터"]
    },
    {
        'text': "<p><strong>A: 주말마다 등산을 가요?<br>B: 네, 일요일________ 산에 가요.</strong></p>",
        'explanation': "<p><strong>마다</strong>: <code>마다</code> qo'shimchasi 'har' ma'nosini bildiradi. 일요일마다 = har yakshanba.</p>",
        'correct': "마다",
        'choices': ["도", "만", "마다", "부터"]
    },
    {
        'text': "<p><strong>A: 요즘 다이어트 중이에요?<br>B: 네, 그래서 점심에는 샐러드________ 먹어요.</strong></p>",
        'explanation': "<p><strong>만</strong>: <code>만</code> qo'shimchasi 'faqat' ma'nosini bildiradi va tasdiq fe'llari bilan keladi.</p>",
        'correct': "만",
        'choices': ["만", "밖에", "도", "나"]
    },
    {
        'text': "<p><strong>A: 혼자 밥을 먹었어요?<br>B: 아니요, 룸메이트________ 같이 먹었어요.</strong></p>",
        'explanation': "<p><strong>하고</strong>: <code>하고 / (이)랑</code> 'bilan' ma'nosida og'zaki nutqda ko'p ishlatiladi.</p>",
        'correct': "랑",
        'choices': ["를", "랑", "에", "이나"]
    },

    # --- 4-bo'lim. Sanash va Qiyoslash (Listing and Contrast) ---
    {
        'text': "<p><strong>A: 이 식당 음식이 어때요?<br>B: 가격도 싸________ 아주 맛있어요.</strong></p>",
        'explanation': "<p><strong>고</strong>: Ikkita ijobiy sifatni ketma-ket sanash uchun <code>-고</code> (va) ishlatiladi (싸다 + 고).</p>",
        'correct': "고",
        'choices': ["고", "거나", "지만", "는데"]
    },
    {
        'text': "<p><strong>A: 보통 주말에 뭐 하면서 쉬어요?<br>B: 집에서 책을 읽________ 음악을 들어요.</strong></p>",
        'explanation': "<p><strong>거나</strong>: Ikki harakatdan birini tanlashni (yoki) ko'rsatish uchun <code>-거나</code> ishlatiladi.</p>",
        'correct': "거나",
        'choices': ["지만", "거나", "고", "는데"]
    },
    {
        'text': "<p><strong>A: 한국어 공부가 재미있어요?<br>B: 네, 조금 어렵________ 정말 재미있어요.</strong></p>",
        'explanation': "<p><strong>지만</strong>: Qarama-qarshilikni (lekin/biroq) ifodalash uchun <code>-지만</code> ishlatiladi. 어렵다 + 지만 = 어렵지만.</p>",
        'correct': "지만",
        'choices': ["고", "거나", "지만", "은데"]
    },
    {
        'text': "<p><strong>A: 밖은 날씨가 어때요?<br>B: 바람이 많이 부________ 춥지는 않아요.</strong></p>",
        'explanation': "<p><strong>는데</strong>: <code>-(으)ㄴ/는데 1</code> fe'llar bilan kelib, yumshoq qarama-qarshilik yoki fon ma'lumotni bildiradi. '불다' 르-noto'g'ri fe'l bo'lgani uchun ㄹ tushib qoladi: 부는데.</p>",
        'correct': "는데",
        'choices': ["는데", "은데", "고", "거나"]
    },
    {
        'text': "<p><strong>A: 언니는 키가 큰데, 동생은 어때요?<br>B: 동생은 키가 작________ 귀여워요.</strong></p>",
        'explanation': "<p><strong>은데</strong>: Sifatlar undosh bilan tugaganda qarama-qarshilikni bildirish uchun <code>-은데</code> qo'shiladi (작다 -> 작은데).</p>",
        'correct': "은데",
        'choices': ["는데", "은데", "고", "지만"]
    },
    {
        'text': "<p><strong>A: 그 가방을 살 거예요?<br>B: 아니요. 디자인은 예쁘________ 너무 비싸서 안 살 거예요.</strong></p>",
        'explanation': "<p><strong>지만</strong>: <code>-지만</code> orqali '예쁘다' (chiroyli) va '비싸다' (qimmat) xususiyatlari kuchli qarama-qarshilikda berilyapti.</p>",
        'correct': "지만",
        'choices': ["고", "거나", "지만", "아서"]
    },
    {
        'text': "<p><strong>A: 주말에 여행을 갈 거예요?<br>B: 날씨가 맑으면 가________ 비가 오면 안 갈 거예요.</strong></p>",
        'explanation': "<p><strong>고</strong>: Ikkita alohida gapni bir-biriga bog'lash uchun <code>-고</code> ishlatiladi.</p>",
        'correct': "고",
        'choices': ["고", "거나", "은데", "어서"]
    },

    # --- 5-bo'lim. Vaqt ifodalari (Time Expressions) ---
    {
        'text': "<p><strong>A: 약을 언제 먹어야 해요?<br>B: 밥을 먹________ 꼭 드세요.</strong></p>",
        'explanation': "<p><strong>기 전에</strong>: <code>V-기 전에</code> 'biror harakatni qilishdan oldin' ma'nosini bildiradi. 밥을 먹기 전에 = ovqatlanishdan oldin.</p>",
        'correct': "기 전에",
        'choices': ["은 후에", "고 나서", "기 전에", "아서"]
    },
    {
        'text': "<p><strong>A: 영화를 본 후에 뭐 할 거예요?<br>B: 영화가 끝난 ________ 커피를 마실 거예요.</strong></p>",
        'explanation': "<p><strong>후에</strong>: <code>V-(으)ㄴ 후에</code> 'qilganidan so'ng' ma'nosini bildiradi. 끝나다 + ㄴ 후에 = 끝난 후에.</p>",
        'correct': "후에",
        'choices': ["전에", "후에", "때", "고 나서"]
    },
    {
        'text': "<p><strong>A: 손은 언제 씻어야 해요?<br>B: 밖에서 돌아오________ 반드시 씻으세요.</strong></p>",
        'explanation': "<p><strong>고 나서</strong>: <code>V-고 나서</code> harakatlarning qat'iy ketma-ketligini (tugatib, keyin) ta'kidlaydi.</p>",
        'correct': "고 나서",
        'choices': ["고 나서", "기 전에", "을 때", "지만"]
    },
    {
        'text': "<p><strong>A: 어제 저녁에 뭐 했어요?<br>B: 친구를 만________ 같이 피자를 먹었어요.</strong></p>",
        'explanation': "<p><strong>나서</strong>: <code>V-아/어서</code> vaqt ketma-ketligini va birinchi harakat ikkinchisi uchun asos bo'lishini bildiradi (do'stni ko'rib, birga yeyish).</p>",
        'correct': "나서",
        'choices': ["나고", "나서", "난 후에", "나기 전에"]
    },
    {
        'text': "<p><strong>A: 언제 한국 노래를 자주 들어요?<br>B: 저는 기분이 좋________ 한국 노래를 들어요.</strong></p>",
        'explanation': "<p><strong>을 때</strong>: <code>A/V-(으)ㄹ 때</code> harakat yoki holat sodir bo'ladigan vaqtni (paytda) bildiradi. 좋다 + 을 때 = 좋을 때.</p>",
        'correct': "을 때",
        'choices': ["을 때", "기 전에", "은 후에", "고 나서"]
    },
    {
        'text': "<p><strong>A: 학생이________ 공부를 열심히 했어요?<br>B: 네, 도서관에서 살다시피 했어요.</strong></p>",
        'explanation': "<p><strong>었을 때</strong>: O'tmishdagi holatni otlar bilan ifodalash uchun <code>N이었/였을 때</code> ishlatiladi. 학생 + 이었을 때.</p>",
        'correct': "이었을 때",
        'choices': ["일 때", "이었을 때", "인 후에", "이기 전에"]
    },
    {
        'text': "<p><strong>A: 이 빵은 어떻게 만들어요?<br>B: 밀가루 반죽을 오븐에 구________ 설탕을 뿌리세요.</strong></p>",
        'explanation': "<p><strong>운 후에</strong>: 굽다 (pishirmoq) ㅂ-noto'g'ri fe'li. 굽다 + (으)ㄴ 후에 = 구운 후에.</p>",
        'correct': "운 후에",
        'choices': ["운 후에", "은 후에", "기 전에", "고 나서"]
    },
    {
        'text': "<p><strong>A: 너무 바쁘면 도와줄까요?<br>B: 괜찮아요. 제가 너무 바________ 말할게요.</strong></p>",
        'explanation': "<p><strong>쁠 때</strong>: 바쁘다 (band bo'lmoq) + ㄹ 때 = 바쁠 때.</p>",
        'correct': "쁠 때",
        'choices': ["빠서", "쁠 때", "쁜 후에", "쁘기 전에"]
    },
    {
        'text': "<p><strong>A: 언제 고향에 돌아갈 거예요?<br>B: 대학교를 졸업한 ________ 돌아갈 계획이에요.</strong></p>",
        'explanation': "<p><strong>후에</strong>: 졸업하다 (bitirmoq) fe'liga o'tgan zamon sifatdoshi va 'so'ng' ma'nosidagi <code>후에</code> qo'shilgan.</p>",
        'correct': "후에",
        'choices': ["전에", "후에", "때", "고 나서"]
    },

    # --- Aralash mavzular (Mixed practice 1-5 units) ---
    {
        'text': "<p><strong>A: 지수 씨, 지금 음악을 ________?<br>B: 네, 좋아하는 가수의 신곡이 나와서요.</strong></p>",
        'explanation': "<p><strong>듣고 있어요</strong>: 듣다 (noto'g'ri fe'l) + 고 있다 = 듣고 있어요. Hozirgi davomiy zamon.</p>",
        'correct': "듣고 있어요",
        'choices': ["들고 있어요", "듣고 있어요", "들어 있어요", "듣었어요"]
    },
    {
        'text': "<p><strong>A: 매운 음식을 잘 먹어요?<br>B: 아니요, 저는 매운 것을 전혀 ________.</strong></p>",
        'explanation': "<p><strong>못 먹어요</strong>: '전혀 못 먹다' umuman yeya olmaslikni (qobiliyatsizlikni) ta'kidlaydi.</p>",
        'correct': "못 먹어요",
        'choices': ["안 먹어요", "못 먹어요", "먹지 않아요", "안 먹었어요"]
    },
    {
        'text': "<p><strong>A: 제주도는 어떤 점이 좋아요?<br>B: 바다가 아름답________ 공기가 맑아요.</strong></p>",
        'explanation': "<p><strong>고</strong>: Sifatlarni bog'lash (chiroyli va...). 아름답다 + 고.</p>",
        'correct': "고",
        'choices': ["고", "지만", "거나", "는데"]
    },
    {
        'text': "<p><strong>A: 버스가 왜 안 오죠?<br>B: 눈이 너무 많이 와서 차가 많이 막히________ 지하철을 탈까요?</strong></p>",
        'explanation': "<p><strong>는데</strong>: <code>-(으)ㄴ/는데</code> holatni tushuntirib, keyingi gap (taklif) uchun fon vazifasini bajaradi.</p>",
        'correct': "는데",
        'choices': ["고", "는데", "거나", "지만"]
    },
    {
        'text': "<p><strong>A: 김치찌개를 만들 줄 알아요?<br>B: 네, 먼저 고기를 볶________ 물을 넣고 끓이세요.</strong></p>",
        'explanation': "<p><strong>고 나서</strong>: Harakatlarning tartibini bildiradi. Qovurib bo'lgach (볶다 + 고 나서).</p>",
        'correct': "고 나서",
        'choices': ["기 전에", "고 나서", "지만", "을 때"]
    },
    {
        'text': "<p><strong>A: 저 식당은 어때요?<br>B: 음식이 맛없________ 서비스도 별로예요.</strong></p>",
        'explanation': "<p><strong>고</strong>: Ikkita salbiy xususiyatni sanab o'tish uchun <code>-고</code>.</p>",
        'correct': "고",
        'choices': ["고", "지만", "은데", "어서"]
    },
    {
        'text': "<p><strong>A: 감기에 걸려서 목이 아파요.<br>B: 따뜻한 물을 많이 마시________ 약을 드세요.</strong></p>",
        'explanation': "<p><strong>고</strong>: Ikkita maslahatni bir-biriga bog'lash uchun ishlatiladi.</p>",
        'correct': "고",
        'choices': ["고", "지만", "거나", "는데"]
    },
    {
        'text': "<p><strong>A: 어제 일찍 잤어요?<br>B: 숙제가 너무 많아서 새벽 2시________ 못 잤어요.</strong></p>",
        'explanation': "<p><strong>까지</strong>: Vaqt chegarasini bildiruvchi (gacha) qo'shimcha.</p>",
        'correct': "까지",
        'choices': ["부터", "까지", "에", "에서"]
    },
    {
        'text': "<p><strong>A: 요즘 매일 수영장에 가요?<br>B: 아니요, 시간이 없어서 일주일________ 한 번 가요.</strong></p>",
        'explanation': "<p><strong>에</strong>: Takrorlanish chastotasini bildirishda (haftada bir marta - 일주일에) <code>에</code> ishlatiladi.</p>",
        'correct': "에",
        'choices': ["에", "에서", "으로", "까지"]
    },
    {
        'text': "<p><strong>A: 이 신발은 너무 작지 않아요?<br>B: 아니요, 제 발에 아주 ________.</strong></p>",
        'explanation': "<p><strong>잘 맞아요</strong>: '맞다' (mos tushmoq) fe'lining hozirgi zamon shakli (A/V-아/어요).</p>",
        'correct': "맞아요",
        'choices': ["맞아요", "맞았어요", "맞을 거예요", "맞고 있어요"]
    },
    {
        'text': "<p><strong>A: 강아지가 참 귀엽네요.<br>B: 네, 솜사탕________ 털이 푹신푹신해요.</strong></p>",
        'explanation': "<p><strong>처럼</strong>: 'Paxta qand kabi' deb o'xshatish uchun <code>N처럼</code> ishlatiladi.</p>",
        'correct': "처럼",
        'choices': ["보다", "처럼", "만큼", "도"]
    },
    {
        'text': "<p><strong>A: 어렸을 때 시골에 살았어요?<br>B: 네, 10살________ 할머니 댁에서 지냈어요.</strong></p>",
        'explanation': "<p><strong>때</strong>: <code>N때</code> o'tmishdagi ma'lum bir davrni yoki yoshni bildiradi (10 yoshda).</p>",
        'correct': "때",
        'choices': ["전에", "후에", "때", "까지"]
    },
    {
        'text': "<p><strong>A: 기차표를 예매했어요?<br>B: 깜빡했어요. 내일 아침에 일어나________ 바로 할게요.</strong></p>",
        'explanation': "<p><strong>고 나서</strong>: Ketma-ketlikni ta'kidlash uchun 'turganimdan so'ng' (일어나고 나서).</p>",
        'correct': "고 나서",
        'choices': ["기 전에", "고 나서", "지만", "을 때"]
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
            title='Takrorlash.',  # --- IGNORE ---
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
