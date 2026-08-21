# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-44 … PR-46.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 44 — sayohat qaydlari, 45 — tajriba (kunma-kun),
46 — umumiy xat. (41 hikoya, 42 mahalla portreti, 43 yangilik xabari edi.)

Grammatika chegarasi (kumulyativ qoida):
  44-matn: sifatlarning Д./Т./П. shakllari — в большо́м го́роде, по
           широ́кой у́лице, с молоды́м води́телем.
  45-matn: koʻplik И.п. va Р.п. — matn kunma-kun sanaydi, shuning uchun
           «пять дней», «мно́го книг», «три дру́га», «дере́вьев» tabiiy
           chiqadi.
  46-matn: koʻplik Д./В./Т./П. — xat janri butun matnni «друзья́м,
           друзья́ми, о друзья́х» ustiga quradi. Oxirgi soʻz — «глаза́ми».

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
        "title":   "В большо́м го́роде",
        "summary": (
            "PR-44 matni. Kichkina shahardan kelgan odamning katta shahardagi "
            "birinchi kuni. Taksi haydovchisi uni bir qarashda tanib oladi — va "
            "sababi kutilmagan."
        ),
        "order":   44,
        "grammar": [
            {
                "pattern":  "Sifat Предло́жный'da: -ОМ / -ОЙ",
                "meaning":  "в большо́м го́роде, в ма́леньком кафе́ — erkak va oʻrta "
                            "jins -ОМ oladi. Ayol jinsi esa -ОЙ: о ста́рой шко́ле.",
                "examples": ["Пе́рвый раз в большо́м го́роде.", "Я сижу́ в ма́леньком кафе́."],
            },
            {
                "pattern":  "Sifat Да́тельный'da: -ОМУ / -ОЙ",
                "meaning":  "по широ́кой у́лице (ayol -ОЙ), к но́вому до́му (erkak "
                            "-ОМУ). Predlog Да́тельный talab qilsa, sifat ham unga "
                            "ergashadi.",
                "examples": ["Я иду́ по широ́кой у́лице."],
            },
            {
                "pattern":  "Sifat Твори́тельный'da: -ЫМ / -ОЙ",
                "meaning":  "с молоды́м води́телем — erkak jins -ЫМ. Tekshiruv: "
                            "savol soʻzining oxiri sifatning oxiri bilan bir xil "
                            "(с каки́м? — с молоды́м).",
                "examples": ["Я говорю́ с молоды́м води́телем."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="birinchi marta">Пе́рвый раз</span> в <strong>большо́м</strong> го́роде.</p>

<p>Здесь всё большо́е. <strong>Больши́е</strong> дома́. <strong>Широ́кие</strong> у́лицы. И мно́го люде́й.</p>

<p>Утром я иду́ по <strong>широ́кой</strong> у́лице. Со́рок <span class="cn-word" data-tr="daqiqa">мину́т</span> — и у́лица не <span class="cn-word" data-pos="verb" data-tr="tugamaydi">конча́ется</span>.</p>

<p>В такси́ я говорю́ <strong>с молоды́м</strong> <span class="cn-word" data-tr="haydovchi">води́телем</span>.</p>

<p>— Вы из <strong>ма́ленького</strong> го́рода? — спра́шивает он.</p>

<p>— Да. Как вы зна́ете?</p>

<p>— Вы смо́трите <span class="cn-word" data-tr="tepaga">вверх</span>, — говори́т он. — Здесь лю́ди смо́трят <span class="cn-word" data-tr="oldinga">вперёд</span>.</p>

<p>Ве́чером я <span class="cn-word" data-pos="verb" data-tr="oʻtiraman">сижу́</span> в <strong>ма́леньком</strong> <span class="cn-word" data-tr="kafe">кафе́</span>. За окно́м — <strong>больши́е</strong> дома́ и <span class="cn-word" data-tr="sariq">жёлтый</span> <span class="cn-word" data-tr="yorugʻlik">свет</span>.</p>

<p>Мне здесь хорошо́. Но я ду́маю о <strong>ма́леньком</strong> го́роде. О <strong>моём</strong>.</p>

<p>В <strong>большо́м</strong> го́роде мо́жно быть оди́н. В <strong>ма́леньком</strong> — нельзя́.</p>

<p>Э́то <span class="cn-word" data-tr="ham yaxshi, ham yomon">и хорошо́, и пло́хо</span>.</p>''',
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
                "explanation": "«Вы смо́трите вверх… Здесь лю́ди смо́трят вперёд». "
                               "Katta shahar odami binolarga qaramaydi — u ularga "
                               "oʻrganib qolgan.",
            },
            {
                "text": "Nega «в большо́м го́роде», lekin «по широ́кой у́лице»?",
                "choices": [
                    "Birinchisi Предло́жный (-ОМ), ikkinchisi Да́тельный (-ОЙ, ayol jinsi)",
                    "Ikkalasi bir xil kelishik",
                    "Chunki «у́лица» koʻplikda",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Sifat otga ergashadi. «В го́роде» — Предло́жный, erkak "
                               "jins → большо́м. «По у́лице» — Да́тельный, ayol jins → "
                               "широ́кой. Ayol jinsida -ОЙ toʻrtta kelishikda "
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
                "explanation": "«В большо́м го́роде мо́жно быть оди́н. В ма́леньком — "
                               "нельзя́. Э́то и хорошо́, и пло́хо». Matn tanlov "
                               "qilmaydi — u faqat farqni aytadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-45 — koʻplik И.п. / Р.п.                TAJRIBA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Пять дней без телефо́на",
        "summary": (
            "PR-45 matni. Besh kunlik tajriba, kunma-kun. Natija kutilganidek "
            "boʻlmadi: kitoblar ham, vaqt ham emas — eshik oldidagi uch doʻst "
            "muhimroq chiqdi."
        ),
        "order":   45,
        "grammar": [
            {
                "pattern":  "Koʻplik Роди́тельный",
                "meaning":  "Son va miqdor soʻzlaridan keyin: пять дней, мно́го книг, "
                            "мно́го часо́в. Erkak jins -ОВ / -ЕЙ, ayol va oʻrta jins "
                            "esa qoʻshimchasiz qoladi.",
                "examples": ["Пять дней без телефо́на.", "Мно́го книг, мно́го слов."],
            },
            {
                "pattern":  "Notoʻgʻri koʻpliklar",
                "meaning":  "Baʼzi soʻzlar koʻplikda butunlay oʻzgaradi: де́рево → "
                            "дере́вья → дере́вьев, друг → друзья́ → друзе́й, "
                            "день → дни → дней.",
                "examples": ["Мно́го дере́вьев.", "Три дру́га у две́ри."],
            },
            {
                "pattern":  "2-3-4 ↔ 5+",
                "meaning":  "PR-36 dagi qoida: 2, 3, 4 dan keyin Роди́тельный BIRLIK "
                            "(три дру́га), 5 va undan yuqori — Роди́тельный KOʻPLIK "
                            "(пять дней).",
                "examples": ["Две кни́ги за два дня.", "Пять дней."],
            },
        ],
        "body": '''<p>Я <span class="cn-word" data-pos="verb" data-tr="qaror qildim">реши́л</span>: пять <strong>дней</strong> без телефо́на.</p>

<p><strong>Пе́рвый день.</strong> Тру́дно. Я <span class="cn-word" data-pos="verb" data-tr="qidiraman">ищу́</span> телефо́н де́сять <strong>раз</strong>. Его́ нет. Ру́ки <span class="cn-word" data-tr="boʻsh">пусты́е</span>.</p>

<p><strong>Второ́й день.</strong> У меня́ мно́го <strong>вре́мени</strong>. Я чита́ю <span class="cn-word" data-tr="sekin">ме́дленно</span>. Две <strong>кни́ги</strong> за два дня.</p>

<p><strong>Тре́тий день.</strong> Я не зна́ю <span class="cn-word" data-tr="yangiliklar">но́вости</span>. И э́то норма́льно.</p>

<p><strong>Четвёртый день.</strong> Я ви́жу мно́го <strong>дере́вьев</strong> в на́шем дворе́. Ра́ньше я их не ви́дел. Они́ стоя́ли там <span class="cn-word" data-tr="doim">всегда́</span>.</p>

<p><strong>Пя́тый день.</strong> Ве́чером ко мне <span class="cn-word" data-pos="verb" data-tr="kelishdi">пришли́</span> три <strong>дру́га</strong>.</p>

<p>— У тебя́ нет телефо́на, — сказа́л Бекзод. — Мы <span class="cn-word" data-pos="verb" data-tr="xavotirlandik">волнова́лись</span>.</p>

<p>Пять дней. Мно́го <strong>книг</strong>. Мно́го <strong>часо́в</strong>. Мно́го <strong>слов</strong> в <span class="cn-word" data-tr="daftar">тетра́ди</span>.</p>

<p>И три <strong>дру́га</strong> у <span class="cn-word" data-tr="eshik oldida">две́ри</span>.</p>

<p>Тепе́рь телефо́н у меня́ есть. Но он <span class="cn-word" data-pos="verb" data-tr="yotadi">лежи́т</span> в су́мке. И я не ищу́ его́ де́сять раз в день.</p>''',
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
                               "alohida qatorda: «И три дру́га у две́ри». Sanalmaydigan "
                               "natija aynan shu.",
            },
            {
                "text": "Nega «пять дней», lekin «три дру́га»?",
                "choices": [
                    "5 dan boshlab Роди́тельный koʻplik, 2-3-4 dan keyin esa birlik",
                    "Chunki «друг» jonli",
                    "Chunki «день» erkak jinsida",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "PR-36 qoidasi: 1 → bosh kelishik; 2, 3, 4 → "
                               "Роди́тельный birlik (дру́га); 5 va undan yuqori → "
                               "Роди́тельный koʻplik (дней).",
            },
            {
                "text": "«Мно́го дере́вьев» — nega bu shakl gʻalati koʻrinadi?",
                "choices": [
                    "Де́рево koʻplikda butunlay oʻzgaradi: дере́вья → дере́вьев",
                    "Chunki daraxtlar jonli hisoblanadi",
                    "Chunki bu oʻrta jins",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Bir guruh soʻz koʻplikda -ЬЯ oladi: де́рево → "
                               "дере́вья, брат → бра́тья, стул → сту́лья. Ularning "
                               "Роди́тельный shakli esa -ЬЕВ boʻladi. Bunday soʻzlar "
                               "qoida bilan emas, yodlab olinadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-46 — koʻplik Д./В./Т./П.                UMUMIY XAT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Письмо́ всем друзья́м",
        "summary": (
            "PR-46 matni. Yil oxirida hamma doʻstlarga yoziladigan umumiy xat. "
            "Butun matn koʻplik kelishiklari ustida turadi — va oxirgi soʻz "
            "«глаза́ми»."
        ),
        "order":   46,
        "grammar": [
            {
                "pattern":  "Koʻplik Д./Т./П.: -АМ, -АМИ, -АХ",
                "meaning":  "Koʻplikda jins yoʻqoladi — uchta jins uchun bitta "
                            "qoʻshimcha. Yumshoq oʻzakda -ЯМ, -ЯМИ, -ЯХ: друзья́м, "
                            "друзья́ми, о друзья́х.",
                "examples": ["Пишу́ всем друзья́м.", "Я ду́маю о ста́рых друзья́х."],
            },
            {
                "pattern":  "детьми́ · людьми́",
                "meaning":  "Butun tizimdagi ikkita istisno. «Лю́дями» va «де́тями» "
                            "emas — людьми́ va детьми́. Ular qofiyalanadi, shuning "
                            "uchun birga yodlanadi.",
                "examples": ["Рабо́таю с ра́зными людьми́.", "Я говорю́ с детьми́."],
            },
            {
                "pattern":  "Sifat koʻplikda: -ЫМ, -ЫМИ, -ЫХ",
                "meaning":  "Sifat ham jinsni yoʻqotadi va ot bilan birga oʻzgaradi: "
                            "ста́рым друзья́м, с ра́зными людьми́, о ста́рых "
                            "друзья́х.",
                "examples": ["Спаси́бо ста́рым друзья́м."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Aziz">Дороги́е</span> друзья́!</p>

<p>Пишу́ <span class="cn-word" data-tr="hammaga">всем</span> — и <strong>ста́рым друзья́м</strong>, и <strong>но́вым</strong>.</p>

<p>Э́тот <span class="cn-word" data-tr="yil">год</span> был тру́дный. Я жил в <strong>двух города́х</strong>. Рабо́тал <strong>с ра́зными людьми́</strong>.</p>

<p>Ча́сто я ду́мал <strong>о ста́рых друзья́х</strong>. И <strong>о де́тях</strong> — мои́ де́ти <span class="cn-word" data-pos="verb" data-tr="oʻsyapti">расту́т</span> бы́стро.</p>

<p>Я говорю́ <strong>с ни́ми</strong> по телефо́ну ка́ждую суббо́ту. Э́то <span class="cn-word" data-tr="oz">ма́ло</span>. Но э́то есть.</p>

<p>Тепе́рь я хочу́ сказа́ть <strong>всем</strong> одно́ сло́во: спаси́бо.</p>

<p>Спаси́бо <strong>ста́рым друзья́м</strong> — за пи́сьма.</p>

<p>Спаси́бо <strong>но́вым</strong> — за <span class="cn-word" data-tr="kechalar">ве́чера</span> и <span class="cn-word" data-tr="suhbatlar">разгово́ры</span>.</p>

<p>Спаси́бо <strong>мои́м де́тям</strong> — за <span class="cn-word" data-tr="savollar">вопро́сы</span>. Они́ спра́шивают <span class="cn-word" data-tr="mendan yaxshiroq">лу́чше, чем я</span>.</p>

<p>Спаси́бо <strong>лю́дям</strong> в <strong>двух города́х</strong> — за <span class="cn-word" data-tr="sabr">терпе́ние</span>.</p>

<p>В <span class="cn-word" data-tr="keyingi">сле́дующем</span> году́ я хочу́ ви́деть <strong>всех</strong>. Не по телефо́ну.</p>

<p><strong>Глаза́ми</strong>.</p>''',
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
                "explanation": "Xat shu ikki jumla bilan tugaydi: «я хочу́ ви́деть "
                               "всех. Не по телефо́ну. Глаза́ми». Butun yil telefon "
                               "orqali oʻtdi — shuning uchun oxirgi soʻz shunchalik "
                               "kuchli.",
            },
            {
                "text": "Nega «с ра́зными людьми́», «лю́дями» emas?",
                "choices": [
                    "Людьми́ — butun tizimdagi ikkita istisnodan biri",
                    "Chunki «лю́ди» jonli",
                    "Chunki oldida sifat bor",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Koʻplik Твори́тельный odatda -АМИ / -ЯМИ boʻladi "
                               "(друзья́ми, города́ми). Faqat ikkita soʻz boshqacha: "
                               "людьми́ va детьми́. Ular qofiyalanadi.",
            },
            {
                "text": "«Друзья́м», «друзья́ми», «о друзья́х» — bu uch shakl nimani "
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
