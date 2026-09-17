# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-88 … PJ-90.

Uzunlik Blok F tasmasida (190–270 soʻz).

Shakl navbati: 88 — intervyu, 89 — sinf soʻrovi hisoboti, 90 — kichik
portret ocherki. Oldingi batchda ertak / ilmiy-ommabop matn / yangilik
xabari boʻlgan edi.

Registr: 88 — intervyu, shuning uchun savol-javob 丁寧体 da, oraliq
izohlar 普通体 da. 89 va 90 — 普通体 (PJ-45 dan beri).

⚠️ CUMULATIVE:
    88 — として va にとって erkin. について・に関して・に対して (PJ-89)
         va ながらも・つつ (PJ-90) YOʻQ.
    89 — + について oilasi. ながらも va つつ hali YOʻQ.
    90 — hammasi erkin.

⚠️ 90-matndagi fakt rost: Yaponiyada mustaqil kitob doʻkonlari soni
oʻn yillar davomida kamayib bormoqda. Qolgani — uydirma doʻkon va
uydirma odam, shuning uchun hech qanday haqiqiy nom yoʻq.

⚠️ 〜のです ham, 〜んです ham bu shelfda yozilmaydi — kurs ikkalasini
ham bermagan. Gate endi ikkovini ham tutadi.

Audio (navbat bilan, oldingi batch 87 da Keita bilan tugagan edi):
    --only 88 --voice ja-JP-NanamiNeural
    --only 89 --voice ja-JP-KeitaNeural
    --only 90 --voice ja-JP-NanamiNeural

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_88_90.py --author=prime
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
        "title":   "ふたつの かお",
        "summary": (
            "PJ-88 matni. Hamshira boʻlib ishlaydigan va ayni paytda ikki "
            "bolaning onasi boʻlgan ayol bilan intervyu. Ikki rol bir "
            "odamda: として rolni, にとって esa uning koʻzini "
            "koʻrsatadi."
        ),
        "order":   88,
        "grammar": [
            {
                "pattern":  "ot + として · としての + ot",
                "meaning":  "«… sifatida» — rolni, maqomni koʻrsatadi. "
                            "Otga yalangʻoch ulanadi; otni aniqlaganda "
                            "oradan の tushadi.",
                "examples": ["<ruby>看護師<rt>かんごし</rt></ruby>として<ruby>働<rt>はたら</rt></ruby>く。",
                             "<ruby>母<rt>はは</rt></ruby>としての<ruby>時間<rt>じかん</rt></ruby>"],
            },
            {
                "pattern":  "ot + にとって",
                "meaning":  "«… nazdida, … uchun» — baho beriladigan "
                            "nuqta. Undan keyin deyarli doim baho "
                            "beruvchi soʻz keladi: 大切だ, 難しい, "
                            "ありがたい.",
                "examples": ["<ruby>私<rt>わたし</rt></ruby>にとっていちばん<ruby>大切<rt>たいせつ</rt></ruby>な<ruby>時間<rt>じかん</rt></ruby>"],
            },
        ],
        "body": '''<p>みどり<ruby>病院<rt>びょういん</rt></ruby>で<ruby>働<rt>はたら</rt></ruby>く<span class="cn-word" data-tr="hamshira"><ruby>看護師<rt>かんごし</rt></ruby></span>、<ruby>森<rt>もり</rt></ruby>さんに<ruby>話<rt>はなし</rt></ruby>を<ruby>聞<rt>き</rt></ruby>いた。<ruby>森<rt>もり</rt></ruby>さんは<ruby>二人<rt>ふたり</rt></ruby>の<ruby>子<rt>こ</rt></ruby>どもの<ruby>母<rt>はは</rt></ruby>でもある。</p>

<p><strong>きしゃ:</strong> <ruby>一日<rt>いちにち</rt></ruby>はどのように<ruby>始<rt>はじ</rt></ruby>まりますか。</p>

<p><strong>もり:</strong> <ruby>朝<rt>あさ</rt></ruby>の<ruby>五時<rt>ごじ</rt></ruby>に<ruby>起<rt>お</rt></ruby>きます。それから<ruby>七時<rt>しちじ</rt></ruby>までは<ruby>母<rt>はは</rt></ruby>としての<ruby>時間<rt>じかん</rt></ruby>です。お<ruby>弁当<rt>べんとう</rt></ruby>を<ruby>作<rt>つく</rt></ruby>って、<ruby>子<rt>こ</rt></ruby>どもを<ruby>送<rt>おく</rt></ruby>ります。<ruby>八時<rt>はちじ</rt></ruby>からは<ruby>看護師<rt>かんごし</rt></ruby>として<ruby>働<rt>はたら</rt></ruby>きます。</p>

<p><ruby>森<rt>もり</rt></ruby>さんは<ruby>笑<rt>わら</rt></ruby>って、<ruby>二<rt>ふた</rt></ruby>つの<ruby>顔<rt>かお</rt></ruby>があると<ruby>言<rt>い</rt></ruby>った。</p>

<p><strong>きしゃ:</strong> <ruby>大変<rt>たいへん</rt></ruby>ではありませんか。</p>

<p><strong>もり:</strong> <ruby>大変<rt>たいへん</rt></ruby>です。でも、<ruby>私<rt>わたし</rt></ruby>にとって、この<ruby>二<rt>ふた</rt></ruby>つはどちらも<ruby>自分<rt>じぶん</rt></ruby>です。<ruby>病院<rt>びょういん</rt></ruby>で<ruby>子<rt>こ</rt></ruby>どもの<ruby>患者<rt>かんじゃ</rt></ruby>さんを<ruby>見<rt>み</rt></ruby>ると、<ruby>母<rt>はは</rt></ruby>としての<ruby>気持<rt>きも</rt></ruby>ちが<ruby>出<rt>で</rt></ruby>てきます。それは<ruby>悪<rt>わる</rt></ruby>いことではないと<ruby>思<rt>おも</rt></ruby>います。</p>

<p><strong>きしゃ:</strong> <span class="cn-word" data-tr="eng qiyin narsa"><ruby>一番<rt>いちばん</rt></ruby><ruby>難<rt>むずか</rt></ruby>しいこと</span>は<ruby>何<rt>なん</rt></ruby>ですか。</p>

<p><strong>もり:</strong> <ruby>時間<rt>じかん</rt></ruby>です。<ruby>子<rt>こ</rt></ruby>どもにとって、<ruby>母親<rt>ははおや</rt></ruby>が<ruby>家<rt>いえ</rt></ruby>にいない<ruby>夜<rt>よる</rt></ruby>は<ruby>寂<rt>さび</rt></ruby>しいはずです。<span class="cn-word" data-tr="tungi navbatchilik"><ruby>夜勤<rt>やきん</rt></ruby></span>の<ruby>日<rt>ひ</rt></ruby>は、<ruby>朝<rt>あさ</rt></ruby>に<ruby>手紙<rt>てがみ</rt></ruby>を<ruby>書<rt>か</rt></ruby>いて<ruby>置<rt>お</rt></ruby>いていきます。</p>

<p><strong>きしゃ:</strong> <ruby>看護師<rt>かんごし</rt></ruby>を<ruby>目指<rt>めざ</rt></ruby>す<ruby>若<rt>わか</rt></ruby>い<ruby>人<rt>ひと</rt></ruby>に<ruby>一言<rt>ひとこと</rt></ruby>お<ruby>願<rt>ねが</rt></ruby>いします。</p>

<p><strong>もり:</strong> <span class="cn-word" data-tr="kasb"><ruby>職業<rt>しょくぎょう</rt></ruby></span>としての<ruby>看護師<rt>かんごし</rt></ruby>は<ruby>楽<rt>らく</rt></ruby>ではありません。でも、だれかにとって<ruby>必要<rt>ひつよう</rt></ruby>な<ruby>人<rt>ひと</rt></ruby>になれます。それは<ruby>私<rt>わたし</rt></ruby>にとって、<ruby>何<rt>なに</rt></ruby>よりも<span class="cn-word" data-tr="qadrli"><ruby>大切<rt>たいせつ</rt></ruby></span>なことです。</p>

<p><ruby>森<rt>もり</rt></ruby>さんは<ruby>時計<rt>とけい</rt></ruby>を<ruby>見<rt>み</rt></ruby>て、<ruby>立<rt>た</rt></ruby>ち<ruby>上<rt>あ</rt></ruby>がった。<span class="cn-word" data-tr="tanaffus"><ruby>休憩<rt>きゅうけい</rt></ruby></span>は<ruby>十五分<rt>じゅうごふん</rt></ruby>だけだった。</p>''',
        "questions": [
            {
                "text": "<ruby>森<rt>もり</rt></ruby>さんの<ruby>朝<rt>あさ</rt></ruby>の<ruby>七時<rt>しちじ</rt></ruby>までは<ruby>何<rt>なん</rt></ruby>の<ruby>時間<rt>じかん</rt></ruby>ですか。",
                "choices": [
                    "<ruby>母<rt>はは</rt></ruby>としての<ruby>時間<rt>じかん</rt></ruby>",
                    "<ruby>看護師<rt>かんごし</rt></ruby>としての<ruby>時間<rt>じかん</rt></ruby>",
                    "<ruby>休<rt>やす</rt></ruby>む<ruby>時間<rt>じかん</rt></ruby>",
                    "<ruby>勉強<rt>べんきょう</rt></ruby>の<ruby>時間<rt>じかん</rt></ruby>",
                ],
                "answer": 0,
                "explanation": "Soat beshda turadi va yettigacha "
                               "ona sifatidagi ish: tushlik "
                               "tayyorlaydi, bolalarni kuzatadi. "
                               "Hamshiralik sakkizdan boshlanadi.",
            },
            {
                "text": "<ruby>夜勤<rt>やきん</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>、<ruby>森<rt>もり</rt></ruby>さんは<ruby>何<rt>なに</rt></ruby>をしますか。",
                "choices": [
                    "<ruby>朝<rt>あさ</rt></ruby>に<ruby>手紙<rt>てがみ</rt></ruby>を<ruby>書<rt>か</rt></ruby>いて<ruby>置<rt>お</rt></ruby>いていく",
                    "<ruby>子<rt>こ</rt></ruby>どもを<ruby>病院<rt>びょういん</rt></ruby>へ<ruby>連<rt>つ</rt></ruby>れていく",
                    "<ruby>仕事<rt>しごと</rt></ruby>を<ruby>休<rt>やす</rt></ruby>む",
                    "<ruby>電話<rt>でんわ</rt></ruby>をかける",
                ],
                "answer": 0,
                "explanation": "Bolalar uchun onasi yoʻq tun "
                               "gʻamgin — shuning uchun u ertalab "
                               "xat yozib qoldiradi. にとって bu "
                               "yerda bolaning koʻzini "
                               "koʻrsatyapti.",
            },
            {
                "text": "<ruby>森<rt>もり</rt></ruby>さんにとって、<ruby>何<rt>なに</rt></ruby>がいちばん<ruby>大切<rt>たいせつ</rt></ruby>ですか。",
                "choices": [
                    "だれかにとって<ruby>必要<rt>ひつよう</rt></ruby>な<ruby>人<rt>ひと</rt></ruby>になれること",
                    "<ruby>給料<rt>きゅうりょう</rt></ruby>が<ruby>高<rt>たか</rt></ruby>いこと",
                    "<ruby>仕事<rt>しごと</rt></ruby>が<ruby>楽<rt>らく</rt></ruby>なこと",
                    "<ruby>休<rt>やす</rt></ruby>みが<ruby>多<rt>おお</rt></ruby>いこと",
                ],
                "answer": 0,
                "explanation": "U kasbning oson emasligini "
                               "yashirmaydi, lekin kimgadir kerakli "
                               "odam boʻla olishni hamma narsadan "
                               "ustun qoʻyadi.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "アンケートの けっか",
        "summary": (
            "PJ-89 matni. Sinf telefon ishlatish haqida soʻrov "
            "oʻtkazdi va natijani hisobot qilib yozdi. について mavzuni, "
            "に対して esa savolga berilgan javobni va ikki guruhning "
            "qarshi qoʻyilishini koʻrsatadi."
        ),
        "order":   89,
        "grammar": [
            {
                "pattern":  "ot + について · についての + ot",
                "meaning":  "«… haqida» — gapning mavzusi. Otni "
                            "aniqlaganda oradan の tushadi.",
                "examples": ["スマホについて<ruby>調<rt>しら</rt></ruby>べた。",
                             "<ruby>時間<rt>じかん</rt></ruby>についての<ruby>質問<rt>しつもん</rt></ruby>"],
            },
            {
                "pattern":  "ot + に<ruby>対<rt>たい</rt></ruby>して",
                "meaning":  "«… ga nisbatan, … ga javoban» — munosabat "
                            "yoki harakat qaratilgan tomon. Ot oldida "
                            "に<ruby>対<rt>たい</rt></ruby>する.",
                "examples": ["<ruby>質問<rt>しつもん</rt></ruby>に<ruby>対<rt>たい</rt></ruby>して<ruby>答<rt>こた</rt></ruby>えた。"],
            },
            {
                "pattern":  "oddiy shakl + のに<ruby>対<rt>たい</rt></ruby>して",
                "meaning":  "Ikki narsani qarshi qoʻyadi: «biri shunday "
                            "boʻlsa, ikkinchisi bunday». な-sifat va ot "
                            "な + の oladi.",
                "examples": ["<ruby>男子<rt>だんし</rt></ruby>が<ruby>多<rt>おお</rt></ruby>いのに<ruby>対<rt>たい</rt></ruby>して、<ruby>女子<rt>じょし</rt></ruby>は<ruby>少<rt>すく</rt></ruby>ない。"],
            },
        ],
        "body": '''<p><ruby>三年<rt>さんねん</rt></ruby><ruby>二組<rt>にくみ</rt></ruby>は、スマホの<ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>について<span class="cn-word" data-tr="soʻrovnoma"><ruby>調査<rt>ちょうさ</rt></ruby></span>を<ruby>行<rt>おこな</rt></ruby>った。<ruby>答<rt>こた</rt></ruby>えたのは<ruby>三十二人<rt>さんじゅうににん</rt></ruby>である。</p>

<p><ruby>最初<rt>さいしょ</rt></ruby>の<ruby>質問<rt>しつもん</rt></ruby>は、<ruby>一日<rt>いちにち</rt></ruby>の<ruby>時間<rt>じかん</rt></ruby>についての<ruby>質問<rt>しつもん</rt></ruby>だった。この<ruby>質問<rt>しつもん</rt></ruby>に<ruby>対<rt>たい</rt></ruby>して、「<ruby>三時間<rt>さんじかん</rt></ruby><ruby>以上<rt>いじょう</rt></ruby>」と<ruby>答<rt>こた</rt></ruby>えた<ruby>人<rt>ひと</rt></ruby>が<ruby>十八人<rt>じゅうはちにん</rt></ruby>いた。<ruby>半分<rt>はんぶん</rt></ruby><ruby>以上<rt>いじょう</rt></ruby>である。</p>

<p><ruby>次<rt>つぎ</rt></ruby>に、<ruby>何<rt>なに</rt></ruby>に<ruby>使<rt>つか</rt></ruby>うかを<ruby>聞<rt>き</rt></ruby>いた。<ruby>動画<rt>どうが</rt></ruby>を<ruby>見<rt>み</rt></ruby>る<ruby>人<rt>ひと</rt></ruby>が<ruby>多<rt>おお</rt></ruby>いのに<ruby>対<rt>たい</rt></ruby>して、<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>む<ruby>人<rt>ひと</rt></ruby>は<ruby>三人<rt>さんにん</rt></ruby>だけだった。ゲームは<ruby>男子<rt>だんし</rt></ruby>に<ruby>多<rt>おお</rt></ruby>く、<span class="cn-word" data-tr="ijtimoiy tarmoq"><ruby>交流<rt>こうりゅう</rt></ruby>サイト</span>は<ruby>女子<rt>じょし</rt></ruby>に<ruby>多<rt>おお</rt></ruby>かった。</p>

<p><span class="cn-word" data-tr="qiziq"><ruby>面白<rt>おもしろ</rt></ruby>い</span><span class="cn-word" data-tr="natija"><ruby>結果<rt>けっか</rt></ruby></span>もあった。「スマホを<ruby>減<rt>へ</rt></ruby>らしたいか」という<ruby>質問<rt>しつもん</rt></ruby>に<ruby>対<rt>たい</rt></ruby>して、<ruby>二十五人<rt>にじゅうごにん</rt></ruby>が「はい」と<ruby>答<rt>こた</rt></ruby>えた。<ruby>使<rt>つか</rt></ruby>う<ruby>時間<rt>じかん</rt></ruby>が<ruby>長<rt>なが</rt></ruby>いのに<ruby>対<rt>たい</rt></ruby>して、<ruby>自分<rt>じぶん</rt></ruby>では<ruby>長<rt>なが</rt></ruby>すぎると<ruby>思<rt>おも</rt></ruby>っている<ruby>人<rt>ひと</rt></ruby>が<ruby>多<rt>おお</rt></ruby>い。</p>

<p><ruby>自由<rt>じゆう</rt></ruby>に<ruby>書<rt>か</rt></ruby>く<ruby>欄<rt>らん</rt></ruby>もあった。「<ruby>朝<rt>あさ</rt></ruby><ruby>起<rt>お</rt></ruby>きてすぐ<ruby>見<rt>み</rt></ruby>てしまう」「<ruby>宿題<rt>しゅくだい</rt></ruby>の<ruby>時<rt>とき</rt></ruby>そばに<ruby>置<rt>お</rt></ruby>くと<ruby>進<rt>すす</rt></ruby>まない」という<ruby>声<rt>こえ</rt></ruby>が<ruby>多<rt>おお</rt></ruby>かった。<ruby>一方<rt>いっぽう</rt></ruby>で、<span class="cn-word" data-tr="foydali tomoni"><ruby>良<rt>よ</rt></ruby>い<ruby>点<rt>てん</rt></ruby></span>についての<ruby>意見<rt>いけん</rt></ruby>もあった。<ruby>遠<rt>とお</rt></ruby>くの<ruby>祖父母<rt>そふぼ</rt></ruby>と<ruby>話<rt>はな</rt></ruby>せる、<ruby>分<rt>わ</rt></ruby>からない<ruby>言葉<rt>ことば</rt></ruby>をすぐ<ruby>調<rt>しら</rt></ruby>べられる、という<ruby>答<rt>こた</rt></ruby>えである。</p>

<p>この<ruby>意見<rt>いけん</rt></ruby>に<ruby>対<rt>たい</rt></ruby>して、<ruby>先生<rt>せんせい</rt></ruby>は「<ruby>道具<rt>どうぐ</rt></ruby>そのものは<ruby>悪<rt>わる</rt></ruby>くない」と<ruby>話<rt>はな</rt></ruby>した。</p>

<p><ruby>先生<rt>せんせい</rt></ruby>は、スマホに<ruby>関<rt>かん</rt></ruby>する<ruby>本<rt>ほん</rt></ruby>を<ruby>図書館<rt>としょかん</rt></ruby>から<ruby>借<rt>か</rt></ruby>りてきた。そこには、<ruby>夜<rt>よる</rt></ruby>の<ruby>光<rt>ひかり</rt></ruby>が<ruby>眠<rt>ねむ</rt></ruby>りに<ruby>悪<rt>わる</rt></ruby>いと<ruby>書<rt>か</rt></ruby>いてあった。</p>

<p><ruby>最後<rt>さいご</rt></ruby>に、クラスで<ruby>一<rt>ひと</rt></ruby>つの<span class="cn-word" data-tr="qoida"><ruby>決<rt>き</rt></ruby>まり</span>を<ruby>作<rt>つく</rt></ruby>った。<ruby>夜<rt>よる</rt></ruby><ruby>十時<rt>じゅうじ</rt></ruby><ruby>以降<rt>いこう</rt></ruby>はスマホを<ruby>机<rt>つくえ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に<ruby>置<rt>お</rt></ruby>く、というものである。<ruby>来月<rt>らいげつ</rt></ruby>、この<ruby>決<rt>き</rt></ruby>まりについてもう<ruby>一度<rt>いちど</rt></ruby><ruby>調<rt>しら</rt></ruby>べる<ruby>予定<rt>よてい</rt></ruby>だ。</p>''',
        "questions": [
            {
                "text": "<ruby>一日<rt>いちにち</rt></ruby>の<ruby>時間<rt>じかん</rt></ruby>についての<ruby>質問<rt>しつもん</rt></ruby>に<ruby>対<rt>たい</rt></ruby>して、<ruby>何人<rt>なんにん</rt></ruby>が「<ruby>三時間<rt>さんじかん</rt></ruby><ruby>以上<rt>いじょう</rt></ruby>」と<ruby>答<rt>こた</rt></ruby>えましたか。",
                "choices": [
                    "<ruby>十八人<rt>じゅうはちにん</rt></ruby>",
                    "<ruby>三人<rt>さんにん</rt></ruby>",
                    "<ruby>二十五人<rt>にじゅうごにん</rt></ruby>",
                    "<ruby>三十二人<rt>さんじゅうににん</rt></ruby>",
                ],
                "answer": 0,
                "explanation": "Oʻttiz ikki kishidan oʻn sakkiztasi "
                               "— yarmidan koʻpi. Yigirma besh — "
                               "«kamaytirmoqchimisiz?» degan boshqa "
                               "savolning javobi.",
            },
            {
                "text": "<ruby>動画<rt>どうが</rt></ruby>と<ruby>本<rt>ほん</rt></ruby>について、<ruby>正<rt>ただ</rt></ruby>しいのはどれですか。",
                "choices": [
                    "<ruby>動画<rt>どうが</rt></ruby>を<ruby>見<rt>み</rt></ruby>る<ruby>人<rt>ひと</rt></ruby>が<ruby>多<rt>おお</rt></ruby>いのに<ruby>対<rt>たい</rt></ruby>して、<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>む<ruby>人<rt>ひと</rt></ruby>は<ruby>少<rt>すく</rt></ruby>ない",
                    "<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>む<ruby>人<rt>ひと</rt></ruby>のほうが<ruby>多<rt>おお</rt></ruby>い",
                    "どちらも<ruby>同<rt>おな</rt></ruby>じくらいだった",
                    "だれも<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>まなかった",
                ],
                "answer": 0,
                "explanation": "Matn ikkisini ataylab yonma-yon "
                               "qoʻyadi — bu のに対して ning "
                               "qarshi qoʻyish maʼnosi. Kitob "
                               "oʻqiydiganlar uch kishi edi, "
                               "yaʼni yoʻq emas.",
            },
            {
                "text": "クラスはどんな<ruby>決<rt>き</rt></ruby>まりを<ruby>作<rt>つく</rt></ruby>りましたか。",
                "choices": [
                    "<ruby>夜<rt>よる</rt></ruby><ruby>十時<rt>じゅうじ</rt></ruby><ruby>以降<rt>いこう</rt></ruby>はスマホを<ruby>机<rt>つくえ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に<ruby>置<rt>お</rt></ruby>く",
                    "スマホを<ruby>学校<rt>がっこう</rt></ruby>に<ruby>持<rt>も</rt></ruby>ってこない",
                    "<ruby>動画<rt>どうが</rt></ruby>を<ruby>見<rt>み</rt></ruby>ない",
                    "<ruby>毎日<rt>まいにち</rt></ruby><ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>む",
                ],
                "answer": 0,
                "explanation": "Taqiq emas — telefonni kechqurun "
                               "oʻntadan keyin stol ustiga qoʻyish. "
                               "Keyingi oy shu qoida yuzasidan "
                               "yana soʻrov oʻtkaziladi.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "ちいさいながらも",
        "summary": (
            "PJ-90 matni. Bekat yonidagi kichkina kitob doʻkoni: "
            "atrofdagi doʻkonlar yopilib borayotganiga qaramay, u "
            "hamon ochiq. Egasi nega davom etayotganini bitta jumla "
            "bilan tushuntiradi."
        ),
        "order":   90,
        "grammar": [
            {
                "pattern":  "ます-oʻzagi / sifat + ながらも",
                "meaning":  "«… ga qaramay, … boʻlsa-da». PJ-38 dagi "
                            "ながら ga も qoʻshilsa, «bir vaqtda» "
                            "degan maʼno qarama-qarshilikka aylanadi.",
                "examples": ["<ruby>小<rt>ちい</rt></ruby>さいながらも、いい<ruby>店<rt>みせ</rt></ruby>だ。",
                             "<ruby>知<rt>し</rt></ruby>っていながらも<ruby>言<rt>い</rt></ruby>わなかった。"],
            },
            {
                "pattern":  "ます-oʻzagi + つつ · つつも",
                "meaning":  "ながら va ながらも ning kitobiy egizagi. "
                            "Faqat feʼlga ulanadi, sifatga emas.",
                "examples": ["<ruby>迷<rt>まよ</rt></ruby>いつつも、<ruby>続<rt>つづ</rt></ruby>けている。"],
            },
            {
                "pattern":  "ます-oʻzagi + つつある",
                "meaning":  "«… boʻlib bormoqda» — qarshilik emas, "
                            "jarayon. Gazeta va ilmiy matnning soʻzi.",
                "examples": ["<ruby>本屋<rt>ほんや</rt></ruby>は<ruby>減<rt>へ</rt></ruby>りつつある。"],
            },
        ],
        "body": '''<p><ruby>駅<rt>えき</rt></ruby>の<ruby>北口<rt>きたぐち</rt></ruby>を<ruby>出<rt>で</rt></ruby>て<ruby>右<rt>みぎ</rt></ruby>へ<ruby>曲<rt>ま</rt></ruby>がると、<ruby>小<rt>ちい</rt></ruby>さな<ruby>本屋<rt>ほんや</rt></ruby>がある。<ruby>店<rt>みせ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>は<ruby>三人<rt>さんにん</rt></ruby>で<span class="cn-word" data-tr="toʻlib qoladi"><ruby>一杯<rt>いっぱい</rt></ruby>になる</span>ほどだ。<ruby>小<rt>ちい</rt></ruby>さいながらも、この<ruby>店<rt>みせ</rt></ruby>は<ruby>五十年<rt>ごじゅうねん</rt></ruby><ruby>続<rt>つづ</rt></ruby>いている。</p>

<p><ruby>日本<rt>にほん</rt></ruby><ruby>中<rt>じゅう</rt></ruby>で、まちの<ruby>本屋<rt>ほんや</rt></ruby>は<ruby>減<rt>へ</rt></ruby>りつつある。<ruby>駅<rt>えき</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>にあった<ruby>大<rt>おお</rt></ruby>きな<ruby>店<rt>みせ</rt></ruby>も、<ruby>去年<rt>きょねん</rt></ruby><ruby>閉<rt>し</rt></ruby>まった。それでも、この<ruby>店<rt>みせ</rt></ruby>の<span class="cn-word" data-tr="eshik pardasi"><ruby>暖簾<rt>のれん</rt></ruby></span>は<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>出<rt>で</rt></ruby>ている。</p>

<p><ruby>店<rt>みせ</rt></ruby>の<ruby>主人<rt>しゅじん</rt></ruby>は<ruby>七十歳<rt>ななじゅっさい</rt></ruby>の<ruby>山田<rt>やまだ</rt></ruby>さんだ。<ruby>山田<rt>やまだ</rt></ruby>さんは<ruby>父親<rt>ちちおや</rt></ruby>からこの<ruby>店<rt>みせ</rt></ruby>を<span class="cn-word" data-tr="meros qilib oldi"><ruby>受<rt>う</rt></ruby>け<ruby>継<rt>つ</rt></ruby>いだ</span>。<ruby>若<rt>わか</rt></ruby>いころは<ruby>別<rt>べつ</rt></ruby>の<ruby>仕事<rt>しごと</rt></ruby>をしたいと<ruby>思<rt>おも</rt></ruby>いつつも、<ruby>結局<rt>けっきょく</rt></ruby>ここに<ruby>残<rt>のこ</rt></ruby>った。</p>

<p><ruby>棚<rt>たな</rt></ruby>は<ruby>狭<rt>せま</rt></ruby>いながらも、よく<ruby>選<rt>えら</rt></ruby>ばれている。<ruby>新<rt>あたら</rt></ruby>しい<ruby>本<rt>ほん</rt></ruby>だけではない。<ruby>三十年前<rt>さんじゅうねんまえ</rt></ruby>の<ruby>本<rt>ほん</rt></ruby>も<ruby>並<rt>なら</rt></ruby>んでいる。</p>

<p><strong>やまだ:</strong> <ruby>売<rt>う</rt></ruby>れないと<ruby>分<rt>わ</rt></ruby>かっていながらも、<ruby>置<rt>お</rt></ruby>いておく<ruby>本<rt>ほん</rt></ruby>があります。だれか<ruby>一人<rt>ひとり</rt></ruby>のために<ruby>待<rt>ま</rt></ruby>っている<ruby>本<rt>ほん</rt></ruby>です。</p>

<p><ruby>去年<rt>きょねん</rt></ruby>の<ruby>冬<rt>ふゆ</rt></ruby>、<ruby>一人<rt>ひとり</rt></ruby>の<ruby>女子<rt>じょし</rt></ruby><ruby>学生<rt>がくせい</rt></ruby>が<ruby>店<rt>みせ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>ってきた。<ruby>祖母<rt>そぼ</rt></ruby>が<ruby>昔<rt>むかし</rt></ruby><ruby>読<rt>よ</rt></ruby>んでいた<ruby>本<rt>ほん</rt></ruby>を<ruby>探<rt>さが</rt></ruby>していた。<ruby>題名<rt>だいめい</rt></ruby>も<ruby>作者<rt>さくしゃ</rt></ruby>も<ruby>分<rt>わ</rt></ruby>からなかった。<ruby>山田<rt>やまだ</rt></ruby>さんは<span class="cn-word" data-tr="bir soatcha"><ruby>一時間<rt>いちじかん</rt></ruby>ほど</span><ruby>話<rt>はな</rt></ruby>を<ruby>聞<rt>き</rt></ruby>き、<ruby>棚<rt>たな</rt></ruby>の<ruby>奥<rt>おく</rt></ruby>から<ruby>一冊<rt>いっさつ</rt></ruby><ruby>出<rt>だ</rt></ruby>してきた。それが<ruby>探<rt>さが</rt></ruby>していた<ruby>本<rt>ほん</rt></ruby>だった。</p>

<p>その<ruby>日<rt>ひ</rt></ruby>から、<ruby>女子<rt>じょし</rt></ruby><ruby>学生<rt>がくせい</rt></ruby>は<ruby>月<rt>つき</rt></ruby>に<ruby>一度<rt>いちど</rt></ruby>この<ruby>店<rt>みせ</rt></ruby>へ<ruby>来<rt>く</rt></ruby>るようになった。<ruby>大<rt>おお</rt></ruby>きな<ruby>店<rt>みせ</rt></ruby>のほうが<ruby>安<rt>やす</rt></ruby>いと<ruby>知<rt>し</rt></ruby>りつつも、ここで<ruby>買<rt>か</rt></ruby>う。<ruby>本<rt>ほん</rt></ruby>を<ruby>選<rt>えら</rt></ruby>ぶ<ruby>時間<rt>じかん</rt></ruby>が<ruby>好<rt>す</rt></ruby>きだからだ。</p>

<p><span class="cn-word" data-tr="ijara haqi"><ruby>家賃<rt>やちん</rt></ruby></span>は<ruby>上<rt>あ</rt></ruby>がりつつある。<ruby>客<rt>きゃく</rt></ruby>は<ruby>少<rt>すく</rt></ruby>ないながらも、<ruby>毎日<rt>まいにち</rt></ruby><ruby>同<rt>おな</rt></ruby>じ<ruby>顔<rt>かお</rt></ruby>が<ruby>何人<rt>なんにん</rt></ruby>か<ruby>来<rt>く</rt></ruby>る。</p>

<p><ruby>山田<rt>やまだ</rt></ruby>さんは、いつまで<ruby>続<rt>つづ</rt></ruby>けられるか<ruby>分<rt>わ</rt></ruby>からないと<ruby>言<rt>い</rt></ruby>う。それでも<ruby>毎朝<rt>まいあさ</rt></ruby>、<ruby>六時<rt>ろくじ</rt></ruby>に<ruby>店<rt>みせ</rt></ruby>を<ruby>開<rt>あ</rt></ruby>ける。</p>''',
        "questions": [
            {
                "text": "この<ruby>本屋<rt>ほんや</rt></ruby>はどんな<ruby>店<rt>みせ</rt></ruby>ですか。",
                "choices": [
                    "<ruby>小<rt>ちい</rt></ruby>さいながらも<ruby>五十年<rt>ごじゅうねん</rt></ruby><ruby>続<rt>つづ</rt></ruby>いている<ruby>店<rt>みせ</rt></ruby>",
                    "<ruby>駅<rt>えき</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>にある<ruby>大<rt>おお</rt></ruby>きな<ruby>店<rt>みせ</rt></ruby>",
                    "<ruby>去年<rt>きょねん</rt></ruby><ruby>開<rt>ひら</rt></ruby>いたばかりの<ruby>店<rt>みせ</rt></ruby>",
                    "<ruby>新<rt>あたら</rt></ruby>しい<ruby>本<rt>ほん</rt></ruby>しか<ruby>置<rt>お</rt></ruby>かない<ruby>店<rt>みせ</rt></ruby>",
                ],
                "answer": 0,
                "explanation": "Uch kishi sigʻsa toʻlib qoladigan "
                               "doʻkon, lekin ellik yildan beri "
                               "ochiq. Bekat oldidagi katta doʻkon "
                               "esa oʻtgan yili yopildi.",
            },
            {
                "text": "<ruby>山田<rt>やまだ</rt></ruby>さんはどうして<ruby>売<rt>う</rt></ruby>れない<ruby>本<rt>ほん</rt></ruby>を<ruby>置<rt>お</rt></ruby>いておきますか。",
                "choices": [
                    "だれか<ruby>一人<rt>ひとり</rt></ruby>のために<ruby>待<rt>ま</rt></ruby>っている<ruby>本<rt>ほん</rt></ruby>だから",
                    "<ruby>捨<rt>す</rt></ruby>てる<ruby>場所<rt>ばしょ</rt></ruby>がないから",
                    "<ruby>父親<rt>ちちおや</rt></ruby>に<ruby>言<rt>い</rt></ruby>われたから",
                    "<ruby>高<rt>たか</rt></ruby>く<ruby>売<rt>う</rt></ruby>れるから",
                ],
                "answer": 0,
                "explanation": "Sotilmasligini bila turib ham "
                               "qoldiradi — chunki oʻsha kitob "
                               "bittagina odamni kutyapti. Keyingi "
                               "xat boshi bu gapni voqea bilan "
                               "isbotlaydi.",
            },
            {
                "text": "<ruby>去年<rt>きょねん</rt></ruby>の<ruby>冬<rt>ふゆ</rt></ruby>、<ruby>女子<rt>じょし</rt></ruby><ruby>学生<rt>がくせい</rt></ruby>はどうなりましたか。",
                "choices": [
                    "<ruby>探<rt>さが</rt></ruby>していた<ruby>本<rt>ほん</rt></ruby>が<ruby>見<rt>み</rt></ruby>つかった",
                    "<ruby>本<rt>ほん</rt></ruby>が<ruby>見<rt>み</rt></ruby>つからなかった",
                    "<ruby>題名<rt>だいめい</rt></ruby>を<ruby>思<rt>おも</rt></ruby>い<ruby>出<rt>だ</rt></ruby>した",
                    "<ruby>別<rt>べつ</rt></ruby>の<ruby>店<rt>みせ</rt></ruby>へ<ruby>行<rt>い</rt></ruby>った",
                ],
                "answer": 0,
                "explanation": "Na nomini, na muallifini bilardi. "
                               "Yamada bir soatcha gapini "
                               "tingladi va javondan aynan oʻsha "
                               "kitobni chiqardi.",
            },
        ],
    },
]
