# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-38 … PK-40 (기 전에/(으)ㄴ 후에, (으)면서, (으)려고 하다).

Kumulyativ qoida: PK-40 gacha oʻrganilgan hamma narsa ochiq.
Aniqlovchi shakllar (PK-43…45), otlashtirish (PK-46), 르/ㅅ/ㅎ notoʻgʻri feʼllar
(PK-47), 고 있다 (PK-42) va 아/어 보다 (PK-41) hali yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_38_40.py --author=prime
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
        "title":   "자기 전에 무엇을 해요?",
        "summary": (
            "PK-38 matni. Minsu bilan Jasur kechqurungi odatlari haqida gaplashadi — "
            "butun suhbat 기 전에 va (으)ㄴ 후에 ustiga qurilgan."
        ),
        "order":   38,
        "grammar": [
            {
                "pattern":  "동사 + 기 전에",
                "meaning":  "“…dan oldin”. Feʼl oʻzagiga shundoq qoʻshiladi — "
                            "받침 ham, notoʻgʻri feʼl ham ahamiyatsiz, chunki "
                            "기 undosh bilan boshlanadi.",
                "examples": ["자기 전에 한국어를 공부해요.",
                             "운동하기 전에 물을 마셔요.",
                             "밥을 먹기 전에 손을 씻어요."],
            },
            {
                "pattern":  "동사 + (으)ㄴ 후에 / (으)ㄴ 다음에",
                "meaning":  "“…dan keyin”. 받침 yoʻq → ㄴ 후에, 받침 bor → 은 후에. "
                            "후에 = 다음에 = 뒤에 — uchalasi bir xil.",
                "examples": ["저녁을 먹은 후에 운동해요.",
                             "공부한 후에 음악을 들어요.",
                             "운동한 다음에 샤워해요."],
            },
            {
                "pattern":  "Ot + 전에 / 후에",
                "meaning":  "Feʼl emas, ot boʻlsa 기 kerak emas: 수업 전에, "
                            "운동 후에, 시험 전에.",
                "examples": ["운동 전에 물을 마셔요.", "수업 후에 친구를 만나요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Minsu">민수</span> 씨와 <span class="cn-word" data-tr="Jasur">자수르</span> 씨가 <span class="cn-word" data-tr="kechqurun">저녁</span>에 <span class="cn-word" data-pos="verb" data-tr="gaplashadi">이야기해요</span>.</p>

<p><strong>민수:</strong> 자수르 씨는 <span class="cn-word" data-tr="uxlashdan oldin">자기 전에</span> 뭐 해요?</p>

<p><strong>자수르:</strong> 저는 자기 전에 한국어를 <span class="cn-word" data-pos="verb" data-tr="oʻrganaman">공부해요</span>. <span class="cn-word" data-tr="oʻqiganimdan keyin">공부한 후에</span> 음악을 들어요. 민수 씨는 뭐 해요?</p>

<p><strong>민수:</strong> 저는 저녁을 <span class="cn-word" data-tr="yegandan keyin">먹은 후에</span> <span class="cn-word" data-pos="verb" data-tr="mashq qilaman">운동해요</span>.</p>

<p><strong>자수르:</strong> <span class="cn-word" data-tr="mashqdan oldin">운동 전에</span> 물을 마셔요?</p>

<p><strong>민수:</strong> 네. <span class="cn-word" data-tr="mashq qilishdan oldin">운동하기 전에</span> 물을 <span class="cn-word" data-pos="adv" data-tr="koʻp">많이</span> 마셔요. 그리고 <span class="cn-word" data-tr="mashq qilgandan keyin">운동한 다음에</span> <span class="cn-word" data-pos="verb" data-tr="dushga tushaman">샤워해요</span>.</p>

<p><strong>자수르:</strong> 샤워한 후에는 <span class="cn-word" data-pos="adv" data-tr="darrov">바로</span> 자요?</p>

<p><strong>민수:</strong> 아니요. 자기 전에 <span class="cn-word" data-tr="oʻn daqiqa">십 분</span> 책을 읽어요. 책을 <span class="cn-word" data-tr="oʻqiganimdan keyin">읽은 후에</span> 자요.</p>

<p><strong>자수르:</strong> 저도 자기 전에 책을 <span class="cn-word" data-pos="verb" data-tr="oʻqigim keladi">읽고 싶어요</span>. 하지만 저는 너무 <span class="cn-word" data-pos="adj" data-tr="charchaganim uchun">피곤해서</span> <span class="cn-word" data-tr="oʻqishdan oldin">읽기 전에</span> 자요.</p>

<p>민수 씨가 <span class="cn-word" data-pos="verb" data-tr="kuldi">웃었어요</span>.</p>''',
        "questions": [
            {
                "text": "Jasur uxlashdan oldin nima qiladi?",
                "choices": [
                    "Koreys tilini oʻrganadi",
                    "Mashq qiladi",
                    "Dushga tushadi",
                    "Kitob oʻqiydi",
                ],
                "answer": 0,
                "explanation": "“저는 자기 전에 한국어를 <b>공부해요</b>” — "
                               "koreys tilini oʻrganadi. Kitob oʻqishni xohlaydi, "
                               "lekin charchagani uchun oʻqishdan oldin uxlab qoladi.",
            },
            {
                "text": "Minsu mashq qilishdan oldin nima qiladi?",
                "choices": [
                    "Dushga tushadi",
                    "Kitob oʻqiydi",
                    "Koʻp suv ichadi",
                    "Musiqa tinglaydi",
                ],
                "answer": 2,
                "explanation": "“운동하기 전에 물을 <b>많이</b> 마셔요” — mashqdan "
                               "oldin koʻp suv ichadi. Dush esa mashqdan "
                               "<b>keyin</b>: 운동한 다음에 샤워해요.",
            },
            {
                "text": "Nega matnda “공부한 후에” deyilgan, “공부하기 후에” emas?",
                "choices": [
                    "후에 doim (으)ㄴ bilan yuradi, 기 bilan emas",
                    "Chunki gap oʻtgan zamonda",
                    "Chunki 공부하다 notoʻgʻri feʼl",
                    "Ikkalasi ham toʻgʻri",
                ],
                "answer": 0,
                "explanation": "Shakllar aralashmasligi kerak: <b>기 전에</b> "
                               "(oldin) va <b>(으)ㄴ 후에</b> (keyin). 하다 da "
                               "받침 yoʻq, shuning uchun 한 후에.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "음악을 들으면서 공부해요",
        "summary": (
            "PK-39 matni. Dilnoza va Sujin kutubxonada qanday oʻqishlarini "
            "solishtiradi — har bir javob (으)면서 bilan tuzilgan."
        ),
        "order":   39,
        "grammar": [
            {
                "pattern":  "동사 + (으)면서",
                "meaning":  "“…ib turib” — ikki ish ayni bir vaqtda. 받침 yoʻq → "
                            "면서, 받침 bor → 으면서. Ikki tomonning egasi bir xil "
                            "boʻlishi shart.",
                "examples": ["음악을 들으면서 공부해요.",
                             "커피를 마시면서 책을 읽어요.",
                             "걸으면서 단어를 외워요."],
            },
            {
                "pattern":  "(으)면서 va notoʻgʻri feʼllar",
                "meaning":  "(으) unli bilan boshlanadi, shuning uchun PK-32 dagi "
                            "oʻzgarishlar ishlaydi: 듣다 → 들으면서, 걷다 → "
                            "걸으면서, 쉽다 → 쉬우면서.",
                "examples": ["들으면서 공부해요.", "걸으면서 외워요."],
            },
            {
                "pattern":  "형용사 + (으)면서 — “ham …, ham …”",
                "meaning":  "Sifat bilan (으)면서 vaqtni emas, bir narsaning ikki "
                            "xususiyatini birlashtiradi.",
                "examples": ["이 방법은 쉬우면서 좋아요.", "그 식당은 싸면서 맛있어요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="kutubxonada">도서관에서</span> <span class="cn-word" data-tr="Dilnoza">딜노자</span> 씨가 <span class="cn-word" data-tr="Sujin">수진</span> 씨를 만났어요.</p>

<p><strong>수진:</strong> 딜노자 씨, 음악을 <span class="cn-word" data-pos="verb" data-tr="tinglab turib">들으면서</span> 공부해요?</p>

<p><strong>딜노자:</strong> 네. 저는 음악을 들으면서 공부해요. 음악이 <span class="cn-word" data-pos="adj" data-tr="tinch, sokin">조용해요</span>. 그래서 좋아요.</p>

<p><strong>수진:</strong> 저는 못 해요. 음악을 들으면서 공부하면 <span class="cn-word" data-pos="verb" data-tr="diqqatimni jamlay olmayman">집중할 수 없어요</span>.</p>

<p><strong>딜노자:</strong> 그럼 수진 씨는 <span class="cn-word" data-pos="adv" data-tr="qanday">어떻게</span> 공부해요?</p>

<p><strong>수진:</strong> 저는 커피를 <span class="cn-word" data-pos="verb" data-tr="ichib turib">마시면서</span> 책을 읽어요. 그리고 <span class="cn-word" data-pos="verb" data-tr="yurib turib">걸으면서</span> <span class="cn-word" data-tr="soʻzlarni">단어를</span> <span class="cn-word" data-pos="verb" data-tr="yodlayman">외워요</span>.</p>

<p><strong>딜노자:</strong> 걸으면서 외워요? <span class="cn-word" data-pos="adv" data-tr="haqiqatan">정말</span> 재미있어요!</p>

<p><strong>수진:</strong> 네. 걸으면서 외우면 <span class="cn-word" data-pos="adv" data-tr="yaxshi">잘</span> <span class="cn-word" data-pos="verb" data-tr="eslab qolaman">기억해요</span>. 이 <span class="cn-word" data-tr="usul">방법</span>은 <span class="cn-word" data-pos="adj" data-tr="ham oson">쉬우면서</span> 좋아요.</p>

<p><strong>딜노자:</strong> 저도 <span class="cn-word" data-tr="ertadan">내일부터</span> 걸으면서 단어를 외울 거예요.</p>

<p>두 사람은 <span class="cn-word" data-pos="verb" data-tr="kulib">웃으면서</span> 이야기했어요.</p>''',
        "questions": [
            {
                "text": "Dilnoza qanday dars qiladi?",
                "choices": [
                    "Yurib turib",
                    "Musiqa tinglab turib",
                    "Qahva ichib turib",
                    "Tinch joyda, musiqasiz",
                ],
                "answer": 1,
                "explanation": "“저는 음악을 <b>들으면서</b> 공부해요” — musiqa "
                               "tinglab dars qiladi. Sujin esa bunday qila olmaydi.",
            },
            {
                "text": "Sujin soʻzlarni qanday yodlaydi?",
                "choices": [
                    "Kitob oʻqib turib",
                    "Qahva ichib turib",
                    "Yurib turib",
                    "Musiqa tinglab turib",
                ],
                "answer": 2,
                "explanation": "“<b>걸으면서</b> 단어를 외워요” — yurib turib "
                               "yodlaydi, chunki shunday qilsa yaxshi eslab qoladi.",
            },
            {
                "text": "“이 방법은 쉬우면서 좋아요” gapida (으)면서 qaysi maʼnoda?",
                "choices": [
                    "Ham oson, ham yaxshi",
                    "Oson boʻlgandan keyin yaxshi boʻladi",
                    "Agar oson boʻlsa, yaxshi boʻladi",
                    "Oson boʻlgani uchun yaxshi",
                ],
                "answer": 0,
                "explanation": "Sifat bilan (으)면서 vaqtni emas, <b>ikki "
                               "xususiyatni</b> birlashtiradi — “ham …, ham …”. "
                               "(쉽다 → 쉬우면서, ㅂ notoʻgʻri feʼli.)",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "방학에 뭐 하려고 해요?",
        "summary": (
            "PK-40 matni. Hana bilan Bekzod taʼtil rejalari haqida gaplashadi — "
            "niyat, amalga oshmagan niyat va maqsad, hammasi (으)려고 bilan."
        ),
        "order":   40,
        "grammar": [
            {
                "pattern":  "동사 + (으)려고 하다",
                "meaning":  "“…moqchiman” — koʻngildagi niyat. 받침 yoʻq → 려고, "
                            "받침 bor → 으려고. (으)ㄹ 거예요 dan farqi: u qaror "
                            "qilingan reja, bu esa hali niyat.",
                "examples": ["한국에 가려고 해요.", "책을 읽으려고 해요.",
                             "부산에도 가려고 해요."],
            },
            {
                "pattern":  "동사 + (으)려고 했어요",
                "meaning":  "Niyat bor edi, lekin amalga oshmadi. Zamon 하다 ga "
                            "qoʻyiladi — 려고 ga emas.",
                "examples": ["작년에 부산에 가려고 했어요. 하지만 못 갔어요."],
            },
            {
                "pattern":  "동사 + (으)려고 (하다siz)",
                "meaning":  "Maqsad bogʻlovchisi: “…uchun”. Ega bir xil boʻlishi "
                            "kerak va keyingi qismda buyruq kelmaydi.",
                "examples": ["한국에 가려고 돈을 모았어요.",
                             "표를 사려고 인터넷을 봐요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="taʼtil">방학</span>이 <span class="cn-word" data-pos="adv" data-tr="tez orada">곧</span> <span class="cn-word" data-pos="verb" data-tr="boshlanadi">시작해요</span>. <span class="cn-word" data-tr="Hana">하나</span> 씨와 <span class="cn-word" data-tr="Bekzod">베크조드</span> 씨가 이야기해요.</p>

<p><strong>하나:</strong> 베크조드 씨, 방학에 뭐 <span class="cn-word" data-pos="verb" data-tr="qilmoqchisiz">하려고 해요</span>?</p>

<p><strong>베크조드:</strong> 저는 한국에 <span class="cn-word" data-pos="verb" data-tr="bormoqchiman">가려고 해요</span>. 한국에 <span class="cn-word" data-tr="borish uchun">가려고</span> <span class="cn-word" data-tr="pul">돈</span>을 <span class="cn-word" data-pos="verb" data-tr="yigʻdim">모았어요</span>.</p>

<p><strong>하나:</strong> <span class="cn-word" data-pos="adv" data-tr="rostdanmi">정말요</span>? 한국에서 뭐 하려고 해요?</p>

<p><strong>베크조드:</strong> <span class="cn-word" data-tr="Seulda">서울에서</span> 친구를 만나고 <span class="cn-word" data-tr="Pusanga ham">부산에도</span> 가려고 해요. 부산은 서울<span class="cn-word" data-tr="…dan koʻra">보다</span> <span class="cn-word" data-pos="adj" data-tr="issiq">따뜻해요</span>.</p>

<p><strong>하나:</strong> 좋아요. 저는 <span class="cn-word" data-tr="oʻtgan yili">작년</span>에 부산에 <span class="cn-word" data-pos="verb" data-tr="bormoqchi edim">가려고 했어요</span>. 하지만 시간이 없어서 못 갔어요.</p>

<p><strong>베크조드:</strong> 그럼 이번 방학에 <span class="cn-word" data-pos="adv" data-tr="birga">같이</span> 갈 수 있어요?</p>

<p><strong>하나:</strong> 네! 저도 가려고 해요. <span class="cn-word" data-tr="chipta">표</span>를 <span class="cn-word" data-tr="sotib olish uchun">사려고</span> 오늘 <span class="cn-word" data-tr="internetga">인터넷을</span> 봐요.</p>

<p><span class="cn-word" data-tr="tashqarida">밖</span>에 비가 <span class="cn-word" data-pos="verb" data-tr="yogʻay deb turibdi">오려고 해요</span>. 두 사람은 <span class="cn-word" data-tr="kafega">카페에</span> <span class="cn-word" data-pos="verb" data-tr="kirishdi">들어갔어요</span>.</p>''',
        "questions": [
            {
                "text": "Bekzod taʼtilda qayerga bormoqchi?",
                "choices": [
                    "Koreyaga",
                    "Faqat Seulga",
                    "Hech qayerga",
                    "Kafega",
                ],
                "answer": 0,
                "explanation": "“저는 한국에 <b>가려고 해요</b>” — Koreyaga "
                               "bormoqchi. U yerda Seulda ham, Pusanda ham "
                               "boʻlmoqchi.",
            },
            {
                "text": "Hana oʻtgan yili Pusanga bordimi?",
                "choices": [
                    "Ha, bordi",
                    "Yoʻq — bormoqchi edi, lekin vaqti boʻlmadi",
                    "Yoʻq — bormoqchi ham emas edi",
                    "Matnda aytilmagan",
                ],
                "answer": 1,
                "explanation": "“가려고 <b>했어요</b>. 하지만 시간이 없어서 못 "
                               "갔어요” — niyat bor edi, lekin amalga oshmadi. "
                               "려고 했어요 aynan shu maʼnoni beradi.",
            },
            {
                "text": "“밖에 비가 오려고 해요” nima degani?",
                "choices": [
                    "Yomgʻir yogʻay deb turibdi",
                    "Yomgʻir yogʻdi",
                    "Yomgʻirning niyati bor",
                    "Agar yomgʻir yogʻsa",
                ],
                "answer": 0,
                "explanation": "Jonsiz narsa bilan (으)려고 하다 niyatni emas, "
                               "<b>yaqin kelajakni</b> bildiradi — “hozir "
                               "boʻladi”. Shuning uchun ular kafega kirishdi.",
            },
        ],
    },
]
