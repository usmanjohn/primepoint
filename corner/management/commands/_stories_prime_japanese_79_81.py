# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-79 … PJ-81. Blok F ochiladi.

Hikoyachi <ruby>普通体</ruby> da (PJ-45 dan beri). Uzunlik endi Blok F
tasmasida: PJ-76…78 dan sezilarli uzunroq, N3 ga yaqin registr.

Shakl navbati: 79 — oʻy-fikr matni (bu shelfdagi birinchi 随筆), 80 —
tushuntirish matni («nega shunday?»), 81 — kichik detektiv. Oldingi
batchda telefon sahnasi / ob-havo etyudi / bir kunda ikki registr
boʻlgan edi.

⚠️ CUMULATIVE:
    79 — こと / の / という / ということ erkin. わけ (PJ-80) va
         はずがない・に違いない (PJ-81) YOʻQ.
    80 — + わけ oilasi. に違いない va はずがない hali YOʻQ.
    81 — hammasi erkin.

⚠️ 〜んです bu batchda ayniqsa oson kirib ketadi — わけ va はず bilan
u tabiiy juftlashadi. Kurs uni hech qachon bermagan, shuning uchun
hamma joyda oddiy 〜です / 〜ます yoki から ishlatilgan.
`verify_pj_stories_79_81.py` buni mexanik tekshiradi.

Audio (navbat bilan, oldingi batch Nanami da tugagan edi):
    --only 79 --voice ja-JP-KeitaNeural
    --only 80 --voice ja-JP-NanamiNeural
    --only 81 --voice ja-JP-KeitaNeural

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_79_81.py --author=prime
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
        "title":   "わからないということ",
        "summary": (
            "PJ-79 matni. Oʻqituvchi doskaga bitta gap yozadi va Rano "
            "uni tushunmaydi — keyin tushunmaganini aytishning oʻzi "
            "javob ekanini biladi. Butun matn ということ ustida yuradi."
        ),
        "order":   79,
        "grammar": [
            {
                "pattern":  "oddiy shakl + ということ",
                "meaning":  "Butun gapni bitta otga aylantiradi. "
                            "Oʻzbekcha «-lik-ni» yoki «degani» bilan "
                            "bir xil ish. Ot va な-sifat oldidan だ "
                            "ni saqlaydi.",
                "examples": ["<ruby>分<rt>わ</rt></ruby>からないということが<ruby>分<rt>わ</rt></ruby>かる。",
                             "<ruby>質問<rt>しつもん</rt></ruby>ができるということ"],
            },
            {
                "pattern":  "feʼl + こと · feʼl + の",
                "meaning":  "Feʼlni otga aylantiradi. の — koʻz bilan "
                            "koʻriladigan aniq harakat, こと — mavhum, "
                            "umumiy harakat.",
                "examples": ["<ruby>質問<rt>しつもん</rt></ruby>ができるのは<ruby>強<rt>つよ</rt></ruby>いことだ。",
                             "<ruby>大切<rt>たいせつ</rt></ruby>なことだ。"],
            },
            {
                "pattern":  "〜とはどういうことですか",
                "meaning":  "«… nima degani?» — soʻzning yoki gapning "
                            "maʼnosini soʻrash.",
                "examples": ["この<ruby>文<rt>ぶん</rt></ruby>はどういうことですか。"],
            },
        ],
        "body": '''<p><ruby>火曜日<rt>かようび</rt></ruby>の<ruby>朝<rt>あさ</rt></ruby>、<ruby>先生<rt>せんせい</rt></ruby>が<span class="cn-word" data-tr="doska"><ruby>黒板<rt>こくばん</rt></ruby></span>に<ruby>一<rt>ひと</rt></ruby>つの<ruby>文<rt>ぶん</rt></ruby>を<ruby>書<rt>か</rt></ruby>いた。「<ruby>自分<rt>じぶん</rt></ruby>が<ruby>分<rt>わ</rt></ruby>からないということが<ruby>分<rt>わ</rt></ruby>かるのは、<ruby>大切<rt>たいせつ</rt></ruby>なことだ。」</p>

<p>ラノはそれをノートに<span class="cn-word" data-tr="koʻchirib oldi"><ruby>写<rt>うつ</rt></ruby>した</span>。<ruby>字<rt>じ</rt></ruby>は<ruby>全部<rt>ぜんぶ</rt></ruby><ruby>読<rt>よ</rt></ruby>めた。でも<ruby>意味<rt>いみ</rt></ruby>は<ruby>分<rt>わ</rt></ruby>からなかった。</p>

<p><ruby>家<rt>いえ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>ってから、ラノは<span class="cn-word" data-tr="lugʻat"><ruby>辞書<rt>じしょ</rt></ruby></span>を<ruby>開<rt>ひら</rt></ruby>いた。「<ruby>大切<rt>たいせつ</rt></ruby>」という<ruby>言葉<rt>ことば</rt></ruby>の<ruby>意味<rt>いみ</rt></ruby>は<ruby>書<rt>か</rt></ruby>いてあった。しかし<ruby>文<rt>ぶん</rt></ruby><ruby>全体<rt>ぜんたい</rt></ruby>の<ruby>意味<rt>いみ</rt></ruby>は<ruby>辞書<rt>じしょ</rt></ruby>に<ruby>載<rt>の</rt></ruby>っていなかった。</p>

<p>はじめ、ラノは<ruby>先生<rt>せんせい</rt></ruby>が<ruby>書<rt>か</rt></ruby>き<span class="cn-word" data-tr="xato qilgan"><ruby>間違<rt>まちが</rt></ruby>えた</span>と<ruby>思<rt>おも</rt></ruby>った。<ruby>同<rt>おな</rt></ruby>じ<ruby>言葉<rt>ことば</rt></ruby>が<ruby>二回<rt>にかい</rt></ruby>も<ruby>入<rt>はい</rt></ruby>っている<ruby>文<rt>ぶん</rt></ruby>を<ruby>見<rt>み</rt></ruby>たことがなかったからだ。しかしノートを<ruby>三回<rt>さんかい</rt></ruby><ruby>読<rt>よ</rt></ruby>んでも、<ruby>字<rt>じ</rt></ruby>は<ruby>正<rt>ただ</rt></ruby>しかった。</p>

<p><ruby>夜<rt>よる</rt></ruby>、ラノは<ruby>兄<rt>あに</rt></ruby>に<ruby>聞<rt>き</rt></ruby>いた。</p>

<p><strong>ラノ:</strong> お<ruby>兄<rt>にい</rt></ruby>さん、この<ruby>文<rt>ぶん</rt></ruby>はどういうことですか。</p>

<p><ruby>兄<rt>あに</rt></ruby>は<ruby>少<rt>すこ</rt></ruby>し<ruby>笑<rt>わら</rt></ruby>った。</p>

<p><strong>あに:</strong> ラノは<ruby>今<rt>いま</rt></ruby>、「<ruby>分<rt>わ</rt></ruby>からない」と<ruby>言<rt>い</rt></ruby>いましたね。それが<ruby>答<rt>こた</rt></ruby>えですよ。</p>

<p>ラノは<span class="cn-word" data-tr="hayron boʻldi"><ruby>驚<rt>おどろ</rt></ruby>いた</span>。<ruby>自分<rt>じぶん</rt></ruby>が<ruby>何<rt>なに</rt></ruby>を<ruby>分<rt>わ</rt></ruby>かっていないか<ruby>言<rt>い</rt></ruby>えるということ。それは、<ruby>分<rt>わ</rt></ruby>かっていないということに<span class="cn-word" data-tr="sezgan, payqagan"><ruby>気<rt>き</rt></ruby>づいている</span>ということだ。<ruby>気<rt>き</rt></ruby>づいていない<ruby>人<rt>ひと</rt></ruby>は、<ruby>質問<rt>しつもん</rt></ruby>をすることもできない。</p>

<p><ruby>次<rt>つぎ</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>、ラノは<ruby>先生<rt>せんせい</rt></ruby>に<ruby>質問<rt>しつもん</rt></ruby>した。<ruby>先生<rt>せんせい</rt></ruby>は<ruby>嬉<rt>うれ</rt></ruby>しそうだった。</p>

<p><strong>せんせい:</strong> <ruby>質問<rt>しつもん</rt></ruby>ができるということは、もう<ruby>半分<rt>はんぶん</rt></ruby><ruby>分<rt>わ</rt></ruby>かっているということですよ。</p>

<p>その<ruby>日<rt>ひ</rt></ruby>の<ruby>夜<rt>よる</rt></ruby>、ラノはノートの<ruby>最後<rt>さいご</rt></ruby>のページに<ruby>大<rt>おお</rt></ruby>きく<ruby>書<rt>か</rt></ruby>いた。「『<ruby>分<rt>わ</rt></ruby>からない』と<ruby>言<rt>い</rt></ruby>えるのは、<span class="cn-word" data-tr="kuchli, dadil"><ruby>強<rt>つよ</rt></ruby>い</span>ことだ。」</p>''',
        "questions": [
            {
                "text": "ラノは<ruby>先生<rt>せんせい</rt></ruby>の<ruby>文<rt>ぶん</rt></ruby>をノートに<ruby>写<rt>うつ</rt></ruby>したあと、どうなりましたか。",
                "choices": [
                    "<ruby>字<rt>じ</rt></ruby>は<ruby>読<rt>よ</rt></ruby>めたが、<ruby>意味<rt>いみ</rt></ruby>は<ruby>分<rt>わ</rt></ruby>からなかった",
                    "<ruby>字<rt>じ</rt></ruby>も<ruby>意味<rt>いみ</rt></ruby>も<ruby>分<rt>わ</rt></ruby>からなかった",
                    "すぐに<ruby>意味<rt>いみ</rt></ruby>が<ruby>分<rt>わ</rt></ruby>かった",
                    "<ruby>先生<rt>せんせい</rt></ruby>にすぐ<ruby>質問<rt>しつもん</rt></ruby>した",
                ],
                "answer": 0,
                "explanation": "Matnda aniq aytilgan: harflarni oʻqiy "
                               "oldi, lekin maʼnosini tushunmadi. "
                               "Oʻqituvchiga savolni faqat keyingi kuni "
                               "berdi.",
            },
            {
                "text": "<ruby>兄<rt>あに</rt></ruby>はどうしてラノの<ruby>質問<rt>しつもん</rt></ruby>が<ruby>答<rt>こた</rt></ruby>えだと<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "<ruby>分<rt>わ</rt></ruby>からないということに<ruby>気<rt>き</rt></ruby>づいていたから",
                    "ラノが<ruby>辞書<rt>じしょ</rt></ruby>を<ruby>開<rt>ひら</rt></ruby>いたから",
                    "ラノが<ruby>先生<rt>せんせい</rt></ruby>に<ruby>質問<rt>しつもん</rt></ruby>したから",
                    "ラノがノートに<ruby>書<rt>か</rt></ruby>いたから",
                ],
                "answer": 0,
                "explanation": "«Tushunmayapman» deyish — tushunmagan "
                               "narsangizni <strong>sezib turganingiz</strong> "
                               "degani. Matn buni ということ bilan aytadi: "
                               "分かっていないということに気づいている.",
            },
            {
                "text": "「<ruby>質問<rt>しつもん</rt></ruby>ができるということは、もう<ruby>半分<rt>はんぶん</rt></ruby><ruby>分<rt>わ</rt></ruby>かっているということですよ。」 — <ruby>先生<rt>せんせい</rt></ruby>は<ruby>何<rt>なに</rt></ruby>を<ruby>言<rt>い</rt></ruby>いたかったのですか。",
                "choices": [
                    "<ruby>質問<rt>しつもん</rt></ruby>ができる<ruby>人<rt>ひと</rt></ruby>は、もう<ruby>大切<rt>たいせつ</rt></ruby>なことに<ruby>気<rt>き</rt></ruby>づいている",
                    "<ruby>質問<rt>しつもん</rt></ruby>は<ruby>半分<rt>はんぶん</rt></ruby>だけしてもいい",
                    "<ruby>質問<rt>しつもん</rt></ruby>をする<ruby>人<rt>ひと</rt></ruby>は<ruby>何<rt>なに</rt></ruby>も<ruby>分<rt>わ</rt></ruby>かっていない",
                    "<ruby>答<rt>こた</rt></ruby>えは<ruby>辞書<rt>じしょ</rt></ruby>に<ruby>載<rt>の</rt></ruby>っている",
                ],
                "answer": 0,
                "explanation": "Bitta gapda ということ ikki marta "
                               "ishlatilgan: birinchisi shartni, "
                               "ikkinchisi xulosani otga aylantiradi. "
                               "«Savol bera olish» — allaqachon "
                               "yarmini tushunish degani.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "かようびの パンや",
        "summary": (
            "PJ-80 matni. Pari har hafta boradigan nonvoyxona faqat "
            "seshanba kuni yopiq. Nega? Javob topilganda «それで…"
            "わけだ» deyish uchun tayyor sahna chiqadi."
        ),
        "order":   80,
        "grammar": [
            {
                "pattern":  "oddiy shakl + わけだ / わけです",
                "meaning":  "«Shuning uchun … ekan-da». Yangi xabar "
                            "bermaydi — tanish narsani endi topilgan "
                            "sababga ulaydi. な-sifat な ni, ot "
                            "という ni oladi.",
                "examples": ["それで<ruby>火曜日<rt>かようび</rt></ruby>は<ruby>休<rt>やす</rt></ruby>みなわけだ。"],
            },
            {
                "pattern":  "〜わけではありません",
                "meaning":  "Qisman inkor — «… degani emas». "
                            "Toʻgʻridan-toʻgʻri «yoʻq» deyish qoʻpol "
                            "boʻlgan joyda ishlatiladi.",
                "examples": ["<ruby>楽<rt>らく</rt></ruby>なわけではありません。"],
            },
            {
                "pattern":  "〜わけにはいきません",
                "meaning":  "«… ning iloji yoʻq» — qobiliyat haqida "
                            "emas: qila olasiz, lekin vada yoki burch "
                            "yoʻl bermaydi.",
                "examples": ["<ruby>休<rt>やす</rt></ruby>むわけにはいきません。"],
            },
        ],
        "body": '''<p><ruby>駅<rt>えき</rt></ruby>の<ruby>近<rt>ちか</rt></ruby>くに<ruby>小<rt>ちい</rt></ruby>さいパン<ruby>屋<rt>や</rt></ruby>がある。パリは<ruby>毎週<rt>まいしゅう</rt></ruby>そこでパンを<ruby>買<rt>か</rt></ruby>う。<ruby>店<rt>みせ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>はやさしいおじさんで、いつも<ruby>一<rt>ひと</rt></ruby>つおまけをくれる。</p>

<p>ただ、<ruby>一<rt>ひと</rt></ruby>つだけ<ruby>分<rt>わ</rt></ruby>からないことがあった。<ruby>火曜日<rt>かようび</rt></ruby>だけ<ruby>店<rt>みせ</rt></ruby>が<span class="cn-word" data-tr="yopiq"><ruby>閉<rt>し</rt></ruby>まっている</span>。<ruby>日曜日<rt>にちようび</rt></ruby>は<ruby>開<rt>あ</rt></ruby>いているのに、<ruby>火曜日<rt>かようび</rt></ruby>はいつも<ruby>暗<rt>くら</rt></ruby>い。</p>

<p>ある<ruby>火曜日<rt>かようび</rt></ruby>の<ruby>午前<rt>ごぜん</rt></ruby>、パリは<ruby>小学校<rt>しょうがっこう</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>を<span class="cn-word" data-tr="oʻtib ketdi"><ruby>通<rt>とお</rt></ruby>った</span>。<ruby>中<rt>なか</rt></ruby>から<ruby>子供<rt>こども</rt></ruby>たちの<ruby>声<rt>こえ</rt></ruby>が<ruby>聞<rt>き</rt></ruby>こえた。<ruby>窓<rt>まど</rt></ruby>から<ruby>見<rt>み</rt></ruby>ると、あのおじさんが<ruby>白<rt>しろ</rt></ruby>い<ruby>服<rt>ふく</rt></ruby>を<ruby>着<rt>き</rt></ruby>て、パンの<span class="cn-word" data-tr="tayyorlash usuli"><ruby>作<rt>つく</rt></ruby>り<ruby>方<rt>かた</rt></ruby></span>を<ruby>教<rt>おし</rt></ruby>えていた。</p>

<p>それで<ruby>火曜日<rt>かようび</rt></ruby>は<ruby>休<rt>やす</rt></ruby>みなわけだ、とパリは<ruby>思<rt>おも</rt></ruby>った。</p>

<p><ruby>次<rt>つぎ</rt></ruby>の<ruby>土曜日<rt>どようび</rt></ruby>、パリは<ruby>店<rt>みせ</rt></ruby>でおじさんに<ruby>聞<rt>き</rt></ruby>いてみた。</p>

<p><strong>パリ:</strong> おじさん、<ruby>火曜日<rt>かようび</rt></ruby>は<ruby>小学校<rt>しょうがっこう</rt></ruby>で<ruby>教<rt>おし</rt></ruby>えていらっしゃいますね。</p>

<p><strong>おじさん:</strong> はい。もう<ruby>十年<rt>じゅうねん</rt></ruby>になります。<ruby>市<rt>し</rt></ruby>の<ruby>先生<rt>せんせい</rt></ruby>に<ruby>頼<rt>たの</rt></ruby>まれましてね。</p>

<p><strong>パリ:</strong> お<ruby>休<rt>やす</rt></ruby>みの<ruby>日<rt>ひ</rt></ruby>なのに、<ruby>大変<rt>たいへん</rt></ruby>ではありませんか。</p>

<p><strong>おじさん:</strong> <span class="cn-word" data-tr="oson, yengil"><ruby>楽<rt>らく</rt></ruby></span>なわけではありません。でも、<ruby>子供<rt>こども</rt></ruby>たちの<ruby>顔<rt>かお</rt></ruby>を<ruby>見<rt>み</rt></ruby>ると、<ruby>休<rt>やす</rt></ruby>むわけにはいきません。</p>

<p>おじさんは<ruby>言<rt>い</rt></ruby>った。パンが<ruby>好<rt>す</rt></ruby>きな<ruby>子供<rt>こども</rt></ruby>は、パンを<ruby>作<rt>つく</rt></ruby>る<ruby>人<rt>ひと</rt></ruby>も<ruby>好<rt>す</rt></ruby>きになる。そういう<ruby>子供<rt>こども</rt></ruby>が<ruby>十年後<rt>じゅうねんご</rt></ruby>に<ruby>店<rt>みせ</rt></ruby>を<ruby>継<rt>つ</rt></ruby>ぐかもしれない。だから<ruby>火曜日<rt>かようび</rt></ruby>は<ruby>店<rt>みせ</rt></ruby>より<ruby>大切<rt>たいせつ</rt></ruby>だ。</p>

<p>その<ruby>日<rt>ひ</rt></ruby>、パリはいつもより<ruby>多<rt>おお</rt></ruby>くパンを<ruby>買<rt>か</rt></ruby>った。<ruby>火曜日<rt>かようび</rt></ruby>の<ruby>暗<rt>くら</rt></ruby>い<ruby>店<rt>みせ</rt></ruby>が、<ruby>前<rt>まえ</rt></ruby>より<span class="cn-word" data-tr="yorugʻ, nurli"><ruby>明<rt>あか</rt></ruby>るく</span><ruby>見<rt>み</rt></ruby>えた。</p>''',
        "questions": [
            {
                "text": "<ruby>火曜日<rt>かようび</rt></ruby>に<ruby>店<rt>みせ</rt></ruby>が<ruby>閉<rt>し</rt></ruby>まっているのはどうしてですか。",
                "choices": [
                    "おじさんが<ruby>小学校<rt>しょうがっこう</rt></ruby>でパンの<ruby>作<rt>つく</rt></ruby>り<ruby>方<rt>かた</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えているから",
                    "おじさんが<ruby>病気<rt>びょうき</rt></ruby>だから",
                    "<ruby>火曜日<rt>かようび</rt></ruby>はお<ruby>客<rt>きゃく</rt></ruby>さんが<ruby>少<rt>すく</rt></ruby>ないから",
                    "パンの<ruby>材料<rt>ざいりょう</rt></ruby>がないから",
                ],
                "answer": 0,
                "explanation": "Pari buni oyna orqali koʻrdi va shundan "
                               "keyin <strong>それで火曜日は休みなわけだ</strong> "
                               "dedi — «shuning uchun seshanba yopiq "
                               "ekan-da». わけ yangi xabar bermaydi, "
                               "koʻrilgan narsani sababga ulaydi.",
            },
            {
                "text": "「<ruby>楽<rt>らく</rt></ruby>なわけではありません。」 — おじさんは<ruby>何<rt>なに</rt></ruby>を<ruby>言<rt>い</rt></ruby>いたかったのですか。",
                "choices": [
                    "<ruby>楽<rt>らく</rt></ruby>だとは<ruby>言<rt>い</rt></ruby>えないが、やめるつもりもない",
                    "<ruby>本当<rt>ほんとう</rt></ruby>はとても<ruby>楽<rt>らく</rt></ruby>だ",
                    "<ruby>今年<rt>ことし</rt></ruby>でやめる",
                    "<ruby>学校<rt>がっこう</rt></ruby>が<ruby>嫌<rt>きら</rt></ruby>いだ",
                ],
                "answer": 0,
                "explanation": "わけではありません butun gapni emas, undan "
                               "chiqadigan <strong>xulosani</strong> inkor "
                               "qiladi — «oson degani emas». Keyingi gap "
                               "buni tasdiqlaydi: 休むわけにはいきません.",
            },
            {
                "text": "「<ruby>休<rt>やす</rt></ruby>むわけにはいきません。」 — これはどういう<ruby>意味<rt>いみ</rt></ruby>ですか。",
                "choices": [
                    "<ruby>休<rt>やす</rt></ruby>むことはできるが、<ruby>休<rt>やす</rt></ruby>んではいけないと<ruby>思<rt>おも</rt></ruby>っている",
                    "<ruby>体<rt>からだ</rt></ruby>が<ruby>弱<rt>よわ</rt></ruby>くて<ruby>休<rt>やす</rt></ruby>めない",
                    "<ruby>店<rt>みせ</rt></ruby>が<ruby>忙<rt>いそが</rt></ruby>しくて<ruby>休<rt>やす</rt></ruby>めない",
                    "<ruby>学校<rt>がっこう</rt></ruby>が<ruby>休<rt>やす</rt></ruby>ませてくれない",
                ],
                "answer": 0,
                "explanation": "わけにはいきません qobiliyat haqida emas. "
                               "Jismonan dam ola oladi — lekin bolalarning "
                               "yuzini koʻrgandan keyin vijdoni yoʻl "
                               "bermaydi. Qobiliyat uchun PJ-42 dagi "
                               "休めません kerak boʻlardi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "だれの てぶくろ",
        "summary": (
            "PJ-81 matni. Sinfda bitta qoʻlqop qolib ketadi va Munira "
            "bilan Inom uni kimniki ekanini mantiq bilan topadi. "
            "はずがありません bilan eshiklar yopiladi, "
            "に違いありません bilan bittasi ochiladi."
        ),
        "order":   81,
        "grammar": [
            {
                "pattern":  "oddiy shakl + はずがありません",
                "meaning":  "«… boʻlishi mumkin emas» — dalilga "
                            "asoslangan qatʼiy rad. Ot はず oldida "
                            "の ni oladi.",
                "examples": ["ラノさんのはずがありません。",
                             "<ruby>先生<rt>せんせい</rt></ruby>のはずがありません。"],
            },
            {
                "pattern":  "oddiy shakl + に<ruby>違<rt>ちが</rt></ruby>いありません",
                "meaning":  "«Shubhasiz …» — eng kuchli taxmin. "
                            "Hamma soʻz turiga yalangʻoch ulanadi: "
                            "ot ham, な-sifat ham qoʻshimcha olmaydi.",
                "examples": ["サッカー<ruby>部<rt>ぶ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>に<ruby>違<rt>ちが</rt></ruby>いありません。"],
            },
            {
                "pattern":  "〜はずだったのに",
                "meaning":  "«… boʻlishi kerak edi, lekin boʻlmadi» — "
                            "amalga oshmagan reja, afsus bilan.",
                "examples": ["<ruby>金曜日<rt>きんようび</rt></ruby>に<ruby>返<rt>かえ</rt></ruby>すはずだったのに。"],
            },
        ],
        "body": '''<p><ruby>金曜日<rt>きんようび</rt></ruby>の<span class="cn-word" data-tr="darslardan keyin"><ruby>放課後<rt>ほうかご</rt></ruby></span>、<ruby>教室<rt>きょうしつ</rt></ruby>に<ruby>手袋<rt>てぶくろ</rt></ruby>が<ruby>片方<rt>かたほう</rt></ruby><ruby>落<rt>お</rt></ruby>ちていた。<ruby>青<rt>あお</rt></ruby>くて、とても<ruby>大<rt>おお</rt></ruby>きい<ruby>手袋<rt>てぶくろ</rt></ruby>だった。ムニラはそれを<span class="cn-word" data-tr="terib oldi"><ruby>拾<rt>ひろ</rt></ruby>った</span>。</p>

<p><strong>ムニラ:</strong> これ、だれのでしょうか。</p>

<p><strong>イノム:</strong> ラノさんのはずがありませんよ。ラノさんは<ruby>今日<rt>きょう</rt></ruby><ruby>休<rt>やす</rt></ruby>みでしたから。</p>

<p><strong>ムニラ:</strong> そうですね。じゃ、<ruby>田中<rt>たなか</rt></ruby><ruby>先生<rt>せんせい</rt></ruby>のでしょうか。</p>

<p><strong>イノム:</strong> <ruby>先生<rt>せんせい</rt></ruby>は<ruby>今朝<rt>けさ</rt></ruby>、<ruby>白<rt>しろ</rt></ruby>い<ruby>手袋<rt>てぶくろ</rt></ruby>をしていました。<ruby>先生<rt>せんせい</rt></ruby>のはずがありません。</p>

<p><ruby>二人<rt>ふたり</rt></ruby>は<ruby>考<rt>かんが</rt></ruby>えた。<ruby>放課後<rt>ほうかご</rt></ruby>にこの<ruby>教室<rt>きょうしつ</rt></ruby>にいたのは、<ruby>三人<rt>さんにん</rt></ruby>だけだった。そして<ruby>手袋<rt>てぶくろ</rt></ruby>は、ムニラの<ruby>手<rt>て</rt></ruby>より<ruby>二<rt>ふた</rt></ruby>まわり<ruby>大<rt>おお</rt></ruby>きかった。<ruby>女子<rt>じょし</rt></ruby>の<ruby>手袋<rt>てぶくろ</rt></ruby>のはずがない。</p>

<p>イノムは<ruby>窓<rt>まど</rt></ruby>の<ruby>外<rt>そと</rt></ruby>を<ruby>見<rt>み</rt></ruby>た。<span class="cn-word" data-tr="maktab hovlisi"><ruby>校庭<rt>こうてい</rt></ruby></span>で<ruby>青<rt>あお</rt></ruby>い<ruby>服<rt>ふく</rt></ruby>の<ruby>生徒<rt>せいと</rt></ruby>たちが<ruby>走<rt>はし</rt></ruby>っていた。</p>

<p><strong>イノム:</strong> サッカー<ruby>部<rt>ぶ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>に<ruby>違<rt>ちが</rt></ruby>いありません。<ruby>今日<rt>きょう</rt></ruby>、この<ruby>教室<rt>きょうしつ</rt></ruby>で<ruby>会議<rt>かいぎ</rt></ruby>がありましたから。</p>

<p><strong>ムニラ:</strong> でも、<ruby>部員<rt>ぶいん</rt></ruby>は<ruby>二十人<rt>にじゅうにん</rt></ruby>もいますよ。</p>

<p>ムニラは<ruby>手袋<rt>てぶくろ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>を<ruby>見<rt>み</rt></ruby>た。<ruby>小<rt>ちい</rt></ruby>さい<ruby>字<rt>じ</rt></ruby>で<ruby>名前<rt>なまえ</rt></ruby>が<ruby>書<rt>か</rt></ruby>いてあった。<ruby>二人<rt>ふたり</rt></ruby>は<span class="cn-word" data-tr="hayron boʻlishdi"><ruby>驚<rt>おどろ</rt></ruby>いた</span>。<ruby>本当<rt>ほんとう</rt></ruby>にサッカー<ruby>部<rt>ぶ</rt></ruby>の<ruby>三年生<rt>さんねんせい</rt></ruby>だった。</p>

<p><ruby>手袋<rt>てぶくろ</rt></ruby>は<ruby>金曜日<rt>きんようび</rt></ruby>に<ruby>返<rt>かえ</rt></ruby>すはずだったのに、<ruby>持<rt>も</rt></ruby>ち<ruby>主<rt>ぬし</rt></ruby>はもう<ruby>帰<rt>かえ</rt></ruby>っていた。<ruby>月曜日<rt>げつようび</rt></ruby>の<ruby>朝<rt>あさ</rt></ruby>、ムニラはそれを<span class="cn-word" data-tr="oʻqituvchilar xonasi"><ruby>職員室<rt>しょくいんしつ</rt></ruby></span>に<ruby>届<rt>とど</rt></ruby>けた。<ruby>昼休<rt>ひるやす</rt></ruby>み、<ruby>大<rt>おお</rt></ruby>きな<ruby>男<rt>おとこ</rt></ruby>の<ruby>子<rt>こ</rt></ruby>が<ruby>取<rt>と</rt></ruby>りに<ruby>来<rt>き</rt></ruby>た。<ruby>手<rt>て</rt></ruby>は、やはりとても<ruby>大<rt>おお</rt></ruby>きかった。</p>''',
        "questions": [
            {
                "text": "イノムはどうしてラノさんの<ruby>手袋<rt>てぶくろ</rt></ruby>ではないと<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "ラノさんは<ruby>今日<rt>きょう</rt></ruby><ruby>学校<rt>がっこう</rt></ruby>に<ruby>来<rt>こ</rt></ruby>なかったから",
                    "ラノさんの<ruby>手袋<rt>てぶくろ</rt></ruby>は<ruby>白<rt>しろ</rt></ruby>いから",
                    "ラノさんはサッカー<ruby>部<rt>ぶ</rt></ruby>ではないから",
                    "ラノさんの<ruby>手<rt>て</rt></ruby>は<ruby>小<rt>ちい</rt></ruby>さいから",
                ],
                "answer": 0,
                "explanation": "Dalil から bilan berilgan: Rano bugun "
                               "yoʻq edi. Shundan keyin <strong>のはずが"
                               "ありません</strong> — «boʻlishi mumkin "
                               "emas». Bu shunchaki taxmin emas, "
                               "yopilgan eshik.",
            },
            {
                "text": "「サッカー<ruby>部<rt>ぶ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>に<ruby>違<rt>ちが</rt></ruby>いありません。」 — イノムはどのくらい<ruby>自信<rt>じしん</rt></ruby>がありましたか。",
                "choices": [
                    "とても<ruby>強<rt>つよ</rt></ruby>い<ruby>自信<rt>じしん</rt></ruby>があった",
                    "<ruby>半分<rt>はんぶん</rt></ruby>ぐらいの<ruby>自信<rt>じしん</rt></ruby>だった",
                    "<ruby>自信<rt>じしん</rt></ruby>はまったくなかった",
                    "ムニラに<ruby>聞<rt>き</rt></ruby>いてから<ruby>決<rt>き</rt></ruby>めた",
                ],
                "answer": 0,
                "explanation": "に違いありません — ishonch shkalasining eng "
                               "yuqori pogʻonasi. かもしれません «boʻlishi "
                               "mumkin», はずです «asosim bor», "
                               "に違いありません esa «shubhasiz». Matn "
                               "oxirida u haq boʻlib chiqdi.",
            },
            {
                "text": "<ruby>手袋<rt>てぶくろ</rt></ruby>はいつ<ruby>返<rt>かえ</rt></ruby>すはずでしたか。",
                "choices": [
                    "<ruby>金曜日<rt>きんようび</rt></ruby>",
                    "<ruby>月曜日<rt>げつようび</rt></ruby>",
                    "<ruby>昼休<rt>ひるやす</rt></ruby>み",
                    "<ruby>放課後<rt>ほうかご</rt></ruby>のすぐあと",
                ],
                "answer": 0,
                "explanation": "<strong>金曜日のうちに返すはずだったのに</strong> "
                               "— «juma kuni qaytarish kerak edi, lekin…». "
                               "はずだった amalga oshmagan rejani bildiradi; "
                               "のに esa afsusni qoʻshadi. Aslida dushanba "
                               "kuni qaytarildi.",
            },
        ],
    },
]
