# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-19 … PJ-21.

⚠️ PJ-20 dan boshlab «hikoya ramkasi» istisnosi TUGAYDI — oʻquvchi endi
〜ます va 〜ません ni biladi, shuning uchun matndagi har bir feʼl darslarda
berilgan boʻlishi shart.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_19_21.py --author=prime
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
        "title":   "わたしも がくせいです",
        "summary": (
            "PJ-19 matni. Kutubxonada uch kishi tanishadi — va «も» har safar «ham» "
            "deganda は ni siqib chiqarayotgani koʻrinadi."
        ),
        "order":   19,
        "grammar": [
            {
                "pattern":  "〜も",
                "meaning":  "«…ham». は va が ni SIQIB CHIQARADI — ular bilan birga "
                            "turmaydi. Boshqa qoʻshimchalar bilan esa birga ishlaydi.",
                "examples": ["<ruby>私<rt>わたし</rt></ruby>も<ruby>学生<rt>がくせい</rt></ruby>です。",
                             "<ruby>学校<rt>がっこう</rt></ruby>にも<ruby>本<rt>ほん</rt></ruby>があります。"],
            },
            {
                "pattern":  "A と B",
                "meaning":  "«A va B» — roʻyxat TOʻLIQ, sanalganlardan boshqa yoʻq. "
                            "Ikkinchi maʼnosi: «bilan».",
                "examples": ["<ruby>本<rt>ほん</rt></ruby>と<ruby>鞄<rt>かばん</rt></ruby>",
                             "<ruby>友達<rt>ともだち</rt></ruby>と<ruby>教室<rt>きょうしつ</rt></ruby>にいます。"],
            },
            {
                "pattern":  "A や B",
                "meaning":  "«A, B va shunga oʻxshashlar» — roʻyxat OCHIQ, namuna "
                            "keltirilgan xolos.",
                "examples": ["<ruby>本<rt>ほん</rt></ruby>や<ruby>雑誌<rt>ざっし</rt></ruby>があります。"],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="kutubxona"><ruby>図書館<rt>としょかん</rt></ruby></span>の<ruby>中<rt>なか</rt></ruby>に アフソナさんと <span class="cn-word" data-tr="Sherbek">シェルベク</span>さんが います。<ruby>机<rt>つくえ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に <ruby>本<rt>ほん</rt></ruby>や <span class="cn-word" data-tr="jurnal"><ruby>雑誌<rt>ざっし</rt></ruby></span>が あります。</p>

<p><strong>シェルベク:</strong> アフソナさんは <ruby>学生<rt>がくせい</rt></ruby>ですか。</p>

<p><strong>アフソナ:</strong> はい。シェルベクさんは？</p>

<p><strong>シェルベク:</strong> <ruby>私<rt>わたし</rt></ruby>も <ruby>学生<rt>がくせい</rt></ruby>です。</p>

<p>そのとき <span class="cn-word" data-tr="Dilnoza">ディルノザ</span>さんが <span class="cn-word" data-pos="verb" data-tr="keldi"><ruby>来<rt>き</rt></ruby>ました</span>。</p>

<p><strong>ディルノザ:</strong> <ruby>私<rt>わたし</rt></ruby>も ここに います！</p>

<p><strong>アフソナ:</strong> ディルノザさんの<ruby>鞄<rt>かばん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に <ruby>何<rt>なに</rt></ruby>が ありますか。</p>

<p><strong>ディルノザ:</strong> <ruby>本<rt>ほん</rt></ruby>と <span class="cn-word" data-tr="daftar">ノート</span>と <ruby>時計<rt>とけい</rt></ruby>が あります。</p>

<p><strong>シェルベク:</strong> <ruby>私<rt>わたし</rt></ruby>の<ruby>鞄<rt>かばん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>にも <ruby>本<rt>ほん</rt></ruby>が あります。でも <ruby>時計<rt>とけい</rt></ruby>は ありません。</p>

<p><strong>ディルノザ:</strong> <span class="cn-word" data-tr="mana">じゃあ</span>、これは シェルベクさんの<ruby>時計<rt>とけい</rt></ruby>ですか。</p>

<p><strong>シェルベク:</strong> あ！ <ruby>私<rt>わたし</rt></ruby>のです。</p>''',
        "questions": [
            {
                "text": "シェルベクさんの<ruby>鞄<rt>かばん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に <ruby>時計<rt>とけい</rt></ruby>が ありますか。",
                "choices": [
                    "はい、あります",
                    "いいえ、ありません",
                    "はい、います",
                    "いいえ、いません",
                ],
                "answer": 1,
                "explanation": "Sherbek «時計は ありません» dedi — soat sumkasida yoʻq "
                               "edi, chunki u stolda qolgan edi. Soat jonsiz narsa, "
                               "shuning uchun ありません (いません emas).",
            },
            {
                "text": "「<ruby>私<rt>わたし</rt></ruby>も<ruby>学生<rt>がくせい</rt></ruby>です」に なぜ は が ありませんか。",
                "choices": [
                    "も が は を おしのけますから",
                    "は は いつも ありませんから",
                    "<ruby>学生<rt>がくせい</rt></ruby>は めいしですから",
                    "しつもんですから",
                ],
                "answer": 0,
                "explanation": "も は va が ni <strong>siqib chiqaradi</strong> — ular "
                               "bir joyda tura olmaydi. «私はも» degan shakl yapon "
                               "tilida mavjud emas.",
            },
            {
                "text": "<ruby>机<rt>つくえ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に <ruby>本<rt>ほん</rt></ruby>や<ruby>雑誌<rt>ざっし</rt></ruby>が あります。ほかの ものも ありますか。",
                "choices": [
                    "いいえ、<ruby>本<rt>ほん</rt></ruby>と<ruby>雑誌<rt>ざっし</rt></ruby>だけです",
                    "はい、ほかの ものも あります",
                    "わかりません",
                    "<ruby>机<rt>つくえ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に <ruby>何<rt>なに</rt></ruby>も ありません",
                ],
                "answer": 1,
                "explanation": "や ishlatilgani uchun roʻyxat <strong>ochiq</strong> — "
                               "«kitob, jurnal va shunga oʻxshashlar». Agar と "
                               "ishlatilganda, roʻyxat toʻliq boʻlardi va boshqa hech "
                               "narsa yoʻqligini bildirardi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "まいにち にほんごを べんきょうします",
        "summary": (
            "PJ-20 matni. Afsonaning bir kuni — birinchi marta matndagi odamlar "
            "gapiribgina qolmay, ish ham qiladi."
        ),
        "order":   20,
        "grammar": [
            {
                "pattern":  "〜ます",
                "meaning":  "Muloyim feʼl shakli. Shaxsga qarab OʻZGARMAYDI, va "
                            "hozirgi hamda kelasi zamon uchun bitta shakl.",
                "examples": ["<ruby>毎日<rt>まいにち</rt></ruby><ruby>勉強<rt>べんきょう</rt></ruby>します。",
                             "<ruby>明日<rt>あした</rt></ruby><ruby>行<rt>い</rt></ruby>きます。"],
            },
            {
                "pattern":  "〜ません",
                "meaning":  "Inkor: ます oʻrniga ません. Boshqa hech narsa oʻzgarmaydi.",
                "examples": ["<ruby>肉<rt>にく</rt></ruby>を<ruby>食<rt>た</rt></ruby>べません。"],
            },
            {
                "pattern":  "Vaqt soʻzi + feʼl",
                "meaning":  "Yapon tilida kelasi zamon YOʻQ — zamonni vaqt soʻzi "
                            "koʻrsatadi, feʼl emas.",
                "examples": ["<ruby>今日<rt>きょう</rt></ruby><ruby>読<rt>よ</rt></ruby>みます。",
                             "<ruby>明日<rt>あした</rt></ruby><ruby>読<rt>よ</rt></ruby>みます。"],
            },
        ],
        "body": '''<p>アフソナさんは <ruby>毎日<rt>まいにち</rt></ruby> <ruby>七時<rt>しちじ</rt></ruby>に <ruby>起<rt>お</rt></ruby>きます。<span class="cn-word" data-tr="ertalab"><ruby>朝<rt>あさ</rt></ruby></span>、コーヒーを <ruby>飲<rt>の</rt></ruby>みます。</p>

<p><ruby>八時<rt>はちじ</rt></ruby>に <ruby>学校<rt>がっこう</rt></ruby>に <ruby>行<rt>い</rt></ruby>きます。<ruby>教室<rt>きょうしつ</rt></ruby>で <span class="cn-word" data-tr="yapon tili"><ruby>日本語<rt>にほんご</rt></ruby></span>を <span class="cn-word" data-tr="oʻqiyman"><ruby>勉強<rt>べんきょう</rt></ruby>します</span>。</p>

<p><strong>やまだ:</strong> アフソナさんは <ruby>毎日<rt>まいにち</rt></ruby> <ruby>勉強<rt>べんきょう</rt></ruby>しますか。</p>

<p><strong>アフソナ:</strong> はい、<ruby>毎日<rt>まいにち</rt></ruby> します。でも <ruby>日曜日<rt>にちようび</rt></ruby>は しません。</p>

<p><strong>やまだ:</strong> <ruby>日曜日<rt>にちようび</rt></ruby>は <ruby>何<rt>なに</rt></ruby>を しますか。</p>

<p><strong>アフソナ:</strong> <span class="cn-word" data-tr="kino"><ruby>映画<rt>えいが</rt></ruby></span>を <ruby>見<rt>み</rt></ruby>ます。<span class="cn-word" data-tr="xat"><ruby>手紙<rt>てがみ</rt></ruby></span>も <ruby>書<rt>か</rt></ruby>きます。</p>

<p><strong>やまだ:</strong> <ruby>明日<rt>あした</rt></ruby>も <ruby>学校<rt>がっこう</rt></ruby>に <ruby>来<rt>き</rt></ruby>ますか。</p>

<p><strong>アフソナ:</strong> はい、<ruby>来<rt>き</rt></ruby>ます。</p>

<p><ruby>五時<rt>ごじ</rt></ruby>に アフソナさんは <span class="cn-word" data-tr="uy"><ruby>家<rt>いえ</rt></ruby></span>に <ruby>帰<rt>かえ</rt></ruby>ります。<ruby>夜<rt>よる</rt></ruby>、<ruby>本<rt>ほん</rt></ruby>を <ruby>読<rt>よ</rt></ruby>みます。テレビは <ruby>見<rt>み</rt></ruby>ません。</p>''',
        "questions": [
            {
                "text": "アフソナさんは <ruby>日曜日<rt>にちようび</rt></ruby>に <ruby>勉強<rt>べんきょう</rt></ruby>しますか。",
                "choices": [
                    "はい、します",
                    "いいえ、しません",
                    "はい、<ruby>毎日<rt>まいにち</rt></ruby>します",
                    "いいえ、<ruby>映画<rt>えいが</rt></ruby>を<ruby>見<rt>み</rt></ruby>ます",
                ],
                "answer": 1,
                "explanation": "«でも 日曜日は しません» — yakshanba kuni oʻqimaydi. "
                               "Bu yerda は qarama-qarshi qoʻyish uchun ishlatilgan: "
                               "«boshqa kunlari qiladi, yakshanba esa yoʻq».",
            },
            {
                "text": "「<ruby>明日<rt>あした</rt></ruby>も <ruby>来<rt>き</rt></ruby>ます」— これは いつですか。",
                "choices": [
                    "<ruby>今<rt>いま</rt></ruby>です",
                    "<ruby>昨日<rt>きのう</rt></ruby>です",
                    "<ruby>未来<rt>みらい</rt></ruby>です",
                    "<ruby>毎日<rt>まいにち</rt></ruby>です",
                ],
                "answer": 2,
                "explanation": "Kelasi zamon — lekin feʼl shakli hozirgi bilan "
                               "<strong>bir xil</strong>. Yapon tilida alohida kelasi "
                               "zamon yoʻq; zamonni 明日 («ertaga») koʻrsatadi.",
            },
            {
                "text": "アフソナさんは <ruby>夜<rt>よる</rt></ruby> テレビを <ruby>見<rt>み</rt></ruby>ますか。",
                "choices": [
                    "はい、<ruby>見<rt>み</rt></ruby>ます",
                    "いいえ、<ruby>見<rt>み</rt></ruby>ません",
                    "はい、<ruby>映画<rt>えいが</rt></ruby>を<ruby>見<rt>み</rt></ruby>ます",
                    "いいえ、<ruby>本<rt>ほん</rt></ruby>を<ruby>見<rt>み</rt></ruby>ます",
                ],
                "answer": 1,
                "explanation": "Oxirgi jumla: «テレビは 見ません». Kechqurun kitob "
                               "oʻqiydi, televizor koʻrmaydi. Kino esa yakshanba "
                               "kuni koʻradi — boshqa kun.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "ジャスルさんの いちにち",
        "summary": (
            "PJ-21 matni. Jasurning bir kuni — を va に har jumlada yonma-yon "
            "ishlaydi va farqi oʻz-oʻzidan koʻrinadi."
        ),
        "order":   21,
        "grammar": [
            {
                "pattern":  "〜を + feʼl",
                "meaning":  "Toʻldiruvchi qoʻshimchasi — oʻzbekchadagi «-ni». "
                            "Faqat oʻtimli feʼllar oladi. [o] deb oʻqiladi.",
                "examples": ["<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みます。",
                             "<ruby>水<rt>みず</rt></ruby>を<ruby>飲<rt>の</rt></ruby>みます。"],
            },
            {
                "pattern":  "〜に + <ruby>行<rt>い</rt></ruby>きます / <ruby>来<rt>き</rt></ruby>ます",
                "meaning":  "Yoʻnalish — oʻzbekchadagi «-ga». «Nimani boraman?» "
                            "maʼnosiz, shuning uchun bunday feʼl を olmaydi.",
                "examples": ["<ruby>学校<rt>がっこう</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。"],
            },
            {
                "pattern":  "SON + <ruby>時<rt>じ</rt></ruby> + に",
                "meaning":  "Aniq vaqtga に qoʻyiladi. Lekin <ruby>今日<rt>きょう</rt></ruby>, "
                            "<ruby>明日<rt>あした</rt></ruby>, <ruby>毎日<rt>まいにち</rt></ruby> ga "
                            "に QOʻYILMAYDI.",
                "examples": ["<ruby>七時<rt>しちじ</rt></ruby>に<ruby>起<rt>お</rt></ruby>きます。",
                             "<ruby>明日<rt>あした</rt></ruby><ruby>行<rt>い</rt></ruby>きます。"],
            },
        ],
        "body": '''<p>ジャスルさんは <ruby>毎朝<rt>まいあさ</rt></ruby> <ruby>六時<rt>ろくじ</rt></ruby>に <ruby>起<rt>お</rt></ruby>きます。<ruby>水<rt>みず</rt></ruby>を <ruby>飲<rt>の</rt></ruby>みます。コーヒーは <ruby>飲<rt>の</rt></ruby>みません。</p>

<p><ruby>七時<rt>しちじ</rt></ruby>に <ruby>学校<rt>がっこう</rt></ruby>に <ruby>行<rt>い</rt></ruby>きます。<span class="cn-word" data-tr="doʻst"><ruby>友達<rt>ともだち</rt></ruby></span>と <ruby>行<rt>い</rt></ruby>きます。</p>

<p><strong>アフソナ:</strong> ジャスルさんは <ruby>朝<rt>あさ</rt></ruby> <ruby>何<rt>なに</rt></ruby>を <ruby>食<rt>た</rt></ruby>べますか。</p>

<p><strong>ジャスル:</strong> パンを <ruby>食<rt>た</rt></ruby>べます。<span class="cn-word" data-tr="goʻsht"><ruby>肉<rt>にく</rt></ruby></span>は <ruby>食<rt>た</rt></ruby>べません。</p>

<p><strong>アフソナ:</strong> <ruby>学校<rt>がっこう</rt></ruby>で <ruby>何<rt>なに</rt></ruby>を しますか。</p>

<p><strong>ジャスル:</strong> <ruby>日本語<rt>にほんご</rt></ruby>を <ruby>勉強<rt>べんきょう</rt></ruby>します。<span class="cn-word" data-tr="kanji"><ruby>漢字<rt>かんじ</rt></ruby></span>も <ruby>書<rt>か</rt></ruby>きます。</p>

<p><ruby>四時<rt>よじ</rt></ruby>に ジャスルさんは <ruby>家<rt>いえ</rt></ruby>に <ruby>帰<rt>かえ</rt></ruby>ります。<span class="cn-word" data-tr="kechqurun"><ruby>夜<rt>よる</rt></ruby></span>、<span class="cn-word" data-tr="musiqa"><ruby>音楽<rt>おんがく</rt></ruby></span>を <ruby>聞<rt>き</rt></ruby>きます。</p>

<p><strong>アフソナ:</strong> <ruby>明日<rt>あした</rt></ruby>も <ruby>六時<rt>ろくじ</rt></ruby>に <ruby>起<rt>お</rt></ruby>きますか。</p>

<p><strong>ジャスル:</strong> いいえ。<ruby>明日<rt>あした</rt></ruby>は <ruby>日曜日<rt>にちようび</rt></ruby>です！ <ruby>十時<rt>じゅうじ</rt></ruby>に <ruby>起<rt>お</rt></ruby>きます。</p>''',
        "questions": [
            {
                "text": "ジャスルさんは <ruby>朝<rt>あさ</rt></ruby> <ruby>何<rt>なに</rt></ruby>を <ruby>飲<rt>の</rt></ruby>みますか。",
                "choices": [
                    "コーヒーを<ruby>飲<rt>の</rt></ruby>みます",
                    "<ruby>水<rt>みず</rt></ruby>を<ruby>飲<rt>の</rt></ruby>みます",
                    "<ruby>何<rt>なに</rt></ruby>も<ruby>飲<rt>の</rt></ruby>みません",
                    "パンを<ruby>飲<rt>の</rt></ruby>みます",
                ],
                "answer": 1,
                "explanation": "«水を 飲みます。コーヒーは 飲みません» — suv ichadi, "
                               "kofe ichmaydi. Diqqat: inkor gapda を oʻrniga は "
                               "kelgan — bu qarama-qarshi qoʻyish.",
            },
            {
                "text": "なぜ「<ruby>学校<rt>がっこう</rt></ruby>に <ruby>行<rt>い</rt></ruby>きます」と いいますか、"
                        "「<ruby>学校<rt>がっこう</rt></ruby>を <ruby>行<rt>い</rt></ruby>きます」と いいませんか。",
                "choices": [
                    "<ruby>学校<rt>がっこう</rt></ruby>は ばしょですから",
                    "<ruby>行<rt>い</rt></ruby>きます は「なにを?」の しつもんに こたえませんから",
                    "を は ふるい ことばですから",
                    "に の ほうが みじかいですから",
                ],
                "answer": 1,
                "explanation": "«Nimani boraman?» degan savol maʼnosiz — 行きます "
                               "toʻldiruvchi olmaydi. Bunday feʼl <strong>に</strong> "
                               "bilan yoʻnalishni oladi. Oʻzbekchada ham «maktabni "
                               "boraman» notoʻgʻri.",
            },
            {
                "text": "<ruby>明日<rt>あした</rt></ruby> ジャスルさんは <ruby>何時<rt>なんじ</rt></ruby>に <ruby>起<rt>お</rt></ruby>きますか。",
                "choices": [
                    "<ruby>六時<rt>ろくじ</rt></ruby>に<ruby>起<rt>お</rt></ruby>きます",
                    "<ruby>七時<rt>しちじ</rt></ruby>に<ruby>起<rt>お</rt></ruby>きます",
                    "<ruby>十時<rt>じゅうじ</rt></ruby>に<ruby>起<rt>お</rt></ruby>きます",
                    "<ruby>四時<rt>よじ</rt></ruby>に<ruby>起<rt>お</rt></ruby>きます",
                ],
                "answer": 2,
                "explanation": "«明日は 日曜日です！ 十時に 起きます» — ertaga yakshanba, "
                               "shuning uchun soat oʻnda turadi. Diqqat: 十時 <strong>ga "
                               "に qoʻyilgan</strong> (aniq vaqt), 明日 ga esa "
                               "<strong>qoʻyilmagan</strong>.",
            },
        ],
    },
]
