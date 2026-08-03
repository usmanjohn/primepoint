# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-83 … PK-85.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Har uchala mashqda bitta 한다체 (PK-74) savoli bor.

Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_83_85.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "한국어",
    "description": "Koreys tili — grammatika va yozuv mashqlari",
    "icon":        "bi-translate",
    "color":       "#d97706",
}

DEFAULTS = {
    "level":                "medium",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}


# ══════════════════════════════════════════════════════════════════════
# PK-83 — 뿐이다 · 따름이다 · 에 불과하다
# ══════════════════════════════════════════════════════════════════════
Q_PK83 = [
    # 1–5 tanish
    {
        "text": "<p><b>(으)ㄹ 뿐이다</b> qanday maʼno beradi?</p>",
        "choices": ["Faqat …, xolos — bundan ortigʻi yoʻq",
                    "…gandan koʻra yaxshiroq",
                    "…ishi bilanoq",
                    "Xoh …, xoh …"],
        "correct": "Faqat …, xolos — bundan ortigʻi yoʻq",
        "explanation": "<p>Kamtarlik yoki oqlanish ohangi: “저는 제 일을 "
                       "했을 뿐이에요”.</p>",
    },
    {
        "text": "<p><b>뿐</b> sizga qaysi darsdan tanish?</p>",
        "choices": ["PK-67 — (으)ㄹ 뿐만 아니라",
                    "PK-52 — 것 같다",
                    "PK-63 — (으)ㄹ 뻔하다",
                    "PK-16 — 만"],
        "correct": "PK-67 — (으)ㄹ 뿐만 아니라",
        "explanation": "<p>Oʻshanda u “faqat emas, balki” ichida edi. "
                       "Endi yakka holda, gapning oxirida.</p>",
    },
    {
        "text": "<p><b>(으)ㄹ 따름이다</b> qaysi uslubga tegishli?</p>",
        "choices": ["Rasmiy yozma til, koʻpincha his-tuygʻu haqida",
                    "Kundalik suhbat",
                    "Bolalar tili",
                    "Faqat soʻroq gaplarda"],
        "correct": "Rasmiy yozma til, koʻpincha his-tuygʻu haqida",
        "explanation": "<p>감사할 따름입니다 · 놀랄 따름이었다. Doʻstga "
                       "aytilsa gʻalati eshitiladi.</p>",
    },
    {
        "text": "<p><b>에 불과하다</b> nimaga qoʻshiladi?</p>",
        "choices": ["Faqat otga", "Faqat feʼlga", "Faqat sifatga",
                    "Har qanday soʻzga"],
        "correct": "Faqat otga",
        "explanation": "<p>변명<b>에</b> 불과하다 · 시작<b>에</b> 불과하다 · "
                       "열 살<b>에</b> 불과했다.</p>",
    },
    {
        "text": "<p><b>불과</b> (不過) ning maʼnosi nima?</p>",
        "choices": ["“Oshib ketmaydi” — chegarani belgilaydi",
                    "“Bogʻlanmasdan”", "“Toʻxtamasdan”", "“Yetarli”"],
        "correct": "“Oshib ketmaydi” — chegarani belgilaydi",
        "explanation": "<p>Shuning uchun ohangi koʻpincha kamsituvchi "
                       "yoki rad etuvchi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 저는 제 일을 <b>____</b> 뿐이에요. "
                "(하다 — oʻtgan zamon)</p>",
        "choices": ["했을", "하을", "하는", "할"],
        "correct": "했을",
        "explanation": "<p>Boʻlib oʻtgan ish — <b>았/었을 뿐이다</b>. "
                       "❌ 하을 degan shakl yoʻq.</p>",
    },
    {
        "text": "<p>Toʻldiring: 그건 <b>____</b> 뿐이에요. 화내지 마세요. "
                "(농담)</p>",
        "choices": ["농담일", "농담", "농담의", "농담이"],
        "correct": "농담일",
        "explanation": "<p>Ot bilan <b>일</b> kerak — 이다 ning "
                       "aniqlovchi shakli.</p>",
    },
    {
        "text": "<p>Toʻldiring: 그것은 변명<b>____</b> 불과하다.</p>",
        "choices": ["에", "을", "이", "으로"],
        "correct": "에",
        "explanation": "<p>명사 + <b>에 불과하다</b>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 그 사람은 아무 말도 없이 <b>____</b> "
                "뿐이었어요. (웃다)</p>",
        "choices": ["웃을", "웃은", "웃는", "웃어"],
        "correct": "웃을",
        "explanation": "<p>뿐이다 oldida <b>(으)ㄹ</b> aniqlovchisi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 도와주셔서 <b>____</b> 따름입니다. "
                "(감사하다)</p>",
        "choices": ["감사할", "감사한", "감사해", "감사했을"],
        "correct": "감사할",
        "explanation": "<p>따름이다 oldida ham <b>(으)ㄹ</b> "
                       "aniqlovchisi.</p>",
    },
    {
        "text": "<p>“Oʻshanda u bor-yoʻgʻi oʻn yoshda edi” — "
                "koreyschada?</p>",
        "choices": ["그때 그는 열 살에 불과했다.",
                    "그때 그는 열 살일 뿐이었다.",
                    "그때 그는 열 살만 있었다.",
                    "그때 그는 열 살에 따름이었다."],
        "correct": "그때 그는 열 살에 불과했다.",
        "explanation": "<p>에 불과하다 <b>raqam</b> bilan juda koʻp "
                       "ishlatiladi.</p>",
    },
    {
        "text": "<p>Bu gapni 한다체 ga oʻgiring (PK-74): "
                "저는 제 일을 했을 뿐이에요.</p>",
        "choices": ["나는 내 일을 했을 뿐이다.",
                    "나는 내 일을 했을 뿐인다.",
                    "저는 제 일을 했을 뿐이었다.",
                    "나는 내 일을 하을 뿐이다."],
        "correct": "나는 내 일을 했을 뿐이다.",
        "explanation": "<p>이다 한다체 da <b>이다</b> boʻlib qoladi, va "
                       "저/제 oʻrniga 나/내.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><b>만</b> (PK-16) va <b>(으)ㄹ 뿐이다</b> farqi nima?</p>",
        "choices": ["만 tanlaydi (boshqalar orasidan bittasini); 뿐이다 "
                    "kamaytiradi (“bundan ortigʻi yoʻq”)",
                    "만 — oʻtgan zamon; 뿐이다 — hozirgi",
                    "만 — rasmiy; 뿐이다 — ogʻzaki",
                    "Farqi yoʻq"],
        "correct": "만 tanlaydi (boshqalar orasidan bittasini); 뿐이다 "
                   "kamaytiradi (“bundan ortigʻi yoʻq”)",
        "explanation": "<p>커피<b>만</b> 마셔요 (choy emas, kofe) ↔ "
                       "커피를 마셨<b>을 뿐이에요</b> (boshqa hech narsa "
                       "qilmadim).</p>",
    },
    {
        "text": "<p>“저는 커피만 마셨을 뿐이에요” — bu jumla toʻgʻrimi?</p>",
        "choices": ["Ha — 만 tanlaydi, 뿐이다 esa “boshqa hech narsa yoʻq” "
                    "deb yopadi",
                    "Yoʻq — ikkalasini birga ishlatib boʻlmaydi",
                    "Yoʻq — 만 olib tashlanishi kerak",
                    "Yoʻq — 뿐이다 olib tashlanishi kerak"],
        "correct": "Ha — 만 tanlaydi, 뿐이다 esa “boshqa hech narsa yoʻq” "
                   "deb yopadi",
        "explanation": "<p>Bu juda tabiiy birikma va koreys tilida koʻp "
                       "uchraydi.</p>",
    },
    {
        "text": "<p>Doʻstingizga “shunchaki qorningiz ochqagan” demoqchisiz. "
                "Qaysi qolip?</p>",
        "choices": ["배고플 뿐이야", "배고플 따름이야",
                    "배고픔에 불과해", "배고플 뿐만 아니야"],
        "correct": "배고플 뿐이야",
        "explanation": "<p>따름이다 — <b>rasmiy yozma</b>. Doʻst bilan "
                       "gapirganda <b>뿐이다</b>.</p>",
    },
    {
        "text": "<p>Qaysi jumla notoʻgʻri?</p>",
        "choices": ["그건 농담 뿐이에요.", "그건 농담일 뿐이에요.",
                    "그것은 변명에 불과하다.", "감사할 따름입니다."],
        "correct": "그건 농담 뿐이에요.",
        "explanation": "<p>Ot bilan <b>일</b> kerak: 농담<b>일</b> "
                       "뿐이에요.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <s>그것은 변명일 뿐과하다.</s></p>",
        "choices": ["불과하다 ot bilan 에 orqali ulanadi — 변명에 불과하다",
                    "변명 emas, 변명이",
                    "그것은 emas, 그것이",
                    "불과하다 emas, 불과이다"],
        "correct": "불과하다 ot bilan 에 orqali ulanadi — 변명에 불과하다",
        "explanation": "<p>뿐이다 va 불과하다 — ikki xil qolip, "
                       "aralashtirib boʻlmaydi.</p>",
    },
    {
        "text": "<p>Xatoni toping: <s>저는 제 일을 하을 뿐이에요.</s></p>",
        "choices": ["하다 → 했을 (oʻtgan) yoki 할 (hozirgi) — 하을 degan "
                    "shakl yoʻq",
                    "제 일을 emas, 제 일이",
                    "뿐이에요 emas, 뿐이다",
                    "저는 emas, 제가"],
        "correct": "하다 → 했을 (oʻtgan) yoki 할 (hozirgi) — 하을 degan "
                   "shakl yoʻq",
        "explanation": "<p>하 da 받침 yoʻq, shuning uchun 을 emas, "
                       "<b>ㄹ</b> qoʻshiladi: 할.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>“Bu hali boshlanishi xolos” — koreyschada?</p>",
        "choices": ["이것은 시작에 불과하다.", "이것은 시작일 따름이다.",
                    "이것은 시작만 하다.", "이것은 시작할 뿐이다."],
        "correct": "이것은 시작에 불과하다.",
        "explanation": "<p>Ot + 에 불과하다 — baho beruvchi qolip. Bu "
                       "jumla TOPIK 읽기 da juda koʻp uchraydi.</p>",
    },
    {
        "text": "<p>Rasmiy nutqda “yordam berganingiz uchun minnatdorman, "
                "xolos” — koreyschada?</p>",
        "choices": ["도와주셔서 감사할 따름입니다.",
                    "도와주셔서 감사할 뿐이야.",
                    "도와주셔서 감사에 불과합니다.",
                    "도와주셔서 감사만 합니다."],
        "correct": "도와주셔서 감사할 따름입니다.",
        "explanation": "<p>따름이다 aynan shunday rasmiy minnatdorchilik "
                       "uchun yaratilgandek.</p>",
    },
]


# ══════════════════════════════════════════════════════════════════════
# PK-84 — 든지 든지, 건 건
# ══════════════════════════════════════════════════════════════════════
Q_PK84 = [
    # 1–5 tanish
    {
        "text": "<p><b>거나</b> qanday maʼno beradi?</p>",
        "choices": ["Yoki — feʼl va sifatlarni bogʻlaydi",
                    "Xoh …, xoh …", "Va", "Lekin"],
        "correct": "Yoki — feʼl va sifatlarni bogʻlaydi",
        "explanation": "<p>책을 읽<b>거나</b> 영화를 봐요. Otlar uchun esa "
                       "<b>(이)나</b>: 커피나 차.</p>",
    },
    {
        "text": "<p><b>든지 … 든지</b> nimani bildiradi?</p>",
        "choices": ["Tanlovning ahamiyati yoʻq — qaysi biri boʻlsa ham "
                    "natija bir xil",
                    "Ikkitasidan bittasini tanlash kerak",
                    "Ikkalasi ham taqiqlangan",
                    "Ikkalasi birga boʻlishi kerak"],
        "correct": "Tanlovning ahamiyati yoʻq — qaysi biri boʻlsa ham "
                   "natija bir xil",
        "explanation": "<p>가든지 안 가든지 마음대로 하세요 — “xoh boring, "
                       "xoh bormang”.</p>",
    },
    {
        "text": "<p>Bu qolip nechta variant talab qiladi?</p>",
        "choices": ["Ikkita — u juft ishlaydi", "Bitta",
                    "Uchta", "Cheklov yoʻq"],
        "correct": "Ikkita — u juft ishlaydi",
        "explanation": "<p>❌ 가든지 마음대로 하세요 → ✅ "
                       "<b>가든지 안 가든지</b>.</p>",
    },
    {
        "text": "<p>Soʻroq soʻziga qoʻshilganda 든지 nima beradi?</p>",
        "choices": ["“Har qanday” maʼnosi: 뭐든지, 누구든지, 언제든지",
                    "Inkor maʼnosi", "Buyruq maʼnosi",
                    "Oʻtgan zamon maʼnosi"],
        "correct": "“Har qanday” maʼnosi: 뭐든지, 누구든지, 언제든지",
        "explanation": "<p>언제든지 연락하세요 — “istalgan vaqtda "
                       "bogʻlaning”.</p>",
    },
    {
        "text": "<p><b>하든 말든</b> dagi 말다 nima qiladi?</p>",
        "choices": ["Ikkinchi qismda inkorni beradi — “qilsa ham, qilmasa "
                    "ham”",
                    "Gapni rasmiy qiladi",
                    "Oʻtgan zamon yasaydi",
                    "Hurmat bildiradi"],
        "correct": "Ikkinchi qismda inkorni beradi — “qilsa ham, qilmasa "
                   "ham”",
        "explanation": "<p>가든 말든 · 하든 말든 · 먹든 말든 — eng koʻp "
                       "uchraydigan juftlik.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: <b>____</b> 안 가든지 마음대로 하세요. "
                "(가다)</p>",
        "choices": ["가든지", "갔든지", "가는든지", "갈든지"],
        "correct": "가든지",
        "explanation": "<p>Oʻzak + 든지, zamon yoʻq.</p>",
    },
    {
        "text": "<p>Toʻldiring: <b>____</b> 선생님이든지 규칙은 같아요. "
                "(학생)</p>",
        "choices": ["학생이든지", "학생든지", "학생일든지", "학생의든지"],
        "correct": "학생이든지",
        "explanation": "<p>받침 bor otda <b>이든지</b>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 주말에는 책을 <b>____</b> 영화를 봐요. "
                "(읽다)</p>",
        "choices": ["읽거나", "읽든지", "읽으나", "읽건"],
        "correct": "읽거나",
        "explanation": "<p>Bu yerda haqiqiy <b>tanlov</b> bor — "
                       "<b>거나</b>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 그 사람이 <b>____</b> 말든 저는 갈 거예요. "
                "(오다)</p>",
        "choices": ["오든", "왔든", "올든", "오는든"],
        "correct": "오든",
        "explanation": "<p>Qisqa shakl <b>든</b> + 말든 — “kelsa ham, "
                       "kelmasa ham”.</p>",
    },
    {
        "text": "<p>“Istalgan vaqtda bogʻlaning” — koreyschada?</p>",
        "choices": ["언제든지 연락하세요.", "언제거나 연락하세요.",
                    "언제나 마나 연락하세요.", "언제일 뿐 연락하세요."],
        "correct": "언제든지 연락하세요.",
        "explanation": "<p>Soʻroq soʻzi + 든지 = “har qanday”.</p>",
    },
    {
        "text": "<p>Toʻldiring: <b>____</b> 작건 상관없어요. (크다)</p>",
        "choices": ["크건", "컸건", "클건", "크는건"],
        "correct": "크건",
        "explanation": "<p><b>건 … 건</b> — 든 든 ning keskinroq "
                       "varianti.</p>",
    },
    {
        "text": "<p>Bu gapni 한다체 ga oʻgiring (PK-74): "
                "날씨가 좋든지 나쁘든지 우리는 출발해요.</p>",
        "choices": ["날씨가 좋든지 나쁘든지 우리는 출발한다.",
                    "날씨가 좋든지 나쁘든지 우리는 출발하는다.",
                    "날씨가 좋든지 나쁘든지 우리는 출발했다.",
                    "날씨가 좋든지 나쁘든지 우리는 출발하다."],
        "correct": "날씨가 좋든지 나쁘든지 우리는 출발한다.",
        "explanation": "<p>출발하 da 받침 yoʻq → <b>ㄴ다</b>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><b>거나</b> va <b>든지 … 든지</b> farqi nima?</p>",
        "choices": ["거나 — tanlov bor; 든지 든지 — tanlov ahamiyatsiz",
                    "거나 — oʻtgan zamon; 든지 — kelasi zamon",
                    "거나 — ot bilan; 든지 — feʼl bilan",
                    "Farqi yoʻq"],
        "correct": "거나 — tanlov bor; 든지 든지 — tanlov ahamiyatsiz",
        "explanation": "<p>커피를 마시<b>거나</b> 차를 마셔요 (bittasini "
                       "tanlayman) ↔ 마시<b>든지</b> … 마시<b>든지</b> "
                       "상관없어요 (farqi yoʻq).</p>",
    },
    {
        "text": "<p>Qaysi jumla notoʻgʻri?</p>",
        "choices": ["가든지 마음대로 하세요.",
                    "가든지 안 가든지 마음대로 하세요.",
                    "학생이든지 선생님이든지 규칙은 같아요.",
                    "크건 작건 상관없어요."],
        "correct": "가든지 마음대로 하세요.",
        "explanation": "<p>Qolip <b>juft</b> ishlaydi — ikkita variant "
                       "kerak.</p>",
    },
    {
        "text": "<p><b>가든 말든</b> iborasining ohangi qanday?</p>",
        "choices": ["“Menga qizigʻi yoʻq” — shuning uchun oʻzidan kattaga "
                    "aytilmaydi",
                    "Juda hurmatli",
                    "Rasmiy va sovuq",
                    "Iltimos ohangi"],
        "correct": "“Menga qizigʻi yoʻq” — shuning uchun oʻzidan kattaga "
                   "aytilmaydi",
        "explanation": "<p>Qisqa shakllar (든, 건) keskinroq eshitiladi.</p>",
    },
    {
        "text": "<p>“Bu kutubxonadan har kim foydalana oladi” — "
                "koreyschada?</p>",
        "choices": ["이 도서관은 누구든지 이용할 수 있다.",
                    "이 도서관은 누구거나 이용할 수 있다.",
                    "이 도서관은 누구나 마나 이용할 수 있다.",
                    "이 도서관은 누구일 뿐 이용할 수 있다."],
        "correct": "이 도서관은 누구든지 이용할 수 있다.",
        "explanation": "<p>누구 + 든지 = “kim boʻlsa ham, har kim”.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <s>학생든지 선생님든지 규칙은 "
                "같아요.</s></p>",
        "choices": ["받침 bor otda 이든지 — 학생이든지 선생님이든지",
                    "규칙은 emas, 규칙이",
                    "같아요 emas, 같다",
                    "든지 emas, 거나"],
        "correct": "받침 bor otda 이든지 — 학생이든지 선생님이든지",
        "explanation": "<p>학생 va 선생님 — ikkalasida ham 받침 bor.</p>",
    },
    {
        "text": "<p>Xatoni toping: <s>갔든지 안 갔든지 마음대로 "
                "하세요.</s></p>",
        "choices": ["든지 oldida zamon boʻlmaydi — 가든지 안 가든지",
                    "마음대로 emas, 마음으로",
                    "하세요 emas, 해요",
                    "안 emas, 못"],
        "correct": "든지 oldida zamon boʻlmaydi — 가든지 안 가든지",
        "explanation": "<p>Ish hali qilinmagan — u faqat variant sifatida "
                       "turibdi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>“Ob-havo yaxshi boʻladimi, yomonmi — biz yoʻlga "
                "chiqamiz” — koreyschada?</p>",
        "choices": ["날씨가 좋든지 나쁘든지 우리는 출발한다.",
                    "날씨가 좋거나 나쁘거나 우리는 출발한다.",
                    "날씨가 좋으나 마나 우리는 출발한다.",
                    "날씨가 좋을 뿐 우리는 출발한다."],
        "correct": "날씨가 좋든지 나쁘든지 우리는 출발한다.",
        "explanation": "<p>Ikkita qarama-qarshi variant — va ikkalasi ham "
                       "qarorni oʻzgartirmaydi.</p>",
    },
    {
        "text": "<p>“U kelsa ham, kelmasa ham men boraman” (qisqa "
                "shaklda) — koreyschada?</p>",
        "choices": ["그 사람이 오든 말든 저는 갈 거예요.",
                    "그 사람이 오거나 말거나 저는 갈 거예요.",
                    "그 사람이 오나 마나 저는 갈 거예요.",
                    "그 사람이 올 뿐 저는 갈 거예요."],
        "correct": "그 사람이 오든 말든 저는 갈 거예요.",
        "explanation": "<p><b>하든 말든</b> qolipining aniq namunasi: "
                       "말다 ikkinchi qismda inkorni beradi.</p>",
    },
]


# ══════════════════════════════════════════════════════════════════════
# PK-85 — (느)니 차라리, (으)나 마나
# ══════════════════════════════════════════════════════════════════════
Q_PK85 = [
    # 1–5 tanish
    {
        "text": "<p><b>A(느)니 차라리 B</b> qanday maʼno beradi?</p>",
        "choices": ["A ni qilgandan koʻra B yaxshiroq",
                    "A ham B ham yaxshi",
                    "A dan keyin B",
                    "A boʻlsa ham B qilaman"],
        "correct": "A ni qilgandan koʻra B yaxshiroq",
        "explanation": "<p>Bu — kamroq yomonini tanlash.</p>",
    },
    {
        "text": "<p>(느)니 차라리 da ikki variant qanday boʻladi?</p>",
        "choices": ["Ikkalasi ham yoqimsiz — soʻzlovchi kamroq yomonini "
                    "tanlaydi",
                    "Ikkalasi ham yaxshi",
                    "Birinchisi yaxshi, ikkinchisi yomon",
                    "Ikkalasi ham betaraf"],
        "correct": "Ikkalasi ham yoqimsiz — soʻzlovchi kamroq yomonini "
                   "tanlaydi",
        "explanation": "<p>Shuning uchun 차라리 (“koʻra, aksincha”) "
                       "yoniga keladi.</p>",
    },
    {
        "text": "<p><b>(으)나 마나</b> ichida qaysi feʼl turibdi?</p>",
        "choices": ["말다 — “qilmaslik”", "마시다 — “ichmoq”",
                    "만나다 — “uchrashmoq”", "많다 — “koʻp”"],
        "correct": "말다 — “qilmaslik”",
        "explanation": "<p>Shuning uchun maʼnosi “qilsa ham, "
                       "<b>qilmasa</b> ham”.</p>",
    },
    {
        "text": "<p>(으)나 마나 nimani bildiradi?</p>",
        "choices": ["Natija oldindan maʼlum — qilishning hojati yoʻq",
                    "Ish juda qiyin",
                    "Ish taqiqlangan",
                    "Ishni albatta qilish kerak"],
        "correct": "Natija oldindan maʼlum — qilishning hojati yoʻq",
        "explanation": "<p>보나 마나 그 사람이 이길 것이다 — “qaramasam ham "
                       "bilaman”.</p>",
    },
    {
        "text": "<p>(느)니 qaysi soʻz turkumi bilan ishlatiladi?</p>",
        "choices": ["Faqat feʼl", "Faqat sifat", "Feʼl va sifat",
                    "Ot bilan ham"],
        "correct": "Faqat feʼl",
        "explanation": "<p>Sifat bilan ❌. Eʼtibor bering: 나쁘<b>니</b> "
                       "butunlay boshqa narsa — “yomon boʻlgani "
                       "uchun”.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 이렇게 <b>____</b> 차라리 걸어가는 것이 "
                "낫다. (기다리다)</p>",
        "choices": ["기다리느니", "기다렸느니", "기다릴느니", "기다리니"],
        "correct": "기다리느니",
        "explanation": "<p>Oʻzak + 느니, oldida zamon yoʻq.</p>",
    },
    {
        "text": "<p>Toʻldiring: 이 약은 <b>____</b> 마나 효과가 없어요. "
                "(먹다)</p>",
        "choices": ["먹으나", "먹나", "먹어나", "먹는나"],
        "correct": "먹으나",
        "explanation": "<p>먹 da 받침 bor → <b>으나 마나</b>.</p>",
    },
    {
        "text": "<p>Toʻldiring: <b>____</b> 마나 그 사람이 이길 것이다. "
                "(보다)</p>",
        "choices": ["보나", "보으나", "본나", "볼나"],
        "correct": "보나",
        "explanation": "<p>보 da 받침 yoʻq → <b>나 마나</b>. "
                       "<b>보나 마나</b> — tayyor ibora.</p>",
    },
    {
        "text": "<p>Toʻldiring: 그 일을 <b>____</b> 차라리 그만두는 것이 "
                "낫다. (하다)</p>",
        "choices": ["하느니", "했느니", "할느니", "하니"],
        "correct": "하느니",
        "explanation": "<p>(느)니 oldida zamon qoʻyilmaydi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 물어보나 마나 대답은 <b>____</b>.</p>",
        "choices": ["똑같아요", "달라요", "좋아요", "새로워요"],
        "correct": "똑같아요",
        "explanation": "<p>나 마나 dan keyin “natija bir xil” degan "
                       "xulosa keladi.</p>",
    },
    {
        "text": "<p>“Urishgan doʻstga birinchi boʻlib yozgandan koʻra "
                "kutganim yaxshiroq” — koreyschada?</p>",
        "choices": ["먼저 연락하느니 차라리 기다리는 것이 낫다.",
                    "먼저 연락했느니 차라리 기다린다.",
                    "먼저 연락하나 마나 기다리는 것이 낫다.",
                    "먼저 연락해 봤자 기다리는 것이 낫다."],
        "correct": "먼저 연락하느니 차라리 기다리는 것이 낫다.",
        "explanation": "<p>Ikkala variant ham yoqimsiz — bu aynan "
                       "(느)니 차라리 ning oʻrni.</p>",
    },
    {
        "text": "<p>Bu gapni 한다체 ga oʻgiring (PK-74): "
                "물어보나 마나 대답은 똑같아요.</p>",
        "choices": ["물어보나 마나 대답은 똑같다.",
                    "물어보나 마나 대답은 똑같는다.",
                    "물어보나 마나 대답은 똑같았다.",
                    "물어보나 마나 대답은 똑같이다."],
        "correct": "물어보나 마나 대답은 똑같다.",
        "explanation": "<p>똑같다 — <b>sifat</b>, 한다체 da lugʻat "
                       "shaklida qoladi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><b>아/어 봤자</b> (PK-80) va <b>(으)나 마나</b> farqi "
                "nima?</p>",
        "choices": ["봤자 — harakat behuda; 나 마나 — natija oldindan "
                    "maʼlum, tekshirishning hojati yoʻq",
                    "봤자 — kelajak; 나 마나 — oʻtmish",
                    "봤자 — yozma; 나 마나 — ogʻzaki",
                    "Farqi yoʻq"],
        "correct": "봤자 — harakat behuda; 나 마나 — natija oldindan "
                   "maʼlum, tekshirishning hojati yoʻq",
        "explanation": "<p>“Yugursang ham ulgurmaysan” → 봤자. "
                       "“Qaramasam ham bilaman” → 나 마나.</p>",
    },
    {
        "text": "<p>“Qaramasam ham bilaman — u yutadi” — qaysi qolip?</p>",
        "choices": ["보나 마나 그 사람이 이길 거예요.",
                    "봐 봤자 그 사람이 이길 거예요.",
                    "보느니 차라리 그 사람이 이길 거예요.",
                    "보든 말든 그 사람이 이길 거예요."],
        "correct": "보나 마나 그 사람이 이길 거예요.",
        "explanation": "<p>Natija <b>oldindan maʼlum</b> — 나 마나.</p>",
    },
    {
        "text": "<p>Qaysi jumla notoʻgʻri?</p>",
        "choices": ["날씨가 나쁘느니 차라리 집에 있는 것이 낫다.",
                    "밖에 나가느니 차라리 집에 있는 것이 낫다.",
                    "그 일을 하느니 차라리 그만두는 것이 낫다.",
                    "이렇게 기다리느니 차라리 걸어가는 것이 낫다."],
        "correct": "날씨가 나쁘느니 차라리 집에 있는 것이 낫다.",
        "explanation": "<p>나쁘다 — <b>sifat</b>. (느)니 faqat feʼl "
                       "bilan.</p>",
    },
    {
        "text": "<p>(느)니 차라리 dan keyin ikkinchi gapda koʻpincha nima "
                "keladi?</p>",
        "choices": ["…는 것이 낫다", "…기 십상이다",
                    "…에 불과하다", "…을 뿐이다"],
        "correct": "…는 것이 낫다",
        "explanation": "<p>낫다 = “yaxshiroq”. Oʻzbekcha “afzal / yaxshi” "
                       "ham xuddi shu oʻrinda turadi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <s>그 일을 했느니 차라리 "
                "그만두는 것이 낫다.</s></p>",
        "choices": ["(느)니 oldida zamon boʻlmaydi — 하느니",
                    "그만두는 emas, 그만둔",
                    "차라리 olib tashlanishi kerak",
                    "낫다 emas, 좋다"],
        "correct": "(느)니 oldida zamon boʻlmaydi — 하느니",
        "explanation": "<p>Ish hali qilinmagan — u faqat rad etilayotgan "
                       "variant.</p>",
    },
    {
        "text": "<p>Xatoni toping: <s>먹나 마나 효과가 없어요.</s></p>",
        "choices": ["먹 da 받침 bor — 먹으나 마나",
                    "효과가 emas, 효과를",
                    "없어요 emas, 없다",
                    "마나 emas, 말나"],
        "correct": "먹 da 받침 bor — 먹으나 마나",
        "explanation": "<p>받침 yoʻq → 나 마나 (보나 마나), 받침 bor → "
                       "으나 마나 (먹으나 마나).</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>“U ishni qilgandan koʻra tashlab qoʻygan yaxshiroq” — "
                "koreyschada?</p>",
        "choices": ["그 일을 하느니 차라리 그만두는 것이 낫다.",
                    "그 일을 하나 마나 그만두는 것이 낫다.",
                    "그 일을 해 봤자 그만두는 것이 낫다.",
                    "그 일을 하든 말든 그만두는 것이 낫다."],
        "correct": "그 일을 하느니 차라리 그만두는 것이 낫다.",
        "explanation": "<p>Ikkalasi ham yoqimsiz, lekin ikkinchisi "
                       "afzalroq — (느)니 차라리.</p>",
    },
    {
        "text": "<p>“Soʻrasangiz ham, soʻramasangiz ham javob bir xil” — "
                "koreyschada?</p>",
        "choices": ["물어보나 마나 대답은 똑같아요.",
                    "물어봐 봤자 대답은 똑같아요.",
                    "물어보느니 차라리 대답은 똑같아요.",
                    "물어보든 말든 대답은 똑같아요."],
        "correct": "물어보나 마나 대답은 똑같아요.",
        "explanation": "<p>“Soʻrash” va “soʻramaslik” — ikkala yoʻl ham "
                       "bir xil natijaga olib keladi. Bu 나 마나 ning "
                       "aniq taʼrifi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-83 Mashq: 뿐이다 · 따름이다 · 에 불과하다",
        "description": "20 savol — “xolos” ning uch shakli, ot bilan 일 "
                       "qoidasi, 만 dan farqi va uslub tanlash.",
        "tutorial":    "PK-83:",
        "level":       "medium",
        "questions":   Q_PK83,
    },
    {
        "title":       "PK-84 Mashq: 든지 든지 · 건 건",
        "description": "20 savol — 거나 bilan farqi, juft ishlash qoidasi, "
                       "(이)든지, soʻroq soʻzlari bilan “har qanday” va "
                       "하든 말든.",
        "tutorial":    "PK-84:",
        "level":       "medium",
        "questions":   Q_PK84,
    },
    {
        "title":       "PK-85 Mashq: (느)니 차라리 · (으)나 마나",
        "description": "20 savol — kamroq yomonini tanlash, faqat feʼl "
                       "sharti, 받침 boʻyicha 나/으나 va 봤자 dan farqi.",
        "tutorial":    "PK-85:",
        "level":       "medium",
        "questions":   Q_PK85,
    },
]
