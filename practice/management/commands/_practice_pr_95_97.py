# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-95 … PR-97.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_95_97.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "Russian",
    "description": "Rus tili — grammatika va yozuv mashqlari",
    "icon":        "bi-translate",
    "color":       "#b91c1c",
}

DEFAULTS = {
    "level":                "hard",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}


# =====================================================================
# PR-95 — Maqollar va matallar
# =====================================================================

Q_PR95 = [
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Посло́вица</strong> nimasi bilan "
                "<strong>фразеологи́зм</strong> dan farq qiladi?</p>",
        "choices": [
            "Poslovitsa qisqaroq",
            "Poslovitsa butun gap va ichida saboq bor",
            "Poslovitsa faqat yozuvda ishlatiladi",
            "Farqi yoʻq, ikkalasi bir xil",
        ],
        "correct": "Poslovitsa butun gap va ichida saboq bor",
        "explanation": "<p><em>Семь раз отме́рь, оди́н раз отре́жь</em> — oʻzi turadi va "
                       "maslahat beradi. <em>Бить баклу́ши</em> esa oʻzi turmaydi — u gap "
                       "ichiga qoʻshiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Семь раз отме́рь, оди́н раз "
                "отре́жь»</strong> ning oʻzbekcha jufti qaysi?</p>",
        "choices": [
            "Yetti oʻlchab, bir kes.",
            "Sabrning tagi sariq oltin.",
            "Nima eksang, shuni oʻrasan.",
            "Oʻz uying — oʻlan toʻshaging.",
        ],
        "correct": "Yetti oʻlchab, bir kes.",
        "explanation": "<p>Ikkala maqol ham <strong>yetti</strong> va <strong>bir</strong> "
                       "raqamlarini ishlatadi, ikkalasi ham oʻlchash va kesish haqida. Bu "
                       "maʼnodosh maqol emas — bu bir xil maqol.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Язы́к до Ки́ева доведёт»</strong>"
                " nimani anglatadi?</p>",
        "choices": [
            "Kiyevda rus tilida gapirishadi",
            "Til oʻrganish uzoq yoʻl",
            "Soʻrab-soʻrab istagan joyingga yetasan",
            "Koʻp gapirgan adashadi",
        ],
        "correct": "Soʻrab-soʻrab istagan joyingga yetasan",
        "explanation": "<p>Oʻzbekcha jufti — <strong>«Soʻrab-soʻrab Makkani "
                       "topibdi»</strong>. Ikkala maqol ham uzoqdagi muqaddas shaharni tilga "
                       "oladi va bir xil narsani aytadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Maqolni toʻldiring: <strong>Не име́й сто "
                "рубле́й, а ___ .</strong></p>",
        "choices": [
            "име́й сто друзе́й",
            "име́й сто книг",
            "рабо́тай сто дней",
            "живи́ сто лет",
        ],
        "correct": "име́й сто друзе́й",
        "explanation": "<p>Oʻzbekchasi: <strong>«Yuz soʻming boʻlguncha, yuz doʻsting "
                       "boʻlsin.»</strong> Obraz deyarli bir xil — faqat pul birligi "
                       "boshqa.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Maqolni qaysi matnda ishlatish "
                "<strong>mumkin emas</strong>?</p>",
        "choices": [
            "Ogʻzaki suhbatda",
            "Insho xulosasida",
            "Doʻstga yozilgan xatda",
            "Arizada va rasmiy hujjatda",
        ],
        "correct": "Arizada va rasmiy hujjatda",
        "explanation": "<p>Maqol — ogʻzaki va neytral nutqning bezagi. Rasmiy hujjatda uslub "
                       "buziladi (PR-90, PR-91): <s>Прошу́ рассмотре́ть… Как говори́тся, семь"
                       " раз отме́рь</s>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Что посе́ешь, то и "
                "пожнёшь»</strong> ning oʻzbekcha jufti?</p>",
        "choices": [
            "Nima eksang, shuni oʻrasan.",
            "Doʻst kulfatda bilinadi.",
            "Yetti oʻlchab, bir kes.",
            "Sabrning tagi sariq oltin.",
        ],
        "correct": "Nima eksang, shuni oʻrasan.",
        "explanation": "<p>Yana bir soʻzma-soʻz moslik: ikkala maqol ham "
                       "<strong>ekish</strong> va <strong>oʻrish</strong> obraziga "
                       "tayanadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Suhbatdosh dedi: <strong>«Ну, пе́рвый "
                "блин…»</strong> U nima demoqchi?</p>",
        "choices": [
            "Non pishirmoqchi",
            "Och qolgan",
            "Birinchi urinish chiqmasligi normal",
            "Nonushta vaqti boʻldi",
        ],
        "correct": "Birinchi urinish chiqmasligi normal",
        "explanation": "<p>Toʻliq maqol — <strong>«Пе́рвый блин ко́мом»</strong>. U yarmini "
                       "aytib toʻxtadi: rus nutqida maqolning yarmini aytish odatiy hol, "
                       "tinglovchi qolganini oʻzi biladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«В гостя́х хорошо́, а до́ма "
                "лу́чше»</strong> ning oʻzbekcha jufti?</p>",
        "choices": [
            "Mehmon otangdan ulugʻ.",
            "Oʻz uying — oʻlan toʻshaging.",
            "Doʻst kulfatda bilinadi.",
            "Yaltiragan hamma narsa oltin emas.",
        ],
        "correct": "Oʻz uying — oʻlan toʻshaging.",
        "explanation": "<p>Obraz butunlay boshqa (mehmonxona ↔ oʻlan toʻshak), lekin maʼno "
                       "bir xil: oʻz uyingdan yaxshi joy yoʻq. Maqolni tarjima qilmang — "
                       "<strong>juftini toping</strong>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Inshoda maqolni qaysi qolip bilan "
                "kiritasiz?</p>",
        "choices": [
            "Я ду́маю, что…",
            "Наприме́р…",
            "Неда́ром говоря́т… / Как говори́тся…",
            "Во-пе́рвых…",
        ],
        "correct": "Неда́ром говоря́т… / Как говори́тся…",
        "explanation": "<p>Ikki tayyor qolip: <strong>Неда́ром говоря́т…</strong> va "
                       "<strong>Как говори́тся…</strong> Ular maqolni xulosaga bogʻlaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi biri <strong>погово́рка</strong>?</p>",
        "choices": [
            "Век живи́ — век учи́сь.",
            "Ни ры́ба ни мя́со.",
            "Что посе́ешь, то и пожнёшь.",
            "Терпе́ние и труд всё перетру́т.",
        ],
        "correct": "Ни ры́ба ни мя́со.",
        "explanation": "<p><em>Ни ры́ба ни мя́со</em> — tugallanmagan obraz, saboq bermaydi "
                       "(«na u, na bu»). Qolgan uchtasi — toʻliq gap va maslahat, yaʼni "
                       "<strong>посло́вица</strong>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Терпе́ние и труд всё "
                "перетру́т»</strong> ning oʻzbekcha jufti?</p>",
        "choices": [
            "Sabrning tagi sariq oltin.",
            "Yetti oʻlchab, bir kes.",
            "Yuz soʻming boʻlguncha, yuz doʻsting boʻlsin.",
            "Nima eksang, shuni oʻrasan.",
        ],
        "correct": "Sabrning tagi sariq oltin.",
        "explanation": "<p>Ikkalasi ham <strong>sabr</strong> haqida va ikkalasi ham uning "
                       "oxiri yaxshi ekanini aytadi — faqat oʻzbekchasi «oltin» obrazini "
                       "qoʻshadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Nega <em>Ти́ше е́дешь — да́льше "
                "бу́дешь</em> da <strong>tire</strong> turibdi?</p>",
        "choices": [
            "Bu xato",
            "Gap qismlari bogʻlovchisiz turgani uchun",
            "Bu savol gap",
            "Tire har doim maqolda boʻladi",
        ],
        "correct": "Gap qismlari bogʻlovchisiz turgani uchun",
        "explanation": "<p>Maqollarda gap qismlari bogʻlovchisiz qoʻshiladi va oʻsha joyga "
                       "tire qoʻyiladi. Xuddi shunday: <em>Век живи́ — век учи́сь</em>. "
                       "Tinish belgilari PR-97 da.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Не всё то зо́лото, что "
                "блести́т»</strong> nimani anglatadi?</p>",
        "choices": [
            "Oltin qimmat",
            "Yaltiragan narsa arzon boʻladi",
            "Tashqi koʻrinishga ishonma",
            "Oltin yaltiramaydi",
        ],
        "correct": "Tashqi koʻrinishga ishonma",
        "explanation": "<p>Oʻzbekchasi ham deyarli soʻzma-soʻz: <strong>«Yaltiragan hamma "
                       "narsa oltin emas.»</strong></p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi shakl <strong>toʻgʻri</strong>?</p>",
        "choices": [
            "Семь раз отме́рить, оди́н раз отре́зать.",
            "Семь раз отме́рь, оди́н раз отре́жь.",
            "Семь раз отмеря́ю, оди́н раз отреза́ю.",
            "Семь раз отме́рил, оди́н раз отре́зал.",
        ],
        "correct": "Семь раз отме́рь, оди́н раз отре́жь.",
        "explanation": "<p>Maqol shakli <strong>qotib qolgan</strong> — <b>buyruq mayli</b>da"
                       " (PR-59) turadi va oʻzgartirilmaydi. Xuddi iboralar kabi (PR-94).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Rus nutqida maqol koʻpincha qanday "
                "aytiladi?</p>",
        "choices": [
            "Ikki marta takrorlanadi",
            "Faqat yozuvda ishlatiladi",
            "Har doim toʻliq aytiladi",
            "Yarmi aytiladi, qolganini tinglovchi oʻzi biladi",
        ],
        "correct": "Yarmi aytiladi, qolganini tinglovchi oʻzi biladi",
        "explanation": "<p><em>— Ну, зна́ешь… не всё то зо́лото…</em> Ikkinchi qism "
                       "aytilmadi, lekin hamma eshitdi. Buning uchun maqolni "
                       "<strong>butunligicha</strong> bilish kerak.</p>",
    },
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": [
            "Друг познаётся в беде́ — э́то пра́вда.",
            "Неда́ром говоря́т: семь раз отме́рь, оди́н раз отре́жь.",
            "Как говори́тся, пе́рвый блин ко́мом.",
            "Прошу́ рассмотре́ть заявле́ние. Как говори́тся, семь раз отме́рь.",
        ],
        "correct": "Прошу́ рассмотре́ть заявле́ние. Как говори́тся, семь раз отме́рь.",
        "explanation": "<p>Bu — <strong>ariza</strong>. Rasmiy hujjatda maqol ishlatilmaydi. "
                       "Qolgan uch gap ogʻzaki yoki insho uslubida va joyida.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": [
            "Maqol rasmiy hujjatda yaxshi eshitiladi.",
            "«Бить баклу́ши» — bu посло́вица.",
            "Maqolni har doim soʻzma-soʻz tarjima qilish kerak.",
            "«Язы́к до Ки́ева доведёт» va «Soʻrab-soʻrab Makkani topibdi» — bir maʼnodagi juft.",
        ],
        "correct": "«Язы́к до Ки́ева доведёт» va «Soʻrab-soʻrab Makkani topibdi» — bir "
                   "maʼnodagi juft.",
        "explanation": "<p>Qolgan uchtasi xato: <em>бить баклу́ши</em> — фразеологи́зм; "
                       "maqolni tarjima qilmasdan <strong>juftini</strong> topish kerak; "
                       "rasmiy hujjatda maqol boʻlmaydi.</p>",
    },
    {
        "text": "<p>Insho xulosasini toʻldiring.</p><p><strong>Fikr: shoshilib qaror qabul "
                "qilmaslik kerak.</strong></p>",
        "choices": [
            "Поэ́тому не сто́ит спеши́ть. Неда́ром говоря́т: семь раз отме́рь, оди́н раз отре́жь.",
            "Поэ́тому не сто́ит спеши́ть. Как говори́тся, пе́рвый блин ко́мом.",
            "Поэ́тому не сто́ит спеши́ть. Неда́ром говоря́т: друг познаётся в беде́.",
            "Поэ́тому не сто́ит спеши́ть. Как говори́тся, ни ры́ба ни мя́со.",
        ],
        "correct": "Поэ́тому не сто́ит спеши́ть. Неда́ром говоря́т: семь раз отме́рь, оди́н "
                   "раз отре́жь.",
        "explanation": "<p>Maqol xulosaga mos kelishi kerak. <em>Ти́ше е́дешь — да́льше "
                       "бу́дешь</em> ham toʻgʻri kelardi; qolgan uchtasi boshqa mavzuda.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Друг познаётся в беде́»</strong> "
                "ning oʻzbekcha jufti?</p>",
        "choices": [
            "Doʻst achitib gapirar.",
            "Doʻstingga ishonma.",
            "Doʻst kulfatda bilinadi.",
            "Yuz doʻsting boʻlsin.",
        ],
        "correct": "Doʻst kulfatda bilinadi.",
        "explanation": "<p>Bu juftlik ham deyarli soʻzma-soʻz: ikkala tilda ham "
                       "<em>doʻst</em> va <em>kulfat</em> soʻzlari turadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Nega maqollarni juft-juft yodlash tavsiya "
                "qilinadi?</p>",
        "choices": [
            "Chunki imtihonda shunday soʻraladi",
            "Chunki ular qisqa",
            "Chunki ruschasi oʻzbekchasidan kelib chiqqan",
            "Chunki soʻzma-soʻz tarjima oʻzbek quloqqa hech narsa aytmaydi",
        ],
        "correct": "Chunki soʻzma-soʻz tarjima oʻzbek quloqqa hech narsa aytmaydi",
        "explanation": "<p>«Til Kiyevgacha olib boradi» — hech kim tushunmaydi. «Soʻrab-"
                       "soʻrab Makkani topibdi» — hamma darrov tushunadi. Shuning uchun "
                       "chapda ruschasi, oʻngda oʻzbekchasi.</p>",
    },
]


# =====================================================================
# PR-96 — Tez-tez adashtiriladigan juftlar
# =====================================================================

Q_PR96 = [
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ___ пальто́ и "
                "вы́шел.</strong></p>",
        "choices": ["наде́л", "одева́л", "оде́лся", "оде́л"],
        "correct": "наде́л",
        "explanation": "<p>Palto — <strong>narsa</strong> (что?), demak "
                       "<strong>наде́ть</strong>. Oʻzbekcha «palto <em>kiydim</em>». "
                       "<em>Оде́ть</em> odamga ishlatiladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ма́ма ___ ребёнка.</strong></p>",
        "choices": ["наде́ла", "надева́ла", "оде́ла", "наде́лась"],
        "correct": "оде́ла",
        "explanation": "<p>Bola — <strong>odam</strong> (кого́?), demak "
                       "<strong>оде́ть</strong>. Oʻzbekcha «bolani <em>kiydirdi</em>» — "
                       "orttirma nisbat.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻzbekcha <strong>«kiydirmoq»</strong> "
                "ruschada qaysi feʼl?</p>",
        "choices": ["оде́ть", "одева́ться", "носи́ть", "наде́ть"],
        "correct": "оде́ть",
        "explanation": "<p>Oʻzbekchadagi <strong>-dir</strong> qoʻshimchasi (orttirma nisbat)"
                       " ruschada alohida feʼl bilan beriladi: <em>kiymoq</em> → наде́ть, "
                       "<em>kiydirmoq</em> → оде́ть.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Rus maktabidagi eslatma qanday "
                "jaranglaydi?</p>",
        "choices": [
            "Надева́ют оде́жду, одева́ют Наде́жду.",
            "Одева́ют оде́жду, надева́ют Наде́жду.",
            "Надева́ют Наде́жду, одева́ют оде́жду.",
            "Оде́жду и Наде́жду надева́ют.",
        ],
        "correct": "Надева́ют оде́жду, одева́ют Наде́жду.",
        "explanation": "<p><em>Оде́жда</em> — narsa, <em>Наде́жда</em> — odam. Soʻzlar joyini"
                       " almashtirgani uchun aynan shu esda qoladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ___ кни́гу на стол ка́ждое "
                "у́тро.</strong></p>",
        "choices": ["кладу́", "покла́л", "ложи́л", "ложу́"],
        "correct": "кладу́",
        "explanation": "<p>Prefikssiz — faqat <strong>класть</strong>. <em>Ложи́ть</em> degan"
                       " feʼl adabiy rus tilida <strong>mavjud emas</strong>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi feʼl adabiy tilda <strong>mavjud "
                "emas</strong>?</p>",
        "choices": ["сложи́ть", "класть", "положи́ть", "ложи́ть"],
        "correct": "ложи́ть",
        "explanation": "<p>Qoida: <strong>prefikssiz — класть, prefiks bilan — "
                       "-ложи́ть</strong>. Shuning uchun <em>положи́ть, сложи́ть, "
                       "вложи́ть</em> bor, <s>ложи́ть</s> esa yoʻq.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он сказа́л ___ са́мое, что и "
                "вчера́.</strong></p>",
        "choices": ["то́же", "то же", "та́кже", "так же"],
        "correct": "то же",
        "explanation": "<p><em>Са́мое</em> qoʻshilyapti, demak <strong>alohida</strong> "
                       "yoziladi — «oʻsha narsa». <em>То́же</em> boʻlganda <em>са́мое</em> "
                       "qoʻshib boʻlmasdi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ___ пойду́ с ва́ми.</strong></p>",
        "choices": ["то же", "то́же", "так же", "тем же"],
        "correct": "то́же",
        "explanation": "<p>«Ham, shuningdek» maʼnosida — <strong>birga</strong>. Tekshiruv: "
                       "<em>та́кже</em> bilan almashtirsa boʻladi, <em>са́мое</em> qoʻshib "
                       "boʻlmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>То́же</strong> yoki <strong>то "
                "же</strong> ekanini qanday tekshirasiz?</p>",
        "choices": [
            "Kelishikka qaraymiz",
            "Urgʻuga qaraymiz",
            "Gap uzunligiga qaraymiz",
            "«Са́мое» ni qoʻshib koʻramiz",
        ],
        "correct": "«Са́мое» ni qoʻshib koʻramiz",
        "explanation": "<p>Qoʻshilsa — <strong>то же</strong> alohida; qoʻshilmasa — "
                       "<strong>то́же</strong> birga. Xuddi shu test <em>та́кже / так же</em>"
                       " uchun ham ishlaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я всё сде́лаю в тече́ни_ "
                "неде́ли.</strong></p>",
        "choices": ["-и", "-е", "-ю", "-ей"],
        "correct": "-е",
        "explanation": "<p>Vaqt haqida gap ketyapti, demak <strong>в тече́ние "
                       "неде́ли</strong> — bu predlog. <em>-и</em> faqat haqiqiy oqim uchun: "
                       "<em>в тече́нии реки́</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>В тече́нии</strong> (-и bilan) "
                "qachon yoziladi?</p>",
        "choices": [
            "Vaqt haqida gapirilganda",
            "Har doim",
            "Rasmiy matnda",
            "Daryo yoki suv oqimi haqida gapirilganda",
        ],
        "correct": "Daryo yoki suv oqimi haqida gapirilganda",
        "explanation": "<p><em>В тече́ни<strong>и</strong> реки́</em> — daryoning oqimida. "
                       "Amalda 99 foiz holatda vaqt nazarda tutiladi, demak deyarli har doim "
                       "<strong>-е</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я пришёл, ___ помо́чь.</strong></p>",
        "choices": ["что бы", "что́бы", "что", "чем"],
        "correct": "что́бы",
        "explanation": "<p>Maqsad bildiryapti, demak <strong>birga</strong>. Test: "
                       "<em>бы</em> ni tashlab koʻring — <s>Я пришёл, что помо́чь</s> buzilib"
                       " ketadi, demak birga yoziladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ ты сде́лал на моём "
                "ме́сте?</strong></p>",
        "choices": ["Что́бы", "Что бы", "Чем бы", "Как бы"],
        "correct": "Что бы",
        "explanation": "<p><em>Бы</em> ni tashlasak — <em>Что ты сде́лал?</em> — gap "
                       "saqlanadi, demak <strong>alohida</strong> yoziladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi urgʻu <strong>toʻgʻri</strong>?</p>",
        "choices": ["позво́нишь", "зво́нит", "звони́т", "зво́нят"],
        "correct": "звони́т",
        "explanation": "<p>Urgʻu <strong>oxirgi boʻgʻinda</strong>: звони́т, звоня́т, "
                       "позвони́шь. Bu rus tilida eng koʻp tekshiriladigan urgʻu.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi soʻz rus tilida <strong>mavjud "
                "emas</strong>?</p>",
        "choices": ["обы́чно", "в о́бщем", "вообще́", "вообщем"],
        "correct": "вообщем",
        "explanation": "<p>Bunday soʻz yoʻq. Bor soʻzlar: <strong>в о́бщем</strong> (alohida,"
                       " «umuman olganda») va <strong>вообще́</strong> (birga, «umuman»).</p>",
    },
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": [
            "Положи́ телефо́н на стол.",
            "Наде́нь ша́пку, на у́лице хо́лодно.",
            "Оде́нь ша́пку, на у́лице хо́лодно.",
            "Ма́ма оде́ла ребёнка и вы́шла.",
        ],
        "correct": "Оде́нь ша́пку, на у́лице хо́лодно.",
        "explanation": "<p>Shapka — narsa, demak <strong>наде́нь</strong>. Qolgan uch gap "
                       "toʻgʻri: bolani <em>оде́ла</em> (odam), telefonni <em>положи́</em> "
                       "(СВ, prefiks bilan).</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": [
            "Я то́же са́мое ду́маю.",
            "Не ложи́ телефо́н на стол.",
            "Я всё сде́лаю в тече́нии неде́ли.",
            "Он мне звони́т ка́ждый день.",
        ],
        "correct": "Он мне звони́т ка́ждый день.",
        "explanation": "<p>Qolgan uchtasi xato: <em>то же са́мое</em> (alohida), <em>не "
                       "клади́</em> (класть), <em>в тече́ние неде́ли</em> (-е).</p>",
    },
    {
        "text": "<p>Bu gapdagi uchta xatoni toping.</p><p><strong>Вообщем, оде́нь ша́пку и не"
                " ложи́ её на стол.</strong></p>",
        "choices": [
            "В о́бщем, наде́нь ша́пку и не клади́ её на стол.",
            "Вообще́, оде́нь ша́пку и не клади́ её на стол.",
            "В о́бщем, оде́нь ша́пку и не ложи́ её на стол.",
            "Вообщем, наде́нь ша́пку и не клади́ её на стол.",
        ],
        "correct": "В о́бщем, наде́нь ша́пку и не клади́ её на стол.",
        "explanation": "<p>Uchta tuzatish: <s>вообщем</s> → <strong>в о́бщем</strong>; "
                       "<s>оде́нь</s> → <strong>наде́нь</strong> (shapka — narsa); "
                       "<s>ложи́</s> → <strong>клади́</strong> (prefikssiz).</p>",
    },
    {
        "text": "<p>Boʻsh joyga toʻgʻri feʼlni qoʻying.</p><p><strong>Ма́ма ___ Афсо́ну и ___"
                " ша́пку.</strong></p>",
        "choices": [
            "наде́ла / наде́ла",
            "наде́ла / оде́ла",
            "оде́ла / наде́ла",
            "оде́ла / оде́ла",
        ],
        "correct": "оде́ла / наде́ла",
        "explanation": "<p>Afsona — odam (кого́?) → <strong>оде́ла</strong>; shapka — narsa "
                       "(что?) → <strong>наде́ла</strong>. Oʻzbekcha: «Afsonani kiydirdi va "
                       "shapka kiydi».</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Nega oʻzbek oʻquvchi <em>наде́ть / "
                "оде́ть</em> farqini osonroq tushunadi?</p>",
        "choices": [
            "Chunki bu farq oʻzbekchada yoʻq",
            "Chunki bu soʻzlar oʻzbekchada ham bor",
            "Chunki oʻzbekchada bu farq «-dir» qoʻshimchasi bilan beriladi",
            "Chunki oʻzbekchada kiyim soʻzi bir xil",
        ],
        "correct": "Chunki oʻzbekchada bu farq «-dir» qoʻshimchasi bilan beriladi",
        "explanation": "<p><em>kiymoq</em> → наде́ть, <em>kiy<strong>dir</strong>moq</em> → "
                       "оде́ть. Farq oʻzbek oʻquvchi uchun yangi emas — u shunchaki boshqa "
                       "joyda turibdi.</p>",
    },
]


# =====================================================================
# PR-97 — Punktuatsiya
# =====================================================================

Q_PR97 = [
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Odamni qutqarish uchun vergul qayerga "
                "qoʻyiladi?</p><p><strong>Казни́ть нельзя́ поми́ловать</strong></p>",
        "choices": [
            "Казни́ть нельзя́, поми́ловать.",
            "Казни́ть нельзя́ поми́ловать.",
            "Казни́ть, нельзя́, поми́ловать.",
            "Казни́ть, нельзя́ поми́ловать.",
        ],
        "correct": "Казни́ть нельзя́, поми́ловать.",
        "explanation": "<p>Vergul <em>нельзя́</em> dan keyin tursa — «qatl qilib boʻlmaydi, "
                       "kechiring». <em>Казни́ть</em> dan keyin tursa — «qatl qiling». Uchta "
                       "soʻz, bitta vergul, ikki xil taqdir.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi gapda <strong>tire</strong> kerak?</p>",
        "choices": ["Дом большо́й.", "Мой брат врач.", "Бе́дность не поро́к.", "Он врач."],
        "correct": "Мой брат врач.",
        "explanation": "<p><strong>Мой брат — врач</strong>: ot va ot, ikkalasi И.п. Qolgan "
                       "uchtasida tire qoʻyilmaydi: ega olmosh, kesim sifat, yoki <em>не</em>"
                       " bor.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi holatda ega bilan kesim orasiga tire"
                " <strong>qoʻyilmaydi</strong>?</p>",
        "choices": [
            "Ega olmosh boʻlganda",
            "Ega ot boʻlganda",
            "Ega infinitiv boʻlganda",
            "Kesim ot boʻlganda",
        ],
        "correct": "Ega olmosh boʻlganda",
        "explanation": "<p><em>Он врач</em>, <s>Он — врач</s> emas. Tire qoʻyilmaydigan yana "
                       "ikki holat: <em>не</em> bor (<em>Бе́дность не поро́к</em>) va kesim "
                       "sifat (<em>Дом большо́й</em>).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Кото́рый</strong> oldida vergul "
                "qachon qoʻyiladi?</p>",
        "choices": ["Har doim", "Faqat uzun gapda", "Faqat gap oxirida", "Hech qachon"],
        "correct": "Har doim",
        "explanation": "<p>Rus tilida ergash gap <strong>istisnosiz</strong> vergul bilan "
                       "ajratiladi: <em>Э́то кни́га<strong>,</strong> кото́рую я "
                       "прочита́л</em>. Bu qoidada tanlov yoʻq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«И»</strong> oldida vergul "
                "kerakmi-yoʻqligini nima hal qiladi?</p>",
        "choices": ["Gapning uzunligi", "Feʼl turi", "Gapda nechta ega borligi", "Urgʻu"],
        "correct": "Gapda nechta ega borligi",
        "explanation": "<p>Bitta ega → vergul yoʻq (<em>Я чита́л и писа́л</em>). Ikki ega → "
                       "vergul bor (<em>Я чита́л<strong>,</strong> и он писа́л</em>).</p>",
    },
    {
        "text": "<p>Vergul kerakmi?</p><p><strong>Афсо́на пе́ла и танцева́ла.</strong></p>",
        "choices": [
            "Yoʻq, kerak emas",
            "Ha, gap oxirida",
            "Ha, ikki tomondan",
            "Ha, «и» oldida",
        ],
        "correct": "Yoʻq, kerak emas",
        "explanation": "<p>Bitta ega (Афсо́на), ikkita feʼl. <em>И</em> dan keyingi qism "
                       "alohida gap boʻlmaydi — <em>танцева́ла</em> ning egasi yoʻq.</p>",
    },
    {
        "text": "<p>Vergul kerakmi?</p><p><strong>Афсо́на пе́ла и Бекзо́д "
                "танцева́л.</strong></p>",
        "choices": [
            "Ha, «и» oldida",
            "Ha, gap boshida",
            "Ha, «Бекзо́д» dan keyin",
            "Yoʻq, kerak emas",
        ],
        "correct": "Ha, «и» oldida",
        "explanation": "<p><strong>Афсо́на пе́ла, и Бекзо́д танцева́л.</strong> Ikki ega — "
                       "demak ikki gap qoʻshilgan. Test: <em>Бекзо́д танцева́л</em> alohida "
                       "toʻliq gap.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi biri <strong>kirish soʻz</strong> "
                "emas?</p>",
        "choices": ["коне́чно", "к сожале́нию", "по-мо́ему", "потому́ что"],
        "correct": "потому́ что",
        "explanation": "<p><em>Потому́ что</em> — <strong>bogʻlovchi</strong>, ergash gapni "
                       "biriktiradi. Kirish soʻzlar esa gapning boʻlagi emas va ikki tomondan"
                       " vergul bilan ajratiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi gap <strong>toʻgʻri</strong>?</p>",
        "choices": [
            "Одна́ко, он не пришёл.",
            "Он одна́ко не пришёл.",
            "Он, одна́ко, не пришёл.",
            "Одна́ко он, не пришёл.",
        ],
        "correct": "Он, одна́ко, не пришёл.",
        "explanation": "<p>Gap oʻrtasida <em>одна́ко</em> — kirish soʻz («shunga qaramay»), "
                       "ikki tomondan vergul. Gap boshida esa u «lekin» degani va vergul "
                       "<strong>olmaydi</strong>: <em>Одна́ко он не пришёл.</em></p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Одна́ко</strong> gap boshida "
                "turganda vergul olamidi?</p>",
        "choices": [
            "Ha, har doim",
            "Yoʻq — u «lekin» degani",
            "Faqat savol gapda",
            "Faqat yozuvda",
        ],
        "correct": "Yoʻq — u «lekin» degani",
        "explanation": "<p>Tekshiruv: <em>но</em> bilan almashtirib koʻring. Almashsa — "
                       "vergul kerak emas: <em>Одна́ко он не пришёл</em> = <em>Но он не "
                       "пришёл</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Undalma</strong> (обраще́ние) "
                "qanday ajratiladi?</p>",
        "choices": [
            "Faqat gap boshida vergul bilan",
            "Ikki nuqta bilan",
            "Ajratilmaydi",
            "Qayerda tursa ham vergul bilan",
        ],
        "correct": "Qayerda tursa ham vergul bilan",
        "explanation": "<p><em>Жасу́р, иди́ сюда́.</em> · <em>Иди́ сюда́, Жасу́р.</em> · "
                       "<em>Скажи́ мне, Жасу́р, где ты был?</em> Oʻzbekchada ham xuddi "
                       "shunday.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Rasmiy xatda murojaatdan keyin qaysi belgi"
                " turadi?</p>",
        "choices": ["Vergul", "Nuqta", "Undov belgisi", "Ikki nuqta"],
        "correct": "Undov belgisi",
        "explanation": "<p><em>Уважа́емая Мари́на Петро́вна<strong>!</strong></em> — keyin "
                       "yangi qatordan bosh harf (PR-91). Oddiy xatda esa vergul ham boʻladi:"
                       " <em>Приве́т, Ка́тя!</em></p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi gapda vergul "
                "<strong>yetishmayapti</strong>?</p>",
        "choices": [
            "Я зна́ю, что он придёт.",
            "Э́то кни́га кото́рую я прочита́л.",
            "Позвони́, когда́ бу́дешь до́ма.",
            "Я пришёл, что́бы помо́чь.",
        ],
        "correct": "Э́то кни́га кото́рую я прочита́л.",
        "explanation": "<p><strong>Э́то кни́га, кото́рую я прочита́л.</strong> "
                       "<em>Который</em> oldida vergul har doim turadi — bu oʻzbek "
                       "oʻquvchilar eng koʻp unutadigan qoida.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Nega bu dars oʻzbek oʻquvchi uchun oson?</p>",
        "choices": [
            "Chunki rus tilida tinish belgilari kam",
            "Chunki qoidalar yodlanmaydi",
            "Chunki oʻzbek tinish tizimi rus tilidan olingan",
            "Chunki vergul ixtiyoriy",
        ],
        "correct": "Chunki oʻzbek tinish tizimi rus tilidan olingan",
        "explanation": "<p>Undalma, kirish soʻz va tire qoidalari oʻzbekchada ham "
                       "<strong>xuddi shunday</strong> ishlaydi: <em>Toshkent — Oʻzbekiston "
                       "poytaxti.</em> Yangi qoida faqat bitta — ergash gap oldidagi "
                       "vergul.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi gapda tire "
                "<strong>notoʻgʻri</strong> qoʻyilgan?</p>",
        "choices": [
            "Москва́ — столи́ца Росси́и.",
            "Чита́ть — моё люби́мое заня́тие.",
            "Мой оте́ц — инжене́р.",
            "Он — врач.",
        ],
        "correct": "Он — врач.",
        "explanation": "<p>Ega <strong>olmosh</strong> boʻlgani uchun tire qoʻyilmaydi: "
                       "<em>Он врач.</em> Qolgan uchtasida ot yoki infinitiv turibdi — tire "
                       "toʻgʻri.</p>",
    },
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": [
            "Я чита́л, и он писа́л.",
            "Я чита́л, и писа́л.",
            "Мы не пошли́, потому́ что шёл дождь.",
            "Коне́чно, я помогу́.",
        ],
        "correct": "Я чита́л, и писа́л.",
        "explanation": "<p>Bitta ega (я), ikkita feʼl — vergul kerak emas: <strong>Я чита́л и"
                       " писа́л.</strong> Qolgan uch gapda vergul joyida.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": [
            "Ergash gap oldida vergul ixtiyoriy.",
            "Tire har doim ega bilan kesim orasida turadi.",
            "Kirish soʻz vergul olmaydi.",
            "«И» oldida vergul ikki ega boʻlganda qoʻyiladi.",
        ],
        "correct": "«И» oldida vergul ikki ega boʻlganda qoʻyiladi.",
        "explanation": "<p>Qolgan uchtasi xato: ergash gap oldida vergul "
                       "<strong>majburiy</strong>; olmosh, <em>не</em> yoki sifat boʻlsa tire"
                       " qoʻyilmaydi; kirish soʻz har doim vergul bilan ajratiladi.</p>",
    },
    {
        "text": "<p>Tinish belgilarini toʻgʻri qoʻying.</p><p><strong>Дилно́за коне́чно я "
                "приду́</strong></p>",
        "choices": [
            "Дилно́за коне́чно, я приду́.",
            "Дилно́за, коне́чно я приду́.",
            "Дилно́за, коне́чно, я приду́.",
            "Дилно́за коне́чно я приду́.",
        ],
        "correct": "Дилно́за, коне́чно, я приду́.",
        "explanation": "<p>Ikkita ajratish kerak: <em>Дилно́за</em> — "
                       "<strong>undalma</strong>, <em>коне́чно</em> — <strong>kirish "
                       "soʻz</strong>. Ikkalasi ham vergul bilan ajratiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bu ikki gap bir xil "
                "maʼnodami?</p><p><strong>Мы не пошли́, потому́ что шёл дождь. / Мы не пошли́"
                " потому́, что шёл дождь.</strong></p>",
        "choices": [
            "Ikkalasi ham xato",
            "Ikkalasi toʻgʻri; ikkinchisida sabab taʼkidlanadi",
            "Faqat birinchisi toʻgʻri",
            "Faqat ikkinchisi toʻgʻri",
        ],
        "correct": "Ikkalasi toʻgʻri; ikkinchisida sabab taʼkidlanadi",
        "explanation": "<p>Vergul bogʻlovchi ichiga koʻchsa, sabab taʼkidlanadi — «aynan "
                       "shuning uchun». Ishonchingiz komil boʻlmasa, "
                       "<strong>birinchi</strong> shaklni tanlang — u har doim toʻgʻri.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻzbekcha <em>«Toshkent — Oʻzbekiston "
                "poytaxti»</em> gapidagi tire ruschada qaysi qoidaga toʻgʻri keladi?</p>",
        "choices": [
            "Kirish soʻz qoidasiga",
            "Undalma qoidasiga",
            "Ergash gap qoidasiga",
            "Ega va kesim orasidagi tire qoidasiga",
        ],
        "correct": "Ega va kesim orasidagi tire qoidasiga",
        "explanation": "<p><em>Москва́ — столи́ца Росси́и</em> bilan aynan bir xil: ot va ot "
                       "orasida, <em>«boʻlmoq»</em> feʼli aytilmagani uchun. Ikkala tilda ham"
                       " bir xil ishlaydi.</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-95 Mashq: Maqollar va matallar",
        "description": (
            "Посло́вица va погово́рка farqi, oʻzbekcha juftlar (Yetti oʻlchab "
            "bir kes; Soʻrab-soʻrab Makkani topibdi) va yarmini aytish odati."
        ),
        "tutorial": "PR-95:",
        "questions": Q_PR95,
    },
    {
        "title": "PR-96 Mashq: Tez-tez adashtiriladigan juftlar",
        "description": (
            "Наде́ть/оде́ть = kiymoq/kiydirmoq, класть/положи́ть va «ложи́ть» "
            "yoʻqligi, то́же/то же, в тече́ние/в тече́нии, что́бы/что бы."
        ),
        "tutorial": "PR-96:",
        "questions": Q_PR96,
    },
    {
        "title": "PR-97 Mashq: Punktuatsiya",
        "description": (
            "«Казни́ть нельзя́ поми́ловать», ega-kesim tiresi, ergash gap "
            "oldidagi majburiy vergul, «и» sinovi, kirish soʻz va undalma."
        ),
        "tutorial": "PR-97:",
        "questions": Q_PR97,
    },
]
