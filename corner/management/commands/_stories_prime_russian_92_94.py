# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-92 … PR-94.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.
⛔ URGʻU BELGISI YOʻQ — 2026-08-24 dagi qaror.

Janr xilma-xilligi: 92 — chat yozishmasi (butunlay yangi shakl,
kursda birinchi marta), 93 — hayot hikoyasi (birinchi suhbat),
94 — ilmiy-ommabop (iboralarning kelib chiqishi).

Grammatika chegarasi (kumulyativ qoida):
  92-matn: xabar tili — qisqartmalar (спс, пжл, крч, норм, др),
           nuqtasiz qisqa javoblar va nuqtali javobning sovuq ohangi.
           Matnning oxiri aynan shu nuqta ustiga qurilgan.
  93-matn: сдавать/сдать, поступить, собеседование savollari,
           «стать кем» (Творительный), rezyume leksikasi.
  94-matn: frazeologizmlar va ularning kelib chiqishi.

⚠️ ATAY QOCHILGAN (keyingi darslar): maqollar (PR-95),
одеть/надеть juftligi (PR-96), punktuatsiya qoidalari (PR-97),
insho qurilishi (PR-98).

⚠️ FAKTLAR:
  92 va 93 — toʻqima matnlar, real daʼvo yoʻq. 92-dagi qisqartmalar
  (спс, пжл, крч, норм, др, сек) — rus yozishmasida haqiqatan
  ishlatiladigan shakllar; qisqa xabar oxiridagi nuqtaning sovuq
  eshitilishi ham zamonaviy yozishma meʼyori.
  94-matn — iboralarning kelib chiqishi haqidagi qabul qilingan
  izohlar: баклуши (yogʻoch qoshiq uchun yorilgan boʻlaklar),
  нос ← носить (oʻzi bilan olib yuriladigan hisob taxtachasi),
  спустя/засучив рукава (eski rus kiyimining uzun yenglari),
  водить за нос (yarmarkadagi ayiqlar). Bular lugʻatlarda
  keltiriladigan standart etimologiyalar.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_92_94.py --author=prime
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
    # PR-92 — xabar tili                             CHAT YOZISHMASI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Чат группы 11-«А»",
        "summary": (
            "PR-92 matni. Sinf chatida tugʻilgan kun tayyorgarligi. Hammasi "
            "yaxshi ketayotgan edi, toki bir kishi javob oxiriga nuqta "
            "qoʻymaguncha — va butun chat tinchib qolmaguncha."
        ),
        "order":   92,
        "grammar": [
            {
                "pattern":  "Сокращения: спс · пжл · крч · норм · др",
                "meaning":  "Yozishmada unlilar tashlab ketiladi, undoshlar "
                            "qoladi. Rasmiy xatga hech qachon kirmaydi.",
                "examples": ["спс за идею", "крч, встречаемся в 5"],
            },
            {
                "pattern":  "Точка в коротком сообщении",
                "meaning":  "Qisqa javob oxiridagi nuqta sovuq yoki xafa "
                            "ohang beradi. «Хорошо» — mayli; «Хорошо.» — "
                            "«gapni yopdik».",
                "examples": ["Хорошо — oddiy rozilik",
                             "Хорошо. — sovuq rozilik"],
            },
            {
                "pattern":  "Скобки вместо интонации",
                "meaning":  "Chatda ovoz yoʻq, shuning uchun ohang «))», "
                            "emoji va undov belgisi bilan beriladi.",
                "examples": ["Спасибо))", "Спасибо!"],
            },
        ],
        "body": '''<p>В чате 11-«А» готовили <span class="cn-word" data-tr="syurpriz">сюрприз</span>. У Дилнозы в пятницу день рождения.</p>

<p><strong>Бекзод:</strong> ребят, у Дилнозы в пт <strong>др</strong></p>

<p><strong>Афсона:</strong> знаю! я торт беру</p>

<p><strong>Бекзод:</strong> <strong>оч</strong> хорошо, тогда я шарики</p>

<p><strong>Катя:</strong> а я <span class="cn-word" data-tr="sovgʻa">подарок</span>, <span class="cn-word" data-tr="faqat">только</span> не знаю какой</p>

<p><strong>Афсона:</strong> книгу? она любит читать</p>

<p><strong>Катя:</strong> <strong>спс</strong> за идею))</p>

<p><strong>Бекзод:</strong> <strong>крч</strong>, собираемся в 5, кабинет 12</p>

<p><strong>Афсона:</strong> <strong>норм</strong></p>

<p><strong>Катя:</strong> а кто её <span class="cn-word" data-pos="verb" data-tr="ushlab turadi">задержит</span>, чтобы мы успели?</p>

<p><strong>Бекзод:</strong> я попрошу Шербека, он <span class="cn-word" data-pos="verb" data-tr="oʻylab topadi">придумает</span> что-нибудь</p>

<p><strong>Афсона:</strong> только пусть не говорит про торт, <span class="cn-word" data-pos="verb" data-tr="taxmin qiladi">догадается</span> сразу</p>

<p><strong>Бекзод:</strong> <strong>сек</strong>, пишу ему</p>

<p><strong>Бекзод:</strong> Жасур, ты идёшь?</p>

<p>Жасур <span class="cn-word" data-pos="verb" data-tr="javob berdi">ответил</span> через минуту.</p>

<p><strong>Жасур:</strong> Да.</p>

<p>В чате <span class="cn-word" data-pos="verb" data-tr="jimlik boʻldi">стало тихо</span>.</p>

<p><strong>Афсона:</strong> ты чего? <span class="cn-word" data-pos="verb" data-tr="xafa boʻldingmi">обиделся</span>?</p>

<p><strong>Жасур:</strong> нет, а что?</p>

<p><strong>Афсона:</strong> ты написал «Да» с точкой</p>

<p><strong>Жасур:</strong> и что</p>

<p><strong>Катя:</strong> с точкой это как будто «да, отстаньте от меня»</p>

<p><strong>Бекзод:</strong> <span class="cn-word" data-tr="haqiqatan">серьёзно</span>, я тоже так <span class="cn-word" data-pos="verb" data-tr="oʻyladim">подумал</span></p>

<p>Жасур <span class="cn-word" data-pos="verb" data-tr="qayta oʻqidi">перечитал</span> свои <span class="cn-word" data-tr="xabarlar">сообщения</span>. Он всегда писал <span class="cn-word" data-tr="toʻgʻri">правильно</span>: с большой буквы, с точкой в конце. Его так <span class="cn-word" data-pos="verb" data-tr="oʻrgatishgan">учили</span>.</p>

<p><strong>Жасур:</strong> так меня в школе учили писать</p>

<p><strong>Катя:</strong> в <span class="cn-word" data-tr="insho">сочинении</span> да! а тут <span class="cn-word" data-tr="boshqa">другое</span></p>

<p><strong>Жасур:</strong> понял))</p>

<p><strong>Жасур:</strong> Да!!</p>

<p><strong>Афсона:</strong> вот теперь <span class="cn-word" data-tr="oʻzimizniki">свой</span> человек</p>

<p>В пятницу Дилноза <span class="cn-word" data-pos="verb" data-tr="kirdi">вошла</span> в кабинет 12 и <span class="cn-word" data-pos="verb" data-tr="toʻxtab qoldi">остановилась</span>. На столе стоял торт, под потолком висели шарики. Она <span class="cn-word" data-pos="verb" data-tr="hech narsa demadi">ничего не сказала</span>, только <span class="cn-word" data-pos="verb" data-tr="jilmaydi">улыбнулась</span>.</p>

<p>Вечером в чате появилось одно сообщение — от Дилнозы: «спасибо))))».</p>

<p>Четыре скобки. Никто не <span class="cn-word" data-pos="verb" data-tr="hisoblamadi">считал</span>, но все <span class="cn-word" data-pos="verb" data-tr="payqashdi">заметили</span>.</p>''',
        "questions": [
            {
                "text": "Nega chat birdan jimib qoldi?",
                "choices": [
                    "Jasur uzoq javob bermadi",
                    "Jasur «Да» soʻzidan keyin nuqta qoʻydi",
                    "Jasur kelmasligini aytdi",
                    "Internet uzilib qoldi"
                ],
                "answer": 1,
                "explanation": "«Ты написал „Да“ с точкой». Zamonaviy rus "
                               "yozishmasida qisqa javob oxiridagi nuqta sovuq "
                               "yoki xafa ohang beradi — hamma buni «отстаньте "
                               "от меня» deb tushundi.",
            },
            {
                "text": "Jasur nega bunday yozgan edi?",
                "choices": [
                    "U chindan ham xafa edi",
                    "U shoshib yozgan edi",
                    "Uni maktabda shunday — bosh harf va nuqta bilan — yozishga oʻrgatishgan",
                    "U qoidani bilmasdi"
                ],
                "answer": 2,
                "explanation": "«Он всегда писал правильно: с большой буквы, с "
                               "точкой в конце. Его так учили». Katya buni "
                               "aniqlashtiradi: «в сочинении да! а тут другое» "
                               "— insho boshqa, chat boshqa.",
            },
            {
                "text": "«Спс за идею))» dagi ikki qavs nima uchun qoʻyilgan?",
                "choices": [
                    "Bu yozuv xatosi",
                    "Bu gapning tugaganini bildiradi",
                    "Bu savol belgisi",
                    "Bu kulgi va iliqlik belgisi — chatda ohang shunday beriladi"
                ],
                "answer": 3,
                "explanation": "Chatda ovoz ham, yuz ham yoʻq. Shuning uchun "
                               "ohang «))», emoji va undov belgisi bilan "
                               "beriladi: <em>Спасибо))</em> — «katta rahmat».",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-93 — ish va oʻqish leksikasi                  HAYOT HIKOYASI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Первое собеседование",
        "summary": (
            "PR-93 matni. Shohruh birinchi ish suhbatiga boradi va bitta "
            "soʻzda adashadi — «сдавал» deydi, «сдал» oʻrniga. Suhbatdosh "
            "buni sezadi va unga kutilmagan savol beradi."
        ),
        "order":   93,
        "grammar": [
            {
                "pattern":  "сдавать ≠ сдать",
                "meaning":  "«Сдавал» — imtihon topshirdim (jarayon). "
                            "«Сдал» — imtihondan oʻtdim (natija). Hikoyaning "
                            "butun tugun shu bitta harfda.",
                "examples": ["Я сдавал экзамен. — natija nomaʼlum.",
                             "Я сдал экзамен. — oʻtdim."],
            },
            {
                "pattern":  "стать кем? — Творительный",
                "meaning":  "«Кем стать?» degan savol Творительный talab "
                            "qiladi: стать переводчиком, работать учителем.",
                "examples": ["Я хочу стать переводчиком.",
                             "Кем вы видите себя через пять лет?"],
            },
            {
                "pattern":  "Лексика собеседования",
                "meaning":  "Suhbat va rezyume soʻzlari: опыт работы, "
                            "навыки, должность, испытательный срок.",
                "examples": ["Расскажите о себе.",
                             "У меня небольшой опыт работы."],
            },
        ],
        "body": '''<p>Шохрух <span class="cn-word" data-pos="verb" data-tr="tugatdi">закончил</span> университет в июне и в июле пошёл на первое <span class="cn-word" data-tr="suhbat">собеседование</span>. Компания <span class="cn-word" data-pos="verb" data-tr="qidirardi">искала</span> переводчика с русского на узбекский.</p>

<p>Женщина напротив <span class="cn-word" data-pos="verb" data-tr="oʻqidi">прочитала</span> его <span class="cn-word" data-tr="rezyume">резюме</span> и сказала:</p>

<p>— Расскажите о себе.</p>

<p>Шохрух <span class="cn-word" data-pos="verb" data-tr="tayyorlangan edi">подготовился</span>. Он <span class="cn-word" data-pos="verb" data-tr="aytdi">рассказал</span> про университет, про <span class="cn-word" data-tr="amaliyot">практику</span>, про то, что два года <span class="cn-word" data-pos="verb" data-tr="shugʻullangan">занимался</span> переводами.</p>

<p>А потом добавил:</p>

<p>— И я <strong>сдавал</strong> государственный экзамен по русскому языку.</p>

<p>Женщина <span class="cn-word" data-pos="verb" data-tr="qaradi">посмотрела</span> на него и спросила:</p>

<p>— <strong>Сдавали</strong> или <strong>сдали</strong>?</p>

<p>Шохрух <span class="cn-word" data-pos="verb" data-tr="tushundi">понял</span> сразу. Он <span class="cn-word" data-pos="verb" data-tr="qizarib ketdi">покраснел</span>.</p>

<p>— <strong>Сдал</strong>. На «отлично».</p>

<p>— Вот и говорите «сдал», — сказала она <span class="cn-word" data-tr="tinch ovozda">спокойно</span>. — Одна буква, а <span class="cn-word" data-tr="butunlay boshqa">совсем другое</span> дело. «Сдавал» — это <span class="cn-word" data-tr="jarayon">процесс</span>. «Сдал» — <span class="cn-word" data-tr="natija">результат</span>. <span class="cn-word" data-tr="ish beruvchiga">Работодателю</span> нужен результат.</p>

<p>Потом она спросила про <span class="cn-word" data-tr="ish tajribasi">опыт работы</span>. Шохрух честно сказал, что опыт небольшой: только практика и <span class="cn-word" data-tr="buyurtmalar">заказы</span> для <span class="cn-word" data-tr="tanishlar">знакомых</span>.</p>

<p>— Это <span class="cn-word" data-tr="normal">нормально</span>, — сказала она. — Мне важно не <span class="cn-word" data-tr="qancha">сколько</span>, а <span class="cn-word" data-tr="nima aynan">что именно</span> вы делали. Вы сказали «занимался переводами». <span class="cn-word" data-tr="qanaqa">Какими</span>?</p>

<p>Шохрух <span class="cn-word" data-pos="verb" data-tr="aytdi">рассказал</span> про <span class="cn-word" data-tr="hujjatlar">документы</span>, про два <span class="cn-word" data-tr="sayt">сайта</span> и про <span class="cn-word" data-tr="qoʻllanma">инструкцию</span> к <span class="cn-word" data-tr="uskuna">оборудованию</span>. Женщина <span class="cn-word" data-pos="verb" data-tr="yozib oldi">записала</span>.</p>

<p>Дальше она спросила, кем он видит себя через пять лет. Шохрух ответил, что хотел бы <span class="cn-word" data-pos="verb" data-tr="boʻlmoq">стать</span> <span class="cn-word" data-tr="tahrirchi">редактором</span>.</p>

<p>Через неделю ему <span class="cn-word" data-pos="verb" data-tr="qoʻngʻiroq qilishdi">позвонили</span>. Его <span class="cn-word" data-pos="verb" data-tr="ishga olishdi">взяли</span> на <span class="cn-word" data-tr="sinov muddati">испытательный срок</span>.</p>

<p>Шохрух говорит, что на том собеседовании выучил <span class="cn-word" data-tr="asosiy dars">главный урок</span>: о себе надо говорить <span class="cn-word" data-tr="tugallangan feʼl bilan">совершенным видом</span>.</p>''',
        "questions": [
            {
                "text": "Nega suhbatdosh «Сдавали или сдали?» deb soʻradi?",
                "choices": [
                    "U Shohruhning gapini eshitmadi",
                    "U imtihon qachon boʻlganini bilmoqchi edi",
                    "«Сдавал» faqat jarayonni bildiradi — natija haqida hech narsa aytmaydi",
                    "U Shohruhni chalgʻitmoqchi edi"
                ],
                "answer": 2,
                "explanation": "«„Сдавал“ — это процесс. „Сдал“ — результат». "
                               "Shohruh «topshirdim» degan edi, «oʻtdim» "
                               "emas — shuning uchun savol tugʻildi.",
            },
            {
                "text": "«Хотел бы стать редактором» — nega «редактором», «редактор» emas?",
                "choices": [
                    "Chunki «стать» Творительный talab qiladi",
                    "Chunki bu koʻplik",
                    "Chunki «редактор» erkak jinsida",
                    "Chunki gap oʻtgan zamonda"
                ],
                "answer": 0,
                "explanation": "«Кем стать?» degan savol <strong>Творительный "
                               "падеж</strong> oladi (PR-40): <em>стать "
                               "редактором</em>, <em>работать "
                               "переводчиком</em>.",
            },
            {
                "text": "Shohruh oʻsha suhbatdan qanday xulosa chiqardi?",
                "choices": [
                    "Suhbatga tayyorlanish shart emas",
                    "Rezyume yozish kerak emas",
                    "Ish beruvchiga tajriba emas, diplom kerak",
                    "Oʻzi haqida gapirganda tugallangan feʼl ishlatish kerak"
                ],
                "answer": 3,
                "explanation": "«О себе надо говорить совершенным видом» — "
                               "yaʼni natijani koʻrsatadigan СВ bilan: "
                               "<em>сдал, поступил, закончил, организовал</em>.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-94 — frazeologizmlar                          ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Бить баклуши и другие загадки",
        "summary": (
            "PR-94 matni. Nega bekorchini «баклуши uruvchi» deyishadi va "
            "nega «burunga oʻyiq qilish» xotira bilan bogʻliq? Toʻrtta "
            "iboraning haqiqiy kelib chiqishi."
        ),
        "order":   94,
        "grammar": [
            {
                "pattern":  "Фразеологизм",
                "meaning":  "Maʼnosi qismlaridan chiqmaydigan turgʻun "
                            "birikma. Lugʻatdan butun holda qidiriladi.",
                "examples": ["бить баклуши — bekorchilik qilmoq",
                             "зарубить на носу — qattiq esda tutmoq"],
            },
            {
                "pattern":  "спустя рукава ↔ засучив рукава",
                "meaning":  "Bir-birining teskarisi va ikkalasi ham bitta "
                            "uzun yengdan chiqqan.",
                "examples": ["Он работал спустя рукава.",
                             "Он взялся за дело засучив рукава."],
            },
            {
                "pattern":  "водить за нос",
                "meaning":  "Aldab yurmoq. Yarmarkalarda ayiqlarni burniga "
                            "halqa oʻtkazib yetaklashardi.",
                "examples": ["Он водил нас за нос целый месяц."],
            },
        ],
        "body": '''<p>Про <span class="cn-word" data-tr="bekorchi">бездельника</span> по-русски говорят, что он <strong>бьёт баклуши</strong>. Слова понятные, а <span class="cn-word" data-tr="maʼno">смысл</span> — нет. Что такое баклуши и зачем их бить?</p>

<p><span class="cn-word" data-tr="javob">Ответ</span> простой. Раньше <span class="cn-word" data-tr="qoshiqlar">ложки</span> в России делали из дерева. <span class="cn-word" data-tr="birinchi navbatda">Сначала</span> от <span class="cn-word" data-tr="yogʻoch">бревна</span> <span class="cn-word" data-pos="verb" data-tr="yorishardi">откалывали</span> <span class="cn-word" data-tr="boʻlaklar">чурки</span> — вот их и называли <strong>баклушами</strong>. Работа была самая лёгкая, её <span class="cn-word" data-pos="verb" data-tr="ishonib topshirishardi">поручали</span> детям. Отсюда и <span class="cn-word" data-tr="maʼno">значение</span>: делать <span class="cn-word" data-tr="arzimas ish">пустяковое дело</span>.</p>

<p>Вторая <span class="cn-word" data-tr="jumboq">загадка</span> — <strong>зарубить на носу</strong>. Значит «<span class="cn-word" data-pos="verb" data-tr="qattiq eslab qolmoq">запомнить крепко</span>». Но при чём тут нос?</p>

<p>А ни при чём. Этот «нос» — не часть лица. Он от глагола <strong>носить</strong>. Когда люди не умели <span class="cn-word" data-pos="verb" data-tr="yozmoq">писать</span>, они носили с собой <span class="cn-word" data-tr="taxtacha">дощечку</span> и делали на ней <span class="cn-word" data-tr="oʻyiqlar">зарубки</span>: сколько взял, сколько <span class="cn-word" data-pos="verb" data-tr="qaytarish kerak">отдать</span>.</p>

<p>Третья история — про <span class="cn-word" data-tr="yenglar">рукава</span>. В старой русской одежде рукава были очень длинные. <span class="cn-word" data-pos="verb" data-tr="ishlash">Работать</span> с <span class="cn-word" data-pos="verb" data-tr="tushirilgan">опущенными</span> рукавами было <span class="cn-word" data-tr="mumkin emas">невозможно</span>.</p>

<p>Поэтому <strong>спустя рукава</strong> — это «<span class="cn-word" data-tr="beparvo">кое-как</span>», а <strong>засучив рукава</strong> — «<span class="cn-word" data-tr="jon-jahdi bilan">изо всех сил</span>». Два <span class="cn-word" data-tr="qarama-qarshi">противоположных</span> выражения из одного рукава.</p>

<p>И последнее: <strong>водить за нос</strong> — обманывать. На ярмарках <span class="cn-word" data-tr="ayiqlar">медведей</span> водили за <span class="cn-word" data-tr="halqa">кольцо</span> в носу. Медведь шёл туда, куда его вели.</p>

<p>Так что <span class="cn-word" data-tr="iboralar">фразеологизмы</span> не надо <span class="cn-word" data-pos="verb" data-tr="yodlash">зубрить</span>. У каждого есть своя история — а история <span class="cn-word" data-pos="verb" data-tr="esda qoladi">запоминается</span> сама.</p>''',
        "questions": [
            {
                "text": "Баклуши aslida nima edi?",
                "choices": [
                    "Yogʻoch qoshiqlar",
                    "Yogʻochdan yorib olingan boʻlaklar — qoshiq yasash uchun xomashyo",
                    "Bolalar oʻyinchogʻi",
                    "Bir turdagi asbob"
                ],
                "answer": 1,
                "explanation": "«От бревна откалывали чурки — вот их и называли "
                               "баклушами». Bu ish eng oson edi va bolalarga "
                               "topshirilardi — shundan «arzimas ish qilmoq» "
                               "maʼnosi chiqqan.",
            },
            {
                "text": "«Зарубить на носу» iborasidagi «нос» nimadan kelib chiqqan?",
                "choices": [
                    "«Нос» — yuzning bir qismi",
                    "«Нос» — kemaning old qismi",
                    "«Нос» — «носить» feʼlidan: oʻzi bilan olib yuriladigan taxtacha",
                    "«Нос» — pichoqning uchi"
                ],
                "answer": 2,
                "explanation": "«Этот „нос“ — не часть лица. Он от глагола "
                               "носить». Yozishni bilmagan odamlar taxtachani "
                               "olib yurib, unga oʻyiq qilishardi.",
            },
            {
                "text": "Nega «спустя рукава» va «засучив рукава» qarama-qarshi maʼno beradi?",
                "choices": [
                    "Chunki ular turli davrlarda paydo boʻlgan",
                    "Chunki eski kiyimning uzun yengi tushirilgan boʻlsa ishlab boʻlmasdi, shimarilgan boʻlsa — boʻlardi",
                    "Chunki birinchisi ayollar, ikkinchisi erkaklar haqida",
                    "Chunki ularning oʻzagi har xil"
                ],
                "answer": 1,
                "explanation": "«Работать с опущенными рукавами было "
                               "невозможно». Shuning uchun tushirilgan yeng — "
                               "beparvolik, shimarilgan yeng — jon-jahdi "
                               "bilan ish. Bitta yengdan ikki ibora.",
            },
        ],
    },
]
