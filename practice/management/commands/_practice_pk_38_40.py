# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-38 … PK-40.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_38_40.py --master=prime \\
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
# PK-38 — 기 전에 / (으)ㄴ 후에
# =====================================================================

Q_PK38 = [
    # 1–5 tanish
    {
        "text": "<p><strong>기 전에</strong> nima maʼnoni beradi?</p>",
        "choices": ["…dan oldin", "…dan keyin", "…gani uchun", "agar …sa"],
        "correct": "…dan oldin",
        "explanation": "<p><strong>기 전에</strong> — “…dan oldin”. Uning juftligi "
                       "<strong>(으)ㄴ 후에</strong> — “…dan keyin”.</p>",
    },
    {
        "text": "<p><strong>가다</strong> ning “borishdan oldin” shakli qaysi?</p>",
        "choices": ["간 전에", "가기 전에", "가은 전에", "갔기 전에"],
        "correct": "가기 전에",
        "explanation": "<p>전에 doim <strong>기</strong> bilan yuradi: 가 + 기 전에 = "
                       "<strong>가기 전에</strong>. 받침 bor-yoʻqligi bu yerda "
                       "ahamiyatsiz.</p>",
    },
    {
        "text": "<p><strong>먹다</strong> ning “yegandan keyin” shakli qaysi?</p>",
        "choices": ["먹기 후에", "먹어 후에", "먹은 후에", "먹는 후에"],
        "correct": "먹은 후에",
        "explanation": "<p>후에 doim <strong>(으)ㄴ</strong> bilan yuradi. 먹 da 받침 "
                       "bor, shuning uchun 으 kiradi: <strong>먹은 후에</strong>.</p>",
    },
    {
        "text": "<p>Qaysi soʻz <strong>후에</strong> bilan bir xil maʼnoda ishlatiladi?</p>",
        "choices": ["전에", "다음에", "때문에", "대신에"],
        "correct": "다음에",
        "explanation": "<p><strong>(으)ㄴ 후에 = (으)ㄴ 다음에 = (으)ㄴ 뒤에</strong> — "
                       "uchalasi toʻliq oʻrin almashadi. Suhbatda 다음에 eng koʻp "
                       "eshitiladi.</p>",
    },
    {
        "text": "<p>Nega <strong>수업 전에</strong> da 기 yoʻq?</p>",
        "choices": ["Chunki 수업 — ot", "Chunki 수업 da 받침 bor",
                    "Chunki gap oʻtgan zamonda", "Chunki 전에 rasmiy shakl"],
        "correct": "Chunki 수업 — ot",
        "explanation": "<p>기 faqat <strong>feʼl</strong> oʻzagiga qoʻshiladi. Ot "
                       "toʻgʻridan toʻgʻri 전에 ni oladi: 수업 전에, 식사 전에, "
                       "시험 전에.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 책을 <strong>______</strong> (읽다) 후에 잤어요.</p>",
        "choices": ["읽은", "읽기", "읽어", "읽었은"],
        "correct": "읽은",
        "explanation": "<p>읽 da 받침 bor (ㄺ) → <strong>읽은 후에</strong>. "
                       "Zamon oxirgi feʼlda (잤어요), shuning uchun 읽었은 emas.</p>",
    },
    {
        "text": "<p>Toʻldiring: 음악을 <strong>______</strong> (듣다) 후에 "
                "공부했어요.</p>",
        "choices": ["듣은", "들은", "듣기", "들기"],
        "correct": "들은",
        "explanation": "<p>듣다 — ㄷ notoʻgʻri feʼli. (으)ㄴ <strong>unli</strong> "
                       "bilan boshlanadi, shuning uchun ㄷ → ㄹ: "
                       "<strong>들은 후에</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 김치를 <strong>______</strong> (만들다) 후에 "
                "친구를 불렀어요.</p>",
        "choices": ["만든", "만들은", "만들기", "만듭은"],
        "correct": "만든",
        "explanation": "<p>ㄹ bilan tugagan oʻzak ㄴ oldida ㄹ ni yoʻqotadi: "
                       "만들 + ㄴ → <strong>만든</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 운동 <strong>______</strong> 물을 많이 마셔요. "
                "(mashqdan <em>oldin</em>)</p>",
        "choices": ["후에", "전에", "때에", "동안"],
        "correct": "전에",
        "explanation": "<p>운동 — ot, shuning uchun 기 kerak emas: "
                       "<strong>운동 전에</strong> — “mashqdan oldin”.</p>",
    },
    {
        "text": "<p>Toʻldiring: 두 시간 <strong>______</strong> 지영 씨가 왔어요.</p>",
        "choices": ["전에", "후에", "다음", "까지"],
        "correct": "전에",
        "explanation": "<p>Vaqt soʻzi + <strong>전에</strong> = “…oldin”: "
                       "두 시간 전에 — ikki soat oldin. Soʻz tartibi oʻzbekchadek.</p>",
    },
    {
        "text": "<p>Toʻldiring: 숙제를 <strong>______</strong> (하다) 후에 게임을 "
                "해요.</p>",
        "choices": ["하기", "했은", "하는", "한"],
        "correct": "한",
        "explanation": "<p>하 da 받침 yoʻq → ㄴ shundoq qoʻshiladi: "
                       "<strong>한 후에</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 저는 <strong>______</strong> (자다) 전에 책을 "
                "읽어요.</p>",
        "choices": ["자기", "잔", "자는", "잤기"],
        "correct": "자기",
        "explanation": "<p>전에 → 기: <strong>자기 전에</strong> — “uxlashdan "
                       "oldin”. Bu kundalik nutqda juda koʻp uchraydigan ibora.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>“Ovqat yeyishdan oldin qoʻlimni yuvaman” — qaysi biri toʻgʻri?</p>",
        "choices": ["밥을 먹은 후에 손을 씻어요", "밥을 먹기 전에 손을 씻어요",
                    "밥을 먹기 후에 손을 씻어요", "밥을 먹은 전에 손을 씻어요"],
        "correct": "밥을 먹기 전에 손을 씻어요",
        "explanation": "<p>“Oldin” → <strong>기 전에</strong>. Qolgan uchtasi "
                       "shakllarni aralashtirib yuborgan.</p>",
    },
    {
        "text": "<p>Nega <strong>듣기 전에</strong> da 듣 oʻzgarmaydi, ammo "
                "<strong>들은 후에</strong> da oʻzgaradi?</p>",
        "choices": ["기 undosh, (으)ㄴ esa unli bilan boshlanadi",
                    "전에 rasmiy, 후에 norasmiy",
                    "Chunki 전에 oʻtgan zamonni bildiradi",
                    "Bu shunchaki istisno, qoidasi yoʻq"],
        "correct": "기 undosh, (으)ㄴ esa unli bilan boshlanadi",
        "explanation": "<p>PK-32 ning asosiy qoidasi: notoʻgʻri tuslanish faqat "
                       "<strong>unli bilan boshlanadigan</strong> qoʻshimcha oldida "
                       "ishlaydi. 기 = ㄱ (undosh) → oʻzgarish yoʻq. (으)ㄴ = unli → "
                       "ㄷ ㄹ ga aylanadi.</p>",
    },
    {
        "text": "<p><strong>수업 전에</strong> va <strong>수업하기 전에</strong> — "
                "farqi nima?</p>",
        "choices": ["Farqi yoʻq, ikkalasi bir xil",
                    "Birinchisi “darsdan oldin”, ikkinchisi “dars oʻtishdan oldin”",
                    "Birinchisi notoʻgʻri",
                    "Ikkinchisi faqat oʻtgan zamonda ishlatiladi"],
        "correct": "Birinchisi “darsdan oldin”, ikkinchisi “dars oʻtishdan oldin”",
        "explanation": "<p>수업 — ot (“dars”), 수업하다 — feʼl (“dars oʻtmoq / "
                       "darsda qatnashmoq”). Oʻquvchi sifatida siz odatda "
                       "<strong>수업 전에</strong> deysiz.</p>",
    },
    {
        "text": "<p>Qaysi gap zamon jihatidan toʻgʻri tuzilgan?</p>",
        "choices": ["운동을 했기 전에 물을 마셨어요",
                    "운동을 하기 전에 물을 마셨어요",
                    "운동을 하기 전에 물을 마셔요했어요",
                    "운동을 했기 전에 물을 마셔요"],
        "correct": "운동을 하기 전에 물을 마셨어요",
        "explanation": "<p>기 전에 dan oldin zamon qoʻyilmaydi. Oxiridagi "
                       "<strong>마셨어요</strong> butun gapni oʻtmishga oladi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>밥을 먹은 전에 손을 씻어요.</strong></p>",
        "choices": ["먹은 → 먹기", "먹은 → 먹었", "전에 → 후에", "씻어요 → 씻은"],
        "correct": "먹은 → 먹기",
        "explanation": "<p>Shakllar almashib ketgan. <strong>전에</strong> doim "
                       "<strong>기</strong> bilan: 밥을 먹기 전에 손을 씻어요.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>친구를 만들은 후에 같이 놀았어요.</strong></p>",
        "choices": ["만들은 → 만든", "만들은 → 만들기", "후에 → 전에",
                    "놀았어요 → 놀아요"],
        "correct": "만들은 → 만든",
        "explanation": "<p>만들다 — ㄹ oʻzak. ㄴ oldida ㄹ tushadi: "
                       "만들 + ㄴ → <strong>만든</strong>.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Uxlashdan oldin koreys tilini oʻrganaman” — qaysi biri toʻgʻri?</p>",
        "choices": ["잔 후에 한국어를 공부해요", "자기 전에 한국어를 공부해요",
                    "자기 후에 한국어를 공부해요", "잤기 전에 한국어를 공부해요"],
        "correct": "자기 전에 한국어를 공부해요",
        "explanation": "<p>“Oldin” → 기 전에, zamon esa oxirgi feʼlda: "
                       "<strong>자기 전에 한국어를 공부해요.</strong></p>",
    },
    {
        "text": "<p>“Dars tugagandan keyin doʻstim bilan uchrashdim” — qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["수업이 끝나기 전에 친구를 만났어요",
                    "수업이 끝난 후에 친구를 만났어요",
                    "수업이 끝나기 후에 친구를 만났어요",
                    "수업이 끝났은 후에 친구를 만났어요"],
        "correct": "수업이 끝난 후에 친구를 만났어요",
        "explanation": "<p>끝나다 → 끝나 (받침 yoʻq) → <strong>끝난 후에</strong>. "
                       "Zamon faqat oxirgi feʼlda: 만났어요.</p>",
    },
]


# =====================================================================
# PK-39 — (으)면서
# =====================================================================

Q_PK39 = [
    # 1–5 tanish
    {
        "text": "<p><strong>(으)면서</strong> nima maʼnoni beradi?</p>",
        "choices": ["…dan keyin", "…ib turib, bir vaqtda", "agar …sa",
                    "…gani uchun"],
        "correct": "…ib turib, bir vaqtda",
        "explanation": "<p><strong>(으)면서</strong> ikki ishni ayni bir paytga "
                       "qoʻyadi: 음악을 들으면서 공부해요 — musiqa tinglab dars "
                       "qilaman.</p>",
    },
    {
        "text": "<p><strong>보다</strong> ning (으)면서 shakli qaysi?</p>",
        "choices": ["보으면서", "봐면서", "보면서", "본면서"],
        "correct": "보면서",
        "explanation": "<p>보 da 받침 yoʻq → 으 kerak emas: <strong>보면서</strong>.</p>",
    },
    {
        "text": "<p><strong>먹다</strong> ning (으)면서 shakli qaysi?</p>",
        "choices": ["먹면서", "먹으면서", "먹어면서", "먹은면서"],
        "correct": "먹으면서",
        "explanation": "<p>먹 da 받침 bor → orasiga 으 kiradi: "
                       "<strong>먹으면서</strong>.</p>",
    },
    {
        "text": "<p>(으)면서 ning eng muhim sharti qaysi?</p>",
        "choices": ["Ikki tomonning egasi bir xil boʻlishi kerak",
                    "Ikkinchi qism buyruq boʻlishi kerak",
                    "Birinchi qism oʻtgan zamonda boʻlishi kerak",
                    "Faqat sifatlar bilan ishlatiladi"],
        "correct": "Ikki tomonning egasi bir xil boʻlishi kerak",
        "explanation": "<p>Ikki ishni <strong>bir odam</strong> bajarishi shart. "
                       "Ikki xil ega boʻlsa, 고 ishlatiladi.</p>",
    },
    {
        "text": "<p>(으)면서 dan <em>oldin</em> oʻtgan zamon qoʻyiladimi?</p>",
        "choices": ["Ha, har doim", "Faqat feʼllar bilan", "Yoʻq, hech qachon",
                    "Faqat inkorda"],
        "correct": "Yoʻq, hech qachon",
        "explanation": "<p><s>들었으면서</s> emas — <strong>들으면서</strong>. "
                       "Zamon oxirgi feʼlda turadi va butun gapga tarqaladi. "
                       "Bu 아/어서 va (으)면 dagi qoidaning aynan oʻzi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 저는 신문을 <strong>______</strong> (읽다) 커피를 "
                "마셔요.</p>",
        "choices": ["읽으면서", "읽면서", "읽어면서", "읽은면서"],
        "correct": "읽으면서",
        "explanation": "<p>읽 da 받침 bor (ㄺ) → <strong>읽으면서</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 지영 씨는 <strong>______</strong> (걷다) 전화해요.</p>",
        "choices": ["걷으면서", "걸으면서", "걷면서", "걸면서"],
        "correct": "걸으면서",
        "explanation": "<p>걷다 — ㄷ notoʻgʻri feʼli. (으) unli oldida ㄷ → ㄹ: "
                       "<strong>걸으면서</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 어머니는 노래를 <strong>______</strong> (부르다) "
                "요리해요.</p>",
        "choices": ["부르면서", "부르으면서", "불면서", "부른면서"],
        "correct": "부르면서",
        "explanation": "<p>부르 da 받침 yoʻq → <strong>부르면서</strong>. "
                       "노래를 부르다 — “qoʻshiq aytmoq”.</p>",
    },
    {
        "text": "<p>Toʻldiring: 아프소나 씨는 <strong>______</strong> (웃다) "
                "인사했어요.</p>",
        "choices": ["웃면서", "웃어면서", "웃으면서", "웃은면서"],
        "correct": "웃으면서",
        "explanation": "<p>웃 da 받침 bor (ㅅ) → <strong>웃으면서</strong> — "
                       "“kulib”.</p>",
    },
    {
        "text": "<p>Toʻldiring: 한국에 <strong>______</strong> (살다) 한국어를 "
                "배웠어요.</p>",
        "choices": ["살으면서", "삶면서", "사면서", "살면서"],
        "correct": "살면서",
        "explanation": "<p>ㄹ oʻzak: 으 qoʻshilmaydi, lekin ㄹ ham tushmaydi — "
                       "<strong>살면서</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 저는 음악을 <strong>______</strong> (듣다) "
                "숙제를 해요.</p>",
        "choices": ["듣으면서", "들으면서", "듣면서", "들면서"],
        "correct": "들으면서",
        "explanation": "<p>듣다 — ㄷ notoʻgʻri feʼli: <strong>들으면서</strong>. "
                       "Bu butun darsning eng koʻp ishlatiladigan misoli.</p>",
    },
    {
        "text": "<p>Toʻldiring: 이 가방은 <strong>______</strong> (가볍다) "
                "튼튼해요.</p>",
        "choices": ["가벼우면서", "가볍으면서", "가볍면서", "가벼면서"],
        "correct": "가벼우면서",
        "explanation": "<p>가볍다 — ㅂ notoʻgʻri feʼli, ㅂ → 우: "
                       "<strong>가벼우면서</strong>. Bu yerda (으)면서 “ham …, "
                       "ham …” maʼnosida: “ham yengil, ham mustahkam”.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p><strong>밥을 먹고 텔레비전을 봐요</strong> nima degani?</p>",
        "choices": ["Ovqat yeb turib televizor koʻraman",
                    "Avval ovqat yeyman, keyin televizor koʻraman",
                    "Ovqat yeganim uchun televizor koʻraman",
                    "Agar ovqat yesam, televizor koʻraman"],
        "correct": "Avval ovqat yeyman, keyin televizor koʻraman",
        "explanation": "<p><strong>고</strong> — ketma-ketlik. Bir vaqtda deyish "
                       "uchun 먹<strong>으면서</strong> 봐요 boʻlishi kerak edi.</p>",
    },
    {
        "text": "<p>“Ovqat yeb turib televizor koʻraman” — qaysi biri?</p>",
        "choices": ["밥을 먹고 텔레비전을 봐요", "밥을 먹어서 텔레비전을 봐요",
                    "밥을 먹으면 텔레비전을 봐요", "밥을 먹으면서 텔레비전을 봐요"],
        "correct": "밥을 먹으면서 텔레비전을 봐요",
        "explanation": "<p>Ikki ish bir daqiqada birga sodir boʻlyapti → "
                       "<strong>(으)면서</strong>. Oʻzbekcha “-ib” ikkalasiga ham "
                       "toʻgʻri kelgani uchun tarjimaga emas, savolga tayaning: "
                       "birga boʻlyaptimi?</p>",
    },
    {
        "text": "<p>Qaysi gapda (으)면서 oʻrniga 고 ishlatilishi kerak?</p>",
        "choices": ["저는 커피를 마시면서 신문을 읽어요",
                    "제가 공부하면서 동생이 텔레비전을 봐요",
                    "지영 씨는 웃으면서 말했어요",
                    "저는 걸으면서 전화해요"],
        "correct": "제가 공부하면서 동생이 텔레비전을 봐요",
        "explanation": "<p>Bu yerda ega ikki xil — men va ukam. (으)면서 buni "
                       "koʻtarmaydi. Toʻgʻrisi: <strong>저는 공부하고 동생은 "
                       "텔레비전을 봐요.</strong></p>",
    },
    {
        "text": "<p><strong>그 식당은 싸면서 맛있어요</strong> nima degani?</p>",
        "choices": ["U oshxona ham arzon, ham mazali",
                    "U oshxona arzon boʻlgani uchun mazali",
                    "Agar oshxona arzon boʻlsa, mazali boʻladi",
                    "U oshxona arzon edi, hozir mazali"],
        "correct": "U oshxona ham arzon, ham mazali",
        "explanation": "<p>Sifatlar bilan (으)면서 vaqtni emas, <strong>ikki "
                       "xususiyatni</strong> birlashtiradi — “ham …, ham …”.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>음악을 듣으면서 공부해요.</strong></p>",
        "choices": ["듣으면서 → 들으면서", "듣으면서 → 듣면서", "공부해요 → 공부하면서",
                    "Xato yoʻq"],
        "correct": "듣으면서 → 들으면서",
        "explanation": "<p>듣다 — ㄷ notoʻgʻri feʼli. (으) unli oldida ㄷ ㄹ ga "
                       "aylanadi: <strong>들으면서</strong>.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>커피를 마셨으면서 이야기했어요.</strong></p>",
        "choices": ["마셨으면서 → 마시면서", "마셨으면서 → 마시고",
                    "이야기했어요 → 이야기해요", "Xato yoʻq"],
        "correct": "마셨으면서 → 마시면서",
        "explanation": "<p>(으)면서 dan oldin zamon qoʻyilmaydi. Oxiridagi "
                       "이야기했어요 butun gapni oʻtmishga oladi: <strong>커피를 "
                       "마시면서 이야기했어요.</strong></p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Ukam televizor koʻrib ovqat yeydi” — qaysi biri toʻgʻri?</p>",
        "choices": ["동생은 텔레비전을 보고 밥을 먹어요",
                    "동생은 텔레비전을 보면서 밥을 먹어요",
                    "동생은 텔레비전을 봐서 밥을 먹어요",
                    "동생은 텔레비전을 보면 밥을 먹어요"],
        "correct": "동생은 텔레비전을 보면서 밥을 먹어요",
        "explanation": "<p>Ikki ish bir vaqtda, ega bitta → <strong>보면서</strong>. "
                       "보 da 받침 yoʻq, shuning uchun 으 kerak emas.</p>",
    },
    {
        "text": "<p>“Men qoʻshiq aytib raqsga tushaman” — qaysi biri toʻgʻri?</p>",
        "choices": ["저는 노래하면서 춤을 춰요", "저는 노래하고 춤을 춰요",
                    "저는 노래해서 춤을 춰요", "저는 노래하면 춤을 춰요"],
        "correct": "저는 노래하면서 춤을 춰요",
        "explanation": "<p>Bitta odam, ikki ish bir vaqtda → "
                       "<strong>노래하면서</strong>. 하 da 받침 yoʻq → 면서.</p>",
    },
]


# =====================================================================
# PK-40 — (으)려고 하다
# =====================================================================

Q_PK40 = [
    # 1–5 tanish
    {
        "text": "<p><strong>(으)려고 하다</strong> nima maʼnoni beradi?</p>",
        "choices": ["…moqchi boʻlmoq (niyat)", "…dan keyin", "…a olmoq",
                    "…ib turib"],
        "correct": "…moqchi boʻlmoq (niyat)",
        "explanation": "<p><strong>(으)려고 하다</strong> koʻngildagi niyatni "
                       "bildiradi: 한국에 가려고 해요 — Koreyaga bormoqchiman.</p>",
    },
    {
        "text": "<p><strong>가다</strong> ning (으)려고 하다 shakli qaysi?</p>",
        "choices": ["가으려고 해요", "가려고 해요", "간려고 해요", "갈려고 해요"],
        "correct": "가려고 해요",
        "explanation": "<p>가 da 받침 yoʻq → 으 kerak emas: "
                       "<strong>가려고 해요</strong>.</p>",
    },
    {
        "text": "<p><strong>먹다</strong> ning (으)려고 하다 shakli qaysi?</p>",
        "choices": ["먹려고 해요", "먹어려고 해요", "먹으려고 해요", "먹는려고 해요"],
        "correct": "먹으려고 해요",
        "explanation": "<p>먹 da 받침 bor → orasiga 으 kiradi: "
                       "<strong>먹으려고 해요</strong>. <s>먹려고</s> — eng koʻp "
                       "uchraydigan xato.</p>",
    },
    {
        "text": "<p>(으)려고 하다 qanday soʻzlar bilan ishlatiladi?</p>",
        "choices": ["Faqat harakat feʼllari bilan", "Faqat sifatlar bilan",
                    "Faqat otlar bilan", "Har qanday soʻz bilan"],
        "correct": "Faqat harakat feʼllari bilan",
        "explanation": "<p>Niyat qilish uchun harakat kerak. <s>예쁘려고 해요</s> "
                       "deyilmaydi — 예쁘다 sifat.</p>",
    },
    {
        "text": "<p><strong>가려고 했어요</strong> nima degani?</p>",
        "choices": ["Bordim", "Bormoqchi edim (lekin bormadim)", "Boraman",
                    "Borgandan keyin"],
        "correct": "Bormoqchi edim (lekin bormadim)",
        "explanation": "<p>하다 oʻtgan zamonga qoʻyilsa, niyat bor edi-yu, amalga "
                       "oshmadi degan maʼno chiqadi: 가려고 했어요. 하지만 "
                       "시간이 없었어요.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 내일 친구를 <strong>______</strong> (만나다) 해요.</p>",
        "choices": ["만나려고", "만나으려고", "만난려고", "만났려고"],
        "correct": "만나려고",
        "explanation": "<p>만나 da 받침 yoʻq → <strong>만나려고 해요</strong> — "
                       "“uchrashmoqchiman”.</p>",
    },
    {
        "text": "<p>Toʻldiring: 주말에 책을 <strong>______</strong> (읽다) 해요.</p>",
        "choices": ["읽려고", "읽어려고", "읽은려고", "읽으려고"],
        "correct": "읽으려고",
        "explanation": "<p>읽 da 받침 bor → <strong>읽으려고 해요</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 김치를 <strong>______</strong> (만들다) 해요.</p>",
        "choices": ["만들려고", "만들으려고", "만드려고", "만든려고"],
        "correct": "만들려고",
        "explanation": "<p>ㄹ oʻzak: 으 qoʻshilmaydi, ㄹ ham tushmaydi — "
                       "<strong>만들려고 해요</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 음악을 <strong>______</strong> (듣다) 해요.</p>",
        "choices": ["듣으려고", "들으려고", "듣려고", "들려고"],
        "correct": "들으려고",
        "explanation": "<p>듣다 — ㄷ notoʻgʻri feʼli, (으) unli oldida ㄷ → ㄹ: "
                       "<strong>들으려고 해요</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 선물을 <strong>______</strong> (사다) 시장에 "
                "갔어요.</p>",
        "choices": ["사려고", "사으려고", "산려고", "샀려고"],
        "correct": "사려고",
        "explanation": "<p>하다siz <strong>(으)려고</strong> — maqsad bogʻlovchisi: "
                       "“sovgʻa sotib olish uchun bozorga bordim”.</p>",
    },
    {
        "text": "<p>Toʻldiring: 어제 공부<strong>______</strong>. 하지만 너무 "
                "피곤해서 잤어요.</p>",
        "choices": ["하려고 해요", "했으려고 해요", "하려고 했어요", "하려고 할 거예요"],
        "correct": "하려고 했어요",
        "explanation": "<p>“Dars qilmoqchi edim” — zamon <strong>하다</strong> ga "
                       "qoʻyiladi: 하려고 <strong>했어요</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 버스가 <strong>______</strong> (출발하다) 해요.</p>",
        "choices": ["출발하려고", "출발하으려고", "출발한려고", "출발했려고"],
        "correct": "출발하려고",
        "explanation": "<p>버스가 출발하려고 해요 — “avtobus joʻnay deb turibdi”. "
                       "Jonsiz narsa bilan (으)려고 하다 yaqin kelajakni "
                       "bildiradi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>“Ertaga imtihonim bor — qatʼiy dars qilaman” — qaysi biri "
                "mosroq?</p>",
        "choices": ["공부하려고 해요", "공부할 거예요", "공부하면서 해요",
                    "공부한 후에 해요"],
        "correct": "공부할 거예요",
        "explanation": "<p><strong>(으)ㄹ 거예요</strong> — qaror qilingan reja. "
                       "공부하려고 해요 desangiz, hali qatʼiy boʻlmagan niyat "
                       "maʼnosi chiqadi.</p>",
    },
    {
        "text": "<p>(으)ㄹ 거예요 va (으)려고 하다 orasidagi asosiy farq nima?</p>",
        "choices": ["Birinchisi rasmiy, ikkinchisi norasmiy",
                    "Birinchisi qaror qilingan reja, ikkinchisi hali niyat",
                    "Birinchisi oʻtgan zamon, ikkinchisi kelasi zamon",
                    "Farqi yoʻq"],
        "correct": "Birinchisi qaror qilingan reja, ikkinchisi hali niyat",
        "explanation": "<p>Oʻzbekcha koʻprik: (으)ㄹ 거예요 ≈ “boraman”, "
                       "(으)려고 하다 ≈ “bor<strong>moqchi</strong>man”. "
                       "“-moqchi” desangiz — deyarli har doim (으)려고 하다.</p>",
    },
    {
        "text": "<p><strong>한국에 가려고 한국어를 배워요</strong> nima degani?</p>",
        "choices": ["Koreyaga borish uchun koreys tilini oʻrganaman",
                    "Koreyaga borgandan keyin koreys tilini oʻrganaman",
                    "Koreyaga borib koreys tilini oʻrganaman",
                    "Agar Koreyaga borsam, koreys tilini oʻrganaman"],
        "correct": "Koreyaga borish uchun koreys tilini oʻrganaman",
        "explanation": "<p>하다siz <strong>(으)려고</strong> maqsad bildiradi: "
                       "maqsad birinchi qismda, unga erishish yoʻli ikkinchisida.</p>",
    },
    {
        "text": "<p>(으)려고 dan keyin nima <em>kelmaydi</em>?</p>",
        "choices": ["Buyruq", "Oʻtgan zamon", "Inkor", "Soʻroq"],
        "correct": "Buyruq",
        "explanation": "<p><s>사진을 찍으려고 카메라를 사세요.</s> — bunday "
                       "deyilmaydi. Bu 아/어서 (PK-35) dagi taqiqning aynan oʻzi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>밥을 먹려고 해요.</strong></p>",
        "choices": ["먹려고 → 먹으려고", "먹려고 → 먹어려고", "해요 → 했어요",
                    "Xato yoʻq"],
        "correct": "먹려고 → 먹으려고",
        "explanation": "<p>먹 da 받침 bor, shuning uchun 으 tushib qolmasligi "
                       "kerak: <strong>먹으려고 해요</strong>.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>어제 갔으려고 해요.</strong></p>",
        "choices": ["갔으려고 해요 → 가려고 했어요", "갔으려고 해요 → 갔으려고 했어요",
                    "어제 → 내일", "갔으려고 해요 → 가으려고 해요"],
        "correct": "갔으려고 해요 → 가려고 했어요",
        "explanation": "<p>Zamon 려고 ga emas, <strong>하다</strong> ga qoʻyiladi: "
                       "어제 가려고 했어요 — “kecha bormoqchi edim”.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Dam olish kunlari koreys tilini oʻrganmoqchiman” — qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["주말에 한국어를 배우려고 해요",
                    "주말에 한국어를 배울려고 해요",
                    "주말에 한국어를 배우으려고 해요",
                    "주말에 한국어를 배웠으려고 해요"],
        "correct": "주말에 한국어를 배우려고 해요",
        "explanation": "<p>배우 da 받침 yoʻq → <strong>배우려고 해요</strong>.</p>",
    },
    {
        "text": "<p>“Kecha kitob oʻqimoqchi edim, lekin vaqtim boʻlmadi” — qaysi "
                "biri toʻgʻri?</p>",
        "choices": ["어제 책을 읽으려고 해요. 하지만 시간이 없었어요",
                    "어제 책을 읽었으려고 해요. 하지만 시간이 없었어요",
                    "어제 책을 읽으려고 했어요. 하지만 시간이 없었어요",
                    "어제 책을 읽려고 했어요. 하지만 시간이 없었어요"],
        "correct": "어제 책을 읽으려고 했어요. 하지만 시간이 없었어요",
        "explanation": "<p>읽 da 받침 bor → 으려고; zamon esa 하다 da → 했어요. "
                       "Ikkala qoida bitta gapda.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-38 Mashq: 기 전에 / (으)ㄴ 후에 — oldin va keyin",
        "description": "20 savol — 기 전에 ning oson tomoni, (으)ㄴ 후에 ning 받침 "
                       "ayrisi, notoʻgʻri feʼllar va zamon qoidasi.",
        "tutorial":    "PK-38:",
        "level":       "medium",
        "questions":   Q_PK38,
    },
    {
        "title":       "PK-39 Mashq: (으)면서 — bir vaqtda ikki ish",
        "description": "20 savol — 받침 ayrisi, bir xil ega sharti, 고 bilan farqi "
                       "va “ham …, ham …” maʼnosi.",
        "tutorial":    "PK-39:",
        "level":       "medium",
        "questions":   Q_PK39,
    },
    {
        "title":       "PK-40 Mashq: (으)려고 하다 — niyat va reja",
        "description": "20 savol — yasalishi, (으)ㄹ 거예요 bilan farqi, "
                       "…려고 했어요 va maqsad bogʻlovchisi.",
        "tutorial":    "PK-40:",
        "level":       "medium",
        "questions":   Q_PK40,
    },
]
