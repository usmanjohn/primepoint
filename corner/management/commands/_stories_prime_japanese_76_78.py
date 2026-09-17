# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-76 … PJ-78. Blok E yopiladi.

Hikoyachi <ruby>普通体</ruby> da (PJ-45 dan beri). Uzunlik endi
PJ-76…100 tasmasida: oldingi batchdan sezilarli uzunroq.

Shakl navbati: 76 — telefon/xabar almashinuvi ustiga qurilgan sahna,
77 — ob-havo etyudi (bu shelfdagi birinchi tasviriy matn), 78 — bir
kunda ikki registr. Oldingi batchda maktab sahnasi / kundalik /
sirli hikoya boʻlgan edi.

⚠️ PJ-78 ATAYLAB toc'ning «qoʻshtirnoq ichi です・ます ni saqlaydi»
qoidasidan chetga chiqadi — chunki DARSNING OʻZI shu haqida. Matn
ikkala registrni yonma-yon koʻrsatadi: doʻst bilan kundalik nutq,
oʻqituvchi bilan 丁寧体. Qoida buzilmayapti, namoyish qilinyapti.

⚠️ CUMULATIVE:
    76 — みたい erkin; 擬音語 (PJ-77) va register materiali (PJ-78) YOʻQ.
    77 — 擬音語・擬態語 qoʻshiladi; PJ-78 materiali hali yoʻq.
    78 — hammasi erkin.

Audio (navbat bilan, oldingi batch Keita da tugagan edi):
    --only 76 --voice ja-JP-NanamiNeural
    --only 77 --voice ja-JP-KeitaNeural
    --only 78 --voice ja-JP-NanamiNeural

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_76_78.py --author=prime
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
        "title":   "みたいな こえ",
        "summary": (
            "PJ-76 matni. Pari telefonda notanish ovozni eshitadi va "
            "uni kimgadir oʻxshatadi. Butun matn みたい ustida "
            "yuradi — va oxirida 見たい ham chiqadi."
        ),
        "order":   76,
        "grammar": [
            {
                "pattern":  "oddiy shakl / ot + みたいです",
                "meaning":  "«…ga oʻxshaydi» — ようだ ning kundalik "
                            "egizagi. Yalangʻoch ulanadi: na だ, na な, "
                            "na の.",
                "examples": ["<ruby>風邪<rt>かぜ</rt></ruby>を<ruby>引<rt>ひ</rt></ruby>いたみたいです。",
                             "<ruby>子供<rt>こども</rt></ruby>みたいだった。"],
            },
            {
                "pattern":  "〜みたいな + ot · 〜みたいに + feʼl",
                "meaning":  "Oʻxshatish. みたい ham な-sifat kabi "
                            "tuslanadi, xuddi そう va よう kabi.",
                "examples": ["<ruby>子供<rt>こども</rt></ruby>みたいな<ruby>声<rt>こえ</rt></ruby>",
                             "<ruby>子供<rt>こども</rt></ruby>みたいに<ruby>笑<rt>わら</rt></ruby>った。"],
            },
            {
                "pattern":  "みたい ≠ <ruby>見<rt>み</rt></ruby>たい",
                "meaning":  "Ajratuvchi belgi — oldidagi が. "
                            "<ruby>顔<rt>かお</rt></ruby>が<ruby>見<rt>み</rt></ruby>たい "
                            "— «yuzini koʻrgim bor».",
                "examples": ["<ruby>顔<rt>かお</rt></ruby>が<ruby>見<rt>み</rt></ruby>たくなった。"],
            },
        ],
        "body": '''<p><ruby>金曜日<rt>きんようび</rt></ruby>の<ruby>夜<rt>よる</rt></ruby>、パリの<ruby>電話<rt>でんわ</rt></ruby>が<ruby>鳴<rt>な</rt></ruby>った。<ruby>知<rt>し</rt></ruby>らない<ruby>番号<rt>ばんごう</rt></ruby>だった。パリは<ruby>少<rt>すこ</rt></ruby>し<ruby>迷<rt>まよ</rt></ruby>ってから、<ruby>出<rt>で</rt></ruby>た。</p>

<p><strong>あいて:</strong> もしもし。ムニラさんのお<ruby>宅<rt>たく</rt></ruby>ですか。</p>

<p><ruby>子供<rt>こども</rt></ruby>みたいな<ruby>声<rt>こえ</rt></ruby>だった。でも<ruby>話<rt>はな</rt></ruby>し<ruby>方<rt>かた</rt></ruby>は<ruby>大人<rt>おとな</rt></ruby>みたいだった。パリは<span class="cn-word" data-tr="chalkashib qoldi"><ruby>混乱<rt>こんらん</rt></ruby>した</span>。</p>

<p><strong>パリ:</strong> いいえ、<ruby>違<rt>ちが</rt></ruby>います。<ruby>番号<rt>ばんごう</rt></ruby>が<ruby>違<rt>ちが</rt></ruby>うみたいです。</p>

<p><strong>あいて:</strong> あ、すみません。<ruby>一<rt>いち</rt></ruby><ruby>番<rt>ばん</rt></ruby>が<ruby>七<rt>なな</rt></ruby>みたいに<ruby>見<rt>み</rt></ruby>えました。</p>

<p>パリは<ruby>笑<rt>わら</rt></ruby>った。<ruby>相手<rt>あいて</rt></ruby>も<ruby>笑<rt>わら</rt></ruby>った。<ruby>笑<rt>わら</rt></ruby>い<ruby>声<rt>ごえ</rt></ruby>は<ruby>本当<rt>ほんとう</rt></ruby>に<ruby>子供<rt>こども</rt></ruby>みたいだった。</p>

<p><strong>あいて:</strong> <ruby>実<rt>じつ</rt></ruby>は、ムニラさんは<ruby>私<rt>わたし</rt></ruby>の<span class="cn-word" data-tr="birga oʻqiydigan doʻst"><ruby>同級生<rt>どうきゅうせい</rt></ruby></span>でした。<ruby>十年<rt>じゅうねん</rt></ruby><ruby>会<rt>あ</rt></ruby>っていません。</p>

<p><strong>パリ:</strong> そうですか。<ruby>探<rt>さが</rt></ruby>しているみたいですね。</p>

<p><strong>あいて:</strong> はい。でも<ruby>番号<rt>ばんごう</rt></ruby>を<ruby>間違<rt>まちが</rt></ruby>えたみたいです。<ruby>三回目<rt>さんかいめ</rt></ruby>です。</p>

<p>パリは<ruby>少<rt>すこ</rt></ruby>し<ruby>考<rt>かんが</rt></ruby>えた。<ruby>学校<rt>がっこう</rt></ruby>に ムニラという<ruby>名前<rt>なまえ</rt></ruby>の<ruby>友達<rt>ともだち</rt></ruby>がいる。<ruby>年<rt>とし</rt></ruby>は<span class="cn-word" data-tr="mos kelmaydi"><ruby>合<rt>あ</rt></ruby>わない</span>。<ruby>同<rt>おな</rt></ruby>じ<ruby>人<rt>ひと</rt></ruby>ではないみたいだ。でも<ruby>名字<rt>みょうじ</rt></ruby>を<ruby>聞<rt>き</rt></ruby>いてみた。</p>

<p><ruby>名字<rt>みょうじ</rt></ruby>は<ruby>同<rt>おな</rt></ruby>じだった。ムニラの<ruby>母<rt>はは</rt></ruby>の<ruby>名前<rt>なまえ</rt></ruby>も ムニラだ。<ruby>親子<rt>おやこ</rt></ruby>で<ruby>同<rt>おな</rt></ruby>じ<ruby>名前<rt>なまえ</rt></ruby>なのだ。</p>

<p><strong>パリ:</strong> <ruby>娘<rt>むすめ</rt></ruby>さんの<ruby>友達<rt>ともだち</rt></ruby>です。<ruby>伝<rt>つた</rt></ruby>えておきます。</p>

<p><ruby>電話<rt>でんわ</rt></ruby>を<ruby>切<rt>き</rt></ruby>ってから、パリは<ruby>窓<rt>まど</rt></ruby>の<ruby>外<rt>そと</rt></ruby>を<ruby>見<rt>み</rt></ruby>た。<ruby>十年<rt>じゅうねん</rt></ruby>という<span class="cn-word" data-tr="uzun vaqt"><ruby>長<rt>なが</rt></ruby>い<ruby>時間<rt>じかん</rt></ruby></span>を<ruby>考<rt>かんが</rt></ruby>えた。<ruby>自分<rt>じぶん</rt></ruby>も<ruby>十年後<rt>じゅうねんご</rt></ruby>、<ruby>誰<rt>だれ</rt></ruby>かの<ruby>顔<rt>かお</rt></ruby>が<ruby>見<rt>み</rt></ruby>たくなるのかもしれない。</p>''',
        "questions": [
            {
                "text": "パリは<ruby>相手<rt>あいて</rt></ruby>の<ruby>声<rt>こえ</rt></ruby>をどう<ruby>思<rt>おも</rt></ruby>いましたか。",
                "choices": [
                    "<ruby>子供<rt>こども</rt></ruby>みたいな<ruby>声<rt>こえ</rt></ruby>だと<ruby>思<rt>おも</rt></ruby>った",
                    "<ruby>大人<rt>おとな</rt></ruby>みたいな<ruby>声<rt>こえ</rt></ruby>だと<ruby>思<rt>おも</rt></ruby>った",
                    "ムニラさんの<ruby>声<rt>こえ</rt></ruby>だと<ruby>思<rt>おも</rt></ruby>った",
                    "<ruby>聞<rt>き</rt></ruby>こえないと<ruby>思<rt>おも</rt></ruby>った",
                ],
                "answer": 0,
                "explanation": "Ovoz — bolanikiga, gapirish tarzi esa "
                               "kattanikiga oʻxshardi. Otdan oldin "
                               "<strong>みたいな</strong>, hech qanday "
                               "の siz.",
            },
            {
                "text": "<ruby>相手<rt>あいて</rt></ruby>はなぜ<ruby>番号<rt>ばんごう</rt></ruby>を<ruby>間違<rt>まちが</rt></ruby>えましたか。",
                "choices": [
                    "<ruby>一<rt>いち</rt></ruby>が<ruby>七<rt>なな</rt></ruby>みたいに<ruby>見<rt>み</rt></ruby>えたから",
                    "<ruby>電話<rt>でんわ</rt></ruby>が<ruby>古<rt>ふる</rt></ruby>かったから",
                    "ムニラさんが<ruby>番号<rt>ばんごう</rt></ruby>を<ruby>変<rt>か</rt></ruby>えたから",
                    "<ruby>夜<rt>よる</rt></ruby>だったから",
                ],
                "answer": 0,
                "explanation": "Feʼldan oldin <strong>みたいに</strong> — "
                               "«yettidek koʻrindi». Otdan oldin esa "
                               "みたいな. Matnda ikkalasi ham bor.",
            },
            {
                "text": "<ruby>最後<rt>さいご</rt></ruby>の<ruby>文<rt>ぶん</rt></ruby>の「<ruby>顔<rt>かお</rt></ruby>が<ruby>見<rt>み</rt></ruby>たくなる」 — これはどういう<ruby>意味<rt>いみ</rt></ruby>ですか。",
                "choices": [
                    "<ruby>誰<rt>だれ</rt></ruby>かの<ruby>顔<rt>かお</rt></ruby>を<ruby>見<rt>み</rt></ruby>たいと<ruby>思<rt>おも</rt></ruby>うようになる",
                    "<ruby>誰<rt>だれ</rt></ruby>かの<ruby>顔<rt>かお</rt></ruby>に<ruby>似<rt>に</rt></ruby>てくる",
                    "<ruby>誰<rt>だれ</rt></ruby>かの<ruby>顔<rt>かお</rt></ruby>が<ruby>見<rt>み</rt></ruby>えなくなる",
                    "<ruby>誰<rt>だれ</rt></ruby>かの<ruby>顔<rt>かお</rt></ruby>を<ruby>忘<rt>わす</rt></ruby>れる",
                ],
                "answer": 0,
                "explanation": "Bu <strong>見たい</strong> — 見る + たい "
                               "(PJ-39), «koʻrgim bor». Ajratuvchi belgi — "
                               "oldidagi <strong>が</strong>. みたい "
                               "boʻlsa, ot bilan orasida hech nima "
                               "boʻlmasdi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "あめの おと",
        "summary": (
            "PJ-77 matni — bir kun ichida yomgʻirning uch ovozi: "
            "ぽつぽつ, ザーザー, しとしと. Shelfdagi birinchi tasviriy "
            "matn, taqlid soʻzlar bilan toʻla."
        ),
        "order":   77,
        "grammar": [
            {
                "pattern":  "taqlid soʻzi + feʼl",
                "meaning":  "Taqlid soʻzi hol boʻlib feʼlni aniqlaydi. "
                            "Qoʻshimcha kerak emas.",
                "examples": ["<ruby>雨<rt>あめ</rt></ruby>がザーザー<ruby>降<rt>ふ</rt></ruby>っていた。",
                             "<ruby>星<rt>ほし</rt></ruby>がきらきら<ruby>光<rt>ひか</rt></ruby>っていた。"],
            },
            {
                "pattern":  "taqlid soʻzi + する / だ",
                "meaning":  "Baʼzilari feʼl yasaydi (ドキドキする), "
                            "baʼzilari holat boʻladi (くたくただ). "
                            "Tanlov qoida bilan chiqmaydi — juftlik "
                            "bilan yodlanadi.",
                "examples": ["<ruby>胸<rt>むね</rt></ruby>がドキドキした。",
                             "<ruby>足<rt>あし</rt></ruby>はくたくただった。"],
            },
            {
                "pattern":  "Katakana ↔ hiragana",
                "meaning":  "Tovush taqlidi katakana bilan, holat "
                            "taqlidi hiragana bilan yoziladi.",
                "examples": ["ザーザー · ゴロゴロ — tovush",
                             "しとしと · ぐっすり — holat"],
            },
        ],
        "body": '''<p><ruby>朝<rt>あさ</rt></ruby>、<ruby>雨<rt>あめ</rt></ruby>はぽつぽつ<ruby>降<rt>ふ</rt></ruby>り<ruby>出<rt>だ</rt></ruby>した。イムロンは<ruby>傘<rt>かさ</rt></ruby>を<ruby>持<rt>も</rt></ruby>たずに<ruby>家<rt>いえ</rt></ruby>を<ruby>出<rt>で</rt></ruby>た。すぐ<ruby>止<rt>や</rt></ruby>むみたいだったからだ。</p>

<p><ruby>駅<rt>えき</rt></ruby>まで<ruby>半分<rt>はんぶん</rt></ruby><ruby>来<rt>き</rt></ruby>たとき、<ruby>空<rt>そら</rt></ruby>がゴロゴロ<ruby>鳴<rt>な</rt></ruby>った。そして<ruby>雨<rt>あめ</rt></ruby>がザーザー<ruby>降<rt>ふ</rt></ruby>り<ruby>始<rt>はじ</rt></ruby>めた。イムロンは<span class="cn-word" data-tr="uyga qaytgisi keldi"><ruby>家<rt>いえ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>りたかった</span>。でも<ruby>駅<rt>えき</rt></ruby>のほうが<ruby>近<rt>ちか</rt></ruby>かった。</p>

<p><ruby>走<rt>はし</rt></ruby>った。<ruby>胸<rt>むね</rt></ruby>がドキドキした。<ruby>靴<rt>くつ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>で<ruby>水<rt>みず</rt></ruby>の<ruby>音<rt>おと</rt></ruby>がした。<ruby>駅<rt>えき</rt></ruby>に<ruby>着<rt>つ</rt></ruby>いたとき、<ruby>服<rt>ふく</rt></ruby>は<span class="cn-word" data-tr="shalabbo boʻldi"><ruby>全部<rt>ぜんぶ</rt></ruby><ruby>濡<rt>ぬ</rt></ruby>れていた</span>。</p>

<p><ruby>駅<rt>えき</rt></ruby>の<ruby>中<rt>なか</rt></ruby>で、<ruby>知<rt>し</rt></ruby>らない<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>がタオルをくれた。</p>

<p><strong>おんなのひと:</strong> どうぞ。<ruby>風邪<rt>かぜ</rt></ruby>を<ruby>引<rt>ひ</rt></ruby>きますよ。</p>

<p><strong>イムロン:</strong> ありがとうございます。<ruby>助<rt>たす</rt></ruby>かりました。</p>

<p><ruby>電車<rt>でんしゃ</rt></ruby>の<ruby>窓<rt>まど</rt></ruby>から<ruby>外<rt>そと</rt></ruby>を<ruby>見<rt>み</rt></ruby>た。<ruby>雨<rt>あめ</rt></ruby>はまだザーザー<ruby>降<rt>ふ</rt></ruby>っていた。<ruby>傘<rt>かさ</rt></ruby>を<ruby>持<rt>も</rt></ruby>っている<ruby>人<rt>ひと</rt></ruby>はゆっくり<ruby>歩<rt>ある</rt></ruby>いていた。<ruby>持<rt>も</rt></ruby>っていない<ruby>人<rt>ひと</rt></ruby>は<ruby>走<rt>はし</rt></ruby>っていた。<ruby>同<rt>おな</rt></ruby>じ<ruby>雨<rt>あめ</rt></ruby>なのに、<ruby>二種類<rt>にしゅるい</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>がいた。</p>

<p><ruby>学校<rt>がっこう</rt></ruby>に<ruby>着<rt>つ</rt></ruby>いたころ、<ruby>雨<rt>あめ</rt></ruby>はしとしとになっていた。<ruby>音<rt>おと</rt></ruby>がほとんどしない<ruby>雨<rt>あめ</rt></ruby>だ。<ruby>教室<rt>きょうしつ</rt></ruby>の<ruby>窓<rt>まど</rt></ruby>は<span class="cn-word" data-tr="buglanib qolgan edi"><ruby>白<rt>しろ</rt></ruby>くなっていた</span>。</p>

<p><ruby>昼<rt>ひる</rt></ruby>、<ruby>雨<rt>あめ</rt></ruby>が<ruby>止<rt>や</rt></ruby>んだ。<ruby>校庭<rt>こうてい</rt></ruby>の<ruby>水<rt>みず</rt></ruby>が<ruby>光<rt>ひか</rt></ruby>っていた。イムロンの<ruby>足<rt>あし</rt></ruby>はくたくただった。でも<ruby>気分<rt>きぶん</rt></ruby>はよかった。</p>

<p><ruby>夜<rt>よる</rt></ruby>、イムロンはぐっすり<ruby>寝<rt>ね</rt></ruby>た。<ruby>朝<rt>あさ</rt></ruby>のぽつぽつも、<ruby>昼<rt>ひる</rt></ruby>のしとしとも、<ruby>全部<rt>ぜんぶ</rt></ruby><ruby>同<rt>おな</rt></ruby>じ<ruby>雨<rt>あめ</rt></ruby>だった。<ruby>日本語<rt>にほんご</rt></ruby>はそれを<ruby>三<rt>みっ</rt></ruby>つの<ruby>言葉<rt>ことば</rt></ruby>で<ruby>呼<rt>よ</rt></ruby>ぶ。</p>''',
        "questions": [
            {
                "text": "<ruby>朝<rt>あさ</rt></ruby>の<ruby>雨<rt>あめ</rt></ruby>はどんな<ruby>雨<rt>あめ</rt></ruby>でしたか。",
                "choices": [
                    "ぽつぽつ — <ruby>少<rt>すこ</rt></ruby>しずつ<ruby>降<rt>ふ</rt></ruby>り<ruby>出<rt>だ</rt></ruby>した",
                    "ザーザー — <ruby>強<rt>つよ</rt></ruby>かった",
                    "しとしと — <ruby>静<rt>しず</rt></ruby>かだった",
                    "<ruby>雨<rt>あめ</rt></ruby>は<ruby>降<rt>ふ</rt></ruby>らなかった",
                ],
                "answer": 0,
                "explanation": "Matnda yomgʻir uch marta nom oladi: "
                               "ertalab <strong>ぽつぽつ</strong> "
                               "(tomchilab), yoʻlda <strong>ザーザー</strong> "
                               "(quyib), tushga yaqin "
                               "<strong>しとしと</strong> (mayda va tinch).",
            },
            {
                "text": "「<ruby>足<rt>あし</rt></ruby>はくたくただった」 — nega くたくたした emas?",
                "choices": [
                    "くたくた だ / です oladi, する emas",
                    "くたくた oʻtgan zamonda する olmaydi",
                    "<ruby>足<rt>あし</rt></ruby> bilan する ishlatilmaydi",
                    "Ikkalasi ham toʻgʻri",
                ],
                "answer": 0,
                "explanation": "Har bir taqlid soʻzi <strong>oʻz "
                               "feʼli bilan</strong> yodlanadi. Matnda "
                               "ikkala yoʻl ham bor: ドキドキ<strong>した</strong> "
                               "va くたくた<strong>だった</strong>.",
            },
            {
                "text": "ザーザー katakana bilan, しとしと hiragana bilan yozilgan. Nega?",
                "choices": [
                    "Birinchisi tovush, ikkinchisi holat",
                    "Birinchisi holat, ikkinchisi tovush",
                    "Birinchisi chet soʻz, ikkinchisi yaponcha",
                    "Yozuv tasodifiy tanlangan",
                ],
                "answer": 0,
                "explanation": "Katakana «bu oddiy yapon soʻzi emas» "
                               "degan belgi — tovush soʻz emas, shovqin. "
                               "しとしと esa deyarli tovushsiz yomgʻir, "
                               "yaʼni <strong>holat</strong>.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "ふたつの ことばづかい",
        "summary": (
            "PJ-78 matni. Rano bir daqiqada ikki xil gapiradi — "
            "doʻstiga kundalik nutqda, oʻqituvchiga 丁寧体 da. "
            "Butun dars bir sahnada koʻrinadi."
        ),
        "order":   78,
        "grammar": [
            {
                "pattern":  "Ikki registr bir sahnada",
                "meaning":  "Doʻst bilan kundalik nutq (だ tushadi, の "
                            "va よ), oʻqituvchi bilan 丁寧体. Bir odam, "
                            "ikki til.",
                "examples": ["<ruby>今日<rt>きょう</rt></ruby>はバイトなの。",
                             "<ruby>今日<rt>きょう</rt></ruby>はアルバイトがあります。"],
            },
            {
                "pattern":  "<ruby>僕<rt>ぼく</rt></ruby> · <ruby>俺<rt>おれ</rt></ruby> · あたし",
                "meaning":  "«Men» ning ohangi gapiruvchini tanishtiradi. "
                            "<ruby>私<rt>わたし</rt></ruby> esa hech qachon "
                            "xato emas.",
                "examples": ["<ruby>俺<rt>おれ</rt></ruby>は<ruby>行<rt>い</rt></ruby>かないぞ。",
                             "<ruby>私<rt>わたし</rt></ruby>は<ruby>行<rt>い</rt></ruby>きません。"],
            },
            {
                "pattern":  "«Siz» oʻrniga ism + さん",
                "meaning":  "あなた sovuq eshitiladi. Yapon tili "
                            "olmosh oʻrniga ismni ishlatadi.",
                "examples": ["ラノさんは<ruby>来<rt>き</rt></ruby>ますか。"],
            },
        ],
        "body": '''<p><ruby>水曜日<rt>すいようび</rt></ruby>の<ruby>放課後<rt>ほうかご</rt></ruby>、ラノは<ruby>教室<rt>きょうしつ</rt></ruby>を<ruby>出<rt>で</rt></ruby>た。<ruby>廊下<rt>ろうか</rt></ruby>でムニラに<ruby>会<rt>あ</rt></ruby>った。</p>

<p><strong>ムニラ:</strong> あ、ラノ！ もう<ruby>帰<rt>かえ</rt></ruby>るの？</p>

<p><strong>ラノ:</strong> うん、<ruby>今日<rt>きょう</rt></ruby>はバイトなの。めっちゃ<ruby>遅<rt>おそ</rt></ruby>れそう。</p>

<p><strong>ムニラ:</strong> やばいじゃん。<ruby>走<rt>はし</rt></ruby>って。</p>

<p>ラノは<ruby>笑<rt>わら</rt></ruby>って、<ruby>階段<rt>かいだん</rt></ruby>のほうへ<ruby>歩<rt>ある</rt></ruby>き<ruby>出<rt>だ</rt></ruby>した。そのとき<ruby>後<rt>うし</rt></ruby>ろから<ruby>声<rt>こえ</rt></ruby>が<ruby>聞<rt>き</rt></ruby>こえた。<ruby>担任<rt>たんにん</rt></ruby>の<ruby>先生<rt>せんせい</rt></ruby>だった。</p>

<p><strong>せんせい:</strong> ラノさん、<ruby>少々<rt>しょうしょう</rt></ruby>よろしいですか。</p>

<p>ラノは<span class="cn-word" data-tr="birdaniga, shu zahoti"><ruby>一瞬<rt>いっしゅん</rt></ruby>で</span><ruby>口<rt>くち</rt></ruby>を<ruby>変<rt>か</rt></ruby>えた。</p>

<p><strong>ラノ:</strong> はい、<ruby>大丈夫<rt>だいじょうぶ</rt></ruby>です。<ruby>何<rt>なん</rt></ruby>でしょうか。</p>

<p><strong>せんせい:</strong> <ruby>来週<rt>らいしゅう</rt></ruby>の<ruby>発表<rt>はっぴょう</rt></ruby>のことですが、<ruby>準備<rt>じゅんび</rt></ruby>は<ruby>進<rt>すす</rt></ruby>んでいますか。</p>

<p><strong>ラノ:</strong> はい。<ruby>今週中<rt>こんしゅうちゅう</rt></ruby>に<ruby>資料<rt>しりょう</rt></ruby>をお<ruby>送<rt>おく</rt></ruby>りします。</p>

<p><ruby>先生<rt>せんせい</rt></ruby>が<ruby>行<rt>い</rt></ruby>ってから、ムニラが<ruby>近<rt>ちか</rt></ruby>づいてきた。<span class="cn-word" data-tr="hayron boʻlgan yuz bilan"><ruby>驚<rt>おどろ</rt></ruby>いた<ruby>顔<rt>かお</rt></ruby>で</span>ラノを<ruby>見<rt>み</rt></ruby>ていた。</p>

<p><strong>ムニラ:</strong> ラノ、<ruby>今<rt>いま</rt></ruby>のすごい。<ruby>別人<rt>べつじん</rt></ruby>みたいだった。</p>

<p><strong>ラノ:</strong> <ruby>別人<rt>べつじん</rt></ruby>じゃないよ。<ruby>同<rt>おな</rt></ruby>じ<ruby>私<rt>わたし</rt></ruby>。</p>

<p>ラノは<ruby>階段<rt>かいだん</rt></ruby>を<ruby>下<rt>お</rt></ruby>りながら<ruby>考<rt>かんが</rt></ruby>えた。<ruby>日本語<rt>にほんご</rt></ruby>を<ruby>習<rt>なら</rt></ruby>い<ruby>始<rt>はじ</rt></ruby>めたころ、<ruby>教科書<rt>きょうかしょ</rt></ruby>には<ruby>一種類<rt>いっしゅるい</rt></ruby>の<ruby>日本語<rt>にほんご</rt></ruby>しかなかった。<ruby>今<rt>いま</rt></ruby>は<ruby>二種類<rt>にしゅるい</rt></ruby><ruby>使<rt>つか</rt></ruby>えるようになった。<ruby>言葉<rt>ことば</rt></ruby>が<ruby>増<rt>ふ</rt></ruby>えたのではない。<span class="cn-word" data-tr="masofani tanlash"><ruby>距離<rt>きょり</rt></ruby>を<ruby>選<rt>えら</rt></ruby>ぶ</span>ことを<ruby>覚<rt>おぼ</rt></ruby>えたのだ。</p>''',
        "questions": [
            {
                "text": "ラノはムニラと<ruby>先生<rt>せんせい</rt></ruby>に<ruby>同<rt>おな</rt></ruby>じ<ruby>話<rt>はな</rt></ruby>し<ruby>方<rt>かた</rt></ruby>をしましたか。",
                "choices": [
                    "いいえ。ムニラには<ruby>普通体<rt>ふつうたい</rt></ruby>、<ruby>先生<rt>せんせい</rt></ruby>には<ruby>丁寧体<rt>ていねいたい</rt></ruby>",
                    "はい。<ruby>両方<rt>りょうほう</rt></ruby><ruby>丁寧体<rt>ていねいたい</rt></ruby>",
                    "はい。<ruby>両方<rt>りょうほう</rt></ruby><ruby>普通体<rt>ふつうたい</rt></ruby>",
                    "いいえ。ムニラには<ruby>敬語<rt>けいご</rt></ruby>、<ruby>先生<rt>せんせい</rt></ruby>には<ruby>普通体<rt>ふつうたい</rt></ruby>",
                ],
                "answer": 0,
                "explanation": "«バイトなの» va «めっちゃ» — doʻst bilan. "
                               "«<ruby>大丈夫<rt>だいじょうぶ</rt></ruby>です» "
                               "va «お<ruby>送<rt>おく</rt></ruby>りします» — "
                               "oʻqituvchi bilan. Bitta daqiqada ikki "
                               "registr.",
            },
            {
                "text": "「<ruby>今日<rt>きょう</rt></ruby>はバイトなの」 — nega <strong>な</strong> paydo boʻldi?",
                "choices": [
                    "だ tushirilgani uchun の dan oldin bogʻlovchi kerak",
                    "バイト な-sifat boʻlgani uchun",
                    "の savol qoʻshimchasi boʻlgani uchun",
                    "Ayol kishi gapirgani uchun",
                ],
                "answer": 0,
                "explanation": "Ot va な-sifat oʻzidan keyin biror narsa "
                               "kelsa, bogʻlovchi talab qiladi — PJ-75 "
                               "dagi <ruby>元気<rt>げんき</rt></ruby>"
                               "<strong>な</strong>ようです bilan bir xil "
                               "mexanizm.",
            },
            {
                "text": "<ruby>最後<rt>さいご</rt></ruby>に ラノは<ruby>何<rt>なに</rt></ruby>を<ruby>覚<rt>おぼ</rt></ruby>えたと<ruby>思<rt>おも</rt></ruby>いましたか。",
                "choices": [
                    "<ruby>距離<rt>きょり</rt></ruby>を<ruby>選<rt>えら</rt></ruby>ぶこと",
                    "<ruby>新<rt>あたら</rt></ruby>しい<ruby>言葉<rt>ことば</rt></ruby>をたくさん",
                    "<ruby>敬語<rt>けいご</rt></ruby>だけ",
                    "<ruby>別人<rt>べつじん</rt></ruby>になること",
                ],
                "answer": 0,
                "explanation": "«<ruby>言葉<rt>ことば</rt></ruby>が"
                               "<ruby>増<rt>ふ</rt></ruby>えたのではない» — "
                               "yangi soʻzlar emas, <strong>masofani "
                               "tanlash</strong>. Keigo bloki (PJ-68…72) "
                               "ham aynan shu haqida edi.",
            },
        ],
    },
]
