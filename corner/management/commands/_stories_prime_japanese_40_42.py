# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-40 … PJ-42.

⚠️ PJ-40 dan boshlab bular DIALOG emas, HIKOYA: hikoyachi bor, kichik voqea
bor, dialog esa faqat ziravor (2-4 qator). Toc shuni talab qiladi.

PJ-40 taklif · PJ-41 ことができます · PJ-42 potensial shakl.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_40_42.py --author=prime
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
        "title":   "まつりへ いきませんか",
        "summary": (
            "PJ-40 matni — shelfdagi birinchi haqiqiy hikoya. Rano yozgi "
            "bayramga taklif qiladi, reja tuziladi, va bir kishi kela olmaydi."
        ),
        "order":   40,
        "grammar": [
            {
                "pattern":  "〜ませんか",
                "meaning":  "«…maysizmi?» — taklif. Shakli inkor, maʼnosi "
                            "taklif; suhbatdoshga «yoʻq» uchun joy qoldiradi.",
                "examples": ["<ruby>祭<rt>まつ</rt></ruby>りへ<ruby>行<rt>い</rt></ruby>きませんか。"],
            },
            {
                "pattern":  "〜ましょう",
                "meaning":  "«…aylik». Rozilikdan keyin reja tuzish uchun. "
                            "Oʻzbekcha «-aylik» ning oʻzi.",
                "examples": ["<ruby>六時<rt>ろくじ</rt></ruby>に<ruby>会<rt>あ</rt></ruby>いましょう。"],
            },
            {
                "pattern":  "〜ましょうか",
                "meaning":  "«Men …ayinmi?» — birga emas, oʻzim yordam "
                            "berishni taklif qilish.",
                "examples": ["<ruby>持<rt>も</rt></ruby>ちましょうか。"],
            },
        ],
        "body": '''<p><ruby>八月<rt>はちがつ</rt></ruby>の<ruby>金曜日<rt>きんようび</rt></ruby>でした。<ruby>町<rt>まち</rt></ruby>に<span class="cn-word" data-tr="bayram"><ruby>祭<rt>まつ</rt></ruby>り</span>のポスターがありました。ラノさんはポスターを<ruby>見<rt>み</rt></ruby>てから、<ruby>友<rt>とも</rt></ruby>だちに<span class="cn-word" data-tr="telefon qildi"><ruby>電話<rt>でんわ</rt></ruby>しました</span>。</p>

<p><strong>ラノ:</strong> みなさん、<ruby>土曜日<rt>どようび</rt></ruby>に<ruby>一緒<rt>いっしょ</rt></ruby>に<ruby>祭<rt>まつ</rt></ruby>りへ<ruby>行<rt>い</rt></ruby>きませんか。</p>

<p>ムニラさんとイノムさんは「いいですね」と<ruby>言<rt>い</rt></ruby>いました。<ruby>三人<rt>さんにん</rt></ruby>は<span class="cn-word" data-tr="reja"><ruby>予定<rt>よてい</rt></ruby></span>を<ruby>作<rt>つく</rt></ruby>りました。<ruby>六時<rt>ろくじ</rt></ruby>に<ruby>駅<rt>えき</rt></ruby>で<ruby>会<rt>あ</rt></ruby>いましょう、と<ruby>決<rt>き</rt></ruby>めました。</p>

<p>でもイムロンさんは<ruby>行<rt>い</rt></ruby>きませんでした。<span class="cn-word" data-tr="yarim kunlik ish">アルバイト</span>がありました。「すみません、ちょっと…」と<ruby>言<rt>い</rt></ruby>いました。ラノさんは<span class="cn-word" data-tr="xafa boʻldi"><ruby>残念<rt>ざんねん</rt></ruby>でした</span>。</p>

<p><ruby>土曜日<rt>どようび</rt></ruby>の<ruby>夕方<rt>ゆうがた</rt></ruby>、<ruby>駅<rt>えき</rt></ruby>に<ruby>人<rt>ひと</rt></ruby>がたくさんいました。ムニラさんは<span class="cn-word" data-tr="katta sumka"><ruby>大<rt>おお</rt></ruby>きいかばん</span>を<ruby>持<rt>も</rt></ruby>っていました。</p>

<p><strong>イノム:</strong> <ruby>持<rt>も</rt></ruby>ちましょうか。</p>

<p><strong>ムニラ:</strong> はい、お<ruby>願<rt>ねが</rt></ruby>いします。</p>

<p><ruby>祭<rt>まつ</rt></ruby>りで<ruby>三人<rt>さんにん</rt></ruby>は<span class="cn-word" data-tr="tushlik">たこ<ruby>焼<rt>や</rt></ruby>き</span>を<ruby>食<rt>た</rt></ruby>べたり、<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>ったりしました。<ruby>九時<rt>くじ</rt></ruby>に<span class="cn-word" data-tr="olovbozlik"><ruby>花火<rt>はなび</rt></ruby></span>を<ruby>見<rt>み</rt></ruby>ました。とても<ruby>楽<rt>たの</rt></ruby>しかったです。</p>

<p><ruby>家<rt>いえ</rt></ruby>へ<ruby>帰<rt>かえ</rt></ruby>ってから、ラノさんはイムロンさんに<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>見<rt>み</rt></ruby>せました。「<ruby>来年<rt>らいねん</rt></ruby>は<ruby>一緒<rt>いっしょ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きましょう。」</p>''',
        "questions": [
            {
                "text": "ラノさんはポスターを<ruby>見<rt>み</rt></ruby>てから<ruby>何<rt>なに</rt></ruby>をしましたか。",
                "choices": [
                    "<ruby>駅<rt>えき</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きました",
                    "<ruby>友<rt>とも</rt></ruby>だちに<ruby>電話<rt>でんわ</rt></ruby>しました",
                    "<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>りました",
                    "アルバイトへ<ruby>行<rt>い</rt></ruby>きました",
                ],
                "answer": 1,
                "explanation": "«ポスターを 見てから、友だちに 電話しました» — plakatni "
                               "koʻrgach, doʻstlariga qoʻngʻiroq qildi va taklif "
                               "qildi.",
            },
            {
                "text": "イノムさんの「<ruby>持<rt>も</rt></ruby>ちましょうか」nima maʼnoni beradi?",
                "choices": [
                    "Birga koʻtaraylik",
                    "Men koʻtarib berayinmi?",
                    "Koʻtaring, iltimos",
                    "Koʻtarish mumkin emas",
                ],
                "answer": 1,
                "explanation": "ましょう<strong>か</strong> — birga emas, "
                               "<strong>oʻzim</strong> qilishni taklif qilish. "
                               "Munira «お願いします» deb rozi boʻldi.",
            },
            {
                "text": "イムロンさんはなぜ<ruby>行<rt>い</rt></ruby>きませんでしたか。",
                "choices": [
                    "<ruby>祭<rt>まつ</rt></ruby>りが<ruby>好<rt>す</rt></ruby>きではありませんから",
                    "アルバイトがありましたから",
                    "<ruby>駅<rt>えき</rt></ruby>が<ruby>遠<rt>とお</rt></ruby>いですから",
                    "<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>りましたから",
                ],
                "answer": 1,
                "explanation": "«アルバイトが ありました» — ishi bor edi. Rad javobini "
                               "esa toʻgʻridan-toʻgʻri aytmadi: "
                               "<strong>«すみません、ちょっと…»</strong> — gap "
                               "tugatilmaydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "ピアノを ひくことが できます",
        "summary": (
            "PJ-41 matni. Maktabda konsert boʻladi va har kim nimani "
            "uddalashini aytadi. 〜ことができます va 〜ができます yonma-yon."
        ),
        "order":   41,
        "grammar": [
            {
                "pattern":  "Lugʻat shakli + ことができます",
                "meaning":  "«…ish mumkin». Feʼl umuman tuslanmaydi — shuning "
                            "uchun uchala guruh ham bir xil.",
                "examples": ["ピアノを<ruby>弾<rt>ひ</rt></ruby>くことができます。"],
            },
            {
                "pattern":  "OT + ができます",
                "meaning":  "Koʻnikma oti bilan こと kerak emas: til, musiqa "
                            "asbobi, sport.",
                "examples": ["<ruby>日本語<rt>にほんご</rt></ruby>ができます。"],
            },
            {
                "pattern":  "〜が<ruby>上手<rt>じょうず</rt></ruby>／<ruby>下手<rt>へた</rt></ruby>",
                "meaning":  "«Mohir» va «uquvsiz» — な-sifat, が oladi. "
                            "上手 ni OʻZINGIZ haqingizda ishlatmang.",
                "examples": ["<ruby>料理<rt>りょうり</rt></ruby>が<ruby>上手<rt>じょうず</rt></ruby>です。"],
            },
        ],
        "body": '''<p><ruby>来月<rt>らいげつ</rt></ruby><ruby>学校<rt>がっこう</rt></ruby>で<span class="cn-word" data-tr="konsert">コンサート</span>があります。やまだ<ruby>先生<rt>せんせい</rt></ruby>は<ruby>教室<rt>きょうしつ</rt></ruby>で<ruby>言<rt>い</rt></ruby>いました。「みなさん、<ruby>何<rt>なに</rt></ruby>ができますか。」</p>

<p>パリさんは<span class="cn-word" data-tr="qoʻlini koʻtardi"><ruby>手<rt>て</rt></ruby>を<ruby>上<rt>あ</rt></ruby>げました</span>。</p>

<p><strong>パリ:</strong> <ruby>私<rt>わたし</rt></ruby>はピアノを<span class="cn-word" data-tr="chalmoq"><ruby>弾<rt>ひ</rt></ruby>く</span>ことができます。でも<ruby>下手<rt>へた</rt></ruby>です。</p>

<p>やまだ<ruby>先生<rt>せんせい</rt></ruby>は<ruby>笑<rt>わら</rt></ruby>いました。パリさんは<ruby>八年<rt>はちねん</rt></ruby><span class="cn-word" data-tr="mashq qildi"><ruby>練習<rt>れんしゅう</rt></ruby>しました</span>。クラスの<ruby>人<rt>ひと</rt></ruby>はみんな<ruby>知<rt>し</rt></ruby>っていました。</p>

<p>ムニラさんは<ruby>料理<rt>りょうり</rt></ruby>が<span class="cn-word" data-tr="mohir"><ruby>上手<rt>じょうず</rt></ruby></span>です。でもコンサートで<ruby>料理<rt>りょうり</rt></ruby>することができません。イノムさんは<ruby>歌<rt>うた</rt></ruby>うことができません。<ruby>泳<rt>およ</rt></ruby>ぐことができますが、コンサートにプールがありません。</p>

<p><strong>やまだ:</strong> イムロンさんは<ruby>何<rt>なに</rt></ruby>ができますか。</p>

<p><strong>イムロン:</strong> <ruby>私<rt>わたし</rt></ruby>は<ruby>日本語<rt>にほんご</rt></ruby>ができます。<ruby>日本<rt>にほん</rt></ruby>の<ruby>歌<rt>うた</rt></ruby>を<span class="cn-word" data-tr="tarjima qilmoq"><ruby>訳<rt>やく</rt></ruby>す</span>ことができます。</p>

<p><ruby>先生<rt>せんせい</rt></ruby>は「いいですね」と<ruby>言<rt>い</rt></ruby>いました。パリさんはピアノを<ruby>弾<rt>ひ</rt></ruby>きます。イムロンさんは<ruby>歌<rt>うた</rt></ruby>の<ruby>言葉<rt>ことば</rt></ruby>を<ruby>作<rt>つく</rt></ruby>ります。ムニラさんとイノムさんは<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>ります。</p>

<p><ruby>四人<rt>よにん</rt></ruby>は<ruby>毎日<rt>まいにち</rt></ruby><ruby>練習<rt>れんしゅう</rt></ruby>しました。</p>''',
        "questions": [
            {
                "text": "パリさんは<ruby>何<rt>なに</rt></ruby>ができますか。",
                "choices": [
                    "<ruby>料理<rt>りょうり</rt></ruby>することができます",
                    "ピアノを<ruby>弾<rt>ひ</rt></ruby>くことができます",
                    "<ruby>歌<rt>うた</rt></ruby>うことができます",
                    "<ruby>泳<rt>およ</rt></ruby>ぐことができます",
                ],
                "answer": 1,
                "explanation": "«ピアノを 弾くことが できます» — sakkiz yil mashq "
                               "qilgan. Ovqat pishirishga mohiri Munira, suza "
                               "oladigani esa Inom.",
            },
            {
                "text": "なぜイムロンさんは「<ruby>日本語<rt>にほんご</rt></ruby>ができます」と<ruby>言<rt>い</rt></ruby>いましたか、「<ruby>日本語<rt>にほんご</rt></ruby>をできます」と<ruby>言<rt>い</rt></ruby>いませんか。",
                "choices": [
                    "できます が oladi, を emas",
                    "日本語 uzun soʻz boʻlgani uchun",
                    "Gap savol boʻlgani uchun",
                    "を faqat odamlar bilan ishlatilgani uchun",
                ],
                "answer": 0,
                "explanation": "できます — 好き va ほしい kabi <strong>holat</strong> "
                               "bildiradi, ish emas. Holat gapida narsa ega boʻlib "
                               "turadi va <strong>が</strong> oladi.",
            },
            {
                "text": "パリさんはなぜ「<ruby>下手<rt>へた</rt></ruby>です」と<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "Chunki haqiqatan ham yomon chaladi",
                    "Chunki oʻzi haqida 上手 deyish maqtanchoqlik boʻlardi",
                    "Chunki pianino eski edi",
                    "Chunki oʻqituvchi shuni soʻradi",
                ],
                "answer": 1,
                "explanation": "Sakkiz yil mashq qilgan va butun sinf buni biladi — "
                               "demak yomon chalmaydi. Yaponchada oʻzi haqida "
                               "<strong>上手</strong> deyish maqtanchoqlik boʻlib "
                               "eshitiladi; kamtarlik bu yerda odat emas, qoida.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "いまは およげます",
        "summary": (
            "PJ-42 matni. Inom suzishni oʻrganadi — bir yozda 'suza "
            "olmayman' dan 'suza olaman' gacha. Potensial shakl butun "
            "matnni tashiydi."
        ),
        "order":   42,
        "grammar": [
            {
                "pattern":  "I guruh: う qatori → え qatori + る",
                "meaning":  "Potensial shakl. Oxirgi tovush え qatoriga "
                            "koʻtariladi: ぐ → げ, む → め, す → せ.",
                "examples": ["<ruby>泳<rt>およ</rt></ruby>ぐ → <ruby>泳<rt>およ</rt></ruby>げる",
                             "<ruby>読<rt>よ</rt></ruby>む → <ruby>読<rt>よ</rt></ruby>める"],
            },
            {
                "pattern":  "II guruh: る → られる · III: できる",
                "meaning":  "II guruhda られる, する esa できる boʻladi — "
                            "oʻtgan darsdan tanish feʼl.",
                "examples": ["<ruby>食<rt>た</rt></ruby>べる → <ruby>食<rt>た</rt></ruby>べられる"],
            },
            {
                "pattern":  "Toʻldiruvchi が oladi",
                "meaning":  "Potensial gapda を emas, が. Imkoniyat — holat, "
                            "ish emas: 好き, ほしい, できる bilan bir qatorda.",
                "examples": ["<ruby>本<rt>ほん</rt></ruby>が<ruby>読<rt>よ</rt></ruby>めます。"],
            },
        ],
        "body": '''<p><ruby>去年<rt>きょねん</rt></ruby>の<ruby>夏<rt>なつ</rt></ruby>、イノムさんは<ruby>泳<rt>およ</rt></ruby>ぐことができませんでした。<ruby>友<rt>とも</rt></ruby>だちは<ruby>海<rt>うみ</rt></ruby>で<ruby>泳<rt>およ</rt></ruby>いだり、<ruby>遊<rt>あそ</rt></ruby>んだりしました。イノムさんは<span class="cn-word" data-tr="qirgʻoq"><ruby>岸<rt>きし</rt></ruby></span>で<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みました。</p>

<p><strong>イムロン:</strong> イノムさん、<ruby>一緒<rt>いっしょ</rt></ruby>に<ruby>泳<rt>およ</rt></ruby>ぎませんか。</p>

<p><strong>イノム:</strong> すみません、ちょっと…。<ruby>私<rt>わたし</rt></ruby>は<ruby>泳<rt>およ</rt></ruby>げません。</p>

<p><ruby>九月<rt>くがつ</rt></ruby>にイノムさんはプールへ<ruby>行<rt>い</rt></ruby>きました。<span class="cn-word" data-tr="oʻqituvchi ayol"><ruby>先生<rt>せんせい</rt></ruby></span>は「<ruby>大丈夫<rt>だいじょうぶ</rt></ruby>です」と<ruby>言<rt>い</rt></ruby>いました。イノムさんは<ruby>毎週<rt>まいしゅう</rt></ruby><span class="cn-word" data-tr="mashq qildi"><ruby>練習<rt>れんしゅう</rt></ruby>しました</span>。<ruby>十月<rt>じゅうがつ</rt></ruby>に<ruby>五<rt>ご</rt></ruby>メートル<ruby>泳<rt>およ</rt></ruby>げました。<ruby>十二月<rt>じゅうにがつ</rt></ruby>に<ruby>五十<rt>ごじゅう</rt></ruby>メートル<ruby>泳<rt>およ</rt></ruby>げました。</p>

<p><ruby>今年<rt>ことし</rt></ruby>の<ruby>夏<rt>なつ</rt></ruby>、<ruby>四人<rt>よにん</rt></ruby>はまた<ruby>海<rt>うみ</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きました。イノムさんは<span class="cn-word" data-tr="suza oldi"><ruby>泳<rt>およ</rt></ruby>げました</span>。<ruby>遠<rt>とお</rt></ruby>い<ruby>所<rt>ところ</rt></ruby>まで<ruby>泳<rt>およ</rt></ruby>げました。</p>

<p><strong>イムロン:</strong> すごいですね。<ruby>去年<rt>きょねん</rt></ruby>は<ruby>泳<rt>およ</rt></ruby>げませんでした。</p>

<p><strong>イノム:</strong> はい。でも<ruby>今<rt>いま</rt></ruby>は<ruby>海<rt>うみ</rt></ruby>が<span class="cn-word" data-tr="yoqadi"><ruby>好<rt>す</rt></ruby>き</span>です。</p>

<p><ruby>夕方<rt>ゆうがた</rt></ruby>、<ruby>四人<rt>よにん</rt></ruby>は<ruby>岸<rt>きし</rt></ruby>で<span class="cn-word" data-tr="quyosh botishi"><ruby>夕日<rt>ゆうひ</rt></ruby></span>を<ruby>見<rt>み</rt></ruby>ました。イノムさんは<ruby>本<rt>ほん</rt></ruby>を<ruby>持<rt>も</rt></ruby>っていませんでした。</p>''',
        "questions": [
            {
                "text": "<ruby>去年<rt>きょねん</rt></ruby>の<ruby>夏<rt>なつ</rt></ruby>、イノムさんは<ruby>海<rt>うみ</rt></ruby>で<ruby>何<rt>なに</rt></ruby>をしましたか。",
                "choices": [
                    "<ruby>泳<rt>およ</rt></ruby>ぎました",
                    "<ruby>岸<rt>きし</rt></ruby>で<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みました",
                    "<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>りました",
                    "プールへ<ruby>行<rt>い</rt></ruby>きました",
                ],
                "answer": 1,
                "explanation": "«イノムさんは 岸で 本を 読みました» — suza olmagani "
                               "uchun qirgʻoqda kitob oʻqidi. Basseynga esa "
                               "sentabrda bordi.",
            },
            {
                "text": "「<ruby>泳<rt>およ</rt></ruby>げません」va「<ruby>泳<rt>およ</rt></ruby>ぐことができません」— farqi nima?",
                "choices": [
                    "Maʼnosi bir xil; birinchisi qisqa, kundalik nutqda koʻproq",
                    "Birinchisi oʻtgan zamon",
                    "Birinchisi kuchliroq inkor",
                    "Ikkinchisi notoʻgʻri"],
                "answer": 0,
                "explanation": "Matnda ikkalasi ham bor va maʼnosi bir xil. Potensial "
                               "shakl kundalik nutqda, <strong>ことができます</strong> "
                               "esa rasmiy tilda va eʼlonlarda koʻproq uchraydi.",
            },
            {
                "text": "Matnning oxirgi gapi nimani bildiradi?",
                "choices": [
                    "Kitobini uyda unutgan edi",
                    "Endi qirgʻoqda oʻtirib kitob oʻqishi shart emas — u suzadi",
                    "Kitob oʻqishni yoqtirmay qoldi",
                    "Kitobini doʻstiga bergan edi",
                ],
                "answer": 1,
                "explanation": "Oʻtgan yozda kitob uning <em>suza olmaganini</em> "
                               "bildirar edi. Bu yil kitob yoʻq — chunki endi u "
                               "suvda. Hikoya buni aytmaydi, koʻrsatadi.",
            },
        ],
    },
]
