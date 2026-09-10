# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-31 … PJ-33.

PJ-31 〜ています · PJ-32 〜てください / 〜てもいいです · PJ-33 taqiq va majburiyat.
⚠️ Har bir matn faqat OʻZ darsigacha berilgan qoliplarni ishlatadi: PJ-31 da
   てください yoʻq, PJ-32 da てはいけません yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_31_33.py --author=prime
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
        "title":   "いま なにを していますか",
        "summary": (
            "PJ-31 matni. Sinfda hamma nimadir qilyapti. Matnda ています ning "
            "ikkala maʼnosi ham bor: davom etayotgan ish va holat — hamda "
            "«bilmasdim» degan gap."
        ),
        "order":   31,
        "grammar": [
            {
                "pattern":  "〜ています — davom etayotgan ish",
                "meaning":  "Ayni damda bajarilayotgan ish. て-shakli + います.",
                "examples": ["<ruby>宿題<rt>しゅくだい</rt></ruby>をしています。",
                             "<ruby>手紙<rt>てがみ</rt></ruby>を<ruby>書<rt>か</rt></ruby>いています。"],
            },
            {
                "pattern":  "〜ています — holat",
                "meaning":  "Bir marta boʻlgan ishning natijasi hozir turibdi. "
                            "<ruby>住<rt>す</rt></ruby>む va "
                            "<ruby>知<rt>し</rt></ruby>る doim shu shaklda.",
                "examples": ["サマルカンドに<ruby>住<rt>す</rt></ruby>んでいます。",
                             "<ruby>知<rt>し</rt></ruby>っています。"],
            },
            {
                "pattern":  "<ruby>知<rt>し</rt></ruby>りません",
                "meaning":  "«Bilmayman». Bu feʼlning inkori ています dan "
                            "emas, oddiy shakldan yasaladi — yagona istisno.",
                "examples": ["<ruby>知<rt>し</rt></ruby>りませんでした。"],
            },
        ],
        "body": '''<p>ラノさんは<ruby>今<rt>いま</rt></ruby><ruby>教室<rt>きょうしつ</rt></ruby>で<span class="cn-word" data-tr="uy vazifasi"><ruby>宿題<rt>しゅくだい</rt></ruby></span>をしています。イノムさんは<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>んでいます。</p>

<p><strong>パリ:</strong> ラノさん、<ruby>今<rt>いま</rt></ruby><ruby>何<rt>なに</rt></ruby>をしていますか。</p>

<p><strong>ラノ:</strong> <ruby>日本語<rt>にほんご</rt></ruby>の<ruby>宿題<rt>しゅくだい</rt></ruby>をしています。パリさんは<ruby>何<rt>なに</rt></ruby>をしていますか。</p>

<p><strong>パリ:</strong> <ruby>私<rt>わたし</rt></ruby>は<span class="cn-word" data-tr="xat"><ruby>手紙<rt>てがみ</rt></ruby></span>を<ruby>書<rt>か</rt></ruby>いています。ムニラさんに<ruby>書<rt>か</rt></ruby>いています。</p>

<p><strong>ラノ:</strong> ムニラさんは<ruby>今<rt>いま</rt></ruby>どこに<span class="cn-word" data-tr="yashaydi"><ruby>住<rt>す</rt></ruby>んでいます</span>か。</p>

<p><strong>パリ:</strong> サマルカンドに<ruby>住<rt>す</rt></ruby>んでいます。<span class="cn-word" data-tr="universitet"><ruby>大学<rt>だいがく</rt></ruby></span>で<ruby>日本語<rt>にほんご</rt></ruby>を<span class="cn-word" data-tr="oʻqitadi"><ruby>教<rt>おし</rt></ruby>えています</span>。</p>

<p><strong>ラノ:</strong> <ruby>私<rt>わたし</rt></ruby>は<span class="cn-word" data-tr="bilmasdim"><ruby>知<rt>し</rt></ruby>りませんでした</span>。イムロンさんは<ruby>知<rt>し</rt></ruby>っていますか。</p>

<p><strong>パリ:</strong> はい、<ruby>知<rt>し</rt></ruby>っています。ムニラさんの<ruby>妹<rt>いもうと</rt></ruby>です。</p>

<p>イノムさんは<ruby>話<rt>はな</rt></ruby>していません。<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>んでいます。</p>''',
        "questions": [
            {
                "text": "パリさんは<ruby>今<rt>いま</rt></ruby><ruby>何<rt>なに</rt></ruby>をしていますか。",
                "choices": [
                    "<ruby>宿題<rt>しゅくだい</rt></ruby>をしています",
                    "<ruby>手紙<rt>てがみ</rt></ruby>を<ruby>書<rt>か</rt></ruby>いています",
                    "<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>んでいます",
                    "<ruby>日本語<rt>にほんご</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えています",
                ],
                "answer": 1,
                "explanation": "«私は 手紙を 書いています» — xat yozyapti. Uy vazifasi "
                               "qilayotgani Rano, kitob oʻqiyotgani Inom.",
            },
            {
                "text": "「サマルカンドに<ruby>住<rt>す</rt></ruby>んでいます」— nega ています ishlatilgan?",
                "choices": [
                    "Chunki bu davom etayotgan ish — hozir koʻchib boryapti",
                    "Chunki bu holat — bir marta koʻchib kelgan, natijasi davom etyapti",
                    "Chunki gap oʻtgan zamonda",
                    "Chunki 住む — II guruh feʼli",
                ],
                "answer": 1,
                "explanation": "<strong>住む</strong> bir zumda tugaydigan ish "
                               "(koʻchib kelish), shuning uchun ています uning "
                               "<strong>natijasini</strong> bildiradi: hozir oʻsha "
                               "yerda yashaydi. Oʻzbekchada bu oddiy hozirgi zamon.",
            },
            {
                "text": "ラノさんは<ruby>何<rt>なに</rt></ruby>と<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "<ruby>知<rt>し</rt></ruby>っていませんでした",
                    "<ruby>知<rt>し</rt></ruby>りませんでした",
                    "<ruby>知<rt>し</rt></ruby>らないでした",
                    "<ruby>知<rt>し</rt></ruby>っていました",
                ],
                "answer": 1,
                "explanation": "«知りませんでした» — «bilmasdim». <strong>知る</strong> "
                               "yagona istisno: uning inkori ています dan emas, "
                               "oddiy shakldan yasaladi. «知っていません» deyilmaydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "きょうしつの にほんご",
        "summary": (
            "PJ-32 matni. Yamada oʻqituvchining darsi — boshidan oxirigacha "
            "てください va てもいいですか ustida. Oxirida muloyim rad javobi: "
            "«すみません、ちょっと…»."
        ),
        "order":   32,
        "grammar": [
            {
                "pattern":  "〜てください",
                "meaning":  "«Iltimos, qiling». Muloyim, lekin koʻrsatma — "
                            "oʻqituvchi oʻquvchiga shunday gapiradi.",
                "examples": ["<ruby>座<rt>すわ</rt></ruby>ってください。",
                             "<ruby>読<rt>よ</rt></ruby>んでください。"],
            },
            {
                "pattern":  "〜てもいいですか",
                "meaning":  "«Qilsam boʻladimi?» — oʻzingizga ruxsat soʻraysiz. "
                            "Yoʻnalish てください ning teskarisi.",
                "examples": ["<ruby>窓<rt>まど</rt></ruby>を<ruby>開<rt>あ</rt></ruby>けてもいいですか。"],
            },
            {
                "pattern":  "どうぞ · すみません、ちょっと…",
                "meaning":  "Ruxsat berish va muloyim rad qilish. Rad javobi "
                            "ataylab TUGATILMAYDI — yaponcha «yoʻq» koʻpincha "
                            "aytilmaydi.",
                "examples": ["はい、いいですよ。どうぞ。", "すみません、ちょっと…"],
            },
        ],
        "body": '''<p><ruby>九時<rt>くじ</rt></ruby>です。やまだ<ruby>先生<rt>せんせい</rt></ruby>が<ruby>教室<rt>きょうしつ</rt></ruby>に<ruby>来<rt>き</rt></ruby>ました。</p>

<p><strong>やまだ:</strong> <span class="cn-word" data-tr="hammangiz">みなさん</span>、<ruby>座<rt>すわ</rt></ruby>ってください。<span class="cn-word" data-tr="darslik"><ruby>教科書<rt>きょうかしょ</rt></ruby></span>を<ruby>開<rt>あ</rt></ruby>けてください。</p>

<p><strong>やまだ:</strong> <ruby>十<rt>じゅう</rt></ruby><span class="cn-word" data-tr="sahifa">ページ</span>を<ruby>見<rt>み</rt></ruby>てください。ラノさん、<ruby>読<rt>よ</rt></ruby>んでください。</p>

<p><strong>ラノ:</strong> <ruby>先生<rt>せんせい</rt></ruby>、すみません。<span class="cn-word" data-tr="yana bir marta">もう<ruby>一度<rt>いちど</rt></ruby></span><ruby>言<rt>い</rt></ruby>ってください。</p>

<p><strong>やまだ:</strong> <ruby>十<rt>じゅう</rt></ruby>ページです。ゆっくり<ruby>読<rt>よ</rt></ruby>んでください。</p>

<p><strong>イムロン:</strong> <ruby>先生<rt>せんせい</rt></ruby>、<span class="cn-word" data-tr="deraza"><ruby>窓<rt>まど</rt></ruby></span>を<ruby>開<rt>あ</rt></ruby>けてもいいですか。<span class="cn-word" data-tr="issiq"><ruby>暑<rt>あつ</rt></ruby>い</span>です。</p>

<p><strong>やまだ:</strong> はい、いいですよ。どうぞ。</p>

<p><strong>パリ:</strong> <ruby>先生<rt>せんせい</rt></ruby>、<span class="cn-word" data-tr="rasm"><ruby>写真<rt>しゃしん</rt></ruby></span>を<ruby>撮<rt>と</rt></ruby>ってもいいですか。</p>

<p><strong>やまだ:</strong> すみません、ちょっと…</p>''',
        "questions": [
            {
                "text": "ラノさんは<ruby>先生<rt>せんせい</rt></ruby>に<ruby>何<rt>なに</rt></ruby>と<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "<ruby>窓<rt>まど</rt></ruby>を<ruby>開<rt>あ</rt></ruby>けてもいいですか",
                    "もう<ruby>一度<rt>いちど</rt></ruby><ruby>言<rt>い</rt></ruby>ってください",
                    "<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>ってもいいですか",
                    "<ruby>教科書<rt>きょうかしょ</rt></ruby>を<ruby>開<rt>あ</rt></ruby>けてください",
                ],
                "answer": 1,
                "explanation": "«もう一度 言ってください» — «yana bir marta ayting». "
                               "Bu yapon tilini oʻrganayotgan odam eng koʻp "
                               "ishlatadigan gap.",
            },
            {
                "text": "パリさんは<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>りましたか。",
                "choices": [
                    "はい、<ruby>先生<rt>せんせい</rt></ruby>が「どうぞ」と<ruby>言<rt>い</rt></ruby>いました",
                    "いいえ、<ruby>先生<rt>せんせい</rt></ruby>は<ruby>教室<rt>きょうしつ</rt></ruby>にいませんでした",
                    "いいえ、<ruby>先生<rt>せんせい</rt></ruby>は「ちょっと…」と<ruby>言<rt>い</rt></ruby>いました",
                    "はい、<ruby>窓<rt>まど</rt></ruby>の<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>りました",
                ],
                "answer": 2,
                "explanation": "«すみません、ちょっと…» — bu <strong>rad javobi</strong>. "
                               "Gap ataylab tugatilmaydi: yaponchada «yoʻq» koʻpincha "
                               "aytilmaydi, lekin suhbatdosh hammasini tushunadi.",
            },
            {
                "text": "«<ruby>座<rt>すわ</rt></ruby>ってください» va «<ruby>窓<rt>まど</rt></ruby>を<ruby>開<rt>あ</rt></ruby>けてもいいですか» — farqi nima?",
                "choices": [
                    "Birinchisi — sen qil, ikkinchisi — men qilsam boʻladimi",
                    "Birinchisi muloyimroq",
                    "Birinchisi oʻtgan zamonda",
                    "Farqi yoʻq, ikkalasi ham iltimos",
                ],
                "answer": 0,
                "explanation": "Yoʻnalish qarama-qarshi. <strong>てください</strong> — "
                               "men senga aytyapman; <strong>てもいいですか</strong> — "
                               "men sendan oʻzimga ruxsat soʻrayapman.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "プールの きそく",
        "summary": (
            "PJ-33 matni. Inom va Imron basseynga borishadi va kirish "
            "eshigidagi qoidalarni oʻqishadi — taqiq, majburiyat va ruxsat "
            "bitta matnda."
        ),
        "order":   33,
        "grammar": [
            {
                "pattern":  "〜てはいけません",
                "meaning":  "«Qilish mumkin emas» — qatʼiy taqiq. て-shaklidan "
                            "yasaladi; は bu yerda [wa] deb oʻqiladi.",
                "examples": ["プールで<ruby>走<rt>はし</rt></ruby>ってはいけません。",
                             "<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>ってはいけません。"],
            },
            {
                "pattern":  "〜なければなりません",
                "meaning":  "«Qilish shart». ない-shaklidan yasaladi. Soʻzma-soʻz "
                            "«…masa boʻlmaydi» — ikki inkor, xuddi oʻzbekchadagi kabi.",
                "examples": ["シャワーを<ruby>使<rt>つか</rt></ruby>わなければなりません。"],
            },
            {
                "pattern":  "〜てもいいです",
                "meaning":  "«Qilsa boʻladi» — ruxsat. Uchta qolip bir matnda "
                            "yonma-yon turadi.",
                "examples": ["<ruby>飲<rt>の</rt></ruby>み<ruby>物<rt>もの</rt></ruby>は<ruby>持<rt>も</rt></ruby>ってもいいです。"],
            },
        ],
        "body": '''<p><ruby>土曜日<rt>どようび</rt></ruby>にイノムさんとイムロンさんは<span class="cn-word" data-tr="basseyn">プール</span>へ<ruby>行<rt>い</rt></ruby>きました。<span class="cn-word" data-tr="kirish eshigi"><ruby>入口<rt>いりぐち</rt></ruby></span>に<span class="cn-word" data-tr="qoidalar"><ruby>規則<rt>きそく</rt></ruby></span>があります。</p>

<p>「プールで<ruby>走<rt>はし</rt></ruby>ってはいけません。プールで<ruby>食<rt>た</rt></ruby>べてはいけません。<span class="cn-word" data-tr="dush">シャワー</span>を<ruby>使<rt>つか</rt></ruby>わなければなりません。」</p>

<p><strong>イノム:</strong> シャワーを<ruby>使<rt>つか</rt></ruby>わなければなりませんか。</p>

<p><strong>イムロン:</strong> はい、<ruby>規則<rt>きそく</rt></ruby>です。<span class="cn-word" data-tr="shapka"><ruby>帽子<rt>ぼうし</rt></ruby></span>も<ruby>使<rt>つか</rt></ruby>わなければなりません。</p>

<p><strong>イノム:</strong> <ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>ってもいいですか。</p>

<p><strong>イムロン:</strong> いいえ、<ruby>撮<rt>と</rt></ruby>ってはいけません。でも<span class="cn-word" data-tr="ichimlik"><ruby>飲<rt>の</rt></ruby>み<ruby>物<rt>もの</rt></ruby></span>は<ruby>持<rt>も</rt></ruby>ってもいいです。</p>

<p><ruby>二人<rt>ふたり</rt></ruby>はシャワーを<ruby>使<rt>つか</rt></ruby>って、プールに<ruby>入<rt>はい</rt></ruby>って、<ruby>泳<rt>およ</rt></ruby>ぎました。プールは<ruby>大<rt>おお</rt></ruby>きかったです。<ruby>人<rt>ひと</rt></ruby>は<ruby>多<rt>おお</rt></ruby>くなかったです。</p>

<p><ruby>四時<rt>よじ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>りました。とても<span class="cn-word" data-tr="qiziqarli"><ruby>楽<rt>たの</rt></ruby>しかった</span>です。</p>''',
        "questions": [
            {
                "text": "プールで<ruby>何<rt>なに</rt></ruby>をしてはいけませんか。",
                "choices": [
                    "<ruby>泳<rt>およ</rt></ruby>いではいけません",
                    "シャワーを<ruby>使<rt>つか</rt></ruby>ってはいけません",
                    "<ruby>走<rt>はし</rt></ruby>ってはいけません",
                    "<ruby>飲<rt>の</rt></ruby>み<ruby>物<rt>もの</rt></ruby>を<ruby>持<rt>も</rt></ruby>ってはいけません",
                ],
                "answer": 2,
                "explanation": "«プールで 走ってはいけません» — yugurish taqiqlangan "
                               "(va ovqatlanish ham). Dush esa aksincha "
                               "<strong>shart</strong>, ichimlikka esa ruxsat bor.",
                },
            {
                "text": "シャワーと<ruby>帽子<rt>ぼうし</rt></ruby>について<ruby>規則<rt>きそく</rt></ruby>は<ruby>何<rt>なん</rt></ruby>ですか。",
                "choices": [
                    "<ruby>使<rt>つか</rt></ruby>ってもいいです",
                    "<ruby>使<rt>つか</rt></ruby>わなければなりません",
                    "<ruby>使<rt>つか</rt></ruby>ってはいけません",
                    "<ruby>使<rt>つか</rt></ruby>わなくてもいいです",
                ],
                "answer": 1,
                "explanation": "«シャワーを 使わなければなりません。帽子も 使わなければ "
                               "なりません» — ikkalasi ham <strong>shart</strong>. "
                               "Bu qolip ない-shaklidan yasaladi: 使う → 使わない → "
                               "使わなければなりません.",
            },
            {
                "text": "«<ruby>使<rt>つか</rt></ruby>わなければなりません» qanday yasalgan?",
                "choices": [
                    "て-shaklidan: 使って + はいけません",
                    "ない-shaklidan: 使わない → 使わなければなりません",
                    "ます shaklidan: 使います + なければ",
                    "Lugʻat shaklidan: 使う + なければ",
                ],
                "answer": 1,
                "explanation": "ない-shakli olinadi, oxirgi <strong>い</strong> "
                               "tashlanadi va <strong>ければなりません</strong> "
                               "qoʻyiladi. Diqqat: 使う — う bilan tugaydi, shuning "
                               "uchun ない-shakli 使<strong>わ</strong>ない.",
            },
        ],
    },
]
