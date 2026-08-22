# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-50 … PR-52.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 50 — yakuniy matn (bir kun), 51 — ilmiy-ommabop,
52 — kundalik hikoya (taʼmir). (47 oʻyin, 48 hikoya, 49 kalendar edi.)

Grammatika chegarasi (kumulyativ qoida):
  50-matn: kelishiklar blokining yakuni. Butun matn BITTA soʻz —
           «шко́ла» — atrofida qurilgan va u oltita shaklda uchraydi.
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
        "title":   "Оди́н день, шесть падеже́й",
        "summary": (
            "PR-50 matni. Oddiy maktab kuni — lekin unda bitta soʻz oltita "
            "shaklda uchraydi. Matn oxirida oʻquvchi buni oʻzi sanab koʻradi."
        ),
        "order":   50,
        "grammar": [
            {
                "pattern":  "Bitta soʻz — oltita shakl",
                "meaning":  "шко́ла · шко́лы · шко́ле · шко́лу · шко́лой · о шко́ле. "
                            "Har bir shakl soʻzning gapdagi boshqa ishini "
                            "koʻrsatadi — xuddi oʻzbekchadagi maktab, maktabning, "
                            "maktabga, maktabni, maktabda, maktabdan kabi.",
                "examples": ["Я иду́ в шко́лу.", "Я иду́ из шко́лы."],
            },
            {
                "pattern":  "Predlog kelishikni tanlaydi",
                "meaning":  "в шко́лу (В.п. — harakat), в шко́ле (П.п. — joy), из "
                            "шко́лы (Р.п.), к шко́ле (Д.п.), за шко́лой (Т.п.). "
                            "Predlog bor boʻlsa, u hal qiladi.",
                "examples": ["Доро́га к шко́ле идёт че́рез парк.", "За шко́лой стадио́н."],
            },
            {
                "pattern":  "Uch soʻz birga oʻzgaradi",
                "meaning":  "Egalik olmoshi, sifat va ot doim bitta guruh: «в на́шей "
                            "ста́рой шко́ле». Otning kelishigini bilsangiz, qolgan "
                            "ikkitasi oʻz-oʻzidan chiqadi.",
                "examples": ["В на́шей ста́рой шко́ле тепло́."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Ertalab">Утром</span> я иду́ <strong>в шко́лу</strong>.</p>

<p><span class="cn-word" data-tr="Yoʻl">Доро́га</span> <strong>к шко́ле</strong> идёт <span class="cn-word" data-tr="orqali">че́рез</span> парк. Два́дцать мину́т <span class="cn-word" data-tr="piyoda">пешко́м</span>.</p>

<p><strong>Шко́ла</strong> — ста́рое <span class="cn-word" data-tr="bino">зда́ние</span>. Ей сто лет. <span class="cn-word" data-tr="Devorlar">Сте́ны</span> <span class="cn-word" data-tr="qalin">то́лстые</span>, о́кна большие.</p>

<p><strong>В на́шей ста́рой шко́ле</strong> зимо́й тепло́, а ле́том <span class="cn-word" data-tr="salqin">прохла́дно</span>.</p>

<p><strong>За шко́лой</strong> есть стадио́н. <span class="cn-word" data-tr="Darslardan keyin">По́сле уро́ков</span> мы игра́ем там в футбо́л.</p>

<p>В три часа́ я иду́ <strong>из шко́лы</strong> домо́й. Уже́ по <span class="cn-word" data-tr="boshqa">друго́й</span> доро́ге — че́рез ры́нок.</p>

<p>Ве́чером ма́ма спра́шивает:</p>

<p>— Что бы́ло <strong>в шко́ле</strong>?</p>

<p>И я расска́зываю <strong>о шко́ле</strong>: об уро́ках, о друзья́х, о футбо́ле.</p>

<p>Оди́н день. Одно́ сло́во. Шесть форм:</p>

<p><strong>шко́ла · шко́лы · шко́ле · шко́лу · шко́лой · о шко́ле</strong>.</p>

<p>Я не ду́маю об э́том. Я про́сто иду́ в шко́лу и говорю́ о шко́ле.</p>

<p>И э́то — хоро́ший <span class="cn-word" data-tr="belgi">знак</span>.</p>''',
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
                "explanation": "«Я не ду́маю об э́том. Я про́сто иду́ в шко́лу». "
                               "Yigirma ikki dars davomida kelishiklar qoida edi; "
                               "oxirida ular odat boʻlishi kerak. Oʻylamay ishlatish "
                               "— maqsadning oʻzi.",
            },
            {
                "text": "«В шко́лу» va «в шко́ле» — nega ikki xil shakl?",
                "choices": [
                    "Birinchisi harakat (qayerga), ikkinchisi joy (qayerda)",
                    "Birinchisi koʻplik",
                    "Birinchisi oʻtgan zamon",
                    "Ikkalasi bir xil"
                ],
                "answer": 0,
                "explanation": "Predlog В ikki kelishik oladi. «Иду́ в шко́лу» — "
                               "harakat bor, demak Вини́тельный. «Что бы́ло в "
                               "шко́ле» — harakat yoʻq, demak Предло́жный.",
            },
            {
                "text": "«В на́шей ста́рой шко́ле» — bu iborada nechta soʻz kelishikka "
                        "kirgan?",
                "choices": [
                    "Uchtasi: на́шей, ста́рой, шко́ле",
                    "Bittasi: шко́ле",
                    "Ikkitasi: ста́рой va шко́ле",
                    "Hech qaysi"
                ],
                "answer": 0,
                "explanation": "Egalik olmoshi, sifat va ot doim birga oʻzgaradi. "
                               "Bu yerda uchalasi ham Предло́жный padejida: -ЕЙ, -ОЙ, "
                               "-Е.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-51 — вид                                ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Чита́л и прочита́л",
        "summary": (
            "PR-51 matni. Ikki soʻz, bitta oʻzak, bitta zamon — lekin maʼnosi "
            "boshqa. Rus tilidagi «вид» nima ekani va nega undan qochib "
            "boʻlmasligi haqida qisqa matn."
        ),
        "order":   51,
        "grammar": [
            {
                "pattern":  "НСВ — jarayon",
                "meaning":  "Что де́лать? — чита́ть, писа́ть, де́лать. Davomiylik, "
                            "takror, odat. Natija haqida hech narsa aytmaydi.",
                "examples": ["Я чита́л два часа́.", "Ка́ждый ве́чер я чита́ю."],
            },
            {
                "pattern":  "СВ — natija",
                "meaning":  "Что сде́лать? — прочита́ть, написа́ть, сде́лать. Ish "
                            "tugadi. СВ da hozirgi zamon YOʻQ: прочита́ю — bu kelasi "
                            "zamon.",
                "examples": ["Я прочита́л кни́гу.", "За́втра я прочита́ю её."],
            },
            {
                "pattern":  "Neytral shakl yoʻq",
                "meaning":  "Oʻzbekcha «oʻqidim» tugagan-tugamaganini aytmaydi — u "
                            "neytral. Ruschada bunday shakl yoʻq: har safar чита́л "
                            "yoki прочита́л deb tanlash kerak. Vidni qiyin qiladigan "
                            "narsa — qoida emas, majburiy tanlov.",
                "examples": ["Ты чита́л? · Ты прочита́л?"],
            },
        ],
        "body": '''<p>Два сло́ва: <strong>чита́л</strong> и <strong>прочита́л</strong>.</p>

<p>Оди́н <span class="cn-word" data-tr="oʻzak">ко́рень</span>. Одно́ вре́мя — проше́дшее. Но <span class="cn-word" data-tr="maʼno">смысл</span> ра́зный.</p>

<p><strong>Чита́л</strong> — э́то <span class="cn-word" data-tr="jarayon">проце́сс</span>. Я сиде́л и чита́л. Мо́жет быть, час. Мо́жет быть, весь ве́чер. Кни́га ко́нчилась и́ли нет — текст об э́том молчи́т.</p>

<p><strong>Прочита́л</strong> — э́то <span class="cn-word" data-tr="natija">результа́т</span>. Кни́га ко́нчилась. Тепе́рь я зна́ю её коне́ц.</p>

<p>Поэ́тому два вопро́са — э́то два ра́зных вопро́са.</p>

<p>«Ты <strong>чита́л</strong> э́ту кни́гу?» зна́чит: ты <span class="cn-word" data-tr="tanishmisan">знако́м</span> с ней?</p>

<p>«Ты <strong>прочита́л</strong> э́ту кни́гу?» зна́чит: ты зако́нчил?</p>

<p>Мо́жно отве́тить «да» на пе́рвый вопро́с и «нет» на второ́й. Э́то не <span class="cn-word" data-tr="ziddiyat">противоре́чие</span>.</p>

<p>В <span class="cn-word" data-tr="oʻzbek tilida">узбе́кском языке́</span> э́та иде́я то́же есть. Но там она́ живёт <span class="cn-word" data-tr="yonida">ря́дом</span> с глаго́лом — э́то второ́е сло́во.</p>

<p>Ру́сский язы́к де́лает друго́е: он <span class="cn-word" data-pos="verb" data-tr="qoʻyadi">кладёт</span> вид <strong>внутрь</strong> сло́ва.</p>

<p>И вот са́мое ва́жное. В ру́сском языке́ нет <span class="cn-word" data-tr="neytral">нейтра́льной</span> фо́рмы.</p>

<p>Ка́ждый раз ну́жно вы́брать: проце́сс и́ли результа́т. Всегда́. Без исключе́ний.</p>

<p>Э́то тру́дно. Но э́то и есть вид.</p>''',
        "questions": [
            {
                "text": "«Ты чита́л э́ту кни́гу?» va «Ты прочита́л э́ту кни́гу?» — "
                        "bu ikki savol nima soʻraydi?",
                "choices": [
                    "Birinchisi: tanishmisan? Ikkinchisi: oxirigacha oʻqidingmi?",
                    "Ikkalasi bir xil narsani soʻraydi",
                    "Birinchisi kelasi zamon haqida",
                    "Ikkinchisi koʻplik haqida"
                ],
                "answer": 0,
                "explanation": "Matn buni aniq aytadi: birinchisi «знако́м с ней?», "
                               "ikkinchisi «зако́нчил?». Va birinchisiga «ha», "
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
                "explanation": "«Там она́ живёт ря́дом с глаго́лом — э́то второ́е "
                               "сло́во» (oʻqib CHIQDIM). «Ру́сский язы́к кладёт вид "
                               "внутрь сло́ва» (ПРОчитал). Bir xil gʻoya, ikki xil "
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
                "explanation": "«В ру́сском языке́ нет нейтра́льной фо́рмы. Ка́ждый "
                               "раз ну́жно вы́брать». Oʻzbekcha «oʻqidim» hech narsa "
                               "vaʼda qilmaydi; ruscha esa har safar jarayon yoki "
                               "natijani tanlashga majbur qiladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-52 — vid juftliklari                    KUNDALIK HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ремо́нт на ку́хне",
        "summary": (
            "PR-52 matni. Bir oylik oshxona taʼmiri: har bir ish avval qilinadi, "
            "keyin qilib boʻlinadi. Buvining oxirgi gapi ikki vidning farqini "
            "bitta jumlada koʻrsatadi."
        ),
        "order":   52,
        "grammar": [
            {
                "pattern":  "Juftlik amalda: де́лали → сде́лали",
                "meaning":  "Bir xil ish ikki shaklda: НСВ jarayonni, СВ natijani "
                            "koʻrsatadi. Matnda har bir ish shu tartibda: avval "
                            "qilinadi, keyin qilib boʻlinadi.",
                "examples": ["Мы де́лали план три ве́чера.", "Пото́м мы сде́лали план."],
            },
            {
                "pattern":  "Prefiks bilan yasalgan juftliklar",
                "meaning":  "кра́сить → покра́сить, чита́ть → прочита́ть, "
                            "де́лать → сде́лать. Qaysi prefiks kerakligini taxmin "
                            "qilib boʻlmaydi — juftlab yodlanadi.",
                "examples": ["Па́па кра́сил сте́ны. Пото́м он покра́сил их."],
            },
            {
                "pattern":  "выбира́ть → вы́брать",
                "meaning":  "Bu yerda НСВ uzunroq — chunki u СВ dan suffiks bilan "
                            "yasalgan. Yoʻnalishga qarang: prefiks СВ tomonga, "
                            "suffiks НСВ tomonga.",
                "examples": ["Ма́ма выбира́ла ла́мпу неде́лю. Пото́м вы́брала."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Bir oy oldin">Ме́сяц наза́д</span> мы <strong>на́чали</strong> <span class="cn-word" data-tr="taʼmir">ремо́нт</span> на ку́хне.</p>

<p><span class="cn-word" data-tr="Avvaliga">Снача́ла</span> мы <strong>де́лали</strong> <span class="cn-word" data-tr="reja">план</span>. До́лго. Три ве́чера.</p>

<p>Пото́м мы <strong>сде́лали</strong> план.</p>

<p>Па́па <strong>кра́сил</strong> <span class="cn-word" data-tr="devorlar">сте́ны</span> два дня. На <span class="cn-word" data-tr="uchinchi">тре́тий</span> день он <strong>покра́сил</strong> их.</p>

<p>Ма́ма <strong>выбира́ла</strong> <span class="cn-word" data-tr="chiroq">ла́мпу</span> неде́лю. Она́ смотре́ла в <span class="cn-word" data-tr="internetda">интерне́те</span> ка́ждый ве́чер. Пото́м <strong>вы́брала</strong>.</p>

<p>Я <strong>чита́л</strong> <span class="cn-word" data-tr="qoʻllanma">инстру́кцию</span> к столу́. Пото́м <strong>прочита́л</strong> её ещё раз. Пото́м мы <strong>де́лали</strong> стол четы́ре часа́.</p>

<p>Тепе́рь стол стои́т на ку́хне. Он немно́го <span class="cn-word" data-tr="qiyshiq">криво́й</span>.</p>

<p>Бабушка <strong>смотре́ла</strong> на нас ме́сяц. Она́ <span class="cn-word" data-pos="verb" data-tr="jim turdi">молча́ла</span>.</p>

<p>Вчера́ она́ <strong>посмотре́ла</strong> на ку́хню и сказа́ла:</p>

<p>— Хорошо́. Но стол криво́й.</p>

<p>Па́па сказа́л:</p>

<p>— Мы <strong>де́лали</strong> его́ четы́ре часа́.</p>

<p>Бабушка сказа́ла:</p>

<p>— Зна́ю. Но вы его́ не <strong>сде́лали</strong>.</p>''',
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
                "explanation": "«Мы де́лали его́ четы́ре часа́» — jarayon bor edi "
                               "(НСВ). «Вы его́ не сде́лали» — natija yoʻq (СВ). Bitta "
                               "feʼl, ikkita shakl — va butun hazil aynan shu farqda.",
            },
            {
                "text": "Nega «выбира́ла» uzunroq, lekin «вы́брала» — СВ?",
                "choices": [
                    "НСВ bu yerda СВ dan suffiks bilan yasalgan",
                    "Chunki «выбира́ла» koʻplik",
                    "Chunki uzun shakl har doim НСВ",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Yoʻnalishga qarang, uzunlikka emas: prefiks qoʻshilsa "
                               "— СВ tomonga (чита́ть → ПРОчитать), suffiks qoʻshilsa "
                               "— НСВ tomonga (вы́брать → выбирАТЬ).",
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
                "explanation": "«де́лали план… сде́лали план», «кра́сил… покра́сил», "
                               "«выбира́ла… вы́брала», «чита́л… прочита́л». Taʼmir "
                               "mavzusi vid uchun ideal: har bir ish avval davom "
                               "etadi, keyin tugaydi.",
            },
        ],
    },
]
