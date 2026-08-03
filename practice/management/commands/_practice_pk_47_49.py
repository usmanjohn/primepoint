# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-47 … PK-49.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_47_49.py --master=prime \\
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
# PK-47 — 르, ㅅ, ㅎ notoʻgʻri feʼllari
# =====================================================================

Q_PK47 = [
    # 1–5 tanish
    {
        "text": "<p>Notoʻgʻri tuslanish qachon ishlaydi?</p>",
        "choices": ["Unli bilan boshlanadigan qoʻshimcha oldida",
                    "Undosh bilan boshlanadigan qoʻshimcha oldida",
                    "Har doim", "Faqat oʻtgan zamonda"],
        "correct": "Unli bilan boshlanadigan qoʻshimcha oldida",
        "explanation": "<p>Bu qoida PK-32 dan beri oʻzgarmagan va oltita "
                       "guruhning hammasiga tegishli.</p>",
    },
    {
        "text": "<p><strong>모르다</strong> ning 아/어요 shakli qaysi?</p>",
        "choices": ["모라요", "몰라요", "모르요", "몰러요"],
        "correct": "몰라요",
        "explanation": "<p>르 guruhi: 으 tushadi va ㄹ ikkilanadi. 모르 dagi "
                       "oldingi unli ㅗ → <strong>몰라요</strong>.</p>",
    },
    {
        "text": "<p><strong>짓다</strong> ning 아/어요 shakli qaysi?</p>",
        "choices": ["짓어요", "지어요", "져요", "짇어요"],
        "correct": "지어요",
        "explanation": "<p>ㅅ guruhi: ㅅ tushadi, lekin unlilar qisqarmaydi — "
                       "<strong>지어요</strong>.</p>",
    },
    {
        "text": "<p><strong>빨갛다</strong> ning 아/어요 shakli qaysi?</p>",
        "choices": ["빨갛아요", "빨가요", "빨개요", "빨아요"],
        "correct": "빨개요",
        "explanation": "<p>ㅎ guruhi: 아/어 oldida ㅎ tushadi va unli "
                       "<strong>ㅐ</strong> ga aylanadi — 빨개요.</p>",
    },
    {
        "text": "<p>Quyidagilardan qaysi biri <em>toʻgʻri</em> feʼl (notoʻgʻri "
                "emas)?</p>",
        "choices": ["짓다", "낫다", "씻다", "붓다"],
        "correct": "씻다",
        "explanation": "<p>씻다 → <strong>씻어요</strong> — ㅅ tushmaydi. Xuddi "
                       "shunday 웃다, 벗다. Oʻzak ㅅ bilan tugagani hali hech "
                       "nimani anglatmaydi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 지영 씨가 노래를 <strong>______</strong> "
                "(부르다).</p>",
        "choices": ["불러요", "부러요", "불라요", "부르요"],
        "correct": "불러요",
        "explanation": "<p>부르 dagi oldingi unli ㅜ (ㅏ ham, ㅗ ham emas) → "
                       "<strong>러</strong>: 불러요.</p>",
    },
    {
        "text": "<p>Toʻldiring: 이 가방은 그 가방하고 <strong>______</strong> "
                "(다르다).</p>",
        "choices": ["달러요", "다러요", "달라요", "다르요"],
        "correct": "달라요",
        "explanation": "<p>다르 dagi oldingi unli ㅏ → <strong>라</strong>: "
                       "달라요.</p>",
    },
    {
        "text": "<p>Toʻldiring: 저는 그 사람을 <strong>______</strong>. "
                "(“tanimayman”)</p>",
        "choices": ["안 알아요", "몰라요", "모르요", "안 몰라요"],
        "correct": "몰라요",
        "explanation": "<p>Koreyschada “bilmaslik” uchun alohida feʼl bor — "
                       "<strong>모르다</strong>. <s>안 알아요</s> deyilmaydi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 감기가 <strong>______</strong> (낫다) 학교에 "
                "갔어요.</p>",
        "choices": ["낫아서", "나아서", "나서", "낳아서"],
        "correct": "나아서",
        "explanation": "<p>낫다 — ㅅ notoʻgʻri feʼli: ㅅ tushadi, unlilar "
                       "qisqarmaydi → <strong>나아서</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 저는 <strong>______</strong> (파랗다) 옷을 "
                "좋아해요.</p>",
        "choices": ["파랗은", "파래", "파란", "파랗는"],
        "correct": "파란",
        "explanation": "<p>(으)ㄴ oldida ㅎ tushadi va faqat ㄴ qoladi: "
                       "<strong>파란 옷</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 저는 그 노래를 <strong>______</strong> 사람을 "
                "찾고 있어요. (모르다 — hozirgi aniqlovchi)</p>",
        "choices": ["몰라는", "모르는", "몰르는", "모른"],
        "correct": "모르는",
        "explanation": "<p>는 undosh bilan boshlanadi → 르 guruhi "
                       "<strong>oʻzgarmaydi</strong>: 모르는.</p>",
    },
    {
        "text": "<p>Toʻldiring: 오늘 날씨가 <strong>______</strong> (좋다).</p>",
        "choices": ["좋아요", "좨요", "좋애요", "조요"],
        "correct": "좋아요",
        "explanation": "<p>좋다 ㅎ guruhiga <strong>kirmaydi</strong> — u "
                       "toʻliq toʻgʻri feʼl: 좋아요, 좋은.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p><strong>어떤</strong> soʻzi qanday yasalgan?</p>",
        "choices": ["어떻다 + (으)ㄴ", "어디 + 은", "어떻다 + 는", "Yasalmagan, alohida soʻz"],
        "correct": "어떻다 + (으)ㄴ",
        "explanation": "<p>ㅎ tushadi va ㄴ qoladi. Xuddi shunday 그런 = 그렇다 + "
                       "(으)ㄴ, 이런 = 이렇다 + (으)ㄴ.</p>",
    },
    {
        "text": "<p>Nega <strong>모르면</strong> da hech nima oʻzgarmaydi?</p>",
        "choices": ["르 guruhi faqat 아/어 oldida oʻzgaradi",
                    "(으)면 rasmiy shakl",
                    "모르다 toʻgʻri feʼl",
                    "Bu istisno"],
        "correct": "르 guruhi faqat 아/어 oldida oʻzgaradi",
        "explanation": "<p>몰라요 (아/어 → oʻzgargan), lekin 모르면, 모르고, "
                       "모르는 — hammasi oʻzgarishsiz.</p>",
    },
    {
        "text": "<p>Qaysi qatorda hammasi toʻgʻri yasalgan?</p>",
        "choices": ["몰라요 · 지어요 · 빨개요", "모라요 · 짓어요 · 빨갛아요",
                    "몰러요 · 져요 · 빨가요", "모르요 · 지으요 · 빨래요"],
        "correct": "몰라요 · 지어요 · 빨개요",
        "explanation": "<p>르 → ㄹ ikkilanadi; ㅅ → ㅅ tushadi, unli qoladi; "
                       "ㅎ → ㅎ tushadi, unli ㅐ boʻladi.</p>",
    },
    {
        "text": "<p>“Olma qizil” va “qizil olma” — koreyschada qaysi juftlik "
                "toʻgʻri?</p>",
        "choices": ["사과가 빨개요 · 빨간 사과", "사과가 빨간 · 빨개요 사과",
                    "사과가 빨갛아요 · 빨갛은 사과", "Ikkalasi ham 빨개요"],
        "correct": "사과가 빨개요 · 빨간 사과",
        "explanation": "<p>Ranglarni <strong>juft holda</strong> yodlash kerak: "
                       "kesim shakli (빨개요) va aniqlovchi shakli (빨간).</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>손을 시어요.</strong></p>",
        "choices": ["시어요 → 씻어요", "시어요 → 지어요", "손을 → 손이", "Xato yoʻq"],
        "correct": "시어요 → 씻어요",
        "explanation": "<p>씻다 — toʻgʻri feʼl, ㅅ tushmaydi: "
                       "<strong>씻어요</strong>.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>동생이 노래를 부러요.</strong></p>",
        "choices": ["부러요 → 불러요", "부러요 → 불라요", "부러요 → 부르요",
                    "Xato yoʻq"],
        "correct": "부러요 → 불러요",
        "explanation": "<p>르 guruhida ㄹ <strong>ikkilanadi</strong>: "
                       "부르 → 불러. Bitta ㄹ yetmaydi.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Men u qoʻshiqni bilmayman” — qaysi biri toʻgʻri?</p>",
        "choices": ["저는 그 노래를 안 알아요", "저는 그 노래를 몰라요",
                    "저는 그 노래를 모르요", "저는 그 노래를 안 몰라요"],
        "correct": "저는 그 노래를 몰라요",
        "explanation": "<p>알다 / 모르다 — juftlik, xuddi 있다 / 없다 kabi.</p>",
    },
    {
        "text": "<p>“Oq futbolka sotib oldim” — qaysi biri toʻgʻri?</p>",
        "choices": ["하얗은 티셔츠를 샀어요", "하얀 티셔츠를 샀어요",
                    "하얘요 티셔츠를 샀어요", "하얗는 티셔츠를 샀어요"],
        "correct": "하얀 티셔츠를 샀어요",
        "explanation": "<p>하얗다 + (으)ㄴ → ㅎ tushadi → <strong>하얀</strong>. "
                       "Kesim shakli esa 하얘요.</p>",
    },
]


# =====================================================================
# PK-48 — (으)니까
# =====================================================================

Q_PK48 = [
    # 1–5 tanish
    {
        "text": "<p><strong>(으)니까</strong> ning 아/어서 dan asosiy farqi nima?</p>",
        "choices": ["Undan keyin buyruq kelishi mumkin",
                    "U faqat yozma nutqda ishlatiladi",
                    "U faqat sifatlar bilan keladi",
                    "Farqi yoʻq"],
        "correct": "Undan keyin buyruq kelishi mumkin",
        "explanation": "<p>배가 아프니까 병원에 <strong>가세요</strong> ✓ · "
                       "<s>아파서 가세요</s> ✗. PK-35 da vaʼda qilingan javob "
                       "aynan shu.</p>",
    },
    {
        "text": "<p><strong>먹다</strong> ning (으)니까 shakli qaysi?</p>",
        "choices": ["먹니까", "먹으니까", "먹어니까", "먹는니까"],
        "correct": "먹으니까",
        "explanation": "<p>먹 da 받침 bor → <strong>으니까</strong>.</p>",
    },
    {
        "text": "<p>(으)니까 dan oldin oʻtgan zamon qoʻyiladimi?</p>",
        "choices": ["Ha, qoʻyiladi", "Yoʻq, hech qachon", "Faqat sifatlar bilan",
                    "Faqat inkorda"],
        "correct": "Ha, qoʻyiladi",
        "explanation": "<p>어제 비가 <strong>왔으니까</strong> 오늘은 길이 안 "
                       "좋아요. Bu ham 아/어서 dan farq qiladi.</p>",
    },
    {
        "text": "<p>Uzr soʻraganda qaysi qolip ishlatiladi?</p>",
        "choices": ["(으)니까", "아/어서", "기 때문에", "(으)면"],
        "correct": "아/어서",
        "explanation": "<p>늦<strong>어서</strong> 죄송합니다. <s>늦으니까 "
                       "죄송합니다</s> qoʻpol eshitiladi — goʻyo bahona "
                       "qilayotgandek.</p>",
    },
    {
        "text": "<p><strong>창문을 여니까 비가 왔어요</strong> nima degani?</p>",
        "choices": ["Deraza ochganim uchun yomgʻir yogʻdi",
                    "Derazani ochsam, yomgʻir yogʻayotgan ekan",
                    "Agar derazani ochsam, yomgʻir yogʻadi",
                    "Derazani ochib yomgʻirni koʻrdim"],
        "correct": "Derazani ochsam, yomgʻir yogʻayotgan ekan",
        "explanation": "<p>Bu (으)니까 ning ikkinchi vazifasi — "
                       "<strong>kashfiyot</strong>. Sabab emas: deraza yomgʻirni "
                       "chaqirmagan.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 시간이 <strong>______</strong> (없다) 빨리 "
                "가세요.</p>",
        "choices": ["없니까", "없어서", "없으니까", "없기 때문에"],
        "correct": "없으니까",
        "explanation": "<p>없 da 받침 bor → 으니까. Keyin buyruq (가세요) bor, "
                       "shuning uchun 아/어서 ham, 기 때문에 ham boʻlmaydi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 음악을 <strong>______</strong> (듣다) 기분이 "
                "좋아요.</p>",
        "choices": ["듣으니까", "들으니까", "듣니까", "들니까"],
        "correct": "들으니까",
        "explanation": "<p>듣다 — ㄷ notoʻgʻri feʼli, (으) unli bilan "
                       "boshlanadi → ㄷ → ㄹ.</p>",
    },
    {
        "text": "<p>Toʻldiring: 서울에 <strong>______</strong> (살다) 지하철을 "
                "자주 타요.</p>",
        "choices": ["살니까", "사니까", "살으니까", "삶니까"],
        "correct": "사니까",
        "explanation": "<p>ㄹ oʻzak ㄴ oldida ㄹ ni yoʻqotadi: 살 + 니까 → "
                       "<strong>사니까</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 날씨가 <strong>______</strong> (덥다) 창문을 "
                "여세요.</p>",
        "choices": ["덥으니까", "더우니까", "덥니까", "더워니까"],
        "correct": "더우니까",
        "explanation": "<p>덥다 — ㅂ notoʻgʻri feʼli: ㅂ → 우 → "
                       "<strong>더우니까</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 어제 비가 <strong>______</strong> 오늘은 길이 안 "
                "좋아요.</p>",
        "choices": ["와서", "오니까", "왔으니까", "오기 때문에"],
        "correct": "왔으니까",
        "explanation": "<p>(으)니까 oldida oʻtgan zamon bemalol turadi: "
                       "<strong>왔으니까</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 집에 <strong>______</strong> (가다) 아무도 "
                "없었어요.</p>",
        "choices": ["가니까", "가서", "갔으니까", "가기 때문에"],
        "correct": "가니까",
        "explanation": "<p>Kashfiyot maʼnosi: “uyga borsam, hech kim yoʻq "
                       "ekan”. Birinchi qism zamonsiz, ikkinchisi oʻtgan "
                       "zamonda.</p>",
    },
    {
        "text": "<p>Toʻldiring: 도와<strong>______</strong> 고맙습니다.</p>",
        "choices": ["주니까", "줘서", "주기 때문에", "주면"],
        "correct": "줘서",
        "explanation": "<p>Rahmat aytganda doim <strong>아/어서</strong>: "
                       "도와줘서 고맙습니다.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["배가 아파서 병원에 가세요", "배가 아프니까 병원에 가세요",
                    "배가 아프기 때문에 병원에 가세요", "배가 아프면 병원에 갔어요"],
        "correct": "배가 아프니까 병원에 가세요",
        "explanation": "<p>Keyin buyruq bor → faqat (으)니까 mumkin.</p>",
    },
    {
        "text": "<p>아/어서 va (으)니까 — qaysi biri subyektiv (soʻzlovchining "
                "fikri)?</p>",
        "choices": ["(으)니까", "아/어서", "Ikkalasi ham", "Hech qaysisi"],
        "correct": "(으)니까",
        "explanation": "<p>아/어서 — obyektiv, umumiy sabab. (으)니까 — "
                       "soʻzlovchi shunday deb hisoblayapti, shuning uchun "
                       "undan keyin buyruq tabiiy.</p>",
    },
    {
        "text": "<p>Bu gapda (으)니까 qaysi maʼnoda? "
                "<strong>가게에 가니까 사람이 아주 많았어요.</strong></p>",
        "choices": ["Sabab", "Kashfiyot", "Shart", "Buyruq"],
        "correct": "Kashfiyot",
        "explanation": "<p>“Doʻkonga borsam, odam juda koʻp ekan”. Doʻkonga "
                       "borgani odamni koʻpaytirmagan — bu sabab emas.</p>",
    },
    {
        "text": "<p>Qaysi gap notoʻgʻri?</p>",
        "choices": ["늦어서 죄송합니다", "늦으니까 죄송합니다",
                    "비가 오니까 우산을 가져가세요", "시간이 없어서 못 갔어요"],
        "correct": "늦으니까 죄송합니다",
        "explanation": "<p>Uzr soʻraganda faqat <strong>아/어서</strong>. "
                       "(으)니까 bu yerda bahona qilayotgandek eshitiladi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>밥을 먹니까 배가 안 고파요.</strong></p>",
        "choices": ["먹니까 → 먹으니까", "먹니까 → 먹어서", "고파요 → 고프니까",
                    "Xato yoʻq"],
        "correct": "먹니까 → 먹으니까",
        "explanation": "<p>먹 da 받침 bor → <strong>으니까</strong>.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>서울에 살니까 자주 가요.</strong></p>",
        "choices": ["살니까 → 사니까", "살니까 → 살으니까", "살니까 → 삽니까",
                    "Xato yoʻq"],
        "correct": "살니까 → 사니까",
        "explanation": "<p>ㄹ oʻzak ㄴ oldida ㄹ ni yoʻqotadi.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Yomgʻir yogʻyapti, shuning uchun soyabon oling” — qaysi "
                "biri toʻgʻri?</p>",
        "choices": ["비가 와서 우산을 가져가세요", "비가 오니까 우산을 가져가세요",
                    "비가 오기 때문에 우산을 가져가세요", "비가 오면 우산을 가져갔어요"],
        "correct": "비가 오니까 우산을 가져가세요",
        "explanation": "<p>Keyin buyruq bor → (으)니까. 오 da 받침 yoʻq → "
                       "니까.</p>",
    },
    {
        "text": "<p>“Uyga borsam, hech kim yoʻq edi” — qaysi biri toʻgʻri?</p>",
        "choices": ["집에 가니까 아무도 없었어요", "집에 가면 아무도 없었어요",
                    "집에 가서 아무도 없었어요", "집에 갔으니까 아무도 없었어요"],
        "correct": "집에 가니까 아무도 없었어요",
        "explanation": "<p>Kashfiyot maʼnosida birinchi qism zamonsiz turadi. "
                       "(으)면 boʻlsa “agar borsam” degan shart chiqadi.</p>",
    },
]


# =====================================================================
# PK-49 — 기 때문에 / 명사 + 때문에
# =====================================================================

Q_PK49 = [
    # 1–5 tanish
    {
        "text": "<p><strong>명사 + 때문에</strong> nima maʼnoni beradi?</p>",
        "choices": ["… sababli, … tufayli", "…dan keyin", "…dan oldin",
                    "… bilan birga"],
        "correct": "… sababli, … tufayli",
        "explanation": "<p>비 때문에 — “yomgʻir sababli”. Oʻzbekcha bilan soʻz "
                       "tartibi ham, tuzilishi ham bir xil.</p>",
    },
    {
        "text": "<p>Feʼl bilan 때문에 qanday ishlatiladi?</p>",
        "choices": ["Oʻzak + 때문에", "Oʻzak + 기 때문에", "Oʻzak + 는 때문에",
                    "Oʻzak + 아/어 때문에"],
        "correct": "Oʻzak + 기 때문에",
        "explanation": "<p>Oʻrtaga <strong>기</strong> (PK-46 dagi "
                       "otlashtiruvchi) qoʻyiladi: 바쁘기 때문에.</p>",
    },
    {
        "text": "<p>기 때문에 dan keyin buyruq kelishi mumkinmi?</p>",
        "choices": ["Ha, har doim", "Yoʻq — buyruq uchun (으)니까 kerak",
                    "Faqat rasmiy nutqda", "Faqat oʻtgan zamonda"],
        "correct": "Yoʻq — buyruq uchun (으)니까 kerak",
        "explanation": "<p><s>비가 오기 때문에 우산을 가져가세요</s> ✗ → "
                       "비가 <strong>오니까</strong> 우산을 가져가세요 ✓.</p>",
    },
    {
        "text": "<p>기 때문에 ning uslubi qanday?</p>",
        "choices": ["Kundalik suhbat", "Rasmiy va yozma",
                    "Faqat bolalar nutqi", "Faqat savollarda"],
        "correct": "Rasmiy va yozma",
        "explanation": "<p>Gazetada, inshoda va TOPIK yozish qismida eng koʻp "
                       "uchraydigan sabab qolipi.</p>",
    },
    {
        "text": "<p>Ot + 이다 bilan qanday boʻladi?</p>",
        "choices": ["학생 때문에", "학생이기 때문에", "학생기 때문에",
                    "학생이 때문에"],
        "correct": "학생이기 때문에",
        "explanation": "<p>“Talaba boʻlganim uchun” — <strong>이기 "
                       "때문에</strong>. 학생 때문에 esa “talaba tufayli” "
                       "(boshqa odam) degani.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: <strong>______</strong> 때문에 오늘 학교에 못 "
                "갔어요. (“qor”)</p>",
        "choices": ["눈이", "눈을", "눈", "눈은"],
        "correct": "눈",
        "explanation": "<p>때문에 oldidagi otga <strong>qoʻshimcha "
                       "qoʻyilmaydi</strong>: 눈 때문에.</p>",
    },
    {
        "text": "<p>Toʻldiring: 시험이 <strong>______</strong> (어렵다) 때문에 "
                "많이 공부했어요.</p>",
        "choices": ["어렵기", "어려우기", "어려워", "어려운"],
        "correct": "어렵기",
        "explanation": "<p>기 undosh bilan boshlanadi, shuning uchun ㅂ "
                       "notoʻgʻri sifati <strong>oʻzgarmaydi</strong>: "
                       "어렵기 때문에.</p>",
    },
    {
        "text": "<p>Toʻldiring: 어제 늦게 <strong>______</strong> (자다) 때문에 "
                "오늘 피곤해요.</p>",
        "choices": ["자기", "잤기", "잔", "자는"],
        "correct": "잤기",
        "explanation": "<p>기 때문에 oldida oʻtgan zamon qoʻyilishi mumkin: "
                       "<strong>잤기 때문에</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 음악을 <strong>______</strong> (듣다) 때문에 "
                "숙제를 못 했어요.</p>",
        "choices": ["들으기", "듣기", "들기", "들은기"],
        "correct": "듣기",
        "explanation": "<p>기 undosh → 듣 oʻzgarmaydi: <strong>듣기 "
                       "때문에</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 저는 <strong>______</strong> 때문에 시간이 "
                "없어요. (“talaba boʻlganim uchun”)</p>",
        "choices": ["학생", "학생이기", "학생기", "학생은"],
        "correct": "학생이기",
        "explanation": "<p>Oʻzingiz haqingizda aytayotgan boʻlsangiz — "
                       "<strong>이기 때문에</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 비가 와요. <strong>______</strong> 우산을 "
                "가져가세요.</p>",
        "choices": ["그래서", "그러니까", "그렇기 때문에", "그러면"],
        "correct": "그러니까",
        "explanation": "<p>Keyin buyruq bor → <strong>그러니까</strong>. "
                       "그래서 va 그렇기 때문에 dan keyin buyruq kelmaydi.</p>",
    },
    {
        "text": "<p>Toʻldiring: <strong>______</strong> 때문에 요즘 바빠요. "
                "(“imtihon”)</p>",
        "choices": ["시험", "시험이", "시험을", "시험이기"],
        "correct": "시험",
        "explanation": "<p>시험 — ot, shuning uchun 기 ham, qoʻshimcha ham "
                       "kerak emas: <strong>시험 때문에</strong>.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Uchta sabab qolipidan qaysi biridan keyin <em>buyruq</em> "
                "kelishi mumkin?</p>",
        "choices": ["아/어서", "(으)니까", "기 때문에", "Uchalasidan ham"],
        "correct": "(으)니까",
        "explanation": "<p>아/어서 va 기 때문에 — buyruqsiz. Faqat "
                       "<strong>(으)니까</strong> buyruq koʻtaradi.</p>",
    },
    {
        "text": "<p><strong>학생 때문에</strong> va <strong>학생이기 "
                "때문에</strong> — farqi nima?</p>",
        "choices": ["Birinchisi “talaba tufayli”, ikkinchisi “talaba boʻlganim uchun”",
                    "Birinchisi rasmiy, ikkinchisi norasmiy",
                    "Birinchisi notoʻgʻri",
                    "Farqi yoʻq"],
        "correct": "Birinchisi “talaba tufayli”, ikkinchisi “talaba boʻlganim uchun”",
        "explanation": "<p>Birinchisida sabab — boshqa odam. Ikkinchisida "
                       "sabab — oʻzingizning holatingiz.</p>",
    },
    {
        "text": "<p>TOPIK yozish qismida qaysi sabab qolipi eng mos?</p>",
        "choices": ["아/어서", "(으)니까", "기 때문에", "(으)면"],
        "correct": "기 때문에",
        "explanation": "<p>기 때문에 — rasmiy va yozma uslub. Insho matnida "
                       "aynan shu kutiladi.</p>",
    },
    {
        "text": "<p>Qaysi gap notoʻgʻri?</p>",
        "choices": ["비 때문에 늦었어요", "바쁘기 때문에 못 갔어요",
                    "도와줬기 때문에 고맙습니다", "학생이기 때문에 시간이 없어요"],
        "correct": "도와줬기 때문에 고맙습니다",
        "explanation": "<p>Rahmat va uzrda faqat <strong>아/어서</strong>: "
                       "도와<strong>줘서</strong> 고맙습니다.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>비가 때문에 늦었어요.</strong></p>",
        "choices": ["비가 → 비", "비가 → 비를", "때문에 → 기 때문에", "Xato yoʻq"],
        "correct": "비가 → 비",
        "explanation": "<p>때문에 oldidagi ot qoʻshimchasiz turadi: "
                       "<strong>비 때문에</strong>.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>바쁘 때문에 못 갔어요.</strong></p>",
        "choices": ["바쁘 → 바쁘기", "바쁘 → 바빠", "바쁘 → 바쁜", "Xato yoʻq"],
        "correct": "바쁘 → 바쁘기",
        "explanation": "<p>Feʼl yoki sifat boʻlsa, oʻrtaga <strong>기</strong> "
                       "kerak: 바쁘기 때문에.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Imtihon tufayli shu kunlarda bandman” — qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["시험 때문에 요즘 바빠요", "시험이기 때문에 요즘 바빠요",
                    "시험기 때문에 요즘 바빠요", "시험이 때문에 요즘 바빠요"],
        "correct": "시험 때문에 요즘 바빠요",
        "explanation": "<p>시험 — ot, qoʻshimchasiz turadi.</p>",
    },
    {
        "text": "<p>“Koreys tili qiyin boʻlgani uchun har kuni oʻqiyman” — "
                "qaysi biri toʻgʻri?</p>",
        "choices": ["한국어가 어려우기 때문에 매일 공부해요",
                    "한국어가 어렵기 때문에 매일 공부해요",
                    "한국어가 어려운 때문에 매일 공부해요",
                    "한국어가 어려워 때문에 매일 공부해요"],
        "correct": "한국어가 어렵기 때문에 매일 공부해요",
        "explanation": "<p>기 undosh → 어렵 oʻzgarmaydi. (아/어요 shakli "
                       "boʻlsa 어려워요 boʻlardi.)</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-47 Mashq: Notoʻgʻri feʼllar 2 — 르, ㅅ, ㅎ",
        "description": "20 savol — 르 guruhida ㄹ ikkilanishi, ㅅ ning soxta "
                       "aʼzolari, ㅎ ranglari va 좋다 istisnosi.",
        "tutorial":    "PK-47:",
        "level":       "medium",
        "questions":   Q_PK47,
    },
    {
        "title":       "PK-48 Mashq: (으)니까 — sabab va kashfiyot",
        "description": "20 savol — buyruq qoidasi, zamon, kashfiyot maʼnosi "
                       "va 아/어서 bilan farqi.",
        "tutorial":    "PK-48:",
        "level":       "medium",
        "questions":   Q_PK48,
    },
    {
        "title":       "PK-49 Mashq: 기 때문에 / 명사 + 때문에",
        "description": "20 savol — ot va feʼl bilan yasalishi, 이기 때문에, "
                       "buyruq taqiqi va uchta sabab qolipining farqi.",
        "tutorial":    "PK-49:",
        "level":       "medium",
        "questions":   Q_PK49,
    },
]
