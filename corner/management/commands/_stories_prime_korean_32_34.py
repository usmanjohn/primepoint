# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-32 … PK-34 (notoʻgʻri feʼllar, 고, 지만).

Kumulyativ qoida: PK-34 gacha oʻrganilgan hamma narsa ochiq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_32_34.py --author=prime
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
        "title":   "날씨가 더워요",
        "summary": (
            "PK-32 matni. Afsona va Jiyong yozgi bogʻda — bir sahifada ㅂ, ㄷ va "
            "으 tuslanishining oʻnlab namunasi."
        ),
        "order":   32,
        "grammar": [
            {
                "pattern":  "ㅂ tuslanishi",
                "meaning":  "Oʻzak ㅂ bilan tugasa, unli oldida ㅂ → 우 boʻladi va "
                            "우 + 어요 = 워요. Faqat unli qoʻshimcha oldida; "
                            "덥습니다 da hech narsa oʻzgarmaydi.",
                "examples": ["오늘 날씨가 더워요.", "겨울은 아주 추워요.",
                             "습도가 높아서 힘들어요."],
            },
            {
                "pattern":  "ㄷ tuslanishi",
                "meaning":  "Oʻzak ㄷ bilan tugasa, unli oldida ㄷ → ㄹ: 듣다 → "
                            "들어요, 걷다 → 걸어요. 받다, 닫다, 믿다 esa oddiy "
                            "feʼllar.",
                "examples": ["음악을 들어요.", "우리 천천히 걸어요."],
            },
            {
                "pattern":  "으 tuslanishi",
                "meaning":  "Oʻzakdagi 으 아/어 oldida tushib qoladi. Oldingi unli "
                            "ㅏ/ㅗ boʻlsa 아, boshqa boʻlsa 어 qoʻshiladi: 아프다 → "
                            "아파요, 예쁘다 → 예뻐요.",
                "examples": ["머리가 아파요.", "오늘은 아주 바빠요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Afsona">아프소나</span> 씨와 <span class="cn-word" data-tr="Jiyong (koreys ismi)">지영</span> 씨는 <span class="cn-word" data-tr="bogʻ">공원</span>에 <span class="cn-word" data-pos="verb" data-tr="bordi">갔어요</span>. <span class="cn-word" data-tr="bugun">오늘</span> <span class="cn-word" data-tr="havo, ob-havo">날씨</span>가 아주 <span class="cn-word" data-pos="adj" data-tr="issiq">더워요</span>.</p>

<p><strong>아프소나:</strong> 지영 씨, 저는 좀 <span class="cn-word" data-pos="adj" data-tr="qiynalyapman">힘들어요</span>. <span class="cn-word" data-tr="bosh">머리</span>가 <span class="cn-word" data-pos="adj" data-tr="ogʻriyapti">아파요</span>.</p>

<p><strong>지영:</strong> 그래요? 우리 <span class="cn-word" data-pos="adv" data-tr="sekin">천천히</span> <span class="cn-word" data-pos="verb" data-tr="yuramiz">걸어요</span>. <span class="cn-word" data-tr="ana u yerda">저기</span> <span class="cn-word" data-tr="daraxt tagida">나무 밑에</span> <span class="cn-word" data-tr="oʻtiring">앉으세요</span>.</p>

<p>아프소나 씨는 나무 밑에 <span class="cn-word" data-pos="verb" data-tr="oʻtirdi">앉았어요</span>. 그리고 <span class="cn-word" data-tr="musiqa">음악</span>을 <span class="cn-word" data-pos="verb" data-tr="tinglaydi">들어요</span>.</p>

<p><strong>지영:</strong> <span class="cn-word" data-tr="Koreya yozi">한국 여름</span>은 <span class="cn-word" data-pos="adv" data-tr="haqiqatan">정말</span> 더워요. <span class="cn-word" data-tr="qish">겨울</span>은 아주 <span class="cn-word" data-pos="adj" data-tr="sovuq">추워요</span>.</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-tr="Oʻzbekiston">우즈베키스탄</span>도 여름이 더워요. 하지만 <span class="cn-word" data-tr="bu yer">여기</span>는 <span class="cn-word" data-tr="namlik">습도</span>가 <span class="cn-word" data-pos="adj" data-tr="baland">높아요</span>. 그래서 더 힘들어요.</p>

<p><strong>지영:</strong> 네, <span class="cn-word" data-tr="toʻgʻri">맞아요</span>. <span class="cn-word" data-tr="ertaga">내일</span>은 안 더워요. <span class="cn-word" data-tr="xavotir olmang">걱정하지 마세요</span>. <span class="cn-word" data-tr="suv">물</span> <span class="cn-word" data-tr="iching">드세요</span>.</p>''',
        "questions": [
            {
                "text": "Nega matnda “더워요” deyilgan, “덥어요” emas?",
                "choices": [
                    "덥다 — ㅂ notoʻgʻri feʼli: ㅂ unli oldida 우 boʻladi",
                    "Chunki gap oʻtgan zamonda",
                    "Chunki 덥다 sifat emas, feʼl",
                    "Chunki oʻzakda 받침 yoʻq",
                ],
                "answer": 0,
                "explanation": "덥 → 더<b>우</b>, keyin 우 + 어요 = <b>워요</b>. "
                               "Xuddi shunday 춥다 → 추워요. Lekin undosh qoʻshimcha "
                               "oldida hech narsa oʻzgarmaydi: 덥<b>습니다</b>.",
            },
            {
                "text": "Afsonaning fikricha, Koreyadagi issiqni nima ogʻirlashtiradi?",
                "choices": [
                    "Namlik yuqoriligi",
                    "Shamol kuchliligi",
                    "Yozning uzunligi",
                    "Bogʻda daraxt yoʻqligi",
                ],
                "answer": 0,
                "explanation": "“여기는 <b>습도가 높아요</b>. 그래서 더 힘들어요” — "
                               "Oʻzbekistonda ham yoz issiq, lekin bu yerda namlik "
                               "baland.",
            },
            {
                "text": "Matndagi “들어요” qaysi feʼldan yasalgan?",
                "choices": [
                    "듣다 — ㄷ unli oldida ㄹ boʻlgan",
                    "들다 — hech narsa oʻzgarmagan",
                    "닫다 — oddiy tuslanish",
                    "돕다 — ㅂ tuslanishi",
                ],
                "answer": 0,
                "explanation": "<b>듣다</b> (eshitmoq) → 듣 + 어요, 받침 ㄷ unli "
                               "oldida <b>ㄹ</b> ga aylanadi → <b>들어요</b>. "
                               "Xuddi shunday 걷다 → 걸어요, u ham shu matnda bor.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "밥을 먹고 학교에 가요",
        "summary": (
            "PK-33 matni. Sherbekning bir kuni — 고 bilan bogʻlangan ketma-ket "
            "ishlar va sanashning farqi matn ichida koʻrinadi."
        ),
        "order":   33,
        "grammar": [
            {
                "pattern":  "동사 + 고 (ketma-ketlik)",
                "meaning":  "Bir ish tugaydi, keyin ikkinchisi boshlanadi — "
                            "oʻzbekchada “…ib”. Zamon faqat OXIRGI feʼlga "
                            "qoʻyiladi: 먹고 갔어요, 먹었고 갔어요 emas.",
                "examples": ["밥을 먹고 학교에 가요.", "숙제를 하고 집에 갔어요.",
                             "일어나고 세수를 해요."],
            },
            {
                "pattern":  "형용사 + 고 (sanash)",
                "meaning":  "Ikki mustaqil fakt — oʻzbekchada “va”. Egalar har xil "
                            "boʻlishi ham mumkin. Sifatlar bilan eng koʻp shu "
                            "maʼnoda uchraydi.",
                "examples": ["이 식당은 싸고 맛있어요.", "저는 학생이고 형은 선생님이에요."],
            },
            {
                "pattern":  "고 va notoʻgʻri feʼllar",
                "meaning":  "고 undosh bilan boshlanadi, shuning uchun PK-32 dagi "
                            "oʻzgarishlar bu yerda BOʻLMAYDI: 듣다 → 듣고, "
                            "덥다 → 덥고, 바쁘다 → 바쁘고.",
                "examples": ["노래를 듣고 단어를 배웠어요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Sherbek">셰르벡</span> 씨는 <span class="cn-word" data-tr="ertalab">아침</span> <span class="cn-word" data-tr="soat yettida">일곱 시에</span> <span class="cn-word" data-pos="verb" data-tr="turib">일어나고</span> <span class="cn-word" data-tr="yuzini yuvadi">세수를 해요</span>. 그리고 <span class="cn-word" data-tr="ovqat">밥</span>을 <span class="cn-word" data-pos="verb" data-tr="yeb">먹고</span> <span class="cn-word" data-tr="maktabga">학교에</span> 가요.</p>

<p><span class="cn-word" data-tr="maktabda">학교에서</span> 한국어를 <span class="cn-word" data-pos="verb" data-tr="oʻqib">공부하고</span> <span class="cn-word" data-tr="doʻstlarini">친구들을</span> <span class="cn-word" data-pos="verb" data-tr="uchratadi">만나요</span>.</p>

<p><strong>셰르벡:</strong> 아프소나 씨, 오늘 <span class="cn-word" data-tr="dars">수업</span>이 <span class="cn-word" data-tr="qanday edi">어땠어요</span>?</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-pos="adj" data-tr="qiziqarli edi">재미있었어요</span>. 우리는 <span class="cn-word" data-tr="qoʻshiq">노래</span>를 <span class="cn-word" data-pos="verb" data-tr="tinglab">듣고</span> <span class="cn-word" data-tr="yangi soʻzlar">새 단어</span>를 <span class="cn-word" data-pos="verb" data-tr="oʻrgandik">배웠어요</span>.</p>

<p><strong>셰르벡:</strong> 저는 <span class="cn-word" data-tr="tushdan keyin">오후</span>에 <span class="cn-word" data-tr="kutubxonaga">도서관에</span> <span class="cn-word" data-pos="verb" data-tr="borib">가고</span> <span class="cn-word" data-tr="uy vazifasi">숙제</span>를 <span class="cn-word" data-tr="qilaman">할 거예요</span>.</p>

<p><strong>아프소나:</strong> 저도 <span class="cn-word" data-pos="adv" data-tr="birga">같이</span> <span class="cn-word" data-tr="bormoqchiman">가고 싶어요</span>.</p>

<p><span class="cn-word" data-tr="ikki kishi">두 사람</span>은 도서관에서 숙제를 하고 집에 <span class="cn-word" data-pos="verb" data-tr="ketishdi">갔어요</span>. 셰르벡 씨는 <span class="cn-word" data-tr="kechki ovqat">저녁</span>을 먹고 한국 <span class="cn-word" data-tr="serial">드라마</span>를 <span class="cn-word" data-pos="verb" data-tr="koʻradi">봐요</span>. 그리고 <span class="cn-word" data-tr="soat oʻn ikkida">열두 시에</span> <span class="cn-word" data-pos="verb" data-tr="uxlaydi">자요</span>.</p>''',
        "questions": [
            {
                "text": "Nega matnda “숙제를 하고 집에 갔어요” deyilgan, "
                        "“숙제를 했고 집에 갔어요” emas?",
                "choices": [
                    "Ketma-ketlikda zamon faqat oxirgi feʼlga qoʻyiladi",
                    "하다 feʼli oʻtgan zamonga kirmaydi",
                    "Chunki ikki ega har xil",
                    "Chunki 고 dan keyin oʻtgan zamon kelmaydi",
                ],
                "answer": 0,
                "explanation": "Bitta odam ketma-ket ikki ish qilgan — bu "
                               "<b>ketma-ketlik</b>. Zamon faqat oxirida: "
                               "<b>하고 갔어요</b>. Oʻzbekchada ham “vazifani "
                               "<b>qilib</b> uyga <b>ketdim</b>” deysiz.",
            },
            {
                "text": "Matndagi “듣고” nega “들고” emas?",
                "choices": [
                    "고 undosh bilan boshlanadi — ㄷ tuslanishi ishga tushmaydi",
                    "듣다 aslida notoʻgʻri feʼl emas",
                    "고 dan oldin har doim asl oʻzak turadi va bu istisno",
                    "Chunki gap oʻtgan zamonda",
                ],
                "answer": 0,
                "explanation": "ㄷ → ㄹ oʻzgarishi faqat <b>unli</b> qoʻshimcha "
                               "oldida boʻladi (들어요, 들으세요). 고 esa undosh "
                               "bilan boshlanadi, shuning uchun <b>듣고</b>.",
            },
            {
                "text": "Afsona nima demoqchi: “저도 같이 가고 싶어요”?",
                "choices": [
                    "Men ham birga bormoqchiman",
                    "Men ham birga bordim",
                    "Men birga bora olmayman",
                    "Siz ham birga boring",
                ],
                "answer": 0,
                "explanation": "Bu yerdagi 고 — bogʻlovchi emas, "
                               "<b>고 싶다</b> (xohish, PK-28) qolipining bir "
                               "qismi. Ikkalasi bir xil koʻrinadi, lekin "
                               "vazifasi boshqa: 가고 싶어요 = “bormoqchiman”.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "한국어는 어렵지만 재미있어요",
        "summary": (
            "PK-34 matni. Afsona va Minsu til oʻrganish haqida gaplashadi — har "
            "bir gapda 지만 kutilmagan tomonni ochadi."
        ),
        "order":   34,
        "grammar": [
            {
                "pattern":  "동사/형용사 + 지만",
                "meaning":  "“…lekin”. Oʻzakka toʻgʻridan-toʻgʻri yopishadi — 으 "
                            "yoʻq, 받침 ayrisi yoʻq. Urgʻu ikkinchi qismga tushadi.",
                "examples": ["한국어는 어렵지만 재미있어요.",
                             "문법은 쉽지만 발음이 어려워요."],
            },
            {
                "pattern":  "았/었 + 지만",
                "meaning":  "고 dan farqli oʻlaroq, zamon 지만 dan OLDIN turadi, "
                            "chunki ikki tomon ikki mustaqil fikr: 갔지만, "
                            "배웠지만, 바빴지만.",
                "examples": ["단어를 많이 외웠지만 자주 잊어요.",
                             "오늘은 바빴지만 내일은 시간이 있어요."],
            },
            {
                "pattern":  "명사 + 이지만 / 지만",
                "meaning":  "Ot bilan 받침 ga qarab: 받침 bor → 이지만 (학생이지만), "
                            "받침 yoʻq → 지만 (친구지만).",
                "examples": ["저는 학생이지만 우즈베크어를 가르칠 수 있어요."],
            },
        ],
        "body": '''<p>아프소나 씨는 한국어를 <span class="cn-word" data-tr="olti oy">육 개월</span> <span class="cn-word" data-pos="verb" data-tr="oʻrgandi">배웠어요</span>. 오늘 <span class="cn-word" data-tr="Minsu (koreys ismi)">민수</span> 씨가 <span class="cn-word" data-pos="verb" data-tr="soʻradi">물었어요</span>.</p>

<p><strong>민수:</strong> 한국어 <span class="cn-word" data-tr="qanday">어때요</span>?</p>

<p><strong>아프소나:</strong> 한국어는 <span class="cn-word" data-pos="adj" data-tr="qiyin, lekin">어렵지만</span> 아주 <span class="cn-word" data-pos="adj" data-tr="qiziqarli">재미있어요</span>.</p>

<p><strong>민수:</strong> <span class="cn-word" data-tr="nima">뭐</span>가 어려워요?</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-tr="grammatika">문법</span>은 <span class="cn-word" data-pos="adj" data-tr="oson, lekin">쉽지만</span> <span class="cn-word" data-tr="talaffuz">발음</span>이 <span class="cn-word" data-pos="adj" data-tr="qiyin">어려워요</span>. 그리고 <span class="cn-word" data-tr="soʻzlarni">단어를</span> <span class="cn-word" data-pos="adv" data-tr="koʻp">많이</span> <span class="cn-word" data-pos="verb" data-tr="yodladim, lekin">외웠지만</span> <span class="cn-word" data-pos="adv" data-tr="tez-tez">자주</span> <span class="cn-word" data-pos="verb" data-tr="unutaman">잊어요</span>.</p>

<p><strong>민수:</strong> 저도 <span class="cn-word" data-tr="oʻzbek tilini">우즈베크어를</span> <span class="cn-word" data-pos="verb" data-tr="oʻrgandim, lekin">배웠지만</span> <span class="cn-word" data-tr="yaxshi eplay olmayman">잘 못해요</span>.</p>

<p><strong>아프소나:</strong> 우리 <span class="cn-word" data-pos="adv" data-tr="birga">같이</span> <span class="cn-word" data-tr="oʻqiylik">공부해요</span>! 저는 <span class="cn-word" data-tr="talaba, lekin">학생이지만</span> 우즈베크어를 <span class="cn-word" data-tr="oʻrgata olaman">가르칠 수 있어요</span>.</p>

<p><strong>민수:</strong> <span class="cn-word" data-tr="yaxshi, kelishdik">좋아요</span>. 오늘은 <span class="cn-word" data-pos="adj" data-tr="band edim, lekin">바빴지만</span> 내일은 <span class="cn-word" data-tr="vaqt">시간</span>이 있어요.</p>''',
        "questions": [
            {
                "text": "Afsona koreys tili haqida oxir-oqibat qanday fikrda?",
                "choices": [
                    "Qiyin boʻlsa ham, unga yoqadi",
                    "Qiziqarli, lekin tashlamoqchi",
                    "Oson va zerikarli",
                    "Umuman fikri yoʻq",
                ],
                "answer": 0,
                "explanation": "“어렵지만 재미있어요” — <b>지만</b> urgʻuni "
                               "<b>ikkinchi</b> qismga beradi. Tartib almashsa "
                               "(재미있지만 어려워요) fikr ham oʻzgarardi — "
                               "u shikoyatga aylanardi.",
            },
            {
                "text": "Nega “배웠지만” deyilgan, “배우지만” emas?",
                "choices": [
                    "지만 da zamon qoʻshimchadan oldin turadi",
                    "배우다 notoʻgʻri feʼl",
                    "Chunki ikki ega har xil",
                    "Chunki gapda 그리고 bor",
                ],
                "answer": 0,
                "explanation": "Bu 고 dan eng muhim farq. 고 da zamon faqat "
                               "oxirgi feʼlda (먹고 잤어요), 지만 da esa har bir "
                               "tomon oʻz zamonini oladi: <b>배웠지만</b>, "
                               "<b>바빴지만</b>.",
            },
            {
                "text": "“저는 학생이지만…” — nega 학생 dan keyin 이 qoʻshilgan?",
                "choices": [
                    "학생 da 받침 bor, shuning uchun 이지만",
                    "Chunki 학생 — kasb nomi",
                    "Chunki gap inkor",
                    "Chunki 지만 har doim 이 bilan keladi",
                ],
                "answer": 0,
                "explanation": "Ot bilan 이다 ning odatdagi ayrisi: 받침 bor → "
                               "<b>이지만</b> (학생이지만), 받침 yoʻq → "
                               "<b>지만</b> (친구지만).",
            },
        ],
    },
]
