# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-44 … PK-46.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_44_46.py --master=prime \\
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
# PK-44 — 동사 + (으)ㄴ / (으)ㄹ
# =====================================================================

Q_PK44 = [
    # 1–5 tanish
    {
        "text": "<p>Feʼl aniqlovchisining <strong>oʻtgan zamon</strong> shakli "
                "qaysi?</p>",
        "choices": ["는", "(으)ㄴ", "(으)ㄹ", "기"],
        "correct": "(으)ㄴ",
        "explanation": "<p><strong>(으)ㄴ</strong> — oʻtgan zamon: 먹은 음식 "
                       "(“yegan taom”). 는 — hozirgi, (으)ㄹ — hali boʻlmagan.</p>",
    },
    {
        "text": "<p><strong>보다</strong> ning oʻtgan zamon aniqlovchisi qaysi?</p>",
        "choices": ["봤은", "보는", "본", "볼"],
        "correct": "본",
        "explanation": "<p>보 da 받침 yoʻq → ㄴ: <strong>본 영화</strong> "
                       "(“koʻrgan kino”). Aniqlovchi ichiga 았/었 qoʻyilmaydi.</p>",
    },
    {
        "text": "<p><strong>먹다</strong> ning kelasi zamon aniqlovchisi qaysi?</p>",
        "choices": ["먹은", "먹는", "먹기", "먹을"],
        "correct": "먹을",
        "explanation": "<p>먹 da 받침 bor → 을: <strong>먹을 음식</strong> — hali "
                       "yeyilmagan taom.</p>",
    },
    {
        "text": "<p>PK-38 dagi <strong>먹은 후에</strong> — bu qanday tuzilgan?</p>",
        "choices": ["Oʻtgan zamon aniqlovchisi + 후 (ot)",
                    "Otlashtiruvchi 기 + 후",
                    "Hozirgi zamon aniqlovchisi + 후",
                    "Maxsus qolip, tuzilishi yoʻq"],
        "correct": "Oʻtgan zamon aniqlovchisi + 후 (ot)",
        "explanation": "<p>후 — “keyin” degan ot, 은 esa bugungi oʻtgan zamon "
                       "aniqlovchisi. Yaʼni siz uni PK-38 da nomini bilmasdan "
                       "ishlatgansiz.</p>",
    },
    {
        "text": "<p>Aniqlovchi ichiga <strong>았/었</strong> qoʻyiladimi?</p>",
        "choices": ["Ha, har doim", "Yoʻq — zamonni aniqlovchining oʻz shakli bildiradi",
                    "Faqat sifatlar bilan", "Faqat (으)ㄹ bilan"],
        "correct": "Yoʻq — zamonni aniqlovchining oʻz shakli bildiradi",
        "explanation": "<p><s>봤은 영화</s> emas — <strong>본 영화</strong>. "
                       "(으)ㄴ ning oʻzi allaqachon “oʻtgan” degan.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 어제 <strong>______</strong> (읽다) 책이 "
                "재미있었어요.</p>",
        "choices": ["읽는", "읽은", "읽을", "읽었은"],
        "correct": "읽은",
        "explanation": "<p>읽 da 받침 bor → 은. Ish tugagan → oʻtgan zamon.</p>",
    },
    {
        "text": "<p>Toʻldiring: 내일 <strong>______</strong> (만나다) 사람이 "
                "누구예요?</p>",
        "choices": ["만난", "만나는", "만날", "만났을"],
        "correct": "만날",
        "explanation": "<p>만나 da 받침 yoʻq → ㄹ. Ish hali boʻlmagan → "
                       "<strong>만날 사람</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 어제 <strong>______</strong> (듣다) 노래가 "
                "좋았어요.</p>",
        "choices": ["듣은", "들은", "듣는", "들는"],
        "correct": "들은",
        "explanation": "<p>듣다 — ㄷ notoʻgʻri feʼli. (으)ㄴ unli bilan "
                       "boshlanadi → ㄷ → ㄹ: <strong>들은 노래</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 서울에 <strong>______</strong> (살다) 친구를 "
                "작년에 만났어요.</p>",
        "choices": ["산", "살은", "살는", "살을"],
        "correct": "산",
        "explanation": "<p>ㄹ oʻzak ㄴ oldida ㄹ ni yoʻqotadi: 살 + ㄴ → "
                       "<strong>산</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 오늘 <strong>______</strong> (하다) 일이 많아요.</p>",
        "choices": ["한", "하는", "할", "했을"],
        "correct": "할",
        "explanation": "<p><strong>할 일</strong> — “qilinadigan ish, vazifa”. "
                       "Ish hali bajarilmagan → (으)ㄹ.</p>",
    },
    {
        "text": "<p>Toʻldiring: 냉장고에 <strong>______</strong> (먹다) 것이 "
                "없어요.</p>",
        "choices": ["먹은", "먹는", "먹기", "먹을"],
        "correct": "먹을",
        "explanation": "<p><strong>먹을 것</strong> — “yegulik”. Hali yeyilmagan "
                       "narsa → (으)ㄹ.</p>",
    },
    {
        "text": "<p>Toʻldiring: 지금 <strong>______</strong> (걷다) 사람이 제 "
                "동생이에요.</p>",
        "choices": ["걸은", "걷는", "걸을", "걸는"],
        "correct": "걷는",
        "explanation": "<p>Hozirgi zamon → <strong>는</strong>, va 는 undosh "
                       "bilan boshlangani uchun 걷 oʻzgarmaydi: 걷는.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p><strong>먹은 음식</strong> va <strong>먹을 음식</strong> — "
                "farqi nima?</p>",
        "choices": ["Birinchisi “yegan taom”, ikkinchisi “hali yemagan taom”",
                    "Birinchisi “hali yemagan”, ikkinchisi “yegan”",
                    "Birinchisi rasmiy, ikkinchisi norasmiy",
                    "Farqi yoʻq"],
        "correct": "Birinchisi “yegan taom”, ikkinchisi “hali yemagan taom”",
        "explanation": "<p>(으)ㄴ — ish tugagan. (으)ㄹ — ish hali sodir "
                       "boʻlmagan.</p>",
    },
    {
        "text": "<p>듣다 ning uchta aniqlovchi shakli qaysi qatorda toʻgʻri?</p>",
        "choices": ["듣은 · 듣는 · 듣을", "들은 · 들는 · 들을",
                    "들은 · 듣는 · 들을", "듣은 · 들는 · 듣을"],
        "correct": "들은 · 듣는 · 들을",
        "explanation": "<p>Oʻrtadagisi oʻzgarmaydi, chunki <strong>는</strong> "
                       "undosh. Chetdagi ikkitasi (으) bilan boshlangani uchun "
                       "ㄷ → ㄹ.</p>",
    },
    {
        "text": "<p>PK-27 dagi <strong>갈 거예요</strong> ichida qaysi aniqlovchi "
                "bor?</p>",
        "choices": ["(으)ㄹ", "(으)ㄴ", "는", "기"],
        "correct": "(으)ㄹ",
        "explanation": "<p>갈 = 가 + ㄹ, 거 esa “narsa” degan ot (것). Yaʼni "
                       "“boradigan narsa(m)” → “boraman”.</p>",
    },
    {
        "text": "<p>Qaysi gap notoʻgʻri?</p>",
        "choices": ["어제 간 식당", "내일 갈 식당", "지금 가는 식당", "어제 갔은 식당"],
        "correct": "어제 갔은 식당",
        "explanation": "<p>Aniqlovchi ichiga 았/었 qoʻyilmaydi. Toʻgʻrisi — "
                       "<strong>어제 간 식당</strong>.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>내일 먹은 음식을 샀어요.</strong></p>",
        "choices": ["먹은 → 먹을", "먹은 → 먹는", "샀어요 → 살 거예요", "Xato yoʻq"],
        "correct": "먹은 → 먹을",
        "explanation": "<p>Ovqat hali yeyilmagan (내일 — ertaga) → "
                       "<strong>먹을 음식</strong>.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>부산에 살은 친구가 있어요.</strong></p>",
        "choices": ["살은 → 산", "살은 → 사는", "살은 → 살", "Xato yoʻq"],
        "correct": "살은 → 산",
        "explanation": "<p>ㄹ oʻzak: 살 + ㄴ → <strong>산</strong>. (Hozir "
                       "yashayotgan boʻlsa — 사는 친구.)</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Kecha koʻrgan kino qiziq boʻldi” — qaysi biri toʻgʻri?</p>",
        "choices": ["어제 본 영화가 재미있었어요", "어제 봤은 영화가 재미있었어요",
                    "어제 볼 영화가 재미있었어요", "어제 보는 영화가 재미있었어요"],
        "correct": "어제 본 영화가 재미있었어요",
        "explanation": "<p>보다 → 본 (받침 yoʻq). Aniqlovchi ichiga zamon "
                       "qoʻyilmaydi.</p>",
    },
    {
        "text": "<p>“Bugun qiladigan ishim koʻp” — qaysi biri toʻgʻri?</p>",
        "choices": ["오늘 한 일이 많아요", "오늘 하는 일이 많아요",
                    "오늘 할 일이 많아요", "오늘 하기 일이 많아요"],
        "correct": "오늘 할 일이 많아요",
        "explanation": "<p><strong>할 일</strong> — hali bajarilmagan ish. "
                       "한 일 “qilingan ish” degani.</p>",
    },
]


# =====================================================================
# PK-45 — 형용사 + (으)ㄴ
# =====================================================================

Q_PK45 = [
    # 1–5 tanish
    {
        "text": "<p>Sifat otdan oldin turishi uchun qaysi shaklni oladi?</p>",
        "choices": ["는", "(으)ㄴ", "(으)ㄹ", "기"],
        "correct": "(으)ㄴ",
        "explanation": "<p>좋다 → <strong>좋은</strong> 사람. Sifat hech qachon "
                       "는 olmaydi.</p>",
    },
    {
        "text": "<p><strong>작다</strong> ning aniqlovchi shakli qaysi?</p>",
        "choices": ["작는", "작은", "작을", "작아"],
        "correct": "작은",
        "explanation": "<p>작 da 받침 bor → 은: <strong>작은 카페</strong>.</p>",
    },
    {
        "text": "<p><strong>예쁘다</strong> ning aniqlovchi shakli qaysi?</p>",
        "choices": ["예쁘는", "예쁜", "예쁠", "예뻐은"],
        "correct": "예쁜",
        "explanation": "<p>예쁘 da 받침 yoʻq → ㄴ: <strong>예쁜 옷</strong>.</p>",
    },
    {
        "text": "<p><strong>춥다</strong> ning aniqlovchi shakli qaysi?</p>",
        "choices": ["춥은", "추운", "추울", "춥는"],
        "correct": "추운",
        "explanation": "<p>ㅂ notoʻgʻri sifati: ㅂ → 우, keyin ㄴ. "
                       "춥 → 추우 → <strong>추운 날씨</strong>.</p>",
    },
    {
        "text": "<p>Nega <strong>맛있는 음식</strong> deyiladi, "
                "<strong>맛있은</strong> emas?</p>",
        "choices": ["맛있다 ichida 있다 — feʼl bor", "맛있다 uzun soʻz",
                    "맛있다 notoʻgʻri feʼl", "Ikkalasi ham toʻgʻri"],
        "correct": "맛있다 ichida 있다 — feʼl bor",
        "explanation": "<p>맛있다 = 맛 + 있다. Feʼllar hozirgi zamonda "
                       "<strong>는</strong> oladi. Xuddi shunday: 재미있는, "
                       "멋있는.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: <strong>______</strong> (조용하다) 곳에서 공부하고 "
                "싶어요.</p>",
        "choices": ["조용하는", "조용할", "조용해", "조용한"],
        "correct": "조용한",
        "explanation": "<p>하다 sifatlari doim <strong>한</strong> boʻladi: "
                       "조용한, 깨끗한, 따뜻한, 유명한.</p>",
    },
    {
        "text": "<p>Toʻldiring: 저는 <strong>______</strong> (맵다) 음식을 "
                "좋아해요.</p>",
        "choices": ["맵은", "매운", "맵는", "매울"],
        "correct": "매운",
        "explanation": "<p>맵다 — ㅂ notoʻgʻri sifati: ㅂ → 우 → "
                       "<strong>매운</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 이 시험은 <strong>______</strong> (어렵다) "
                "시험이에요.</p>",
        "choices": ["어렵은", "어려운", "어렵는", "어려울"],
        "correct": "어려운",
        "explanation": "<p>어렵다 → 어려우 → <strong>어려운</strong>. Juftligi: "
                       "쉽다 → 쉬운.</p>",
    },
    {
        "text": "<p>Toʻldiring: 지영 씨는 <strong>______</strong> (길다) 머리를 "
                "좋아해요.</p>",
        "choices": ["길은", "긴", "길는", "길을"],
        "correct": "긴",
        "explanation": "<p>ㄹ oʻzak ㄴ oldida ㄹ ni yoʻqotadi: 길 + ㄴ → "
                       "<strong>긴</strong>. Xuddi shunday: 멀다 → 먼.</p>",
    },
    {
        "text": "<p>Toʻldiring: 이 가방은 <strong>______</strong> (비싸다) "
                "가방이에요.</p>",
        "choices": ["비싼", "비싸은", "비싸는", "비쌀"],
        "correct": "비싼",
        "explanation": "<p>비싸 da 받침 yoʻq → ㄴ: <strong>비싼 가방</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: <strong>______</strong> 음식을 좋아해요? "
                "(“qanaqa”)</p>",
        "choices": ["어떤", "어디", "언제", "얼마"],
        "correct": "어떤",
        "explanation": "<p><strong>어떤</strong> — “qanaqa, qanday”. Javobda "
                       "sifat aniqlovchisi keladi: 매운 음식을 좋아해요.</p>",
    },
    {
        "text": "<p>Toʻldiring: 우리 학교는 <strong>______</strong> (넓다) "
                "운동장이 있어요.</p>",
        "choices": ["넓는", "넓은", "넓을", "넓어"],
        "correct": "넓은",
        "explanation": "<p>넓 da 받침 bor → 은: <strong>넓은 운동장</strong> "
                       "(“keng maydon”).</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p><strong>먹은 사람</strong> va <strong>좋은 사람</strong> — "
                "ikkalasi ham (으)ㄴ. Farqi nima?</p>",
        "choices": ["먹다 feʼl → oʻtgan zamon; 좋다 sifat → hozirgi zamon",
                    "먹다 sifat; 좋다 feʼl",
                    "Birinchisi rasmiy, ikkinchisi norasmiy",
                    "Farqi yoʻq"],
        "correct": "먹다 feʼl → oʻtgan zamon; 좋다 sifat → hozirgi zamon",
        "explanation": "<p>Shakl bir xil, maʼnoni <strong>soʻzning turi</strong> "
                       "hal qiladi. “Yegan odam” va “yaxshi odam”.</p>",
    },
    {
        "text": "<p>Qaysi soʻz koreyschada <em>sifat</em> (형용사)?</p>",
        "choices": ["먹다", "가다", "좋다", "읽다"],
        "correct": "좋다",
        "explanation": "<p>Oʻzbekcha tarjimasi sifat boʻlsa (yaxshi, katta, "
                       "sovuq), u koreyschada ham 형용사. Qolgan uchtasi "
                       "harakat bildiradi.</p>",
    },
    {
        "text": "<p>Qaysi gap notoʻgʻri?</p>",
        "choices": ["예쁜 옷", "추운 날씨", "예쁘는 옷", "긴 머리"],
        "correct": "예쁘는 옷",
        "explanation": "<p>Sifat <strong>는</strong> olmaydi. Toʻgʻrisi — "
                       "<strong>예쁜 옷</strong>.</p>",
    },
    {
        "text": "<p>Qaysi qatorda ㅂ sifatlari toʻgʻri yasalgan?</p>",
        "choices": ["추운 · 매운 · 쉬운", "춥은 · 맵은 · 쉽은",
                    "추울 · 매울 · 쉬울", "춥는 · 맵는 · 쉽는"],
        "correct": "추운 · 매운 · 쉬운",
        "explanation": "<p>ㅂ → 우, keyin ㄴ. Bu bitta qoida oltita eng koʻp "
                       "ishlatiladigan sifatni qoplaydi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>오늘은 춥은 날씨예요.</strong></p>",
        "choices": ["춥은 → 추운", "춥은 → 추울", "춥은 → 춥는", "Xato yoʻq"],
        "correct": "춥은 → 추운",
        "explanation": "<p>춥다 — ㅂ notoʻgʻri sifati: 춥 → 추우 → "
                       "<strong>추운</strong>.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>어제 재미있은 영화를 봤어요.</strong></p>",
        "choices": ["재미있은 → 재미있는", "재미있은 → 재미있을",
                    "봤어요 → 보는", "Xato yoʻq"],
        "correct": "재미있은 → 재미있는",
        "explanation": "<p>재미있다 ichida 있다 (feʼl) bor → "
                       "<strong>는</strong> oladi.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Men achchiq taomlarni yaxshi koʻraman” — qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["저는 맵은 음식을 좋아해요", "저는 매운 음식을 좋아해요",
                    "저는 맵는 음식을 좋아해요", "저는 매울 음식을 좋아해요"],
        "correct": "저는 매운 음식을 좋아해요",
        "explanation": "<p>맵다 → <strong>매운</strong> (ㅂ → 우).</p>",
    },
    {
        "text": "<p>“Tinch va toza kafe” — qaysi biri toʻgʻri?</p>",
        "choices": ["조용하고 깨끗한 카페", "조용하는 깨끗하는 카페",
                    "조용할 깨끗할 카페", "조용해 깨끗해 카페"],
        "correct": "조용하고 깨끗한 카페",
        "explanation": "<p>Ikki sifatni <strong>고</strong> (PK-33) bilan "
                       "bogʻlaymiz, oxirgisiga aniqlovchi shakli qoʻyiladi: "
                       "조용하고 <strong>깨끗한</strong> 카페.</p>",
    },
]


# =====================================================================
# PK-46 — 는 것, 기, (으)ㅁ
# =====================================================================

Q_PK46 = [
    # 1–5 tanish
    {
        "text": "<p><strong>것</strong> — bu nima?</p>",
        "choices": ["“Narsa” degan oddiy ot", "Feʼl qoʻshimchasi",
                    "Soʻroq soʻzi", "Bogʻlovchi"],
        "correct": "“Narsa” degan oddiy ot",
        "explanation": "<p>Kuchi shundaki, oldiga istalgan aniqlovchi qoʻyish "
                       "mumkin: 먹는 것 · 먹은 것 · 먹을 것.</p>",
    },
    {
        "text": "<p>TOPIK varaqasidagi <strong>읽기</strong> nima degani?</p>",
        "choices": ["Oʻqigan", "Oʻqish", "Oʻqiydigan", "Oʻqiyapman"],
        "correct": "Oʻqish",
        "explanation": "<p>읽다 + 기 = <strong>읽기</strong> — oʻzbekchadagi "
                       "“-ish” qoʻshimchasining aynan juftligi. Xuddi shunday: "
                       "쓰기, 듣기, 말하기.</p>",
    },
    {
        "text": "<p><strong>것이</strong> ogʻzaki nutqda qanday qisqaradi?</p>",
        "choices": ["게", "걸", "건", "거"],
        "correct": "게",
        "explanation": "<p>것이 → <strong>게</strong>, 것을 → 걸, 것은 → 건, "
                       "것이에요 → 거예요.</p>",
    },
    {
        "text": "<p><strong>갈 거예요</strong> ning toʻliq shakli qaysi?</p>",
        "choices": ["갈 것이에요", "가기 이에요", "간 것이에요", "가는 것이에요"],
        "correct": "갈 것이에요",
        "explanation": "<p>것 + 이에요 → 거예요. Yaʼni PK-27 dagi qolip aslida "
                       "<strong>aniqlovchi + ot + 이다</strong>.</p>",
    },
    {
        "text": "<p><strong>(으)ㅁ</strong> qayerda ishlatiladi?</p>",
        "choices": ["Kundalik suhbatda", "Tayyor soʻzlar va eʼlonlarda",
                    "Faqat savollarda", "Faqat oʻtgan zamonda"],
        "correct": "Tayyor soʻzlar va eʼlonlarda",
        "explanation": "<p>도움, 웃음, 있음, 없음 — bular tayyor soʻzlar. "
                       "Yangi soʻz yasash uchun oʻzingiz ishlatmang.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 한국 노래를 <strong>______</strong> (듣다) 것을 "
                "좋아해요.</p>",
        "choices": ["들은", "듣는", "들을", "듣기"],
        "correct": "듣는",
        "explanation": "<p>는 undosh bilan boshlanadi → 듣 oʻzgarmaydi: "
                       "<strong>듣는 것을</strong> (ogʻzaki: 듣는 걸).</p>",
    },
    {
        "text": "<p>Toʻldiring: 이 문제는 <strong>______</strong> (풀다) "
                "쉬워요.</p>",
        "choices": ["푸는 것", "풀기", "푼 것", "풀 것"],
        "correct": "풀기",
        "explanation": "<p>쉽다 / 어렵다 bilan doim <strong>기</strong> "
                       "keladi: 풀기 쉬워요.</p>",
    },
    {
        "text": "<p>Toʻldiring: 냉장고에 <strong>______</strong> 것이 없어요. "
                "(“yegulik”)</p>",
        "choices": ["먹은", "먹는", "먹기", "먹을"],
        "correct": "먹을",
        "explanation": "<p><strong>먹을 것</strong> — hali yeyilmagan narsa. "
                       "Ogʻzaki: 먹을 게 없어요.</p>",
    },
    {
        "text": "<p>Toʻldiring: 이 카페는 <strong>______</strong> (공부하다) "
                "좋아요.</p>",
        "choices": ["공부하는 것", "공부한 것", "공부하기", "공부할 것"],
        "correct": "공부하기",
        "explanation": "<p><strong>기 좋다</strong> — “…ish uchun yaxshi”: "
                       "공부하기 좋아요.</p>",
    },
    {
        "text": "<p>Toʻldiring: 비가 <strong>______</strong> (오다) "
                "시작했어요.</p>",
        "choices": ["오는 것", "온 것", "올 것", "오기"],
        "correct": "오기",
        "explanation": "<p><strong>기 시작하다</strong> — “…ishni boshlamoq”: "
                       "비가 오기 시작했어요 (“yomgʻir yogʻa boshladi”).</p>",
    },
    {
        "text": "<p>Toʻldiring: 제가 <strong>______</strong> (좋아하다) 것은 "
                "음악이에요.</p>",
        "choices": ["좋아하는", "좋아한", "좋아할", "좋아하기"],
        "correct": "좋아하는",
        "explanation": "<p>좋아하다 — feʼl, hozirgi zamonda "
                       "<strong>는</strong> oladi.</p>",
    },
    {
        "text": "<p><strong>돕다</strong> dan yasalgan ot qaysi?</p>",
        "choices": ["돕기", "도움", "돕는 것", "도울 것"],
        "correct": "도움",
        "explanation": "<p>돕다 → <strong>도움</strong> (“yordam”) — (으)ㅁ "
                       "bilan yasalgan tayyor soʻz.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p><strong>는 것</strong> va <strong>기</strong> — asosiy farqi "
                "nima?</p>",
        "choices": ["는 것 butun gapni otga aylantiradi va zamoni bor; 기 esa "
                    "ish-harakatning nomi, zamoni yoʻq",
                    "기 butun gapni otga aylantiradi",
                    "는 것 faqat yozma nutqda",
                    "Farqi yoʻq"],
        "correct": "는 것 butun gapni otga aylantiradi va zamoni bor; 기 esa "
                   "ish-harakatning nomi, zamoni yoʻq",
        "explanation": "<p>는/은/을 것 — uch zamonda. 기 esa zamonsiz va maʼlum "
                       "soʻzlar bilan mustahkam birikadi (쉽다, 어렵다, 좋다, "
                       "시작하다, 전에).</p>",
    },
    {
        "text": "<p>PK-38 dagi <strong>기 전에</strong> — bu qanday tuzilgan?</p>",
        "choices": ["Otlashtiruvchi 기 + 전 (ot)", "Aniqlovchi 는 + 전",
                    "Maxsus qolip, tuzilishi yoʻq", "Feʼl + bogʻlovchi"],
        "correct": "Otlashtiruvchi 기 + 전 (ot)",
        "explanation": "<p>전 — “oldin” degan ot. 먹기 전에 = “yeyish "
                       "oldidan”. Yaʼni siz 기 ni sakkiz dars oldin "
                       "ishlatgansiz.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["이 책은 읽는 것 쉬워요", "이 책은 읽기 쉬워요",
                    "이 책은 읽을 것 쉬워요", "이 책은 읽은 것 쉬워요"],
        "correct": "이 책은 읽기 쉬워요",
        "explanation": "<p>쉽다 bilan <strong>기</strong> keladi, 는 것 emas.</p>",
    },
    {
        "text": "<p><strong>먹는 것이 많아요</strong> va <strong>먹을 것이 "
                "많아요</strong> — farqi nima?</p>",
        "choices": ["Birinchisi “yeyish koʻp”, ikkinchisi “yegulik koʻp”",
                    "Birinchisi “yegulik koʻp”, ikkinchisi “yeyish koʻp”",
                    "Ikkalasi bir xil",
                    "Ikkinchisi notoʻgʻri"],
        "correct": "Birinchisi “yeyish koʻp”, ikkinchisi “yegulik koʻp”",
        "explanation": "<p>것 oldidagi aniqlovchi maʼnoni oʻzgartiradi: "
                       "는 것 — jarayon, (으)ㄹ 것 — hali ishlatilmagan "
                       "predmet.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>이 책은 읽는 것 어려워요.</strong></p>",
        "choices": ["읽는 것 → 읽기", "읽는 것 → 읽은 것", "어려워요 → 어렵는",
                    "Xato yoʻq"],
        "correct": "읽는 것 → 읽기",
        "explanation": "<p>어렵다 bilan <strong>기</strong> keladi: "
                       "이 책은 읽기 어려워요.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>냉장고에 먹기 것이 없어요.</strong></p>",
        "choices": ["먹기 → 먹을", "먹기 → 먹은", "것이 → 것을", "Xato yoʻq"],
        "correct": "먹기 → 먹을",
        "explanation": "<p>것 oldiga <strong>aniqlovchi</strong> keladi, 기 "
                       "emas: 먹을 것이 없어요.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Koreys tilini oʻrganish qiziqarli” — qaysi biri toʻgʻri?</p>",
        "choices": ["한국어를 배우기가 재미있어요",
                    "한국어를 배우는 것이 재미있어요",
                    "한국어를 배운 것이 재미있어요",
                    "한국어를 배울 것이 재미있어요"],
        "correct": "한국어를 배우는 것이 재미있어요",
        "explanation": "<p>Umumiy fikr bildirayotganda <strong>는 것</strong> "
                       "tabiiy. Ogʻzaki nutqda: 배우는 게 재미있어요.</p>",
    },
    {
        "text": "<p>“Bu kafe dars qilish uchun yaxshi” — qaysi biri toʻgʻri?</p>",
        "choices": ["이 카페는 공부하는 것 좋아요", "이 카페는 공부하기 좋아요",
                    "이 카페는 공부한 것 좋아요", "이 카페는 공부할 것 좋아요"],
        "correct": "이 카페는 공부하기 좋아요",
        "explanation": "<p><strong>기 좋다</strong> — mustahkam birikma: "
                       "공부하기 좋아요.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-44 Mashq: Aniqlovchi 2 — (으)ㄴ va (으)ㄹ",
        "description": "20 savol — oʻtgan va kelasi aniqlovchisi, notoʻgʻri "
                       "feʼllar, ㄹ oʻzaklar va uchta zamonning farqi.",
        "tutorial":    "PK-44:",
        "level":       "medium",
        "questions":   Q_PK44,
    },
    {
        "title":       "PK-45 Mashq: Aniqlovchi 3 — 형용사 + (으)ㄴ",
        "description": "20 savol — sifat aniqlovchisi, ㅂ sifatlari, 하다 "
                       "guruhi va feʼl bilan chalkashmaslik.",
        "tutorial":    "PK-45:",
        "level":       "medium",
        "questions":   Q_PK45,
    },
    {
        "title":       "PK-46 Mashq: Otlashtirish — 는 것, 기, (으)ㅁ",
        "description": "20 savol — 는 것 ning zamonlari, 게/걸/건 qisqarishlari, "
                       "기 birikmalari va (으)ㅁ.",
        "tutorial":    "PK-46:",
        "level":       "medium",
        "questions":   Q_PK46,
    },
]
