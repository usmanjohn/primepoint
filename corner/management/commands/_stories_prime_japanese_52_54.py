# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-52 … PJ-54.

Hikoyachi 普通体 da (PJ-45 dan beri), qoʻshtirnoq ichi です・ます ni
saqlaydi.

Shakl navbati: 52 — maslahat suhbati, 53 — hodisa/yangilik hikoyasi,
54 — kitob sharhi. Oldingi batchda xat / reja hikoyasi / tushuntiruvchi
matn boʻlgan edi.

⚠️ Har bir matn faqat OʻZ darsigacha boʻlgan grammatikani ishlatadi:
52 da から/ので va が/けど yoʻq, 53 da が/けど yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_52_54.py --author=prime
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
        "title":   "きょうとへ いくなら",
        "summary": (
            "PJ-52 matni. Rano Yaponiyaga boradi, va hamma unga "
            "maslahat beradi — har bir maslahat なら bilan "
            "boshlanadi, chunki shart Ranonikidir, maslahat "
            "beruvchiniki emas."
        ),
        "order":   52,
        "grammar": [
            {
                "pattern":  "<ruby>普通体<rt>ふつうたい</rt></ruby> + なら",
                "meaning":  "«…adigan boʻlsang». Shart suhbatdoshdan "
                            "olinadi, shuning uchun なら deyarli doim "
                            "maslahat bilan keladi.",
                "examples": ["<ruby>京都<rt>きょうと</rt></ruby>へ<ruby>行<rt>い</rt></ruby>くなら、<ruby>春<rt>はる</rt></ruby>がいいです。"],
            },
            {
                "pattern":  "Ot va な-sifatdan keyin だ TUSHADI",
                "meaning":  "なら ning oʻzi だ dan yasalgan, unga "
                            "ikkinchi だ kerak emas.",
                "examples": ["<ruby>学生<rt>がくせい</rt></ruby>なら<ruby>安<rt>やす</rt></ruby>い。",
                             "<ruby>静<rt>しず</rt></ruby>かなら、そこがいい。"],
            },
            {
                "pattern":  "Natija shartdan OLDIN",
                "meaning":  "Faqat なら da shunday: «boradigan boʻlsang, "
                            "xarita ol» — xarita ketishdan oldin "
                            "olinadi.",
                "examples": ["<ruby>行<rt>い</rt></ruby>くなら、<ruby>地図<rt>ちず</rt></ruby>を<ruby>買<rt>か</rt></ruby>ってください。"],
            },
        ],
        "body": '''<p>ラノさんは<ruby>夏<rt>なつ</rt></ruby>に<ruby>日本<rt>にほん</rt></ruby>へ<span class="cn-word" data-tr="sayohat"><ruby>旅行<rt>りょこう</rt></ruby></span>する。<ruby>昼<rt>ひる</rt></ruby>にみんなにそれを<ruby>言<rt>い</rt></ruby>った。すると、<ruby>三人<rt>さんにん</rt></ruby>が<ruby>三<rt>みっ</rt></ruby>つの<span class="cn-word" data-tr="maslahat"><ruby>助言<rt>じょげん</rt></ruby></span>をした。</p>

<p><strong>ムニラ:</strong> <ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>くなら、<ruby>京都<rt>きょうと</rt></ruby>がいいですよ。<ruby>古<rt>ふる</rt></ruby>い<ruby>町<rt>まち</rt></ruby>です。</p>

<p><strong>イノム:</strong> <ruby>京都<rt>きょうと</rt></ruby>へ<ruby>行<rt>い</rt></ruby>くなら、<ruby>春<rt>はる</rt></ruby>がいちばんきれいです。<span class="cn-word" data-tr="sakura"><ruby>桜<rt>さくら</rt></ruby></span>が<ruby>咲<rt>さ</rt></ruby>きます。</p>

<p><strong>パリ:</strong> <ruby>春<rt>はる</rt></ruby>なら<ruby>人<rt>ひと</rt></ruby>がとても<ruby>多<rt>おお</rt></ruby>いです。<ruby>秋<rt>あき</rt></ruby>のほうがいいと<ruby>思<rt>おも</rt></ruby>います。<span class="cn-word" data-tr="kuzgi qizil barglar"><ruby>紅葉<rt>こうよう</rt></ruby></span>もきれいです。</p>

<p>ラノさんは<ruby>笑<rt>わら</rt></ruby>った。<ruby>三人<rt>さんにん</rt></ruby>の<ruby>助言<rt>じょげん</rt></ruby>は<ruby>全部<rt>ぜんぶ</rt></ruby><ruby>違<rt>ちが</rt></ruby>った。</p>

<p><strong>ラノ:</strong> みなさん、ありがとうございます。でも、<ruby>私<rt>わたし</rt></ruby>の<ruby>休<rt>やす</rt></ruby>みは<ruby>夏<rt>なつ</rt></ruby>です。<ruby>春<rt>はる</rt></ruby>にも<ruby>秋<rt>あき</rt></ruby>にも<ruby>行<rt>い</rt></ruby>けません。</p>

<p><strong>ムニラ:</strong> <ruby>夏<rt>なつ</rt></ruby>なら、<ruby>北<rt>きた</rt></ruby>へ<ruby>行<rt>い</rt></ruby>ってください。<ruby>北海道<rt>ほっかいどう</rt></ruby>は<ruby>暑<rt>あつ</rt></ruby>くないです。</p>

<p>その<ruby>日<rt>ひ</rt></ruby>の<ruby>夜<rt>よる</rt></ruby>、ラノさんは<span class="cn-word" data-tr="xarita"><ruby>地図<rt>ちず</rt></ruby></span>を<ruby>見<rt>み</rt></ruby>た。<ruby>北海道<rt>ほっかいどう</rt></ruby>は<ruby>遠<rt>とお</rt></ruby>かった。<ruby>京都<rt>きょうと</rt></ruby>は<ruby>近<rt>ちか</rt></ruby>かった。</p>

<p>ラノさんは<ruby>京都<rt>きょうと</rt></ruby>を<span class="cn-word" data-tr="tanladi"><ruby>選<rt>えら</rt></ruby>んだ</span>。<ruby>行<rt>い</rt></ruby>くなら、<ruby>準備<rt>じゅんび</rt></ruby>が<ruby>要<rt>い</rt></ruby>る。<ruby>次<rt>つぎ</rt></ruby>の<ruby>朝<rt>あさ</rt></ruby>、<ruby>新<rt>あたら</rt></ruby>しいカメラを<ruby>買<rt>か</rt></ruby>った。</p>''',
        "questions": [
            {
                "text": "ムニラさんは<ruby>最初<rt>さいしょ</rt></ruby>に<ruby>何<rt>なに</rt></ruby>と<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "Yaponiyaga boradigan boʻlsa, Kioto yaxshi",
                    "Yozda shimolga borish kerak",
                    "Bahorda odam koʻp boʻladi",
                    "Kamera sotib olish kerak",
                ],
                "answer": 0,
                "explanation": "<strong>日本へ行くなら、京都がいいですよ。</strong> "
                               "Shart Ranoniki — Munira uni shunchaki "
                               "koʻtarib olyapti. Aynan shu なら ning ishi.",
            },
            {
                "text": "«<ruby>春<rt>はる</rt></ruby>なら<ruby>人<rt>ひと</rt></ruby>がとても<ruby>多<rt>おお</rt></ruby>いです» — nega bu yerda だ yoʻq?",
                "choices": [
                    "Chunki なら ning oʻzi だ dan yasalgan",
                    "Chunki 春 な-sifat",
                    "Chunki gap muloyim shaklda",
                    "Chunki bu savol",
                ],
                "answer": 0,
                "explanation": "なら oldida ot va な-sifat <strong>だ ni "
                               "tashlaydi</strong>: 春なら ✓, «春だなら» ✗. "
                               "Bu と (だと) va ot (な) qoidalaridan "
                               "farq qiladi.",
            },
            {
                "text": "«<ruby>行<rt>い</rt></ruby>くなら、<ruby>準備<rt>じゅんび</rt></ruby>が<ruby>要<rt>い</rt></ruby>る» — kamera qachon olindi?",
                "choices": [
                    "Safardan oldin, ertasi kuni ertalab",
                    "Kiotoda",
                    "Safardan keyin",
                    "Hali olinmagan",
                ],
                "answer": 0,
                "explanation": "Faqat <strong>なら</strong> da natija "
                               "shartdan oldin boʻla oladi. «行ったら» "
                               "boʻlganda kamera Yaponiyada olinardi — "
                               "bu ikki gap ikki boshqa reja haqida.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "でんしゃが とまったので",
        "summary": (
            "PJ-53 matni. Bir tongda poyezd toʻxtaydi va butun sinf "
            "kechikadi — har bir odam sababini boshqacha aytadi, "
            "kimdir から bilan, kimdir ので bilan."
        ),
        "order":   53,
        "grammar": [
            {
                "pattern":  "SABAB + ので + NATIJA",
                "meaning":  "«…gani uchun». Yumshoq, odobli: bu holat, "
                            "gapiruvchining qarori emas.",
                "examples": ["<ruby>電車<rt>でんしゃ</rt></ruby>が<ruby>止<rt>と</rt></ruby>まったので、<ruby>遅<rt>おく</rt></ruby>れました。"],
            },
            {
                "pattern":  "SABAB + から + NATIJA",
                "meaning":  "«…gani uchun», lekin bu MENING hukmim. "
                            "Buyruq va iltimos bilan yaxshi keladi.",
                "examples": ["<ruby>危<rt>あぶ</rt></ruby>ないから、<ruby>入<rt>はい</rt></ruby>らないでください。"],
            },
            {
                "pattern":  "ので oldida <b>な</b>, から oldida <b>だ</b>",
                "meaning":  "ので = の + で, va の ot. Shuning uchun "
                            "な-sifat va ot な kiyadi; から esa だ oladi.",
                "examples": ["<ruby>雨<rt>あめ</rt></ruby>なので · <ruby>雨<rt>あめ</rt></ruby>だから"],
            },
        ],
        "body": '''<p><ruby>火曜日<rt>かようび</rt></ruby>の<ruby>朝<rt>あさ</rt></ruby>、<ruby>駅<rt>えき</rt></ruby>に<ruby>人<rt>ひと</rt></ruby>がたくさん<ruby>立<rt>た</rt></ruby>っていた。<ruby>電車<rt>でんしゃ</rt></ruby>が<ruby>動<rt>うご</rt></ruby>かなかった。<ruby>北<rt>きた</rt></ruby>の<ruby>駅<rt>えき</rt></ruby>で<span class="cn-word" data-tr="hodisa"><ruby>事故<rt>じこ</rt></ruby></span>があったので、<ruby>全部<rt>ぜんぶ</rt></ruby>の<ruby>電車<rt>でんしゃ</rt></ruby>が<ruby>止<rt>と</rt></ruby>まった。</p>

<p><ruby>駅員<rt>えきいん</rt></ruby>の<ruby>声<rt>こえ</rt></ruby>が<ruby>聞<rt>き</rt></ruby>こえた。</p>

<p><strong>えきいん:</strong> <ruby>事故<rt>じこ</rt></ruby>がありましたので、<ruby>電車<rt>でんしゃ</rt></ruby>は<ruby>止<rt>と</rt></ruby>まっています。<ruby>危<rt>あぶ</rt></ruby>ないですから、<span class="cn-word" data-tr="sariq chiziq"><ruby>黄色<rt>きいろ</rt></ruby>い<ruby>線<rt>せん</rt></ruby></span>の<ruby>中<rt>なか</rt></ruby>に<ruby>入<rt>はい</rt></ruby>らないでください。</p>

<p>イノムさんは<ruby>時計<rt>とけい</rt></ruby>を<ruby>見<rt>み</rt></ruby>た。<ruby>八時<rt>はちじ</rt></ruby><ruby>十分<rt>じゅっぷん</rt></ruby>。<ruby>学校<rt>がっこう</rt></ruby>は<ruby>八時<rt>はちじ</rt></ruby><ruby>半<rt>はん</rt></ruby>に<ruby>始<rt>はじ</rt></ruby>まる。<ruby>間<rt>ま</rt></ruby>に<ruby>合<rt>あ</rt></ruby>わなかった。</p>

<p><span class="cn-word" data-tr="soat toʻqqizdan keyin"><ruby>九時<rt>くじ</rt></ruby>すぎ</span>に<ruby>教室<rt>きょうしつ</rt></ruby>に<ruby>着<rt>つ</rt></ruby>いた。<ruby>先生<rt>せんせい</rt></ruby>は<ruby>何<rt>なに</rt></ruby>も<ruby>言<rt>い</rt></ruby>わなかった。<ruby>教室<rt>きょうしつ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>は<span class="cn-word" data-tr="yarmi boʻsh"><ruby>半分<rt>はんぶん</rt></ruby>ぐらい<ruby>空<rt>あ</rt></ruby>いていた</span>。</p>

<p><ruby>昼<rt>ひる</rt></ruby>にみんなが<ruby>集<rt>あつ</rt></ruby>まった。<ruby>理由<rt>りゆう</rt></ruby>は<ruby>一<rt>ひと</rt></ruby>つだった。でも、みんなのことばは<ruby>違<rt>ちが</rt></ruby>った。</p>

<p><strong>パリ:</strong> <ruby>電車<rt>でんしゃ</rt></ruby>が<ruby>止<rt>と</rt></ruby>まったので、<ruby>遅<rt>おく</rt></ruby>れました。すみません。</p>

<p><strong>イノム:</strong> <ruby>電車<rt>でんしゃ</rt></ruby>が<ruby>止<rt>と</rt></ruby>まったから、<span class="cn-word" data-tr="mening aybim emas"><ruby>私<rt>わたし</rt></ruby>のせい</span>じゃありません。</p>

<p>ムニラさんはイノムさんを<ruby>見<rt>み</rt></ruby>た。ラノさんも<ruby>見<rt>み</rt></ruby>た。<ruby>二人<rt>ふたり</rt></ruby>は<ruby>何<rt>なに</rt></ruby>も<ruby>言<rt>い</rt></ruby>わなかった。</p>

<p><ruby>同<rt>おな</rt></ruby>じ<ruby>事故<rt>じこ</rt></ruby>、<ruby>同<rt>おな</rt></ruby>じ<ruby>朝<rt>あさ</rt></ruby>、<ruby>同<rt>おな</rt></ruby>じ<ruby>理由<rt>りゆう</rt></ruby>。ことばが<ruby>一<rt>ひと</rt></ruby>つ<ruby>違<rt>ちが</rt></ruby>った。それで<ruby>音<rt>おと</rt></ruby>が<ruby>全<rt>まった</rt></ruby>く<ruby>違<rt>ちが</rt></ruby>った。</p>''',
        "questions": [
            {
                "text": "なぜ<ruby>電車<rt>でんしゃ</rt></ruby>が<ruby>止<rt>と</rt></ruby>まりましたか。",
                "choices": [
                    "Shimoldagi bekatda hodisa yuz bergani uchun",
                    "Qattiq yomgʻir yoqqani uchun",
                    "Bayram kuni boʻlgani uchun",
                    "Mashinist kasal boʻlgani uchun",
                ],
                "answer": 0,
                "explanation": "<strong>北の駅で事故があったので、全部の電車が"
                               "止まった。</strong> Sabab oldinda, natija "
                               "keyin — yaponchada boshqa tartib yoʻq.",
            },
            {
                "text": "<ruby>駅員<rt>えきいん</rt></ruby>はなぜ「<ruby>危<rt>あぶ</rt></ruby>ないですから」と<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "Chunki keyin iltimos keladi — から buyruq bilan mos tushadi",
                    "Chunki ので faqat oʻtgan zamon bilan keladi",
                    "Chunki 危ない な-sifat",
                    "Chunki u kechikkan edi",
                ],
                "answer": 0,
                "explanation": "から — «men shuni sabab deb hisobladim». "
                               "Undan keyin <strong>入らないでください</strong> "
                               "turibdi. Oʻsha odam voqeani tushuntirganda "
                               "esa ので ishlatdi: 事故がありましたので.",
            },
            {
                "text": "パリさん bilan イノムさん ning gaplari nimasi bilan farq qiladi?",
                "choices": [
                    "Pari ので bilan uzr soʻradi, Inom から bilan oʻzini oqladi",
                    "Pari ertaroq kelgan edi",
                    "Inom boshqa sababni aytdi",
                    "Pari oddiy shaklda gapirdi",
                ],
                "answer": 0,
                "explanation": "Sabab bitta edi, soʻz bitta farq qildi. "
                               "<strong>ので</strong> — bu holat; "
                               "<strong>から</strong> — bu mening hukmim. "
                               "Shuning uchun kechirim soʻraganda doim ので.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "ながいけど おもしろい",
        "summary": (
            "PJ-54 matni — kitob sharhi. Munira sinf gazetasiga "
            "sharh yozadi, va sharh janri が / けど ustiga "
            "qurilgan: yaxshi tomoni, lekin yomon tomoni."
        ),
        "order":   54,
        "grammar": [
            {
                "pattern":  "GAP + が / けど + GAP",
                "meaning":  "«Lekin». Oʻzbekchadan farqli: birinchi "
                            "gapning oxiriga yopishadi, ikkinchisining "
                            "boshida turmaydi.",
                "examples": ["<ruby>長<rt>なが</rt></ruby>いけど<ruby>面白<rt>おもしろ</rt></ruby>い。",
                             "<ruby>難<rt>むずか</rt></ruby>しいですが、<ruby>読<rt>よ</rt></ruby>めます。"],
            },
            {
                "pattern":  "が — rasmiy · けど — suhbat",
                "meaning":  "Bitta maʼnoning toʻrtta uzunligi: "
                            "けど → けれど → けれども → が. Qanchalik "
                            "uzun, shunchalik rasmiy.",
                "examples": ["<ruby>高<rt>たか</rt></ruby>いですが、<ruby>買<rt>か</rt></ruby>います。"],
            },
            {
                "pattern":  "Ular muloyimlikni oʻzgartirmaydi",
                "meaning":  "と, とき va ので oddiy shakl talab qilgan "
                            "edi. が va けど esa oldingi gapga umuman "
                            "tegmaydi.",
                "examples": ["<ruby>安<rt>やす</rt></ruby>いですが、<ruby>買<rt>か</rt></ruby>いません。"],
            },
        ],
        "body": '''<p><ruby>学校<rt>がっこう</rt></ruby>の<span class="cn-word" data-tr="gazeta"><ruby>新聞<rt>しんぶん</rt></ruby></span>に<ruby>本<rt>ほん</rt></ruby>の<span class="cn-word" data-tr="sharh"><ruby>紹介<rt>しょうかい</rt></ruby></span>を<ruby>書<rt>か</rt></ruby>く。<ruby>今月<rt>こんげつ</rt></ruby>はムニラさんの<ruby>番<rt>ばん</rt></ruby>だった。</p>

<p><ruby>今月<rt>こんげつ</rt></ruby>の<ruby>本<rt>ほん</rt></ruby>：『<ruby>砂<rt>すな</rt></ruby>の<ruby>町<rt>まち</rt></ruby>』</p>

<p>この<ruby>本<rt>ほん</rt></ruby>は<ruby>四百<rt>よんひゃく</rt></ruby>ページあります。<ruby>長<rt>なが</rt></ruby>いですが、<ruby>面白<rt>おもしろ</rt></ruby>いです。<ruby>私<rt>わたし</rt></ruby>は<ruby>三日<rt>みっか</rt></ruby>で<ruby>読<rt>よ</rt></ruby>みました。</p>

<p><span class="cn-word" data-tr="hikoya"><ruby>物語<rt>ものがたり</rt></ruby></span>は<ruby>小<rt>ちい</rt></ruby>さい<ruby>町<rt>まち</rt></ruby>で<ruby>始<rt>はじ</rt></ruby>まります。<ruby>主人公<rt>しゅじんこう</rt></ruby>は<ruby>十六<rt>じゅうろく</rt></ruby><ruby>歳<rt>さい</rt></ruby>の<ruby>女<rt>おんな</rt></ruby>の<ruby>子<rt>こ</rt></ruby>です。<ruby>最初<rt>さいしょ</rt></ruby>の<ruby>百<rt>ひゃく</rt></ruby>ページは<span class="cn-word" data-tr="sekin"><ruby>遅<rt>おそ</rt></ruby>い</span>ですが、そのあとは<ruby>速<rt>はや</rt></ruby>いです。</p>

<p><ruby>言葉<rt>ことば</rt></ruby>は<ruby>難<rt>むずか</rt></ruby>しいですが、<ruby>会話<rt>かいわ</rt></ruby>は<ruby>易<rt>やさ</rt></ruby>しいです。<ruby>漢字<rt>かんじ</rt></ruby>も<ruby>多<rt>おお</rt></ruby>くないので、<ruby>私<rt>わたし</rt></ruby>たちも<ruby>読<rt>よ</rt></ruby>めます。</p>

<p><ruby>一<rt>ひと</rt></ruby>つ<ruby>言<rt>い</rt></ruby>いたいことがあります。<span class="cn-word" data-tr="oxiri"><ruby>終<rt>お</rt></ruby>わり</span>は<ruby>悲<rt>かな</rt></ruby>しいです。でも、<ruby>悪<rt>わる</rt></ruby>い<ruby>終<rt>お</rt></ruby>わりではありません。</p>

<p><ruby>図書館<rt>としょかん</rt></ruby>に<ruby>二冊<rt>にさつ</rt></ruby>あります。<ruby>読<rt>よ</rt></ruby>みたいなら、<ruby>早<rt>はや</rt></ruby>く<ruby>行<rt>い</rt></ruby>ってください。</p>

<p>ムニラ</p>

<p>ラノさんはこれを<ruby>読<rt>よ</rt></ruby>んだ。そして<ruby>図書館<rt>としょかん</rt></ruby>へ<ruby>走<rt>はし</rt></ruby>った。<ruby>二冊<rt>にさつ</rt></ruby>ともなかった。</p>''',
        "questions": [
            {
                "text": "ムニラさんはこの<ruby>本<rt>ほん</rt></ruby>をどう<ruby>思<rt>おも</rt></ruby>っていますか。",
                "choices": [
                    "Uzun, lekin qiziqarli — uch kunda oʻqib chiqqan",
                    "Qisqa va oson",
                    "Qiyin va zerikarli",
                    "Oxirigacha oʻqiy olmagan",
                ],
                "answer": 0,
                "explanation": "<strong>長いですが、面白いです。</strong> "
                               "Sharh janri が / けど ustiga qurilgan: "
                               "bir tomoni, lekin ikkinchi tomoni.",
            },
            {
                "text": "«<ruby>長<rt>なが</rt></ruby>いですが» — nega が birinchi gapga yopishgan?",
                "choices": [
                    "Chunki yaponchada «lekin» birinchi gapning oxiriga qoʻyiladi",
                    "Chunki 長い い-sifat",
                    "Chunki gap muloyim shaklda",
                    "Chunki bu sharh",
                ],
                "answer": 0,
                "explanation": "Oʻzbekchada «lekin» <strong>ikkinchi</strong> "
                               "gapning boshida turadi: «uzun, lekin qiziqarli». "
                               "Yaponchada が <strong>birinchi</strong> gapga "
                               "yopishadi — bir gap chapda. Shuni bir marta "
                               "sezsangiz, boshqa xato qilmaysiz.",
            },
            {
                "text": "«<ruby>読<rt>よ</rt></ruby>みたいなら、<ruby>早<rt>はや</rt></ruby>く<ruby>行<rt>い</rt></ruby>ってください» — nega bu yerda なら?",
                "choices": [
                    "Chunki shart oʻquvchidan olinadi va maslahat kitobxonga qaratilgan",
                    "Chunki kutubxona uzoq",
                    "Chunki kitob uzun",
                    "Chunki bu oʻtgan zamon",
                ],
                "answer": 0,
                "explanation": "なら (PJ-52) <strong>suhbatdoshning</strong> "
                               "niyatini koʻtarib oladi: «oʻqimoqchi "
                               "boʻlsangiz…». Va maslahat oʻqishdan "
                               "<em>oldin</em> beriladi — bu ham なら ning "
                               "oʻz ishi.",
            },
        ],
    },
]
