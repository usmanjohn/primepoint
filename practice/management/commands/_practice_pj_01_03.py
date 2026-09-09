# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-1 … PJ-3 (yozuv bloki).

12 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PJ_PRACTICE.md · lesson list in toc_pj_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_01_03.py --master=prime \\
        --expect-questions=12
"""

SUBJECT = {
    "name":        "日本語",
    "description": "Yapon tili — grammatika va yozuv mashqlari",
    "icon":        "bi-brilliance",
    "color":       "#be123c",
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
# PJ-1 — Yapon yozuvi: nega uchta alifbo bor
# =====================================================================

Q_PJ1 = [
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>Yapon tilida nechta yozuv tizimi bir vaqtda ishlatiladi?</strong></p>",
        "choices": ["Bitta", "Ikkita", "Uchta", "Toʻrtta"],
        "correct": "Uchta",
        "explanation": "<p><strong>Uchta</strong>: hiragana, katakana va kanji. Ular bitta "
                       "gap ichida birga ishlaydi va har birining oʻz vazifasi bor — "
                       "biri ikkinchisining oʻrnini bosmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>Hiragananing asosiy vazifasi nima?</strong></p>",
        "choices": ["Chet soʻzlarni yozish", "Grammatik qoʻshimchalar va feʼl oxirlari",
                    "Faqat ismlarni yozish", "Maʼnoni bildirish"],
        "correct": "Grammatik qoʻshimchalar va feʼl oxirlari",
        "explanation": "<p><strong>Grammatika</strong> — hiragananing asosiy ishi. Qoʻshimchalar "
                       "(助詞), feʼl oxirlari va sof yaponcha soʻzlar shu yozuvda yoziladi. "
                       "Chet soʻzlar katakanada, maʼno esa kanjida beriladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>コーヒー qaysi yozuvda yozilgan?</strong></p>",
        "choices": ["Hiragana", "Katakana", "Kanji", "Romaji"],
        "correct": "Katakana",
        "explanation": "<p><strong>Katakana</strong>. コーヒー — «kofe» soʻzi chet tildan "
                       "kirgan, shuning uchun katakanada yoziladi. Katakana belgilari "
                       "burchakli va keskin — hiragananing yumaloq shaklidan shu bilan "
                       "farq qiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>Sizning ismingiz yaponchada qaysi yozuvda yoziladi?</strong></p>",
        "choices": ["Hiragana", "Kanji", "Katakana", "Har uchalasida ham"],
        "correct": "Katakana",
        "explanation": "<p><strong>Katakana</strong>. Chet el ismlari doim katakanada "
                       "yoziladi: アフソナ (Afsona), ジャスル (Jasur), ウズベキスタン "
                       "(Oʻzbekiston).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>Kanji nimani bildiradi?</strong></p>",
        "choices": ["Tovushni", "Maʼnoni", "Urgʻuni", "Gap oxirini"],
        "correct": "Maʼnoni",
        "explanation": "<p><strong>Maʼnoni</strong>. Hiragana va katakana tovush yozadi, "
                       "kanji esa maʼno yozadi. Shuning uchun bitta kanji bir necha xil "
                       "oʻqilishi mumkin — maʼnosi esa oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>Nega yapon tilini faqat hiragana bilan yozish qulay emas?</strong></p>",
        "choices": ["Hiraganada belgilar yetishmaydi",
                    "Bir xil eshitiladigan soʻzlar juda koʻp va ular farqlanmay qoladi",
                    "Hiragana faqat bolalar uchun",
                    "Hiraganani yaponlar oʻqiy olmaydi"],
        "correct": "Bir xil eshitiladigan soʻzlar juda koʻp va ular farqlanmay qoladi",
        "explanation": "<p>Yapon tilida omofon — bir xil eshitiladigan soʻz juda koʻp. "
                       "こうしょう deb oʻqiladigan soʻzlar oʻttizdan ortiq. Faqat hiragana "
                       "bilan yozilsa, hammasi bir xil koʻrinadi; <strong>kanji ularni "
                       "koʻz uchun ajratib beradi</strong>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>Yaponcha matnda soʻzlar orasida boʻshliq qoʻyiladimi?</strong></p>",
        "choices": ["Ha, har doim", "Yoʻq — kanji va hiragananing almashinuvi chegara koʻrsatadi",
                    "Faqat rasmiy matnlarda", "Faqat kitoblarda"],
        "correct": "Yoʻq — kanji va hiragananing almashinuvi chegara koʻrsatadi",
        "explanation": "<p><strong>Boʻshliq qoʻyilmaydi.</strong> Uchta yozuvning almashinuvi "
                       "soʻz chegarasini oʻzi koʻrsatib beradi: kanji koʻrinsa yangi soʻz "
                       "boshlandi, hiragana koʻrinsa grammatika davom etyapti. Bu — uchta "
                       "yozuvni saqlab qolishning yana bir sababi.</p>",
    },
    {
        "text": "<p>Quyidagi gapda <strong>日本語</strong> qaysi yozuvda?</p>"
                "<p><strong>わたしは日本語を勉強します。</strong></p>",
        "choices": ["Hiragana", "Katakana", "Kanji", "Romaji"],
        "correct": "Kanji",
        "explanation": "<p><strong>Kanji</strong>. 日本語 uchta kanjidan iborat: 日 (kun, "
                       "quyosh) + 本 (asos) + 語 (til) = «yapon tili». Qolgan わたしは va "
                       "を…します boʻlaklari hiraganada.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>Kanji ustidagi kichkina hiragana nima deyiladi?</strong></p>",
        "choices": ["Romaji", "Furigana", "Katakana", "Dakuten"],
        "correct": "Furigana",
        "explanation": "<p><strong>Furigana</strong> (ふりがな) — kanjining qanday oʻqilishini "
                       "koʻrsatadigan kichik hiragana. Prime Japanese darslarida u butun "
                       "kurs davomida saqlanadi, shuning uchun siz hech qachon notanish "
                       "belgi oldida toʻxtab qolmaysiz.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>Yapon tilida feʼl gapning qayerida turadi?</strong></p>",
        "choices": ["Boshida", "Oʻrtasida", "Oxirida", "Tartib erkin, farqi yoʻq"],
        "correct": "Oxirida",
        "explanation": "<p><strong>Oxirida.</strong> Yapon tili — SOV tili: ega → "
                       "toʻldiruvchi → feʼl. Oʻzbek tili ham xuddi shunday, shuning uchun "
                       "oʻzbek oʻquvchi uchun bu tartib tabiiy: «Men kitobni oʻqiyman» = "
                       "わたしは本を読みます.</p>",
    },
    {
        "text": "<p>Qaysi javob toʻgʻri?</p>"
                "<p><strong>ワンワン — bu nima va nega katakanada?</strong></p>",
        "choices": ["Chet el ismi", "Tovush taqlidi — itning ovozi",
                    "Kanjining oʻqilishi", "Grammatik qoʻshimcha"],
        "correct": "Tovush taqlidi — itning ovozi",
        "explanation": "<p><strong>Tovush taqlidi.</strong> Katakana uch narsa uchun "
                       "ishlatiladi: chet soʻzlar, chet el ismlari va <strong>tovush "
                       "taqlidi</strong>. ワンワン — oʻzbekcha «vov-vov».</p>",
    },
    {
        "text": "<p>Qaysi fikr <strong>notoʻgʻri</strong>?</p>",
        "choices": ["Hiragana va katakana bir xil 46 tovushni beradi",
                    "Kanji tovushni emas, maʼnoni yozadi",
                    "Avval kanjini, keyin hiraganani oʻrgangan maʼqul",
                    "Katakana chet soʻzlar uchun ishlatiladi"],
        "correct": "Avval kanjini, keyin hiraganani oʻrgangan maʼqul",
        "explanation": "<p>Bu — <strong>notoʻgʻri</strong> fikr. Avval <strong>hiragana</strong> "
                       "oʻrganiladi: barcha qoʻshimchalar va feʼl oxirlari hiraganada, ularsiz "
                       "birorta gap tuzib boʻlmaydi. Kanjisiz gap tushunarli qoladi, "
                       "hiraganasiz esa yoʻq.</p>",
    },
]


# =====================================================================
# PJ-2 — Hiragana 1: あ-そ
# =====================================================================

Q_PJ2 = [
    {
        "text": "<p>Bu belgi qanday oʻqiladi?</p><p><strong>う</strong></p>",
        "choices": ["a", "u", "o", "e"],
        "correct": "u",
        "explanation": "<p><strong>u</strong>. Lekin oʻzbekcha «u» dan farq qiladi: lablar "
                       "oldinga choʻzilmaydi, ogʻiz yassi qoladi. Lab choʻzsangiz, chet el "
                       "aksenti eshitiladi.</p>",
    },
    {
        "text": "<p>Bu belgi qanday oʻqiladi?</p><p><strong>し</strong></p>",
        "choices": ["si", "shi", "chi", "hi"],
        "correct": "shi",
        "explanation": "<p><strong>shi</strong>. Yapon tilida «si» degan tovush "
                       "<em>umuman yoʻq</em>: s + i birikmasi doim yumshab «shi» boʻlib "
                       "chiqadi. Shuning uchun すし — «susi» emas, <strong>sushi</strong>.</p>",
    },
    {
        "text": "<p>Beshta unlini toʻgʻri tartibda koʻrsating.</p>",
        "choices": ["あ い う え お", "あ え い お う", "い あ う お え", "お う え い あ"],
        "correct": "あ い う え お",
        "explanation": "<p><strong>あ い う え お</strong> — a, i, u, e, o. Bu tartib tasodifiy "
                       "emas: har bir yapon lugʻati, har bir jadval va har bir feʼl "
                       "tuslanishi shu tartibda yuradi. Bir marta yodlang — yuzinchi "
                       "darsgacha ishlatasiz.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>かさ</strong></p>",
        "choices": ["kasa", "kaza", "saka", "kesa"],
        "correct": "kasa",
        "explanation": "<p><strong>kasa</strong> — soyabon. か = ka, さ = sa. Belgilarni "
                       "chapdan oʻngga ketma-ket oʻqiysiz, xuddi oʻzbekchadagidek.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>すし</strong></p>",
        "choices": ["susi", "sushi", "shisu", "suchi"],
        "correct": "sushi",
        "explanation": "<p><strong>sushi</strong>. す = su, し = <strong>shi</strong> — «si» "
                       "emas. Bu soʻzni butun dunyo biladi va uning yozilishi し ning "
                       "qoidasini eslab qolishga yordam beradi.</p>",
    },
    {
        "text": "<p>«sekai» (dunyo) soʻzi hiraganada qanday yoziladi?</p>",
        "choices": ["せかい", "さけい", "せきあ", "しかい"],
        "correct": "せかい",
        "explanation": "<p><strong>せかい</strong> — se + ka + i. Uchta boʻgʻin, uchta belgi. "
                       "Hiragana boʻgʻin yozuvi boʻlgani uchun «s» va «e» ni alohida "
                       "yozmaysiz — せ bitta butun belgi.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>おおきい</strong></p>",
        "choices": ["okii", "ōkii", "ooki", "okai"],
        "correct": "ōkii",
        "explanation": "<p><strong>ōkii</strong> — katta. Ikkita お ketma-ket kelsa, «o» "
                       "tovushi <em>uzun</em> aytiladi va lotin yozuvida <strong>ō</strong> "
                       "deb belgilanadi. Uzunlikni qisqartirib aytish maʼnoni buzadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>Hiragana qanday yozuv turi?</strong></p>",
        "choices": ["Harf yozuvi — har belgi bitta tovush",
                    "Boʻgʻin yozuvi — har belgi bitta boʻgʻin",
                    "Maʼno yozuvi — har belgi bitta soʻz",
                    "Raqam yozuvi"],
        "correct": "Boʻgʻin yozuvi — har belgi bitta boʻgʻin",
        "explanation": "<p><strong>Boʻgʻin yozuvi.</strong> か ni «k» va «a» ga ajratib "
                       "boʻlmaydi — u bitta butun boʻgʻin. Shuning uchun oʻzbekcha «ka» "
                       "ikkita harf bilan yozilsa, yaponchada bitta belgi yetadi.</p>",
    },
    {
        "text": "<p>Qaysi juftlikda ikkala belgi ham <strong>さ</strong>-qatoriga tegishli?</p>",
        "choices": ["か va き", "さ va そ", "あ va か", "こ va し"],
        "correct": "さ va そ",
        "explanation": "<p><strong>さ va そ</strong> — ikkalasi ham s- tovushi bilan boshlanadi "
                       "(sa, so). か va き — か-qatori; こ — か-qatori, し — さ-qatori, "
                       "demak «こ va し» aralash juftlik.</p>",
    },
    {
        "text": "<p><strong>さ</strong> va <strong>き</strong> ni bir-biridan nima ajratadi?</p>",
        "choices": ["さ da ikkita gorizontal chiziq, き da bitta",
                    "さ da bitta gorizontal chiziq, き da ikkita",
                    "Faqat kattaligi bilan",
                    "Hech qanday farq yoʻq, ikkalasi bir xil"],
        "correct": "さ da bitta gorizontal chiziq, き da ikkita",
        "explanation": "<p><strong>Chiziqlarni sanang:</strong> さ da bitta gorizontal chiziq, "
                       "き da ikkita. Bu ikki belgi boshlovchilar eng koʻp adashtiradigan "
                       "juftlik — shuning uchun ularni chiziq soni bilan farqlang.</p>",
    },
    {
        "text": "<p>Qaysi oʻqilish <strong>notoʻgʻri</strong>?</p>",
        "choices": ["あき = aki", "いす = isu", "すし = susi", "こえ = koe"],
        "correct": "すし = susi",
        "explanation": "<p><strong>すし «susi» emas — «sushi».</strong> し har doim "
                       "<strong>shi</strong> deb oʻqiladi. Qolgan uchtasi toʻgʻri: あき "
                       "(kuz), いす (stul), こえ (ovoz).</p>",
    },
    {
        "text": "<p>Nega <strong>すき</strong> soʻzi [ski] deb eshitiladi?</p>",
        "choices": ["す belgisi xato yozilgan",
                    "Jarangsiz undosh yonida u tovushi ovozsiz qoladi",
                    "き belgisi u tovushini yutadi",
                    "Bu soʻz chet tildan kirgan"],
        "correct": "Jarangsiz undosh yonida u tovushi ovozsiz qoladi",
        "explanation": "<p>Yapon tilida <strong>u</strong> va <strong>i</strong> tovushlari "
                       "jarangsiz undoshlar orasida yoki soʻz oxirida ovozini yoʻqotadi. "
                       "すき dagi u — k dan oldin turgani uchun deyarli eshitilmaydi. "
                       "Atayin «yutish»ga urinmang: tez gapirsangiz oʻzi shunday chiqadi.</p>",
    },
]


# =====================================================================
# PJ-3 — Hiragana 2: た-ほ
# =====================================================================

Q_PJ3 = [
    {
        "text": "<p>Bu belgi qanday oʻqiladi?</p><p><strong>つ</strong></p>",
        "choices": ["tu", "tsu", "chi", "su"],
        "correct": "tsu",
        "explanation": "<p><strong>tsu</strong>. Bu tovush oʻzbek tilida ham bor — «otsa» "
                       "soʻzining oʻrtasidagi <em>ts</em>. Rus tilidagi <em>ц</em> ham "
                       "xuddi shu. «tu» deb aytish — eng koʻp uchraydigan boshlovchi "
                       "xatosi.</p>",
    },
    {
        "text": "<p>Bu belgi qanday oʻqiladi?</p><p><strong>ち</strong></p>",
        "choices": ["ti", "chi", "shi", "ni"],
        "correct": "chi",
        "explanation": "<p><strong>chi</strong>. Oʻtgan darsdagi し = shi bilan bir xil "
                       "sabab: <strong>i unlisidan oldin til tovushi yumshaydi</strong>. "
                       "Yapon tilida «ti» degan tovush yoʻq.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>なつ</strong></p>",
        "choices": ["natu", "natsu", "nachi", "tsuna"],
        "correct": "natsu",
        "explanation": "<p><strong>natsu</strong> — yoz. つ = tsu, «tu» emas. Bu qoidani "
                       "bir marta oʻrgansangiz, keyin hech qachon adashmaysiz.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>ちかてつ</strong></p>",
        "choices": ["chikatetsu", "tikatetu", "chikatetu", "shikatetsu"],
        "correct": "chikatetsu",
        "explanation": "<p><strong>chikatetsu</strong> — metro. Ikkita istisno bir soʻzda: "
                       "ち = <strong>chi</strong> va つ = <strong>tsu</strong>. Soʻz "
                       "<em>chika</em> (yer osti) + <em>tetsu</em> (temir) dan yigʻilgan — "
                       "«yer osti temiri».</p>",
    },
    {
        "text": "<p>«hoshi» (yulduz) soʻzi hiraganada qanday yoziladi?</p>",
        "choices": ["ほし", "はし", "ほち", "ほす"],
        "correct": "ほし",
        "explanation": "<p><strong>ほし</strong> — ho + shi. はし boʻlsa «hashi» (koʻprik yoki "
                       "tayoqcha) boʻlib qoladi — bitta unli maʼnoni butunlay "
                       "oʻzgartiradi.</p>",
    },
    {
        "text": "<p><strong>の</strong> belgisini <strong>ぬ</strong> va <strong>ね</strong> "
                "dan nima ajratadi?</p>",
        "choices": ["の da qoʻshimcha nuqta bor",
                    "の faqat bitta halqadan iborat, boshqa hech narsa yoʻq",
                    "の boshqa yozuvga tegishli",
                    "の kattaroq yoziladi"],
        "correct": "の faqat bitta halqadan iborat, boshqa hech narsa yoʻq",
        "explanation": "<p><strong>の — eng sodda:</strong> bitta silliq halqa. <strong>ね</strong> "
                       "da halqadan chapda tik chiziq bor. <strong>ぬ</strong> ね ga oʻxshaydi, "
                       "lekin dumi halqani kesib oʻtadi. Qoida: <em>sodda = の, tik chiziqli = "
                       "ね, kesib oʻtgan = ぬ</em>.</p>",
    },
    {
        "text": "<p><strong>ほ</strong> belgisi <strong>は</strong> dan nimasi bilan farq qiladi?</p>",
        "choices": ["Tepasida qoʻshimcha gorizontal chiziq bor",
                    "Halqasi yopiq",
                    "Tik chizigʻi yoʻq",
                    "Ikkita nuqtasi bor"],
        "correct": "Tepasida qoʻshimcha gorizontal chiziq bor",
        "explanation": "<p><strong>ほ = は + bitta gorizontal chiziq</strong> tepada. Boshqa "
                       "hammasi bir xil. Shuning uchun ularni tez yozganda ehtiyot boʻling — "
                       "chiziqni tushirib qoldirsangiz, boshqa belgi chiqadi.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>ふね</strong></p>",
        "choices": ["hune", "fune", "funo", "henu"],
        "correct": "fune",
        "explanation": "<p><strong>fune</strong> — kema. ふ — na sof «h», na sof «f»: yuqori "
                       "tishlar pastki labga <em>tegmaydi</em>, ikki lab orasidan havo "
                       "oʻtadi — xuddi shamdagi olovni puflagandek.</p>",
    },
    {
        "text": "<p>Qaysi juftlikning ikkala belgisi ham <strong>は</strong>-qatoriga tegishli?</p>",
        "choices": ["な va に", "ひ va ほ", "た va て", "ぬ va ふ"],
        "correct": "ひ va ほ",
        "explanation": "<p><strong>ひ va ほ</strong> — ikkalasi ham h- tovushi bilan boshlanadi "
                       "(hi, ho). な va に — な-qatori; た va て — た-qatori; ぬ va ふ — "
                       "aralash juftlik (nu va fu).</p>",
    },
    {
        "text": "<p><strong>は</strong> belgisi qachon [wa] deb oʻqiladi?</p>",
        "choices": ["Har doim", "Hech qachon",
                    "Grammatik qoʻshimcha boʻlib, soʻzdan keyin yolgʻiz turganda",
                    "Faqat soʻz boshida"],
        "correct": "Grammatik qoʻshimcha boʻlib, soʻzdan keyin yolgʻiz turganda",
        "explanation": "<p>Soʻz ichida <strong>は = ha</strong> (はな — gul). Lekin qoʻshimcha "
                       "(助詞) boʻlib soʻzdan keyin yolgʻiz turganda <strong>[wa]</strong> deb "
                       "oʻqiladi. Bu — butun kursdagi eng koʻp uchraydigan oʻqish xatosi; "
                       "PJ-14 da unga toʻliq qaytamiz.</p>",
    },
    {
        "text": "<p>Qaysi oʻqilish <strong>notoʻgʻri</strong>?</p>",
        "choices": ["ねこ = neko", "いぬ = inu", "ちち = titi", "はな = hana"],
        "correct": "ちち = titi",
        "explanation": "<p><strong>ちち «titi» emas — «chichi»</strong> (ota). ち har doim "
                       "<strong>chi</strong> deb oʻqiladi. Qolgan uchtasi toʻgʻri: ねこ "
                       "(mushuk), いぬ (it), はな (gul).</p>",
    },
    {
        "text": "<p>Qaysi gap <strong>toʻgʻri</strong>?</p>",
        "choices": ["ふ ni aytganda yuqori tishlar pastki labga tegadi",
                    "ふ ni aytganda tish labga tegmaydi, havo ikki lab orasidan oʻtadi",
                    "ふ butunlay «h» kabi aytiladi",
                    "ふ katakanaga tegishli belgi"],
        "correct": "ふ ni aytganda tish labga tegmaydi, havo ikki lab orasidan oʻtadi",
        "explanation": "<p>ふ — «h» va «f» orasidagi tovush. Ingliz tilidagi <em>f</em> kabi "
                       "tishni labga tegizsangiz, yaponcha eshitilmaydi. <strong>Ikkala lab "
                       "bir-biriga yaqin turadi va havo ular orasidan oʻtadi.</strong></p>",
    },
]


PRACTICES = [
    {
        "title":       "PJ-1 Mashq: Yapon yozuvi — nega uchta alifbo bor",
        "description": "12 savol — hiragana, katakana va kanjining vazifalari, furigana, SOV tartibi.",
        "tutorial":    "PJ-1:",
        "level":       "easy",
        "questions":   Q_PJ1,
    },
    {
        "title":       "PJ-2 Mashq: Hiragana 1 — あ-そ",
        "description": "12 savol — beshta unli, か va さ qatorlari, し = shi va す ning ovozsizlanishi.",
        "tutorial":    "PJ-2:",
        "level":       "easy",
        "questions":   Q_PJ2,
    },
    {
        "title":       "PJ-3 Mashq: Hiragana 2 — た-ほ",
        "description": "12 savol — た, な va は qatorlari, ち/つ/ふ istisnolari, ぬ/ね/の farqi.",
        "tutorial":    "PJ-3:",
        "level":       "easy",
        "questions":   Q_PJ3,
    },
]
