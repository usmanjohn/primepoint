# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-71 … PK-73.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_71_73.py --master=prime \\
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


# =====================================================================
# PK-71 — (으)ㄹ 겸, 고자
# =====================================================================

Q_PK71 = [
    # 1–5 tanish
    {
        "text": "<p><strong>(으)ㄹ 겸</strong> nimani bildiradi?</p>",
        "choices": ["Bitta ish, ikkita maqsad", "Ikki tomonni qiyoslash",
                    "Kutilmagan xalaqit", "Bajarilmagan majburiyat"],
        "correct": "Bitta ish, ikkita maqsad",
        "explanation": "<p>Oʻzbekchada — “<strong>bir yoʻla</strong> u ham "
                       "boʻlsin, bu ham boʻlsin”.</p>",
    },
    {
        "text": "<p><strong>겸</strong> soʻzi grammatik jihatdan nima?</p>",
        "choices": ["Feʼl", "Ot", "Ravish", "Qoʻshimcha"],
        "correct": "Ot",
        "explanation": "<p>Yettinchi <strong>aniqlovchi + ot</strong>: "
                       "것 · 줄 · 뻔 · 테 · 뿐 · 데 · 겸. Shuning uchun "
                       "oldida (으)ㄹ turadi.</p>",
    },
    {
        "text": "<p><strong>고자</strong> qaysi uslubga tegishli?</p>",
        "choices": ["Kundalik ogʻzaki nutq", "Rasmiy va yozma matn",
                    "Faqat doʻstlar orasida", "Faqat savol gaplarda"],
        "correct": "Rasmiy va yozma matn",
        "explanation": "<p>Ariza, maqola, rasmiy nutq. Kundalik gapda "
                       "<strong>(으)려고</strong> eshitiladi.</p>",
    },
    {
        "text": "<p><strong>아침 겸 점심</strong> nima degani?</p>",
        "choices": ["Nonushtadan keyingi tushlik",
                    "Nonushta ham, tushlik ham boʻladigan ovqat",
                    "Nonushtasiz tushlik",
                    "Ikki marta ovqatlanish"],
        "correct": "Nonushta ham, tushlik ham boʻladigan ovqat",
        "explanation": "<p>Ot bilan <strong>겸</strong> ikki vazifani "
                       "bildiradi: 거실 겸 서재, 가수 겸 배우.</p>",
    },
    {
        "text": "<p><strong>고자</strong> qaysi uslub bilan yuradi?</p>",
        "choices": ["해요체", "습니다체", "반말", "Farqi yoʻq"],
        "correct": "습니다체",
        "explanation": "<p>한국어를 배우고자 한국에 "
                       "<strong>왔습니다</strong> — rasmiy qolip rasmiy "
                       "uslub bilan.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 운동도 <strong>______</strong> 겸 친구도 "
                "만날 겸 공원에 갔어요. (하다)</p>",
        "choices": ["하는", "한", "할", "하기"],
        "correct": "할",
        "explanation": "<p>겸 — ot, oldida <strong>(으)ㄹ</strong> "
                       "aniqlovchisi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 바람도 <strong>______</strong> 겸 밖에 "
                "나갔어요. (쐬다)</p>",
        "choices": ["쐬는", "쐴", "쐰", "쐬기"],
        "correct": "쐴",
        "explanation": "<p>쐬 da 받침 yoʻq → <strong>쐴 겸</strong> — "
                       "“havo ham olay deb”.</p>",
    },
    {
        "text": "<p>Toʻldiring: 저는 한국어를 <strong>______</strong> "
                "한국에 왔습니다. (배우다 + 고자)</p>",
        "choices": ["배웠고자", "배우고자", "배울고자", "배우기고자"],
        "correct": "배우고자",
        "explanation": "<p>고자 dan oldin <strong>zamon qoʻshimchasi "
                       "qoʻyilmaydi</strong>.</p>",
    },
    {
        "text": "<p>“Men shifokor boʻlish niyatidaman” — qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["저는 의사가 되고자 합니다",
                    "저는 의사가 될 겸 합니다",
                    "저는 의사가 됐고자 합니다",
                    "저는 의사가 되기 고자 합니다"],
        "correct": "저는 의사가 되고자 합니다",
        "explanation": "<p><strong>고자 하다</strong> — “…moqchiman” ning "
                       "rasmiy shakli.</p>",
    },
    {
        "text": "<p>Toʻldiring: 늦게 일어나서 <strong>______</strong>을 "
                "먹었어요.</p>",
        "choices": ["아침 겸 점심", "아침을 겸 점심", "아침 겸의 점심",
                    "아침이 겸 점심"],
        "correct": "아침 겸 점심",
        "explanation": "<p>Ot bilan 겸 <strong>qoʻshimchasiz</strong> "
                       "ikkita otni bogʻlaydi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 이 문제를 <strong>______</strong> 많이 "
                "노력했습니다. (해결하다 + 고자)</p>",
        "choices": ["해결하고자", "해결했고자", "해결할고자", "해결하려고자"],
        "correct": "해결하고자",
        "explanation": "<p>Oʻzak + <strong>고자</strong>, zamonsiz.</p>",
    },
    {
        "text": "<p>“Bir yoʻla koreys tilini ham oʻrganay, madaniyatni ham "
                "koʻray deb bordim” — qaysi biri toʻgʻri?</p>",
        "choices": ["한국어도 배우 겸 문화도 보 겸 갔어요",
                    "한국어도 배울 겸 문화도 볼 겸 갔어요",
                    "한국어도 배우고자 문화도 보고자 갔어요",
                    "한국어도 배우기 겸 문화도 보기 겸 갔어요"],
        "correct": "한국어도 배울 겸 문화도 볼 겸 갔어요",
        "explanation": "<p>Ikki marta takrorlangan <strong>(으)ㄹ 겸</strong> "
                       "— eng koʻp uchraydigan shakli.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p><strong>고자</strong> va <strong>(으)려고</strong> farqi "
                "nimada?</p>",
        "choices": ["Maʼnosi bir xil, farq uslubda: 고자 rasmiy va yozma",
                    "고자 kundalik, (으)려고 rasmiy",
                    "고자 oʻtgan zamon uchun",
                    "(으)려고 faqat sifat bilan"],
        "correct": "Maʼnosi bir xil, farq uslubda: 고자 rasmiy va yozma",
        "explanation": "<p>TOPIK 쓰기 da 고자 uslubni koʻtaradi; 듣기 da "
                       "esa (으)려고 eshitiladi.</p>",
    },
    {
        "text": "<p>Nima uchun <strong>한국어를 배우고자 한국에 가세요</strong> "
                "notoʻgʻri?</p>",
        "choices": ["Zamon xato",
                    "고자 dan keyin buyruq kelmaydi",
                    "배우다 feʼl emas",
                    "받침 xato"],
        "correct": "고자 dan keyin buyruq kelmaydi",
        "explanation": "<p>고자 ning uch sharti: bir xil ega · zamon yoʻq · "
                       "keyin <strong>buyruq va taklif yoʻq</strong>.</p>",
    },
    {
        "text": "<p>(으)ㄹ 겸 gapida oxirgi feʼl odatda qanday boʻladi?</p>",
        "choices": ["Ikkita alohida feʼl",
                    "Bitta feʼl — ikkala maqsad bitta harakatga sigʻadi",
                    "Har doim buyruq",
                    "Har doim kelasi zamon"],
        "correct": "Bitta feʼl — ikkala maqsad bitta harakatga sigʻadi",
        "explanation": "<p>갔어요, 나갔어요, 했어요 — “bir yoʻla” degani "
                       "aynan shu: bitta safar, ikkita maqsad.</p>",
    },
    {
        "text": "<p><strong>고자</strong> ning egasi haqida nima "
                "toʻgʻri?</p>",
        "choices": ["Ikkala gapning egasi bir xil boʻlishi kerak",
                    "Egalar boshqa boʻlishi kerak",
                    "Ega boʻlmasligi kerak",
                    "Faqat uchinchi shaxs"],
        "correct": "Ikkala gapning egasi bir xil boʻlishi kerak",
        "explanation": "<p>Maqsad kimniki boʻlsa, harakatni ham oʻsha odam "
                       "qiladi — bu 겸 uchun ham amal qiladi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>운동도 하 겸 친구도 만나 겸 "
                "공원에 갔어요.</strong></p>",
        "choices": ["하 겸 / 만나 겸 → 할 겸 / 만날 겸",
                    "하 겸 / 만나 겸 → 하는 겸 / 만나는 겸",
                    "공원에 → 공원을", "Xato yoʻq"],
        "correct": "하 겸 / 만나 겸 → 할 겸 / 만날 겸",
        "explanation": "<p>겸 ot boʻlgani uchun oldida <strong>(으)ㄹ</strong> "
                       "aniqlovchisi shart.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>한국어를 배웠고자 한국에 "
                "왔습니다.</strong></p>",
        "choices": ["배웠고자 → 배우고자", "배웠고자 → 배울고자",
                    "왔습니다 → 왔어요", "Xato yoʻq"],
        "correct": "배웠고자 → 배우고자",
        "explanation": "<p>고자 dan oldin zamon qoʻshimchasi "
                       "qoʻyilmaydi.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>Rasmiy arizada: “Bu dasturga qatnashish maqsadida ariza "
                "berdim” — qaysi biri toʻgʻri?</p>",
        "choices": ["이 프로그램에 참가할 겸 지원했습니다",
                    "이 프로그램에 참가하고자 지원했습니다",
                    "이 프로그램에 참가했고자 지원했습니다",
                    "이 프로그램에 참가하기 고자 지원했습니다"],
        "correct": "이 프로그램에 참가하고자 지원했습니다",
        "explanation": "<p>Rasmiy hujjat — <strong>고자</strong> + "
                       "습니다체.</p>",
    },
    {
        "text": "<p><strong>가:</strong> 왜 시장에 갔어요?</p>"
                "<p><strong>나:</strong> ___</p>",
        "choices": ["과일도 살 겸 친구도 만날 겸 갔어요",
                    "과일도 사고자 친구도 만나고자 갔어요",
                    "과일도 살 겸 친구도 만날 겸 가세요",
                    "과일도 사기 겸 친구도 만나기 겸 갔어요"],
        "correct": "과일도 살 겸 친구도 만날 겸 갔어요",
        "explanation": "<p>Kundalik suhbat — <strong>(으)ㄹ 겸</strong>. "
                       "고자 bu yerda juda rasmiy boʻlib eshitiladi.</p>",
    },
]


# =====================================================================
# PK-72 — 기 마련이다, (으)ㄴ/는 법이다
# =====================================================================

Q_PK72 = [
    # 1–5 tanish
    {
        "text": "<p><strong>기 마련이다</strong> nimani bildiradi?</p>",
        "choices": ["…ishi tabiiy", "…shi mumkin", "…sam boʻlardi",
                    "…maqsadida"],
        "correct": "…ishi tabiiy",
        "explanation": "<p>사람은 누구나 실수하기 마련이에요 — “har qanday "
                       "odam xato qilishi <strong>tabiiy</strong>”.</p>",
    },
    {
        "text": "<p><strong>법</strong> soʻzi nima degani?</p>",
        "choices": ["Qonun", "Usul", "Joy", "Vaqt"],
        "correct": "Qonun",
        "explanation": "<p>Shuning uchun 법이다 qatʼiy eshitiladi — "
                       "oʻzbekchada “dunyoning <strong>qonuni</strong> "
                       "shu”.</p>",
    },
    {
        "text": "<p><strong>마련</strong> dan oldin qaysi shakl keladi?</p>",
        "choices": ["기", "(으)ㄹ", "는", "(으)ㄴ"],
        "correct": "기",
        "explanation": "<p>실수하<strong>기</strong> 마련이에요 — PK-46 dagi "
                       "otlashtiruvchi 기.</p>",
    },
    {
        "text": "<p><strong>법</strong> dan oldin qaysi shakl keladi?</p>",
        "choices": ["기", "Aniqlovchi shakli ((으)ㄴ/는)", "고", "아/어"],
        "correct": "Aniqlovchi shakli ((으)ㄴ/는)",
        "explanation": "<p>성공하<strong>는</strong> 법이에요 — 법 ot "
                       "boʻlgani uchun oldida aniqlovchi turadi.</p>",
    },
    {
        "text": "<p>Bu ikki qolip qayerda ayniqsa koʻp uchraydi?</p>",
        "choices": ["Maqollarda va TOPIK II matnlarining xulosasida",
                    "Faqat savol gaplarda",
                    "Faqat buyruqlarda",
                    "Faqat reklama matnlarida"],
        "correct": "Maqollarda va TOPIK II matnlarining xulosasida",
        "explanation": "<p>Maqol — vaqtdan tashqari haqiqat, aynan shu "
                       "qoliplarning uyi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 사람은 누구나 <strong>______</strong> "
                "마련이에요. (실수하다)</p>",
        "choices": ["실수할", "실수하는", "실수하기", "실수한"],
        "correct": "실수하기",
        "explanation": "<p>마련 dan oldin <strong>기</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 노력하면 <strong>______</strong> 법이에요. "
                "(성공하다)</p>",
        "choices": ["성공하기", "성공하는", "성공할", "성공한"],
        "correct": "성공하는",
        "explanation": "<p>법 dan oldin aniqlovchi; feʼl "
                       "<strong>는</strong> oladi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 처음에는 <strong>______</strong> "
                "마련이에요. (어렵다)</p>",
        "choices": ["어려운", "어려울", "어렵기", "어려워서"],
        "correct": "어렵기",
        "explanation": "<p>마련 sifat bilan ham <strong>기</strong> "
                       "oladi: 어렵기 마련이에요.</p>",
    },
    {
        "text": "<p>Toʻldiring: 시간이 지나면 <strong>______</strong> "
                "마련이에요. (잊다)</p>",
        "choices": ["잊는", "잊을", "잊기", "잊은"],
        "correct": "잊기",
        "explanation": "<p>Koʻpincha <strong>(으)면</strong> bilan "
                       "juftlik: shart + tabiiy natija.</p>",
    },
    {
        "text": "<p>“Yaxshi ishga vaqt ketadi — qoida shunday” — qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["좋은 일에는 시간이 걸리기 법이에요",
                    "좋은 일에는 시간이 걸리는 법이에요",
                    "좋은 일에는 시간이 걸릴 법이에요",
                    "좋은 일에는 시간이 걸린 법이에요"],
        "correct": "좋은 일에는 시간이 걸리는 법이에요",
        "explanation": "<p>걸리다 — feʼl → <strong>는 법이다</strong>.</p>",
    },
    {
        "text": "<p><strong>게 마련이다</strong> haqida nima toʻgʻri?</p>",
        "choices": ["Notoʻgʻri shakl",
                    "기 마련이다 bilan bir xil maʼno",
                    "Faqat oʻtgan zamon uchun",
                    "Faqat ot bilan"],
        "correct": "기 마련이다 bilan bir xil maʼno",
        "explanation": "<p>실수하게 마련이에요 = 실수하기 마련이에요. "
                       "기 shakli biroz koʻproq uchraydi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 열심히 하면 실력이 <strong>______</strong> "
                "마련이에요. (늘다)</p>",
        "choices": ["느는", "늘기", "늘", "는"],
        "correct": "늘기",
        "explanation": "<p>마련 → <strong>기</strong>: 늘기 마련이에요 "
                       "(“malaka oshishi tabiiy”).</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Doʻstingiz imtihondan yiqildi. Qaysi qolip "
                "yumshoqroq?</p>",
        "choices": ["처음에는 어렵기 마련이에요",
                    "노력해야 하는 법이에요",
                    "실패하는 법이에요",
                    "실수하기 십상이에요"],
        "correct": "처음에는 어렵기 마련이에요",
        "explanation": "<p><strong>기 마련이다</strong> — yumshoq kuzatuv, "
                       "tasalli. <strong>법이다</strong> tengdoshga “men "
                       "bilaman, sen bilmaysan” degandek chiqadi.</p>",
    },
    {
        "text": "<p>Ikkalasining ohangdagi farqi nimada?</p>",
        "choices": ["기 마련이다 — yumshoq kuzatuv; 법이다 — qatʼiy haqiqat "
                    "va oʻgit",
                    "기 마련이다 — qatʼiy; 법이다 — yumshoq",
                    "Ikkalasi bir xil",
                    "법이다 faqat savolda ishlatiladi"],
        "correct": "기 마련이다 — yumshoq kuzatuv; 법이다 — qatʼiy haqiqat "
                   "va oʻgit",
        "explanation": "<p>법 = “qonun” — soʻzning oʻzi ohangni "
                       "belgilaydi.</p>",
    },
    {
        "text": "<p>Nima uchun <strong>시간이 지났기 마련이에요</strong> "
                "notoʻgʻri?</p>",
        "choices": ["받침 xato",
                    "Bu qolip umumiy haqiqat haqida — bitta oʻtgan hodisa "
                    "haqida emas",
                    "지나다 feʼl emas",
                    "마련 aniqlovchi oladi"],
        "correct": "Bu qolip umumiy haqiqat haqida — bitta oʻtgan hodisa "
                   "haqida emas",
        "explanation": "<p>Toʻgʻrisi — 시간이 <strong>지나면 잊기 "
                       "마련이에요</strong>.</p>",
    },
    {
        "text": "<p>Bu qoliplar TOPIK II oʻqishida koʻpincha matnning "
                "qaysi qismida turadi?</p>",
        "choices": ["Birinchi jumlada", "Xulosa jumlasida",
                    "Sarlavhada", "Savolda"],
        "correct": "Xulosa jumlasida",
        "explanation": "<p>Muallif oxirida umumiy haqiqatni aytadi — "
                       "shuning uchun bu qoliplarni bilish matnning "
                       "asosiy fikrini topishga yordam beradi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>사람은 누구나 실수할 "
                "마련이에요.</strong></p>",
        "choices": ["실수할 → 실수하기", "실수할 → 실수하는",
                    "누구나 → 누구도", "Xato yoʻq"],
        "correct": "실수할 → 실수하기",
        "explanation": "<p>마련 dan oldin <strong>기</strong> keladi, "
                       "(으)ㄹ emas.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>노력하면 성공하기 "
                "법이에요.</strong></p>",
        "choices": ["성공하기 → 성공하는", "성공하기 → 성공할",
                    "노력하면 → 노력해서", "Xato yoʻq"],
        "correct": "성공하기 → 성공하는",
        "explanation": "<p>법 ot boʻlgani uchun oldida "
                       "<strong>aniqlovchi</strong> turadi.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Vaqt oʻtsa, unutilishi tabiiy” — qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["시간이 지나면 잊는 마련이에요",
                    "시간이 지나면 잊기 마련이에요",
                    "시간이 지났으면 잊기 마련이에요",
                    "시간이 지나면 잊을 마련이에요"],
        "correct": "시간이 지나면 잊기 마련이에요",
        "explanation": "<p>(으)면 + 기 마련이다 — bu qolipning eng tipik "
                       "juftligi.</p>",
    },
    {
        "text": "<p><strong>가:</strong> 한국어가 너무 어려워요.</p>"
                "<p><strong>나:</strong> ___</p>",
        "choices": ["처음에는 어렵기 마련이에요",
                    "처음에는 어려운 마련이에요",
                    "처음에는 어렵기 십상이에요",
                    "처음에는 어려울 법이에요"],
        "correct": "처음에는 어렵기 마련이에요",
        "explanation": "<p>Tasalli berish — <strong>기 마련이다</strong> "
                       "ning eng tabiiy oʻrni.</p>",
    },
]


# =====================================================================
# PK-73 — (으)ㄹ지도 모르다, 기 십상이다
# =====================================================================

Q_PK73 = [
    # 1–5 tanish
    {
        "text": "<p><strong>(으)ㄹ지도 모르다</strong> nimani bildiradi?</p>",
        "choices": ["…shi mumkin (past ishonch)", "…ishi tabiiy",
                    "…maqsadida", "…sam boʻlardi"],
        "correct": "…shi mumkin (past ishonch)",
        "explanation": "<p>비가 올지도 몰라요 — “yomgʻir yogʻishi "
                       "<strong>mumkin</strong>”, faqat ehtimol.</p>",
    },
    {
        "text": "<p><strong>모르다</strong> bu qolipda “bilmayman” degani "
                "boʻladimi?</p>",
        "choices": ["Ha", "Yoʻq — (으)ㄹ지도 모르다 bitta qolip va “…shi "
                    "mumkin” degani",
                    "Faqat savolda", "Faqat inkorda"],
        "correct": "Yoʻq — (으)ㄹ지도 모르다 bitta qolip va “…shi "
                   "mumkin” degani",
        "explanation": "<p>Uni boʻlaklarga ajratib tarjima qilmang.</p>",
    },
    {
        "text": "<p><strong>십상</strong> (十常) soʻzma-soʻz nima degani?</p>",
        "choices": ["Oʻn martadan oʻni", "Oʻn kun", "Oʻninchi",
                    "Oʻn kishi"],
        "correct": "Oʻn martadan oʻni",
        "explanation": "<p>Shuning uchun “deyarli har doim shunday "
                       "boʻladi” degan maʼno beradi.</p>",
    },
    {
        "text": "<p><strong>기 십상이다</strong> ning natijasi qanday "
                "boʻladi?</p>",
        "choices": ["Doim salbiy", "Doim ijobiy", "Har xil", "Neytral"],
        "correct": "Doim salbiy",
        "explanation": "<p>Bu <strong>ogohlantirish</strong> qolipi. "
                       "<s>성공하기 십상이에요</s> ✗.</p>",
    },
    {
        "text": "<p><strong>십상</strong> dan oldin qaysi shakl keladi?</p>",
        "choices": ["기", "(으)ㄹ", "는", "아/어"],
        "correct": "기",
        "explanation": "<p>실수하<strong>기</strong> 십상이에요 — "
                       "마련이다 bilan bir xil.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 내일 비가 <strong>______</strong> 몰라요. "
                "(오다)</p>",
        "choices": ["오지도", "올지도", "온지도", "왔지도"],
        "correct": "올지도",
        "explanation": "<p>오 da 받침 yoʻq → <strong>ㄹ지도</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 시험이 <strong>______</strong> 몰라요. "
                "(어렵다)</p>",
        "choices": ["어렵을지도", "어려울지도", "어려운지도", "어렵지도"],
        "correct": "어려울지도",
        "explanation": "<p>어렵다 — ㅂ notoʻgʻri sifati (PK-32): "
                       "어려우 + ㄹ지도.</p>",
    },
    {
        "text": "<p>Toʻldiring: 자스루르 씨가 벌써 <strong>______</strong> "
                "몰라요. (가다, oʻtgan zamon)</p>",
        "choices": ["갈지도", "갔을지도", "간지도", "가지도"],
        "correct": "갔을지도",
        "explanation": "<p>Oʻtgan zamon <strong>았/었을지도</strong> ichida "
                       "boʻladi, 모르다 da emas.</p>",
    },
    {
        "text": "<p>Toʻldiring: 그 사람이 새 선생님<strong>______</strong> "
                "몰라요.</p>",
        "choices": ["일지도", "이지도", "인지도", "이라지도"],
        "correct": "일지도",
        "explanation": "<p>Ot + 이다 → <strong>일지도 모르다</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 서두르면 <strong>______</strong> "
                "십상이에요. (실수하다)</p>",
        "choices": ["실수할", "실수하는", "실수하기", "실수한"],
        "correct": "실수하기",
        "explanation": "<p>십상 dan oldin <strong>기</strong>.</p>",
    },
    {
        "text": "<p>“Xaritasiz borsangiz, adashib qolishingiz turgan gap” — "
                "qaysi biri toʻgʻri?</p>",
        "choices": ["지도 없이 가면 길을 잃기 십상이에요",
                    "지도 없이 가면 길을 잃을 십상이에요",
                    "지도 없이 가면 길을 잃기 마련이에요",
                    "지도 없이 가면 길을 잃을지도 십상이에요"],
        "correct": "지도 없이 가면 길을 잃기 십상이에요",
        "explanation": "<p>Ogohlantirish + salbiy natija = "
                       "<strong>기 십상이다</strong>, va oldida 기.</p>",
    },
    {
        "text": "<p>Toʻldiring: 밤에 커피를 마시면 잠을 못 "
                "<strong>______</strong> 십상이에요. (자다)</p>",
        "choices": ["잘", "자는", "자기", "잔"],
        "correct": "자기",
        "explanation": "<p>못 자<strong>기</strong> 십상이에요 — inkor "
                       "십상 dan oldin turadi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Bu uchtasini ishonch boʻyicha eng yuqoridan pastga "
                "tizing: 올 것 같아요 · 올 거예요 · 올지도 몰라요</p>",
        "choices": ["올 거예요 → 올 것 같아요 → 올지도 몰라요",
                    "올지도 몰라요 → 올 것 같아요 → 올 거예요",
                    "올 것 같아요 → 올 거예요 → 올지도 몰라요",
                    "Uchalasi bir xil"],
        "correct": "올 거예요 → 올 것 같아요 → 올지도 몰라요",
        "explanation": "<p>Oʻzbekchada ham shu zinapoya bor: “yogʻadi” → "
                       "“yogʻadiganga oʻxshaydi” → “balki yogʻar”.</p>",
    },
    {
        "text": "<p><strong>기 마련이다</strong> va <strong>기 십상이다</strong> "
                "farqi nimada?</p>",
        "choices": ["마련이다 — tabiiy (yaxshi ham, yomon ham); 십상이다 — "
                    "ogohlantirish, faqat yomon",
                    "마련이다 faqat yomon; 십상이다 har xil",
                    "Ikkalasi bir xil",
                    "십상이다 faqat sifat bilan"],
        "correct": "마련이다 — tabiiy (yaxshi ham, yomon ham); 십상이다 — "
                   "ogohlantirish, faqat yomon",
        "explanation": "<p>처음에는 어렵기 <strong>마련</strong>이에요 "
                       "(tasalli) / 서두르면 실수하기 <strong>십상</strong>"
                       "이에요 (ogohlantirish).</p>",
    },
    {
        "text": "<p>Nima uchun <strong>열심히 하면 성공하기 십상이에요</strong> "
                "notoʻgʻri?</p>",
        "choices": ["받침 xato",
                    "십상 natijasi doim salbiy — muvaffaqiyat yaxshi natija",
                    "성공하다 feʼl emas",
                    "(으)면 kelmaydi"],
        "correct": "십상 natijasi doim salbiy — muvaffaqiyat yaxshi natija",
        "explanation": "<p>Toʻgʻrisi — 성공하는 <strong>법이에요</strong> "
                       "yoki 성공하기 <strong>마련이에요</strong>.</p>",
    },
    {
        "text": "<p><strong>기 십상이다</strong> koʻpincha qaysi qolip bilan "
                "yuradi?</p>",
        "choices": ["(으)면", "고자", "(으)ㄹ 겸", "잖아요"],
        "correct": "(으)면",
        "explanation": "<p>Shart + ogohlantirish: 서두르<strong>면</strong> "
                       "실수하기 십상이에요.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>내일 비가 오지도 몰라요.</strong></p>",
        "choices": ["오지도 → 올지도", "오지도 → 온지도",
                    "몰라요 → 모르겠어요", "Xato yoʻq"],
        "correct": "오지도 → 올지도",
        "explanation": "<p>Aniqlovchi shakli shart: "
                       "<strong>(으)ㄹ지도</strong>.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>서두르면 실수할 "
                "십상이에요.</strong></p>",
        "choices": ["실수할 → 실수하기", "실수할 → 실수하는",
                    "서두르면 → 서둘러서", "Xato yoʻq"],
        "correct": "실수할 → 실수하기",
        "explanation": "<p>십상 dan oldin <strong>기</strong> keladi.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Jasur allaqachon ketgan boʻlishi mumkin” — qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["자스루르 씨가 벌써 갈지도 몰라요",
                    "자스루르 씨가 벌써 갔을지도 몰라요",
                    "자스루르 씨가 벌써 갔지도 몰라요",
                    "자스루르 씨가 벌써 갈지도 몰랐어요"],
        "correct": "자스루르 씨가 벌써 갔을지도 몰라요",
        "explanation": "<p>Oʻtgan zamon <strong>았/었을지도</strong> "
                       "ichida.</p>",
    },
    {
        "text": "<p><strong>가:</strong> 지도 없이 산에 가도 돼요?</p>"
                "<p><strong>나:</strong> ___</p>",
        "choices": ["길을 잃기 십상이에요. 지도를 가져가세요",
                    "길을 잃기 마련이에요. 지도를 가져가세요",
                    "길을 잃을 십상이에요. 지도를 가져가세요",
                    "길을 잃고자 합니다"],
        "correct": "길을 잃기 십상이에요. 지도를 가져가세요",
        "explanation": "<p>Ogohlantirish + salbiy natija + maslahat — "
                       "<strong>기 십상이다</strong> ning eng tipik "
                       "oʻrni.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-71 Mashq: (으)ㄹ 겸 · 고자",
        "description": "20 savol — ikki maqsad, ot bilan 겸, rasmiy 고자 va "
                       "uning uchta sharti, (으)려고 dan farqi.",
        "tutorial":    "PK-71:",
        "level":       "medium",
        "questions":   Q_PK71,
    },
    {
        "title":       "PK-72 Mashq: 기 마련이다 · (으)ㄴ/는 법이다",
        "description": "20 savol — 기 va aniqlovchi farqi, ikki qolipning "
                       "ohangi, maqol tili va TOPIK II xulosa jumlalari.",
        "tutorial":    "PK-72:",
        "level":       "medium",
        "questions":   Q_PK72,
    },
    {
        "title":       "PK-73 Mashq: (으)ㄹ지도 모르다 · 기 십상이다",
        "description": "20 savol — ishonch darajalari zinapoyasi, oʻtgan "
                       "zamon shakli va 십상 ning majburiy salbiy natijasi.",
        "tutorial":    "PK-73:",
        "level":       "medium",
        "questions":   Q_PK73,
    },
]
