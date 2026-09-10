# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-43 … PJ-45.

⚠️ PJ-45 dan boshlab HIKOYACHI oddiy shaklda gapiradi (普通体). Qoʻshtirnoq
   ichidagi nutq esa oʻz uslubini saqlaydi — odamlar baribir です・ます
   bilan gaplashadi. Toc shuni talab qiladi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_43_45.py --author=prime
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
        "title":   "ねこが さんびき",
        "summary": (
            "PJ-43 matni. Munira uyiga mushuk olib keladi — va sanoq "
            "soʻzlari butun matn boʻylab ishlaydi: 匹, 個, 本, 人."
        ),
        "order":   43,
        "grammar": [
            {
                "pattern":  "SON + <ruby>助数詞<rt>じょすうし</rt></ruby>",
                "meaning":  "Yaponchada narsa turiga qarab sanaladi: tirik "
                            "jonzot 匹, uzun narsa 本, kichik buyum 個.",
                "examples": ["<ruby>猫<rt>ねこ</rt></ruby>が<ruby>三匹<rt>さんびき</rt></ruby>います。"],
            },
            {
                "pattern":  "Tovush oʻzgarishi",
                "meaning":  "1, 6, 8, 10 kichik っ qoʻshadi; 3 va 何 は "
                            "qatorini jaranglashtiradi (は → ば).",
                "examples": ["<ruby>一匹<rt>いっぴき</rt></ruby> · <ruby>三匹<rt>さんびき</rt></ruby> · <ruby>何匹<rt>なんびき</rt></ruby>"],
            },
            {
                "pattern":  "Gapda joyi",
                "meaning":  "Sanoq soʻzi otdan keyin, feʼldan oldin turadi va "
                            "hech qanday qoʻshimcha olmaydi.",
                "examples": ["りんごを<ruby>三個<rt>さんこ</rt></ruby><ruby>買<rt>か</rt></ruby>いました。"],
            },
        ],
        "body": '''<p><ruby>先週<rt>せんしゅう</rt></ruby>の<ruby>日曜日<rt>にちようび</rt></ruby>、ムニラさんは<ruby>公園<rt>こうえん</rt></ruby>で<span class="cn-word" data-tr="mushukcha"><ruby>子猫<rt>こねこ</rt></ruby></span>を<ruby>見<rt>み</rt></ruby>ました。<ruby>一匹<rt>いっぴき</rt></ruby>ではありませんでした。<ruby>三匹<rt>さんびき</rt></ruby>いました。</p>

<p>ムニラさんは<ruby>家<rt>いえ</rt></ruby>へ<ruby>帰<rt>かえ</rt></ruby>ってから、<ruby>母<rt>はは</rt></ruby>に<ruby>電話<rt>でんわ</rt></ruby>しました。「<ruby>子猫<rt>こねこ</rt></ruby>が<ruby>三匹<rt>さんびき</rt></ruby>います。どうしましょうか。」</p>

<p><ruby>母<rt>はは</rt></ruby>は「<ruby>一匹<rt>いっぴき</rt></ruby>だけ」と<ruby>言<rt>い</rt></ruby>いました。ムニラさんは<span class="cn-word" data-tr="qora"><ruby>黒<rt>くろ</rt></ruby>い</span><ruby>子猫<rt>こねこ</rt></ruby>を<ruby>選<rt>えら</rt></ruby>びました。<ruby>名前<rt>なまえ</rt></ruby>はクロです。</p>

<p><ruby>月曜日<rt>げつようび</rt></ruby>にムニラさんは<ruby>店<rt>みせ</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きました。<span class="cn-word" data-tr="baliq"><ruby>魚<rt>さかな</rt></ruby></span>を<ruby>二匹<rt>にひき</rt></ruby>、<span class="cn-word" data-tr="tuxum"><ruby>卵<rt>たまご</rt></ruby></span>を<ruby>六個<rt>ろっこ</rt></ruby>、<span class="cn-word" data-tr="sut">ぎゅうにゅう</span>を<ruby>一本<rt>いっぽん</rt></ruby><ruby>買<rt>か</rt></ruby>いました。</p>

<p><ruby>教室<rt>きょうしつ</rt></ruby>でラノさんが<ruby>聞<rt>き</rt></ruby>きました。</p>

<p><strong>ラノ:</strong> <ruby>子猫<rt>こねこ</rt></ruby>は<ruby>何匹<rt>なんびき</rt></ruby>いますか。</p>

<p><strong>ムニラ:</strong> <ruby>一匹<rt>いっぴき</rt></ruby>です。でも<ruby>公園<rt>こうえん</rt></ruby>に<ruby>二匹<rt>にひき</rt></ruby>います。</p>

<p><ruby>次<rt>つぎ</rt></ruby>の<ruby>週<rt>しゅう</rt></ruby>、ラノさんとパリさんも<ruby>公園<rt>こうえん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きました。<ruby>今<rt>いま</rt></ruby>クロには<span class="cn-word" data-tr="doʻst"><ruby>友<rt>とも</rt></ruby>だち</span>が<ruby>二人<rt>ふたり</rt></ruby>います。<ruby>子猫<rt>こねこ</rt></ruby>も<ruby>二匹<rt>にひき</rt></ruby>あたらしい<ruby>家<rt>いえ</rt></ruby>を<span class="cn-word" data-tr="topdi"><ruby>見<rt>み</rt></ruby>つけました</span>。</p>''',
        "questions": [
            {
                "text": "<ruby>公園<rt>こうえん</rt></ruby>に<ruby>子猫<rt>こねこ</rt></ruby>が<ruby>何匹<rt>なんびき</rt></ruby>いましたか。",
                "choices": [
                    "<ruby>一匹<rt>いっぴき</rt></ruby>",
                    "<ruby>二匹<rt>にひき</rt></ruby>",
                    "<ruby>三匹<rt>さんびき</rt></ruby>",
                    "<ruby>六匹<rt>ろっぴき</rt></ruby>",
                ],
                "answer": 2,
                "explanation": "«一匹では ありませんでした。三匹 いました» — bitta emas, "
                               "uchta edi. Munira ulardan bittasini uyiga olib ketdi.",
            },
            {
                "text": "«<ruby>六個<rt>ろっこ</rt></ruby>» nega «ろくこ» emas?",
                "choices": [
                    "1, 6, 8, 10 kichik っ qoʻshadi",
                    "個 doim jaranglashadi",
                    "6 har doim tartibsiz",
                    "卵 sanaladigan narsa boʻlgani uchun",
                ],
                "answer": 0,
                "explanation": "か qatoridagi sanoq soʻzida 1, 6, 8, 10 sokuon oladi: "
                               "<strong>いっこ, ろっこ, はっこ, じゅっこ</strong>. "
                               "Jaranglashish esa faqat は qatorida boʻladi.",
            },
            {
                "text": "«ぎゅうにゅうを<ruby>一本<rt>いっぽん</rt></ruby>» — nega 本?",
                "choices": [
                    "Chunki sut kitob bilan sanaladi",
                    "Chunki shisha uzun narsa",
                    "Chunki sut suyuqlik",
                    "Chunki 本 hamma narsani sanaydi",
                ],
                "answer": 1,
                "explanation": "本 sanoq soʻzi sifatida <strong>uzun narsa</strong>ni "
                               "sanaydi — shisha, qalam, soyabon. «Kitob» degani emas: "
                               "kitob 冊 bilan sanaladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "どちらが たかいですか",
        "summary": (
            "PJ-44 matni. Imron velosiped tanlaydi — ikkitasini taqqoslaydi, "
            "keyin uchtasidan eng arzonini. より, のほうが va いちばん."
        ),
        "order":   44,
        "grammar": [
            {
                "pattern":  "A は B より SIFAT です",
                "meaning":  "より PAST tomonni belgilaydi. Sifat esa umuman "
                            "oʻzgarmaydi — oʻzbekcha «-roq» dan farqi shu.",
                "examples": ["この<ruby>自転車<rt>じてんしゃ</rt></ruby>はあの<ruby>自転車<rt>じてんしゃ</rt></ruby>より<ruby>高<rt>たか</rt></ruby>いです。"],
            },
            {
                "pattern":  "A と B と、どちらが〜ですか",
                "meaning":  "Ikki narsadan tanlash. 何 emas — u uchta va undan "
                            "koʻp narsa uchun. Javobda のほうが.",
                "examples": ["どちらが<ruby>安<rt>やす</rt></ruby>いですか。", "こちらのほうが<ruby>安<rt>やす</rt></ruby>いです。"],
            },
            {
                "pattern":  "〜の<ruby>中<rt>なか</rt></ruby>でいちばん〜",
                "meaning":  "Uch va undan koʻp narsa ichidan eng ustuni. "
                            "Sifat yana oʻzgarmaydi.",
                "examples": ["この<ruby>店<rt>みせ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>でいちばん<ruby>安<rt>やす</rt></ruby>いです。"],
            },
        ],
        "body": '''<p>イムロンさんは<span class="cn-word" data-tr="velosiped"><ruby>自転車<rt>じてんしゃ</rt></ruby></span>がほしかったです。<ruby>土曜日<rt>どようび</rt></ruby>にラノさんと<ruby>一緒<rt>いっしょ</rt></ruby>に<ruby>店<rt>みせ</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きました。</p>

<p><span class="cn-word" data-tr="doʻkon"><ruby>店<rt>みせ</rt></ruby></span>に<ruby>自転車<rt>じてんしゃ</rt></ruby>が<ruby>三台<rt>さんだい</rt></ruby>ありました。<ruby>赤<rt>あか</rt></ruby>いのと<ruby>青<rt>あお</rt></ruby>いのと<ruby>黒<rt>くろ</rt></ruby>いのです。</p>

<p><strong>ラノ:</strong> <ruby>赤<rt>あか</rt></ruby>いのと<ruby>青<rt>あお</rt></ruby>いのと、どちらが<ruby>好<rt>す</rt></ruby>きですか。</p>

<p><strong>イムロン:</strong> <ruby>青<rt>あお</rt></ruby>いほうが<ruby>好<rt>す</rt></ruby>きです。でも<ruby>赤<rt>あか</rt></ruby>いのより<span class="cn-word" data-tr="qimmat"><ruby>高<rt>たか</rt></ruby>い</span>です。</p>

<p><ruby>黒<rt>くろ</rt></ruby>い<ruby>自転車<rt>じてんしゃ</rt></ruby>はこの<ruby>店<rt>みせ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>でいちばん<ruby>安<rt>やす</rt></ruby>かったです。でもいちばん<ruby>古<rt>ふる</rt></ruby>かったです。イムロンさんは<span class="cn-word" data-tr="uzoq"><ruby>長<rt>なが</rt></ruby>い</span><ruby>時間<rt>じかん</rt></ruby><ruby>考<rt>かんが</rt></ruby>えました。</p>

<p><strong>ラノ:</strong> <ruby>青<rt>あお</rt></ruby>いのはいちばん<ruby>速<rt>はや</rt></ruby>いですよ。</p>

<p>イムロンさんは<ruby>青<rt>あお</rt></ruby>い<ruby>自転車<rt>じてんしゃ</rt></ruby>を<ruby>買<rt>か</rt></ruby>いました。<ruby>次<rt>つぎ</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>、<ruby>学校<rt>がっこう</rt></ruby>まで<ruby>十五分<rt>じゅうごふん</rt></ruby>で<ruby>行<rt>い</rt></ruby>けました。バスより<span class="cn-word" data-tr="tezroq"><ruby>速<rt>はや</rt></ruby>かった</span>です。</p>''',
        "questions": [
            {
                "text": "イムロンさんはどの<ruby>自転車<rt>じてんしゃ</rt></ruby>を<ruby>買<rt>か</rt></ruby>いましたか。",
                "choices": [
                    "<ruby>赤<rt>あか</rt></ruby>いの",
                    "<ruby>青<rt>あお</rt></ruby>いの",
                    "<ruby>黒<rt>くろ</rt></ruby>いの",
                    "<ruby>何<rt>なに</rt></ruby>も<ruby>買<rt>か</rt></ruby>いませんでした",
                ],
                "answer": 1,
                "explanation": "«青い自転車を 買いました» — koʻkini oldi. U eng arzoni "
                               "emas edi, lekin eng tezi edi.",
            },
            {
                "text": "«<ruby>青<rt>あお</rt></ruby>いのは<ruby>赤<rt>あか</rt></ruby>いのより<ruby>高<rt>たか</rt></ruby>いです» — qaysi biri qimmat?",
                "choices": [
                    "<ruby>青<rt>あお</rt></ruby>いの",
                    "<ruby>赤<rt>あか</rt></ruby>いの",
                    "Ikkalasi bir xil",
                    "Matnda aytilmagan",
                ],
                "answer": 0,
                "explanation": "<strong>より</strong> PAST tomonni belgilaydi — yaʼni "
                               "undan oldingi narsa arzonroq. Demak qimmati "
                               "<strong>青いの</strong>. Bu qolipdagi eng koʻp "
                               "uchraydigan xato — より ni teskari tushunish.",
            },
            {
                "text": "Nega ラノさん «どちらが» deb soʻradi, «<ruby>何<rt>なに</rt></ruby>が» emas?",
                "choices": [
                    "Chunki ikkitasidan tanlash kerak edi",
                    "Chunki velosiped haqida gap ketyapti",
                    "Chunki どちら muloyimroq",
                    "Chunki 何 faqat odamlar uchun",
                ],
                "answer": 0,
                "explanation": "<strong>どちら</strong> — ikki narsadan bittasi. "
                               "何 esa uchta va undan koʻp narsa uchun ishlatiladi. "
                               "Oxirida uchta velosiped taqqoslanganda «いちばん» "
                               "kelgan.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "にっき — はじめての でんしゃ",
        "summary": (
            "PJ-45 matni — shelfdagi birinchi 普通体 hikoya. Bu kundalik "
            "yozuvi, shuning uchun hikoyachi oddiy shaklda gapiradi; "
            "qoʻshtirnoq ichidagi nutq esa です・ます da qoladi."
        ),
        "order":   45,
        "grammar": [
            {
                "pattern":  "<ruby>普通体<rt>ふつうたい</rt></ruby> — feʼl",
                "meaning":  "行く · 行かない · 行った · 行かなかった. Bularning "
                            "uchtasi PJ-28, 34, 35 dan tanish; faqat "
                            "〜なかった yangi.",
                "examples": ["<ruby>朝<rt>あさ</rt></ruby><ruby>早<rt>はや</rt></ruby>く<ruby>起<rt>お</rt></ruby>きた。",
                             "<ruby>友<rt>とも</rt></ruby>だちは<ruby>来<rt>こ</rt></ruby>なかった。"],
            },
            {
                "pattern":  "だ · じゃない · だった",
                "meaning":  "です ning oddiy shakli. Faqat OT va な-sifat "
                            "bilan — い-sifatga だ qoʻshilmaydi.",
                "examples": ["<ruby>学生<rt>がくせい</rt></ruby>だ。", "<ruby>静<rt>しず</rt></ruby>かだった。"],
            },
            {
                "pattern":  "Qoʻshtirnoq oʻz uslubini saqlaydi",
                "meaning":  "Hikoyachi oddiy shaklda, lekin odamlar baribir "
                            "です・ます bilan gaplashadi.",
                "examples": ["「<ruby>大丈夫<rt>だいじょうぶ</rt></ruby>ですか」と<ruby>言<rt>い</rt></ruby>った。"],
            },
        ],
        "body": '''<p><ruby>四月<rt>しがつ</rt></ruby><ruby>十日<rt>とおか</rt></ruby>。<span class="cn-word" data-tr="havo"><ruby>天気<rt>てんき</rt></ruby></span>がよかった。</p>

<p><ruby>今日<rt>きょう</rt></ruby><ruby>初<rt>はじ</rt></ruby>めて<ruby>一人<rt>ひとり</rt></ruby>で<ruby>電車<rt>でんしゃ</rt></ruby>に<ruby>乗<rt>の</rt></ruby>った。<ruby>朝<rt>あさ</rt></ruby><ruby>六時<rt>ろくじ</rt></ruby><ruby>半<rt>はん</rt></ruby>に<ruby>起<rt>お</rt></ruby>きた。<ruby>母<rt>はは</rt></ruby>は<span class="cn-word" data-tr="hali">まだ</span><ruby>寝<rt>ね</rt></ruby>ていた。</p>

<p><ruby>駅<rt>えき</rt></ruby>は<ruby>静<rt>しず</rt></ruby>かじゃなかった。<ruby>人<rt>ひと</rt></ruby>がたくさんいた。<ruby>切符<rt>きっぷ</rt></ruby>を<ruby>買<rt>か</rt></ruby>うことができなかった。<span class="cn-word" data-tr="mashina">きかい</span>が<ruby>分<rt>わ</rt></ruby>からなかった。</p>

<p><ruby>後<rt>うし</rt></ruby>ろに<ruby>立<rt>た</rt></ruby>っていた<span class="cn-word" data-tr="ayol">おんな</span>の<ruby>人<rt>ひと</rt></ruby>が<ruby>手伝<rt>てつだ</rt></ruby>った。</p>

<p><strong>おんな:</strong> <ruby>大丈夫<rt>だいじょうぶ</rt></ruby>ですか。ここを<ruby>押<rt>お</rt></ruby>してください。</p>

<p><ruby>切符<rt>きっぷ</rt></ruby>を<ruby>買<rt>か</rt></ruby>ってから、<ruby>電車<rt>でんしゃ</rt></ruby>に<ruby>乗<rt>の</rt></ruby>った。<ruby>電車<rt>でんしゃ</rt></ruby>はバスより<ruby>速<rt>はや</rt></ruby>かった。<ruby>窓<rt>まど</rt></ruby>から<span class="cn-word" data-tr="daryo"><ruby>川<rt>かわ</rt></ruby></span>を<ruby>見<rt>み</rt></ruby>た。とてもきれいだった。</p>

<p><ruby>学校<rt>がっこう</rt></ruby>まで<ruby>二十分<rt>にじゅっぷん</rt></ruby>。バスは<ruby>四十分<rt>よんじゅっぷん</rt></ruby>。<ruby>明日<rt>あした</rt></ruby>も<ruby>電車<rt>でんしゃ</rt></ruby>で<ruby>行<rt>い</rt></ruby>く。</p>

<p><span class="cn-word" data-tr="qoʻrqinchli emas edi"><ruby>怖<rt>こわ</rt></ruby>くなかった</span>。</p>''',
        "questions": [
            {
                "text": "この<ruby>文<rt>ぶん</rt></ruby>はなぜ<ruby>普通体<rt>ふつうたい</rt></ruby>ですか。",
                "choices": [
                    "Chunki bu kundalik — oʻzi uchun yozilgan",
                    "Chunki yozuvchi bolakay",
                    "Chunki gaplar qisqa",
                    "Chunki bu oʻtgan zamon",
                ],
                "answer": 0,
                "explanation": "<strong>日記</strong> — kundalik. Unda hech kimga "
                               "murojaat qilinmaydi, shuning uchun muloyimlik ham "
                               "kerak emas. Kitob, gazeta va roman ham shu uslubda.",
            },
            {
                "text": "«<ruby>大丈夫<rt>だいじょうぶ</rt></ruby>ですか» — nega bu gap <ruby>丁寧体<rt>ていねいたい</rt></ruby> da?",
                "choices": [
                    "Chunki bu qoʻshtirnoq ichidagi nutq — odamlar bir-biriga muloyim gapiradi",
                    "Chunki bu savol",
                    "Chunki yozuvchi xato qilgan",
                    "Chunki 大丈夫 な-sifat",
                ],
                "answer": 0,
                "explanation": "Hikoyachi oddiy shaklda gapiradi, lekin "
                               "<strong>qoʻshtirnoq ichi oʻz uslubini saqlaydi</strong>. "
                               "Notanish odam bilan gaplashganda です・ます ishlatiladi.",
            },
            {
                "text": "«<ruby>静<rt>しず</rt></ruby>かじゃなかった» ning muloyim shakli qaysi?",
                "choices": [
                    "<ruby>静<rt>しず</rt></ruby>かではありませんでした",
                    "<ruby>静<rt>しず</rt></ruby>かではありません",
                    "<ruby>静<rt>しず</rt></ruby>かくなかったです",
                    "<ruby>静<rt>しず</rt></ruby>かでした",
                ],
                "answer": 0,
                "explanation": "静か — な-sifat, demak ot kabi tuslanadi. Oddiy "
                               "shakldagi <strong>じゃなかった</strong> muloyim "
                               "shaklda <strong>ではありませんでした</strong> boʻladi.",
            },
        ],
    },
]
