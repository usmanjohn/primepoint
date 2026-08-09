# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-12 … PR-14.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_12_14.py --master=prime \\
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
# PR-12 — Sifat otga moslashadi
# =====================================================================

Q_PR12 = [
    # 1–5 tanish
    {
        "text": "<p>Sifat nimaga qarab shakl oʻzgartiradi?</p>",
        "choices": ["Otning jinsi va soniga", "Gapdagi oʻrniga", "Urgʻuning joyiga",
                    "Hech nimaga — u oʻzgarmaydi"],
        "correct": "Otning jinsi va soniga",
        "explanation": "<p><strong>но́вый дом / но́вая кни́га / но́вое окно́ / но́вые "
                       "кни́ги</strong>. Bu naqsh siz uchun uchinchi marta: "
                       "<em>он/она́/оно́/они́</em> (PR-8), <em>мой/моя́/моё/мои́</em> "
                       "(PR-10), endi sifat.</p>",
    },
    {
        "text": "<p><strong>кни́га</strong> bilan qaysi shakl ishlatiladi?</p>",
        "choices": ["но́вый", "но́вая", "но́вое", "но́вые"],
        "correct": "но́вая",
        "explanation": "<p><strong>но́вая кни́га</strong>. <em>Кни́га</em> ayol jinsi "
                       "(-а), demak sifatning oxiri <strong>-ая</strong>.</p>",
    },
    {
        "text": "<p><strong>окно́</strong> bilan qaysi shakl ishlatiladi?</p>",
        "choices": ["но́вый", "но́вая", "но́вое", "но́вые"],
        "correct": "но́вое",
        "explanation": "<p><strong>но́вое окно́</strong>. <em>Окно́</em> oʻrta jins (-о), "
                       "demak <strong>-ое</strong>. Bu shakl eng koʻp unutiladi, chunki "
                       "oʻzbekchada uchinchi jins yoʻq.</p>",
    },
    {
        "text": "<p>Sifat gapda qayerda turadi?</p>",
        "choices": ["Otdan oldin — oʻzbekchadagidek", "Otdan keyin — doim",
                    "Gap boshida", "Gap oxirida"],
        "correct": "Otdan oldin — oʻzbekchadagidek",
        "explanation": "<p><em>но́вая шко́ла</em> = <em>yangi maktab</em> — soʻz tartibi "
                       "bir xil. Sifat kesim boʻlganda esa otdan keyin turadi: "
                       "<em>Шко́ла но́вая</em>, va bunda tire qoʻyilmaydi (PR-11).</p>",
    },
    {
        "text": "<p><strong>кни́ги</strong> (koʻplik) bilan qaysi shakl?</p>",
        "choices": ["но́вый", "но́вая", "но́вое", "но́вые"],
        "correct": "но́вые",
        "explanation": "<p><strong>но́вые кни́ги</strong>. Koʻplikda jins yana yoʻqoladi "
                       "(PR-9 dagi <em>они́</em> kabi) — hamma jins uchun bitta shakl "
                       "<strong>-ые</strong>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga: <strong>___ шко́ла</strong> (katta)</p>",
        "choices": ["большо́й", "больша́я", "большо́е", "больши́е"],
        "correct": "больша́я",
        "explanation": "<p><strong>больша́я шко́ла</strong>. <em>Шко́ла</em> ayol jinsi. "
                       "Diqqat: <em>большо́й</em> — urgʻuli oxirli tur, shuning uchun "
                       "uning shakllari <strong>большо́й / больша́я / большо́е / "
                       "больши́е</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>___ язы́к</strong> (rus tili)</p>",
        "choices": ["ру́сскый", "ру́сская", "ру́сский", "ру́сское"],
        "correct": "ру́сский",
        "explanation": "<p><strong>ру́сский язы́к</strong>. Oʻzak <strong>К</strong> bilan "
                       "tugaydi, u esa <strong>Г К Х Ж Ч Ш Щ</strong> roʻyxatida — "
                       "ulardan keyin <strong>-ы</strong> hech qachon yozilmaydi. "
                       "Xuddi shu qoida PR-9 da <em>кни́ги</em> ni tushuntirgan edi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>___ окно́</strong> (yaxshi)</p>",
        "choices": ["хоро́шое", "хоро́шее", "хоро́ший", "хоро́шая"],
        "correct": "хоро́шее",
        "explanation": "<p><strong>хоро́шее окно́</strong>. <strong>Ш</strong> dan keyin "
                       "urgʻusiz <strong>о</strong> <strong>е</strong> ga aylanadi. "
                       "Solishtiring: <em>большо́е</em> da urgʻu oxirda, shuning uchun "
                       "u yerda <strong>о</strong> qoladi.</p>",
    },
    {
        "text": "<p>Savolni tuzing: <strong>___ э́то кни́ги?</strong></p>",
        "choices": ["Како́й", "Кака́я", "Како́е", "Каки́е"],
        "correct": "Каки́е",
        "explanation": "<p><strong>Каки́е э́то кни́ги?</strong> Savol soʻzi ham otga "
                       "moslashadi — xuddi <em>чей/чья/чьё/чьи</em> kabi (PR-10). "
                       "Birlikda: <em>Кака́я э́то кни́га?</em></p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>___ кот</strong> (kichkina)</p>",
        "choices": ["ма́ленькый", "ма́ленькая", "ма́ленький", "ма́ленькое"],
        "correct": "ма́ленький",
        "explanation": "<p><strong>ма́ленький кот</strong>. <em>Кот</em> erkak jinsi, va "
                       "oʻzak <strong>К</strong> bilan tugagani uchun oxiri "
                       "<strong>-ий</strong>, <em>-ый</em> emas.</p>",
    },
    {
        "text": "<p>Ikkita sifatni bogʻlang: <strong>Э́то ___ и ___ шко́ла.</strong> "
                "(katta, yangi)</p>",
        "choices": ["большо́й va но́вый", "больша́я va но́вая", "большо́е va но́вое",
                    "больши́е va но́вые"],
        "correct": "больша́я va но́вая",
        "explanation": "<p><strong>Э́то больша́я и но́вая шко́ла.</strong> Ikkala sifat "
                       "ham bitta otga qaraydi, demak ikkalasi ham ayol shaklida. "
                       "Ularni <strong>и</strong> bilan bogʻlash mumkin.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring: <strong>Bu — qiziqarli kitob.</strong></p>",
        "choices": ["Э́то интере́сный кни́га.", "Э́то интере́сная кни́га.",
                    "Э́то интере́сное кни́га.", "Э́то кни́га интере́сный."],
        "correct": "Э́то интере́сная кни́га.",
        "explanation": "<p><strong>Э́то интере́сная кни́га.</strong> <em>Кни́га</em> ayol "
                       "jinsi, sifat esa otdan oldin turadi — oʻzbekcha bilan bir xil "
                       "tartib.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>но́вая шко́ла</strong> va <strong>шко́ла но́вая</strong> — "
                "farqi nima?</p>",
        "choices": ["Farqi yoʻq", "Birinchisi nomlaydi («yangi maktab»), ikkinchisi "
                    "xabar beradi («maktab yangi»)",
                    "Birinchisi notoʻgʻri", "Ikkinchisi koʻplikda"],
        "correct": "Birinchisi nomlaydi («yangi maktab»), ikkinchisi xabar beradi "
                   "(«maktab yangi»)",
        "explanation": "<p>Ikkalasi ham toʻgʻri, lekin vazifasi boshqa. Sifat oldinda "
                       "boʻlsa — u otni <em>taʼriflaydi</em>. Keyin boʻlsa — u "
                       "<em>kesim</em>, va bunda tire qoʻyilmaydi (PR-11).</p>",
    },
    {
        "text": "<p>Nega <strong>большо́й</strong>, lekin <strong>но́вый</strong>?</p>",
        "choices": ["Bu ikki xil tur, lekin farq faqat urgʻuda",
                    "Chunki большо́й koʻplikda", "Chunki но́вый ayol jinsida",
                    "Chunki большо́й chet soʻz"],
        "correct": "Bu ikki xil tur, lekin farq faqat urgʻuda",
        "explanation": "<p>Urgʻu oxirga tushsa, <strong>-ый</strong> avtomatik "
                       "<strong>-о́й</strong> boʻlib chiqadi: <em>молодо́й, плохо́й, "
                       "дорого́й, большо́й</em>. Bu yangi qoida emas — bu talaffuzning "
                       "imloga taʼsiri.</p>",
    },
    {
        "text": "<p>Oʻzbek va rus sifati orasidagi asosiy farq nima?</p>",
        "choices": ["Oʻzbek sifati oʻzgarmaydi, rus sifati otga moslashadi",
                    "Rus sifati otdan keyin turadi", "Oʻzbek sifati otdan keyin turadi",
                    "Farqi yoʻq"],
        "correct": "Oʻzbek sifati oʻzgarmaydi, rus sifati otga moslashadi",
        "explanation": "<p><em>yangi uy, yangi kitob, yangi derazalar</em> — oʻzbekcha "
                       "<em>yangi</em> qimirlamaydi. Ruschada esa toʻrtta shakl bor. "
                       "Yaxshi xabar: <strong>soʻz tartibi bir xil</strong> — sifat "
                       "ikkala tilda ham otdan oldin turadi.</p>",
    },
    {
        "text": "<p>Qaysi qatorda hamma sifat <strong>oʻrta jins</strong> shaklida?</p>",
        "choices": ["но́вый, большо́й, хоро́ший", "но́вая, больша́я, хоро́шая",
                    "но́вое, большо́е, хоро́шее", "но́вые, больши́е, хоро́шие"],
        "correct": "но́вое, большо́е, хоро́шее",
        "explanation": "<p>Oʻrta jins oxiri <strong>-ое</strong> yoki <strong>-ее</strong>. "
                       "Diqqat: <em>хоро́шее</em> (Ш dan keyin urgʻusiz о → е), lekin "
                       "<em>большо́е</em> (urgʻu oxirda, о qoladi).</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi birikmada xato bor?</p>",
        "choices": ["но́вое сло́во", "больша́я шко́ла", "хоро́шое окно́", "ста́рый го́род"],
        "correct": "хоро́шое окно́",
        "explanation": "<p>Toʻgʻrisi <strong>хоро́шее окно́</strong>. <strong>Ж Ч Ш "
                       "Щ</strong> dan keyin urgʻusiz <strong>о</strong> "
                       "<strong>е</strong> ga aylanadi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Дом — большо́й.", "Дом большо́й.", "Дом большо́е.",
                    "Дом больша́я."],
        "correct": "Дом большо́й.",
        "explanation": "<p><strong>Дом большо́й.</strong> Ikkita narsa birga: "
                       "<em>дом</em> erkak jinsi → <strong>большо́й</strong>, va kesim "
                       "sifat boʻlgani uchun <strong>tire qoʻyilmaydi</strong> "
                       "(PR-11).</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Soʻzlarni tartibga soling.</p><p><strong>кни́га / интере́сная / "
                "э́то</strong></p>",
        "choices": ["Э́то интере́сная кни́га.", "Интере́сная э́то кни́га.",
                    "Э́то кни́га интере́сная.", "Кни́га интере́сная э́то."],
        "correct": "Э́то интере́сная кни́га.",
        "explanation": "<p><strong>Э́то интере́сная кни́га.</strong> Tartib: "
                       "<em>э́то</em> → sifat → ot. (<em>Э́то кни́га интере́сная</em> "
                       "grammatik jihatdan mumkin, lekin bu boshqa maʼno — “bu kitob "
                       "qiziqarli”.)</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p><p><strong>— Кака́я э́то шко́ла?<br>"
                "— Э́то ___ шко́ла.</strong> (yangi)</p>",
        "choices": ["но́вый", "но́вая", "но́вое", "но́вые"],
        "correct": "но́вая",
        "explanation": "<p><strong>но́вая</strong>. Savoldagi <em>Кака́я</em> sizga "
                       "javobning shaklini aytib turibdi: <em>-ая</em> soʻralgan, "
                       "demak <em>-ая</em> javob beriladi. Savol soʻzining shakli — "
                       "bepul yordam.</p>",
    },
]


# =====================================================================
# PR-13 — Sonlar 0–100
# =====================================================================

Q_PR13 = [
    # 1–5 tanish
    {
        "text": "<p><strong>40</strong> ruschada qanday?</p>",
        "choices": ["со́рок", "четы́рдесят", "четы́редцать", "четы́реста"],
        "correct": "со́рок",
        "explanation": "<p><strong>со́рок</strong> — bu istisno, u hech qanday naqshga "
                       "kirmaydi. Ikkinchi shunday istisno — <strong>девяно́сто</strong> "
                       "(90). Ularni alohida yodlash kerak.</p>",
    },
    {
        "text": "<p><strong>во́семь</strong> soʻzida urgʻu qayerda?</p>",
        "choices": ["Birinchi boʻgʻinda", "Ikkinchi boʻgʻinda", "Oxirgi harfda",
                    "Urgʻu yoʻq"],
        "correct": "Birinchi boʻgʻinda",
        "explanation": "<p><strong>во́</strong>семь — urgʻu boshda. Xuddi shunday "
                       "<strong>де́</strong>вять va <strong>де́</strong>сять. Bu uchtasi "
                       "eng koʻp adashtiriladigan urgʻular.</p>",
    },
    {
        "text": "<p><strong>-надцать</strong> qoʻshimchasi nimani bildiradi?</p>",
        "choices": ["“oʻn ustiga”", "“oʻn marta”", "“yuz”", "Hech nimani — bu shunchaki "
                    "oxir"],
        "correct": "“oʻn ustiga”",
        "explanation": "<p><strong>-надцать</strong> — qadimgi <em>“на де́сять”</em>, "
                       "yaʼni “oʻn ustiga”. Shuning uchun <strong>оди́ннадцать</strong> = "
                       "“bir oʻn ustiga”. Oʻzbekcha <em>oʻn bir</em> ham xuddi shu "
                       "mantiq, faqat tartib teskari.</p>",
    },
    {
        "text": "<p>Sonlar orasida qaysi biri jinsga qarab oʻzgaradi?</p>",
        "choices": ["три", "пять", "оди́н", "де́сять"],
        "correct": "оди́н",
        "explanation": "<p>Faqat <strong>оди́н</strong> sifat kabi ishlaydi: "
                       "<strong>оди́н / одна́ / одно́</strong>. (<em>Два</em> da ham "
                       "kichik farq bor — ayol jinsi uchun <em>две</em> — lekin u "
                       "toʻliq uch shaklga ega emas.)</p>",
    },
    {
        "text": "<p><strong>Ско́лько?</strong> nima degani?</p>",
        "choices": ["Nechta? Qancha?", "Qanday?", "Qayerda?", "Kimning?"],
        "correct": "Nechta? Qancha?",
        "explanation": "<p><strong>Ско́лько?</strong> — miqdor soʻraydi. Doʻkonda eng "
                       "kerakli shakli: <strong>Ско́лько сто́ит?</strong> — “qancha "
                       "turadi?”. Bu turgʻun ibora, soʻz tartibi oʻzgarmaydi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga: <strong>___ шко́ла</strong> (bitta)</p>",
        "choices": ["оди́н", "одна́", "одно́", "одни́"],
        "correct": "одна́",
        "explanation": "<p><strong>одна́ шко́ла</strong>. <em>Шко́ла</em> ayol jinsi (-а), "
                       "demak <strong>одна́</strong>. Erkak: <em>оди́н дом</em>; "
                       "oʻrta: <em>одно́ окно́</em>.</p>",
    },
    {
        "text": "<p><strong>два</strong> yoki <strong>две</strong>? "
                "<strong>___ сестры́</strong></p>",
        "choices": ["два", "две", "оба", "двое"],
        "correct": "две",
        "explanation": "<p><strong>две сестры́</strong>. <em>Сестра́</em> ayol jinsi. "
                       "Erkak va oʻrta jins uchun <strong>два</strong>: "
                       "<em>два бра́та, два окна́</em>.</p>",
    },
    {
        "text": "<p><strong>78</strong> ruschada qanday?</p>",
        "choices": ["се́мьдесят во́семь", "семьдеся́т восе́мь", "се́мдесят во́семь",
                    "семна́дцать во́семь"],
        "correct": "се́мьдесят во́семь",
        "explanation": "<p><strong>се́мьдесят во́семь</strong>. Ikkala soʻzda ham urgʻu "
                       "<strong>birinchi</strong> boʻgʻinda — bu 70 va 80 ning oʻziga "
                       "xosligi. Solishtiring: <em>пятьдеся́т</em> (50) da urgʻu "
                       "oxirda.</p>",
    },
    {
        "text": "<p><strong>14</strong> ruschada qanday?</p>",
        "choices": ["четы́ренадцать", "четы́рнадцать", "четы́редцать", "четы́рдцать"],
        "correct": "четы́рнадцать",
        "explanation": "<p><strong>четы́рнадцать</strong> — bitta boʻgʻin tushib qolgan. "
                       "<em>Четы́ре</em> + <em>надцать</em> boʻlishi kerak edi, lekin "
                       "<strong>-е-</strong> yoʻqolgan. Bu 11–20 orasidagi yagona "
                       "gʻalatilik.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>___ окно́</strong> (bitta)</p>",
        "choices": ["оди́н", "одна́", "одно́", "одни́"],
        "correct": "одно́",
        "explanation": "<p><strong>одно́ окно́</strong>. <em>Окно́</em> oʻrta jins (-о), "
                       "demak <strong>одно́</strong> — xuddi <em>но́вое</em>, "
                       "<em>моё</em>, <em>оно́</em> kabi.</p>",
    },
    {
        "text": "<p><strong>35</strong> ruschada qanday?</p>",
        "choices": ["три́дцать пять", "три́дцатьпять", "три пять", "трина́дцать пять"],
        "correct": "три́дцать пять",
        "explanation": "<p><strong>три́дцать пять</strong> — ikkita alohida soʻz, katta "
                       "son avval. Xuddi oʻzbekchadagidek: <em>oʻttiz besh</em>. "
                       "Qoʻshma sonlarda hech qanday hiyla yoʻq.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>два́дцать ___ кни́ги</strong> (2)</p>",
        "choices": ["два", "две", "одна́", "оба"],
        "correct": "две",
        "explanation": "<p><strong>два́дцать две кни́ги</strong>. <em>Два/две</em> farqi "
                       "qoʻshma sonlarda ham saqlanadi: <em>кни́га</em> ayol jinsi, "
                       "demak <strong>две</strong>. Xuddi shunday: "
                       "<em>три́дцать два до́ма</em>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>пятьдеся́т</strong> va <strong>се́мьдесят</strong> — urgʻuda "
                "farq bormi?</p>",
        "choices": ["Yoʻq, ikkalasida ham oxirda",
                    "Ha: пятьдеся́т — oxirda, се́мьдесят — boshda",
                    "Ha: пятьдеся́т — boshda, се́мьдесят — oxirda",
                    "Ikkalasida ham boshda"],
        "correct": "Ha: пятьдеся́т — oxirda, се́мьдесят — boshda",
        "explanation": "<p><strong>пятьдеся́т</strong> (50) va <strong>шестьдеся́т</strong> "
                       "(60) da urgʻu oxirda; <strong>се́мьдесят</strong> (70) va "
                       "<strong>во́семьдесят</strong> (80) da esa boshda. Bu oʻnliklardagi "
                       "yagona nomuvofiqlik.</p>",
    },
    {
        "text": "<p>Rus va oʻzbek sonlari orasidagi asosiy farq nima?</p>",
        "choices": ["Ruschada оди́н jinsga qarab oʻzgaradi va sondan keyin ot shaklini "
                    "oʻzgartiradi",
                    "Oʻzbekchada sonlar oʻzgaradi", "Ruschada sonlar yoʻq",
                    "Farqi yoʻq"],
        "correct": "Ruschada оди́н jinsga qarab oʻzgaradi va sondan keyin ot shaklini "
                   "oʻzgartiradi",
        "explanation": "<p>Oʻzbekchada <em>bir kitob, ikki kitob, besh kitob</em> — ot "
                       "umuman oʻzgarmaydi. Ruschada esa <em>оди́н дом, два до́ма, пять "
                       "домо́в</em>. Toʻliq qoida PR-36 da; hozircha shuni payqab "
                       "qoʻying.</p>",
    },
    {
        "text": "<p>Uch, toʻrt, besh sonlari jinsga qarab oʻzgaradimi?</p>",
        "choices": ["Ha, hammasi", "Faqat уch", "Yoʻq — faqat 1 va 2 da farq bor",
                    "Faqat besh"],
        "correct": "Yoʻq — faqat 1 va 2 da farq bor",
        "explanation": "<p><em>Три кни́ги</em> va <em>три до́ма</em> — bir xil shakl. "
                       "Jins farqi faqat <strong>оди́н/одна́/одно́</strong> va "
                       "<strong>два/две</strong> da bor. Qolgan hamma son "
                       "oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Yoshni aytish uchun qaysi ibora ishlatiladi?</p>",
        "choices": ["Я пятна́дцать лет.", "Мне пятна́дцать лет.",
                    "У меня́ пятна́дцать лет.", "Я есть пятна́дцать."],
        "correct": "Мне пятна́дцать лет.",
        "explanation": "<p><strong>Мне пятна́дцать лет</strong> — soʻzma-soʻz “menga oʻn "
                       "besh yil”. Bu <em>дательный падеж</em> va uni PR-38 da "
                       "oʻrganamiz. Hozircha uni tayyor ibora sifatida yodlang — "
                       "u har kuni kerak.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi birikmada xato bor?</p>",
        "choices": ["одна́ ру́чка", "два до́ма", "оди́н кни́га", "одно́ сло́во"],
        "correct": "оди́н кни́га",
        "explanation": "<p>Toʻgʻrisi <strong>одна́ кни́га</strong>. <em>Кни́га</em> ayol "
                       "jinsi, va <strong>оди́н</strong> sifat kabi otga "
                       "moslashadi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Ско́лько сто́ит тетра́дь?", "Ско́лько тетра́дь сто́ит?",
                    "Сто́ит ско́лько тетра́дь?", "Ско́лько есть тетра́дь?"],
        "correct": "Ско́лько сто́ит тетра́дь?",
        "explanation": "<p><strong>Ско́лько сто́ит …?</strong> — turgʻun ibora, soʻz "
                       "tartibi oʻzgarmaydi. Xuddi <em>Как вас зову́т?</em> kabi "
                       "(PR-7) — uni butunlaligicha yodlang.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p><strong>21</strong> ni ruschada yozing.</p>",
        "choices": ["два́дцать оди́н", "оди́н два́дцать", "два́дцатьоди́н",
                    "два́дцать пе́рвый"],
        "correct": "два́дцать оди́н",
        "explanation": "<p><strong>два́дцать оди́н</strong> — katta son avval, kichigi "
                       "keyin, ikkita alohida soʻz. (<em>Два́дцать пе́рвый</em> — bu "
                       "“yigirma birinchi”, tartib son; u PR-82 da.)</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p><p><strong>— Ско́лько сто́ит ру́чка?<br>"
                "— ___ ты́сячи.</strong> (3)</p>",
        "choices": ["Три", "Тре́тий", "Трина́дцать", "Три́дцать"],
        "correct": "Три",
        "explanation": "<p><strong>Три ты́сячи.</strong> Diqqat: <em>трина́дцать</em> — "
                       "13, <em>три́дцать</em> — 30, <em>тре́тий</em> — “uchinchi”. "
                       "Bu toʻrtta soʻz bir-biriga oʻxshaydi va ularni ajratish "
                       "muhim.</p>",
    },
]


# =====================================================================
# PR-14 — У меня есть
# =====================================================================

Q_PR14 = [
    # 1–5 tanish
    {
        "text": "<p>Rus tilida “ega boʻlmoq” feʼli kundalik nutqda ishlatiladimi?</p>",
        "choices": ["Ha, har doim", "Yoʻq — uning oʻrniga «У меня́ есть …» ishlatiladi",
                    "Faqat savolda", "Faqat oʻtgan zamonda"],
        "correct": "Yoʻq — uning oʻrniga «У меня́ есть …» ishlatiladi",
        "explanation": "<p><strong>У меня́ есть брат</strong> — soʻzma-soʻz “menda aka "
                       "bor”. Oʻzbek tili ham aynan shunday qiladi, shuning uchun bu "
                       "qurilma sizga tanish.</p>",
    },
    {
        "text": "<p>Ruscha <strong>есть</strong> oʻzbekchada qaysi soʻzga toʻgʻri "
                "keladi?</p>",
        "choices": ["bor", "ega", "yeyish", "bu"],
        "correct": "bor",
        "explanation": "<p><strong>есть</strong> = <strong>bor</strong>. "
                       "<em>У меня́ есть брат</em> = <em>Menda aka bor</em>. Shuning "
                       "uchun tekshiruv oddiy: oʻzbekcha tarjimada “bor” soʻzi bormi? "
                       "Bor boʻlsa — <strong>есть</strong> kerak.</p>",
    },
    {
        "text": "<p><strong>она́</strong> uchun egalik shakli qaysi?</p>",
        "choices": ["у его́", "у него́", "у неё", "у них"],
        "correct": "у неё",
        "explanation": "<p><strong>у неё</strong> — ayol egasi uchun. Erkak: "
                       "<strong>у него́</strong>; ular: <strong>у них</strong>.</p>",
    },
    {
        "text": "<p><strong>у него́</strong> qanday oʻqiladi?</p>",
        "choices": ["[у него́]", "[у н'иво́]", "[у эго́]", "[у н'эго́]"],
        "correct": "[у н'иво́]",
        "explanation": "<p><strong>[у н'иво́]</strong> — PR-10 dagi qoida yana ishlayapti: "
                       "<strong>-го</strong> oxiri <strong>[во]</strong> boʻlib "
                       "oʻqiladi. Xuddi <em>его́</em> [йиво́] va <em>сего́дня</em> "
                       "[с'иво́дн'ъ] kabi.</p>",
    },
    {
        "text": "<p><strong>вы</strong> uchun egalik shakli qaysi?</p>",
        "choices": ["у вы", "у вас", "у ваш", "у них"],
        "correct": "у вас",
        "explanation": "<p><strong>у вас</strong> — <em>У вас есть вопро́с?</em> "
                       "(“Savolingiz bormi?”). PR-7 dagidek, <strong>вы</strong> ham "
                       "hurmat, ham koʻplik uchun ishlatiladi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Bu gapni ruschaga oʻgiring: <strong>Mening singlim bor.</strong></p>",
        "choices": ["Я име́ю сестра́.", "У меня́ есть сестра́.", "Мой сестра́ есть.",
                    "У я есть сестра́."],
        "correct": "У меня́ есть сестра́.",
        "explanation": "<p><strong>У меня́ есть сестра́.</strong> Soʻzma-soʻz “menda "
                       "singil bor”. <em>Име́ю</em> juda kitobiy va kundalik nutqda "
                       "ishlatilmaydi; <em>у я</em> esa umuman notoʻgʻri.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>У ___ есть кот.</strong> (uning — erkak "
                "kishi)</p>",
        "choices": ["его́", "него́", "неё", "их"],
        "correct": "него́",
        "explanation": "<p><strong>У него́ есть кот.</strong> <strong>У</strong> "
                       "predlogidan keyin <strong>н-</strong> qoʻshiladi: "
                       "<em>его́ → у него́</em>. Egalik sifatida esa <em>его́ кот</em> "
                       "deb qolaveradi.</p>",
    },
    {
        "text": "<p>Bu gapda <strong>есть</strong> kerakmi? <strong>Э́то ___ на́ша "
                "шко́ла.</strong></p>",
        "choices": ["Ha", "Yoʻq — bu nomlash, mavjudlik emas", "Faqat savolda",
                    "Faqat koʻplikda"],
        "correct": "Yoʻq — bu nomlash, mavjudlik emas",
        "explanation": "<p><strong>Э́то на́ша шко́ла.</strong> Oʻzbekchaga oʻgiring: "
                       "“Bu — bizning maktabimiz”. Bu yerda “bor” soʻzi yoʻq, demak "
                       "<strong>есть</strong> ham kerak emas (PR-6, PR-11).</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>У ___ есть де́ти.</strong> (ularning)</p>",
        "choices": ["их", "них", "неё", "нас"],
        "correct": "них",
        "explanation": "<p><strong>У них есть де́ти.</strong> Yana oʻsha "
                       "<strong>н-</strong>: <em>их → у них</em>. Egalik sifatida esa "
                       "<em>их дом</em>.</p>",
    },
    {
        "text": "<p>Savolni tuzing: <strong>Sening lugʻating bormi?</strong></p>",
        "choices": ["У тебя́ есть слова́рь?", "Ты есть слова́рь?",
                    "У ты есть слова́рь?", "Твой слова́рь есть?"],
        "correct": "У тебя́ есть слова́рь?",
        "explanation": "<p><strong>У тебя́ есть слова́рь?</strong> Savolda soʻz tartibi "
                       "oʻzgarmaydi — faqat ohang koʻtariladi (PR-6). Qisqa javob: "
                       "<em>Да, есть.</em></p>",
    },
    {
        "text": "<p>Bu gapda <strong>есть</strong> kerakmi? <strong>У меня́ ___ но́вая "
                "маши́на.</strong></p>",
        "choices": ["Ha, albatta", "Yoʻq — gap mashinaning qanaqaligida, borligida emas",
                    "Faqat inkorda", "Faqat koʻplikda"],
        "correct": "Yoʻq — gap mashinaning qanaqaligida, borligida emas",
        "explanation": "<p><strong>У меня́ но́вая маши́на</strong> — “mashinam yangi”. "
                       "Mashina borligi allaqachon maʼlum; diqqat markazi "
                       "<em>но́вая</em> da. Solishtiring: <em>У меня́ есть "
                       "маши́на</em> — “mashinam bor”.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>У ___ есть уро́к.</strong> (bizning)</p>",
        "choices": ["мы", "нас", "наш", "нам"],
        "correct": "нас",
        "explanation": "<p><strong>У нас есть уро́к.</strong> <strong>У</strong> dan "
                       "keyin olmosh shaklini oʻzgartiradi: <em>мы → нас</em>. "
                       "Bu shakllarni hozircha tayyor holda yodlang — toʻliq jadval "
                       "PR-41 da.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>его́ кот</strong> va <strong>у него́ есть кот</strong> — nega "
                "biri <em>его́</em>, biri <em>него́</em>?</p>",
        "choices": ["Chunki «у» predlogidan keyin н- qoʻshiladi",
                    "Chunki birinchisi koʻplikda", "Chunki ikkinchisi savol",
                    "Bu xato, ikkalasi bir xil boʻlishi kerak"],
        "correct": "Chunki «у» predlogidan keyin н- qoʻshiladi",
        "explanation": "<p><strong>Н-</strong> faqat predlog bilan paydo boʻladi: "
                       "<em>его́ кот</em> (egalik, PR-10) lekin <em>у <strong>н</strong>его́ "
                       "есть кот</em> (predlog bilan). Xuddi shunday <em>её → у неё</em>, "
                       "<em>их → у них</em>.</p>",
    },
    {
        "text": "<p>PR-6 da «Э́то <s>есть</s> дом» notoʻgʻri edi. Endi <strong>есть</strong> "
                "paydo boʻldi. Qarama-qarshilik bormi?</p>",
        "choices": ["Ha, qoida oʻzgardi",
                    "Yoʻq — bu ikki xil ish: nomlash (есть yoʻq) va mavjudlik (есть bor)",
                    "Ha, PR-6 notoʻgʻri edi",
                    "Yoʻq, chunki есть faqat savolda ishlatiladi"],
        "correct": "Yoʻq — bu ikki xil ish: nomlash (есть yoʻq) va mavjudlik (есть bor)",
        "explanation": "<p><em>Э́то дом</em> — nima ekanini aytyapmiz, demak "
                       "<strong>есть</strong> yoʻq. <em>У меня́ есть дом</em> — bor yoki "
                       "yoʻqligini aytyapmiz, demak <strong>есть</strong> bor. Ikki xil "
                       "maʼno, ikki xil qurilma.</p>",
    },
    {
        "text": "<p>Oʻzbekcha «Menda kitob bor» va ruscha «У меня́ есть кни́га» — "
                "qanchalik oʻxshash?</p>",
        "choices": ["Deyarli soʻz-soʻzga bir xil qurilma",
                    "Umuman boshqa qurilma", "Faqat tarjimada oʻxshash",
                    "Ruschada feʼl bor, oʻzbekchada yoʻq"],
        "correct": "Deyarli soʻz-soʻzga bir xil qurilma",
        "explanation": "<p><em>Menda</em> = <strong>у меня́</strong>, <em>bor</em> = "
                       "<strong>есть</strong>. Ikkala tilda ham “ega boʻlmoq” feʼli "
                       "yoʻq — ikkalasi ham “falon joyda falon narsa bor” deydi. "
                       "Bu Prime Russian kursidagi eng tekin darslardan biri.</p>",
    },
    {
        "text": "<p>«Vaqtim yoʻq» ruschada qanday?</p>",
        "choices": ["У меня́ нет вре́мя.", "У меня́ не вре́мя.",
                    "У меня́ нет вре́мени.", "Я нет вре́мя."],
        "correct": "У меня́ нет вре́мени.",
        "explanation": "<p><strong>У меня́ нет вре́мени.</strong> Inkor shakli yangi "
                       "kelishikni (родительный падеж) talab qiladi — uni PR-34 da "
                       "oʻrganamiz. Hozircha bu iborani va <em>У меня́ нет "
                       "де́нег</em> ni tayyor holda yodlang.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["У меня́ есть брат.", "У неё есть кот.", "У его́ есть маши́на.",
                    "У нас есть уро́к."],
        "correct": "У его́ есть маши́на.",
        "explanation": "<p>Toʻgʻrisi <strong>У него́ есть маши́на</strong>. "
                       "<strong>У</strong> predlogidan keyin <strong>н-</strong> "
                       "qoʻshiladi. Bu eng koʻp uchraydigan xato, chunki egalik "
                       "shaklida (<em>его́ маши́на</em>) н- yoʻq.</p>",
    },
    {
        "text": "<p>Qaysi gapda <strong>есть</strong> ortiqcha?</p>",
        "choices": ["У нас есть уро́к.", "Э́то есть но́вая шко́ла.",
                    "У вас есть вопро́с?", "Здесь есть библиоте́ка."],
        "correct": "Э́то есть но́вая шко́ла.",
        "explanation": "<p>Toʻgʻrisi <strong>Э́то но́вая шко́ла</strong> — bu nomlash. "
                       "Qolgan uchtasida “bor” maʼnosi bor: <em>darsimiz bor, "
                       "savolingiz bormi, bu yerda kutubxona bor</em>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Soʻzlarni tartibga soling.</p><p><strong>есть / у / брат / "
                "меня́</strong></p>",
        "choices": ["У меня́ есть брат.", "Есть у меня́ брат.", "У брат меня́ есть.",
                    "Меня́ у есть брат."],
        "correct": "У меня́ есть брат.",
        "explanation": "<p><strong>У меня́ есть брат.</strong> Qolip qatʼiy: "
                       "<em>у</em> → olmosh → <em>есть</em> → narsa.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p><p><strong>— У тебя́ есть слова́рь?<br>"
                "— Да, ___. А у ___?</strong> (sizda-chi)</p>",
        "choices": ["есть … вас", "есть … вы", "име́ю … вас", "есть … ваш"],
        "correct": "есть … вас",
        "explanation": "<p><strong>— Да, есть. А у вас?</strong> Qisqa javobda otni "
                       "takrorlash shart emas — xuddi oʻzbekchadagi “Ha, bor” kabi. "
                       "Savolni qaytarishda esa <em>у вас?</em> ishlatiladi.</p>",
    },
]


# =====================================================================

PRACTICES = [
    {
        "title": "PR-12 Mashq: Sifat otga moslashadi — новый, новая, новое, новые",
        "description": "20 savol — sifatning toʻrt shakli, -ый / -о́й / -ий turlari, "
                       "Г К Х Ж Ч Ш Щ qoidasi va како́й? savoli.",
        "tutorial": "PR-12:",
        "questions": Q_PR12,
    },
    {
        "title": "PR-13 Mashq: Sonlar 0–100 va «сколько?»",
        "description": "20 savol — 0 dan 100 gacha, оди́н/одна́/одно́, два va две farqi, "
                       "istisnolar (со́рок, девяно́сто) va urgʻu.",
        "tutorial": "PR-13:",
        "questions": Q_PR13,
    },
    {
        "title": "PR-14 Mashq: У меня есть — rus tilida egalik",
        "description": "20 savol — «У меня́ есть …» qolipi, yettita shakl, «у» dan keyingi "
                       "н-, va есть qachon kerak.",
        "tutorial": "PR-14:",
        "questions": Q_PR14,
    },
]
