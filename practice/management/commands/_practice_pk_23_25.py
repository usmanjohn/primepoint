# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-23 … PK-25 (sonlar va vaqt).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_23_25.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "한국어",
    "description": "Koreys tili — grammatika va yozuv mashqlari",
    "icon":        "bi-translate",
    "color":       "#d97706",
}

DEFAULTS = {
    "level":                "easy",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}


# =====================================================================
# PK-23 — 한자어 sonlar
# =====================================================================

Q_PK23 = [
    # 1–5 tanish
    {
        "text": "<p><strong>칠</strong> qaysi raqam?</p>",
        "choices": ["7", "4", "8", "10"],
        "correct": "7",
        "explanation": "<p>일(1) 이(2) 삼(3) 사(4) 오(5) 육(6) <strong>칠(7)</strong> "
                       "팔(8) 구(9) 십(10).</p>",
    },
    {
        "text": "<p><strong>만</strong> qancha?</p>",
        "choices": ["10 000", "1 000", "100", "100 000"],
        "correct": "10 000",
        "explanation": "<p><strong>만 = 10 000</strong>. Koreys tilida katta birlik ming "
                       "emas, oʻn ming — shuning uchun raqamlar oʻngdan toʻrttadan "
                       "ajratiladi.</p>",
    },
    {
        "text": "<p>한자어 sonlar nimani sanaydi?</p>",
        "choices": ["Pul, sana, daqiqa, qavat", "Narsalar va odamlar",
                    "Yosh va soat", "Hayvonlar"],
        "correct": "Pul, sana, daqiqa, qavat",
        "explanation": "<p>한자어 — <strong>oʻlchov va raqamlar</strong> uchun: 원, 분, "
                       "년/월/일, 층, 번. Narsalar va odamlar esa 고유어 bilan "
                       "sanaladi (PK-24).</p>",
    },
    {
        "text": "<p>Telefon raqamida nol qanday aytiladi?</p>",
        "choices": ["공", "영", "빵", "무"],
        "correct": "공",
        "explanation": "<p>Telefon uchun <strong>공</strong>, matematikada esa "
                       "<strong>영</strong>. Telefon raqamida har bir raqam alohida "
                       "oʻqiladi: 공일공.</p>",
    },
    {
        "text": "<p><strong>몇</strong> birlikka nisbatan qayerda turadi?</p>",
        "choices": ["Birlikdan oldin", "Birlikdan keyin", "Gap oxirida", "Gap boshida"],
        "correct": "Birlikdan oldin",
        "explanation": "<p><strong>몇 번</strong>, <strong>몇 층</strong>, "
                       "<strong>몇 시</strong> — 몇 har doim birlikdan oldin.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p><strong>37</strong> ni koreyschada yozing.</p>",
        "choices": ["삼십칠", "칠십삼", "삼칠", "삼십일곱"],
        "correct": "삼십칠",
        "explanation": "<p>3 × 10 + 7 = <strong>삼십칠</strong>. Katta birlik oldin, "
                       "kichigi keyin — oʻzbekcha “oʻttiz yetti” kabi.</p>",
    },
    {
        "text": "<p><strong>100 000</strong> ni koreyschada yozing.</p>",
        "choices": ["십만", "백천", "만십", "천백"],
        "correct": "십만",
        "explanation": "<p>10 × 만 (10 000) = <strong>십만</strong>. Oʻngdan toʻrttadan "
                       "ajrating: 10|0000.</p>",
    },
    {
        "text": "<p><strong>1 000 000</strong> ni koreyschada yozing.</p>",
        "choices": ["백만", "천천", "만만", "십십만"],
        "correct": "백만",
        "explanation": "<p>100 × 만 = <strong>백만</strong>. 100|0000 deb ajrating — "
                       "oʻzbekcha “million” toʻgʻridan-toʻgʻri koʻchmaydi.</p>",
    },
    {
        "text": "<p>“Bu kitob 5000 von” ni koreyschaga oʻgiring.</p>",
        "choices": ["이 책은 오천 원이에요.", "이 책은 다섯천 원이에요.",
                    "이 책은 오천 개예요.", "이 책은 다섯 원이에요."],
        "correct": "이 책은 오천 원이에요.",
        "explanation": "<p>Pul — 한자어: <strong>오천</strong> (5 × 1000) + "
                       "<strong>원</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>가게가 ___ 층에 "
                "있어요?</strong></p>",
        "choices": ["몇", "얼마", "누구", "무슨"],
        "correct": "몇",
        "explanation": "<p><strong>몇</strong> — son soʻraydi va birlikdan oldin turadi: "
                       "몇 층. 얼마 esa narx uchun.</p>",
    },
    {
        "text": "<p><strong>십육</strong> qanday oʻqiladi?</p>",
        "choices": ["[심뉵]", "[십육]", "[시뷰]", "[십뉵]"],
        "correct": "[심뉵]",
        "explanation": "<p>비음화 — 16 talaffuzda oʻzgaradi: <strong>[심뉵]</strong>. "
                       "60 (육십) esa 경음화 bilan [육씹].</p>",
    },
    {
        "text": "<p>“2026-yil” ni koreyschada yozing.</p>",
        "choices": ["이천이십육년", "둘천스물여섯년", "이십육년", "이천이십육 살"],
        "correct": "이천이십육년",
        "explanation": "<p>Sana — 한자어: 이천(2000) + 이십(20) + 육(6) + "
                       "<strong>년</strong>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Nega koreys raqamlarini uchtadan emas, toʻrttadan ajratish "
                "kerak?</p>",
        "choices": ["Chunki katta birlik 만 = 10 000, ming emas",
                    "Chunki koreyscha oʻngdan chapga yoziladi",
                    "Chunki 백 = 1000",
                    "Chunki koreyschada vergul yoʻq"],
        "correct": "Chunki katta birlik 만 = 10 000, ming emas",
        "explanation": "<p>Oʻzbekcha/inglizcha vergul mingga qarab qoʻyiladi (1,000,000), "
                       "koreys tizimi esa <strong>만</strong> ga qarab: 100|0000 = "
                       "<strong>백만</strong>.</p>",
    },
    {
        "text": "<p><strong>영</strong> va <strong>공</strong> farqi nima?</p>",
        "choices": ["영 — matematikada, 공 — telefon raqamlarida",
                    "영 — telefon, 공 — matematika",
                    "Farqi yoʻq",
                    "영 — katta sonlar, 공 — kichik sonlar"],
        "correct": "영 — matematikada, 공 — telefon raqamlarida",
        "explanation": "<p>Ikkalasi ham “nol”, lekin qoʻllanishi boshqa. Telefon "
                       "raqamida har doim <strong>공</strong>.</p>",
    },
    {
        "text": "<p>Qaysi birlik 한자어 son bilan <em>ishlatilmaydi</em>?</p>",
        "choices": ["살 (yosh)", "원 (pul)", "층 (qavat)", "분 (daqiqa)"],
        "correct": "살 (yosh)",
        "explanation": "<p>Yosh — <strong>고유어</strong> tizimi bilan: 스무 살, "
                       "열여섯 살. Qolgan uchtasi 한자어 oladi.</p>",
    },
    {
        "text": "<p>Koreys va oʻzbek son tuzilishi qanday oʻxshaydi?</p>",
        "choices": ["Ikkalasida ham katta birlik oldin, kichigi keyin",
                    "Ikkalasida ham 만 birligi bor",
                    "Ikkalasida ikkita son tizimi bor",
                    "Hech qanday oʻxshashlik yoʻq"],
        "correct": "Ikkalasida ham katta birlik oldin, kichigi keyin",
        "explanation": "<p><em>oʻttiz yetti</em> → <strong>삼십칠</strong>. Farqi shundaki, "
                       "koreyschada “oʻttiz” alohida soʻz emas — u ochiq hisoblanadi "
                       "(삼십), ya'ni yodlash kamroq.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi javob <em>notoʻgʻri</em>?</p>",
        "choices": ["1 000 000 = 천천", "10 000 = 만", "100 = 백", "1 000 = 천"],
        "correct": "1 000 000 = 천천",
        "explanation": "<p>Toʻgʻrisi — <strong>백만</strong> (100 × 만). "
                       "<s>천천</s> degan tuzilma koreys tilida yoʻq.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["이 책은 만 원이에요.", "이 책은 하나만 원이에요.",
                    "이 책은 만 살이에요.", "이 책은 열 원이에요만."],
        "correct": "이 책은 만 원이에요.",
        "explanation": "<p>Pul — 한자어 son + <strong>원</strong>: 만 원 = 10 000 von. "
                       "살 esa yosh uchun.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 전화번호가 몇 번이에요?<br>나: ___</strong></p>",
        "choices": ["공일공 이삼사오예요.", "영일영 이삼사오예요.",
                    "하나공하나 이삼사오예요.", "공일공 둘셋넷다섯이에요."],
        "correct": "공일공 이삼사오예요.",
        "explanation": "<p>Telefon raqamida nol <strong>공</strong>, va raqamlar "
                       "<strong>한자어</strong> bilan aytiladi — 고유어 (하나, 둘) "
                       "ishlatilmaydi.</p>",
    },
    {
        "text": "<p><strong>50 000 von</strong> ni koreyschada yozing.</p>",
        "choices": ["오만 원", "오천 원", "십만 원", "다섯만 원"],
        "correct": "오만 원",
        "explanation": "<p>5 × 만 (10 000) = <strong>오만</strong> = 50 000. "
                       "오천 esa 5000 boʻlardi.</p>",
    },
]


# =====================================================================
# PK-24 — 고유어 sonlar va sanoq soʻzlari
# =====================================================================

Q_PK24 = [
    # 1–5 tanish
    {
        "text": "<p><strong>다섯</strong> qaysi raqam?</p>",
        "choices": ["5", "4", "6", "10"],
        "correct": "5",
        "explanation": "<p>하나(1) 둘(2) 셋(3) 넷(4) <strong>다섯(5)</strong> 여섯(6) "
                       "일곱(7) 여덟(8) 아홉(9) 열(10).</p>",
    },
    {
        "text": "<p>고유어 sonlar nechagacha boradi?</p>",
        "choices": ["99 gacha", "10 gacha", "1000 gacha", "Cheksiz"],
        "correct": "99 gacha",
        "explanation": "<p>고유어 sonlar <strong>99 gacha</strong>. 100 dan boshlab har "
                       "doim 한자어: 백, 천, 만.</p>",
    },
    {
        "text": "<p>Odamlarni sanash uchun qaysi sanoq soʻzi ishlatiladi?</p>",
        "choices": ["명", "개", "마리", "권"],
        "correct": "명",
        "explanation": "<p><strong>명</strong> — odamlar (hurmatlisi <strong>분</strong>). "
                       "개 — narsalar, 마리 — hayvonlar, 권 — kitoblar.</p>",
    },
    {
        "text": "<p>Hayvonlarni sanash uchun qaysi sanoq soʻzi ishlatiladi?</p>",
        "choices": ["마리", "명", "개", "살"],
        "correct": "마리",
        "explanation": "<p><strong>마리</strong> — hayvonlar uchun: 고양이 두 마리. "
                       "Oʻzbekchadagi “ikki <em>bosh</em>” bilan bir xil tushuncha.</p>",
    },
    {
        "text": "<p>Sanash tartibi qanday?</p>",
        "choices": ["ot → son → sanoq soʻzi", "son → sanoq soʻzi → ot",
                    "sanoq soʻzi → son → ot", "son → ot → sanoq soʻzi"],
        "correct": "ot → son → sanoq soʻzi",
        "explanation": "<p><strong>사과 세 개</strong> — ot birinchi. Oʻzbekchada esa "
                       "teskari: “besh <em>dona</em> <b>olma</b>”.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>“Uchta olma” ni koreyschaga oʻgiring.</p>",
        "choices": ["사과 세 개", "세 개 사과", "사과 셋 개", "삼 개 사과"],
        "correct": "사과 세 개",
        "explanation": "<p>Ikki narsa: <strong>ot birinchi</strong> (사과), va 셋 → "
                       "<strong>세</strong> qisqargan.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>학생 ___ 명 있어요.</strong> "
                "(“ikki oʻquvchi”)</p>",
        "choices": ["두", "둘", "이", "두개"],
        "correct": "두",
        "explanation": "<p>Sanoq soʻzi oldida <strong>둘 → 두</strong> qisqaradi. "
                       "이 esa 한자어, odamlar uchun ishlatilmaydi.</p>",
    },
    {
        "text": "<p>“Men 20 yoshdaman” ni koreyschaga oʻgiring.</p>",
        "choices": ["저는 스무 살이에요.", "저는 스물 살이에요.",
                    "저는 이십 살이에요.", "저는 스무 개예요."],
        "correct": "저는 스무 살이에요.",
        "explanation": "<p>Yosh — 고유어, va 스물 sanoq (살) oldida "
                       "<strong>스무</strong> boʻlib qisqaradi.</p>",
    },
    {
        "text": "<p>“Toʻrtta mushuk” ni koreyschaga oʻgiring.</p>",
        "choices": ["고양이 네 마리", "고양이 넷 마리", "네 마리 고양이", "고양이 사 마리"],
        "correct": "고양이 네 마리",
        "explanation": "<p>Ot birinchi, 넷 → <strong>네</strong>, va hayvon uchun "
                       "<strong>마리</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>책 다섯 ___ 있어요.</strong></p>",
        "choices": ["권", "명", "마리", "살"],
        "correct": "권",
        "explanation": "<p><strong>권</strong> — kitoblar uchun maxsus sanoq soʻzi: "
                       "책 다섯 권.</p>",
    },
    {
        "text": "<p>Oʻqituvchini hurmat bilan sanash uchun qaysi soʻz?</p>",
        "choices": ["분", "명", "개", "마리"],
        "correct": "분",
        "explanation": "<p><strong>분</strong> — odamlarning hurmatli sanoq soʻzi: "
                       "선생님 한 분. Diqqat: 분 한자어 bilan “daqiqa” degani.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>커피 두 ___ 마셔요.</strong></p>",
        "choices": ["잔", "권", "마리", "명"],
        "correct": "잔",
        "explanation": "<p><strong>잔</strong> — piyola/stakan uchun: 커피 두 잔. "
                       "Shisha uchun esa 병.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Qaysi toʻrtta son sanoq oldida qisqaradi?</p>",
        "choices": ["하나, 둘, 셋, 넷", "다섯, 여섯, 일곱, 여덟",
                    "일, 이, 삼, 사", "열, 스물, 서른, 마흔"],
        "correct": "하나, 둘, 셋, 넷",
        "explanation": "<p><strong>한, 두, 세, 네</strong> (va 스물 → 스무). Qoida 11–14 ga "
                       "ham tegishli: 열한 개, 열두 개.</p>",
    },
    {
        "text": "<p>Oʻzbek tilidagi qaysi soʻzlar koreys sanoq soʻzlariga toʻgʻri "
                "keladi?</p>",
        "choices": ["dona, nafar, bosh", "ta, lar, ning",
                    "ko'p, oz, hamma", "bir, ikki, uch"],
        "correct": "dona, nafar, bosh",
        "explanation": "<p>“besh <em>dona</em> olma” → 사과 다섯 <strong>개</strong>; "
                       "“uch <em>nafar</em> odam” → 사람 세 <strong>명</strong>; "
                       "“ikki <em>bosh</em>” → 두 <strong>마리</strong>.</p>",
    },
    {
        "text": "<p>Koreys va oʻzbek sanash tartibi qanday farq qiladi?</p>",
        "choices": ["Koreyschada ot birinchi, oʻzbekchada oxirida",
                    "Koreyschada ot oxirida, oʻzbekchada birinchi",
                    "Farqi yoʻq",
                    "Oʻzbekchada sanoq soʻzi yoʻq"],
        "correct": "Koreyschada ot birinchi, oʻzbekchada oxirida",
        "explanation": "<p><em>besh dona <b>olma</b></em> va <strong>사과</strong> 다섯 개. "
                       "Bu — darsdagi yagona joy, oʻzbek tili xalaqit beradi, shuning "
                       "uchun alohida eʼtibor bering.</p>",
    },
    {
        "text": "<p>Yosh qaysi tizim bilan aytiladi?</p>",
        "choices": ["고유어 + 살", "한자어 + 살", "한자어 + 세", "고유어 + 년"],
        "correct": "고유어 + 살",
        "explanation": "<p><strong>고유어 + 살</strong>: 스무 살, 열여섯 살. "
                       "<s>이십 살</s> notoʻgʻri.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["고양이 네 명 있어요.", "고양이 네 마리 있어요.",
                    "학생 두 명 있어요.", "책 다섯 권 있어요."],
        "correct": "고양이 네 명 있어요.",
        "explanation": "<p>고양이 — hayvon, shuning uchun <strong>마리</strong> kerak. "
                       "명 faqat odamlar uchun.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["사과 세 개 있어요.", "세 개 사과 있어요.",
                    "사과 셋 개 있어요.", "사과 삼 개 있어요."],
        "correct": "사과 세 개 있어요.",
        "explanation": "<p>Ot birinchi, 셋 qisqarib <strong>세</strong>, va narsalar "
                       "uchun 한자어 emas, <strong>고유어</strong>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
                "<p><strong>있어요 / 두 / 교실에 / 학생이 / 명</strong></p>",
        "choices": ["교실에 학생이 두 명 있어요.", "교실에 두 명 학생이 있어요.",
                    "학생이 교실에 명 두 있어요.", "두 명 학생이 교실에 있어요."],
        "correct": "교실에 학생이 두 명 있어요.",
        "explanation": "<p>Joy → ot + 이/가 → son + sanoq → kesim. Ot har doim son va "
                       "sanoqdan <strong>oldin</strong> turadi.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 몇 살이에요?<br>나: ___</strong></p>",
        "choices": ["열여섯 살이에요.", "십육 살이에요.",
                    "열여섯 개예요.", "십육 명이에요."],
        "correct": "열여섯 살이에요.",
        "explanation": "<p>Yosh — <strong>고유어 + 살</strong>. 십육 esa 한자어 va yosh "
                       "uchun ishlatilmaydi.</p>",
    },
]


# =====================================================================
# PK-25 — Vaqt, sana, hafta kunlari
# =====================================================================

Q_PK25 = [
    # 1–5 tanish
    {
        "text": "<p>Soat qaysi son tizimi bilan aytiladi?</p>",
        "choices": ["고유어", "한자어", "Ikkalasi ham", "Hech qaysi"],
        "correct": "고유어",
        "explanation": "<p>Soat — <strong>고유어 + 시</strong>: 한 시, 두 시, 세 시. "
                       "Daqiqa esa 한자어 + 분.</p>",
    },
    {
        "text": "<p>Daqiqa qaysi son tizimi bilan aytiladi?</p>",
        "choices": ["한자어", "고유어", "Ikkalasi ham", "Hech qaysi"],
        "correct": "한자어",
        "explanation": "<p>Daqiqa — <strong>한자어 + 분</strong>: 삼십 분, 십오 분.</p>",
    },
    {
        "text": "<p><strong>반</strong> nima degani?</p>",
        "choices": ["yarim", "soat", "daqiqa", "tun"],
        "correct": "yarim",
        "explanation": "<p><strong>반</strong> = yarim: 두 시 반 = 2:30. Kundalik nutqda "
                       "삼십 분 dan koʻra koʻproq ishlatiladi.</p>",
    },
    {
        "text": "<p><strong>수요일</strong> qaysi kun?</p>",
        "choices": ["chorshanba", "dushanba", "shanba", "juma"],
        "correct": "chorshanba",
        "explanation": "<p><strong>수</strong> — “suv”. Koreys hafta kunlari unsurlardan: "
                       "월(oy) 화(olov) 수(suv) 목(yogʻoch) 금(metall) 토(tuproq) "
                       "일(quyosh).</p>",
    },
    {
        "text": "<p>Sana tartibi qanday?</p>",
        "choices": ["yil → oy → kun", "kun → oy → yil",
                    "oy → kun → yil", "oy → yil → kun"],
        "correct": "yil → oy → kun",
        "explanation": "<p><strong>이천이십육년 팔월 이일</strong> — kattadan kichikka, "
                       "xuddi oʻzbekchadagi “2026-yil 2-avgust” kabi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p><strong>3:30</strong> ni koreyschada yozing.</p>",
        "choices": ["세 시 삼십 분", "삼 시 삼십 분", "세 시 서른 분", "삼 시 서른 분"],
        "correct": "세 시 삼십 분",
        "explanation": "<p>Soat <strong>고유어</strong> (세), daqiqa <strong>한자어</strong> "
                       "(삼십). Ikki tizim bitta jumlada.</p>",
    },
    {
        "text": "<p><strong>12:00</strong> ni koreyschada yozing.</p>",
        "choices": ["열두 시", "십이 시", "열둘 시", "십이 분"],
        "correct": "열두 시",
        "explanation": "<p>Soat 고유어, va 열둘 sanoq oldida <strong>열두</strong> boʻlib "
                       "qisqaradi.</p>",
    },
    {
        "text": "<p><strong>6-oy</strong> qanday yoziladi?</p>",
        "choices": ["유월", "육월", "여섯월", "유일월"],
        "correct": "유월",
        "explanation": "<p><strong>유월</strong> — istisno, ㄱ tushib qolgan. Ikkinchi "
                       "istisno: 10-oy = <strong>시월</strong>.</p>",
    },
    {
        "text": "<p><strong>10-oy</strong> qanday yoziladi?</p>",
        "choices": ["시월", "십월", "열월", "시일월"],
        "correct": "시월",
        "explanation": "<p><strong>시월</strong> — ㅂ tushib qolgan. Faqat 6 va 10 "
                       "istisno, qolgan oylar qoidaga boʻysunadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>저는 여덟 시___ 학교에 "
                "가요.</strong></p>",
        "choices": ["에", "에서", "이", "은"],
        "correct": "에",
        "explanation": "<p>Vaqt <strong>에</strong> oladi (PK-14). Lekin 오늘, 어제, 내일 "
                       "hech qachon olmaydi.</p>",
    },
    {
        "text": "<p>“Soat necha?” ni koreyschaga oʻgiring.</p>",
        "choices": ["몇 시예요?", "며칠이에요?", "무슨 요일이에요?", "몇 살이에요?"],
        "correct": "몇 시예요?",
        "explanation": "<p><strong>몇 시</strong> — soat. 며칠 — sana, 무슨 요일 — hafta "
                       "kuni, 몇 살 — yosh.</p>",
    },
    {
        "text": "<p><strong>금요일</strong> qaysi unsurdan?</p>",
        "choices": ["metall, oltin", "olov", "suv", "tuproq"],
        "correct": "metall, oltin",
        "explanation": "<p><strong>금</strong> — metall/oltin, ya'ni juma. 화 — olov "
                       "(seshanba), 수 — suv (chorshanba), 토 — tuproq (shanba).</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Nega soat 고유어, daqiqa esa 한자어 bilan aytiladi?</p>",
        "choices": ["Soat sanaladi, daqiqa oʻlchanadi",
                    "Soat oʻlchanadi, daqiqa sanaladi",
                    "Bu shunchaki yodlanadi, sababi yoʻq",
                    "Chunki 시 받침siz"],
        "correct": "Soat sanaladi, daqiqa oʻlchanadi",
        "explanation": "<p>Sanaladigan narsalar <strong>고유어</strong> oladi (PK-24), "
                       "oʻlchanadigan narsalar esa <strong>한자어</strong> (PK-23).</p>",
    },
    {
        "text": "<p>Koreys va oʻzbek hafta kunlari qanday farq qiladi?</p>",
        "choices": ["Koreysda unsurlar, oʻzbekchada sanoq",
                    "Koreysda sanoq, oʻzbekchada unsurlar",
                    "Ikkalasida ham unsurlar",
                    "Ikkalasida ham xudolar nomi"],
        "correct": "Koreysda unsurlar, oʻzbekchada sanoq",
        "explanation": "<p>Oʻzbekcha <em>dushanba</em> (ikkinchi), <em>seshanba</em> "
                       "(uchinchi) — sanoqqa qurilgan. Koreyscha 월·화·수·목·금 esa "
                       "unsurlarga. Ikkalasi ham mantiqiy, mantiqi boshqa.</p>",
    },
    {
        "text": "<p>Qaysi juftlik <em>notoʻgʻri</em>?</p>",
        "choices": ["두 시 서른 분", "두 시 삼십 분", "두 시 반", "세 시 십오 분"],
        "correct": "두 시 서른 분",
        "explanation": "<p>Daqiqa <strong>한자어</strong> bilan: 삼십 분. 서른 esa 고유어 va "
                       "daqiqa uchun ishlatilmaydi.</p>",
    },
    {
        "text": "<p>Sana tartibi bo'yicha koreys tili qaysi tilga oʻxshaydi?</p>",
        "choices": ["Oʻzbek tiliga — yil, oy, kun",
                    "Ingliz tiliga — oy, kun, yil",
                    "Hech qaysisiga",
                    "Rus tiliga — kun, oy, yil"],
        "correct": "Oʻzbek tiliga — yil, oy, kun",
        "explanation": "<p><em>2026-yil 2-avgust</em> → <strong>이천이십육년 팔월 이일</strong>. "
                       "Ingliz tilida esa teskari (<em>August 2, 2026</em>).</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["삼 시 삼십 분이에요.", "세 시 삼십 분이에요.",
                    "두 시 반이에요.", "열두 시예요."],
        "correct": "삼 시 삼십 분이에요.",
        "explanation": "<p>Soat <strong>고유어</strong> bilan: <em>세 시</em>. 삼 esa "
                       "한자어 va soat uchun ishlatilmaydi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["오늘은 며칠이에요?", "오늘에는 며칠이에요?",
                    "오늘에 며칠이에요?", "오늘은 몇 살이에요?"],
        "correct": "오늘은 며칠이에요?",
        "explanation": "<p><strong>오늘 에 olmaydi</strong> (PK-14). 며칠 — sana soʻraydi, "
                       "몇 살 esa yosh.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 몇 시에 학교에 가요?<br>나: ___</strong></p>",
        "choices": ["여덟 시 반에 가요.", "팔 시 반에 가요.",
                    "여덟 시 반에서 가요.", "여덟 시 반 가요."],
        "correct": "여덟 시 반에 가요.",
        "explanation": "<p>Soat <strong>고유어</strong> (여덟 시), yarim — <strong>반</strong>, "
                       "va vaqt <strong>에</strong> oladi.</p>",
    },
    {
        "text": "<p>“Dushanbadan jumagacha” ni koreyschaga oʻgiring.</p>",
        "choices": ["월요일부터 금요일까지", "월요일에서 금요일까지",
                    "월요일까지 금요일부터", "화요일부터 토요일까지"],
        "correct": "월요일부터 금요일까지",
        "explanation": "<p>Vaqt oraligʻida “…dan” uchun <strong>부터</strong> (PK-16), "
                       "va 월요일 — dushanba, 금요일 — juma.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-23 Mashq: 한자어 sonlar",
        "description": "20 savol — xitoy ildizli sonlar, 만 birligi va qayerda ishlatilishi.",
        "tutorial":    "PK-23:",
        "level":       "easy",
        "questions":   Q_PK23,
    },
    {
        "title":       "PK-24 Mashq: 고유어 sonlar va sanoq soʻzlari",
        "description": "20 savol — asl koreys sonlari, qisqarish va 개/명/마리/권.",
        "tutorial":    "PK-24:",
        "level":       "easy",
        "questions":   Q_PK24,
    },
    {
        "title":       "PK-25 Mashq: Vaqt, sana va hafta kunlari",
        "description": "20 savol — soat va daqiqa, oy istisnolari va hafta kunlari.",
        "tutorial":    "PK-25:",
        "level":       "easy",
        "questions":   Q_PK25,
    },
]
