# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-29 … PK-31.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_29_31.py --master=prime \\
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
# PK-29 — (으)세요 / 지 마세요
# =====================================================================

Q_PK29 = [
    # 1–5 tanish
    {
        "text": "<p><strong>(으)세요</strong> qanday maʼno beradi?</p>",
        "choices": ["Hurmatli buyruq va iltimos", "Oʻtgan zamon",
                    "Xohish", "Inkor"],
        "correct": "Hurmatli buyruq va iltimos",
        "explanation": "<p><strong>(으)세요</strong> — “…ing” degan hurmatli buyruq: "
                       "앉으세요, 오세요. U quruq buyruq emas, balki iltimos yoki "
                       "marhamat ohangida eshitiladi.</p>",
    },
    {
        "text": "<p>Taqiq (“…mang”) qaysi qolip bilan beriladi?</p>",
        "choices": ["지 마세요", "안 …세요", "못 …세요", "지 않으세요"],
        "correct": "지 마세요",
        "explanation": "<p>Taqiq faqat <strong>지 마세요</strong>: 가지 마세요, "
                       "먹지 마세요. <s>안 가세요</s> esa “bormaysiz(mi)” degan "
                       "darak yoki savol.</p>",
    },
    {
        "text": "<p>받침 boʻlmagan oʻzakka qaysi shakl qoʻshiladi?</p>",
        "choices": ["세요", "으세요", "이세요", "을세요"],
        "correct": "세요",
        "explanation": "<p>Oʻzak unli bilan tugasa — <strong>세요</strong> "
                       "(가세요, 오세요). 받침 bor boʻlsa <strong>으세요</strong> "
                       "(읽으세요).</p>",
    },
    {
        "text": "<p><strong>먹다</strong> ning hurmatli buyruq shakli qaysi?</p>",
        "choices": ["드세요", "먹으세요", "먹세요", "잡으세요"],
        "correct": "드세요",
        "explanation": "<p>먹다 va 마시다 ning hurmatli shakli maxsus — "
                       "<strong>드세요</strong>. Yodlash kerak boʻlgan beshta "
                       "shakldan biri.</p>",
    },
    {
        "text": "<p><strong>안녕히 주무세요</strong> nima degani?</p>",
        "choices": ["Xayrli tun (tinch uxlang)", "Xush kelibsiz",
                    "Yaxshi boring", "Rahmat"],
        "correct": "Xayrli tun (tinch uxlang)",
        "explanation": "<p>자다 ning hurmatli shakli <strong>주무세요</strong>. "
                       "Demak 안녕히 주무세요 — “tinch uxlang”. PK-9 dagi ibora "
                       "aslida shu qolipda yasalgan.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>여기 ___</strong> "
                "(“Bu yerga oʻtiring.”) — 앉다</p>",
        "choices": ["앉으세요", "앉세요", "앉아세요", "앉으십니다"],
        "correct": "앉으세요",
        "explanation": "<p>Oʻzak <strong>앉</strong> — 받침 bor, shuning uchun "
                       "<strong>으세요</strong>. <s>앉세요</s> notoʻgʻri.</p>",
    },
    {
        "text": "<p><strong>만들다</strong> dan hurmatli buyruq yasang.</p>",
        "choices": ["만드세요", "만들으세요", "만들세요", "만들어세요"],
        "correct": "만드세요",
        "explanation": "<p>Oʻzak ㄹ bilan tugasa, ㄹ <strong>tushib qoladi</strong>: "
                       "만들 → <strong>만드세요</strong>. Xuddi shunday 팔다 → "
                       "파세요, 살다 → 사세요.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>여기에서 사진을 ___</strong> "
                "(“Bu yerda rasmga olmang.”) — 찍다</p>",
        "choices": ["찍지 마세요", "안 찍으세요", "못 찍으세요", "찍으세요"],
        "correct": "찍지 마세요",
        "explanation": "<p>Taqiq — <strong>지 마세요</strong>, va bu qolipda "
                       "받침 ayrisi yoʻq: 찍<strong>지 마세요</strong>.</p>",
    },
    {
        "text": "<p>“Kutib turing” ni koreyschaga oʻgiring. (기다리다)</p>",
        "choices": ["기다리세요", "기다리으세요", "기다려세요", "기다리지 마세요"],
        "correct": "기다리세요",
        "explanation": "<p>Oʻzak <strong>기다리</strong> — unli bilan tugaydi, "
                       "shuning uchun oddiy <strong>세요</strong>.</p>",
    },
    {
        "text": "<p>Muzeyda yozuv turibdi. Qaysi shakl eng mos?</p>",
        "choices": ["사진을 찍지 마십시오.", "사진을 찍지 마.",
                    "사진을 찍지 마세요?", "사진을 안 찍어요."],
        "correct": "사진을 찍지 마십시오.",
        "explanation": "<p>Rasmiy eʼlon va yozuvlarda <strong>합니다체</strong> "
                       "ishlatiladi: 지 마십시오. Ogʻzaki nutqda esa 찍지 "
                       "마세요.</p>",
    },
    {
        "text": "<p><strong>어디에 가세요?</strong> nima degani?</p>",
        "choices": ["Qayerga ketyapsiz?", "Qayerga boring!",
                    "Qayerga bordingiz?", "Qayerga bormang!"],
        "correct": "Qayerga ketyapsiz?",
        "explanation": "<p>(으)세요 savol ohangida <strong>hurmatli savol</strong> "
                       "boʻladi — buyruq emas. Ya'ni bitta shakl ikki vazifada "
                       "ishlaydi.</p>",
    },
    {
        "text": "<p>Ustozga suv uzatyapsiz. Qaysi gap toʻgʻri?</p>",
        "choices": ["물 드세요.", "물 먹으세요.", "물 먹어요.", "물 드십니다."],
        "correct": "물 드세요.",
        "explanation": "<p>마시다/먹다 ning hurmatli shakli <strong>드세요</strong>. "
                       "먹으세요 grammatik jihatdan yasalgan, lekin ustozga nisbatan "
                       "qoʻpol eshitiladi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>가세요</strong> va <strong>가지 마세요</strong> farqi nima?</p>",
        "choices": ["Birinchisi — boring, ikkinchisi — bormang",
                    "Birinchisi — bordingiz, ikkinchisi — bormadingiz",
                    "Birinchisi — borasiz, ikkinchisi — borolmaysiz",
                    "Farqi yoʻq"],
        "correct": "Birinchisi — boring, ikkinchisi — bormang",
        "explanation": "<p>(으)세요 — buyruq, <strong>지 마세요</strong> — taqiq. "
                       "Ikkalasi ham bitta hurmat darajasida.</p>",
    },
    {
        "text": "<p><strong>안 가세요</strong> nima maʼno beradi?</p>",
        "choices": ["Bormaysizmi? (savol/darak)", "Bormang! (taqiq)",
                    "Bora olmaysiz", "Bormadingiz"],
        "correct": "Bormaysizmi? (savol/darak)",
        "explanation": "<p>안 — oddiy inkor (PK-21), taqiq emas. Taqiq uchun "
                       "<strong>가지 마세요</strong> kerak.</p>",
    },
    {
        "text": "<p>Nega <s>저는 학교에 가세요</s> notoʻgʻri?</p>",
        "choices": ["(으)세요 hurmat bildiradi — oʻzi haqida ishlatilmaydi",
                    "Chunki 학교 받침 bilan tugaydi",
                    "Chunki 가다 notoʻgʻri feʼl",
                    "Chunki 에 emas, 에서 kerak"],
        "correct": "(으)세요 hurmat bildiradi — oʻzi haqida ishlatilmaydi",
        "explanation": "<p>Odam oʻzini hurmatlamaydi. Toʻgʻrisi — "
                       "<strong>저는 학교에 가요</strong>. Bu shakl faqat suhbatdosh "
                       "yoki hurmatli uchinchi shaxs haqida.</p>",
    },
    {
        "text": "<p><strong>앉으세요</strong> va <strong>앉으십시오</strong> farqi nima?</p>",
        "choices": ["Ikkinchisi rasmiyroq — eʼlon va rasmiy nutq uchun",
                    "Ikkinchisi taqiq",
                    "Ikkinchisi oʻtgan zamon",
                    "Ikkinchisi savol"],
        "correct": "Ikkinchisi rasmiyroq — eʼlon va rasmiy nutq uchun",
        "explanation": "<p>앉으세요 — 해요체 (kundalik hurmat), "
                       "<strong>앉으십시오</strong> — 합니다체 (aeroport, metro, "
                       "rasmiy xat).</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["만들으세요.", "만드세요.", "읽으세요.", "가세요."],
        "correct": "만들으세요.",
        "explanation": "<p>ㄹ oʻzak ㄹ ni tashlaydi: <strong>만드세요</strong>. "
                       "<s>만들으세요</s> ham, <s>만들세요</s> ham notoʻgʻri.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["여기에 앉지 마세요.", "여기에 안 앉으세요.",
                    "여기에 앉지 않으세요.", "여기에 못 앉으세요."],
        "correct": "여기에 앉지 마세요.",
        "explanation": "<p>Taqiq faqat <strong>지 마세요</strong>. Qolganlari "
                       "grammatik jihatdan bor, lekin ular darak/savol — “oʻtirmaysiz”, "
                       "“oʻtirolmaysiz”.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 선생님, 어디에 앉아요?<br>나: ___</strong></p>",
        "choices": ["여기 앉으세요.", "여기 앉아세요.",
                    "저는 여기 앉으세요.", "여기 앉지 마요."],
        "correct": "여기 앉으세요.",
        "explanation": "<p>Suhbatdoshga aytilgan hurmatli buyruq: 받침 bor → "
                       "<strong>앉으세요</strong>. <s>저는 앉으세요</s> notoʻgʻri — "
                       "hurmat shakli oʻzi haqida ishlatilmaydi.</p>",
    },
    {
        "text": "<p>Bu gapni taqiqqa oʻgiring: <strong>여기에서 사진을 "
                "찍으세요.</strong></p>",
        "choices": ["여기에서 사진을 찍지 마세요.", "여기에서 사진을 안 찍으세요.",
                    "여기에서 사진을 못 찍으세요.", "여기에서 사진을 찍지 않으세요."],
        "correct": "여기에서 사진을 찍지 마세요.",
        "explanation": "<p>Faqat oxiri oʻzgaradi: (으)세요 → <strong>지 마세요</strong>. "
                       "Toʻldiruvchi va joy qoʻshimchasi oʻz joyida qoladi.</p>",
    },
]


# =====================================================================
# PK-30 — (으)ㄹ 수 있다 / 없다
# =====================================================================

Q_PK30 = [
    # 1–5 tanish
    {
        "text": "<p><strong>(으)ㄹ 수 있다</strong> nima maʼno beradi?</p>",
        "choices": ["…ola olmoq", "…gim keladi", "…ib bermoq", "…mang"],
        "correct": "…ola olmoq",
        "explanation": "<p><strong>(으)ㄹ 수 있다</strong> — imkon yoki qobiliyat: "
                       "갈 수 있어요 = bora olaman.</p>",
    },
    {
        "text": "<p><strong>수</strong> soʻzining maʼnosi nima?</p>",
        "choices": ["yoʻl, usul, imkon", "vaqt", "son", "joy"],
        "correct": "yoʻl, usul, imkon",
        "explanation": "<p><strong>수</strong> — ot. Shuning uchun qolip soʻzma-soʻz "
                       "“…qiladigan <b>imkon bor</b>” deb oʻqiladi va oxirida "
                       "있다/없다 turadi.</p>",
    },
    {
        "text": "<p>받침 boʻlmagan oʻzakka qaysi shakl qoʻshiladi?</p>",
        "choices": ["ㄹ 수 있어요", "을 수 있어요", "를 수 있어요", "이 수 있어요"],
        "correct": "ㄹ 수 있어요",
        "explanation": "<p>받침 yoʻq → ㄹ oʻzakning ostiga yopishadi: 가 → "
                       "<strong>갈 수 있어요</strong>. 받침 bor boʻlsa alohida boʻgʻin: "
                       "먹<strong>을</strong> 수 있어요.</p>",
    },
    {
        "text": "<p>Inkor shakli qaysi?</p>",
        "choices": ["(으)ㄹ 수 없어요", "(으)ㄹ 수 안 있어요",
                    "(으)ㄹ 수 있지 않아요", "못 (으)ㄹ 수 있어요"],
        "correct": "(으)ㄹ 수 없어요",
        "explanation": "<p>있다 ning jufti <strong>없다</strong> — 안 qoʻshilmaydi. "
                       "Bu PK-13 dagi 있다/없다 juftligining oʻzi.</p>",
    },
    {
        "text": "<p><strong>할 수 있어요</strong> qanday oʻqiladi?</p>",
        "choices": ["[할 쑤 이써요]", "[할 수 이서요]", "[하 수 있어요]", "[할 쑤 잇어요]"],
        "correct": "[할 쑤 이써요]",
        "explanation": "<p>ㄹ 받침dan keyin ㅅ qattiqlashadi — <strong>경음화</strong> "
                       "(PK-8). 있어요 esa 연음화 bilan [이써요].</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>저는 김치를 ___ 수 "
                "있어요.</strong> (먹다)</p>",
        "choices": ["먹을", "먹", "먹어", "먹는"],
        "correct": "먹을",
        "explanation": "<p>Oʻzak 먹 — 받침 bor, shuning uchun <strong>을 수</strong>: "
                       "먹을 수 있어요.</p>",
    },
    {
        "text": "<p><strong>운전하다</strong> dan “hayday olaman” yasang.</p>",
        "choices": ["운전할 수 있어요", "운전을 수 있어요",
                    "운전해 수 있어요", "운전하을 수 있어요"],
        "correct": "운전할 수 있어요",
        "explanation": "<p>Oʻzak 운전하 — unli bilan tugaydi, shuning uchun ㄹ ostiga "
                       "yopishadi: <strong>운전할 수 있어요</strong>.</p>",
    },
    {
        "text": "<p><strong>만들다</strong> dan “tayyorlay olaman” yasang.</p>",
        "choices": ["만들 수 있어요", "만들을 수 있어요",
                    "만드 수 있어요", "만들어 수 있어요"],
        "correct": "만들 수 있어요",
        "explanation": "<p>Oʻzak allaqachon ㄹ bilan tugagan — yangi ㄹ qoʻshilmaydi: "
                       "<strong>만들 수 있어요</strong>. Xuddi PK-27 dagi 살 거예요 "
                       "kabi.</p>",
    },
    {
        "text": "<p>“Kecha kelolmadim” ni koreyschaga oʻgiring.</p>",
        "choices": ["어제 올 수 없었어요.", "어제 왔을 수 없어요.",
                    "어제 올 수 없어요.", "어제 올 수 안 있었어요."],
        "correct": "어제 올 수 없었어요.",
        "explanation": "<p>Oʻzak 오 → <strong>올 수</strong>, oʻtgan zamon esa "
                       "<strong>없다</strong> ga qoʻshiladi: 없었어요.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>가: 한국어를 할 수 "
                "있어요?<br>나: 네, 조금 ___</strong></p>",
        "choices": ["할 수 있어요.", "할 수 없어요.", "하고 싶어요.", "할 거예요."],
        "correct": "할 수 있어요.",
        "explanation": "<p>네 (ha) bilan boshlangan javob tasdiq boʻlishi kerak — "
                       "<strong>할 수 있어요</strong>. Qolganlari savolga javob "
                       "bermaydi.</p>",
    },
    {
        "text": "<p>“Yolgʻiz bora olmayman” ni koreyschaga oʻgiring.</p>",
        "choices": ["혼자 갈 수 없어요.", "혼자 갈 수 안 있어요.",
                    "혼자 가을 수 없어요.", "혼자 갔 수 없어요."],
        "correct": "혼자 갈 수 없어요.",
        "explanation": "<p>받침 yoʻq → <strong>갈 수</strong>, inkor esa "
                       "<strong>없어요</strong>.</p>",
    },
    {
        "text": "<p>Rasmiy shakli (합니다체) qaysi?</p>",
        "choices": ["갈 수 있습니다", "갈 수 있어습니다",
                    "갈 수 있읍니다", "갈 수 있어요습니다"],
        "correct": "갈 수 있습니다",
        "explanation": "<p>Tuslanish oxirgi soʻzda: 있다 → <strong>있습니다</strong> "
                       "(PK-19).</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>못 가요</strong> va <strong>갈 수 없어요</strong> "
                "haqida nima toʻgʻri?</p>",
        "choices": ["Deyarli bir xil; 못 qisqa va ogʻzaki, 수 없다 toʻliqroq",
                    "못 — oʻtgan zamon, 수 없다 — hozirgi",
                    "못 — xohish, 수 없다 — imkon",
                    "못 faqat sifat bilan ishlatiladi"],
        "correct": "Deyarli bir xil; 못 qisqa va ogʻzaki, 수 없다 toʻliqroq",
        "explanation": "<p>Ikkalasi koʻp joyda almashinadi. Farqi ohangda: "
                       "<strong>못</strong> kundalik va qisqa, <strong>수 없다</strong> "
                       "yumshoqroq hamda yozma nutqda ham ishlaydi.</p>",
    },
    {
        "text": "<p>Nega 못 dan koʻra (으)ㄹ 수 있다 qolipi kengroq deyiladi?</p>",
        "choices": ["못 ning ijobiy jufti yoʻq — “ola olaman” faqat 수 있다 bilan",
                    "못 faqat oʻtgan zamonda ishlatiladi",
                    "못 faqat yozma nutqda uchraydi",
                    "못 sifatlar bilan ham ishlatiladi"],
        "correct": "못 ning ijobiy jufti yoʻq — “ola olaman” faqat 수 있다 bilan",
        "explanation": "<p>못 faqat <em>inkor</em> tomonni beradi. Ijobiy maʼno — "
                       "“qila olaman” — faqat <strong>할 수 있어요</strong> bilan "
                       "aytiladi.</p>",
    },
    {
        "text": "<p><strong>갈 거예요</strong> va <strong>갈 수 있어요</strong> "
                "farqi nima?</p>",
        "choices": ["Birinchisi — reja, ikkinchisi — imkon",
                    "Birinchisi — imkon, ikkinchisi — reja",
                    "Birinchisi — xohish, ikkinchisi — buyruq",
                    "Farqi yoʻq"],
        "correct": "Birinchisi — reja, ikkinchisi — imkon",
        "explanation": "<p>갈 거예요 — “boraman” (PK-27, qaror). "
                       "<strong>갈 수 있어요</strong> — “bora olaman” (imkon bor, "
                       "lekin borishim shart emas).</p>",
    },
    {
        "text": "<p><strong>가고 싶어요</strong> va <strong>갈 수 있어요</strong> "
                "farqi nima?</p>",
        "choices": ["Xohish va imkon", "Oʻtgan va hozirgi zamon",
                    "Buyruq va taqiq", "Rasmiy va norasmiy"],
        "correct": "Xohish va imkon",
        "explanation": "<p>가고 싶어요 — <em>borgim keladi</em> (PK-28, istak). "
                       "<strong>갈 수 있어요</strong> — <em>bora olaman</em> (imkoniyat). "
                       "Odam xohlashi mumkin, lekin bora olmasligi ham mumkin.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["만들을 수 있어요.", "만들 수 있어요.",
                    "먹을 수 있어요.", "갈 수 있어요."],
        "correct": "만들을 수 있어요.",
        "explanation": "<p>Oʻzak 만들 allaqachon ㄹ bilan tugaydi — yangi ㄹ "
                       "qoʻshilmaydi: <strong>만들 수 있어요</strong>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["어제 갈 수 있었어요.", "어제 갔을 수 있어요.",
                    "어제 갈 수 안 있었어요.", "어제 가 수 있었어요."],
        "correct": "어제 갈 수 있었어요.",
        "explanation": "<p>Tuslanish har doim oxirgi soʻzda — <strong>있다</strong> da: "
                       "갈 수 <strong>있었어요</strong>. Asosiy feʼlga oʻtgan zamon "
                       "qoʻshilmaydi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 매운 음식을 먹을 수 있어요?<br>나: 아니요, ___</strong></p>",
        "choices": ["먹을 수 없어요.", "먹을 수 있어요.",
                    "먹고 싶어요.", "먹지 마세요."],
        "correct": "먹을 수 없어요.",
        "explanation": "<p>아니요 (yoʻq) bilan boshlangan javob inkor boʻlishi kerak — "
                       "<strong>먹을 수 없어요</strong>. 못 먹어요 ham toʻgʻri "
                       "boʻlardi.</p>",
    },
    {
        "text": "<p>Soʻzlarni toʻgʻri tartibda joylashtiring:<br>"
                "<strong>김치를 / 저는 / 없어요 / 먹을 / 수</strong></p>",
        "choices": ["저는 김치를 먹을 수 없어요.", "저는 없어요 김치를 먹을 수.",
                    "김치를 저는 없어요 먹을 수.", "먹을 수 저는 김치를 없어요."],
        "correct": "저는 김치를 먹을 수 없어요.",
        "explanation": "<p>Koreys tili SOV: ega (저는) → toʻldiruvchi (김치를) → kesim "
                       "(할 수 없어요). Kesim <strong>har doim oxirida</strong>, "
                       "xuddi oʻzbekchadagidek.</p>",
    },
]


# =====================================================================
# PK-31 — 아/어 주다
# =====================================================================

Q_PK31 = [
    # 1–5 tanish
    {
        "text": "<p><strong>아/어 주다</strong> nima maʼno beradi?</p>",
        "choices": ["…ib bermoq (boshqa odam uchun qilmoq)", "…ola olmoq",
                    "…gim keladi", "…mang"],
        "correct": "…ib bermoq (boshqa odam uchun qilmoq)",
        "explanation": "<p><strong>아/어 주다</strong> — ish boshqa odamning foydasiga "
                       "qilinganini bildiradi: 읽어 주다 = oʻqib bermoq.</p>",
    },
    {
        "text": "<p>Iltimos qilishning eng koʻp ishlatiladigan shakli qaysi?</p>",
        "choices": ["아/어 주세요", "아/어 줘요", "아/어 줬어요", "아/어 주지 마세요"],
        "correct": "아/어 주세요",
        "explanation": "<p><strong>아/어 주세요</strong> — “…ib bering”. 주다 ning "
                       "hurmatli buyruq shakli 주세요 (PK-29).</p>",
    },
    {
        "text": "<p>Bu qolip oʻzbekchadagi qaysi tuzilmaga toʻgʻri keladi?</p>",
        "choices": ["-ib bering (oʻqib bering)", "-a olaman (oʻqiy olaman)",
                    "-gim keladi", "-ma (oʻqima)"],
        "correct": "-ib bering (oʻqib bering)",
        "explanation": "<p>Ikkala tilda ham asosiy feʼl oldinda, “bermoq” keyinda: "
                       "<strong>oʻqib bering</strong> = 읽어 주세요.</p>",
    },
    {
        "text": "<p>Odamga (“doʻstimga”) qaysi qoʻshimcha qoʻshiladi?</p>",
        "choices": ["한테 / 에게", "에", "에서", "의"],
        "correct": "한테 / 에게",
        "explanation": "<p>Odam uchun <strong>한테</strong> (ogʻzaki) yoki "
                       "<strong>에게</strong> (yozma). 에 esa joy uchun (PK-14).</p>",
    },
    {
        "text": "<p>Iltimosda <strong>좀</strong> nima vazifa bajaradi?</p>",
        "choices": ["Gapni yumshatadi (“iltimos”, “-chi”)", "Miqdorni aniqlaydi",
                    "Inkor qiladi", "Oʻtgan zamon yasaydi"],
        "correct": "Gapni yumshatadi (“iltimos”, “-chi”)",
        "explanation": "<p>좀 aslida “ozgina” degani, lekin iltimosda u "
                       "<strong>xushmuomalalik</strong> bildiradi: 사진 좀 찍어 "
                       "주세요.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p><strong>읽다</strong> dan “oʻqib bering” yasang.</p>",
        "choices": ["읽어 주세요", "읽고 주세요", "읽으 주세요", "읽을 주세요"],
        "correct": "읽어 주세요",
        "explanation": "<p>Avval 아/어 shakli (읽 + 어 → <strong>읽어</strong>), keyin "
                       "주세요. 고 bu yerda ishlatilmaydi.</p>",
    },
    {
        "text": "<p><strong>가르치다</strong> dan “oʻrgatib bering” yasang.</p>",
        "choices": ["가르쳐 주세요", "가르치 주세요",
                    "가르치어 주세요", "가르칠 주세요"],
        "correct": "가르쳐 주세요",
        "explanation": "<p>가르치 + 어 → <strong>가르쳐</strong> (PK-18 dagi "
                       "qisqarish), keyin 주세요.</p>",
    },
    {
        "text": "<p><strong>하다</strong> dan “qilib bering” yasang.</p>",
        "choices": ["해 주세요", "하 주세요", "하어 주세요", "할 주세요"],
        "correct": "해 주세요",
        "explanation": "<p>하다 ning 아/어 shakli — <strong>해</strong>. Demak "
                       "해 주세요.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>친구___ 책을 사 "
                "줬어요.</strong></p>",
        "choices": ["한테", "에", "에서", "을"],
        "correct": "한테",
        "explanation": "<p>친구 — odam, shuning uchun <strong>한테</strong> yoki "
                       "에게. <s>친구에</s> notoʻgʻri — 에 faqat joy va vaqt "
                       "uchun.</p>",
    },
    {
        "text": "<p>“Yana bir marta aytib bering” ni koreyschaga oʻgiring.</p>",
        "choices": ["다시 말해 주세요.", "다시 말하 주세요.",
                    "다시 말고 주세요.", "다시 말할 주세요."],
        "correct": "다시 말해 주세요.",
        "explanation": "<p>말하다 → 아/어 shakli <strong>말해</strong>, keyin 주세요. "
                       "다시 = yana.</p>",
    },
    {
        "text": "<p>Oʻtgan zamon shakli qaysi?</p><p><strong>읽어 주다 → ?</strong></p>",
        "choices": ["읽어 줬어요", "읽었어 줘요", "읽어 주었요", "읽었어 줬어요"],
        "correct": "읽어 줬어요",
        "explanation": "<p>Tuslanish faqat <strong>주다</strong> da: 주었어요 → "
                       "qisqargani 줬어요. Asosiy feʼl 읽어 shaklida qoladi.</p>",
    },
    {
        "text": "<p>Taqiq shakli qaysi?</p><p><strong>읽어 주다 → “oʻqib "
                "bermang”</strong></p>",
        "choices": ["읽어 주지 마세요", "읽지 마 주세요",
                    "안 읽어 주세요", "읽어 안 주세요"],
        "correct": "읽어 주지 마세요",
        "explanation": "<p>지 마세요 (PK-29) oxirgi feʼlga — <strong>주다</strong> ga "
                       "qoʻshiladi: 읽어 주지 마세요.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>물을 주세요</strong> va <strong>물을 사 주세요</strong> "
                "farqi nima?</p>",
        "choices": ["Birinchisi narsani, ikkinchisi ishni soʻraydi",
                    "Birinchisi rasmiy, ikkinchisi norasmiy",
                    "Birinchisi oʻtgan zamon",
                    "Farqi yoʻq"],
        "correct": "Birinchisi narsani, ikkinchisi ishni soʻraydi",
        "explanation": "<p>물을 주세요 — “suv bering” (narsa). "
                       "<strong>물을 사 주세요</strong> — “suv sotib olib bering” "
                       "(ish). Otdan keyin toʻgʻridan-toʻgʻri 주세요.</p>",
    },
    {
        "text": "<p>Nega <s>친구에 책을 사 줬어요</s> notoʻgʻri?</p>",
        "choices": ["Odamga 한테/에게 kerak, 에 emas",
                    "Chunki 친구 받침 bilan tugamaydi",
                    "Chunki 사다 notoʻgʻri feʼl",
                    "Chunki oʻtgan zamon ishlatilgan"],
        "correct": "Odamga 한테/에게 kerak, 에 emas",
        "explanation": "<p>Koreys tili odam va joyni ajratadi: 학교<b>에</b> 가요 "
                       "(joy), 친구<b>한테</b> 줘요 (odam). Oʻzbekchada ikkalasi ham "
                       "<em>-ga</em> boʻlgani uchun bu yerda koʻp adashiladi.</p>",
    },
    {
        "text": "<p><strong>에게</strong> va <strong>한테</strong> farqi nima?</p>",
        "choices": ["에게 — yozma/rasmiy, 한테 — ogʻzaki",
                    "에게 — odam, 한테 — joy",
                    "에게 — koʻplik, 한테 — birlik",
                    "Farqi yoʻq, ikkalasi ham rasmiy"],
        "correct": "에게 — yozma/rasmiy, 한테 — ogʻzaki",
        "explanation": "<p>Maʼnosi bir xil, uslubi boshqa. Hurmatli shakli esa "
                       "<strong>께</strong>: 선생님<b>께</b>.</p>",
    },
    {
        "text": "<p><strong>도와주세요</strong> nima degani?</p>",
        "choices": ["Yordam bering", "Kutib turing", "Kirmang", "Rahmat"],
        "correct": "Yordam bering",
        "explanation": "<p>돕다 (yordam bermoq) + 아 주세요 → <strong>도와주세요</strong>. "
                       "Bu shakl bir soʻz boʻlib qolgan — hozircha yod olib "
                       "qoʻying.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["읽고 주세요.", "읽어 주세요.",
                    "해 주세요.", "만들어 주세요."],
        "correct": "읽고 주세요.",
        "explanation": "<p>Bu qolip <strong>아/어</strong> shaklini talab qiladi, "
                       "고 ni emas: <strong>읽어 주세요</strong>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["어머니가 김치를 만들어 줬어요.",
                    "어머니가 김치를 만들었어 줘요.",
                    "어머니가 김치를 만들고 줬어요.",
                    "어머니가 김치를 만들 줬어요."],
        "correct": "어머니가 김치를 만들어 줬어요.",
        "explanation": "<p>아/어 shakli <strong>만들어</strong>, tuslanish esa "
                       "<strong>주다</strong> da: 줬어요.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 저는 한국어를 잘 몰라요.<br>나: 그럼 제가 ___</strong></p>",
        "choices": ["가르쳐 줄 거예요.", "가르쳐 주세요.",
                    "가르쳐 주지 마세요.", "가르치 줄 거예요."],
        "correct": "가르쳐 줄 거예요.",
        "explanation": "<p>Gapiruvchi <em>oʻzi</em> yordam berishni aytyapti, shuning "
                       "uchun iltimos shakli (주세요) toʻgʻri kelmaydi. Kelasi zamon "
                       "주다 ga qoʻshiladi: <strong>가르쳐 줄 거예요</strong> "
                       "(PK-27).</p>",
    },
    {
        "text": "<p>Koʻchada oʻtgan odamdan suratga tushirishni soʻrayapsiz. "
                "Eng tabiiy gap qaysi?</p>",
        "choices": ["사진 좀 찍어 주세요.", "사진을 찍으세요.",
                    "사진을 찍고 싶어요.", "사진을 찍지 마세요."],
        "correct": "사진 좀 찍어 주세요.",
        "explanation": "<p>Ish <em>siz uchun</em> qilinadi → <strong>아/어 주세요</strong>, "
                       "va <strong>좀</strong> iltimosni yumshatadi. 찍으세요 shunchaki "
                       "“rasmga oling” degan quruq buyruq boʻlardi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-29 Mashq: (으)세요 / 지 마세요 — buyruq va taqiq",
        "description": "20 savol — 받침 ayrisi, ㄹ oʻzaklar, maxsus hurmat shakllari "
                       "va taqiq.",
        "tutorial":    "PK-29:",
        "level":       "easy",
        "questions":   Q_PK29,
    },
    {
        "title":       "PK-30 Mashq: (으)ㄹ 수 있다/없다 — imkon",
        "description": "20 savol — 받침 ayrisi, ㄹ oʻzaklar, oʻtgan zamon va 못 bilan "
                       "farqi.",
        "tutorial":    "PK-30:",
        "level":       "easy",
        "questions":   Q_PK30,
    },
    {
        "title":       "PK-31 Mashq: 아/어 주다 — iltimos",
        "description": "20 savol — 아/어 shakli, 주세요, 한테/에게 va 좀 ning oʻrni.",
        "tutorial":    "PK-31:",
        "level":       "easy",
        "questions":   Q_PK31,
    },
]
