# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-82 … PJ-84. Burch va vaqtning aniq nuqtasi.

Uzunlik Blok F tasmasida (190–270 soʻz).

Shakl navbati: 82 — kundalik (日記), 83 — xat (メール), 84 — kichik
kulgili hikoya. Oldingi batchda 随筆 / tushuntirish matni / detektiv
boʻlgan edi.

Registr: 82 va 84 — 普通体 (PJ-45 dan beri hikoyachi shunday gapiradi).
83 — xat, shuning uchun boshdan oxirigacha 丁寧体 (toc bunga ruxsat
beradi: «xat va kundaliklar ikkalasidan birini tanlaydi va oxirigacha
ushlab turadi»).

⚠️ CUMULATIVE:
    82 — べき oilasi va なければならない erkin. ばかり (PJ-83) va
         ところ (PJ-84) YOʻQ.
    83 — + ばかり ning uchala ulanishi. ところ hali YOʻQ.
    84 — hammasi erkin; matn ataylab たところ va たばかり ni yonma-yon
         qoʻymaydi — solishtirish darsning ishi, hikoyaniki emas.

⚠️ 〜ているところ **holat** feʼliga tushmaydi, shuning uchun 84-matnda
「えきにいるところ」 emas, 「でんしゃを まっているところ」 turadi.

⚠️ しかたがない bu shelfda yozilmaydi: gate 〜しか〜ない (PJ-91) ni
qidiradi va bu ibora unga tushib qoladi.

Audio (navbat bilan, oldingi batch 81 da Keita bilan tugagan edi):
    --only 82 --voice ja-JP-NanamiNeural
    --only 83 --voice ja-JP-KeitaNeural
    --only 84 --voice ja-JP-NanamiNeural

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_82_84.py --author=prime
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
        "title":   "さいふの ひ",
        "summary": (
            "PJ-82 matni. Pari maktabga ketayotib yoʻlda hamyon topib "
            "oladi. Hech kim koʻrmadi, hech kim bilmaydi — lekin u "
            "nima qilish kerakligini biladi. Kundalik shaklidagi matn: "
            "butun voqea べき va なければならない ustida yuradi."
        ),
        "order":   82,
        "grammar": [
            {
                "pattern":  "<ruby>辞書形<rt>じしょけい</rt></ruby> + べきだ",
                "meaning":  "«… qilish toʻgʻri» — hech kim majburlamaydi, "
                            "lekin vijdon shuni aytadi. Inkori "
                            "べきではない, oʻtgan zamoni べきだった "
                            "(qilinmagan ish uchun afsus).",
                "examples": ["<ruby>返<rt>かえ</rt></ruby>すべきだ。",
                             "するべきだから、する。"],
            },
            {
                "pattern":  "〜なければならない",
                "meaning":  "«… qilmasam boʻlmaydi» — qoida yoki vaziyat "
                            "majbur qiladi. べき dan farqi shu: bu yerda "
                            "tanlov yoʻq.",
                "examples": ["<ruby>交番<rt>こうばん</rt></ruby>に<ruby>届<rt>とど</rt></ruby>けなければならない。"],
            },
            {
                "pattern":  "〜に<ruby>違<rt>ちが</rt></ruby>いない",
                "meaning":  "«shubhasiz …» — PJ-81 dagi ishonch. "
                            "Matnda topilgan hamyon egasining holati "
                            "shu bilan aytiladi.",
                "examples": ["<ruby>困<rt>こま</rt></ruby>っているに<ruby>違<rt>ちが</rt></ruby>いない。"],
            },
        ],
        "body": '''<p><ruby>十月<rt>じゅうがつ</rt></ruby><ruby>七日<rt>なのか</rt></ruby>、<ruby>火曜日<rt>かようび</rt></ruby>。<ruby>晴<rt>は</rt></ruby>れ。</p>

<p><ruby>学校<rt>がっこう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>く<ruby>道<rt>みち</rt></ruby>で、<ruby>白<rt>しろ</rt></ruby>い<span class="cn-word" data-tr="hamyon"><ruby>財布<rt>さいふ</rt></ruby></span>を<ruby>見<rt>み</rt></ruby>つけた。<ruby>中<rt>なか</rt></ruby>には<ruby>三千円<rt>さんぜんえん</rt></ruby>と、<ruby>一枚<rt>いちまい</rt></ruby>のカードが<ruby>入<rt>はい</rt></ruby>っていた。</p>

<p>はじめ、どきどきした。だれも<ruby>見<rt>み</rt></ruby>ていなかった。だれも<ruby>知<rt>し</rt></ruby>らない。でも、すぐに<ruby>分<rt>わ</rt></ruby>かった。これは<ruby>私<rt>わたし</rt></ruby>のお<ruby>金<rt>かね</rt></ruby>ではない。<span class="cn-word" data-tr="tushirib qoldirgan"><ruby>落<rt>お</rt></ruby>とした</span><ruby>人<rt>ひと</rt></ruby>は<ruby>今<rt>いま</rt></ruby>、<ruby>困<rt>こま</rt></ruby>っているに<ruby>違<rt>ちが</rt></ruby>いない。<ruby>返<rt>かえ</rt></ruby>すべきだ。</p>

<p><ruby>母<rt>はは</rt></ruby>はいつも<ruby>言<rt>い</rt></ruby>っていた。お<ruby>金<rt>かね</rt></ruby>を<ruby>拾<rt>ひろ</rt></ruby>ったら、<ruby>必<rt>かなら</rt></ruby>ず<span class="cn-word" data-tr="topshirmoq, yetkazmoq"><ruby>届<rt>とど</rt></ruby>ける</span>べきだ、と。</p>

<p><span class="cn-word" data-tr="mahalla militsiya punkti"><ruby>交番<rt>こうばん</rt></ruby></span>は<ruby>駅<rt>えき</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>にある。<ruby>学校<rt>がっこう</rt></ruby>に<ruby>遅<rt>おく</rt></ruby>れるかもしれないと<ruby>思<rt>おも</rt></ruby>ったが、<ruby>遅<rt>おく</rt></ruby>れてもいい。<ruby>落<rt>お</rt></ruby>とし<ruby>物<rt>もの</rt></ruby>は<ruby>交番<rt>こうばん</rt></ruby>に<ruby>届<rt>とど</rt></ruby>けなければならない。それが<span class="cn-word" data-tr="qoida, tartib"><ruby>決<rt>き</rt></ruby>まり</span>だ。</p>

<p>おまわりさんは<ruby>私<rt>わたし</rt></ruby>の<ruby>名前<rt>なまえ</rt></ruby>と<ruby>住所<rt>じゅうしょ</rt></ruby>を<ruby>書<rt>か</rt></ruby>いた。</p>

<p><strong>おまわりさん:</strong> ありがとう。<span class="cn-word" data-tr="egasi"><ruby>持<rt>も</rt></ruby>ち<ruby>主<rt>ぬし</rt></ruby></span>にすぐ<ruby>連絡<rt>れんらく</rt></ruby>しなければなりません。</p>

<p><ruby>学校<rt>がっこう</rt></ruby>には<ruby>十五分<rt>じゅうごふん</rt></ruby><ruby>遅<rt>おく</rt></ruby>れた。<ruby>先生<rt>せんせい</rt></ruby>に<ruby>理由<rt>りゆう</rt></ruby>を<ruby>話<rt>はな</rt></ruby>したら、<ruby>先生<rt>せんせい</rt></ruby>は<ruby>笑<rt>わら</rt></ruby>った。</p>

<p><strong>せんせい:</strong> それは<ruby>正<rt>ただ</rt></ruby>しいことをしましたね。</p>

<p><ruby>夕方<rt>ゆうがた</rt></ruby>、<ruby>交番<rt>こうばん</rt></ruby>から<ruby>電話<rt>でんわ</rt></ruby>が<ruby>来<rt>き</rt></ruby>た。<ruby>財布<rt>さいふ</rt></ruby>の<ruby>持<rt>も</rt></ruby>ち<ruby>主<rt>ぬし</rt></ruby>は<ruby>七十歳<rt>ななじゅっさい</rt></ruby>のおばあさんだった。<ruby>病院<rt>びょういん</rt></ruby>のお<ruby>金<rt>かね</rt></ruby>だったそうだ。</p>

<p>もし<ruby>私<rt>わたし</rt></ruby>があの<ruby>道<rt>みち</rt></ruby>を<ruby>通<rt>とお</rt></ruby>らなかったら、おばあさんはとても<ruby>困<rt>こま</rt></ruby>ったはずだ。</p>

<p><ruby>今日<rt>きょう</rt></ruby>、<ruby>一<rt>ひと</rt></ruby>つのことを<ruby>学<rt>まな</rt></ruby>んだ。<ruby>正<rt>ただ</rt></ruby>しいことをするのに、<ruby>理由<rt>りゆう</rt></ruby>はいらない。するべきだから、する。それだけだ。</p>''',
        "questions": [
            {
                "text": "パリはどうして<ruby>交番<rt>こうばん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きましたか。",
                "choices": [
                    "<ruby>落<rt>お</rt></ruby>とし<ruby>物<rt>もの</rt></ruby>は<ruby>届<rt>とど</rt></ruby>けなければならないから",
                    "<ruby>学校<rt>がっこう</rt></ruby>に<ruby>遅<rt>おく</rt></ruby>れたかったから",
                    "おばあさんに<ruby>会<rt>あ</rt></ruby>いたかったから",
                    "<ruby>先生<rt>せんせい</rt></ruby>に<ruby>言<rt>い</rt></ruby>われたから",
                ],
                "answer": 0,
                "explanation": "Matnda aniq aytilgan: topilgan narsani "
                               "koʻrsatilgan joyga topshirish shart — "
                               "«それが決まりだ». Oʻqituvchi voqeadan "
                               "keyin xabar topdi, undan oldin emas.",
            },
            {
                "text": "パリは<ruby>学校<rt>がっこう</rt></ruby>にどのくらい<ruby>遅<rt>おく</rt></ruby>れましたか。",
                "choices": [
                    "<ruby>十五分<rt>じゅうごふん</rt></ruby>",
                    "<ruby>三十分<rt>さんじゅっぷん</rt></ruby>",
                    "<ruby>一時間<rt>いちじかん</rt></ruby>",
                    "<ruby>遅<rt>おく</rt></ruby>れなかった",
                ],
                "answer": 0,
                "explanation": "«学校には十五分遅れた» — oʻn besh daqiqa. "
                               "Pari kechikishi mumkinligini oldindan "
                               "bilardi va shunga qaramay bordi.",
            },
            {
                "text": "<ruby>最後<rt>さいご</rt></ruby>にパリは<ruby>何<rt>なに</rt></ruby>を<ruby>学<rt>まな</rt></ruby>びましたか。",
                "choices": [
                    "<ruby>正<rt>ただ</rt></ruby>しいことをするのに<ruby>理由<rt>りゆう</rt></ruby>はいらない",
                    "お<ruby>金<rt>かね</rt></ruby>は<ruby>大切<rt>たいせつ</rt></ruby>だ",
                    "<ruby>学校<rt>がっこう</rt></ruby>に<ruby>遅<rt>おく</rt></ruby>れてはいけない",
                    "おばあさんは<ruby>親切<rt>しんせつ</rt></ruby>だ",
                ],
                "answer": 0,
                "explanation": "Kundalikning oxirgi qatori: toʻgʻri ish "
                               "uchun sabab kerak emas — «するべきだから、"
                               "する». Bu べきだ ning butun maʼnosi: "
                               "majburiyat emas, ichki burch.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "ついたばかりの メール",
        "summary": (
            "PJ-83 matni. Imron Yaponiyaga endigina yetib keldi va "
            "yaponiyalik doʻstiga xat yozadi: yotoqxona, xonadoshi, "
            "doʻkon ovqati, tez gapiradigan ustoz. ばかり ning uchala "
            "ulanishi ham shu xatda turadi."
        ),
        "order":   83,
        "grammar": [
            {
                "pattern":  "ot + ばかり",
                "meaning":  "«faqat shu, boshqasi yoʻq» — va koʻpincha "
                            "«haddan tashqari koʻp» degan baho bilan. "
                            "を va が tushib qoladi.",
                "examples": ["ゲームばかりしています。",
                             "パンばかり<ruby>食<rt>た</rt></ruby>べています。"],
            },
            {
                "pattern":  "〜てばかりいる",
                "meaning":  "«faqat shu ishni qilib yuradi» — takrorlanadigan "
                            "harakat, koʻpincha tanqid ohangida. いる ni "
                            "tashlab boʻlmaydi.",
                "examples": ["<ruby>聞<rt>き</rt></ruby>いてばかりいます。"],
            },
            {
                "pattern":  "〜たばかりだ · 〜たばかりの + ot",
                "meaning":  "«endigina …di». Soatga emas, gapiruvchining "
                            "hissiga qaraydi. Otni aniqlaganda oradan "
                            "の tushadi.",
                "examples": ["<ruby>着<rt>つ</rt></ruby>いたばかりです。",
                             "<ruby>買<rt>か</rt></ruby>ったばかりの<ruby>靴<rt>くつ</rt></ruby>"],
            },
        ],
        "body": '''<p><ruby>田中<rt>たなか</rt></ruby>さんへ</p>

<p>お<ruby>元気<rt>げんき</rt></ruby>ですか。イムロンです。<ruby>先週<rt>せんしゅう</rt></ruby>、<ruby>日本<rt>にほん</rt></ruby>に<ruby>着<rt>つ</rt></ruby>いたばかりです。まだ<ruby>何<rt>なに</rt></ruby>も<ruby>分<rt>わ</rt></ruby>かりませんが、<ruby>毎日<rt>まいにち</rt></ruby><ruby>楽<rt>たの</rt></ruby>しいです。</p>

<p><span class="cn-word" data-tr="yotoqxona"><ruby>寮<rt>りょう</rt></ruby></span>の<ruby>部屋<rt>へや</rt></ruby>は<ruby>小<rt>ちい</rt></ruby>さいですが、きれいです。<ruby>同<rt>おな</rt></ruby>じ<ruby>部屋<rt>へや</rt></ruby>のワンさんは<ruby>中国<rt>ちゅうごく</rt></ruby>から<ruby>来<rt>き</rt></ruby>た<ruby>学生<rt>がくせい</rt></ruby>です。ワンさんはゲームばかりしていて、あまり<ruby>勉強<rt>べんきょう</rt></ruby>しません。でも、とてもやさしい<ruby>人<rt>ひと</rt></ruby>です。</p>

<p><span class="cn-word" data-tr="ovqatlanish"><ruby>食事<rt>しょくじ</rt></ruby></span>の<ruby>話<rt>はなし</rt></ruby>もします。<ruby>近<rt>ちか</rt></ruby>くにコンビニがあるので、<ruby>私<rt>わたし</rt></ruby>はおにぎりとパンばかり<ruby>食<rt>た</rt></ruby>べています。<ruby>母<rt>はは</rt></ruby>がこの<ruby>手紙<rt>てがみ</rt></ruby>を<ruby>読<rt>よ</rt></ruby>んだら、きっと<span class="cn-word" data-tr="jahli chiqadi"><ruby>怒<rt>おこ</rt></ruby>る</span>でしょう。「<ruby>野菜<rt>やさい</rt></ruby>も<ruby>食<rt>た</rt></ruby>べるべきだ」と<ruby>言<rt>い</rt></ruby>われるに<ruby>違<rt>ちが</rt></ruby>いありません。</p>

<p><ruby>日本語<rt>にほんご</rt></ruby>の<ruby>授業<rt>じゅぎょう</rt></ruby>は<ruby>毎日<rt>まいにち</rt></ruby>あります。<ruby>先生<rt>せんせい</rt></ruby>の<ruby>話<rt>はなし</rt></ruby>は<ruby>速<rt>はや</rt></ruby>いです。<ruby>私<rt>わたし</rt></ruby>は<ruby>聞<rt>き</rt></ruby>いてばかりいて、まだ<ruby>質問<rt>しつもん</rt></ruby>ができません。でも、<ruby>来<rt>き</rt></ruby>たばかりですから、ゆっくり<span class="cn-word" data-tr="koʻnikmoq"><ruby>慣<rt>な</rt></ruby>れる</span>つもりです。</p>

<p><ruby>先月<rt>せんげつ</rt></ruby><ruby>買<rt>か</rt></ruby>ったばかりの<ruby>靴<rt>くつ</rt></ruby>は、もう<span class="cn-word" data-tr="iflos boʻldi"><ruby>汚<rt>よご</rt></ruby>れました</span>。<ruby>東京<rt>とうきょう</rt></ruby>は<ruby>歩<rt>ある</rt></ruby>く<ruby>町<rt>まち</rt></ruby>ですね。<ruby>毎日<rt>まいにち</rt></ruby><ruby>一時間<rt>いちじかん</rt></ruby><ruby>以上<rt>いじょう</rt></ruby><ruby>歩<rt>ある</rt></ruby>いています。</p>

<p><ruby>先週<rt>せんしゅう</rt></ruby>の<ruby>日曜日<rt>にちようび</rt></ruby>、ワンさんと<ruby>公園<rt>こうえん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きました。<ruby>桜<rt>さくら</rt></ruby>はもう<ruby>終<rt>お</rt></ruby>わっていましたが、<ruby>人<rt>ひと</rt></ruby>が<ruby>多<rt>おお</rt></ruby>くて<span class="cn-word" data-tr="hayron boʻldim"><ruby>驚<rt>おどろ</rt></ruby>きました</span>。ワンさんは<ruby>写真<rt>しゃしん</rt></ruby>ばかり<ruby>撮<rt>と</rt></ruby>っていて、なかなか<ruby>歩<rt>ある</rt></ruby>きません。でも、その<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>見<rt>み</rt></ruby>せてもらったら、とてもきれいでした。ゲームばかりの<ruby>人<rt>ひと</rt></ruby>だと<ruby>思<rt>おも</rt></ruby>っていましたが、<ruby>間違<rt>まちが</rt></ruby>っていました。</p>

<p><ruby>今度<rt>こんど</rt></ruby>、<ruby>田中<rt>たなか</rt></ruby>さんに<ruby>会<rt>あ</rt></ruby>いたいです。<ruby>時間<rt>じかん</rt></ruby>があったら、<ruby>教<rt>おし</rt></ruby>えてください。</p>

<p>イムロンより</p>''',
        "questions": [
            {
                "text": "ワンさんはどんな<ruby>人<rt>ひと</rt></ruby>ですか。",
                "choices": [
                    "ゲームばかりしていますが、やさしい<ruby>人<rt>ひと</rt></ruby>です",
                    "<ruby>毎日<rt>まいにち</rt></ruby><ruby>勉強<rt>べんきょう</rt></ruby>している<ruby>人<rt>ひと</rt></ruby>です",
                    "<ruby>日本<rt>にほん</rt></ruby>から<ruby>来<rt>き</rt></ruby>た<ruby>学生<rt>がくせい</rt></ruby>です",
                    "イムロンの<ruby>先生<rt>せんせい</rt></ruby>です",
                ],
                "answer": 0,
                "explanation": "Imron ikki narsani aytadi: Van faqat "
                               "oʻyin oʻynaydi va koʻp oʻqimaydi — "
                               "lekin juda mehribon. ゲームばかり "
                               "tanqid ohangini beradi, keyingi でも "
                               "esa uni yumshatadi.",
            },
            {
                "text": "イムロンはどうして<ruby>質問<rt>しつもん</rt></ruby>ができませんか。",
                "choices": [
                    "<ruby>日本<rt>にほん</rt></ruby>に<ruby>来<rt>き</rt></ruby>たばかりだからです",
                    "<ruby>先生<rt>せんせい</rt></ruby>がこわいからです",
                    "<ruby>授業<rt>じゅぎょう</rt></ruby>がないからです",
                    "<ruby>時間<rt>じかん</rt></ruby>がないからです",
                ],
                "answer": 0,
                "explanation": "«来たばかりですから» — sabab xatning "
                               "oʻzida turibdi. たばかり bu yerda "
                               "uzr ham, umid ham: hali yangi, "
                               "shuning uchun asta-sekin koʻnikadi.",
            },
            {
                "text": "イムロンの<ruby>靴<rt>くつ</rt></ruby>はどうなりましたか。",
                "choices": [
                    "<ruby>買<rt>か</rt></ruby>ったばかりですが、もう<ruby>汚<rt>よご</rt></ruby>れました",
                    "<ruby>古<rt>ふる</rt></ruby>いので、<ruby>捨<rt>す</rt></ruby>てました",
                    "<ruby>田中<rt>たなか</rt></ruby>さんにもらいました",
                    "まだ<ruby>買<rt>か</rt></ruby>っていません",
                ],
                "answer": 0,
                "explanation": "«先月買ったばかりの靴は、もう汚れました» "
                               "— bir oy oldin olingan, lekin Imron uchun "
                               "hali «yangi». たばかり soatni emas, hisni "
                               "oʻlchashining aniq misoli.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "あと いっぷん",
        "summary": (
            "PJ-84 matni. Ranoning payshanbasi: har bir ishga roppa-rosa "
            "bir daqiqa yetmaydi. Uydan chiqayotganda onasi chaqiradi, "
            "bekatga yetganda eshik yopiladi, sinfga kirayotganda ustoz "
            "uning ismini chaqirib boʻlgan edi. Butun matn ところ ustida "
            "yuradi."
        ),
        "order":   84,
        "grammar": [
            {
                "pattern":  "<ruby>辞書形<rt>じしょけい</rt></ruby> + ところ · 〜ているところ · 〜たところ",
                "meaning":  "Ish oʻqidagi uchta nuqta: hali boshlanmagan, "
                            "aynan hozir davom etyapti, hozirgina tugadi. "
                            "ところ har doim tor oynadan qaraydi.",
                "examples": ["<ruby>出<rt>で</rt></ruby>るところだった。",
                             "<ruby>待<rt>ま</rt></ruby>っているところに<ruby>電話<rt>でんわ</rt></ruby>が<ruby>来<rt>き</rt></ruby>た。",
                             "<ruby>呼<rt>よ</rt></ruby>んだところです。"],
            },
            {
                "pattern":  "〜ところに / 〜ところを",
                "meaning":  "«aynan oʻsha paytda» — ish shu daqiqada "
                            "uzilganini bildiradi. ところを dan keyin "
                            "koʻpincha <ruby>見<rt>み</rt></ruby>られる "
                            "kabi feʼl keladi.",
                "examples": ["<ruby>入<rt>はい</rt></ruby>るところを<ruby>見<rt>み</rt></ruby>られた。"],
            },
        ],
        "body": '''<p><ruby>木曜日<rt>もくようび</rt></ruby>の<ruby>朝<rt>あさ</rt></ruby>、ラノは<span class="cn-word" data-tr="omadi yurishmadi"><ruby>運<rt>うん</rt></ruby>が<ruby>悪<rt>わる</rt></ruby>かった</span>。</p>

<p><ruby>目<rt>め</rt></ruby>が<ruby>覚<rt>さ</rt></ruby>めたとき、<ruby>時計<rt>とけい</rt></ruby>は<ruby>七時<rt>しちじ</rt></ruby><ruby>五十分<rt>ごじゅっぷん</rt></ruby>だった。<ruby>学校<rt>がっこう</rt></ruby>は<ruby>八時<rt>はちじ</rt></ruby>に<ruby>始<rt>はじ</rt></ruby>まる。ラノは<ruby>急<rt>いそ</rt></ruby>いで<ruby>服<rt>ふく</rt></ruby>を<ruby>着<rt>き</rt></ruby>た。<ruby>家<rt>いえ</rt></ruby>を<ruby>出<rt>で</rt></ruby>るところに、<ruby>母<rt>はは</rt></ruby>が<ruby>呼<rt>よ</rt></ruby>んだ。</p>

<p><strong>はは:</strong> お<span class="cn-word" data-tr="tushlik quticha"><ruby>弁当<rt>べんとう</rt></ruby></span>を<ruby>忘<rt>わす</rt></ruby>れているよ。</p>

<p><ruby>戻<rt>もど</rt></ruby>って、<ruby>弁当<rt>べんとう</rt></ruby>を<ruby>持<rt>も</rt></ruby>って、また<ruby>走<rt>はし</rt></ruby>った。<ruby>駅<rt>えき</rt></ruby>に<ruby>着<rt>つ</rt></ruby>いたところで、<ruby>電車<rt>でんしゃ</rt></ruby>のドアが<span class="cn-word" data-tr="yopildi"><ruby>閉<rt>し</rt></ruby>まった</span>。あと<ruby>一分<rt>いっぷん</rt></ruby>。</p>

<p><ruby>次<rt>つぎ</rt></ruby>の<ruby>電車<rt>でんしゃ</rt></ruby>を<ruby>待<rt>ま</rt></ruby>っているところに、ムニラから<ruby>電話<rt>でんわ</rt></ruby>が<ruby>来<rt>き</rt></ruby>た。</p>

<p><strong>ムニラ:</strong> <ruby>今<rt>いま</rt></ruby>どこ。</p>

<p><strong>ラノ:</strong> <ruby>今<rt>いま</rt></ruby>、<ruby>電車<rt>でんしゃ</rt></ruby>を<ruby>待<rt>ま</rt></ruby>っているところ。</p>

<p><strong>ムニラ:</strong> <ruby>先生<rt>せんせい</rt></ruby>がもう<ruby>教室<rt>きょうしつ</rt></ruby>に<ruby>来<rt>き</rt></ruby>たよ。</p>

<p><ruby>電車<rt>でんしゃ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>で、ラノは<ruby>弁当<rt>べんとう</rt></ruby>の<ruby>箱<rt>はこ</rt></ruby>を<ruby>開<rt>あ</rt></ruby>けてみた。おにぎりが<ruby>二<rt>ふた</rt></ruby>つ<ruby>入<rt>はい</rt></ruby>っていた。<ruby>朝<rt>あさ</rt></ruby>ラノが<ruby>起<rt>お</rt></ruby>きたとき、<ruby>母<rt>はは</rt></ruby>はもうそれを<ruby>作<rt>つく</rt></ruby>っているところだった。ラノは<ruby>急<rt>いそ</rt></ruby>いでいて、<ruby>何<rt>なに</rt></ruby>も<ruby>言<rt>い</rt></ruby>わずに<ruby>出<rt>で</rt></ruby>てきた。<ruby>帰<rt>かえ</rt></ruby>ったら<ruby>謝<rt>あやま</rt></ruby>るべきだ、とラノは<ruby>思<rt>おも</rt></ruby>った。</p>

<p><ruby>学校<rt>がっこう</rt></ruby>に<ruby>着<rt>つ</rt></ruby>いたのは<ruby>八時<rt>はちじ</rt></ruby><ruby>二十分<rt>にじゅっぷん</rt></ruby>だった。<ruby>教室<rt>きょうしつ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>るところを、<ruby>先生<rt>せんせい</rt></ruby>に<ruby>見<rt>み</rt></ruby>られた。</p>

<p><strong>せんせい:</strong> ラノさん、<ruby>今<rt>いま</rt></ruby>ちょうどあなたの<ruby>名前<rt>なまえ</rt></ruby>を<ruby>呼<rt>よ</rt></ruby>んだところですよ。</p>

<p>みんなが<ruby>笑<rt>わら</rt></ruby>った。ラノも<ruby>笑<rt>わら</rt></ruby>った。<ruby>自分<rt>じぶん</rt></ruby>の<ruby>席<rt>せき</rt></ruby>に<ruby>座<rt>すわ</rt></ruby>ったとき、まだ<ruby>息<rt>いき</rt></ruby>が<ruby>切<rt>き</rt></ruby>れていた。</p>

<p>その<ruby>夜<rt>よる</rt></ruby>、ラノは<ruby>日記<rt>にっき</rt></ruby>に<ruby>書<rt>か</rt></ruby>いた。「<ruby>今日<rt>きょう</rt></ruby>は<ruby>一日中<rt>いちにちじゅう</rt></ruby>、あと<ruby>一分<rt>いっぷん</rt></ruby><span class="cn-word" data-tr="yetmadi"><ruby>足<rt>た</rt></ruby>りなかった</span>。でも、<ruby>最後<rt>さいご</rt></ruby>には<span class="cn-word" data-tr="ulgurdim"><ruby>間<rt>ま</rt></ruby>に<ruby>合<rt>あ</rt></ruby>った</span>。あと<ruby>一分<rt>いっぷん</rt></ruby>は、まだ<ruby>一分<rt>いっぷん</rt></ruby>ある、という<ruby>意味<rt>いみ</rt></ruby>でもある。」</p>''',
        "questions": [
            {
                "text": "ラノが<ruby>家<rt>いえ</rt></ruby>を<ruby>出<rt>で</rt></ruby>るところに、<ruby>何<rt>なに</rt></ruby>がありましたか。",
                "choices": [
                    "<ruby>母<rt>はは</rt></ruby>が<ruby>弁当<rt>べんとう</rt></ruby>のことを<ruby>言<rt>い</rt></ruby>った",
                    "ムニラから<ruby>電話<rt>でんわ</rt></ruby>が<ruby>来<rt>き</rt></ruby>た",
                    "<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>り<ruby>出<rt>だ</rt></ruby>した",
                    "<ruby>時計<rt>とけい</rt></ruby>が<ruby>止<rt>と</rt></ruby>まった",
                ],
                "answer": 0,
                "explanation": "«家を出るところに、母が呼んだ» — Rano "
                               "hali chiqmagan edi, bir oyogʻi ostonada. "
                               "ところに aynan shu uzilishni koʻrsatadi.",
            },
            {
                "text": "<ruby>先生<rt>せんせい</rt></ruby>はラノに<ruby>何<rt>なに</rt></ruby>と<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "<ruby>今<rt>いま</rt></ruby>ちょうど<ruby>名前<rt>なまえ</rt></ruby>を<ruby>呼<rt>よ</rt></ruby>んだところだ",
                    "もう<ruby>授業<rt>じゅぎょう</rt></ruby>が<ruby>終<rt>お</rt></ruby>わった",
                    "<ruby>明日<rt>あした</rt></ruby>は<ruby>早<rt>はや</rt></ruby>く<ruby>来<rt>き</rt></ruby>なさい",
                    "<ruby>弁当<rt>べんとう</rt></ruby>を<ruby>忘<rt>わす</rt></ruby>れたでしょう",
                ],
                "answer": 0,
                "explanation": "«今ちょうど名前を呼んだところですよ» — "
                               "ism bir necha soniya oldin chaqirilgan. "
                               "たところ ちょうど bilan doim yonma-yon "
                               "yuradi, chunki ikkalasi ham aniq daqiqani "
                               "koʻrsatadi.",
            },
            {
                "text": "ラノは<ruby>日記<rt>にっき</rt></ruby>に<ruby>何<rt>なに</rt></ruby>と<ruby>書<rt>か</rt></ruby>きましたか。",
                "choices": [
                    "あと<ruby>一分<rt>いっぷん</rt></ruby>は、まだ<ruby>一分<rt>いっぷん</rt></ruby>あるという<ruby>意味<rt>いみ</rt></ruby>でもある",
                    "<ruby>明日<rt>あした</rt></ruby>は<ruby>早<rt>はや</rt></ruby>く<ruby>起<rt>お</rt></ruby>きるべきだ",
                    "<ruby>電車<rt>でんしゃ</rt></ruby>は<ruby>遅<rt>おそ</rt></ruby>かった",
                    "ムニラに<ruby>謝<rt>あやま</rt></ruby>るべきだった",
                ],
                "answer": 0,
                "explanation": "Kundalikning oxirgi jumlasi kunni "
                               "teskari tomondan koʻrsatadi: yetishmagan "
                               "bir daqiqa — ayni paytda hali qolgan bir "
                               "daqiqa. Shuning uchun hikoya kulgi bilan "
                               "tugaydi, afsus bilan emas.",
            },
        ],
    },
]
