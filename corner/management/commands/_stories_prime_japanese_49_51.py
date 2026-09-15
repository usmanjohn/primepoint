# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-49 … PJ-51.

Hikoyachi 普通体 da (PJ-45 dan beri), qoʻshtirnoq ichi です・ます ni
saqlaydi.

Shakl navbati: 49 — xat (bolalik xotirasi), 50 — reja hikoyasi,
51 — tushuntiruvchi matn (mashina qanday ishlaydi). Oldingi batchda
hikoya / masal / maktab sahnasi boʻlgan edi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_49_51.py --author=prime
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
        "title":   "ちいさい ときの なつ",
        "summary": (
            "PJ-49 matni — xat. Munira doʻstiga bolaligidagi yozlarni "
            "yozadi, va butun matn とき ustida yuradi: 小さいとき, "
            "子どものとき, 行ったとき."
        ),
        "order":   49,
        "grammar": [
            {
                "pattern":  "<ruby>普通体<rt>ふつうたい</rt></ruby> + とき",
                "meaning":  "«…ganda». とき — ot, shuning uchun undan "
                            "oldin PJ-48 ning qoidasi ishlaydi.",
                "examples": ["<ruby>小<rt>ちい</rt></ruby>さいとき、よく<ruby>泣<rt>な</rt></ruby>いた。",
                             "<ruby>子<rt>こ</rt></ruby>どものとき、<ruby>村<rt>むら</rt></ruby>へ<ruby>行<rt>い</rt></ruby>った。"],
            },
            {
                "pattern":  "Otdan oldin <b>の</b>, な-sifatdan oldin <b>な</b>",
                "meaning":  "とき ot boʻlgani uchun だ turolmaydi: "
                            "子どもの とき, ひまな とき.",
                "examples": ["<ruby>学生<rt>がくせい</rt></ruby>のとき", "ひまなとき"],
            },
            {
                "pattern":  "<ruby>行<rt>い</rt></ruby>くとき / <ruby>行<rt>い</rt></ruby>ったとき",
                "meaning":  "Lugʻat shakli — ish tugamagan; た-shakli — "
                            "ish tugagan. Zamon asosiy ishga qarab "
                            "oʻlchanadi.",
                "examples": ["<ruby>村<rt>むら</rt></ruby>へ<ruby>行<rt>い</rt></ruby>くとき、バスに<ruby>乗<rt>の</rt></ruby>った。",
                             "<ruby>村<rt>むら</rt></ruby>へ<ruby>着<rt>つ</rt></ruby>いたとき、おばあさんがいた。"],
            },
        ],
        "body": '''<p>パリさんへ</p>

<p><ruby>元気<rt>げんき</rt></ruby>か。<ruby>私<rt>わたし</rt></ruby>は<ruby>元気<rt>げんき</rt></ruby>だ。<ruby>今日<rt>きょう</rt></ruby>は<ruby>子<rt>こ</rt></ruby>どものときの<ruby>話<rt>はなし</rt></ruby>を<ruby>書<rt>か</rt></ruby>く。</p>

<p><ruby>小<rt>ちい</rt></ruby>さいとき、<ruby>毎年<rt>まいとし</rt></ruby><ruby>夏<rt>なつ</rt></ruby>に<ruby>村<rt>むら</rt></ruby>のおばあさんの<ruby>家<rt>いえ</rt></ruby>へ<ruby>行<rt>い</rt></ruby>った。<ruby>村<rt>むら</rt></ruby>へ<ruby>行<rt>い</rt></ruby>くとき、<ruby>母<rt>はは</rt></ruby>はいつも<span class="cn-word" data-tr="non">パン</span>を<ruby>作<rt>つく</rt></ruby>った。バスの<ruby>中<rt>なか</rt></ruby>でそれを<ruby>食<rt>た</rt></ruby>べた。</p>

<p><ruby>村<rt>むら</rt></ruby>に<ruby>着<rt>つ</rt></ruby>いたとき、おばあさんはもう<ruby>門<rt>もん</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>に<ruby>立<rt>た</rt></ruby>っていた。<ruby>私<rt>わたし</rt></ruby>の<ruby>名前<rt>なまえ</rt></ruby>を<ruby>大<rt>おお</rt></ruby>きい<ruby>声<rt>こえ</rt></ruby>で<ruby>呼<rt>よ</rt></ruby>んだ。</p>

<p><ruby>朝<rt>あさ</rt></ruby>はいつも<span class="cn-word" data-tr="issiq"><ruby>暑<rt>あつ</rt></ruby>かった</span>。ひまなとき、<ruby>私<rt>わたし</rt></ruby>たちは<span class="cn-word" data-tr="daryo"><ruby>川<rt>かわ</rt></ruby></span>へ<ruby>行<rt>い</rt></ruby>った。<ruby>水<rt>みず</rt></ruby>は<ruby>冷<rt>つめ</rt></ruby>たかった。</p>

<p><ruby>夜<rt>よる</rt></ruby>、<ruby>外<rt>そと</rt></ruby>で<ruby>食<rt>た</rt></ruby>べた。おばあさんは<ruby>食<rt>た</rt></ruby>べるとき、いつも<ruby>昔<rt>むかし</rt></ruby>の<ruby>話<rt>はなし</rt></ruby>をした。</p>

<p><strong>おばあさん:</strong> わたしが<ruby>学生<rt>がくせい</rt></ruby>のとき、この<ruby>村<rt>むら</rt></ruby>に<ruby>学校<rt>がっこう</rt></ruby>がありませんでした。<ruby>毎日<rt>まいにち</rt></ruby><ruby>一時間<rt>いちじかん</rt></ruby><ruby>歩<rt>ある</rt></ruby>きました。</p>

<p><ruby>私<rt>わたし</rt></ruby>はその<ruby>話<rt>はなし</rt></ruby>が<ruby>好<rt>す</rt></ruby>きだった。<ruby>今<rt>いま</rt></ruby>も<ruby>覚<rt>おぼ</rt></ruby>えている。</p>

<p><ruby>村<rt>むら</rt></ruby>を<ruby>出<rt>で</rt></ruby>るとき、おばあさんは<span class="cn-word" data-tr="hech nima demadi"><ruby>何<rt>なに</rt></ruby>も<ruby>言<rt>い</rt></ruby>わなかった</span>。バスが<ruby>出<rt>で</rt></ruby>たとき、まだ<ruby>門<rt>もん</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>にいた。</p>

<p>パリさんの<ruby>子<rt>こ</rt></ruby>どものときの<ruby>夏<rt>なつ</rt></ruby>はどうだったか。<ruby>手紙<rt>てがみ</rt></ruby>を<ruby>待<rt>ま</rt></ruby>っている。</p>

<p>ムニラ</p>''',
        "questions": [
            {
                "text": "ムニラさんは<ruby>小<rt>ちい</rt></ruby>さいとき、<ruby>夏<rt>なつ</rt></ruby>にどこへ<ruby>行<rt>い</rt></ruby>きましたか。",
                "choices": [
                    "Qishloqqa, buvisining uyiga",
                    "Dengiz boʻyiga",
                    "Maktab lageriga",
                    "Xolasining shahridagi uyiga",
                ],
                "answer": 0,
                "explanation": "<strong>村のおばあさんの家へ行った</strong> — "
                               "har yili yozda. «小さいとき» va «子どものとき» "
                               "— yaponchada bolalik haqida gapirishning eng "
                               "tabiiy ikki yoʻli.",
            },
            {
                "text": "«<ruby>村<rt>むら</rt></ruby>へ<ruby>行<rt>い</rt></ruby>くとき» va «<ruby>村<rt>むら</rt></ruby>に<ruby>着<rt>つ</rt></ruby>いたとき» — nega zamonlar boshqa?",
                "choices": [
                    "Birinchisida yoʻl hali tugamagan, ikkinchisida yetib borilgan",
                    "Birinchisi hozirgi, ikkinchisi oʻtgan zamon haqida",
                    "Birinchisi qishloq haqida, ikkinchisi shahar haqida",
                    "Ikkalasi bir xil, farqi yoʻq",
                ],
                "answer": 0,
                "explanation": "とき ichidagi zamon <strong>ish tugaganmi "
                               "yoki yoʻqmi</strong> degan savolga javob "
                               "beradi. Non yoʻlda yeyilgan — demak 行くとき. "
                               "Buvi darvoza oldida turgani esa yetib "
                               "borgandan keyin koʻringan — 着いたとき.",
            },
            {
                "text": "«<ruby>学生<rt>がくせい</rt></ruby>のとき» — nega bu yerda の?",
                "choices": [
                    "Chunki とき ot, va otdan oldin ot の oladi",
                    "Chunki 学生 な-sifat",
                    "Chunki gap oʻtgan zamonda",
                    "Chunki buvi katta yoshda",
                ],
                "answer": 0,
                "explanation": "とき — ot (<ruby>時<rt>とき</rt></ruby>), "
                               "shuning uchun undan oldin PJ-48 ning qoidasi "
                               "ishlaydi: ot <strong>の</strong>, な-sifat "
                               "<strong>な</strong>. «学生だとき» notoʻgʻri.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "テストが おわったら",
        "summary": (
            "PJ-50 matni. Uch doʻst imtihondan keyingi kunni rejalashtiradi "
            "— たら ning «…gach» maʼnosi. Oxirida esa uning uchinchi "
            "maʼnosi: kutilmagan kashfiyot."
        ),
        "order":   50,
        "grammar": [
            {
                "pattern":  "た-shakli + ら — «…gach»",
                "meaning":  "Shartdagi ish albatta boʻladigan boʻlsa, "
                            "たら «…gandan keyin» degani.",
                "examples": ["テストが<ruby>終<rt>お</rt></ruby>わったら<ruby>映画<rt>えいが</rt></ruby>を<ruby>見<rt>み</rt></ruby>る。"],
            },
            {
                "pattern":  "た-shakli + ら — «agar»",
                "meaning":  "Ish noaniq boʻlsa, oʻsha shakl sof shart "
                            "boʻlib qoladi. Farqni mazmun koʻrsatadi.",
                "examples": ["<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>ったら、<ruby>家<rt>いえ</rt></ruby>にいる。"],
            },
            {
                "pattern":  "Kutilmagan kashfiyot",
                "meaning":  "Ikkala qism ham oʻtgan zamonda boʻlsa, "
                            "たら «bordim — va koʻrdimki…» degani.",
                "examples": ["<ruby>教室<rt>きょうしつ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>ったら、<ruby>先生<rt>せんせい</rt></ruby>がいた。"],
            },
        ],
        "body": '''<p><ruby>木曜日<rt>もくようび</rt></ruby>の<ruby>昼<rt>ひる</rt></ruby>、イノムさんとラノさんとムニラさんは<ruby>教室<rt>きょうしつ</rt></ruby>の<ruby>窓<rt>まど</rt></ruby>の<ruby>近<rt>ちか</rt></ruby>くで<ruby>話<rt>はな</rt></ruby>していた。<span class="cn-word" data-tr="ertaga"><ruby>明日<rt>あした</rt></ruby></span>は<ruby>最後<rt>さいご</rt></ruby>のテストだった。</p>

<p><strong>イノム:</strong> テストが<ruby>終<rt>お</rt></ruby>わったら、<ruby>何<rt>なに</rt></ruby>をしますか。</p>

<p><strong>ラノ:</strong> <ruby>私<rt>わたし</rt></ruby>は<ruby>十時間<rt>じゅうじかん</rt></ruby><ruby>寝<rt>ね</rt></ruby>ます。<ruby>起<rt>お</rt></ruby>きたら、また<ruby>寝<rt>ね</rt></ruby>ます。</p>

<p>みんな<ruby>笑<rt>わら</rt></ruby>った。ムニラさんは<ruby>川<rt>かわ</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きたいと<ruby>言<rt>い</rt></ruby>った。<ruby>天気<rt>てんき</rt></ruby>がよかったら<ruby>自転車<rt>じてんしゃ</rt></ruby>で<ruby>行<rt>い</rt></ruby>く。<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>ったら、<ruby>家<rt>いえ</rt></ruby>で<ruby>映画<rt>えいが</rt></ruby>を<ruby>見<rt>み</rt></ruby>る。</p>

<p>イノムさんは<span class="cn-word" data-tr="hech narsa oʻylamagan edi"><ruby>何<rt>なに</rt></ruby>も<ruby>考<rt>かんが</rt></ruby>えていなかった</span>。</p>

<p><strong>イノム:</strong> <ruby>安<rt>やす</rt></ruby>かったら、<ruby>新<rt>あたら</rt></ruby>しい<span class="cn-word" data-tr="poyabzal"><ruby>靴<rt>くつ</rt></ruby></span>を<ruby>買<rt>か</rt></ruby>いたいです。</p>

<p><ruby>金曜日<rt>きんようび</rt></ruby>、テストは<ruby>三時<rt>さんじ</rt></ruby>に<ruby>終<rt>お</rt></ruby>わった。<ruby>三人<rt>さんにん</rt></ruby>は<ruby>教室<rt>きょうしつ</rt></ruby>を<ruby>出<rt>で</rt></ruby>た。<ruby>外<rt>そと</rt></ruby>は<ruby>暑<rt>あつ</rt></ruby>かった。</p>

<p>イノムさんは<ruby>店<rt>みせ</rt></ruby>へ<ruby>行<rt>い</rt></ruby>った。<ruby>店<rt>みせ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>ったら、<ruby>先生<rt>せんせい</rt></ruby>がいた。<ruby>先生<rt>せんせい</rt></ruby>も<ruby>靴<rt>くつ</rt></ruby>を<span class="cn-word" data-tr="qidirayotgan edi"><ruby>探<rt>さが</rt></ruby>していた</span>。</p>

<p><strong>せんせい:</strong> テストはどうでしたか。</p>

<p><strong>イノム:</strong> <ruby>難<rt>むずか</rt></ruby>しかったです。でも<ruby>終<rt>お</rt></ruby>わりました。</p>

<p><ruby>先生<rt>せんせい</rt></ruby>は<ruby>笑<rt>わら</rt></ruby>った。イノムさんは<ruby>靴<rt>くつ</rt></ruby>を<ruby>買<rt>か</rt></ruby>わなかった。<ruby>高<rt>たか</rt></ruby>かった。でも<ruby>家<rt>いえ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>ったら、<span class="cn-word" data-tr="onasi"><ruby>母<rt>はは</rt></ruby></span>が<ruby>新<rt>あたら</rt></ruby>しい<ruby>靴<rt>くつ</rt></ruby>を<ruby>持<rt>も</rt></ruby>っていた。</p>''',
        "questions": [
            {
                "text": "ラノさんはテストが<ruby>終<rt>お</rt></ruby>わったら<ruby>何<rt>なに</rt></ruby>をしますか。",
                "choices": [
                    "Oʻn soat uxlaydi, keyin yana uxlaydi",
                    "Daryoga boradi",
                    "Yangi poyabzal oladi",
                    "Kino koʻradi",
                ],
                "answer": 0,
                "explanation": "<strong>十時間寝ます。起きたら、また寝ます。</strong> "
                               "Bu yerdagi たら — «…gach»: imtihon tugashi ham, "
                               "uygʻonish ham aniq narsa, shubha emas.",
            },
            {
                "text": "«<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>ったら、<ruby>家<rt>いえ</rt></ruby>で<ruby>映画<rt>えいが</rt></ruby>を<ruby>見<rt>み</rt></ruby>る» — bu たら qaysi maʼnoda?",
                "choices": [
                    "«Agar» — yomgʻir yogʻishi noaniq",
                    "«…gach» — yomgʻir albatta yogʻadi",
                    "Kutilmagan kashfiyot",
                    "Buyruq",
                ],
                "answer": 0,
                "explanation": "Yomgʻir yogʻishiga <strong>shubha bor</strong>, "
                               "shuning uchun bu sof shart. Xuddi shu shakl "
                               "«テストが終わったら» da esa «…gach» maʼnosini "
                               "beradi — farqni mazmun koʻrsatadi.",
            },
            {
                "text": "«<ruby>店<rt>みせ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>ったら、<ruby>先生<rt>せんせい</rt></ruby>がいた» — nega bu uchinchi maʼno?",
                "choices": [
                    "Chunki ikkala qism ham oʻtgan zamonda va oʻqituvchini koʻrish kutilmagan edi",
                    "Chunki doʻkonga kirish noaniq edi",
                    "Chunki gap qoʻshtirnoq ichida",
                    "Chunki 入る I guruh feʼli",
                ],
                "answer": 0,
                "explanation": "Kutilmagan kashfiyot たら sining ikkita "
                               "belgisi bor: <strong>ikkala qism ham oʻtgan "
                               "zamonda</strong>, va ikkinchi qism gapiruvchiga "
                               "bogʻliq emas. Oʻzbekchada ham aynan shunday "
                               "aytiladi: «doʻkonga kirsam, oʻqituvchi turibdi».",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "じどうはんばいきの なか",
        "summary": (
            "PJ-51 matni — tushuntiruvchi matn. Yaponiyadagi avtomat "
            "qanday ishlaydi, va matn boshdan-oyoq と ustida yuradi: "
            "«bossang — chiqadi»."
        ),
        "order":   51,
        "grammar": [
            {
                "pattern":  "lugʻat shakli + と",
                "meaning":  "«…sa, har doim shunday boʻladi». Mashina, "
                            "tabiat qonuni, yoʻl koʻrsatish — hammasi と "
                            "bilan.",
                "examples": ["ボタンを<ruby>押<rt>お</rt></ruby>すと、<ruby>飲<rt>の</rt></ruby>み<ruby>物<rt>もの</rt></ruby>が<ruby>出<rt>で</rt></ruby>ます。"],
            },
            {
                "pattern":  "え-qator + ば",
                "meaning":  "Mantiqiy shart: «bu boʻlsa, u boʻladi». "
                            "い-sifatda い → ければ.",
                "examples": ["<ruby>近<rt>ちか</rt></ruby>ければ<ruby>歩<rt>ある</rt></ruby>く。",
                             "ボタンを<ruby>押<rt>お</rt></ruby>せば<ruby>分<rt>わ</rt></ruby>かる。"],
            },
            {
                "pattern":  "と dan keyin buyruq turolmaydi",
                "meaning":  "と «har doim shunday» degani, shuning uchun "
                            "undan keyin iltimos yoki xohish kelmaydi — "
                            "u yerda たら ishlatiladi.",
                "examples": ["お<ruby>金<rt>かね</rt></ruby>がなかったら、<ruby>店<rt>みせ</rt></ruby>へ<ruby>行<rt>い</rt></ruby>ってください。"],
            },
        ],
        "body": '''<p><ruby>日本<rt>にほん</rt></ruby>の<ruby>町<rt>まち</rt></ruby>を<ruby>歩<rt>ある</rt></ruby>くと、<span class="cn-word" data-tr="avtomat"><ruby>自動販売機<rt>じどうはんばいき</rt></ruby></span>がたくさんある。<ruby>駅<rt>えき</rt></ruby>にも、<ruby>公園<rt>こうえん</rt></ruby>にも、<ruby>小<rt>ちい</rt></ruby>さい<ruby>村<rt>むら</rt></ruby>にもある。</p>

<p><ruby>機械<rt>きかい</rt></ruby>は<ruby>簡単<rt>かんたん</rt></ruby>だ。お<ruby>金<rt>かね</rt></ruby>を<ruby>入<rt>い</rt></ruby>れると、ボタンの<ruby>下<rt>した</rt></ruby>の<span class="cn-word" data-tr="chiroqcha">ランプ</span>がつく。ボタンを<ruby>押<rt>お</rt></ruby>すと、<ruby>飲<rt>の</rt></ruby>み<ruby>物<rt>もの</rt></ruby>が<ruby>下<rt>した</rt></ruby>から<ruby>出<rt>で</rt></ruby>る。お<ruby>金<rt>かね</rt></ruby>が<ruby>多<rt>おお</rt></ruby>かったら、<span class="cn-word" data-tr="qaytim">おつり</span>も<ruby>出<rt>で</rt></ruby>る。</p>

<p><ruby>機械<rt>きかい</rt></ruby>の<ruby>中<rt>なか</rt></ruby>はおもしろい。<ruby>機械<rt>きかい</rt></ruby>はまずお<ruby>金<rt>かね</rt></ruby>の<ruby>大<rt>おお</rt></ruby>きさと<span class="cn-word" data-tr="ogʻirlik"><ruby>重<rt>おも</rt></ruby>さ</span>を<ruby>見<rt>み</rt></ruby>る。<ruby>正<rt>ただ</rt></ruby>しければ、お<ruby>金<rt>かね</rt></ruby>は<ruby>中<rt>なか</rt></ruby>へ<ruby>入<rt>はい</rt></ruby>る。<ruby>正<rt>ただ</rt></ruby>しくなければ、<ruby>下<rt>した</rt></ruby>からすぐ<ruby>出<rt>で</rt></ruby>る。</p>

<p><ruby>冬<rt>ふゆ</rt></ruby>はあたたかい<ruby>飲<rt>の</rt></ruby>み<ruby>物<rt>もの</rt></ruby>も<ruby>売<rt>う</rt></ruby>っている。<span class="cn-word" data-tr="qizil"><ruby>赤<rt>あか</rt></ruby>い</span><ruby>字<rt>じ</rt></ruby>を<ruby>見<rt>み</rt></ruby>ると、それはあたたかい。<span class="cn-word" data-tr="koʻk"><ruby>青<rt>あお</rt></ruby>い</span><ruby>字<rt>じ</rt></ruby>を<ruby>見<rt>み</rt></ruby>ると、それは<ruby>冷<rt>つめ</rt></ruby>たい。</p>

<p><ruby>日本<rt>にほん</rt></ruby>には<ruby>自動販売機<rt>じどうはんばいき</rt></ruby>が<ruby>四百万台<rt>よんひゃくまんだい</rt></ruby>ぐらいある。<ruby>人<rt>ひと</rt></ruby>の<ruby>数<rt>かず</rt></ruby>で<ruby>見<rt>み</rt></ruby>ると、<ruby>世界<rt>せかい</rt></ruby>で<ruby>一番<rt>いちばん</rt></ruby><ruby>多<rt>おお</rt></ruby>い。<ruby>理由<rt>りゆう</rt></ruby>は<span class="cn-word" data-tr="bir nechta">いくつか</span>ある。<ruby>町<rt>まち</rt></ruby>が<ruby>安全<rt>あんぜん</rt></ruby>だ。<ruby>人<rt>ひと</rt></ruby>が<ruby>多<rt>おお</rt></ruby>い。<ruby>店<rt>みせ</rt></ruby>の<ruby>場所<rt>ばしょ</rt></ruby>が<ruby>高<rt>たか</rt></ruby>い。</p>

<p><ruby>外国<rt>がいこく</rt></ruby>から<ruby>来<rt>き</rt></ruby>た<ruby>人<rt>ひと</rt></ruby>はよく<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>る。<ruby>日本<rt>にほん</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>は<ruby>毎日<rt>まいにち</rt></ruby><ruby>見<rt>み</rt></ruby>ている。もう<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>らない。</p>

<p><ruby>機械<rt>きかい</rt></ruby>の<ruby>横<rt>よこ</rt></ruby>に「<ruby>動<rt>うご</rt></ruby>かなかったら、ここに<ruby>電話<rt>でんわ</rt></ruby>してください」と<ruby>書<rt>か</rt></ruby>いた<ruby>紙<rt>かみ</rt></ruby>がある。</p>''',
        "questions": [
            {
                "text": "ボタンを<ruby>押<rt>お</rt></ruby>すと<ruby>何<rt>なに</rt></ruby>が<ruby>出<rt>で</rt></ruby>ますか。",
                "choices": [
                    "Ichimlik — pastdan chiqadi",
                    "Chiroqcha yonadi",
                    "Qaytim pul",
                    "Chek",
                ],
                "answer": 0,
                "explanation": "<strong>ボタンを押すと、飲み物が下から出る。</strong> "
                               "Bu と ning oʻz maydoni: har safar shunday "
                               "boʻladi, shubha yoʻq.",
            },
            {
                "text": "お<ruby>金<rt>かね</rt></ruby>が<ruby>正<rt>ただ</rt></ruby>しくなければ、<ruby>何<rt>なに</rt></ruby>が<ruby>起<rt>お</rt></ruby>こりますか。",
                "choices": [
                    "Tanga pastdan darrov qaytib chiqadi",
                    "Mashina ovoz chiqaradi",
                    "Chiroqcha oʻchadi",
                    "Tanga ichkarida qoladi",
                ],
                "answer": 0,
                "explanation": "<strong>正しくなければ、下からすぐ出る。</strong> "
                               "«くなければ» — い-sifat inkorining ば shakli: "
                               "くない → <strong>くなければ</strong>.",
            },
            {
                "text": "«<ruby>機械<rt>きかい</rt></ruby>が<ruby>動<rt>うご</rt></ruby>かなかったら、…<ruby>電話<rt>でんわ</rt></ruby>してください» — nega bu yerda たら, と emas?",
                "choices": [
                    "Chunki と dan keyin iltimos turolmaydi",
                    "Chunki mashina har doim buziladi",
                    "Chunki 動く II guruh feʼli",
                    "Chunki gap inkorda",
                ],
                "answer": 0,
                "explanation": "と «har doim shunday boʻladi» degani, shuning "
                               "uchun undan keyin <strong>tabiat</strong> "
                               "turishi kerak, sizning irodangiz emas. "
                               "Iltimos, buyruq, taklif va xohish — hammasi "
                               "<strong>たら</strong> talab qiladi.",
            },
        ],
    },
]
