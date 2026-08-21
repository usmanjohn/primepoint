# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-24 … PR-26.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 24 — xat, 25 — biografik hikoya, 26 — oila portreti.
(21 intervyu, 22 sahna, 23 kundalik daftar edi — hech qaysisi takrorlanmadi.)

Grammatika chegarasi (kumulyativ qoida):
  24-matn: kelasi zamon бу́ду + infinitiv (PR-24). Qaytim feʼllar YOʻQ
           (PR-25), мочь/уме́ть YOʻQ (PR-26).
  25-matn: -ся / -сь feʼllari (PR-25) oʻtgan zamonda. Hikoyachi — yigit,
           shuning uchun учи́лся / боя́лся / стара́лся. Мочь va уме́ть hali
           yoʻq, shuning uchun «suza olmasdim» oʻrniga «боя́лся» ishlatilgan.
  26-matn: уме́ть va мочь (PR-26) — butun matn shu ikkisining farqi ustiga
           qurilgan.

Kelishiklar hali oʻrgatilmagan (PR-29 dan): matnlar bosh kelishikda, «в
шко́лу», «у меня́», «ка́ждую суббо́ту» kabi iboralar butun boʻlak sifatida
cn-word bilan izohlangan.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_24_26.py --author=prime
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
    # PR-24 — kelasi zamon                XAT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "За́втра экза́мен",
        "summary": (
            "PR-24 matni. Afsona buvisiga xat yozadi: ertaga imtihon, bugun "
            "tayyorgarlik, shanbada qoʻngʻiroq va yozda birga choy. Butun xat "
            "kelasi zamon ustiga qurilgan."
        ),
        "order":   24,
        "grammar": [
            {
                "pattern":  "бу́ду + infinitiv",
                "meaning":  "Kelasi zamon ikki soʻzdan iborat: tuslanadigan yordamchi "
                            "feʼl (бу́ду, бу́дешь, бу́дет, бу́дем, бу́дете, бу́дут) va "
                            "oʻzgarmagan infinitiv. Faqat birinchi soʻz tuslanadi.",
                "examples": ["Я бу́ду чита́ть весь день.", "Мы бу́дем пить чай."],
            },
            {
                "pattern":  "Yolgʻiz бу́ду — «boʻlaman»",
                "meaning":  "Agar gapda boshqa feʼl boʻlmasa, бу́ду oʻzi kesim boʻladi: "
                            "Я бу́ду до́ма. За́втра бу́дет дождь. Yoniga yana «быть» "
                            "qoʻshilmaydi.",
                "examples": ["Ле́том я бу́ду в Самарка́нде.", "За́втра бу́дет дождь."],
            },
            {
                "pattern":  "не бу́ду",
                "meaning":  "Inkor tuslanadigan feʼlning oldiga tushadi — infinitivning "
                            "emas. Toʻgʻri: «я не бу́ду спеши́ть», notoʻgʻri: «я бу́ду не "
                            "спеши́ть».",
                "examples": ["Я не бу́ду спеши́ть."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Aziz, qadrli">До́рогая</span> бабушка!</p>

<p>За́втра <span class="cn-word" data-tr="menda ... bor">у меня́</span> <span class="cn-word" data-tr="imtihon">экза́мен</span>. Ру́сский язык.</p>

<p>Сегодня я <strong>бу́ду</strong> чита́ть весь день. Потом я <strong>бу́ду</strong> писа́ть слова́. Вечером я <strong>бу́ду</strong> спать ра́но. Я не <strong>бу́ду</strong> <span class="cn-word" data-pos="verb" data-tr="shoshmoq">спеши́ть</span>.</p>

<p>Вчера́ я чита́ла три часа́. Это было тру́дно. Но сегодня <strong>бу́дет</strong> хорошо́ — я зна́ю.</p>

<p>Мама говори́т: «За́втра <strong>бу́дет</strong> дождь». <span class="cn-word" data-tr="Hechqisi yoʻq">Ничего́</span>. Зонт у меня́ есть.</p>

<p>Бабушка, я <span class="cn-word" data-pos="verb" data-tr="vaʼda beraman">обеща́ю</span>: в субботу я <strong>бу́ду</strong> звони́ть. И потом <strong>бу́ду</strong> звони́ть <span class="cn-word" data-tr="har shanba">ка́ждую суббо́ту</span>. <span class="cn-word" data-tr="albatta">Обяза́тельно</span>.</p>

<p>А <span class="cn-word" data-tr="yozda">ле́том</span> я <strong>бу́ду</strong> в Самарка́нде. Мы <strong>бу́дем</strong> пить чай и говори́ть. До́лго.</p>

<p>Экза́мен — за́втра. А чай — <span class="cn-word" data-tr="yozda">ле́том</span>. Я <strong>бу́ду</strong> ду́мать о ча́е.</p>

<p>Афсона</p>''',
        "questions": [
            {
                "text": "Afsona xatida buvisiga qanday vaʼda beradi?",
                "choices": [
                    "Har shanba qoʻngʻiroq qilishga",
                    "Imtihonni aʼlo baholarga topshirishga",
                    "Yozda Samarqandda qolishga",
                    "Har kuni xat yozishga"
                ],
                "answer": 0,
                "explanation": "«Я обеща́ю: в субботу я бу́ду звони́ть. И потом бу́ду "
                               "звони́ть ка́ждую суббо́ту. Обяза́тельно» — vaʼda aynan "
                               "qoʻngʻiroq haqida.",
            },
            {
                "text": "«Я бу́ду чита́ть» va «Я бу́ду в Самарка́нде» — nega birinchisida "
                        "ikkita feʼl bor, ikkinchisida bittasi?",
                "choices": [
                    "Ikkinchisida infinitiv kerak emas — бу́ду oʻzi «boʻlaman» degani",
                    "Ikkinchisi oʻtgan zamon",
                    "Bu xato, ikkinchisida ham infinitiv boʻlishi kerak",
                    "Birinchisi hozirgi zamon"
                ],
                "answer": 0,
                "explanation": "Agar gapda boshqa feʼl boʻlsa, u infinitivda qoladi: "
                               "«бу́ду чита́ть». Agar boshqa feʼl boʻlmasa, «бу́ду» ning "
                               "oʻzi kesim boʻladi va «boʻlaman» maʼnosini beradi. "
                               "Yoniga yana «быть» qoʻshib boʻlmaydi.",
            },
            {
                "text": "Xat qanday tugaydi va bu nimani koʻrsatadi?",
                "choices": [
                    "Imtihon ertaga, choy esa yozda — Afsona uzoqroqqa qaraydi",
                    "Afsona imtihondan qoʻrqadi",
                    "Afsona Samarqandga koʻchib ketmoqchi",
                    "Buvisi kasal boʻlib qolgan"
                ],
                "answer": 0,
                "explanation": "«Экза́мен — за́втра. А чай — ле́том. Я бу́ду ду́мать о "
                               "ча́е» — Afsona ertangi tashvishni yozgi quvonch bilan "
                               "yonma-yon qoʻyadi. Xat imtihon haqida boshlanib, "
                               "buvisi bilan koʻrishish haqida tugaydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-25 — qaytim feʼllar              BIOGRAFIK HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Как я учи́лся пла́вать",
        "summary": (
            "PR-25 matni. Jasur qishloqda suzishni oʻrganadi: birinchi kuni "
            "qoʻrqadi, akasi kuladi, toʻrtinchi kuni suzadi — va aka endi "
            "kulmaydi. Hikoyachi yigit, shuning uchun feʼllar -СЯ bilan."
        ),
        "order":   25,
        "grammar": [
            {
                "pattern":  "-ся / -сь",
                "meaning":  "Qaytim qoʻshimchasi feʼlning eng oxirida turadi. Unlidan "
                            "keyin -СЬ (учу́сь, стара́юсь), undoshdan keyin -СЯ "
                            "(у́чится, боя́лся). Oʻzbekchadagi -(i)n- ga oʻxshaydi: "
                            "yuv-in-moq.",
                "examples": ["Я учи́лся пла́вать.", "Шербе́к смея́лся."],
            },
            {
                "pattern":  "Oʻtgan zamonda: учи́лся / учи́лась",
                "meaning":  "Avval jins qoʻshimchasi, keyin -ся/-сь. Erkak: учи́л+СЯ "
                            "(Л — undosh). Ayol: учи́ла+СЬ (А — unli). Koʻplik: "
                            "учи́ли+СЬ.",
                "examples": ["Я боя́лся.", "Мы учи́лись вме́сте."],
            },
            {
                "pattern":  "Faqat -ся bilan yashaydigan feʼllar",
                "meaning":  "Смея́ться, боя́ться, стара́ться, улыба́ться, находи́ться — "
                            "bu feʼllar -ся siz umuman mavjud emas. «Он смеёт» degan "
                            "shakl yoʻq.",
                "examples": ["Я стара́лся.", "Река́ нахо́дится далеко́."],
            },
        ],
        "body": '''<p>Это было <span class="cn-word" data-tr="ancha oldin">давно́</span>. Я <strong>учи́лся</strong> пла́вать <span class="cn-word" data-tr="qishloqda">в дере́вне</span>. Там была́ <span class="cn-word" data-tr="daryo">река́</span>.</p>

<p>Пе́рвый день. Вода́ была́ холо́дная. Я <strong>боя́лся</strong>.</p>

<p>Мой брат Шербек <strong>смея́лся</strong>. Шербек пла́вал хорошо́.</p>

<p>— Жасур, вода́ <span class="cn-word" data-tr="iliq">тёплая</span>, — говори́л Шербек. — Я <strong>учи́лся</strong> три дня. И ты <strong>бу́дешь</strong> пла́вать.</p>

<p>Второ́й день. Я <strong>стара́лся</strong>. Оди́н <span class="cn-word" data-tr="marta">раз</span>. Потом ещё раз. Потом ещё. Вода́ была́ <span class="cn-word" data-tr="hamma joyda">везде́</span>. Шербек <strong>смея́лся</strong> <span class="cn-word" data-tr="yana">сно́ва</span>.</p>

<p>Тре́тий день. Я <strong>учи́лся</strong> у́тром. Потом я <strong>учи́лся</strong> ве́чером. Я <strong>стара́лся</strong> и <span class="cn-word" data-pos="verb" data-tr="jim turdim">молча́л</span>.</p>

<p>Четвёртый день. Я <span class="cn-word" data-pos="verb" data-tr="suzdim">плыл</span>! Три <span class="cn-word" data-tr="metr">ме́тра</span>. Потом пять.</p>

<p>Шербек не <strong>смея́лся</strong>. Шербек <strong>улыба́лся</strong>.</p>

<p>Теперь я живу́ в Ташкенте. Река́ <strong>нахо́дится</strong> далеко́. Но я <span class="cn-word" data-pos="verb" data-tr="eslayman">по́мню</span> э́ту во́ду.</p>

<p>Вода́ была́ холо́дная то́лько оди́н день. Пе́рвый. Потом я <span class="cn-word" data-tr="shunchaki">про́сто</span> <strong>боя́лся</strong> <span class="cn-word" data-tr="kamroq">ме́ньше</span>.</p>''',
        "questions": [
            {
                "text": "Toʻrtinchi kuni Sherbek nega kulmadi?",
                "choices": [
                    "Chunki Jasur nihoyat suzdi — u endi jilmaydi",
                    "Chunki Jasur unga xafa boʻldi",
                    "Chunki Sherbek uyga ketgan edi",
                    "Chunki suv juda sovuq edi"
                ],
                "answer": 0,
                "explanation": "«Шербек не смея́лся. Шербек улыба́лся» — kulish oʻrnini "
                               "jilmayish egalladi. Bu ikki soʻzning farqi butun "
                               "hikoyaning tugashi: masxara emas, quvonch.",
            },
            {
                "text": "Nega matnda «я учи́лся» va «я боя́лся» yozilgan, «учи́лась» va "
                        "«боя́лась» emas?",
                "choices": [
                    "Hikoyachi yigit — avval jins qoʻshimchasi, keyin -СЯ qoʻshiladi",
                    "Chunki -СЯ har doim erkak shaklida ishlatiladi",
                    "Chunki bu koʻplik",
                    "Chunki bu hozirgi zamon"
                ],
                "answer": 0,
                "explanation": "Ikki qadam: avval oʻtgan zamon va jins (учи́л- / боя́л-, "
                               "chunki Jasur yigit), keyin qoʻshimcha. Oxirida Л — undosh, "
                               "demak -СЯ. Qiz aytganda «учи́лась, боя́лась» boʻlardi: "
                               "oxirida А — unli, demak -СЬ.",
            },
            {
                "text": "Matnning oxirgi jumlasi nimani anglatadi?",
                "choices": [
                    "Suv emas, qoʻrquv asosiy toʻsiq boʻlgan",
                    "Suv har kuni isib borgan",
                    "Jasur suzishni tashlagan",
                    "Birinchi kun eng osoni boʻlgan"
                ],
                "answer": 0,
                "explanation": "«Вода́ была́ холо́дная то́лько оди́н день… Потом я про́сто "
                               "боя́лся ме́ньше» — suv oʻzgarmadi, Jasur oʻzgardi. "
                               "Hikoya sovuq suv haqida emas, qoʻrquv haqida.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-26 — мочь va уметь                OILA PORTRETI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ба́бушка уме́ет всё",
        "summary": (
            "PR-26 matni. Dilnozaning buvisi hamma narsani biladi, lekin bugun "
            "qoʻllari ogʻriydi. Shuning uchun buvi aytadi, nabiralar qiladi — va "
            "oxirida uning eng katta mahorati maʼlum boʻladi."
        ),
        "order":   26,
        "grammar": [
            {
                "pattern":  "уме́ть — oʻrganilgan mahorat",
                "meaning":  "Bir marta oʻrganilgan va endi doim bor: suzish, tikish, "
                            "ovqat pishirish. Oʻzbekcha tekshiruv: «-ni BILAMAN» "
                            "toʻgʻri kelsa — уме́ть.",
                "examples": ["Ба́бушка уме́ет шить.", "Я уме́ю говори́ть по-ру́сски."],
            },
            {
                "pattern":  "мочь — shu ondagi imkoniyat",
                "meaning":  "Sharoit, kuch, ruxsat, vaqt. Ertaga boshqacha boʻlishi "
                            "mumkin. Oʻzbekcha tekshiruv: «-A OLAMAN» toʻgʻri kelsa — "
                            "мочь. Tuslanishi: могу́ … мо́жешь, мо́жет, мо́жем, "
                            "мо́жете … мо́гут («Г ikki chetda, Ж oʻrtada»).",
                "examples": ["Сего́дня я не могу́.", "Мы мо́жем помога́ть."],
            },
            {
                "pattern":  "Ikkinchi feʼl — infinitivda",
                "meaning":  "Уме́ть va мочь yonidagi feʼl hech qachon tuslanmaydi: "
                            "уме́ю гото́вить, не могу́ шить. Bu PR-19 dan beri "
                            "oʻzgarmayotgan qoida.",
                "examples": ["Бекзо́д уме́ет бы́стро бе́гать."],
            },
        ],
        "body": '''<p>Моя бабушка <strong>уме́ет</strong> всё.</p>

<p>Она <strong>уме́ет</strong> гото́вить плов. Она <strong>уме́ет</strong> <span class="cn-word" data-pos="verb" data-tr="tikmoq">шить</span>. Она <strong>уме́ет</strong> чита́ть <span class="cn-word" data-tr="arabchada">по-ара́бски</span>. Она <strong>уме́ет</strong> <span class="cn-word" data-pos="verb" data-tr="tinglamoq">слу́шать</span> — э́то то́же <span class="cn-word" data-tr="mahorat, hunar">уме́ние</span>.</p>

<p>Мой брат Бекзод <strong>уме́ет</strong> бы́стро <span class="cn-word" data-pos="verb" data-tr="yugurmoq">бе́гать</span>. Я <strong>уме́ю</strong> говори́ть по-ру́сски. Немно́го.</p>

<p>Сегодня суббота. Бабушка хо́чет гото́вить плов. Но бабушка не <strong>мо́жет</strong>.</p>

<p>— <span class="cn-word" data-tr="qoʻllar">Ру́ки</span>, — говори́т бабушка. — Я <strong>уме́ю</strong>, но сегодня не <strong>могу́</strong>.</p>

<p>— Бабушка, я <strong>уме́ю</strong>! — говори́т Бекзод.</p>

<p>Э́то <span class="cn-word" data-tr="yolgʻon, notoʻgʻri">непра́вда</span>. Бекзод не <strong>уме́ет</strong> гото́вить плов. Но он <strong>мо́жет</strong> <span class="cn-word" data-pos="verb" data-tr="yordam bermoq">помога́ть</span>.</p>

<p>Бабушка <span class="cn-word" data-pos="verb" data-tr="oʻtiradi">сиди́т</span> и говори́т. Бекзод и я де́лаем.</p>

<p>— Рис. Вода́. Тепе́рь мя́со, — говори́т бабушка. — Ме́дленно. Плов лю́бит <span class="cn-word" data-tr="vaqt">вре́мя</span>.</p>

<p>Вечером мы еди́м плов. Плов хоро́ший.</p>

<p>Тепе́рь я зна́ю: бабушка <strong>уме́ет</strong> гото́вить, шить и чита́ть по-ара́бски. Но <span class="cn-word" data-tr="eng asosiysi">са́мое гла́вное</span> — бабушка <strong>уме́ет</strong> учи́ть.</p>''',
        "questions": [
            {
                "text": "Nega bugun oshni buvi emas, nabiralari pishirdi?",
                "choices": [
                    "Buvining qoʻllari ogʻriydi — u biladi, lekin bugun qila olmaydi",
                    "Buvi osh pishirishni unutgan",
                    "Bekzod buvidan yaxshiroq pishiradi",
                    "Buvi shanba kuni ishlamaydi"
                ],
                "answer": 0,
                "explanation": "Buvining oʻz gapi butun darsni bir jumlaga jamlaydi: "
                               "«Я уме́ю, но сегодня не могу́» — mahorat joyida, "
                               "imkoniyat esa bugun yoʻq.",
            },
            {
                "text": "«Бекзод не уме́ет гото́вить плов. Но он мо́жет помога́ть» — bu "
                        "ikki gap farqni qanday koʻrsatadi?",
                "choices": [
                    "Mahorati yoʻq (не уме́ет), lekin imkoniyati bor (мо́жет)",
                    "Ikkalasi bir xil maʼnoda",
                    "Birinchisi oʻtgan zamon, ikkinchisi hozirgi",
                    "Bekzod umuman yordam bera olmaydi"
                ],
                "answer": 0,
                "explanation": "Bekzod osh pishirishni oʻrganmagan — demak «не уме́ет». "
                               "Lekin sogʻ, yonida va tayyor — demak «мо́жет помога́ть». "
                               "Bir odamda bittasi boʻlib, ikkinchisi boʻlmasligi "
                               "mumkin.",
            },
            {
                "text": "Matn nima bilan tugaydi va bu nega muhim?",
                "choices": [
                    "Buvining eng katta mahorati — oʻrgatish",
                    "Buvi endi hech narsa qila olmaydi",
                    "Dilnoza osh pishirishni oʻrganmadi",
                    "Bekzod haqiqatan ham osh pishira oladi"
                ],
                "answer": 0,
                "explanation": "«Са́мое гла́вное — бабушка уме́ет учи́ть». Buvi qoʻli "
                               "bilan emas, gapi bilan osh pishirdi: «Рис. Вода́. Тепе́рь "
                               "мя́со». Bu ham уме́ние — oʻrganilgan, yoʻqolmaydigan "
                               "mahorat.",
            },
        ],
    },
]
