# -*- coding: utf-8 -*-
"""Prime Math — Blok B, darslar 19–21 (aralash sonlar, oʻnlik kasrlar).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt

Uchta oyoq birga yoziladi:
  mashqlar — practice/management/commands/_practice_pm_19_21.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_19_21.py

⚠️ Kumulyativ:
  • PM-19 notoʻgʻri kasr va aralash sonni OCHADI — 16–18 darslardagi «javob
    doim toʻgʻri kasr» cheklovi shu darsdan boshlab tugaydi;
  • PM-19 da hali VERGULLI SON YOʻQ — oʻnlik kasr PM-20 da kiritiladi;
  • foiz PM-22 dan boshlanadi — bu uch darsda foiz yoʻq;
  • aralash son yozuvi: butun son + pm-frac (masalan 2 1/2). Yangi klass
    kiritilmagan — pm-frac inline-flex, shuning uchun butun sondan keyin
    toʻgʻri turadi.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_19_21.py --author=prime
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
    # PM-19 — aralash sonlar va notoʻgʻri kasrlar
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-19: Aralash sonlar va notoʻgʻri kasrlar",
        "category": "math",
        "order": 19,
        "summary": (
            "«Ikki yarim soat» ni qanday yozamiz? Toʻgʻri va notoʻgʻri kasr, aralash "
            "son, ular orasidagi oʻtish va aralash sonlarni qoʻshish-ayirish."
        ),
        "stories": ["Ikki yarim soat"],
        "content": """
<h2>PM-19: Aralash sonlar va notoʻgʻri kasrlar</h2>

<p>Afsona mashgʻulot jadvaliga qaradi: dushanba — <b>2 soat 30 daqiqa</b>. Buni sonda
qanday yozish kerak? «Ikki yarim» degan gap tushunarli, lekin bu <i>bitta son</i> emas,
ikkitasi: butun va kasr. Matematikada ular birga yoziladi va bunday yozuv
<b>aralash son</b> deyiladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>toʻgʻri va notoʻgʻri kasrni ajratasiz;</li>
    <li>notoʻgʻri kasrni aralash songa aylantirasiz va teskarisini qilasiz;</li>
    <li>aralash sonni son oʻqida topasiz;</li>
    <li>aralash sonlarni qoʻshasiz va ayirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uch turdagi kasr</span>
  <span class="pe-chip pe-chip--v">toʻgʻri: surat &lt; maxraj</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">notoʻgʻri: surat ≥ maxraj</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">aralash: butun + kasr</span>
</div>

<h3>1. Butundan katta kasrlar</h3>

<p>Hozirgacha kasrlarimiz butundan kichik edi: 3/4, 2/5, 1/6. Ammo hayotda butundan
kattasi ham uchraydi. Ikki yarim non — bu <b>beshta yarim</b>, yaʼni <b>5/2</b>.</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">1-non</span>
    <span class="pm-model__bar" style="width:40%">2/2</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">2-non</span>
    <span class="pm-model__bar" style="width:40%">2/2</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">3-non</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:20%">1/2</span>
  </div>
  <p class="pm-model__tot">Jami beshta yarim: 5/2 = 2 1/2</p>
</div>

<p>Bitta miqdor, ikki xil yozuv:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Notoʻgʻri kasr</p>
    <p><b>5/2</b> — surat maxrajdan katta. Hisoblashda qulay: koʻpaytirish va
    boʻlishda faqat shu koʻrinish ishlatiladi.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Aralash son</p>
    <p><b>2 1/2</b> — butun va kasr birga. Oʻqishda qulay: miqdorning kattaligi darrov
    koʻrinadi.</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">«Notoʻgʻri» degani xato degani emas</p>
  <p>7/3 mutlaqo toʻgʻri yozilgan son. Nom shunchaki shakl haqida: unda surat maxrajdan
  katta, yaʼni kasr butundan oshib ketgan. Javobni qaysi koʻrinishda yozish kerakligi
  masalaning oʻziga bogʻliq.</p>
</div>

<h3>2. Notoʻgʻri kasrdan aralash songa</h3>

<p>Bu yerda PM-4 dagi <b>qoldiqli boʻlish</b> ish beradi. Kasr — aslida boʻlish, demak
7/3 degani 7 ÷ 3 degani.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">7/3 = 7 ÷ 3</span>
    <span class="pm-solve__why">Kasr — boʻlish</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">7 ÷ 3 = 2 (qoldiq 1)</span>
    <span class="pm-solve__why">Ikkita butun chiqdi, bitta uchdan bir ortdi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">7/3 = 2 1/3</span>
    <span class="pm-solve__why">Boʻlinma — butun, qoldiq — surat, maxraj
    oʻzgarmaydi</span>
  </div>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Qoida</p>
  <p>Suratni maxrajga boʻling. <b>Boʻlinma</b> butun qism boʻladi, <b>qoldiq</b> yangi
  surat, <b>maxraj</b> esa oʻzgarmaydi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">11/4 = 2 3/4</p>
  <p class="pe-ex__uz">11 ÷ 4 = 2 (qoldiq 3). Ikkita butun va uchta chorak.</p>
</div>

<h3>3. Aralash sondan notoʻgʻri kasrga</h3>

<p>Teskari yoʻl. Butunni kasrga aylantiramiz va qoʻshamiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 2/5</span>
    <span class="pm-solve__why">Berilgan aralash son</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 = 15/5</span>
    <span class="pm-solve__why">Har bir butunda beshta beshdan bir bor: 3 × 5 = 15</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">15/5 + 2/5 = 17/5</span>
    <span class="pm-solve__why">Butun va kasr qismni qoʻshdik</span>
  </div>
</div>

<p>Qisqasi: <b>butun × maxraj + surat</b>, maxraj oʻzgarishsiz qoladi.
3 × 5 + 2 = 17, demak 17/5.</p>

<div class="pm-num">
  <div class="pm-num__track">
    <span class="pm-num__band" style="left:0%;width:68%"></span>
    <span class="pm-num__tick" style="left:0%"><i>0</i></span>
    <span class="pm-num__tick" style="left:20%"><i>1</i></span>
    <span class="pm-num__tick" style="left:40%"><i>2</i></span>
    <span class="pm-num__tick" style="left:60%"><i>3</i></span>
    <span class="pm-num__tick" style="left:80%"><i>4</i></span>
    <span class="pm-num__tick" style="left:100%"><i>5</i></span>
    <span class="pm-num__dot" style="left:68%"><i>17/5</i></span>
  </div>
</div>

<p>Son oʻqi javobni tekshirib beradi: 17/5 nuqtasi 3 bilan 4 orasida turibdi, 3 ga
yaqinroq. Aralash son 3 2/5 aynan shuni aytadi.</p>

<h3>4. Aralash sonlarni qoʻshish</h3>

<p>Ikki yoʻl bor, ikkalasi ham toʻgʻri javob beradi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">1 1/4 + 2 1/2</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">butunlar: 1 + 2 = 3</span>
    <span class="pm-solve__why">Birinchi yoʻl — qismlarni alohida qoʻshish</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">kasrlar: 1/4 + 2/4 = 3/4</span>
    <span class="pm-solve__why">Umumiy maxraj 4 (PM-17)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 3 3/4</span>
    <span class="pm-solve__why">Butun va kasrni birlashtirdik</span>
  </div>
</div>

<p>Endi qiyinrogʻi — kasr qismlar yigʻilib, butundan oshib ketsa:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2 3/4 + 1 1/2</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">butunlar: 3 &nbsp;·&nbsp; kasrlar: 3/4 + 2/4 = 5/4</span>
    <span class="pm-solve__why">Kasr qism butundan oshdi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5/4 = 1 1/4</span>
    <span class="pm-solve__why">Ortiqcha butunni ajratdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3 + 1 1/4 = 4 1/4</span>
    <span class="pm-solve__why">Ajratilgan butunni butunlarga qoʻshdik</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Ikkinchi yoʻl — hammasini notoʻgʻri kasrga</p>
  <p>2 3/4 = 11/4, 1 1/2 = 3/2 = 6/4. Keyin 11/4 + 6/4 = 17/4 = 4 1/4. Xuddi shu javob.
  Bu yoʻl uzunroq koʻrinadi, lekin <b>hech qachon adashtirmaydi</b> — ayniqsa
  ayirishda.</p>
</div>

<h3>5. Ayirish — bu yerda ehtiyot boʻling</h3>

<p>3 1/4 − 1 3/4. Kasr qismlarni ayirmoqchi boʻlsangiz, 1/4 dan 3/4 ni ayirish kerak
boʻlib qoladi — bu esa hozircha bizga notanish. Yechim: <b>ikkalasini ham notoʻgʻri
kasrga aylantiring</b>.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 1/4 = 13/4 &nbsp;·&nbsp; 1 3/4 = 7/4</span>
    <span class="pm-solve__why">3 × 4 + 1 = 13 va 1 × 4 + 3 = 7</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">13/4 − 7/4 = 6/4</span>
    <span class="pm-solve__why">Maxrajlar bir xil — suratlarni ayirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">6/4 = 3/2 = 1 1/2</span>
    <span class="pm-solve__why">Qisqartirdik va aralash songa aylantirdik</span>
  </div>
</div>

<h3>6. Matnli masala</h3>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Masala</p>
  <p>Usta ikkita taxta oldi: biri <b>1 3/4 metr</b>, ikkinchisi <b>2 1/2 metr</b>.
  Ularni uchma-uch ulab, <b>3 1/4 metr</b>lik boʻlak kesib oldi. Necha metr taxta
  qoldi?</p>
</div>

<p><b>Reja:</b> avval jami uzunlikni topamiz, keyin kesilganini ayiramiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">1 3/4 + 2 1/2</span>
    <span class="pm-solve__why">Jami uzunlik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= 3 + (3/4 + 2/4) = 3 + 5/4</span>
    <span class="pm-solve__why">Kasr qism butundan oshdi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= 4 1/4 metr</span>
    <span class="pm-solve__why">5/4 = 1 1/4, uni butunlarga qoʻshdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">4 1/4 − 3 1/4 = 1 metr</span>
    <span class="pm-solve__why">Kasr qismlar teng — faqat butunlar ayirildi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Teskari yoʻl: 3 1/4 + 1 = 4 1/4 ✓ Va notoʻgʻri kasrda: 7/4 + 5/2 = 7/4 + 10/4 =
  17/4; 17/4 − 13/4 = 4/4 = 1 ✓ Ikki xil yoʻl bir xil javob berdi.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Taxtalar taxminan ikki va ikki yarim metr — jami toʻrt metrga yaqin.
  Undan uch metrdan koʻproq kesilgan, demak bir metr atrofida qolishi kerak.
  Mos keldi.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">2 1/3 = 2 × 1/3 = 2/3</p>
  <p class="pe-fix__good">2 1/3 = 2 + 1/3 = 7/3</p>
  <p class="pe-fix__why">Aralash sonda butun bilan kasr orasida <b>qoʻshish</b> yashiringan,
  koʻpaytirish emas. Va javob 2 dan katta boʻlishi kerak edi — 2/3 esa 1 dan ham
  kichik.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">11/4 = 4 3/11</p>
  <p class="pe-fix__good">11/4 = 2 3/4</p>
  <p class="pe-fix__why">Surat maxrajga boʻlinadi, teskarisi emas. Boʻlinma 2 —
  butun qism, qoldiq 3 — yangi surat, maxraj 4 oʻzgarmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">3 1/4 − 1 3/4 = 2 2/4</p>
  <p class="pe-fix__good">3 1/4 − 1 3/4 = 1 1/2</p>
  <p class="pe-fix__why">Kasr qismlar «kattadan kichigini» deb ayirilgan: 3/4 − 1/4
  qilingan. Aslida 1/4 dan 3/4 ni ayirish kerak edi — shuning uchun notoʻgʻri kasrga
  oʻtish xavfsizroq.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 9/4 ni aralash son koʻrinishida yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>2 1/4.</b> 9 ÷ 4 = 2 (qoldiq 1).</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 1 5/6 ni notoʻgʻri kasr koʻrinishida yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>11/6.</b> 1 × 6 + 5 = 11, maxraj oʻzgarmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 8/3 son oʻqida qaysi ikki butun son orasida turadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>2 va 3 orasida.</b> 8 ÷ 3 = 2 (qoldiq 2), demak 8/3 = 2 2/3 — uchga
    yaqinroq.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 2 1/2 + 1 3/4 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>4 1/4.</b> Butunlar 3, kasrlar 2/4 + 3/4 = 5/4 = 1 1/4. Jami 3 + 1 1/4.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Buvijon ertalab 2 1/4 kg un, kechqurun 1 1/2 kg un ishlatdi.
  Jami qancha un ketdi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3 3/4 kg.</b> Butunlar: 2 + 1 = 3. Kasrlar: 1/4 + 2/4 = 3/4. Bu safar kasr
    qism butundan oshmadi, shuning uchun qoʻshimcha qadam kerak emas.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Toʻgʻri kasr</b><span>surati maxrajidan kichik kasr; ingl. proper
    fraction</span></li>
  <li><b>Notoʻgʻri kasr</b><span>surati maxrajidan katta yoki unga teng kasr;
    ingl. improper fraction</span></li>
  <li><b>Aralash son</b><span>butun son va kasr birga yozilgan son; ingl. mixed
    number</span></li>
  <li><b>Butun qism</b><span>aralash sondagi butun son; ingl. whole part</span></li>
  <li><b>Kasr qism</b><span>aralash sondagi kasr; ingl. fractional part</span></li>
  <li><b>Qoldiq</b><span>boʻlishdan ortib qolgan son; ingl. remainder</span></li>
  <li><b>Boʻlinma</b><span>boʻlish natijasi; ingl. quotient</span></li>
  <li><b>Son oʻqi</b><span>sonlar tartib bilan joylashgan chiziq; ingl. number
    line</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Notoʻgʻri kasr → aralash son:</b> suratni maxrajga boʻling; boʻlinma —
      butun, qoldiq — yangi surat.</li>
    <li><b>Aralash son → notoʻgʻri kasr:</b> butun × maxraj + surat.</li>
    <li><b>Ayirishda notoʻgʻri kasrga oʻting</b> — bu yoʻl hech qachon
      adashtirmaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-20 — oʻnlik kasrlar
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-20: Oʻnlik kasrlar — razryadning davomi",
        "category": "math",
        "order": 20,
        "summary": (
            "Tarozida 1,250 kg yozilgan — bu qancha? Vergul, vergul ortidagi "
            "razryadlar, oʻnlik kasrni oddiy kasrga aylantirish va toʻgʻri taqqoslash."
        ),
        "stories": ["Tarozidagi raqamlar"],
        "content": """
<h2>PM-20: Oʻnlik kasrlar — razryadning davomi</h2>

<p>Bozorda tarozi ekranida <b>1,250</b> yozuvi paydo boʻldi. Sherbek oʻyladi: bu bir
kilo ikki yuz ellik grammmi, yoki bir kilo ikki yuz ellik <i>kilogrammmi</i>? Vergul
qayerdan chiqdi va u nimani anglatadi? Bugungi dars aynan shu belgi haqida.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>vergul nimani ajratishini bilasiz;</li>
    <li>vergul ortidagi razryadlarni nomlaysiz: oʻndan bir, yuzdan bir, mingdan bir;</li>
    <li>oʻnlik kasrni oddiy kasrga va teskarisiga aylantirasiz;</li>
    <li>oʻnlik kasrlarni toʻgʻri taqqoslaysiz — bu yerda eng koʻp xato qilinadi.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Vergul nimani ajratadi</span>
  <span class="pe-chip pe-chip--o">butun qism</span>
  <span class="pe-op">,</span>
  <span class="pe-chip pe-chip--v">butundan kichik qism</span>
</div>

<h3>1. Razryad oʻngga davom etadi</h3>

<p>PM-1 da razryadlarni oʻrgangan edik: birlik, oʻnlik, yuzlik. Ular chapga qarab
<b>oʻn barobar oshib</b> boradi. Endi teskari tomonga yuramiz — oʻngga qarab har
razryad oʻn barobar <b>kichrayadi</b>.</p>

<div class="pe-table-wrap"><table>
  <tr><th>Razryad</th><th>Qiymati</th><th>Kasr koʻrinishi</th></tr>
  <tr><td>yuzlik</td><td>100</td><td>—</td></tr>
  <tr><td>oʻnlik</td><td>10</td><td>—</td></tr>
  <tr><td>birlik</td><td>1</td><td>—</td></tr>
  <tr><td><b>vergul</b></td><td colspan="2">bu yerdan butundan kichik qism boshlanadi</td></tr>
  <tr><td>oʻndan bir</td><td>0,1</td><td>1/10</td></tr>
  <tr><td>yuzdan bir</td><td>0,01</td><td>1/100</td></tr>
  <tr><td>mingdan bir</td><td>0,001</td><td>1/1000</td></tr>
</table></div>

<p>Demak vergul yangi narsa emas — u razryadlar zanjirining <b>davomi</b>. Faqat
qayerda butun tugab, boʻlaklar boshlanishini koʻrsatib turadi.</p>

<div class="pe-ex">
  <p class="pe-ex__math">3,45 = 3 butun + 4 ta oʻndan bir + 5 ta yuzdan bir</p>
  <p class="pe-ex__uz">Oʻqilishi: «uch butun qirq besh yuzdan bir».</p>
</div>

<h3>2. Oʻnlik kasrdan oddiy kasrga</h3>

<p>Bu juda oson: <b>vergul ortida nechta raqam boʻlsa, maxrajda shuncha nol</b>.</p>

<div class="pe-table-wrap"><table>
  <tr><th>Oʻnlik</th><th>Vergul ortida</th><th>Kasr</th><th>Qisqarganda</th></tr>
  <tr><td>0,7</td><td>1 ta raqam</td><td>7/10</td><td>7/10</td></tr>
  <tr><td>0,25</td><td>2 ta raqam</td><td>25/100</td><td>1/4</td></tr>
  <tr><td>0,08</td><td>2 ta raqam</td><td>8/100</td><td>2/25</td></tr>
  <tr><td>2,5</td><td>1 ta raqam</td><td>2 5/10</td><td>2 1/2</td></tr>
</table></div>

<p>Teskari yoʻl ham shunday ishlaydi. 3/10 — maxrajda bitta nol, demak vergul ortida
bitta raqam: <b>0,3</b>. 7/100 esa <b>0,07</b> — ikkita raqam kerak, shuning uchun
oldiga nol qoʻyildi.</p>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Nol tashlab ketilmaydi</p>
  <p>7/100 = <b>0,07</b>, 0,7 emas! Yuzdan bir razryadiga yetish uchun oʻndan bir
  oʻrni band boʻlishi kerak — u yerga nol yoziladi. 0,7 esa 70/100 boʻlib qolardi,
  yaʼni oʻn barobar katta son.</p>
</div>

<h3>3. Oxirgi nollar hech narsani oʻzgartirmaydi</h3>

<p>Endi Sherbekning tarozisiga qaytamiz. <b>1,250</b> va <b>1,25</b> — bir xil sonmi?
Ha, bir xil.</p>

<div class="pe-ex">
  <p class="pe-ex__math">1,25 = 1,250 = 1,2500</p>
  <p class="pe-ex__uz">Oxiriga qoʻshilgan nol hech narsa qoʻshmaydi: 25/100 =
  250/1000.</p>
  <p class="pe-ex__why">Bu PM-16 dagi kasrning asosiy xossasi — surat va maxrajni
  10 ga koʻpaytirdik, xolos.</p>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Lekin diqqat</p>
  <p>Nolni <b>oxiriga</b> qoʻshish mumkin, <b>oʻrtasiga</b> yoki <b>boshiga</b> emas.
  1,25 · 1,205 · 1,025 — bular uchta boshqa-boshqa son.</p>
</div>

<h3>4. Taqqoslash — bu yerda eng koʻp xato qilinadi</h3>

<p>Qaysi biri katta: <b>0,9</b> yoki <b>0,45</b>? Koʻpchilik 0,45 deydi, chunki 45 soni
9 dan katta. Bu <b>notoʻgʻri</b>.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">0,9 va 0,45</span>
    <span class="pm-solve__why">Raqamlar soni har xil — solishtirish qiyin</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">0,9 = 0,90</span>
    <span class="pm-solve__why">Oxiriga nol qoʻshdik — son oʻzgarmadi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">0,90 &gt; 0,45</span>
    <span class="pm-solve__why">Endi ikkalasi ham yuzdan bir: 90 &gt; 45</span>
  </div>
</div>

<div class="pm-num">
  <div class="pm-num__track">
    <span class="pm-num__band" style="left:0%;width:90%"></span>
    <span class="pm-num__tick" style="left:0%"><i>0</i></span>
    <span class="pm-num__tick" style="left:45%"><i>0,45</i></span>
    <span class="pm-num__tick" style="left:90%"><i>0,9</i></span>
    <span class="pm-num__tick" style="left:100%"><i>1</i></span>
  </div>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Taqqoslash tartibi</p>
  <p>1. Avval <b>butun qism</b>ni solishtiring. Katta boʻlsa — tamom.<br>
  2. Butunlar teng boʻlsa, <b>oʻndan bir</b>ga qarang, keyin <b>yuzdan bir</b>ga —
  razryadma-razryad, chapdan oʻngga.<br>
  3. Kerak boʻlsa oxiriga nol qoʻshib, raqamlar sonini tenglashtiring.</p>
  <p><b>Uzunroq son katta degani emas:</b> 0,9 soni 0,45 dan katta.</p>
</div>

<h3>5. Matnli masala</h3>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Masala</p>
  <p>Uch xaltaning ogʻirligi: birinchisi <b>2,5 kg</b>, ikkinchisi <b>2,45 kg</b>,
  uchinchisi <b>2,405 kg</b>. Ularni ogʻirligi boʻyicha oʻsish tartibida joylashtiring
  va eng ogʻiri bilan eng yengili orasidagi farqni ayting.</p>
</div>

<p><b>Reja:</b> avval hammasini bir xil razryadgacha keltiramiz — mingdan birgacha.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2,5 = 2,500</span>
    <span class="pm-solve__why">Oxiriga ikkita nol qoʻshdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2,45 = 2,450</span>
    <span class="pm-solve__why">Bitta nol qoʻshdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2,405 — oʻzgarishsiz</span>
    <span class="pm-solve__why">Endi uchalasi ham mingdan bir razryadida</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2,405 &lt; 2,450 &lt; 2,500</span>
    <span class="pm-solve__why">405 &lt; 450 &lt; 500 — oʻsish tartibi shu</span>
  </div>
</div>

<p>Eng ogʻiri 2,5 kg, eng yengili 2,405 kg. Farq: <b>2,500 − 2,405 = 0,095 kg</b>,
yaʼni 95 gramm.</p>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Grammga oʻtkazamiz: 2 500 g, 2 450 g va 2 405 g. Tartib oʻsha ✓ Farq
  2 500 − 2 405 = 95 g ✓ Kilogrammda 0,095 kg — bir xil.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Foydali hiyla</p>
  <p>Oʻnlik kasrlar chalkashtirsa, ularni <b>mayda birlikka</b> oʻtkazing: kilogrammni
  grammga, metrni santimetrga, soʻmni tiyinga. Butun sonlar bilan ishlash har doim
  osonroq, javobni esa oxirida qaytarasiz.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">0,45 &gt; 0,9</p>
  <p class="pe-fix__good">0,45 &lt; 0,9</p>
  <p class="pe-fix__why">Butun sonlardagi «uzunroq — kattaroq» qoidasi bu yerda
  ishlamaydi. 0,9 = 0,90, va 90 soni 45 dan katta.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">7/100 = 0,7</p>
  <p class="pe-fix__good">7/100 = 0,07</p>
  <p class="pe-fix__why">Maxrajda ikkita nol bor, demak vergul ortida ikkita raqam
  boʻlishi kerak. Oʻndan bir oʻrni boʻsh — u yerga nol yoziladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">0,5 = 1/5</p>
  <p class="pe-fix__good">0,5 = 5/10 = 1/2</p>
  <p class="pe-fix__why">Vergul ortidagi raqam <b>surat</b> boʻladi, maxraj emas.
  Maxrajni nollar soni belgilaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 0,3 ni oddiy kasr koʻrinishida yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3/10.</b> Vergul ortida bitta raqam — maxrajda bitta nol.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 9/100 ni oʻnlik kasr koʻrinishida yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>0,09.</b> Maxrajda ikkita nol — vergul ortida ikkita raqam kerak, shuning
    uchun 9 dan oldin nol turadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 1,2 va 1,15 dan qaysi biri katta?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>1,2.</b> Butunlar teng. 1,2 = 1,20, va 20 &gt; 15.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 12,05 sonida 5 raqami qaysi razryadda turibdi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Yuzdan bir razryadida.</b> Verguldan keyingi birinchi oʻrin — oʻndan bir
    (u yerda 0 turibdi), ikkinchisi — yuzdan bir.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Bir doʻkonda olma 12 500 soʻm, ikkinchisida 12,5 ming soʻm.
  Qaysi biri arzon?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Narxlar teng.</b> 12,5 ming soʻm — bu 12 ming va yana yarim ming, yaʼni
    12 500 soʻm. Vergul bu yerda ming soʻmning boʻlagini koʻrsatyapti.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Oʻnlik kasr</b><span>vergul bilan yoziladigan kasr; ingl. decimal
    fraction</span></li>
  <li><b>Vergul</b><span>butun qismni kasr qismdan ajratuvchi belgi; ingl. decimal
    point</span></li>
  <li><b>Oʻndan bir</b><span>verguldan keyingi birinchi razryad, 0,1; ingl.
    tenth</span></li>
  <li><b>Yuzdan bir</b><span>verguldan keyingi ikkinchi razryad, 0,01; ingl.
    hundredth</span></li>
  <li><b>Mingdan bir</b><span>verguldan keyingi uchinchi razryad, 0,001; ingl.
    thousandth</span></li>
  <li><b>Butun qism</b><span>verguldan chapdagi son; ingl. whole part</span></li>
  <li><b>Kasr qism</b><span>verguldan oʻngdagi raqamlar; ingl. decimal part</span></li>
  <li><b>Razryad</b><span>raqamning sondagi oʻrni; ingl. place value</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Vergul — razryadlarning davomi:</b> oʻngga qarab har razryad oʻn barobar
      kichrayadi.</li>
    <li><b>Vergul ortida nechta raqam boʻlsa, maxrajda shuncha nol:</b>
      0,07 = 7/100.</li>
    <li><b>Uzunroq son katta emas.</b> Taqqoslashdan oldin oxiriga nol qoʻshib,
      razryadlarni tenglashtiring: 0,9 = 0,90 &gt; 0,45.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-21 — oʻnlik kasrlar bilan toʻrt amal
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-21: Oʻnlik kasrlar bilan toʻrt amal",
        "category": "math",
        "order": 21,
        "summary": (
            "Vergulni qayerga qoʻyish kerak? Ustunda qoʻshish va ayirish, "
            "koʻpaytirishda xonalarni sanash, boʻlishda vergulni surish."
        ),
        "stories": ["Benzin va yoʻl"],
        "content": """
<h2>PM-21: Oʻnlik kasrlar bilan toʻrt amal</h2>

<p>Samarqandga yoʻl — <b>300 km</b>. Mashina har yuz kilometrda <b>9,5 litr</b> benzin
yeydi, benzinning litri esa <b>8 400 soʻm</b>. Yoʻlga qancha pul ketadi? Bu savolga
javob berish uchun oʻnlik kasrlar bilan koʻpaytirish kerak — va butun qiyinchilik
bitta belgida: <b>vergul qayerda turadi?</b></p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>oʻnlik kasrlarni ustunda qoʻshasiz va ayirasiz;</li>
    <li>koʻpaytirishda vergul oʻrnini xonalarni sanab topasiz;</li>
    <li>oʻnlik kasrga boʻlishni butun songa boʻlishga aylantirasiz;</li>
    <li>10, 100, 1000 ga koʻpaytirish va boʻlishni bir soniyada bajarasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uch amal — uch qoida</span>
  <span class="pe-chip pe-chip--v">+ va −: vergulni vergul ostiga</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">×: xonalarni sanang</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">÷: vergulni suring</span>
</div>

<h3>1. Qoʻshish va ayirish — vergul vergul ostida</h3>

<p>Bu yerda qoida bitta va u qatʼiy: <b>vergullar bir ustunda turishi kerak</b>.
Shunda razryadlar ham oʻz-oʻzidan mos keladi.</p>

<div class="pe-table-wrap"><table class="pm-col">
  <tr><td></td><td>2</td><td>,</td><td>4</td><td>5</td></tr>
  <tr class="pm-col__op"><td>+</td><td>1</td><td>,</td><td>3</td><td>0</td></tr>
  <tr class="pm-col__res"><td></td><td>3</td><td>,</td><td>7</td><td>5</td></tr>
</table></div>

<p>Diqqat qiling: 1,3 ni <b>1,30</b> deb yozdik. Oxirgi nol sonni oʻzgartirmaydi
(PM-20), lekin ustunni tekislaydi va xatoning oldini oladi.</p>

<div class="pe-ex">
  <p class="pe-ex__math">6 − 1,4 = 6,0 − 1,4 = 4,6</p>
  <p class="pe-ex__uz">Butun sonni ham vergul bilan yozish mumkin: 6 = 6,0.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Eng koʻp uchraydigan xato</p>
  <p>Sonlarni <b>oʻng chetidan</b> tekislash — butun sonlardagi odat. 2,5 + 1,25 ni
  shunday yozsangiz, birlik yuzdan bir ustiga tushib qoladi va javob butunlay
  buziladi. Tekislash faqat <b>vergul boʻyicha</b>.</p>
</div>

<h3>2. Koʻpaytirish — xonalarni sanang</h3>

<p>Koʻpaytirishda vergulni tekislash <b>shart emas</b>. Aksincha: avval vergulni
umuman unutamiz.</p>

<div class="pe-steps">
  <ol>
    <li>Vergullarni eʼtiborsiz qoldirib, sonlarni <b>butun son kabi</b>
      koʻpaytiring.</li>
    <li>Ikkala koʻpaytuvchida vergul ortidagi raqamlarni <b>jami sanang</b>.</li>
    <li>Javobda oʻng chetdan shuncha raqam sanab, vergulni qoʻying.</li>
  </ol>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">0,2 × 0,3</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2 × 3 = 6</span>
    <span class="pm-solve__why">Vergulsiz koʻpaytirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">1 + 1 = 2 ta xona</span>
    <span class="pm-solve__why">Har bir sonda vergul ortida bittadan raqam bor</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">0,2 × 0,3 = 0,06</span>
    <span class="pm-solve__why">Oʻng chetdan ikkita raqam sanab vergul qoʻydik</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Nega ikkita xona?</p>
  <p>0,2 = 2/10 va 0,3 = 3/10. Ularni koʻpaytirsak 6/100 chiqadi — maxrajda ikkita
  nol, demak vergul ortida ikkita raqam. Xona sanash — aslida maxrajlarni
  koʻpaytirish.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">1,2 × 5 = 6</p>
  <p class="pe-ex__uz">12 × 5 = 60, bitta xona: 6,0 — yaʼni 6.</p>
</div>

<h3>3. 10, 100, 1000 — vergul yuradi</h3>

<p>Oʻnning darajalariga koʻpaytirish yoki boʻlish uchun hech narsa hisoblash shart
emas: vergulning oʻzi joyini oʻzgartiradi.</p>

<div class="pe-table-wrap"><table>
  <tr><th>Amal</th><th>Vergul qayerga</th><th>Misol</th></tr>
  <tr><td>× 10</td><td>1 oʻrin oʻngga</td><td>4,7 → 47</td></tr>
  <tr><td>× 100</td><td>2 oʻrin oʻngga</td><td>4,7 → 470</td></tr>
  <tr><td>÷ 10</td><td>1 oʻrin chapga</td><td>23,5 → 2,35</td></tr>
  <tr><td>÷ 100</td><td>2 oʻrin chapga</td><td>23,5 → 0,235</td></tr>
</table></div>

<p>Mantiqi oddiy: son oʻn barobar oshsa, har bir raqam bitta razryadga chapga
siljiydi. Buni yozuvda koʻrsatishning eng qisqa yoʻli — vergulni siljitish.</p>

<h3>4. Boʻlish</h3>

<p><b>Butun songa boʻlish</b> oddiy: odatdagidek boʻlaverasiz, vergulni esa
oʻz oʻrnida qoldirasiz.</p>

<div class="pe-ex">
  <p class="pe-ex__math">7,5 ÷ 5 = 1,5</p>
  <p class="pe-ex__uz">75 ÷ 5 = 15, bitta xona qoladi — 1,5.</p>
</div>

<p><b>Oʻnlik kasrga boʻlish</b> esa bir hiyla talab qiladi. Boʻluvchi butun son
boʻlishi kerak, shuning uchun <b>ikkala sonning ham vergulini birga suramiz</b>.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3,6 ÷ 0,4</span>
    <span class="pm-solve__why">Boʻluvchi kasr — noqulay</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= 36 ÷ 4</span>
    <span class="pm-solve__why">Ikkalasini 10 ga koʻpaytirdik: vergul bir oʻrin
    oʻngga</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 9</span>
    <span class="pm-solve__why">Endi oddiy boʻlish</span>
  </div>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Nega javob oʻzgarmaydi</p>
  <p>Boʻlinuvchi va boʻluvchini <b>bir xil songa</b> koʻpaytirsangiz, boʻlinma
  oʻzgarmaydi — bu PM-16 dagi kasrning asosiy xossasi. 3,6/0,4 = 36/4 — bitta
  kasrning ikki xil yozuvi.</p>
</div>

<h3>5. Matnli masala</h3>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Masala</p>
  <p>Samarqandgacha <b>300 km</b>. Mashina har <b>100 km</b> da <b>9,5 litr</b> benzin
  sarflaydi. Benzinning bir litri <b>8 400 soʻm</b>. Yoʻlga qancha pul ketadi?</p>
</div>

<p><b>Reja:</b> avval necha yuz kilometr ekanini topamiz, keyin benzin miqdorini,
oxirida narxni.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">300 ÷ 100 = 3</span>
    <span class="pm-solve__why">Uchta yuz kilometr</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 × 9,5 = 28,5 litr</span>
    <span class="pm-solve__why">95 × 3 = 285, bitta xona — 28,5</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">28,5 × 8 400 = 239 400 soʻm</span>
    <span class="pm-solve__why">285 × 84 = 23 940; nollar va xona hisobga
    olinganda 239 400</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Boshqa yoʻl: 28,5 = 28 + 0,5. 28 × 8 400 = 235 200 va 0,5 × 8 400 = 4 200.
  Yigʻindisi 235 200 + 4 200 = <b>239 400</b> ✓</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Taxminan 30 litr, litri taxminan 8 000 soʻm — demak 240 000 soʻm atrofida.
  Javob shu yerda, razryadda xato yoʻq.</span>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Qaytish yoʻli ham bor</p>
  <p>Agar borib-kelish soʻralganda, yoʻl 600 km boʻlardi: 6 × 9,5 = 57 litr,
  57 × 8 400 = 478 800 soʻm. Masalada nima soʻralganini har doim ikki marta
  oʻqing.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">2,5 + 1,25 = 1,50 (oʻng chetdan tekisladim)</p>
  <p class="pe-fix__good">2,5 + 1,25 = 2,50 + 1,25 = 3,75</p>
  <p class="pe-fix__why">Tekislash vergul boʻyicha boʻladi, oxirgi raqam boʻyicha
  emas. Va tez tekshiruv: yigʻindi 2,5 dan katta boʻlishi shart edi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">0,2 × 0,3 = 0,6</p>
  <p class="pe-fix__good">0,2 × 0,3 = 0,06</p>
  <p class="pe-fix__why">Xonalar qoʻshiladi: 1 + 1 = 2. Va mantiq: 0,3 birdan kichik,
  demak natija 0,2 dan <b>kichik</b> boʻlishi kerak (PM-18).</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">3,6 ÷ 0,4 = 0,9</p>
  <p class="pe-fix__good">3,6 ÷ 0,4 = 9</p>
  <p class="pe-fix__why">Faqat bitta sonning verguli surilgan. Ikkalasini ham
  10 ga koʻpaytirish kerak: 36 ÷ 4 = 9.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 1,5 + 2,3 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3,8.</b> Vergul vergul ostida: butunlar 1 + 2 = 3, oʻndan birlar
    5 + 3 = 8.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 5,7 − 2,4 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3,3.</b> 57 − 24 = 33, bitta xona.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 0,4 × 0,5 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>0,2.</b> 4 × 5 = 20, ikkita xona — 0,20, yaʼni 0,2. Oxirgi nol tashlab
    yuboriladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 23,5 ÷ 10 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>2,35.</b> Vergul bir oʻrin chapga suriladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Sherbek bozordan 2,4 kg olma oldi. Bir kilogrammi
  15 000 soʻm. U qancha toʻladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>36 000 soʻm.</b> 24 × 15 = 360, bitta xona: 36,0 — yaʼni 36 ming soʻm.
    Taxmin bilan tekshiring: 2,4 taxminan 2,5, 2,5 × 15 000 = 37 500 — javob shu
    atrofda.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Oʻnlik kasr</b><span>vergul bilan yoziladigan kasr; ingl. decimal</span></li>
  <li><b>Oʻnlik xona</b><span>verguldan keyingi raqam oʻrni; ingl. decimal
    place</span></li>
  <li><b>Boʻlinuvchi</b><span>boʻlinayotgan son; ingl. dividend</span></li>
  <li><b>Boʻluvchi</b><span>nechaga boʻlinayotganini bildiruvchi son;
    ingl. divisor</span></li>
  <li><b>Boʻlinma</b><span>boʻlish natijasi; ingl. quotient</span></li>
  <li><b>Koʻpaytma</b><span>koʻpaytirish natijasi; ingl. product</span></li>
  <li><b>Ustunda hisoblash</b><span>razryadlarni bir ustunga tizib hisoblash;
    ingl. column arithmetic</span></li>
  <li><b>Taxmin</b><span>javobning kattaligini oldindan baholash;
    ingl. estimation</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Qoʻshish-ayirishda vergul vergul ostida turadi</b> — kerak boʻlsa oxiriga
      nol qoʻshing.</li>
    <li><b>Koʻpaytirishda xonalar qoʻshiladi:</b> 0,2 × 0,3 da 1 + 1 = 2 xona,
      javob 0,06.</li>
    <li><b>Kasrga boʻlishda ikkala sonning vergulini birga suring:</b>
      3,6 ÷ 0,4 = 36 ÷ 4 = 9.</li>
  </ul>
</div>
""",
    },
]
