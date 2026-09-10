# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-25 … PJ-27.

PJ-25 い-sifatlar · PJ-26 な-sifatlar · PJ-27 uchta feʼl guruhi.
PJ-27 dan Block C boshlanadi — matn biroz uzunroq (70–130 soʻz).

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_25_27.py --author=prime
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
        "title":   "おおきい ねこと ちいさい ねこ",
        "summary": (
            "PJ-25 matni. Muniraning ikkita mushugi bor — biri katta, biri "
            "kichik. Butun matn い-sifatlar ustida turadi: kesim, inkor va "
            "oʻtgan zamon."
        ),
        "order":   25,
        "grammar": [
            {
                "pattern":  "い-sifat + です",
                "meaning":  "Sifat kesim boʻlib keladi. です faqat muloyimlik "
                            "uchun — u sifatga zamon bermaydi.",
                "examples": ["シロは<ruby>大<rt>おお</rt></ruby>きいです。",
                             "クロは<ruby>小<rt>ちい</rt></ruby>さいです。"],
            },
            {
                "pattern":  "い → くない",
                "meaning":  "い-sifatning inkori. Oxirgi い oʻrniga くない.",
                "examples": ["シロは<ruby>速<rt>はや</rt></ruby>くないです。"],
            },
            {
                "pattern":  "い → かった",
                "meaning":  "い-sifatning oʻtgan zamoni. «でした» EMAS — "
                            "zamonni sifatning oʻzi tashiydi.",
                "examples": ["とても<ruby>面白<rt>おもしろ</rt></ruby>かったです。"],
            },
            {
                "pattern":  "SIFAT + OT",
                "meaning":  "Sifat otga toʻgʻridan-toʻgʻri yopishadi, の siz.",
                "examples": ["<ruby>白<rt>しろ</rt></ruby>い<ruby>猫<rt>ねこ</rt></ruby> · <ruby>黒<rt>くろ</rt></ruby>い<ruby>猫<rt>ねこ</rt></ruby>"],
            },
        ],
        "body": '''<p>ムニラさんの<ruby>家<rt>いえ</rt></ruby>に<span class="cn-word" data-tr="mushuk"><ruby>猫<rt>ねこ</rt></ruby></span>がいます。<span class="cn-word" data-tr="ism"><ruby>名前<rt>なまえ</rt></ruby></span>はシロとクロです。</p>

<p><strong>ラノ:</strong> シロは<ruby>大<rt>おお</rt></ruby>きいですね。クロは<ruby>小<rt>ちい</rt></ruby>さいです。</p>

<p><strong>ムニラ:</strong> はい。シロは<span class="cn-word" data-tr="oq"><ruby>白<rt>しろ</rt></ruby>い</span><ruby>猫<rt>ねこ</rt></ruby>です。クロは<span class="cn-word" data-tr="qora"><ruby>黒<rt>くろ</rt></ruby>い</span><ruby>猫<rt>ねこ</rt></ruby>です。</p>

<p><strong>ラノ:</strong> クロは<span class="cn-word" data-tr="tez"><ruby>速<rt>はや</rt></ruby>い</span>ですか。</p>

<p><strong>ムニラ:</strong> とても<ruby>速<rt>はや</rt></ruby>いです。シロは<ruby>速<rt>はや</rt></ruby>くないです。シロは<ruby>毎日<rt>まいにち</rt></ruby><span class="cn-word" data-tr="koʻp">たくさん</span><ruby>食<rt>た</rt></ruby>べます。</p>

<p><strong>ラノ:</strong> <ruby>昨日<rt>きのう</rt></ruby>の<ruby>朝<rt>あさ</rt></ruby>、シロを<ruby>見<rt>み</rt></ruby>ました。とても<span class="cn-word" data-tr="qiziqarli edi"><ruby>面白<rt>おもしろ</rt></ruby>かった</span>です。</p>

<p><strong>ムニラ:</strong> シロはいい<ruby>猫<rt>ねこ</rt></ruby>です。クロもいい<ruby>猫<rt>ねこ</rt></ruby>です。</p>''',
        "questions": [
            {
                "text": "シロは どんな <ruby>猫<rt>ねこ</rt></ruby>ですか。",
                "choices": [
                    "<ruby>小<rt>ちい</rt></ruby>さい<ruby>黒<rt>くろ</rt></ruby>い<ruby>猫<rt>ねこ</rt></ruby>です",
                    "<ruby>大<rt>おお</rt></ruby>きい<ruby>白<rt>しろ</rt></ruby>い<ruby>猫<rt>ねこ</rt></ruby>です",
                    "<ruby>大<rt>おお</rt></ruby>きい<ruby>黒<rt>くろ</rt></ruby>い<ruby>猫<rt>ねこ</rt></ruby>です",
                    "<ruby>小<rt>ちい</rt></ruby>さい<ruby>白<rt>しろ</rt></ruby>い<ruby>猫<rt>ねこ</rt></ruby>です",
                ],
                "answer": 1,
                "explanation": "«シロは 大きいですね» va «シロは 白い猫です» — katta va oq. "
                               "Diqqat qiling: <strong>白い猫</strong> da の yoʻq — sifat "
                               "otga toʻgʻridan-toʻgʻri yopishadi.",
            },
            {
                "text": "シロは<ruby>速<rt>はや</rt></ruby>いですか。",
                "choices": [
                    "はい、とても<ruby>速<rt>はや</rt></ruby>いです",
                    "いいえ、<ruby>速<rt>はや</rt></ruby>くないです",
                    "いいえ、<ruby>速<rt>はや</rt></ruby>いではありません",
                    "はい、<ruby>速<rt>はや</rt></ruby>かったです",
                ],
                "answer": 1,
                "explanation": "«シロは 速くないです» — Shiro tez emas; tez yuradigani Kuro. "
                               "<strong>いいえ、速いではありません</strong> notoʻgʻri "
                               "yozilgan: い-sifatning inkori ではありません emas, "
                               "<strong>くない</strong>.",
            },
            {
                "text": "ラノさんは<ruby>昨日<rt>きのう</rt></ruby>の<ruby>朝<rt>あさ</rt></ruby>どう<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "とても<ruby>面白<rt>おもしろ</rt></ruby>いでした",
                    "とても<ruby>面白<rt>おもしろ</rt></ruby>いかったです",
                    "とても<ruby>面白<rt>おもしろ</rt></ruby>かったです",
                    "とても<ruby>面白<rt>おもしろ</rt></ruby>くでした",
                ],
                "answer": 2,
                "explanation": "い-sifatning oʻtgan zamoni: oxirgi い oʻrniga "
                               "<strong>かった</strong>. です oʻzgarmaydi — zamonni "
                               "sifat tashiydi. «面白いでした» eng koʻp uchraydigan xato.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "しずかな としょかん",
        "summary": (
            "PJ-26 matni. Inom har shanba kutubxonaga boradi. Matnda な-sifat "
            "uch holatda koʻrinadi: otdan oldin な bilan, kesim boʻlib な siz, "
            "va 〜が好きです qolipida."
        ),
        "order":   26,
        "grammar": [
            {
                "pattern":  "な-sifat + な + OT",
                "meaning":  "Otdan oldin turganda な-sifat な oladi.",
                "examples": ["<ruby>静<rt>しず</rt></ruby>かな<ruby>所<rt>ところ</rt></ruby>",
                             "<ruby>有名<rt>ゆうめい</rt></ruby>な<ruby>図書館<rt>としょかん</rt></ruby>"],
            },
            {
                "pattern":  "な-sifat + です / ではありません / でした",
                "meaning":  "Kesim boʻlganda な YOʻQOLADI va sifat ot kabi "
                            "tuslanadi — PJ-13 dagi qolipning oʻzi.",
                "examples": ["<ruby>図書館<rt>としょかん</rt></ruby>は<ruby>静<rt>しず</rt></ruby>かです。",
                             "<ruby>静<rt>しず</rt></ruby>かではありませんでした。"],
            },
            {
                "pattern":  "〜が<ruby>好<rt>す</rt></ruby>きです",
                "meaning":  "«… yoqadi». Yoqadigan narsa を emas, が oladi — "
                            "chunki 好き feʼl emas, sifat.",
                "examples": ["<ruby>数学<rt>すうがく</rt></ruby>が<ruby>好<rt>す</rt></ruby>きです。",
                             "<ruby>漢字<rt>かんじ</rt></ruby>は<ruby>好<rt>す</rt></ruby>きではありません。"],
            },
        ],
        "body": '''<p>イノムさんは<ruby>毎週<rt>まいしゅう</rt></ruby><ruby>土曜日<rt>どようび</rt></ruby>に<span class="cn-word" data-tr="kutubxona"><ruby>図書館<rt>としょかん</rt></ruby></span>へ<ruby>行<rt>い</rt></ruby>きます。<ruby>図書館<rt>としょかん</rt></ruby>は<span class="cn-word" data-tr="jimjit"><ruby>静<rt>しず</rt></ruby>か</span>です。<ruby>大<rt>おお</rt></ruby>きい<span class="cn-word" data-tr="bino"><ruby>建物<rt>たてもの</rt></ruby></span>です。</p>

<p><strong>パリ:</strong> イノムさん、ここは<span class="cn-word" data-tr="qulay"><ruby>便利<rt>べんり</rt></ruby></span>ですか。</p>

<p><strong>イノム:</strong> はい、とても<ruby>便利<rt>べんり</rt></ruby>です。<ruby>私<rt>わたし</rt></ruby>の<ruby>家<rt>いえ</rt></ruby>から<span class="cn-word" data-tr="yaqin"><ruby>近<rt>ちか</rt></ruby>い</span>です。</p>

<p><strong>パリ:</strong> <ruby>私<rt>わたし</rt></ruby>は<ruby>数学<rt>すうがく</rt></ruby>が<span class="cn-word" data-tr="yoqadigan"><ruby>好<rt>す</rt></ruby>き</span>です。イノムさんは<ruby>何<rt>なに</rt></ruby>が<ruby>好<rt>す</rt></ruby>きですか。</p>

<p><strong>イノム:</strong> <ruby>日本語<rt>にほんご</rt></ruby>が<ruby>好<rt>す</rt></ruby>きです。でも<span class="cn-word" data-tr="iyeroglif"><ruby>漢字<rt>かんじ</rt></ruby></span>は<ruby>好<rt>す</rt></ruby>きではありません。</p>

<p><strong>パリ:</strong> ここは<span class="cn-word" data-tr="mashhur"><ruby>有名<rt>ゆうめい</rt></ruby></span>な<ruby>図書館<rt>としょかん</rt></ruby>ですか。</p>

<p><strong>イノム:</strong> はい。<ruby>私<rt>わたし</rt></ruby>は<ruby>静<rt>しず</rt></ruby>かな<span class="cn-word" data-tr="joy"><ruby>所<rt>ところ</rt></ruby></span>が<ruby>好<rt>す</rt></ruby>きです。</p>

<p><ruby>先週<rt>せんしゅう</rt></ruby>の<ruby>土曜日<rt>どようび</rt></ruby>は<ruby>静<rt>しず</rt></ruby>かではありませんでした。<span class="cn-word" data-tr="bola"><ruby>子供<rt>こども</rt></ruby></span>がたくさんいました。</p>''',
        "questions": [
            {
                "text": "イノムさんは<ruby>何<rt>なに</rt></ruby>が<ruby>好<rt>す</rt></ruby>きですか。",
                "choices": [
                    "<ruby>数学<rt>すうがく</rt></ruby>が<ruby>好<rt>す</rt></ruby>きです",
                    "<ruby>漢字<rt>かんじ</rt></ruby>が<ruby>好<rt>す</rt></ruby>きです",
                    "<ruby>日本語<rt>にほんご</rt></ruby>が<ruby>好<rt>す</rt></ruby>きです",
                    "<ruby>建物<rt>たてもの</rt></ruby>が<ruby>好<rt>す</rt></ruby>きです",
                ],
                "answer": 2,
                "explanation": "«日本語が 好きです。でも 漢字は 好きではありません» — "
                               "yapon tili yoqadi, ammo iyerogliflar yoqmaydi. "
                               "<strong>数学が好きです</strong> — bu Parining gapi.",
            },
            {
                "text": "<ruby>先週<rt>せんしゅう</rt></ruby>の<ruby>土曜日<rt>どようび</rt></ruby>、<ruby>図書館<rt>としょかん</rt></ruby>はどうでしたか。",
                "choices": [
                    "<ruby>静<rt>しず</rt></ruby>かでした",
                    "<ruby>静<rt>しず</rt></ruby>かではありませんでした",
                    "<ruby>静<rt>しず</rt></ruby>かくなかったです",
                    "<ruby>便利<rt>べんり</rt></ruby>ではありませんでした",
                ],
                "answer": 1,
                "explanation": "Bolalar koʻp edi, shuning uchun jimjit emas edi. "
                               "な-sifat <strong>ot kabi</strong> tuslanadi: "
                               "ではありませんでした. «静かくなかった» — い-sifatning "
                               "shakli, な-sifatga toʻgʻri kelmaydi.",
            },
            {
                "text": "なぜ「<ruby>静<rt>しず</rt></ruby>かな<ruby>所<rt>ところ</rt></ruby>」da な bor, «<ruby>図書館<rt>としょかん</rt></ruby>は<ruby>静<rt>しず</rt></ruby>かです» da な yoʻq?",
                "choices": [
                    "<ruby>所<rt>ところ</rt></ruby>は<ruby>短<rt>みじか</rt></ruby>い<ruby>言葉<rt>ことば</rt></ruby>ですから",
                    "な は otdan oldin turganda qoʻshiladi, kesim boʻlganda yoʻqoladi",
                    "な は soʻroq gapda ishlatilmaydi",
                    "な は <ruby>図書館<rt>としょかん</rt></ruby> bilan ishlatilmaydi",
                ],
                "answer": 1,
                "explanation": "な-sifatning yagona qoidasi shu: <strong>な faqat otdan "
                               "oldin</strong> paydo boʻladi. Kesim boʻlganda sifat "
                               "yalangʻoch qoladi va です oladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "がっこうの あさ",
        "summary": (
            "PJ-27 matni. Imronning bir kuni — ichida uchala feʼl guruhidan "
            "feʼllar bor: 起きます va 寝ます (II), 読みます va 書きます (I), "
            "します va 来ます (III), hamda uchta tuzoq feʼl: 入ります, 帰ります, 走ります."
        ),
        "order":   27,
        "grammar": [
            {
                "pattern":  "I guruh (五段): う qatori → い qatori",
                "meaning":  "Eng katta guruh. Oxirgi tovush い qatoriga tushadi: "
                            "む→み, く→き, す→し, つ→ち.",
                "examples": ["<ruby>読<rt>よ</rt></ruby>む → <ruby>読<rt>よ</rt></ruby>みます",
                             "<ruby>書<rt>か</rt></ruby>く → <ruby>書<rt>か</rt></ruby>きます"],
            },
            {
                "pattern":  "II guruh (一段): る tushadi",
                "meaning":  "る bilan tugaydi va oldida い yoki え bor. る ni "
                            "olib tashlab ます qoʻyiladi.",
                "examples": ["<ruby>起<rt>お</rt></ruby>きる → <ruby>起<rt>お</rt></ruby>きます",
                             "<ruby>寝<rt>ね</rt></ruby>る → <ruby>寝<rt>ね</rt></ruby>ます"],
            },
            {
                "pattern":  "III guruh (不規則): faqat ikkita",
                "meaning":  "する → します, 来る → 来ます. Kanji oʻzgarmaydi, "
                            "oʻqilishi oʻzgaradi: く → き.",
                "examples": ["<ruby>勉強<rt>べんきょう</rt></ruby>する → <ruby>勉強<rt>べんきょう</rt></ruby>します",
                             "<ruby>来<rt>く</rt></ruby>る → <ruby>来<rt>き</rt></ruby>ます"],
            },
            {
                "pattern":  "Tuzoq feʼllar: 入る, 帰る",
                "meaning":  "る dan oldin い yoki え bor, lekin ular II emas, "
                            "I guruhda: 入ります, 帰ります.",
                "examples": ["<ruby>入<rt>はい</rt></ruby>る → <ruby>入<rt>はい</rt></ruby>ります",
                             "<ruby>帰<rt>かえ</rt></ruby>る → <ruby>帰<rt>かえ</rt></ruby>ります"],
            },
        ],
        "body": '''<p>イムロンさんは<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>六時<rt>ろくじ</rt></ruby>に<span class="cn-word" data-tr="turadi"><ruby>起<rt>お</rt></ruby>きます</span>。<span class="cn-word" data-tr="nonushta"><ruby>朝<rt>あさ</rt></ruby>ごはん</span>を<ruby>食<rt>た</rt></ruby>べます。<ruby>牛乳<rt>ぎゅうにゅう</rt></ruby>を<ruby>飲<rt>の</rt></ruby>みます。</p>

<p><ruby>七時<rt>しちじ</rt></ruby>にバスで<ruby>学校<rt>がっこう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きます。バスの<ruby>中<rt>なか</rt></ruby>で<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みます。<ruby>八時<rt>はちじ</rt></ruby>に<ruby>教室<rt>きょうしつ</rt></ruby>に<span class="cn-word" data-tr="kiradi"><ruby>入<rt>はい</rt></ruby>ります</span>。<span class="cn-word" data-tr="doʻst"><ruby>友<rt>とも</rt></ruby>だち</span>を<span class="cn-word" data-tr="kutadi"><ruby>待<rt>ま</rt></ruby>ちます</span>。</p>

<p><strong>ラノ:</strong> おはようございます。<ruby>今日<rt>きょう</rt></ruby>は<ruby>何<rt>なに</rt></ruby>をしますか。</p>

<p><strong>イムロン:</strong> <ruby>日本語<rt>にほんご</rt></ruby>を<ruby>勉強<rt>べんきょう</rt></ruby>します。<span class="cn-word" data-tr="iyeroglif"><ruby>漢字<rt>かんじ</rt></ruby></span>も<ruby>書<rt>か</rt></ruby>きます。</p>

<p><strong>ラノ:</strong> やまだ<ruby>先生<rt>せんせい</rt></ruby>は<ruby>来<rt>き</rt></ruby>ますか。</p>

<p><strong>イムロン:</strong> はい、<ruby>八時<rt>はちじ</rt></ruby><ruby>半<rt>はん</rt></ruby>に<ruby>来<rt>き</rt></ruby>ます。</p>

<p><ruby>十二時<rt>じゅうにじ</rt></ruby>に<ruby>二人<rt>ふたり</rt></ruby>は<span class="cn-word" data-tr="oshxona"><ruby>食堂<rt>しょくどう</rt></ruby></span>へ<ruby>行<rt>い</rt></ruby>きます。イムロンさんはパンを<span class="cn-word" data-tr="sotib oladi"><ruby>買<rt>か</rt></ruby>います</span>。ラノさんはお<ruby>茶<rt>ちゃ</rt></ruby>を<ruby>飲<rt>の</rt></ruby>みます。<ruby>二人<rt>ふたり</rt></ruby>は<ruby>日本語<rt>にほんご</rt></ruby>で<ruby>話<rt>はな</rt></ruby>します。</p>

<p><strong>ラノ:</strong> イムロンさんは<ruby>毎朝<rt>まいあさ</rt></ruby><span class="cn-word" data-tr="yuguradi"><ruby>走<rt>はし</rt></ruby>ります</span>か。</p>

<p><strong>イムロン:</strong> はい、<ruby>走<rt>はし</rt></ruby>ります。でも<ruby>今日<rt>きょう</rt></ruby>は<ruby>走<rt>はし</rt></ruby>りませんでした。</p>

<p><ruby>四時<rt>よじ</rt></ruby>に<ruby>家<rt>いえ</rt></ruby>へ<span class="cn-word" data-tr="qaytadi"><ruby>帰<rt>かえ</rt></ruby>ります</span>。<ruby>夜<rt>よる</rt></ruby><ruby>十時<rt>じゅうじ</rt></ruby>に<span class="cn-word" data-tr="uxlaydi"><ruby>寝<rt>ね</rt></ruby>ます</span>。<span class="cn-word" data-tr="uzun"><ruby>長<rt>なが</rt></ruby>い</span><ruby>一日<rt>いちにち</rt></ruby>です。</p>''',
        "questions": [
            {
                "text": "イムロンさんは<ruby>何時<rt>なんじ</rt></ruby>に<ruby>教室<rt>きょうしつ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>りますか。",
                "choices": [
                    "<ruby>六時<rt>ろくじ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>ります",
                    "<ruby>七時<rt>しちじ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>ります",
                    "<ruby>八時<rt>はちじ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>ります",
                    "<ruby>八時<rt>はちじ</rt></ruby><ruby>半<rt>はん</rt></ruby>に<ruby>入<rt>はい</rt></ruby>ります",
                ],
                "answer": 2,
                "explanation": "«八時に 教室に 入ります» — soat sakkizda. Olti — turadigan "
                               "vaqti, yetti — avtobusga chiqadigan vaqti, sakkiz yarim — "
                               "oʻqituvchi keladigan vaqt.",
            },
            {
                "text": "<ruby>入<rt>はい</rt></ruby>る feʼli qaysi guruhda?",
                "choices": [
                    "II guruh (<ruby>一段<rt>いちだん</rt></ruby>)",
                    "I guruh (<ruby>五段<rt>ごだん</rt></ruby>)",
                    "III guruh (<ruby>不規則<rt>ふきそく</rt></ruby>)",
                    "Hech qaysi guruhga kirmaydi",
                ],
                "answer": 1,
                "explanation": "る dan oldin い turibdi, shuning uchun II guruhga oʻxshaydi "
                               "— lekin bu beshta tuzoq feʼldan biri. Javobni matnning "
                               "oʻzi beradi: <strong>入ります</strong>, «はいます» emas. "
                               "り chiqsa — feʼl I guruhda.",
            },
            {
                "text": "「<ruby>来<rt>く</rt></ruby>る」ning ます shakli matnda qanday yozilgan?",
                "choices": [
                    "<ruby>来<rt>く</rt></ruby>ります",
                    "<ruby>来<rt>く</rt></ruby>ます",
                    "<ruby>来<rt>き</rt></ruby>ます",
                    "<ruby>来<rt>こ</rt></ruby>ます",
                ],
                "answer": 2,
                "explanation": "«やまだ先生は 来ますか» — kanji oʻsha, lekin oʻqilishi "
                               "<strong>き</strong> ga oʻzgardi. Bu 来る ning tartibsizligi, "
                               "va u faqat furigana orqali koʻrinadi.",
            },
        ],
    },
]
