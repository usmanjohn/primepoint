# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-21 … PK-22 (inkor, Block B yakuni).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_21_22.py --master=prime \\
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
# PK-21 — 안 / 지 않다
# =====================================================================

Q_PK21 = [
    # 1–5 tanish
    {
        "text": "<p><strong>안</strong> feʼlga nisbatan qayerda turadi?</p>",
        "choices": ["Feʼl oldida, alohida soʻz boʻlib", "Feʼl oxirida qoʻshimcha boʻlib",
                    "Gap boshida", "Gap oxirida"],
        "correct": "Feʼl oldida, alohida soʻz boʻlib",
        "explanation": "<p><strong>안</strong> feʼlning oldiga alohida soʻz boʻlib "
                       "qoʻyiladi: <em>안 마셔요, 안 가요</em>. Oʻzakka yopishadigan shakl "
                       "esa 지 않다.</p>",
    },
    {
        "text": "<p><strong>지 않다</strong> qanday qoʻshiladi?</p>",
        "choices": ["Oʻzakka yopishadi", "Feʼl oldiga qoʻyiladi",
                    "Otga qoʻshiladi", "Gap boshiga qoʻyiladi"],
        "correct": "Oʻzakka yopishadi",
        "explanation": "<p>먹다 → 먹 + <strong>지 않다</strong> = 먹지 않아요. Bu shakl "
                       "oʻzbekcha <em>-ma</em> qoʻshimchasiga yaqinroq.</p>",
    },
    {
        "text": "<p><strong>안</strong> va <strong>지 않다</strong> maʼnosi farq "
                "qiladimi?</p>",
        "choices": ["Yoʻq — maʼnosi bir xil, uslubi boshqa",
                    "Ha — biri kuchliroq inkor",
                    "Ha — biri oʻtgan zamon",
                    "Ha — biri faqat sifatlar uchun"],
        "correct": "Yoʻq — maʼnosi bir xil, uslubi boshqa",
        "explanation": "<p>Ikkalasi ham “…mayman”. <strong>안</strong> ogʻzaki va qisqa, "
                       "<strong>지 않다</strong> yozma va biroz taʼkidli.</p>",
    },
    {
        "text": "<p><strong>있다</strong> ning inkori qaysi?</p>",
        "choices": ["없다", "안 있다", "있지 않다", "아니다"],
        "correct": "없다",
        "explanation": "<p><strong>없다</strong> — alohida soʻz. Koreys tilida uchta "
                       "soʻzning inkori shunday: 있다 → 없다, 알다 → 모르다, "
                       "이다 → 아니다.</p>",
    },
    {
        "text": "<p><strong>알다</strong> ning inkori qaysi?</p>",
        "choices": ["모르다", "안 알다", "알지 못하다", "없다"],
        "correct": "모르다",
        "explanation": "<p><strong>모르다</strong> — “bilmaslik”. 해요체 shakli "
                       "<em>몰라요</em>. <s>안 알아요</s> notoʻgʻri.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>“저는 커피를 마셔요” ni qisqa shaklda inkor qiling.</p>",
        "choices": ["저는 커피를 안 마셔요.", "저는 커피를 마셔 안요.",
                    "저는 안 커피를 마셔요.", "저는 커피를 마시 안요."],
        "correct": "저는 커피를 안 마셔요.",
        "explanation": "<p><strong>안</strong> feʼlning bevosita oldiga tushadi — "
                       "toʻldiruvchidan keyin, kesimdan oldin.</p>",
    },
    {
        "text": "<p>“가다” ni uzun shaklda inkor qiling (해요체).</p>",
        "choices": ["가지 않아요", "가지 않어요", "가 않아요", "안 가지요"],
        "correct": "가지 않아요",
        "explanation": "<p>Oʻzak 가 + 지 않다. Tuslanadigan narsa <strong>않다</strong>, "
                       "uning oxirgi unlisi ㅏ → <strong>않아요</strong>.</p>",
    },
    {
        "text": "<p>“공부하다” ni 안 bilan inkor qiling.</p>",
        "choices": ["공부 안 해요", "안 공부해요", "공부해 안요", "공부하 안요"],
        "correct": "공부 안 해요",
        "explanation": "<p>공부하다 = <strong>공부</strong> (ot) + <strong>하다</strong> "
                       "(feʼl). 안 feʼlning oldiga tushadi, ya'ni oʻrtaga: "
                       "<em>공부 안 해요</em>.</p>",
    },
    {
        "text": "<p>“공부하다” ni 지 않다 bilan inkor qiling.</p>",
        "choices": ["공부하지 않아요", "공부 하지 않아요", "공부지 않아요", "공부 안 하지요"],
        "correct": "공부하지 않아요",
        "explanation": "<p><strong>지 않다 boʻlinmaydi</strong> — u butun oʻzakka "
                       "yopishadi: 공부하 + 지 않아요. Faqat 안 oʻrtaga tushadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>저는 시간이 ___.</strong> "
                "(“vaqtim yoʻq”)</p>",
        "choices": ["없어요", "안 있어요", "있지 않아요", "아니에요"],
        "correct": "없어요",
        "explanation": "<p>있다 ning inkori — <strong>없다</strong>. <s>안 있어요</s> va "
                       "<s>있지 않아요</s> ishlatilmaydi.</p>",
    },
    {
        "text": "<p>“먹지 않다” ni oʻtgan zamonga oʻgiring.</p>",
        "choices": ["먹지 않았어요", "먹었지 않아요", "안 먹지 않았어요", "먹지 안았어요"],
        "correct": "먹지 않았어요",
        "explanation": "<p>Tuslanish <strong>oxirgi soʻzda</strong> boʻladi: 않다 → 않아요 "
                       "→ <strong>않았어요</strong>. Qisqa shakli: <em>안 "
                       "먹었어요</em>.</p>",
    },
    {
        "text": "<p>“날씨가 좋아요” ni inkor qiling.</p>",
        "choices": ["날씨가 안 좋아요.", "날씨가 좋아 안요.",
                    "날씨가 없어요.", "날씨가 좋아 아니에요."],
        "correct": "날씨가 안 좋아요.",
        "explanation": "<p>Sifatlar ham 안 yoki 지 않다 bilan inkor qilinadi: "
                       "<strong>안 좋아요</strong> yoki <em>좋지 않아요</em>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Nega “안 공부해요” notoʻgʻri?</p>",
        "choices": ["공부하다 ot + feʼldan iborat, 안 esa feʼl oldiga tushadi",
                    "Chunki 공부 받침 bilan tugaydi",
                    "Chunki 안 faqat sifatlar bilan keladi",
                    "Chunki 공부하다 sifat"],
        "correct": "공부하다 ot + feʼldan iborat, 안 esa feʼl oldiga tushadi",
        "explanation": "<p>공부하다 aslida “tahsilni qilmoq”. 안 <em>하다</em> ning oldiga "
                       "tushadi: <strong>공부 안 해요</strong>. Bu qoida barcha 명사+하다 "
                       "feʼllariga tegishli.</p>",
    },
    {
        "text": "<p>Qaysi juftlik <em>notoʻgʻri</em>?</p>",
        "choices": ["있다 → 안 있다", "있다 → 없다", "알다 → 모르다", "이다 → 아니다"],
        "correct": "있다 → 안 있다",
        "explanation": "<p>Bu uchta soʻz <strong>안 yoki 지 않다 olmaydi</strong> — "
                       "ularning inkori alohida soʻz. Toʻgʻrisi: <em>없다</em>.</p>",
    },
    {
        "text": "<p>Nega 지 않다 oʻzbek oʻquvchiga tabiiyroq tuyuladi?</p>",
        "choices": ["Oʻzbekchada inkor ham qoʻshimcha bilan beriladi (bormayman)",
                    "Chunki u qisqaroq",
                    "Chunki u faqat yozma nutqda",
                    "Chunki u tuslanmaydi"],
        "correct": "Oʻzbekchada inkor ham qoʻshimcha bilan beriladi (bormayman)",
        "explanation": "<p>Oʻzbekcha <em>bor<b>ma</b>yman</em> — qoʻshimcha oʻzakka "
                       "yopishadi, xuddi <strong>지 않다</strong> kabi. 안 esa alohida "
                       "soʻz va oʻzbekchada ekvivalenti yoʻq — lekin ogʻzaki nutqda "
                       "koreyslar aynan uni koʻproq ishlatadi.</p>",
    },
    {
        "text": "<p>“먹지 않아요” da nima tuslanadi?</p>",
        "choices": ["않다", "먹다", "지", "Ikkalasi ham"],
        "correct": "않다",
        "explanation": "<p>Oʻzak (먹) oʻzgarmaydi — tuslanadigan narsa <strong>않다</strong>. "
                       "Uning oxirgi unlisi ㅏ, shuning uchun har doim "
                       "<strong>않아요</strong>.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["저는 시간이 안 있어요.", "저는 시간이 없어요.",
                    "저는 커피를 안 마셔요.", "저는 공부 안 해요."],
        "correct": "저는 시간이 안 있어요.",
        "explanation": "<p>있다 ning inkori — <strong>없다</strong>: <em>시간이 "
                       "없어요</em>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["저는 일 안 했어요.", "저는 안 일했어요.",
                    "저는 일했 안어요.", "저는 일 없 했어요."],
        "correct": "저는 일 안 했어요.",
        "explanation": "<p>일하다 = 일 (ot) + 하다, shuning uchun 안 oʻrtaga: "
                       "<strong>일 안 했어요</strong>. Uzun shakli — <em>일하지 "
                       "않았어요</em>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Bu gapni uzun shaklga oʻgiring: <strong>저는 안 가요.</strong></p>",
        "choices": ["저는 가지 않아요.", "저는 가 않아요.",
                    "저는 안 가지 않아요.", "저는 가지 안아요."],
        "correct": "저는 가지 않아요.",
        "explanation": "<p>Oʻzak 가 + <strong>지 않아요</strong>. Maʼnosi oʻzgarmaydi — "
                       "faqat uslubi rasmiyroq boʻladi.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 커피 마셔요?<br>나: 아니요, ___</strong></p>",
        "choices": ["안 마셔요.", "못 마셔요.", "없어요.", "아니에요."],
        "correct": "안 마셔요.",
        "explanation": "<p>Oddiy inkor — <strong>안 마셔요</strong>. 못 마셔요 “icholmayman” "
                       "degan boshqa maʼno berardi (PK-22).</p>",
    },
]


# =====================================================================
# PK-22 — 못 / 지 못하다
# =====================================================================

Q_PK22 = [
    # 1–5 tanish
    {
        "text": "<p><strong>못</strong> nima maʼnoni beradi?</p>",
        "choices": ["Qila olmayman — imkoniyat yoʻq", "Qilmayman — xohlamayman",
                    "Qilaman", "Qilgan edim"],
        "correct": "Qila olmayman — imkoniyat yoʻq",
        "explanation": "<p><strong>못</strong> — imkoniyat yoʻqligi. Xohlaysiz, lekin "
                       "nimadir toʻsqinlik qilyapti. 안 esa tanlov: “xohlamayman”.</p>",
    },
    {
        "text": "<p><strong>안</strong> va <strong>못</strong> farqi nima?</p>",
        "choices": ["안 — tanlov, 못 — imkoniyat yoʻqligi",
                    "안 — imkoniyat yoʻqligi, 못 — tanlov",
                    "Farqi yoʻq",
                    "안 — hozirgi, 못 — oʻtgan zamon"],
        "correct": "안 — tanlov, 못 — imkoniyat yoʻqligi",
        "explanation": "<p>Oʻzbekcha bilan bir xil: <em>bormayman</em> (안 가요) va "
                       "<em>bora olmayman</em> (못 가요).</p>",
    },
    {
        "text": "<p><strong>못</strong> ning uzun shakli qaysi?</p>",
        "choices": ["지 못하다", "지 않다", "지 말다", "안 하다"],
        "correct": "지 못하다",
        "explanation": "<p><strong>지 못하다</strong> → 해요체 da <em>지 못해요</em>, chunki "
                       "못하다 — 하다 feʼli.</p>",
    },
    {
        "text": "<p><strong>못</strong> sifatlar bilan ishlatiladimi?</p>",
        "choices": ["Yoʻq — sifat bilan faqat 안 yoki 지 않다",
                    "Ha, har doim",
                    "Faqat oʻtgan zamonda",
                    "Faqat rasmiy nutqda"],
        "correct": "Yoʻq — sifat bilan faqat 안 yoki 지 않다",
        "explanation": "<p>“Yaxshi boʻla olmaslik” degan maʼno yoʻq — <s>못 좋아요</s> "
                       "notoʻgʻri. Toʻgʻrisi: <strong>안 좋아요</strong> yoki "
                       "<em>좋지 않아요</em>.</p>",
    },
    {
        "text": "<p><strong>못 해요</strong> qanday oʻqiladi?</p>",
        "choices": ["[모태요]", "[몯해요]", "[모새요]", "[못해요]"],
        "correct": "[모태요]",
        "explanation": "<p>격음화: 못 ning 받침i [ㄷ] boʻlib toʻxtaydi, keyin ㅎ bilan "
                       "birikib <strong>ㅌ</strong> beradi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>“Bugun bandman, borolmayman” — qaysi shakl kerak?</p>",
        "choices": ["오늘은 못 가요.", "오늘은 안 가요.",
                    "오늘은 가지 않아요.", "오늘은 없어요."],
        "correct": "오늘은 못 가요.",
        "explanation": "<p>Borishni xohlaysiz, lekin ish toʻsqinlik qilyapti → "
                       "<strong>못</strong>. 안 가요 “bormoqchi emasman” degan boshqa "
                       "maʼno berardi.</p>",
    },
    {
        "text": "<p>“Kofeni yoqtirmayman, ichmayman” — qaysi shakl kerak?</p>",
        "choices": ["커피를 안 마셔요.", "커피를 못 마셔요.",
                    "커피가 없어요.", "커피를 마시지 못해요."],
        "correct": "커피를 안 마셔요.",
        "explanation": "<p>Bu <strong>tanlov</strong> — yoqtirmaysiz, shuning uchun 안. "
                       "Agar shifokor taqiqlagan boʻlsa, <em>못 마셔요</em> "
                       "boʻlardi.</p>",
    },
    {
        "text": "<p>“가다” ni uzun shaklda “borolmayman” qiling.</p>",
        "choices": ["가지 못해요", "가지 않아요", "가지 못아요", "못 가지요"],
        "correct": "가지 못해요",
        "explanation": "<p>Oʻzak 가 + 지 못하다. 못하다 — 하다 feʼli, shuning uchun "
                       "<strong>못해요</strong>.</p>",
    },
    {
        "text": "<p>“공부하다” ni 못 bilan inkor qiling (oʻtgan zamon).</p>",
        "choices": ["공부 못 했어요", "못 공부했어요", "공부했 못어요", "공부하 못았어요"],
        "correct": "공부 못 했어요",
        "explanation": "<p>PK-21 dagi qoida bu yerda ham ishlaydi: 명사+하다 da inkor "
                       "<strong>oʻrtaga</strong> tushadi. Oʻqilishi "
                       "[공부 모태써요].</p>",
    },
    {
        "text": "<p><strong>못 먹어요</strong> qanday oʻqiladi?</p>",
        "choices": ["[몬머거요]", "[몯머거요]", "[모머거요]", "[못머거요]"],
        "correct": "[몬머거요]",
        "explanation": "<p>비음화: 못 ning [ㄷ] tovushi ㅁ oldidan <strong>[ㄴ]</strong> ga "
                       "aylanadi.</p>",
    },
    {
        "text": "<p><strong>못 가요</strong> qanday oʻqiladi?</p>",
        "choices": ["[몯까요]", "[몬가요]", "[모까요]", "[못가요]"],
        "correct": "[몯까요]",
        "explanation": "<p>경음화: toʻxtovchi 받침dan keyin ㄱ qattiqlashib "
                       "<strong>ㄲ</strong> boʻladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>날씨가 ___ 좋아요.</strong> "
                "(“havo yaxshi emas”)</p>",
        "choices": ["안", "못", "없", "아니"],
        "correct": "안",
        "explanation": "<p><strong>안</strong> — sifat bilan faqat shu ishlatiladi. "
                       "<s>못 좋아요</s> notoʻgʻri.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>“한국어를 안 배워요” va “한국어를 못 배워요” farqi nima?</p>",
        "choices": ["Birinchisi — xohlamayman, ikkinchisi — imkoniyat yoʻq",
                    "Birinchisi — imkoniyat yoʻq, ikkinchisi — xohlamayman",
                    "Farqi yoʻq",
                    "Birinchisi oʻtgan zamon"],
        "correct": "Birinchisi — xohlamayman, ikkinchisi — imkoniyat yoʻq",
        "explanation": "<p><strong>안 배워요</strong> — vaqtim bor, lekin oʻrganmayman. "
                       "<strong>못 배워요</strong> — oʻrganmoqchiman, lekin maktab yoki "
                       "vaqt yoʻq.</p>",
    },
    {
        "text": "<p>Oʻzbekchada 못 ga nima toʻgʻri keladi?</p>",
        "choices": ["-a olmaslik (bora olmayman)", "-ma (bormayman)",
                    "-gan (borgan)", "-moqchi (bormoqchi)"],
        "correct": "-a olmaslik (bora olmayman)",
        "explanation": "<p>Oʻzbek tilida bu farq allaqachon bor: <em>bormayman</em> "
                       "(안 가요) va <em>bora <b>olmayman</b></em> (못 가요). Shuning uchun "
                       "bu dars oʻzbek oʻquvchiga oson tushadi.</p>",
    },
    {
        "text": "<p>Nega 못 ning talaffuzi uch xil boʻladi?</p>",
        "choices": ["Keyingi tovushga qarab 경음화, 비음화 yoki 격음화 ishlaydi",
                    "Chunki 못 ikki xil yoziladi",
                    "Chunki 못 sifat ham, feʼl ham",
                    "Chunki u har doim oʻtgan zamonda"],
        "correct": "Keyingi tovushga qarab 경음화, 비음화 yoki 격음화 ishlaydi",
        "explanation": "<p>못 ning 받침i [ㄷ] boʻlib toʻxtaydi, keyin PK-8 dagi qoidalar "
                       "ishga tushadi: 못 가요 [몯까요], 못 먹어요 [몬머거요], "
                       "못 해요 [모태요].</p>",
    },
    {
        "text": "<p>“지 못해요” da nega 해요 boʻladi?</p>",
        "choices": ["못하다 — 하다 feʼli, 하다 esa har doim 해요",
                    "Chunki 못 받침li",
                    "Chunki bu sifat",
                    "Chunki u oʻtgan zamon"],
        "correct": "못하다 — 하다 feʼli, 하다 esa har doim 해요",
        "explanation": "<p>PK-18 qoidasi: 하다 → 해요. Shuning uchun 지 못하다 har doim "
                       "<strong>지 못해요</strong> boʻladi — yangi narsa yodlash "
                       "kerak emas.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["날씨가 못 좋아요.", "날씨가 안 좋아요.",
                    "오늘은 못 가요.", "공부 못 했어요."],
        "correct": "날씨가 못 좋아요.",
        "explanation": "<p><strong>못 sifat bilan ishlatilmaydi</strong>. Toʻgʻrisi: "
                       "<em>날씨가 안 좋아요</em>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["어제 공부 못 했어요.", "어제 못 공부했어요.",
                    "어제 공부했 못어요.", "어제 공부 안 못 했어요."],
        "correct": "어제 공부 못 했어요.",
        "explanation": "<p>명사+하다 feʼllarida inkor <strong>oʻrtaga</strong> tushadi — "
                       "안 uchun ham, 못 uchun ham bir xil qoida.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Afsona kofeni yoqtirmaydi. Dilnozaga shifokor kofeni taqiqlagan. "
                "Qaysi qator toʻgʻri?</p>",
        "choices": ["Afsona: 안 마셔요 · Dilnoza: 못 마셔요",
                    "Afsona: 못 마셔요 · Dilnoza: 안 마셔요",
                    "Ikkalasi ham: 안 마셔요",
                    "Ikkalasi ham: 못 마셔요"],
        "correct": "Afsona: 안 마셔요 · Dilnoza: 못 마셔요",
        "explanation": "<p>Afsonaniki — <strong>tanlov</strong> (yoqtirmaydi) → 안. "
                       "Dilnozaniki — <strong>toʻsqinlik</strong> (taqiq bor) → 못. "
                       "Bir xil harakat, ikki xil sabab.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 오늘 집에 와요?<br>나: 아니요, 일이 많아요. ___</strong></p>",
        "choices": ["못 가요.", "안 가요.", "없어요.", "가지 않아요."],
        "correct": "못 가요.",
        "explanation": "<p>Sabab aytilgan — <em>일이 많아요</em> (ishim koʻp), ya'ni "
                       "toʻsqinlik bor. Shuning uchun <strong>못 가요</strong>. 안 가요 "
                       "bu sababga mos kelmaydi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-21 Mashq: Inkor 1 — 안 va 지 않다",
        "description": "20 savol — ikki inkor shakli, 하다 feʼllari va uchta istisno.",
        "tutorial":    "PK-21:",
        "level":       "easy",
        "questions":   Q_PK21,
    },
    {
        "title":       "PK-22 Mashq: Inkor 2 — 못 va 지 못하다",
        "description": "20 savol — 안 va 못 farqi, sifat cheklovi va 못 ning talaffuzi.",
        "tutorial":    "PK-22:",
        "level":       "easy",
        "questions":   Q_PK22,
    },
]
