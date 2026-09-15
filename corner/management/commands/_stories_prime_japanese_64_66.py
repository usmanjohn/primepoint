# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-64 … PJ-66.

Hikoyachi 普通体 da (PJ-45 dan beri), qoʻshtirnoq ichi です・ます ni
saqlaydi.

Shakl navbati: 64 — omadsiz kun hikoyasi, 65 — oilaviy suhbat,
66 — orqaga qarash (esse). Oldingi batchda yaxshilik zanjiri /
tergov / yangiliklar byulleteni boʻlgan edi.

⚠️ CUMULATIVE: 64 da kauzativ yoʻq va kauzativ-passiv yoʻq;
65 da kauzativ-passiv yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_64_66.py --author=prime
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
        "title":   "ついてない ひ",
        "summary": (
            "PJ-64 matni. Inomning omadsiz kuni — va yaponcha yomon "
            "kun hikoyasi deyarli doim aziyat passivi bilan "
            "yoziladi, chunki har bir gap zarar koʻrgan odamdan "
            "boshlanadi."
        ),
        "order":   64,
        "grammar": [
            {
                "pattern":  "Oʻtimsiz feʼl + passiv",
                "meaning":  "«…va men shundan zarar koʻrdim». "
                            "Gapning egasi ishda umuman ishtirok "
                            "etmaydi.",
                "examples": ["<ruby>雨<rt>あめ</rt></ruby>に<ruby>降<rt>ふ</rt></ruby>られた。",
                             "<ruby>子<rt>こ</rt></ruby>どもに<ruby>泣<rt>な</rt></ruby>かれた。"],
            },
            {
                "pattern":  "を qoladi",
                "meaning":  "Egalik buyumi zarar koʻrganda を oʻz "
                            "joyida qoladi, chunki gapning egasi — "
                            "odam.",
                "examples": ["<ruby>足<rt>あし</rt></ruby>を<ruby>踏<rt>ふ</rt></ruby>まれた。"],
            },
            {
                "pattern":  "Sababchi に oladi",
                "meaning":  "Passiv gapda ishni boshlagan tomon doim "
                            "に bilan turadi — yomgʻir ham, odam ham.",
                "examples": ["<ruby>弟<rt>おとうと</rt></ruby>にケーキを<ruby>食<rt>た</rt></ruby>べられた。"],
            },
        ],
        "body": '''<p><ruby>木曜日<rt>もくようび</rt></ruby>は<span class="cn-word" data-tr="omadsiz kun">ついてない<ruby>日<rt>ひ</rt></ruby></span>だった。</p>

<p><ruby>朝<rt>あさ</rt></ruby>、<ruby>家<rt>いえ</rt></ruby>を<ruby>出<rt>で</rt></ruby>たとき<ruby>空<rt>そら</rt></ruby>は<ruby>青<rt>あお</rt></ruby>かった。<ruby>駅<rt>えき</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>で<ruby>雨<rt>あめ</rt></ruby>に<ruby>降<rt>ふ</rt></ruby>られた。かさはなかった。</p>

<p><ruby>電車<rt>でんしゃ</rt></ruby>は<ruby>込<rt>こ</rt></ruby>んでいた。<ruby>知<rt>し</rt></ruby>らない<ruby>人<rt>ひと</rt></ruby>に<ruby>足<rt>あし</rt></ruby>を<ruby>踏<rt>ふ</rt></ruby>まれた。その<ruby>人<rt>ひと</rt></ruby>は<ruby>気<rt>き</rt></ruby>がつかなかった。</p>

<p><ruby>学校<rt>がっこう</rt></ruby>で<ruby>作文<rt>さくぶん</rt></ruby>を<ruby>出<rt>だ</rt></ruby>した。<ruby>名前<rt>なまえ</rt></ruby>を<ruby>書<rt>か</rt></ruby>かなかった。<ruby>忘<rt>わす</rt></ruby>れていた。<ruby>先生<rt>せんせい</rt></ruby>に<ruby>叱<rt>しか</rt></ruby>られた。</p>

<p><ruby>昼<rt>ひる</rt></ruby>、<ruby>机<rt>つくえ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>にパンを<ruby>置<rt>お</rt></ruby>いた。<ruby>三分<rt>さんぷん</rt></ruby><ruby>後<rt>ご</rt></ruby>、パンがなかった。<span class="cn-word" data-tr="sinfdoshim"><ruby>同<rt>おな</rt></ruby>じクラスの<ruby>子<rt>こ</rt></ruby></span>に<ruby>食<rt>た</rt></ruby>べられた。</p>

<p><ruby>放課後<rt>ほうかご</rt></ruby>、<ruby>図書館<rt>としょかん</rt></ruby>で<ruby>勉強<rt>べんきょう</rt></ruby>した。<ruby>隣<rt>となり</rt></ruby>の<ruby>子<rt>こ</rt></ruby>に<span class="cn-word" data-tr="yigʻlab yubordi"><ruby>泣<rt>な</rt></ruby>かれた</span>。<ruby>何<rt>なに</rt></ruby>も<ruby>読<rt>よ</rt></ruby>めなかった。</p>

<p><ruby>家<rt>いえ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>って、<ruby>母<rt>はは</rt></ruby>にこの<ruby>話<rt>はなし</rt></ruby>をした。<ruby>母<rt>はは</rt></ruby>は<ruby>笑<rt>わら</rt></ruby>った。</p>

<p><strong>はは:</strong> ひどい<ruby>日<rt>ひ</rt></ruby>でしたね。でも、<ruby>五<rt>いつ</rt></ruby>つ<ruby>全部<rt>ぜんぶ</rt></ruby><span class="cn-word" data-tr="eslab qoldingiz"><ruby>覚<rt>おぼ</rt></ruby>えていますよ</span>。いい<ruby>日<rt>ひ</rt></ruby>は<ruby>覚<rt>おぼ</rt></ruby>えていません。</p>

<p>イノムさんは<ruby>考<rt>かんが</rt></ruby>えた。<ruby>先週<rt>せんしゅう</rt></ruby>の<ruby>月曜日<rt>げつようび</rt></ruby>に<ruby>何<rt>なに</rt></ruby>があったか。<ruby>思<rt>おも</rt></ruby>い<ruby>出<rt>だ</rt></ruby>せなかった。</p>''',
        "questions": [
            {
                "text": "イノムさんは<ruby>駅<rt>えき</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>で<ruby>何<rt>なに</rt></ruby>がありましたか。",
                "choices": [
                    "Yomgʻirda qolib ketdi — soyaboni yoʻq edi",
                    "Poyezdga kechikdi",
                    "Hamyonini yoʻqotdi",
                    "Doʻstini uchratdi",
                ],
                "answer": 0,
                "explanation": "<strong>雨に降られた</strong> — soʻzma-soʻz "
                               "«yomgʻir tomonidan yogʻildim». Inom hech nima "
                               "qilmadi, lekin gapning egasi — u.",
            },
            {
                "text": "«<ruby>足<rt>あし</rt></ruby>を<ruby>踏<rt>ふ</rt></ruby>まれた» — nega を qolgan?",
                "choices": [
                    "Chunki gapning egasi oyoq emas, Inom",
                    "Chunki 足 ot",
                    "Chunki 踏む I guruh feʼli",
                    "Chunki gap oʻtgan zamonda",
                ],
                "answer": 0,
                "explanation": "Egasi <strong>odam</strong> boʻlsa, gap "
                               "shikoyatga aylanadi va を oʻz joyida qoladi. "
                               "Oʻzbekchada «oyogʻimni bosib ketishdi».",
            },
            {
                "text": "<ruby>母<rt>はは</rt></ruby>は<ruby>何<rt>なに</rt></ruby>と<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "Beshtasini ham eslab qolgansiz — yaxshi kunlar esda qolmaydi",
                    "Ertaga yaxshi kun boʻladi",
                    "Soyabon olib yurish kerak",
                    "Oʻqituvchiga aytish kerak",
                ],
                "answer": 0,
                "explanation": "Va matn shu bilan tugaydi: Inom oʻtgan "
                               "dushanbani eslay olmaydi. Aziyat passivi "
                               "yomon kunlarni <strong>gap ichiga</strong> "
                               "yozib qoʻyadi — shuning uchun ular "
                               "esda qoladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "いかせて ください",
        "summary": (
            "PJ-65 matni. Rano Yaponiyada oʻqishga bormoqchi va "
            "otasidan ruxsat soʻraydi — matnda kauzativning ikkala "
            "maʼnosi ham bor: majbur qilish va ruxsat berish."
        ),
        "order":   65,
        "grammar": [
            {
                "pattern":  "ない-oʻzak + せる / させる",
                "meaning":  "«Qildirmoq» yoki «ruxsat bermoq». Bitta "
                            "shakl, ikki maʼno; kontekst ajratadi.",
                "examples": ["<ruby>行<rt>い</rt></ruby>かせる。", "<ruby>勉強<rt>べんきょう</rt></ruby>させる。"],
            },
            {
                "pattern":  "〜させてください",
                "meaning":  "«…qilishimga ruxsat bering». Yaponchada "
                            "ruxsat soʻrashning asosiy yoʻli.",
                "examples": ["<ruby>行<rt>い</rt></ruby>かせてください。",
                             "<ruby>考<rt>かんが</rt></ruby>えさせてください。"],
            },
            {
                "pattern":  "〜させてくれる — ruxsat",
                "meaning":  "くれる yaxshilikni bildiradi, va "
                            "majburlash yaxshilik boʻlmaydi — shuning "
                            "uchun bu qolip deyarli doim «ruxsat».",
                "examples": ["<ruby>父<rt>ちち</rt></ruby>は<ruby>行<rt>い</rt></ruby>かせてくれた。"],
            },
        ],
        "body": '''<p><ruby>十一月<rt>じゅういちがつ</rt></ruby>、ラノさんは<span class="cn-word" data-tr="chet elda oʻqish"><ruby>留学<rt>りゅうがく</rt></ruby></span>のことを<ruby>父<rt>ちち</rt></ruby>に<ruby>話<rt>はな</rt></ruby>した。<ruby>一年間<rt>いちねんかん</rt></ruby><ruby>日本<rt>にほん</rt></ruby>の<ruby>高校<rt>こうこう</rt></ruby>で<ruby>勉強<rt>べんきょう</rt></ruby>したかった。</p>

<p><ruby>父<rt>ちち</rt></ruby>は<ruby>最初<rt>さいしょ</rt></ruby><ruby>反対<rt>はんたい</rt></ruby>した。</p>

<p><strong>ちち:</strong> まだ<ruby>早<rt>はや</rt></ruby>いです。<ruby>十七歳<rt>じゅうななさい</rt></ruby>です。</p>

<p><strong>ラノ:</strong> <ruby>一年間<rt>いちねんかん</rt></ruby>です。<span class="cn-word" data-tr="yuborsangiz"><ruby>行<rt>い</rt></ruby>かせて</span>ください。おねがいします。</p>

<p><ruby>父<rt>ちち</rt></ruby>は<ruby>三日間<rt>みっかかん</rt></ruby><ruby>何<rt>なに</rt></ruby>も<ruby>言<rt>い</rt></ruby>わなかった。ラノさんも<ruby>何<rt>なに</rt></ruby>も<ruby>言<rt>い</rt></ruby>わなかった。</p>

<p><ruby>四日目<rt>よっかめ</rt></ruby>の<ruby>夜<rt>よる</rt></ruby>、<ruby>父<rt>ちち</rt></ruby>は<ruby>紙<rt>かみ</rt></ruby>を<ruby>持<rt>も</rt></ruby>ってきた。<ruby>上<rt>うえ</rt></ruby>に<ruby>三<rt>みっ</rt></ruby>つの<span class="cn-word" data-tr="shart"><ruby>条件<rt>じょうけん</rt></ruby></span>があった。</p>

<p><strong>ちち:</strong> <ruby>一<rt>ひと</rt></ruby>つ。<ruby>毎週<rt>まいしゅう</rt></ruby><ruby>電話<rt>でんわ</rt></ruby>してください。<ruby>二<rt>ふた</rt></ruby>つ。お<ruby>金<rt>かね</rt></ruby>の<ruby>記録<rt>きろく</rt></ruby>を<ruby>書<rt>か</rt></ruby>いてください。<ruby>三<rt>みっ</rt></ruby>つ。<ruby>日本語<rt>にほんご</rt></ruby>の<ruby>試験<rt>しけん</rt></ruby>を<ruby>受<rt>う</rt></ruby>けてください。</p>

<p>ラノさんは<ruby>三<rt>みっ</rt></ruby>つとも<ruby>約束<rt>やくそく</rt></ruby>した。<ruby>父<rt>ちち</rt></ruby>は<ruby>行<rt>い</rt></ruby>かせてくれた。</p>

<p><ruby>後<rt>あと</rt></ruby>で<ruby>母<rt>はは</rt></ruby>から<ruby>聞<rt>き</rt></ruby>いた。<ruby>父<rt>ちち</rt></ruby>は<ruby>三日間<rt>みっかかん</rt></ruby><ruby>毎晩<rt>まいばん</rt></ruby><ruby>地図<rt>ちず</rt></ruby>を<ruby>見<rt>み</rt></ruby>ていた。そして<ruby>母<rt>はは</rt></ruby>に<ruby>同<rt>おな</rt></ruby>じ<ruby>質問<rt>しつもん</rt></ruby>を<ruby>三回<rt>さんかい</rt></ruby>させた。「<ruby>遠<rt>とお</rt></ruby>いですか。」</p>''',
        "questions": [
            {
                "text": "ラノさんは<ruby>父<rt>ちち</rt></ruby>に<ruby>何<rt>なに</rt></ruby>を<ruby>頼<rt>たの</rt></ruby>みましたか。",
                "choices": [
                    "Bir yilga Yaponiyaga oʻqishga yuborishini",
                    "Pul berishini",
                    "Yaponchani oʻrgatishini",
                    "Maktabni oʻzgartirishini",
                ],
                "answer": 0,
                "explanation": "<strong>行かせてください</strong> — kauzativning "
                               "て-shakli + ください. Yaponchada ruxsat "
                               "soʻrashning asosiy yoʻli shu: «qilaman» "
                               "deyish qoʻpol, «qilishimga ruxsat bering» "
                               "esa tabiiy.",
            },
            {
                "text": "«<ruby>父<rt>ちち</rt></ruby>は<ruby>行<rt>い</rt></ruby>かせてくれた» — bu majburmi yoki ruxsatmi?",
                "choices": [
                    "Ruxsat — くれる yaxshilikni bildiradi",
                    "Majbur",
                    "Ikkalasi ham boʻlishi mumkin",
                    "Gapdan bilib boʻlmaydi",
                ],
                "answer": 0,
                "explanation": "Majburlash yaxshilik boʻlmaydi, shuning "
                               "uchun <strong>〜させてくれた</strong> deyarli "
                               "doim «ruxsat berdi» degani.",
            },
            {
                "text": "<ruby>母<rt>はは</rt></ruby>に<ruby>同<rt>おな</rt></ruby>じ<ruby>質問<rt>しつもん</rt></ruby>を<ruby>三回<rt>さんかい</rt></ruby>させたのはだれですか。",
                "choices": [
                    "Otasi — u uch kecha xaritaga qaragan edi",
                    "Ranoning oʻzi",
                    "Onasi",
                    "Maktab oʻqituvchisi",
                ],
                "answer": 0,
                "explanation": "Bu yerda kauzativ ikkinchi maʼnosida: "
                               "<strong>させた</strong> — «qildirdi». Ota "
                               "jim yurgan uch kun ichida nima qilganini "
                               "matn faqat oxirida aytadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "ピアノの れんしゅう",
        "summary": (
            "PJ-66 matni. Kattalik yoshiga yetgan odam bolaligidagi "
            "pianino mashqlarini eslaydi — kauzativ-passiv butun "
            "matnni koʻtarib turadi, va oxirida ohang oʻzgaradi."
        ),
        "order":   66,
        "grammar": [
            {
                "pattern":  "kauzativ + passiv",
                "meaning":  "«Majburan qildim». Kauzativ II guruh feʼli "
                            "boʻlib qoladi, shuning uchun unga られる "
                            "qoʻshiladi.",
                "examples": ["<ruby>練習<rt>れんしゅう</rt></ruby>させられた。",
                             "<ruby>行<rt>い</rt></ruby>かせられた。"],
            },
            {
                "pattern":  "Qisqa shakl 〜される",
                "meaning":  "Faqat I guruhda, す bilan tugamaydigan "
                            "feʼllarda: 待たせられる → 待たされる.",
                "examples": ["<ruby>一時間<rt>いちじかん</rt></ruby><ruby>待<rt>ま</rt></ruby>たされた。"],
            },
            {
                "pattern":  "Ohangi doim salbiy",
                "meaning":  "Gapda «yoqmasdi» degan soʻz boʻlmasa ham, "
                            "u feʼlning ichida turadi.",
                "examples": ["<ruby>毎日<rt>まいにち</rt></ruby><ruby>三十分<rt>さんじゅっぷん</rt></ruby><ruby>練習<rt>れんしゅう</rt></ruby>させられた。"],
            },
        ],
        "body": '''<p><ruby>六歳<rt>ろくさい</rt></ruby>のとき、<ruby>母<rt>はは</rt></ruby>にピアノを<ruby>習<rt>なら</rt></ruby>わせられた。<ruby>自分<rt>じぶん</rt></ruby>で<ruby>選<rt>えら</rt></ruby>ばなかった。</p>

<p><ruby>毎日<rt>まいにち</rt></ruby><ruby>三十分<rt>さんじゅっぷん</rt></ruby><ruby>練習<rt>れんしゅう</rt></ruby>させられた。<ruby>外<rt>そと</rt></ruby>で<ruby>友<rt>とも</rt></ruby>だちが<ruby>遊<rt>あそ</rt></ruby>んでいた。<span class="cn-word" data-tr="deraza yonida"><ruby>窓<rt>まど</rt></ruby>の<ruby>近<rt>ちか</rt></ruby>く</span>にピアノがあった。それが<ruby>一番<rt>いちばん</rt></ruby><ruby>辛<rt>つら</rt></ruby>かった。</p>

<p><ruby>発表会<rt>はっぴょうかい</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>は<ruby>一時間<rt>いちじかん</rt></ruby>になった。<ruby>会場<rt>かいじょう</rt></ruby>では<ruby>二時間<rt>にじかん</rt></ruby><ruby>待<rt>ま</rt></ruby>たされた。<ruby>演奏<rt>えんそう</rt></ruby>は<ruby>三分<rt>さんぷん</rt></ruby>だった。</p>

<p><ruby>十四歳<rt>じゅうよんさい</rt></ruby>のとき、やめた。<ruby>母<rt>はは</rt></ruby>は<ruby>何<rt>なに</rt></ruby>も<ruby>言<rt>い</rt></ruby>わなかった。ピアノは<ruby>八年間<rt>はちねんかん</rt></ruby><ruby>誰<rt>だれ</rt></ruby>も<ruby>触<rt>さわ</rt></ruby>らなかった。</p>

<p><ruby>去年<rt>きょねん</rt></ruby>の<ruby>冬<rt>ふゆ</rt></ruby>、<ruby>友<rt>とも</rt></ruby>だちの<ruby>家<rt>いえ</rt></ruby>でピアノを<ruby>見<rt>み</rt></ruby>た。<ruby>座<rt>すわ</rt></ruby>って、<ruby>手<rt>て</rt></ruby>を<ruby>置<rt>お</rt></ruby>いた。<span class="cn-word" data-tr="qoʻllarim esda saqlagan ekan"><ruby>手<rt>て</rt></ruby>が<ruby>覚<rt>おぼ</rt></ruby>えていた</span>。</p>

<p><ruby>八年<rt>はちねん</rt></ruby><ruby>触<rt>さわ</rt></ruby>らなかったが、<ruby>指<rt>ゆび</rt></ruby>が<ruby>動<rt>うご</rt></ruby>いた。<ruby>友<rt>とも</rt></ruby>だちは<ruby>驚<rt>おどろ</rt></ruby>いた。</p>

<p><strong>ともだち:</strong> いつ<ruby>習<rt>なら</rt></ruby>いましたか。</p>

<p><strong>わたし:</strong> <ruby>子<rt>こ</rt></ruby>どものときです。<ruby>好<rt>す</rt></ruby>きじゃありませんでした。</p>

<p>いまは<ruby>週<rt>しゅう</rt></ruby>に<ruby>一度<rt>いちど</rt></ruby><ruby>弾<rt>ひ</rt></ruby>いている。<ruby>誰<rt>だれ</rt></ruby>にも<span class="cn-word" data-tr="majburlanmayapman"><ruby>言<rt>い</rt></ruby>われていない</span>。それが<ruby>一番<rt>いちばん</rt></ruby><ruby>違<rt>ちが</rt></ruby>う。</p>''',
        "questions": [
            {
                "text": "<ruby>子<rt>こ</rt></ruby>どものとき、ピアノの<ruby>練習<rt>れんしゅう</rt></ruby>はどうでしたか。",
                "choices": [
                    "Har kuni oʻttiz daqiqa majburan mashq qildirishardi",
                    "Oʻzi xohlab mashq qilardi",
                    "Haftada bir marta mashq qilardi",
                    "Umuman mashq qilmasdi",
                ],
                "answer": 0,
                "explanation": "<strong>練習させられた</strong> — kauzativ-passiv. "
                               "Gapda «yoqmasdi» degan soʻz yoʻq, lekin u "
                               "feʼlning ichida turibdi.",
            },
            {
                "text": "«<ruby>二時間<rt>にじかん</rt></ruby><ruby>待<rt>ま</rt></ruby>たされた» — nega bu qisqa shakl?",
                "choices": [
                    "Chunki 待つ I guruh feʼli va す bilan tugamaydi",
                    "Chunki gap oʻtgan zamonda",
                    "Chunki 待つ II guruh feʼli",
                    "Chunki bu ogʻzaki nutq"],
                "answer": 0,
                "explanation": "〜せられる → <strong>〜される</strong> qisqarishi "
                               "faqat I guruhda ishlaydi. 待たせられた ham "
                               "toʻgʻri, lekin qisqa shakl tabiiyroq. "
                               "«話さされる» esa mavjud emas.",
            },
            {
                "text": "<ruby>最後<rt>さいご</rt></ruby>の<ruby>文<rt>ぶん</rt></ruby>「<ruby>誰<rt>だれ</rt></ruby>にも<ruby>言<rt>い</rt></ruby>われていない」はなぜ<ruby>大切<rt>たいせつ</rt></ruby>ですか。",
                "choices": [
                    "Chunki endi hech kim majburlamayapti — butun matnning ohangi shu bilan oʻzgaradi",
                    "Chunki u endi yaxshi chaladi",
                    "Chunki onasi vafot etgan",
                    "Chunki pianino yangi",
                ],
                "answer": 0,
                "explanation": "Matn boshdan-oyoq kauzativ-passiv bilan "
                               "yuradi — «majburlashardi». Oxirgi gapda esa "
                               "oddiy passiv inkorda: hech kim aytmayapti. "
                               "Ish bir xil, ohang butunlay boshqa.",
            },
        ],
    },
]
