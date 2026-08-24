# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-77 … PR-79.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 77 — kundalik daftar, 78 — sirli hikoya,
79 — maktab hikoyasi. (74 ilmiy-ommabop, 75 biografik hikoya,
76 portret edi — uchta bir xil shakl ketma-ket kelmayapti.)

Grammatika chegarasi (kumulyativ qoida):
  77-matn: ка́ждый / весь / все / всё / любо́й / друго́й / остальны́е.
           Sarlavhaning oʻzi darsning asosiy juftligi, va oxirgi jumla
           ham shu juftlik ustiga qurilgan.
  78-matn: -то / -нибудь / ко́е-. Har uchala zarracha ham matnda oʻz
           oʻrnida: oʻtgan zamon xabari → -то, savol va kelajak →
           -нибудь, «bilaman-u aytmayman» → ко́е-.
  79-matn: ikki inkor. Никто́ / ничего́ / никогда́ / никому́ beshta
           joyda, har birida feʼl oldida «не» turibdi.

⚠️ ATAY QOCHILGAN (keyingi darslar): sana va davomiylik qurilishlari
(PR-80), shaxssiz gaplar (PR-81), жамловчи sonlar — о́ба, тро́е (PR-82),
благодаря́ / несмотря́ на (PR-83), частицы — же, ведь, ли́шь (PR-84).

⚠️ 78-matnda ATAYIN bitta «никто́ … не» bor — u PR-79 da oʻrgatiladi,
lekin bu ibora oldingi matnlarda ham lugʻat sifatida uchragan va
kichik sir janrisiz iloji yoʻq. 79-matn uni toʻliq ochadi.

Uchala matn ham toʻqima voqealar — real daʼvo yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_77_79.py --author=prime
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
    # PR-77 — ка́ждый / весь                          KUNDALIK DAFTAR
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ка́ждое у́тро, весь год",
        "summary": (
            "PR-77 matni. Anna bir yil davomida har kuni ertalab bitta "
            "daraxtni suratga oldi. Yakuniy xulosasi darsning grammatikasi "
            "bilan aytilgan: har kuni bir xil edi, yil boʻyi esa — yoʻq."
        ),
        "order":   77,
        "grammar": [
            {
                "pattern":  "Ка́ждый — takror · весь — davomiylik",
                "meaning":  "«Ка́ждое у́тро» — har ertalab (necha marta?). «Весь "
                            "год» — yil boʻyi (qancha vaqt?). Sarlavha ikkalasini "
                            "yonma-yon qoʻyadi.",
                "examples": ["Ка́ждое у́тро Анна фотографи́ровала де́рево.",
                             "Она́ де́лала э́то весь год."],
            },
            {
                "pattern":  "Все ↔ всё — bir harf",
                "meaning":  "«Все фотогра́фии» — koʻplik (rasmlar). «Всё "
                            "измени́лось» — oʻrta jins, birlik (hamma narsa). "
                            "Feʼlga qarab ajratiladi.",
                "examples": ["Все фотогра́фии бы́ли почти́ одина́ковые.",
                             "И всё-таки всё измени́лось."],
            },
            {
                "pattern":  "Любо́й · друго́й · остальны́е",
                "meaning":  "«Любо́й день» — istalgan kun. «Друго́й» — boshqa. "
                            "«Остальны́е» — qolganlar.",
                "examples": ["Возьми́те любо́й сни́мок из ма́рта.",
                             "Остальны́е лежа́т в па́пке."],
            },
        ],
        "body": '''<p><em>31 декабря́. После́дняя за́пись.</em></p>

<p>Год наза́д я реши́ла де́лать оди́н <span class="cn-word" data-tr="surat, kadr">сни́мок</span> в день. Всегда́ одно́ и то же де́рево во дворе́, всегда́ в во́семь утра́, всегда́ с одно́го ме́ста. Штати́в я поста́вила у <span class="cn-word" data-tr="panjara">пери́л</span> и бо́льше не дви́гала.</p>

<p><strong>Ка́ждое у́тро</strong> я выходи́ла на <span class="cn-word" data-tr="balkon">балко́н</span> и <span class="cn-word" data-pos="verb" data-tr="suratga olardim">фотографи́ровала</span>. Три́ста шестьдеся́т пять раз.</p>

<p>Пе́рвый ме́сяц бы́ло интере́сно. Второ́й — <span class="cn-word" data-tr="zerikarli">ску́чно</span>. В ма́рте я два ра́за <span class="cn-word" data-tr="sal boʻlmasa unutayozdim">чуть не забы́ла</span>, и оди́н раз сде́лала сни́мок в <span class="cn-word" data-tr="xalat">хала́те</span>, пря́мо из-под <span class="cn-word" data-tr="koʻrpa">одея́ла</span>.</p>

<p><strong>Весь</strong> апре́ль шли дожди́, и де́рево стоя́ло <span class="cn-word" data-tr="yalangʻoch, bargsiz">го́лое</span>. <strong>Все</strong> сни́мки того́ ме́сяца се́рые и <span class="cn-word" data-tr="xira, oʻchgan">ту́склые</span>.</p>

<p>Ле́том я уезжа́ла на неде́лю и попроси́ла <span class="cn-word" data-tr="qoʻshni ayolni">сосе́дку</span>. Она́ фотографи́ровала <strong>ка́ждый</strong> день, как я проси́ла. Её сни́мки <span class="cn-word" data-pos="verb" data-tr="ajralib turadi">отлича́ются</span>: она́ стоя́ла на <span class="cn-word" data-tr="yarim qadam chaproqda">полшага́ ле́вее</span>.</p>

<p>Вчера́ я <span class="cn-word" data-pos="verb" data-tr="tera boshladim">собрала́</span> <strong>все</strong> фотогра́фии в оди́н файл и посмотре́ла их <span class="cn-word" data-tr="ketma-ket">подря́д</span>.</p>

<p>Вот что <span class="cn-word" data-tr="gʻalati">стра́нно</span>. Возьми́те <strong>любо́й</strong> сни́мок и сни́мок сле́дующего дня — <span class="cn-word" data-tr="farq">ра́зницы</span> нет. Совсе́м. <strong>Ка́ждый</strong> день похо́ж на <span class="cn-word" data-tr="oldingi">предыду́щий</span>.</p>

<p>А тепе́рь возьми́те <span class="cn-word" data-tr="birinchisini">пе́рвый</span> и после́дний. Э́то <strong>друго́е</strong> де́рево. <strong>Друго́й</strong> двор. <strong>Друга́я</strong> зима́.</p>

<p><strong>Ка́ждый</strong> день был одина́ковым. А <strong>весь</strong> год — нет.</p>

<p>Ду́маю, с людьми́ <span class="cn-word" data-tr="xuddi shunday">так же</span>. <span class="cn-word" data-tr="qolganlarini">Остально́е</span> напишу́ в сле́дующем году́.</p>''',
        "questions": [
            {
                "text": "Anna yil davomida nima qildi?",
                "choices": [
                    "Har kuni yangi daraxt ekdi",
                    "Har ertalab soat sakkizda bir xil daraxtni suratga oldi",
                    "Har oy bitta rasm chizdi",
                    "Qoʻshnisining rasmlarini yigʻdi"
                ],
                "answer": 1,
                "explanation": "«Всегда́ одно́ и то же де́рево во дворе́, "
                               "всегда́ в во́семь утра́, всегда́ с одного́ "
                               "ме́ста» — 365 marta.",
            },
            {
                "text": "Nega matnda «ка́ждое у́тро», lekin «весь апре́ль»?",
                "choices": [
                    "Chunki aprel ayol jinsida",
                    "Chunki bu matndagi xato",
                    "Chunki «весь» faqat oylar bilan ishlatiladi",
                    "Chunki «ка́ждое у́тро» — takror, «весь апре́ль» — bitta uzluksiz davr"
                ],
                "answer": 3,
                "explanation": "Savol ikki xil: «necha marta?» → ка́ждый; "
                               "«qancha vaqt?» → весь. Oʻzbekchada ham «har "
                               "ertalab» va «aprel boʻyi» ikki xil aytiladi.",
            },
            {
                "text": "Kundalikning asosiy xulosasi nima?",
                "choices": [
                    "Har kuni bir xil edi, lekin butun yil — yoʻq",
                    "Suratga olish zerikarli ish",
                    "Qoʻshni notoʻgʻri suratga olgan",
                    "Daraxt oʻzgarmagan"
                ],
                "answer": 0,
                "explanation": "«Ка́ждый день был одина́ковым. А весь год — "
                               "нет». Ikki qoʻshni surat orasida farq yoʻq, "
                               "birinchi va oxirgisi orasida esa boshqa "
                               "daraxt.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-78 — noaniq olmoshlar                          SIRLI HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Кто́-то оста́вил зонт",
        "summary": (
            "PR-78 matni. Kichik kafeda kimdir soyabon qoldirib ketdi. Uni "
            "ikki yil kutishdi. Egasi kelmadi — lekin soyabon kafening eng "
            "kerakli narsasiga aylandi."
        ),
        "order":   78,
        "grammar": [
            {
                "pattern":  "-то — voqea boʻlgan, kimligi nomaʼlum",
                "meaning":  "Oʻtgan zamon xabari. Sarlavhaning oʻzi shunday: "
                            "soyabonni qoldirgan odam bor, faqat kimligi "
                            "nomaʼlum.",
                "examples": ["Кто́-то оста́вил зонт у окна́.",
                             "На ру́чке что́-то напи́сано."],
            },
            {
                "pattern":  "-нибудь — savol, kelasi zamon, shart",
                "meaning":  "Hali boʻlmagan yoki boʻldimi deb soʻralayotgan narsa. "
                            "Matnda savolda ham, kelasi zamonda ham bor.",
                "examples": ["Кто́-нибудь спра́шивал про зонт?",
                             "Е́сли кто́-нибудь придёт, отда́йте ему́."],
            },
            {
                "pattern":  "ко́е- — bilaman, aytmayman",
                "meaning":  "Soʻzlovchi biladi, lekin atayin aytmaydi. Predlog "
                            "bilan kelganda uchta alohida soʻz: ко́е с кем.",
                "examples": ["Ко́е-кто из ста́рых госте́й по́мнит тот ве́чер."],
            },
        ],
        "body": '''<p>В ма́леньком кафе́ на углу́ <strong>кто́-то</strong> оста́вил зонт.</p>

<p>Э́то бы́ло в октябре́ два го́да наза́д. Ве́чером шёл дождь, наро́ду бы́ло мно́го, и <span class="cn-word" data-tr="ofitsiantka">официа́нтка</span> Ле́на нашла́ зонт у окна́, когда́ закрыва́ла зал.</p>

<p>Зонт был ста́рый, но хоро́ший: тёмно-си́ний, с деревя́нной <span class="cn-word" data-tr="dastasi">ру́чкой</span>. На ру́чке <strong>что́-то</strong> бы́ло напи́сано ме́лкими <span class="cn-word" data-tr="harflar">бу́квами</span>, но <span class="cn-word" data-pos="verb" data-tr="oʻchib ketgan">стёрлось</span>.</p>

<p>Ле́на поста́вила зонт в у́гол и жда́ла.</p>

<p>Пе́рвую неде́лю она́ спра́шивала госте́й: «<strong>Кто́-нибудь</strong> забы́л зонт?» <span class="cn-word" data-pos="verb" data-tr="bosh chayqashardi">Кача́ли голово́й</span>.</p>

<p>Пото́м она́ <span class="cn-word" data-pos="verb" data-tr="osib qoʻydi">пове́сила</span> <span class="cn-word" data-tr="eʼlon">объявле́ние</span> на дверь. Прошёл ме́сяц. Никто́ не пришёл.</p>

<p>Зимо́й зонт переста́вили за <span class="cn-word" data-tr="peshtaxta">сто́йку</span>. Ле́том про него́ <span class="cn-word" data-pos="verb" data-tr="unutishdi">забы́ли</span>.</p>

<p>А в сентябре́ случи́лось вот что. На у́лице начался́ <span class="cn-word" data-tr="jala">ли́вень</span>, и одна́ де́вушка <span class="cn-word" data-pos="verb" data-tr="yugurib kirdi">вбежа́ла</span> в кафе́ <span class="cn-word" data-tr="jiqqa hoʻl">совсе́м мо́края</span>. Ле́на <span class="cn-word" data-tr="oʻylamasdan">не разду́мывая</span> доста́ла зонт и дала́ ей.</p>

<p>Де́вушка верну́ла его́ на сле́дующий день.</p>

<p>С тех пор зонт живёт у две́ри. Его́ берёт <strong>кто́-нибудь</strong>, кому́ ну́жно, и прино́сит обра́тно. За два го́да он <span class="cn-word" data-pos="verb" data-tr="sayohat qildi">пропутеше́ствовал</span> по всему́ райо́ну и ни ра́зу не <span class="cn-word" data-pos="verb" data-tr="yoʻqolmadi">потеря́лся</span>.</p>

<p><strong>Ко́е-кто</strong> из ста́рых госте́й говори́т, что зна́ет хозя́ина. Но и́мени не называ́ет.</p>

<p>Ле́на счита́ет, что э́то и не ва́жно. Зонт <span class="cn-word" data-pos="verb" data-tr="topdi">нашёл</span> себе́ рабо́ту получше, чем стоя́ть в <span class="cn-word" data-tr="shkafda">шкафу́</span>.</p>''',
        "questions": [
            {
                "text": "Soyabon bilan oxir-oqibat nima boʻldi?",
                "choices": [
                    "Egasi ikki yildan keyin kelib olib ketdi",
                    "Lena uni uyiga olib ketdi",
                    "U yoʻqolib qoldi",
                    "U eshik yonida turadi va kerak boʻlganlar olib turadi"
                ],
                "answer": 3,
                "explanation": "«Его́ берёт кто́-нибудь, кому́ ну́жно, и "
                               "прино́сит обра́тно». Ikki yilda u butun mahalla "
                               "boʻylab yurdi va bir marta ham yoʻqolmadi.",
            },
            {
                "text": "Nega matnda «Кто́-нибудь забы́л зонт?», lekin «Кто́-то оста́вил зонт»?",
                "choices": [
                    "Chunki birinchisi savol, ikkinchisi esa boʻlib oʻtgan voqea haqidagi xabar",
                    "Chunki birinchisi koʻplik",
                    "Chunki «-нибудь» faqat ayollar haqida ishlatiladi",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Savolda har doim -нибудь: kimdir unutgan-unutmagani "
                               "hali nomaʼlum. Xabarda esa -то: soyabon "
                               "qoldirilgan, demak odam bor.",
            },
            {
                "text": "«Ко́е-кто из ста́рых госте́й» nimani bildiradi?",
                "choices": [
                    "Hech kim bilmaydi",
                    "Bir kishi bor — u biladi, lekin ismini aytmaydi",
                    "Hamma mehmonlar biladi",
                    "Lena buni oʻzi oʻylab topgan"
                ],
                "answer": 1,
                "explanation": "«Но и́мени не называ́ет». Ко́е- ning butun "
                               "maʼnosi shu: soʻzlovchi biladi, lekin atayin "
                               "aytmaydi — «кто́-то» dan farqi ana shunda.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-79 — ikki inkor                             MAKTAB HIKOYASI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Никто́ ничего́ не сказа́л",
        "summary": (
            "PR-79 matni. Sherbek rus maktabiga koʻchib keldi va birinchi "
            "kundan hech narsa tushunmadi. Kimdir uning partasiga har kuni "
            "tarjima qoʻyib keta boshladi — va hech kim hech narsa demadi."
        ),
        "order":   79,
        "grammar": [
            {
                "pattern":  "Ikki inkor: ни- + не",
                "meaning":  "Inkor soʻzi bor joyda feʼl oldida «не» turishi shart "
                            "— xuddi oʻzbekchadagi «hech kim demadi» kabi. "
                            "Matnda beshta joyda.",
                "examples": ["Никто́ ничего́ не сказа́л.",
                             "Шербе́к никогда́ не узна́л, кто э́то был."],
            },
            {
                "pattern":  "Bir gapda bir nechta inkor",
                "meaning":  "«Никто́ никогда́ ничего́ не спроси́л» — uchta inkor "
                            "soʻzi va bitta «не». Bu meʼyor, xato emas.",
                "examples": ["Никто́ никогда́ ничего́ у него́ не спроси́л."],
            },
            {
                "pattern":  "Predlog soʻzni ikkiga boʻladi",
                "meaning":  "«Ни с кем», «ни о чём» — uchta alohida soʻz. "
                            "Predlog «ни» bilan asosiy soʻz orasiga tushadi.",
                "examples": ["Пе́рвый ме́сяц он ни с кем не разгова́ривал."],
            },
        ],
        "body": '''<p>Шербе́к прие́хал в Росси́ю в сентябре́ и пошёл в восьмо́й класс.</p>

<p>По-ру́сски он знал два́дцать слов. На пе́рвом уро́ке учи́тельница что́-то до́лго объясня́ла, весь класс <span class="cn-word" data-pos="verb" data-tr="yozardi">запи́сывал</span>, а Шербе́к смотре́л в <span class="cn-word" data-tr="daftar">тетра́дь</span> и <span class="cn-word" data-pos="verb" data-tr="tushunmasdi">не понима́л</span> <strong>ничего́</strong>.</p>

<p>Пе́рвый ме́сяц он <strong>ни с кем не</strong> разгова́ривал. Не потому́, что не хоте́л. Про́сто слов не́ было.</p>

<p>В октябре́ он нашёл в <span class="cn-word" data-tr="parta">па́рте</span> <span class="cn-word" data-tr="qogʻoz varaqcha">листо́к</span>. На нём бы́ли ру́сские слова́ с уро́ка и рядом — перево́д на узбе́кский. <span class="cn-word" data-tr="qoʻlyozma">По́черк</span> был <span class="cn-word" data-tr="notekis">неро́вный</span>, де́тский.</p>

<p>Шербе́к <span class="cn-word" data-pos="verb" data-tr="atrofga qaradi">огляде́лся</span>. <strong>Никто́</strong> на него́ <strong>не</strong> смотре́л.</p>

<p>На сле́дующий день листо́к был сно́ва. И че́рез день. И <strong>всю</strong> зи́му.</p>

<p>Он <span class="cn-word" data-pos="verb" data-tr="urinib koʻrdi">пыта́лся</span> поня́ть, кто э́то. Но в кла́ссе <strong>никто́ никогда́ ничего́ не</strong> говори́л про листки́. Ребя́та <span class="cn-word" data-pos="verb" data-tr="salomlashardi">здоро́вались</span>, <span class="cn-word" data-pos="verb" data-tr="taklif qilishardi">зва́ли</span> игра́ть в футбо́л — и <strong>ничего́ не</strong> спра́шивали.</p>

<p>К ма́рту Шербе́к на́чал отвеча́ть на уро́ках. К ма́ю — <span class="cn-word" data-pos="verb" data-tr="bahslashardi">спо́рил</span> с учи́телем.</p>

<p>В после́дний день <span class="cn-word" data-tr="oʻquv yili">уче́бного го́да</span> он положи́л в свою́ па́рту листо́к. На нём бы́ло одно́ сло́во: «Спаси́бо».</p>

<p>У́тром листка́ <strong>не</strong> было. Вме́сто него́ лежа́л друго́й, с <span class="cn-word" data-tr="oʻsha xatda">тем же по́черком</span>: «Не за что».</p>

<p>Шербе́к так и <strong>не</strong> узна́л, кто э́то был. <strong>Никто́ ничего́ не</strong> сказа́л — <span class="cn-word" data-tr="ehtimol">возмо́жно</span>, и́менно поэ́тому всё <span class="cn-word" data-pos="verb" data-tr="davom etdi">продолжа́лось</span> <strong>весь</strong> год.</p>''',
        "questions": [
            {
                "text": "Sherbek partasidan nima topdi?",
                "choices": [
                    "Oʻqituvchining eslatmasini",
                    "Dars soʻzlarining oʻzbekchaga tarjimasi yozilgan varaqchani",
                    "Futbol jamoasining roʻyxatini",
                    "Oʻzining eski daftarini"
                ],
                "answer": 1,
                "explanation": "«Ру́сские слова́ с уро́ка и рядом — перево́д на "
                               "узбе́кский». Qoʻlyozma bolalarniki edi, va "
                               "varaqcha butun qish davomida takrorlandi.",
            },
            {
                "text": "Nega matnda «ни с кем не разгова́ривал» — nega uchta alohida soʻz?",
                "choices": [
                    "Chunki bu koʻplik shakli",
                    "Chunki «с» predlogi «ни» va «кем» orasiga tushadi",
                    "Chunki gap oʻtgan zamonda",
                    "Bu matndagi xato"
                ],
                "answer": 1,
                "explanation": "Predlog inkor olmoshini ikkiga boʻladi va "
                               "uchalasi alohida yoziladi: ни с кем, ни о чём, "
                               "ни у кого́. Feʼl oldidagi «не» esa baribir "
                               "saqlanadi.",
            },
            {
                "text": "Hikoyaning oxirgi jumlasi nima demoqchi?",
                "choices": [
                    "Sinfdoshlar Sherbekni yoqtirmasdi",
                    "Varaqchalarni oʻqituvchi qoʻyib ketardi",
                    "Aynan hech kim hech narsa demagani uchun bu bir yil davom etdi",
                    "Sherbek oxiri kim ekanini bilib oldi"
                ],
                "answer": 2,
                "explanation": "«Никто́ ничего́ не сказа́л — возмо́жно, и́менно "
                               "поэ́тому всё продолжа́лось весь год». Aytilsa, "
                               "u minnatdorchilikka aylanardi va toʻxtardi.",
            },
        ],
    },
]
