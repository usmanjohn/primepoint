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
           ishlatadi: два́дцать одна́ исто́рия.

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
        "title":   "Письмо́ из Сиби́ри",
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
                            "joydan (из до́ма), С — НА oladigan joydan (с рабо́ты), "
                            "ОТ — odamdan (от ма́мы).",
                "examples": ["Я иду́ из до́ма.", "Ве́чером — с рабо́ты.", "Письмо́ от ма́мы."],
            },
            {
                "pattern":  "без · для · о́коло · по́сле",
                "meaning":  "Bu predloglarning maʼnosi oʻzbekchada tanish: -siz, "
                            "uchun, yaqinida, keyin. Farq faqat joyda — ruschada "
                            "ular soʻzdan OLDIN turadi va ot Р.п. ga kiradi.",
                "examples": ["Чай без са́хара.", "Э́то для тебя́.", "По́сле рабо́ты."],
            },
            {
                "pattern":  "у + Роди́тельный",
                "meaning":  "Ikki maʼnoda: joy (у о́зера — koʻl yonida) va egalik "
                            "(у меня́ — menda, PR-14). Ikkalasi ham Р.п. talab qiladi.",
                "examples": ["Я гуля́ю у о́зера."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Assalom">Здра́вствуй</span>, Афсона!</p>

<p>Э́то письмо́ <strong>из Сиби́ри</strong>. <strong>Из</strong> го́рода <strong>Ирку́тска</strong>.</p>

<p>Я живу́ здесь <span class="cn-word" data-tr="bir oy">ме́сяц</span>. Утром я иду́ <strong>из</strong> до́ма на рабо́ту. Вечером иду́ <strong>с</strong> рабо́ты домо́й. <strong>До</strong> до́ма <span class="cn-word" data-tr="uzoq emas">недалеко́</span>.</p>

<p><strong>О́коло</strong> до́ма есть <span class="cn-word" data-tr="koʻl">о́зеро</span>. Не Байка́л — ма́ленькое. Но <span class="cn-word" data-tr="qishda">зимо́й</span> оно́ <span class="cn-word" data-tr="oq">бе́лое</span>.</p>

<p>Здесь пьют чай <strong>без</strong> <span class="cn-word" data-tr="shakar">са́хара</span>. Снача́ла я не понима́л. Тепе́рь понима́ю.</p>

<p><strong>По́сле</strong> рабо́ты я гуля́ю <strong>у</strong> о́зера. Оди́н. Здесь тихо.</p>

<p>Вчера́ бы́ло письмо́ <strong>от</strong> мамы. Мама пи́шет: «Когда́ ты домо́й?»</p>

<p>Я не зна́ю. Здесь хо́лодно. Здесь <span class="cn-word" data-tr="uzoq">далеко́</span> <strong>от</strong> Ташке́нта. Но здесь я ду́маю ме́дленно — и э́то хорошо́.</p>

<p>В <span class="cn-word" data-tr="konvert">конве́рте</span> есть <span class="cn-word" data-tr="fotosurat">фотогра́фия</span>. Э́то <strong>для тебя́</strong>. О́зеро <strong>у</strong> до́ма, утром.</p>

<p>Я жду письмо́ <strong>от тебя́</strong>.</p>

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
                "explanation": "«Здесь хо́лодно. Здесь далеко́ от Ташке́нта. Но здесь я "
                               "ду́маю ме́дленно — и э́то хорошо́». Sovuq va uzoqlik "
                               "kamchilik, sekin oʻylash esa afzallik — xat shu "
                               "muvozanat ustida turadi.",
            },
            {
                "text": "Nega «из до́ма», lekin «с рабо́ты»?",
                "choices": [
                    "Дом В oladi (→ ИЗ), рабо́та esa НА oladi (→ С)",
                    "Chunki ikkalasi ikki xil kelishik",
                    "Chunki «дом» erkak jinsida",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "PR-30 dagi В/НА roʻyxati bu yerda uchinchi marta "
                               "ishlayapti: «в до́ме» → «из до́ма», «на рабо́те» → "
                               "«с рабо́ты». Yangi roʻyxat yodlash kerak emas.",
            },
            {
                "text": "Nega «письмо́ от ма́мы», «из ма́мы» emas?",
                "choices": [
                    "ОТ odam uchun ishlatiladi, ИЗ va С esa joy uchun",
                    "Chunki «ма́ма» ayol jinsida",
                    "Chunki xat uzoqdan kelgan",
                    "Ikkala variant ham toʻgʻri"
                ],
                "answer": 0,
                "explanation": "Uchta «-dan» uch xil ish qiladi: joydan chiqsangiz ИЗ "
                               "yoki С, odamning oldidan kelsangiz yoki odamdan bir "
                               "narsa olsangiz — ОТ. Matn oxirida ham shunday: «письмо́ "
                               "от тебя́».",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-36 — sonlar bilan Р.п.                  ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ско́лько в Москве́ мосто́в?",
        "summary": (
            "PR-36 matni. Oddiy koʻrinadigan savol — lekin unga bitta javob "
            "yoʻq, chunki har kim boshqa narsani sanaydi. Matn son qoidasini "
            "shu savol ustida koʻrsatadi."
        ),
        "order":   36,
        "grammar": [
            {
                "pattern":  "1 · 2-3-4 · 5+",
                "meaning":  "Son otning shaklini tanlaydi: оди́н мост (bosh kelishik), "
                            "два моста́ (Р.п. birlik), пять мосто́в (Р.п. koʻplik). "
                            "Oʻzbekchada ot umuman oʻzgarmaydi — bu sof yangi ish.",
                "examples": ["Оди́н мост. Два моста́. Пять мосто́в."],
            },
            {
                "pattern":  "мно́го / ма́ло + Р.п.",
                "meaning":  "Miqdor soʻzlari ham Роди́тельный talab qiladi: мно́го "
                            "мосто́в, мно́го люде́й, ма́ло воды́. Sanaladigan narsa — "
                            "koʻplik, sanalmaydigani — birlik.",
                "examples": ["В Москве́ мно́го рек, доро́г и мосто́в."],
            },
            {
                "pattern":  "для + Р.п.",
                "meaning":  "«Uchun» — PR-35 dan. Bu yerda u koʻplik bilan keladi: "
                            "для маши́н, для люде́й — koʻplik Роди́тельный shakli.",
                "examples": ["Есть мосты́ для маши́н. Есть мосты́ для люде́й."],
            },
        ],
        "body": '''<p><strong>Ско́лько</strong> в Москве́ <strong>мосто́в</strong>? Э́то не просто́й вопро́с.</p>

<p>Снача́ла ну́жно отве́тить на друго́й вопро́с. Что мы <span class="cn-word" data-pos="verb" data-tr="sanaymiz">счита́ем</span>?</p>

<p>Есть <span class="cn-word" data-tr="koʻpriklar">мосты́</span> <strong>че́рез</strong> ре́ку. Есть мосты́ <strong>для</strong> маши́н. Есть мосты́ <strong>для</strong> люде́й. Есть мосты́ <strong>для</strong> <span class="cn-word" data-tr="metro">метро́</span>.</p>

<p>Одна́ кни́га счита́ет одно́. Друга́я кни́га счита́ет друго́е. Поэ́тому <span class="cn-word" data-tr="raqamlar">чи́сла</span> ра́зные.</p>

<p>Но ру́сский язы́к здесь <span class="cn-word" data-tr="qiziq">интере́сный</span>.</p>

<p><strong>Оди́н мост</strong>. <strong>Два моста́</strong>. <strong>Пять мосто́в</strong>.</p>

<p>Одно́ сло́во — три фо́рмы. Почему́?</p>

<p>Э́то <span class="cn-word" data-tr="eski">ста́рое</span> пра́вило. По́сле 2, 3, 4 — одна́ фо́рма. По́сле 5, 6, 7 — друга́я.</p>

<p>Тако́е пра́вило рабо́тает всегда́. И с <span class="cn-word" data-tr="daryolar">ре́ками</span>, и с <span class="cn-word" data-tr="yoʻllar">доро́гами</span>, и с года́ми.</p>

<p>Так <strong>ско́лько</strong> в Москве́ <strong>мосто́в</strong>?</p>

<p><span class="cn-word" data-tr="halol">Че́стный</span> отве́т: <strong>мно́го</strong>. В Москве́ мно́го рек, мно́го доро́г и мно́го <strong>мосто́в</strong>.</p>

<p><span class="cn-word" data-tr="Aniq son">То́чное число́</span> зна́ет не ка́ждый. А пра́вило зна́ет <span class="cn-word" data-tr="har bir">ка́ждый</span>, кто у́чит ру́сский язы́к.</p>''',
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
                               "mashinalar uchun, odamlar uchun, metro uchun — «Одна́ "
                               "кни́га счита́ет одно́. Друга́я кни́га счита́ет "
                               "друго́е».",
            },
            {
                "text": "«Оди́н мост. Два моста́. Пять мосто́в» — bu uch shakl nimani "
                        "koʻrsatadi?",
                "choices": [
                    "Rus tilida son otning shaklini tanlaydi",
                    "Koʻpriklar har xil kattalikda",
                    "Bu uch xil koʻprik turi",
                    "Bu uch xil kelishik"
                ],
                "answer": 0,
                "explanation": "1 — bosh kelishik; 2, 3, 4 — Роди́тельный birlik; 5 va "
                               "undan yuqori — Роди́тельный koʻplik. Oʻzbekchada esa "
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
                "explanation": "«То́чное число́ зна́ет не ка́ждый. А пра́вило зна́ет "
                               "ка́ждый, кто у́чит ру́сский язы́к». Matn statistikadan "
                               "grammatikaga oʻtadi: raqam oʻzgaruvchan, qoida esa "
                               "barqaror.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-37 — Д.п. «кому?»                       SINF SAHNASI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Пода́рок учи́телю",
        "summary": (
            "PR-37 matni. Sinf oʻqituvchiga sovgʻa tanlay olmaydi: kitobmi, "
            "ruchkami? Jasurning taklifi hammaga yoqmaydi — lekin oxirida "
            "oʻqituvchining javobi hamma narsani hal qiladi."
        ),
        "order":   37,
        "grammar": [
            {
                "pattern":  "Да́тельный — кому́?",
                "meaning":  "Oʻzbekcha -GA ning aynan oʻzi. Erkak va oʻrta jins -У/-Ю "
                            "(учи́телю, кла́ссу), ayol jinsi -Е (Афсо́не, ма́ме). "
                            "Olmoshlar: мне, тебе́, ему́, ей, нам, вам, им.",
                "examples": ["Пода́рок учи́телю.", "Мы напи́шем ему́ пи́сьма."],
            },
            {
                "pattern":  "Ikki toʻldiruvchi: кому́ + что",
                "meaning":  "Дать, сказа́ть, писа́ть feʼllari ikkita toʻldiruvchi "
                            "oladi: kimga (Д.п.) va nimani (В.п.). Oʻzbekchadagi "
                            "tartib ham xuddi shunday.",
                "examples": ["Говори́т учи́тель кла́ссу."],
            },
            {
                "pattern":  "мно́го + Р.п. koʻplik",
                "meaning":  "PR-36 dan: miqdor soʻzi Роди́тельный koʻplik talab "
                            "qiladi — мно́го ру́чек. Va son ham: два́дцать одно́ "
                            "письмо́ (oxiri 1 — bosh kelishik).",
                "examples": ["У учи́теля мно́го ру́чек.", "Два́дцать одно́ письмо́."],
            },
        ],
        "body": '''<p>Ско́ро <span class="cn-word" data-tr="bayram">пра́здник</span>. Класс ду́мает: како́й <span class="cn-word" data-tr="sovgʻa">пода́рок</span> <strong>учи́телю</strong>?</p>

<p>Афсона говори́т: «Кни́га. Учи́тель лю́бит чита́ть».</p>

<p>Бекзод говори́т: «Не кни́га. Ру́чка».</p>

<p>Катя говори́т: «У учи́теля мно́го <span class="cn-word" data-tr="ruchkalar">ру́чек</span>».</p>

<p>Жасур молчи́т. Пото́м говори́т ти́хо:</p>

<p>— Мы мо́жем написа́ть <strong>ему́</strong> <span class="cn-word" data-tr="xatlar">пи́сьма</span>. Оди́н <span class="cn-word" data-tr="oʻquvchi">учени́к</span> — одно́ письмо́.</p>

<p><span class="cn-word" data-tr="sinf">Класс</span> молчи́т.</p>

<p>— Два́дцать одно́ письмо́? — спра́шивает Катя.</p>

<p>— Два́дцать одно́, — говори́т Жасур.</p>

<p>Пра́здник. Учи́тель <span class="cn-word" data-pos="verb" data-tr="ochadi">открыва́ет</span> <span class="cn-word" data-tr="quti">коро́бку</span>.</p>

<p>Там нет кни́ги. Нет ру́чки. Там два́дцать одно́ письмо́.</p>

<p>Учи́тель чита́ет ме́дленно. Одно́ письмо́. <span class="cn-word" data-tr="ikkinchisi">Второ́е</span>. <span class="cn-word" data-tr="uchinchisi">Тре́тье</span>.</p>

<p>Пото́м он говори́т <strong>кла́ссу</strong>:</p>

<p>— Спаси́бо. Кни́га — э́то одна́ <span class="cn-word" data-tr="hikoya">исто́рия</span>. А здесь два́дцать одна́.</p>''',
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
                "explanation": "Jasurning taklifi: «Оди́н учени́к — одно́ письмо́». "
                               "Qutida na kitob, na ruchka bor edi — «Там два́дцать "
                               "одно́ письмо́».",
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
                "explanation": "«Кни́га — э́то одна́ исто́рия. А здесь два́дцать "
                               "одна́». Sovgʻa qimmatligi bilan emas, ichidagi hikoyalar "
                               "soni bilan oʻlchanadi — shuning uchun sinfning "
                               "tanlovi toʻgʻri chiqdi.",
            },
            {
                "text": "Nega «два́дцать одно́ письмо́», «два́дцать одни́ пи́сьма» emas?",
                "choices": [
                    "Son 1 ga tugasa, ot bosh kelishikda va birlikda qoladi",
                    "Chunki «письмо́» oʻrta jinsda",
                    "Chunki xatlar bir xil edi",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "PR-36 qoidasi: katta sonlarda oxirgi raqamga qaraladi. "
                               "Oxiri 1 boʻlsa — bosh kelishik, birlik. Shuning uchun "
                               "oxirgi jumlada ham «два́дцать одна́ исто́рия» — ayol "
                               "jinsi uchun «одна́».",
            },
        ],
    },
]
