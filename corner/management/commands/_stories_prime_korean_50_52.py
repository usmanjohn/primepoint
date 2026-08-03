# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-50 … PK-52 (아/어야 하다, 아/어도 되다, 것 같다).

Kumulyativ qoida: PK-52 gacha oʻrganilgan hamma narsa ochiq.
PK-50 matnida 아/어도 되다 (51) va 것 같다 (52) hali YOʻQ.
PK-51 matnida 것 같다 hali yoʻq.
Block E (53+) — (으)ㄹ 줄 알다, 기로 하다, 잖아요, majhul/orttirma nisbat,
아/어 버리다, aytilgan gap — hech qaysisida yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_50_52.py --author=prime
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
        "title":   "내일까지 숙제를 내야 해요",
        "summary": (
            "PK-50 matni. Sherbek uy vazifasini unutdi va nima qilishi "
            "kerakligini oʻqituvchidan soʻraydi — butun suhbat 아/어야 하다 "
            "ustida yuradi."
        ),
        "order":   50,
        "grammar": [
            {
                "pattern":  "동사/형용사 + 아/어야 하다 / 되다",
                "meaning":  "“…ishi kerak”. 아/어요 shaklidan yasaladi: 요 "
                            "oʻrniga 야 하다. 하다 rasmiyroq, 되다 ogʻzakiroq — "
                            "ikkalasi ham toʻgʻri.",
                "examples": ["내일까지 숙제를 내야 해요.",
                             "지금 가야 돼요.",
                             "방이 깨끗해야 해요."],
            },
            {
                "pattern":  "아/어야 했어요 — oʻtgan zamon",
                "meaning":  "Zamon oxirdagi 하다/되다 ga qoʻyiladi, 야 ga emas: "
                            "가야 했어요 (“borishim kerak edi”), 갔어야 해요 EMAS.",
                "examples": ["어제 병원에 가야 했어요.",
                             "숙제를 어제 해야 했어요."],
            },
            {
                "pattern":  "야 ning maʼnosi",
                "meaning":  "야 — “faqat, aynan”. 가야 해요 soʻzma-soʻz “faqat "
                            "borsam — boʻladi”, yaʼni boshqa yoʻl yoʻq. "
                            "Shundan majburiyat kelib chiqadi.",
                "examples": ["약을 먹어야 해요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Sherbek">셰르벡</span> 씨가 <span class="cn-word" data-tr="uy vazifasini">숙제</span>를 <span class="cn-word" data-pos="verb" data-tr="unutdi">잊었어요</span>. <span class="cn-word" data-tr="oʻqituvchi">선생님</span>과 <span class="cn-word" data-pos="verb" data-tr="gaplashyapti">이야기하고 있어요</span>.</p>

<p><strong>셰르벡:</strong> 선생님, 숙제를 <span class="cn-word" data-pos="adv" data-tr="qachongacha">언제까지</span> <span class="cn-word" data-pos="verb" data-tr="topshirishim kerak">내야 해요</span>?</p>

<p><strong>선생님:</strong> <span class="cn-word" data-tr="ertagacha">내일까지</span> 내야 해요. <span class="cn-word" data-pos="adv" data-tr="aslida">사실</span> <span class="cn-word" data-tr="kecha">어제</span> <span class="cn-word" data-pos="verb" data-tr="qilishingiz kerak edi">해야 했어요</span>.</p>

<p><strong>셰르벡:</strong> <span class="cn-word" data-pos="verb" data-tr="uzr soʻrayman">죄송합니다</span>. <span class="cn-word" data-pos="adj" data-tr="kasal boʻlganim uchun">아파서</span> 못 했어요.</p>

<p><strong>선생님:</strong> <span class="cn-word" data-pos="adj" data-tr="hech gap emas">괜찮아요</span>. 하지만 <span class="cn-word" data-tr="bugun kechqurun">오늘 저녁</span>에 <span class="cn-word" data-pos="verb" data-tr="qilishingiz kerak">해야 돼요</span>. <span class="cn-word" data-tr="masalalar">문제</span>가 <span class="cn-word" data-pos="adj" data-tr="qiyin">어려워요</span>. 그러니까 <span class="cn-word" data-pos="adv" data-tr="erta">일찍</span> <span class="cn-word" data-pos="verb" data-tr="boshlashingiz kerak">시작해야 해요</span>.</p>

<p><strong>셰르벡:</strong> 네. <span class="cn-word" data-tr="kitobni">책</span>도 <span class="cn-word" data-pos="verb" data-tr="oʻqishim kerakmi">읽어야 해요</span>?</p>

<p><strong>선생님:</strong> 네. 그리고 <span class="cn-word" data-tr="yozuv">글</span>이 <span class="cn-word" data-pos="adj" data-tr="toza boʻlishi kerak">깨끗해야 해요</span>. <span class="cn-word" data-tr="ismingizni">이름</span>도 <span class="cn-word" data-pos="verb" data-tr="yozishingiz kerak">써야 해요</span>.</p>

<p><strong>셰르벡:</strong> <span class="cn-word" data-pos="verb" data-tr="tushundim">알았어요</span>. 오늘은 <span class="cn-word" data-tr="doʻstim bilan">친구하고</span> <span class="cn-word" data-pos="verb" data-tr="oʻynamoqchi edim">놀려고 했어요</span>. 하지만 <span class="cn-word" data-pos="verb" data-tr="qilishim kerak">해야 해요</span>.</p>

<p><strong>선생님:</strong> <span class="cn-word" data-tr="dam olish kunlarida">주말</span>에 <span class="cn-word" data-pos="verb" data-tr="oʻynang">노세요</span>. <span class="cn-word" data-tr="hozir">지금</span>은 <span class="cn-word" data-tr="oʻqish">공부하는 것</span>이 제일 <span class="cn-word" data-tr="muhim">중요해요</span>.</p>''',
        "questions": [
            {
                "text": "Uy vazifasini qachongacha topshirish kerak?",
                "choices": [
                    "Bugun kechgacha",
                    "Ertagacha",
                    "Dam olish kunigacha",
                    "Kechagacha edi, endi kech",
                ],
                "answer": 1,
                "explanation": "“<b>내일까지</b> 내야 해요” — ertagacha. "
                               "Aslida kecha topshirilishi kerak edi "
                               "(어제 해야 했어요), lekin muddat uzaytirildi.",
            },
            {
                "text": "Oʻqituvchi nega erta boshlashni aytdi?",
                "choices": [
                    "Chunki masalalar qiyin",
                    "Chunki ertaga bayram",
                    "Chunki Sherbek kasal",
                    "Chunki kitob uzun",
                ],
                "answer": 0,
                "explanation": "“문제가 <b>어려워요</b>. 그러니까 일찍 "
                               "시작해야 해요” — masalalar qiyin boʻlgani "
                               "uchun. 그러니까 dan keyin maslahat kelgani "
                               "ham eʼtiborga loyiq (PK-48).",
            },
            {
                "text": "Nega matnda “어제 해야 했어요” deyilgan, "
                        "“어제 했어야 해요” emas?",
                "choices": [
                    "Zamon oxirdagi 하다 ga qoʻyiladi",
                    "Chunki 하다 notoʻgʻri feʼl",
                    "Chunki gap savol shaklida",
                    "Ikkalasi ham toʻgʻri",
                ],
                "answer": 0,
                "explanation": "Bu — butun kurs boʻyicha takrorlanadigan "
                               "qoida: <b>zamon gapning oxirida</b>. "
                               "야 ga zamon qoʻyilmaydi.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "여기에서 사진을 찍어도 돼요?",
        "summary": (
            "PK-51 matni. Dilnoza bilan Hana muzeyda — nima mumkin, nima "
            "mumkin emasligini soʻrashadi. Ruxsat va taqiq yonma-yon."
        ),
        "order":   51,
        "grammar": [
            {
                "pattern":  "동사 + 아/어도 되다",
                "meaning":  "Ruxsat: “…sa ham boʻladi”. 아/어요 shaklidan "
                            "yasaladi. 되다 oʻrniga 괜찮다 yoki 좋다 ham "
                            "ishlatiladi.",
                "examples": ["여기에서 사진을 찍어도 돼요?",
                             "네, 찍어도 돼요.", "여기에 앉아도 괜찮아요."],
            },
            {
                "pattern":  "동사 + (으)면 안 되다",
                "meaning":  "Taqiq: “…sa boʻlmaydi”. Ruxsat savoliga RAD "
                            "javobi shu qolip bilan beriladi — qolip "
                            "almashadi.",
                "examples": ["여기에서 먹으면 안 돼요.",
                             "아니요, 들어가면 안 돼요."],
            },
            {
                "pattern":  "안 …아/어도 되다 va (으)면 안 되다",
                "meaning":  "Aralashtirmang: 안 가도 돼요 — “bormasangiz ham "
                            "boʻladi” (shart emas), 가면 안 돼요 — “borsangiz "
                            "boʻlmaydi” (taqiq). Inkorning oʻrniga qarang.",
                "examples": ["표를 안 사도 돼요.", "만지면 안 돼요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Dilnoza">딜노자</span> 씨와 <span class="cn-word" data-tr="Hana">하나</span> 씨가 <span class="cn-word" data-tr="muzeyga">박물관에</span> 갔어요.</p>

<p><strong>딜노자:</strong> <span class="cn-word" data-tr="chipta">표</span>를 <span class="cn-word" data-pos="verb" data-tr="sotib olishimiz kerak">사야 해요</span>?</p>

<p><strong>하나:</strong> 아니요. <span class="cn-word" data-tr="talabalar">학생</span>은 표를 <span class="cn-word" data-pos="verb" data-tr="sotib olmasa ham boʻladi">안 사도 돼요</span>. <span class="cn-word" data-tr="talaba guvohnomasi">학생증</span>만 <span class="cn-word" data-pos="adj" data-tr="kerak">필요해요</span>.</p>

<p><span class="cn-word" data-tr="ichkariga">안에</span> <span class="cn-word" data-pos="verb" data-tr="kirishdi">들어갔어요</span>. <span class="cn-word" data-tr="rasm">그림</span>이 <span class="cn-word" data-pos="adj" data-tr="juda chiroyli">아주 예뻐요</span>.</p>

<p><strong>딜노자:</strong> 여기에서 <span class="cn-word" data-tr="surat">사진</span>을 <span class="cn-word" data-pos="verb" data-tr="olsam boʻladimi">찍어도 돼요</span>?</p>

<p><strong>하나:</strong> 네, <span class="cn-word" data-pos="verb" data-tr="olsangiz boʻladi">찍어도 돼요</span>. 하지만 <span class="cn-word" data-tr="chiroq">플래시</span>를 <span class="cn-word" data-pos="verb" data-tr="ishlatsangiz boʻlmaydi">쓰면 안 돼요</span>.</p>

<p><strong>딜노자:</strong> 그림을 <span class="cn-word" data-pos="verb" data-tr="tegsam boʻladimi">만져도 돼요</span>?</p>

<p><strong>하나:</strong> 아니요! <span class="cn-word" data-pos="verb" data-tr="tegsangiz boʻlmaydi">만지면 안 돼요</span>. 그리고 여기에서 <span class="cn-word" data-pos="verb" data-tr="yesangiz boʻlmaydi">먹으면 안 돼요</span>.</p>

<p><strong>딜노자:</strong> <span class="cn-word" data-pos="verb" data-tr="gaplashsak boʻladimi">이야기해도 돼요</span>?</p>

<p><strong>하나:</strong> <span class="cn-word" data-pos="adv" data-tr="jimgina">조용히</span> 이야기해도 <span class="cn-word" data-pos="adj" data-tr="hech gap emas">괜찮아요</span>. 하지만 <span class="cn-word" data-pos="adj" data-tr="shovqin qilsangiz">시끄러우면</span> 안 돼요.</p>

<p><strong>딜노자:</strong> <span class="cn-word" data-pos="verb" data-tr="tushundim">알았어요</span>. 여기는 <span class="cn-word" data-tr="qoidalar">규칙</span>이 <span class="cn-word" data-pos="adj" data-tr="koʻp">많아요</span>!</p>

<p><strong>하나:</strong> 하지만 <span class="cn-word" data-tr="rasmlar">그림</span>은 <span class="cn-word" data-pos="adj" data-tr="chiroyli">예뻐요</span>. <span class="cn-word" data-pos="verb" data-tr="kelganimiz uchun">와서</span> 좋아요.</p>''',
        "questions": [
            {
                "text": "Talabalar chipta sotib olishi kerakmi?",
                "choices": [
                    "Ha, kerak",
                    "Yoʻq — sotib olmasa ham boʻladi",
                    "Yoʻq — sotib olsa boʻlmaydi",
                    "Matnda aytilmagan",
                ],
                "answer": 1,
                "explanation": "“학생은 표를 <b>안 사도 돼요</b>” — bu "
                               "<b>shart emas</b> degani, taqiq emas. "
                               "사면 안 돼요 boʻlganda “sotib olsangiz "
                               "boʻlmaydi” degan boshqa maʼno chiqardi.",
            },
            {
                "text": "Muzeyda nima mumkin?",
                "choices": [
                    "Rasmga tegish",
                    "Ovqat yeyish",
                    "Surat olish (chiroqsiz)",
                    "Baland ovozda gaplashish",
                ],
                "answer": 2,
                "explanation": "“사진을 <b>찍어도 돼요</b>. 하지만 플래시를 "
                               "<b>쓰면 안 돼요</b>” — surat olish mumkin, "
                               "lekin chiroq bilan emas.",
            },
            {
                "text": "Nega Hana rad javobida “안 만져도 돼요” demadi?",
                "choices": [
                    "Chunki taqiq (으)면 안 되다 bilan beriladi",
                    "Chunki 만지다 notoʻgʻri feʼl",
                    "Chunki Dilnoza undan kichik",
                    "Ikkalasi ham toʻgʻri boʻlardi",
                ],
                "answer": 0,
                "explanation": "안 만져도 돼요 “tegmasangiz ham boʻladi” "
                               "degan boʻlardi — yaʼni ruxsat bermaslik "
                               "emas. Taqiq uchun qolip almashadi: "
                               "<b>만지면 안 돼요</b>.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "비가 올 것 같아요",
        "summary": (
            "PK-52 matni. Bekzod bilan Jasur osmonga qarab taxmin qilishadi — "
            "uch zamonda 것 같다, va oxirida qolipning madaniy vazifasi ham "
            "koʻrinadi."
        ),
        "order":   52,
        "grammar": [
            {
                "pattern":  "동사 + (으)ㄴ/는/(으)ㄹ 것 같다",
                "meaning":  "Taxmin: “…ga oʻxshaydi”. Zamonni ANIQLOVCHI "
                            "bildiradi: 온 것 (yoqqan), 오는 것 (yogʻayotgan), "
                            "올 것 (yogʻadigan). 같다 tuslanmaydi.",
                "examples": ["비가 올 것 같아요.", "지금 자는 것 같아요.",
                             "벌써 간 것 같아요."],
            },
            {
                "pattern":  "형용사 + (으)ㄴ 것 같다 · 명사 + 인 것 같다",
                "meaning":  "Sifat bilan (으)ㄴ — lekin bu HOZIRGI zamon: "
                            "매운 것 같아요 (“achchiqqa oʻxshaydi”). Ot bilan "
                            "이다 tuslanadi: 선생님인 것 같아요.",
                "examples": ["이 음식이 매운 것 같아요.",
                             "저분은 선생님인 것 같아요."],
            },
            {
                "pattern":  "것 같다 — fikrni yumshatish",
                "meaning":  "Koreyslar bilgan narsasini ham shu qolip bilan "
                            "aytadi, chunki qatʼiy hukm biroz keskin "
                            "eshitiladi. Ogʻzaki nutqda 것 → 거.",
                "examples": ["맛있는 것 같아요.", "좋은 거 같아요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Bekzod">베크조드</span> 씨와 <span class="cn-word" data-tr="Jasur">자수르</span> 씨가 <span class="cn-word" data-tr="tashqarida">밖에</span> 있어요. <span class="cn-word" data-tr="osmon">하늘</span>을 <span class="cn-word" data-pos="verb" data-tr="qarashyapti">보고 있어요</span>.</p>

<p><strong>베크조드:</strong> <span class="cn-word" data-tr="bulut">구름</span>이 <span class="cn-word" data-pos="adj" data-tr="qora">까매요</span>. 비가 <span class="cn-word" data-pos="verb" data-tr="yogʻadiganga oʻxshaydi">올 것 같아요</span>.</p>

<p><strong>자수르:</strong> <span class="cn-word" data-pos="adv" data-tr="haqiqatan">정말</span>이에요. <span class="cn-word" data-tr="soyabon">우산</span>을 <span class="cn-word" data-pos="verb" data-tr="olib kelishimiz kerak">가져와야 해요</span>. 하지만 제 우산이 <span class="cn-word" data-tr="uyda">집에</span> <span class="cn-word" data-pos="verb" data-tr="borga oʻxshaydi">있는 것 같아요</span>.</p>

<p><strong>베크조드:</strong> <span class="cn-word" data-tr="Afsona">아프소나</span> 씨는 우산이 있어요. <span class="cn-word" data-pos="adv" data-tr="hozir">지금</span> <span class="cn-word" data-tr="kutubxonada">도서관에</span> <span class="cn-word" data-pos="verb" data-tr="borga oʻxshaydi">있는 것 같아요</span>.</p>

<p>두 사람이 도서관에 갔어요. 하지만 아프소나 씨가 없어요.</p>

<p><strong>자수르:</strong> <span class="cn-word" data-pos="adv" data-tr="allaqachon">벌써</span> <span class="cn-word" data-pos="verb" data-tr="ketganga oʻxshaydi">간 것 같아요</span>.</p>

<p><strong>베크조드:</strong> <span class="cn-word" data-tr="anavi kishi">저분</span>은 <span class="cn-word" data-tr="oʻqituvchi boʻlsa kerak">선생님인 것 같아요</span>. <span class="cn-word" data-pos="verb" data-tr="soʻraylik">물어봐요</span>.</p>

<p><strong>선생님:</strong> 아프소나 씨요? <span class="cn-word" data-tr="oʻn daqiqa oldin">십 분 전에</span> 갔어요. 밖에 비가 <span class="cn-word" data-pos="verb" data-tr="yogʻayotganga oʻxshaydi">오는 것 같아요</span>. <span class="cn-word" data-pos="verb" data-tr="oʻtiring">앉으세요</span>.</p>

<p><strong>자수르:</strong> <span class="cn-word" data-pos="verb" data-tr="rahmat">고맙습니다</span>. 선생님, 이 <span class="cn-word" data-tr="kitob">책</span>이 <span class="cn-word" data-pos="adj" data-tr="qiyinga oʻxshaydi">어려운 것 같아요</span>.</p>

<p><strong>선생님:</strong> <span class="cn-word" data-pos="adv" data-tr="birinchida">처음에는</span> 어려워요. 하지만 <span class="cn-word" data-pos="adj" data-tr="qiziqarli">재미있어요</span>. 저도 <span class="cn-word" data-tr="yaxshiga oʻxshaydi">좋은 것 같아요</span>.</p>''',
        "questions": [
            {
                "text": "Nega Bekzod “비가 올 것 같아요” dedi?",
                "choices": [
                    "Chunki yomgʻir yogʻayotgan edi",
                    "Chunki bulut qora edi",
                    "Chunki Jasur shunday dedi",
                    "Chunki soyaboni bor edi",
                ],
                "answer": 1,
                "explanation": "“구름이 <b>까매요</b>. 비가 <b>올</b> 것 "
                               "같아요” — bulutga qarab taxmin qilyapti. "
                               "Hali yogʻmagani uchun (으)ㄹ.",
            },
            {
                "text": "Afsona qayerda?",
                "choices": [
                    "Kutubxonada",
                    "Uyda",
                    "Allaqachon ketgan",
                    "Oʻqituvchi bilan",
                ],
                "answer": 2,
                "explanation": "“벌써 <b>간</b> 것 같아요” va oʻqituvchi "
                               "tasdiqladi: “십 분 전에 갔어요”. Ish tugagan "
                               "→ (으)ㄴ 것 같다.",
            },
            {
                "text": "Oʻqituvchi kitobni yaxshi biladi. Nega baribir "
                        "“좋은 것 같아요” dedi?",
                "choices": [
                    "Fikrini yumshatish uchun",
                    "Chunki kitobni oʻqimagan",
                    "Chunki 좋아요 notoʻgʻri shakl",
                    "Chunki bu rasmiy shakl",
                ],
                "answer": 0,
                "explanation": "Koreys madaniyatida oʻz fikrini qatʼiy aytish "
                               "biroz keskin eshitiladi. Shuning uchun "
                               "bilgan narsani ham <b>것 같아요</b> bilan "
                               "aytish odat — bu grammatikadan koʻra "
                               "madaniyat masalasi.",
            },
        ],
    },
]
