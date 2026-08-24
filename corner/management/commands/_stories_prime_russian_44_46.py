# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-44 … PR-46.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 44 — sayohat qaydlari, 45 — tajriba (kunma-kun),
46 — umumiy xat. (41 hikoya, 42 mahalla portreti, 43 yangilik xabari edi.)

Grammatika chegarasi (kumulyativ qoida):
  44-matn: sifatlarning Д./Т./П. shakllari — в большом городе, по
           широкой улице, с молодым водителем.
  45-matn: koʻplik И.п. va Р.п. — matn kunma-kun sanaydi, shuning uchun
           «пять дней», «много книг», «три друга», «деревьев» tabiiy
           chiqadi.
  46-matn: koʻplik Д./В./Т./П. — xat janri butun matnni «друзьям,
           друзьями, о друзьях» ustiga quradi. Oxirgi soʻz — «глазами».

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_44_46.py --author=prime
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
    # PR-44 — sifat Д./Т./П.                    SAYOHAT QAYDLARI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "В большом городе",
        "summary": (
            "PR-44 matni. Kichkina shahardan kelgan odamning katta shahardagi "
            "birinchi kuni. Taksi haydovchisi uni bir qarashda tanib oladi — va "
            "sababi kutilmagan."
        ),
        "order":   44,
        "grammar": [
            {
                "pattern":  "Sifat Предложный'da: -ОМ / -ОЙ",
                "meaning":  "в большом городе, в маленьком кафе — erkak va oʻrta "
                            "jins -ОМ oladi. Ayol jinsi esa -ОЙ: о старой школе.",
                "examples": ["Первый раз в большом городе.", "Я сижу в маленьком кафе."],
            },
            {
                "pattern":  "Sifat Дательный'da: -ОМУ / -ОЙ",
                "meaning":  "по широкой улице (ayol -ОЙ), к новому дому (erkak "
                            "-ОМУ). Predlog Дательный talab qilsa, sifat ham unga "
                            "ergashadi.",
                "examples": ["Я иду по широкой улице."],
            },
            {
                "pattern":  "Sifat Творительный'da: -ЫМ / -ОЙ",
                "meaning":  "с молодым водителем — erkak jins -ЫМ. Tekshiruv: "
                            "savol soʻzining oxiri sifatning oxiri bilan bir xil "
                            "(с каким? — с молодым).",
                "examples": ["Я говорю с молодым водителем."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="birinchi marta">Первый раз</span> в <strong>большом</strong> городе.</p>

<p>Здесь всё большое. <strong>Большие</strong> дома. <strong>Широкие</strong> улицы. И много людей.</p>

<p>Утром я иду по <strong>широкой</strong> улице. Сорок <span class="cn-word" data-tr="daqiqa">минут</span> — и улица не <span class="cn-word" data-pos="verb" data-tr="tugamaydi">кончается</span>.</p>

<p>В такси я говорю <strong>с молодым</strong> <span class="cn-word" data-tr="haydovchi">водителем</span>.</p>

<p>— Вы из <strong>маленького</strong> города? — спрашивает он.</p>

<p>— Да. Как вы знаете?</p>

<p>— Вы смотрите <span class="cn-word" data-tr="tepaga">вверх</span>, — говорит он. — Здесь люди смотрят <span class="cn-word" data-tr="oldinga">вперёд</span>.</p>

<p>Вечером я <span class="cn-word" data-pos="verb" data-tr="oʻtiraman">сижу</span> в <strong>маленьком</strong> <span class="cn-word" data-tr="kafe">кафе</span>. За окном — <strong>большие</strong> дома и <span class="cn-word" data-tr="sariq">жёлтый</span> <span class="cn-word" data-tr="yorugʻlik">свет</span>.</p>

<p>Мне здесь хорошо. Но я думаю о <strong>маленьком</strong> городе. О <strong>моём</strong>.</p>

<p>В <strong>большом</strong> городе можно быть один. В <strong>маленьком</strong> — нельзя.</p>

<p>Это <span class="cn-word" data-tr="ham yaxshi, ham yomon">и хорошо, и плохо</span>.</p>''',
        "questions": [
            {
                "text": "Taksi haydovchisi mehmonni qanday tanib oldi?",
                "choices": [
                    "U tepaga qarab yurardi — mahalliylar esa oldinga qarashadi",
                    "U ruscha gapira olmadi",
                    "U manzilni bilmasdi",
                    "Uning kiyimi boshqacha edi"
                ],
                "answer": 0,
                "explanation": "«Вы смотрите вверх… Здесь люди смотрят вперёд». "
                               "Katta shahar odami binolarga qaramaydi — u ularga "
                               "oʻrganib qolgan.",
            },
            {
                "text": "Nega «в большом городе», lekin «по широкой улице»?",
                "choices": [
                    "Birinchisi Предложный (-ОМ), ikkinchisi Дательный (-ОЙ, ayol jinsi)",
                    "Ikkalasi bir xil kelishik",
                    "Chunki «улица» koʻplikda",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Sifat otga ergashadi. «В городе» — Предложный, erkak "
                               "jins → большом. «По улице» — Дательный, ayol jins → "
                               "широкой. Ayol jinsida -ОЙ toʻrtta kelishikda "
                               "ishlatiladi.",
            },
            {
                "text": "Matnning oxirgi uch jumlasi nimani anglatadi?",
                "choices": [
                    "Katta shaharda yolgʻiz boʻlish mumkin — bu ham afzallik, ham kamchilik",
                    "Katta shahar kichkinasidan yaxshiroq",
                    "Muallif kichkina shaharga qaytmoqchi",
                    "Katta shaharda odamlar yomon"
                ],
                "answer": 0,
                "explanation": "«В большом городе можно быть один. В маленьком — "
                               "нельзя. Это и хорошо, и плохо». Matn tanlov "
                               "qilmaydi — u faqat farqni aytadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-45 — koʻplik И.п. / Р.п.                TAJRIBA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Пять дней без телефона",
        "summary": (
            "PR-45 matni. Besh kunlik tajriba, kunma-kun. Natija kutilganidek "
            "boʻlmadi: kitoblar ham, vaqt ham emas — eshik oldidagi uch doʻst "
            "muhimroq chiqdi."
        ),
        "order":   45,
        "grammar": [
            {
                "pattern":  "Koʻplik Родительный",
                "meaning":  "Son va miqdor soʻzlaridan keyin: пять дней, много книг, "
                            "много часов. Erkak jins -ОВ / -ЕЙ, ayol va oʻrta jins "
                            "esa qoʻshimchasiz qoladi.",
                "examples": ["Пять дней без телефона.", "Много книг, много слов."],
            },
            {
                "pattern":  "Notoʻgʻri koʻpliklar",
                "meaning":  "Baʼzi soʻzlar koʻplikda butunlay oʻzgaradi: дерево → "
                            "деревья → деревьев, друг → друзья → друзей, "
                            "день → дни → дней.",
                "examples": ["Много деревьев.", "Три друга у двери."],
            },
            {
                "pattern":  "2-3-4 ↔ 5+",
                "meaning":  "PR-36 dagi qoida: 2, 3, 4 dan keyin Родительный BIRLIK "
                            "(три друга), 5 va undan yuqori — Родительный KOʻPLIK "
                            "(пять дней).",
                "examples": ["Две книги за два дня.", "Пять дней."],
            },
        ],
        "body": '''<p>Я <span class="cn-word" data-pos="verb" data-tr="qaror qildim">решил</span>: пять <strong>дней</strong> без телефона.</p>

<p><strong>Первый день.</strong> Трудно. Я <span class="cn-word" data-pos="verb" data-tr="qidiraman">ищу</span> телефон десять <strong>раз</strong>. Его нет. Руки <span class="cn-word" data-tr="boʻsh">пустые</span>.</p>

<p><strong>Второй день.</strong> У меня много <strong>времени</strong>. Я читаю <span class="cn-word" data-tr="sekin">медленно</span>. Две <strong>книги</strong> за два дня.</p>

<p><strong>Третий день.</strong> Я не знаю <span class="cn-word" data-tr="yangiliklar">новости</span>. И это нормально.</p>

<p><strong>Четвёртый день.</strong> Я вижу много <strong>деревьев</strong> в нашем дворе. Раньше я их не видел. Они стояли там <span class="cn-word" data-tr="doim">всегда</span>.</p>

<p><strong>Пятый день.</strong> Вечером ко мне <span class="cn-word" data-pos="verb" data-tr="kelishdi">пришли</span> три <strong>друга</strong>.</p>

<p>— У тебя нет телефона, — сказал Бекзод. — Мы <span class="cn-word" data-pos="verb" data-tr="xavotirlandik">волновались</span>.</p>

<p>Пять дней. Много <strong>книг</strong>. Много <strong>часов</strong>. Много <strong>слов</strong> в <span class="cn-word" data-tr="daftar">тетради</span>.</p>

<p>И три <strong>друга</strong> у <span class="cn-word" data-tr="eshik oldida">двери</span>.</p>

<p>Теперь телефон у меня есть. Но он <span class="cn-word" data-pos="verb" data-tr="yotadi">лежит</span> в сумке. И я не ищу его десять раз в день.</p>''',
        "questions": [
            {
                "text": "Tajribaning eng muhim natijasi nima boʻldi?",
                "choices": [
                    "Beshinchi kuni uch doʻsti xavotirlanib kelishdi",
                    "U ikkita kitob oʻqidi",
                    "U yangiliklarni bilmay qoldi",
                    "U hovlidagi daraxtlarni sanadi"
                ],
                "answer": 0,
                "explanation": "Matn kitoblar, soatlar va soʻzlarni sanaydi — keyin "
                               "alohida qatorda: «И три друга у двери». Sanalmaydigan "
                               "natija aynan shu.",
            },
            {
                "text": "Nega «пять дней», lekin «три друга»?",
                "choices": [
                    "5 dan boshlab Родительный koʻplik, 2-3-4 dan keyin esa birlik",
                    "Chunki «друг» jonli",
                    "Chunki «день» erkak jinsida",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "PR-36 qoidasi: 1 → bosh kelishik; 2, 3, 4 → "
                               "Родительный birlik (друга); 5 va undan yuqori → "
                               "Родительный koʻplik (дней).",
            },
            {
                "text": "«Много деревьев» — nega bu shakl gʻalati koʻrinadi?",
                "choices": [
                    "Дерево koʻplikda butunlay oʻzgaradi: деревья → деревьев",
                    "Chunki daraxtlar jonli hisoblanadi",
                    "Chunki bu oʻrta jins",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Bir guruh soʻz koʻplikda -ЬЯ oladi: дерево → "
                               "деревья, брат → братья, стул → стулья. Ularning "
                               "Родительный shakli esa -ЬЕВ boʻladi. Bunday soʻzlar "
                               "qoida bilan emas, yodlab olinadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-46 — koʻplik Д./В./Т./П.                UMUMIY XAT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Письмо всем друзьям",
        "summary": (
            "PR-46 matni. Yil oxirida hamma doʻstlarga yoziladigan umumiy xat. "
            "Butun matn koʻplik kelishiklari ustida turadi — va oxirgi soʻz "
            "«глазами»."
        ),
        "order":   46,
        "grammar": [
            {
                "pattern":  "Koʻplik Д./Т./П.: -АМ, -АМИ, -АХ",
                "meaning":  "Koʻplikda jins yoʻqoladi — uchta jins uchun bitta "
                            "qoʻshimcha. Yumshoq oʻzakda -ЯМ, -ЯМИ, -ЯХ: друзьям, "
                            "друзьями, о друзьях.",
                "examples": ["Пишу всем друзьям.", "Я думаю о старых друзьях."],
            },
            {
                "pattern":  "детьми · людьми",
                "meaning":  "Butun tizimdagi ikkita istisno. «Людями» va «детями» "
                            "emas — людьми va детьми. Ular qofiyalanadi, shuning "
                            "uchun birga yodlanadi.",
                "examples": ["Работаю с разными людьми.", "Я говорю с детьми."],
            },
            {
                "pattern":  "Sifat koʻplikda: -ЫМ, -ЫМИ, -ЫХ",
                "meaning":  "Sifat ham jinsni yoʻqotadi va ot bilan birga oʻzgaradi: "
                            "старым друзьям, с разными людьми, о старых "
                            "друзьях.",
                "examples": ["Спасибо старым друзьям."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Aziz">Дорогие</span> друзья!</p>

<p>Пишу <span class="cn-word" data-tr="hammaga">всем</span> — и <strong>старым друзьям</strong>, и <strong>новым</strong>.</p>

<p>Этот <span class="cn-word" data-tr="yil">год</span> был трудный. Я жил в <strong>двух городах</strong>. Работал <strong>с разными людьми</strong>.</p>

<p>Часто я думал <strong>о старых друзьях</strong>. И <strong>о детях</strong> — мои дети <span class="cn-word" data-pos="verb" data-tr="oʻsyapti">растут</span> быстро.</p>

<p>Я говорю <strong>с ними</strong> по телефону каждую субботу. Это <span class="cn-word" data-tr="oz">мало</span>. Но это есть.</p>

<p>Теперь я хочу сказать <strong>всем</strong> одно слово: спасибо.</p>

<p>Спасибо <strong>старым друзьям</strong> — за письма.</p>

<p>Спасибо <strong>новым</strong> — за <span class="cn-word" data-tr="kechalar">вечера</span> и <span class="cn-word" data-tr="suhbatlar">разговоры</span>.</p>

<p>Спасибо <strong>моим детям</strong> — за <span class="cn-word" data-tr="savollar">вопросы</span>. Они спрашивают <span class="cn-word" data-tr="mendan yaxshiroq">лучше, чем я</span>.</p>

<p>Спасибо <strong>людям</strong> в <strong>двух городах</strong> — за <span class="cn-word" data-tr="sabr">терпение</span>.</p>

<p>В <span class="cn-word" data-tr="keyingi">следующем</span> году я хочу видеть <strong>всех</strong>. Не по телефону.</p>

<p><strong>Глазами</strong>.</p>''',
        "questions": [
            {
                "text": "Xat muallifi kelasi yilda nimani xohlaydi?",
                "choices": [
                    "Hammani telefon orqali emas, oʻz koʻzi bilan koʻrishni",
                    "Ikki shaharda yashashni",
                    "Koʻproq xat yozishni",
                    "Yangi doʻstlar orttirishni"
                ],
                "answer": 0,
                "explanation": "Xat shu ikki jumla bilan tugaydi: «я хочу видеть "
                               "всех. Не по телефону. Глазами». Butun yil telefon "
                               "orqali oʻtdi — shuning uchun oxirgi soʻz shunchalik "
                               "kuchli.",
            },
            {
                "text": "Nega «с разными людьми», «людями» emas?",
                "choices": [
                    "Людьми — butun tizimdagi ikkita istisnodan biri",
                    "Chunki «люди» jonli",
                    "Chunki oldida sifat bor",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Koʻplik Творительный odatda -АМИ / -ЯМИ boʻladi "
                               "(друзьями, городами). Faqat ikkita soʻz boshqacha: "
                               "людьми va детьми. Ular qofiyalanadi.",
            },
            {
                "text": "«Друзьям», «друзьями», «о друзьях» — bu uch shakl nimani "
                        "koʻrsatadi?",
                "choices": [
                    "Koʻplikda jins yoʻqoladi va faqat kelishik qoʻshimchasi qoladi",
                    "Bu uch xil soʻz",
                    "Bu uchta xil doʻstlik turi",
                    "Bu birlik shakllari"
                ],
                "answer": 0,
                "explanation": "Bitta oʻzak (друзь-) va uchta qoʻshimcha: -ЯМ (Д.п.), "
                               "-ЯМИ (Т.п.), -ЯХ (П.п.). Oʻzbekchada ham xuddi "
                               "shunday: doʻst-lar-ga, doʻst-lar-da.",
            },
        ],
    },
]
