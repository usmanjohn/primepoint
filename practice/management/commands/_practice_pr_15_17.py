# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-15 … PR-17.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_15_17.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "Russian",
    "description": "Rus tili — grammatika va yozuv mashqlari",
    "icon":        "bi-translate",
    "color":       "#b91c1c",
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
# PR-15 — Savol soʻzlari
# =====================================================================

Q_PR15 = [
    # 1–5 tanish
    {
        "text": "<p><strong>где?</strong> nima degani?</p>",
        "choices": ["qayerda?", "qayerga?", "qayerdan?", "qachon?"],
        "correct": "qayerda?",
        "explanation": "<p><strong>где</strong> — turgan joyni soʻraydi, harakat yoʻq. "
                       "<em>Куда́</em> — qayerga (harakat bor), <em>отку́да</em> — "
                       "qayerdan.</p>",
    },
    {
        "text": "<p>Rus tilida savol berish uchun yordamchi feʼl kerakmi?</p>",
        "choices": ["Ha, yordamchi soʻz qoʻshiladi", "Yoʻq — savol soʻzini oldinga "
                    "qoʻyasiz, xolos", "Faqat uzun gaplarda", "Faqat rasmiy nutqda"],
        "correct": "Yoʻq — savol soʻzini oldinga qoʻyasiz, xolos",
        "explanation": "<p>Ingliz tilida <em>do/does</em> kerak. Rus va oʻzbek tillarida "
                       "esa yoʻq: <em>Qayerda yashaysan?</em> — <strong>Где ты "
                       "живёшь?</strong> Savol soʻzi oldinga chiqadi, qolgani oʻz "
                       "joyida qoladi.</p>",
    },
    {
        "text": "<p><strong>отку́да?</strong> nima degani?</p>",
        "choices": ["qayerda?", "qayerdan?", "qayerga?", "nega?"],
        "correct": "qayerdan?",
        "explanation": "<p><strong>отку́да</strong> — chiqish nuqtasini soʻraydi. "
                       "Uchlik: <strong>где</strong> (qayerda) — <strong>куда́</strong> "
                       "(qayerga) — <strong>отку́да</strong> (qayerdan), oʻzbekcha bilan "
                       "aynan mos.</p>",
    },
    {
        "text": "<p>Qaysi savol soʻzi otga <strong>moslashadi</strong>?</p>",
        "choices": ["где", "когда́", "како́й", "почему́"],
        "correct": "како́й",
        "explanation": "<p><strong>како́й / кака́я / како́е / каки́е</strong>. Xuddi "
                       "shunday <em>чей</em> (PR-10) va <em>ско́лько</em> ham. Qolgan "
                       "savol soʻzlari hech qachon oʻzgarmaydi.</p>",
    },
    {
        "text": "<p><strong>Потому́ что</strong> nima degani?</p>",
        "choices": ["chunki", "shuning uchun", "lekin", "agar"],
        "correct": "chunki",
        "explanation": "<p><strong>Потому́ что</strong> — “chunki”, sababni bildiradi. "
                       "U <em>почему́?</em> savoliga javob beradi: <em>— Почему́? — "
                       "Потому́ что…</em></p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga: <strong>___ уро́к? — За́втра.</strong></p>",
        "choices": ["Где", "Куда́", "Когда́", "Как"],
        "correct": "Когда́",
        "explanation": "<p><strong>Когда́ уро́к?</strong> Javobda vaqt turibdi "
                       "(<em>за́втра</em>), demak savol <strong>когда́</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>___ ты? — Домо́й.</strong></p>",
        "choices": ["Где", "Куда́", "Отку́да", "Почему́"],
        "correct": "Куда́",
        "explanation": "<p><strong>Куда́ ты?</strong> Javob <em>домо́й</em> (“uyga”) — "
                       "bu yoʻnalish, harakat bor. Agar javob <em>до́ма</em> (“uyda”) "
                       "boʻlsa edi, savol <strong>где</strong> boʻlardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>___ Дилно́за? — Здесь.</strong></p>",
        "choices": ["Куда́", "Отку́да", "Где", "Заче́м"],
        "correct": "Где",
        "explanation": "<p><strong>Где Дилно́за?</strong> Javob <em>здесь</em> — turgan "
                       "joy, harakat yoʻq. Bu <strong>где</strong> ning aynan oʻz "
                       "vazifasi.</p>",
    },
    {
        "text": "<p><strong>почему́</strong> yoki <strong>заче́м</strong>? "
                "<strong>___ он до́ма? — Потому́ что сего́дня суббо́та.</strong></p>",
        "choices": ["Почему́", "Заче́м", "Ikkalasi ham", "Hech qaysisi"],
        "correct": "Почему́",
        "explanation": "<p>Javob <em>Потому́ что…</em> bilan boshlanyapti — bu "
                       "<strong>sabab</strong>, demak savol <strong>почему́</strong>. "
                       "<em>Заче́м</em> esa maqsadni soʻraydi.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring: <strong>Bu qanday maktab?</strong></p>",
        "choices": ["Како́й э́то шко́ла?", "Кака́я э́то шко́ла?", "Како́е э́то шко́ла?",
                    "Как э́то шко́ла?"],
        "correct": "Кака́я э́то шко́ла?",
        "explanation": "<p><strong>Кака́я э́то шко́ла?</strong> <em>Шко́ла</em> ayol "
                       "jinsi, va <strong>како́й</strong> otga moslashadi. "
                       "<em>Как</em> esa boshqa soʻz — u “qanday (tarzda)” degani: "
                       "<em>Как дела́?</em></p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>___ дела́? — Хорошо́.</strong></p>",
        "choices": ["Како́й", "Кака́я", "Как", "Что"],
        "correct": "Как",
        "explanation": "<p><strong>Как дела́?</strong> — turgʻun ibora (PR-7). "
                       "<em>Как</em> — “qanday tarzda”, u oʻzgarmaydi. "
                       "<em>Како́й</em> esa otga qaraydi va moslashadi.</p>",
    },
    {
        "text": "<p><strong>Где шко́ла?</strong> gapida ovoz qanday yuradi?</p>",
        "choices": ["Oxirigacha koʻtariladi", "Savol soʻzida koʻtarilib, keyin pasayadi",
                    "Bir tekis", "Oxirida koʻtariladi"],
        "correct": "Savol soʻzida koʻtarilib, keyin pasayadi",
        "explanation": "<p>ГДЕ ↗ шко́ла ↘. Bu “ha/yoʻq” savolidan farq qiladi — u yerda "
                       "ovoz oxirigacha koʻtariladi: <em>Э́то шко́ла?</em> ↗ Rus quloqi "
                       "bu ikki ohangni darrov ajratadi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>Где ты идёшь?</strong> — bu gapda nima notoʻgʻri?</p>",
        "choices": ["Harakat bor, demak куда́ boʻlishi kerak", "Savol soʻzi oxirda "
                    "boʻlishi kerak", "Hech nima notoʻgʻri emas", "Ты oʻrniga вы kerak"],
        "correct": "Harakat bor, demak куда́ boʻlishi kerak",
        "explanation": "<p>Toʻgʻrisi <strong>Куда́ ты идёшь?</strong> — “qayerga "
                       "ketyapsan?”. <em>Где</em> harakatsiz joyni soʻraydi. "
                       "Oʻzbekchada ham <em>qayerga ketyapsan</em> deysiz, "
                       "<em>qayerda</em> emas.</p>",
    },
    {
        "text": "<p><strong>Почему́</strong> va <strong>заче́м</strong> — farqi nima?</p>",
        "choices": ["Почему́ — sabab (orqaga qaraydi), заче́м — maqsad (oldinga qaraydi)",
                    "Почему́ — rasmiy, заче́м — norasmiy",
                    "Почему́ — odam haqida, заче́м — narsa haqida",
                    "Farqi yoʻq"],
        "correct": "Почему́ — sabab (orqaga qaraydi), заче́м — maqsad (oldinga qaraydi)",
        "explanation": "<p><em>Почему́ он до́ма?</em> — nima boʻlgani uchun. "
                       "<em>Заче́м э́то?</em> — nima maqsadda kerak. Oʻzbekchada bu farq "
                       "<em>“nega”</em> va <em>“nima uchun”</em> orasida sezilib "
                       "turadi.</p>",
    },
    {
        "text": "<p>Nega <strong>где / куда́ / отку́да</strong> uchligi oʻzbek "
                "oʻquvchisi uchun oson?</p>",
        "choices": ["Chunki oʻzbekchada ham aynan shu uchlik bor: "
                    "qayerda / qayerga / qayerdan",
                    "Chunki ular bir xil oʻqiladi",
                    "Chunki ular kam ishlatiladi",
                    "Chunki ularni yodlash shart emas"],
        "correct": "Chunki oʻzbekchada ham aynan shu uchlik bor: "
                   "qayerda / qayerga / qayerdan",
        "explanation": "<p>Ingliz tili buni ikkitaga siqadi (<em>where</em> / "
                       "<em>where … from</em>), rus va oʻzbek tillari esa uchtasini ham "
                       "alohida saqlaydi. Yaʼni tushunchani oʻrganish shart emas — "
                       "faqat uchta soʻzni yodlash kifoya.</p>",
    },
    {
        "text": "<p>Hozircha <strong>Где?</strong> savoliga qanday javob berish "
                "xavfsiz?</p>",
        "choices": ["Ravish bilan: здесь, там", "Ot bilan: шко́ла",
                    "Feʼl bilan", "Son bilan"],
        "correct": "Ravish bilan: здесь, там",
        "explanation": "<p>Ot bilan javob berish uchun kelishik kerak: "
                       "<em>в шко́ле</em> (PR-30). Ravishlar esa hech qanday kelishik "
                       "talab qilmaydi — <strong>здесь, там, туда́, сюда́, домо́й</strong> "
                       "bilan bemalol gaplashish mumkin.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi savolda xato bor?</p>",
        "choices": ["Где ты живёшь?", "Кто э́то?", "Кто э́то кни́га?", "Когда́ уро́к?"],
        "correct": "Кто э́то кни́га?",
        "explanation": "<p>Kitob jonsiz, demak <strong>Что э́то?</strong> boʻlishi kerak "
                       "(PR-6). <em>Кто</em> faqat odam va hayvon uchun.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Как дела́ у тебя́ есть?", "Как дела́?", "Как есть дела́?",
                    "Что дела́?"],
        "correct": "Как дела́?",
        "explanation": "<p><strong>Как дела́?</strong> — turgʻun ibora (PR-7), unga hech "
                       "nima qoʻshilmaydi. <em>Есть</em> bu yerda umuman kerak emas — "
                       "bu mavjudlik haqidagi gap emas (PR-14).</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Soʻzlarni tartibga soling.</p><p><strong>Жасу́р / где</strong></p>",
        "choices": ["Где Жасу́р?", "Жасу́р где?", "Где Жасу́р есть?", "Жасу́р есть где?"],
        "correct": "Где Жасу́р?",
        "explanation": "<p><strong>Где Жасу́р?</strong> Savol soʻzi boshda. "
                       "(<em>Жасу́р где?</em> suhbatda uchraydi, lekin bu taʼkidli "
                       "shakl — oddiy savol emas. <em>Есть</em> esa kerak emas.)</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p><p><strong>— ___ ты? — Отту́да.</strong></p>",
        "choices": ["Где", "Куда́", "Отку́да", "Когда́"],
        "correct": "Отку́да",
        "explanation": "<p><strong>Отку́да ты?</strong> Javob <em>отту́да</em> "
                       "(“u yerdan”) — chiqish nuqtasi. Javobning shakli sizga savolni "
                       "aytib turibdi: <em>там → где</em>, <em>туда́ → куда́</em>, "
                       "<em>отту́да → отку́да</em>.</p>",
    },
]


# =====================================================================
# PR-16 — этот / тот
# =====================================================================

Q_PR16 = [
    # 1–5 tanish
    {
        "text": "<p><strong>кни́га</strong> bilan qaysi shakl ishlatiladi?</p>",
        "choices": ["э́тот", "э́та", "э́то", "э́ти"],
        "correct": "э́та",
        "explanation": "<p><strong>э́та кни́га</strong>. Aniqlovchi <em>э́тот</em> otga "
                       "moslashadi: <strong>э́тот / э́та / э́то / э́ти</strong>.</p>",
    },
    {
        "text": "<p>Mustaqil <strong>э́то</strong> nechta shaklga ega?</p>",
        "choices": ["Bitta — u hech qachon oʻzgarmaydi", "Ikkita", "Uchta", "Toʻrtta"],
        "correct": "Bitta — u hech qachon oʻzgarmaydi",
        "explanation": "<p><em>Э́то дом. Э́то кни́га. Э́то о́кна.</em> — bitta shakl, "
                       "hamma holat uchun (PR-6). Aniqlovchi <strong>э́тот</strong> esa "
                       "toʻrtta shaklga ega.</p>",
    },
    {
        "text": "<p><strong>тот</strong> nima degani?</p>",
        "choices": ["bu", "anavi, oʻsha", "mana", "shu yerda"],
        "correct": "anavi, oʻsha",
        "explanation": "<p><strong>тот</strong> uzoqdagi yoki boshqa narsani koʻrsatadi. "
                       "Toʻliq qator: <strong>тот / та / то / те</strong>.</p>",
    },
    {
        "text": "<p><strong>вот</strong> nima degani?</p>",
        "choices": ["mana", "shu yerda", "u yerda", "qayerda"],
        "correct": "mana",
        "explanation": "<p><strong>Вот</strong> — koʻrsatish soʻzi: <em>Вот моя́ "
                       "кни́га</em> (“mana kitobim”). <strong>Здесь</strong> esa joyni "
                       "bildiradi: <em>Моя́ кни́га здесь</em> (“kitobim shu yerda”).</p>",
    },
    {
        "text": "<p>Rus tilida koʻrsatishning nechta darajasi bor?</p>",
        "choices": ["Ikkita — э́тот va тот", "Uchta", "Bitta", "Toʻrtta"],
        "correct": "Ikkita — э́тот va тот",
        "explanation": "<p>Oʻzbek tilida uchta daraja bor: <em>bu / shu / u</em>. Rus "
                       "tilida esa ikkita: <strong>э́тот</strong> va <strong>тот</strong>. "
                       "Oʻzbekchadagi <em>bu</em> va <em>shu</em> — ikkalasi ham "
                       "<strong>э́тот</strong> ga tushadi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga: <strong>___ шко́ла но́вая.</strong> (bu maktab)</p>",
        "choices": ["Э́то", "Э́та", "Э́тот", "Э́ти"],
        "correct": "Э́та",
        "explanation": "<p><strong>Э́та шко́ла но́вая.</strong> Bu yerda “bu” maktabga "
                       "yopishgan, demak aniqlovchi shakl kerak. <em>Шко́ла</em> ayol "
                       "jinsi → <strong>э́та</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>___ шко́ла.</strong> (bu — maktab)</p>",
        "choices": ["Э́то", "Э́та", "Э́тот", "Э́ти"],
        "correct": "Э́то",
        "explanation": "<p><strong>Э́то шко́ла.</strong> Bu yerda nomlayapmiz — “bu — "
                       "maktab”. Mustaqil <strong>э́то</strong>, u oʻzgarmaydi. "
                       "Oldingi savol bilan yonma-yon qoʻying: butun dars shu ikki "
                       "gapda.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>Э́ти ру́чки но́вые, а ___ ста́рые.</strong></p>",
        "choices": ["тот", "та", "то", "те"],
        "correct": "те",
        "explanation": "<p><strong>те</strong>. Koʻplikda uzoqdagisi — <strong>те</strong>. "
                       "Toʻliq qator: <em>э́тот — тот, э́та — та, э́то — то, "
                       "э́ти — те</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>___ дом но́вый, а тот ста́рый.</strong></p>",
        "choices": ["Э́то", "Э́та", "Э́тот", "Э́ти"],
        "correct": "Э́тот",
        "explanation": "<p><strong>Э́тот дом но́вый.</strong> <em>Дом</em> erkak jinsi, "
                       "va “bu” uyga yopishgan. Gapning ikkinchi qismida "
                       "<strong>тот</strong> — uzoqdagisi.</p>",
    },
    {
        "text": "<p>Doʻstingizga kitobingizni koʻrsatyapsiz. Nima deysiz?</p>",
        "choices": ["Здесь моя́ кни́га!", "Вот моя́ кни́га!", "Там моя́ кни́га!",
                    "Э́то здесь кни́га!"],
        "correct": "Вот моя́ кни́га!",
        "explanation": "<p><strong>Вот</strong> — koʻrsatganda. <em>Здесь</em> joyni "
                       "bildiradi (“shu yerda”), <em>там</em> esa uzoqni (“ana u "
                       "yerda”).</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring: <strong>Bu kitob meniki emas.</strong></p>",
        "choices": ["Э́то кни́га не моя́.", "Э́та кни́га не моя́.",
                    "Э́тот кни́га не моя́.", "Э́ти кни́га не моя́."],
        "correct": "Э́та кни́га не моя́.",
        "explanation": "<p><strong>Э́та кни́га не моя́.</strong> “Bu” kitobga yopishgan "
                       "(“bu kitob”), demak <strong>э́та</strong>. Agar <em>Э́то не "
                       "моя́ кни́га</em> desangiz — bu ham toʻgʻri, lekin maʼnosi "
                       "biroz boshqa: “bu mening kitobim emas”.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>Кака́я кни́га твоя́ — э́та и́ли ___?</strong></p>",
        "choices": ["тот", "та", "то", "те"],
        "correct": "та",
        "explanation": "<p><strong>та</strong>. <em>Кни́га</em> ayol jinsi, demak "
                       "uzoqdagisi <strong>та</strong>. Diqqat: otni takrorlash shart "
                       "emas — <em>э́та</em> va <em>та</em> oʻzi yetadi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>Э́то кни́га</strong> va <strong>Э́та кни́га</strong> — farqi "
                "nima?</p>",
        "choices": ["Birinchisi “bu — kitob” (nomlash), ikkinchisi “bu kitob” (aniqlash)",
                    "Farqi yoʻq", "Birinchisi koʻplik", "Ikkinchisi notoʻgʻri"],
        "correct": "Birinchisi “bu — kitob” (nomlash), ikkinchisi “bu kitob” (aniqlash)",
        "explanation": "<p><em>Э́то кни́га.</em> — nima ekanini aytyapmiz, gap tugadi. "
                       "<em>Э́та кни́га…</em> — qaysi kitob ekanini aytyapmiz, gap davom "
                       "etadi: <em>Э́та кни́га но́вая</em>.</p>",
    },
    {
        "text": "<p>Tekshiruvning eng oson yoʻli qaysi?</p>",
        "choices": ["Oʻzbekchada “bu” dan keyin toʻxtalsangiz — э́то; toʻxtalmasangiz "
                    "— э́тот",
                    "Gapning uzunligiga qarash", "Urgʻuga qarash",
                    "Har doim э́то ishlatish"],
        "correct": "Oʻzbekchada “bu” dan keyin toʻxtalsangiz — э́то; toʻxtalmasangiz "
                   "— э́тот",
        "explanation": "<p>“Bu — kitob” (toʻxtaldingiz, tire tushdi) → mustaqil "
                       "<strong>э́то</strong>. “Bu kitob yangi” (toʻxtalmadingiz) → "
                       "<strong>э́та</strong>. Bu tekshiruv deyarli har doim "
                       "ishlaydi.</p>",
    },
    {
        "text": "<p><strong>Э́то окно́</strong> — nima uchun bu ibora ikki xil "
                "tushunilishi mumkin?</p>",
        "choices": ["Chunki oʻrta jinsda mustaqil va aniqlovchi shakl bir xil koʻrinadi",
                    "Chunki окно́ chet soʻz",
                    "Chunki urgʻu ikki joyda boʻlishi mumkin",
                    "Chunki окно́ koʻplikda"],
        "correct": "Chunki oʻrta jinsda mustaqil va aniqlovchi shakl bir xil koʻrinadi",
        "explanation": "<p><em>Э́то окно́.</em> = “bu — deraza”. <em>Э́то окно́ "
                       "большо́е.</em> = “bu deraza katta”. Davomi hal qiladi. Boshqa "
                       "jinslarda bunday chalkashlik yoʻq: <em>э́то дом</em> va "
                       "<em>э́тот дом</em> aniq farq qiladi.</p>",
    },
    {
        "text": "<p><strong>Вот</strong> va <strong>здесь</strong> — farqi nima?</p>",
        "choices": ["Вот — koʻrsatish (“mana”), здесь — joy (“shu yerda”)",
                    "Вот — uzoq, здесь — yaqin",
                    "Farqi yoʻq", "Вот — savol, здесь — javob"],
        "correct": "Вот — koʻrsatish (“mana”), здесь — joy (“shu yerda”)",
        "explanation": "<p><em>Вот шко́ла</em> = “mana maktab” (endi koʻrsatyapman). "
                       "<em>Шко́ла здесь</em> = “maktab shu yerda” (joyini "
                       "aytyapman).</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Э́та кни́га моя́.", "Э́тот дом но́вый.", "Э́тот кни́га моя́.",
                    "Э́ти ру́чки но́вые."],
        "correct": "Э́тот кни́га моя́.",
        "explanation": "<p>Toʻgʻrisi <strong>Э́та кни́га моя́</strong>. <em>Кни́га</em> "
                       "ayol jinsi, demak <strong>э́та</strong>. Aniqlovchi "
                       "<em>э́тот</em> otga moslashadi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Э́то дом но́вый, а э́то ста́рый.", "Э́тот дом но́вый, а тот ста́рый.",
                    "Э́тот дом но́вый, а э́тот ста́рый.", "Э́то дом но́вый, а тот ста́рый."],
        "correct": "Э́тот дом но́вый, а тот ста́рый.",
        "explanation": "<p>Ikkita uyni solishtiryapmiz: yaqindagisi "
                       "<strong>э́тот</strong>, uzoqdagisi <strong>тот</strong>. "
                       "Ikkalasini <em>э́то</em> yoki <em>э́тот</em> deb atash — "
                       "solishtirishni buzadi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Soʻzlarni tartibga soling.</p><p><strong>и́ли / э́тот / тот</strong></p>",
        "choices": ["Э́тот и́ли тот?", "Тот и́ли э́тот э́то?", "И́ли э́тот тот?",
                    "Э́тот тот и́ли?"],
        "correct": "Э́тот и́ли тот?",
        "explanation": "<p><strong>Э́тот и́ли тот?</strong> — “bumi yoki anavimi?”. "
                       "Rus suhbatida juda koʻp uchraydigan savol; otni takrorlash "
                       "shart emas.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p><p><strong>— Кака́я ру́чка твоя́?<br>"
                "— Не э́та, а ___.</strong></p>",
        "choices": ["тот", "та", "то", "те"],
        "correct": "та",
        "explanation": "<p><strong>та</strong>. <em>Ру́чка</em> ayol jinsi → "
                       "<strong>та</strong>. Bu yerda ikkita dars birga ishlayapti: "
                       "<em>э́та/та</em> (PR-16) va <em>«не X, а Y»</em> qurilmasi "
                       "(PR-17).</p>",
    },
]


# =====================================================================
# PR-17 — Да, нет, не, ни
# =====================================================================

Q_PR17 = [
    # 1–5 tanish
    {
        "text": "<p><strong>Нет</strong> va <strong>не</strong> — asosiy farq nima?</p>",
        "choices": ["Нет — javob va yoʻqlik, oʻzi turadi; не — bitta soʻzni inkor qiladi",
                    "Нет — rasmiy, не — norasmiy",
                    "Нет — otlar bilan, не — sifatlar bilan",
                    "Farqi yoʻq"],
        "correct": "Нет — javob va yoʻqlik, oʻzi turadi; не — bitta soʻzni inkor qiladi",
        "explanation": "<p>Ular bir gapda birga ishlaydi: <em>«<strong>Нет</strong>, э́то "
                       "<strong>не</strong> шко́ла»</em> — birinchisi savolga javob, "
                       "ikkinchisi <em>шко́ла</em> soʻzini inkor qiladi.</p>",
    },
    {
        "text": "<p><strong>Не</strong> qayerda turadi?</p>",
        "choices": ["Inkor qilinadigan soʻzning oldida", "Gap oxirida", "Gap boshida",
                    "Otdan keyin"],
        "correct": "Inkor qilinadigan soʻzning oldida",
        "explanation": "<p><em>Э́то <strong>не</strong> шко́ла.</em> Oʻzbekcha "
                       "<em>emas</em> soʻzning orqasida turadi, ruscha <strong>не</strong> "
                       "esa oldida. Bu kichik farq har kuni xatoga sabab boʻladi.</p>",
    },
    {
        "text": "<p><strong>ни … ни …</strong> nima degani?</p>",
        "choices": ["na … na …", "yoki … yoki …", "ham … ham …", "agar … unda …"],
        "correct": "na … na …",
        "explanation": "<p>Ruscha <strong>ни … ни …</strong> va oʻzbekcha "
                       "<strong>na … na …</strong> aynan bir xil ishlaydi: ikkalasi ham "
                       "juftlikda keladi va ikkala qismni birdan inkor qiladi.</p>",
    },
    {
        "text": "<p><strong>«Не X, а Y»</strong> qurilmasi nima uchun?</p>",
        "choices": ["Tuzatish: X emas, balki Y", "Savol berish", "Qarshilik bildirish",
                    "Sabab aytish"],
        "correct": "Tuzatish: X emas, balki Y",
        "explanation": "<p><em>Он не студе́нт, <strong>а</strong> учи́тель.</em> — "
                       "notoʻgʻri fikrni almashtiradi. Bu rus tilida har kuni "
                       "ishlatiladigan qolip.</p>",
    },
    {
        "text": "<p><strong>Ни</strong> yolgʻiz ishlaydimi?</p>",
        "choices": ["Ha, har doim", "Yoʻq — u juftlikda keladi", "Faqat savolda",
                    "Faqat gap boshida"],
        "correct": "Yoʻq — u juftlikda keladi",
        "explanation": "<p><strong>Ни</strong> э́то, <strong>ни</strong> то. Bitta "
                       "<em>ни</em> yolgʻiz turmaydi — u har doim takrorlanadi va "
                       "ikkala qismni inkor qiladi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga: <strong>Э́то ___ мой телефо́н.</strong></p>",
        "choices": ["нет", "не", "ни", "да"],
        "correct": "не",
        "explanation": "<p><strong>не</strong>. Gap ichida, soʻzning oldida — "
                       "<strong>не</strong>. <em>Нет</em> esa javob sifatida gap boshida "
                       "turadi: <em>Нет, э́то не мой телефо́н.</em></p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>— Э́то шко́ла? — ___, э́то библиоте́ка.</strong></p>",
        "choices": ["Не", "Нет", "Ни", "Да"],
        "correct": "Нет",
        "explanation": "<p><strong>Нет</strong> — savolga javob. U oʻzi turadi va odatda "
                       "gap boshida. Gap ichida esa <em>не</em> ishlatilardi: "
                       "<em>Нет, э́то не шко́ла.</em></p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>Он не врач, ___ учи́тель.</strong></p>",
        "choices": ["но", "а", "и", "или"],
        "correct": "а",
        "explanation": "<p><strong>а</strong> — bu <em>«не X, а Y»</em> qurilmasi, "
                       "tuzatish. <strong>Но</strong> bu yerda notoʻgʻri: u qarshilik "
                       "bildiradi (<em>Он врач, но молодо́й</em>).</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring: <strong>Bu kitob emas.</strong></p>",
        "choices": ["Э́то кни́га не.", "Э́то нет кни́га.", "Э́то не кни́га.",
                    "Не э́то кни́га."],
        "correct": "Э́то не кни́га.",
        "explanation": "<p><strong>Э́то не кни́га.</strong> <em>Не</em> aynan "
                       "<em>кни́га</em> ning oldida. Gap oxiriga qoʻyish — oʻzbekcha "
                       "<em>emas</em> ning taʼsiri va bu ruschada xato.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>___ чай, ___ ко́фе. Спаси́бо.</strong></p>",
        "choices": ["Не … не", "Нет … нет", "Ни … ни", "А … а"],
        "correct": "Ни … ни",
        "explanation": "<p><strong>Ни чай, ни ко́фе.</strong> — “na choy, na qahva”. "
                       "Ikkala narsani birdan rad qilyapmiz, demak juftlik "
                       "<strong>ни … ни …</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>Шко́ла но́вая, ___ ма́ленькая.</strong></p>",
        "choices": ["а", "но", "ни", "не"],
        "correct": "но",
        "explanation": "<p><strong>но</strong> — bu qarshilik: “yangi, <em>lekin</em> "
                       "kichkina”. Bu yerda hech narsa tuzatilmayapti, shuning uchun "
                       "<em>а</em> emas.</p>",
    },
    {
        "text": "<p><strong>Не я здесь</strong> nima degani?</p>",
        "choices": ["Men shu yerda emasman", "Shu yerda men emasman (boshqa odam)",
                    "Men shu yerdaman", "Bu gap notoʻgʻri"],
        "correct": "Shu yerda men emasman (boshqa odam)",
        "explanation": "<p><strong>Не</strong> qayerda tursa — oʻshani inkor qiladi. "
                       "Bu yerda u <em>я</em> ning oldida, demak “men” inkor qilinyapti. "
                       "Solishtiring: <em>Я не здесь</em> = “men shu yerda "
                       "emasman”.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>А</strong> va <strong>но</strong> — farqi nima?</p>",
        "choices": ["А tuzatadi («bu emas, balki u»), но qarshilik bildiradi («lekin»)",
                    "А rasmiy, но norasmiy",
                    "А otlar bilan, но feʼllar bilan", "Farqi yoʻq"],
        "correct": "А tuzatadi («bu emas, balki u»), но qarshilik bildiradi («lekin»)",
        "explanation": "<p><em>Он не студе́нт, <strong>а</strong> учи́тель</em> — "
                       "tuzatish. <em>Шко́ла но́вая, <strong>но</strong> "
                       "ма́ленькая</em> — qarshilik. Ikkalasi ham oʻzbekchaga “lekin” "
                       "deb tarjima qilinadi, lekin ular boshqa ish qiladi.</p>",
    },
    {
        "text": "<p>Oʻzbekcha <strong>emas</strong> va ruscha <strong>не</strong> — "
                "asosiy farq nima?</p>",
        "choices": ["Oʻzbekcha soʻzdan keyin, ruscha soʻzdan oldin turadi",
                    "Oʻzbekcha soʻzdan oldin, ruscha keyin turadi",
                    "Ikkalasi ham gap oxirida", "Farqi yoʻq"],
        "correct": "Oʻzbekcha soʻzdan keyin, ruscha soʻzdan oldin turadi",
        "explanation": "<p><em>bu maktab <strong>emas</strong></em> → <em>э́то "
                       "<strong>не</strong> шко́ла</em>. Har safar “emas” deb "
                       "oʻylaganingizda, uni <strong>oldinga koʻchiring</strong>.</p>",
    },
    {
        "text": "<p><strong>— Э́то не твоя́ ру́чка? — Нет, не моя́.</strong> Javob nimani "
                "bildiradi?</p>",
        "choices": ["Ruchka uniki emas", "Ruchka uniki", "Javob noaniq",
                    "Bu gap notoʻgʻri"],
        "correct": "Ruchka uniki emas",
        "explanation": "<p>Inkor savolga javob berishda rus va oʻzbek tillari "
                       "<strong>bir xil</strong> ishlaydi: “yoʻq” degani “yoʻq, "
                       "emas”. Ingliz tilida bu joy chalkash, sizda esa chalkash "
                       "emas.</p>",
    },
    {
        "text": "<p>Nega <strong>ни … ни …</strong> oʻzbek oʻquvchisi uchun oson?</p>",
        "choices": ["Chunki oʻzbekchada aynan shunday «na … na …» juftligi bor",
                    "Chunki u kam ishlatiladi",
                    "Chunki u faqat yozuvda uchraydi",
                    "Chunki u oʻzgarmaydi"],
        "correct": "Chunki oʻzbekchada aynan shunday «na … na …» juftligi bor",
        "explanation": "<p><em>na bu, na u</em> = <strong>ни э́то, ни то</strong>. "
                       "Ikkala tilda ham juftlik takrorlanadi va ikkala qismni inkor "
                       "qiladi. Tarjima qilishda hech nima oʻzgartirish kerak emas.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Нет, э́то не дом.", "Дом не большо́й.", "Э́то кни́га не.",
                    "Э́то не моя́ кни́га, а её."],
        "correct": "Э́то кни́га не.",
        "explanation": "<p><strong>Не</strong> gap oxiriga qoʻyilmaydi — bu oʻzbekcha "
                       "<em>emas</em> ning taʼsiri. Toʻgʻrisi: <strong>Э́то не "
                       "кни́га.</strong></p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Он не студе́нт, но учи́тель.", "Он не студе́нт, а учи́тель.",
                    "Он нет студе́нт, а учи́тель.", "Он студе́нт не, а учи́тель."],
        "correct": "Он не студе́нт, а учи́тель.",
        "explanation": "<p>Uchta narsa toʻgʻri boʻlishi kerak: <strong>не</strong> "
                       "(<em>нет</em> emas), u <em>студе́нт</em> ning oldida, va "
                       "tuzatishda <strong>а</strong> (<em>но</em> emas).</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Soʻzlarni tartibga soling.</p><p><strong>шко́ла / э́то / "
                "не</strong></p>",
        "choices": ["Э́то не шко́ла.", "Не э́то шко́ла.", "Э́то шко́ла не.",
                    "Шко́ла не э́то."],
        "correct": "Э́то не шко́ла.",
        "explanation": "<p><strong>Э́то не шко́ла.</strong> Tartib har doim bir xil: "
                       "<em>э́то</em> → <em>не</em> → ot.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p><p><strong>— Чай?<br>"
                "— ___, спаси́бо. ___ чай, ___ ко́фе.</strong></p>",
        "choices": ["Нет … Ни … ни", "Не … Ни … ни", "Нет … Не … не", "Ни … Нет … нет"],
        "correct": "Нет … Ни … ни",
        "explanation": "<p><strong>— Нет, спаси́бо. Ни чай, ни ко́фе.</strong> Birinchisi "
                       "savolga javob (<em>нет</em>), keyingisi ikkala narsani birdan "
                       "rad qiladigan juftlik (<em>ни … ни</em>).</p>",
    },
]


# =====================================================================

PRACTICES = [
    {
        "title": "PR-15 Mashq: Savol soʻzlari: кто, что, где, когда, почему, как, какой",
        "description": "20 savol — sakkiz savol soʻzi, где/куда́/отку́да uchligi, "
                       "почему́ va заче́м farqi, savol ohangi.",
        "tutorial": "PR-15:",
        "questions": Q_PR15,
    },
    {
        "title": "PR-16 Mashq: Bu va anavi: этот, эта, это, эти — va «тот»",
        "description": "20 savol — mustaqil э́то va aniqlovchi э́тот farqi, toʻrt shakl, "
                       "тот/та/то/те va вот/здесь/там.",
        "tutorial": "PR-16:",
        "questions": Q_PR16,
    },
    {
        "title": "PR-17 Mashq: Да, нет, не, ни — inkorning toʻrt shakli",
        "description": "20 savol — нет va не farqi, не ning joyi, «не X, а Y» qurilmasi "
                       "va ни … ни juftligi.",
        "tutorial": "PR-17:",
        "questions": Q_PR17,
    },
]
