# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-18 … PK-20.

PK-18 dan boshlab feʼl tizimi ochildi, shuning uchun bu matnlar toc dagi
"narrative frame" istisnosiga muhtoj emas — hamma shakl darslarda oʻrgatilgan.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_18_20.py --author=prime
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
        "title":   "저는 매일 공부해요",
        "summary": (
            "PK-18 matni. Afsonaning bir kuni — 해요체 dagi birinchi toʻliq matn. "
            "Feʼllar ham, sifatlar ham bir xil qoida bilan tuslanadi."
        ),
        "order":   18,
        "grammar": [
            {
                "pattern":  "동사/형용사 어간 + 아요 / 어요 / 해요",
                "meaning":  "해요체 — kundalik hurmat shakli. Oʻzakning oxirgi unlisi "
                            "ㅏ yoki ㅗ boʻlsa 아요, boshqa har qanday holatda 어요, "
                            "하다 esa har doim 해요.",
                "examples": ["먹어요", "좋아요", "공부해요", "마셔요"],
            },
            {
                "pattern":  "Qisqargan oʻzaklar",
                "meaning":  "Oʻzak unli bilan tugasa, ikki unli qoʻshilib ketadi: "
                            "ㅗ+ㅏ=ㅘ, ㅜ+ㅓ=ㅝ, ㅣ+ㅓ=ㅕ. Bu PK-3 dagi qoʻshma unlilar.",
                "examples": ["보다 → 봐요", "주다 → 줘요", "마시다 → 마셔요",
                             "오다 → 와요"],
            },
            {
                "pattern":  "형용사 = 동사 · 명사 + 이에요/예요",
                "meaning":  "Koreys sifati feʼlning oʻzi — bogʻlama kerak emas "
                            "(좋아요, 맛있어요). Otga esa 이에요 (받침 bor) yoki "
                            "예요 (받침 yoʻq) qoʻshiladi.",
                "examples": ["재미있어요.", "학생이에요.", "의사예요."],
            },
        ],
        "body": '''<p>저는 <span class="cn-word" data-tr="Afsona">아프소나</span><span class="cn-word" data-tr="…man (kundalik)">예요</span>. 저는 <span class="cn-word" data-tr="talaba">학생</span><span class="cn-word" data-tr="…man">이에요</span>.</p>

<p><span class="cn-word" data-tr="ertalab">아침</span>에 저는 <span class="cn-word" data-tr="uy">집</span>에서 <span class="cn-word" data-tr="sut">우유</span>를 <span class="cn-word" data-pos="verb" data-tr="ichaman">마셔요</span>. <span class="cn-word" data-tr="ovqat">밥</span>도 <span class="cn-word" data-pos="verb" data-tr="yeyman">먹어요</span>.</p>

<p><span class="cn-word" data-tr="keyin">그리고</span> <span class="cn-word" data-tr="maktab">학교</span>에 <span class="cn-word" data-pos="verb" data-tr="boraman">가요</span>. 학교에서 <span class="cn-word" data-tr="koreys tili">한국어</span>를 <span class="cn-word" data-pos="verb" data-tr="oʻrganaman">공부해요</span>.</p>

<p>한국어가 <span class="cn-word" data-pos="adj" data-tr="qiziqarli">재미있어요</span>. 저는 한국어를 <span class="cn-word" data-pos="verb" data-tr="yoqtiraman">좋아해요</span>.</p>

<p><span class="cn-word" data-tr="tush payti">점심</span>에 <span class="cn-word" data-tr="doʻst">친구</span>를 <span class="cn-word" data-pos="verb" data-tr="uchrataman">만나요</span>. 우리는 <span class="cn-word" data-tr="birga">같이</span> 밥을 먹어요. 밥이 <span class="cn-word" data-pos="adj" data-tr="mazali">맛있어요</span>.</p>

<p><span class="cn-word" data-tr="kechqurun">저녁</span>에 집에 <span class="cn-word" data-pos="verb" data-tr="kelaman">와요</span>. 집에서 <span class="cn-word" data-tr="kitob">책</span>을 <span class="cn-word" data-pos="verb" data-tr="oʻqiyman">읽어요</span>. <span class="cn-word" data-tr="televizor">텔레비전</span>도 <span class="cn-word" data-pos="verb" data-tr="koʻraman">봐요</span>.</p>

<p><strong>딜노자:</strong> 아프소나 씨, <span class="cn-word" data-tr="har kuni">매일</span> 한국어를 공부해요?</p>

<p><strong>아프소나:</strong> 네, 매일 공부해요. 딜노자 씨도 한국어를 공부해요?</p>

<p><strong>딜노자:</strong> 저는 <span class="cn-word" data-tr="dam olish kuni">주말</span>에 공부해요. 저도 한국어를 좋아해요.</p>''',
        "questions": [
            {
                "text": "Nega matnda “재미있어요” deyilgan, “재미있이에요” emas?",
                "choices": [
                    "재미있다 — sifat, ya'ni feʼlning oʻzi; bogʻlama kerak emas",
                    "Chunki 재미있다 받침 bilan tugamaydi",
                    "Chunki bu savol gapi",
                    "Chunki 이에요 faqat odamlar uchun",
                ],
                "answer": 0,
                "explanation": "Koreys tilida sifat feʼlning oʻzi — u mustaqil tuslanadi "
                               "va unga 이에요 qoʻshish kerak emas. 이에요/예요 faqat OTGA "
                               "qoʻshiladi: 학생이에요, 의사예요.",
            },
            {
                "text": "“마셔요” qanday yasalgan?",
                "choices": [
                    "마시 + 어요, ㅣ va ㅓ qoʻshilib ㅕ boʻlgan",
                    "마시 + 아요, chunki oxirgi unli ㅏ",
                    "마시다 + 요",
                    "마셔 + 이에요",
                ],
                "answer": 0,
                "explanation": "Oʻzak 마시 unli bilan tugaydi. Oxirgi unli ㅣ — ㅏ ham, ㅗ "
                               "ham emas, demak 어요. Ikki unli qoʻshilib qisqaradi: "
                               "ㅣ + ㅓ = ㅕ → 마셔요.",
            },
            {
                "text": "Dilnoza qachon koreys tilini oʻrganadi?",
                "choices": [
                    "Dam olish kunlari",
                    "Har kuni",
                    "Ertalab",
                    "Umuman oʻrganmaydi",
                ],
                "answer": 0,
                "explanation": "“저는 주말에 공부해요” — u dam olish kunlari oʻrganadi, "
                               "Afsona esa har kuni (매일). Diqqat: 주말 vaqt bildirgani "
                               "uchun 에 oladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "자기소개를 합니다",
        "summary": (
            "PK-19 matni. Bekzod bir xil narsani ikki xil darajada aytadi — "
            "합니다체 sinf oldida, 해요체 doʻsti bilan."
        ),
        "order":   19,
        "grammar": [
            {
                "pattern":  "동사/형용사 어간 + ㅂ니다 / 습니다",
                "meaning":  "합니다체 — rasmiy daraja. Oʻzak unli bilan tugasa ㅂ니다 "
                            "(ㅂ oxirgi blok tagiga tushadi), undosh bilan tugasa 습니다. "
                            "Unli uygʻunligi yoʻq — faqat 받침 ayrisi.",
                "examples": ["갑니다", "먹습니다", "마십니다", "좋습니다"],
            },
            {
                "pattern":  "ㄹ 어간 + ㅂ니다",
                "meaning":  "Oʻzak ㄹ bilan tugasa, ㄹ TUSHIB QOLADI: 살다 → 삽니다, "
                            "알다 → 압니다. 해요체 da esa ㄹ joyida qoladi (살아요).",
                "examples": ["살다 → 삽니다", "알다 → 압니다"],
            },
            {
                "pattern":  "합니다체 va 해요체 farqi",
                "meaning":  "Ikkalasi ham 존댓말. 합니다체 — rasmiy, masofali "
                            "(taqdimot, xizmat sohasi). 해요체 — kundalik, iliq "
                            "(doʻstlar, qoʻshnilar, sinf).",
                "examples": ["공부합니다 (rasmiy)", "공부해요 (kundalik)"],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Bekzod">벡조드</span> 씨는 <span class="cn-word" data-tr="sinfxona">교실</span>에서 <span class="cn-word" data-tr="oʻzini tanishtirish">자기소개</span>를 <span class="cn-word" data-pos="verb" data-tr="qiladi">합니다</span>.</p>

<p><strong>벡조드:</strong> 안녕하세요? 저는 벡조드<span class="cn-word" data-tr="…man (rasmiy)">입니다</span>. <span class="cn-word" data-tr="Oʻzbekiston">우즈베키스탄</span>에서 <span class="cn-word" data-pos="verb" data-tr="keldim">왔습니다</span>. 저는 <span class="cn-word" data-tr="talaba">학생</span>입니다.</p>

<p><strong>벡조드:</strong> <span class="cn-word" data-tr="har kuni">매일</span> <span class="cn-word" data-tr="maktab">학교</span>에 <span class="cn-word" data-pos="verb" data-tr="boraman (rasmiy)">갑니다</span>. 학교에서 <span class="cn-word" data-tr="koreys tili">한국어</span>를 <span class="cn-word" data-pos="verb" data-tr="oʻrganaman (rasmiy)">배웁니다</span>. 한국어가 <span class="cn-word" data-pos="adj" data-tr="qiziqarli (rasmiy)">재미있습니다</span>.</p>

<p><strong>벡조드:</strong> 저는 <span class="cn-word" data-tr="Seul">서울</span>에 <span class="cn-word" data-pos="verb" data-tr="yashayman">삽니다</span>. <span class="cn-word" data-tr="mening">제</span> <span class="cn-word" data-tr="uy">집</span>은 학교 <span class="cn-word" data-tr="yon">옆</span>에 있습니다. <span class="cn-word" data-tr="rahmat">감사합니다</span>.</p>

<p><span class="cn-word" data-tr="keyin">그리고</span> 벡조드 씨는 <span class="cn-word" data-tr="doʻst">친구</span> <span class="cn-word" data-tr="Jasur">자수르</span> 씨를 <span class="cn-word" data-pos="verb" data-tr="uchratadi">만납니다</span>. 친구하고는 <span class="cn-word" data-tr="kundalik daraja">해요체</span>가 <span class="cn-word" data-pos="adj" data-tr="yaxshi">좋아요</span>.</p>

<p><strong>벡조드:</strong> 자수르 씨, 저는 벡조드<span class="cn-word" data-tr="…man (kundalik)">예요</span>. 서울에 <span class="cn-word" data-pos="verb" data-tr="yashayman (kundalik)">살아요</span>. 한국어를 <span class="cn-word" data-pos="verb" data-tr="oʻrganaman (kundalik)">배워요</span>.</p>

<p><strong>자수르:</strong> 저도 한국어를 배워요. 한국어가 <span class="cn-word" data-pos="adj" data-tr="qiziqarli">재미있어요</span>.</p>

<p>벡조드 씨는 교실에서 <span class="cn-word" data-tr="rasmiy daraja">합니다체</span>를 <span class="cn-word" data-pos="verb" data-tr="ishlatadi">씁니다</span>. 친구하고 해요체를 씁니다. 합니다체와 해요체는 <span class="cn-word" data-tr="hurmat nutqi">존댓말</span>입니다.</p>''',
        "questions": [
            {
                "text": "Nega Bekzod “살다” ni 삽니다 deb aytdi, 살습니다 emas?",
                "choices": [
                    "Oʻzak ㄹ bilan tugaydi — ㅂ니다 oldidan ㄹ tushib qoladi",
                    "Chunki 살다 sifat",
                    "Chunki 살 받침siz",
                    "Chunki bu oʻtgan zamon",
                ],
                "answer": 0,
                "explanation": "ㄹ oʻzaklarda ㅂ니다 qoʻshilganda ㄹ tushadi: 살 → 사 + ㅂ니다 "
                               "= 삽니다. 해요체 da esa ㄹ joyida qoladi — matnda buni ham "
                               "koʻrasiz: 살아요.",
            },
            {
                "text": "Bekzod nega bir xil narsani ikki xil shaklda aytdi?",
                "choices": [
                    "Sinf oldida rasmiy (합니다체), doʻsti bilan kundalik (해요체)",
                    "Chunki birinchi marta xato qildi",
                    "Chunki 합니다체 oʻtgan zamon",
                    "Chunki doʻsti koreys tilini bilmaydi",
                ],
                "answer": 0,
                "explanation": "Ikkalasi ham 존댓말 (hurmat nutqi), lekin 합니다체 rasmiy va "
                               "masofali — taqdimot uchun; 해요체 esa iliq va kundalik — "
                               "doʻstlar uchun. Matnning oxirgi jumlasi shuni aytadi.",
            },
            {
                "text": "“재미있습니다” va “재미있어요” orasidagi farq nima?",
                "choices": [
                    "Faqat daraja — maʼnosi bir xil",
                    "Birinchisi oʻtgan zamon",
                    "Birinchisi savol",
                    "Birinchisi sifat, ikkinchisi feʼl",
                ],
                "answer": 0,
                "explanation": "Maʼnosi bir xil — “qiziqarli”. Farqi faqat nutq darajasida: "
                               "재미있습니다 rasmiy (합니다체), 재미있어요 kundalik (해요체). "
                               "재미있다 받침li oʻzak, shuning uchun 습니다 oladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "어제 무엇을 했어요?",
        "summary": (
            "PK-20 matni. Sherbek va Jiyoung kechagi kunlarini soʻzlaydi — "
            "oʻtgan zamon 았/었어요 butun matn davomida."
        ),
        "order":   20,
        "grammar": [
            {
                "pattern":  "동사/형용사 + 았어요 / 었어요 / 했어요",
                "meaning":  "Oʻtgan zamon. Yangi qoida yoʻq: avval 아/어요 shaklini "
                            "yasang, 요 ni oling, ㅆ어요 qoʻshing. 하다 → 해요 → 했어요.",
                "examples": ["먹어요 → 먹었어요", "가요 → 갔어요", "봐요 → 봤어요",
                             "해요 → 했어요"],
            },
            {
                "pattern":  "았/었습니다",
                "meaning":  "Rasmiy oʻtgan zamon. Oʻtgan oʻzak har doim ㅆ 받침i bilan "
                            "tugagani uchun HAR DOIM 습니다 oladi, hech qachon ㅂ니다 emas.",
                "examples": ["갔습니다", "먹었습니다", "했습니다"],
            },
            {
                "pattern":  "이었어요 / 였어요 · 있었어요 / 없었어요",
                "meaning":  "이다 ning oʻtgan shakli 받침 ayrisiga boʻysunadi. "
                            "있다/없다 esa oddiy qoida bilan: 있었어요, 없었어요.",
                "examples": ["학생이었어요.", "의사였어요.", "시간이 없었어요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="kecha">어제</span> 저는 <span class="cn-word" data-tr="maktab">학교</span>에 <span class="cn-word" data-pos="verb" data-tr="bordim">갔어요</span>.</p>

<p><span class="cn-word" data-tr="ertalab">아침</span>에 <span class="cn-word" data-tr="uy">집</span>에서 <span class="cn-word" data-tr="ovqat">밥</span>을 <span class="cn-word" data-pos="verb" data-tr="yedim">먹었어요</span>. <span class="cn-word" data-tr="sut">우유</span>도 <span class="cn-word" data-pos="verb" data-tr="ichdim">마셨어요</span>.</p>

<p>학교에서 <span class="cn-word" data-tr="koreys tili">한국어</span>를 <span class="cn-word" data-pos="verb" data-tr="oʻrgandim">공부했어요</span>. 한국어가 <span class="cn-word" data-pos="adj" data-tr="qiziqarli edi">재미있었어요</span>.</p>

<p><span class="cn-word" data-tr="tush payti">점심</span>에 <span class="cn-word" data-tr="doʻst">친구</span>를 <span class="cn-word" data-pos="verb" data-tr="uchratdim">만났어요</span>. 우리는 <span class="cn-word" data-tr="birga">같이</span> 밥을 먹었어요.</p>

<p><span class="cn-word" data-tr="kechqurun">저녁</span>에 집에 <span class="cn-word" data-pos="verb" data-tr="keldim">왔어요</span>. 집에서 <span class="cn-word" data-tr="kitob">책</span>을 <span class="cn-word" data-pos="verb" data-tr="oʻqidim">읽었어요</span>. <span class="cn-word" data-tr="televizor">텔레비전</span>도 <span class="cn-word" data-pos="verb" data-tr="koʻrdim">봤어요</span>.</p>

<p><strong>지영:</strong> <span class="cn-word" data-tr="Sherbek">셰르벡</span> 씨, 어제 <span class="cn-word" data-tr="nima">무엇</span>을 <span class="cn-word" data-pos="verb" data-tr="qildingiz">했어요</span>?</p>

<p><strong>셰르벡:</strong> 저는 어제 친구하고 학교에 갔어요. 학교에서 한국어를 <span class="cn-word" data-pos="verb" data-tr="oʻrgandim">배웠어요</span>.</p>

<p><strong>지영:</strong> 어제 <span class="cn-word" data-tr="vaqt">시간</span>이 <span class="cn-word" data-tr="bor edi">있었어요</span>?</p>

<p><strong>셰르벡:</strong> <span class="cn-word" data-tr="ertalabdan">아침부터</span> <span class="cn-word" data-tr="kechgacha">저녁까지</span> 학교에 있었어요. 시간이 <span class="cn-word" data-tr="yoʻq edi">없었어요</span>. 지영 씨는 어제 무엇을 했어요?</p>

<p><strong>지영:</strong> 저는 집에 있었어요. 책만 읽었어요. 어제는 <span class="cn-word" data-pos="adj" data-tr="yaxshi edi">좋았어요</span>.</p>''',
        "questions": [
            {
                "text": "“봤어요” qanday yasalgan?",
                "choices": [
                    "보다 → 봐요 → 요 olinadi → ㅆ어요 qoʻshiladi",
                    "보다 → 보았어요 → qisqaradi",
                    "보다 + 았습니다",
                    "보다 + 이었어요",
                ],
                "answer": 0,
                "explanation": "Eng ishonchli yoʻl — avval hozirgi shaklni yasash. "
                               "보다 → 봐요 (ㅗ+ㅏ=ㅘ), keyin 요 ni olib ㅆ어요 qoʻshamiz → "
                               "봤어요. Qisqargan shakllarga alohida qoida kerak emas.",
            },
            {
                "text": "Nega Sherbekning kecha vaqti yoʻq edi?",
                "choices": [
                    "Ertalabdan kechgacha maktabda edi",
                    "Uyda kitob oʻqidi",
                    "Doʻsti bilan ovqat yedi",
                    "Televizor koʻrdi",
                ],
                "answer": 0,
                "explanation": "“아침부터 저녁까지 학교에 있었어요. 시간이 없었어요” — "
                               "부터…까지 (PK-16) oraliqni koʻrsatadi, 없었어요 esa 없다 ning "
                               "oʻtgan shakli.",
            },
            {
                "text": "Oʻtgan zamonda rasmiy shakl nega har doim 습니다 boʻladi?",
                "choices": [
                    "Oʻtgan oʻzak oxirida ㅆ 받침i turadi",
                    "Chunki oʻtgan zamon har doim rasmiy",
                    "Chunki 습니다 qisqaroq",
                    "Chunki ㅂ니다 faqat sifatlar uchun",
                ],
                "answer": 0,
                "explanation": "갔, 먹었, 했 — hammasi ㅆ bilan tugaydi, ya'ni 받침li. "
                               "PK-19 qoidasi boʻyicha 받침li oʻzak har doim 습니다 oladi: "
                               "갔습니다, 먹었습니다, 했습니다.",
            },
        ],
    },
]
