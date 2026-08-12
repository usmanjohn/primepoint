# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-66, PM-67, PM-68 (Blok E: Geometriya).

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr: 66 — sharh, 67 — hikoya, 68 — kundalik.
⚠️ Tocda 68-matn «hikoya» deb rejalashtirilgan edi, lekin 67 ham hikoya —
   ketma-ket ikkitasi bir xil shakl boʻlib qolardi. Mavzu (sinf polini
   qoplash) saqlandi, shakli kundalikka oʻzgartirildi; tocdagi janr
   yorligʻi ham yangilandi.

⚠️ Kumulyativ — bu uchligida tartib qatʼiy:
   • 66-matnda PERIMETR ham, YUZA ham YOʻQ (ular PM-67 va PM-68) —
     faqat shakl va burchak;
   • 67-matnda faqat PERIMETR;
   • 68-matnda yuza, va u aynan perimetrdan farqlanadi.
⚠️ `grammar.pattern` va `examples` ekranlanadi — <sup> emas, Unicode ²
   yoziladi.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_66_68.py --author=prime
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
    # PM-66 — toʻrtburchaklar oilasi                              SHARH
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Gilam naqshidagi shakllar",
        "summary": (
            "PM-66 matni. Sharh: Afsona buvisining gilamiga geometriya "
            "koʻzi bilan qaraydi va naqshdagi har bir shaklga toʻgʻri nom "
            "topadi — romb, trapetsiya, kvadrat."
        ),
        "order":   66,
        "grammar": [
            {
                "pattern":  "parallelogrammda qoʻshni burchaklar 180°, qarama-qarshilari teng",
                "meaning":  "Romb ham parallelogramm, shuning uchun unga "
                            "ham shu qoida ishlaydi: bitta burchak "
                            "bilinsa, qolgan uchtasi hisoblab topiladi.",
                "examples": [
                    "romb: 180 − 110 = 70°, burchaklari 110°, 70°, 110°, 70°",
                    "tekshiruv: 110 + 70 + 110 + 70 = 360",
                    "kichik kvadratchalar: toʻrtala burchagi ham 90°",
                ],
            },
        ],
        "questions": [
            {
                "text": "Afsona nega naqshdagi shakllarni «romb» deb "
                        "atadi, «kvadrat» deb emas?",
                "choices": [
                    "Ular kvadratdan kattaroq boʻlgani uchun",
                    "Tomonlari teng, lekin burchaklari 90° emasligi uchun",
                    "Ular rangli boʻlgani uchun",
                    "Buvisi shunday oʻrgatgani uchun",
                ],
                "answer": 1,
                "explanation": "Rombning toʻrtala tomoni teng, lekin "
                               "burchaklari 90° boʻlishi shart emas. "
                               "Naqshdagi shakllar qiya turgani uchun "
                               "ular romb — kvadrat esa rombning "
                               "burchaklari 90° boʻlgan maxsus holati.",
            },
            {
                "text": "Rombning katta burchagi 110° boʻlsa, kichigi necha "
                        "gradus?",
                "choices": ["55°", "70°", "90°", "250°"],
                "answer": 1,
                "explanation": "Romb — parallelogramm, demak qoʻshni "
                               "burchaklar 180° ni beradi: 180 − 110 = 70°. "
                               "«55°» — 110 ning yarmi, uning bu yerda "
                               "hech qanday asosi yoʻq.",
            },
            {
                "text": "Chetdagi naqsh nega trapetsiya deb ataldi?",
                "choices": [
                    "Faqat bitta juft tomoni parallel boʻlgani uchun",
                    "Ikkala juft tomoni ham parallel boʻlgani uchun",
                    "Toʻrtala tomoni teng boʻlgani uchun",
                    "Burchaklari 90° boʻlgani uchun",
                ],
                "answer": 0,
                "explanation": "Trapetsiyada faqat bitta juft tomon "
                               "parallel boʻladi — aynan shu bilan u "
                               "parallelogrammdan farq qiladi. Gilam "
                               "chetidagi naqshning yuqori va quyi "
                               "tomonlari parallel, yon tomonlari esa "
                               "yigʻilib boradi.",
            },
        ],
        "body": """
<p>Afsona buvisining xonasida gilam bor. U kichkinaligidan shu gilamga
qarab oʻsgan, lekin bugun unga birinchi marta boshqacha koʻz bilan
qaradi.</p>

<p>Gilamning oʻrtasida katta naqsh takrorlanadi. Har bir naqshning toʻrtta
<span class="cn-word" data-tr="koʻpburchakni hosil qiluvchi kesma">tomon</span>i
bor va hammasi bir xil uzunlikda. Lekin ular qiya turadi — burchaklari
<strong>90</strong>° emas.</p>

<p>«Bu kvadrat emas», — dedi Afsona ovoz chiqarib. «Bu
<span class="cn-word" data-tr="toʻrtala tomoni teng boʻlgan parallelogramm">romb</span>.»</p>

<p>U <span class="cn-word" data-tr="burchak oʻlchaydigan yarim doira shaklidagi asbob">transportir</span>
bilan oʻlchadi. Katta
<span class="cn-word" data-tr="umumiy boshlangʻich nuqtali ikki nur hosil qilgan shakl">burchak</span>
<strong>110</strong>
<span class="cn-word" data-tr="burchak oʻlchov birligi">gradus</span>
chiqdi. Kichigini oʻlchashning hojati qolmadi:
romb ham
<span class="cn-word" data-tr="qarama-qarshi tomonlari juft-juft parallel toʻrtburchak">parallelogramm</span>,
demak
<span class="cn-word" data-tr="bitta tomonni baham koʻrgan burchaklar">qoʻshni burchaklar</span>
180° ni beradi: 180 − 110 = <strong>70</strong>°.</p>

<p>Tekshirib ham koʻrdi: 110 + 70 + 110 + 70 = <strong>360</strong>° —
har qanday
<span class="cn-word" data-tr="toʻrt tomonli shakl">toʻrtburchak</span>da
shuncha boʻlishi kerak. Demak
<span class="cn-word" data-tr="roʻparama-roʻpara turgan, teng burchaklar">qarama-qarshi burchaklar</span>
juft-juft teng ekan.</p>

<p>Naqshlarning orasida kichkina shakllar bor edi. Ularning tomonlari ham
teng, burchaklari esa 90°. Bular
<span class="cn-word" data-tr="ham romb, ham toʻgʻri toʻrtburchak boʻlgan shakl">kvadrat</span>lar.</p>

<p>«Demak kvadrat ham romb ekan-da», — oʻyladi Afsona. Toʻgʻri: kvadratning
toʻrtala tomoni teng, demak u rombning shartini bajaradi. Teskarisi esa
notoʻgʻri — oʻrtadagi qiya naqshlar hech qachon kvadrat boʻlolmaydi.</p>

<p>Gilamning chetidagi hoshiyada boshqacha shakl chiqdi. Uning yuqori va
quyi tomonlari
<span class="cn-word" data-tr="hech qachon kesishmaydigan chiziqlar">parallel</span>
edi — ular trapetsiyaning
<span class="cn-word" data-tr="trapetsiyaning parallel tomonlaridan biri">asos</span>lari.
Yon tomonlari esa bir-biriga qarab yigʻilib borardi. Bu —
<span class="cn-word" data-tr="faqat bitta juft tomoni parallel toʻrtburchak">trapetsiya</span>.
Ikkala juft ham parallel boʻlmagani uchun u parallelogramm emas.</p>

<p>Kechqurun Afsona buvisiga oʻzi topgan nomlarni sanab berdi. Buvisi
kuldi: «Men bu gilamni qirq yildan beri koʻraman. Sen esa bir kunda uning
tilini oʻrganib olibsan.»</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-67 — perimetr                                           HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Bogʻga panjara",
        "summary": (
            "PM-67 matni. Hikoya: Sherbek bogʻga panjara olishga boradi va "
            "ikkita tomonni qoʻshib qoʻya qoladi. Doʻkonchi xatoni "
            "topib beradi."
        ),
        "order":   67,
        "grammar": [
            {
                "pattern":  "P = 2 × (a + b)",
                "meaning":  "Toʻgʻri toʻrtburchakning perimetri — hamma "
                            "tomonining yigʻindisi. Qarama-qarshi tomonlar "
                            "teng boʻlgani uchun har bir son ikki marta "
                            "qoʻshiladi.",
                "examples": [
                    "2 × (18 + 10) = 2 × 28 = 56 m",
                    "darvoza chiqarildi: 56 − 4 = 52 m",
                    "narxi: 52 × 25 000 = 1 300 000 soʻm",
                ],
            },
        ],
        "questions": [
            {
                "text": "Sherbek birinchi marta qanday xato qildi?",
                "choices": [
                    "Bogʻning tomonlarini notoʻgʻri oʻlchadi",
                    "Faqat ikkita tomonni qoʻshdi va ikkilantirishni "
                    "unutdi",
                    "Tomonlarni bir-biriga koʻpaytirdi",
                    "Darvozani hisobga olmadi",
                ],
                "answer": 1,
                "explanation": "U 18 + 10 = 28 deb toʻxtab qoldi. Bu faqat "
                               "ikkita tomon. Bogʻning atrofi toʻrtta "
                               "tomondan iborat, shuning uchun javob "
                               "2 × 28 = 56 metr.",
            },
            {
                "text": "Darvozani hisobga olgandan keyin necha metr panjara "
                        "kerak boʻldi?",
                "choices": ["24 m", "28 m", "52 m", "56 m"],
                "answer": 2,
                "explanation": "Butun chegara 56 metr, darvoza esa 4 metr — "
                               "u yerga panjara qoʻyilmaydi: "
                               "56 − 4 = 52 metr. «56 m» — darvoza "
                               "ayirilmagan javob.",
            },
            {
                "text": "Panjara jami necha soʻm turdi?",
                "choices": [
                    "700 000 soʻm",
                    "1 300 000 soʻm",
                    "1 400 000 soʻm",
                    "1 800 000 soʻm",
                ],
                "answer": 1,
                "explanation": "52 metr panjara, har bir metri 25 000 soʻm: "
                               "52 × 25 000 = 1 300 000 soʻm. "
                               "«1 400 000» — darvoza ayirilmagan holat "
                               "(56 × 25 000).",
            },
        ],
        "body": """
<p>Sherbekning otasi bogʻni panjara bilan oʻramoqchi boʻldi. Oʻlchashni
Sherbekka topshirdi.</p>

<p>Bogʻ
<span class="cn-word" data-tr="burchaklari 90° boʻlgan parallelogramm">toʻgʻri toʻrtburchak</span>
shaklida. Sherbek
<span class="cn-word" data-tr="uzunlik oʻlchaydigan lentali asbob">ruletka</span>
bilan oʻlchadi:
<span class="cn-word" data-tr="toʻgʻri toʻrtburchakning katta oʻlchovi">uzunlik</span>i
<strong>18</strong>
<span class="cn-word" data-tr="uzunlik birligi, 100 santimetr">metr</span>,
<span class="cn-word" data-tr="toʻgʻri toʻrtburchakning kichik oʻlchovi">en</span>i
<strong>10</strong> metr.</p>

<p>U daftariga yozdi: 18 + 10 = <strong>28</strong>. Soʻng doʻkonga bordi.</p>

<p>«Yigirma sakkiz metr panjara bering», — dedi u.</p>

<p>Doʻkonchi Nodira opa qalam oldi. «Bogʻing toʻgʻri toʻrtburchakmi?
Unda menga uning
<span class="cn-word" data-tr="shaklni oʻrab turgan chiziqning uzunligi">perimetr</span>i
kerak. Sen esa faqat ikkita
<span class="cn-word" data-tr="koʻpburchakni hosil qiluvchi kesma">tomon</span>ni
qoʻshibsan.»</p>

<p>U qogʻozga toʻrtburchak chizdi va har bir tomonni koʻrsatdi.
<span class="cn-word" data-tr="roʻparama-roʻpara turgan, teng tomonlar">Qarama-qarshi tomonlar</span>
teng, demak <strong>18</strong> ham, <strong>10</strong> ham ikki martadan
uchraydi.</p>

<p>«Chegara boʻylab bir marta aylanib chiq», — dedi u. Yigʻindini
<span class="cn-word" data-tr="ikki barobar qilish, 2 ga koʻpaytirish">ikkilantirish</span>
kerak edi: 2 × (18 + 10) = 2 × 28 = <strong>56</strong> metr.</p>

<p>Sherbek qizarib ketdi. Yigirma sakkiz metr panjara olganida bogʻning
yarmi ochiq qolar edi.</p>

<p>«Yana bir narsa», — dedi Nodira opa. «Darvoza qoʻyasizlarmi?»</p>

<p>Sherbek otasiga qoʻngʻiroq qildi: darvoza <strong>4</strong> metr
boʻlarkan. U yerga panjara kerak emas.</p>

<p>56 − 4 = <strong>52</strong> metr.</p>

<p>Panjaraning bir metri <strong>25 000</strong> soʻm edi. Uzunlikni narxga
<span class="cn-word" data-tr="bir sonni ikkinchisiga marta-marta qoʻshish amali">koʻpaytirish</span>
qoldi: 52 × 25 000 = <strong>1 300 000</strong> soʻm.</p>

<p>Uyga qaytgach, Sherbek daftariga bir jumla yozib qoʻydi: «Perimetr —
bu <span class="cn-word" data-tr="shaklning tashqi konturi">chegara</span>,
ikkita tomon emas.»</p>

<p>Ertasi kuni panjara keltirildi. Uzunligi aniq yetdi — bir metr ham
ortiqcha emas, bir metr ham kam emas.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-68 — yuza                                            KUNDALIK
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Sinf polini qoplash",
        "summary": (
            "PM-68 matni. Kundalik: Jasur sinfdagi taʼmir ishlarini uch kun "
            "davomida yozib boradi — yuzani hisoblash, shkaf tagini "
            "chiqarib tashlash va zaxira plitka."
        ),
        "order":   68,
        "grammar": [
            {
                "pattern":  "S = a × b; plitkalar soni = yuza ÷ bitta plitkaning yuzasi",
                "meaning":  "Yuza — shakl ichiga sigʻadigan birlik "
                            "kvadratlar soni. Qoplash masalasida ikkala "
                            "yuza ham bir xil birlikda boʻlishi shart.",
                "examples": [
                    "sinf: 7 × 6 = 42 m²",
                    "shkaf tagi: 2 × 1,5 = 3 m², qoladi 42 − 3 = 39 m²",
                    "plitka: 0,5 × 0,5 = 0,25 m², kerak 39 ÷ 0,25 = 156 ta",
                ],
            },
        ],
        "questions": [
            {
                "text": "Jasur nega 42 m² ni emas, 39 m² ni hisobga oldi?",
                "choices": [
                    "Bir qismini keyingi yilga qoldirishdi",
                    "Shkaf turadigan 3 m² ga plitka yotqizilmaydi",
                    "Xonaning bir burchagi notekis edi",
                    "Plitka yetishmay qoldi",
                ],
                "answer": 1,
                "explanation": "Burchakdagi shkaf 2 m × 1,5 m joyni "
                               "egallaydi, yaʼni 3 m². Uning tagiga plitka "
                               "qoʻyilmaydi, shuning uchun "
                               "42 − 3 = 39 m² qoplanadi.",
            },
            {
                "text": "Bitta plitkaning yuzasi qancha?",
                "choices": ["0,1 m²", "0,25 m²", "0,5 m²", "2,5 m²"],
                "answer": 1,
                "explanation": "Plitkaning tomoni 50 sm = 0,5 m, demak "
                               "yuzasi 0,5 × 0,5 = 0,25 m². «0,5 m²» — "
                               "tomonning oʻzi, yuzasi emas.",
            },
            {
                "text": "Usta zaxira bilan birga nechta plitka buyurtma "
                        "qildi?",
                "choices": ["156 ta", "160 ta", "168 ta", "180 ta"],
                "answer": 2,
                "explanation": "39 ÷ 0,25 = 156 ta plitka kerak, usta esa "
                               "sinib qolishi mumkinligi uchun 12 ta "
                               "zaxira qoʻshdi: 156 + 12 = 168 ta.",
            },
        ],
        "body": """
<p><b>Dushanba.</b> Sinfimizga taʼmir boshlandi. Eski pol olib tashlandi,
oʻrniga plitka yotqiziladi. Direktor ustaga: «Hisobni oʻquvchilar bilan
birga qiling, foydasi tegadi», — dedi.</p>

<p><b>Seshanba.</b> Bugun oʻlchadik. Sinf
<span class="cn-word" data-tr="burchaklari 90° boʻlgan parallelogramm">toʻgʻri toʻrtburchak</span>:
<span class="cn-word" data-tr="toʻgʻri toʻrtburchakning katta oʻlchovi">uzunlik</span>i
<strong>7</strong> metr,
<span class="cn-word" data-tr="toʻgʻri toʻrtburchakning kichik oʻlchovi">en</span>i
<strong>6</strong> metr. Usta menga
<span class="cn-word" data-tr="shakl ichiga sigʻadigan birlik kvadratlar soni">yuza</span>ni
soʻradi.</p>

<p>Men avval 2 × (7 + 6) = 26 deb yozdim. Usta bosh chayqadi: «Bu —
<span class="cn-word" data-tr="shaklni oʻrab turgan chiziqning uzunligi">perimetr</span>,
plitka esa polning ichiga yotadi.» Toʻgʻri hisob koʻpaytirish orqali
ekan: 7 × 6 = <strong>42</strong>
<span class="cn-word" data-tr="tomoni 1 metr boʻlgan kvadratning yuzasi">m²</span>.</p>

<p>Burchakdagi katta shkaf joyidan qimirlamaydi. Uning tagi
2 × 1,5 = <strong>3</strong> m². Demak qoplanadigan yuza:
42 − 3 = <strong>39</strong> m².</p>

<p><b>Chorshanba.</b> Plitka keldi. Har biri
<span class="cn-word" data-tr="toʻrtala tomoni teng va burchaklari 90° boʻlgan shakl">kvadrat</span>,
tomoni <strong>50</strong>
<span class="cn-word" data-tr="metrning yuzdan bir qismi">santimetr</span>.
Usta: «Avval
<span class="cn-word" data-tr="hamma sonni bir xil oʻlchovga oʻtkazish">birliklarni tenglashtir</span>»,
— dedi. 50 sm = <strong>0,5</strong> metr, demak bitta plitkaning yuzasi
0,5 × 0,5 = <strong>0,25</strong> m².</p>

<p>Nechta kerak? Xonaning yuzasini bitta plitkaning yuzasiga
<span class="cn-word" data-tr="qanchaga boʻlinishini topish amali">boʻlish</span>
kifoya: 39 ÷ 0,25 = <strong>156</strong> ta.</p>

<p>Usta buyurtmaga <strong>12</strong> ta qoʻshdi: «Kesganda ham, tashiganda
ham sinadi. <span class="cn-word" data-tr="ehtimoliy yoʻqotish uchun ortiqcha olingan miqdor">Zaxira</span>siz
ish boshlamaymiz.» Jami <strong>168</strong> ta.</p>

<p><b>Payshanba.</b> Plitka yotqizildi. Oxirida oltita butun plitka va bir
nechta kesilgani ortdi.</p>

<p>Bugun bir narsani tushundim: <b>perimetr</b> va <b>yuza</b> —
butunlay boshqa savollar. Devor boʻylab ketadigan plintus uchun perimetr
kerak boʻladi. Pol uchun esa yuza. Birligiga qarasang, qaysi biri ekani
darrov bilinadi:
<span class="cn-word" data-tr="uzunlik birligi">metr</span> yoki kvadrat metr.</p>
""",
    },
]
