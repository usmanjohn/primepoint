# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-10 … PJ-12 (kanji va sonlar).

12 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PJ_PRACTICE.md · lesson list in toc_pj_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_10_12.py --master=prime \\
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
# PJ-10 — Kanji nima
# =====================================================================

Q_PJ10 = [
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>Kanji Yaponiyaga qayerdan kelgan?</strong></p>",
        "choices": ["Koreyadan, yaponlar oʻzlari yaratgan", "Xitoydan, Koreya orqali",
                    "Hindistondan buddizm bilan", "Yaponiyada mustaqil paydo boʻlgan"],
        "correct": "Xitoydan, Koreya orqali",
        "explanation": "<p><strong>Xitoydan</strong>, taxminan 1500 yil oldin, Koreya "
                       "orqali. Soʻzning oʻzi ham shuni aytadi: <ruby>漢字<rt>かんじ</rt></ruby> "
                       "— «Han belgilari», Xitoydagi Han sulolasi nomidan.</p>",
    },
    {
        "text": "<p><ruby>森<rt>もり</rt></ruby> belgisi qanday yasalgan?</p>",
        "choices": ["Ikkita <ruby>木<rt>き</rt></ruby> dan", "Uchta <ruby>木<rt>き</rt></ruby> dan",
                    "<ruby>木<rt>き</rt></ruby> va <ruby>山<rt>やま</rt></ruby> dan",
                    "Bu rasm, qismlarga boʻlinmaydi"],
        "correct": "Uchta <ruby>木<rt>き</rt></ruby> dan",
        "explanation": "<p><strong>Uchta daraxt</strong> = qalin oʻrmon. Bu "
                       "<strong>qoʻshilma</strong> turiga misol: maʼnolar qoʻshilib "
                       "yangi maʼno beradi. Ikkita daraxt esa "
                       "<ruby>林<rt>はやし</rt></ruby> — oʻrmoncha.</p>",
    },
    {
        "text": "<p>Radikal (<ruby>部首<rt>ぶしゅ</rt></ruby>) nima?</p>",
        "choices": ["Kanjining oʻqilishi", "Kanjining takrorlanadigan qismi",
                    "Kanjining chiziqlar soni", "Kanjining maʼnosi"],
        "correct": "Kanjining takrorlanadigan qismi",
        "explanation": "<p>Radikal — kanjilarda qayta-qayta uchraydigan "
                       "<strong>qism</strong>. ~2000 belgi ~200 ta radikaldan yigʻilgan, "
                       "shuning uchun siz rasmlarni emas, <strong>gʻishtlarni</strong> "
                       "oʻrganasiz. Radikal koʻpincha maʼnoga ishora ham beradi.</p>",
    },
    {
        "text": "<p><ruby>休<rt>やす</rt></ruby>む («dam olmoq») belgisi qaysi ikki qismdan "
                "iborat?</p>",
        "choices": ["Suv va daraxt", "Odam va daraxt", "Ogʻiz va odam", "Quyosh va oy"],
        "correct": "Odam va daraxt",
        "explanation": "<p><strong>亻</strong> (odam) + <strong><ruby>木<rt>き</rt></ruby></strong> "
                       "(daraxt) = odam daraxtga suyanib turibdi → <strong>dam olmoq</strong>. "
                       "Bir marta koʻrgan odam buni unutmaydi.</p>",
    },
    {
        "text": "<p>Kanjilarning taxminan qancha qismida bir boʻlak <strong>oʻqilishni</strong> "
                "koʻrsatadi?</p>",
        "choices": ["Deyarli hech qaysisida", "Taxminan choragida",
                    "80 foizdan koʻpida", "Faqat sonlarda"],
        "correct": "80 foizdan koʻpida",
        "explanation": "<p><strong>80 foizdan koʻpi</strong> «maʼno + tovush» turiga "
                       "kiradi: bir qism nima haqida ekanini, boshqasi qanday oʻqilishini "
                       "aytadi. Aynan shuning uchun notanish belgini ham taxmin qilish "
                       "mumkin.</p>",
    },
    {
        "text": "<p>Chiziq tartibining asosiy qoidalari qaysi?</p>",
        "choices": ["Pastdan yuqoriga, oʻngdan chapga",
                    "Yuqoridan pastga, chapdan oʻngga, gorizontal vertikaldan oldin",
                    "Avval barcha vertikal chiziqlar",
                    "Tartib ahamiyatsiz"],
        "correct": "Yuqoridan pastga, chapdan oʻngga, gorizontal vertikaldan oldin",
        "explanation": "<p>Uchta qoida yetadi. Toʻgʻri tartibda yozilgan belgi "
                       "<strong>toʻgʻri koʻrinadi</strong> — chiziqlarning uzunligi va "
                       "burchagi oʻz-oʻzidan joyiga tushadi. Telefondagi qoʻlyozma "
                       "kiritish ham shu tartibga qarab ishlaydi.</p>",
    },
    {
        "text": "<p>N5 darajasi uchun taxminan nechta kanji kerak?</p>",
        "choices": ["~100", "~300", "~650", "2136"],
        "correct": "~100",
        "explanation": "<p><strong>~100</strong> ta. N4 uchun ~300, N3 uchun ~650, "
                       "rasmiy <ruby>常用漢字<rt>じょうようかんじ</rt></ruby> roʻyxatida "
                       "esa 2136 ta belgi bor — yapon bolasi ularni toʻqqiz yilda "
                       "oʻrganadi.</p>",
    },
    {
        "text": "<p>Nega yaponlar kanjidan hiragana va katakanani yasashga majbur "
                "boʻlgan?</p>",
        "choices": ["Kanji juda koʻp edi",
                    "Yapon tilida feʼl va sifat tuslanadi, xitoy tilida esa yoʻq",
                    "Xitoy yozuvi taqiqlangan edi",
                    "Kanjini yozish qiyin edi"],
        "correct": "Yapon tilida feʼl va sifat tuslanadi, xitoy tilida esa yoʻq",
        "explanation": "<p>Yapon tili xitoy tiliga <strong>umuman oʻxshamaydi</strong>: "
                       "yaponchada feʼl va sifat doim tuslanadi. Grammatikani yozish "
                       "uchun kana kerak boʻldi. Bugungi tizim shu ikki qatlamning "
                       "qoʻshilishi: <strong>maʼno kanjida, grammatika kanada</strong>.</p>",
    },
    {
        "text": "<p>Qaysi belgi <strong>rasm</strong> (象形) turiga kiradi?</p>",
        "choices": ["<ruby>山<rt>やま</rt></ruby>", "<ruby>上<rt>うえ</rt></ruby>",
                    "<ruby>林<rt>はやし</rt></ruby>", "<ruby>休<rt>やす</rt></ruby>む"],
        "correct": "<ruby>山<rt>やま</rt></ruby>",
        "explanation": "<p><strong><ruby>山<rt>やま</rt></ruby></strong> — togʻning "
                       "oddiylashtirilgan surati, uchta choʻqqi. "
                       "<ruby>上<rt>うえ</rt></ruby> — shartli belgi (指事), "
                       "<ruby>林<rt>はやし</rt></ruby> va <ruby>休<rt>やす</rt></ruby>む "
                       "esa qoʻshilma.</p>",
    },
    {
        "text": "<p><ruby>水<rt>みず</rt></ruby> radikali (氵) boʻlgan kanji nima haqida "
                "boʻlishi mumkin?</p>",
        "choices": ["Odam va tana", "Suyuqlik va suv", "Daraxt va oʻsimlik", "Nutq va soʻz"],
        "correct": "Suyuqlik va suv",
        "explanation": "<p>Radikal maʼnoga ishora beradi. 氵 koʻrsangiz, soʻz suvga yoki "
                       "suyuqlikka aloqador: <ruby>海<rt>うみ</rt></ruby> dengiz, "
                       "<ruby>池<rt>いけ</rt></ruby> hovuz, <ruby>酒<rt>さけ</rt></ruby> "
                       "ichimlik.</p>",
    },
    {
        "text": "<p>Nega bu kursda kanjidan qoʻrqmaslik kerak?</p>",
        "choices": ["Kanji tez orada bekor qilinadi",
                    "Har bir kanji furigana bilan yoziladi, shuning uchun toʻxtab qolmaysiz",
                    "Faqat oʻnta kanji kerak boʻladi",
                    "Kanjini bilmasdan ham yapon tilida yozish mumkin"],
        "correct": "Har bir kanji furigana bilan yoziladi, shuning uchun toʻxtab qolmaysiz",
        "explanation": "<p>Prime Japanese darslarida <strong>har bir kanji furigana "
                       "bilan</strong> yoziladi — yuzinchi darsda ham. Kanjini tanish "
                       "asta-sekin oʻz-oʻzidan keladi, chunki uni oʻqilishi bilan birga, "
                       "minglab marta koʻrasiz.</p>",
    },
    {
        "text": "<p>Qaysi gap <strong>notoʻgʻri</strong>?</p>",
        "choices": ["Kanji ~200 ta qismdan yigʻiladi",
                    "Radikal lugʻatda kanjini topishga yordam beradi",
                    "Har bir kanjini alohida rasm sifatida yodlash kerak",
                    "Kanji maʼnoni, kana grammatikani tashiydi"],
        "correct": "Har bir kanjini alohida rasm sifatida yodlash kerak",
        "explanation": "<p>Bu — <strong>notoʻgʻri</strong> va eng zararli fikr. Kanji "
                       "<strong>qismlardan</strong> yigʻiladi: <ruby>休<rt>やす</rt></ruby>む "
                       "ni yodlamang — 亻 va <ruby>木<rt>き</rt></ruby> ni koʻring.</p>",
    },
]


# =====================================================================
# PJ-11 — On'yomi va kun'yomi
# =====================================================================

Q_PJ11 = [
    {
        "text": "<p>Nega bitta kanjining ikkita oʻqilishi bor?</p>",
        "choices": ["Yaponlar ikki xil shevada gapiradi",
                    "Belgi Xitoydan oʻz talaffuzi bilan kelgan, yaponlarda esa oʻsha maʼnoda oʻz soʻzi bor edi",
                    "Bir oʻqilish eski, ikkinchisi yangi",
                    "Bu yozuv xatosi"],
        "correct": "Belgi Xitoydan oʻz talaffuzi bilan kelgan, yaponlarda esa oʻsha maʼnoda oʻz soʻzi bor edi",
        "explanation": "<p>Yaponlar «togʻ» ni allaqachon <strong>やま</strong> derdi. "
                       "Xitoydan <ruby>山<rt>やま</rt></ruby> belgisi oʻz talaffuzi "
                       "(サン) bilan keldi. Ikkalasi ham saqlanib qoldi: "
                       "<strong>on</strong> xitoycha, <strong>kun</strong> yaponcha.</p>",
    },
    {
        "text": "<p>Kanji boshqa kanji bilan yopishgan boʻlsa, odatda qaysi oʻqilish "
                "ishlaydi?</p>",
        "choices": ["Kun'yomi", "On'yomi", "Ikkalasi ham", "Har xil, qoida yoʻq"],
        "correct": "On'yomi",
        "explanation": "<p><strong>On'yomi.</strong> Qoida: <strong>kanji + kanji → "
                       "on</strong>, <strong>yolgʻiz yoki hiragana dumi bilan → "
                       "kun</strong>. Bu taxmin beradi, kafolat emas — lekin koʻpincha "
                       "toʻgʻri chiqadi.</p>",
    },
    {
        "text": "<p><ruby>火山<rt>かざん</rt></ruby> soʻzida qaysi oʻqilish ishlagan?</p>",
        "choices": ["Kun'yomi", "On'yomi", "Aralash", "Bu katakana soʻz"],
        "correct": "On'yomi",
        "explanation": "<p><strong>On'yomi</strong> — ikkita kanji bir-biriga yopishgan. "
                       "Maʼnosi <strong>vulqon</strong>: olov + togʻ. Yolgʻiz turganda "
                       "esa <ruby>山<rt>やま</rt></ruby> «やま» boʻlardi.</p>",
    },
    {
        "text": "<p>Okurigana (<ruby>送<rt>おく</rt></ruby>り<ruby>仮名<rt>がな</rt></ruby>) "
                "nima?</p>",
        "choices": ["Kanji ustidagi oʻqilish", "Kanjidan keyin keladigan hiragana",
                    "Kanjining xitoycha talaffuzi", "Lugʻatdagi tartib raqami"],
        "correct": "Kanjidan keyin keladigan hiragana",
        "explanation": "<p>Kanjidan keyingi <strong>hiragana dumi</strong>. U ikki ish "
                       "qiladi: kun'yomi ekanini koʻrsatadi va <strong>tuslanishni</strong> "
                       "tashiydi. Kanji ustidagi oʻqilish esa <em>furigana</em> — boshqa "
                       "narsa.</p>",
    },
    {
        "text": "<p>Bu uch shakl orasida nima oʻzgaryapti?</p>"
                "<p><strong><ruby>見<rt>み</rt></ruby>る → <ruby>見<rt>み</rt></ruby>ます → "
                "<ruby>見<rt>み</rt></ruby>ました</strong></p>",
        "choices": ["Kanji oʻzgaryapti", "Faqat hiragana dumi oʻzgaryapti",
                    "Ikkalasi ham oʻzgaryapti", "Oʻqilish butunlay oʻzgaryapti"],
        "correct": "Faqat hiragana dumi oʻzgaryapti",
        "explanation": "<p><strong>Kanji qimirlamaydi</strong> — u oʻzakni tashiydi. "
                       "Faqat dum oʻzgaradi. Oʻzbekcha bilan aynan bir xil mantiq: "
                       "<em>koʻr</em>-moq, <em>koʻr</em>-di, <em>koʻr</em>-adi — oʻzak "
                       "bir xil qoladi.</p>",
    },
    {
        "text": "<p>Lugʻatda oʻqilish <strong>katakana</strong> bilan berilgan boʻlsa, bu "
                "nimani bildiradi?</p>",
        "choices": ["Bu soʻz katakanada yoziladi", "Bu on'yomi",
                    "Bu kun'yomi", "Bu chet soʻz"],
        "correct": "Bu on'yomi",
        "explanation": "<p>Bu shunchaki <strong>shartli belgi</strong>: katakana = "
                       "on'yomi, hiragana = kun'yomi. Haqiqiy matnda furigana "
                       "<strong>doim hiraganada</strong> boʻladi.</p>",
    },
    {
        "text": "<p><ruby>日<rt>ひ</rt></ruby> belgisi <ruby>日本人<rt>にほんじん</rt></ruby> "
                "da nega «ひ» emas?</p>",
        "choices": ["Bu boshqa belgi", "Boshqa kanjilar bilan yopishgan — demak on'yomi",
                    "Chunki soʻz uzun", "Bu istisno, qoidasi yoʻq"],
        "correct": "Boshqa kanjilar bilan yopishgan — demak on'yomi",
        "explanation": "<p>Qoida ishlayapti: <strong>kanji + kanji → on'yomi</strong>. "
                       "Yolgʻiz turganda kun'yomi «ひ» boʻlardi.</p>",
    },
    {
        "text": "<p>Kanji <strong>yolgʻiz</strong> turganda odatda qaysi oʻqilish "
                "ishlaydi?</p>",
        "choices": ["On'yomi", "Kun'yomi", "Ikkalasi teng", "Bu soʻzga bogʻliq emas"],
        "correct": "Kun'yomi",
        "explanation": "<p><strong>Kun'yomi</strong> — yaponlarning oʻz soʻzi. "
                       "<ruby>山<rt>やま</rt></ruby> yolgʻiz turganda «やま», "
                       "<ruby>水<rt>みず</rt></ruby> esa «みず».</p>",
    },
    {
        "text": "<p>Oʻqilishni yodlashning eng samarali usuli qaysi?</p>",
        "choices": ["Har bir kanjining barcha oʻqilishlarini roʻyxat qilib yodlash",
                    "Oʻqilishni soʻz ichida yodlash",
                    "Faqat on'yomi ni yodlash",
                    "Faqat kun'yomi ni yodlash"],
        "correct": "Oʻqilishni soʻz ichida yodlash",
        "explanation": "<p><strong>Soʻz ichida.</strong> "
                       "<ruby>日本<rt>にほん</rt></ruby> ni butun soʻz sifatida bilsangiz, "
                       "<ruby>日<rt>にち</rt></ruby> ning oʻqilishi oʻz-oʻzidan kelib "
                       "chiqadi — va istisnolar ham shu yoʻl bilan yodda qoladi.</p>",
    },
    {
        "text": "<p>Qaysi soʻzda <strong>kun'yomi</strong> ishlagan?</p>",
        "choices": ["<ruby>日本人<rt>にほんじん</rt></ruby>", "<ruby>火山<rt>かざん</rt></ruby>",
                    "<ruby>水曜日<rt>すいようび</rt></ruby>", "<ruby>大<rt>おお</rt></ruby>きい"],
        "correct": "<ruby>大<rt>おお</rt></ruby>きい",
        "explanation": "<p><strong><ruby>大<rt>おお</rt></ruby>きい</strong> — hiragana "
                       "dumi bor, demak kun'yomi. Qolgan uchtasida kanjilar "
                       "yopishgan — hammasi on'yomi.</p>",
    },
    {
        "text": "<p>Nega <ruby>見<rt>み</rt></ruby> ni okuriganasiz yozish yaxshi emas?</p>",
        "choices": ["Bu grammatik xato emas, shunchaki chiroyli emas",
                    "Dum boʻlmasa oʻqilish ham, feʼl shakli ham noaniq qoladi",
                    "Kanji yolgʻiz yozilmaydi",
                    "Bu belgi doim dum bilan keladi"],
        "correct": "Dum boʻlmasa oʻqilish ham, feʼl shakli ham noaniq qoladi",
        "explanation": "<p>Dum <strong>ikkita maʼlumot</strong> tashiydi: kun'yomi "
                       "ekani va qaysi shakl ekani. <ruby>見<rt>み</rt></ruby>る "
                       "«koʻrmoq», <ruby>見<rt>み</rt></ruby>ました «koʻrdim» — farqni "
                       "faqat dum koʻrsatadi.</p>",
    },
    {
        "text": "<p>Qaysi gap <strong>notoʻgʻri</strong>?</p>",
        "choices": ["On'yomi xitoychadan kelgan oʻqilish",
                    "Kun'yomi yaponlarning oʻz soʻzi",
                    "Kanji + kanji birikmasi odatda kun'yomi bilan oʻqiladi",
                    "Okurigana tuslanishni tashiydi"],
        "correct": "Kanji + kanji birikmasi odatda kun'yomi bilan oʻqiladi",
        "explanation": "<p>Teskarisi: <strong>kanji + kanji → on'yomi</strong>. "
                       "Kun'yomi kanji yolgʻiz turganda yoki hiragana dumi bilan "
                       "kelganda ishlaydi.</p>",
    },
]


# =====================================================================
# PJ-12 — Sonlar, sana, yosh
# =====================================================================

Q_PJ12 = [
    {
        "text": "<p>Bu son qanday oʻqiladi?</p><p><strong><ruby>三十四<rt>?</rt></ruby></strong></p>",
        "choices": ["さんじゅうよん", "さんじゅうし", "みっつじゅうよん", "さんじゅっよん"],
        "correct": "さんじゅうよん",
        "explanation": "<p><strong>さんじゅうよん</strong> = 34, yaʼni 3 × 10 + 4. "
                       "Yaponchada 11 dan 99 gacha hamma son shu tarzda qoʻshish va "
                       "koʻpaytirish bilan yasaladi — yangi soʻz yodlash kerak emas.</p>",
    },
    {
        "text": "<p>Aprel oyi qanday oʻqiladi?</p>",
        "choices": ["よんがつ", "しがつ", "よががつ", "しちがつ"],
        "correct": "しがつ",
        "explanation": "<p><strong>しがつ</strong> (<ruby>四月<rt>しがつ</rt></ruby>). "
                       "Oylarda 4, 7 va 9 majburan <strong>し · しち · く</strong> "
                       "shaklini oladi — bu tanlov emas. «よんがつ» deb aytsangiz, "
                       "yaponcha eshitilmaydi.</p>",
    },
    {
        "text": "<p>Oyning 20-kuni qanday aytiladi?</p>",
        "choices": ["にじゅうにち", "はつか", "にじゅっか", "ふつか"],
        "correct": "はつか",
        "explanation": "<p><strong>はつか</strong> — qoidaga boʻysunmaydigan alohida "
                       "soʻz. Xuddi shunday 14 (じゅうよっか) va 24 (にじゅうよっか) "
                       "ham istisno. <strong>ふつか</strong> esa 2-kun.</p>",
    },
    {
        "text": "<p>300 soni qanday oʻqiladi?</p>",
        "choices": ["さんひゃく", "さんびゃく", "さんぴゃく", "みひゃく"],
        "correct": "さんびゃく",
        "explanation": "<p><strong>さんびゃく</strong> — ひ jaranglashib <strong>び</strong> "
                       "boʻladi. Bu tartibsizlik emas, talaffuzni yengillashtiradigan "
                       "tabiiy hodisa. 600 esa ろっぴゃく, 800 — はっぴゃく.</p>",
    },
    {
        "text": "<p>Payshanba kuni qanday oʻqiladi?</p>",
        "choices": ["もくようび", "きんようび", "すいようび", "かようび"],
        "correct": "もくようび",
        "explanation": "<p><strong>もくようび</strong> (<ruby>木曜日<rt>もくようび</rt></ruby>) "
                       "— «daraxt kuni». Hafta kunlari tabiat unsurlaridan yasalgan: "
                       "oy, olov, suv, daraxt, oltin, tuproq, quyosh.</p>",
    },
    {
        "text": "<p>Yigirma yosh qanday aytiladi?</p>",
        "choices": ["にじゅっさい", "はたち", "にじゅうさい", "はつか"],
        "correct": "はたち",
        "explanation": "<p><strong>はたち</strong> — butunlay alohida soʻz, "
                       "«にじゅっさい» emas. Yaponiyada bu muhim yosh sanaladi. "
                       "<strong>はつか</strong> esa oyning 20-kuni — adashtirmang.</p>",
    },
    {
        "text": "<p>10 000 soni qanday aytiladi?</p>",
        "choices": ["まん", "いちまん", "じゅうせん", "ひゃくせん"],
        "correct": "いちまん",
        "explanation": "<p><strong>いちまん</strong> — doim いち bilan. «まん» yolgʻiz "
                       "ishlatilmaydi. Diqqat: yaponchada 10 000 «oʻn ming» emas, "
                       "alohida birlik.</p>",
    },
    {
        "text": "<p>Oyning 8-kuni qanday aytiladi?</p>",
        "choices": ["はちにち", "ようか", "やっか", "はっか"],
        "correct": "ようか",
        "explanation": "<p><strong>ようか</strong>. Oyning birinchi oʻn kuni butunlay "
                       "istisno — ular qadimgi yaponcha sanoqdan yasalgan: ついたち, "
                       "ふつか, みっか, よっか, いつか, むいか, なのか, "
                       "<strong>ようか</strong>, ここのか, とおか.</p>",
    },
    {
        "text": "<p>Sentabr oyi qanday oʻqiladi?</p>",
        "choices": ["きゅうがつ", "くがつ", "ここのがつ", "きゅうかつ"],
        "correct": "くがつ",
        "explanation": "<p><strong>くがつ</strong>. Yana oʻsha uchlik: oylarda 4, 7 va 9 "
                       "majburan し · しち · く boʻladi. «きゅうがつ» notoʻgʻri.</p>",
    },
    {
        "text": "<p>Bir kishi va ikki kishi qanday aytiladi?</p>",
        "choices": ["いちにん va ににん", "ひとり va ふたり",
                    "ひとつ va ふたつ", "いちり va にり"],
        "correct": "ひとり va ふたり",
        "explanation": "<p><strong>ひとり</strong> va <strong>ふたり</strong> — birinchi "
                       "ikkitasi istisno. Uchinchisidan qoida boshlanadi: "
                       "<ruby>三人<rt>さんにん</rt></ruby>. Sanoq soʻzlarining toʻliq "
                       "tizimini PJ-43 da koʻramiz.</p>",
    },
    {
        "text": "<p>Nima uchun yaponchada sonning oʻzi narsani sanash uchun yetmaydi?</p>",
        "choices": ["Sonlar juda qisqa",
                    "Son bilan narsa orasiga sanoq soʻzi qoʻyilishi shart",
                    "Sonlar faqat sanada ishlatiladi",
                    "Narsalar sanalmaydi"],
        "correct": "Son bilan narsa orasiga sanoq soʻzi qoʻyilishi shart",
        "explanation": "<p>Sanoq soʻzi narsaning turiga qarab oʻzgaradi: odam uchun "
                       "<ruby>人<rt>にん</rt></ruby>, yassi narsa uchun "
                       "<ruby>枚<rt>まい</rt></ruby>. Oʻzbekchada ham bu bor («uch "
                       "<em>nafar</em> odam»), lekin u yerda ixtiyoriy, yaponchada "
                       "esa <strong>majburiy</strong>.</p>",
    },
    {
        "text": "<p>Qaysi oʻqilish <strong>notoʻgʻri</strong>?</p>",
        "choices": ["<ruby>二十<rt>にじゅう</rt></ruby> = 20",
                    "<ruby>七月<rt>ななかつ</rt></ruby> = iyul",
                    "<ruby>百<rt>ひゃく</rt></ruby> = 100",
                    "<ruby>十日<rt>とおか</rt></ruby> = oyning 10-kuni"],
        "correct": "<ruby>七月<rt>ななかつ</rt></ruby> = iyul",
        "explanation": "<p>Iyul — <strong>しちがつ</strong>, «ななかつ» emas. Oylarda 7 "
                       "majburan «しち» boʻladi. Qolgan uchtasi toʻgʻri.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PJ-10 Mashq: Kanji nima",
        "description": "12 savol — kanjining kelib chiqishi, toʻrt turi, radikallar va chiziq tartibi.",
        "tutorial":    "PJ-10:",
        "level":       "easy",
        "questions":   Q_PJ10,
    },
    {
        "title":       "PJ-11 Mashq: On'yomi va kun'yomi",
        "description": "12 savol — ikki oʻqilishning sababi, qaysi biri qachon, okurigana.",
        "tutorial":    "PJ-11:",
        "level":       "easy",
        "questions":   Q_PJ11,
    },
    {
        "title":       "PJ-12 Mashq: Sonlar, sana va yosh",
        "description": "12 savol — sonlar va tovush oʻzgarishlari, oy va kun nomlari, hafta kunlari, yosh.",
        "tutorial":    "PJ-12:",
        "level":       "easy",
        "questions":   Q_PJ12,
    },
]
