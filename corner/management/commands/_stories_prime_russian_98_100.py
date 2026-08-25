# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-98 … PR-100. KURSNING OXIRGI MATNLARI.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.
⛔ URGʻU BELGISI YOʻQ — 2026-08-24 dagi qaror.

Janr xilma-xilligi: 98 — qoʻllanma (koʻrsatma matni), 99 —
ilmiy-ommabop, 100 — oʻquvchiga bevosita murojaat (kursda birinchi
va oxirgi marta ishlatilgan shakl).

Grammatika chegarasi (kumulyativ qoida):
  98-matn: insho qurilishi va bogʻlovchilar — matnning oʻzi
           koʻrsatmaga aylangan.
  99-matn: rus tilining qatlamlari; полногласие kaliti va turkiy
           qatlam.
  100-matn: chegara YOʻQ. Bu — kursning oxirgi matni, shuning uchun
           unda butun kurs grammatikasi erkin ishlatilgan: который,
           деепричастие, вид, шахссиз гап, тире. Aynan shu matn
           oʻquvchiga oʻz darajasini koʻrsatadi.

⚠️ FAKTLAR:
  98 — koʻrsatma matni, daʼvo yoʻq.
  99 — lugʻatlarda keltiriladigan standart etimologiyalar:
       карандаш ← turkiy qora+tosh; изюм ← turkiy uzum;
       богатырь ← turkiy bahodir; сундук ← sandiq; сарай ← saroy;
       деньги ← tanga; вокзал ← London Vauxhall; зонтик ← golland
       zonnedek (undan keyin «зонт» teskari yasalgan).
       Полногласие/неполногласие juftliklari (город/град,
       голова/глава, здоровье/здравствуйте) — rus tili tarixining
       asosiy hodisalaridan.
  100 — toʻqima murojaat, real daʼvo yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_98_100.py --author=prime
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
    # PR-98 — matn qurish                                   QOʻLLANMA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Как написать сочинение",
        "summary": (
            "PR-98 matni. Insho yozishning besh qadami — qoʻllanma shaklida. "
            "Matnning oʻzi ham aynan shu qoidalar boʻyicha qurilgan."
        ),
        "order":   98,
        "grammar": [
            {
                "pattern":  "Вступление — основная часть — заключение",
                "meaning":  "Inshoning uch qismi. Oʻzbekcha kirish — asosiy "
                            "qism — xulosa bilan aynan bir xil.",
                "examples": ["Во вступлении ты называешь тему.",
                             "В заключении ты возвращаешься к тезису."],
            },
            {
                "pattern":  "Связки: во-первых · однако · таким образом",
                "meaning":  "Bogʻlovchi soʻzlar. Ular gaplarni matnga "
                            "aylantiradi.",
                "examples": ["Во-первых, это дорого.",
                             "Таким образом, вывод очевиден."],
            },
            {
                "pattern":  "Один абзац — одна мысль",
                "meaning":  "Abzats qoidasi. Tekshiruv: abzatsni bitta "
                            "jumlada aytib bera olasizmi?",
                "examples": ["Новая мысль — новый абзац."],
            },
        ],
        "body": '''<p>Многие <span class="cn-word" data-pos="verb" data-tr="oʻtirishadi">садятся</span> за сочинение и <span class="cn-word" data-pos="verb" data-tr="qarab qolishadi">смотрят</span> на пустой лист <span class="cn-word" data-tr="yarim soat">полчаса</span>. Проблема почти всегда одна и та же: они <span class="cn-word" data-pos="verb" data-tr="boshlashadi">начинают</span> писать <span class="cn-word" data-tr="oʻylamasdan">не подумав</span>.</p>

<p>Сочинение <span class="cn-word" data-pos="verb" data-tr="qoʻrqitadi">пугает</span> многих. На самом деле это <span class="cn-word" data-tr="ish">работа</span>, у которой есть <span class="cn-word" data-tr="tartib">порядок</span>. Пять шагов — и текст готов.</p>

<p><strong>Шаг первый.</strong> Прочитай тему два раза и <span class="cn-word" data-pos="verb" data-tr="ayt">скажи</span> себе одним предложением, что ты <span class="cn-word" data-pos="verb" data-tr="oʻylaysan">думаешь</span>. Это твой <span class="cn-word" data-tr="asosiy fikr">тезис</span>. Если ты не можешь сказать его одним предложением, писать <span class="cn-word" data-tr="hali erta">ещё рано</span>.</p>

<p><strong>Шаг второй.</strong> <span class="cn-word" data-pos="verb" data-tr="topmoq">Найди</span> два <span class="cn-word" data-tr="dalil">аргумента</span>. Не пять и не один. Два — это <span class="cn-word" data-tr="yetarli">достаточно</span>, и каждый получит свой <span class="cn-word" data-tr="abzats">абзац</span>.</p>

<p><strong>Шаг третий.</strong> <span class="cn-word" data-pos="verb" data-tr="yoz">Напиши</span> вступление: две-три фразы. Сначала <span class="cn-word" data-tr="mavzu">тема</span>, потом тезис. Не начинай <span class="cn-word" data-tr="uzoqdan">издалека</span> — <span class="cn-word" data-tr="tekshiruvchi">проверяющий</span> ищет мысль, а не <span class="cn-word" data-tr="kirish">введение</span> на полстраницы.</p>

<p><strong>Шаг четвёртый.</strong> Основная часть. Каждый абзац начинай со <span class="cn-word" data-tr="bogʻlovchi">связки</span>: <em>во-первых</em>, <em>во-вторых</em>, <em>кроме того</em>. Если есть <span class="cn-word" data-tr="qarshi fikr">возражение</span>, поставь <em>однако</em> — текст сразу станет <span class="cn-word" data-tr="jiddiyroq">серьёзнее</span>.</p>

<p><strong>Шаг пятый.</strong> Заключение. <span class="cn-word" data-pos="verb" data-tr="qayt">Вернись</span> к тезису, но <span class="cn-word" data-tr="boshqa soʻzlar bilan">другими словами</span>. Не <span class="cn-word" data-pos="verb" data-tr="qoʻshma">добавляй</span> новых аргументов и не <span class="cn-word" data-pos="verb" data-tr="kechirim soʻrama">извиняйся</span>.</p>

<p>Между шагами есть <span class="cn-word" data-tr="yana bitta">ещё одно</span> правило, и оно <span class="cn-word" data-tr="eng muhim">самое важное</span>: <span class="cn-word" data-tr="bir abzats">один абзац</span> — <span class="cn-word" data-tr="bir fikr">одна мысль</span>. Если ты не можешь <span class="cn-word" data-pos="verb" data-tr="aytib bermoq">пересказать</span> абзац одним предложением, <span class="cn-word" data-pos="verb" data-tr="ikkiga boʻl">раздели</span> его на два.</p>

<p>И <span class="cn-word" data-tr="oxirgi">последнее</span>. <span class="cn-word" data-pos="verb" data-tr="oʻqi">Прочитай</span> текст вслух. Там, где ты <span class="cn-word" data-pos="verb" data-tr="toʻxtading">запнулся</span>, <span class="cn-word" data-tr="oʻquvchi">читатель</span> запнётся тоже.</p>''',
        "questions": [
            {
                "text": "Matnga koʻra, tezisni qanday tekshirasiz?",
                "choices": [
                    "Uni oʻqituvchiga koʻrsatib",
                    "Uni bitta jumlada ayta olasizmi — shu bilan",
                    "Uni lugʻatdan qarab",
                    "Uni ikki marta yozib"
                ],
                "answer": 1,
                "explanation": "«Скажи себе одним предложением, что ты думаешь… "
                               "Если ты не можешь сказать его одним "
                               "предложением, писать ещё рано». Bitta jumla — "
                               "fikrning tayyorligini bildiradi.",
            },
            {
                "text": "Nega ikkita dalil tavsiya qilinadi — beshta emas?",
                "choices": [
                    "Chunki koʻproq yozish qiyin",
                    "Chunki oʻqituvchi beshtasini oʻqimaydi",
                    "Chunki ikkitasi yetarli va har biri oʻz abzatsini oladi",
                    "Chunki beshta dalil topilmaydi"
                ],
                "answer": 2,
                "explanation": "«Два — это достаточно, и каждый получит свой "
                               "абзац». Bu abzats qoidasi bilan bogʻlangan: bir "
                               "abzats — bir fikr.",
            },
            {
                "text": "Matnning oxirgi maslahati nima va nega u ishlaydi?",
                "choices": [
                    "Matnni ovoz chiqarib oʻqish — toʻxtagan joyingizda oʻquvchi ham toʻxtaydi",
                    "Matnni ertaga qayta oʻqish",
                    "Matnni doʻstingizga berish",
                    "Matnni qisqartirish"
                ],
                "answer": 0,
                "explanation": "«Прочитай текст вслух. Там, где ты запнулся, "
                               "читатель запнётся тоже». Ovoz matndagi "
                               "notekislikni koʻzdan koʻra tezroq topadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-99 — til tarixi                              ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Откуда пришли русские слова",
        "summary": (
            "PR-99 matni. «Здравствуйте» aslida «sogʻ boʻling» degani, "
            "«карандаш» esa «qora tosh». Rus tilining toʻrt qatlami va "
            "ulardan bittasi oʻzbek oʻquvchiga bolaligidan tanish."
        ),
        "order":   99,
        "grammar": [
            {
                "pattern":  "-оро- / -ра-: здоровье → здравствуйте",
                "meaning":  "Ruscha shakl aniq maʼno, kitobiy shakl mavhum "
                            "maʼno oladi: город/град, голова/глава.",
                "examples": ["голова — глава", "сторона — страна"],
            },
            {
                "pattern":  "Тюркский слой",
                "meaning":  "Turkiy qatlam: карандаш, изюм, богатырь, "
                            "сундук, сарай, деньги. Oʻzbek oʻquvchi ularni "
                            "taniydi.",
                "examples": ["карандаш — кара + таш",
                             "богатырь — bahodir"],
            },
            {
                "pattern":  "Европейский слой",
                "meaning":  "XVIII asrdan: golland, fransuz, ingliz. "
                            "Вокзал — London bogʻining nomidan.",
                "examples": ["матрос, компас — голландские",
                             "пальто, балет — французские"],
            },
        ],
        "body": '''<p>Русский язык <span class="cn-word" data-tr="oʻxshaydi">похож</span> на старый дом, который <span class="cn-word" data-pos="verb" data-tr="qurishgan">строили</span> много раз. Каждое <span class="cn-word" data-tr="asr">столетие</span> оставило свой <span class="cn-word" data-tr="qatlam">слой</span>.</p>

<p>Самый старый слой — <span class="cn-word" data-tr="oʻz soʻzlari">свои слова</span>: <em>мать</em>, <em>брат</em>, <em>вода</em>, <em>дом</em>, <em>хлеб</em>. Они короткие и <span class="cn-word" data-tr="issiq">тёплые</span>, и мы их не <span class="cn-word" data-pos="verb" data-tr="sezmaymiz">замечаем</span>.</p>

<p>Второй слой пришёл из <span class="cn-word" data-tr="cherkov kitoblari">церковных книг</span>. Он <span class="cn-word" data-pos="verb" data-tr="qoldirgan">оставил</span> странные <span class="cn-word" data-tr="juftliklar">пары</span>: <em>город</em> и <em>град</em>, <em>голова</em> и <em>глава</em>, <em>сторона</em> и <em>страна</em>.</p>

<p><span class="cn-word" data-tr="qoida">Правило</span> тут простое. Форма с <strong>-оро-</strong> <span class="cn-word" data-pos="verb" data-tr="anglatadi">означает</span> <span class="cn-word" data-tr="aniq narsa">конкретную вещь</span>, форма с <strong>-ра-</strong> — <span class="cn-word" data-tr="mavhum tushuncha">отвлечённое понятие</span>. Поэтому <em>глава книги</em>, но <em>ударился головой</em>.</p>

<p>А теперь <span class="cn-word" data-tr="eng qizigʻi">самое интересное</span>. Слово <strong>здравствуйте</strong> — из этой же пары. Оно от слова <em>здоровье</em> и <span class="cn-word" data-pos="verb" data-tr="anglatadi">значит</span> просто «<span class="cn-word" data-tr="sogʻ boʻling">будьте здоровы</span>».</p>

<p>Третий слой — <span class="cn-word" data-tr="turkiy">тюркский</span>. Тут русский и узбекский <span class="cn-word" data-pos="verb" data-tr="uchrashadi">встречаются</span>.</p>

<p><strong>Карандаш</strong> — это «кара» и «таш», <span class="cn-word" data-tr="qora tosh">чёрный камень</span>. <strong>Богатырь</strong>, герой русских <span class="cn-word" data-tr="ertaklar">сказок</span>, носит тюркское имя. <strong>Изюм</strong> — это «узум», <span class="cn-word" data-tr="uzum">виноград</span>. И ещё <em>сундук</em>, <em>сарай</em>, <em>деньги</em>, <em>базар</em>, <em>амбар</em>.</p>

<p>Четвёртый слой — <span class="cn-word" data-tr="yevropa">европейский</span>. При Петре пришли <em>матрос</em> и <em>компас</em>, позже — <em>пальто</em> и <em>балет</em>, сегодня — <em>компьютер</em> и <em>менеджер</em>.</p>

<p><span class="cn-word" data-tr="shunday qilib">Итак</span>, каждое русское слово <span class="cn-word" data-pos="verb" data-tr="kelgan">пришло</span> откуда-то. И часть из них пришла <span class="cn-word" data-tr="siz tomondan">с вашей стороны</span>.</p>''',
        "questions": [
            {
                "text": "«Здравствуйте» soʻzi qaysi soʻzdan kelib chiqqan?",
                "choices": [
                    "«Здесь» soʻzidan",
                    "«Здоровье» soʻzidan — «sogʻ boʻling» degani",
                    "«Звать» soʻzidan",
                    "Turkiy tildan"
                ],
                "answer": 1,
                "explanation": "«Оно от слова здоровье и значит просто „будьте "
                               "здоровы“». <em>Здоровье</em> — <em>-оро-</em> "
                               "li ruscha shakl, <em>здравствуйте</em> — "
                               "<em>-ра-</em> li kitobiy shakl.",
            },
            {
                "text": "Nega «глава книги», lekin «ударился головой»?",
                "choices": [
                    "Chunki «глава» eskirgan",
                    "Chunki bu ikki xil soʻz",
                    "Chunki -оро- aniq narsani, -ра- mavhum tushunchani bildiradi",
                    "Chunki «голова» faqat ogʻzaki nutqda ishlatiladi"
                ],
                "answer": 2,
                "explanation": "«Форма с -оро- означает конкретную вещь, форма "
                               "с -ра- — отвлечённое понятие». Bosh moddiy — "
                               "<em>головой</em>; bob mavhum — <em>глава</em>.",
            },
            {
                "text": "Matnning oxirgi jumlasi nimani nazarda tutyapti?",
                "choices": [
                    "Rus tili juda qadimiy",
                    "Rus tilida koʻp soʻz bor",
                    "Rus tilini oʻrganish qiyin",
                    "Rus tilidagi soʻzlarning bir qismi turkiy — yaʼni oʻquvchining oʻz tomonidan kelgan"
                ],
                "answer": 3,
                "explanation": "«И часть из них пришла с вашей стороны». "
                               "Карандаш, богатырь, изюм, сундук — oʻzbek "
                               "oʻquvchi bu soʻzlarni yodlamaydi, taniydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-100 — yakun                            OʻQUVCHIGA MUROJAAT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Сто уроков спустя",
        "summary": (
            "PR-100 matni va butun kursning oxirgi matni. Bu hikoya emas — "
            "bu sizga qaratilgan murojaat. Agar uni lugʻatsiz oʻqisangiz, "
            "javob shu matnning oʻzida."
        ),
        "order":   100,
        "grammar": [
            {
                "pattern":  "Весь курс сразу",
                "meaning":  "Bu matnda chegara yoʻq: который, деепричастие, "
                            "феʼl turi, shaxssiz gap, tire — hammasi birga. "
                            "Uni oʻqiy olsangiz, kurs oʻz ishini bajardi.",
                "examples": ["Человек, который дочитал до конца…",
                             "Открыв эту страницу, ты уже знал ответ."],
            },
            {
                "pattern":  "Тире вместо «быть»",
                "meaning":  "Ot bilan ot orasida tire — hozirgi zamonda "
                            "«boʻlmoq» feʼli aytilmaydi.",
                "examples": ["Язык — не гора, а дорога.",
                             "Сто уроков — это только начало."],
            },
            {
                "pattern":  "Ни пуха ни пера! — К чёрту!",
                "meaning":  "Omad tilash va uning yagona toʻgʻri javobi. "
                            "Kursning oxirgi iborasi.",
                "examples": ["Ни пуха ни пера!", "— К чёрту!"],
            },
        ],
        "body": '''<p>Ты <span class="cn-word" data-pos="verb" data-tr="oxirigacha oʻqib chiqding">дочитал до конца</span>. Таких <span class="cn-word" data-tr="koʻp emas">немного</span>.</p>

<p><span class="cn-word" data-pos="verb" data-tr="eslab koʻr">Вспомни</span> первый урок. Там были буквы, и семь из них <span class="cn-word" data-pos="verb" data-tr="aldardi">обманывали</span> тебя: <em>В</em>, <em>Н</em>, <em>Р</em>, <em>С</em>, <em>У</em>, <em>Х</em>, <em>Ы</em>. Ты <span class="cn-word" data-pos="verb" data-tr="oʻqirding">читал</span> медленно, по одному <span class="cn-word" data-tr="boʻgʻin">слогу</span>.</p>

<p>Сейчас ты читаешь этот текст и не <span class="cn-word" data-pos="verb" data-tr="oʻylayapsan">думаешь</span> о буквах <span class="cn-word" data-tr="umuman">вообще</span>.</p>

<p>Потом были <span class="cn-word" data-tr="kelishiklar">падежи</span>. Двадцать два урока. Тогда <span class="cn-word" data-pos="verb" data-tr="tuyulardi">казалось</span>, что их <span class="cn-word" data-pos="verb" data-tr="yodlab boʻlmaydi">невозможно запомнить</span>. Но у тебя было <span class="cn-word" data-tr="ustunlik">преимущество</span>, которого нет у англичанина: в твоём <span class="cn-word" data-tr="ona tili">родном языке</span> падежи тоже есть.</p>

<p>Потом был вид глагола, и <span class="cn-word" data-tr="sifatdosh">причастие</span>, и <span class="cn-word" data-tr="ravishdosh">деепричастие</span>. И вот <span class="cn-word" data-tr="hozir">сейчас</span> в этом тексте они <span class="cn-word" data-pos="verb" data-tr="turibdi">стоят</span> рядом, а ты их даже не <span class="cn-word" data-pos="verb" data-tr="payqamading">заметил</span>.</p>

<p>Это и есть <span class="cn-word" data-tr="natija">результат</span>. Не то, что ты <span class="cn-word" data-pos="verb" data-tr="yodlading">выучил</span> правила. А то, что они <span class="cn-word" data-pos="verb" data-tr="koʻrinmay qoldi">стали невидимыми</span>.</p>

<p>Теперь <span class="cn-word" data-tr="halol gap">честно</span>. Сто уроков — это не <span class="cn-word" data-tr="tugash">конец</span>. Ты хорошо <span class="cn-word" data-pos="verb" data-tr="oʻqiysan">читаешь</span>, <span class="cn-word" data-pos="verb" data-tr="yozasan">пишешь</span> уверенно, но <span class="cn-word" data-pos="verb" data-tr="gapirmading">говорил</span> ты мало. Это <span class="cn-word" data-pos="verb" data-tr="tuzatiladi">лечится</span> только одним: <span class="cn-word" data-tr="suhbat">разговором</span>.</p>

<p><span class="cn-word" data-pos="verb" data-tr="topgin">Найди</span> собеседника. <span class="cn-word" data-pos="verb" data-tr="oʻqi">Читай</span> вслух по десять минут в день. <span class="cn-word" data-pos="verb" data-tr="yoz">Пиши</span> три предложения в <span class="cn-word" data-tr="kundalik">дневник</span> — три, не больше, чтобы не <span class="cn-word" data-pos="verb" data-tr="tashlab qoʻymaslik">бросить</span>.</p>

<p>Язык — не <span class="cn-word" data-tr="togʻ">гора</span>, на которую <span class="cn-word" data-pos="verb" data-tr="chiqasan">поднимаешься</span> один раз. Это <span class="cn-word" data-tr="yoʻl">дорога</span>, по которой <span class="cn-word" data-pos="verb" data-tr="yurasan">идёшь</span>.</p>

<p>Ты уже на ней.</p>

<p><strong>Ни пуха ни пера!</strong></p>''',
        "questions": [
            {
                "text": "Matnga koʻra, oʻrganishning asosiy natijasi nima?",
                "choices": [
                    "Qoidalarni yodlab olish",
                    "Qoidalarning koʻrinmay qolishi — ular haqida oʻylamay oʻqish",
                    "Barcha soʻzlarni bilish",
                    "Imtihon topshirish"
                ],
                "answer": 1,
                "explanation": "«Не то, что ты выучил правила. А то, что они "
                               "стали невидимыми». Grammatika esdan chiqqanda "
                               "emas, koʻrinmay qolganda ishlay boshlaydi.",
            },
            {
                "text": "Matn oʻquvchining qaysi kuchli va qaysi zaif tomonini aytadi?",
                "choices": [
                    "Kuchli — gapirish, zaif — oʻqish",
                    "Kuchli — tinglash, zaif — yozish",
                    "Kuchli — oʻqish va yozish, zaif — gapirish",
                    "Hammasi bir xil darajada"
                ],
                "answer": 2,
                "explanation": "«Ты хорошо читаешь, пишешь уверенно, но "
                               "говорил ты мало. Это лечится только одним: "
                               "разговором». Matn maqtamaydi — halol aytadi.",
            },
            {
                "text": "Nega kundalikka kuniga atigi uchta jumla yozish tavsiya qilinadi?",
                "choices": [
                    "Chunki koʻproq yozishga vaqt yoʻq",
                    "Chunki uch jumla yetarli darajada qiyin",
                    "Chunki oʻqituvchi shuni talab qiladi",
                    "Chunki uchta jumla yozmaslik uchun bahona topilmaydi — shuning uchun tashlab qoʻyilmaydi"
                ],
                "answer": 3,
                "explanation": "«Три, не больше, чтобы не бросить». Kichik "
                               "vaʼda bajariladi; katta vaʼda uchinchi kuni "
                               "tashlab qoʻyiladi.",
            },
        ],
    },
]
