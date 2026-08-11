# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-19 … PM-21.

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr xilma-xilligi: 19 — kundalik (mashgʻulot jadvali), 20 — hikoya (bozorda
tarozi), 21 — sayohat qaydlari (Samarqand yoʻli).

⚠️ Kumulyativ: 19-matnda vergulli son yoʻq (oʻnlik kasr PM-20 da);
   foiz PM-22 dan — uchala matnda ham foiz yoʻq.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_19_21.py --author=prime
"""

SUBJECT = {
    "name":    "Matematika",
    "summary": "Matematika: hayotdagi matnlar, atamalar va matematik hikoyalar.",
    "icon":    "bi-calculator",
    "color":   "#f59e0b",
    "order":   7,
}

COLLECTION = {
    "title":       "Prime Math Readings",
    "description": (
        "Prime Math darslarining oʻqish matnlari — har biri oʻz darsining "
        "matematikasini hayotdagi matn ichida koʻrsatadi. Atamalar izohi bilan."
    ),
    "order": 1,
}

STORIES = [
    # ══════════════════════════════════════════════════════════════════
    # PM-19 — aralash sonlar                             KUNDALIK
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ikki yarim soat",
        "summary": (
            "PM-19 matni. Afsonaning mashgʻulot kundaligi: soat va daqiqalar aralash "
            "songa aylanadi, haftalik jami esa notoʻgʻri kasr bilan hisoblanadi."
        ),
        "order":   19,
        "grammar": [
            {
                "pattern":  "Aralash son ↔ notoʻgʻri kasr",
                "meaning":  "Aralash sonni notoʻgʻri kasrga aylantirish uchun "
                            "butunni maxrajga koʻpaytirib, suratga qoʻshamiz. "
                            "Teskarisi uchun suratni maxrajga boʻlamiz: boʻlinma — "
                            "butun, qoldiq — yangi surat.",
                "examples": [
                    "2 1/4 = (2 × 4 + 1)/4 = 9/4",
                    "22/4 = 5 (qoldiq 2) → 5 2/4 = 5 1/2",
                ],
            },
        ],
        "questions": [
            {
                "text": "Afsona kundaligiga nima uchun kasr yozdi?",
                "choices": [
                    "Soatlar butun son bilan yozilmagani uchun",
                    "Murabbiy shunday talab qilgani uchun",
                    "Daftarida joy kam boʻlgani uchun",
                    "Daqiqalarni sanashni bilmagani uchun",
                ],
                "answer": 0,
                "explanation": "Mashgʻulot 2 soat 30 daqiqa davom etdi — bu butun "
                               "son emas, shuning uchun aralash son kerak boʻldi.",
            },
            {
                "text": "2 1/4 soat notoʻgʻri kasr koʻrinishida qanday yoziladi?",
                "choices": ["4/9 soat", "7/4 soat", "9/4 soat", "21/4 soat"],
                "answer": 2,
                "explanation": "2 × 4 + 1 = 9, maxraj oʻzgarmaydi: 9/4 soat.",
            },
            {
                "text": "Uch mashgʻulot: 1 1/2 · 2 1/4 · 1 3/4 soat. Haftada jami "
                        "necha soat?",
                "choices": ["4 1/2 soat", "5 soat", "5 1/2 soat", "6 soat"],
                "answer": 2,
                "explanation": "Toʻrtdan boʻlakka keltiramiz: 6/4 + 9/4 + 7/4 = "
                               "22/4. 22 ÷ 4 = 5 (qoldiq 2), demak 5 2/4 = "
                               "5 1/2 soat.",
            },
        ],
        "body": """
<p><b>Yakshanba, kech.</b></p>

<p>Bugun haftalik jadvalni hisobladim. Murabbiy har oyning oxirida «necha soat
mashgʻulot qilding?» deb soʻraydi, men esa har safar shoshib qolardim. Endi
daftarga yozib boraman.</p>

<p><b>Dushanba:</b> 1 soat 30 daqiqa. <b>Chorshanba:</b> 2 soat 15 daqiqa.
<b>Juma:</b> 1 soat 45 daqiqa.</p>

<p>Birinchi qiyinchilik shu yerda boshlandi. Daqiqalarni soatga aylantirish kerak edi.
30 daqiqa — soatning yarmi, yaʼni 1/2. 15 daqiqa — choragi, 1/4. 45 daqiqa esa uchta
chorak, 3/4.</p>

<p>Demak: <strong>1 1/2</strong>, <strong>2 1/4</strong> va <strong>1 3/4</strong>
soat. Butun son va kasr birga yozilgan bunday sonni
<span class="cn-word" data-tr="butun son va kasr birga yozilgan son">aralash son</span>
deyilarkan.</p>

<p>Qoʻshishga urinib koʻrdim va yana toʻxtadim: maxrajlar har xil. Onam maslahat berdi
— hammasini bir xil koʻrinishga keltir.</p>

<p>Men uchalasini ham <span class="cn-word" data-tr="surati maxrajidan katta yoki unga teng kasr">notoʻgʻri kasr</span>ga
aylantirdim. Buning uchun <span class="cn-word" data-tr="aralash sondagi butun son">butun qism</span>ni
maxrajga koʻpaytirib, <span class="cn-word" data-tr="kasrning yuqorigi soni">surat</span>ga
qoʻshish kerak ekan: 1 1/2 = 3/2 = 6/4, keyin 2 1/4 = 9/4, va 1 3/4 = 7/4.</p>

<p>Endi hammasi toʻrtdan boʻlak: <strong>6/4 + 9/4 + 7/4 = 22/4</strong>.</p>

<p>Oxirgi qadam eng yoqimlisi boʻldi. 22 ni 4 ga boʻldim: 5 chiqdi,
<span class="cn-word" data-tr="boʻlishdan ortib qolgan son">qoldiq</span> 2. Demak
<strong>5 2/4</strong>, <span class="cn-word" data-tr="surat va maxrajni umumiy boʻluvchiga boʻlish">qisqartirsam</span>
— <strong>5 1/2 soat</strong>.</p>

<p>Besh yarim soat. Koʻp emas ekan. Kelasi haftaga yana bir mashgʻulot qoʻshaman.</p>

<p>Bugun bir narsani tushundim: hisoblash uchun <b>notoʻgʻri kasr</b> qulay,
aytish uchun esa <b>aralash son</b>. «Yigirma ikki toʻrtdan bir soat mashq qildim»
degan gap gʻalati eshitiladi, «besh yarim soat» esa tabiiy.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-20 — oʻnlik kasrlar                             HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Tarozidagi raqamlar",
        "summary": (
            "PM-20 matni. Bozor tarozisidagi vergul nimani anglatadi — va nega "
            "0,9 kilogramm 0,45 kilogrammdan ogʻirroq."
        ),
        "order":   20,
        "grammar": [
            {
                "pattern":  "Oxirgi nol sonni oʻzgartirmaydi",
                "meaning":  "Vergul ortiga qoʻshilgan oxirgi nol sonning qiymatini "
                            "oʻzgartirmaydi, chunki u faqat kasrni kattaroq maxrajga "
                            "keltiradi. Taqqoslashdan oldin aynan shu yoʻl bilan "
                            "razryadlarni tenglashtiriladi.",
                "examples": [
                    "1,25 = 1,250 (25/100 = 250/1000)",
                    "0,9 = 0,90, demak 0,9 > 0,45",
                ],
            },
        ],
        "questions": [
            {
                "text": "Sherbek nega tarozidagi yozuvni tushunmadi?",
                "choices": [
                    "Ekran ishlamay qolgan edi",
                    "Vergul nimani ajratishini bilmasdi",
                    "Sotuvchi narxni aytmadi",
                    "Tarozi grammda koʻrsatardi",
                ],
                "answer": 1,
                "explanation": "1,250 yozuvidagi vergul butun kilogrammni undan "
                               "kichik qismdan ajratib turadi — Sherbek shuni "
                               "bilmasdi.",
            },
            {
                "text": "1,250 kg va 1,25 kg — bu ikkisi qanday?",
                "choices": [
                    "Birinchisi ogʻirroq",
                    "Ikkinchisi ogʻirroq",
                    "Ikkalasi bir xil",
                    "Taqqoslab boʻlmaydi",
                ],
                "answer": 2,
                "explanation": "Oxirgi nol hech narsa qoʻshmaydi: 250/1000 = 25/100. "
                               "Ikkalasi ham 1 kilo 250 gramm.",
            },
            {
                "text": "Bir paketda 0,9 kg, ikkinchisida 0,45 kg guruch bor. Qaysi "
                        "biri ogʻirroq va necha grammga?",
                "choices": [
                    "0,45 kg — 360 grammga",
                    "0,9 kg — 45 grammga",
                    "0,9 kg — 450 grammga",
                    "Ikkalasi teng",
                ],
                "answer": 2,
                "explanation": "0,9 = 0,90, demak 900 gramm va 450 gramm. "
                               "900 − 450 = 450 gramm farq.",
            },
        ],
        "body": """
<p>Sherbek buvijoni bilan bozorga bordi. Sotuvchi goʻshtni tarozi ustiga qoʻydi va
ekranda raqamlar chiqdi: <strong>1,250</strong>.</p>

<p>— Bu qancha boʻldi? — soʻradi Sherbek.</p>

<p>— Bir kilo ikki yuz ellik gramm, — dedi sotuvchi.</p>

<p>Sherbek hayron boʻldi. Ekranda «gramm» degan soʻz yoʻq edi, faqat raqamlar va bitta
kichkina belgi — <span class="cn-word" data-tr="butun qismni kasr qismdan ajratuvchi belgi">vergul</span>.</p>

<p>Buvijoni tushuntirdi. Verguldan chapdagi 1 — butun kilogramm. Oʻngdagi raqamlar esa
kilogrammning boʻlaklari: birinchi oʻrin —
<span class="cn-word" data-tr="verguldan keyingi birinchi razryad, 0,1">oʻndan bir</span>,
ikkinchisi — <span class="cn-word" data-tr="verguldan keyingi ikkinchi razryad, 0,01">yuzdan bir</span>,
uchinchisi — <span class="cn-word" data-tr="verguldan keyingi uchinchi razryad, 0,001">mingdan bir</span>.
Kilogrammning mingdan bir qismi esa aynan bir gramm.</p>

<p>Keyingi doʻkonda yana bir tarozi bor edi. Unda <strong>1,25</strong> yozilgandi.</p>

<p>— Bu kamroq ekan-da? — dedi Sherbek.</p>

<p>— Yoʻq, — kuldi buvijoni. — Bu ham xuddi shu. Oxirgi nol hech narsa qoʻshmaydi.</p>

<p>Ular uyga kelib, Sherbek daftariga yozdi: 1,25 = 1,250, chunki 25/100 va 250/1000 —
bir xil <span class="cn-word" data-tr="butunning teng boʻlaklari bilan yoziladigan son">kasr</span>ning
ikki yozuvi.</p>

<p>Kechqurun uni yana bir savol qiynadi. Bir paketda <b>0,9 kg</b> guruch,
ikkinchisida <b>0,45 kg</b>. Qaysi biri ogʻir? «Toʻqson besh — toʻqqizdan katta»,
deb oʻyladi u avvaliga.</p>

<p>Keyin buvijonining usulini esladi: <span class="cn-word" data-tr="raqamning sondagi oʻrni">razryad</span>larni
tenglashtirish kerak. <strong>0,9 = 0,90</strong>. Endi hammasi ravshan: 90 va 45.
Grammga oʻtkazsa ham shu chiqadi — 900 gramm va 450 gramm.</p>

<p>Oʻnlik kasrda uzunroq son katta degani emas ekan. Buni Sherbek shu kuni,
tarozi oldida turib oʻrgandi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-21 — oʻnlik amallar                             SAYOHAT QAYDLARI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Benzin va yoʻl",
        "summary": (
            "PM-21 matni. Samarqandga yoʻlga chiqishdan oldin otasi bilan hisob "
            "qildilar: uch amal, bitta vergul va yoʻlning haqiqiy narxi."
        ),
        "order":   21,
        "grammar": [
            {
                "pattern":  "Oʻnlik kasrni koʻpaytirish — xonalarni sanash",
                "meaning":  "Vergulni unutib, sonlarni butun son kabi koʻpaytiramiz. "
                            "Soʻng ikkala koʻpaytuvchidagi vergul ortidagi "
                            "raqamlarni jami sanab, javobda oʻng chetdan shuncha "
                            "raqam sanaymiz va vergulni qoʻyamiz.",
                "examples": [
                    "3 × 9,5 = 28,5 litr (95 × 3 = 285, bitta xona)",
                    "28,5 × 8 400 = 239 400 soʻm",
                ],
            },
        ],
        "questions": [
            {
                "text": "Otasi yoʻlga chiqishdan oldin nima uchun hisob qildi?",
                "choices": [
                    "Mashinani tekshirish uchun",
                    "Yoʻl uzunligini oʻlchash uchun",
                    "Yoʻlga qancha pul kerakligini oldindan bilish uchun",
                    "Tezlikni hisoblash uchun",
                ],
                "answer": 2,
                "explanation": "Hamyondagi pul yetadimi yoki yoʻqmi — buni yoʻlda "
                               "emas, uyda bilib olish kerak.",
            },
            {
                "text": "300 km yoʻlga necha litr benzin ketadi?",
                "choices": ["9,5 litr", "19 litr", "28,5 litr", "95 litr"],
                "answer": 2,
                "explanation": "300 ÷ 100 = 3 ta yuz kilometr, har biriga 9,5 litr: "
                               "3 × 9,5 = 28,5 litr.",
            },
            {
                "text": "Benzinning litri 8 400 soʻm boʻlsa, yoʻlga qancha pul ketadi?",
                "choices": [
                    "79 800 soʻm",
                    "239 400 soʻm",
                    "285 000 soʻm",
                    "478 800 soʻm",
                ],
                "answer": 1,
                "explanation": "28,5 × 8 400 = 239 400 soʻm. Tekshiruv: "
                               "28 × 8 400 = 235 200 va 0,5 × 8 400 = 4 200, "
                               "jami 239 400.",
            },
        ],
        "body": """
<p><b>Payshanba, ertalab.</b> Ertaga Samarqandga chiqamiz. Otam kechqurun daftarni
olib, yonimga oʻtirdi.</p>

<p>— Yoʻlga chiqishdan oldin bir narsani bilib olish kerak, — dedi u. — Qancha pul
ketadi?</p>

<p>Uch xil son bor edi. Yoʻl — <b>300 km</b>. Mashinaning
<span class="cn-word" data-tr="mashina yoʻlda ishlatadigan yoqilgʻi miqdori">sarfi</span>
— har 100 kilometrda <b>9,5 litr</b>. Benzinning litri — <b>8 400 soʻm</b>.</p>

<p>Birinchi qadam oson boʻldi: 300 ÷ 100 = 3. Yaʼni yoʻl uchta «yuz kilometr»dan
iborat — bu <span class="cn-word" data-tr="boʻlish natijasi">boʻlinma</span>.</p>

<p>Ikkinchi qadamda birinchi marta <span class="cn-word" data-tr="vergul bilan yoziladigan kasr">oʻnlik kasr</span>
bilan ishladim. 3 × 9,5. Otam aytdi: vergulni unut, 95 ni 3 ga koʻpaytir — 285 chiqadi.
Keyin <span class="cn-word" data-tr="verguldan keyingi raqam oʻrni">oʻnlik xona</span>larni
sana: 9,5 da bitta xona bor, demak javobda ham bitta. <strong>28,5 litr</strong>.</p>

<p>— Mantiqan ham toʻgʻri, — dedi u. — Har yuz kilometrga oʻn litrga yaqin, uch
yuzga esa oʻttizga yaqin.</p>

<p>Uchinchi qadam eng kattasi edi: <strong>28,5 × 8 400</strong>. Bu safar
<span class="cn-word" data-tr="hisoblashdan oldin javobning kattaligini baholash">taxmin</span>
qilib koʻrdim — 30 litr, litri 8 mingdan — demak 240 ming atrofida.</p>

<p>Aniq hisob esa shunday chiqdi: 28 × 8 400 = 235 200, va 0,5 × 8 400 = 4 200.
Ikkalasini qoʻshdim: <strong>239 400 soʻm</strong>. Taxminimga juda yaqin —
demak <span class="cn-word" data-tr="raqamning sondagi oʻrni">razryad</span>da xato
yoʻq.</p>

<p>— Endi bitta savol, — dedi otam kulib. — Bu faqat borish. Qaytish-chi?</p>

<p>Men bir zumda tushundim: yoʻl 600 kilometr boʻladi, benzin 57 litr, pul esa
<strong>478 800 soʻm</strong>. Masalada nima soʻralganini ikki marta oʻqish kerak
ekan.</p>

<p>Otam hamyoniga qaradi va: «Yetadi», dedi. Ertaga yoʻlga chiqamiz.</p>
""",
    },
]
