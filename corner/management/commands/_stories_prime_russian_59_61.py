# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-59 … PR-61.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 59 — qoʻllanma (buyruq shakllari bilan), 60 — maslahat
xati, 61 — tarixiy matn. (56 sayohat qaydlari, 57 ilmiy-ommabop, 58 hikoya
edi.) 59 PR-27 dagi «Пра́вила библиоте́ки» ga oʻxshaydi, lekin shakli
boshqa: u qoidalar roʻyxati edi, bu esa odamga qaratilgan yoʻriqnoma.

⚠️ FAKTLAR (61-matn). Peterburg haqidagi daʼvolar tekshirilgan va ehtiyot
bilan tanlangan: shahar 1703-yilda Pyotr I tomonidan asos solingan;
Neva deltasidagi botqoq yerda qurilgan; birinchi qurilgan narsa qalʼa
boʻlgan; 1712-yilda poytaxtga aylangan; qurilish ogʻir sharoitda kechgan
va koʻp odam halok boʻlgan. ANIQ qurbonlar soni ATAY aytilmagan —
manbalarda u juda har xil va bahsli.

Grammatika chegarasi (kumulyativ qoida):
  59-matn: buyruq mayli. НСВ (умумий taklif) va СВ (aniq vazifa) yonma-yon,
           va inkor buyruqda НСВ.
  60-matn: бы. Xat janri ideal — maslahat, afsus va muloyim taklif
           hammasi shartli maylda beriladi.
  61-matn: majhul nisbat. Tarixiy matnda bajaruvchi koʻpincha muhim emas,
           shuning uchun «был постро́ен» tabiiy chiqadi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_59_61.py --author=prime
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
    # PR-59 — buyruq mayli                       QOʻLLANMA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Инстру́кция для но́вого сотру́дника",
        "summary": (
            "PR-59 matni. Yangi xodim uchun eslatma varaqasi: qachon kelish, "
            "kalitni kimdan olish, kofe qoidasi. Oxirgi band eslatmaning oʻzi "
            "haqida."
        ),
        "order":   59,
        "grammar": [
            {
                "pattern":  "Buyruq: -Й / -И / -Ь",
                "meaning":  "«Они́» shaklidan yasaladi: чита́ют → чита́й, говоря́т → "
                            "говори́, гото́вят → готовь. ВЫ shakli -ТЕ qoʻshadi. "
                            "Oʻzbekcha oʻqi! / oʻqing! bilan bir xil tizim.",
                "examples": ["Приходи́те в де́вять.", "Возьми́те ключ."],
            },
            {
                "pattern":  "Inkor buyruqda НСВ",
                "meaning":  "Не опа́здывайте, не теря́йте, не бо́йтесь — inkor "
                            "buyruqda deyarli har doim tugallanmagan feʼl. Bu "
                            "taqiq maʼnosini beradi.",
                "examples": ["Не опа́здывайте.", "Не бо́йтесь ошиба́ться."],
            },
            {
                "pattern":  "НСВ ↔ СВ buyruqda",
                "meaning":  "Спра́шивайте (umumiy taklif — har doim shunday qiling) "
                            "va прочита́йте (aniq vazifa — bir marta, oxirigacha). "
                            "Oxirgi band ikkalasini yonma-yon qoʻyadi.",
                "examples": ["Спра́шивайте. Э́то норма́льно.", "Прочита́йте оди́н раз."],
            },
        ],
        "body": '''<p>Здра́вствуйте! Вы — но́вый <span class="cn-word" data-tr="xodim">сотру́дник</span>. Вот <span class="cn-word" data-tr="eslatma varaqasi">па́мятка</span>.</p>

<p><strong>Приходи́те</strong> в де́вять. <strong>Не опа́здывайте</strong> — э́то ва́жно то́лько в пе́рвую неде́лю. Пото́м уже́ не о́чень.</p>

<p><strong>Возьми́те</strong> <span class="cn-word" data-tr="kalit">ключ</span> у Ни́ны Петро́вны. <strong>Не теря́йте</strong> его́.</p>

<p>Ко́фе — на ку́хне. <strong>Пе́йте</strong> ско́лько хоти́те. Но <strong>помо́йте</strong> <span class="cn-word" data-tr="chashka">ча́шку</span>.</p>

<p><strong>Пиши́те</strong> пи́сьма <span class="cn-word" data-tr="qisqa">ко́ротко</span>. <span class="cn-word" data-tr="Uzun">Дли́нные</span> пи́сьма никто́ не чита́ет.</p>

<p>Что́-то <span class="cn-word" data-tr="tushunarsiz">непоня́тно</span>? <strong>Спра́шивайте</strong>. Э́то норма́льно.</p>

<p><strong>Не бо́йтесь</strong> <span class="cn-word" data-pos="verb" data-tr="xato qilmoq">ошиба́ться</span>. В пе́рвый ме́сяц оши́бка — э́то не оши́бка, а <span class="cn-word" data-tr="oʻqish">учёба</span>.</p>

<p>В <span class="cn-word" data-tr="juma">пя́тницу</span> мы пьём чай вме́сте в четы́ре. <strong>Приходи́те</strong>.</p>

<p>И <span class="cn-word" data-tr="oxirgisi">после́днее</span>.</p>

<p><strong>Не чита́йте</strong> э́ту па́мятку ка́ждый день.</p>

<p><strong>Прочита́йте</strong> оди́н раз — и <strong>рабо́тайте</strong>.</p>''',
        "questions": [
            {
                "text": "Eslatmaning oxirgi bandi nima deydi?",
                "choices": [
                    "Eslatmani bir marta oʻqib, ishga kirishing kerak",
                    "Eslatmani har kuni oʻqish kerak",
                    "Eslatmani saqlab qoʻyish kerak",
                    "Eslatma keraksiz"
                ],
                "answer": 0,
                "explanation": "«Не чита́йте э́ту па́мятку ка́ждый день. Прочита́йте "
                               "оди́н раз — и рабо́тайте». Ikki buyruq, ikki vid: "
                               "takrorni taqiqlaydi (НСВ) va bitta aniq vazifa "
                               "beradi (СВ).",
            },
            {
                "text": "Nega matnda «не чита́йте», lekin «прочита́йте»?",
                "choices": [
                    "Inkor buyruqda НСВ, aniq vazifada esa СВ ishlatiladi",
                    "Ikkalasi bir xil",
                    "Birinchisi hurmat shakli",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Inkor buyruq deyarli har doim НСВ oladi — bu taqiq. "
                               "«Прочита́йте оди́н раз» esa bir martalik aniq vazifa, "
                               "demak СВ.",
            },
            {
                "text": "Eslatma xatolar haqida nima deydi?",
                "choices": [
                    "Birinchi oyda xato — bu xato emas, oʻqish",
                    "Xato qilish taqiqlanadi",
                    "Xatolar uchun jarima bor",
                    "Xatolar haqida hech narsa aytilmagan"
                ],
                "answer": 0,
                "explanation": "«Не бо́йтесь ошиба́ться. В пе́рвый ме́сяц оши́бка — "
                               "э́то не оши́бка, а учёба». Eslatmaning ohangi qatʼiy "
                               "emas — u yangi odamni tinchlantirmoqchi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-60 — бы                                 MASLAHAT XATI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Е́сли бы я знал ра́ньше",
        "summary": (
            "PR-60 matni. Oleg amaki jiyaniga maslahat soʻragan xatiga javob "
            "yozadi. Uchta maslahat beradi — va oxirida ularning barchasini "
            "bekor qiladi."
        ),
        "order":   60,
        "grammar": [
            {
                "pattern":  "е́сли бы …, … бы",
                "meaning":  "Noreal shart: ikkala qismda ham БЫ va oʻtgan zamon. "
                            "«Е́сли бы я мог верну́ться, я бы сде́лал» — qaytib "
                            "bora olmayman, shuning uchun qilmadim ham.",
                "examples": ["Е́сли бы я мог верну́ться, я бы сде́лал три ве́щи."],
            },
            {
                "pattern":  "я бы + oʻtgan zamon",
                "meaning":  "Shartli mayl faqat oʻtgan zamon bilan yasaladi va "
                            "tuslanmaydi. Jinsga qaraydi: я бы сде́лал (erkak), "
                            "я бы сде́лала (ayol).",
                "examples": ["Я бы бо́льше слу́шал.", "Я бы звони́л ча́ще."],
            },
            {
                "pattern":  "на твоём ме́сте",
                "meaning":  "Maslahat berishning eng muloyim yoʻli — chunki bu buyruq "
                            "emas. Rasmiy shakli: на ва́шем ме́сте.",
                "examples": ["На твоём ме́сте я бы не спра́шивал сове́та."],
            },
        ],
        "body": '''<p>До́рогой Жасу́р!</p>

<p>Ты <span class="cn-word" data-pos="verb" data-tr="soʻrayapsan">про́сишь</span> <span class="cn-word" data-tr="maslahat">сове́та</span>. Я не зна́ю, что сказа́ть. Но я скажу́ так.</p>

<p><strong>Е́сли бы</strong> я мог <span class="cn-word" data-pos="verb" data-tr="qaytmoq">верну́ться</span> в два́дцать лет, я <strong>бы</strong> сде́лал три ве́щи.</p>

<p><span class="cn-word" data-tr="Birinchidan">Пе́рвое</span>. Я <strong>бы</strong> <span class="cn-word" data-tr="koʻproq">бо́льше</span> слу́шал и <span class="cn-word" data-tr="kamroq">ме́ньше</span> говори́л.</p>

<p>Второ́е. Я <strong>бы</strong> не боя́лся ошиба́ться. <span class="cn-word" data-tr="Xato">Оши́бка</span> — э́то не <span class="cn-word" data-tr="oxir">коне́ц</span>. Э́то <span class="cn-word" data-tr="shunchaki">про́сто</span> день.</p>

<p>Тре́тье. Я <strong>бы</strong> звони́л ба́бушке <span class="cn-word" data-tr="tez-tezroq">ча́ще</span>.</p>

<p>Но я не могу́ верну́ться. И ты не мо́жешь взять мой <span class="cn-word" data-tr="tajriba">о́пыт</span> — он не рабо́тает в чужи́х рука́х.</p>

<p><strong>На твоём ме́сте</strong> я <strong>бы</strong> не спра́шивал сове́та. Я <strong>бы</strong> про́сто на́чал.</p>

<p>И вот ещё что.</p>

<p><strong>Е́сли бы</strong> мне сказа́ли всё э́то в два́дцать лет, я <strong>бы</strong> не по́нял.</p>

<p>Поэ́тому не слу́шай меня́. Иди́ и де́лай.</p>

<p>Твой дя́дя Оле́г</p>''',
        "questions": [
            {
                "text": "Xat oxirida Oleg amaki nima deydi?",
                "choices": [
                    "Meni tinglama — borib qil",
                    "Har kuni menga yoz",
                    "Buvingga qoʻngʻiroq qil",
                    "Universitetga kir"
                ],
                "answer": 0,
                "explanation": "«Не слу́шай меня́. Иди́ и де́лай». U uchta maslahat "
                               "beradi, keyin oʻzi ularni bekor qiladi — chunki yigirma "
                               "yoshda oʻzi ham bunday gaplarni tushunmagan boʻlardi.",
            },
            {
                "text": "«Е́сли бы мне сказа́ли всё э́то в два́дцать лет, я бы не "
                        "по́нял» — bu jumla nimani anglatadi?",
                "choices": [
                    "Maslahat faqat tajriba orttirgandan keyin tushuniladi",
                    "Hech kim unga hech narsa aytmagan",
                    "U yigirma yoshda emas edi",
                    "U maslahatni yomon koʻradi"
                ],
                "answer": 0,
                "explanation": "Bu xatning butun mantigʻi: maslahat berish oson, lekin "
                               "u qabul qilinishi uchun odam tayyor boʻlishi kerak. "
                               "Shuning uchun oxirgi maslahat — maslahat "
                               "soʻramaslik.",
            },
            {
                "text": "Nega matnda «я бы сде́лал», «я бы сде́лаю» emas?",
                "choices": [
                    "БЫ faqat oʻtgan zamon bilan ishlatiladi",
                    "Chunki bu koʻplik",
                    "Chunki gapirayotgan odam erkak",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Shartli mayl — oʻtgan zamon + БЫ. Boshqa zamon bilan "
                               "ishlatilmaydi. Shakl faqat jinsga qaraydi: erkak "
                               "«сде́лал бы», ayol «сде́лала бы».",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-61 — majhul nisbat                      TARIXIY MATN
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Как был постро́ен Петербу́рг",
        "summary": (
            "PR-61 matni. 1703-yil, Neva deltasidagi botqoq — va uning ustida "
            "qurilgan shahar. Matn oxirida botqoq hali ham oʻsha yerda ekani "
            "eslatiladi."
        ),
        "order":   61,
        "grammar": [
            {
                "pattern":  "был постро́ен — natija",
                "meaning":  "Qisqa sifatdosh + БЫТЬ. Egaga moslashadi: был "
                            "постро́ен (erkak), была́ постро́ена (ayol), бы́ли "
                            "постро́ены (koʻplik).",
                "examples": ["Петербу́рг был постро́ен на боло́те.", "Была́ постро́ена кре́пость."],
            },
            {
                "pattern":  "стро́ился — jarayon",
                "meaning":  "НСВ + -СЯ majhul nisbatning jarayon shakli: «го́род "
                            "стро́ился мно́го лет» — qurilish davom etgan, natija "
                            "hali yoʻq.",
                "examples": ["Го́род стро́ился мно́го лет."],
            },
            {
                "pattern":  "Bajaruvchi — Твори́тельный",
                "meaning":  "Kim qilgani aytilsa, u Твори́тельный'ga kiradi: "
                            "«постро́ен людьми́». Oʻzbekchada bu «odamlar TOMONIDAN» "
                            "boʻlardi.",
                "examples": ["Го́род был постро́ен людьми́."],
            },
        ],
        "body": '''<p>Петербу́рг <strong>был постро́ен</strong> на <span class="cn-word" data-tr="botqoq">боло́те</span>.</p>

<p>В 1703 году́ Пётр Пе́рвый <span class="cn-word" data-pos="verb" data-tr="asos soldi">основа́л</span> здесь го́род.</p>

<p><span class="cn-word" data-tr="Joy">Ме́сто</span> бы́ло <span class="cn-word" data-tr="yomon">плохо́е</span>: вода́, боло́то, хо́лод, <span class="cn-word" data-tr="shamol">ве́тер</span>.</p>

<p>Но ме́сто бы́ло ва́жное: здесь река́ Нева́ идёт в мо́ре.</p>

<p>Снача́ла <strong>была́ постро́ена</strong> <span class="cn-word" data-tr="qalʼa">кре́пость</span>. Пото́м <strong>бы́ли постро́ены</strong> дома́, у́лицы, <span class="cn-word" data-tr="kanallar">кана́лы</span>.</p>

<p>Го́род <strong>стро́ился</strong> мно́го лет. Рабо́та была́ тяжёлая: лю́ди рабо́тали в воде́ и в хо́лоде. Мно́го люде́й <span class="cn-word" data-pos="verb" data-tr="halok boʻldi">поги́бло</span>.</p>

<p>В 1712 году́ Петербу́рг стал <span class="cn-word" data-tr="poytaxt">столи́цей</span>.</p>

<p>Сего́дня э́то большо́й го́род: кана́лы, мосты́, <span class="cn-word" data-tr="saroylar">дворцы́</span>.</p>

<p>Но под ка́ждым до́мом — всё то же боло́то.</p>

<p>Го́род <strong>был постро́ен</strong> людьми́ — не приро́дой. И он стои́т уже́ три <span class="cn-word" data-tr="asr">ве́ка</span>.</p>''',
        "questions": [
            {
                "text": "Nega shunday yomon joyda shahar qurildi?",
                "choices": [
                    "Neva daryosi shu yerda dengizga chiqadi — joy muhim edi",
                    "U yerda koʻp tosh bor edi",
                    "Bu yer arzon edi",
                    "Matnda aytilmagan"
                ],
                "answer": 0,
                "explanation": "«Ме́сто бы́ло плохо́е… Но ме́сто бы́ло ва́жное: здесь "
                               "река́ Нева́ идёт в мо́ре». Ikki jumla bir-biriga "
                               "qarama-qarshi qoʻyilgan: yomon, lekin muhim.",
            },
            {
                "text": "«Была́ постро́ена кре́пость» va «бы́ли постро́ены дома́» — "
                        "nega shakl har xil?",
                "choices": [
                    "Qisqa sifatdosh egaga moslashadi: кре́пость ayol, дома́ koʻplik",
                    "Chunki qalʼa avval qurilgan",
                    "Chunki ular har xil zamonda",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Qisqa sifatdosh sifat kabi ishlaydi: jins va son "
                               "boʻyicha moslashadi — постро́ен / постро́ена / "
                               "постро́ено / постро́ены.",
            },
            {
                "text": "Matnning oxirgi jumlasi nimani taʼkidlaydi?",
                "choices": [
                    "Shaharni tabiat emas, odamlar qurgan",
                    "Shahar juda eski",
                    "Botqoq quritilgan",
                    "Shahar hali qurilmoqda"
                ],
                "answer": 0,
                "explanation": "«Го́род был постро́ен людьми́ — не приро́дой». "
                               "Undan oldingi jumla ham shuni tayyorlaydi: «под "
                               "ка́ждым до́мом — всё то же боло́то». Botqoq hali "
                               "ham oʻsha yerda, lekin shahar uch asr turibdi.",
            },
        ],
    },
]
