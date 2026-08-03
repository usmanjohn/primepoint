# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-68 … PK-70.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_68_70.py --master=prime \\
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
# PK-68 — (으)ㄴ/는 데다가
# =====================================================================

Q_PK68 = [
    # 1–5 tanish
    {
        "text": "<p><strong>(으)ㄴ/는 데다가</strong> nimani bildiradi?</p>",
        "choices": ["Ikkinchi holat birinchisining ustiga tushadi",
                    "Ikki tomonni qiyoslash",
                    "Sal boʻlmasa sodir boʻlgan ish",
                    "Boshqaning gapini yetkazish"],
        "correct": "Ikkinchi holat birinchisining ustiga tushadi",
        "explanation": "<p>Oʻzbekcha juftligi — “<strong>ustiga ustak</strong>”, "
                       "“…gani <strong>yetmagandek</strong>”.</p>",
    },
    {
        "text": "<p><strong>데</strong> soʻzi nima degani?</p>",
        "choices": ["Vaqt", "Joy, holat", "Sabab", "Ayb"],
        "correct": "Joy, holat",
        "explanation": "<p>Oltinchi <strong>aniqlovchi + ot</strong>: "
                       "것 · 줄 · 뻔 · 테 · 뿐 · 데.</p>",
    },
    {
        "text": "<p>Feʼl bu qolipda qanday shakl oladi?</p>",
        "choices": ["는 데다가", "(으)ㄴ 데다가", "(으)ㄹ 데다가", "인 데다가"],
        "correct": "는 데다가",
        "explanation": "<p>오다 → 오<strong>는</strong> 데다가 — hozirgi "
                       "zamon aniqlovchisi (PK-43).</p>",
    },
    {
        "text": "<p>Sifat bu qolipda qanday shakl oladi?</p>",
        "choices": ["는 데다가", "(으)ㄴ 데다가", "(으)ㄹ 데다가", "게 데다가"],
        "correct": "(으)ㄴ 데다가",
        "explanation": "<p>좁다 → 좁<strong>은</strong> 데다가, 비싸다 → "
                       "비싼 데다가.</p>",
    },
    {
        "text": "<p>Ikkinchi gapda odatda qaysi qoʻshimchalar turadi?</p>",
        "choices": ["도 yoki 까지", "만 yoki 부터", "은/는", "에게"],
        "correct": "도 yoki 까지",
        "explanation": "<p>바람<strong>도</strong> 불어요, 비<strong>까지</strong> "
                       "왔어요 — 까지 ohangni yanada kuchaytiradi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 비가 <strong>______</strong> 데다가 바람도 "
                "세게 불어요. (오다)</p>",
        "choices": ["온", "올", "오는", "오던"],
        "correct": "오는",
        "explanation": "<p>Feʼl, hozirgi zamon → <strong>는 데다가</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 방이 <strong>______</strong> 데다가 창문도 "
                "없어요. (좁다)</p>",
        "choices": ["좁는", "좁은", "좁을", "좁아서"],
        "correct": "좁은",
        "explanation": "<p>좁다 — sifat, 받침 bor → "
                       "<strong>은 데다가</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 그 사람은 <strong>______</strong> 데다가 "
                "아르바이트도 해요. (학생이다)</p>",
        "choices": ["학생이는", "학생인", "학생일", "학생이라"],
        "correct": "학생인",
        "explanation": "<p>Ot + 이다 → <strong>인 데다가</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 어제는 몸이 <strong>______</strong> 데다가 "
                "일도 많아서 힘들었어요. (아프다)</p>",
        "choices": ["아픈", "아프는", "아플", "아파서"],
        "correct": "아픈",
        "explanation": "<p>아프다 — sifat, 받침 yoʻq → "
                       "<strong>ㄴ 데다가</strong>.</p>",
    },
    {
        "text": "<p>“Yoʻl tiqilgani yetmagandek yomgʻir ham yogʻdi, shuning "
                "uchun kechikdim” — qaysi biri toʻgʻri?</p>",
        "choices": ["길이 막히는 데다가 비까지 와서 늦었어요",
                    "길이 막힌 데다가 비까지 와서 늦었어요",
                    "길이 막힐 데다가 비까지 와서 늦었어요",
                    "길이 막히는 반면에 비까지 와서 늦었어요"],
        "correct": "길이 막히는 데다가 비까지 와서 늦었어요",
        "explanation": "<p>막히다 — feʼl → 는 데다가. Ikkala holat ham "
                       "salbiy, va oxirida <strong>natija</strong> "
                       "keladi.</p>",
    },
    {
        "text": "<p>Ogʻzaki nutqda bu qolip qanday qisqaradi?</p>",
        "choices": ["데다", "데가", "다가", "데도"],
        "correct": "데다",
        "explanation": "<p><strong>가</strong> tushadi: 방이 좁은 "
                       "<strong>데다</strong> 창문도 없어요.</p>",
    },
    {
        "text": "<p>Toʻldiring: 그 식당은 음식이 <strong>______</strong> "
                "데다가 값도 싸요. (맛있다)</p>",
        "choices": ["맛있은", "맛있는", "맛있을", "맛있던"],
        "correct": "맛있는",
        "explanation": "<p>맛있다 — 있다 bilan tugagani uchun "
                       "<strong>는</strong> oladi. Ikkala tomon ham "
                       "ijobiy — bu ham toʻgʻri.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Nima uchun <strong>예쁜 데다가 성격이 나빠요</strong> "
                "notoʻgʻri?</p>",
        "choices": ["받침 xato",
                    "Ikkala tomon bir yoʻnalishda boʻlishi kerak — biri "
                    "maqtov, biri ayb",
                    "예쁘다 feʼl",
                    "Zamon xato"],
        "correct": "Ikkala tomon bir yoʻnalishda boʻlishi kerak — biri "
                   "maqtov, biri ayb",
        "explanation": "<p>Qarama-qarshi tomonlar uchun PK-66 dagi "
                       "<strong>반면에</strong> kerak: 예쁜 반면에 성격이 "
                       "나빠요.</p>",
    },
    {
        "text": "<p><strong>뿐만 아니라</strong> va <strong>데다가</strong> "
                "farqi nimada?</p>",
        "choices": ["뿐만 아니라 sanaydi; 데다가 ustiga qoʻyadi va koʻpincha "
                    "natijaga olib keladi",
                    "뿐만 아니라 qiyoslaydi; 데다가 sanaydi",
                    "Ikkalasi bir xil",
                    "데다가 faqat sifat bilan keladi"],
        "correct": "뿐만 아니라 sanaydi; 데다가 ustiga qoʻyadi va koʻpincha "
                   "natijaga olib keladi",
        "explanation": "<p>Koʻp holatda ikkalasi ham toʻgʻri boʻladi — "
                       "farq ohangda: roʻyxat va toʻplanish.</p>",
    },
    {
        "text": "<p>Bu qolipning uchta sharti qaysi?</p>",
        "choices": ["Bir yoʻnalish · bir mavzu · koʻpincha natija",
                    "Oʻtgan zamon · inkor · buyruq",
                    "Bir xil ega · zamon yoʻq · salbiy natija",
                    "Faqat feʼl · faqat sifat · faqat ot"],
        "correct": "Bir yoʻnalish · bir mavzu · koʻpincha natija",
        "explanation": "<p>Uchalasi buzilsa gap gʻalati eshitiladi — "
                       "ayniqsa birinchisi.</p>",
    },
    {
        "text": "<p>Qaysi gapda <strong>데다가</strong> ishlatib "
                "boʻlmaydi?</p>",
        "choices": ["Xona tor, ustiga derazasi ham yoʻq",
                    "Ovqati mazali, ustiga narxi ham arzon",
                    "Chiroyli, lekin xarakteri yomon",
                    "Kasal edim, ustiga ish ham koʻp edi"],
        "correct": "Chiroyli, lekin xarakteri yomon",
        "explanation": "<p>Bu yerda ikki tomon <strong>qarama-qarshi</strong> "
                       "— 반면에 kerak. Qolgan uchtasida ikkala tomon "
                       "bir yoʻnalishda.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>방이 좁는 데다가 창문도 "
                "없어요.</strong></p>",
        "choices": ["좁는 → 좁은", "좁는 → 좁을", "창문도 → 창문이",
                    "Xato yoʻq"],
        "correct": "좁는 → 좁은",
        "explanation": "<p>좁다 — sifat, shuning uchun "
                       "<strong>(으)ㄴ</strong> oladi.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>그 사람은 학생이는 데다가 "
                "아르바이트도 해요.</strong></p>",
        "choices": ["학생이는 → 학생인", "학생이는 → 학생일",
                    "아르바이트도 → 아르바이트를", "Xato yoʻq"],
        "correct": "학생이는 → 학생인",
        "explanation": "<p>Ot + 이다 → <strong>인</strong>.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Xona tor, ustiga derazasi ham yoʻq” — qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["방이 좁는 데다가 창문도 없어요",
                    "방이 좁은 데다가 창문도 없어요",
                    "방이 좁은 반면에 창문도 없어요",
                    "방이 좁을 데다가 창문도 없어요"],
        "correct": "방이 좁은 데다가 창문도 없어요",
        "explanation": "<p>Sifat → (으)ㄴ 데다가, ikkinchi gapda "
                       "<strong>도</strong>, ikkala tomon ham salbiy.</p>",
    },
    {
        "text": "<p><strong>가:</strong> 어제 왜 그렇게 힘들었어요?</p>"
                "<p><strong>나:</strong> ___</p>",
        "choices": ["몸이 아픈 데다가 일도 많았어요",
                    "몸이 아프는 데다가 일도 많았어요",
                    "몸이 아픈 반면에 일도 많았어요",
                    "몸이 아플 데다가 일도 많았어요"],
        "correct": "몸이 아픈 데다가 일도 많았어요",
        "explanation": "<p>Ikki salbiy holat toʻplanib natijaga "
                       "(힘들었어요) olib keldi — aynan 데다가 ning "
                       "oʻrni.</p>",
    },
]


# =====================================================================
# PK-69 — 는 바람에, (으)ㄴ/는 탓에, 느라고
# =====================================================================

Q_PK69 = [
    # 1–5 tanish
    {
        "text": "<p><strong>는 바람에</strong> qanday sababni bildiradi?</p>",
        "choices": ["Rejalashtirilgan sababni",
                    "Kutilmagan xalaqitni",
                    "Ijobiy sababni",
                    "Soʻzlovchining niyatini"],
        "correct": "Kutilmagan xalaqitni",
        "explanation": "<p>바람 — “shamol”. Toʻsatdan bir narsa esib keldi "
                       "va rejani buzdi.</p>",
    },
    {
        "text": "<p><strong>탓</strong> soʻzi nima degani?</p>",
        "choices": ["Ayb, gunoh", "Sharofat", "Shamol", "Imkoniyat"],
        "correct": "Ayb, gunoh",
        "explanation": "<p>Shuning uchun 탓에 shunchaki sabab emas, "
                       "<strong>ayblov</strong> beradi.</p>",
    },
    {
        "text": "<p><strong>느라고</strong> qanday maʼno beradi?</p>",
        "choices": ["…ga ovora boʻlib (bahona)", "…ning sharofati bilan",
                    "…gan sari", "sal boʻlmasa …"],
        "correct": "…ga ovora boʻlib (bahona)",
        "explanation": "<p>숙제하느라고 잠을 못 잤어요 — “uy vazifasiga "
                       "<strong>ovora boʻlib</strong> uxlay olmadim”.</p>",
    },
    {
        "text": "<p><strong>탓에</strong> ning ijobiy jufti qaysi?</p>",
        "choices": ["바람에", "느라고", "덕분에", "때문에"],
        "correct": "덕분에",
        "explanation": "<p>선생님 <strong>덕분에</strong> 합격했어요 — "
                       "“oʻqituvchining <strong>sharofati</strong> "
                       "bilan”.</p>",
    },
    {
        "text": "<p><strong>느라고</strong> ning eng muhim sharti nima?</p>",
        "choices": ["Ikkala gapning egasi bir xil boʻlishi",
                    "Ikkala gapning egasi boshqa boʻlishi",
                    "Natija ijobiy boʻlishi",
                    "Zamon qoʻshimchasi boʻlishi"],
        "correct": "Ikkala gapning egasi bir xil boʻlishi",
        "explanation": "<p>Boshqa odam xalaqit bergan boʻlsa — 느라고 emas, "
                       "<strong>바람에</strong>.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 비가 <strong>______</strong> 바람에 소풍을 "
                "못 갔어요. (오다)</p>",
        "choices": ["온", "오는", "올", "왔는"],
        "correct": "오는",
        "explanation": "<p>바람에 dan oldin faqat <strong>는</strong> — "
                       "zamon qoʻshimchasi qoʻyilmaydi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 숙제를 <strong>______</strong> 잠을 못 "
                "잤어요. (하다 + 느라고)</p>",
        "choices": ["했느라고", "하느라고", "할느라고", "하는느라고"],
        "correct": "하느라고",
        "explanation": "<p>느라고 dan oldin ham zamon boʻlmaydi: "
                       "<strong>하느라고</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: <strong>______</strong> 탓에 시험을 잘 못 "
                "봤어요. (게으르다)</p>",
        "choices": ["게으르는", "게으른", "게으를", "게을러서"],
        "correct": "게으른",
        "explanation": "<p>게으르다 — sifat → <strong>(으)ㄴ 탓에</strong>.</p>",
    },
    {
        "text": "<p>“Ob-havo tufayli samolyot bekor qilindi” — qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["날씨를 탓에 비행기가 취소됐어요",
                    "날씨가 탓에 비행기가 취소됐어요",
                    "날씨 탓에 비행기가 취소됐어요",
                    "날씨인 탓에 비행기가 취소됐어요"],
        "correct": "날씨 탓에 비행기가 취소됐어요",
        "explanation": "<p>Ot bilan 탓에 <strong>qoʻshimchasiz</strong> "
                       "keladi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 버스가 갑자기 <strong>______</strong> 바람에 "
                "넘어질 뻔했어요. (서다)</p>",
        "choices": ["선", "서는", "설", "섰는"],
        "correct": "서는",
        "explanation": "<p>바람에 → faqat 는. PK-63 dagi "
                       "<strong>뻔했어요</strong> bilan juda tabiiy "
                       "juftlik.</p>",
    },
    {
        "text": "<p>Toʻldiring: 게임을 <strong>______</strong> 전화를 못 "
                "받았어요. (하다 + 느라고)</p>",
        "choices": ["하느라고", "했느라고", "하는 바람에", "한 탓에"],
        "correct": "하느라고",
        "explanation": "<p>Ikkala ishni ham <strong>men</strong> qilaman "
                       "— bu bahona, demak 느라고.</p>",
    },
    {
        "text": "<p>“Oʻqituvchining sharofati bilan imtihondan oʻtdim” — "
                "qaysi biri toʻgʻri?</p>",
        "choices": ["선생님 탓에 합격했어요", "선생님 덕분에 합격했어요",
                    "선생님 바람에 합격했어요", "선생님 느라고 합격했어요"],
        "correct": "선생님 덕분에 합격했어요",
        "explanation": "<p>Natija <strong>yaxshi</strong> boʻlgani uchun "
                       "덕분에. 탓에 ayb koʻrsatadi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Nima uchun <strong>동생이 게임하느라고 저는 공부를 못 "
                "했어요</strong> notoʻgʻri?</p>",
        "choices": ["Zamon xato",
                    "느라고 da ikkala gapning egasi bir xil boʻlishi kerak",
                    "게임하다 feʼl emas",
                    "공부를 toʻldiruvchi boʻlolmaydi"],
        "correct": "느라고 da ikkala gapning egasi bir xil boʻlishi kerak",
        "explanation": "<p>Toʻgʻrisi — 동생이 게임하<strong>는 바람에</strong> "
                       "저는 공부를 못 했어요.</p>",
    },
    {
        "text": "<p>Qaysi qolip “kimningdir aybi” ohangini beradi?</p>",
        "choices": ["는 바람에", "(으)ㄴ/는 탓에", "느라고", "덕분에"],
        "correct": "(으)ㄴ/는 탓에",
        "explanation": "<p>탓 — “ayb” degan ot. 게으른 탓에 = "
                       "“dangasaligim <strong>aybi bilan</strong>”.</p>",
    },
    {
        "text": "<p><strong>는 바람에</strong> dan keyingi gap qanday "
                "boʻladi?</p>",
        "choices": ["Odatda oʻtgan zamonda va salbiy",
                    "Odatda kelasi zamonda",
                    "Odatda buyruq",
                    "Odatda ijobiy"],
        "correct": "Odatda oʻtgan zamonda va salbiy",
        "explanation": "<p>Kutilmagan xalaqit allaqachon boʻlib oʻtgan va "
                       "natija koʻpincha yomon: 못 갔어요, 늦었어요.</p>",
    },
    {
        "text": "<p>Qaysi qatorda uchalasi ham toʻgʻri yozilgan?</p>",
        "choices": ["온 바람에 / 했느라고 / 게으르는 탓에",
                    "오는 바람에 / 하느라고 / 게으른 탓에",
                    "올 바람에 / 하는느라고 / 게으를 탓에",
                    "왔는 바람에 / 하느라고 / 게으른 탓에"],
        "correct": "오는 바람에 / 하느라고 / 게으른 탓에",
        "explanation": "<p>바람에 va 느라고 da <strong>zamon yoʻq</strong>; "
                       "탓에 dan oldin sifat (으)ㄴ oladi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>비가 온 바람에 소풍을 못 "
                "갔어요.</strong></p>",
        "choices": ["온 → 오는", "온 → 올", "못 갔어요 → 안 갔어요",
                    "Xato yoʻq"],
        "correct": "온 → 오는",
        "explanation": "<p>바람에 dan oldin faqat <strong>는</strong> "
                       "shakli keladi.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>숙제를 했느라고 잠을 못 "
                "잤어요.</strong></p>",
        "choices": ["했느라고 → 하느라고", "했느라고 → 하는 느라고",
                    "잠을 → 잠이", "Xato yoʻq"],
        "correct": "했느라고 → 하느라고",
        "explanation": "<p>느라고 dan oldin zamon qoʻshimchasi "
                       "qoʻyilmaydi.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Kech turib qolganim tufayli darsga kechikdim” — qaysi "
                "biri eng tabiiy?</p>",
        "choices": ["늦잠을 자는 바람에 지각했어요",
                    "늦잠을 잔 바람에 지각했어요",
                    "늦잠을 자느라고 지각했어요",
                    "늦잠 덕분에 지각했어요"],
        "correct": "늦잠을 자는 바람에 지각했어요",
        "explanation": "<p>Kutilmagan xalaqit + salbiy natija = "
                       "<strong>는 바람에</strong>, va oldida zamon "
                       "boʻlmaydi.</p>",
    },
    {
        "text": "<p><strong>가:</strong> 왜 전화를 안 받았어요?</p>"
                "<p><strong>나:</strong> ___</p>",
        "choices": ["샤워하느라고 못 받았어요", "샤워했느라고 못 받았어요",
                    "샤워하는 탓에 못 받았어요", "샤워 덕분에 못 받았어요"],
        "correct": "샤워하느라고 못 받았어요",
        "explanation": "<p>Bu <strong>bahona</strong>: ikkala ishni ham men "
                       "qilaman, va ikkinchisi bajarilmay qoldi.</p>",
    },
]


# =====================================================================
# PK-70 — (으)ㄹ걸 그랬다, 았/었어야 했다
# =====================================================================

Q_PK70 = [
    # 1–5 tanish
    {
        "text": "<p><strong>(으)ㄹ걸 그랬다</strong> nimani bildiradi?</p>",
        "choices": ["…sam boʻlardi (afsus)", "…shim mumkin",
                    "…moqchiman", "…sa kerak"],
        "correct": "…sam boʻlardi (afsus)",
        "explanation": "<p>일찍 잘걸 그랬어요 — “erta uxlasam boʻlardi”. "
                       "Demak uxlamadim va hozir afsusdaman.</p>",
    },
    {
        "text": "<p><strong>걸</strong> qaysi soʻzning qisqargani?</p>",
        "choices": ["것을", "거기", "그것", "게"],
        "correct": "것을",
        "explanation": "<p>갈 <strong>것을</strong> 그랬다 → 갈<strong>걸"
                       "</strong> 그랬어요 — yana oʻsha 것 oilasi.</p>",
    },
    {
        "text": "<p>Bu qolipning inkori qanday?</p>",
        "choices": ["안 (으)ㄹ걸 그랬다", "지 말걸 그랬다",
                    "지 않을걸 그랬다", "못 (으)ㄹ걸 그랬다"],
        "correct": "지 말걸 그랬다",
        "explanation": "<p>그 말을 하지 <strong>말걸</strong> 그랬어요 — "
                       "“u gapni aytmasam boʻlardi”. 마걸 emas.</p>",
    },
    {
        "text": "<p><strong>(으)ㄹ걸 그랬다</strong> kim haqida "
                "ishlatiladi?</p>",
        "choices": ["Faqat oʻzim haqimda", "Faqat boshqalar haqida",
                    "Har kim haqida", "Faqat guruh haqida"],
        "correct": "Faqat oʻzim haqimda",
        "explanation": "<p>Bu <strong>shaxsiy afsus</strong>. Boshqa odam "
                       "haqida 았/었어야 했다 ishlatiladi.</p>",
    },
    {
        "text": "<p><strong>았/었어야 했다</strong> qaysi qolipning oʻtgan "
                "zamoni?</p>",
        "choices": ["아/어도 되다", "아/어야 하다", "아/어 보다", "아/어 주다"],
        "correct": "아/어야 하다",
        "explanation": "<p>PK-50 dagi majburiyat qolipi. Majburiyat bor "
                       "edi, lekin <strong>bajarilmadi</strong>.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 어제 일찍 <strong>______</strong> 그랬어요. "
                "(자다)</p>",
        "choices": ["잤을걸", "잘걸", "자을걸", "자는걸"],
        "correct": "잘걸",
        "explanation": "<p>자 da 받침 yoʻq → <strong>ㄹ걸</strong>. Zamon "
                       "qoʻshimchasi qoʻyilmaydi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 더 열심히 <strong>______</strong> 그랬어요. "
                "(공부하다)</p>",
        "choices": ["공부했을걸", "공부하는걸", "공부할걸", "공부하을걸"],
        "correct": "공부할걸",
        "explanation": "<p>하 da 받침 yoʻq → <strong>공부할걸</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 아침을 <strong>______</strong> 그랬어요. "
                "(먹다)</p>",
        "choices": ["먹을걸", "먹걸", "먹는걸", "먹었을걸"],
        "correct": "먹을걸",
        "explanation": "<p>먹 da 받침 bor → <strong>을걸</strong>.</p>",
    },
    {
        "text": "<p>“U gapni aytmasam boʻlardi” — qaysi biri toʻgʻri?</p>",
        "choices": ["그 말을 하지 마걸 그랬어요",
                    "그 말을 안 할걸 그랬어요",
                    "그 말을 하지 말걸 그랬어요",
                    "그 말을 하지 않을걸 그랬어요"],
        "correct": "그 말을 하지 말걸 그랬어요",
        "explanation": "<p>말다 ning oʻzagi <strong>말</strong> → "
                       "말걸. Bu PK-61 dagi 말라고 bilan bir xil "
                       "mantiq.</p>",
    },
    {
        "text": "<p>Toʻldiring: 우산을 <strong>______</strong> 했어요. "
                "(가져오다 + 았/었어야)</p>",
        "choices": ["가져와야", "가져왔어야", "가져올걸", "가져오느라고"],
        "correct": "가져왔어야",
        "explanation": "<p>Bajarilmagan majburiyat uchun <strong>았/었</strong> "
                       "kerak: 가져왔어야 했어요.</p>",
    },
    {
        "text": "<p>Ogʻzaki nutqda bu qolip qanday qisqaradi?</p>",
        "choices": ["그랬어요 tushadi, faqat (으)ㄹ걸 qoladi",
                    "걸 tushadi", "(으)ㄹ tushadi", "Qisqarmaydi"],
        "correct": "그랬어요 tushadi, faqat (으)ㄹ걸 qoladi",
        "explanation": "<p>아… 일찍 <strong>올걸</strong>. — oʻz-oʻziga "
                       "aytilgan gap, ohangi pasayadi.</p>",
    },
    {
        "text": "<p>“Oʻshanda kechirim soʻrashim kerak edi” — qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["그때 사과해야 했어요", "그때 사과했어야 했어요",
                    "그때 사과할걸 했어요", "그때 사과하느라고 했어요"],
        "correct": "그때 사과했어야 했어요",
        "explanation": "<p>Majburiyat bor edi va <strong>bajarilmadi</strong> "
                       "— shuning uchun 았/었어야 했어요.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Farqi nimada? <strong>일찍 잘걸 그랬어요</strong> / "
                "<strong>일찍 잤어야 했어요</strong></p>",
        "choices": ["Birinchisi — shaxsiy hissiy afsus; ikkinchisi — "
                    "obyektiv majburiyat bajarilmagan",
                    "Birinchisi obyektiv, ikkinchisi hissiy",
                    "Ikkalasi bir xil",
                    "Birinchisi kelasi zamon"],
        "correct": "Birinchisi — shaxsiy hissiy afsus; ikkinchisi — "
                   "obyektiv majburiyat bajarilmagan",
        "explanation": "<p>Shuning uchun ikkinchisi kuchliroq va "
                       "<strong>boshqa odam haqida ham</strong> "
                       "aytiladi.</p>",
    },
    {
        "text": "<p>Doʻstingizni tanqid qilmoqchisiz: “oldindan aytishi "
                "kerak edi”. Qaysi qolip?</p>",
        "choices": ["미리 말할걸 그랬어요", "미리 말했어야 했어요",
                    "미리 말하느라고 했어요", "미리 말할 뻔했어요"],
        "correct": "미리 말했어야 했어요",
        "explanation": "<p>(으)ㄹ걸 그랬다 faqat <strong>oʻzingiz</strong> "
                       "haqingizda. Boshqa odam uchun 았/었어야 했다.</p>",
    },
    {
        "text": "<p><strong>커피를 마시지 말걸 그랬어요</strong> — kofe "
                "ichdimmi?</p>",
        "choices": ["Ha, ichdim va afsusdaman", "Yoʻq, ichmadim",
                    "Bilib boʻlmaydi", "Ichmoqchi edim"],
        "correct": "Ha, ichdim va afsusdaman",
        "explanation": "<p>지 말걸 그랬다 = “qilmasam boʻlardi” — demak "
                       "<strong>qildim</strong>. Aynan shuning uchun "
                       "afsus bor.</p>",
    },
    {
        "text": "<p>걸 dan oldin nima kelmaydi?</p>",
        "choices": ["(으)ㄹ", "Zamon qoʻshimchasi (았/었)", "Feʼl oʻzagi",
                    "지 말"],
        "correct": "Zamon qoʻshimchasi (았/었)",
        "explanation": "<p><s>잤을걸 그랬어요</s> ✗ → <strong>잘걸 "
                       "그랬어요</strong>. Faqat (으)ㄹ.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>어제 일찍 잤을걸 그랬어요.</strong></p>",
        "choices": ["잤을걸 → 잘걸", "잤을걸 → 자을걸",
                    "그랬어요 → 그래요", "Xato yoʻq"],
        "correct": "잤을걸 → 잘걸",
        "explanation": "<p>걸 dan oldin faqat <strong>(으)ㄹ</strong> — "
                       "zamon qoʻshimchasi qoʻyilmaydi.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>그 말을 하지 마걸 그랬어요.</strong></p>",
        "choices": ["마걸 → 말걸", "마걸 → 말을걸", "하지 → 하기",
                    "Xato yoʻq"],
        "correct": "마걸 → 말걸",
        "explanation": "<p>말다 ning oʻzagi <strong>말</strong>, unga "
                       "ㄹ걸 emas, toʻgʻridan-toʻgʻri 걸 qoʻshiladi: "
                       "말걸.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Koʻproq tirishib oʻqisam boʻlardi” — qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["더 열심히 공부했을걸 그랬어요",
                    "더 열심히 공부할걸 그랬어요",
                    "더 열심히 공부하느라고 그랬어요",
                    "더 열심히 공부할 뻔했어요"],
        "correct": "더 열심히 공부할걸 그랬어요",
        "explanation": "<p>공부하 + ㄹ걸 그랬어요 — shaxsiy afsus.</p>",
    },
    {
        "text": "<p><strong>가:</strong> 시험 어땠어요?</p>"
                "<p><strong>나:</strong> 잘 못 봤어요. ___</p>",
        "choices": ["더 열심히 공부할걸 그랬어요",
                    "더 열심히 공부했을걸 그랬어요",
                    "더 열심히 공부하는 바람에 그랬어요",
                    "더 열심히 공부할 뻔했어요"],
        "correct": "더 열심히 공부할걸 그랬어요",
        "explanation": "<p>Imtihon oʻtdi, oʻzgartirib boʻlmaydi — qolgani "
                       "faqat <strong>afsus</strong>. Aynan bu qolipning "
                       "oʻrni.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-68 Mashq: (으)ㄴ/는 데다가 — vaziyatning ogʻirlashuvi",
        "description": "20 savol — feʼl/sifat/ot shakllari, uchta shart, "
                       "뿐만 아니라 va 반면에 dan farqi.",
        "tutorial":    "PK-68:",
        "level":       "medium",
        "questions":   Q_PK68,
    },
    {
        "title":       "PK-69 Mashq: 는 바람에 · 탓에 · 느라고",
        "description": "20 savol — uchta salbiy sabab qolipi, zamon "
                       "cheklovlari, bir xil ega sharti va 덕분에 juftligi.",
        "tutorial":    "PK-69:",
        "level":       "medium",
        "questions":   Q_PK69,
    },
    {
        "title":       "PK-70 Mashq: (으)ㄹ걸 그랬다 · 았/었어야 했다",
        "description": "20 savol — yasalishi, 지 말걸 inkori, kim haqida "
                       "ishlatilishi va ikki qolipning ohangdagi farqi.",
        "tutorial":    "PK-70:",
        "level":       "medium",
        "questions":   Q_PK70,
    },
]
