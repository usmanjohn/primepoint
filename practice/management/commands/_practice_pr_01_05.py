# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-1 … PR-5 (kirill alifbosi bloki).

12 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_01_05.py --master=prime \\
        --expect-questions=12
"""

SUBJECT = {
    "name":        "Russian",
    "description": "Rus tili — grammatika va yozuv mashqlari",
    "icon":        "bi-translate",
    "color":       "#b91c1c",
}

DEFAULTS = {
    "level":                "easy",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}


# =====================================================================
# PR-1 — Kirill alifbosi: uchta oila va yettita soxta doʻst
# =====================================================================

Q_PR1 = [
    # 1–3 tanish
    {
        "text": "<p>Rus alifbosida nechta harf bor?</p>",
        "choices": ["33", "26", "30", "36"],
        "correct": "33",
        "explanation": "<p><strong>33</strong> harf: 10 unli, 21 undosh va tovushi "
                       "boʻlmagan 2 belgi (<strong>ъ</strong> va <strong>ь</strong>). "
                       "Oʻzbek kirillida 35 ta edi — chunki unda Ў, Қ, Ғ, Ҳ boʻlgan, "
                       "lekin Ы va Щ boʻlmagan.</p>",
    },
    {
        "text": "<p>Bu harf qanday oʻqiladi?</p><p><strong>Р р</strong></p>",
        "choices": ["r", "p", "b", "n"],
        "correct": "r",
        "explanation": "<p><strong>r</strong> — “rahmat”dagi r. Bu <strong>ВНРСУХИ</strong> "
                       "roʻyxatidagi eng xavfli harf: lotincha “P” ga oʻxshaydi, lekin "
                       "hech qachon “p” oʻqilmaydi. Ruscha “p” tovushi — <strong>П</strong> "
                       "harfi.</p>",
    },
    {
        "text": "<p>Bu harf qaysi oilaga kiradi?</p><p><strong>М м</strong></p>",
        "choices": ["“Bir xil” — lotinga ham oʻxshaydi, lotincha ham oʻqiladi",
                    "“Soxta doʻst” — oʻxshaydi, lekin boshqacha oʻqiladi",
                    "“Yangi shakl” — hech nimaga oʻxshamaydi",
                    "Bu harf umuman rus alifbosida yoʻq"],
        "correct": "“Bir xil” — lotinga ham oʻxshaydi, lotincha ham oʻqiladi",
        "explanation": "<p><strong>М</strong> — birinchi oiladan, А К М О Т Е bilan birga. "
                       "Koʻrinishi ham, tovushi ham lotincha “M” bilan bir xil, shuning "
                       "uchun uni yodlash shart emas.</p>",
    },
    # 4–7 oʻqish
    {
        "text": "<p>Bu soʻzni oʻqing.</p><p><strong>СПОРТ</strong></p>",
        "choices": ["[cnopt]", "[спорт]", "[shport]", "[snort]"],
        "correct": "[спорт]",
        "explanation": "<p><strong>[спорт]</strong> — “sport”. Ikkita soxta doʻst bor: "
                       "<strong>С</strong> = s (“c” emas) va <strong>Р</strong> = r "
                       "(“p” emas). П esa haqiqatan “p” beradi.</p>",
    },
    {
        "text": "<p>Bu soʻzni oʻqing.</p><p><strong>ВОДА́</strong></p>",
        "choices": ["[boda]", "[vada]", "[woda]", "[vodya]"],
        "correct": "[vada]",
        "explanation": "<p><strong>[vada]</strong> — “suv”. <strong>В har doim v</strong>, "
                       "hech qachon “b” emas (ruscha “b” — <strong>Б</strong> harfi). "
                       "Birinchi О esa urgʻusiz, shuning uchun [a] boʻlib oʻqiladi — "
                       "bu <strong>аканье</strong>, PR-5 da batafsil koʻramiz.</p>",
    },
    {
        "text": "<p>Bu soʻzni oʻqing.</p><p><strong>МУЗЕ́Й</strong></p>",
        "choices": ["[myuzey]", "[muzen]", "[muzey]", "[mizey]"],
        "correct": "[muzey]",
        "explanation": "<p><strong>[muzey]</strong> — “muzey”. <strong>У</strong> = u "
                       "(lotincha “y” emas!) va <strong>Й</strong> = qisqa y. Urgʻu "
                       "<strong>Е</strong> da: муз<strong>е́</strong>й.</p>",
    },
    {
        "text": "<p>Qaysi soʻzda <strong>uchta</strong> “soxta doʻst” harf bor?</p>",
        "choices": ["ПАРК", "БАНК", "СУВЕНИ́Р", "МЕТРО́"],
        "correct": "СУВЕНИ́Р",
        "explanation": "<p><strong>СУВЕНИ́Р</strong> da toʻrttadan ortiq: <strong>С</strong>(s), "
                       "<strong>У</strong>(u), <strong>В</strong>(v), <strong>Н</strong>(n), "
                       "<strong>И</strong>(i), <strong>Р</strong>(r). ПАРК da faqat Р, "
                       "БАНК da faqat Н, МЕТРО́ da faqat Р.</p>",
    },
    # 8–10 farqlash
    {
        "text": "<p>Qaysi harf oʻzbek kirillida bor, lekin rus alifbosida "
                "<strong>yoʻq</strong>?</p>",
        "choices": ["Щ", "Ы", "Ў", "Ц"],
        "correct": "Ў",
        "explanation": "<p><strong>Ў</strong> — Ў, Қ, Ғ, Ҳ toʻrttasi faqat oʻzbek "
                       "kirillida. Aksincha, <strong>Ы</strong> va <strong>Щ</strong> "
                       "ruschada bor, oʻzbek kirillida esa boʻlmagan. Ц ikkalasida "
                       "ham bor.</p>",
    },
    {
        "text": "<p>Ruscha “h” tovushini qaysi harf beradi?</p>",
        "choices": ["Н", "Х", "Г", "Bunday tovush rus tilida yoʻq"],
        "correct": "Х",
        "explanation": "<p><strong>Х</strong> — “xona”dagi x. <strong>Н</strong> esa "
                       "lotincha “H” ga oʻxshaydi, lekin u <strong>n</strong> oʻqiladi — "
                       "bu ВНРСУХИ dagi klassik tuzoq. Diqqat: oʻzbekchadagi Ҳ va Х "
                       "farqi rus tilida yoʻq, faqat bitta Х bor.</p>",
    },
    {
        "text": "<p>Soʻz ustidagi belgi (´) nimani bildiradi? Masalan: "
                "<strong>метро́</strong></p>",
        "choices": ["Bu alohida harf", "Bu urgʻu belgisi — qaysi boʻgʻin baland aytilishini "
                    "koʻrsatadi", "Bu tinish belgisi", "Bu unlini yumshatadi"],
        "correct": "Bu urgʻu belgisi — qaysi boʻgʻin baland aytilishini koʻrsatadi",
        "explanation": "<p>Bu <strong>ударе́ние</strong> — urgʻu belgisi. U harf emas va "
                       "haqiqiy ruscha matnda yozilmaydi; faqat oʻquvchilar uchun "
                       "kitoblarda boʻladi. Prime Russian darslarida biz uni yozamiz, "
                       "chunki ruschada urgʻu talaffuzning yarmi.</p>",
    },
    # 11–12 qoʻllash
    {
        "text": "<p>Qaysi oʻqish <strong>notoʻgʻri</strong>?</p>",
        "choices": ["ПАРК = [park]", "СТУДЕ́НТ = [styudent]", "БАНК = [bank]",
                    "ТЕА́ТР = [teatr]"],
        "correct": "СТУДЕ́НТ = [styudent]",
        "explanation": "<p><strong>СТУДЕ́НТ</strong> — <strong>[student]</strong>. "
                       "<strong>У</strong> bu “u”, “yu” emas. Ruscha “yu” tovushi "
                       "alohida harf bilan yoziladi — <strong>Ю</strong>. Bu ВНРСУХИ "
                       "dagi У harfining eng koʻp uchraydigan xatosi.</p>",
    },
    {
        "text": "<p>Kursiv (qiya) yozuvda qaysi harf lotincha “m” ga oʻxshab qoladi?</p>",
        "choices": ["и", "н", "т", "п"],
        "correct": "т",
        "explanation": "<p>Kursivda <strong>т</strong> lotincha “m” ga, <strong>и</strong> "
                       "esa lotincha “u” ga oʻxshab qoladi. Ikkalasi ham baribir eski "
                       "tovushini beradi: т = t, и = i. Birinchi haftada bu koʻpchilikni "
                       "shoshiradi, keyin koʻnikasiz.</p>",
    },
]


# =====================================================================
# PR-2 — Unlilar: beshta juftlik, Ы, va я ё ю е ning ikki vazifasi
# =====================================================================

Q_PR2 = [
    # 1–3 tanish
    {
        "text": "<p>Rus tilida nechta unli harf bor?</p>",
        "choices": ["5", "6", "10", "12"],
        "correct": "10",
        "explanation": "<p><strong>10</strong> unli — lekin ular <strong>beshta "
                       "juftlik</strong>: а—я, о—ё, у—ю, э—е, ы—и. Chap ustun qattiq, "
                       "oʻng ustun yumshoq. Shuning uchun yodlash 10 emas, 5 ta ish.</p>",
    },
    {
        "text": "<p><strong>о</strong> harfining yumshoq jufti qaysi?</p>",
        "choices": ["ё", "ю", "я", "е"],
        "correct": "ё",
        "explanation": "<p><strong>ё</strong>. Juftliklar: а—я, <strong>о—ё</strong>, "
                       "у—ю, э—е, ы—и. Tovush oʻzi bir xil (o), farq oldidagi undoshga "
                       "tegishli: <em>нос</em> qattiq, <em>нёс</em> yumshoq.</p>",
    },
    {
        "text": "<p>Qaysi unli soʻz boshida <strong>hech qachon</strong> kelmaydi?</p>",
        "choices": ["и", "э", "ы", "о"],
        "correct": "ы",
        "explanation": "<p><strong>ы</strong> hech qachon soʻz boshida kelmaydi — uni "
                       "doim undoshdan keyin koʻrasiz: <em>мы, ты, сын, был</em>. "
                       "Qolgan uchtasi bemalol soʻz boshlaydi: <em>и́мя, э́то, о́сень</em>.</p>",
    },
    # 4–7 oʻqish
    {
        "text": "<p><strong>ЛЮ́ДИ</strong> soʻzida <strong>ю</strong> nima qilyapti?</p>",
        "choices": ["“й + у” beryapti", "Л ni yumshatyapti", "Hech nima qilmayapti",
                    "Urgʻuni koʻrsatyapti"],
        "correct": "Л ni yumshatyapti",
        "explanation": "<p><strong>[л'у́д'и]</strong> — ю bu yerda <strong>undoshdan "
                       "keyin</strong> turibdi, shuning uchun “й” bermaydi, faqat Л ni "
                       "yumshatadi. “Lyudi” deb oʻqing, “Lyyudi” emas. Agar ю soʻz "
                       "boshida boʻlsa (<em>юг</em>), oʻshanda [йу] beradi.</p>",
    },
    {
        "text": "<p><strong>Я́БЛОКО</strong> soʻzida <strong>я</strong> nima qilyapti?</p>",
        "choices": ["Faqat yumshatyapti", "“й + а” beryapti", "[э] boʻlib oʻqilyapti",
                    "Tovushsiz"],
        "correct": "“й + а” beryapti",
        "explanation": "<p><strong>[йа́блъкъ]</strong> — я <strong>soʻz boshida</strong> "
                       "turibdi, demak birinchi vazifada: ikkita tovush, й + а. "
                       "“Ablako” emas, “Yablaka”. Xuddi shu narsa unlidan keyin "
                       "(<em>моя́</em>) va ь dan keyin (<em>семья́</em>) ham boʻladi.</p>",
    },
    {
        "text": "<p>Bu ikki soʻz bir xil oʻqiladimi?</p><p><strong>мы́ло — ми́ло</strong></p>",
        "choices": ["Ha, farqi yoʻq", "Yoʻq: [мы́лъ] va [м'и́лъ] — ikki xil soʻz",
                    "Ha, faqat urgʻu boshqa", "Yoʻq, lekin maʼnosi bir xil"],
        "correct": "Yoʻq: [мы́лъ] va [м'и́лъ] — ikki xil soʻz",
        "explanation": "<p><strong>мы́ло</strong> — sovun, <strong>ми́ло</strong> — "
                       "yoqimli. <strong>Ы</strong> ni <strong>И</strong> deb aytish — "
                       "oʻzbek oʻquvchisining eng koʻp uchraydigan talaffuz xatosi, va "
                       "u maʼnoni buzadi.</p>",
    },
    {
        "text": "<p>Qaysi soʻzda urgʻuni topish uchun hech narsa qilish shart emas?</p>",
        "choices": ["молоко́", "кни́га", "тётя", "окно́"],
        "correct": "тётя",
        "explanation": "<p><strong>тётя</strong> — unda <strong>ё</strong> bor, "
                       "<strong>ё esa har doim urgʻuli</strong>. Bitta istisno ham yoʻq. "
                       "Shuning uchun ё ustiga urgʻu belgisi ham qoʻyilmaydi — u "
                       "allaqachon urgʻuli.</p>",
    },
    # 8–10 farqlash
    {
        "text": "<p><strong>Ы</strong> tovushini chiqarish uchun nima qilish kerak?</p>",
        "choices": ["“и” deb aytib, tilni oldinga surish",
                    "“у” deb aytib, lablarni yoyish (til orqada qoladi)",
                    "“о” deb aytib, ogʻizni kengaytirish",
                    "“а” deb aytib, tilni koʻtarish"],
        "correct": "“у” deb aytib, lablarni yoyish (til orqada qoladi)",
        "explanation": "<p><strong>“у” → lablarni yoying</strong>. Til orqada, tomoqqa "
                       "yaqin qoladi — “i” emas; lab yoyilgan — “u” ham emas. Chiqqan "
                       "tovush <strong>ы</strong>. Oʻzbek tilida bu tovush yoʻq, shuning "
                       "uchun uni alohida mashq qilish kerak.</p>",
    },
    {
        "text": "<p><strong>нос</strong> va <strong>нёс</strong> — farqi nimada?</p>",
        "choices": ["Faqat urgʻuda", "Н ning yumshoqligida — va bu ikki xil soʻz",
                    "Farqi yoʻq", "Birinchisi koʻplik"],
        "correct": "Н ning yumshoqligida — va bu ikki xil soʻz",
        "explanation": "<p><strong>нос</strong> [нос] — burun. <strong>нёс</strong> "
                       "[н'ос] — koʻtarib ketardi. Yagona farq — Н qattiqmi yoki "
                       "yumshoq. Oʻzbek tilida yumshoqlik maʼnoni oʻzgartirmaydi, rus "
                       "tilida esa oʻzgartiradi.</p>",
    },
    {
        "text": "<p><strong>Ё</strong> haqida qaysi gap toʻgʻri?</p>",
        "choices": ["U hech qachon urgʻuli boʻlmaydi",
                    "U har doim urgʻuli, lekin bosmada koʻpincha “е” deb yoziladi",
                    "U faqat soʻz oxirida keladi",
                    "U undosh harf"],
        "correct": "U har doim urgʻuli, lekin bosmada koʻpincha “е” deb yoziladi",
        "explanation": "<p>Ikkala qism ham muhim. <strong>Ё har doim urgʻuli</strong>, "
                       "va gazeta-kitoblarda nuqtalari tashlab ketiladi: <em>ещё</em> "
                       "oʻrniga <em>еще</em>. Bu chalkashtiradi, chunki <em>всё</em> "
                       "(hammasi) va <em>все</em> (hammalari) — ikki xil soʻz.</p>",
    },
    # 11–12 qoʻllash
    {
        "text": "<p>Qaysi oʻqish <strong>notoʻgʻri</strong>?</p>",
        "choices": ["мя́со = [м'а́съ]", "я́блоко = [а́блъкъ]", "семья́ = [сим'йа́]",
                    "нет = [н'эт]"],
        "correct": "я́блоко = [а́блъкъ]",
        "explanation": "<p>Toʻgʻrisi <strong>[йа́блъкъ]</strong>. Soʻz boshida "
                       "<strong>я = й + а</strong>, “й” tushib qolmaydi. Qolgan uchtasi "
                       "toʻgʻri: мя́со da я undoshdan keyin (faqat yumshatadi), семья́ "
                       "da ь dan keyin (й qaytadi), нет da е undoshdan keyin.</p>",
    },
    {
        "text": "<p>Boʻsh joyga qaysi harf tushadi? Yumshoq juftlik kerak.</p>"
                "<p><strong>э — ___</strong></p>",
        "choices": ["и", "е", "я", "ю"],
        "correct": "е",
        "explanation": "<p><strong>э — е</strong>. Toʻliq roʻyxat: а—я, о—ё, у—ю, "
                       "<strong>э—е</strong>, ы—и. Shuning uchun <em>э́то</em> qattiq, "
                       "<em>нет</em> esa yumshoq Н bilan aytiladi.</p>",
    },
]


# =====================================================================
# PR-3 — Undoshlar 1: jarangli va jarangsiz juftliklar
# =====================================================================

Q_PR3 = [
    # 1–3 tanish
    {
        "text": "<p>Jarangli (зво́нкий) va jarangsiz (глухо́й) undoshni qanday "
                "ajratasiz?</p>",
        "choices": ["Ogʻiz ochiqligiga qarab", "Til qayerdaligiga qarab",
                    "Tomoq titraydimi yoki yoʻqmi — barmoq bilan tekshiriladi",
                    "Soʻzning uzunligiga qarab"],
        "correct": "Tomoq titraydimi yoki yoʻqmi — barmoq bilan tekshiriladi",
        "explanation": "<p>Barmoqni tomoqqa qoʻying va “<strong>ззззз</strong>” deng — "
                       "titraydi, demak <strong>jarangli</strong>. Endi "
                       "“<strong>сссс</strong>” deng — jim, demak "
                       "<strong>jarangsiz</strong>. Ogʻiz va til bir xil holatda "
                       "turadi; farq faqat ovoz paychalarida.</p>",
    },
    {
        "text": "<p><strong>З</strong> harfining jarangsiz jufti qaysi?</p>",
        "choices": ["С", "Ц", "Ш", "Ж"],
        "correct": "С",
        "explanation": "<p><strong>З — С</strong>. Oltita juftlik: б-п, в-ф, г-к, д-т, "
                       "<strong>з-с</strong>, ж-ш. Ж ning jufti — Ш; Ц ning esa jarangli "
                       "jufti umuman yoʻq.</p>",
    },
    {
        "text": "<p>Qaysi undoshning jufti <strong>yoʻq</strong>?</p>",
        "choices": ["Б", "Ж", "Д", "Р"],
        "correct": "Р",
        "explanation": "<p><strong>Р</strong> — u <em>doim jarangli</em>, jarangsiz "
                       "jufti yoʻq. Bu guruh: <strong>Л М Н Р Й</strong> (сонорные). "
                       "Qolganlarining jufti bor: Б—П, Ж—Ш, Д—Т.</p>",
    },
    # 4–7 oʻqish
    {
        "text": "<p><strong>ДЕНЬ</strong> soʻzida Д qattiqmi yoki yumshoq?</p>",
        "choices": ["Qattiq", "Yumshoq — chunki keyin Е turibdi",
                    "Yumshoq — chunki oxirida Ь bor", "Bu soʻzda Д umuman yoʻq"],
        "correct": "Yumshoq — chunki keyin Е turibdi",
        "explanation": "<p><strong>[д'эн']</strong>. Undoshni <strong>keyingi harf</strong> "
                       "yumshatadi: Д dan keyin <strong>Е</strong> (yumshoq unli) "
                       "turibdi. Soʻz oxiridagi Н ni esa <strong>Ь</strong> yumshatadi — "
                       "yaʼni soʻzda ikkita yumshoq undosh bor.</p>",
    },
    {
        "text": "<p>Nega <strong>друг</strong> soʻzi [друк] deb oʻqiladi?</p>",
        "choices": ["Chunki Г soʻz oxirida oʻz jarangsiz juftiga (К) aylanadi",
                    "Chunki Г har doim [к] oʻqiladi",
                    "Chunki soʻzda урgʻu yoʻq",
                    "Chunki oxirida Ь yoʻq"],
        "correct": "Chunki Г soʻz oxirida oʻz jarangsiz juftiga (К) aylanadi",
        "explanation": "<p>Bu <strong>оглушение</strong>: soʻz oxirida jarangli undosh "
                       "<strong>oʻz juftiga</strong> oʻtadi — boshqa tovushga emas. "
                       "Г → К, Б → П, Д → Т, З → С. Mana shuning uchun juftliklarni "
                       "bilish kerak edi. Toʻliq qoida PR-5 da.</p>",
    },
    {
        "text": "<p>Qaysi soʻzda hamma undosh <strong>qattiq</strong>?</p>",
        "choices": ["мать", "дя́дя", "стол", "день"],
        "correct": "стол",
        "explanation": "<p><strong>стол</strong> — С, Т, Л uchalasidan keyin ham yo qattiq "
                       "unli (о), yo soʻz oxiri. Qolganlarida yumshatuvchi bor: "
                       "<em>мать</em> da Ь, <em>дя́дя</em> da Я, <em>день</em> da Е "
                       "va Ь.</p>",
    },
    {
        "text": "<p>Ruscha <strong>Г</strong> harfi qanday aytiladi?</p>",
        "choices": ["Oʻzbekchadagi “gʻ” kabi, tomoqning chuqurroq yeridan",
                    "Oddiy “g” — oʻzbekchadagi “g” kabi",
                    "“h” kabi", "“k” kabi"],
        "correct": "Oddiy “g” — oʻzbekchadagi “g” kabi",
        "explanation": "<p>Rus tilida <strong>Ғ (gʻ) tovushi umuman yoʻq</strong> — faqat "
                       "oddiy Г bor. <em>го́род</em> [го́рът] ni “gʻorod” deb aytmang. "
                       "Xuddi shunday, ruschada Қ ham yoʻq — faqat К.</p>",
    },
    # 8–10 farqlash
    {
        "text": "<p>Qaysi guruh <strong>doim jarangsiz</strong>?</p>",
        "choices": ["Л М Н Р Й", "Б В Г Д", "Х Ц Ч Щ", "А О У Ы"],
        "correct": "Х Ц Ч Щ",
        "explanation": "<p><strong>Х Ц Ч Щ</strong> — bularning jarangli jufti yoʻq, "
                       "tomoq ularda hech qachon titramaydi. <strong>Л М Н Р Й</strong> "
                       "esa aksincha — doim jarangli. А О У Ы — bular unli, undosh "
                       "emas.</p>",
    },
    {
        "text": "<p><strong>мат</strong> va <strong>мать</strong> — farqi nima?</p>",
        "choices": ["Farqi yoʻq",
                    "Т ning yumshoqligi — va bu ikki xil soʻz: shaxmatdagi mot va ona",
                    "Faqat urgʻu boshqa",
                    "Ikkinchisi koʻplik"],
        "correct": "Т ning yumshoqligi — va bu ikki xil soʻz: shaxmatdagi mot va ona",
        "explanation": "<p><strong>мат</strong> [мат] va <strong>мать</strong> [мат'] — "
                       "yagona farq Т ning yumshoqligida, lekin maʼno butunlay boshqa. "
                       "Oʻzbek tilida qattiq-yumshoqlik maʼnoni oʻzgartirmaydi; rus "
                       "tilida oʻzgartiradi. Yana: <em>угол</em> (burchak) — "
                       "<em>у́голь</em> (koʻmir).</p>",
    },
    {
        "text": "<p>Nega <strong>во́дка</strong> [во́тка] deb oʻqiladi?</p>",
        "choices": ["Chunki Д soʻz oxirida turibdi",
                    "Chunki jarangsiz К dan oldin Д ham jarangsizlanadi → Т",
                    "Chunki bu chet soʻz",
                    "Chunki urgʻu birinchi boʻgʻinda"],
        "correct": "Chunki jarangsiz К dan oldin Д ham jarangsizlanadi → Т",
        "explanation": "<p>Bu <strong>ассимиляция</strong> — ogʻiz keyingi tovushga "
                       "oldindan tayyorlanadi. Tomoq bir tovushda ishlab, keyingisida "
                       "darrov toʻxtay olmaydi. Teskarisi ham boʻladi: "
                       "<em>сде́лать</em> → [зд'э́лът'], jarangli Д dan oldin С → З.</p>",
    },
    # 11–12 qoʻllash
    {
        "text": "<p>Qaysi oʻqish <strong>notoʻgʻri</strong>?</p>",
        "choices": ["дом = [дом]", "мать = [мати]", "стол = [стол]", "там = [там]"],
        "correct": "мать = [мати]",
        "explanation": "<p>Toʻgʻrisi <strong>[мат']</strong>. <strong>Ь hech qanday "
                       "tovush chiqarmaydi</strong> — u faqat Т ni yumshatadi. Soʻz "
                       "oxiriga “i” qoʻshish oʻzbek oʻquvchisining eng koʻp uchraydigan "
                       "xatosi.</p>",
    },
    {
        "text": "<p>Nega <strong>Ки́ев</strong> soʻzi [ки́иф] deb oʻqiladi?</p>",
        "choices": ["Chunki soʻz oxiridagi В oʻz jarangsiz juftiga (Ф) oʻtadi",
                    "Chunki В har doim [ф] oʻqiladi",
                    "Chunki bu chet el nomi",
                    "Chunki oxirida unli bor"],
        "correct": "Chunki soʻz oxiridagi В oʻz jarangsiz juftiga (Ф) oʻtadi",
        "explanation": "<p><strong>В — Ф</strong> juftligi ishladi: soʻz oxirida jarangli "
                       "В jarangsiz Ф ga aylanadi. Soʻz ichida esa В baribir “v” "
                       "boʻlib qolaveradi: <em>вода́</em> [вада́].</p>",
    },
]


# =====================================================================
# PR-4 — Shivirlovchilar ж ш щ ч ц, й va ikki belgi ъ ь
# =====================================================================

Q_PR4 = [
    # 1–3 tanish
    {
        "text": "<p>Qaysi undosh <strong>doim yumshoq</strong>?</p>",
        "choices": ["Ж", "Ц", "Ш", "Ч"],
        "correct": "Ч",
        "explanation": "<p><strong>Ч</strong> (va <strong>Щ</strong>) — doim yumshoq. "
                       "<strong>Ж, Ш, Ц</strong> esa aksincha — doim qattiq, ortidan "
                       "nima yozilishidan qatʼi nazar.</p>",
    },
    {
        "text": "<p><strong>Щ</strong> harfi qanday tovush beradi?</p>",
        "choices": ["Uzun yumshoq “sh”", "“ch”", "“sht”", "“s”"],
        "correct": "Uzun yumshoq “sh”",
        "explanation": "<p><strong>Щ</strong> — bu uzunroq va yumshoqroq “sh”: til "
                       "tanglayga koʻproq yaqinlashadi. <em>пло́щадь</em> (maydon), "
                       "<em>ещё</em> (hali). Bu harf oʻzbek kirillida yoʻq edi, shuning "
                       "uchun u siz uchun yangi.</p>",
    },
    {
        "text": "<p><strong>Ъ</strong> va <strong>Ь</strong> harflarining tovushi bormi?</p>",
        "choices": ["Ha, ikkalasida ham", "Faqat Ь da bor",
                    "Yoʻq — ikkalasi ham tovushsiz, ular faqat koʻrsatma beradi",
                    "Faqat Ъ da bor"],
        "correct": "Yoʻq — ikkalasi ham tovushsiz, ular faqat koʻrsatma beradi",
        "explanation": "<p>Ikkalasining ham <strong>oʻz tovushi yoʻq</strong>. "
                       "<strong>Ь</strong> oldidagi undoshni yumshatadi (мать, соль), "
                       "<strong>Ъ</strong> esa ajratadi, keyingi я ё ю е ni “й + unli” "
                       "qilib oʻqitadi (съесть).</p>",
    },
    # 4–7 oʻqish
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>МАШИ́НА</strong></p>",
        "choices": ["[маши́нъ] yumshoq shi bilan", "[машы́нъ]", "[масы́нъ]", "[мащи́нъ]"],
        "correct": "[машы́нъ]",
        "explanation": "<p><strong>[машы́нъ]</strong>. Yozilishi <strong>ШИ</strong>, "
                       "oʻqilishi <strong>[шы]</strong> — chunki <strong>Ш doim "
                       "qattiq</strong> va И uni yumshata olmaydi. Bu “жи-ши пиши с "
                       "буквой И” qoidasi: imlo bir xil, talaffuz boshqa.</p>",
    },
    {
        "text": "<p><strong>ЖИЗНЬ</strong> soʻzidagi ЖИ qanday oʻqiladi?</p>",
        "choices": ["[жи]", "[жы]", "[зи]", "[щи]"],
        "correct": "[жы]",
        "explanation": "<p><strong>[жы]</strong> — butun soʻz [жызн']. Ж doim qattiq, "
                       "shuning uchun И [ы] boʻlib chiqadi. Oxiridagi <strong>Ь</strong> "
                       "esa Н ni yumshatadi.</p>",
    },
    {
        "text": "<p><strong>СЕМЬЯ́</strong> soʻzida Ь nima qilyapti?</p>",
        "choices": ["Faqat М ni yumshatyapti", "Hech nima — u ortiqcha harf",
                    "М ni yumshatyapti va ajratyapti, shuning uchun Я = [йа]",
                    "Urgʻuni koʻrsatyapti"],
        "correct": "М ni yumshatyapti va ajratyapti, shuning uchun Я = [йа]",
        "explanation": "<p><strong>[сим'йа́]</strong> — soʻz ichidagi Ь koʻpincha ikki "
                       "ish qiladi. “Semya” emas, “sim-YA”: Я bu yerda toʻliq "
                       "[йа] boʻlib oʻqiladi, chunki oldida ajratuvchi belgi bor.</p>",
    },
    {
        "text": "<p>Qaysi soʻz <strong>feʼl</strong> (infinitiv)?</p>",
        "choices": ["мать", "соль", "день", "брать"],
        "correct": "брать",
        "explanation": "<p><strong>брать</strong> — “olmoq”. U <strong>-ть</strong> bilan "
                       "tugaydi, bu infinitiv belgisi: чита́ть, писа́ть, говори́ть, жить. "
                       "Qolganlari otlar — ular oddiy undosh + Ь bilan tugagan. Notanish "
                       "soʻz oxirida <strong>-ть</strong> koʻrsangiz, bu feʼl.</p>",
    },
    # 8–10 farqlash
    {
        "text": "<p><strong>наш</strong> va <strong>пло́щадь</strong> — oxirgi tovush "
                "farqi nimada?</p>",
        "choices": ["Farqi yoʻq", "наш da qisqa qattiq [ш], пло́щадь da uzun yumshoq [щ']",
                    "наш da yumshoq, пло́щадь da qattiq", "Ikkalasi ham [ч]"],
        "correct": "наш da qisqa qattiq [ш], пло́щадь da uzun yumshoq [щ']",
        "explanation": "<p><strong>Ш</strong> — qisqa va qattiq. <strong>Щ</strong> — "
                       "uzunroq va yumshoq. Bu ikki tovushni ajratish oʻzbek oʻquvchisi "
                       "uchun mashq talab qiladi, chunki oʻzbek kirillida Щ boʻlmagan.</p>",
    },
    {
        "text": "<p><strong>у́гол</strong> va <strong>у́голь</strong> — qaysi biri "
                "“koʻmir”?</p>",
        "choices": ["у́голь", "у́гол", "Ikkalasi ham", "Hech qaysisi"],
        "correct": "у́голь",
        "explanation": "<p><strong>у́голь</strong> — koʻmir; <strong>у́гол</strong> — "
                       "burchak. Yagona farq — oxiridagi <strong>Ь</strong>, yaʼni Л "
                       "yumshoqmi yoki qattiq. Bitta tovushsiz harf ikkita soʻzni "
                       "ajratib turibdi.</p>",
    },
    {
        "text": "<p>Qaysi soʻzda <strong>Ъ</strong> boʻlishi kerak?</p>",
        "choices": ["сесть", "семья", "съесть", "писать"],
        "correct": "съесть",
        "explanation": "<p><strong>съесть</strong> (yeb qoʻymoq) = <strong>с-</strong> "
                       "prefiksi + <strong>есть</strong>. Prefiksdan keyin, Е dan oldin — "
                       "Ъ ning aynan oʻz joyi: [с-йэст']. Ъ siz yozsangiz "
                       "<em>сесть</em> (oʻtirmoq) chiqadi — butunlay boshqa soʻz.</p>",
    },
    # 11–12 qoʻllash
    {
        "text": "<p>Qaysi oʻqish <strong>notoʻgʻri</strong>?</p>",
        "choices": ["цирк = [цырк]", "чай = [чай]", "соль = [соли]", "жить = [жыт']"],
        "correct": "соль = [соли]",
        "explanation": "<p>Toʻgʻrisi <strong>[сол']</strong>. Ь unli emas — u hech qanday "
                       "tovush qoʻshmaydi, faqat Л ni yumshatadi. “Soli” deb aytish — "
                       "oʻzbek oʻquvchisining klassik xatosi.</p>",
    },
    {
        "text": "<p><strong>Й</strong> harfi haqida qaysi gap toʻgʻri?</p>",
        "choices": ["Bu unli harf", "Bu undosh — “qisqa и”, oʻzi boʻgʻin yasamaydi",
                    "Bu tovushsiz belgi", "Bu faqat chet soʻzlarda uchraydi"],
        "correct": "Bu undosh — “qisqa и”, oʻzi boʻgʻin yasamaydi",
        "explanation": "<p><strong>Й</strong> (и краткое) — undosh. U aynan я, ё, ю, е "
                       "ichidagi “й” tovushi, faqat ochiq yozilgan: <em>чай, мой, "
                       "музе́й</em>. Oʻzi boʻgʻin yasay olmaydi.</p>",
    },
]


# =====================================================================
# PR-5 — Urgʻu, аканье, иканье va оглушение
# =====================================================================

Q_PR5 = [
    # 1–3 tanish
    {
        "text": "<p>Bitta ruscha soʻzda nechta urgʻuli boʻgʻin boʻladi?</p>",
        "choices": ["Bitta", "Ikkita", "Boʻgʻinlar soniga teng", "Urgʻu umuman yoʻq"],
        "correct": "Bitta",
        "explanation": "<p>Faqat <strong>bitta</strong>. U qolganlaridan uzunroq, "
                       "balandroq va aniqroq aytiladi; qolgan boʻgʻinlar siqiladi va "
                       "qisqaradi. Rus talaffuzining yarmi shu — hamma boʻgʻinni bir xil "
                       "kuch bilan aytish “oʻzbek aksenti”ning asosiy sababi.</p>",
    },
    {
        "text": "<p>Rus tilida urgʻu qayerda turadi?</p>",
        "choices": ["Doim oxirgi boʻgʻinda", "Doim birinchi boʻgʻinda",
                    "Istalgan boʻgʻinda — va soʻz oʻzgarganda koʻchishi ham mumkin",
                    "Doim ikkinchi boʻgʻinda"],
        "correct": "Istalgan boʻgʻinda — va soʻz oʻzgarganda koʻchishi ham mumkin",
        "explanation": "<p>Rus urgʻusi <strong>erkin va koʻchuvchan</strong>: "
                       "<em>рука́ → ру́ки</em>, <em>окно́ → о́кна</em>, <em>го́род → "
                       "города́</em>. Oʻzbek tilida esa urgʻu deyarli doim oxirgi "
                       "boʻgʻinda va u koʻchmaydi — mana shu farq eng koʻp qiyinchilik "
                       "tugʻdiradi.</p>",
    },
    {
        "text": "<p>Urgʻusiz <strong>О</strong> qanday oʻqiladi?</p>",
        "choices": ["[о] — oʻzgarmaydi", "[у]", "[а] — urgʻudan uzoqda esa [ъ]", "[и]"],
        "correct": "[а] — urgʻudan uzoqda esa [ъ]",
        "explanation": "<p>Bu <strong>аканье</strong> — rus talaffuzining eng koʻp "
                       "uchraydigan qoidasi. Urgʻudan bir boʻgʻin oldingi О aniq [а]; "
                       "undan uzoqroqdagisi va soʻz oxiridagisi deyarli eshitilmaydigan "
                       "[ъ] boʻlib qoladi.</p>",
    },
    # 4–7 oʻqish
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>МОЛОКО́</strong></p>",
        "choices": ["[молоко́]", "[мълако́]", "[мулуко́]", "[малака́]"],
        "correct": "[мълако́]",
        "explanation": "<p><strong>[мълако́]</strong>. Urgʻu oxirgi О da — u toʻliq [о]. "
                       "Undan oldingi О → [а]. Eng birinchisi urgʻudan uzoq → [ъ]. "
                       "Uchta bir xil harf, uch xil tovush — hammasi urgʻugacha "
                       "boʻlgan masofaga bogʻliq.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>ХОРОШО́</strong></p>",
        "choices": ["[хорошо́]", "[хърашо́]", "[харашо́]", "[хърышо́]"],
        "correct": "[хърашо́]",
        "explanation": "<p><strong>[хърашо́]</strong> — xuddi <em>молоко́</em> kabi. "
                       "Oxirgi О urgʻuli va toʻliq; oʻrtadagisi [а]; birinchisi [ъ]. "
                       "Bu naqsh uch boʻgʻinli soʻzlarda doim takrorlanadi.</p>",
    },
    {
        "text": "<p><strong>СЕСТРА́</strong> soʻzidagi Е qanday oʻqiladi?</p>",
        "choices": ["[э]", "[и]", "[а]", "[ы]"],
        "correct": "[и]",
        "explanation": "<p><strong>[систра́]</strong> — bu <strong>иканье</strong>: "
                       "urgʻusiz <strong>Е</strong> va <strong>Я</strong> [и] boʻlib "
                       "qisqaradi. Yana: <em>язы́к</em> → [йизы́к], <em>пятёрка</em> → "
                       "[п'ит'о́ркъ].</p>",
    },
    {
        "text": "<p><strong>САД</strong> (bogʻ) qanday oʻqiladi?</p>",
        "choices": ["[сат]", "[сад]", "[зат]", "[сът]"],
        "correct": "[сат]",
        "explanation": "<p><strong>[сат]</strong> — <strong>оглушение</strong>: soʻz "
                       "oxiridagi jarangli Д oʻz jarangsiz juftiga, Т ga aylanadi. "
                       "Diqqat: yozganda baribir <em>сад</em> — oʻzgargani talaffuz, "
                       "imlo emas.</p>",
    },
    # 8–10 farqlash
    {
        "text": "<p><strong>за́мок</strong> va <strong>замо́к</strong> — farqi nima?</p>",
        "choices": ["Farqi yoʻq", "за́мок = qulf, замо́к = qalʼa — urgʻu maʼnoni oʻzgartirdi",
                    "Birinchisi koʻplik", "Ikkinchisi eskirgan shakl"],
        "correct": "за́мок = qulf, замо́к = qalʼa — urgʻu maʼnoni oʻzgartirdi",
        "explanation": "<p>Bir xil harflar, bitta farq — urgʻu, va maʼno butunlay boshqa. "
                       "Yana bir juftlik: <strong>му́ка</strong> (azob) — "
                       "<strong>мука́</strong> (un). Shuning uchun yangi soʻzni "
                       "<em>urgʻusi bilan birga</em> yodlash kerak.</p>",
    },
    {
        "text": "<p>Nega <strong>про́сьба</strong> soʻzi [про́з'бъ] deb oʻqiladi?</p>",
        "choices": ["Chunki jarangli Б dan oldin С jaranglashadi → З",
                    "Chunki soʻz oxirida jarangsizlanish boʻldi",
                    "Chunki Ь harfi С ni oʻzgartirdi",
                    "Chunki urgʻu birinchi boʻgʻinda"],
        "correct": "Chunki jarangli Б dan oldin С jaranglashadi → З",
        "explanation": "<p>Bu <strong>ассимиляция</strong>ning teskari yoʻnalishi: ogʻiz "
                       "keyingi tovushga oldindan tayyorlanadi. <em>Во́дка</em> → "
                       "[во́тка] da jarangli tovush jarangsizlandi, bu yerda esa "
                       "aksincha boʻldi.</p>",
    },
    {
        "text": "<p>Qaysi soʻzda urgʻu <strong>oxirgi</strong> boʻgʻinda emas?</p>",
        "choices": ["молоко́", "окно́", "ру́ки", "вода́"],
        "correct": "ру́ки",
        "explanation": "<p><strong>ру́ки</strong> — urgʻu birinchi boʻgʻinda. Qizigʻi "
                       "shundaki, uning birligi <em>рука́</em> da urgʻu oxirda edi. "
                       "Rus urgʻusi soʻz shakli oʻzgarganda <strong>koʻchadi</strong> — "
                       "buni har bir yangi soʻzda tekshirish kerak.</p>",
    },
    # 11–12 qoʻllash
    {
        "text": "<p>Qaysi oʻqish <strong>notoʻgʻri</strong>?</p>",
        "choices": ["вода́ = [вада́]", "нож = [нош]", "го́род = [го́род]",
                    "Москва́ = [масква́]"],
        "correct": "го́род = [го́род]",
        "explanation": "<p>Bu yerda <strong>ikkita</strong> xato bor: ikkinchi О urgʻusiz, "
                       "demak [ъ] boʻladi; oxirdagi Д esa jarangsizlanib Т boʻladi. "
                       "Toʻgʻrisi — <strong>[го́рът]</strong>. Bitta qisqa soʻzda "
                       "аканье ham, оглушение ham ishlagan.</p>",
    },
    {
        "text": "<p>Bu gapda nechta soʻz talaffuzda oʻzgaradi?</p>"
                "<p><strong>Хлеб и молоко́ на столе́.</strong></p>",
        "choices": ["Bittasi", "Ikkitasi", "Uchtasi — хлеб, молоко́ va столе́",
                    "Hech qaysisi"],
        "correct": "Uchtasi — хлеб, молоко́ va столе́",
        "explanation": "<p><strong>[хлеп и мълако́ нъ стал'э́]</strong>. "
                       "<em>Хлеб</em> → [хлеп] (оглушение), <em>молоко́</em> → [мълако́] "
                       "(аканье), <em>на столе́</em> → [нъ стал'э́] (аканье, ikki marta). "
                       "Bitta qisqa gapda uchala qoida ham ishladi.</p>",
    },
]


# =====================================================================

PRACTICES = [
    {
        "title": "PR-1 Mashq: Kirill alifbosi — siz bilgan 33 harf va sizni chalgʻitadigan yettitasi",
        "description": "12 savol — alifboning uchta oilasi, ВНРСУХИ soxta doʻstlari va "
                       "birinchi ruscha soʻzlarni oʻqish.",
        "tutorial": "PR-1:",
        "questions": Q_PR1,
    },
    {
        "title": "PR-2 Mashq: Unlilar: а о у э ы va yumshatuvchi juftlar я ё ю е и",
        "description": "12 savol — beshta unli juftlik, Ы tovushi va я ё ю е ning "
                       "ikki vazifasi.",
        "tutorial": "PR-2:",
        "questions": Q_PR2,
    },
    {
        "title": "PR-3 Mashq: Undoshlar 1: jarangli va jarangsiz juftliklar",
        "description": "12 savol — oltita juftlik, juftsiz undoshlar va undoshning "
                       "qattiq-yumshoqligi.",
        "tutorial": "PR-3:",
        "questions": Q_PR3,
    },
    {
        "title": "PR-4 Mashq: Undoshlar 2: shivirlovchilar ж ш щ ч ц, й harfi va ikki belgi ъ ь",
        "description": "12 savol — жи-ши qoidasi, Ш va Щ farqi, Ъ va Ь ning vazifasi.",
        "tutorial": "PR-4:",
        "questions": Q_PR4,
    },
    {
        "title": "PR-5 Mashq: Urgʻu (ударение), аканье va soʻz oxiridagi jarangsizlanish",
        "description": "12 savol — urgʻu maʼnoni qanday oʻzgartiradi, аканье, иканье "
                       "va оглушение.",
        "tutorial": "PR-5:",
        "questions": Q_PR5,
    },
]
