# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-61 … PJ-63.

Hikoyachi 普通体 da (PJ-45 dan beri), qoʻshtirnoq ichi です・ます ni
saqlaydi.

Shakl navbati: 61 — yaxshilik zanjiri hikoyasi, 62 — kichik tergov
(xulosa chiqarish), 63 — shahar yangiliklari (byulleten shakli).
Oldingi batchda falokat / tayyorgarlik / odat hikoyasi boʻlgan edi.

⚠️ CUMULATIVE: 61 da でしょう/かもしれ/はず yoʻq va passiv yoʻq;
62 da passiv yoʻq. 63 dagi passiv faqat TOʻGʻRI passiv (直接受身) —
«aziyat passivi» PJ-64 da.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_61_63.py --author=prime
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
        "title":   "てつだって くれた",
        "summary": (
            "PJ-61 matni. Bir kunda uchta yaxshilik bir-biriga ulanadi "
            "— va matn boshdan-oyoq 〜てくれる, 〜てあげる, 〜てもらう "
            "ustida yuradi."
        ),
        "order":   61,
        "grammar": [
            {
                "pattern":  "て-shakli + くれる",
                "meaning":  "«Menga qilib berdi». Yaxshilik ichkariga "
                            "kelganda doim くれる.",
                "examples": ["<ruby>荷物<rt>にもつ</rt></ruby>を<ruby>持<rt>も</rt></ruby>ってくれた。"],
            },
            {
                "pattern":  "て-shakli + あげる / もらう",
                "meaning":  "あげる — mendan chiqadi; もらう — men "
                            "olaman (ega — men).",
                "examples": ["<ruby>弟<rt>おとうと</rt></ruby>を<ruby>手伝<rt>てつだ</rt></ruby>ってあげた。",
                             "<ruby>教<rt>おし</rt></ruby>えてもらった。"],
            },
            {
                "pattern":  "〜てくれてありがとう",
                "meaning":  "Yaponchada rahmat aytganda nima uchun "
                            "ekanini feʼl bilan koʻrsatish odat.",
                "examples": ["<ruby>手伝<rt>てつだ</rt></ruby>ってくれてありがとう。"],
            },
        ],
        "body": '''<p><ruby>火曜日<rt>かようび</rt></ruby>の<ruby>朝<rt>あさ</rt></ruby>、パリさんは<ruby>大<rt>おお</rt></ruby>きい<span class="cn-word" data-tr="yuk"><ruby>荷物<rt>にもつ</rt></ruby></span>を<ruby>持<rt>も</rt></ruby>っていた。<ruby>文化祭<rt>ぶんかさい</rt></ruby>の<ruby>道具<rt>どうぐ</rt></ruby>だった。<ruby>階段<rt>かいだん</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>で<ruby>止<rt>と</rt></ruby>まった。</p>

<p><ruby>知<rt>し</rt></ruby>らない<ruby>男<rt>おとこ</rt></ruby>の<ruby>子<rt>こ</rt></ruby>が<ruby>半分<rt>はんぶん</rt></ruby><ruby>持<rt>も</rt></ruby>ってくれた。<ruby>三階<rt>さんがい</rt></ruby>まで<ruby>一緒<rt>いっしょ</rt></ruby>に<ruby>上<rt>あ</rt></ruby>がった。</p>

<p><strong>パリ:</strong> <ruby>手伝<rt>てつだ</rt></ruby>ってくれてありがとうございます。</p>

<p><strong>おとこのこ:</strong> いいえ。<ruby>僕<rt>ぼく</rt></ruby>も<ruby>去年<rt>きょねん</rt></ruby><span class="cn-word" data-tr="shu yerda"><ruby>同<rt>おな</rt></ruby>じ<ruby>場所<rt>ばしょ</rt></ruby></span>で<ruby>手伝<rt>てつだ</rt></ruby>ってもらいました。</p>

<p><ruby>昼<rt>ひる</rt></ruby>、パリさんは<ruby>教室<rt>きょうしつ</rt></ruby>でイノムさんに<ruby>会<rt>あ</rt></ruby>った。イノムさんは<ruby>数学<rt>すうがく</rt></ruby>の<ruby>問題<rt>もんだい</rt></ruby>で<ruby>困<rt>こま</rt></ruby>っていた。パリさんは<ruby>三十分<rt>さんじゅっぷん</rt></ruby><ruby>教<rt>おし</rt></ruby>えてあげた。</p>

<p><ruby>放課後<rt>ほうかご</rt></ruby>、イノムさんは<ruby>弟<rt>おとうと</rt></ruby>を<ruby>手伝<rt>てつだ</rt></ruby>ってあげた。<ruby>弟<rt>おとうと</rt></ruby>は<ruby>自転車<rt>じてんしゃ</rt></ruby>が<span class="cn-word" data-tr="mindirib boʻlmasdi"><ruby>乗<rt>の</rt></ruby>れなかった</span>。</p>

<p><ruby>夜<rt>よる</rt></ruby>、パリさんは<ruby>日記<rt>にっき</rt></ruby>を<ruby>書<rt>か</rt></ruby>いた。</p>

<p>「<ruby>今日<rt>きょう</rt></ruby>、<ruby>知<rt>し</rt></ruby>らない<ruby>人<rt>ひと</rt></ruby>に<ruby>手伝<rt>てつだ</rt></ruby>ってもらいました。<ruby>私<rt>わたし</rt></ruby>もイノムさんに<ruby>教<rt>おし</rt></ruby>えてあげました。<ruby>三<rt>みっ</rt></ruby>つ<ruby>目<rt>め</rt></ruby>は<ruby>知<rt>し</rt></ruby>りません。でも、きっとあると<ruby>思<rt>おも</rt></ruby>います。」</p>

<p><span class="cn-word" data-tr="uchinchisi"><ruby>三<rt>みっ</rt></ruby>つ<ruby>目<rt>め</rt></ruby></span>はあった。イノムさんの<ruby>弟<rt>おとうと</rt></ruby>が、<ruby>次<rt>つぎ</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>、<ruby>公園<rt>こうえん</rt></ruby>で<ruby>小<rt>ちい</rt></ruby>さい<ruby>女<rt>おんな</rt></ruby>の<ruby>子<rt>こ</rt></ruby>に<ruby>自転車<rt>じてんしゃ</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えてあげた。</p>''',
        "questions": [
            {
                "text": "<ruby>男<rt>おとこ</rt></ruby>の<ruby>子<rt>こ</rt></ruby>はなぜパリさんを<ruby>手伝<rt>てつだ</rt></ruby>いましたか。",
                "choices": [
                    "Oʻtgan yili oʻsha joyda unga ham yordam berishgan edi",
                    "Pari uning sinfdoshi edi",
                    "Oʻqituvchi soʻragan edi",
                    "Yuk juda ogʻir edi",
                ],
                "answer": 0,
                "explanation": "<strong>去年同じ場所で手伝ってもらいました。</strong> "
                               "もらう — ega oʻzi, yaʼni «menga yordam "
                               "berishdi».",
            },
            {
                "text": "«<ruby>持<rt>も</rt></ruby>ってくれた» va «<ruby>教<rt>おし</rt></ruby>えてあげた» — nega ikki xil feʼl?",
                "choices": [
                    "Birinchisida yaxshilik Pariga kelyapti, ikkinchisida undan chiqyapti",
                    "Birinchisi oʻtgan, ikkinchisi hozirgi zamon",
                    "Birinchisi rasmiy, ikkinchisi oddiy",
                    "Birinchisi narsa, ikkinchisi ish uchun",
                ],
                "answer": 0,
                "explanation": "Yoʻnalish <strong>feʼlning ichida</strong>. "
                               "Oʻzbekcha «-ib bermoq» qurilmasi bir xil, "
                               "faqat yaponchada «bermoq» ikkiga boʻlingan: "
                               "くれる va あげる.",
            },
            {
                "text": "<ruby>日記<rt>にっき</rt></ruby>の「<ruby>三<rt>みっ</rt></ruby>つ<ruby>目<rt>め</rt></ruby>」とは<ruby>何<rt>なに</rt></ruby>ですか。",
                "choices": [
                    "Uchinchi yaxshilik — Inomning ukasi boshqa bolaga velosiped oʻrgatgani",
                    "Uchinchi kun",
                    "Uchinchi qavat",
                    "Uchinchi masala",
                ],
                "answer": 0,
                "explanation": "Pari ikkitasini bilardi: unga yordam "
                               "berishdi, u Inomga oʻrgatdi. Uchinchisi "
                               "uning koʻzidan tashqarida sodir boʻldi — "
                               "zanjir davom etdi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "かさは どこでしょう",
        "summary": (
            "PJ-62 matni. Munira soyabonini yoʻqotadi va uchtasi "
            "birga xulosa chiqaradi — かもしれません, でしょう va "
            "はずです bitta suhbatda uch xil ishonchni koʻrsatadi."
        ),
        "order":   62,
        "grammar": [
            {
                "pattern":  "〜かもしれません",
                "meaning":  "Eng past daraja: gapiruvchi bilmaydi va "
                            "shuni ochiq aytadi.",
                "examples": ["<ruby>教室<rt>きょうしつ</rt></ruby>にあるかもしれません。"],
            },
            {
                "pattern":  "〜でしょう",
                "meaning":  "Oʻrtacha-yuqori daraja: ishonaman, lekin "
                            "kafolat bermayman. Ohang koʻtarilsa — "
                            "tasdiq soʻrash.",
                "examples": ["だれかが<ruby>持<rt>も</rt></ruby>っていったでしょう。"],
            },
            {
                "pattern":  "〜はずです",
                "meaning":  "Mantiqiy kutish: dalil bor. はず — OT, "
                            "shuning uchun undan oldin な / の.",
                "examples": ["<ruby>図書館<rt>としょかん</rt></ruby>にあるはずです。",
                             "<ruby>青<rt>あお</rt></ruby>いはずです。"],
            },
        ],
        "body": '''<p><ruby>金曜日<rt>きんようび</rt></ruby>の<ruby>放課後<rt>ほうかご</rt></ruby>、ムニラさんのかさがなかった。<ruby>朝<rt>あさ</rt></ruby>は<ruby>雨<rt>あめ</rt></ruby>だった。<ruby>今<rt>いま</rt></ruby>も<ruby>降<rt>ふ</rt></ruby>っている。</p>

<p><strong>ムニラ:</strong> どこでしょう。<ruby>朝<rt>あさ</rt></ruby>から<ruby>三<rt>みっ</rt></ruby>つの<ruby>場所<rt>ばしょ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きました。</p>

<p><strong>ラノ:</strong> <ruby>教室<rt>きょうしつ</rt></ruby>にあるかもしれません。<ruby>見<rt>み</rt></ruby>ましたか。</p>

<p><strong>ムニラ:</strong> <ruby>見<rt>み</rt></ruby>ました。ありませんでした。</p>

<p>イノムさんは<span class="cn-word" data-tr="bir oz oʻylab turdi"><ruby>少<rt>すこ</rt></ruby>し<ruby>考<rt>かんが</rt></ruby>えた</span>。そして<ruby>三<rt>みっ</rt></ruby>つの<ruby>質問<rt>しつもん</rt></ruby>をした。</p>

<p><strong>イノム:</strong> <ruby>朝<rt>あさ</rt></ruby>、どこで<ruby>雨<rt>あめ</rt></ruby>が<ruby>止<rt>や</rt></ruby>みましたか。</p>

<p><strong>ムニラ:</strong> <ruby>図書館<rt>としょかん</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>です。</p>

<p><strong>イノム:</strong> じゃ、<ruby>図書館<rt>としょかん</rt></ruby>にあるはずです。<ruby>雨<rt>あめ</rt></ruby>が<ruby>止<rt>や</rt></ruby>んだら、<ruby>人<rt>ひと</rt></ruby>はかさを<span class="cn-word" data-tr="qoʻyib qoʻyadi"><ruby>置<rt>お</rt></ruby>きます</span>。</p>

<p><ruby>三人<rt>さんにん</rt></ruby>は<ruby>図書館<rt>としょかん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>った。<span class="cn-word" data-tr="soyabon qoʻyadigan joy">かさ<ruby>立<rt>た</rt></ruby>て</span>に<ruby>六<rt>むっ</rt></ruby>つあった。</p>

<p><strong>ラノ:</strong> どれでしょう。<ruby>全部<rt>ぜんぶ</rt></ruby><ruby>黒<rt>くろ</rt></ruby>いです。</p>

<p><strong>ムニラ:</strong> <ruby>私<rt>わたし</rt></ruby>のかさは<ruby>青<rt>あお</rt></ruby>いはずです。<ruby>去年<rt>きょねん</rt></ruby><ruby>母<rt>はは</rt></ruby>と<ruby>買<rt>か</rt></ruby>いました。</p>

<p><ruby>一番下<rt>いちばんした</rt></ruby>に<ruby>青<rt>あお</rt></ruby>いかさがあった。<ruby>柄<rt>え</rt></ruby>に<ruby>小<rt>ちい</rt></ruby>さい<ruby>名前<rt>なまえ</rt></ruby>があった。</p>

<p><strong>イノム:</strong> <ruby>雨<rt>あめ</rt></ruby>が<ruby>止<rt>や</rt></ruby>んだ<ruby>場所<rt>ばしょ</rt></ruby>を<ruby>思<rt>おも</rt></ruby>い<ruby>出<rt>だ</rt></ruby>したら、かさは<ruby>見<rt>み</rt></ruby>つかります。いつも<ruby>見<rt>み</rt></ruby>つかります。</p>''',
        "questions": [
            {
                "text": "ラノさんの「<ruby>教室<rt>きょうしつ</rt></ruby>にあるかもしれません」 — bu qanday daraja?",
                "choices": [
                    "Eng past — hech qanday dalil yoʻq, shunchaki ehtimol",
                    "Eng yuqori — aniq dalil bor",
                    "Oʻrtacha — odatda shunday boʻladi",
                    "Bu umuman taxmin emas",
                ],
                "answer": 0,
                "explanation": "<strong>かもしれません</strong> — ~50%. "
                               "Rano shunchaki bir joyni taklif qilyapti, "
                               "hech nimaga asoslanmayapti.",
            },
            {
                "text": "イノムさんはなぜ「<ruby>図書館<rt>としょかん</rt></ruby>にあるはずです」と<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "Chunki dalil bor: yomgʻir kutubxona oldida toʻxtagan",
                    "Chunki kutubxonani yaxshi koʻradi",
                    "Chunki Munira shunday dedi",
                    "Chunki soyabon koʻk edi",
                ],
                "answer": 0,
                "explanation": "はず — <strong>mantiqiy kutish</strong>: "
                               "dalil bor va undan xulosa chiqarilyapti. "
                               "Shuning uchun Inom avval uchta savol berdi.",
            },
            {
                "text": "«<ruby>私<rt>わたし</rt></ruby>のは<ruby>青<rt>あお</rt></ruby>いはずです» — nega bu yerda はず, でしょう emas?",
                "choices": [
                    "Chunki Munira soyabonni oʻzi sotib olgan — bu aniq dalil",
                    "Chunki 青い い-sifat",
                    "Chunki gap oʻtgan zamonda",
                    "Chunki u ishonchsiz",
                ],
                "answer": 0,
                "explanation": "«Nega shunday deb oʻylaysiz?» degan savolga "
                               "aniq javob bor — oʻtgan yili onasi bilan "
                               "sotib olgan. Dalil bor, demak "
                               "<strong>はず</strong>.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "まちの ニュース",
        "summary": (
            "PJ-63 matni — shahar byulleteni, uchta qisqa xabar. "
            "Yangiliklar passivning oʻz janri: kim qilgani emas, "
            "nima boʻlgani muhim."
        ),
        "order":   63,
        "grammar": [
            {
                "pattern":  "ない-oʻzak + れる / られる",
                "meaning":  "Passiv. I guruh あ-qatorga tushadi + れる, "
                            "II guruh る → られる.",
                "examples": ["<ruby>建<rt>た</rt></ruby>てられた。", "<ruby>選<rt>えら</rt></ruby>ばれた。"],
            },
            {
                "pattern":  "Qiluvchi に oladi",
                "meaning":  "Yaponchada passiv gapda kim qilgani に "
                            "bilan aytiladi, va bu butunlay tabiiy.",
                "examples": ["<ruby>子<rt>こ</rt></ruby>どもたちに<ruby>選<rt>えら</rt></ruby>ばれた。"],
            },
            {
                "pattern":  "Kim qilgani muhim boʻlmaganda",
                "meaning":  "Yangiliklar va ilmiy matnlar passiv bilan "
                            "yoziladi — xuddi oʻzbekchadagi kabi.",
                "examples": ["<ruby>今年<rt>ことし</rt></ruby>の<ruby>夏<rt>なつ</rt></ruby>に<ruby>行<rt>おこな</rt></ruby>われる。"],
            },
        ],
        "body": '''<p><ruby>今週<rt>こんしゅう</rt></ruby>の<ruby>町<rt>まち</rt></ruby>のニュース。</p>

<p><ruby>一<rt>ひと</rt></ruby>つ<ruby>目<rt>め</rt></ruby>。<ruby>駅<rt>えき</rt></ruby>の<ruby>近<rt>ちか</rt></ruby>くに<ruby>新<rt>あたら</rt></ruby>しい<ruby>図書館<rt>としょかん</rt></ruby>が<ruby>建<rt>た</rt></ruby>てられた。<ruby>二年<rt>にねん</rt></ruby>かかった。<ruby>中<rt>なか</rt></ruby>に<ruby>子<rt>こ</rt></ruby>どもの<ruby>部屋<rt>へや</rt></ruby>がある。<ruby>日本語<rt>にほんご</rt></ruby>の<ruby>本<rt>ほん</rt></ruby>が<ruby>三万冊<rt>さんまんさつ</rt></ruby><ruby>置<rt>お</rt></ruby>かれている。</p>

<p><ruby>二<rt>ふた</rt></ruby>つ<ruby>目<rt>め</rt></ruby>。<ruby>先週<rt>せんしゅう</rt></ruby>いなくなった<span class="cn-word" data-tr="mushuk"><ruby>猫<rt>ねこ</rt></ruby></span>が<ruby>発見<rt>はっけん</rt></ruby>された。<ruby>名前<rt>なまえ</rt></ruby>はミケだ。<ruby>公園<rt>こうえん</rt></ruby>の<span class="cn-word" data-tr="skameyka">ベンチ</span>の<ruby>下<rt>した</rt></ruby>にいた。<ruby>高校生<rt>こうこうせい</rt></ruby>に<ruby>見<rt>み</rt></ruby>つけられた。<ruby>元気<rt>げんき</rt></ruby>だ。</p>

<p><ruby>三<rt>みっ</rt></ruby>つ<ruby>目<rt>め</rt></ruby>。<ruby>夏<rt>なつ</rt></ruby>の<span class="cn-word" data-tr="bayram"><ruby>祭<rt>まつ</rt></ruby>り</span>の<ruby>日<rt>ひ</rt></ruby>が<ruby>決<rt>き</rt></ruby>められた。<ruby>八月<rt>はちがつ</rt></ruby><ruby>十日<rt>とおか</rt></ruby>だ。<ruby>今年<rt>ことし</rt></ruby>の<ruby>歌<rt>うた</rt></ruby>は<ruby>小学校<rt>しょうがっこう</rt></ruby>の<ruby>子<rt>こ</rt></ruby>どもたちに<ruby>選<rt>えら</rt></ruby>ばれた。</p>

<p>この<ruby>祭<rt>まつ</rt></ruby>りは<ruby>三百年前<rt>さんびゃくねんまえ</rt></ruby>から<ruby>行<rt>おこな</rt></ruby>われている。<ruby>昔<rt>むかし</rt></ruby>は<ruby>川<rt>かわ</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>で<ruby>行<rt>おこな</rt></ruby>われた。<ruby>今<rt>いま</rt></ruby>は<ruby>駅<rt>えき</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>の<ruby>広場<rt>ひろば</rt></ruby>で<ruby>行<rt>おこな</rt></ruby>われる。</p>

<p><ruby>四<rt>よっ</rt></ruby>つ<ruby>目<rt>め</rt></ruby>。<ruby>駅<rt>えき</rt></ruby>の<ruby>南口<rt>みなみぐち</rt></ruby>の<span class="cn-word" data-tr="koʻprik"><ruby>橋<rt>はし</rt></ruby></span>が<ruby>来月<rt>らいげつ</rt></ruby>から<ruby>直<rt>なお</rt></ruby>される。<ruby>工事<rt>こうじ</rt></ruby>は<ruby>三<rt>さん</rt></ruby>か<ruby>月<rt>げつ</rt></ruby>かかる。その<ruby>間<rt>あいだ</rt></ruby>は<ruby>北口<rt>きたぐち</rt></ruby>が<ruby>使<rt>つか</rt></ruby>われる。<ruby>学校<rt>がっこう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>く<ruby>道<rt>みち</rt></ruby>も<ruby>変<rt>か</rt></ruby>わる。</p>

<p><span class="cn-word" data-tr="oxirgi xabar"><ruby>最後<rt>さいご</rt></ruby>に<ruby>一<rt>ひと</rt></ruby>つ</span>。<ruby>図書館<rt>としょかん</rt></ruby>の<ruby>名前<rt>なまえ</rt></ruby>はまだ<ruby>決<rt>き</rt></ruby>まっていない。<ruby>町<rt>まち</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>から<ruby>名前<rt>なまえ</rt></ruby>を<span class="cn-word" data-tr="toʻplayapti"><ruby>集<rt>あつ</rt></ruby>めている</span>。<ruby>来月<rt>らいげつ</rt></ruby><ruby>一<rt>ひと</rt></ruby>つ<ruby>選<rt>えら</rt></ruby>ばれる。</p>''',
        "questions": [
            {
                "text": "<ruby>新<rt>あたら</rt></ruby>しい<ruby>図書館<rt>としょかん</rt></ruby>について<ruby>何<rt>なに</rt></ruby>が<ruby>分<rt>わ</rt></ruby>かりますか。",
                "choices": [
                    "Bekat yaqinida qurilgan va ichida 30 000 kitob bor",
                    "Oʻtgan oyda ochilgan",
                    "Nomi allaqachon tanlangan",
                    "Ikki qavatli",
                ],
                "answer": 0,
                "explanation": "<strong>建てられました</strong> va "
                               "<strong>置かれています</strong> — ikkalasi "
                               "ham passiv. Kim qurgani muhim emas: "
                               "yangiliklar janri shunday.",
            },
            {
                "text": "«<ruby>高校生<rt>こうこうせい</rt></ruby>に<ruby>見<rt>み</rt></ruby>つけられました» — に nimani koʻrsatyapti?",
                "choices": [
                    "Kim topganini — qiluvchini",
                    "Qayerda topilganini",
                    "Qachon topilganini",
                    "Nima uchun topilganini",
                ],
                "answer": 0,
                "explanation": "Passiv gapda qiluvchi <strong>に</strong> "
                               "oladi. Oʻzbekchada «oʻquvchi tomonidan "
                               "topildi» sunʼiy eshitiladi — shuning uchun "
                               "buni oddiy gap bilan tarjima qilish "
                               "toʻgʻriroq: «maktab oʻquvchisi topdi».",
            },
            {
                "text": "<ruby>祭<rt>まつ</rt></ruby>りの<ruby>歌<rt>うた</rt></ruby>はだれが<ruby>選<rt>えら</rt></ruby>びましたか。",
                "choices": [
                    "Boshlangʻich maktab bolalari",
                    "Shahar hokimiyati",
                    "Kutubxona xodimlari",
                    "Hali tanlanmagan",
                ],
                "answer": 0,
                "explanation": "<strong>子どもたちに選ばれました</strong> — "
                               "passiv, qiluvchi に bilan. Matn oxirida esa "
                               "kutubxona nomi haqida <strong>選ばれます</strong> "
                               "— hali tanlanmagan, kelasi zamon.",
            },
        ],
    },
]
