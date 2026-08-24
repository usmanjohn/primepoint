# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-41 … PR-43.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 41 — kichik tushunmovchilik (hikoya), 42 — mahalla
portreti, 43 — yangilik xabari. (38 hikoya, 39 retsept, 40 intervyu edi;
41 ham hikoya, lekin shakli butunlay boshqa — ikki odam orasidagi
tushunmovchilik, ketma-ket ikki kun.)

Grammatika chegarasi (kumulyativ qoida):
  41-matn: olmoshlarning turlanishi — меня/мне/мной/обо мне va Н qoidasi.
           Matnda bitta odam (Afsona) uchta-toʻrtta shaklda uchraydi.
  42-matn: egalik olmoshlari — наш → нашем, мой → моего — VA его ning
           oʻzgarmasligi. Ikkalasi yonma-yon turadi.
  43-matn: sifatlarning Р.п. va В.п. shakllari. Yangilik xabari janri
           bu yerda qulay: «старого моста», «новый мост» takrorlanadi.

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
        "title":   "Она мне не позвонила",
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
                "examples": ["Катя ждала её.", "Ты не звонила мне."],
            },
            {
                "pattern":  "Predlogdan keyin Н",
                "meaning":  "Он / она / они olmoshlari predlogdan keyin Н bilan "
                            "boshlanadi: у него, к ней, о ней. Predlogsiz esa Н "
                            "yoʻq: его нет, я вижу её.",
                "examples": ["Афсона пришла к ней.", "У него нет батареи."],
            },
            {
                "pattern":  "обо мне / о тебе",
                "meaning":  "«О» predlogi «мне» dan oldin «обо» boʻladi — talaffuz "
                            "uchun. Xuddi «ко мне» va «со мной» kabi.",
                "examples": ["Ты думала обо мне, я думала о тебе."],
            },
        ],
        "body": '''<p>В субботу Афсона сказала Кате: «Я <span class="cn-word" data-pos="verb" data-tr="qoʻngʻiroq qilaman">позвоню</span> вечером».</p>

<p>Катя <span class="cn-word" data-pos="verb" data-tr="kutdi">ждала</span> <strong>её</strong>. Час. Два часа.</p>

<p>Афсона не <span class="cn-word" data-pos="verb" data-tr="qoʻngʻiroq qilmadi">позвонила</span>.</p>

<p>Кате было грустно. Она думала <strong>о ней</strong> <span class="cn-word" data-tr="butun kechqurun">весь вечер</span>.</p>

<p>«Она <span class="cn-word" data-pos="verb" data-tr="unutdi">забыла</span> <strong>меня</strong>», — думала Катя.</p>

<p>В <span class="cn-word" data-tr="yakshanba">воскресенье</span> Афсона пришла <strong>к ней</strong>.</p>

<p>— Ты не звонила <strong>мне</strong>, — сказала Катя тихо.</p>

<p>— Мой телефон, — сказала Афсона. — <strong>У него</strong> нет <span class="cn-word" data-tr="batareya">батареи</span>. Уже два дня.</p>

<p>Катя <span class="cn-word" data-pos="verb" data-tr="qaradi">посмотрела</span> <strong>на неё</strong>. Потом на телефон. Телефон был <span class="cn-word" data-tr="qora">чёрный</span> и тихий.</p>

<p>Афсона молчала. Потом сказала:</p>

<p>— Я думала <strong>о тебе</strong> тоже. Два вечера.</p>

<p>Катя смеялась.</p>

<p>— Значит, так, — сказала она. — Ты думала <strong>обо мне</strong>. Я думала <strong>о тебе</strong>. А телефон молчал.</p>

<p>Теперь у Афсоны есть <span class="cn-word" data-tr="quvvatlagich">зарядка</span>. Она живёт у Кати. На <span class="cn-word" data-tr="har ehtimolga qarshi">всякий случай</span>.</p>''',
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
                "explanation": "«У него нет батареи. Уже два дня». Katya esa «Она "
                               "забыла меня» deb oʻylagan edi — matnning butun "
                               "tugʻuni shu ikki taxmin orasida.",
            },
            {
                "text": "«Она думала о ней» va «Ты думала обо мне» — nega bir xil "
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
                "explanation": "«Теперь у Афсоны есть зарядка. Она живёт у Кати. На "
                               "всякий случай». Doʻstlik muammoni hal qilmadi — "
                               "quvvatlagich hal qildi. Bu hikoyaning kichkina "
                               "hazili.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-42 — egalik olmoshlari              MAHALLA PORTRETI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "В нашем дворе",
        "summary": (
            "PR-42 matni. Bir hovlining portreti: qoʻshni Oleg Petrovich, buvi, "
            "eski daraxt va bolalarning ovozi. Oxirgi ikki jumla butun matnni "
            "bir soʻzga jamlaydi."
        ),
        "order":   42,
        "grammar": [
            {
                "pattern":  "наш → нашем, нашего",
                "meaning":  "Egalik olmoshi ot bilan BIRGA oʻzgaradi: в нашем "
                            "дворе (Предложный), музыка нашего двора "
                            "(Родительный).",
                "examples": ["В нашем дворе есть дерево.", "Музыка нашего двора."],
            },
            {
                "pattern":  "мой → моего, моя",
                "meaning":  "Xuddi shunday: у моего соседа (Родительный), моя "
                            "бабушка (bosh kelishik). Ayol jinsida моей toʻrtta "
                            "kelishikda ishlatiladi.",
                "examples": ["У моего соседа есть собака."],
            },
            {
                "pattern":  "его / её / их — oʻzgarmaydi",
                "meaning":  "Bu uchtasi hech qachon turlanmaydi va predlogdan keyin "
                            "Н ham olmaydi: его дом, в его доме, их голоса. "
                            "Oʻzbekchadagi -i qoʻshimchasi kabi.",
                "examples": ["Его дом первый.", "Их голоса — это музыка."],
            },
        ],
        "body": '''<p><strong>Наш</strong> <span class="cn-word" data-tr="hovli">двор</span> маленький. Но здесь живёт много людей.</p>

<p>В <strong>нашем</strong> дворе есть <span class="cn-word" data-tr="daraxt">дерево</span>. Старое. Летом под ним <span class="cn-word" data-tr="soya">тень</span>.</p>

<p><strong>Мой</strong> <span class="cn-word" data-tr="qoʻshni">сосед</span> — Олег Петрович. <strong>Его</strong> дом первый. <strong>Его</strong> окно смотрит на улицу.</p>

<p>У <strong>моего</strong> соседа есть <span class="cn-word" data-tr="it">собака</span>. Её <span class="cn-word" data-pos="verb" data-tr="ismi">зовут</span> Дина.</p>

<p><strong>Моя</strong> бабушка сидит у <strong>нашего</strong> <span class="cn-word" data-tr="podyezd, kirish">подъезда</span> каждый вечер.</p>

<p>Она знает здесь каждый дом. И каждую собаку.</p>

<p>Вечером дети играют. <strong>Их</strong> <span class="cn-word" data-tr="ovozlar">голоса</span> — это музыка <strong>нашего</strong> двора.</p>

<p>Зимой во дворе тихо. Только Дина и <span class="cn-word" data-tr="qor">снег</span>.</p>

<p>Летом — громко. Дети, вода, <span class="cn-word" data-tr="velosiped">велосипед</span>.</p>

<p>Я знаю каждое окно в <strong>нашем</strong> доме. Я знаю, где Олег Петрович <span class="cn-word" data-pos="verb" data-tr="ichadi">пьёт</span> чай.</p>

<p>Это не <strong>мой</strong> дом.</p>

<p>Это <strong>наш</strong> дом.</p>''',
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
                "explanation": "«Это не мой дом. Это наш дом». Butun matn qoʻshnilar, "
                               "buvi, bolalar va it haqida edi — oxirgi ikki jumla "
                               "shuni bitta soʻz almashtirish bilan aytadi: "
                               "мой → наш.",
            },
            {
                "text": "Nega «в нашем дворе», lekin «его дом»?",
                "choices": [
                    "Наш ot bilan birga oʻzgaradi, его esa hech qachon oʻzgarmaydi",
                    "Chunki «двор» erkak jinsida",
                    "Chunki birinchisi koʻplik",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Мой, твой, наш, ваш — sifat kabi turlanadi. Его, её, "
                               "их esa turlanmaydi: «его дом», «в его доме», «с "
                               "его собакой» — har doim bir xil.",
            },
            {
                "text": "«Их голоса — это музыка нашего двора» — bu jumlada "
                        "nechta soʻz kelishikka kirgan?",
                "choices": [
                    "Ikkitasi: нашего va двора",
                    "Bittasi: двора",
                    "Uchtasi: их, нашего, двора",
                    "Hech qaysi"
                ],
                "answer": 0,
                "explanation": "«Нашего двора» — Родительный, egalik: «hovlimizning "
                               "musiqasi». Ikkala soʻz ham oʻzgargan. «Их» esa "
                               "oʻzgarmaydi — u har doim shu shaklda qoladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-43 — sifat Р.п. / В.п.               YANGILIK XABARI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Старого моста больше нет",
        "summary": (
            "PR-43 matni. Qisqa mahalliy xabar: qirq yil turgan eski koʻprik "
            "olib tashlandi. Xabar oxirida Nina Petrovna boʻsh joyga qarab "
            "turadi."
        ),
        "order":   43,
        "grammar": [
            {
                "pattern":  "Sifat Родительный'da: -ОГО / -ОЙ",
                "meaning":  "Sifat otga ergashadi: старого моста, новой дороги. "
                            "-ОГО har doim [ово] boʻlib oʻqiladi.",
                "examples": ["Старого моста больше нет.", "У нового моста будет две дороги."],
            },
            {
                "pattern":  "Sifat Винительный'da",
                "meaning":  "Jonsiz erkak — oʻzgarmaydi (новый мост), ayol jinsi "
                            "-УЮ oladi. Jonlilik sifatga ham tegadi.",
                "examples": ["Она ходила через старый мост.", "Я буду помнить старый."],
            },
            {
                "pattern":  "нет + Родительный",
                "meaning":  "PR-34 dan: «yoʻq» dan keyin ot Родительный'ga kiradi — "
                            "va sifat ham. «Старого моста нет» — ikkala soʻz "
                            "oʻzgargan.",
                "examples": ["Вечером старого моста уже не было."],
            },
        ],
        "body": '''<p><strong>Старого моста</strong> <span class="cn-word" data-tr="endi yoʻq">больше нет</span>.</p>

<p>Он <span class="cn-word" data-pos="verb" data-tr="turgan">стоял</span> здесь <span class="cn-word" data-tr="qirq yil">сорок лет</span>. Теперь его нет.</p>

<p>Вчера утром пришли <span class="cn-word" data-tr="ishchilar">рабочие</span>. Вечером <strong>старого моста</strong> уже не было.</p>

<p>Люди смотрели тихо. Один человек <span class="cn-word" data-pos="verb" data-tr="rasmga oldi">сфотографировал</span> <span class="cn-word" data-tr="boʻsh joy">пустое место</span>.</p>

<p>Нина Петровна помнит <strong>старый мост</strong> с <span class="cn-word" data-tr="bolalikdan">детства</span>.</p>

<p>— Я ходила в школу через <strong>старый мост</strong>, — говорит она. — Каждый день. Одиннадцать лет.</p>

<p>Скоро здесь будет <strong>новый мост</strong>. Он будет <span class="cn-word" data-tr="keng">широкий</span> и <span class="cn-word" data-tr="yorugʻ">светлый</span>.</p>

<p><span class="cn-word" data-tr="muhandislar">Инженеры</span> говорят: у <strong>нового моста</strong> будет две дороги для машин и один <span class="cn-word" data-tr="yoʻl(ak)">путь</span> для людей.</p>

<p>Это хорошо. <strong>У старого моста</strong> не было места для людей.</p>

<p>Нина Петровна смотрит на пустое место над водой.</p>

<p>— <strong>Новый мост</strong> — это хорошо, — говорит она. — Но я буду помнить <strong>старый</strong>.</p>''',
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
                "explanation": "«У нового моста будет две дороги для машин и "
                               "один путь для людей» — va darrov keyin: «У старого "
                               "моста не было места для людей». Xabar farqni "
                               "aynan shu ikki jumla bilan koʻrsatadi.",
            },
            {
                "text": "«Старого моста» va «старый мост» — nega ikki xil shakl?",
                "choices": [
                    "Birinchisi Родительный («нет» dan keyin), ikkinchisi Винительный",
                    "Birinchisi koʻplik",
                    "Ikkinchisi ayol jinsida",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "«Нет» va «у» dan keyin Родительный keladi — sifat "
                               "-ОГО oladi. «Через старый мост» esa Винительный, "
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
                "explanation": "«Новый мост — это хорошо. Но я буду помнить "
                               "старый». U oʻn bir yil har kuni oʻsha koʻprikdan "
                               "maktabga borgan. Xabar raqamlar bilan boshlanib, "
                               "xotira bilan tugaydi.",
            },
        ],
    },
]
