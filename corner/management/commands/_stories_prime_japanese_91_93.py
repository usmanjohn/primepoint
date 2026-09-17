# -*- coding: utf-8 -*-
"""Prime Japanese Readings — PJ-91 … PJ-93.

Uzunlik Blok F tasmasida (190–270 soʻz).

Shakl navbati: 91 — kichik kundalik voqea (pul yetmagan kun),
92 — sogʻliq boʻyicha maslahat ustuni, 93 — bitiruv nutqi.
Oldingi batchda intervyu / soʻrov hisoboti / portret ocherki
boʻlgan edi.

Registr: 91 — 普通体 hikoya. 92 — maslahat ustuni, oʻquvchiga
murojaat qilgani uchun boshdan oxirigacha 丁寧体. 93 — nutq,
shuning uchun ham 丁寧体 (ikkalasi ham toc ning «xat va kundalik
birini tanlab oxirigacha ushlaydi» ruxsatiga kiradi).

⚠️ CUMULATIVE:
    91 — さえ, こそ, しか〜ない erkin. がち・っぽい・気味 (PJ-92) va
         おかげで・せいで (PJ-93) YOʻQ.
    92 — + moyillik oilasi. おかげで va せいで hali YOʻQ.
    93 — hammasi erkin.

⚠️ 92-matndagi maslahatlar umumiy va zararsiz: erta yotish, issiq
suv ichish, shifokorga borish. Hech qanday dori nomi yoki tibbiy
daʼvo yoʻq — bu shelf shifokor emas.

⚠️ 〜のです ham, 〜んです ham bu shelfda yozilmaydi.

Audio (navbat bilan, oldingi batch 90 da Nanami bilan tugagan edi):
    --only 91 --voice ja-JP-KeitaNeural
    --only 92 --voice ja-JP-NanamiNeural
    --only 93 --voice ja-JP-KeitaNeural

    python manage.py import_corner \
        corner/management/commands/_stories_prime_japanese_91_93.py --author=prime
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
        "title":   "せんえんしか なかった",
        "summary": (
            "PJ-91 matni. Imron doʻstiga tugʻilgan kun sovgʻasi olmoqchi, "
            "lekin hamyonida atigi ming iyena bor. Doʻkonma-doʻkon "
            "yurib, oxirida eng arzon narsani tanlaydi — va aynan "
            "oʻsha narsa eng toʻgʻrisi boʻlib chiqadi."
        ),
        "order":   91,
        "grammar": [
            {
                "pattern":  "〜しか + inkor",
                "meaning":  "«faqat …, atigi …». Gapiruvchi buni KAM deb "
                            "hisoblaydi, va feʼl albatta inkorda turadi. "
                            "が va を ni siqib chiqaradi.",
                "examples": ["<ruby>千円<rt>せんえん</rt></ruby>しかなかった。",
                             "<ruby>一<rt>ひと</rt></ruby>つしか<ruby>買<rt>か</rt></ruby>えない。"],
            },
            {
                "pattern":  "〜さえ · 〜さえ〜ば",
                "meaning":  "«hatto … ham». ば bilan birga kelsa, maʼno "
                            "«faqat … boʻlsa bas» ga oʻzgaradi.",
                "examples": ["<ruby>百円<rt>ひゃくえん</rt></ruby>さえなかった。",
                             "<ruby>気持<rt>きも</rt></ruby>ちさえあれば"],
            },
            {
                "pattern":  "〜こそ",
                "meaning":  "«aynan shu» — boshqasini rad etib, bittasini "
                            "ajratadi. こちらこそ — rahmatga javob.",
                "examples": ["これこそ<ruby>探<rt>さが</rt></ruby>していた<ruby>物<rt>もの</rt></ruby>だ。"],
            },
        ],
        "body": '''<p>イムロンは<ruby>財布<rt>さいふ</rt></ruby>を<ruby>開<rt>ひら</rt></ruby>いた。<ruby>千円<rt>せんえん</rt></ruby>しかなかった。<ruby>明日<rt>あした</rt></ruby>はムニラの<ruby>誕生日<rt>たんじょうび</rt></ruby>だ。</p>

<p><ruby>駅<rt>えき</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>の<ruby>店<rt>みせ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>った。きれいな<span class="cn-word" data-tr="sharf"><ruby>襟巻<rt>えりま</rt></ruby>き</span>があったが、<ruby>三千円<rt>さんぜんえん</rt></ruby>だった。<ruby>手<rt>て</rt></ruby>に<ruby>取<rt>と</rt></ruby>って、<ruby>戻<rt>もど</rt></ruby>した。</p>

<p><ruby>次<rt>つぎ</rt></ruby>の<ruby>店<rt>みせ</rt></ruby>では、<ruby>小<rt>ちい</rt></ruby>さな<ruby>人形<rt>にんぎょう</rt></ruby>が<ruby>千二百円<rt>せんにひゃくえん</rt></ruby>だった。あと<ruby>二百円<rt>にひゃくえん</rt></ruby>。その<ruby>二百円<rt>にひゃくえん</rt></ruby>さえなかった。</p>

<p>イムロンは<span class="cn-word" data-tr="dilgir boʻldi"><ruby>情<rt>なさ</rt></ruby>けなくなった</span>。<ruby>三年間<rt>さんねんかん</rt></ruby>の<ruby>友<rt>とも</rt></ruby>だちに、<ruby>千円<rt>せんえん</rt></ruby>の<ruby>物<rt>もの</rt></ruby>しか<ruby>買<rt>か</rt></ruby>えない。</p>

<p><ruby>兄<rt>あに</rt></ruby>に<ruby>電話<rt>でんわ</rt></ruby>してみた。<ruby>兄<rt>あに</rt></ruby>は<ruby>笑<rt>わら</rt></ruby>って、「<ruby>値段<rt>ねだん</rt></ruby>ばかり<ruby>見<rt>み</rt></ruby>ていると、いい<ruby>物<rt>もの</rt></ruby>は<ruby>見<rt>み</rt></ruby>つからないよ」と<ruby>言<rt>い</rt></ruby>った。イムロンは<ruby>意味<rt>いみ</rt></ruby>が<ruby>分<rt>わ</rt></ruby>からなかった。</p>

<p><ruby>帰<rt>かえ</rt></ruby>り<ruby>道<rt>みち</rt></ruby>、<ruby>古<rt>ふる</rt></ruby>い<span class="cn-word" data-tr="qogʻoz buyumlar doʻkoni"><ruby>文房具屋<rt>ぶんぼうぐや</rt></ruby></span>の<ruby>前<rt>まえ</rt></ruby>を<ruby>通<rt>とお</rt></ruby>った。<ruby>窓<rt>まど</rt></ruby>に<ruby>青<rt>あお</rt></ruby>い<ruby>万年筆<rt>まんねんひつ</rt></ruby>が<ruby>一本<rt>いっぽん</rt></ruby>あった。<ruby>八百円<rt>はっぴゃくえん</rt></ruby>。</p>

<p>ムニラは<ruby>毎日<rt>まいにち</rt></ruby><ruby>日記<rt>にっき</rt></ruby>を<ruby>書<rt>か</rt></ruby>いている。イムロンはそれを<ruby>思<rt>おも</rt></ruby>い<ruby>出<rt>だ</rt></ruby>した。これこそムニラに<span class="cn-word" data-tr="mos keladigan"><ruby>似合<rt>にあ</rt></ruby>う</span><ruby>物<rt>もの</rt></ruby>だ。</p>

<p><ruby>次<rt>つぎ</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>、ムニラは<ruby>箱<rt>はこ</rt></ruby>を<ruby>開<rt>あ</rt></ruby>けて、<ruby>長<rt>なが</rt></ruby>い<ruby>間<rt>あいだ</rt></ruby><ruby>何<rt>なに</rt></ruby>も<ruby>言<rt>い</rt></ruby>わなかった。</p>

<p><strong>ムニラ:</strong> どうして<ruby>分<rt>わ</rt></ruby>かったの。わたし、ずっと<ruby>青<rt>あお</rt></ruby>い<ruby>万年筆<rt>まんねんひつ</rt></ruby>がほしかった。</p>

<p><strong>イムロン:</strong> ごめん、<ruby>八百円<rt>はっぴゃくえん</rt></ruby>の<ruby>物<rt>もの</rt></ruby>しか<ruby>買<rt>か</rt></ruby>えなかった。</p>

<p><strong>ムニラ:</strong> こちらこそ、ありがとう。<ruby>値段<rt>ねだん</rt></ruby>じゃないよ。</p>

<p>イムロンは<ruby>家<rt>いえ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>って<ruby>考<rt>かんが</rt></ruby>えた。<ruby>金<rt>かね</rt></ruby>さえあれば<ruby>高<rt>たか</rt></ruby>い<ruby>物<rt>もの</rt></ruby>が<ruby>買<rt>か</rt></ruby>える。でも、<ruby>相手<rt>あいて</rt></ruby>のことを<ruby>知<rt>し</rt></ruby>っている<ruby>人<rt>ひと</rt></ruby>しか、<ruby>正<rt>ただ</rt></ruby>しい<ruby>物<rt>もの</rt></ruby>は<ruby>選<rt>えら</rt></ruby>べない。</p>''',
        "questions": [
            {
                "text": "イムロンの<ruby>財布<rt>さいふ</rt></ruby>にはいくらありましたか。",
                "choices": [
                    "<ruby>千円<rt>せんえん</rt></ruby>しかなかった",
                    "<ruby>三千円<rt>さんぜんえん</rt></ruby>あった",
                    "<ruby>千二百円<rt>せんにひゃくえん</rt></ruby>あった",
                    "<ruby>八百円<rt>はっぴゃくえん</rt></ruby>しかなかった",
                ],
                "answer": 0,
                "explanation": "Birinchi jumlada aytilgan: atigi ming "
                               "iyena. Sakkiz yuz — sovgʻaning narxi, "
                               "uch ming — sharfniki.",
            },
            {
                "text": "イムロンはどうして<ruby>万年筆<rt>まんねんひつ</rt></ruby>を<ruby>選<rt>えら</rt></ruby>びましたか。",
                "choices": [
                    "ムニラが<ruby>毎日<rt>まいにち</rt></ruby><ruby>日記<rt>にっき</rt></ruby>を<ruby>書<rt>か</rt></ruby>いているから",
                    "いちばん<ruby>安<rt>やす</rt></ruby>かったから",
                    "<ruby>店<rt>みせ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>にすすめられたから",
                    "<ruby>青<rt>あお</rt></ruby>い<ruby>色<rt>いろ</rt></ruby>が<ruby>好<rt>す</rt></ruby>きだから",
                ],
                "answer": 0,
                "explanation": "U doʻstining har kuni kundalik "
                               "yozishini esladi — «これこそ似合う物だ». "
                               "Arzonligi sabab emas, tasodif edi.",
            },
            {
                "text": "<ruby>最後<rt>さいご</rt></ruby>にイムロンは<ruby>何<rt>なに</rt></ruby>を<ruby>考<rt>かんが</rt></ruby>えましたか。",
                "choices": [
                    "<ruby>相手<rt>あいて</rt></ruby>を<ruby>知<rt>し</rt></ruby>っている<ruby>人<rt>ひと</rt></ruby>だけが<ruby>正<rt>ただ</rt></ruby>しい<ruby>物<rt>もの</rt></ruby>を<ruby>選<rt>えら</rt></ruby>べる",
                    "お<ruby>金<rt>かね</rt></ruby>がいちばん<ruby>大切<rt>たいせつ</rt></ruby>だ",
                    "<ruby>来年<rt>らいねん</rt></ruby>は<ruby>高<rt>たか</rt></ruby>い<ruby>物<rt>もの</rt></ruby>を<ruby>買<rt>か</rt></ruby>う",
                    "<ruby>友<rt>とも</rt></ruby>だちに<ruby>謝<rt>あやま</rt></ruby>るべきだ",
                ],
                "answer": 0,
                "explanation": "Pul qimmat narsa oladi, lekin "
                               "<em>toʻgʻri</em> narsani faqat "
                               "odamni biladigan kishi tanlay "
                               "oladi. Hikoyaning butun maʼnosi "
                               "shu oxirgi jumlada.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "あきは かぜぎみ",
        "summary": (
            "PJ-92 matni. Kuzda nega tez-tez shamollaymiz degan savolga "
            "javob beradigan qisqa maslahat ustuni: harorat farqi, "
            "quruq havo, kech yotish. がち, っぽい va 気味 uchalasi ham "
            "shu matnda yashaydi."
        ),
        "order":   92,
        "grammar": [
            {
                "pattern":  "ます-oʻzagi / ot + がち",
                "meaning":  "«tez-tez … boʻladi» — chastota. Ohangi "
                            "deyarli doim salbiy. Otni aniqlaganda "
                            "の oladi.",
                "examples": ["<ruby>忘<rt>わす</rt></ruby>れがちです。",
                             "<ruby>曇<rt>くも</rt></ruby>りがちの<ruby>日<rt>ひ</rt></ruby>"],
            },
            {
                "pattern":  "ot / oʻzak + っぽい",
                "meaning":  "«… simon, … ga oʻxshagan» — koʻrinish yoki "
                            "xususiyat. Natija い-sifat boʻlib tuslanadi.",
                "examples": ["<ruby>子供<rt>こども</rt></ruby>っぽい",
                             "<ruby>忘<rt>わす</rt></ruby>れっぽくなります。"],
            },
            {
                "pattern":  "ます-oʻzagi / ot + <ruby>気味<rt>ぎみ</rt></ruby>",
                "meaning":  "«bir oz …» — daraja. Gapni yumshatadi, "
                            "shuning uchun oʻz ahvoli haqida aytishda "
                            "juda koʻp ishlatiladi.",
                "examples": ["<ruby>風邪<rt>かぜ</rt></ruby><ruby>気味<rt>ぎみ</rt></ruby>です。",
                             "<ruby>疲<rt>つか</rt></ruby>れ<ruby>気味<rt>ぎみ</rt></ruby>です。"],
            },
        ],
        "body": '''<p><ruby>秋<rt>あき</rt></ruby>になると、「なんだか<ruby>風邪<rt>かぜ</rt></ruby><ruby>気味<rt>ぎみ</rt></ruby>です」と<ruby>言<rt>い</rt></ruby>う<ruby>人<rt>ひと</rt></ruby>が<ruby>増<rt>ふ</rt></ruby>えます。どうしてでしょうか。</p>

<p><ruby>一<rt>ひと</rt></ruby>つ<ruby>目<rt>め</rt></ruby>の<ruby>理由<rt>りゆう</rt></ruby>は、<ruby>朝<rt>あさ</rt></ruby>と<ruby>昼<rt>ひる</rt></ruby>の<span class="cn-word" data-tr="harorat farqi"><ruby>温度差<rt>おんどさ</rt></ruby></span>です。<ruby>秋<rt>あき</rt></ruby>は<ruby>朝<rt>あさ</rt></ruby><ruby>寒<rt>さむ</rt></ruby>くて、<ruby>昼<rt>ひる</rt></ruby><ruby>暖<rt>あたた</rt></ruby>かい<ruby>日<rt>ひ</rt></ruby>が<ruby>多<rt>おお</rt></ruby>いです。<ruby>朝<rt>あさ</rt></ruby>に<ruby>合<rt>あ</rt></ruby>わせて<ruby>服<rt>ふく</rt></ruby>を<ruby>選<rt>えら</rt></ruby>ぶと、<ruby>昼<rt>ひる</rt></ruby>は<ruby>暑<rt>あつ</rt></ruby>すぎます。<ruby>体<rt>からだ</rt></ruby>は<ruby>疲<rt>つか</rt></ruby>れがちになります。</p>

<p><ruby>二<rt>ふた</rt></ruby>つ<ruby>目<rt>め</rt></ruby>は<span class="cn-word" data-tr="quruq havo"><ruby>乾<rt>かわ</rt></ruby>いた<ruby>空気<rt>くうき</rt></ruby></span>です。<ruby>秋<rt>あき</rt></ruby>の<ruby>空気<rt>くうき</rt></ruby>は<ruby>夏<rt>なつ</rt></ruby>より<ruby>乾<rt>かわ</rt></ruby>いています。のどが<ruby>弱<rt>よわ</rt></ruby>くなり、<ruby>朝<rt>あさ</rt></ruby><ruby>起<rt>お</rt></ruby>きたとき<span class="cn-word" data-tr="isitmasi bordek"><ruby>熱<rt>ねつ</rt></ruby>っぽい</span>と<ruby>感<rt>かん</rt></ruby>じる<ruby>人<rt>ひと</rt></ruby>もいます。</p>

<p><ruby>三<rt>みっ</rt></ruby>つ<ruby>目<rt>め</rt></ruby>は<ruby>生活<rt>せいかつ</rt></ruby>です。<ruby>秋<rt>あき</rt></ruby>は<ruby>夜<rt>よる</rt></ruby>が<ruby>長<rt>なが</rt></ruby>く、<ruby>本<rt>ほん</rt></ruby>や<ruby>動画<rt>どうが</rt></ruby>で<ruby>夜更<rt>よふ</rt></ruby>かししがちです。<ruby>寝<rt>ね</rt></ruby><span class="cn-word" data-tr="uyqusizlik"><ruby>不足<rt>ぶそく</rt></ruby></span>が<ruby>続<rt>つづ</rt></ruby>くと、<ruby>忘<rt>わす</rt></ruby>れっぽくなり、<ruby>怒<rt>おこ</rt></ruby>りっぽくもなります。</p>

<p><ruby>四<rt>よっ</rt></ruby>つ<ruby>目<rt>め</rt></ruby>は<ruby>食事<rt>しょくじ</rt></ruby>です。<ruby>秋<rt>あき</rt></ruby>はおいしい<ruby>物<rt>もの</rt></ruby>が<ruby>多<rt>おお</rt></ruby>いので、つい<ruby>食<rt>た</rt></ruby>べすぎがちです。<ruby>食<rt>た</rt></ruby>べすぎた<ruby>次<rt>つぎ</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>は、<ruby>体<rt>からだ</rt></ruby>が<span class="cn-word" data-tr="ogʻir, harakatsiz"><ruby>重<rt>おも</rt></ruby>い</span>と<ruby>感<rt>かん</rt></ruby>じる<ruby>人<rt>ひと</rt></ruby>が<ruby>多<rt>おお</rt></ruby>いです。<ruby>秋<rt>あき</rt></ruby>に<ruby>太<rt>ふと</rt></ruby>り<ruby>気味<rt>ぎみ</rt></ruby>になるのは、あなただけではありません。</p>

<p>では、どうすればいいでしょうか。<ruby>特別<rt>とくべつ</rt></ruby>なことは<ruby>要<rt>い</rt></ruby>りません。<ruby>薄<rt>うす</rt></ruby>い<ruby>上着<rt>うわぎ</rt></ruby>を<ruby>一枚<rt>いちまい</rt></ruby><span class="cn-word" data-tr="olib yurmoq"><ruby>持<rt>も</rt></ruby>ち<ruby>歩<rt>ある</rt></ruby>く</span>。<ruby>温<rt>あたた</rt></ruby>かい<ruby>水<rt>みず</rt></ruby>を<ruby>少<rt>すこ</rt></ruby>しずつ<ruby>飲<rt>の</rt></ruby>む。そして、<ruby>早<rt>はや</rt></ruby>く<ruby>寝<rt>ね</rt></ruby>る。それだけで<ruby>体<rt>からだ</rt></ruby>はずいぶん<ruby>楽<rt>らく</rt></ruby>になります。</p>

<p><ruby>最後<rt>さいご</rt></ruby>に<ruby>一<rt>ひと</rt></ruby>つ。<ruby>風邪<rt>かぜ</rt></ruby><ruby>気味<rt>ぎみ</rt></ruby>のときは<ruby>無理<rt>むり</rt></ruby>をしないでください。<ruby>元気<rt>げんき</rt></ruby>な<ruby>人<rt>ひと</rt></ruby>ほど「まだ<ruby>大丈夫<rt>だいじょうぶ</rt></ruby>」と<ruby>考<rt>かんが</rt></ruby>えがちです。<ruby>熱<rt>ねつ</rt></ruby>が<ruby>出<rt>で</rt></ruby>たら、<ruby>必<rt>かなら</rt></ruby>ず<ruby>病院<rt>びょういん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きましょう。</p>''',
        "questions": [
            {
                "text": "<ruby>秋<rt>あき</rt></ruby>に<ruby>体<rt>からだ</rt></ruby>が<ruby>疲<rt>つか</rt></ruby>れがちになるのはどうしてですか。",
                "choices": [
                    "<ruby>朝<rt>あさ</rt></ruby>と<ruby>昼<rt>ひる</rt></ruby>の<ruby>温度差<rt>おんどさ</rt></ruby>が<ruby>大<rt>おお</rt></ruby>きいから",
                    "<ruby>夏<rt>なつ</rt></ruby>より<ruby>暑<rt>あつ</rt></ruby>いから",
                    "<ruby>雨<rt>あめ</rt></ruby>が<ruby>多<rt>おお</rt></ruby>いから",
                    "<ruby>food<rt>しょく</rt></ruby>が<ruby>変<rt>か</rt></ruby>わるから",
                ],
                "answer": 0,
                "explanation": "Ertalab sovuq, kunduzi issiq — "
                               "ertalabga qarab kiyinsangiz kunduzi "
                               "issiq boʻlib ketadi. Tana shu "
                               "farqdan charchaydi.",
            },
            {
                "text": "<ruby>寝<rt>ね</rt></ruby><ruby>不足<rt>ぶそく</rt></ruby>が<ruby>続<rt>つづ</rt></ruby>くとどうなりますか。",
                "choices": [
                    "<ruby>忘<rt>わす</rt></ruby>れっぽくなり、<ruby>怒<rt>おこ</rt></ruby>りっぽくなる",
                    "<ruby>声<rt>こえ</rt></ruby>が<ruby>大<rt>おお</rt></ruby>きくなる",
                    "<ruby>朝<rt>あさ</rt></ruby><ruby>早<rt>はや</rt></ruby>く<ruby>起<rt>お</rt></ruby>きられる",
                    "<ruby>空気<rt>くうき</rt></ruby>が<ruby>乾<rt>かわ</rt></ruby>く",
                ],
                "answer": 0,
                "explanation": "っぽい xususiyatni aytadi: uyqusiz "
                               "odam unutuvchan va jizzaki boʻlib "
                               "qoladi. Ovoz bogʻiqligi esa quruq "
                               "havoning natijasi.",
            },
            {
                "text": "<ruby>元気<rt>げんき</rt></ruby>な<ruby>人<rt>ひと</rt></ruby>について、<ruby>何<rt>なに</rt></ruby>と<ruby>書<rt>か</rt></ruby>いてありますか。",
                "choices": [
                    "「まだ<ruby>大丈夫<rt>だいじょうぶ</rt></ruby>」と<ruby>考<rt>かんが</rt></ruby>えがちだ",
                    "すぐ<ruby>病院<rt>びょういん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>く",
                    "<ruby>風邪<rt>かぜ</rt></ruby>をひかない",
                    "<ruby>早<rt>はや</rt></ruby>く<ruby>寝<rt>ね</rt></ruby>る",
                ],
                "answer": 0,
                "explanation": "Aynan sogʻlom odamlar oʻzini "
                               "zoʻriqtiradi — «hali boʻladi» deb "
                               "oʻylab qoʻyadi. がち shu "
                               "takrorlanadigan xatoni aytadi.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "そつぎょうの スピーチ",
        "summary": (
            "PJ-93 matni. Bitiruv kunidagi qisqa nutq: uch yil ichida "
            "kimga rahmat aytish kerakligi va bir marta hamma narsani "
            "yomgʻirdan koʻrgan kun. おかげで minnatdorchilikni, せいで "
            "esa oʻsha bitta kunni koʻtaradi."
        ),
        "order":   93,
        "grammar": [
            {
                "pattern":  "〜おかげで",
                "meaning":  "«… sharofati bilan» — natija yaxshi, gapda "
                            "minnatdorchilik bor. Ot の, な-sifat な, "
                            "feʼl oddiy shakl oladi.",
                "examples": ["<ruby>先生<rt>せんせい</rt></ruby>のおかげで<ruby>合格<rt>ごうかく</rt></ruby>しました。",
                             "<ruby>手伝<rt>てつだ</rt></ruby>ってくれたおかげで"],
            },
            {
                "pattern":  "〜せいで · 〜のせいにする",
                "meaning":  "«… dastidan» — natija yomon, gapda ayb bor. "
                            "せい ning oʻzi «ayb» degani, shuning uchun "
                            "せいにする — «ayblamoq».",
                "examples": ["<ruby>雨<rt>あめ</rt></ruby>のせいで<ruby>中止<rt>ちゅうし</rt></ruby>になりました。",
                             "<ruby>人<rt>ひと</rt></ruby>のせいにしていました。"],
            },
        ],
        "body": '''<p><ruby>今日<rt>きょう</rt></ruby>は<ruby>私<rt>わたし</rt></ruby>たちの<ruby>卒業式<rt>そつぎょうしき</rt></ruby>です。<ruby>三年<rt>さんねん</rt></ruby>という<ruby>時間<rt>じかん</rt></ruby>は、<ruby>長<rt>なが</rt></ruby>いようで<ruby>短<rt>みじか</rt></ruby>かったです。</p>

<p>まず、<ruby>先生方<rt>せんせいがた</rt></ruby>のおかげで、ここまで<ruby>来<rt>く</rt></ruby>ることができました。<ruby>私<rt>わたし</rt></ruby>は<ruby>一年生<rt>いちねんせい</rt></ruby>のとき、<ruby>数学<rt>すうがく</rt></ruby>が<span class="cn-word" data-tr="qiynaladigan fan"><ruby>苦手<rt>にがて</rt></ruby></span>でした。<ruby>山田<rt>やまだ</rt></ruby><ruby>先生<rt>せんせい</rt></ruby>が<ruby>放課後<rt>ほうかご</rt></ruby>に<ruby>教<rt>おし</rt></ruby>えてくださったおかげで、<ruby>今<rt>いま</rt></ruby>は<ruby>好<rt>す</rt></ruby>きになりました。</p>

<p><ruby>去年<rt>きょねん</rt></ruby>の<ruby>体育祭<rt>たいいくさい</rt></ruby>のことも<ruby>忘<rt>わす</rt></ruby>れられません。<ruby>朝<rt>あさ</rt></ruby>から<ruby>雨<rt>あめ</rt></ruby>で、<ruby>午後<rt>ごご</rt></ruby>の<span class="cn-word" data-tr="estafeta"><ruby>競走<rt>きょうそう</rt></ruby></span>は<ruby>雨<rt>あめ</rt></ruby>のせいで<ruby>中止<rt>ちゅうし</rt></ruby>になりました。<ruby>私<rt>わたし</rt></ruby>たちは<ruby>三<rt>さん</rt></ruby>か<ruby>月<rt>げつ</rt></ruby><ruby>練習<rt>れんしゅう</rt></ruby>していました。<ruby>教室<rt>きょうしつ</rt></ruby>でだれも<ruby>話<rt>はな</rt></ruby>しませんでした。</p>

<p>そのとき、クラスの<span class="cn-word" data-tr="sinf rahbari"><ruby>担任<rt>たんにん</rt></ruby></span>の<ruby>先生<rt>せんせい</rt></ruby>がこう<ruby>言<rt>い</rt></ruby>いました。</p>

<p><strong>せんせい:</strong> <ruby>天気<rt>てんき</rt></ruby>のせいにしても、<ruby>何<rt>なに</rt></ruby>も<ruby>変<rt>か</rt></ruby>わりませんよ。<ruby>体育館<rt>たいいくかん</rt></ruby>が<ruby>空<rt>あ</rt></ruby>いています。</p>

<p><ruby>私<rt>わたし</rt></ruby>たちは<ruby>体育館<rt>たいいくかん</rt></ruby>で<ruby>競走<rt>きょうそう</rt></ruby>をしました。<ruby>狭<rt>せま</rt></ruby>くて、<ruby>何回<rt>なんかい</rt></ruby>も<ruby>曲<rt>ま</rt></ruby>がらなければなりませんでした。でも、あの<ruby>日<rt>ひ</rt></ruby>がいちばん<ruby>楽<rt>たの</rt></ruby>しかったと、みんなが<ruby>言<rt>い</rt></ruby>います。<ruby>先生<rt>せんせい</rt></ruby>のあの<ruby>一言<rt>ひとこと</rt></ruby>のおかげです。</p>

<p><ruby>家族<rt>かぞく</rt></ruby>にも<span class="cn-word" data-tr="minnatdorman"><ruby>感謝<rt>かんしゃ</rt></ruby>しています</span>。<ruby>母<rt>はは</rt></ruby>が<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>早<rt>はや</rt></ruby>く<ruby>起<rt>お</rt></ruby>きてくれたおかげで、<ruby>私<rt>わたし</rt></ruby>は<ruby>一度<rt>いちど</rt></ruby>も<span class="cn-word" data-tr="kechikish"><ruby>遅刻<rt>ちこく</rt></ruby></span>しませんでした。</p>

<p><ruby>明日<rt>あした</rt></ruby>からは、それぞれ<ruby>別<rt>べつ</rt></ruby>の<ruby>道<rt>みち</rt></ruby>を<ruby>歩<rt>ある</rt></ruby>きます。うまくいかない<ruby>日<rt>ひ</rt></ruby>もあるはずです。そんなとき、だれかのせいにしないで、あの<ruby>体育館<rt>たいいくかん</rt></ruby>を<ruby>思<rt>おも</rt></ruby>い<ruby>出<rt>だ</rt></ruby>したいと<ruby>思<rt>おも</rt></ruby>います。</p>

<p>おかげさまで、いい<ruby>三年<rt>さんねん</rt></ruby><ruby>間<rt>かん</rt></ruby>でした。ありがとうございました。</p>''',
        "questions": [
            {
                "text": "<ruby>話<rt>はな</rt></ruby>している<ruby>人<rt>ひと</rt></ruby>は<ruby>一年生<rt>いちねんせい</rt></ruby>のとき<ruby>何<rt>なに</rt></ruby>が<ruby>苦手<rt>にがて</rt></ruby>でしたか。",
                "choices": [
                    "<ruby>数学<rt>すうがく</rt></ruby>",
                    "<ruby>体育<rt>たいいく</rt></ruby>",
                    "<ruby>日本語<rt>にほんご</rt></ruby>",
                    "<ruby>音楽<rt>おんがく</rt></ruby>",
                ],
                "answer": 0,
                "explanation": "Matematika. Yamada ustoz darsdan "
                               "keyin oʻqitgani sharofati bilan u "
                               "hozir bu fanni yaxshi koʻradi.",
            },
            {
                "text": "<ruby>担任<rt>たんにん</rt></ruby>の<ruby>先生<rt>せんせい</rt></ruby>は<ruby>何<rt>なに</rt></ruby>と<ruby>言<rt>い</rt></ruby>いましたか。",
                "choices": [
                    "<ruby>天気<rt>てんき</rt></ruby>のせいにしても<ruby>何<rt>なに</rt></ruby>も<ruby>変<rt>か</rt></ruby>わらない",
                    "<ruby>来年<rt>らいねん</rt></ruby>また<ruby>競走<rt>きょうそう</rt></ruby>をしよう",
                    "<ruby>家<rt>いえ</rt></ruby>へ<ruby>帰<rt>かえ</rt></ruby>りなさい",
                    "<ruby>雨<rt>あめ</rt></ruby>が<ruby>止<rt>や</rt></ruby>むまで<ruby>待<rt>ま</rt></ruby>とう",
                ],
                "answer": 0,
                "explanation": "«Ob-havoni ayblab nima "
                               "oʻzgaradi?» — せいにする aynan "
                               "«ayblamoq» degani. Keyin u "
                               "sport zali boʻshligini aytadi.",
            },
            {
                "text": "<ruby>話<rt>はな</rt></ruby>している<ruby>人<rt>ひと</rt></ruby>は<ruby>一度<rt>いちど</rt></ruby>も<ruby>遅刻<rt>ちこく</rt></ruby>しませんでした。どうしてですか。",
                "choices": [
                    "<ruby>母<rt>はは</rt></ruby>が<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>早<rt>はや</rt></ruby>く<ruby>起<rt>お</rt></ruby>きてくれたから",
                    "<ruby>学校<rt>がっこう</rt></ruby>が<ruby>近<rt>ちか</rt></ruby>かったから",
                    "<ruby>時計<rt>とけい</rt></ruby>を<ruby>二<rt>ふた</rt></ruby>つ<ruby>持<rt>も</rt></ruby>っていたから",
                    "<ruby>先生<rt>せんせい</rt></ruby>が<ruby>電話<rt>でんわ</rt></ruby>してくれたから",
                ],
                "answer": 0,
                "explanation": "Onasi har kuni erta turgani "
                               "sharofati bilan. おかげで bu yerda "
                               "feʼlga ulangan: 起きてくれた + "
                               "おかげで.",
            },
        ],
    },
]
