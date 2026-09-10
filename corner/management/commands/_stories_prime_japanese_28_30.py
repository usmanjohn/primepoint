# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-28 … PJ-30.

PJ-28 lugʻat shakli · PJ-29 て-shakli (II/III) · PJ-30 て-shakli (I guruh).
⚠️ PJ-29 matni faqat II va III guruhning て-shakllarini ishlatadi — I guruhning
   て-shakli PJ-30 da beriladi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_28_30.py --author=prime
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
        "title":   "じしょに ありません",
        "summary": (
            "PJ-28 matni. Rano lugʻatdan «のみます» ni qidiradi va topa "
            "olmaydi. Yamada oʻqituvchi unga lugʻat shaklini koʻrsatadi."
        ),
        "order":   28,
        "grammar": [
            {
                "pattern":  "<ruby>辞書形<rt>じしょけい</rt></ruby> — lugʻat shakli",
                "meaning":  "Feʼlning ます siz shakli. Lugʻat faqat shuni "
                            "beradi, chunki ます — muloyimlik qoʻshimchasi, "
                            "feʼlning qismi emas.",
                "examples": ["<ruby>飲<rt>の</rt></ruby>みます → <ruby>飲<rt>の</rt></ruby>む",
                             "<ruby>食<rt>た</rt></ruby>べます → <ruby>食<rt>た</rt></ruby>べる"],
            },
            {
                "pattern":  "I guruh: い qatori → う qatori",
                "meaning":  "み → む, き → く, し → す, ち → つ, り → る.",
                "examples": ["<ruby>読<rt>よ</rt></ruby>みます → <ruby>読<rt>よ</rt></ruby>む",
                             "<ruby>聞<rt>き</rt></ruby>きます → <ruby>聞<rt>き</rt></ruby>く"],
            },
            {
                "pattern":  "II guruh: ます → る",
                "meaning":  "Oʻzak oʻzgarmaydi, ます oʻrniga る qoʻyiladi.",
                "examples": ["<ruby>起<rt>お</rt></ruby>きます → <ruby>起<rt>お</rt></ruby>きる"],
            },
        ],
        "body": '''<p>ラノさんは<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みます。<ruby>本<rt>ほん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に「<ruby>飲<rt>の</rt></ruby>みます」があります。ラノさんは<span class="cn-word" data-tr="lugʻat"><ruby>辞書<rt>じしょ</rt></ruby></span>を<ruby>見<rt>み</rt></ruby>ます。でも<ruby>辞書<rt>じしょ</rt></ruby>に「のみます」はありません。</p>

<p><strong>ラノ:</strong> やまだ<ruby>先生<rt>せんせい</rt></ruby>、<ruby>辞書<rt>じしょ</rt></ruby>に「のみます」がありません。</p>

<p><strong>やまだ:</strong> <ruby>辞書<rt>じしょ</rt></ruby>は「<ruby>飲<rt>の</rt></ruby>む」です。「ます」は<span class="cn-word" data-tr="qoʻshimcha"><ruby>助動詞<rt>じょどうし</rt></ruby></span>です。<ruby>動詞<rt>どうし</rt></ruby>の<span class="cn-word" data-tr="qismi"><ruby>部分<rt>ぶぶん</rt></ruby></span>ではありません。</p>

<p><strong>ラノ:</strong> そうですか。「<ruby>読<rt>よ</rt></ruby>みます」は「<ruby>読<rt>よ</rt></ruby>む」ですか。</p>

<p><strong>やまだ:</strong> はい。「み」は「む」です。「<ruby>聞<rt>き</rt></ruby>きます」も<ruby>同<rt>おな</rt></ruby>じです。「<ruby>聞<rt>き</rt></ruby>く」です。</p>

<p><strong>ラノ:</strong> 「<ruby>起<rt>お</rt></ruby>きます」は「<ruby>起<rt>お</rt></ruby>く」ですか。</p>

<p><strong>やまだ:</strong> いいえ。「<ruby>起<rt>お</rt></ruby>きる」です。「<ruby>聞<rt>き</rt></ruby>きます」と「<ruby>起<rt>お</rt></ruby>きます」は<span class="cn-word" data-tr="boshqacha"><ruby>違<rt>ちが</rt></ruby>います</span>。<span class="cn-word" data-tr="guruh"><ruby>動詞<rt>どうし</rt></ruby>のグループ</span>が<ruby>違<rt>ちが</rt></ruby>います。</p>

<p>ラノさんは<ruby>新<rt>あたら</rt></ruby>しい<ruby>動詞<rt>どうし</rt></ruby>を<span class="cn-word" data-tr="daftar"><ruby>辞書<rt>じしょ</rt></ruby>のノート</span>に<ruby>書<rt>か</rt></ruby>きます。<ruby>辞書形<rt>じしょけい</rt></ruby>も<ruby>書<rt>か</rt></ruby>きます。</p>''',
        "questions": [
            {
                "text": "なぜ<ruby>辞書<rt>じしょ</rt></ruby>に「のみます」がありませんか。",
                "choices": [
                    "<ruby>辞書<rt>じしょ</rt></ruby>が<ruby>古<rt>ふる</rt></ruby>いですから",
                    "「ます」は<ruby>助動詞<rt>じょどうし</rt></ruby>ですから",
                    "「のむ」は<ruby>動詞<rt>どうし</rt></ruby>ではありませんから",
                    "ラノさんの<ruby>辞書<rt>じしょ</rt></ruby>は<ruby>小<rt>ちい</rt></ruby>さいですから",
                ],
                "answer": 1,
                "explanation": "«「ます」は 助動詞です。動詞の 部分では ありません» — "
                               "ます feʼlning qismi emas, muloyimlik qoʻshimchasi. "
                               "Lugʻat feʼlning oʻzini beradi: <strong>飲む</strong>.",
            },
            {
                "text": "「<ruby>聞<rt>き</rt></ruby>きます」の<ruby>辞書形<rt>じしょけい</rt></ruby>は<ruby>何<rt>なん</rt></ruby>ですか。",
                "choices": [
                    "<ruby>聞<rt>き</rt></ruby>きる",
                    "<ruby>聞<rt>き</rt></ruby>く",
                    "<ruby>聞<rt>き</rt></ruby>る",
                    "<ruby>聞<rt>き</rt></ruby>む",
                ],
                "answer": 1,
                "explanation": "«「聞きます」も 同じです。「聞く」です» — bu I guruh feʼli, "
                               "shuning uchun き koʻtarilib <strong>く</strong> boʻladi. "
                               "«聞きる» — II guruhning shakli, bu feʼlga toʻgʻri kelmaydi.",
            },
            {
                "text": "なぜ「<ruby>起<rt>お</rt></ruby>きます」と「<ruby>聞<rt>き</rt></ruby>きます」の<ruby>辞書形<rt>じしょけい</rt></ruby>が<ruby>違<rt>ちが</rt></ruby>いますか。",
                "choices": [
                    "Ular boshqa-boshqa guruhlarga tegishli",
                    "Ularning kanjilari boshqacha",
                    "Biri yangi soʻz, ikkinchisi eski",
                    "Oʻzaklarining uzunligi har xil",
                ],
                "answer": 0,
                "explanation": "Ikkala oʻzak ham «き» bilan tugaydi, lekin 起きる — "
                               "II guruh, 聞く — I guruh. Shuning uchun ます shakliga "
                               "qarab guruhni aniqlab boʻlmaydi: feʼlni "
                               "<strong>lugʻat shaklida</strong> yodlash kerak.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "おきて、たべて、がっこうへ",
        "summary": (
            "PJ-29 matni. Muniraning ertalabki tartibi — butun matn て bilan "
            "ulangan gaplar ustida turadi. Faqat II va III guruh feʼllari."
        ),
        "order":   29,
        "grammar": [
            {
                "pattern":  "II guruh: る → て",
                "meaning":  "Lugʻat shaklidagi る olib tashlanadi, て qoʻyiladi.",
                "examples": ["<ruby>起<rt>お</rt></ruby>きる → <ruby>起<rt>お</rt></ruby>きて",
                             "<ruby>食<rt>た</rt></ruby>べる → <ruby>食<rt>た</rt></ruby>べて"],
            },
            {
                "pattern":  "III guruh: して · <ruby>来<rt>き</rt></ruby>て",
                "meaning":  "Yodlanadi. する ning qoʻshma feʼllari ham して "
                            "boʻladi.",
                "examples": ["<ruby>勉強<rt>べんきょう</rt></ruby>する → <ruby>勉強<rt>べんきょう</rt></ruby>して"],
            },
            {
                "pattern":  "〜て、〜ます",
                "meaning":  "Ikki ishni ulaydi — oʻzbekchadagi «-ib» kabi. "
                            "Zamonni faqat OXIRGI feʼl tashiydi.",
                "examples": ["<ruby>起<rt>お</rt></ruby>きて、<ruby>食<rt>た</rt></ruby>べます。",
                             "<ruby>見<rt>み</rt></ruby>て、<ruby>寝<rt>ね</rt></ruby>ました。"],
            },
        ],
        "body": '''<p>ムニラさんの<ruby>朝<rt>あさ</rt></ruby>は<span class="cn-word" data-tr="band"><ruby>忙<rt>いそが</rt></ruby>しい</span>です。<ruby>六時<rt>ろくじ</rt></ruby>に<ruby>起<rt>お</rt></ruby>きて、<span class="cn-word" data-tr="nonushta"><ruby>朝<rt>あさ</rt></ruby>ごはん</span>を<ruby>食<rt>た</rt></ruby>べて、<ruby>七時<rt>しちじ</rt></ruby>にバスに<span class="cn-word" data-tr="minadi"><ruby>乗<rt>の</rt></ruby>ります</span>。</p>

<p><strong>ラノ:</strong> ムニラさん、<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>何<rt>なに</rt></ruby>をしますか。</p>

<p><strong>ムニラ:</strong> <ruby>起<rt>お</rt></ruby>きて、<ruby>朝<rt>あさ</rt></ruby>ごはんを<ruby>食<rt>た</rt></ruby>べて、<ruby>学校<rt>がっこう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きます。</p>

<p><strong>ラノ:</strong> <ruby>私<rt>わたし</rt></ruby>も<ruby>同<rt>おな</rt></ruby>じです。でも<ruby>朝<rt>あさ</rt></ruby>ごはんを<ruby>食<rt>た</rt></ruby>べて、<span class="cn-word" data-tr="televizor">テレビ</span>を<ruby>見<rt>み</rt></ruby>て、<ruby>学校<rt>がっこう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きます。</p>

<p><strong>ムニラ:</strong> テレビを<ruby>見<rt>み</rt></ruby>ますか。<ruby>時間<rt>じかん</rt></ruby>がありますか。</p>

<p><strong>ラノ:</strong> <ruby>五時<rt>ごじ</rt></ruby><ruby>半<rt>はん</rt></ruby>に<ruby>起<rt>お</rt></ruby>きます。<ruby>時間<rt>じかん</rt></ruby>があります。</p>

<p><ruby>学校<rt>がっこう</rt></ruby>で<ruby>二人<rt>ふたり</rt></ruby>は<ruby>勉強<rt>べんきょう</rt></ruby>して、<span class="cn-word" data-tr="tushlik"><ruby>昼<rt>ひる</rt></ruby>ごはん</span>を<ruby>食<rt>た</rt></ruby>べます。やまだ<ruby>先生<rt>せんせい</rt></ruby>が<ruby>教室<rt>きょうしつ</rt></ruby>に<ruby>来<rt>き</rt></ruby>て、<ruby>日本語<rt>にほんご</rt></ruby>を<span class="cn-word" data-tr="oʻrgatadi"><ruby>教<rt>おし</rt></ruby>えます</span>。</p>

<p><ruby>昨日<rt>きのう</rt></ruby>ムニラさんは<span class="cn-word" data-tr="kino"><ruby>映画<rt>えいが</rt></ruby></span>を<ruby>見<rt>み</rt></ruby>て、<ruby>十時<rt>じゅうじ</rt></ruby>に<ruby>寝<rt>ね</rt></ruby>ました。</p>''',
        "questions": [
            {
                "text": "ムニラさんは<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>何<rt>なに</rt></ruby>をしますか。",
                "choices": [
                    "<ruby>起<rt>お</rt></ruby>きて、テレビを<ruby>見<rt>み</rt></ruby>て、<ruby>学校<rt>がっこう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きます",
                    "<ruby>起<rt>お</rt></ruby>きて、<ruby>朝<rt>あさ</rt></ruby>ごはんを<ruby>食<rt>た</rt></ruby>べて、<ruby>学校<rt>がっこう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きます",
                    "<ruby>起<rt>お</rt></ruby>きて、<ruby>勉強<rt>べんきょう</rt></ruby>して、<ruby>寝<rt>ね</rt></ruby>ます",
                    "<ruby>映画<rt>えいが</rt></ruby>を<ruby>見<rt>み</rt></ruby>て、<ruby>学校<rt>がっこう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きます",
                ],
                "answer": 1,
                "explanation": "«起きて、朝ごはんを 食べて、学校へ 行きます» — turadi, "
                               "nonushta qiladi, maktabga boradi. Televizor koʻradigani "
                               "— Rano.",
            },
            {
                "text": "なぜラノさんは<ruby>時間<rt>じかん</rt></ruby>がありますか。",
                "choices": [
                    "<ruby>学校<rt>がっこう</rt></ruby>が<ruby>近<rt>ちか</rt></ruby>いですから",
                    "<ruby>朝<rt>あさ</rt></ruby>ごはんを<ruby>食<rt>た</rt></ruby>べませんから",
                    "<ruby>五時<rt>ごじ</rt></ruby><ruby>半<rt>はん</rt></ruby>に<ruby>起<rt>お</rt></ruby>きますから",
                    "テレビが<ruby>好<rt>す</rt></ruby>きですから",
                ],
                "answer": 2,
                "explanation": "«五時半に 起きます。時間が あります» — soat besh yarimda "
                               "turadi, shuning uchun vaqti bor. Munira esa oltida "
                               "turadi.",
            },
            {
                "text": "「<ruby>映画<rt>えいが</rt></ruby>を<ruby>見<rt>み</rt></ruby>て、<ruby>十時<rt>じゅうじ</rt></ruby>に<ruby>寝<rt>ね</rt></ruby>ました」— なぜ「<ruby>見<rt>み</rt></ruby>ました」ではありませんか。",
                "choices": [
                    "て-shakli zamon koʻrsatmaydi; zamonni oxirgi feʼl tashiydi",
                    "Kino kecha emas, bugun koʻrilgan",
                    "見る II guruh feʼli boʻlgani uchun",
                    "Gap juda uzun boʻlgani uchun",
                ],
                "answer": 0,
                "explanation": "て-shakli oʻzgarmaydi — u zamon koʻrsatmaydi. Butun "
                               "gapning zamonini <strong>寝ました</strong> tashiydi, "
                               "shuning uchun ikkala ish ham kecha boʻlgan.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "うみで およいで",
        "summary": (
            "PJ-30 matni. Imronning yozgi kuni — I guruhning beshta て "
            "qoidasi bir matnda: って, んで, いて, いで, して, va 行って."
        ),
        "order":   30,
        "grammar": [
            {
                "pattern":  "う・つ・る → って",
                "meaning":  "Uchta oxir bitta natijaga keladi. Kichik っ — "
                            "sokuon, u keyingi undoshni ikkilantiradi.",
                "examples": ["<ruby>買<rt>か</rt></ruby>う → <ruby>買<rt>か</rt></ruby>って",
                             "<ruby>帰<rt>かえ</rt></ruby>る → <ruby>帰<rt>かえ</rt></ruby>って"],
            },
            {
                "pattern":  "む・ぶ・ぬ → んで",
                "meaning":  "Jarangli tovushlardan keyin ulanish ham jarangli "
                            "boʻladi: て emas, で.",
                "examples": ["<ruby>読<rt>よ</rt></ruby>む → <ruby>読<rt>よ</rt></ruby>んで",
                             "<ruby>遊<rt>あそ</rt></ruby>ぶ → <ruby>遊<rt>あそ</rt></ruby>んで"],
            },
            {
                "pattern":  "く → いて · ぐ → いで · す → して",
                "meaning":  "Jarangsiz く jarangsiz て oladi, jarangli ぐ esa "
                            "jarangli で.",
                "examples": ["<ruby>書<rt>か</rt></ruby>く → <ruby>書<rt>か</rt></ruby>いて",
                             "<ruby>泳<rt>およ</rt></ruby>ぐ → <ruby>泳<rt>およ</rt></ruby>いで"],
            },
            {
                "pattern":  "<ruby>行<rt>い</rt></ruby>く → <ruby>行<rt>い</rt></ruby>って",
                "meaning":  "Yagona istisno. Qoida boʻyicha «いいて» chiqishi "
                            "kerak edi, lekin chiqmaydi.",
                "examples": ["<ruby>海<rt>うみ</rt></ruby>へ<ruby>行<rt>い</rt></ruby>って、<ruby>泳<rt>およ</rt></ruby>ぎました。"],
            },
        ],
        "body": '''<p><ruby>土曜日<rt>どようび</rt></ruby>の<ruby>朝<rt>あさ</rt></ruby>、イムロンさんは<ruby>友<rt>とも</rt></ruby>だちを<ruby>待<rt>ま</rt></ruby>って、バスに<span class="cn-word" data-tr="minadi"><ruby>乗<rt>の</rt></ruby>ります</span>。<ruby>二人<rt>ふたり</rt></ruby>は<span class="cn-word" data-tr="dengiz"><ruby>海<rt>うみ</rt></ruby></span>へ<ruby>行<rt>い</rt></ruby>って、<span class="cn-word" data-tr="suzadi"><ruby>泳<rt>およ</rt></ruby>ぎます</span>。</p>

<p><strong>イノム:</strong> イムロンさん、<ruby>今日<rt>きょう</rt></ruby>は<ruby>何<rt>なに</rt></ruby>をしますか。</p>

<p><strong>イムロン:</strong> <ruby>海<rt>うみ</rt></ruby>で<ruby>泳<rt>およ</rt></ruby>いで、<ruby>遊<rt>あそ</rt></ruby>んで、<ruby>四時<rt>よじ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>ります。</p>

<p><strong>イノム:</strong> <ruby>朝<rt>あさ</rt></ruby>ごはんは<ruby>食<rt>た</rt></ruby>べましたか。</p>

<p><strong>イムロン:</strong> はい。パンを<ruby>買<rt>か</rt></ruby>って、<ruby>牛乳<rt>ぎゅうにゅう</rt></ruby>を<ruby>飲<rt>の</rt></ruby>みました。</p>

<p><ruby>海<rt>うみ</rt></ruby>は<ruby>静<rt>しず</rt></ruby>かでした。<ruby>二人<rt>ふたり</rt></ruby>は<ruby>泳<rt>およ</rt></ruby>いで、<span class="cn-word" data-tr="oʻynab"><ruby>遊<rt>あそ</rt></ruby>んで</span>、<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>んで、<ruby>日本語<rt>にほんご</rt></ruby>で<ruby>話<rt>はな</rt></ruby>しました。</p>

<p><ruby>夕方<rt>ゆうがた</rt></ruby>イムロンさんは<span class="cn-word" data-tr="xat"><ruby>手紙<rt>てがみ</rt></ruby></span>を<ruby>書<rt>か</rt></ruby>いて、<ruby>家<rt>いえ</rt></ruby>へ<ruby>帰<rt>かえ</rt></ruby>って、<ruby>十時<rt>じゅうじ</rt></ruby>に<ruby>寝<rt>ね</rt></ruby>ました。<span class="cn-word" data-tr="uzun"><ruby>長<rt>なが</rt></ruby>い</span><ruby>一日<rt>いちにち</rt></ruby>でした。</p>''',
        "questions": [
            {
                "text": "イムロンさんは<ruby>朝<rt>あさ</rt></ruby><ruby>何<rt>なに</rt></ruby>をしましたか。",
                "choices": [
                    "パンを<ruby>買<rt>か</rt></ruby>って、<ruby>牛乳<rt>ぎゅうにゅう</rt></ruby>を<ruby>飲<rt>の</rt></ruby>みました",
                    "<ruby>手紙<rt>てがみ</rt></ruby>を<ruby>書<rt>か</rt></ruby>いて、<ruby>海<rt>うみ</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きました",
                    "<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>って、<ruby>帰<rt>かえ</rt></ruby>りました",
                    "<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>んで、<ruby>寝<rt>ね</rt></ruby>ました",
                ],
                "answer": 0,
                "explanation": "«パンを 買って、牛乳を 飲んで、家を 出ました» — non sotib "
                               "olib, sut ichib, uydan chiqdi. Xatni esa kechqurun yozdi.",
            },
            {
                "text": "「<ruby>行<rt>い</rt></ruby>く」の て-shakli なぜ「いいて」ではありませんか。",
                "choices": [
                    "行く II guruh feʼli boʻlgani uchun",
                    "行く — butun kursdagi yagona istisno",
                    "行く III guruh feʼli boʻlgani uchun",
                    "«いいて» juda uzun boʻlgani uchun",
                ],
                "answer": 1,
                "explanation": "く → いて qoidasi «いいて» berishi kerak edi, lekin "
                               "行く butun kursdagi <strong>yagona istisno</strong>: "
                               "行って. Boshqa hech qaysi く feʼli bunday qilmaydi — "
                               "書く → 書いて.",
            },
            {
                "text": "なぜ「<ruby>泳<rt>およ</rt></ruby>いで」に「で」があります、「て」ではありませんか。",
                "choices": [
                    "«Dengiz» soʻzi bilan bogʻliq boʻlgani uchun",
                    "泳ぐ II guruh feʼli boʻlgani uchun",
                    "ぐ — jarangli tovush boʻlgani uchun",
                    "Gap oʻrtasida turgani uchun",
                ],
                "answer": 2,
                "explanation": "ぐ — jarangli tovush, shuning uchun ulanish ham jarangli "
                               "boʻladi: <strong>いで</strong>. Jarangsiz く esa "
                               "<strong>いて</strong> oladi: 書いて. Bir juftlik, "
                               "bitta farq.",
            },
        ],
    },
]
