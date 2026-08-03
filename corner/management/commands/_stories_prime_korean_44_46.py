# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-44 … PK-46 ((으)ㄴ/(으)ㄹ, 형용사 + (으)ㄴ, 는 것/기).

Kumulyativ qoida: PK-46 gacha oʻrganilgan hamma narsa ochiq.
PK-44 matnida sifat aniqlovchisi (PK-45) va 는 것 (PK-46) hali YOʻQ.
PK-45 matnida 는 것 hali yoʻq.
르/ㅅ/ㅎ notoʻgʻri feʼllar (PK-47), (으)니까 (48), 기 때문에 (49),
아/어야 하다 (50), 것 같다 (52) — hech qaysisida yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_44_46.py --author=prime
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
        "title":   "어제 본 영화",
        "summary": (
            "PK-44 matni. Afsona bilan Minsu kecha koʻrgan kino va ertaga "
            "koʻradigan kino haqida gaplashadi — (으)ㄴ va (으)ㄹ yonma-yon."
        ),
        "order":   44,
        "grammar": [
            {
                "pattern":  "동사 + (으)ㄴ + 명사",
                "meaning":  "Oʻtgan zamon aniqlovchisi: “…gan ot”. 받침 yoʻq → "
                            "ㄴ, 받침 bor → 은. Aniqlovchi ichiga 았/었 "
                            "qoʻyilmaydi: 봤은 emas, 본.",
                "examples": ["어제 본 영화가 재미있었어요.",
                             "제가 읽은 책이에요.",
                             "작년에 간 식당이 좋았어요."],
            },
            {
                "pattern":  "동사 + (으)ㄹ + 명사",
                "meaning":  "Hali sodir boʻlmagan ish: “…adigan ot”. 받침 yoʻq → "
                            "ㄹ, 받침 bor → 을. 할 일, 먹을 것, 볼 영화.",
                "examples": ["내일 볼 영화를 정했어요.",
                             "오늘 할 일이 많아요.",
                             "주말에 만날 사람이 있어요."],
            },
            {
                "pattern":  "Notoʻgʻri feʼllar va ㄹ oʻzaklar",
                "meaning":  "(으) unli bilan boshlanadi, shuning uchun PK-32 "
                            "oʻzgarishlari ishlaydi: 듣다 → 들은 · 들을. "
                            "ㄹ oʻzak ㄴ oldida ㄹ ni yoʻqotadi: 살다 → 산.",
                "examples": ["어제 들은 노래가 좋았어요.", "서울에 산 친구예요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Afsona">아프소나</span> 씨와 <span class="cn-word" data-tr="Minsu">민수</span> 씨가 <span class="cn-word" data-tr="kafeda">카페에서</span> 이야기하고 있어요.</p>

<p><strong>민수:</strong> 아프소나 씨, <span class="cn-word" data-tr="kecha">어제</span> 뭐 했어요?</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-tr="kino">영화</span>를 봤어요. 어제 <span class="cn-word" data-tr="koʻrgan">본</span> 영화가 <span class="cn-word" data-pos="adj" data-tr="qiziq edi">재미있었어요</span>.</p>

<p><strong>민수:</strong> 영화 <span class="cn-word" data-tr="nomi">이름</span>이 뭐예요?</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-tr="koreys kinosi">한국 영화</span>예요. 제가 <span class="cn-word" data-tr="oʻqigan">읽은</span> <span class="cn-word" data-tr="kitob">책</span>도 <span class="cn-word" data-pos="adv" data-tr="birga">같이</span> 있어요. <span class="cn-word" data-tr="kitobni">책</span>을 <span class="cn-word" data-pos="adv" data-tr="avval">먼저</span> 읽고 영화를 봤어요.</p>

<p><strong>민수:</strong> 저도 <span class="cn-word" data-tr="koʻrgim keladi">보고 싶어요</span>. <span class="cn-word" data-tr="ertaga">내일</span> <span class="cn-word" data-tr="koʻradigan">볼</span> 영화를 <span class="cn-word" data-pos="verb" data-tr="belgilab qoʻydim">정했어요</span>. 그 영화를 볼 거예요.</p>

<p><strong>아프소나:</strong> 좋아요! 하지만 저는 내일 <span class="cn-word" data-tr="qiladigan ish">할 일</span>이 <span class="cn-word" data-pos="adj" data-tr="koʻp">많아요</span>. <span class="cn-word" data-tr="uy vazifasi">숙제</span>도 있어요.</p>

<p><strong>민수:</strong> 그럼 <span class="cn-word" data-tr="dam olish kuni">주말</span>에 같이 봐요. 주말에 <span class="cn-word" data-tr="uchrashiladigan">만날</span> 사람도 없어요.</p>

<p><strong>아프소나:</strong> 네. 어제 <span class="cn-word" data-tr="tinglagan">들은</span> <span class="cn-word" data-tr="qoʻshiq">노래</span>도 그 영화 노래예요. <span class="cn-word" data-pos="adv" data-tr="haqiqatan">정말</span> 좋아요.</p>''',
        "questions": [
            {
                "text": "Afsona kecha nima qildi?",
                "choices": [
                    "Kino koʻrdi",
                    "Uy vazifasini qildi",
                    "Doʻsti bilan uchrashdi",
                    "Qoʻshiq tingladi",
                ],
                "answer": 0,
                "explanation": "“영화를 봤어요. 어제 <b>본</b> 영화가 "
                               "재미있었어요” — kino koʻrdi va u qiziq boʻldi.",
            },
            {
                "text": "Nega ular ertaga emas, dam olish kunida uchrashadi?",
                "choices": [
                    "Kino ertaga yoʻq",
                    "Afsonaning ertaga qiladigan ishi koʻp",
                    "Minsu band",
                    "Kafe yopiq",
                ],
                "answer": 1,
                "explanation": "“저는 내일 <b>할 일</b>이 많아요. 숙제도 "
                               "있어요” — ertaga bajariladigan ishi koʻp. "
                               "할 일 — hali qilinmagan ish, shuning uchun "
                               "(으)ㄹ.",
            },
            {
                "text": "Nega matnda “본 영화” deyilgan, “봤은 영화” emas?",
                "choices": [
                    "Aniqlovchi ichiga 았/었 qoʻyilmaydi",
                    "Chunki 보다 notoʻgʻri feʼl",
                    "Chunki 영화 unli bilan tugaydi",
                    "Ikkalasi ham toʻgʻri",
                ],
                "answer": 0,
                "explanation": "<b>(으)ㄴ</b> ning oʻzi allaqachon “oʻtgan” "
                               "degan — zamonni ikki marta bildirish shart "
                               "emas. 보 da 받침 yoʻq → <b>본</b>.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "우리 동네에서 제일 좋은 곳",
        "summary": (
            "PK-45 matni. Jasur oʻz mahallasidagi eng yaxshi joyni taʼriflaydi — "
            "har bir jumlada sifat aniqlovchisi ishlaydi."
        ),
        "order":   45,
        "grammar": [
            {
                "pattern":  "형용사 + (으)ㄴ + 명사",
                "meaning":  "Sifat otdan oldin turishi uchun (으)ㄴ oladi. "
                            "받침 yoʻq → ㄴ (예쁜), 받침 bor → 은 (좋은, 작은). "
                            "Sifat hech qachon 는 olmaydi.",
                "examples": ["제일 좋은 곳이에요.", "작은 가게가 있어요.",
                             "넓은 공원도 있어요."],
            },
            {
                "pattern":  "하다 sifatlari va ㅂ sifatlari",
                "meaning":  "하다 sifatlari → 한 (조용한, 깨끗한, 따뜻한). "
                            "ㅂ sifatlari ㅂ ni 우 ga aylantiradi (춥다 → 추운, "
                            "맵다 → 매운, 어렵다 → 어려운).",
                "examples": ["조용한 공원이에요.", "추운 날씨에도 사람이 많아요.",
                             "매운 음식을 팔아요."],
            },
            {
                "pattern":  "재미있는 / 맛있는 — istisno",
                "meaning":  "재미있다, 맛있다 ichida 있다 (feʼl) boʻlgani uchun "
                            "ular (으)ㄴ emas, 는 oladi.",
                "examples": ["맛있는 빵을 팔아요.", "재미있는 곳이에요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Jasur">자수르</span> 씨와 <span class="cn-word" data-tr="Sujin">수진</span> 씨가 <span class="cn-word" data-tr="mahalla">동네</span> 이야기를 하고 있어요.</p>

<p><strong>수진:</strong> 자수르 씨 동네에는 <span class="cn-word" data-tr="qanaqa">어떤</span> <span class="cn-word" data-tr="joylar">곳</span>이 있어요?</p>

<p><strong>자수르:</strong> 우리 동네에서 <span class="cn-word" data-pos="adv" data-tr="eng">제일</span> <span class="cn-word" data-tr="yaxshi">좋은</span> 곳은 <span class="cn-word" data-tr="park">공원</span>이에요. <span class="cn-word" data-tr="keng">넓은</span> 공원이에요. 그리고 <span class="cn-word" data-tr="tinch">조용한</span> 곳이에요.</p>

<p><strong>수진:</strong> <span class="cn-word" data-tr="sovuq">추운</span> <span class="cn-word" data-tr="ob-havo">날씨</span>에도 사람이 많아요?</p>

<p><strong>자수르:</strong> 네, 많아요. 공원 <span class="cn-word" data-tr="oldida">앞에</span> <span class="cn-word" data-tr="kichkina">작은</span> <span class="cn-word" data-tr="doʻkon">가게</span>가 있어요. 거기에서 <span class="cn-word" data-tr="issiq">따뜻한</span> 차를 <span class="cn-word" data-pos="verb" data-tr="sotadi">팔아요</span>. <span class="cn-word" data-tr="mazali">맛있는</span> <span class="cn-word" data-tr="non">빵</span>도 있어요.</p>

<p><strong>수진:</strong> <span class="cn-word" data-pos="adj" data-tr="qimmatmi">비싸요</span>?</p>

<p><strong>자수르:</strong> 아니요. <span class="cn-word" data-tr="arzon">싼</span> 가게예요. 그래서 학생이 많아요. 저도 <span class="cn-word" data-tr="uzoq">먼</span> 곳에서 <span class="cn-word" data-pos="adv" data-tr="tez-tez">자주</span> 가요.</p>

<p><strong>수진:</strong> <span class="cn-word" data-tr="achchiq">매운</span> 음식도 있어요? 저는 매운 음식을 <span class="cn-word" data-pos="verb" data-tr="yaxshi koʻraman">좋아해요</span>.</p>

<p><strong>자수르:</strong> 네! <span class="cn-word" data-tr="mashhur">유명한</span> 식당도 있어요. 거기 음식 이름은 <span class="cn-word" data-pos="adj" data-tr="qiyin">어려워요</span>. 하지만 음식은 <span class="cn-word" data-pos="adv" data-tr="juda">아주</span> 맛있어요.</p>

<p><strong>수진:</strong> <span class="cn-word" data-tr="qiziqarli">재미있는</span> 동네예요! <span class="cn-word" data-tr="keyingi safar">다음에</span> 같이 가요.</p>''',
        "questions": [
            {
                "text": "Jasurning mahallasidagi eng yaxshi joy qaysi?",
                "choices": [
                    "Kichkina doʻkon",
                    "Mashhur oshxona",
                    "Keng va tinch park",
                    "Maktab",
                ],
                "answer": 2,
                "explanation": "“제일 <b>좋은</b> 곳은 공원이에요. <b>넓은</b> "
                               "공원이에요. 그리고 <b>조용한</b> 곳이에요” — "
                               "keng va tinch park.",
            },
            {
                "text": "Nega doʻkonga talabalar koʻp keladi?",
                "choices": [
                    "Chunki u arzon",
                    "Chunki u park ichida",
                    "Chunki u mashhur",
                    "Chunki u kechgacha ochiq",
                ],
                "answer": 0,
                "explanation": "“<b>싼</b> 가게예요. 그래서 학생이 많아요” — "
                               "arzon, shuning uchun talabalar koʻp. "
                               "(싸다 → 싼, 받침 yoʻq.)",
            },
            {
                "text": "Nega matnda “맛있는 빵” deyilgan, “맛있은 빵” emas?",
                "choices": [
                    "맛있다 ichida 있다 — feʼl bor, shuning uchun 는 oladi",
                    "Chunki 빵 chet soʻzi",
                    "Chunki gap hozirgi zamonda",
                    "Chunki 맛있다 ㅂ notoʻgʻri sifati",
                ],
                "answer": 0,
                "explanation": "맛있다 = 맛 + <b>있다</b>. 있다 feʼl, feʼllar "
                               "esa hozirgi zamonda 는 oladi. Xuddi shunday: "
                               "재미있는 동네.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "한국어 배우는 것이 재미있어요",
        "summary": (
            "PK-46 matni. Dilnoza bilan Hana TOPIK boʻlimlari — 읽기, 듣기, "
            "쓰기, 말하기 — haqida gaplashadi va nima oson, nima qiyin ekanini "
            "solishtiradi."
        ),
        "order":   46,
        "grammar": [
            {
                "pattern":  "동사 + 는 것",
                "meaning":  "Butun gapni otga aylantiradi: “…ish / …adigan "
                            "narsa”. Ogʻzaki nutqda 것이 → 게, 것을 → 걸, "
                            "것은 → 건.",
                "examples": ["한국어를 배우는 것이 재미있어요.",
                             "제가 좋아하는 것은 듣기예요.",
                             "노래를 듣는 걸 좋아해요."],
            },
            {
                "pattern":  "동사 + 기",
                "meaning":  "Ish-harakatning nomi — oʻzbekcha “-ish” "
                            "qoʻshimchasi: 읽기, 듣기, 쓰기, 말하기. "
                            "기 쉽다 / 기 어렵다 / 기 좋다 / 기 시작하다.",
                "examples": ["이 책은 읽기 쉬워요.", "쓰기가 제일 어려워요.",
                             "한국어를 공부하기 시작했어요."],
            },
            {
                "pattern":  "먹을 것 · 할 일",
                "meaning":  "것 oldiga aniqlovchi keladi, 기 emas. (으)ㄹ 것 — "
                            "hali ishlatilmagan predmet: 먹을 것 (yegulik), "
                            "볼 것 (koʻriladigan narsa).",
                "examples": ["읽을 것이 많아요.", "할 일이 많아요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Dilnoza">딜노자</span> 씨와 <span class="cn-word" data-tr="Hana">하나</span> 씨가 <span class="cn-word" data-tr="kutubxonada">도서관에서</span> <span class="cn-word" data-tr="TOPIK">토픽</span> <span class="cn-word" data-pos="verb" data-tr="tayyorgarlik koʻryapti">준비하고 있어요</span>.</p>

<p><strong>하나:</strong> 딜노자 씨, 한국어 <span class="cn-word" data-tr="oʻrganish">배우는 것</span>이 <span class="cn-word" data-pos="adj" data-tr="qiziqarli">재미있어요</span>?</p>

<p><strong>딜노자:</strong> 네, <span class="cn-word" data-pos="adv" data-tr="juda">아주</span> 재미있어요. 하지만 <span class="cn-word" data-pos="adj" data-tr="qiyin">어려워요</span>. 토픽에는 <span class="cn-word" data-tr="oʻqish">읽기</span>, <span class="cn-word" data-tr="tinglash">듣기</span>, <span class="cn-word" data-tr="yozish">쓰기</span>가 있어요.</p>

<p><strong>하나:</strong> <span class="cn-word" data-tr="qaysi biri">뭐가</span> 제일 어려워요?</p>

<p><strong>딜노자:</strong> 저는 <span class="cn-word" data-tr="yozish">쓰기</span>가 제일 <span class="cn-word" data-pos="adj" data-tr="qiyin">어려워요</span>. 듣기는 <span class="cn-word" data-tr="tinglash oson">듣기 쉬워요</span>. 하지만 쓰기는 <span class="cn-word" data-tr="yozish qiyin">쓰기 어려워요</span>.</p>

<p><strong>하나:</strong> 저는 <span class="cn-word" data-tr="teskarisi">반대</span>예요. 제가 <span class="cn-word" data-tr="yaxshi koʻradigan narsa">좋아하는 것</span>은 쓰기예요. <span class="cn-word" data-pos="adv" data-tr="lekin">그런데</span> 듣기가 어려워요. 한국 사람은 <span class="cn-word" data-pos="adv" data-tr="tez">빨리</span> <span class="cn-word" data-pos="verb" data-tr="gapiradi">말해요</span>.</p>

<p><strong>딜노자:</strong> 그럼 한국 노래를 <span class="cn-word" data-tr="tinglashni">듣는 걸</span> <span class="cn-word" data-pos="verb" data-tr="sinab koʻring">해 보세요</span>. 저도 노래를 <span class="cn-word" data-pos="verb" data-tr="tinglay boshladim">듣기 시작했어요</span>. 그 <span class="cn-word" data-pos="adv" data-tr="keyin">후에</span> 듣기가 <span class="cn-word" data-pos="adj" data-tr="oson">쉬워요</span>.</p>

<p><strong>하나:</strong> <span class="cn-word" data-pos="adj" data-tr="yaxshi fikr">좋은 생각</span>이에요! 이 <span class="cn-word" data-tr="kutubxona">도서관</span>은 <span class="cn-word" data-tr="dars qilish uchun yaxshi">공부하기 좋아요</span>. <span class="cn-word" data-tr="oʻqiladigan narsa">읽을 것</span>도 많아요.</p>

<p><strong>딜노자:</strong> 네. <span class="cn-word" data-tr="qiladigan ish">할 일</span>이 많아요. 하지만 <span class="cn-word" data-tr="oʻrganish">배우는 게</span> 재미있어요.</p>''',
        "questions": [
            {
                "text": "Dilnoza uchun TOPIKning qaysi qismi eng qiyin?",
                "choices": [
                    "Oʻqish (읽기)",
                    "Tinglash (듣기)",
                    "Yozish (쓰기)",
                    "Hammasi bir xil",
                ],
                "answer": 2,
                "explanation": "“저는 <b>쓰기</b>가 제일 어려워요… 쓰기는 쓰기 "
                               "어려워요” — yozish. Tinglash esa unga oson.",
            },
            {
                "text": "Dilnoza Hanaga nimani maslahat berdi?",
                "choices": [
                    "Koʻproq yozishni",
                    "Koreys qoʻshiqlarini tinglashni",
                    "Kutubxonaga kelmaslikni",
                    "Sekinroq gapirishni",
                ],
                "answer": 1,
                "explanation": "“한국 노래를 <b>듣는 걸</b> 해 보세요. 저도 "
                               "노래를 <b>듣기 시작했어요</b>” — oʻzi ham "
                               "shunday qilgan va tinglash osonlashgan.",
            },
            {
                "text": "Nega matnda “읽을 것” deyilgan, “읽기 것” emas?",
                "choices": [
                    "것 oldiga aniqlovchi keladi, 기 emas",
                    "Chunki 읽다 da 받침 bor",
                    "Chunki gap oʻtgan zamonda",
                    "Ikkalasi ham toʻgʻri",
                ],
                "answer": 0,
                "explanation": "것 — ot, va otdan oldin <b>aniqlovchi</b> "
                               "turadi: 읽<b>을</b> 것 (“oʻqiladigan narsa”). "
                               "기 esa 쉽다/어렵다/좋다/시작하다 bilan keladi.",
            },
        ],
    },
]
