# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-13 … PJ-15.

Har bir matn oʻz darsining grammatikasini kamida ikki marta koʻrsatadi va faqat
oʻsha darsgacha oʻrganilgan qoliplardan foydalanadi (kumulyativ qoida).
Toc: corner/management/commands/toc_prime_japanese_readings.txt

PJ-20 gacha feʼl yoʻq, shuning uchun hikoya ramkasi uchun toc'da ruxsat etilgan
yopiq roʻyxat ishlatiladi (あります · います · 言いました …), doim cn-word izohi bilan.
Har bir kanji <ruby> furigana bilan yoziladi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_13_15.py --author=prime
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
        "title":   "はじめまして",
        "summary": (
            "PJ-13 matni. Afsona yapon tili darsida oʻzini tanishtiradi — va «です» "
            "bilan «ではありません» ni birinchi marta amalda koʻrasiz."
        ),
        "order":   13,
        "grammar": [
            {
                "pattern":  "〜です",
                "meaning":  "«…dir». Yaponchadagi eng oddiy kesim. Shaxsga qarab "
                            "OʻZGARMAYDI — men, sen, u uchun bir xil.",
                "examples": ["わたしは がくせいです。", "やまださんは せんせいです。"],
            },
            {
                "pattern":  "〜ではありません",
                "meaning":  "«…emas» — です ning inkori. では bu yerda [dewa] deb "
                            "oʻqiladi, chunki は grammatik qoʻshimcha.",
                "examples": ["せんせいではありません。", "にほんじんではありません。"],
            },
            {
                "pattern":  "〜ですか",
                "meaning":  "Savol. Gap oxiriga か qoʻshiladi, soʻz tartibi "
                            "oʻzgarmaydi va ohang koʻtarilmaydi.",
                "examples": ["がくせいですか。", "はい、そうです。"],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="yapon tili"><ruby>日本語<rt>にほんご</rt></ruby></span>の<span class="cn-word" data-tr="dars"><ruby>教室<rt>きょうしつ</rt></ruby></span>です。<span class="cn-word" data-tr="Afsona">アフソナ</span>さんと<span class="cn-word" data-tr="Yamada (familiya)">やまだ</span>さんが<span class="cn-word" data-pos="verb" data-tr="bor, turibdi">います</span>。</p>

<p><strong>やまだ:</strong> <span class="cn-word" data-tr="tanishganimdan xursandman">はじめまして</span>。わたしは やまだです。</p>

<p><strong>アフソナ:</strong> はじめまして。わたしは アフソナです。</p>

<p><strong>やまだ:</strong> アフソナさんは <span class="cn-word" data-tr="yapon (millat)"><ruby>日本人<rt>にほんじん</rt></ruby></span>ですか。</p>

<p><strong>アフソナ:</strong> <span class="cn-word" data-tr="yoʻq">いいえ</span>、<ruby>日本人<rt>にほんじん</rt></ruby>ではありません。<span class="cn-word" data-tr="oʻzbek (millat)">ウズベキスタンじん</span>です。</p>

<p><strong>やまだ:</strong> そうですか。<span class="cn-word" data-tr="talaba"><ruby>学生<rt>がくせい</rt></ruby></span>ですか。</p>

<p><strong>アフソナ:</strong> <span class="cn-word" data-tr="ha">はい</span>、<span class="cn-word" data-tr="shunday">そうです</span>。やまださんは？</p>

<p><strong>やまだ:</strong> わたしは <ruby>学生<rt>がくせい</rt></ruby>ではありません。<span class="cn-word" data-tr="oʻqituvchi"><ruby>先生<rt>せんせい</rt></ruby></span>です。</p>

<p>アフソナさんは <span class="cn-word" data-pos="verb" data-tr="dedi"><ruby>言<rt>い</rt></ruby>いました</span>。</p>

<p><strong>アフソナ:</strong> <span class="cn-word" data-tr="kechirasiz">すみません</span>、<ruby>先生<rt>せんせい</rt></ruby>！</p>''',
        "questions": [
            {
                "text": "アフソナさんは にほんじんですか。",
                "choices": [
                    "はい、にほんじんです",
                    "いいえ、ウズベキスタンじんです",
                    "はい、せんせいです",
                    "いいえ、せんせいです",
                ],
                "answer": 1,
                "explanation": "Afsona «いいえ、にほんじんではありません。ウズベキスタンじんです» "
                               "dedi — yapon emas, oʻzbek. Matnda inkor shakli "
                               "ではありません aynan shu yerda ishlatilgan.",
            },
            {
                "text": "やまださんは がくせいですか。",
                "choices": [
                    "はい、がくせいです",
                    "いいえ、せんせいです",
                    "はい、にほんじんです",
                    "いいえ、がくせいです",
                ],
                "answer": 1,
                "explanation": "Yamada «わたしは がくせいではありません。せんせいです» dedi. "
                               "Aynan shuning uchun Afsona oxirida uyalib qoldi — u "
                               "oʻqituvchiga tengdoshiday savol bergan edi.",
            },
            {
                "text": "アフソナさんの かおが あかいです。なぜですか。",
                "choices": [
                    "きょうしつが あついです",
                    "やまださんが せんせいでした",
                    "アフソナさんは がくせいではありません",
                    "やまださんが ウズベキスタンじんです",
                ],
                "answer": 1,
                "explanation": "Afsona Yamadadan «がくせいですか» deb soʻragan edi — lekin "
                               "u aslida oʻqituvchi edi. Shuning uchun Afsona uyalib "
                               "«すみません、せんせい！» dedi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "だれが せんせいですか",
        "summary": (
            "PJ-14 matni. Yangi oʻquvchi sinfda oʻqituvchini qidiradi — va «が» bilan "
            "«は» ning farqi oʻz-oʻzidan koʻrinadi."
        ),
        "order":   14,
        "grammar": [
            {
                "pattern":  "だれが 〜ですか",
                "meaning":  "«Kim …?». Savol soʻzi bilan DOIM が ishlatiladi — "
                            "«だれは» degan birikma yapon tilida mavjud emas.",
                "examples": ["だれが せんせいですか。", "だれが がくせいですか。"],
            },
            {
                "pattern":  "〜が 〜です (javob)",
                "meaning":  "Savolga javobda ham が saqlanadi: «aynan u». は emas.",
                "examples": ["やまださんが せんせいです。", "わたしが がくせいです。"],
            },
            {
                "pattern":  "〜は 〜です、〜は 〜です",
                "meaning":  "Ikkita は — qarama-qarshi qoʻyish, oʻzbekchadagi «esa».",
                "examples": ["やまださんは せんせいです。ジャスルさんは がくせいです。"],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="bugun"><ruby>今日<rt>きょう</rt></ruby></span>は <span class="cn-word" data-tr="birinchi kun">はつか</span>です。<span class="cn-word" data-tr="Jasur">ジャスル</span>さんは <span class="cn-word" data-tr="yangi oʻquvchi"><ruby>新入生<rt>しんにゅうせい</rt></ruby></span>です。<ruby>教室<rt>きょうしつ</rt></ruby>に <span class="cn-word" data-tr="uch kishi"><ruby>三人<rt>さんにん</rt></ruby></span><span class="cn-word" data-pos="verb" data-tr="bor">います</span>。</p>

<p><strong>ジャスル:</strong> <span class="cn-word" data-tr="kechirasiz">あの、すみません</span>。<span class="cn-word" data-tr="kim"><ruby>誰<rt>だれ</rt></ruby></span>が <ruby>先生<rt>せんせい</rt></ruby>ですか。</p>

<p><strong>アフソナ:</strong> <span class="cn-word" data-tr="anavi kishi">あのひと</span>が <ruby>先生<rt>せんせい</rt></ruby>です。やまださんです。</p>

<p><strong>ジャスル:</strong> そうですか。<span class="cn-word" data-tr="bu kishi">このひと</span>は？</p>

<p><strong>アフソナ:</strong> このひとは わたしの<span class="cn-word" data-tr="doʻst"><ruby>友達<rt>ともだち</rt></ruby></span>です。<span class="cn-word" data-tr="Dilnoza">ディルノザ</span>さんです。ディルノザさんは <ruby>学生<rt>がくせい</rt></ruby>です。わたしは ディルノザさんの <ruby>友達<rt>ともだち</rt></ruby>です。</p>

<p><strong>ジャスル:</strong> みなさんは <ruby>学生<rt>がくせい</rt></ruby>ですか。</p>

<p><strong>アフソナ:</strong> はい。でも やまださんは <ruby>学生<rt>がくせい</rt></ruby>ではありません。<ruby>先生<rt>せんせい</rt></ruby>です。</p>

<p>そのとき、やまださんが <span class="cn-word" data-pos="verb" data-tr="keldi"><ruby>来<rt>き</rt></ruby>ました</span>。</p>

<p><strong>やまだ:</strong> <ruby>誰<rt>だれ</rt></ruby>が <ruby>新入生<rt>しんにゅうせい</rt></ruby>ですか。</p>

<p><strong>ジャスル:</strong> わたしが <ruby>新入生<rt>しんにゅうせい</rt></ruby>です。ジャスルです。</p>''',
        "questions": [
            {
                "text": "だれが せんせいですか。",
                "choices": [
                    "アフソナさんです",
                    "ディルノザさんです",
                    "やまださんです",
                    "ジャスルさんです",
                ],
                "answer": 2,
                "explanation": "Afsona «あのひとが せんせいです。やまださんです» dedi. "
                               "Diqqat qiling: savolda ham, javobda ham は emas, "
                               "が ishlatilgan — bu PJ-14 ning asosiy qoidasi.",
            },
            {
                "text": "ジャスルさんは なぜ「わたしが あたらしい がくせいです」と いいましたか。",
                "choices": [
                    "「だれが」の しつもんに こたえましたから",
                    "ジャスルさんは せんせいですから",
                    "ジャスルさんは にほんじんですから",
                    "アフソナさんが しつもんしましたから",
                ],
                "answer": 0,
                "explanation": "Yamada «だれが あたらしい がくせいですか» deb soʻradi. "
                               "Savol soʻziga javob berilganda が saqlanadi va «aynan "
                               "men» degan maʼno beradi. Agar «わたしは» desa, javob "
                               "savolga toʻgʻri kelmasdi.",
            },
            {
                "text": "ディルノザさんは がくせいですか。",
                "choices": [
                    "いいえ、せんせいです",
                    "はい、がくせいです",
                    "いいえ、あたらしい がくせいです",
                    "はい、せんせいです",
                ],
                "answer": 1,
                "explanation": "Afsona «ディルノザさんは がくせいです» dedi. Bu yerda は "
                               "ishlatilgan, chunki bu oddiy xabar — savolga javob emas.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "これは なんですか",
        "summary": (
            "PJ-15 matni. Afsona doʻkonda uch narsani koʻrsatadi — これ, それ va あれ "
            "ning masofasi bir sahnada koʻrinadi."
        ),
        "order":   15,
        "grammar": [
            {
                "pattern":  "これ・それ・あれ",
                "meaning":  "Uch masofa: これ menga yaqin, それ SENGA yaqin, あれ "
                            "ikkalamizdan ham uzoq. Ular yolgʻiz turadi.",
                "examples": ["これは ペンです。", "それは かばんです。", "あれは とけいです。"],
            },
            {
                "pattern":  "この・その・あの ＋ ot",
                "meaning":  "Xuddi shu uch masofa, lekin ortidan ALBATTA ot keladi. "
                            "Yolgʻiz turolmaydi.",
                "examples": ["この ほんは わたしのです。", "あの かばんは いくらですか。"],
            },
            {
                "pattern":  "これは なんですか",
                "meaning":  "«Bu nima?» — なん = nima. Doʻkonda eng koʻp kerak "
                            "boʻladigan gap.",
                "examples": ["これは なんですか。", "それは かさです。"],
            },
        ],
        "body": '''<p>アフソナさんは <span class="cn-word" data-tr="doʻkon"><ruby>店<rt>みせ</rt></ruby></span>に <span class="cn-word" data-pos="verb" data-tr="bordi"><ruby>行<rt>い</rt></ruby>きました</span>。<span class="cn-word" data-tr="sotuvchi">てんいん</span>さんが <span class="cn-word" data-pos="verb" data-tr="bor">います</span>。</p>

<p><strong>アフソナ:</strong> <span class="cn-word" data-tr="kechirasiz">すみません</span>。これは <span class="cn-word" data-tr="nima"><ruby>何<rt>なん</rt></ruby></span>ですか。</p>

<p><strong>てんいん:</strong> それは <span class="cn-word" data-tr="soyabon"><ruby>傘<rt>かさ</rt></ruby></span>です。</p>

<p><strong>アフソナ:</strong> そうですか。<span class="cn-word" data-tr="anavi">あれ</span>は <ruby>何<rt>なん</rt></ruby>ですか。</p>

<p><strong>てんいん:</strong> あれは <span class="cn-word" data-tr="soat"><ruby>時計<rt>とけい</rt></ruby></span>です。<span class="cn-word" data-tr="yaponcha">にほん</span>の <ruby>時計<rt>とけい</rt></ruby>です。</p>

<p><strong>アフソナ:</strong> あの <ruby>時計<rt>とけい</rt></ruby>は <span class="cn-word" data-tr="qancha">いくら</span>ですか。</p>

<p><strong>てんいん:</strong> <span class="cn-word" data-tr="olti ming iyena"><ruby>六千円<rt>ろくせんえん</rt></ruby></span>です。</p>

<p>アフソナさんの<span class="cn-word" data-tr="qoʻl">て</span>に <span class="cn-word" data-tr="sumka">かばん</span>が あります。てんいんさんが <span class="cn-word" data-pos="verb" data-tr="koʻrdi"><ruby>見<rt>み</rt></ruby>ました</span>。</p>

<p><strong>てんいん:</strong> その かばんは <span class="cn-word" data-tr="siznikimi">あなたの</span>ですか。</p>

<p><strong>アフソナ:</strong> はい、この かばんは わたしのです。<span class="cn-word" data-tr="lekin">でも</span> あの <ruby>時計<rt>とけい</rt></ruby>は わたしの <span class="cn-word" data-tr="orzu">ゆめ</span>です！</p>''',
        "questions": [
            {
                "text": "てんいんさんは なぜ「それは かさです」と いいましたか。",
                "choices": [
                    "かさが アフソナさんの ちかくに ありますから",
                    "かさが てんいんさんの ちかくに ありますから",
                    "かさが とおくに ありますから",
                    "かさが みせに ありませんから",
                ],
                "answer": 0,
                "explanation": "それ — «SENGA yaqin narsa». Soyabon Afsonaning yonida "
                               "edi, shuning uchun sotuvchi それ dedi. Afsona esa "
                               "oʻziga yaqin boʻlgani uchun これ degan edi. Bir narsa, "
                               "ikki xil soʻz — masofa kimga nisbatan oʻlchanishiga qarab.",
            },
            {
                "text": "とけいは いくらですか。",
                "choices": [
                    "ろくせんえんです",
                    "ろっぴゃくえんです",
                    "さんぜんえんです",
                    "いちまんえんです",
                ],
                "answer": 0,
                "explanation": "«ろくせんえん» — 6000 iyena. PJ-12 dagi sonlar shu yerda "
                               "ish beryapti: 六千 = ろくせん.",
            },
            {
                "text": "なぜ「あの とけい」と いいますか、「あれ とけい」と いいませんか。",
                "choices": [
                    "「あれ」は ふるい ことばですから",
                    "「あれ」の あとに めいしが きませんから",
                    "「あの」は とおい ものですから",
                    "「あれ」は しつもんの ことばですから",
                ],
                "answer": 1,
                "explanation": "あれ yolgʻiz turadi — ortidan ot kela olmaydi. Ot bilan "
                               "ishlatish uchun あの kerak: «あの とけい» = «anavi soat». "
                               "Oxirgi boʻgʻinga qarang — れ toʻliq, の bogʻlovchi.",
            },
        ],
    },
]
