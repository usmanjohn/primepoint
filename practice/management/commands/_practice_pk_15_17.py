# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-15 … PK-17.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_15_17.py --master=prime \\
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
# PK-15 — 이거/그거/저거 va 여기/거기/저기
# =====================================================================

Q_PK15 = [
    # 1–5 tanish
    {
        "text": "<p>Koreys tilida koʻrsatish necha pogʻonali?</p>",
        "choices": ["Uch — 이 / 그 / 저", "Ikki — 이 / 저",
                    "Toʻrt — 이 / 그 / 저 / 어", "Bir — faqat 이"],
        "correct": "Uch — 이 / 그 / 저",
        "explanation": "<p><strong>Uch pogʻona</strong>, xuddi oʻzbekchadagi "
                       "<em>bu · shu · u</em> kabi. Ingliz tilida esa faqat ikkita "
                       "(this / that), shuning uchun ingliz tilidan oʻrganuvchi 그 va 저 "
                       "ni doim adashtiradi.</p>",
    },
    {
        "text": "<p><strong>그것</strong> qachon ishlatiladi?</p>",
        "choices": ["Tinglovchi tomonidagi yoki aytib oʻtilgan narsa uchun",
                    "Gapiruvchi qoʻlidagi narsa uchun",
                    "Ikkalasidan uzoqdagi narsa uchun",
                    "Faqat savolda"],
        "correct": "Tinglovchi tomonidagi yoki aytib oʻtilgan narsa uchun",
        "explanation": "<p><strong>그</strong> = oʻzbekcha “shu”. U tinglovchiga yaqin "
                       "narsani <em>yoki</em> ikkalangiz allaqachon gapirgan narsani "
                       "bildiradi.</p>",
    },
    {
        "text": "<p>“Bu yer” koreyschada qanday?</p>",
        "choices": ["여기", "거기", "저기", "어디"],
        "correct": "여기",
        "explanation": "<p><strong>여기</strong> — bu yer. 거기 = shu yer, 저기 = u yer, "
                       "어디 = qayer.</p>",
    },
    {
        "text": "<p><strong>것</strong> nima degani?</p>",
        "choices": ["narsa", "odam", "joy", "vaqt"],
        "correct": "narsa",
        "explanation": "<p><strong>것</strong> = “narsa”, shuning uchun 이것 = “bu narsa”. "
                       "Ot qoʻshilsa 것 keraksiz boʻlib tushadi: 이 책.</p>",
    },
    {
        "text": "<p><strong>누구</strong> nima degani?</p>",
        "choices": ["kim", "nima", "qayer", "qachon"],
        "correct": "kim",
        "explanation": "<p><strong>누구</strong> = kim. 무엇/뭐 = nima, 어디 = qayer. "
                       "Ega shaklida 누구 + 가 → <em>누가</em> boʻladi (PK-12).</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Suhbatdoshingiz qoʻlidagi kitobga qanday koʻrsatasiz?</p>",
        "choices": ["그 책", "이 책", "저 책", "어느 책"],
        "correct": "그 책",
        "explanation": "<p><strong>그</strong> — tinglovchi tomonidagi narsa, oʻzbekcha "
                       "“shu”. 이 sizda boʻlgan narsa uchun, 저 esa ikkalangizdan ham "
                       "uzoqdagi narsa uchun.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ 책은 제 책입니다.</strong> "
                "(“bu kitob”)</p>",
        "choices": ["이", "이것", "이것은", "여기"],
        "correct": "이",
        "explanation": "<p><strong>이</strong>. Ot (책) qoʻshilganda <strong>것 "
                       "tushadi</strong>, shuning uchun <s>이것 책</s> emas, "
                       "<b>이 책</b>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>책이 여기___ 있습니다.</strong></p>",
        "choices": ["에", "에서", "이", "은"],
        "correct": "에",
        "explanation": "<p><strong>에</strong> — 있다/없다 bilan har doim 에 (PK-14). "
                       "여기에 = “bu yerda”.</p>",
    },
    {
        "text": "<p>“Oʻqituvchi anavi yerda” ni koreyschaga oʻgiring.</p>",
        "choices": ["선생님은 저기에 계십니다.", "선생님은 여기에 있습니다.",
                    "선생님은 저기에서 계십니다.", "선생님은 거기에 계십니다."],
        "correct": "선생님은 저기에 계십니다.",
        "explanation": "<p><strong>저기</strong> (uzoqdagi joy) + <strong>에</strong> "
                       "(있다/계시다 bilan) + <strong>계십니다</strong> (hurmatli odam "
                       "haqida gap ketyapti).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ 사람은 누구입니까?</strong> "
                "(“anavi odam”)</p>",
        "choices": ["저", "저것", "저기", "그것"],
        "correct": "저",
        "explanation": "<p><strong>저 사람</strong> — “anavi odam”. Odam uchun 것 emas, "
                       "사람 ishlatiladi; 저것 esa narsa uchun.</p>",
    },
    {
        "text": "<p>“이것은 무엇입니까?” savoliga tabiiy javob qaysi?</p>",
        "choices": ["그것은 가방입니다.", "이것은 가방입니다.",
                    "저것은 가방입니다.", "여기는 가방입니다."],
        "correct": "그것은 가방입니다.",
        "explanation": "<p>Narsa <em>savol beruvchida</em>, ya'ni javob beruvchi uchun u "
                       "“shu” — <strong>그것</strong>. Pogʻona kim qarayotganiga qarab "
                       "almashadi, xuddi oʻzbekchadagi bu/shu kabi.</p>",
    },
    {
        "text": "<p>Ogʻzaki nutqda <strong>이것</strong> qanday qisqaradi?</p>",
        "choices": ["이거", "이게", "여기", "이의"],
        "correct": "이거",
        "explanation": "<p><strong>이거</strong> — ogʻzaki shakl. 이것<em>이</em> esa "
                       "<strong>이게</strong> boʻlib qisqaradi. Darslikda 이것, koʻchada "
                       "deyarli har doim 이거 eshitasiz.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>그것</strong> va <strong>저것</strong> farqi nima?</p>",
        "choices": ["그것 — tinglovchida, 저것 — ikkalasidan uzoq",
                    "그것 — uzoqda, 저것 — tinglovchida",
                    "그것 — gapiruvchida, 저것 — tinglovchida",
                    "Farqi yoʻq"],
        "correct": "그것 — tinglovchida, 저것 — ikkalasidan uzoq",
        "explanation": "<p>Oʻzbekcha bilan solishtiring: <strong>그것</strong> = “shu”, "
                       "<strong>저것</strong> = “u / anavi”. Ingliz tilida ikkalasi ham "
                       "<em>that</em>, shuning uchun bu farq u yerdan oʻrganuvchi uchun "
                       "qiyin.</p>",
    },
    {
        "text": "<p>Bu ikki gapdagi <strong>저</strong> bir xilmi?<br>"
                "(a) 저는 학생입니다. &nbsp;(b) 저 사람은 학생입니다.</p>",
        "choices": ["Yoʻq — (a) “men”, (b) “anavi”",
                    "Ha, ikkalasi ham “men”",
                    "Ha, ikkalasi ham “anavi”",
                    "Yoʻq — (a) “anavi”, (b) “men”"],
        "correct": "Yoʻq — (a) “men”, (b) “anavi”",
        "explanation": "<p>Farqni <strong>keyingi soʻz</strong> aytib turadi: 저 dan keyin "
                       "qoʻshimcha (는) kelsa — “men”; darhol ot (사람) kelsa — "
                       "“anavi”.</p>",
    },
    {
        "text": "<p>Qaysi qatorda joy shakllari toʻgʻri berilgan?</p>",
        "choices": ["여기 / 거기 / 저기", "이것 / 그것 / 저것",
                    "이 사람 / 그 사람 / 저 사람", "무엇 / 누구 / 어디"],
        "correct": "여기 / 거기 / 저기",
        "explanation": "<p><strong>여기 / 거기 / 저기</strong> — joy uchun. Narsa uchun "
                       "이것/그것/저것, odam uchun 이 사람/그 사람/저 사람.</p>",
    },
    {
        "text": "<p>Nega ingliz tilidan oʻrganuvchi 그 va 저 ni adashtiradi, oʻzbek "
                "oʻquvchi esa yoʻq?</p>",
        "choices": ["Ingliz tilida ikki pogʻona bor, oʻzbek va koreys tilida uchta",
                    "Ingliz tilida koʻrsatish umuman yoʻq",
                    "Oʻzbek tilida toʻrt pogʻona bor",
                    "Koreys tilida ikki pogʻona bor"],
        "correct": "Ingliz tilida ikki pogʻona bor, oʻzbek va koreys tilida uchta",
        "explanation": "<p>Ingliz tili <em>this / that</em> bilan cheklangan, oʻzbek tilida "
                       "esa <strong>bu · shu · u</strong> — koreyscha 이 · 그 · 저 bilan "
                       "aynan mos. Tarjima tayyor turibdi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["이것 책은 제 책입니다.", "이 책은 제 책입니다.",
                    "이것은 책입니다.", "그 책은 자수르 씨 책입니다."],
        "correct": "이것 책은 제 책입니다.",
        "explanation": "<p>Ot qoʻshilganda <strong>것 tushadi</strong>: "
                       "<em>이 책은 제 책입니다.</em> 이것 yolgʻiz turganda esa toʻgʻri: "
                       "<em>이것은 책입니다.</em></p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["책이 여기에 있습니다.", "책이 여기 있습니다.",
                    "책이 여기에서 있습니다.", "책은 여기에 계십니다."],
        "correct": "책이 여기에 있습니다.",
        "explanation": "<p>Joy + <strong>에</strong> + <strong>있습니다</strong>. 에서 "
                       "notoʻgʻri (bu holat, harakat emas), 계십니다 esa faqat odamlar "
                       "uchun.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 저 사람은 누구입니까?<br>나: ___</strong></p>",
        "choices": ["그 사람은 선생님입니다.", "저것은 선생님입니다.",
                    "여기는 선생님입니다.", "그 사람은 어디입니까?"],
        "correct": "그 사람은 선생님입니다.",
        "explanation": "<p>Savol odam haqida (누구), shuning uchun javobda ham "
                       "<strong>사람</strong> ishlatiladi. 저것 narsa uchun, 여기 esa joy "
                       "uchun.</p>",
    },
    {
        "text": "<p>Sinfxonada turibsiz. Eshik uzoqda, kitob qoʻlingizda. Qaysi qator "
                "toʻgʻri?</p>",
        "choices": ["이것은 책입니다. 저것은 문입니다.",
                    "저것은 책입니다. 이것은 문입니다.",
                    "그것은 책입니다. 여기는 문입니다.",
                    "이것은 문입니다. 그것은 책입니다."],
        "correct": "이것은 책입니다. 저것은 문입니다.",
        "explanation": "<p>Kitob <em>sizda</em> → <strong>이것</strong>. Eshik "
                       "<em>ikkalangizdan uzoq</em> → <strong>저것</strong>.</p>",
    },
]


# =====================================================================
# PK-16 — 도, 만, 부터, 까지, 하고/와/과
# =====================================================================

Q_PK16 = [
    # 1–5 tanish
    {
        "text": "<p><strong>도</strong> nima degani?</p>",
        "choices": ["ham", "faqat", "-dan", "va"],
        "correct": "ham",
        "explanation": "<p><strong>도</strong> = “ham”: 저도 학생입니다 — “Men ham "
                       "talabaman”.</p>",
    },
    {
        "text": "<p><strong>만</strong> nima degani?</p>",
        "choices": ["faqat", "ham", "-gacha", "bilan"],
        "correct": "faqat",
        "explanation": "<p><strong>만</strong> = “faqat”: 책만 있습니다 — “faqat kitob "
                       "bor”.</p>",
    },
    {
        "text": "<p><strong>부터</strong> va <strong>까지</strong> nima degani?</p>",
        "choices": ["-dan va -gacha", "-ga va -dan", "ham va faqat", "va va yoki"],
        "correct": "-dan va -gacha",
        "explanation": "<p><strong>부터</strong> = “-dan”, <strong>까지</strong> = "
                       "“-gacha”: 아침부터 저녁까지 — “ertalabdan kechgacha”.</p>",
    },
    {
        "text": "<p>받침 bor otga “va” qanday qoʻshiladi?</p>",
        "choices": ["과", "와", "하고만", "도"],
        "correct": "과",
        "explanation": "<p>받침 <strong>bor</strong> → <strong>과</strong> (책과), yoʻq → "
                       "<strong>와</strong> (친구와). <em>하고</em> esa hech qachon "
                       "oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Qaysi shakl hech qachon oʻzgarmaydi?</p>",
        "choices": ["하고", "와/과", "은/는", "이/가"],
        "correct": "하고",
        "explanation": "<p><strong>하고</strong> — 받침 ayrisi yoʻq, har doim bir xil: "
                       "책하고, 친구하고. Shuning uchun boshlangʻich darajada eng "
                       "qulay.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>“Men ham talabaman” ni koreyschaga oʻgiring.</p>",
        "choices": ["저도 학생입니다.", "저는도 학생입니다.",
                    "저도는 학생입니다.", "저만 학생입니다."],
        "correct": "저도 학생입니다.",
        "explanation": "<p><strong>도 은/는 ni almashtiradi</strong>, u bilan yonma-yon "
                       "kelmaydi. Oʻzbekchada ham “men ham” deymiz, “menniham” "
                       "emas.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>저는 책___ 있습니다.</strong> "
                "(“faqat kitob”)</p>",
        "choices": ["만", "이만", "만이", "도만"],
        "correct": "만",
        "explanation": "<p><strong>만</strong> ham 이/가 ni almashtiradi, shuning uchun "
                       "<s>책이만</s> notoʻgʻri.</p>",
    },
    {
        "text": "<p>“Ertalabdan kechgacha” ni koreyschaga oʻgiring.</p>",
        "choices": ["아침부터 저녁까지", "아침까지 저녁부터",
                    "아침에서 저녁까지", "아침도 저녁만"],
        "correct": "아침부터 저녁까지",
        "explanation": "<p>Tartib oʻzbekcha bilan bir xil: <em>ertalab<b>dan</b> "
                       "kech<b>gacha</b></em> → <strong>아침부터 저녁까지</strong>.</p>",
    },
    {
        "text": "<p>“Maktabdan uygacha” ni koreyschaga oʻgiring.</p>",
        "choices": ["학교에서 집까지", "학교부터 집까지",
                    "학교에 집까지", "학교까지 집에서"],
        "correct": "학교에서 집까지",
        "explanation": "<p>Bu <em>joy</em> oraligʻi, shuning uchun “…dan” uchun 부터 emas, "
                       "<strong>에서</strong>. “…gacha” esa ikkalasida ham 까지.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>가방 안에 책___ 돈이 "
                "있습니다.</strong></p>",
        "choices": ["과", "와", "도", "만"],
        "correct": "과",
        "explanation": "<p><strong>과</strong> — 책 받침 (ㄱ) bilan tugaydi. "
                       "책하고 돈 ham toʻgʻri boʻlardi.</p>",
    },
    {
        "text": "<p>“친구 va 저” ni toʻgʻri yozing.</p>",
        "choices": ["친구와 저", "친구과 저", "친구도 저", "친구만 저"],
        "correct": "친구와 저",
        "explanation": "<p><strong>친구와</strong> — 친구 unli (ㅜ) bilan tugaydi, 받침 "
                       "yoʻq → 와.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>자수르 씨___ 한국 "
                "사람입니다.</strong> (“faqat Jasur”)</p>",
        "choices": ["만", "도", "과", "부터"],
        "correct": "만",
        "explanation": "<p><strong>만</strong> = “faqat”: boshqalar koreys emas, faqat "
                       "Jasur.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>도</strong> va <strong>만</strong> farqi nima?</p>",
        "choices": ["도 qoʻshadi (“ham”), 만 cheklaydi (“faqat”)",
                    "도 cheklaydi, 만 qoʻshadi",
                    "Ikkalasi ham “ham” degani",
                    "도 vaqt, 만 joy uchun"],
        "correct": "도 qoʻshadi (“ham”), 만 cheklaydi (“faqat”)",
        "explanation": "<p><strong>저도</strong> = “men ham” (boshqalar qatoriga "
                       "qoʻshiladi), <strong>저만</strong> = “faqat men” (boshqalar "
                       "chiqarib tashlanadi). Lekin ikkalasi ham 은/는 va 이/가 ni "
                       "almashtiradi.</p>",
    },
    {
        "text": "<p>Vaqt va joy oraligʻida “…dan” qanday farq qiladi?</p>",
        "choices": ["Vaqt — 부터, joy — 에서", "Vaqt — 에서, joy — 부터",
                    "Ikkalasi ham 부터", "Ikkalasi ham 에"],
        "correct": "Vaqt — 부터, joy — 에서",
        "explanation": "<p><strong>아침부터</strong> (vaqt) va <strong>학교에서</strong> "
                       "(joy). “…gacha” esa ikkalasida ham <strong>까지</strong>.</p>",
    },
    {
        "text": "<p>Nega “저는도” notoʻgʻri?</p>",
        "choices": ["도 mavzu qoʻshimchasini almashtiradi, u bilan birga kelmaydi",
                    "Chunki 저 받침 bilan tugamaydi",
                    "Chunki 도 faqat feʼl bilan keladi",
                    "Chunki 도 gap oxirida turishi kerak"],
        "correct": "도 mavzu qoʻshimchasini almashtiradi, u bilan birga kelmaydi",
        "explanation": "<p>Toʻgʻrisi — <strong>저도</strong>. Xuddi shu qoida 만 ga ham "
                       "tegishli: <em>저만</em>, <s>저는만</s> emas.</p>",
    },
    {
        "text": "<p>“책만 있습니다. 돈은 없습니다.” — nega ikkinchi gapda 은 "
                "ishlatilgan?</p>",
        "choices": ["Chunki qiyoslanmoqda — “pul esa yoʻq”",
                    "Chunki 돈 받침 bilan tugaydi",
                    "Chunki 은 har doim inkor bilan keladi",
                    "Bu xato, 이 boʻlishi kerak"],
        "correct": "Chunki qiyoslanmoqda — “pul esa yoʻq”",
        "explanation": "<p>PK-12 dagi qoida: <strong>은/는</strong> qiyoslash soyasini "
                       "beradi — oʻzbekcha “<em>esa</em>”. Kitob bor, pul <em>esa</em> "
                       "yoʻq.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["저는도 학생입니다.", "저도 학생입니다.",
                    "저만 학생입니다.", "저는 학생입니다."],
        "correct": "저는도 학생입니다.",
        "explanation": "<p><strong>도</strong> 은/는 ni almashtiradi: toʻgʻrisi "
                       "<em>저도 학생입니다</em>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["책과 가방이 있습니다.", "책와 가방이 있습니다.",
                    "책과만 가방이 있습니다.", "책은과 가방이 있습니다."],
        "correct": "책과 가방이 있습니다.",
        "explanation": "<p>책 받침 (ㄱ) bilan tugaydi → <strong>과</strong>. "
                       "책하고 가방 ham toʻgʻri boʻlardi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
                "<p><strong>있습니다 / 학교에 / 저녁까지 / 아침부터</strong></p>",
        "choices": ["아침부터 저녁까지 학교에 있습니다.",
                    "학교에 아침부터 있습니다 저녁까지.",
                    "저녁까지 아침부터 학교에 있습니다.",
                    "아침부터 학교에 저녁까지 있습니다."],
        "correct": "아침부터 저녁까지 학교에 있습니다.",
        "explanation": "<p>Vaqt oraligʻi → joy → kesim. <strong>부터 avval, 까지 "
                       "keyin</strong> — xuddi oʻzbekchadagi “ertalabdan kechgacha” "
                       "kabi.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 저는 학생입니다.<br>나: ___ 학생입니다.</strong> "
                "(“Men ham”)</p>",
        "choices": ["저도", "저는도", "저만", "저는"],
        "correct": "저도",
        "explanation": "<p><strong>저도</strong> — “men ham”. 저만 “faqat men” degan "
                       "boshqa maʼno berardi, 저는 esa “ham” maʼnosini umuman "
                       "bermaydi.</p>",
    },
]


# =====================================================================
# PK-17 — 을/를 va 의
# =====================================================================

Q_PK17 = [
    # 1–5 tanish
    {
        "text": "<p><strong>을/를</strong> qaysi vazifani bajaradi?</p>",
        "choices": ["Toʻldiruvchini belgilaydi (-ni)", "Egani belgilaydi",
                    "Mavzuni belgilaydi", "Joyni belgilaydi"],
        "correct": "Toʻldiruvchini belgilaydi (-ni)",
        "explanation": "<p><strong>을/를</strong> — toʻldiruvchi (목적어) qoʻshimchasi, "
                       "oʻzbekcha <em>-ni</em> bilan aynan bir xil vazifada: "
                       "책<b>을</b> 읽습니다 = “kitob<b>ni</b> oʻqiyman”.</p>",
    },
    {
        "text": "<p>받침 bor otga qaysi shakl qoʻshiladi?</p>",
        "choices": ["을", "를", "의", "와"],
        "correct": "을",
        "explanation": "<p>받침 <strong>bor</strong> → <strong>을</strong> (책을, 밥을), "
                       "yoʻq → <strong>를</strong> (커피를, 친구를).</p>",
    },
    {
        "text": "<p><strong>의</strong> nima maʼnoni beradi?</p>",
        "choices": ["-ning (egalik)", "-ni (toʻldiruvchi)", "-da (joy)", "ham"],
        "correct": "-ning (egalik)",
        "explanation": "<p><strong>의</strong> = oʻzbekcha <em>-ning</em>: "
                       "친구의 가방 = “doʻstning sumkasi”.</p>",
    },
    {
        "text": "<p>Koreys gapida soʻz tartibi qanday?</p>",
        "choices": ["ega → toʻldiruvchi → kesim", "ega → kesim → toʻldiruvchi",
                    "kesim → ega → toʻldiruvchi", "toʻldiruvchi → kesim → ega"],
        "correct": "ega → toʻldiruvchi → kesim",
        "explanation": "<p><strong>SOV</strong> — xuddi oʻzbekchadagidek: “Men kitobni "
                       "oʻqiyman” → 저는 책을 읽습니다. Ingliz tilida esa toʻldiruvchi "
                       "feʼldan <em>keyin</em> keladi.</p>",
    },
    {
        "text": "<p><strong>저의</strong> ning amaldagi qisqargan shakli qaysi?</p>",
        "choices": ["제", "내", "네", "저"],
        "correct": "제",
        "explanation": "<p><strong>제</strong> (저의) — hurmatli “mening”. "
                       "<strong>내</strong> esa 나의 ning qisqargani, ya'ni 반말 "
                       "shakli.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>저는 밥___ 먹습니다.</strong></p>",
        "choices": ["을", "를", "이", "은"],
        "correct": "을",
        "explanation": "<p><strong>을</strong> — 밥 받침 (ㅂ) bilan tugaydi. “Men ovqatni "
                       "yeyman”.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>저는 커피___ 마십니다.</strong></p>",
        "choices": ["를", "을", "가", "는"],
        "correct": "를",
        "explanation": "<p><strong>를</strong> — 커피 unli (ㅣ) bilan tugaydi, 받침 "
                       "yoʻq.</p>",
    },
    {
        "text": "<p>“Men koreys tilini oʻrganaman” ni koreyschaga oʻgiring.</p>",
        "choices": ["저는 한국어를 공부합니다.", "저는 공부합니다 한국어를.",
                    "저는 한국어을 공부합니다.", "한국어를 저는 공부합니다만."],
        "correct": "저는 한국어를 공부합니다.",
        "explanation": "<p>한국어 unli bilan tugaydi → <strong>를</strong>, va kesim "
                       "<strong>gap oxirida</strong> — oʻzbekcha tartib bilan bir "
                       "xil.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>저는 집___ 우유를 "
                "마십니다.</strong></p>",
        "choices": ["에서", "에", "이", "은"],
        "correct": "에서",
        "explanation": "<p><strong>에서</strong> — 마시다 harakat feʼli. PK-14 qoidasi: "
                       "있다/없다 bilan 에, harakat feʼli bilan 에서.</p>",
    },
    {
        "text": "<p>“doʻstning sumkasi” ni koreyschaga oʻgiring.</p>",
        "choices": ["친구의 가방", "친구를 가방", "가방의 친구", "친구와 가방"],
        "correct": "친구의 가방",
        "explanation": "<p><strong>친구의 가방</strong> — egasi oldinda, egalik qilinuvchi "
                       "keyinda, xuddi oʻzbekchadagi “doʻst<b>ning</b> sumkasi” "
                       "kabi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ 이름은 "
                "벡조드입니다.</strong> (hurmatli)</p>",
        "choices": ["제", "내", "저를", "나의"],
        "correct": "제",
        "explanation": "<p><strong>제</strong> — 저의 ning qisqargan shakli, hurmatli "
                       "nutqda. 내 esa 반말 shakli va 입니다 bilan mos kelmaydi.</p>",
    },
    {
        "text": "<p>Qaysi birikmada <strong>의</strong> odatda tushib qoladi?</p>",
        "choices": ["한국 사람", "친구의 가방", "선생님의 책", "누구의 가방"],
        "correct": "한국 사람",
        "explanation": "<p>Ikki ot tabiiy bogʻlangan boʻlsa 의 <strong>tushadi</strong>: "
                       "한국 사람, 학교 친구. Egasi <em>aniq bir kishi</em> boʻlganda esa "
                       "의 kerak: 친구<b>의</b> 가방.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>을/를</strong> va <strong>이/가</strong> farqi nima?</p>",
        "choices": ["을/를 — toʻldiruvchi, 이/가 — ega",
                    "을/를 — ega, 이/가 — toʻldiruvchi",
                    "Ikkalasi ham ega",
                    "을/를 — egalik, 이/가 — joy"],
        "correct": "을/를 — toʻldiruvchi, 이/가 — ega",
        "explanation": "<p><strong>저는 책을 읽습니다</strong> — 책 harakatni qabul qiladi "
                       "(toʻldiruvchi). <strong>책이 있습니다</strong> — 책 gapning egasi. "
                       "Oʻzbekchada ham “kitob<em>ni</em>” va “kitob bor” "
                       "farqlanadi.</p>",
    },
    {
        "text": "<p>Nega “집에서 마십니다” toʻgʻri, “집에 마십니다” notoʻgʻri?</p>",
        "choices": ["마시다 harakat feʼli — harakat joyi 에서 oladi",
                    "Chunki 집 받침 bilan tugamaydi",
                    "Chunki 에 faqat vaqt uchun",
                    "Ikkalasi ham toʻgʻri"],
        "correct": "마시다 harakat feʼli — harakat joyi 에서 oladi",
        "explanation": "<p>Uyda <em>turibman</em> → 집<b>에</b> 있습니다. Uyda "
                       "<em>ichaman</em> → 집<b>에서</b> 마십니다. Oʻzbekchada ikkalasi ham "
                       "“uyda”, shuning uchun bu farqni alohida eslab qolish kerak.</p>",
    },
    {
        "text": "<p>Egalik maʼnosidagi <strong>의</strong> qanday oʻqiladi?</p>",
        "choices": ["[에]", "[의]", "[이]", "[으]"],
        "correct": "[에]",
        "explanation": "<p>Egalik qoʻshimchasi boʻlganda <strong>의 → [에]</strong>: "
                       "친구의 → [친구에]. Bu PK-3 da oʻrganilgan uch xil oʻqilishning "
                       "biri.</p>",
    },
    {
        "text": "<p>Nega oʻzbek oʻquvchi uchun 을/를 oson?</p>",
        "choices": ["Oʻzbekcha “-ni” bilan bir xil vazifada va soʻz tartibi ham bir xil",
                    "Chunki u hech qachon oʻzgarmaydi",
                    "Chunki u faqat savolda ishlatiladi",
                    "Chunki oʻzbekchada toʻldiruvchi yoʻq"],
        "correct": "Oʻzbekcha “-ni” bilan bir xil vazifada va soʻz tartibi ham bir xil",
        "explanation": "<p><em>Men · kitob<b>ni</b> · oʻqiyman</em> → "
                       "<em>저는 · 책<b>을</b> · 읽습니다</em>. Uchala boʻlak bir xil "
                       "tartibda. Ingliz tilida esa toʻldiruvchi feʼldan keyin keladi va "
                       "qoʻshimcha olmaydi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["저는 커피을 마십니다.", "저는 커피를 마십니다.",
                    "저는 책을 읽습니다.", "저는 밥을 먹습니다."],
        "correct": "저는 커피을 마십니다.",
        "explanation": "<p>커피 unli bilan tugaydi, 받침 yoʻq → <strong>를</strong>. "
                       "Toʻgʻrisi: <em>저는 커피를 마십니다.</em></p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["저는 학교에서 한국어를 공부합니다.",
                    "저는 학교에 한국어를 공부합니다.",
                    "저는 학교에서 한국어가 공부합니다.",
                    "저는 공부합니다 학교에서 한국어를."],
        "correct": "저는 학교에서 한국어를 공부합니다.",
        "explanation": "<p>Uchtasi toʻgʻri boʻlishi kerak: <strong>에서</strong> (harakat "
                       "feʼli), <strong>를</strong> (toʻldiruvchi), va kesim "
                       "<strong>oxirida</strong>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
                "<p><strong>읽습니다 / 저는 / 책을 / 집에서</strong></p>",
        "choices": ["저는 집에서 책을 읽습니다.", "저는 책을 집에서 읽습니다만.",
                    "집에서 읽습니다 저는 책을.", "책을 저는 집에서 읽습니다만."],
        "correct": "저는 집에서 책을 읽습니다.",
        "explanation": "<p>Ega → joy → toʻldiruvchi → kesim. Joy toʻldiruvchidan oldin "
                       "turadi, kesim esa har doim <strong>oxirida</strong>.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 그 책은 누구의 책입니까?<br>나: ___</strong></p>",
        "choices": ["이 책은 친구의 책입니다.", "이 책은 친구를 책입니다.",
                    "이 책은 친구에서 책입니다.", "이 책은 친구도 책입니다."],
        "correct": "이 책은 친구의 책입니다.",
        "explanation": "<p>Savol egalik haqida (누구<b>의</b>), shuning uchun javobda ham "
                       "<strong>의</strong> ishlatiladi. Diqqat: savol beruvchi 그 책 dedi, "
                       "javob beruvchi esa <strong>이 책</strong> — kitob unda "
                       "(PK-15).</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-15 Mashq: 이거/그거/저거 va 여기/거기/저기",
        "description": "20 savol — uch pogʻonali koʻrsatish, 것 tushishi va joy shakllari.",
        "tutorial":    "PK-15:",
        "level":       "easy",
        "questions":   Q_PK15,
    },
    {
        "title":       "PK-16 Mashq: 도, 만, 부터, 까지, 하고/와/과",
        "description": "20 savol — “ham”, “faqat”, oraliq va “va” qoʻshimchalari.",
        "tutorial":    "PK-16:",
        "level":       "easy",
        "questions":   Q_PK16,
    },
    {
        "title":       "PK-17 Mashq: 을/를 va 의",
        "description": "20 savol — toʻldiruvchi, egalik, soʻz tartibi va 에/에서 farqi.",
        "tutorial":    "PK-17:",
        "level":       "easy",
        "questions":   Q_PK17,
    },
]
