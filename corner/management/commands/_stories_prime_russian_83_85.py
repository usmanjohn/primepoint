# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-83 … PR-85.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.
⛔ URGʻU BELGISI YOʻQ — 2026-08-24 dagi qaror.

Janr xilma-xilligi: 83 — hayot hikoyasi (haqiqiy odam), 84 — jonli
suhbat, 85 — dialog. 84 va 85 ikkalasi ham suhbat, chunki ikkala dars
ham ogʻzaki nutq haqida — lekin shakli boshqa: 84 uch kishilik suhbat
hikoya ichida, 85 esa ikki kishilik toza dialog.

Grammatika chegarasi (kumulyativ qoida):
  83-matn: predloglar — благодаря, из-за, несмотря на, вместо, кроме,
           по, за. Yettalasi ham bir matnda, har biri oʻz kelishigida.
  84-matn: yuklamalar — же, ведь, разве, неужели, ну, вот, даже,
           только, -то (taʼkid).
  85-matn: jonli soʻzlashuv — короче, слушай, значит, Да ладно!,
           Ничего себе!, Давай!, вы не подскажете.

⚠️ ATAY QOCHILGAN (keyingi darslar): soʻz yasalishi tahlili (PR-86),
-тель / -щик suffikslari (PR-87), kichraytirish shakllari (PR-88).

⚠️ FAKTLAR (83-matn — HAQIQIY ODAM):
  Srinivasa Ramanujan (1887–1920), Hindiston. Deyarli oʻz-oʻzidan
  oʻrgangan; Madrasda port boshqarmasida hisobchi boʻlib ishlagan.
  1913-yil yanvarda Kembrijdagi uchta matematikka xat yozgan; ikkitasi
  qogʻozlarni indamay qaytargan, uchinchisi — G. H. Hardi — javob
  bergan. 1914-yilda Angliyaga borgan. 1918-yilda Qirollik jamiyati
  aʼzosi etib saylangan — tarixdagi eng yosh aʼzolardan biri.
  1919-yilda Hindistonga qaytgan va 1920-yilda 32 yoshida vafot etgan.
  1729 haqidagi mashhur voqea: Hardi kasalxonaga kelib, taksi raqami
  «zerikarli» ekanini aytgan; Ramanujan darrov javob bergan — 1729 ikki
  kubning yigʻindisi sifatida ikki xil usulda yozilishi mumkin boʻlgan
  eng kichik son: 1³+12³ = 9³+10³ = 1729. (Tekshirildi: 1+1728 = 1729,
  729+1000 = 1729.)
  84 va 85 — toʻqima suhbatlar, real daʼvo yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_83_85.py --author=prime
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
    # PR-83 — predloglar                              HAYOT HIKOYASI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Благодаря одному письму",
        "summary": (
            "PR-83 matni. Hindistonlik hisobchi Ramanujan 1913-yilda "
            "Kembrijga uchta xat yozdi. Ikkitasi javobsiz qoldi, uchinchisi "
            "matematika tarixini oʻzgartirdi. Faktlar haqiqiy."
        ),
        "order":   83,
        "grammar": [
            {
                "pattern":  "Благодаря + Дат.п. · из-за + Род.п.",
                "meaning":  "Yaxshi sabab va yomon sabab. Sarlavhaning oʻzi "
                            "«благодаря одному письму» — bitta xat tufayli.",
                "examples": ["Благодаря одному письму его жизнь изменилась.",
                             "Из-за болезни он вернулся домой."],
            },
            {
                "pattern":  "Несмотря на + Вин.п.",
                "meaning":  "Oʻzbekcha «qaramay» ning soʻzma-soʻz nusxasi. "
                            "Matnda ikki marta: kasallikka va urushga qaramay.",
                "examples": ["Несмотря на войну, он поехал в Англию.",
                             "Несмотря на болезнь, он продолжал работать."],
            },
            {
                "pattern":  "Вместо · кроме · по · за",
                "meaning":  "«Вместо» va «кроме» — Род.п.; «по» — Дат.п.; «за» "
                            "esa maʼnosiga qarab Вин.п. yoki Твор.п.",
                "examples": ["Кроме Харди, ему не ответил никто.",
                             "Вместо доказательств он прислал только результаты."],
            },
        ],
        "body": '''<p>В январе 1913 года профессор Кембриджа Годфри Харди получил <span class="cn-word" data-tr="xat">письмо</span> из Индии.</p>

<p>Письмо было длинное и <span class="cn-word" data-tr="gʻalati">странное</span>. В нём стояло около ста <span class="cn-word" data-tr="teoremalar">теорем</span> — почти без <span class="cn-word" data-tr="isbotlar">доказательств</span>. <strong>Вместо</strong> доказательств автор <span class="cn-word" data-pos="verb" data-tr="joʻnatdi">прислал</span> <strong>только</strong> <span class="cn-word" data-tr="natijalar">результаты</span>.</p>

<p>Автора звали Сриниваса Рамануджан. Ему было двадцать пять лет. Он работал <span class="cn-word" data-tr="hisobchi">клерком</span> в порту Мадраса и <span class="cn-word" data-pos="verb" data-tr="olardi">получал</span> двадцать <span class="cn-word" data-tr="funt (pul)">фунтов</span> в год. <span class="cn-word" data-tr="oliy maʼlumot">Высшего образования</span> у него не было: он дважды <span class="cn-word" data-pos="verb" data-tr="yiqilgan (imtihondan)">провалил</span> экзамены, потому что <strong>кроме</strong> математики его ничего не <span class="cn-word" data-pos="verb" data-tr="qiziqtirmasdi">интересовало</span>.</p>

<p>Это было <strong>не первое</strong> его письмо. <strong>По</strong> <span class="cn-word" data-tr="maslahatiga koʻra">совету</span> друга он написал троим профессорам в Кембридж. Двое вернули бумаги <span class="cn-word" data-tr="bir soʻz aytmay">без единого слова</span>.</p>

<p>Харди сначала тоже подумал, что это <span class="cn-word" data-tr="hazil">шутка</span>. Он показал письмо <span class="cn-word" data-tr="hamkasbiga">коллеге</span>, и они просидели <strong>за</strong> ним весь вечер.</p>

<p>К ночи Харди сказал <span class="cn-word" data-tr="ibora">фразу</span>, которая вошла в историю: эти формулы <span class="cn-word" data-pos="verb" data-tr="rost boʻlishi kerak">должны быть верны</span>, потому что <strong>придумать</strong> такое <span class="cn-word" data-tr="hech kimning">ни у кого</span> не хватило бы <span class="cn-word" data-tr="tasavvur">воображения</span>.</p>

<p>Он ответил.</p>

<p><strong>Благодаря</strong> этому ответу Рамануджан в 1914 году приехал в Англию — <strong>несмотря на</strong> войну, <strong>несмотря на</strong> <span class="cn-word" data-tr="taqiq">запрет</span> матери и <strong>несмотря на</strong> то, что он никогда не выезжал из Индии.</p>

<p>За пять лет он <span class="cn-word" data-pos="verb" data-tr="chop etdi">опубликовал</span> десятки работ. В 1918 году его выбрали <span class="cn-word" data-tr="aʼzo">членом</span> <span class="cn-word" data-tr="Qirollik jamiyati">Королевского общества</span> — одним из самых молодых за всю его историю.</p>

<p><strong>Из-за</strong> болезни он вернулся домой и умер в 1920 году. Ему было тридцать два.</p>

<p>Есть история, которую любят математики. Харди приехал к нему в больницу и сказал, что ехал на такси номер 1729 — скучное число.</p>

<p>Рамануджан ответил сразу: нет, оно очень интересное. Это <span class="cn-word" data-tr="eng kichik son">самое маленькое число</span>, которое можно записать как <span class="cn-word" data-tr="yigʻindi">сумму</span> двух <span class="cn-word" data-tr="kublar">кубов</span> двумя <span class="cn-word" data-tr="usulda">способами</span>.</p>

<p>1 + 1728. И 729 + 1000.</p>''',
        "questions": [
            {
                "text": "Nega Ramanujanning birinchi ikkita xati javobsiz qoldi?",
                "choices": [
                    "Xatlar yoʻqolib ketgan edi",
                    "U ingliz tilini bilmasdi",
                    "Ikki professor qogʻozlarni bir soʻz aytmay qaytarib yuborishdi",
                    "U notoʻgʻri manzilga yozgan edi"
                ],
                "answer": 2,
                "explanation": "«Двое вернули бумаги без единого слова». Faqat "
                               "uchinchisi — Hardi — javob bergan, va aynan shu "
                               "javob hammasini oʻzgartirgan.",
            },
            {
                "text": "Nega matnda «благодаря этому ответу», lekin «из-за болезни»?",
                "choices": [
                    "Chunki «благодаря» yaxshi natijaga, «из-за» yomon natijaga ishlatiladi",
                    "Chunki ikkalasi ham bir xil kelishikni oladi",
                    "Chunki «из-за» faqat kasallik haqida ishlatiladi",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Javob uni Angliyaga olib keldi — yaxshi natija, "
                               "demak «благодаря» + Дательный. Kasallik uni "
                               "qaytarib yubordi — yomon natija, demak «из-за» "
                               "+ Родительный.",
            },
            {
                "text": "1729 soni nimasi bilan qiziq?",
                "choices": [
                    "Bu Hardining taksi raqami boʻlgani uchun",
                    "U ikki kubning yigʻindisi sifatida ikki xil usulda yozilishi mumkin",
                    "U eng katta tub son",
                    "U Ramanujanning tugʻilgan yili"
                ],
                "answer": 1,
                "explanation": "1 + 1728 = 1³ + 12³, va 729 + 1000 = 9³ + 10³. "
                               "Ikkalasi ham 1729 beradi — va bunday xossaga ega "
                               "eng kichik son shu.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-84 — yuklamalar                                  JONLI SUHBAT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ну и что же?",
        "summary": (
            "PR-84 matni. Uch kursdosh imtihondan keyin koridorda bahslashadi: "
            "birinchisi hammasini bilardi, ikkinchisi hech narsani, uchinchisi "
            "esa savolni umuman boshqacha qoʻyadi."
        ),
        "order":   84,
        "grammar": [
            {
                "pattern":  "Же · ведь — taʼkid va umumiy bilim",
                "meaning":  "«Же» = oʻzbekcha «-ku» («Aytdim-ku!»). «Ведь» — "
                            "«axir, oʻzing bilasan». Ikkalasi ham maʼno emas, "
                            "munosabat qoʻshadi.",
                "examples": ["Я же говорил, что будет вопрос про падежи!",
                             "Ты ведь тоже не читал последнюю главу."],
            },
            {
                "pattern":  "Разве · неужели — hayrat",
                "meaning":  "«Разве» — «rostdanmi?», yumshoqroq. «Неужели» — "
                            "«nahotki», kuchli ishonmaslik.",
                "examples": ["Разве это был не последний вопрос?",
                             "Неужели ты всё выучил за одну ночь?"],
            },
            {
                "pattern":  "Ну · вот · даже · -то (taʼkid)",
                "meaning":  "Jonli nutqning tayanchi. «Я-то знаю» dagi -то — "
                            "taʼkid, PR-78 dagi noaniqlik emas.",
                "examples": ["Ну и что же теперь делать?",
                             "Я-то знаю, а вот он — нет."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="imtihon">Экзамен</span> <span class="cn-word" data-pos="verb" data-tr="tugadi">закончился</span> в час дня. В <span class="cn-word" data-tr="yoʻlakda">коридоре</span> стояли трое: Дилноза, Бекзод и Жасур.</p>

<p>— <strong>Ну</strong> что, как? — спросил Жасур.</p>

<p>— <strong>Неужели</strong> ты не понял? — Дилноза села на <span class="cn-word" data-tr="deraza tokchasi">подоконник</span>. — Я <strong>же</strong> говорила, что будет вопрос про <span class="cn-word" data-tr="kelishiklar">падежи</span>. Я <strong>же</strong> всем говорила.</p>

<p>— Говорила, — <span class="cn-word" data-pos="verb" data-tr="rozi boʻldi">согласился</span> Бекзод. — <strong>Только</strong> ты это сказала за пять минут <span class="cn-word" data-tr="…dan oldin">до</span> экзамена.</p>

<p>— <strong>Ведь</strong> <span class="cn-word" data-tr="kech boʻlsa ham, hech boʻlmagandan yaxshi">лучше поздно, чем никогда</span>.</p>

<p>Жасур молчал. Он смотрел в <span class="cn-word" data-tr="deraza">окно</span> и <span class="cn-word" data-pos="verb" data-tr="sanardi">считал</span> что-то на пальцах.</p>

<p>— <strong>Разве</strong> это был не последний вопрос? — спросил он <span class="cn-word" data-tr="nihoyat">наконец</span>. — Я думал, их <strong>всего</strong> двадцать.</p>

<p>— Двадцать один, — сказала Дилноза. — <strong>Вот</strong> в этом и <span class="cn-word" data-tr="butun gap shunda">всё дело</span>.</p>

<p>— <strong>Ну и что же</strong> теперь? — Бекзод <span class="cn-word" data-pos="verb" data-tr="yelka qisdi">пожал плечами</span>. — <span class="cn-word" data-tr="qayta topshiruv">Пересдача</span> через две недели.</p>

<p>— <strong>Даже</strong> если пересдача, — сказала Дилноза, — я <span class="cn-word" data-tr="baribir">всё равно</span> не понимаю <span class="cn-word" data-tr="kelishiklarni">падежи</span>.</p>

<p>Наступила <span class="cn-word" data-tr="jimlik">тишина</span>.</p>

<p>— <strong>Я-то</strong> думал, ты их знаешь, — сказал Жасур. — Ты <strong>ведь</strong> всё время про них говоришь.</p>

<p>— Говорю. Но говорить и понимать — <span class="cn-word" data-tr="turli narsalar">разные вещи</span>.</p>

<p>Бекзод <span class="cn-word" data-pos="verb" data-tr="kuldi">засмеялся</span> первым. <strong>Ну</strong> а <strong>потом</strong> засмеялись все трое, <span class="cn-word" data-tr="chunki ular biladiki">потому что знали</span>: через две недели они будут сидеть здесь <strong>же</strong> и говорить то <strong>же</strong> самое.</p>''',
        "questions": [
            {
                "text": "Nega Bekzod Dilnozaning gapiga eʼtiroz bildirdi?",
                "choices": [
                    "Chunki Dilnoza hech narsa aytmagan edi",
                    "Chunki Dilnoza buni imtihondan atigi besh daqiqa oldin aytgan",
                    "Chunki savol kelishiklar haqida emas edi",
                    "Chunki Bekzod imtihonga kirmagan"
                ],
                "answer": 1,
                "explanation": "«Только ты это сказала за пять минут до "
                               "экзамена». Dilnoza haq edi, lekin ogohlantirish "
                               "juda kech kelgan.",
            },
            {
                "text": "«Я-то думал, ты их знаешь» — bu yerdagi -то nima vazifa bajaryapti?",
                "choices": [
                    "Noaniqlik: «kimdir oʻylagan»",
                    "Savol yasayapti",
                    "Taʼkid: «men-ku oʻylagandim»",
                    "Inkor qilyapti"
                ],
                "answer": 2,
                "explanation": "Bu yuklama -то, PR-78 dagi noaniqlik emas. U "
                               "oddiy olmoshga yopishib, uni ajratib "
                               "koʻrsatadi: «men-ku shunday oʻylagandim, sen "
                               "esa…».",
            },
            {
                "text": "Nega uchalasi oxirida kulib yuborishdi?",
                "choices": [
                    "Chunki imtihondan oʻtishdi",
                    "Chunki Jasur hazil qildi",
                    "Chunki qayta topshiruv bekor qilindi",
                    "Chunki ikki haftadan keyin ham shu yerda, shu gapni aytishlarini bilishardi"
                ],
                "answer": 3,
                "explanation": "«Через две недели они будут сидеть здесь же и "
                               "говорить то же самое». Ikkala «же» ham "
                               "aynanlikni bildiradi — oʻsha joy, oʻsha gap.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-85 — jonli soʻzlashuv                                  DIALOG
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Разговор в такси",
        "summary": (
            "PR-85 matni. Toshkentdan kelgan yoʻlovchi va moskvalik haydovchi "
            "oʻrtasidagi yigirma daqiqalik suhbat — kitobdagi rus tili bilan "
            "koʻchadagi rus tili uchrashadigan joy."
        ),
        "order":   85,
        "grammar": [
            {
                "pattern":  "Toʻldiruvchilar: короче · слушай · значит",
                "meaning":  "Jonli nutqning tayanchi. «Короче» uzun gapni "
                            "yakunlaydi, «слушай» yangi mavzu boshlaydi, "
                            "«значит» tushuntirishga oʻtadi.",
                "examples": ["Слушай, а ты откуда?",
                             "Короче, приехал и остался."],
            },
            {
                "pattern":  "Javoblar: Да ладно! · Ничего себе! · Ясно",
                "meaning":  "Butun holda yodlanadigan undovlar. «Ничего себе» "
                            "soʻzma-soʻz hech narsani anglatmaydi — u shunchaki "
                            "«Voy-boʻy!».",
                "examples": ["Да ладно! Серьёзно?", "Ничего себе!"],
            },
            {
                "pattern":  "Давай! — norasmiy xayrlashuv",
                "meaning":  "«Давай» bu yerda «ber» emas, «xayr» degani. Faqat "
                            "tengdosh yoki doʻst bilan.",
                "examples": ["— Ну всё, давай! — Давай, спасибо!"],
            },
        ],
        "body": '''<p>— Здравствуйте. На Ленинградский вокзал, пожалуйста.</p>

<p>— Садитесь. <span class="cn-word" data-tr="yumshoq soʻrash: aytib yubormaysizmi">Не подскажете</span>, вам к какому <span class="cn-word" data-tr="chiqish, podyezd">подъезду</span>?</p>

<p>— Я не знаю. Я первый раз.</p>

<p>— <strong>Слушай</strong>, а ты откуда? <span class="cn-word" data-tr="talaffuz">Акцент</span> интересный.</p>

<p>— Из Ташкента.</p>

<p>— <strong>Да ладно!</strong> У меня <span class="cn-word" data-tr="qaynonam">тёща</span> из Ташкента. <strong>Значит</strong>, земляки почти.</p>

<p>Машина выехала на <span class="cn-word" data-tr="koʻchaga">проспект</span>. Было полпятого, и <span class="cn-word" data-tr="tirbandlik">пробка</span> стояла до самого моста.</p>

<p>— <strong>Ничего себе</strong>, — сказал пассажир. — Это надолго?</p>

<p>— Минут сорок. <strong>Короче</strong>, успеем, не волнуйтесь. У вас поезд <strong>во сколько</strong>?</p>

<p>— В семь.</p>

<p>— <strong>Ну</strong> тогда вообще спокойно.</p>

<p>Помолчали. Водитель <span class="cn-word" data-pos="verb" data-tr="oʻchirdi">выключил</span> радио.</p>

<p>— <strong>Слушай</strong>, а <strong>щас</strong> в Ташкенте жарко?</p>

<p>— Тридцать пять.</p>

<p>— <span class="cn-word" data-tr="voy">Ох</span>. <strong>А</strong> у нас <span class="cn-word" data-tr="oʻn beshga zoʻrgʻa yetadi">пятнадцать еле-еле</span>. <strong>Вот</strong> так и живём.</p>

<p>Пассажир засмеялся. Он <span class="cn-word" data-pos="verb" data-tr="payqadi">заметил</span>, что водитель говорит «щас», а не «сейчас», и что это <span class="cn-word" data-tr="umuman qiyin emas">совсем не трудно</span> понять.</p>

<p>Вокзал показался через тридцать восемь минут.</p>

<p>— <strong>Вот и всё</strong>, — сказал водитель. — <span class="cn-word" data-tr="yetib keldik">Приехали</span>. Тёще <span class="cn-word" data-tr="salom ayting">привет передавай</span>, если что.</p>

<p>— Она <strong>же</strong> ваша, не моя.</p>

<p>— <strong>Ну и что?</strong> — <span class="cn-word" data-pos="verb" data-tr="qoʻl siltadi">махнул рукой</span> водитель. — <strong>Ну всё, давай!</strong></p>

<p>— <strong>Давай</strong>. Спасибо.</p>''',
        "questions": [
            {
                "text": "Haydovchi nega yoʻlovchiga «земляки почти» dedi?",
                "choices": [
                    "Chunki ular bir maktabda oʻqishgan",
                    "Chunki uning qaynonasi Toshkentdan",
                    "Chunki ikkalasi ham Moskvada tugʻilgan",
                    "Chunki ular qoʻshni uyda yashashadi"
                ],
                "answer": 1,
                "explanation": "«У меня тёща из Ташкента. Значит, земляки "
                               "почти». Bu — jonli nutqda tanishuvni "
                               "boshlashning odatiy yoʻli.",
            },
            {
                "text": "Yoʻlovchi haydovchining nutqida nimani payqadi?",
                "choices": [
                    "U «щас» deydi, «сейчас» emas — va buni tushunish qiyin emas ekan",
                    "U juda tez gapiradi",
                    "U notoʻgʻri kelishiklarni ishlatadi",
                    "U faqat rasmiy soʻzlarni ishlatadi"
                ],
                "answer": 0,
                "explanation": "«Заметил, что водитель говорит „щас“, а не "
                               "„сейчас“, и что это совсем не трудно понять». "
                               "Ogʻzaki qisqarish — boshqa til emas, oʻsha til "
                               "tez gapirilgani.",
            },
            {
                "text": "Suhbat oxiridagi «Давай!» nimani anglatadi?",
                "choices": [
                    "Pulni bering",
                    "Boshlang",
                    "Xayr — norasmiy xayrlashuv",
                    "Yordam bering"
                ],
                "answer": 2,
                "explanation": "«Давай» bu yerda feʼl emas, xayrlashuv. Yoʻlovchi "
                               "ham shunday javob beradi: «Давай. Спасибо». "
                               "Rasmiy holatda esa «до свидания» aytilardi.",
            },
        ],
    },
]
