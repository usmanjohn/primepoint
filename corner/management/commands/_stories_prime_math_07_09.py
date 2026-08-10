# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-7 … PM-9.

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr xilma-xilligi: 7 — ilmiy-ommabop (kriptografiya), 8 — bekatdagi sahna
(hikoya; toc da «ilmiy-ommabop» deb belgilangan edi, lekin ketma-ket ikkita
ilmiy-ommabop matn boʻlmasligi uchun sahnaga aylantirildi), 9 — kundalik daftar.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_07_09.py --author=prime
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
    # PM-7 — tub sonlar                       ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Tub sonlar sirni qanday saqlaydi",
        "summary": (
            "PM-7 matni. Ikki tub sonni koʻpaytirish oson, koʻpaytmani qaytib "
            "ajratish esa juda qiyin. Butun internet xavfsizligi shu bir tomonlama "
            "yoʻlga tayanadi."
        ),
        "order":   7,
        "grammar": [
            {
                "pattern":  "Koʻpaytirish oson, ajratish qiyin",
                "meaning":  "Ikkita tub sonni koʻpaytirish bir necha soniyalik ish. "
                            "Teskarisi — katta sonni tub koʻpaytuvchilarga ajratish — "
                            "son kattalashgani sari juda ogʻirlashadi. Shifrlash aynan "
                            "shu farqqa tayanadi.",
                "examples": [
                    "7 × 13 = 91 — bir soniya",
                    "91 = ? × ? — sinab koʻrish kerak: 2, 3, 5, 7…",
                ],
            },
        ],
        "questions": [
            {
                "text": "Matnga koʻra, shifrlash nimaga tayanadi?",
                "choices": [
                    "Kompyuterlarning tez ishlashiga",
                    "Tub sonlar roʻyxatining maxfiyligiga",
                    "Koʻpaytirish oson, ajratish esa qiyin ekaniga",
                    "Juda uzun parollarga",
                ],
                "answer": 2,
                "explanation": "Ikki tub sonni koʻpaytirish oson; koʻpaytmadan oʻsha "
                               "tub sonlarni qaytib topish esa katta sonlarda deyarli "
                               "imkonsiz boʻlib qoladi.",
            },
            {
                "text": "91 sonini tub koʻpaytuvchilarga ajrating.",
                "choices": ["3 × 31", "7 × 13", "9 × 11", "91 tub son"],
                "answer": 1,
                "explanation": "2 ✗, 3 ✗ (9 + 1 = 10), 5 ✗, 7 ✓ — <b>91 = 7 × 13</b>. "
                               "9 × 11 = 99, 3 × 31 = 93 — ikkalasi ham 91 emas.",
            },
            {
                "text": "Nega Sherbek 91 ni avval tub son deb oʻyladi?",
                "choices": [
                    "U 7 ga boʻlib koʻrmagan edi",
                    "U 91 ni juft deb hisobladi",
                    "Unga shunday aytishgan edi",
                    "91 haqiqatan ham tub son",
                ],
                "answer": 0,
                "explanation": "2, 3 va 5 ga tekshirib toʻxtab qolgan. Tekshiruvni "
                               "boʻlinma boʻluvchidan kichik boʻlgunicha davom "
                               "ettirish kerak.",
            },
        ],
        "body": """
<p>Sherbek doskaga 91 deb yozdi.</p>

<p>— Bu <span class="cn-word" data-tr="faqat 1 va oʻziga boʻlinadigan son">tub son</span>,
— dedi u. — Ikkiga boʻlinmaydi, uchga ham, beshga ham.</p>

<p>— Yettiga urinib koʻrdingmi? — soʻradi Afsona.</p>

<p>Sherbek qalamini oldi: 91 ÷ 7 = 13. Demak <strong>91 = 7 × 13</strong> —
<span class="cn-word" data-tr="ikkitadan koʻp boʻluvchisi bor son">murakkab son</span>
ekan.</p>

<p>Ana shu kichik sahna butun internetning asosini koʻrsatadi.</p>

<p>7 va 13 ni koʻpaytirish uchun bir soniya kerak. Teskari yoʻl esa — 91 ni koʻrib turib,
undan 7 va 13 ni topish — sinab koʻrishni talab qiladi. 91 kichkina son, shuning uchun
sinash tez tugadi. Endi ikkita tub son har biri yuzta raqamdan iborat boʻlsa-chi?</p>

<p>Ularni koʻpaytirish kompyuter uchun hamon bir zumlik ish.
<span class="cn-word" data-tr="sonni tub koʻpaytuvchilarga ajratish">Ajratish</span> esa
shunchalik ogʻirki, dunyodagi eng kuchli kompyuterlar ham buni oqilona vaqt ichida
uddalay olmaydi.</p>

<p>Telefoningiz bankka ulanganda aynan shu qoidadan foydalanadi. Katta
<span class="cn-word" data-tr="koʻpaytirish natijasi">koʻpaytma</span> hammaga ochiq —
uni <span class="cn-word" data-tr="hamma koʻra oladigan kalit">ochiq kalit</span> deb
atashadi. Uni hosil qilgan ikkita tub son esa yashirin qoladi va
<span class="cn-word" data-tr="faqat egasida boʻladigan kalit">maxfiy kalit</span>
boʻlib xizmat qiladi. Xabarni ochiq kalit bilan yopish mumkin, ochish uchun esa maxfiy
kalit kerak.</p>

<p>Shu tariqa ikki ming yil oldin faqat qiziqish uchun oʻrganilgan tub sonlar bugun har
kuni milliardlab marta ishlatiladi. Eratosfen buni bilmagan edi. U shunchaki
<span class="cn-word" data-tr="murakkab sonlarni oʻchirib, tublarini qoldirish usuli">gʻalvir</span>
tuzib, sonlarni saralagan edi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-8 — EKUB / EKUK                       BEKATDAGI SAHNA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ikki avtobus qachon bir vaqtda keladi",
        "summary": (
            "PM-8 matni. Bekatda kutib turgan buvijon nabirasidan bitta savol soʻraydi "
            "— va javob EKUK da chiqadi."
        ),
        "order":   8,
        "grammar": [
            {
                "pattern":  "«Qachon uchrashadi?» → EKUK",
                "meaning":  "Takrorlanib turadigan ikki hodisaning yana bir vaqtga "
                            "toʻgʻri kelishi eng kichik umumiy karraliga teng.",
                "examples": [
                    "12 = 2 × 2 × 3 · 18 = 2 × 3 × 3",
                    "EKUK(12, 18) = 2 × 2 × 3 × 3 = 36 daqiqa",
                ],
            },
            {
                "pattern":  "«Eng koʻpi bilan nechta guruh?» → EKUB",
                "meaning":  "Bor narsani teng boʻlishda esa eng katta umumiy boʻluvchi "
                            "kerak boʻladi. Ikkalasini adashtirmang.",
                "examples": ["EKUB(12, 18) = 6"],
            },
        ],
        "questions": [
            {
                "text": "Buvijon nima uchun 8:36 gacha kutishga qaror qildi?",
                "choices": [
                    "Chunki 12-avtobus kech qolgan edi",
                    "Chunki oʻsha paytda ikkala avtobus ham bir vaqtda keladi",
                    "Chunki 18-avtobus tezroq yuradi",
                    "Chunki bekatda oʻrindiq bor edi",
                ],
                "answer": 1,
                "explanation": "Ikkala avtobus ham bir paytda kelsa, qaysi biriga "
                               "chiqishni tanlash mumkin — buvijon shuni kutdi.",
            },
            {
                "text": "Avtobuslar keyingi safar necha daqiqadan keyin birga keladi?",
                "choices": ["24 daqiqa", "30 daqiqa", "36 daqiqa", "216 daqiqa"],
                "answer": 2,
                "explanation": "EKUK(12, 18) = 2 × 2 × 3 × 3 = <b>36</b>. Tekshirish: "
                               "36 ÷ 12 = 3 ✓, 36 ÷ 18 = 2 ✓ 216 — bu koʻpaytma, eng "
                               "kichik umumiy karrali emas.",
            },
            {
                "text": "Matndagi ikkinchi savol — 12 ta gul va 18 ta shirinlikni teng "
                        "paketlarga solish — qanday hisoblanadi?",
                "choices": [
                    "EKUB(12, 18) = 6 ta paket",
                    "EKUK(12, 18) = 36 ta paket",
                    "12 + 18 = 30 ta paket",
                    "12 × 18 = 216 ta paket",
                ],
                "answer": 0,
                "explanation": "Bu safar bor narsani <b>boʻlyapmiz</b>, demak EKUB "
                               "kerak: 6 ta paket, har birida 2 ta gul va 3 ta "
                               "shirinlik.",
            },
        ],
        "body": """
<p>Bekatda buvijon va nabirasi Bekzod turishardi. Ikkalasi ham shaharga ketishi kerak
edi.</p>

<p>Bekatdagi jadvalda ikkita qator bor edi: 12-avtobus har <strong>12 daqiqada</strong>,
18-avtobus har <strong>18 daqiqada</strong> keladi. Soat roppa-rosa 8:00 da ikkalasi
birga kelib ketdi — Bekzod ulgurmay qoldi.</p>

<p>— Xafa boʻlma, — dedi buvijon. — Menga bari bir qaysi biriga chiqish, faqat ikkalasi
birga kelganini koʻrmoqchiman. Qachon shunday boʻladi?</p>

<p>Bekzod daftarini ochdi va har bir avtobusning
<span class="cn-word" data-tr="berilgan songa qoldiqsiz boʻlinadigan son">karrali</span>larini
yozib chiqdi. 12-avtobus 12, 24, 36, 48-daqiqalarda keladi. 18-avtobus 18, 36,
54-daqiqalarda. Ikkala roʻyxatda ham bor birinchi son — <strong>36</strong>.</p>

<p>— Bu <span class="cn-word" data-tr="ikkala sonning ham karralisi boʻlgan eng kichik son">eng kichik umumiy karrali</span>,
— dedi u. — Qisqacha <span class="cn-word" data-tr="eng kichik umumiy karrali">EKUK</span>.
Uni sanab oʻtirmasa ham boʻladi:
<span class="cn-word" data-tr="sonni tub sonlar koʻpaytmasi sifatida yozish">ajratma</span>lardan
topiladi. 12 = 2 × 2 × 3, 18 = 2 × 3 × 3, demak EKUK = 2 × 2 × 3 × 3 = 36.</p>

<p>— Demak 8:36 da, — dedi buvijon. — Unda oʻtiraylik.</p>

<p>Ular oʻrindiqqa oʻtirishdi. Buvijonning sumkasida 12 ta gul va 18 ta shirinlik bor
edi — bularni bugun nabiralariga teng ulashmoqchi edi.</p>

<p>— Buni ham hisoblab ber, — dedi u. — Eng koʻpi bilan nechta bir xil paket chiqadi?</p>

<p>Bekzod bir zum oʻyladi. Bu safar boshqa savol edi: bor narsani <em>boʻlish</em> kerak.
Demak <span class="cn-word" data-tr="ikkala sonni ham boʻladigan eng katta son">EKUB</span>
kerak. U ikkala sonning
<span class="cn-word" data-tr="ikkala sonni ham qoldiqsiz boʻladigan son">umumiy boʻluvchi</span>larini
qaradi: 2 va 3. Ularning koʻpaytmasi — <strong>6</strong>.</p>

<p>— Olti paket, — dedi Bekzod. — Har birida ikkita gul va uchta shirinlik.</p>

<p>Aynan shu payt ikkita avtobus yonma-yon kelib toʻxtadi. Soat 8:36 edi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-9 — manfiy sonlar                     KUNDALIK DAFTAR
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Qish kundaligi",
        "summary": (
            "PM-9 matni. Dilnoza bir hafta davomida haroratni yozib boradi va "
            "manfiy sonlarni taqqoslash haqidagi eng koʻp uchraydigan xatoni tutadi."
        ),
        "order":   9,
        "grammar": [
            {
                "pattern":  "Son oʻqida oʻngdagi son katta",
                "meaning":  "Manfiy sonlarni taqqoslashning yagona ishonchli qoidasi. "
                            "Ikki manfiy sondan nolga yaqinrogʻi katta boʻladi.",
                "examples": [
                    "−8 < −5 < −3 < 0 < +2",
                    "−7 < −2, demak havo isigan",
                ],
            },
        ],
        "questions": [
            {
                "text": "Jasur nima uchun “sovuq kuchaydi” deb xato qildi?",
                "choices": [
                    "U termometrni notoʻgʻri oʻqidi",
                    "U ertalabki haroratni eslay olmadi",
                    "U 7 raqami 2 dan katta boʻlgani uchun −7 ni kattaroq deb oʻyladi",
                    "U haroratni son oʻqida chizdi",
                ],
                "answer": 2,
                "explanation": "Minus belgisi “noldan qancha uzoq” degani emas, “qaysi "
                               "tomonda” degani. −7 son oʻqida −2 dan chapda, demak "
                               "kichikroq.",
            },
            {
                "text": "Kundalikdagi eng sovuq kun qaysi?",
                "choices": ["Dushanba", "Seshanba", "Juma", "Chorshanba"],
                "answer": 1,
                "explanation": "Seshanba −8° — son oʻqida eng chapdagi son. Tartib: "
                               "−8 &lt; −5 &lt; −3 &lt; 0 &lt; +2.",
            },
            {
                "text": "Payshanba (+2°) seshanbadan (−8°) necha daraja issiq?",
                "choices": ["6 daraja", "8 daraja", "12 daraja", "10 daraja"],
                "answer": 3,
                "explanation": "Son oʻqida sanaymiz: −8 dan 0 gacha 8 qadam, 0 dan "
                               "+2 gacha yana 2 qadam — jami <b>10</b> daraja. "
                               "6 — raqamlarni ayirib yuborganda chiqadigan javob.",
            },
        ],
        "body": """
<p><strong>Dushanba.</strong> Bugundan boshlab har kuni ertalabki haroratni yozib
boraman. Termometr <strong>−3°</strong> koʻrsatdi — uch
<span class="cn-word" data-tr="haroratning oʻlchov birligi">daraja</span> sovuq.
Daftarimga son oʻqini chizdim va nolning chap tomonida uch qadam sanadim.</p>

<p><strong>Seshanba.</strong> <strong>−8°</strong>. Maktabga borgunimcha qulogʻim
muzladi. Bu haftaning eng sovuq kuni boʻlsa kerak.</p>

<p><strong>Chorshanba.</strong> Roppa-rosa <strong>0°</strong>. Muz eriy boshladi.
Matematika darsida bilib oldim:
<span class="cn-word" data-tr="musbat ham, manfiy ham boʻlmagan son; sanoq boshlanadigan nuqta">nol</span>
na <span class="cn-word" data-tr="noldan katta son">musbat</span>, na
<span class="cn-word" data-tr="noldan kichik son">manfiy</span> ekan — u shunchaki
chegara.</p>

<p><strong>Payshanba.</strong> <strong>+2°</strong>. Quyosh chiqdi. Bugun birinchi marta
plyus belgili son yozdim.</p>

<p><strong>Juma.</strong> <strong>−5°</strong>. Yana sovudi.</p>

<p>Tanaffusda Jasur bilan bahslashdik. U ertalab −7°, tushda −2° boʻlganini aytib,
«sovuq kuchaydi» dedi.</p>

<p>Men daftarimdagi
<span class="cn-word" data-tr="sonlar tartib bilan joylashgan chiziq">son oʻqi</span>ni
koʻrsatdim. −7 chapda, −2 esa undan oʻngda turibdi. Oʻngdagi son doim katta, demak
harorat <em>koʻtarilgan</em>: havo isigan.</p>

<p>— Lekin yetti ikkidan katta-ku, — dedi Jasur.</p>

<p>— Minus belgisi «qancha uzoq» degani emas, «qaysi tomonda» degani, — dedim men.</p>

<p><strong>Shanba.</strong> Butun haftani
<span class="cn-word" data-tr="kichikdan kattaga qarab joylashtirish">oʻsish tartibi</span>da
yozdim: <strong>−8 &lt; −5 &lt; −3 &lt; 0 &lt; +2</strong>. Eng sovuq kun — seshanba, eng issigʻi
— payshanba. Ular orasidagi farq esa oʻn daraja: noldan pastda sakkiz qadam, noldan
yuqorida ikki qadam.</p>

<p>Kundalikning oxiriga bitta qator yozib qoʻydim: <em>«Ishonmasang — son oʻqini
chiz.»</em></p>
""",
    },
]
