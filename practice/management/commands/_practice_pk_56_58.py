# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-56 … PK-58.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_56_58.py --master=prime \\
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
# PK-56 — Majhul nisbat: -이/히/리/기- va 아/어지다
# =====================================================================

Q_PK56 = [
    # 1–5 tanish
    {
        "text": "<p>Majhul nisbat nima uchun ishlatiladi?</p>",
        "choices": ["Ishni boshqa odam qildirganini koʻrsatish uchun",
                    "Ish bajaruvchisi emas, ishning oʻzi muhim boʻlganda",
                    "Kelasi zamonni bildirish uchun",
                    "Buyruq berish uchun"],
        "correct": "Ish bajaruvchisi emas, ishning oʻzi muhim boʻlganda",
        "explanation": "<p>“Eshik <strong>ochildi</strong>” — kim ochgani "
                       "aytilmaydi. Oʻzbek tilida ham majhul nisbat aynan "
                       "shu ish uchun.</p>",
    },
    {
        "text": "<p><strong>열다</strong> ning majhul shakli qaysi?</p>",
        "choices": ["열리다", "열이다", "열히다", "열기다"],
        "correct": "열리다",
        "explanation": "<p>Oʻzak <strong>ㄹ</strong> bilan tugagan → "
                       "<strong>리</strong> qoʻshimchasi: 문이 열려요.</p>",
    },
    {
        "text": "<p><strong>듣다</strong> ning majhul shakli qaysi?</p>",
        "choices": ["듣히다", "듣이다", "들리다", "듣기다"],
        "correct": "들리다",
        "explanation": "<p>듣다 — ㄷ notoʻgʻri feʼli (PK-32): oʻzak "
                       "<strong>들</strong> boʻladi, keyin ㄹ dan keyin "
                       "리 keladi → <strong>들리다</strong>.</p>",
    },
    {
        "text": "<p>Gap majhulga oʻtganda <strong>을/를</strong> nimaga "
                "aylanadi?</p>",
        "choices": ["이/가", "은/는", "에게", "의"],
        "correct": "이/가",
        "explanation": "<p>Toʻldiruvchi ega boʻlib qoladi: 문<strong>을</strong> "
                       "열었어요 → 문<strong>이</strong> 열렸어요.</p>",
    },
    {
        "text": "<p><strong>하다</strong> bilan tugaydigan feʼllar majhulga "
                "qaysi soʻz bilan oʻtadi?</p>",
        "choices": ["시키다", "버리다", "지다", "되다"],
        "correct": "되다",
        "explanation": "<p>시작하다 → <strong>시작되다</strong>, 준비하다 → "
                       "준비되다, 사용하다 → 사용되다.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 문이 <strong>______</strong> (열다).</p>",
        "choices": ["열었어요", "열렸어요", "열어졌어요", "열히었어요"],
        "correct": "열렸어요",
        "explanation": "<p>열리다 + 었어요 → <strong>열렸어요</strong>. "
                       "열었어요 boʻlsa “men ochdim” degani — u majhul "
                       "emas.</p>",
    },
    {
        "text": "<p>Toʻldiring: 창문이 바람<strong>______</strong> 닫혔어요.</p>",
        "choices": ["에", "에게", "한테", "을"],
        "correct": "에",
        "explanation": "<p>바람 (shamol) — jonsiz, shuning uchun "
                       "<strong>에</strong>. Odam yoki hayvon boʻlganda "
                       "에게/한테 ishlatiladi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 쥐가 고양이<strong>______</strong> 잡혔어요.</p>",
        "choices": ["에", "가", "에게", "를"],
        "correct": "에게",
        "explanation": "<p>고양이 — jonli, shuning uchun <strong>에게</strong> "
                       "(yoki 한테). Bitta gapda ikkita 가 boʻlmaydi.</p>",
    },
    {
        "text": "<p><strong>만들다</strong> ning majhul shakli qaysi?</p>",
        "choices": ["만들리다", "만들어지다", "만들히다", "만들되다"],
        "correct": "만들어지다",
        "explanation": "<p>만들다 ning 이/히/리/기 shakli yoʻq — shunday "
                       "feʼllar uchun <strong>아/어지다</strong> yoʻli "
                       "ochiq: 이 빵은 우유로 만들어져요.</p>",
    },
    {
        "text": "<p>Toʻldiring: 갑자기 불이 <strong>______</strong> (끄다).</p>",
        "choices": ["껐어요", "꺼졌어요", "끄었어요", "꺼리었어요"],
        "correct": "꺼졌어요",
        "explanation": "<p>끄다 → 꺼지다 → <strong>꺼졌어요</strong> "
                       "(chiroq oʻzi oʻchdi). 껐어요 boʻlsa “men oʻchirdim” "
                       "degani.</p>",
    },
    {
        "text": "<p>Toʻldiring: 수업이 아홉 시에 <strong>______</strong> "
                "(시작하다).</p>",
        "choices": ["시작해요", "시작시켜요", "시작돼요", "시작해져요"],
        "correct": "시작돼요",
        "explanation": "<p>Dars <em>oʻzi</em> boshlanadi → majhul → "
                       "<strong>시작돼요</strong>. 시작해요 boʻlsa kimdir "
                       "boshlayotgan boʻladi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 길이 많이 <strong>______</strong> (막다).</p>",
        "choices": ["막았어요", "막혔어요", "막아졌어요", "막되었어요"],
        "correct": "막혔어요",
        "explanation": "<p>막다 → <strong>막히다</strong>. 길이 막혔어요 = "
                       "“yoʻl tiqilib qoldi” — har kuni eshitiladigan "
                       "gap.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Farqi nimada? <strong>산을 봐요</strong> / "
                "<strong>산이 보여요</strong></p>",
        "choices": ["Ikkalasi bir xil",
                    "Birinchisi — men qarayman, ikkinchisi — togʻ koʻrinadi",
                    "Birinchisi oʻtgan zamon, ikkinchisi hozirgi",
                    "Birinchisi hurmatli shakl"],
        "correct": "Birinchisi — men qarayman, ikkinchisi — togʻ koʻrinadi",
        "explanation": "<p>보다 — men qilayotgan ish (toʻldiruvchi 산<strong>을"
                       "</strong>). 보이다 — majhul: togʻ <em>oʻzi</em> "
                       "koʻrinadi (ega 산<strong>이</strong>).</p>",
    },
    {
        "text": "<p><strong>감기에 걸렸어요</strong> nima degani?</p>",
        "choices": ["Shamollab qoldim", "Shamolladim deb oʻyladim",
                    "Shamollashdan qoʻrqaman", "Shamol esdi"],
        "correct": "Shamollab qoldim",
        "explanation": "<p>걸리다 — 걸다 ning majhuli, lekin bu iborada "
                       "“kasallikka ilinmoq” maʼnosida qotib qolgan. "
                       "걸리다 vaqt haqida ham ishlatiladi: 30분 "
                       "걸려요.</p>",
    },
    {
        "text": "<p><strong>날씨가 추워졌어요</strong> — bu majhul nisbatmi?</p>",
        "choices": ["Ha, 지다 hamma joyda majhul yasaydi",
                    "Yoʻq — 춥다 sifat, bu yerda 지다 “…lashib bormoq” "
                    "degani",
                    "Ha, chunki ega bor",
                    "Yoʻq, chunki oʻtgan zamon"],
        "correct": "Yoʻq — 춥다 sifat, bu yerda 지다 “…lashib bormoq” degani",
        "explanation": "<p><strong>Feʼl + 지다</strong> — majhul "
                       "(만들어지다). <strong>Sifat + 지다</strong> — "
                       "oʻzgarish: 좋아지다 (yaxshilanmoq), 추워지다 "
                       "(sovib bormoq).</p>",
    },
    {
        "text": "<p>“Bu kitob doʻkonda yaxshi sotiladi” — qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["이 책은 서점에서 잘 팔아요",
                    "이 책은 서점에서 잘 팔려요",
                    "이 책은 서점에서 잘 팔히어요",
                    "이 책은 서점을 잘 팔려요"],
        "correct": "이 책은 서점에서 잘 팔려요",
        "explanation": "<p>Kitob <em>sotiladi</em> — majhul: 팔다 → "
                       "<strong>팔리다</strong>. 팔아요 boʻlsa “men "
                       "sotaman” degani.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>문을 열렸어요.</strong></p>",
        "choices": ["문을 → 문이", "열렸어요 → 열었어요",
                    "문을 → 문에", "Xato yoʻq"],
        "correct": "문을 → 문이",
        "explanation": "<p>Majhul feʼlda toʻldiruvchi qolmaydi — "
                       "을/를 <strong>이/가</strong>ga aylanadi: "
                       "<strong>문이 열렸어요</strong>.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>저기 산이 보여져요.</strong></p>",
        "choices": ["산이 → 산을", "보여져요 → 보여요",
                    "보여져요 → 봐져요", "Xato yoʻq"],
        "correct": "보여져요 → 보여요",
        "explanation": "<p>보이다 <em>allaqachon</em> majhul. Ustiga yana "
                       "아/어지다 qoʻshilsa ikki qavat majhul boʻladi — "
                       "koreys tilida bunday qilinmaydi.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Deraza shamoldan yopildi” — qaysi biri toʻgʻri?</p>",
        "choices": ["창문을 바람에 닫혔어요", "창문이 바람에게 닫혔어요",
                    "창문이 바람에 닫혔어요", "창문이 바람에 닫았어요"],
        "correct": "창문이 바람에 닫혔어요",
        "explanation": "<p>Ega — 창문<strong>이</strong>, jonsiz bajaruvchi "
                       "— 바람<strong>에</strong>, majhul feʼl — "
                       "<strong>닫혔어요</strong>.</p>",
    },
    {
        "text": "<p><strong>가:</strong> 왜 늦었어요?</p>"
                "<p><strong>나:</strong> ___</p>",
        "choices": ["길을 막았어요", "길이 막혔어요",
                    "길이 막았어요", "길을 막혀졌어요"],
        "correct": "길이 막혔어요",
        "explanation": "<p>“Yoʻl tiqilib qoldi” — yoʻlni men toʻsganim "
                       "yoʻq, shuning uchun majhul: 길<strong>이</strong> "
                       "<strong>막혔어요</strong>.</p>",
    },
]


# =====================================================================
# PK-57 — Orttirma nisbat: -이/히/리/기/우/구/추- va 게 하다
# =====================================================================

Q_PK57 = [
    # 1–5 tanish
    {
        "text": "<p>Orttirma nisbat nimani bildiradi?</p>",
        "choices": ["Ish oʻz-oʻzidan boʻlganini",
                    "Ishni boshqa odam qildirganini",
                    "Ish tugaganini",
                    "Ish hali boshlanmaganini"],
        "correct": "Ishni boshqa odam qildirganini",
        "explanation": "<p>Oʻzbekchada -tir-, -dir-, -t-: “uygʻo<strong>t"
                       "</strong>di”, “ye<strong>dir</strong>di”. "
                       "Koreyschada 이/히/리/기/우/구/추.</p>",
    },
    {
        "text": "<p><strong>먹다</strong> ning orttirma shakli qaysi?</p>",
        "choices": ["먹히다", "먹이다", "먹리다", "먹우다"],
        "correct": "먹이다",
        "explanation": "<p><strong>먹이다</strong> — “yedirmoq”. Diqqat: "
                       "먹<strong>히</strong>다 — bu majhul (“yeyiladi”), "
                       "PK-56 dan.</p>",
    },
    {
        "text": "<p><strong>자다</strong> ning orttirma shakli qaysi?</p>",
        "choices": ["자이다", "잘리다", "재우다", "자히다"],
        "correct": "재우다",
        "explanation": "<p>자다 → <strong>재우다</strong> (uxlatmoq) — "
                       "우 qoʻshimchasi. Juftlik: 깨다 → 깨우다 "
                       "(uygʻotmoq).</p>",
    },
    {
        "text": "<p><strong>입다</strong> ning orttirma shakli qaysi?</p>",
        "choices": ["입히다", "입이다", "입리다", "입추다"],
        "correct": "입히다",
        "explanation": "<p><strong>입히다</strong> — “kiydirmoq”: "
                       "아이에게 옷을 입혀요.</p>",
    },
    {
        "text": "<p><strong>하다</strong> feʼllari orttirmaga qaysi soʻz "
                "bilan oʻtadi?</p>",
        "choices": ["되다", "지다", "시키다", "버리다"],
        "correct": "시키다",
        "explanation": "<p>공부하다 → <strong>공부시키다</strong>. Majhul "
                       "tomonida 되다 edi (공부되다) — ikkalasini "
                       "yonma-yon eslang.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 엄마가 아이<strong>______</strong> 밥을 "
                "먹여요.</p>",
        "choices": ["를", "에게", "이", "에서"],
        "correct": "에게",
        "explanation": "<p>밥 allaqachon 을 olgan. Bitta gapda ikkita "
                       "을/를 boʻlmaydi, shuning uchun odam "
                       "<strong>에게</strong> (yoki 한테) oladi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 언니가 동생<strong>______</strong> 깨웠어요.</p>",
        "choices": ["이", "에게", "을", "에"],
        "correct": "을",
        "explanation": "<p>깨다 da toʻldiruvchi yoʻq edi, shuning uchun "
                       "orttirmada odam <strong>을/를</strong> oladi. "
                       "Xuddi 자다 → 동생을 재웠어요 kabi.</p>",
    },
    {
        "text": "<p><strong>알다</strong> ning orttirma shakli va maʼnosi?</p>",
        "choices": ["알리다 — bildirmoq", "알이다 — bilmoq",
                    "알히다 — bilinmoq", "알우다 — bilishtirmoq"],
        "correct": "알리다 — bildirmoq",
        "explanation": "<p>Oʻzak ㄹ bilan tugagan → <strong>리</strong>: "
                       "친구에게 소식을 알렸어요 (doʻstimga xabar "
                       "berdim).</p>",
    },
    {
        "text": "<p><strong>웃다</strong> ning orttirma shakli qaysi?</p>",
        "choices": ["웃이다", "웃히다", "웃리다", "웃기다"],
        "correct": "웃기다",
        "explanation": "<p>Oʻzak ㅅ bilan tugagan → <strong>기</strong>: "
                       "웃기다 (kuldirmoq). 그 영화가 정말 웃겨요.</p>",
    },
    {
        "text": "<p>“Onasi Jasurga xonani tozalattirdi” — qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["어머니가 자스루르에게 방을 청소했어요",
                    "어머니가 자스루르에게 방을 청소하게 했어요",
                    "어머니가 자스루르를 방을 청소해요",
                    "어머니가 자스루르에게 방을 청소되었어요"],
        "correct": "어머니가 자스루르에게 방을 청소하게 했어요",
        "explanation": "<p>청소하다 ning 이/히/리/기 shakli yoʻq → "
                       "<strong>게 하다</strong> ishlatiladi (yoki "
                       "청소시켰어요).</p>",
    },
    {
        "text": "<p>Toʻldiring: 어머니가 아기를 <strong>______</strong> "
                "(자다).</p>",
        "choices": ["자요", "재요", "재워요", "잤어요"],
        "correct": "재워요",
        "explanation": "<p>자다 → 재우다 → <strong>재워요</strong>. "
                       "우 qoʻshimchasi tushib qolmaydi.</p>",
    },
    {
        "text": "<p><strong>타다</strong> ning orttirma shakli qaysi?</p>",
        "choices": ["태우다", "타이다", "탈리다", "타추다"],
        "correct": "태우다",
        "explanation": "<p><strong>태우다</strong> — “mindirmoq”: "
                       "친구를 차에 태웠어요 (doʻstimni mashinaga "
                       "mindirdim).</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Farqi nimada? <strong>동생이 잤어요</strong> / "
                "<strong>동생을 재웠어요</strong></p>",
        "choices": ["Ikkalasi bir xil",
                    "Birinchisi — ukam uxladi, ikkinchisi — ukamni uxlatdim",
                    "Birinchisi hurmatli shakl",
                    "Ikkinchisi kelasi zamon"],
        "correct": "Birinchisi — ukam uxladi, ikkinchisi — ukamni uxlatdim",
        "explanation": "<p>자다 — ish oʻzidan. 재우다 — men qildirdim. "
                       "Qoʻshimcha ham oʻzgargan: 동생<strong>이</strong> "
                       "→ 동생<strong>을</strong>.</p>",
    },
    {
        "text": "<p><strong>제가 친구에게 사진을 보여요</strong> — bu "
                "majhulmi yoki orttirma?</p>",
        "choices": ["Majhul — rasm koʻrinadi", "Orttirma — rasm koʻrsataman",
                    "Ikkalasi ham emas", "Kontekstdan bilib boʻlmaydi"],
        "correct": "Orttirma — rasm koʻrsataman",
        "explanation": "<p>Belgisi — 사진<strong>을</strong>, yaʼni "
                       "toʻldiruvchi bor. 산<strong>이</strong> 보여요 da "
                       "toʻldiruvchi yoʻq — u majhul.</p>",
    },
    {
        "text": "<p>Farqi nimada? <strong>밥을 먹여요</strong> / "
                "<strong>밥을 먹게 해요</strong></p>",
        "choices": ["Birinchisi bevosita (qoʻli bilan yediradi), ikkinchisi "
                    "bilvosita (aytdi, ruxsat berdi)",
                    "Birinchisi bilvosita, ikkinchisi bevosita",
                    "Ikkalasi bir xil",
                    "Birinchisi majhul"],
        "correct": "Birinchisi bevosita (qoʻli bilan yediradi), ikkinchisi "
                   "bilvosita (aytdi, ruxsat berdi)",
        "explanation": "<p>먹이다 — onasi qoshiq bilan yediradi. "
                       "먹게 하다 — “ovqatni ye” dedi, bola oʻzi yedi. "
                       "게 하다 har qanday feʼl bilan ishlaydi.</p>",
    },
    {
        "text": "<p><strong>늦추다</strong> nima degani?</p>",
        "choices": ["Kechikmoq", "Kechiktirmoq", "Tezlashtirmoq",
                    "Kutmoq"],
        "correct": "Kechiktirmoq",
        "explanation": "<p>늦다 (kechikmoq) ning orttirmasi — "
                       "<strong>늦추다</strong> (kechiktirmoq): 시험을 "
                       "일주일 늦췄어요. Juftlari: 낮추다, 맞추다.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>엄마가 아이를 밥을 먹여요.</strong></p>",
        "choices": ["아이를 → 아이에게", "밥을 → 밥이",
                    "먹여요 → 먹어요", "Xato yoʻq"],
        "correct": "아이를 → 아이에게",
        "explanation": "<p>Bitta gapda ikkita 을/를 boʻlmaydi. Asl feʼlda "
                       "toʻldiruvchi bor boʻlsa (밥을 먹다), odam "
                       "<strong>에게</strong> oladi.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>선생님이 학생들을 공부시키게 "
                "했어요.</strong></p>",
        "choices": ["공부시키게 했어요 → 공부하게 했어요",
                    "학생들을 → 학생들이",
                    "공부시키게 했어요 → 공부되게 했어요",
                    "Xato yoʻq"],
        "correct": "공부시키게 했어요 → 공부하게 했어요",
        "explanation": "<p>시키다 ham, 게 하다 ham orttirma. Ikkalasini "
                       "birga qoʻysangiz ikki qavat orttirma boʻladi — "
                       "bittasini tanlang: 공부하게 했어요 yoki "
                       "공부시켰어요.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Ona bolaga kiyim kiydiradi” — qaysi biri toʻgʻri?</p>",
        "choices": ["어머니가 아이를 옷을 입혀요",
                    "어머니가 아이에게 옷을 입어요",
                    "어머니가 아이에게 옷을 입혀요",
                    "어머니가 아이가 옷을 입혀요"],
        "correct": "어머니가 아이에게 옷을 입혀요",
        "explanation": "<p>Yangi ega — 어머니<strong>가</strong>, eski ega "
                       "→ 아이<strong>에게</strong>, toʻldiruvchi qoladi "
                       "— 옷<strong>을</strong>, feʼl orttirma — "
                       "<strong>입혀요</strong>.</p>",
    },
    {
        "text": "<p><strong>가:</strong> 동생이 아직 자요?</p>"
                "<p><strong>나:</strong> 아니요, 제가 아까 ___</p>",
        "choices": ["깼어요", "깨웠어요", "깨워졌어요", "깨우게 됐어요"],
        "correct": "깨웠어요",
        "explanation": "<p>“Men uygʻotdim” — orttirma: 깨다 → "
                       "<strong>깨우다</strong>. 깼어요 boʻlsa “men "
                       "uygʻondim” degani.</p>",
    },
]


# =====================================================================
# PK-58 — 아/어 버리다
# =====================================================================

Q_PK58 = [
    # 1–5 tanish
    {
        "text": "<p><strong>아/어 버리다</strong> nimani bildiradi?</p>",
        "choices": ["Ish hali tugamaganini",
                    "Ish butunlay tugaganini va gapiruvchining tuygʻusini",
                    "Ishni boshqa odam qildirganini",
                    "Ish takrorlanishini"],
        "correct": "Ish butunlay tugaganini va gapiruvchining tuygʻusini",
        "explanation": "<p>Oʻzbekcha juftligi — “ye<strong>b qoʻydi</strong>”, "
                       "“keti<strong>b qoldi</strong>”: maʼlumot ustiga "
                       "his ham qoʻshiladi.</p>",
    },
    {
        "text": "<p><strong>버리다</strong> feʼlining asl maʼnosi nima?</p>",
        "choices": ["Tashlamoq", "Olmoq", "Qoldirmoq", "Boshlamoq"],
        "correct": "Tashlamoq",
        "explanation": "<p>쓰레기를 버려요 — axlatni tashlayman. Koʻmakchi "
                       "boʻlganda esa “qilingan ishni tashlab yubordim” "
                       "degan tuygʻu beradi.</p>",
    },
    {
        "text": "<p><strong>하다</strong> bu qolipda qanday shaklga "
                "kiradi?</p>",
        "choices": ["하 버리다", "해 버리다", "하고 버리다", "할 버리다"],
        "correct": "해 버리다",
        "explanation": "<p>버리다 dan oldin feʼl <strong>아/어 shaklida"
                       "</strong> turadi. 하다 ning 아/어 shakli — "
                       "<strong>해</strong>.</p>",
    },
    {
        "text": "<p>Zamon qoʻshimchasi qayerga qoʻshiladi?</p>",
        "choices": ["Asosiy feʼlga", "버리다 ga", "Ikkalasiga",
                    "Gap oxiriga alohida"],
        "correct": "버리다 ga",
        "explanation": "<p>먹어 <strong>버렸</strong>어요 — 버리 + 었 → "
                       "버렸. <s>먹었어 버려요</s> notoʻgʻri.</p>",
    },
    {
        "text": "<p><strong>잃어버리다</strong> nima degani?</p>",
        "choices": ["Esdan chiqarmoq", "Yoʻqotib qoʻymoq",
                    "Tashlab yubormoq", "Topib olmoq"],
        "correct": "Yoʻqotib qoʻymoq",
        "explanation": "<p>지갑을 <strong>잃어버렸어요</strong> — hamyonimni "
                       "yoʻqotib qoʻydim. Bu soʻz 버리다 bilan "
                       "<strong>qoʻshib</strong> yoziladi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 동생이 케이크를 다 <strong>______</strong> "
                "버렸어요. (먹다)</p>",
        "choices": ["먹", "먹어", "먹고", "먹은"],
        "correct": "먹어",
        "explanation": "<p>먹다 ning oxirgi unlisi ㅓ → <strong>어</strong>: "
                       "먹어 버렸어요.</p>",
    },
    {
        "text": "<p>Toʻldiring: 친구가 인사도 안 하고 <strong>______</strong> "
                "버렸어요. (가다)</p>",
        "choices": ["가", "가서", "가고", "간"],
        "correct": "가",
        "explanation": "<p>가다 ning oxirgi unlisi ㅏ → 가 + 아 = "
                       "<strong>가</strong> (qoʻshilib ketadi): 가 "
                       "버렸어요.</p>",
    },
    {
        "text": "<p>Toʻldiring: 용돈을 하루 만에 다 <strong>______</strong> "
                "버렸어요. (쓰다)</p>",
        "choices": ["쓰", "써", "쓰고", "쓴"],
        "correct": "써",
        "explanation": "<p>쓰다 — ㅡ notoʻgʻri feʼli (PK-32): ㅡ tushadi va "
                       "어 keladi → <strong>써</strong>.</p>",
    },
    {
        "text": "<p>“Kitobni oʻqib tashladim” — qaysi biri toʻgʻri?</p>",
        "choices": ["책을 다 읽 버렸어요", "책을 다 읽어 버렸어요",
                    "책을 다 읽고 버렸어요", "책을 다 읽어졌어요"],
        "correct": "책을 다 읽어 버렸어요",
        "explanation": "<p>읽다 → 읽<strong>어</strong> 버렸어요. "
                       "<strong>다</strong> (“hammasi”) bu qolip bilan "
                       "juda koʻp yuradi.</p>",
    },
    {
        "text": "<p>“Ismini esdan chiqaribman” — qaysi biri toʻgʻri?</p>",
        "choices": ["이름을 잊어버렸어요", "이름을 잊버렸어요",
                    "이름을 잊어졌어요", "이름을 잊게 했어요"],
        "correct": "이름을 잊어버렸어요",
        "explanation": "<p><strong>잊어버리다</strong> — 잃어버리다 kabi "
                       "qoʻshib yoziladigan bitta soʻz.</p>",
    },
    {
        "text": "<p>Bu qolip koʻpincha qaysi soʻz bilan birga keladi?</p>",
        "choices": ["아직", "다", "조금", "가끔"],
        "correct": "다",
        "explanation": "<p><strong>다</strong> = “hammasi, butunlay”. "
                       "다 먹어 버렸어요, 다 써 버렸어요 — ikkalasi "
                       "bir-birini kuchaytiradi.</p>",
    },
    {
        "text": "<p>Doʻstlar orasida (반말) <strong>먹어 버렸어</strong> "
                "qanday aytiladi?</p>",
        "choices": ["먹어버렸어", "먹버렸어", "먹어 버려어", "먹었어 버려"],
        "correct": "먹어버렸어",
        "explanation": "<p>Kundalik nutqda 아/어 va 버리다 bitta soʻzday "
                       "qoʻshilib ketadi: 야, 내 빵 <strong>먹어버렸어"
                       "</strong>?</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Farqi nimada? <strong>케이크를 먹었어요</strong> / "
                "<strong>케이크를 먹어 버렸어요</strong></p>",
        "choices": ["Ikkalasi bir xil",
                    "Birinchisi oddiy maʼlumot, ikkinchisida tuygʻu ham bor",
                    "Birinchisi kelasi zamon",
                    "Ikkinchisi hurmatliroq"],
        "correct": "Birinchisi oddiy maʼlumot, ikkinchisida tuygʻu ham bor",
        "explanation": "<p>먹었어요 — shunchaki yedim. 먹어 버렸어요 — "
                       "hammasi tugadi, endi yoʻq, va bu menga taʼsir "
                       "qildi (afsus yoki yengillik).</p>",
    },
    {
        "text": "<p><strong>숙제를 다 해 버렸어요!</strong> — bu yerda qaysi "
                "tuygʻu bor?</p>",
        "choices": ["Afsus", "Yengillik", "Qoʻrquv", "Shubha"],
        "correct": "Yengillik",
        "explanation": "<p>Ogʻir ish tugadi, yelkadan yuk tushdi — "
                       "<strong>시원함</strong>. Undov belgisi ham shuni "
                       "aytib turibdi.</p>",
    },
    {
        "text": "<p><strong>친구가 인사도 안 하고 가 버렸어요.</strong> — "
                "bu yerda qaysi tuygʻu bor?</p>",
        "choices": ["Yengillik", "Xursandchilik", "Afsus va xafalik",
                    "Hech qanday tuygʻu yoʻq"],
        "correct": "Afsus va xafalik",
        "explanation": "<p>“Xayrlashmasdan ketib qoldi” — soʻzlovchi buni "
                       "istamagan. Qaysi tuygʻu ekanini faqat kontekst "
                       "aytadi.</p>",
    },
    {
        "text": "<p>Nima uchun <strong>날씨가 추워 버렸어요</strong> "
                "notoʻgʻri?</p>",
        "choices": ["Zamon xato",
                    "춥다 — sifat, 버리다 esa faqat harakat feʼllari bilan "
                    "keladi",
                    "날씨 ega boʻlolmaydi",
                    "버리다 dan oldin 고 kerak"],
        "correct": "춥다 — sifat, 버리다 esa faqat harakat feʼllari bilan "
                   "keladi",
        "explanation": "<p>Sifatning oʻzgarishi uchun PK-56 dagi "
                       "<strong>아/어지다</strong> bor: "
                       "<strong>추워졌어요</strong>.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>숙제를 다 하 버렸어요.</strong></p>",
        "choices": ["하 버렸어요 → 해 버렸어요", "하 버렸어요 → 할 버렸어요",
                    "숙제를 → 숙제가", "Xato yoʻq"],
        "correct": "하 버렸어요 → 해 버렸어요",
        "explanation": "<p>버리다 dan oldin feʼl <strong>아/어 shaklida"
                       "</strong> turishi shart. 하다 → <strong>해</strong>.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>용돈을 다 써 버려었어요.</strong></p>",
        "choices": ["써 → 쓰", "버려었어요 → 버렸어요",
                    "용돈을 → 용돈이", "Xato yoʻq"],
        "correct": "버려었어요 → 버렸어요",
        "explanation": "<p>버리 + 었 → <strong>버렸</strong>. ㅣ va 었 "
                       "qoʻshilib 렸 boʻladi.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Hamyonimni yoʻqotib qoʻydim” — qaysi biri toʻgʻri?</p>",
        "choices": ["지갑이 잃어버렸어요", "지갑을 잃어 버려요",
                    "지갑을 잃어버렸어요", "지갑을 잃게 했어요"],
        "correct": "지갑을 잃어버렸어요",
        "explanation": "<p>Toʻldiruvchi 지갑<strong>을</strong>, feʼl "
                       "oʻtgan zamonda va qoʻshib yoziladi — "
                       "<strong>잃어버렸어요</strong>.</p>",
    },
    {
        "text": "<p><strong>가:</strong> 케이크가 어디 있어요?</p>"
                "<p><strong>나:</strong> ___</p>",
        "choices": ["동생이 다 먹어 버렸어요", "동생이 다 먹어졌어요",
                    "동생이 다 먹이었어요", "동생이 다 먹게 했어요"],
        "correct": "동생이 다 먹어 버렸어요",
        "explanation": "<p>“Ukam hammasini yeb qoʻyibdi” — tort tugadi, "
                       "va gapiruvchi bundan afsusda. Aynan "
                       "<strong>아/어 버리다</strong> ning oʻrni.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-56 Mashq: Majhul nisbat — 이/히/리/기 va 아/어지다",
        "description": "20 savol — toʻrtta qoʻshimcha, gapdagi qoʻshimchalar "
                       "oʻzgarishi, 아/어지다 va 하다 → 되다 yoʻli.",
        "tutorial":    "PK-56:",
        "level":       "medium",
        "questions":   Q_PK56,
    },
    {
        "title":       "PK-57 Mashq: Orttirma nisbat — 이/히/리/기/우/구/추 va 게 하다",
        "description": "20 savol — yettita qoʻshimcha, 에게 va 을/를 tanlash, "
                       "게 하다, 시키다 va ikki maʼnoli feʼllar.",
        "tutorial":    "PK-57:",
        "level":       "medium",
        "questions":   Q_PK57,
    },
    {
        "title":       "PK-58 Mashq: 아/어 버리다 — tugallanish va his-tuygʻu",
        "description": "20 savol — yasalishi, zamonning oʻrni, ikki tuygʻu, "
                       "잃어버리다/잊어버리다 va qachon ishlatmaslik.",
        "tutorial":    "PK-58:",
        "level":       "medium",
        "questions":   Q_PK58,
    },
]
