# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-55 … PJ-57.

Hikoyachi 普通体 da (PJ-45 dan beri), qoʻshtirnoq ichi です・ます ni
saqlaydi.

Shakl navbati: 55 — sport hikoyasi, 56 — intervyu, 57 — oʻzgarish
hikoyasi (ilgari / hozir). Oldingi batchda maslahat suhbati / hodisa
hikoyasi / kitob sharhi boʻlgan edi.

⚠️ CUMULATIVE: 55 da ために/ように yoʻq, 55 va 56 da なる yoʻq —
なる kursda faqat PJ-57 da ochiq oʻrgatiladi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_55_57.py --author=prime
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
        "title":   "あめが ふっても",
        "summary": (
            "PJ-55 matni. Maktab voleybol jamoasi musobaqadan oldingi "
            "hafta — yomgʻir yogʻsa ham, zal band boʻlsa ham mashq "
            "davom etadi."
        ),
        "order":   55,
        "grammar": [
            {
                "pattern":  "て-shakli + も",
                "meaning":  "«…sa ham». Natija shartga qaramaydi — "
                            "PJ-50 dagi たら ning teskarisi.",
                "examples": ["<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>っても、<ruby>練習<rt>れんしゅう</rt></ruby>する。"],
            },
            {
                "pattern":  "Ot va な-sifat <b>で</b> + も",
                "meaning":  "Otning て-shakli で (PJ-29), shuning uchun "
                            "でも. い-sifat esa くて + も.",
                "examples": ["<ruby>日曜日<rt>にちようび</rt></ruby>でも<ruby>来<rt>く</rt></ruby>る。",
                             "<ruby>寒<rt>さむ</rt></ruby>くても<ruby>走<rt>はし</rt></ruby>る。"],
            },
            {
                "pattern":  "Soʻroq soʻzi + ても",
                "meaning":  "«Farqi yoʻq»: いくら〜ても — «qancha …sa "
                            "ham», だれが〜ても — «kim …sa ham».",
                "examples": ["いくら<ruby>練習<rt>れんしゅう</rt></ruby>しても、<ruby>勝<rt>か</rt></ruby>てなかった。"],
            },
        ],
        "body": '''<p><ruby>試合<rt>しあい</rt></ruby>まで<ruby>一週間<rt>いっしゅうかん</rt></ruby>だった。バレーボール<span class="cn-word" data-tr="jamoa"><ruby>部<rt>ぶ</rt></ruby></span>は<ruby>毎日<rt>まいにち</rt></ruby><ruby>練習<rt>れんしゅう</rt></ruby>していた。</p>

<p><ruby>月曜日<rt>げつようび</rt></ruby>、<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>った。イノムさんは<ruby>今日<rt>きょう</rt></ruby>はないと<ruby>思<rt>おも</rt></ruby>った。でも<ruby>先輩<rt>せんぱい</rt></ruby>から<span class="cn-word" data-tr="xabar">れんらく</span>が<ruby>来<rt>き</rt></ruby>た。</p>

<p><strong>せんぱい:</strong> <ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>っても、<ruby>練習<rt>れんしゅう</rt></ruby>はあります。<ruby>体育館<rt>たいいくかん</rt></ruby>に<ruby>来<rt>き</rt></ruby>てください。</p>

<p><ruby>水曜日<rt>すいようび</rt></ruby>、<ruby>体育館<rt>たいいくかん</rt></ruby>はバスケット<ruby>部<rt>ぶ</rt></ruby>が<ruby>使<rt>つか</rt></ruby>っていた。<span class="cn-word" data-tr="hovli"><ruby>校庭<rt>こうてい</rt></ruby></span>は<ruby>濡<rt>ぬ</rt></ruby>れていた。<ruby>先輩<rt>せんぱい</rt></ruby>は<ruby>廊下<rt>ろうか</rt></ruby>を<ruby>見<rt>み</rt></ruby>た。</p>

<p><strong>せんぱい:</strong> ここでもいいです。<ruby>狭<rt>せま</rt></ruby>くても、パスの<ruby>練習<rt>れんしゅう</rt></ruby>はできます。</p>

<p><ruby>金曜日<rt>きんようび</rt></ruby>、ムニラさんが<ruby>足<rt>あし</rt></ruby>を<span class="cn-word" data-tr="jarohatladi"><ruby>怪我<rt>けが</rt></ruby>した</span>。ムニラさんは<ruby>休<rt>やす</rt></ruby>まなかった。<ruby>座<rt>すわ</rt></ruby>って、みんなの<ruby>数<rt>かず</rt></ruby>を<ruby>数<rt>かぞ</rt></ruby>えた。</p>

<p><ruby>日曜日<rt>にちようび</rt></ruby>、<ruby>試合<rt>しあい</rt></ruby>があった。いくら<ruby>頑張<rt>がんば</rt></ruby>っても、<span class="cn-word" data-tr="yutolmadik"><ruby>勝<rt>か</rt></ruby>てなかった</span>。<ruby>二対<rt>にたい</rt></ruby><ruby>三<rt>さん</rt></ruby>だった。</p>

<p><ruby>帰<rt>かえ</rt></ruby>りの<ruby>電車<rt>でんしゃ</rt></ruby>で、だれも<ruby>話<rt>はな</rt></ruby>さなかった。<ruby>駅<rt>えき</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>で<ruby>先輩<rt>せんぱい</rt></ruby>が<ruby>立<rt>た</rt></ruby>った。</p>

<p><strong>せんぱい:</strong> <ruby>来年<rt>らいねん</rt></ruby>もあります。<ruby>負<rt>ま</rt></ruby>けても、<ruby>練習<rt>れんしゅう</rt></ruby>は<ruby>続<rt>つづ</rt></ruby>けてください。</p>

<p>イノムさんは<ruby>次<rt>つぎ</rt></ruby>の<ruby>朝<rt>あさ</rt></ruby>も<ruby>体育館<rt>たいいくかん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>った。<ruby>六時<rt>ろくじ</rt></ruby>だった。だれもいないと<ruby>思<rt>おも</rt></ruby>った。ムニラさんがいた。</p>''',
        "questions": [
            {
                "text": "<ruby>月曜日<rt>げつようび</rt></ruby>、<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>ったとき、<ruby>練習<rt>れんしゅう</rt></ruby>はどうなりましたか。",
                "choices": [
                    "Bekor qilinmadi — sport zalida oʻtkazildi",
                    "Bekor qilindi",
                    "Hovlida oʻtkazildi",
                    "Yakshanbaga koʻchirildi",
                ],
                "answer": 0,
                "explanation": "<strong>雨が降っても、練習はあります。</strong> "
                               "ても da natija shartga qaramaydi — yomgʻir "
                               "mashqni bekor qilmaydi.",
            },
            {
                "text": "«<ruby>狭<rt>せま</rt></ruby>くても» va «ここでも» — nega ikki xil shakl?",
                "choices": [
                    "狭い い-sifat, shuning uchun くて; ここ ot, shuning uchun で",
                    "Birinchisi oʻtgan zamon, ikkinchisi hozirgi",
                    "Birinchisi muloyim, ikkinchisi oddiy",
                    "Ikkinchisi xato",
                ],
                "answer": 0,
                "explanation": "Bitta qoida, ikki koʻrinish: て-shakli "
                               "い-sifatda <strong>くて</strong>, ot va "
                               "な-sifatda <strong>で</strong> (PJ-29).",
            },
            {
                "text": "«いくら<ruby>頑張<rt>がんば</rt></ruby>っても» nimani anglatadi?",
                "choices": [
                    "Qancha harakat qilsak ham",
                    "Harakat qilganimiz uchun",
                    "Harakat qilsak",
                    "Harakat qilmadik",
                ],
                "answer": 0,
                "explanation": "Soʻroq soʻzi + ても = «farqi yoʻq». "
                               "<strong>いくら〜ても</strong> dan keyin "
                               "deyarli doim kutilmagan yoki teskari "
                               "natija keladi — bu yerda 勝てなかった.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "なんの ために",
        "summary": (
            "PJ-56 matni — maktab gazetasi uchun intervyu. Uch kishi "
            "nega oʻqiyotganini aytadi, va uchalasi ham ために yoki "
            "ように bilan javob beradi."
        ),
        "order":   56,
        "grammar": [
            {
                "pattern":  "Lugʻat shakli / OT + の + ために",
                "meaning":  "«…ish uchun». Maqsaddagi ishni gapiruvchi "
                            "oʻzi qiladi va boshqara oladi.",
                "examples": ["<ruby>看護師<rt>かんごし</rt></ruby>になるために<ruby>勉強<rt>べんきょう</rt></ruby>しています。",
                             "<ruby>健康<rt>けんこう</rt></ruby>のために<ruby>走<rt>はし</rt></ruby>っています。"],
            },
            {
                "pattern":  "Potensial / inkor + ように",
                "meaning":  "«…sin deb». Maqsad gapiruvchining "
                            "irodasidan tashqarida: qobiliyat, inkor "
                            "yoki boshqa odamning ishi.",
                "examples": ["<ruby>読<rt>よ</rt></ruby>めるように<ruby>漢字<rt>かんじ</rt></ruby>を<ruby>書<rt>か</rt></ruby>いています。",
                             "<ruby>忘<rt>わす</rt></ruby>れないように<ruby>書<rt>か</rt></ruby>きます。"],
            },
            {
                "pattern":  "〜ようにしています",
                "meaning":  "«…ishga harakat qilaman» — shunchaki odat "
                            "emas, ongli saʼy-harakat.",
                "examples": ["<ruby>毎日<rt>まいにち</rt></ruby><ruby>三十分<rt>さんじゅっぷん</rt></ruby><ruby>読<rt>よ</rt></ruby>むようにしています。"],
            },
        ],
        "body": '''<p><ruby>学校<rt>がっこう</rt></ruby>の<ruby>新聞<rt>しんぶん</rt></ruby>のために、<ruby>三人<rt>さんにん</rt></ruby>に<span class="cn-word" data-tr="intervyu">インタビュー</span>をした。<ruby>質問<rt>しつもん</rt></ruby>は<ruby>一<rt>ひと</rt></ruby>つだった。「<ruby>何<rt>なん</rt></ruby>のために<ruby>勉強<rt>べんきょう</rt></ruby>していますか。」</p>

<p><strong>パリ:</strong> わたしは<ruby>病院<rt>びょういん</rt></ruby>で<span class="cn-word" data-tr="ishlash uchun"><ruby>働<rt>はたら</rt></ruby>くために</span><ruby>勉強<rt>べんきょう</rt></ruby>しています。<ruby>母<rt>はは</rt></ruby>も<ruby>看護師<rt>かんごし</rt></ruby>です。</p>

<p><strong>イノム:</strong> ぼくは<ruby>日本語<rt>にほんご</rt></ruby>の<ruby>新聞<rt>しんぶん</rt></ruby>が<ruby>読<rt>よ</rt></ruby>めるように、<ruby>漢字<rt>かんじ</rt></ruby>を<ruby>毎日<rt>まいにち</rt></ruby><ruby>書<rt>か</rt></ruby>いています。まだ<ruby>難<rt>むずか</rt></ruby>しいです。</p>

<p><strong>ムニラ:</strong> <ruby>正直<rt>しょうじき</rt></ruby>に<ruby>言<rt>い</rt></ruby>うと、<ruby>分<rt>わ</rt></ruby>かりません。でも<ruby>忘<rt>わす</rt></ruby>れないように、<ruby>毎日<rt>まいにち</rt></ruby><ruby>少<rt>すこ</rt></ruby>し<ruby>読<rt>よ</rt></ruby>むようにしています。</p>

<p><ruby>三<rt>みっ</rt></ruby>つの<ruby>答<rt>こた</rt></ruby>えは<ruby>違<rt>ちが</rt></ruby>った。でも<span class="cn-word" data-tr="bir joyi oʻxshash edi"><ruby>一<rt>ひと</rt></ruby>つ<ruby>同<rt>おな</rt></ruby>じだった</span>。<ruby>三人<rt>さんにん</rt></ruby>とも<ruby>毎日<rt>まいにち</rt></ruby><ruby>何<rt>なに</rt></ruby>かをしていた。</p>

<p>パリさんの<ruby>目的<rt>もくてき</rt></ruby>は<ruby>遠<rt>とお</rt></ruby>い。<ruby>病院<rt>びょういん</rt></ruby>で<ruby>働<rt>はたら</rt></ruby>くまで<ruby>六年<rt>ろくねん</rt></ruby>ある。イノムさんの<ruby>目的<rt>もくてき</rt></ruby>は<ruby>近<rt>ちか</rt></ruby>い。<ruby>新聞<rt>しんぶん</rt></ruby>の<ruby>一<rt>いち</rt></ruby>ページでいい。</p>

<p>ムニラさんには<span class="cn-word" data-tr="maqsad"><ruby>目的<rt>もくてき</rt></ruby></span>がなかった。でも<ruby>習慣<rt>しゅうかん</rt></ruby>があった。</p>

<p><ruby>先生<rt>せんせい</rt></ruby>にこの<ruby>記事<rt>きじ</rt></ruby>を<ruby>見<rt>み</rt></ruby>せた。<ruby>先生<rt>せんせい</rt></ruby>は<ruby>三<rt>みっ</rt></ruby>つ<ruby>目<rt>め</rt></ruby>の<ruby>答<rt>こた</rt></ruby>えを<ruby>指<rt>ゆび</rt></ruby>で<ruby>指<rt>さ</rt></ruby>した。</p>

<p><strong>せんせい:</strong> <ruby>目的<rt>もくてき</rt></ruby>がある<ruby>人<rt>ひと</rt></ruby>は<ruby>強<rt>つよ</rt></ruby>いです。でも<ruby>習慣<rt>しゅうかん</rt></ruby>がある<ruby>人<rt>ひと</rt></ruby>は<ruby>遠<rt>とお</rt></ruby>くまで<ruby>行<rt>い</rt></ruby>きます。</p>''',
        "questions": [
            {
                "text": "パリさんはなぜ<ruby>勉強<rt>べんきょう</rt></ruby>していますか。",
                "choices": [
                    "Hamshira boʻlish uchun — onasi kasalxonada ishlaydi",
                    "Yaponcha gazeta oʻqiy olish uchun",
                    "Unutmaslik uchun",
                    "Oʻqituvchi soʻraganidan",
                ],
                "answer": 0,
                "explanation": "<strong>看護師になるために</strong> — hamshira "
                               "boʻlish Pari tanlaydigan yoʻl, demak "
                               "boshqarib boʻladigan maqsad: ために.",
            },
            {
                "text": "イノムさんはなぜ ために emas, ように<ruby>使<rt>つか</rt></ruby>いましたか。",
                "choices": [
                    "Chunki «oʻqiy olish» — qobiliyat, qaror emas",
                    "Chunki u kanji yozadi",
                    "Chunki gazeta yaponcha",
                    "Chunki u hali yosh",
                ],
                "answer": 0,
                "explanation": "<strong>読めるように</strong> — potensial shakl. "
                               "Siz «ertaga oʻqiy oladigan boʻlaman» deb "
                               "qaror qila olmaysiz; siz faqat mashq "
                               "qilasiz. Oʻzbekchada ham «oʻqiy "
                               "olishim uchun».",
            },
            {
                "text": "<ruby>先生<rt>せんせい</rt></ruby>は<ruby>何<rt>なに</rt></ruby>と<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "Maqsadi bor odam kuchli, lekin odati bor odam uzoqqa boradi",
                    "Maqsadsiz oʻqish foydasiz",
                    "Uch javob ham notoʻgʻri",
                    "Hamshira boʻlish eng yaxshi yoʻl",
                ],
                "answer": 0,
                "explanation": "Oʻqituvchi uchinchi javobni — Muniraning "
                               "<strong>毎日少し読むようにしています</strong> "
                               "degan gapini — koʻrsatdi. 〜ようにしています "
                               "shunchaki odat emas, ongli saʼy-harakat.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "はなせる ように なった",
        "summary": (
            "PJ-57 matni. Bir yil oldin Rano bir ogʻiz ham gapira "
            "olmasdi. Matn boshdan-oyoq なる ustida yuradi — va "
            "oxirida ことになりました chiqadi."
        ),
        "order":   57,
        "grammar": [
            {
                "pattern":  "〜ようになる",
                "meaning":  "«…adigan boʻlmoq». Qobiliyat yoki odat "
                            "oʻzgardi: ilgari yoʻq edi, endi bor.",
                "examples": ["<ruby>話<rt>はな</rt></ruby>せるようになった。",
                             "<ruby>野菜<rt>やさい</rt></ruby>を<ruby>食<rt>た</rt></ruby>べるようになった。"],
            },
            {
                "pattern":  "い-sifat <b>く</b> · ot <b>に</b> + なる",
                "meaning":  "なる ga ulanish uch xil: sifat く ga "
                            "tushadi, ot に oladi, feʼl ように orqali "
                            "ulanadi.",
                "examples": ["<ruby>楽<rt>たの</rt></ruby>しくなった。", "<ruby>先生<rt>せんせい</rt></ruby>になる。"],
            },
            {
                "pattern":  "〜ことにする / 〜ことになる",
                "meaning":  "する — men qaror qildim; なる — shunday "
                            "boʻlib qoldi. Yaponcha kamtarlik ikkinchisini "
                            "tanlaydi.",
                "examples": ["<ruby>続<rt>つづ</rt></ruby>けることにした。",
                             "<ruby>行<rt>い</rt></ruby>くことになりました。"],
            },
        ],
        "body": '''<p><ruby>一年前<rt>いちねんまえ</rt></ruby>、ラノさんは<ruby>日本語<rt>にほんご</rt></ruby>で<ruby>一言<rt>ひとこと</rt></ruby>も<ruby>話<rt>はな</rt></ruby>せなかった。<span class="cn-word" data-tr="hatto salomlashish ham">あいさつも</span><ruby>難<rt>むずか</rt></ruby>しかった。</p>

<p><ruby>最初<rt>さいしょ</rt></ruby>の<ruby>一<rt>いっ</rt></ruby>か<ruby>月<rt>げつ</rt></ruby>、ひらがなを<ruby>覚<rt>おぼ</rt></ruby>えた。<ruby>三<rt>さん</rt></ruby>か<ruby>月<rt>げつ</rt></ruby>で<ruby>短<rt>みじか</rt></ruby>い<ruby>文<rt>ぶん</rt></ruby>が<ruby>読<rt>よ</rt></ruby>めるようになった。<ruby>半年<rt>はんとし</rt></ruby>で<ruby>店<rt>みせ</rt></ruby>で<ruby>買<rt>か</rt></ruby>い<ruby>物<rt>もの</rt></ruby>ができるようになった。</p>

<p><ruby>途中<rt>とちゅう</rt></ruby>で<span class="cn-word" data-tr="qiyin payt"><ruby>辛<rt>つら</rt></ruby>い<ruby>時期<rt>じき</rt></ruby></span>があった。<ruby>漢字<rt>かんじ</rt></ruby>が<ruby>多<rt>おお</rt></ruby>くなった。<ruby>教科書<rt>きょうかしょ</rt></ruby>が<ruby>厚<rt>あつ</rt></ruby>くなった。ラノさんは<ruby>一度<rt>いちど</rt></ruby>やめたいと<ruby>思<rt>おも</rt></ruby>った。でも<ruby>毎晩<rt>まいばん</rt></ruby><ruby>十五分<rt>じゅうごふん</rt></ruby>、<ruby>続<rt>つづ</rt></ruby>けることにした。</p>

<p><ruby>少<rt>すこ</rt></ruby>しずつ<ruby>変<rt>か</rt></ruby>わった。アニメが<ruby>字幕<rt>じまく</rt></ruby>なしで<ruby>分<rt>わ</rt></ruby>かるようになった。<ruby>日本語<rt>にほんご</rt></ruby>の<ruby>歌<rt>うた</rt></ruby>が<ruby>好<rt>す</rt></ruby>きになった。<ruby>勉強<rt>べんきょう</rt></ruby>が<ruby>楽<rt>たの</rt></ruby>しくなった。</p>

<p><ruby>先週<rt>せんしゅう</rt></ruby>、<ruby>学校<rt>がっこう</rt></ruby>に<ruby>日本<rt>にほん</rt></ruby>から<ruby>先生<rt>せんせい</rt></ruby>が<ruby>来<rt>き</rt></ruby>た。ラノさんは<ruby>十分間<rt>じゅっぷんかん</rt></ruby><ruby>話<rt>はな</rt></ruby>した。<ruby>一度<rt>いちど</rt></ruby>も<ruby>英語<rt>えいご</rt></ruby>を<ruby>使<rt>つか</rt></ruby>わなかった。</p>

<p><strong>せんせい:</strong> どのぐらい<ruby>勉強<rt>べんきょう</rt></ruby>しましたか。</p>

<p><strong>ラノ:</strong> <ruby>一年<rt>いちねん</rt></ruby>です。<ruby>毎晩<rt>まいばん</rt></ruby><ruby>十五分<rt>じゅうごふん</rt></ruby>です。</p>

<p><ruby>先生<rt>せんせい</rt></ruby>は<ruby>驚<rt>おどろ</rt></ruby>いた。そして<ruby>一<rt>ひと</rt></ruby>つ<ruby>提案<rt>ていあん</rt></ruby>をした。</p>

<p><ruby>来年<rt>らいねん</rt></ruby>の<ruby>夏<rt>なつ</rt></ruby>、ラノさんは<ruby>日本<rt>にほん</rt></ruby>の<ruby>高校<rt>こうこう</rt></ruby>へ<span class="cn-word" data-tr="borishi hal boʻldi"><ruby>行<rt>い</rt></ruby>くことになった</span>。ラノさんは<ruby>今<rt>いま</rt></ruby>も<ruby>毎晩<rt>まいばん</rt></ruby><ruby>十五分<rt>じゅうごふん</rt></ruby><ruby>勉強<rt>べんきょう</rt></ruby>している。</p>''',
        "questions": [
            {
                "text": "ラノさんは<ruby>半年<rt>はんとし</rt></ruby>で<ruby>何<rt>なに</rt></ruby>ができるようになりましたか。",
                "choices": [
                    "Doʻkonda xarid qila oladigan boʻldi",
                    "Anime tarjimasiz tushunadigan boʻldi",
                    "Yaponiyaga bordi",
                    "Hiraganani yodladi",
                ],
                "answer": 0,
                "explanation": "<strong>半年で店で買い物ができるようになった。</strong> "
                               "〜ようになる — qobiliyat oʻzgarishi: ilgari "
                               "yoʻq edi, endi bor.",
            },
            {
                "text": "«<ruby>教科書<rt>きょうかしょ</rt></ruby>が<ruby>厚<rt>あつ</rt></ruby>くなった» — nega bu yerda く?",
                "choices": [
                    "Chunki 厚い い-sifat, va い-sifat なる oldida く ga tushadi",
                    "Chunki 教科書 ot",
                    "Chunki gap oʻtgan zamonda",
                    "Chunki bu qobiliyat",
                ],
                "answer": 0,
                "explanation": "なる ga ulanish uch xil: い-sifat "
                               "<strong>く</strong> (厚くなった), ot va "
                               "な-sifat <strong>に</strong> (好きになった), "
                               "feʼl <strong>ように</strong> (分かるように "
                               "なった). Uchalasi ham shu matnda bor.",
            },
            {
                "text": "«<ruby>続<rt>つづ</rt></ruby>けることにした» va «<ruby>行<rt>い</rt></ruby>くことになった» — farqi nima?",
                "choices": [
                    "Birinchisini Rano oʻzi hal qildi, ikkinchisi esa shunday boʻlib qoldi",
                    "Birinchisi kelasi zamon, ikkinchisi oʻtgan",
                    "Birinchisi rasmiy, ikkinchisi oddiy",
                    "Farqi yoʻq",
                ],
                "answer": 0,
                "explanation": "する = men qaror qildim; なる = shunday "
                               "boʻldi. Maktabga borish taklifni "
                               "oʻqituvchi qildi — shuning uchun "
                               "<strong>ことになった</strong>. Yaponchada "
                               "qarorni oʻzingiz qilgan boʻlsangiz ham "
                               "koʻpincha shunday aytiladi.",
            },
        ],
    },
]
