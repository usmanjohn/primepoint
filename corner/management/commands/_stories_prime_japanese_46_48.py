# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-46 … PJ-48.

Hikoyachi 普通体 da gapiradi (PJ-45 dan boshlangan qoida), qoʻshtirnoq
ichidagi nutq esa です・ます ni saqlaydi.

Shakl navbati: 46 — kundalik hayot hikoyasi, 47 — masal (Ezop),
48 — maktabdagi kichik qidiruv. Uchtasi uch xil.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_46_48.py --author=prime
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
        "title":   "ムニラさんは おこっていると おもった",
        "summary": (
            "PJ-46 matni. Ikki kun davomida hikoyachi Munira undan "
            "xafa deb oʻylaydi — va butun matn 〜と思った ustiga "
            "qurilgan. Sabab esa umuman boshqa narsa chiqadi."
        ),
        "order":   46,
        "grammar": [
            {
                "pattern":  "<ruby>普通体<rt>ふつうたい</rt></ruby> + と<ruby>思<rt>おも</rt></ruby>う",
                "meaning":  "«…deb oʻylayman». と — oʻzbekcha «deb». Undan "
                            "oldin doim oddiy shakl turadi.",
                "examples": ["<ruby>怒<rt>おこ</rt></ruby>っていると<ruby>思<rt>おも</rt></ruby>った。",
                             "<ruby>来<rt>こ</rt></ruby>ないと<ruby>思<rt>おも</rt></ruby>った。"],
            },
            {
                "pattern":  "Ot va な-sifat + <b>だ</b> + と",
                "meaning":  "と dan oldin だ tushmaydi. い-sifat esa だ "
                            "olmaydi.",
                "examples": ["<ruby>元気<rt>げんき</rt></ruby>だと<ruby>思<rt>おも</rt></ruby>った。",
                             "<ruby>忙<rt>いそが</rt></ruby>しいと<ruby>思<rt>おも</rt></ruby>った。"],
            },
            {
                "pattern":  "Boshqa odam — <ruby>思<rt>おも</rt></ruby>っている",
                "meaning":  "Birovning fikri haqida gapirilsa, ている "
                            "shakli ishlatiladi: siz uning holatini "
                            "koʻrasiz, ichidagi ovozini emas.",
                "examples": ["ムニラさんも<ruby>同<rt>おな</rt></ruby>じことを<ruby>思<rt>おも</rt></ruby>っていた。"],
            },
        ],
        "body": '''<p><ruby>月曜日<rt>げつようび</rt></ruby>、ムニラさんは<ruby>教室<rt>きょうしつ</rt></ruby>で<ruby>私<rt>わたし</rt></ruby>に<ruby>何<rt>なに</rt></ruby>も<ruby>言<rt>い</rt></ruby>わなかった。<ruby>目<rt>め</rt></ruby>も<ruby>合<rt>あ</rt></ruby>わなかった。</p>

<p><ruby>私<rt>わたし</rt></ruby>は<span class="cn-word" data-tr="jahli chiqqan"><ruby>怒<rt>おこ</rt></ruby>っている</span>と<ruby>思<rt>おも</rt></ruby>った。<ruby>先週<rt>せんしゅう</rt></ruby>の<ruby>試験<rt>しけん</rt></ruby>のことだと<ruby>思<rt>おも</rt></ruby>った。<ruby>私<rt>わたし</rt></ruby>のほうが<ruby>点<rt>てん</rt></ruby>がよかった。それが<ruby>原因<rt>げんいん</rt></ruby>だと<ruby>思<rt>おも</rt></ruby>った。</p>

<p><ruby>火曜日<rt>かようび</rt></ruby>も<ruby>同<rt>おな</rt></ruby>じだった。ムニラさんは<ruby>昼<rt>ひる</rt></ruby>ごはんを<ruby>一人<rt>ひとり</rt></ruby>で<ruby>食<rt>た</rt></ruby>べた。<span class="cn-word" data-tr="endi">もう</span><ruby>話<rt>はな</rt></ruby>さないと<ruby>思<rt>おも</rt></ruby>った。</p>

<p><ruby>水曜日<rt>すいようび</rt></ruby>の<ruby>朝<rt>あさ</rt></ruby>、ラノさんに<ruby>聞<rt>き</rt></ruby>いた。</p>

<p><strong>ラノ:</strong> ムニラさんはおばあさんの<ruby>病院<rt>びょういん</rt></ruby>に<ruby>行<rt>い</rt></ruby>っています。<ruby>毎日<rt>まいにち</rt></ruby>です。とても<ruby>忙<rt>いそが</rt></ruby>しいと<ruby>言<rt>い</rt></ruby>っていました。</p>

<p><ruby>私<rt>わたし</rt></ruby>は<span class="cn-word" data-tr="uyaldim"><ruby>恥<rt>は</rt></ruby>ずかしかった</span>。でも、それは<ruby>私<rt>わたし</rt></ruby>の<span class="cn-word" data-tr="xato"><ruby>間違<rt>まちが</rt></ruby>い</span>だった。</p>

<p>その<ruby>日<rt>ひ</rt></ruby>の<ruby>午後<rt>ごご</rt></ruby>、<ruby>私<rt>わたし</rt></ruby>はムニラさんの<ruby>机<rt>つくえ</rt></ruby>に<ruby>小<rt>ちい</rt></ruby>さい<ruby>手紙<rt>てがみ</rt></ruby>を<ruby>置<rt>お</rt></ruby>いた。「<ruby>大丈夫<rt>だいじょうぶ</rt></ruby>ですか。<ruby>手伝<rt>てつだ</rt></ruby>いたいです。」</p>

<p><ruby>次<rt>つぎ</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>、ムニラさんは<ruby>笑<rt>わら</rt></ruby>った。そして<ruby>言<rt>い</rt></ruby>った。</p>

<p><strong>ムニラ:</strong> ありがとう。わたしも<ruby>同<rt>おな</rt></ruby>じことを<ruby>思<rt>おも</rt></ruby>っていました。あなたが<ruby>怒<rt>おこ</rt></ruby>っていると<ruby>思<rt>おも</rt></ruby>っていました。</p>''',
        "questions": [
            {
                "text": "<ruby>私<rt>わたし</rt></ruby>はなぜムニラさんが<ruby>怒<rt>おこ</rt></ruby>っていると<ruby>思<rt>おも</rt></ruby>いましたか。",
                "choices": [
                    "Chunki Munira u bilan gaplashmadi va koʻziga ham qaramadi",
                    "Chunki Munira unga xat yozdi",
                    "Chunki Munira kasalxonaga ketdi",
                    "Chunki Munira imtihondan yuqori ball oldi",
                ],
                "answer": 0,
                "explanation": "Dushanba kuni Munira hech nima demadi va "
                               "koʻz ham urishtirmadi. Hikoyachi buni "
                               "jahl deb tushundi — lekin bu faqat "
                               "<strong>uning taxmini</strong> edi, fakt emas. "
                               "Butun matn shu farq ustiga qurilgan.",
            },
            {
                "text": "ムニラさんは<ruby>本当<rt>ほんとう</rt></ruby>は<ruby>何<rt>なに</rt></ruby>をしていましたか。",
                "choices": [
                    "Har kuni buvisining oldiga kasalxonaga borardi",
                    "Imtihonga tayyorlanardi",
                    "Boshqa maktabga oʻtmoqchi edi",
                    "Ranoga xat yozardi",
                ],
                "answer": 0,
                "explanation": "Rano shuni aytadi: おばあさんの病院に行っています。"
                               "毎日です。 Munira jahl qilgani yoʻq edi — "
                               "shunchaki <strong>忙しかった</strong>.",
            },
            {
                "text": "«わたしも<ruby>同<rt>おな</rt></ruby>じことを<ruby>思<rt>おも</rt></ruby>っていました» — nega bu yerda <ruby>思<rt>おも</rt></ruby>っていました?",
                "choices": [
                    "Chunki bu ancha vaqtdan beri davom etgan fikr",
                    "Chunki bu boshqa odamning fikri",
                    "Chunki 思う II guruh feʼli",
                    "Chunki gap qoʻshtirnoq ichida",
                ],
                "answer": 0,
                "explanation": "ています davom etayotgan holatni koʻrsatadi "
                               "(PJ-31). Munira bu fikrda <strong>bir necha "
                               "kun turgan edi</strong>, shuning uchun "
                               "思いました emas, 思っていました. Shu shakl "
                               "boshqa odamning fikri haqida gapirilganda "
                               "ham ishlatiladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "きたかぜと たいよう",
        "summary": (
            "PJ-47 matni — Ezopning mashhur masali. Butun hikoya "
            "«…と言った» ustida yuradi, va PJ-44 dagi より / のほうが "
            "ham qaytib keladi."
        ),
        "order":   47,
        "grammar": [
            {
                "pattern":  "「…」と<ruby>言<rt>い</rt></ruby>った",
                "meaning":  "Koʻchirma gap: odamning soʻzi aynan "
                            "qaytariladi va uning oʻz uslubi saqlanadi.",
                "examples": ["「わたしのほうが<ruby>強<rt>つよ</rt></ruby>いです」と<ruby>言<rt>い</rt></ruby>った。"],
            },
            {
                "pattern":  "<ruby>普通体<rt>ふつうたい</rt></ruby> + と<ruby>言<rt>い</rt></ruby>った",
                "meaning":  "Oʻzlashtirilgan gap: 「」 yoʻq, mazmuni "
                            "qaytariladi, oldida oddiy shakl turadi.",
                "examples": ["それができるほうが<ruby>強<rt>つよ</rt></ruby>いと<ruby>言<rt>い</rt></ruby>った。"],
            },
            {
                "pattern":  "Zamon siljimaydi",
                "meaning":  "Qoʻshtirnoq ichidagi zamon aytilgan paytga "
                            "qarab oʻlchanadi — oʻzbekchadagidek.",
                "examples": ["「<ruby>今<rt>いま</rt></ruby>からやります」と<ruby>言<rt>い</rt></ruby>った。"],
            },
        ],
        "body": '''<p><ruby>昔<rt>むかし</rt></ruby>、<span class="cn-word" data-tr="shimol shamoli"><ruby>北風<rt>きたかぜ</rt></ruby></span>と<span class="cn-word" data-tr="quyosh"><ruby>太陽<rt>たいよう</rt></ruby></span>が<ruby>話<rt>はな</rt></ruby>していた。ふたりは<ruby>自分<rt>じぶん</rt></ruby>のほうが<ruby>強<rt>つよ</rt></ruby>いと<ruby>思<rt>おも</rt></ruby>っていた。</p>

<p><strong>きたかぜ:</strong> わたしのほうがあなたより<ruby>強<rt>つよ</rt></ruby>いです。</p>

<p><strong>たいよう:</strong> わたしはそう<ruby>思<rt>おも</rt></ruby>いません。<span class="cn-word" data-tr="sinab koʻraylik"><ruby>試<rt>ため</rt></ruby>しましょう</span>。</p>

<p>その<ruby>日<rt>ひ</rt></ruby>、<ruby>道<rt>みち</rt></ruby>を<span class="cn-word" data-tr="sayohatchi"><ruby>旅人<rt>たびびと</rt></ruby></span>が<ruby>歩<rt>ある</rt></ruby>いていた。あたたかい<span class="cn-word" data-tr="ustki kiyim"><ruby>上着<rt>うわぎ</rt></ruby></span>を<ruby>着<rt>き</rt></ruby>ていた。<ruby>太陽<rt>たいよう</rt></ruby>は「<ruby>旅人<rt>たびびと</rt></ruby>が<ruby>上着<rt>うわぎ</rt></ruby>を<ruby>脱<rt>ぬ</rt></ruby>ぎます。それができるほうが<ruby>強<rt>つよ</rt></ruby>いです」と<ruby>言<rt>い</rt></ruby>った。</p>

<p><ruby>北風<rt>きたかぜ</rt></ruby>は「<ruby>簡単<rt>かんたん</rt></ruby>です」と<ruby>言<rt>い</rt></ruby>った。そして<ruby>強<rt>つよ</rt></ruby>く<ruby>吹<rt>ふ</rt></ruby>いた。<ruby>旅人<rt>たびびと</rt></ruby>は<ruby>寒<rt>さむ</rt></ruby>かった。そして<ruby>上着<rt>うわぎ</rt></ruby>を<span class="cn-word" data-tr="mahkam ushladi"><ruby>強<rt>つよ</rt></ruby>く<ruby>持<rt>も</rt></ruby>った</span>。<ruby>北風<rt>きたかぜ</rt></ruby>はもっと<ruby>強<rt>つよ</rt></ruby>く<ruby>吹<rt>ふ</rt></ruby>いた。<ruby>旅人<rt>たびびと</rt></ruby>は<ruby>上着<rt>うわぎ</rt></ruby>を<ruby>脱<rt>ぬ</rt></ruby>がなかった。</p>

<p><ruby>北風<rt>きたかぜ</rt></ruby>は<ruby>疲<rt>つか</rt></ruby>れた。そして「もうできません」と<ruby>言<rt>い</rt></ruby>った。</p>

<p><ruby>次<rt>つぎ</rt></ruby>は<ruby>太陽<rt>たいよう</rt></ruby>だった。<ruby>太陽<rt>たいよう</rt></ruby>は<ruby>何<rt>なに</rt></ruby>も<ruby>言<rt>い</rt></ruby>わなかった。<span class="cn-word" data-tr="ohista">しずかに</span><ruby>光<rt>ひか</rt></ruby>った。<ruby>道<rt>みち</rt></ruby>があたたかかった。<ruby>旅人<rt>たびびと</rt></ruby>は<ruby>暑<rt>あつ</rt></ruby>いと<ruby>思<rt>おも</rt></ruby>った。そして<ruby>自分<rt>じぶん</rt></ruby>で<ruby>上着<rt>うわぎ</rt></ruby>を<ruby>脱<rt>ぬ</rt></ruby>いだ。</p>

<p><strong>たいよう:</strong> <ruby>風<rt>かぜ</rt></ruby>より<ruby>光<rt>ひかり</rt></ruby>のほうが<ruby>強<rt>つよ</rt></ruby>いですね。</p>

<p>この<ruby>話<rt>はなし</rt></ruby>は<ruby>二千年<rt>にせんねん</rt></ruby>ぐらい<ruby>前<rt>まえ</rt></ruby>にギリシャの<span class="cn-word" data-tr="Ezop">イソップ</span>が<ruby>作<rt>つく</rt></ruby>った。</p>''',
        "questions": [
            {
                "text": "<ruby>北風<rt>きたかぜ</rt></ruby>と<ruby>太陽<rt>たいよう</rt></ruby>は<ruby>何<rt>なに</rt></ruby>を<ruby>試<rt>ため</rt></ruby>しましたか。",
                "choices": [
                    "Sayohatchi ustki kiyimini yechsin — buni kim uddalay olishini",
                    "Kim tezroq yugurishini",
                    "Kim balandroq ovoz chiqarishini",
                    "Kim uzoqroq shamol esdira olishini",
                ],
                "answer": 0,
                "explanation": "太陽 aytadi: 旅人が上着を脱ぐ。それができるほうが強い。 "
                               "Bu — oʻzlashtirilgan gap: 「」 yoʻq, oldida "
                               "<strong>oddiy shakl</strong> turibdi.",
            },
            {
                "text": "«<ruby>簡単<rt>かんたん</rt></ruby>です» — nega bu gap <ruby>丁寧体<rt>ていねいたい</rt></ruby> da?",
                "choices": [
                    "Chunki bu 「」 ichidagi koʻchirma gap — odamning oʻz uslubi saqlanadi",
                    "Chunki 簡単 な-sifat",
                    "Chunki hikoyachi ham 丁寧体 da gapiradi",
                    "Chunki bu savol",
                ],
                "answer": 0,
                "explanation": "Hikoyachi butun matnda oddiy shaklda gapiradi "
                               "(吹いた, 脱いだ), lekin <strong>「」 ichi "
                               "tegilmaydi</strong>. Koʻchirma gapda siz "
                               "hech narsani tuzatmaysiz.",
            },
            {
                "text": "なぜ<ruby>旅人<rt>たびびと</rt></ruby>は<ruby>上着<rt>うわぎ</rt></ruby>を<ruby>脱<rt>ぬ</rt></ruby>ぎましたか。",
                "choices": [
                    "Chunki issiq boʻlib ketdi va oʻzi yechdi",
                    "Chunki shamol uni yechirdi",
                    "Chunki quyosh undan soʻradi",
                    "Chunki u uyiga yetib keldi",
                ],
                "answer": 0,
                "explanation": "太陽 hech nima demadi — shunchaki yoritdi. "
                               "旅人は暑いと<strong>思った</strong>, keyin "
                               "自分で 脱いだ. Masalning maʼnosi shu: "
                               "kuch emas, iliqlik ishni bitirdi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "わすれものの はこ",
        "summary": (
            "PJ-48 matni. Pari yoʻqotgan daftarini qidiradi va matn "
            "boshdan-oyoq aniqlovchi ergash gaplardan tuzilgan: "
            "«kecha yozgan daftar», «oʻqituvchi olib kelgan quti»."
        ),
        "order":   48,
        "grammar": [
            {
                "pattern":  "GAP (<ruby>普通体<rt>ふつうたい</rt></ruby>) + OT",
                "meaning":  "Aniqlovchi ergash gap otdan oldin turadi — "
                            "oʻzbekchadagi «men yozgan daftar» bilan bir "
                            "xil tartib. Bogʻlovchi soʻz ham, vergul ham "
                            "yoʻq.",
                "examples": ["<ruby>昨日<rt>きのう</rt></ruby><ruby>書<rt>か</rt></ruby>いたノート",
                             "<ruby>先生<rt>せんせい</rt></ruby>が<ruby>持<rt>も</rt></ruby>ってきた<ruby>箱<rt>はこ</rt></ruby>"],
            },
            {
                "pattern":  "Ichkaridagi ega — <b>が</b>",
                "meaning":  "Ergash gap ichida は turolmaydi: は butun "
                            "gapning mavzusini koʻrsatadi, ergash gapda "
                            "esa mavzu boʻlmaydi.",
                "examples": ["パリさんが<ruby>探<rt>さが</rt></ruby>していたノート"],
            },
            {
                "pattern":  "Otdan oldin だ → な / の",
                "meaning":  "と oldida だ saqlanadi, ot oldida esa u な "
                            "(な-sifat) yoki の (ot) boʻlib qoladi.",
                "examples": ["<ruby>大切<rt>たいせつ</rt></ruby>なノート",
                             "<ruby>日本語<rt>にほんご</rt></ruby>の<ruby>先生<rt>せんせい</rt></ruby>"],
            },
        ],
        "body": '''<p><ruby>金曜日<rt>きんようび</rt></ruby>の<ruby>放課後<rt>ほうかご</rt></ruby>、パリさんはノートをなくした。<ruby>昨日<rt>きのう</rt></ruby>の<ruby>夜<rt>よる</rt></ruby>ずっと<ruby>書<rt>か</rt></ruby>いたノートだった。<ruby>月曜日<rt>げつようび</rt></ruby>に<ruby>出<rt>だ</rt></ruby>す<span class="cn-word" data-tr="insho"><ruby>作文<rt>さくぶん</rt></ruby></span>がその<ruby>中<rt>なか</rt></ruby>にあった。</p>

<p>パリさんは<ruby>教室<rt>きょうしつ</rt></ruby>を<ruby>探<rt>さが</rt></ruby>した。<ruby>自分<rt>じぶん</rt></ruby>が<ruby>座<rt>すわ</rt></ruby>った<ruby>席<rt>せき</rt></ruby>も、<ruby>昼<rt>ひる</rt></ruby>ごはんを<ruby>食<rt>た</rt></ruby>べた<ruby>場所<rt>ばしょ</rt></ruby>も<ruby>見<rt>み</rt></ruby>た。ノートはなかった。</p>

<p><span class="cn-word" data-tr="topilgan buyumlar"><ruby>忘<rt>わす</rt></ruby>れ<ruby>物<rt>もの</rt></ruby></span>の<ruby>箱<rt>はこ</rt></ruby>が<ruby>職員室<rt>しょくいんしつ</rt></ruby>にあると<ruby>思<rt>おも</rt></ruby>った。<ruby>私<rt>わたし</rt></ruby>は「<ruby>職員室<rt>しょくいんしつ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きましょう」と<ruby>言<rt>い</rt></ruby>った。</p>

<p><ruby>職員室<rt>しょくいんしつ</rt></ruby>で<ruby>先生<rt>せんせい</rt></ruby>が<ruby>大<rt>おお</rt></ruby>きい<ruby>箱<rt>はこ</rt></ruby>を<ruby>持<rt>も</rt></ruby>ってきた。<ruby>中<rt>なか</rt></ruby>にはたくさんの<ruby>物<rt>もの</rt></ruby>があった。<ruby>名前<rt>なまえ</rt></ruby>がない<span class="cn-word" data-tr="soatlar"><ruby>時計<rt>とけい</rt></ruby></span>、<ruby>去年<rt>きょねん</rt></ruby>から<span class="cn-word" data-tr="hech kim olmagan"><ruby>誰<rt>だれ</rt></ruby>も<ruby>取<rt>と</rt></ruby>らなかった</span>かさ、<ruby>片方<rt>かたほう</rt></ruby>の<span class="cn-word" data-tr="qoʻlqoplar">てぶくろ</span>。</p>

<p><strong>せんせい:</strong> ここにある<ruby>物<rt>もの</rt></ruby>は<ruby>全部<rt>ぜんぶ</rt></ruby><ruby>誰<rt>だれ</rt></ruby>かの<ruby>大切<rt>たいせつ</rt></ruby>な<ruby>物<rt>もの</rt></ruby>でした。でも<ruby>探<rt>さが</rt></ruby>しに<ruby>来<rt>く</rt></ruby>る<ruby>人<rt>ひと</rt></ruby>は<ruby>少<rt>すく</rt></ruby>ないです。</p>

<p>パリさんが<ruby>探<rt>さが</rt></ruby>していたノートは<ruby>箱<rt>はこ</rt></ruby>の<ruby>一番<rt>いちばん</rt></ruby><ruby>下<rt>した</rt></ruby>にあった。<ruby>表紙<rt>ひょうし</rt></ruby>に<ruby>書<rt>か</rt></ruby>いた<ruby>名前<rt>なまえ</rt></ruby>がまだ<ruby>読<rt>よ</rt></ruby>めた。</p>

<p><strong>パリ:</strong> ありがとうございます。とてもうれしいです。</p>

<p><ruby>帰<rt>かえ</rt></ruby>る<ruby>道<rt>みち</rt></ruby>で、パリさんは<ruby>小<rt>ちい</rt></ruby>さい<ruby>声<rt>こえ</rt></ruby>で<ruby>今度<rt>こんど</rt></ruby>から<ruby>全部<rt>ぜんぶ</rt></ruby>の<ruby>物<rt>もの</rt></ruby>に<ruby>名前<rt>なまえ</rt></ruby>を<ruby>書<rt>か</rt></ruby>くと<ruby>言<rt>い</rt></ruby>った。</p>''',
        "questions": [
            {
                "text": "パリさんがなくしたノートはどんなノートでしたか。",
                "choices": [
                    "Kecha kechqurun uzoq vaqt yozgan, ichida inshosi bor daftar",
                    "Oʻqituvchi bergan yangi daftar",
                    "Kutubxonadan olgan daftar",
                    "Ranodan qarzga olgan daftar",
                ],
                "answer": 0,
                "explanation": "昨日の夜ずっと<strong>書いた</strong>ノート — "
                               "aniqlovchi ergash gap. Uni oxiridan oʻqing: "
                               "ノート → 書いた → 昨日の夜ずっと.",
            },
            {
                "text": "「パリさんが<ruby>探<rt>さが</rt></ruby>していたノート」 — nega bu yerda が, は emas?",
                "choices": [
                    "Chunki bu ergash gapning ichi, u yerda は turolmaydi",
                    "Chunki パリさん — yangi personaj",
                    "Chunki gap oʻtgan zamonda",
                    "Chunki ノート — toʻldiruvchi",
                ],
                "answer": 0,
                "explanation": "は <strong>butun gapning</strong> mavzusini "
                               "koʻrsatadi (PJ-14). Aniqlovchi ergash gapda "
                               "mavzu boʻlmaydi — faqat ega bor, ega esa "
                               "<strong>が</strong> oladi.",
            },
            {
                "text": "<ruby>先生<rt>せんせい</rt></ruby>は<ruby>箱<rt>はこ</rt></ruby>について<ruby>何<rt>なに</rt></ruby>と<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "Ichidagi narsalarning hammasi kimningdir qadrli buyumi edi, lekin qidirib keladigan odam kam",
                    "Quti har oy toʻliq boʻshatiladi",
                    "Faqat daftarlar saqlanadi",
                    "Yoʻqolgan buyumlar boshqa maktabga yuboriladi",
                ],
                "answer": 0,
                "explanation": "«<ruby>大切<rt>たいせつ</rt></ruby>な<ruby>物<rt>もの</rt></ruby>» "
                               "— otdan oldin な-sifat <strong>な</strong> "
                               "kiyadi. «探しに来る人» ham aniqlovchi ergash "
                               "gap: «qidirib keladigan odam».",
            },
        ],
    },
]
