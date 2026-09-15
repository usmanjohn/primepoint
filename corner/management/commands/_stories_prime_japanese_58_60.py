# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-58 … PJ-60.

Hikoyachi 普通体 da (PJ-45 dan beri), qoʻshtirnoq ichi です・ます ni
saqlaydi.

Shakl navbati: 58 — kichik falokat hikoyasi, 59 — tayyorgarlik
hikoyasi, 60 — odat/bayram haqida hikoya. Oldingi batchda sport
hikoyasi / intervyu / oʻzgarish hikoyasi boʻlgan edi.

⚠️ CUMULATIVE: 58 da ておく/てみる yoʻq, 58 va 59 da あげる/くれる/もらう
yoʻq. Uchalasida ham 〜てあげる/〜てくれる/〜てもらう YOʻQ — ular PJ-61 da.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_58_60.py --author=prime
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
        "title":   "けして しまった",
        "summary": (
            "PJ-58 matni. Inom inshosini topshirishdan bir kun oldin "
            "faylni oʻchirib qoʻyadi — va matn boshdan-oyoq "
            "〜てしまう ustida yuradi."
        ),
        "order":   58,
        "grammar": [
            {
                "pattern":  "て-shakli + しまう — afsus",
                "meaning":  "«…ib qoʻymoq». Ish xohlanmagan holda "
                            "sodir boʻlgan, va gapda afsus bor.",
                "examples": ["<ruby>消<rt>け</rt></ruby>してしまった。",
                             "<ruby>忘<rt>わす</rt></ruby>れてしまった。"],
            },
            {
                "pattern":  "て-shakli + しまう — tugatish",
                "meaning":  "«…ib boʻlmoq». Ishdan hech nima "
                            "qolmadi. Qaysi maʼno ekanini feʼlning "
                            "oʻzi koʻrsatadi.",
                "examples": ["<ruby>全部<rt>ぜんぶ</rt></ruby><ruby>書<rt>か</rt></ruby>いてしまった。"],
            },
            {
                "pattern":  "<ruby>壊<rt>こわ</rt></ruby>す / <ruby>壊<rt>こわ</rt></ruby>れる",
                "meaning":  "PJ-57 dagi する / なる chizigʻi: す — men "
                            "qildim, れる — oʻzi boʻldi. Afsus qolipiga "
                            "koʻpincha ikkinchisi qoʻshiladi.",
                "examples": ["パソコンが<ruby>壊<rt>こわ</rt></ruby>れてしまった。"],
            },
        ],
        "body": '''<p><ruby>木曜日<rt>もくようび</rt></ruby>の<ruby>夜<rt>よる</rt></ruby>、イノムさんは<span class="cn-word" data-tr="insho"><ruby>作文<rt>さくぶん</rt></ruby></span>を<ruby>書<rt>か</rt></ruby>いていた。<ruby>三時間<rt>さんじかん</rt></ruby><ruby>書<rt>か</rt></ruby>いた。やっと<ruby>全部<rt>ぜんぶ</rt></ruby><ruby>書<rt>か</rt></ruby>いてしまった。</p>

<p><ruby>疲<rt>つか</rt></ruby>れていた。<ruby>目<rt>め</rt></ruby>が<ruby>痛<rt>いた</rt></ruby>かった。パソコンの<span class="cn-word" data-tr="tugma">ボタン</span>を<ruby>押<rt>お</rt></ruby>した。そして<ruby>画面<rt>がめん</rt></ruby>を<ruby>見<rt>み</rt></ruby>た。</p>

<p><ruby>作文<rt>さくぶん</rt></ruby>がなかった。<span class="cn-word" data-tr="oʻchirib qoʻydim"><ruby>消<rt>け</rt></ruby>してしまった</span>。</p>

<p>イノムさんは<ruby>十分間<rt>じゅっぷんかん</rt></ruby><ruby>動<rt>うご</rt></ruby>かなかった。それから<ruby>母<rt>はは</rt></ruby>を<ruby>呼<rt>よ</rt></ruby>んだ。<ruby>母<rt>はは</rt></ruby>はパソコンを<ruby>見<rt>み</rt></ruby>た。</p>

<p><strong>はは:</strong> ここを<ruby>見<rt>み</rt></ruby>てください。<ruby>古<rt>ふる</rt></ruby>いファイルがあります。</p>

<p><ruby>古<rt>ふる</rt></ruby>いファイルは<ruby>一時間前<rt>いちじかんまえ</rt></ruby>のものだった。<ruby>半分<rt>はんぶん</rt></ruby>あった。イノムさんは<ruby>座<rt>すわ</rt></ruby>った。そして<ruby>残<rt>のこ</rt></ruby>りをもう<ruby>一度<rt>いちど</rt></ruby><ruby>書<rt>か</rt></ruby>いた。</p>

<p><ruby>二時<rt>にじ</rt></ruby>に<ruby>終<rt>お</rt></ruby>わった。<ruby>今度<rt>こんど</rt></ruby>は<ruby>三<rt>みっ</rt></ruby>つの<ruby>場所<rt>ばしょ</rt></ruby>に<ruby>保存<rt>ほぞん</rt></ruby>した。</p>

<p><ruby>金曜日<rt>きんようび</rt></ruby>、<ruby>先生<rt>せんせい</rt></ruby>が<ruby>作文<rt>さくぶん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>んだ。そして<ruby>言<rt>い</rt></ruby>った。</p>

<p><strong>せんせい:</strong> これはとてもいいです。<ruby>二番目<rt>にばんめ</rt></ruby>の<ruby>半分<rt>はんぶん</rt></ruby>が<ruby>特<rt>とく</rt></ruby>にいいです。</p>

<p>イノムさんは<ruby>笑<rt>わら</rt></ruby>った。<span class="cn-word" data-tr="ikkinchi yarmi"><ruby>二番目<rt>にばんめ</rt></ruby>の<ruby>半分<rt>はんぶん</rt></ruby></span>は<ruby>二度目<rt>にどめ</rt></ruby>に<ruby>書<rt>か</rt></ruby>いたものだった。</p>''',
        "questions": [
            {
                "text": "イノムさんはパソコンで<ruby>何<rt>なに</rt></ruby>をしてしまいましたか。",
                "choices": [
                    "Inshosini oʻchirib qoʻydi",
                    "Kompyuterni sindirib qoʻydi",
                    "Faylni notoʻgʻri joyga saqladi",
                    "Uxlab qoldi",
                ],
                "answer": 0,
                "explanation": "<strong>消してしまった</strong> — «oʻchirib "
                               "qoʻydi». Bu afsus maʼnosi: «oʻchirmoq» "
                               "feʼlining bu yerda yaxshi tomoni yoʻq.",
            },
            {
                "text": "«<ruby>全部<rt>ぜんぶ</rt></ruby><ruby>書<rt>か</rt></ruby>いてしまった» va «<ruby>消<rt>け</rt></ruby>してしまった» — nega ikki xil maʼno?",
                "choices": [
                    "Birinchisi vazifa edi va tugadi; ikkinchisi xohlanmagan edi",
                    "Birinchisi hozirgi, ikkinchisi oʻtgan zamon",
                    "Birinchisi muloyim, ikkinchisi oddiy",
                    "Ikkalasi ham afsus bildiradi",
                ],
                "answer": 0,
                "explanation": "Bitta qolip, ikki maʼno — va qaysi biri "
                               "ekanini <strong>feʼlning oʻzi</strong> "
                               "koʻrsatadi. Oʻzbekchada ham «yozib "
                               "boʻldim» va «oʻchirib qoʻydim».",
            },
            {
                "text": "<ruby>先生<rt>せんせい</rt></ruby>はどの<ruby>部分<rt>ぶぶん</rt></ruby>を<ruby>特<rt>とく</rt></ruby>に<ruby>褒<rt>ほ</rt></ruby>めましたか。",
                "choices": [
                    "Ikkinchi yarmini — yaʼni ikkinchi marta yozilganini",
                    "Birinchi yarmini",
                    "Sarlavhasini",
                    "Hech qaysi qismini",
                ],
                "answer": 0,
                "explanation": "二番目の半分は二度目に書いたものだった — "
                               "oʻchirib qoʻygani uni yaxshiroq yozishga "
                               "majbur qilgan edi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "ぶんかさいの じゅんび",
        "summary": (
            "PJ-59 matni. Sinf madaniyat bayramiga taom doʻkoni "
            "tayyorlaydi — ておく butun matn boʻylab tayyorgarlikni, "
            "てみる esa sinab koʻrishni olib yuradi."
        ),
        "order":   59,
        "grammar": [
            {
                "pattern":  "て-shakli + おく",
                "meaning":  "«Oldindan qilib qoʻymoq». Ish hozir "
                            "qilinadi, foydasi keyin koʻrinadi.",
                "examples": ["<ruby>材料<rt>ざいりょう</rt></ruby>を<ruby>買<rt>か</rt></ruby>っておいた。",
                             "<ruby>机<rt>つくえ</rt></ruby>を<ruby>並<rt>なら</rt></ruby>べておいた。"],
            },
            {
                "pattern":  "て-shakli + みる",
                "meaning":  "«Qilib koʻrmoq» — ikkala tilda ham "
                            "yordamchi feʼl «koʻrmoq».",
                "examples": ["<ruby>作<rt>つく</rt></ruby>ってみた。", "<ruby>食<rt>た</rt></ruby>べてみてください。"],
            },
            {
                "pattern":  "Yordamchi feʼl kana bilan",
                "meaning":  "おく va みる yordamchi boʻlganda "
                            "kanjisini yoʻqotadi: 置く emas おく, "
                            "見る emas みる.",
                "examples": ["<ruby>書<rt>か</rt></ruby>いておきます。", "<ruby>着<rt>き</rt></ruby>てみます。"],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="madaniyat bayrami"><ruby>文化祭<rt>ぶんかさい</rt></ruby></span>まで<ruby>三日<rt>みっか</rt></ruby>だった。ムニラさんのクラスは<ruby>食<rt>た</rt></ruby>べ<ruby>物<rt>もの</rt></ruby>の<ruby>店<rt>みせ</rt></ruby>をする。メニューは<span class="cn-word" data-tr="osh"><ruby>お米<rt>こめ</rt></ruby>の<ruby>料理<rt>りょうり</rt></ruby></span>だった。</p>

<p><ruby>水曜日<rt>すいようび</rt></ruby>、ムニラさんは<ruby>家<rt>いえ</rt></ruby>で<ruby>一度<rt>いちど</rt></ruby><ruby>作<rt>つく</rt></ruby>ってみた。<ruby>味<rt>あじ</rt></ruby>が<ruby>薄<rt>うす</rt></ruby>かった。<span class="cn-word" data-tr="tuz"><ruby>塩<rt>しお</rt></ruby></span>を<ruby>足<rt>た</rt></ruby>してみた。<ruby>今度<rt>こんど</rt></ruby>はよかった。</p>

<p><ruby>木曜日<rt>もくようび</rt></ruby>の<ruby>放課後<rt>ほうかご</rt></ruby>、みんなで<ruby>準備<rt>じゅんび</rt></ruby>した。イノムさんは<span class="cn-word" data-tr="masalliq"><ruby>材料<rt>ざいりょう</rt></ruby></span>を<ruby>買<rt>か</rt></ruby>っておいた。ラノさんは<ruby>机<rt>つくえ</rt></ruby>を<ruby>並<rt>なら</rt></ruby>べておいた。パリさんは<ruby>値段<rt>ねだん</rt></ruby>の<ruby>紙<rt>かみ</rt></ruby>を<ruby>書<rt>か</rt></ruby>いておいた。</p>

<p><strong>ムニラ:</strong> <ruby>米<rt>こめ</rt></ruby>は<ruby>今晩<rt>こんばん</rt></ruby><ruby>洗<rt>あら</rt></ruby>っておきます。<ruby>朝<rt>あさ</rt></ruby>は<ruby>時間<rt>じかん</rt></ruby>がありません。</p>

<p><ruby>金曜日<rt>きんようび</rt></ruby>の<ruby>朝<rt>あさ</rt></ruby>、<ruby>七時<rt>しちじ</rt></ruby>に<ruby>集<rt>あつ</rt></ruby>まった。<ruby>十時<rt>じゅうじ</rt></ruby>に<ruby>店<rt>みせ</rt></ruby>が<ruby>開<rt>あ</rt></ruby>いた。</p>

<p><ruby>最初<rt>さいしょ</rt></ruby>の<ruby>客<rt>きゃく</rt></ruby>は<ruby>小<rt>ちい</rt></ruby>さい<ruby>女<rt>おんな</rt></ruby>の<ruby>子<rt>こ</rt></ruby>だった。<ruby>一口<rt>ひとくち</rt></ruby><ruby>食<rt>た</rt></ruby>べてみた。そして<ruby>母<rt>はは</rt></ruby>を<ruby>呼<rt>よ</rt></ruby>んだ。</p>

<p><ruby>十二時<rt>じゅうにじ</rt></ruby>に<ruby>料理<rt>りょうり</rt></ruby>が<ruby>全部<rt>ぜんぶ</rt></ruby>なくなってしまった。<ruby>二時<rt>にじ</rt></ruby>まで<ruby>店<rt>みせ</rt></ruby>を<ruby>開<rt>あ</rt></ruby>ける<ruby>予定<rt>よてい</rt></ruby>だった。</p>

<p><strong>ラノ:</strong> もっと<ruby>作<rt>つく</rt></ruby>っておけばよかったですね。</p>

<p>ムニラさんは<ruby>紙<rt>かみ</rt></ruby>に<span class="cn-word" data-tr="sotildi">「うりきれ」</span>と<ruby>書<rt>か</rt></ruby>いた。そして<ruby>来年<rt>らいねん</rt></ruby>のために<ruby>数<rt>かず</rt></ruby>を<ruby>書<rt>か</rt></ruby>いておいた。</p>''',
        "questions": [
            {
                "text": "ムニラさんは<ruby>水曜日<rt>すいようび</rt></ruby>に<ruby>何<rt>なに</rt></ruby>をしましたか。",
                "choices": [
                    "Uyda bir marta pishirib koʻrdi va tuz qoʻshib koʻrdi",
                    "Masalliq sotib olib qoʻydi",
                    "Stollarni tizib qoʻydi",
                    "Narx qogʻozini yozib qoʻydi",
                ],
                "answer": 0,
                "explanation": "<strong>作ってみた</strong> va "
                               "<strong>足してみた</strong> — sinab koʻrish. "
                               "てみる: qilasan va natijaga qaraysan.",
            },
            {
                "text": "«<ruby>材料<rt>ざいりょう</rt></ruby>を<ruby>買<rt>か</rt></ruby>っておいた» va «<ruby>作<rt>つく</rt></ruby>ってみた» — farqi nima?",
                "choices": [
                    "Birinchisi kelajak uchun tayyorgarlik, ikkinchisi sinash",
                    "Birinchisi sinash, ikkinchisi tayyorgarlik",
                    "Ikkalasi ham tayyorgarlik",
                    "Birinchisi rasmiy, ikkinchisi oddiy",
                ],
                "answer": 0,
                "explanation": "<strong>ておく</strong> — ish kelajakka "
                               "qaratilgan (foydasi bayramda koʻrinadi). "
                               "<strong>てみる</strong> — natijani hozir "
                               "bilmayman, shuning uchun sinaб koʻraman.",
            },
            {
                "text": "<ruby>十二時<rt>じゅうにじ</rt></ruby>に<ruby>何<rt>なに</rt></ruby>が<ruby>起<rt>お</rt></ruby>こりましたか。",
                "choices": [
                    "Taom butunlay tugab qoldi, garchi doʻkon soat ikkigacha ochiq boʻlishi kerak edi",
                    "Doʻkon yopildi",
                    "Yomgʻir yogʻdi",
                    "Yangi masalliq keltirildi",
                ],
                "answer": 0,
                "explanation": "<strong>なくなってしまった</strong> — «tugab "
                               "qoldi». Bu PJ-58 dagi afsus maʼnosi, va "
                               "shuning uchun Rano «もっと作っておけば» "
                               "deydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "おとしだま",
        "summary": (
            "PJ-60 matni. Yaponiyadagi Yangi yil odati — bolalar "
            "kattalardan pul konvertini oladi. Matn くれる va もらう "
            "bilan toʻla, chunki butun odat yoʻnalish haqida."
        ),
        "order":   60,
        "grammar": [
            {
                "pattern":  "くれる — menga keladi",
                "meaning":  "Boshqa odam MENGA (yoki oʻz odamimga) "
                            "beradi. «私にあげました» notoʻgʻri.",
                "examples": ["おじが<ruby>私<rt>わたし</rt></ruby>にお<ruby>年玉<rt>としだま</rt></ruby>をくれた。"],
            },
            {
                "pattern":  "もらう — men olaman",
                "meaning":  "Bir voqeani ikkinchi tomondan aytadi: "
                            "ega men boʻlsam もらう, boshqa odam "
                            "boʻlsa くれる.",
                "examples": ["<ruby>私<rt>わたし</rt></ruby>はおじにお<ruby>年玉<rt>としだま</rt></ruby>をもらった。"],
            },
            {
                "pattern":  "あげる — mendan chiqadi",
                "meaning":  "Men boshqa odamga beraman. Menga qarab "
                            "yoʻnala olmaydi.",
                "examples": ["<ruby>私<rt>わたし</rt></ruby>は<ruby>弟<rt>おとうと</rt></ruby>にアイスをあげた。"],
            },
        ],
        "body": '''<p><ruby>日本<rt>にほん</rt></ruby>の<ruby>正月<rt>しょうがつ</rt></ruby>に<span class="cn-word" data-tr="Yangi yil puli">お<ruby>年玉<rt>としだま</rt></ruby></span>という<ruby>習慣<rt>しゅうかん</rt></ruby>がある。<ruby>大人<rt>おとな</rt></ruby>が<ruby>子<rt>こ</rt></ruby>どもに<ruby>小<rt>ちい</rt></ruby>さい<span class="cn-word" data-tr="konvert"><ruby>袋<rt>ふくろ</rt></ruby></span>を<ruby>渡<rt>わた</rt></ruby>す。<ruby>中<rt>なか</rt></ruby>にお<ruby>金<rt>かね</rt></ruby>がある。</p>

<p><ruby>私<rt>わたし</rt></ruby>の<ruby>友<rt>とも</rt></ruby>だちのけんくんは<ruby>十歳<rt>じゅっさい</rt></ruby>だ。<ruby>去年<rt>きょねん</rt></ruby>の<ruby>正月<rt>しょうがつ</rt></ruby>、けんくんは<ruby>六人<rt>ろくにん</rt></ruby>からお<ruby>年玉<rt>としだま</rt></ruby>をもらった。</p>

<p>おじいさんがくれた。おばあさんもくれた。おじさんが<ruby>二人<rt>ふたり</rt></ruby>くれた。<ruby>近所<rt>きんじょ</rt></ruby>のおばさんもくれた。<span class="cn-word" data-tr="hammasi boʻlib"><ruby>全部<rt>ぜんぶ</rt></ruby>で</span><ruby>三万円<rt>さんまんえん</rt></ruby>になった。</p>

<p>けんくんは<ruby>妹<rt>いもうと</rt></ruby>に<ruby>千円<rt>せんえん</rt></ruby>あげた。<ruby>妹<rt>いもうと</rt></ruby>は<ruby>三歳<rt>さんさい</rt></ruby>で、まだお<ruby>年玉<rt>としだま</rt></ruby>の<ruby>意味<rt>いみ</rt></ruby>が<ruby>分<rt>わ</rt></ruby>からない。</p>

<p><strong>けん:</strong> これは<ruby>妹<rt>いもうと</rt></ruby>の<ruby>分<rt>ぶん</rt></ruby>です。ぼくがあげます。</p>

<p><ruby>母<rt>はは</rt></ruby>はけんくんのお<ruby>金<rt>かね</rt></ruby>を<span class="cn-word" data-tr="bankka qoʻydi"><ruby>銀行<rt>ぎんこう</rt></ruby>に<ruby>入<rt>い</rt></ruby>れた</span>。<ruby>子<rt>こ</rt></ruby>どもは<ruby>三千円<rt>さんぜんえん</rt></ruby>まで<ruby>使<rt>つか</rt></ruby>える。これも<ruby>習慣<rt>しゅうかん</rt></ruby>だ。</p>

<p><ruby>面白<rt>おもしろ</rt></ruby>いことがある。<ruby>大人<rt>おとな</rt></ruby>は<ruby>正月<rt>しょうがつ</rt></ruby>にお<ruby>年玉<rt>としだま</rt></ruby>をもらわない。<ruby>大人<rt>おとな</rt></ruby>は<ruby>渡<rt>わた</rt></ruby>すが、もらわない。だから<ruby>大人<rt>おとな</rt></ruby>にとって<ruby>正月<rt>しょうがつ</rt></ruby>は<ruby>高<rt>たか</rt></ruby>い<ruby>季節<rt>きせつ</rt></ruby>だ。</p>

<p>けんくんは<ruby>今年<rt>ことし</rt></ruby>も<ruby>待<rt>ま</rt></ruby>っている。<ruby>私<rt>わたし</rt></ruby>は<ruby>待<rt>ま</rt></ruby>っていない。<ruby>私<rt>わたし</rt></ruby>は<ruby>十七歳<rt>じゅうななさい</rt></ruby>だ。</p>''',
        "questions": [
            {
                "text": "お<ruby>年玉<rt>としだま</rt></ruby>とは<ruby>何<rt>なに</rt></ruby>ですか。",
                "choices": [
                    "Yangi yilda kattalar bolalarga beradigan pul konverti",
                    "Bolalar kattalarga beradigan sovgʻa",
                    "Maktabdagi mukofot",
                    "Yangi yil taomi",
                ],
                "answer": 0,
                "explanation": "<strong>大人が子どもに小さい袋を渡す。</strong> "
                               "Yaponiyadagi haqiqiy odat: 正月 da bolalar "
                               "qarindoshlardan pul oladi.",
            },
            {
                "text": "«おじいさんがくれた» — nega あげた emas?",
                "choices": [
                    "Chunki pul hikoyachining doʻstiga — «oʻz odami»ga kelyapti",
                    "Chunki bobo keksa",
                    "Chunki gap oʻtgan zamonda",
                    "Chunki pul koʻp edi",
                ],
                "answer": 0,
                "explanation": "Yoʻnalish <strong>feʼlning ichida</strong>. "
                               "Sovgʻa ichkariga kelsa — くれる; mendan "
                               "chiqsa — あげる. Oʻzbekchada esa yoʻnalish "
                               "«menga» / «unga» qoʻshimchasida turadi.",
            },
            {
                "text": "けんくんが<ruby>妹<rt>いもうと</rt></ruby>に<ruby>千円<rt>せんえん</rt></ruby>渡したとき、なぜ「あげた」ですか。",
                "choices": [
                    "Chunki pul Kendan chiqyapti — u gapning egasi",
                    "Chunki singlisi kichkina",
                    "Chunki pul koʻp emas",
                    "Chunki bu Yangi yil",
                ],
                "answer": 0,
                "explanation": "Bir matnda uchala feʼl ham bor: Ken "
                               "<strong>もらった</strong> (oldi), "
                               "qarindoshlar <strong>くれた</strong> "
                               "(unga berishdi), Ken singlisiga "
                               "<strong>あげた</strong> (berdi).",
            },
        ],
    },
]
