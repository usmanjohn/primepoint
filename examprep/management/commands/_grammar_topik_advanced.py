# -*- coding: utf-8 -*-
"""Grammar bank — 고급 문형: advanced patterns for TOPIK 5-6 (읽기 41-50, 쓰기 53-54).

Order decade: 600-699. See STYLE_GUIDE_GRAMMAR.md.
"""

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

POINTS = [
    {
        "pattern":   "-(으)ㄹ 뿐만 아니라",
        "category":  "expression",
        "function":  "listing",
        "level":     5,
        "freq":      3,
        "register":  "written",
        "meaning":   "«faqat ... emas, balki ... ham»",
        "attach":    "동사/형용사 + -(으)ㄹ 뿐만 아니라 · 명사 + 뿐만 아니라",
        "form_rule": "Fe'l/sifat: 싸<b>ㄹ 뿐만 아니라</b> · Ot: 학생<b>뿐만 아니라</b><br>"
                     "O'tgan: <b>-았/었을 뿐만 아니라</b>",
        "note":      "<p><b>쓰기 54 uchun eng foydali qo'shish iborasi.</b> Ikkinchi qism birinchisidan "
                     "kuchliroq bo'lishi kerak.</p>"
                     "<p>Tayyor qolip: <i>이 방법은 비용이 적게 들 <b>뿐만 아니라</b> 효과도 크다.</i></p>",
        "examples": [
            ("이 제품은 값이 쌀 뿐만 아니라 품질도 좋다.", "Bu mahsulot arzon bo'libgina qolmay, sifati ham yaxshi."),
            ("환경 오염은 건강뿐만 아니라 경제에도 영향을 미친다.", "Ekologik ifloslanish sog'liqqagina emas, iqtisodga ham ta'sir qiladi."),
        ],
        "synonyms": [
            ("-(으)ㄴ/는 데다가", "-는 데다가 = «ustiga-ustak» (og'zakiroq); -(으)ㄹ 뿐만 아니라 = yozma, rasmiy"),
            ("게다가", "게다가 = bog'lovchi ravish, yangi jumla boshlaydi"),
        ],
        "order": 600,
    },
    {
        "pattern":   "-(으)ㄴ/는 데다가",
        "category":  "connective",
        "function":  "listing",
        "level":     5,
        "freq":      2,
        "meaning":   "«ustiga-ustak, buning ustiga»",
        "attach":    "동사 + -는 데다가 · 형용사 + -(으)ㄴ 데다가",
        "form_rule": "Ikki qism <b>bir xil yo'nalishda</b> bo'lishi shart (ikkalasi ijobiy yoki "
                     "ikkalasi salbiy).",
        "note":      "<p>❌ 값이 싼 데다가 품질이 나쁘다 — bu noto'g'ri (biri ijobiy, biri salbiy). "
                     "Bunday holatda <b>-지만</b> kerak.</p>",
        "examples": [
            ("비가 오는 데다가 바람까지 불어서 춥다.", "Yomg'ir yog'ayotgani ustiga shamol ham esib, sovuq."),
            ("실력이 좋은 데다가 성실하기까지 하다.", "Saviyasi yaxshi bo'lgani ustiga mehnatkash ham."),
        ],
        "synonyms": [
            ("-(으)ㄹ 뿐만 아니라", "ma'nosi bir xil; -는 데다가 og'zakiroq, -(으)ㄹ 뿐만 아니라 yozma"),
        ],
        "order": 601,
    },
    {
        "pattern":   "-(으)ㅁ에 따라 / -(으)ㅁ에 따르면",
        "category":  "expression",
        "function":  "reason",
        "level":     5,
        "freq":      3,
        "register":  "written",
        "meaning":   "«-ga qarab, -ga ko'ra» — bog'liqlik va manba",
        "attach":    "명사 + 에 따라 · 동사 + -(으)ㅁ에 따라 · 명사 + 에 따르면",
        "form_rule": "<b>에 따라</b> = «...ga qarab o'zgaradi» · <b>에 따르면</b> = «...ga ko'ra» (manba)",
        "note":      "<p><b>쓰기 53 ning eng kerakli iborasi</b> — grafik manbasini ko'rsatadi: "
                     "<i>조사 결과<b>에 따르면</b> ...</i></p>"
                     "<p>Bog'liqlik uchun: <i>소득이 증가함<b>에 따라</b> 소비도 늘었다.</i></p>",
        "examples": [
            ("통계청 자료에 따르면 1인 가구가 크게 늘었다.", "Statistika qo'mitasi ma'lumotiga ko'ra yolg'iz yashovchi xonadonlar keskin ko'paydi."),
            ("기술이 발전함에 따라 일자리 구조가 변하고 있다.", "Texnologiya rivojlangani sari ish o'rinlari tuzilishi o'zgarmoqda."),
        ],
        "synonyms": [
            ("-(으)ㄹ수록", "-(으)ㄹ수록 = «...-gan sari» (og'zakiroq); -(으)ㅁ에 따라 = rasmiy, hisobot uslubi"),
            ("(으)로 인해", "(으)로 인해 = sabab-natija; 에 따라 = mutanosib o'zgarish"),
        ],
        "order": 602,
    },
    {
        "pattern":   "-기 마련이다 / -게 마련이다",
        "category":  "expression",
        "function":  "guess",
        "level":     5,
        "freq":      2,
        "register":  "written",
        "meaning":   "«tabiiy, albatta shunday bo'ladi»",
        "attach":    "동사/형용사 + -기/-게 마련이다",
        "form_rule": "Ikki shakl ham to'g'ri va bir xil ma'noda.",
        "note":      "<p>Umumiy haqiqat va tabiiy qonuniyat haqida. 쓰기 54 da fikrni "
                     "umumlashtirishda kuchli ta'sir beradi.</p>",
        "examples": [
            ("사람은 누구나 실수하기 마련이다.", "Har qanday odam xato qilishi tabiiy."),
            ("노력하면 좋은 결과가 나오게 마련이다.", "Harakat qilsang, yaxshi natija chiqishi tabiiy."),
        ],
        "synonyms": [
            ("-는 법이다", "-는 법이다 = «qoidasi shunday» — deyarli bir xil, biroz kitobiyroq"),
        ],
        "order": 603,
    },
    {
        "pattern":   "-더니 / -았/었더니",
        "category":  "connective",
        "function":  "discovery",
        "level":     5,
        "freq":      3,
        "meaning":   "-더니 = «...-gan edi, natijada» · -았더니 = «men ...-gan edim, natijada»",
        "attach":    "동사/형용사 + -더니 · 동사 + -았/었더니",
        "form_rule": "<b>-더니</b>: ega = <b>boshqa odam</b>, men ko'rgan holat<br>"
                     "<b>-았/었더니</b>: ega = <b>men</b>, mening harakatim natijasi",
        "note":      "<p>TOPIK 5-6 da eng ko'p chalkashtiriladigan juftlik:</p>"
                     "<ul><li><i>아프소나가 열심히 공부하<b>더니</b> 1등을 했다.</i> — Afsona tirishib "
                     "o'qigan edi, natijada birinchi bo'ldi. (men kuzatdim)</li>"
                     "<li><i>아침을 안 먹<b>었더니</b> 배가 고프다.</i> — Nonushta qilmagan edim, "
                     "natijada qornim och. (o'zim)</li></ul>",
        "mistake":   "<p>❌ 내가 공부하<b>더니</b> 1등을 했다 → o'zim haqimda 더니 ishlatilmaydi. "
                     "✅ 공부<b>했더니</b>.</p>",
        "examples": [
            ("동생이 감기에 걸리더니 결국 병원에 갔다.", "Ukam shamollagan edi, oxiri shifoxonaga bordi."),
            ("운동을 시작했더니 건강이 좋아졌다.", "Sport bilan shug'ullana boshlagan edim, sog'ligim yaxshilandi."),
        ],
        "synonyms": [
            ("-아서/어서", "-아서 = oddiy sabab; -았더니 = «men shunday qildim, natijada BILDIM/BO'LDI»"),
            ("-더라고요", "-더라고요 = ko'rgan narsani xabar qiladi; -더니 = ko'rgan narsa + natijasi"),
        ],
        "order": 604,
    },
    {
        "pattern":   "-(으)ㄴ/는 셈이다",
        "category":  "expression",
        "function":  "degree",
        "level":     5,
        "freq":      2,
        "register":  "written",
        "meaning":   "«hisobda shunday chiqadi, deyarli shunday»",
        "attach":    "동사 + -는 셈이다 · 형용사 + -(으)ㄴ 셈이다",
        "form_rule": "O'tgan: <b>-(으)ㄴ 셈이다</b>",
        "note":      "<p>Aniq shunday emas, lekin <b>hisob-kitob qilsak natija bir xil</b>. "
                     "쓰기 53 da grafikni umumlashtirishda foydali.</p>",
        "examples": [
            ("숙제를 거의 다 했으니까 끝난 셈이다.", "Uy vazifasining deyarli hammasini qildim, demak tugagan hisob."),
            ("열 명 중 아홉 명이 찬성했으니 모두 동의한 셈이다.", "O'n kishidan to'qqiztasi rozi bo'ldi — hammasi rozi hisob."),
        ],
        "synonyms": [
            ("-(으)ㄴ/는 편이다", "-는 편이다 = moyillik; -는 셈이다 = hisob-kitob xulosasi"),
        ],
        "order": 605,
    },
    {
        "pattern":   "-(으)ㄴ 채(로)",
        "category":  "expression",
        "function":  "change",
        "level":     5,
        "freq":      2,
        "meaning":   "«-gan holicha (o'zgartirmasdan)»",
        "attach":    "동사 + -(으)ㄴ 채(로)",
        "form_rule": "Doim <b>-(으)ㄴ</b> shaklida (o'tgan aniqlovchi). Inkor: <b>-지 않은 채</b>.",
        "note":      "<p>Bir holat <b>saqlanib turgan holda</b> boshqa ish qilinadi — ko'pincha "
                     "g'ayrioddiy yoki noqulay holat.</p>",
        "examples": [
            ("신발을 신은 채로 방에 들어갔다.", "Oyoq kiyimni yechmasdan xonaga kirdi."),
            ("불을 켠 채 잠이 들었어요.", "Chiroqni o'chirmasdan uxlab qoldim."),
        ],
        "synonyms": [
            ("-(으)면서", "-(으)면서 = ikki harakat birga; -(으)ㄴ 채로 = birinchi HOLAT saqlanadi"),
            ("-아/어 있다", "-아 있다 = holatning o'zini bildiradi; -(으)ㄴ 채로 = «shu holatda» qo'shimcha ish"),
        ],
        "order": 606,
    },
    {
        "pattern":   "-기는커녕 / -기는 하지만",
        "category":  "connective",
        "function":  "contrast",
        "level":     5,
        "freq":      2,
        "meaning":   "«u yoqda tursin» · «...-ishi -adi-yu, lekin»",
        "attach":    "동사/형용사 + -기는커녕 · -기는 하지만",
        "form_rule": "<b>-기는커녕</b> = kutilganini ham, undan kichigini ham inkor qiladi<br>"
                     "<b>-기는 하지만</b> = qisman tan olib, keyin qarshi chiqadi (qisqargani: <b>-긴 하지만</b>)",
        "note":      "<p><b>-기는 하지만</b> munozara inshosida juda foydali — qarama-qarshi fikrni "
                     "tan olib, keyin o'z fikrini aytish: <i>편리하<b>기는 하지만</b> 부작용도 있다.</i></p>",
        "examples": [
            ("쉬기는커녕 밥 먹을 시간도 없었다.", "Dam olish u yoqda tursin, ovqatlanishga ham vaqt bo'lmadi."),
            ("이 방법이 효과적이기는 하지만 비용이 많이 든다.", "Bu usul samarali-yu, lekin xarajati ko'p."),
        ],
        "synonyms": [
            ("은/는커녕", "otga qo'shiladigan varianti"),
            ("-지만", "-지만 = oddiy qarshilik; -기는 하지만 = avval tan oladi, keyin qarshi chiqadi"),
        ],
        "order": 607,
    },
    {
        "pattern":   "-(으)ㅁ에도 불구하고",
        "category":  "connective",
        "function":  "concession",
        "level":     5,
        "freq":      3,
        "register":  "written",
        "meaning":   "«-ga qaramasdan» — rasmiy qarshi qo'yish",
        "attach":    "동사/형용사 + -(으)ㅁ에도 불구하고 · 명사 + 에도 불구하고",
        "form_rule": "Fe'lni ot qilish: 노력하다 → 노력<b>함</b> → 노력함<b>에도 불구하고</b><br>"
                     "Ot: 노력<b>에도 불구하고</b>",
        "note":      "<p><b>쓰기 54 uchun eng yuqori darajali qarshi qo'yish iborasi.</b> "
                     "-는데도 ning rasmiy varianti.</p>",
        "examples": [
            ("여러 대책에도 불구하고 문제는 해결되지 않았다.", "Ko'plab chora-tadbirlarga qaramasdan muammo hal bo'lmadi."),
            ("경제가 어려움에도 불구하고 소비는 증가했다.", "Iqtisod og'ir bo'lishiga qaramay iste'mol oshdi."),
        ],
        "synonyms": [
            ("-(으)ㄴ/는데도", "-는데도 = og'zaki/neytral; -(으)ㅁ에도 불구하고 = rasmiy yozma"),
            ("-더라도", "-더라도 = faraziy («bo'lsa ham»); 에도 불구하고 = ro'y bergan faktga qaramay"),
        ],
        "order": 608,
    },
    {
        "pattern":   "-고자 / -고자 하다",
        "category":  "connective",
        "function":  "purpose",
        "level":     5,
        "freq":      2,
        "register":  "written",
        "meaning":   "«-moqchi, -ish maqsadida» — rasmiy niyat",
        "attach":    "동사 + -고자 (하다)",
        "form_rule": "-(으)려고 ning <b>rasmiy yozma</b> varianti. Ikki qism egasi bir xil.",
        "note":      "<p>Taqdimot, ariza va ilmiy matnlarda: <i>본 연구에서는 ...을/를 살펴보<b>고자 한다</b>.</i></p>",
        "examples": [
            ("이 글에서는 청년 실업 문제를 살펴보고자 한다.", "Ushbu maqolada yoshlar ishsizligi muammosini ko'rib chiqmoqchimiz."),
            ("고객의 불편을 줄이고자 제도를 개선하였다.", "Mijozlar noqulayligini kamaytirish maqsadida tizim takomillashtirildi."),
        ],
        "synonyms": [
            ("-(으)려고", "-(으)려고 = og'zaki niyat; -고자 = rasmiy yozma"),
            ("-기 위해서", "-기 위해서 = umumiy maqsad; -고자 = so'zlovchining niyati, kitobiy"),
        ],
        "order": 609,
    },
    {
        "pattern":   "-(으)ㄹ 따름이다 / -(으)ㄹ 뿐이다",
        "category":  "expression",
        "function":  "degree",
        "level":     5,
        "freq":      1,
        "register":  "written",
        "meaning":   "«faqat shu, xolos»",
        "attach":    "동사/형용사 + -(으)ㄹ 따름이다 / -(으)ㄹ 뿐이다",
        "form_rule": "<b>따름</b> kuchliroq va rasmiyroq; <b>뿐</b> keng ishlatiladi.",
        "note":      "<p>Boshqa hech qanday imkoniyat/his yo'qligini ta'kidlaydi: "
                     "<i>그저 감사할 <b>따름입니다</b>.</i></p>",
        "examples": [
            ("최선을 다했을 뿐이다.", "Faqat qo'limdan kelganini qildim, xolos."),
            ("도움을 주신 분들께 감사할 따름입니다.", "Yordam berganlarga faqat minnatdorman, xolos."),
        ],
        "synonyms": [
            ("만", "만 = neytral «faqat»; -(으)ㄹ 따름이다 = kitobiy, hissiy ta'kid"),
        ],
        "order": 610,
    },
    {
        "pattern":   "-(으)ㄹ 지경이다",
        "category":  "expression",
        "function":  "degree",
        "level":     5,
        "freq":      1,
        "meaning":   "«shu darajaga yetdi (yomon holat)»",
        "attach":    "동사/형용사 + -(으)ㄹ 지경이다",
        "form_rule": "Deyarli doim <b>salbiy</b> holat bilan.",
        "note":      "<p>Chidab bo'lmas darajaga yetganini bildiradi: <i>배가 고파서 쓰러질 <b>지경이다</b>.</i></p>",
        "examples": [
            ("일이 너무 많아서 죽을 지경이에요.", "Ish shunchalik ko'pki, o'lay deyapman."),
            ("소음 때문에 잠을 못 잘 지경이다.", "Shovqin tufayli uxlay olmaydigan darajaga yetdim."),
        ],
        "synonyms": [
            ("-(으)ㄹ 뻔하다", "-(으)ㄹ 뻔하다 = sodir bo'layozdi (bir lahza); -(으)ㄹ 지경이다 = davomiy og'ir holat"),
        ],
        "order": 611,
    },
    {
        "pattern":   "-(으)ㄹ 바에야 / -느니",
        "category":  "connective",
        "function":  "choice",
        "level":     6,
        "freq":      1,
        "meaning":   "«...-gandan ko'ra, yaxshisi ...»",
        "attach":    "동사 + -(으)ㄹ 바에야 · 동사 + -느니",
        "form_rule": "Ikkinchi qismda ko'pincha <b>차라리</b> keladi.",
        "note":      "<p>Ikkala variant ham yomon, lekin ikkinchisi <b>kamroq yomon</b> degan tanlov.</p>",
        "examples": [
            ("포기할 바에야 끝까지 해 보겠다.", "Voz kechgandan ko'ra oxirigacha urinib ko'raman."),
            ("이렇게 살 바에야 차라리 다시 시작하겠다.", "Shunday yashagandan ko'ra, yaxshisi qaytadan boshlayman."),
        ],
        "synonyms": [
            ("-는 대신에", "-는 대신에 = neytral almashtirish; -(으)ㄹ 바에야 = ikkalasi ham yomon, kamrog'ini tanlash"),
        ],
        "order": 612,
    },
    {
        "pattern":   "-(으)ㄴ/는 만큼",
        "category":  "connective",
        "function":  "reason",
        "level":     5,
        "freq":      2,
        "register":  "written",
        "meaning":   "«-gani darajasida / -gani uchun»",
        "attach":    "동사 + -는 만큼 · 형용사 + -(으)ㄴ 만큼",
        "form_rule": "Ot bilan: 전문가<b>인 만큼</b>",
        "note":      "<p>Ikki ma'no: <b>daraja</b> (노력한 만큼 결과가 나온다) va "
                     "<b>rasmiy sabab</b> (전문가인 만큼 책임도 크다).</p>",
        "examples": [
            ("노력한 만큼 좋은 결과를 얻었다.", "Harakat qilganim darajasida yaxshi natija oldim."),
            ("시간이 부족한 만큼 계획이 중요하다.", "Vaqt yetishmagani uchun reja muhim."),
        ],
        "synonyms": [
            ("만큼", "otga qo'shiladigan varianti (taqqoslash)"),
            ("-기 때문에", "-기 때문에 = sof sabab; -(으)ㄴ 만큼 = «shu darajada bo'lgani uchun»"),
        ],
        "order": 613,
    },
    {
        "pattern":   "-(으)ㄹ 법하다 / -(으)ㅁ직하다",
        "category":  "expression",
        "function":  "guess",
        "level":     6,
        "freq":      1,
        "meaning":   "«-sa ajab emas, bo'lishi mumkin»",
        "attach":    "동사/형용사 + -(으)ㄹ 법하다",
        "form_rule": "Yozma va kitobiy uslub.",
        "note":      "<p>Mantiqan kutilishi mumkin bo'lgan narsa haqida — TOPIK 6 읽기 da uchraydi.</p>",
        "examples": [
            ("그런 결과가 나올 법한 상황이었다.", "Bunday natija chiqishi ajab emas edi."),
            ("충분히 화가 날 법하다.", "Jahli chiqishi tabiiy."),
        ],
        "synonyms": [
            ("-(으)ㄹ 것 같다", "-(으)ㄹ 것 같다 = kundalik taxmin; -(으)ㄹ 법하다 = kitobiy, mantiqiy ehtimol"),
        ],
        "order": 614,
    },
    {
        "pattern":   "-는 한 / -지 않는 한",
        "category":  "connective",
        "function":  "condition",
        "level":     5,
        "freq":      2,
        "register":  "written",
        "meaning":   "«-gan ekan, -masa» — chegara shart",
        "attach":    "동사 + -는 한",
        "form_rule": "Inkor shakli juda ko'p: <b>-지 않는 한</b> («...-masa»).",
        "note":      "<p><b>쓰기 54 uchun kuchli qolip</b>: "
                     "<i>인식이 바뀌<b>지 않는 한</b> 문제는 해결되지 않을 것이다.</i></p>",
        "examples": [
            ("특별한 일이 없는 한 제시간에 도착할 것이다.", "Alohida hodisa bo'lmasa, o'z vaqtida yetib boraman."),
            ("정책이 바뀌지 않는 한 상황은 나아지지 않는다.", "Siyosat o'zgarmas ekan, vaziyat yaxshilanmaydi."),
        ],
        "synonyms": [
            ("-(으)면", "-(으)면 = oddiy shart; -는 한 = «shu holat davom etar ekan» degan chegara"),
            ("-아야", "-아야 = «faqat shu shart bilan»; -지 않는 한 = «bo'lmasa, hech qachon»"),
        ],
        "order": 615,
    },
    {
        "pattern":   "-(으)ㄴ/는 데(에)",
        "category":  "expression",
        "function":  "purpose",
        "level":     4,
        "freq":      3,
        "meaning":   "«-ishda, -ish uchun» — vazifa/soha ko'rsatish",
        "attach":    "동사 + -는 데(에) + 도움이 되다/필요하다/중요하다",
        "form_rule": "⚠️ Bu <b>데</b> — «-는데» (fon) emas. Ajratib yoziladi va ko'pincha "
                     "«도움이 되다, 시간이 걸리다, 필요하다» bilan keladi.",
        "note":      "<p><b>쓰기 54 da eng ko'p ishlatiladigan qoliplardan biri</b>: "
                     "<i>이 방법은 문제를 해결하<b>는 데</b> 큰 도움이 된다.</i></p>",
        "mistake":   "<p>«-는데» (bir so'z, fon) va «-는 데» (ikki so'z, «...-ishda») ni farqlang: "
                     "<i>비가 오<b>는데</b> 우산이 없다</i> (fon) ≠ <i>공부하<b>는 데</b> 시간이 걸린다</i> (vazifa).</p>",
        "examples": [
            ("한국어를 배우는 데 시간이 오래 걸렸다.", "Koreys tilini o'rganishda ko'p vaqt ketdi."),
            ("이 프로그램은 취업하는 데에 도움이 된다.", "Bu dastur ishga joylashishda yordam beradi."),
        ],
        "synonyms": [
            ("-기 위해서", "-기 위해서 = maqsad («uchun»); -는 데 = soha/vazifa («...-ishda»)"),
        ],
        "order": 616,
    },
    {
        "pattern":   "-(으)ㄴ/는 것으로 나타나다/보이다",
        "category":  "expression",
        "function":  "quote",
        "level":     5,
        "freq":      3,
        "register":  "written",
        "meaning":   "«...ligi ma'lum bo'ldi / ko'rinmoqda» — hisobot uslubi",
        "attach":    "동사/형용사 + -(으)ㄴ/는 것으로 나타나다",
        "form_rule": "Shu oilaga: <b>-것으로 조사되다, -것으로 밝혀지다, -것으로 전망되다, "
                     "-것으로 분석되다</b>.",
        "note":      "<p><b>쓰기 53 ning asosiy jumla qolipi.</b> Grafik natijasini bayon qiladi: "
                     "<i>조사 결과 응답자의 60%가 찬성하<b>는 것으로 나타났다</b>.</i></p>",
        "examples": [
            ("1인 가구가 지속적으로 증가하는 것으로 나타났다.", "Yolg'iz yashovchi xonadonlar muttasil ortib borayotgani ma'lum bo'ldi."),
            ("내년에는 상황이 개선될 것으로 전망된다.", "Kelasi yil vaziyat yaxshilanishi kutilmoqda."),
        ],
        "synonyms": [
            ("-다고 하다", "-다고 하다 = og'zaki ko'chirma; -것으로 나타나다 = rasmiy hisobot uslubi"),
            ("-(으)ㅁ에 따르면", "에 따르면 = manbani ko'rsatadi; -것으로 나타나다 = natijani bayon qiladi"),
        ],
        "order": 617,
    },
    {
        "pattern":   "-아/어야말로 · -(이)야말로",
        "category":  "particle",
        "function":  "degree",
        "level":     6,
        "freq":      1,
        "meaning":   "«aynan shu, mana shu» — kuchli ta'kid",
        "attach":    "명사 + (이)야말로",
        "form_rule": "받침 bor → <b>이야말로</b> · 받침 yo'q → <b>야말로</b>",
        "note":      "<p>쓰기 54 xulosasida fikrni kuchaytirish uchun: "
                     "<i>교육<b>이야말로</b> 미래를 바꾸는 힘이다.</i></p>",
        "examples": [
            ("건강이야말로 가장 큰 재산이다.", "Aynan sog'liq — eng katta boylik."),
            ("지금이야말로 행동할 때이다.", "Mana shu payt — harakat qilish vaqti."),
        ],
        "synonyms": [
            ("은/는", "은/는 = oddiy mavzu/ta'kid; (이)야말로 = kuchli, hissiy ta'kid"),
        ],
        "order": 618,
    },
]
