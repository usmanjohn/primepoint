# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-41 … PR-43.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 41 — kichik tushunmovchilik (hikoya), 42 — mahalla
portreti, 43 — yangilik xabari. (38 hikoya, 39 retsept, 40 intervyu edi;
41 ham hikoya, lekin shakli butunlay boshqa — ikki odam orasidagi
tushunmovchilik, ketma-ket ikki kun.)

Grammatika chegarasi (kumulyativ qoida):
  41-matn: olmoshlarning turlanishi — меня́/мне/мной/обо мне va Н qoidasi.
           Matnda bitta odam (Afsona) uchta-toʻrtta shaklda uchraydi.
  42-matn: egalik olmoshlari — наш → на́шем, мой → моего́ — VA его́ ning
           oʻzgarmasligi. Ikkalasi yonma-yon turadi.
  43-matn: sifatlarning Р.п. va В.п. shakllari. Yangilik xabari janri
           bu yerda qulay: «ста́рого моста́», «но́вый мост» takrorlanadi.

⚠️ 43-matn haqida: bu MAHALLIY, oʻylab topilgan xabar. Unda real dunyo
haqida hech qanday fakt daʼvo qilinmaydi (aniq shahar, sana, raqam yoʻq),
shuning uchun toc'ning «facts must be true» qoidasi buzilmaydi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_41_43.py --author=prime
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
    # PR-41 — olmoshlar                     KICHIK TUSHUNMOVCHILIK
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Она́ мне не позвони́ла",
        "summary": (
            "PR-41 matni. Katya butun kechqurun qoʻngʻiroqni kutadi. Afsona "
            "qoʻngʻiroq qilmaydi. Ertasi kuni sabab maʼlum boʻladi — va ikkalasi "
            "ham bir xil narsani qilgan ekan."
        ),
        "order":   41,
        "grammar": [
            {
                "pattern":  "Olmoshning oltita shakli",
                "meaning":  "Bitta odam matnda bir necha shaklda uchraydi: её "
                            "(В.п.), ей (Д.п.), о ней (П.п.). Shaklni gapdagi ish "
                            "tanlaydi, odam emas.",
                "examples": ["Ка́тя ждала́ её.", "Ты не звони́ла мне."],
            },
            {
                "pattern":  "Predlogdan keyin Н",
                "meaning":  "Он / она́ / они́ olmoshlari predlogdan keyin Н bilan "
                            "boshlanadi: у него́, к ней, о ней. Predlogsiz esa Н "
                            "yoʻq: его́ нет, я ви́жу её.",
                "examples": ["Афсо́на пришла́ к ней.", "У него́ нет бата́реи."],
            },
            {
                "pattern":  "обо мне / о тебе́",
                "meaning":  "«О» predlogi «мне» dan oldin «обо» boʻladi — talaffuz "
                            "uchun. Xuddi «ко мне» va «со мной» kabi.",
                "examples": ["Ты ду́мала обо мне, я ду́мала о тебе́."],
            },
        ],
        "body": '''<p>В суббо́ту Афсона сказа́ла Кате: «Я <span class="cn-word" data-pos="verb" data-tr="qoʻngʻiroq qilaman">позвоню́</span> ве́чером».</p>

<p>Катя <span class="cn-word" data-pos="verb" data-tr="kutdi">ждала́</span> <strong>её</strong>. Час. Два часа́.</p>

<p>Афсона не <span class="cn-word" data-pos="verb" data-tr="qoʻngʻiroq qilmadi">позвони́ла</span>.</p>

<p>Кате бы́ло гру́стно. Она́ ду́мала <strong>о ней</strong> <span class="cn-word" data-tr="butun kechqurun">весь ве́чер</span>.</p>

<p>«Она́ <span class="cn-word" data-pos="verb" data-tr="unutdi">забы́ла</span> <strong>меня́</strong>», — ду́мала Катя.</p>

<p>В <span class="cn-word" data-tr="yakshanba">воскресе́нье</span> Афсона пришла́ <strong>к ней</strong>.</p>

<p>— Ты не звони́ла <strong>мне</strong>, — сказа́ла Катя ти́хо.</p>

<p>— Мой телефо́н, — сказа́ла Афсона. — <strong>У него́</strong> нет <span class="cn-word" data-tr="batareya">бата́реи</span>. Уже́ два дня.</p>

<p>Катя <span class="cn-word" data-pos="verb" data-tr="qaradi">посмотре́ла</span> <strong>на неё</strong>. Пото́м на телефо́н. Телефо́н был <span class="cn-word" data-tr="qora">чёрный</span> и ти́хий.</p>

<p>Афсона молча́ла. Пото́м сказа́ла:</p>

<p>— Я ду́мала <strong>о тебе́</strong> тоже. Два ве́чера.</p>

<p>Катя смея́лась.</p>

<p>— Зна́чит, так, — сказа́ла она́. — Ты ду́мала <strong>обо мне</strong>. Я ду́мала <strong>о тебе́</strong>. А телефо́н молча́л.</p>

<p>Тепе́рь у Афсоны есть <span class="cn-word" data-tr="quvvatlagich">заря́дка</span>. Она́ живёт у Кати. На <span class="cn-word" data-tr="har ehtimolga qarshi">вся́кий слу́чай</span>.</p>''',
        "questions": [
            {
                "text": "Nega Afsona qoʻngʻiroq qilmadi?",
                "choices": [
                    "Telefonining batareyasi ikki kundan beri oʻlgan edi",
                    "U Katyani unutgan edi",
                    "U Katyadan xafa boʻlgan edi",
                    "U shanba kuni band edi"
                ],
                "answer": 0,
                "explanation": "«У него́ нет бата́реи. Уже́ два дня». Katya esa «Она́ "
                               "забы́ла меня́» deb oʻylagan edi — matnning butun "
                               "tugʻuni shu ikki taxmin orasida.",
            },
            {
                "text": "«Она́ ду́мала о ней» va «Ты ду́мала обо мне» — nega bir xil "
                        "predlog ikki xil koʻrinadi?",
                "choices": [
                    "«Мне» dan oldin О predlogi ОБО boʻladi — talaffuz uchun",
                    "Chunki birinchisi uchinchi shaxs",
                    "Chunki ikkinchisi oʻtgan zamon",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Uchta predlog «мне / мной» dan oldin unli oladi: "
                               "о → обо, к → ко, с → со. «Обо мне», «ко мне», «со "
                               "мной» — uchtasini birga yodlash osonroq.",
            },
            {
                "text": "Matnning oxirgi jumlasi nimani anglatadi?",
                "choices": [
                    "Endi Afsonaning quvvatlagichi Katyanikida turadi — bunday hol takrorlanmasin deb",
                    "Afsona Katyanikiga koʻchib oʻtdi",
                    "Katya Afsonaga yangi telefon oldi",
                    "Afsona endi telefon ishlatmaydi"
                ],
                "answer": 0,
                "explanation": "«Тепе́рь у Афсоны есть заря́дка. Она́ живёт у Кати. На "
                               "вся́кий слу́чай». Doʻstlik muammoni hal qilmadi — "
                               "quvvatlagich hal qildi. Bu hikoyaning kichkina "
                               "hazili.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-42 — egalik olmoshlari              MAHALLA PORTRETI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "В на́шем дворе́",
        "summary": (
            "PR-42 matni. Bir hovlining portreti: qoʻshni Oleg Petrovich, buvi, "
            "eski daraxt va bolalarning ovozi. Oxirgi ikki jumla butun matnni "
            "bir soʻzga jamlaydi."
        ),
        "order":   42,
        "grammar": [
            {
                "pattern":  "наш → на́шем, на́шего",
                "meaning":  "Egalik olmoshi ot bilan BIRGA oʻzgaradi: в на́шем "
                            "дворе́ (Предло́жный), му́зыка на́шего двора́ "
                            "(Роди́тельный).",
                "examples": ["В на́шем дворе́ есть де́рево.", "Му́зыка на́шего двора́."],
            },
            {
                "pattern":  "мой → моего́, моя́",
                "meaning":  "Xuddi shunday: у моего́ сосе́да (Роди́тельный), моя́ "
                            "бабушка (bosh kelishik). Ayol jinsida мое́й toʻrtta "
                            "kelishikda ishlatiladi.",
                "examples": ["У моего́ сосе́да есть соба́ка."],
            },
            {
                "pattern":  "его́ / её / их — oʻzgarmaydi",
                "meaning":  "Bu uchtasi hech qachon turlanmaydi va predlogdan keyin "
                            "Н ham olmaydi: его́ дом, в его́ до́ме, их го́лоса. "
                            "Oʻzbekchadagi -i qoʻshimchasi kabi.",
                "examples": ["Его́ дом пе́рвый.", "Их го́лоса — э́то му́зыка."],
            },
        ],
        "body": '''<p><strong>Наш</strong> <span class="cn-word" data-tr="hovli">двор</span> ма́ленький. Но здесь живёт мно́го люде́й.</p>

<p>В <strong>на́шем</strong> дворе́ есть <span class="cn-word" data-tr="daraxt">де́рево</span>. Ста́рое. Ле́том под ним <span class="cn-word" data-tr="soya">тень</span>.</p>

<p><strong>Мой</strong> <span class="cn-word" data-tr="qoʻshni">сосе́д</span> — Олег Петро́вич. <strong>Его́</strong> дом пе́рвый. <strong>Его́</strong> окно́ смо́трит на у́лицу.</p>

<p>У <strong>моего́</strong> сосе́да есть <span class="cn-word" data-tr="it">соба́ка</span>. Её <span class="cn-word" data-pos="verb" data-tr="ismi">зову́т</span> Ди́на.</p>

<p><strong>Моя́</strong> бабушка сиди́т у <strong>на́шего</strong> <span class="cn-word" data-tr="podyezd, kirish">подъе́зда</span> ка́ждый ве́чер.</p>

<p>Она́ зна́ет здесь ка́ждый дом. И ка́ждую соба́ку.</p>

<p>Ве́чером де́ти игра́ют. <strong>Их</strong> <span class="cn-word" data-tr="ovozlar">го́лоса</span> — э́то му́зыка <strong>на́шего</strong> двора́.</p>

<p>Зимо́й во дворе́ ти́хо. То́лько Ди́на и <span class="cn-word" data-tr="qor">снег</span>.</p>

<p>Ле́том — громко. Дети, вода́, <span class="cn-word" data-tr="velosiped">велосипе́д</span>.</p>

<p>Я зна́ю ка́ждое окно́ в <strong>на́шем</strong> до́ме. Я зна́ю, где Олег Петро́вич <span class="cn-word" data-pos="verb" data-tr="ichadi">пьёт</span> чай.</p>

<p>Э́то не <strong>мой</strong> дом.</p>

<p>Э́то <strong>наш</strong> дом.</p>''',
        "questions": [
            {
                "text": "Matnning oxirgi ikki jumlasi nimani bildiradi?",
                "choices": [
                    "Hovli bitta odamning emas — u yerda yashovchi hammaniki",
                    "Muallif boshqa uyga koʻchgan",
                    "Uy qoʻshniniki",
                    "Muallif oʻz uyini sotmoqchi"
                ],
                "answer": 0,
                "explanation": "«Э́то не мой дом. Э́то наш дом». Butun matn qoʻshnilar, "
                               "buvi, bolalar va it haqida edi — oxirgi ikki jumla "
                               "shuni bitta soʻz almashtirish bilan aytadi: "
                               "мой → наш.",
            },
            {
                "text": "Nega «в на́шем дворе́», lekin «его́ дом»?",
                "choices": [
                    "Наш ot bilan birga oʻzgaradi, его́ esa hech qachon oʻzgarmaydi",
                    "Chunki «двор» erkak jinsida",
                    "Chunki birinchisi koʻplik",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Мой, твой, наш, ваш — sifat kabi turlanadi. Его́, её, "
                               "их esa turlanmaydi: «его́ дом», «в его́ до́ме», «с "
                               "его́ соба́кой» — har doim bir xil.",
            },
            {
                "text": "«Их го́лоса — э́то му́зыка на́шего двора́» — bu jumlada "
                        "nechta soʻz kelishikka kirgan?",
                "choices": [
                    "Ikkitasi: на́шего va двора́",
                    "Bittasi: двора́",
                    "Uchtasi: их, на́шего, двора́",
                    "Hech qaysi"
                ],
                "answer": 0,
                "explanation": "«На́шего двора́» — Роди́тельный, egalik: «hovlimizning "
                               "musiqasi». Ikkala soʻz ham oʻzgargan. «Их» esa "
                               "oʻzgarmaydi — u har doim shu shaklda qoladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-43 — sifat Р.п. / В.п.               YANGILIK XABARI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ста́рого моста́ бо́льше нет",
        "summary": (
            "PR-43 matni. Qisqa mahalliy xabar: qirq yil turgan eski koʻprik "
            "olib tashlandi. Xabar oxirida Nina Petrovna boʻsh joyga qarab "
            "turadi."
        ),
        "order":   43,
        "grammar": [
            {
                "pattern":  "Sifat Роди́тельный'da: -ОГО / -ОЙ",
                "meaning":  "Sifat otga ergashadi: ста́рого моста́, но́вой доро́ги. "
                            "-ОГО har doim [ово] boʻlib oʻqiladi.",
                "examples": ["Ста́рого моста́ бо́льше нет.", "У но́вого моста́ бу́дет две доро́ги."],
            },
            {
                "pattern":  "Sifat Вини́тельный'da",
                "meaning":  "Jonsiz erkak — oʻzgarmaydi (но́вый мост), ayol jinsi "
                            "-УЮ oladi. Jonlilik sifatga ham tegadi.",
                "examples": ["Она́ ходи́ла че́рез ста́рый мост.", "Я бу́ду по́мнить ста́рый."],
            },
            {
                "pattern":  "нет + Роди́тельный",
                "meaning":  "PR-34 dan: «yoʻq» dan keyin ot Роди́тельный'ga kiradi — "
                            "va sifat ham. «Ста́рого моста́ нет» — ikkala soʻz "
                            "oʻzgargan.",
                "examples": ["Ве́чером ста́рого моста́ уже́ не́ было."],
            },
        ],
        "body": '''<p><strong>Ста́рого моста́</strong> <span class="cn-word" data-tr="endi yoʻq">бо́льше нет</span>.</p>

<p>Он <span class="cn-word" data-pos="verb" data-tr="turgan">стоя́л</span> здесь <span class="cn-word" data-tr="qirq yil">со́рок лет</span>. Тепе́рь его́ нет.</p>

<p>Вчера́ у́тром пришли́ <span class="cn-word" data-tr="ishchilar">рабо́чие</span>. Ве́чером <strong>ста́рого моста́</strong> уже́ не́ было.</p>

<p>Лю́ди смотре́ли ти́хо. Оди́н челове́к <span class="cn-word" data-pos="verb" data-tr="rasmga oldi">сфотографи́ровал</span> <span class="cn-word" data-tr="boʻsh joy">пусто́е ме́сто</span>.</p>

<p>Ни́на Петро́вна по́мнит <strong>ста́рый мост</strong> с <span class="cn-word" data-tr="bolalikdan">де́тства</span>.</p>

<p>— Я ходи́ла в шко́лу че́рез <strong>ста́рый мост</strong>, — говори́т она́. — Ка́ждый день. Оди́ннадцать лет.</p>

<p>Ско́ро здесь бу́дет <strong>но́вый мост</strong>. Он бу́дет <span class="cn-word" data-tr="keng">широ́кий</span> и <span class="cn-word" data-tr="yorugʻ">све́тлый</span>.</p>

<p><span class="cn-word" data-tr="muhandislar">Инжене́ры</span> говоря́т: у <strong>но́вого моста́</strong> бу́дет две доро́ги для маши́н и оди́н <span class="cn-word" data-tr="yoʻl(ak)">путь</span> для люде́й.</p>

<p>Э́то хорошо́. <strong>У ста́рого моста́</strong> не́ было ме́ста для люде́й.</p>

<p>Ни́на Петро́вна смо́трит на пусто́е ме́сто над водо́й.</p>

<p>— <strong>Но́вый мост</strong> — э́то хорошо́, — говори́т она́. — Но я бу́ду по́мнить <strong>ста́рый</strong>.</p>''',
        "questions": [
            {
                "text": "Yangi koʻprik eskisidan nima bilan farq qiladi?",
                "choices": [
                    "Unda odamlar uchun ham yoʻl boʻladi",
                    "U kichikroq boʻladi",
                    "U temirdan boʻladi",
                    "U boshqa joyda quriladi"
                ],
                "answer": 0,
                "explanation": "«У но́вого моста́ бу́дет две доро́ги для маши́н и "
                               "оди́н путь для люде́й» — va darrov keyin: «У ста́рого "
                               "моста́ не́ было ме́ста для люде́й». Xabar farqni "
                               "aynan shu ikki jumla bilan koʻrsatadi.",
            },
            {
                "text": "«Ста́рого моста́» va «ста́рый мост» — nega ikki xil shakl?",
                "choices": [
                    "Birinchisi Роди́тельный («нет» dan keyin), ikkinchisi Вини́тельный",
                    "Birinchisi koʻplik",
                    "Ikkinchisi ayol jinsida",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "«Нет» va «у» dan keyin Роди́тельный keladi — sifat "
                               "-ОГО oladi. «Че́рез ста́рый мост» esa Вини́тельный, "
                               "va koʻprik jonsiz boʻlgani uchun shakl bosh kelishik "
                               "bilan bir xil qoladi.",
            },
            {
                "text": "Nina Petrovnaning oxirgi gapi nimani koʻrsatadi?",
                "choices": [
                    "U yangi koʻprikka qarshi emas, lekin eskisi uning hayotining bir qismi edi",
                    "U yangi koʻprikni yoqtirmaydi",
                    "U koʻprik qurilishiga qarshi",
                    "U boshqa shaharga koʻchmoqchi"
                ],
                "answer": 0,
                "explanation": "«Но́вый мост — э́то хорошо́. Но я бу́ду по́мнить "
                               "ста́рый». U oʻn bir yil har kuni oʻsha koʻprikdan "
                               "maktabga borgan. Xabar raqamlar bilan boshlanib, "
                               "xotira bilan tugaydi.",
            },
        ],
    },
]
