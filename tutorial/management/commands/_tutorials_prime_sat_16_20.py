# -*- coding: utf-8 -*-
"""Prime SAT Math — lessons 16–20 (systems of linear equations).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_SAT.md
Lesson list: tutorial/management/commands/toc_prime_sat_math.txt

  mashqlar — practice/management/commands/_practice_ps_16_20.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_sat_readings_16_20.py

⚠️ ESKI SAT-16 … SAT-20 ustiga yoziladi (--republish).
⚠️ Til: sarlavha va test savollari inglizcha, tushuntirish oʻzbekcha. Son: 3.5 va 1,200.

⚠️ Kumulyativ (SAT-1…15 erkin: ifoda, tenglama, matndan tenglama, modul, qiyalik va
   uning formulasi, y = mx + b, point-slope/standart shakl, chizish, kontekst, parallel,
   perpendikulyar, tengsizliklar):
  • SAT-16 — sistema tushunchasi va oʻrniga qoʻyish usuli. Yechim — NUQTA.
  • SAT-17 — yoʻqotish (elimination) usuli; kerak boʻlsa oldin koʻpaytirish;
    SAT'ning sevimli qisqa yoʻli: ikki tenglamani qoʻshib x + y ni topish.
  • SAT-18 — matndan sistema tuzish (soni + qiymati, yigʻindi + ayirma).
  • SAT-19 — cheksiz koʻp yechim: bir tenglama ikkinchisining karrasi.
  • SAT-20 — yechim yoʻq: bir xil qiyalik, boshqa oʻzgarmas had. Blokning yakuni —
    uchala holatni bir jadvalda birlashtiradi (SAT-2 va SAT-11 ga qaytish).
  • ⛔ Kvadrat sistema (SAT-38) YOʻQ; modulli tengsizlik (SAT-22) YOʻQ; ps-desmos SAT-83 dan.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_sat_16_20.py \\
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
    # SAT-16 — substitution
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-16: Systems of Linear Equations: Solving by Substitution",
        "category": "math",
        "order": 16,
        "summary": (
            "Ikki tenglama, ikki nomaʼlum va bitta yechim — nuqta. Bitta harfni "
            "yolgʻiz qoldirib, uni ikkinchi tenglamaga qoʻyish: SAT'da eng koʻp "
            "ishlaydigan usul."
        ),
        "stories": ["Two Receipts"],
        "content": """
<h2>SAT-16: Systems of Linear Equations: Solving by Substitution</h2>

<p>Shu paytgacha har bir tenglamada bitta nomaʼlum bor edi. Endi ikkitasi bor — va shuning
uchun bitta tenglama yetmaydi: <mark>ikki nomaʼlumni topish uchun ikkita shart kerak</mark>.
Ikkita tenglama birga <strong>system</strong> deb ataladi, va SAT'ning har bir modulida
ulardan bir nechtasi bor.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>sistemaning yechimi nima ekanini bilasiz — u son emas, <em>nuqta</em>;</li>
    <li>bitta harfni yolgʻiz qoldirib, uni ikkinchi tenglamaga qoʻyasiz;</li>
    <li>ikkinchi nomaʼlumni orqaga qoʻyib topasiz va ikkala tenglamada tekshirasiz;</li>
    <li>savol <em>x</em> ni emas, <em>x</em> + <em>y</em> ni soʻraganini payqaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">A system</span>
  <span class="pe-chip pe-chip--s">tenglama 1</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">tenglama 2</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">(x, y)</span>
</div>

<h3>Yechim — bu nuqta</h3>

<p>Sistemaning yechimi — <u>ikkala</u> tenglamani bir vaqtda rost qiladigan
(<em>x</em>, <em>y</em>) juftligi. Grafik tilida bu ikki chiziqning
<strong>kesishgan nuqtasi</strong>: u birinchi chiziqda ham, ikkinchisida ham yotadi.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Shuning uchun javobni <b>ikkala</b> tenglamada tekshirish kerak. Faqat bittasida
  tekshirish — yarim tekshiruv; xato koʻpincha aynan ikkinchisida chiqadi.
</div>

<h3>Oʻrniga qoʻyish — qachon eng tez</h3>

<blockquote>Agar bir tenglamada harflardan biri <u>allaqachon yolgʻiz</u> tursa
(<em>y</em> = … yoki <em>x</em> = …), oʻrniga qoʻyish usuli eng tez yoʻl.</blockquote>

<p>Uch qadam: <strong>izolyatsiya → qoʻyish → orqaga qoʻyish</strong>.</p>

<h3>Misol 1 (oson)</h3>

<p><em>y</em> = 2<em>x</em> + 1 va 3<em>x</em> + <em>y</em> = 11.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x + (2x + 1) = 11</span>
    <span class="pm-solve__why">y ning oʻrniga 2x + 1 ni qoʻydik — endi bitta nomaʼlum</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5x + 1 = 11  →  x = 2</span>
    <span class="pm-solve__why">Oddiy chiziqli tenglama (SAT-2)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">y = 2(2) + 1 = 5  →  (2, 5)</span>
    <span class="pm-solve__why">x ni birinchi tenglamaga <b>orqaga qoʻydik</b></span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Birinchi: 5 = 2(2) + 1 ✓. Ikkinchi: 3(2) + 5 = 11 ✓ — ikkala tenglama ham rost.</p>
</div>

<h3>Misol 2 (oʻrta) — x yolgʻiz turganda</h3>

<p><em>x</em> = <em>y</em> − 3 va 2<em>x</em> + 3<em>y</em> = 19.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2(y − 3) + 3y = 19</span>
    <span class="pm-solve__why">x ning oʻrniga y − 3 ni <b>qavs bilan</b> qoʻydik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2y − 6 + 3y = 19  →  5y = 25</span>
    <span class="pm-solve__why">Qavs ochildi, oʻxshash hadlar qoʻshildi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">y = 5, x = 5 − 3 = 2  →  (2, 5)</span>
    <span class="pm-solve__why">Orqaga qoʻydik</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Oʻrniga qoʻyganda <b>qavs</b> yozing: 2(<em>y</em> − 3), 2<em>y</em> − 3 emas.
  Qavssiz qoʻyish shu mavzudagi eng koʻp uchraydigan xato va u javobni butunlay
  oʻzgartiradi.
</div>

<h3>Misol 3 (SAT darajasi) — avval izolyatsiya qilish kerak</h3>

<p>2<em>x</em> + <em>y</em> = 7 va 3<em>x</em> − 2<em>y</em> = 7.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">y = 7 − 2x</span>
    <span class="pm-solve__why">Birinchi tenglamada y ni yolgʻiz qoldirdik — koeffitsienti 1, eng qulayi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x − 2(7 − 2x) = 7</span>
    <span class="pm-solve__why">Ikkinchi tenglamaga qoʻydik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x − 14 + 4x = 7  →  7x = 21</span>
    <span class="pm-solve__why">−2 × (−2x) = <b>+4x</b> — ishoraga eʼtibor</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 3, y = 7 − 6 = 1  →  (3, 1)</span>
    <span class="pm-solve__why">Tekshiruv: 2(3) + 1 = 7 ✓ va 3(3) − 2(1) = 7 ✓</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Qaysi harfni izolyatsiya qilish kerak? <b>Koeffitsienti 1 boʻlganini</b> — shunda kasr
  paydo boʻlmaydi. Yuqorida <em>y</em> tanlandi, chunki uning oldida son yoʻq edi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Sistemada ikkita tenglama <b>bir vaqtda</b> bajarilishi kerak — shuning uchun ular
  «va» bilan bogʻlangan, «yoki» bilan emas. Bitta tenglamani qanoatlantirgan nuqta
  yechim boʻlmaydi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>the solution to the system</b><span>sistemaning yechimi — (x, y) juftligi</span></li>
  <li><b>what is the value of x + y</b><span>x + y ning qiymati — ikkalasini topib qoʻshing</span></li>
  <li><b>if (a, b) is the solution</b><span>agar (a, b) yechim boʻlsa — a bu x, b bu y</span></li>
  <li><b>satisfies both equations</b><span>ikkala tenglamani ham qanoatlantiradi</span></li>
  <li><b>the point of intersection</b><span>kesishish nuqtasi — yechimning grafikdagi nomi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p><i>y</i> = 3<i>x</i> − 4</p>
    <p>2<i>x</i> + <i>y</i> = 11</p>
    <p>If (<i>x</i>, <i>y</i>) is the solution to the system above, what is the value of
    <i>x</i> + <i>y</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>3</li>
    <li>5</li>
    <li>8</li>
    <li>15</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 8</p>
      <div class="pm-solve">
        <div class="pm-solve__row">
          <span class="pm-solve__step">2x + (3x − 4) = 11</span>
          <span class="pm-solve__why">y ning oʻrniga qoʻydik</span>
        </div>
        <div class="pm-solve__row">
          <span class="pm-solve__step">5x = 15  →  x = 3</span>
          <span class="pm-solve__why">4 ni qoʻshdik, 5 ga boʻldik</span>
        </div>
        <div class="pm-solve__row pm-solve__row--ans">
          <span class="pm-solve__step">y = 3(3) − 4 = 5, x + y = 8</span>
          <span class="pm-solve__why">Savol yigʻindini soʻradi</span>
        </div>
      </div>
      <p>Ikkala son ham — 3 va 5 — javoblar orasida turibdi. Sistema savollarida oxirgi
      jumlani ikki marta oʻqish shart.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">3</span>
  <span class="ps-trap__why">Bu <b>x</b> ning qiymati. Sistemani toʻgʻri yechib, savolni
  oxirigacha oʻqimaslik — bu mavzudagi eng qimmat xato.</span>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">15</span>
  <span class="ps-trap__why">5x = 15 da toʻxtab qolgan javob. Yarim yoʻldagi son har
  doim variantlar orasida boʻladi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p><i>x</i> + 2<i>y</i> = 10</p>
    <p><i>x</i> = <i>y</i> + 1</p>
    <p>If (<i>a</i>, <i>b</i>) is the solution to the system above, what is the value of
    <i>a</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>3</li>
    <li>4</li>
    <li>7</li>
    <li>10</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 4</p>
      <p>(<i>a</i>, <i>b</i>) — bu (<i>x</i>, <i>y</i>), demak <b>a bu x</b>.</p>
      <div class="pm-solve">
        <div class="pm-solve__row">
          <span class="pm-solve__step">(y + 1) + 2y = 10  →  3y = 9  →  y = 3</span>
          <span class="pm-solve__why">x ning oʻrniga y + 1 ni qoʻydik</span>
        </div>
        <div class="pm-solve__row pm-solve__row--ans">
          <span class="pm-solve__step">x = 3 + 1 = 4</span>
          <span class="pm-solve__why">Tekshiruv: 4 + 2(3) = 10 ✓</span>
        </div>
      </div>
      <p><b>3</b> — bu <i>b</i>, yaʼni <i>y</i>. Harflar oʻzgarganda ham tartib oʻsha:
      birinchisi x, ikkinchisi y.</p>
    </div>
  </details>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Sistemani koʻrganingizda 5 soniyada usul tanlang:</p>
  <ol>
    <li>Bir harf <b>yolgʻiz</b> turibdimi (y = … yoki x = …)? → oʻrniga qoʻying.</li>
    <li>Koeffitsienti 1 boʻlgan harf bormi? → uni izolyatsiya qiling.</li>
    <li>Ikkalasi ham yoʻqmi? → yoʻqotish usuli tezroq (SAT-17).</li>
  </ol>
  <p>Va oxirida <b>savolni qayta oʻqing</b>: u koʻpincha x ni emas, x + y yoki 2y ni
  soʻraydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">x = y − 3 ni qoʻyganda: 2y − 3 + 3y = 19</p>
  <p class="pe-good">2(y − 3) + 3y = 19</p>
  <p class="pe-fix__why">Butun ifoda x ning oʻrnini egallaydi, demak u <b>qavs ichida</b>
  koʻpaytiriladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">x = 3 topildi → javob 3.</p>
  <p class="pe-good">Savol x + y ni soʻragan boʻlsa, javob 8.</p>
  <p class="pe-fix__why">Sistemaning yechimi <b>ikkita</b> son. Qaysi biri (yoki qaysi
  ifoda) soʻralganini savolning oxirgi jumlasi aytadi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Yechimni <b>nuqta</b> koʻrinishida yozib qoʻying: (3, 1). Shunda «qaysi biri x edi?»
  degan savol tugʻilmaydi va tekshirish ham osonlashadi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Solve: <i>y</i> = <i>x</i> + 2 and 3<i>x</i> + <i>y</i> = 10</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(2, 4) — 3x + x + 2 = 10 → 4x = 8 → x = 2, keyin y = 4.
  Tekshiruv: 3(2) + 4 = 10 ✓</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Solve: <i>x</i> = 2<i>y</i> and <i>x</i> + <i>y</i> = 12</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(8, 4) — 2y + y = 12 → 3y = 12 → y = 4, keyin x = 8.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Solve: <i>y</i> = 5 − <i>x</i> and 2<i>x</i> + <i>y</i> = 8</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(3, 2) — 2x + 5 − x = 8 → x + 5 = 8 → x = 3, keyin y = 2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Where do <i>y</i> = 4<i>x</i> and <i>y</i> = <i>x</i> + 6 intersect?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(2, 8) — ikkala chiziq ham y ga yechilgan, demak
  4x = x + 6 → 3x = 6 → x = 2, va y = 8.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Two numbers add to 30, and one is 4 more than the other. What are they?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">17 va 13 — x + y = 30 va x = y + 4 → (y + 4) + y = 30 →
  2y = 26 → y = 13, x = 17.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>system of equations</b><span>tenglamalar sistemasi</span></li>
  <li><b>substitution</b><span>oʻrniga qoʻyish usuli</span></li>
  <li><b>the solution to the system</b><span>sistemaning yechimi — (x, y)</span></li>
  <li><b>satisfies both equations</b><span>ikkala tenglamani ham qanoatlantiradi</span></li>
  <li><b>point of intersection</b><span>kesishish nuqtasi</span></li>
  <li><b>isolate</b><span>yolgʻiz qoldirish</span></li>
  <li><b>substitute into</b><span>… ga qoʻyish</span></li>
  <li><b>ordered pair</b><span>tartiblangan juftlik (x, y)</span></li>
  <li><b>simultaneously</b><span>bir vaqtda</span></li>
  <li><b>back-substitute</b><span>orqaga qoʻyish (ikkinchi harfni topish uchun)</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Yechim — <b>nuqta</b>, ikkala tenglamani ham rost qiladigan (x, y).</li>
    <li>Oʻrniga qoʻyganda <b>qavs</b> yozing va koeffitsienti 1 boʻlgan harfni tanlang.</li>
    <li>Ikkala sonni topib, <b>savolni qayta oʻqing</b>: u x + y ni soʻragan boʻlishi
        mumkin.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-17 — elimination
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-17: Systems of Linear Equations: Solving by Elimination",
        "category": "math",
        "order": 17,
        "summary": (
            "Ikki tenglamani qoʻshib yoki ayirib, bitta nomaʼlumni butunlay "
            "yoʻqotish. Kerak boʻlsa avval koʻpaytiramiz — va SAT'ning sevimli "
            "qisqa yoʻli: qoʻshishning oʻzi x + y ni beradi."
        ),
        "stories": ["The Balance and Two Weighings"],
        "content": """
<h2>SAT-17: Systems of Linear Equations: Solving by Elimination</h2>

<p>Oʻrniga qoʻyish usuli bitta harf yolgʻiz turganda ajoyib ishlaydi. Lekin
2<em>x</em> + 3<em>y</em> = 12 va 4<em>x</em> − 3<em>y</em> = 6 kabi sistemada hech qaysi
harf yolgʻiz emas, va izolyatsiya kasrlar keltirib chiqaradi. Bunday holatda ikkinchi usul
tezroq: <mark>ikki tenglamani bir-biriga qoʻshib, nomaʼlumlardan birini butunlay
yoʻqotish</mark>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>koeffitsientlar qarama-qarshi boʻlganda tenglamalarni qoʻshasiz;</li>
    <li>bir xil boʻlganda ayirasiz;</li>
    <li>hech qaysisi mos kelmasa, avval koʻpaytirib mos qilasiz;</li>
    <li>SAT soʻraydigan <em>x</em> + <em>y</em> ni koʻpincha bitta qoʻshish bilan olasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Elimination</span>
  <span class="pe-chip pe-chip--o">+3y</span>
  <span class="pe-op">va</span>
  <span class="pe-chip pe-chip--neg">−3y</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">qoʻshsak yoʻqoladi</span>
</div>

<h3>Nega qoʻshish mumkin</h3>

<p>Tenglama — bu ikki tomonning teng ekani. Teng narsalarni teng narsalarga qoʻshsak,
tenglik saqlanadi. Shuning uchun chap tomonlarni chap tomonlarga, oʻng tomonlarni oʻng
tomonlarga qoʻshish mumkin — va agar bir harfning koeffitsientlari
<u>qarama-qarshi</u> boʻlsa, u yoʻqoladi.</p>

<h3>Misol 1 (oson) — qoʻshish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + y = 10<br>x − y = 4</span>
    <span class="pm-solve__why">y ning koeffitsientlari +1 va −1 — qarama-qarshi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x = 14  →  x = 7</span>
    <span class="pm-solve__why">Ikki tenglamani qoʻshdik, y yoʻqoldi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">7 + y = 10  →  y = 3  →  (7, 3)</span>
    <span class="pm-solve__why">x ni istalgan tenglamaga orqaga qoʻydik</span>
  </div>
</div>

<h3>Misol 2 (oʻrta)</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + 3y = 12<br>4x − 3y = 6</span>
    <span class="pm-solve__why">+3y va −3y — qoʻshsak yoʻqoladi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">6x = 18  →  x = 3</span>
    <span class="pm-solve__why">2x + 4x = 6x va 12 + 6 = 18</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2(3) + 3y = 12  →  y = 2  →  (3, 2)</span>
    <span class="pm-solve__why">Tekshiruv: 4(3) − 3(2) = 6 ✓</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Koeffitsientlar <b>bir xil</b> boʻlsa (masalan +3y va +3y), qoʻshish emas,
  <b>ayirish</b> kerak. Ayirishda esa oʻng tomonni ham ayirishni unutmang va har bir
  hadning ishorasini almashtiring — bu yerda xato koʻp boʻladi.
</div>

<h3>Misol 3 (SAT darajasi) — avval koʻpaytiring</h3>

<p>3<em>x</em> + 4<em>y</em> = 10 va 2<em>x</em> + <em>y</em> = 5. Hech qaysi koeffitsient
mos kelmaydi, shuning uchun ikkinchi tenglamani <strong>4 ga koʻpaytiramiz</strong>.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">8x + 4y = 20</span>
    <span class="pm-solve__why">Ikkinchi tenglamaning <b>hamma hadi</b> 4 ga koʻpaytirildi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(8x + 4y) − (3x + 4y) = 20 − 10</span>
    <span class="pm-solve__why">Endi 4y ikkalasida ham bor — ayiramiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">5x = 10  →  x = 2, y = 1</span>
    <span class="pm-solve__why">Tekshiruv: 3(2) + 4(1) = 10 ✓ va 2(2) + 1 = 5 ✓</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Koʻpaytirganda <b>oʻng tomon ham</b> koʻpayadi: 2<i>x</i> + <i>y</i> = 5 ni 4 ga
  koʻpaytirsak 8<i>x</i> + 4<i>y</i> = <b>20</b>, 5 emas. Faqat chap tomonni
  koʻpaytirish — bu mavzudagi klassik xato.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Koʻpaytiruvchini tanlashda <b>kichigini</b> qidiring: 3 va 2 uchun 6 ga chiqarish
  shart emas — koʻpincha bitta tenglamani koʻpaytirish yetadi. Ortiqcha katta sonlar
  faqat hisobni ogʻirlashtiradi va xato ehtimolini oshiradi.
</div>

<h3>SAT'ning qisqa yoʻli: javob koʻpincha qoʻshishning oʻzida</h3>

<p>Testda sistema koʻpincha <em>x</em> ni emas, <strong><em>x</em> + <em>y</em></strong> ni
soʻraydi. Va koʻp savolda ikki tenglamani shunchaki qoʻshishning oʻzi javobni beradi —
har bir nomaʼlumni alohida topmasdan.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x + 2y = 14<br>2x + 3y = 11</span>
    <span class="pm-solve__why">Berilgan sistema</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5x + 5y = 25</span>
    <span class="pm-solve__why">Ikkalasini qoʻshdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x + y = 5</span>
    <span class="pm-solve__why">Hamma hadni 5 ga boʻldik — 15 soniyada tugadi</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Savol <em>x</em> + <em>y</em> yoki <em>x</em> − <em>y</em> ni soʻrasa, avval
  <b>qoʻshib va ayirib koʻring</b>. Koeffitsientlar simmetrik boʻlsa (3 va 2, keyin 2 va 3),
  javob deyarli har doim bitta amalda chiqadi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>what is the value of x + y</b><span>x + y qancha — qoʻshib koʻring</span></li>
  <li><b>eliminate one variable</b><span>bitta nomaʼlumni yoʻqotish</span></li>
  <li><b>multiply the second equation by</b><span>ikkinchi tenglamani … ga koʻpaytiring</span></li>
  <li><b>add the equations</b><span>tenglamalarni qoʻshing</span></li>
  <li><b>which of the following gives</b><span>quyidagilardan qaysi biri … beradi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>2<i>x</i> + 3<i>y</i> = 12</p>
    <p>4<i>x</i> − 3<i>y</i> = 6</p>
    <p>What is the value of <i>x</i> in the solution to the system above?</p>
  </div>
  <ol class="ps-ch">
    <li>2</li>
    <li>3</li>
    <li>6</li>
    <li>18</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 3</p>
      <p>+3<i>y</i> va −3<i>y</i> qarama-qarshi, shuning uchun qoʻshamiz:
      6<i>x</i> = 18, demak <i>x</i> = 3.</p>
      <p><b>18</b> — 6x = 18 da toʻxtab qolgan javob; <b>2</b> — bu <i>y</i>, x emas.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">2</span>
  <span class="ps-trap__why">Bu <i>y</i> ning qiymati. Sistema toʻgʻri yechilgan, lekin
  savol <b>x</b> ni soʻragan edi — ikki javob ham variantlar orasida turadi.</span>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">18</span>
  <span class="ps-trap__why">6<i>x</i> = 18 dan keyin 6 ga boʻlish qilinmagan. Har
  qoʻshishdan keyin «hali boʻlish qoldimi?» deb soʻrang.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>3<i>x</i> + 2<i>y</i> = 14</p>
    <p>2<i>x</i> + 3<i>y</i> = 11</p>
    <p>What is the value of <i>x</i> + <i>y</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>3</li>
    <li>4</li>
    <li>5</li>
    <li>25</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 5</p>
      <p>Ikki tenglamani qoʻshamiz: 5<i>x</i> + 5<i>y</i> = 25, keyin 5 ga boʻlamiz:
      <i>x</i> + <i>y</i> = 5. Har bir nomaʼlumni alohida topish shart emas.</p>
      <p>(Xohlasangiz: ayirish x − y = 3 beradi, va ikkalasidan x = 4, y = 1 — lekin
      bu qoʻshimcha ish.)</p>
      <p><b>25</b> — boʻlishdan oldingi son; <b>4</b> — bu <i>x</i>.</p>
    </div>
  </details>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Sistemani koʻrganingizda ikki savol bering:</p>
  <ol>
    <li>Bir harfning koeffitsientlari <b>qarama-qarshi</b>mi? → qoʻshing.</li>
    <li><b>Bir xil</b>mi? → ayiring.</li>
    <li>Ikkalasi ham yoʻqmi? → bittasini koʻpaytirib mos qiling (kichikroq songa).</li>
  </ol>
  <p>Va savol <em>x</em> + <em>y</em> ni soʻrasa, avval shunchaki qoʻshib koʻring — bu
  eng tez ochkolardan biri.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">2x + y = 5 ni 4 ga koʻpaytirdik: 8x + 4y = 5</p>
  <p class="pe-good">8x + 4y = 20</p>
  <p class="pe-fix__why">Tenglamaning <b>ikkala tomoni</b> koʻpaytiriladi, aks holda
  tenglik buziladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">(8x + 4y) − (3x + 4y) = 20 − 10 → 5x + 8y = 10</p>
  <p class="pe-good">5x = 10</p>
  <p class="pe-fix__why">Ayirishda 4y − 4y = 0 — u <b>yoʻqoladi</b>, qoʻshilmaydi. Usulning
  butun maqsadi shu.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikkala usul ham (oʻrniga qoʻyish va yoʻqotish) <b>bir xil javob</b> beradi — ular
  faqat yoʻl. Testda vaqtni qaysi biri tejasa, oʻshani tanlang: koeffitsientlar
  «tayyor» boʻlsa yoʻqotish, bir harf yolgʻiz tursa oʻrniga qoʻyish.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Solve: <i>x</i> + <i>y</i> = 9 and <i>x</i> − <i>y</i> = 1</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(5, 4) — qoʻshamiz: 2x = 10 → x = 5, keyin y = 4.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Solve: 2<i>x</i> + <i>y</i> = 7 and 3<i>x</i> − <i>y</i> = 8</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(3, 1) — y ning koeffitsientlari qarama-qarshi: qoʻshsak
  5x = 15 → x = 3, keyin y = 1.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Solve: 4<i>x</i> + 3<i>y</i> = 18 and 4<i>x</i> − 3<i>y</i> = 6</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(3, 2) — qoʻshsak 8x = 24 → x = 3; keyin 12 + 3y = 18 →
  y = 2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Solve: <i>x</i> + 2<i>y</i> = 8 and 3<i>x</i> − <i>y</i> = 3</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(2, 3) — birinchisini 3 ga koʻpaytiramiz: 3x + 6y = 24, keyin
  ikkinchisini ayiramiz: 7y = 21 → y = 3, x = 2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  If 5<i>x</i> + 4<i>y</i> = 20 and 4<i>x</i> + 5<i>y</i> = 16, what is <i>x</i> + <i>y</i>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">4 — qoʻshamiz: 9x + 9y = 36, keyin 9 ga boʻlamiz. Alohida
  yechish kerak emas.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>elimination</b><span>yoʻqotish usuli</span></li>
  <li><b>eliminate a variable</b><span>nomaʼlumni yoʻqotish</span></li>
  <li><b>add / subtract the equations</b><span>tenglamalarni qoʻshish / ayirish</span></li>
  <li><b>multiply both sides</b><span>ikkala tomonni koʻpaytirish</span></li>
  <li><b>opposite coefficients</b><span>qarama-qarshi koeffitsientlar</span></li>
  <li><b>identical coefficients</b><span>bir xil koeffitsientlar</span></li>
  <li><b>the resulting equation</b><span>hosil boʻlgan tenglama</span></li>
  <li><b>back-substitute</b><span>orqaga qoʻyish</span></li>
  <li><b>simultaneous equations</b><span>sistemaning boshqa nomi</span></li>
  <li><b>verify</b><span>tekshirmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Qarama-qarshi koeffitsient — <b>qoʻshing</b>; bir xil — <b>ayiring</b>;
        mos kelmasa — avval koʻpaytiring.</li>
    <li>Koʻpaytirganda <b>oʻng tomon ham</b> koʻpayadi.</li>
    <li>Savol <em>x</em> + <em>y</em> ni soʻrasa, shunchaki <b>qoʻshib koʻring</b> —
        koʻpincha javob bir amalda chiqadi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-18 — word problems with systems
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-18: Word Problems Involving Systems of Linear Equations",
        "category": "math",
        "order": 18,
        "summary": (
            "Ikki nomaʼlum, ikki jumla, ikki tenglama. Chipta va narx, yigʻindi va "
            "ayirma, ikki xil narsaning soni — SAT'da eng koʻp uchraydigan uch oila."
        ),
        "stories": ["The Inspector Counts Legs"],
        "content": """
<h2>SAT-18: Word Problems Involving Systems of Linear Equations</h2>

<p>SAT-3 da bitta nomaʼlumli matnli masalani tenglamaga aylantirgan edik. Endi
nomaʼlum ikkita — kattalar chiptasi va bolalar chiptasi, daftar va ruchka, choy va qahva —
va shuning uchun <mark>matnda ham ikkita jumla</mark> boʻladi. Har bir jumla bitta
tenglama beradi, va ikkalasi birga sistemani hosil qiladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>matndagi ikki jumlani ikki tenglamaga aylantirasiz;</li>
    <li>uchta doimiy oilani tanib olasiz: soni + qiymati, yigʻindi + ayirma, ikki narx;</li>
    <li>harflarni <u>nimaga</u> qoʻyganingizni yozib qoʻyasiz;</li>
    <li>javobni matnga qaytarib tekshirasiz — ikkala shart boʻyicha.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The classic pair</span>
  <span class="pe-chip pe-chip--s">soni: a + c = jami</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">qiymati: 8a + 5c = pul</span>
</div>

<h3>Uch oila — SAT boshqasini deyarli soʻramaydi</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span> Soni va qiymati</p>
    <p>Chiptalar, tangalar, ichimliklar. Birinchi tenglama <b>nechta</b>, ikkinchisi
    <b>qancha pul</b>.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span> Yigʻindi va ayirma</p>
    <p>«Ikki sonning yigʻindisi 54, farqi 8». Eng tez yechiladigan tur — qoʻshish
    usuli bilan (SAT-17).</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span> Ikki xil narx</p>
    <p>Daftar $3, ruchka $2, jami 15 dona va $37. Yuqoridagi birinchi oilaning
    doʻkondagi koʻrinishi.</p>
  </div>
</div>

<h3>Misol 1 (oson) — soni va qiymati</h3>

<p><em>Adult tickets cost $8 and child tickets cost $5. A family bought 20 tickets for
$136. How many adult tickets did they buy?</em></p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">a = adult tickets, c = child tickets</span>
    <span class="pm-solve__why">Avval harflarni aniqladik — <b>nimaning soni</b></span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">a + c = 20<br>8a + 5c = 136</span>
    <span class="pm-solve__why">Birinchi jumla — nechta; ikkinchisi — qancha pul</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">8a + 5(20 − a) = 136</span>
    <span class="pm-solve__why">c = 20 − a ni qoʻydik (SAT-16)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3a + 100 = 136  →  a = 12, c = 8</span>
    <span class="pm-solve__why">8a − 5a = 3a</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Soni: 12 + 8 = 20 ✓. Puli: 8(12) + 5(8) = 96 + 40 = 136 ✓ — <b>ikkala</b> shart ham
  bajarildi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Matnli sistemada tekshiruv ikki qatorli boʻlishi shart: <b>soni</b> toʻgʻrimi va
  <b>puli</b> toʻgʻrimi. Faqat bittasini tekshirgan oʻquvchi notoʻgʻri javobni
  «toʻgʻri» deb qabul qiladi.
</div>

<h3>Misol 2 (oʻrta) — yigʻindi va ayirma</h3>

<p><em>The sum of two numbers is 54 and their difference is 8. What are the numbers?</em></p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + y = 54<br>x − y = 8</span>
    <span class="pm-solve__why">Ikki jumla — ikki tenglama</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x = 62  →  x = 31</span>
    <span class="pm-solve__why">Qoʻshdik — y yoʻqoldi (SAT-17)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">y = 54 − 31 = 23</span>
    <span class="pm-solve__why">Tekshiruv: 31 + 23 = 54 ✓ va 31 − 23 = 8 ✓</span>
  </div>
</div>

<h3>Misol 3 (SAT darajasi) — doʻkon</h3>

<p><em>Notebooks cost $3 each and pens cost $2 each. A customer bought 15 items for $37.
How many notebooks did they buy?</em></p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">n + p = 15<br>3n + 2p = 37</span>
    <span class="pm-solve__why">Soni va qiymati</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3n + 2(15 − n) = 37</span>
    <span class="pm-solve__why">p = 15 − n</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">n + 30 = 37  →  n = 7, p = 8</span>
    <span class="pm-solve__why">Tekshiruv: 3(7) + 2(8) = 21 + 16 = 37 ✓</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  «Soni va qiymati» oilasida <b>doim</b> arzonrogʻining narxini umumiy songa koʻpaytirib
  koʻring: 15 dona × $2 = $30. Haqiqiy pul $37, farq $7, va har bir daftar $1 qimmat —
  demak 7 ta daftar. Bu usul 15 soniya oladi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>how many adult tickets</b><span>nechta kattalar chiptasi — javob <em>soni</em></span></li>
  <li><b>how many more … than</b><span>nechtaga koʻp — javob <em>ayirma</em>, son emas</span></li>
  <li><b>the sum / the difference of</b><span>yigʻindisi / farqi</span></li>
  <li><b>which system of equations represents</b><span>qaysi sistema shu vaziyatni ifodalaydi</span></li>
  <li><b>a total of 20 tickets</b><span>jami 20 ta chipta — bu «soni» tenglamasi</span></li>
</ul>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Savol «<em>which system of equations represents…</em>» desa, sistemani <b>yechish
  shart emas</b> — faqat toʻgʻri tuzilganini tanlang. Bitta qulay son bilan tekshiring:
  20 ta chipta hammasi kattalarniki boʻlsa, pul 8 × 20 = $160 boʻlardi — demak «pul»
  tenglamasida 8 va 5 turishi kerak, 20 emas.
</div>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">90 s</span></p>
  <div class="ps-stem__q">
    <p>Adult tickets to a museum cost $8 each and child tickets cost $5 each. A group
    bought a total of 20 tickets for $136. How many adult tickets did the group buy?</p>
  </div>
  <ol class="ps-ch">
    <li>8</li>
    <li>12</li>
    <li>17</li>
    <li>20</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 12</p>
      <p>a + c = 20 va 8a + 5c = 136. c = 20 − a ni qoʻysak: 3a + 100 = 136, demak
      a = 12 va c = 8.</p>
      <p><b>8</b> — bolalar chiptasi soni; <b>17</b> — 136 ÷ 8, yaʼni «hamma chipta
      kattalarniki» deb hisoblangan javob.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">8</span>
  <span class="ps-trap__why">Ikkinchi nomaʼlum — bolalar chiptasi soni. Sistema toʻgʻri
  yechilgan, javob esa notoʻgʻri tanlangan: qaysi harf nimani bildirganini boshida
  yozib qoʻying.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">90 s</span></p>
  <div class="ps-stem__q">
    <p>Using the same information — 20 tickets for $136, with adult tickets at $8 and
    child tickets at $5 — how many <b>more</b> adult tickets than child tickets did the
    group buy?</p>
  </div>
  <ol class="ps-ch">
    <li>4</li>
    <li>8</li>
    <li>12</li>
    <li>20</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 4</p>
      <p>a = 12 va c = 8, demak farq 12 − 8 = <b>4</b>.</p>
      <p>Bu savolning butun qiyinligi bitta soʻzda: <em>more … than</em> <b>ayirmani</b>
      soʻraydi. Ikkala son ham javoblar orasida turibdi (12 va 8) va ikkalasi ham
      notoʻgʻri.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">12</span>
  <span class="ps-trap__why">Kattalar chiptasi soni — oldingi savolning javobi.
  <em>How many more … than</em> degan savol ayirmani soʻraydi; sonning oʻzini emas.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Matnli sistemani toʻrt qadamda yozing:</p>
  <ol>
    <li><b>Harflarni aniqlang</b> — nimaning soni, qaysi birligi bilan.</li>
    <li>«<b>Nechta</b>» jumlasini yozing (odatda a + c = jami).</li>
    <li>«<b>Qancha</b>» jumlasini yozing (narx × soni).</li>
    <li>Yeching, keyin <b>ikkala</b> shartga qaytarib tekshiring.</li>
  </ol>
  <p>Javoblar son boʻlsa, backsolving ham ishlaydi: har bir variantni «nechta» va
  «qancha» shartlariga qoʻyib koʻring.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">20 ta chipta $136 → har biri 136 ÷ 20 = $6.80</p>
  <p class="pe-good">Oʻrtacha narx $6.80, lekin hech bir chipta bunday turmaydi.</p>
  <p class="pe-fix__why">Ikki xil narx bor. Oʻrtacha son savolga javob bermaydi — ikkita
  tenglama kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">a + c = 136 va 8a + 5c = 20</p>
  <p class="pe-good">a + c = 20 va 8a + 5c = 136</p>
  <p class="pe-fix__why">Ikki tenglama oʻrin almashgan: <b>20</b> — chiptalar soni,
  <b>136</b> — pul. Birlikni yozib qoʻysangiz bu xato boʻlmaydi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Javob <b>butun son</b> va <b>manfiy emas</b> boʻlishi kerak — chipta yoki daftar
  soni haqida gap ketyapti. Agar kasr yoki manfiy son chiqsa, tenglama notoʻgʻri
  tuzilgan; yechishni emas, <b>tuzishni</b> qayta koʻring.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  The sum of two numbers is 54 and their difference is 8. What is the larger number?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">31 — qoʻshamiz: 2x = 62 → x = 31, va ikkinchisi 23.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Notebooks cost $3 and pens cost $2. A customer buys 15 items for $37. How many
  notebooks?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">7 ta — n + p = 15, 3n + 2p = 37 → n + 30 = 37 → n = 7
  (va 8 ta ruchka).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A rectangle has a perimeter of 34 and its length is 5 more than its width. What is the
  width?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">6 — 2(w + w + 5) = 34 → 4w + 10 = 34 → w = 6, uzunligi 11.
  Tekshiruv: 2(6 + 11) = 34 ✓</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  A jar holds 30 coins, some worth 5 and some worth 10, with a total value of 220. How
  many 5-coins are there?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">16 ta — x + y = 30 va 5x + 10y = 220 → 5x + 300 − 10x = 220 →
  −5x = −80 → x = 16 (va 14 ta 10-lik).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A cafe sells tea for $2 and coffee for $3. One morning it sold 40 drinks for $104. How
  many coffees were sold?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">24 ta — t + c = 40 va 2t + 3c = 104 → 80 + c = 104 → c = 24
  (va 16 ta choy).</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>a total of</b><span>jami; «nechta» tenglamasi</span></li>
  <li><b>how many more … than</b><span>nechtaga koʻp — ayirma soʻralyapti</span></li>
  <li><b>the sum / difference of two numbers</b><span>ikki sonning yigʻindisi / farqi</span></li>
  <li><b>each</b><span>har biri — narxni songa koʻpaytiradi</span></li>
  <li><b>which system represents</b><span>qaysi sistema ifodalaydi</span></li>
  <li><b>combined</b><span>birgalikda</span></li>
  <li><b>perimeter</b><span>perimetr</span></li>
  <li><b>value</b><span>qiymat (pul)</span></li>
  <li><b>respectively</b><span>mos ravishda</span></li>
  <li><b>whole number of</b><span>butun sonda — chipta boʻlaklanmaydi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Ikki nomaʼlum — <b>ikki jumla, ikki tenglama</b>: biri nechta, ikkinchisi
        qancha.</li>
    <li>Harflarni <b>birligi bilan</b> yozib qoʻying, aks holda javob almashib
        ketadi.</li>
    <li>Tekshiruv <b>ikki qatorli</b>: soni ham, qiymati ham toʻgʻri chiqishi
        kerak.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-19 — infinitely many solutions
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-19: Systems with Infinite Solutions (Identical Lines)",
        "category": "math",
        "order": 19,
        "summary": (
            "Ikki tenglama aslida bitta chiziqni ikki marta yozgan boʻlsa, yechim "
            "cheksiz koʻp. Buni tanish usuli: bir tenglama ikkinchisining karrasi — "
            "va SAT aynan shu koʻpaytuvchini soʻraydi."
        ),
        "stories": ["Two Signs, One Offer"],
        "content": """
<h2>SAT-19: Systems with Infinite Solutions (Identical Lines)</h2>

<p>Odatda ikki chiziq bitta nuqtada kesishadi va sistemaning bitta yechimi boʻladi. Lekin
ikki tenglama <mark>aynan bir xil chiziqni</mark> tasvirlashi ham mumkin — shunchaki
boshqacha yozilgan boʻladi. U holda ular butun uzunligi boʻylab ustma-ust tushadi va
har bir nuqta yechim boʻladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>«cheksiz koʻp yechim» nima demakligini rasm bilan tushunasiz;</li>
    <li>bir tenglama ikkinchisining karrasi ekanini bir qarashda koʻrasiz;</li>
    <li>nomaʼlum koeffitsientni (<em>k</em> yoki <em>c</em>) topasiz;</li>
    <li>nisbat testini qoʻllaysiz: A, B va C bir xil koʻpaytuvchi bilan oʻzgaradi.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Infinitely many solutions</span>
  <span class="pe-chip pe-chip--s">A<sub>1</sub> ÷ A<sub>2</sub></span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">B<sub>1</sub> ÷ B<sub>2</sub></span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">C<sub>1</sub> ÷ C<sub>2</sub></span>
</div>

<h3>Bitta chiziq, ikki xil yozuv</h3>

<p>2<em>x</em> + 3<em>y</em> = 8 tenglamasining ikkala tomonini 2 ga koʻpaytiring:
4<em>x</em> + 6<em>y</em> = 16. Bu <u>yangi</u> chiziq emas — bu oʻsha chiziqning ikki
barobar kattalashtirilgan yozuvi. Har bir (<em>x</em>, <em>y</em>) juftligi ikkalasini
ham bir vaqtda rost qiladi.</p>

<p>SAT-2 dagi «cheksiz koʻp yechim» holati esingizdami? U yerda yechganda <b>0 = 0</b>
qolar edi. SAT-11 da esa bu «ustma-ust tushgan chiziqlar» deb atalgan edi. Uchalasi —
bitta hodisaning uch xil koʻrinishi: <strong>algebrada</strong>, <strong>grafikda</strong>
va endi <strong>sistemada</strong>.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Cheksiz koʻp yechim» degani «har qanday son toʻgʻri» degani <b>emas</b>. Yechimlar
  faqat oʻsha chiziq ustidagi nuqtalar — ular cheksiz koʻp, lekin chiziqdan tashqaridagi
  nuqta yechim emas.
</div>

<h3>Nisbat testi</h3>

<blockquote>Ikki tenglamada mos koeffitsientlarning nisbati <u>uchalasida ham</u> bir xil
boʻlsa — cheksiz koʻp yechim.</blockquote>

<div class="pe-ex">
  <p class="pe-ex__math">4 ÷ 2 = 6 ÷ 3 = 16 ÷ 8 = 2</p>
  <p class="pe-ex__uz">4x + 6y = 16 va 2x + 3y = 8 — hamma joyda koʻpaytuvchi 2.</p>
  <p class="pe-ex__why">Agar oxirgi nisbat boshqacha boʻlganda, yechim umuman boʻlmasdi (SAT-20).</p>
</div>

<h3>Misol 1 (oson)</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + 3y = 8<br>4x + 6y = k</span>
    <span class="pm-solve__why">Ikkinchi tenglamaning chap tomoni birinchisidan 2 barobar katta</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">k = 2 × 8 = 16</span>
    <span class="pm-solve__why">Oʻng tomon ham <b>oʻsha</b> koʻpaytuvchi bilan oʻsishi kerak</span>
  </div>
</div>

<h3>Misol 2 (oʻrta) — koʻpaytuvchi kasr</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">6x + 2y = 10<br>3x + y = c</span>
    <span class="pm-solve__why">Ikkinchisi birinchisining <b>yarmi</b></span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">c = 10 ÷ 2 = 5</span>
    <span class="pm-solve__why">Koʻpaytuvchi 1/2, demak oʻng tomon ham ikkiga boʻlinadi</span>
  </div>
</div>

<h3>Misol 3 (SAT darajasi) — nomaʼlum chap tomonda</h3>

<p><em>kx</em> + 4<em>y</em> = 12 va 3<em>x</em> + 2<em>y</em> = 6 sistemasining cheksiz
koʻp yechimi bor. <em>k</em> nechaga teng?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">4 ÷ 2 = 2 va 12 ÷ 6 = 2</span>
    <span class="pm-solve__why">Maʼlum ikkita nisbatdan koʻpaytuvchini topdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">k = 2 × 3 = 6</span>
    <span class="pm-solve__why">x ning koeffitsienti ham oʻsha koʻpaytuvchiga boʻysunadi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>k = 6 boʻlsa birinchi tenglama 6x + 4y = 12 boʻladi, va u aynan 3x + 2y = 6 ning
  ikki barobari ✓</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu savol turida <b>hech qachon</b> sistemani yechmang. Yechishga urinsangiz 0 = 0
  chiqadi va u sizga <i>k</i> ni bermaydi. Javob faqat <b>koeffitsientlarni
  solishtirishdan</b> chiqadi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>infinitely many solutions</b><span>cheksiz koʻp yechim — bitta chiziq</span></li>
  <li><b>the same line</b><span>oʻsha chiziq</span></li>
  <li><b>a multiple of the other</b><span>ikkinchisining karrasi</span></li>
  <li><b>for what value of k</b><span>k ning qaysi qiymatida</span></li>
  <li><b>equivalent equations</b><span>teng kuchli tenglamalar</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>4<i>x</i> + <i>ky</i> = 20</p>
    <p>2<i>x</i> + 3<i>y</i> = 10</p>
    <p>If the system above has infinitely many solutions, what is the value of
    <i>k</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>3</li>
    <li>6</li>
    <li>10</li>
    <li>12</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 6</p>
      <p>4 ÷ 2 = 2 va 20 ÷ 10 = 2 — koʻpaytuvchi 2. Demak <i>k</i> = 2 × 3 = 6.</p>
      <p>Tekshiruv: 4x + 6y = 20 aynan 2x + 3y = 10 ning ikki barobari ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">3</span>
  <span class="ps-trap__why">Ikkinchi tenglamadagi koeffitsient shunchaki koʻchirilgan.
  Cheksiz koʻp yechim uchun koeffitsientlar <b>teng</b> emas, <b>proporsional</b>
  boʻlishi kerak.</span>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">12</span>
  <span class="ps-trap__why">Koʻpaytuvchi 4 deb olingan (4 ÷ 1). Koʻpaytuvchini
  <b>ikkita</b> maʼlum nisbatdan tekshiring — ular bir xil chiqishi shart.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>Which system of equations has infinitely many solutions?</p>
  </div>
  <ol class="ps-ch">
    <li><i>x</i> + <i>y</i> = 4 and 2<i>x</i> + 2<i>y</i> = 9</li>
    <li><i>x</i> + <i>y</i> = 4 and 3<i>x</i> + 3<i>y</i> = 12</li>
    <li><i>x</i> + <i>y</i> = 4 and <i>x</i> − <i>y</i> = 4</li>
    <li><i>x</i> + <i>y</i> = 4 and 2<i>x</i> + 3<i>y</i> = 8</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) x + y = 4 va 3x + 3y = 12</p>
      <p>Ikkinchi tenglama birinchisining aynan uch barobari: 3 ÷ 1 = 3 ÷ 1 = 12 ÷ 4 = 3
      ✓</p>
      <p><b>A</b> — chap tomon ikki barobar, oʻng tomon esa emas (8 boʻlishi kerak edi,
      9 emas): bu <b>yechimsiz</b> sistema (SAT-20). <b>C</b> va <b>D</b> oddiy
      kesishuvchi chiziqlar — bitta yechim.</p>
    </div>
  </details>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>«Cheksiz koʻp yechim» savolini uch qadamda yoping:</p>
  <ol>
    <li>Maʼlum ikki juft koeffitsientdan <b>koʻpaytuvchini</b> toping (masalan 4 ÷ 2 = 2).</li>
    <li>Uni oʻng tomonda ham tekshiring — bir xil chiqishi shart.</li>
    <li>Nomaʼlum koeffitsientni oʻsha koʻpaytuvchiga koʻpaytiring.</li>
  </ol>
  <p>Agar oʻng tomondagi nisbat boshqacha boʻlsa, savol aslida <b>yechimsiz</b> holat
  haqida (SAT-20) — sarlavhani qayta oʻqing.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">2x + 3y = 8 va 4x + 6y = 8 — cheksiz koʻp yechim.</p>
  <p class="pe-good">Bu sistemaning yechimi <b>yoʻq</b>.</p>
  <p class="pe-fix__why">Chap tomon ikki barobar, oʻng tomon esa oʻsha-oʻsha. 16 boʻlishi
  kerak edi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Koeffitsientlar teng boʻlsa — cheksiz koʻp yechim.</p>
  <p class="pe-good">Ular <b>proporsional</b> boʻlishi kerak, teng emas.</p>
  <p class="pe-fix__why">3x + 3y = 12 va x + y = 4 — koeffitsientlar teng emas, lekin
  nisbat hamma joyda 3.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Tez usul: bitta tenglamani <b>soddalashtiring</b>. 3x + 3y = 12 ni 3 ga boʻlsangiz
  x + y = 4 chiqadi — ikkinchisi bilan bir xil. Bu nisbat testidan ham tezroq.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  For what value of <i>k</i> does 3<i>x</i> + 5<i>y</i> = 9 and 6<i>x</i> + 10<i>y</i> =
  <i>k</i> have infinitely many solutions?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>k</i> = 18 — koʻpaytuvchi 2, demak oʻng tomon ham
  ikkilanadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  For what value of <i>c</i> does 10<i>x</i> + 4<i>y</i> = 22 and 5<i>x</i> + 2<i>y</i> =
  <i>c</i> have infinitely many solutions?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>c</i> = 11 — ikkinchisi birinchisining yarmi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Do <i>y</i> = 2<i>x</i> + 1 and 2<i>y</i> = 4<i>x</i> + 2 have one solution, none, or
  infinitely many?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Cheksiz koʻp — ikkinchisini 2 ga boʻlsak birinchisi chiqadi.
  Bu bitta chiziq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  For what value of <i>k</i> does <i>kx</i> + 6<i>y</i> = 15 and 2<i>x</i> + 4<i>y</i> =
  10 have infinitely many solutions?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>k</i> = 3 — 6 ÷ 4 = 1.5 va 15 ÷ 10 = 1.5, demak
  <i>k</i> = 1.5 × 2 = 3.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  If a system has infinitely many solutions, what do its two graphs look like?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ular ustma-ust tushgan <b>bitta</b> chiziq — ikkinchisi
  koʻrinmaydi, chunki u birinchisining tagida yotadi.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>infinitely many solutions</b><span>cheksiz koʻp yechim</span></li>
  <li><b>identical / the same line</b><span>bir xil chiziq</span></li>
  <li><b>a multiple of</b><span>…ning karrasi</span></li>
  <li><b>proportional</b><span>proporsional; nisbati bir xil</span></li>
  <li><b>equivalent equations</b><span>teng kuchli tenglamalar</span></li>
  <li><b>coincide</b><span>ustma-ust tushmoq</span></li>
  <li><b>coefficient</b><span>koeffitsient</span></li>
  <li><b>constant term</b><span>oʻzgarmas had (oʻng tomondagi son)</span></li>
  <li><b>simplify the equation</b><span>tenglamani soddalashtirish</span></li>
  <li><b>for what value of k</b><span>k ning qaysi qiymatida</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Cheksiz koʻp yechim = ikki tenglama <b>bitta chiziq</b>ni yozgan.</li>
    <li>Test: <b>A, B va C bir xil koʻpaytuvchi</b> bilan bogʻlangan boʻlishi kerak.</li>
    <li>Eng tez yoʻl — bitta tenglamani <b>soddalashtirib</b>, ikkinchisi bilan
        solishtirish.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-20 — no solution  (block A closer)
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-20: Systems with No Solution (Parallel Lines)",
        "category": "math",
        "order": 20,
        "summary": (
            "Bir xil qiyalik, boshqa oʻzgarmas had — chiziqlar parallel va hech qachon "
            "uchrashmaydi. Blokning yakuni: uchala holat bitta jadvalda."
        ),
        "stories": ["The Fare That Never Catches Up"],
        "content": """
<h2>SAT-20: Systems with No Solution (Parallel Lines)</h2>

<p>SAT-19 da ikki tenglama bitta chiziqni yozgan edi. Endi teskarisi: ular
<mark>bir xil tiklikda, lekin turli balandlikda</mark> ketadi. Bunday ikki chiziq
qanchalik uzaytirilmasin uchrashmaydi — demak ikkala tenglamani bir vaqtda rost
qiladigan (<em>x</em>, <em>y</em>) juftligi <strong>yoʻq</strong>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>«yechim yoʻq» holatini koeffitsientlardan tanib olasiz;</li>
    <li>uni cheksiz koʻp yechimdan faqat <u>oʻng tomon</u> bilan ajratasiz;</li>
    <li>nomaʼlum koeffitsientni topasiz;</li>
    <li>uchala holatni bitta jadvalda koʻrasiz — bu butun blokning xulosasi.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">No solution</span>
  <span class="pe-chip pe-chip--s">A<sub>1</sub> ÷ A<sub>2</sub></span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">B<sub>1</sub> ÷ B<sub>2</sub></span>
  <span class="pe-op">≠</span>
  <span class="pe-chip pe-chip--neg">C<sub>1</sub> ÷ C<sub>2</sub></span>
</div>

<h3>Farq faqat bitta sonda</h3>

<p>Ikki holat bir-biriga juda oʻxshaydi va SAT ularni bitta savolda solishtiradi.
Chap tomonlar <b>ikkalasida ham</b> proporsional; farq oʻng tomonda:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Cheksiz koʻp (SAT-19)</p>
    <p>2<i>x</i> + 3<i>y</i> = 8 va 4<i>x</i> + 6<i>y</i> = <b>16</b></p>
    <p>Oʻng tomon ham ikkilangan — bitta chiziq.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Yechim yoʻq (SAT-20)</p>
    <p>2<i>x</i> + 3<i>y</i> = 8 va 4<i>x</i> + 6<i>y</i> = <b>9</b></p>
    <p>Oʻng tomon ikkilanmagan — parallel chiziqlar.</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikkinchi holatni algebra bilan tekshiring: 4x + 6y ni 2 ga boʻlsak 2x + 3y = 4.5
  chiqadi. Lekin birinchi tenglama 2x + 3y = 8 deydi. <b>Bitta ifoda ikki xil songa
  teng boʻla olmaydi</b> — shuning uchun yechim yoʻq.
</div>

<h3>Misol 1 (oson)</h3>

<p><em>y</em> = 5<em>x</em> + 2 va <em>y</em> = <em>kx</em> − 3 sistemasining yechimi
yoʻq. <em>k</em> nechaga teng?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">k = 5</span>
    <span class="pm-solve__why">Qiyaliklar teng boʻlishi kerak — chiziqlar parallel</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2 ≠ −3 ✓</span>
    <span class="pm-solve__why">b lar har xil, demak ular <b>ustma-ust tushmaydi</b> — haqiqatan yechim yoʻq</span>
  </div>
</div>

<h3>Misol 2 (oʻrta) — standart shaklda</h3>

<p>3<em>x</em> + <em>ky</em> = 7 va 6<em>x</em> + 4<em>y</em> = 11.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 ÷ 6 = 1/2</span>
    <span class="pm-solve__why">x koeffitsientlarining nisbati</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">k ÷ 4 = 1/2  →  k = 2</span>
    <span class="pm-solve__why">y koeffitsientlari ham shu nisbatda boʻlishi kerak</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">7 ÷ 11 ≠ 1/2 ✓</span>
    <span class="pm-solve__why">Oʻng tomon nisbati boshqa — demak yechim yoʻq</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Uchinchi qadamni tashlab ketmang. Agar oʻng tomon ham 1/2 nisbatda boʻlganda
  (masalan 7 va 14), javob «yechim yoʻq» emas, <b>cheksiz koʻp</b> boʻlardi — va
  <em>k</em> oʻsha-oʻsha 2 boʻlib qolardi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikki <b>toʻgʻri chiziq</b> hech qachon roppa-rosa ikki nuqtada kesishmaydi — ikkita
  umumiy nuqtasi bor chiziqlar butunlay ustma-ust tushadi. Shuning uchun «exactly two»
  degan javob chiziqli sistemada har doim notoʻgʻri.
</div>

<h3>Uchala holat — blokning xulosasi</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Koeffitsientlar</th><th>Grafik</th><th>Yechim</th></tr>
  <tr><td>Qiyaliklar <b>har xil</b></td><td>kesishadi</td><td class="pm-word__sym">bitta</td></tr>
  <tr><td>Qiyaliklar teng, C nisbati <b>boshqa</b></td><td>parallel</td><td class="pm-word__sym">yoʻq</td></tr>
  <tr><td>Qiyaliklar teng, C nisbati ham <b>oʻsha</b></td><td>ustma-ust</td><td class="pm-word__sym">cheksiz</td></tr>
</table></div>

<p>Bu jadval SAT-2 (0 = 0 va 6 = 5), SAT-11 (parallel va ustma-ust chiziqlar) va
SAT-19 ni bitta joyga yigʻadi. Uchala dars bir xil hodisani uch xil tilda aytgan edi.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>no solution</b><span>yechimi yoʻq — parallel chiziqlar</span></li>
  <li><b>exactly one solution</b><span>roppa-rosa bitta yechim — kesishadi</span></li>
  <li><b>for what value of k does the system have no solution</b><span>k ning qaysi qiymatida yechim boʻlmaydi</span></li>
  <li><b>the graphs are parallel</b><span>grafiklar parallel</span></li>
  <li><b>how many solutions does the system have</b><span>sistemaning nechta yechimi bor</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>2<i>x</i> + 3<i>y</i> = 9</p>
    <p>4<i>x</i> + <i>ky</i> = 7</p>
    <p>If the system above has no solution, what is the value of <i>k</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>3</li>
    <li>6</li>
    <li>7</li>
    <li>18</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 6</p>
      <p>Chap tomonlar proporsional boʻlishi kerak: 4 ÷ 2 = 2, demak
      <i>k</i> = 2 × 3 = 6.</p>
      <p>Tekshiruv: 4x + 6y = 7 va 2x + 3y = 9 — ikkinchisini ikkilasak
      4x + 6y = 18, bu 7 emas. Demak chiziqlar parallel va yechim yoʻq ✓</p>
      <p><b>18</b> — aynan cheksiz koʻp yechim beradigan oʻng tomon; u savolning
      javobi emas, lekin nima uchun 6 toʻgʻri ekanini tasdiqlaydi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">3</span>
  <span class="ps-trap__why">Ikkinchi tenglamadagi koeffitsient koʻchirilgan. Parallellik
  uchun koeffitsientlar teng emas, <b>proporsional</b> boʻlishi kerak — bu yerda
  koʻpaytuvchi 2.</span>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">7</span>
  <span class="ps-trap__why">Oʻng tomondagi son <i>k</i> deb olingan. Savol
  <i>y</i> ning <b>koeffitsientini</b> soʻrayapti — tenglamadagi oʻrniga qarang.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>3<i>x</i> − <i>y</i> = 5</p>
    <p>6<i>x</i> − 2<i>y</i> = 10</p>
    <p>How many solutions does the system above have?</p>
  </div>
  <ol class="ps-ch">
    <li>None</li>
    <li>Exactly one</li>
    <li>Exactly two</li>
    <li>Infinitely many</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: D) Infinitely many</p>
      <p>6 ÷ 3 = 2, (−2) ÷ (−1) = 2 va 10 ÷ 5 = 2 — <b>uchala</b> nisbat ham 2. Demak
      ikkinchi tenglama birinchisining ikki barobari, ular bitta chiziq.</p>
      <p>Agar oʻng tomon 10 emas, 11 boʻlganda, javob <b>None</b> boʻlardi. Farq
      shu bitta sonda.</p>
    </div>
  </details>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>«Nechta yechim?» savolini 20 soniyada yoping:</p>
  <ol>
    <li>x koeffitsientlari nisbatini oling.</li>
    <li>y koeffitsientlari nisbati bilan solishtiring. <b>Har xil</b> boʻlsa — bitta
        yechim, tugadi.</li>
    <li>Teng boʻlsa, oʻng tomon nisbatiga qarang: <b>oʻsha</b> boʻlsa cheksiz koʻp,
        <b>boshqa</b> boʻlsa yechim yoʻq.</li>
  </ol>
  <p>Uchta boʻlish — va sistema umuman yechilmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Qiyaliklar teng boʻlsa, yechim har doim yoʻq.</p>
  <p class="pe-good">Yoʻq — oʻng tomon ham mos boʻlsa, yechim <b>cheksiz koʻp</b>.</p>
  <p class="pe-fix__why">Teng qiyalik ikki holatni beradi; ularni faqat oʻzgarmas had
  ajratadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">«No solution» degani x = 0.</p>
  <p class="pe-good">Hech qanday (x, y) juftligi ikkala tenglamani rost qilmaydi.</p>
  <p class="pe-fix__why">x = 0 — bu haqiqiy yechim boʻlardi. «Yechim yoʻq» esa
  <b>hech qanday</b> juftlik toʻgʻri kelmasligi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Blok A (SAT-1…22) shu yerda yopiladi: chiziq nima ekanidan boshlab, ikki chiziqning
  uchta mumkin boʻlgan munosabatigacha yetib keldik — <b>kesishadi</b>,
  <b>parallel</b>, <b>ustma-ust</b>. SAT'dagi chiziqli savollarning deyarli hammasi
  shu uch rasmning biri haqida.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  For what value of <i>k</i> does <i>y</i> = 4<i>x</i> + 1 and <i>y</i> = <i>kx</i> − 6
  have no solution?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>k</i> = 4 — qiyaliklar teng boʻlishi kerak, va b lar
  (1 va −6) allaqachon har xil.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  How many solutions do <i>x</i> + <i>y</i> = 5 and 2<i>x</i> + 2<i>y</i> = 7 have?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Bittasi ham yoʻq — chap tomon ikkilangan, oʻng tomon esa 10
  boʻlishi kerak edi, 7 emas. Parallel chiziqlar.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  How many solutions do <i>x</i> + <i>y</i> = 5 and <i>x</i> − <i>y</i> = 1 have?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Roppa-rosa bittasi — qiyaliklari har xil, demak kesishadi:
  (3, 2).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  For what value of <i>k</i> does 5<i>x</i> + <i>ky</i> = 3 and 10<i>x</i> + 4<i>y</i> = 9
  have no solution?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>k</i> = 2 — 5 ÷ 10 = 1/2, demak k ÷ 4 = 1/2. Oʻng tomon:
  3 ÷ 9 = 1/3 ≠ 1/2 ✓ demak haqiqatan yechim yoʻq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Two lines have the same slope and the same <i>y</i>-intercept. How many solutions does
  the system have?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Cheksiz koʻp — bu bitta chiziq, ustma-ust tushgan (SAT-19).</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>no solution</b><span>yechimi yoʻq</span></li>
  <li><b>exactly one solution</b><span>roppa-rosa bitta yechim</span></li>
  <li><b>parallel graphs</b><span>parallel grafiklar</span></li>
  <li><b>consistent / inconsistent</b><span>yechimi bor / yechimi yoʻq sistema</span></li>
  <li><b>proportional coefficients</b><span>proporsional koeffitsientlar</span></li>
  <li><b>constant term</b><span>oʻzgarmas had</span></li>
  <li><b>never intersect</b><span>hech qachon kesishmaydi</span></li>
  <li><b>how many solutions</b><span>nechta yechim</span></li>
  <li><b>ratio</b><span>nisbat</span></li>
  <li><b>coincident lines</b><span>ustma-ust tushgan chiziqlar</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Yechim yoʻq = <b>qiyaliklar teng, oʻzgarmas hadlar mos emas</b>.</li>
    <li>Farq faqat <b>oʻng tomonda</b>: mos boʻlsa cheksiz koʻp, mos boʻlmasa yechim
        yoʻq.</li>
    <li>Uchta boʻlish — uchta javob: <b>kesishadi · parallel · ustma-ust</b>.</li>
  </ul>
</div>
""",
    },
]
