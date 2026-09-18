# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-97 … PJ-100. SHELFNING OXIRGI TOʻRTTASI.

Uzunlik Blok F tasmasida (190–270 soʻz).

Shakl navbati: 97 — XAT (darsning oʻz qolipi, 拝啓…敬具 bilan),
98 — buvi va nabira hikoyasi (maqollar matn ichida yashaydi),
99 — til haqidagi ustun (である体), 100 — yakuniy ocherk.
Oldingi batchda oilaviy hikoya / sport reportaji / gazeta xabari
boʻlgan edi.

Registr:
    97 — 丁寧体, boshdan oxirigacha (xat oʻz registrini tanlab,
         oxirigacha ushlaydi — toc ruxsati).
    98 — 普通体 hikoya, «» ichidagi gap 丁寧体.
    99 — である体 (PJ-96 dan keyin erkin), chunki bu ustun.
    100 — 普通体 ocherk.

⚠️ CUMULATIVE:
    97 — 拝啓・敬具, 時候の挨拶, お世話になっております erkin.
         四字熟語・ことわざ (98), 和語・漢語・外来語 (99) YOʻQ.
    98 — + maqollar va toʻrt belgili iboralar. Qatlam atamalari
         hali YOʻQ.
    99 — + 和語・漢語・外来語. Hammasi erkin.
    100 — hammasi erkin; yangi grammatika kiritilmaydi.

⚠️ 〜のです ham, 〜んです ham, 意向形 ham bu shelfda yozilmaydi —
100-matnda «やめようと思った» emas, «やめたいと思った».

⚠️ 99-matn oʻylab topilgan maktab haqida; haqiqiy joy nomi yoʻq.

⚠️ AUDIODAN OLDIN NARRATSIYANI OʻQIB CHIQING — <rt> va teglar
olib tashlangan holda. 97-matndagi 拝啓 va 敬具 ovoz chiqarib
oʻqiladi, va bu ataylab: oʻquvchi xat qolipini quloq bilan ham
eshitadi.

Audio (navbat bilan, oldingi batch 96 da Nanami bilan tugagan edi):
    --only 97  --voice ja-JP-KeitaNeural
    --only 98  --voice ja-JP-NanamiNeural
    --only 99  --voice ja-JP-KeitaNeural
    --only 100 --voice ja-JP-NanamiNeural

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_97_100.py --author=prime
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
        "title":   "せんせいへの てがみ",
        "summary": (
            "PJ-97 matni. Ikki yil oldin bitirgan Munira ustoziga xat "
            "yozadi: birinchi yaponcha telefon suhbati, va oʻshanda "
            "esiga tushgan bitta gap. Xatning butun qolipi — 拝啓 dan "
            "敬具 gacha — matnning oʻzida koʻrinadi."
        ),
        "order":   97,
        "grammar": [
            {
                "pattern":  "<ruby>拝啓<rt>はいけい</rt></ruby> … <ruby>敬具<rt>けいぐ</rt></ruby>",
                "meaning":  "Qogʻoz xatning boshi va oxiri — juftlik. Birini "
                            "yozsangiz, ikkinchisi majburiy. Qisqa xatda esa "
                            "前略 … 草々 juftligi ishlatiladi.",
                "examples": ["<ruby>拝啓<rt>はいけい</rt></ruby>　<ruby>桜<rt>さくら</rt></ruby>の<ruby>花<rt>はな</rt></ruby>が<ruby>美<rt>うつく</rt></ruby>しい<ruby>季節<rt>きせつ</rt></ruby>となりました。",
                             "<ruby>敬具<rt>けいぐ</rt></ruby>"],
            },
            {
                "pattern":  "<ruby>時候<rt>じこう</rt></ruby>の<ruby>挨拶<rt>あいさつ</rt></ruby>",
                "meaning":  "Mavsum salomi — xat ishga oʻtishdan oldin fasldan "
                            "boshlanadi, keyin odamning ahvoli soʻraladi. "
                            "Oʻzbek xatidagi hol-ahvol soʻrashning jufti.",
                "examples": ["<ruby>朝晩<rt>あさばん</rt></ruby>はまだ<ruby>冷<rt>ひ</rt></ruby>えます。",
                             "<ruby>先生<rt>せんせい</rt></ruby>はお<ruby>元気<rt>げんき</rt></ruby>でいらっしゃいますか。"],
            },
            {
                "pattern":  "〜てくださる · 〜ていただく",
                "meaning":  "Yuqoridagi odamning siz uchun qilgan ishi. "
                            "くださる — u qildi; いただく — men olдim. "
                            "Xatda minnatdorchilik shu ikkovi bilan aytiladi.",
                "examples": ["<ruby>何度<rt>なんど</rt></ruby>も<ruby>言<rt>い</rt></ruby>ってくださいました。",
                             "お<ruby>話<rt>はな</rt></ruby>しさせてください。"],
            },
        ],
        "body": '''<p><ruby>拝啓<rt>はいけい</rt></ruby>　<ruby>桜<rt>さくら</rt></ruby>の<ruby>花<rt>はな</rt></ruby>が<ruby>美<rt>うつく</rt></ruby>しい<ruby>季節<rt>きせつ</rt></ruby>となりました。<ruby>先生<rt>せんせい</rt></ruby>はお<ruby>元気<rt>げんき</rt></ruby>でいらっしゃいますか。</p>

<p><span class="cn-word" data-tr="uzoq vaqt xabar bermadim">ご<ruby>無沙汰<rt>ぶさた</rt></ruby>しております</span>。<ruby>二年前<rt>にねんまえ</rt></ruby>に<ruby>卒業<rt>そつぎょう</rt></ruby>したムニラです。</p>

<p>あのころ、<ruby>私<rt>わたし</rt></ruby>は<ruby>日本語<rt>にほんご</rt></ruby>が<span class="cn-word" data-tr="uddalay olmaydigan"><ruby>苦手<rt>にがて</rt></ruby></span>でした。<ruby>教室<rt>きょうしつ</rt></ruby>で<ruby>一度<rt>いちど</rt></ruby>も<ruby>手<rt>て</rt></ruby>を<ruby>上<rt>あ</rt></ruby>げませんでした。<ruby>先生<rt>せんせい</rt></ruby>は「<ruby>間違<rt>まちが</rt></ruby>えてもいいですよ」と<ruby>何度<rt>なんど</rt></ruby>も<ruby>言<rt>い</rt></ruby>ってくださいました。</p>

<p><ruby>今<rt>いま</rt></ruby>、<ruby>私<rt>わたし</rt></ruby>は<ruby>町<rt>まち</rt></ruby>の<ruby>小<rt>ちい</rt></ruby>さな<ruby>会社<rt>かいしゃ</rt></ruby>で<ruby>働<rt>はたら</rt></ruby>いております。<ruby>先月<rt>せんげつ</rt></ruby>、<ruby>初<rt>はじ</rt></ruby>めて<ruby>日本<rt>にほん</rt></ruby>のお<ruby>客様<rt>きゃくさま</rt></ruby>と<ruby>電話<rt>でんわ</rt></ruby>で<ruby>話<rt>はな</rt></ruby>しました。</p>

<p><span class="cn-word" data-tr="hayajonlandim"><ruby>緊張<rt>きんちょう</rt></ruby>しました</span>が、<ruby>最後<rt>さいご</rt></ruby>まで<ruby>日本語<rt>にほんご</rt></ruby>で<ruby>話<rt>はな</rt></ruby>せました。<ruby>三度<rt>さんど</rt></ruby><ruby>間違<rt>まちが</rt></ruby>えました。でも、<ruby>相手<rt>あいて</rt></ruby>は<ruby>最後<rt>さいご</rt></ruby>まで<ruby>聞<rt>き</rt></ruby>いてくださいました。</p>

<p><ruby>電話<rt>でんわ</rt></ruby>を<ruby>切<rt>き</rt></ruby>ったあと、<ruby>先生<rt>せんせい</rt></ruby>の<span class="cn-word" data-tr="bitta gap"><ruby>一言<rt>ひとこと</rt></ruby></span>を<ruby>思<rt>おも</rt></ruby>い<ruby>出<rt>だ</rt></ruby>しました。<ruby>間違<rt>まちが</rt></ruby>えてもいい。あの<ruby>言葉<rt>ことば</rt></ruby>がなかったら、<ruby>私<rt>わたし</rt></ruby>は<ruby>話<rt>はな</rt></ruby>さなかったと<ruby>思<rt>おも</rt></ruby>います。</p>

<p><ruby>今<rt>いま</rt></ruby>でも<ruby>日本語<rt>にほんご</rt></ruby>は<ruby>上手<rt>じょうず</rt></ruby>ではありません。<ruby>辞書<rt>じしょ</rt></ruby>を<ruby>毎日<rt>まいにち</rt></ruby><ruby>開<rt>ひら</rt></ruby>きます。でも、もう<span class="cn-word" data-tr="qoʻrqinchli emas"><ruby>怖<rt>こわ</rt></ruby>くありません</span>。</p>

<p><ruby>桜<rt>さくら</rt></ruby>が<ruby>咲<rt>さ</rt></ruby>くころ、<ruby>学校<rt>がっこう</rt></ruby>へ<span class="cn-word" data-tr="bormoq (kamtarona)"><ruby>伺<rt>うかが</rt></ruby>いたい</span>と<ruby>思<rt>おも</rt></ruby>っております。その<ruby>時<rt>とき</rt></ruby>は、ぜひお<ruby>話<rt>はな</rt></ruby>しさせてください。</p>

<p><ruby>朝晩<rt>あさばん</rt></ruby>はまだ<span class="cn-word" data-tr="sovuq boʻlmoq"><ruby>冷<rt>ひ</rt></ruby>えます</span>。どうぞお<ruby>体<rt>からだ</rt></ruby>を<ruby>大切<rt>たいせつ</rt></ruby>に<span class="cn-word" data-tr="qilmoq (hurmatli)">なさって</span>ください。</p>

<p><ruby>敬具<rt>けいぐ</rt></ruby></p>''',
        "questions": [
            {
                "text": "ムニラは<ruby>今<rt>いま</rt></ruby><ruby>何<rt>なに</rt></ruby>をしていますか。",
                "choices": [
                    "<ruby>町<rt>まち</rt></ruby>の<ruby>小<rt>ちい</rt></ruby>さな<ruby>会社<rt>かいしゃ</rt></ruby>で<ruby>働<rt>はたら</rt></ruby>いています",
                    "<ruby>学校<rt>がっこう</rt></ruby>で<ruby>教<rt>おし</rt></ruby>えています",
                    "<ruby>日本<rt>にほん</rt></ruby>に<ruby>住<rt>す</rt></ruby>んでいます",
                    "まだ<ruby>高校<rt>こうこう</rt></ruby>の<ruby>学生<rt>がくせい</rt></ruby>です",
                ],
                "answer": 0,
                "explanation": "Xatda aniq aytilgan: u shaharchadagi "
                               "kichik kompaniyada ishlaydi. Yaponiyaga "
                               "ketgani haqida hech narsa yozilmagan — "
                               "mijoz bilan telefonda gaplashgan.",
            },
            {
                "text": "<ruby>先生<rt>せんせい</rt></ruby>はどんな<ruby>言葉<rt>ことば</rt></ruby>を<ruby>何度<rt>なんど</rt></ruby>も<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "<ruby>間違<rt>まちが</rt></ruby>えてもいい",
                    "<ruby>毎日<rt>まいにち</rt></ruby><ruby>勉強<rt>べんきょう</rt></ruby>しなさい",
                    "<ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きなさい",
                    "<ruby>手<rt>て</rt></ruby>を<ruby>上<rt>あ</rt></ruby>げなさい",
                ],
                "answer": 0,
                "explanation": "«Xato qilsang ham boʻladi» — ustoz "
                               "shuni takrorlagan. Va aynan shu gap "
                               "ikki yildan keyin, telefon suhbatidan "
                               "soʻng esiga tushgan.",
            },
            {
                "text": "この<ruby>手紙<rt>てがみ</rt></ruby>はどうして<ruby>敬具<rt>けいぐ</rt></ruby>で<ruby>終<rt>お</rt></ruby>わりますか。",
                "choices": [
                    "<ruby>拝啓<rt>はいけい</rt></ruby>で<ruby>始<rt>はじ</rt></ruby>まったから",
                    "<ruby>前略<rt>ぜんりゃく</rt></ruby>で<ruby>始<rt>はじ</rt></ruby>まったから",
                    "メールだから",
                    "<ruby>先生<rt>せんせい</rt></ruby>に<ruby>書<rt>か</rt></ruby>いたから",
                ],
                "answer": 0,
                "explanation": "頭語 va 結語 — juftlik. Xat 拝啓 bilan "
                               "boshlangan, demak 敬具 bilan tugashi "
                               "shart. 前略 boshlangan boʻlsa, 草々 "
                               "bilan tugardi.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "いしの うえにも さんねん",
        "summary": (
            "PJ-98 matni. Inom hamma ishni uch kunda tashlab qoʻyadi. "
            "Buvisi unga ikkita maqol aytadi — va bir yildan keyin "
            "nabira bogʻdagi daraxtga qarab, ularning maʼnosini "
            "tushunadi."
        ),
        "order":   98,
        "grammar": [
            {
                "pattern":  "<ruby>三日坊主<rt>みっかぼうず</rt></ruby>",
                "meaning":  "«Uch kunlik rohib» — boshlagan ishini tez "
                            "tashlab qoʻyadigan odam. Oʻzbekcha «bir kunlik "
                            "gʻayrat». Diqqat: oʻqilishi kun'yomi — istisno.",
                "examples": ["<ruby>三日坊主<rt>みっかぼうず</rt></ruby>だな。"],
            },
            {
                "pattern":  "<ruby>石<rt>いし</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>にも<ruby>三年<rt>さんねん</rt></ruby>",
                "meaning":  "«Toshning ustida ham uch yil» — sovuq tosh ham "
                            "uch yil oʻtirsang isiydi. Oʻzbekcha jufti: "
                            "«sabr tagi — sariq oltin».",
                "examples": ["<ruby>冷<rt>つめ</rt></ruby>たい<ruby>石<rt>いし</rt></ruby>でも、<ruby>三年<rt>さんねん</rt></ruby><ruby>座<rt>すわ</rt></ruby>れば<ruby>温<rt>あたた</rt></ruby>かくなる。"],
            },
            {
                "pattern":  "<ruby>塵<rt>ちり</rt></ruby>も<ruby>積<rt>つ</rt></ruby>もれば<ruby>山<rt>やま</rt></ruby>となる",
                "meaning":  "«Chang ham yigʻilsa togʻ boʻladi» — kichik "
                            "narsalarning toʻplanishi haqida. Oʻzbekcha "
                            "jufti: «tomchi tomchi koʻl boʻlar».",
                "examples": ["<ruby>一日<rt>いちにち</rt></ruby><ruby>十分<rt>じゅっぷん</rt></ruby>でいい。"],
            },
        ],
        "body": '''<p>イノムは<ruby>何<rt>なん</rt></ruby>でもすぐに<ruby>始<rt>はじ</rt></ruby>める。そして<ruby>三日<rt>みっか</rt></ruby>でやめる。</p>

<p>ギターは<ruby>三日<rt>みっか</rt></ruby>。<ruby>絵<rt>え</rt></ruby>は<ruby>三日<rt>みっか</rt></ruby>。<ruby>走<rt>はし</rt></ruby>ることも<ruby>三日<rt>みっか</rt></ruby>だった。</p>

<p>「<ruby>三日坊主<rt>みっかぼうず</rt></ruby>だな」と<ruby>兄<rt>あに</rt></ruby>が<ruby>笑<rt>わら</rt></ruby>った。イノムは<ruby>怒<rt>おこ</rt></ruby>った。でも、<span class="cn-word" data-tr="javob qaytarolmadi"><ruby>言<rt>い</rt></ruby>い<ruby>返<rt>かえ</rt></ruby>せなかった</span>。</p>

<p>ある<ruby>日<rt>ひ</rt></ruby>、<ruby>祖母<rt>そぼ</rt></ruby>の<ruby>家<rt>いえ</rt></ruby>へ<ruby>行<rt>い</rt></ruby>った。<ruby>祖母<rt>そぼ</rt></ruby>は<ruby>庭<rt>にわ</rt></ruby>で<ruby>小<rt>ちい</rt></ruby>さな<ruby>木<rt>き</rt></ruby>に<ruby>水<rt>みず</rt></ruby>をやっていた。</p>

<p>「おばあちゃん、この<ruby>木<rt>き</rt></ruby>、いつ<ruby>大<rt>おお</rt></ruby>きくなるの」</p>

<p>「<ruby>十年<rt>じゅうねん</rt></ruby>かかりますよ」と<ruby>祖母<rt>そぼ</rt></ruby>は<ruby>言<rt>い</rt></ruby>った。「<ruby>石<rt>いし</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>にも<ruby>三年<rt>さんねん</rt></ruby>、という<ruby>言葉<rt>ことば</rt></ruby>があります。<ruby>冷<rt>つめ</rt></ruby>たい<ruby>石<rt>いし</rt></ruby>でも、<ruby>三年<rt>さんねん</rt></ruby><ruby>座<rt>すわ</rt></ruby>れば<ruby>温<rt>あたた</rt></ruby>かくなるでしょう」</p>

<p>イノムは<span class="cn-word" data-tr="jim qoldi"><ruby>黙<rt>だま</rt></ruby>っていた</span>。<ruby>三年<rt>さんねん</rt></ruby>は<ruby>長<rt>なが</rt></ruby>い。</p>

<p><ruby>祖母<rt>そぼ</rt></ruby>は<ruby>水<rt>みず</rt></ruby>をやりながら<ruby>言<rt>い</rt></ruby>った。「わたしもこの<ruby>木<rt>き</rt></ruby>を<ruby>八年<rt>はちねん</rt></ruby><span class="cn-word" data-tr="oʻstirmoq"><ruby>育<rt>そだ</rt></ruby>てています</span>。<ruby>去年<rt>きょねん</rt></ruby>、<ruby>初<rt>はじ</rt></ruby>めて<ruby>花<rt>はな</rt></ruby>が<ruby>咲<rt>さ</rt></ruby>きました」</p>

<p>「<ruby>毎日<rt>まいにち</rt></ruby><ruby>全部<rt>ぜんぶ</rt></ruby>やらなくてもいいですよ」と<ruby>祖母<rt>そぼ</rt></ruby>は<ruby>続<rt>つづ</rt></ruby>けた。「<ruby>塵<rt>ちり</rt></ruby>も<ruby>積<rt>つ</rt></ruby>もれば<ruby>山<rt>やま</rt></ruby>となる。<ruby>一日<rt>いちにち</rt></ruby><ruby>十分<rt>じゅっぷん</rt></ruby>でいいんですから」</p>

<p>その<ruby>日<rt>ひ</rt></ruby>から、イノムは<ruby>毎日<rt>まいにち</rt></ruby><ruby>十分<rt>じゅっぷん</rt></ruby>だけギターを<ruby>触<rt>さわ</rt></ruby>った。<ruby>上手<rt>じょうず</rt></ruby>にならない<ruby>日<rt>ひ</rt></ruby>もあった。やめたくなる<ruby>日<rt>ひ</rt></ruby>もあった。</p>

<p><ruby>一年<rt>いちねん</rt></ruby>たった。イノムは<ruby>祖母<rt>そぼ</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>で<ruby>一曲<rt>いっきょく</rt></ruby><span class="cn-word" data-tr="chalmoq (torli asbob)"><ruby>弾<rt>ひ</rt></ruby>いた</span>。<ruby>短<rt>みじか</rt></ruby>い<ruby>曲<rt>きょく</rt></ruby>だった。でも、<ruby>最後<rt>さいご</rt></ruby>まで<ruby>弾<rt>ひ</rt></ruby>けた。</p>

<p><ruby>祖母<rt>そぼ</rt></ruby>は<ruby>何<rt>なに</rt></ruby>も<ruby>言<rt>い</rt></ruby>わずに、<ruby>庭<rt>にわ</rt></ruby>の<ruby>木<rt>き</rt></ruby>を<span class="cn-word" data-tr="barmogʻi bilan koʻrsatdi"><ruby>指<rt>ゆび</rt></ruby>さした</span>。<ruby>木<rt>き</rt></ruby>は、<ruby>少<rt>すこ</rt></ruby>しだけ<ruby>高<rt>たか</rt></ruby>くなっていた。</p>''',
        "questions": [
            {
                "text": "<ruby>兄<rt>あに</rt></ruby>はイノムを<ruby>何<rt>なに</rt></ruby>と<ruby>呼<rt>よ</rt></ruby>びましたか。",
                "choices": [
                    "<ruby>三日坊主<rt>みっかぼうず</rt></ruby>",
                    "<ruby>初志貫徹<rt>しょしかんてつ</rt></ruby>",
                    "<ruby>一石二鳥<rt>いっせきにちょう</rt></ruby>",
                    "<ruby>十人十色<rt>じゅうにんといろ</rt></ruby>",
                ],
                "answer": 0,
                "explanation": "«Uch kunlik rohib» — hamma ishni "
                               "uch kunda tashlab qoʻyadigan odam. "
                               "初志貫徹 aynan teskarisi: boshlagan "
                               "ishni oxiriga yetkazish.",
            },
            {
                "text": "<ruby>祖母<rt>そぼ</rt></ruby>はイノムに<ruby>何<rt>なに</rt></ruby>と<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "<ruby>一日<rt>いちにち</rt></ruby><ruby>十分<rt>じゅっぷん</rt></ruby>でいい",
                    "<ruby>毎日<rt>まいにち</rt></ruby><ruby>三時間<rt>さんじかん</rt></ruby>やりなさい",
                    "ギターをやめなさい",
                    "<ruby>木<rt>き</rt></ruby>に<ruby>水<rt>みず</rt></ruby>をやりなさい",
                ],
                "answer": 0,
                "explanation": "«Har kuni hammasini qilish shart "
                               "emas, kuniga oʻn daqiqa yetadi» — "
                               "va buni 塵も積もれば山となる maqoli "
                               "bilan asosladi.",
            },
            {
                "text": "<ruby>最後<rt>さいご</rt></ruby>に<ruby>祖母<rt>そぼ</rt></ruby>はどうして<ruby>木<rt>き</rt></ruby>を<ruby>指<rt>ゆび</rt></ruby>さしましたか。",
                "choices": [
                    "<ruby>木<rt>き</rt></ruby>も<ruby>少<rt>すこ</rt></ruby>しずつ<ruby>大<rt>おお</rt></ruby>きくなったから",
                    "<ruby>木<rt>き</rt></ruby>に<ruby>水<rt>みず</rt></ruby>をやってほしかったから",
                    "<ruby>木<rt>き</rt></ruby>が<ruby>病気<rt>びょうき</rt></ruby>だったから",
                    "ギターを<ruby>木<rt>き</rt></ruby>の<ruby>下<rt>した</rt></ruby>に<ruby>置<rt>お</rt></ruby>きたかったから",
                ],
                "answer": 0,
                "explanation": "Buvi hech narsa demadi — daraxtning "
                               "oʻzi javob edi. Bir yilda u ham "
                               "«bir ozgina» oʻsgan, xuddi nabirasi "
                               "kabi. Hikoyaning butun maʼnosi shu "
                               "imo-ishorada.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "みっつの ことば",
        "summary": (
            "PJ-99 matni — til haqidagi ustun, である体da. Maktab "
            "eʼlonlar taxtasida uchta qogʻoz osilgan va uchalasi ham "
            "bitta narsani aytadi, lekin uchta boshqa soʻz bilan. "
            "Nega shunday — matn shuni tushuntiradi."
        ),
        "order":   99,
        "grammar": [
            {
                "pattern":  "<ruby>和語<rt>わご</rt></ruby>・<ruby>漢語<rt>かんご</rt></ruby>・<ruby>外来語<rt>がいらいご</rt></ruby>",
                "meaning":  "Lugʻatning uch qatlami. Kun'yomi bilan oʻqilsa "
                            "和語, on'yomi bilan oʻqilsa 漢語, katakanada "
                            "yozilsa 外来語. Oʻzbekchadagi yigʻilish · "
                            "majlis · miting uchligining aynan oʻzi.",
                "examples": ["<ruby>集<rt>あつ</rt></ruby>まり · <ruby>集会<rt>しゅうかい</rt></ruby> · ミーティング",
                             "<ruby>和語<rt>わご</rt></ruby>はやわらかく、<ruby>話<rt>はな</rt></ruby>し<ruby>言葉<rt>ことば</rt></ruby>に<ruby>向<rt>む</rt></ruby>いている。"],
            },
            {
                "pattern":  "である<ruby>体<rt>たい</rt></ruby>",
                "meaning":  "Yozma-rasmiy uslub — maqola va ustunning tili. "
                            "だ ning oʻrniga である keladi; feʼl va い-sifat "
                            "oʻzgarmaydi. Bu matnning oʻzi shu uslubda.",
                "examples": ["<ruby>生徒会<rt>せいとかい</rt></ruby>の<ruby>紙<rt>かみ</rt></ruby>である。",
                             "<ruby>答<rt>こた</rt></ruby>えは<ruby>言葉<rt>ことば</rt></ruby>の<ruby>層<rt>そう</rt></ruby>である。"],
            },
        ],
        "body": '''<p>ある<ruby>高校<rt>こうこう</rt></ruby>の<span class="cn-word" data-tr="eʼlonlar taxtasi"><ruby>掲示板<rt>けいじばん</rt></ruby></span>に、<ruby>三枚<rt>さんまい</rt></ruby>の<ruby>紙<rt>かみ</rt></ruby>が<span class="cn-word" data-tr="yopishtirilgan"><ruby>貼<rt>は</rt></ruby>ってあった</span>。<ruby>三枚<rt>さんまい</rt></ruby>とも<ruby>同<rt>おな</rt></ruby>じことを<ruby>知<rt>し</rt></ruby>らせている。しかし、<ruby>使<rt>つか</rt></ruby>っている<ruby>言葉<rt>ことば</rt></ruby>が<ruby>違<rt>ちが</rt></ruby>う。</p>

<p><ruby>一枚目<rt>いちまいめ</rt></ruby>には「あしたの<ruby>集<rt>あつ</rt></ruby>まり、わすれないでね」と<ruby>書<rt>か</rt></ruby>いてある。<ruby>生徒会<rt>せいとかい</rt></ruby>の<ruby>紙<rt>かみ</rt></ruby>である。</p>

<p><ruby>二枚目<rt>にまいめ</rt></ruby>は「<ruby>明日<rt>あす</rt></ruby>、<ruby>全校<rt>ぜんこう</rt></ruby><ruby>集会<rt>しゅうかい</rt></ruby>を<ruby>実施<rt>じっし</rt></ruby>する」。<ruby>先生<rt>せんせい</rt></ruby>が<ruby>書<rt>か</rt></ruby>いた<ruby>紙<rt>かみ</rt></ruby>である。</p>

<p><ruby>三枚目<rt>さんまいめ</rt></ruby>は<ruby>英語部<rt>えいごぶ</rt></ruby>のもので、「あしたのミーティング、<ruby>来<rt>き</rt></ruby>てね」とある。</p>

<p><ruby>三<rt>みっ</rt></ruby>つとも<ruby>正<rt>ただ</rt></ruby>しい。<ruby>三<rt>みっ</rt></ruby>つとも<ruby>同<rt>おな</rt></ruby>じ<ruby>意味<rt>いみ</rt></ruby>である。では、<ruby>何<rt>なに</rt></ruby>が<ruby>違<rt>ちが</rt></ruby>うのか。</p>

<p><ruby>答<rt>こた</rt></ruby>えは<ruby>言葉<rt>ことば</rt></ruby>の<span class="cn-word" data-tr="qatlam"><ruby>層<rt>そう</rt></ruby></span>である。<ruby>日本語<rt>にほんご</rt></ruby>の<span class="cn-word" data-tr="soʻz boyligi"><ruby>語彙<rt>ごい</rt></ruby></span>は<ruby>三<rt>みっ</rt></ruby>つの<ruby>層<rt>そう</rt></ruby>からできている。<ruby>和語<rt>わご</rt></ruby>、<ruby>漢語<rt>かんご</rt></ruby>、<ruby>外来語<rt>がいらいご</rt></ruby>である。</p>

<p><ruby>和語<rt>わご</rt></ruby>は<ruby>昔<rt>むかし</rt></ruby>から<ruby>日本<rt>にほん</rt></ruby>にある<ruby>言葉<rt>ことば</rt></ruby>で、<ruby>読<rt>よ</rt></ruby>み<ruby>方<rt>かた</rt></ruby>は<ruby>訓読<rt>くんよ</rt></ruby>みになる。やわらかく、<ruby>話<rt>はな</rt></ruby>し<ruby>言葉<rt>ことば</rt></ruby>に<span class="cn-word" data-tr="mos keladi"><ruby>向<rt>む</rt></ruby>いている</span>。</p>

<p><ruby>漢語<rt>かんご</rt></ruby>は<ruby>中国<rt>ちゅうごく</rt></ruby>から<ruby>入<rt>はい</rt></ruby>った<ruby>言葉<rt>ことば</rt></ruby>で、<ruby>音読<rt>おんよ</rt></ruby>みで<ruby>読<rt>よ</rt></ruby>む。<ruby>短<rt>みじか</rt></ruby>くて、<ruby>意味<rt>いみ</rt></ruby>が<span class="cn-word" data-tr="quyuq, zich"><ruby>濃<rt>こ</rt></ruby>い</span>。だから<ruby>新聞<rt>しんぶん</rt></ruby>の<span class="cn-word" data-tr="sarlavha"><ruby>見出<rt>みだ</rt></ruby>し</span>や<ruby>公式<rt>こうしき</rt></ruby>の<ruby>文章<rt>ぶんしょう</rt></ruby>に<ruby>使<rt>つか</rt></ruby>われる。</p>

<p><ruby>外来語<rt>がいらいご</rt></ruby>はカタカナで<ruby>書<rt>か</rt></ruby>く。<ruby>新<rt>あたら</rt></ruby>しい<ruby>物<rt>もの</rt></ruby>や、<ruby>仕事<rt>しごと</rt></ruby>の<ruby>場面<rt>ばめん</rt></ruby>に<ruby>多<rt>おお</rt></ruby>い。</p>

<p>つまり、<ruby>三枚<rt>さんまい</rt></ruby>の<ruby>紙<rt>かみ</rt></ruby>は<ruby>三人<rt>さんにん</rt></ruby>の<ruby>書<rt>か</rt></ruby>き<ruby>手<rt>て</rt></ruby>を<span class="cn-word" data-tr="aks ettiradi"><ruby>映<rt>うつ</rt></ruby>している</span>。<ruby>生徒<rt>せいと</rt></ruby>、<ruby>先生<rt>せんせい</rt></ruby>、そして<ruby>部活動<rt>ぶかつどう</rt></ruby>である。<ruby>言葉<rt>ことば</rt></ruby>を<ruby>選<rt>えら</rt></ruby>ぶとき、<ruby>私<rt>わたし</rt></ruby>たちは<ruby>自分<rt>じぶん</rt></ruby>がだれであるかも<ruby>選<rt>えら</rt></ruby>んでいる。</p>''',
        "questions": [
            {
                "text": "<ruby>三枚<rt>さんまい</rt></ruby>の<ruby>紙<rt>かみ</rt></ruby>は<ruby>何<rt>なに</rt></ruby>が<ruby>違<rt>ちが</rt></ruby>いますか。",
                "choices": [
                    "<ruby>使<rt>つか</rt></ruby>っている<ruby>言葉<rt>ことば</rt></ruby>の<ruby>層<rt>そう</rt></ruby>",
                    "<ruby>知<rt>し</rt></ruby>らせている<ruby>内容<rt>ないよう</rt></ruby>",
                    "<ruby>貼<rt>は</rt></ruby>ってある<ruby>場所<rt>ばしょ</rt></ruby>",
                    "<ruby>書<rt>か</rt></ruby>いてある<ruby>日<rt>ひ</rt></ruby>",
                ],
                "answer": 0,
                "explanation": "Matnda aniq aytilgan: uchalasi ham "
                               "bir xil narsani bildiradi va uchalasi "
                               "ham toʻgʻri. Farq — soʻzning qatlamida: "
                               "集まり, 集会 va ミーティング.",
            },
            {
                "text": "<ruby>漢語<rt>かんご</rt></ruby>はどうして<ruby>新聞<rt>しんぶん</rt></ruby>の<ruby>見出<rt>みだ</rt></ruby>しに<ruby>使<rt>つか</rt></ruby>われますか。",
                "choices": [
                    "<ruby>短<rt>みじか</rt></ruby>くて<ruby>意味<rt>いみ</rt></ruby>が<ruby>濃<rt>こ</rt></ruby>いから",
                    "やわらかい<ruby>感<rt>かん</rt></ruby>じがするから",
                    "<ruby>新<rt>あたら</rt></ruby>しい<ruby>言葉<rt>ことば</rt></ruby>だから",
                    "カタカナで<ruby>書<rt>か</rt></ruby>くから",
                ],
                "answer": 0,
                "explanation": "Sarlavhada joy tor, 漢語 esa bir xil "
                               "maʼnoni kamroq belgida aytadi. "
                               "Yumshoqlik — 和語 ning xususiyati, "
                               "katakana esa 外来語 niki.",
            },
            {
                "text": "この<ruby>文章<rt>ぶんしょう</rt></ruby>の<ruby>最後<rt>さいご</rt></ruby>の<ruby>文<rt>ぶん</rt></ruby>は<ruby>何<rt>なに</rt></ruby>を<ruby>言<rt>い</rt></ruby>っていますか。",
                "choices": [
                    "<ruby>言葉<rt>ことば</rt></ruby>を<ruby>選<rt>えら</rt></ruby>ぶことは、<ruby>自分<rt>じぶん</rt></ruby>がだれであるかを<ruby>選<rt>えら</rt></ruby>ぶことでもある",
                    "<ruby>三枚<rt>さんまい</rt></ruby>の<ruby>紙<rt>かみ</rt></ruby>は<ruby>全部<rt>ぜんぶ</rt></ruby><ruby>間違<rt>まちが</rt></ruby>っている",
                    "<ruby>外来語<rt>がいらいご</rt></ruby>を<ruby>使<rt>つか</rt></ruby>わないほうがいい",
                    "<ruby>生徒会<rt>せいとかい</rt></ruby>の<ruby>紙<rt>かみ</rt></ruby>がいちばんいい",
                ],
                "answer": 0,
                "explanation": "Qatlamni tanlash — shunchaki uslub "
                               "masalasi emas: u yozuvchining kimligini "
                               "koʻrsatadi. Matn hech bir qogʻozni "
                               "xato deb aytmaydi — uchalasi ham "
                               "toʻgʻri deyilgan.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "じしょを ひらかなかった ひ",
        "summary": (
            "PJ-100 matni — kursning va shelfning soʻnggi matni. Rano "
            "uch yil davomida kuniga oʻn daqiqa oʻqidi. Bir shanba kuni "
            "kitobni yopgach, stol ustidagi lugʻatga qaradi va bir "
            "narsani payqadi."
        ),
        "order":   100,
        "grammar": [
            {
                "pattern":  "〜ている · 〜ていた",
                "meaning":  "Davom etayotgan ish yoki qolgan natija. Bu "
                            "matnda koʻproq ikkinchisi: «shunday boʻlib "
                            "qolgan edi» degan maʼno.",
                "examples": ["<ruby>三十<rt>さんじゅう</rt></ruby>ページ<ruby>読<rt>よ</rt></ruby>んでいた。",
                             "<ruby>言葉<rt>ことば</rt></ruby>が<ruby>見<rt>み</rt></ruby>えなくなっていた。"],
            },
            {
                "pattern":  "〜なくなる",
                "meaning":  "«…maydigan boʻlib qolmoq» — oʻzgarishni "
                            "bildiradi. ない-shakli + なる. Sekin sodir "
                            "boʻladigan oʻzgarishlar uchun.",
                "examples": ["<ruby>辞書<rt>じしょ</rt></ruby>を<ruby>開<rt>ひら</rt></ruby>かなくなった。",
                             "<ruby>言葉<rt>ことば</rt></ruby>が<ruby>見<rt>み</rt></ruby>えなくなる。"],
            },
            {
                "pattern":  "〜たい",
                "meaning":  "Gapiruvchining istagi. Bu matnda u salbiy "
                            "paytda ham chiqadi: «tashlab qoʻygim keldi».",
                "examples": ["<ruby>本気<rt>ほんき</rt></ruby>でやめたいと<ruby>思<rt>おも</rt></ruby>った。"],
            },
        ],
        "body": '''<p>ラノが<ruby>日本語<rt>にほんご</rt></ruby>を<ruby>始<rt>はじ</rt></ruby>めたのは、<ruby>高校<rt>こうこう</rt></ruby><ruby>一年<rt>いちねん</rt></ruby>の<ruby>春<rt>はる</rt></ruby>だった。</p>

<p><ruby>最初<rt>さいしょ</rt></ruby>の<ruby>一<rt>いっ</rt></ruby>か<ruby>月<rt>げつ</rt></ruby>、ひらがなを<ruby>覚<rt>おぼ</rt></ruby>えるだけで<ruby>大変<rt>たいへん</rt></ruby>だった。カタカナを<ruby>覚<rt>おぼ</rt></ruby>えたころには、ひらがなを<ruby>半分<rt>はんぶん</rt></ruby><ruby>忘<rt>わす</rt></ruby>れていた。</p>

<p><ruby>漢字<rt>かんじ</rt></ruby>が<ruby>出<rt>で</rt></ruby>てきた<ruby>日<rt>ひ</rt></ruby>、ラノは<span class="cn-word" data-tr="jiddiy, rostdan"><ruby>本気<rt>ほんき</rt></ruby>で</span>やめたいと<ruby>思<rt>おも</rt></ruby>った。</p>

<p>それでも、<ruby>毎日<rt>まいにち</rt></ruby><ruby>十分<rt>じゅっぷん</rt></ruby>だけ<ruby>読<rt>よ</rt></ruby>んだ。うまくいかない<ruby>日<rt>ひ</rt></ruby>も、<ruby>十分<rt>じゅっぷん</rt></ruby>だけ。</p>

<p><ruby>一年目<rt>いちねんめ</rt></ruby>、<ruby>辞書<rt>じしょ</rt></ruby>を<ruby>一<rt>いち</rt></ruby>ページに<ruby>二十回<rt>にじゅっかい</rt></ruby><ruby>開<rt>ひら</rt></ruby>いた。<ruby>二年目<rt>にねんめ</rt></ruby>、<ruby>十回<rt>じゅっかい</rt></ruby>になった。</p>

<p><ruby>三年目<rt>さんねんめ</rt></ruby>のある<ruby>土曜日<rt>どようび</rt></ruby>、ラノは<ruby>図書館<rt>としょかん</rt></ruby>で<ruby>日本<rt>にほん</rt></ruby>の<span class="cn-word" data-tr="roman, qissa"><ruby>小説<rt>しょうせつ</rt></ruby></span>を<ruby>借<rt>か</rt></ruby>りた。<ruby>薄<rt>うす</rt></ruby>い<ruby>本<rt>ほん</rt></ruby>だった。<ruby>家<rt>いえ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>って、<ruby>椅子<rt>いす</rt></ruby>に<ruby>座<rt>すわ</rt></ruby>って、<ruby>読<rt>よ</rt></ruby>み<ruby>始<rt>はじ</rt></ruby>めた。</p>

<p><span class="cn-word" data-tr="oʻziga kelganda, payqaganda"><ruby>気<rt>き</rt></ruby>がつくと</span>、<ruby>外<rt>そと</rt></ruby>は<ruby>暗<rt>くら</rt></ruby>かった。<ruby>三十<rt>さんじゅう</rt></ruby>ページ<ruby>読<rt>よ</rt></ruby>んでいた。</p>

<p>そして、<ruby>机<rt>つくえ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>を<ruby>見<rt>み</rt></ruby>た。<ruby>辞書<rt>じしょ</rt></ruby>は<span class="cn-word" data-tr="yopiq edi"><ruby>閉<rt>と</rt></ruby>じていた</span>。<ruby>一度<rt>いちど</rt></ruby>も<ruby>開<rt>ひら</rt></ruby>かなかった。</p>

<p>ラノは<ruby>長<rt>なが</rt></ruby>い<ruby>間<rt>あいだ</rt></ruby>、その<ruby>辞書<rt>じしょ</rt></ruby>を<ruby>見<rt>み</rt></ruby>ていた。うれしいというより、<span class="cn-word" data-tr="gʻalati, tushunarsiz"><ruby>不思議<rt>ふしぎ</rt></ruby></span>だった。<ruby>言葉<rt>ことば</rt></ruby>が、いつのまにか<ruby>見<rt>み</rt></ruby>えなくなっていた。</p>

<p><ruby>言葉<rt>ことば</rt></ruby>が<ruby>見<rt>み</rt></ruby>えなくなったとき、はじめて<span class="cn-word" data-tr="hikoya, voqea"><ruby>物語<rt>ものがたり</rt></ruby></span>が<ruby>見<rt>み</rt></ruby>える。</p>

<p><ruby>次<rt>つぎ</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>、ラノはまた<ruby>図書館<rt>としょかん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>った。<ruby>今度<rt>こんど</rt></ruby>は、<ruby>少<rt>すこ</rt></ruby>し<ruby>厚<rt>あつ</rt></ruby>い<ruby>本<rt>ほん</rt></ruby>を<ruby>選<rt>えら</rt></ruby>んだ。</p>''',
        "questions": [
            {
                "text": "ラノは<ruby>毎日<rt>まいにち</rt></ruby>どのくらい<ruby>読<rt>よ</rt></ruby>みましたか。",
                "choices": [
                    "<ruby>十分<rt>じゅっぷん</rt></ruby>だけ",
                    "<ruby>三時間<rt>さんじかん</rt></ruby>",
                    "<ruby>一<rt>いち</rt></ruby>ページ",
                    "<ruby>土曜日<rt>どようび</rt></ruby>だけ",
                ],
                "answer": 0,
                "explanation": "Kuniga atigi oʻn daqiqa — «ishlar "
                               "yurishmagan kunlari ham, oʻn daqiqa». "
                               "Matnning butun kuchi shu kichkina "
                               "raqamda.",
            },
            {
                "text": "<ruby>三年目<rt>さんねんめ</rt></ruby>の<ruby>土曜日<rt>どようび</rt></ruby>、<ruby>何<rt>なに</rt></ruby>が<ruby>起<rt>お</rt></ruby>こりましたか。",
                "choices": [
                    "<ruby>辞書<rt>じしょ</rt></ruby>を<ruby>一度<rt>いちど</rt></ruby>も<ruby>開<rt>ひら</rt></ruby>かずに<ruby>三十<rt>さんじゅう</rt></ruby>ページ<ruby>読<rt>よ</rt></ruby>んだ",
                    "<ruby>試験<rt>しけん</rt></ruby>に<ruby>合格<rt>ごうかく</rt></ruby>した",
                    "<ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>った",
                    "<ruby>新<rt>あたら</rt></ruby>しい<ruby>辞書<rt>じしょ</rt></ruby>を<ruby>買<rt>か</rt></ruby>った",
                ],
                "answer": 0,
                "explanation": "U kitobni oʻqib tugatgach, stolga "
                               "qaradi: lugʻat yopiq turardi. Imtihon "
                               "ham, sayohat ham matnda yoʻq — voqea "
                               "butunlay uyda, stol ustida boʻlib "
                               "oʻtadi.",
            },
            {
                "text": "「<ruby>言葉<rt>ことば</rt></ruby>が<ruby>見<rt>み</rt></ruby>えなくなったとき、はじめて<ruby>物語<rt>ものがたり</rt></ruby>が<ruby>見<rt>み</rt></ruby>える」は<ruby>何<rt>なに</rt></ruby>を<ruby>言<rt>い</rt></ruby>っていますか。",
                "choices": [
                    "<ruby>言葉<rt>ことば</rt></ruby>に<ruby>気<rt>き</rt></ruby>を<ruby>取<rt>と</rt></ruby>られなくなると、<ruby>内容<rt>ないよう</rt></ruby>そのものが<ruby>読<rt>よ</rt></ruby>める",
                    "<ruby>言葉<rt>ことば</rt></ruby>を<ruby>忘<rt>わす</rt></ruby>れたほうがいい",
                    "<ruby>辞書<rt>じしょ</rt></ruby>は<ruby>要<rt>い</rt></ruby>らない",
                    "<ruby>小説<rt>しょうせつ</rt></ruby>は<ruby>薄<rt>うす</rt></ruby>いほうがいい",
                ],
                "answer": 0,
                "explanation": "Til oʻrganishning maqsadi — tilni "
                               "koʻrmay qoʻyish. Har soʻzda toʻxtab "
                               "turgan odam matnni emas, soʻzlarni "
                               "oʻqiydi. Rano uch yildan keyin "
                               "birinchi marta hikoyaning oʻzini "
                               "oʻqidi — lugʻatni unutish yaxshi "
                               "degani emas.",
            },
        ],
    },
]
