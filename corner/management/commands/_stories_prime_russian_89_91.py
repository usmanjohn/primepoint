# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-89 … PR-91.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.
⛔ URGʻU BELGISI YOʻQ — 2026-08-24 dagi qaror.

Janr xilma-xilligi: 89 — ilmiy-ommabop (til haqida), 90 — ikki xat
(maktub-javob), 91 — kundalik hikoya (ichida haqiqiy ariza matni).

Grammatika chegarasi (kumulyativ qoida):
  89-matn: soʻz tartibi — bitta gap toʻrt xil tartibda, har biri
           boshqa savolga javob beradi; artiklsiz «oʻsha/bir» farqi.
  90-matn: uslub — bir voqea ikki xil kiyimda: doʻstga xat va
           rasmiy xat. PR-84/85/88 belgilarining hammasi birinchi
           xatda bor, ikkinchisida bittasi ham yoʻq.
  91-matn: ariza tili — shapkadagi Дательный va от+Родительный,
           «Прошу Вас…», «в связи с…», «С уважением».

⚠️ ATAY QOCHILGAN (keyingi darslar): chat va xabar tili (PR-92),
rezyume va suhbat leksikasi (PR-93), frazeologizmlar (PR-94),
maqollar (PR-95), punktuatsiya qoidalari (PR-97).

⚠️ FAKTLAR:
  89-matn — lingvistik faktlar. Rus tilida artikl yoʻqligi va uning
  vazifasini soʻz tartibi bajarishi — tilshunoslikda yaxshi maʼlum
  hodisa (актуальное членение предложения). Matndagi «Пришёл
  мальчик» / «Мальчик пришёл» qarama-qarshiligi darslikdagi klassik
  misol. Oʻzbek tilidagi «Xonada stol turardi» / «Stol xonada
  turardi» juftligi ham xuddi shu mantiqda ishlaydi.
  90 va 91 — toʻqima matnlar, real daʼvo yoʻq. 91-matndagi ariza
  namunasi rus maktab hujjatchiligining odatiy shakli.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_89_91.py --author=prime
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
    # PR-89 — soʻz tartibi                          ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Одно предложение, четыре смысла",
        "summary": (
            "PR-89 matni. Uch soʻzli bitta gap — toʻrt xil tartib, toʻrt xil "
            "maʼno. Rus tilida artikl yoʻq, uning oʻrniga soʻz tartibi "
            "ishlaydi; oʻzbek tilida ham xuddi shunday."
        ),
        "order":   89,
        "grammar": [
            {
                "pattern":  "Новое — в конце предложения",
                "meaning":  "Tanish narsa gap boshida, yangi narsa oxirida. "
                            "Eng muhim soʻz — oxirgi soʻz.",
                "examples": ["Книгу купил Жасур. — kim sotib oldi?",
                             "Жасур купил книгу. — nimani sotib oldi?"],
            },
            {
                "pattern":  "Порядок слов вместо артикля",
                "meaning":  "Rus tilida «the» ham, «a» ham yoʻq. Ega oxirda "
                            "boʻlsa — yangi narsa, boshida boʻlsa — tanish.",
                "examples": ["Пришёл мальчик. — bir bola keldi.",
                             "Мальчик пришёл. — oʻsha bola keldi."],
            },
            {
                "pattern":  "Не + inkor qilinayotgan soʻz",
                "meaning":  "«Не» oʻzidan keyingi soʻzni inkor qiladi. Uni "
                            "koʻchirsangiz, gapning maʼnosi oʻzgaradi.",
                "examples": ["Я не брал эту книгу.",
                             "Не я брал эту книгу."],
            },
        ],
        "body": '''<p>Возьмём три слова: <strong>Жасур</strong>, <strong>купил</strong>, <strong>книгу</strong>. Из них можно составить <span class="cn-word" data-tr="bir nechta">несколько</span> предложений, и все они будут <span class="cn-word" data-tr="toʻgʻri">правильными</span>. Но <span class="cn-word" data-tr="maʼno">смысл</span> у каждого будет свой.</p>

<p><strong>Жасур купил книгу.</strong> Это ответ на вопрос «что он купил?».</p>

<p><strong>Книгу купил Жасур.</strong> А это уже ответ на другой вопрос: «кто купил книгу?». Про книгу мы <span class="cn-word" data-pos="verb" data-tr="bilardik">знали</span> и раньше. Новое здесь — <span class="cn-word" data-tr="ism">имя</span>.</p>

<p><strong>Книгу Жасур купил вчера.</strong> Тут новое — <span class="cn-word" data-tr="vaqt">время</span>.</p>

<p>Правило простое: <span class="cn-word" data-tr="eng muhim">самое важное</span> слово русский язык ставит <strong>в конец</strong>. То, что <span class="cn-word" data-tr="allaqachon">уже</span> известно, идёт <span class="cn-word" data-tr="oldinda">впереди</span>.</p>

<p>У этого правила есть <span class="cn-word" data-tr="kutilmagan">неожиданное</span> применение.</p>

<p>В русском языке нет <span class="cn-word" data-tr="artikllar">артиклей</span>. В английском есть <em>the</em> и <em>a</em>, во французском тоже. А по-русски как <span class="cn-word" data-pos="verb" data-tr="ajratmoq">различить</span>, о каком мальчике идёт речь — о знакомом или о новом?</p>

<p><span class="cn-word" data-tr="tartib bilan">Порядком слов</span>.</p>

<p><strong>Пришёл мальчик</strong> — мальчик новый, мы слышим о нём <span class="cn-word" data-tr="birinchi marta">впервые</span>.</p>

<p><strong>Мальчик пришёл</strong> — мальчик знакомый, мы его <span class="cn-word" data-pos="verb" data-tr="kutardik">ждали</span>.</p>

<p>И ещё одно место, где порядок решает всё, — это <span class="cn-word" data-tr="inkor">отрицание</span>.</p>

<p><strong>Я не брал эту книгу</strong> — я её не брал, и всё.</p>

<p><strong>Не я брал эту книгу</strong> — книгу брали, но <span class="cn-word" data-tr="men emas">не я</span>. Частица <strong>не</strong> <span class="cn-word" data-pos="verb" data-tr="inkor qiladi">отрицает</span> то слово, которое стоит <span class="cn-word" data-tr="undan keyin">после неё</span>. <span class="cn-word" data-pos="verb" data-tr="koʻchiring">Передвиньте</span> её на одно слово — и <span class="cn-word" data-pos="verb" data-tr="oʻzgaradi">изменится</span> то, кто <span class="cn-word" data-tr="aybdor">виноват</span>.</p>

<p><span class="cn-word" data-tr="qiziq narsa">Интересно</span>, что узбекский язык <span class="cn-word" data-pos="verb" data-tr="hal qiladi">решает</span> эту задачу <span class="cn-word" data-tr="xuddi shunday">точно так же</span>. Артиклей в нём тоже нет, и порядок слов работает по тому же <span class="cn-word" data-tr="qoida">принципу</span>.</p>

<p>Так что <span class="cn-word" data-tr="erkinlik">свобода</span> русского порядка слов — это не <span class="cn-word" data-tr="tartibsizlik">беспорядок</span>. Это <span class="cn-word" data-tr="qurol">инструмент</span>.</p>''',
        "questions": [
            {
                "text": "Matnga koʻra, rus gapida eng muhim soʻz qayerda turadi?",
                "choices": [
                    "Gap boshida",
                    "Feʼldan oldin",
                    "Gap oxirida",
                    "Egadan keyin"
                ],
                "answer": 2,
                "explanation": "«Самое важное слово русский язык ставит в "
                               "конец. То, что уже известно, идёт впереди». "
                               "Shuning uchun <em>Книгу купил Жасур</em> «kim?» "
                               "degan savolga javob beradi.",
            },
            {
                "text": "«Пришёл мальчик» va «Мальчик пришёл» orasidagi farq nima?",
                "choices": [
                    "Birinchisi savol, ikkinchisi darak gap",
                    "Birinchisida bola yangi, ikkinchisida esa tanish",
                    "Birinchisi oʻtgan zamon, ikkinchisi hozirgi zamon",
                    "Farqi yoʻq, ikkalasi bir xil"
                ],
                "answer": 1,
                "explanation": "«Пришёл мальчик — мальчик новый… Мальчик пришёл "
                               "— мальчик знакомый, мы его ждали». Rus tilida "
                               "artikl yoʻq, shuning uchun bu farqni tartib "
                               "koʻrsatadi.",
            },
            {
                "text": "Matn oxiridagi «Это инструмент» degan xulosa nimani anglatadi?",
                "choices": [
                    "Rus tilini oʻrganish qiyin",
                    "Soʻz tartibini yodlash kerak",
                    "Erkin tartib — tartibsizlik emas, balki maʼnoni boshqarish vositasi",
                    "Rus tilida artikl kerak edi"
                ],
                "answer": 2,
                "explanation": "«Свобода русского порядка слов — это не "
                               "беспорядок. Это инструмент». Tartib erkin, "
                               "lekin bekorga emas: u har safar boshqa maʼno "
                               "beradi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-90 — uslub                                        IKKI XAT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Два письма об одном и том же",
        "summary": (
            "PR-90 matni. Nina konferensiyaga kech qoladi. U bir xil xabarni "
            "ikki marta yozadi — dugonasiga va rahbariga. Voqea bitta, matn "
            "esa butunlay boshqa."
        ),
        "order":   90,
        "grammar": [
            {
                "pattern":  "Разговорный стиль",
                "meaning":  "Norasmiy uslub belgilari: ты, yuklamalar (же, "
                            "ну, вот), qisqarishlar, kichraytirish.",
                "examples": ["Слушай, я застряла, вот беда!",
                             "Ну, до связи!"],
            },
            {
                "pattern":  "Официальный стиль",
                "meaning":  "Rasmiy uslub: Вы bosh harf bilan, «сообщаю», "
                            "«в связи с», «С уважением».",
                "examples": ["Уважаемый Олег Николаевич!",
                             "Сообщаю Вам, что задержусь."],
            },
            {
                "pattern":  "сообщить · в связи с · с уважением",
                "meaning":  "Rasmiy juftlar: сказать → сообщить, "
                            "из-за → в связи с. Rasmiy soʻz uzunroq boʻladi.",
                "examples": ["В связи с отменой рейса…",
                             "С уважением, Нина Соколова"],
            },
        ],
        "body": '''<p>Нина <span class="cn-word" data-pos="verb" data-tr="uchishi kerak edi">должна была лететь</span> на конференцию в понедельник утром. В воскресенье вечером её <span class="cn-word" data-tr="reys">рейс</span> <span class="cn-word" data-pos="verb" data-tr="bekor qilishdi">отменили</span>.</p>

<p>Нина написала два письма. Первое — <span class="cn-word" data-tr="dugonasiga">подруге</span> Кате, второе — руководителю Олегу Николаевичу.</p>

<p><strong>Первое письмо:</strong></p>

<p>«Кать, привет! Слушай, у меня тут <span class="cn-word" data-tr="baxtsizlik">беда</span>: рейс отменили, представляешь? Прямо вечером, <span class="cn-word" data-tr="hech qanday">безо всякого</span> <span class="cn-word" data-tr="ogohlantirish">предупреждения</span>. Я теперь <span class="cn-word" data-pos="verb" data-tr="tushaman">попадаю</span> только во вторник, и то <span class="cn-word" data-tr="agar">если</span> <span class="cn-word" data-tr="chiptalar">билеты</span> будут. Сидела в аэропорту два часа, потом поехала домой. Ну ладно, <span class="cn-word" data-pos="verb" data-tr="hal qilamiz">разберёмся</span>. Ты же знаешь, у меня всегда так: <span class="cn-word" data-tr="eng muhim kunda">в самый важный день</span> что-нибудь да <span class="cn-word" data-pos="verb" data-tr="sinadi">сломается</span>. Ты там <span class="cn-word" data-pos="verb" data-tr="yordam ber">прикрой</span>, если что спросят. Всё, побежала. До связи!»</p>

<p><strong>Второе письмо:</strong></p>

<p>«Уважаемый Олег Николаевич!</p>

<p>Сообщаю Вам, что не смогу прибыть на конференцию в понедельник, 16 марта, в связи с отменой рейса Ташкент — Москва.</p>

<p>В настоящее время я <span class="cn-word" data-pos="verb" data-tr="koʻrib chiqyapman">рассматриваю</span> <span class="cn-word" data-tr="variantlar">варианты</span> на вторник и сообщу Вам <span class="cn-word" data-tr="aniq">точное</span> время <span class="cn-word" data-tr="kelish">прибытия</span> сегодня до 18:00.</p>

<p>Прошу Вас <span class="cn-word" data-pos="verb" data-tr="koʻchirmoq">перенести</span> моё <span class="cn-word" data-tr="maʼruza">выступление</span> на вторник. Все <span class="cn-word" data-tr="materiallar">материалы</span> к докладу <span class="cn-word" data-pos="verb" data-tr="tayyorlangan">подготовлены</span> и будут <span class="cn-word" data-pos="verb" data-tr="yuborilgan">направлены</span> Вам заранее.</p>

<p>Заранее благодарю за понимание.</p>

<p>С уважением,<br>Нина Соколова»</p>

<p>Нина перечитала оба письма и <span class="cn-word" data-pos="verb" data-tr="jilmaydi">улыбнулась</span>. В первом было четыре <span class="cn-word" data-tr="undov belgisi">восклицательных знака</span>, во втором — ни одного. В первом она <span class="cn-word" data-pos="verb" data-tr="shikoyat qilardi">жаловалась</span>, во втором — <span class="cn-word" data-pos="verb" data-tr="taklif qilardi">предлагала</span> решение.</p>

<p>Одно событие. Один человек. Два <span class="cn-word" data-tr="butunlay boshqa">совершенно разных</span> текста — и оба правильные.</p>''',
        "questions": [
            {
                "text": "Nima uchun Nina bitta voqea haqida ikki xil xat yozdi?",
                "choices": [
                    "Chunki birinchi xatni yuborolmadi",
                    "Chunki oluvchilar har xil — dugonasi va rahbari",
                    "Chunki u ikki marta kech qoldi",
                    "Chunki rahbari birinchi xatni tushunmadi"
                ],
                "answer": 1,
                "explanation": "«Первое — подруге Кате, второе — руководителю "
                               "Олегу Николаевичу». Uslubni vaziyat va oluvchi "
                               "tanlaydi: bitta xabar, ikki xil kiyim.",
            },
            {
                "text": "Ikkinchi xatda birinchisidan farqli oʻlaroq nima YOʻQ?",
                "choices": [
                    "Kech qolish sababi",
                    "Imzo",
                    "Yuklamalar («ну», «вот»), qisqarishlar va murojaatning qisqa shakli",
                    "Rahbarning ismi"
                ],
                "answer": 2,
                "explanation": "Birinchi xatda «Кать», «ну ладно», «всё, "
                               "побежала» bor; ikkinchisida bittasi ham yoʻq. "
                               "Yuklama, qisqarish va kichraytirish — "
                               "norasmiylik belgilari (PR-84, PR-85, PR-88).",
            },
            {
                "text": "Nina rahbariga «из-за отмены рейса» emas, «в связи с отменой рейса» deb yozdi. Nega?",
                "choices": [
                    "Chunki «из-за» xato",
                    "Chunki «в связи с» rasmiy uslubning juftidir",
                    "Chunki reys bekor qilinmagan edi",
                    "Chunki «в связи с» qisqaroq"
                ],
                "answer": 1,
                "explanation": "<em>Из-за</em> — kundalik soʻz, <em>в связи "
                               "с</em> — uning rasmiy jufti. Eʼtibor bering, "
                               "kelishik ham oʻzgaradi: <em>из-за</em> "
                               "Родительный, <em>в связи с</em> esa "
                               "Творительный oladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-91 — ariza tili                             KUNDALIK HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Первое заявление Бекзода",
        "summary": (
            "PR-91 matni. Bekzod hayotidagi birinchi arizasini yozadi va uni "
            "uch marta qaytadan yozishga toʻgʻri keladi. Uchinchi urinishdan "
            "keyin ariza matni toʻliq keltirilgan."
        ),
        "order":   91,
        "grammar": [
            {
                "pattern":  "Шапка: кому? — Дательный",
                "meaning":  "Arizaning yuqori satri «kimga?» degan savolga "
                            "javob beradi. Oʻzbekcha -GA qoʻshimchasi.",
                "examples": ["Директору школы № 12",
                             "Ивановой Марине Петровне"],
            },
            {
                "pattern":  "Шапка: от кого? — от + Родительный",
                "meaning":  "Pastki satr «kimdan?» degan savolga javob "
                            "beradi. Oʻzbekcha -DAN qoʻshimchasi.",
                "examples": ["от ученика 9-А класса",
                             "от Умарова Бекзода"],
            },
            {
                "pattern":  "Прошу Вас… в связи с…",
                "meaning":  "Ariza matnining qolipi: «Прошу» + infinitiv, "
                            "keyin sabab «в связи с» bilan.",
                "examples": ["Прошу Вас разрешить мне не посещать занятия.",
                             "…в связи с участием в олимпиаде."],
            },
        ],
        "body": '''<p>Бекзод <span class="cn-word" data-pos="verb" data-tr="oʻtdi">прошёл</span> на областную олимпиаду по русскому языку. Олимпиада была в четверг, а в четверг у него уроки.</p>

<p><span class="cn-word" data-tr="sinf rahbari">Классный руководитель</span> сказала коротко: «Пиши заявление».</p>

<p>Бекзод никогда не писал заявлений. Он взял лист и написал: «Здравствуйте! Я хочу пойти на олимпиаду в четверг. Бекзод».</p>

<p>Учительница <span class="cn-word" data-pos="verb" data-tr="oʻqidi">прочитала</span> и вернула лист. «Это <span class="cn-word" data-tr="xat">записка</span>, а не заявление. У заявления есть <span class="cn-word" data-tr="shakl">форма</span>».</p>

<p>Дома старшая сестра Дилноза <span class="cn-word" data-pos="verb" data-tr="tushuntirdi">объяснила</span> ему <span class="cn-word" data-tr="asosiysini">главное</span>.</p>

<p>— <span class="cn-word" data-tr="tepada">Наверху</span> справа две строки. Первая — <span class="cn-word" data-tr="kimga">кому</span>. Вторая — <span class="cn-word" data-tr="kimdan">от кого</span>. И это <span class="cn-word" data-tr="turli kelishiklar">разные падежи</span>.</p>

<p>— Почему разные?</p>

<p>— <span class="cn-word" data-pos="verb" data-tr="oʻylab koʻr">Подумай</span> по-узбекски. Ты пишешь «direktor<strong>ga</strong>» и «Bekzod<strong>dan</strong>». Два разных <span class="cn-word" data-tr="qoʻshimcha">окончания</span>, правда? В русском то же самое.</p>

<p>— И ещё, — добавила Дилноза. — В заявлении не пишут «я хочу». Пишут «прошу». Это не <span class="cn-word" data-tr="xohish">желание</span>, это <span class="cn-word" data-tr="soʻrov">просьба</span>.</p>

<p>Бекзод <span class="cn-word" data-pos="verb" data-tr="tushundi">понял</span> и написал <span class="cn-word" data-tr="uchinchi marta">в третий раз</span>:</p>

<p>«Директору школы № 12<br>Ивановой М. П.<br>от ученика 9-А класса<br>Умарова Бекзода</p>

<p><strong>Заявление</strong></p>

<p>Прошу Вас разрешить мне не посещать занятия 19 марта 2026 года в связи с участием в областной олимпиаде по русскому языку.</p>

<p>16.03.2026 &nbsp;&nbsp; Умаров»</p>

<p>Учительница прочитала, <span class="cn-word" data-pos="verb" data-tr="bosh irgʻadi">кивнула</span> и <span class="cn-word" data-pos="verb" data-tr="imzoladi">подписала</span>.</p>

<p>— Вот теперь заявление, — сказала она. — <span class="cn-word" data-pos="verb" data-tr="saqlab qoʻy">Сохрани</span> этот лист. Ты будешь писать такие всю жизнь.</p>''',
        "questions": [
            {
                "text": "Nega oʻqituvchi Bekzodning birinchi matnini qaytardi?",
                "choices": [
                    "Chunki unda xatolar bor edi",
                    "Chunki bu xatcha edi, arizaning shakli esa boshqa",
                    "Chunki Bekzod olimpiadaga oʻtmagan edi",
                    "Chunki u qoʻlda yozilgan edi"
                ],
                "answer": 1,
                "explanation": "«Это записка, а не заявление. У заявления есть "
                               "форма». Arizada ijod kerak emas — qolip kerak: "
                               "shapka, sarlavha, «Прошу», sana va imzo.",
            },
            {
                "text": "Dilnoza shapkadagi ikki kelishikni qanday tushuntirdi?",
                "choices": [
                    "Ularni yodlash kerakligini aytdi",
                    "Lugʻatdan qarashni maslahat berdi",
                    "Oʻzbekcha «direktorga» va «Bekzoddan» bilan taqqosladi",
                    "Ularning farqi yoʻqligini aytdi"
                ],
                "answer": 2,
                "explanation": "«Ты пишешь „direktorga“ и „Bekzoddan“. Два "
                               "разных окончания, правда? В русском то же "
                               "самое». Oʻzbekcha -GA = Дательный, -DAN = "
                               "от + Родительный.",
            },
            {
                "text": "Uchinchi variantda «Прошу Вас разрешить…» deb yozilgan. Birinchi variantdan farqi nimada?",
                "choices": [
                    "Uzunroq yozilgan",
                    "Xohish emas, soʻrov bildirilgan — arizaning qolipi shu",
                    "Sana qoʻshilgan",
                    "Oʻqituvchining ismi yozilgan"
                ],
                "answer": 1,
                "explanation": "Birinchi variantda «Я хочу пойти» — xohish. "
                               "Arizada esa har doim «Прошу» + infinitiv "
                               "boʻladi: «Прошу Вас разрешить мне не посещать "
                               "занятия».",
            },
        ],
    },
]
