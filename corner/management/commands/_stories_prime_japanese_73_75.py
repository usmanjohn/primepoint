# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-73 … PJ-75. Taxminning toʻrt ovozi.

Hikoyachi 普通体 da (PJ-45 dan beri), qoʻshtirnoq ichi です・ます ni
saqlaydi.

Shakl navbati: 73 — sahna (maktab hovlisi), 74 — kundalik (日記),
75 — kichik sirli hikoya. Oldingi batchda telefon suhbati /
tushuntiruvchi esse / oilaviy sahna boʻlgan edi.

⚠️ CUMULATIVE — bu batchda u odatdagidan qattiqroq, chunki uchala
dars bitta qoʻshimchani boʻlishadi:
    73 — faqat 様態 そう (降りそうだ). 伝聞 そう YOʻQ, ようだ YOʻQ,
         らしい YOʻQ.
    74 — 伝聞 そう qoʻshiladi (降るそうだ). ようだ / らしい hali yoʻq.
    75 — toʻrttasi ham erkin.
Buni `verify_pj_stories_73_75.py` mexanik tekshiradi: har bir
「そう」 dan oldingi shakl qayta chiqariladi.

Audio (navbat bilan):
    --only 73 --voice ja-JP-KeitaNeural
    --only 74 --voice ja-JP-NanamiNeural
    --only 75 --voice ja-JP-KeitaNeural

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_73_75.py --author=prime
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
        "title":   "あめが ふりそうな そら",
        "summary": (
            "PJ-73 matni. Musobaqa mashqi kuni osmon qorayadi. "
            "Munira «yogʻay deb turibdi» deydi, oʻqituvchi "
            "«yogʻadiganga oʻxshamaydi» deydi — va biri haq chiqadi."
        ),
        "order":   73,
        "grammar": [
            {
                "pattern":  "ます-oʻzak + そうだ",
                "meaning":  "Koʻrganimdan chiqargan xulosa — «…ay deb "
                            "turibdi». Feʼlning oxiri kesiladi.",
                "examples": ["<ruby>今<rt>いま</rt></ruby>にも<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>りそうだった。",
                             "<ruby>降<rt>ふ</rt></ruby>りそうにありませんね。"],
            },
            {
                "pattern":  "い-sifat (い tushadi) + そうだ",
                "meaning":  "«…ga oʻxshaydi, …koʻrinadi». な-sifatdan "
                            "esa だ tushadi.",
                "examples": ["<ruby>眠<rt>ねむ</rt></ruby>そうな<ruby>顔<rt>かお</rt></ruby>をしていた。",
                             "<ruby>楽<rt>たの</rt></ruby>しそうだった。"],
            },
            {
                "pattern":  "そうな + ot · そうに + feʼl",
                "meaning":  "〜そう な-sifat kabi tuslanadi: otdan oldin "
                            "な, feʼldan oldin に.",
                "examples": ["<ruby>泣<rt>な</rt></ruby>きそうな<ruby>顔<rt>かお</rt></ruby>",
                             "<ruby>楽<rt>たの</rt></ruby>しそうに<ruby>笑<rt>わら</rt></ruby>った。"],
            },
        ],
        "body": '''<p><ruby>十月<rt>じゅうがつ</rt></ruby>の<ruby>土曜日<rt>どようび</rt></ruby>、ムニラは<ruby>朝<rt>あさ</rt></ruby>から<ruby>空<rt>そら</rt></ruby>を<ruby>見<rt>み</rt></ruby>ていた。<ruby>雲<rt>くも</rt></ruby>が<ruby>厚<rt>あつ</rt></ruby>くて、<span class="cn-word" data-tr="hozir-hozir, mana-mana"><ruby>今<rt>いま</rt></ruby>にも</span><ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>りそうだった。<ruby>今日<rt>きょう</rt></ruby>は<ruby>運動会<rt>うんどうかい</rt></ruby>の<ruby>練習<rt>れんしゅう</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>だ。</p>

<p><span class="cn-word" data-tr="maktab hovlisi"><ruby>校庭<rt>こうてい</rt></ruby></span>に<ruby>着<rt>つ</rt></ruby>くと、イムロンがもう<ruby>来<rt>き</rt></ruby>ていた。イムロンは<ruby>眠<rt>ねむ</rt></ruby>そうな<ruby>顔<rt>かお</rt></ruby>をしていた。</p>

<p><strong>イムロン:</strong> <ruby>昨日<rt>きのう</rt></ruby>、<ruby>遅<rt>おそ</rt></ruby>くまで<ruby>走<rt>はし</rt></ruby>っていました。<ruby>足<rt>あし</rt></ruby>が<ruby>痛<rt>いた</rt></ruby>いです。</p>

<p><strong>ムニラ:</strong> でも、<ruby>空<rt>そら</rt></ruby>を<ruby>見<rt>み</rt></ruby>てください。<ruby>今<rt>いま</rt></ruby>にも<ruby>降<rt>ふ</rt></ruby>りそうですよ。</p>

<p><ruby>二人<rt>ふたり</rt></ruby>が<ruby>話<rt>はな</rt></ruby>していると、<ruby>先生<rt>せんせい</rt></ruby>が<ruby>来<rt>き</rt></ruby>た。<ruby>先生<rt>せんせい</rt></ruby>は<ruby>空<rt>そら</rt></ruby>を<ruby>見<rt>み</rt></ruby>て、<ruby>少<rt>すこ</rt></ruby>し<ruby>考<rt>かんが</rt></ruby>えた。</p>

<p><strong>せんせい:</strong> <ruby>降<rt>ふ</rt></ruby>りそうにありませんね。<ruby>始<rt>はじ</rt></ruby>めましょう。</p>

<p><ruby>練習<rt>れんしゅう</rt></ruby>が<ruby>始<rt>はじ</rt></ruby>まった。<ruby>三十分後<rt>さんじゅっぷんご</rt></ruby>、<ruby>大<rt>おお</rt></ruby>きな<ruby>音<rt>おと</rt></ruby>がして、<ruby>雨<rt>あめ</rt></ruby>が<ruby>落<rt>お</rt></ruby>ちてきた。みんな<ruby>走<rt>はし</rt></ruby>って<span class="cn-word" data-tr="sport zali"><ruby>体育館<rt>たいいくかん</rt></ruby></span>に<ruby>入<rt>はい</rt></ruby>った。ムニラの<ruby>服<rt>ふく</rt></ruby>はもう<ruby>濡<rt>ぬ</rt></ruby>れていた。イムロンは<ruby>泣<rt>な</rt></ruby>きそうな<ruby>顔<rt>かお</rt></ruby>をしていたが、すぐに<ruby>笑<rt>わら</rt></ruby>った。</p>

<p><strong>イムロン:</strong> <ruby>先生<rt>せんせい</rt></ruby>の<ruby>天気予報<rt>てんきよほう</rt></ruby>は<span class="cn-word" data-tr="toʻgʻri chiqmoq, roʻyobga chiqmoq"><ruby>当<rt>あ</rt></ruby>たり</span>ませんでしたね。</p>

<p><ruby>先生<rt>せんせい</rt></ruby>も<ruby>笑<rt>わら</rt></ruby>った。<ruby>体育館<rt>たいいくかん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>は、<ruby>外<rt>そと</rt></ruby>より<ruby>楽<rt>たの</rt></ruby>しそうだった。</p>''',
        "questions": [
            {
                "text": "ムニラは<ruby>朝<rt>あさ</rt></ruby>、<ruby>空<rt>そら</rt></ruby>を<ruby>見<rt>み</rt></ruby>て<ruby>何<rt>なに</rt></ruby>を<ruby>思<rt>おも</rt></ruby>いましたか。",
                "choices": [
                    "<ruby>今<rt>いま</rt></ruby>にも<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>りそうだと<ruby>思<rt>おも</rt></ruby>った",
                    "<ruby>雨<rt>あめ</rt></ruby>はもう<ruby>降<rt>ふ</rt></ruby>ったと<ruby>思<rt>おも</rt></ruby>った",
                    "<ruby>今日<rt>きょう</rt></ruby>はいい<ruby>天気<rt>てんき</rt></ruby>だと<ruby>思<rt>おも</rt></ruby>った",
                    "<ruby>練習<rt>れんしゅう</rt></ruby>はないと<ruby>思<rt>おも</rt></ruby>った",
                ],
                "answer": 0,
                "explanation": "<strong>降りそうだった</strong> — yomgʻir "
                               "hali yogʻmagan. Bu qolip doim <strong>hali "
                               "sodir boʻlmagan</strong> narsani bildiradi: "
                               "«yogʻay deb turibdi».",
            },
            {
                "text": "<ruby>先生<rt>せんせい</rt></ruby>は<ruby>空<rt>そら</rt></ruby>を<ruby>見<rt>み</rt></ruby>て<ruby>何<rt>なん</rt></ruby>と<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "<ruby>降<rt>ふ</rt></ruby>りそうにありません — «yogʻadiganga oʻxshamaydi»",
                    "<ruby>降<rt>ふ</rt></ruby>りそうです — «yogʻay deb turibdi»",
                    "<ruby>降<rt>ふ</rt></ruby>りました — «yogʻdi»",
                    "<ruby>降<rt>ふ</rt></ruby>るでしょう — «yogʻsa kerak»",
                ],
                "answer": 0,
                "explanation": "Feʼlda inkor <strong>そう dan keyin</strong> "
                               "keladi: 降りそうにありません. Oʻqituvchining "
                               "xulosasi notoʻgʻri chiqdi — oʻttiz daqiqadan "
                               "keyin yomgʻir yogʻdi.",
            },
            {
                "text": "「<ruby>泣<rt>な</rt></ruby>きそうな<ruby>顔<rt>かお</rt></ruby>」 — nega そうな, そうに emas?",
                "choices": [
                    "Keyingi soʻz ot, shuning uchun な",
                    "Keyingi soʻz feʼl, shuning uchun な",
                    "<ruby>泣<rt>な</rt></ruby>く feʼl boʻlgani uchun",
                    "Oʻtgan zamon boʻlgani uchun",
                ],
                "answer": 0,
                "explanation": "〜そう <strong>な-sifat kabi</strong> "
                               "tuslanadi: otdan oldin <strong>な</strong>, "
                               "feʼldan oldin <strong>に</strong>. Matnda "
                               "ikkalasi ham bor — 泣きそうな顔 va "
                               "楽しそうに笑った.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "せんぱいの はなし",
        "summary": (
            "PJ-74 matni — kundalik (日記). Bir kunda eshitilgan uchta "
            "xabar: yangi oʻqituvchi, yopiladigan kutubxona va "
            "senpaining imtihoni. Hammasi 〜そうだ bilan uzatiladi."
        ),
        "order":   74,
        "grammar": [
            {
                "pattern":  "oddiy shakl + そうだ",
                "meaning":  "Eshitilgan xabar — «…ekan». Hech nima "
                            "kesilmaydi; ot va な-sifat だ ni saqlaydi.",
                "examples": ["<ruby>新<rt>あたら</rt></ruby>しい<ruby>先生<rt>せんせい</rt></ruby>が<ruby>来<rt>く</rt></ruby>るそうだ。",
                             "<ruby>明日<rt>あした</rt></ruby>は<ruby>雨<rt>あめ</rt></ruby>だそうですよ。"],
            },
            {
                "pattern":  "〜によると · 〜の<ruby>話<rt>はなし</rt></ruby>では",
                "meaning":  "Xabarning manbasi. Gap boshida turadi va "
                            "deyarli doim そうだ bilan juftlashadi.",
                "examples": ["<ruby>天気予報<rt>てんきよほう</rt></ruby>によると、<ruby>明日<rt>あした</rt></ruby>は<ruby>雨<rt>あめ</rt></ruby>だそうです。",
                             "<ruby>先輩<rt>せんぱい</rt></ruby>の<ruby>話<rt>はなし</rt></ruby>では、<ruby>試験<rt>しけん</rt></ruby>は<ruby>難<rt>むずか</rt></ruby>しいそうだ。"],
            },
            {
                "pattern":  "<ruby>元気<rt>げんき</rt></ruby>そうだった ↔ <ruby>元気<rt>げんき</rt></ruby>だそうだ",
                "meaning":  "Bitta だ ikki qolipni ajratadi: birinchisi "
                            "«koʻrdim», ikkinchisi «eshitdim».",
                "examples": ["<ruby>先輩<rt>せんぱい</rt></ruby>は<ruby>元気<rt>げんき</rt></ruby>そうだった。"],
            },
        ],
        "body": '''<p><ruby>十一月三日<rt>じゅういちがつみっか</rt></ruby>　<ruby>水曜日<rt>すいようび</rt></ruby>　くもり</p>

<p><ruby>今日<rt>きょう</rt></ruby>、<span class="cn-word" data-tr="toʻgarak, klub"><ruby>部活<rt>ぶかつ</rt></ruby></span>の<span class="cn-word" data-tr="katta sinf oʻquvchisi, ustoz akaxon"><ruby>先輩<rt>せんぱい</rt></ruby></span>といろいろな<ruby>話<rt>はなし</rt></ruby>をした。<ruby>書<rt>か</rt></ruby>いておきたいことが<ruby>三<rt>みっ</rt></ruby>つある。</p>

<p><ruby>一<rt>ひと</rt></ruby>つ<ruby>目<rt>め</rt></ruby>。<ruby>来月<rt>らいげつ</rt></ruby>、<ruby>新<rt>あたら</rt></ruby>しい<ruby>先生<rt>せんせい</rt></ruby>が<ruby>来<rt>く</rt></ruby>るそうだ。<ruby>先輩<rt>せんぱい</rt></ruby>は<span class="cn-word" data-tr="oʻqituvchilar xonasi"><ruby>職員室<rt>しょくいんしつ</rt></ruby></span>で<ruby>聞<rt>き</rt></ruby>いたと<ruby>言<rt>い</rt></ruby>っていた。その<ruby>先生<rt>せんせい</rt></ruby>は<ruby>日本語<rt>にほんご</rt></ruby>も<ruby>韓国語<rt>かんこくご</rt></ruby>も<ruby>教<rt>おし</rt></ruby>えられるそうだ。</p>

<p><ruby>二<rt>ふた</rt></ruby>つ<ruby>目<rt>め</rt></ruby>。<ruby>図書館<rt>としょかん</rt></ruby>の<ruby>二階<rt>にかい</rt></ruby>が<ruby>閉<rt>し</rt></ruby>まるそうだ。<span class="cn-word" data-tr="taʼmirlash ishlari"><ruby>工事<rt>こうじ</rt></ruby></span>があるそうだ。<ruby>三月<rt>さんがつ</rt></ruby>まで<ruby>使<rt>つか</rt></ruby>えないそうだ。<ruby>試験<rt>しけん</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>なので、<ruby>少<rt>すこ</rt></ruby>し<ruby>困<rt>こま</rt></ruby>る。</p>

<p><ruby>三<rt>みっ</rt></ruby>つ<ruby>目<rt>め</rt></ruby>。<ruby>先輩<rt>せんぱい</rt></ruby>は<ruby>来年<rt>らいねん</rt></ruby>、<ruby>東京<rt>とうきょう</rt></ruby>の<ruby>大学<rt>だいがく</rt></ruby>を<span class="cn-word" data-tr="imtihon topshirmoq"><ruby>受<rt>う</rt></ruby>ける</span>そうだ。<ruby>先輩<rt>せんぱい</rt></ruby>の<ruby>話<rt>はなし</rt></ruby>では、あの<ruby>大学<rt>だいがく</rt></ruby>の<ruby>試験<rt>しけん</rt></ruby>はとても<ruby>難<rt>むずか</rt></ruby>しいそうだ。でも<ruby>先輩<rt>せんぱい</rt></ruby>は<ruby>元気<rt>げんき</rt></ruby>そうだった。<ruby>全然<rt>ぜんぜん</rt></ruby><ruby>心配<rt>しんぱい</rt></ruby>していない<ruby>顔<rt>かお</rt></ruby>だった。</p>

<p><ruby>先輩<rt>せんぱい</rt></ruby>に「<ruby>先輩<rt>せんぱい</rt></ruby>はすごいですね」と<ruby>言<rt>い</rt></ruby>ったら、<ruby>笑<rt>わら</rt></ruby>って<ruby>答<rt>こた</rt></ruby>えた。</p>

<p><strong>せんぱい:</strong> <ruby>天気予報<rt>てんきよほう</rt></ruby>によると、<ruby>明日<rt>あした</rt></ruby>は<ruby>雨<rt>あめ</rt></ruby>だそうですよ。<ruby>傘<rt>かさ</rt></ruby>を<ruby>忘<rt>わす</rt></ruby>れないでください。</p>

<p><ruby>大事<rt>だいじ</rt></ruby>な<ruby>話<rt>はなし</rt></ruby>の<ruby>後<rt>あと</rt></ruby>に、これだ。<ruby>先輩<rt>せんぱい</rt></ruby>はいつもこうだ。</p>''',
        "questions": [
            {
                "text": "<ruby>図書館<rt>としょかん</rt></ruby>の<ruby>二階<rt>にかい</rt></ruby>はどうなりますか。",
                "choices": [
                    "<ruby>工事<rt>こうじ</rt></ruby>があって、<ruby>三月<rt>さんがつ</rt></ruby>まで<ruby>使<rt>つか</rt></ruby>えない",
                    "<ruby>新<rt>あたら</rt></ruby>しい<ruby>本<rt>ほん</rt></ruby>が<ruby>入<rt>はい</rt></ruby>る",
                    "<ruby>三月<rt>さんがつ</rt></ruby>から<ruby>開<rt>あ</rt></ruby>く",
                    "<ruby>先生<rt>せんせい</rt></ruby>の<ruby>部屋<rt>へや</rt></ruby>になる",
                ],
                "answer": 0,
                "explanation": "Uchala gap ham <strong>そうだ</strong> bilan "
                               "tugaydi — yozuvchi bularni oʻzi koʻrmagan, "
                               "senpaidan <strong>eshitgan</strong>.",
            },
            {
                "text": "「<ruby>先輩<rt>せんぱい</rt></ruby>は<ruby>元気<rt>げんき</rt></ruby>そうだった」 — bu nimani bildiradi?",
                "choices": [
                    "Yozuvchi senpaini koʻrdi va tetik ekanini oʻzi sezdi",
                    "Yozuvchi senpai tetik ekanini birovdan eshitdi",
                    "Senpai tetik boʻlishni xohlagan",
                    "Senpai kasal edi",
                ],
                "answer": 0,
                "explanation": "だ <strong>yoʻq</strong> — demak bu koʻrinish "
                               "そう (PJ-73). Agar «元気<strong>だ</strong>"
                               "そうだ» boʻlsa, «tetik ekan» — eshitilgan "
                               "xabar boʻlardi. Butun farq bitta bogʻinda.",
            },
            {
                "text": "<ruby>先輩<rt>せんぱい</rt></ruby>は<ruby>明日<rt>あした</rt></ruby>の<ruby>天気<rt>てんき</rt></ruby>をどこで<ruby>知<rt>し</rt></ruby>りましたか。",
                "choices": [
                    "<ruby>天気予報<rt>てんきよほう</rt></ruby>で",
                    "<ruby>職員室<rt>しょくいんしつ</rt></ruby>で",
                    "<ruby>空<rt>そら</rt></ruby>を<ruby>見<rt>み</rt></ruby>て",
                    "<ruby>図書館<rt>としょかん</rt></ruby>で",
                ],
                "answer": 0,
                "explanation": "<strong>〜によると</strong> xabarning "
                               "manbasini koʻrsatadi va gapning boshida "
                               "turadi — oʻzbekcha «ob-havo maʼlumotiga "
                               "koʻra» bilan bir xil tartib.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "となりの へやの おと",
        "summary": (
            "PJ-75 matni — kichik sirli hikoya. Qoʻshni xonadan ovoz "
            "kelmay qoladi. Hikoyachining oʻz xulosalari ようだ bilan, "
            "boshqalardan eshitgani らしい bilan aytiladi."
        ),
        "order":   75,
        "grammar": [
            {
                "pattern":  "oddiy shakl + ようだ",
                "meaning":  "Dalil menda — koʻrdim, eshitdim, sezdim. "
                            "Ot <b>の</b>, な-sifat <b>な</b> oladi.",
                "examples": ["<ruby>誰<rt>だれ</rt></ruby>もいないようだ。",
                             "<ruby>長<rt>なが</rt></ruby>い<ruby>間<rt>あいだ</rt></ruby><ruby>何<rt>なに</rt></ruby>も<ruby>食<rt>た</rt></ruby>べていないようだった。"],
            },
            {
                "pattern":  "oddiy shakl + らしい",
                "meaning":  "Gap tashqaridan keldi — dalil menda emas. "
                            "Yalangʻoch ulanadi: na だ, na な, na の.",
                "examples": ["<ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>したらしいですよ。",
                             "<ruby>旅行<rt>りょこう</rt></ruby>に<ruby>行<rt>い</rt></ruby>っていたらしい。"],
            },
            {
                "pattern":  "〜のような + ot",
                "meaning":  "Oʻxshatish — «…ga oʻxshagan». ようだ ning "
                            "ikkinchi ishi; feʼl oldida ように boʻladi.",
                "examples": ["<ruby>子供<rt>こども</rt></ruby>のような<ruby>声<rt>こえ</rt></ruby>が<ruby>聞<rt>き</rt></ruby>こえた。"],
            },
        ],
        "body": '''<p><ruby>先週<rt>せんしゅう</rt></ruby>から、<ruby>隣<rt>となり</rt></ruby>の<ruby>部屋<rt>へや</rt></ruby>の<ruby>音<rt>おと</rt></ruby>が<ruby>聞<rt>き</rt></ruby>こえなくなった。</p>

<p><ruby>私<rt>わたし</rt></ruby>のアパートは<ruby>古<rt>ふる</rt></ruby>い。<ruby>壁<rt>かべ</rt></ruby>が<span class="cn-word" data-tr="yupqa"><ruby>薄<rt>うす</rt></ruby>い</span>ので、<ruby>隣<rt>となり</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>の<ruby>生活<rt>せいかつ</rt></ruby>の<ruby>音<rt>おと</rt></ruby>がいつも<ruby>聞<rt>き</rt></ruby>こえる。<ruby>朝<rt>あさ</rt></ruby><ruby>六時<rt>ろくじ</rt></ruby>のラジオ、<ruby>夜<rt>よる</rt></ruby><ruby>十時<rt>じゅうじ</rt></ruby>のテレビ。でも<ruby>先週<rt>せんしゅう</rt></ruby>の<ruby>火曜日<rt>かようび</rt></ruby>から、<ruby>何<rt>なに</rt></ruby>も<ruby>聞<rt>き</rt></ruby>こえない。</p>

<p><ruby>木曜日<rt>もくようび</rt></ruby>、ドアの<ruby>前<rt>まえ</rt></ruby>を<ruby>見<rt>み</rt></ruby>た。<ruby>新聞<rt>しんぶん</rt></ruby>が<span class="cn-word" data-tr="toʻplanib qolgan"><ruby>溜<rt>た</rt></ruby>まっている</span>。<ruby>電気<rt>でんき</rt></ruby>も<ruby>消<rt>き</rt></ruby>えている。<ruby>誰<rt>だれ</rt></ruby>もいないようだ。</p>

<p><span class="cn-word" data-tr="uy boshqaruvchisi, komendant"><ruby>管理人<rt>かんりにん</rt></ruby></span>さんに<ruby>聞<rt>き</rt></ruby>いてみた。</p>

<p><strong>かんりにん:</strong> <ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>したらしいですよ。<ruby>私<rt>わたし</rt></ruby>も<ruby>聞<rt>き</rt></ruby>いただけですが。</p>

<p>その<ruby>夜<rt>よる</rt></ruby>、<ruby>階段<rt>かいだん</rt></ruby>で<ruby>子供<rt>こども</rt></ruby>のような<ruby>声<rt>こえ</rt></ruby>が<ruby>聞<rt>き</rt></ruby>こえた。<ruby>私<rt>わたし</rt></ruby>は<ruby>驚<rt>おどろ</rt></ruby>いて、<ruby>下<rt>した</rt></ruby>を<ruby>見<rt>み</rt></ruby>た。<ruby>小<rt>ちい</rt></ruby>さな<ruby>猫<rt>ねこ</rt></ruby>が<ruby>一匹<rt>いっぴき</rt></ruby>、<ruby>隣<rt>となり</rt></ruby>の<ruby>部屋<rt>へや</rt></ruby>のドアの<ruby>前<rt>まえ</rt></ruby>に<ruby>座<rt>すわ</rt></ruby>っていた。</p>

<p><ruby>猫<rt>ねこ</rt></ruby>は<span class="cn-word" data-tr="ozib ketgan edi"><ruby>痩<rt>や</rt></ruby>せていた</span>。<ruby>長<rt>なが</rt></ruby>い<ruby>間<rt>あいだ</rt></ruby><ruby>何<rt>なに</rt></ruby>も<ruby>食<rt>た</rt></ruby>べていないようだった。<ruby>私<rt>わたし</rt></ruby>は<ruby>部屋<rt>へや</rt></ruby>に<ruby>戻<rt>もど</rt></ruby>って、<ruby>牛乳<rt>ぎゅうにゅう</rt></ruby>を<ruby>持<rt>も</rt></ruby>ってきた。</p>

<p><ruby>次<rt>つぎ</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>、<ruby>隣<rt>となり</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>が<ruby>帰<rt>かえ</rt></ruby>ってきた。<ruby>旅行<rt>りょこう</rt></ruby>に<ruby>行<rt>い</rt></ruby>っていたらしい。<ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>しの<ruby>話<rt>はなし</rt></ruby>はうそだった。<ruby>猫<rt>ねこ</rt></ruby>はその<ruby>人<rt>ひと</rt></ruby>の<ruby>猫<rt>ねこ</rt></ruby>で、<ruby>窓<rt>まど</rt></ruby>から<ruby>出<rt>で</rt></ruby>てしまったそうだ。</p>

<p><ruby>今<rt>いま</rt></ruby>、<ruby>壁<rt>かべ</rt></ruby>の<ruby>向<rt>む</rt></ruby>こうからまたラジオの<ruby>音<rt>おと</rt></ruby>が<ruby>聞<rt>き</rt></ruby>こえる。<ruby>音<rt>おと</rt></ruby>がないと、<ruby>少<rt>すこ</rt></ruby>し<ruby>寂<rt>さび</rt></ruby>しい。</p>''',
        "questions": [
            {
                "text": "「<ruby>誰<rt>だれ</rt></ruby>もいないようだ」 — <ruby>私<rt>わたし</rt></ruby>はどうしてそう<ruby>思<rt>おも</rt></ruby>いましたか。",
                "choices": [
                    "<ruby>新聞<rt>しんぶん</rt></ruby>が<ruby>溜<rt>た</rt></ruby>まっていて、<ruby>電気<rt>でんき</rt></ruby>も<ruby>消<rt>き</rt></ruby>えていたから",
                    "<ruby>管理人<rt>かんりにん</rt></ruby>さんが<ruby>言<rt>い</rt></ruby>ったから",
                    "<ruby>隣<rt>となり</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>が<ruby>言<rt>い</rt></ruby>ったから",
                    "<ruby>猫<rt>ねこ</rt></ruby>を<ruby>見<rt>み</rt></ruby>たから",
                ],
                "answer": 0,
                "explanation": "<strong>ようだ</strong> — dalil hikoyachining "
                               "oʻzida. U toʻplangan gazetani va oʻchgan "
                               "chiroqni <strong>koʻrdi</strong> va xulosani "
                               "oʻzi chiqardi.",
            },
            {
                "text": "<ruby>管理人<rt>かんりにん</rt></ruby>さんはなぜ「<ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>したらしいですよ」と<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "<ruby>自分<rt>じぶん</rt></ruby>も<ruby>聞<rt>き</rt></ruby>いただけで、<ruby>見<rt>み</rt></ruby>ていないから",
                    "<ruby>自分<rt>じぶん</rt></ruby>で<ruby>見<rt>み</rt></ruby>たから",
                    "<ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>しを<ruby>手伝<rt>てつだ</rt></ruby>ったから",
                    "<ruby>新聞<rt>しんぶん</rt></ruby>で<ruby>読<rt>よ</rt></ruby>んだから",
                ],
                "answer": 0,
                "explanation": "<strong>らしい</strong> javobgarlikni "
                               "oʻzidan uzoqlashtiradi — «shunday deyishdi». "
                               "Va u buni oʻzi ham aytadi: 「私も聞いた"
                               "だけですが」. Xabar yolgʻon chiqadi.",
            },
            {
                "text": "<ruby>猫<rt>ねこ</rt></ruby>はどうして<ruby>外<rt>そと</rt></ruby>に<ruby>出<rt>で</rt></ruby>ましたか。",
                "choices": [
                    "<ruby>窓<rt>まど</rt></ruby>から<ruby>出<rt>で</rt></ruby>てしまったそうだ",
                    "<ruby>隣<rt>となり</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>が<ruby>出<rt>だ</rt></ruby>した",
                    "<ruby>管理人<rt>かんりにん</rt></ruby>さんが<ruby>出<rt>だ</rt></ruby>した",
                    "ドアが<ruby>開<rt>あ</rt></ruby>いていた",
                ],
                "answer": 0,
                "explanation": "Oxirgi gapda uchinchi qolip chiqadi: "
                               "<strong>そうだ</strong> — hikoyachi buni "
                               "qoʻshnidan <strong>eshitdi</strong>. Bitta "
                               "matnda uchala taxmin qolipi ham bor.",
            },
        ],
    },
]
