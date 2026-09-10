# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-37 … PJ-39.

PJ-37 ish tartibi · PJ-38 〜ながら · PJ-39 xohish.
⚠️ PJ-37 da ながら YOʻQ, PJ-38 da たい YOʻQ — har bir matn faqat oʻz
   darsigacha berilganini ishlatadi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_37_39.py --author=prime
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
        "title":   "いえを でるまえに",
        "summary": (
            "PJ-37 matni. Munira ertalabki tartibini aytadi — 〜てから, "
            "〜まえに va 〜たあとで bir matnda, va uchtasining oʻzagi har xil."
        ),
        "order":   37,
        "grammar": [
            {
                "pattern":  "〜てから",
                "meaning":  "«…gandan keyin». て-shakli + から. Birinchi ish "
                            "tugashi taʼkidlanadi.",
                "examples": ["<ruby>起<rt>お</rt></ruby>きてから<ruby>顔<rt>かお</rt></ruby>を<ruby>洗<rt>あら</rt></ruby>います。"],
            },
            {
                "pattern":  "〜まえに",
                "meaning":  "«…dan oldin». Oldida DOIM lugʻat shakli turadi — "
                            "gap qaysi zamonda boʻlishidan qatʼi nazar.",
                "examples": ["<ruby>家<rt>いえ</rt></ruby>を<ruby>出<rt>で</rt></ruby>るまえに",
                             "<ruby>寝<rt>ね</rt></ruby>るまえに<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みました。"],
            },
            {
                "pattern":  "〜たあとで · OT + のあとで",
                "meaning":  "«…gandan keyin». Oldida DOIM た-shakli; ot bilan "
                            "ulanganda esa の qoʻyiladi.",
                "examples": ["<ruby>食<rt>た</rt></ruby>べたあとで",
                             "<ruby>授業<rt>じゅぎょう</rt></ruby>のあとで"],
            },
        ],
        "body": '''<p>ムニラさんの<ruby>朝<rt>あさ</rt></ruby>は<ruby>毎日<rt>まいにち</rt></ruby><ruby>同<rt>おな</rt></ruby>じです。<ruby>六時<rt>ろくじ</rt></ruby>に<ruby>起<rt>お</rt></ruby>きてから、<span class="cn-word" data-tr="yuz"><ruby>顔<rt>かお</rt></ruby></span>を<span class="cn-word" data-tr="yuvadi"><ruby>洗<rt>あら</rt></ruby>います</span>。</p>

<p><strong>ラノ:</strong> ムニラさんは<ruby>朝<rt>あさ</rt></ruby>ごはんを<ruby>食<rt>た</rt></ruby>べたあとで<ruby>何<rt>なに</rt></ruby>をしますか。</p>

<p><strong>ムニラ:</strong> <span class="cn-word" data-tr="chiqishdan oldin"><ruby>家<rt>いえ</rt></ruby>を<ruby>出<rt>で</rt></ruby>るまえに</span><ruby>宿題<rt>しゅくだい</rt></ruby>を<ruby>見<rt>み</rt></ruby>ます。<ruby>時々<rt>ときどき</rt></ruby><ruby>母<rt>はは</rt></ruby>を<ruby>手伝<rt>てつだ</rt></ruby>います。</p>

<p><strong>ラノ:</strong> <ruby>私<rt>わたし</rt></ruby>は<ruby>宿題<rt>しゅくだい</rt></ruby>を<ruby>見<rt>み</rt></ruby>ません。<ruby>朝<rt>あさ</rt></ruby>は<span class="cn-word" data-tr="vaqt"><ruby>時間<rt>じかん</rt></ruby></span>がありません。</p>

<p><strong>ムニラ:</strong> <span class="cn-word" data-tr="dars"><ruby>授業<rt>じゅぎょう</rt></ruby></span>のあとで<ruby>図書館<rt>としょかん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きますか。</p>

<p><strong>ラノ:</strong> はい。でも<ruby>今日<rt>きょう</rt></ruby>は<ruby>友<rt>とも</rt></ruby>だちに<ruby>会<rt>あ</rt></ruby>ってから<ruby>行<rt>い</rt></ruby>きます。</p>

<p><ruby>昨日<rt>きのう</rt></ruby>ムニラさんは<ruby>寝<rt>ね</rt></ruby>るまえに<ruby>日本語<rt>にほんご</rt></ruby>の<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みました。<span class="cn-word" data-tr="ovqatlanish"><ruby>食事<rt>しょくじ</rt></ruby></span>のまえにも<ruby>読<rt>よ</rt></ruby>みました。</p>

<p><ruby>二人<rt>ふたり</rt></ruby>は<ruby>教室<rt>きょうしつ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>ってから、<span class="cn-word" data-tr="oʻtirishdi"><ruby>座<rt>すわ</rt></ruby>りました</span>。</p>''',
        "questions": [
            {
                "text": "ムニラさんは<ruby>家<rt>いえ</rt></ruby>を<ruby>出<rt>で</rt></ruby>るまえに<ruby>何<rt>なに</rt></ruby>をしますか。",
                "choices": [
                    "<ruby>顔<rt>かお</rt></ruby>を<ruby>洗<rt>あら</rt></ruby>います",
                    "<ruby>宿題<rt>しゅくだい</rt></ruby>を<ruby>見<rt>み</rt></ruby>ます",
                    "<ruby>図書館<rt>としょかん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きます",
                    "<ruby>友<rt>とも</rt></ruby>だちに<ruby>会<rt>あ</rt></ruby>います",
                ],
                "answer": 1,
                "explanation": "«家を 出るまえに 宿題を 見ます» — uydan chiqishdan "
                               "oldin uy vazifasini koʻradi. Yuzini esa turgandan "
                               "keyin yuvadi.",
            },
            {
                "text": "«<ruby>昨日<rt>きのう</rt></ruby>…<ruby>寝<rt>ね</rt></ruby>るまえに…<ruby>読<rt>よ</rt></ruby>みました» — nega <ruby>寝<rt>ね</rt></ruby>た emas?",
                "choices": [
                    "まえに oldida doim lugʻat shakli turadi",
                    "Chunki gap oʻtgan zamonda emas",
                    "Chunki 寝る — II guruh feʼli",
                    "Chunki 昨日 soʻzi bor",
                ],
                "answer": 0,
                "explanation": "Oʻzakni <strong>qolip</strong> tanlaydi, gapning zamoni "
                               "emas. まえに doim lugʻat shaklini oladi; oʻtgan zamonni "
                               "esa oxirgi feʼl (読みました) tashiydi.",
            },
            {
                "text": "«<ruby>授業<rt>じゅぎょう</rt></ruby>のあとで» — nega の bor?",
                "choices": [
                    "Chunki oldida ot turibdi",
                    "Chunki あと — feʼl",
                    "Chunki gap savol",
                    "Chunki 授業 uzun soʻz",
                ],
                "answer": 0,
                "explanation": "あと va まえ ning oʻzi ham ot, shuning uchun ular "
                               "oldidagi otga <strong>の</strong> bilan ulanadi. Feʼl "
                               "oldida esa の qoʻyilmaydi: 出るまえに.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "おんがくを ききながら",
        "summary": (
            "PJ-38 matni. Kim qanday oʻqiydi — musiqa bilanmi, jimjitmi. "
            "Matn 〜ながら ustida turadi va oxirgi feʼl har doim asosiy ish."
        ),
        "order":   38,
        "grammar": [
            {
                "pattern":  "ます oʻzagi + ながら",
                "meaning":  "«…gan holda». Ikki ish bir vaqtda ketadi. "
                            "ながら hech qachon zamon olmaydi.",
                "examples": ["<ruby>音楽<rt>おんがく</rt></ruby>を<ruby>聞<rt>き</rt></ruby>きながら<ruby>勉強<rt>べんきょう</rt></ruby>します。"],
            },
            {
                "pattern":  "Asosiy ish — oxirgi feʼl",
                "meaning":  "ながら bilan belgilangan ish ikkinchi darajali; "
                            "gapning asl mazmuni oxirgi feʼlda.",
                "examples": ["<ruby>歩<rt>ある</rt></ruby>きながら<ruby>話<rt>はな</rt></ruby>しました。"],
            },
            {
                "pattern":  "Ega bitta boʻlishi shart",
                "meaning":  "Ikkala ishni ham bir odam bajaradi. Ikki egali "
                            "gapni ながら bilan tuzib boʻlmaydi.",
                "examples": ["<ruby>働<rt>はたら</rt></ruby>きながら<ruby>勉強<rt>べんきょう</rt></ruby>します。"],
            },
        ],
        "body": '''<p><ruby>試験<rt>しけん</rt></ruby>のまえの<ruby>夜<rt>よる</rt></ruby>です。イノムさんとパリさんは<ruby>図書館<rt>としょかん</rt></ruby>にいます。</p>

<p><strong>イノム:</strong> パリさんは<span class="cn-word" data-tr="musiqa"><ruby>音楽<rt>おんがく</rt></ruby></span>を<ruby>聞<rt>き</rt></ruby>きながら<ruby>勉強<rt>べんきょう</rt></ruby>しますか。</p>

<p><strong>パリ:</strong> はい、いつも<ruby>聞<rt>き</rt></ruby>きながら<ruby>勉強<rt>べんきょう</rt></ruby>します。<ruby>静<rt>しず</rt></ruby>かな<ruby>所<rt>ところ</rt></ruby>は<ruby>好<rt>す</rt></ruby>きではありません。</p>

<p><strong>イノム:</strong> <ruby>私<rt>わたし</rt></ruby>は<ruby>音楽<rt>おんがく</rt></ruby>を<ruby>聞<rt>き</rt></ruby>きながら<ruby>勉強<rt>べんきょう</rt></ruby>しません。<ruby>静<rt>しず</rt></ruby>かな<ruby>所<rt>ところ</rt></ruby>が<ruby>好<rt>す</rt></ruby>きです。</p>

<p><strong>パリ:</strong> そうですか。</p>

<p><strong>イノム:</strong> でも<ruby>家<rt>いえ</rt></ruby>で<span class="cn-word" data-tr="ovqatlanib"><ruby>食<rt>た</rt></ruby>べながら</span>テレビを<ruby>見<rt>み</rt></ruby>ます。</p>

<p><strong>パリ:</strong> イムロンさんは<span class="cn-word" data-tr="ishlab"><ruby>働<rt>はたら</rt></ruby>きながら</span><ruby>勉強<rt>べんきょう</rt></ruby>しています。<span class="cn-word" data-tr="yarim kunlik ish">アルバイト</span>があります。</p>

<p><strong>イノム:</strong> <ruby>大変<rt>たいへん</rt></ruby>ですね。</p>

<p><ruby>二人<rt>ふたり</rt></ruby>は<ruby>十時<rt>じゅうじ</rt></ruby>まで<ruby>勉強<rt>べんきょう</rt></ruby>しました。それから<span class="cn-word" data-tr="yurgan holda"><ruby>歩<rt>ある</rt></ruby>きながら</span><ruby>家<rt>いえ</rt></ruby>へ<ruby>帰<rt>かえ</rt></ruby>りました。</p>''',
        "questions": [
            {
                "text": "パリさんはどうやって<ruby>勉強<rt>べんきょう</rt></ruby>しますか。",
                "choices": [
                    "<ruby>静<rt>しず</rt></ruby>かな<ruby>所<rt>ところ</rt></ruby>で<ruby>勉強<rt>べんきょう</rt></ruby>します",
                    "<ruby>音楽<rt>おんがく</rt></ruby>を<ruby>聞<rt>き</rt></ruby>きながら<ruby>勉強<rt>べんきょう</rt></ruby>します",
                    "テレビを<ruby>見<rt>み</rt></ruby>ながら<ruby>勉強<rt>べんきょう</rt></ruby>します",
                    "<ruby>働<rt>はたら</rt></ruby>きながら<ruby>勉強<rt>べんきょう</rt></ruby>します",
                ],
                "answer": 1,
                "explanation": "«いつも 聞きながら 勉強します» — doim musiqa bilan. "
                               "Jimjit joyni yoqtirmaydi. Ishlab oʻqiydigani esa Imron.",
            },
            {
                "text": "«<ruby>音楽<rt>おんがく</rt></ruby>を<ruby>聞<rt>き</rt></ruby>きながら<ruby>勉強<rt>べんきょう</rt></ruby>します» — asosiy ish qaysi?",
                "choices": [
                    "Musiqa tinglash",
                    "Oʻqish",
                    "Ikkalasi teng",
                    "Aniqlab boʻlmaydi",
                ],
                "answer": 1,
                "explanation": "Asosiy ish har doim <strong>oxirgi feʼl</strong>da — "
                               "bu yerda 勉強します. ながら bilan belgilangan ish "
                               "(tinglash) fon boʻlib qoladi.",
            },
            {
                "text": "«<ruby>働<rt>はたら</rt></ruby>きながら<ruby>勉強<rt>べんきょう</rt></ruby>しています» bu yerda nima maʼnoni beradi?",
                "choices": [
                    "Ayni daqiqada ish joyida oʻqiyapti",
                    "Ishlaydi va shu bilan birga oʻqiydi — hayotining bir davri",
                    "Ishlagandan keyin oʻqiydi",
                    "Ishlashni xohlaydi",
                ],
                "answer": 1,
                "explanation": "ながら uzun muddatga ham yaraydi: «bir vaqtda» degani "
                               "ayni daqiqa emas, <strong>hayotning bir davri</strong>. "
                               "«Ishlagandan keyin» boʻlsa <strong>働いてから</strong> "
                               "deyilardi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "にほんへ いきたいです",
        "summary": (
            "PJ-39 matni. Yozgi taʼtil rejalari — kim nima qilmoqchi va "
            "nimasi kerak. 〜たいです va 〜がほしいです yonma-yon."
        ),
        "order":   39,
        "grammar": [
            {
                "pattern":  "ます oʻzagi + たいです",
                "meaning":  "«…moqchiman». Natija い-sifat boʻladi: "
                            "たくないです, たかったです.",
                "examples": ["<ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きたいです。",
                             "<ruby>行<rt>い</rt></ruby>きたかったです。"],
            },
            {
                "pattern":  "OT + がほしいです",
                "meaning":  "«… kerak». ほしい — い-sifat, shuning uchun が "
                            "oladi, を emas.",
                "examples": ["お<ruby>金<rt>かね</rt></ruby>がほしいです。"],
            },
            {
                "pattern":  "Faqat oʻzi haqida",
                "meaning":  "Xohish — ichki tuygʻu, shuning uchun boshqa odam "
                            "haqida bunday aytilmaydi. Savolda esa mumkin.",
                "examples": ["<ruby>何<rt>なに</rt></ruby>がしたいですか。"],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="yozgi taʼtil"><ruby>夏休<rt>なつやす</rt></ruby>み</span>のまえの<ruby>金曜日<rt>きんようび</rt></ruby>です。<ruby>三人<rt>さんにん</rt></ruby>は<ruby>公園<rt>こうえん</rt></ruby>で<ruby>話<rt>はな</rt></ruby>しています。</p>

<p><strong>イムロン:</strong> みなさんは<ruby>夏休<rt>なつやす</rt></ruby>みに<ruby>何<rt>なに</rt></ruby>がしたいですか。</p>

<p><strong>ムニラ:</strong> <ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きたいです。<ruby>京都<rt>きょうと</rt></ruby>を<ruby>見<rt>み</rt></ruby>たいです。でも<span class="cn-word" data-tr="pul">お<ruby>金<rt>かね</rt></ruby></span>がほしいです。</p>

<p><strong>ラノ:</strong> <ruby>私<rt>わたし</rt></ruby>は<span class="cn-word" data-tr="velosiped"><ruby>自転車<rt>じてんしゃ</rt></ruby></span>がほしいです。<ruby>毎日<rt>まいにち</rt></ruby><ruby>公園<rt>こうえん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きたいです。</p>

<p><strong>イムロン:</strong> <ruby>私<rt>わたし</rt></ruby>は<span class="cn-word" data-tr="dam olmoq"><ruby>休<rt>やす</rt></ruby>みたい</span>です。<ruby>去年<rt>きょねん</rt></ruby>の<ruby>夏<rt>なつ</rt></ruby>は<ruby>働<rt>はたら</rt></ruby>きました。<span class="cn-word" data-tr="dam olmoqchi edim"><ruby>休<rt>やす</rt></ruby>みたかった</span>です。</p>

<p><strong>ムニラ:</strong> <ruby>今年<rt>ことし</rt></ruby>は<ruby>働<rt>はたら</rt></ruby>きたくないですか。</p>

<p><strong>イムロン:</strong> はい、<span class="cn-word" data-tr="ishlamoqchi emasman"><ruby>働<rt>はたら</rt></ruby>きたくない</span>です。<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>んだり、<ruby>泳<rt>およ</rt></ruby>いだりしたいです。</p>

<p><strong>ラノ:</strong> <ruby>私<rt>わたし</rt></ruby>も<ruby>海<rt>うみ</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きたいです。</p>

<p><ruby>三人<rt>さんにん</rt></ruby>は<ruby>夏休<rt>なつやす</rt></ruby>みの<ruby>話<rt>はなし</rt></ruby>をしながら<ruby>家<rt>いえ</rt></ruby>へ<ruby>帰<rt>かえ</rt></ruby>りました。</p>''',
        "questions": [
            {
                "text": "ムニラさんは<ruby>夏休<rt>なつやす</rt></ruby>みに<ruby>何<rt>なに</rt></ruby>がしたいですか。",
                "choices": [
                    "<ruby>自転車<rt>じてんしゃ</rt></ruby>がほしいです",
                    "<ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きたいです",
                    "<ruby>休<rt>やす</rt></ruby>みたいです",
                    "<ruby>働<rt>はたら</rt></ruby>きたいです",
                ],
                "answer": 1,
                "explanation": "«日本へ 行きたいです。京都を 見たいです» — Yaponiyaga "
                               "bormoqchi. Velosiped kerak boʻlgani Rano, dam olmoqchi "
                               "boʻlgani esa Imron.",
            },
            {
                "text": "«<ruby>休<rt>やす</rt></ruby>みたかったです» nima maʼnoni beradi?",
                "choices": [
                    "Dam olmoqchi edim",
                    "Dam olmoqchiman",
                    "Dam olmoqchi emasman",
                    "Dam oldim",
                ],
                "answer": 0,
                "explanation": "たい — <strong>い-sifat</strong>, shuning uchun oʻtgan "
                               "zamonni oʻzi tashiydi: い → <strong>かった</strong>. "
                               "«休みたいでした» notoʻgʻri boʻlardi.",
            },
            {
                "text": "«お<ruby>金<rt>かね</rt></ruby>がほしいです» — nega が, を emas?",
                "choices": [
                    "Chunki ほしい sifat, feʼl emas",
                    "Chunki お金 uzun soʻz",
                    "Chunki gap savol",
                    "Chunki お金 sanab boʻlmaydigan narsa",
                ],
                "answer": 0,
                "explanation": "を — feʼlning toʻldiruvchisi. ほしい esa "
                               "<strong>い-sifat</strong>, xuddi 好き kabi, shuning "
                               "uchun kerak boʻlgan narsa gapda ega boʻlib turadi va "
                               "<strong>が</strong> oladi.",
            },
        ],
    },
]
