# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-47 … PR-49.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 47 — oʻyin (dialog), 48 — hikoya, 49 — kalendar
(roʻyxat shaklidagi matn). (44 sayohat qaydlari, 45 tajriba, 46 xat edi.)

Grammatika chegarasi (kumulyativ qoida):
  47-matn: soʻroq soʻzlarining kelishiklari. «Yigirma savol» oʻyini bu
           uchun ideal janr — matn deyarli butunlay savollardan iborat,
           va har bir savol boshqa kelishikda.
  48-matn: predloglar xaritasi. Metroda adashish hikoyasi — har bir
           jumlada boshqa predlog, va oxirida ularning barchasi bitta
           yoʻnalishga olib keladi.
  49-matn: vaqt ifodalari. Kalendar janri toʻrtta kelishikni tabiiy
           ravishda bir sahifaga sigʻdiradi: в январе́ · в суббо́ту ·
           ле́том · пя́того ма́я.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_47_49.py --author=prime
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
    # PR-47 — soʻroq soʻzlari                    OʻYIN
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Игра́ «Два́дцать вопро́сов»",
        "summary": (
            "PR-47 matni. Sinf «Yigirma savol» oʻyinini oʻynaydi: bir kishi "
            "odamni oʻylaydi, qolganlar savol beradi. Butun matn savollardan "
            "iborat — va har biri boshqa kelishikda."
        ),
        "order":   47,
        "grammar": [
            {
                "pattern":  "Savol = javob kutilayotgan kelishik",
                "meaning":  "Кого́ ты ждёшь? — Бра́та. Кому́ ты пи́шешь? — Бра́ту. "
                            "Savol qanday kelishikda boʻlsa, javob ham oʻsha "
                            "kelishikda. Predlog ham savoldan javobga koʻchadi.",
                "examples": ["Кого́ ты ду́маешь?", "С кем он рабо́тает?"],
            },
            {
                "pattern":  "кто → кого́ · что → чего́",
                "meaning":  "КТО jonli otlar kabi turlanadi (Р.п. = В.п. = кого́), "
                            "ЧТО esa jonsizlar kabi (Р.п. чего́, lekin В.п. что). "
                            "PR-32 dagi jonlilik qoidasi bu yerda ham ishlaydi.",
                "examples": ["Кого́ вы зна́ете?", "О чём он пи́шет?"],
            },
            {
                "pattern":  "чей / чья / чьё / чьи",
                "meaning":  "«Kimniki?» — otga jins va son boʻyicha moslashadi, "
                            "xuddi мой kabi: чей дом, чья кни́га, чьё окно́, чьи "
                            "ключи́.",
                "examples": ["Чья э́то фотогра́фия?"],
            },
        ],
        "body": '''<p>В пя́тницу Марина Олеговна <span class="cn-word" data-pos="verb" data-tr="taklif qildi">предложи́ла</span> <span class="cn-word" data-tr="oʻyin">игру́</span>.</p>

<p>— Оди́н челове́к ду́мает о челове́ке. Други́е <span class="cn-word" data-pos="verb" data-tr="topishadi">уга́дывают</span>. Два́дцать вопро́сов. Отве́ты то́лько «да» и́ли «нет».</p>

<p><span class="cn-word" data-pos="verb" data-tr="oʻylaydi">Ду́мает</span> Жасур. Класс спра́шивает <span class="cn-word" data-tr="navbat bilan">по о́череди</span>.</p>

<p>Афсона: — Э́то <span class="cn-word" data-tr="erkak">мужчи́на</span>?</p>

<p>Жасур: — Да.</p>

<p>Бекзод: — <strong>Кого́</strong> он у́чит? Дете́й?</p>

<p>Марина Олеговна: — Бекзод, э́то не вопро́с «да и́ли нет».</p>

<p>Бекзод: — Извини́те. Он у́чит дете́й?</p>

<p>— Да.</p>

<p>Катя: — Он рабо́тает <strong>с ни́ми</strong> ка́ждый день?</p>

<p>— Да.</p>

<p>Дилноза: — <strong>О ком</strong> все говоря́т в на́шем кла́ссе?</p>

<p>Класс <span class="cn-word" data-pos="verb" data-tr="kulishdi">засмея́лся</span>.</p>

<p>— Э́то тоже не вопро́с, — сказа́ла Марина Олеговна. Но она́ <span class="cn-word" data-pos="verb" data-tr="jilmaydi">улыбну́лась</span>.</p>

<p>Бекзод: — Он в э́той <span class="cn-word" data-tr="xona">ко́мнате</span>?</p>

<p>Жасур: — Да.</p>

<p>Тишина́. Пото́м все посмотре́ли в одну́ <span class="cn-word" data-tr="tomon">сто́рону</span>.</p>

<p>— <strong>Чей</strong> э́то был <span class="cn-word" data-tr="fikr, gʻoya">вопро́с</span>? — спроси́ла Марина Олеговна.</p>

<p>— Бекзо́да, — сказа́л класс.</p>

<p>Шесть вопро́сов. Не два́дцать.</p>''',
        "questions": [
            {
                "text": "Jasur kim haqida oʻylagan edi?",
                "choices": [
                    "Marina Olegovna — oʻqituvchining oʻzi haqida",
                    "Bekzod haqida",
                    "Oʻz akasi haqida",
                    "Maktab direktori haqida"
                ],
                "answer": 0,
                "explanation": "Savollar ketma-ket koʻrsatadi: erkak — bolalarni "
                               "oʻqitadi — har kuni ular bilan ishlaydi — shu xonada. "
                               "Shundan keyin «все посмотре́ли в одну́ сто́рону». "
                               "Oʻqituvchining oʻzi javob ekan.",
            },
            {
                "text": "Nega Bekzodning birinchi savoli qabul qilinmadi?",
                "choices": [
                    "«Кого́ он у́чит?» — bu «ha yoki yoʻq» savoli emas",
                    "Savol juda qiyin edi",
                    "Bekzod navbatini kutmadi",
                    "Savol notoʻgʻri tuzilgan edi"
                ],
                "answer": 0,
                "explanation": "Oʻyin qoidasi: «Отве́ты то́лько „да“ и́ли „нет“». "
                               "«Кого́?» ochiq savol — unga «ha» deb javob berib "
                               "boʻlmaydi. Bekzod darrov tuzatdi: «Он у́чит дете́й?»",
            },
            {
                "text": "«Кого́ он у́чит?» va «О ком все говоря́т?» — nega bir xil "
                        "soʻz ikki xil koʻrinadi?",
                "choices": [
                    "Кого́ — Вини́тельный, о ком — Предло́жный",
                    "Bittasi koʻplik",
                    "Bittasi oʻtgan zamon",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Soʻroq soʻzi javob kutilayotgan kelishikda beriladi. "
                               "«Учи́ть кого́?» — Вини́тельный. «Говори́ть о ком?» — "
                               "Предло́жный, va predlog ham savolga koʻchadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-48 — predloglar xaritasi                HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Как я потеря́лся в метро́",
        "summary": (
            "PR-48 matni. Metroda birinchi marta: chiqish, oʻtish, yana chiqish "
            "— va har bir qadam boshqa predlog. Yordam kutilmagan tomondan "
            "keladi."
        ),
        "order":   48,
        "grammar": [
            {
                "pattern":  "Predlog kelishikni tanlaydi",
                "meaning":  "в метро́ (П.п.), из метро́ (Р.п.), к вы́ходу (Д.п.), "
                            "под землёй (Т.п.). Har bir predlog oʻz kelishigini "
                            "talab qiladi — bu butun tizimning kaliti.",
                "examples": ["Я стою́ в метро́.", "Я иду́ к вы́ходу."],
            },
            {
                "pattern":  "в ↔ из · на ↔ с · к ↔ от",
                "meaning":  "Antonim juftliklar. Soʻz В olsa, «dan» uchun ИЗ; НА "
                            "olsa — С; odam tomon К boʻlsa, odamdan ОТ.",
                "examples": ["Из метро́ на у́лицу.", "От ста́нции к ста́нции."],
            },
            {
                "pattern":  "Harakat bor / harakat yoʻq",
                "meaning":  "Bir xil predlog ikki kelishik olishi mumkin. Harakat "
                            "yoʻq — joy kelishigi (в метро́), harakat bor — "
                            "Вини́тельный (в метро́ — kirish).",
                "examples": ["Я иду́ че́рез пере́ход."],
            },
        ],
        "body": '''<p>Пе́рвый день <strong>в</strong> большо́м го́роде. Я <strong>в</strong> метро́.</p>

<p>Здесь <strong>под</strong> <span class="cn-word" data-tr="yer">землёй</span> есть <span class="cn-word" data-tr="butun">це́лый</span> го́род. Лю́ди иду́т <strong>по</strong> <span class="cn-word" data-tr="oʻtish yoʻli">перехо́ду</span> бы́стро. Никто́ не стои́т.</p>

<p>Я иду́ <strong>к</strong> <span class="cn-word" data-tr="chiqish">вы́ходу</span>. Но вы́ходов здесь <span class="cn-word" data-tr="sakkiz">во́семь</span>.</p>

<p>Я иду́ <strong>из</strong> перехо́да <strong>на</strong> у́лицу. Э́то не моя́ у́лица.</p>

<p>Я иду́ <strong>с</strong> у́лицы обра́тно <strong>в</strong> метро́.</p>

<p>Тепе́рь я иду́ <strong>че́рез</strong> друго́й перехо́д. <strong>Ря́дом с</strong> ним <span class="cn-word" data-tr="xarita">ка́рта</span>. Но <strong>на</strong> ка́рте <span class="cn-word" data-tr="oʻttiz">три́дцать</span> ста́нций.</p>

<p>Я стою́ <strong>пе́ред</strong> ка́ртой де́сять мину́т.</p>

<p><strong>Ко</strong> мне подхо́дит <span class="cn-word" data-tr="keksa ayol">ста́рая же́нщина</span> <strong>с</strong> <span class="cn-word" data-tr="paketlar">паке́тами</span>.</p>

<p>— Вам куда́? — спра́шивает она́.</p>

<p>Я говорю́ <span class="cn-word" data-tr="manzil">а́дрес</span>.</p>

<p>— А, э́то <strong>за</strong> ры́нком, — говори́т она́. — Иди́те <strong>до</strong> ста́нции «Парк», пото́м <strong>от</strong> <span class="cn-word" data-tr="bekat">ста́нции</span> <span class="cn-word" data-tr="chapga">нале́во</span>. Вы́ход но́мер три.</p>

<p>Я иду́. Ста́нция «Парк». Вы́ход но́мер три. Ры́нок.</p>

<p>И <strong>за</strong> ры́нком — мой дом.</p>

<p>Тепе́рь я зна́ю: <strong>в</strong> большо́м го́роде ка́рта помога́ет. Но челове́к помога́ет лу́чше.</p>''',
        "questions": [
            {
                "text": "Kim adashgan odamga yordam berdi?",
                "choices": [
                    "Paketlar koʻtargan keksa ayol",
                    "Metro xodimi",
                    "Devordagi xarita",
                    "Politsiyachi"
                ],
                "answer": 0,
                "explanation": "«Ко мне подхо́дит ста́рая же́нщина с паке́тами». U "
                               "aniq yoʻriqnoma berdi: bekatgacha, keyin chapga, "
                               "uchinchi chiqish. Matn shu bilan tugaydi: «Челове́к "
                               "помога́ет лу́чше».",
            },
            {
                "text": "«Из перехо́да» va «с у́лицы» — nega ikki xil predlog?",
                "choices": [
                    "Перехо́д В oladi (→ ИЗ), у́лица esa НА oladi (→ С)",
                    "Chunki bittasi ayol jinsida",
                    "Chunki bittasi koʻplik",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "PR-30 dagi В/НА roʻyxati bu yerda ham ishlaydi: «в "
                               "перехо́де» → «из перехо́да»; «на у́лице» → «с "
                               "у́лицы». Antonim juftliklar shu qoidaga tayanadi.",
            },
            {
                "text": "Matnda «за ры́нком» ikki marta uchraydi. Nega bu shakl "
                        "oʻzgarmadi?",
                "choices": [
                    "Ikkalasida ham harakat yoʻq — joy koʻrsatilyapti (Т.п.)",
                    "Chunki «ры́нок» erkak jinsida",
                    "Chunki bu ism",
                    "Ikkinchisi xato boʻlishi kerak"
                ],
                "answer": 0,
                "explanation": "ЗА ikki kelishik oladi. Harakat boʻlsa Вини́тельный "
                               "(«идти́ за дом»), harakat boʻlmasa Твори́тельный "
                               "(«за ры́нком» — bozor orqasida joylashgan). Matnda "
                               "ikkalasi ham joy maʼnosida.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-49 — vaqt ifodalari                     KALENDAR
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Календа́рь Ни́ны",
        "summary": (
            "PR-49 matni. Ninaning bir yili — bitta sahifada. Har bir oyda bir "
            "voqea, va oxirida maʼlum boʻladiki, kalendarda bitta kun boʻsh "
            "qolgan."
        ),
        "order":   49,
        "grammar": [
            {
                "pattern":  "в + Предло́жный — oy va yil",
                "meaning":  "в январе́, в ма́е, в 2026 году́. Uzun vaqt joy kabi "
                            "koʻriladi: «uning ichida». ГОД -У́ oladi: в году́.",
                "examples": ["В январе́ Ни́на начала́ рабо́ту.", "В 2026 году́."],
            },
            {
                "pattern":  "в + Вини́тельный — hafta kuni va soat",
                "meaning":  "в суббо́ту, во вто́рник, в два часа́. Qisqa vaqt nuqta "
                            "kabi koʻriladi. ВО — ikki undoshdan oldin.",
                "examples": ["В суббо́ту — теа́тр.", "Во вто́рник экза́мен."],
            },
            {
                "pattern":  "Твори́тельный — fasl va kun qismi",
                "meaning":  "ле́том, зимо́й, у́тром, ве́чером — predlogsiz. Bular "
                            "Твори́тельный padejida qotib qolgan ravishlar.",
                "examples": ["Ле́том она́ была́ в дере́вне.", "У́тром — рабо́та."],
            },
        ],
        "body": '''<p>У Ни́ны есть <span class="cn-word" data-tr="kalendar">календа́рь</span>. Оди́н год — одна́ <span class="cn-word" data-tr="sahifa">страни́ца</span>.</p>

<p><strong>В январе́</strong> она́ начала́ но́вую рабо́ту. Бы́ло хо́лодно и <span class="cn-word" data-tr="qiyin">тру́дно</span>.</p>

<p><strong>В феврале́</strong> — <span class="cn-word" data-tr="hech narsa">ничего́</span>. Про́сто рабо́та.</p>

<p><strong>В ма́рте</strong> она́ <span class="cn-word" data-pos="verb" data-tr="sotib oldi">купи́ла</span> велосипе́д. <strong>У́тром</strong> — рабо́та, <strong>ве́чером</strong> — <span class="cn-word" data-tr="park">парк</span>.</p>

<p><strong>В апре́ле</strong> <strong>во вто́рник</strong> у неё был экза́мен. Она́ <span class="cn-word" data-pos="verb" data-tr="topshirdi">сдала́</span>.</p>

<p><strong>Ле́том</strong> Ни́на была́ в дере́вне. <strong>В ию́не</strong>, <strong>в ию́ле</strong> и <strong>в а́вгусте</strong>. Три ме́сяца без го́рода.</p>

<p><strong>В сентябре́</strong> — сно́ва рабо́та. <strong>В октябре́</strong> она́ <span class="cn-word" data-pos="verb" data-tr="uchrashdi">познако́милась</span> с Олегом.</p>

<p><strong>В ноябре́</strong> они́ ходи́ли в <span class="cn-word" data-tr="teatr">теа́тр</span> <strong>в суббо́ту</strong>. Ка́ждую суббо́ту.</p>

<p><strong>В декабре́</strong> <strong>но́чью</strong> шёл снег. Ни́на смотре́ла в окно́ и ду́мала о го́де.</p>

<p>Оди́н год. Оди́н велосипе́д. Оди́н экза́мен. Оди́н Олег.</p>

<p>Но в календаре́ есть оди́н <span class="cn-word" data-tr="boʻsh">пусто́й</span> день. <strong>Пя́тое ма́я</strong>.</p>

<p><strong>Пя́того ма́я</strong> Ни́на ничего́ не де́лала. Она́ сиде́ла до́ма и чита́ла.</p>

<p>Тепе́рь она́ ду́мает: э́то был <span class="cn-word" data-tr="eng yaxshi">са́мый лу́чший</span> день <strong>в году́</strong>.</p>''',
        "questions": [
            {
                "text": "Nina uchun yilning eng yaxshi kuni qaysi boʻldi?",
                "choices": [
                    "Beshinchi may — hech narsa qilmagan kuni",
                    "Yangi ish boshlagan kuni yanvarda",
                    "Imtihon topshirgan kuni aprelda",
                    "Oleg bilan tanishgan kuni oktyabrda"
                ],
                "answer": 0,
                "explanation": "Kalendarda bitta boʻsh kun qolgan edi — «Пя́того ма́я "
                               "Ни́на ничего́ не де́лала». Va oxirgi jumla: «э́то был "
                               "са́мый лу́чший день в году́». Yilning eng yaxshi kuni "
                               "yozilmagan kun ekan.",
            },
            {
                "text": "Nega «в ма́е», lekin «в суббо́ту»?",
                "choices": [
                    "Oy Предло́жный oladi, hafta kuni esa Вини́тельный",
                    "Ikkalasi bir xil kelishik",
                    "Chunki «суббо́та» ayol jinsida",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Rus tili vaqtni joy kabi koʻradi: uzun vaqt (oy, yil) "
                               "— «ichida», demak Предло́жный. Qisqa vaqt (kun, soat) "
                               "— «nuqtaga», demak Вини́тельный.",
            },
            {
                "text": "«Ле́том», «у́тром», «но́чью» — bu shakllarda nega predlog "
                        "yoʻq?",
                "choices": [
                    "Bular Твори́тельный padejida qotib qolgan ravishlar",
                    "Chunki ular qisqa soʻzlar",
                    "Chunki predlog tushirib qoldirilgan",
                    "Chunki bular sifat"
                ],
                "answer": 0,
                "explanation": "Fasllar va kun qismlari Твори́тельный shaklida "
                               "ishlatiladi va predlog olmaydi: ле́том, зимо́й, "
                               "у́тром, ве́чером, но́чью. Oʻquvchi ularni PR-20 dan "
                               "beri ishlatib kelgan — endi nega bunday ekanini "
                               "biladi.",
            },
        ],
    },
]
