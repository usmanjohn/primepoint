# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-65 … PK-67.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_65_67.py --master=prime \\
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
# PK-65 — (으)ㄹ수록
# =====================================================================

Q_PK65 = [
    # 1–5 tanish
    {
        "text": "<p><strong>(으)ㄹ수록</strong> nimani bildiradi?</p>",
        "choices": ["Bir narsa ortgan sari ikkinchisi ham oʻzgaradi",
                    "Ish sal boʻlmasa sodir boʻlardi",
                    "Ikki narsani qiyoslash",
                    "Faqat bir marta boʻlgan hodisa"],
        "correct": "Bir narsa ortgan sari ikkinchisi ham oʻzgaradi",
        "explanation": "<p>배울수록 재미있어요 = “oʻrgangan <strong>sari</strong> "
                       "qiziq boʻladi”. Oʻzbekchada tayyor qurilma bor.</p>",
    },
    {
        "text": "<p><strong>배우다</strong> bu qolipda qanday shaklga "
                "kiradi?</p>",
        "choices": ["배우을수록", "배울수록", "배우는수록", "배운수록"],
        "correct": "배울수록",
        "explanation": "<p>배우 da 받침 yoʻq → <strong>ㄹ수록</strong>.</p>",
    },
    {
        "text": "<p><strong>많다</strong> bu qolipda qanday shaklga "
                "kiradi?</p>",
        "choices": ["많를수록", "많은수록", "많을수록", "많는수록"],
        "correct": "많을수록",
        "explanation": "<p>많 da 받침 bor → <strong>을수록</strong>. Bu "
                       "qolip sifat bilan ham ishlaydi.</p>",
    },
    {
        "text": "<p>Kuchaytirilgan shakli qanday yasaladi?</p>",
        "choices": ["(으)면 + (으)ㄹ수록", "(으)니까 + (으)ㄹ수록",
                    "고 + (으)ㄹ수록", "지만 + (으)ㄹ수록"],
        "correct": "(으)면 + (으)ㄹ수록",
        "explanation": "<p>하<strong>면</strong> 할<strong>수록</strong> — "
                       "feʼl ikki marta aytiladi va maʼno kuchayadi.</p>",
    },
    {
        "text": "<p><strong>갈수록</strong> alohida soʻz sifatida nima "
                "degani?</p>",
        "choices": ["Borgandan keyin", "Tobora, kundan-kunga",
                    "Borish kerak", "Bora olaman"],
        "correct": "Tobora, kundan-kunga",
        "explanation": "<p>갈수록 날씨가 추워져요 — “kundan-kunga havo sovib "
                       "boryapti”. Feʼlsiz ham ishlatiladi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 한국어는 <strong>______</strong> "
                "재미있어요. (배우다)</p>",
        "choices": ["배울수록", "배우을수록", "배운수록", "배웠을수록"],
        "correct": "배울수록",
        "explanation": "<p>받침 yoʻq → ㄹ수록. Zamon qoʻshimchasi "
                       "qoʻyilmaydi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 시간이 <strong>______</strong> 실력이 "
                "좋아져요. (지나다)</p>",
        "choices": ["지날수록", "지나을수록", "지났을수록", "지나는수록"],
        "correct": "지날수록",
        "explanation": "<p>지나 da 받침 yoʻq → <strong>지날수록</strong>. "
                       "Keyingi gapda 아/어지다 turgani ham tipik.</p>",
    },
    {
        "text": "<p>Toʻldiring: 이 노래는 <strong>______</strong> "
                "들을수록 좋아요. (듣다)</p>",
        "choices": ["듣면", "들으면", "듣으면", "들면"],
        "correct": "들으면",
        "explanation": "<p>듣다 — ㄷ notoʻgʻri feʼli (PK-32): oʻzak "
                       "<strong>들</strong> boʻladi → 들으면 "
                       "들을수록.</p>",
    },
    {
        "text": "<p>Toʻldiring: 사람이 <strong>______</strong> 좋아요. "
                "(많다)</p>",
        "choices": ["많은수록", "많을수록", "많는수록", "많았을수록"],
        "correct": "많을수록",
        "explanation": "<p>받침 bor → <strong>을수록</strong>: “odam koʻp "
                       "boʻlgan sari yaxshi”.</p>",
    },
    {
        "text": "<p><strong>만들다</strong> bu qolipda qanday boʻladi?</p>",
        "choices": ["만들을수록", "만들수록", "만드는수록", "만든수록"],
        "correct": "만들수록",
        "explanation": "<p>ㄹ oʻzak bitta ㄹ boʻlib qoladi: 만들 + ㄹ수록 → "
                       "<strong>만들수록</strong>.</p>",
    },
    {
        "text": "<p>“Koreys tili oʻqigan sari osonlashib boradi” — qaysi "
                "biri toʻgʻri?</p>",
        "choices": ["한국어는 공부할수록 쉬워져요",
                    "한국어는 공부했을수록 쉬워져요",
                    "한국어는 공부하는수록 쉬워져요",
                    "한국어는 공부하면 쉬워요"],
        "correct": "한국어는 공부할수록 쉬워져요",
        "explanation": "<p>공부할수록 + <strong>쉬워져요</strong> "
                       "(아/어지다) — bu ikkisi juftlik boʻlib "
                       "yuradi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 그 사람은 <strong>______</strong> 알수록 "
                "좋은 사람이에요. (알다)</p>",
        "choices": ["알면", "알으면", "안면", "아면"],
        "correct": "알면",
        "explanation": "<p>알다 — ㄹ oʻzak, 면 toʻgʻridan-toʻgʻri "
                       "qoʻshiladi: <strong>알면 알수록</strong>.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Nima uchun <strong>어제 학교에 갈수록 친구를 만났어요</strong> "
                "notoʻgʻri?</p>",
        "choices": ["받침 xato",
                    "Bu bir martalik hodisa — (으)ㄹ수록 asta-sekin "
                    "oʻzgarish uchun",
                    "Zamon xato",
                    "Ega yoʻq"],
        "correct": "Bu bir martalik hodisa — (으)ㄹ수록 asta-sekin "
                   "oʻzgarish uchun",
        "explanation": "<p>Toʻgʻrisi — 어제 학교에 <strong>가서</strong> "
                       "친구를 만났어요 (PK-35).</p>",
    },
    {
        "text": "<p>Zamon qoʻshimchasi qayerda boʻladi?</p>",
        "choices": ["수록 dan oldin", "Oxirgi feʼlda", "Ikkalasida",
                    "Hech qayerda"],
        "correct": "Oxirgi feʼlda",
        "explanation": "<p>배울수록 재미<strong>있었어요</strong> — "
                       "<s>배웠을수록</s> emas.</p>",
    },
    {
        "text": "<p>Bu qolip qaysi bilan eng koʻp juftlik boʻlib "
                "yuradi?</p>",
        "choices": ["아/어지다", "아/어 버리다", "(으)ㄹ 뻔하다", "기로 하다"],
        "correct": "아/어지다",
        "explanation": "<p>Ikkalasi ham <strong>oʻzgarish</strong> haqida: "
                       "배울수록 쉬워져요, 지날수록 좋아져요.</p>",
    },
    {
        "text": "<p><strong>배울수록</strong> va <strong>배우면 "
                "배울수록</strong> farqi nimada?</p>",
        "choices": ["Ikkinchisi notoʻgʻri",
                    "Maʼnosi bir xil, ikkinchisi kuchliroq va ogʻzaki "
                    "nutqda koʻproq",
                    "Birinchisi oʻtgan zamon",
                    "Ikkinchisi faqat sifat bilan"],
        "correct": "Maʼnosi bir xil, ikkinchisi kuchliroq va ogʻzaki "
                   "nutqda koʻproq",
        "explanation": "<p>Ikkilangan shakl majburiy emas — u faqat "
                       "maʼnoni kuchaytiradi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>사람이 많를수록 좋아요.</strong></p>",
        "choices": ["많를수록 → 많을수록", "많를수록 → 많은수록",
                    "사람이 → 사람은", "Xato yoʻq"],
        "correct": "많를수록 → 많을수록",
        "explanation": "<p>많 da 받침 bor → <strong>을수록</strong>. "
                       "를수록 degan shakl yoʻq.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>시간이 지났을수록 실력이 "
                "좋아졌어요.</strong></p>",
        "choices": ["지났을수록 → 지날수록", "지났을수록 → 지나는수록",
                    "좋아졌어요 → 좋았어요", "Xato yoʻq"],
        "correct": "지났을수록 → 지날수록",
        "explanation": "<p>수록 dan oldin zamon qoʻshimchasi qoʻyilmaydi — "
                       "zamon oxirgi feʼlda (좋아졌어요).</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Bu qoʻshiq eshitgan sari yoqadi” — qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["이 노래는 들으면 들을수록 좋아요",
                    "이 노래는 듣으면 듣을수록 좋아요",
                    "이 노래는 들었을수록 좋아요",
                    "이 노래는 듣는수록 좋아요"],
        "correct": "이 노래는 들으면 들을수록 좋아요",
        "explanation": "<p>듣다 → 들으면 들을수록 (ㄷ notoʻgʻri feʼli).</p>",
    },
    {
        "text": "<p><strong>가:</strong> 요즘 날씨가 어때요?</p>"
                "<p><strong>나:</strong> ___</p>",
        "choices": ["갈수록 추워져요", "갔을수록 추워져요",
                    "가는수록 추워져요", "갈수록 추웠어요"],
        "correct": "갈수록 추워져요",
        "explanation": "<p><strong>갈수록</strong> — “tobora, kundan-kunga”. "
                       "추워지다 (아/어지다) bilan tabiiy juftlik.</p>",
    },
]


# =====================================================================
# PK-66 — (으)ㄴ/는 반면에
# =====================================================================

Q_PK66 = [
    # 1–5 tanish
    {
        "text": "<p><strong>(으)ㄴ/는 반면에</strong> nimani bildiradi?</p>",
        "choices": ["Sababni", "Bitta mavzuning ikki tomonini",
                    "Ketma-ketlikni", "Shartni"],
        "correct": "Bitta mavzuning ikki tomonini",
        "explanation": "<p>Oʻzbekchadagi <strong>“esa”</strong>: “grammatikasi "
                       "oson, talaffuzi <strong>esa</strong> qiyin”.</p>",
    },
    {
        "text": "<p>Feʼl bu qolipda qanday shakl oladi?</p>",
        "choices": ["는 반면에", "(으)ㄴ 반면에", "(으)ㄹ 반면에", "인 반면에"],
        "correct": "는 반면에",
        "explanation": "<p>좋아하다 → 좋아하<strong>는</strong> 반면에. "
                       "Bu PK-43 dagi aniqlovchi qoidasi.</p>",
    },
    {
        "text": "<p>Sifat bu qolipda qanday shakl oladi?</p>",
        "choices": ["는 반면에", "(으)ㄴ 반면에", "(으)ㄹ 반면에", "게 반면에"],
        "correct": "(으)ㄴ 반면에",
        "explanation": "<p>좋다 → 좋<strong>은</strong> 반면에, 비싸다 → "
                       "비싼 반면에. Bu PK-45 dagi qoida.</p>",
    },
    {
        "text": "<p>Ot (이다) bu qolipda qanday shakl oladi?</p>",
        "choices": ["이는 반면에", "인 반면에", "이라 반면에", "일 반면에"],
        "correct": "인 반면에",
        "explanation": "<p>학생이다 → <strong>학생인 반면에</strong>.</p>",
    },
    {
        "text": "<p>Yozma matnda bu qolip qanday qisqaradi?</p>",
        "choices": ["반면", "반대", "반만", "면에"],
        "correct": "반면",
        "explanation": "<p><strong>에</strong> tushadi: 편리한 <strong>반면"
                       "</strong> 공기가 나빠요. TOPIK 쓰기 uchun juda "
                       "foydali.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 서울은 <strong>______</strong> 반면에 "
                "집값이 비싸요. (편리하다)</p>",
        "choices": ["편리하는", "편리한", "편리할", "편리해서"],
        "correct": "편리한",
        "explanation": "<p>편리하다 — sifat, 받침 yoʻq → "
                       "<strong>ㄴ 반면에</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 저는 운동을 <strong>______</strong> 반면에 "
                "동생은 책을 좋아해요. (좋아하다)</p>",
        "choices": ["좋아한", "좋아할", "좋아하는", "좋아해서"],
        "correct": "좋아하는",
        "explanation": "<p>좋아하다 — <strong>feʼl</strong>, hozirgi "
                       "zamonda 는 oladi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 이 카페는 커피가 <strong>______</strong> "
                "반면에 자리가 좁아요. (좋다)</p>",
        "choices": ["좋는", "좋은", "좋을", "좋아하는"],
        "correct": "좋은",
        "explanation": "<p>좋다 — sifat, 받침 bor → "
                       "<strong>은 반면에</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 하나 씨는 <strong>______</strong> 반면에 "
                "언니는 가수예요. (학생이다)</p>",
        "choices": ["학생이는", "학생인", "학생일", "학생이라"],
        "correct": "학생인",
        "explanation": "<p>Ot + 이다 → <strong>인 반면에</strong>.</p>",
    },
    {
        "text": "<p>“Akam tinch, ukam esa shoʻx” — qaysi biri toʻgʻri?</p>",
        "choices": ["형은 조용하는 반면에 동생은 활발해요",
                    "형은 조용한 반면에 동생은 활발해요",
                    "형이 조용한 반면에 동생이 활발해요",
                    "형은 조용할 반면에 동생은 활발해요"],
        "correct": "형은 조용한 반면에 동생은 활발해요",
        "explanation": "<p>조용하다 sifat → 조용한. Ikkala egada ham "
                       "<strong>은</strong> — qiyoslash yuklamasi "
                       "(PK-12).</p>",
    },
    {
        "text": "<p>Bu qolipda egalar odatda qaysi qoʻshimchani oladi?</p>",
        "choices": ["이/가", "은/는", "을/를", "에게"],
        "correct": "은/는",
        "explanation": "<p>형<strong>은</strong> … 동생<strong>은</strong> — "
                       "은/는 aynan <strong>qiyoslash</strong> uchun "
                       "(PK-12), shuning uchun bu tasodif emas.</p>",
    },
    {
        "text": "<p>Toʻldiring: 도시는 <strong>______</strong> 반면 공기가 "
                "나빠요. (편리하다)</p>",
        "choices": ["편리한", "편리하는", "편리할", "편리했던"],
        "correct": "편리한",
        "explanation": "<p>반면 — 에 tushgan rasmiy shakl, lekin oldidagi "
                       "aniqlovchi oʻzgarmaydi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p><strong>지만</strong> va <strong>반면에</strong> farqi "
                "nimada?</p>",
        "choices": ["지만 — oddiy “lekin”; 반면에 — “esa”, ikki tomonni "
                    "qiyoslash",
                    "지만 — “esa”; 반면에 — “lekin”",
                    "Ikkalasi bir xil",
                    "지만 faqat sifat bilan keladi"],
        "correct": "지만 — oddiy “lekin”; 반면에 — “esa”, ikki tomonni "
                   "qiyoslash",
        "explanation": "<p>지만 bogʻliq boʻlmagan ikki gapni ham qoʻshadi. "
                       "반면에 esa <strong>bitta mavzuning</strong> ikki "
                       "tomoni uchun.</p>",
    },
    {
        "text": "<p>Qaysi gapda <strong>반면에</strong> ishlatib "
                "boʻlmaydi?</p>",
        "choices": ["Seul qulay, uy narxi esa qimmat",
                    "Yomgʻir yogʻyapti, lekin maktabga boraman",
                    "Akam tinch, ukam esa shoʻx",
                    "Kofesi mazali, joyi esa tor"],
        "correct": "Yomgʻir yogʻyapti, lekin maktabga boraman",
        "explanation": "<p>“Yomgʻir” va “maktabga borish” bitta narsaning "
                       "ikki tomoni emas — bu yerda <strong>지만</strong> "
                       "kerak.</p>",
    },
    {
        "text": "<p>Nima uchun <strong>좋는 반면에</strong> notoʻgʻri?</p>",
        "choices": ["Chunki 좋다 sifat — sifat (으)ㄴ oladi",
                    "Chunki 좋다 feʼl",
                    "Chunki 받침 yoʻq",
                    "Chunki zamon kerak"],
        "correct": "Chunki 좋다 sifat — sifat (으)ㄴ oladi",
        "explanation": "<p>Toʻgʻrisi — <strong>좋은 반면에</strong>. "
                       "는 faqat feʼlga.</p>",
    },
    {
        "text": "<p>Bu qolip TOPIK ning qaysi qismida ayniqsa "
                "foydali?</p>",
        "choices": ["듣기 (tinglash)", "쓰기 (yozish) — grafik tasvirlashda",
                    "Faqat ogʻzaki nutqda", "Hech qayerda"],
        "correct": "쓰기 (yozish) — grafik tasvirlashda",
        "explanation": "<p>Grafik yoki jadvalda ikki tomonni koʻrsatish "
                       "kerak: “남자는 … 반면에 여자는 …”. Bitta jumlada "
                       "butun taqqoslash.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>저는 운동을 좋아한 반면에 동생은 "
                "책을 좋아해요.</strong></p>",
        "choices": ["좋아한 → 좋아하는", "좋아한 → 좋아할",
                    "동생은 → 동생이", "Xato yoʻq"],
        "correct": "좋아한 → 좋아하는",
        "explanation": "<p>좋아하다 — feʼl, hozirgi zamonda "
                       "<strong>는</strong> oladi.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>하나 씨는 학생이는 반면에 언니는 "
                "가수예요.</strong></p>",
        "choices": ["학생이는 → 학생인", "학생이는 → 학생일",
                    "학생이는 → 학생이라", "Xato yoʻq"],
        "correct": "학생이는 → 학생인",
        "explanation": "<p>Ot + 이다 → <strong>인</strong>: 학생인 "
                       "반면에.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Koreys tilining grammatikasi oson, talaffuzi esa "
                "qiyin” — qaysi biri toʻgʻri?</p>",
        "choices": ["문법이 쉬는 반면에 발음이 어려워요",
                    "문법이 쉬운 반면에 발음이 어려워요",
                    "문법이 쉬울 반면에 발음이 어려워요",
                    "문법이 쉽은 반면에 발음이 어려워요"],
        "correct": "문법이 쉬운 반면에 발음이 어려워요",
        "explanation": "<p>쉽다 — ㅂ notoʻgʻri sifati (PK-32): 쉬우 + ㄴ → "
                       "<strong>쉬운</strong>.</p>",
    },
    {
        "text": "<p><strong>가:</strong> 그 카페 어때요?</p>"
                "<p><strong>나:</strong> ___</p>",
        "choices": ["커피가 맛있는 반면에 자리가 좁아요",
                    "커피가 맛있을 반면에 자리가 좁아요",
                    "커피가 맛있는 반면에 값도 싸요",
                    "커피가 맛있지만 자리가 좁는 반면에"],
        "correct": "커피가 맛있는 반면에 자리가 좁아요",
        "explanation": "<p>맛있다 — sifat boʻlsa ham 있다 bilan tugagani "
                       "uchun <strong>는</strong> oladi. Ikki tomon: "
                       "yaxshi va yomon.</p>",
    },
]


# =====================================================================
# PK-67 — (으)ㄹ 뿐만 아니라
# =====================================================================

Q_PK67 = [
    # 1–5 tanish
    {
        "text": "<p><strong>(으)ㄹ 뿐만 아니라</strong> nimani bildiradi?</p>",
        "choices": ["Faqat … emas, … ham", "…, … esa …", "…gan sari",
                    "sal boʻlmasa …"],
        "correct": "Faqat … emas, … ham",
        "explanation": "<p>맛있을 뿐만 아니라 값도 싸요 — “faqat mazali "
                       "emas, narxi ham arzon”.</p>",
    },
    {
        "text": "<p><strong>뿐</strong> soʻzi nima degani?</p>",
        "choices": ["Faqat, xolos", "Usul", "Holat", "Niyat"],
        "correct": "Faqat, xolos",
        "explanation": "<p>Yana bitta <strong>aniqlovchi + ot</strong>: "
                       "것 · 줄 · 뻔 · 테 · 뿐.</p>",
    },
    {
        "text": "<p><strong>맛있다</strong> bu qolipda qanday shaklga "
                "kiradi?</p>",
        "choices": ["맛있는 뿐만 아니라", "맛있을 뿐만 아니라",
                    "맛있은 뿐만 아니라", "맛있던 뿐만 아니라"],
        "correct": "맛있을 뿐만 아니라",
        "explanation": "<p>뿐 dan oldin <strong>(으)ㄹ</strong> keladi; "
                       "맛있 da 받침 bor → 을.</p>",
    },
    {
        "text": "<p>Ot bilan ishlatilganda qanday boʻladi?</p>",
        "choices": ["한국어를 뿐만 아니라", "한국어가 뿐만 아니라",
                    "한국어뿐만 아니라", "한국어일 뿐만 아니라"],
        "correct": "한국어뿐만 아니라",
        "explanation": "<p>Ot bilan <strong>을/를 va 이/가 tushadi</strong> "
                       "— 뿐만 아니라 toʻgʻridan-toʻgʻri otga "
                       "yopishadi.</p>",
    },
    {
        "text": "<p>Ikkinchi gapda odatda qaysi qoʻshimcha turadi?</p>",
        "choices": ["도", "만", "은/는", "까지"],
        "correct": "도",
        "explanation": "<p>값<strong>도</strong> 싸요 — “narxi <strong>ham"
                       "</strong> arzon”. Qolipning maʼnosi shuni "
                       "talab qiladi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 그 식당은 음식이 <strong>______</strong> "
                "뿐만 아니라 값도 싸요. (맛있다)</p>",
        "choices": ["맛있는", "맛있을", "맛있은", "맛있어서"],
        "correct": "맛있을",
        "explanation": "<p>받침 bor → <strong>을 뿐만 아니라</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: <strong>______</strong> 뿐만 아니라 한국 "
                "문화도 배워요. (한국어)</p>",
        "choices": ["한국어를", "한국어가", "한국어", "한국어에"],
        "correct": "한국어",
        "explanation": "<p>Ot bilan qoʻshimcha qoʻyilmaydi: "
                       "<strong>한국어뿐만 아니라</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 어제는 비가 <strong>______</strong> 뿐만 "
                "아니라 바람도 불었어요. (오다)</p>",
        "choices": ["오는", "올", "온", "왔을"],
        "correct": "올",
        "explanation": "<p>오 da 받침 yoʻq → <strong>올 뿐만 아니라</strong>. "
                       "Zamonni oxirgi feʼl koʻtaradi (불었어요).</p>",
    },
    {
        "text": "<p>“Hana faqat talaba emas, balki mashhur qoʻshiqchi” — "
                "qaysi biri toʻgʻri?</p>",
        "choices": ["하나 씨는 학생인 뿐만 아니라 유명한 가수예요",
                    "하나 씨는 학생일 뿐만 아니라 유명한 가수예요",
                    "하나 씨는 학생을 뿐만 아니라 유명한 가수예요",
                    "하나 씨는 학생는 뿐만 아니라 유명한 가수예요"],
        "correct": "하나 씨는 학생일 뿐만 아니라 유명한 가수예요",
        "explanation": "<p>이다 bilan — <strong>일 뿐만 아니라</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 그 사람은 노래를 <strong>______</strong> "
                "뿐만 아니라 춤도 잘 춰요. (잘하다)</p>",
        "choices": ["잘하는", "잘한", "잘할", "잘했을"],
        "correct": "잘할",
        "explanation": "<p>잘하 da 받침 yoʻq → <strong>잘할 뿐만 "
                       "아니라</strong>.</p>",
    },
    {
        "text": "<p>Jumla boshida turgan <strong>뿐만 아니라</strong> nima "
                "degani?</p>",
        "choices": ["Bundan tashqari", "Shuning uchun", "Lekin", "Chunki"],
        "correct": "Bundan tashqari",
        "explanation": "<p>“그 카페는 커피가 맛있어요. <strong>뿐만 아니라</strong> "
                       "자리도 넓어요.” Yozma matnda 또한 bilan "
                       "almashtirsa ham boʻladi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 이 책은 <strong>______</strong> 뿐만 아니라 "
                "그림도 예뻐요. (재미있다)</p>",
        "choices": ["재미있는", "재미있을", "재미있은", "재미있어서"],
        "correct": "재미있을",
        "explanation": "<p>재미있 da 받침 bor → <strong>재미있을 뿐만 "
                       "아니라</strong>.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Nima uchun <strong>음식이 맛있을 뿐만 아니라 값이 "
                "비싸요</strong> notoʻgʻri?</p>",
        "choices": ["받침 xato",
                    "Ikkala dalil bir tomonga qarashi kerak — bu yerda biri "
                    "maqtov, biri ayb",
                    "Zamon xato",
                    "값 ega boʻlolmaydi"],
        "correct": "Ikkala dalil bir tomonga qarashi kerak — bu yerda biri "
                   "maqtov, biri ayb",
        "explanation": "<p>Qarama-qarshi dalillar uchun PK-66 dagi "
                       "<strong>반면에</strong> kerak: 맛있는 반면에 값이 "
                       "비싸요.</p>",
    },
    {
        "text": "<p>Qaysi qolip qarama-qarshi ikki tomonni "
                "koʻrsatadi?</p>",
        "choices": ["(으)ㄹ 뿐만 아니라", "(으)ㄴ/는 반면에", "(으)ㄹ수록",
                    "(으)ㄹ 테니까"],
        "correct": "(으)ㄴ/는 반면에",
        "explanation": "<p>뿐만 아니라 — <strong>bir tomonga</strong> "
                       "qaragan ikki dalilni qoʻshadi. 반면에 esa ikki "
                       "<strong>qarama-qarshi</strong> tomonni.</p>",
    },
    {
        "text": "<p>Zamon qoʻshimchasi qayerda boʻladi?</p>",
        "choices": ["뿐 dan oldin", "Oxirgi feʼlda", "Ikkalasida",
                    "뿐만 va 아니라 orasida"],
        "correct": "Oxirgi feʼlda",
        "explanation": "<p>비가 <strong>올</strong> 뿐만 아니라 바람도 "
                       "<strong>불었어요</strong> — oldida (으)ㄹ "
                       "yetadi.</p>",
    },
    {
        "text": "<p>Bu beshta qolipda nima umumiy? "
                "<strong>것 · 줄 · 뻔 · 테 · 뿐</strong></p>",
        "choices": ["Hammasi feʼl", "Hammasi ot — aniqlovchi + ot qurilmasi",
                    "Hammasi qoʻshimcha", "Hammasi ravish"],
        "correct": "Hammasi ot — aniqlovchi + ot qurilmasi",
        "explanation": "<p>Shuning uchun beshtasining ham oldida aniqlovchi "
                       "shakli turadi va ular bir xil his beradi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>한국어를 뿐만 아니라 한국 문화도 "
                "배워요.</strong></p>",
        "choices": ["한국어를 → 한국어", "한국어를 → 한국어가",
                    "한국어를 → 한국어일", "Xato yoʻq"],
        "correct": "한국어를 → 한국어",
        "explanation": "<p>Ot bilan <strong>을/를 tushadi</strong>: "
                       "한국어뿐만 아니라.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>음식이 맛있는 뿐만 아니라 값도 "
                "싸요.</strong></p>",
        "choices": ["맛있는 → 맛있을", "맛있는 → 맛있은",
                    "값도 → 값이", "Xato yoʻq"],
        "correct": "맛있는 → 맛있을",
        "explanation": "<p>뿐 dan oldin <strong>(으)ㄹ</strong> keladi, "
                       "는 emas.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Faqat koreys tilini emas, madaniyatini ham "
                "oʻrganamiz” — qaysi biri toʻgʻri?</p>",
        "choices": ["한국어뿐만 아니라 한국 문화도 배워요",
                    "한국어를 뿐만 아니라 한국 문화도 배워요",
                    "한국어뿐만 아니라 한국 문화를 배워요",
                    "한국어일 뿐만 아니라 한국 문화도 배워요"],
        "correct": "한국어뿐만 아니라 한국 문화도 배워요",
        "explanation": "<p>Ot — qoʻshimchasiz, ikkinchi gapda esa "
                       "<strong>도</strong>.</p>",
    },
    {
        "text": "<p><strong>가:</strong> 그 식당 어때요?</p>"
                "<p><strong>나:</strong> ___</p>",
        "choices": ["음식이 맛있을 뿐만 아니라 값도 싸요",
                    "음식이 맛있는 뿐만 아니라 값도 싸요",
                    "음식이 맛있을 뿐만 아니라 값이 비싸요",
                    "음식이 맛있을 뿐만 아니라 값을 싸요"],
        "correct": "음식이 맛있을 뿐만 아니라 값도 싸요",
        "explanation": "<p>(으)ㄹ shakli, ikkinchi gapda <strong>도</strong>, "
                       "va ikkala dalil ham <strong>ijobiy</strong> — "
                       "uchala shart bajarilgan.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-65 Mashq: (으)ㄹ수록 — “…gan sari”",
        "description": "20 savol — 받침 ayrisi, (으)면 bilan kuchaytirish, "
                       "아/어지다 juftligi va zamonning oʻrni.",
        "tutorial":    "PK-65:",
        "level":       "medium",
        "questions":   Q_PK65,
    },
    {
        "title":       "PK-66 Mashq: (으)ㄴ/는 반면에 — qarama-qarshi tomon",
        "description": "20 savol — feʼl/sifat/ot shakllari, 지만 dan farqi, "
                       "은/는 ning oʻrni va 반면 qisqargan shakli.",
        "tutorial":    "PK-66:",
        "level":       "medium",
        "questions":   Q_PK66,
    },
    {
        "title":       "PK-67 Mashq: (으)ㄹ 뿐만 아니라 — “faqat emas, balki”",
        "description": "20 savol — (으)ㄹ shakli, ot bilan qoʻshimchaning "
                       "tushishi, 도 ning oʻrni va 반면에 dan farqi.",
        "tutorial":    "PK-67:",
        "level":       "medium",
        "questions":   Q_PK67,
    },
]
