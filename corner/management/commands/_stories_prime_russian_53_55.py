# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-53 … PR-55.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 53 — uchta xat (yangi shakl: bitta kun, uch qalam),
54 — biografik hikoya, 55 — kundalik yoʻl. (50 yakuniy matn, 51
ilmiy-ommabop, 52 kundalik hikoya edi.)

Grammatika chegarasi (kumulyativ qoida):
  53-matn: vid TANLOV ekanini koʻrsatadi. Uch odam bitta kunni yozadi:
           biri jarayonni, biri natijani, uchinchisi ikkalasini. Matnning
           oxiri buni ochiq aytadi.
  54-matn: signal soʻzlar amalda — ка́ждый день, ча́сто, ре́дко (НСВ)
           va наконе́ц, за три дня (СВ). Biografik janr bu uchun ideal.
  55-matn: идти́ ↔ ходи́ть. Matnda uchala maʼno ham bor: hozir (иду́),
           muntazam (хожу́), borib-kelish (ходи́л) va qobiliyat (хо́дит).

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_53_55.py --author=prime
"""

SUBJECT = {
    "name":    "Russian",
    "summary": "Rus tili: hikoyalar, lugʻat va yozish shablonlari.",
    "icon":    "bi-translate",
    "color":   "#b91c1c",
}

COLLECTION = {
    "title":       "Prime Russian Readings",
    "description": (
        "Prime Russian darslarining oʻqish matnlari — har biri oʻz darsining "
        "grammatikasini matn ichida koʻrsatadi. Lugʻat izohlari bilan."
    ),
    "order": 3,
}

STORIES = [
    # ══════════════════════════════════════════════════════════════════
    # PR-53 — vid va zamon                       UCHTA XAT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Три письма́ об одно́м дне",
        "summary": (
            "PR-53 matni. Uch doʻst bitta shanba haqida yozadi. Kun bitta, "
            "lekin xatlar uchta — chunki har biri boshqa narsani tanlagan."
        ),
        "order":   53,
        "grammar": [
            {
                "pattern":  "НСВ — jarayon haqida yozish",
                "meaning":  "Гуля́ли, сиде́ли, говори́ли — nima QILGANI aytiladi, "
                            "natija emas. Bu shakl kunni ichkaridan koʻrsatadi.",
                "examples": ["Мы гуля́ли в па́рке. До́лго."],
            },
            {
                "pattern":  "СВ — natija haqida yozish",
                "meaning":  "Посмотре́ли, купи́ла, написа́ла — nima TUGAGANI "
                            "aytiladi. Bu shakl kunni roʻyxat sifatida koʻrsatadi.",
                "examples": ["Мы посмотре́ли фильм. Я купи́ла кни́гу."],
            },
            {
                "pattern":  "Ikkalasi bir gapda",
                "meaning":  "«Я чита́ла, но не прочита́ла» — jarayon boʻldi, natija "
                            "boʻlmadi. Bu ziddiyat emas: vid tizimining butun kuchi "
                            "aynan shunda.",
                "examples": ["Я чита́ла в авто́бусе, но не прочита́ла."],
            },
        ],
        "body": '''<p>Одна́ <span class="cn-word" data-tr="shanba">суббо́та</span>. Три <span class="cn-word" data-tr="xat">письма́</span>.</p>

<p><strong>Бекзод пи́шет:</strong></p>

<p>«Мы <strong>гуля́ли</strong> в па́рке. До́лго. Пото́м <strong>сиде́ли</strong> в кафе́ и <strong>говори́ли</strong>. О шко́ле, о ле́те, о <span class="cn-word" data-tr="filmlar">фи́льмах</span>. Хоро́ший был день».</p>

<p><strong>Катя пи́шет:</strong></p>

<p>«Мы <strong>посмотре́ли</strong> но́вый фильм. Пото́м я <strong>купи́ла</strong> кни́гу и <strong>верну́лась</strong> домо́й. Ве́чером <strong>написа́ла</strong> два письма́ и <strong>сде́лала</strong> <span class="cn-word" data-tr="uy vazifasi">уро́ки</span>».</p>

<p><strong>Афсона пи́шет:</strong></p>

<p>«Снача́ла мы до́лго <strong>гуля́ли</strong>, пото́м <strong>посмотре́ли</strong> фильм. В авто́бусе я <strong>чита́ла</strong> — но не <strong>прочита́ла</strong>. <span class="cn-word" data-pos="verb" data-tr="Qoldi">Оста́лось</span> три <span class="cn-word" data-tr="sahifa">страни́цы</span>».</p>

<p>Оди́н день. Три письма́. И <span class="cn-word" data-tr="xuddi">как бу́дто</span> три ра́зных дня.</p>

<p>Бекзод пи́шет о <span class="cn-word" data-tr="jarayon">проце́ссе</span>: что они́ <strong>де́лали</strong>.</p>

<p>Катя пи́шет о <span class="cn-word" data-tr="natija">результа́те</span>: что они́ <strong>сде́лали</strong>.</p>

<p>Афсона пи́шет о двух вме́сте.</p>

<p>Кто прав? <span class="cn-word" data-tr="Hammasi">Все</span>.</p>

<p>Вид — э́то не пра́вило. Э́то <span class="cn-word" data-tr="tanlov">вы́бор</span>: что ты хо́чешь сказа́ть.</p>''',
        "questions": [
            {
                "text": "Nega bitta kun haqidagi uchta xat shunchalik boshqacha "
                        "chiqdi?",
                "choices": [
                    "Har biri boshqa narsani tanlagan: jarayon, natija yoki ikkalasi",
                    "Ular boshqa-boshqa kunlarda uchrashgan",
                    "Bekzod hammasini unutgan",
                    "Katya kinoga bormagan"
                ],
                "answer": 0,
                "explanation": "Matn buni oxirida ochiq aytadi: Bekzod jarayon haqida "
                               "(де́лали), Katya natija haqida (сде́лали), Afsona esa "
                               "ikkalasi haqida yozgan. Kun bitta — tanlov uchta.",
            },
            {
                "text": "«Я чита́ла — но не прочита́ла» nimani anglatadi?",
                "choices": [
                    "Oʻqidi, lekin kitobni tugatmadi",
                    "Umuman oʻqimadi",
                    "Kitobni ikki marta oʻqidi",
                    "Kitobni yoʻqotdi"
                ],
                "answer": 0,
                "explanation": "Jarayon boʻldi (НСВ — чита́ла), natija boʻlmadi (СВ — "
                               "не прочита́ла). Keyingi jumla buni tasdiqlaydi: "
                               "«Оста́лось три страни́цы».",
            },
            {
                "text": "Matnning oxirgi jumlasi vid haqida nima deydi?",
                "choices": [
                    "Vid — qoida emas, balki nima aytmoqchi ekaningizni tanlash",
                    "Vid faqat yozuvda ishlatiladi",
                    "НСВ har doim toʻgʻriroq",
                    "СВ har doim toʻgʻriroq"
                ],
                "answer": 0,
                "explanation": "«Вид — э́то не пра́вило. Э́то вы́бор: что ты хо́чешь "
                               "сказа́ть». Uch xat ham toʻgʻri — ular shunchaki "
                               "kunning boshqa tomonini koʻrsatadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-54 — vidni tanlash                      BIOGRAFIK HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Как я гото́вился к экза́мену",
        "summary": (
            "PR-54 matni. Uch oylik tayyorgarlik: har kuni ikki soatdan, keyin "
            "aprelda uch kunlik yakuniy takror. Oxirida bir jumlalik xulosa."
        ),
        "order":   54,
        "grammar": [
            {
                "pattern":  "НСВ signallari",
                "meaning":  "Ка́ждый день, иногда́, ча́сто, ре́дко, два часа́ — "
                            "hammasi takror yoki davomiylikni bildiradi va НСВ "
                            "talab qiladi.",
                "examples": ["Ка́ждый день я чита́л два часа́.", "Ре́дко смотре́л фи́льмы."],
            },
            {
                "pattern":  "СВ signallari",
                "meaning":  "Наконе́ц, за три дня, оди́н раз — natija yoki muddatni "
                            "bildiradi va СВ talab qiladi. Diqqat: «два часа́» НСВ, "
                            "«за два часа́» esa СВ.",
                "examples": ["Прочита́л их за три дня.", "Наконе́ц я по́нял."],
            },
            {
                "pattern":  "Ketma-ketlik → СВ",
                "meaning":  "«Взял … прочита́л … по́нял … сдал» — birin-ketin tugagan "
                            "ishlar. Hikoyaning oxirgi qismi shu naqshda quriladi.",
                "examples": ["Я взял все тетра́ди и прочита́л их."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="imtihon">Экза́мен</span> был в ма́е. Я <strong>гото́вился</strong> три <span class="cn-word" data-tr="oy">ме́сяца</span>.</p>

<p><strong>Ка́ждый день</strong> я <strong>чита́л</strong> два часа́. <strong>Иногда́</strong> три.</p>

<p><strong>Ча́сто</strong> я <strong>писа́л</strong> слова́ в тетра́дь. <strong>Ре́дко</strong> <strong>смотре́л</strong> фи́льмы. <span class="cn-word" data-tr="Deyarli">Почти́</span> не <strong>гуля́л</strong>.</p>

<p>Э́то бы́ло <span class="cn-word" data-tr="zerikarli">ску́чно</span>. И <span class="cn-word" data-tr="uzoq">до́лго</span>.</p>

<p>В апре́ле я <strong>реши́л</strong>: <span class="cn-word" data-tr="Yetadi, boʻldi">хва́тит</span>.</p>

<p>Я <strong>взял</strong> все <span class="cn-word" data-tr="daftarlar">тетра́ди</span> и <strong>прочита́л</strong> их <strong>за три дня</strong>.</p>

<p><strong>Наконе́ц</strong> я <strong>по́нял</strong>: я зна́ю не <span class="cn-word" data-tr="hammasi">всё</span>, но мно́го.</p>

<p>В ма́е я <strong>сдал</strong> экза́мен.</p>

<p>Тепе́рь я зна́ю оди́н <span class="cn-word" data-tr="sir">секре́т</span>.</p>

<p><strong>Ка́ждый день</strong> — э́то <strong>чита́л</strong>. Три дня в апре́ле — э́то <strong>прочита́л</strong>.</p>

<p>И <span class="cn-word" data-tr="ikkinchisi">второ́е</span> не рабо́тает без <span class="cn-word" data-tr="birinchisi">пе́рвого</span>.</p>''',
        "questions": [
            {
                "text": "Matnning oxirgi jumlasi nimani anglatadi?",
                "choices": [
                    "Uch kunlik yakuniy takror faqat uch oylik mehnat ustiga qurilgani uchun ishladi",
                    "Aprelda oʻqish yetarli edi",
                    "Har kuni oʻqish foydasiz boʻldi",
                    "Imtihon oson edi"
                ],
                "answer": 0,
                "explanation": "«Ка́ждый день — э́то чита́л. Три дня в апре́ле — э́то "
                               "прочита́л. И второ́е не рабо́тает без пе́рвого». "
                               "Natija (СВ) jarayonsiz (НСВ) boʻlmaydi — bu ham "
                               "grammatik, ham hayotiy xulosa.",
            },
            {
                "text": "Nega matnda «чита́л два часа́», lekin «прочита́л за три "
                        "дня»?",
                "choices": [
                    "«Два часа́» davomiylik (НСВ), «за три дня» esa muddat (СВ)",
                    "Chunki uchinchisi koʻproq vaqt",
                    "Chunki birinchisi takroriy",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Bitta predlog butun maʼnoni oʻzgartiradi: «два часа́» "
                               "— qancha vaqt ketgani; «за три дня» — qancha vaqtda "
                               "tugagani. Birinchisi НСВ, ikkinchisi СВ chaqiradi.",
            },
            {
                "text": "Matnning oxirgi qismida nega hamma feʼl СВ da?",
                "choices": [
                    "Chunki bu ketma-ketlik: взял → прочита́л → по́нял → сдал",
                    "Chunki bular takroriy ishlar",
                    "Chunki ular kelasi zamonda",
                    "Chunki ular uzoq davom etdi"
                ],
                "answer": 0,
                "explanation": "Birin-ketin tugagan ishlar har doim СВ talab qiladi. "
                               "Matnning boshi (НСВ — takror va davomiylik) va oxiri "
                               "(СВ — ketma-ketlik) bir-biriga qarama-qarshi "
                               "qoʻyilgan.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-55 — идти / ходить                      KUNDALIK YOʻL
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Доро́га в шко́лу",
        "summary": (
            "PR-55 matni. Har kungi yigirma daqiqalik yoʻl — va buvining "
            "oʻn kilometri. Matn oxirida oʻquvchi yomgʻirdan shikoyat qilishni "
            "bas qiladi."
        ),
        "order":   55,
        "grammar": [
            {
                "pattern":  "хожу́ — muntazam",
                "meaning":  "Takror yoki odat: «Я хожу́ в шко́лу пешко́м» — har kuni "
                            "shunday qilaman. Oʻzbekcha «borib turaman».",
                "examples": ["Я хожу́ в шко́лу пешко́м.", "Он уже́ хо́дит."],
            },
            {
                "pattern":  "иду́ / шёл — hozir, bir tomonga",
                "meaning":  "Aynan hozir yoʻldaman: «Сего́дня я иду́ ме́дленно». "
                            "Oʻtgan zamonda «шёл» — yoʻlda edim, yetib bordimmi "
                            "nomaʼlum.",
                "examples": ["Сего́дня я иду́ ме́дленно.", "У́тром я шёл и ду́мал."],
            },
            {
                "pattern":  "ходи́л — borib kelish",
                "meaning":  "Bordim VA qaytdim — tugagan safar. «Вчера́ я ходи́л в "
                            "магази́н» = doʻkonga borib keldim. Oʻzbekcha «borib "
                            "keldim».",
                "examples": ["Вчера́ я ходи́л в магази́н."],
            },
        ],
        "body": '''<p>Я <strong>хожу́</strong> в шко́лу <span class="cn-word" data-tr="piyoda">пешко́м</span>. Ка́ждый день, пять лет.</p>

<p>Сего́дня я <strong>иду́</strong> <span class="cn-word" data-tr="sekin">ме́дленно</span>. <strong>Идёт</strong> <span class="cn-word" data-tr="yomgʻir">дождь</span>.</p>

<p>Вчера́ я <strong>ходи́л</strong> в магази́н по́сле шко́лы. <span class="cn-word" data-pos="verb" data-tr="sotib oldim">Купи́л</span> хлеб и <span class="cn-word" data-pos="verb" data-tr="qaytdim">верну́лся</span> домо́й.</p>

<p>Мой брат Бекзод ещё ма́ленький. Но он уже́ <strong>хо́дит</strong>. Ме́дленно, но <span class="cn-word" data-tr="oʻzi">сам</span>.</p>

<p>Ба́бушка говори́т:</p>

<p>— Ра́ньше я <strong>ходи́ла</strong> в шко́лу де́сять <span class="cn-word" data-tr="kilometr">киломе́тров</span>. Ка́ждый день. И зимо́й тоже.</p>

<p>Я не зна́ю, пра́вда э́то и́ли нет. Ба́бушка <span class="cn-word" data-pos="verb" data-tr="yaxshi koʻradi">лю́бит</span> таки́е <span class="cn-word" data-tr="hikoyalar">исто́рии</span>.</p>

<p>Но сего́дня у́тром я <strong>шёл</strong> и ду́мал о ба́бушке.</p>

<p>Де́сять киломе́тров. Ка́ждый день. Зимо́й.</p>

<p>Моя́ <span class="cn-word" data-tr="yoʻl">доро́га</span> — два́дцать мину́т.</p>

<p>Тепе́рь я не <span class="cn-word" data-pos="verb" data-tr="shikoyat qilaman">жа́луюсь</span> на дождь.</p>''',
        "questions": [
            {
                "text": "Matn nima bilan tugaydi va nega?",
                "choices": [
                    "Muallif endi yomgʻirdan shikoyat qilmaydi — buvining yoʻli ancha ogʻir edi",
                    "Muallif maktabga bormaslikka qaror qildi",
                    "Buvi yolgʻon aytgani maʼlum boʻldi",
                    "Bekzod maktabga bora boshladi"
                ],
                "answer": 0,
                "explanation": "«Де́сять киломе́тров… Моя́ доро́га — два́дцать "
                               "мину́т». Taqqoslash oʻz-oʻzidan xulosa chiqaradi. "
                               "Buvining hikoyasi rostmi yoki yoʻqmi — matn buni ham "
                               "aytmaydi, va bu muhim emas.",
            },
            {
                "text": "«Я хожу́ в шко́лу» va «Сего́дня я иду́» — nega ikki xil "
                        "feʼl?",
                "choices": [
                    "Хожу́ — muntazam odat, иду́ — aynan hozir yoʻldaman",
                    "Bittasi oʻtgan zamon",
                    "Bittasi СВ, boshqasi НСВ",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Ikkalasi ham НСВ — farq vid emas, yoʻnalish. "
                               "Oʻzbekcha tekshiruv: «borib turaman» (хожу́) va "
                               "«boryapman» (иду́).",
            },
            {
                "text": "«Вчера́ я ходи́л в магази́н» nimani anglatadi?",
                "choices": [
                    "Doʻkonga bordim va qaytdim — safar tugagan",
                    "Doʻkonga ketayotgan edim",
                    "Doʻkonga har kuni boraman",
                    "Doʻkonga bormoqchi edim"
                ],
                "answer": 0,
                "explanation": "Ходи́л — borib-kelish. Keyingi jumla buni tasdiqlaydi: "
                               "«Купи́л хлеб и верну́лся домо́й». Agar «шёл» boʻlsa, "
                               "gap faqat yoʻl haqida boʻlardi.",
            },
        ],
    },
]
