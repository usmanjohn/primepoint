# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-22 … PJ-24.

Hikoya ramkasi istisnosi PJ-20 da tugagan: har bir feʼl darslarda berilgan.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_22_24.py --author=prime
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
        "title":   "バスで がっこうへ",
        "summary": (
            "PJ-22 matni. Sherbek maktabga qanday borishini aytadi — で uch xil "
            "ishda: transport, ish joyi va yana transport."
        ),
        "order":   22,
        "grammar": [
            {
                "pattern":  "JOY で + harakat feʼli",
                "meaning":  "Ish BAJARILAYOTGAN joy. あります/います bilan esa "
                            "に ishlatiladi — feʼl hal qiladi.",
                "examples": ["<ruby>教室<rt>きょうしつ</rt></ruby>で<ruby>勉強<rt>べんきょう</rt></ruby>します。",
                             "<ruby>家<rt>いえ</rt></ruby>で<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みます。"],
            },
            {
                "pattern":  "VOSITA で",
                "meaning":  "«… bilan, … yordamida»: transport, asbob, til.",
                "examples": ["バスで<ruby>行<rt>い</rt></ruby>きます。",
                             "<ruby>日本語<rt>にほんご</rt></ruby>で<ruby>話<rt>はな</rt></ruby>します。"],
            },
            {
                "pattern":  "JOY へ",
                "meaning":  "Yoʻnalish, «… tomonga». [e] deb oʻqiladi. に bilan "
                            "deyarli bir xil; へ biroz rasmiyroq.",
                "examples": ["<ruby>学校<rt>がっこう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きます。"],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Sherbek">シェルベク</span>さんの<span class="cn-word" data-tr="uy"><ruby>家<rt>いえ</rt></ruby></span>から <ruby>学校<rt>がっこう</rt></ruby>まで バスで <ruby>三十分<rt>さんじゅっぷん</rt></ruby>です。</p>

<p><strong>アフソナ:</strong> シェルベクさんは <ruby>毎日<rt>まいにち</rt></ruby> <span class="cn-word" data-tr="qanday">どう</span>やって <ruby>学校<rt>がっこう</rt></ruby>へ <ruby>行<rt>い</rt></ruby>きますか。</p>

<p><strong>シェルベク:</strong> <span class="cn-word" data-tr="avtobus">バス</span>で <ruby>行<rt>い</rt></ruby>きます。<span class="cn-word" data-tr="velosiped"><ruby>自転車<rt>じてんしゃ</rt></ruby></span>では <ruby>行<rt>い</rt></ruby>きません。</p>

<p><strong>アフソナ:</strong> <ruby>私<rt>わたし</rt></ruby>は <span class="cn-word" data-tr="piyoda"><ruby>歩<rt>ある</rt></ruby>いて</span> <ruby>行<rt>い</rt></ruby>きます。<ruby>家<rt>いえ</rt></ruby>は <ruby>学校<rt>がっこう</rt></ruby>の<ruby>後<rt>うし</rt></ruby>ろです。</p>

<p><strong>シェルベク:</strong> そうですか。バスの<ruby>中<rt>なか</rt></ruby>で <ruby>何<rt>なに</rt></ruby>を しますか… <ruby>私<rt>わたし</rt></ruby>は バスで <ruby>本<rt>ほん</rt></ruby>を <ruby>読<rt>よ</rt></ruby>みます。</p>

<p><strong>アフソナ:</strong> バスに <ruby>人<rt>ひと</rt></ruby>が <span class="cn-word" data-tr="koʻp">たくさん</span> いますか。</p>

<p><strong>シェルベク:</strong> はい、<ruby>朝<rt>あさ</rt></ruby>は たくさん います。でも <ruby>本<rt>ほん</rt></ruby>を <ruby>読<rt>よ</rt></ruby>みます。</p>

<p><span class="cn-word" data-tr="maktabda"><ruby>学校<rt>がっこう</rt></ruby></span>で <ruby>二人<rt>ふたり</rt></ruby>は <ruby>日本語<rt>にほんご</rt></ruby>を <ruby>勉強<rt>べんきょう</rt></ruby>します。<span class="cn-word" data-tr="sinf"><ruby>教室<rt>きょうしつ</rt></ruby></span>に やまだ<ruby>先生<rt>せんせい</rt></ruby>が います。</p>

<p><strong>やまだ:</strong> <ruby>教室<rt>きょうしつ</rt></ruby>では <ruby>日本語<rt>にほんご</rt></ruby>で <ruby>話<rt>はな</rt></ruby>します。</p>''',
        "questions": [
            {
                "text": "シェルベクさんは <ruby>何<rt>なに</rt></ruby>で <ruby>学校<rt>がっこう</rt></ruby>へ <ruby>行<rt>い</rt></ruby>きますか。",
                "choices": [
                    "<ruby>自転車<rt>じてんしゃ</rt></ruby>で<ruby>行<rt>い</rt></ruby>きます",
                    "バスで<ruby>行<rt>い</rt></ruby>きます",
                    "<ruby>歩<rt>ある</rt></ruby>いて<ruby>行<rt>い</rt></ruby>きます",
                    "<ruby>電車<rt>でんしゃ</rt></ruby>で<ruby>行<rt>い</rt></ruby>きます",
                ],
                "answer": 1,
                "explanation": "«バスで 行きます。自転車では 行きません» — avtobusda "
                               "boradi, velosipedda emas. Bu yerda で <strong>vosita</strong> "
                               "maʼnosida: nima yordamida.",
            },
            {
                "text": "なぜ「<ruby>教室<rt>きょうしつ</rt></ruby>に やまだ<ruby>先生<rt>せんせい</rt></ruby>が います」と いいますか、"
                        "「<ruby>教室<rt>きょうしつ</rt></ruby>で」と いいませんか。",
                "choices": [
                    "います は そんざいの どうしですから",
                    "<ruby>先生<rt>せんせい</rt></ruby>は ひとですから",
                    "<ruby>教室<rt>きょうしつ</rt></ruby>は ちいさいですから",
                    "で は ふるい ことばですから",
                ],
                "answer": 0,
                "explanation": "います mavjudlikni bildiradi, harakatni emas — shuning "
                               "uchun <strong>に</strong>. Oʻsha jumlaning oldida esa "
                               "«学校で 勉強します» bor: u harakat, demak <strong>で</strong>.",
            },
            {
                "text": "シェルベクさんは バスの<ruby>中<rt>なか</rt></ruby>で <ruby>何<rt>なに</rt></ruby>を しますか。",
                "choices": [
                    "<ruby>音楽<rt>おんがく</rt></ruby>を<ruby>聞<rt>き</rt></ruby>きます",
                    "<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みます",
                    "<ruby>勉強<rt>べんきょう</rt></ruby>します",
                    "<ruby>手紙<rt>てがみ</rt></ruby>を<ruby>書<rt>か</rt></ruby>きます",
                ],
                "answer": 1,
                "explanation": "«私は バスで 本を 読みます» — avtobusda kitob oʻqiydi. "
                               "Diqqat: bu yerda で ikki xil ishda — «バスで» vosita, "
                               "«バスの中で» esa ish joyi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "きのうの にちようび",
        "summary": (
            "PJ-23 matni. Dilnoza kechagi yakshanbani aytib beradi — butun matn "
            "oʻtgan zamonda, va inkor shakli ham koʻrinadi."
        ),
        "order":   23,
        "grammar": [
            {
                "pattern":  "〜ました",
                "meaning":  "Oʻtgan zamon: ます → ました. Istisno YOʻQ — hamma "
                            "feʼl uchun bitta qoida.",
                "examples": ["<ruby>映画<rt>えいが</rt></ruby>を<ruby>見<rt>み</rt></ruby>ました。",
                             "<ruby>友達<rt>ともだち</rt></ruby>に<ruby>会<rt>あ</rt></ruby>いました。"],
            },
            {
                "pattern":  "〜ませんでした",
                "meaning":  "Oʻtgan zamon inkori: ません (inkor) + でした (oʻtgan).",
                "examples": ["<ruby>勉強<rt>べんきょう</rt></ruby>しませんでした。"],
            },
            {
                "pattern":  "でした",
                "meaning":  "です ning oʻtgan shakli, «…edi».",
                "examples": ["<ruby>昨日<rt>きのう</rt></ruby>は<ruby>日曜日<rt>にちようび</rt></ruby>でした。"],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="kecha"><ruby>昨日<rt>きのう</rt></ruby></span>は <ruby>日曜日<rt>にちようび</rt></ruby>でした。<span class="cn-word" data-tr="Dilnoza">ディルノザ</span>さんは <ruby>学校<rt>がっこう</rt></ruby>へ <ruby>行<rt>い</rt></ruby>きませんでした。</p>

<p><ruby>朝<rt>あさ</rt></ruby> <ruby>十時<rt>じゅうじ</rt></ruby>に <ruby>起<rt>お</rt></ruby>きました。<ruby>家<rt>いえ</rt></ruby>で パンを <ruby>食<rt>た</rt></ruby>べました。<ruby>勉強<rt>べんきょう</rt></ruby>は しませんでした。</p>

<p><strong>アフソナ:</strong> <ruby>昨日<rt>きのう</rt></ruby> <ruby>何<rt>なに</rt></ruby>を しましたか。</p>

<p><strong>ディルノザ:</strong> <span class="cn-word" data-tr="bogʻ"><ruby>公園<rt>こうえん</rt></ruby></span>へ <ruby>行<rt>い</rt></ruby>きました。そこで <ruby>友達<rt>ともだち</rt></ruby>に <span class="cn-word" data-pos="verb" data-tr="uchrashdim"><ruby>会<rt>あ</rt></ruby>いました</span>。</p>

<p><strong>アフソナ:</strong> <ruby>公園<rt>こうえん</rt></ruby>に <ruby>人<rt>ひと</rt></ruby>が いましたか。</p>

<p><strong>ディルノザ:</strong> はい、たくさん いました。<span class="cn-word" data-tr="mushuk"><ruby>猫<rt>ねこ</rt></ruby></span>も いました！</p>

<p><strong>アフソナ:</strong> <ruby>映画<rt>えいが</rt></ruby>は <ruby>見<rt>み</rt></ruby>ましたか。</p>

<p><strong>ディルノザ:</strong> いいえ、<ruby>見<rt>み</rt></ruby>ませんでした。でも <span class="cn-word" data-pos="verb" data-tr="sotib oldim"><ruby>買<rt>か</rt></ruby>いました</span>… <ruby>本<rt>ほん</rt></ruby>を <ruby>買<rt>か</rt></ruby>いました。</p>

<p><strong>アフソナ:</strong> <ruby>何<rt>なん</rt></ruby>の <ruby>本<rt>ほん</rt></ruby>でしたか。</p>

<p><strong>ディルノザ:</strong> <ruby>日本語<rt>にほんご</rt></ruby>の <ruby>本<rt>ほん</rt></ruby>でした。<ruby>夜<rt>よる</rt></ruby> <ruby>家<rt>いえ</rt></ruby>で <ruby>読<rt>よ</rt></ruby>みました。</p>''',
        "questions": [
            {
                "text": "ディルノザさんは <ruby>昨日<rt>きのう</rt></ruby> <ruby>勉強<rt>べんきょう</rt></ruby>しましたか。",
                "choices": [
                    "はい、しました",
                    "いいえ、しませんでした",
                    "はい、<ruby>公園<rt>こうえん</rt></ruby>でしました",
                    "いいえ、<ruby>学校<rt>がっこう</rt></ruby>でしました",
                ],
                "answer": 1,
                "explanation": "«勉強は しませんでした» — oʻqimadi. ませんでした = "
                               "ません (inkor) + でした (oʻtgan). Diqqat: 勉強 dan "
                               "keyin は kelgan — bu qarama-qarshi qoʻyish.",
            },
            {
                "text": "<ruby>公園<rt>こうえん</rt></ruby>に <ruby>猫<rt>ねこ</rt></ruby>が いましたか、ありましたか。",
                "choices": [
                    "ありました",
                    "いました",
                    "いませんでした",
                    "ありませんでした",
                ],
                "answer": 1,
                "explanation": "<strong>いました</strong> — mushuk jonli. Jonli/jonsiz "
                               "farqi oʻtgan zamonda ham saqlanadi: います → いました, "
                               "あります → ありました.",
            },
            {
                "text": "ディルノザさんは <ruby>何<rt>なに</rt></ruby>を <ruby>買<rt>か</rt></ruby>いましたか。",
                "choices": [
                    "<ruby>映画<rt>えいが</rt></ruby>を<ruby>買<rt>か</rt></ruby>いました",
                    "パンを<ruby>買<rt>か</rt></ruby>いました",
                    "<ruby>日本語<rt>にほんご</rt></ruby>の<ruby>本<rt>ほん</rt></ruby>を<ruby>買<rt>か</rt></ruby>いました",
                    "<ruby>何<rt>なに</rt></ruby>も<ruby>買<rt>か</rt></ruby>いませんでした",
                ],
                "answer": 2,
                "explanation": "«新しい 本を 買いました… 日本語の 本でした» — yapon tili "
                               "kitobini sotib oldi. Kinoni esa koʻrmadi "
                               "(見ませんでした).",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "なんじから なんじまで",
        "summary": (
            "PJ-24 matni. Yamada oʻqituvchining ish kuni — soat, hafta kunlari va "
            "から〜まで bitta jadvalda ishlaydi."
        ),
        "order":   24,
        "grammar": [
            {
                "pattern":  "A から B まで",
                "meaning":  "«A dan B gacha» — vaqt uchun ham, joy uchun ham. "
                            "に QOʻSHILMAYDI.",
                "examples": ["<ruby>九時<rt>くじ</rt></ruby>から<ruby>五時<rt>ごじ</rt></ruby>まで<ruby>働<rt>はたら</rt></ruby>きます。",
                             "<ruby>家<rt>いえ</rt></ruby>から<ruby>学校<rt>がっこう</rt></ruby>まで"],
            },
            {
                "pattern":  "SON + <ruby>時<rt>じ</rt></ruby>",
                "meaning":  "Soat. Uchta istisno: 4 = よじ, 7 = しちじ, 9 = くじ. "
                            "«Yarim» — <ruby>半<rt>はん</rt></ruby>.",
                "examples": ["<ruby>四時<rt>よじ</rt></ruby>", "<ruby>七時半<rt>しちじはん</rt></ruby>"],
            },
            {
                "pattern":  "Hafta kuni + に",
                "meaning":  "Hafta kuni aniq nuqta, shuning uchun に oladi. "
                            "<ruby>毎週<rt>まいしゅう</rt></ruby> esa OLMAYDI.",
                "examples": ["<ruby>月曜日<rt>げつようび</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。"],
            },
        ],
        "body": '''<p>やまだ<ruby>先生<rt>せんせい</rt></ruby>は <ruby>毎日<rt>まいにち</rt></ruby> <span class="cn-word" data-pos="verb" data-tr="ishlaydi"><ruby>働<rt>はたら</rt></ruby>きます</span>。</p>

<p><strong>シェルベク:</strong> <ruby>先生<rt>せんせい</rt></ruby>は <ruby>何時<rt>なんじ</rt></ruby>から <ruby>何時<rt>なんじ</rt></ruby>まで <ruby>働<rt>はたら</rt></ruby>きますか。</p>

<p><strong>やまだ:</strong> <span class="cn-word" data-tr="ertalabki"><ruby>午前<rt>ごぜん</rt></ruby></span><ruby>八時<rt>はちじ</rt></ruby>から <span class="cn-word" data-tr="kunduzgi"><ruby>午後<rt>ごご</rt></ruby></span><ruby>四時<rt>よじ</rt></ruby>まで <ruby>働<rt>はたら</rt></ruby>きます。</p>

<p><strong>シェルベク:</strong> <ruby>日本語<rt>にほんご</rt></ruby>の <span class="cn-word" data-tr="dars"><ruby>授業<rt>じゅぎょう</rt></ruby></span>は <ruby>何時<rt>なんじ</rt></ruby>に <span class="cn-word" data-pos="verb" data-tr="boshlanadi"><ruby>始<rt>はじ</rt></ruby>まります</span>か。</p>

<p><strong>やまだ:</strong> <ruby>九時半<rt>くじはん</rt></ruby>に <ruby>始<rt>はじ</rt></ruby>まります。<ruby>月曜日<rt>げつようび</rt></ruby>から <ruby>金曜日<rt>きんようび</rt></ruby>まで あります。</p>

<p><strong>シェルベク:</strong> <ruby>土曜日<rt>どようび</rt></ruby>と <ruby>日曜日<rt>にちようび</rt></ruby>は？</p>

<p><strong>やまだ:</strong> <ruby>土曜日<rt>どようび</rt></ruby>と <ruby>日曜日<rt>にちようび</rt></ruby>は <ruby>学校<rt>がっこう</rt></ruby>へ <ruby>来<rt>き</rt></ruby>ません。<ruby>家<rt>いえ</rt></ruby>で <ruby>本<rt>ほん</rt></ruby>を <ruby>読<rt>よ</rt></ruby>みます。</p>

<p><strong>シェルベク:</strong> <ruby>私<rt>わたし</rt></ruby>の<ruby>家<rt>いえ</rt></ruby>から <ruby>学校<rt>がっこう</rt></ruby>まで <ruby>四十分<rt>よんじゅっぷん</rt></ruby>です。</p>

<p><strong>やまだ:</strong> <ruby>四十分<rt>よんじゅっぷん</rt></ruby>ですか。<ruby>何時<rt>なんじ</rt></ruby>に <ruby>起<rt>お</rt></ruby>きますか。</p>

<p><strong>シェルベク:</strong> <ruby>六時半<rt>ろくじはん</rt></ruby>に <ruby>起<rt>お</rt></ruby>きます。バスで <ruby>来<rt>き</rt></ruby>ます。</p>''',
        "questions": [
            {
                "text": "やまだ<ruby>先生<rt>せんせい</rt></ruby>は <ruby>何時<rt>なんじ</rt></ruby>から <ruby>何時<rt>なんじ</rt></ruby>まで <ruby>働<rt>はたら</rt></ruby>きますか。",
                "choices": [
                    "<ruby>九時半<rt>くじはん</rt></ruby>から<ruby>四時<rt>よじ</rt></ruby>まで",
                    "<ruby>八時<rt>はちじ</rt></ruby>から<ruby>四時<rt>よじ</rt></ruby>まで",
                    "<ruby>八時<rt>はちじ</rt></ruby>から<ruby>五時<rt>ごじ</rt></ruby>まで",
                    "<ruby>六時半<rt>ろくじはん</rt></ruby>から<ruby>四時<rt>よじ</rt></ruby>まで",
                ],
                "answer": 1,
                "explanation": "«午前八時から 午後四時まで 働きます». 九時半 esa "
                               "<em>darsning</em> boshlanish vaqti, ish vaqti emas. "
                               "Diqqat: 四時 «よじ» deb oʻqiladi, «よんじ» emas.",
            },
            {
                "text": "なぜ「<ruby>九時半<rt>くじはん</rt></ruby>に <ruby>始<rt>はじ</rt></ruby>まります」に に が ありますが、"
                        "「<ruby>九時<rt>くじ</rt></ruby>から」に ありませんか。",
                "choices": [
                    "から が じかんの かんけいを あらわしますから",
                    "<ruby>九時半<rt>くじはん</rt></ruby>は ながいですから",
                    "に は あさだけ つかいますから",
                    "から は ふるい ことばですから",
                ],
                "answer": 0,
                "explanation": "から va まで <strong>oʻzi</strong> vaqt munosabatini "
                               "bildiradi, shuning uchun に ortiqcha. Yolgʻiz turgan "
                               "aniq vaqtga esa に qoʻyiladi: 九時半に 始まります.",
            },
            {
                "text": "シェルベクさんの<ruby>家<rt>いえ</rt></ruby>から <ruby>学校<rt>がっこう</rt></ruby>まで どのくらいですか。",
                "choices": [
                    "<ruby>三十分<rt>さんじゅっぷん</rt></ruby>です",
                    "<ruby>四十分<rt>よんじゅっぷん</rt></ruby>です",
                    "<ruby>一時間<rt>いちじかん</rt></ruby>です",
                    "<ruby>十分<rt>じゅっぷん</rt></ruby>です",
                ],
                "answer": 1,
                "explanation": "«四十分です» — qirq daqiqa. Bu yerda から…まで "
                               "<strong>joy</strong> uchun ishlatilgan, vaqt uchun "
                               "emas: «uydan maktabgacha».",
            },
        ],
    },
]
