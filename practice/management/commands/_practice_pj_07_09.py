# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-7 … PJ-9 (katakana).

12 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PJ_PRACTICE.md · lesson list in toc_pj_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_07_09.py --master=prime \\
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
# PJ-7 — Katakana 1: ア-ソ
# =====================================================================

Q_PJ7 = [
    {
        "text": "<p>Bu belgi qanday oʻqiladi?</p><p><strong>ウ</strong></p>",
        "choices": ["u", "a", "wa", "ku"],
        "correct": "u",
        "explanation": "<p><strong>u</strong> — katakana ウ, hiragana <strong>う</strong> "
                       "ning jufti. Tovushi aynan bir xil: faqat shakl boshqa.</p>",
    },
    {
        "text": "<p><strong>ア</strong> va <strong>あ</strong> orasida qanday farq bor?</p>",
        "choices": ["Tovushi boshqa", "Tovushi bir xil, vazifasi va shakli boshqa",
                    "ア uzunroq aytiladi", "ア faqat ismlarda uchraydi"],
        "correct": "Tovushi bir xil, vazifasi va shakli boshqa",
        "explanation": "<p>Ikkalasi ham <strong>[a]</strong>. Katakana yangi tovush "
                       "bermaydi — u siz bilgan 46 boʻgʻinning ikkinchi kiyimi. Farq "
                       "shaklda (burchakli / yumaloq) va vazifada (chet soʻz / "
                       "grammatika).</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>アイス</strong></p>",
        "choices": ["aisu", "aizu", "asui", "aishi"],
        "correct": "aisu",
        "explanation": "<p><strong>aisu</strong> — muzqaymoq. Chet soʻz boʻlgani uchun "
                       "katakanada yozilgan. ス dagi «u» yengil aytiladi.</p>",
    },
    {
        "text": "<p>Nega katakana burchakli, hiragana esa yumaloq?</p>",
        "choices": ["Katakana keyinroq yaratilgan",
                    "Katakana kanjining bir boʻlagidan, hiragana esa butun kanjining tez yozilishidan chiqqan",
                    "Katakana chet elda yaratilgan",
                    "Bu shunchaki uslub masalasi"],
        "correct": "Katakana kanjining bir boʻlagidan, hiragana esa butun kanjining tez yozilishidan chiqqan",
        "explanation": "<p><strong>Kelib chiqishi</strong> shaklni belgilagan. Rohiblar "
                       "matn chetiga izoh yozish uchun kanjining <em>bir boʻlagini</em> "
                       "olgan — boʻlak keskin chiziqlar beradi (阿 → ア). Hiragana esa "
                       "butun kanjini uzluksiz qoʻlyozmada yozishdan chiqqan (安 → あ), "
                       "shuning uchun u oqadi.</p>",
    },
    {
        "text": "<p>Katakana qaysi uch narsa uchun ishlatiladi?</p>",
        "choices": ["Grammatika, feʼl oxirlari va qoʻshimchalar",
                    "Chet soʻzlar, chet el ismlari va tovush taqlidi",
                    "Faqat rasmiy hujjatlar",
                    "Sonlar, sanalar va oʻlchov birliklari"],
        "correct": "Chet soʻzlar, chet el ismlari va tovush taqlidi",
        "explanation": "<p>Uchtasi ham «chetdan kelgan» degan umumiy gʻoyaga bogʻlanadi. "
                       "Grammatika, feʼl oxirlari va qoʻshimchalar esa <strong>doim "
                       "hiraganada</strong> yoziladi.</p>",
    },
    {
        "text": "<p>«oashisu» (voha) soʻzi katakanada qanday yoziladi?</p>",
        "choices": ["オアシス", "オアシツ", "アオシス", "オアスシ"],
        "correct": "オアシス",
        "explanation": "<p><strong>オアシス</strong> — o + a + shi + su. Toʻrtta belgi, "
                       "toʻrtta zarb. シ = «shi», «si» emas — bu qoida katakanada ham "
                       "aynan shunday ishlaydi.</p>",
    },
    {
        "text": "<p>Nega <strong>オアシス</strong> oxirida <strong>ス</strong> turadi?</p>",
        "choices": ["Bu soʻzning asl shakli shunday",
                    "Yapon tilida yolgʻiz undosh boʻlmaydi, shuning uchun «s» ga «u» qoʻshilgan",
                    "ス bu yerda oʻqilmaydi",
                    "Katakana soʻzlari doim ス bilan tugaydi"],
        "correct": "Yapon tilida yolgʻiz undosh boʻlmaydi, shuning uchun «s» ga «u» qoʻshilgan",
        "explanation": "<p><strong>Yolgʻiz undosh boʻlmaydi</strong> (ん dan tashqari). "
                       "Chet soʻz yaponchaga oʻtganda har bir yolgʻiz undoshga unli "
                       "qoʻshiladi — aynan shuning uchun chet soʻzlar yaponchada "
                       "uzunroq eshitiladi.</p>",
    },
    {
        "text": "<p>Quyidagi katakana belgilaridan qaysi biri oʻz hiragana juftiga "
                "eng oʻxshash?</p>",
        "choices": ["ク", "カ", "ス", "コ"],
        "correct": "カ",
        "explanation": "<p><strong>カ</strong> va <strong>か</strong> deyarli bir xil "
                       "koʻrinadi, chunki ikkalasi bitta kanjidan chiqqan. Xuddi shunday "
                       "juftliklar: キ~き, セ~せ. Ularni alohida yodlash shart emas.</p>",
    },
    {
        "text": "<p><strong>ク</strong> va <strong>ケ</strong> ni nima ajratadi?</p>",
        "choices": ["ケ da uchinchi, tik chiziq bor", "ク kattaroq yoziladi",
                    "ケ da halqa bor", "Hech qanday farq yoʻq"],
        "correct": "ケ da uchinchi, tik chiziq bor",
        "explanation": "<p><strong>Chiziqlarni sanang.</strong> ク ikki chiziqdan iborat va "
                       "oʻtkir burchak yasaydi; ケ da esa qoʻshimcha tik chiziq bor.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>スイス</strong></p>",
        "choices": ["suisu", "sushi", "suizu", "shiisu"],
        "correct": "suisu",
        "explanation": "<p><strong>suisu</strong> — Shveytsariya. Mamlakat nomi, demak "
                       "chet el nomi, demak katakana. Diqqat: birinchi va uchinchi belgi "
                       "bir xil — ス.</p>",
    },
    {
        "text": "<p>Yaponcha matnda katakana nima uchun darrov koʻzga tashlanadi?</p>",
        "choices": ["U kattaroq yoziladi",
                    "Uning burchakli shakli yumaloq hiragana orasida ajralib turadi",
                    "U doim qizil rangda beriladi",
                    "U doim gap boshida keladi"],
        "correct": "Uning burchakli shakli yumaloq hiragana orasida ajralib turadi",
        "explanation": "<p>Bu — katakananing <strong>ishi</strong>. Keskin shakli "
                       "oʻquvchiga «diqqat, bu soʻz chetdan kelgan» degan signalni bir "
                       "zumda beradi.</p>",
    },
    {
        "text": "<p>Qaysi gap <strong>notoʻgʻri</strong>?</p>",
        "choices": ["ア va あ bir xil tovushni beradi",
                    "Katakana chet soʻzlar uchun ishlatiladi",
                    "Katakana hiraganadan boshqa tovushlarni bildiradi",
                    "Chet el ismlari katakanada yoziladi"],
        "correct": "Katakana hiraganadan boshqa tovushlarni bildiradi",
        "explanation": "<p>Bu — <strong>notoʻgʻri</strong>. Tovushlar aynan bir xil: "
                       "ア = あ = [a]. Faqat shakl va vazifa boshqa. Qolgan uchtasi "
                       "toʻgʻri.</p>",
    },
]


# =====================================================================
# PJ-8 — Katakana 2: タ-ン
# =====================================================================

Q_PJ8 = [
    {
        "text": "<p>Bu belgi qanday oʻqiladi?</p><p><strong>ツ</strong></p>",
        "choices": ["shi", "tsu", "so", "n"],
        "correct": "tsu",
        "explanation": "<p><strong>tsu</strong> — katakana ツ, hiragana <strong>つ</strong> "
                       "ning jufti. Kichik chiziqlari <strong>tepada</strong> va deyarli "
                       "tik; uzun chizigʻi tepadan pastga tushadi.</p>",
    },
    {
        "text": "<p><strong>シ</strong> va <strong>ツ</strong> ni qaysi qoida bilan "
                "ajratasiz?</p>",
        "choices": ["Kattaligi bilan",
                    "Chiziq yoʻnalishi bilan — kelib chiqqan hiraganadan meros",
                    "Nuqtalar soni bilan",
                    "Ularni faqat yodlash mumkin"],
        "correct": "Chiziq yoʻnalishi bilan — kelib chiqqan hiraganadan meros",
        "explanation": "<p><strong>Yoʻnalish hal qiladi.</strong> シ — し dan, uning uzun "
                       "chizigʻi <em>pastdan yuqoriga</em> koʻtariladi va kichik chiziqlar "
                       "chap yonda, yotiq. ツ — つ dan, uzun chizigʻi <em>tepadan "
                       "pastga</em> tushadi va kichik chiziqlar tepada, tik. Yodlash "
                       "shart emas.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>テレビ</strong></p>",
        "choices": ["terebi", "telebi", "tereби", "tsurebi"],
        "correct": "terebi",
        "explanation": "<p><strong>terebi</strong> — televizor. <strong>ビ</strong> = ヒ + "
                       "dakuten. Asl soʻzdagi «l» ラ-qatoriga aylangan, chunki yapon "
                       "tilida l tovushi yoʻq.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>ミルク</strong></p>",
        "choices": ["miruku", "mirku", "milk", "miluku"],
        "correct": "miruku",
        "explanation": "<p><strong>miruku</strong> — sut, <strong>uch zarb</strong>. Ikki "
                       "qoida ishladi: «l» → ラ-qatori (ル), va oxirgi yolgʻiz «k» ga "
                       "unli qoʻshildi (ク).</p>",
    },
    {
        "text": "<p>Katakana <strong>ヘ</strong> va hiragana <strong>へ</strong> orasida "
                "qanday farq bor?</p>",
        "choices": ["ヘ kattaroq", "Hech qanday — shakli ham, oʻqilishi ham bir xil",
                    "ヘ boshqa tovush beradi", "ヘ faqat ismlarda ishlatiladi"],
        "correct": "Hech qanday — shakli ham, oʻqilishi ham bir xil",
        "explanation": "<p>Bu — yaponcha yozuvdagi <strong>yagona</strong> shunday "
                       "juftlik: ikkalasi aynan bir xil chiziladi va [he] deb oʻqiladi. "
                       "Qaysi alifbo ekani atrofdagi belgilardan maʼlum boʻladi.</p>",
    },
    {
        "text": "<p>«pan» (non) soʻzi katakanada qanday yoziladi?</p>",
        "choices": ["パン", "バン", "ハン", "パソ"],
        "correct": "パン",
        "explanation": "<p><strong>パン</strong> — ハ ga <strong>handakuten</strong> (゜) "
                       "qoʻyilib «pa» boʻlgan, keyin ン. バン boʻlsa dakuten bilan «ban» "
                       "boʻlib qolardi.</p>",
    },
    {
        "text": "<p>Dakuten va handakuten katakanada qanday ishlaydi?</p>",
        "choices": ["Katakanada ular ishlatilmaydi",
                    "Hiraganadagi bilan aynan bir xil",
                    "Faqat handakuten ishlatiladi",
                    "Ular teskari maʼno beradi"],
        "correct": "Hiraganadagi bilan aynan bir xil",
        "explanation": "<p><strong>Hech narsa oʻzgarmaydi.</strong> Ikkita tirnoq "
                       "jaranglashtiradi (カ → ガ), doiracha esa p beradi (ハ → パ). "
                       "PJ-6 da oʻrgangan hamma narsa shundoq ishlayveradi.</p>",
    },
    {
        "text": "<p><strong>ソ</strong> va <strong>ン</strong> dan qaysi birining uzun "
                "chizigʻi pastdan yuqoriga koʻtariladi?</p>",
        "choices": ["ソ", "ン", "Ikkalasi ham", "Hech qaysisi"],
        "correct": "ン",
        "explanation": "<p><strong>ン</strong> — u <strong>ん</strong> dan kelib chiqqan, "
                       "ん esa pastdan yuqoriga sweep qiladi. <strong>ソ</strong> esa "
                       "<strong>そ</strong> dan, uning chizigʻi tepadan pastga tushadi. "
                       "Xuddi シ/ツ juftligidagi mantiq.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>トマト</strong></p>",
        "choices": ["tomato", "tomata", "tamato", "tomado"],
        "correct": "tomato",
        "explanation": "<p><strong>tomato</strong> — pomidor. Diqqat qiling: birinchi va "
                       "uchinchi belgi <strong>bir xil</strong> — ト. Katakana soʻzlarida "
                       "bunday takror koʻp uchraydi.</p>",
    },
    {
        "text": "<p><strong>ス</strong> va <strong>ヌ</strong> ni nima ajratadi?</p>",
        "choices": ["ヌ da kesib oʻtadigan qoʻshimcha chiziq bor",
                    "ス da kesib oʻtadigan qoʻshimcha chiziq bor",
                    "ヌ da halqa bor",
                    "Faqat kattaligi bilan"],
        "correct": "ヌ da kesib oʻtadigan qoʻshimcha chiziq bor",
        "explanation": "<p><strong>ヌ</strong> da chapdan oʻngga kesib oʻtadigan "
                       "qoʻshimcha chiziq bor; <strong>ス</strong> da esa yoʻq — u "
                       "burchak, keyin dumdan iborat.</p>",
    },
    {
        "text": "<p>Nega <strong>ヲ</strong> zamonaviy matnda deyarli uchramaydi?</p>",
        "choices": ["U eskirgan va bekor qilingan",
                    "U faqat grammatik qoʻshimcha tovushini bildiradi, qoʻshimchalar esa doim hiraganada yoziladi",
                    "Uni yozish juda qiyin",
                    "U faqat ismlarda ishlatiladi"],
        "correct": "U faqat grammatik qoʻshimcha tovushini bildiradi, qoʻshimchalar esa doim hiraganada yoziladi",
        "explanation": "<p>ヲ jadvalda hiragana <strong>を</strong> ning jufti sifatida "
                       "turadi, lekin を faqat grammatik qoʻshimcha, qoʻshimchalar esa "
                       "<strong>doim hiraganada</strong>. Shuning uchun ヲ ga oʻrin "
                       "qolmaydi.</p>",
    },
    {
        "text": "<p>Qaysi oʻqilish <strong>notoʻgʻri</strong>?</p>",
        "choices": ["ホテル = hoteru", "ピアノ = piano",
                    "ワイン = wain", "ミルク = milk"],
        "correct": "ミルク = milk",
        "explanation": "<p><strong>ミルク «milk» emas — [miruku]</strong>, uch zarb. "
                       "Yaponchada yolgʻiz undosh boʻlmaydi va l tovushi yoʻq, shuning "
                       "uchun soʻz uzayadi. Qolgan uchtasi toʻgʻri.</p>",
    },
]


# =====================================================================
# PJ-9 — ー, chet soʻzlar, yangi birikmalar
# =====================================================================

Q_PJ9 = [
    {
        "text": "<p><strong>コーヒー</strong> soʻzida nechta zarb (mora) bor?</p>",
        "choices": ["Ikkita", "Uchta", "Toʻrtta", "Beshta"],
        "correct": "Toʻrtta",
        "explanation": "<p><strong>Toʻrtta</strong>: ko · o · hi · i. Har bir "
                       "<strong>ー</strong> toʻliq bitta zarb sanaladi — xuddi ん va ッ "
                       "kabi. Uni «tashlab ketish» eng koʻp uchraydigan xato.</p>",
    },
    {
        "text": "<p><strong>ー</strong> belgisi nima qiladi?</p>",
        "choices": ["Oldingi unlini uzaytiradi", "Keyingi undoshni ikkilantiradi",
                    "Soʻzni ajratadi", "Urgʻuni koʻrsatadi"],
        "correct": "Oldingi unlini uzaytiradi",
        "explanation": "<p><strong>Uzaytiradi</strong> — hiraganadagi おう yoki えい ning "
                       "katakana usuli, faqat ancha soddaroq. Keyingi undoshni "
                       "ikkilantiradigan belgi esa boshqa: kichik <strong>ッ</strong>.</p>",
    },
    {
        "text": "<p>Nega «test» yaponchada <strong>テスト</strong> boʻladi?</p>",
        "choices": ["Asl soʻz shunday eshitiladi",
                    "Yolgʻiz undoshga unli qoʻshiladi: «s» ga «u», «t» ga «o»",
                    "Katakana soʻzlari doim uch belgidan iborat",
                    "ト bu yerda oʻqilmaydi"],
        "correct": "Yolgʻiz undoshga unli qoʻshiladi: «s» ga «u», «t» ga «o»",
        "explanation": "<p>Yapon tilida yolgʻiz undosh boʻlmaydi. Odatda "
                       "<strong>u</strong> qoʻshiladi, lekin <strong>t va d dan keyin "
                       "o</strong> qoʻshiladi — shuning uchun テスト, uch zarb.</p>",
    },
    {
        "text": "<p><strong>ファ</strong> qanday yasalgan?</p>",
        "choices": ["フ + kichik ァ", "ハ + kichik ァ", "フ + katta ア", "ヒ + kichik ャ"],
        "correct": "フ + kichik ァ",
        "explanation": "<p><strong>フ</strong> [«fu»] ning unlisi oʻchirilib, "
                       "<strong>kichik ァ</strong> bilan almashtiriladi: «f» + «a» = "
                       "fa. Shu mantiq bilan ティ, ディ, シェ va boshqalarni ham "
                       "oʻzingiz oʻqiy olasiz.</p>",
    },
    {
        "text": "<p>«Dilnoza» ismidagi «l» tovushiga nima boʻladi?</p>",
        "choices": ["Tushib qoladi", "ラ-qatoriga aylanadi", "ン ga aylanadi",
                    "Oʻzgarishsiz qoladi"],
        "correct": "ラ-qatoriga aylanadi",
        "explanation": "<p>Yapon tilida <strong>l tovushi yoʻq</strong> — u doim "
                       "ラ-qatoriga aylanadi. Shuning uchun «Dilnoza» → "
                       "<strong>ディルノザ</strong>, di-ru-no-za.</p>",
    },
    {
        "text": "<p>«Oʻzbekiston» katakanada qanday yoziladi?</p>",
        "choices": ["ウズベキスタン", "ウズベキスタヌ", "ウヅベキスタン", "オズベキスタン"],
        "correct": "ウズベキスタン",
        "explanation": "<p><strong>ウズベキスタン</strong> — u-zu-be-ki-su-ta-n, yetti "
                       "zarb. Oxirgi yolgʻiz «n» uchun <strong>ン</strong> ishlatiladi — "
                       "bu yagona undosh, unga unli qoʻshilmaydi. «zu» uchun ズ yoziladi, "
                       "ヅ emas.</p>",
    },
    {
        "text": "<p><strong>ファ</strong> va <strong>フア</strong> orasida qanday farq bor?</p>",
        "choices": ["Hech qanday", "ファ bitta zarb (fa), フア ikki zarb (fu-a)",
                    "フア bitta zarb, ファ ikki zarb", "Biri eski, biri yangi shakl"],
        "correct": "ファ bitta zarb (fa), フア ikki zarb (fu-a)",
        "explanation": "<p><strong>Kattaligi maʼno beradi.</strong> Kichik ァ oldingi "
                       "belgiga qoʻshilib bitta tovush yasaydi; katta ア esa alohida "
                       "belgi va oʻz zarbini oladi. Xuddi きゃ / きや kabi.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>ノート</strong></p>",
        "choices": ["noto", "nōto", "nooto", "nouto"],
        "correct": "nōto",
        "explanation": "<p><strong>[nōto]</strong> — daftar. ー oldingi «o» ni "
                       "uzaytiradi, oxirgi «t» ga esa «o» qoʻshilgan. Uch zarb: "
                       "no · o · to.</p>",
    },
    {
        "text": "<p>Yapon tilida «v» tovushi uchun odatda nima ishlatiladi?</p>",
        "choices": ["Doim ヴ", "Koʻpincha バ-qatori, ヴ kamroq",
                    "ワ-qatori", "Bunday tovush yozilmaydi"],
        "correct": "Koʻpincha バ-qatori, ヴ kamroq",
        "explanation": "<p><strong>ヴ</strong> belgisi bor (ウ + dakuten), lekin yaponlar "
                       "odatda バ-qatorini afzal koʻradi: «violin» koʻpincha "
                       "<strong>バイオリン</strong> deb yoziladi.</p>",
    },
    {
        "text": "<p>Nega chet soʻzlar yaponchada uzunroq eshitiladi?</p>",
        "choices": ["Yaponlar sekin gapiradi",
                    "Har bir yolgʻiz undoshga unli qoʻshiladi, shuning uchun zarblar koʻpayadi",
                    "Katakana belgilari uzun",
                    "Chet soʻzlarga doim ー qoʻshiladi"],
        "correct": "Har bir yolgʻiz undoshga unli qoʻshiladi, shuning uchun zarblar koʻpayadi",
        "explanation": "<p>Yapon tovush tizimi tor: yolgʻiz undosh boʻlmaydi. Shuning "
                       "uchun «test» bir boʻgʻindan <strong>uch zarbga</strong> "
                       "aylanadi. Bu buzilish emas, moslashish — oʻzbek tili ham "
                       "«Tokyo» ni «Tokio» deb oladi.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>スーパー</strong></p>",
        "choices": ["supa", "sūpā", "suupaa", "supaa"],
        "correct": "sūpā",
        "explanation": "<p><strong>[sūpā]</strong> — doʻkon. Ikkita ー, ikkita uzun unli. "
                       "Toʻrt zarb: su · u · pa · a.</p>",
    },
    {
        "text": "<p>Qaysi gap <strong>notoʻgʻri</strong>?</p>",
        "choices": ["ー oldingi unlini uzaytiradi",
                    "ー zarb sanalmaydi",
                    "Chet el ismlari katakanada yoziladi",
                    "Yapon tilida l tovushi yoʻq"],
        "correct": "ー zarb sanalmaydi",
        "explanation": "<p>Bu — <strong>notoʻgʻri</strong>. <strong>ー toʻliq bitta zarb "
                       "sanaladi</strong>, xuddi ん va kichik ッ kabi. Shuning uchun "
                       "コーヒー toʻrt zarbdan iborat. Qolgan uchtasi toʻgʻri.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PJ-7 Mashq: Katakana 1 — ア-ソ",
        "description": "12 savol — birinchi 15 katakana belgisi, ikkita alifboning vazifasi va tarixi.",
        "tutorial":    "PJ-7:",
        "level":       "easy",
        "questions":   Q_PJ7,
    },
    {
        "title":       "PJ-8 Mashq: Katakana 2 — タ-ン va chalgʻituvchi juftliklar",
        "description": "12 savol — qolgan 31 belgi, シ/ツ va ソ/ン yoʻnalish qoidasi, dakuten.",
        "tutorial":    "PJ-8:",
        "level":       "easy",
        "questions":   Q_PJ8,
    },
    {
        "title":       "PJ-9 Mashq: Uzun unlilar ー va chet soʻzlar",
        "description": "12 savol — ー va mora hisobi, chet soʻz moslashuvi, ファ/ティ birikmalari.",
        "tutorial":    "PJ-9:",
        "level":       "easy",
        "questions":   Q_PJ9,
    },
]
