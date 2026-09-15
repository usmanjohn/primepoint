# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-67 … PJ-69.

Hikoyachi 普通体 da (PJ-45 dan beri), qoʻshtirnoq ichi です・ます ni
saqlaydi.

Shakl navbati: 67 — sport kuni hikoyasi, 68 — birinchi ish kuni
(xatolar orqali oʻrganish), 69 — doʻkondagi sahna. Oldingi batchda
omadsiz kun / oilaviy suhbat / orqaga qarash boʻlgan edi.

⚠️ CUMULATIVE: 67 da keigo yoʻq; 68 da 尊敬語 maxsus feʼllari yoʻq —
u dars faqat TUSHUNCHAni beradi, shakllar PJ-69 da.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_67_69.py --author=prime
"""

SUBJECT = {
    "name":    "Japanese",
    "summary": "Yapon tili: hikoyalar, lugʻat va oʻqish matnlari.",
    "icon":    "bi-brilliance",
    "color":   "#be123c",
}

COLLECTION = {
    "title":       "Prime Japanese Readings",
    "description": (
        "Prime Japanese darslarining oʻqish matnlari — har biri oʻz darsining "
        "grammatikasini matn ichida koʻrsatadi. Furigana, lugʻat izohlari va audio bilan."
    ),
    "order": 7,
}

STORIES = [
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "がんばれ",
        "summary": (
            "PJ-67 matni. Maktab sport kuni — buyruq shakli bu yerda "
            "qoʻpol emas, chunki u maydonda va belgilarda turadi, "
            "odamga qaratilmagan."
        ),
        "order":   67,
        "grammar": [
            {
                "pattern":  "<ruby>命令形<rt>めいれいけい</rt></ruby>",
                "meaning":  "I guruh え-qatorga tushadi, II guruh ろ "
                            "oladi, 来る → 来い. Belgida va baqiriqda "
                            "toʻgʻri, odamga aytilmaydi.",
                "examples": ["<ruby>頑張<rt>がんば</rt></ruby>れ！", "<ruby>走<rt>はし</rt></ruby>れ！"],
            },
            {
                "pattern":  "<ruby>禁止形<rt>きんしけい</rt></ruby>",
                "meaning":  "Lugʻat shakli + な, istisnosiz. "
                            "Ogohlantirish belgilarida uchraydi.",
                "examples": ["<ruby>入<rt>はい</rt></ruby>るな。", "<ruby>触<rt>さわ</rt></ruby>るな。"],
            },
            {
                "pattern":  "〜なさい",
                "meaning":  "ます-oʻzagi + なさい — qatʼiy, lekin "
                            "qoʻpol emas. Ustozdan oʻquvchiga.",
                "examples": ["<ruby>並<rt>なら</rt></ruby>びなさい。"],
            },
        ],
        "body": '''<p><ruby>十月<rt>じゅうがつ</rt></ruby>の<ruby>土曜日<rt>どようび</rt></ruby>、<span class="cn-word" data-tr="sport kuni"><ruby>体育祭<rt>たいいくさい</rt></ruby></span>があった。<ruby>朝<rt>あさ</rt></ruby>から<ruby>空<rt>そら</rt></ruby>は<ruby>青<rt>あお</rt></ruby>かった。</p>

<p><ruby>校庭<rt>こうてい</rt></ruby>に<ruby>紙<rt>かみ</rt></ruby>が<ruby>三<rt>みっ</rt></ruby>つあった。<ruby>一<rt>ひと</rt></ruby>つ<ruby>目<rt>め</rt></ruby>に「<span class="cn-word" data-tr="toʻxta"><ruby>止<rt>と</rt></ruby>まれ</span>」。<ruby>二<rt>ふた</rt></ruby>つ<ruby>目<rt>め</rt></ruby>に「<ruby>入<rt>はい</rt></ruby>るな」。<ruby>三<rt>みっ</rt></ruby>つ<ruby>目<rt>め</rt></ruby>に「<ruby>走<rt>はし</rt></ruby>るな」。</p>

<p>イノムさんは<ruby>笑<rt>わら</rt></ruby>った。<ruby>体育祭<rt>たいいくさい</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>に「<ruby>走<rt>はし</rt></ruby>るな」の<ruby>紙<rt>かみ</rt></ruby>があった。それは<ruby>廊下<rt>ろうか</rt></ruby>の<ruby>紙<rt>かみ</rt></ruby>だった。</p>

<p><ruby>先生<rt>せんせい</rt></ruby>が<ruby>来<rt>き</rt></ruby>た。</p>

<p><strong>せんせい:</strong> みなさん、<ruby>並<rt>なら</rt></ruby>びなさい。<ruby>十時<rt>じゅうじ</rt></ruby>に<ruby>始<rt>はじ</rt></ruby>まります。</p>

<p><ruby>最後<rt>さいご</rt></ruby>の<ruby>種目<rt>しゅもく</rt></ruby>は<span class="cn-word" data-tr="estafeta">リレー</span>だった。ムニラさんのクラスは<ruby>三位<rt>さんい</rt></ruby>だった。パリさんが<ruby>最後<rt>さいご</rt></ruby>に<ruby>走<rt>はし</rt></ruby>った。</p>

<p><ruby>全員<rt>ぜんいん</rt></ruby>が<ruby>立<rt>た</rt></ruby>った。そして<ruby>同<rt>おな</rt></ruby>じ<ruby>言葉<rt>ことば</rt></ruby>を<ruby>叫<rt>さけ</rt></ruby>んだ。</p>

<p>「<span class="cn-word" data-tr="harakat qil!"><ruby>頑張<rt>がんば</rt></ruby>れ</span>！<ruby>走<rt>はし</rt></ruby>れ！」</p>

<p>この<ruby>言葉<rt>ことば</rt></ruby>は<ruby>命令形<rt>めいれいけい</rt></ruby>だ。<ruby>教室<rt>きょうしつ</rt></ruby>では<ruby>使<rt>つか</rt></ruby>わない。でも<ruby>校庭<rt>こうてい</rt></ruby>では<ruby>誰<rt>だれ</rt></ruby>も<span class="cn-word" data-tr="qoʻpol deb oʻylamaydi"><ruby>失礼<rt>しつれい</rt></ruby>だと<ruby>思<rt>おも</rt></ruby>わない</span>。</p>

<p>パリさんのクラスは<ruby>二位<rt>にい</rt></ruby>になった。パリさんは<ruby>倒<rt>たお</rt></ruby>れた。<ruby>六人<rt>ろくにん</rt></ruby>が<ruby>走<rt>はし</rt></ruby>った。</p>''',
        "questions": [
            {
                "text": "<ruby>校庭<rt>こうてい</rt></ruby>の<ruby>紙<rt>かみ</rt></ruby>にどんな<ruby>言葉<rt>ことば</rt></ruby>がありましたか。",
                "choices": [
                    "止まれ, 入るな, 走るな — buyruq va taqiq shakllari",
                    "Faqat muloyim iltimoslar",
                    "Oʻquvchilarning ismlari",
                    "Musobaqa jadvali",
                ],
                "answer": 0,
                "explanation": "Belgi <strong>qisqa</strong> boʻlishi kerak — "
                               "shuning uchun u buyruq va taqiq shakllarini "
                               "ishlatadi. Muloyim boʻlish uning vazifasi "
                               "emas.",
            },
            {
                "text": "<ruby>先生<rt>せんせい</rt></ruby>はなぜ「<ruby>並<rt>なら</rt></ruby>べ」ではなく「<ruby>並<rt>なら</rt></ruby>びなさい」と<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "Chunki 〜なさい qatʼiy, lekin qoʻpol emas — ustozdan oʻquvchiga",
                    "Chunki 並ぶ II guruh feʼli",
                    "Chunki oʻquvchilar koʻp edi",
                    "Chunki bu yozma nutq",
                ],
                "answer": 0,
                "explanation": "Zinapoya: <strong>命令形 → 〜なさい → "
                               "〜てください</strong>. Oʻqituvchi oʻrtadagi "
                               "pogʻonani tanladi.",
            },
            {
                "text": "«<ruby>頑張<rt>がんば</rt></ruby>れ！» nega qoʻpol emas?",
                "choices": [
                    "Chunki bu buyruq emas, quvvatlash — va maydonda hamma shunday baqiradi",
                    "Chunki 頑張る I guruh feʼli",
                    "Chunki u qisqa",
                    "Chunki oʻqituvchi ruxsat bergan",
                ],
                "answer": 0,
                "explanation": "Shakl bir xil, <strong>vazifasi</strong> "
                               "boshqa. Matn buni ochiq aytadi: 教室では "
                               "使わない。でも校庭では誰も失礼だと思わない。",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "はじめての アルバイト",
        "summary": (
            "PJ-68 matni. Ranoning birinchi ish kuni — u keigoni "
            "ikki marta xato ishlatadi, va xatolarning oʻzi darsning "
            "mavzusini koʻrsatadi: keigo muloyimlik emas, mavqe."
        ),
        "order":   68,
        "grammar": [
            {
                "pattern":  "<ruby>敬語<rt>けいご</rt></ruby> — uch tarmoq",
                "meaning":  "尊敬語 suhbatdoshni koʻtaradi, 謙譲語 meni "
                            "pasaytiradi, 丁寧語 butun gapga kiyim "
                            "beradi.",
                "examples": ["<ruby>丁寧語<rt>ていねいご</rt></ruby>: <ruby>食<rt>た</rt></ruby>べます"],
            },
            {
                "pattern":  "Oʻzingizga hurmat qoʻshilmaydi",
                "meaning":  "尊敬語 faqat boshqa odamning ishiga, "
                            "謙譲語 faqat mening ishimga qoʻyiladi.",
                "examples": ["<ruby>私<rt>わたし</rt></ruby>がいたします。"],
            },
            {
                "pattern":  "<ruby>内<rt>うち</rt></ruby> va <ruby>外<rt>そと</rt></ruby>",
                "meaning":  "Oʻz guruhingiz — ichkari. Mijoz — "
                            "tashqari. Shuning uchun oʻz boshligʻingizni "
                            "mijozga gapirganda pasaytirasiz.",
                "examples": ["<ruby>店長<rt>てんちょう</rt></ruby>はおりません。"],
            },
        ],
        "body": '''<p>ラノさんは<ruby>十一月<rt>じゅういちがつ</rt></ruby>から<span class="cn-word" data-tr="yarim kunlik ish">アルバイト</span>を<ruby>始<rt>はじ</rt></ruby>めた。<ruby>駅<rt>えき</rt></ruby>の<ruby>近<rt>ちか</rt></ruby>くの<ruby>本屋<rt>ほんや</rt></ruby>だった。</p>

<p><ruby>初日<rt>しょにち</rt></ruby>、<span class="cn-word" data-tr="doʻkon mudiri"><ruby>店長<rt>てんちょう</rt></ruby></span>が<ruby>三<rt>みっ</rt></ruby>つのことを<ruby>教<rt>おし</rt></ruby>えた。</p>

<p><strong>てんちょう:</strong> お<ruby>客<rt>きゃく</rt></ruby>さまには<ruby>敬語<rt>けいご</rt></ruby>を<ruby>使<rt>つか</rt></ruby>います。<ruby>敬語<rt>けいご</rt></ruby>は<span class="cn-word" data-tr="muloyimlik emas"><ruby>丁寧<rt>ていねい</rt></ruby>さではありません</span>。<ruby>位置<rt>いち</rt></ruby>です。</p>

<p>ラノさんは<ruby>分<rt>わ</rt></ruby>からなかった。でも<ruby>三日後<rt>みっかご</rt></ruby>に<ruby>分<rt>わ</rt></ruby>かった。</p>

<p><ruby>最初<rt>さいしょ</rt></ruby>の<ruby>失敗<rt>しっぱい</rt></ruby>。お<ruby>客<rt>きゃく</rt></ruby>さまに「<ruby>私<rt>わたし</rt></ruby>がいらっしゃいます」と<ruby>言<rt>い</rt></ruby>った。<ruby>店長<rt>てんちょう</rt></ruby>は<ruby>静<rt>しず</rt></ruby>かに<ruby>直<rt>なお</rt></ruby>した。</p>

<p><strong>てんちょう:</strong> それはお<ruby>客<rt>きゃく</rt></ruby>さまの<ruby>言葉<rt>ことば</rt></ruby>です。<ruby>自分<rt>じぶん</rt></ruby>には<ruby>使<rt>つか</rt></ruby>いません。</p>

<p><ruby>二<rt>ふた</rt></ruby>つ<ruby>目<rt>め</rt></ruby>の<ruby>失敗<rt>しっぱい</rt></ruby>は<ruby>電話<rt>でんわ</rt></ruby>だった。お<ruby>客<rt>きゃく</rt></ruby>さまが<ruby>店長<rt>てんちょう</rt></ruby>を<ruby>探<rt>さが</rt></ruby>していた。ラノさんは「<ruby>店長<rt>てんちょう</rt></ruby>はいらっしゃいません」と<ruby>答<rt>こた</rt></ruby>えた。</p>

<p><strong>てんちょう:</strong> <ruby>私<rt>わたし</rt></ruby>はラノさんの<ruby>内<rt>うち</rt></ruby>です。お<ruby>客<rt>きゃく</rt></ruby>さまは<ruby>外<rt>そと</rt></ruby>です。<ruby>外<rt>そと</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>と<ruby>話<rt>はな</rt></ruby>すとき、<ruby>内<rt>うち</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>を<ruby>下<rt>した</rt></ruby>げます。</p>

<p>ラノさんは<span class="cn-word" data-tr="daftariga yozdi"><ruby>手帳<rt>てちょう</rt></ruby>に<ruby>書<rt>か</rt></ruby>いた</span>。「<ruby>敬語<rt>けいご</rt></ruby>は<ruby>位置<rt>いち</rt></ruby>。<ruby>言葉<rt>ことば</rt></ruby>は<ruby>人<rt>ひと</rt></ruby>によって<ruby>変<rt>か</rt></ruby>わる。」</p>

<p><ruby>一<rt>いっ</rt></ruby>か<ruby>月後<rt>げつご</rt></ruby>、ラノさんは<ruby>間違<rt>まちが</rt></ruby>えなくなった。でも<span class="cn-word" data-tr="hali ham oʻylab turadi">まだ<ruby>考<rt>かんが</rt></ruby>えている</span>。<ruby>店長<rt>てんちょう</rt></ruby>は<ruby>考<rt>かんが</rt></ruby>えていない。</p>''',
        "questions": [
            {
                "text": "<ruby>店長<rt>てんちょう</rt></ruby>は<ruby>敬語<rt>けいご</rt></ruby>について<ruby>何<rt>なに</rt></ruby>と<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "Keigo muloyimlik emas, mavqe",
                    "Keigo juda qiyin",
                    "Keigo faqat telefonda kerak",
                    "Keigoni oʻrganish shart emas",
                ],
                "answer": 0,
                "explanation": "<strong>敬語は丁寧さではありません。位置です。</strong> "
                               "Bu butun blokning kaliti: keigo kim yuqorida "
                               "ekanini koʻrsatadi, muloyimlikni emas.",
            },
            {
                "text": "<ruby>最初<rt>さいしょ</rt></ruby>の<ruby>失敗<rt>しっぱい</rt></ruby>は<ruby>何<rt>なに</rt></ruby>でしたか。",
                "choices": [
                    "Oʻzi haqida 尊敬語 ishlatdi",
                    "Mijozga 謙譲語 ishlatdi",
                    "Oddiy shaklda gapirdi",
                    "Mudirning ismini unutdi",
                ],
                "answer": 0,
                "explanation": "«<strong>私がいらっしゃいます</strong>» — bu "
                               "mijozning soʻzi. 尊敬語 hech qachon oʻzingiz "
                               "haqingizda ishlatilmaydi.",
            },
            {
                "text": "<ruby>電話<rt>でんわ</rt></ruby>で<ruby>何<rt>なに</rt></ruby>が<ruby>間違<rt>まちが</rt></ruby>っていましたか。",
                "choices": [
                    "Oʻz mudirini mijozga gapirganda koʻtardi — uni pasaytirish kerak edi",
                    "Juda tez gapirdi",
                    "Mijozni pasaytirdi",
                    "Oddiy shaklda javob berdi",
                ],
                "answer": 0,
                "explanation": "Mudir — Ranoning <strong>内</strong>, mijoz "
                               "esa <strong>外</strong>. Tashqi odam bilan "
                               "gapirganda ichkaridagilar pasaytiriladi. "
                               "Doʻkon ichida esa いらっしゃいます toʻgʻri "
                               "boʻlardi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "おきゃくさまが いらっしゃる",
        "summary": (
            "PJ-69 matni. Bir soatlik doʻkon smenasi — 尊敬語 ning "
            "uchala yoʻli ham bitta matnda ishlaydi: maxsus feʼl, "
            "お〜になる qolipi va passiv shakl."
        ),
        "order":   69,
        "grammar": [
            {
                "pattern":  "Maxsus feʼllar",
                "meaning":  "いらっしゃる, 召し上がる, おっしゃる, なさる, "
                            "ご覧になる. ます shaklida り → い.",
                "examples": ["いらっしゃいませ。", "<ruby>何<rt>なに</rt></ruby>とおっしゃいましたか。"],
            },
            {
                "pattern":  "お + ます-oʻzak + になる",
                "meaning":  "Maxsus feʼli yoʻq feʼllar uchun mahsuldor "
                            "qolip. する va 来る uni olmaydi.",
                "examples": ["お<ruby>読<rt>よ</rt></ruby>みになりますか。",
                             "お<ruby>待<rt>ま</rt></ruby>ちになりました。"],
            },
            {
                "pattern":  "Passiv shakl = yengil hurmat",
                "meaning":  "PJ-63 dagi 受身形 keigoning eng oson "
                            "darajasi sifatida ham ishlaydi.",
                "examples": ["もう<ruby>帰<rt>かえ</rt></ruby>られました。"],
            },
        ],
        "body": '''<p><ruby>土曜日<rt>どようび</rt></ruby>の<ruby>午後<rt>ごご</rt></ruby>、<ruby>本屋<rt>ほんや</rt></ruby>は<ruby>込<rt>こ</rt></ruby>んでいた。ラノさんは<ruby>三時<rt>さんじ</rt></ruby>から<ruby>四時<rt>よじ</rt></ruby>まで<ruby>入口<rt>いりぐち</rt></ruby>に<ruby>立<rt>た</rt></ruby>っていた。</p>

<p><ruby>一人目<rt>ひとりめ</rt></ruby>は<ruby>年上<rt>としうえ</rt></ruby>の<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>だった。<ruby>料理<rt>りょうり</rt></ruby>の<ruby>本<rt>ほん</rt></ruby>を<ruby>探<rt>さが</rt></ruby>していた。</p>

<p><strong>ラノ:</strong> <span class="cn-word" data-tr="xush kelibsiz">いらっしゃいませ</span>。こちらをご<ruby>覧<rt>らん</rt></ruby>になりますか。</p>

<p><strong>おきゃくさま:</strong> はい。ありがとう。</p>

<p><ruby>二人目<rt>ふたりめ</rt></ruby>は<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>だった。<ruby>小<rt>ちい</rt></ruby>さい<ruby>声<rt>こえ</rt></ruby>で<ruby>何<rt>なに</rt></ruby>か<ruby>言<rt>い</rt></ruby>った。ラノさんは<ruby>聞<rt>き</rt></ruby>こえなかった。</p>

<p><strong>ラノ:</strong> すみません、<ruby>何<rt>なに</rt></ruby>とおっしゃいましたか。</p>

<p><ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>は<ruby>地図<rt>ちず</rt></ruby>の<ruby>本<rt>ほん</rt></ruby>を<ruby>探<rt>さが</rt></ruby>していた。ラノさんは<ruby>三階<rt>さんがい</rt></ruby>に<span class="cn-word" data-tr="olib chiqdi"><ruby>案内<rt>あんない</rt></ruby>した</span>。</p>

<p><ruby>三人目<rt>さんにんめ</rt></ruby>は<ruby>中学生<rt>ちゅうがくせい</rt></ruby>だった。<ruby>三十分<rt>さんじゅっぷん</rt></ruby><ruby>同<rt>おな</rt></ruby>じ<ruby>本<rt>ほん</rt></ruby>をお<ruby>読<rt>よ</rt></ruby>みになっていた。</p>

<p><ruby>四時<rt>よじ</rt></ruby>に<ruby>店長<rt>てんちょう</rt></ruby>が<ruby>来<rt>き</rt></ruby>た。</p>

<p><strong>てんちょう:</strong> <ruby>社長<rt>しゃちょう</rt></ruby>はもう<ruby>帰<rt>かえ</rt></ruby>られました。<ruby>今日<rt>きょう</rt></ruby>はどうでしたか。</p>

<p><strong>ラノ:</strong> <ruby>三人<rt>さんにん</rt></ruby>のお<ruby>客<rt>きゃく</rt></ruby>さまといらっしゃいました。<span class="cn-word" data-tr="ah, xato qildim">あ、<ruby>間違<rt>まちが</rt></ruby>えました</span>。<ruby>話<rt>はな</rt></ruby>しました。</p>

<p><ruby>店長<rt>てんちょう</rt></ruby>は<ruby>笑<rt>わら</rt></ruby>った。ラノさんは<ruby>自分<rt>じぶん</rt></ruby>で<ruby>気<rt>き</rt></ruby>がついた。<ruby>初<rt>はじ</rt></ruby>めてだった。</p>''',
        "questions": [
            {
                "text": "ラノさんは<ruby>一人目<rt>ひとりめ</rt></ruby>のお<ruby>客<rt>きゃく</rt></ruby>さまに<ruby>何<rt>なに</rt></ruby>と<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "こちらをご覧になりますか — «buni koʻrasizmi?»",
                    "こちらを見ますか",
                    "こちらを拝見しますか",
                    "こちらをお見になりますか",
                ],
                "answer": 0,
                "explanation": "<strong>ご覧になる</strong> — «koʻrmoq» ning "
                               "尊敬語 shakli. Mijozning ishi, demak uni "
                               "koʻtarish kerak.",
            },
            {
                "text": "«お<ruby>読<rt>よ</rt></ruby>みになっていた» qaysi yoʻl bilan yasalgan?",
                "choices": [
                    "お + ます-oʻzak + になる — mahsuldor qolip",
                    "Maxsus feʼl",
                    "Passiv shakl",
                    "Kauzativ shakl",
                ],
                "answer": 0,
                "explanation": "読む ning maxsus 尊敬語 feʼli yoʻq, shuning "
                               "uchun <strong>お読みになる</strong> qolipi "
                               "ishlatiladi. ます-oʻzagi — 読み.",
            },
            {
                "text": "ラノさんning oxirgi xatosi nima edi?",
                "choices": [
                    "Oʻzi haqida いらっしゃいました dedi — 尊敬語 oʻzingizga ishlatilmaydi",
                    "Mijozlar sonini notoʻgʻri aytdi",
                    "Mudirni pasaytirdi",
                    "Oddiy shaklda javob berdi",
                ],
                "answer": 0,
                "explanation": "U darrov sezdi va tuzatdi: <strong>話しました</strong>. "
                               "Mudir kulgani ham shundan — xatoni oʻzi "
                               "topgani birinchi marta edi.",
            },
        ],
    },
]
