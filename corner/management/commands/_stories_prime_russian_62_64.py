# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-62 … PR-64.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 62 — ilmiy-ommabop (til haqida), 63 — mahalla portreti
(hikoya), 64 — kichik voqea + xulosa. (59 qoʻllanma, 60 xat, 61 tarix edi —
demak uchta bir xil shakl ketma-ket kelmayapti.)

Grammatika chegarasi (kumulyativ qoida):
  62-matn: -ся ning oltita maʼnosi. ⚠️ КОТО́РЫЙ bu matnda ATAY yoʻq —
           u faqat PR-63 da oʻrgatiladi, matn esa PR-62 ники.
  63-matn: который. Beshta kelishikda va predlog bilan: кото́рого,
           кото́рый, у кото́рого, к кото́рому, с кото́рым, в кото́ром.
  64-matn: что va что́бы yonma-yon. Xat janri emas, xat HAQIDA voqea —
           shuning uchun «хоте́л, что́бы…» va «ду́мал, что…» tabiiy
           ravishda bir matnga sigʻadi.

⚠️ FAKTLAR: 62-matndagi oʻzbek tili haqidagi daʼvo tekshirilgan —
oʻzbekchada -in- (oʻzlik), -ish- (birgalik) va -il- (majhul) uchta
alohida qoʻshimcha, ruschada esa bularning hammasi bitta -ся.
63 va 64 — toʻqima voqealar, real daʼvo yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_62_64.py --author=prime
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
    # PR-62 — -ся                                ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Шесть значе́ний одно́й ча́стицы",
        "summary": (
            "PR-62 matni. Ikki harf — «-ся» — va uning oltita vazifasi, "
            "bittadan misol bilan. Oxirida oʻzbek tili bilan solishtirish: "
            "bizda uchta qoʻshimcha, ruschada bitta."
        ),
        "order":   62,
        "grammar": [
            {
                "pattern":  "-ся ning oltita maʼnosi",
                "meaning":  "Oʻziga qaytish (мо́ется), bir-biriga (встреча́ются), "
                            "majhul nisbat (стро́ится), holat (спи́тся), faqat -ся "
                            "bilan yashaydigan feʼllar (смея́ться) va maʼno "
                            "oʻzgarishi (учи́ть → учи́ться).",
                "examples": ["Он мо́ется.", "Они́ встреча́ются."],
            },
            {
                "pattern":  "-ся feʼli obyekt olmaydi",
                "meaning":  "Он мо́ет маши́ну (obyekt bor) ↔ он мо́ется (obyekt "
                            "yoʻq). Matnning ikkinchi bandi shu farq ustiga "
                            "qurilgan.",
                "examples": ["Он мо́ет маши́ну.", "Он мо́ется."],
            },
            {
                "pattern":  "-ся ↔ oʻzbekcha -in-, -ish-, -il-",
                "meaning":  "Oʻzbekchada uchta alohida qoʻshimcha bor, ruschada "
                            "esa bitta. Shuning uchun oʻzbek oʻquvchisi bu "
                            "maʼnolarni rus bolasidan koʻra aniqroq ajratadi.",
                "examples": ["yuvinmoq → мы́ться", "koʻrishmoq → встреча́ться"],
            },
        ],
        "body": '''<p>В ру́сском языке́ есть о́чень коро́ткая <span class="cn-word" data-tr="qoʻshimcha, zarracha">ча́стица</span> — <strong>-ся</strong>. Две бу́квы. Но рабо́т у неё шесть.</p>

<p><strong>Пе́рвая рабо́та.</strong> Челове́к де́лает что́-то с собо́й. «Он мо́ет маши́ну» — здесь есть <span class="cn-word" data-tr="obyekt">объе́кт</span>. «Он <strong>мо́ется</strong>» — объе́кта нет, потому́ что объе́кт — сам челове́к.</p>

<p><strong>Втора́я.</strong> Лю́ди де́лают что́-то друг дру́гу. Они́ <strong>встреча́ются</strong> в суббо́ту. Они́ <strong>ссо́рятся</strong>, а пото́м <strong>мирятся</strong>. Оди́н челове́к так не мо́жет — ну́жно как ми́нимум дво́е.</p>

<p><strong>Тре́тья.</strong> Кто де́лал — <span class="cn-word" data-tr="nomaʼlum">неизве́стно</span> и́ли не ва́жно. Дом <strong>стро́ится</strong>. Магази́н <strong>открыва́ется</strong> в де́вять. Кто и́менно открыва́ет дверь, мы не говори́м.</p>

<p><strong>Четвёртая.</strong> <span class="cn-word" data-tr="holat">Состоя́ние</span>. «Мне не <strong>спи́тся</strong>». «Мне <strong>хо́чется</strong> ча́я». Здесь никто́ не де́йствует. Есть то́лько челове́к и его́ состоя́ние.</p>

<p><strong>Пя́тая.</strong> Есть глаго́лы, <span class="cn-word" data-tr="faqat">то́лько</span> с -ся. <strong>Смея́ться. Боя́ться. Наде́яться. Улыба́ться.</strong> Сло́ва «смеять» в ру́сском языке́ про́сто нет.</p>

<p><strong>Шеста́я.</strong> Значе́ние <span class="cn-word" data-pos="verb" data-tr="oʻzgaradi">меня́ется</span>. <strong>Учи́ть</strong> — так де́лает учи́тель. <strong>Учи́ться</strong> — так де́лает <span class="cn-word" data-tr="oʻquvchi">учени́к</span>. Две бу́квы, и де́йствие пошло́ в другу́ю сто́рону.</p>

<p>Тепе́рь <span class="cn-word" data-tr="eng qizigʻi">са́мое интере́сное</span>. В узбе́кском языке́ для э́тих значе́ний есть <strong>три</strong> ра́зных су́ффикса: оди́н для <span class="cn-word" data-tr="birinchi">пе́рвого</span> значе́ния, друго́й для второ́го, тре́тий для тре́тьего.</p>

<p>Ру́сский язы́к в э́том ме́сте <span class="cn-word" data-tr="tejamkor">эконо́мный</span>. Узбе́кский — <span class="cn-word" data-tr="aniqroq">точне́е</span>.</p>

<p>Поэ́тому для вас э́та те́ма не тру́дная. Вы уже́ зна́ете <span class="cn-word" data-tr="farqni">ра́зницу</span> — вам ну́жно то́лько запо́мнить, что здесь она́ пи́шется одина́ково.</p>''',
        "questions": [
            {
                "text": "Nega «Он мо́ется» gapida obyekt yoʻq?",
                "choices": [
                    "Chunki obyekt — odamning oʻzi",
                    "Chunki bu majhul nisbat",
                    "Chunki feʼl -ся bilan tugaydi va bu tasodifiy",
                    "Chunki gap toʻliq emas"
                ],
                "answer": 0,
                "explanation": "Matn buni ochiq aytadi: «объе́кт — сам челове́к». "
                               "Bu -ся ning birinchi maʼnosi, oʻzbekcha "
                               "«yuvinmoq» dagi -in- bilan bir xil.",
            },
            {
                "text": "Matnga koʻra, «смеять» soʻzi haqida nima toʻgʻri?",
                "choices": [
                    "Bunday soʻz rus tilida umuman yoʻq",
                    "U eskirgan soʻz",
                    "U faqat kitobiy tilda ishlatiladi",
                    "U «смея́ться» ning buyruq shakli"
                ],
                "answer": 0,
                "explanation": "«Сло́ва „смеять“ в ру́сском языке́ про́сто нет». Bu "
                               "beshinchi guruh — -ся siz yashamaydigan feʼllar.",
            },
            {
                "text": "Matnning oxirgi xulosasi nima?",
                "choices": [
                    "Oʻzbek tili farqlarni aniqroq koʻrsatadi, shuning uchun bu mavzu oʻzbek oʻquvchisi uchun qiyin emas",
                    "Rus tili oʻzbek tilidan qiyinroq",
                    "Oʻzbek tilida -ся ga oʻxshash qoʻshimcha yoʻq",
                    "Bu maʼnolarni yodlashning imkoni yoʻq"
                ],
                "answer": 0,
                "explanation": "«Ру́сский язы́к эконо́мный. Узбе́кский — точне́е… вам "
                               "ну́жно то́лько запо́мнить, что здесь она́ пи́шется "
                               "одина́ково».",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-63 — который                            MAHALLA PORTRETI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Челове́к, кото́рый чини́л всё",
        "summary": (
            "PR-63 matni. Hovlida hamma taniydigan usta Shavkat-aka: u pul "
            "olmagan, lekin har kim undan biror narsa oʻrgangan. Koʻchib "
            "ketgach, hovli nima qilganini koʻrsatadigan hikoya."
        ),
        "order":   63,
        "grammar": [
            {
                "pattern":  "который — jins va son otdan",
                "meaning":  "Aniqlanayotgan ot erkak boʻlsa кото́рый, ayol boʻlsa "
                            "кото́рая, koʻplik boʻlsa кото́рые. Matnda uchalasi "
                            "ham bor.",
                "examples": ["челове́к, кото́рого зна́ли все",
                             "дверь, кото́рая не закрыва́лась"],
            },
            {
                "pattern":  "который — kelishik oʻz gapidan",
                "meaning":  "Кото́рого (koʻrdilar — kimni?), кото́рому (bordilar — "
                            "kimga?), кото́рым (bogʻlangan — kim bilan?). Kelishik "
                            "ergash gapdagi vazifaga qarab tanlanadi.",
                "examples": ["сосе́д, кото́рому все звони́ли",
                             "ма́стер, кото́рым горди́лся весь двор"],
            },
            {
                "pattern":  "Predlog кото́рый dan oldin",
                "meaning":  "У кото́рого, в кото́ром, с кото́рым — predlog ergash "
                            "gap oxirida qolmaydi, u кото́рый bilan birga oldinga "
                            "koʻchadi. Vergul esa predlogdan oldin qoʻyiladi.",
                "examples": ["дом, в кото́ром он жил", "стари́к, у кото́рого был ключ"],
            },
        ],
        "body": '''<p>В на́шем дворе́ жил челове́к, <strong>кото́рого</strong> зна́ли все. Его́ зва́ли Шавка́т-ака́.</p>

<p>Шавка́т-ака́ был <span class="cn-word" data-tr="usta">ма́стер</span>. Не тот ма́стер, <strong>кото́рый</strong> рабо́тает в мастерско́й и берёт де́ньги. Друго́й. Он про́сто чини́л <span class="cn-word" data-tr="narsalar">ве́щи</span>, <strong>кото́рые</strong> <span class="cn-word" data-pos="verb" data-tr="buzilardi">лома́лись</span> во дворе́.</p>

<p>Дверь, <strong>кото́рая</strong> не закрыва́лась. <span class="cn-word" data-tr="Kran">Кран</span>, <strong>кото́рый</strong> <span class="cn-word" data-pos="verb" data-tr="tomchilardi">ка́пал</span>. Велосипе́д, <strong>у кото́рого</strong> сло́малась цепь. Ла́мпа в подъе́зде, <strong>в кото́ром</strong> всегда́ бы́ло темно́.</p>

<p>Он был <span class="cn-word" data-tr="qoʻshni">сосе́д</span>, <strong>кото́рому</strong> звони́ли пе́рвым. И он всегда́ приходи́л.</p>

<p>Де́нег Шавка́т-ака́ не брал. Совсе́м. Но у него́ бы́ло одно́ <span class="cn-word" data-tr="shart">усло́вие</span>: челове́к, <strong>кото́рому</strong> он помога́л, до́лжен был стоя́ть ря́дом и <span class="cn-word" data-pos="verb" data-tr="qaramoq">смотре́ть</span>.</p>

<p>— Смотри́, — говори́л он. — В сле́дующий раз сде́лаешь сам.</p>

<p>Жасу́р, <strong>кото́рый</strong> жил на тре́тьем этаже́, так научи́лся чини́ть кран. Дилно́за, <strong>кото́рая</strong> учи́лась в шко́ле, так научи́лась <span class="cn-word" data-pos="verb" data-tr="almashtirmoq">меня́ть</span> ла́мпу. Ро́за Кари́мовна, <strong>кото́рой</strong> бы́ло се́мьдесят два го́да, так научи́лась <span class="cn-word" data-pos="verb" data-tr="ulamoq">клеить</span> ме́бель.</p>

<p>В про́шлом году́ Шавка́т-ака́ уе́хал к до́чери в друго́й го́род.</p>

<p>Пе́рвую неде́лю двор ждал. Все ду́мали, что тепе́рь всё <span class="cn-word" data-pos="verb" data-tr="buziladi">слома́ется</span> и <span class="cn-word" data-pos="verb" data-tr="qoladi">оста́нется</span> сло́манным.</p>

<p>Но во втору́ю неде́лю Жасу́р почини́л кран у Ни́ны Петро́вны. Дилно́за <span class="cn-word" data-pos="verb" data-tr="almashtirdi">поменя́ла</span> ла́мпу в подъе́зде. А Ро́за Кари́мовна <span class="cn-word" data-pos="verb" data-tr="tuzatdi">почини́ла</span> стул, <strong>на кото́ром</strong> сиде́ла три́дцать лет.</p>

<p>Ма́стер, <strong>кото́рым</strong> горди́лся весь двор, уе́хал. А двор оста́лся с рука́ми.</p>

<p>Э́то и был его́ настоя́щий <span class="cn-word" data-tr="ish, mehnat">труд</span>.</p>''',
        "questions": [
            {
                "text": "Shavkat-akaning yagona sharti nima edi?",
                "choices": [
                    "U yordam bergan odam yonida turib qarab tursin",
                    "Ish haqi kichik boʻlsa ham toʻlansin",
                    "Uni oldindan telefon qilib chaqirishsin",
                    "Asboblarni qoʻshni bersin"
                ],
                "answer": 0,
                "explanation": "«Челове́к, кото́рому он помога́л, до́лжен был стоя́ть ря́дом и "
                               "смотре́ть». Va sababi keyingi qatorda: «В "
                               "сле́дующий раз сде́лаешь сам».",
            },
            {
                "text": "Nima uchun matnda «у кото́рого сло́малась цепь» deyilgan, «кото́рого» emas?",
                "choices": [
                    "Predlog «у» кото́рый bilan birga oldinga koʻchadi",
                    "Chunki velosiped jonsiz",
                    "Chunki bu koʻplik shakli",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Rus tilida predlog ergash gap oxirida qolmaydi — u "
                               "кото́рый bilan birga keladi. Vergul esa "
                               "predlogdan oldin qoʻyiladi.",
            },
            {
                "text": "Shavkat-aka ketgandan keyin hovlida nima boʻldi?",
                "choices": [
                    "Qoʻshnilar buzilgan narsalarni oʻzlari tuzata boshladi",
                    "Hovli yangi usta yolladi",
                    "Hech kim hech narsani tuzatmadi",
                    "Shavkat-aka har hafta qaytib kelib turdi"
                ],
                "answer": 0,
                "explanation": "Jasur kranni, Dilnoza lampani, Roza Karimovna esa "
                               "stulni tuzatdi — «двор оста́лся с рука́ми».",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-64 — что / чтобы                        KICHIK VOQEA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Что́бы тебя́ по́няли",
        "summary": (
            "PR-64 matni. Jasur maktab direktoriga xat yozadi va javob "
            "olmaydi. Sergey Petrovich xatni qayta yozdirmaydi — faqat uchta "
            "savol beradi."
        ),
        "order":   64,
        "grammar": [
            {
                "pattern":  "что — fakt",
                "meaning":  "Знать, ду́мать, ви́деть, понима́ть feʼllaridan keyin "
                            "«что» keladi: bu axborot, sodir boʻlgan yoki "
                            "boʻladigan narsa.",
                "examples": ["Он ду́мал, что письмо́ хоро́шее.",
                             "Тепе́рь я зна́ю, что письмо́ бы́ло плохо́е."],
            },
            {
                "pattern":  "чтобы + oʻtgan zamon (ega boshqa)",
                "meaning":  "Хоте́ть, проси́ть, ну́жно feʼllaridan keyin «что́бы», "
                            "va undan keyingi feʼl oʻtgan zamonda boʻladi — bu "
                            "oʻtmish emas, shunchaki shakl.",
                "examples": ["Он хоте́л, что́бы дире́ктор отве́тил.",
                             "Ну́жно, что́бы тебя́ по́няли."],
            },
            {
                "pattern":  "чтобы + infinitiv (ega bir xil)",
                "meaning":  "Ikkala qismda ham ega bitta boʻlsa, «что́бы» dan keyin "
                            "infinitiv qoʻyiladi — oʻzbekcha «-sh uchun».",
                "examples": ["Он написа́л письмо́, что́бы попроси́ть но́вые мячи́.",
                             "Пиши́, что́бы тебя́ по́няли."],
            },
        ],
        "body": '''<p>Жасу́р написа́л письмо́ <span class="cn-word" data-tr="direktorga">дире́ктору</span> шко́лы. Он написа́л его́, <strong>что́бы попроси́ть</strong> но́вые мячи́ для спортза́ла. Ста́рые мячи́ уже́ не <span class="cn-word" data-pos="verb" data-tr="sakramas edi">пры́гали</span> — они́ ста́ли <span class="cn-word" data-tr="yumshoq">мя́гкими</span>.</p>

<p>Он ду́мал, <strong>что</strong> письмо́ хоро́шее. Оно́ бы́ло дли́нное — две <span class="cn-word" data-tr="sahifa">страни́цы</span>.</p>

<p>Он хоте́л, <strong>что́бы дире́ктор отве́тил</strong> бы́стро.</p>

<p>Дире́ктор не отве́тил. Ни че́рез неде́лю, ни че́рез две.</p>

<p>Тогда́ Жасу́р пошёл к Серге́ю Петро́вичу — учи́телю, кото́рый вёл у них ру́сский язы́к.</p>

<p>— Прочита́йте, пожа́луйста. Я хочу́, <strong>что́бы вы сказа́ли</strong>, где оши́бка.</p>

<p>Серге́й Петро́вич прочита́л письмо́ два ра́за. Пото́м он <span class="cn-word" data-pos="verb" data-tr="qoʻydi">положи́л</span> его́ на стол.</p>

<p>— Оши́бок в <span class="cn-word" data-tr="grammatika">грамма́тике</span> нет, — сказа́л он. — Ни одно́й. Но я <span class="cn-word" data-pos="verb" data-tr="beraman">зада́м</span> три вопро́са.</p>

<p>— Пе́рвый: что тебе́ ну́жно? Отве́ть одни́м <span class="cn-word" data-tr="jumla">предложе́нием</span>.</p>

<p>Жасу́р <span class="cn-word" data-pos="verb" data-tr="oʻyladi">поду́мал</span> и сказа́л:</p>

<p>— Шесть мяче́й.</p>

<p>— Второ́й: в како́й <span class="cn-word" data-tr="qatorda">строке́</span> письма́ э́то напи́сано?</p>

<p>Жасу́р посмотре́л. Э́то бы́ло напи́сано на второ́й страни́це, в конце́.</p>

<p>— Тре́тий: дире́ктор чита́ет три́дцать пи́сем в день. До второ́й страни́цы он дошёл?</p>

<p>Жасу́р <span class="cn-word" data-pos="verb" data-tr="jim qoldi">замолча́л</span>.</p>

<p>Ве́чером он написа́л но́вое письмо́. Четы́ре строки́. В пе́рвой строке́ — про́сьба. Во второ́й — <span class="cn-word" data-tr="sabab">причи́на</span>. В тре́тьей — ско́лько сто́ит. В четвёртой — спаси́бо.</p>

<p>Отве́т пришёл на сле́дующий день.</p>

<p>Тепе́рь Жасу́р зна́ет, <strong>что</strong> дли́нное письмо́ — не всегда́ хоро́шее письмо́.</p>

<p>Пиши́ не для того́, <strong>что́бы сказа́ть</strong>. Пиши́ для того́, <strong>что́бы тебя́ по́няли</strong>.</p>''',
        "questions": [
            {
                "text": "Nega direktor birinchi xatga javob bermadi?",
                "choices": [
                    "Xat uzun edi va asosiy iltimos ikkinchi sahifaning oxirida turardi",
                    "Xatda grammatik xatolar koʻp edi",
                    "Direktor xatni umuman olmadi",
                    "Iltimos juda qimmatga tushardi"
                ],
                "answer": 0,
                "explanation": "Sergey Petrovichning uchinchi savoli shuni "
                               "koʻrsatadi: «дире́ктор чита́ет три́дцать пи́сем в "
                               "день. До второ́й страни́цы он дошёл?»",
            },
            {
                "text": "Nega matnda «Он хоте́л, что́бы дире́ктор отве́тил», lekin «Он ду́мал, что письмо́ хоро́шее»?",
                "choices": [
                    "«Хоте́ть» istakni bildiradi — что́бы; «ду́мать» faktni — что",
                    "Ikkalasi bir xil, farqi yoʻq",
                    "«Что́бы» faqat oʻtmish haqida ishlatiladi",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Xohlash, soʻrash, talab qilish — что́бы va undan "
                               "keyin oʻtgan zamon. Bilish, oʻylash, aytish — "
                               "что va oddiy zamonlar.",
            },
            {
                "text": "Ikkinchi xat qanday tuzilgan edi?",
                "choices": [
                    "Toʻrt qator: iltimos, sabab, narx, minnatdorchilik",
                    "Ikki sahifa, lekin xatosiz",
                    "Bir qator: «Menga olti dona toʻp kerak»",
                    "Direktorning savollariga javoblar"
                ],
                "answer": 0,
                "explanation": "«Четы́ре строки́. В пе́рвой — про́сьба. Во второ́й — "
                               "причи́на. В тре́тьей — ско́лько сто́ит. В "
                               "четвёртой — спаси́бо». Va javob ertasiga keldi.",
            },
        ],
    },
]
