# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-70 … PJ-72. Keigo bloki yopiladi.

Hikoyachi 普通体 da (PJ-45 dan beri), qoʻshtirnoq ichi です・ます ni
saqlaydi.

Shakl navbati: 70 — telefon suhbati, 71 — tushuntiruvchi esse,
72 — oilaviy sahna. Oldingi batchda sport kuni / birinchi ish kuni /
doʻkon sahnasi boʻlgan edi.

⚠️ CUMULATIVE: 70 da ございます va doʻkon iboralari yoʻq (PJ-71);
70 va 71 da うち/そと chegarasi ochiq tushuntirilmaydi (PJ-72).

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_70_72.py --author=prime
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
        "title":   "でんわの こえ",
        "summary": (
            "PJ-70 matni. Rano birinchi marta ish telefonini koʻtaradi "
            "— va butun suhbat 謙譲語 ustida yuradi: 申します, "
            "おります, 伺います."
        ),
        "order":   70,
        "grammar": [
            {
                "pattern":  "お + ます-oʻzak + する",
                "meaning":  "«Men qilaman» — oʻzini pasaytiruvchi "
                            "mahsuldor qolip. Xitoycha oʻzakli feʼl ご "
                            "oladi.",
                "examples": ["お<ruby>伝<rt>つた</rt></ruby>えします。",
                             "ご<ruby>連絡<rt>れんらく</rt></ruby>します。"],
            },
            {
                "pattern":  "Maxsus <ruby>謙譲語<rt>けんじょうご</rt></ruby> feʼllari",
                "meaning":  "申す (aytmoq), おる (boʻlmoq), 参る "
                            "(bormoq), 伺う (soʻramoq). ます da "
                            "istisno emas.",
                "examples": ["ラノと<ruby>申<rt>もう</rt></ruby>します。",
                             "<ruby>店長<rt>てんちょう</rt></ruby>はおりません。"],
            },
            {
                "pattern":  "Ish suhbatdoshga tegsa — kamtar shakl",
                "meaning":  "Tegmasa oddiy 丁寧語 yetadi. Keigo — "
                            "munosabatning tili.",
                "examples": ["お<ruby>待<rt>ま</rt></ruby>ちしております。"],
            },
        ],
        "body": '''<p><ruby>火曜日<rt>かようび</rt></ruby>の<ruby>午前<rt>ごぜん</rt></ruby>、<ruby>本屋<rt>ほんや</rt></ruby>の<ruby>電話<rt>でんわ</rt></ruby>が<ruby>鳴<rt>な</rt></ruby>った。<ruby>店長<rt>てんちょう</rt></ruby>は<ruby>倉庫<rt>そうこ</rt></ruby>にいた。ラノさんが<ruby>初<rt>はじ</rt></ruby>めて<ruby>受話器<rt>じゅわき</rt></ruby>を<ruby>取<rt>と</rt></ruby>った。</p>

<p><strong>ラノ:</strong> はい、<ruby>本屋<rt>ほんや</rt></ruby>でございます。ラノと<ruby>申<rt>もう</rt></ruby>します。</p>

<p><strong>あいて:</strong> <ruby>出版社<rt>しゅっぱんしゃ</rt></ruby>の<ruby>山田<rt>やまだ</rt></ruby>と<ruby>申<rt>もう</rt></ruby>します。<ruby>店長<rt>てんちょう</rt></ruby>さんはいらっしゃいますか。</p>

<p>ラノさんは<ruby>一瞬<rt>いっしゅん</rt></ruby><ruby>迷<rt>まよ</rt></ruby>った。<span class="cn-word" data-tr="mudir yonida yoʻq edi"><ruby>店長<rt>てんちょう</rt></ruby>はそこにいなかった</span>。</p>

<p><strong>ラノ:</strong> <ruby>店長<rt>てんちょう</rt></ruby>はただ<ruby>今<rt>いま</rt></ruby>おりません。<ruby>三十分後<rt>さんじゅっぷんご</rt></ruby>に<ruby>戻<rt>もど</rt></ruby>ります。</p>

<p><strong>あいて:</strong> では、ご<ruby>伝言<rt>でんごん</rt></ruby>をお<ruby>願<rt>ねが</rt></ruby>いします。</p>

<p><strong>ラノ:</strong> はい、お<ruby>伝<rt>つた</rt></ruby>えします。</p>

<p><ruby>山田<rt>やまだ</rt></ruby>さんは<ruby>来週<rt>らいしゅう</rt></ruby>の<ruby>金曜日<rt>きんようび</rt></ruby>に<span class="cn-word" data-tr="tashrif buyurmoqchi"><ruby>伺<rt>うかが</rt></ruby>いたい</span>と<ruby>言<rt>い</rt></ruby>った。ラノさんは<ruby>紙<rt>かみ</rt></ruby>に<ruby>書<rt>か</rt></ruby>いた。</p>

<p><strong>ラノ:</strong> <ruby>来週<rt>らいしゅう</rt></ruby>の<ruby>金曜日<rt>きんようび</rt></ruby>ですね。お<ruby>待<rt>ま</rt></ruby>ちしております。</p>

<p><ruby>電話<rt>でんわ</rt></ruby>を<ruby>切<rt>き</rt></ruby>ってから、ラノさんは<ruby>手<rt>て</rt></ruby>が<span class="cn-word" data-tr="titrayotgan edi"><ruby>震<rt>ふる</rt></ruby>えていた</span>。<ruby>三十分後<rt>さんじゅっぷんご</rt></ruby>、<ruby>店長<rt>てんちょう</rt></ruby>が<ruby>戻<rt>もど</rt></ruby>った。ラノさんは<ruby>紙<rt>かみ</rt></ruby>を<ruby>渡<rt>わた</rt></ruby>した。</p>

<p><strong>てんちょう:</strong> <ruby>一<rt>ひと</rt></ruby>つも<ruby>間違<rt>まちが</rt></ruby>えませんでした。よくできました。</p>

<p>ラノさんは<ruby>何<rt>なに</rt></ruby>も<ruby>言<rt>い</rt></ruby>わなかった。でも<ruby>夜<rt>よる</rt></ruby>、<ruby>手帳<rt>てちょう</rt></ruby>に<ruby>一<rt>いち</rt></ruby>ページ<ruby>書<rt>か</rt></ruby>いた。</p>''',
        "questions": [
            {
                "text": "ラノさんは<ruby>電話<rt>でんわ</rt></ruby>で<ruby>自分<rt>じぶん</rt></ruby>の<ruby>名前<rt>なまえ</rt></ruby>をどう<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "ラノと申します — «aytmoq» ning kamtar shakli bilan",
                    "ラノと言います",
                    "ラノとおっしゃいます",
                    "ラノでいらっしゃいます",
                ],
                "answer": 0,
                "explanation": "<strong>申す</strong> — 謙譲語. おっしゃる "
                               "esa 尊敬語 va u faqat suhbatdosh uchun. "
                               "Oʻz ismingizni aytish — oʻz ishingiz.",
            },
            {
                "text": "«<ruby>店長<rt>てんちょう</rt></ruby>はただ<ruby>今<rt>いま</rt></ruby>おりません» — nega いらっしゃいません emas?",
                "choices": [
                    "Chunki mudir Ranoning oʻz guruhida, suhbatdosh esa tashqarida",
                    "Chunki mudir omborda edi",
                    "Chunki おる qisqaroq",
                    "Chunki bu telefon suhbati",
                ],
                "answer": 0,
                "explanation": "Tashqi odam bilan gapirganda oʻz "
                               "guruhingizdagi odam <strong>pasaytiriladi</strong>. "
                               "Doʻkon ichida esa いらっしゃいます toʻgʻri "
                               "boʻlardi — PJ-72 shu haqida.",
            },
            {
                "text": "«お<ruby>伝<rt>つた</rt></ruby>えします» qaysi qolip bilan yasalgan?",
                "choices": [
                    "お + ます-oʻzak + する — kamtar mahsuldor qolip",
                    "お + ます-oʻzak + になる",
                    "Maxsus feʼl",
                    "Passiv shakl",
                ],
                "answer": 0,
                "explanation": "伝える ning ます-oʻzagi 伝え, ustiga "
                               "<strong>する</strong>. «お伝えになる» boʻlsa "
                               "u suhbatdoshning ishi boʻlardi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "コンビニの ことば",
        "summary": (
            "PJ-71 matni — tushuntiruvchi matn. Nega Yaponiyadagi "
            "hamma doʻkonda bir xil gaplar eshitiladi, va nega "
            "ularni yodlash grammatikadan foydaliroq."
        ),
        "order":   71,
        "grammar": [
            {
                "pattern":  "ございます",
                "meaning":  "ある va です ning eng muloyim shakli. "
                            "Hech kimni koʻtarmaydi va pasaytirmaydi "
                            "— butun gapga kiyim beradi.",
                "examples": ["こちらでございます。", "<ruby>二階<rt>にかい</rt></ruby>にございます。"],
            },
            {
                "pattern":  "Tayyor iboralar",
                "meaning":  "いらっしゃいませ, 少々お待ちください, "
                            "かしこまりました — bular yasalmaydi, "
                            "butunligicha yodlanadi.",
                "examples": ["いらっしゃいませ。", "かしこまりました。"],
            },
            {
                "pattern":  "ませ — ます ning buyruq shakli",
                "meaning":  "PJ-67 dagi え-qator, lekin qoʻpol emas: "
                            "u faqat mijozga qaratilgan iboralarda "
                            "qolgan.",
                "examples": ["またお<ruby>越<rt>こ</rt></ruby>しくださいませ。"],
            },
        ],
        "body": '''<p><ruby>日本<rt>にほん</rt></ruby>の<span class="cn-word" data-tr="kichik doʻkon">コンビニ</span>に<ruby>入<rt>はい</rt></ruby>ると、<ruby>必<rt>かなら</rt></ruby>ず<ruby>同<rt>おな</rt></ruby>じ<ruby>言葉<rt>ことば</rt></ruby>が<ruby>聞<rt>き</rt></ruby>こえる。「いらっしゃいませ。」</p>

<p><ruby>東京<rt>とうきょう</rt></ruby>でも<ruby>大阪<rt>おおさか</rt></ruby>でも<ruby>北海道<rt>ほっかいどう</rt></ruby>でも<ruby>同<rt>おな</rt></ruby>じだ。<ruby>店員<rt>てんいん</rt></ruby>が<ruby>変<rt>か</rt></ruby>わっても<ruby>言葉<rt>ことば</rt></ruby>は<ruby>変<rt>か</rt></ruby>わらない。</p>

<p><ruby>理由<rt>りゆう</rt></ruby>は<ruby>簡単<rt>かんたん</rt></ruby>だ。この<ruby>言葉<rt>ことば</rt></ruby>は<span class="cn-word" data-tr="tayyor bloklar"><ruby>決<rt>き</rt></ruby>まった<ruby>形<rt>かたち</rt></ruby></span>だ。<ruby>店員<rt>てんいん</rt></ruby>は<ruby>作<rt>つく</rt></ruby>らない。<ruby>覚<rt>おぼ</rt></ruby>える。</p>

<p><ruby>十<rt>じゅう</rt></ruby>ぐらいの<ruby>文<rt>ぶん</rt></ruby>がある。「<ruby>少々<rt>しょうしょう</rt></ruby>お<ruby>待<rt>ま</rt></ruby>ちください。」「かしこまりました。」「<ruby>申<rt>もう</rt></ruby>し<ruby>訳<rt>わけ</rt></ruby>ございません。」「またお<ruby>越<rt>こ</rt></ruby>しくださいませ。」</p>

<p>この<ruby>十<rt>じゅう</rt></ruby>を<ruby>覚<rt>おぼ</rt></ruby>えれば、コンビニの<ruby>会話<rt>かいわ</rt></ruby>は<ruby>全部<rt>ぜんぶ</rt></ruby><ruby>分<rt>わ</rt></ruby>かる。<ruby>文法<rt>ぶんぽう</rt></ruby>より<span class="cn-word" data-tr="foydaliroq"><ruby>役<rt>やく</rt></ruby>に<ruby>立<rt>た</rt></ruby>つ</span>。</p>

<p><ruby>面白<rt>おもしろ</rt></ruby>いことがある。<ruby>店員<rt>てんいん</rt></ruby>がよく<ruby>使<rt>つか</rt></ruby>う<ruby>言<rt>い</rt></ruby>い<ruby>方<rt>かた</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に、<ruby>正<rt>ただ</rt></ruby>しくないものもある。「<ruby>千円<rt>せんえん</rt></ruby>になります」がその<ruby>一<rt>ひと</rt></ruby>つだ。<ruby>値段<rt>ねだん</rt></ruby>は「なる」と<ruby>言<rt>い</rt></ruby>わない。「<ruby>千円<rt>せんえん</rt></ruby>でございます」が<ruby>正<rt>ただ</rt></ruby>しい。</p>

<p>でも<ruby>誰<rt>だれ</rt></ruby>も<ruby>直<rt>なお</rt></ruby>さない。<ruby>長<rt>なが</rt></ruby>い<ruby>言葉<rt>ことば</rt></ruby>は<ruby>丁寧<rt>ていねい</rt></ruby>に<ruby>聞<rt>き</rt></ruby>こえる。それで<ruby>残<rt>のこ</rt></ruby>った。</p>

<p><ruby>外国<rt>がいこく</rt></ruby>から<ruby>来<rt>き</rt></ruby>た<ruby>人<rt>ひと</rt></ruby>に<ruby>敬語<rt>けいご</rt></ruby>は<ruby>要<rt>い</rt></ruby>らない。「ありがとう」でじゅうぶんだ。でも<ruby>店員<rt>てんいん</rt></ruby>の<ruby>言葉<rt>ことば</rt></ruby>が<ruby>分<rt>わ</rt></ruby>からないと、<ruby>会話<rt>かいわ</rt></ruby>が<ruby>止<rt>と</rt></ruby>まる。</p>

<p>だから<ruby>敬語<rt>けいご</rt></ruby>は<span class="cn-word" data-tr="gapirish uchun emas"><ruby>話<rt>はな</rt></ruby>すためではない</span>。<ruby>聞<rt>き</rt></ruby>くためだ。</p>''',
        "questions": [
            {
                "text": "なぜ<ruby>日本<rt>にほん</rt></ruby>の<ruby>店<rt>みせ</rt></ruby>で<ruby>同<rt>おな</rt></ruby>じ<ruby>言葉<rt>ことば</rt></ruby>が<ruby>聞<rt>き</rt></ruby>こえますか。",
                "choices": [
                    "Chunki bu gaplar tayyor bloklar — xodim ularni yasamaydi, yodlaydi",
                    "Chunki xodimlar bir maktabda oʻqigan",
                    "Chunki qonun shunday talab qiladi",
                    "Chunki yapon tilida boshqa soʻz yoʻq",
                ],
                "answer": 0,
                "explanation": "<strong>決まった形だ。店員は作らない。覚える。</strong> "
                               "Oʻzbekchada ham «xush kelibsiz», «yana "
                               "keling» — siz ularni yasamaysiz.",
            },
            {
                "text": "«<ruby>千円<rt>せんえん</rt></ruby>になります» nega notoʻgʻri hisoblanadi?",
                "choices": [
                    "Chunki narx «boʻlmaydi» — u shunchaki shu",
                    "Chunki 千円 juda arzon",
                    "Chunki bu juda qisqa",
                    "Chunki なる I guruh feʼli",
                ],
                "answer": 0,
                "explanation": "Toʻgʻrisi — <strong>千円でございます</strong>. "
                               "Lekin matn aytadi: uzun gap muloyim "
                               "eshitiladi, shuning uchun bu shakl "
                               "qolgan.",
            },
            {
                "text": "<ruby>最後<rt>さいご</rt></ruby>の<ruby>文<rt>ぶん</rt></ruby>「<ruby>敬語<rt>けいご</rt></ruby>は<ruby>聞<rt>き</rt></ruby>くためだ」nimani anglatadi?",
                "choices": [
                    "Keigoni gapirish uchun emas, eshitganini tushunish uchun oʻrganish kerak",
                    "Keigoni umuman oʻrganish shart emas",
                    "Keigo faqat xodimlar uchun",
                    "Keigo faqat yozma tilda kerak",
                ],
                "answer": 0,
                "explanation": "Chet ellikdan keigo kutilmaydi — «ありがとう» "
                               "yetadi. Lekin xodimning gapini "
                               "tushunmasangiz, <strong>会話が止まる</strong>.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "ちちと おとうさん",
        "summary": (
            "PJ-72 matni. Uyga mehmon keladi va bola bir kunda bitta "
            "narsani oʻrganadi: otasi ikki xil ataladi, va qaysi "
            "birini tanlash kim eshitayotganiga bogʻliq."
        ),
        "order":   72,
        "grammar": [
            {
                "pattern":  "<ruby>内<rt>うち</rt></ruby> pasayadi, <ruby>外<rt>そと</rt></ruby> koʻtariladi",
                "meaning":  "Oʻz guruhim — oilam, ishxonam — tashqi "
                            "odam oldida pasaytiriladi.",
                "examples": ["<ruby>父<rt>ちち</rt></ruby>はおりません。",
                             "お<ruby>父<rt>とう</rt></ruby>さんはいらっしゃいますか。"],
            },
            {
                "pattern":  "Oila aʼzolarining ikki nomi",
                "meaning":  "父 / お父さん, 母 / お母さん, 兄 / お兄さん "
                            "— birinchisi meniki, ikkinchisi sizniki.",
                "examples": ["<ruby>母<rt>はは</rt></ruby>は<ruby>先生<rt>せんせい</rt></ruby>です。",
                             "お<ruby>母<rt>かあ</rt></ruby>さんはお<ruby>元気<rt>げんき</rt></ruby>ですか。"],
            },
            {
                "pattern":  "Chegara siljiydi",
                "meaning":  "Bir xil odam goh ichkarida, goh "
                            "tashqarida boʻladi — tinglovchiga qarab.",
                "examples": ["<ruby>家<rt>いえ</rt></ruby>で: お<ruby>父<rt>とう</rt></ruby>さん。"],
            },
        ],
        "body": '''<p><ruby>日曜日<rt>にちようび</rt></ruby>の<ruby>午後<rt>ごご</rt></ruby>、イノムさんの<ruby>家<rt>いえ</rt></ruby>に<ruby>父<rt>ちち</rt></ruby>の<ruby>友<rt>とも</rt></ruby>だちが<ruby>来<rt>き</rt></ruby>た。イノムさんは<ruby>十二歳<rt>じゅうにさい</rt></ruby>の<ruby>弟<rt>おとうと</rt></ruby>と<ruby>一緒<rt>いっしょ</rt></ruby>に<ruby>玄関<rt>げんかん</rt></ruby>へ<ruby>出<rt>で</rt></ruby>た。</p>

<p><strong>おきゃく:</strong> こんにちは。お<ruby>父<rt>とう</rt></ruby>さんはいらっしゃいますか。</p>

<p><ruby>弟<rt>おとうと</rt></ruby>が<ruby>先<rt>さき</rt></ruby>に<ruby>答<rt>こた</rt></ruby>えた。</p>

<p><strong>おとうと:</strong> はい、お<ruby>父<rt>とう</rt></ruby>さんはいらっしゃいます。</p>

<p>イノムさんは<span class="cn-word" data-tr="ukasiga qaradi"><ruby>弟<rt>おとうと</rt></ruby>を<ruby>見<rt>み</rt></ruby>た</span>。そして<ruby>静<rt>しず</rt></ruby>かに<ruby>言<rt>い</rt></ruby>い<ruby>直<rt>なお</rt></ruby>した。</p>

<p><strong>イノム:</strong> はい、<ruby>父<rt>ちち</rt></ruby>はおります。<ruby>少々<rt>しょうしょう</rt></ruby>お<ruby>待<rt>ま</rt></ruby>ちください。</p>

<p><ruby>客<rt>きゃく</rt></ruby>が<ruby>帰<rt>かえ</rt></ruby>ってから、<ruby>弟<rt>おとうと</rt></ruby>が<ruby>聞<rt>き</rt></ruby>いた。</p>

<p><strong>おとうと:</strong> どうして「お<ruby>父<rt>とう</rt></ruby>さん」はだめですか。<ruby>家<rt>いえ</rt></ruby>でいつも<ruby>言<rt>い</rt></ruby>っています。</p>

<p>イノムさんは<ruby>紙<rt>かみ</rt></ruby>に<ruby>丸<rt>まる</rt></ruby>を<ruby>一<rt>ひと</rt></ruby>つ<ruby>書<rt>か</rt></ruby>いた。<ruby>中<rt>なか</rt></ruby>に「ぼくたち」と<ruby>書<rt>か</rt></ruby>いた。<ruby>外<rt>そと</rt></ruby>に「おきゃく」と<ruby>書<rt>か</rt></ruby>いた。</p>

<p><strong>イノム:</strong> <ruby>内<rt>うち</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>は<ruby>下<rt>さ</rt></ruby>げます。<ruby>外<rt>そと</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>は<ruby>上<rt>あ</rt></ruby>げます。<ruby>父<rt>ちち</rt></ruby>は<ruby>内<rt>うち</rt></ruby>です。</p>

<p><strong>おとうと:</strong> じゃ、<ruby>家<rt>いえ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>では。</p>

<p><strong>イノム:</strong> <ruby>家<rt>いえ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>には<span class="cn-word" data-tr="tashqi odam yoʻq"><ruby>外<rt>そと</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>がいません</span>。だから「お<ruby>父<rt>とう</rt></ruby>さん」でいいです。</p>

<p><ruby>弟<rt>おとうと</rt></ruby>はしばらく<ruby>丸<rt>まる</rt></ruby>を<ruby>見<rt>み</rt></ruby>ていた。そして<ruby>一<rt>ひと</rt></ruby>つ<ruby>質問<rt>しつもん</rt></ruby>をした。</p>

<p><strong>おとうと:</strong> <ruby>丸<rt>まる</rt></ruby>は<ruby>動<rt>うご</rt></ruby>きますか。</p>

<p>イノムさんは<ruby>笑<rt>わら</rt></ruby>った。<ruby>弟<rt>おとうと</rt></ruby>は<ruby>一番<rt>いちばん</rt></ruby><ruby>大切<rt>たいせつ</rt></ruby>なことを<ruby>聞<rt>き</rt></ruby>いた。</p>''',
        "questions": [
            {
                "text": "<ruby>弟<rt>おとうと</rt></ruby>の<ruby>答<rt>こた</rt></ruby>えのどこが<ruby>間違<rt>まちが</rt></ruby>っていましたか。",
                "choices": [
                    "Mehmonga oʻz otasini お父さん deb, いらっしゃいます bilan koʻtardi",
                    "Juda sekin javob berdi",
                    "Mehmonni ichkariga taklif qilmadi",
                    "Otasining ismini aytdi",
                ],
                "answer": 0,
                "explanation": "Oʻz oilangiz — <strong>内</strong>. Tashqi "
                               "odam oldida u pasaytiriladi: "
                               "<strong>父はおります</strong>.",
            },
            {
                "text": "イノムさんは<ruby>紙<rt>かみ</rt></ruby>に<ruby>何<rt>なに</rt></ruby>を<ruby>書<rt>か</rt></ruby>きましたか。",
                "choices": [
                    "Bitta doira — ichida «biz», tashqarisida «mehmon»",
                    "Ikkita ustun",
                    "Feʼllar roʻyxati",
                    "Oila aʼzolarining ismlari",
                ],
                "answer": 0,
                "explanation": "内 va 外 — bu ikki roʻyxat emas, "
                               "<strong>bitta chegara</strong>. Shuning "
                               "uchun uni chizib koʻrsatish eng oson "
                               "yoʻl.",
            },
            {
                "text": "<ruby>弟<rt>おとうと</rt></ruby>の<ruby>最後<rt>さいご</rt></ruby>の<ruby>質問<rt>しつもん</rt></ruby>nega muhim?",
                "choices": [
                    "Chunki chegara haqiqatan ham siljiydi — bu butun tizimning kaliti",
                    "Chunki u doira chizishni oʻrgandi",
                    "Chunki u mehmonni yoqtirmadi",
                    "Chunki u javobni bilardi",
                ],
                "answer": 0,
                "explanation": "«<strong>丸は動きますか</strong>» — ha, "
                               "harakat qiladi. Bir xil odam ertalab 内 "
                               "da, tushdan keyin 外 da boʻlishi mumkin. "
                               "Shuning uchun keigo yodlash emas, qayerda "
                               "turganingizni sezish mashqi.",
            },
        ],
    },
]
