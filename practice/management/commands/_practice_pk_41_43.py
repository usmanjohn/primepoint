# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-41 … PK-43.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_41_43.py --master=prime \\
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
# PK-41 — 아/어 보다
# =====================================================================

Q_PK41 = [
    # 1–5 tanish
    {
        "text": "<p><strong>아/어 보다</strong> nima maʼnoni beradi?</p>",
        "choices": ["…ib koʻrmoq, sinab koʻrmoq", "…ib turibdi", "…moqchiman",
                    "…dan keyin"],
        "correct": "…ib koʻrmoq, sinab koʻrmoq",
        "explanation": "<p>보다 “koʻrmoq” degani va oʻzbekchadagi “-ib koʻrmoq” "
                       "bilan bir xil obrazdan yasalgan: 먹어 보다 = “yeb "
                       "koʻrmoq”.</p>",
    },
    {
        "text": "<p><strong>먹다</strong> ning 아/어 보다 shakli qaysi?</p>",
        "choices": ["먹고 보다", "먹으 보다", "먹어 보다", "먹은 보다"],
        "correct": "먹어 보다",
        "explanation": "<p>아/어요 shaklini oling (먹어요), 요 oʻrniga 보다 "
                       "qoʻying: <strong>먹어 보다</strong>.</p>",
    },
    {
        "text": "<p><strong>하다</strong> ning 아/어 보다 shakli qaysi?</p>",
        "choices": ["하 보다", "해 보다", "하어 보다", "했 보다"],
        "correct": "해 보다",
        "explanation": "<p>하다 → 해요 → <strong>해 보다</strong>. “한번 해 "
                       "보세요” — “bir qilib koʻring”.</p>",
    },
    {
        "text": "<p><strong>가 봤어요</strong> nima degani?</p>",
        "choices": ["Boraman", "Borib koʻrganman", "Bormoqchiman",
                    "Borib turibman"],
        "correct": "Borib koʻrganman",
        "explanation": "<p>아/어 봤어요 hayotdagi <strong>tajriba</strong>ni "
                       "bildiradi: 한국에 가 봤어요? — “Koreyaga borib "
                       "koʻrganmisiz?”</p>",
    },
    {
        "text": "<p>아/어 보다 qaysi soʻzlar bilan ishlatilmaydi?</p>",
        "choices": ["Sifatlar bilan", "Harakat feʼllari bilan",
                    "Oʻtgan zamon bilan", "Inkor bilan"],
        "correct": "Sifatlar bilan",
        "explanation": "<p>Sinab koʻrish uchun harakat kerak. <s>예뻐 보다</s>, "
                       "<s>더워 보다</s> deyilmaydi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 이 차를 <strong>______</strong> (마시다) 보세요.</p>",
        "choices": ["마시", "마셔", "마시고", "마신"],
        "correct": "마셔",
        "explanation": "<p>마시다 → 마셔요 → <strong>마셔 보세요</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 한국 노래를 <strong>______</strong> (듣다) 봤어요?</p>",
        "choices": ["듣어", "들어", "듣고", "들으"],
        "correct": "들어",
        "explanation": "<p>듣다 — ㄷ notoʻgʻri feʼli. 아/어 unli bilan "
                       "boshlanadi, shuning uchun ㄷ → ㄹ: <strong>들어 "
                       "봤어요</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 이 옷을 <strong>______</strong> (입다) 보세요.</p>",
        "choices": ["입고", "입으", "입어", "입은"],
        "correct": "입어",
        "explanation": "<p>입다 → 입어요 → <strong>입어 보세요</strong> — "
                       "“bu kiyimni kiyib koʻring”.</p>",
    },
    {
        "text": "<p>Toʻldiring: 저는 김치를 <strong>______</strong>. "
                "(“yeb koʻrgim keladi”)</p>",
        "choices": ["먹어 보고 싶어요", "먹어 보세요", "먹어 봤어요", "먹고 싶어 봐요"],
        "correct": "먹어 보고 싶어요",
        "explanation": "<p>먹어 보다 (sinab koʻrmoq) + 고 싶다 (xohlamoq) = "
                       "<strong>먹어 보고 싶어요</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 친구를 <strong>______</strong> (돕다) 봤어요.</p>",
        "choices": ["돕어", "도와", "돕고", "도우"],
        "correct": "도와",
        "explanation": "<p>돕다 — ㅂ notoʻgʻri feʼli: 도와요 → <strong>도와 "
                       "봤어요</strong>.</p>",
    },
    {
        "text": "<p>“Koreyaga hech borgan emasman” — qaysi biri?</p>",
        "choices": ["한국에 가 봤어요", "한국에 안 가 봤어요", "한국에 못 가 봤어요",
                    "한국에 가 보세요"],
        "correct": "한국에 안 가 봤어요",
        "explanation": "<p><strong>안</strong> — shunchaki bormaganman. "
                       "못 가 봤어요 esa “bora olmaganman” — imkon boʻlmagan.</p>",
    },
    {
        "text": "<p>Toʻldiring: <strong>______</strong> 한국 음식을 먹어 보세요. "
                "(“bir marta”)</p>",
        "choices": ["한번", "한 개", "하나", "한 시"],
        "correct": "한번",
        "explanation": "<p><strong>한번</strong> — “bir marta”. 아/어 보세요 "
                       "bilan juda koʻp yuradi: 한번 해 보세요.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p><strong>먹으세요</strong> va <strong>먹어 보세요</strong> — "
                "farqi nima?</p>",
        "choices": ["Farqi yoʻq",
                    "Birinchisi koʻrsatma, ikkinchisi yumshoq tavsiya",
                    "Birinchisi oʻtgan zamon",
                    "Ikkinchisi faqat yozma nutqda"],
        "correct": "Birinchisi koʻrsatma, ikkinchisi yumshoq tavsiya",
        "explanation": "<p>먹으세요 — “yeng”. 먹어 보세요 — “bir sinab koʻring, "
                       "yoqmasa qoʻying”. Notanish narsani tavsiya qilganda "
                       "ikkinchisi tabiiyroq.</p>",
    },
    {
        "text": "<p>“안 가 봤어요” va “못 가 봤어요” orasidagi farq nima?</p>",
        "choices": ["Birinchisi — bormaganman, ikkinchisi — bora olmaganman",
                    "Birinchisi rasmiy, ikkinchisi norasmiy",
                    "Birinchisi kelasi zamon",
                    "Farqi yoʻq"],
        "correct": "Birinchisi — bormaganman, ikkinchisi — bora olmaganman",
        "explanation": "<p>PK-21 va PK-22 dagi <strong>안 / 못</strong> farqi bu "
                       "yerda ham ishlaydi. 못 da biroz afsus bor: xohlardim, "
                       "lekin imkon boʻlmadi.</p>",
    },
    {
        "text": "<p>Qaysi gap notoʻgʻri?</p>",
        "choices": ["김치를 먹어 보세요", "한국에 가 봤어요", "이 옷이 예뻐 보세요",
                    "노래를 들어 보세요"],
        "correct": "이 옷이 예뻐 보세요",
        "explanation": "<p>예쁘다 — sifat, sinab koʻrib boʻlmaydi. Kiyim haqida "
                       "aytmoqchi boʻlsangiz: <strong>이 옷을 입어 "
                       "보세요</strong>.</p>",
    },
    {
        "text": "<p>Nega <strong>들어 보다</strong> da 듣 oʻzgardi, ammo "
                "<strong>듣고 싶다</strong> da oʻzgarmaydi?</p>",
        "choices": ["아/어 unli, 고 esa undosh bilan boshlanadi",
                    "보다 notoʻgʻri feʼl",
                    "고 싶다 rasmiy shakl",
                    "Bu istisno, qoidasi yoʻq"],
        "correct": "아/어 unli, 고 esa undosh bilan boshlanadi",
        "explanation": "<p>PK-32 ning asosiy qoidasi: notoʻgʻri tuslanish faqat "
                       "<strong>unli bilan boshlanadigan</strong> qoʻshimcha "
                       "oldida ishlaydi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>김치를 먹고 보세요.</strong></p>",
        "choices": ["먹고 → 먹어", "먹고 → 먹으", "보세요 → 봤어요", "Xato yoʻq"],
        "correct": "먹고 → 먹어",
        "explanation": "<p>Qolip 고 emas, <strong>아/어</strong> bilan yasaladi: "
                       "김치를 먹어 보세요.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>저는 한국에 갔어 봤어요.</strong></p>",
        "choices": ["갔어 → 가", "갔어 → 갔", "봤어요 → 보세요", "Xato yoʻq"],
        "correct": "갔어 → 가",
        "explanation": "<p>Zamon faqat <strong>보다</strong> ga qoʻyiladi: "
                       "저는 한국에 <strong>가 봤어요</strong>.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Bu qoʻshiqni bir tinglab koʻring” — qaysi biri toʻgʻri?</p>",
        "choices": ["이 노래를 한번 듣어 보세요", "이 노래를 한번 들어 보세요",
                    "이 노래를 한번 듣고 보세요", "이 노래를 한번 들어 봤어요"],
        "correct": "이 노래를 한번 들어 보세요",
        "explanation": "<p>듣다 → 들어요 → 들어 보세요, oldiga 한번 — "
                       "“bir marta”.</p>",
    },
    {
        "text": "<p>“Chechu oroliga borib koʻrgim keladi” — qaysi biri toʻgʻri?</p>",
        "choices": ["제주도에 가 보고 싶어요", "제주도에 가고 보고 싶어요",
                    "제주도에 가 봤고 싶어요", "제주도에 가 보세요 싶어요"],
        "correct": "제주도에 가 보고 싶어요",
        "explanation": "<p>가 보다 + 고 싶다 → <strong>가 보고 싶어요</strong>.</p>",
    },
]


# =====================================================================
# PK-42 — 고 있다 va 아/어 있다
# =====================================================================

Q_PK42 = [
    # 1–5 tanish
    {
        "text": "<p><strong>고 있다</strong> nima maʼnoni beradi?</p>",
        "choices": ["Harakat hozir davom etyapti", "Harakat tugagan, natijasi turibdi",
                    "Harakatni sinab koʻrish", "Harakatga niyat qilish"],
        "correct": "Harakat hozir davom etyapti",
        "explanation": "<p><strong>고 있다</strong> — “…yapman”: 밥을 먹고 "
                       "있어요 (ovqat yeyapman).</p>",
    },
    {
        "text": "<p><strong>먹다</strong> ning 고 있다 shakli qaysi?</p>",
        "choices": ["먹어 있어요", "먹으고 있어요", "먹고 있어요", "먹는 있어요"],
        "correct": "먹고 있어요",
        "explanation": "<p>Oʻzakka shundoq 고 있다 qoʻshiladi — 받침 ayrisi "
                       "yoʻq: <strong>먹고 있어요</strong>.</p>",
    },
    {
        "text": "<p><strong>앉아 있어요</strong> nima degani?</p>",
        "choices": ["Oʻtiryapti (hozir oʻtirish harakatida)", "Oʻtiribdi (oʻtirgan holatda)",
                    "Oʻtirmoqchi", "Oʻtirib koʻrdi"],
        "correct": "Oʻtiribdi (oʻtirgan holatda)",
        "explanation": "<p><strong>아/어 있다</strong> tugagan harakatning "
                       "natijasini koʻrsatadi. 앉고 있어요 esa hozir oʻtirayotgan "
                       "paytni bildiradi.</p>",
    },
    {
        "text": "<p><strong>듣다</strong> ning 고 있다 shakli qaysi?</p>",
        "choices": ["들고 있어요", "듣고 있어요", "들어 있어요", "들으고 있어요"],
        "correct": "듣고 있어요",
        "explanation": "<p>고 undosh bilan boshlanadi, shuning uchun oʻzak "
                       "oʻzgarmaydi: <strong>듣고 있어요</strong>. (들고 있어요 "
                       "boshqa gap — “qoʻlida ushlab turibdi”.)</p>",
    },
    {
        "text": "<p>아/어 있다 qaysi feʼllar bilan <em>kelmaydi</em>?</p>",
        "choices": ["Toʻldiruvchi oladigan feʼllar bilan", "앉다, 서다 kabi feʼllar bilan",
                    "Oʻtgan zamonda", "Inkor bilan"],
        "correct": "Toʻldiruvchi oladigan feʼllar bilan",
        "explanation": "<p><s>밥을 먹어 있어요</s> deyilmaydi — 먹다 toʻldiruvchi "
                       "oladi. Toʻgʻrisi: 밥을 <strong>먹고</strong> 있어요.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 저는 지금 한국어를 <strong>______</strong> "
                "(공부하다).</p>",
        "choices": ["공부해 있어요", "공부하고 있어요", "공부한 있어요",
                    "공부하는 있어요"],
        "correct": "공부하고 있어요",
        "explanation": "<p>Davom etayotgan harakat → <strong>고 있다</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 수진 씨가 문 앞에 <strong>______</strong> (서다).</p>",
        "choices": ["서고 있어요", "서 있어요", "선 있어요", "서는 있어요"],
        "correct": "서 있어요",
        "explanation": "<p>“Eshik oldida turibdi” — bu harakat emas, holat: "
                       "<strong>서 있어요</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 동생이 침대에 <strong>______</strong> (눕다).</p>",
        "choices": ["눕어 있어요", "누워 있어요", "눕고 있어요", "누우 있어요"],
        "correct": "누워 있어요",
        "explanation": "<p>눕다 — ㅂ notoʻgʻri feʼli: 누워요 → <strong>누워 "
                       "있어요</strong> (“yotibdi”).</p>",
    },
    {
        "text": "<p>Toʻldiring: 어제 저녁에 텔레비전을 <strong>______</strong> "
                "(보다).</p>",
        "choices": ["보고 있었어요", "봤고 있어요", "봐 있었어요", "보고 있어요"],
        "correct": "보고 있었어요",
        "explanation": "<p>Zamon <strong>있다</strong> ga qoʻyiladi: "
                       "있<strong>었</strong>어요.</p>",
    },
    {
        "text": "<p>Toʻldiring: 베크조드 씨가 벌써 교실에 <strong>______</strong> "
                "(오다).</p>",
        "choices": ["오고 있어요", "와 있어요", "온 있어요", "오아 있어요"],
        "correct": "와 있어요",
        "explanation": "<p><strong>와 있어요</strong> — kelib boʻlgan, shu "
                       "yerda. 오고 있어요 desangiz “kelayapti, hali yoʻlda” "
                       "degan boshqa maʼno chiqadi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 아프소나 씨는 티셔츠를 <strong>______</strong> "
                "(입다).</p>",
        "choices": ["입어 있어요", "입고 있어요", "입은 있어요", "입으 있어요"],
        "correct": "입고 있어요",
        "explanation": "<p>Kiyim feʼllari <strong>고 있다</strong> oladi. "
                       "Vaziyatga qarab “kiygan” yoki “kiyayapti” degani "
                       "boʻlishi mumkin.</p>",
    },
    {
        "text": "<p>Toʻldiring: 냉장고에 우유가 조금 <strong>______</strong> "
                "(남다).</p>",
        "choices": ["남고 있어요", "남아 있어요", "남은 있어요", "남으 있어요"],
        "correct": "남아 있어요",
        "explanation": "<p>남다 — holat feʼli: <strong>남아 있어요</strong> "
                       "(“ozgina qolibdi”).</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p><strong>앉고 있어요</strong> va <strong>앉아 있어요</strong> — "
                "farqi nima?</p>",
        "choices": ["Birinchisi “oʻtiryapti”, ikkinchisi “oʻtiribdi”",
                    "Birinchisi “oʻtiribdi”, ikkinchisi “oʻtiryapti”",
                    "Birinchisi rasmiy, ikkinchisi norasmiy",
                    "Farqi yoʻq"],
        "correct": "Birinchisi “oʻtiryapti”, ikkinchisi “oʻtiribdi”",
        "explanation": "<p>고 있다 — harakat hozir ketyapti. 아/어 있다 — harakat "
                       "tugagan, natijasi turibdi. Oʻzbekchadagi “-yapti / "
                       "-ibdi” farqining aynan oʻzi.</p>",
    },
    {
        "text": "<p>Qaysi gap notoʻgʻri?</p>",
        "choices": ["책을 읽고 있어요", "책을 읽어 있어요", "의자에 앉아 있어요",
                    "음악을 듣고 있어요"],
        "correct": "책을 읽어 있어요",
        "explanation": "<p>읽다 toʻldiruvchi oladi (책<strong>을</strong>), "
                       "shuning uchun 아/어 있다 bilan kelmaydi. Toʻgʻrisi: "
                       "책을 읽고 있어요.</p>",
    },
    {
        "text": "<p>“Bekzod hozir kelayapti (hali yoʻlda)” — qaysi biri?</p>",
        "choices": ["베크조드 씨가 와 있어요", "베크조드 씨가 오고 있어요",
                    "베크조드 씨가 온 후에 왔어요", "베크조드 씨가 와 봤어요"],
        "correct": "베크조드 씨가 오고 있어요",
        "explanation": "<p>Harakat hali davom etyapti → <strong>오고 "
                       "있어요</strong>. 와 있어요 esa “kelib boʻlgan”.</p>",
    },
    {
        "text": "<p>Nega <strong>듣고 있어요</strong> da 듣 oʻzgarmaydi, ammo "
                "<strong>들어 보세요</strong> da oʻzgaradi?</p>",
        "choices": ["고 undosh, 아/어 esa unli bilan boshlanadi",
                    "있다 notoʻgʻri feʼl",
                    "보다 rasmiy shakl",
                    "Bu istisno"],
        "correct": "고 undosh, 아/어 esa unli bilan boshlanadi",
        "explanation": "<p>Yana oʻsha PK-32 qoidasi: notoʻgʻri tuslanish faqat "
                       "unli bilan boshlanadigan qoʻshimcha oldida ishlaydi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>어제 공부했고 있었어요.</strong></p>",
        "choices": ["공부했고 → 공부하고", "있었어요 → 있어요",
                    "공부했고 → 공부해", "Xato yoʻq"],
        "correct": "공부했고 → 공부하고",
        "explanation": "<p>Zamon faqat <strong>있다</strong> ga qoʻyiladi: "
                       "어제 공부하고 있었어요.</p>",
    },
    {
        "text": "<p>Xatoni toping (“stulda oʻtiribdi” maʼnosida): "
                "<strong>지영 씨는 의자에 앉고 있어요.</strong></p>",
        "choices": ["앉고 → 앉아", "앉고 → 앉은", "의자에 → 의자를", "Xato yoʻq"],
        "correct": "앉고 → 앉아",
        "explanation": "<p>Holatni aytmoqchi boʻlsangiz — <strong>앉아 "
                       "있어요</strong>. 앉고 있어요 “hozir oʻtirayotgan payt” "
                       "degani.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Hozir ovqat yeyapman” — qaysi biri toʻgʻri?</p>",
        "choices": ["지금 밥을 먹어 있어요", "지금 밥을 먹고 있어요",
                    "지금 밥을 먹는 있어요", "지금 밥을 먹어 봤어요"],
        "correct": "지금 밥을 먹고 있어요",
        "explanation": "<p>Davom etayotgan harakat va toʻldiruvchili feʼl — "
                       "ikkalasi ham <strong>고 있다</strong> ni talab "
                       "qiladi.</p>",
    },
    {
        "text": "<p>“Doʻstim kutubxonada oʻtiribdi” — qaysi biri toʻgʻri?</p>",
        "choices": ["친구가 도서관에 앉아 있어요", "친구가 도서관에 앉고 있어요",
                    "친구가 도서관에 앉은 있어요", "친구가 도서관에 앉아 봤어요"],
        "correct": "친구가 도서관에 앉아 있어요",
        "explanation": "<p>Oʻtirish harakati tugagan, qolgani — oʻtirgan "
                       "holat: <strong>앉아 있어요</strong>.</p>",
    },
]


# =====================================================================
# PK-43 — 동사 + 는 (aniqlovchi)
# =====================================================================

Q_PK43 = [
    # 1–5 tanish
    {
        "text": "<p><strong>동사 + 는</strong> aniqlovchisi qanday maʼno beradi?</p>",
        "choices": ["…adigan, …yotgan (hozirgi zamon)", "…gan (oʻtgan zamon)",
                    "…adigan (kelasi zamon)", "…gani uchun"],
        "correct": "…adigan, …yotgan (hozirgi zamon)",
        "explanation": "<p>는 — hozirgi zamon va odat aniqlovchisi: 읽는 책 — "
                       "“oʻqiydigan kitob”.</p>",
    },
    {
        "text": "<p><strong>먹다</strong> ning aniqlovchi shakli qaysi?</p>",
        "choices": ["먹은", "먹을", "먹는", "먹어"],
        "correct": "먹는",
        "explanation": "<p>Oʻzakka shundoq 는 qoʻshiladi: <strong>먹는 "
                       "사람</strong> — “yeydigan odam”.</p>",
    },
    {
        "text": "<p><strong>살다</strong> ning aniqlovchi shakli qaysi?</p>",
        "choices": ["살는", "사는", "산", "살은"],
        "correct": "사는",
        "explanation": "<p>ㄹ oʻzak ㄴ tovushi oldida ㄹ ni yoʻqotadi: "
                       "살 + 는 → <strong>사는</strong>. 서울에 사는 친구.</p>",
    },
    {
        "text": "<p>“Qiziqarli kitob” — qaysi biri toʻgʻri?</p>",
        "choices": ["재미있은 책", "재미있는 책", "재미있을 책", "재미있어 책"],
        "correct": "재미있는 책",
        "explanation": "<p>재미있다 ichida <strong>있다</strong> — feʼl bor, "
                       "shuning uchun 는 oladi.</p>",
    },
    {
        "text": "<p>Aniqlovchi ot bilan qanday joylashadi?</p>",
        "choices": ["Otning oldida", "Otning orqasida", "Gap oxirida",
                    "Ega bilan birga"],
        "correct": "Otning oldida",
        "explanation": "<p>Koreys tilida aniqlovchi doim otdan <strong>oldin</strong> "
                       "turadi — oʻzbek tilidagidek: “kitob oʻqiydigan bola” = "
                       "책을 읽는 아이.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 지금 음악을 <strong>______</strong> (듣다) 사람은 "
                "제 동생이에요.</p>",
        "choices": ["들는", "듣는", "들은", "듣은"],
        "correct": "듣는",
        "explanation": "<p>는 undosh bilan boshlanadi, shuning uchun 듣 "
                       "oʻzgarmaydi: <strong>듣는 사람</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 부산에 <strong>______</strong> (살다) 친구가 "
                "있어요.</p>",
        "choices": ["사는", "살는", "산", "살은"],
        "correct": "사는",
        "explanation": "<p>ㄹ tushadi: 살 + 는 → <strong>사는</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 제가 <strong>______</strong> (알다) 사람이에요.</p>",
        "choices": ["알는", "아는", "안", "알은"],
        "correct": "아는",
        "explanation": "<p>알다 ham ㄹ oʻzak: <strong>아는 사람</strong> — "
                       "“tanish odam”.</p>",
    },
    {
        "text": "<p>Toʻldiring: 한국어를 <strong>______</strong> (공부하다) "
                "학생이 많아요.</p>",
        "choices": ["공부한", "공부할", "공부해", "공부하는"],
        "correct": "공부하는",
        "explanation": "<p><strong>공부하는 학생</strong> — “koreys tilini "
                       "oʻrganadigan talaba”. Toʻldiruvchi (한국어를) "
                       "aniqlovchi ichida qoladi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 이 식당은 <strong>______</strong> 음식이 많아요. "
                "(“mazali”)</p>",
        "choices": ["맛있는", "맛있은", "맛있을", "맛있어"],
        "correct": "맛있는",
        "explanation": "<p>맛있다 ham 있다 dan yasalgan → <strong>맛있는</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: <strong>______</strong> 자주 가는 카페가 학교 "
                "앞에 있어요.</p>",
        "choices": ["저는", "제는", "제가", "저를"],
        "correct": "제가",
        "explanation": "<p>Aniqlovchi ichidagi ega <strong>이/가</strong> oladi, "
                       "은/는 emas: <strong>제가 자주 가는 카페</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 어머니가 <strong>______</strong> (만들다) 음식이 "
                "제일 맛있어요.</p>",
        "choices": ["만들는", "만드는", "만든", "만들은"],
        "correct": "만드는",
        "explanation": "<p>만들다 — ㄹ oʻzak: 만들 + 는 → <strong>만드는</strong>.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p><strong>먹는 사람</strong> va <strong>먹은 사람</strong> — "
                "farqi nima?</p>",
        "choices": ["Birinchisi “yeydigan odam”, ikkinchisi “yegan odam”",
                    "Birinchisi “yegan odam”, ikkinchisi “yeydigan odam”",
                    "Birinchisi rasmiy, ikkinchisi norasmiy",
                    "Farqi yoʻq"],
        "correct": "Birinchisi “yeydigan odam”, ikkinchisi “yegan odam”",
        "explanation": "<p><strong>는</strong> — hozirgi zamon, "
                       "<strong>(으)ㄴ</strong> — oʻtgan zamon aniqlovchisi "
                       "(PK-44).</p>",
    },
    {
        "text": "<p>Nega 재미있다 는 oladi, 예쁘다 esa olmaydi?</p>",
        "choices": ["재미있다 ichida 있다 — feʼl bor, 예쁘다 esa sifat",
                    "재미있다 uzunroq soʻz",
                    "예쁘다 notoʻgʻri feʼl",
                    "Ikkalasi ham 는 oladi"],
        "correct": "재미있다 ichida 있다 — feʼl bor, 예쁘다 esa sifat",
        "explanation": "<p>Sifatlar boshqa aniqlovchi shakl oladi (PK-45), "
                       "lekin 재미있다, 맛있다, 멋있다 feʼllar qatorida turadi.</p>",
    },
    {
        "text": "<p>Qaysi gap notoʻgʻri?</p>",
        "choices": ["매일 신문을 읽는 사람", "서울에 사는 친구", "재미있은 책",
                    "제가 아는 사람"],
        "correct": "재미있은 책",
        "explanation": "<p>Toʻgʻrisi — <strong>재미있는 책</strong>.</p>",
    },
    {
        "text": "<p>Nega bu darsda 듣다 oʻzgarmaydi?</p>",
        "choices": ["는 undosh bilan boshlanadi", "는 unli bilan boshlanadi",
                    "듣다 notoʻgʻri feʼl emas", "Aniqlovchida qoidalar ishlamaydi"],
        "correct": "는 undosh bilan boshlanadi",
        "explanation": "<p>Siz buni uch marta koʻrdingiz: 듣기 전에 (PK-38), "
                       "듣고 있어요 (PK-42), 듣는 음악 (bugun). Undosh "
                       "qoʻshimcha oldida oʻzak tinch turadi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>서울에 살는 친구가 있어요.</strong></p>",
        "choices": ["살는 → 사는", "살는 → 산", "친구가 → 친구는", "Xato yoʻq"],
        "correct": "살는 → 사는",
        "explanation": "<p>ㄹ oʻzak ㄴ oldida ㄹ ni yoʻqotadi: "
                       "<strong>사는 친구</strong>.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>제는 자주 가는 카페가 있어요.</strong></p>",
        "choices": ["제는 → 제가", "제는 → 저는", "가는 → 간", "Xato yoʻq"],
        "correct": "제는 → 제가",
        "explanation": "<p>Aniqlovchi ichidagi ega 이/가 oladi: <strong>제가 "
                       "자주 가는 카페</strong>.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>Ikki gapni bittaga birlashtiring: 학생이 한국어를 공부해요. + "
                "그 학생은 제 친구예요.</p>",
        "choices": ["한국어를 공부한 학생은 제 친구예요",
                    "한국어를 공부하는 학생은 제 친구예요",
                    "한국어를 공부해 학생은 제 친구예요",
                    "학생이 한국어를 공부하는 제 친구예요"],
        "correct": "한국어를 공부하는 학생은 제 친구예요",
        "explanation": "<p>Birinchi gap butunligicha aniqlovchiga aylanadi va "
                       "학생 ning <strong>oldiga</strong> oʻtadi.</p>",
    },
    {
        "text": "<p>“Har kuni gazeta oʻqiydigan odam” — qaysi biri toʻgʻri?</p>",
        "choices": ["매일 신문을 읽는 사람", "매일 신문을 읽은 사람",
                    "사람 매일 신문을 읽는", "매일 신문을 읽어 사람"],
        "correct": "매일 신문을 읽는 사람",
        "explanation": "<p>Payt (매일) va toʻldiruvchi (신문을) aniqlovchi "
                       "ichida qoladi, aniqlovchi esa otdan oldin turadi — "
                       "oʻzbekchadagi tartibning aynan oʻzi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-41 Mashq: 아/어 보다 — sinab koʻrish va tajriba",
        "description": "20 savol — yasalishi, 아/어 보세요 tavsiyasi, "
                       "아/어 봤어요 tajribasi va 고 싶다 bilan birikishi.",
        "tutorial":    "PK-41:",
        "level":       "medium",
        "questions":   Q_PK41,
    },
    {
        "title":       "PK-42 Mashq: 고 있다 va 아/어 있다",
        "description": "20 savol — harakat va holat farqi, 아/어 있다 ning "
                       "cheklovi va zamonning oʻrni.",
        "tutorial":    "PK-42:",
        "level":       "medium",
        "questions":   Q_PK42,
    },
    {
        "title":       "PK-43 Mashq: Aniqlovchi 1 — 동사 + 는",
        "description": "20 savol — yasalishi, ㄹ oʻzaklar, 있는/없는 va "
                       "aniqlovchi ichidagi ega.",
        "tutorial":    "PK-43:",
        "level":       "medium",
        "questions":   Q_PK43,
    },
]
