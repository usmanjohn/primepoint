# -*- coding: utf-8 -*-
"""Prime GMAT — GMAT-6 … GMAT-10: fractions and decimals, remainders, exponents and
roots, units digits, ratios and proportions.

Written with STYLE_GUIDE_PRIME_GMAT.md (on top of STYLE_GUIDE_PRIME_SAT.md) ·
lesson list in toc_prime_gmat.txt. Exam English in the stems, Uzbek for the teaching.
Five answer choices, no calculator, no geometry, no data sufficiency.

Import:
    python manage.py import_tutorials tutorial/management/commands/_tutorials_prime_gmat_06_10.py --author=prime
"""

PLAYLIST = {
    "title": "Prime GMAT",
    "category": "math",
    "description": (
        "GMAT Focus Edition'ning Quant boʻlimi — biznes maktabiga yoʻl. Savollar ingliz "
        "tilida, chunki imtihon shunday; tushuntirish oʻzbek tilida. Har bir darsda "
        "haqiqiy GMAT uslubidagi savollar, tuzoq javoblar va 20 savollik mashq."
    ),
}

GMAT6 = """
<h2>GMAT-6: Fractions and Decimals Without a Calculator</h2>

<p>GMAT kasrlarni yaxshi koʻradi, chunki kalkulyatorsiz ularni <mark>tez solishtirish</mark>
koʻnikmani tekshiradi. Bu darsda kasr va oʻnli kasr orasida bir zumda oʻtish, ikki kasrni
koʻpaytmalar orqali solishtirish va oʻnli kasrga boʻlishni oddiy boʻlishga aylantirishni
oʻrganamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>eng koʻp uchraydigan kasrlarning oʻnli koʻrinishini yoddan bilasiz;</li>
    <li>ikki kasrni oʻzaro koʻpaytirish (<i>cross-multiplication</i>) bilan solishtirasiz;</li>
    <li>oʻnli kasrga boʻlishda vergulni xatosiz koʻchirasiz;</li>
    <li>kasr qachon chekli oʻnli kasr boʻlishini aytib berasiz.</li>
  </ul>
</div>

<h3>Yoddan bilish kerak boʻlgan jadval</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Kasr</th><th>Oʻnli kasr</th><th>Kasr</th><th>Oʻnli kasr</th></tr>
  <tr><td>1/2</td><td class="pm-word__sym">0.5</td><td>1/8</td><td class="pm-word__sym">0.125</td></tr>
  <tr><td>1/3</td><td class="pm-word__sym">0.333…</td><td>3/8</td><td class="pm-word__sym">0.375</td></tr>
  <tr><td>1/4</td><td class="pm-word__sym">0.25</td><td>5/8</td><td class="pm-word__sym">0.625</td></tr>
  <tr><td>1/5</td><td class="pm-word__sym">0.2</td><td>7/8</td><td class="pm-word__sym">0.875</td></tr>
  <tr><td>1/6</td><td class="pm-word__sym">0.1666…</td><td>1/9</td><td class="pm-word__sym">0.111…</td></tr>
  <tr><td>1/20</td><td class="pm-word__sym">0.05</td><td>1/25</td><td class="pm-word__sym">0.04</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu jadvalni bilish — vaqt. «0.375 × 64» koʻrsangiz, <b>3/8 × 64 = 24</b> deb oʻqiysiz va
  ustunda koʻpaytirmaysiz. Imtihondan oldin sakkizdan birlarni (1/8, 3/8, 5/8, 7/8) albatta
  yodlang — GMAT ularni ayniqsa koʻp ishlatadi.
</div>

<h3>Ikki kasrni solishtirish — oʻzaro koʻpaytirish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">5/8 ? 7/11</span>
    <span class="pm-solve__why">Umumiy maxraj topish shart emas</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5 × 11 = 55; 7 × 8 = 56</span>
    <span class="pm-solve__why">Har bir surat qarshidagi maxrajga koʻpaytiriladi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">55 &lt; 56 → 5/8 &lt; 7/11</span>
    <span class="pm-solve__why">Kattaroq koʻpaytma tomondagi kasr kattaroq</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Beshta kasrdan eng kattasini topish kerak boʻlsa, avval <b>1/2 bilan solishtiring</b>:
  yarmidan kichiklari darrov chiqib ketadi. Qolgan ikki-uchtasini oʻzaro koʻpaytirish bilan
  solishtiring.
</div>

<h3>Oʻnli kasrga boʻlish — vergulni yoʻqoting</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">0.36 ÷ 0.004</span>
    <span class="pm-solve__why">Boʻluvchida uchta oʻnli xona bor</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= 360 ÷ 4</span>
    <span class="pm-solve__why">Ikkala sonni 1,000 ga koʻpaytirdik — boʻlinma oʻzgarmaydi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">90</span>
    <span class="pm-solve__why">Endi oddiy boʻlish</span>
  </div>
</div>

<h3>Kasrga boʻlish — teskarisiga koʻpaytirish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2/3 ÷ 4/9 = 2/3 × 9/4</span>
    <span class="pm-solve__why">Ikkinchi kasr agʻdariladi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 18/12 = 3/2 = 1.5</span>
    <span class="pm-solve__why">Qisqartiramiz</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Kasr qachon <b>chekli oʻnli kasr</b> (<i>terminating decimal</i>) boʻladi? Qisqartirilgan
  kasrning maxrajida faqat 2 va 5 qatnashsa. 7/20 = 0.35 (20 = 2 × 2 × 5) — chekli;
  1/6 = 0.1666… (6 da 3 bor) — cheksiz.
</div>

<h3>Kasr, foiz va oʻnli kasr — bitta son, uch xil yozuv</h3>

<p>GMAT bir savolning ichida uchala yozuvni aralashtirib yuboradi: «3/8 of the budget»,
«a 37.5% share», «0.375 of the total» — bu bitta son. Foizga oʻtish uchun oʻnli kasrni
100 ga koʻpaytiring: 0.375 = 37.5%. Teskarisiga — 100 ga boʻling: 12.5% = 0.125 = 1/8.
Shuning uchun yuqoridagi jadval foiz masalalarida ham ishlaydi: 87.5% — bu 7/8, demak
«87.5% of 640» = 640 ÷ 8 × 7 = 560.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Hisobni qaysi yozuvda qilishni <b>oʻzingiz tanlang</b>. 0.375 × 64 ni ustunda koʻpaytirish
  qiyin, 3/8 × 64 esa ogʻzaki: 64 ÷ 8 = 8, 8 × 3 = 24. Aksincha, 0.2 + 0.15 kabi qoʻshishda
  oʻnli kasr qulayroq. Qoida oddiy: koʻpaytirish va boʻlishda — kasr, qoʻshish va ayirishda —
  oʻnli kasr.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>which of the following is greatest</b><span>quyidagilardan qaysi biri eng katta</span></li>
  <li><b>numerator / denominator</b><span>surat / maxraj</span></li>
  <li><b>reciprocal</b><span>teskari son: 3/4 ning teskarisi 4/3</span></li>
  <li><b>terminating decimal</b><span>chekli oʻnli kasr</span></li>
  <li><b>what fraction of … remains</b><span>… ning qancha qismi qoldi</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>Which of the following is greatest?</p>
  </div>
  <ol class="ps-ch">
    <li>9/16</li>
    <li>3/5</li>
    <li>5/8</li>
    <li>7/11</li>
    <li>13/20</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: E) 13/20</p>
      <p>13/20 = 0.65, 7/11 = 0.636…, 5/8 = 0.625, 3/5 = 0.6, 9/16 = 0.5625. Eng yaqin ikkitasini
      oʻzaro koʻpaytirish bilan tekshiring: 13 × 11 = 143, 7 × 20 = 140 — 13/20 katta.</p>
      <p><b>7/11</b> — «katta maxraj — katta kasr» deb oʻylagan javob.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">7/11</span>
  <span class="ps-trap__why">Sonlarning kattaligi kasrning kattaligi emas. Kasrni faqat
  surat va maxrajni birga koʻrib baholash mumkin.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>What is the value of 0.36 ÷ 0.004?</p>
  </div>
  <ol class="ps-ch">
    <li>0.9</li>
    <li>9</li>
    <li>90</li>
    <li>900</li>
    <li>9,000</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 90</p>
      <p>Ikkalasini 1,000 ga koʻpaytiramiz: 360 ÷ 4 = 90.</p>
      <p><b>9</b> — faqat ikki xonaga surilgan javob (36 ÷ 4).</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">9</span>
  <span class="ps-trap__why">Vergulni boʻluvchidagi xonalar soniga qarab suring: 0.004 da
  uchta xona — demak 1,000 ga koʻpaytirasiz, 100 ga emas.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Oʻnli kasrli hisobda <b>javobning tartibini</b> avval baholang:</p>
  <ol>
    <li>0.36 ÷ 0.004 — kichik sonni juda kichik songa boʻlish, demak natija kattalashadi;</li>
    <li>javobni orqaga tekshiring: 90 × 0.004 = 0.36 ✓;</li>
    <li>variantlar 10 barobar farq qilsa, aniq raqamlar emas, faqat tartib muhim.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">1/2 + 1/3 = 2/5</p>
  <p class="pe-good">1/2 + 1/3 = 3/6 + 2/6 = 5/6</p>
  <p class="pe-fix__why">Kasrlarni qoʻshishda suratlar va maxrajlar alohida qoʻshilmaydi — umumiy maxraj kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">3/4 ÷ 3/8 = 9/32</p>
  <p class="pe-good">3/4 × 8/3 = 2</p>
  <p class="pe-fix__why">Boʻlishda ikkinchi kasr agʻdariladi; 9/32 — koʻpaytma.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «2/5 of a number is 18» — avval butun sonni toping (18 ÷ 2/5 = 45), keyin soʻralgan
  qismini oling. Toʻgʻridan-toʻgʻri kasrdan kasrga oʻtishga urinish koʻpincha xatoga olib keladi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> What is 3/8 as a decimal?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">0.375 — 1/8 = 0.125, uch marta.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> What is 0.125 × 72?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">9 — 0.125 = 1/8, 72 ÷ 8 = 9.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> What is 2/3 ÷ 4/9?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">1.5 — 2/3 × 9/4 = 18/12 = 3/2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> Which is greater, 4/7 or 5/9?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">4/7 — 4 × 9 = 36, 5 × 7 = 35.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> A project budget of $2,400 spends
  3/8 on design. How much is spent on design?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">$900 — 2,400 ÷ 8 = 300, 300 × 3 = 900.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>fraction</b><span>kasr</span></li>
  <li><b>numerator</b><span>surat</span></li>
  <li><b>denominator</b><span>maxraj</span></li>
  <li><b>reciprocal</b><span>teskari son</span></li>
  <li><b>decimal place</b><span>oʻnli xona</span></li>
  <li><b>terminating decimal</b><span>chekli oʻnli kasr</span></li>
  <li><b>cross-multiply</b><span>oʻzaro koʻpaytirmoq</span></li>
  <li><b>budget</b><span>byudjet</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Sakkizdan birlarni yodlang: 0.125, 0.375, 0.625, 0.875.</li>
    <li>Ikki kasr — oʻzaro koʻpaytiring; beshta kasr — avval 1/2 bilan solishtiring.</li>
    <li>Oʻnli kasrga boʻlishda ikkala sonni 10, 100, 1,000 ga koʻpaytiring.</li>
    <li>Kasrga boʻlish = teskarisiga koʻpaytirish.</li>
    <li>Chekli oʻnli kasr — qisqartirilgan maxrajda faqat 2 va 5.</li>
  </ul>
</div>
"""

GMAT7 = """
<h2>GMAT-7: Remainders and Divisibility Patterns</h2>

<p>Qoldiq — boʻlishdan «ortib qolgan» qism. GMAT uni <mark>hafta kunlari, qadoqlash va
navbat</mark> masalalariga yashiradi. Qoldiqlarning bitta ajoyib xususiyati bor: ular bilan
xuddi sonlar kabi qoʻshish va koʻpaytirish mumkin — bu katta sonlarni hisoblamasdan javob
topishga imkon beradi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>boʻlishni <i>n</i> = boʻluvchi × boʻlinma + qoldiq koʻrinishida yozasiz;</li>
    <li>qoldiq doim boʻluvchidan kichik ekanini tekshiruv sifatida ishlatasiz;</li>
    <li>qoldiqlarni qoʻshib va koʻpaytirib, katta sonning qoldigʻini topasiz;</li>
    <li>«necha kundan keyin qaysi kun» masalasini 7 ga boʻlish bilan yechasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Division with remainder</span>
  <span class="pe-chip pe-chip--o">n</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">d × q</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">r</span>
  <span class="pe-op">, 0 ≤ r &lt; d</span>
</div>

<p>47 ni 6 ga boʻlsak: 47 = 6 × 7 + 5, qoldiq 5. Qoldiq <b>har doim 0 dan boʻluvchigacha</b>:
6 ga boʻlganda qoldiq faqat 0, 1, 2, 3, 4 yoki 5 boʻlishi mumkin.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Kichik sonni katta songa boʻlsangiz, qoldiq — sonning oʻzi: 3 ni 8 ga boʻlganda boʻlinma 0,
  qoldiq 3. Bizda koʻpchilik bu yerda «qoldiq 0» yoki «boʻlinmaydi» deb javob beradi.
</div>

<h3>Qoldiq berilgan sonlar — roʻyxat tuzing</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">«n leaves a remainder of 2 when divided by 5»</span>
    <span class="pm-solve__why">n = 5k + 2</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">n = 2, 7, 12, 17, 22, …</span>
    <span class="pm-solve__why">2 dan boshlab har safar 5 qoʻshamiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Eng kichik musbat qiymat: 2</span>
    <span class="pm-solve__why">k = 0 ham ruxsat — 2 = 5 × 0 + 2</span>
  </div>
</div>

<h3>Qoldiqlar bilan hisoblash</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">n ÷ 6 → qoldiq 4. 2n ÷ 6 → ?</span>
    <span class="pm-solve__why">n ni bilmaymiz — kerak ham emas</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2 × 4 = 8</span>
    <span class="pm-solve__why">Qoldiqni koʻpaytiramiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">8 = 6 + 2 → qoldiq 2</span>
    <span class="pm-solve__why">8 boʻluvchidan katta — yana bir marta boʻlamiz</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Tekshirish uchun eng kichik misol sonni oling: n = 4 (4 ni 6 ga boʻlsak qoldiq 4).
  2n = 8, 8 ni 6 ga boʻlsak qoldiq 2 ✓. Bitta aniq son — eng ishonchli tekshiruv.
</div>

<h3>Hafta kunlari — 7 ga boʻlish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Bugun dushanba. 100 kundan keyin?</span>
    <span class="pm-solve__why">Har 7 kunda yana dushanba</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">100 = 7 × 14 + 2</span>
    <span class="pm-solve__why">14 toʻliq hafta va yana 2 kun</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Dushanba + 2 kun = chorshanba</span>
    <span class="pm-solve__why">Faqat qoldiq hal qiladi</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «100 days from today» — bugundan <b>keyin</b> 100 kun. Bugunni birinchi kun deb sanamang:
  1 kundan keyin — seshanba, 7 kundan keyin — yana dushanba.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Navbat bilan» (<i>in rotation</i>) masalalari ham qoldiq masalasi: 6 ta stolga 200 ta
  chipta navbat bilan berilsa, 200-chipta qaysi stolga tushishini 200 ni 6 ga boʻlishdagi
  qoldiq aytadi (2 → 2-stol). Bitta nozik joy bor: <b>qoldiq 0 boʻlsa, oxirgi stol</b>
  (6-stol), «0-stol» emas. Hafta kunlarida ham shunday: qoldiq 0 — bugungi kunning oʻzi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>leaves a remainder of 3 when divided by 7</b><span>7 ga boʻlganda qoldiq 3</span></li>
  <li><b>quotient</b><span>boʻlinma — necha marta sigʻishi</span></li>
  <li><b>is evenly divisible</b><span>qoldiqsiz boʻlinadi</span></li>
  <li><b>days from today</b><span>bugundan keyin … kun</span></li>
  <li><b>as evenly as possible</b><span>iloji boricha teng</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>When the positive integer <i>n</i> is divided by 6, the remainder is 4. What is the
    remainder when 2<i>n</i> is divided by 6?</p>
  </div>
  <ol class="ps-ch">
    <li>0</li>
    <li>2</li>
    <li>4</li>
    <li>6</li>
    <li>8</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 2</p>
      <p>Qoldiqni ikkiga koʻpaytiramiz: 8, keyin 8 ni 6 ga boʻlamiz — qoldiq 2.
      Tekshiruv: n = 10, 2n = 20 = 6 × 3 + 2 ✓.</p>
      <p><b>8</b> — qoldiqni koʻpaytirib, yana boʻlishni unutgan javob.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">8</span>
  <span class="ps-trap__why">6 ga boʻlganda qoldiq 6 yoki undan katta boʻlolmaydi. 6 va 8 —
  bu variantlarni qoldiq qoidasining oʻzi chiqarib tashlaydi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>If today is Monday, what day of the week will it be 100 days from today?</p>
  </div>
  <ol class="ps-ch">
    <li>Tuesday</li>
    <li>Wednesday</li>
    <li>Thursday</li>
    <li>Friday</li>
    <li>Saturday</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) Wednesday</p>
      <p>100 = 7 × 14 + 2. 14 hafta oʻtib yana dushanba, keyin 2 kun — chorshanba.</p>
      <p><b>Tuesday</b> — bugunni birinchi kun deb sanagan javob.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">Tuesday</span>
  <span class="ps-trap__why">Bir kunlik siljish. Kichik misol bilan tekshiring: «1 day from
  Monday» — seshanba, yaʼni qoldiq 1 bir kun oldinga suradi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Qoldiq savolida <b>shartga mos eng kichik sonni</b> qoʻying:</p>
  <ol>
    <li>«n ÷ 6 → qoldiq 4» — n = 4 deb oling;</li>
    <li>soʻralgan ifodani shu son bilan hisoblang;</li>
    <li>shubha boʻlsa, ikkinchi son bilan (n = 10) takrorlang — javob bir xil chiqishi kerak.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">3 ÷ 8 → qoldiq 0</p>
  <p class="pe-good">3 ÷ 8 → boʻlinma 0, qoldiq 3</p>
  <p class="pe-fix__why">8 soni 3 ning ichiga bir marta ham sigʻmaydi — butun 3 qoldiq boʻlib qoladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">2n ÷ 6 → qoldiq 8</p>
  <p class="pe-good">qoldiq 2</p>
  <p class="pe-fix__why">Qoldiq boʻluvchidan kichik boʻlishi shart; 8 dan yana bitta 6 ni ayiring.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> What is the remainder when 47 is divided by 6?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">5 — 47 = 6 × 7 + 5.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> What is the smallest integer greater than 20
  that leaves a remainder of 3 when divided by 5?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">23 — 3, 8, 13, 18, 23.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> What is the remainder when 3 is divided by 8?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">3 — boʻlinma 0, butun son qoldiq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> When <i>n</i> is divided by 7, the remainder
  is 3. What is the remainder when <i>n</i> + 5 is divided by 7?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">1 — 3 + 5 = 8 = 7 + 1.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> A supplier packs 250 products in boxes
  of 12. How many products are left over?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">10 — 12 × 20 = 240, 250 − 240 = 10.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>remainder</b><span>qoldiq</span></li>
  <li><b>quotient</b><span>boʻlinma</span></li>
  <li><b>divisor</b><span>boʻluvchi</span></li>
  <li><b>dividend</b><span>boʻlinuvchi</span></li>
  <li><b>evenly</b><span>qoldiqsiz, teng</span></li>
  <li><b>day of the week</b><span>hafta kuni</span></li>
  <li><b>left over</b><span>ortib qolgan</span></li>
  <li><b>in rotation</b><span>navbat bilan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>n = d × q + r va har doim 0 ≤ r &lt; d.</li>
    <li>Kichik sonni katta songa boʻlsangiz, qoldiq — sonning oʻzi.</li>
    <li>Qoldiqlarni qoʻshing yoki koʻpaytiring, keyin yana boʻluvchiga boʻling.</li>
    <li>Hafta kunlari — 7 ga boʻlishdagi qoldiq; bugunni sanamang.</li>
    <li>Shartga mos eng kichik sonni qoʻyib tekshiring.</li>
  </ul>
</div>
"""

GMAT8 = """
<h2>GMAT-8: Exponents and Roots</h2>

<p>Daraja va ildiz savollarida GMAT sizdan katta son hisoblashni deyarli hech qachon
soʻramaydi. Uning sevimli usuli — <mark>har xil asoslarni bitta asosga keltirish</mark>:
8, 16 va 32 — hammasi 2 ning darajalari. Buni koʻrsangiz, murakkab koʻrinadigan ifoda bir
qatorda yechiladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>daraja qoidalarini (koʻpaytirish, boʻlish, darajaga koʻtarish) adashtirmaysiz;</li>
    <li>asoslarni bir xil qilib, darajali tenglamani yechasiz;</li>
    <li>ildizni soddalashtirasiz: √50 = 5√2;</li>
    <li>manfiy asos va manfiy daraja tuzoqlarini tanib olasiz.</li>
  </ul>
</div>

<h3>Daraja qoidalari</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Qoida</th><th>Misol</th></tr>
  <tr><td>a<sup>m</sup> × a<sup>n</sup> = a<sup>m + n</sup></td><td class="pm-word__sym">2<sup>3</sup> × 2<sup>4</sup> = 2<sup>7</sup></td></tr>
  <tr><td>a<sup>m</sup> ÷ a<sup>n</sup> = a<sup>m − n</sup></td><td class="pm-word__sym">3<sup>8</sup> ÷ 3<sup>6</sup> = 3<sup>2</sup> = 9</td></tr>
  <tr><td>(a<sup>m</sup>)<sup>n</sup> = a<sup>mn</sup></td><td class="pm-word__sym">(3<sup>2</sup>)<sup>3</sup> = 3<sup>6</sup></td></tr>
  <tr><td>a<sup>0</sup> = 1</td><td class="pm-word__sym">5<sup>0</sup> = 1</td></tr>
  <tr><td>a<sup>−n</sup> = 1/a<sup>n</sup></td><td class="pm-word__sym">2<sup>−3</sup> = 1/8</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Daraja qoidalari <b>faqat koʻpaytirish va boʻlishda</b> ishlaydi. 2<sup>3</sup> + 2<sup>3</sup> ≠ 2<sup>6</sup>:
  bu 8 + 8 = 16 = 2<sup>4</sup>. Qoʻshishda umumiy koʻpaytuvchini chiqaring: 2<sup>3</sup>(1 + 1).
</div>

<h3>Asosni bir xil qilish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2<sup><i>x</i></sup> = 8<sup>4</sup></span>
    <span class="pm-solve__why">8 ni 2 ning darajasi sifatida yozamiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">8<sup>4</sup> = (2<sup>3</sup>)<sup>4</sup> = 2<sup>12</sup></span>
    <span class="pm-solve__why">Darajani darajaga koʻtarishda koʻpaytiramiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step"><i>x</i> = 12</span>
    <span class="pm-solve__why">Asoslar teng — darajalar ham teng</span>
  </div>
</div>

<h3>Ifodani soddalashtirish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">(3<sup>5</sup> × 3<sup>3</sup>) ÷ 9<sup>3</sup></span>
    <span class="pm-solve__why">Hammasini 3 ga keltiramiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3<sup>8</sup> ÷ 3<sup>6</sup></span>
    <span class="pm-solve__why">9<sup>3</sup> = (3<sup>2</sup>)<sup>3</sup> = 3<sup>6</sup></span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3<sup>2</sup> = 9</span>
    <span class="pm-solve__why">Boʻlishda darajalar ayiriladi</span>
  </div>
</div>

<h3>Ildizlar</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">√50 = √(25 × 2)</span>
    <span class="pm-solve__why">Eng katta toʻliq kvadrat boʻluvchini ajratamiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 5√2</span>
    <span class="pm-solve__why">√25 = 5 ildiz tashqarisiga chiqadi</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  √a × √b = √(ab), lekin <b>√(a + b) ≠ √a + √b</b>: √(9 + 16) = √25 = 5, 3 + 4 = 7 emas.
  GMAT bu tuzoqni deyarli har doim variantlar orasiga qoʻyadi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qavsga eʼtibor bering: <b>(−2)<sup>4</sup> = 16</b>, lekin <b>−2<sup>4</sup> = −16</b>. Qavssiz
  minus darajaga kirmaydi — avval 2<sup>4</sup> hisoblanadi, keyin minus qoʻyiladi.
</div>

<h3>Darajali oʻsish — biznes tilida</h3>

<p>GMAT darajalarni koʻpincha oʻsish masalasiga oʻraydi: «doubles every 6 years»,
«triples each year». Bunday jumlada har bir davr <b>koʻpaytirish</b>dir: 4 davr — 2<sup>4</sup>
= 16 baravar. Davrlar sonini toping (24 yil ÷ 6 yil = 4), keyin asosni shu darajaga koʻtaring.
Teskari savol ham uchraydi: ikki yilda 9 baravar oʻsgan boʻlsa, har yili 3 baravar oʻsgan,
chunki 3<sup>2</sup> = 9 — bu yerda daraja emas, ildiz kerak.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Har yili ikki baravar» va «har yili 100 taga oshdi» — butunlay boshqa narsa. Birinchisi
  koʻpaytirish (darajali oʻsish), ikkinchisi qoʻshish (chiziqli oʻsish). 1,000 dan boshlab
  5 yilda birinchisi 32,000 beradi, ikkinchisi atigi 1,500. Savolda «every», «each» va
  «times» soʻzlarini qidiring — ular koʻpaytirishni bildiradi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>exponent / power</b><span>daraja koʻrsatkichi</span></li>
  <li><b>base</b><span>asos</span></li>
  <li><b>square root</b><span>kvadrat ildiz</span></li>
  <li><b>doubles every 6 years</b><span>har 6 yilda ikki baravar oshadi — darajali oʻsish</span></li>
  <li><b>in simplest form</b><span>eng sodda koʻrinishda</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>If 2<sup><i>x</i></sup> = 8<sup>4</sup>, what is the value of <i>x</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>7</li>
    <li>8</li>
    <li>12</li>
    <li>16</li>
    <li>32</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 12</p>
      <p>8<sup>4</sup> = (2<sup>3</sup>)<sup>4</sup> = 2<sup>12</sup>, demak <i>x</i> = 12.</p>
      <p><b>7</b> — darajalarni koʻpaytirish oʻrniga qoʻshgan javob (3 + 4).</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">7</span>
  <span class="ps-trap__why">Darajani darajaga koʻtarishda koʻpaytiriladi; qoʻshish — bir xil
  asosli sonlarni koʻpaytirganda.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>What is the value of (3<sup>5</sup> × 3<sup>3</sup>) ÷ 9<sup>3</sup>?</p>
  </div>
  <ol class="ps-ch">
    <li>1/3</li>
    <li>1</li>
    <li>3</li>
    <li>9</li>
    <li>27</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: D) 9</p>
      <p>3<sup>8</sup> ÷ 3<sup>6</sup> = 3<sup>2</sup> = 9.</p>
      <p><b>1/3</b> — 9<sup>3</sup> ni 3<sup>9</sup> deb yozgan javob: asos va daraja koʻpaytirib yuborilgan.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">1/3</span>
  <span class="ps-trap__why">9<sup>3</sup> = 3<sup>6</sup>, 3<sup>9</sup> emas. Asosni almashtirganda faqat
  daraja koʻrsatkichi oʻzgaradi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Darajali savolda <b>hamma narsani eng kichik asosga</b> keltiring:</p>
  <ol>
    <li>4, 8, 16, 32 → 2; 9, 27, 81 → 3; 25, 125 → 5;</li>
    <li>koʻpaytirish va boʻlishni darajalar ustida bajaring;</li>
    <li>oxirida faqat kichik darajani hisoblang (3<sup>2</sup> = 9).</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">2<sup>3</sup> + 2<sup>3</sup> = 2<sup>6</sup></p>
  <p class="pe-good">2<sup>3</sup> + 2<sup>3</sup> = 2 × 2<sup>3</sup> = 2<sup>4</sup></p>
  <p class="pe-fix__why">Qoʻshishda darajalar qoʻshilmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">√(9 + 16) = 3 + 4 = 7</p>
  <p class="pe-good">√25 = 5</p>
  <p class="pe-fix__why">Ildiz yigʻindiga boʻlinmaydi — avval yigʻindini hisoblang.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> What is 5<sup>3</sup> × 5<sup>−1</sup>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">25 — 5<sup>3 − 1</sup> = 5<sup>2</sup>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> Simplify √72.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">6√2 — 72 = 36 × 2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> What is 2<sup>10</sup>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">1,024 — buni yodlab qoʻying, 2<sup>10</sup> ≈ 1,000.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> What is (−3)<sup>3</sup>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Manfiy 27 — toq daraja manfiy ishorani saqlaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> An investment of $5,000 doubles every
  6 years. What is it worth after 24 years?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">$80,000 — 24 ÷ 6 = 4 marta ikki baravar: 5,000 × 2<sup>4</sup>.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>exponent</b><span>daraja koʻrsatkichi</span></li>
  <li><b>base</b><span>asos</span></li>
  <li><b>power</b><span>daraja</span></li>
  <li><b>square root</b><span>kvadrat ildiz</span></li>
  <li><b>perfect square</b><span>toʻliq kvadrat</span></li>
  <li><b>to double</b><span>ikki baravar oshmoq</span></li>
  <li><b>to triple</b><span>uch baravar oshmoq</span></li>
  <li><b>growth factor</b><span>oʻsish koeffitsiyenti</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Koʻpaytirishda darajalar qoʻshiladi, darajaga koʻtarishda koʻpaytiriladi.</li>
    <li>Asoslarni bir xil qiling: 8 = 2<sup>3</sup>, 9 = 3<sup>2</sup>.</li>
    <li>a<sup>0</sup> = 1, a<sup>−n</sup> = 1/a<sup>n</sup>.</li>
    <li>√(a + b) ≠ √a + √b; √50 = 5√2.</li>
    <li>(−2)<sup>4</sup> = 16, −2<sup>4</sup> = −16 — qavs hal qiladi.</li>
  </ul>
</div>
"""

GMAT9 = """
<h2>GMAT-9: Units Digits and Cyclicity</h2>

<p>«What is the units digit of 7<sup>42</sup>?» — bu sonda 36 ta raqam bor, lekin oxirgi raqamini
topish uchun <mark>bitta raqam bilan</mark> ishlash kifoya. Darajalarning oxirgi raqamlari
takrorlanadi, va GMAT aynan shu takrorlanishni (<i>cyclicity</i>) bilishingizni tekshiradi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>koʻpaytmaning oxirgi raqamini faqat oxirgi raqamlar bilan topasiz;</li>
    <li>2, 3, 7, 8 ning 4 lik siklini va 4, 9 ning 2 lik siklini bilasiz;</li>
    <li>katta darajaning oxirgi raqamini daraja ÷ 4 qoldigʻi bilan topasiz;</li>
    <li>faktorialning oxiridagi nollarni sanaysiz.</li>
  </ul>
</div>

<h3>Faqat oxirgi raqam muhim</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">24 × 37 × 58 → oxirgi raqam?</span>
    <span class="pm-solve__why">Toʻliq koʻpaytma kerak emas</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4 × 7 = 28 → 8</span>
    <span class="pm-solve__why">Har qadamda faqat oxirgi raqamni saqlaymiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">8 × 8 = 64 → 4</span>
    <span class="pm-solve__why">Javob: 4</span>
  </div>
</div>

<h3>Oxirgi raqamlar sikli</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Oxirgi raqam</th><th>Darajalari (sikl uzunligi)</th></tr>
  <tr><td>2</td><td class="pm-word__sym">2, 4, 8, 6 (4)</td></tr>
  <tr><td>3</td><td class="pm-word__sym">3, 9, 7, 1 (4)</td></tr>
  <tr><td>7</td><td class="pm-word__sym">7, 9, 3, 1 (4)</td></tr>
  <tr><td>8</td><td class="pm-word__sym">8, 4, 2, 6 (4)</td></tr>
  <tr><td>4</td><td class="pm-word__sym">4, 6 (2)</td></tr>
  <tr><td>9</td><td class="pm-word__sym">9, 1 (2)</td></tr>
  <tr><td>0, 1, 5, 6</td><td class="pm-word__sym">oʻzgarmaydi (1)</td></tr>
</table></div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">7<sup>42</sup> → oxirgi raqam?</span>
    <span class="pm-solve__why">7 ning sikli: 7, 9, 3, 1 — uzunligi 4</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">42 = 4 × 10 + 2</span>
    <span class="pm-solve__why">Daraja ÷ 4 qoldigʻi — sikldagi oʻrin</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Ikkinchi oʻrin → 9</span>
    <span class="pm-solve__why">Qoldiq 0 boʻlsa — siklning <b>toʻrtinchi</b> oʻrni</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Eng koʻp xato — <b>qoldiq 0</b> holati. 2<sup>40</sup>: 40 ÷ 4 qoldiq 0, demak siklning
  oxirgi elementi — 6, birinchisi (2) emas. Tekshiruv: 2<sup>4</sup> = 16 — oxiri 6 ✓.
</div>

<h3>Oxiridagi nollar</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">30! nechta nol bilan tugaydi?</span>
    <span class="pm-solve__why">Har bir nol — bitta 10 = 2 × 5</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">30 ÷ 5 = 6; 30 ÷ 25 = 1 (butun qismi)</span>
    <span class="pm-solve__why">5 lar kamroq — ularni sanaymiz; 25 ichida ikkita 5 bor</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">6 + 1 = 7 ta nol</span>
    <span class="pm-solve__why">2 lar har doim yetarli</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  <i>n</i>! (<i>n factorial</i>) — 1 dan <i>n</i> gacha boʻlgan sonlar koʻpaytmasi: 5! = 120.
  Nollar uchun: <i>n</i> ÷ 5 + <i>n</i> ÷ 25 + <i>n</i> ÷ 125 (har birining butun qismi).
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Yigʻindining oxirgi raqami ham faqat oxirgi raqamlardan chiqadi: 13<sup>3</sup> + 22<sup>2</sup> →
  7 + 4 = 11 → 1. Har bir qoʻshiluvchining oxirgi raqamini alohida toping, keyin qoʻshing.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Units digit</b> va <b>tens digit</b>ni adashtirmang: 3,847 da birlar raqami 7,
  oʻnlar raqami 4. GMAT baʼzan aynan oʻnlar raqamini soʻraydi — u holda oxirgi <b>ikki</b>
  raqam bilan ishlash kerak (24 × 37 → 888, oʻnlar raqami 8). Savolni oxirigacha oʻqing:
  «units» soʻzi boʻlmasa, sikl usuli yetarli emas.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>units digit</b><span>birlar xonasidagi raqam — oxirgi raqam</span></li>
  <li><b>tens digit</b><span>oʻnlar xonasidagi raqam</span></li>
  <li><b>trailing zeros</b><span>oxiridagi nollar</span></li>
  <li><b>n! (n factorial)</b><span>1 × 2 × … × n</span></li>
  <li><b>ends in</b><span>… bilan tugaydi</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>What is the units digit of 7<sup>42</sup>?</p>
  </div>
  <ol class="ps-ch">
    <li>1</li>
    <li>3</li>
    <li>5</li>
    <li>7</li>
    <li>9</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: E) 9</p>
      <p>Sikl 7, 9, 3, 1; 42 ÷ 4 qoldiq 2 → ikkinchi element, 9.</p>
      <p><b>1</b> — «juft daraja — 1» deb oʻylagan javob. Bu faqat 4 ga boʻlinadigan darajada toʻgʻri.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">1</span>
  <span class="ps-trap__why">7 ning sikli 4 lik, 2 lik emas. 42 juft, lekin 4 ga boʻlinmaydi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>How many zeros are at the end of 30!, the product of the integers from 1 to 30?</p>
  </div>
  <ol class="ps-ch">
    <li>3</li>
    <li>6</li>
    <li>7</li>
    <li>10</li>
    <li>30</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 7</p>
      <p>5 ga boʻlinadiganlar: 5, 10, 15, 20, 25, 30 — 6 ta; 25 ikkinchi 5 ni beradi. Jami 7.</p>
      <p><b>6</b> — 25 dagi ikkinchi 5 ni unutgan javob. <b>3</b> — faqat 10, 20, 30 ni sanagan.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">6</span>
  <span class="ps-trap__why">25 = 5 × 5 — u ikkita nol beradi. 25, 50, 75, 100 kabi sonlarni
  ikki marta sanang.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Oxirgi raqam savolida:</p>
  <ol>
    <li>asosning faqat oxirgi raqamini oling (23<sup>17</sup> → 3<sup>17</sup>);</li>
    <li>sikl uzunligini toping (koʻpincha 4);</li>
    <li>daraja ÷ sikl qoldigʻi = oʻrin; qoldiq 0 → oxirgi oʻrin.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">2<sup>40</sup> → qoldiq 0 → birinchi oʻrin → 2</p>
  <p class="pe-good">qoldiq 0 → toʻrtinchi oʻrin → 6</p>
  <p class="pe-fix__why">4 ga boʻlinadigan daraja siklning oxiriga tushadi: 2<sup>4</sup> = 16.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">25! → 25 ÷ 5 = 5 ta nol</p>
  <p class="pe-good">5 + 1 = 6 ta nol</p>
  <p class="pe-fix__why">25 ning oʻzi ikkita 5 beradi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> What is the units digit of 3<sup>7</sup>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">7 — sikl 3, 9, 7, 1; 7 ÷ 4 qoldiq 3.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> What is the units digit of 24 × 37 × 58?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">4 — 4 × 7 → 8, 8 × 8 → 4.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> What is the units digit of 2<sup>20</sup>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">6 — 20 ÷ 4 qoldiq 0, siklning oxiri.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> How many zeros are at the end of 50!?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">12 — 50 ÷ 5 = 10, 50 ÷ 25 = 2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> What is the units digit of 13<sup>3</sup> + 22<sup>2</sup>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">1 — 7 + 4 = 11.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>units digit</b><span>oxirgi (birlar) raqami</span></li>
  <li><b>tens digit</b><span>oʻnlar raqami</span></li>
  <li><b>cyclicity</b><span>takrorlanish, sikllilik</span></li>
  <li><b>pattern</b><span>qonuniyat</span></li>
  <li><b>factorial</b><span>faktorial</span></li>
  <li><b>trailing zeros</b><span>oxiridagi nollar</span></li>
  <li><b>product</b><span>koʻpaytma</span></li>
  <li><b>serial number</b><span>tartib raqami</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Oxirgi raqam faqat oxirgi raqamlardan chiqadi — qolganini tashlang.</li>
    <li>2, 3, 7, 8 — sikl 4; 4, 9 — sikl 2; 0, 1, 5, 6 — oʻzgarmaydi.</li>
    <li>Daraja ÷ 4 qoldigʻi — sikldagi oʻrin; qoldiq 0 — oxirgi oʻrin.</li>
    <li>n! dagi nollar: n ÷ 5 + n ÷ 25 + … (butun qismlar).</li>
    <li>Yigʻindida har bir hadning oxirgi raqamini alohida toping.</li>
  </ul>
</div>
"""

GMAT10 = """
<h2>GMAT-10: Ratios and Proportions</h2>

<p>Nisbat — biznesning kundalik tili: foydani sheriklar orasida boʻlish, xodimlar tarkibi,
valyuta kursi, xarajat normasi. GMAT'da nisbat savollari bitta gʻoyaga tayanadi:
<mark>nisbat — bu qismlar</mark>, va bitta qismning qiymatini topsangiz, qolgani oʻz-oʻzidan
chiqadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>nisbatni «qismlar» bilan yechasiz: 2:7 → 9 qism;</li>
    <li>ikki nisbatni umumiy had orqali birlashtirasiz;</li>
    <li>toʻgʻri va teskari proporsiyani farqlaysiz;</li>
    <li>nisbat oʻzgargandagi masalani tenglama bilan yechasiz.</li>
  </ul>
</div>

<h3>Nisbat — qismlar</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Managers : analysts = 2 : 7; total 36</span>
    <span class="pm-solve__why">Jami 2 + 7 = 9 qism</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Bir qism = 36 ÷ 9 = 4</span>
    <span class="pm-solve__why">Asosiy qadam — bitta qismning qiymati</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Analysts = 7 × 4 = 28</span>
    <span class="pm-solve__why">Managers = 2 × 4 = 8; tekshiruv: 28 + 8 = 36 ✓</span>
  </div>
</div>

<h3>Ikki nisbatni birlashtirish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">a : b = 2 : 3, b : c = 4 : 5</span>
    <span class="pm-solve__why">b ikkalasida bor, lekin 3 va 4 — har xil</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">a : b = 8 : 12, b : c = 12 : 15</span>
    <span class="pm-solve__why">b ni EKUK(3, 4) = 12 ga keltirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">a : b : c = 8 : 12 : 15 → a : c = 8 : 15</span>
    <span class="pm-solve__why">Endi uchala son bitta shkalada</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  2:3 va 4:5 dan «2:5» deb chetki sonlarni olish — eng keng tarqalgan xato. Oʻrtadagi had
  (b) ikkala nisbatda <b>bir xil son</b> boʻlmaguncha, nisbatlarni birlashtirib boʻlmaydi.
</div>

<h3>Toʻgʻri va teskari proporsiya</h3>

<p><b>Toʻgʻri proporsiya</b> — koʻproq mashina, koʻproq mahsulot. Saqlanadigan narsa —
<b>nisbat</b>: 4 mashina 240 dona, 7 mashina 420 dona, chunki 240/4 = 420/7 = 60.</p>

<p><b>Teskari proporsiya</b> — koʻproq ishchi, kamroq kun. Saqlanadigan narsa —
<b>koʻpaytma</b>: 6 ishchi 10 kunda, 15 ishchi 4 kunda, chunki 6 × 10 = 15 × 4 = 60.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">6 workers → 10 days; 15 workers → ?</span>
    <span class="pm-solve__why">Ish hajmi = 6 × 10 = 60 ishchi-kun</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">60 ÷ 15 = 4 days</span>
    <span class="pm-solve__why">Ishchilar koʻpaydi — kunlar kamaydi</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Proporsiyani yozishdan oldin bitta savol bering: <b>bittasi oshsa, ikkinchisi oshadimi
  yoki kamayadimi?</b> Kamaysa — nisbat emas, koʻpaytma saqlanadi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Nisbat oʻzgaradigan masalada («6 more dogs arrive, the ratio becomes 1:1») har ikkala
  miqdorni bitta harf bilan yozing: mushuklar 4<i>k</i>, itlar 3<i>k</i>. Keyin yangi shartni
  tenglama qiling: 4<i>k</i> = 3<i>k</i> + 6.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Nisbat <b>haqiqiy son emas</b>. «Managers to analysts is 2 to 7» — bu 2 ta menejer degani
  emas: 4, 8 yoki 20 ta boʻlishi mumkin. Shuning uchun nisbatning oʻzidan hech qachon
  miqdor chiqarmang — bitta haqiqiy son (jami, farq yoki bir guruh) berilmaguncha javob
  yoʻq. Berilgan son — bitta qismni topishning kaliti.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>the ratio of A to B is 2 to 7</b><span>A : B = 2 : 7 — tartib muhim</span></li>
  <li><b>in the ratio 3:5</b><span>3:5 nisbatda boʻlinadi</span></li>
  <li><b>at the same rate</b><span>bir xil tezlikda — proporsiya</span></li>
  <li><b>is proportional to</b><span>… ga proporsional</span></li>
  <li><b>scale</b><span>masshtab</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>The ratio of managers to analysts at a firm is 2 to 7. If the firm has 36 employees
    in these two roles, how many of them are analysts?</p>
  </div>
  <ol class="ps-ch">
    <li>8</li>
    <li>14</li>
    <li>18</li>
    <li>26</li>
    <li>28</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: E) 28</p>
      <p>9 qism, bir qism 4; analitiklar 7 × 4 = 28.</p>
      <p><b>8</b> — menejerlar soni: savolni oxirigacha oʻqing.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">8</span>
  <span class="ps-trap__why">Ikkinchi guruhning qiymati. GMAT ikkala guruhni ham variantlarga
  qoʻyadi — oxirida savol <b>kimni</b> soʻraganini qayta oʻqing.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>If the ratio of <i>a</i> to <i>b</i> is 2 to 3 and the ratio of <i>b</i> to <i>c</i> is
    4 to 5, what is the ratio of <i>a</i> to <i>c</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>2 : 5</li>
    <li>1 : 2</li>
    <li>8 : 15</li>
    <li>3 : 4</li>
    <li>4 : 5</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 8 : 15</p>
      <p>b ni 12 ga keltiramiz: a : b : c = 8 : 12 : 15.</p>
      <p><b>2 : 5</b> — chetki sonlarni toʻgʻridan-toʻgʻri olgan javob.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">2 : 5</span>
  <span class="ps-trap__why">Oʻrtadagi had ikkala nisbatda turlicha (3 va 4) — avval uni bir xil
  songa keltiring.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Nisbat savolida <b>bir qismni</b> toping:</p>
  <ol>
    <li>qismlarni qoʻshing (2 + 7 = 9);</li>
    <li>maʼlum miqdorni mos qismlar soniga boʻling (36 ÷ 9 = 4);</li>
    <li>soʻralgan guruhni qismlar soniga koʻpaytiring — va jami bilan tekshiring.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">8 workers: 15 days → 12 workers: 22.5 days</p>
  <p class="pe-good">8 × 15 = 120; 120 ÷ 12 = 10 days</p>
  <p class="pe-fix__why">Ishchilar koʻpaysa, kunlar kamayadi — bu teskari proporsiya.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">2:3 va 4:5 → a : c = 2 : 5</p>
  <p class="pe-good">8 : 15</p>
  <p class="pe-fix__why">Umumiy hadni avval bir xil qiling.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> $1,200 is split in the ratio 3:5. What is
  the smaller share?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">$450 — 8 qism, bir qism 150, 3 × 150.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> If 4 machines make 240 units per hour, how
  many units do 7 such machines make per hour?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">420 — bitta mashina 60, 7 × 60.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> 6 workers finish a job in 10 days. How many
  days would 15 workers need at the same rate?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">4 — 60 ishchi-kun ÷ 15.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> The ratio of men to women in a class of 36
  is 4:5. How many women are there?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">20 — 9 qism, bir qism 4, 5 × 4.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> A map's scale is 1 cm : 25 km. Two cities are
  7.2 cm apart on the map. How far apart are they?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">180 km — 7.2 × 25.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>ratio</b><span>nisbat</span></li>
  <li><b>proportion</b><span>proporsiya</span></li>
  <li><b>share</b><span>ulush</span></li>
  <li><b>part</b><span>qism</span></li>
  <li><b>directly proportional</b><span>toʻgʻri proporsional</span></li>
  <li><b>inversely proportional</b><span>teskari proporsional</span></li>
  <li><b>exchange rate</b><span>valyuta kursi</span></li>
  <li><b>scale</b><span>masshtab</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Nisbat — qismlar: qismlarni qoʻshing, bir qismni toping.</li>
    <li>Ikki nisbatni birlashtirishdan oldin umumiy hadni tenglang.</li>
    <li>Toʻgʻri proporsiyada nisbat, teskarisida koʻpaytma saqlanadi.</li>
    <li>Nisbat oʻzgarsa: 4k va 3k yozing, yangi shartni tenglama qiling.</li>
    <li>Oxirida savol qaysi guruhni soʻraganini qayta oʻqing.</li>
  </ul>
</div>
"""

TUTORIALS = [
    {
        "title": "GMAT-6: Fractions and Decimals Without a Calculator",
        "category": "math", "order": 6,
        "summary": "Kasr va oʻnli kasr jadvali, kasrlarni oʻzaro koʻpaytirish bilan solishtirish, oʻnli kasrga va kasrga boʻlish, chekli oʻnli kasr qoidasi.",
        "stories": ["Three-Eighths of the Budget"],
        "content": GMAT6,
    },
    {
        "title": "GMAT-7: Remainders and Divisibility Patterns",
        "category": "math", "order": 7,
        "summary": "Qoldiqli boʻlish, qoldiqlar bilan hisoblash, hafta kunlari masalalari va shartga mos eng kichik son bilan tekshirish.",
        "stories": ["The Bottles That Did Not Fit"],
        "content": GMAT7,
    },
    {
        "title": "GMAT-8: Exponents and Roots",
        "category": "math", "order": 8,
        "summary": "Daraja qoidalari, asoslarni bir xil qilish, ildizlarni soddalashtirish va manfiy asos hamda √(a + b) tuzoqlari.",
        "stories": ["Doubling Every Year"],
        "content": GMAT8,
    },
    {
        "title": "GMAT-9: Units Digits and Cyclicity",
        "category": "math", "order": 9,
        "summary": "Koʻpaytma va darajaning oxirgi raqami, 4 lik va 2 lik sikllar, qoldiq 0 tuzogʻi va faktorialning oxiridagi nollar.",
        "stories": ["The Last Digit Check"],
        "content": GMAT9,
    },
    {
        "title": "GMAT-10: Ratios and Proportions",
        "category": "math", "order": 10,
        "summary": "Nisbatni qismlar bilan yechish, ikki nisbatni birlashtirish, toʻgʻri va teskari proporsiya, nisbat oʻzgaradigan masalalar.",
        "stories": ["Two to Three to Four"],
        "content": GMAT10,
    },
]
