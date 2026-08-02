# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-21 … PK-22 (Block B yakuni).

Kumulyativ qoida: PK-22 gacha oʻrganilgan hamma narsa ochiq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_21_22.py --author=prime
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
        "title":   "저는 커피를 안 마셔요",
        "summary": (
            "PK-21 matni. Jasur va Afsona nimani qilmasligini gaplashadi — "
            "안 va 지 않다 yonma-yon, hamda 없다 va 몰라요 istisnolari."
        ),
        "order":   21,
        "grammar": [
            {
                "pattern":  "안 + 동사/형용사",
                "meaning":  "Qisqa inkor — feʼl OLDIGA alohida soʻz boʻlib qoʻyiladi. "
                            "Ogʻzaki nutqda eng koʻp ishlatiladigan shakl.",
                "examples": ["안 마셔요.", "안 가요.", "날씨가 안 좋아요."],
            },
            {
                "pattern":  "어간 + 지 않다",
                "meaning":  "Uzun inkor — oʻzakka yopishadi, maʼnosi 안 bilan bir xil. "
                            "Tuslanadigan narsa 않다, uning oxirgi unlisi ㅏ, "
                            "shuning uchun har doim 지 않아요.",
                "examples": ["마시지 않아요.", "가지 않아요.", "좋지 않아요."],
            },
            {
                "pattern":  "하다 feʼllari va uchta istisno",
                "meaning":  "명사+하다 da 안 OʻRTAGA tushadi (공부 안 해요). Uchta soʻzning "
                            "inkori esa alohida soʻz: 있다→없다, 알다→모르다, 이다→아니다.",
                "examples": ["공부 안 해요.", "시간이 없어요.", "몰라요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Jasur">자수르</span> 씨와 <span class="cn-word" data-tr="Afsona">아프소나</span> 씨는 <span class="cn-word" data-tr="sinfxona">교실</span>에 있어요.</p>

<p><strong>자수르:</strong> 아프소나 씨, <span class="cn-word" data-tr="kofe">커피</span> <span class="cn-word" data-pos="verb" data-tr="ichasizmi">마셔요</span>?</p>

<p><strong>아프소나:</strong> 아니요, 저는 커피를 <span class="cn-word" data-tr="…ma (qisqa inkor)">안</span> 마셔요. <span class="cn-word" data-tr="sut">우유</span>를 마셔요.</p>

<p><strong>자수르:</strong> 저도 커피를 <span class="cn-word" data-tr="ichmayman (uzun inkor)">마시지 않아요</span>. 저는 <span class="cn-word" data-tr="choy">차</span>를 좋아해요.</p>

<p><strong>아프소나:</strong> 오늘 <span class="cn-word" data-tr="maktab">학교</span>에 <span class="cn-word" data-pos="verb" data-tr="borasizmi">가요</span>?</p>

<p><strong>자수르:</strong> 아니요, 오늘은 안 가요. <span class="cn-word" data-tr="dam olish kuni">주말</span>이에요. 주말에는 <span class="cn-word" data-tr="oʻqish">공부</span> 안 해요.</p>

<p><strong>아프소나:</strong> 저는 주말에도 공부해요. 하지만 오늘은 <span class="cn-word" data-tr="vaqt">시간</span>이 <span class="cn-word" data-tr="yoʻq">없어요</span>.</p>

<p><strong>자수르:</strong> <span class="cn-word" data-tr="nega">왜</span>요?</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-tr="bilmayman">몰라요</span>. 오늘은 <span class="cn-word" data-tr="ish">일</span>이 <span class="cn-word" data-pos="adj" data-tr="koʻp">많아요</span>.</p>

<p>아프소나 씨는 커피를 안 마셔요. 자수르 씨도 커피를 마시지 않아요. 자수르 씨와 아프소나 씨는 <span class="cn-word" data-tr="choy">차</span>를 좋아해요. <span class="cn-word" data-tr="lekin">하지만</span> 자수르 씨는 주말에 공부 안 해요. 아프소나 씨는 주말에도 공부해요.</p>''',
        "questions": [
            {
                "text": "Matnda “마시지 않아요” va “안 마셔요” ikkalasi ham ishlatilgan. Farqi nima?",
                "choices": [
                    "Maʼnosi bir xil — biri uzun, biri qisqa shakl",
                    "Birinchisi oʻtgan zamon",
                    "Birinchisi savol, ikkinchisi javob",
                    "Birinchisi imkoniyat yoʻqligini bildiradi",
                ],
                "answer": 0,
                "explanation": "안 + feʼl va oʻzak + 지 않다 — bir xil maʼno. 안 ogʻzaki "
                               "nutqda koʻproq, 지 않다 esa yozma va biroz taʼkidli. "
                               "Matnda ikkalasi ataylab yonma-yon qoʻyilgan.",
            },
            {
                "text": "Nega matnda “공부 안 해요” deyilgan, “안 공부해요” emas?",
                "choices": [
                    "공부하다 = 공부 (ot) + 하다 (feʼl), 안 esa feʼl oldiga tushadi",
                    "Chunki 공부 받침 bilan tugaydi",
                    "Chunki bu oʻtgan zamon",
                    "Chunki 안 har doim gap oxirida",
                ],
                "answer": 0,
                "explanation": "명사+하다 tuzilishidagi feʼllarda 안 OʻRTAGA tushadi: "
                               "공부 안 해요, 일 안 해요. Uzun shakl esa boʻlinmaydi — "
                               "공부하지 않아요.",
            },
            {
                "text": "Nega Afsona “시간이 안 있어요” demadi?",
                "choices": [
                    "있다 ning inkori alohida soʻz — 없다",
                    "Chunki 시간 받침 bilan tugaydi",
                    "Chunki u oʻtgan zamonda gapiryapti",
                    "Chunki 안 faqat feʼllar bilan keladi",
                ],
                "answer": 0,
                "explanation": "Uchta soʻzning inkori alohida: 있다 → 없다, 알다 → 모르다, "
                               "이다 → 아니다. Matnda ikkitasini koʻrasiz: 없어요 va 몰라요.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "오늘은 못 가요",
        "summary": (
            "PK-22 matni. Sherbek borishni xohlaydi, lekin imkoni yoʻq — 안 va 못 "
            "bir suhbatda qarama-qarshi qoʻyilgan."
        ),
        "order":   22,
        "grammar": [
            {
                "pattern":  "못 + 동사",
                "meaning":  "Imkoniyat yoʻqligi: “qila olmayman”. 안 (tanlov) dan farqi "
                            "shu — xohlaysiz, lekin nimadir toʻsqinlik qilyapti. "
                            "Oʻzbekcha “-a olmoq” ning inkori.",
                "examples": ["못 가요.", "못 먹어요.", "못 했어요."],
            },
            {
                "pattern":  "어간 + 지 못하다",
                "meaning":  "못 ning uzun shakli. 못하다 — 하다 feʼli, shuning uchun "
                            "har doim 지 못해요 boʻladi.",
                "examples": ["가지 못해요.", "먹지 못해요.", "읽지 못해요."],
            },
            {
                "pattern":  "못 ning talaffuzi",
                "meaning":  "못 ning 받침i [ㄷ] boʻlib toʻxtaydi, keyingi tovushga qarab "
                            "uch xil oʻzgaradi: 경음화, 비음화 yoki 격음화 (PK-8).",
                "examples": ["못 가요 → [몯까요]", "못 먹어요 → [몬머거요]",
                             "못 해요 → [모태요]"],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Jiyoung">지영</span> 씨와 <span class="cn-word" data-tr="Sherbek">셰르벡</span> 씨가 <span class="cn-word" data-pos="verb" data-tr="gaplashadi">말해요</span>.</p>

<p><strong>지영:</strong> 셰르벡 씨, <span class="cn-word" data-tr="bugun">오늘</span> <span class="cn-word" data-tr="uy">집</span>에 <span class="cn-word" data-pos="verb" data-tr="kelasizmi">와요</span>?</p>

<p><strong>셰르벡:</strong> 오늘은 <span class="cn-word" data-tr="…ay olmayman">못</span> <span class="cn-word" data-pos="verb" data-tr="boraman">가요</span>. <span class="cn-word" data-tr="ish">일</span>이 <span class="cn-word" data-pos="adj" data-tr="koʻp">많아요</span>.</p>

<p><strong>지영:</strong> <span class="cn-word" data-tr="ertaga">내일</span>은 집에 와요?</p>

<p><strong>셰르벡:</strong> <span class="cn-word" data-tr="ertaga">내일</span>도 <span class="cn-word" data-tr="borolmayman (uzun)">가지 못해요</span>. <span class="cn-word" data-tr="vaqt">시간</span>이 없어요.</p>

<p><strong>지영:</strong> <span class="cn-word" data-tr="kecha">어제</span>는 <span class="cn-word" data-tr="nima">무엇</span>을 <span class="cn-word" data-pos="verb" data-tr="qildingiz">했어요</span>?</p>

<p><strong>셰르벡:</strong> 어제도 <span class="cn-word" data-tr="oʻqish">공부</span> <span class="cn-word" data-tr="qila olmadim">못 했어요</span>. <span class="cn-word" data-pos="adj" data-tr="band edim">바빴어요</span>.</p>

<p><strong>지영:</strong> <span class="cn-word" data-tr="kofe">커피</span>를 <span class="cn-word" data-pos="verb" data-tr="ichasizmi">마셔요</span>?</p>

<p><strong>셰르벡:</strong> 저는 커피를 <span class="cn-word" data-tr="…ma (tanlov)">안</span> 마셔요. 커피를 <span class="cn-word" data-pos="verb" data-tr="yoqtirmayman">좋아하지 않아요</span>. <span class="cn-word" data-tr="lekin">하지만</span> <span class="cn-word" data-tr="choy">차</span>는 마셔요.</p>

<p>셰르벡 씨는 오늘 지영 씨 집에 <span class="cn-word" data-tr="borolmaydi">못 가요</span>. 일이 많아요. 커피는 <span class="cn-word" data-tr="ichmaydi">안 마셔요</span> — 커피를 좋아하지 않아요. “안”과 “못”은 <span class="cn-word" data-tr="bir xil emas">같지 않아요</span>.</p>''',
        "questions": [
            {
                "text": "Nega Sherbek “못 가요” dedi, “안 가요” emas?",
                "choices": [
                    "Bormoqchi, lekin ishi koʻp — imkoniyat yoʻq",
                    "Chunki u bormoqchi emas",
                    "Chunki bu oʻtgan zamon",
                    "Chunki 가다 har doim 못 bilan keladi",
                ],
                "answer": 0,
                "explanation": "못 = imkoniyat yoʻqligi (“bora olmayman”), 안 = tanlov "
                               "(“bormayman”). Sherbekning ishi koʻp — bu toʻsqinlik, "
                               "shuning uchun 못. Oʻzbekchada ham xuddi shu farq bor.",
            },
            {
                "text": "Xuddi shu suhbatda Sherbek kofe haqida nega “안 마셔요” dedi?",
                "choices": [
                    "Kofeni yoqtirmaydi — bu tanlov, imkoniyat masalasi emas",
                    "Chunki kofe yoʻq edi",
                    "Chunki u kasal",
                    "Chunki 마시다 못 bilan ishlatilmaydi",
                ],
                "answer": 0,
                "explanation": "“커피를 좋아하지 않아요” — u kofeni yoqtirmaydi. Bu tanlov, "
                               "shuning uchun 안. Agar shifokor taqiqlagan boʻlsa "
                               "“못 마셔요” boʻlardi.",
            },
            {
                "text": "“공부 못 했어요” qanday oʻqiladi?",
                "choices": [
                    "[공부 모태써요]",
                    "[공부 못 해써요]",
                    "[공부 몯해써요]",
                    "[공부 모새써요]",
                ],
                "answer": 0,
                "explanation": "못 ning 받침i [ㄷ] boʻlib toʻxtaydi, keyin ㅎ bilan "
                               "uchrashib 격음화 boʻyicha ㅌ beradi: 못 해 → [모태]. "
                               "Bu PK-8 dagi qoida.",
            },
        ],
    },
]
