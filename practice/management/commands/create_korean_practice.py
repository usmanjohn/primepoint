from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
    {
        'text': "<p><strong>A: 아지즈 씨, 어제 시장에서 뭐 샀어요?<br>B: 시장에서 사과________ 바나나를 샀어요. 과일이 아주 싱싱해요.</strong></p>",
        'explanation': "<p><strong>사과와</strong>: '사과' unli bilan tugagani uchun rasmiy/yozma bog'lovchi yuklama <code>-와</code> to'g'ri keladi. Variantlar ichida eng to'g'ri grammatik juftlikdir.</p>",
        'correct': "사과와",
        'choices': ["사과과", "사과와", "사과이랑", "사과하고랑"]
    },
    {
        'text': "<p><strong>A: 주말에 보통 혼자 쇼핑을 해요?<br>B: 아니요, 저는 주말마다 친구________ 같이 쇼핑몰에 가요.</strong></p>",
        'explanation': "<p><strong>친구하고</strong>: Kimdir bilan birgalikda (같이) harakat qilishni ifodalashda neytral <code>-하고</code> yuklamasi juda keng qo'llaniladi.</p>",
        'correct': "친구하고",
        'choices': ["친구과", "친구하고", "친구이랑", "친구은"]
    },
    {
        'text': "<p><strong>A: 안바르 씨, 방에 책상이 있어요?<br>B: 네, 제 방에는 책상________ 침대가 모두 있습니다.</strong></p>",
        'explanation': "<p><strong>책상과</strong>: '책상' undosh (pochim) bilan tugagani uchun va gap '습니다' rasmiy uslubida bo'lgani sababli <code>-과</code> yuklamasi eng to'g'ri javobdir.</p>",
        'correct': "책상과",
        'choices': ["책상와", "책상과", "책상랑", "책상을"]
    },
    {
        'text': "<p><strong>A: 동생, 내일 나________ 같이 도서관에 갈래?<br>B: 응, 좋아! 내일 아침에 일찍 만나서 같이 가자.</strong></p>",
        'explanation': "<p><strong>랑</strong>: Yaqin insonlar o'rtasidagi norasmiy og'zaki nutqda (반말) unli bilan tugagan '나' (men) so'ziga <code>-랑</code> yuklamasi qo'shiladi.</p>",
        'correct': "랑",
        'choices': ["과", "이랑", "랑", "하고과"]
    },
    {
        'text': "<p><strong>A: 비빔밥에 보통 무슨 재료가 들어가요?<br>B: 여러 가지 야채________ 고기가 들어가서 아주 영양이 풍부해요.</strong></p>",
        'explanation': "<p><strong>야채하고</strong>: Ikki mahsulotni bir-biriga bog'lash uchun unli/undosh ajratmaydigan <code>-하고</code> yuklamasi muloqotda juda tabiiy eshitiladi.</p>",
        'correct': "야채하고",
        'choices': ["야채과", "야채하고", "야채이랑", "야채를"]
    },
    {
        'text': "<p><strong>A: 켈리 씨, 어제 퇴근하고 뭐 하셨어요?<br>B: 회사 동료들________ 함께 식당에서 삼겹살을 먹었어요.</strong></p>",
        'explanation': "<p><strong>동료들과</strong>: '함께' (birgalikda) so'zi bilan rasmiy tarzda ishlatilganda, undosh bilan tugagan '동료들' so'ziga <code>-과</code> qo'shiladi.</p>",
        'correct': "동료들과",
        'choices': ["동료들와", "동료들과", "동료들랑", "동료들하고랑"]
    },
    {
        'text': "<p><strong>A: 우즈베키스탄 전통 음식 중에서 뭐가 제일 유명해요?<br>B: 기름밥________ 샤실릭이 제일 인기가 많고 맛있어요.</strong></p>",
        'explanation': "<p><strong>기름밥이랑</strong>: '기름밥' undosh bilan tugagani uchun kundalik og'zaki nutq shakli bo'lgan <code>-이랑</code> yuklamasi variantlar orasida to'g'ri keladi.</p>",
        'correct': "기름밥이랑",
        'choices': ["기름밥랑", "기름밥이랑", "기름밥와", "기름밥과"]
    },
    {
        'text': "<p><strong>A: 오늘 아침 메뉴는 무엇이었습니까?<br>B: 간단하게 구운 빵________ 따뜻한 커피를 마셨습니다.</strong></p>",
        'explanation': "<p><strong>빵과</strong>: Gap '습니다' (rasmiy yozma uslub) bilan tugagani uchun, undosh bilan tugagan '빵' so'ziga <code>-과</code> yuklamasini qo'shish eng to'g'ri yechimdir.</p>",
        'correct': "빵과",
        'choices': ["빵와", "빵과", "빵랑", "빵하고랑"]
    },
    {
        'text': "<p><strong>A: 소라 씨, 이번 방학 때 누구하고 여행을 갈 거예요?<br>B: 고향에 있는 가족들________ 같이 제주도에 갈 계획이에요.</strong></p>",
        'explanation': "<p><strong>가족들하고</strong>: Savolda '누구하고' deb so'ralgani sababli, javobda ham unga mos ravishda <code>-하고</code> yuklamasidan foydalanish suhbatni ravon qiladi.</p>",
        'correct': "가족들하고",
        'choices': ["가족들와", "가족들하고", "가족들랑", "가족들을"]
    },
    {
        'text': "<p><strong>A: 수진아, 오늘 저녁에 김치찌개________ 불고기 중에서 뭘 먹을까?<br>B: 음, 나는 매콤한 김치찌개가 더 먹고 싶어.</strong></p>",
        'explanation': "<p><strong>찌개랑</strong>: Bir-biri bilan yaqin munosabatdagi og'zaki savolda unli bilan tugagan '찌개' so'zidan so'ng <code>-랑</code> yuklamasi keladi.</p>",
        'correct': "찌개랑",
        'choices': ["찌개과", "찌개랑", "찌개이랑", "찌개하고랑"]
    },
    {
        'text': "<p><strong>A: 한국의 겨울 날씨는 보통 어때요?<br>B: 눈이 많이 내리고 강한 바람________ 같이 찾아와서 아주 춥습니다.</strong></p>",
        'explanation': "<p><strong>바람과</strong>: Rasmiy tushuntirish berish jarayonida undosh bilan tugagan '바람' so'ziga <code>-과</code> yuklamasi qo'shiladi.</p>",
        'correct': "바람과",
        'choices': ["바람와", "바람과", "바람랑", "바람을"]
    },
    {
        'text': "<p><strong>A: 내일 학교에 갈 때 무엇을 가져가야 해요?<br>B: 교과서________ 필기도구를 꼭 챙겨오셔야 합니다.</strong></p>",
        'explanation': "<p><strong>교과서와</strong>: '교과서' unli bilan tugagani va jumlada rasmiy ohang (합니다) borligi bois <code>-와</code> yuklamasi mos keladi.</p>",
        'correct': "교과서와",
        'choices': ["교과서과", "교과서와", "교과서이랑", "교과서를"]
    },
    {
        'text': "<p><strong>A: 어제 마트에서 우유를 샀어요?<br>B: 아니요, 우유는 안 사고 주스________ 생수만 몇 병 샀어요.</strong></p>",
        'explanation': "<p><strong>주스하고</strong>: Ikki ichimlik nomini o'zaro bog'lashda <code>-하고</code> yuklamasidan foydalanish kundalik hayotda eng ommabop usuldir.</p>",
        'correct': "주스하고",
        'choices': ["주스과", "주스하고", "주스이랑", "주스가"]
    },
    {
        'text': "<p><strong>A: 이번 프로젝트는 누구랑 같이 담당하게 되었어요?<br>B: 마케팅 팀의 영수 씨________ 같이 일하게 되었어요.</strong></p>",
        'explanation': "<p><strong>씨하고</strong>: Inson ismlari va unvonlaridan keyin (씨, 부장님) birgalikda ishlash ma'nosini neytral yoki og'zaki ifodalashda <code>-하고</code> juda to'g'ri keladi.</p>",
        'correct': "씨하고",
        'choices': ["씨과", "씨하고", "씨이랑", "씨를"]
    },
    {
        'text': "<p><strong>A: 지민아, 마트에 가면 뭐 사올까?<br>B: 내가 먹을 초콜릿________ 동생이 먹을 사탕 좀 사다 줘.</strong></p>",
        'explanation': "<p><strong>초콜릿이랑</strong>: Og'zaki suhbatda (사다 줘) undosh bilan tugagan '초콜릿' so'zi ortidan <code>-이랑</code> yuklamasi ishlatiladi.</p>",
        'correct': "초콜릿이랑",
        'choices': ["초콜릿랑", "초콜릿이랑", "초콜릿와", "초콜릿하고과"]
    },
    {
        'text': "<p><strong>A: 외국어를 배울 때는 무엇이 중요합니까?<br>B: 꾸준한 문법 공부________ 끊임없는 말하기 연습이 필요합니다.</strong></p>",
        'explanation': "<p><strong>공부와</strong>: Rasmiy ma'ruzaviy nutqda unli bilan tugagan '공부' so'zini keyingi otga bog'lash uchun <code>-와</code> ishlatiladi.</p>",
        'correct': "공부와",
        'choices': ["공부과", "공부와", "공부이", "공부랑"]
    },
    {
        'text': "<p><strong>A: 안드레이 씨, 한국에서 어떤 스포츠를 자주 해요?<br>B: 저는 주로 회사 동료들________ 축구나 테니스를 쳐요.</strong></p>",
        'explanation': "<p><strong>동료들하고</strong>: Hamkasblar bilan birga sport o'ynashni oddiy va samimiy tushuntirish uchun <code>-하고</code> qo'llaniladi.</p>",
        'correct': "동료들하고",
        'choices': ["동료들와", "동료들하고", "동료들랑", "동료들을"]
    },
    {
        'text': "<p><strong>A: 인형이 아주 귀엽네요. 누구한테 선물할 거예요?<br>B: 제 조카________ 제 친구 딸에게 주려고 두 개 샀어요.</strong></p>",
        'explanation': "<p><strong>조카하고</strong>: Ikki qabul qiluvchi shaxsni (조카, 친구 딸) ketma-ket bog'lab ko'rsatish uchun <code>-하고</code> to'g'ri keladi.</p>",
        'correct': "조카하고",
        'choices': ["조카과", "조카하고", "조카랑하고", "조카를"]
    },
    {
        'text': "<p><strong>A: 가방 안에 무엇이 들어 있습니까?<br>B: 여권________ 외국인등록증이 들어 있습니다. 중요한 물건입니다.</strong></p>",
        'explanation': "<p><strong>여권과</strong>: Hujjatlarni sanab ko'rsatishda va rasmiy gap (들어 있습니다) ohangida undoshli '여권' so'ziga <code>-과</code> mos keladi.</p>",
        'correct': "여권과",
        'choices': ["여권와", "여권과", "여권랑", "여권을"]
    },
    {
        'text': "<p><strong>A: 자밀 씨, 이번 주말에 약속이 있어요?<br>B: 고향에서 온 친척________ 같이 서울 구경을 하기로 했어요.</strong></p>",
        'explanation': "<p><strong>친척하고</strong>: Qarindosh (친척) bilan birga sayr qilishni ifodalashda keng qo'llaniladigan neytral <code>-하고</code> yuklamasi variantlar ichida to'g'ridir.</p>",
        'correct': "친척하고",
        'choices': ["친척과와", "친척하고", "친척랑", "친척을"]
    },
    {
        'text': "<p><strong>A: 식당에서 주문할 때 김밥________ 라면을 같이 시켰어요?<br>B: 네, 분식집에서는 그 두 가지를 같이 먹어야 맛있거든요.</strong></p>",
        'explanation': "<p><strong>김밥하고</strong>: Kundalik taomlanish mavzusidagi dialogda 'kimbap va ramen' birikmasini hosil qilish uchun <code>-하고</code> eng tabiiy shakldir.</p>",
        'correct': "김밥하고",
        'choices': ["김밥와", "김밥하고", "김밥랑하고", "김밥이"]
    },
    {
        'text': "<p><strong>A: 어머니 생신 선물로 무얼 준비하면 좋을까요?<br>B: 예쁜 화장품________ 따뜻한 스카프를 선물해 보세요. 좋아하실 거예요.</strong></p>",
        'explanation': "<p><strong>화장품과</strong>: Tavsiya berish jarayonida bir oz vazminlik va rasmiylikni saqlash maqsadida undosh bilan tugagan '화장품' so'ziga <code>-과</code> ulanadi.</p>",
        'correct': "화장품과",
        'choices': ["화장품와", "화장품과", "화장품랑", "화장품하고과"]
    },
    {
        'text': "<p><strong>A: 민우야, 너 어제 누구________ 하루 종일 있었어?<br>B: 하루 종일 집에서 강아지사랑 놀았어.</strong></p>",
        'explanation': "<p><strong>지랑</strong>: Unli bilan tugagan '누구' (kim) so'zi norasmiy suhbatda kelganda, unga <code>-랑</code> yuklamasi ulanishi qoidaga mos keladi (누구랑).</p>",
        'correct': "지랑",
        'choices': ["지과", "지이랑", "지랑", "지하고과"]
    },
    {
        'text': "<p><strong>A: 컴퓨터를 사려고 하는데 모니터________ 본체를 따로 사야 해요?<br>B: 요즘은 일체형 컴퓨터도 많지만, 보통은 따로 사는 게 성능이 좋아요.</strong></p>",
        'explanation': "<p><strong>모니터와</strong>: Texnik jihozlarni tushuntirish va o'zaro solishtirishda unli bilan tugagan '모니터' so'ziga yozma/rasmiy uslubdagi <code>-와</code> mos keladi.</p>",
        'correct': "모니터와",
        'choices': ["모니터과", "모니터와", "모니터랑", "모니터를"]
    },
    {
        'text': "<p><strong>A: 한국 생활 중에서 가장 적응하기 힘든 게 뭐예요?<br>B: 매운 음식________ 빠른 속도의 문화가 조금 힘들었어요. 지금은 괜찮아요.</strong></p>",
        'explanation': "<p><strong>음식과</strong>: '음식' (taom) so'zi undosh bilan tugagani va o'z tajribasini jiddiy tushuntirayotgani uchun rasmiy yozma uslubdagi <code>-과</code> yuklamasi to'g'ri bo'ladi.</p>",
        'correct': "음식과",
        'choices': ["음식와", "음식과", "음식랑", "음식을"]
    }
]



QUESTIONS_class_4 = [
    {
        'text': "<p><strong>A: 아지즈 씨, 지금 어디에 가고 있어요?<br>B: 내일 시험이 있어서 공부하러 도서관________ 가고 있어요.</strong></p>",
        'explanation': "<p><strong>도서관에</strong>: '가다' (bormoq) yo'nalish fe'li kelganda, harakat yo'nalgan joyga <code>-에</code> kelishigi qo'shiladi.</p>",
        'correct': "도서관에",
        'choices': ["도서관에서", "도서관에", "도서관부터", "도서관까지"]
    },
    {
        'text': "<p><strong>A: 주말에 보통 어디에서 친구를 만나요?<br>B: 주말에는 보통 조용한 카페________ 만나서 커피를 마셔요.</strong></p>",
        'explanation': "<p><strong>카페에서</strong>: '만나다' (chrashmoq) kabi dinamik ish-harakat sodir bo'layotgan joyni ifodalash uchun o'rin-payt kelishigi (<code>-에서</code>) ishlatilishi kerak.</p>",
        'correct': "카페에서",
        'choices': ["카페에", "카페에서", "카페부터", "카페까지"]
    },
    {
        'text': "<p><strong>A: 회사 근무 시간이 어떻게 되나요?<br>B: 오전 9시________ 오후 6시까지 일합니다. 주말에는 쉽니다.</strong></p>",
        'explanation': "<p><strong>9시부터</strong>: Vaqtning boshlanish nuqtasini ko'rsatish uchun <code>-부터</code> yuklamasi ishlatiladi. '오후 6시까지' (soat 6-gacha) iborasi bilan juftlik hosil qiladi.</p>",
        'correct': "9시부터",
        'choices': ["9시에", "9시에서", "9시부터", "9시까지"]
    },
    {
        'text': "<p><strong>A: 안바르 씨의 고향은 어디예요?<br>B: 저는 우즈베키스탄________ 왔습니다. 만나서 반갑습니다.</strong></p>",
        'explanation': "<p><strong>우즈베키스탄에서</strong>: Kelib chiqish mamlakati yoki harakatning boshlanish joyini '오다' (kelmoq) fe'li bilan ifodalashda <code>-에서</code> ishlatiladi.</p>",
        'correct': "우즈베키스탄에서",
        'choices': ["우즈베키스탄에", "우즈베키스탄에서", "우즈베키스탄부터", "우즈베키스탄까지"]
    },
    {
        'text': "<p><strong>A: 집이 학교하고 가깝습니까?<br>B: 네, 아주 가깝습니다. 집________ 학교까지 걸어서 5분밖에 안 걸려요.</strong></p>",
        'explanation': "<p><strong>집에서</strong>: Joylar orasidagi masofa haqida gap ketganda, boshlanish joyiga <code>-에서</code>, tugash joyiga esa '까지' qo'shiladi.</p>",
        'correct': "집에서",
        'choices': ["집에", "집에서", "집부터", "집까지"]
    },
    {
        'text': "<p><strong>A: 마크 씨, 혹시 지금 방에 책상이 있어요?<br>B: 네, 방________ 침대하고 책상이 모두 있어요.</strong></p>",
        'explanation': "<p><strong>방에</strong>: Shaxs yoki narsaning ma'lum bir joyda mavjudligini (<code>있다/없다</code>) ko'rsatish uchun joy so'ziga <code>-에</code> qo'shiladi.</p>",
        'correct': "방에",
        'choices': ["방에", "방에서", "방부터", "방까지"]
    },
    {
        'text': "<p><strong>A: 한국 대학교는 보통 몇 월________ 첫 학기가 시작돼요?<br>B: 한국은 보통 3월에 새 학기가 시작됩니다.</strong></p>",
        'explanation': "<p><strong>월에</strong>: Muayyan vaqtni (yil, oy, kun, soat) ko'rsatish uchun vaqt so'zidan keyin har doim <code>-에</code> payt kelishigi qo'yiladi.</p>",
        'correct': "월에",
        'choices': ["월에", "월에서", "월부터", "월까지"]
    },
    {
        'text': "<p><strong>A: 어제 저녁에 왜 전화를 안 받았어요?<br>B: 미안해요. 그때 극장________ 친구하고 영화를 보고 있었어요.</strong></p>",
        'explanation': "<p><strong>극장에서</strong>: '영화를 보다' (kino ko'rmoq) dinamik harakati sodir bo'layotgan aniq joyni ifodalash uchun <code>-에서</code> talab qilinadi.</p>",
        'correct': "극장에서",
        'choices': ["극장에", "극장에서", "극장부터", "극장까지"]
    },
    {
        'text': "<p><strong>A: 겨울 방학이 언제까지예요?<br>B: 이번 주 금요일________ 방학이고 다음 주 월요일에 개학해요.</strong></p>",
        'explanation': "<p><strong>금요일까지</strong>: Vaqt yoki muddatning oxirgi tugash nuqtasini belgilash uchun <code>-까지</code> (gacha) yuklamasi qo'shiladi.</p>",
        'correct': "금요일까지",
        'choices': ["금요일에", "금요일에서", "금요일부터", "금요일까지"]
    },
    {
        'text': "<p><strong>A: 흐엉 씨, 한국에 언제 오셨어요?<br>B: 저는 지난주 토요일________ 한국에 도착했습니다.</strong></p>",
        'explanation': "<p><strong>토요일에</strong>: 'Geenhanju toyoil' (O'tgan hafta shanba) aniq vaqtni anglatgani uchun unga payt kelishigi <code>-에</code> biriktiriladi.</p>",
        'correct': "토요일에",
        'choices': ["토요일에", "토요일에서", "토요일부터", "토요일까지"]
    },
    {
        'text': "<p><strong>A: 매일 저녁 몇 시에 운동을 하세요?<br>B: 퇴근하고 보통 밤 8시________ 9시까지 헬스장에서 운동해요.</strong></p>",
        'explanation': "<p><strong>8시부터</strong>: Orqasidan '9시까지' kelgani sababli, vaqtning boshlanish chegarasini bildiruvchi <code>-부터</code> eng to'g'ri variantdir.</p>",
        'correct': "8시부터",
        'choices': ["8시에", "8시에서", "8시부터", "8시까지"]
    },
    {
        'text': "<p><strong>A: 안드레이 씨, 주말에 공원________ 뭐 했어요?<br>B: 날씨가 좋아서 자전거를 탔어요.</strong></p>",
        'explanation': "<p><strong>공원에서</strong>: 공원 (bog') ichida '자전거를 타다' (velosiped uchmoq) harakati bajarilgani sababli o'rin-payt kelishigi <code>-에서</code> qo'yiladi.</p>",
        'correct': "공원에서",
        'choices': ["공원에", "공원에서", "공원부터", "공원까지"]
    },
    {
        'text': "<p><strong>A: 실례지만 시청에 가려면 어디________ 내려야 합니까?<br>B: 다음 버스 정류장에서 내리시면 됩니다.</strong></p>",
        'explanation': "<p><strong>어디에서</strong>: '내리다' (tushmoq) harakati bajariladigan joy so'ralayotgani uchun <code>어디에서</code> (qayerda) shakli to'g'ri bo'ladi.</p>",
        'correct': "어디에서",
        'choices': ["어디에", "어디에서", "어디부터", "어디까지"]
    },
    {
        'text': "<p><strong>A: 수진 씨, 이번 휴가 때 어디________ 갈 거예요?<br>B: 가족들과 함께 제주도에 가려고 해요.</strong></p>",
        'explanation': "<p><strong>어디에</strong>: '갈 거예요' (bormoqchiman) yo'nalish fe'li bilan ishlatilganda, so'roq so'zi bo'lgan 'eodi' (qayer) ga <code>-에</code> qo'shiladi.</p>",
        'correct': "어디에",
        'choices': ["어디에", "어디에서", "어디부터", "어디까지"]
    },
    {
        'text': "<p><strong>A: 이 백화점은 몇 시에 문을 닫아요?<br>B: 밤 10시________ 영업이 끝납니다. 서두르세요.</strong></p>",
        'explanation': "<p><strong>10시에</strong>: Vaqt aniq ko'rsatilganda va o'sha vaqtda biror holat yuz berganda <code>-에</code> ishlatiladi.</p>",
        'correct': "10시에",
        'choices': ["10시에", "10시에서", "10시부터", "10시까지"]
    },
    {
        'text': "<p><strong>A: 서울역________ 인천공항까지 지하철로 얼마나 걸려요?<br>B: 급행열차를 타면 50분쯤 걸려요.</strong></p>",
        'explanation': "<p><strong>서울역에서</strong>: '인천공항까지' bilan bog'lanib, masofaning boshlanish nuqtasini ko'rsatgani uchun joy nomi ortidan <code>-에서</code> kelishi shart.</p>",
        'correct': "서울역에서",
        'choices': ["서울역에", "서울역에서", "서울역부터", "서울역까지"]
    },
    {
        'text': "<p><strong>A: 자밀 씨, 어제 쇼핑몰________ 옷을 많이 샀어요?<br>B: 아니요, 구경만 하고 아무것도 안 샀어요.</strong></p>",
        'explanation': "<p><strong>쇼핑몰에서</strong>: '옷을 사다' (kiyim sotib olmoq) yoki '구경하다' (tomosha qilmoq) harakatlari bajarilgan joyni anglatish uchun <code>-에서</code> mos keladi.</p>",
        'correct': "쇼핑몰에서",
        'choices': ["쇼핑몰에", "쇼핑몰에서", "쇼핑몰부터", "쇼핑몰까지"]
    },
    {
        'text': "<p><strong>A: 혹시 지갑을 어디에 두었는지 기억나요?<br>B: 아! 아까 거실 탁자 위________ 올려놓은 것 같아요. 가 보세요.</strong></p>",
        'explanation': "<p><strong>탁자 위에</strong>: Narsani ma'lum bir nuqtaga qo'yib qo'yish (올려놓다, 두다, 놓다) yo'nalishli joylashuvni bildirgani uchun <code>-에</code> bilan qo'llanadi.</p>",
        'correct': "탁자 위에",
        'choices': ["탁자 위에", "탁자 위에서", "탁자 위부터", "탁자 위까지"]
    },
    {
        'text': "<p><strong>A: 은행 업무는 보통 몇 시에 끝나요?<br>B: 오후 4시________ 은행 문을 닫으니까 그 전에 가셔야 해요.</strong></p>",
        'explanation': "<p><strong>4시에</strong>: Ish-harakat (bank yopilishi) sodir bo'ladigan aniq vaqt momentini ko'rsatgani uchun <code>-에</code> to'g'ri keladi.</p>",
        'correct': "4시에",
        'choices': ["4시에", "4시에서", "4시부터", "4시까지"]
    },
    {
        'text': "<p><strong>A: 오늘 한국어 수업은 몇 시부터예요?<br>B: 오후 2시________ 시작하니까 늦지 않게 오세요.</strong></p>",
        'explanation': "<p><strong>부터</strong>: Darsning boshlanish vaqt chegarasini ta'kidlayotgani va savolda '몇 시부터예요?' deb so'ralgani uchun javobda ham <code>-부터</code> ishlatiladi.</p>",
        'correct': "부터",
        'choices': ["에", "에서", "부터", "까지"]
    },
    {
        'text': "<p><strong>A: 식당 코너는 몇 층________ 있어요?<br>B: 건물 5층에 있으니까 엘리베이터를 타세요.</strong></p>",
        'explanation': "<p><strong>층에</strong>: '있다' (bor) fe'li bilan birga kelib, qavatning joylashuv o'rnini ko'rsatgani uchun <code>-에</code> qo'shiladi.</p>",
        'correct': "층에",
        'choices': ["층에", "층에서", "층부터", "층까지"]
    },
    {
        'text': "<p><strong>A: 소라 씨는 회사에 다녀요?<br>B: 아니요, 회사에 안 다녀요. 지금은 집________ 재택근무를 하고 있어요.</strong></p>",
        'explanation': "<p><strong>집에서</strong>: '재택근무를 하다' (uyda turib ishlamoq) harakat fe'li bo'lgani sababli harakat bajarilayotgan joyni ko'rsatuvchi <code>-에서</code> tanlanadi.</p>",
        'correct': "집에서",
        'choices': ["집에", "집에서", "집부터", "집까지"]
    },
    {
        'text': "<p><strong>A: 여름 휴가는 언제부터 언제까지예요?<br>B: 8월 1일부터 8월 5일________ 휴가예요.</strong></p>",
        'explanation': "<p><strong>5일까지</strong>: '8월 1일부터' (1-avgustdan) iborasi bilan bog'lanib, ta'til tugaydigan oxirgi muddat chegarasini ko'rsatish uchun <code>-까지</code> kerak.</p>",
        'correct': "5일까지",
        'choices': ["5일에", "5일에서", "5일부터", "5일까지"]
    },
    {
        'text': "<p><strong>A: 한국 여행을 가고 싶은데 어디가 좋아요?<br>B: 서울도 좋지만 제주도________ 꼭 가 보세요. 정말 아름다워요.</strong></p>",
        'explanation': "<p><strong>제주도에</strong>: '가 보다' (borib ko'rmoq) yo'nalishli fe'li bo'lgani sababli boriladigan manzilga <code>-에</code> qo'shiladi.</p>",
        'correct': "제주도에",
        'choices': ["제주도에", "제주도에서", "제주도부터", "제주도까지"]
    },
    {
        'text': "<p><strong>A: 한국어 말하기 대회가 어디________ 열립니까?<br>B: 대학교 본관 대강당에서 열릴 예정입니다.</strong></p>",
        'explanation': "<p><strong>어디에서</strong>: '열리다' (o'tkazilmoq/ochilmoq) tadbiri sodir bo'ladigan joy so'ralayotgani uchun <code>어디에서</code> qo'llanilishi lozim.</p>",
        'correct': "어디에서",
        'choices': ["어디에", "어디에서", "어디부터", "어디까지"]
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
            title='4-dars: Vaqt/Joy Kelishiklari',  # --- IGNORE ---
            master=master,
            defaults={
                'description': 'Koreys tili - 4 dars: Vaqt/Joy kelishiklari haqida testlar',
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

        for i, q in enumerate(QUESTIONS_class_4, start=1):
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
