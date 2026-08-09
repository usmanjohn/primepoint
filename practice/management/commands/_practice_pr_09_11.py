# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-9 … PR-11.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_09_11.py --master=prime \\
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
# PR-9 — Koʻplik
# =====================================================================

Q_PR9 = [
    # 1–5 tanish
    {
        "text": "<p><strong>стол</strong> ning koʻpligi qaysi?</p>",
        "choices": ["столы́", "стола́", "сто́ли", "столя́"],
        "correct": "столы́",
        "explanation": "<p><strong>столы́</strong>. Erkak jinsi, undosh bilan tugagan → "
                       "<strong>-ы</strong>. Diqqat: urgʻu oxirga koʻchdi — "
                       "<em>стол → сто<strong>лы́</strong></em>.</p>",
    },
    {
        "text": "<p><strong>шко́ла</strong> ning koʻpligi qaysi?</p>",
        "choices": ["шко́ли", "шко́лы", "шко́ла́", "шко́лья"],
        "correct": "шко́лы",
        "explanation": "<p><strong>шко́лы</strong>. Ayol jinsi, <strong>-а</strong> "
                       "<strong>-ы</strong> ga almashadi. Oxirgi undosh <em>л</em> "
                       "yettita harf roʻyxatida yoʻq, shuning uchun imlo qoidasi bu "
                       "yerda ishlamaydi.</p>",
    },
    {
        "text": "<p><strong>окно́</strong> ning koʻpligi qaysi?</p>",
        "choices": ["окны́", "о́кни", "о́кна", "окна́"],
        "correct": "о́кна",
        "explanation": "<p><strong>о́кна</strong>. Oʻrta jins <strong>-о</strong> ni "
                       "<strong>-а</strong> ga almashtiradi. Va urgʻu koʻchdi: birlikda "
                       "окн<strong>о́</strong>, koʻplikda <strong>о́</strong>кна.</p>",
    },
    {
        "text": "<p>Koʻplikdagi ot qaysi olmosh bilan almashtiriladi?</p>",
        "choices": ["он", "она́", "оно́", "они́"],
        "correct": "они́",
        "explanation": "<p><strong>они́</strong> — jinsdan qatʼi nazar. Koʻplikda jins "
                       "yoʻqoladi: <em>столы́ — они́, кни́ги — они́, о́кна — они́</em>. "
                       "Bu rus tilidagi yoqimli yengilliklardan biri.</p>",
    },
    {
        "text": "<p>Qaysi yettita harfdan keyin <strong>-ы</strong> hech qachon "
                "yozilmaydi?</p>",
        "choices": ["Б В Г Д Ж З К", "Г К Х Ж Ч Ш Щ", "Л М Н Р Й Ц Ф",
                    "П Т С Ф Х Ц Ч"],
        "correct": "Г К Х Ж Ч Ш Щ",
        "explanation": "<p><strong>Г К Х Ж Ч Ш Щ</strong>. Ulardan keyin har doim "
                       "<strong>-и</strong> keladi: <em>кни́ги, ру́чки, врачи́</em>. "
                       "Xuddi shu roʻyxat PR-4 dagi <em>жи-ши</em> qoidasining "
                       "orqasida ham turadi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>кни́га → ___</strong></p>",
        "choices": ["кни́гы", "кни́ги", "кни́га́", "кни́гья"],
        "correct": "кни́ги",
        "explanation": "<p><strong>кни́ги</strong>. Soʻz <strong>Г</strong> bilan "
                       "tugaydi, u esa yettita harf roʻyxatida — demak "
                       "<strong>-ы</strong> emas, <strong>-и</strong>.</p>",
    },
    {
        "text": "<p><strong>врач</strong> ning koʻpligi?</p>",
        "choices": ["врачы́", "врача́", "врачи́", "вра́чья"],
        "correct": "врачи́",
        "explanation": "<p><strong>врачи́</strong>. <strong>Ч</strong> yettita harf "
                       "roʻyxatida, shuning uchun <strong>-и</strong>. Urgʻu ham oxirga "
                       "koʻchdi.</p>",
    },
    {
        "text": "<p><strong>мо́ре</strong> ning koʻpligi?</p>",
        "choices": ["моря́", "мо́ры", "мо́реи", "мо́ри"],
        "correct": "моря́",
        "explanation": "<p><strong>моря́</strong>. Oʻrta jinsdagi <strong>-е</strong> "
                       "<strong>-я</strong> ga almashadi. Xuddi shunday: "
                       "<em>зда́ние → зда́ния</em>, <em>по́ле → поля́</em>.</p>",
    },
    {
        "text": "<p><strong>челове́к</strong> ning koʻpligi?</p>",
        "choices": ["челове́ки", "челове́ка", "лю́ди", "челове́чи"],
        "correct": "лю́ди",
        "explanation": "<p><strong>лю́ди</strong> — bu istisno, butunlay boshqa soʻz. "
                       "<em>Челове́ки</em> degan shakl yoʻq. Xuddi shunday "
                       "<em>ребёнок → де́ти</em>.</p>",
    },
    {
        "text": "<p><strong>друг</strong> ning koʻpligi?</p>",
        "choices": ["дру́ги", "друзья́", "друга́", "дру́гы"],
        "correct": "друзья́",
        "explanation": "<p><strong>друзья́</strong> — <strong>-ья</strong> guruhidan. "
                       "Bu guruhda yana: <em>брат → бра́тья</em>, "
                       "<em>сын → сыновья́</em>, <em>стул → сту́лья</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Где кни́ги? — ___ "
                "здесь.</strong></p>",
        "choices": ["Он", "Она́", "Оно́", "Они́"],
        "correct": "Они́",
        "explanation": "<p><strong>Они́</strong>. <em>Кни́ги</em> koʻplikda, va koʻplikda "
                       "har doim <strong>они́</strong> — <em>кни́га</em> ayol jinsida "
                       "boʻlsa ham, bu endi ahamiyatsiz.</p>",
    },
    {
        "text": "<p><strong>дверь</strong> ning koʻpligi?</p>",
        "choices": ["две́ри", "две́ры", "двера́", "две́рья"],
        "correct": "две́ри",
        "explanation": "<p><strong>две́ри</strong>. <strong>-ь</strong> bilan tugagan ot "
                       "koʻplikda <strong>-и</strong> oladi — jinsi erkak boʻlsa ham, "
                       "ayol boʻlsa ham: <em>дверь → две́ри</em>, "
                       "<em>слова́рь → словари́</em>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>дома́</strong> va <strong>до́ма</strong> — farqi nima?</p>",
        "choices": ["Farqi yoʻq", "дома́ = uylar, до́ма = uyda — urgʻu ajratadi",
                    "дома́ = uyda, до́ма = uylar", "Ikkinchisi eskirgan shakl"],
        "correct": "дома́ = uylar, до́ма = uyda — urgʻu ajratadi",
        "explanation": "<p><strong>дома́</strong> — <em>дом</em> ning koʻpligi (uylar). "
                       "<strong>до́ма</strong> — “uyda”. <em>Здесь дома́</em> = bu yerda "
                       "uylar; <em>Я до́ма</em> = men uydaman. PR-5 dagi "
                       "<em>за́мок / замо́к</em> kabi — urgʻu maʼno tashiydi.</p>",
    },
    {
        "text": "<p>Qaysi qatorda hamma ot <strong>faqat koʻplikda</strong> "
                "yashaydi?</p>",
        "choices": ["столы́, кни́ги, о́кна", "де́ньги, часы́, очки́",
                    "друзья́, бра́тья, сту́лья", "лю́ди, де́ти, ма́тери"],
        "correct": "де́ньги, часы́, очки́",
        "explanation": "<p><strong>де́ньги</strong> (pul), <strong>часы́</strong> (soat), "
                       "<strong>очки́</strong> (koʻzoynak) — bularning birligi umuman "
                       "yoʻq. Yana: <em>роди́тели, кани́кулы, но́жницы</em>. Qolgan "
                       "qatorlarning hammasida birlik shakli bor.</p>",
    },
    {
        "text": "<p>Nima uchun <strong>го́род → города́</strong>, <strong>го́роды</strong> "
                "emas?</p>",
        "choices": ["Chunki у erkak jinsining urgʻuli -а́ roʻyxatidan",
                    "Chunki у Д bilan tugaydi", "Chunki bu oʻrta jins",
                    "Chunki bu chet soʻz"],
        "correct": "Chunki у erkak jinsining urgʻuli -а́ roʻyxatidan",
        "explanation": "<p>Bir guruh erkak jinsdagi ot <strong>-ы</strong> emas, urgʻuli "
                       "<strong>-а́</strong> oladi: <em>дома́, города́, поезда́, "
                       "паспорта́, учителя́, доктора́, глаза́</em>. Bu roʻyxat "
                       "yodlanadi.</p>",
    },
    {
        "text": "<p>Oʻzbekcha <strong>-lar</strong> va rus koʻpligi orasidagi asosiy "
                "farq nima?</p>",
        "choices": ["Oʻzbekchada bitta qoʻshimcha, ruschada qoʻshimcha jinsga va "
                    "oxirgi harfga bogʻliq",
                    "Ruschada koʻplik umuman yoʻq",
                    "Oʻzbekchada qoʻshimcha soʻz oldida turadi",
                    "Farqi yoʻq"],
        "correct": "Oʻzbekchada bitta qoʻshimcha, ruschada qoʻshimcha jinsga va "
                   "oxirgi harfga bogʻliq",
        "explanation": "<p>Oʻzbekchada <em>-lar</em> hamma narsaga qoʻshiladi. Ruschada "
                       "esa asosan ikkita qoʻshimcha bor: <strong>-ы/-и</strong> (erkak "
                       "va ayol) va <strong>-а/-я</strong> (oʻrta jins + qisqa roʻyxat). "
                       "Yaʼni ikkita narsa, oʻn ikkita emas.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi soʻzda xato bor?</p>",
        "choices": ["столы́", "кни́гы", "о́кна", "две́ри"],
        "correct": "кни́гы",
        "explanation": "<p>Toʻgʻrisi <strong>кни́ги</strong>. <strong>Г</strong> dan keyin "
                       "<strong>-ы</strong> hech qachon yozilmaydi. Bu Prime Russian "
                       "oʻquvchisining eng koʻp uchraydigan imlo xatosi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Где о́кна? — Оно́ здесь.", "Где о́кна? — Она́ здесь.",
                    "Где о́кна? — Они́ здесь.", "Где о́кна? — Он здесь."],
        "correct": "Где о́кна? — Они́ здесь.",
        "explanation": "<p><strong>Они́</strong>. <em>О́кна</em> — koʻplik, demak "
                       "<strong>они́</strong>. <em>Оно́</em> faqat birlikdagi oʻrta jins "
                       "uchun: <em>окно́ — оно́</em>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Bu gapni koʻplikka oʻgiring.</p><p><strong>Э́то кни́га.</strong></p>",
        "choices": ["Э́то кни́ги.", "Э́то кни́гы.", "Э́ти кни́ги.", "Э́то кни́га́."],
        "correct": "Э́то кни́ги.",
        "explanation": "<p><strong>Э́то кни́ги.</strong> Diqqat: <em>э́то</em> "
                       "<strong>oʻzgarmaydi</strong> — u koʻplikda ham <em>э́то</em> "
                       "boʻlib qolaveradi (PR-6). Oʻzgargani faqat ot.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p><p><strong>— Кто э́то?<br>"
                "— Э́то ___. Дилно́за, Жасу́р и Шербе́к.</strong></p>",
        "choices": ["мои́ друзья́", "мои́ дру́ги", "мой друзья́", "моя́ друзья́"],
        "correct": "мои́ друзья́",
        "explanation": "<p><strong>мои́ друзья́</strong>. Ikkita narsa birga ishladi: "
                       "<em>друг</em> ning koʻpligi istisno — <strong>друзья́</strong>, "
                       "va koʻplikdagi ot bilan egalik <strong>мои́</strong> shaklini "
                       "oladi (PR-10).</p>",
    },
]


# =====================================================================
# PR-10 — Olmoshlar va egalik
# =====================================================================

Q_PR10 = [
    # 1–5 tanish
    {
        "text": "<p>Rus tilida nechta shaxs olmoshi bor?</p>",
        "choices": ["Oltita", "Sakkizta", "Uchta", "Toʻrtta"],
        "correct": "Sakkizta",
        "explanation": "<p>Sakkizta: <strong>я, ты, он, она́, оно́, мы, вы, они́</strong>. "
                       "Oʻzbekchadan farqi — uchinchi shaxs birlikda uchta shakl bor "
                       "(он/она́/оно́), oʻzbekchada esa bitta “u”.</p>",
    },
    {
        "text": "<p><strong>мой</strong> soʻzi nimaga qarab oʻzgaradi?</p>",
        "choices": ["Egalik qilingan narsaning jinsiga", "Eganing jinsiga",
                    "Gapdagi oʻrniga", "Hech nimaga — u oʻzgarmaydi"],
        "correct": "Egalik qilingan narsaning jinsiga",
        "explanation": "<p>Bu darsning asosiy gʻoyasi. <em>Мой брат</em>, lekin "
                       "<em>моя́ сестра́</em> — “men” oʻzgarmadim, oʻzgargani "
                       "<strong>ot</strong>. Oʻzbekchada esa qoʻshimcha aynan egani "
                       "koʻrsatadi (<em>kitobim, kitobing</em>) — bu teskari tizim.</p>",
    },
    {
        "text": "<p><strong>его́</strong> qanday oʻqiladi?</p>",
        "choices": ["[эго́]", "[йиго́]", "[йиво́]", "[йего́]"],
        "correct": "[йиво́]",
        "explanation": "<p><strong>[йиво́]</strong>. Ikkita narsa boʻldi: "
                       "<strong>-го</strong> oxiri <strong>[во]</strong> boʻlib oʻqiladi, "
                       "va urgʻusiz <em>е</em> [и] ga qisqardi (иканье). Xuddi shunday: "
                       "<em>сего́дня</em> [с'иво́дн'ъ].</p>",
    },
    {
        "text": "<p><strong>кни́га</strong> bilan qaysi egalik shakli ishlatiladi?</p>",
        "choices": ["мой", "моя́", "моё", "мои́"],
        "correct": "моя́",
        "explanation": "<p><strong>моя́ кни́га</strong>. <em>Кни́га</em> ayol jinsi (-а), "
                       "demak egalik ham ayol shaklida. Naqsh: "
                       "<strong>мой / моя́ / моё / мои́</strong>.</p>",
    },
    {
        "text": "<p><strong>их</strong> soʻzi nechta shaklga ega?</p>",
        "choices": ["Bitta — u hech qachon oʻzgarmaydi", "Ikkita", "Uchta", "Toʻrtta"],
        "correct": "Bitta — u hech qachon oʻzgarmaydi",
        "explanation": "<p><strong>его́, её, их</strong> — uchalasi ham oʻzgarmaydi: "
                       "<em>их дом, их кни́га, их окно́, их друзья́</em>. Bu darsning eng "
                       "oson qismi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ шко́ла</strong> "
                "(bizning)</p>",
        "choices": ["наш", "на́ша", "на́ше", "на́ши"],
        "correct": "на́ша",
        "explanation": "<p><strong>на́ша шко́ла</strong>. <em>Шко́ла</em> ayol jinsi. "
                       "Naqsh <em>мой</em> bilan bir xil: "
                       "<strong>наш / на́ша / на́ше / на́ши</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ окно́</strong> "
                "(mening)</p>",
        "choices": ["мой", "моя́", "моё", "мои́"],
        "correct": "моё",
        "explanation": "<p><strong>моё окно́</strong>. <em>Окно́</em> oʻrta jins (-о), "
                       "demak <strong>моё</strong>. Bu shakl eng koʻp unutiladi, chunki "
                       "oʻzbekchada uchinchi jins yoʻq.</p>",
    },
    {
        "text": "<p>Savolni tuzing.</p><p><strong>___ э́то тетра́дь?</strong></p>",
        "choices": ["Чей", "Чья", "Чьё", "Чьи"],
        "correct": "Чья",
        "explanation": "<p><strong>Чья э́то тетра́дь?</strong> <em>Тетра́дь</em> — "
                       "<strong>-ь</strong> bilan tugagan ayol jinsidagi ot (PR-8), "
                       "shuning uchun <strong>чья</strong>. Savol soʻzi ham otga "
                       "moslashadi.</p>",
    },
    {
        "text": "<p>Savolni tuzing.</p><p><strong>___ э́то кни́ги?</strong></p>",
        "choices": ["Чей", "Чья", "Чьё", "Чьи"],
        "correct": "Чьи",
        "explanation": "<p><strong>Чьи э́то кни́ги?</strong> <em>Кни́ги</em> koʻplikda, "
                       "demak <strong>чьи</strong>. Birlikda boʻlsa edi: "
                       "<em>Чья э́то кни́га?</em></p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi? (Dilnozaning kitobi)</p>"
                "<p><strong>Э́то ___ кни́га.</strong></p>",
        "choices": ["его́", "её", "их", "ея́"],
        "correct": "её",
        "explanation": "<p><strong>её кни́га</strong>. Ega — Dilnoza, yaʼni ayol kishi, "
                       "shuning uchun <strong>её</strong>. Diqqat: <em>кни́га</em> ham "
                       "ayol jinsida, lekin bu ahamiyatsiz — <strong>её</strong> "
                       "baribir oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ друзья́</strong> "
                "(sening)</p>",
        "choices": ["твой", "твоя́", "твоё", "твои́"],
        "correct": "твои́",
        "explanation": "<p><strong>твои́ друзья́</strong>. <em>Друзья́</em> koʻplikda "
                       "(<em>друг</em> ning istisno koʻpligi, PR-9), demak koʻplik "
                       "shakli <strong>твои́</strong>.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Bu mening akam.</strong></p>",
        "choices": ["Э́то моя́ брат.", "Э́то мой брат.", "Э́то моё брат.",
                    "Э́то брат мой."],
        "correct": "Э́то мой брат.",
        "explanation": "<p><strong>Э́то мой брат.</strong> <em>Брат</em> undosh bilan "
                       "tugaydi — erkak jinsi, demak <strong>мой</strong>. Egalik soʻzi "
                       "har doim otning <strong>oldida</strong> turadi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Nega <strong>мой брат</strong>, lekin <strong>моя́ сестра́</strong>?</p>",
        "choices": ["Chunki ega oʻzgardi", "Chunki ot oʻzgardi: брат — m., сестра́ — f.",
                    "Chunki сестра́ koʻplikda", "Chunki bu ikki xil odam"],
        "correct": "Chunki ot oʻzgardi: брат — m., сестра́ — f.",
        "explanation": "<p>Ega (“men”) oʻzgarmadi. Egalik soʻzi <strong>egalik qilingan "
                       "narsaga</strong> moslashadi — bu oʻzbekchaning aynan teskarisi, "
                       "chunki oʻzbekcha <em>-im</em> qoʻshimchasi egani koʻrsatadi.</p>",
    },
    {
        "text": "<p>Qaysi guruh <strong>hech qachon oʻzgarmaydi</strong>?</p>",
        "choices": ["мой, твой, наш", "его́, её, их", "чей, чья, чьё", "он, она́, оно́"],
        "correct": "его́, её, их",
        "explanation": "<p><strong>его́, её, их</strong> — bu uchtasining umuman shakli "
                       "yoʻq. Qolgan guruhlarning hammasi otning jinsiga qarab "
                       "oʻzgaradi.</p>",
    },
    {
        "text": "<p><strong>вы</strong> olmoshi nechta vazifada ishlatiladi?</p>",
        "choices": ["Bitta — hurmat", "Bitta — koʻplik", "Ikkita — hurmat va koʻplik",
                    "Uchta"],
        "correct": "Ikkita — hurmat va koʻplik",
        "explanation": "<p>PR-7 dagi qoida: <strong>вы</strong> bitta odamga hurmat "
                       "bilan (<em>siz</em>) ham, bir nechta odamga (<em>sizlar</em>) "
                       "ham murojaat. Egalik shakli ikkalasida ham "
                       "<strong>ваш / ва́ша / ва́ше / ва́ши</strong>.</p>",
    },
    {
        "text": "<p>Qaysi soʻzda <strong>-го</strong> oxiri <strong>[во]</strong> boʻlib "
                "oʻqiladi?</p>",
        "choices": ["его́ va сего́дня", "мой va моя́", "их va её", "наш va ваш"],
        "correct": "его́ va сего́дня",
        "explanation": "<p><strong>его́</strong> [йиво́] va <strong>сего́дня</strong> "
                       "[с'иво́дн'ъ]. Bu qoida keyinchalik hamma "
                       "<em>-ого / -его</em> oxirida ishlaydi (PR-43). Hozircha: "
                       "<strong>-го</strong> koʻrsangiz, <strong>[во]</strong> deng.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Э́то мой брат.", "Э́то моя́ сестра́.", "Э́то мой сестра́.",
                    "Э́то моё окно́."],
        "correct": "Э́то мой сестра́.",
        "explanation": "<p>Toʻgʻrisi <strong>моя́ сестра́</strong>. <em>Сестра́</em> ayol "
                       "jinsida (-а), shuning uchun egalik ham ayol shaklida boʻlishi "
                       "kerak. Bu oʻzbek oʻquvchisining eng koʻp uchraydigan xatosi, "
                       "chunki oʻzbekchada egalik jinsga umuman bogʻliq emas.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Э́то её дом.", "Э́то ея́ дом.", "Э́то ей дом.", "Э́то её́я дом."],
        "correct": "Э́то её дом.",
        "explanation": "<p><strong>Э́то её дом.</strong> <em>Её</em> hech qachon "
                       "oʻzgarmaydi — <em>её дом, её кни́га, её окно́, её друзья́</em>. "
                       "Unga qoʻshimcha qoʻshishga urinish keng tarqalgan xato.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Soʻzlarni tartibga soling.</p><p><strong>телефо́н / э́то / мой / "
                "не</strong></p>",
        "choices": ["Э́то не мой телефо́н.", "Э́то мой не телефо́н.",
                    "Не э́то мой телефо́н.", "Э́то мой телефо́н не."],
        "correct": "Э́то не мой телефо́н.",
        "explanation": "<p><strong>Э́то не мой телефо́н.</strong> <em>Не</em> inkor "
                       "qilinayotgan qismning oldida turadi (PR-6), egalik esa otning "
                       "oldida. Tartib: <em>э́то → не → мой → ot</em>.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p><p><strong>— Чья э́то тетра́дь?<br>"
                "— ___ Спаси́бо!</strong></p>",
        "choices": ["Мой!", "Моя́!", "Моё!", "Мои́!"],
        "correct": "Моя́!",
        "explanation": "<p><strong>Моя́!</strong> Savolda <em>чья</em> ishlatilgan, demak "
                       "ot ayol jinsida (<em>тетра́дь</em>), va javob ham ayol shaklida "
                       "boʻladi. Savol soʻzining shakli sizga javobning shaklini "
                       "aytib turadi.</p>",
    },
]


# =====================================================================
# PR-11 — Feʼlsiz gaplar va tire
# =====================================================================

Q_PR11 = [
    # 1–5 tanish
    {
        "text": "<p>Rus tilida hozirgi zamonda “boʻlmoq” feʼli qoʻyiladimi?</p>",
        "choices": ["Ha, har doim", "Yoʻq — hech qachon", "Faqat otlar bilan",
                    "Faqat savolda"],
        "correct": "Yoʻq — hech qachon",
        "explanation": "<p>Hozirgi zamonda u <strong>hech qachon</strong> qoʻyilmaydi — "
                       "faqat <em>это</em> bilan emas, hamma gapda: <em>Я студе́нт. "
                       "Он врач. Мы до́ма.</em> Oʻtgan va kelasi zamonda esa qaytib "
                       "keladi.</p>",
    },
    {
        "text": "<p>Tire (—) qachon qoʻyiladi?</p>",
        "choices": ["Ikkala tomon ham ot boʻlganda", "Ega olmosh boʻlganda",
                    "Kesim sifat boʻlganda", "Har doim"],
        "correct": "Ikkala tomon ham ot boʻlganda",
        "explanation": "<p><strong>Ot + ot = tire</strong>: <em>Москва́ — столи́ца. "
                       "Мой брат — врач.</em> Ega olmosh boʻlsa yoki kesim sifat/ravish "
                       "boʻlsa — tire qoʻyilmaydi.</p>",
    },
    {
        "text": "<p><strong>шко́ла</strong> bilan oʻtgan zamonda qaysi shakl "
                "ishlatiladi?</p>",
        "choices": ["был", "была́", "бы́ло", "бы́ли"],
        "correct": "была́",
        "explanation": "<p><strong>была́</strong> — <em>шко́ла</em> ayol jinsi (-а). "
                       "Toʻliq uchlik: <strong>был</strong> (m.) / "
                       "<strong>была́</strong> (f.) / <strong>бы́ло</strong> (oʻrta) / "
                       "<strong>бы́ли</strong> (koʻplik).</p>",
    },
    {
        "text": "<p>Kelasi zamonda nechta shakl bor?</p>",
        "choices": ["Ikkita — бу́дет va бу́дут", "Toʻrtta, jinsga qarab", "Bitta",
                    "Uchta"],
        "correct": "Ikkita — бу́дет va бу́дут",
        "explanation": "<p><strong>бу́дет</strong> (birlik) va <strong>бу́дут</strong> "
                       "(koʻplik). Jins bu yerda ahamiyatsiz, shuning uchun kelasi zamon "
                       "oʻtgan zamondan osonroq.</p>",
    },
    {
        "text": "<p><strong>ко́фе</strong> qaysi jinsda?</p>",
        "choices": ["Oʻrta — chunki -е bilan tugaydi", "Erkak — bu istisno",
                    "Ayol", "Jinsi yoʻq"],
        "correct": "Erkak — bu istisno",
        "explanation": "<p><strong>Erkak jinsida</strong>: <em>ко́фе горя́чий</em>, "
                       "<em>горя́чее</em> emas. PR-8 qoidasiga koʻra <strong>-е</strong> "
                       "oʻrta jins boʻlishi kerak edi, lekin bu chet tildan kirgan "
                       "soʻzning istisnosi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Tire kerakmi?</p><p><strong>Мой брат ___ врач.</strong></p>",
        "choices": ["Ha — «Мой брат — врач»", "Yoʻq", "Faqat savolda",
                    "Faqat oʻtgan zamonda"],
        "correct": "Ha — «Мой брат — врач»",
        "explanation": "<p>Ikkala tomon ham ot (<em>брат</em> va <em>врач</em>), demak "
                       "tire qoʻyiladi. Solishtiring: <em>Он врач</em> — bu yerda ega "
                       "olmosh, shuning uchun tire yoʻq.</p>",
    },
    {
        "text": "<p>Tire kerakmi?</p><p><strong>Дом ___ большо́й.</strong></p>",
        "choices": ["Ha", "Yoʻq — kesim sifat", "Faqat koʻplikda", "Faqat yozuvda"],
        "correct": "Yoʻq — kesim sifat",
        "explanation": "<p><strong>Дом большо́й.</strong> Kesim sifat "
                       "(<em>большо́й</em>), ot emas — shuning uchun tire hech qachon "
                       "qoʻyilmaydi. Xuddi shunday: <em>Ко́фе горя́чий.</em></p>",
    },
    {
        "text": "<p>Tire kerakmi?</p><p><strong>Я ___ студе́нт.</strong></p>",
        "choices": ["Ha", "Yoʻq — ega olmosh", "Faqat ayol kishi haqida",
                    "Faqat koʻplikda"],
        "correct": "Yoʻq — ega olmosh",
        "explanation": "<p><strong>Я студе́нт.</strong> Ega olmosh boʻlsa, tire "
                       "qoʻyilmaydi. (Kuchli taʼkid uchun <em>«Я — учи́тель!»</em> "
                       "deyish mumkin, lekin oddiy gapda bunday yozilmaydi.)</p>",
    },
    {
        "text": "<p>Oʻtgan zamonga oʻgiring.</p><p><strong>Окно́ здесь.</strong></p>",
        "choices": ["Окно́ был здесь.", "Окно́ была́ здесь.", "Окно́ бы́ло здесь.",
                    "Окно́ бы́ли здесь."],
        "correct": "Окно́ бы́ло здесь.",
        "explanation": "<p><strong>Окно́ бы́ло здесь.</strong> <em>Окно́</em> — oʻrta "
                       "jins (-о), demak <strong>бы́ло</strong>. Bu shakl eng koʻp "
                       "unutiladi, chunki oʻzbekcha <em>edi</em> jinsga qarab "
                       "oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Kelasi zamonga oʻgiring.</p><p><strong>Здесь уро́ки.</strong></p>",
        "choices": ["Здесь бу́дет уро́ки.", "Здесь бу́дут уро́ки.",
                    "Здесь бы́ли уро́ки.", "Здесь есть уро́ки."],
        "correct": "Здесь бу́дут уро́ки.",
        "explanation": "<p><strong>бу́дут</strong> — <em>уро́ки</em> koʻplikda. Birlikda "
                       "boʻlsa edi: <em>Здесь бу́дет уро́к.</em></p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Toshkent — "
                "poytaxt.</strong></p>",
        "choices": ["Ташке́нт есть столи́ца.", "Ташке́нт — столи́ца.",
                    "Ташке́нт столи́ца есть.", "Ташке́нт э́то есть столи́ца."],
        "correct": "Ташке́нт — столи́ца.",
        "explanation": "<p><strong>Ташке́нт — столи́ца.</strong> Ikkala tomon ham ot, "
                       "demak tire. <em>Есть</em> esa hech qaysi variantda kerak emas — "
                       "hozirgi zamonda “boʻlmoq” qoʻyilmaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Вчера́ ___ хо́лодно. "
                "Сего́дня хорошо́.</strong></p>",
        "choices": ["был", "была́", "бы́ло", "бу́дет"],
        "correct": "бы́ло",
        "explanation": "<p><strong>бы́ло</strong>. Ravish bilan (<em>хо́лодно</em>) doim "
                       "oʻrta jins shakli ishlatiladi. Ikkinchi gapda esa hech qanday "
                       "feʼl yoʻq — chunki u hozirgi zamon.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>Мой брат — врач</strong> va <strong>Он врач</strong> — nega "
                "biri tire bilan, biri tiresiz?</p>",
        "choices": ["Birinchisida ega ot, ikkinchisida olmosh",
                    "Birinchisi uzunroq", "Ikkinchisi savol", "Bu shunchaki uslub"],
        "correct": "Birinchisida ega ot, ikkinchisida olmosh",
        "explanation": "<p>Butun qoida shu juftlikda. <em>Мой брат</em> — ot, "
                       "<em>врач</em> — ot → tire. <em>Он</em> — olmosh → tire yoʻq. "
                       "Bu ikki gapni yodlab qoʻysangiz, qoidani hech qachon "
                       "unutmaysiz.</p>",
    },
    {
        "text": "<p>Rus <strong>был</strong> va oʻzbek <strong>edi</strong> — farqi "
                "nima?</p>",
        "choices": ["Farqi yoʻq", "Ruscha shakl jinsga qarab oʻzgaradi, oʻzbekcha yoʻq",
                    "Oʻzbekcha shakl jinsga qarab oʻzgaradi",
                    "Ruscha shakl faqat koʻplikda ishlatiladi"],
        "correct": "Ruscha shakl jinsga qarab oʻzgaradi, oʻzbekcha yoʻq",
        "explanation": "<p>Vazifasi bir xil: <em>был</em> = <em>edi</em>, "
                       "<em>бу́дет</em> = <em>boʻladi</em>, hozirgi zamonda ikkala tilda "
                       "ham hech nima. Yagona farq — ruschada "
                       "<strong>был / была́ / бы́ло / бы́ли</strong>.</p>",
    },
    {
        "text": "<p>Qaysi qatorda tire <strong>kerak emas</strong>?</p>",
        "choices": ["Москва́ ___ столи́ца", "Мой го́род ___ Ташке́нт",
                    "Ко́фе ___ горя́чий", "Мой па́па ___ врач"],
        "correct": "Ко́фе ___ горя́чий",
        "explanation": "<p><strong>Ко́фе горя́чий</strong> — kesim sifat, demak tire "
                       "yoʻq. Qolgan uchtasida ikkala tomon ham ot, shuning uchun tire "
                       "qoʻyiladi.</p>",
    },
    {
        "text": "<p>Oʻzbekcha <strong>«Men talabaman»</strong> va ruscha "
                "<strong>«Я студе́нт»</strong> — farqi nima?</p>",
        "choices": ["Oʻzbekchada kesim qoʻshimchasi (-man) bor, ruschada hech nima yoʻq",
                    "Ruschada qoʻshimcha bor, oʻzbekchada yoʻq",
                    "Ikkalasida ham feʼl bor", "Farqi yoʻq"],
        "correct": "Oʻzbekchada kesim qoʻshimchasi (-man) bor, ruschada hech nima yoʻq",
        "explanation": "<p>Oʻzbekchada <em>-man, -san, -miz</em> qoʻshimchasi bor. "
                       "Ruschada esa <strong>hech narsa</strong> qoʻyilmaydi: "
                       "<em>Я студе́нт. Ты студе́нт. Мы студе́нты.</em> Faqat olmosh "
                       "oʻzgaradi — oʻrganadigan qoʻshimcha yoʻq.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Москва́ — столи́ца.", "Я студе́нт.", "Окно́ — большо́е.",
                    "За́втра бу́дет уро́к."],
        "correct": "Окно́ — большо́е.",
        "explanation": "<p>Tire ortiqcha. Toʻgʻrisi <strong>Окно́ большо́е.</strong> — "
                       "kesim sifat boʻlganda tire qoʻyilmaydi. Qolgan uchtasi toʻgʻri: "
                       "ot + ot → tire; olmosh ega → tire yoʻq; kelasi zamonda feʼl "
                       "bor.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я есть студе́нт.", "Я студе́нт есть.", "Я студе́нт.",
                    "Я — есть студе́нт."],
        "correct": "Я студе́нт.",
        "explanation": "<p><strong>Я студе́нт.</strong> <em>Есть</em> hozirgi zamonda "
                       "hech qachon qoʻyilmaydi, va olmoshdan keyin tire ham kerak "
                       "emas. Ingliz tilini oʻrgangan oʻquvchi bu yerda “is” ni "
                       "qoʻshib yuborishga moyil boʻladi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Soʻzlarni tartibga soling va tireni toʻgʻri qoʻying.</p>"
                "<p><strong>Ташке́нт / го́род / мой</strong></p>",
        "choices": ["Мой го́род — Ташке́нт.", "Мой го́род Ташке́нт.",
                    "Мой — го́род Ташке́нт.", "Го́род мой — Ташке́нт."],
        "correct": "Мой го́род — Ташке́нт.",
        "explanation": "<p><strong>Мой го́род — Ташке́нт.</strong> <em>Мой го́род</em> "
                       "ot birikmasi, <em>Ташке́нт</em> ham ot — demak tire. Egalik "
                       "soʻzi otning oldida turadi.</p>",
    },
    {
        "text": "<p>Uch zamonni toʻldiring.</p><p><strong>Вчера́ ___ хо́лодно. "
                "Сего́дня хорошо́. За́втра ___ жа́рко.</strong></p>",
        "choices": ["бы́ло … бу́дет", "был … бу́дут", "была́ … бу́дет",
                    "бу́дет … бы́ло"],
        "correct": "бы́ло … бу́дет",
        "explanation": "<p><strong>бы́ло … бу́дет</strong>. Ravish bilan oʻrta jins "
                       "shakli (<em>бы́ло</em>), kelasi zamonda birlik "
                       "(<em>бу́дет</em>). Oʻrtadagi gapda feʼl yoʻq — u hozirgi "
                       "zamon, va hozirgi zamon rus tilida boʻshliq.</p>",
    },
]


# =====================================================================

PRACTICES = [
    {
        "title": "PR-9 Mashq: Koʻplik (множественное число) — -ы, -и, -а va istisnolar",
        "description": "20 savol — jinsga qarab koʻplik qoʻshimchasi, Г К Х Ж Ч Ш Щ imlo "
                       "qoidasi, urgʻu koʻchishi va istisnolar.",
        "tutorial": "PR-9:",
        "questions": Q_PR9,
    },
    {
        "title": "PR-10 Mashq: Shaxs olmoshlari va egalik: мой, твой, наш, ваш",
        "description": "20 savol — sakkiz olmosh, egalikning otga moslashuvi, "
                       "oʻzgarmas его́/её/их va чей/чья/чьё/чьи.",
        "tutorial": "PR-10:",
        "questions": Q_PR10,
    },
    {
        "title": "PR-11 Mashq: «Быть» yoʻq gaplar: Я студент. Кофе горячий. Tire qachon qoʻyiladi?",
        "description": "20 savol — feʼlsiz gaplar, tire qoidasi, был/была́/бы́ло/бы́ли va "
                       "бу́дет/бу́дут.",
        "tutorial": "PR-11:",
        "questions": Q_PR11,
    },
]
