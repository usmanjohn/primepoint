# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-94 … PJ-96.

Uzunlik Blok F tasmasida (190–270 soʻz).

Shakl navbati: 94 — kichik oilaviy hikoya (oshxona haftasi),
95 — sport reportaji, 96 — GAZETA XABARI. Oldingi batchda
kundalik voqea / maslahat ustuni / bitiruv nutqi boʻlgan edi.

Registr: 94 va 95 — 普通体 hikoya, «» ichidagi gap 丁寧体.
96 — である体, chunki darsning oʻzi shu haqda: bu matn PJ-96
ning namunasi, gazeta uslubining oʻzi.

⚠️ CUMULATIVE:
    94 — どころか, ばかりか, どころではない erkin. とたん・次第・
         かのうちに (PJ-95) va である体 (PJ-96) YOʻQ.
    95 — + とたん, 次第, か〜ないかのうちに. である体 hali YOʻQ
         (hikoya だ体da).
    96 — hammasi erkin, va である体 aynan shu matnning tili.
    97…100 dan hech narsa yoʻq: 拝啓・敬具, 四字熟語, ことわざ,
    和語・漢語・外来語.

⚠️ 〜のです ham, 〜んです ham bu shelfda yozilmaydi.

⚠️ 96-matn — oʻylab topilgan shahar haqidagi oʻylab topilgan
xabar. Hech qanday haqiqiy joy nomi, sana yoki tashkilot
nomi yoʻq: gazeta USLUBI oʻrgatilyapti, yangilik emas.

⚠️ AUDIODAN OLDIN NARRATSIYANI OʻQIB CHIQING — <rt> olib
tashlangan, teglar olib tashlangan holda. PJ-13…15 da
«行来ました» aynan shu bosqichda ushlangan edi.

Audio (navbat bilan, oldingi batch 93 da Keita bilan tugagan edi):
    --only 94 --voice ja-JP-NanamiNeural
    --only 95 --voice ja-JP-KeitaNeural
    --only 96 --voice ja-JP-NanamiNeural

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_94_96.py --author=prime
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
        "title":   "にがてどころか",
        "summary": (
            "PJ-94 matni. Pari oshpazlikni umuman uddalay olmasligiga "
            "ishonardi. Onasi bir haftaga ketganda, oshxona unga qoladi. "
            "Birinchi kun falokat boʻladi — lekin hafta oxirida onasi "
            "«uddalay olmas emish» deb kuladi."
        ),
        "order":   94,
        "grammar": [
            {
                "pattern":  "〜どころか",
                "meaning":  "«… u yoqda tursin; aksincha». Kutilgan narsani "
                            "rad etib, undan kuchliroq haqiqatni aytadi. "
                            "Ikkinchi qismida deyarli doim も turadi.",
                "examples": ["<ruby>苦手<rt>にがて</rt></ruby>どころか、いちばん<ruby>上手<rt>じょうず</rt></ruby>だ。",
                             "<ruby>一時間<rt>いちじかん</rt></ruby>どころか、<ruby>三時間<rt>さんじかん</rt></ruby>もかかった。"],
            },
            {
                "pattern":  "〜ばかりか",
                "meaning":  "«ustiga-ustak, … ham». Birinchi qismni rad "
                            "etmaydi — u haqiqat, va ustiga kutilmagan "
                            "yana bittasi qoʻshiladi.",
                "examples": ["<ruby>料理<rt>りょうり</rt></ruby>ばかりか、かたづけもするようになった。"],
            },
            {
                "pattern":  "〜どころではない",
                "meaning":  "«… qayoqda, uning payti emas». Narsani emas, "
                            "vaziyatni inkor qiladi: bu haqda gapirishning "
                            "oʻzi ortiqcha.",
                "examples": ["おいしいどころではなかった。"],
            },
        ],
        "body": '''<p>パリは<ruby>料理<rt>りょうり</rt></ruby>が<span class="cn-word" data-tr="uddalay olmaydigan, yoqtirmaydigan"><ruby>苦手<rt>にがて</rt></ruby></span>だった。<ruby>台所<rt>だいどころ</rt></ruby>に<ruby>立<rt>た</rt></ruby>つと、いつも<ruby>何<rt>なに</rt></ruby>かを<span class="cn-word" data-tr="kuydirib yubormoq"><ruby>焦<rt>こ</rt></ruby>がした</span>。</p>

<p>ある<ruby>週<rt>しゅう</rt></ruby>、<ruby>母<rt>はは</rt></ruby>が<ruby>一週間<rt>いっしゅうかん</rt></ruby><ruby>家<rt>いえ</rt></ruby>にいなかった。</p>

<p><strong>おかあさん:</strong> パリ、おねがいね。かんたんな<ruby>物<rt>もの</rt></ruby>でいいですよ。</p>

<p><ruby>最初<rt>さいしょ</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>はひどかった。ごはんは<ruby>固<rt>かた</rt></ruby>く、スープは<span class="cn-word" data-tr="shoʻr"><ruby>塩<rt>しお</rt></ruby>からかった</span>。おいしいどころではなかった。<ruby>弟<rt>おとうと</rt></ruby>のイノムは<ruby>一口<rt>ひとくち</rt></ruby><ruby>食<rt>た</rt></ruby>べて、<ruby>水<rt>みず</rt></ruby>を<ruby>飲<rt>の</rt></ruby>んだ。</p>

<p><ruby>次<rt>つぎ</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>、パリはノートを<ruby>開<rt>ひら</rt></ruby>いた。<ruby>母<rt>はは</rt></ruby>の<span class="cn-word" data-tr="retsept"><ruby>作<rt>つく</rt></ruby>り<ruby>方<rt>かた</rt></ruby></span>を<ruby>一行<rt>いちぎょう</rt></ruby>ずつ<ruby>書<rt>か</rt></ruby>き<ruby>写<rt>うつ</rt></ruby>した。<ruby>時間<rt>じかん</rt></ruby>をはかり、<ruby>味<rt>あじ</rt></ruby>をみた。</p>

<p><ruby>三日目<rt>みっかめ</rt></ruby>のスープは、<ruby>悪<rt>わる</rt></ruby>くなかった。<ruby>四日目<rt>よっかめ</rt></ruby>には、イノムが<span class="cn-word" data-tr="yana bir marta olmoq">おかわり</span>をした。</p>

<p><ruby>金曜日<rt>きんようび</rt></ruby>、パリは<ruby>初<rt>はじ</rt></ruby>めて<ruby>友<rt>とも</rt></ruby>だちを<ruby>家<rt>いえ</rt></ruby>に<ruby>呼<rt>よ</rt></ruby>んだ。ムニラは<ruby>一皿<rt>ひとさら</rt></ruby><ruby>食<rt>た</rt></ruby>べて、<ruby>手<rt>て</rt></ruby>を<ruby>止<rt>と</rt></ruby>めた。「これ、お<ruby>店<rt>みせ</rt></ruby>の<ruby>味<rt>あじ</rt></ruby>ですね」と<ruby>言<rt>い</rt></ruby>った。パリは<ruby>笑<rt>わら</rt></ruby>って、<ruby>何<rt>なに</rt></ruby>も<ruby>言<rt>い</rt></ruby>わなかった。</p>

<p><ruby>週<rt>しゅう</rt></ruby>の<ruby>終<rt>お</rt></ruby>わり、<ruby>母<rt>はは</rt></ruby>が<ruby>帰<rt>かえ</rt></ruby>ってきた。<ruby>台所<rt>だいどころ</rt></ruby>はきれいで、<ruby>鍋<rt>なべ</rt></ruby>も<span class="cn-word" data-tr="yigʻishtirilgan"><ruby>片<rt>かた</rt></ruby>づいていた</span>。</p>

<p><strong>おかあさん:</strong> <ruby>苦手<rt>にがて</rt></ruby>どころか、いちばん<ruby>上手<rt>じょうず</rt></ruby>じゃないですか。</p>

<p><strong>パリ:</strong> <ruby>苦手<rt>にがて</rt></ruby>だと<ruby>思<rt>おも</rt></ruby>っていただけです。<ruby>一度<rt>いちど</rt></ruby>もやったことがなかっただけです。</p>

<p>その<ruby>日<rt>ひ</rt></ruby>から、パリは<ruby>料理<rt>りょうり</rt></ruby>ばかりか、かたづけもするようになった。<ruby>弟<rt>おとうと</rt></ruby>も<ruby>手伝<rt>てつだ</rt></ruby>うようになった。</p>

<p>パリは<ruby>気<rt>き</rt></ruby>がついた。<ruby>料理<rt>りょうり</rt></ruby>は<ruby>難<rt>むずか</rt></ruby>しいどころか、<ruby>数学<rt>すうがく</rt></ruby>よりずっとやさしい。<ruby>答<rt>こた</rt></ruby>えが<ruby>毎日<rt>まいにち</rt></ruby><ruby>目<rt>め</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>に<ruby>出<rt>で</rt></ruby>てくるからだ。</p>

<p>「<ruby>苦手<rt>にがて</rt></ruby>」というのは、できないという<ruby>意味<rt>いみ</rt></ruby>ではない。まだ<ruby>一度<rt>いちど</rt></ruby>もやっていない、という<ruby>意味<rt>いみ</rt></ruby>のこともある。</p>''',
        "questions": [
            {
                "text": "<ruby>最初<rt>さいしょ</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>の<ruby>料理<rt>りょうり</rt></ruby>はどうでしたか。",
                "choices": [
                    "おいしいどころではなかった",
                    "<ruby>母<rt>はは</rt></ruby>の<ruby>物<rt>もの</rt></ruby>より<ruby>上手<rt>じょうず</rt></ruby>だった",
                    "イノムがおかわりをした",
                    "<ruby>弟<rt>おとうと</rt></ruby>が<ruby>作<rt>つく</rt></ruby>った",
                ],
                "answer": 0,
                "explanation": "Guruch qattiq, shoʻrva shoʻr edi — "
                               "«mazali qayoqda». おかわり esa "
                               "toʻrtinchi kuni boʻlgan, birinchi "
                               "kuni emas.",
            },
            {
                "text": "パリは<ruby>二<rt>ふつ</rt></ruby>か<ruby>目<rt>め</rt></ruby>に<ruby>何<rt>なに</rt></ruby>をしましたか。",
                "choices": [
                    "<ruby>母<rt>はは</rt></ruby>の<ruby>作<rt>つく</rt></ruby>り<ruby>方<rt>かた</rt></ruby>をノートに<ruby>書<rt>か</rt></ruby>き<ruby>写<rt>うつ</rt></ruby>した",
                    "<ruby>店<rt>みせ</rt></ruby>で<ruby>食<rt>た</rt></ruby>べた",
                    "<ruby>母<rt>はは</rt></ruby>に<ruby>電話<rt>でんわ</rt></ruby>した",
                    "<ruby>料理<rt>りょうり</rt></ruby>をやめた",
                ],
                "answer": 0,
                "explanation": "U onasining retseptini bir qatordan "
                               "koʻchirib yozdi, vaqtni oʻlchadi va "
                               "mazasini tatib koʻrdi. Yordam "
                               "soʻramadi — oʻzi usul topdi.",
            },
            {
                "text": "この<ruby>話<rt>はなし</rt></ruby>のいちばん<ruby>大<rt>たい</rt></ruby><ruby>切<rt>せつ</rt></ruby>な<ruby>意味<rt>いみ</rt></ruby>は<ruby>何<rt>なに</rt></ruby>ですか。",
                "choices": [
                    "「<ruby>苦手<rt>にがて</rt></ruby>」は、まだやっていないという<ruby>意味<rt>いみ</rt></ruby>のこともある",
                    "<ruby>料理<rt>りょうり</rt></ruby>は<ruby>母<rt>はは</rt></ruby>がするべきだ",
                    "ノートを<ruby>買<rt>か</rt></ruby>うと<ruby>上手<rt>じょうず</rt></ruby>になる",
                    "スープはむずかしい",
                ],
                "answer": 0,
                "explanation": "Oxirgi jumla butun matnning "
                               "maʼnosi: «uddalay olmayman» "
                               "koʻpincha «hali bir marta ham "
                               "qilib koʻrmadim» degani boʻladi.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "ホイッスルが なったとたん",
        "summary": (
            "PJ-95 matni. Shahar chempionatining finali, uch daqiqa "
            "qoldi va Inom jamoasi bir ochkoga ortda. Murabbiyning "
            "koʻrsatmasi, oxirgi zarba va hushtak — hammasi bir necha "
            "soniyada. とたん, 次第 va か〜ないかのうちに shu matnda yashaydi."
        ),
        "order":   95,
        "grammar": [
            {
                "pattern":  "た-shakli + とたん(に)",
                "meaning":  "«…ishi bilanoq». Ikki voqea orasida vaqt "
                            "yoʻq, ikkinchisi KUTILMAGAN va gap OʻTGAN "
                            "zamonda tugaydi.",
                "examples": ["シュートを<ruby>打<rt>う</rt></ruby>ったとたん、<ruby>体育館<rt>たいいくかん</rt></ruby>が<ruby>静<rt>しず</rt></ruby>かになった。",
                             "ホイッスルが<ruby>鳴<rt>な</rt></ruby>ったとたん、みんなが<ruby>走<rt>はし</rt></ruby>り<ruby>出<rt>だ</rt></ruby>した。"],
            },
            {
                "pattern":  "ます-oʻzagi / ot + <ruby>次第<rt>しだい</rt></ruby>",
                "meaning":  "«…ishi bilan, … qilaman». Rejali ish, va gap "
                            "KELASI zamonda — buyruq, iltimos yoki niyat "
                            "bilan tugaydi. Oʻtgan zamon boʻlmaydi.",
                "examples": ["ボールを<ruby>取<rt>と</rt></ruby>り<ruby>次第<rt>しだい</rt></ruby>、<ruby>前<rt>まえ</rt></ruby>に<ruby>出<rt>で</rt></ruby>ろ。",
                             "バスが<ruby>来<rt>き</rt></ruby><ruby>次第<rt>しだい</rt></ruby>、<ruby>帰<rt>かえ</rt></ruby>るぞ。"],
            },
            {
                "pattern":  "lugʻat shakli + か + ない-shakli + かのうちに",
                "meaning":  "«…ar-etmas». Ikki voqea ustma-ust tushgan — "
                            "birinchisi tugamasidan ikkinchisi boshlangan. "
                            "Yozma tilning qolipi.",
                "examples": ["<ruby>取<rt>と</rt></ruby>るか<ruby>取<rt>と</rt></ruby>らないかのうちに、<ruby>相手<rt>あいて</rt></ruby>が<ruby>二人<rt>ふたり</rt></ruby><ruby>走<rt>はし</rt></ruby>ってきた。"],
            },
        ],
        "body": '''<p><ruby>十月<rt>じゅうがつ</rt></ruby>の<ruby>土曜日<rt>どようび</rt></ruby>、<ruby>市<rt>し</rt></ruby>の<ruby>大会<rt>たいかい</rt></ruby>の<span class="cn-word" data-tr="final"><ruby>決勝<rt>けっしょう</rt></ruby></span>だった。イノムのチームは<ruby>一点<rt>いってん</rt></ruby><ruby>負<rt>ま</rt></ruby>けていた。<ruby>残<rt>のこ</rt></ruby>りは<ruby>三分<rt>さんぷん</rt></ruby>。</p>

<p><ruby>体育館<rt>たいいくかん</rt></ruby>は<ruby>暑<rt>あつ</rt></ruby>かった。<span class="cn-word" data-tr="murabbiy"><ruby>監督<rt>かんとく</rt></ruby></span>がみんなを<ruby>呼<rt>よ</rt></ruby>んだ。</p>

<p><strong>かんとく:</strong> <ruby>時間<rt>じかん</rt></ruby>がない。ボールを<ruby>取<rt>と</rt></ruby>り<ruby>次第<rt>しだい</rt></ruby>、<ruby>前<rt>まえ</rt></ruby>に<ruby>出<rt>で</rt></ruby>ろ。<ruby>考<rt>かんが</rt></ruby>えるな。</p>

<p>イムロンがボールを<ruby>取<rt>と</rt></ruby>った。<ruby>取<rt>と</rt></ruby>るか<ruby>取<rt>と</rt></ruby>らないかのうちに、<ruby>相手<rt>あいて</rt></ruby>の<span class="cn-word" data-tr="oʻyinchi"><ruby>選手<rt>せんしゅ</rt></ruby></span>が<ruby>二人<rt>ふたり</rt></ruby><ruby>走<rt>はし</rt></ruby>ってきた。イムロンは<ruby>右<rt>みぎ</rt></ruby>を<ruby>見<rt>み</rt></ruby>て、<ruby>左<rt>ひだり</rt></ruby>のイノムにパスした。</p>

<p><ruby>残<rt>のこ</rt></ruby>り<ruby>十秒<rt>じゅうびょう</rt></ruby>。イノムは<ruby>走<rt>はし</rt></ruby>って、<ruby>止<rt>と</rt></ruby>まって、シュートを<ruby>打<rt>う</rt></ruby>った。<ruby>打<rt>う</rt></ruby>ったとたん、<ruby>体育館<rt>たいいくかん</rt></ruby>が<ruby>静<rt>しず</rt></ruby>かになった。</p>

<p>ボールは<span class="cn-word" data-tr="savat halqasi">リング</span>に<ruby>当<rt>あ</rt></ruby>たった。<ruby>一度<rt>いちど</rt></ruby><ruby>上<rt>うえ</rt></ruby>に<ruby>上<rt>あ</rt></ruby>がって、それから<ruby>中<rt>なか</rt></ruby>に<ruby>落<rt>お</rt></ruby>ちた。</p>

<p>ホイッスルが<ruby>鳴<rt>な</rt></ruby>るか<ruby>鳴<rt>な</rt></ruby>らないかのうちに、みんながコートに<ruby>飛<rt>と</rt></ruby>び<ruby>出<rt>だ</rt></ruby>した。<ruby>一点<rt>いってん</rt></ruby><ruby>差<rt>さ</rt></ruby>で<ruby>勝<rt>か</rt></ruby>った。</p>

<p><ruby>観客<rt>かんきゃく</rt></ruby>が<ruby>立<rt>た</rt></ruby>ち<ruby>上<rt>あ</rt></ruby>がった。<ruby>相手<rt>あいて</rt></ruby>のチームの<ruby>選手<rt>せんしゅ</rt></ruby>たちも<ruby>手<rt>て</rt></ruby>をたたいた。いい<ruby>試合<rt>しあい</rt></ruby>だったと、だれもが<ruby>思<rt>おも</rt></ruby>った。</p>

<p>イノムは<ruby>床<rt>ゆか</rt></ruby>に<ruby>座<rt>すわ</rt></ruby>った。<ruby>立<rt>た</rt></ruby>ち<ruby>上<rt>あ</rt></ruby>がったとたん、<ruby>足<rt>あし</rt></ruby>が<span class="cn-word" data-tr="titradi"><ruby>震<rt>ふる</rt></ruby>えた</span>。<ruby>三分<rt>さんぷん</rt></ruby><ruby>前<rt>まえ</rt></ruby>までは、<ruby>負<rt>ま</rt></ruby>けると<ruby>思<rt>おも</rt></ruby>っていた。</p>

<p><strong>かんとく:</strong> バスが<ruby>来<rt>き</rt></ruby><ruby>次第<rt>しだい</rt></ruby>、<ruby>帰<rt>かえ</rt></ruby>るぞ。</p>

<p>だれも<ruby>動<rt>うご</rt></ruby>かなかった。<ruby>監督<rt>かんとく</rt></ruby>も<ruby>動<rt>うご</rt></ruby>かなかった。</p>

<p><ruby>試合<rt>しあい</rt></ruby>は<ruby>三分<rt>さんぷん</rt></ruby>で<ruby>変<rt>か</rt></ruby>わる。<span class="cn-word" data-tr="taslim boʻlmoq"><ruby>諦<rt>あきら</rt></ruby>めた</span>とたん、<ruby>本当<rt>ほんとう</rt></ruby>に<ruby>終<rt>お</rt></ruby>わる。イノムはその<ruby>日<rt>ひ</rt></ruby>、それを<ruby>体<rt>からだ</rt></ruby>で<ruby>覚<rt>おぼ</rt></ruby>えた。</p>''',
        "questions": [
            {
                "text": "<ruby>監督<rt>かんとく</rt></ruby>は<ruby>何<rt>なに</rt></ruby>と<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "ボールを<ruby>取<rt>と</rt></ruby>り<ruby>次第<rt>しだい</rt></ruby>、<ruby>前<rt>まえ</rt></ruby>に<ruby>出<rt>で</rt></ruby>ろ",
                    "ゆっくり<ruby>考<rt>かんが</rt></ruby>えろ",
                    "<ruby>後<rt>うし</rt></ruby>ろで<ruby>待<rt>ま</rt></ruby>て",
                    "シュートを<ruby>打<rt>う</rt></ruby>つな",
                ],
                "answer": 0,
                "explanation": "Vaqt yoʻq edi, shuning uchun murabbiy "
                               "«toʻpni olishing bilan oldinga chiq» dedi. "
                               "次第 aynan shunday buyruq bilan keladi — "
                               "とたん esa buyruq koʻtarmaydi.",
            },
            {
                "text": "イノムがシュートを<ruby>打<rt>う</rt></ruby>ったとき、<ruby>体育館<rt>たいいくかん</rt></ruby>はどうなりましたか。",
                "choices": [
                    "<ruby>静<rt>しず</rt></ruby>かになった",
                    "みんなが<ruby>歌<rt>うた</rt></ruby>った",
                    "<ruby>電気<rt>でんき</rt></ruby>が<ruby>消<rt>き</rt></ruby>えた",
                    "<ruby>試合<rt>しあい</rt></ruby>が<ruby>止<rt>と</rt></ruby>まった",
                ],
                "answer": 0,
                "explanation": "«<ruby>打<rt>う</rt></ruby>ったとたん、"
                               "<ruby>体育館<rt>たいいくかん</rt></ruby>が"
                               "<ruby>静<rt>しず</rt></ruby>かになった» — zarbadan "
                               "keyin sport zali jimib qoldi. Kutilmagan "
                               "va bir zumda — とたん uchun ideal.",
            },
            {
                "text": "この<ruby>話<rt>はなし</rt></ruby>の<ruby>最後<rt>さいご</rt></ruby>の<ruby>文<rt>ぶん</rt></ruby>は<ruby>何<rt>なに</rt></ruby>を<ruby>言<rt>い</rt></ruby>っていますか。",
                "choices": [
                    "<ruby>諦<rt>あきら</rt></ruby>めたとたん、<ruby>試合<rt>しあい</rt></ruby>は<ruby>本当<rt>ほんとう</rt></ruby>に<ruby>終<rt>お</rt></ruby>わる",
                    "<ruby>強<rt>つよ</rt></ruby>いチームは<ruby>必<rt>かなら</rt></ruby>ず<ruby>勝<rt>か</rt></ruby>つ",
                    "<ruby>監督<rt>かんとく</rt></ruby>の<ruby>話<rt>はなし</rt></ruby>は<ruby>長<rt>なが</rt></ruby>い",
                    "バスを<ruby>待<rt>ま</rt></ruby>つのはつまらない",
                ],
                "answer": 0,
                "explanation": "Oʻyin uch daqiqada oʻzgaradi; u haqiqatan "
                               "tugaydigan yagona payt — taslim boʻlgan "
                               "payt. Inom buni oʻsha kuni tanasi bilan "
                               "bilib oldi.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "こうこうせいが つくった ちず",
        "summary": (
            "PJ-96 matni — gazeta xabari, である体da yozilgan. Bir "
            "shaharning maktab oʻquvchilari tez yoʻlni emas, dam olsa "
            "boʻladigan yoʻlni koʻrsatadigan xarita tuzishdi. Matnning "
            "oʻzi darsning namunasi: yozma uslub qanday koʻrinadi."
        ),
        "order":   96,
        "grammar": [
            {
                "pattern":  "である<ruby>体<rt>たい</rt></ruby>",
                "meaning":  "Yozma-rasmiy uslub: insho, maqola, ilmiy ish "
                            "va gazetaning tili. だ ning oʻrniga である "
                            "keladi; feʼl va い-sifat oʻzgarmaydi.",
                "examples": ["ふつうの<ruby>地図<rt>ちず</rt></ruby>ではない。",
                             "<ruby>二年生<rt>にねんせい</rt></ruby>の<ruby>八人<rt>はちにん</rt></ruby>である。"],
            },
            {
                "pattern":  "しかし · また · なお · <ruby>一方<rt>いっぽう</rt></ruby>",
                "meaning":  "Yozma bogʻlovchilar. Gapda でも, それから, "
                            "ちなみに deymiz; matnda esa shular turadi — "
                            "oʻzbekcha «lekin» va «biroq» kabi.",
                "examples": ["しかし、その<ruby>道<rt>みち</rt></ruby>は<ruby>急<rt>きゅう</rt></ruby>な<ruby>坂<rt>さか</rt></ruby>だった。",
                             "なお、<ruby>学校<rt>がっこう</rt></ruby>のサイトからも<ruby>見<rt>み</rt></ruby>られる。"],
            },
        ],
        "body": '''<p>ある<ruby>町<rt>まち</rt></ruby>の<ruby>高校<rt>こうこう</rt></ruby>の<ruby>生徒<rt>せいと</rt></ruby>たちが、<ruby>町<rt>まち</rt></ruby>の<ruby>地図<rt>ちず</rt></ruby>を<ruby>作<rt>つく</rt></ruby>った。ふつうの<ruby>地図<rt>ちず</rt></ruby>ではない。<ruby>坂<rt>さか</rt></ruby>の<ruby>多<rt>おお</rt></ruby>い<ruby>道<rt>みち</rt></ruby>と、<ruby>休<rt>やす</rt></ruby>める<ruby>場所<rt>ばしょ</rt></ruby>が<ruby>書<rt>か</rt></ruby>いてある<ruby>地図<rt>ちず</rt></ruby>である。</p>

<p><ruby>作<rt>つく</rt></ruby>ったのは<ruby>二年生<rt>にねんせい</rt></ruby>の<ruby>八人<rt>はちにん</rt></ruby>である。<span class="cn-word" data-tr="turtki, boshlanish"><ruby>始<rt>はじ</rt></ruby>まり</span>は<ruby>去年<rt>きょねん</rt></ruby>の<ruby>秋<rt>あき</rt></ruby>の<ruby>出来事<rt>できごと</rt></ruby>だった。<ruby>道<rt>みち</rt></ruby>をたずねられた<ruby>生徒<rt>せいと</rt></ruby>が、<span class="cn-word" data-tr="qisqa yoʻl"><ruby>近道<rt>ちかみち</rt></ruby></span>を<ruby>教<rt>おし</rt></ruby>えた。しかし、その<ruby>道<rt>みち</rt></ruby>は<ruby>急<rt>きゅう</rt></ruby>な<ruby>坂<rt>さか</rt></ruby>だった。たずねたのは、<ruby>八十<rt>はちじゅう</rt></ruby><ruby>歳<rt>さい</rt></ruby>の<ruby>女性<rt>じょせい</rt></ruby>である。</p>

<p><ruby>生徒<rt>せいと</rt></ruby>たちは<ruby>町<rt>まち</rt></ruby>を<ruby>歩<rt>ある</rt></ruby>き、<ruby>坂<rt>さか</rt></ruby>の<span class="cn-word" data-tr="qiyalik burchagi"><ruby>角度<rt>かくど</rt></ruby></span>をはかった。また、ベンチのある<ruby>場所<rt>ばしょ</rt></ruby>、<ruby>水<rt>みず</rt></ruby>が<ruby>飲<rt>の</rt></ruby>める<ruby>場所<rt>ばしょ</rt></ruby>、<ruby>屋根<rt>やね</rt></ruby>のある<ruby>場所<rt>ばしょ</rt></ruby>を<span class="cn-word" data-tr="yozib bordi"><ruby>記録<rt>きろく</rt></ruby>した</span>。<ruby>歩<rt>ある</rt></ruby>いた<span class="cn-word" data-tr="masofa"><ruby>距離<rt>きょり</rt></ruby></span>は<ruby>百<rt>ひゃく</rt></ruby>キロを<ruby>超<rt>こ</rt></ruby>えた。</p>

<p><ruby>地図<rt>ちず</rt></ruby>は<ruby>二種類<rt>にしゅるい</rt></ruby>ある。<ruby>一<rt>ひと</rt></ruby>つは<ruby>紙<rt>かみ</rt></ruby>、もう<ruby>一<rt>ひと</rt></ruby>つはやさしい<ruby>日本語<rt>にほんご</rt></ruby>のものである。<ruby>町<rt>まち</rt></ruby>に<ruby>住<rt>す</rt></ruby>む<ruby>外国人<rt>がいこくじん</rt></ruby>にも<ruby>読<rt>よ</rt></ruby>めるようにした。</p>

<p><ruby>印刷<rt>いんさつ</rt></ruby>の<span class="cn-word" data-tr="xarajat"><ruby>費用<rt>ひよう</rt></ruby></span>は、<ruby>文化祭<rt>ぶんかさい</rt></ruby>で<ruby>集<rt>あつ</rt></ruby>めたお<ruby>金<rt>かね</rt></ruby>である。<ruby>最初<rt>さいしょ</rt></ruby>は<ruby>百部<rt>ひゃくぶ</rt></ruby>だったが、<ruby>足<rt>た</rt></ruby>りなくなり、また<ruby>二百部<rt>にひゃくぶ</rt></ruby><ruby>刷<rt>す</rt></ruby>った。</p>

<p>「<ruby>速<rt>はや</rt></ruby>い<ruby>道<rt>みち</rt></ruby>より、<ruby>休<rt>やす</rt></ruby>める<ruby>道<rt>みち</rt></ruby>を<ruby>書<rt>か</rt></ruby>きたかった」と、<ruby>代表<rt>だいひょう</rt></ruby>の<ruby>生徒<rt>せいと</rt></ruby>は<span class="cn-word" data-tr="bayon qildi"><ruby>述<rt>の</rt></ruby>べた</span>。</p>

<p><ruby>地図<rt>ちず</rt></ruby>は<ruby>町<rt>まち</rt></ruby>の<ruby>図書館<rt>としょかん</rt></ruby>に<ruby>置<rt>お</rt></ruby>かれている。なお、<ruby>学校<rt>がっこう</rt></ruby>のサイトからも<ruby>見<rt>み</rt></ruby>られる。</p>

<p><ruby>一方<rt>いっぽう</rt></ruby>、<span class="cn-word" data-tr="hal boʻlmagan masala"><ruby>課題<rt>かだい</rt></ruby></span>も<ruby>残<rt>のこ</rt></ruby>る。<ruby>工事<rt>こうじ</rt></ruby>で<ruby>道<rt>みち</rt></ruby>は<ruby>変<rt>か</rt></ruby>わる。<ruby>生徒<rt>せいと</rt></ruby>たちは、<ruby>毎年<rt>まいとし</rt></ruby><ruby>春<rt>はる</rt></ruby>に<ruby>調<rt>しら</rt></ruby>べ<ruby>直<rt>なお</rt></ruby>すつもりである。</p>

<p>「<ruby>地図<rt>ちず</rt></ruby>は<ruby>一度<rt>いちど</rt></ruby><ruby>作<rt>つく</rt></ruby>って<ruby>終<rt>お</rt></ruby>わりではない」と、<ruby>担当<rt>たんとう</rt></ruby>の<ruby>先生<rt>せんせい</rt></ruby>は<ruby>語<rt>かた</rt></ruby>った。</p>''',
        "questions": [
            {
                "text": "この<ruby>地図<rt>ちず</rt></ruby>にはどんなことが<ruby>書<rt>か</rt></ruby>いてあるか。",
                "choices": [
                    "<ruby>坂<rt>さか</rt></ruby>の<ruby>多<rt>おお</rt></ruby>い<ruby>道<rt>みち</rt></ruby>と<ruby>休<rt>やす</rt></ruby>める<ruby>場所<rt>ばしょ</rt></ruby>",
                    "<ruby>店<rt>みせ</rt></ruby>の<ruby>名前<rt>なまえ</rt></ruby>と<ruby>値段<rt>ねだん</rt></ruby>",
                    "バスの<ruby>時間<rt>じかん</rt></ruby>",
                    "<ruby>学校<rt>がっこう</rt></ruby>までの<ruby>近道<rt>ちかみち</rt></ruby>",
                ],
                "answer": 0,
                "explanation": "Birinchi xatboshida aytilgan: bu oddiy "
                               "xarita emas — unda qiya yoʻllar va dam "
                               "olsa boʻladigan joylar bor. Qisqa yoʻl "
                               "esa aynan muammoning oʻzi edi.",
            },
            {
                "text": "<ruby>地図<rt>ちず</rt></ruby>を<ruby>作<rt>つく</rt></ruby>る<ruby>始<rt>はじ</rt></ruby>まりは<ruby>何<rt>なに</rt></ruby>だったか。",
                "choices": [
                    "<ruby>近道<rt>ちかみち</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えたが、それが<ruby>急<rt>きゅう</rt></ruby>な<ruby>坂<rt>さか</rt></ruby>だったこと",
                    "<ruby>先生<rt>せんせい</rt></ruby>に<ruby>言<rt>い</rt></ruby>われたこと",
                    "<ruby>町<rt>まち</rt></ruby>から<ruby>頼<rt>たの</rt></ruby>まれたこと",
                    "<ruby>図書館<rt>としょかん</rt></ruby>の<ruby>地図<rt>ちず</rt></ruby>が<ruby>古<rt>ふる</rt></ruby>かったこと",
                ],
                "answer": 0,
                "explanation": "Oʻtgan kuzda bir oʻquvchi 80 yoshli "
                               "ayolga qisqa yoʻlni koʻrsatgan, lekin "
                               "oʻsha yoʻl tik qiyalik boʻlib chiqqan. "
                               "Butun ish shundan boshlangan.",
            },
            {
                "text": "<ruby>生徒<rt>せいと</rt></ruby>たちはこれから<ruby>何<rt>なに</rt></ruby>をするつもりか。",
                "choices": [
                    "<ruby>毎年<rt>まいとし</rt></ruby><ruby>春<rt>はる</rt></ruby>に<ruby>調<rt>しら</rt></ruby>べ<ruby>直<rt>なお</rt></ruby>す",
                    "<ruby>地図<rt>ちず</rt></ruby>を<ruby>売<rt>う</rt></ruby>る",
                    "<ruby>新<rt>あたら</rt></ruby>しい<ruby>町<rt>まち</rt></ruby>の<ruby>地図<rt>ちず</rt></ruby>も<ruby>作<rt>つく</rt></ruby>る",
                    "<ruby>図書館<rt>としょかん</rt></ruby>で<ruby>働<rt>はたら</rt></ruby>く",
                ],
                "answer": 0,
                "explanation": "Qurilish ishlari yoʻllarni oʻzgartiradi, "
                               "shuning uchun ular har yili bahorda "
                               "qaytadan tekshirmoqchi. «Xarita bir marta "
                               "tuzilib tugaydigan narsa emas» — "
                               "maqolaning oxirgi gapi.",
            },
        ],
    },
]
