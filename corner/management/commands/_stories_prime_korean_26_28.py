# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-26 … PK-28 (soʻroq, kelasi zamon, xohish).

Kumulyativ qoida: PK-28 gacha oʻrganilgan hamma narsa ochiq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_26_28.py --author=prime
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
        "title":   "언제 만나요?",
        "summary": (
            "PK-26 matni. Afsona va Bekzod uchrashuvni kelishadi — oltita soʻroq "
            "soʻzi bir suhbatda, hammasi oʻz oʻrnida."
        ),
        "order":   26,
        "grammar": [
            {
                "pattern":  "누구 · 뭐 · 어디 · 언제 · 왜 · 어떻게",
                "meaning":  "Asosiy soʻroq soʻzlari. Ular gapda JAVOB turadigan joyda "
                            "qoladi — hech qayerga koʻchmaydi, xuddi oʻzbekchadagidek.",
                "examples": ["언제 만나요?", "어디에서 만나요?", "왜 안 가요?"],
            },
            {
                "pattern":  "누구 + 가 = 누가",
                "meaning":  "Soʻroq soʻzlari oddiy ot kabi qoʻshimcha oladi: 누구를, "
                            "누구의, 어디에서. Lekin 누구 + 가 majburiy ravishda "
                            "누가 boʻlib qisqaradi.",
                "examples": ["누가 왔어요?", "누구를 만나요?", "누구의 책이에요?"],
            },
            {
                "pattern":  "뭐 va 무엇 · qoʻshimchaning tushishi",
                "meaning":  "뭐 — ogʻzaki, 무엇 — yozma. Kundalik nutqda soʻroq soʻzidan "
                            "keyingi qoʻshimcha koʻpincha tushiriladi: 뭐 해요?, 어디 가요?",
                "examples": ["뭐 해요?", "무엇을 합니까?", "어디 가요?"],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Afsona">아프소나</span> 씨와 <span class="cn-word" data-tr="Bekzod">벡조드</span> 씨가 <span class="cn-word" data-pos="verb" data-tr="gaplashadi">말해요</span>.</p>

<p><strong>벡조드:</strong> 아프소나 씨, <span class="cn-word" data-tr="bugun">오늘</span> <span class="cn-word" data-tr="nima">뭐</span> <span class="cn-word" data-pos="verb" data-tr="qilyapsiz">해요</span>?</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-tr="kutubxona">도서관</span>에서 <span class="cn-word" data-pos="verb" data-tr="oʻqiyman">공부해요</span>. 벡조드 씨는 뭐 해요?</p>

<p><strong>벡조드:</strong> 저는 <span class="cn-word" data-tr="doʻst">친구</span>를 <span class="cn-word" data-pos="verb" data-tr="uchrataman">만나요</span>.</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-tr="kim">누구</span>를 만나요?</p>

<p><strong>벡조드:</strong> <span class="cn-word" data-tr="Jasur">자수르</span> 씨를 만나요.</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-tr="qachon">언제</span> 만나요?</p>

<p><strong>벡조드:</strong> <span class="cn-word" data-tr="tushdan keyin">오후</span> <span class="cn-word" data-tr="soat uchda">세 시</span>에 만나요. <span class="cn-word" data-tr="qayerda">어디에서</span> 공부해요?</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-tr="maktab">학교</span> <span class="cn-word" data-tr="yon">옆</span> 도서관에서 공부해요.</p>

<p><strong>벡조드:</strong> <span class="cn-word" data-tr="nega">왜</span> <span class="cn-word" data-tr="uy">집</span>에서 공부 <span class="cn-word" data-tr="qilmaysiz">안 해요</span>?</p>

<p><strong>아프소나:</strong> 집은 <span class="cn-word" data-tr="yaxshi emas">좋지 않아요</span>. 도서관이 <span class="cn-word" data-pos="adj" data-tr="yaxshi">좋아요</span>.</p>

<p><strong>벡조드:</strong> <span class="cn-word" data-tr="qanday">어떻게</span> 한국어를 공부해요?</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-tr="har kuni">매일</span> <span class="cn-word" data-tr="kitob">책</span>을 <span class="cn-word" data-pos="verb" data-tr="oʻqiyman">읽어요</span>.</p>''',
        "questions": [
            {
                "text": "Matnda “누구를 만나요?” deyilgan. Nega soʻroq soʻzi gap boshiga koʻchmagan?",
                "choices": [
                    "Koreys soʻroq soʻzi javob turadigan joyda qoladi",
                    "Chunki 누구 받침 bilan tugamaydi",
                    "Chunki bu oʻtgan zamon",
                    "Bu xato — boshiga koʻchishi kerak edi",
                ],
                "answer": 0,
                "explanation": "Koreys va oʻzbek tilida soʻroq soʻzi javob turadigan "
                               "joyda qoladi: “Kimni uchratasiz?” → 누구를 만나요? Ingliz "
                               "tilida esa u gap boshiga chiqadi (What / Who…).",
            },
            {
                "text": "Afsona nega uyda oʻqimaydi?",
                "choices": [
                    "Uyda qiyin, kutubxona yaxshiroq",
                    "Uyda vaqti yoʻq",
                    "Uy uzoqda",
                    "Kitoblari yoʻq",
                ],
                "answer": 0,
                "explanation": "“집은 좋지 않아요. 도서관이 좋아요” — uy yaxshi emas, kutubxona "
                               "yaxshi. Inkor uchun 지 않다 ishlatilgan (PK-21).",
            },
            {
                "text": "“어디에서 공부해요?” da nega 에서, 에 emas?",
                "choices": [
                    "공부하다 harakat feʼli — harakat joyi 에서 oladi",
                    "Chunki 어디 받침 bilan tugamaydi",
                    "Chunki bu savol gapi",
                    "Chunki 에 faqat vaqt uchun",
                ],
                "answer": 0,
                "explanation": "PK-14 qoidasi soʻroq soʻzlariga ham tegishli: 있다/없다 "
                               "bilan 에, harakat feʼli bilan 에서. Matnda 도서관에 가요 "
                               "(yoʻnalish → 에) ham bor.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "내일 뭐 할 거예요?",
        "summary": (
            "PK-27 matni. Uch doʻstning ertangi rejalari — va ob-havo haqidagi "
            "taxmin, ya'ni bitta shaklning ikkinchi vazifasi."
        ),
        "order":   27,
        "grammar": [
            {
                "pattern":  "동사 + (으)ㄹ 거예요",
                "meaning":  "Kelasi zamon. 받침 yoʻq → ㄹ 거예요 (갈), bor → 을 거예요 "
                            "(먹을). Oʻzak allaqachon ㄹ bilan tugasa yangi ㄹ qoʻshilmaydi. "
                            "Oʻqilishi har doim [꺼예요].",
                "examples": ["갈 거예요", "먹을 거예요", "할 거예요", "살 거예요"],
            },
            {
                "pattern":  "Reja yoki taxmin — egaga bogʻliq",
                "meaning":  "저는 …ㄹ 거예요 → REJA (“qilaman”). 그 사람은 …ㄹ 거예요 → "
                            "TAXMIN (“qilsa kerak”), chunki boshqa odamning niyatini "
                            "bilib boʻlmaydi.",
                "examples": ["저는 갈 거예요.", "자수르 씨는 집에 있을 거예요.",
                             "내일 비가 올 거예요."],
            },
            {
                "pattern":  "Inkor va rasmiy shakl",
                "meaning":  "Inkor: 안 갈 거예요 yoki 가지 않을 거예요. "
                            "Rasmiy: (으)ㄹ 겁니다.",
                "examples": ["안 갈 거예요.", "가지 않을 거예요.", "갈 겁니다."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="ertaga">내일</span>은 <span class="cn-word" data-tr="shanba">토요일</span>이에요. <span class="cn-word" data-tr="Jiyoung">지영</span> 씨가 <span class="cn-word" data-tr="doʻstlar">친구들</span>과 <span class="cn-word" data-pos="verb" data-tr="gaplashadi">말해요</span>.</p>

<p><strong>지영:</strong> <span class="cn-word" data-tr="Dilnoza">딜노자</span> 씨, 내일 <span class="cn-word" data-tr="nima">뭐</span> <span class="cn-word" data-tr="qilasiz">할 거예요</span>?</p>

<p><strong>딜노자:</strong> 저는 <span class="cn-word" data-tr="uy">집</span>에서 <span class="cn-word" data-tr="kitob">책</span>을 <span class="cn-word" data-tr="oʻqiyman">읽을 거예요</span>. <span class="cn-word" data-tr="koreys tili">한국어</span>도 <span class="cn-word" data-tr="oʻrganaman">공부할 거예요</span>.</p>

<p><strong>지영:</strong> <span class="cn-word" data-tr="Sherbek">셰르벡</span> 씨는 뭐 할 거예요?</p>

<p><strong>셰르벡:</strong> 저는 <span class="cn-word" data-tr="doʻst">친구</span>를 <span class="cn-word" data-tr="uchrataman">만날 거예요</span>. <span class="cn-word" data-tr="tushdan keyin">오후</span> <span class="cn-word" data-tr="soat ikkida">두 시</span>에 <span class="cn-word" data-tr="uchrashaman">만날 거예요</span>.</p>

<p><strong>지영:</strong> <span class="cn-word" data-tr="qayerda">어디에서</span> 만날 거예요?</p>

<p><strong>셰르벡:</strong> <span class="cn-word" data-tr="Seul">서울</span>에서 만날 거예요. 저는 서울에 <span class="cn-word" data-tr="yashayman">살 거예요</span>.</p>

<p><strong>지영:</strong> <span class="cn-word" data-tr="Jasur">자수르</span> 씨는 <span class="cn-word" data-pos="verb" data-tr="kelmaydi">안 와요</span>. <span class="cn-word" data-tr="ish">일</span>이 <span class="cn-word" data-pos="adj" data-tr="koʻp">많아요</span>. 자수르 씨는 집에 <span class="cn-word" data-tr="boʻlsa kerak">있을 거예요</span>.</p>

<p><strong>딜노자:</strong> 내일 <span class="cn-word" data-tr="yomgʻir">비</span>가 <span class="cn-word" data-tr="yogʻsa kerak">올 거예요</span>. 그래서 저는 <span class="cn-word" data-tr="chiqmayman">안 나갈 거예요</span>.</p>

<p>딜노자 씨는 집에서 책을 읽을 거예요. 셰르벡 씨는 친구를 만날 거예요. 자수르 씨는 집에 있을 거예요 — <span class="cn-word" data-tr="lekin">하지만</span> 지영 씨는 <span class="cn-word" data-tr="bilmaydi">몰라요</span>. 그것은 <span class="cn-word" data-tr="taxmin">추측</span>이에요.</p>''',
        "questions": [
            {
                "text": "Matnda “자수르 씨는 집에 있을 거예요” — bu reja emas, taxmin. Nega?",
                "choices": [
                    "Gap boshqa odam haqida — uning niyatini bilib boʻlmaydi",
                    "Chunki 있다 받침 bilan tugaydi",
                    "Chunki bu oʻtgan zamon",
                    "Chunki Jasur kelmaydi",
                ],
                "answer": 0,
                "explanation": "(으)ㄹ 거예요 ning maʼnosini EGA hal qiladi: 저는 …ㄹ 거예요 "
                               "= reja, 그 사람은 …ㄹ 거예요 = taxmin. Matnning oxirgi "
                               "jumlasi buni ochiq aytadi: 그것은 추측이에요.",
            },
            {
                "text": "Nega “살 거예요” da 을 qoʻshilmagan?",
                "choices": [
                    "Oʻzak allaqachon ㄹ bilan tugaydi",
                    "Chunki 살다 sifat",
                    "Chunki bu taxmin",
                    "Bu xato — 살을 거예요 boʻlishi kerak",
                ],
                "answer": 0,
                "explanation": "살다 ning oʻzagi 살 — u allaqachon ㄹ bilan tugaydi, "
                               "shuning uchun yangi ㄹ qoʻshilmaydi: 살 거예요. "
                               "Solishtiring: 먹 → 먹을 거예요.",
            },
            {
                "text": "Dilnoza nega ertaga chiqmaydi?",
                "choices": [
                    "Yomgʻir yogʻsa kerak",
                    "Ishi koʻp",
                    "Doʻstini uchratadi",
                    "Kasal",
                ],
                "answer": 0,
                "explanation": "“내일 비가 올 거예요. 그래서 저는 안 나갈 거예요” — yomgʻir "
                               "haqidagi gap ham taxmin (ob-havoning niyati yoʻq), "
                               "chiqmaslik esa uning oʻz rejasi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "저는 한국에 가고 싶어요",
        "summary": (
            "PK-28 matni. Har kimning orzusi boshqacha — va matn 고 싶어요 bilan "
            "고 싶어해요 farqini oʻz ichida koʻrsatadi."
        ),
        "order":   28,
        "grammar": [
            {
                "pattern":  "동사 + 고 싶어요",
                "meaning":  "Xohish — “…gim keladi”. 받침 ayrisi yoʻq: 고 oʻzakka "
                            "toʻgʻridan-toʻgʻri yopishadi. Tuslanish har doim 싶다 da "
                            "boʻladi, feʼlda emas.",
                "examples": ["가고 싶어요", "먹고 싶어요", "공부하고 싶어요"],
            },
            {
                "pattern":  "고 싶어하다 — uchinchi shaxs",
                "meaning":  "고 싶다 FAQAT “men” (darak) va “siz” (savol) uchun. Boshqa "
                            "odam haqida 고 싶어하다 ishlatiladi, chunki uning ichki "
                            "istagini bilib boʻlmaydi — faqat tashqi belgilarini.",
                "examples": ["저는 가고 싶어요.", "자수르 씨는 가고 싶어해요."],
            },
            {
                "pattern":  "Xohish va reja farqi",
                "meaning":  "가고 싶어요 — xohish, hali reja emas. 갈 거예요 — qaror "
                            "qilingan reja. Oʻzbekchada ham “borgim keladi” va "
                            "“boraman” farqlanadi.",
                "examples": ["가고 싶어요 (xohish)", "갈 거예요 (reja)"],
            },
        ],
        "body": '''<p>저는 <span class="cn-word" data-tr="Afsona">아프소나</span>예요. 저는 <span class="cn-word" data-tr="Koreya">한국</span>에 <span class="cn-word" data-tr="borgim keladi">가고 싶어요</span>.</p>

<p><span class="cn-word" data-tr="Seul">서울</span>에서 <span class="cn-word" data-tr="koreys tili">한국어</span>를 <span class="cn-word" data-tr="oʻrganmoqchiman">배우고 싶어요</span>. <span class="cn-word" data-tr="koreys ovqati">한국 음식</span>도 <span class="cn-word" data-tr="yegim keladi">먹고 싶어요</span>. <span class="cn-word" data-tr="kimchi-jjigae">김치찌개</span>를 <span class="cn-word" data-pos="verb" data-tr="yegim keladi">먹고 싶어요</span>.</p>

<p><strong>지영:</strong> 아프소나 씨, <span class="cn-word" data-tr="qachon">언제</span> 한국에 <span class="cn-word" data-tr="borasiz">갈 거예요</span>?</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-tr="bilmayman">몰라요</span>. <span class="cn-word" data-tr="pul">돈</span>이 <span class="cn-word" data-tr="yoʻq">없어요</span>. 그래서 <span class="cn-word" data-tr="hozir">지금</span>은 <span class="cn-word" data-tr="borolmayman">못 가요</span>. <span class="cn-word" data-tr="lekin">하지만</span> 가고 싶어요.</p>

<p><strong>지영:</strong> <span class="cn-word" data-tr="Jasur">자수르</span> 씨도 한국에 <span class="cn-word" data-tr="bormoqchi (uchinchi shaxs)">가고 싶어해요</span>?</p>

<p><strong>아프소나:</strong> 아니요. 자수르 씨는 <span class="cn-word" data-tr="Yaponiya">일본</span>에 <span class="cn-word" data-tr="bormoqchi">가고 싶어해요</span>. <span class="cn-word" data-tr="Dilnoza">딜노자</span> 씨는 <span class="cn-word" data-tr="sayohat">여행</span>을 <span class="cn-word" data-tr="qilmoqchi">하고 싶어해요</span>.</p>

<p><strong>지영:</strong> <span class="cn-word" data-tr="nima">뭐</span> <span class="cn-word" data-tr="oʻrganmoqchisiz">배우고 싶어요</span>?</p>

<p><strong>아프소나:</strong> 한국어를 배우고 싶어요. <span class="cn-word" data-tr="kecha">어제</span>도 <span class="cn-word" data-tr="oʻrganmoqchi edim">배우고 싶었어요</span>. 하지만 <span class="cn-word" data-tr="vaqt">시간</span>이 없었어요.</p>

<p>아프소나 씨는 한국에 가고 싶어요. 자수르 씨는 일본에 가고 싶어해요. 딜노자 씨는 여행을 하고 싶어해요. <span class="cn-word" data-tr="hamma">모두</span> <span class="cn-word" data-tr="orzu">꿈</span>이 있어요.</p>''',
        "questions": [
            {
                "text": "Nega matnda Afsona “가고 싶어요” deydi, Jasur haqida esa “가고 싶어해요”?",
                "choices": [
                    "고 싶다 faqat “men” va “siz” uchun; boshqa odam uchun 고 싶어하다",
                    "Chunki Jasur uzoqda",
                    "Chunki 자수르 받침 bilan tugaydi",
                    "Chunki bu oʻtgan zamon",
                ],
                "answer": 0,
                "explanation": "Boshqa odamning ICHKI istagini bilib boʻlmaydi — faqat "
                               "tashqi belgilarini koʻrasiz. Koreys tili buni "
                               "grammatikada ajratadi: 싶다 (mening istagim) va "
                               "싶어하다 (uning koʻrinib turgan istagi).",
            },
            {
                "text": "Afsona nega hozir Koreyaga borolmaydi?",
                "choices": [
                    "Puli yoʻq",
                    "Vaqti yoʻq",
                    "Koreys tilini bilmaydi",
                    "Bormoqchi emas",
                ],
                "answer": 0,
                "explanation": "“돈이 없어요. 그래서 지금은 못 가요” — puli yoʻq, shuning "
                               "uchun BOROLMAYDI (못, imkoniyat yoʻqligi — PK-22). Lekin "
                               "xohishi bor: “하지만 가고 싶어요”.",
            },
            {
                "text": "“배우고 싶었어요” qanday yasalgan?",
                "choices": [
                    "Tuslanish 싶다 da — 싶어요 → 싶었어요",
                    "Feʼlda: 배웠고 싶어요",
                    "고 ga oʻtgan zamon qoʻshilgan",
                    "Bu 고 싶어하다 ning shakli",
                ],
                "answer": 0,
                "explanation": "Tuslanish har doim OXIRGI soʻzda: 배우고 싶다 → "
                               "배우고 싶었어요. <배웠고 싶어요> notoʻgʻri. Bu 지 않다 "
                               "(PK-21) bilan bir xil mantiq.",
            },
        ],
    },
]
