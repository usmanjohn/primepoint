# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-29 … PK-31 (buyruq, imkon, iltimos).

Kumulyativ qoida: PK-31 gacha oʻrganilgan hamma narsa ochiq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_29_31.py --author=prime
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
        "title":   "여기 앉으세요",
        "summary": (
            "PK-29 matni. Afsona birinchi marta koreys darsiga kiradi — bir dars "
            "davomida oʻnlab (으)세요 va bitta 지 마세요 eshitiladi."
        ),
        "order":   29,
        "grammar": [
            {
                "pattern":  "동사 + (으)세요",
                "meaning":  "Hurmatli buyruq va iltimos. 받침 yoʻq → 세요 (가세요), "
                            "받침 bor → 으세요 (앉으세요). ㄹ oʻzak ㄹ ni tashlaydi "
                            "(만들다 → 만드세요).",
                "examples": ["여기 앉으세요.", "책을 읽으세요.", "잠깐 기다리세요."],
            },
            {
                "pattern":  "동사 + 지 마세요",
                "meaning":  "Taqiq — “…mang”. 받침 ayrisi yoʻq, oʻzakka toʻgʻridan-"
                            "toʻgʻri yopishadi. Taqiq uchun 안 ishlatilmaydi.",
                "examples": ["여기에서 사진을 찍지 마세요.", "늦지 마세요."],
            },
            {
                "pattern":  "드세요 · 계세요 · 주무세요",
                "meaning":  "Ayrim feʼllarning hurmatli shakli butunlay boshqa: "
                            "먹다/마시다 → 드세요, 있다 → 계세요, 자다 → 주무세요. "
                            "Va bu shakl oʻzi haqida ishlatilmaydi.",
                "examples": ["물 드세요.", "안녕히 계세요.", "안녕히 주무세요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Afsona">아프소나</span> 씨는 <span class="cn-word" data-tr="bugun">오늘</span> <span class="cn-word" data-tr="birinchi marta">처음</span> <span class="cn-word" data-tr="koreys tili darsi">한국어 교실</span>에 <span class="cn-word" data-pos="verb" data-tr="keldi">왔어요</span>.</p>

<p><strong>선생님:</strong> <span class="cn-word" data-tr="xush kelibsiz">어서 오세요</span>. <span class="cn-word" data-tr="bu yerga">여기</span> <span class="cn-word" data-tr="oʻtiring">앉으세요</span>.</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-tr="rahmat">감사합니다</span>.</p>

<p><strong>선생님:</strong> <span class="cn-word" data-tr="suv">물</span> <span class="cn-word" data-tr="iching">드세요</span>. 그리고 <span class="cn-word" data-tr="kitob">책</span>을 <span class="cn-word" data-tr="oching">펴세요</span>. <span class="cn-word" data-tr="9-bet">9쪽</span>을 <span class="cn-word" data-tr="oʻqing">읽으세요</span>.</p>

<p>아프소나 씨는 책을 읽어요. <span class="cn-word" data-pos="adv" data-tr="lekin">하지만</span> <span class="cn-word" data-pos="adj" data-tr="qiyin">어려워요</span>.</p>

<p><strong>아프소나:</strong> 선생님, <span class="cn-word" data-tr="sekin">천천히</span> <span class="cn-word" data-tr="gapiring">말씀하세요</span>. 저는 한국어를 <span class="cn-word" data-tr="yaxshi">잘</span> <span class="cn-word" data-tr="bilmayman">몰라요</span>.</p>

<p><strong>선생님:</strong> <span class="cn-word" data-tr="ha">네</span>. <span class="cn-word" data-tr="xavotir olmang">걱정하지 마세요</span>. <span class="cn-word" data-tr="har kuni">매일</span> <span class="cn-word" data-tr="oʻqing">공부하세요</span>. 그리고 <span class="cn-word" data-tr="darsga">수업에</span> <span class="cn-word" data-tr="kechikmang">늦지 마세요</span>.</p>

<p><span class="cn-word" data-tr="dars">수업</span>이 <span class="cn-word" data-pos="verb" data-tr="tugadi">끝났어요</span>.</p>

<p><strong>선생님:</strong> <span class="cn-word" data-tr="ertaga">내일</span> 또 <span class="cn-word" data-tr="keling">오세요</span>. 안녕히 <span class="cn-word" data-tr="boring">가세요</span>.</p>

<p><strong>아프소나:</strong> 선생님, 안녕히 <span class="cn-word" data-tr="qoling">계세요</span>.</p>''',
        "questions": [
            {
                "text": "Nega matnda “앉으세요” deyilgan, “앉세요” emas?",
                "choices": [
                    "앉 oʻzagida 받침 bor — shuning uchun 으세요",
                    "Chunki bu taqiq",
                    "Chunki 앉다 notoʻgʻri feʼl",
                    "Chunki gap oʻtgan zamonda",
                ],
                "answer": 0,
                "explanation": "받침 bor boʻlsa <b>으세요</b> qoʻshiladi (앉으세요, "
                               "읽으세요), 받침 yoʻq boʻlsa oddiy <b>세요</b> "
                               "(가세요, 오세요).",
            },
            {
                "text": "Oʻqituvchi Afsonaga nimani taqiqladi?",
                "choices": [
                    "Darsga kechikishni",
                    "Kitob oʻqishni",
                    "Savol berishni",
                    "Suv ichishni",
                ],
                "answer": 0,
                "explanation": "“수업에 늦지 마세요” — darsga kechikmang. Taqiq har doim "
                               "<b>지 마세요</b> bilan beriladi; “걱정하지 마세요” "
                               "(xavotir olmang) ham shu qolipda.",
            },
            {
                "text": "Nega oʻqituvchi “가세요” deydi, Afsona esa “계세요”?",
                "choices": [
                    "Ketayotgan odamga 가세요, qoladigan odamga 계세요",
                    "Biri hurmatli, ikkinchisi emas",
                    "Biri savol, ikkinchisi buyruq",
                    "Farqi yoʻq, ikkalasi bir xil",
                ],
                "answer": 0,
                "explanation": "안녕히 <b>가세요</b> — “yaxshi boring” (ketayotganga). "
                               "안녕히 <b>계세요</b> — “yaxshi qoling” (qoladiganga). "
                               "계세요 — 있다 ning hurmatli shakli.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "저는 김치를 먹을 수 있어요",
        "summary": (
            "PK-30 matni. Sherbek Koreyaga kelgan doʻstiga savol beradi — nima "
            "qila oladi, nima qila olmaydi. Imkon va imkonsizlik yonma-yon."
        ),
        "order":   30,
        "grammar": [
            {
                "pattern":  "동사 + (으)ㄹ 수 있다",
                "meaning":  "Imkon va qobiliyat. 받침 yoʻq → ㄹ 수 있어요 (갈), 받침 "
                            "bor → 을 수 있어요 (먹을). Oʻzak ㄹ bilan tugasa yangi ㄹ "
                            "qoʻshilmaydi. Oʻqilishi [쑤].",
                "examples": ["갈 수 있어요", "먹을 수 있어요", "만들 수 있어요"],
            },
            {
                "pattern":  "동사 + (으)ㄹ 수 없다",
                "meaning":  "Imkonsizlik. Inkor uchun 안 emas, 있다 ning jufti "
                            "없다 ishlatiladi. Oʻtgan zamon oxirgi soʻzda: "
                            "(으)ㄹ 수 있었어요 / 없었어요.",
                "examples": ["갈 수 없어요", "먹을 수 없었어요"],
            },
            {
                "pattern":  "못 va (으)ㄹ 수 없다",
                "meaning":  "Ikkalasi ham “ololmaslik”. 못 qisqa va ogʻzaki, "
                            "(으)ㄹ 수 없다 esa toʻliqroq. Lekin ijobiy tomonda 못 "
                            "ning jufti yoʻq — “qila olaman” faqat 할 수 있어요.",
                "examples": ["못 가요.", "갈 수 없어요.", "할 수 있어요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Sherbek">셰르벡</span> 씨는 <span class="cn-word" data-tr="Koreya">한국</span>에 <span class="cn-word" data-pos="verb" data-tr="keldi">왔어요</span>. <span class="cn-word" data-tr="doʻst">친구</span> <span class="cn-word" data-tr="Minsu">민수</span> 씨와 <span class="cn-word" data-tr="restoran">식당</span>에서 <span class="cn-word" data-pos="verb" data-tr="ovqatlanadi">밥을 먹어요</span>.</p>

<p><strong>민수:</strong> 셰르벡 씨, <span class="cn-word" data-tr="achchiq">매운</span> <span class="cn-word" data-tr="ovqat">음식</span>을 <span class="cn-word" data-tr="yeya olasizmi">먹을 수 있어요</span>?</p>

<p><strong>셰르벡:</strong> 네, 저는 <span class="cn-word" data-tr="kimchi">김치</span>를 먹을 수 있어요. <span class="cn-word" data-tr="lekin">하지만</span> <span class="cn-word" data-tr="juda">아주</span> 매운 음식은 <span class="cn-word" data-tr="yeya olmayman">먹을 수 없어요</span>.</p>

<p><strong>민수:</strong> 한국어를 <span class="cn-word" data-tr="gapira olasizmi">할 수 있어요</span>?</p>

<p><strong>셰르벡:</strong> <span class="cn-word" data-tr="ozgina">조금</span> 할 수 있어요. <span class="cn-word" data-tr="kitob">책</span>도 <span class="cn-word" data-tr="oʻqiy olaman">읽을 수 있어요</span>. <span class="cn-word" data-tr="oʻtgan yil">작년</span>에는 <span class="cn-word" data-tr="oʻqiy olmasdim">읽을 수 없었어요</span>.</p>

<p><strong>민수:</strong> <span class="cn-word" data-tr="ajoyib">정말 좋아요</span>! <span class="cn-word" data-tr="ertaga">내일</span> <span class="cn-word" data-tr="togʻ">산</span>에 <span class="cn-word" data-tr="borasizmi">갈 거예요</span>?</p>

<p><strong>셰르벡:</strong> <span class="cn-word" data-tr="bormoqchiman">가고 싶어요</span>. 하지만 <span class="cn-word" data-tr="ish">일</span>이 <span class="cn-word" data-pos="adj" data-tr="koʻp">많아요</span>. 그래서 <span class="cn-word" data-tr="borolmayman">갈 수 없어요</span>.</p>

<p><strong>민수:</strong> 그럼 <span class="cn-word" data-tr="shanba">토요일</span>에 갈 수 있어요?</p>

<p><strong>셰르벡:</strong> 네, 토요일에는 갈 수 있어요. 저는 <span class="cn-word" data-tr="yolgʻiz">혼자</span> 산에 <span class="cn-word" data-tr="borolmayman">갈 수 없어요</span>. <span class="cn-word" data-tr="birga">같이</span> 가세요!</p>

<p>민수 씨는 <span class="cn-word" data-tr="kimchi jjigae">김치찌개</span>를 <span class="cn-word" data-tr="tayyorlay oladi">만들 수 있어요</span>. 셰르벡 씨는 <span class="cn-word" data-tr="tayyorlay olmaydi">만들 수 없어요</span>. 하지만 <span class="cn-word" data-tr="oʻrganmoqchi">배우고 싶어해요</span>.</p>''',
        "questions": [
            {
                "text": "Nega matnda “만들 수 있어요” da 을 qoʻshilmagan?",
                "choices": [
                    "Oʻzak 만들 allaqachon ㄹ bilan tugaydi",
                    "Chunki 만들다 sifat",
                    "Chunki bu inkor",
                    "Bu xato — 만들을 수 있어요 boʻlishi kerak",
                ],
                "answer": 0,
                "explanation": "Oʻzak ㄹ bilan tugasa yangi ㄹ qoʻshilmaydi: "
                               "<b>만들 수 있어요</b>. Solishtiring: 먹 → 먹을 수 있어요. "
                               "PK-27 dagi 살 거예요 ham shu qoida.",
            },
            {
                "text": "Sherbek nega ertaga togʻga borolmaydi?",
                "choices": [
                    "Ishi koʻp",
                    "Yomgʻir yogʻadi",
                    "Bormoqchi emas",
                    "Yoʻlni bilmaydi",
                ],
                "answer": 0,
                "explanation": "“일이 많아요. 그래서 갈 수 없어요” — ishi koʻp. Xohishi "
                               "esa bor: “가고 싶어요” (PK-28). Xohish va imkon — "
                               "boshqa-boshqa narsa.",
            },
            {
                "text": "“작년에는 읽을 수 없었어요” gapida oʻtgan zamon qayerga qoʻshilgan?",
                "choices": [
                    "없다 ga — 없었어요",
                    "읽다 ga — 읽었을",
                    "수 ga",
                    "Hech qayerga, 작년 soʻzi yetarli",
                ],
                "answer": 0,
                "explanation": "Tuslanish har doim <b>oxirgi soʻzda</b>: 읽을 수 "
                               "<b>없었어요</b>. <s>읽었을 수 없어요</s> notoʻgʻri — "
                               "bu PK-28 dagi 고 싶었어요 bilan bir xil mantiq.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "사진 좀 찍어 주세요",
        "summary": (
            "PK-31 matni. Dilnoza Seulda sayohatda — bir kunda bir necha marta "
            "iltimos qiladi va bir marta oʻzi yordam beradi."
        ),
        "order":   31,
        "grammar": [
            {
                "pattern":  "동사 + 아/어 주다",
                "meaning":  "Ish boshqa odamning foydasiga qilinadi — oʻzbekchadagi "
                            "“…ib bermoq”. 받침 ayrisi yoʻq: 아/어 shakli olinadi va "
                            "주다 yoniga qoʻyiladi.",
                "examples": ["읽어 주다", "사 주다", "해 주다", "가르쳐 주다"],
            },
            {
                "pattern":  "아/어 주세요 · 좀",
                "meaning":  "Iltimosning asosiy shakli (주다 + PK-29 dagi 세요). "
                            "좀 feʼldan oldin turib iltimosni yumshatadi — "
                            "oʻzbekchadagi “iltimos” yoki “-chi” kabi.",
                "examples": ["사진 좀 찍어 주세요.", "다시 말해 주세요.",
                             "문을 열어 주세요."],
            },
            {
                "pattern":  "한테 / 에게 / 께",
                "meaning":  "Ish kimga qilinganini koʻrsatadi. 한테 — ogʻzaki, "
                            "에게 — yozma, 께 — hurmatli. Diqqat: odamga 한테/에게, "
                            "joyga esa 에.",
                "examples": ["친구한테 사 줬어요.", "저에게 만들어 주셨어요.",
                             "선생님께 써 줬어요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Dilnoza">딜노자</span> 씨는 <span class="cn-word" data-tr="Seul">서울</span>에서 <span class="cn-word" data-tr="sayohat">여행</span>을 해요. <span class="cn-word" data-tr="bugun">오늘</span> <span class="cn-word" data-tr="ob-havo">날씨</span>가 <span class="cn-word" data-pos="adj" data-tr="yaxshi">좋아요</span>.</p>

<p><strong>딜노자:</strong> <span class="cn-word" data-tr="kechirasiz">저기요</span>, <span class="cn-word" data-tr="rasm">사진</span> <span class="cn-word" data-tr="iltimos">좀</span> <span class="cn-word" data-tr="olib bering">찍어 주세요</span>.</p>

<p><strong>한국 사람:</strong> 네, <span class="cn-word" data-tr="bir">하나</span>, <span class="cn-word" data-tr="ikki">둘</span>, <span class="cn-word" data-tr="uch">셋</span>!</p>

<p><strong>딜노자:</strong> <span class="cn-word" data-tr="rahmat">감사합니다</span>. <span class="cn-word" data-tr="yana bir marta">한 번 더</span> <span class="cn-word" data-tr="olib bering">찍어 주세요</span>.</p>

<p><span class="cn-word" data-tr="keyin">그 다음</span>에 딜노자 씨는 <span class="cn-word" data-tr="doʻkon">가게</span>에 <span class="cn-word" data-pos="verb" data-tr="kirdi">갔어요</span>. <span class="cn-word" data-tr="narx">값</span>을 <span class="cn-word" data-tr="bilmaydi">몰라요</span>.</p>

<p><strong>딜노자:</strong> <span class="cn-word" data-tr="bu">이것</span>은 <span class="cn-word" data-tr="qancha">얼마</span>예요? <span class="cn-word" data-tr="sekin">천천히</span> <span class="cn-word" data-tr="aytib bering">말해 주세요</span>.</p>

<p><strong>가게 사람:</strong> <span class="cn-word" data-tr="oʻn ming von">만 원</span>이에요.</p>

<p>딜노자 씨는 <span class="cn-word" data-tr="doʻst">친구</span> <span class="cn-word" data-tr="Afsona">아프소나</span> 씨<span class="cn-word" data-tr="ga">한테</span> <span class="cn-word" data-tr="sovgʻa">선물</span>을 <span class="cn-word" data-tr="sotib olib berdi">사 줬어요</span>.</p>

<p><span class="cn-word" data-tr="kechqurun">저녁</span>에 <span class="cn-word" data-tr="Jiyoung">지영</span> 씨가 <span class="cn-word" data-tr="kimchi jjigae">김치찌개</span>를 <span class="cn-word" data-tr="tayyorlab berdi">만들어 줬어요</span>.</p>

<p><strong>딜노자:</strong> <span class="cn-word" data-tr="juda">아주</span> <span class="cn-word" data-pos="adj" data-tr="mazali">맛있어요</span>! <span class="cn-word" data-tr="menga">저한테</span> <span class="cn-word" data-tr="oʻrgatib bering">가르쳐 주세요</span>.</p>

<p><strong>지영:</strong> 네, <span class="cn-word" data-tr="ertaga">내일</span> <span class="cn-word" data-tr="oʻrgatib beraman">가르쳐 줄 거예요</span>. 하지만 오늘은 <span class="cn-word" data-tr="dam oling">쉬세요</span>.</p>''',
        "questions": [
            {
                "text": "Matnda “사진 좀 찍어 주세요” deyilgan. 좀 nima uchun qoʻshilgan?",
                "choices": [
                    "Iltimosni yumshatish uchun — “iltimos”, “-chi” kabi",
                    "“Ozgina rasm” degani",
                    "Oʻtgan zamon yasash uchun",
                    "Inkor qilish uchun",
                ],
                "answer": 0,
                "explanation": "좀 aslida “ozgina” degani, lekin iltimosda u miqdorni "
                               "emas, <b>xushmuomalalikni</b> bildiradi va feʼldan "
                               "oldin turadi.",
            },
            {
                "text": "“친구한테 선물을 사 줬어요” da nega 한테, 에 emas?",
                "choices": [
                    "친구 — odam; odamga 한테/에게, joyga esa 에",
                    "Chunki 친구 받침 bilan tugamaydi",
                    "Chunki gap oʻtgan zamonda",
                    "Chunki 사다 notoʻgʻri feʼl",
                ],
                "answer": 0,
                "explanation": "Koreys tili odam va joyni ajratadi: 학교<b>에</b> 가요 "
                               "(joy), 친구<b>한테</b> 줘요 (odam). Oʻzbekchada ikkalasi "
                               "ham “-ga” boʻlgani uchun bu yerda koʻp adashiladi.",
            },
            {
                "text": "“만들어 줬어요” da oʻtgan zamon qayerga qoʻshilgan?",
                "choices": [
                    "주다 ga — 줬어요",
                    "만들다 ga — 만들었어",
                    "Ikkalasiga ham",
                    "Hech qayerga",
                ],
                "answer": 0,
                "explanation": "Tuslanish faqat <b>주다</b> da boʻladi: 만들어 "
                               "<b>줬어요</b>. <s>만들었어 줘요</s> notoʻgʻri — asosiy "
                               "feʼl 아/어 shaklida qotib qoladi.",
            },
        ],
    },
]
