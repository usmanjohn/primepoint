# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-68 … PR-70.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 68 — sirli hikoya, 69 — hayot hikoyasi (haqiqiy odam),
70 — ilmiy-ommabop. (65 kundalik daftar, 66 ilmiy-ommabop, 67 intervyu edi —
uchta bir xil shakl ketma-ket kelmayapti.)

Grammatika chegarasi (kumulyativ qoida):
  68-matn: ли. Bilvosita savol beshta joyda («не знал, придёт ли», «спросил,
           знают ли», «не помнил, сколько» — savol soʻzli variant ham
           qarshi qoʻyilgan) va oxirida «вряд ли».
  69-matn: тот, кто / то, что. Beshta shaklda: тот кто, то что, все кто,
           о том что, дело в том что.
  70-matn: действительные причастия — живущие, стоящие, работающие,
           идущие, выросший, изучающие. Otdan keyin turganda vergul bilan.

⚠️ ATAY QOCHILGAN (keyingi darslar): страдательные причастия (PR-71),
деепричастие (PR-72), qisqa sifat — рад, готов, прав (PR-73), SIFAT
DARAJALARI — самый / больше / лучше / глубже (PR-74), свой (PR-75),
себя (PR-76), кто-то / кто-нибудь (PR-78).
Yagona istisno — 68-matndagi sarlavha va matndagi «никто не знал»:
ikki inkor PR-79 da oʻrgatiladi, lekin bu ibora tocda oʻsha nom bilan
rejalashtirilgan va oldingi matnlarda ham lugʻat sifatida uchragan.
cn-word izohi berilgan.

⚠️ FAKTLAR:
  69-matn — HAQIQIY ODAM: Жадав Пайенг (Jadav Payeng), Hindiston, Assam,
  Majuli oroli. 1979 da toshqindan keyin qumli orolda yalangʻoch yer qolgan;
  u yolgʻiz bambuk va daraxt ekishni boshlagan; qirq yildan keyin ~550
  gektar oʻrmon paydo boʻlgan, unga «Молаи» laqabidan «Молаи» oʻrmoni deb
  nom berilgan; u yerga fillar, karkidonlar va yoʻlbarslar keladi;
  2015-yilda «Падма Шри» davlat mukofotini olgan.
  70-matn — Norilsk qutb tuni ~45 kun; abadiy muzloq (вечная мерзлота)
  ustidagi uylar «сваи» — ustunlar ustiga quriladi, aks holda uyning issigʻi
  yerni eritadi; nenetslar — kiyik boquvchi koʻchmanchilar, chumda yashaydi;
  Yakutskda qishda -50 gradusgacha sovuq boʻladi.
  68-matn — toʻqima voqea, real daʼvo yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_68_70.py --author=prime
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
    # PR-68 — ли                                       SIRLI HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Никто не знал, придёт ли он",
        "summary": (
            "PR-68 matni. Har yili 1-sentabrda kichik qishloq maktabiga "
            "kitob toʻla posilka keladi, lekin joʻnatuvchisi yozilmagan. "
            "Qorovul Nikolay Ivanovich sirni ochadi — va sir ochilgach, "
            "savolning oʻzi keraksiz boʻlib qoladi."
        ),
        "order":   68,
        "grammar": [
            {
                "pattern":  "Bilvosita savol: ли",
                "meaning":  "Savolni boshqa gap ichiga solganda ли majburiy. U "
                            "soʻralayotgan soʻzdan keyin turadi — oʻzbekcha "
                            "«-mi» kabi.",
                "examples": ["Никто не знал, придёт ли посылка.",
                             "Он спросил, знают ли на почте отправителя."],
            },
            {
                "pattern":  "Savol soʻzi bor boʻlsa — ли yoʻq",
                "meaning":  "«Кто присылает», «откуда приходит» — bu gaplarda "
                            "savol soʻzi bor, shuning uchun ли qoʻyilmaydi. Matn "
                            "ikkala qurilishni yonma-yon koʻrsatadi.",
                "examples": ["Никто не знал, кто присылает книги.",
                             "Он посмотрел, откуда пришла посылка."],
            },
            {
                "pattern":  "Вряд ли",
                "meaning":  "«Dargumon» degan tayyor ibora. Ichida ли turibdi, "
                            "lekin u qotib qolgan — alohida tahlil qilinmaydi.",
                "examples": ["Вряд ли мы узнаем, кто это."],
            },
        ],
        "body": '''<p>Каждый год, первого сентября, в школу села Ивановка приходит <span class="cn-word" data-tr="pochta posilkasi">посылка</span>. <span class="cn-word" data-tr="ichida">Внутри</span> — книги. Новые, хорошие книги.</p>

<p><span class="cn-word" data-tr="joʻnatuvchi">Отправителя</span> в посылке нет. Только адрес школы и <span class="cn-word" data-tr="sana">дата</span>.</p>

<p>Первая посылка пришла в 2003 году. Учителя тогда <span class="cn-word" data-pos="verb" data-tr="qaror qilishdi">решили</span>, что это <span class="cn-word" data-tr="tasodif">случайность</span>. Но через год посылка пришла снова. И ещё через год.</p>

<p>Каждое лето в школе начинался один и тот же <span class="cn-word" data-tr="suhbat, gap">разговор</span>. <strong>Никто не знал, придёт ли</strong> посылка в этом году. И <strong>никто не знал, кто</strong> её присылает.</p>

<p>Директор школы несколько раз <span class="cn-word" data-pos="verb" data-tr="soʻradi">спрашивал</span> на почте, <strong>знают ли</strong> там отправителя. На почте отвечали, что не знают: посылку <span class="cn-word" data-pos="verb" data-tr="joʻnatishadi">присылают</span> без имени.</p>

<p><span class="cn-word" data-tr="qorovul">Сторож</span> Николай Иванович работал в школе тридцать лет. <span class="cn-word" data-tr="bir kuni">Однажды</span> он взял старые посылки и посмотрел, <strong>откуда они пришли</strong>.</p>

<p>Все <span class="cn-word" data-tr="pochta shtempeli">штампы</span> были из одного города — из Иркутска.</p>

<p>Николай Иванович написал письмо на иркутскую почту. Он спросил, <strong>можно ли</strong> узнать имя <span class="cn-word" data-tr="joʻnatuvchining">отправителя</span>. Он не <span class="cn-word" data-pos="verb" data-tr="umid qilmasdi">надеялся</span> на ответ. «<strong>Вряд ли</strong> они <span class="cn-word" data-pos="verb" data-tr="qidira boshlaydi">станут искать</span>», — думал он.</p>

<p>Ответ пришёл через два месяца. Книги присылала <span class="cn-word" data-tr="ayol">женщина</span> по имени Ирина Сергеевна. Она училась в этой школе сорок лет назад, потом <span class="cn-word" data-pos="verb" data-tr="ketib qoldi">уехала</span> и стала врачом.</p>

<p>В 2003 году она позвонила в <span class="cn-word" data-tr="tuman markaziga">район</span> и спросила, <strong>работает ли</strong> ещё её старая школа. Ей ответили, что работает. <span class="cn-word" data-tr="oʻshandan beri">С тех пор</span> она присылает книги.</p>

<p>Теперь в Ивановке знают её имя. Но первого сентября никто уже не спрашивает, придёт ли посылка.</p>

<p>Все <span class="cn-word" data-tr="allaqachon, shusiz ham">и так</span> знают, что придёт.</p>''',
        "questions": [
            {
                "text": "Nikolay Ivanovich sirni qanday yechdi?",
                "choices": [
                    "Pochtachini kuzatib turdi",
                    "Eski posilkalardagi shtempellarga qaradi — hammasi Irkutskdan edi",
                    "Direktordan soʻradi",
                    "Kitoblarning ichidagi imzoni topdi"
                ],
                "answer": 1,
                "explanation": "«Он взял старые посылки и посмотрел, откуда "
                               "они пришли. Все штампы были из одного "
                               "города — из Иркутска». Shundan keyin u xat "
                               "yozdi.",
            },
            {
                "text": "Nega matnda «знают ли там отправителя», lekin «кто её присылает» — birida ли bor, ikkinchisida yoʻq?",
                "choices": [
                    "Chunki birinchisi oʻtgan zamonda",
                    "Chunki ikkinchisi inkor gap",
                    "Chunki ikkinchi gapda savol soʻzi «кто» bor — ли keraksiz",
                    "Chunki «присылать» feʼli ли ni olmaydi"
                ],
                "answer": 2,
                "explanation": "Ли faqat «ha/yoʻq» savoli boʻlganda qoʻyiladi. "
                               "Gapda «кто», «где», «откуда» kabi savol soʻzi "
                               "boʻlsa, ли ortiqcha — xuddi oʻzbekchada «kim "
                               "joʻnatadimi» deyilmagani kabi.",
            },
            {
                "text": "Hikoyaning oxiri nima demoqchi?",
                "choices": [
                    "Sir ochilgani yaxshi boʻlmadi",
                    "Irina Sergeyevna endi kitob joʻnatmaydi",
                    "Pochta xizmati yaxshi ishlaydi",
                    "Endi «keladimi?» degan savolning oʻzi kerak emas — hamma ishonadi"
                ],
                "answer": 3,
                "explanation": "«Никто уже не спрашивает, придёт ли посылка. "
                               "Все и так знают, что придёт». Yaʼni bilvosita "
                               "savol («придёт ли») oddiy tasdiqqa («что "
                               "придёт») aylandi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-69 — тот, кто / то, что                      HAYOT HIKOYASI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Тот, кто сажает деревья",
        "summary": (
            "PR-69 matni. Haqiqiy odam haqida: hindistonlik Jadav Payeng "
            "1979-yilda yalangʻoch qumli orolda yolgʻiz daraxt eka boshlagan "
            "va qirq yilda 550 gektarlik oʻrmon yaratgan. Faktlar haqiqiy."
        ),
        "order":   69,
        "grammar": [
            {
                "pattern":  "Тот, кто — odam haqida",
                "meaning":  "Ot boʻlmaganda «тот» otning oʻrnida turadi. Matnning "
                            "sarlavhasi ham, birinchi va oxirgi jumlasi ham shu "
                            "qurilishga qurilgan.",
                "examples": ["Тот, кто сажает дерево, думает о других.",
                             "Тот, кого считали странным, оказался прав."],
            },
            {
                "pattern":  "То, что — narsa yoki butun fikr haqida",
                "meaning":  "«То, что он сделал» — u qilgan ish. Predlogdan keyin "
                            "«то» hech qachon tushib qolmaydi: о том, что…",
                "examples": ["То, что он сделал, теперь называют лесом.",
                             "Никто не думал о том, что будет через сорок лет."],
            },
            {
                "pattern":  "Все, кто + birlik feʼl · дело в том, что",
                "meaning":  "«Кто» dan keyingi feʼl har doim birlikda turadi. "
                            "«Дело в том, что…» = «Gap shundaki…».",
                "examples": ["Все, кто видел остров, говорил одно и то же.",
                             "Дело в том, что земля была пустая."],
            },
        ],
        "body": '''<p>В Индии есть <span class="cn-word" data-tr="maqol">пословица</span>: <strong>тот, кто</strong> сажает дерево, думает о других.</p>

<p>В 1979 году на реке Брахмапутра случилось большое <span class="cn-word" data-tr="toshqin">наводнение</span>. Вода ушла и оставила голый <span class="cn-word" data-tr="qumloq">песок</span>. На этом песке умерло много змей: там не было <span class="cn-word" data-tr="soya">тени</span>, и солнце убило их за один день.</p>

<p>Это увидел шестнадцатилетний мальчик. Его звали Жадав Пайенг. Он жил на острове Маджули и пас <span class="cn-word" data-tr="buyvollar">буйволов</span>.</p>

<p>Жадав пошёл к <span class="cn-word" data-tr="kattalar">взрослым</span> и спросил, что можно сделать. Ему ответили, что на песке деревья не растут.</p>

<p>Тогда он взял двадцать <span class="cn-word" data-tr="bambuk koʻchati">ростков бамбука</span> и посадил их сам.</p>

<p>Потом он приходил каждый день. Он носил воду в вёдрах. Он делал <span class="cn-word" data-tr="soyabon, chodir">навесы</span> из листьев, чтобы молодые деревья не сгорели на солнце. Он приносил <span class="cn-word" data-tr="chumolilar">муравьёв</span>, чтобы они меняли <span class="cn-word" data-tr="tuproq">почву</span>.</p>

<p><strong>Все, кто</strong> видел его в те годы, считал его странным. <strong>Дело в том, что</strong> работа была бесконечная, а <span class="cn-word" data-tr="natija">результат</span> никто не мог увидеть.</p>

<p>Жадав работал тридцать лет. Один.</p>

<p>В 2008 году на остров пришли <span class="cn-word" data-tr="mansabdorlar">чиновники</span>. Они искали <span class="cn-word" data-tr="fillar podasi">стадо слонов</span>. И нашли лес.</p>

<p>Никто не знал <span class="cn-word" data-tr="bu haqda">об этом</span> лесе. На карте его не было.</p>

<p>Сейчас <strong>то, что</strong> посадил Жадав, занимает пятьсот пятьдесят гектаров. Там живут слоны, <span class="cn-word" data-tr="karkidonlar">носороги</span>, олени и тигры. Лес называют «Молаи» — по <span class="cn-word" data-tr="laqab">прозвищу</span> Жадава.</p>

<p>В 2015 году Индия дала ему государственную <span class="cn-word" data-tr="mukofot">награду</span>.</p>

<p>Журналисты спрашивают его <strong>о том, что</strong> он чувствует. Жадав отвечает коротко: он просто продолжает сажать.</p>

<p><strong>Тот, кого</strong> считали странным, оказался <span class="cn-word" data-tr="oddiygina">просто</span> терпеливым.</p>''',
        "questions": [
            {
                "text": "Jadav Payeng nega daraxt eka boshladi?",
                "choices": [
                    "Hukumat undan shuni soʻradi",
                    "U orolda buyvollar uchun oʻtloq izlardi",
                    "Maktabda unga shunday topshiriq berishdi",
                    "Toshqindan keyin yalangʻoch qumda ilonlar soyasizlikdan qirilib ketdi"
                ],
                "answer": 3,
                "explanation": "«Там не было тени, и солнце убило их за один "
                               "день». Oʻn olti yoshli bola shuni koʻrgach, "
                               "yigirmata bambuk koʻchatini oʻzi ekdi.",
            },
            {
                "text": "Nega matnda «Все, кто видел его, считал» deyilgan — nega «считали» emas?",
                "choices": [
                    "Chunki gap bitta odam haqida",
                    "Chunki bu oʻtgan zamon",
                    "Chunki feʼl «кто» ga tegishli, «кто» dan keyin esa birlik turadi",
                    "Bu matndagi xato"
                ],
                "answer": 2,
                "explanation": "«Кто» dan keyingi feʼl har doim birlikda boʻladi, "
                               "hatto «все» bilan ham. Asosiy gapga tegishli feʼl "
                               "esa koʻplikda turishi mumkin — bu ikki alohida "
                               "gap.",
            },
            {
                "text": "Matn oxirida Jadav haqida qanday xulosa chiqariladi?",
                "choices": [
                    "Uni gʻalati deb hisoblashardi, aslida esa u shunchaki sabrli edi",
                    "U mashhur boʻlishni xohlagan",
                    "U aslida gʻalati odam edi",
                    "U mukofot uchun ishlagan"
                ],
                "answer": 0,
                "explanation": "«Тот, кого считали странным, оказался просто "
                               "терпеливым». Bu yerda «тот» asosiy gapda ega "
                               "(И.п.), «кого» esa oʻz gapida obyekt (В.п.) — "
                               "darsning ikki kelishik qoidasi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-70 — действительные причастия              ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Люди, живущие на Севере",
        "summary": (
            "PR-70 matni. Rossiya Shimolida odamlar qanday yashaydi: qutb "
            "tuni, abadiy muzloq va ustunlar ustidagi uylar, kiyik boquvchi "
            "nenetslar. Sarlavhaning oʻzi — sifatdoshli oborot."
        ),
        "order":   70,
        "grammar": [
            {
                "pattern":  "Hozirgi zamon sifatdoshi: -ущ- / -ющ- / -ащ- / -ящ-",
                "meaning":  "«Они» shaklidan yasaladi: живу[т] → живущий. "
                            "Oʻzbekcha «-ayotgan / -adigan» ga toʻgʻri keladi.",
                "examples": ["люди, живущие на Севере",
                             "учёные, изучающие вечную мерзлоту"],
            },
            {
                "pattern":  "Oʻtgan zamon sifatdoshi: -вш- / -ш-",
                "meaning":  "Oʻtgan zamon erkak shaklidan: вырос → выросший. "
                            "Oʻzbekcha «-gan».",
                "examples": ["человек, выросший в тундре",
                             "поезд, пришедший утром"],
            },
            {
                "pattern":  "Vergul oʻringa bogʻliq",
                "meaning":  "Oborot otdan keyin tursa — ikki tomondan vergul. "
                            "Otdan oldin tursa (oʻzbekcha tartib) — vergulsiz.",
                "examples": ["дома, стоящие на сваях",
                             "стоящие на сваях дома"],
            },
        ],
        "body": '''<p>Над Полярным кругом солнце работает не так, как у нас. Зимой оно не встаёт, летом не садится. В Норильске <span class="cn-word" data-tr="qutb tuni">полярная ночь</span> длится сорок пять дней.</p>

<p><strong>Люди, живущие</strong> в таких городах, привыкают к этому. Но <span class="cn-word" data-tr="tabiat, muhit">природа</span> ставит и другие задачи.</p>

<p>Первая задача — <span class="cn-word" data-tr="abadiy muzloq">вечная мерзлота</span>. Это земля, которая не <span class="cn-word" data-pos="verb" data-tr="erimaydi">тает</span> даже летом. Она начинается в одном метре от поверхности и уходит вниз на сотни метров.</p>

<p>Дом, <span class="cn-word" data-pos="verb" data-tr="turgan">стоящий</span> на такой земле, греет её. Мерзлота тает, и дом начинает падать.</p>

<p>Поэтому на Севере строят иначе. <strong>Дома, стоящие</strong> в Якутске и Норильске, не касаются земли: они стоят на <span class="cn-word" data-tr="ustunlar, qoziqlar">сваях</span>. Между домом и землёй ходит <span class="cn-word" data-tr="sovuq havo">холодный воздух</span>. Земля остаётся <span class="cn-word" data-tr="sovuq">холодной</span>, и дом стоит.</p>

<p>Вторая задача — <span class="cn-word" data-tr="masofa">расстояние</span>. <strong>Ненцы, живущие</strong> в тундре, пасут <span class="cn-word" data-tr="bugʻular">оленей</span>. <span class="cn-word" data-tr="poda">Стадо</span> идёт за <span class="cn-word" data-tr="yem, oziq">кормом</span>, и люди идут за стадом. За год семья проходит сотни километров.</p>

<p>Их дом называется <span class="cn-word" data-tr="chum — kiyik terisidan chodir">чум</span>. Его можно собрать за час и разобрать за час.</p>

<p>Человек, <span class="cn-word" data-pos="verb" data-tr="oʻsgan">выросший</span> в тундре, читает снег как книгу. Он видит, где прошли олени и когда будет <span class="cn-word" data-tr="boʻron">пурга</span>.</p>

<p>Третья задача — <span class="cn-word" data-tr="ovqat">еда</span>. Овощи на Севере не растут. Но <strong>люди, живущие</strong> здесь тысячи лет, нашли решение: <span class="cn-word" data-tr="baliq">рыба</span> и оленина дают витамин D, который в другом месте даёт солнце.</p>

<p>Сейчас в тундре работают <strong>учёные, изучающие</strong> мерзлоту. Они говорят, что земля начала таять слишком быстро, и что дома на сваях теперь надо строить иначе.</p>

<p>Север учит одному: здесь выигрывает не <span class="cn-word" data-tr="kuchli">сильный</span>, а тот, кто <span class="cn-word" data-pos="verb" data-tr="dunyoni kuzatadi">смотрит по сторонам</span>.</p>''',
        "questions": [
            {
                "text": "Nega Shimolda uylar ustunlar ustiga quriladi?",
                "choices": [
                    "Uyning issigʻi abadiy muzloqni eritmasligi uchun",
                    "Qor uyni bosib qolmasligi uchun",
                    "Bugʻular uyning tagidan oʻtishi uchun",
                    "Toshqin suvi kirmasligi uchun"
                ],
                "answer": 0,
                "explanation": "«Дом, стоящий на такой земле, греет её. "
                               "Мерзлота тает, и дом начинает падать». "
                               "Ustunlar orasidan sovuq havo oʻtadi va yer "
                               "muzlagan holda qoladi.",
            },
            {
                "text": "«Человек, выросший в тундре» — bu qanday shakl va nimani bildiradi?",
                "choices": [
                    "Hozirgi zamon sifatdoshi — «oʻsayotgan odam»",
                    "Oddiy sifat — «katta odam»",
                    "Oʻtgan zamon sifatdoshi — «oʻsgan odam»",
                    "Ravishdosh — «oʻsib»"
                ],
                "answer": 2,
                "explanation": "«Вырос» — oʻtgan zamon erkak shakli, unda -л "
                               "yoʻq, shuning uchun -ш- qoʻshilib «выросший» "
                               "hosil boʻlgan. Uni «который вырос» deb yoyish "
                               "mumkin.",
            },
            {
                "text": "Nega «Дома, стоящие в Якутске…» da vergul bor, «стоящие на сваях дома» da esa yoʻq?",
                "choices": [
                    "Chunki birinchisi koʻplikda",
                    "Chunki ikkinchisida oborot qisqaroq",
                    "Bu erkin tanlov, qoida yoʻq",
                    "Chunki vergul oborot otdan KEYIN turgandagina qoʻyiladi"
                ],
                "answer": 3,
                "explanation": "Oborot otdan keyin tursa — ikki tomondan vergul. "
                               "Otdan oldin tursa (oʻzbekcha tartib — «ustunlar "
                               "ustida turgan uylar») vergul umuman "
                               "qoʻyilmaydi.",
            },
        ],
    },
]
