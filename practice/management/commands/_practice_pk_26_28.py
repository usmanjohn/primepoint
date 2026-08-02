# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-26 … PK-28.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_26_28.py --master=prime \\
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
# PK-26 — Soʻroq soʻzlari
# =====================================================================

Q_PK26 = [
    # 1–5 tanish
    {
        "text": "<p><strong>언제</strong> nima degani?</p>",
        "choices": ["qachon", "qayer", "nega", "qanday"],
        "correct": "qachon",
        "explanation": "<p><strong>언제</strong> — qachon. 어디 — qayer, 왜 — nega, "
                       "어떻게 — qanday.</p>",
    },
    {
        "text": "<p><strong>어떻게</strong> nima degani?</p>",
        "choices": ["qanday", "qachon", "kim", "nechta"],
        "correct": "qanday",
        "explanation": "<p><strong>어떻게</strong> — qanday, qay tarzda: "
                       "어떻게 공부해요?</p>",
    },
    {
        "text": "<p>Koreys soʻroq soʻzi gapda qayerda turadi?</p>",
        "choices": ["Javob turadigan joyda", "Gap boshida",
                    "Gap oxirida", "Kesimdan keyin"],
        "correct": "Javob turadigan joyda",
        "explanation": "<p>Soʻroq soʻzi <strong>koʻchmaydi</strong>: 저는 학교에 가요 → "
                       "저는 <b>어디에</b> 가요? Oʻzbekchada ham shunday.</p>",
    },
    {
        "text": "<p><strong>누구 + 가</strong> qanday boʻladi?</p>",
        "choices": ["누가", "누구가", "누구이", "누구를"],
        "correct": "누가",
        "explanation": "<p><strong>누가</strong> — majburiy qisqarish. <s>누구가</s> "
                       "yozilmaydi.</p>",
    },
    {
        "text": "<p><strong>뭐</strong> va <strong>무엇</strong> farqi nima?</p>",
        "choices": ["뭐 — ogʻzaki, 무엇 — yozma", "뭐 — yozma, 무엇 — ogʻzaki",
                    "뭐 — savol, 무엇 — javob", "Farqi yoʻq"],
        "correct": "뭐 — ogʻzaki, 무엇 — yozma",
        "explanation": "<p>Kundalik nutqda deyarli har doim <strong>뭐</strong>, rasmiy "
                       "matnda esa <strong>무엇</strong>: 무엇을 합니까?</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ 왔어요?</strong> "
                "(“Kim keldi?”)</p>",
        "choices": ["누가", "누구가", "누구를", "누구의"],
        "correct": "누가",
        "explanation": "<p>Ega vazifasida <strong>누가</strong> — 누구 va 가 qoʻshilib "
                       "qisqargan.</p>",
    },
    {
        "text": "<p>“Kimni uchratasiz?” ni koreyschaga oʻgiring.</p>",
        "choices": ["누구를 만나요?", "누가 만나요?", "누구의 만나요?", "누구에 만나요?"],
        "correct": "누구를 만나요?",
        "explanation": "<p>“Kim<b>ni</b>” — toʻldiruvchi, shuning uchun "
                       "<strong>누구를</strong>. 누가 esa ega boʻlardi (“kim "
                       "uchratadi?”).</p>",
    },
    {
        "text": "<p>“Qayerda oʻqiysiz?” ni koreyschaga oʻgiring.</p>",
        "choices": ["어디에서 공부해요?", "어디에 공부해요?",
                    "어디 공부해요에서?", "어디가 공부해요?"],
        "correct": "어디에서 공부해요?",
        "explanation": "<p>공부하다 — harakat feʼli, shuning uchun joy "
                       "<strong>에서</strong> oladi (PK-14).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ 안 가요?</strong> "
                "(“Nega bormaysiz?”)</p>",
        "choices": ["왜", "언제", "어떻게", "누가"],
        "correct": "왜",
        "explanation": "<p><strong>왜</strong> — nega. Sabab soʻraydi.</p>",
    },
    {
        "text": "<p>“Bu qancha?” ni koreyschaga oʻgiring.</p>",
        "choices": ["이것은 얼마예요?", "이것은 몇이에요?",
                    "이것은 무슨이에요?", "이것은 어느예요?"],
        "correct": "이것은 얼마예요?",
        "explanation": "<p><strong>얼마</strong> — narx soʻraydi. 몇 esa birlik bilan "
                       "keladi (몇 개, 몇 명).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ 나라 사람이에요?</strong> "
                "(“Qaysi mamlakatdansiz?”)</p>",
        "choices": ["어느", "무슨", "얼마", "언제"],
        "correct": "어느",
        "explanation": "<p><strong>어느</strong> — maʼlum roʻyxatdan tanlashni soʻraydi "
                       "(“qaysi biri”). 무슨 esa turini soʻraydi (“qanaqa”).</p>",
    },
    {
        "text": "<p>Ogʻzaki nutqda “저는 뭐를 먹어요?” qanday qisqaradi?</p>",
        "choices": ["저는 뭐 먹어요?", "저는 뭐를 먹어?",
                    "뭐 저는 먹어요?", "저는 먹어요 뭐?"],
        "correct": "저는 뭐 먹어요?",
        "explanation": "<p>Kundalik nutqda soʻroq soʻzidan keyingi qoʻshimcha koʻpincha "
                       "<strong>tushiriladi</strong>: 뭐 해요?, 어디 가요?</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Koreys va ingliz soʻroq gapi qanday farq qiladi?</p>",
        "choices": ["Koreysda soʻz koʻchmaydi, ingliz tilida gap boshiga chiqadi",
                    "Koreysda gap boshiga chiqadi, ingliz tilida koʻchmaydi",
                    "Ikkalasida ham koʻchadi",
                    "Ikkalasida ham koʻchmaydi"],
        "correct": "Koreysda soʻz koʻchmaydi, ingliz tilida gap boshiga chiqadi",
        "explanation": "<p>Ingliz tilida <em>What do you eat?</em> — <em>what</em> oldinga "
                       "chiqib yordamchi feʼl qoʻshiladi. Koreys va oʻzbek tilida esa "
                       "soʻz <strong>oʻz oʻrnida</strong> qoladi.</p>",
    },
    {
        "text": "<p><strong>무슨</strong> va <strong>어느</strong> farqi nima?</p>",
        "choices": ["무슨 — turini, 어느 — roʻyxatdan tanlashni soʻraydi",
                    "무슨 — tanlashni, 어느 — turini soʻraydi",
                    "Farqi yoʻq",
                    "무슨 — odamlar, 어느 — narsalar uchun"],
        "correct": "무슨 — turini, 어느 — roʻyxatdan tanlashni soʻraydi",
        "explanation": "<p>“<em>Qanaqa</em> kitob?” → <strong>무슨 책</strong>. "
                       "“<em>Qaysi</em> mamlakat?” → <strong>어느 나라</strong>.</p>",
    },
    {
        "text": "<p>Qaysi juftlik <em>notoʻgʻri</em>?</p>",
        "choices": ["누구가 왔어요?", "누가 왔어요?", "누구를 만나요?", "누구의 책이에요?"],
        "correct": "누구가 왔어요?",
        "explanation": "<p><strong>누구 + 가 = 누가</strong> — qisqarish majburiy. Qolgan "
                       "qoʻshimchalar bilan esa 누구 oʻz shaklida qoladi.</p>",
    },
    {
        "text": "<p><strong>몇</strong> va <strong>얼마</strong> farqi nima?</p>",
        "choices": ["몇 birlik bilan keladi, 얼마 narx soʻraydi",
                    "몇 narx, 얼마 birlik uchun",
                    "Farqi yoʻq",
                    "몇 faqat odamlar uchun"],
        "correct": "몇 birlik bilan keladi, 얼마 narx soʻraydi",
        "explanation": "<p><strong>몇 개</strong>, <strong>몇 명</strong>, "
                       "<strong>몇 시</strong> — birlik bilan. <strong>얼마</strong> esa "
                       "yolgʻiz: 얼마예요?</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["뭐 저는 먹어요?", "저는 뭐 먹어요?",
                    "저는 어디에 가요?", "누가 왔어요?"],
        "correct": "뭐 저는 먹어요?",
        "explanation": "<p>Soʻroq soʻzi ingliz tilidagidek oldinga koʻchmaydi. Toʻgʻrisi: "
                       "<strong>저는 뭐 먹어요?</strong></p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["어디에서 공부해요?", "어디에 공부해요?",
                    "어디를 공부해요?", "어디가 공부해요?"],
        "correct": "어디에서 공부해요?",
        "explanation": "<p>Harakat feʼli bilan joy <strong>에서</strong> oladi. "
                       "어디에 boʻlsa yoʻnalish (“qayerga”) boʻlardi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: ___ 만나요?<br>나: 오후 세 시에 만나요.</strong></p>",
        "choices": ["언제", "어디에서", "누구를", "어떻게"],
        "correct": "언제",
        "explanation": "<p>Javob <em>vaqt</em> beryapti (오후 세 시), demak savol "
                       "<strong>언제</strong> — “qachon”.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: ___ 한국어를 공부해요?<br>나: 매일 책을 읽어요.</strong></p>",
        "choices": ["어떻게", "언제", "누가", "얼마"],
        "correct": "어떻게",
        "explanation": "<p>Javob <em>usulni</em> aytyapti (“har kuni kitob oʻqiyman”), "
                       "demak savol <strong>어떻게</strong> — “qanday”.</p>",
    },
]


# =====================================================================
# PK-27 — (으)ㄹ 거예요
# =====================================================================

Q_PK27 = [
    # 1–5 tanish
    {
        "text": "<p>받침 <strong>yoʻq</strong> oʻzakka qaysi shakl qoʻshiladi?</p>",
        "choices": ["ㄹ 거예요", "을 거예요", "고 싶어요", "습니다"],
        "correct": "ㄹ 거예요",
        "explanation": "<p>받침 yoʻq → <strong>ㄹ 거예요</strong>, va ㄹ oʻzakning tagiga "
                       "tushadi: 가 + ㄹ = <b>갈</b>.</p>",
    },
    {
        "text": "<p>받침 <strong>bor</strong> oʻzakka qaysi shakl qoʻshiladi?</p>",
        "choices": ["을 거예요", "ㄹ 거예요", "아 거예요", "이 거예요"],
        "correct": "을 거예요",
        "explanation": "<p>받침 bor → <strong>을 거예요</strong>: 먹 → "
                       "<b>먹을 거예요</b>.</p>",
    },
    {
        "text": "<p><strong>갈 거예요</strong> qanday oʻqiladi?</p>",
        "choices": ["[갈 꺼예요]", "[갈 거예요]", "[가 거예요]", "[갈 커예요]"],
        "correct": "[갈 꺼예요]",
        "explanation": "<p>경음화: ㄹ dan keyin ㄱ qattiqlashadi. Yozilishi hech qachon "
                       "oʻzgarmaydi — har doim <strong>거예요</strong>.</p>",
    },
    {
        "text": "<p>(으)ㄹ 거예요 ning ikki maʼnosi qaysi?</p>",
        "choices": ["Reja va taxmin", "Xohish va reja",
                    "Oʻtgan va hozirgi", "Buyruq va taklif"],
        "correct": "Reja va taxmin",
        "explanation": "<p>Oʻzingiz haqingizda — <strong>reja</strong>; boshqa odam yoki "
                       "ob-havo haqida — <strong>taxmin</strong>.</p>",
    },
    {
        "text": "<p>(으)ㄹ 거예요 ning rasmiy shakli qaysi?</p>",
        "choices": ["(으)ㄹ 겁니다", "(으)ㄹ 거요", "(으)ㄹ 습니다", "(으)ㄹ 이에요"],
        "correct": "(으)ㄹ 겁니다",
        "explanation": "<p>합니다체 da <strong>(으)ㄹ 겁니다</strong>: 갈 겁니다, "
                       "먹을 겁니다.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p><strong>먹다</strong> ni kelasi zamonga oʻgiring.</p>",
        "choices": ["먹을 거예요", "먹ㄹ 거예요", "머글 거예요", "먹 거예요"],
        "correct": "먹을 거예요",
        "explanation": "<p>Oʻzak 먹 받침li (ㄱ) → <strong>을 거예요</strong>. Oʻqilishi "
                       "[머글 꺼예요], lekin yozilishi 먹을 거예요.</p>",
    },
    {
        "text": "<p><strong>배우다</strong> ni kelasi zamonga oʻgiring.</p>",
        "choices": ["배울 거예요", "배우을 거예요", "배워 거예요", "배우 거예요"],
        "correct": "배울 거예요",
        "explanation": "<p>Oʻzak 배우 받침siz → ㄹ oxirgi blok tagiga tushadi: 우 + ㄹ = "
                       "<strong>울</strong>.</p>",
    },
    {
        "text": "<p><strong>살다</strong> ni kelasi zamonga oʻgiring.</p>",
        "choices": ["살 거예요", "살을 거예요", "삽 거예요", "사ㄹ 거예요"],
        "correct": "살 거예요",
        "explanation": "<p>Oʻzak allaqachon ㄹ bilan tugaydi, shuning uchun yangi ㄹ "
                       "<strong>qoʻshilmaydi</strong>.</p>",
    },
    {
        "text": "<p>“Ertaga nima qilasiz?” ni koreyschaga oʻgiring.</p>",
        "choices": ["내일 뭐 할 거예요?", "내일에 뭐 할 거예요?",
                    "내일 뭐 하을 거예요?", "뭐 내일 할 거예요?"],
        "correct": "내일 뭐 할 거예요?",
        "explanation": "<p><strong>내일</strong> 에 olmaydi (PK-14), <strong>뭐</strong> "
                       "oʻz oʻrnida (PK-26), va 하다 → <strong>할 거예요</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>내일 비가 ___.</strong> "
                "(“yomgʻir yogʻsa kerak”)</p>",
        "choices": ["올 거예요", "오을 거예요", "와 거예요", "옵 거예요"],
        "correct": "올 거예요",
        "explanation": "<p>오다 oʻzagi 오 받침siz → ㄹ tagiga tushadi: <strong>올 거예요</strong>. "
                       "Ob-havo haqida — bu <em>taxmin</em>.</p>",
    },
    {
        "text": "<p>“갈 거예요” ni inkor qiling.</p>",
        "choices": ["안 갈 거예요", "갈 안 거예요", "갈 거예요 안", "안 가을 거예요"],
        "correct": "안 갈 거예요",
        "explanation": "<p><strong>안</strong> feʼl qismining oldiga tushadi: "
                       "안 갈 거예요. Uzun shakli — <em>가지 않을 거예요</em>.</p>",
    },
    {
        "text": "<p>“Doʻstimni uchrataman” ni koreyschaga oʻgiring.</p>",
        "choices": ["친구를 만날 거예요.", "친구를 만나을 거예요.",
                    "친구가 만날 거예요.", "친구를 만나 거예요."],
        "correct": "친구를 만날 거예요.",
        "explanation": "<p>만나다 oʻzagi 만나 받침siz → 나 + ㄹ = <strong>만날</strong>. "
                       "Toʻldiruvchi <strong>를</strong> oladi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki gap nega boshqacha tarjima qilinadi?<br>"
                "(a) 저는 집에 있을 거예요. (b) 자수르 씨는 집에 있을 거예요.</p>",
        "choices": ["(a) reja, (b) taxmin — ega hal qiladi",
                    "(a) taxmin, (b) reja",
                    "(a) hozirgi, (b) kelasi zamon",
                    "Farqi yoʻq"],
        "correct": "(a) reja, (b) taxmin — ega hal qiladi",
        "explanation": "<p>Oʻzingiz haqingizda — reja (“uyda boʻlaman”). Boshqa odam "
                       "haqida — taxmin (“uyda boʻlsa kerak”), chunki uning niyatini "
                       "bilolmaysiz.</p>",
    },
    {
        "text": "<p><strong>가요</strong> va <strong>갈 거예요</strong> farqi nima?</p>",
        "choices": ["갈 거예요 aniqroq niyat bildiradi",
                    "가요 faqat hozirgi zamon",
                    "갈 거예요 oʻtgan zamon",
                    "Farqi yoʻq"],
        "correct": "갈 거예요 aniqroq niyat bildiradi",
        "explanation": "<p>가요 ≈ “boraman” (umumiy, kontekstga bogʻliq). "
                       "갈 거예요 ≈ “bormoqchiman” — rejalashtirilgan niyat. Oʻzbekchada "
                       "ham shu farq bor.</p>",
    },
    {
        "text": "<p>Nega 살다 → 살 거예요, 살을 거예요 emas?</p>",
        "choices": ["Oʻzak allaqachon ㄹ bilan tugaydi",
                    "Chunki 살다 sifat",
                    "Chunki bu taxmin",
                    "Chunki 살 받침siz"],
        "correct": "Oʻzak allaqachon ㄹ bilan tugaydi",
        "explanation": "<p>ㄹ oʻzaklarda mavjud ㄹ ning oʻzi ishlatiladi — yangisi "
                       "qoʻshilmaydi. Solishtiring: 먹 → 먹을 거예요.</p>",
    },
    {
        "text": "<p>Yozilishi va oʻqilishi qanday farq qiladi?</p>",
        "choices": ["Yoziladi 거예요, oʻqiladi [꺼예요]",
                    "Yoziladi 꺼예요, oʻqiladi [거예요]",
                    "Ikkalasi bir xil",
                    "Yoziladi 거에요, oʻqiladi [거예요]"],
        "correct": "Yoziladi 거예요, oʻqiladi [꺼예요]",
        "explanation": "<p>경음화 faqat talaffuzga taʼsir qiladi. Imlo hech qachon "
                       "oʻzgarmaydi — bu PK-8 dagi umumiy qoida.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["저는 가을 거예요.", "저는 갈 거예요.",
                    "저는 먹을 거예요.", "저는 살 거예요."],
        "correct": "저는 가을 거예요.",
        "explanation": "<p>가 받침siz → ㄹ tagiga tushadi: <strong>갈 거예요</strong>. "
                       "<s>가을</s> notoʻgʻri.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["내일 책을 읽을 거예요.", "내일에 책을 읽을 거예요.",
                    "내일 책이 읽을 거예요.", "내일 책을 읽ㄹ 거예요."],
        "correct": "내일 책을 읽을 거예요.",
        "explanation": "<p>내일 에 olmaydi, 책 toʻldiruvchi (을), va 읽 받침li → "
                       "<strong>읽을 거예요</strong>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Bu gapni kelasi zamonga oʻgiring: <strong>저는 한국어를 "
                "공부해요.</strong></p>",
        "choices": ["저는 한국어를 공부할 거예요.", "저는 한국어를 공부을 거예요.",
                    "저는 한국어를 공부했을 거예요.", "저는 한국어를 공부하 거예요."],
        "correct": "저는 한국어를 공부할 거예요.",
        "explanation": "<p>공부하 oʻzagi 받침siz → 하 + ㄹ = <strong>할</strong> → "
                       "공부할 거예요.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 주말에 뭐 할 거예요?<br>나: ___</strong></p>",
        "choices": ["집에서 책을 읽을 거예요.", "집에서 책을 읽었어요.",
                    "집에서 책을 읽을 거예요만.", "집에 책을 읽을 거예요."],
        "correct": "집에서 책을 읽을 거예요.",
        "explanation": "<p>Savol kelasi zamonda — javob ham. 읽다 harakat feʼli, shuning "
                       "uchun joy <strong>에서</strong> (PK-14).</p>",
    },
]


# =====================================================================
# PK-28 — 고 싶다
# =====================================================================

Q_PK28 = [
    # 1–5 tanish
    {
        "text": "<p><strong>고 싶어요</strong> nima maʼnoni beradi?</p>",
        "choices": ["…gim keladi", "…aman (kelasi)", "…dim (oʻtgan)", "…may man"],
        "correct": "…gim keladi",
        "explanation": "<p><strong>고 싶어요</strong> — xohish: 가고 싶어요 “borgim "
                       "keladi”. Reja uchun esa 갈 거예요.</p>",
    },
    {
        "text": "<p>고 oʻzakka qanday qoʻshiladi?</p>",
        "choices": ["Toʻgʻridan-toʻgʻri, 받침 ayrisi yoʻq", "받침 bor boʻlsa 으고",
                    "Faqat unli oʻzaklarga", "Oʻzak oxiri oʻzgaradi"],
        "correct": "Toʻgʻridan-toʻgʻri, 받침 ayrisi yoʻq",
        "explanation": "<p>Bu darsda 받침 muammosi <strong>yoʻq</strong>: 먹 + 고 싶어요, "
                       "가 + 고 싶어요.</p>",
    },
    {
        "text": "<p>Uchinchi shaxs uchun qaysi shakl ishlatiladi?</p>",
        "choices": ["고 싶어하다", "고 싶다", "고 있다", "고 싶어요"],
        "correct": "고 싶어하다",
        "explanation": "<p><strong>고 싶어하다</strong> — boshqa odam haqida: "
                       "자수르 씨는 가고 싶어해요.</p>",
    },
    {
        "text": "<p>고 싶다 da nima tuslanadi?</p>",
        "choices": ["싶다", "asosiy feʼl", "고", "Ikkalasi ham"],
        "correct": "싶다",
        "explanation": "<p>Tuslanish har doim <strong>싶다</strong> da: 가고 "
                       "<b>싶었어요</b>, 가고 <b>싶지 않아요</b>. <s>갔고 싶어요</s> "
                       "notoʻgʻri.</p>",
    },
    {
        "text": "<p>Nega 싶다 → 싶어요 boʻladi?</p>",
        "choices": ["Oxirgi unli ㅣ — ㅏ ham, ㅗ ham emas",
                    "Chunki 싶 받침li",
                    "Chunki 싶다 feʼl",
                    "Bu istisno"],
        "correct": "Oxirgi unli ㅣ — ㅏ ham, ㅗ ham emas",
        "explanation": "<p>PK-18 qoidasi: oxirgi unli ㅏ/ㅗ boʻlmasa <strong>어요</strong>. "
                       "싶 ning unlisi ㅣ → 싶어요.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p><strong>먹다</strong> dan “yegim keladi” yasang.</p>",
        "choices": ["먹고 싶어요", "먹을 싶어요", "먹어 싶어요", "먹고 싶어해요"],
        "correct": "먹고 싶어요",
        "explanation": "<p>Oʻzak 먹 + <strong>고 싶어요</strong>. 받침 ayrisi yoʻq.</p>",
    },
    {
        "text": "<p>“Jasur Koreyaga bormoqchi” ni koreyschaga oʻgiring.</p>",
        "choices": ["자수르 씨는 한국에 가고 싶어해요.",
                    "자수르 씨는 한국에 가고 싶어요.",
                    "자수르 씨는 한국에 갈 싶어해요.",
                    "자수르 씨는 한국에서 가고 싶어해요."],
        "correct": "자수르 씨는 한국에 가고 싶어해요.",
        "explanation": "<p>Uchinchi shaxs → <strong>고 싶어해요</strong>. Va 가다 yoʻnalish "
                       "bildirgani uchun 한국<b>에</b>.</p>",
    },
    {
        "text": "<p>“가고 싶어요” ni oʻtgan zamonga oʻgiring.</p>",
        "choices": ["가고 싶었어요", "갔고 싶어요", "가고 싶어했어요", "갔고 싶었어요"],
        "correct": "가고 싶었어요",
        "explanation": "<p>Tuslanish <strong>싶다</strong> da: 싶어요 → "
                       "<strong>싶었어요</strong>.</p>",
    },
    {
        "text": "<p>“가고 싶어요” ni inkor qiling.</p>",
        "choices": ["가고 싶지 않아요", "안 가고 싶어요만",
                    "가지 않고 싶어요", "가고 안 싶어요"],
        "correct": "가고 싶지 않아요",
        "explanation": "<p>Inkor ham <strong>싶다</strong> ga qoʻshiladi: "
                       "가고 <b>싶지 않아요</b> — “borgim kelmaydi”.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>물___ 마시고 싶어요.</strong></p>",
        "choices": ["을", "이", "에", "도"],
        "correct": "을",
        "explanation": "<p>Toʻldiruvchi <strong>을/를</strong> oladi. 물이 마시고 싶어요 ham "
                       "toʻgʻri, lekin boshlangʻich darajada <strong>을/를</strong> ni "
                       "ishlating.</p>",
    },
    {
        "text": "<p>“공부하다” dan “oʻqigim keladi” yasang.</p>",
        "choices": ["공부하고 싶어요", "공부 고 싶어요",
                    "공부해고 싶어요", "공부할 싶어요"],
        "correct": "공부하고 싶어요",
        "explanation": "<p>Oʻzak <strong>공부하</strong> butunligicha olinadi, keyin "
                       "고 싶어요 qoʻshiladi.</p>",
    },
    {
        "text": "<p>“Nima yegingiz keladi?” ni koreyschaga oʻgiring.</p>",
        "choices": ["뭐 먹고 싶어요?", "뭐 먹고 싶어해요?",
                    "뭐 먹을 거예요 싶어요?", "뭐 먹고 싶다?"],
        "correct": "뭐 먹고 싶어요?",
        "explanation": "<p>Savol <em>suhbatdoshga</em> berilyapti, ya'ni “siz” — demak "
                       "<strong>고 싶어요</strong>, 고 싶어해요 emas.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Nega uchinchi shaxs uchun boshqa shakl kerak?</p>",
        "choices": ["Boshqa odamning ichki istagini bilib boʻlmaydi",
                    "Chunki 고 싶다 juda qisqa",
                    "Chunki uchinchi shaxs hurmatli",
                    "Chunki 싶다 sifat"],
        "correct": "Boshqa odamning ichki istagini bilib boʻlmaydi",
        "explanation": "<p>Siz faqat <em>tashqi belgilarini</em> koʻrasiz. Koreys tili "
                       "buni grammatikada ajratadi: 싶다 (mening istagim) va 싶어하다 "
                       "(uning koʻrinib turgan istagi).</p>",
    },
    {
        "text": "<p><strong>갈 거예요</strong> va <strong>가고 싶어요</strong> farqi "
                "nima?</p>",
        "choices": ["Birinchisi reja, ikkinchisi xohish",
                    "Birinchisi xohish, ikkinchisi reja",
                    "Birinchisi oʻtgan zamon",
                    "Farqi yoʻq"],
        "correct": "Birinchisi reja, ikkinchisi xohish",
        "explanation": "<p><strong>갈 거예요</strong> — qaror qilingan (“boraman”). "
                       "<strong>가고 싶어요</strong> — hali istak (“borgim keladi”). "
                       "Oʻzbekchada ham shu farq bor.</p>",
    },
    {
        "text": "<p>Qaysi gap <em>notoʻgʻri</em>?</p>",
        "choices": ["갔고 싶어요", "가고 싶었어요", "가고 싶어요", "가고 싶지 않아요"],
        "correct": "갔고 싶어요",
        "explanation": "<p>Tuslanish asosiy feʼlda emas, <strong>싶다</strong> da "
                       "boʻladi. Toʻgʻrisi: <em>가고 싶었어요</em>.</p>",
    },
    {
        "text": "<p>Oʻzbekchadagi qaysi ibora 고 싶어요 ga eng yaqin?</p>",
        "choices": ["borgim keladi", "boraman", "borgan edim", "bora olaman"],
        "correct": "borgim keladi",
        "explanation": "<p><strong>가고 싶어요</strong> — his-tuygʻu, ichki istak. "
                       "“Boraman” esa 가요 yoki 갈 거예요 ga toʻgʻri keladi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["딜노자 씨는 가고 싶어요.", "딜노자 씨는 가고 싶어해요.",
                    "저는 가고 싶어요.", "뭐 먹고 싶어요?"],
        "correct": "딜노자 씨는 가고 싶어요.",
        "explanation": "<p>Uchinchi shaxs haqida gap ketyapti → <strong>고 "
                       "싶어해요</strong>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["한국어를 배우고 싶어요.", "한국어를 배울 싶어요.",
                    "한국어를 배웠고 싶어요.", "한국어가 배우고 싶어해요."],
        "correct": "한국어를 배우고 싶어요.",
        "explanation": "<p>Oʻzak 배우 + <strong>고 싶어요</strong>, toʻldiruvchi "
                       "<strong>를</strong>, va gapiruvchi oʻzi haqida — 싶어요.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 어디에 가고 싶어요?<br>나: ___</strong></p>",
        "choices": ["서울에 가고 싶어요.", "서울에서 가고 싶어요.",
                    "서울에 가고 싶어해요.", "서울을 가고 싶어요."],
        "correct": "서울에 가고 싶어요.",
        "explanation": "<p>가다 yoʻnalish bildiradi → <strong>에</strong>, va javob "
                       "beruvchi <em>oʻzi</em> haqida gapiryapti → 싶어요.</p>",
    },
    {
        "text": "<p>Bu gapni uchinchi shaxsga oʻgiring: <strong>저는 여행을 하고 "
                "싶어요.</strong></p>",
        "choices": ["딜노자 씨는 여행을 하고 싶어해요.",
                    "딜노자 씨는 여행을 하고 싶어요.",
                    "딜노자 씨는 여행을 할 싶어해요.",
                    "딜노자 씨는 여행이 하고 싶어해요."],
        "correct": "딜노자 씨는 여행을 하고 싶어해요.",
        "explanation": "<p>Faqat oxiri oʻzgaradi: <strong>싶어요 → 싶어해요</strong>. "
                       "Toʻldiruvchi va qolgan boʻlaklar oʻz joyida qoladi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-26 Mashq: Soʻroq soʻzlari",
        "description": "20 savol — oltita soʻroq soʻzi, ularning oʻrni va qoʻshimchalari.",
        "tutorial":    "PK-26:",
        "level":       "easy",
        "questions":   Q_PK26,
    },
    {
        "title":       "PK-27 Mashq: (으)ㄹ 거예요 — kelasi zamon",
        "description": "20 savol — 받침 ayrisi, ㄹ oʻzaklar, reja va taxmin farqi.",
        "tutorial":    "PK-27:",
        "level":       "easy",
        "questions":   Q_PK27,
    },
    {
        "title":       "PK-28 Mashq: 고 싶다 — xohish",
        "description": "20 savol — xohish shakli, uchinchi shaxs qoidasi, reja bilan farqi.",
        "tutorial":    "PK-28:",
        "level":       "easy",
        "questions":   Q_PK28,
    },
]
