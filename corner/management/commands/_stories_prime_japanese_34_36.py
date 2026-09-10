# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-34 … PJ-36.

PJ-34 ない-shakli · PJ-35 た-shakli va tajriba · PJ-36 〜たり.
⚠️ PJ-34 matnida た-shakli YOʻQ, PJ-35 da 〜たり YOʻQ — har biri faqat oʻz
   darsigacha berilganini ishlatadi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_34_36.py --author=prime
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
        "title":   "としょかんで まもる ことと まもらない こと",
        "summary": (
            "PJ-34 matni. Kutubxonachi yangi oʻquvchilarga qoidalarni "
            "tushuntiradi — 〜ないでください va 〜てはいけません yonma-yon, "
            "va ular bir xil emas."
        ),
        "order":   34,
        "grammar": [
            {
                "pattern":  "ない-shakli",
                "meaning":  "Feʼlning inkor oʻzagi. I guruh あ qatorini oladi, "
                            "II guruhda る tushadi.",
                "examples": ["<ruby>走<rt>はし</rt></ruby>る → <ruby>走<rt>はし</rt></ruby>らない",
                             "<ruby>食<rt>た</rt></ruby>べる → <ruby>食<rt>た</rt></ruby>べない"],
            },
            {
                "pattern":  "〜ないでください",
                "meaning":  "«Iltimos, qilmang» — shaxsiy iltimos. "
                            "〜てはいけません esa qoida: ikkalasi bir xil emas.",
                "examples": ["<ruby>忘<rt>わす</rt></ruby>れないでください。",
                             "ここで<ruby>食<rt>た</rt></ruby>べないでください。"],
            },
            {
                "pattern":  "ある → ない",
                "meaning":  "Yagona feʼl bunday tutadi: inkorda feʼlning oʻzi "
                            "yoʻqoladi. «あらない» degan soʻz yoʻq.",
                "examples": ["<ruby>時間<rt>じかん</rt></ruby>がありません。"],
            },
        ],
        "body": '''<p>ラノさんとパリさんは<span class="cn-word" data-tr="birinchi marta"><ruby>初<rt>はじ</rt></ruby>めて</span><ruby>大学<rt>だいがく</rt></ruby>の<ruby>図書館<rt>としょかん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きました。<span class="cn-word" data-tr="kutubxonachi"><ruby>司書<rt>ししょ</rt></ruby></span>のやまもとさんが<ruby>規則<rt>きそく</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えています。</p>

<p><strong>やまもと:</strong> <ruby>図書館<rt>としょかん</rt></ruby>で<ruby>食<rt>た</rt></ruby>べてはいけません。<ruby>走<rt>はし</rt></ruby>ってはいけません。これは<ruby>規則<rt>きそく</rt></ruby>です。</p>

<p><strong>やまもと:</strong> それから、<ruby>本<rt>ほん</rt></ruby>に<ruby>書<rt>か</rt></ruby>かないでください。<span class="cn-word" data-tr="unutmang"><ruby>忘<rt>わす</rt></ruby>れないで</span>ください。</p>

<p><strong>パリ:</strong> すみません、「いけません」と「ないでください」は<ruby>同<rt>おな</rt></ruby>じですか。</p>

<p><strong>やまもと:</strong> いいえ。「いけません」は<ruby>規則<rt>きそく</rt></ruby>です。「ないでください」は<span class="cn-word" data-tr="iltimos"><ruby>私<rt>わたし</rt></ruby>のお<ruby>願<rt>ねが</rt></ruby>い</span>です。</p>

<p><strong>ラノ:</strong> <ruby>本<rt>ほん</rt></ruby>を<ruby>家<rt>いえ</rt></ruby>へ<ruby>持<rt>も</rt></ruby>って<ruby>帰<rt>かえ</rt></ruby>ってもいいですか。</p>

<p><strong>やまもと:</strong> はい、いいですよ。でも<ruby>二週間<rt>にしゅうかん</rt></ruby>です。<span class="cn-word" data-tr="rioya qiling"><ruby>規則<rt>きそく</rt></ruby>を<ruby>守<rt>まも</rt></ruby>って</span>ください。</p>

<p><strong>パリ:</strong> <ruby>今日<rt>きょう</rt></ruby>は<ruby>時間<rt>じかん</rt></ruby>がありません。<ruby>明日<rt>あした</rt></ruby><ruby>来<rt>き</rt></ruby>ます。</p>

<p><ruby>二人<rt>ふたり</rt></ruby>は<ruby>規則<rt>きそく</rt></ruby>を<span class="cn-word" data-tr="daftar">ノート</span>に<ruby>書<rt>か</rt></ruby>いています。</p>''',
        "questions": [
            {
                "text": "やまもとさんによると、「いけません」と「ないでください」の<ruby>違<rt>ちが</rt></ruby>いは<ruby>何<rt>なん</rt></ruby>ですか。",
                "choices": [
                    "Birinchisi qoida, ikkinchisi shaxsiy iltimos",
                    "Birinchisi shaxsiy iltimos, ikkinchisi qoida",
                    "Farqi yoʻq, ikkalasi bir xil",
                    "Birinchisi muloyimroq",
                ],
                "answer": 0,
                "explanation": "«「いけません」は 規則です。「ないでください」は 私の "
                               "お願いです» — birinchisi kutubxonaning qoidasi, "
                               "ikkinchisi kutubxonachining <strong>oʻz iltimosi</strong>. "
                               "Grammatika emas, kimning gapi ekani hal qiladi.",
            },
            {
                "text": "ラノさんは<ruby>何<rt>なに</rt></ruby>を<ruby>聞<rt>き</rt></ruby>きましたか。",
                "choices": [
                    "<ruby>図書館<rt>としょかん</rt></ruby>で<ruby>食<rt>た</rt></ruby>べてもいいですか",
                    "<ruby>本<rt>ほん</rt></ruby>を<ruby>家<rt>いえ</rt></ruby>へ<ruby>持<rt>も</rt></ruby>って<ruby>帰<rt>かえ</rt></ruby>ってもいいですか",
                    "<ruby>本<rt>ほん</rt></ruby>に<ruby>書<rt>か</rt></ruby>いてもいいですか",
                    "<ruby>図書館<rt>としょかん</rt></ruby>で<ruby>走<rt>はし</rt></ruby>ってもいいですか",
                ],
                "answer": 1,
                "explanation": "«本を 家へ 持って 帰ってもいいですか» — kitobni uyga "
                               "olib ketsa boʻladimi. Javob: <strong>はい、いいですよ</strong>, "
                               "lekin ikki hafta muddat bilan.",
            },
            {
                "text": "「<ruby>時間<rt>じかん</rt></ruby>がありません」— ある feʼlining ない-shakli qanday?",
                "choices": [
                    "あらない",
                    "ない",
                    "ありない",
                    "あるない",
                ],
                "answer": 1,
                "explanation": "<strong>ない</strong> — feʼlning oʻzi butunlay "
                               "yoʻqoladi. Bu butun tildagi yagona shunday feʼl, va "
                               "uning muloyim shaklini siz PJ-16 dan beri bilasiz: "
                               "<strong>ありません</strong>.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "にほんへ いった ことが ありますか",
        "summary": (
            "PJ-35 matni. Sinfda tajriba haqida suhbat — kim nima qilib "
            "koʻrgan. Matn 〜たことがあります va «まだありません» ustida turadi."
        ),
        "order":   35,
        "grammar": [
            {
                "pattern":  "た-shakli",
                "meaning":  "て-shaklining oxirgi harfi almashadi: て → た, "
                            "で → だ. Boshqa hech narsa oʻzgarmaydi.",
                "examples": ["<ruby>行<rt>い</rt></ruby>って → <ruby>行<rt>い</rt></ruby>った",
                             "<ruby>読<rt>よ</rt></ruby>んで → <ruby>読<rt>よ</rt></ruby>んだ"],
            },
            {
                "pattern":  "〜たことがあります",
                "meaning":  "«Qilganman» — tajriba. こと «ish» degan ot, "
                            "shuning uchun が oladi va ある bilan tugaydi.",
                "examples": ["<ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>ったことがあります。"],
            },
            {
                "pattern":  "まだありません",
                "meaning":  "«Hali yoʻq». Yolgʻiz ありません quruq eshitiladi; "
                            "まだ eshikni ochiq qoldiradi.",
                "examples": ["いいえ、まだありません。"],
            },
        ],
        "body": '''<p><ruby>教室<rt>きょうしつ</rt></ruby>でイノムさんとムニラさんとイムロンさんが<ruby>話<rt>はな</rt></ruby>しています。</p>

<p><strong>イノム:</strong> ムニラさんは<ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>ったことがありますか。</p>

<p><strong>ムニラ:</strong> はい、あります。<ruby>三年前<rt>さんねんまえ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きました。<ruby>京都<rt>きょうと</rt></ruby>で<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>りました。</p>

<p><strong>イムロン:</strong> <span class="cn-word" data-tr="Fuji togʻi"><ruby>富士山<rt>ふじさん</rt></ruby></span>に<span class="cn-word" data-tr="chiqqan"><ruby>登<rt>のぼ</rt></ruby>った</span>ことがありますか。</p>

<p><strong>ムニラ:</strong> いいえ、<span class="cn-word" data-tr="hali">まだ</span>ありません。<ruby>時間<rt>じかん</rt></ruby>がありませんでした。</p>

<p><strong>イノム:</strong> <ruby>私<rt>わたし</rt></ruby>は<ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>ったことがありません。でも<span class="cn-word" data-tr="sushi">すし</span>を<ruby>食<rt>た</rt></ruby>べたことがあります。</p>

<p><strong>イムロン:</strong> <ruby>私<rt>わたし</rt></ruby>もあります。タシケントの<ruby>店<rt>みせ</rt></ruby>で<ruby>食<rt>た</rt></ruby>べました。とても<span class="cn-word" data-tr="mazali"><ruby>美味<rt>おい</rt></ruby>しかった</span>です。</p>

<p><strong>ムニラ:</strong> <ruby>日本<rt>にほん</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>に<span class="cn-word" data-tr="uchrashgan"><ruby>会<rt>あ</rt></ruby>った</span>ことがありますか。</p>

<p><strong>イノム:</strong> はい、あります。<ruby>大学<rt>だいがく</rt></ruby>で<ruby>先生<rt>せんせい</rt></ruby>に<ruby>会<rt>あ</rt></ruby>いました。<ruby>日本語<rt>にほんご</rt></ruby>で<ruby>話<rt>はな</rt></ruby>しました。</p>''',
        "questions": [
            {
                "text": "ムニラさんは<ruby>富士山<rt>ふじさん</rt></ruby>に<ruby>登<rt>のぼ</rt></ruby>りましたか。",
                "choices": [
                    "はい、<ruby>三年前<rt>さんねんまえ</rt></ruby>に<ruby>登<rt>のぼ</rt></ruby>りました",
                    "いいえ、まだ<ruby>登<rt>のぼ</rt></ruby>ったことがありません",
                    "はい、<ruby>京都<rt>きょうと</rt></ruby>で<ruby>登<rt>のぼ</rt></ruby>りました",
                    "いいえ、<ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>ったことがありません",
                ],
                "answer": 1,
                "explanation": "«いいえ、まだ ありません» — hali chiqmagan, chunki "
                               "vaqti boʻlmagan. Yaponiyaga esa borgan: uch yil "
                               "oldin Kiotoda rasmga olgan.",
            },
            {
                "text": "«<ruby>三年前<rt>さんねんまえ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きました» — なぜ「<ruby>行<rt>い</rt></ruby>ったことがあります」ではありませんか。",
                "choices": [
                    "Aniq vaqt aytilgan, shuning uchun oddiy oʻtgan zamon",
                    "行く — I guruh feʼli boʻlgani uchun",
                    "Gap juda uzun boʻlgani uchun",
                    "Yaponiya uzoq boʻlgani uchun",
                ],
                "answer": 0,
                "explanation": "Tajriba qolipi <strong>qachonligi aytilmaganda</strong> "
                               "ishlatiladi. «三年前» aniq vaqt — u bilan oddiy oʻtgan "
                               "zamon keladi. Munira avval «あります» deb tajribani "
                               "aytdi, keyin tafsilotga oʻtdi.",
            },
            {
                "text": "イノムさんについて<ruby>正<rt>ただ</rt></ruby>しいのはどれですか。",
                "choices": [
                    "<ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>ったことがありますが、すしを<ruby>食<rt>た</rt></ruby>べたことがありません",
                    "<ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>ったことがありませんが、すしを<ruby>食<rt>た</rt></ruby>べたことがあります",
                    "<ruby>日本<rt>にほん</rt></ruby>へも<ruby>行<rt>い</rt></ruby>って、すしも<ruby>食<rt>た</rt></ruby>べました",
                    "<ruby>日本<rt>にほん</rt></ruby>へも<ruby>行<rt>い</rt></ruby>ったことがありません、すしも<ruby>食<rt>た</rt></ruby>べたことがありません",
                ],
                "answer": 1,
                "explanation": "«日本へ 行ったことが ありません。でも すしを 食べた "
                               "ことが あります» — Yaponiyada boʻlmagan, lekin sushi "
                               "yeb koʻrgan. Va yapon oʻqituvchisi bilan ham uchrashgan.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "にちようびに なにを したり しますか",
        "summary": (
            "PJ-36 matni. Uch doʻstning dam olish kuni — har biri oʻz "
            "ishlarini 〜たり bilan sanaydi, yaʼni roʻyxatni ochiq qoldiradi."
        ),
        "order":   36,
        "grammar": [
            {
                "pattern":  "〜たり〜たりします",
                "meaning":  "«Shunaqa ishlar qilaman». Roʻyxat OCHIQ qoladi — "
                            "て bilan ulashdan farqi shu.",
                "examples": ["<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>んだり、<ruby>音楽<rt>おんがく</rt></ruby>を<ruby>聞<rt>き</rt></ruby>いたりします。"],
            },
            {
                "pattern":  "Zamon oxirida",
                "meaning":  "たり qismlari oʻzgarmaydi. Butun gapning zamonini "
                            "faqat oxirgi する tashiydi.",
                "examples": ["<ruby>泳<rt>およ</rt></ruby>いだり、<ruby>遊<rt>あそ</rt></ruby>んだりしました。"],
            },
            {
                "pattern":  "〜たり〜たり — takrorlanish",
                "meaning":  "Qarama-qarshi juftlikda maʼno «misol» emas, "
                            "«u yoq-bu yoq, takror-takror» boʻladi.",
                "examples": ["<ruby>行<rt>い</rt></ruby>ったり<ruby>来<rt>き</rt></ruby>たりします。"],
            },
        ],
        "body": '''<p><ruby>金曜日<rt>きんようび</rt></ruby>の<ruby>夕方<rt>ゆうがた</rt></ruby>です。<ruby>三人<rt>さんにん</rt></ruby>は<ruby>日曜日<rt>にちようび</rt></ruby>の<ruby>話<rt>はなし</rt></ruby>をしています。</p>

<p><strong>ラノ:</strong> みなさんは<ruby>日曜日<rt>にちようび</rt></ruby>に<ruby>何<rt>なに</rt></ruby>をしたりしますか。</p>

<p><strong>パリ:</strong> <ruby>家<rt>いえ</rt></ruby>で<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>んだり、<span class="cn-word" data-tr="musiqa"><ruby>音楽<rt>おんがく</rt></ruby></span>を<ruby>聞<rt>き</rt></ruby>いたりします。<ruby>時々<rt>ときどき</rt></ruby><ruby>母<rt>はは</rt></ruby>を<span class="cn-word" data-tr="yordam beraman"><ruby>手伝<rt>てつだ</rt></ruby>ったり</span>します。</p>

<p><strong>イムロン:</strong> <ruby>私<rt>わたし</rt></ruby>は<span class="cn-word" data-tr="park"><ruby>公園<rt>こうえん</rt></ruby></span>へ<ruby>行<rt>い</rt></ruby>きます。<ruby>友<rt>とも</rt></ruby>だちに<ruby>会<rt>あ</rt></ruby>ったり、<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>ったりします。</p>

<p><strong>ラノ:</strong> <ruby>私<rt>わたし</rt></ruby>は<span class="cn-word" data-tr="dam olaman"><ruby>休<rt>やす</rt></ruby>んだり</span>、<ruby>日本語<rt>にほんご</rt></ruby>を<ruby>勉強<rt>べんきょう</rt></ruby>したりします。でも<ruby>先週<rt>せんしゅう</rt></ruby>の<ruby>日曜日<rt>にちようび</rt></ruby>は<span class="cn-word" data-tr="band"><ruby>忙<rt>いそが</rt></ruby>しかった</span>です。</p>

<p><strong>パリ:</strong> <ruby>何<rt>なに</rt></ruby>をしましたか。</p>

<p><strong>ラノ:</strong> <span class="cn-word" data-tr="tozalash"><ruby>掃除<rt>そうじ</rt></ruby></span>したり、<ruby>買<rt>か</rt></ruby>い<ruby>物<rt>もの</rt></ruby>したりしました。<ruby>一日<rt>いちにち</rt></ruby><ruby>家<rt>いえ</rt></ruby>と<ruby>店<rt>みせ</rt></ruby>を<ruby>行<rt>い</rt></ruby>ったり<ruby>来<rt>き</rt></ruby>たりしました。</p>

<p><strong>イムロン:</strong> それは<ruby>大変<rt>たいへん</rt></ruby>でしたね。</p>''',
        "questions": [
            {
                "text": "パリさんは<ruby>日曜日<rt>にちようび</rt></ruby>に<ruby>何<rt>なに</rt></ruby>をしたりしますか。",
                "choices": [
                    "<ruby>公園<rt>こうえん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>ったり、<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>ったりします",
                    "<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>んだり、<ruby>音楽<rt>おんがく</rt></ruby>を<ruby>聞<rt>き</rt></ruby>いたりします",
                    "<ruby>掃除<rt>そうじ</rt></ruby>したり、<ruby>買<rt>か</rt></ruby>い<ruby>物<rt>もの</rt></ruby>したりします",
                    "<ruby>休<rt>やす</rt></ruby>んだり、<ruby>勉強<rt>べんきょう</rt></ruby>したりします",
                ],
                "answer": 1,
                "explanation": "«家で 本を 読んだり、音楽を 聞いたりします» — uyda kitob "
                               "oʻqiydi va musiqa tinglaydi. Parkka boradigani Imron, "
                               "tozalagani esa Rano oʻtgan yakshanba kuni.",
            },
            {
                "text": "「<ruby>行<rt>い</rt></ruby>ったり<ruby>来<rt>き</rt></ruby>たりしました」bu yerda nima maʼnoni beradi?",
                "choices": [
                    "Borib-kelib turdi — takror-takror",
                    "Bordi va qaytmadi",
                    "Bormoqchi edi",
                    "Bir marta bordi",
                ],
                "answer": 0,
                "explanation": "Qarama-qarshi juftlikda 〜たり〜たり «misol» emas, "
                               "<strong>takrorlanish</strong> bildiradi: kun boʻyi uy "
                               "bilan doʻkon orasida borib-kelib turgan.",
            },
            {
                "text": "«<ruby>掃除<rt>そうじ</rt></ruby>したり、<ruby>買<rt>か</rt></ruby>い<ruby>物<rt>もの</rt></ruby>したりしました» — nega oxirida しました turadi?",
                "choices": [
                    "Chunki zamonni faqat oxirgi する tashiydi",
                    "Chunki 掃除する — III guruh feʼli",
                    "Chunki ikkita ish sanalgan",
                    "Chunki gap savol emas",
                ],
                "answer": 0,
                "explanation": "たり qismlari <strong>hech qachon oʻzgarmaydi</strong>. "
                               "Gapda haqiqiy kesim bitta — oxirgi する — va butun "
                               "gapning zamoni ham, muloyimligi ham oʻshanda.",
            },
        ],
    },
]
