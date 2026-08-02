# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-18 … PK-20 (feʼl tizimi).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_18_20.py --master=prime \\
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
# PK-18 — 아/어요
# =====================================================================

Q_PK18 = [
    # 1–5 tanish
    {
        "text": "<p>Lugʻat shaklidan oʻzakni qanday olasiz?</p>",
        "choices": ["다 ni olib tashlaysiz", "요 ni olib tashlaysiz",
                    "Birinchi boʻgʻinni olasiz", "이 ni qoʻshasiz"],
        "correct": "다 ni olib tashlaysiz",
        "explanation": "<p>Lugʻatda har bir feʼl va sifat <strong>다</strong> bilan "
                       "tugaydi. Undan oldingi qism — oʻzak (어간): 먹다 → 먹, "
                       "가다 → 가.</p>",
    },
    {
        "text": "<p>Oʻzakning oxirgi unlisi <strong>ㅏ</strong> yoki <strong>ㅗ</strong> "
                "boʻlsa, qaysi qoʻshimcha keladi?</p>",
        "choices": ["아요", "어요", "해요", "이에요"],
        "correct": "아요",
        "explanation": "<p>Unli uygʻunligi: oxirgi unli <strong>ㅏ yoki ㅗ → 아요</strong> "
                       "(앉아요, 좋아요). Boshqa har qanday holatda <strong>어요</strong>.</p>",
    },
    {
        "text": "<p><strong>하다</strong> bilan tugagan soʻzlar qanday tuslanadi?</p>",
        "choices": ["해요", "하아요", "하어요", "합요"],
        "correct": "해요",
        "explanation": "<p><strong>하다 → 해요</strong> — istisno, lekin eng foydali "
                       "istisno: koreys tilidagi minglab soʻz 하다 bilan yasaladi "
                       "(공부해요, 좋아해요, 말해요).</p>",
    },
    {
        "text": "<p>Koreys sifatlari qanday ishlaydi?</p>",
        "choices": ["Feʼl kabi tuslanadi — bogʻlama kerak emas",
                    "Har doim 이에요 oladi",
                    "Umuman tuslanmaydi",
                    "Faqat 입니다 bilan keladi"],
        "correct": "Feʼl kabi tuslanadi — bogʻlama kerak emas",
        "explanation": "<p>Koreys tilida <strong>sifat feʼlning oʻzi</strong>: 좋아요, "
                       "맛있어요 — bir soʻz butun gap boʻla oladi. Ingliz tilidagi "
                       "<em>is</em> kabi bogʻlama kerak emas.</p>",
    },
    {
        "text": "<p>Otga 해요체 da nima qoʻshiladi?</p>",
        "choices": ["이에요 / 예요", "아요 / 어요", "습니다", "이/가"],
        "correct": "이에요 / 예요",
        "explanation": "<p>받침 <strong>bor → 이에요</strong> (학생이에요), yoʻq → "
                       "<strong>예요</strong> (의사예요). Bu 입니다 ning kundalik "
                       "shakli.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p><strong>먹다</strong> ni 해요체 ga oʻgiring.</p>",
        "choices": ["먹어요", "먹아요", "먹해요", "먹이에요"],
        "correct": "먹어요",
        "explanation": "<p>Oʻzak <strong>먹</strong>, oxirgi unli <strong>ㅓ</strong> — "
                       "ㅏ ham, ㅗ ham emas, demak <strong>어요</strong>.</p>",
    },
    {
        "text": "<p><strong>좋다</strong> ni 해요체 ga oʻgiring.</p>",
        "choices": ["좋아요", "좋어요", "좋해요", "좋이에요"],
        "correct": "좋아요",
        "explanation": "<p>Oʻzak <strong>좋</strong>, oxirgi unli <strong>ㅗ</strong> → "
                       "<strong>아요</strong>. 좋다 sifat, lekin qoida bir xil.</p>",
    },
    {
        "text": "<p><strong>보다</strong> ni 해요체 ga oʻgiring.</p>",
        "choices": ["봐요", "보아요", "보어요", "봅요"],
        "correct": "봐요",
        "explanation": "<p>Oʻzak <strong>보</strong> (ㅗ) → 아요, lekin oʻzak unli bilan "
                       "tugagani uchun qisqaradi: <strong>ㅗ + ㅏ = ㅘ</strong> → "
                       "봐요.</p>",
    },
    {
        "text": "<p><strong>마시다</strong> ni 해요체 ga oʻgiring.</p>",
        "choices": ["마셔요", "마시어요", "마시아요", "마셔에요"],
        "correct": "마셔요",
        "explanation": "<p>Oʻzak <strong>마시</strong> (ㅣ) → 어요, qisqaradi: "
                       "<strong>ㅣ + ㅓ = ㅕ</strong> → 마셔요.</p>",
    },
    {
        "text": "<p><strong>배우다</strong> ni 해요체 ga oʻgiring.</p>",
        "choices": ["배워요", "배우어요", "배우아요", "배웨요"],
        "correct": "배워요",
        "explanation": "<p>Oʻzak <strong>배우</strong> (ㅜ) → 어요, qisqaradi: "
                       "<strong>ㅜ + ㅓ = ㅝ</strong> → 배워요.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>저는 학생___.</strong> "
                "(해요체)</p>",
        "choices": ["이에요", "예요", "어요", "습니다"],
        "correct": "이에요",
        "explanation": "<p><strong>이에요</strong> — 학생 받침 (ㅇ) bilan tugaydi. "
                       "의사 boʻlganida <em>예요</em> boʻlardi.</p>",
    },
    {
        "text": "<p>“Men har kuni koreys tilini oʻrganaman” ni koreyschaga oʻgiring.</p>",
        "choices": ["저는 매일 한국어를 공부해요.", "저는 매일 한국어를 공부하어요.",
                    "저는 매일 한국어가 공부해요.", "저는 매일 한국어를 공부이에요."],
        "correct": "저는 매일 한국어를 공부해요.",
        "explanation": "<p><strong>공부하다 → 공부해요</strong>, va 한국어 toʻldiruvchi "
                       "boʻlgani uchun <strong>를</strong> oladi (PK-17).</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Nega <strong>먹어요</strong>, <strong>먹아요</strong> emas?</p>",
        "choices": ["Oʻzakning oxirgi unlisi ㅓ — ㅏ ham, ㅗ ham emas",
                    "Chunki 먹 받침li",
                    "Chunki 먹다 feʼl, sifat emas",
                    "Chunki 아요 faqat 하다 uchun"],
        "correct": "Oʻzakning oxirgi unlisi ㅓ — ㅏ ham, ㅗ ham emas",
        "explanation": "<p>Unli uygʻunligi <strong>faqat oxirgi unliga</strong> qaraydi, "
                       "받침ga emas. ㅏ/ㅗ → 아요; boshqa hamma narsa → 어요.</p>",
    },
    {
        "text": "<p>Qaysi gap <em>notoʻgʻri</em>?</p>",
        "choices": ["맛있이에요", "맛있어요", "학생이에요", "의사예요"],
        "correct": "맛있이에요",
        "explanation": "<p><strong>맛있다 — sifat</strong>, ya'ni feʼlning oʻzi. Unga "
                       "bogʻlama qoʻshilmaydi: <strong>맛있어요</strong>. 이에요/예요 esa "
                       "faqat <em>otga</em> qoʻshiladi.</p>",
    },
    {
        "text": "<p>해요체 da darak, savol va iltimosni nima ajratadi?</p>",
        "choices": ["Ohang — shakl bir xil", "Qoʻshimcha oʻzgaradi",
                    "Soʻz tartibi oʻzgaradi", "Ular umuman farqlanmaydi"],
        "correct": "Ohang — shakl bir xil",
        "explanation": "<p><strong>가요.</strong> (boraman) · <strong>가요?</strong> "
                       "(borasizmi?) · <strong>가요.</strong> (boring) — bitta shakl toʻrt "
                       "vazifada. Bu 해요체 ning eng qulay tomoni.</p>",
    },
    {
        "text": "<p>Qisqarish qoidalari qayerdan kelib chiqqan?</p>",
        "choices": ["PK-3 dagi qoʻshma unlilardan (ㅗ+ㅏ=ㅘ, ㅜ+ㅓ=ㅝ, ㅣ+ㅓ=ㅕ)",
                    "받침 qoidasidan",
                    "비음화 dan",
                    "Bular yodlanadi, qoidasi yoʻq"],
        "correct": "PK-3 dagi qoʻshma unlilardan (ㅗ+ㅏ=ㅘ, ㅜ+ㅓ=ㅝ, ㅣ+ㅓ=ㅕ)",
        "explanation": "<p>Yangi qoida yoʻq — oʻsha qoʻshma unlilar feʼl ichida "
                       "uchrashmoqda. 보+아요 = <strong>봐요</strong>, 마시+어요 = "
                       "<strong>마셔요</strong>.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["저는 공부하어요.", "저는 공부해요.",
                    "저는 책을 읽어요.", "저는 커피를 마셔요."],
        "correct": "저는 공부하어요.",
        "explanation": "<p><strong>하다 har doim 해요</strong>: toʻgʻrisi "
                       "<em>공부해요</em>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["한국어가 재미있어요.", "한국어가 재미있이에요.",
                    "한국어를 재미있어요.", "한국어가 재미있아요."],
        "correct": "한국어가 재미있어요.",
        "explanation": "<p>Uchtasi toʻgʻri boʻlishi kerak: ega <strong>가</strong>, sifat "
                       "bogʻlamasiz, va oxirgi unli ㅣ boʻlgani uchun "
                       "<strong>어요</strong>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
                "<p><strong>마셔요 / 저는 / 집에서 / 우유를</strong></p>",
        "choices": ["저는 집에서 우유를 마셔요.", "저는 우유를 집에서 마셔요만.",
                    "집에서 저는 마셔요 우유를.", "우유를 저는 집에서 마셔요만."],
        "correct": "저는 집에서 우유를 마셔요.",
        "explanation": "<p>Ega → joy → toʻldiruvchi → kesim. <strong>에서</strong> "
                       "ishlatilgan, chunki 마시다 harakat feʼli (PK-14).</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 커피 마셔요?<br>나: 네, ___</strong></p>",
        "choices": ["마셔요.", "마시어요.", "마십니다만.", "마셔이에요."],
        "correct": "마셔요.",
        "explanation": "<p>해요체 da savol va javob <strong>bir xil shaklda</strong> — "
                       "faqat ohang farq qiladi. Shuning uchun javob ham "
                       "<em>마셔요</em>.</p>",
    },
]


# =====================================================================
# PK-19 — ㅂ니다 / 습니다
# =====================================================================

Q_PK19 = [
    # 1–5 tanish
    {
        "text": "<p>합니다체 da qoʻshimcha nimaga qarab tanlanadi?</p>",
        "choices": ["Oʻzakda 받침 bor-yoʻqligiga", "Oxirgi unliga",
                    "Feʼl yoki sifat ekaniga", "Gapning uzunligiga"],
        "correct": "Oʻzakda 받침 bor-yoʻqligiga",
        "explanation": "<p>받침 <strong>yoʻq → ㅂ니다</strong> (갑니다), <strong>bor → "
                       "습니다</strong> (먹습니다). Unli uygʻunligi bu yerda umuman "
                       "ishlamaydi — shuning uchun 합니다체 해요체 dan oson.</p>",
    },
    {
        "text": "<p>Oʻzak <strong>unli</strong> bilan tugasa qaysi shakl keladi?</p>",
        "choices": ["ㅂ니다", "습니다", "아요", "이에요"],
        "correct": "ㅂ니다",
        "explanation": "<p><strong>ㅂ니다</strong>, va ㅂ oʻzakning oxirgi bloki "
                       "<em>tagiga</em> 받침 boʻlib tushadi: 가 + ㅂ니다 = "
                       "<strong>갑니다</strong>.</p>",
    },
    {
        "text": "<p><strong>갑니다</strong> qanday oʻqiladi?</p>",
        "choices": ["[감니다]", "[갑니다]", "[가니다]", "[갑미다]"],
        "correct": "[감니다]",
        "explanation": "<p>비음화 (PK-8): ㅂ dan keyin ㄴ kelgani uchun ㅂ → ㅁ. "
                       "<strong>-ㅂ니다</strong> hech qachon “p-ni-da” deb "
                       "aytilmaydi.</p>",
    },
    {
        "text": "<p>Rasmiy savol qanday yasaladi?</p>",
        "choices": ["다 → 까", "요 qoʻshiladi", "이 qoʻshiladi", "Soʻzlar oʻrni almashadi"],
        "correct": "다 → 까",
        "explanation": "<p><strong>갑니다 → 갑니까?</strong> — xuddi 입니다 → 입니까 kabi "
                       "(PK-10). Soʻz tartibi oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>합니다체 va 해요체 haqida qaysi javob toʻgʻri?</p>",
        "choices": ["Ikkalasi ham 존댓말", "합니다체 존댓말, 해요체 반말",
                    "해요체 존댓말, 합니다체 반말", "Ikkalasi ham 반말"],
        "correct": "Ikkalasi ham 존댓말",
        "explanation": "<p>Ikkalasi ham <strong>hurmat nutqi</strong> (PK-11). Farqi "
                       "faqat uslubda: 합니다체 rasmiy va masofali, 해요체 kundalik va "
                       "iliq.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p><strong>먹다</strong> ni 합니다체 ga oʻgiring.</p>",
        "choices": ["먹습니다", "먹ㅂ니다", "먹읍니다", "멉니다"],
        "correct": "먹습니다",
        "explanation": "<p>Oʻzak <strong>먹</strong> 받침li (ㄱ) → <strong>습니다</strong>. "
                       "Oʻqilishi [먹씀니다].</p>",
    },
    {
        "text": "<p><strong>마시다</strong> ni 합니다체 ga oʻgiring.</p>",
        "choices": ["마십니다", "마시습니다", "마셔습니다", "마시ㅂ니다"],
        "correct": "마십니다",
        "explanation": "<p>Oʻzak <strong>마시</strong> unli bilan tugaydi → ㅂ니다, va ㅂ "
                       "oxirgi blok tagiga tushadi: 시 + ㅂ = <strong>십</strong>.</p>",
    },
    {
        "text": "<p><strong>살다</strong> ni 합니다체 ga oʻgiring.</p>",
        "choices": ["삽니다", "살습니다", "살읍니다", "사습니다"],
        "correct": "삽니다",
        "explanation": "<p><strong>ㄹ tushadi</strong>: 살 → 사 + ㅂ니다 = 삽니다. "
                       "해요체 da esa ㄹ qoladi — <em>살아요</em>.</p>",
    },
    {
        "text": "<p><strong>좋다</strong> ni 합니다체 ga oʻgiring.</p>",
        "choices": ["좋습니다", "좋ㅂ니다", "좋아습니다", "좁니다"],
        "correct": "좋습니다",
        "explanation": "<p>Oʻzak <strong>좋</strong> 받침li (ㅎ) → <strong>습니다</strong>. "
                       "Sifat ham feʼl kabi tuslanadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>한국어를 ___?</strong> "
                "(“oʻrganasizmi?”, rasmiy)</p>",
        "choices": ["공부합니까", "공부합니다", "공부해요", "공부습니까"],
        "correct": "공부합니까",
        "explanation": "<p>Rasmiy savol: <strong>다 → 까</strong>. 공부합니다 → "
                       "공부합니까?</p>",
    },
    {
        "text": "<p>Doʻkonda xizmatchi mijozga qaysi darajada gapiradi?</p>",
        "choices": ["합니다체", "해요체", "반말", "Farqi yoʻq"],
        "correct": "합니다체",
        "explanation": "<p>Xizmat sohasida <strong>합니다체</strong> — professional "
                       "masofa. Shuning uchun doʻkonda <em>어서 오세요, 감사합니다</em> "
                       "eshitasiz.</p>",
    },
    {
        "text": "<p>“Men Seulda yashayman” ni rasmiy shaklda yozing.</p>",
        "choices": ["저는 서울에 삽니다.", "저는 서울에서 삽니다.",
                    "저는 서울에 살습니다.", "저는 서울에 살아습니다."],
        "correct": "저는 서울에 삽니다.",
        "explanation": "<p>Ikki narsa: <strong>ㄹ tushadi</strong> (삽니다), va 살다 holat "
                       "bildirgani uchun joy <strong>에</strong> oladi, 에서 emas "
                       "(PK-14).</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Nega 합니다체 해요체 dan oson?</p>",
        "choices": ["Unli uygʻunligi ham, qisqarish ham yoʻq — faqat 받침",
                    "Chunki qoʻshimchasi qisqaroq",
                    "Chunki u faqat feʼllarga qoʻshiladi",
                    "Chunki u kam ishlatiladi"],
        "correct": "Unli uygʻunligi ham, qisqarish ham yoʻq — faqat 받침",
        "explanation": "<p>해요체 da oxirgi unliga qarash va qisqarishni hisoblash kerak. "
                       "합니다체 da esa faqat bitta savol: <strong>받침 bormi?</strong></p>",
    },
    {
        "text": "<p>살다 ning ikki shakli qaysi?</p>",
        "choices": ["삽니다 (합니다체) va 살아요 (해요체)",
                    "살습니다 va 살어요",
                    "삽니다 va 사요",
                    "살습니다 va 살아요"],
        "correct": "삽니다 (합니다체) va 살아요 (해요체)",
        "explanation": "<p>ㄹ <strong>faqat ㅂ니다 oldidan</strong> tushadi. 해요체 da u "
                       "joyida qoladi: 살 + 아요 = <strong>살아요</strong> (oxirgi unli "
                       "ㅏ).</p>",
    },
    {
        "text": "<p>Qaysi juftlik toʻgʻri?</p>",
        "choices": ["가요 / 갑니다", "가요 / 가습니다", "가어요 / 갑니다", "가아요 / 갑니다"],
        "correct": "가요 / 갑니다",
        "explanation": "<p>해요체: 가 + 아요 → qisqaradi → <strong>가요</strong>. "
                       "합니다체: 가 받침siz → <strong>갑니다</strong>.</p>",
    },
    {
        "text": "<p>Yangiliklar diktori qaysi darajada gapiradi?</p>",
        "choices": ["합니다체", "해요체", "반말", "Aralash"],
        "correct": "합니다체",
        "explanation": "<p><strong>합니다체</strong> — rasmiy, masofali va professional. "
                       "Yangiliklar, taqdimot, rasmiy xat — hammasi shu darajada.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["저는 한국에 살습니다.", "저는 한국에 삽니다.",
                    "저는 밥을 먹습니다.", "저는 커피를 마십니다."],
        "correct": "저는 한국에 살습니다.",
        "explanation": "<p><strong>ㄹ tushadi</strong>: toʻgʻrisi <em>삽니다</em>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["날씨가 좋습니다.", "날씨가 좋ㅂ니다.",
                    "날씨가 좋아습니다.", "날씨가 좋습니다이에요."],
        "correct": "날씨가 좋습니다.",
        "explanation": "<p>좋 받침li → <strong>습니다</strong>. Sifat boʻlgani uchun "
                       "bogʻlama ham kerak emas.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Bu gapni rasmiy shaklga oʻgiring: <strong>저는 한국어를 "
                "공부해요.</strong></p>",
        "choices": ["저는 한국어를 공부합니다.", "저는 한국어를 공부습니다.",
                    "저는 한국어를 공부해습니다.", "저는 한국어를 공부이에요."],
        "correct": "저는 한국어를 공부합니다.",
        "explanation": "<p>공부하 oʻzagi unli bilan tugaydi → <strong>ㅂ니다</strong>: "
                       "하 + ㅂ = <strong>합</strong> → 공부합니다.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 한국어를 공부합니까?<br>나: 네, ___</strong></p>",
        "choices": ["공부합니다.", "공부합니까.", "공부해요만.", "공부습니다."],
        "correct": "공부합니다.",
        "explanation": "<p>Savol 까 bilan, javob esa <strong>다</strong> bilan: "
                       "공부합니다. Rasmiy suhbatda javob ham 합니다체 da boʻladi.</p>",
    },
]


# =====================================================================
# PK-20 — 았/었어요
# =====================================================================

Q_PK20 = [
    # 1–5 tanish
    {
        "text": "<p>Oʻtgan zamonni yasashning eng ishonchli yoʻli qaysi?</p>",
        "choices": ["Avval 아/어요 shaklini yasab, 요 ni olib ㅆ어요 qoʻshish",
                    "Oʻzakka darhol 았습니다 qoʻshish",
                    "Lugʻat shakliga 었 qoʻshish",
                    "Har bir feʼlni alohida yodlash"],
        "correct": "Avval 아/어요 shaklini yasab, 요 ni olib ㅆ어요 qoʻshish",
        "explanation": "<p>Uch qadam: 먹다 → <strong>먹어요</strong> → 먹어 → "
                       "<strong>먹었어요</strong>. Shu usul qisqargan shakllarda ham "
                       "ishlaydi.</p>",
    },
    {
        "text": "<p><strong>하다</strong> ning oʻtgan shakli qaysi?</p>",
        "choices": ["했어요", "하었어요", "하았어요", "핬어요"],
        "correct": "했어요",
        "explanation": "<p>해요 dan boshlang: 해 + ㅆ어요 = <strong>했어요</strong>. "
                       "공부하다 → 공부했어요.</p>",
    },
    {
        "text": "<p>Oʻtgan zamonda rasmiy shakl qanday?</p>",
        "choices": ["았/었습니다", "았/었ㅂ니다", "았/었이에요", "았/었습니까만"],
        "correct": "았/었습니다",
        "explanation": "<p><strong>갔습니다, 먹었습니다, 했습니다</strong> — oʻtgan oʻzak "
                       "ㅆ 받침i bilan tugagani uchun har doim 습니다.</p>",
    },
    {
        "text": "<p><strong>있다</strong> ning oʻtgan shakli qaysi?</p>",
        "choices": ["있었어요", "있았어요", "이었어요", "있이에요"],
        "correct": "있었어요",
        "explanation": "<p>있어요 → 있어 + ㅆ어요 = <strong>있었어요</strong> (“bor edi”). "
                       "없다 esa <em>없었어요</em>.</p>",
    },
    {
        "text": "<p>Qaysi soʻz <strong>에</strong> olmaydi?</p>",
        "choices": ["어제", "아침", "저녁", "주말"],
        "correct": "어제",
        "explanation": "<p><strong>오늘, 어제, 내일</strong> hech qachon 에 olmaydi "
                       "(PK-14). Boshqa vaqt soʻzlari esa oladi: 아침<em>에</em>, "
                       "주말<em>에</em>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p><strong>읽다</strong> ni oʻtgan zamonga oʻgiring.</p>",
        "choices": ["읽었어요", "읽았어요", "읽였어요", "읽어었어요"],
        "correct": "읽었어요",
        "explanation": "<p>읽어요 → 읽어 + ㅆ어요 = <strong>읽었어요</strong>. Oxirgi unli "
                       "ㅣ boʻlgani uchun 어 tarafi.</p>",
    },
    {
        "text": "<p><strong>가다</strong> ni oʻtgan zamonga oʻgiring.</p>",
        "choices": ["갔어요", "가았어요", "가었어요", "갔았어요"],
        "correct": "갔어요",
        "explanation": "<p>가요 → 가 + ㅆ어요 = <strong>갔어요</strong>. ㅆ mavjud blok "
                       "tagiga 받침 boʻlib tushadi.</p>",
    },
    {
        "text": "<p><strong>보다</strong> ni oʻtgan zamonga oʻgiring.</p>",
        "choices": ["봤어요", "보았어요", "봐았어요", "보었어요"],
        "correct": "봤어요",
        "explanation": "<p>보다 → <strong>봐요</strong> (ㅗ+ㅏ=ㅘ) → 봐 + ㅆ어요 = "
                       "<strong>봤어요</strong>.</p>",
    },
    {
        "text": "<p><strong>마시다</strong> ni oʻtgan zamonga oʻgiring.</p>",
        "choices": ["마셨어요", "마시었어요", "마샸어요", "마셔었어요"],
        "correct": "마셨어요",
        "explanation": "<p>마셔요 → 마셔 + ㅆ어요 = <strong>마셨어요</strong>. Qisqargan "
                       "shaklga alohida qoida kerak emas.</p>",
    },
    {
        "text": "<p>“Kecha nima qildingiz?” ni koreyschaga oʻgiring.</p>",
        "choices": ["어제 무엇을 했어요?", "어제에 무엇을 했어요?",
                    "어제 무엇이 했어요?", "어제 무엇을 하었어요?"],
        "correct": "어제 무엇을 했어요?",
        "explanation": "<p>Uchta narsa: <strong>어제</strong> (에 olmaydi), "
                       "<strong>무엇을</strong> (toʻldiruvchi), <strong>했어요</strong> "
                       "(하다 → 해요 → 했어요).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>저는 어제 학생___.</strong> "
                "(“talaba edim”)</p>",
        "choices": ["이었어요", "였어요", "이에요", "있었어요"],
        "correct": "이었어요",
        "explanation": "<p><strong>이었어요</strong> — 학생 받침li. 의사 boʻlganida "
                       "<em>였어요</em> boʻlardi.</p>",
    },
    {
        "text": "<p><strong>갔다</strong> ni rasmiy oʻtgan shaklga oʻgiring.</p>",
        "choices": ["갔습니다", "갔ㅂ니다", "갑니다", "갔어습니다"],
        "correct": "갔습니다",
        "explanation": "<p>Oʻtgan oʻzak <strong>갔</strong> ㅆ 받침i bilan tugaydi → "
                       "<strong>습니다</strong>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Nega oʻtgan zamonda hech qachon ㅂ니다 boʻlmaydi?</p>",
        "choices": ["Oʻtgan oʻzak har doim ㅆ 받침i bilan tugaydi",
                    "Chunki ㅂ니다 faqat sifatlar uchun",
                    "Chunki oʻtgan zamon rasmiy emas",
                    "Chunki ㅆ unli hisoblanadi"],
        "correct": "Oʻtgan oʻzak har doim ㅆ 받침i bilan tugaydi",
        "explanation": "<p>갔, 먹었, 했 — hammasi 받침li. PK-19 qoidasi boʻyicha 받침li oʻzak "
                       "<strong>습니다</strong> oladi.</p>",
    },
    {
        "text": "<p>Koreys va ingliz oʻtgan zamoni orasidagi asosiy farq nima?</p>",
        "choices": ["Koreysda notoʻgʻri feʼllar roʻyxati yoʻq — qoida hammaga bir xil",
                    "Koreysda oʻtgan zamon umuman yoʻq",
                    "Koreysda oʻzak butunlay oʻzgaradi",
                    "Koreysda oʻtgan zamon faqat rasmiy nutqda"],
        "correct": "Koreysda notoʻgʻri feʼllar roʻyxati yoʻq — qoida hammaga bir xil",
        "explanation": "<p>Ingliz tilida <em>go → went</em>, <em>eat → ate</em> yodlanadi. "
                       "Koreysda esa oʻzbekchadagi kabi <strong>qoʻshimcha</strong> "
                       "qoʻshiladi va qoida oʻzgarmaydi.</p>",
    },
    {
        "text": "<p><strong>먹었어요</strong> va <strong>먹었습니다</strong> farqi nima?</p>",
        "choices": ["Faqat daraja — maʼnosi bir xil", "Birinchisi hozirgi zamon",
                    "Ikkinchisi savol", "Birinchisi 반말"],
        "correct": "Faqat daraja — maʼnosi bir xil",
        "explanation": "<p>Ikkalasi ham “yedim”. 먹었어요 — 해요체 (kundalik), "
                       "먹었습니다 — 합니다체 (rasmiy). Ikkalasi ham 존댓말.</p>",
    },
    {
        "text": "<p>Nega PK-18 “kursning kaliti” deb ataladi?</p>",
        "choices": ["Oʻtgan zamon va boshqa koʻp shakl 아/어요 asosiga quriladi",
                    "Chunki u eng qisqa dars",
                    "Chunki unda 받침 yoʻq",
                    "Chunki u faqat sifatlar haqida"],
        "correct": "Oʻtgan zamon va boshqa koʻp shakl 아/어요 asosiga quriladi",
        "explanation": "<p>Oʻtgan zamon uchun yangi qoida yoʻq — 아/어요 ni yasab, ㅆ어요 "
                       "qoʻshasiz. Keyingi darslardagi koʻp shakl ham shu asosdan "
                       "chiqadi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["저는 어제에 학교에 갔어요.", "저는 어제 학교에 갔어요.",
                    "저는 아침에 밥을 먹었어요.", "저는 주말에 책을 읽었어요."],
        "correct": "저는 어제에 학교에 갔어요.",
        "explanation": "<p><strong>어제 에 olmaydi</strong> (PK-14). Toʻgʻrisi: "
                       "<em>어제 학교에 갔어요.</em> Diqqat: 학교<b>에</b> toʻgʻri, chunki "
                       "가다 yoʻnalish bildiradi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["어제 한국어를 공부했어요.", "어제 한국어를 공부하었어요.",
                    "어제 한국어가 공부했어요.", "어제 한국어를 공부했습니다요."],
        "correct": "어제 한국어를 공부했어요.",
        "explanation": "<p><strong>공부하다 → 공부해요 → 공부했어요</strong>, va 한국어 "
                       "toʻldiruvchi boʻlgani uchun <strong>를</strong>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Bu gapni oʻtgan zamonga oʻgiring: <strong>저는 집에서 책을 "
                "읽어요.</strong></p>",
        "choices": ["저는 집에서 책을 읽었어요.", "저는 집에서 책을 읽았어요.",
                    "저는 집에 책을 읽었어요.", "저는 집에서 책이 읽었어요."],
        "correct": "저는 집에서 책을 읽었어요.",
        "explanation": "<p>Faqat kesim oʻzgaradi: 읽어요 → <strong>읽었어요</strong>. "
                       "Qolgan boʻlaklar — 에서 (harakat feʼli) va 을 (toʻldiruvchi) — "
                       "oʻz joyida qoladi.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 어제 시간이 있었어요?<br>나: 아니요, ___</strong></p>",
        "choices": ["시간이 없었어요.", "시간이 없어요.",
                    "시간이 아니었어요.", "시간을 없었어요."],
        "correct": "시간이 없었어요.",
        "explanation": "<p>Savol oʻtgan zamonda — javob ham oʻtgan zamonda: "
                       "<strong>없었어요</strong>. 있다/없다 dan oldingi ot esa "
                       "<strong>이/가</strong> oladi (PK-13).</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-18 Mashq: Feʼl va sifat + 아/어요",
        "description": "20 savol — oʻzak, unli uygʻunligi, qisqarish va sifat-feʼllar.",
        "tutorial":    "PK-18:",
        "level":       "easy",
        "questions":   Q_PK18,
    },
    {
        "title":       "PK-19 Mashq: Feʼl va sifat + ㅂ니다/습니다",
        "description": "20 savol — 받침 ayrisi, ㄹ tushishi va ikki darajaning farqi.",
        "tutorial":    "PK-19:",
        "level":       "easy",
        "questions":   Q_PK19,
    },
    {
        "title":       "PK-20 Mashq: Oʻtgan zamon 았/었어요",
        "description": "20 savol — uch qadamli yasash, rasmiy shakl va 이었어요/였어요.",
        "tutorial":    "PK-20:",
        "level":       "easy",
        "questions":   Q_PK20,
    },
]
