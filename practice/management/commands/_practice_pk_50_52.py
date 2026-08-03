# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-50 … PK-52.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_50_52.py --master=prime \\
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
# PK-50 — 아/어야 하다 / 되다
# =====================================================================

Q_PK50 = [
    # 1–5 tanish
    {
        "text": "<p><strong>아/어야 하다</strong> nima maʼnoni beradi?</p>",
        "choices": ["…ishi kerak", "…sa ham boʻladi", "…ga oʻxshaydi",
                    "…sa boʻlmaydi"],
        "correct": "…ishi kerak",
        "explanation": "<p>가야 해요 — “borishim kerak”. Majburiyat va zaruratni "
                       "bildiradi.</p>",
    },
    {
        "text": "<p><strong>먹다</strong> ning 아/어야 하다 shakli qaysi?</p>",
        "choices": ["먹야 해요", "먹어야 해요", "먹으야 해요", "먹고야 해요"],
        "correct": "먹어야 해요",
        "explanation": "<p>아/어요 shaklini oling (먹어요), 요 oʻrniga 야 하다 "
                       "qoʻying: <strong>먹어야 해요</strong>.</p>",
    },
    {
        "text": "<p><strong>하다</strong> ning 아/어야 하다 shakli qaysi?</p>",
        "choices": ["하야 해요", "해야 해요", "하어야 해요", "했야 해요"],
        "correct": "해야 해요",
        "explanation": "<p>하다 → 해요 → <strong>해야 해요</strong>. "
                       "<s>하야</s> degan shakl yoʻq.</p>",
    },
    {
        "text": "<p>“…ishim kerak edi” qanday aytiladi?</p>",
        "choices": ["갔어야 해요", "가야 했어요", "가야 해었요", "갔야 했어요"],
        "correct": "가야 했어요",
        "explanation": "<p>Zamon oxirdagi <strong>하다</strong> ga qoʻyiladi: "
                       "가야 <strong>했어요</strong>.</p>",
    },
    {
        "text": "<p><strong>하다</strong> va <strong>되다</strong> orasida qanday "
                "farq bor?</p>",
        "choices": ["하다 rasmiyroq, 되다 ogʻzakiroq — ikkalasi ham toʻgʻri",
                    "되다 notoʻgʻri shakl",
                    "하다 faqat oʻtgan zamonda",
                    "되다 faqat sifatlar bilan"],
        "correct": "하다 rasmiyroq, 되다 ogʻzakiroq — ikkalasi ham toʻgʻri",
        "explanation": "<p>가야 해요 = 가야 돼요. Boshlangʻich darajada bu farqni "
                       "oʻylab oʻtirmang.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 내일 일찍 <strong>______</strong> (일어나다) 해요.</p>",
        "choices": ["일어나야", "일어나서", "일어나면", "일어나고"],
        "correct": "일어나야",
        "explanation": "<p>일어나요 → 요 oʻrniga 야: <strong>일어나야 "
                       "해요</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 이 노래를 <strong>______</strong> (듣다) 해요.</p>",
        "choices": ["듣어야", "들어야", "듣야", "들으야"],
        "correct": "들어야",
        "explanation": "<p>듣다 → 들어요 → <strong>들어야 해요</strong>. "
                       "아/어 unli bilan boshlanadi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 친구를 <strong>______</strong> (돕다) 해요.</p>",
        "choices": ["돕어야", "도와야", "도우야", "돕야"],
        "correct": "도와야",
        "explanation": "<p>돕다 — ㅂ notoʻgʻri feʼli: 도와요 → "
                       "<strong>도와야 해요</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 방이 <strong>______</strong> (깨끗하다) 해요.</p>",
        "choices": ["깨끗하야", "깨끗해야", "깨끗한야", "깨끗하여야"],
        "correct": "깨끗해야",
        "explanation": "<p>깨끗하다 → 깨끗해요 → <strong>깨끗해야 해요</strong>. "
                       "Sifat bilan ham ishlaydi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 어제 병원에 <strong>______</strong>. "
                "(“borishim kerak edi”)</p>",
        "choices": ["가야 해요", "갔어야 해요", "가야 했어요", "갔야 했어요"],
        "correct": "가야 했어요",
        "explanation": "<p>Zamon 하다 ga qoʻyiladi, 야 ga emas.</p>",
    },
    {
        "text": "<p>Toʻldiring: 그 사람은 <strong>______</strong> 해요. "
                "(“talaba boʻlishi kerak”)</p>",
        "choices": ["학생이어야", "학생여야", "학생야", "학생이야"],
        "correct": "학생이어야",
        "explanation": "<p>학생 da 받침 bor → <strong>이어야</strong>. "
                       "받침 yoʻq boʻlsa 여야: 친구여야 해요.</p>",
    },
    {
        "text": "<p>Toʻldiring: 노래를 <strong>______</strong> (부르다) 해요.</p>",
        "choices": ["부르야", "불러야", "불라야", "부러야"],
        "correct": "불러야",
        "explanation": "<p>부르다 — 르 notoʻgʻri feʼli: 불러요 → "
                       "<strong>불러야 해요</strong>.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p><strong>가야 해요</strong> dagi <strong>야</strong> nima "
                "degani?</p>",
        "choices": ["“faqat, aynan”", "“ham”", "“lekin”", "“yoki”"],
        "correct": "“faqat, aynan”",
        "explanation": "<p>가야 해요 soʻzma-soʻz “faqat borsam — boʻladi”. "
                       "Boshqa yoʻl yoʻqligidan majburiyat kelib chiqadi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["학교에 가야 있어요", "학교에 가야 해요",
                    "학교에 가야 없어요", "학교에 가야 이에요"],
        "correct": "학교에 가야 해요",
        "explanation": "<p>야 dan keyin <strong>하다</strong> yoki "
                       "<strong>되다</strong> keladi — 있다 emas.</p>",
    },
    {
        "text": "<p>Nega 듣다 bu qolipda 들어야 boʻladi?</p>",
        "choices": ["아/어 unli bilan boshlanadi",
                    "야 unli bilan boshlanadi",
                    "하다 notoʻgʻri feʼl",
                    "Bu istisno"],
        "correct": "아/어 unli bilan boshlanadi",
        "explanation": "<p>PK-32 ning qoidasi: notoʻgʻri tuslanish faqat unli "
                       "qoʻshimcha oldida ishlaydi. Qolip 아/어요 shaklidan "
                       "yasalgani uchun oʻzgarish sodir boʻladi.</p>",
    },
    {
        "text": "<p>Qaysi gap notoʻgʻri?</p>",
        "choices": ["매일 공부해야 합니다", "지금 가야 돼요",
                    "어제 갔어야 해요", "약을 먹어야 해요"],
        "correct": "어제 갔어야 해요",
        "explanation": "<p>Zamon ikki marta qoʻyilgan. Toʻgʻrisi — "
                       "<strong>어제 가야 했어요</strong>.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>방이 깨끗하야 해요.</strong></p>",
        "choices": ["깨끗하야 → 깨끗해야", "깨끗하야 → 깨끗한야",
                    "해요 → 있어요", "Xato yoʻq"],
        "correct": "깨끗하야 → 깨끗해야",
        "explanation": "<p>하다 → 해요 → 해야. <s>하야</s> degan shakl yoʻq.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>음악을 듣어야 해요.</strong></p>",
        "choices": ["듣어야 → 들어야", "듣어야 → 듣야", "해요 → 돼요", "Xato yoʻq"],
        "correct": "듣어야 → 들어야",
        "explanation": "<p>듣다 — ㄷ notoʻgʻri feʼli: 들어요 → 들어야.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Ertaga erta turishim kerak” — qaysi biri toʻgʻri?</p>",
        "choices": ["내일 일찍 일어나야 해요", "내일 일찍 일어나면 해요",
                    "내일 일찍 일어나서 해요", "내일 일찍 일어나도 해요"],
        "correct": "내일 일찍 일어나야 해요",
        "explanation": "<p>Majburiyat → <strong>아/어야 하다</strong>.</p>",
    },
    {
        "text": "<p>“Imtihon savollari oson boʻlishi kerak” — qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["시험 문제가 쉽어야 해요", "시험 문제가 쉬워야 해요",
                    "시험 문제가 쉬운야 해요", "시험 문제가 쉽야 해요"],
        "correct": "시험 문제가 쉬워야 해요",
        "explanation": "<p>쉽다 — ㅂ notoʻgʻri sifati: 쉬워요 → "
                       "<strong>쉬워야 해요</strong>.</p>",
    },
]


# =====================================================================
# PK-51 — 아/어도 되다 va (으)면 안 되다
# =====================================================================

Q_PK51 = [
    # 1–5 tanish
    {
        "text": "<p><strong>아/어도</strong> nima maʼnoni beradi?</p>",
        "choices": ["…sa ham", "…gani uchun", "…dan keyin", "…moqchiman"],
        "correct": "…sa ham",
        "explanation": "<p>비가 와도 = “yomgʻir yogʻsa ham”. Bu — bugungi "
                       "ikkala qolipning asosi.</p>",
    },
    {
        "text": "<p><strong>아/어도 되다</strong> nima maʼnoni beradi?</p>",
        "choices": ["…sa boʻlmaydi", "…sa ham boʻladi (ruxsat)",
                    "…ishi kerak", "…ga oʻxshaydi"],
        "correct": "…sa ham boʻladi (ruxsat)",
        "explanation": "<p>가도 돼요 — “borsangiz boʻladi”. Oʻzbekcha bilan "
                       "soʻzma-soʻz bir xil ibora.</p>",
    },
    {
        "text": "<p><strong>먹다</strong> ning taqiq shakli qaysi?</p>",
        "choices": ["먹면 안 돼요", "먹으면 안 돼요", "먹어도 안 돼요",
                    "먹어야 안 돼요"],
        "correct": "먹으면 안 돼요",
        "explanation": "<p>먹 da 받침 bor → <strong>먹으면 안 돼요</strong>.</p>",
    },
    {
        "text": "<p><strong>안 가도 돼요</strong> nima degani?</p>",
        "choices": ["Borsangiz boʻlmaydi", "Borishingiz kerak",
                    "Bormasangiz ham boʻladi", "Borasiz shekilli"],
        "correct": "Bormasangiz ham boʻladi",
        "explanation": "<p>Bu — <strong>shart emas</strong>. Taqiq esa "
                       "가면 안 돼요 (“borsangiz boʻlmaydi”).</p>",
    },
    {
        "text": "<p>“들어가도 돼요?” savoliga <em>rad</em> javobi qanday?</p>",
        "choices": ["아니요, 안 들어가도 돼요", "아니요, 들어가면 안 돼요",
                    "아니요, 들어가야 해요", "아니요, 들어가는 것 같아요"],
        "correct": "아니요, 들어가면 안 돼요",
        "explanation": "<p>Rad javobida qolip <strong>almashadi</strong>: "
                       "아/어도 → (으)면 안 되다.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 여기에 <strong>______</strong> (앉다) 돼요?</p>",
        "choices": ["앉으도", "앉아도", "앉면", "앉어도"],
        "correct": "앉아도",
        "explanation": "<p>앉다 → 앉아요 → <strong>앉아도 돼요?</strong></p>",
    },
    {
        "text": "<p>Toʻldiring: 도서관에서 <strong>______</strong> (먹다) 안 "
                "돼요.</p>",
        "choices": ["먹면", "먹어도", "먹으면", "먹어야"],
        "correct": "먹으면",
        "explanation": "<p>Taqiq → (으)면 안 되다. 먹 da 받침 bor → "
                       "<strong>먹으면</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 음악을 <strong>______</strong> (듣다) 돼요?</p>",
        "choices": ["듣어도", "들어도", "듣도", "들으도"],
        "correct": "들어도",
        "explanation": "<p>듣다 → 들어요 → <strong>들어도 돼요?</strong></p>",
    },
    {
        "text": "<p>Toʻldiring: 여기에서 담배를 <strong>______</strong> "
                "(피우다) 돼요?</p>",
        "choices": ["피우도", "피워도", "피우어도", "피워야"],
        "correct": "피워도",
        "explanation": "<p>피우다 → 피워요 → <strong>피워도 돼요?</strong></p>",
    },
    {
        "text": "<p>Toʻldiring: 비가 <strong>______</strong> 학교에 가요. "
                "(“yogʻsa ham”)</p>",
        "choices": ["와도", "와서", "오면", "오니까"],
        "correct": "와도",
        "explanation": "<p>아/어도 = “…sa ham”: <strong>비가 와도</strong> "
                       "학교에 가요.</p>",
    },
    {
        "text": "<p>Toʻldiring: 수업 시간에 <strong>______</strong> (전화하다) "
                "안 돼요.</p>",
        "choices": ["전화하면", "전화해도", "전화하어도", "전화해야"],
        "correct": "전화하면",
        "explanation": "<p>Taqiq → (으)면 안 되다. 하 da 받침 yoʻq → "
                       "<strong>전화하면</strong>.</p>",
    },
    {
        "text": "<p><strong>되다</strong> oʻrniga yana qaysi soʻz ishlatiladi?</p>",
        "choices": ["괜찮다", "모르다", "같다", "다르다"],
        "correct": "괜찮다",
        "explanation": "<p>먹어도 <strong>괜찮아요</strong> = 먹어도 돼요 = "
                       "먹어도 좋아요 — uchalasi bir xil maʼno.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p><strong>안 와도 돼요</strong> va <strong>오면 안 돼요</strong> — "
                "farqi nima?</p>",
        "choices": ["Birinchisi “kelmasangiz ham boʻladi”, ikkinchisi "
                    "“kelsangiz boʻlmaydi”",
                    "Birinchisi “kelsangiz boʻlmaydi”, ikkinchisi "
                    "“kelmasangiz ham boʻladi”",
                    "Ikkalasi bir xil",
                    "Birinchisi notoʻgʻri"],
        "correct": "Birinchisi “kelmasangiz ham boʻladi”, ikkinchisi "
                   "“kelsangiz boʻlmaydi”",
        "explanation": "<p>Inkorning <strong>oʻrniga</strong> qarang: "
                       "<b>안</b> 와도 돼요 da inkor birinchi feʼlda, "
                       "오면 <b>안</b> 돼요 da esa oxirida.</p>",
    },
    {
        "text": "<p>“Borish majburiy emas” — qaysi biri?</p>",
        "choices": ["가야 해요", "가도 돼요", "가면 안 돼요", "안 가도 돼요"],
        "correct": "안 가도 돼요",
        "explanation": "<p>“Bormasangiz ham boʻladi” — majburiyat yoʻq. "
                       "가도 돼요 esa “borsangiz boʻladi” (ruxsat).</p>",
    },
    {
        "text": "<p>Toʻrtta qolipdan qaysi biri <em>taqiq</em>ni bildiradi?</p>",
        "choices": ["아/어야 하다", "아/어도 되다", "(으)면 안 되다",
                    "안 …아/어도 되다"],
        "correct": "(으)면 안 되다",
        "explanation": "<p>가면 안 돼요 — “borsangiz boʻlmaydi”. Qolganlari: "
                       "kerak · mumkin · shart emas.</p>",
    },
    {
        "text": "<p>Nega 아/어도 되다 oʻzbek oʻquvchiga oson?</p>",
        "choices": ["Chunki oʻzbekchada ham “…sa ham boʻladi” deyiladi",
                    "Chunki u qisqa qolip",
                    "Chunki 받침 ayrisi yoʻq",
                    "Chunki u faqat savollarda ishlatiladi"],
        "correct": "Chunki oʻzbekchada ham “…sa ham boʻladi” deyiladi",
        "explanation": "<p>가도 돼요 soʻzma-soʻz “borsa ham boʻladi” — "
                       "oʻzbekchada aynan shunday aytiladi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>여기에서 먹면 안 돼요.</strong></p>",
        "choices": ["먹면 → 먹으면", "먹면 → 먹어도", "안 돼요 → 안 해요",
                    "Xato yoʻq"],
        "correct": "먹면 → 먹으면",
        "explanation": "<p>먹 da 받침 bor → <strong>먹으면</strong>.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>여기에서 사진을 찍도 돼요?</strong></p>",
        "choices": ["찍도 → 찍어도", "찍도 → 찍으면", "찍도 → 찍어야",
                    "Xato yoʻq"],
        "correct": "찍도 → 찍어도",
        "explanation": "<p>아/어요 shaklidan yasaladi: 찍어요 → "
                       "<strong>찍어도 돼요?</strong></p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Bu yerda surat olsam boʻladimi?” — qaysi biri toʻgʻri?</p>",
        "choices": ["여기에서 사진을 찍어도 돼요?", "여기에서 사진을 찍으면 안 돼요?",
                    "여기에서 사진을 찍어야 돼요?", "여기에서 사진을 찍는 것 같아요?"],
        "correct": "여기에서 사진을 찍어도 돼요?",
        "explanation": "<p>Ruxsat soʻrash → <strong>아/어도 돼요?</strong></p>",
    },
    {
        "text": "<p>가다 bilan toʻrtta qolipni toʻgʻri tartibda qaysi qator "
                "beradi? (kerak · mumkin · mumkin emas · shart emas)</p>",
        "choices": ["가야 해요 · 가도 돼요 · 가면 안 돼요 · 안 가도 돼요",
                    "가도 돼요 · 가야 해요 · 안 가도 돼요 · 가면 안 돼요",
                    "가면 안 돼요 · 안 가도 돼요 · 가야 해요 · 가도 돼요",
                    "가야 돼요 · 가면 돼요 · 가도 안 돼요 · 안 가야 돼요"],
        "correct": "가야 해요 · 가도 돼요 · 가면 안 돼요 · 안 가도 돼요",
        "explanation": "<p>Bu toʻrtlik PK-50 va PK-51 ning birgalikdagi "
                       "xulosasi — uni yod olsangiz, tizim yopiladi.</p>",
    },
]


# =====================================================================
# PK-52 — (으)ㄴ/는/(으)ㄹ 것 같다
# =====================================================================

Q_PK52 = [
    # 1–5 tanish
    {
        "text": "<p><strong>것 같다</strong> nima maʼnoni beradi?</p>",
        "choices": ["…ga oʻxshaydi, shekilli", "…ishi kerak", "…sa ham boʻladi",
                    "…dan keyin"],
        "correct": "…ga oʻxshaydi, shekilli",
        "explanation": "<p>Taxmin bildiradi: 비가 올 것 같아요 — “yomgʻir "
                       "yogʻadiganga oʻxshaydi”.</p>",
    },
    {
        "text": "<p>Qolip qanday qismlardan yigʻilgan?</p>",
        "choices": ["Aniqlovchi + 것 + 같다", "기 + 것 + 같다",
                    "아/어 + 것 + 같다", "(으)면 + 같다"],
        "correct": "Aniqlovchi + 것 + 같다",
        "explanation": "<p>Hammasi tanish: aniqlovchi (PK-43, 44, 45) va "
                       "것 (PK-46).</p>",
    },
    {
        "text": "<p>“Yomgʻir yogʻ<em>ayotgan</em>ga oʻxshaydi” — qaysi biri?</p>",
        "choices": ["비가 온 것 같아요", "비가 오는 것 같아요", "비가 올 것 같아요",
                    "비가 오기 것 같아요"],
        "correct": "비가 오는 것 같아요",
        "explanation": "<p>Hozirgi zamon → <strong>는</strong>. 온 것 = "
                       "yoqqan, 올 것 = yogʻadigan.</p>",
    },
    {
        "text": "<p>Ot bilan qanday boʻladi?</p>",
        "choices": ["선생님 것 같아요", "선생님인 것 같아요", "선생님는 것 같아요",
                    "선생님이기 것 같아요"],
        "correct": "선생님인 것 같아요",
        "explanation": "<p>이다 + (으)ㄴ → <strong>인</strong>: 선생님인 것 "
                       "같아요.</p>",
    },
    {
        "text": "<p>Ogʻzaki nutqda <strong>것 같아요</strong> qanday "
                "eshitiladi?</p>",
        "choices": ["거 같아요", "게 같아요", "걸 같아요", "곳 같아요"],
        "correct": "거 같아요",
        "explanation": "<p>것 → <strong>거</strong>. Yozma matnda esa 것 "
                       "yoziladi — TOPIK da ham shunday.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 밖에 비가 <strong>______</strong> (오다) 것 "
                "같아요. (“yogʻadiganga oʻxshaydi”)</p>",
        "choices": ["온", "오는", "올", "오기"],
        "correct": "올",
        "explanation": "<p>Hali boʻlmagan ish → <strong>(으)ㄹ</strong>: "
                       "올 것 같아요.</p>",
    },
    {
        "text": "<p>Toʻldiring: 이 문제가 <strong>______</strong> (어렵다) 것 "
                "같아요.</p>",
        "choices": ["어렵은", "어려운", "어렵는", "어려울"],
        "correct": "어려운",
        "explanation": "<p>어렵다 — sifat, ㅂ → 우: <strong>어려운 것 "
                       "같아요</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 지영 씨가 지금 <strong>______</strong> "
                "(공부하다) 것 같아요.</p>",
        "choices": ["공부한", "공부하는", "공부할", "공부하기"],
        "correct": "공부하는",
        "explanation": "<p>Hozirgi zamon → <strong>는</strong>. 공부한 것 "
                       "같아요 “oʻqiganga oʻxshaydi” degani.</p>",
    },
    {
        "text": "<p>Toʻldiring: 아프소나 씨가 벌써 <strong>______</strong> "
                "(가다) 것 같아요. (“ketganga oʻxshaydi”)</p>",
        "choices": ["간", "가는", "갈", "가기"],
        "correct": "간",
        "explanation": "<p>Ish tugagan → <strong>(으)ㄴ</strong>: "
                       "간 것 같아요.</p>",
    },
    {
        "text": "<p>Toʻldiring: 이 음식이 <strong>______</strong> (맵다) 것 "
                "같아요.</p>",
        "choices": ["맵은", "매운", "맵는", "매울"],
        "correct": "매운",
        "explanation": "<p>맵다 — sifat, ㅂ → 우: <strong>매운 것 같아요</strong> "
                       "(“achchiqqa oʻxshaydi”, hozirgi zamon).</p>",
    },
    {
        "text": "<p>Toʻldiring: 저분은 <strong>______</strong> 것 같아요. "
                "(“shifokor boʻlsa kerak”)</p>",
        "choices": ["의사", "의사인", "의사는", "의사기"],
        "correct": "의사인",
        "explanation": "<p>Ot bilan 이다 tuslanadi: 의사 + "
                       "<strong>인</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 그 영화가 <strong>______</strong> (재미있다) 것 "
                "같아요.</p>",
        "choices": ["재미있은", "재미있는", "재미있을", "재미있어"],
        "correct": "재미있는",
        "explanation": "<p>재미있다 ichida 있다 (feʼl) bor → "
                       "<strong>는</strong> oladi (PK-43).</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p><strong>먹은 것 같아요</strong> va <strong>매운 것 "
                "같아요</strong> — ikkalasi ham (으)ㄴ. Farqi nima?</p>",
        "choices": ["먹다 feʼl → oʻtgan zamon; 맵다 sifat → hozirgi zamon",
                    "먹다 sifat; 맵다 feʼl",
                    "Birinchisi rasmiy, ikkinchisi norasmiy",
                    "Farqi yoʻq"],
        "correct": "먹다 feʼl → oʻtgan zamon; 맵다 sifat → hozirgi zamon",
        "explanation": "<p>PK-45 dagi tuzoqning oʻzi: shakl bir xil, maʼnoni "
                       "soʻzning turi hal qiladi.</p>",
    },
    {
        "text": "<p>Zamon qayerda koʻrsatiladi?</p>",
        "choices": ["Aniqlovchida", "같다 da", "것 da", "Gap boshida"],
        "correct": "Aniqlovchida",
        "explanation": "<p>온/오는/올 것 같아요 — zamonni <strong>aniqlovchi</strong> "
                       "bildiradi. 같다 tuslanmaydi.</p>",
    },
    {
        "text": "<p>Nega koreys odam taomni yeb turib “맛있는 것 같아요” "
                "deydi?</p>",
        "choices": ["Fikrini yumshatish uchun", "Chunki mazasini bilmaydi",
                    "Chunki bu rasmiy shakl", "Chunki 맛있어요 notoʻgʻri"],
        "correct": "Fikrini yumshatish uchun",
        "explanation": "<p>Koreys madaniyatida oʻz fikrini qatʼiy aytish biroz "
                       "keskin eshitiladi. Shuning uchun bilgan narsani ham "
                       "것 같아요 bilan aytish odat.</p>",
    },
    {
        "text": "<p>Qaysi gap notoʻgʻri?</p>",
        "choices": ["비가 올 것 같아요", "매운 것 같아요", "매웠는 것 같아요",
                    "선생님인 것 같아요"],
        "correct": "매웠는 것 같아요",
        "explanation": "<p>맵다 — sifat, (으)ㄴ oladi va aniqlovchi ichiga zamon "
                       "qoʻyilmaydi. Toʻgʻrisi — <strong>매운 것 같아요</strong>.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>저분은 의사 것 같아요.</strong></p>",
        "choices": ["의사 → 의사인", "의사 → 의사는", "같아요 → 같은", "Xato yoʻq"],
        "correct": "의사 → 의사인",
        "explanation": "<p>Ot bilan 이다 tuslanadi: 의사<strong>인</strong> 것 "
                       "같아요.</p>",
    },
    {
        "text": "<p>Xatoni toping (“hozir oʻqiyaptiga oʻxshaydi” maʼnosida): "
                "<strong>지금 공부한 것 같아요.</strong></p>",
        "choices": ["공부한 → 공부하는", "공부한 → 공부할", "공부한 → 공부하기",
                    "Xato yoʻq"],
        "correct": "공부한 → 공부하는",
        "explanation": "<p>Hozirgi zamon → <strong>는</strong>. 공부한 것 "
                       "같아요 “oʻqiganga oʻxshaydi” degani.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Bu taom achchiqqa oʻxshaydi” — qaysi biri toʻgʻri?</p>",
        "choices": ["이 음식이 매운 것 같아요", "이 음식이 맵는 것 같아요",
                    "이 음식이 매울 것 같아요", "이 음식이 매웠는 것 같아요"],
        "correct": "이 음식이 매운 것 같아요",
        "explanation": "<p>맵다 sifat → (으)ㄴ, va ㅂ → 우: 매운.</p>",
    },
    {
        "text": "<p>“Afsona allaqachon ketganga oʻxshaydi” — qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["아프소나 씨가 벌써 가는 것 같아요",
                    "아프소나 씨가 벌써 갈 것 같아요",
                    "아프소나 씨가 벌써 간 것 같아요",
                    "아프소나 씨가 벌써 갔는 것 같아요"],
        "correct": "아프소나 씨가 벌써 간 것 같아요",
        "explanation": "<p>Ish tugagan → <strong>(으)ㄴ</strong>. Aniqlovchi "
                       "ichiga 았/었 qoʻyilmaydi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-50 Mashq: 아/어야 하다 / 되다 — majburiyat",
        "description": "20 savol — yasalishi, 하다/되다 farqi, zamonning oʻrni "
                       "va sifat/ot bilan ishlatilishi.",
        "tutorial":    "PK-50:",
        "level":       "medium",
        "questions":   Q_PK50,
    },
    {
        "title":       "PK-51 Mashq: 아/어도 되다 va (으)면 안 되다",
        "description": "20 savol — ruxsat, taqiq, rad javobi va “shart emas” "
                       "bilan “mumkin emas” farqi.",
        "tutorial":    "PK-51:",
        "level":       "medium",
        "questions":   Q_PK51,
    },
    {
        "title":       "PK-52 Mashq: (으)ㄴ/는/(으)ㄹ 것 같다 — taxmin",
        "description": "20 savol — uch zamon, feʼl/sifat tuzogʻi, 인 것 같다 "
                       "va 거 같아요 qisqarishi.",
        "tutorial":    "PK-52:",
        "level":       "medium",
        "questions":   Q_PK52,
    },
]
