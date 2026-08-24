# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-50 … PR-52.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 50 — yakuniy matn (bir kun), 51 — ilmiy-ommabop,
52 — kundalik hikoya (taʼmir). (47 oʻyin, 48 hikoya, 49 kalendar edi.)

Grammatika chegarasi (kumulyativ qoida):
  50-matn: kelishiklar blokining yakuni. Butun matn BITTA soʻz —
           «школа» — atrofida qurilgan va u oltita shaklda uchraydi.
           Vid hali YOʻQ: matn butunlay НСВ da.
  51-matn: vid haqidagi ilmiy-ommabop matn. Uning mavzusi aynan shu,
           shuning uchun ikkala vid ham misol sifatida keladi.
  52-matn: vid juftliklari amalda. Taʼmir mavzusi ideal: har bir ish
           avval JARAYON (НСВ), keyin NATIJA (СВ) boʻladi.

⚠️ 51-matnda oʻzbekcha soʻzlar KELTIRILMAYDI (matn tili — ruscha).
   Oʻzbekcha bilan solishtiruv `grammar` bloki va savollarda beriladi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_50_52.py --author=prime
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
    # PR-50 — kelishiklar yakuni                YAKUNIY MATN
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Один день, шесть падежей",
        "summary": (
            "PR-50 matni. Oddiy maktab kuni — lekin unda bitta soʻz oltita "
            "shaklda uchraydi. Matn oxirida oʻquvchi buni oʻzi sanab koʻradi."
        ),
        "order":   50,
        "grammar": [
            {
                "pattern":  "Bitta soʻz — oltita shakl",
                "meaning":  "школа · школы · школе · школу · школой · о школе. "
                            "Har bir shakl soʻzning gapdagi boshqa ishini "
                            "koʻrsatadi — xuddi oʻzbekchadagi maktab, maktabning, "
                            "maktabga, maktabni, maktabda, maktabdan kabi.",
                "examples": ["Я иду в школу.", "Я иду из школы."],
            },
            {
                "pattern":  "Predlog kelishikni tanlaydi",
                "meaning":  "в школу (В.п. — harakat), в школе (П.п. — joy), из "
                            "школы (Р.п.), к школе (Д.п.), за школой (Т.п.). "
                            "Predlog bor boʻlsa, u hal qiladi.",
                "examples": ["Дорога к школе идёт через парк.", "За школой стадион."],
            },
            {
                "pattern":  "Uch soʻz birga oʻzgaradi",
                "meaning":  "Egalik olmoshi, sifat va ot doim bitta guruh: «в нашей "
                            "старой школе». Otning kelishigini bilsangiz, qolgan "
                            "ikkitasi oʻz-oʻzidan chiqadi.",
                "examples": ["В нашей старой школе тепло."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Ertalab">Утром</span> я иду <strong>в школу</strong>.</p>

<p><span class="cn-word" data-tr="Yoʻl">Дорога</span> <strong>к школе</strong> идёт <span class="cn-word" data-tr="orqali">через</span> парк. Двадцать минут <span class="cn-word" data-tr="piyoda">пешком</span>.</p>

<p><strong>Школа</strong> — старое <span class="cn-word" data-tr="bino">здание</span>. Ей сто лет. <span class="cn-word" data-tr="Devorlar">Стены</span> <span class="cn-word" data-tr="qalin">толстые</span>, окна большие.</p>

<p><strong>В нашей старой школе</strong> зимой тепло, а летом <span class="cn-word" data-tr="salqin">прохладно</span>.</p>

<p><strong>За школой</strong> есть стадион. <span class="cn-word" data-tr="Darslardan keyin">После уроков</span> мы играем там в футбол.</p>

<p>В три часа я иду <strong>из школы</strong> домой. Уже по <span class="cn-word" data-tr="boshqa">другой</span> дороге — через рынок.</p>

<p>Вечером мама спрашивает:</p>

<p>— Что было <strong>в школе</strong>?</p>

<p>И я рассказываю <strong>о школе</strong>: об уроках, о друзьях, о футболе.</p>

<p>Один день. Одно слово. Шесть форм:</p>

<p><strong>школа · школы · школе · школу · школой · о школе</strong>.</p>

<p>Я не думаю об этом. Я просто иду в школу и говорю о школе.</p>

<p>И это — хороший <span class="cn-word" data-tr="belgi">знак</span>.</p>''',
        "questions": [
            {
                "text": "Matnning oxirgi jumlasi nega «yaxshi belgi» deb ataladi?",
                "choices": [
                    "Chunki kelishiklar haqida oʻylamay ishlatish — tilni bilish belgisi",
                    "Chunki maktab yaqin",
                    "Chunki ob-havo yaxshi",
                    "Chunki dars tugadi"
                ],
                "answer": 0,
                "explanation": "«Я не думаю об этом. Я просто иду в школу». "
                               "Yigirma ikki dars davomida kelishiklar qoida edi; "
                               "oxirida ular odat boʻlishi kerak. Oʻylamay ishlatish "
                               "— maqsadning oʻzi.",
            },
            {
                "text": "«В школу» va «в школе» — nega ikki xil shakl?",
                "choices": [
                    "Birinchisi harakat (qayerga), ikkinchisi joy (qayerda)",
                    "Birinchisi koʻplik",
                    "Birinchisi oʻtgan zamon",
                    "Ikkalasi bir xil"
                ],
                "answer": 0,
                "explanation": "Predlog В ikki kelishik oladi. «Иду в школу» — "
                               "harakat bor, demak Винительный. «Что было в "
                               "школе» — harakat yoʻq, demak Предложный.",
            },
            {
                "text": "«В нашей старой школе» — bu iborada nechta soʻz kelishikka "
                        "kirgan?",
                "choices": [
                    "Uchtasi: нашей, старой, школе",
                    "Bittasi: школе",
                    "Ikkitasi: старой va школе",
                    "Hech qaysi"
                ],
                "answer": 0,
                "explanation": "Egalik olmoshi, sifat va ot doim birga oʻzgaradi. "
                               "Bu yerda uchalasi ham Предложный padejida: -ЕЙ, -ОЙ, "
                               "-Е.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-51 — вид                                ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Читал и прочитал",
        "summary": (
            "PR-51 matni. Ikki soʻz, bitta oʻzak, bitta zamon — lekin maʼnosi "
            "boshqa. Rus tilidagi «вид» nima ekani va nega undan qochib "
            "boʻlmasligi haqida qisqa matn."
        ),
        "order":   51,
        "grammar": [
            {
                "pattern":  "НСВ — jarayon",
                "meaning":  "Что делать? — читать, писать, делать. Davomiylik, "
                            "takror, odat. Natija haqida hech narsa aytmaydi.",
                "examples": ["Я читал два часа.", "Каждый вечер я читаю."],
            },
            {
                "pattern":  "СВ — natija",
                "meaning":  "Что сделать? — прочитать, написать, сделать. Ish "
                            "tugadi. СВ da hozirgi zamon YOʻQ: прочитаю — bu kelasi "
                            "zamon.",
                "examples": ["Я прочитал книгу.", "Завтра я прочитаю её."],
            },
            {
                "pattern":  "Neytral shakl yoʻq",
                "meaning":  "Oʻzbekcha «oʻqidim» tugagan-tugamaganini aytmaydi — u "
                            "neytral. Ruschada bunday shakl yoʻq: har safar читал "
                            "yoki прочитал deb tanlash kerak. Vidni qiyin qiladigan "
                            "narsa — qoida emas, majburiy tanlov.",
                "examples": ["Ты читал? · Ты прочитал?"],
            },
        ],
        "body": '''<p>Два слова: <strong>читал</strong> и <strong>прочитал</strong>.</p>

<p>Один <span class="cn-word" data-tr="oʻzak">корень</span>. Одно время — прошедшее. Но <span class="cn-word" data-tr="maʼno">смысл</span> разный.</p>

<p><strong>Читал</strong> — это <span class="cn-word" data-tr="jarayon">процесс</span>. Я сидел и читал. Может быть, час. Может быть, весь вечер. Книга кончилась или нет — текст об этом молчит.</p>

<p><strong>Прочитал</strong> — это <span class="cn-word" data-tr="natija">результат</span>. Книга кончилась. Теперь я знаю её конец.</p>

<p>Поэтому два вопроса — это два разных вопроса.</p>

<p>«Ты <strong>читал</strong> эту книгу?» значит: ты <span class="cn-word" data-tr="tanishmisan">знаком</span> с ней?</p>

<p>«Ты <strong>прочитал</strong> эту книгу?» значит: ты закончил?</p>

<p>Можно ответить «да» на первый вопрос и «нет» на второй. Это не <span class="cn-word" data-tr="ziddiyat">противоречие</span>.</p>

<p>В <span class="cn-word" data-tr="oʻzbek tilida">узбекском языке</span> эта идея тоже есть. Но там она живёт <span class="cn-word" data-tr="yonida">рядом</span> с глаголом — это второе слово.</p>

<p>Русский язык делает другое: он <span class="cn-word" data-pos="verb" data-tr="qoʻyadi">кладёт</span> вид <strong>внутрь</strong> слова.</p>

<p>И вот самое важное. В русском языке нет <span class="cn-word" data-tr="neytral">нейтральной</span> формы.</p>

<p>Каждый раз нужно выбрать: процесс или результат. Всегда. Без исключений.</p>

<p>Это трудно. Но это и есть вид.</p>''',
        "questions": [
            {
                "text": "«Ты читал эту книгу?» va «Ты прочитал эту книгу?» — "
                        "bu ikki savol nima soʻraydi?",
                "choices": [
                    "Birinchisi: tanishmisan? Ikkinchisi: oxirigacha oʻqidingmi?",
                    "Ikkalasi bir xil narsani soʻraydi",
                    "Birinchisi kelasi zamon haqida",
                    "Ikkinchisi koʻplik haqida"
                ],
                "answer": 0,
                "explanation": "Matn buni aniq aytadi: birinchisi «знаком с ней?», "
                               "ikkinchisi «закончил?». Va birinchisiga «ha», "
                               "ikkinchisiga «yoʻq» deb javob berish mumkin — bu "
                               "ziddiyat emas.",
            },
            {
                "text": "Matnga koʻra rus tili va oʻzbek tili orasidagi asosiy farq "
                        "nima?",
                "choices": [
                    "Oʻzbekchada bu maʼno feʼl yonida, ruschada esa feʼl ichida yashaydi",
                    "Oʻzbekchada bunday tushuncha umuman yoʻq",
                    "Ruschada bu faqat oʻtgan zamonda ishlaydi",
                    "Oʻzbekchada bu faqat yozuvda ishlatiladi"
                ],
                "answer": 0,
                "explanation": "«Там она живёт рядом с глаголом — это второе "
                               "слово» (oʻqib CHIQDIM). «Русский язык кладёт вид "
                               "внутрь слова» (ПРОчитал). Bir xil gʻoya, ikki xil "
                               "joylashuv.",
            },
            {
                "text": "Nega matn vidni «qiyin» deb ataydi?",
                "choices": [
                    "Chunki ruschada neytral shakl yoʻq — har safar tanlash shart",
                    "Chunki juda koʻp qoida bor",
                    "Chunki shakllar bir-biriga oʻxshaydi",
                    "Chunki u faqat kitobiy tilda ishlatiladi"
                ],
                "answer": 0,
                "explanation": "«В русском языке нет нейтральной формы. Каждый "
                               "раз нужно выбрать». Oʻzbekcha «oʻqidim» hech narsa "
                               "vaʼda qilmaydi; ruscha esa har safar jarayon yoki "
                               "natijani tanlashga majbur qiladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-52 — vid juftliklari                    KUNDALIK HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ремонт на кухне",
        "summary": (
            "PR-52 matni. Bir oylik oshxona taʼmiri: har bir ish avval qilinadi, "
            "keyin qilib boʻlinadi. Buvining oxirgi gapi ikki vidning farqini "
            "bitta jumlada koʻrsatadi."
        ),
        "order":   52,
        "grammar": [
            {
                "pattern":  "Juftlik amalda: делали → сделали",
                "meaning":  "Bir xil ish ikki shaklda: НСВ jarayonni, СВ natijani "
                            "koʻrsatadi. Matnda har bir ish shu tartibda: avval "
                            "qilinadi, keyin qilib boʻlinadi.",
                "examples": ["Мы делали план три вечера.", "Потом мы сделали план."],
            },
            {
                "pattern":  "Prefiks bilan yasalgan juftliklar",
                "meaning":  "красить → покрасить, читать → прочитать, "
                            "делать → сделать. Qaysi prefiks kerakligini taxmin "
                            "qilib boʻlmaydi — juftlab yodlanadi.",
                "examples": ["Папа красил стены. Потом он покрасил их."],
            },
            {
                "pattern":  "выбирать → выбрать",
                "meaning":  "Bu yerda НСВ uzunroq — chunki u СВ dan suffiks bilan "
                            "yasalgan. Yoʻnalishga qarang: prefiks СВ tomonga, "
                            "suffiks НСВ tomonga.",
                "examples": ["Мама выбирала лампу неделю. Потом выбрала."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Bir oy oldin">Месяц назад</span> мы <strong>начали</strong> <span class="cn-word" data-tr="taʼmir">ремонт</span> на кухне.</p>

<p><span class="cn-word" data-tr="Avvaliga">Сначала</span> мы <strong>делали</strong> <span class="cn-word" data-tr="reja">план</span>. Долго. Три вечера.</p>

<p>Потом мы <strong>сделали</strong> план.</p>

<p>Папа <strong>красил</strong> <span class="cn-word" data-tr="devorlar">стены</span> два дня. На <span class="cn-word" data-tr="uchinchi">третий</span> день он <strong>покрасил</strong> их.</p>

<p>Мама <strong>выбирала</strong> <span class="cn-word" data-tr="chiroq">лампу</span> неделю. Она смотрела в <span class="cn-word" data-tr="internetda">интернете</span> каждый вечер. Потом <strong>выбрала</strong>.</p>

<p>Я <strong>читал</strong> <span class="cn-word" data-tr="qoʻllanma">инструкцию</span> к столу. Потом <strong>прочитал</strong> её ещё раз. Потом мы <strong>делали</strong> стол четыре часа.</p>

<p>Теперь стол стоит на кухне. Он немного <span class="cn-word" data-tr="qiyshiq">кривой</span>.</p>

<p>Бабушка <strong>смотрела</strong> на нас месяц. Она <span class="cn-word" data-pos="verb" data-tr="jim turdi">молчала</span>.</p>

<p>Вчера она <strong>посмотрела</strong> на кухню и сказала:</p>

<p>— Хорошо. Но стол кривой.</p>

<p>Папа сказал:</p>

<p>— Мы <strong>делали</strong> его четыре часа.</p>

<p>Бабушка сказала:</p>

<p>— Знаю. Но вы его не <strong>сделали</strong>.</p>''',
        "questions": [
            {
                "text": "Buvining oxirgi gapi nima demoqchi?",
                "choices": [
                    "Toʻrt soat ishladingiz, lekin stolni tugatmadingiz",
                    "Stolni umuman qilmadingiz",
                    "Stol juda tez qilindi",
                    "Stol yaxshi chiqdi"
                ],
                "answer": 0,
                "explanation": "«Мы делали его четыре часа» — jarayon bor edi "
                               "(НСВ). «Вы его не сделали» — natija yoʻq (СВ). Bitta "
                               "feʼl, ikkita shakl — va butun hazil aynan shu farqda.",
            },
            {
                "text": "Nega «выбирала» uzunroq, lekin «выбрала» — СВ?",
                "choices": [
                    "НСВ bu yerda СВ dan suffiks bilan yasalgan",
                    "Chunki «выбирала» koʻplik",
                    "Chunki uzun shakl har doim НСВ",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Yoʻnalishga qarang, uzunlikka emas: prefiks qoʻshilsa "
                               "— СВ tomonga (читать → ПРОчитать), suffiks qoʻshilsa "
                               "— НСВ tomonga (выбрать → выбирАТЬ).",
            },
            {
                "text": "Matnda har bir ish qanday tartibda tasvirlangan?",
                "choices": [
                    "Avval jarayon (НСВ), keyin natija (СВ)",
                    "Avval natija, keyin jarayon",
                    "Faqat natijalar sanalgan",
                    "Faqat jarayonlar sanalgan"
                ],
                "answer": 0,
                "explanation": "«делали план… сделали план», «красил… покрасил», "
                               "«выбирала… выбрала», «читал… прочитал». Taʼmir "
                               "mavzusi vid uchun ideal: har bir ish avval davom "
                               "etadi, keyin tugaydi.",
            },
        ],
    },
]
