# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-74 … PR-76.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 74 — ilmiy-ommabop, 75 — biografik hikoya,
76 — portret (usta haqida). (71 biografiya, 72 hikoya, 73 maktub-javob
edi — uchta bir xil shakl ketma-ket kelmayapti.)

Grammatika chegarasi (kumulyativ qoida):
  74-matn: sifat darajalari — са́мая дли́нная, длинне́е, бо́льше, ме́ньше,
           ху́же, гора́здо, всех/всего́ hamda «чем» va Роди́тельный li
           solishtirishning ikkalasi ham.
  75-matn: свой — beshta kelishikda va ikkala maʼnoda («oʻzining» va
           «ijara emas, oʻziniki»). Ataylab bitta «его́» ham qoʻyilgan,
           farq koʻrinib tursin uchun.
  76-matn: себя́ / себе́ / собо́й va сам / сама́ / са́ми yonma-yon, plus
           iboralar: у себя́, про себя́, взять себя́ в ру́ки, сде́лай сам.

⚠️ ATAY QOCHILGAN (keyingi darslar): ка́ждый / весь / любо́й ning nozik
farqi (PR-77), кто́-то / кто́-нибудь (PR-78), никто́ … не (PR-79),
shaxssiz gaplar (PR-81), жамловчи sonlar — о́ба, тро́е (PR-82),
благодаря́ / несмотря́ на (PR-83).

⚠️ FAKTLAR (74-matn tekshirilgan):
  · Nil anʼanaviy ravishda ~6650 km, Amazonka ~6400 km deb hisoblanadi;
  · 2007-yilda Braziliya ekspeditsiyasi Amazonkaning boshini Peru
    janubidan topib, uzunligini ~6992 km deb eʼlon qilgan — bahs hamon
    tugamagan;
  · nizoning sababi — daryo QAYERDA boshlanadi va QAYERDA tugaydi degan
    savolga yagona javob yoʻqligi;
  · Amazonka suv miqdori boʻyicha shubhasiz birinchi: okeanga quyiladigan
    daryo suvining taxminan beshdan bir qismini u olib boradi;
  · Volga — Yevropaning eng uzun daryosi, ~3530 km.
  75 va 76 — toʻqima voqealar, real daʼvo yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_74_76.py --author=prime
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
    # PR-74 — sifat darajalari                        ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Са́мая дли́нная река́",
        "summary": (
            "PR-74 matni. Dunyodagi eng uzun daryo qaysi — Nilmi yoki "
            "Amazonkami? Savol oddiy koʻrinadi, lekin javob yoʻq: chunki "
            "daryo qayerda boshlanishini hech kim aniq ayta olmaydi."
        ),
        "order":   74,
        "grammar": [
            {
                "pattern":  "Са́мый + sifat — orttirma daraja",
                "meaning":  "Oʻzbekcha «eng». Diqqat: «са́мый» sifat kabi "
                            "turlanadi — са́мая река́, са́мое о́зеро.",
                "examples": ["са́мая дли́нная река́ в ми́ре",
                             "са́мый изве́стный отве́т"],
            },
            {
                "pattern":  "Ikki xil solishtirish: чем va Роди́тельный",
                "meaning":  "«Ни́л длинне́е, чем Амазо́нка» = «Ни́л длинне́е "
                            "Амазо́нки». Ikkinchisi oʻzbekcha «-dan» ning aynan "
                            "oʻzi.",
                "examples": ["Амазо́нка длинне́е Ни́ла.",
                             "Она́ ши́ре, чем все други́е ре́ки."],
            },
            {
                "pattern":  "Всех va всего́",
                "meaning":  "«Всех» — sanaladigan narsalardan, «всего́» — umuman "
                            "hamma narsadan. Matnda ikkalasi ham bor.",
                "examples": ["Э́та река́ несёт бо́льше всех.",
                             "Бо́льше всего́ учёных интересу́ет нача́ло реки́."],
            },
        ],
        "body": '''<p>Како́й вопро́с мо́жет быть <span class="cn-word" data-tr="oddiyroq">про́ще</span>: кака́я река́ в ми́ре <strong>са́мая дли́нная</strong>?</p>

<p>В шко́ле мно́гие годы отвеча́ли: Нил. Его́ <span class="cn-word" data-tr="uzunligi">длина́</span> — приме́рно 6650 киломе́тров. Амазо́нка <span class="cn-word" data-pos="verb" data-tr="hisoblanardi">счита́лась</span> второ́й: о́коло 6400.</p>

<p>Но в 2007 году́ брази́льская <span class="cn-word" data-tr="ekspeditsiya">экспеди́ция</span> <span class="cn-word" data-pos="verb" data-tr="koʻtarildi">подняла́сь</span> высоко́ в го́ры на ю́ге Перу́ и нашла́ друго́й <span class="cn-word" data-tr="manba, boshlanish joyi">исто́к</span> Амазо́нки. Е́сли счита́ть отту́да, Амазо́нка получа́ется <strong>длинне́е</strong> — почти́ 6992 киломе́тра.</p>

<p><span class="cn-word" data-tr="bahs">Спор</span> идёт до сих пор. И де́ло не в <span class="cn-word" data-tr="oʻlchov asboblari">приборах</span>.</p>

<p>Де́ло в том, что у большо́й реки́ нет одно́й то́чки нача́ла. У большо́й реки́ <span class="cn-word" data-tr="oʻnlab">деся́тки</span> <span class="cn-word" data-tr="irmoqlar">прито́ков</span>. Кото́рый из них счита́ть <span class="cn-word" data-tr="asosiy">гла́вным</span>? Тот, что <strong>длинне́е</strong>? Тот, что <span class="cn-word" data-pos="verb" data-tr="olib boradi">несёт</span> <strong>бо́льше</strong> воды́? Тот, что <strong>вы́ше</strong> в гора́х? Ка́ждый отве́т даёт другу́ю ци́фру.</p>

<p>С <span class="cn-word" data-tr="quyilish joyi, deltasi">у́стьем</span> ещё <strong>ху́же</strong>. Амазо́нка <span class="cn-word" data-pos="verb" data-tr="quyiladi">впада́ет</span> в океа́н широ́кой <span class="cn-word" data-tr="daryo ogʻzi, keng quyilish">де́льтой</span>, и грани́цу ме́жду реко́й и океа́ном ка́ждый учёный прово́дит <span class="cn-word" data-tr="har xil, boshqacha">по-ра́зному</span>.</p>

<p>Зато́ в одно́м спо́ра нет. По <span class="cn-word" data-tr="suv miqdori">коли́честву воды́</span> Амазо́нка — пе́рвая, и <strong>гора́здо</strong> впереди́ <strong>всех</strong> остальны́х. Она́ одна́ несёт в океа́н приме́рно <strong>пя́тую часть</strong> все́й речно́й воды́ Земли́.</p>

<p>Для <span class="cn-word" data-tr="solishtirish uchun">сравне́ния</span>: Во́лга, <strong>са́мая дли́нная</strong> река́ Евро́пы, коро́че Амазо́нки почти́ в два ра́за — 3530 киломе́тров.</p>

<p>Так кака́я река́ <strong>са́мая дли́нная</strong>? <span class="cn-word" data-tr="halol, rostini aytganda">Че́стный</span> отве́т: <span class="cn-word" data-tr="qarab turadi">зави́сит</span> от того́, где вы реши́те, что река́ начала́сь.</p>

<p><strong>Бо́льше всего́</strong> здесь интере́сно друго́е. Вопро́с был не о реке́. Он был о том, как мы <span class="cn-word" data-pos="verb" data-tr="oʻlchaymiz">измеря́ем</span>.</p>''',
        "questions": [
            {
                "text": "Nega «eng uzun daryo qaysi?» degan savolga aniq javob yoʻq?",
                "choices": [
                    "Chunki oʻlchov asboblari aniq emas",
                    "Chunki daryolar har yili uzunligini oʻzgartiradi",
                    "Chunki daryoning qayerda boshlanishi va tugashini har kim boshqacha belgilaydi",
                    "Chunki Nil bilan Amazonka bir xil uzunlikda"
                ],
                "answer": 2,
                "explanation": "«Де́ло не в прибо́рах» deb matn ochiq aytadi. "
                               "Irmoqlarning qaysi biri asosiy sanalishi va "
                               "delta qayerda tugashi — ikkalasi ham "
                               "kelishilmagan.",
            },
            {
                "text": "Nega matnda «коро́че Амазо́нки», lekin «длинне́е, чем Амазо́нка» ham boʻlishi mumkin edi?",
                "choices": [
                    "Chunki ikkalasi ham toʻgʻri — bu solishtirishning ikki yoʻli",
                    "Chunki «коро́че» faqat Роди́тельный bilan ishlatiladi",
                    "Chunki «чем» faqat odamlar haqida ishlatiladi",
                    "Chunki bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "«Чем + Имени́тельный» (vergul bilan) va «чем» siz "
                               "Роди́тельный — ikkalasi ham meʼyorda. Ikkinchisi "
                               "oʻzbekcha «Amazonka<b>dan</b> qisqa» ga aynan "
                               "toʻgʻri keladi.",
            },
            {
                "text": "Amazonka nimasi bilan shubhasiz birinchi?",
                "choices": [
                    "Uzunligi bilan",
                    "Irmoqlari soni bilan",
                    "Balandligi bilan",
                    "Okeanga olib boradigan suv miqdori bilan — dunyo daryo suvining beshdan bir qismi"
                ],
                "answer": 3,
                "explanation": "«По коли́честву воды́ Амазо́нка — пе́рвая, и "
                               "гора́здо впереди́ всех остальны́х». Uzunlik "
                               "boʻyicha bahs ketadi, suv boʻyicha esa "
                               "yoʻq.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-75 — свой                                  BIOGRAFIK HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Свой дом",
        "summary": (
            "PR-75 matni. Olga yigirma yilda oʻn bir marta koʻchdi va bir "
            "quti hech qachon ochilmadi. Nihoyat oʻz kvartirasi paydo "
            "boʻlganda, u birinchi navbatda oʻsha qutini ochdi."
        ),
        "order":   75,
        "grammar": [
            {
                "pattern":  "Свой — gapning egasiga tegishli",
                "meaning":  "Oʻzbekcha «oʻz». Matnda beshta kelishikda uchraydi: "
                            "свои́ ве́щи, свое́й ко́мнаты, своего́ угла́, "
                            "свои́м, о своём.",
                "examples": ["Она́ вози́ла свои́ ве́щи из кварти́ры в кварти́ру.",
                             "У неё не́ было своего́ угла́."],
            },
            {
                "pattern":  "Свой ↔ её",
                "meaning":  "Matnda ataylab bittasi «её» qoʻyilgan — u boshqa "
                            "odamning narsasini bildiradi. Farqni koʻring.",
                "examples": ["Она́ откры́ла свою́ коро́бку. (oʻzinikini)",
                             "Она́ помни́ла её слова́. (buvisining soʻzlarini)"],
            },
            {
                "pattern":  "Свой = «ijara emas, oʻziniki»",
                "meaning":  "Ikkinchi maʼnosi. Sarlavhaning oʻzi shu haqda: "
                            "«свой дом» — ijaraga olingan emas.",
                "examples": ["Наконе́ц у неё появи́лся свой дом."],
            },
        ],
        "body": '''<p>За два́дцать лет О́льга <span class="cn-word" data-pos="verb" data-tr="koʻchdi">переезжа́ла</span> оди́ннадцать раз.</p>

<p>Она́ <span class="cn-word" data-pos="verb" data-tr="ijaraga olardi">снима́ла</span> ко́мнаты, пото́м <span class="cn-word" data-tr="ijaraga olingan">съёмные</span> кварти́ры. Ка́ждый раз она́ вози́ла из кварти́ры в кварти́ру <strong>свои́</strong> ве́щи: две су́мки оде́жды, ла́мпу и коро́бку.</p>

<p>Коро́бку она́ <span class="cn-word" data-pos="verb" data-tr="ochmasdi">не открыва́ла</span>.</p>

<p>Внутри́ лежа́ли шесть <span class="cn-word" data-tr="tarelkalar, likopchalar">таре́лок</span>. Их дала́ ей ба́бушка, когда́ О́льге бы́ло девятна́дцать. Ба́бушка тогда́ сказа́ла: «Откро́ешь, когда́ бу́дет <strong>свой</strong> дом». О́льга по́мнила <strong>её</strong> слова́ то́чно, <span class="cn-word" data-tr="soʻzma-soʻz">сло́во в сло́во</span>.</p>

<p>В пе́рвой кварти́ре таре́лки бы́ло <span class="cn-word" data-tr="qoʻyadigan joy yoʻq">не́куда ста́вить</span>. Во второ́й <span class="cn-word" data-tr="uy egasi (ayol)">хозя́йка</span> не разреша́ла ме́нять <span class="cn-word" data-tr="idish-tovoq">посу́ду</span>. В тре́тьей О́льга <span class="cn-word" data-pos="verb" data-tr="yashadi">прожила́</span> то́лько во́семь ме́сяцев.</p>

<p>Пото́м она́ <span class="cn-word" data-pos="verb" data-tr="toʻxtatdi">переста́ла</span> <span class="cn-word" data-pos="verb" data-tr="ochishga urinmoq">пыта́ться</span>. Коро́бка про́сто перее́хала ещё во́семь раз.</p>

<p>О́льга рабо́тала <span class="cn-word" data-tr="buxgalter">бухга́лтером</span>, пото́м откры́ла <strong>своё</strong> ма́ленькое де́ло. Де́ньги <span class="cn-word" data-pos="verb" data-tr="yigʻildi">копи́лись</span> ме́дленно — четы́рнадцать лет.</p>

<p>В со́рок два го́да она́ купи́ла кварти́ру. Одна́ ко́мната, ку́хня, седьмо́й <span class="cn-word" data-tr="qavat">эта́ж</span>.</p>

<p>В день <span class="cn-word" data-tr="koʻchib oʻtish">перее́зда</span> О́льга не ста́ла <span class="cn-word" data-pos="verb" data-tr="ochib joylashtirmoq">разбира́ть</span> су́мки. Она́ се́ла на пол посреди́ <strong>свое́й</strong> ко́мнаты и откры́ла коро́бку.</p>

<p>Все шесть таре́лок бы́ли <span class="cn-word" data-tr="butun, sinmagan">це́лые</span>.</p>

<p>Она́ <span class="cn-word" data-pos="verb" data-tr="yuvdi">вы́мыла</span> их и поста́вила в <span class="cn-word" data-tr="shkaf">шкаф</span>. Пото́м до́лго сиде́ла на полу́ и смотре́ла на них.</p>

<p>Ба́бушка была́ права́ в одно́м, но не совсе́м. <strong>Свой</strong> дом — э́то не сте́ны и не <span class="cn-word" data-tr="hujjatlar">докуме́нты</span>. Э́то ме́сто, где мо́жно <span class="cn-word" data-pos="verb" data-tr="ochib, joyiga qoʻymoq">распакова́ть</span> после́днюю коро́бку.</p>''',
        "questions": [
            {
                "text": "Nega Olga qutini yigirma yil davomida ochmadi?",
                "choices": [
                    "Quti qulflangan edi",
                    "U buvisining «oʻz uying boʻlganda ochasan» degan gapini eslardi",
                    "U tarelkalarni yoqtirmasdi",
                    "Quti juda ogʻir edi"
                ],
                "answer": 1,
                "explanation": "«Откро́ешь, когда́ бу́дет свой дом». Yigirma yil "
                               "va oʻn bir koʻchish davomida bu shart "
                               "bajarilmagan edi.",
            },
            {
                "text": "Nega matnda «свои́ ве́щи», lekin «её слова́»?",
                "choices": [
                    "Chunki «слова́» koʻplikda",
                    "Chunki «её» qisqaroq",
                    "Bu matndagi xato",
                    "Chunki narsalar Olganiki — u gapning egasi; soʻzlar esa buvisiniki"
                ],
                "answer": 3,
                "explanation": "«Свой» faqat gapning egasiga tegishli narsani "
                               "bildiradi. Buvi boshqa odam, shuning uchun uning "
                               "soʻzlari «её слова́». Agar «свои́ слова́» "
                               "deyilsa, Olganing oʻz soʻzlari chiqardi.",
            },
            {
                "text": "Hikoya oxirida «свой дом» qanday taʼriflanadi?",
                "choices": [
                    "Devorlar va hujjatlar",
                    "Yettinchi qavatdagi kvartira",
                    "Oxirgi qutini ochish mumkin boʻlgan joy",
                    "Buvidan qolgan olti tarelka"
                ],
                "answer": 2,
                "explanation": "«Э́то ме́сто, где мо́жно распакова́ть после́днюю "
                               "коро́бку». Yaʼni «oʻz uy» — mulk emas, "
                               "koʻchmaslikka ishonch.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-76 — себя́ va сам                                    PORTRET
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Сде́лай сам",
        "summary": (
            "PR-76 matni. Viktor Stepanovichning ustaxonasi buzilgan narsalarni "
            "tuzatmaydi — u odamlarga oʻzlari tuzatishni oʻrgatadi. Va aslida "
            "u butunlay boshqa narsani tuzatadi."
        ),
        "order":   76,
        "grammar": [
            {
                "pattern":  "Сам — taʼkid, egaga moslashadi",
                "meaning":  "«Hech kim yordam bermadi, oʻzi qildi»: сам, сама́, "
                            "са́ми. Ustaxonaning nomi ham shu — «Сде́лай сам».",
                "examples": ["Она́ сама́ почини́ла кран.",
                             "Ма́льчик сам собра́л велосипе́д."],
            },
            {
                "pattern":  "Себя́ / себе́ / собо́й — toʻldiruvchi",
                "meaning":  "Har doim gapning egasiga qaytadi va hamma shaxs "
                            "uchun bitta shakl. Matnda uchala kelishikda ham bor.",
                "examples": ["Он не ве́рил в себя́.",
                             "Ви́ктор Степа́нович был недово́лен собо́й."],
            },
            {
                "pattern":  "Iboralar: у себя́ · про себя́ · взять себя́ в ру́ки",
                "meaning":  "Kundalik nutqning tayyor boʻlaklari. «У себя́» — oʻz "
                            "joyida, «про себя́» — ichida, ovoz chiqarmay.",
                "examples": ["Ма́стер всегда́ у себя́ с восьми́ утра́.",
                             "Она́ счита́ла про себя́ до десяти́."],
            },
        ],
        "body": '''<p>На двери́ ма́ленькой <span class="cn-word" data-tr="ustaxona">мастерско́й</span> <span class="cn-word" data-pos="verb" data-tr="osilib turibdi">виси́т</span> <span class="cn-word" data-tr="taxtacha, yozuv">табли́чка</span>: «Сде́лай <strong>сам</strong>».</p>

<p>Хозя́ина зову́т Ви́ктор Степа́нович. Он <strong>у себя́</strong> с восьми́ утра́ до шести́ ве́чера.</p>

<p>Лю́ди прино́сят ему́ <span class="cn-word" data-tr="buzilgan">сло́манные</span> ве́щи: <span class="cn-word" data-tr="choynaklar">ча́йники</span>, ла́мпы, велосипе́ды, <span class="cn-word" data-tr="stullar">стулья</span>. Ви́ктор Степа́нович смо́трит на вещь, <span class="cn-word" data-pos="verb" data-tr="bosh irgʻaydi">кива́ет</span> — и не берёт <span class="cn-word" data-tr="asboblar">инструме́нты</span>.</p>

<p>Вме́сто э́того он <span class="cn-word" data-pos="verb" data-tr="oʻtqizadi">сажа́ет</span> челове́ка за стол и говори́т: «Дава́йте вме́сте. <span class="cn-word" data-pos="verb" data-tr="ushlang">Держи́те</span> вот здесь».</p>

<p>Пе́рвые де́сять мину́т лю́ди <span class="cn-word" data-pos="verb" data-tr="jahllari chiqadi">сердя́тся</span>. Они́ пришли́ <span class="cn-word" data-tr="tayyor natija uchun">за гото́вым результа́том</span>, а не за уро́ком.</p>

<p>Пото́м всё <span class="cn-word" data-pos="verb" data-tr="oʻzgaradi">меня́ется</span>.</p>

<p>Ната́лья, <span class="cn-word" data-tr="oʻqituvchi ayol">учи́тельница</span> из <span class="cn-word" data-tr="qoʻshni">сосе́дней</span> шко́лы, принесла́ ста́рую ла́мпу. Че́рез со́рок мину́т она́ <strong>сама́</strong> нашла́ <span class="cn-word" data-tr="uzilgan sim">обры́в в про́воде</span>. Она́ до́лго смотре́ла на свои́ ру́ки и <span class="cn-word" data-pos="verb" data-tr="takrorlardi">повторя́ла</span> <strong>про себя́</strong>: «Я э́то <strong>сама́</strong>».</p>

<p>Оди́н ма́льчик, Ти́мур, приходи́л четы́ре ра́за <span class="cn-word" data-tr="bitta velosiped bilan">с одни́м велосипе́дом</span>. На четвёртый раз он <strong>сам</strong> поменя́л <span class="cn-word" data-tr="zanjir">цепь</span>. Ви́ктор Степа́нович да́же не встал со <span class="cn-word" data-tr="stuldan">сту́ла</span>.</p>

<p>Я спроси́л ма́стера, почему́ он рабо́тает так ме́дленно. Он мог бы почини́ть ла́мпу за пять мину́т.</p>

<p>Ви́ктор Степа́нович <span class="cn-word" data-pos="verb" data-tr="qoʻlini siltadi">махну́л руко́й</span> на табли́чку.</p>

<p>«Челове́к прино́сит ла́мпу, — сказа́л он. — А ухо́дит с мы́слью, что <span class="cn-word" data-pos="verb" data-tr="uddalay oladi">спра́вится</span>. В сле́дующий раз он не пойдёт к ма́стеру. Он возьмёт <strong>себя́</strong> в ру́ки и попро́бует».</p>

<p>Он <span class="cn-word" data-pos="verb" data-tr="jim qoldi">помолча́л</span> и <span class="cn-word" data-pos="verb" data-tr="qoʻshib qoʻydi">доба́вил</span>: «Я не чиню́ ве́щи. Я чиню́ то, что лю́ди ду́мают о <strong>себе́</strong>».</p>''',
        "questions": [
            {
                "text": "Viktor Stepanovich buzilgan narsalarni nima qiladi?",
                "choices": [
                    "Tez va arzon tuzatib beradi",
                    "Ularni umuman qabul qilmaydi",
                    "Egasini stol yoniga oʻtqizib, birga tuzatishga oʻrgatadi",
                    "Yangisini sotadi"
                ],
                "answer": 2,
                "explanation": "«Дава́йте вме́сте. Держи́те вот здесь». Shuning "
                               "uchun eshikdagi yozuv — «Сде́лай сам».",
            },
            {
                "text": "Nega matnda «она́ сама́ нашла́», lekin «он возьмёт себя́ в ру́ки»?",
                "choices": [
                    "Chunki birinchisi ayol, ikkinchisi erkak haqida",
                    "Chunki birinchisi «kim?» degan taʼkid, ikkinchisi «kimni?» degan toʻldiruvchi",
                    "Chunki «себя́» faqat kelasi zamonda ishlatiladi",
                    "Bu matndagi xato"
                ],
                "answer": 1,
                "explanation": "«Сама́ нашла́» — hech kim yordam bermadi (taʼkid). "
                               "«Возьмёт себя́ в ру́ки» — «kimni?» degan savolga "
                               "javob (toʻldiruvchi). Oʻzbekchada ikkalasi ham "
                               "«oʻzi», ruschada esa ikki xil soʻz.",
            },
            {
                "text": "Usta oʻz ishini qanday tushuntiradi?",
                "choices": [
                    "U narsalarni emas, odamlarning oʻzlari haqidagi fikrini tuzatadi",
                    "U shunchaki sekin ishlashni yoqtiradi",
                    "U yordamchi topa olmaydi",
                    "U asboblarini hech kimga bermaydi"
                ],
                "answer": 0,
                "explanation": "«Я не чиню́ ве́щи. Я чиню́ то, что лю́ди ду́мают о "
                               "себе́». Timur toʻrtinchi safar zanjirni oʻzi "
                               "almashtirgani — shuning isboti.",
            },
        ],
    },
]
