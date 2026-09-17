# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-85 … PJ-87.

Uzunlik Blok F tasmasida (190–270 soʻz).

Shakl navbati: 85 — 昔話 (xalq ertagini qayta aytish), 86 — ilmiy-ommabop
matn, 87 — yangilik xabari. Oldingi batchda kundalik / xat / kulgili
hikoya boʻlgan edi.

Registr: uchalasi ham 普通体 (PJ-45 dan beri hikoyachi shunday gapiradi).
87-matndagi館長ning gapi — quoted speech, oʻz registrini saqlaydi.

⚠️ CUMULATIVE:
    85 — うちに / あいだに erkin. につれて・にしたがって (PJ-86) va
         によって (PJ-87) YOʻQ.
    86 — + につれて va にしたがって. によって hali YOʻQ — shuning uchun
         «haroratga qarab» degan joyда にしたがって va で ishlatilgan.
    87 — hammasi erkin.

⚠️ 86-matndagi faktlar rost: 桜前線 — havo maʼlumotida ishlatiladigan
haqiqiy atama; gullash mart oxirida Kyushu dan boshlanib may da
Hokkaido ga yetadi; balandlik oshgan sari harorat tushadi; shahar
markazi atrofdagi qishloqdan issiqroq. 87-matn esa ataylab uydirma
shaharcha haqida — haqiqiy joy yoki odam nomi yoʻq.

⚠️ 〜のです bu shelfda yozilmaydi: kurs uni bermagan, va u 〜んです ning
yozma egizagi. Gate 〜んです ni tutadi, のです ni esa qoʻlda kuzatish
kerak.

Audio (navbat bilan, oldingi batch 84 da Nanami bilan tugagan edi):
    --only 85 --voice ja-JP-KeitaNeural
    --only 86 --voice ja-JP-NanamiNeural
    --only 87 --voice ja-JP-KeitaNeural

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_85_87.py --author=prime
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
        "title":   "あかるいうちに",
        "summary": (
            "PJ-85 matni. Togʻ etagidagi qishloqda bitta qoida bor edi: "
            "dovondan yorugʻida oʻtish kerak. Bir yigit doʻstlari bilan "
            "gaplashib turib vaqtni unutadi — va qorongʻida yoʻlni "
            "yoʻqotadi. Eski ertak shaklidagi matn."
        ),
        "order":   85,
        "grammar": [
            {
                "pattern":  "〜うちに · 〜ないうちに",
                "meaning":  "«… ekan, kech boʻlmasdan». Oyna oʻz-oʻzidan "
                            "yopiladi: yorugʻlik ketadi, ovqat sovuydi, "
                            "yoshlik oʻtadi. Inkor bilan — «… boʻlmasdan "
                            "oldin».",
                "examples": ["<ruby>明<rt>あか</rt></ruby>るいうちに<ruby>越<rt>こ</rt></ruby>えろ。",
                             "<ruby>暗<rt>くら</rt></ruby>くならないうちに<ruby>帰<rt>かえ</rt></ruby>る。"],
            },
            {
                "pattern":  "〜ているうちに",
                "meaning":  "«… qilib turib» — ish qilib turganda "
                            "sezilmagan holda boshqa narsa oʻzgarib "
                            "qoladi. Keyingi gapda koʻpincha 〜てしまう "
                            "yoki 〜なる keladi.",
                "examples": ["<ruby>話<rt>はな</rt></ruby>しているうちに、<ruby>時間<rt>じかん</rt></ruby>を<ruby>忘<rt>わす</rt></ruby>れてしまった。"],
            },
            {
                "pattern":  "〜あいだに",
                "meaning":  "«… davomida bir payt». Chegarasi aniq "
                            "oraliqning ichidagi bitta nuqta. に "
                            "boʻlmasa — butun oraliq.",
                "examples": ["<ruby>寝<rt>ね</rt></ruby>ているあいだに、<ruby>朝<rt>あさ</rt></ruby>になった。"],
            },
        ],
        "body": '''<p>むかし、ある<ruby>山<rt>やま</rt></ruby>のふもとに<ruby>小<rt>ちい</rt></ruby>さな<ruby>村<rt>むら</rt></ruby>があった。<ruby>村<rt>むら</rt></ruby>から<ruby>町<rt>まち</rt></ruby>へ<ruby>行<rt>い</rt></ruby>くには、<ruby>一<rt>ひと</rt></ruby>つの<span class="cn-word" data-tr="togʻ dovoni"><ruby>峠<rt>とうげ</rt></ruby></span>を<ruby>越<rt>こ</rt></ruby>えなければならなかった。</p>

<p>その<ruby>峠<rt>とうげ</rt></ruby>には、<ruby>古<rt>ふる</rt></ruby>い<span class="cn-word" data-tr="rivoyat, eski gap"><ruby>言<rt>い</rt></ruby>い<ruby>伝<rt>つた</rt></ruby>え</span>があった。「<ruby>明<rt>あか</rt></ruby>るいうちに<ruby>越<rt>こ</rt></ruby>えろ。」</p>

<p>ある<ruby>秋<rt>あき</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>、<ruby>若<rt>わか</rt></ruby>い<ruby>男<rt>おとこ</rt></ruby>が<ruby>町<rt>まち</rt></ruby>へ<ruby>買<rt>か</rt></ruby>い<ruby>物<rt>もの</rt></ruby>に<ruby>行<rt>い</rt></ruby>った。<ruby>友<rt>とも</rt></ruby>だちと<ruby>話<rt>はな</rt></ruby>しているうちに、<ruby>時間<rt>じかん</rt></ruby>を<ruby>忘<rt>わす</rt></ruby>れてしまった。</p>

<p><ruby>外<rt>そと</rt></ruby>に<ruby>出<rt>で</rt></ruby>ると、<ruby>空<rt>そら</rt></ruby>はもう<ruby>赤<rt>あか</rt></ruby>かった。<ruby>暗<rt>くら</rt></ruby>くならないうちに<ruby>峠<rt>とうげ</rt></ruby>を<ruby>越<rt>こ</rt></ruby>えなければならない。<ruby>男<rt>おとこ</rt></ruby>は<ruby>急<rt>いそ</rt></ruby>いだ。</p>

<p>しかし、<ruby>坂<rt>さか</rt></ruby>を<ruby>登<rt>のぼ</rt></ruby>っているうちに、<ruby>日<rt>ひ</rt></ruby>が<span class="cn-word" data-tr="botdi"><ruby>沈<rt>しず</rt></ruby>んだ</span>。まわりは<span class="cn-word" data-tr="zim-ziyo"><ruby>真<rt>ま</rt></ruby>っ<ruby>暗<rt>くら</rt></ruby></span>になった。<ruby>男<rt>おとこ</rt></ruby>は<ruby>道<rt>みち</rt></ruby>が<ruby>分<rt>わ</rt></ruby>からなくなった。</p>

<p>そのとき、<ruby>遠<rt>とお</rt></ruby>くに<ruby>小<rt>ちい</rt></ruby>さな<span class="cn-word" data-tr="chiroq nuri"><ruby>明<rt>あ</rt></ruby>かり</span>が<ruby>見<rt>み</rt></ruby>えた。<ruby>近<rt>ちか</rt></ruby>づくと、<ruby>一人<rt>ひとり</rt></ruby>のおばあさんが<ruby>立<rt>た</rt></ruby>っていた。</p>

<p><strong>おばあさん:</strong> <ruby>明<rt>あか</rt></ruby>るいうちに<ruby>来<rt>き</rt></ruby>ませんでしたね。<ruby>今夜<rt>こんや</rt></ruby>はうちで<ruby>休<rt>やす</rt></ruby>みなさい。</p>

<p>おばあさんは<ruby>男<rt>おとこ</rt></ruby>を<ruby>自分<rt>じぶん</rt></ruby>の<ruby>家<rt>いえ</rt></ruby>へ<ruby>連<rt>つ</rt></ruby>れて<ruby>行<rt>い</rt></ruby>った。<ruby>男<rt>おとこ</rt></ruby>はそこで<ruby>一晩<rt>ひとばん</rt></ruby><ruby>休<rt>やす</rt></ruby>んだ。</p>

<p><ruby>男<rt>おとこ</rt></ruby>が<ruby>寝<rt>ね</rt></ruby>ているあいだに、<ruby>朝<rt>あさ</rt></ruby>になった。<ruby>目<rt>め</rt></ruby>が<ruby>覚<rt>さ</rt></ruby>めると、<ruby>家<rt>いえ</rt></ruby>はなかった。<ruby>男<rt>おとこ</rt></ruby>は<span class="cn-word" data-tr="oʻt-oʻlan"><ruby>草<rt>くさ</rt></ruby></span>の<ruby>上<rt>うえ</rt></ruby>で<ruby>寝<rt>ね</rt></ruby>ていた。まわりは<ruby>明<rt>あか</rt></ruby>るく、<ruby>道<rt>みち</rt></ruby>がはっきり<ruby>見<rt>み</rt></ruby>えた。</p>

<p><ruby>男<rt>おとこ</rt></ruby>は<ruby>村<rt>むら</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>って、この<ruby>話<rt>はなし</rt></ruby>をした。それから<ruby>村<rt>むら</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>たちは、<ruby>子<rt>こ</rt></ruby>どもにこう<ruby>言<rt>い</rt></ruby>うようになった。「<ruby>明<rt>あか</rt></ruby>るいうちに<ruby>帰<rt>かえ</rt></ruby>れ。<ruby>暗<rt>くら</rt></ruby>くなってからでは、だれが<ruby>助<rt>たす</rt></ruby>けてくれるか<ruby>分<rt>わ</rt></ruby>からない。」</p>''',
        "questions": [
            {
                "text": "<ruby>男<rt>おとこ</rt></ruby>はどうして<ruby>時間<rt>じかん</rt></ruby>を<ruby>忘<rt>わす</rt></ruby>れましたか。",
                "choices": [
                    "<ruby>友<rt>とも</rt></ruby>だちと<ruby>話<rt>はな</rt></ruby>しているうちに<ruby>忘<rt>わす</rt></ruby>れた",
                    "<ruby>買<rt>か</rt></ruby>い<ruby>物<rt>もの</rt></ruby>が<ruby>多<rt>おお</rt></ruby>かったから",
                    "<ruby>時計<rt>とけい</rt></ruby>を<ruby>持<rt>も</rt></ruby>っていなかったから",
                    "<ruby>町<rt>まち</rt></ruby>で<ruby>寝<rt>ね</rt></ruby>てしまったから",
                ],
                "answer": 0,
                "explanation": "«話しているうちに、時間を忘れてしまった» "
                               "— 〜ているうちに aynan shu ishni qiladi: "
                               "ish qilib turganda sezilmagan holda "
                               "boshqa narsa oʻzgaradi.",
            },
            {
                "text": "<ruby>朝<rt>あさ</rt></ruby>、<ruby>男<rt>おとこ</rt></ruby>は<ruby>何<rt>なに</rt></ruby>を<ruby>見<rt>み</rt></ruby>ましたか。",
                "choices": [
                    "<ruby>家<rt>いえ</rt></ruby>はなく、<ruby>自分<rt>じぶん</rt></ruby>は<ruby>草<rt>くさ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>にいた",
                    "おばあさんが<ruby>朝<rt>あさ</rt></ruby>ごはんを<ruby>作<rt>つく</rt></ruby>っていた",
                    "<ruby>村<rt>むら</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>たちが<ruby>来<rt>き</rt></ruby>ていた",
                    "まだ<ruby>暗<rt>くら</rt></ruby>くて<ruby>何<rt>なに</rt></ruby>も<ruby>見<rt>み</rt></ruby>えなかった",
                ],
                "answer": 0,
                "explanation": "Uyqudan uygʻonganda uy ham, kampir ham "
                               "yoʻq edi — yigit oʻt ustida yotgan edi. "
                               "Ertak buni izohlamaydi, va aynan shu "
                               "uni ertak qiladi.",
            },
            {
                "text": "<ruby>村<rt>むら</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>たちは<ruby>子<rt>こ</rt></ruby>どもに<ruby>何<rt>なに</rt></ruby>と<ruby>言<rt>い</rt></ruby>うようになりましたか。",
                "choices": [
                    "<ruby>明<rt>あか</rt></ruby>るいうちに<ruby>帰<rt>かえ</rt></ruby>れ",
                    "<ruby>峠<rt>とうげ</rt></ruby>を<ruby>越<rt>こ</rt></ruby>えるな",
                    "おばあさんに<ruby>会<rt>あ</rt></ruby>うな",
                    "<ruby>町<rt>まち</rt></ruby>へ<ruby>行<rt>い</rt></ruby>くな",
                ],
                "answer": 0,
                "explanation": "Ertakning xulosasi taqiq emas — vaqt "
                               "haqidagi maslahat: «yorugʻida qayt». "
                               "Buyruq shakli 帰れ (PJ-67) maqolga "
                               "keskin ohang beradi.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "さくらが きたへ すすむ",
        "summary": (
            "PJ-86 matni. Yaponiyada bahor janubdan shimolga qarab "
            "sekin siljiydi, va bu harakatning oʻz nomi bor — «sakura "
            "fronti». Ilmiy-ommabop matn: harorat koʻtarilgan sari "
            "gullar ochiladi, balandlikka chiqqan sari kechikadi."
        ),
        "order":   86,
        "grammar": [
            {
                "pattern":  "<ruby>辞書形<rt>じしょけい</rt></ruby> / ot + につれて",
                "meaning":  "«… gan sari». Ikki narsa birga, sekin-asta "
                            "oʻzgaradi. Ikkala tomon ham oʻzgarish "
                            "boʻlishi shart.",
                "examples": ["<ruby>暖<rt>あたた</rt></ruby>かくなるにつれて、<ruby>花<rt>はな</rt></ruby>が<ruby>開<rt>ひら</rt></ruby>く。"],
            },
            {
                "pattern":  "<ruby>辞書形<rt>じしょけい</rt></ruby> / ot + にしたがって",
                "meaning":  "Ikki ishi bor: «… gan sari» (につれて bilan "
                            "bir xil) va «… ga muvofiq» (qoida, odat, "
                            "koʻrsatma bilan).",
                "examples": ["<ruby>高<rt>たか</rt></ruby>く<ruby>登<rt>のぼ</rt></ruby>るにしたがって、<ruby>気温<rt>きおん</rt></ruby>が<ruby>下<rt>さ</rt></ruby>がる。",
                             "<ruby>習慣<rt>しゅうかん</rt></ruby>にしたがって"],
            },
        ],
        "body": '''<p><ruby>日本<rt>にほん</rt></ruby>の<ruby>春<rt>はる</rt></ruby>は、<ruby>南<rt>みなみ</rt></ruby>から<ruby>北<rt>きた</rt></ruby>へゆっくり<ruby>動<rt>うご</rt></ruby>く。</p>

<p><ruby>三月<rt>さんがつ</rt></ruby>の<ruby>終<rt>お</rt></ruby>わりごろ、<ruby>九州<rt>きゅうしゅう</rt></ruby>で<ruby>桜<rt>さくら</rt></ruby>が<span class="cn-word" data-tr="ochiladi (gul)"><ruby>咲<rt>さ</rt></ruby>く</span>。それから<ruby>毎日<rt>まいにち</rt></ruby><ruby>少<rt>すこ</rt></ruby>しずつ、<ruby>花<rt>はな</rt></ruby>は<ruby>北<rt>きた</rt></ruby>へ<ruby>進<rt>すす</rt></ruby>む。<ruby>五月<rt>ごがつ</rt></ruby>になると、<ruby>北海道<rt>ほっかいどう</rt></ruby>でも<ruby>桜<rt>さくら</rt></ruby>が<ruby>見<rt>み</rt></ruby>られる。</p>

<p><ruby>日本人<rt>にほんじん</rt></ruby>はこの<ruby>動<rt>うご</rt></ruby>きを「<ruby>桜前線<rt>さくらぜんせん</rt></ruby>」と<ruby>呼<rt>よ</rt></ruby>ぶ。<ruby>天気予報<rt>てんきよほう</rt></ruby>でも、<ruby>毎年<rt>まいとし</rt></ruby>この<ruby>言葉<rt>ことば</rt></ruby>が<ruby>使<rt>つか</rt></ruby>われる。</p>

<p><ruby>桜<rt>さくら</rt></ruby>が<ruby>咲<rt>さ</rt></ruby>く<ruby>日<rt>ひ</rt></ruby>は、<span class="cn-word" data-tr="havo harorati"><ruby>気温<rt>きおん</rt></ruby></span>で<ruby>決<rt>き</rt></ruby>まる。<ruby>暖<rt>あたた</rt></ruby>かくなるにつれて、<ruby>花<rt>はな</rt></ruby>が<ruby>開<rt>ひら</rt></ruby>く。だから<ruby>南<rt>みなみ</rt></ruby>のほうが<ruby>早<rt>はや</rt></ruby>く、<ruby>北<rt>きた</rt></ruby>のほうが<ruby>遅<rt>おそ</rt></ruby>い。</p>

<p><ruby>山<rt>やま</rt></ruby>でも<ruby>同<rt>おな</rt></ruby>じことが<ruby>起<rt>お</rt></ruby>きる。<ruby>高<rt>たか</rt></ruby>く<ruby>登<rt>のぼ</rt></ruby>るにしたがって、<ruby>気温<rt>きおん</rt></ruby>が<ruby>下<rt>さ</rt></ruby>がる。そのため、<ruby>同<rt>おな</rt></ruby>じ<ruby>山<rt>やま</rt></ruby>でも、<ruby>下<rt>した</rt></ruby>の<ruby>桜<rt>さくら</rt></ruby>と<ruby>上<rt>うえ</rt></ruby>の<ruby>桜<rt>さくら</rt></ruby>は<ruby>同<rt>おな</rt></ruby>じ<ruby>日<rt>ひ</rt></ruby>に<ruby>咲<rt>さ</rt></ruby>かない。</p>

<p><ruby>最近<rt>さいきん</rt></ruby>、この<span class="cn-word" data-tr="front (meteorologiyada)"><ruby>前線<rt>ぜんせん</rt></ruby></span>の<ruby>動<rt>うご</rt></ruby>きが<ruby>少<rt>すこ</rt></ruby>しずつ<ruby>変<rt>か</rt></ruby>わってきた。<span class="cn-word" data-tr="shahar"><ruby>都市<rt>とし</rt></ruby></span>が<ruby>大<rt>おお</rt></ruby>きくなるにつれて、まちの<ruby>気温<rt>きおん</rt></ruby>が<ruby>上<rt>あ</rt></ruby>がる。そのため、<ruby>都会<rt>とかい</rt></ruby>の<ruby>桜<rt>さくら</rt></ruby>は、まわりの<span class="cn-word" data-tr="qishloq joy"><ruby>田舎<rt>いなか</rt></ruby></span>より<ruby>早<rt>はや</rt></ruby>く<ruby>咲<rt>さ</rt></ruby>くことがある。</p>

<p><ruby>桜<rt>さくら</rt></ruby>が<ruby>咲<rt>さ</rt></ruby>いてから<span class="cn-word" data-tr="toʻkilmoq"><ruby>散<rt>ち</rt></ruby>る</span>までは、だいたい<ruby>一週間<rt>いっしゅうかん</rt></ruby>から<ruby>十日<rt>とおか</rt></ruby>だ。<ruby>短<rt>みじか</rt></ruby>いあいだに、<ruby>日本中<rt>にほんじゅう</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>が<ruby>花<rt>はな</rt></ruby>を<ruby>見<rt>み</rt></ruby>に<ruby>行<rt>い</rt></ruby>く。</p>

<p>「<ruby>咲<rt>さ</rt></ruby>いた」と<ruby>決<rt>き</rt></ruby>めるしかたもおもしろい。<span class="cn-word" data-tr="meteorologiya stansiyasi"><ruby>気象台<rt>きしょうだい</rt></ruby></span>は、まちごとに<ruby>一本<rt>いっぽん</rt></ruby>の<ruby>木<rt>き</rt></ruby>を<ruby>選<rt>えら</rt></ruby>んでおく。その<ruby>木<rt>き</rt></ruby>に<ruby>五<rt>いつ</rt></ruby>つか<ruby>六<rt>むっ</rt></ruby>つの<ruby>花<rt>はな</rt></ruby>が<ruby>開<rt>ひら</rt></ruby>くと、「<span class="cn-word" data-tr="gullash (rasmiy eʼlon)"><ruby>開花<rt>かいか</rt></ruby></span>」と<ruby>発表<rt>はっぴょう</rt></ruby>される。<ruby>春<rt>はる</rt></ruby>が<ruby>北<rt>きた</rt></ruby>へ<ruby>進<rt>すす</rt></ruby>むにつれて、この<ruby>発表<rt>はっぴょう</rt></ruby>も<ruby>北<rt>きた</rt></ruby>へ<ruby>動<rt>うご</rt></ruby>いていく。</p>

<p><ruby>花見<rt>はなみ</rt></ruby>のしかたは、<ruby>地方<rt>ちほう</rt></ruby>の<ruby>習慣<rt>しゅうかん</rt></ruby>にしたがって<ruby>少<rt>すこ</rt></ruby>しずつ<ruby>違<rt>ちが</rt></ruby>う。<ruby>公園<rt>こうえん</rt></ruby>で<ruby>食<rt>た</rt></ruby>べる<ruby>人<rt>ひと</rt></ruby>もいれば、ただ<ruby>歩<rt>ある</rt></ruby>いて<ruby>見<rt>み</rt></ruby>るだけの<ruby>人<rt>ひと</rt></ruby>もいる。</p>''',
        "questions": [
            {
                "text": "<ruby>桜<rt>さくら</rt></ruby>が<ruby>咲<rt>さ</rt></ruby>く<ruby>日<rt>ひ</rt></ruby>は<ruby>何<rt>なに</rt></ruby>で<ruby>決<rt>き</rt></ruby>まりますか。",
                "choices": [
                    "<ruby>気温<rt>きおん</rt></ruby>",
                    "<ruby>雨<rt>あめ</rt></ruby>の<ruby>量<rt>りょう</rt></ruby>",
                    "<ruby>風<rt>かぜ</rt></ruby>の<ruby>強<rt>つよ</rt></ruby>さ",
                    "<ruby>土<rt>つち</rt></ruby>の<ruby>色<rt>いろ</rt></ruby>",
                ],
                "answer": 0,
                "explanation": "Matnda aniq aytilgan: gullash kuni "
                               "harorat bilan belgilanadi — «暖かく "
                               "なるにつれて、花が開く». Shuning uchun "
                               "janub erta, shimol kech.",
            },
            {
                "text": "<ruby>同<rt>おな</rt></ruby>じ<ruby>山<rt>やま</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>と<ruby>下<rt>した</rt></ruby>では、どうして<ruby>咲<rt>さ</rt></ruby>く<ruby>日<rt>ひ</rt></ruby>が<ruby>違<rt>ちが</rt></ruby>いますか。",
                "choices": [
                    "<ruby>高<rt>たか</rt></ruby>く<ruby>登<rt>のぼ</rt></ruby>るにしたがって<ruby>気温<rt>きおん</rt></ruby>が<ruby>下<rt>さ</rt></ruby>がるから",
                    "<ruby>上<rt>うえ</rt></ruby>のほうが<ruby>風<rt>かぜ</rt></ruby>が<ruby>強<rt>つよ</rt></ruby>いから",
                    "<ruby>上<rt>うえ</rt></ruby>の<ruby>桜<rt>さくら</rt></ruby>は<ruby>種類<rt>しゅるい</rt></ruby>が<ruby>違<rt>ちが</rt></ruby>うから",
                    "<ruby>下<rt>した</rt></ruby>には<ruby>人<rt>ひと</rt></ruby>が<ruby>多<rt>おお</rt></ruby>いから",
                ],
                "answer": 0,
                "explanation": "Balandlik oshgan sari harorat tushadi, "
                               "shuning uchun bitta togʻning etagi va "
                               "choʻqqisi bir kunda gullamaydi. Bu "
                               "にしたがって ning «…gan sari» maʼnosi.",
            },
            {
                "text": "<ruby>都会<rt>とかい</rt></ruby>の<ruby>桜<rt>さくら</rt></ruby>について、<ruby>正<rt>ただ</rt></ruby>しいのはどれですか。",
                "choices": [
                    "まわりの<ruby>田舎<rt>いなか</rt></ruby>より<ruby>早<rt>はや</rt></ruby>く<ruby>咲<rt>さ</rt></ruby>くことがある",
                    "まわりの<ruby>田舎<rt>いなか</rt></ruby>より<ruby>遅<rt>おそ</rt></ruby>く<ruby>咲<rt>さ</rt></ruby>く",
                    "<ruby>咲<rt>さ</rt></ruby>かなくなった",
                    "<ruby>一年<rt>いちねん</rt></ruby>に<ruby>二回<rt>にかい</rt></ruby><ruby>咲<rt>さ</rt></ruby>く",
                ],
                "answer": 0,
                "explanation": "Shahar kattalashgan sari markazdagi "
                               "harorat koʻtariladi, shuning uchun "
                               "shahar sakurasi atrofdagi qishloqdan "
                               "oldinroq ochilishi mumkin.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "まちの としょかんが ひらいた",
        "summary": (
            "PJ-87 matni. Midori shaharchasida yangi kutubxona ochildi: "
            "uni yosh meʼmor loyihalagan, pulining bir qismini "
            "shaharchaning oʻzi yigʻgan, ish vaqti kunga qarab "
            "farq qiladi. Yangilik xabari shaklidagi matn."
        ),
        "order":   87,
        "grammar": [
            {
                "pattern":  "ot + によって",
                "meaning":  "Toʻrtta vazifa, bitta maʼno — «ish shu "
                            "narsadan kelib chiqdi»: bajaruvchi "
                            "(tomonidan), sabab (tufayli), vosita "
                            "(orqali), farqlanish (ga qarab).",
                "examples": ["<ruby>建築家<rt>けんちくか</rt></ruby>によって<ruby>設計<rt>せっけい</rt></ruby>された。",
                             "<ruby>曜日<rt>ようび</rt></ruby>によって<ruby>違<rt>ちが</rt></ruby>う。"],
            },
            {
                "pattern":  "ot + による + ot",
                "meaning":  "によって ning ot oldidagi shakli: "
                            "«…dan kelib chiqqan …».",
                "examples": ["<ruby>台風<rt>たいふう</rt></ruby>による<ruby>被害<rt>ひがい</rt></ruby>"],
            },
            {
                "pattern":  "bajaruvchisiz passiv",
                "meaning":  "Yozma matnda kim qilgani koʻpincha "
                            "aytilmaydi — fakt muhim, bajaruvchi emas. "
                            "Yangilik tilining odatiy ovozi.",
                "examples": ["<ruby>昔話<rt>むかしばなし</rt></ruby>が<ruby>読<rt>よ</rt></ruby>まれる。"],
            },
        ],
        "body": '''<p><ruby>先週<rt>せんしゅう</rt></ruby>の<ruby>土曜日<rt>どようび</rt></ruby>、みどり<ruby>町<rt>まち</rt></ruby>に<ruby>新<rt>あたら</rt></ruby>しい<ruby>図書館<rt>としょかん</rt></ruby>が<ruby>開<rt>ひら</rt></ruby>いた。</p>

<p>この<ruby>建物<rt>たてもの</rt></ruby>は、<ruby>三十歳<rt>さんじゅっさい</rt></ruby>の<ruby>若<rt>わか</rt></ruby>い<span class="cn-word" data-tr="meʼmor, arxitektor"><ruby>建築家<rt>けんちくか</rt></ruby></span>によって<span class="cn-word" data-tr="loyihalangan"><ruby>設計<rt>せっけい</rt></ruby>された</span>。<ruby>屋根<rt>やね</rt></ruby>の<ruby>形<rt>かたち</rt></ruby>は、<ruby>町<rt>まち</rt></ruby>の<ruby>後<rt>うし</rt></ruby>ろにある<ruby>山<rt>やま</rt></ruby>に<ruby>似<rt>に</rt></ruby>ている。<ruby>壁<rt>かべ</rt></ruby>のれんがは、<ruby>町<rt>まち</rt></ruby>の<ruby>工場<rt>こうじょう</rt></ruby>で<ruby>作<rt>つく</rt></ruby>られたものだ。</p>

<p><ruby>建設<rt>けんせつ</rt></ruby>のお<ruby>金<rt>かね</rt></ruby>の<ruby>一部<rt>いちぶ</rt></ruby>は、<ruby>町<rt>まち</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>たちによって<ruby>集<rt>あつ</rt></ruby>められた。<ruby>三年<rt>さんねん</rt></ruby>のあいだに、<ruby>二千人<rt>にせんにん</rt></ruby><ruby>以上<rt>いじょう</rt></ruby>が<span class="cn-word" data-tr="hamkorlik qildi"><ruby>協力<rt>きょうりょく</rt></ruby>した</span>。</p>

<p><ruby>図書館<rt>としょかん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>には、<ruby>二万冊<rt>にまんさつ</rt></ruby>の<ruby>本<rt>ほん</rt></ruby>がある。<ruby>開<rt>ひら</rt></ruby>いている<ruby>時間<rt>じかん</rt></ruby>は<ruby>曜日<rt>ようび</rt></ruby>によって<ruby>違<rt>ちが</rt></ruby>う。<ruby>平日<rt>へいじつ</rt></ruby>は<ruby>午前<rt>ごぜん</rt></ruby><ruby>九時<rt>くじ</rt></ruby>から<ruby>午後<rt>ごご</rt></ruby><ruby>八時<rt>はちじ</rt></ruby>まで、<ruby>土曜日<rt>どようび</rt></ruby>と<ruby>日曜日<rt>にちようび</rt></ruby>は<ruby>午後<rt>ごご</rt></ruby><ruby>六時<rt>ろくじ</rt></ruby>までだ。</p>

<p><ruby>一階<rt>いっかい</rt></ruby>には<ruby>子<rt>こ</rt></ruby>どものための<ruby>部屋<rt>へや</rt></ruby>がある。ここでは、<ruby>毎週<rt>まいしゅう</rt></ruby><ruby>土曜日<rt>どようび</rt></ruby>に、<ruby>町<rt>まち</rt></ruby>のお<ruby>年寄<rt>としよ</rt></ruby>りによって<ruby>昔話<rt>むかしばなし</rt></ruby>が<ruby>読<rt>よ</rt></ruby>まれる。</p>

<p><span class="cn-word" data-tr="kutubxona mudiri"><ruby>館長<rt>かんちょう</rt></ruby></span>はこう<ruby>話<rt>はな</rt></ruby>した。</p>

<p><strong>かんちょう:</strong> <ruby>本<rt>ほん</rt></ruby>の<ruby>選<rt>えら</rt></ruby>び<ruby>方<rt>かた</rt></ruby>は、<ruby>来<rt>き</rt></ruby>た<ruby>人<rt>ひと</rt></ruby>の<span class="cn-word" data-tr="istak, soʻrov"><ruby>希望<rt>きぼう</rt></ruby></span>によって<ruby>決<rt>き</rt></ruby>めています。<ruby>読<rt>よ</rt></ruby>みたい<ruby>本<rt>ほん</rt></ruby>がない<ruby>人<rt>ひと</rt></ruby>は、ぜひ<ruby>教<rt>おし</rt></ruby>えてください。</p>

<p><ruby>開<rt>ひら</rt></ruby>いた<ruby>日<rt>ひ</rt></ruby>には、<ruby>朝<rt>あさ</rt></ruby>から<ruby>長<rt>なが</rt></ruby>い<span class="cn-word" data-tr="navbat"><ruby>列<rt>れつ</rt></ruby></span>ができた。みどり<ruby>町<rt>まち</rt></ruby>の<ruby>人口<rt>じんこう</rt></ruby>は<ruby>八千人<rt>はっせんにん</rt></ruby>ぐらいだが、その<ruby>日<rt>ひ</rt></ruby>だけで<ruby>千二百人<rt>せんにひゃくにん</rt></ruby>が<ruby>来<rt>き</rt></ruby>たという。<ruby>二階<rt>にかい</rt></ruby>の<ruby>窓<rt>まど</rt></ruby>からは、<ruby>山<rt>やま</rt></ruby>と<ruby>川<rt>かわ</rt></ruby>がよく<ruby>見<rt>み</rt></ruby>える。<ruby>窓<rt>まど</rt></ruby>の<ruby>近<rt>ちか</rt></ruby>くの<ruby>席<rt>せき</rt></ruby>は<ruby>人気<rt>にんき</rt></ruby>があるので、<ruby>来<rt>き</rt></ruby>た<ruby>順番<rt>じゅんばん</rt></ruby>によって<ruby>決<rt>き</rt></ruby>まる。</p>

<p><ruby>先月<rt>せんげつ</rt></ruby>の<ruby>台風<rt>たいふう</rt></ruby>による<span class="cn-word" data-tr="zarar, talafot"><ruby>被害<rt>ひがい</rt></ruby></span>で、<ruby>隣<rt>となり</rt></ruby>の<ruby>町<rt>まち</rt></ruby>の<ruby>図書館<rt>としょかん</rt></ruby>はまだ<ruby>閉<rt>し</rt></ruby>まっている。みどり<ruby>町<rt>まち</rt></ruby>の<ruby>図書館<rt>としょかん</rt></ruby>は、その<ruby>町<rt>まち</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>も<ruby>使<rt>つか</rt></ruby>えるようにするという。</p>''',
        "questions": [
            {
                "text": "<ruby>建設<rt>けんせつ</rt></ruby>のお<ruby>金<rt>かね</rt></ruby>の<ruby>一部<rt>いちぶ</rt></ruby>はどうやって<ruby>集<rt>あつ</rt></ruby>まりましたか。",
                "choices": [
                    "<ruby>町<rt>まち</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>たちによって<ruby>集<rt>あつ</rt></ruby>められた",
                    "<ruby>建築家<rt>けんちくか</rt></ruby>が<ruby>全部<rt>ぜんぶ</rt></ruby><ruby>出<rt>だ</rt></ruby>した",
                    "<ruby>隣<rt>となり</rt></ruby>の<ruby>町<rt>まち</rt></ruby>から<ruby>借<rt>か</rt></ruby>りた",
                    "<ruby>工場<rt>こうじょう</rt></ruby>が<ruby>払<rt>はら</rt></ruby>った",
                ],
                "answer": 0,
                "explanation": "«町の人たちによって集められた» — uch yil "
                               "davomida ikki mingdan ortiq kishi "
                               "qatnashgan. Bu によって ning bajaruvchi "
                               "maʼnosi.",
            },
            {
                "text": "<ruby>図書館<rt>としょかん</rt></ruby>の<ruby>開<rt>ひら</rt></ruby>いている<ruby>時間<rt>じかん</rt></ruby>はどうなっていますか。",
                "choices": [
                    "<ruby>曜日<rt>ようび</rt></ruby>によって<ruby>違<rt>ちが</rt></ruby>う",
                    "<ruby>毎日<rt>まいにち</rt></ruby><ruby>同<rt>おな</rt></ruby>じだ",
                    "<ruby>土曜日<rt>どようび</rt></ruby>は<ruby>閉<rt>し</rt></ruby>まっている",
                    "<ruby>午前中<rt>ごぜんちゅう</rt></ruby>だけ<ruby>開<rt>ひら</rt></ruby>いている",
                ],
                "answer": 0,
                "explanation": "Ish kunlari kechqurun sakkizgacha, "
                               "dam olish kunlari oltigacha. Bu によって "
                               "ning toʻrtinchi maʼnosi — «…ga qarab "
                               "farq qiladi», va u doim 違う bilan "
                               "keladi.",
            },
            {
                "text": "<ruby>隣<rt>となり</rt></ruby>の<ruby>町<rt>まち</rt></ruby>の<ruby>図書館<rt>としょかん</rt></ruby>はどうなりましたか。",
                "choices": [
                    "<ruby>台風<rt>たいふう</rt></ruby>による<ruby>被害<rt>ひがい</rt></ruby>で、まだ<ruby>閉<rt>し</rt></ruby>まっている",
                    "<ruby>先週<rt>せんしゅう</rt></ruby><ruby>新<rt>あたら</rt></ruby>しくなった",
                    "みどり<ruby>町<rt>まち</rt></ruby>へ<ruby>移<rt>うつ</rt></ruby>った",
                    "<ruby>本<rt>ほん</rt></ruby>を<ruby>全部<rt>ぜんぶ</rt></ruby><ruby>売<rt>う</rt></ruby>った",
                ],
                "answer": 0,
                "explanation": "«台風による被害で» — ot oldida qolip "
                               "による ga oʻzgaradi. Shuning uchun "
                               "Midori kutubxonasi qoʻshni "
                               "shaharchaning aholisiga ham eshigini "
                               "ochmoqchi.",
            },
        ],
    },
]
