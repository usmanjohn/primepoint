# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-16 … PJ-18.

Kumulyativ qoida: faqat PJ-18 gacha oʻrganilgan qoliplar.
PJ-20 gacha feʼl yoʻq → toc'dagi hikoya ramkasi roʻyxati ishlatiladi.
Toc: corner/management/commands/toc_prime_japanese_readings.txt

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_16_18.py --author=prime
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
        "title":   "ねこは どこですか",
        "summary": (
            "PJ-16 matni. Dilnozaning mushugi yoʻqolib qoladi — va uni qidirishda "
            "あります bilan います farqi har jumlada koʻrinadi."
        ),
        "order":   16,
        "grammar": [
            {
                "pattern":  "JOY に NARSA が あります / います",
                "meaning":  "«…da … bor». Jonsiz narsa uchun あります, jonli "
                            "narsa uchun います. Joy qoʻshimchasi — に.",
                "examples": ["<ruby>机<rt>つくえ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に<ruby>本<rt>ほん</rt></ruby>があります。",
                             "そこに<ruby>猫<rt>ねこ</rt></ruby>がいます。"],
            },
            {
                "pattern":  "NARSA は JOY に あります / います",
                "meaning":  "«… qayerda». Narsa maʼlum boʻlsa, u は oladi va gap "
                            "boshiga chiqadi.",
                "examples": ["<ruby>猫<rt>ねこ</rt></ruby>は<ruby>鞄<rt>かばん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>にいます。"],
            },
            {
                "pattern":  "ここ・そこ・あそこ・どこ",
                "meaning":  "Joy soʻzlari. ko-so-a-do tizimining joy qatori.",
                "examples": ["<ruby>猫<rt>ねこ</rt></ruby>はどこですか。", "あそこです。"],
            },
        ],
        "body": '''<p><ruby>今日<rt>きょう</rt></ruby>は<ruby>日曜日<rt>にちようび</rt></ruby>です。<span class="cn-word" data-tr="Dilnoza">ディルノザ</span>さんの<span class="cn-word" data-tr="uy"><ruby>家<rt>いえ</rt></ruby></span>に アフソナさんが <span class="cn-word" data-pos="verb" data-tr="keldi"><ruby>来<rt>き</rt></ruby>ました</span>。</p>

<p><strong>アフソナ:</strong> ディルノザさんの<span class="cn-word" data-tr="mushuk"><ruby>猫<rt>ねこ</rt></ruby></span>は どこですか。</p>

<p><strong>ディルノザ:</strong> ここに います。あ、<span class="cn-word" data-tr="yoʻq">いません</span>！</p>

<p><ruby>机<rt>つくえ</rt></ruby>の<span class="cn-word" data-tr="ust"><ruby>上<rt>うえ</rt></ruby></span>に <ruby>本<rt>ほん</rt></ruby>が あります。<ruby>本<rt>ほん</rt></ruby>の<span class="cn-word" data-tr="ost"><ruby>下<rt>した</rt></ruby></span>に <ruby>猫<rt>ねこ</rt></ruby>は いません。</p>

<p><strong>ディルノザ:</strong> <ruby>机<rt>つくえ</rt></ruby>の<ruby>下<rt>した</rt></ruby>ですか。</p>

<p><strong>アフソナ:</strong> いいえ。そこには <span class="cn-word" data-tr="poyabzal"><ruby>靴<rt>くつ</rt></ruby></span>が あります。<ruby>猫<rt>ねこ</rt></ruby>は いません。</p>

<p><span class="cn-word" data-tr="oʻsha payt">そのとき</span>、<span class="cn-word" data-tr="sumka"><ruby>鞄<rt>かばん</rt></ruby></span>の<span class="cn-word" data-tr="ich"><ruby>中<rt>なか</rt></ruby></span>に <span class="cn-word" data-tr="ovoz"><ruby>声<rt>こえ</rt></ruby></span>が あります。</p>

<p><strong>ディルノザ:</strong> あそこです！ <ruby>猫<rt>ねこ</rt></ruby>は <ruby>鞄<rt>かばん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に います。</p>

<p><strong>アフソナ:</strong> <ruby>鞄<rt>かばん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に <ruby>本<rt>ほん</rt></ruby>が ありますか。</p>

<p><strong>ディルノザ:</strong> はい。<ruby>本<rt>ほん</rt></ruby>と <ruby>猫<rt>ねこ</rt></ruby>が います… いいえ、<ruby>本<rt>ほん</rt></ruby>は あります、<ruby>猫<rt>ねこ</rt></ruby>は います！</p>''',
        "questions": [
            {
                "text": "<ruby>猫<rt>ねこ</rt></ruby>は どこに いましたか。",
                "choices": [
                    "<ruby>机<rt>つくえ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に",
                    "<ruby>机<rt>つくえ</rt></ruby>の<ruby>下<rt>した</rt></ruby>に",
                    "<ruby>鞄<rt>かばん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に",
                    "<ruby>本<rt>ほん</rt></ruby>の<ruby>下<rt>した</rt></ruby>に",
                ],
                "answer": 2,
                "explanation": "Dilnoza oxirida «猫は 鞄の中に います» dedi — mushuk "
                               "sumka ichida edi. Stol tagida poyabzal, stol ustida "
                               "kitob bor edi.",
            },
            {
                "text": "なぜ「<ruby>本<rt>ほん</rt></ruby>は あります」と いいますか。",
                "choices": [
                    "<ruby>本<rt>ほん</rt></ruby>は <ruby>大<rt>おお</rt></ruby>きいですから",
                    "<ruby>本<rt>ほん</rt></ruby>は いきものでは ありませんから",
                    "<ruby>本<rt>ほん</rt></ruby>は <ruby>鞄<rt>かばん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に ありますから",
                    "<ruby>本<rt>ほん</rt></ruby>は ディルノザさんのですから",
                ],
                "answer": 1,
                "explanation": "Kitob — jonsiz narsa, shuning uchun あります ishlatiladi. "
                               "Mushuk esa tirik jonzot, shuning uchun います. Dilnoza "
                               "oxirida oʻzini tuzatdi — aynan shu farqni.",
            },
            {
                "text": "<ruby>机<rt>つくえ</rt></ruby>の<ruby>下<rt>した</rt></ruby>に <ruby>何<rt>なに</rt></ruby>が ありましたか。",
                "choices": [
                    "<ruby>靴<rt>くつ</rt></ruby>",
                    "<ruby>本<rt>ほん</rt></ruby>",
                    "<ruby>鞄<rt>かばん</rt></ruby>",
                    "<ruby>猫<rt>ねこ</rt></ruby>",
                ],
                "answer": 0,
                "explanation": "Afsona «そこには 靴が あります» dedi — stol tagida "
                               "poyabzal bor edi. Poyabzal jonsiz, shuning uchun あります.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "わたしの かばん",
        "summary": (
            "PJ-17 matni. Sinfda bir xil ikkita sumka topiladi — va の qoʻshimchasi "
            "kimniki ekanini hal qiladi."
        ),
        "order":   17,
        "grammar": [
            {
                "pattern":  "A の B",
                "meaning":  "«A ning B si». Egalik ham, ikki otni bogʻlash ham "
                            "shu bitta qoʻshimcha bilan.",
                "examples": ["<ruby>私<rt>わたし</rt></ruby>の<ruby>鞄<rt>かばん</rt></ruby>",
                             "<ruby>日本語<rt>にほんご</rt></ruby>の<ruby>本<rt>ほん</rt></ruby>"],
            },
            {
                "pattern":  "〜の (ot tushirilgan)",
                "meaning":  "の dan keyingi ot aniq boʻlsa, u tushirib qoldiriladi "
                            "va の ning oʻzi «…niki» maʼnosini oladi.",
                "examples": ["これは<ruby>私<rt>わたし</rt></ruby>のです。",
                             "<ruby>誰<rt>だれ</rt></ruby>のですか。"],
            },
            {
                "pattern":  "A の B の C",
                "meaning":  "Zanjir. Chapdan oʻngga torayadi; asosiy narsa — "
                            "OXIRGI soʻz.",
                "examples": ["<ruby>私<rt>わたし</rt></ruby>の<ruby>友達<rt>ともだち</rt></ruby>の<ruby>鞄<rt>かばん</rt></ruby>"],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="sinf xonasi"><ruby>教室<rt>きょうしつ</rt></ruby></span>の<ruby>中<rt>なか</rt></ruby>に <span class="cn-word" data-tr="sumka"><ruby>鞄<rt>かばん</rt></ruby></span>が <span class="cn-word" data-tr="ikkita">ふたつ</span> あります。<span class="cn-word" data-tr="bir xil">おなじ</span> <ruby>鞄<rt>かばん</rt></ruby>です。</p>

<p><strong>ジャスル:</strong> この<ruby>鞄<rt>かばん</rt></ruby>は <ruby>誰<rt>だれ</rt></ruby>のですか。</p>

<p><strong>アフソナ:</strong> それは <ruby>私<rt>わたし</rt></ruby>のです。</p>

<p><strong>ジャスル:</strong> あの<ruby>鞄<rt>かばん</rt></ruby>は アフソナさんのですか。</p>

<p><strong>アフソナ:</strong> いいえ、あれは <ruby>私<rt>わたし</rt></ruby>のでは ありません。ディルノザさんのです。</p>

<p><ruby>鞄<rt>かばん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に <ruby>本<rt>ほん</rt></ruby>が あります。<span class="cn-word" data-tr="yapon tili"><ruby>日本語<rt>にほんご</rt></ruby></span>の<span class="cn-word" data-tr="kitob"><ruby>本<rt>ほん</rt></ruby></span>です。<ruby>本<rt>ほん</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に <span class="cn-word" data-tr="ism"><ruby>名前<rt>なまえ</rt></ruby></span>が あります。</p>

<p><strong>ジャスル:</strong> あ、これは <ruby>私<rt>わたし</rt></ruby>の<span class="cn-word" data-tr="doʻst"><ruby>友達<rt>ともだち</rt></ruby></span>の<ruby>本<rt>ほん</rt></ruby>です。<span class="cn-word" data-tr="Bekzod">ベクゾド</span>さんのです。</p>

<p><strong>アフソナ:</strong> <span class="cn-word" data-tr="nega"><ruby>何<rt>なん</rt></ruby>で</span> ベクゾドさんの<ruby>本<rt>ほん</rt></ruby>が ディルノザさんの<ruby>鞄<rt>かばん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に ありますか。</p>

<p><strong>ジャスル:</strong> <span class="cn-word" data-tr="bilmayman">さあ</span>… ディルノザさんは ベクゾドさんの<ruby>友達<rt>ともだち</rt></ruby>です。</p>''',
        "questions": [
            {
                "text": "<ruby>本<rt>ほん</rt></ruby>は <ruby>誰<rt>だれ</rt></ruby>のですか。",
                "choices": [
                    "アフソナさんのです",
                    "ディルノザさんのです",
                    "ベクゾドさんのです",
                    "ジャスルさんのです",
                ],
                "answer": 2,
                "explanation": "Jasur «これは 私の友達の本です。ベクゾドさんのです» dedi. "
                               "Zanjirda asosiy narsa oxirgi soʻz — 本, va uning egasi "
                               "Bekzod.",
            },
            {
                "text": "「<ruby>私<rt>わたし</rt></ruby>の<ruby>友達<rt>ともだち</rt></ruby>の<ruby>本<rt>ほん</rt></ruby>」は <ruby>何<rt>なん</rt></ruby>ですか。",
                "choices": [
                    "<ruby>友達<rt>ともだち</rt></ruby>",
                    "<ruby>私<rt>わたし</rt></ruby>",
                    "<ruby>本<rt>ほん</rt></ruby>",
                    "<ruby>鞄<rt>かばん</rt></ruby>",
                ],
                "answer": 2,
                "explanation": "の zanjirida asosiy narsa doim <strong>oxirgi</strong> "
                               "soʻz. «Mening doʻstimning kitobi» — gap kitob haqida, "
                               "qolgan ikkitasi uni aniqlaydi.",
            },
            {
                "text": "アフソナさんの<ruby>鞄<rt>かばん</rt></ruby>は どれですか。",
                "choices": [
                    "この<ruby>鞄<rt>かばん</rt></ruby>です",
                    "あの<ruby>鞄<rt>かばん</rt></ruby>です",
                    "ディルノザさんのです",
                    "ベクゾドさんのです",
                ],
                "answer": 0,
                "explanation": "Jasur «この鞄は 誰のですか» deb soʻraganda Afsona "
                               "«それは 私のです» dedi. あの鞄 esa Dilnozaniki. Diqqat: "
                               "Jasur この dedi, Afsona esa それ — sumka Jasurga yaqin edi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "きょうしつは どこですか",
        "summary": (
            "PJ-18 matni. Yangi oʻquvchi maktabda yoʻl soʻraydi — bitta qisqa "
            "suhbatda oltita soʻroq soʻzi ishlaydi."
        ),
        "order":   18,
        "grammar": [
            {
                "pattern":  "どこ・いつ・どう・いくら",
                "meaning":  "Soʻroq soʻzlari. Ular JAVOB turadigan joyda turadi — "
                            "gapni qayta qurish kerak emas.",
                "examples": ["<ruby>教室<rt>きょうしつ</rt></ruby>はどこですか。",
                             "<ruby>試験<rt>しけん</rt></ruby>はいつですか。"],
            },
            {
                "pattern":  "<ruby>何<rt>なん</rt></ruby> / <ruby>何<rt>なに</rt></ruby>",
                "meaning":  "Bitta kanji, ikki oʻqilish: です・の va sanoq soʻzidan "
                            "oldin なん, が・を dan oldin なに.",
                "examples": ["これは<ruby>何<rt>なん</rt></ruby>ですか。",
                             "<ruby>何<rt>なに</rt></ruby>がありますか。"],
            },
            {
                "pattern":  "<ruby>誰<rt>だれ</rt></ruby>が 〜ですか",
                "meaning":  "Soʻroq soʻzi は OLMAYDI — doim が. Lekin gapning "
                            "boshqa qismi bemalol は oladi.",
                "examples": ["<ruby>誰<rt>だれ</rt></ruby>が<ruby>先生<rt>せんせい</rt></ruby>ですか。"],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Sherbek">シェルベク</span>さんは <span class="cn-word" data-tr="yangi oʻquvchi"><ruby>新入生<rt>しんにゅうせい</rt></ruby></span>です。<span class="cn-word" data-tr="maktab"><ruby>学校<rt>がっこう</rt></ruby></span>の<span class="cn-word" data-tr="old"><ruby>前<rt>まえ</rt></ruby></span>に アフソナさんが います。</p>

<p><strong>シェルベク:</strong> あの、すみません。<ruby>日本語<rt>にほんご</rt></ruby>の<ruby>教室<rt>きょうしつ</rt></ruby>は どこですか。</p>

<p><strong>アフソナ:</strong> あそこです。<span class="cn-word" data-tr="kutubxona"><ruby>図書館<rt>としょかん</rt></ruby></span>の<ruby>中<rt>なか</rt></ruby>では ありません。<ruby>図書館<rt>としょかん</rt></ruby>の<span class="cn-word" data-tr="orqa"><ruby>後<rt>うし</rt></ruby>ろ</span>です。</p>

<p><strong>シェルベク:</strong> ありがとうございます。<ruby>先生<rt>せんせい</rt></ruby>は <ruby>誰<rt>だれ</rt></ruby>ですか。</p>

<p><strong>アフソナ:</strong> やまだ<ruby>先生<rt>せんせい</rt></ruby>です。</p>

<p><strong>シェルベク:</strong> <span class="cn-word" data-tr="imtihon"><ruby>試験<rt>しけん</rt></ruby></span>は いつですか。</p>

<p><strong>アフソナ:</strong> <ruby>二十日<rt>はつか</rt></ruby>です。</p>

<p><strong>シェルベク:</strong> <ruby>日本語<rt>にほんご</rt></ruby>は どうですか。</p>

<p><strong>アフソナ:</strong> <span class="cn-word" data-tr="kanji"><ruby>漢字<rt>かんじ</rt></ruby></span>が <span class="cn-word" data-tr="koʻp">たくさん</span> あります！</p>

<p>シェルベクさんの<ruby>手<rt>て</rt></ruby>に <span class="cn-word" data-tr="qogʻoz"><ruby>紙<rt>かみ</rt></ruby></span>が あります。アフソナさんが <span class="cn-word" data-pos="verb" data-tr="koʻrdi"><ruby>見<rt>み</rt></ruby>ました</span>。</p>

<p><strong>アフソナ:</strong> それは <ruby>何<rt>なん</rt></ruby>ですか。</p>

<p><strong>シェルベク:</strong> これは <ruby>学校<rt>がっこう</rt></ruby>の<span class="cn-word" data-tr="xarita"><ruby>地図<rt>ちず</rt></ruby></span>です。でも <ruby>日本語<rt>にほんご</rt></ruby>の<ruby>教室<rt>きょうしつ</rt></ruby>は ここに ありません！</p>''',
        "questions": [
            {
                "text": "<ruby>日本語<rt>にほんご</rt></ruby>の<ruby>教室<rt>きょうしつ</rt></ruby>は どこですか。",
                "choices": [
                    "<ruby>図書館<rt>としょかん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>です",
                    "<ruby>図書館<rt>としょかん</rt></ruby>の<ruby>後<rt>うし</rt></ruby>ろです",
                    "<ruby>学校<rt>がっこう</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>です",
                    "<ruby>地図<rt>ちず</rt></ruby>の<ruby>中<rt>なか</rt></ruby>です",
                ],
                "answer": 1,
                "explanation": "Afsona «図書館の中では ありません。図書館の後ろです» dedi — "
                               "kutubxonaning ichida emas, orqasida.",
            },
            {
                "text": "なぜ「それは<ruby>何<rt>なん</rt></ruby>ですか」と いいますか、"
                        "「<ruby>何<rt>なに</rt></ruby>ですか」と いいませんか。",
                "choices": [
                    "です の <ruby>前<rt>まえ</rt></ruby>は <ruby>何<rt>なん</rt></ruby>ですから",
                    "が の <ruby>前<rt>まえ</rt></ruby>は <ruby>何<rt>なん</rt></ruby>ですから",
                    "<ruby>何<rt>なに</rt></ruby>は <ruby>古<rt>ふる</rt></ruby>い ことばですから",
                    "しつもんでは ありませんから",
                ],
                "answer": 0,
                "explanation": "です dan oldin doim <strong>なん</strong> oʻqiladi — "
                               "«なんです» tilga yengilroq tushadi. が dan oldin esa "
                               "なに boʻlardi.",
            },
            {
                "text": "シェルベクさんの<ruby>問題<rt>もんだい</rt></ruby>は <ruby>何<rt>なん</rt></ruby>ですか。",
                "choices": [
                    "<ruby>先生<rt>せんせい</rt></ruby>が いません",
                    "<ruby>試験<rt>しけん</rt></ruby>が <ruby>今日<rt>きょう</rt></ruby>です",
                    "<ruby>地図<rt>ちず</rt></ruby>に <ruby>日本語<rt>にほんご</rt></ruby>の<ruby>教室<rt>きょうしつ</rt></ruby>が ありません",
                    "<ruby>漢字<rt>かんじ</rt></ruby>が わかりません",
                ],
                "answer": 2,
                "explanation": "Oxirgi jumlada Sherbek «日本語の教室は ここに ありません» "
                               "dedi — xaritada yapon tili sinfi koʻrsatilmagan. Aynan "
                               "shuning uchun u Afsonadan soʻrashi kerak edi.",
            },
        ],
    },
]
