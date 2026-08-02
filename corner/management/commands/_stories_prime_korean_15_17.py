# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-15 … PK-17.

Kumulyativ qoida: faqat PK-17 gacha oʻrganilgan grammatika. PK-17 dan boshlab
darsda berilgan feʼllar (읽습니다, 봅니다, 먹습니다, 마십니다, 공부합니다,
좋아합니다) matnda erkin ishlatiladi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_15_17.py --author=prime
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
        "title":   "이것은 무엇입니까?",
        "summary": (
            "PK-15 matni. Afsona va Jasur sinfxonadagi narsalarni nomlaydi — "
            "이것 · 그것 · 저것 uchligi bir suhbatda uchalasi ham ishlatiladi."
        ),
        "order":   15,
        "grammar": [
            {
                "pattern":  "이것 / 그것 / 저것",
                "meaning":  "Uch pogʻonali koʻrsatish: 이 = gapiruvchida (bu), "
                            "그 = tinglovchida yoki aytib oʻtilgan (shu), 저 = ikkalasidan "
                            "uzoq (anavi). Oʻzbekcha bu · shu · u bilan aynan mos.",
                "examples": ["이것은 책입니다.", "그것은 가방입니다.",
                             "저것은 창문입니다."],
            },
            {
                "pattern":  "이/그/저 + 명사",
                "meaning":  "Ot qoʻshilganda 것 tushib qoladi: 이것 → 이 책. Odam uchun "
                            "이 사람 / 그 사람 / 저 사람.",
                "examples": ["이 책은 제 책입니다.", "저 사람은 선생님입니다."],
            },
            {
                "pattern":  "여기 / 거기 / 저기 + 에",
                "meaning":  "Joy shakllari. 있다/없다 bilan har doim 에 qoʻshiladi.",
                "examples": ["책이 여기에 있습니다.", "선생님은 저기에 계십니다."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Afsona">아프소나</span> 씨와 <span class="cn-word" data-tr="Jasur">자수르</span> 씨는 <span class="cn-word" data-tr="sinfxona">교실</span>에 있습니다.</p>

<p><strong>아프소나:</strong> 자수르 씨, <span class="cn-word" data-tr="bu narsa">이것</span>은 <span class="cn-word" data-tr="nima">무엇</span>입니까?</p>

<p><strong>자수르:</strong> <span class="cn-word" data-tr="shu narsa">그것</span>은 <span class="cn-word" data-tr="kitob">책</span>입니다. <span class="cn-word" data-tr="bu kitob">이 책</span>은 제 책입니다.</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-tr="anavi narsa">저것</span>도 책입니까?</p>

<p><strong>자수르:</strong> 아니요, <span class="cn-word" data-tr="anavi">저것</span>은 책이 아닙니다. 저것은 <span class="cn-word" data-tr="deraza">창문</span>입니다.</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-tr="anavi odam">저 사람</span>은 <span class="cn-word" data-tr="kim">누구</span>입니까?</p>

<p><strong>자수르:</strong> <span class="cn-word" data-tr="shu odam">그 사람</span>은 <span class="cn-word" data-tr="oʻqituvchi">선생님</span>입니다. 선생님은 <span class="cn-word" data-tr="anavi yer">저기</span>에 <span class="cn-word" data-tr="bor (hurmatli)">계십니다</span>.</p>

<p><strong>아프소나:</strong> 제 <span class="cn-word" data-tr="sumka">가방</span>은 <span class="cn-word" data-tr="qayer">어디</span>에 있습니까?</p>

<p><strong>자수르:</strong> 아프소나 씨 가방은 <span class="cn-word" data-tr="bu yer">여기</span>에 있습니다. <span class="cn-word" data-tr="stol">책상</span> <span class="cn-word" data-tr="ost">아래</span>에 있습니다.</p>

<p>교실에 책상이 있습니다. 책상 <span class="cn-word" data-tr="ust">위</span>에 책이 있습니다. 저기에 <span class="cn-word" data-tr="eshik">문</span>이 있습니다.</p>''',
        "questions": [
            {
                "text": "Afsona “이것은 무엇입니까?” dedi, Jasur esa “그것은 책입니다” deb javob berdi. Nega pogʻona oʻzgardi?",
                "choices": [
                    "Narsa Afsonada — Jasur uchun u “shu”, Afsona uchun “bu”",
                    "Chunki Jasur savolni tushunmadi",
                    "Chunki 그것 har doim javobda ishlatiladi",
                    "Chunki kitob uzoqda edi",
                ],
                "answer": 0,
                "explanation": "Pogʻona kim qarayotganiga qarab almashadi. Narsa "
                               "gapiruvchining tomonida boʻlsa 이것, tinglovchining "
                               "tomonida boʻlsa 그것. Xuddi oʻzbekchadagi “bu” va “shu” "
                               "kabi.",
            },
            {
                "text": "Matnda “이 책은 제 책입니다” deyilgan, “이것 책은” emas. Nega?",
                "choices": [
                    "Ot qoʻshilganda 것 tushib qoladi",
                    "Chunki 책 받침 bilan tugaydi",
                    "Chunki bu egalik gapi",
                    "Chunki 이것 faqat savolda ishlatiladi",
                ],
                "answer": 0,
                "explanation": "것 “narsa” degani, ya'ni 이것 = “bu narsa”. Ot qoʻshilsa "
                               "것 keraksiz boʻlib qoladi va tushadi: 이 책 = “bu kitob”.",
            },
            {
                "text": "Oʻqituvchi qayerda va matn buni qanday ifodalagan?",
                "choices": [
                    "저기에 계십니다 — anavi yerda (hurmatli shakl bilan)",
                    "여기에 있습니다 — bu yerda",
                    "거기에 계십니다 — shu yerda",
                    "교실에 없습니다 — sinfda yoʻq",
                ],
                "answer": 0,
                "explanation": "“선생님은 저기에 계십니다” — 저기 (ikkalasidan uzoq joy) + "
                               "에 (있다/계시다 bilan har doim) + 계십니다 (있다 ning "
                               "hurmatli shakli, chunki gap oʻqituvchi haqida).",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "아침부터 저녁까지",
        "summary": (
            "PK-16 matni. Dilnoza va Bekzod kunlarini va nimasi borligini "
            "solishtiradi — 도, 만, 부터…까지 va 와/과 bir matnda."
        ),
        "order":   16,
        "grammar": [
            {
                "pattern":  "명사 + 도 / 만",
                "meaning":  "도 = “ham”, 만 = “faqat”. Ikkalasi ham 은/는 va 이/가 ni "
                            "ALMASHTIRADI — ular bilan yonma-yon kelmaydi (저도, 책만).",
                "examples": ["저도 학생입니다.", "저는 책만 있습니다.",
                             "자수르 씨만 한국 사람입니다."],
            },
            {
                "pattern":  "명사 + 부터 … 명사 + 까지",
                "meaning":  "“-dan … -gacha”, vaqt oraligʻi uchun. Joy oraligʻida esa "
                            "“…dan” uchun 부터 emas, 에서 ishlatiladi.",
                "examples": ["아침부터 저녁까지", "학교에서 집까지"],
            },
            {
                "pattern":  "명사 + 와/과/하고",
                "meaning":  "“va”, ikki otni bogʻlaydi. 받침 bor → 과, yoʻq → 와. "
                            "하고 hech qachon oʻzgarmaydi va ogʻzaki nutqda koʻproq.",
                "examples": ["책과 가방", "친구와 저", "책하고 돈"],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Dilnoza">딜노자</span> 씨와 <span class="cn-word" data-tr="Bekzod">벡조드</span> 씨는 <span class="cn-word" data-tr="tengdosh">동갑</span>입니다.</p>

<p><strong>딜노자:</strong> 벡조드 씨는 <span class="cn-word" data-tr="ertalab">아침</span><span class="cn-word" data-tr="-dan">부터</span> <span class="cn-word" data-tr="kechqurun">저녁</span><span class="cn-word" data-tr="-gacha">까지</span> <span class="cn-word" data-tr="maktab">학교</span>에 있습니까?</p>

<p><strong>벡조드:</strong> 네, 아침부터 저녁까지 학교에 있습니다. 딜노자 씨<span class="cn-word" data-tr="ham">도</span> 학교에 있습니까?</p>

<p><strong>딜노자:</strong> 저<span class="cn-word" data-tr="ham">도</span> 학교에 있습니다. <span class="cn-word" data-tr="tush payti">점심</span>부터 저녁까지 있습니다.</p>

<p><strong>벡조드:</strong> 딜노자 씨 <span class="cn-word" data-tr="sumka">가방</span> <span class="cn-word" data-tr="ich">안</span>에 <span class="cn-word" data-tr="nima">무엇</span>이 있습니까?</p>

<p><strong>딜노자:</strong> <span class="cn-word" data-tr="kitob">책</span><span class="cn-word" data-tr="va">과</span> <span class="cn-word" data-tr="pul">돈</span>이 있습니다. 벡조드 씨 가방 안에는 무엇이 있습니까?</p>

<p><strong>벡조드:</strong> 저는 책<span class="cn-word" data-tr="faqat">만</span> 있습니다. 돈은 없습니다.</p>

<p><strong>딜노자:</strong> <span class="cn-word" data-tr="doʻst">친구</span>와 저는 <span class="cn-word" data-tr="uy">집</span>에서 학교까지 <span class="cn-word" data-tr="birga">같이</span> 갑니다.</p>

<p>벡조드 씨는 아침부터 저녁까지 학교에 있습니다. 딜노자 씨는 점심부터 저녁까지 학교에 있습니다. 벡조드 씨는 책만 있습니다. 딜노자 씨는 책과 돈이 있습니다. 딜노자 씨와 벡조드 씨는 <span class="cn-word" data-tr="doʻst">친구</span>입니다.</p>''',
        "questions": [
            {
                "text": "Nega matnda “저도 학교에 있습니다” deyilgan, “저는도” emas?",
                "choices": [
                    "도 mavzu qoʻshimchasini (은/는) almashtiradi",
                    "Chunki 저 받침 bilan tugamaydi",
                    "Chunki bu savol gapi",
                    "Chunki 도 faqat feʼl bilan keladi",
                ],
                "answer": 0,
                "explanation": "도 va 만 은/는 va 이/가 ni ALMASHTIRADI, ular bilan "
                               "yonma-yon kelmaydi. Oʻzbekchada ham “men ham” deymiz, "
                               "“menniham” emas.",
            },
            {
                "text": "Bekzodning sumkasida nima bor?",
                "choices": [
                    "Faqat kitob — puli yoʻq",
                    "Kitob va pul",
                    "Faqat pul",
                    "Hech narsa yoʻq",
                ],
                "answer": 0,
                "explanation": "“저는 책만 있습니다. 돈은 없습니다” — 만 “faqat” degani. "
                               "Ikkinchi gapda 은 ishlatilgan, chunki qiyoslanmoqda "
                               "(PK-12 dagi 는 ning “esa” maʼnosi).",
            },
            {
                "text": "Matnda “집에서 학교까지” deyilgan. Nega 부터 emas, 에서?",
                "choices": [
                    "Chunki bu joy oraligʻi, vaqt emas",
                    "Chunki 집 받침 bilan tugamaydi",
                    "Chunki 부터 faqat ertalab uchun",
                    "Chunki keyin 까지 keladi",
                ],
                "answer": 0,
                "explanation": "Vaqt oraligʻida “…dan” uchun 부터 (아침부터), joy oraligʻida "
                               "esa 에서 (집에서) ishlatiladi. “…gacha” ikkalasida ham 까지.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "제 가방 안에",
        "summary": (
            "PK-17 matni. Sherbek kunini soʻzlab beradi — 을/를 toʻldiruvchisi va "
            "birinchi feʼllar, hamda 에 va 에서 farqi amalda."
        ),
        "order":   17,
        "grammar": [
            {
                "pattern":  "명사 + 을/를 + 동사",
                "meaning":  "Toʻldiruvchi qoʻshimchasi — oʻzbekcha “-ni”. 받침 bor → 을, "
                            "yoʻq → 를. Soʻz tartibi oʻzbekcha bilan bir xil: "
                            "ega → toʻldiruvchi → kesim.",
                "examples": ["저는 책을 읽습니다.", "저는 커피를 마십니다.",
                             "한국어를 공부합니다."],
            },
            {
                "pattern":  "장소 + 에서 + 동사",
                "meaning":  "Harakat feʼli bilan joy 에서 oladi; 있다/없다 bilan esa 에. "
                            "Mana shu farq PK-14 da oʻrgatilgan edi va endi ishlaydi.",
                "examples": ["집에서 우유를 마십니다.", "학교에서 공부합니다.",
                             "교실에 있습니다."],
            },
            {
                "pattern":  "명사 + 의 · 제 / 내",
                "meaning":  "Egalik — oʻzbekcha “-ning”. Egalik maʼnosida [에] deb "
                            "oʻqiladi. Amalda 저의 → 제, 나의 → 내 qisqargan shakli "
                            "ishlatiladi; tabiiy bogʻlangan otlarda 의 tushadi.",
                "examples": ["친구의 가방", "제 이름", "한국 사람"],
            },
        ],
        "body": '''<p>저는 <span class="cn-word" data-tr="Sherbek">셰르벡</span>입니다. <span class="cn-word" data-tr="mening">제</span> <span class="cn-word" data-tr="kun">하루</span>는 <span class="cn-word" data-tr="ertalab">아침</span>부터 <span class="cn-word" data-tr="kechqurun">저녁</span>까지입니다.</p>

<p>아침에 저는 <span class="cn-word" data-tr="uy">집</span>에서 <span class="cn-word" data-tr="sut">우유</span><span class="cn-word" data-tr="-ni">를</span> <span class="cn-word" data-pos="verb" data-tr="ichaman">마십니다</span>. <span class="cn-word" data-tr="ovqat">밥</span>도 <span class="cn-word" data-pos="verb" data-tr="yeyman">먹습니다</span>.</p>

<p><span class="cn-word" data-tr="keyin">그리고</span> 저는 <span class="cn-word" data-tr="maktab">학교</span>에 갑니다. 학교<span class="cn-word" data-tr="-da (harakat)">에서</span> <span class="cn-word" data-tr="koreys tili">한국어</span>를 <span class="cn-word" data-pos="verb" data-tr="oʻrganaman">공부합니다</span>. 저는 한국어를 <span class="cn-word" data-pos="verb" data-tr="yoqtiraman">좋아합니다</span>.</p>

<p><span class="cn-word" data-tr="mening">제</span> <span class="cn-word" data-tr="sumka">가방</span> <span class="cn-word" data-tr="ich">안</span>에 <span class="cn-word" data-tr="kitob">책</span>과 <span class="cn-word" data-tr="pul">돈</span>이 있습니다.</p>

<p><strong>딜노자:</strong> 셰르벡 씨, 그 책은 <span class="cn-word" data-tr="kim">누구</span><span class="cn-word" data-tr="-ning">의</span> 책입니까?</p>

<p><strong>셰르벡:</strong> 이 책은 <span class="cn-word" data-tr="doʻst">친구</span>의 책입니다. 저는 이 책을 <span class="cn-word" data-pos="verb" data-tr="oʻqiyman">읽습니다</span>.</p>

<p><strong>딜노자:</strong> 저도 그 책을 좋아합니다.</p>

<p><span class="cn-word" data-tr="kechqurun">저녁</span>에 저는 집에 있습니다. 집에서 <span class="cn-word" data-tr="televizor">텔레비전</span>을 <span class="cn-word" data-pos="verb" data-tr="koʻraman">봅니다</span>. <span class="cn-word" data-tr="tush payti">점심</span>부터 저녁까지 저는 <span class="cn-word" data-tr="vaqt">시간</span>이 없습니다.</p>''',
        "questions": [
            {
                "text": "Matnda “집에서 우유를 마십니다” va “집에 있습니다” — nega bir xil joy ikki xil qoʻshimcha oladi?",
                "choices": [
                    "마시다 harakat feʼli (에서), 있다 esa holat bildiradi (에)",
                    "Chunki birinchisi ertalab, ikkinchisi kechqurun",
                    "Chunki 집 받침 bilan tugamaydi",
                    "Ikkalasi ham xato, bir xil boʻlishi kerak",
                ],
                "answer": 0,
                "explanation": "PK-14 qoidasi: 있다/없다 bilan har doim 에, harakat feʼli "
                               "bilan esa 에서. Uyda TURIBMAN → 집에 있습니다; uyda ICHAMAN "
                               "→ 집에서 마십니다. Oʻzbekchada ikkalasi ham “uyda”.",
            },
            {
                "text": "“저는 한국어를 공부합니다” gapida 를 nima vazifasini bajaradi?",
                "choices": [
                    "Toʻldiruvchini belgilaydi — oʻzbekcha “-ni”",
                    "Egani belgilaydi",
                    "Mavzuni belgilaydi",
                    "Joyni belgilaydi",
                ],
                "answer": 0,
                "explanation": "을/를 — toʻldiruvchi qoʻshimchasi, oʻzbekcha “-ni” bilan "
                               "aynan bir xil vazifada: “koreys tili<b>ni</b> oʻrganaman”. "
                               "한국어 unli bilan tugagani uchun 를 tanlangan.",
            },
            {
                "text": "Sherbek oʻqiyotgan kitob kimniki?",
                "choices": [
                    "Doʻstiniki",
                    "Oʻziniki",
                    "Dilnozaniki",
                    "Oʻqituvchiniki",
                ],
                "answer": 0,
                "explanation": "“이 책은 친구의 책입니다” — 의 egalik qoʻshimchasi, oʻzbekcha "
                               "“-ning”. Ya'ni kitob doʻstiniki. Egalik maʼnosida 의 [에] "
                               "deb oʻqiladi.",
            },
        ],
    },
]
