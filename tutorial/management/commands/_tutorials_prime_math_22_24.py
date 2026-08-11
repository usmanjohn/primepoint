# -*- coding: utf-8 -*-
"""Prime Math — Blok B, darslar 22–24 (foizning uch qiyofasi va ikki teskari savol).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt

Uchta oyoq birga yoziladi:
  mashqlar — practice/management/commands/_practice_pm_22_24.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_22_24.py

⚠️ Kumulyativ:
  • PM-22 FOIZNI OCHADI — undan oldingi darslarda foiz umuman ishlatilmagan;
  • oʻnlik kasr (PM-20) va oʻnlik kasrlar bilan amallar (PM-21) shu yerda
    toʻliq ishlatiladi — foiz aslida oʻnlik kasrning boshqa nomi;
  • PM-23 faqat «sonning p foizi» ni beradi; «necha foiz?» va «foizdan butun»
    PM-24 da;
  • foiz OʻZGARISHI (oshdi/kamaydi) PM-25 da, chegirma-ustama-soliq PM-26 da —
    bu uch darsda ular yoʻq. PM-24 dagi chegirma faqat «narxning p foizi»
    darajasida, yangi narxni topish qoidasisiz.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_22_24.py --author=prime
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
    # PM-22 — kasr ↔ oʻnlik ↔ foiz
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-22: Kasr ↔ oʻnlik ↔ foiz: bitta sonning uch qiyofasi",
        "category": "math",
        "order": 22,
        "summary": (
            "1/2, 0,5 va 50% — bitta sonning uchta yozuvi. Kasrni oʻnlikka, oʻnlikni "
            "foizga, foizni kasrga aylantirish va turli koʻrinishdagi sonlarni "
            "taqqoslash."
        ),
        "stories": ["Bitta son, uch xil libos"],
        "content": """
<h2>PM-22: Kasr ↔ oʻnlik ↔ foiz: bitta sonning uch qiyofasi</h2>

<p>Sherbek doʻkonda uchta yozuvni koʻrdi. Birinchi vitrinada «<b>1/2 narxda</b>», ikkinchisida
«<b>0,5 koeffitsient</b>», uchinchisida «<b>50% chegirma</b>». U uzoq oʻyladi: qaysi biri
foydaliroq ekan? Javob kulgili — uchalasi ham <i>bitta xil</i> son. Faqat kiyimi boshqa.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>foiz nima ekanini va nega u aynan yuzga bogʻlanganini bilasiz;</li>
    <li>kasrni oʻnlik kasrga, oʻnlikni foizga aylantirasiz;</li>
    <li>foizni oʻnlik kasrga va oddiy kasrga qaytarasiz;</li>
    <li>har xil koʻrinishdagi sonlarni bir-biri bilan taqqoslay olasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uch qiyofa, bitta son</span>
  <span class="pe-chip pe-chip--o">kasr → oʻnlik: surat ÷ maxraj</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">oʻnlik → foiz: × 100</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">foiz → oʻnlik: ÷ 100</span>
</div>

<h3>1. Foiz — bu yuzdan boʻlak</h3>

<p>Kasr butunni istalgan sondagi boʻlakka boʻlishi mumkin: uchdan bir, sakkizdan besh,
oʻn ettidan toʻqqiz. Bu erkinlik qulay, lekin taqqoslashda halaqit beradi. 5/8 katta yoki
7/11 mi? Darrov aytolmaysiz.</p>

<p>Shuning uchun odamlar bitta maxrajni tanlab olishdi — <b>100</b>. Butunni doim yuzta teng
boʻlakka boʻlamiz va nechtasi kerakligini aytamiz. Shu <b>yuzdan boʻlak</b>ning nomi —
<b>foiz</b>, belgisi <b>%</b>.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 220 245" role="img" aria-label="Yuz katakli kvadrat, yigirma besh katagi boʻyalgan">
    <rect class="pm-fill--hl" x="10" y="10" width="200" height="50"/>
    <rect class="pm-ln" x="10" y="10" width="200" height="200" fill="none"/>
    <line class="pm-ln pm-ln--dash" x1="30"  y1="10" x2="30"  y2="210"/>
    <line class="pm-ln pm-ln--dash" x1="50"  y1="10" x2="50"  y2="210"/>
    <line class="pm-ln pm-ln--dash" x1="70"  y1="10" x2="70"  y2="210"/>
    <line class="pm-ln pm-ln--dash" x1="90"  y1="10" x2="90"  y2="210"/>
    <line class="pm-ln pm-ln--dash" x1="110" y1="10" x2="110" y2="210"/>
    <line class="pm-ln pm-ln--dash" x1="130" y1="10" x2="130" y2="210"/>
    <line class="pm-ln pm-ln--dash" x1="150" y1="10" x2="150" y2="210"/>
    <line class="pm-ln pm-ln--dash" x1="170" y1="10" x2="170" y2="210"/>
    <line class="pm-ln pm-ln--dash" x1="190" y1="10" x2="190" y2="210"/>
    <line class="pm-ln pm-ln--dash" x1="10" y1="30"  x2="210" y2="30"/>
    <line class="pm-ln pm-ln--dash" x1="10" y1="50"  x2="210" y2="50"/>
    <line class="pm-ln pm-ln--dash" x1="10" y1="70"  x2="210" y2="70"/>
    <line class="pm-ln pm-ln--dash" x1="10" y1="90"  x2="210" y2="90"/>
    <line class="pm-ln pm-ln--dash" x1="10" y1="110" x2="210" y2="110"/>
    <line class="pm-ln pm-ln--dash" x1="10" y1="130" x2="210" y2="130"/>
    <line class="pm-ln pm-ln--dash" x1="10" y1="150" x2="210" y2="150"/>
    <line class="pm-ln pm-ln--dash" x1="10" y1="170" x2="210" y2="170"/>
    <line class="pm-ln pm-ln--dash" x1="10" y1="190" x2="210" y2="190"/>
    <text class="pm-lbl pm-lbl--hl" x="110" y="235" text-anchor="middle">25 katak = 25/100 = 0,25 = 25%</text>
  </svg>
  <figcaption>Butun — yuzta katak. Boʻyalgani yigirma beshta: butunning choragi.</figcaption>
</figure>

<p>Yuzta katakning yigirma beshtasi boʻyaldi. Buni toʻrt xil aytish mumkin va toʻrtalasi
ham toʻgʻri: «yigirma besh katak», «25/100», «0,25», «25 foiz».</p>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Foiz — son emas, ulush</p>
  <p>«25%» oʻzicha hech nimani anglatmaydi: <b>nimaning</b> 25 foizi? Foiz doim biror
  butunga tegishli. 25% ta olma degan gap yoʻq — 40 ta olmaning 25 foizi bor, u 10 ta olma.
  Shuning uchun foizni koʻrsangiz, birinchi savol doim bitta: <b>butun nima?</b></p>
</div>

<h3>2. Uchta koʻrinish yonma-yon</h3>

<p>Eng koʻp uchraydigan sonlarni yodda saqlash arziydi — ular kundalik hisobda har kuni
kerak boʻladi.</p>

<div class="pe-table-wrap"><table>
  <tr><th>Kasr</th><th>Oʻnlik kasr</th><th>Foiz</th><th>Qayerda uchraydi</th></tr>
  <tr><td>1/2</td><td>0,5</td><td>50%</td><td>yarim narx, yarim yoʻl</td></tr>
  <tr><td>1/4</td><td>0,25</td><td>25%</td><td>chorak soat, chorak non</td></tr>
  <tr><td>3/4</td><td>0,75</td><td>75%</td><td>uch chorak, 45 daqiqa</td></tr>
  <tr><td>1/5</td><td>0,2</td><td>20%</td><td>beshdan bir, choyxona ustamasi</td></tr>
  <tr><td>1/10</td><td>0,1</td><td>10%</td><td>eng oson foiz</td></tr>
  <tr><td>1/100</td><td>0,01</td><td>1%</td><td>foizning oʻzi</td></tr>
  <tr><td>1</td><td>1,0</td><td>100%</td><td>butunning hammasi</td></tr>
</table></div>

<p>Jadvalning oxirgi qatoriga eʼtibor bering. <b>100% — butunning oʻzi</b>, yaʼni 1. Demak
100% dan katta foiz ham boʻladi: 150% — bir butun va yana yarim. Bu gʻalati emas, buni
kundalik hayotda ham koʻrasiz: «narx 200% ga oshdi» degani narx uch baravar boʻldi.</p>

<h3>3. Kasrdan oʻnlikka: shunchaki boʻlish</h3>

<p>PM-15 da koʻrgan edik: kasr chizigʻi — boʻlish belgisi. Shuning uchun kasrni oʻnlik
kasrga aylantirish uchun hech qanday yangi qoida kerak emas — suratni maxrajga boʻlamiz
(PM-21 dagi vergulni surib boʻlish).</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3/8 = 3 ÷ 8</span>
    <span class="pm-solve__why">Kasr chizigʻi — boʻlish belgisi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3,000 ÷ 8</span>
    <span class="pm-solve__why">3 ni 3,000 deb yozdik — nol qoʻshsak qiymat oʻzgarmaydi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">30 ÷ 8 = 3 (qoldiq 6) → 0,3…</span>
    <span class="pm-solve__why">Birinchi oʻnlik razryad</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">60 ÷ 8 = 7 (qoldiq 4) → 0,37…</span>
    <span class="pm-solve__why">Ikkinchi razryad</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">40 ÷ 8 = 5 → 3/8 = 0,375</span>
    <span class="pm-solve__why">Qoldiq nolga aylandi — boʻlish tugadi</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Qulay yoʻl: maxrajni 10, 100 yoki 1000 ga keltiring</p>
  <p>Agar maxrajni butun songa koʻpaytirib 100 qilish mumkin boʻlsa, boʻlishning umuman
  keragi yoʻq: 7/20 = 35/100 = 0,35 (surat va maxrajni 5 ga koʻpaytirdik), 3/5 = 6/10 = 0,6,
  17/25 = 68/100 = 0,68. Bu PM-16 dagi teng kasrlar qoidasining oʻzi.</p>
</div>

<h3>4. Oʻnlikdan foizga: yuzga koʻpaytirish</h3>

<p>Foiz — yuzdan boʻlak. Demak oʻnlik kasrda nechta yuzdan boʻlak borligini bilish uchun
uni <b>100 ga koʻpaytiramiz</b>. PM-21 dan bilamiz: 100 ga koʻpaytirish — vergulni ikki xona
<b>oʻngga</b> surish.</p>

<div class="pe-ex">
  <p class="pe-ex__math">0,375 × 100 = 37,5 → 37,5%</p>
  <p class="pe-ex__uz">Uch sakkizdan boʻlak — oʻttiz yetti yarim foiz.</p>
  <p class="pe-ex__why">Vergul ikki xona oʻngga surildi: 0,375 → 37,5.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">0,06 × 100 = 6 → 6%</p>
  <p class="pe-ex__uz">Yuzdan olti boʻlak — olti foiz.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">1,25 × 100 = 125 → 125%</p>
  <p class="pe-ex__uz">Bir butun va chorak — bir yuz yigirma besh foiz.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Eng koʻp uchraydigan chalkashlik: 0,5 va 5%</p>
  <p>0,5 — bu <b>50%</b>, 5% emas! Vergul ikki xona surilishi kerak, bitta emas. Tekshirish
  oson: 0,5 butunning yarmi, yarim esa yuz katakning ellikta katagi. 5% esa juda oz —
  yuzta katakdan beshtasi.</p>
</div>

<h3>5. Foizdan orqaga: kasrga va oʻnlikka</h3>

<p>Teskari yoʻl ham teskari amal bilan: <b>100 ga boʻlamiz</b>, yaʼni vergulni ikki xona
<b>chapga</b> suramiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">40% = 40 ÷ 100 = 0,4</span>
    <span class="pm-solve__why">Foizdan oʻnlik kasrga</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">40% = 40/100</span>
    <span class="pm-solve__why">Foizdan oddiy kasrga: maxraj — doim 100</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">40/100 = 2/5</span>
    <span class="pm-solve__why">Surat va maxrajni 20 ga qisqartirdik (PM-16)</span>
  </div>
</div>

<p>Yana ikkita: 7% = 0,07 = 7/100 (qisqarmaydi, chunki 7 — tub son), 12% = 0,12 = 12/100 =
3/25 (4 ga qisqardi).</p>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Hisobda foiz belgisi qatnashmaydi</p>
  <p>Hisoblashga kirishishdan oldin foizni <b>doim</b> oʻnlik kasrga aylantiring. «30%» ni
  hisobga 30 deb olib kirsangiz, javob yuz baravar katta chiqadi. Foiz — yozuv, hisobning
  tili esa oʻnlik kasr.</p>
</div>

<h3>6. Nima uchun bularning hammasi kerak: taqqoslash</h3>

<p>Uch qiyofani bilishning eng katta foydasi — <b>har xil koʻrinishdagi sonlarni
taqqoslash</b>. Buning uchun ularni bitta qiyofaga keltiramiz, odatda foizga.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Savol</p>
    <p>Qaysi biri katta: <b>3/5</b> yoki <b>58%</b>?</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Yechim</p>
    <p>3/5 = 6/10 = 0,6 = <b>60%</b>. 60% &gt; 58%, demak <b>3/5 kattaroq</b>.</p>
  </div>
</div>

<h3>Matnli masala</h3>

<p><b>Uch doʻkon bir xil kurtkani sotmoqda.</b> «Bahor» doʻkoni narxning 1/4 qismini
chegirma qilyapti. «Chorsu» doʻkoni narxning 0,2 qismini. «Yangi bozor» esa 30 foizini.
Kurtka hamma joyda bir xil narxda turibdi.</p>

<p><b>Savol:</b> Dilnoza qaysi doʻkondan olsa, koʻproq yutadi?</p>

<p><b>Reja:</b> narx nomaʼlum, lekin u hamma joyda bir xil — demak faqat <i>ulush</i>larni
taqqoslash yetarli. Uchalasini foizga aylantiramiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">1/4 = 1 ÷ 4 = 0,25 = 25%</span>
    <span class="pm-solve__why">«Bahor» — kasrni oʻnlikka, keyin foizga</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">0,2 × 100 = 20%</span>
    <span class="pm-solve__why">«Chorsu» — vergul ikki xona oʻngga</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">30% — allaqachon foizda</span>
    <span class="pm-solve__why">«Yangi bozor» — aylantirish kerak emas</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">30% &gt; 25% &gt; 20%</span>
    <span class="pm-solve__why">Eng katta chegirma — «Yangi bozor» doʻkonida</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Faraz qilaylik, narx 200 000 soʻm. Choragi — 50 000; 0,2 qismi — 40 000; 30 foizi —
  60 000. Eng kattasi yana «Yangi bozor» ✓ Narxni boshqa qilib olsak ham tartib
  oʻzgarmaydi, chunki taqqoslanayotgani — ulush.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>1/4 — chorak, yaʼni «choragidan sal kamroq» boʻlgan 0,2 dan katta; 30% esa
  chorakdan katta. Hisoblashdan oldin ham javob koʻrinib turibdi.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">0,5 = 5%</p>
  <p class="pe-fix__good">0,5 = 50%</p>
  <p class="pe-fix__why">Vergul <b>ikki</b> xona oʻngga suriladi, bitta emas: 0,5 → 05,0 →
  50. Nazorat savoli: 0,5 butunning yarmi; yarim — bu koʻpmi yoki 5 katakmi?</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">1/5 = 0,15</p>
  <p class="pe-fix__good">1/5 = 0,2</p>
  <p class="pe-fix__why">Surat va maxraj shunchaki yonma-yon yozib yuborilgan. Kasrni
  oʻnlikka aylantirish uchun <b>boʻlish</b> kerak: 1 ÷ 5 = 0,2. Yoki maxrajni 10 ga
  keltiring: 1/5 = 2/10 = 0,2.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">25% = 25</p>
  <p class="pe-fix__good">25% = 0,25</p>
  <p class="pe-fix__why">Foiz belgisi «yuzga boʻl» degan buyruq. Uni tushirib qoldirsangiz,
  hisob yuz baravar xato boʻladi: 800 × 25 = 20 000 emas, 800 × 0,25 = 200.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 0,08 ni foizda yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>8%.</b> Vergul ikki xona oʻngga: 0,08 → 8.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 3/4 ni oʻnlik kasr va foiz koʻrinishida yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>0,75 va 75%.</b> 3 ÷ 4 = 0,75; 0,75 × 100 = 75.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 60% ni qisqartirilgan oddiy kasr koʻrinishida yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3/5.</b> 60% = 60/100; surat va maxrajni 20 ga boʻldik.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Qaysi biri kichik: 0,35 yoki 2/5?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>0,35 kichik.</b> 2/5 = 0,4 = 40%, 0,35 esa 35%. 35% &lt; 40%.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Bekzod kitobning 0,35 qismini oʻqidi, Dilnoza esa xuddi shu
  kitobning 2/5 qismini. Kim koʻproq oʻqidi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Dilnoza.</b> 0,35 = 35%, 2/5 = 0,4 = 40%. Kitob bitta va bir xil, shuning uchun
    ulushlarni taqqoslash yetarli: 40% &gt; 35%.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Foiz</b><span>butunning yuzdan bir boʻlagi, belgisi %; ingl. percent</span></li>
  <li><b>Butun</b><span>foiz olinayotgan miqdorning oʻzi, 100%; ingl. whole</span></li>
  <li><b>Ulush</b><span>butunning bir qismi, kasr yoki foiz bilan aytiladi; ingl.
    share</span></li>
  <li><b>Oʻnlik kasr</b><span>vergul bilan yoziladigan kasr; ingl. decimal</span></li>
  <li><b>Surat</b><span>kasrning yuqorigi soni; ingl. numerator</span></li>
  <li><b>Maxraj</b><span>kasrning pastki soni; ingl. denominator</span></li>
  <li><b>Aylantirish</b><span>bir yozuvdan boshqasiga oʻtish; ingl. convert</span></li>
  <li><b>Qisqartirish</b><span>kasrni umumiy boʻluvchiga boʻlish; ingl. simplify</span></li>
  <li><b>Taqqoslash</b><span>qaysi biri katta ekanini aniqlash; ingl. compare</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Foiz — yuzdan boʻlak.</b> 25% = 25/100 = 0,25. Butunning oʻzi — 100%.</li>
    <li><b>Vergul ikki xona:</b> oʻnlikdan foizga — oʻngga; foizdan oʻnlikka — chapga.</li>
    <li><b>Taqqoslash uchun bitta qiyofaga keltiring.</b> 3/5 va 58% ni yonma-yon
      qoʻyishning yagona yoʻli — ikkalasini ham foizga aylantirish.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-23 — sonning foizini topish
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-23: Sonning foizini topish",
        "category": "math",
        "order": 23,
        "summary": (
            "«240 000 soʻmning 30 foizi qancha?» — foizni oʻnlik kasrga aylantirib "
            "koʻpaytirish, 1% orqali ogʻzaki hisoblash va oson foizlarning yoʻllari."
        ),
        "stories": ["Bozordagi chegirma"],
        "content": """
<h2>PM-23: Sonning foizini topish</h2>

<p>Afsonaning 240 000 soʻmi bor edi. U pulining 30 foiziga kitob oldi. Kitob necha soʻm
turdi? Bu — foiz bilan bogʻliq savollarning eng koʻp uchraydigani: <b>butun maʼlum, foiz
maʼlum, qism nomaʼlum</b>. Va uni yechishning bitta qisqa yoʻli bor.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>sonning berilgan foizini bir amal bilan topasiz;</li>
    <li>1% orqali ogʻzaki hisoblashni oʻrganasiz;</li>
    <li>10%, 50%, 25%, 20%, 5% ni qogʻozsiz hisoblaysiz;</li>
    <li>javob mantiqiy chiqqanini taxmin bilan tekshirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Asosiy formula</span>
  <span class="pe-chip pe-chip--o">sonning p foizi</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">son × p ÷ 100</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">son × 0,p</span>
</div>

<h3>1. Nega koʻpaytirish?</h3>

<p>PM-22 da koʻrdik: 30% — bu 30/100, yaʼni 0,3. Endi «240 000 ning 30 foizi» degan gapni
soʻzma-soʻz oʻqiymiz: <b>240 000 ning 0,3 qismi</b>. Kasrning «qismi» esa PM-18 dan beri
bizga tanish — u <b>koʻpaytirish</b> bilan topiladi. Yarmini topish uchun 1/2 ga
koʻpaytirgan edik; 0,3 qismini topish uchun 0,3 ga koʻpaytiramiz.</p>

<div class="pe-call pe-rule">
  <p class="pe-call__t">«…ning» degan soʻz koʻpaytirishni anglatadi</p>
  <p>Matnda «<b>ning</b> foizi», «<b>ning</b> yarmi», «<b>ning</b> uchdan biri» — hammasi
  bitta amal: koʻpaytirish. Bu qoidani bir marta tushunsangiz, foiz masalalari oddiy
  koʻpaytirishga aylanadi.</p>
</div>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">Butun (100%)</span>
    <span class="pm-model__bar" style="width:100%">240 000 soʻm</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">Kitob (30%)</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:30%">?</span>
  </div>
  <p class="pm-model__tot">Qism = 240 000 × 0,3</p>
</div>

<h3>2. Birinchi usul: oʻnlik kasrga aylantirib koʻpaytirish</h3>

<p>Bu asosiy usul. Uch qadam: foizni oʻnlikka aylantiring, songa koʻpaytiring, birlikni
yozing.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">240 000 ning 30% i</span>
    <span class="pm-solve__why">Berilgan: butun 240 000, foiz 30</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">30% = 0,3</span>
    <span class="pm-solve__why">Vergulni ikki xona chapga surdik (PM-22)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">240 000 × 0,3 = 72 000</span>
    <span class="pm-solve__why">24 × 3 = 72, keyin nollar va vergul joyiga qoʻyildi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Kitob 72 000 soʻm turdi</span>
    <span class="pm-solve__why">Birlik — soʻm; javob butundan kichik ✓</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>30% — chorakdan (25%) sal koʻproq. 240 000 ning choragi 60 000. Bizning javob 72 000 —
  60 000 dan katta, lekin yarmidan (120 000) kichik ✓ Mantiqiy.</p>
</div>

<h3>3. Ikkinchi usul: 1% orqali</h3>

<p>Kalkulyator boʻlmasa, bu usul tezroq. Avval <b>bitta foiz</b>ni topamiz — buning uchun
sonni 100 ga boʻlish yetarli (vergul ikki xona chapga). Keyin uni kerakli foizga
koʻpaytiramiz.</p>

<div class="pe-ex">
  <p class="pe-ex__math">900 ÷ 100 = 9 → 9 × 3 = 27</p>
  <p class="pe-ex__uz">900 ning bir foizi 9; uch foizi esa 27.</p>
  <p class="pe-ex__why">Foiz — yuzdan boʻlak, shuning uchun 1% ni topish 100 ga boʻlish
  demakdir.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">4500 ÷ 100 = 45 → 45 × 20 = 900</p>
  <p class="pe-ex__uz">4500 ning yigirma foizi — 900.</p>
</div>

<h3>4. Oson foizlar — ularni hisoblamang, biling</h3>

<p>Baʼzi foizlarni koʻpaytirishsiz, faqat boʻlish bilan topsa boʻladi. Bozorda, doʻkonda,
imtihonda shu yoʻl tezlik beradi.</p>

<div class="pe-table-wrap"><table>
  <tr><th>Foiz</th><th>Nima qilamiz</th><th>Misol</th></tr>
  <tr><td>50%</td><td>2 ga boʻlamiz</td><td>86 000 → 43 000</td></tr>
  <tr><td>25%</td><td>4 ga boʻlamiz</td><td>4800 → 1200</td></tr>
  <tr><td>20%</td><td>5 ga boʻlamiz</td><td>350 → 70</td></tr>
  <tr><td>10%</td><td>10 ga boʻlamiz</td><td>62 000 → 6200</td></tr>
  <tr><td>5%</td><td>10% ning yarmi</td><td>62 000 → 3100</td></tr>
  <tr><td>1%</td><td>100 ga boʻlamiz</td><td>62 000 → 620</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Foizlarni bir-biriga qoʻshsa boʻladi</p>
  <p>15% ni topish uchun alohida formula kerak emas: <b>15% = 10% + 5%</b>. 60 000 ning 10%
  i — 6000, yarmi — 3000, jami <b>9000</b>. Xuddi shunday 35% = 25% + 10%, 30% = 10% × 3.
  Bu bozorda eng koʻp ishlatiladigan hisob.</p>
</div>

<h3>5. Foiz 100 dan katta boʻlsa</h3>

<p>Qoida oʻzgarmaydi. 90 ning 120 foizi: 120% = 1,2, demak 90 × 1,2 = <b>108</b>. Javob
butundan katta chiqdi — va bu toʻgʻri, chunki 120% butundan koʻp. Har doim shu nazoratni
qiling:</p>

<div class="pe-legend">
  <span><i class="pe-chip pe-chip--v"></i> foiz &lt; 100% → javob butundan <b>kichik</b></span>
  <span><i class="pe-chip pe-chip--o"></i> foiz = 100% → javob butunning <b>oʻzi</b></span>
  <span><i class="pe-chip pe-chip--s"></i> foiz &gt; 100% → javob butundan <b>katta</b></span>
</div>

<h3>Matnli masala</h3>

<p><b>Maktabda 750 oʻquvchi bor.</b> Ulardan 12 foizi sport toʻgaragiga qatnaydi.
Toʻgarakka qatnamaydiganlar sinf tadbiriga qoladi.</p>

<p><b>Savol:</b> nechta oʻquvchi sport toʻgaragiga qatnaydi va nechtasi tadbirga qoladi?</p>

<p><b>Reja:</b> butun — 750 oʻquvchi. Avval 12 foizni topamiz, keyin uni butundan ayiramiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">1% = 750 ÷ 100 = 7,5</span>
    <span class="pm-solve__why">Bir foizni topdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">12% = 7,5 × 12 = 90</span>
    <span class="pm-solve__why">Bir foizni oʻn ikkiga koʻpaytirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">750 − 90 = 660</span>
    <span class="pm-solve__why">Qolganlar tadbirga: 90 sportda, 660 tadbirda</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Boshqa yoʻl bilan: 750 × 0,12 = 90 ✓ Va nazorat: 90 + 660 = 750 ✓ — qismlar butunni
  toʻldirdi. 1% i 7,5 kishi chiqqani gʻalati emas: bu oraliq hisob, oxirgi javob esa butun
  son.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>12% — oʻndan bir sal koʻproq. 750 ning oʻndan biri 75, demak javob 75 dan biroz
  katta boʻlishi kerak. 90 — mos.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">700 ning 15% i = 700 × 15 = 10 500</p>
  <p class="pe-fix__good">700 ning 15% i = 700 × 0,15 = 105</p>
  <p class="pe-fix__why">Foiz belgisi tushirib qoldirilgan. Javob butunning oʻzidan 15
  baravar katta chiqdi — bu darrov koʻrinib turadigan xato. Ulush butundan katta
  boʻlolmaydi (foiz 100 dan kichik boʻlsa).</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">240 ning 30% i = 240 ÷ 30 = 8</p>
  <p class="pe-fix__good">240 ning 30% i = 240 × 0,3 = 72</p>
  <p class="pe-fix__why">Foizga boʻlingan. Boʻlish faqat <b>100</b> ga qilinadi (1% ni
  topishda), foizga emas. Nazorat: 30% — chorakdan koʻproq, 240 ning choragi esa 60;
  8 juda kichik.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">80 000 ning 5% i = 8000</p>
  <p class="pe-fix__good">80 000 ning 5% i = 4000</p>
  <p class="pe-fix__why">5% oʻrniga 10% hisoblangan. 5% — bu 10% ning <b>yarmi</b>:
  8000 ÷ 2 = 4000. Bu ogʻzaki hisobdagi eng koʻp uchraydigan shoshqaloqlik.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 400 ning 25% i qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>100.</b> 25% — chorak, demak 400 ÷ 4 = 100.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 350 ning 8% i qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>28.</b> 1% = 3,5; 3,5 × 8 = 28. Yoki 350 × 0,08 = 28.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 60 000 soʻmning 15% i qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>9000 soʻm.</b> 10% = 6000, 5% = 3000, jami 9000.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 2500 ning 6% i qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>150.</b> 1% = 25; 25 × 6 = 150.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Jasurning oyligi 1 800 000 soʻm. U har oy oyligining 20 foizini
  jamgʻarmaga qoʻyadi. Bir oyda qancha jamgʻaradi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>360 000 soʻm.</b> 20% — beshdan bir: 1 800 000 ÷ 5 = 360 000. Tekshirish:
    360 000 × 5 = 1 800 000 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Foiz</b><span>yuzdan boʻlak, belgisi %; ingl. percent</span></li>
  <li><b>Butun</b><span>foiz olinayotgan asos, 100%; ingl. whole</span></li>
  <li><b>Qism</b><span>butunning foiz bilan ajratilgan boʻlagi; ingl. part</span></li>
  <li><b>Asos</b><span>foiz nimadan olinayotgani; ingl. base</span></li>
  <li><b>Koʻpaytuvchi</b><span>foizning oʻnlik koʻrinishi, masalan 0,3; ingl.
    multiplier</span></li>
  <li><b>Jamgʻarma</b><span>ajratib qoʻyilgan pul; ingl. savings</span></li>
  <li><b>Taxmin</b><span>javobning taxminiy kattaligini oldindan aytish; ingl.
    estimate</span></li>
  <li><b>Tekshirish</b><span>javobni teskari amal bilan sinash; ingl. check</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Sonning p foizi = son × 0,p.</b> Foizni avval oʻnlik kasrga aylantiring.</li>
    <li><b>1% = son ÷ 100.</b> Undan istalgan foizni koʻpaytirib olasiz — ogʻzaki
      hisobning kaliti.</li>
    <li><b>Oson foizlarni yodlang:</b> 50% ÷2, 25% ÷4, 20% ÷5, 10% ÷10, 5% — oʻndan
      birning yarmi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-24 — foizdan butunni topish va «necha foiz?»
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-24: Foizdan butunni topish va «necha foiz?» savoli",
        "category": "math",
        "order": 24,
        "summary": (
            "Foizning ikkita teskari savoli: «40 dan 34 tasi necha foiz?» va «12 foizi "
            "9000 boʻlsa, butun qancha?». Boʻlish, 1% orqali yoʻl va uch turdagi "
            "savolni ajratish."
        ),
        "stories": ["Imtihon natijasi"],
        "content": """
<h2>PM-24: Foizdan butunni topish va «necha foiz?» savoli</h2>

<p>Jasur imtihondan chiqdi: 40 savoldan 34 tasini toʻgʻri ishlagan. Maktab esa natijani
foizda eʼlon qiladi. Bu <b>necha foiz</b> boʻladi? Oʻsha kuni onasi doʻkonda boshqa savolga
duch keldi: chegirma 12 foiz ekan va u 9000 soʻmni tejadi. Unda <b>kurtka qancha
turgan</b>? Ikkala savol ham PM-23 ning teskarisi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>bir sonning ikkinchisidan necha foiz ekanini topasiz;</li>
    <li>foizi maʼlum boʻlganda butunni tiklaysiz;</li>
    <li>uch turdagi foiz savolini bir-biridan ajratasiz;</li>
    <li>har bir javobni teskari amal bilan tekshirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki teskari savol</span>
  <span class="pe-chip pe-chip--v">necha foiz = qism ÷ butun × 100</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">butun = qism ÷ 0,p</span>
</div>

<h3>1. Avval savolni tanib oling</h3>

<p>Foiz masalalarida uchta son qatnashadi: <b>butun</b>, <b>foiz</b> va <b>qism</b>.
Ulardan ikkitasi doim berilgan, bittasi soʻraladi. Shuning uchun birinchi ish — nima
nomaʼlumligini aniqlash.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Savol shunday berilgan</th><th>Nomaʼlum</th><th>Nima qilamiz</th></tr>
  <tr><td>160 ning 20 foizi qancha?</td><td class="pm-word__sym">qism</td>
      <td>160 × 0,2 = 32</td></tr>
  <tr><td>32 — 160 ning necha foizi?</td><td class="pm-word__sym">foiz</td>
      <td>32 ÷ 160 × 100 = 20%</td></tr>
  <tr><td>Sonning 20 foizi 32. Son qancha?</td><td class="pm-word__sym">butun</td>
      <td>32 ÷ 0,2 = 160</td></tr>
</table></div>

<p>Uch qatorda ham bir xil uchlik: 160, 20%, 32. Faqat qaysi biri yashiringani boshqa.
PM-23 birinchi qatorni oʻrgatgan edi — endi qolgan ikkitasi.</p>

<div class="pe-call pe-uz">
  <p class="pe-call__t">«Nimaning?» degan savolni oʻzingizga bering</p>
  <p>«32 — 160 ning necha foizi?» degan gapda <b>butun</b> — 160, chunki «ning» soʻzi
  undan keyin turibdi. Boʻlishda ham shu tartib: <b>qismni butunga</b> boʻlamiz, teskarisiga
  emas. Bu darsning eng koʻp xato qilinadigan joyi shu.</p>
</div>

<h3>2. «Necha foiz?» — qismni butunga boʻlamiz</h3>

<p>Nega boʻlish? Chunki foiz — bu ulush, ulush esa kasr: qism/butun. PM-22 dan bilamiz —
kasrni foizga aylantirish uchun uni oʻnlikka aylantirib, 100 ga koʻpaytiramiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">34 ta toʻgʻri, jami 40 ta savol</span>
    <span class="pm-solve__why">Qism — 34, butun — 40</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">34/40</span>
    <span class="pm-solve__why">Ulushni kasr qilib yozdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">34 ÷ 40 = 0,85</span>
    <span class="pm-solve__why">Kasrdan oʻnlikka (PM-21 dagi boʻlish)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">0,85 × 100 = 85%</span>
    <span class="pm-solve__why">Jasurning natijasi — 85 foiz</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Teskari amal — PM-23 ning oʻzi: 40 ning 85% i = 40 × 0,85 = 34 ✓ Yana bir nazorat:
  qism butundan kichik edi, demak javob 100% dan kichik chiqishi shart. 85% &lt; 100% ✓</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Qisqartirish tezlashtiradi</p>
  <p>34/40 ni avval qisqartirsa ham boʻladi: 34/40 = 17/20 = 85/100 = 85%. Maxrajni 100 ga
  keltirish — foizni topishning eng qisqa yoʻli, chunki foiz allaqachon yuz maxrajli kasr.
  9/20 = 45/100 = 45%, 7/25 = 28/100 = 28%.</p>
</div>

<h3>3. Foizdan butunni topish — bu boʻlish</h3>

<p>Endi ikkinchi teskari savol. Butun nomaʼlum, lekin uning bir boʻlagi va oʻsha boʻlakning
foizi maʼlum. PM-23 da <b>butun × 0,p = qism</b> edi. Demak butunni tiklash uchun teskari
amal — <b>qismni 0,p ga boʻlish</b>.</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">Chegirma (12%)</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:12%">9000</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">Narx (100%)</span>
    <span class="pm-model__bar" style="width:100%">?</span>
  </div>
  <p class="pm-model__tot">Kichik boʻlak maʼlum — butunni topish kerak</p>
</div>

<p>Buni ikki yoʻl bilan yechish mumkin. Ikkalasi ham bir xil javob beradi.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">1-yoʻl: 1% orqali</p>
    <p>12% = 9000, demak <b>1% = 9000 ÷ 12 = 750</b>. Butun — 100%, yaʼni
    <b>750 × 100 = 75 000</b>.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">2-yoʻl: toʻgʻridan-toʻgʻri boʻlish</p>
    <p>12% = 0,12, demak <b>9000 ÷ 0,12 = 75 000</b>. Vergulni surib boʻlish —
    900 000 ÷ 12 = 75 000.</p>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>75 000 × 0,12 = 9000 ✓ Kurtka 75 000 soʻm turgan. Nazorat: butun har doim qismdan
  katta chiqishi kerak (foiz 100 dan kichik boʻlsa). 75 000 &gt; 9000 ✓</p>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Bu yerda koʻpaytirish emas, boʻlish</p>
  <p>Eng koʻp uchraydigan xato: 9000 × 0,12 = 1080 deb yozish. Oʻylab koʻring — javob
  qismdan ham kichik chiqdi. Butun kichkina boʻlagidan kichik boʻlishi mumkinmi? Yoʻq.
  Demak amal notoʻgʻri tanlangan.</p>
</div>

<h3>4. 1% orqali yoʻl — eng ishonchlisi</h3>

<p>Agar formulalar chalkashib ketsa, doim shu yoʻlga qayting: <b>avval 1% ni toping</b>,
keyin kerakli foizga koʻpaytiring. Bu uch turdagi savolning hammasida ishlaydi.</p>

<div class="pe-ex">
  <p class="pe-ex__math">30% = 60 → 1% = 60 ÷ 30 = 2 → 100% = 200</p>
  <p class="pe-ex__uz">Sonning oʻttiz foizi 60 boʻlsa, sonning oʻzi 200.</p>
  <p class="pe-ex__why">Bir foiz — 2; yuz foiz esa undan yuz baravar katta.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">5% = 15 → 1% = 3 → 100% = 300</p>
  <p class="pe-ex__uz">Sonning besh foizi 15 boʻlsa, son — 300.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Sherbek kitob doʻkonida lugʻat buyurtma qildi.</b> Buyurtma berishda u narxning 40
foizini oldindan toʻladi — bu 24 000 soʻm boʻldi. Qolganini kitob kelganda toʻlaydi.</p>

<p><b>Savol:</b> lugʻat necha soʻm turadi va Sherbek yana qancha toʻlashi kerak?</p>

<p><b>Reja:</b> qism (24 000) va uning foizi (40%) maʼlum, butun nomaʼlum. Butunni
topamiz, keyin toʻlanganini ayiramiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">40% = 24 000</span>
    <span class="pm-solve__why">Berilgan: oldindan toʻlov</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">1% = 24 000 ÷ 40 = 600</span>
    <span class="pm-solve__why">Bir foizni topdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">100% = 600 × 100 = 60 000</span>
    <span class="pm-solve__why">Lugʻatning toʻliq narxi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">60 000 − 24 000 = 36 000</span>
    <span class="pm-solve__why">Qolgan toʻlov — 36 000 soʻm</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>60 000 ning 40% i: 60 000 × 0,4 = 24 000 ✓ Qolgani 60% boʻlishi kerak edi:
  60 000 × 0,6 = 36 000 ✓ Ikki yoʻl bir xil javob berdi.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>40% — butunning yarmiga yaqin. Toʻlangani 24 000 boʻlsa, butun 50 000 dan
  sal koʻproq boʻlishi kerak. 60 000 — mos.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">18 — 30 ning necha foizi? 30 ÷ 18 × 100 ≈ 167%</p>
  <p class="pe-fix__good">18 ÷ 30 × 100 = 60%</p>
  <p class="pe-fix__why">Boʻlish teskari qilingan. <b>Qism butunga</b> boʻlinadi. Nazorat:
  18 — 30 dan kichik, demak javob 100% dan kichik chiqishi shart edi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Sonning 12% i 9000. Son = 9000 × 0,12 = 1080</p>
  <p class="pe-fix__good">Son = 9000 ÷ 0,12 = 75 000</p>
  <p class="pe-fix__why">Butunni topishda koʻpaytirilgan. Butun har doim oʻz boʻlagidan
  katta — 1080 esa 9000 dan kichik, demak javob mantiqsiz.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Sinfda 25 oʻquvchi, 5 tasi kelmadi → 5% kelmadi</p>
  <p class="pe-fix__good">5 ÷ 25 × 100 = 20% kelmadi</p>
  <p class="pe-fix__why">Qismning oʻzi foiz deb olingan. 5 ta oʻquvchi — 5% emas: butun 100
  emas, 25. Foiz faqat butun 100 boʻlgandagina qism bilan bir xil son boʻladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 20 — 50 ning necha foizi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>40%.</b> 20 ÷ 50 = 0,4; 0,4 × 100 = 40. Yoki 20/50 = 40/100.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 45 — 60 ning necha foizi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>75%.</b> 45/60 = 3/4 = 0,75 = 75%.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Sonning 25% i 90. Son qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>360.</b> 25% — chorak, demak son toʻrt baravar katta: 90 × 4 = 360. Tekshirish:
    360 ÷ 4 = 90 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Sonning 8% i 24. Son qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>300.</b> 1% = 24 ÷ 8 = 3; 100% = 3 × 100 = 300. Tekshirish: 300 × 0,08 = 24 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Dilnoza kitobning 84 betini oʻqidi — bu kitobning 70 foizi
  ekan. Kitobda jami nechta bet bor va yana nechta bet qoldi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>120 bet, yana 36 bet qoldi.</b> 1% = 84 ÷ 70 = 1,2; 100% = 120 bet.
    Qolgani: 120 − 84 = 36 bet (yaʼni 30%). Tekshirish: 120 × 0,7 = 84 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Qism</b><span>butundan ajratilgan boʻlak; ingl. part</span></li>
  <li><b>Butun</b><span>100% ga teng asos; ingl. whole</span></li>
  <li><b>Ulush</b><span>qismning butunga nisbati; ingl. share</span></li>
  <li><b>Teskari amal</b><span>koʻpaytirishga — boʻlish, qoʻshishga — ayirish; ingl.
    inverse operation</span></li>
  <li><b>Oldindan toʻlov</b><span>narxning bir qismini avval toʻlash; ingl. deposit</span></li>
  <li><b>Natija foizi</b><span>toʻgʻri javoblar ulushi; ingl. score percentage</span></li>
  <li><b>Tiklash</b><span>maʼlum boʻlakdan butunni topish; ingl. recover</span></li>
  <li><b>Nazorat</b><span>javob mantiqiy ekanini tekshirish; ingl. sanity check</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>«Necha foiz?» — qismni butunga boʻling</b> va 100 ga koʻpaytiring.</li>
    <li><b>Butunni topish — boʻlish:</b> qism ÷ 0,p. Yoki avval 1% ni toping, keyin
      100 ga koʻpaytiring.</li>
    <li><b>Javobni mantiq bilan tekshiring:</b> butun qismdan katta, foiz esa qism
      butundan kichik boʻlsa, 100 dan kichik.</li>
  </ul>
</div>
""",
    },
]
