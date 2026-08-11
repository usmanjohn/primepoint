# -*- coding: utf-8 -*-
"""Prime Math — Blok B, darslar 16–18 (kasrlar bilan amallar).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt

Uchta oyoq birga yoziladi:
  mashqlar — practice/management/commands/_practice_pm_16_18.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_16_18.py

⚠️ Kumulyativ — bu uch darsning eng qattiq cheklovi:
  • NOTOʻGʻRI KASR va ARALASH SON PM-19 da oʻrgatiladi. Shuning uchun bu
    darslarda har bir javob toʻgʻri kasr (yoki butun son) boʻlishi shart:
    yigʻindilar 1 dan oshmaydi, 5/4 yoki 1 1/2 kabi yozuvlar yoʻq.
  • Shu sababli PM-18 da kasrga boʻlish faqat BIRLIK KASRga boʻlish bilan
    chegaralangan (1/6 ning teskarisi — butun son 6, notoʻgʻri kasr emas).
  • Oʻnlik kasr PM-20 da — vergulli son yoʻq.
  • Foiz PM-23 dan boshlanadi — foiz yoʻq.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_16_18.py --author=prime
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
    # PM-16 — qisqartirish va taqqoslash
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-16: Kasrlarni qisqartirish va taqqoslash",
        "category": "math",
        "order": 16,
        "summary": (
            "3/4 va 6/8 — bir xil narsami? Teng kasrlar, kasrning asosiy xossasi, "
            "EKUB bilan bir qadamda qisqartirish va har qanday ikki kasrni taqqoslash."
        ),
        "stories": ["Qaysi biri koʻproq?"],
        "content": """
<h2>PM-16: Kasrlarni qisqartirish va taqqoslash</h2>

<p>Nodira opaning daftarida yozilgan: <b>3/4 stakan sut</b>. Telefondagi retseptda esa
xuddi shu taom uchun <b>6/8 stakan sut</b> deyilgan. Afsona ikkalasiga qarab qoldi:
qaysi biri toʻgʻri? Javob — <b>ikkalasi ham</b>. Bu bitta miqdorning ikki xil
yozuvi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>teng kasrlarni tanib olasiz va oʻzingiz yasaysiz;</li>
    <li>kasrning asosiy xossasini bilasiz va nega u ishlashini tushunasiz;</li>
    <li>EKUB yordamida kasrni <b>bir qadamda</b> qisqartirasiz;</li>
    <li>maxrajlari har xil boʻlgan ikki kasrni taqqoslaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Kasrning asosiy xossasi</span>
  <span class="pe-chip pe-chip--s">surat</span>
  <span class="pe-op">va</span>
  <span class="pe-chip pe-chip--o">maxraj</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">bir xil songa koʻpaytirilsa yoki boʻlinsa,
    kasr oʻzgarmaydi</span>
</div>

<h3>1. Bir xil miqdor, boshqa yozuv</h3>

<p>Bitta nonni <b>4</b> boʻlakka boʻlib, 3 tasini oling. Endi xuddi shu nonni <b>8</b>
boʻlakka boʻlib, 6 tasini oling. Qoʻlingizdagi non miqdori bir xil — faqat pichoq
boshqacha yurgan.</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">3/4</span>
    <span class="pm-model__bar" style="width:75%">uchta chorak</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">6/8</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:75%">oltita sakkizdan
      bir</span>
  </div>
  <p class="pm-model__tot">Uzunligi bir xil — demak kasrlar teng</p>
</div>

<p>Nega shunday boʻldi? Chunki har bir chorakni ikkiga boʻldik: boʻlaklar soni ham
(3 → 6), butunning boʻlinishi ham (4 → 8) ikki barobar oshdi. Ikkalasi birga oshgani
uchun ulush oʻzgarmadi.</p>

<div class="pe-ex">
  <p class="pe-ex__math">3/4 = (3 × 2)/(4 × 2) = 6/8</p>
  <p class="pe-ex__uz">Surat va maxrajni bir xil songa koʻpaytirdik — bu kasrni
  <b>kengaytirish</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">6/8 = (6 ÷ 2)/(8 ÷ 2) = 3/4</p>
  <p class="pe-ex__uz">Teskari yoʻl — bu kasrni <b>qisqartirish</b>.</p>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Nega bu xossa ishlaydi</p>
  <p>Kasr — aslida boʻlish. 6 ÷ 8 va 3 ÷ 4 bir xil natija beradi, chunki ikkala sonni
  ham 2 ga boʻldik. Bir xil songa boʻlingan boʻlinma oʻzgarmaydi.</p>
</div>

<h3>2. Qisqartirish</h3>

<p>Qisqartirish — surat va maxrajning <b>umumiy boʻluvchisi</b>ni topib, ikkalasini
ham unga boʻlish. Umumiy boʻluvchini PM-8 da oʻrgangan edik.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">12/18</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= 6/9</span>
    <span class="pm-solve__why">Ikkalasini 2 ga boʻldik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 2/3</span>
    <span class="pm-solve__why">Endi ikkalasini 3 ga boʻldik</span>
  </div>
</div>

<p>Ikki qadam ketdi. Lekin buni <b>bir qadamda</b> ham qilish mumkin edi — agar darrov
eng katta umumiy boʻluvchini olsak.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">EKUB(12, 18) = 6</span>
    <span class="pm-solve__why">PM-8 dagi usul</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">12/18 = (12 ÷ 6)/(18 ÷ 6) = 2/3</span>
    <span class="pm-solve__why">Bitta amalda tugadi</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Mana shu yerda EKUB ish beradi</p>
  <p>PM-8 da «EKUB qayerda kerak boʻladi?» degan savol qolgan edi. Javob shu: kasrni
  bir qadamda, oxirigacha qisqartirish uchun.</p>
</div>

<p>Surat va maxrajning 1 dan boshqa umumiy boʻluvchisi qolmasa, kasr
<b>qisqarmas</b> deyiladi. 2/3, 3/4, 7/9 — qisqarmas. Javobni doim shu holatda
yozish qabul qilingan.</p>

<h3>3. Eng katta xato — faqat bittasini boʻlish</h3>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Diqqat</p>
  <p><b>6/9 ≠ 2/9.</b> Faqat suratni boʻlsangiz, boʻlaklar soni kamayadi, lekin
  boʻlakning kattaligi oʻzgarmaydi — demak miqdor kamayib ketadi.<br>
  Toʻgʻrisi: <b>6/9 = 2/3</b> — ikkalasini ham 3 ga boʻlamiz.</p>
  <p>Va yana bittasi: qisqartirishda faqat <b>koʻpaytirish-boʻlish</b> ishlaydi.
  Surat va maxrajdan bir xil sonni <i>ayirib</i> boʻlmaydi: 5/7 va 3/5 teng emas.</p>
</div>

<h3>4. Taqqoslash</h3>

<p>Uch xil holat bor, uchtasi ham oson.</p>

<div class="pe-table-wrap"><table>
  <tr><th>Holat</th><th>Nima qilamiz</th><th>Misol</th></tr>
  <tr><td>Maxrajlar bir xil</td><td>Suratlarni solishtiramiz</td>
      <td>3/8 &lt; 5/8</td></tr>
  <tr><td>Suratlar bir xil</td><td>Maxraji kichigi kattaroq</td>
      <td>2/5 &gt; 2/7</td></tr>
  <tr><td>Ikkalasi ham har xil</td><td>Umumiy maxrajga keltiramiz</td>
      <td>1/2 va 2/5 → ?</td></tr>
</table></div>

<p>Uchinchi holatni ishlab koʻramiz. <b>1/2 va 2/5</b> dan qaysi biri katta? Boʻlaklar
har xil kattalikda — solishtirib boʻlmaydi. Demak ikkalasini bir xil boʻlakka
keltiramiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Umumiy maxraj: 10</span>
    <span class="pm-solve__why">2 va 5 ning eng kichik umumiy karralisi (EKUK)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">1/2 = 5/10</span>
    <span class="pm-solve__why">Surat va maxrajni 5 ga koʻpaytirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2/5 = 4/10</span>
    <span class="pm-solve__why">Surat va maxrajni 2 ga koʻpaytirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">5/10 &gt; 4/10, demak 1/2 &gt; 2/5</span>
    <span class="pm-solve__why">Endi boʻlaklar bir xil — suratlarni solishtirdik</span>
  </div>
</div>

<div class="pm-num">
  <div class="pm-num__track">
    <span class="pm-num__band" style="left:0%;width:50%"></span>
    <span class="pm-num__tick" style="left:0%"><i>0</i></span>
    <span class="pm-num__tick" style="left:40%"><i>2/5</i></span>
    <span class="pm-num__tick" style="left:50%"><i>1/2</i></span>
    <span class="pm-num__tick" style="left:100%"><i>1</i></span>
  </div>
</div>

<h3>5. Matnli masala</h3>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Masala</p>
  <p>5-A sinfda <b>20 oʻquvchi</b> bor, ulardan <b>12 tasi</b> kutubxonaga yozilgan.
  5-B sinfda <b>25 oʻquvchi</b> bor, ulardan <b>15 tasi</b> yozilgan. Qaysi sinfda
  yozilganlarning ulushi katta?</p>
</div>

<p><b>Nima soʻralyapti?</b> Sonlar emas — <b>ulush</b>. 15 soni 12 dan katta, lekin bu
hech narsani hal qilmaydi, chunki sinflar ham har xil.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">5-A: 12/20</span>
    <span class="pm-solve__why">EKUB(12, 20) = 4</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">12/20 = 3/5</span>
    <span class="pm-solve__why">Ikkalasini 4 ga boʻldik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5-B: 15/25 = 3/5</span>
    <span class="pm-solve__why">Ikkalasini 5 ga boʻldik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3/5 = 3/5 — ulushlar teng</span>
    <span class="pm-solve__why">Ikkala sinfda ham har besh oʻquvchidan uchtasi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>5-A: 20 ÷ 5 = 4, 4 × 3 = 12 ✓ &nbsp;·&nbsp; 5-B: 25 ÷ 5 = 5, 5 × 3 = 15 ✓
  Ikkala hisob ham oʻz soniga qaytdi.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Nega bu muhim</p>
  <p>Qisqartirish — «chiroyli yozish» uchun emas. U ikki narsani <b>solishtirish</b>
  imkonini beradi. 12/20 va 15/25 ga qarab hech narsa aytolmaysiz; 3/5 va 3/5 ga
  qarab esa darrov aytasiz.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">6/9 = 2/9</p>
  <p class="pe-fix__good">6/9 = 2/3</p>
  <p class="pe-fix__why">Faqat surat boʻlingan. Kasrning asosiy xossasi ikkalasini
  ham bir xil songa boʻlishni talab qiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">5/7 = 3/5 (ikkalasidan 2 ni ayirdim)</p>
  <p class="pe-fix__good">5/7 qisqarmas kasr — u oʻzgarmaydi</p>
  <p class="pe-fix__why">Xossada faqat koʻpaytirish va boʻlish bor. Ayirish kasrni
  butunlay boshqa songa aylantirib yuboradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">2/7 &gt; 2/5, chunki 7 &gt; 5</p>
  <p class="pe-fix__good">2/7 &lt; 2/5</p>
  <p class="pe-fix__why">Suratlar teng boʻlganda maxraji <b>kichik</b> kasr kattaroq:
  yettiga boʻlingan boʻlak beshga boʻlingandan kichik.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 8/12 ni qisqartiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>2/3.</b> EKUB(8, 12) = 4. 8 ÷ 4 = 2, 12 ÷ 4 = 3.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 2/3 ni maxraji 15 boʻlgan kasr koʻrinishida yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>10/15.</b> 15 ÷ 3 = 5, demak ikkalasini 5 ga koʻpaytiramiz:
    (2 × 5)/(3 × 5) = 10/15.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 4/9 va 4/7 dan qaysi biri katta?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>4/7.</b> Suratlar teng, demak maxraji kichigi kattaroq boʻladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 2/3 va 3/4 dan qaysi biri katta?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3/4.</b> Umumiy maxraj 12: 2/3 = 8/12, 3/4 = 9/12. 9 &gt; 8, demak
    3/4 kattaroq.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Bogʻda 30 ta daraxtdan 18 tasi olma. Olmalarning ulushini
  qisqarmas kasr bilan yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3/5.</b> 18/30, EKUB(18, 30) = 6: 18 ÷ 6 = 3, 30 ÷ 6 = 5. Tekshiruv:
    30 ÷ 5 = 6, 6 × 3 = 18 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Teng kasrlar</b><span>bir xil miqdorni bildiruvchi turli yozuvlar;
    ingl. equivalent fractions</span></li>
  <li><b>Qisqartirish</b><span>surat va maxrajni umumiy boʻluvchiga boʻlish;
    ingl. simplifying</span></li>
  <li><b>Kengaytirish</b><span>surat va maxrajni bir xil songa koʻpaytirish;
    ingl. expanding</span></li>
  <li><b>Qisqarmas kasr</b><span>surat va maxrajining umumiy boʻluvchisi 1 boʻlgan kasr;
    ingl. fraction in lowest terms</span></li>
  <li><b>Umumiy boʻluvchi</b><span>ikkala sonni ham qoldiqsiz boʻluvchi son;
    ingl. common divisor</span></li>
  <li><b>EKUB</b><span>eng katta umumiy boʻluvchi; ingl. greatest common divisor</span></li>
  <li><b>Umumiy maxraj</b><span>ikki kasrni bir xil boʻlakka keltiruvchi maxraj;
    ingl. common denominator</span></li>
  <li><b>Ulush</b><span>butunning qanchasi ekanini bildiruvchi kasr; ingl. share</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Surat va maxrajni bir xil songa koʻpaytirsangiz yoki boʻlsangiz, kasr
      oʻzgarmaydi.</b> Faqat koʻpaytirish va boʻlish — ayirish emas.</li>
    <li><b>EKUB kasrni bir qadamda qisqartiradi.</b></li>
    <li><b>Taqqoslash uchun umumiy maxraj kerak.</b> Boʻlaklar bir xil boʻlmasa,
      solishtirib boʻlmaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-17 — qoʻshish va ayirish, umumiy maxraj
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-17: Kasrlarni qoʻshish va ayirish — umumiy maxraj",
        "category": "math",
        "order": 17,
        "summary": (
            "1/2 + 1/3 nega 2/5 emas? Bir xil maxrajli kasrlarni qoʻshish, umumiy "
            "maxrajni EKUK bilan topish va javobni qisqartirish."
        ),
        "stories": ["Devorni ikki kunda boʻyash"],
        "content": """
<h2>PM-17: Kasrlarni qoʻshish va ayirish — umumiy maxraj</h2>

<p>Bekzod devorning <b>1/3</b> qismini birinchi kuni, <b>1/4</b> qismini ikkinchi kuni
boʻyadi. Otasi soʻradi: «Qanchasi tayyor?» Bekzod tez javob berdi: «Ikki
qoʻshuv bir — uch; uch qoʻshuv toʻrt — yetti. 2/7 boʻlibdi». Bu javob
<b>notoʻgʻri</b>, va nega notoʻgʻri ekanini tushunish bugungi darsning oʻzi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>bir xil maxrajli kasrlarni bir soniyada qoʻshasiz;</li>
    <li>maxrajlar nega hech qachon qoʻshilmasligini tushunasiz;</li>
    <li>EKUK yordamida eng kichik umumiy maxrajni topasiz;</li>
    <li>javobni qisqartirib, tugallangan koʻrinishda yozasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bir xil maxrajda</span>
  <span class="pe-chip pe-chip--s">suratlarni qoʻshamiz</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--neg">maxraj oʻzgarmaydi</span>
</div>

<h3>1. Boʻlaklar bir xil boʻlsa</h3>

<p>Nonning <b>1/8</b> qismi va yana <b>3/8</b> qismi — qancha? Boʻlaklar bir xil
kattalikda, shuning uchun ularni oddiygina <b>sanaymiz</b>: bitta boʻlak va uchta
boʻlak — toʻrtta boʻlak.</p>

<div class="pe-ex">
  <p class="pe-ex__math">1/8 + 3/8 = 4/8 = 1/2</p>
  <p class="pe-ex__uz">Toʻrtta sakkizdan bir — nonning yarmi. Javobni PM-16 dagidek
  qisqartirdik.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Maxraj nega qoʻshilmaydi</p>
  <p>Maxraj — boʻlakning <b>nomi</b>, soni emas. «Uchta olma + ikkita olma = beshta
  olma» deymiz, «beshta olmaolma» demaymiz. Xuddi shunday: 1/8 + 3/8 = 4/8, hech
  qachon 4/16 emas.</p>
</div>

<p>Ayirish ham xuddi shunday ishlaydi:</p>

<div class="pe-ex">
  <p class="pe-ex__math">7/9 − 4/9 = 3/9 = 1/3</p>
  <p class="pe-ex__uz">Toʻqqizta boʻlakdan yettitasi bor edi, toʻrttasi ketdi.</p>
</div>

<h3>2. Boʻlaklar har xil boʻlsa</h3>

<p>Endi Bekzodning masalasi. <b>1/3 + 1/4</b>. Bu yerda boʻlaklar har xil kattalikda —
uchdan bir chorakdan katta. Har xil narsani qoʻshib boʻlmaydi, avval ularni
<b>bir xil boʻlakka</b> aylantirish kerak.</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">1/3</span>
    <span class="pm-model__bar" style="width:33%">= 4/12</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">1/4</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:25%">= 3/12</span>
  </div>
  <p class="pm-model__tot">Ikkalasi ham oʻn ikkidan boʻlakka aylandi</p>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">EKUK(3, 4) = 12</span>
    <span class="pm-solve__why">Eng kichik umumiy maxraj — PM-8 dagi usul</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">1/3 = 4/12</span>
    <span class="pm-solve__why">12 ÷ 3 = 4, demak ikkalasini 4 ga koʻpaytirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">1/4 = 3/12</span>
    <span class="pm-solve__why">12 ÷ 4 = 3, ikkalasini 3 ga koʻpaytirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">4/12 + 3/12 = 7/12</span>
    <span class="pm-solve__why">Endi boʻlaklar bir xil — suratlarni qoʻshdik</span>
  </div>
</div>

<p>Demak devorning <b>7/12</b> qismi boʻyalgan, 2/7 emas. Farqni koʻring: 7/12 yarmidan
biroz koʻp, 2/7 esa uchdan birdan ham kam. Bekzodning javobi juda katta xato edi.</p>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Tez tekshiruv</p>
  <p>Qoʻshishda javob har ikkala qoʻshiluvchidan ham <b>katta</b> boʻlishi shart.
  Bekzodning javobi 2/7 esa 1/3 dan kichik chiqqan edi — bu allaqachon xato
  ekanini koʻrsatib turibdi.</p>
</div>

<h3>3. Bir maxraj ikkinchisiga boʻlinsa</h3>

<p>Baʼzida umumiy maxrajni izlash shart emas — u allaqachon oldingizda turadi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2/3 − 1/6</span>
    <span class="pm-solve__why">6 soni 3 ga boʻlinadi — demak umumiy maxraj 6</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= 4/6 − 1/6</span>
    <span class="pm-solve__why">Faqat birinchi kasrni kengaytirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 3/6 = 1/2</span>
    <span class="pm-solve__why">Ayirdik va qisqartirdik</span>
  </div>
</div>

<h3>4. Uch qadamlik tartib</h3>

<div class="pe-steps">
  <ol>
    <li><b>Umumiy maxrajni toping</b> — maxrajlarning EKUK i.</li>
    <li><b>Har bir kasrni kengaytiring</b> — umumiy maxrajni oʻz maxrajiga boʻling va
      chiqqan songa surat bilan maxrajni koʻpaytiring.</li>
    <li><b>Suratlarni qoʻshing yoki ayiring</b>, maxrajni oʻzgarishsiz qoldiring, keyin
      javobni qisqartiring.</li>
  </ol>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">2/5 + 3/10 = 4/10 + 3/10 = 7/10</p>
  <p class="pe-ex__uz">EKUK(5, 10) = 10. Faqat birinchi kasr kengaydi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">1/2 + 1/3 = 3/6 + 2/6 = 5/6</p>
  <p class="pe-ex__uz">EKUK(2, 3) = 6. «Ikki qoʻshuv uch — besh» degan javob (2/5)
  butunlay boshqa son.</p>
</div>

<h3>5. Matnli masala</h3>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Masala</p>
  <p>Afsona kitobning <b>1/4</b> qismini dushanba, <b>2/5</b> qismini seshanba kuni
  oʻqidi. Kitobning qanchasi <b>qolgan</b>?</p>
</div>

<p><b>Diqqat:</b> soʻralgani oʻqilgani emas, <b>qolgani</b>. Demak ikki qadam kerak.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">EKUK(4, 5) = 20</span>
    <span class="pm-solve__why">Umumiy maxraj</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">1/4 = 5/20 &nbsp;·&nbsp; 2/5 = 8/20</span>
    <span class="pm-solve__why">20 ÷ 4 = 5 va 20 ÷ 5 = 4</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5/20 + 8/20 = 13/20</span>
    <span class="pm-solve__why">Oʻqilgan qism</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">20/20 − 13/20 = 7/20</span>
    <span class="pm-solve__why">Butun kitob — 20/20; qolgani 7/20</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>13/20 + 7/20 = 20/20 = 1 ✓ Butun kitob qaytdi. Va 13/20 yarmidan sal koʻproq —
  Afsona kitobning yarmidan koʻpini oʻqigan, demak javob mantiqiy.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Butunni kasr koʻrinishida yozish</p>
  <p>Butundan kasr ayirish uchun butunni <b>maxraj/maxraj</b> koʻrinishida yozing:
  1 = 20/20, 1 = 12/12, 1 = 8/8. Shundan keyin ayirish oddiy boʻlib qoladi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">1/2 + 1/3 = 2/5</p>
  <p class="pe-fix__good">1/2 + 1/3 = 5/6</p>
  <p class="pe-fix__why">Suratlar ham, maxrajlar ham qoʻshib yuborilgan. Maxraj —
  boʻlakning nomi; u qoʻshilmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">3/8 + 1/8 = 4/16</p>
  <p class="pe-fix__good">3/8 + 1/8 = 4/8 = 1/2</p>
  <p class="pe-fix__why">Maxrajlar allaqachon bir xil edi — ularni qoʻshishning hech
  qanday sababi yoʻq.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">1/3 + 1/6 = 2/9 (maxrajlarni koʻpaytirdim, keyin adashdim)</p>
  <p class="pe-fix__good">1/3 + 1/6 = 2/6 + 1/6 = 3/6 = 1/2</p>
  <p class="pe-fix__why">Umumiy maxrajga keltirganda <b>surat ham</b> oʻzgarishi kerak.
  Maxrajni oʻzgartirib, suratni joyida qoldirish — eng koʻp uchraydigan yoʻqotish.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 2/7 + 3/7 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5/7.</b> Maxrajlar bir xil — faqat suratlarni qoʻshamiz.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 5/6 − 1/6 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>4/6 = 2/3.</b> Ayirdik va qisqartirdik — javob doim qisqarmas koʻrinishda
    yoziladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 1/2 + 1/4 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3/4.</b> 4 soni 2 ga boʻlinadi, demak umumiy maxraj 4: 2/4 + 1/4 = 3/4.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 3/4 − 2/3 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>1/12.</b> EKUK(4, 3) = 12: 9/12 − 8/12 = 1/12. Javob juda kichik chiqdi —
    toʻgʻri, chunki 3/4 va 2/3 bir-biriga juda yaqin sonlar.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Dilnoza pulining 1/5 qismiga daftar, 1/2 qismiga kitob
  oldi. Pulining qanchasi qoldi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3/10.</b> EKUK(5, 2) = 10: 2/10 + 5/10 = 7/10 sarflandi.
    10/10 − 7/10 = 3/10 qoldi. Tekshiruv: 7/10 + 3/10 = 10/10 = 1 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Umumiy maxraj</b><span>ikki kasrni bir xil boʻlakka keltiruvchi maxraj;
    ingl. common denominator</span></li>
  <li><b>Eng kichik umumiy maxraj</b><span>maxrajlarning EKUK i;
    ingl. least common denominator</span></li>
  <li><b>EKUK</b><span>eng kichik umumiy karrali; ingl. least common multiple</span></li>
  <li><b>Kengaytirish</b><span>kasrni kattaroq maxrajli teng kasrga aylantirish;
    ingl. expanding</span></li>
  <li><b>Yigʻindi</b><span>qoʻshish natijasi; ingl. sum</span></li>
  <li><b>Ayirma</b><span>ayirish natijasi; ingl. difference</span></li>
  <li><b>Qisqarmas kasr</b><span>oxirigacha qisqartirilgan kasr; ingl. fraction in
    lowest terms</span></li>
  <li><b>Butun</b><span>maxraj/maxraj koʻrinishida yoziladi: 1 = 12/12; ingl. whole</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Maxrajlar bir xil boʻlsa — faqat suratlarni qoʻshing.</b> Maxraj hech
      qachon qoʻshilmaydi.</li>
    <li><b>Har xil boʻlsa — EKUK bilan umumiy maxrajga keltiring,</b> suratni ham
      birga oʻzgartirib.</li>
    <li><b>Javobni qisqartiring</b> va tekshiring: qoʻshishda natija ikkala
      qoʻshiluvchidan ham katta boʻlishi kerak.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-18 — koʻpaytirish va boʻlish
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-18: Kasrlarni koʻpaytirish va boʻlish",
        "category": "math",
        "order": 18,
        "summary": (
            "Yarimning uchdan biri qancha? Kasrni butun songa va kasrga koʻpaytirish, "
            "«dan» soʻzi nega koʻpaytirish ekani va boʻlishning haqiqiy maʼnosi."
        ),
        "stories": ["Yarimning uchdan biri"],
        "content": """
<h2>PM-18: Kasrlarni koʻpaytirish va boʻlish</h2>

<p>Retsept olti kishiga moʻljallangan va unda <b>1/2 stakan yogʻ</b> deyilgan. Nodira
opa esa ikki kishiga osh damlamoqchi — demak retseptning <b>uchdan bir</b> qismi
kerak. Savol: yarim stakanning uchdan biri qancha? Bu masala kasrlarni koʻpaytirishga
olib keladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>kasrni butun songa va kasrni kasrga koʻpaytirasiz;</li>
    <li>«…ning …dan biri» degan iborani koʻpaytirish deb oʻqiysiz;</li>
    <li>koʻpaytma nega kichrayishini tushunasiz;</li>
    <li>kasrga boʻlishning maʼnosini bilasiz: «nechtasi sigʻadi?»</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Koʻpaytirish qoidasi</span>
  <span class="pe-chip pe-chip--s">surat × surat</span>
  <span class="pe-op">/</span>
  <span class="pe-chip pe-chip--o">maxraj × maxraj</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">keyin qisqartiring</span>
</div>

<h3>1. Kasrni butun songa koʻpaytirish</h3>

<p>Bu eng tanish holat, chunki koʻpaytirish — takroriy qoʻshish (PM-3).</p>

<div class="pe-ex">
  <p class="pe-ex__math">3 × 1/8 = 1/8 + 1/8 + 1/8 = 3/8</p>
  <p class="pe-ex__uz">Uchta sakkizdan bir boʻlak — 3/8. Boʻlaklar soni oshdi,
  boʻlakning kattaligi esa oʻzgarmadi.</p>
  <p class="pe-ex__why">Demak butun son faqat <b>suratga</b> koʻpaytiriladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">5 × 1/10 = 5/10 = 1/2</p>
  <p class="pe-ex__uz">Beshta oʻndan bir — yarim.</p>
</div>

<h3>2. «Dan» soʻzi — bu koʻpaytirish</h3>

<p>Bu darsning kaliti. Matnli masalada <b>«…ning …qismi»</b> yoki
<b>«…ning …dan biri»</b> uchrasa, u koʻpaytirish demakdir.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Matnda shunday deyiladi</th><th>Matematikada</th><th>Misol</th></tr>
  <tr><td>yarmining uchdan biri</td><td class="pm-word__sym">1/2 × 1/3</td><td>= 1/6</td></tr>
  <tr><td>24 ning toʻrtdan uchi</td><td class="pm-word__sym">3/4 × 24</td><td>= 18</td></tr>
  <tr><td>3/4 kilogrammning yarmi</td><td class="pm-word__sym">1/2 × 3/4</td><td>= 3/8</td></tr>
</table></div>

<p>PM-15 da 24 ning 3/4 qismini ikki qadamda topgan edik (24 ÷ 4, keyin × 3). Endi
uning nomini ham bilamiz: bu koʻpaytirish edi.</p>

<h3>3. Kasrni kasrga koʻpaytirish</h3>

<p>Nodira opaning masalasi: <b>1/2 × 1/3</b>. Rasm hamma narsani aytib beradi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 330 170" role="img" aria-label="Yarimning uchdan biri — 1/6">
    <rect class="pm-ln" x="30" y="30" width="180" height="120" fill="none"/>
    <rect class="pm-fill" x="30" y="30" width="90" height="120"/>
    <rect class="pm-fill pm-fill--hl" x="30" y="30" width="90" height="40"/>
    <line class="pm-ln pm-ln--dash" x1="120" y1="30" x2="120" y2="150"/>
    <line class="pm-ln pm-ln--dash" x1="30" y1="70" x2="210" y2="70"/>
    <line class="pm-ln pm-ln--dash" x1="30" y1="110" x2="210" y2="110"/>
    <text class="pm-lbl" x="55" y="22">yarmi</text>
    <text class="pm-lbl pm-lbl--hl" x="45" y="57">1/6</text>
    <text class="pm-lbl" x="228" y="55">uchga</text>
    <text class="pm-lbl" x="228" y="75">boʻlindi</text>
  </svg>
  <figcaption>Butun avval ikkiga, keyin uchga boʻlindi — jami oltita teng katak.
  Boʻyalgan katak — yarmining uchdan biri.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">1/2 × 1/3</span>
    <span class="pm-solve__why">«Yarmining uchdan biri»</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= (1 × 1)/(2 × 3)</span>
    <span class="pm-solve__why">Surat suratga, maxraj maxrajga</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 1/6 stakan</span>
    <span class="pm-solve__why">Butun oltita katakka boʻlindi, bittasi kerak</span>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">3/4 × 2/3 = 6/12 = 1/2</p>
  <p class="pe-ex__uz">Suratlar: 3 × 2 = 6. Maxrajlar: 4 × 3 = 12. Keyin
  qisqartirdik.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Koʻpaytirdik — lekin kichraydi!</p>
  <p>Butun sonlarda koʻpaytirish sonni oshiradi: 6 × 3 = 18. Kasrda esa teskarisi
  boʻlishi mumkin: 1/2 × 1/3 = 1/6, yaʼni yarmidan ham kichik.</p>
  <p>Sabab oddiy: <b>1 dan kichik songa koʻpaytirish — boʻlakni olish demak.</b>
  «Yarmining uchdan biri» yarimdan kichik boʻlishi tabiiy.</p>
</div>

<h3>4. Kasrni butun songa boʻlish</h3>

<p>Yarim nonni <b>3</b> bolaga teng boʻlsak, har biriga qancha tegadi? Yarim non yana
uchga boʻlinadi — yaʼni butun oltiga boʻlingan boʻladi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">1/2 ÷ 3</span>
    <span class="pm-solve__why">Yarim non uch bolaga</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 1/6</span>
    <span class="pm-solve__why">Boʻlaklar soni oshdi, demak maxraj 3 barobar
    kattalashdi</span>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">3/4 ÷ 3 = 1/4</p>
  <p class="pe-ex__uz">3/4 kilogramm guruch uch kishiga — har biriga 1/4 kilogramm.
  Bu yerda surat 3 ga boʻlindi.</p>
</div>

<h3>5. Kasrga boʻlish — «nechtasi sigʻadi?»</h3>

<p>Boʻlishning ikkinchi maʼnosi bor va u aynan shu yerda kerak boʻladi:
<b>nechta marta sigʻadi?</b></p>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Savol</p>
  <p>Yarim litr sut bor. Har bir chashka <b>1/6</b> litr sigʻdiradi. Nechta chashka
  toʻldiriladi?</p>
</div>

<div class="pm-num">
  <div class="pm-num__track">
    <span class="pm-num__band" style="left:0%;width:50%"></span>
    <span class="pm-num__tick" style="left:0%"><i>0</i></span>
    <span class="pm-num__tick" style="left:16.6%"><i>1/6</i></span>
    <span class="pm-num__tick" style="left:33.3%"><i>2/6</i></span>
    <span class="pm-num__tick" style="left:50%"><i>1/2</i></span>
    <span class="pm-num__tick" style="left:100%"><i>1</i></span>
  </div>
</div>

<p>Son oʻqida sanaymiz: 1/6, 2/6, 3/6 — uchinchi belgida yarimga yetdik. Demak
<b>1/2 ÷ 1/6 = 3</b>. Javob butun son chiqdi, chunki savol «nechta boʻlak?»
degan edi.</p>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Qoida</p>
  <p>Birlik kasrga boʻlish — uning <b>maxrajiga koʻpaytirish</b> demak:
  <br>÷ 1/6 &nbsp;=&nbsp; × 6 &nbsp;·&nbsp; ÷ 1/4 &nbsp;=&nbsp; × 4.</p>
  <p>Chunki bitta butunda oltita 1/6 bor. Boʻlaklar qancha kichik boʻlsa, ular
  shuncha koʻp sigʻadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">3/4 ÷ 1/4 = 3/4 × 4 = 3</p>
  <p class="pe-ex__uz">3/4 kilogramm unda nechta 1/4 kilogrammlik paket bor? Uchta.</p>
</div>

<h3>6. Matnli masala</h3>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Masala</p>
  <p>Retsept <b>6 kishiga</b> moʻljallangan: <b>1/2 stakan yogʻ</b> va <b>3/4 kg
  guruch</b>. Nodira opa <b>2 kishiga</b> osh damlamoqchi. Unga qancha yogʻ va qancha
  guruch kerak?</p>
</div>

<p><b>Nima soʻralyapti?</b> Ikkita miqdor. <b>Reja:</b> 2 kishi — 6 kishining uchdan
biri, demak har bir mahsulotning 1/3 qismini olamiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2 ÷ 6 = 1/3</span>
    <span class="pm-solve__why">Retseptning qaysi qismi kerakligini topdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">1/3 × 1/2 = 1/6 stakan</span>
    <span class="pm-solve__why">Yogʻ: yarimning uchdan biri</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">1/3 × 3/4 = 3/12 = 1/4 kg</span>
    <span class="pm-solve__why">Guruch: 3/4 ning uchdan biri</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Teskari yoʻldan yuramiz: agar bir ulush 1/6 stakan boʻlsa, uchta ulush
  3 × 1/6 = 3/6 = 1/2 stakan beradi ✓ Guruch: 3 × 1/4 = 3/4 kg ✓ Ikkalasi ham
  retseptga qaytdi.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Odam soni uch barobar kamaydi, demak mahsulot ham taxminan uch barobar
  kamayishi kerak. 1/2 dan 1/6 ga, 3/4 dan 1/4 ga — ikkalasi ham roppa-rosa uch
  barobar. Mantiqiy.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">1/2 × 1/3 = 2/6</p>
  <p class="pe-fix__good">1/2 × 1/3 = 1/6</p>
  <p class="pe-fix__why">Koʻpaytirishda suratlar ham koʻpaytiriladi: 1 × 1 = 1,
  qoʻshilmaydi. 2/6 javobi suratlarni qoʻshib yuborganda chiqadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">1/2 × 1/3 &gt; 1/2, chunki koʻpaytirdik</p>
  <p class="pe-fix__good">1/2 × 1/3 &lt; 1/2</p>
  <p class="pe-fix__why">1 dan kichik songa koʻpaytirish natijani <b>kichraytiradi</b>.
  «Yarmining uchdan biri» yarimdan katta boʻlishi mumkin emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">1/2 ÷ 3 = 3/2</p>
  <p class="pe-fix__good">1/2 ÷ 3 = 1/6</p>
  <p class="pe-fix__why">Boʻlish ulushni kichraytiradi. Yarim nonni uchga boʻlsangiz,
  har kimga yarimdan kam tegishi kerak.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 4 × 1/9 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>4/9.</b> Butun son faqat suratga koʻpaytiriladi — boʻlaklar soni oshadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 2/3 × 1/2 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>1/3.</b> (2 × 1)/(3 × 2) = 2/6, qisqartirsak 1/3. «Uchdan ikkining yarmi —
    uchdan bir» — mantiqan ham toʻgʻri.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 2/5 × 5/6 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>1/3.</b> (2 × 5)/(5 × 6) = 10/30, EKUB(10, 30) = 10, demak 1/3.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 1/2 ÷ 1/8 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>4.</b> Savol: yarimga nechta 1/8 sigʻadi? 1/2 = 4/8, demak toʻrtta.
    Qoida bilan: ÷ 1/8 = × 8, 1/2 × 8 = 4.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Bir bogʻ yerning 3/4 qismi ekilgan. Ekilgan qismning 1/3 i
  — pomidor. Pomidor butun yerning qaysi qismini egallaydi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>1/4.</b> «Ekilgan qismning uchdan biri» — bu 1/3 × 3/4 = 3/12 = 1/4.
    Diqqat: 1/3 butun yerdan emas, faqat ekilgan qismdan olindi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Koʻpaytma</b><span>koʻpaytirish natijasi; ingl. product</span></li>
  <li><b>Boʻlinma</b><span>boʻlish natijasi; ingl. quotient</span></li>
  <li><b>Birlik kasr</b><span>surati 1 boʻlgan kasr: 1/6, 1/8; ingl. unit
    fraction</span></li>
  <li><b>Kasrning qismi</b><span>«…ning …qismi» — koʻpaytirish bilan topiladi;
    ingl. fraction of</span></li>
  <li><b>Qisqartirish</b><span>javobni eng sodda koʻrinishga keltirish;
    ingl. simplifying</span></li>
  <li><b>Teskari amal</b><span>koʻpaytirishni bekor qiluvchi boʻlish;
    ingl. inverse operation</span></li>
  <li><b>Ulush</b><span>bir kishiga yoki bir qismga tegadigan miqdor;
    ingl. share</span></li>
  <li><b>Retsept</b><span>miqdorlari kasr bilan berilgan tayyorlash tartibi;
    ingl. recipe</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Koʻpaytirish: surat suratga, maxraj maxrajga,</b> keyin qisqartiring.</li>
    <li><b>«…ning …qismi» — koʻpaytirish.</b> Va 1 dan kichik songa koʻpaytirish
      natijani kichraytiradi.</li>
    <li><b>Birlik kasrga boʻlish — maxrajiga koʻpaytirish:</b> ÷ 1/6 = × 6, chunki
      savol «nechtasi sigʻadi?» degani.</li>
  </ul>
</div>
""",
    },
]
