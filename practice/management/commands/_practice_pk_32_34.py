# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-32 … PK-34.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
PK-32 dan boshlab level = medium.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_32_34.py --master=prime \\
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
# PK-32 — Notoʻgʻri feʼllar 1: ㅂ, ㄷ, 으
# =====================================================================

Q_PK32 = [
    # 1–5 tanish
    {
        "text": "<p>Notoʻgʻri tuslanish qachon ishga tushadi?</p>",
        "choices": ["Qoʻshimcha unli bilan boshlanganda",
                    "Qoʻshimcha undosh bilan boshlanganda",
                    "Gap oʻtgan zamonda boʻlganda",
                    "Har doim, hech qanday shartsiz"],
        "correct": "Qoʻshimcha unli bilan boshlanganda",
        "explanation": "<p>Oʻzgarish <strong>oʻzak bilan qoʻshimcha uchrashadigan "
                       "joyda</strong> boʻladi. Uchrashuv joyida unli boʻlsa — oʻzak "
                       "oʻzgaradi (더워요, 들어요). Undosh boʻlsa hech narsa "
                       "boʻlmaydi: 덥습니다, 듣습니다.</p>",
    },
    {
        "text": "<p><strong>덥다</strong> ning 아/어요 shakli qaysi?</p>",
        "choices": ["덥어요", "더워요", "더어요", "덥아요"],
        "correct": "더워요",
        "explanation": "<p>ㅂ tuslanishi: 덥 → 더<strong>우</strong>, keyin "
                       "우 + 어요 = <strong>워요</strong>. <s>덥어요</s> — oʻzbek "
                       "oʻquvchi eng koʻp qiladigan xato.</p>",
    },
    {
        "text": "<p><strong>듣다</strong> ning 아/어요 shakli qaysi?</p>",
        "choices": ["듣어요", "듣아요", "들어요", "듣워요"],
        "correct": "들어요",
        "explanation": "<p>ㄷ tuslanishi: 받침 <strong>ㄷ</strong> unli oldida "
                       "<strong>ㄹ</strong> ga aylanadi — 듣 → 들. Xuddi shunday "
                       "걷다 → 걸어요.</p>",
    },
    {
        "text": "<p><strong>바쁘다</strong> ning 아/어요 shakli qaysi?</p>",
        "choices": ["바빠요", "바쁘어요", "바뻐요", "바쁴요"],
        "correct": "바빠요",
        "explanation": "<p>으 tushadi, keyin oldingi boʻgʻinga qaraladi: 바 dagi "
                       "unli <strong>ㅏ</strong>, shuning uchun <strong>아</strong> "
                       "qoʻshiladi — 바빠요.</p>",
    },
    {
        "text": "<p>ㅂ tuslanishida 받침 ㅂ nimaga aylanadi?</p>",
        "choices": ["ㄹ", "으", "우", "이"],
        "correct": "우",
        "explanation": "<p>ㅂ → <strong>우</strong>: 춥다 → 추우 → 추워요. "
                       "ㄹ ga aylanadigani — ㄷ tuslanishi (듣다 → 들어요).</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>어제는 아주 ___</strong> (“Kecha juda sovuq edi.”) — 춥다</p>",
        "choices": ["춥었어요", "추웠어요", "춥았어요", "추었어요"],
        "correct": "추웠어요",
        "explanation": "<p>Oʻtgan zamon ham 아/어 shakliga qurilgani uchun ㅂ "
                       "baribir oʻzgaradi: 춥 → 추우 → 추워 → "
                       "<strong>추웠어요</strong>.</p>",
    },
    {
        "text": "<p><strong>걷다</strong> dan “yura olaman” degan shaklni tuzing.</p>",
        "choices": ["걷을 수 있어요", "걸을 수 있어요", "걷를 수 있어요",
                    "걸를 수 있어요"],
        "correct": "걸을 수 있어요",
        "explanation": "<p>(으)ㄹ 수 있다 ham <strong>으</strong> — yaʼni unli — "
                       "bilan boshlanadi, shuning uchun ㄷ → ㄹ oʻzgarishi bu yerda "
                       "ham ishlaydi: <strong>걸을 수 있어요</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>머리가 ___</strong> (“Boshim ogʻriyapti.”) — 아프다</p>",
        "choices": ["아프어요", "아푸요", "아파요", "아퍼요"],
        "correct": "아파요",
        "explanation": "<p>으 tushadi; oldingi boʻgʻin 아 da unli <strong>ㅏ</strong>, "
                       "shuning uchun 아 qoʻshiladi — <strong>아파요</strong>.</p>",
    },
    {
        "text": "<p><strong>예쁘다</strong> ning toʻgʻri shakli qaysi?</p>",
        "choices": ["예뻐요", "예빠요", "예쁘어요", "예뻬요"],
        "correct": "예뻐요",
        "explanation": "<p>으 tushgach 예 dagi unli qaraladi — u <strong>ㅖ</strong>, "
                       "yaʼni ㅏ ham, ㅗ ham emas. Shuning uchun <strong>어</strong>: "
                       "예뻐요. Solishtiring: 아프다 → 아파요.</p>",
    },
    {
        "text": "<p><strong>쓰다</strong> (yozmoq) ning 아/어요 shakli qaysi?</p>",
        "choices": ["싸요", "쓰어요", "써요", "쑤어요"],
        "correct": "써요",
        "explanation": "<p>Oʻzak bitta boʻgʻindan iborat — qaraydigan “oldingi "
                       "boʻgʻin” yoʻq. Bunday paytda har doim <strong>어</strong>: "
                       "쓰 + 어요 = <strong>써요</strong>. Xuddi shunday 크다 → "
                       "커요.</p>",
    },
    {
        "text": "<p><strong>돕다</strong> (yordam bermoq) ning shakli qaysi?</p>",
        "choices": ["도워요", "도와요", "돕어요", "도우요"],
        "correct": "도와요",
        "explanation": "<p><strong>돕다</strong> va <strong>곱다</strong> — ㅂ "
                       "guruhining ikkita istisnosi: ular 워요 emas, "
                       "<strong>와요</strong> beradi. Boshqa hech bir ㅂ feʼl bunday "
                       "qilmaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>이 노래를 ___</strong> (“Bu qoʻshiqni tinglang.”) — 듣다</p>",
        "choices": ["들으세요", "듣으세요", "듣세요", "들세요"],
        "correct": "들으세요",
        "explanation": "<p>(으)세요 unli bilan boshlanadi → ㄷ → ㄹ: 듣 → 들. "
                       "받침 bor, shuning uchun <strong>으세요</strong> — "
                       "<strong>들으세요</strong>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikkitadan qaysi biri <strong>notoʻgʻri</strong> feʼl?</p>"
                "<p><strong>입다</strong> · <strong>맵다</strong></p>",
        "choices": ["입다", "맵다", "Ikkalasi ham", "Hech qaysisi"],
        "correct": "맵다",
        "explanation": "<p><strong>맵다</strong> → 매워요 (notoʻgʻri), "
                       "<strong>입다</strong> → 입어요 (oddiy). Ishonchli belgi: "
                       "ㅂ bilan tugagan <em>sifat</em>lar deyarli har doim "
                       "notoʻgʻri, <em>harakat feʼl</em>lari koʻpincha toʻgʻri.</p>",
    },
    {
        "text": "<p><strong>닫다</strong> (yopmoq) ning toʻgʻri shakli qaysi?</p>",
        "choices": ["달아요", "닫어요", "닫아요", "다라요"],
        "correct": "닫아요",
        "explanation": "<p>닫다 — <em>oddiy</em> feʼl, ㄷ oʻzgarmaydi: "
                       "<strong>닫아요</strong>. 걷다 (걸어요) bilan adashtirmang. "
                       "받다 va 믿다 ham shunday oddiy.</p>",
    },
    {
        "text": "<p><strong>덥다</strong> ning 습니다 shakli qaysi?</p>",
        "choices": ["더웁니다", "덥습니다", "더워습니다", "덥읍니다"],
        "correct": "덥습니다",
        "explanation": "<p>습니다 <strong>undosh</strong> bilan boshlanadi, shuning "
                       "uchun oʻzak umuman oʻzgarmaydi: <strong>덥습니다</strong>. "
                       "Notoʻgʻri feʼl “har doim notoʻgʻri” degani emas.</p>",
    },
    {
        "text": "<p>Qaysi juftlikda ikkala feʼl ham <strong>notoʻgʻri</strong>?</p>",
        "choices": ["받다 · 닫다", "입다 · 잡다", "춥다 · 걷다", "믿다 · 좁다"],
        "correct": "춥다 · 걷다",
        "explanation": "<p><strong>춥다</strong> → 추워요 (ㅂ), <strong>걷다</strong> "
                       "→ 걸어요 (ㄷ). Qolgan juftliklarning hammasi oddiy feʼllar: "
                       "받아요, 닫아요, 입어요, 잡아요, 믿어요, 좁아요.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["오늘 날씨가 덥어요.", "저는 음악을 듣어요.",
                    "저는 오늘 바빠요.", "옷을 이워요."],
        "correct": "저는 오늘 바빠요.",
        "explanation": "<p><strong>바쁘다 → 바빠요</strong> toʻgʻri. Qolganlari: "
                       "덥어요 → <strong>더워요</strong>, 듣어요 → "
                       "<strong>들어요</strong>, 이워요 → <strong>입어요</strong> "
                       "(입다 oddiy feʼl).</p>",
    },
    {
        "text": "<p>Qaysi gapda <strong>xato bor</strong>?</p>",
        "choices": ["김치가 아주 매워요.", "공원에서 걸어요.",
                    "언니가 아주 예뻐요.", "저는 편지를 쓰어요."],
        "correct": "저는 편지를 쓰어요.",
        "explanation": "<p><strong>쓰어요</strong> notoʻgʻri — 으 tushishi kerak: "
                       "<strong>써요</strong>. Qolgan uchtasi toʻgʻri: 맵다 → 매워요, "
                       "걷다 → 걸어요, 예쁘다 → 예뻐요.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 한국어가 어때요?<br>나: ___</strong></p>",
        "choices": ["어렵어요.", "어려워요.", "어렵아요.", "어려어요."],
        "correct": "어려워요.",
        "explanation": "<p>어렵다 — ㅂ notoʻgʻri feʼli: 어렵 → 어려우 → "
                       "<strong>어려워요</strong>. Sifatlarning ㅂ guruhi eng katta "
                       "guruh: 쉽다, 무겁다, 가깝다 ham shunday.</p>",
    },
    {
        "text": "<p>“Kecha juda band edim, shuning uchun xat yoza olmadim” — "
                "eng toʻgʻri gap qaysi?</p>",
        "choices": ["어제 아주 바빴어요. 그래서 편지를 못 썼어요.",
                    "어제 아주 바쁘었어요. 그래서 편지를 못 쓰었어요.",
                    "어제 아주 바빠었어요. 그래서 편지를 못 써었어요.",
                    "어제 아주 바쁩었어요. 그래서 편지를 못 썼어요."],
        "correct": "어제 아주 바빴어요. 그래서 편지를 못 썼어요.",
        "explanation": "<p>Ikkala feʼl ham 으 guruhida: 바쁘 + 았어요 = "
                       "<strong>바빴어요</strong>, 쓰 + 었어요 = "
                       "<strong>썼어요</strong>. Oʻtgan zamon ham 아/어 shakliga "
                       "tayangani uchun 으 baribir tushadi.</p>",
    },
]


# =====================================================================
# PK-33 — 고
# =====================================================================

Q_PK33 = [
    # 1–5 tanish
    {
        "text": "<p><strong>고</strong> qanday vazifani bajaradi?</p>",
        "choices": ["Ikki gapni bogʻlaydi — “va” yoki “…ib”",
                    "Inkor yasaydi",
                    "Oʻtgan zamon yasaydi",
                    "Savol yasaydi"],
        "correct": "Ikki gapni bogʻlaydi — “va” yoki “…ib”",
        "explanation": "<p><strong>고</strong> ikki gapni bitta qiladi. Ikki maʼnoda "
                       "ishlaydi: <em>sanash</em> (김치는 맵고 불고기는 달아요) va "
                       "<em>ketma-ketlik</em> (밥을 먹고 학교에 가요).</p>",
    },
    {
        "text": "<p><strong>먹다</strong> ga 고 qoʻshing.</p>",
        "choices": ["먹으고", "머고", "먹고", "먹어고"],
        "correct": "먹고",
        "explanation": "<p>고 oʻzakka <strong>toʻgʻridan-toʻgʻri</strong> yopishadi. "
                       "받침 ayrisi yoʻq, 으 yoʻq: 먹 + 고 = <strong>먹고</strong>.</p>",
    },
    {
        "text": "<p>고 da 받침 ayrisi bormi?</p>",
        "choices": ["Ha, 받침 bor boʻlsa 으고", "Yoʻq, har doim shunchaki 고",
                    "Ha, 받침 bor boʻlsa 이고", "Faqat sifatlarda bor"],
        "correct": "Yoʻq, har doim shunchaki 고",
        "explanation": "<p>고 — eng oson qoʻshimchalardan biri: 가고, 먹고, 읽고, "
                       "공부하고. <s>먹으고</s> degan shakl yoʻq. (이고 — bu boshqa "
                       "narsa: ot + 이다 shakli.)</p>",
    },
    {
        "text": "<p>Ketma-ketlik maʼnosida oʻtgan zamon qayerga qoʻyiladi?</p>",
        "choices": ["Faqat oxirgi feʼlga", "Faqat birinchi feʼlga",
                    "Ikkala feʼlga ham", "Hech qaysisiga"],
        "correct": "Faqat oxirgi feʼlga",
        "explanation": "<p><strong>밥을 먹고 잤어요</strong> — <s>먹었고</s> emas. "
                       "Oʻzbekcha ham xuddi shunday: “ovqat <em>yeb</em> "
                       "uxla<em>dim</em>” — zamon faqat oxirgi feʼlda.</p>",
    },
    {
        "text": "<p><strong>학생</strong> (talaba) ga 고 qanday qoʻshiladi?</p>",
        "choices": ["학생고", "학생이고", "학생으고", "학생하고"],
        "correct": "학생이고",
        "explanation": "<p>Ot + 이다 shakli 받침 ga qarab tanlanadi: 받침 bor → "
                       "<strong>이고</strong> (학생이고), 받침 yoʻq → "
                       "<strong>고</strong> (친구고).</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>저는 아침에 밥을 ___ 학교에 가요.</strong> — 먹다</p>",
        "choices": ["먹어서", "먹었고", "먹고", "먹으고"],
        "correct": "먹고",
        "explanation": "<p>Ketma-ketlik: avval ovqat, keyin maktab. Zamon oxirgi "
                       "feʼlda (가요), shuning uchun birinchisi sof oʻzak + 고 = "
                       "<strong>먹고</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>이 식당은 ___ 맛있어요.</strong> "
                "(“Bu oshxona arzon va mazali.”) — 싸다</p>",
        "choices": ["싸고", "싸으고", "쌌고", "싸서"],
        "correct": "싸고",
        "explanation": "<p>Sifatlar ham 고 oladi: 싸 + 고 = <strong>싸고</strong>. "
                       "Bu <em>sanash</em> maʼnosi — ikki xususiyat bir vaqtda.</p>",
    },
    {
        "text": "<p><strong>덥다</strong> ga 고 qoʻshilganda oʻzak oʻzgaradimi?</p>",
        "choices": ["Ha — 더우고", "Yoʻq — 덥고", "Ha — 더워고", "Ha — 덥으고"],
        "correct": "Yoʻq — 덥고",
        "explanation": "<p>Notoʻgʻri tuslanish faqat <strong>unli</strong> bilan "
                       "boshlanuvchi qoʻshimcha oldida boʻladi. 고 esa undosh bilan "
                       "boshlanadi, shuning uchun <strong>덥고</strong> — hech narsa "
                       "oʻzgarmaydi (PK-32).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>어제 숙제를 ___ 놀았어요.</strong> — 하다</p>",
        "choices": ["했고", "하고", "해고", "하았고"],
        "correct": "하고",
        "explanation": "<p>Ketma-ketlikda birinchi feʼl zamonsiz qoladi: "
                       "<strong>하고</strong>. Oʻtgan zamon faqat oxirida — "
                       "놀았어요.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>손을 ___ 드세요.</strong> "
                "(“Qoʻlingizni yuvib ovqatlaning.”) — 씻다</p>",
        "choices": ["씻으세요", "씻어요", "씻고", "씻으고"],
        "correct": "씻고",
        "explanation": "<p>Buyruq shakli faqat <em>oxirgi</em> feʼlda turadi "
                       "(드세요), 고 dan oldingi qism esa har doim sof oʻzak + 고: "
                       "<strong>씻고</strong>.</p>",
    },
    {
        "text": "<p>Qaysi gap “Nonushta qilmay maktabga boraman” degan maʼnoni "
                "beradi?</p>",
        "choices": ["아침을 안 먹고 학교에 가요.", "아침을 먹고 학교에 안 가요.",
                    "아침을 먹지 마세요.", "아침을 못 먹어요."],
        "correct": "아침을 안 먹고 학교에 가요.",
        "explanation": "<p>고 dan oldingi qism ham inkor boʻlishi mumkin: "
                       "<strong>안 먹고</strong>. Ikkinchi variant esa teskarisini "
                       "aytadi — “nonushta qilib maktabga bormayman”.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>어제는 ___ 오늘은 더워요.</strong> "
                "(“Kecha sovuq edi, bugun issiq.”) — 춥다</p>",
        "choices": ["춥고", "추웠고", "추워고", "춥었고"],
        "correct": "추웠고",
        "explanation": "<p>Bu <em>sanash</em> — ikki har xil vaqt haqidagi ikki "
                       "alohida fakt, shuning uchun har biri oʻz zamonini oladi: "
                       "<strong>추웠고</strong>. (춥다 → 추웠 — PK-32, ㅂ → 우.)</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Qaysi gapda 고 <strong>ketma-ketlik</strong> (“…ib”) "
                "maʼnosida?</p>",
        "choices": ["김치는 맵고 불고기는 달아요.",
                    "옷을 사고 집에 갔어요.",
                    "이 옷은 싸고 예뻐요.",
                    "아프소나 씨는 학생이고 자수르 씨는 선생님이에요."],
        "correct": "옷을 사고 집에 갔어요.",
        "explanation": "<p><strong>옷을 사고 집에 갔어요</strong> — avval biri, "
                       "keyin ikkinchisi, ega bitta. Qolgan uchtasi "
                       "<em>sanash</em>: ikki mustaqil fakt, koʻpincha ikki xil "
                       "ega.</p>",
    },
    {
        "text": "<p>Qaysi juftlikda zamon <strong>toʻgʻri</strong> qoʻyilgan?</p>",
        "choices": ["밥을 먹었고 잤어요.", "밥을 먹고 잤어요.",
                    "밥을 먹었고 자요.", "밥을 먹고 자았어요."],
        "correct": "밥을 먹고 잤어요.",
        "explanation": "<p>Ketma-ketlikda zamon <strong>faqat oxirgi feʼlda</strong>. "
                       "<s>먹었고 잤어요</s> — koreys qulogʻiga ortiqcha eshitiladi.</p>",
    },
    {
        "text": "<p><strong>그리고</strong> va <strong>고</strong> orasidagi farq "
                "nima?</p>",
        "choices": ["Maʼnosi butunlay boshqa",
                    "그리고 — mustaqil soʻz, gap boshida; 고 — oʻzakka yopishadigan qoʻshimcha",
                    "고 faqat sifatlar bilan ishlatiladi",
                    "그리고 faqat yozma nutqda ishlatiladi"],
        "correct": "그리고 — mustaqil soʻz, gap boshida; 고 — oʻzakka yopishadigan qoʻshimcha",
        "explanation": "<p>Maʼnosi yaqin, oʻrni boshqa. <strong>밥을 먹고 "
                       "학교에 가요</strong> = <strong>밥을 먹어요. 그리고 학교에 "
                       "가요</strong>. Bittasini tanlang — ikkalasini birga "
                       "ishlatmang.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri yasalgan?</p>",
        "choices": ["아프소나 씨는 학생고 자수르 씨는 선생님이에요.",
                    "아프소나 씨는 학생이고 자수르 씨는 선생님이에요.",
                    "아프소나 씨는 학생으고 자수르 씨는 선생님이에요.",
                    "아프소나 씨는 학생이가고 자수르 씨는 선생님이에요."],
        "correct": "아프소나 씨는 학생이고 자수르 씨는 선생님이에요.",
        "explanation": "<p>학생 da 받침 bor → <strong>이고</strong>. 받침 yoʻq "
                       "boʻlganda esa oddiy 고: 친구<strong>고</strong>.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda <strong>xato bor</strong>?</p>",
        "choices": ["숙제를 하고 놀았어요.", "이 옷은 싸고 예뻐요.",
                    "책을 읽으고 잤어요.", "손을 씻고 밥을 먹어요."],
        "correct": "책을 읽으고 잤어요.",
        "explanation": "<p>고 da <strong>으 yoʻq</strong>: <s>읽으고</s> → "
                       "<strong>읽고</strong>. 고 받침 ayrisi boʻlmagan "
                       "qoʻshimcha.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["어제 숙제를 했고 놀았어요.",
                    "어제 숙제를 하고 놀았어요.",
                    "어제 숙제를 하고 놀아요.",
                    "숙제를 하고 놀았어요, 어제."],
        "correct": "어제 숙제를 하고 놀았어요.",
        "explanation": "<p>Zamon oxirgi feʼlda (놀았어요), vaqt soʻzi esa gap "
                       "boshida (어제). Uchinchi variantda zamon yoʻqolgan, "
                       "toʻrtinchisida soʻz tartibi buzilgan.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 아침에 뭐 해요?<br>나: ___</strong></p>",
        "choices": ["일어나고 세수를 하고 학교에 가요.",
                    "일어나서 세수를 해고 학교에 가요.",
                    "일어났고 세수를 했고 학교에 가요.",
                    "일어나고 세수를 하고 학교에 갔어요."],
        "correct": "일어나고 세수를 하고 학교에 가요.",
        "explanation": "<p>Kundalik tartib — hozirgi zamon, va 고 ni ketma-ket "
                       "qoʻyish mumkin. Zamon faqat oxirgi feʼlda: "
                       "<strong>가요</strong>.</p>",
    },
    {
        "text": "<p>“Kimchi achchiq va bulgogi shirin” — qaysi gap toʻgʻri?</p>",
        "choices": ["김치는 맵고 불고기는 달아요.",
                    "김치는 매워고 불고기는 달아요.",
                    "김치는 맵으고 불고기는 달아요.",
                    "김치는 맵고 불고기는 다라요."],
        "correct": "김치는 맵고 불고기는 달아요.",
        "explanation": "<p>맵다 + 고 = <strong>맵고</strong> (고 undosh bilan "
                       "boshlangani uchun ㅂ oʻzgarmaydi), 달다 → "
                       "<strong>달아요</strong>. Bu sanash: ikki alohida fakt, "
                       "ikki xil ega.</p>",
    },
]


# =====================================================================
# PK-34 — 지만
# =====================================================================

Q_PK34 = [
    # 1–5 tanish
    {
        "text": "<p><strong>지만</strong> qanday maʼno beradi?</p>",
        "choices": ["…lekin (qarama-qarshilik)", "…ib (ketma-ketlik)",
                    "…gani uchun (sabab)", "…moqchiman (xohish)"],
        "correct": "…lekin (qarama-qarshilik)",
        "explanation": "<p><strong>지만</strong> ikkinchi qism birinchisidan "
                       "<em>kutilmagan</em> narsa ekanini bildiradi: 한국어는 "
                       "어렵지만 재미있어요 — qiyin boʻlsa yoqmasligi kerak edi, "
                       "lekin yoqadi.</p>",
    },
    {
        "text": "<p><strong>먹다</strong> ga 지만 qoʻshing.</p>",
        "choices": ["먹으지만", "먹지만", "먹어지만", "머지만"],
        "correct": "먹지만",
        "explanation": "<p>지만 oʻzakka <strong>toʻgʻridan-toʻgʻri</strong> "
                       "yopishadi — 으 yoʻq, 받침 ayrisi yoʻq: 먹 + 지만 = "
                       "<strong>먹지만</strong>.</p>",
    },
    {
        "text": "<p>지만 da oʻtgan zamon qayerga qoʻyiladi?</p>",
        "choices": ["Faqat oxirgi feʼlga", "지만 dan oldin ham boʻladi",
                    "Zamon umuman ishlatilmaydi", "Faqat gap boshiga"],
        "correct": "지만 dan oldin ham boʻladi",
        "explanation": "<p><strong>한국에 갔지만 친구를 못 만났어요</strong> — "
                       "ikki tomon ikki mustaqil fikr, shuning uchun har biri oʻz "
                       "zamonini oladi. Bu 고 dan eng muhim farq.</p>",
    },
    {
        "text": "<p><strong>학생</strong> ga 지만 qanday qoʻshiladi?</p>",
        "choices": ["학생지만", "학생으지만", "학생이지만", "학생하지만"],
        "correct": "학생이지만",
        "explanation": "<p>받침 bor → <strong>이지만</strong> (학생이지만), "
                       "받침 yoʻq → <strong>지만</strong> (친구지만). Bu 이다 ning "
                       "odatdagi 받침 ayrisi.</p>",
    },
    {
        "text": "<p><strong>하지만</strong> nima?</p>",
        "choices": ["Qoʻshimcha — oʻzakka yopishadi",
                    "Mustaqil soʻz — yangi gap boshida turadi",
                    "Feʼlning oʻtgan zamoni",
                    "Savol soʻzi"],
        "correct": "Mustaqil soʻz — yangi gap boshida turadi",
        "explanation": "<p><strong>하지만</strong> alohida soʻz: 비싸요. "
                       "<strong>하지만</strong> 샀어요. <strong>지만</strong> esa "
                       "qoʻshimcha: 비싸<strong>지만</strong> 샀어요. Maʼnosi bir "
                       "xil, oʻrni boshqa.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>한국어는 ___ 재미있어요.</strong> — 어렵다</p>",
        "choices": ["어렵으지만", "어려워지만", "어렵지만", "어려우지만"],
        "correct": "어렵지만",
        "explanation": "<p>지만 undosh bilan boshlanadi, shuning uchun ㅂ "
                       "oʻzgarmaydi: <strong>어렵지만</strong>. PK-32 ning qoidasi "
                       "bu yerda ham ishlaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>어제 한국에 ___ 친구를 못 만났어요.</strong> — 가다</p>",
        "choices": ["가지만", "갔지만", "가고", "갈 지만"],
        "correct": "갔지만",
        "explanation": "<p>Ish oʻtmishda boʻlgani uchun zamon <em>지만 dan "
                       "oldin</em> turadi: <strong>갔지만</strong>. <s>가지만</s> "
                       "zamonsiz boʻlib qoladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>이 옷은 ___ 너무 비싸요.</strong> — 예쁘다</p>",
        "choices": ["예뻐지만", "예쁘지만", "예쁘어지만", "예쁩지만"],
        "correct": "예쁘지만",
        "explanation": "<p>으 tuslanishi faqat 아/어 oldida boʻladi. 지만 undosh "
                       "bilan boshlangani uchun 으 joyida qoladi: "
                       "<strong>예쁘지만</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>어제는 ___ 오늘은 안 바빠요.</strong> — 바쁘다</p>",
        "choices": ["바쁘지만", "바빠지만", "바빴지만", "바쁩지만"],
        "correct": "바빴지만",
        "explanation": "<p>Kecha — oʻtgan zamon, shuning uchun 지만 dan oldin "
                       "았 qoʻyiladi: 바쁘 + 았 = 바빴 → "
                       "<strong>바빴지만</strong>.</p>",
    },
    {
        "text": "<p>Qaysi gap “Men kimchini yoqtiraman, lekin ukam yoqtirmaydi” "
                "degani?</p>",
        "choices": ["저는 김치를 좋아하지만 동생은 안 좋아해요.",
                    "저는 김치를 좋아하고 동생은 안 좋아해요.",
                    "저는 김치를 안 좋아하지만 동생은 좋아해요.",
                    "저는 김치를 좋아하지만 동생도 좋아해요."],
        "correct": "저는 김치를 좋아하지만 동생은 안 좋아해요.",
        "explanation": "<p>지만 uchun ikki ega har xil boʻlishi mutlaqo normal. "
                       "Uchinchi variant teskarisini aytadi, toʻrtinchisida esa "
                       "qarama-qarshilik yoʻq.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>___ 시험이 어려웠어요.</strong> "
                "(“Oʻqidim, lekin imtihon qiyin edi.”) — 공부하다</p>",
        "choices": ["공부하지만", "공부했지만", "공부하고", "공부해지만"],
        "correct": "공부했지만",
        "explanation": "<p>Oʻqish ishi oʻtmishda tugagan: "
                       "<strong>공부했지만</strong>. 어려웠어요 da esa 어렵다 → "
                       "어려웠 (PK-32, ㅂ → 우).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>자수르 씨는 ___ 한국어를 아주 잘해요.</strong> — 학생</p>",
        "choices": ["학생지만", "학생이지만", "학생이고", "학생하지만"],
        "correct": "학생이지만",
        "explanation": "<p>받침 bor (학생) → <strong>이지만</strong>. 이고 ham "
                       "grammatik jihatdan toʻgʻri, lekin u shunchaki sanaydi — "
                       "bu yerda esa kutilmagan narsa aytilyapti.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Qaysi biri toʻgʻri?</p>"
                "<p><strong>이 식당은 싸고 맛없어요</strong> · "
                "<strong>이 식당은 싸지만 맛없어요</strong></p>",
        "choices": ["이 식당은 싸고 맛없어요", "이 식당은 싸지만 맛없어요",
                    "Ikkalasi ham bir xil", "Ikkalasi ham notoʻgʻri"],
        "correct": "이 식당은 싸지만 맛없어요",
        "explanation": "<p>Arzon — yaxshi xabar, mazasiz — yomon. Ular "
                       "<strong>qarama-qarshi</strong>, shuning uchun "
                       "<strong>지만</strong>. 고 ishlatilsa, ikkala tomon bir "
                       "yoʻnalishga qaragan boʻlishi kerak edi (싸고 맛있어요).</p>",
    },
    {
        "text": "<p>Qaysi gapda zamon <strong>toʻgʻri</strong> qoʻyilgan?</p>",
        "choices": ["밥을 먹었고 배고파요.", "밥을 먹었지만 배고파요.",
                    "밥을 먹고 배고팠어요지만.", "밥을 먹지만 배고파요."],
        "correct": "밥을 먹었지만 배고파요.",
        "explanation": "<p>지만 da zamon oldin ham boʻladi: "
                       "<strong>먹었지만</strong>. 고 da esa boʻlmaydi — shuning "
                       "uchun 먹었고 gʻalati. Toʻrtinchisi zamonsiz.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["비싸지만 하지만 샀어요.", "비싸요 지만 샀어요.",
                    "비싸지만 샀어요.", "비싸고 하지만 샀어요."],
        "correct": "비싸지만 샀어요.",
        "explanation": "<p>Bittasini tanlang: <strong>비싸지만 샀어요</strong> "
                       "yoki <strong>비싸요. 하지만 샀어요</strong>. Ikkalasini "
                       "birga ishlatish — “lekin lekin” degani.</p>",
    },
    {
        "text": "<p><strong>어렵지만 재미있어요</strong> gapida soʻzlovchi asosan "
                "nima demoqchi?</p>",
        "choices": ["Til qiyin — shikoyat qilyapti",
                    "Til qiziqarli — ijobiy fikr",
                    "Tilni tashlamoqchi",
                    "Til haqida hech qanday fikri yoʻq"],
        "correct": "Til qiziqarli — ijobiy fikr",
        "explanation": "<p>지만 <strong>ikkinchi qismga urgʻu beradi</strong>. "
                       "Tartibni almashtiring — fikr ham oʻzgaradi: 재미있지만 "
                       "어려워요 endi shikoyatga aylanadi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda <strong>xato bor</strong>?</p>",
        "choices": ["이 옷은 예쁘지만 비싸요.", "한국어는 어렵으지만 재미있어요.",
                    "밥을 먹었지만 배고파요.", "저는 학생이지만 일도 해요."],
        "correct": "한국어는 어렵으지만 재미있어요.",
        "explanation": "<p>지만 da <strong>으 yoʻq</strong>: <s>어렵으지만</s> → "
                       "<strong>어렵지만</strong>. Qolgan uchtasi toʻgʻri "
                       "yasalgan.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["어제 한국에 가지만 친구를 못 만났어요.",
                    "어제 한국에 갔지만 친구를 못 만났어요.",
                    "어제 한국에 갔고지만 친구를 못 만났어요.",
                    "어제 한국에 갔지만 친구를 못 만나요."],
        "correct": "어제 한국에 갔지만 친구를 못 만났어요.",
        "explanation": "<p>어제 — oʻtgan zamon, shuning uchun ikkala tomon ham "
                       "oʻtgan zamonda: <strong>갔지만 … 못 만났어요</strong>. "
                       "Birinchisida zamon yoʻq, oxirgisida oxirgi feʼl hozirgi "
                       "zamonda qolib ketgan.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 그 영화 어땠어요?<br>나: ___</strong></p>",
        "choices": ["길었지만 재미있었어요.", "길고 재미있었어요지만.",
                    "길지만 재미있었어요만.", "길었고 재미있었어요지만."],
        "correct": "길었지만 재미있었어요.",
        "explanation": "<p>Kino allaqachon koʻrilgan — ikkala tomon ham oʻtgan "
                       "zamonda: <strong>길었지만 재미있었어요</strong>. 지만 "
                       "oʻzakka yopishadi, gap oxiriga emas.</p>",
    },
    {
        "text": "<p>“Kecha sovuq edi, lekin bugun issiq” — qaysi gap toʻgʻri?</p>",
        "choices": ["어제는 춥었지만 오늘은 덥어요.",
                    "어제는 추웠지만 오늘은 더워요.",
                    "어제는 추웠고 오늘은 덥어요.",
                    "어제는 추워지만 오늘은 더워요."],
        "correct": "어제는 추웠지만 오늘은 더워요.",
        "explanation": "<p>춥다 → 추웠 (ㅂ → 우) + 지만, 덥다 → 더워요. Uchta "
                       "dars bitta gapda: PK-32 (notoʻgʻri feʼl), PK-20 (oʻtgan "
                       "zamon), PK-34 (지만).</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-32 Mashq: Notoʻgʻri feʼllar 1: ㅂ, ㄷ, 으",
        "description": "20 savol — ㅂ → 우, ㄷ → ㄹ, 으 tushishi va oʻzgarish "
                       "qachon boʻlmasligi.",
        "tutorial":    "PK-32:",
        "level":       "medium",
        "questions":   Q_PK32,
    },
    {
        "title":       "PK-33 Mashq: 고 — sanash va ketma-ketlik",
        "description": "20 savol — 고 ning ikki maʼnosi, zamonning oʻrni, 이고 "
                       "va notoʻgʻri feʼllar bilan xatti-harakati.",
        "tutorial":    "PK-33:",
        "level":       "medium",
        "questions":   Q_PK33,
    },
    {
        "title":       "PK-34 Mashq: 지만 — qarama-qarshilik",
        "description": "20 savol — 지만 ning yasalishi, zamon 지만 dan oldin, "
                       "이지만, 하지만 va 고 bilan farqi.",
        "tutorial":    "PK-34:",
        "level":       "medium",
        "questions":   Q_PK34,
    },
]
