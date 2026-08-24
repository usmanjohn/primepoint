# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-35 … PR-37.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 35 — xat, 36 — ilmiy-ommabop, 37 — sinf sahnasi.
(32 vokzal sahnasi, 33 sayohat qaydlari, 34 oila tarixi edi.)

⚠️ FAKTLAR HAQIDA (36-matn). Toc qoidasi: «Facts must be true». Moskvadagi
koʻpriklarning ANIQ soni manbalarda har xil — chunki nimani sanash kerakligi
har xil (daryo ustidagi koʻpriklar, yoʻl koʻpriklari, piyodalar koʻprigi,
metro koʻpriklari). Shuning uchun matn aniq raqam AYTMAYDI; aksincha,
uning mavzusi aynan shu — nega bu savolga bitta javob yoʻq. Bu ham rost,
ham grammatika uchun ideal: bitta koʻprik, ikki koʻprik, besh koʻprik.

Grammatika chegarasi (kumulyativ qoida):
  35-matn: Р.п. predloglar bilan (из, с, от, до, у, без, для, около, после).
  36-matn: sonlar bilan Р.п. — 1 / 2-3-4 / 5+ uchligi matnning oʻzida
           tushuntiriladi.
  37-matn: Д.п. — «кому?». Oxirgi jumla PR-36 dagi son qoidasini ham
           ishlatadi: двадцать одна история.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_35_37.py --author=prime
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
    # PR-35 — Р.п. predloglar                    XAT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Письмо из Сибири",
        "summary": (
            "PR-35 matni. Sherbek Sibirdan Afsonaga xat yozadi: kundalik yoʻli, "
            "uy yonidagi koʻl, shakarsiz choy — va konvertda unga atalgan bir "
            "narsa."
        ),
        "order":   35,
        "grammar": [
            {
                "pattern":  "из / с / от — uchta «-dan»",
                "meaning":  "Oʻzbekcha -DAN ruschada uchga boʻlinadi. ИЗ — В oladigan "
                            "joydan (из дома), С — НА oladigan joydan (с работы), "
                            "ОТ — odamdan (от мамы).",
                "examples": ["Я иду из дома.", "Вечером — с работы.", "Письмо от мамы."],
            },
            {
                "pattern":  "без · для · около · после",
                "meaning":  "Bu predloglarning maʼnosi oʻzbekchada tanish: -siz, "
                            "uchun, yaqinida, keyin. Farq faqat joyda — ruschada "
                            "ular soʻzdan OLDIN turadi va ot Р.п. ga kiradi.",
                "examples": ["Чай без сахара.", "Это для тебя.", "После работы."],
            },
            {
                "pattern":  "у + Родительный",
                "meaning":  "Ikki maʼnoda: joy (у озера — koʻl yonida) va egalik "
                            "(у меня — menda, PR-14). Ikkalasi ham Р.п. talab qiladi.",
                "examples": ["Я гуляю у озера."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Assalom">Здравствуй</span>, Афсона!</p>

<p>Это письмо <strong>из Сибири</strong>. <strong>Из</strong> города <strong>Иркутска</strong>.</p>

<p>Я живу здесь <span class="cn-word" data-tr="bir oy">месяц</span>. Утром я иду <strong>из</strong> дома на работу. Вечером иду <strong>с</strong> работы домой. <strong>До</strong> дома <span class="cn-word" data-tr="uzoq emas">недалеко</span>.</p>

<p><strong>Около</strong> дома есть <span class="cn-word" data-tr="koʻl">озеро</span>. Не Байкал — маленькое. Но <span class="cn-word" data-tr="qishda">зимой</span> оно <span class="cn-word" data-tr="oq">белое</span>.</p>

<p>Здесь пьют чай <strong>без</strong> <span class="cn-word" data-tr="shakar">сахара</span>. Сначала я не понимал. Теперь понимаю.</p>

<p><strong>После</strong> работы я гуляю <strong>у</strong> озера. Один. Здесь тихо.</p>

<p>Вчера было письмо <strong>от</strong> мамы. Мама пишет: «Когда ты домой?»</p>

<p>Я не знаю. Здесь холодно. Здесь <span class="cn-word" data-tr="uzoq">далеко</span> <strong>от</strong> Ташкента. Но здесь я думаю медленно — и это хорошо.</p>

<p>В <span class="cn-word" data-tr="konvert">конверте</span> есть <span class="cn-word" data-tr="fotosurat">фотография</span>. Это <strong>для тебя</strong>. Озеро <strong>у</strong> дома, утром.</p>

<p>Я жду письмо <strong>от тебя</strong>.</p>

<p>Шербек</p>''',
        "questions": [
            {
                "text": "Sherbek nega Toshkentga qaytishni bilmayapti?",
                "choices": [
                    "Sibirda u sekin oʻylay oladi va bu unga yoqadi",
                    "U yerda ishi juda koʻp",
                    "Yoʻl juda qimmat",
                    "U onasidan xafa"
                ],
                "answer": 0,
                "explanation": "«Здесь холодно. Здесь далеко от Ташкента. Но здесь я "
                               "думаю медленно — и это хорошо». Sovuq va uzoqlik "
                               "kamchilik, sekin oʻylash esa afzallik — xat shu "
                               "muvozanat ustida turadi.",
            },
            {
                "text": "Nega «из дома», lekin «с работы»?",
                "choices": [
                    "Дом В oladi (→ ИЗ), работа esa НА oladi (→ С)",
                    "Chunki ikkalasi ikki xil kelishik",
                    "Chunki «дом» erkak jinsida",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "PR-30 dagi В/НА roʻyxati bu yerda uchinchi marta "
                               "ishlayapti: «в доме» → «из дома», «на работе» → "
                               "«с работы». Yangi roʻyxat yodlash kerak emas.",
            },
            {
                "text": "Nega «письмо от мамы», «из мамы» emas?",
                "choices": [
                    "ОТ odam uchun ishlatiladi, ИЗ va С esa joy uchun",
                    "Chunki «мама» ayol jinsida",
                    "Chunki xat uzoqdan kelgan",
                    "Ikkala variant ham toʻgʻri"
                ],
                "answer": 0,
                "explanation": "Uchta «-dan» uch xil ish qiladi: joydan chiqsangiz ИЗ "
                               "yoki С, odamning oldidan kelsangiz yoki odamdan bir "
                               "narsa olsangiz — ОТ. Matn oxirida ham shunday: «письмо "
                               "от тебя».",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-36 — sonlar bilan Р.п.                  ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Сколько в Москве мостов?",
        "summary": (
            "PR-36 matni. Oddiy koʻrinadigan savol — lekin unga bitta javob "
            "yoʻq, chunki har kim boshqa narsani sanaydi. Matn son qoidasini "
            "shu savol ustida koʻrsatadi."
        ),
        "order":   36,
        "grammar": [
            {
                "pattern":  "1 · 2-3-4 · 5+",
                "meaning":  "Son otning shaklini tanlaydi: один мост (bosh kelishik), "
                            "два моста (Р.п. birlik), пять мостов (Р.п. koʻplik). "
                            "Oʻzbekchada ot umuman oʻzgarmaydi — bu sof yangi ish.",
                "examples": ["Один мост. Два моста. Пять мостов."],
            },
            {
                "pattern":  "много / мало + Р.п.",
                "meaning":  "Miqdor soʻzlari ham Родительный talab qiladi: много "
                            "мостов, много людей, мало воды. Sanaladigan narsa — "
                            "koʻplik, sanalmaydigani — birlik.",
                "examples": ["В Москве много рек, дорог и мостов."],
            },
            {
                "pattern":  "для + Р.п.",
                "meaning":  "«Uchun» — PR-35 dan. Bu yerda u koʻplik bilan keladi: "
                            "для машин, для людей — koʻplik Родительный shakli.",
                "examples": ["Есть мосты для машин. Есть мосты для людей."],
            },
        ],
        "body": '''<p><strong>Сколько</strong> в Москве <strong>мостов</strong>? Это не простой вопрос.</p>

<p>Сначала нужно ответить на другой вопрос. Что мы <span class="cn-word" data-pos="verb" data-tr="sanaymiz">считаем</span>?</p>

<p>Есть <span class="cn-word" data-tr="koʻpriklar">мосты</span> <strong>через</strong> реку. Есть мосты <strong>для</strong> машин. Есть мосты <strong>для</strong> людей. Есть мосты <strong>для</strong> <span class="cn-word" data-tr="metro">метро</span>.</p>

<p>Одна книга считает одно. Другая книга считает другое. Поэтому <span class="cn-word" data-tr="raqamlar">числа</span> разные.</p>

<p>Но русский язык здесь <span class="cn-word" data-tr="qiziq">интересный</span>.</p>

<p><strong>Один мост</strong>. <strong>Два моста</strong>. <strong>Пять мостов</strong>.</p>

<p>Одно слово — три формы. Почему?</p>

<p>Это <span class="cn-word" data-tr="eski">старое</span> правило. После 2, 3, 4 — одна форма. После 5, 6, 7 — другая.</p>

<p>Такое правило работает всегда. И с <span class="cn-word" data-tr="daryolar">реками</span>, и с <span class="cn-word" data-tr="yoʻllar">дорогами</span>, и с годами.</p>

<p>Так <strong>сколько</strong> в Москве <strong>мостов</strong>?</p>

<p><span class="cn-word" data-tr="halol">Честный</span> ответ: <strong>много</strong>. В Москве много рек, много дорог и много <strong>мостов</strong>.</p>

<p><span class="cn-word" data-tr="Aniq son">Точное число</span> знает не каждый. А правило знает <span class="cn-word" data-tr="har bir">каждый</span>, кто учит русский язык.</p>''',
        "questions": [
            {
                "text": "Nega Moskvadagi koʻpriklar soniga bitta javob yoʻq?",
                "choices": [
                    "Chunki har kim boshqa narsani sanaydi",
                    "Chunki har yili yangi koʻprik quriladi",
                    "Chunki hech kim sanamagan",
                    "Chunki koʻpriklar juda kichkina"
                ],
                "answer": 0,
                "explanation": "Matn buni ochiq aytadi: daryo ustidagi koʻpriklar, "
                               "mashinalar uchun, odamlar uchun, metro uchun — «Одна "
                               "книга считает одно. Другая книга считает "
                               "другое».",
            },
            {
                "text": "«Один мост. Два моста. Пять мостов» — bu uch shakl nimani "
                        "koʻrsatadi?",
                "choices": [
                    "Rus tilida son otning shaklini tanlaydi",
                    "Koʻpriklar har xil kattalikda",
                    "Bu uch xil koʻprik turi",
                    "Bu uch xil kelishik"
                ],
                "answer": 0,
                "explanation": "1 — bosh kelishik; 2, 3, 4 — Родительный birlik; 5 va "
                               "undan yuqori — Родительный koʻplik. Oʻzbekchada esa "
                               "«bir koʻprik, ikki koʻprik, besh koʻprik» — ot umuman "
                               "oʻzgarmaydi.",
            },
            {
                "text": "Matnning oxirgi jumlasi nimani anglatadi?",
                "choices": [
                    "Aniq sonni hamma bilmaydi, lekin qoidani rus tilini oʻrganayotgan har kim biladi",
                    "Faqat moskvaliklar aniq sonni biladi",
                    "Qoidani bilish shart emas",
                    "Koʻpriklarni sanash foydasiz"
                ],
                "answer": 0,
                "explanation": "«Точное число знает не каждый. А правило знает "
                               "каждый, кто учит русский язык». Matn statistikadan "
                               "grammatikaga oʻtadi: raqam oʻzgaruvchan, qoida esa "
                               "barqaror.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-37 — Д.п. «кому?»                       SINF SAHNASI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Подарок учителю",
        "summary": (
            "PR-37 matni. Sinf oʻqituvchiga sovgʻa tanlay olmaydi: kitobmi, "
            "ruchkami? Jasurning taklifi hammaga yoqmaydi — lekin oxirida "
            "oʻqituvchining javobi hamma narsani hal qiladi."
        ),
        "order":   37,
        "grammar": [
            {
                "pattern":  "Дательный — кому?",
                "meaning":  "Oʻzbekcha -GA ning aynan oʻzi. Erkak va oʻrta jins -У/-Ю "
                            "(учителю, классу), ayol jinsi -Е (Афсоне, маме). "
                            "Olmoshlar: мне, тебе, ему, ей, нам, вам, им.",
                "examples": ["Подарок учителю.", "Мы напишем ему письма."],
            },
            {
                "pattern":  "Ikki toʻldiruvchi: кому + что",
                "meaning":  "Дать, сказать, писать feʼllari ikkita toʻldiruvchi "
                            "oladi: kimga (Д.п.) va nimani (В.п.). Oʻzbekchadagi "
                            "tartib ham xuddi shunday.",
                "examples": ["Говорит учитель классу."],
            },
            {
                "pattern":  "много + Р.п. koʻplik",
                "meaning":  "PR-36 dan: miqdor soʻzi Родительный koʻplik talab "
                            "qiladi — много ручек. Va son ham: двадцать одно "
                            "письмо (oxiri 1 — bosh kelishik).",
                "examples": ["У учителя много ручек.", "Двадцать одно письмо."],
            },
        ],
        "body": '''<p>Скоро <span class="cn-word" data-tr="bayram">праздник</span>. Класс думает: какой <span class="cn-word" data-tr="sovgʻa">подарок</span> <strong>учителю</strong>?</p>

<p>Афсона говорит: «Книга. Учитель любит читать».</p>

<p>Бекзод говорит: «Не книга. Ручка».</p>

<p>Катя говорит: «У учителя много <span class="cn-word" data-tr="ruchkalar">ручек</span>».</p>

<p>Жасур молчит. Потом говорит тихо:</p>

<p>— Мы можем написать <strong>ему</strong> <span class="cn-word" data-tr="xatlar">письма</span>. Один <span class="cn-word" data-tr="oʻquvchi">ученик</span> — одно письмо.</p>

<p><span class="cn-word" data-tr="sinf">Класс</span> молчит.</p>

<p>— Двадцать одно письмо? — спрашивает Катя.</p>

<p>— Двадцать одно, — говорит Жасур.</p>

<p>Праздник. Учитель <span class="cn-word" data-pos="verb" data-tr="ochadi">открывает</span> <span class="cn-word" data-tr="quti">коробку</span>.</p>

<p>Там нет книги. Нет ручки. Там двадцать одно письмо.</p>

<p>Учитель читает медленно. Одно письмо. <span class="cn-word" data-tr="ikkinchisi">Второе</span>. <span class="cn-word" data-tr="uchinchisi">Третье</span>.</p>

<p>Потом он говорит <strong>классу</strong>:</p>

<p>— Спасибо. Книга — это одна <span class="cn-word" data-tr="hikoya">история</span>. А здесь двадцать одна.</p>''',
        "questions": [
            {
                "text": "Sinf oxirida oʻqituvchiga nima berdi?",
                "choices": [
                    "Yigirma bitta xat — har bir oʻquvchidan bittadan",
                    "Kitob",
                    "Ruchka",
                    "Kitob va ruchka"
                ],
                "answer": 0,
                "explanation": "Jasurning taklifi: «Один ученик — одно письмо». "
                               "Qutida na kitob, na ruchka bor edi — «Там двадцать "
                               "одно письмо».",
            },
            {
                "text": "Oʻqituvchining oxirgi gapi nimani anglatadi?",
                "choices": [
                    "Kitob bitta hikoya, xatlar esa yigirma bitta hikoya",
                    "U kitobni koʻproq yoqtirardi",
                    "Xatlar juda qisqa boʻlgan",
                    "U yigirma bitta kitob soʻragan"
                ],
                "answer": 0,
                "explanation": "«Книга — это одна история. А здесь двадцать "
                               "одна». Sovgʻa qimmatligi bilan emas, ichidagi hikoyalar "
                               "soni bilan oʻlchanadi — shuning uchun sinfning "
                               "tanlovi toʻgʻri chiqdi.",
            },
            {
                "text": "Nega «двадцать одно письмо», «двадцать одни письма» emas?",
                "choices": [
                    "Son 1 ga tugasa, ot bosh kelishikda va birlikda qoladi",
                    "Chunki «письмо» oʻrta jinsda",
                    "Chunki xatlar bir xil edi",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "PR-36 qoidasi: katta sonlarda oxirgi raqamga qaraladi. "
                               "Oxiri 1 boʻlsa — bosh kelishik, birlik. Shuning uchun "
                               "oxirgi jumlada ham «двадцать одна история» — ayol "
                               "jinsi uchun «одна».",
            },
        ],
    },
]
