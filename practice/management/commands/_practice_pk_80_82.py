# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-80 … PK-82.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Har uchala mashqda bitta 한다체 (PK-74) savoli bor.

Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_80_82.py --master=prime \\
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


# ══════════════════════════════════════════════════════════════════════
# PK-80 — 아/어 봤자
# ══════════════════════════════════════════════════════════════════════
Q_PK80 = [
    # 1–5 tanish
    {
        "text": "<p><b>아/어 봤자</b> ning asosiy maʼnosi nima?</p>",
        "choices": ["Urinsang ham foydasi yoʻq",
                    "Qilishing bilanoq boʻladi",
                    "Qilaversang, yaxshi boʻladi",
                    "Qilganingda edi, boʻlardi"],
        "correct": "Urinsang ham foydasi yoʻq",
        "explanation": "<p>Urinishning oʻzi mumkin, lekin <b>natija "
                       "oʻzgarmaydi</b>.</p>",
    },
    {
        "text": "<p>봤자 ning ichida qaysi tanish qolip turibdi?</p>",
        "choices": ["아/어 보다 (PK-41) — “sinab koʻrmoq”",
                    "아/어 놓다 (PK-59)",
                    "고 있다 (PK-42)",
                    "아/어 주다 (PK-31)"],
        "correct": "아/어 보다 (PK-41) — “sinab koʻrmoq”",
        "explanation": "<p>봤 = 보 + 았. Yaʼni “sinab koʻrgan taqdirda "
                       "ham”.</p>",
    },
    {
        "text": "<p>봤자 dan keyingi natija qanday boʻladi?</p>",
        "choices": ["Salbiy yoki foydasiz", "Doim ijobiy",
                    "Har xil boʻlishi mumkin", "Faqat buyruq"],
        "correct": "Salbiy yoki foydasiz",
        "explanation": "<p>소용없다 · 안 되다 · 마찬가지다 · 이미 …았다 — "
                       "bularning hammasi foydasizlikni bildiradi.</p>",
    },
    {
        "text": "<p>봤자 ning ikkinchi maʼnosi qanday?</p>",
        "choices": ["“Koʻpi bilan …, undan ortiq emas”",
                    "“Albatta …”", "“Hech qachon …”", "“Birinchi navbatda …”"],
        "correct": "“Koʻpi bilan …, undan ortiq emas”",
        "explanation": "<p>비싸 봤자 삼만 원이에요 — “qancha qimmat boʻlsa "
                       "ham, koʻpi bilan oʻttiz ming von”.</p>",
    },
    {
        "text": "<p>Qaysi soʻz 봤자 bilan koʻp birga keladi?</p>",
        "choices": ["아무리", "만약", "그렇게", "이미"],
        "correct": "아무리",
        "explanation": "<p>아무리 설명해 봤자 안 들어요 — “qancha "
                       "tushuntirsangiz ham”.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 지금 <b>____</b> 기차는 이미 떠났어요. "
                "(가다)</p>",
        "choices": ["가 봤자", "갔 봤자", "가서 봤자", "갈 봤자"],
        "correct": "가 봤자",
        "explanation": "<p>가 + 봤자. Zamon 봤자 ning oʻzida bor.</p>",
    },
    {
        "text": "<p>Toʻldiring: 아무리 <b>____</b> 그 사람은 안 들어요. "
                "(설명하다)</p>",
        "choices": ["설명해 봤자", "설명하 봤자", "설명했 봤자", "설명할 봤자"],
        "correct": "설명해 봤자",
        "explanation": "<p>하다 → <b>해</b> + 봤자.</p>",
    },
    {
        "text": "<p>Toʻldiring: 지금 <b>____</b> 소용없어요. (후회하다)</p>",
        "choices": ["후회해 봤자", "후회하 봤자", "후회했 봤자", "후회하고 봤자"],
        "correct": "후회해 봤자",
        "explanation": "<p>Pushaymonlik endi hech narsani "
                       "oʻzgartirmaydi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 그 가방이 <b>____</b> 삼만 원이에요. "
                "(비싸다)</p>",
        "choices": ["비싸 봤자", "비쌌 봤자", "비쌀 봤자", "비싸서 봤자"],
        "correct": "비싸 봤자",
        "explanation": "<p>“Koʻpi bilan” maʼnosida <b>sifat</b> bilan ham "
                       "boʻladi: 비싸 + 봤자.</p>",
    },
    {
        "text": "<p>Toʻldiring: 지금 서둘러 봤자 <b>____</b>.</p>",
        "choices": ["마찬가지예요", "잘될 거예요", "성공할 거예요", "좋아요"],
        "correct": "마찬가지예요",
        "explanation": "<p>봤자 dan keyin foydasizlik keladi — "
                       "“baribir, oʻsha-oʻsha”.</p>",
    },
    {
        "text": "<p>“Bola qancha yesa ham, qancha yeyardi?” — "
                "koreyschada?</p>",
        "choices": ["아이가 먹어 봤자 얼마나 먹겠어요?",
                    "아이가 먹다가는 얼마나 먹어요?",
                    "아이가 먹었더라면 얼마나 먹어요?",
                    "아이가 먹을 만큼 얼마나 먹어요?"],
        "correct": "아이가 먹어 봤자 얼마나 먹겠어요?",
        "explanation": "<p>“Koʻpi bilan” maʼnosi — miqdorni kichraytirib "
                       "koʻrsatish.</p>",
    },
    {
        "text": "<p>Bu gapni 한다체 ga oʻgiring (PK-74): "
                "지금 가 봤자 소용없어요.</p>",
        "choices": ["지금 가 봤자 소용없다.", "지금 가 봤자 소용없는다.",
                    "지금 가 봤자 소용없이다.", "지금 가 봤자 소용없었다."],
        "correct": "지금 가 봤자 소용없다.",
        "explanation": "<p>없다 한다체 da <b>oʻzgarmaydi</b> — 없는다 "
                       "notoʻgʻri.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu gap qaysi maʼnoda? 그 가방이 비싸 봤자 삼만 "
                "원이에요.</p>",
        "choices": ["“Koʻpi bilan” — ikkinchi gapda raqam turgani buni "
                    "koʻrsatadi",
                    "“Foydasi yoʻq”",
                    "“Juda qimmat”",
                    "“Arzon emas”"],
        "correct": "“Koʻpi bilan” — ikkinchi gapda raqam turgani buni "
                   "koʻrsatadi",
        "explanation": "<p>Qaysi maʼno ekanini <b>ikkinchi gap</b> aytib "
                       "beradi: raqam → “koʻpi bilan”, 소용없다 → “foydasi "
                       "yoʻq”.</p>",
    },
    {
        "text": "<p><b>아/어 봤자</b> va <b>다가는</b> (PK-79) farqi nima?</p>",
        "choices": ["봤자 — “urinma, natija oʻzgarmaydi”; 다가는 — “toʻxtat, "
                    "yomon boʻladi”",
                    "봤자 — kelajak; 다가는 — oʻtmish",
                    "봤자 — yozma; 다가는 — ogʻzaki",
                    "Farqi yoʻq"],
        "correct": "봤자 — “urinma, natija oʻzgarmaydi”; 다가는 — “toʻxtat, "
                   "yomon boʻladi”",
        "explanation": "<p>봤자 <b>qoʻl siltaydi</b>, 다가는 esa "
                       "<b>ogohlantiradi</b>.</p>",
    },
    {
        "text": "<p>Qaysi jumla notoʻgʻri?</p>",
        "choices": ["열심히 공부해 봤자 시험에 붙을 거예요.",
                    "지금 가 봤자 기차는 이미 떠났어요.",
                    "아무리 설명해 봤자 그 사람은 안 들어요.",
                    "지금 후회해 봤자 소용없어요."],
        "correct": "열심히 공부해 봤자 시험에 붙을 거예요.",
        "explanation": "<p>봤자 dan keyin <b>ijobiy</b> natija kelmaydi. "
                       "Yaxshi natija uchun — <b>다가 보면</b> (PK-77).</p>",
    },
    {
        "text": "<p>Nega 봤자 oldida zamon qoʻyilmaydi?</p>",
        "choices": ["Chunki oʻtgan zamon 봤자 ning oʻzida bor (봤 = 보 + 았)",
                    "Chunki 봤자 faqat kelajak haqida",
                    "Chunki 자 zamonni bekor qiladi",
                    "Chunki natija salbiy"],
        "correct": "Chunki oʻtgan zamon 봤자 ning oʻzida bor (봤 = 보 + 았)",
        "explanation": "<p>❌ 갔 봤자 → ✅ <b>가 봤자</b>.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <s>지금 갔 봤자 소용없어요.</s></p>",
        "choices": ["Zamon 봤자 ichida bor — 가 봤자",
                    "소용없어요 emas, 소용없다",
                    "지금 emas, 이제",
                    "봤자 emas, 봐자"],
        "correct": "Zamon 봤자 ichida bor — 가 봤자",
        "explanation": "<p>봤 = 보 + 았. Oldiga yana 았 qoʻyilmaydi.</p>",
    },
    {
        "text": "<p>Xatoni toping: <s>지금 가 봤자 빨리 가세요.</s></p>",
        "choices": ["봤자 dan keyin buyruq emas, foydasizlik keladi",
                    "가 봤자 emas, 갈 봤자",
                    "빨리 emas, 천천히",
                    "가세요 emas, 가요"],
        "correct": "봤자 dan keyin buyruq emas, foydasizlik keladi",
        "explanation": "<p>Toʻgʻrisi — 지금 가 봤자 <b>소용없어요</b>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>“Qancha tushuntirsangiz ham, u odam eshitmaydi” — "
                "koreyschada?</p>",
        "choices": ["아무리 설명해 봤자 그 사람은 안 들어요.",
                    "아무리 설명하다가는 그 사람은 안 들어요.",
                    "아무리 설명했더라면 그 사람은 안 들어요.",
                    "아무리 설명하자마자 그 사람은 안 들어요."],
        "correct": "아무리 설명해 봤자 그 사람은 안 들어요.",
        "explanation": "<p>아무리 + 봤자 — qolipning eng klassik "
                       "juftligi.</p>",
    },
    {
        "text": "<p>“Hozir borganingiz bilan poyezd allaqachon ketgan” — "
                "koreyschada?</p>",
        "choices": ["지금 가 봤자 기차는 이미 떠났어요.",
                    "지금 가다가는 기차는 이미 떠났어요.",
                    "지금 갔더라면 기차는 이미 떠났어요.",
                    "지금 가는 김에 기차는 이미 떠났어요."],
        "correct": "지금 가 봤자 기차는 이미 떠났어요.",
        "explanation": "<p><b>이미 …았/었다</b> — 봤자 ning eng tabiiy "
                       "ikkinchi gaplaridan biri.</p>",
    },
]


# ══════════════════════════════════════════════════════════════════════
# PK-81 — (으)ㄹ지라도, 더라도, (으)ㅁ에도 불구하고
# ══════════════════════════════════════════════════════════════════════
Q_PK81 = [
    # 1–5 tanish
    {
        "text": "<p><b>더라도</b> qanday maʼno beradi?</p>",
        "choices": ["Nima boʻlsa ham (kuchli yon berish)",
                    "…ishi bilanoq", "…ganing bilan foydasi yoʻq",
                    "…gudek darajada"],
        "correct": "Nima boʻlsa ham (kuchli yon berish)",
        "explanation": "<p>Sharoit yomon boʻlsa ham qaror "
                       "oʻzgarmaydi.</p>",
    },
    {
        "text": "<p><b>(으)ㅁ에도 불구하고</b> nima haqida gapiradi?</p>",
        "choices": ["Allaqachon boʻlgan FAKT",
                    "Kelajakdagi faraz",
                    "Har kuni takrorlanadigan odat",
                    "Buyruq"],
        "correct": "Allaqachon boʻlgan FAKT",
        "explanation": "<p>Bu asosiy chegara: 더라도 — faraz, "
                       "에도 불구하고 — fakt.</p>",
    },
    {
        "text": "<p><b>(으)ㄹ지라도</b> qaysi uslubga tegishli?</p>",
        "choices": ["Kitobiy — yozma matn, nutq, shior",
                    "Kundalik suhbat",
                    "Bolalar tili",
                    "Faqat soʻroq gaplarda"],
        "correct": "Kitobiy — yozma matn, nutq, shior",
        "explanation": "<p>Doʻstga aytilsa gʻalati eshitiladi — unda "
                       "<b>더라도</b> ishlatiladi.</p>",
    },
    {
        "text": "<p><b>불구하고</b> ning hanzuviy asosi 不拘 nimani "
                "bildiradi?</p>",
        "choices": ["“Bogʻlanmasdan, qaramasdan”",
                    "“Toʻxtatmasdan”", "“Bilmasdan”", "“Koʻrmasdan”"],
        "correct": "“Bogʻlanmasdan, qaramasdan”",
        "explanation": "<p>Oʻzbekcha “<b>qaramay</b>” ham xuddi shu obraz: "
                       "“bu meni toʻxtatmaydi”.</p>",
    },
    {
        "text": "<p>(으)ㅁ에도 불구하고 dagi (으)ㅁ qaysi darsdan tanish?</p>",
        "choices": ["PK-46 — otlashtirish (는 것, 기, (으)ㅁ)",
                    "PK-43 — aniqlovchi 는",
                    "PK-56 — majhul nisbat",
                    "PK-33 — 고"],
        "correct": "PK-46 — otlashtirish (는 것, 기, (으)ㅁ)",
        "explanation": "<p>노력하다 → <b>노력함</b>, 노력했다 → "
                       "<b>노력했음</b>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 무슨 일이 <b>____</b> 저는 갈 거예요. "
                "(있다)</p>",
        "choices": ["있더라도", "있었더라도", "있을더라도", "있음에도"],
        "correct": "있더라도",
        "explanation": "<p>더라도 farazga qaraydi — oldida zamon "
                       "boʻlmaydi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 몸이 <b>____</b> 약속은 지킬 것이다. "
                "(아프다)</p>",
        "choices": ["아플지라도", "아픔지라도", "아파지라도", "아팠지라도"],
        "correct": "아플지라도",
        "explanation": "<p>아프 da 받침 yoʻq → <b>ㄹ지라도</b>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 여러 번 <b>____</b> 불구하고 결과는 좋지 "
                "않았다. (노력하다 — oʻtgan zamon)</p>",
        "choices": ["노력했음에도", "노력하음에도", "노력함에도", "노력해음에도"],
        "correct": "노력했음에도",
        "explanation": "<p>Oʻtgan zamon → <b>했음</b>. ❌ 하음 degan shakl "
                       "yoʻq.</p>",
    },
    {
        "text": "<p>Toʻldiring: 시간이 <b>____</b> 책은 매일 읽으세요. "
                "(없다)</p>",
        "choices": ["없더라도", "없었더라도", "없음에도", "없을지라도"],
        "correct": "없더라도",
        "explanation": "<p>Buyruq bilan ishlatilganda kundalik va tabiiy "
                       "shakl — <b>더라도</b>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 나이가 <b>____</b> 불구하고 그 학생은 아주 "
                "침착하다. (어리다)</p>",
        "choices": ["어림에도", "어릴지라도", "어리더라도", "어렸음에는"],
        "correct": "어림에도",
        "explanation": "<p>어리다 → <b>어림</b> + 에도 불구하고. Bu allaqachon "
                       "haqiqat.</p>",
    },
    {
        "text": "<p>Toʻldiring: 비<b>____</b> 불구하고 경기는 계속되었다.</p>",
        "choices": ["에도", "임에도", "함에도", "라도"],
        "correct": "에도",
        "explanation": "<p><b>Ot</b> bilan toʻgʻridan toʻgʻri: "
                       "비<b>에도</b> 불구하고.</p>",
    },
    {
        "text": "<p>Bu gapni 한다체 ga oʻgiring (PK-74): "
                "무슨 일이 있더라도 저는 갈 거예요.</p>",
        "choices": ["무슨 일이 있더라도 나는 갈 것이다.",
                    "무슨 일이 있더라도 나는 간다 것이다.",
                    "무슨 일이 있었더라도 나는 갈 것이다.",
                    "무슨 일이 있더라도 나는 갈 거다."],
        "correct": "무슨 일이 있더라도 나는 갈 것이다.",
        "explanation": "<p>(으)ㄹ 거예요 → <b>(으)ㄹ 것이다</b>, va 한다체 da "
                       "odatda 저 emas, <b>나</b>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>“노력하더라도 안 될 거예요” va “노력했음에도 불구하고 안 "
                "됐어요” farqi nima?</p>",
        "choices": ["Birinchisi — hali harakat qilmagan (faraz); "
                    "ikkinchisi — harakat qilgan va boʻlmagan (fakt)",
                    "Birinchisi — rasmiy; ikkinchisi — ogʻzaki",
                    "Birinchisi — oʻtmish; ikkinchisi — kelajak",
                    "Farqi yoʻq"],
        "correct": "Birinchisi — hali harakat qilmagan (faraz); "
                   "ikkinchisi — harakat qilgan va boʻlmagan (fakt)",
        "explanation": "<p>Bu darsning asosiy chegarasi: <b>faraz ↔ "
                       "fakt</b>.</p>",
    },
    {
        "text": "<p>“Ertaga yomgʻir yogʻsa ham boraman” — qaysi qolip?</p>",
        "choices": ["내일 비가 오더라도 갈 거예요.",
                    "내일 비가 옴에도 불구하고 갈 거예요.",
                    "내일 비가 왔음에도 불구하고 갈 거예요.",
                    "내일 비가 와 봤자 갈 거예요."],
        "correct": "내일 비가 오더라도 갈 거예요.",
        "explanation": "<p>Ertaga — hali <b>fakt emas</b>. Faraz uchun "
                       "<b>더라도</b>.</p>",
    },
    {
        "text": "<p>Doʻstingizga “qiyin boʻlsa ham voz kechma” demoqchisiz. "
                "Qaysi qolip tabiiy?</p>",
        "choices": ["힘들더라도 포기하지 마.", "힘들지라도 포기하지 마.",
                    "힘듦에도 불구하고 포기하지 마.", "힘들어 봤자 포기하지 마."],
        "correct": "힘들더라도 포기하지 마.",
        "explanation": "<p>(으)ㄹ지라도 va 에도 불구하고 — <b>kitobiy</b>. "
                       "Suhbatda 더라도.</p>",
    },
    {
        "text": "<p>PK-80 dagi <b>봤자</b> va bugungi <b>더라도</b> "
                "orasidagi farq nima?</p>",
        "choices": ["봤자 — “urinma, natija oʻzgarmaydi”; 더라도 — “boʻlsa "
                    "ham baribir qilaman”",
                    "봤자 — kelajak; 더라도 — oʻtmish",
                    "봤자 — fakt; 더라도 — faraz",
                    "Farqi yoʻq"],
        "correct": "봤자 — “urinma, natija oʻzgarmaydi”; 더라도 — “boʻlsa "
                   "ham baribir qilaman”",
        "explanation": "<p>Biri <b>qoʻl siltaydi</b>, ikkinchisi "
                       "<b>turib oladi</b>.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <s>노력하음에도 불구하고 실패했어요.</s></p>",
        "choices": ["하다 → 함 / 했음 — 노력했음에도 boʻlishi kerak",
                    "불구하고 emas, 불고하고",
                    "실패했어요 emas, 실패해요",
                    "에도 emas, 에는"],
        "correct": "하다 → 함 / 했음 — 노력했음에도 boʻlishi kerak",
        "explanation": "<p>❌ 하음 degan shakl yoʻq. (으)ㅁ otlashtirishi "
                       "하다 dan <b>함</b> yasaydi.</p>",
    },
    {
        "text": "<p>Xatoni toping: <s>무슨 일이 있었더라도 저는 갈 "
                "거예요.</s></p>",
        "choices": ["더라도 oldida zamon boʻlmaydi — 있더라도",
                    "무슨 일이 emas, 무슨 일을",
                    "갈 거예요 emas, 갔어요",
                    "저는 emas, 제가"],
        "correct": "더라도 oldida zamon boʻlmaydi — 있더라도",
        "explanation": "<p>더라도 hali boʻlmagan holatni tasavvur "
                       "qiladi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>“Bir necha marta harakat qilganiga qaramay, natija "
                "yaxshi boʻlmadi” — koreyschada?</p>",
        "choices": ["여러 번 노력했음에도 불구하고 결과는 좋지 않았다.",
                    "여러 번 노력하더라도 결과는 좋지 않았다.",
                    "여러 번 노력할지라도 결과는 좋지 않았다.",
                    "여러 번 노력해 봤자 결과는 좋지 않았다."],
        "correct": "여러 번 노력했음에도 불구하고 결과는 좋지 않았다.",
        "explanation": "<p>Harakat <b>boʻlgan</b> — bu fakt, shuning uchun "
                       "에도 불구하고.</p>",
    },
    {
        "text": "<p>“Natija yomon boʻlsa-da, pushaymon boʻlmayman” "
                "(kitobiy uslubda) — koreyschada?</p>",
        "choices": ["결과가 나쁠지라도 후회하지 않을 것이다.",
                    "결과가 나쁘더라도 후회하지 않아요.",
                    "결과가 나쁨에도 불구하고 후회하지 않을 것이다.",
                    "결과가 나빠 봤자 후회하지 않을 것이다."],
        "correct": "결과가 나쁠지라도 후회하지 않을 것이다.",
        "explanation": "<p>(으)ㄹ지라도 + (으)ㄹ 것이다 — ikkalasi ham kitobiy "
                       "uslub, bir-biriga mos.</p>",
    },
]


# ══════════════════════════════════════════════════════════════════════
# PK-82 — (으)ㄹ 정도로 / (으)ㄹ 만큼
# ══════════════════════════════════════════════════════════════════════
Q_PK82 = [
    # 1–5 tanish
    {
        "text": "<p><b>정도</b> soʻzining maʼnosi nima?</p>",
        "choices": ["Daraja, oʻlcham", "Miqdor", "Yoʻl", "Holat"],
        "correct": "Daraja, oʻlcham",
        "explanation": "<p>程度. Shuning uchun (으)ㄹ 정도로 = “…gudek "
                       "darajada”.</p>",
    },
    {
        "text": "<p><b>(으)ㄹ 만큼</b> nimani koʻrsatadi?</p>",
        "choices": ["Miqdor va tenglik — “shuncha, shu qadar”",
                    "Sabab", "Vaqt", "Maqsad"],
        "correct": "Miqdor va tenglik — “shuncha, shu qadar”",
        "explanation": "<p>먹을 만큼 드세요 — “qancha yeysiz, shuncha "
                       "oling”.</p>",
    },
    {
        "text": "<p>정도로 va 만큼 oldida qanday aniqlovchi turadi?</p>",
        "choices": ["(으)ㄹ (oʻtgan ish uchun 만큼 bilan (으)ㄴ ham boʻladi)",
                    "Faqat 는", "Faqat (으)ㄴ", "Aniqlovchi kerak emas"],
        "correct": "(으)ㄹ (oʻtgan ish uchun 만큼 bilan (으)ㄴ ham boʻladi)",
        "explanation": "<p>배가 <b>아플</b> 정도로 · <b>노력한</b> 만큼.</p>",
    },
    {
        "text": "<p>Koreyscha gapda oʻlchov qayerda turadi?</p>",
        "choices": ["Asosiy feʼldan OLDIN",
                    "Asosiy feʼldan KEYIN",
                    "Gapning oxirida",
                    "Farqi yoʻq"],
        "correct": "Asosiy feʼldan OLDIN",
        "explanation": "<p><b>배가 아플 정도로</b> 웃었어요 — oʻzbekcha "
                       "tarjimada ham xuddi shu tartib.</p>",
    },
    {
        "text": "<p>Ikki odamni tenglashtirish uchun qaysi qolip "
                "ishlatiladi?</p>",
        "choices": ["만큼 — 언니만큼 노래를 잘해요",
                    "정도로 — 언니 정도로 노래를 잘해요",
                    "Ikkalasi ham",
                    "Hech qaysisi"],
        "correct": "만큼 — 언니만큼 노래를 잘해요",
        "explanation": "<p>Tenglashtirish — <b>faqat 만큼</b>. Va u ot "
                       "bilan toʻgʻridan toʻgʻri ishlatiladi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 배가 <b>____</b> 정도로 웃었어요. (아프다)</p>",
        "choices": ["아플", "아픈", "아파", "아팠던"],
        "correct": "아플",
        "explanation": "<p>정도로 oldida <b>(으)ㄹ</b> aniqlovchisi.</p>",
    },
    {
        "text": "<p>Toʻldiring: <b>____</b> 만큼 드세요. (먹다)</p>",
        "choices": ["먹을", "먹는", "먹은", "먹어"],
        "correct": "먹을",
        "explanation": "<p>“Yeydiganingizcha” — <b>먹을 만큼</b>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 눈을 뜰 수 <b>____</b> 정도로 바람이 "
                "강했어요. (없다)</p>",
        "choices": ["없을", "없는", "없은", "없어"],
        "correct": "없을",
        "explanation": "<p>없다 → <b>없을</b> 정도로.</p>",
    },
    {
        "text": "<p>Toʻldiring: <b>____</b> 만큼 결과가 나와요. "
                "(노력하다 — oʻtgan ish)</p>",
        "choices": ["노력한", "노력할", "노력하는", "노력했을"],
        "correct": "노력한",
        "explanation": "<p>Allaqachon qilingan ish uchun "
                       "<b>(으)ㄴ 만큼</b>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 말도 못 <b>____</b> 정도로 피곤했어요.</p>",
        "choices": ["할", "한", "해", "했던"],
        "correct": "할",
        "explanation": "<p>못 <b>할</b> 정도로 — “gapira olmaydigan "
                       "darajada”.</p>",
    },
    {
        "text": "<p>“Shuncha boʻlsa yetarli” — koreyschada?</p>",
        "choices": ["이 정도면 충분해요.", "이 만큼이면 충분해요.",
                    "이 정도로 충분해요.", "이 만큼 충분해요."],
        "correct": "이 정도면 충분해요.",
        "explanation": "<p>정도 <b>ot</b> sifatida ham ishlatiladi: "
                       "이 정도, 그 정도.</p>",
    },
    {
        "text": "<p>Bu gapni 한다체 ga oʻgiring (PK-74): "
                "말도 못 할 정도로 피곤했어요.</p>",
        "choices": ["말도 못 할 정도로 피곤했다.",
                    "말도 못 할 정도로 피곤한다.",
                    "말도 못 할 정도로 피곤했는다.",
                    "말도 못 할 정도로 피곤하다 했다."],
        "correct": "말도 못 할 정도로 피곤했다.",
        "explanation": "<p>피곤하다 — sifat, oʻtgan zamon <b>했다</b>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>정도로 va 만큼 orasidagi asosiy farq nima?</p>",
        "choices": ["정도로 — daraja va kuch; 만큼 — miqdor va tenglik",
                    "정도로 — oʻtmish; 만큼 — kelajak",
                    "정도로 — feʼl bilan; 만큼 — sifat bilan",
                    "정도로 — rasmiy; 만큼 — ogʻzaki"],
        "correct": "정도로 — daraja va kuch; 만큼 — miqdor va tenglik",
        "explanation": "<p>배가 아플 정도로 웃었어요 (qanchalik kuchli) ↔ "
                       "먹을 만큼 드세요 (qancha miqdor).</p>",
    },
    {
        "text": "<p>Qaysi jumla notoʻgʻri?</p>",
        "choices": ["아프소나 씨는 언니 정도로 노래를 잘해요.",
                    "아프소나 씨는 언니만큼 노래를 잘해요.",
                    "배가 아플 정도로 웃었어요.",
                    "먹을 만큼 드세요."],
        "correct": "아프소나 씨는 언니 정도로 노래를 잘해요.",
        "explanation": "<p>Ikki odamni <b>tenglashtirish</b> — faqat "
                       "<b>만큼</b>.</p>",
    },
    {
        "text": "<p>“죽을 정도로 힘들었어요” va “죽을 만큼 힘들었어요” — "
                "qaysi toʻgʻri?</p>",
        "choices": ["Ikkalasi ham toʻgʻri — farq faqat urgʻuda",
                    "Faqat birinchisi",
                    "Faqat ikkinchisi",
                    "Ikkalasi ham notoʻgʻri"],
        "correct": "Ikkalasi ham toʻgʻri — farq faqat urgʻuda",
        "explanation": "<p>정도로 darajaga, 만큼 miqdorga urgʻu beradi. "
                       "Lekin tenglashtirish maʼnosida faqat 만큼.</p>",
    },
    {
        "text": "<p>“Qancha yeysiz, shuncha oling” — bu daraja soʻzimi "
                "yoki miqdor?</p>",
        "choices": ["Miqdor — shuning uchun 만큼",
                    "Daraja — shuning uchun 정도로",
                    "Ikkalasi ham emas",
                    "Sabab"],
        "correct": "Miqdor — shuning uchun 만큼",
        "explanation": "<p>먹을 <b>만큼</b> 드세요. ❌ 먹을 정도로 "
                       "드세요.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <s>웃었어요 배가 아플 정도로.</s></p>",
        "choices": ["Oʻlchov asosiy feʼldan OLDIN turadi — "
                    "배가 아플 정도로 웃었어요",
                    "아플 emas, 아픈",
                    "배가 emas, 배는",
                    "정도로 emas, 만큼"],
        "correct": "Oʻlchov asosiy feʼldan OLDIN turadi — "
                   "배가 아플 정도로 웃었어요",
        "explanation": "<p>Bu qolipdagi eng koʻp uchraydigan xato. "
                       "Oʻzbekcha tarjimadagi tartib ham xuddi shunday.</p>",
    },
    {
        "text": "<p>Xatoni toping: <s>배가 아픈 정도로 웃었어요.</s></p>",
        "choices": ["정도로 oldida (으)ㄹ kerak — 아플 정도로",
                    "웃었어요 emas, 웃어요",
                    "배가 emas, 배를",
                    "정도로 emas, 정도에"],
        "correct": "정도로 oldida (으)ㄹ kerak — 아플 정도로",
        "explanation": "<p>Qorin ogʻrigani <b>haqiqatan boʻlgan</b> emas — "
                       "u faqat oʻlchov sifatida tasavvur qilinyapti.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>“Koʻzni ocha olmaydigan darajada shamol kuchli edi” — "
                "koreyschada?</p>",
        "choices": ["눈을 뜰 수 없을 정도로 바람이 강했어요.",
                    "바람이 강했어요 눈을 뜰 수 없을 정도로.",
                    "눈을 뜰 수 없는 정도로 바람이 강했어요.",
                    "눈을 뜰 수 없을 만큼 바람이 강해요."],
        "correct": "눈을 뜰 수 없을 정도로 바람이 강했어요.",
        "explanation": "<p>Oʻlchov oldinda, (으)ㄹ aniqlovchisi bilan.</p>",
    },
    {
        "text": "<p>“Afsona opasi qadar yaxshi qoʻshiq aytadi” — "
                "koreyschada?</p>",
        "choices": ["아프소나 씨는 언니만큼 노래를 잘해요.",
                    "아프소나 씨는 언니 정도로 노래를 잘해요.",
                    "아프소나 씨는 언니를 만큼 노래를 잘해요.",
                    "아프소나 씨는 언니만큼이 노래를 잘해요."],
        "correct": "아프소나 씨는 언니만큼 노래를 잘해요.",
        "explanation": "<p>만큼 <b>ot bilan toʻgʻridan toʻgʻri</b> "
                       "qoʻshiladi — qoʻshimcha kerak emas.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-80 Mashq: 아/어 봤자",
        "description": "20 savol — behuda urinish, zamon qoidasi, "
                       "majburiy foydasiz natija va “koʻpi bilan” "
                       "maʼnosi.",
        "tutorial":    "PK-80:",
        "level":       "medium",
        "questions":   Q_PK80,
    },
    {
        "title":       "PK-81 Mashq: 더라도 · (으)ㄹ지라도 · (으)ㅁ에도 불구하고",
        "description": "20 savol — yon berishning uch darajasi, faraz va "
                       "fakt chegarasi, (으)ㅁ otlashtirishi va uslub "
                       "tanlash.",
        "tutorial":    "PK-81:",
        "level":       "medium",
        "questions":   Q_PK81,
    },
    {
        "title":       "PK-82 Mashq: (으)ㄹ 정도로 · (으)ㄹ 만큼",
        "description": "20 savol — daraja va miqdor farqi, gapdagi "
                       "tartib, (으)ㄹ aniqlovchisi va ot bilan "
                       "tenglashtirish.",
        "tutorial":    "PK-82:",
        "level":       "medium",
        "questions":   Q_PK82,
    },
]
