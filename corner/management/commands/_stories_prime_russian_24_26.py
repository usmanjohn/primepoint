# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-24 … PR-26.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 24 — xat, 25 — biografik hikoya, 26 — oila portreti.
(21 intervyu, 22 sahna, 23 kundalik daftar edi — hech qaysisi takrorlanmadi.)

Grammatika chegarasi (kumulyativ qoida):
  24-matn: kelasi zamon буду + infinitiv (PR-24). Qaytim feʼllar YOʻQ
           (PR-25), мочь/уметь YOʻQ (PR-26).
  25-matn: -ся / -сь feʼllari (PR-25) oʻtgan zamonda. Hikoyachi — yigit,
           shuning uchun учился / боялся / старался. Мочь va уметь hali
           yoʻq, shuning uchun «suza olmasdim» oʻrniga «боялся» ishlatilgan.
  26-matn: уметь va мочь (PR-26) — butun matn shu ikkisining farqi ustiga
           qurilgan.

Kelishiklar hali oʻrgatilmagan (PR-29 dan): matnlar bosh kelishikda, «в
школу», «у меня», «каждую субботу» kabi iboralar butun boʻlak sifatida
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
        "title":   "Завтра экзамен",
        "summary": (
            "PR-24 matni. Afsona buvisiga xat yozadi: ertaga imtihon, bugun "
            "tayyorgarlik, shanbada qoʻngʻiroq va yozda birga choy. Butun xat "
            "kelasi zamon ustiga qurilgan."
        ),
        "order":   24,
        "grammar": [
            {
                "pattern":  "буду + infinitiv",
                "meaning":  "Kelasi zamon ikki soʻzdan iborat: tuslanadigan yordamchi "
                            "feʼl (буду, будешь, будет, будем, будете, будут) va "
                            "oʻzgarmagan infinitiv. Faqat birinchi soʻz tuslanadi.",
                "examples": ["Я буду читать весь день.", "Мы будем пить чай."],
            },
            {
                "pattern":  "Yolgʻiz буду — «boʻlaman»",
                "meaning":  "Agar gapda boshqa feʼl boʻlmasa, буду oʻzi kesim boʻladi: "
                            "Я буду дома. Завтра будет дождь. Yoniga yana «быть» "
                            "qoʻshilmaydi.",
                "examples": ["Летом я буду в Самарканде.", "Завтра будет дождь."],
            },
            {
                "pattern":  "не буду",
                "meaning":  "Inkor tuslanadigan feʼlning oldiga tushadi — infinitivning "
                            "emas. Toʻgʻri: «я не буду спешить», notoʻgʻri: «я буду не "
                            "спешить».",
                "examples": ["Я не буду спешить."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Aziz, qadrli">Дорогая</span> бабушка!</p>

<p>Завтра <span class="cn-word" data-tr="menda ... bor">у меня</span> <span class="cn-word" data-tr="imtihon">экзамен</span>. Русский язык.</p>

<p>Сегодня я <strong>буду</strong> читать весь день. Потом я <strong>буду</strong> писать слова. Вечером я <strong>буду</strong> спать рано. Я не <strong>буду</strong> <span class="cn-word" data-pos="verb" data-tr="shoshmoq">спешить</span>.</p>

<p>Вчера я читала три часа. Это было трудно. Но сегодня <strong>будет</strong> хорошо — я знаю.</p>

<p>Мама говорит: «Завтра <strong>будет</strong> дождь». <span class="cn-word" data-tr="Hechqisi yoʻq">Ничего</span>. Зонт у меня есть.</p>

<p>Бабушка, я <span class="cn-word" data-pos="verb" data-tr="vaʼda beraman">обещаю</span>: в субботу я <strong>буду</strong> звонить. И потом <strong>буду</strong> звонить <span class="cn-word" data-tr="har shanba">каждую субботу</span>. <span class="cn-word" data-tr="albatta">Обязательно</span>.</p>

<p>А <span class="cn-word" data-tr="yozda">летом</span> я <strong>буду</strong> в Самарканде. Мы <strong>будем</strong> пить чай и говорить. Долго.</p>

<p>Экзамен — завтра. А чай — <span class="cn-word" data-tr="yozda">летом</span>. Я <strong>буду</strong> думать о чае.</p>

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
                "explanation": "«Я обещаю: в субботу я буду звонить. И потом буду "
                               "звонить каждую субботу. Обязательно» — vaʼda aynan "
                               "qoʻngʻiroq haqida.",
            },
            {
                "text": "«Я буду читать» va «Я буду в Самарканде» — nega birinchisida "
                        "ikkita feʼl bor, ikkinchisida bittasi?",
                "choices": [
                    "Ikkinchisida infinitiv kerak emas — буду oʻzi «boʻlaman» degani",
                    "Ikkinchisi oʻtgan zamon",
                    "Bu xato, ikkinchisida ham infinitiv boʻlishi kerak",
                    "Birinchisi hozirgi zamon"
                ],
                "answer": 0,
                "explanation": "Agar gapda boshqa feʼl boʻlsa, u infinitivda qoladi: "
                               "«буду читать». Agar boshqa feʼl boʻlmasa, «буду» ning "
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
                "explanation": "«Экзамен — завтра. А чай — летом. Я буду думать о "
                               "чае» — Afsona ertangi tashvishni yozgi quvonch bilan "
                               "yonma-yon qoʻyadi. Xat imtihon haqida boshlanib, "
                               "buvisi bilan koʻrishish haqida tugaydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-25 — qaytim feʼllar              BIOGRAFIK HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Как я учился плавать",
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
                            "keyin -СЬ (учусь, стараюсь), undoshdan keyin -СЯ "
                            "(учится, боялся). Oʻzbekchadagi -(i)n- ga oʻxshaydi: "
                            "yuv-in-moq.",
                "examples": ["Я учился плавать.", "Шербек смеялся."],
            },
            {
                "pattern":  "Oʻtgan zamonda: учился / училась",
                "meaning":  "Avval jins qoʻshimchasi, keyin -ся/-сь. Erkak: учил+СЯ "
                            "(Л — undosh). Ayol: учила+СЬ (А — unli). Koʻplik: "
                            "учили+СЬ.",
                "examples": ["Я боялся.", "Мы учились вместе."],
            },
            {
                "pattern":  "Faqat -ся bilan yashaydigan feʼllar",
                "meaning":  "Смеяться, бояться, стараться, улыбаться, находиться — "
                            "bu feʼllar -ся siz umuman mavjud emas. «Он смеёт» degan "
                            "shakl yoʻq.",
                "examples": ["Я старался.", "Река находится далеко."],
            },
        ],
        "body": '''<p>Это было <span class="cn-word" data-tr="ancha oldin">давно</span>. Я <strong>учился</strong> плавать <span class="cn-word" data-tr="qishloqda">в деревне</span>. Там была <span class="cn-word" data-tr="daryo">река</span>.</p>

<p>Первый день. Вода была холодная. Я <strong>боялся</strong>.</p>

<p>Мой брат Шербек <strong>смеялся</strong>. Шербек плавал хорошо.</p>

<p>— Жасур, вода <span class="cn-word" data-tr="iliq">тёплая</span>, — говорил Шербек. — Я <strong>учился</strong> три дня. И ты <strong>будешь</strong> плавать.</p>

<p>Второй день. Я <strong>старался</strong>. Один <span class="cn-word" data-tr="marta">раз</span>. Потом ещё раз. Потом ещё. Вода была <span class="cn-word" data-tr="hamma joyda">везде</span>. Шербек <strong>смеялся</strong> <span class="cn-word" data-tr="yana">снова</span>.</p>

<p>Третий день. Я <strong>учился</strong> утром. Потом я <strong>учился</strong> вечером. Я <strong>старался</strong> и <span class="cn-word" data-pos="verb" data-tr="jim turdim">молчал</span>.</p>

<p>Четвёртый день. Я <span class="cn-word" data-pos="verb" data-tr="suzdim">плыл</span>! Три <span class="cn-word" data-tr="metr">метра</span>. Потом пять.</p>

<p>Шербек не <strong>смеялся</strong>. Шербек <strong>улыбался</strong>.</p>

<p>Теперь я живу в Ташкенте. Река <strong>находится</strong> далеко. Но я <span class="cn-word" data-pos="verb" data-tr="eslayman">помню</span> эту воду.</p>

<p>Вода была холодная только один день. Первый. Потом я <span class="cn-word" data-tr="shunchaki">просто</span> <strong>боялся</strong> <span class="cn-word" data-tr="kamroq">меньше</span>.</p>''',
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
                "explanation": "«Шербек не смеялся. Шербек улыбался» — kulish oʻrnini "
                               "jilmayish egalladi. Bu ikki soʻzning farqi butun "
                               "hikoyaning tugashi: masxara emas, quvonch.",
            },
            {
                "text": "Nega matnda «я учился» va «я боялся» yozilgan, «училась» va "
                        "«боялась» emas?",
                "choices": [
                    "Hikoyachi yigit — avval jins qoʻshimchasi, keyin -СЯ qoʻshiladi",
                    "Chunki -СЯ har doim erkak shaklida ishlatiladi",
                    "Chunki bu koʻplik",
                    "Chunki bu hozirgi zamon"
                ],
                "answer": 0,
                "explanation": "Ikki qadam: avval oʻtgan zamon va jins (учил- / боял-, "
                               "chunki Jasur yigit), keyin qoʻshimcha. Oxirida Л — undosh, "
                               "demak -СЯ. Qiz aytganda «училась, боялась» boʻlardi: "
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
                "explanation": "«Вода была холодная только один день… Потом я просто "
                               "боялся меньше» — suv oʻzgarmadi, Jasur oʻzgardi. "
                               "Hikoya sovuq suv haqida emas, qoʻrquv haqida.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-26 — мочь va уметь                OILA PORTRETI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Бабушка умеет всё",
        "summary": (
            "PR-26 matni. Dilnozaning buvisi hamma narsani biladi, lekin bugun "
            "qoʻllari ogʻriydi. Shuning uchun buvi aytadi, nabiralar qiladi — va "
            "oxirida uning eng katta mahorati maʼlum boʻladi."
        ),
        "order":   26,
        "grammar": [
            {
                "pattern":  "уметь — oʻrganilgan mahorat",
                "meaning":  "Bir marta oʻrganilgan va endi doim bor: suzish, tikish, "
                            "ovqat pishirish. Oʻzbekcha tekshiruv: «-ni BILAMAN» "
                            "toʻgʻri kelsa — уметь.",
                "examples": ["Бабушка умеет шить.", "Я умею говорить по-русски."],
            },
            {
                "pattern":  "мочь — shu ondagi imkoniyat",
                "meaning":  "Sharoit, kuch, ruxsat, vaqt. Ertaga boshqacha boʻlishi "
                            "mumkin. Oʻzbekcha tekshiruv: «-A OLAMAN» toʻgʻri kelsa — "
                            "мочь. Tuslanishi: могу … можешь, может, можем, "
                            "можете … могут («Г ikki chetda, Ж oʻrtada»).",
                "examples": ["Сегодня я не могу.", "Мы можем помогать."],
            },
            {
                "pattern":  "Ikkinchi feʼl — infinitivda",
                "meaning":  "Уметь va мочь yonidagi feʼl hech qachon tuslanmaydi: "
                            "умею готовить, не могу шить. Bu PR-19 dan beri "
                            "oʻzgarmayotgan qoida.",
                "examples": ["Бекзод умеет быстро бегать."],
            },
        ],
        "body": '''<p>Моя бабушка <strong>умеет</strong> всё.</p>

<p>Она <strong>умеет</strong> готовить плов. Она <strong>умеет</strong> <span class="cn-word" data-pos="verb" data-tr="tikmoq">шить</span>. Она <strong>умеет</strong> читать <span class="cn-word" data-tr="arabchada">по-арабски</span>. Она <strong>умеет</strong> <span class="cn-word" data-pos="verb" data-tr="tinglamoq">слушать</span> — это тоже <span class="cn-word" data-tr="mahorat, hunar">умение</span>.</p>

<p>Мой брат Бекзод <strong>умеет</strong> быстро <span class="cn-word" data-pos="verb" data-tr="yugurmoq">бегать</span>. Я <strong>умею</strong> говорить по-русски. Немного.</p>

<p>Сегодня суббота. Бабушка хочет готовить плов. Но бабушка не <strong>может</strong>.</p>

<p>— <span class="cn-word" data-tr="qoʻllar">Руки</span>, — говорит бабушка. — Я <strong>умею</strong>, но сегодня не <strong>могу</strong>.</p>

<p>— Бабушка, я <strong>умею</strong>! — говорит Бекзод.</p>

<p>Это <span class="cn-word" data-tr="yolgʻon, notoʻgʻri">неправда</span>. Бекзод не <strong>умеет</strong> готовить плов. Но он <strong>может</strong> <span class="cn-word" data-pos="verb" data-tr="yordam bermoq">помогать</span>.</p>

<p>Бабушка <span class="cn-word" data-pos="verb" data-tr="oʻtiradi">сидит</span> и говорит. Бекзод и я делаем.</p>

<p>— Рис. Вода. Теперь мясо, — говорит бабушка. — Медленно. Плов любит <span class="cn-word" data-tr="vaqt">время</span>.</p>

<p>Вечером мы едим плов. Плов хороший.</p>

<p>Теперь я знаю: бабушка <strong>умеет</strong> готовить, шить и читать по-арабски. Но <span class="cn-word" data-tr="eng asosiysi">самое главное</span> — бабушка <strong>умеет</strong> учить.</p>''',
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
                               "«Я умею, но сегодня не могу» — mahorat joyida, "
                               "imkoniyat esa bugun yoʻq.",
            },
            {
                "text": "«Бекзод не умеет готовить плов. Но он может помогать» — bu "
                        "ikki gap farqni qanday koʻrsatadi?",
                "choices": [
                    "Mahorati yoʻq (не умеет), lekin imkoniyati bor (может)",
                    "Ikkalasi bir xil maʼnoda",
                    "Birinchisi oʻtgan zamon, ikkinchisi hozirgi",
                    "Bekzod umuman yordam bera olmaydi"
                ],
                "answer": 0,
                "explanation": "Bekzod osh pishirishni oʻrganmagan — demak «не умеет». "
                               "Lekin sogʻ, yonida va tayyor — demak «может помогать». "
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
                "explanation": "«Самое главное — бабушка умеет учить». Buvi qoʻli "
                               "bilan emas, gapi bilan osh pishirdi: «Рис. Вода. Теперь "
                               "мясо». Bu ham умение — oʻrganilgan, yoʻqolmaydigan "
                               "mahorat.",
            },
        ],
    },
]
