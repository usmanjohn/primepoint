# -*- coding: utf-8 -*-
"""Grammar bank — 접속부사: bog'lovchi ravishlar (sentence connectors).

Order decade 700-799. Unlike the rest of the bank these join *sentences*, not
clauses — they are what makes a 쓰기 54 essay read as structured rather than as
a list. Kept in the grammar bank rather than the vocab bank because the student
looks them up while writing, next to -지만 and -기 때문에.
See STYLE_GUIDE_GRAMMAR.md.
"""

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

POINTS = [
    # ── Qarama-qarshilik ──────────────────────────────────────────────────
    {
        "pattern":   "그러나",
        "category":  "adverb",
        "function":  "contrast",
        "level":     3,
        "freq":      3,
        "register":  "written",
        "meaning":   "«biroq, lekin» — yozma qarama-qarshilik",
        "attach":    "문장 앞 (yangi jumla boshida)",
        "form_rule": "Jumla boshida, keyin vergul qo‘yilmaydi: <b>그러나</b> 결과는 달랐다.",
        "note":      "<p><b>쓰기 54 ning asosiy qarshilik bog‘lovchisi.</b> 하지만 dan rasmiyroq — "
                     "inshoda 그러나, og‘zaki nutqda 하지만.</p>"
                     "<p>Tayyor qolip: <i>물론 [반대 의견]도 일리가 있다. <b>그러나</b> [내 의견]이다.</i></p>",
        "mistake":   "<p>❌ Insho ichida 하지만 va 그러나 ni aralashtirmang — bittasini tanlang "
                     "va oxirigacha shuni ishlating (foydalanuvchi metodi: bitta shablonni mukammal).</p>",
        "examples": [
            ("여러 대책이 시행되었다. 그러나 문제는 해결되지 않았다.",
             "Bir qancha chora ko‘rildi. Biroq muammo hal bo‘lmadi."),
        ],
        "synonyms": [
            ("하지만", "하지만 = og‘zaki va yumshoq; 그러나 = yozma va rasmiy"),
            ("-지만", "-지만 = bitta gap ICHIDA bog‘laydi; 그러나 = yangi jumla boshlaydi"),
        ],
        "order": 700,
    },
    {
        "pattern":   "하지만",
        "category":  "adverb",
        "function":  "contrast",
        "level":     2,
        "freq":      3,
        "meaning":   "«lekin, ammo» — kundalik qarama-qarshilik",
        "attach":    "문장 앞",
        "note":      "<p>그러나 bilan ma’nosi bir xil, uslubi erkinroq. 듣기 dialoglarida ko‘p.</p>",
        "examples": [
            ("한국어는 어렵습니다. 하지만 아주 재미있습니다.",
             "Koreys tili qiyin. Lekin juda qiziqarli."),
        ],
        "synonyms": [
            ("그러나", "그러나 = yozma/rasmiy; 하지만 = og‘zaki va neytral"),
            ("그런데", "그런데 = mavzuni burish yoki fon; 하지만 = aniq qarshilik"),
        ],
        "order": 701,
    },
    {
        "pattern":   "그런데",
        "category":  "adverb",
        "function":  "contrast",
        "level":     2,
        "freq":      3,
        "meaning":   "«lekin; aytgancha» — yumshoq qarshilik yoki mavzu almashtirish",
        "attach":    "문장 앞",
        "note":      "<p>Ikki vazifa: <b>yumshoq qarshilik</b> (비가 왔어요. <b>그런데</b> 우산이 없었어요) "
                     "va <b>mavzuni burish</b> (<b>그런데</b> 요즘 어떻게 지내세요?).</p>"
                     "<p>⚠️ Ikkinchi vazifasi tufayli <b>쓰기 54 da ishlatilmaydi</b> — inshoda "
                     "mavzu burilmasligi kerak.</p>",
        "mistake":   "<p>❌ 쓰기 54: ... <b>그런데</b> 환경 문제도 심각하다. → ✅ <b>또한</b> / <b>그러나</b>. "
                     "그런데 og‘zaki suhbat bog‘lovchisi.</p>",
        "examples": [
            ("어제 시장에 갔어요. 그런데 문을 닫았더라고요.",
             "Kecha bozorga bordim. Lekin yopiq ekan."),
        ],
        "synonyms": [
            ("하지만", "하지만 = sof qarshilik; 그런데 = fon berish yoki mavzu burish"),
            ("-(으)ㄴ/는데", "-는데 = gap ichidagi varianti — bir xil vazifa, bir xil ohang"),
        ],
        "order": 702,
    },
    {
        "pattern":   "반면(에)",
        "category":  "adverb",
        "function":  "contrast",
        "level":     5,
        "freq":      3,
        "register":  "written",
        "meaning":   "«boshqa tomondan, aksincha» — ikki tomonni taqqoslash",
        "attach":    "문장 앞 · 명사 + 인 반면",
        "note":      "<p><b>쓰기 53/54 uchun eng foydali taqqoslash bog‘lovchisi.</b> "
                     "Grafikda ikki guruhni yonma-yon qo‘yganda: "
                     "<i>남성은 40%였다. <b>반면에</b> 여성은 60%로 나타났다.</i></p>",
        "examples": [
            ("도시는 편리하다. 반면에 생활비가 많이 든다.",
             "Shahar qulay. Buning aksincha, turmush xarajati ko‘p."),
        ],
        "synonyms": [
            ("-(으)ㄴ/는 반면에", "gap ICHIDA bog‘laydigan varianti — ma’nosi bir xil"),
            ("오히려", "오히려 = kutilganning teskarisi (hayrat); 반면에 = neytral taqqoslash"),
        ],
        "order": 703,
    },
    {
        "pattern":   "오히려",
        "category":  "adverb",
        "function":  "contrast",
        "level":     4,
        "freq":      3,
        "meaning":   "«aksincha» — kutilganga zid natija",
        "attach":    "문장 앞 또는 문장 중간",
        "note":      "<p><b>읽기 uchun kalit belgi:</b> 오히려 dan keyin <b>kutilganning teskarisi</b> "
                     "keladi, va savolning javobi ko‘pincha aynan o‘sha jumlada bo‘ladi.</p>",
        "examples": [
            ("약을 먹었는데 오히려 더 아팠다.", "Dori ichdim, aksincha battar og‘ridi."),
            ("규제를 강화했지만 오히려 문제가 늘었다.", "Cheklov kuchaytirildi, aksincha muammo ko‘paydi."),
        ],
        "synonyms": [
            ("반면에", "반면에 = ikki narsani xolis taqqoslash; 오히려 = kutilmagan teskari natija"),
        ],
        "order": 704,
    },

    # ── Sabab va natija ───────────────────────────────────────────────────
    {
        "pattern":   "따라서",
        "category":  "adverb",
        "function":  "reason",
        "level":     5,
        "freq":      3,
        "register":  "written",
        "meaning":   "«shunday ekan, binobarin» — mantiqiy xulosa",
        "attach":    "문장 앞",
        "note":      "<p><b>쓰기 54 xulosa paragrafining birinchi so‘zi.</b> Tayyor qolip: "
                     "<i><b>따라서</b> [주체]은/는 [행동]해야 할 것이다.</i></p>",
        "examples": [
            ("자원은 한정되어 있다. 따라서 절약이 필요하다.",
             "Resurslar cheklangan. Shunday ekan, tejash zarur."),
        ],
        "synonyms": [
            ("그러므로", "deyarli bir xil; 그러므로 biroz ko‘proq kitobiy"),
            ("그래서", "그래서 = og‘zaki, oddiy sabab; 따라서 = rasmiy mantiqiy xulosa"),
            ("-(으)므로", "gap ichida bog‘laydigan varianti"),
        ],
        "order": 710,
    },
    {
        "pattern":   "그러므로",
        "category":  "adverb",
        "function":  "reason",
        "level":     5,
        "freq":      2,
        "register":  "written",
        "meaning":   "«shu sababli» — ilmiy/rasmiy xulosa",
        "attach":    "문장 앞",
        "note":      "<p>따라서 dan ham quruqroq: ilmiy maqola, qonun matni, falsafiy dalil.</p>",
        "examples": [
            ("모든 자료가 이를 뒷받침한다. 그러므로 결론은 분명하다.",
             "Barcha ma’lumot buni tasdiqlaydi. Shu sababli xulosa aniq."),
        ],
        "synonyms": [
            ("따라서", "따라서 = keng qo‘llanadigan rasmiy xulosa; 그러므로 = eng kitobiy"),
        ],
        "order": 711,
    },
    {
        "pattern":   "그래서",
        "category":  "adverb",
        "function":  "reason",
        "level":     1,
        "freq":      3,
        "meaning":   "«shuning uchun» — kundalik sabab-natija",
        "attach":    "문장 앞",
        "note":      "<p>Og‘zaki nutqning asosiy sabab bog‘lovchisi. "
                     "⚠️ <b>쓰기 54 da ishlatmang</b> — u yerda 따라서 kerak.</p>",
        "examples": [
            ("어제 늦게 잤어요. 그래서 오늘 피곤해요.",
             "Kecha kech uxladim. Shuning uchun bugun charchaganman."),
        ],
        "synonyms": [
            ("따라서", "따라서 = insho uchun; 그래서 = suhbat uchun"),
            ("-아서/어서", "gap ichida bog‘laydigan varianti"),
        ],
        "order": 712,
    },
    {
        "pattern":   "결국",
        "category":  "adverb",
        "function":  "reason",
        "level":     4,
        "freq":      3,
        "meaning":   "«oxir-oqibat, natijada»",
        "attach":    "문장 앞 또는 문장 중간",
        "note":      "<p>Uzoq jarayonning yakuniy natijasi — ko‘pincha salbiy yoki muqarrar.</p>",
        "examples": [
            ("여러 번 시도했지만 결국 실패했다.", "Bir necha bor urindim, oxir-oqibat muvaffaqiyatsiz bo‘ldi."),
        ],
        "synonyms": [
            ("마침내", "마침내 = ijobiy, kutilgan yakun; 결국 = ko‘pincha salbiy oqibat"),
        ],
        "order": 713,
    },

    # ── Qo'shish va sanash ────────────────────────────────────────────────
    {
        "pattern":   "또한",
        "category":  "adverb",
        "function":  "listing",
        "level":     4,
        "freq":      3,
        "register":  "written",
        "meaning":   "«shuningdek, bundan tashqari»",
        "attach":    "문장 앞",
        "note":      "<p><b>쓰기 54 dagi ikkinchi dalilni boshlashning eng toza usuli.</b> "
                     "게다가 dan neytralroq — insho uchun 또한 ni tanlang.</p>",
        "examples": [
            ("이 방법은 효과적이다. 또한 비용도 적게 든다.",
             "Bu usul samarali. Shuningdek, xarajati ham kam."),
        ],
        "synonyms": [
            ("게다가", "게다가 = «ustiga-ustak» (hissiy kuchaytirish); 또한 = neytral qo‘shish"),
            ("-(으)ㄹ 뿐만 아니라", "gap ICHIDA bog‘laydigan varianti"),
        ],
        "order": 720,
    },
    {
        "pattern":   "게다가",
        "category":  "adverb",
        "function":  "listing",
        "level":     4,
        "freq":      2,
        "meaning":   "«ustiga-ustak, buning ustiga»",
        "attach":    "문장 앞",
        "note":      "<p>Ikkinchi fikr birinchisini <b>kuchaytiradi</b> va ikkalasi bir yo‘nalishda "
                     "bo‘lishi kerak (ikkalasi ijobiy yoki ikkalasi salbiy).</p>",
        "mistake":   "<p>❌ 값이 싸다. <b>게다가</b> 품질이 나쁘다. → yo‘nalish qarama-qarshi. "
                     "✅ 값이 싸다. <b>그러나</b> 품질이 나쁘다.</p>",
        "examples": [
            ("길이 막혔다. 게다가 비까지 내렸다.", "Yo‘l tirband edi. Ustiga-ustak yomg‘ir ham yog‘di."),
        ],
        "synonyms": [
            ("또한", "또한 = neytral va yozma; 게다가 = hissiy, kuchaytiruvchi"),
            ("-(으)ㄴ/는 데다가", "gap ichida bog‘laydigan varianti"),
        ],
        "order": 721,
    },
    {
        "pattern":   "첫째 · 둘째 · 셋째",
        "category":  "adverb",
        "function":  "listing",
        "level":     4,
        "freq":      3,
        "register":  "written",
        "meaning":   "«birinchidan, ikkinchidan…» — dalillarni sanash",
        "attach":    "문장 앞",
        "form_rule": "<b>첫째(로), 둘째(로), 셋째(로)</b> · yakunda <b>마지막으로</b> (nihoyat).",
        "note":      "<p><b>쓰기 54 ning tuzilish skeleti.</b> Ikki-uch dalilni shu bilan raqamlang — "
                     "baholovchi matn tuzilganini darrov ko‘radi.</p>"
                     "<p>Qolip: <i>그 이유는 다음과 같다. <b>첫째</b>, ... <b>둘째</b>, ... "
                     "<b>마지막으로</b>, ...</i></p>",
        "examples": [
            ("이유는 두 가지이다. 첫째, 비용이 많이 든다. 둘째, 시간이 부족하다.",
             "Sabab ikkita. Birinchidan, xarajat ko‘p. Ikkinchidan, vaqt yetishmaydi."),
        ],
        "synonyms": [
            ("우선 · 다음으로", "og‘zakiroq varianti — ma’nosi bir xil"),
        ],
        "order": 722,
    },

    # ── Izohlash va misol ────────────────────────────────────────────────
    {
        "pattern":   "즉",
        "category":  "adverb",
        "function":  "listing",
        "level":     5,
        "freq":      2,
        "register":  "written",
        "meaning":   "«ya’ni, boshqacha aytganda»",
        "attach":    "문장 앞",
        "note":      "<p>Oldingi fikrni <b>boshqa so‘z bilan takrorlaydi</b>, yangi fikr qo‘shmaydi.</p>",
        "examples": [
            ("응답자의 절반이 반대했다. 즉, 두 명 중 한 명은 부정적이었다.",
             "Respondentlarning yarmi qarshi chiqdi. Ya’ni, ikki kishidan biri salbiy qaragan."),
        ],
        "synonyms": [
            ("다시 말해", "다시 말해 = «boshqacha aytganda» — biroz uzunroq va yumshoqroq"),
        ],
        "order": 730,
    },
    {
        "pattern":   "예를 들어",
        "category":  "adverb",
        "function":  "listing",
        "level":     3,
        "freq":      3,
        "meaning":   "«masalan» — misol keltirish",
        "attach":    "문장 앞",
        "form_rule": "Rasmiy varianti: <b>예를 들면</b> · <b>예컨대</b> (eng kitobiy).",
        "note":      "<p><b>쓰기 54 da dalilni misol bilan mustahkamlash</b> — har paragrafda "
                     "bittadan misol matnni ishonarli qiladi.</p>",
        "examples": [
            ("환경을 지키는 방법은 많다. 예를 들어 대중교통을 이용할 수 있다.",
             "Atrof-muhitni asrash yo‘li ko‘p. Masalan, jamoat transportidan foydalanish mumkin."),
        ],
        "synonyms": [
            ("실제로", "실제로 = «amalda, haqiqatda» (dalil); 예를 들어 = aniq misol"),
        ],
        "order": 731,
    },
    {
        "pattern":   "한편",
        "category":  "adverb",
        "function":  "contrast",
        "level":     5,
        "freq":      2,
        "register":  "written",
        "meaning":   "«boshqa tomondan; shu bilan birga»",
        "attach":    "문장 앞",
        "note":      "<p>Mavzuning <b>boshqa qirrasiga</b> o‘tadi — 반면에 kabi qarshi qo‘ymaydi, "
                     "shunchaki yangi tomonni ochadi. Yangiliklar uslubida ko‘p.</p>",
        "examples": [
            ("수출은 늘었다. 한편 수입은 큰 변화가 없었다.",
             "Eksport ortdi. Boshqa tomondan, importda katta o‘zgarish bo‘lmadi."),
        ],
        "synonyms": [
            ("반면에", "반면에 = aniq qarama-qarshilik; 한편 = boshqa qirrani ochish"),
        ],
        "order": 732,
    },
    {
        "pattern":   "그럼에도 불구하고",
        "category":  "adverb",
        "function":  "concession",
        "level":     5,
        "freq":      2,
        "register":  "written",
        "meaning":   "«shunga qaramasdan»",
        "attach":    "문장 앞",
        "note":      "<p>Eng kuchli yozma qarshi qo‘yish bog‘lovchisi. "
                     "쓰기 54 dagi «chora ko‘rildi, lekin natija yo‘q» qismi uchun.</p>",
        "examples": [
            ("여러 대책이 마련되었다. 그럼에도 불구하고 상황은 나아지지 않았다.",
             "Bir qancha chora ko‘rildi. Shunga qaramasdan vaziyat yaxshilanmadi."),
        ],
        "synonyms": [
            ("-(으)ㅁ에도 불구하고", "gap ICHIDA bog‘laydigan varianti"),
            ("그러나", "그러나 = oddiy qarshilik; 그럼에도 불구하고 = kuchli, «hamma narsaga qaramay»"),
        ],
        "order": 733,
    },
]
