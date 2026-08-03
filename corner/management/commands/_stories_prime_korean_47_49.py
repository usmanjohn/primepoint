# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-47 … PK-49 (르/ㅅ/ㅎ, (으)니까, 기 때문에).

Kumulyativ qoida: PK-49 gacha oʻrganilgan hamma narsa ochiq.
PK-47 matnida (으)니까 (48) va 때문에 (49) hali YOʻQ.
PK-48 matnida 때문에 hali yoʻq.
아/어야 하다 (50), 아/어도 되다 (51), 것 같다 (52), majhul nisbat (56) —
hech qaysisida yoʻq.

Uchta matn bitta ipga bogʻlangan: qizil soyabon PK-47 da yoʻqoladi,
PK-48 da yana kerak boʻladi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_47_49.py --author=prime
"""

SUBJECT = {
    "name":    "Korean",
    "summary": "Koreys tili: hikoyalar, lugʻat va yozish shablonlari.",
    "icon":    "bi-translate",
    "color":   "#d97706",
}

COLLECTION = {
    "title":       "Prime Korean Readings",
    "description": (
        "Prime Korean darslarining oʻqish matnlari — har biri oʻz darsining "
        "grammatikasini matn ichida koʻrsatadi. Lugʻat izohlari va audio bilan."
    ),
    "order": 2,
}

STORIES = [
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "빨간 우산이 어디에 있어요?",
        "summary": (
            "PK-47 matni. Afsona soyabonini yoʻqotdi — suhbat boshdan oxir "
            "르, ㅅ va ㅎ notoʻgʻri feʼllari ustida yuradi."
        ),
        "order":   47,
        "grammar": [
            {
                "pattern":  "르 guruhi — 모르다, 다르다, 부르다",
                "meaning":  "아/어 oldida 으 tushadi va ㄹ ikkilanadi. 라/러 "
                            "tanlovi oldingi unliga bogʻliq: ㅏ/ㅗ boʻlsa 라, "
                            "boshqasi boʻlsa 러.",
                "examples": ["저는 몰라요.", "이 우산은 제 우산하고 달라요.",
                             "선생님을 불렀어요."],
            },
            {
                "pattern":  "ㅎ guruhi — ranglar",
                "meaning":  "아/어 oldida ㅎ tushadi va unli ㅐ boʻladi "
                            "(빨갛다 → 빨개요). (으)ㄴ oldida esa faqat ㅎ "
                            "tushadi (빨간). Har bir rangni juft yodlang.",
                "examples": ["제 우산은 빨개요.", "빨간 우산을 찾고 있어요.",
                             "그 우산은 파래요."],
            },
            {
                "pattern":  "ㅅ guruhi va uning soxta aʼzolari",
                "meaning":  "짓다 → 지어요, 낫다 → 나아요 — ㅅ tushadi. Lekin "
                            "씻다 → 씻어요, 웃다 → 웃어요 — bular toʻgʻri "
                            "feʼllar, ㅅ tushmaydi.",
                "examples": ["손을 씻었어요.", "감기가 나았어요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Afsona">아프소나</span> 씨가 <span class="cn-word" data-tr="soyabon">우산</span>을 <span class="cn-word" data-pos="verb" data-tr="yoʻqotdi">잃었어요</span>. <span class="cn-word" data-tr="Sujin">수진</span> 씨와 같이 <span class="cn-word" data-pos="verb" data-tr="qidiryapti">찾고 있어요</span>.</p>

<p><strong>수진:</strong> 아프소나 씨 우산은 <span class="cn-word" data-tr="qanaqa">어떤</span> 우산이에요?</p>

<p><strong>아프소나:</strong> 제 우산은 <span class="cn-word" data-pos="adj" data-tr="qizil">빨개요</span>. <span class="cn-word" data-tr="qizil">빨간</span> 우산이에요. <span class="cn-word" data-pos="adj" data-tr="kichkina">작아요</span>.</p>

<p><strong>수진:</strong> 여기 우산이 하나 있어요. 이 우산이에요?</p>

<p><strong>아프소나:</strong> 아니요. 그 우산은 <span class="cn-word" data-pos="adj" data-tr="koʻk">파래요</span>. 제 우산하고 <span class="cn-word" data-pos="adj" data-tr="boshqacha">달라요</span>.</p>

<p><strong>수진:</strong> 그럼 <span class="cn-word" data-tr="qorovul">경비원</span> <span class="cn-word" data-tr="amaki">아저씨</span>를 <span class="cn-word" data-pos="verb" data-tr="chaqiraylik">불러요</span>. 저는 아저씨 <span class="cn-word" data-tr="ismini">이름</span>을 <span class="cn-word" data-pos="verb" data-tr="bilmayman">몰라요</span>. 하지만 <span class="cn-word" data-pos="adv" data-tr="doim">항상</span> 저기에 <span class="cn-word" data-pos="verb" data-tr="oʻtiradi">앉아 있어요</span>.</p>

<p>두 사람이 아저씨를 <span class="cn-word" data-pos="verb" data-tr="chaqirishdi">불렀어요</span>.</p>

<p><strong>아저씨:</strong> 빨간 우산요? 네, 여기 있어요. <span class="cn-word" data-tr="ertalab">아침</span>에 한 <span class="cn-word" data-tr="talaba">학생</span>이 <span class="cn-word" data-pos="verb" data-tr="olib keldi">가져왔어요</span>.</p>

<p><strong>아프소나:</strong> 아, <span class="cn-word" data-pos="adv" data-tr="haqiqatan">정말</span> 고맙습니다! 저는 이 우산을 <span class="cn-word" data-pos="adv" data-tr="juda">아주</span> <span class="cn-word" data-pos="verb" data-tr="yaxshi koʻraman">좋아해요</span>.</p>

<p><strong>수진:</strong> <span class="cn-word" data-tr="shundaymi">그래요</span>? 저도 <span class="cn-word" data-tr="oq">하얀</span> 우산이 있어요. 하지만 아프소나 씨 우산이 더 <span class="cn-word" data-pos="adj" data-tr="chiroyli">예뻐요</span>.</p>

<p>두 사람은 <span class="cn-word" data-pos="verb" data-tr="kulishdi">웃었어요</span>.</p>''',
        "questions": [
            {
                "text": "Afsonaning soyaboni qanaqa?",
                "choices": [
                    "Koʻk va katta",
                    "Qizil va kichkina",
                    "Oq va kichkina",
                    "Qizil va katta",
                ],
                "answer": 1,
                "explanation": "“제 우산은 <b>빨개요</b>… <b>작아요</b>” — "
                               "qizil va kichkina. Koʻk soyabon boshqa "
                               "odamniki: 그 우산은 파래요.",
            },
            {
                "text": "Sujin qorovul haqida nima dedi?",
                "choices": [
                    "Uning ismini bilmaydi",
                    "U bugun kelmagan",
                    "U Afsonaning qoʻshnisi",
                    "U soyabonni olib ketgan",
                ],
                "answer": 0,
                "explanation": "“저는 아저씨 이름을 <b>몰라요</b>” — ismini "
                               "bilmaydi. Koreyschada “bilmaslik” uchun "
                               "alohida feʼl bor: 모르다.",
            },
            {
                "text": "Nega matnda “빨개요” va “빨간” ikki xil shakl?",
                "choices": [
                    "빨개요 — kesim, 빨간 — aniqlovchi (otdan oldin)",
                    "빨개요 rasmiy, 빨간 norasmiy",
                    "빨개요 hozirgi, 빨간 oʻtgan zamon",
                    "Ikkalasi bir xil, farqi yoʻq",
                ],
                "answer": 0,
                "explanation": "ㅎ sifatlari ikki xil oʻzgaradi: 아/어요 oldida "
                               "ㅎ tushadi va unli ㅐ boʻladi (빨<b>개</b>요), "
                               "(으)ㄴ oldida esa faqat ㅎ tushadi "
                               "(빨<b>간</b> 우산).",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "비가 오니까 우산을 가져가세요",
        "summary": (
            "PK-48 matni. Ertasi kuni yomgʻir yogʻyapti — Sujin maslahat "
            "beradi. Har bir maslahat (으)니까 bilan, chunki 아/어서 buyruq "
            "koʻtarmaydi."
        ),
        "order":   48,
        "grammar": [
            {
                "pattern":  "동사/형용사 + (으)니까 + buyruq",
                "meaning":  "Sabab koʻrsatib, keyin buyruq yoki maslahat berish. "
                            "아/어서 dan asosiy farqi shu: undan keyin buyruq "
                            "kelmaydi, (으)니까 dan keyin esa keladi.",
                "examples": ["비가 오니까 우산을 가져가세요.",
                             "시간이 없으니까 빨리 가요.",
                             "날씨가 추우니까 옷을 입으세요."],
            },
            {
                "pattern":  "(으)니까 — kashfiyot",
                "meaning":  "“Bir ish qildim va shunda bilib qoldim”. "
                            "Oʻzbekcha juftligi: “-sam … ekan”. Birinchi qism "
                            "zamonsiz, ikkinchisi oʻtgan zamonda.",
                "examples": ["창문을 여니까 비가 왔어요.",
                             "집에 가니까 아무도 없었어요."],
            },
            {
                "pattern":  "Uzr va rahmatda — faqat 아/어서",
                "meaning":  "늦어서 죄송합니다, 도와줘서 고맙습니다. Bu yerda "
                            "(으)니까 qoʻpol eshitiladi — goʻyo bahona "
                            "qilayotgandek.",
                "examples": ["늦어서 죄송합니다.", "우산을 줘서 고마워요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="ertasi kuni">다음 날</span> <span class="cn-word" data-tr="ertalab">아침</span>이에요. <span class="cn-word" data-tr="Sujin">수진</span> 씨가 <span class="cn-word" data-tr="derazani">창문</span>을 <span class="cn-word" data-pos="verb" data-tr="ochsa">여니까</span> 비가 <span class="cn-word" data-pos="verb" data-tr="yogʻayotgan ekan">왔어요</span>.</p>

<p><strong>수진:</strong> 아프소나 씨! 비가 <span class="cn-word" data-tr="yogʻayotgani uchun">오니까</span> <span class="cn-word" data-tr="soyabon">우산</span>을 <span class="cn-word" data-pos="verb" data-tr="olib keting">가져가세요</span>.</p>

<p><strong>아프소나:</strong> 네! <span class="cn-word" data-tr="kecha">어제</span> <span class="cn-word" data-pos="verb" data-tr="topganim uchun">찾았으니까</span> 지금 <span class="cn-word" data-tr="sumkamda">가방에</span> 있어요.</p>

<p><strong>수진:</strong> <span class="cn-word" data-pos="adj" data-tr="sovuq boʻlgani uchun">추우니까</span> 따뜻한 <span class="cn-word" data-tr="kiyim">옷</span>도 <span class="cn-word" data-pos="verb" data-tr="kiying">입으세요</span>.</p>

<p><strong>아프소나:</strong> 네, 좋아요. <span class="cn-word" data-tr="vaqt">시간</span>이 <span class="cn-word" data-tr="yoʻq boʻlgani uchun">없으니까</span> <span class="cn-word" data-pos="adv" data-tr="tez">빨리</span> 가요.</p>

<p>두 사람이 <span class="cn-word" data-tr="bekatga">정류장에</span> <span class="cn-word" data-pos="verb" data-tr="borishsa">가니까</span> <span class="cn-word" data-tr="avtobus">버스</span>가 <span class="cn-word" data-pos="adv" data-tr="allaqachon">벌써</span> <span class="cn-word" data-pos="verb" data-tr="ketib boʻlgan ekan">떠났어요</span>.</p>

<p><strong>아프소나:</strong> 아! 버스가 없어요.</p>

<p><strong>수진:</strong> <span class="cn-word" data-pos="verb" data-tr="xavotir olmang">걱정하지 마세요</span>. <span class="cn-word" data-tr="metro">지하철</span>이 <span class="cn-word" data-pos="adj" data-tr="tez boʻlgani uchun">빠르니까</span> 지하철을 <span class="cn-word" data-pos="verb" data-tr="mining">타세요</span>.</p>

<p><span class="cn-word" data-tr="maktabda">학교에서</span> 두 사람이 <span class="cn-word" data-pos="verb" data-tr="kechikishdi">늦었어요</span>.</p>

<p><strong>아프소나:</strong> 선생님, <span class="cn-word" data-tr="kechikkanimiz uchun">늦어서</span> <span class="cn-word" data-pos="verb" data-tr="uzr soʻraymiz">죄송합니다</span>.</p>

<p><strong>선생님:</strong> <span class="cn-word" data-tr="shundaymi">그래요</span>? 비가 <span class="cn-word" data-tr="yogʻayotgani uchun">오니까</span> <span class="cn-word" data-pos="adj" data-tr="hech gap emas">괜찮아요</span>. <span class="cn-word" data-pos="verb" data-tr="oʻtiring">앉으세요</span>.</p>''',
        "questions": [
            {
                "text": "Sujin derazani ochganda nima boʻldi?",
                "choices": [
                    "Deraza ochilmadi",
                    "Yomgʻir yogʻayotgan ekan",
                    "Quyosh chiqdi",
                    "Avtobus keldi",
                ],
                "answer": 1,
                "explanation": "“창문을 <b>여니까</b> 비가 왔어요” — bu sabab "
                               "emas, <b>kashfiyot</b>: derazani ochib, "
                               "yomgʻirni koʻrdi. Oʻzbekcha: “ochsam, "
                               "yogʻayotgan ekan”.",
            },
            {
                "text": "Nega ular avtobusga tusha olmadi?",
                "choices": [
                    "Avtobus allaqachon ketib boʻlgan edi",
                    "Puli yoʻq edi",
                    "Bekat uzoq edi",
                    "Avtobus toʻla edi",
                ],
                "answer": 0,
                "explanation": "“정류장에 <b>가니까</b> 버스가 <b>벌써</b> "
                               "떠났어요” — yana kashfiyot: bekatga borishsa, "
                               "avtobus ketib boʻlgan ekan.",
            },
            {
                "text": "Nega Afsona “늦으니까 죄송합니다” demadi?",
                "choices": [
                    "Uzr soʻraganda faqat 아/어서 ishlatiladi",
                    "Chunki 늦다 notoʻgʻri feʼl",
                    "Chunki oʻqituvchi katta",
                    "Ikkalasi ham toʻgʻri boʻlardi",
                ],
                "answer": 0,
                "explanation": "Uzr va rahmatda doim <b>아/어서</b>: "
                               "늦<b>어서</b> 죄송합니다. (으)니까 bu yerda "
                               "bahona qilayotgandek qoʻpol eshitiladi.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "시험 때문에 바빠요",
        "summary": (
            "PK-49 matni. Bekzod TOPIKga tayyorlanyapti va nega bandligini "
            "tushuntiradi — rasmiy sabab qolipi 때문에 bilan."
        ),
        "order":   49,
        "grammar": [
            {
                "pattern":  "명사 + 때문에",
                "meaning":  "“… sababli, … tufayli”. Ot qoʻshimchasiz turadi: "
                            "비 때문에 (비가 때문에 EMAS). Oʻzbekcha bilan soʻz "
                            "tartibi bir xil.",
                "examples": ["시험 때문에 요즘 바빠요.", "비 때문에 늦었어요.",
                             "숙제 때문에 못 갔어요."],
            },
            {
                "pattern":  "동사/형용사 + 기 때문에",
                "meaning":  "Oʻrtaga 기 qoʻyiladi. 기 undosh bilan boshlanadi, "
                            "shuning uchun notoʻgʻri feʼllar oʻzgarmaydi "
                            "(어렵기, 듣기). Zamon oldin qoʻyilishi mumkin.",
                "examples": ["한국어가 어렵기 때문에 매일 공부해요.",
                             "어제 늦게 잤기 때문에 피곤해요."],
            },
            {
                "pattern":  "때문에 dan keyin buyruq YOʻQ",
                "meaning":  "아/어서 dagidek — buyruq, taklif va maslahat "
                            "kelmaydi. Buyruq kerak boʻlsa, (으)니까 (PK-48) "
                            "ishlatiladi. 때문에 ning uslubi rasmiy va yozma.",
                "examples": ["비가 오니까 우산을 가져가세요. (때문에 emas)"],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Bekzod">베크조드</span> 씨와 <span class="cn-word" data-tr="Jasur">자수르</span> 씨가 <span class="cn-word" data-tr="kutubxonada">도서관에서</span> <span class="cn-word" data-pos="verb" data-tr="uchrashishdi">만났어요</span>.</p>

<p><strong>자수르:</strong> 베크조드 씨, <span class="cn-word" data-tr="shu kunlarda">요즘</span> <span class="cn-word" data-pos="adv" data-tr="nega">왜</span> <span class="cn-word" data-pos="adj" data-tr="band">바빠요</span>?</p>

<p><strong>베크조드:</strong> <span class="cn-word" data-tr="imtihon tufayli">시험 때문에</span> 바빠요. <span class="cn-word" data-tr="keyingi oy">다음 달</span>에 <span class="cn-word" data-tr="TOPIK">토픽</span> 시험이 있어요.</p>

<p><strong>자수르:</strong> <span class="cn-word" data-tr="qaysi qismi">어떤 부분</span>이 <span class="cn-word" data-pos="adj" data-tr="qiyin">어려워요</span>?</p>

<p><strong>베크조드:</strong> <span class="cn-word" data-tr="yozish">쓰기</span>가 제일 어려워요. <span class="cn-word" data-tr="grammatika">문법</span>이 <span class="cn-word" data-tr="qiyin boʻlgani uchun">어렵기 때문에</span> 매일 <span class="cn-word" data-pos="verb" data-tr="oʻqiyman">공부해요</span>. 하지만 <span class="cn-word" data-tr="vaqt">시간</span>이 <span class="cn-word" data-pos="adj" data-tr="yetarli emas">부족해요</span>.</p>

<p><strong>자수르:</strong> <span class="cn-word" data-tr="men ham">저도</span> <span class="cn-word" data-tr="talaba boʻlganim uchun">학생이기 때문에</span> 시간이 없어요. <span class="cn-word" data-tr="uy vazifasi">숙제</span> 때문에 <span class="cn-word" data-tr="dam olish kunlari">주말</span>에도 <span class="cn-word" data-pos="verb" data-tr="dam ololmayman">못 쉬어요</span>.</p>

<p><strong>베크조드:</strong> <span class="cn-word" data-tr="kecha">어제</span> <span class="cn-word" data-pos="adv" data-tr="kech">늦게</span> <span class="cn-word" data-tr="yotganim uchun">잤기 때문에</span> <span class="cn-word" data-tr="bugun">오늘</span> <span class="cn-word" data-pos="adj" data-tr="charchaganman">피곤해요</span>. 하지만 <span class="cn-word" data-tr="oʻrganish">공부하는 것</span>이 <span class="cn-word" data-pos="adj" data-tr="qiziqarli">재미있어요</span>.</p>

<p><strong>자수르:</strong> <span class="cn-word" data-tr="shunday ekan">그러니까</span> 오늘은 <span class="cn-word" data-pos="adv" data-tr="erta">일찍</span> <span class="cn-word" data-pos="verb" data-tr="yoting">자세요</span>. <span class="cn-word" data-tr="salomatlik">건강</span>이 제일 <span class="cn-word" data-tr="muhim">중요해요</span>.</p>

<p><strong>베크조드:</strong> 네. <span class="cn-word" data-tr="aytganingiz uchun">말해 줘서</span> <span class="cn-word" data-pos="verb" data-tr="rahmat">고마워요</span>.</p>''',
        "questions": [
            {
                "text": "Nega Bekzod shu kunlarda band?",
                "choices": [
                    "Ishi koʻp",
                    "Keyingi oydagi TOPIK imtihoni tufayli",
                    "Kasal boʻlgani uchun",
                    "Uy vazifasi tufayli",
                ],
                "answer": 1,
                "explanation": "“<b>시험 때문에</b> 바빠요. 다음 달에 토픽 "
                               "시험이 있어요” — imtihon tufayli. 숙제 때문에 "
                               "band boʻlgani — Jasur.",
            },
            {
                "text": "Jasur nega dam ololmaydi?",
                "choices": [
                    "Talaba boʻlgani va uy vazifasi tufayli",
                    "Ishlagani uchun",
                    "TOPIKga tayyorlanayotgani uchun",
                    "Kasal boʻlgani uchun",
                ],
                "answer": 0,
                "explanation": "“<b>학생이기 때문에</b> 시간이 없어요. "
                               "<b>숙제 때문에</b> 주말에도 못 쉬어요” — "
                               "ikkita sabab, ikkita shakl: ot bilan 때문에, "
                               "이다 bilan 이기 때문에.",
            },
            {
                "text": "Nega Jasur maslahat berayotganda “그러니까” dedi, "
                        "“그렇기 때문에” emas?",
                "choices": [
                    "때문에 dan keyin buyruq kelmaydi",
                    "그렇기 때문에 notoʻgʻri shakl",
                    "Chunki ular tengdosh",
                    "Chunki gap oʻtgan zamonda",
                ],
                "answer": 0,
                "explanation": "Keyin buyruq bor (일찍 자세요), shuning uchun "
                               "faqat <b>(으)니까</b> oilasi mumkin. 때문에 "
                               "va 아/어서 buyruq koʻtarmaydi.",
            },
        ],
    },
]
