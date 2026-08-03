# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-41 … PK-43 (아/어 보다, 고 있다/아/어 있다, 동사 + 는).

Kumulyativ qoida: PK-43 gacha oʻrganilgan hamma narsa ochiq.
PK-41 va PK-42 matnlarida 는 aniqlovchisi hali YOʻQ (u PK-43 da ochiladi).
Oʻtgan/kelasi aniqlovchi (PK-44), sifat aniqlovchisi (PK-45), otlashtirish
(PK-46) va 르/ㅅ/ㅎ notoʻgʻri feʼllar (PK-47) hali yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_41_43.py --author=prime
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
        "title":   "한국 음식을 먹어 보세요",
        "summary": (
            "PK-41 matni. Sujin Sherbekka koreys taomlarini tavsiya qiladi — "
            "butun suhbat 아/어 보세요 va 아/어 봤어요 ustiga qurilgan."
        ),
        "order":   41,
        "grammar": [
            {
                "pattern":  "동사 + 아/어 보세요",
                "meaning":  "“…ib koʻring” — yumshoq tavsiya. 먹으세요 (“yeng”) "
                            "dan koʻra muloyimroq: “bir sinab koʻring”. "
                            "한번 bilan koʻp yuradi.",
                "examples": ["이 김밥을 먹어 보세요.",
                             "한번 들어 보세요.",
                             "떡볶이도 먹어 보세요."],
            },
            {
                "pattern":  "동사 + 아/어 봤어요",
                "meaning":  "“…ib koʻrganman” — hayotdagi tajriba. Inkori "
                            "안 …아/어 봤어요 (bunday qilmaganman) yoki "
                            "못 …아/어 봤어요 (qila olmaganman).",
                "examples": ["한국 음식을 먹어 봤어요?",
                             "저는 김치를 안 먹어 봤어요.",
                             "불고기는 먹어 봤어요."],
            },
            {
                "pattern":  "동사 + 아/어 보고 싶어요",
                "meaning":  "“…ib koʻrgim keladi” — 아/어 보다 va 고 싶다 "
                            "birlashgan shakli.",
                "examples": ["한국에 가 보고 싶어요.", "떡볶이를 먹어 보고 싶어요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Sujin">수진</span> 씨와 <span class="cn-word" data-tr="Sherbek">셰르벡</span> 씨가 <span class="cn-word" data-tr="koreys oshxonasida">한국 식당</span>에 갔어요.</p>

<p><strong>수진:</strong> 셰르벡 씨, 한국 <span class="cn-word" data-tr="taom">음식</span>을 <span class="cn-word" data-pos="verb" data-tr="yeb koʻrganmisiz">먹어 봤어요</span>?</p>

<p><strong>셰르벡:</strong> <span class="cn-word" data-tr="bulgogi">불고기</span>는 먹어 봤어요. 하지만 <span class="cn-word" data-tr="tteokbokki">떡볶이</span>는 <span class="cn-word" data-pos="verb" data-tr="yeb koʻrmaganman">안 먹어 봤어요</span>.</p>

<p><strong>수진:</strong> 그럼 오늘 <span class="cn-word" data-pos="adv" data-tr="bir marta">한번</span> <span class="cn-word" data-pos="verb" data-tr="yeb koʻring">먹어 보세요</span>. 떡볶이는 <span class="cn-word" data-pos="adj" data-tr="achchiq">매워요</span>. 하지만 <span class="cn-word" data-pos="adj" data-tr="juda mazali">아주 맛있어요</span>.</p>

<p><strong>셰르벡:</strong> 매워요? 그럼 <span class="cn-word" data-pos="adv" data-tr="ozgina">조금</span>만 <span class="cn-word" data-pos="verb" data-tr="yeb koʻraman">먹어 볼 거예요</span>.</p>

<p>셰르벡 씨가 떡볶이를 조금 먹었어요.</p>

<p><strong>셰르벡:</strong> <span class="cn-word" data-pos="adj" data-tr="mazali">맛있어요</span>! 매워요. 하지만 <span class="cn-word" data-pos="adv" data-tr="yana">또</span> 먹고 싶어요.</p>

<p><strong>수진:</strong> 그럼 <span class="cn-word" data-tr="keyingi safar">다음에</span> <span class="cn-word" data-tr="kimchi jjigae">김치찌개</span>도 먹어 보세요. 그리고 한국 <span class="cn-word" data-tr="qoʻshiq">노래</span>도 <span class="cn-word" data-pos="verb" data-tr="tinglab koʻring">들어 보세요</span>.</p>

<p><strong>셰르벡:</strong> 네! 저는 한국에도 <span class="cn-word" data-pos="verb" data-tr="borib koʻrgim keladi">가 보고 싶어요</span>.</p>''',
        "questions": [
            {
                "text": "Sherbek ilgari qaysi taomni yeb koʻrgan?",
                "choices": [
                    "Bulgogini",
                    "Tteokbokkini",
                    "Kimchi jjigaeni",
                    "Hech qaysisini",
                ],
                "answer": 0,
                "explanation": "“<b>불고기</b>는 먹어 봤어요. 하지만 떡볶이는 "
                               "<b>안</b> 먹어 봤어요” — bulgogini yeb koʻrgan, "
                               "tteokbokkini esa yoʻq.",
            },
            {
                "text": "Sherbek tteokbokkini yegandan keyin nima dedi?",
                "choices": [
                    "Juda achchiq, boshqa yemayman",
                    "Mazali emas ekan",
                    "Achchiq, lekin yana yegisi keladi",
                    "Umuman yemadi",
                ],
                "answer": 2,
                "explanation": "“매워요. 하지만 <b>또 먹고 싶어요</b>” — achchiq, "
                               "lekin yana yegisi kelyapti.",
            },
            {
                "text": "Nega Sujin “먹으세요” emas, “먹어 보세요” deydi?",
                "choices": [
                    "아/어 보세요 yumshoqroq — “bir sinab koʻring” degani",
                    "먹으세요 notoʻgʻri shakl",
                    "Chunki Sherbek undan katta",
                    "Chunki taom achchiq",
                ],
                "answer": 0,
                "explanation": "먹으세요 — “yeng” degan koʻrsatma. <b>먹어 "
                               "보세요</b> — “bir sinab koʻring, yoqmasa "
                               "qoʻying”. Notanish taomni tavsiya qilganda "
                               "koreyslar deyarli har doim shuni tanlaydi.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "지금 뭐 하고 있어요?",
        "summary": (
            "PK-42 matni. Dilnoza telefon qiladi va uydagilar nima qilayotganini "
            "aytadi — 고 있다 va 아/어 있다 yonma-yon turadi."
        ),
        "order":   42,
        "grammar": [
            {
                "pattern":  "동사 + 고 있다",
                "meaning":  "“…yapman” — harakat hozir davom etyapti. Oʻzak "
                            "oʻzgarmaydi, chunki 고 undosh bilan boshlanadi: "
                            "듣고 있어요.",
                "examples": ["저는 지금 숙제를 하고 있어요.",
                             "동생은 음악을 듣고 있어요.",
                             "어머니는 요리하고 있어요."],
            },
            {
                "pattern":  "동사 + 아/어 있다",
                "meaning":  "“…ib turibdi” — harakat tugagan, natijasi qolgan. "
                            "Faqat toʻldiruvchi olmaydigan feʼllar bilan: "
                            "앉다, 서다, 눕다, 오다, 남다.",
                "examples": ["아버지는 소파에 앉아 있어요.",
                             "동생은 침대에 누워 있어요.",
                             "친구가 벌써 와 있어요."],
            },
            {
                "pattern":  "고 있다 va 아/어 있다 farqi",
                "meaning":  "앉고 있어요 — hozir oʻtirayotgan payt "
                            "(“oʻtiryapti”). 앉아 있어요 — allaqachon oʻtirgan "
                            "(“oʻtiribdi”). Oʻzbekchadagi “-yapti / -ibdi” "
                            "farqining aynan oʻzi.",
                "examples": ["앉고 있어요 ≠ 앉아 있어요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Dilnoza">딜노자</span> 씨와 <span class="cn-word" data-tr="Hana">하나</span> 씨가 <span class="cn-word" data-tr="telefonda">전화로</span> <span class="cn-word" data-pos="verb" data-tr="gaplashyapti">이야기하고 있어요</span>.</p>

<p><strong>하나:</strong> 딜노자 씨, 지금 뭐 <span class="cn-word" data-pos="verb" data-tr="qilyapsiz">하고 있어요</span>?</p>

<p><strong>딜노자:</strong> 저는 지금 <span class="cn-word" data-tr="uy vazifasi">숙제</span>를 하고 있어요. <span class="cn-word" data-tr="uyda">집에</span> 있어요.</p>

<p><strong>하나:</strong> <span class="cn-word" data-tr="oila aʼzolari">가족</span>도 <span class="cn-word" data-tr="hammasi">모두</span> 집에 있어요?</p>

<p><strong>딜노자:</strong> 네. <span class="cn-word" data-tr="otam">아버지</span>는 <span class="cn-word" data-tr="divanda">소파에</span> <span class="cn-word" data-pos="verb" data-tr="oʻtiribdi">앉아 있어요</span>. <span class="cn-word" data-tr="gazeta">신문</span>을 <span class="cn-word" data-pos="verb" data-tr="oʻqiyapti">읽고 있어요</span>.</p>

<p><strong>하나:</strong> <span class="cn-word" data-tr="onangiz">어머니</span>는 뭐 하고 있어요?</p>

<p><strong>딜노자:</strong> <span class="cn-word" data-tr="oshxonada">부엌에서</span> <span class="cn-word" data-pos="verb" data-tr="ovqat pishiryapti">요리하고 있어요</span>. <span class="cn-word" data-tr="ukam">동생</span>은 <span class="cn-word" data-tr="karavotda">침대에</span> <span class="cn-word" data-pos="verb" data-tr="yotibdi">누워 있어요</span>. 음악을 <span class="cn-word" data-pos="verb" data-tr="tinglayapti">듣고 있어요</span>.</p>

<p><strong>하나:</strong> <span class="cn-word" data-pos="adj" data-tr="tinch">조용해요</span>?</p>

<p><strong>딜노자:</strong> 아니요! 동생 음악이 <span class="cn-word" data-pos="adj" data-tr="baland">시끄러워요</span>. 그래서 저는 <span class="cn-word" data-pos="verb" data-tr="diqqatimni jamlay olmayapman">집중할 수 없어요</span>.</p>

<p><strong>하나:</strong> 그럼 도서관에 <span class="cn-word" data-pos="verb" data-tr="keling">오세요</span>. 저는 <span class="cn-word" data-pos="adv" data-tr="allaqachon">벌써</span> 도서관에 <span class="cn-word" data-pos="verb" data-tr="kelib boʻldim">와 있어요</span>.</p>

<p><strong>딜노자:</strong> 좋아요! 지금 <span class="cn-word" data-pos="verb" data-tr="ketyapman">가고 있어요</span>.</p>''',
        "questions": [
            {
                "text": "Dilnozaning otasi nima qilyapti?",
                "choices": [
                    "Ovqat pishiryapti",
                    "Divanda oʻtirib gazeta oʻqiyapti",
                    "Karavotda yotibdi",
                    "Kutubxonada",
                ],
                "answer": 1,
                "explanation": "“아버지는 소파에 <b>앉아 있어요</b>. 신문을 "
                               "<b>읽고 있어요</b>” — oʻtirgan holatda (아/어 "
                               "있다) va oʻqish harakati davom etyapti (고 있다).",
            },
            {
                "text": "Hana qayerda?",
                "choices": [
                    "Uyda",
                    "Oshxonada",
                    "Yoʻlda, kutubxonaga ketyapti",
                    "Kutubxonada — allaqachon kelib boʻlgan",
                ],
                "answer": 3,
                "explanation": "“저는 벌써 도서관에 <b>와 있어요</b>” — kelish "
                               "harakati tugagan, natijasi: u shu yerda. "
                               "Dilnoza esa hali yoʻlda — 가고 있어요.",
            },
            {
                "text": "Nega “누워 있어요” deyilgan, “눕고 있어요” emas?",
                "choices": [
                    "Chunki ukasi allaqachon yotgan holatda",
                    "Chunki 눕다 notoʻgʻri feʼl",
                    "Chunki gap oʻtgan zamonda",
                    "Ikkalasi ham bir xil",
                ],
                "answer": 0,
                "explanation": "눕고 있어요 “hozir yotayotgan payt” degani. "
                               "Ukasi esa allaqachon yotibdi — bu <b>holat</b>, "
                               "shuning uchun 아/어 있다.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "제가 자주 가는 카페",
        "summary": (
            "PK-43 matni. Bekzod oʻzi tez-tez boradigan kafe haqida gapiradi — "
            "har bir jumlada 는 aniqlovchisi ishlaydi."
        ),
        "order":   43,
        "grammar": [
            {
                "pattern":  "동사 + 는 + 명사",
                "meaning":  "Hozirgi zamon aniqlovchisi: “…adigan ot”. Oʻzakka "
                            "shundoq qoʻshiladi — 는 undosh bilan boshlangani "
                            "uchun ayri ham, notoʻgʻri oʻzgarish ham yoʻq.",
                "examples": ["제가 자주 가는 카페",
                             "한국어를 공부하는 학생",
                             "매일 신문을 읽는 사람"],
            },
            {
                "pattern":  "ㄹ oʻzak + 는",
                "meaning":  "ㄹ bilan tugagan oʻzak ㄴ tovushi oldida ㄹ ni "
                            "yoʻqotadi: 살다 → 사는, 알다 → 아는, 만들다 → 만드는.",
                "examples": ["학교 앞에 사는 친구", "제가 아는 사람",
                             "그 카페에서 만드는 커피"],
            },
            {
                "pattern":  "있다 / 없다 → 있는 / 없는",
                "meaning":  "재미있다, 맛있다 ichida 있다 — feʼl bor, shuning "
                            "uchun ular 는 oladi. Haqiqiy sifatlar boshqa shakl "
                            "oladi (PK-45).",
                "examples": ["재미있는 책", "맛있는 케이크", "재미없는 영화"],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Bekzod">베크조드</span> 씨와 <span class="cn-word" data-tr="Minsu">민수</span> 씨가 <span class="cn-word" data-pos="verb" data-tr="gaplashyapti">이야기하고 있어요</span>.</p>

<p><strong>베크조드:</strong> 민수 씨, <span class="cn-word" data-tr="men tez-tez boradigan">제가 자주 가는</span> <span class="cn-word" data-tr="kafe">카페</span>가 학교 <span class="cn-word" data-tr="oldida">앞에</span> 있어요.</p>

<p><strong>민수:</strong> 그 카페가 좋아요?</p>

<p><strong>베크조드:</strong> <span class="cn-word" data-pos="adj" data-tr="kichkina">작아요</span>. 하지만 그 카페에서 <span class="cn-word" data-tr="tayyorlanadigan">만드는</span> <span class="cn-word" data-tr="qahva">커피</span>는 <span class="cn-word" data-tr="mazali">맛있는</span> 커피예요. <span class="cn-word" data-tr="tort">케이크</span>도 <span class="cn-word" data-pos="adj" data-tr="mazali">맛있어요</span>.</p>

<p><strong>민수:</strong> <span class="cn-word" data-tr="odamlar">사람</span>이 <span class="cn-word" data-pos="adj" data-tr="koʻpmi">많아요</span>?</p>

<p><strong>베크조드:</strong> <span class="cn-word" data-tr="ertalab">아침</span>에는 <span class="cn-word" data-tr="ishga boradigan">회사에 가는</span> 사람이 많아요. <span class="cn-word" data-tr="tushdan keyin">오후</span>에는 <span class="cn-word" data-tr="dars qiladigan">공부하는</span> <span class="cn-word" data-tr="talabalar">학생</span>이 많아요. 저도 거기에서 공부해요.</p>

<p><strong>민수:</strong> <span class="cn-word" data-pos="adj" data-tr="tinch">조용해요</span>?</p>

<p><strong>베크조드:</strong> 네. 그리고 거기에서 <span class="cn-word" data-tr="qoʻyiladigan">나오는</span> 음악도 좋아요. <span class="cn-word" data-tr="men taniydigan">제가 아는</span> 노래가 자주 나와요.</p>

<p><strong>민수:</strong> <span class="cn-word" data-pos="adj" data-tr="qiziqarli">재미있는</span> <span class="cn-word" data-tr="joy">곳</span>이에요. <span class="cn-word" data-tr="keyingi safar">다음에</span> 같이 <span class="cn-word" data-pos="verb" data-tr="boraylik">가요</span>.</p>

<p><strong>베크조드:</strong> 좋아요! 학교 앞에 <span class="cn-word" data-tr="yashaydigan">사는</span> 아프소나 씨도 같이 가요.</p>''',
        "questions": [
            {
                "text": "Kafega ertalab kimlar koʻp keladi?",
                "choices": [
                    "Dars qiladigan talabalar",
                    "Ishga boradigan odamlar",
                    "Qoʻshiq tinglaydigan odamlar",
                    "Hech kim kelmaydi",
                ],
                "answer": 1,
                "explanation": "“아침에는 <b>회사에 가는</b> 사람이 많아요” — "
                               "ertalab ishga boradiganlar. Talabalar esa "
                               "tushdan keyin: 오후에는 공부하는 학생이 많아요.",
            },
            {
                "text": "Nega matnda “만드는 커피” deyilgan, “만들는 커피” emas?",
                "choices": [
                    "ㄹ oʻzak ㄴ oldida ㄹ ni yoʻqotadi",
                    "만들다 notoʻgʻri feʼl",
                    "Chunki 커피 unli bilan tugaydi",
                    "Ikkalasi ham toʻgʻri",
                ],
                "answer": 0,
                "explanation": "만들 + 는 → <b>만드는</b>. Xuddi shu qoida "
                               "살다 → 사는, 알다 → 아는 da ham ishlaydi — va "
                               "PK-38 dagi 만든 후에 da ham.",
            },
            {
                "text": "“재미있는 곳” — nega 재미있은 emas?",
                "choices": [
                    "Chunki 재미있다 ichida 있다 — feʼl bor",
                    "Chunki 곳 qisqa soʻz",
                    "Chunki gap hozirgi zamonda",
                    "Chunki 재미있다 notoʻgʻri feʼl",
                ],
                "answer": 0,
                "explanation": "재미있다, 맛있다, 멋있다 — ichida <b>있다</b> "
                               "boʻlgani uchun feʼllar qatorida turadi va "
                               "<b>는</b> oladi. Haqiqiy sifatlar boshqa shakl "
                               "oladi (PK-45).",
            },
        ],
    },
]
