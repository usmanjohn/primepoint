# -*- coding: utf-8 -*-
"""Grammar bank — 종결어미 (sentence endings): nutq darajalari va ohang.

Order decade: 200-299. See STYLE_GUIDE_GRAMMAR.md.
"""

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

POINTS = [
    # ── Nutq darajalari ────────────────────────────────────────────────────
    {
        "pattern":   "-(스)ㅂ니다 / -(스)ㅂ니까?",
        "category":  "ending",
        "function":  "politeness",
        "level":     1,
        "freq":      3,
        "register":  "formal",
        "meaning":   "hurmatli rasmiy shakl (하십시오체) — xabar va so'roq",
        "attach":    "동사/형용사 + -(스)ㅂ니다",
        "form_rule": "받침 yo'q → <b>-ㅂ니다</b> (가다 → 갑니다) · 받침 bor → <b>-습니다</b> (먹다 → 먹습니다)"
                     "<br>ㄹ 받침 tushadi: 살다 → <b>삽니다</b>. So'roq: -ㅂ니까? / -습니까?",
        "note":      "<p>Eng rasmiy daraja: yangiliklar, e'lonlar, taqdimot, ish suhbati, armiya. "
                     "<b>TOPIK 듣기 va 읽기 da doim uchraydi.</b></p>"
                     "<p>쓰기 51-52 (rasmiy xat/e'lon) da ham shu shakl kerak.</p>",
        "examples": [
            ("저는 우즈베키스탄에서 왔습니다.", "Men O'zbekistondan keldim."),
            ("어디에서 근무하십니까?", "Qayerda ishlaysiz?"),
        ],
        "synonyms": [
            ("-아요/어요", "-아요/어요 = muloyim, lekin erkinroq (해요체); -습니다 = rasmiy, uzoq masofa"),
            ("-(느)ㄴ다", "-(느)ㄴ다 = yozma neytral (신문체) — 쓰기 53/54 uchun; -습니다 = rasmiy nutq"),
        ],
        "order": 200,
    },
    {
        "pattern":   "-아요/어요",
        "category":  "ending",
        "function":  "politeness",
        "level":     1,
        "freq":      3,
        "register":  "polite",
        "meaning":   "muloyim kundalik shakl (해요체)",
        "attach":    "동사/형용사 + -아요/어요",
        "form_rule": "Oxirgi unli ㅏ yoki ㅗ → <b>-아요</b> (가다 → 가요, 좋다 → 좋아요)<br>"
                     "Boshqa unlilar → <b>-어요</b> (먹다 → 먹어요, 마시다 → 마셔요)<br>"
                     "하다 → <b>해요</b>",
        "note":      "<p>Bir xil shakl <b>to'rt vazifani</b> bajaradi — ohang farqlaydi: "
                     "xabar (가요.), so'roq (가요?), buyruq (가요!), taklif (같이 가요~).</p>"
                     "<p>⚠️ 쓰기 53/54 inshosida <b>ishlatilmaydi</b> — u yerda -(느)ㄴ다 kerak.</p>",
        "mistake":   "<p>❌ 쓰기 54: 환경 문제가 심각<b>해요</b>. → ✅ 환경 문제가 심각<b>하다</b>. "
                     "Inshoda 해요체 ishlatish ball yo'qotadi.</p>",
        "examples": [
            ("아침마다 커피를 마셔요.", "Har kuni ertalab qahva ichaman."),
            ("주말에 뭐 해요?", "Dam olish kuni nima qilasiz?"),
        ],
        "synonyms": [
            ("-(스)ㅂ니다", "-습니다 = rasmiyroq va uzoqroq; -아요 = muloyim, iliq"),
            ("-아/어 (반말)", "요 ni olib tashlasangiz — 반말 (yaqin do'st, kichik yoshdagilar bilan)"),
        ],
        "order": 201,
    },
    {
        "pattern":   "-(느)ㄴ다 / -다",
        "category":  "ending",
        "function":  "politeness",
        "level":     3,
        "freq":      3,
        "register":  "written",
        "meaning":   "yozma neytral shakl (한다체) — insho, gazeta, kitob",
        "attach":    "동사 + -(느)ㄴ다 · 형용사 + -다 · 명사 + -이다",
        "form_rule": "Fe'l, 받침 yo'q → <b>-ㄴ다</b> (가다 → 간다) · 받침 bor → <b>-는다</b> (먹다 → 먹는다)<br>"
                     "Sifat o'zgarmaydi: 좋다 → <b>좋다</b> · Ot: 학생<b>이다</b><br>"
                     "O'tgan zamon hamma uchun bir xil: <b>-았/었다</b>",
        "note":      "<p><b>TOPIK 쓰기 53 va 54 ning majburiy uslubi.</b> Butun insho shu shaklda "
                     "yozilishi kerak — bitta 해요체 jumla ham ball tushiradi.</p>"
                     "<p>Gazeta sarlavhalari, ilmiy matn, 읽기 41-50 parchalari ham shu uslubda.</p>",
        "mistake":   "<p>Insho o'rtasida uslub almashib ketishi — eng ko'p uchraydigan 쓰기 xatosi. "
                     "Yozib bo'lgach, <b>har bir jumlaning oxirini tekshiring</b>.</p>",
        "examples": [
            ("현대 사회에서 환경 문제는 점점 심각해진다.", "Zamonaviy jamiyatda ekologiya muammosi tobora jiddiylashmoqda."),
            ("조사 결과 응답자의 절반이 찬성했다.", "So'rov natijasiga ko'ra respondentlarning yarmi rozi bo'lgan."),
        ],
        "synonyms": [
            ("-(스)ㅂ니다", "-습니다 = og'zaki rasmiy (nutq, e'lon); -(느)ㄴ다 = yozma neytral (insho, maqola)"),
            ("-아요/어요", "쓰기 53/54 da -아요 ishlatib bo'lmaydi — faqat -(느)ㄴ다"),
        ],
        "order": 202,
    },

    # ── So'roq, taklif, buyruq ─────────────────────────────────────────────
    {
        "pattern":   "-(으)세요",
        "category":  "ending",
        "function":  "politeness",
        "level":     1,
        "freq":      3,
        "register":  "polite",
        "meaning":   "muloyim buyruq/iltimos va hurmatli xabar",
        "attach":    "동사 + -(으)세요",
        "form_rule": "받침 yo'q → <b>-세요</b> (가다 → 가세요) · 받침 bor → <b>-으세요</b> (읽다 → 읽으세요)<br>"
                     "Maxsus shakllar: 먹다 → <b>드세요</b>, 자다 → <b>주무세요</b>, 있다 → <b>계세요</b>",
        "note":      "<p>Ikki ma'no: <b>iltimos</b> (여기 앉<b>으세요</b> — bu yerga o'tiring) va "
                     "<b>hurmatli xabar/so'roq</b> (선생님이 오<b>세요</b> — ustoz kelyaptilar).</p>"
                     "<p>Inkori: <b>-지 마세요</b> — 사진을 찍<b>지 마세요</b>.</p>",
        "examples": [
            ("여기에 이름을 쓰세요.", "Bu yerga ismingizni yozing."),
            ("할머니께서는 지금 주무세요.", "Buvim hozir uxlayaptilar."),
        ],
        "synonyms": [
            ("-아/어 주세요", "-아 주세요 = «men uchun qiling» (iltimos, xizmat); -(으)세요 = oddiy ko'rsatma"),
            ("-(으)십시오", "-(으)십시오 = eng rasmiy buyruq (e'lon, xizmat ko'rsatish); -(으)세요 = kundalik"),
        ],
        "order": 203,
    },
    {
        "pattern":   "-(으)ㄹ까요?",
        "category":  "ending",
        "function":  "intention",
        "level":     1,
        "freq":      3,
        "meaning":   "«-aylikmi? -sammikin?» — taklif, fikr so'rash, taxmin",
        "attach":    "동사 + -(으)ㄹ까요?",
        "form_rule": "받침 yo'q → <b>-ㄹ까요</b> (가다 → 갈까요) · 받침 bor → <b>-을까요</b> (먹다 → 먹을까요)",
        "note":      "<p>Uch ma'no:</p><ul>"
                     "<li><b>Taklif</b> (biz): 같이 갈<b>까요</b>? — birga boraylikmi?</li>"
                     "<li><b>Fikr so'rash</b> (men): 제가 도와드릴<b>까요</b>? — yordam beraymi?</li>"
                     "<li><b>Taxmin</b> (uchinchi shaxs): 내일 비가 올<b>까요</b>? — ertaga yomg'ir yog'armikin?</li></ul>",
        "examples": [
            ("점심을 같이 먹을까요?", "Tushlikni birga yeymizmi?"),
            ("이 옷이 아프소나한테 어울릴까요?", "Bu kiyim Afsonaga yarasharmikin?"),
        ],
        "synonyms": [
            ("-(으)ㅂ시다", "-ㅂ시다 = qat'iy taklif («qilaylik»); -(으)ㄹ까요 = fikrini so'raydi («qilaylikmi?»)"),
            ("-(으)ㄹ래요?", "-(으)ㄹ래요 = erkin, do'stona («xohlaysanmi?»); -(으)ㄹ까요 = muloyimroq"),
        ],
        "order": 204,
    },
    {
        "pattern":   "-(으)ㅂ시다",
        "category":  "ending",
        "function":  "intention",
        "level":     1,
        "freq":      2,
        "register":  "formal",
        "meaning":   "«-aylik» — taklif (qat'iy)",
        "attach":    "동사 + -(으)ㅂ시다",
        "form_rule": "받침 yo'q → <b>-ㅂ시다</b> (가다 → 갑시다) · 받침 bor → <b>-읍시다</b> (먹다 → 먹읍시다)",
        "note":      "<p>⚠️ Kattalarga (ustoz, boshliq) nisbatan ishlatilmaydi — u holda "
                     "<b>-(으)시겠어요?</b> yoki <b>-(으)ㄹ까요?</b> deyiladi.</p>",
        "examples": [
            ("시간이 없으니까 택시를 탑시다.", "Vaqt yo'q, taksi olaylik."),
            ("다시 한번 생각해 봅시다.", "Yana bir bor o'ylab ko'raylik."),
        ],
        "synonyms": [
            ("-(으)ㄹ까요?", "-(으)ㄹ까요 = ruxsat so'raydi; -(으)ㅂ시다 = qaror aytadi"),
            ("-아요/어요", "가요~ ohangi bilan ham taklif bo'ladi — eng yumshoq varianti"),
        ],
        "order": 205,
    },
    {
        "pattern":   "-(으)ㄹ래요",
        "category":  "ending",
        "function":  "intention",
        "level":     2,
        "freq":      2,
        "register":  "polite",
        "meaning":   "«-moqchiman / -asanmi?» — o'z xohishi va do'stona taklif",
        "attach":    "동사 + -(으)ㄹ래요",
        "form_rule": "받침 yo'q → <b>-ㄹ래요</b> · 받침 bor → <b>-을래요</b>",
        "note":      "<p>Faqat <b>o'zim</b> (xohish) yoki <b>sen/siz</b> (so'roq) uchun — uchinchi shaxsga "
                     "ishlatilmaydi. Erkin ohang, shuning uchun ustozga aytilmaydi.</p>",
        "mistake":   "<p>❌ 선생님, 커피 드<b>실래요</b>? biroz erkin. ✅ 선생님, 커피 <b>드시겠어요</b>?</p>",
        "examples": [
            ("저는 집에서 쉴래요.", "Men uyda dam olaman."),
            ("주말에 같이 영화 볼래요?", "Dam olish kuni birga kino ko'ramizmi?"),
        ],
        "synonyms": [
            ("-고 싶다", "-고 싶다 = ichki xohish («istayman»); -(으)ㄹ래요 = qaror va e'lon («qilaman»)"),
            ("-(으)ㄹ게요", "-(으)ㄹ게요 = tinglovchiga va'da; -(으)ㄹ래요 = o'z xohishi"),
        ],
        "order": 206,
    },
    {
        "pattern":   "-(으)ㄹ게요",
        "category":  "ending",
        "function":  "intention",
        "level":     2,
        "freq":      2,
        "register":  "polite",
        "meaning":   "«-aman» — tinglovchiga qaratilgan va'da/qaror",
        "attach":    "동사 + -(으)ㄹ게요",
        "form_rule": "받침 yo'q → <b>-ㄹ게요</b> · 받침 bor → <b>-을게요</b>. Talaffuzi [ㄹ께요].",
        "note":      "<p>Faqat <b>1-shaxs</b> uchun va faqat tinglovchi bo'lganda. "
                     "«Sen aytganingdek qilaman» ohangi bor.</p>",
        "mistake":   "<p>❌ 내일 비가 <b>올게요</b> → ✅ 내일 비가 <b>올 거예요</b>. "
                     "Ob-havo va'da bera olmaydi — -(으)ㄹ게요 faqat «men» uchun.</p>",
        "examples": [
            ("제가 먼저 갈게요.", "Men oldinroq boraman."),
            ("내일까지 숙제를 끝낼게요.", "Ertagacha uy vazifasini tugataman."),
        ],
        "synonyms": [
            ("-(으)ㄹ 거예요", "-(으)ㄹ 거예요 = oddiy reja/taxmin, tinglovchi shart emas; -(으)ㄹ게요 = va'da"),
            ("-(으)ㄹ래요", "-(으)ㄹ래요 = «xohlayman»; -(으)ㄹ게요 = «sen uchun shunday qilaman»"),
        ],
        "order": 207,
    },

    # ── His-tuyg'u va ohang ────────────────────────────────────────────────
    {
        "pattern":   "-네요",
        "category":  "ending",
        "function":  "feeling",
        "level":     2,
        "freq":      3,
        "register":  "polite",
        "meaning":   "«-ekan!» — hozir bilib, hayron bo'lish",
        "attach":    "동사/형용사 + -네요",
        "form_rule": "받침ga qaramay <b>-네요</b>. ㄹ tushadi: 멀다 → <b>머네요</b>. "
                     "O'tgan zamon: <b>-았/었네요</b>.",
        "note":      "<p><b>Aynan shu daqiqada</b> ko'rib/eshitib bilingan narsaga reaksiya. "
                     "TOPIK 듣기 dialoglarida juda tez-tez uchraydi.</p>",
        "examples": [
            ("와, 한국어를 정말 잘하시네요!", "Voy, koreyschani juda yaxshi bilar ekansiz!"),
            ("밖에 눈이 오네요.", "Tashqarida qor yog'ayapti-ku."),
        ],
        "synonyms": [
            ("-군요", "-군요 = «demak shunday ekan» (tushunib yetish, kitobiy); -네요 = to'g'ridan-to'g'ri hayrat"),
            ("-잖아요", "-잖아요 = «axir bilasiz-ku» (ma'lum narsani eslatish); -네요 = yangi bilib olish"),
        ],
        "order": 210,
    },
    {
        "pattern":   "-군요 / -는군요",
        "category":  "ending",
        "function":  "discovery",
        "level":     3,
        "freq":      2,
        "meaning":   "«demak, shunday ekan» — tushunib yetish",
        "attach":    "형용사 + -군요 · 동사 + -는군요",
        "form_rule": "Sifat → <b>-군요</b> (춥다 → 춥군요) · Fe'l → <b>-는군요</b> (가다 → 가는군요)<br>"
                     "O'tgan zamon hamma uchun: <b>-았/었군요</b>. 반말: <b>-구나</b>.",
        "note":      "<p>Suhbatdoshdan eshitib yoki o'zi ko'rib <b>xulosa chiqarish</b> ohangi: "
                     "«ha-a, demak shunaqa». 네요 dan biroz kitobiyroq.</p>",
        "examples": [
            ("그래서 어제 학교에 안 왔군요.", "Demak, shuning uchun kecha maktabga kelmagan ekansiz."),
            ("여기가 유명한 식당이구나.", "Bu yer o'sha mashhur restoran ekan-da."),
        ],
        "synonyms": [
            ("-네요", "-네요 = darhol hayrat; -군요 = sababini tushunib yetish"),
            ("-더라고요", "-더라고요 = o'zim ko'rgan tajribamni aytish; -군요 = hozir bilib olish"),
        ],
        "order": 211,
    },
    {
        "pattern":   "-지요? / -죠?",
        "category":  "ending",
        "function":  "feeling",
        "level":     2,
        "freq":      3,
        "register":  "polite",
        "meaning":   "«-a? shundaymi?» — tasdiq so'rash",
        "attach":    "동사/형용사/명사 + -지요?",
        "form_rule": "Og'zaki nutqda <b>-죠</b> ga qisqaradi.",
        "note":      "<p>So'zlovchi javobni <b>allaqachon biladi</b>, faqat tasdiq kutadi. "
                     "So'roqsiz (xabar) shaklda «albatta, shunday» ma'nosini beradi: "
                     "<i>제가 하<b>죠</b>.</i></p>",
        "examples": [
            ("오늘 날씨가 좋지요?", "Bugun ob-havo yaxshi-a?"),
            ("자수르 씨도 학생이죠?", "Jasur ham talaba-ku, shundaymi?"),
        ],
        "synonyms": [
            ("-잖아요", "-잖아요 = «axir shunday-ku» (eslatish, biroz qat'iy); -지요 = muloyim tasdiq so'rash"),
            ("-네요", "-네요 = o'zi yangi bilib oldi; -지요 = ikkalasi ham biladi"),
        ],
        "order": 212,
    },
    {
        "pattern":   "-잖아요",
        "category":  "ending",
        "function":  "feeling",
        "level":     3,
        "freq":      2,
        "register":  "polite",
        "meaning":   "«axir ... -ku» — ma'lum narsani eslatish",
        "attach":    "동사/형용사 + -잖아요",
        "form_rule": "O'tgan zamon: <b>-았/었잖아요</b>. Ot: 학생<b>이잖아요</b>.",
        "note":      "<p>Tinglovchi <b>biladi</b> deb hisoblanadi — shuning uchun begonaga yoki "
                     "kattaga ishlatilsa qo'pol tuyulishi mumkin.</p>",
        "examples": [
            ("오늘 일요일이잖아요. 은행이 문을 닫았어요.", "Axir bugun yakshanba-ku. Bank yopiq."),
            ("제가 어제 말했잖아요.", "Men kecha aytdim-ku."),
        ],
        "synonyms": [
            ("-지요", "-지요 = muloyim tasdiq; -잖아요 = «bilasiz-ku» (biroz tanbeh ohangi)"),
            ("-거든요", "-거든요 = tinglovchi BILMAGAN sababni aytadi; -잖아요 = biladigan narsani eslatadi"),
        ],
        "order": 213,
    },
    {
        "pattern":   "-거든요",
        "category":  "ending",
        "function":  "reason",
        "level":     3,
        "freq":      2,
        "register":  "polite",
        "meaning":   "«chunki, gap shundaki» — noma'lum sababni aytish",
        "attach":    "동사/형용사 + -거든요",
        "form_rule": "받침ga qaramay <b>-거든요</b>. O'tgan zamon: <b>-았/었거든요</b>.",
        "note":      "<p>Tinglovchi <b>bilmaydigan</b> sabab yoki ma'lumotni beradi. Ko'pincha "
                     "gapning ikkinchi qismida keladi: <i>— 왜 안 갔어요? — 시간이 없<b>었거든요</b>.</i></p>",
        "examples": [
            ("오늘 일찍 가요. 병원에 가야 하거든요.", "Bugun erta ketaman. Shifoxonaga borishim kerak."),
            ("이 식당을 잘 알아요. 자주 오거든요.", "Bu restoranni yaxshi bilaman. Tez-tez kelaman."),
        ],
        "synonyms": [
            ("-잖아요", "-잖아요 = tinglovchi biladi; -거든요 = tinglovchi bilmaydi"),
            ("-아서/어서", "-아서 = gap ichida sabab; -거든요 = alohida jumla bo'lib sababni qo'shadi"),
        ],
        "order": 214,
    },
    {
        "pattern":   "-더라고요",
        "category":  "ending",
        "function":  "experience",
        "level":     4,
        "freq":      2,
        "register":  "polite",
        "meaning":   "«ko'rsam ... ekan» — o'zi guvoh bo'lgan narsani aytish",
        "attach":    "동사/형용사 + -더라고요",
        "form_rule": "반말: <b>-더라</b>. O'tgan zamon: <b>-았/었더라고요</b>.",
        "note":      "<p>⚠️ <b>O'zi shaxsan ko'rgan/eshitgan</b> narsa haqida. Shuning uchun "
                     "o'z his-tuyg'ungizga (내가 기쁘더라고요 ❌) ishlatilmaydi — "
                     "boshqaning holatiga ishlatiladi.</p>",
        "examples": [
            ("어제 그 영화를 봤는데 정말 재미있더라고요.", "Kecha o'sha kinoni ko'rdim — rostdan qiziq ekan."),
            ("시장에 가 보니까 사람이 많더라고요.", "Bozorga borsam, odam ko'p ekan."),
        ],
        "synonyms": [
            ("-군요", "-군요 = hozir bilib oldi; -더라고요 = o'tmishda ko'rgan tajribasini aytmoqda"),
            ("-던데요", "-던데요 = eslatib, javob kutadi; -더라고요 = shunchaki xabar beradi"),
        ],
        "order": 215,
    },
    {
        "pattern":   "-(으)ㄴ/는데요",
        "category":  "ending",
        "function":  "feeling",
        "level":     3,
        "freq":      2,
        "register":  "polite",
        "meaning":   "yumshoq xabar / e'tiroz / davomini kutish ohangi",
        "attach":    "동사 + -는데요 · 형용사 + -(으)ㄴ데요",
        "form_rule": "Fe'l → <b>-는데요</b> (가다 → 가는데요) · Sifat, 받침 yo'q → <b>-ㄴ데요</b> (크다 → 큰데요) · "
                     "받침 bor → <b>-은데요</b> (좋다 → 좋은데요)",
        "note":      "<p>Gapni <b>tugatmasdan</b> tugatadi — «...-ku, xo'sh?» ohangi. "
                     "Yumshoq rad javobi uchun ideal: <i>지금은 좀 바쁜<b>데요</b>...</i></p>",
        "examples": [
            ("그 책은 지금 없는데요.", "U kitob hozir yo'q-ku..."),
            ("날씨가 정말 좋은데요!", "Ob-havo juda ham yaxshi-ku!"),
        ],
        "synonyms": [
            ("-지만", "-지만 = aniq qarama-qarshilik; -는데 = yumshoq fon/kirish"),
            ("-거든요", "-거든요 = sababni aytadi; -는데요 = javobni tinglovchiga qoldiradi"),
        ],
        "order": 216,
    },
    {
        "pattern":   "-(으)ㄹ 거예요",
        "category":  "ending",
        "function":  "guess",
        "level":     1,
        "freq":      3,
        "meaning":   "«-aman / -sa kerak» — kelasi zamon va taxmin",
        "attach":    "동사/형용사 + -(으)ㄹ 거예요",
        "form_rule": "받침 yo'q → <b>-ㄹ 거예요</b> · 받침 bor → <b>-을 거예요</b><br>"
                     "Rasmiy: <b>-(으)ㄹ 것입니다</b> · Yozma: <b>-(으)ㄹ 것이다</b>",
        "note":      "<p>1-shaxs bilan = <b>reja</b> (저는 갈 거예요). "
                     "3-shaxs bilan = <b>taxmin</b> (아프소나는 안 올 거예요).</p>"
                     "<p>쓰기 54 da yozma shakli <b>-(으)ㄹ 것이다</b> juda kerak.</p>",
        "examples": [
            ("내년에 한국에 갈 거예요.", "Kelasi yil Koreyaga boraman."),
            ("이 문제는 쉽게 해결될 것이다.", "Bu muammo oson hal bo'ladi."),
        ],
        "synonyms": [
            ("-겠-", "-겠- = qat'iy niyat yoki hozirgi taxmin; -(으)ㄹ 거예요 = reja, kuchsizroq taxmin"),
            ("-(으)ㄹ게요", "-(으)ㄹ게요 = tinglovchiga va'da; -(으)ㄹ 거예요 = shunchaki reja"),
        ],
        "order": 217,
    },
    {
        "pattern":   "-지 마세요",
        "category":  "ending",
        "function":  "obligation",
        "level":     1,
        "freq":      2,
        "meaning":   "«-mang» — taqiq",
        "attach":    "동사 + -지 마세요",
        "form_rule": "Rasmiy: <b>-지 마십시오</b> · 반말: <b>-지 마</b> · Taklif: <b>-지 맙시다</b>",
        "note":      "<p>E'lon va ogohlantirishlarda <b>-지 마십시오</b> shakli uchraydi — "
                     "TOPIK 읽기 ning 안내문 savollarida ko'p ko'rasiz.</p>",
        "examples": [
            ("여기에서 사진을 찍지 마세요.", "Bu yerda surat olmang."),
            ("잔디밭에 들어가지 마십시오.", "Maysazorga kirmang."),
        ],
        "synonyms": [
            ("-(으)면 안 되다", "-(으)면 안 되다 = «mumkin emas» (qoida); -지 마세요 = to'g'ridan-to'g'ri buyruq"),
        ],
        "order": 218,
    },
]
