# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-4 … PJ-6 (yozuv bloki, hiragananing oxiri).

12 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PJ_PRACTICE.md · lesson list in toc_pj_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_04_06.py --master=prime \\
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
# PJ-4 — Hiragana 3: ま-ん
# =====================================================================

Q_PJ4 = [
    {
        "text": "<p>Bu belgi qanday oʻqiladi?</p><p><strong>む</strong></p>",
        "choices": ["mu", "nu", "ma", "me"],
        "correct": "mu",
        "explanation": "<p><strong>mu</strong> — ま-qatorining u-katagi. Bu qatorda hech "
                       "qanday istisno yoʻq: qanday yozilsa, shunday oʻqiladi.</p>",
    },
    {
        "text": "<p>Bu belgi qanday oʻqiladi?</p><p><strong>を</strong></p>",
        "choices": ["wo", "o", "wa", "n"],
        "correct": "o",
        "explanation": "<p><strong>[o]</strong>. «wo» — bu belgining eski nomi va uni "
                       "kompyuterda yozish usuli, lekin bugungi yapon tilida u sof "
                       "<strong>o</strong> deb aytiladi. を soʻz ichida hech qachon "
                       "ishlatilmaydi — u faqat grammatik qoʻshimcha.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>くるま</strong></p>",
        "choices": ["kuruma", "kurruma", "kuluma", "kumura"],
        "correct": "kuruma",
        "explanation": "<p><strong>kuruma</strong> — mashina. る dagi <strong>r</strong> "
                       "oʻzbekcha «r» emas: til tanglayga <em>bir marta</em> yengil urib "
                       "oʻtadi, titramaydi. «kurrruma» — eng koʻp uchraydigan xato.</p>",
    },
    {
        "text": "<p>Nega や-qatorida faqat uchta belgi bor?</p>",
        "choices": ["Qolganlari yoʻqolib ketgan",
                    "«yi» va «ye» tovushlari yapon tilida mavjud emas",
                    "Ular katakanada yoziladi",
                    "Ularni faqat bolalar ishlatadi"],
        "correct": "«yi» va «ye» tovushlari yapon tilida mavjud emas",
        "explanation": "<p>Jadvaldagi boʻshliq <strong>tilning oʻzidagi boʻshliqni</strong> "
                       "koʻrsatadi: «yi» va «ye» tovushlari yapon tilida yoʻq, shuning uchun "
                       "ular uchun belgi ham yoʻq. や-qatorida faqat や, ゆ, よ bor.</p>",
    },
    {
        "text": "<p>«sora» (osmon) soʻzi hiraganada qanday yoziladi?</p>",
        "choices": ["そら", "さら", "そろ", "しら"],
        "correct": "そら",
        "explanation": "<p><strong>そら</strong> — so + ra. さら boʻlsa «sara» (likopcha), "
                       "そろ boʻlsa «soro» boʻlib qoladi.</p>",
    },
    {
        "text": "<p><strong>にほん</strong> soʻzida nechta zarb (mora) bor?</p>",
        "choices": ["Ikkita", "Uchta", "Toʻrtta", "Bitta"],
        "correct": "Uchta",
        "explanation": "<p><strong>Uchta</strong>: に · ほ · ん. <strong>ん toʻliq bitta "
                       "zarb sanaladi</strong> — bu yapon ritmining asosiy qoidasi. Uni "
                       "oldingi boʻgʻinga qoʻshib yubormang.</p>",
    },
    {
        "text": "<p>Quyidagilardan qaysi biri <strong>ん</strong> haqida toʻgʻri?</p>",
        "choices": ["Soʻz boshida kela oladi",
                    "Hech qachon soʻz boshida kelmaydi",
                    "Faqat katakanada ishlatiladi",
                    "Unli tovush beradi"],
        "correct": "Hech qachon soʻz boshida kelmaydi",
        "explanation": "<p>Yaponchada <strong>ん bilan boshlanadigan soʻz yoʻq</strong>. "
                       "ん — alifbodagi yagona belgi, u unlisiz; shuning uchun u doim "
                       "boshqa boʻgʻindan keyin turadi.</p>",
    },
    {
        "text": "<p><strong>り</strong> va <strong>い</strong> ni qanday farqlaysiz?</p>",
        "choices": ["り da nuqta bor",
                    "い ikkita qisqa alohida chiziq, り ning oʻng chizigʻi uzun va pastga egiladi",
                    "い kattaroq yoziladi",
                    "Hech qanday farq yoʻq"],
        "correct": "い ikkita qisqa alohida chiziq, り ning oʻng chizigʻi uzun va pastga egiladi",
        "explanation": "<p><strong>Uzunligiga qarang.</strong> い — ikkita qisqa, bir-biridan "
                       "ajralgan chiziq. り — oʻng chizigʻi uzun va pastga egilib ketadi. "
                       "Bu ikkalasi eng koʻp adashtiriladigan juftlik.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>こんにちは</strong></p>",
        "choices": ["konnichiha", "konnichiwa", "konichiwa", "konnitiha"],
        "correct": "konnichiwa",
        "explanation": "<p><strong>konnichiwa</strong> — kunduzgi salom. Oxiridagi "
                       "<strong>は</strong> [wa] deb oʻqiladi, chunki u grammatik "
                       "qoʻshimcha. Ichidagi <strong>ち</strong> esa «chi» — «ti» emas.</p>",
    },
    {
        "text": "<p><strong>を</strong> qayerda ishlatiladi?</p>",
        "choices": ["Soʻzlarning ichida, お oʻrniga",
                    "Faqat grammatik qoʻshimcha sifatida",
                    "Faqat ismlarni yozishda",
                    "Soʻz boshida"],
        "correct": "Faqat grammatik qoʻshimcha sifatida",
        "explanation": "<p>を <strong>hech qachon soʻz ichida ishlatilmaydi</strong>. Uning "
                       "bitta vazifasi bor: toʻldiruvchini belgilash — oʻzbekchadagi "
                       "<em>-ni</em> qoʻshimchasi kabi. を ni koʻrsangiz, bu soʻz emas, "
                       "grammatika.</p>",
    },
    {
        "text": "<p><strong>め</strong> va <strong>ぬ</strong> ni nima ajratadi?</p>",
        "choices": ["ぬ ning dumi halqa hosil qiladi, め da halqa yoʻq",
                    "め ning dumi halqa hosil qiladi, ぬ da halqa yoʻq",
                    "ぬ ikkita chiziqdan, め uchtadan iborat",
                    "Faqat kattaligi bilan"],
        "correct": "ぬ ning dumi halqa hosil qiladi, め da halqa yoʻq",
        "explanation": "<p><strong>Halqani qidiring.</strong> ぬ ning dumi oʻralib halqa "
                       "yasaydi; め da dum shunchaki chiqib ketadi. Xuddi shu usul る "
                       "(halqali) va ろ (halqasiz) ni ham ajratadi.</p>",
    },
    {
        "text": "<p>Qaysi oʻqilish <strong>notoʻgʻri</strong>?</p>",
        "choices": ["やま = yama", "ゆき = yuki", "そら = sora", "を = wo"],
        "correct": "を = wo",
        "explanation": "<p><strong>を «wo» emas — [o]</strong>. Qolgan uchtasi toʻgʻri: やま "
                       "(togʻ), ゆき (qor), そら (osmon).</p>",
    },
]


# =====================================================================
# PJ-5 — Hiragana 4: butun jadval, uzun unlilar, mora
# =====================================================================

Q_PJ5 = [
    {
        "text": "<p><strong>せんせい</strong> soʻzining oxiri qanday talaffuz qilinadi?</p>",
        "choices": ["Uzun e — [sensē]", "Alohida i bilan — [sen-se-i]",
                    "Uzun i — [sensī]", "Qisqa e, keyin urgʻuli i"],
        "correct": "Uzun e — [sensē]",
        "explanation": "<p><strong>えい</strong> birikmasi ikkita alohida unli emas, "
                       "<strong>uzun e</strong> beradi: [sensē]. Lotin yozuvida bu soʻz "
                       "odatda «sensei» deb yoziladi — yozilishi shunday, lekin "
                       "<em>talaffuzi</em> uzun e. Bu — boshlovchilar eng koʻp adashadigan "
                       "uzun unli.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>おはよう</strong></p>",
        "choices": ["ohayou", "ohayō", "ohaiyo", "ohayo u"],
        "correct": "ohayō",
        "explanation": "<p><strong>[ohayō]</strong> — xayrli tong. <strong>おう</strong> "
                       "birikmasi uzun <strong>o</strong> beradi, «yo-u» emas.</p>",
    },
    {
        "text": "<p><strong>おかあさん</strong> soʻzida nechta zarb (mora) bor?</p>",
        "choices": ["Toʻrtta", "Beshta", "Uchta", "Oltita"],
        "correct": "Beshta",
        "explanation": "<p><strong>Beshta</strong>: お · か · あ · さ · ん. Uzun unlining "
                       "ikkinchi qismi (あ) ham, <strong>ん</strong> ham toʻliq bitta zarb "
                       "sanaladi — ikkalasi ham hisobga kiradi.</p>",
    },
    {
        "text": "<p><strong>ゆき</strong> va <strong>ゆうき</strong> orasida qanday farq bor?</p>",
        "choices": ["Faqat yozilishi, maʼnosi bir xil",
                    "Unli uzunligi — va maʼnosi butunlay boshqa: qor va jasorat",
                    "Biri hiragana, biri katakana",
                    "Biri eski, biri yangi shakl"],
        "correct": "Unli uzunligi — va maʼnosi butunlay boshqa: qor va jasorat",
        "explanation": "<p>Yapon tilida <strong>unli uzunligi maʼnoni oʻzgartiradi</strong>. "
                       "<strong>ゆき</strong> — qor (ikki zarb), <strong>ゆうき</strong> — "
                       "jasorat (uch zarb). Uzun unlini haqiqatan ham ikki barobar uzoq "
                       "ushlang.</p>",
    },
    {
        "text": "<p>五十音図 jadvalidagi <strong>ustunlar</strong> nimani bildiradi?</p>",
        "choices": ["Undoshlarni", "Unlilarni — a, i, u, e, o",
                    "Soʻz turkumlarini", "Yozuv tizimlarini"],
        "correct": "Unlilarni — a, i, u, e, o",
        "explanation": "<p><strong>Unlilarni.</strong> Tepadagi qator — beshta unli, "
                       "chapdagi ustun — undosh. Har bir katak ularning kesishmasi: "
                       "«k» qatori × «a» ustuni = か.</p>",
    },
    {
        "text": "<p>Yapon tilida zarblar (mora) uzunligi qanday?</p>",
        "choices": ["Urgʻuli boʻgʻin uzunroq aytiladi",
                    "Hammasi teng — soʻz sanagandek, tekis aytiladi",
                    "Birinchi zarb doim uzun",
                    "Oxirgi zarb doim qisqa"],
        "correct": "Hammasi teng — soʻz sanagandek, tekis aytiladi",
        "explanation": "<p><strong>Hammasi teng.</strong> Oʻzbek tilidan farqli oʻlaroq, "
                       "birorta boʻgʻin urgʻu bilan choʻzilmaydi. Aynan shuning uchun "
                       "yaponcha gapirayotgan odam <em>tekis</em> eshitiladi.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>とおる</strong></p>",
        "choices": ["toru", "tōru", "tooru", "toolu"],
        "correct": "tōru",
        "explanation": "<p><strong>[tōru]</strong> — oʻtib ketmoq. Ketma-ket kelgan "
                       "<strong>おお</strong> uzun o beradi. Uch zarb: と · お · る.</p>",
    },
    {
        "text": "<p>Yapon grammatikasi 五十音図 jadvali bilan qanday bogʻliq?</p>",
        "choices": ["Hech qanday bogʻliqligi yoʻq",
                    "Feʼl tuslanganda oxirgi boʻgʻin shu qator ichida siljiydi",
                    "Jadval faqat lugʻat tartibi uchun kerak",
                    "Jadval faqat bolalar uchun"],
        "correct": "Feʼl tuslanganda oxirgi boʻgʻin shu qator ichida siljiydi",
        "explanation": "<p>Bu jadval shunchaki oʻrganish vositasi emas. Feʼl tuslanganda "
                       "uning oxirgi boʻgʻini <strong>shu qator ichida yuqoriga yoki "
                       "pastga siljiydi</strong>: よむ → よみます, yaʼni む dan み ga. "
                       "PJ-27 da butun tizim ochiladi.</p>",
    },
    {
        "text": "<p>Qaysi juftlik uzun <strong>e</strong> tovushini beradi?</p>",
        "choices": ["えい", "えう", "えお", "えあ"],
        "correct": "えい",
        "explanation": "<p><strong>えい</strong> — uzun e. Xuddi shunday <strong>おう</strong> "
                       "uzun o beradi. Bu ikkalasi eng koʻp uchraydigan uzun unli "
                       "juftliklari va ikkalasi ham «i» yoki «u» kabi alohida "
                       "aytilmaydi.</p>",
    },
    {
        "text": "<p>Nima uchun yaponcha matnda soʻz chegarasini topish qiyin?</p>",
        "choices": ["Harflar juda kichik",
                    "Soʻzlar orasida boʻshliq qoʻyilmaydi",
                    "Matn oʻngdan chapga oʻqiladi",
                    "Har bir soʻz bitta belgi bilan yoziladi"],
        "correct": "Soʻzlar orasida boʻshliq qoʻyilmaydi",
        "explanation": "<p><strong>Boʻshliq yoʻq.</strong> Aynan shuning uchun kanji kerak: "
                       "kanji va hiragananing almashinuvi soʻz chegarasini koʻrsatib "
                       "beradi. Faqat kana bilan yozilgan uzun gap shuning uchun "
                       "oʻqishga ogʻir.</p>",
    },
    {
        "text": "<p>Qaysi oʻqilish <strong>notoʻgʻri</strong>?</p>",
        "choices": ["おはよう = ohayō", "ゆうき = yuki",
                    "やま = yama", "こころ = kokoro"],
        "correct": "ゆうき = yuki",
        "explanation": "<p><strong>ゆうき «yuki» emas — [yūki]</strong> (jasorat). うう uzun "
                       "u beradi, shuning uchun bu soʻz uch zarbdan iborat. «yuki» — bu "
                       "<strong>ゆき</strong>, qor. Qolgan uchtasi toʻgʻri.</p>",
    },
    {
        "text": "<p>Yaponcha oʻqishni tezlashtirish uchun eng samarali usul qaysi?</p>",
        "choices": ["Har bir belgini alohida yodlab chiqish",
                    "Kuniga bir oz, muntazam ovoz chiqarib oʻqish",
                    "Faqat lotin yozuvida oʻqish",
                    "Bir kunda butun jadvalni koʻchirib yozish"],
        "correct": "Kuniga bir oz, muntazam ovoz chiqarib oʻqish",
        "explanation": "<p><strong>Muntazamlik</strong> hal qiladi, hajm emas. Ovoz chiqarib "
                       "oʻqish koʻz va quloqni bir vaqtda oʻrgatadi, shuning uchun u "
                       "jimgina oʻqishdan samaraliroq. Maqsad — belgini emas, "
                       "<em>butun soʻzni</em> bir qarashda koʻrish.</p>",
    },
]


# =====================================================================
# PJ-6 — Dakuten, handakuten, yōon, sokuon
# =====================================================================

Q_PJ6 = [
    {
        "text": "<p><strong>か</strong> ga dakuten (゛) qoʻyilsa nima boʻladi?</p>",
        "choices": ["が", "ぱ", "きゃ", "っか"],
        "correct": "が",
        "explanation": "<p><strong>が</strong> [ga]. Dakuten — ikkita tirnoq — jarangsiz "
                       "undoshni jaranglashtiradi: <strong>k → g</strong>, s → z, "
                       "t → d, h → b.</p>",
    },
    {
        "text": "<p>Handakuten (゜) qaysi qatorga qoʻyiladi?</p>",
        "choices": ["か-qatoriga", "さ-qatoriga", "は-qatoriga", "た-qatoriga"],
        "correct": "は-qatoriga",
        "explanation": "<p>Faqat <strong>は-qatoriga</strong>, va <strong>p</strong> "
                       "tovushini beradi: は → ぱ, ひ → ぴ, ふ → ぷ. Shunday qilib は "
                       "qatori uch xil boʻladi: sof (は), tirnoqli (ば), doirali (ぱ).</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>きって</strong></p>",
        "choices": ["kite", "kitte", "kitsute", "kiyte"],
        "correct": "kitte",
        "explanation": "<p><strong>[kitte]</strong> — pochta markasi. Kichik "
                       "<strong>っ</strong> keyingi undoshni ikkilantiradi va oʻzi bir "
                       "zarblik <em>jimlik</em>. <strong>きて</strong> [kite] esa «kel» — "
                       "butunlay boshqa soʻz.</p>",
    },
    {
        "text": "<p><strong>きょう</strong> soʻzida nechta zarb (mora) bor?</p>",
        "choices": ["Bitta", "Ikkita", "Uchta", "Toʻrtta"],
        "correct": "Ikkita",
        "explanation": "<p><strong>Ikkita</strong>: kyo + o. <strong>Kichik ょ oʻz zarbini "
                       "olmaydi</strong> — u き ga qoʻshilib bitta tovush yasaydi. Uni "
                       "«ki-yo-u» deb uch zarbda aytish — eng koʻp uchraydigan xato.</p>",
    },
    {
        "text": "<p>Bu birikma qanday oʻqiladi?</p><p><strong>しゃ</strong></p>",
        "choices": ["shiya", "sha", "sya", "sha i"],
        "correct": "sha",
        "explanation": "<p><strong>sha</strong>. し allaqachon «shi» boʻlgani uchun, unga "
                       "kichik ゃ qoʻshilganda «shya» emas, sodda <strong>sha</strong> "
                       "chiqadi. Xuddi shunday ちゃ = «cha», じゃ = «ja».</p>",
    },
    {
        "text": "<p>Yozayotganda [ji] tovushi uchun qaysi belgini tanlaysiz?</p>",
        "choices": ["Deyarli doim じ", "Deyarli doim ぢ",
                    "Ikkalasi teng ishlatiladi", "し + dakuten emas, boshqa belgi"],
        "correct": "Deyarli doim じ",
        "explanation": "<p><strong>じ</strong>. ぢ juda kam uchraydi — faqat ち dan yasalgan "
                       "soʻz qoʻshilganda yoki ち takrorlanganda. Shubhalansangiz じ yozing "
                       "va deyarli har doim toʻgʻri boʻlasiz. Xuddi shu qoida ず va づ "
                       "uchun ham ishlaydi.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>がっこう</strong></p>",
        "choices": ["gakou", "gakkō", "gatsukou", "gakkou"],
        "correct": "gakkō",
        "explanation": "<p><strong>[gakkō]</strong> — maktab. Ikkita narsa bir soʻzda: "
                       "kichik <strong>っ</strong> keyingi k ni ikkilantiradi, "
                       "<strong>こう</strong> esa uzun o beradi. Toʻrt zarb: が · っ · こ · う.</p>",
    },
    {
        "text": "<p>Kichik <strong>っ</strong> ning oʻz tovushi bormi?</p>",
        "choices": ["Ha, «tsu» deb oʻqiladi",
                    "Yoʻq — u bir zarblik jimlik, keyingi undoshni ikkilantiradi",
                    "Ha, «t» deb oʻqiladi",
                    "Yoʻq, va u zarb ham sanalmaydi"],
        "correct": "Yoʻq — u bir zarblik jimlik, keyingi undoshni ikkilantiradi",
        "explanation": "<p>っ ning <strong>oʻz tovushi yoʻq</strong>, lekin u "
                       "<strong>toʻliq bitta zarb</strong> sanaladi: ogʻiz keyingi tovushga "
                       "tayyorlanib toʻxtab turadi. Toʻxtashni tashlab ketsangiz, boshqa "
                       "soʻz chiqadi.</p>",
    },
    {
        "text": "<p><strong>しんぶん</strong> soʻzidagi ん qanday eshitiladi?</p>",
        "choices": ["[n] — oʻzgarmaydi", "[m] — chunki keyin b keladi",
                    "[ng] — burun orqali", "Umuman eshitilmaydi"],
        "correct": "[m] — chunki keyin b keladi",
        "explanation": "<p><strong>[shimbun]</strong>. ん tovushi keyingi harfga moslashadi: "
                       "<strong>b, p yoki m dan oldin u [m] boʻlib chiqadi</strong>, chunki "
                       "ogʻiz allaqachon shu tovushga tayyorlanadi. Buni atayin qilish "
                       "shart emas — oʻzi shunday chiqadi.</p>",
    },
    {
        "text": "<p><strong>きゃ</strong> va <strong>きや</strong> orasida qanday farq bor?</p>",
        "choices": ["Hech qanday farq yoʻq",
                    "きゃ bitta zarb (kya), きや ikki zarb (ki-ya)",
                    "きや bitta zarb, きゃ ikki zarb",
                    "Biri hiragana, biri katakana"],
        "correct": "きゃ bitta zarb (kya), きや ikki zarb (ki-ya)",
        "explanation": "<p><strong>Kattaligi maʼno beradi.</strong> Kichik ゃ oldingi "
                       "belgiga qoʻshilib <strong>bitta</strong> tovush yasaydi; katta や "
                       "esa alohida belgi va oʻz zarbini oladi. Qoʻlda yozganda kichikni "
                       "haqiqatan kichik yozing.</p>",
    },
    {
        "text": "<p>Qaysi oʻqilish <strong>notoʻgʻri</strong>?</p>",
        "choices": ["みず = mizu", "でんしゃ = densha",
                    "きょう = kiyou", "ざっし = zasshi"],
        "correct": "きょう = kiyou",
        "explanation": "<p><strong>きょう «kiyou» emas — [kyō]</strong>, ikki zarb. Kichik "
                       "ょ alohida aytilmaydi, う esa uzun o yasaydi. Qolgan uchtasi "
                       "toʻgʻri.</p>",
    },
    {
        "text": "<p>Qaysi gap <strong>toʻgʻri</strong>?</p>",
        "choices": ["Dakuten har qanday belgiga qoʻyilishi mumkin",
                    "Dakuten faqat か, さ, た va は qatorlariga qoʻyiladi",
                    "Dakuten unlilarga qoʻyiladi",
                    "Dakuten belgining tovushini uzaytiradi"],
        "correct": "Dakuten faqat か, さ, た va は qatorlariga qoʻyiladi",
        "explanation": "<p>Dakuten <strong>jarangsiz undoshni jaranglashtiradi</strong>, "
                       "shuning uchun u faqat jarangsiz juftligi bor qatorlarda ishlaydi: "
                       "か→が, さ→ざ, た→だ, は→ば. Unlilarga yoki な, ま, ら qatorlariga "
                       "qoʻyilmaydi — ular allaqachon jarangli.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PJ-4 Mashq: Hiragana 3 — ま-ん",
        "description": "12 savol — ま, や, ら va わ qatorlari, yaponcha r, を va ん ning qoidalari.",
        "tutorial":    "PJ-4:",
        "level":       "easy",
        "questions":   Q_PJ4,
    },
    {
        "title":       "PJ-5 Mashq: Hiragana 4 — butun 五十音図 ni oʻqish",
        "description": "12 savol — jadvalning mantiqi, uzun unlilar (えい, おう) va mora hisobi.",
        "tutorial":    "PJ-5:",
        "level":       "easy",
        "questions":   Q_PJ5,
    },
    {
        "title":       "PJ-6 Mashq: Dakuten, handakuten, yōon va sokuon",
        "description": "12 savol — ゛va ゜, じ/ぢ va ず/づ, kichik ゃゅょ hamda kichik っ.",
        "tutorial":    "PJ-6:",
        "level":       "easy",
        "questions":   Q_PJ6,
    },
]
