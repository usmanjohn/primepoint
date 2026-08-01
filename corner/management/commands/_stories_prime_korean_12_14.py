# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-12 … PK-14.

Kumulyativ qoida: faqat PK-14 gacha oʻrganilgan grammatika. Dialog satrlari qat'iy
ravishda darslar doirasida; hikoya satrlari toc dagi yopiq feʼllar roʻyxatidan
foydalanadi (있습니다, 없습니다, 갑니다, 왔습니다, 만났습니다, 말했습니다, 주었습니다).

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_12_14.py --author=prime
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
        "title":   "제 친구 아프소나",
        "summary": (
            "PK-12 matni. Bekzod sinfdoshlarini tanishtiradi — 은/는 qiyoslash uchun, "
            "이/가 esa “kim?” savoliga javob berish uchun ishlatiladi."
        ),
        "order":   12,
        "grammar": [
            {
                "pattern":  "명사 + 은/는",
                "meaning":  "Mavzu qoʻshimchasi — “…ga kelsak”, oʻzbekcha “esa”. 받침 bor "
                            "boʻlsa 은, yoʻq boʻlsa 는. Ikki narsani qiyoslaganda ham shu.",
                "examples": ["저는 학생입니다.", "아프소나 씨는 의사입니다.",
                             "선생님은 지영입니다."],
            },
            {
                "pattern":  "명사 + 이/가",
                "meaning":  "Ega qoʻshimchasi — “kim?” savoliga javob va yangi maʼlumot. "
                            "받침 bor boʻlsa 이, yoʻq boʻlsa 가.",
                "examples": ["누가 선생님입니까?", "지영 씨가 선생님입니다."],
            },
            {
                "pattern":  "누가 …입니까?",
                "meaning":  "“Kim …dir?”. Bu savolga javobda HAR DOIM 이/가 ishlatiladi, "
                            "은/는 emas — chunki javob yangi maʼlumot beradi.",
                "examples": ["누가 학생입니까?", "누가 의사입니까?"],
            },
        ],
        "body": '''<p>저는 <span class="cn-word" data-tr="Bekzod">벡조드</span>입니다. 저는 <span class="cn-word" data-tr="talaba">학생</span>입니다.</p>

<p><span class="cn-word" data-tr="Afsona">아프소나</span> 씨는 제 <span class="cn-word" data-tr="doʻst">친구</span>입니다. 아프소나 씨는 <span class="cn-word" data-tr="shifokor">의사</span>입니다. <span class="cn-word" data-tr="Jasur">자수르</span> 씨는 의사가 <span class="cn-word" data-tr="emas">아닙니다</span>. 자수르 씨는 학생입니다.</p>

<p><span class="cn-word" data-tr="Jiyoung">지영</span> 씨가 <span class="cn-word" data-pos="verb" data-tr="keldi">왔습니다</span>.</p>

<p><strong>벡조드:</strong> <span class="cn-word" data-tr="kim">누가</span> <span class="cn-word" data-tr="oʻqituvchi">선생님</span>입니까?</p>

<p><strong>아프소나:</strong> 지영 씨가 선생님입니다.</p>

<p><strong>벡조드:</strong> 지영 씨는 <span class="cn-word" data-tr="koreys">한국 사람</span>입니까?</p>

<p><strong>아프소나:</strong> 네, 지영 씨는 한국 사람입니다.</p>

<p><strong>벡조드:</strong> 아프소나 씨는 한국 사람입니까?</p>

<p><strong>아프소나:</strong> 아니요. 저는 한국 사람이 아닙니다. 저는 <span class="cn-word" data-tr="oʻzbek">우즈베키스탄 사람</span>입니다.</p>

<p>저는 <span class="cn-word" data-tr="ism">이름</span>이 벡조드입니다. 아프소나 씨는 의사입니다. 자수르 씨는 학생입니다. 지영 씨는 선생님입니다. <span class="cn-word" data-tr="biz">우리</span>는 친구입니다.</p>''',
        "questions": [
            {
                "text": "Nega Bekzodning savoliga “지영 씨가 선생님입니다” deb javob berildi, “지영 씨는” emas?",
                "choices": [
                    "Chunki “누가?” (kim?) savoliga javobda har doim 이/가 ishlatiladi",
                    "Chunki 지영 받침 bilan tugaydi",
                    "Chunki Jiyoung koreys",
                    "Chunki bu inkor gap",
                ],
                "answer": 0,
                "explanation": "“누가?” savoli aynan egani soʻraydi va javob yangi "
                               "maʼlumot beradi — shuning uchun 이/가. Agar 는 ishlatilsa, "
                               "“Jiyoungga kelsak…” degan maʼno chiqib, savolga javob "
                               "boʻlmay qolardi.",
            },
            {
                "text": "Matnda “자수르 씨는 의사가 아닙니다” deyilgan. Nega bu yerda 가 turibdi?",
                "choices": [
                    "Chunki 아니다 dan oldin har doim 이/가 keladi",
                    "Chunki 의사 받침 bilan tugaydi",
                    "Chunki bu savol gapi",
                    "Chunki Jasur talaba",
                ],
                "answer": 0,
                "explanation": "아니다 (“emas”) dan oldingi ot har doim 이/가 oladi. "
                               "의사 unli bilan tugagani uchun 가 tanlandi. Gapdagi mavzu "
                               "esa 자수르 씨는 — bitta gapda bitta mavzu, bitta ega.",
            },
            {
                "text": "Afsona kim?",
                "choices": [
                    "Oʻzbekistonlik shifokor",
                    "Koreys oʻqituvchi",
                    "Oʻzbekistonlik talaba",
                    "Koreys shifokor",
                ],
                "answer": 0,
                "explanation": "“아프소나 씨는 의사입니다” — u shifokor. Va oʻzi aytdi: "
                               "“저는 한국 사람이 아닙니다. 저는 우즈베키스탄 사람입니다” — "
                               "koreys emas, oʻzbekistonlik.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "저는 친구가 있습니다",
        "summary": (
            "PK-13 matni. Dilnoza va Sherbek nimasi bor, nimasi yoʻqligi haqida "
            "gaplashadi — 있습니다 / 없습니다 va egalik tuzilishi."
        ),
        "order":   13,
        "grammar": [
            {
                "pattern":  "명사 + 이/가 있습니다 / 없습니다",
                "meaning":  "“…bor” va “…yoʻq”. 있다/없다 dan oldingi ot har doim 이/가 "
                            "oladi, chunki u gapning egasi. Oʻqilishi [읻씀니다] / [업씀니다].",
                "examples": ["책이 있습니다.", "시간이 없습니다.", "질문이 있습니까?"],
            },
            {
                "pattern":  "저는 + 명사 + 이/가 있습니다",
                "meaning":  "Egalik: “menda … bor”. Koreys tilida alohida “ega boʻlmoq” "
                            "feʼli yoʻq — mavzu + ega + 있다 ishlatiladi. Bu oʻzbekcha "
                            "“menda … bor” tuzilishi bilan aynan bir xil.",
                "examples": ["저는 친구가 있습니다.", "지영 씨는 가방이 없습니다."],
            },
            {
                "pattern":  "계십니다",
                "meaning":  "있다 ning hurmatli shakli. FAQAT odamlarga nisbatan "
                            "ishlatiladi — narsalar uchun hech qachon.",
                "examples": ["선생님이 계십니다."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Dilnoza">딜노자</span> 씨가 <span class="cn-word" data-pos="verb" data-tr="keldi">왔습니다</span>. <span class="cn-word" data-tr="Sherbek">셰르벡</span> 씨가 왔습니다.</p>

<p><strong>딜노자:</strong> 셰르벡 씨, <span class="cn-word" data-tr="vaqt">시간</span>이 <span class="cn-word" data-tr="bormi">있습니까</span>?</p>

<p><strong>셰르벡:</strong> 네, 시간이 <span class="cn-word" data-tr="bor">있습니다</span>.</p>

<p><strong>딜노자:</strong> 저는 <span class="cn-word" data-tr="savol">질문</span>이 있습니다. 셰르벡 씨는 <span class="cn-word" data-tr="kitob">책</span>이 있습니까?</p>

<p><strong>셰르벡:</strong> 아니요, 저는 책이 <span class="cn-word" data-tr="yoʻq">없습니다</span>. 저는 <span class="cn-word" data-tr="sumka">가방</span>이 없습니다. <span class="cn-word" data-tr="pul">돈</span>이 없습니다.</p>

<p><strong>딜노자:</strong> <span class="cn-word" data-tr="unda, xoʻsh">그럼</span>, 셰르벡 씨는 <span class="cn-word" data-tr="nima">무엇</span>이 있습니까?</p>

<p><strong>셰르벡:</strong> 저는 <span class="cn-word" data-tr="doʻst">친구</span>가 있습니다. 딜노자 씨가 제 친구입니다.</p>

<p>딜노자 씨는 책이 있습니다. 딜노자 씨는 가방이 있습니다. 셰르벡 씨는 친구가 있습니다.</p>

<p><span class="cn-word" data-tr="oʻqituvchi">선생님</span>이 <span class="cn-word" data-tr="bor (hurmatli)">계십니다</span>. 선생님은 <span class="cn-word" data-tr="Jiyoung">지영</span> 씨입니다. 지영 씨는 질문이 없습니다.</p>''',
        "questions": [
            {
                "text": "Sherbekda nima bor?",
                "choices": [
                    "Doʻst",
                    "Kitob va sumka",
                    "Pul",
                    "Hech narsa yoʻq",
                ],
                "answer": 0,
                "explanation": "“저는 친구가 있습니다” — Sherbekda kitob ham, sumka ham, "
                               "pul ham yoʻq, lekin doʻsti bor. Va u qoʻshib qoʻydi: "
                               "“딜노자 씨가 제 친구입니다”.",
            },
            {
                "text": "Nega matnda “선생님이 계십니다” deyilgan, “있습니다” emas?",
                "choices": [
                    "Chunki 계시다 — 있다 ning hurmatli shakli va odamlarga ishlatiladi",
                    "Chunki oʻqituvchi uzoqda turibdi",
                    "Chunki bu savol gapi",
                    "Chunki 선생님 받침 bilan tugaydi",
                ],
                "answer": 0,
                "explanation": "계시다 — 있다 ning hurmatli shakli. U FAQAT odamlarga "
                               "nisbatan ishlatiladi. Narsa uchun ishlatilsa (책이 "
                               "계십니다) kulgili chiqadi.",
            },
            {
                "text": "“저는 친구가 있습니다” gapida nega ikki xil qoʻshimcha bor?",
                "choices": [
                    "저는 — mavzu, 친구가 — ega",
                    "저는 — ega, 친구가 — toʻldiruvchi",
                    "Ikkalasi ham ega",
                    "Bu xato, bittasi ortiqcha",
                ],
                "answer": 0,
                "explanation": "Bu PK-12 dagi farqning amaliy koʻrinishi: 저는 mavzuni "
                               "belgilaydi (“men haqimda”), 친구가 esa egani (“nima bor”). "
                               "Bitta gapda bitta mavzu va bitta ega boʻlishi normal.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "우리 교실에 있습니다",
        "summary": (
            "PK-14 matni. Jasur sinfxonada nima qayerdaligini tasvirlaydi — 에 "
            "qoʻshimchasi, oʻrin soʻzlari va 에서 ning “…dan” maʼnosi."
        ),
        "order":   14,
        "grammar": [
            {
                "pattern":  "장소 + 에 있습니다 / 없습니다",
                "meaning":  "Joyda turish. 있다/없다 koʻrsangiz — HAR DOIM 에, hech qachon "
                            "에서 emas. Bu istisnosiz ishlaydigan qoida.",
                "examples": ["책이 가방에 있습니다.", "지영 씨는 교실에 있습니다."],
            },
            {
                "pattern":  "명사 + 안/위/아래/앞/뒤/옆 + 에",
                "meaning":  "Oʻrin soʻzi otdan KEYIN keladi — xuddi oʻzbekchadagi "
                            "“sumka ichida”, “stol ustida” kabi. Ingliz tilida esa teskari.",
                "examples": ["가방 안에 있습니다.", "책상 위에 있습니다.",
                             "친구 옆에 있습니다."],
            },
            {
                "pattern":  "장소 + 에서 왔습니다",
                "meaning":  "“…dan keldim”. 에서 ning ikkinchi maʼnosi — kelib chiqish, "
                            "oʻzbekcha “-dan”. Tanishuvda eng koʻp ishlatiladigan gaplardan.",
                "examples": ["저는 우즈베키스탄에서 왔습니다."],
            },
        ],
        "body": '''<p>저는 자수르입니다. 저는 <span class="cn-word" data-tr="Oʻzbekiston">우즈베키스탄</span>에서 <span class="cn-word" data-pos="verb" data-tr="keldim">왔습니다</span>. <span class="cn-word" data-tr="bugun">오늘</span> 저는 <span class="cn-word" data-tr="sinfxona">교실</span>에 <span class="cn-word" data-tr="bor, turibman">있습니다</span>.</p>

<p>우리 교실에 <span class="cn-word" data-tr="stol, parta">책상</span>이 있습니다. 책상 <span class="cn-word" data-tr="ust">위</span>에 <span class="cn-word" data-tr="kitob">책</span>이 있습니다. 책상 <span class="cn-word" data-tr="ost">아래</span>에 <span class="cn-word" data-tr="sumka">가방</span>이 있습니다. 가방 <span class="cn-word" data-tr="ich">안</span>에 <span class="cn-word" data-tr="pul">돈</span>이 없습니다.</p>

<p><strong>딜노자:</strong> 자수르 씨, <span class="cn-word" data-tr="oʻqituvchi">선생님</span>이 교실에 <span class="cn-word" data-tr="bormi">있습니까</span>?</p>

<p><strong>자수르:</strong> 아니요, 선생님은 교실에 없습니다. 선생님은 교실 <span class="cn-word" data-tr="tashqari">밖</span>에 <span class="cn-word" data-tr="bor (hurmatli)">계십니다</span>.</p>

<p><strong>딜노자:</strong> 아프소나 씨는 <span class="cn-word" data-tr="qayer">어디</span>에 있습니까?</p>

<p><strong>자수르:</strong> 아프소나 씨는 제 <span class="cn-word" data-tr="yon">옆</span>에 있습니다.</p>

<p>그리고 <span class="cn-word" data-tr="Bekzod">벡조드</span> 씨가 <span class="cn-word" data-pos="verb" data-tr="keldi">왔습니다</span>. 벡조드 씨는 <span class="cn-word" data-tr="Koreya">한국</span>에서 왔습니다.</p>

<p><strong>벡조드:</strong> 안녕하세요? 저는 한국에서 왔습니다. <span class="cn-word" data-tr="ertalab">아침</span>에 시간이 있습니다.</p>

<p>교실 <span class="cn-word" data-tr="old">앞</span>에 <span class="cn-word" data-tr="eshik">문</span>이 있습니다. 교실 <span class="cn-word" data-tr="orqa">뒤</span>에 <span class="cn-word" data-tr="deraza">창문</span>이 있습니다. 우리 교실에 책상, 가방, 문, 창문이 있습니다.</p>''',
        "questions": [
            {
                "text": "Matnda “교실에 있습니다” deyilgan, “교실에서 있습니다” emas. Nega?",
                "choices": [
                    "Chunki 있다/없다 bilan har doim 에 ishlatiladi",
                    "Chunki 교실 받침 bilan tugaydi",
                    "Chunki bu oʻtgan zamon",
                    "Chunki 에서 faqat odamlar uchun",
                ],
                "answer": 0,
                "explanation": "있다/없다 holatni bildiradi, harakatni emas — shuning uchun "
                               "har doim 에. 에서 esa harakat joyini koʻrsatadi "
                               "(교실에서 공부합니다). Oʻzbekchada ikkalasi ham “-da” "
                               "boʻlgani uchun bu chalkashadi.",
            },
            {
                "text": "Sumka qayerda va uning ichida nima bor?",
                "choices": [
                    "Stol ostida; ichida pul yoʻq",
                    "Stol ustida; ichida kitob bor",
                    "Sinf tashqarisida; ichida pul bor",
                    "Eshik oldida; ichida kitob yoʻq",
                ],
                "answer": 0,
                "explanation": "“책상 아래에 가방이 있습니다” — sumka stol ostida. "
                               "“가방 안에 돈이 없습니다” — ichida pul yoʻq. Oʻrin soʻzlari "
                               "(아래, 안) otdan keyin keladi.",
            },
            {
                "text": "“저는 우즈베키스탄에서 왔습니다” dagi 에서 qaysi maʼnoda?",
                "choices": [
                    "“…dan” — kelib chiqish",
                    "“…da” — harakat joyi",
                    "“…ga” — yoʻnalish",
                    "“…gacha” — chegara",
                ],
                "answer": 0,
                "explanation": "Bu 에서 ning ikkinchi maʼnosi: kelib chiqish, oʻzbekcha "
                               "“-dan”. Agar 에 ishlatilsa (우즈베키스탄에 왔습니다), maʼno "
                               "“Oʻzbekistonga keldim” boʻlib oʻzgarardi.",
            },
        ],
    },
]
