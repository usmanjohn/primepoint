# -*- coding: utf-8 -*-
"""Prime SAT Math — lessons 26–30 (ildizdan koʻphadga, koʻphaddan koʻpaytuvchiga).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_SAT.md
Lesson list: tutorial/management/commands/toc_prime_sat_math.txt

  mashqlar — practice/management/commands/_practice_ps_26_30.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_sat_readings_26_30.py

⚠️ ESKI SAT-26 … SAT-30 ustiga yoziladi (--republish).
⚠️ Til: sarlavha va test savollari inglizcha, tushuntirish oʻzbekcha. Son: 3.5 va 1,200.

⚠️ Kumulyativ (SAT-1…25 erkin: butun Blok A + daraja qonunlari, manfiy va kasr
   koʻrsatkichlar, ildizni soddalashtirish):
  • SAT-26 — maxrajni ratsionallash; qoʻshma ifoda (conjugate).
  • SAT-27 — koʻphad: daraja, bosh koeffitsient, qoʻshish va ayirish.
  • SAT-28 — koʻphadlarni koʻpaytirish: FOIL va undan kengrogʻi.
  • SAT-29 — koʻpaytuvchilarga ajratish: umumiy koʻpaytuvchi va guruhlash.
  • SAT-30 — kvadratlar ayirmasi va toʻliq kvadrat uchhadi.
  • ⛔ Kvadrat tenglama yechish (SAT-31…33) YOʻQ; ratsional ifodalar (SAT-40, 41) YOʻQ;
    ps-desmos SAT-83 dan.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_sat_26_30.py \\
        --author=prime --republish
"""

PLAYLIST = {
    "title": "Prime SAT Math",
    "category": "math",
    "description": (
        "Digital SAT matematikasi noldan — 100 dars. Savollar ingliz tilida, "
        "chunki test shunday; tushuntirish oʻzbek tilida, chunki oʻqituvchi shunday. "
        "Har bir darsda haqiqiy SAT savollari, tuzoq javoblar va 20 savollik mashq."
    ),
}

TUTORIALS = [

    # ══════════════════════════════════════════════════════════════════
    # SAT-26 — rationalizing denominators
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-26: Rationalizing Denominators",
        "category": "math",
        "order": 26,
        "summary": (
            "Maxrajdagi ildizdan qutulish: kasrni oʻsha ildizga koʻpaytirish, "
            "yoki ikki hadli maxrajda qoʻshma ifodadan foydalanish."
        ),
        "stories": ["Before the Calculator"],
        "content": """
<h2>SAT-26: Rationalizing Denominators</h2>

<p>SAT javoblarida <sup>1</sup>⁄<sub>√2</sub> koʻrinishidagi ifodani deyarli koʻrmaysiz —
u yerda <mark>√2 ⁄ 2</mark> turadi. Ikkalasi bir xil son (0.7071), lekin matematikaning
eski odati maxrajda ildiz qoldirmaydi. Bu odat qayerdan chiqqanini bilish qoidani
yodlashdan koʻra foydali.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>maxrajdagi bitta ildizdan qutulasiz;</li>
    <li>natijani soddalashtirasiz (SAT-25);</li>
    <li>ikki hadli maxrajda <em>qoʻshma ifoda</em>dan foydalanasiz;</li>
    <li>javobingizni SAT kutgan koʻrinishga keltirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The move</span>
  <span class="pe-chip pe-chip--s">1 ÷ √a</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--v">√a ÷ √a</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">√a ÷ a</span>
</div>

<h3>Nega bu odat paydo boʻlgan</h3>

<p>Kalkulyatorgacha boʻlgan davrda 1 ni 1.41421 ga <u>qoʻlda</u> boʻlish uzoq va xatoga
moyil ish edi. Lekin 1.41421 ni <u>2 ga</u> boʻlish — bolalar ishi. Shuning uchun
matematiklar ildizni yuqoriga koʻchirib olishardi: javob oʻsha, hisob esa bir necha marta
oson.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bugun kalkulyator bor, lekin odat qolgan — va SAT javoblari aynan shu odatga
  binoan yozilgan. Demak toʻgʻri hisoblab, javobni javoblar orasidan topa olmaslik
  mumkin: <b>soddalashtirish shakli ham javobning bir qismi</b>.
</div>

<h3>Bitta ildiz — bitta koʻpaytirish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">6 ÷ √3</span>
    <span class="pm-solve__why">Maxrajda ildiz turibdi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(6 × √3) ÷ (√3 × √3) = 6√3 ÷ 3</span>
    <span class="pm-solve__why">Surat va maxrajni <b>bir xil</b> songa koʻpaytirdik — kasr oʻzgarmadi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2√3</span>
    <span class="pm-solve__why">6 ÷ 3 = 2. Tekshiruv: 6 ÷ 1.732 ≈ 3.46 va 2 × 1.732 ≈ 3.46 ✓</span>
  </div>
</div>

<p>Eʼtibor bering, √3 × √3 = 3 — ildiz butunlay yoʻqoldi. Bu usulning butun sirri shu:
<strong>ildizni oʻziga koʻpaytirsangiz, u ildiz boʻlmay qoladi</strong>.</p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Surat va maxrajni <b>bir xil</b> songa koʻpaytirish shart — bu 1 ga koʻpaytirish bilan
  bir xil va kasrning qiymatini oʻzgartirmaydi. Faqat maxrajni koʻpaytirsangiz, boshqa
  son hosil boʻladi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Maxrajdagi ildiz <b>sonning oʻzini</b> oʻzgartirmaydi — faqat yozilish shaklini.
  6 ÷ √3 va 2√3 bir xil son (≈ 3.46). Shuning uchun ratsionallash «yechish» emas,
  <b>qayta yozish</b>: hech qanday yangi javob paydo boʻlmaydi.
</div>

<h3>Ikki hadli maxraj — qoʻshma ifoda</h3>

<p>Maxrajda 2 + √3 kabi ifoda tursa, oddiy koʻpaytirish yordam bermaydi. Bu yerda
<strong>conjugate</strong> — qoʻshma ifoda — ishlatiladi: oʻsha ikki had, lekin
oʻrtasidagi ishora almashtirilgan.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">1 ÷ (2 + √3)</span>
    <span class="pm-solve__why">Qoʻshma ifoda: 2 − √3</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(2 − √3) ÷ ((2 + √3)(2 − √3))</span>
    <span class="pm-solve__why">Ikkalasini ham qoʻshma ifodaga koʻpaytirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">maxraj = 4 − 3 = 1</span>
    <span class="pm-solve__why">Kvadratlar ayirmasi (SAT-30): oʻrtadagi hadlar qisqaradi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2 − √3</span>
    <span class="pm-solve__why">Tekshiruv: 1 ÷ 3.732 ≈ 0.268 va 2 − 1.732 ≈ 0.268 ✓</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Qoʻshma ifodaga koʻpaytirish nega ishlaydi? Chunki (<i>a</i> + <i>b</i>)(<i>a</i> − <i>b</i>)
  = <i>a</i><sup>2</sup> − <i>b</i><sup>2</sup> — oʻrtadagi ildizli hadlar bir-birini
  yoʻqotadi. Buni SAT-30 da toʻliq koʻramiz; hozircha natijani ishlatamiz.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>rationalize the denominator</b><span>maxrajni ratsionallashtiring</span></li>
  <li><b>which is equivalent to</b><span>qaysi ifoda teng kuchli</span></li>
  <li><b>in simplest form</b><span>eng sodda koʻrinishda</span></li>
  <li><b>the conjugate of</b><span>…ning qoʻshma ifodasi</span></li>
  <li><b>where a and b are integers</b><span>a va b — butun sonlar</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>Which expression is equivalent to 10 ÷ √5?</p>
  </div>
  <ol class="ps-ch">
    <li>2</li>
    <li>2√5</li>
    <li>5√2</li>
    <li>10√5</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 2√5</p>
      <p>Surat va maxrajni √5 ga koʻpaytiramiz: 10√5 ÷ 5 = 2√5.</p>
      <p>Tekshiruv: 10 ÷ 2.236 ≈ 4.47 va 2 × 2.236 ≈ 4.47 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">10√5</span>
  <span class="ps-trap__why">Maxrajga boʻlish unutilgan: koʻpaytirgandan keyin
  maxrajda 5 paydo boʻladi va 10 ÷ 5 = 2 boʻladi.</span>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">2</span>
  <span class="ps-trap__why">Ildiz butunlay yoʻqotilgan. 10 ÷ √5 ≈ 4.47, 2 emas —
  bir qarashda tekshirish mumkin.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">80 s</span></p>
  <div class="ps-stem__q">
    <p>Which expression is equivalent to 1 ÷ (3 − √2)?</p>
  </div>
  <ol class="ps-ch">
    <li>(3 − √2) ÷ 7</li>
    <li>(3 + √2) ÷ 7</li>
    <li>(3 + √2) ÷ 11</li>
    <li>3 + √2</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) (3 + √2) ÷ 7</p>
      <p>Qoʻshma ifoda 3 + √2. Maxraj: (3 − √2)(3 + √2) = 9 − 2 = 7.</p>
      <p>Tekshiruv: 1 ÷ (3 − 1.414) = 1 ÷ 1.586 ≈ 0.631, va (3 + 1.414) ÷ 7 ≈ 0.631 ✓</p>
    </div>
  </details>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Ildizli javoblarni tanlashda kalkulyator eng ishonchli hakam:</p>
  <ol>
    <li>Asl ifodani hisoblang (masalan 1 ÷ (3 − √2) ≈ 0.631).</li>
    <li>Javoblarni ham hisoblang.</li>
    <li>Mos kelgani — javob, hech qanday koʻpaytirishsiz.</li>
  </ol>
  <p>Bu usul ayniqsa qoʻshma ifoda savollarida foydali: u yerda belgi xatosi juda
  oson boʻladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">1 ÷ √2 = √2</p>
  <p class="pe-good">1 ÷ √2 = √2 ÷ 2</p>
  <p class="pe-fix__why">Koʻpaytirgandan keyin maxrajda <b>2</b> qoladi. Tekshiruv:
  1 ÷ 1.414 ≈ 0.71, va √2 ≈ 1.41 — teng emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">(2 + √3) ning qoʻshmasi (−2 + √3)</p>
  <p class="pe-good">Qoʻshmasi (2 − √3)</p>
  <p class="pe-fix__why">Faqat <b>oʻrtadagi</b> ishora almashadi, birinchi hadniki
  emas.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ratsionallashdan keyin javobni <b>yana bir marta soddalashtiring</b>: 6√3 ÷ 3 = 2√3.
  SAT javoblari har doim oxirigacha soddalashtirilgan boʻladi va yarim yoʻldagi
  koʻrinish variantlar orasida turadi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Rationalize: 1 ÷ √2</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">√2 ÷ 2 — surat va maxrajni √2 ga koʻpaytiramiz;
  √2 × √2 = 2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Rationalize: 3 ÷ √5</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">3√5 ÷ 5 — bu safar qisqartirish yoʻq, chunki 3 va 5 ning
  umumiy boʻluvchisi yoʻq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Rationalize and simplify: 8 ÷ √2</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">4√2 — 8√2 ÷ 2 = 4√2. Oxirgi qisqartirishni unutmang.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  What is the conjugate of 5 + √7?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">5 − √7 — faqat oʻrtadagi ishora almashadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Rationalize: 4 ÷ (√5 − 1)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">√5 + 1 — qoʻshma ifoda (√5 + 1), maxraj 5 − 1 = 4, va
  4 ÷ 4 = 1. Tekshiruv: 4 ÷ 1.236 ≈ 3.24 va 2.236 + 1 ≈ 3.24 ✓</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>rationalize</b><span>ratsionallashtirish (ildizdan qutulish)</span></li>
  <li><b>denominator</b><span>maxraj</span></li>
  <li><b>numerator</b><span>surat</span></li>
  <li><b>conjugate</b><span>qoʻshma ifoda (ishorasi almashtirilgan)</span></li>
  <li><b>equivalent</b><span>teng kuchli</span></li>
  <li><b>simplest form</b><span>eng sodda koʻrinish</span></li>
  <li><b>irrational</b><span>irratsional son</span></li>
  <li><b>multiply top and bottom</b><span>surat va maxrajni koʻpaytirish</span></li>
  <li><b>integer</b><span>butun son</span></li>
  <li><b>cancel</b><span>qisqartirmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Bitta ildiz boʻlsa — <b>oʻsha ildizga</b> koʻpaytiring; ildiz oʻziga
        koʻpaytirilganda yoʻqoladi.</li>
    <li>Ikki hadli maxrajda — <b>qoʻshma ifoda</b>: faqat oʻrtadagi ishora
        almashadi.</li>
    <li>Oxirida <b>yana soddalashtiring</b>: 6√3 ÷ 3 = 2√3.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-27 — polynomials: adding and subtracting
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-27: Introduction to Polynomials: Adding and Subtracting",
        "category": "math",
        "order": 27,
        "summary": (
            "Koʻphad nima, uning darajasi va bosh koeffitsienti; qoʻshish oddiy, "
            "ayirish esa faqat bitta narsaga — qavs oldidagi minusga — bogʻliq."
        ),
        "stories": ["Two Rooms and a Corridor"],
        "content": """
<h2>SAT-27: Introduction to Polynomials: Adding and Subtracting</h2>

<p>SAT-1 da 3<em>x</em> + 5 kabi ifodalar bilan ishlagan edik. <strong>Polynomial</strong>
— shunday ifodalarning kattarogʻi: bir necha had, har birida harf butun va manfiy boʻlmagan
darajada. Yaxshi yangilik shuki, ularni qoʻshish va ayirish <mark>SAT-1 dagi oʻxshash
hadlar qoidasining oʻzi</mark> — hech qanday yangi amal yoʻq.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>koʻphadning <em>darajasi</em> va <em>bosh koeffitsienti</em>ni aytasiz;</li>
    <li>uni standart koʻrinishda (kamayuvchi daraja boʻyicha) yozasiz;</li>
    <li>ikki koʻphadni qoʻshasiz;</li>
    <li>ayirishda qavs oldidagi minusni <u>hamma hadga</u> tarqatasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Standard form</span>
  <span class="pe-chip pe-chip--v">3x<sup>2</sup></span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">5x</span>
  <span class="pe-op">−</span>
  <span class="pe-chip pe-chip--o">2</span>
  <span class="pe-chip pe-chip--opt">daraja 2 · bosh koeffitsient 3</span>
</div>

<h3>Uchta soʻz</h3>

<ul>
  <li><strong>Degree</strong> (daraja) — eng katta koʻrsatkich. 3<em>x</em><sup>2</sup> +
      5<em>x</em> − 2 ning darajasi <b>2</b>.</li>
  <li><strong>Leading coefficient</strong> (bosh koeffitsient) — eng katta darajali
      hadning oldidagi son. Bu yerda <b>3</b>.</li>
  <li><strong>Constant term</strong> (oʻzgarmas had) — harfsiz had, bu yerda <b>−2</b>.</li>
</ul>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bosh koeffitsientni topishdan oldin koʻphadni <b>standart koʻrinishga</b> keltiring —
  hadlarni kamayuvchi daraja boʻyicha tartiblang. 5 − 2<i>x</i><sup>3</sup> + <i>x</i>
  ning bosh koeffitsienti 5 emas, <b>−2</b>: u −2<i>x</i><sup>3</sup> + <i>x</i> + 5
  boʻlib yoziladi.
</div>

<h3>Qoʻshish — oʻxshash hadlarni birlashtirish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">(3x<sup>2</sup> + 5x − 2) + (x<sup>2</sup> − 4x + 7)</span>
    <span class="pm-solve__why">Qavslarni ochamiz — qoʻshishda hech narsa oʻzgarmaydi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x<sup>2</sup> + x<sup>2</sup> = 4x<sup>2</sup></span>
    <span class="pm-solve__why">Bir xil darajali hadlar oʻxshash hadlar (SAT-1)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">4x<sup>2</sup> + x + 5</span>
    <span class="pm-solve__why">5x − 4x = x va −2 + 7 = 5</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Koʻrsatkich <b>butun va manfiy boʻlmagan</b> boʻlishi koʻphadning taʼrifidagi shart.
  Shuning uchun 3<i>x</i><sup>−2</sup> ham, √<i>x</i> ham koʻphad emas — SAT ba'zan
  aynan shuni soʻraydi.
</div>

<h3>Ayirish — butun ikkinchi qavsning ishorasi almashadi</h3>

<p>Bu darsdagi yagona qiyinchilik shu, va u SAT-1 dagi eski tanish: qavs oldidagi minus
<u>ichkaridagi hamma hadga</u> tegadi, faqat birinchisiga emas.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">(3x<sup>2</sup> + 5x − 2) − (x<sup>2</sup> − 4x + 7)</span>
    <span class="pm-solve__why">Berilgan ifoda</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x<sup>2</sup> + 5x − 2 − x<sup>2</sup> + 4x − 7</span>
    <span class="pm-solve__why">Uchala hadning ham ishorasi almashdi: −x<sup>2</sup>, <b>+4x</b>, −7</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2x<sup>2</sup> + 9x − 9</span>
    <span class="pm-solve__why">Oʻxshash hadlar birlashtirildi</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Ayirishda ikkinchi qavsni <b>oldin</b> qayta yozing: ishoralarini almashtirib, keyin
  qoʻshing. Ikki ishni bir vaqtda qilish — bu mavzudagi xatolarning deyarli
  hammasi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>which expression is equivalent to</b><span>qaysi ifoda teng kuchli</span></li>
  <li><b>the degree of the polynomial</b><span>koʻphadning darajasi — eng katta koʻrsatkich</span></li>
  <li><b>the leading coefficient</b><span>bosh koeffitsient</span></li>
  <li><b>the constant term</b><span>oʻzgarmas had (harfsiz)</span></li>
  <li><b>in standard form</b><span>standart koʻrinishda (kamayuvchi daraja boʻyicha)</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>Which expression is equivalent to (4<i>x</i><sup>2</sup> − 3<i>x</i> + 1) −
    (2<i>x</i><sup>2</sup> + 5<i>x</i> − 6)?</p>
  </div>
  <ol class="ps-ch">
    <li>2<i>x</i><sup>2</sup> − 8<i>x</i> + 7</li>
    <li>2<i>x</i><sup>2</sup> − 8<i>x</i> − 5</li>
    <li>2<i>x</i><sup>2</sup> + 2<i>x</i> − 5</li>
    <li>6<i>x</i><sup>2</sup> + 2<i>x</i> − 5</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 2x<sup>2</sup> − 8x + 7</p>
      <p>Ikkinchi qavsning uchala hadi ham ishorasini almashtiradi:
      −2<i>x</i><sup>2</sup>, −5<i>x</i>, <b>+6</b>.</p>
      <p>Keyin: 4 − 2 = 2, −3 − 5 = −8, 1 + 6 = 7.</p>
      <p>Tekshirish: <i>x</i> = 1 qoʻying. Asl ifoda (4 − 3 + 1) − (2 + 5 − 6) =
      2 − 1 = 1, va 2 − 8 + 7 = 1 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">2x<sup>2</sup> − 8x − 5</span>
  <span class="ps-trap__why">Oxirgi hadning ishorasi almashtirilmagan: −6 ni +6 qilish
  kerak edi. Minus faqat birinchi ikki hadga tarqatilgan.</span>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">6x<sup>2</sup> + 2x − 5</span>
  <span class="ps-trap__why">Ayirish oʻrniga <b>qoʻshilgan</b>. Bu javob qavslar
  orasida plyus turganda toʻgʻri boʻlardi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">40 s</span></p>
  <div class="ps-stem__q">
    <p>What is the degree and the leading coefficient of the polynomial
    5 − 2<i>x</i><sup>3</sup> + <i>x</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>Degree 1, leading coefficient 1</li>
    <li>Degree 3, leading coefficient −2</li>
    <li>Degree 3, leading coefficient 5</li>
    <li>Degree 5, leading coefficient −2</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) daraja 3, bosh koeffitsient −2</p>
      <p>Standart koʻrinishda: −2<i>x</i><sup>3</sup> + <i>x</i> + 5. Eng katta
      koʻrsatkich 3, va u turgan hadning koeffitsienti −2 (ishorasi bilan).</p>
      <p><b>Bosh koeffitsient 5</b> — birinchi yozilgan sonni olgan javob; hadlarning
      yozilish tartibi ahamiyatsiz.</p>
    </div>
  </details>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Koʻphadli javoblarni <b>bitta son qoʻyib</b> tekshiring (SAT-1 dagi usul):</p>
  <ol>
    <li><i>x</i> = 1 emas, <i>x</i> = 2 ni tanlang — u koʻproq xatoni ochadi.</li>
    <li>Asl ifodani hisoblang.</li>
    <li>Javoblarni ham hisoblang; mos kelgani — javob.</li>
  </ol>
  <p>Uzun ayirishda bu usul belgi xatosini butunlay chetlab oʻtadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">(5x − 4) − (2x − 9) = 3x − 13</p>
  <p class="pe-good">3x + 5</p>
  <p class="pe-fix__why">−(−9) = <b>+9</b>, va −4 + 9 = 5. Ikkinchi qavsdagi manfiy
  had ayirilganda musbatga aylanadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">3x<sup>2</sup> + 2x = 5x<sup>3</sup></p>
  <p class="pe-good">Ular oʻxshash hadlar emas — soddalashtirib boʻlmaydi.</p>
  <p class="pe-fix__why">Faqat <b>bir xil darajali</b> hadlar qoʻshiladi. Daraja esa
  qoʻshishda umuman oʻzgarmaydi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikki koʻphad qoʻshilganda yoki ayirilganda natijaning darajasi <b>ortmaydi</b> —
  koʻpi bilan oʻsha boʻlib qoladi (ba'zan kamayadi, agar bosh hadlar qisqarsa).
  Daraja faqat <b>koʻpaytirishda</b> ortadi — bu keyingi dars.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Simplify: (2<i>x</i><sup>2</sup> + 3<i>x</i>) + (<i>x</i><sup>2</sup> − <i>x</i>)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">3<i>x</i><sup>2</sup> + 2<i>x</i> — 2 + 1 = 3 va
  3 − 1 = 2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Simplify: (5<i>x</i> − 4) − (2<i>x</i> − 9)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">3<i>x</i> + 5 — ikkinchi qavs ishoralarini almashtiradi:
  −2x va +9.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  What is the degree of 7<i>x</i><sup>4</sup> − 3<i>x</i><sup>2</sup> + 1?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">4 — eng katta koʻrsatkich. Hadlar soni (uchta) daraja
  emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Simplify: (<i>x</i><sup>3</sup> + 2<i>x</i>) + (3<i>x</i><sup>3</sup> − <i>x</i> + 5)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">4<i>x</i><sup>3</sup> + <i>x</i> + 5 — x<sup>3</sup> lar
  qoʻshildi, 2x − x = x, va 5 yolgʻiz qoldi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A triangle has sides of (2<i>x</i> + 1), (3<i>x</i> − 2) and (<i>x</i> + 6). Write its
  perimeter.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">6<i>x</i> + 5 — uchala tomonni qoʻshamiz: 2x + 3x + x = 6x,
  va 1 − 2 + 6 = 5.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>polynomial</b><span>koʻphad</span></li>
  <li><b>term</b><span>had</span></li>
  <li><b>degree</b><span>daraja — eng katta koʻrsatkich</span></li>
  <li><b>leading coefficient</b><span>bosh koeffitsient</span></li>
  <li><b>constant term</b><span>oʻzgarmas had</span></li>
  <li><b>standard form</b><span>standart koʻrinish (kamayuvchi daraja)</span></li>
  <li><b>like terms</b><span>oʻxshash hadlar</span></li>
  <li><b>combine</b><span>birlashtirmoq</span></li>
  <li><b>binomial / trinomial</b><span>ikkihad / uchhad</span></li>
  <li><b>perimeter</b><span>perimetr</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Daraja — <b>eng katta koʻrsatkich</b>; bosh koeffitsient shu had oldidagi
        son, ishorasi bilan.</li>
    <li>Ayirishda ikkinchi qavsning <b>hamma hadi</b> ishorasini almashtiradi.</li>
    <li>Faqat <b>bir xil darajali</b> hadlar birlashadi — daraja qoʻshishda
        oʻzgarmaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-28 — multiplying polynomials
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-28: Multiplying Polynomials (FOIL and beyond)",
        "category": "math",
        "order": 28,
        "summary": (
            "Har bir hadni har bir hadga koʻpaytirish. Ikki ikkihad uchun bu FOIL "
            "deb ataladi, lekin qoida kattaroq ifodalarda ham oʻsha."
        ),
        "stories": ["The Garden That Grew Twice"],
        "content": """
<h2>SAT-28: Multiplying Polynomials (FOIL and beyond)</h2>

<p>Koʻphadlarni koʻpaytirish bitta qoidaga tayanadi va u yangi emas: <mark>birinchi
qavsdagi har bir had ikkinchi qavsdagi har bir hadga koʻpaytiriladi</mark>. Ikki ikkihad
uchun bu toʻrtta koʻpaytma beradi va uni eslab qolish uchun <strong>FOIL</strong> degan
nom oʻylab topilgan.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>ikki ikkihadni FOIL bilan koʻpaytirasiz;</li>
    <li>oʻrtadagi hadni toʻgʻri birlashtirasiz;</li>
    <li>uch hadli qavs bilan ham ishlaysiz;</li>
    <li>faqat bitta koeffitsient soʻralganda butun koʻpaytirishni qilmaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">FOIL</span>
  <span class="pe-chip pe-chip--s">First</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">Outer</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">Inner</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--aux">Last</span>
</div>

<h3>Toʻrtta koʻpaytma</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">(x + 3)(x + 5)</span>
    <span class="pm-solve__why">Berilgan koʻpaytma</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x · x = x<sup>2</sup>   ·   x · 5 = 5x</span>
    <span class="pm-solve__why">First va Outer</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 · x = 3x   ·   3 · 5 = 15</span>
    <span class="pm-solve__why">Inner va Last</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x<sup>2</sup> + 8x + 15</span>
    <span class="pm-solve__why">Oʻrtadagi ikki had oʻxshash: 5x + 3x = 8x</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  FOIL — bu yangi qoida emas, <b>qavs ochishning</b> tartibli koʻrinishi (SAT-1).
  Shuning uchun u faqat ikki ikkihad uchun ishlaydi; uch hadli qavsda esa
  «har birini har biriga» degan asosiy qoida qoʻllanadi.
</div>

<h3>Ishoralar bilan</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">(2x − 1)(x + 4)</span>
    <span class="pm-solve__why">Manfiy had bor — ishora u bilan birga yuradi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x<sup>2</sup> + 8x − x − 4</span>
    <span class="pm-solve__why">2x·x, 2x·4, (−1)·x, (−1)·4</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2x<sup>2</sup> + 7x − 4</span>
    <span class="pm-solve__why">8x − x = 7x</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻrtadagi hadning ishorasi eng koʻp xato beradigan joy. Uni alohida hisoblang:
  «katta son manfiymi?» degan savolga javob bering. (2x − 1)(x + 4) da +8x va −x —
  natija musbat; (2x + 1)(x − 4) da esa −8x va +x — natija manfiy.
</div>

<h3>Kattaroq qavs — oʻsha qoida</h3>

<p>(<em>x</em> + 3)(<em>x</em><sup>2</sup> − 2<em>x</em> + 1) da toʻrtta emas, <b>oltita</b>
koʻpaytma boʻladi: birinchi qavsda ikki had, ikkinchisida uchta.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x(x<sup>2</sup> − 2x + 1) = x<sup>3</sup> − 2x<sup>2</sup> + x</span>
    <span class="pm-solve__why">Birinchi hadni tarqatdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3(x<sup>2</sup> − 2x + 1) = 3x<sup>2</sup> − 6x + 3</span>
    <span class="pm-solve__why">Ikkinchi hadni tarqatdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x<sup>3</sup> + x<sup>2</sup> − 5x + 3</span>
    <span class="pm-solve__why">−2x<sup>2</sup> + 3x<sup>2</sup> = x<sup>2</sup>; x − 6x = −5x</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Koʻpaytmadagi hadlar sonini oldindan biling: 2 × 3 = <b>6</b> ta koʻpaytma boʻlishi
  kerak. Agar beshta yozgan boʻlsangiz, bittasini tashlab ketgansiz — bu eng tez
  tekshiruv.
</div>

<h3>Faqat bitta koeffitsient soʻralganda</h3>

<p>SAT koʻpincha butun koʻpaytmani emas, <u>bitta hadning koeffitsientini</u> soʻraydi.
U holda faqat oʻsha hadni beradigan koʻpaytmalarni hisoblang.</p>

<div class="pe-ex">
  <p class="pe-ex__math">(3x − 2)(x + 4) da x ning koeffitsienti</p>
  <p class="pe-ex__uz">Faqat ikkita koʻpaytma x beradi: 3x · 4 = 12x va (−2) · x = −2x.</p>
  <p class="pe-ex__why">Demak 12 − 2 = 10. Qolgan ikki koʻpaytmani hisoblash shart emas.</p>
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>the product of</b><span>…ning koʻpaytmasi</span></li>
  <li><b>expand</b><span>qavslarni oching</span></li>
  <li><b>the coefficient of x</b><span>x ning koeffitsienti</span></li>
  <li><b>which is equivalent to</b><span>qaysi ifoda teng kuchli</span></li>
  <li><b>where a, b and c are constants</b><span>a, b va c — sonlar</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>Which expression is equivalent to (2<i>x</i> + 3)(<i>x</i> − 5)?</p>
  </div>
  <ol class="ps-ch">
    <li>2<i>x</i><sup>2</sup> − 7<i>x</i> − 15</li>
    <li>2<i>x</i><sup>2</sup> + 7<i>x</i> − 15</li>
    <li>2<i>x</i><sup>2</sup> − 13<i>x</i> − 15</li>
    <li>2<i>x</i><sup>2</sup> − 15</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 2x<sup>2</sup> − 7x − 15</p>
      <p>2<i>x</i>·<i>x</i> = 2<i>x</i><sup>2</sup>; 2<i>x</i>·(−5) = −10<i>x</i>;
      3·<i>x</i> = 3<i>x</i>; 3·(−5) = −15. Oʻrtada −10<i>x</i> + 3<i>x</i> =
      −7<i>x</i>.</p>
      <p>Tekshirish: <i>x</i> = 2 → (7)(−3) = −21, va 8 − 14 − 15 = −21 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">2x<sup>2</sup> − 15</span>
  <span class="ps-trap__why">Faqat First va Last hisoblangan — oʻrtadagi ikki
  koʻpaytma tashlab ketilgan. Toʻrtta koʻpaytma boʻlishi kerak.</span>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">2x<sup>2</sup> + 7x − 15</span>
  <span class="ps-trap__why">Oʻrta hadning ishorasi notoʻgʻri: −10x + 3x = −7x, +7x
  emas. Kattaroq son manfiy edi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>In the product (3<i>x</i> − 2)(<i>x</i> + 4), what is the coefficient of
    <i>x</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>−8</li>
    <li>3</li>
    <li>10</li>
    <li>12</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 10</p>
      <p><i>x</i> hadini faqat ikkita koʻpaytma beradi: 3<i>x</i> · 4 = 12<i>x</i> va
      (−2) · <i>x</i> = −2<i>x</i>. Demak 12 − 2 = 10.</p>
      <p><b>−8</b> — oʻzgarmas had (−2 × 4); <b>12</b> — faqat bitta koʻpaytma
      hisoblangan javob.</p>
    </div>
  </details>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Koʻpaytirish savolida ikki tez filtr bor:</p>
  <ol>
    <li><b>Oxirgi son</b> — ikki oxirgi hadning koʻpaytmasi. (2x + 3)(x − 5) uchun
        3 × (−5) = −15, va faqat shu bilan yarim javob oʻchadi.</li>
    <li><b>Birinchi had</b> — ikki bosh hadning koʻpaytmasi: 2<i>x</i><sup>2</sup>.</li>
  </ol>
  <p>Qolganini oʻrta had ajratadi — va koʻpincha uni hisoblash shart ham
  boʻlmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">(x + 3)(x + 5) = x<sup>2</sup> + 15</p>
  <p class="pe-good">x<sup>2</sup> + 8x + 15</p>
  <p class="pe-fix__why">Oʻrtadagi ikki koʻpaytma unutilgan. Koʻpaytirish faqat
  «birinchini birinchiga, oxirgini oxirgiga» degani emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">(x + 5)<sup>2</sup> = x<sup>2</sup> + 25</p>
  <p class="pe-good">x<sup>2</sup> + 10x + 25</p>
  <p class="pe-fix__why">Kvadrat — bu (x + 5)(x + 5), demak oʻrtada 5x + 5x = 10x
  ham bor. Bu SAT'dagi eng qadimiy xato.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Koʻpaytirishda daraja <b>ortadi</b>: ikkita birinchi darajali qavs ikkinchi darajali
  koʻphad beradi. Qoʻshishda esa daraja oʻzgarmasdi (SAT-27) — bu ikki amalning asosiy
  farqi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Expand: (<i>x</i> + 2)(<i>x</i> + 7)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i><sup>2</sup> + 9<i>x</i> + 14 — oʻrtada
  7x + 2x = 9x.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Expand: (<i>x</i> − 4)(<i>x</i> + 4)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i><sup>2</sup> − 16 — oʻrtadagi hadlar
  (+4x va −4x) bir-birini yoʻqotadi. Bu SAT-30 dagi kvadratlar ayirmasi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Expand: (2<i>x</i> + 1)(3<i>x</i> − 2)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">6<i>x</i><sup>2</sup> − <i>x</i> − 2 — oʻrtada
  −4x + 3x = −x.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Expand: (<i>x</i> + 5)<sup>2</sup></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i><sup>2</sup> + 10<i>x</i> + 25 — kvadratni ikki
  qavs deb yozing va FOIL qiling.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A rectangular garden is (<i>x</i> + 3) metres by (<i>x</i> + 5) metres. Write its area
  as a polynomial.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i><sup>2</sup> + 8<i>x</i> + 15 kvadrat metr. Agar
  x = 10 boʻlsa: 13 × 15 = 195, va 100 + 80 + 15 = 195 ✓</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>expand</b><span>qavsni ochish</span></li>
  <li><b>product</b><span>koʻpaytma</span></li>
  <li><b>binomial</b><span>ikkihad</span></li>
  <li><b>distribute</b><span>tarqatish (har biriga koʻpaytirish)</span></li>
  <li><b>coefficient of x</b><span>x ning koeffitsienti</span></li>
  <li><b>middle term</b><span>oʻrtadagi had</span></li>
  <li><b>constant term</b><span>oʻzgarmas had</span></li>
  <li><b>squared</b><span>kvadratga koʻtarilgan</span></li>
  <li><b>area</b><span>yuza</span></li>
  <li><b>equivalent</b><span>teng kuchli</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Har bir hadni har bir hadga</b> — FOIL shu qoidaning ikki ikkihad uchun
        nomi.</li>
    <li>Koʻpaytmalar soni = hadlar sonining koʻpaytmasi (2 × 3 = 6) — eng tez
        tekshiruv.</li>
    <li>(x + 5)<sup>2</sup> ≠ x<sup>2</sup> + 25: <b>oʻrtadagi had</b> har doim
        bor.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-29 — factoring: GCF and grouping
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-29: Factoring: Greatest Common Factor (GCF) and Grouping",
        "category": "math",
        "order": 29,
        "summary": (
            "Koʻpaytirishning teskarisi. Har doim umumiy koʻpaytuvchidan boshlanadi, "
            "toʻrt hadli ifodada esa guruhlash usuli qoʻllanadi."
        ),
        "stories": ["Rows for the Sports Day"],
        "content": """
<h2>SAT-29: Factoring: Greatest Common Factor (GCF) and Grouping</h2>

<p>SAT-28 da qavslarni ochdik. Endi teskari yoʻnalishda yuramiz: berilgan ifodani
<mark>koʻpaytmaga aylantiramiz</mark>. Bu ish <strong>factoring</strong> deb ataladi va
Blok B ning yarmi shunga tayanadi — kvadrat tenglamalar, ratsional ifodalar, grafiklarning
nollari. Va u har doim bitta qadamdan boshlanadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>eng katta umumiy koʻpaytuvchini (GCF) topasiz — son va harf boʻyicha;</li>
    <li>uni qavs oldiga chiqarasiz va tekshirasiz;</li>
    <li>toʻrt hadli ifodani guruhlash bilan ajratasiz;</li>
    <li>«toʻliq ajratilgan» va «yarim ajratilgan» javobni farqlaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Always first</span>
  <span class="pe-chip pe-chip--v">GCF</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">qavs oldiga</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">qolgani qavs ichida</span>
</div>

<h3>GCF — son va harf alohida</h3>

<p>Umumiy koʻpaytuvchini ikki bosqichda toping: avval <u>sonlarning</u> eng katta umumiy
boʻluvchisi, keyin <u>har bir harfning</u> eng kichik darajasi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">6x<sup>3</sup> + 9x<sup>2</sup></span>
    <span class="pm-solve__why">Sonlar: 6 va 9 → EKUB 3. Harf: x<sup>3</sup> va x<sup>2</sup> → x<sup>2</sup></span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">GCF = 3x<sup>2</sup></span>
    <span class="pm-solve__why">Ikkalasini birlashtirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3x<sup>2</sup>(2x + 3)</span>
    <span class="pm-solve__why">Tekshiruv: qavsni ochsak 6x<sup>3</sup> + 9x<sup>2</sup> ✓</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Harf uchun <b>eng kichik</b> daraja olinadi: x<sup>3</sup> va x<sup>2</sup> dan
  x<sup>2</sup>. Sabab oddiy — x<sup>3</sup> ni qavs oldiga chiqarsangiz, ikkinchi hadda
  x qolmaydi va ajratma notoʻgʻri boʻladi.
</div>

<h3>Ikki harfli misol</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">12x<sup>2</sup>y − 18xy<sup>2</sup></span>
    <span class="pm-solve__why">Sonlar: 12 va 18 → 6. x: eng kichigi x. y: eng kichigi y</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">6xy(2x − 3y)</span>
    <span class="pm-solve__why">Tekshiruv: 6xy · 2x = 12x<sup>2</sup>y ✓ va 6xy · (−3y) = −18xy<sup>2</sup> ✓</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Ajratmani <b>har doim qavsni ochib</b> tekshiring. Bu 5 soniya oladi va bu mavzudagi
  barcha xatolarni tutadi — chunki koʻpaytirish siz allaqachon bilgan ish (SAT-28).
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ajratish — koʻpaytirishning <b>teskarisi</b>, shuning uchun uni tekshirish har doim
  oson: qavsni oching va asl ifodani koʻring. Matematikada javobni bunchalik tez
  tekshirish mumkin boʻlgan mavzu kam.
</div>

<h3>Toʻrt had — guruhlash</h3>

<p>Toʻrtta hadning hammasida umumiy koʻpaytuvchi boʻlmasligi mumkin. Unda ularni
<strong>ikkitadan guruhlab</strong>, har guruhdan alohida GCF chiqaramiz — va agar qavs
ichidagilar bir xil boʻlsa, ish bitdi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x<sup>3</sup> + 3x<sup>2</sup> + 2x + 6</span>
    <span class="pm-solve__why">Toʻrtta had, umumiy koʻpaytuvchi yoʻq</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x<sup>2</sup>(x + 3) + 2(x + 3)</span>
    <span class="pm-solve__why">Birinchi ikkitasidan x<sup>2</sup>, ikkinchi ikkitasidan 2</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">(x + 3)(x<sup>2</sup> + 2)</span>
    <span class="pm-solve__why">(x + 3) ikkalasida ham bor — uni oldinga chiqardik</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Guruhlashdan keyin qavs ichidagilar <b>bir xil</b> chiqishi shart. Agar (x + 3) va
  (x − 3) chiqsa, ikkinchi guruhdan manfiy son chiqarish kerak boʻladi — yoki
  guruhlash boshqacha qilinishi kerak.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>factor completely</b><span>toʻliq ajrating — yarim ajratilgan javob notoʻgʻri</span></li>
  <li><b>the greatest common factor</b><span>eng katta umumiy koʻpaytuvchi</span></li>
  <li><b>which is equivalent to</b><span>qaysi ifoda teng kuchli</span></li>
  <li><b>by grouping</b><span>guruhlash usuli bilan</span></li>
  <li><b>where a and b are integers</b><span>a va b — butun sonlar</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>Which expression shows 8<i>x</i><sup>3</sup> + 12<i>x</i><sup>2</sup> factored
    completely?</p>
  </div>
  <ol class="ps-ch">
    <li>2<i>x</i><sup>2</sup>(4<i>x</i> + 6)</li>
    <li>4<i>x</i>(2<i>x</i><sup>2</sup> + 3<i>x</i>)</li>
    <li>4<i>x</i><sup>2</sup>(2<i>x</i> + 3)</li>
    <li>4<i>x</i><sup>2</sup>(2<i>x</i> + 12)</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 4x<sup>2</sup>(2x + 3)</p>
      <p>Sonlar 8 va 12 → EKUB 4; harflar x<sup>3</sup> va x<sup>2</sup> →
      x<sup>2</sup>.</p>
      <p>Tekshiruv: 4x<sup>2</sup> · 2x = 8x<sup>3</sup> ✓ va 4x<sup>2</sup> · 3 =
      12x<sup>2</sup> ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">2x<sup>2</sup>(4x + 6)</span>
  <span class="ps-trap__why">Qavsni ochsangiz toʻgʻri ifoda chiqadi, lekin ajratma
  <b>toʻliq emas</b>: qavs ichida hali 2 umumiy koʻpaytuvchi bor.
  «Factor completely» degan soʻz shuni talab qiladi.</span>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">4x(2x<sup>2</sup> + 3x)</span>
  <span class="ps-trap__why">Bu ham toʻliq emas — qavs ichida x qolgan. Toʻliq
  ajratilgan javobning qavsida <b>umumiy koʻpaytuvchi qolmaydi</b>.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>Which expression is equivalent to <i>x</i><sup>3</sup> + 3<i>x</i><sup>2</sup> +
    2<i>x</i> + 6?</p>
  </div>
  <ol class="ps-ch">
    <li>(<i>x</i> − 3)(<i>x</i><sup>2</sup> + 2)</li>
    <li>(<i>x</i> + 2)(<i>x</i><sup>2</sup> + 3)</li>
    <li>(<i>x</i> + 3)(<i>x</i><sup>2</sup> − 2)</li>
    <li>(<i>x</i> + 3)(<i>x</i><sup>2</sup> + 2)</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: D) (x + 3)(x<sup>2</sup> + 2)</p>
      <p>Guruhlaymiz: x<sup>2</sup>(x + 3) + 2(x + 3), keyin (x + 3) ni oldinga
      chiqaramiz.</p>
      <p>Tekshirish uchun qavslarni oching yoki <i>x</i> = 1 qoʻying: asl ifoda
      1 + 3 + 2 + 6 = 12, va (4)(3) = 12 ✓</p>
    </div>
  </details>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Ajratish savollarida javoblarni <b>koʻpaytirib</b> tekshirish har doim tezroq:</p>
  <ol>
    <li>Javobdagi qavslarni oching (SAT-28).</li>
    <li>Asl ifoda chiqsa — javob shu.</li>
    <li>Ikkitasi ham toʻgʻri chiqsa, «<b>completely</b>» soʻziga qarang: qavs ichida
        umumiy koʻpaytuvchi qolgani javob emas.</li>
  </ol>
  <p>Yoki bitta son qoʻying: <i>x</i> = 1 koʻpincha yetadi va 10 soniya oladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">6x<sup>3</sup> + 9x<sup>2</sup> = 3x<sup>3</sup>(2 + 3)</p>
  <p class="pe-good">3x<sup>2</sup>(2x + 3)</p>
  <p class="pe-fix__why">Harfning <b>eng kichik</b> darajasi chiqariladi. x<sup>3</sup>
  ni chiqarsangiz, ikkinchi hadda x qolmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">5x<sup>2</sup> − 15x = 5x(x − 15)</p>
  <p class="pe-good">5x(x − 3)</p>
  <p class="pe-fix__why">15x ni 5x ga boʻlganda 3 chiqadi, 15 emas. Har doim qavsni
  ochib tekshiring.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>GCF har doim birinchi qadam.</b> Hatto keyingi darsdagi formulalar (kvadratlar
  ayirmasi) ishlatilishidan oldin ham: 2x<sup>2</sup> − 18 ni avval 2(x<sup>2</sup> − 9)
  deb yozing, keyin 2(x − 3)(x + 3). GCF ni oʻtkazib yuborish — koʻp savolda javobni
  yarim yoʻlda qoldiradi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Factor: 6<i>x</i> + 9</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">3(2<i>x</i> + 3) — 6 va 9 ning EKUBi 3.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Factor: 5<i>x</i><sup>2</sup> − 15<i>x</i></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">5<i>x</i>(<i>x</i> − 3) — son 5, harf x (eng kichik
  daraja).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Factor: 12<i>x</i><sup>2</sup><i>y</i> − 18<i>xy</i><sup>2</sup></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">6<i>xy</i>(2<i>x</i> − 3<i>y</i>) — 12 va 18 ning EKUBi 6,
  har ikki harfdan bittadan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Factor by grouping: <i>x</i><sup>3</sup> + 4<i>x</i><sup>2</sup> + 3<i>x</i> + 12</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(<i>x</i> + 4)(<i>x</i><sup>2</sup> + 3) —
  x<sup>2</sup>(x + 4) + 3(x + 4).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A rectangle has an area of 2<i>x</i><sup>2</sup> + 6<i>x</i>. Write its dimensions as
  a product.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">2<i>x</i>(<i>x</i> + 3) — tomonlari 2x va (x + 3) boʻlishi
  mumkin. Ajratish geometriyada «tomonlarni topish» degani.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>factor</b><span>koʻpaytuvchilarga ajratmoq</span></li>
  <li><b>factor completely</b><span>toʻliq ajratmoq</span></li>
  <li><b>greatest common factor</b><span>eng katta umumiy koʻpaytuvchi</span></li>
  <li><b>grouping</b><span>guruhlash usuli</span></li>
  <li><b>common factor</b><span>umumiy koʻpaytuvchi</span></li>
  <li><b>expand to check</b><span>tekshirish uchun qavsni ochish</span></li>
  <li><b>lowest power</b><span>eng kichik daraja</span></li>
  <li><b>dimensions</b><span>oʻlchamlar (tomonlar)</span></li>
  <li><b>product</b><span>koʻpaytma</span></li>
  <li><b>equivalent</b><span>teng kuchli</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>GCF har doim birinchi</b>: sonlar uchun EKUB, harflar uchun eng kichik
        daraja.</li>
    <li>Toʻrt had boʻlsa — <b>ikkitadan guruhlang</b>; qavs ichidagilar bir xil
        chiqishi kerak.</li>
    <li>Javobni <b>qavsni ochib</b> tekshiring, va «completely» soʻzini
        oʻqing.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-30 — difference of squares & perfect square trinomials
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-30: Factoring: Difference of Squares and Perfect Square Trinomials",
        "category": "math",
        "order": 30,
        "summary": (
            "Ikki formula: kvadratlar ayirmasi va toʻliq kvadrat uchhadi. Ularni "
            "tanish SAT'da eng tez ochkolardan biri — hatto ogʻzaki hisobda ham."
        ),
        "stories": ["The Trader's Two Squares"],
        "content": """
<h2>SAT-30: Factoring: Difference of Squares and Perfect Square Trinomials</h2>

<p>Ba'zi koʻphadlar shunchalik tez-tez uchraydiki, ularni ajratishni <u>hisoblamasdan</u>
tanib olish kerak. SAT'da ikkitasi boshqalardan koʻra koʻproq chiqadi, va ikkalasi ham
<mark>bir qarashda taniladigan shakl</mark>ga ega.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>kvadratlar ayirmasini bir qarashda ajratasiz;</li>
    <li>toʻliq kvadrat uchhadini tanib olasiz;</li>
    <li>kvadratlar <em>yigʻindisi</em> ajratilmasligini bilasiz;</li>
    <li>bu formulani ogʻzaki hisobda ham ishlatasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Two patterns</span>
  <span class="pe-chip pe-chip--v">a<sup>2</sup> − b<sup>2</sup> = (a − b)(a + b)</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">a<sup>2</sup> ± 2ab + b<sup>2</sup> = (a ± b)<sup>2</sup></span>
</div>

<h3>Kvadratlar ayirmasi</h3>

<p>Ikki toʻliq kvadrat, orasida <strong>minus</strong> — bu shakl har doim ikki qavsga
ajraladi, va oʻrtada hech qanday had yoʻq.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Ifoda</th><th>a va b</th><th>Ajratmasi</th></tr>
  <tr><td>x<sup>2</sup> − 25</td><td class="pm-word__sym">x va 5</td><td>(x − 5)(x + 5)</td></tr>
  <tr><td>9x<sup>2</sup> − 16</td><td class="pm-word__sym">3x va 4</td><td>(3x − 4)(3x + 4)</td></tr>
  <tr><td>49x<sup>2</sup> − 4</td><td class="pm-word__sym">7x va 2</td><td>(7x − 2)(7x + 2)</td></tr>
</table></div>

<p>Nega ishlaydi? Qavslarni oching (SAT-28): (x − 5)(x + 5) = x<sup>2</sup> + 5x − 5x − 25,
va oʻrtadagi ikki had <u>bir-birini yoʻqotadi</u>. Aynan shu narsa SAT-26 dagi qoʻshma
ifodani ham ishlatgan edi.</p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Kvadratlar <b>yigʻindisi</b> — x<sup>2</sup> + 25 — butun sonlar bilan ajratilmaydi.
  SAT buni bilib turib javoblar orasiga (x + 5)(x + 5) ni qoʻyadi; oching va koʻring:
  u x<sup>2</sup> + 10x + 25 beradi.
</div>

<h3>Toʻliq kvadrat uchhadi</h3>

<p>Uchta had, chetlaridagi ikkitasi toʻliq kvadrat, oʻrtadagisi esa aynan
<strong>ikki karra</strong> ularning ildizlari koʻpaytmasi — bu bitta qavsning kvadrati.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x<sup>2</sup> + 10x + 25</span>
    <span class="pm-solve__why">Chetlari: x<sup>2</sup> va 25 — ildizlari x va 5</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2 × x × 5 = 10x ✓</span>
    <span class="pm-solve__why">Oʻrtadagi had mos keldi — demak shakl toʻgʻri</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">(x + 5)<sup>2</sup></span>
    <span class="pm-solve__why">Oʻrtadagi had musbat boʻlgani uchun qavsda ham plyus</span>
  </div>
</div>

<p>Xuddi shunday, <em>x</em><sup>2</sup> − 12<em>x</em> + 36 = (<em>x</em> − 6)<sup>2</sup>:
chetlari x va 6, oʻrtasi 2 × 6 = 12, ishorasi manfiy.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻrtadagi hadni <b>tekshirish</b> shart. x<sup>2</sup> + 7x + 25 da chetlari toʻliq
  kvadrat, lekin 2 × 5 = 10 ≠ 7 — demak bu toʻliq kvadrat uchhadi <b>emas</b> va
  formulani qoʻllab boʻlmaydi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikki qavsning ishorasi kvadratlar ayirmasida <b>albatta har xil</b> boʻladi, lekin
  qaysi biri oldin yozilishi ahamiyatsiz: (x − 5)(x + 5) va (x + 5)(x − 5) bir xil.
  Koʻpaytirish tartibi natijani oʻzgartirmaydi.
</div>

<h3>Ogʻzaki hisobdagi foydasi</h3>

<p>Formulaning eng chiroyli qoʻllanishi — ikki katta sonning kvadratlari ayirmasi.
51<sup>2</sup> − 49<sup>2</sup> ni hisoblash uchun ikkala kvadratni bilish shart emas:</p>

<div class="pe-ex">
  <p class="pe-ex__math">51<sup>2</sup> − 49<sup>2</sup> = (51 − 49)(51 + 49) = 2 × 100 = 200</p>
  <p class="pe-ex__uz">Ikki ayirma, bitta koʻpaytirish — hammasi ogʻzaki.</p>
  <p class="pe-ex__why">Tekshiruv: 2,601 − 2,401 = 200 ✓</p>
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>difference of squares</b><span>kvadratlar ayirmasi</span></li>
  <li><b>perfect square trinomial</b><span>toʻliq kvadrat uchhadi</span></li>
  <li><b>factor the expression</b><span>ifodani koʻpaytuvchilarga ajrating</span></li>
  <li><b>which of the following is a factor of</b><span>quyidagilardan qaysi biri koʻpaytuvchi</span></li>
  <li><b>cannot be factored</b><span>ajratib boʻlmaydi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">40 s</span></p>
  <div class="ps-stem__q">
    <p>Which expression is equivalent to 49<i>x</i><sup>2</sup> − 4?</p>
  </div>
  <ol class="ps-ch">
    <li>(7<i>x</i> − 2)(7<i>x</i> + 2)</li>
    <li>(7<i>x</i> − 2)<sup>2</sup></li>
    <li>(49<i>x</i> − 4)(<i>x</i> + 1)</li>
    <li>(7<i>x</i> − 4)(7<i>x</i> + 1)</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) (7x − 2)(7x + 2)</p>
      <p>49<i>x</i><sup>2</sup> ning ildizi 7<i>x</i>, 4 niki 2 — kvadratlar
      ayirmasi.</p>
      <p><b>(7x − 2)<sup>2</sup></b> ochilganda 49x<sup>2</sup> − 28x + 4 beradi —
      oʻrtada had paydo boʻladi, bizda esa u yoʻq.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">(7x − 2)<sup>2</sup></span>
  <span class="ps-trap__why">Ikki shakl adashtirilgan. Kvadratlar ayirmasida qavslar
  <b>har xil ishorali</b>, toʻliq kvadratda esa ikkalasi bir xil.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>Which expression is equivalent to <i>x</i><sup>2</sup> − 14<i>x</i> + 49?</p>
  </div>
  <ol class="ps-ch">
    <li>(<i>x</i> − 7)<sup>2</sup></li>
    <li>(<i>x</i> + 7)<sup>2</sup></li>
    <li>(<i>x</i> − 7)(<i>x</i> + 7)</li>
    <li>(<i>x</i> − 14)(<i>x</i> + 49)</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) (x − 7)<sup>2</sup></p>
      <p>Chetlari x va 7; oʻrtasi 2 × 7 = 14 ✓, ishorasi manfiy — demak (x − 7)
      ning kvadrati.</p>
      <p><b>(x − 7)(x + 7)</b> ochilganda x<sup>2</sup> − 49 beradi: oʻrtadagi had
      yoʻqoladi, bizda esa u bor.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">(x + 7)<sup>2</sup></span>
  <span class="ps-trap__why">Ishora eʼtiborsiz qolgan. Oʻrtadagi had <b>manfiy</b>,
  demak qavsda ham minus boʻlishi kerak.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Ajratish savolida shaklni uch savol bilan aniqlang:</p>
  <ol>
    <li><b>Nechta had bor?</b> Ikkita va orasida minus → kvadratlar ayirmasi.</li>
    <li>Uchta had boʻlsa: chetlari toʻliq kvadratmi?</li>
    <li>Ha boʻlsa: oʻrtadagi had <b>ikki karra</b> ildizlar koʻpaytmasimi? Ha —
        toʻliq kvadrat; yoʻq — oddiy ajratish (SAT-31).</li>
  </ol>
  <p>Va har doim <b>GCF dan boshlang</b> (SAT-29): 2x<sup>2</sup> − 18 avval
  2(x<sup>2</sup> − 9) boʻladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">x<sup>2</sup> + 25 = (x + 5)(x + 5)</p>
  <p class="pe-good">x<sup>2</sup> + 25 ajratilmaydi.</p>
  <p class="pe-fix__why">Oching: (x + 5)(x + 5) = x<sup>2</sup> + 10x + 25. Kvadratlar
  <b>yigʻindisi</b> ajralmaydi — faqat ayirmasi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">9x<sup>2</sup> − 16 = (3x − 16)(3x + 16)</p>
  <p class="pe-good">(3x − 4)(3x + 4)</p>
  <p class="pe-fix__why">Qavsga sonning oʻzi emas, uning <b>ildizi</b> yoziladi:
  √16 = 4.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu ikki formula keyingi darslarning poydevori: kvadrat tenglamani yechishda (SAT-31),
  ratsional ifodani qisqartirishda (SAT-41) va parabolaning nollarini topishda ular
  qayta-qayta ishlatiladi. Shuning uchun ularni <b>tanib olish</b> hisoblashdan
  muhimroq.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Factor: <i>x</i><sup>2</sup> − 36</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(<i>x</i> − 6)(<i>x</i> + 6) — kvadratlar ayirmasi,
  ildizlari x va 6.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Factor: 4<i>x</i><sup>2</sup> − 9</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(2<i>x</i> − 3)(2<i>x</i> + 3) — √(4x²) = 2x va
  √9 = 3.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Factor: <i>x</i><sup>2</sup> + 8<i>x</i> + 16</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(<i>x</i> + 4)<sup>2</sup> — chetlari x va 4, oʻrtasi
  2 × 4 = 8 ✓</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Factor: <i>x</i><sup>2</sup> − 20<i>x</i> + 100</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(<i>x</i> − 10)<sup>2</sup> — oʻrtasi 2 × 10 = 20, ishorasi
  manfiy.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Without a calculator, work out 103<sup>2</sup> − 97<sup>2</sup>.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">1,200 — (103 − 97)(103 + 97) = 6 × 200. Ikkala kvadratni
  hisoblash umuman kerak emas.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>difference of squares</b><span>kvadratlar ayirmasi</span></li>
  <li><b>sum of squares</b><span>kvadratlar yigʻindisi (ajralmaydi)</span></li>
  <li><b>perfect square trinomial</b><span>toʻliq kvadrat uchhadi</span></li>
  <li><b>a factor of</b><span>…ning koʻpaytuvchisi</span></li>
  <li><b>cannot be factored</b><span>ajratib boʻlmaydi</span></li>
  <li><b>middle term</b><span>oʻrtadagi had</span></li>
  <li><b>square root</b><span>kvadrat ildiz</span></li>
  <li><b>pattern</b><span>shakl, andoza</span></li>
  <li><b>recognise</b><span>tanib olmoq</span></li>
  <li><b>mentally</b><span>ogʻzaki (hisoblab)</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Ikki toʻliq kvadrat va <b>minus</b> → (a − b)(a + b); oʻrtada had
        boʻlmaydi.</li>
    <li>Uchhadda oʻrtadagi had <b>2ab</b> boʻlsa → (a ± b)<sup>2</sup>, ishorasi
        oʻrtadagi haddan.</li>
    <li>Kvadratlar <b>yigʻindisi</b> ajralmaydi — va bu SAT'ning doimiy tuzogʻi.</li>
  </ul>
</div>
""",
    },
]
