# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-32 … PR-34.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 32 — vokzal sahnasi, 33 — sayohat qaydlari, 34 — oila
tarixi. (29 ilmiy-ommabop, 30 sirli hikoya, 31 kitob sharhi edi.)

Grammatika chegarasi (kumulyativ qoida):
  32-matn: В.п. toʻldiruvchi sifatida. Matn butunlay jonli/jonsiz farqi
           ustiga qurilgan — odamlar odamni kutadi, odamlar narsani kutadi.
           Yoʻnalish maʼnosi (в шко́лу) hali YOʻQ — u PR-33 da.
  33-matn: В.п. yoʻnalish sifatida + «где?» bilan qarama-qarshiligi.
  34-matn: Р.п. egalik va «нет». Egalik zanjiri matnning oxirini quradi:
           дом де́да → дом отца́ → наш дом.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_32_34.py --author=prime
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
    # PR-32 — В.п. jonli/jonsiz                VOKZAL SAHNASI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Кто кого́ ждёт?",
        "summary": (
            "PR-32 matni. Vokzalda hamma kimnidir yoki nimanidir kutyapti — va "
            "aynan shu «kimni / nimani» farqi rus tilida soʻz shaklini "
            "oʻzgartiradi. Oxirida bittasi eng uzoq kutgani maʼlum boʻladi."
        ),
        "order":   32,
        "grammar": [
            {
                "pattern":  "Вини́тельный — jonli erkak",
                "meaning":  "Odam yoki hayvon boʻlsa, erkak jinsidagi ot -А / -Я "
                            "oladi: Жасу́р → Жасу́ра, брат → бра́та. Oʻzbekchadagi "
                            "-NI ning oʻzi, faqat shakl jonlilikka qaraydi.",
                "examples": ["Бекзо́д ждёт Жасу́ра.", "Ни́на ви́дит сестру́."],
            },
            {
                "pattern":  "Вини́тельный — jonsiz erkak",
                "meaning":  "Narsa boʻlsa, shakl UMUMAN oʻzgarmaydi: по́езд → по́езд, "
                            "авто́бус → авто́бус. Shuning uchun «ждёт по́езд», lekin "
                            "«ждёт бра́та».",
                "examples": ["Оле́г ждёт по́езд.", "Афсо́на ждёт авто́бус."],
            },
            {
                "pattern":  "Ayol jinsi — har doim -У",
                "meaning":  "Ayol jinsida jonlilik umuman ishlamaydi: сестра́ → "
                            "сестру́, Афсо́на → Афсо́ну, кни́га → кни́гу. Bitta "
                            "qoʻshimcha, hech qanday shart yoʻq.",
                "examples": ["Жасу́р ждёт Афсо́ну."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="vokzal">Вокза́л</span>. Ве́чер. Здесь все ждут.</p>

<p>Ни́на ждёт <strong>сестру́</strong>. Оле́г ждёт <strong>по́езд</strong>.</p>

<p>Жасур ждёт <strong>Афсо́ну</strong>. Афсона ждёт <strong>авто́бус</strong>.</p>

<p>А Бекзод ждёт <strong>Жасу́ра</strong>. И Жасур э́того не зна́ет.</p>

<p>Здесь есть оди́н <span class="cn-word" data-tr="muhim">ва́жный</span> вопро́с. Почему́ «сестру́», но «по́езд»?</p>

<p>Отве́т <span class="cn-word" data-tr="oddiy">просто́й</span>. <span class="cn-word" data-tr="singil, opa">Сестра́</span> — <span class="cn-word" data-tr="odam">челове́к</span>. По́езд — <span class="cn-word" data-tr="narsa, buyum">вещь</span>. Ру́сский язы́к ви́дит э́ту <span class="cn-word" data-tr="farq">ра́зницу</span>.</p>

<p>Вот по́езд. Все смо́трят.</p>

<p>Ни́на ви́дит <strong>сестру́</strong>. Сестра́ ви́дит <strong>Ни́ну</strong>.</p>

<p>Оле́г ви́дит <strong>по́езд</strong> — и <span class="cn-word" data-pos="verb" data-tr="yugurmoq">бежи́т</span>.</p>

<p>Афсона ви́дит <strong>авто́бус</strong>. Жасур ви́дит <strong>Афсо́ну</strong>.</p>

<p>А Бекзод уже́ давно́ ви́дит <strong>Жасу́ра</strong>. И молчи́т.</p>

<p>Бекзод ждал <span class="cn-word" data-tr="uzoqroq">до́льше</span> всех. Бекзод лю́бит <span class="cn-word" data-tr="syurprizlar">сюрпри́зы</span>.</p>''',
        "questions": [
            {
                "text": "Matnga koʻra kim eng uzoq kutdi?",
                "choices": [
                    "Bekzod — u Jasurni kutdi va jim turdi",
                    "Nina — u singlisini kutdi",
                    "Oleg — u poyezdni kutdi",
                    "Afsona — u avtobusni kutdi"
                ],
                "answer": 0,
                "explanation": "«Бекзод ждал до́льше всех». Matn boshida ham aytilgan "
                               "edi: «Бекзод ждёт Жасу́ра. И Жасур э́того не зна́ет» — "
                               "u koʻrinmasdan kutib turgan, chunki syurprizlarni "
                               "yaxshi koʻradi.",
            },
            {
                "text": "Nega matnda «ждёт сестру́», lekin «ждёт по́езд»?",
                "choices": [
                    "Сестра́ ayol jinsida (-У), по́езд esa jonsiz erkak (oʻzgarmaydi)",
                    "Chunki bittasi oʻtgan zamon",
                    "Chunki «по́езд» koʻplikda",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Ikkalasi ham Вини́тельный padejida. Ayol jinsi har doim "
                               "-У oladi. Erkak jinsida esa jonlilik hal qiladi: poyezd "
                               "— narsa, demak shakl bosh kelishik bilan bir xil "
                               "qoladi.",
            },
            {
                "text": "«Бекзод ви́дит Жасу́ра» — nega -А qoʻshilgan?",
                "choices": [
                    "Jasur — odam, demak jonli erkak: -А oladi",
                    "Chunki Jasur akasi",
                    "Chunki bu koʻplik",
                    "Chunki «ви́дит» feʼli har doim -А talab qiladi"
                ],
                "answer": 0,
                "explanation": "Jonli erkak otlar Вини́тельный'da -А / -Я oladi va "
                               "shakli Роди́тельный bilan bir xil boʻladi. Agar Bekzod "
                               "avtobusni koʻrayotgan boʻlsa, hech narsa "
                               "qoʻshilmasdi: «ви́дит авто́бус».",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-33 — В.п. yoʻnalish                    SAYOHAT QAYDLARI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Куда́ идёт э́тот авто́бус?",
        "summary": (
            "PR-33 matni. Yangi shaharda birinchi hafta: bozor, pochta, "
            "kutubxona, ish. Bitta xato haydovchini kuldiradi — va aynan shu "
            "xato «где?» bilan «куда́?» farqini bir umrga eslatib qoladi."
        ),
        "order":   33,
        "grammar": [
            {
                "pattern":  "куда́? — в / на + Вини́тельный",
                "meaning":  "Harakatning manzili. Predlog PR-30 dagidek qoladi, faqat "
                            "qoʻshimcha oʻzgaradi: на рабо́те → на рабо́ту, в шко́ле → "
                            "в шко́лу. Oʻzbekchadagi -DA ↔ -GA farqi.",
                "examples": ["Я иду́ на ры́нок.", "Я е́ду на рабо́ту."],
            },
            {
                "pattern":  "Jonsiz erkak — oʻzgarmaydi",
                "meaning":  "«Куда́?» maʼnosida ham jonsiz erkak otlar bosh kelishikda "
                            "qoladi: в магази́н, на ры́нок, на уро́к. Faqat predlog "
                            "qoʻshiladi.",
                "examples": ["Пото́м в магази́н и в библиоте́ку."],
            },
            {
                "pattern":  "до́ма ↔ домо́й",
                "meaning":  "Ravishlar juftligi: где? — до́ма, здесь, там. Куда́? — "
                            "домо́й, сюда́, туда́. Ular hech qachon aralashmaydi.",
                "examples": ["Ве́чером — домо́й."],
            },
        ],
        "body": '''<p>Я ещё не зна́ю э́тот го́род. Я то́лько спра́шиваю: «Куда́?»</p>

<p>Утром я иду́ <strong>на ры́нок</strong>. Там громко и <span class="cn-word" data-tr="mazali">вку́сно</span>.</p>

<p>Пото́м я иду́ <strong>на по́чту</strong>. Пото́м <strong>в магази́н</strong> и <strong>в библиоте́ку</strong>.</p>

<p><span class="cn-word" data-tr="soat ikkida">В два часа́</span> я е́ду <strong>на рабо́ту</strong>. Ве́чером — <strong>домо́й</strong>.</p>

<p>Вот всё <span class="cn-word" data-tr="qoida">пра́вило</span>. «Где?» — я <strong>на рабо́те</strong>. «Куда́?» — я е́ду <strong>на рабо́ту</strong>. Оди́н предло́г, два <span class="cn-word" data-tr="qoʻshimchalar">оконча́ния</span>.</p>

<p>Оди́н раз я говорю́ <span class="cn-word" data-tr="notoʻgʻri">непра́вильно</span>.</p>

<p>Я в <span class="cn-word" data-tr="taksi">такси́</span> и говорю́: «Я е́ду <strong>в Москве́</strong>».</p>

<p><span class="cn-word" data-tr="haydovchi">Води́тель</span> смеётся.</p>

<p>— Вы уже́ <strong>в Москве́</strong>, — говори́т он. — А <strong>куда́</strong> вы е́дете?</p>

<p>Тепе́рь я по́мню э́то <span class="cn-word" data-tr="butun umr">всю жизнь</span>. <strong>-Е</strong> — э́то «здесь». <strong>-У</strong> — э́то «туда́».</p>

<p><strong>В суббо́ту</strong> я е́ду <strong>в дере́вню</strong>. В <span class="cn-word" data-tr="yakshanba">воскресе́нье</span> — <strong>домо́й</strong>.</p>

<p>Я ещё не зна́ю го́род. Но я уже́ зна́ю <span class="cn-word" data-tr="asosiy savol">гла́вный вопро́с</span>: «Куда́?»</p>''',
        "questions": [
            {
                "text": "Taksida qanday xato qilindi?",
                "choices": [
                    "«В Москве́» deyildi — bu «Moskvada», «Moskvaga» emas",
                    "Manzil notoʻgʻri aytildi",
                    "Haydovchiga salom berilmadi",
                    "Pul yetmadi"
                ],
                "answer": 0,
                "explanation": "«Я е́ду в Москве́» soʻzma-soʻz «Moskva ichida "
                               "ketyapman» degani. Haydovchining javobi shuning uchun "
                               "kulgili: «Вы уже́ в Москве́. А куда́ вы е́дете?»",
            },
            {
                "text": "Matndagi qoidani oʻz soʻzingiz bilan ayting: -Е va -У nima "
                        "farq qiladi?",
                "choices": [
                    "-Е joyni bildiradi (qayerda), -У manzilni (qayerga)",
                    "-Е koʻplik, -У birlik",
                    "-Е oʻtgan zamon, -У hozirgi",
                    "-Е erkak jinsi, -У ayol jinsi"
                ],
                "answer": 0,
                "explanation": "Matnning oʻzi buni aytadi: «-Е — э́то „здесь“. -У — "
                               "э́то „туда́“». Predlog ikkala holatda ham bir xil, "
                               "shuning uchun maʼnoni faqat qoʻshimcha hal qiladi — "
                               "xuddi oʻzbekchadagi -DA va -GA kabi.",
            },
            {
                "text": "Nega «в библиоте́ку», lekin «в магази́н»?",
                "choices": [
                    "Библиоте́ка ayol jinsida (-У), магази́н esa jonsiz erkak (oʻzgarmaydi)",
                    "Chunki kutubxona kattaroq",
                    "Chunki «магази́н» chet soʻzi",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Ikkalasi ham Вини́тельный, ikkalasi ham «куда́?». Ayol "
                               "jinsi -У oladi, jonsiz erkak esa umuman oʻzgarmaydi — "
                               "unga faqat predlog qoʻshiladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-34 — Р.п. egalik va нет                OILA TARIXI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Дом моего́ де́да",
        "summary": (
            "PR-34 matni. Qishloqdagi eski uy — bobodan otaga, otadan bizga. "
            "Uyda koʻp narsa yoʻq, lekin buvining bir jumlasi nima borligini "
            "aytib beradi."
        ),
        "order":   34,
        "grammar": [
            {
                "pattern":  "Egalik: кни́га бра́та",
                "meaning":  "Egasi HAR DOIM orqada turadi va u kelishikka kiradi. "
                            "Oʻzbekchaning teskarisi: «akaning kitobi» → «кни́га "
                            "бра́та». Birinchi soʻz bosh kelishikda qoladi.",
                "examples": ["Э́то дом де́да.", "Окно́ ку́хни смо́трит на восто́к."],
            },
            {
                "pattern":  "нет + Роди́тельный",
                "meaning":  "«Yoʻq» dan keyin ot har doim Роди́тельный'da: есть "
                            "кни́га → нет кни́ги. Oʻzbekchada ot oʻzgarmaydi, "
                            "ruschada oʻzgaradi.",
                "examples": ["Здесь нет телеви́зора.", "В го́роде нет вре́мени."],
            },
            {
                "pattern":  "вре́мя → вре́мени",
                "meaning":  "-МЯ ga tugaydigan kichik guruh (вре́мя, и́мя) alohida "
                            "turlanadi. «Нет вре́мени» — rus tilida eng koʻp "
                            "aytiladigan iboralardan biri.",
                "examples": ["В го́роде нет вре́мени. А здесь вре́мя есть."],
            },
        ],
        "body": '''<p>В дере́вне есть ста́рый дом. Э́то дом <strong>де́да</strong>.</p>

<p><span class="cn-word" data-tr="bobo">Дед</span> <span class="cn-word" data-pos="verb" data-tr="qurgan">стро́ил</span> э́тот дом до́лго. Три го́да.</p>

<p>Дом <strong>де́да</strong> не большо́й. Две ко́мнаты и <span class="cn-word" data-tr="oshxona">ку́хня</span>. Окно́ <strong>ку́хни</strong> смо́трит на <span class="cn-word" data-tr="sharq">восто́к</span>.</p>

<p>Здесь нет <strong>телеви́зора</strong>. Нет <strong>интерне́та</strong>. Зимо́й <span class="cn-word" data-tr="baʼzan">иногда́</span> нет <strong>воды́</strong>.</p>

<p>Но здесь есть <span class="cn-word" data-tr="sukunat">тишина́</span>. И <span class="cn-word" data-tr="hid">за́пах</span> <strong>хле́ба</strong>.</p>

<p>Ка́ждое ле́то мы е́дем в дере́вню.</p>

<p>Бабушка сиди́т на <span class="cn-word" data-tr="ayvonda">вера́нде</span> и говори́т ме́дленно.</p>

<p>— В го́роде нет <strong>вре́мени</strong>, — говори́т бабушка. — А здесь вре́мя есть.</p>

<p>Я ду́маю об э́том <span class="cn-word" data-tr="uzoq">до́лго</span>. Бабушка <span class="cn-word" data-tr="haqli">права́</span>.</p>

<p>В го́роде у нас есть телеви́зор, интерне́т и вода́. Но нет <strong>вре́мени</strong>.</p>

<p>Здесь нет <strong>телеви́зора</strong>. Но есть вре́мя, тишина́ и хлеб.</p>

<p><span class="cn-word" data-tr="avvaliga">Снача́ла</span> э́то был дом <strong>де́да</strong>. Пото́м — дом <strong>отца́</strong>. Тепе́рь э́то наш дом.</p>''',
        "questions": [
            {
                "text": "Buvining gapi nimani anglatadi?",
                "choices": [
                    "Shaharda hamma narsa bor, lekin vaqt yoʻq; qishloqda teskarisi",
                    "Qishloqda hayot qiyinroq",
                    "Shaharda yashash yaxshiroq",
                    "Buvi shaharga koʻchmoqchi"
                ],
                "answer": 0,
                "explanation": "«В го́роде нет вре́мени. А здесь вре́мя есть» — matn "
                               "shu jumla atrofida qurilgan. Keyingi xatboshi uni "
                               "ochib beradi: shaharda televizor, internet va suv "
                               "bor, lekin vaqt yoʻq.",
            },
            {
                "text": "«Дом де́да» nega «де́да дом» emas?",
                "choices": [
                    "Ruschada egalik bildiruvchi soʻz har doim orqada turadi",
                    "Chunki «дед» erkak jinsida",
                    "Chunki uy kattaroq",
                    "Ikkala variant ham toʻgʻri"
                ],
                "answer": 0,
                "explanation": "Bu oʻzbekchaning teskarisi. Oʻzbekchada «bobo-NING "
                               "uy-I» — egasi oldinda va ikkala soʻz belgilanadi. "
                               "Ruschada «дом де́да» — egasi orqada va faqat u "
                               "kelishikka kiradi.",
            },
            {
                "text": "«Здесь нет телеви́зора» — nega «телеви́зор» emas?",
                "choices": [
                    "«Нет» dan keyin ot har doim Роди́тельный padejida boʻladi",
                    "Chunki televizor jonli hisoblanadi",
                    "Chunki bu koʻplik",
                    "Chunki bu oʻtgan zamon"
                ],
                "answer": 0,
                "explanation": "Solishtiring: «есть телеви́зор» (bosh kelishik) va «нет "
                               "телеви́зора» (Роди́тельный). Oʻzbekchada ot ikkala "
                               "gapda ham oʻzgarmaydi — «televizor bor / televizor "
                               "yoʻq» — shuning uchun bu qoidani alohida yodlash "
                               "kerak.",
            },
        ],
    },
]
