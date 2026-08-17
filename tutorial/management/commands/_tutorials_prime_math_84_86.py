# -*- coding: utf-8 -*-
"""Prime Math — darslar 84–86 (ehtimollik hisobi; masala oʻqish; nomaʼlum tanlash).

**PM-84 Blok F ni yopadi (Maʼlumot va ehtimollik, 75–84).
  PM-85 va PM-86 Blok G ni ochadi (Matnli masalalar ustaxonasi, 85–94).**
Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md

  mashqlar — practice/management/commands/_practice_pm_84_86.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_84_86.py

⚠️ Bu batch kursning burilish nuqtasi. PM-84 gacha kurs HISOBLASHNI
   oʻrgatdi; Blok G dan boshlab kurs MASALANI OʻQISHNI oʻrgatadi.
   Shuning uchun PM-85 da bitta ham yangi formula yoʻq — faqat toʻrt
   qadam va pm-word jadvali; butun ogʻirlik toʻliq yechilgan
   masalalarda. PM-86 esa bitta savolga javob beradi: NIMANI x deb
   olish kerak. Javob: hamma narsa oʻlchanadigan eng kichik miqdorni.

⚠️ Kumulyativ chegaralar:
  • PM-84 — P = qulay ÷ jami ni SANASH bilan birga (PM-82), teskari
    hodisa 1 − P, va nisbiy chastota (tajriba). ⛔ Shartli ehtimollik
    va hodisalar yigʻindisi/koʻpaytmasi qoidalari YOʻQ — kursda umuman
    yoʻq;
  • PM-85 — masalani oʻqishning toʻrt qadami. ⛔ Chizma usuli PM-87 da,
    ortiqcha/yetishmayotgan maʼlumot PM-94 da;
  • PM-86 — nomaʼlumni tanlash va jadval. ⛔ Harakat (PM-88/89), ish
    (PM-90), aralashma (PM-91), narx-miqdor-qiymat maxsus usul sifatida
    (PM-92) va yosh masalalari (PM-93) YOʻQ — bu yerda jadval faqat
    umumiy vosita sifatida koʻrsatiladi.
  • Faol ishlatiladi: sanash prinsipi (PM-82), ehtimollik gʻoyasi
    (PM-83), kasr↔oʻnlik↔foiz (PM-22), yaxlitlash (PM-14), tenglama
    (PM-36/37), matnli masaladan tenglama (PM-38/39), sistema (PM-53).

⚠️ Arifmetika darvozasi: scratchpad/verify_pm_84_86.py hamma sonni
   qayta hisoblaydi (36 ta hol, 11/36, chastotalar, 135 000, 48/36,
   16 000/24 000, 40 000/80 000/60 000, 12 000/36 000, 5/25 chipta).

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_84_86.py --author=prime
"""

PLAYLIST = {
    "title": "Prime Math",
    "category": "math",
    "description": (
        "Maktab matematikasi noldan — 100 ta dars. Sonlar, kasr va foiz, algebra, "
        "grafik, geometriya, statistika va matnli masalalar. Hammasi oʻzbek tilida, "
        "har bir qoida nega ishlashi tushuntirilgan."
    ),
}

TUTORIALS = [
    # ══════════════════════════════════════════════════════════════════
    # PM-84 — ehtimollikni hisoblash va tajriba bilan tekshirish
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-84: Ehtimollikni hisoblash va tajriba bilan tekshirish",
        "category": "math",
        "order": 84,
        "summary": (
            "Ehtimollikni ikki yoʻl bilan topamiz: hollarni sanab hisoblab "
            "va tajriba oʻtkazib. Teskari hodisa qoidasi (1 − P) koʻp "
            "masalani bir qatorga qisqartiradi."
        ),
        "stories": ["Lotereya nega yutqazadi"],
        "content": """
<h2>PM-84: Ehtimollikni hisoblash va tajriba bilan tekshirish</h2>

<p>Ikkita zar tashlaymiz va yigʻindisi 7 chiqishiga umid qilamiz. Nega
aynan 7? Chunki 7 — eng koʻp uchraydigan yigʻindi. Buni qaydan bilamiz?</p>

<p>Ikki yoʻl bor. Birinchisi — hamma hollarni <b>sanab</b>, formulaga
qoʻyish. Ikkinchisi — zarni yuz marta tashlab, <b>hisoblab turish</b>.
Bu darsda ikkalasini ham oʻrganamiz va ular bir-birini tekshirishini
koʻramiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>koʻpaytirish prinsipi bilan jami hollarni sanaysiz;</li>
    <li>teskari hodisa qoidasini (1 − P) qoʻllaysiz;</li>
    <li>nisbiy chastotani hisoblab, uni ehtimollik bilan solishtirasiz;</li>
    <li>qachon faqat tajriba yordam berishini bilib olasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki yoʻl, bitta son</span>
  <span class="pe-chip pe-chip--o">qulay ÷ jami</span>
  <span class="pe-op">≈</span>
  <span class="pe-chip pe-chip--v">roʻy berdi ÷ tajriba soni</span>
</div>

<h3>1. Jami hollarni sanash — PM-82 shu yerda kerak boʻladi</h3>

<p>PM-83 da formulani oʻrgandik: <b>P = qulay hollar ÷ jami hollar</b>.
Zar va tanga uchun jami hollar koʻrinib turardi: 6 va 2. Endi
qiyinrogʻi.</p>

<p>Ikkita zar tashlandi. Jami nechta hol bor?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Birinchi zar — 6 xil natija</span>
    <span class="pm-solve__why">1, 2, 3, 4, 5, 6</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Ikkinchi zar — yana 6 xil natija</span>
    <span class="pm-solve__why">Birinchisi qanday tushishidan qatʼi nazar</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">6 × 6 = 36 ta hol</span>
    <span class="pm-solve__why">Koʻpaytirish prinsipi (PM-82)</span>
  </div>
</div>

<p>Endi yigʻindisi 7 boʻlgan hollarni sanaymiz. Birinchi zarni oldin
yozamiz, shuning uchun (1; 6) va (6; 1) — ikkita <b>har xil</b> hol:</p>

<div class="pe-ex">
  <p class="pe-ex__math">(1; 6) (2; 5) (3; 4) (4; 3) (5; 2) (6; 1) — 6 ta hol</p>
  <p class="pe-ex__uz">Yigʻindisi 7 boʻladigan oltita juftlik bor.</p>
</div>

<div class="pm-solve">
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">P(7) = 6 ÷ 36 = <sup>1</sup>/<sub>6</sub> ≈ 0,17</span>
    <span class="pm-solve__why">Olti qulay hol, jami 36 ta</span>
  </div>
</div>

<p>Endi 8 ni sanaymiz: (2; 6) (3; 5) (4; 4) (5; 3) (6; 2) — <b>beshta</b>
hol. Demak P(8) = 5 ÷ 36 ≈ 0,14. Haqiqatan ham 7 ehtimolliroq ekan.</p>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Yigʻindilar teng imkoniyatli EMAS</p>
  <p>Ikki zarning yigʻindisi 2 dan 12 gacha — oʻn bir xil son.
  «Demak har birining ehtimolligi <sup>1</sup>/<sub>11</sub>» deb
  oʻylash — eng koʻp uchraydigan xato. Yigʻindi 2 faqat bitta yoʻl
  bilan chiqadi (1; 1), yigʻindi 7 esa oltita yoʻl bilan. Formula
  <b>teng imkoniyatli</b> hollarni talab qiladi, yigʻindilar esa teng
  emas — shuning uchun maxrajda 11 emas, <b>36</b> turadi.</p>
</div>

<h3>2. Teskari hodisa: 1 − P</h3>

<p>Baʼzan qulay hollarni sanash uzoq, teskarisini sanash esa oson. Shunda
teskari tomondan yuriladi.</p>

<div class="pe-formula">
  <span class="pe-formula__label">Teskari hodisa qoidasi</span>
  <span class="pe-chip pe-chip--s">P(A roʻy bermasligi)</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">1</span>
  <span class="pe-op">−</span>
  <span class="pe-chip pe-chip--o">P(A)</span>
</div>

<p>Nega ishlaydi? Hodisa yo roʻy beradi, yo bermaydi — uchinchi yoʻl
yoʻq. Demak ularning ehtimolliklari yigʻindisi butun 1 ni beradi.</p>

<div class="pe-ex">
  <p class="pe-ex__math">P(zarda 6 emas) = 1 − <sup>1</sup>/<sub>6</sub> = <sup>5</sup>/<sub>6</sub></p>
  <p class="pe-ex__uz">Oltita yoqdan beshtasi olti emas.</p>
</div>

<p>Endi qoida haqiqatan ish beradigan masala. <b>Ikkita zar tashlandi.
Kamida bitta 6 tushish ehtimolligi qancha?</b></p>

<p>«Kamida bitta» — bu bir 6, ikkita 6, birinchi zarda 6, ikkinchisida
6… sanash chalkash. Teskarisi esa juda tiniq: <b>hech bir zarda 6
yoʻq</b>.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Jami hollar: 6 × 6 = 36</span>
    <span class="pm-solve__why">Koʻpaytirish prinsipi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">6 siz hollar: 5 × 5 = 25</span>
    <span class="pm-solve__why">Har bir zarda 6 dan boshqa 5 xil natija</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">P(6 yoʻq) = 25 ÷ 36</span>
    <span class="pm-solve__why">Teskari hodisaning ehtimolligi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">P(kamida bitta 6) = 1 − <sup>25</sup>/<sub>36</sub> = <sup>11</sup>/<sub>36</sub> ≈ 0,31</span>
    <span class="pm-solve__why">Butundan teskarisini ayirdik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>36 ta holdan 25 tasida 6 yoʻq, demak qolgan 36 − 25 = 11 tasida
  kamida bitta 6 bor. 11 ÷ 36 ≈ 0,31 ✓ — ikki yoʻl bir xil javob berdi.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">«Kamida bitta» degan soʻzni koʻrsangiz</p>
  <p>Deyarli har doim teskari hodisa qulayroq. «Kamida bitta» ning
  teskarisi — <b>bitta ham emas</b>, va uni sanash odatda bitta
  koʻpaytmaga sigʻadi.</p>
</div>

<h3>3. Ikkinchi yoʻl: tajriba va nisbiy chastota</h3>

<p>Zarni sanash mumkin edi, chunki uning oltita yogʻi teng. Lekin
knopkani (kanselyariya tugmasini) tashlasak, u uchi bilan tushadimi yoki
yonboshlab? Bu yerda sanaydigan «teng yoq» yoʻq. Bitta chora qoladi —
tashlab koʻrish.</p>

<div class="pe-formula">
  <span class="pe-formula__label">Nisbiy chastota</span>
  <span class="pe-chip pe-chip--s">chastota</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">hodisa roʻy bergan marta</span>
  <span class="pe-op">÷</span>
  <span class="pe-chip pe-chip--o">jami tajriba</span>
</div>

<p>Dilnoza tangani tashladi va gerb necha marta tushganini yozib bordi.
Uning daftari:</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Necha marta tashlandi</th><th>Gerb tushdi</th><th>Nisbiy chastota</th></tr>
  <tr><td>20</td><td class="pm-word__sym">13</td><td>13 ÷ 20 = 0,650</td></tr>
  <tr><td>50</td><td class="pm-word__sym">29</td><td>29 ÷ 50 = 0,580</td></tr>
  <tr><td>100</td><td class="pm-word__sym">56</td><td>56 ÷ 100 = 0,560</td></tr>
  <tr><td>200</td><td class="pm-word__sym">106</td><td>106 ÷ 200 = 0,530</td></tr>
  <tr><td>500</td><td class="pm-word__sym">254</td><td>254 ÷ 500 = 0,508</td></tr>
</table></div>

<figure class="pm-fig">
  <svg viewBox="0 0 320 200" role="img" aria-label="Gerb chastotasi tajriba soni ortgani sari 0,5 ga yaqinlashadi">
    <line class="pm-ch__grid" x1="46" y1="30" x2="302" y2="30"/>
    <text class="pm-ch__cap" x="40" y="34" text-anchor="end">1,0</text>
    <text class="pm-ch__cap" x="40" y="99" text-anchor="end">0,5</text>
    <line class="pm-ch__ax" x1="46" y1="160" x2="302" y2="160"/>
    <text class="pm-ch__cap" x="40" y="164" text-anchor="end">0</text>
    <line class="pm-ch__ref" x1="46" y1="95" x2="302" y2="95"/>
    <polyline class="pm-ch__line" points="76,75.5 130,84.6 184,87.2 238,91.1 292,94"/>
    <circle class="pm-ch__dot" cx="76" cy="75.5" r="4"/>
    <circle class="pm-ch__dot" cx="130" cy="84.6" r="4"/>
    <circle class="pm-ch__dot" cx="184" cy="87.2" r="4"/>
    <circle class="pm-ch__dot" cx="238" cy="91.1" r="4"/>
    <circle class="pm-ch__dot" cx="292" cy="94" r="4"/>
    <text class="pm-ch__val" x="76" y="66" text-anchor="middle">0,65</text>
    <text class="pm-ch__val" x="130" y="76" text-anchor="middle">0,58</text>
    <text class="pm-ch__val" x="184" y="78" text-anchor="middle">0,56</text>
    <text class="pm-ch__val" x="238" y="82" text-anchor="middle">0,53</text>
    <text class="pm-ch__val" x="290" y="85" text-anchor="middle">0,508</text>
    <text class="pm-ch__lbl" x="76" y="176" text-anchor="middle">20</text>
    <text class="pm-ch__lbl" x="130" y="176" text-anchor="middle">50</text>
    <text class="pm-ch__lbl" x="184" y="176" text-anchor="middle">100</text>
    <text class="pm-ch__lbl" x="238" y="176" text-anchor="middle">200</text>
    <text class="pm-ch__lbl" x="292" y="176" text-anchor="middle">500</text>
    <text class="pm-ch__cap" x="302" y="115" text-anchor="end">punktir — kutilgan 0,5</text>
  </svg>
  <figcaption>Tajriba koʻpaygan sari chastota 0,5 ga yaqinlashib boradi.
  Oʻq 0 dan boshlangan — PM-81 dagi qoida bu yerda ham amal qiladi.</figcaption>
</figure>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Koʻp takrorlash qoidasi</p>
  <p>Tajriba soni ortgani sari nisbiy chastota ehtimollikka
  <b>yaqinlashadi</b>. 20 ta tashlashda 0,65 chiqishi mumkin va bu hech
  qanday gʻalati emas; 500 ta tashlashda esa 0,5 dan uzoqlashish deyarli
  imkonsiz. Shuning uchun bitta qisqa tajribaga ishonib xulosa
  chiqarilmaydi.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Tanga «qarzdor» emas</p>
  <p>Ketma-ket besh marta gerb tushdi — endi raqam tushish ehtimolligi
  ortadimi? <b>Yoʻq.</b> Tangada xotira yoʻq: keyingi tashlashda ham
  P = 0,5. Chastota 0,5 ga qaytishi kelgusi natijalar «tuzatgani» uchun
  emas, yangi tashlashlar soni koʻpayib, eski beshtasining ulushi
  kichrayib ketgani uchun.</p>
</div>

<h3>4. Qachon faqat tajriba qoladi</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Sanab hisoblanadi</p>
    <p>Tanga, zar, qopchadagi sharlar, lotereya biletlari — natijalar
    teng imkoniyatli va sanoqli.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Faqat tajriba</p>
    <p>Knopka, ob-havo, jamoaning gʻalabasi, lampochkaning ishlash
    muddati — teng yoqlar yoʻq, kuzatuv kerak.</p>
  </div>
</div>

<p>PM-83 da ob-havo bashoratidagi «60% yomgʻir» soni haqida gapirgan
edik. Mana u qayerdan olinadi: bugungiga oʻxshash ob-havo sharoiti
oʻtmishda 100 marta kuzatilgan boʻlsa va shulardan 60 tasida yomgʻir
yoqqan boʻlsa, chastota 60 ÷ 100 = 0,6 boʻladi. Bu — sanab emas,
<b>kuzatib</b> olingan ehtimollik.</p>

<h3>Matnli masala</h3>

<p>Bekzodning qutisida faqat qizil va koʻk sharlar bor. Jami 20 ta shar
borligini biladi, lekin nechtadan ekanini bilmaydi. U 60 marta koʻzini
yumib bitta shar oldi, rangini yozdi va sharni qutiga qaytarib soldi.
Koʻk shar 45 marta chiqdi.</p>

<p><b>Qutida taxminan nechta koʻk shar bor?</b></p>

<p><b>Reja:</b> tajribadan nisbiy chastotani topamiz. U koʻk shar
chiqish ehtimolligiga yaqin. Keyin bu ehtimollikni 20 ta sharga
qoʻllaymiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">chastota = 45 ÷ 60 = 0,75</span>
    <span class="pm-solve__why">Koʻk chiqqan marta ÷ jami tajriba</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">P(koʻk) ≈ 0,75</span>
    <span class="pm-solve__why">60 ta tajriba — yetarlicha koʻp</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">koʻk sharlar ≈ 20 × 0,75</span>
    <span class="pm-solve__why">Jami sharlarning 75 foizi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 15 ta koʻk shar</span>
    <span class="pm-solve__why">Qolgani 20 − 15 = 5 ta qizil</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Agar qutida 15 koʻk va 5 qizil shar boʻlsa, P(qizil) = 5 ÷ 20 =
  0,25. Tajribada qizil 60 − 45 = 15 marta chiqqan, ya'ni chastotasi
  15 ÷ 60 = 0,25 ✓
  <br><b>Javob:</b> qutida taxminan 15 ta koʻk shar bor.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>45 — 60 ning uchdan toʻrt qismi. Demak sharlarning ham
  taxminan uchdan toʻrti koʻk: 20 ning <sup>3</sup>/<sub>4</sub> qismi
  15 ta.</span>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">«Taxminan» soʻzi bejiz emas</p>
  <p>Tajriba aniq javob bermaydi — u <b>baho</b> beradi. Boshqa 60 ta
  tajribada koʻk 43 yoki 47 marta chiqishi mumkin edi. Shuning uchun
  javobda «taxminan 15» deb yoziladi, «roppa-rosa 15» deb emas.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Ikki zarning yigʻindisi 2 dan 12 gacha, demak
  P(7) = <sup>1</sup>/<sub>11</sub></p>
  <p class="pe-fix__good">P(7) = 6 ÷ 36 = <sup>1</sup>/<sub>6</sub></p>
  <p class="pe-fix__why">Yigʻindilar teng imkoniyatli emas. Maxrajda
  <b>teng imkoniyatli</b> hollar turadi — ular 36 ta juftlik.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">P(kamida bitta 6) = <sup>1</sup>/<sub>6</sub> +
  <sup>1</sup>/<sub>6</sub> = <sup>2</sup>/<sub>6</sub></p>
  <p class="pe-fix__good">1 − <sup>25</sup>/<sub>36</sub> =
  <sup>11</sup>/<sub>36</sub></p>
  <p class="pe-fix__why">Ikkala zarda ham 6 tushgan hol ikki marta
  sanaladi. Qoʻshish oʻrniga teskari hodisadan yuriladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">P(yutmaslik) = 1 ÷ P(yutish)</p>
  <p class="pe-fix__good">P(yutmaslik) = 1 − P(yutish)</p>
  <p class="pe-fix__why">Teskari hodisada <b>ayiriladi</b>, boʻlinmaydi.
  P = 0,25 boʻlsa, 1 ÷ 0,25 = 4 — bu ehtimollik boʻlishi mumkin emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">20 marta tashlaganda gerb 13 marta tushdi —
  demak bu tanga nosoz</p>
  <p class="pe-fix__good">20 ta tajriba xulosa uchun juda kam</p>
  <p class="pe-fix__why">Kichik tajribada chastota 0,5 dan ancha
  chetlashishi tabiiy. Xulosa uchun yuzlab tashlash kerak.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Ikkita zar tashlandi. Jami nechta hol bor va
  yigʻindisi 5 boʻlgan nechta hol bor?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>36 ta hol, ulardan 4 tasi.</b> Jami 6 × 6 = 36. Yigʻindisi 5:
    (1; 4) (2; 3) (3; 2) (4; 1) — toʻrtta. P = 4 ÷ 36 =
    <sup>1</sup>/<sub>9</sub> ≈ 0,11.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Bir hodisaning ehtimolligi 0,3. Uning roʻy
  bermaslik ehtimolligi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>0,7.</b> Teskari hodisa qoidasi: 1 − 0,3 = 0,7. Foizda
    aytganda 70%.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Ikkita zar tashlandi. Kamida bitta 1 tushish
  ehtimolligi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b><sup>11</sup>/<sub>36</sub> ≈ 0,31.</b> 1 siz hollar:
    5 × 5 = 25. Demak 1 − 25 ÷ 36 = 11 ÷ 36. Bu 6 bilan bir xil javob —
    zarning yoqlari teng huquqli.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Sherbek knopkani 200 marta tashladi; u
  76 marta uchi bilan yuqoriga tushdi. Nisbiy chastotani toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>0,38.</b> 76 ÷ 200 = 0,38, ya'ni 38%. Knopkani sanab
    hisoblab boʻlmaydi — faqat shunday tajriba yordam beradi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Tanga ketma-ket 4 marta gerb tomoni bilan
  tushdi. Beshinchi tashlashda raqam tushish ehtimolligi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>0,5.</b> Tangada xotira yoʻq. Oldingi natijalar keyingisiga
    umuman taʼsir qilmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Qopchada 8 ta yashil va 12 ta sariq shar bor.
  Bitta shar olindi. Yashil <b>chiqmaslik</b> ehtimolligini ikki yoʻl
  bilan toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>0,6.</b> Toʻgʻridan-toʻgʻri: sariqlar 12 ta, 12 ÷ 20 = 0,6.
    Teskari hodisa bilan: P(yashil) = 8 ÷ 20 = 0,4, demak
    1 − 0,4 = 0,6 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">7. Afsona qutidagi rangli qalamlar bilan tajriba
  qildi: 80 marta qalam olib, rangini yozib, qaytarib soldi. Qizil qalam
  20 marta chiqdi. Qutida jami 12 ta qalam bor. Taxminan nechtasi
  qizil?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Taxminan 3 ta.</b> chastota = 20 ÷ 80 = 0,25. Demak
    12 × 0,25 = 3 ta qizil qalam. Tekshiramiz: 3 ÷ 12 = 0,25 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Ehtimollik</b><span>hodisaning roʻy berish imkoniyati oʻlchovi;
    ingl. probability</span></li>
  <li><b>Teskari hodisa</b><span>berilgan hodisa roʻy bermasligi;
    ingl. complementary event</span></li>
  <li><b>Nisbiy chastota</b><span>roʻy bergan marta ÷ jami tajriba;
    ingl. relative frequency</span></li>
  <li><b>Tajriba</b><span>natijasi oldindan nomaʼlum boʻlgan takroriy
    sinov; ingl. experiment</span></li>
  <li><b>Sinov</b><span>tajribaning bitta takrori; ingl. trial</span></li>
  <li><b>Koʻpaytirish prinsipi</b><span>bosqichlardagi variantlar
    koʻpaytiriladi; ingl. counting principle</span></li>
  <li><b>Teng imkoniyatli</b><span>hamma natijaning imkoniyati bir xil;
    ingl. equally likely</span></li>
  <li><b>Kutilgan qiymat</b><span>uzoq muddatda kutiladigan oʻrtacha
    natija; ingl. expected value</span></li>
  <li><b>Baho</b><span>aniq emas, taxminiy qiymat; ingl.
    estimate</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Jami hollarni koʻpaytirish prinsipi bilan sanaladi: ikki zar —
      6 × 6 = 36.</li>
    <li>Maxrajda teng imkoniyatli hollar turadi, natija turlari
      emas.</li>
    <li>P(A roʻy bermasligi) = 1 − P(A). «Kamida bitta» — deyarli har
      doim shu qoida.</li>
    <li>Nisbiy chastota = roʻy bergan marta ÷ jami tajriba.</li>
    <li>Tajriba koʻpaygan sari chastota ehtimollikka yaqinlashadi.</li>
    <li>Teng yoqlar boʻlmaganda (knopka, ob-havo) faqat tajriba
      qoladi.</li>
    <li>Tasodifda xotira yoʻq: oldingi natija keyingisiga taʼsir
      qilmaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-85 — masalani oʻqishning toʻrt qadami
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-85: Masalani oʻqishning toʻrt qadami",
        "category": "math",
        "order": 85,
        "summary": (
            "Matnli masala qiyin boʻlgani uchun emas, notoʻgʻri oʻqilgani "
            "uchun yechilmaydi. Toʻrt qadam: nima berilgan va nima soʻralgan, "
            "reja, yechish, tekshirish."
        ),
        "stories": ["Masalani qanday oʻqish kerak"],
        "content": """
<h2>PM-85: Masalani oʻqishning toʻrt qadami</h2>

<p>Sinfda eng koʻp eshitiladigan gap: «Men hisoblashni bilaman, lekin
masalani tushunmayapman». Bu — matematika muammosi emas, <b>oʻqish</b>
muammosi.</p>

<p>Shu darsdan boshlab kursning oxirgi qismi boshlanadi: matnni
matematikaga aylantirish ustaxonasi. Bu yerda yangi formula yoʻq.
Bor-yoʻgʻi toʻrtta qadam bor — va ular ishlaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>har qanday masalani toʻrt qadamga ajratasiz;</li>
    <li>berilgan bilan soʻralganni bir-biridan ajratasiz;</li>
    <li>soʻzni belgiga aylantirish jadvalidan foydalanasiz;</li>
    <li>javobni doim tekshirib, gap bilan yozib beradigan boʻlasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Toʻrt qadam</span>
  <span class="pe-chip pe-chip--o">Oʻqi</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">Reja tuz</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">Yech</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--adv">Tekshir</span>
</div>

<h3>1. Qadamlar nima deydi</h3>

<div class="pe-steps">
  <ol>
    <li><b>Oʻqi.</b> Ikki marta oʻqing. Birinchi oʻqishda voqeani
      tushunasiz, ikkinchisida sonlarni yozib olasiz. Soʻralgan savolni
      alohida yozing — koʻpincha xato aynan shu yerda boshlanadi.</li>
    <li><b>Reja tuz.</b> Nomaʼlumni tanlang va unga nom bering
      («x — Dilnoza chizgan rasmlar soni»). Berilganlar bilan
      nomaʼlumni bogʻlaydigan gapni toping va uni tenglamaga
      aylantiring.</li>
    <li><b>Yech.</b> Endi hisoblaysiz. Bu — eng oson qadam, chunki
      birinchi ikkitasi bajarilgan boʻlsa, faqat texnika qoladi.</li>
    <li><b>Tekshir.</b> Javobni masalaning oʻz gaplariga qaytarib
      qoʻying. Birlik toʻgʻrimi? Javob mantiqiymi? Va eng muhimi:
      <b>soʻralgan narsa shumi?</b></li>
  </ol>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Birinchi qadam eng uzun boʻlishi kerak</p>
  <p>Yaxshi yechuvchi vaqtining yarmini oʻqishga sarflaydi, hisoblashga
  esa oz. Yomon yechuvchi darrov hisoblay boshlaydi va notoʻgʻri
  savolga toʻgʻri javob topadi.</p>
</div>

<h3>2. Soʻzni belgiga aylantirish</h3>

<p>Matnli masalaning yuragi shu jadvalda. Uni yod olish shart emas —
lekin har bir qatorni tanish shart.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Matnda shunday deyiladi</th><th>Matematikada</th><th>Misol</th></tr>
  <tr><td>…dan 5 ta koʻp</td><td class="pm-word__sym">+ 5</td><td>x + 5</td></tr>
  <tr><td>…dan 5 ta kam</td><td class="pm-word__sym">− 5</td><td>x − 5</td></tr>
  <tr><td>…dan 3 marta koʻp</td><td class="pm-word__sym">× 3</td><td>3x</td></tr>
  <tr><td>…dan 3 marta kam</td><td class="pm-word__sym">÷ 3</td><td>x ÷ 3</td></tr>
  <tr><td>…ning yarmi</td><td class="pm-word__sym">÷ 2</td><td>x ÷ 2</td></tr>
  <tr><td>jami, birgalikda</td><td class="pm-word__sym">+</td><td>x + y</td></tr>
  <tr><td>nechtaga koʻp?</td><td class="pm-word__sym">−</td><td>katta − kichik</td></tr>
  <tr><td>necha marta koʻp?</td><td class="pm-word__sym">÷</td><td>katta ÷ kichik</td></tr>
  <tr><td>har biriga 4 tadan</td><td class="pm-word__sym">× 4</td><td>4n</td></tr>
  <tr><td>kamida 12</td><td class="pm-word__sym">≥ 12</td><td>x ≥ 12</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">«Nechtaga koʻp» va «necha marta koʻp»</p>
  <p>Bu ikkisi bir-biriga eng koʻp aralashadigan juftlik, va bu
  matematika xatosi emas — <b>til</b> xatosi. «12 ta koʻp» — ayirma
  (qoʻshiladi yoki ayiriladi). «12 marta koʻp» — nisbat (koʻpaytiriladi
  yoki boʻlinadi). Masalada shu ikki soʻzni har doim doira ichiga
  oling.</p>
</div>

<h3>3. Birinchi misol — toʻrt qadam toʻliq</h3>

<p><b>Masala.</b> Afsona 45 000 soʻmga daftar oldi. Bu uning pulining
uchdan bir qismi edi. Afsonada qancha pul bor edi?</p>

<div class="pe-steps">
  <ol>
    <li><b>Oʻqi.</b> Berilgan: daftar 45 000 soʻm; bu — jami pulning
      <sup>1</sup>/<sub>3</sub> qismi. Soʻralgan: <b>jami pul</b>.</li>
    <li><b>Reja.</b> x — Afsonaning jami puli. «Pulining uchdan bir
      qismi» degani x ÷ 3. Demak x ÷ 3 = 45 000.</li>
    <li><b>Yech.</b> x = 45 000 × 3 = 135 000.</li>
    <li><b>Tekshir.</b> 135 000 ÷ 3 = 45 000 ✓ Javob soʻmda, musbat,
      daftar narxidan katta — mantiqiy.</li>
  </ol>
</div>

<div class="pm-check">
  <p class="pm-check__t">Javob gap bilan</p>
  <p>«Afsonada 135 000 soʻm bor edi.» Bitta son emas, gap. Shunda
  savolga javob berilgan-berilmagani darrov koʻrinadi.</p>
</div>

<h3>4. Ikkinchi misol — ikkita miqdor, bitta bogʻlanish</h3>

<p><b>Masala.</b> Ikki qutida jami 84 ta olma bor. Birinchi qutida
ikkinchisidan 12 ta koʻp. Har bir qutida nechtadan?</p>

<p><b>1-qadam.</b> Berilgan: jami 84; farq 12. Soʻralgan: har bir
qutidagi olmalar soni — ya'ni <b>ikkita</b> son.</p>

<p><b>2-qadam.</b> x — ikkinchi qutidagi olmalar (kichigi). Unda
birinchi quti — x + 12. Jami: x + (x + 12) = 84.</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">2-quti</span>
    <span class="pm-model__bar" style="width:43%">x</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">1-quti</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:57%">x + 12</span>
  </div>
  <p class="pm-model__tot">Jami: x + (x + 12) = 84</p>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + x + 12 = 84</span>
    <span class="pm-solve__why">Qavsni ochdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + 12 = 84</span>
    <span class="pm-solve__why">Oʻxshash hadlarni ixchamladik (PM-32)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x = 72</span>
    <span class="pm-solve__why">Ikki tomondan 12 ni ayirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 36, x + 12 = 48</span>
    <span class="pm-solve__why">Ikki tomonni 2 ga boʻldik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>36 + 48 = 84 ✓ va 48 − 36 = 12 ✓ Ikkala shart ham bajarildi.
  <br><b>Javob:</b> ikkinchi qutida 36 ta, birinchisida 48 ta olma.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Ikkala shartni ham tekshiring</p>
  <p>Masalada ikkita shart bor edi — yigʻindi va farq. Faqat
  bittasini tekshirish yetarli emas: 40 va 44 ham yigʻindisi 84 beradi,
  lekin farqi 12 emas.</p>
</div>

<h3>5. Uchinchi misol — sonlar qulay emas</h3>

<p><b>Masala.</b> Sherbek doʻkondan 2 kg guruch va 3 kg un olib,
96 000 soʻm toʻladi. Guruchning bir kilosi unning bir kilosidan
8 000 soʻm qimmat. Har birining kilosi necha soʻm?</p>

<p><b>Reja:</b> x — unning bir kilosi (kichigi). Guruch — x + 8 000.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2(x + 8000) + 3x = 96 000</span>
    <span class="pm-solve__why">2 kg guruch pul + 3 kg un puli</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + 16 000 + 3x = 96 000</span>
    <span class="pm-solve__why">Qavsni ochdik (PM-33)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5x + 16 000 = 96 000</span>
    <span class="pm-solve__why">Oʻxshash hadlar</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5x = 80 000</span>
    <span class="pm-solve__why">16 000 ni ayirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 16 000; guruch = 24 000</span>
    <span class="pm-solve__why">5 ga boʻldik, keyin 8 000 qoʻshdik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>2 kg guruch: 2 × 24 000 = 48 000 soʻm. 3 kg un: 3 × 16 000 =
  48 000 soʻm. Jami 96 000 ✓ Farq: 24 000 − 16 000 = 8 000 ✓
  <br><b>Javob:</b> un 16 000 soʻm, guruch 24 000 soʻm.</p>
</div>

<h3>Matnli masala</h3>

<p>Bekzod va Dilnoza birgalikda 96 ta rasm chizishdi. Bekzod
Dilnozadan 3 marta koʻp chizdi.</p>

<p><b>Bekzod Dilnozadan nechta koʻp rasm chizdi?</b></p>

<p><b>1-qadam.</b> Berilgan: jami 96; Bekzod = 3 × Dilnoza. Soʻralgan:
ularning <b>farqi</b> — ikkalasining soni emas, farqi. Bu savolni
alohida yozib qoʻyamiz.</p>

<p><b>2-qadam.</b> x — Dilnoza chizgan rasmlar (kichigi). Bekzod — 3x.</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">Dilnoza</span>
    <span class="pm-model__bar" style="width:25%">x</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">Bekzod</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:75%">3x</span>
  </div>
  <p class="pm-model__tot">Jami: x + 3x = 96</p>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + 3x = 96</span>
    <span class="pm-solve__why">Jami 96 ta rasm</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4x = 96</span>
    <span class="pm-solve__why">Oʻxshash hadlar</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = 24 — Dilnoza; 3x = 72 — Bekzod</span>
    <span class="pm-solve__why">4 ga boʻldik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">72 − 24 = 48</span>
    <span class="pm-solve__why">Savol farqni soʻragan edi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>24 + 72 = 96 ✓ va 72 ÷ 24 = 3 ✓ Ikkala shart bajarildi.
  <br><b>Javob:</b> Bekzod Dilnozadan 48 ta koʻp rasm chizdi.</p>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Toʻrtinchi qadamni tashlab ketmang</p>
  <p>Bu masalada x = 24 topilgandan keyin toʻxtash — eng oson va eng
  koʻp uchraydigan xato. 24 ham, 72 ham toʻgʻri hisoblangan, lekin
  savolga javob emas. Tekshirish qadami aynan shuni ushlaydi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Ikki son yigʻindisi 60, biri ikkinchisidan
  3 marta katta. Katta son — 15</p>
  <p class="pe-fix__good">Katta son — 45</p>
  <p class="pe-fix__why">x + 3x = 60 → x = 15, lekin x — <b>kichik</b>
  son. Savol kattasini soʻragan: 3 × 15 = 45.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Sinfda 32 oʻquvchi, qizlar oʻgʻillardan 6 taga
  kam → har biri 32 ÷ 2 = 16</p>
  <p class="pe-fix__good">Oʻgʻil 19, qiz 13</p>
  <p class="pe-fix__why">Teng boʻlish farqni yoʻqotadi. x + (x − 6) = 32
  → 2x = 38 → x = 19, qizlar 19 − 6 = 13.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Yoʻlga 2 soat 30 minut ketdi → 2 + 30 = 32</p>
  <p class="pe-fix__good">2 soat 30 minut = 150 minut (yoki 2,5 soat)</p>
  <p class="pe-fix__why">Har xil birlikdagi sonlar qoʻshilmaydi. Avval
  bitta birlikka keltiriladi: 2 × 60 + 30 = 150.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">«Afsonada 45 000 soʻm bor edi» (yuqoridagi
  birinchi misol)</p>
  <p class="pe-fix__good">«Afsonada 135 000 soʻm bor edi»</p>
  <p class="pe-fix__why">45 000 — berilgan son, javob emas. Masalani
  oxirigacha oʻqimay, koʻzga birinchi tashlangan son yozilgan.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Jasur Sherbekdan 7 ta koʻp kitob oʻqidi.»
  Sherbek x ta oʻqigan boʻlsa, Jasur nechta oʻqigan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>x + 7.</b> «7 ta koʻp» — qoʻshish, koʻpaytirish emas.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «Jasur Sherbekdan 7 marta koʻp kitob
  oʻqidi.» Endi-chi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>7x.</b> «marta» soʻzi koʻpaytirishni bildiradi. Bitta harf
    butun masalani oʻzgartirib yuboradi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Bir son va uning yarmi yigʻindisi 90 ga
  teng. Bu son qanday?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>60.</b> x + x ÷ 2 = 90 → 1,5x = 90 → x = 60. Tekshirish:
    60 + 30 = 90 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Ikki son yigʻindisi 100, farqi 20. Sonlarni
  toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>60 va 40.</b> x + (x + 20) = 100 → 2x = 80 → x = 40,
    ikkinchisi 60. Tekshirish: 40 + 60 = 100 ✓, 60 − 40 = 20 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Dilnoza kitobning uchdan bir qismini oʻqidi
  va 96 bet qoldi. Kitobda nechta bet bor?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>144 bet.</b> Uchdan biri oʻqilsa, <sup>2</sup>/<sub>3</sub>
    qismi qolgan: x × <sup>2</sup>/<sub>3</sub> = 96 → x = 96 × 3 ÷ 2 =
    144. Tekshirish: 144 ÷ 3 = 48 oʻqildi, 144 − 48 = 96 ✓ Diqqat: 96
    — oʻqilgani emas, qolgani.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Bogʻda olma daraxti nok daraxtidan 2 marta
  koʻp. Jami 54 ta daraxt bor. Olma daraxti nokdan nechtaga koʻp?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>18 taga koʻp.</b> x + 2x = 54 → x = 18 (nok), olma 36.
    Savol farqni soʻragan: 36 − 18 = 18. Tekshirish: 18 + 36 = 54 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">7. Sinf ekskursiyaga chiqdi. Avtobusda
  oʻrindiqlar 4 tadan qatorda joylashgan. 43 oʻquvchi va 3 oʻqituvchi
  bor. Kamida nechta qator kerak?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>12 qator.</b> Jami 43 + 3 = 46 kishi. 46 ÷ 4 = 11 qator va
    2 kishi qoldi (PM-4), demak yana bitta qator kerak: 11 + 1 = 12.
    «Kamida» soʻzi qoldiqni yuqoriga yaxlitlashni talab qiladi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Matnli masala</b><span>vaziyat matn bilan berilgan masala;
    ingl. word problem</span></li>
  <li><b>Berilgan</b><span>masalada aytilgan maʼlumot; ingl.
    given</span></li>
  <li><b>Soʻralgan</b><span>masalaning savoli; ingl. what is
    asked</span></li>
  <li><b>Nomaʼlum</b><span>topilishi kerak boʻlgan miqdor; ingl.
    unknown</span></li>
  <li><b>Shart</b><span>bajarilishi kerak boʻlgan bogʻlanish; ingl.
    condition</span></li>
  <li><b>Reja</b><span>yechishning oldindan tuzilgan yoʻli; ingl.
    plan</span></li>
  <li><b>Tenglama</b><span>ikki ifodaning tengligi; ingl.
    equation</span></li>
  <li><b>Tekshirish</b><span>javobni masala shartlariga qaytarib
    qoʻyish; ingl. checking</span></li>
  <li><b>Ayirma</b><span>«nechtaga koʻp» savolining javobi; ingl.
    difference</span></li>
  <li><b>Nisbat</b><span>«necha marta koʻp» savolining javobi; ingl.
    ratio</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Toʻrt qadam: oʻqi → reja tuz → yech → tekshir.</li>
    <li>Soʻralgan savolni alohida yozib qoʻying.</li>
    <li>Nomaʼlumga nom bering: «x — Dilnoza chizgan rasmlar soni».</li>
    <li>«ta koʻp» — qoʻshish, «marta koʻp» — koʻpaytirish.</li>
    <li>Masalaning hamma shartlarini tekshiring, bittasini emas.</li>
    <li>Javobni gap bilan yozing — shunda notoʻgʻri savolga javob
      berganingiz darrov koʻrinadi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-86 — nomaʼlumni tanlash va jadval tuzish
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-86: Nomaʼlumni tanlash va jadval tuzish",
        "category": "math",
        "order": 86,
        "summary": (
            "Bitta masalani ikki xil nomaʼlum bilan yechib koʻramiz va "
            "toʻgʻri tanlov ishni necha barobar yengillashtirishini koʻramiz. "
            "Jadval esa chalkash matnni tartibga soladi."
        ),
        "stories": ["Uch aka-uka va pul"],
        "content": """
<h2>PM-86: Nomaʼlumni tanlash va jadval tuzish</h2>

<p>PM-85 da toʻrt qadamni oʻrgandik. Ikkinchi qadamda «nomaʼlumni
tanlang» deyilgan edi — lekin qaysi birini?</p>

<p>Masalada uchta miqdor boʻlsa, x deb uchalasidan birini olish mumkin.
Uchalasi ham toʻgʻri javobga olib boradi. Faqat bittasi bilan yoʻl
qisqa va butun sonli, qolgan ikkitasi bilan esa kasrlar bilan
kurashasiz. Bu dars — ana shu tanlov haqida.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>x deb qaysi miqdorni olish kerakligini bilib olasiz;</li>
    <li>qolgan miqdorlarni x orqali yozasiz;</li>
    <li>chalkash masalani jadvalga solasiz;</li>
    <li>«boshida — keyin» jadvali bilan oʻzgarishli masalani yechasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Tanlash qoidasi</span>
  <span class="pe-chip pe-chip--s">x</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">qolganlari oʻzi orqali oʻlchanadigan miqdor</span>
</div>

<h3>1. Qaysi miqdorni x deb olish kerak</h3>

<p>Masala matnini oʻqing va shu savolni bering: <b>hamma boshqa
miqdorlar kimga qarab taʼriflangan?</b> Oʻsha miqdor x boʻladi.
Odatda u eng kichigi boʻlib chiqadi.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Matnda shunday deyilgan</th><th>x deb kimni olamiz</th><th>Qolganlari</th></tr>
  <tr><td>B — A dan 3 marta koʻp</td><td class="pm-word__sym">x = A</td><td>B = 3x</td></tr>
  <tr><td>B — A dan 5 taga koʻp</td><td class="pm-word__sym">x = A</td><td>B = x + 5</td></tr>
  <tr><td>A — B dan 4 marta kam</td><td class="pm-word__sym">x = A</td><td>B = 4x</td></tr>
  <tr><td>Jami 30 kishi, kattalar bor</td><td class="pm-word__sym">x = kattalar</td><td>bolalar = 30 − x</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Oddiy tekshiruv</p>
  <p>Nomaʼlumni tanlaganingizdan keyin qolgan miqdorlarni yozib
  koʻring. Agar birortasida kasr chiziq paydo boʻlsa — ehtimol
  notoʻgʻri miqdorni tanlagansiz. Qaytib, kichigini x deb oling.</p>
</div>

<h3>2. Bitta masala, ikkita tanlov</h3>

<p><b>Masala.</b> Uch doʻst birgalikda 180 000 soʻm topdi. Jasur
Afsonadan 2 marta koʻp oldi, Sherbek esa Afsonadan 20 000 soʻm koʻp
oldi. Har biri qancha oldi?</p>

<p>Hamma narsa <b>Afsonaga</b> qarab aytilgan — demak x = Afsona.</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">Afsona</span>
    <span class="pm-model__bar" style="width:25%">x</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">Jasur</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:50%">2x</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">Sherbek</span>
    <span class="pm-model__bar" style="width:37%">x + 20 000</span>
  </div>
  <p class="pm-model__tot">Jami: x + 2x + (x + 20 000) = 180 000</p>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + 2x + x + 20 000 = 180 000</span>
    <span class="pm-solve__why">Qavsni ochdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4x + 20 000 = 180 000</span>
    <span class="pm-solve__why">Oʻxshash hadlar: x + 2x + x = 4x</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4x = 160 000</span>
    <span class="pm-solve__why">20 000 ni ayirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 40 000</span>
    <span class="pm-solve__why">4 ga boʻldik</span>
  </div>
</div>

<p>Endi qolganlarini topamiz: Jasur — 2 × 40 000 = 80 000 soʻm;
Sherbek — 40 000 + 20 000 = 60 000 soʻm.</p>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>40 000 + 80 000 + 60 000 = 180 000 ✓
  <br>Jasur Afsonadan 2 marta koʻp: 80 000 ÷ 40 000 = 2 ✓
  <br>Sherbek Afsonadan 20 000 koʻp: 60 000 − 40 000 = 20 000 ✓
  <br><b>Javob:</b> Afsona 40 000, Jasur 80 000, Sherbek 60 000 soʻm.</p>
</div>

<h4>Endi noqulay tanlovni sinab koʻramiz</h4>

<p>Xuddi shu masalani x = <b>Jasur</b> deb yechsak nima boʻladi? Unda
Afsona — x ÷ 2, Sherbek — x ÷ 2 + 20 000.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + x ÷ 2 + (x ÷ 2 + 20 000) = 180 000</span>
    <span class="pm-solve__why">Hamma narsa Jasur orqali</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + 20 000 = 180 000</span>
    <span class="pm-solve__why">x ÷ 2 + x ÷ 2 = x, demak x + x = 2x</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 80 000 — Jasur</span>
    <span class="pm-solve__why">Javob oʻsha, lekin yoʻl kasrli edi</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Javob bir xil, mehnat har xil</p>
  <p>Ikkala tanlov ham 80 000 ni beradi — bu tasodif emas, masala bitta.
  Lekin birinchi yoʻlda faqat butun sonlar bor edi, ikkinchisida esa
  x ÷ 2 bilan ishlashga toʻgʻri keldi. Sonlar chiroyli chiqmaganda
  bunday kasrlar xatoga aylanadi. <b>Shuning uchun kichigini x deb
  oling.</b></p>
</div>

<h3>3. Jadval — chalkash matnni tartibga soladi</h3>

<p>Masalada ikkita holat boʻlsa (boshida va keyin, kelishdan oldin va
keyin), jadval matnni bir zumda tinchitadi. Ustunlar — holatlar,
qatorlar — qatnashchilar.</p>

<p><b>Masala.</b> Afsonada Jasurdan 3 marta koʻp pul bor edi. Afsona
Jasurga 12 000 soʻm berdi va shundan keyin pullari teng boʻldi. Boshida
har birida qancha pul bor edi?</p>

<p>x = Jasurning boshidagi puli (kichigi). Unda Afsonada 3x boʻlgan.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Kim</th><th>Boshida</th><th>12 000 berilgandan keyin</th></tr>
  <tr><td>Jasur</td><td class="pm-word__sym">x</td><td>x + 12 000</td></tr>
  <tr><td>Afsona</td><td class="pm-word__sym">3x</td><td>3x − 12 000</td></tr>
</table></div>

<p>Oxirgi ustundagi ikki ifoda <b>teng</b> — masalaning sharti shu.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x − 12 000 = x + 12 000</span>
    <span class="pm-solve__why">Pullar teng boʻldi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x − 12 000 = 12 000</span>
    <span class="pm-solve__why">Ikki tomondan x ni ayirdik (PM-37)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x = 24 000</span>
    <span class="pm-solve__why">12 000 ni qoʻshdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 12 000 — Jasur; 3x = 36 000 — Afsona</span>
    <span class="pm-solve__why">2 ga boʻldik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Boshida: Afsona 36 000, Jasur 12 000 — 36 000 ÷ 12 000 = 3 ✓
  <br>Keyin: Afsona 36 000 − 12 000 = 24 000; Jasur 12 000 + 12 000 =
  24 000 — teng ✓
  <br><b>Javob:</b> Jasurda 12 000, Afsonada 36 000 soʻm bor edi.</p>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Jadval qachon kerak</p>
  <p>Masalada <b>ikki holat</b> (oldin/keyin) yoki <b>ikki turdagi
  narsa</b> (katta chipta / bola chiptasi, 2 000 lik / 5 000 lik
  banknot) boʻlsa — darrov jadval chizing. Jadval tuzilgandan keyin
  tenglama oʻzi koʻrinib qoladi.</p>
</div>

<h3>Matnli masala</h3>

<p>Sinf muzeyga bordi. Jami 30 kishi kirdi. Katta odam chiptasi
15 000 soʻm, bola chiptasi 6 000 soʻm turadi. Chiptalarga hammasi
bo'lib 225 000 soʻm toʻlandi.</p>

<p><b>Nechta katta odam va nechta bola borgan?</b></p>

<p><b>Reja:</b> ikki turdagi chipta bor — jadval tuzamiz. x = kattalar
soni. Unda bolalar — 30 − x.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Chipta turi</th><th>Soni</th><th>Umumiy qiymati</th></tr>
  <tr><td>Katta (15 000 soʻm)</td><td class="pm-word__sym">x</td><td>15 000x</td></tr>
  <tr><td>Bola (6 000 soʻm)</td><td class="pm-word__sym">30 − x</td><td>6 000(30 − x)</td></tr>
  <tr><td>Jami</td><td class="pm-word__sym">30</td><td>225 000</td></tr>
</table></div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">15 000x + 6 000(30 − x) = 225 000</span>
    <span class="pm-solve__why">Oxirgi ustunning yigʻindisi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">15 000x + 180 000 − 6 000x = 225 000</span>
    <span class="pm-solve__why">Qavsni ochdik (PM-33)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">9 000x + 180 000 = 225 000</span>
    <span class="pm-solve__why">15 000x − 6 000x = 9 000x</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">9 000x = 45 000</span>
    <span class="pm-solve__why">180 000 ni ayirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 5 — kattalar; 30 − 5 = 25 — bolalar</span>
    <span class="pm-solve__why">9 000 ga boʻldik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Kattalar: 5 × 15 000 = 75 000 soʻm. Bolalar: 25 × 6 000 =
  150 000 soʻm. Jami 75 000 + 150 000 = 225 000 ✓ Odamlar soni
  5 + 25 = 30 ✓
  <br><b>Javob:</b> 5 ta katta odam va 25 ta bola borgan.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Hamma bola boʻlganda 30 × 6 000 = 180 000 soʻm boʻlardi.
  Haqiqatda 45 000 soʻm koʻp toʻlangan. Har bir katta odam
  15 000 − 6 000 = 9 000 soʻm qoʻshimcha qiladi, demak kattalar
  45 000 ÷ 9 000 = 5 ta. Bir qatorda javob ✓</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">«Jasur Afsonadan 2 marta koʻp» → Jasur = x,
  Afsona = 2x</p>
  <p class="pe-fix__good">Afsona = x, Jasur = 2x</p>
  <p class="pe-fix__why">Koʻpaytiruvchi <b>koʻp</b> boʻlgan tomonga
  qoʻyiladi. Ifodalarni yozgach, ovoz chiqarib oʻqib koʻring:
  «Jasurda 2x, Afsonada x — ha, Jasurda koʻproq».</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Afsona = x, Jasur = y, Sherbek = z</p>
  <p class="pe-fix__good">Afsona = x, Jasur = 2x, Sherbek = x + 20 000</p>
  <p class="pe-fix__why">Uchta harf uchta tenglama talab qiladi.
  Bogʻlanishlar berilgan ekan, hammasini <b>bitta</b> harf orqali
  yozish kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Jami 30 kishi, kattalar x ta → bolalar =
  x − 30</p>
  <p class="pe-fix__good">bolalar = 30 − x</p>
  <p class="pe-fix__why">Ayirish tartibi teskari. Jamidan bir qismi
  ayiriladi, aksincha emas — x − 30 manfiy son berardi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">x = 40 000 topildi → «Javob: 40 000 soʻm»</p>
  <p class="pe-fix__good">Afsona 40 000, Jasur 80 000, Sherbek 60 000</p>
  <p class="pe-fix__why">Savol <b>har birining</b> ulushini soʻragan.
  x topilgach, qolgan ifodalarga qiymat qoʻyish qolgan (PM-31).</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Kitob daftardan 4 marta qimmat.» Qaysi
  birini x deb olish qulay va ikkinchisi qanday yoziladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Daftarni: daftar = x, kitob = 4x.</b> Daftar arzonroq —
    kichigi. Kitobni x desak, daftar x ÷ 4 boʻlib, kasr paydo
    boʻlardi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Sinfda 28 oʻquvchi. Qizlar q ta boʻlsa,
  oʻgʻillar nechta?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>28 − q.</b> Jamidan qizlar ayiriladi. q − 28 emas.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Ikki doʻst 90 000 soʻmni shunday boʻlishdi:
  biri ikkinchisidan 2 marta koʻp oldi. Har biri qancha oldi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>30 000 va 60 000 soʻm.</b> x + 2x = 90 000 → 3x = 90 000 →
    x = 30 000, ikkinchisi 60 000. Tekshirish: 30 000 + 60 000 =
    90 000 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Bekzodda Dilnozadan 2 marta koʻp marka bor.
  Bekzod Dilnozaga 6 ta marka bersa, ular teng boʻladi. Har birida
  nechtadan marka bor?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Dilnozada 12, Bekzodda 24.</b> Jadval: Dilnoza x → x + 6;
    Bekzod 2x → 2x − 6. Teng: 2x − 6 = x + 6 → x = 12. Tekshirish:
    24 − 6 = 18 va 12 + 6 = 18 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Qutida 2 000 soʻmlik va 5 000 soʻmlik
  banknotlar bor. Jami 24 ta banknot, umumiy summa 81 000 soʻm.
  Nechtadan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>13 ta ikki minglik, 11 ta besh minglik.</b> x — ikki
    mingliklar soni, 24 − x — besh mingliklar.
    2 000x + 5 000(24 − x) = 81 000 → 2 000x + 120 000 − 5 000x =
    81 000 → −3 000x = −39 000 → x = 13. Tekshirish: 13 × 2 000 =
    26 000, 11 × 5 000 = 55 000, jami 81 000 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Uch sonning yigʻindisi 88. Ikkinchisi
  birinchisidan 3 marta katta, uchinchisi birinchisidan 8 taga katta.
  Sonlarni toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>16, 48 va 24.</b> Hamma narsa birinchi songa qarab aytilgan,
    demak x — birinchi son. x + 3x + (x + 8) = 88 → 5x + 8 = 88 →
    5x = 80 → x = 16. Ikkinchisi 3 × 16 = 48, uchinchisi 16 + 8 = 24.
    Tekshirish: 16 + 48 + 24 = 88 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">7. Kinoteatrga 40 kishi bordi. Katta chipta
  20 000 soʻm, bola chiptasi 8 000 soʻm. Jami 464 000 soʻm toʻlandi.
  Nechta katta odam bor edi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>12 ta katta odam</b> (va 28 ta bola). x — kattalar:
    20 000x + 8 000(40 − x) = 464 000 → 20 000x + 320 000 − 8 000x =
    464 000 → 12 000x = 144 000 → x = 12. Tekshirish:
    12 × 20 000 = 240 000, 28 × 8 000 = 224 000, jami 464 000 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Nomaʼlum</b><span>x deb belgilanadigan miqdor; ingl.
    unknown</span></li>
  <li><b>Oʻzgaruvchi</b><span>har xil qiymat olishi mumkin boʻlgan harf;
    ingl. variable</span></li>
  <li><b>Ifoda</b><span>harf va sonlardan tuzilgan yozuv; ingl.
    expression</span></li>
  <li><b>Bogʻlanish</b><span>miqdorlarni bir-biriga ulovchi shart;
    ingl. relationship</span></li>
  <li><b>Jadval</b><span>maʼlumotni qator va ustunlarga joylash; ingl.
    table</span></li>
  <li><b>Holat</b><span>jadvalning bir ustuni: boshida yoki keyin;
    ingl. stage</span></li>
  <li><b>Chizmali model</b><span>miqdorlarni tasmalar bilan koʻrsatish;
    ingl. bar model</span></li>
  <li><b>Qavsni ochish</b><span>koʻpaytuvchini qavs ichiga tarqatish;
    ingl. expanding</span></li>
  <li><b>Oʻrniga qoʻyish</b><span>x ning qiymatini ifodaga qoʻyish;
    ingl. substitution</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>x deb qolganlari oʻzi orqali oʻlchanadigan miqdorni oling —
      odatda eng kichigini.</li>
    <li>Notoʻgʻri tanlov ham javobga olib boradi, lekin kasrlar
      orqali.</li>
    <li>Hamma miqdorni <b>bitta</b> harf bilan yozing; ikkinchi harf
      ikkinchi tenglama talab qiladi.</li>
    <li>«Jami n ta» boʻlsa, ikkinchi qism n − x, x − n emas.</li>
    <li>Ikki holat yoki ikki tur boʻlsa — jadval tuzing; tenglama
      jadvalning oxirgi ustunidan chiqadi.</li>
    <li>x topilgach toʻxtamang: savol nimani soʻraganini qaytib
      oʻqing.</li>
  </ul>
</div>
""",
    },
]
