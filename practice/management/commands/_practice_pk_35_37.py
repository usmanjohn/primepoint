# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-35 … PK-37.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_35_37.py --master=prime \\
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
# PK-35 — 아/어서
# =====================================================================

Q_PK35 = [
    # 1–5 tanish
    {
        "text": "<p><strong>아/어서</strong> ning asosiy maʼnosi qaysi?</p>",
        "choices": ["…gani uchun (sabab)", "…lekin (qarama-qarshilik)",
                    "agar …sa (shart)", "…moqchiman (xohish)"],
        "correct": "…gani uchun (sabab)",
        "explanation": "<p><strong>아/어서</strong> oldingi qismni sabab, keyingi "
                       "qismni natija qiladi: 배가 아파서 병원에 갔어요. Ikkinchi "
                       "vazifasi — bogʻliq ketma-ketlik (빵을 사서 먹었어요).</p>",
    },
    {
        "text": "<p><strong>가다</strong> ning 아/어서 shakli qaysi?</p>",
        "choices": ["가아서", "가서", "가어서", "갔서"],
        "correct": "가서",
        "explanation": "<p>아/어요 shaklini oling (가요) va 요 oʻrniga <strong>서</strong> "
                       "qoʻying: <strong>가서</strong>. Bu butun darsning qolipi.</p>",
    },
    {
        "text": "<p>아/어서 dan oldin oʻtgan zamon qoʻyiladimi?</p>",
        "choices": ["Ha, har doim", "Yoʻq, hech qachon",
                    "Faqat sifatlar bilan", "Faqat inkorda"],
        "correct": "Yoʻq, hech qachon",
        "explanation": "<p><s>아팠어서</s> degan shakl yoʻq — toʻgʻrisi "
                       "<strong>아파서</strong>. Zamon faqat oxirgi feʼlda turadi "
                       "va u butun gapni oʻtmishga oladi.</p>",
    },
    {
        "text": "<p>아/어서 dan keyin nima <strong>kelmaydi</strong>?</p>",
        "choices": ["Buyruq va taklif", "Oʻtgan zamon", "Inkor", "Savol"],
        "correct": "Buyruq va taklif",
        "explanation": "<p><s>배가 아파서 병원에 가세요</s> notoʻgʻri. Sabab "
                       "shunchaki tushuntiriladi, undan buyruq chiqarilmaydi. "
                       "Darak, savol va inkor esa bemalol.</p>",
    },
    {
        "text": "<p><strong>만나서 반갑습니다</strong> qaysi qolipda yasalgan?</p>",
        "choices": ["만나다 + 아/어서", "만나다 + 고", "만나다 + 지만",
                    "만나다 + (으)세요"],
        "correct": "만나다 + 아/어서",
        "explanation": "<p>만나다 → 만나요 → <strong>만나서</strong>. PK-9 dagi "
                       "tanishuv iborasi aslida shu darsning qolipi — “uchrashib, "
                       "xursandman”.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>배가 ___ 병원에 갔어요.</strong> — 아프다</p>",
        "choices": ["아팠어서", "아프어서", "아파서", "아프서"],
        "correct": "아파서",
        "explanation": "<p>으 tushadi va 아 qoʻshiladi (oldingi unli ㅏ): 아파 + 서 "
                       "= <strong>아파서</strong>. <s>아팠어서</s> — zamon "
                       "qoʻyilmaydi.</p>",
    },
    {
        "text": "<p><strong>바쁘다</strong> ning 아/어서 shakli qaysi?</p>",
        "choices": ["바빠서", "바쁘어서", "바빴어서", "바뻐서"],
        "correct": "바빠서",
        "explanation": "<p>아/어요 shakli 바빠요, demak <strong>바빠서</strong>. "
                       "아/어서 unli bilan boshlangani uchun 으 tuslanishi ishga "
                       "tushadi (PK-32).</p>",
    },
    {
        "text": "<p><strong>듣다</strong> ning 아/어서 shakli qaysi?</p>",
        "choices": ["듣어서", "듣아서", "들어서", "듣고서"],
        "correct": "들어서",
        "explanation": "<p>ㄷ → ㄹ, chunki 아/어서 unli bilan boshlanadi: "
                       "<strong>들어서</strong>. Solishtiring: 듣<strong>고</strong>, "
                       "듣<strong>지만</strong> — u yerda oʻzgarmagan edi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>시간이 ___ 숙제를 못 했어요.</strong> — 없다</p>",
        "choices": ["없고", "없지만", "없어서", "없으서"],
        "correct": "없어서",
        "explanation": "<p>Sabab koʻrsatilyapti: vaqt yoʻqligi — sabab, vazifa "
                       "qilinmagani — natija. 없다 → <strong>없어서</strong>. "
                       "Inkor ham sabab boʻlaveradi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>날씨가 ___ 물을 많이 마셔요.</strong> — 덥다</p>",
        "choices": ["덥어서", "더워서", "덥아서", "더우서"],
        "correct": "더워서",
        "explanation": "<p>ㅂ → 우: 덥 → 더우 → 더워 + 서 = "
                       "<strong>더워서</strong>.</p>",
    },
    {
        "text": "<p><strong>학생</strong> ga 아/어서 qanday qoʻshiladi?</p>",
        "choices": ["학생어서", "학생아서", "학생이어서", "학생여서"],
        "correct": "학생이어서",
        "explanation": "<p>Ot + 이다: 받침 bor → <strong>이어서</strong> "
                       "(학생이어서), 받침 yoʻq → <strong>여서</strong> "
                       "(친구여서).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>도서관에 ___ 책을 읽었어요.</strong> — 가다</p>",
        "choices": ["가고", "가서", "갔어서", "가지만"],
        "correct": "가서",
        "explanation": "<p>Kitob <em>oʻsha</em> kutubxonada oʻqilgan — ikki ish "
                       "bogʻlangan, joy ikkinchi qismga koʻchgan. Shuning uchun "
                       "<strong>가서</strong>, 가고 emas.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Qaysi biri toʻgʻri?</p>"
                "<p><strong>빵을 사고 먹었어요</strong> · "
                "<strong>빵을 사서 먹었어요</strong> (“nonni sotib olib yedim”)</p>",
        "choices": ["빵을 사고 먹었어요", "빵을 사서 먹었어요",
                    "Ikkalasi ham bir xil", "Ikkalasi ham notoʻgʻri"],
        "correct": "빵을 사서 먹었어요",
        "explanation": "<p>Yeyilgan non — <em>aynan oʻsha</em> non, demak ikki ish "
                       "bogʻlangan: <strong>사서 먹었어요</strong>. 사고 deyilsa, "
                       "non yeyishga aloqasiz boʻlib qolardi.</p>",
    },
    {
        "text": "<p>Qaysi gapda zamon <strong>toʻgʻri</strong> qoʻyilgan?</p>",
        "choices": ["어제 아팠어서 못 갔어요.", "어제 아파서 못 갔어요.",
                    "어제 아파서 못 가요.", "어제 아팠어서 못 가요."],
        "correct": "어제 아파서 못 갔어요.",
        "explanation": "<p>아/어서 dan oldin zamon yoʻq (아파서), oxirgi feʼlda esa "
                       "bor (못 갔어요). Uchinchi variantda 어제 bilan hozirgi zamon "
                       "toʻqnashib qolgan.</p>",
    },
    {
        "text": "<p>Qaysi bogʻlovchida zamon undan <strong>oldin</strong> "
                "turishi mumkin?</p>",
        "choices": ["고 (ketma-ketlik)", "아/어서", "지만", "Hech qaysisida"],
        "correct": "지만",
        "explanation": "<p><strong>지만</strong> da mumkin: 갔지만, 바빴지만. "
                       "고 (ketma-ketlik) va 아/어서 da esa zamon faqat oxirgi "
                       "feʼlda turadi.</p>",
    },
    {
        "text": "<p>Qaysi gap <strong>notoʻgʻri</strong>?</p>",
        "choices": ["시간이 없어서 못 갔어요.", "너무 바빠서 못 왔어요.",
                    "배가 아파서 병원에 가세요.", "날씨가 더워서 힘들어요."],
        "correct": "배가 아파서 병원에 가세요.",
        "explanation": "<p>아/어서 dan keyin <strong>buyruq kelmaydi</strong>. "
                       "Qolgan uchtasi darak gap, shuning uchun toʻgʻri.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda <strong>xato bor</strong>?</p>",
        "choices": ["친구를 만나서 영화를 봤어요.", "날씨가 덥어서 힘들어요.",
                    "시간이 없어서 못 왔어요.", "학교에 가서 공부해요."],
        "correct": "날씨가 덥어서 힘들어요.",
        "explanation": "<p>아/어서 unli bilan boshlanadi → ㅂ tuslanishi ishga "
                       "tushishi kerak: <s>덥어서</s> → <strong>더워서</strong>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["자수르 씨는 학생어서 바빠요.",
                    "자수르 씨는 학생이어서 바빠요.",
                    "자수르 씨는 학생아서 바빠요.",
                    "자수르 씨는 학생이었어서 바빠요."],
        "correct": "자수르 씨는 학생이어서 바빠요.",
        "explanation": "<p>학생 da 받침 bor → <strong>이어서</strong>. Oxirgi "
                       "variantda esa yana oʻsha xato — 아/어서 dan oldin zamon "
                       "qoʻyilgan.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 왜 안 왔어요?<br>나: ___</strong></p>",
        "choices": ["너무 바빠서 못 왔어요.", "너무 바빴어서 못 왔어요.",
                    "너무 바쁘고 못 왔어요.", "너무 바쁘지만 못 왔어요."],
        "correct": "너무 바빠서 못 왔어요.",
        "explanation": "<p><strong>왜</strong> savoliga javob — sabab, demak "
                       "아/어서. Zamon faqat oxirida: <strong>바빠서 못 "
                       "왔어요</strong>.</p>",
    },
    {
        "text": "<p>“Vaqtim yoʻq, shuning uchun bora olmayman” — qaysi gap "
                "toʻgʻri?</p>",
        "choices": ["시간이 없어서 못 가요.", "시간이 없었어서 못 가요.",
                    "시간이 없고 못 가요.", "시간이 없어서 가지 마세요."],
        "correct": "시간이 없어서 못 가요.",
        "explanation": "<p>없다 → <strong>없어서</strong>, natija qismida esa "
                       "못 가요. Oxirgi variant taqiq bilan tugagani uchun "
                       "notoʻgʻri — 아/어서 dan keyin buyruq kelmaydi.</p>",
    },
]


# =====================================================================
# PK-36 — (으)면
# =====================================================================

Q_PK36 = [
    # 1–5 tanish
    {
        "text": "<p><strong>(으)면</strong> qanday maʼno beradi?</p>",
        "choices": ["agar …sa (shart)", "…gani uchun (sabab)",
                    "…lekin", "…ib (ketma-ketlik)"],
        "correct": "agar …sa (shart)",
        "explanation": "<p><strong>(으)면</strong> hali boʻlmagan, lekin boʻlishi "
                       "mumkin boʻlgan narsani bildiradi: 비가 오면 집에 있을 "
                       "거예요. Ikkinchi maʼnosi — umumiy qoida (봄이 오면 꽃이 "
                       "펴요).</p>",
    },
    {
        "text": "<p>받침 boʻlmagan oʻzakka qaysi shakl qoʻshiladi?</p>",
        "choices": ["으면", "면", "이면", "아면"],
        "correct": "면",
        "explanation": "<p>Oʻzak unli bilan tugasa — <strong>면</strong> "
                       "(가면, 오면). 받침 bor boʻlsa <strong>으면</strong> "
                       "(먹으면, 있으면).</p>",
    },
    {
        "text": "<p><strong>먹다</strong> ning (으)면 shakli qaysi?</p>",
        "choices": ["먹면", "머면", "먹으면", "먹어면"],
        "correct": "먹으면",
        "explanation": "<p>Oʻzak 먹 — 받침 bor, shuning uchun "
                       "<strong>으면</strong>: 먹으면.</p>",
    },
    {
        "text": "<p>(으)면 dan keyin buyruq kela oladimi?</p>",
        "choices": ["Ha, bemalol", "Yoʻq, hech qachon",
                    "Faqat inkor buyruq", "Faqat rasmiy shaklda"],
        "correct": "Ha, bemalol",
        "explanation": "<p><strong>시간이 있으면 오세요</strong> — mutlaqo "
                       "toʻgʻri. Bu 아/어서 dan asosiy farq: u yerda buyruq "
                       "taqiqlangan edi.</p>",
    },
    {
        "text": "<p><strong>만약</strong> nima vazifa bajaradi?</p>",
        "choices": ["Shartni kuchaytiradi — “agar”",
                    "(으)면 ning oʻrnini bosadi",
                    "Inkor yasaydi",
                    "Oʻtgan zamon yasaydi"],
        "correct": "Shartni kuchaytiradi — “agar”",
        "explanation": "<p><strong>만약</strong> gap boshida turadi va shartni aniq "
                       "belgilaydi, lekin (으)면 ni <em>almashtirmaydi</em>: "
                       "만약 비가 오면… Ikkalasi birga ishlaydi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>시간이 ___ 오세요.</strong> — 있다</p>",
        "choices": ["있면", "있으면", "있어면", "있어서"],
        "correct": "있으면",
        "explanation": "<p>있 — 받침 bor → <strong>있으면</strong>. Eʼtibor bering: "
                       "undan keyin buyruq turibdi va bu toʻgʻri. 있어서 boʻlsa "
                       "buyruq kela olmasdi.</p>",
    },
    {
        "text": "<p><strong>만들다</strong> ning (으)면 shakli qaysi?</p>",
        "choices": ["만들면", "만드면", "만들으면", "만듬면"],
        "correct": "만들면",
        "explanation": "<p>ㄹ <em>tushmaydi</em> va 으 ham qoʻshilmaydi: "
                       "<strong>만들면</strong>. ㄹ faqat ㄴ, ㅂ, ㅅ oldida tushadi "
                       "(만드세요, 만듭니다); 면 esa ㅁ bilan boshlanadi.</p>",
    },
    {
        "text": "<p><strong>덥다</strong> ning (으)면 shakli qaysi?</p>",
        "choices": ["덥으면", "덥면", "더우면", "더워면"],
        "correct": "더우면",
        "explanation": "<p>받침 bor → 으 keladi, yaʼni unli — shuning uchun ㅂ "
                       "tuslanishi ishga tushadi: 덥 → 더우 → "
                       "<strong>더우면</strong>.</p>",
    },
    {
        "text": "<p><strong>듣다</strong> ning (으)면 shakli qaysi?</p>",
        "choices": ["듣으면", "들으면", "듣면", "들면"],
        "correct": "들으면",
        "explanation": "<p>으 unli bilan boshlangani uchun ㄷ → ㄹ: "
                       "<strong>들으면</strong>. Solishtiring: 듣<strong>고</strong>, "
                       "듣<strong>지만</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>비가 ___ 집에 있을 거예요.</strong> — 오다</p>",
        "choices": ["오으면", "왔으면", "오면", "와면"],
        "correct": "오면",
        "explanation": "<p>오 — 받침 yoʻq, demak 으 kerak emas: "
                       "<strong>오면</strong>. Natija qismida kelasi zamon juda "
                       "tabiiy — shart hali bajarilmagan.</p>",
    },
    {
        "text": "<p><strong>학생</strong> ga (으)면 qanday qoʻshiladi?</p>",
        "choices": ["학생면", "학생이면", "학생으면", "학생여면"],
        "correct": "학생이면",
        "explanation": "<p>Ot + 이다: 받침 bor → <strong>이면</strong> (학생이면), "
                       "받침 yoʻq → <strong>면</strong> (친구면).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>모르면 저한테 ___</strong> (“Bilmasangiz mendan "
                "soʻrang.”) — 물어보다</p>",
        "choices": ["물어보세요", "물어봐서", "물어보면", "물어보지만"],
        "correct": "물어보세요",
        "explanation": "<p>Shart (모르면) qoʻyilgach, natija qismida buyruq "
                       "keladi: <strong>물어보세요</strong>. (으)면 buyruq bilan "
                       "bemalol ishlaydi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Qaysi biri toʻgʻri?</p>"
                "<p><strong>머리가 아파서 약을 드세요</strong> · "
                "<strong>머리가 아프면 약을 드세요</strong></p>",
        "choices": ["머리가 아파서 약을 드세요", "머리가 아프면 약을 드세요",
                    "Ikkalasi ham toʻgʻri", "Ikkalasi ham notoʻgʻri"],
        "correct": "머리가 아프면 약을 드세요",
        "explanation": "<p>Ikki sabab: bosh hali ogʻrimayapti (bu maslahat), va "
                       "아/어서 dan keyin <strong>buyruq kelmaydi</strong>. "
                       "Shart esa buyruq bilan bemalol ishlaydi.</p>",
    },
    {
        "text": "<p>Boʻlib boʻlgan ish uchun qaysi qolip ishlatiladi?</p>",
        "choices": ["(으)면", "아/어서", "Ikkalasi ham", "Hech qaysisi"],
        "correct": "아/어서",
        "explanation": "<p><strong>Allaqachon boʻlgan</strong> narsa sabab bo‘ladi "
                       "→ 아/어서 (배가 아파서 병원에 갔어요). <strong>Hali "
                       "boʻlmagan</strong> narsa shart → (으)면.</p>",
    },
    {
        "text": "<p>Qaysi gap “Bahor kelganda gullar ochiladi” degani?</p>",
        "choices": ["봄이 오면 꽃이 펴요.", "봄이 와서 꽃이 펴요.",
                    "봄이 오고 꽃이 펴요.", "봄이 오지만 꽃이 펴요."],
        "correct": "봄이 오면 꽃이 펴요.",
        "explanation": "<p>Bu har yili takrorlanadigan umumiy qoida — (으)면 ning "
                       "ikkinchi maʼnosi. Bu yerda “agar” emas, "
                       "“<strong>…ganda</strong>” deb tarjima qilinadi.</p>",
    },
    {
        "text": "<p><strong>바쁘다</strong> ga (으)면 qoʻshilganda oʻzak "
                "oʻzgaradimi?</p>",
        "choices": ["Ha — 바빠면", "Yoʻq — 바쁘면", "Ha — 바쁘으면", "Ha — 바빴으면"],
        "correct": "Yoʻq — 바쁘면",
        "explanation": "<p>바쁘 oʻzagida <strong>받침 yoʻq</strong>, shuning uchun "
                       "으 ham qoʻshilmaydi — oʻzak bilan qoʻshimcha orasida unli "
                       "toʻqnashuvi yoʻq: <strong>바쁘면</strong>.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda <strong>xato bor</strong>?</p>",
        "choices": ["시간이 있으면 같이 영화를 봐요.", "비가 오으면 집에 있어요.",
                    "학생이면 이 책을 살 수 있어요.", "날씨가 더우면 창문을 여세요."],
        "correct": "비가 오으면 집에 있어요.",
        "explanation": "<p>오 — 받침 yoʻq, demak 으 qoʻshilmaydi: "
                       "<s>오으면</s> → <strong>오면</strong>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["만약 시간이 있어요 가요.", "만약 시간이 있으면 갈 거예요.",
                    "만약 시간이 있고 갈 거예요.", "만약 시간이 있어서 가세요."],
        "correct": "만약 시간이 있으면 갈 거예요.",
        "explanation": "<p>만약 oʻzi shart yasamaydi — qoʻshimcha baribir kerak: "
                       "<strong>있으면</strong>. Oxirgi variantda esa 아/어서 dan "
                       "keyin buyruq qoʻyilgan.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 내일 시간 있어요?<br>나: 네. ___</strong></p>",
        "choices": ["시간이 있으면 같이 도서관에 가요.",
                    "시간이 있어서 같이 도서관에 가요.",
                    "시간이 있고 같이 도서관에 가요.",
                    "시간이 있지만 같이 도서관에 가요."],
        "correct": "시간이 있으면 같이 도서관에 가요.",
        "explanation": "<p>Taklif qilinyapti va shart hali bajarilmagan — "
                       "<strong>(으)면</strong>. Taklif ham buyruq kabi 아/어서 "
                       "bilan kelmaydi.</p>",
    },
    {
        "text": "<p>“Koreyaga borsangiz kimchi yeng” — qaysi gap toʻgʻri?</p>",
        "choices": ["한국에 가면 김치를 드세요.", "한국에 가서 김치를 드세요.",
                    "한국에 갔으면 김치를 드세요.", "한국에 가고 김치를 드세요."],
        "correct": "한국에 가면 김치를 드세요.",
        "explanation": "<p>Shart + maslahat — (으)면 ning eng tipik ishlatilishi: "
                       "<strong>가면 … 드세요</strong>. 가서 boʻlsa buyruq kela "
                       "olmasdi.</p>",
    },
]


# =====================================================================
# PK-37 — 보다 / 제일 · 가장
# =====================================================================

Q_PK37 = [
    # 1–5 tanish
    {
        "text": "<p><strong>보다</strong> qanday maʼno beradi?</p>",
        "choices": ["…dan (taqqoslash)", "…ga (yoʻnalish)",
                    "…bilan (birgalik)", "…uchun (maqsad)"],
        "correct": "…dan (taqqoslash)",
        "explanation": "<p><strong>보다</strong> solishtiriladigan narsaga "
                       "yopishadi: 저는 동생<strong>보다</strong> 커요 — “men "
                       "ukamdan kattaman”. Oʻzbekcha “-dan” bilan bir xil.</p>",
    },
    {
        "text": "<p><strong>덜</strong> nima degani?</p>",
        "choices": ["koʻproq", "kamroq", "eng", "juda"],
        "correct": "kamroq",
        "explanation": "<p><strong>덜</strong> — 더 ning teskarisi: 이 옷이 저 "
                       "옷보다 <strong>덜</strong> 비싸요 (“kamroq qimmat”). Uni "
                       "tushirib qoldirsangiz maʼno teskarisiga aylanadi.</p>",
    },
    {
        "text": "<p><strong>제일</strong> va <strong>가장</strong> orasida qanday "
                "farq bor?</p>",
        "choices": ["Maʼnosi bir xil, faqat uslubi boshqa",
                    "제일 — “eng”, 가장 — “kamroq”",
                    "제일 sifat bilan, 가장 feʼl bilan ishlatiladi",
                    "가장 faqat inkorda ishlatiladi"],
        "correct": "Maʼnosi bir xil, faqat uslubi boshqa",
        "explanation": "<p>Ikkalasi ham “eng”. <strong>제일</strong> kundalik "
                       "ogʻzaki nutqda, <strong>가장</strong> yozma va rasmiy "
                       "uslubda koʻproq uchraydi. Birga ishlatilmaydi.</p>",
    },
    {
        "text": "<p><strong>중에서</strong> nima vazifa bajaradi?</p>",
        "choices": ["Doirani belgilaydi — “…lar orasida”",
                    "Sabab koʻrsatadi", "Shart yasaydi", "Inkor yasaydi"],
        "correct": "Doirani belgilaydi — “…lar orasida”",
        "explanation": "<p>과일 <strong>중에서</strong> 사과를 제일 좋아해요 — "
                       "“mevalar orasida”. Joy haqida gapirilsa "
                       "<strong>에서</strong> ishlatiladi: 한국에서 서울이 제일 "
                       "커요.</p>",
    },
    {
        "text": "<p>보다 oldidan 을/를 qoʻyiladimi?</p>",
        "choices": ["Ha, har doim", "Yoʻq, hech qachon",
                    "Faqat jonli otlarda", "Faqat 더 bilan birga"],
        "correct": "Yoʻq, hech qachon",
        "explanation": "<p><s>동생을 보다</s> notoʻgʻri — 보다 qoʻshimcha, otga "
                       "toʻgʻridan-toʻgʻri yopishadi: <strong>동생보다</strong>. "
                       "(Alohida 보다 feʼli ham bor, lekin u “koʻrmoq” degani.)</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>저는 ___ 커요.</strong> (“Men ukamdan kattaman.”) — 동생</p>",
        "choices": ["동생을 보다", "동생보다", "동생에서", "동생하고"],
        "correct": "동생보다",
        "explanation": "<p>보다 otga toʻgʻridan-toʻgʻri yopishadi va 받침 ayrisi "
                       "yoʻq: <strong>동생보다</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>오늘이 어제보다 더 ___</strong> — 덥다</p>",
        "choices": ["덥어요", "더워요", "덥아요", "더우요"],
        "correct": "더워요",
        "explanation": "<p>Taqqoslash sifatning shaklini oʻzgartirmaydi — 덥다 "
                       "baribir <strong>더워요</strong> boʻladi (PK-32, ㅂ → 우).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>과일 ___ 사과를 제일 좋아해요.</strong></p>",
        "choices": ["에서", "보다", "중에서", "하고"],
        "correct": "중에서",
        "explanation": "<p>Narsalar guruhi doirasi — <strong>중에서</strong>. "
                       "에서 joy uchun ishlatiladi: 한국<strong>에서</strong> "
                       "서울이 제일 커요.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>우리 반___ 셰르벡 씨가 제일 커요.</strong></p>",
        "choices": ["보다", "중에서", "에서", "이면"],
        "correct": "에서",
        "explanation": "<p>“Sinfda” — joy, shuning uchun <strong>에서</strong>. "
                       "Agar “oʻquvchilar orasida” deyilsa, 학생들 "
                       "<strong>중에서</strong> boʻlardi.</p>",
    },
    {
        "text": "<p><strong>크다</strong> ning toʻgʻri shakli qaysi?</p>",
        "choices": ["크어요", "커요", "카요", "크아요"],
        "correct": "커요",
        "explanation": "<p>으 tushadi va oʻzak bitta boʻgʻindan iborat — qaraydigan "
                       "oldingi boʻgʻin yoʻq, shuning uchun <strong>어</strong>: "
                       "<strong>커요</strong> (PK-32).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>이 옷이 저 옷보다 ___ 비싸요.</strong> "
                "(“kamroq qimmat”)</p>",
        "choices": ["더", "덜", "제일", "안"],
        "correct": "덜",
        "explanation": "<p><strong>덜</strong> = kamroq. <strong>안 비싸요</strong> "
                       "boʻlsa shunchaki “qimmat emas” degan boshqa maʼno chiqadi — "
                       "taqqoslash yoʻqoladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>한국어가 영어보다 ___</strong> — 어렵다</p>",
        "choices": ["어렵어요", "어려워요", "어렵아요", "어려우요"],
        "correct": "어려워요",
        "explanation": "<p>ㅂ tuslanishi: 어렵 → 어려우 → "
                       "<strong>어려워요</strong>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["이게 제일 가장 맛있어요.", "이게 제일 맛있어요.",
                    "이게 가장 제일 맛있어요.", "이게 제일 더 맛있어요."],
        "correct": "이게 제일 맛있어요.",
        "explanation": "<p>제일 va 가장 — bir xil maʼno, birga ishlatilmaydi "
                       "(“eng eng” boʻlib qoladi). 제일 bilan 더 ham birga "
                       "kelmaydi.</p>",
    },
    {
        "text": "<p><strong>더</strong> ni tushirib qoldirsa boʻladimi?</p>"
                "<p><strong>저는 동생보다 (더) 커요</strong></p>",
        "choices": ["Ha — 보다 oʻzi “…dan” maʼnosini beradi",
                    "Yoʻq — 더 majburiy",
                    "Faqat savol gaplarda boʻladi",
                    "Faqat 가장 bilan birga boʻladi"],
        "correct": "Ha — 보다 oʻzi “…dan” maʼnosini beradi",
        "explanation": "<p><strong>더 ixtiyoriy</strong> — u faqat urgʻuni "
                       "kuchaytiradi. <strong>덜</strong> esa ixtiyoriy emas: uni "
                       "qoʻymasangiz maʼno teskarisiga aylanadi.</p>",
    },
    {
        "text": "<p>“Ukamdan koʻra <em>men</em> kattaman” degan urgʻu qaysi "
                "gapda?</p>",
        "choices": ["저는 동생보다 커요.", "동생보다 제가 커요.",
                    "동생이 저보다 커요.", "저는 동생이 커요."],
        "correct": "동생보다 제가 커요.",
        "explanation": "<p>보다 li boʻlak oldinga chiqarilsa, urgʻu egaga "
                       "koʻchadi. Uchinchi variant esa teskarisini aytadi — "
                       "“ukam mendan katta”.</p>",
    },
    {
        "text": "<p>Qaysi gapda <strong>doira</strong> notoʻgʻri berilgan?</p>",
        "choices": ["음식 중에서 김치가 제일 매워요.",
                    "한국에서 서울이 제일 커요.",
                    "과일 에서 사과가 제일 맛있어요.",
                    "우리 반에서 누가 제일 커요?"],
        "correct": "과일 에서 사과가 제일 맛있어요.",
        "explanation": "<p>과일 — joy emas, narsalar guruhi, shuning uchun "
                       "<strong>중에서</strong> kerak: 과일 <strong>중에서</strong> "
                       "사과가 제일 맛있어요.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda <strong>xato bor</strong>?</p>",
        "choices": ["저는 동생보다 커요.", "과일 중에서 사과가 좋아해요.",
                    "오늘이 어제보다 더 더워요.", "이 옷이 저 옷보다 덜 비싸요."],
        "correct": "과일 중에서 사과가 좋아해요.",
        "explanation": "<p>좋아하다 — oʻtimli feʼl, toʻldiruvchi oladi: "
                       "<strong>사과를</strong> 제일 좋아해요. 사과가 boʻlsa ega "
                       "boʻlib qoladi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["저는 동생을 보다 커요.", "저는 동생보다 커요.",
                    "저는 동생보다를 커요.", "저는 동생에서 커요."],
        "correct": "저는 동생보다 커요.",
        "explanation": "<p>보다 — qoʻshimcha, oldidan ham, keyinidan ham 을/를 "
                       "olmaydi: <strong>동생보다</strong>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 우리 반에서 누가 제일 커요?<br>나: ___</strong></p>",
        "choices": ["셰르벡 씨가 제일 커요.", "셰르벡 씨는 제일 커요보다.",
                    "셰르벡 씨가 가장 제일 커요.", "셰르벡 씨를 제일 커요."],
        "correct": "셰르벡 씨가 제일 커요.",
        "explanation": "<p>Javobda ega <strong>이/가</strong> oladi — “aynan u” "
                       "degani (PK-12). 제일 esa sifatdan oldin turadi.</p>",
    },
    {
        "text": "<p>“Koreys tili ingliz tilidan qiyinroq” — qaysi gap toʻgʻri?</p>",
        "choices": ["한국어가 영어보다 어려워요.", "한국어가 영어를 보다 어렵어요.",
                    "한국어가 영어중에서 어려워요.", "한국어가 영어보다 제일 어려워요."],
        "correct": "한국어가 영어보다 어려워요.",
        "explanation": "<p>보다 otga toʻgʻridan-toʻgʻri yopishadi, 어렵다 → "
                       "<strong>어려워요</strong>. 제일 bu yerda notoʻgʻri — "
                       "u ikki narsani emas, butun guruhni nazarda tutadi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-35 Mashq: 아/어서 — sabab va ketma-ketlik",
        "description": "20 savol — yasalishi, ikkita taqiq (zamon yoʻq, buyruq "
                       "yoʻq) va 고 bilan farqi.",
        "tutorial":    "PK-35:",
        "level":       "medium",
        "questions":   Q_PK35,
    },
    {
        "title":       "PK-36 Mashq: (으)면 — shart va faraz",
        "description": "20 savol — 받침 ayrisi, ㄹ oʻzaklar, notoʻgʻri feʼllar "
                       "va 아/어서 bilan farqi.",
        "tutorial":    "PK-36:",
        "level":       "medium",
        "questions":   Q_PK36,
    },
    {
        "title":       "PK-37 Mashq: 보다 va 제일 / 가장 — taqqoslash",
        "description": "20 savol — 보다, 더, 덜, 제일, 가장 va 중에서 ning "
                       "oʻrni.",
        "tutorial":    "PK-37:",
        "level":       "medium",
        "questions":   Q_PK37,
    },
]
