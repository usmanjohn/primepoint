# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-5 … PK-8 (Hangul bloki yakuni).

12 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_05_08.py --master=prime \\
        --expect-questions=12
"""

SUBJECT = {
    "name":        "한국어",
    "description": "Koreys tili — grammatika va yozuv mashqlari",
    "icon":        "bi-translate",
    "color":       "#d97706",
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
# PK-5 — Undoshlar 2: ㅈ va nafasli ㅊ ㅋ ㅌ ㅍ ㅎ
# =====================================================================

Q_PK5 = [
    {
        "text": "<p>ㄷ ga bitta chiziq qoʻshsak qaysi harf chiqadi?</p>",
        "choices": ["ㅌ", "ㄸ", "ㄴ", "ㅊ"],
        "correct": "ㅌ",
        "explanation": "<p><strong>ㅌ</strong>. Qoʻshimcha chiziq — qoʻshimcha <em>nafas</em>. "
                       "ㄸ esa chiziq emas, harfning ikki marta yozilgani (qattiq undosh, "
                       "PK-6).</p>",
    },
    {
        "text": "<p>Bu harf qaysi tovushni beradi?</p><p><strong>ㅍ</strong></p>",
        "choices": ["Nafasli [p]", "[f]", "[b]", "Nafasli [k]"],
        "correct": "Nafasli [p]",
        "explanation": "<p><strong>Nafasli [p]</strong>. Koreys tilida <em>f</em> tovushi "
                       "umuman yoʻq — chet soʻzlar ham ㅍ bilan yoziladi: coffee → 커피, "
                       "France → 프랑스.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>Nafasli undoshlar (ㅋ ㅌ ㅍ ㅊ) soʻzdagi joyiga qarab "
                "oʻzgaradimi?</strong></p>",
        "choices": ["Yoʻq — ular har doim bir xil", "Ha, unlilar orasida jaranglashadi",
                    "Ha, soʻz oxirida yoʻqoladi", "Faqat 받침da oʻzgaradi"],
        "correct": "Yoʻq — ular har doim bir xil",
        "explanation": "<p><strong>Oʻzgarmaydi.</strong> Jaranglashish qoidasi (soʻz boshida “k”, "
                       "unlilar orasida “g”) faqat <em>oddiy</em> undoshlarga — ㄱ ㄷ ㅂ ㅈ ga "
                       "tegishli. Nafasli undoshlar har doim kuchli nafas bilan aytiladi.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>아버지</strong></p>",
        "choices": ["[a-bo-ji]", "[a-po-chi]", "[a-bo-chi]", "[a-po-ji]"],
        "correct": "[a-bo-ji]",
        "explanation": "<p><strong>[a-bo-ji]</strong> — “ota”. ㅂ ham, ㅈ ham ikkita unli orasida "
                       "turibdi, shuning uchun ikkalasi ham jaranglashgan.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>커피</strong></p>",
        "choices": ["[kho-phi]", "[ko-fi]", "[ko-pi]", "[kho-fi]"],
        "correct": "[kho-phi]",
        "explanation": "<p><strong>[kho-phi]</strong> — “kofe”. Ikkala undosh ham nafasli. "
                       "ㅍ ≠ f: koreys tilida <em>f</em> tovushi yoʻq.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>포도</strong></p>",
        "choices": ["[pho-do]", "[po-to]", "[fo-do]", "[pho-to]"],
        "correct": "[pho-do]",
        "explanation": "<p><strong>[pho-do]</strong> — “uzum”. ㅍ nafasli va oʻzgarmaydi, ㄷ esa "
                       "unlilar orasida jaranglashib “d” boʻlgan.</p>",
    },
    {
        "text": "<p>“Qogʻoz sinovi” nimani tekshiradi?</p>",
        "choices": ["Undosh nafasli yoki nafassiz ekanini",
                    "Unli tik yoki yotiq ekanini",
                    "받침 bor yoki yoʻqligini",
                    "Boʻgʻinning uzunligini"],
        "correct": "Undosh nafasli yoki nafassiz ekanini",
        "explanation": "<p>Qogʻozni lablar oldida ushlab, <strong>바</strong> va "
                       "<strong>파</strong> deb ayting: nafassiz 바 da qogʻoz deyarli "
                       "qimirlamaydi, nafasli 파 da esa sezilarli uchadi.</p>",
    },
    {
        "text": "<p>Qaysi juftlik <strong>달</strong> va <strong>탈</strong> ni toʻgʻri "
                "tavsiflaydi?</p>",
        "choices": ["달 — nafassiz “oy”, 탈 — nafasli “niqob”",
                    "달 — nafasli “niqob”, 탈 — nafassiz “oy”",
                    "Ikkalasi ham “oy”, faqat imlosi boshqa",
                    "Ikkalasi ham nafasli"],
        "correct": "달 — nafassiz “oy”, 탈 — nafasli “niqob”",
        "explanation": "<p>Koreys tilida <strong>nafas maʼnoni ajratadi</strong>: 달 (“oy”) "
                       "nafassiz ㄷ bilan, 탈 (“niqob”) nafasli ㅌ bilan. Oʻzbekchada bunday farq "
                       "yoʻq, shuning uchun buni alohida mashq qilish kerak.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>축하</strong></p>",
        "choices": ["[추카]", "[축하]", "[추가]", "[축가]"],
        "correct": "[추카]",
        "explanation": "<p><strong>[추카]</strong> — “tabrik”. 받침 ㄱ keyingi ㅎ bilan birikib "
                       "nafasli <strong>ㅋ</strong> beradi. Bu hodisa <em>격음화</em> deb "
                       "ataladi — PK-8 da toʻliq koʻriladi.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>좋아요</strong></p>",
        "choices": ["[조아요]", "[조하요]", "[초하요]", "[좋아요]"],
        "correct": "[조아요]",
        "explanation": "<p><strong>[조아요]</strong>. 받침 holatidagi <strong>ㅎ ikkita unli "
                       "orasida qolganda tushib ketadi</strong>. 좋다 (“yaxshi”) eng koʻp "
                       "ishlatiladigan soʻzlardan, shuning uchun buni hozirdan yodlang.</p>",
    },
    {
        "text": "<p>Qaysi gapdagi talaffuz notoʻgʻri?</p>",
        "choices": ["커피 → [ko-fi]", "코 → [kho]", "차 → [cha]", "하나 → [ha-na]"],
        "correct": "커피 → [ko-fi]",
        "explanation": "<p><strong>커피 → [ko-fi]</strong> notoʻgʻri. Koreys tilida <em>f</em> "
                       "yoʻq va ㅋ nafasli boʻlishi kerak: toʻgʻrisi <strong>[kho-phi]</strong>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>ㅎ harfi unlilar orasida qanday tutadi?</strong></p>",
        "choices": ["Kuchsizlanadi va koʻpincha yoʻqoladi", "Kuchayadi",
                    "Qattiq undoshga aylanadi", "Hech qachon oʻzgarmaydi"],
        "correct": "Kuchsizlanadi va koʻpincha yoʻqoladi",
        "explanation": "<p><strong>Yoʻqoladi</strong>: 좋아요 → [조아요], 전화 → [저놔]. Soʻz "
                       "boshida esa ㅎ oddiy “h” boʻlib aytiladi: 하나, 형, 한국.</p>",
    },
]


# =====================================================================
# PK-6 — Undoshlar 3: qattiq ㄲ ㄸ ㅃ ㅆ ㅉ
# =====================================================================

Q_PK6 = [
    {
        "text": "<p>ㅂ ning qattiq jufti qaysi?</p>",
        "choices": ["ㅃ", "ㅍ", "ㅁ", "ㅄ"],
        "correct": "ㅃ",
        "explanation": "<p><strong>ㅃ</strong> — ㅂ ikki marta yozilgani. ㅍ esa <em>nafasli</em> "
                       "jufti. Uchlik: ㅂ (oddiy) · ㅍ (nafas koʻp) · ㅃ (nafas yoʻq, tomoq "
                       "tarang).</p>",
    },
    {
        "text": "<p>Qaysi undoshning nafasli jufti yoʻq?</p>",
        "choices": ["ㅅ", "ㄱ", "ㄷ", "ㅈ"],
        "correct": "ㅅ",
        "explanation": "<p><strong>ㅅ</strong>. Uning faqat qattiq jufti bor — ㅆ. Shuning uchun "
                       "koreys tilida jami 19 ta undosh: 14 asosiy + 5 qattiq.</p>",
    },
    {
        "text": "<p>Qattiq undoshni qanday aytasiz?</p>",
        "choices": ["Nafassiz, tomoq tarang holda", "Kuchli nafas bilan",
                    "Burun orqali", "Ovozni pasaytirib"],
        "correct": "Nafassiz, tomoq tarang holda",
        "explanation": "<p><strong>Nafas chiqarmasdan, tomoqni taranglashtirib.</strong> Qogʻoz "
                       "sinovida 빠 da qogʻoz <em>umuman</em> qimirlamaydi — nafasli 파 da esa "
                       "uchib ketadi.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>오빠</strong></p>",
        "choices": ["[oppa]", "[oba]", "[opha]", "[oʻba]"],
        "correct": "[oppa]",
        "explanation": "<p><strong>[oppa]</strong> — “aka” (qiz bola uchun). Qattiq undosh "
                       "<em>hech qachon jaranglashmaydi</em>, shuning uchun [oba] boʻlishi "
                       "mumkin emas.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>아까</strong></p>",
        "choices": ["[akka]", "[aga]", "[akha]", "[aka]"],
        "correct": "[akka]",
        "explanation": "<p><strong>[akka]</strong>. PK-4 dagi “unlilar orasida ㄱ → g” qoidasi "
                       "faqat <em>oddiy</em> undoshlarga tegishli — qattiq undosh hech qachon "
                       "jaranglashmaydi.</p>",
    },
    {
        "text": "<p>“non” soʻzi koreyschada qanday yoziladi?</p>",
        "choices": ["빵", "방", "팡", "밤"],
        "correct": "빵",
        "explanation": "<p><strong>빵</strong> [ppang]. Boshida qattiq ㅃ, oxirida 받침 ㅇ. "
                       "방 esa “xona”, butunlay boshqa soʻz.</p>",
    },
    {
        "text": "<p>Qaysi biri “qiz (farzand)” degani?</p>",
        "choices": ["딸", "탈", "달", "탕"],
        "correct": "딸",
        "explanation": "<p><strong>딸</strong> — qattiq ㄸ bilan. 탈 = “niqob” (nafasli), "
                       "달 = “oy” (oddiy). Uchalasining farqi faqat birinchi undoshda.</p>",
    },
    {
        "text": "<p>Qaysi uchlik toʻgʻri tartibda berilgan "
                "(oddiy — nafasli — qattiq)?</p>",
        "choices": ["불 — 풀 — 뿔", "뿔 — 불 — 풀", "풀 — 뿔 — 불", "불 — 뿔 — 풀"],
        "correct": "불 — 풀 — 뿔",
        "explanation": "<p><strong>불</strong> (olov, oddiy ㅂ) — <strong>풀</strong> (oʻt, "
                       "nafasli ㅍ) — <strong>뿔</strong> (shox, qattiq ㅃ). Unli va 받침 bir xil, "
                       "farq faqat birinchi undoshda.</p>",
    },
    {
        "text": "<p>Oʻzbek tilidagi qaysi soʻz qattiq undosh tovushiga eng yaqin?</p>",
        "choices": ["ikki", "kitob", "olma", "non"],
        "correct": "ikki",
        "explanation": "<p><strong>ikki</strong> — ikkilangan undosh keskin va tarang chiqadi, "
                       "aynan koreys qattiq undoshi kabi. Farqi shundaki, koreyschada u soʻz "
                       "<em>boshida</em> ham keladi: 까, 따, 빠.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>ㄲ qanday yasalgan?</strong></p>",
        "choices": ["ㄱ ikki marta yozilgan", "ㄱ ga chiziq qoʻshilgan",
                    "ㄱ va ㅋ birikkan", "Bu butunlay yangi shakl"],
        "correct": "ㄱ ikki marta yozilgan",
        "explanation": "<p>Qattiq undoshda <strong>yangi shakl yoʻq</strong> — bu shunchaki "
                       "harfning ikki marta yozilgani. Yangi boʻlgani faqat tomoqning "
                       "holati.</p>",
    },
    {
        "text": "<p>Bekzod <strong>오빠</strong> ni “opa” deb aytdi. Xato qayerda?</p>",
        "choices": ["Tomoqni taranglashtirmadi va ㅃ oʻrniga oddiy ㅂ aytdi",
                    "Nafasni juda kuchli chiqardi",
                    "받침ni tushirib qoldirdi",
                    "Unlini notoʻgʻri aytdi"],
        "correct": "Tomoqni taranglashtirmadi va ㅃ oʻrniga oddiy ㅂ aytdi",
        "explanation": "<p>Qattiq undoshda tovush <strong>keskin va quruq</strong> boʻlishi kerak "
                       "— oʻzbekcha <em>akka</em> dagi kabi. Toʻgʻrisi <strong>[oppa]</strong>.</p>",
    },
    {
        "text": "<p>Qaysi javob notoʻgʻri?</p>",
        "choices": ["Qattiq undosh unlilar orasida jaranglashadi",
                    "Qattiq undoshda nafas chiqmaydi",
                    "ㅆ — ㅅ ning qattiq jufti",
                    "Koreys tilida jami 19 ta undosh bor"],
        "correct": "Qattiq undosh unlilar orasida jaranglashadi",
        "explanation": "<p>Qattiq undosh <strong>hech qachon jaranglashmaydi</strong>: 아까 har "
                       "doim [akka], hech qachon [aga] emas. Jaranglashish faqat oddiy "
                       "undoshlarda (ㄱ ㄷ ㅂ ㅈ) boʻladi.</p>",
    },
]


# =====================================================================
# PK-7 — Boʻgʻin bloklari va 받침
# =====================================================================

Q_PK7 = [
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>받침 nima?</strong></p>",
        "choices": ["Boʻgʻin blokining eng pastidagi undosh",
                    "Boʻgʻindagi unli",
                    "Boʻgʻin boshidagi undosh",
                    "Ikki soʻz orasidagi boʻshliq"],
        "correct": "Boʻgʻin blokining eng pastidagi undosh",
        "explanation": "<p><strong>받침</strong> — “tayanch” degani, blokni pastdan koʻtarib "
                       "turgan undosh. Rasmiy nomi 종성.</p>",
    },
    {
        "text": "<p>받침 oʻrnida nechta <em>tovush</em> boʻlishi mumkin?</p>",
        "choices": ["7 ta", "14 ta", "19 ta", "27 ta"],
        "correct": "7 ta",
        "explanation": "<p><strong>Yettita: ㄱ, ㄴ, ㄷ, ㄹ, ㅁ, ㅂ, ㅇ.</strong> Yozilishi mumkin "
                       "boʻlgan harf 27 ta, lekin ular shu yettitaga yigʻiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>Qoʻshaloq 받침da (겹받침) nechta harf oʻqiladi?</strong></p>",
        "choices": ["Odatda bittasi", "Ikkalasi ham", "Hech qaysisi", "Har doim ikkinchisi"],
        "correct": "Odatda bittasi",
        "explanation": "<p><strong>Odatda bittasi</strong>: 값 → [갑], 없다 → [업따], "
                       "읽다 → [익따], 앉다 → [안따]. Qaysi biri oʻqilishi soʻzga qarab "
                       "oʻzgaradi.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>옷</strong></p>",
        "choices": ["[옫]", "[오스]", "[옷]", "[온]"],
        "correct": "[옫]",
        "explanation": "<p><strong>[옫]</strong> — “kiyim”. 받침 holatidagi ㅅ toʻxtaydi va "
                       "[ㄷ] boʻlib eshitiladi. “s” tovushi chiqmaydi.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>앞</strong></p>",
        "choices": ["[압]", "[아프]", "[앞]", "[안]"],
        "correct": "[압]",
        "explanation": "<p><strong>[압]</strong> — “old, oldi”. 받침 holatida <strong>ㅍ → "
                       "[ㅂ]</strong>, chunki toʻxtatilgan tovushda nafas farqi eshitilmay "
                       "qoladi.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>부엌</strong></p>",
        "choices": ["[부억]", "[부엌]", "[부어크]", "[부업]"],
        "correct": "[부억]",
        "explanation": "<p><strong>[부억]</strong> — “oshxona”. 받침 holatidagi ㅋ ham, ㄲ ham "
                       "[ㄱ] boʻlib oʻqiladi.</p>",
    },
    {
        "text": "<p>Bu uchtasi nega bir xil tugaydi?</p>"
                "<p><strong>옷 · 낮 · 꽃</strong></p>",
        "choices": ["ㅅ, ㅈ, ㅊ — uchalasi ham 받침da [ㄷ] boʻladi",
                    "Ular aslida bir xil soʻz",
                    "Ularning 받침i bir xil harf",
                    "Bu istisno, qoidasi yoʻq"],
        "correct": "ㅅ, ㅈ, ㅊ — uchalasi ham 받침da [ㄷ] boʻladi",
        "explanation": "<p>[옫], [낟], [꼳]. Bu uchta harfning farqi tovushni <em>chiqarishda</em> "
                       "edi, 받침 esa chiqarilmaydi — shuning uchun farq yoʻqoladi. Bu "
                       "<strong>yetti tovush qoidasi</strong>.</p>",
    },
    {
        "text": "<p>받침ni toʻgʻri aytish uchun nima qilish kerak?</p>",
        "choices": ["Tovushni boshlab, shu holatda toʻxtash",
                    "Tovushni kuchli chiqarish",
                    "Oxiriga qisqa unli qoʻshish",
                    "Nafasni kuchaytirish"],
        "correct": "Tovushni boshlab, shu holatda toʻxtash",
        "explanation": "<p>받침 <strong>portlatilmaydi</strong>: 밥 da lablar yumilgan holda "
                       "toʻxtaydi, hech qanday havo chiqmaydi. Bu chet ellik talaffuzining eng "
                       "sezilarli belgisi.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>꽃이</strong></p>",
        "choices": ["[꼬치]", "[꼳이]", "[꼬시]", "[꼳시]"],
        "correct": "[꼬치]",
        "explanation": "<p><strong>[꼬치]</strong>. Keyingi boʻgʻin unli bilan boshlangani uchun "
                       "받침 ㅊ <em>tiriladi</em> va oʻsha yoqqa koʻchadi. Yolgʻiz turganda esa "
                       "꽃 = [꼳].</p>",
    },
    {
        "text": "<p>Agar 꽃 [꼳] deb oʻqilsa, nega uni 꼳 deb yozmaymiz?</p>",
        "choices": ["Imlo soʻzning asl shaklini saqlaydi",
                    "꼳 degan boʻgʻin mavjud emas",
                    "Bu shunchaki eski anʼana",
                    "Chunki ㅊ chiroyliroq koʻrinadi"],
        "correct": "Imlo soʻzning asl shaklini saqlaydi",
        "explanation": "<p>Unli qoʻshilishi bilan ㅊ tiriladi: <strong>꽃이 → [꼬치]</strong>. Agar "
                       "꼳 deb yozilsa, bu bogʻlanish yoʻqolardi. Koreys imlosi maʼno boʻlagini "
                       "saqlaydi, talaffuz esa moslashadi.</p>",
    },
    {
        "text": "<p>Sherbek <strong>밥</strong> ni “pabı” deb aytdi. Nimani tuzatish kerak?</p>",
        "choices": ["받침ni portlatmaslik — lablar yumilgan holda toʻxtashi kerak",
                    "Birinchi undoshni nafasli aytish",
                    "Unlini uzunroq cho'zish",
                    "받침ni butunlay tushirib qoldirish"],
        "correct": "받침ni portlatmaslik — lablar yumilgan holda toʻxtashi kerak",
        "explanation": "<p>U oxiriga ortiqcha unli qoʻshdi. Toʻgʻrisi <strong>[밥]</strong> — "
                       "lablar yumiladi va shu holatda toʻxtaydi.</p>",
    },
    {
        "text": "<p>Qaysi javob notoʻgʻri?</p>",
        "choices": ["값 “kaps” deb, ikkala harf bilan oʻqiladi",
                    "밖 → [박]",
                    "받침 holatidagi ㅌ [ㄷ] boʻladi",
                    "받침 bitta yoki qoʻshaloq boʻlishi mumkin"],
        "correct": "값 “kaps” deb, ikkala harf bilan oʻqiladi",
        "explanation": "<p>Qoʻshaloq 받침da odatda <strong>bittasi</strong> oʻqiladi: "
                       "값 → <strong>[갑]</strong>. Ikkala harfni ham aytish notoʻgʻri.</p>",
    },
]


# =====================================================================
# PK-8 — Talaffuz qoidalari
# =====================================================================

Q_PK8 = [
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>연음화 nima?</strong></p>",
        "choices": ["받침ning keyingi boʻgʻinga koʻchishi",
                    "Undoshning qattiqlashishi",
                    "Burun tovushiga aylanish",
                    "ㅎ bilan nafasliga aylanish"],
        "correct": "받침ning keyingi boʻgʻinga koʻchishi",
        "explanation": "<p><strong>연음화</strong> — keyingi boʻgʻin unli bilan (ㅇ bilan) "
                       "boshlansa, 받침 oʻsha yoqqa koʻchadi: 한국어 → [한구거].</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>격음화da qaysi harf ishtirok etadi?</strong></p>",
        "choices": ["ㅎ", "ㅇ", "ㄹ", "ㅅ"],
        "correct": "ㅎ",
        "explanation": "<p><strong>ㅎ</strong> — nafasning oʻzi. U yonidagi oddiy undoshga "
                       "qoʻshilib, uni nafasliga aylantiradi: ㄱ+ㅎ → ㅋ, ㅂ+ㅎ → ㅍ.</p>",
    },
    {
        "text": "<p>Koreys imlosi talaffuzga qarab oʻzgaradimi?</p>",
        "choices": ["Yoʻq — imlo barqaror, talaffuz moslashadi",
                    "Ha, har doim qanday aytilsa shunday yoziladi",
                    "Faqat chet soʻzlarda oʻzgaradi",
                    "Faqat 받침da oʻzgaradi"],
        "correct": "Yoʻq — imlo barqaror, talaffuz moslashadi",
        "explanation": "<p>Koreys imlosi <strong>maʼno boʻlaklarini saqlaydi</strong>. 입니다 "
                       "[임니다] deb aytilsa ham, har doim 입니다 deb yoziladi — chunki 입 shu "
                       "shaklning oʻzagi.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>음악</strong></p>",
        "choices": ["[으막]", "[음악]", "[음막]", "[우막]"],
        "correct": "[으막]",
        "explanation": "<p><strong>[으막]</strong> — “musiqa”. 연음화: keyingi boʻgʻin ㅇ bilan "
                       "boshlangani uchun 음 ning 받침i (ㅁ) oʻsha yoqqa koʻchdi.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>학교</strong></p>",
        "choices": ["[학꾜]", "[학교]", "[하교]", "[학코]"],
        "correct": "[학꾜]",
        "explanation": "<p><strong>[학꾜]</strong> — “maktab”. 경음화: toʻxtovchi 받침 (ㄱ) dan "
                       "keyin kelgan oddiy undosh qattiqlashadi. Tomoq 받침da tarang qolgani "
                       "uchun bu oʻz-oʻzidan sodir boʻladi.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>먹다</strong></p>",
        "choices": ["[먹따]", "[먹다]", "[머따]", "[먹타]"],
        "correct": "[먹따]",
        "explanation": "<p><strong>[먹따]</strong> — “yemoq”. 경음화: 받침 ㄱ dan keyin oddiy ㄷ "
                       "qattiq ㄸ ga aylandi.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>한국말</strong></p>",
        "choices": ["[한궁말]", "[한국말]", "[한궁발]", "[하국말]"],
        "correct": "[한궁말]",
        "explanation": "<p><strong>[한궁말]</strong> — “koreys tili”. 비음화: 받침 ㄱ dan keyin "
                       "ㅁ kelgani uchun ㄱ burun tovushi <strong>ㅇ</strong> ga aylandi.</p>",
    },
    {
        "text": "<p>Bu shakl qanday oʻqiladi?</p><p><strong>입니다</strong></p>",
        "choices": ["[임니다]", "[입니다]", "[이니다]", "[입미다]"],
        "correct": "[임니다]",
        "explanation": "<p><strong>[임니다]</strong>. 비음화: ㅂ dan keyin ㄴ kelgani uchun ㅂ "
                       "burun tovushi ㅁ ga aylanadi. Bu koreys tilidagi eng koʻp ishlatiladigan "
                       "shakl — hozirdan toʻgʻri yodlang.</p>",
    },
    {
        "text": "<p><strong>축하 → [추카]</strong> — bu qaysi qoida?</p>",
        "choices": ["격음화", "연음화", "경음화", "비음화"],
        "correct": "격음화",
        "explanation": "<p><strong>격음화</strong> — 받침 ㄱ va keyingi ㅎ birikib nafasli ㅋ "
                       "beradi. ㅎ nafasning oʻzi boʻlgani uchun yonidagi undoshga "
                       "“yopishadi”.</p>",
    },
    {
        "text": "<p><strong>설날 → [설랄]</strong> — bu qaysi qoida?</p>",
        "choices": ["유음화", "비음화", "경음화", "연음화"],
        "correct": "유음화",
        "explanation": "<p><strong>유음화</strong> — ㄴ va ㄹ uchrashganda ikkalasi ham [ㄹ] "
                       "boʻladi: 설날 → [설랄], 신라 → [실라].</p>",
    },
    {
        "text": "<p>Afsona <strong>저는 학생입니다</strong> ni “...hak-seng ip-ni-da” deb "
                "oʻqidi. Toʻgʻrisi qaysi?</p>",
        "choices": ["[학쌩임니다]", "[학생임니다]", "[학쌩입니다]", "[학생입니다]"],
        "correct": "[학쌩임니다]",
        "explanation": "<p>Ikkita qoida ishlaydi: <strong>학생 → [학쌩]</strong> (경음화 — 받침 "
                       "ㄱ dan keyin ㅅ qattiqlashadi) va <strong>입니다 → [임니다]</strong> "
                       "(비음화 — ㅂ dan keyin ㄴ kelgani uchun ㅂ → ㅁ).</p>",
    },
    {
        "text": "<p>Qaysi javob notoʻgʻri?</p>",
        "choices": ["Talaffuzga qarab 임니다 deb yozish kerak",
                    "한국어 → [한구거]",
                    "좋아요 → [조아요]",
                    "입다 → [입따]"],
        "correct": "Talaffuzga qarab 임니다 deb yozish kerak",
        "explanation": "<p><strong>Imlo hech qachon oʻzgarmaydi</strong> — har doim "
                       "<strong>입니다</strong> deb yoziladi, faqat oʻqilishi [임니다] boʻladi. "
                       "Koreys yozuvi soʻzni saqlaydi, talaffuz esa ogʻizga moslashadi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-5 Mashq: Undoshlar 2 — ㅈ va nafasli ㅊ ㅋ ㅌ ㅍ ㅎ",
        "description": "12 savol — nafasli undoshlar, qogʻoz sinovi va ㅎ ning xatti-harakati.",
        "tutorial":    "PK-5:",
        "level":       "easy",
        "questions":   Q_PK5,
    },
    {
        "title":       "PK-6 Mashq: Undoshlar 3 — qattiq ㄲ ㄸ ㅃ ㅆ ㅉ",
        "description": "12 savol — qattiq undoshlar va koreys undoshlarining uchlik tizimi.",
        "tutorial":    "PK-6:",
        "level":       "easy",
        "questions":   Q_PK6,
    },
    {
        "title":       "PK-7 Mashq: Boʻgʻin bloklari va 받침",
        "description": "12 savol — blok shakllari, yetti tovush qoidasi va 받침 talaffuzi.",
        "tutorial":    "PK-7:",
        "level":       "easy",
        "questions":   Q_PK7,
    },
    {
        "title":       "PK-8 Mashq: Talaffuz qoidalari — 연음화, 격음화, 경음화, 비음화",
        "description": "12 savol — toʻrtta talaffuz qoidasi va imlo bilan talaffuz farqi.",
        "tutorial":    "PK-8:",
        "level":       "easy",
        "questions":   Q_PK8,
    },
]
