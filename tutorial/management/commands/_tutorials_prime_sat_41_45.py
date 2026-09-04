# -*- coding: utf-8 -*-
"""Prime SAT Math — lessons 41–45 (kasrli ifodalar, teoremalar, koʻrsatkichli oʻsish).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_SAT.md
Lesson list: tutorial/management/commands/toc_prime_sat_math.txt

⚠️ SARLAVHALAR BAZADAN OLINGAN, aynan (2026-09-04 da toc bazaga moslandi).
   Yozishdan oldin har doim tekshiring:
   Tutorial.objects.filter(title__startswith='SAT-')

⚠️ Kumulyativ (SAT-1…40 erkin: butun Blok A, koʻphadlar, ajratish, kvadrat
   tenglama, diskriminant, uch, grafik, sistema, ildizli va kasrli tenglamalar):
  • SAT-41 — kasrli ifodani qisqartirish va koʻphadni boʻlish (qoldiq bilan).
  • SAT-42 — qoldiq va koʻpaytuvchi teoremalari: P(a) hamma narsani aytadi.
  • SAT-43 — yuqori darajali koʻphad grafigi: chekka xatti-harakati va karralilik.
  • SAT-44 — chiziqli va koʻrsatkichli oʻsishni farqlash (jadval, foiz, soʻz).
  • SAT-45 — matndan koʻrsatkichli funksiya yozish: a — boshlangʻich, b — koeffitsient.
  • ⛔ Murakkab foiz (SAT-46) YOʻQ; funksiya belgilanishi (SAT-47) YOʻQ;
    logarifm umuman YOʻQ (digital SAT'da yoʻq).

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_sat_41_45.py \\
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
    # SAT-41 — simplifying rational expressions & polynomial division
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-41: Simplifying Rational Expressions & Polynomial Division",
        "category": "math",
        "order": 41,
        "summary": (
            "Suratni ham, maxrajni ham ajrating va umumiy qavsni qisqartiring. "
            "Boʻlinmasa — qoldiqli koʻrinishda yozing."
        ),
        "stories": ["What the Bolt Would Not Give"],
        "content": """
<h2>SAT-41: Simplifying Rational Expressions & Polynomial Division</h2>

<p>Kasrli ifodani qisqartirish uchun bitta qoida bor, va SAT uni buzishga
undaydigan javoblarni ataylab qoʻyadi: <mark>faqat koʻpaytuvchini qisqartirish
mumkin, hadni emas</mark>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>surat va maxrajni ajratib, umumiy qavsni qisqartirasiz;</li>
    <li>had va koʻpaytuvchi farqini hech qachon adashtirmaysiz;</li>
    <li>taqiqlangan qiymatni saqlab qolasiz (SAT-40);</li>
    <li>boʻlinmaydigan ifodani qoldiq bilan yozasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The one rule</span>
  <span class="pe-chip pe-chip--v">koʻpaytuvchi qisqaradi</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">had qisqarmaydi</span>
</div>

<h3>Qisqartirish — uch qadam</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">(x<sup>2</sup> − 9) ÷ (x + 3)</span>
    <span class="pm-solve__why">Taqiq: x ≠ −3 (SAT-40)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(x − 3)(x + 3) ÷ (x + 3)</span>
    <span class="pm-solve__why">Suratni ajratdik — kvadratlar ayirmasi (SAT-30)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x − 3,  x ≠ −3</span>
    <span class="pm-solve__why">(x + 3) butun qavs — koʻpaytuvchi, shuning uchun qisqaradi</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Qisqartirish taqiqni <b>oʻchirmaydi</b>. x − 3 ifodasi x = −3 da −6 beradi, asl
  ifoda esa u yerda aniqlanmagan. SAT baʼzan javob variantiga «x ≠ −3» ni ataylab
  qoʻshadi.
</div>

<h3>Eng koʻp uchraydigan xato</h3>

<div class="pe-fix">
  <p class="pe-bad">(x + 3) ÷ 3 = x</p>
  <p class="pe-good">Qisqarmaydi</p>
  <p class="pe-fix__why">Suratda <b>qoʻshish</b> turibdi, koʻpaytirish emas. 3 —
  had, koʻpaytuvchi emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">(x<sup>2</sup> + 4) ÷ (x + 2) = x + 2</p>
  <p class="pe-good">Qisqarmaydi — x<sup>2</sup> + 4 ajralmaydi</p>
  <p class="pe-fix__why">Kvadratlar <b>yigʻindisi</b> ajralmaydi; faqat ayirmasi
  ajraladi (SAT-30).</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Tez sinov: <b>surat butunlay qavsga oʻralganmi?</b> (x + 3)(x − 3) — ha, demak
  har bir qavs koʻpaytuvchi. x<sup>2</sup> + 4x − ha, lekin faqat x ni chiqargandan
  keyin: x(x + 4). Plyus belgisi koʻrinib turgan joyda hech narsa qisqarmaydi.
</div>

<h3>Boʻlinmasa — qoldiq bilan</h3>

<p>Baʼzida maxraj suratga toʻliq boʻlinmaydi. U holda javob <b>butun qism +
qoldiq</b> koʻrinishida yoziladi — bu SAT'ning sevimli javob shakli.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">(x<sup>2</sup> + 5x + 7) ÷ (x + 2)</span>
    <span class="pm-solve__why">Surat ajralmaydi: 7 ni beradigan juftlik 5 ni bermaydi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x<sup>2</sup> + 5x + 7 = (x + 2)(x + 3) + 1</span>
    <span class="pm-solve__why">(x+2)(x+3) = x<sup>2</sup> + 5x + 6, yetmagani 1</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x + 3 + 1 ÷ (x + 2)</span>
    <span class="pm-solve__why">Butun qism x + 3, qoldiq 1</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Uzun boʻlishni oʻrganish shart emas. <b>Qavsni tanlang va tekshiring:</b>
  (x + 2) ni nimaga koʻpaytirsam x<sup>2</sup> + 5x chiqadi? — (x + 3) ga. Oching,
  asl surat bilan solishtiring, farqi qoldiq boʻladi. Bu SAT'da ancha tez.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>which expression is equivalent to</b><span>qaysi ifoda teng kuchli</span></li>
  <li><b>in simplest form</b><span>eng sodda koʻrinishda</span></li>
  <li><b>where x ≠ −2</b><span>x −2 ga teng boʻlmaganda</span></li>
  <li><b>the remainder</b><span>qoldiq</span></li>
  <li><b>reduce the fraction</b><span>kasrni qisqartiring</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">55 s</span></p>
  <div class="ps-stem__q">
    <p>Which expression is equivalent to (<i>x</i><sup>2</sup> − 16) ÷
    (<i>x</i> − 4), where <i>x</i> ≠ 4?</p>
  </div>
  <ol class="ps-ch">
    <li><i>x</i> + 4</li>
    <li><i>x</i> − 4</li>
    <li><i>x</i><sup>2</sup> − 4</li>
    <li>4</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) x + 4</p>
      <p>x<sup>2</sup> − 16 = (x − 4)(x + 4), va (x − 4) qisqaradi.</p>
      <p>Tekshiruv: x = 5 da asl ifoda (25 − 16) ÷ 1 = 9, va 5 + 4 = 9 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">x − 4</span>
  <span class="ps-trap__why">Maxrajdagi qavs javobga koʻchirilgan. Qisqaradigan qavs
  <b>yoʻqoladi</b>; qoladigani — ikkinchisi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">90 s</span></p>
  <div class="ps-stem__q">
    <p>Which expression is equivalent to (<i>x</i><sup>2</sup> + 5<i>x</i> + 7) ÷
    (<i>x</i> + 2)?</p>
  </div>
  <ol class="ps-ch">
    <li><i>x</i> + 3 + 1 ÷ (<i>x</i> + 2)</li>
    <li><i>x</i> + 3</li>
    <li><i>x</i> + 7 ÷ (<i>x</i> + 2)</li>
    <li><i>x</i> + 3 − 1 ÷ (<i>x</i> + 2)</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) x + 3 + 1 ÷ (x + 2)</p>
      <p>(x + 2)(x + 3) = x<sup>2</sup> + 5x + 6, va suratda 7 bor — demak qoldiq 1.</p>
      <p>Tekshiruv x = 0 da: asl ifoda 7 ÷ 2 = 3.5, va 3 + 0.5 = 3.5 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">x + 3</span>
  <span class="ps-trap__why">Qoldiq tashlab ketilgan. x = 0 qoʻyib koʻring: bu
  javob 3 beradi, asl ifoda esa 3.5.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Teng kuchli ifoda soʻralganda hisoblamang — <b>bitta son qoʻying</b>:</p>
  <ol>
    <li>Taqiqlanmagan oson son tanlang (koʻpincha <i>x</i> = 0 yoki 1);</li>
    <li>Asl ifodaning qiymatini hisoblang;</li>
    <li>Har bir javobni oʻsha sonda tekshiring — bittasi mos keladi.</li>
  </ol>
  <p>Bu usul qisqartirish xatosini ham, qoldiqni unutishni ham butunlay
  chetlab oʻtadi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qoldiqli javobning maʼnosi oddiy: <b>(x + 2) suratga toʻliq sigʻmaydi</b>, va
  sigʻmay qolgan qismi 1 boʻlib qoladi. Bu 17 ÷ 5 = 3 va qoldiq 2 bilan bir xil
  fikr, faqat harflar bilan.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Javob variantlari orasida <b>x ≠ …</b> shartli va shartsiz variantlar boʻlsa,
  shartlisini tanlang: qisqartirilgan ifoda asl ifodaga faqat oʻsha qiymat
  chiqarib tashlanganda teng boʻladi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Simplify: (<i>x</i><sup>2</sup> − 25) ÷ (<i>x</i> − 5)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> + 5, bunda x ≠ 5.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Simplify: (<i>x</i><sup>2</sup> + 5<i>x</i> + 6) ÷ (<i>x</i> + 2)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> + 3 — surat (x + 2)(x + 3).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Simplify: (2<i>x</i><sup>2</sup> + 7<i>x</i> + 3) ÷ (<i>x</i> + 3)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">2<i>x</i> + 1 — surat (2x + 1)(x + 3) (SAT-32).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Can (<i>x</i> + 5) ÷ 5 be simplified to <i>x</i>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — 5 had, koʻpaytuvchi emas. x = 5 da asl ifoda 2,
  x esa 5.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Write (<i>x</i><sup>2</sup> + 3<i>x</i> + 5) ÷ (<i>x</i> + 1) with a
  remainder.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> + 2 + 3 ÷ (<i>x</i> + 1) — chunki
  (x + 1)(x + 2) = x<sup>2</sup> + 3x + 2, va 5 − 2 = 3.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>rational expression</b><span>kasrli ifoda</span></li>
  <li><b>simplest form</b><span>eng sodda koʻrinish</span></li>
  <li><b>common factor</b><span>umumiy koʻpaytuvchi</span></li>
  <li><b>factor vs term</b><span>koʻpaytuvchi va had</span></li>
  <li><b>cancel</b><span>qisqartirmoq</span></li>
  <li><b>numerator / denominator</b><span>surat / maxraj</span></li>
  <li><b>remainder</b><span>qoldiq</span></li>
  <li><b>quotient</b><span>boʻlinma (butun qism)</span></li>
  <li><b>equivalent expression</b><span>teng kuchli ifoda</span></li>
  <li><b>undefined at</b><span>… da aniqlanmagan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Avval <b>ajrating</b>, keyin qisqartiring — hech qachon teskarisi emas.</li>
    <li>Faqat <b>koʻpaytuvchi</b> qisqaradi; plyus koʻringan joyda hech narsa
        qisqarmaydi.</li>
    <li>Boʻlinmasa, <b>butun qism + qoldiq ÷ maxraj</b> koʻrinishida yozing.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-42 — the remainder and factor theorems
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-42: The Remainder Theorem and the Factor Theorem",
        "category": "math",
        "order": 42,
        "summary": (
            "Koʻphadni (x − a) ga boʻlishdan chiqadigan qoldiq — bu shunchaki "
            "P(a). Qoldiq nol boʻlsa, (x − a) koʻpaytuvchi."
        ),
        "stories": ["The Test That Takes One Line"],
        "content": """
<h2>SAT-42: The Remainder Theorem and the Factor Theorem</h2>

<p>SAT-41 da boʻlish uzun ish edi. Endi bitta hayratlanarli qisqartma:
<mark>qoldiqni topish uchun boʻlish shart emas</mark> — bitta son qoʻyish yetadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>qoldiqni P(a) hisoblab topasiz;</li>
    <li>(x − a) koʻpaytuvchimi yoʻqmi — bir qadamda aytasiz;</li>
    <li>(x + 3) ni koʻrsangiz x = −3 qoʻyasiz;</li>
    <li>noma'lum koeffitsientni topish savollarini yechasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The remainder theorem</span>
  <span class="pe-chip pe-chip--s">P(x) ÷ (x − a)</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">qoldiq = P(a)</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The factor theorem</span>
  <span class="pe-chip pe-chip--s">P(a) = 0</span>
  <span class="pe-op">⟺</span>
  <span class="pe-chip pe-chip--o">(x − a) koʻpaytuvchi</span>
</div>

<h3>Nima uchun ishlaydi</h3>

<p>Har qanday boʻlishni shunday yozish mumkin: <b>P(x) = (x − a)·Q(x) + R</b>.
Endi x oʻrniga <em>a</em> qoʻying — birinchi qavs nolga aylanadi va butun ko'paytma
yoʻqoladi. Qoladigani faqat R.</p>

<div class="pm-check">
  <p class="pm-check__t">Bir qatorda</p>
  <p>P(a) = (a − a)·Q(a) + R = 0 · Q(a) + R = R</p>
</div>

<h3>Qoldiqni topish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">P(x) = x<sup>3</sup> − 2x<sup>2</sup> + 3x − 5, boʻluvchi (x − 2)</span>
    <span class="pm-solve__why">a = 2</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">P(2) = 8 − 8 + 6 − 5</span>
    <span class="pm-solve__why">Har bir hadni alohida hisobladik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Qoldiq = 1</span>
    <span class="pm-solve__why">Boʻlish umuman qilinmadi</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Boʻluvchi <b>(x + 3)</b> boʻlsa, u (x − (−3)) degani — demak <b>x = −3</b>
  qoʻyiladi. Ishorani almashtirishni unutish bu mavzudagi asosiy xato, va tuzoq
  javob har doim P(3) boʻladi.
</div>

<h3>Koʻpaytuvchi teoremasi ish boshida</h3>

<p>P(x) = x<sup>3</sup> − 4x<sup>2</sup> + x + 6 ni ajratish kerak boʻlsin. Kubik
uchun tayyor formula yoʻq, lekin bir nechta oson sonni sinab koʻrish mumkin:</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Sinov</th><th>Hisob</th><th>Xulosa</th></tr>
  <tr><td>P(1)</td><td>1 − 4 + 1 + 6 = 4</td><td class="pm-word__sym">koʻpaytuvchi emas</td></tr>
  <tr><td>P(2)</td><td>8 − 16 + 2 + 6 = 0</td><td class="pm-word__sym">(x − 2) koʻpaytuvchi ✓</td></tr>
  <tr><td>P(−1)</td><td>−1 − 4 − 1 + 6 = 0</td><td class="pm-word__sym">(x + 1) koʻpaytuvchi ✓</td></tr>
  <tr><td>P(3)</td><td>27 − 36 + 3 + 6 = 0</td><td class="pm-word__sym">(x − 3) koʻpaytuvchi ✓</td></tr>
</table></div>

<p>Uchta nol topildi, daraja ham uch — demak
P(x) = (x − 2)(x + 1)(x − 3), va boshqa nol yoʻq.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Qaysi sonlarni sinash kerak? <b>Erkin hadning boʻluvchilarini.</b> Yuqorida
  erkin had 6 edi, shuning uchun 1, 2, 3, 6 va ularning manfiylari — hammasi
  boʻlib bir necha soniyalik ish.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>the remainder when P(x) is divided by</b><span>P(x) … ga boʻlingandagi qoldiq</span></li>
  <li><b>is a factor of</b><span>… ning koʻpaytuvchisi</span></li>
  <li><b>P(3) = 0</b><span>demak (x − 3) koʻpaytuvchi va 3 — nol</span></li>
  <li><b>for what value of k</b><span>k ning qaysi qiymatida</span></li>
  <li><b>which of the following must be true</b><span>qaysi biri albatta toʻgʻri</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>What is the remainder when <i>P</i>(<i>x</i>) = <i>x</i><sup>3</sup> −
    2<i>x</i><sup>2</sup> + 3<i>x</i> − 5 is divided by <i>x</i> − 2?</p>
  </div>
  <ol class="ps-ch">
    <li>1</li>
    <li>0</li>
    <li>−5</li>
    <li>−27</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 1</p>
      <p>P(2) = 8 − 8 + 6 − 5 = 1.</p>
      <p><b>−27</b> — P(−2) hisoblangan: −8 − 8 − 6 − 5. Boʻluvchi (x − 2) boʻlsa
      x = <b>+2</b> qoʻyiladi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">−27</span>
  <span class="ps-trap__why">Ishora teskari olingan. Qoida: (x − a) da <b>a</b> —
  minusdan keyingi sonning oʻzi, ishorasi bilan emas.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">85 s</span></p>
  <div class="ps-stem__q">
    <p>In the polynomial <i>P</i>(<i>x</i>) = <i>x</i><sup>3</sup> +
    <i>kx</i><sup>2</sup> − 4<i>x</i> + 1, <i>k</i> is a constant. If
    <i>x</i> − 1 is a factor of <i>P</i>, what is the value of <i>k</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>2</li>
    <li>−2</li>
    <li>4</li>
    <li>1</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 2</p>
      <p>«x − 1 is a factor» → P(1) = 0. Demak 1 + k − 4 + 1 = 0 → k = 2.</p>
      <p>Tekshiruv: P(x) = x<sup>3</sup> + 2x<sup>2</sup> − 4x + 1, va
      P(1) = 1 + 2 − 4 + 1 = 0 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">−2</span>
  <span class="ps-trap__why">Tenglama yechilganda ishora almashtirilgan:
  k − 2 = 0 dan k = 2 chiqadi, −2 emas.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Bu mavzuda uchta iborani uchta amalga bogʻlang:</p>
  <ol>
    <li>«remainder when divided by (x − a)» → <b>P(a) ni hisoblang</b>;</li>
    <li>«(x − a) is a factor» → <b>P(a) = 0 deb yozing</b>;</li>
    <li>«P(a) = 0» → a nol, (x − a) koʻpaytuvchi, va grafik u yerda x oʻqini
        kesadi (SAT-43).</li>
  </ol>
  <p>Uchalasi bir xil faktning uch xil aytilishi — bu ularni yodlashning eng
  qisqa yoʻli.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">(x + 3) ga boʻlish → P(3) ni hisoblash</p>
  <p class="pe-good">P(−3)</p>
  <p class="pe-fix__why">(x + 3) = (x − (−3)), demak a = −3.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">P(2) = 0 → 2 koʻpaytuvchi</p>
  <p class="pe-good">(x − 2) koʻpaytuvchi</p>
  <p class="pe-fix__why">Koʻpaytuvchi — <b>qavs</b>, son emas. 2 esa nol
  deyiladi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Teoremaning butun kuchi shunda: <b>uzun boʻlish bir qoʻyishga aylanadi</b>.
  SAT'da qoldiq soʻralgan savol 20 soniyalik ish; boʻlishga oʻtirgan oʻquvchi esa
  ikki daqiqa yoʻqotadi va ishora xatosi qilish ehtimoli koʻp.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Nol», «ildiz», «koʻpaytuvchi» va «x oʻqi bilan kesishish» — bular <b>bitta
  narsaning toʻrt nomi</b>. SAT savolni har safar boshqa nom bilan beradi, javob
  esa oʻsha-oʻsha.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Teorema faqat <b>chiziqli</b> boʻluvchi (x − a) uchun ishlaydi. Boʻluvchi
  x<sup>2</sup> − 1 boʻlsa, uni avval (x − 1)(x + 1) deb ajrating va har biriga
  alohida qoʻying — SAT bundan nariga oʻtmaydi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  What is the remainder when <i>x</i><sup>2</sup> + 3<i>x</i> + 5 is divided by
  <i>x</i> + 1?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">3 — P(−1) = 1 − 3 + 5.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Is (<i>x</i> + 2) a factor of <i>x</i><sup>3</sup> + 2<i>x</i><sup>2</sup> −
  <i>x</i> − 2?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ha — P(−2) = −8 + 8 + 2 − 2 = 0.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  If <i>P</i>(4) = 0, which expression must be a factor of <i>P</i>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(<i>x</i> − 4) — koʻpaytuvchi teoremasi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Is (<i>x</i> − 1) a factor of <i>x</i><sup>3</sup> − 7<i>x</i> + 6?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ha — P(1) = 1 − 7 + 6 = 0.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  For what value of <i>k</i> is (<i>x</i> − 2) a factor of
  <i>x</i><sup>2</sup> + <i>kx</i> − 10?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>k</i> = 3 — P(2) = 4 + 2k − 10 = 0.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>polynomial</b><span>koʻphad</span></li>
  <li><b>remainder theorem</b><span>qoldiq haqidagi teorema</span></li>
  <li><b>factor theorem</b><span>koʻpaytuvchi haqidagi teorema</span></li>
  <li><b>is divided by</b><span>… ga boʻlinadi</span></li>
  <li><b>is a factor of</b><span>… ning koʻpaytuvchisi</span></li>
  <li><b>zero of the polynomial</b><span>koʻphadning noli</span></li>
  <li><b>constant term</b><span>erkin had</span></li>
  <li><b>evaluate</b><span>qiymatini hisoblamoq</span></li>
  <li><b>must be true</b><span>albatta toʻgʻri</span></li>
  <li><b>cubic</b><span>kubik (uchinchi darajali)</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Qoldiq = <b>P(a)</b> — boʻlish shart emas.</li>
    <li>P(a) = 0 boʻlsa <b>(x − a)</b> koʻpaytuvchi; aksi ham toʻgʻri.</li>
    <li>(x + 3) ni koʻrsangiz <b>x = −3</b> qoʻying.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-43 — higher-degree graphs
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-43: Graphs of Higher-Degree Polynomials — End Behavior & Multiplicity",
        "category": "math",
        "order": 43,
        "summary": (
            "Grafikning ikki chekkasini daraja va bosh koeffitsient hal qiladi; "
            "har bir nolda kesish yoki urinish — karralilikning juft-toqligi."
        ),
        "stories": ["Reading the Ridge Line"],
        "content": """
<h2>SAT-43: Graphs of Higher-Degree Polynomials — End Behavior & Multiplicity</h2>

<p>Uchinchi va toʻrtinchi darajali koʻphadning grafigini toʻliq chizish SAT'da
soʻralmaydi. Soʻraladigani ikkita: <mark>chekkalarda nima boʻladi</mark> va
<mark>har bir nolda grafik kesadimi yoki uriladimi</mark>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>daraja va bosh koeffitsientdan chekka xatti-harakatini aytasiz;</li>
    <li>karralilik juftmi toqmi — kesish yoki urinish deb oʻqiysiz;</li>
    <li>ajratilgan koʻrinishdan grafikni tasvirlaysiz;</li>
    <li>burilishlar soni darajadan bitta kam ekanini bilasiz.</li>
  </ul>
</div>

<h3>Chekka xatti-harakati — ikki savol</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Daraja</th><th>Bosh koeffitsient</th><th>Chap chekka</th><th>Oʻng chekka</th></tr>
  <tr><td>juft (2, 4)</td><td>musbat</td><td class="pm-word__sym">yuqoriga</td><td>yuqoriga</td></tr>
  <tr><td>juft</td><td>manfiy</td><td class="pm-word__sym">pastga</td><td>pastga</td></tr>
  <tr><td>toq (3, 5)</td><td>musbat</td><td class="pm-word__sym">pastga</td><td>yuqoriga</td></tr>
  <tr><td>toq</td><td>manfiy</td><td class="pm-word__sym">yuqoriga</td><td>pastga</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Yodlash oson: <b>juft daraja — ikki chekka bir xil</b> (parabola kabi),
  <b>toq daraja — ikki chekka qarama-qarshi</b> (chiziq kabi). Manfiy bosh
  koeffitsient esa rasmni shunchaki agʻdarib qoʻyadi.
</div>

<h3>Karralilik — kesish yoki urinish</h3>

<p>Nol qavsda necha marta takrorlansa, oʻsha uning <b>karraliligi</b>. Va grafik
uchun faqat bitta narsa muhim: juftmi yoki toqmi.</p>

<div class="pe-formula">
  <span class="pe-formula__label">At each zero</span>
  <span class="pe-chip pe-chip--s">toq karralilik → kesadi</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">juft karralilik → uriladi</span>
</div>

<p>y = (x − 1)(x + 2)<sup>2</sup> ni koʻrib chiqamiz. x = 1 nolining karraliligi 1
(toq) — grafik u yerda oʻqni <b>kesib oʻtadi</b>. x = −2 nolining karraliligi 2
(juft) — grafik u yerda oʻqqa <b>tegib qaytadi</b>.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 240" role="img"
       aria-label="The graph of y equals x minus one times x plus two squared: it
                   touches the x-axis at minus two and crosses it at one">
    <line class="pm-ln" x1="20" y1="139" x2="300" y2="139"/>
    <line class="pm-ln" x1="200" y1="14" x2="200" y2="230"/>
    <polyline class="pm-fill" fill="none"
      points="20,207 50,154 80,139 110,150 140,173 170,196 200,207 230,192 260,139 284,60"/>
    <circle cx="80"  cy="139" r="4"/>
    <circle cx="260" cy="139" r="4"/>
    <text class="pm-lbl" x="52"  y="130">x = −2</text>
    <text class="pm-lbl" x="238" y="130">x = 1</text>
    <text class="pm-lbl" x="46"  y="176">touches</text>
    <text class="pm-lbl" x="250" y="176">crosses</text>
  </svg>
  <figcaption>y = (x − 1)(x + 2)<sup>2</sup>. x = −2 da grafik oʻqqa tegib
  qaytadi (juft karralilik), x = 1 da kesib oʻtadi (toq).</figcaption>
</figure>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Ishorani tekshirish uchun nolning ikki tomonidan bittadan son qoʻying.
  Yuqoridagi grafikda x = −3 da qiymat manfiy, x = −1 da ham manfiy — demak
  grafik oʻqni kesmagan, faqat tegib qaytgan.
</div>

<h3>Burilishlar soni</h3>

<p>n-darajali koʻphadning grafigi <b>koʻpi bilan n − 1 marta</b> buriladi. Uchinchi
daraja — koʻpi bilan ikki burilish; toʻrtinchi — koʻpi bilan uch. SAT baʼzan
rasmni koʻrsatib «bu koʻphadning darajasi kamida qancha?» deb soʻraydi.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>end behavior</b><span>chekka xatti-harakati</span></li>
  <li><b>as x increases without bound</b><span>x cheksiz oshganda</span></li>
  <li><b>touches the x-axis but does not cross</b><span>oʻqqa tegadi, lekin kesmaydi</span></li>
  <li><b>multiplicity</b><span>karralilik</span></li>
  <li><b>at least degree</b><span>darajasi kamida …</span></li>
  <li><b>turning points</b><span>burilish nuqtalari</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = (<i>x</i> − 1)
    (<i>x</i> + 2)<sup>2</sup>. At which value of <i>x</i> does the graph of
    <i>f</i> touch the <i>x</i>-axis without crossing it?</p>
  </div>
  <ol class="ps-ch">
    <li><i>x</i> = −2</li>
    <li><i>x</i> = 1</li>
    <li><i>x</i> = 2</li>
    <li><i>x</i> = 0</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) x = −2</p>
      <p>(x + 2) kvadratda — karralilik 2, juft, demak urinish.</p>
      <p>Tekshiruv: f(−3) = −4 va f(−1) = −2 — ikkala tomonda ham manfiy, ishora
      almashmagan ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">x = 2</span>
  <span class="ps-trap__why">Qavsdagi son shundoq koʻchirilgan. (x + 2) noli
  x = <b>−2</b>; ishora almashadi (SAT-31).</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">55 s</span></p>
  <div class="ps-stem__q">
    <p>For the function <i>g</i>(<i>x</i>) = −2<i>x</i><sup>3</sup> +
    5<i>x</i> − 1, what happens as <i>x</i> increases without bound?</p>
  </div>
  <ol class="ps-ch">
    <li><i>g</i>(<i>x</i>) decreases without bound</li>
    <li><i>g</i>(<i>x</i>) increases without bound</li>
    <li><i>g</i>(<i>x</i>) approaches −1</li>
    <li><i>g</i>(<i>x</i>) approaches zero</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) decreases without bound</p>
      <p>Toq daraja va manfiy bosh koeffitsient: oʻng chekka <b>pastga</b>
      ketadi.</p>
      <p>Katta x da −2x<sup>3</sup> qolgan hamma haddan kattaroq boʻlib qoladi —
      chekkani doim bosh had hal qiladi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">approaches −1</span>
  <span class="ps-trap__why">Erkin had chekka xatti-harakatiga umuman taʼsir
  qilmaydi; u faqat y oʻqidagi nuqtani beradi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Grafik savolida faqat <b>uchta</b> narsaga qarang:</p>
  <ol>
    <li>Ikki chekka bir xil tomondami (juft daraja) yoki qarama-qarshimi (toq);</li>
    <li>Har bir nolda kesish (toq) yoki urinish (juft);</li>
    <li>Burilishlar soni — daraja kamida shundan bitta koʻp.</li>
  </ol>
  <p>Erkin had, oʻrtadagi koeffitsientlar va grafikning aniq balandligi bu
  savollarda deyarli hech qachon kerak boʻlmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">(x + 2)<sup>2</sup> → grafik x = 2 da uriladi</p>
  <p class="pe-good">x = −2 da</p>
  <p class="pe-fix__why">Qavsning noli — qavs ichidagi sonning
  qarama-qarshisi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">−2x<sup>3</sup> + 5x − 1 → chekkada −1 ga yaqinlashadi</p>
  <p class="pe-good">Pastga cheksiz ketadi</p>
  <p class="pe-fix__why">Chekkani <b>bosh had</b> boshqaradi, erkin had emas.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Karralilik 3 boʻlsa nima boʻladi? Toq — demak grafik <b>kesib oʻtadi</b>, lekin
  oʻtayotganda <em>yassilanadi</em>, yaʼni oʻqqa bir lahza yopishgandek koʻrinadi.
  SAT'da javob baribir «crosses» boʻladi: muhimi juft-toqlik.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Nollarning karraliligi yigʻindisi darajaga teng. (x − 1)(x + 2)<sup>2</sup> da
  1 + 2 = 3 — kubik. Bu qavslarni ochmasdan darajani aytishning eng tez
  yoʻli.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  What is the degree of <i>y</i> = (<i>x</i> − 3)<sup>2</sup>(<i>x</i> + 1)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">3 — karraliliklar yigʻindisi 2 + 1.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  At which zero does the graph of <i>y</i> = (<i>x</i> − 3)<sup>2</sup>
  (<i>x</i> + 1) cross the <i>x</i>-axis?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">x = −1 — karraliligi 1, toq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Describe the end behavior of <i>y</i> = <i>x</i><sup>4</sup> −
  3<i>x</i><sup>2</sup> + 1.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ikkala chekka ham yuqoriga — juft daraja, musbat bosh
  koeffitsient.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  A graph has four turning points. What is the least possible degree of the
  polynomial?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">5 — burilishlar soni koʻpi bilan daraja minus bir.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Describe the end behavior of <i>y</i> = −<i>x</i><sup>5</sup> + 2<i>x</i>.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Chap chekka yuqoriga, oʻng chekka pastga — toq daraja,
  manfiy bosh koeffitsient.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>end behavior</b><span>chekka xatti-harakati</span></li>
  <li><b>leading coefficient</b><span>bosh koeffitsient</span></li>
  <li><b>degree</b><span>daraja</span></li>
  <li><b>multiplicity</b><span>karralilik</span></li>
  <li><b>crosses / touches</b><span>kesadi / uriladi</span></li>
  <li><b>turning point</b><span>burilish nuqtasi</span></li>
  <li><b>without bound</b><span>chegarasiz, cheksiz</span></li>
  <li><b>even / odd degree</b><span>juft / toq daraja</span></li>
  <li><b>flattens out</b><span>yassilanadi</span></li>
  <li><b>at least</b><span>kamida</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Juft daraja</b> — chekkalar bir xil; <b>toq daraja</b> —
        qarama-qarshi.</li>
    <li>Nolda <b>toq karralilik kesadi, juft karralilik uriladi</b>.</li>
    <li>Chekkani faqat <b>bosh had</b> hal qiladi; erkin had emas.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-44 — exponential vs linear growth
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-44: Exponential vs. Linear Growth",
        "category": "math",
        "order": 44,
        "summary": (
            "Chiziqli oʻsish bir xil miqdorni QOʻSHADI, koʻrsatkichli oʻsish bir "
            "xil songa KOʻPAYTIRADI. Farqi bitta soʻzda: qoʻshish yoki foiz."
        ),
        "stories": ["The Squares of the Chessboard"],
        "content": """
<h2>SAT-44: Exponential vs. Linear Growth</h2>

<p>Bu SAT'dagi eng koʻp beriladigan «modelni tanlash» savoli, va u odatda bitta
soʻzga bogʻliq boʻladi. <mark>Chiziqli — har safar bir xil miqdor qoʻshiladi;
koʻrsatkichli — har safar bir xil songa koʻpaytiriladi.</mark></p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>jadvaldan qaysi model ekanini ikki qadamda aniqlaysiz;</li>
    <li>matndagi kalit soʻzlarni modelga bogʻlaysiz;</li>
    <li>foiz har doim koʻrsatkichli ekanini bilasiz;</li>
    <li>koʻrsatkichli oʻsish nima uchun oxirida chiziqlini ortda qoldirishini
        tushuntirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The test</span>
  <span class="pe-chip pe-chip--s">ayirmalar bir xil → chiziqli</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">nisbatlar bir xil → koʻrsatkichli</span>
</div>

<h3>Jadvalni tekshirish</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>x</th><th>Birinchi jadval</th><th>Ikkinchi jadval</th></tr>
  <tr><td>0</td><td>2</td><td>2</td></tr>
  <tr><td>1</td><td>5</td><td>6</td></tr>
  <tr><td>2</td><td>8</td><td>18</td></tr>
  <tr><td>3</td><td>11</td><td>54</td></tr>
  <tr><td></td><td class="pm-word__sym">har safar +3 → chiziqli</td>
      <td class="pm-word__sym">har safar ×3 → koʻrsatkichli</td></tr>
</table></div>

<p>Ikkala jadvalda ham «3» soni bor, lekin u butunlay boshqa ish qiladi. Birinchisida
u <b>qoʻshiladi</b>, ikkinchisida <b>koʻpaytiriladi</b>.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Jadval berilsa, ikki qadamni tartib bilan bajaring: avval qoʻshni qiymatlarni
  <b>ayiring</b>. Ayirmalar bir xil boʻlsa — chiziqli, tamom. Boʻlmasa,
  <b>boʻling</b> — nisbatlar bir xil boʻlsa koʻrsatkichli.
</div>

<h3>Matndagi kalit soʻzlar</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Matnda</th><th>Model</th></tr>
  <tr><td>increases by 40 each year</td><td class="pm-word__sym">chiziqli</td></tr>
  <tr><td>increases by 8% each year</td><td class="pm-word__sym">koʻrsatkichli</td></tr>
  <tr><td>doubles every hour</td><td class="pm-word__sym">koʻrsatkichli</td></tr>
  <tr><td>loses half its value each year</td><td class="pm-word__sym">koʻrsatkichli</td></tr>
  <tr><td>a fixed fee plus 5 dollars per item</td><td class="pm-word__sym">chiziqli</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Foiz koʻrsatkichli demakdir</b> — deyarli istisnosiz. Sababi: 8 foiz har yili
  <u>oʻsha yilgi</u> miqdordan olinadi, demak qoʻshiladigan son har yili
  oʻzgaradi. Chiziqli modelda esa qoʻshiladigan son doim bir xil qoladi.
</div>

<h3>Nega koʻrsatkichli har doim yutadi</h3>

<p>Ikki ishchi taqqoslaymiz. Birinchisi kuniga 100 ming som oladi. Ikkinchisi
birinchi kuni 1 som oladi, lekin har kuni maoshi ikki barobar oshadi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">10-kun: 100 ming va 512 som</span>
    <span class="pm-solve__why">Chiziqli hali ancha oldinda</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">18-kun: 100 ming va 131 mingdan koʻp</span>
    <span class="pm-solve__why">Koʻrsatkichli endigina oʻzib ketdi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">25-kun: 100 ming va 16 milliondan koʻp</span>
    <span class="pm-solve__why">Bir hafta ichida farq 160 barobar boʻldi</span>
  </div>
</div>

<p>Boshlanishi qanchalik kichik boʻlmasin, koʻrsatkichli oʻsish har qanday chiziqli
oʻsishni <b>oxir-oqibat</b> ortda qoldiradi. SAT bu jumlani deyarli shu soʻzlar
bilan beradi.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>increases by a constant amount</b><span>bir xil miqdorga oshadi → chiziqli</span></li>
  <li><b>increases by a constant percentage</b><span>bir xil foizga oshadi → koʻrsatkichli</span></li>
  <li><b>doubles / triples / halves</b><span>ikki, uch barobar / yarmiga</span></li>
  <li><b>which model best fits the data</b><span>qaysi model maʼlumotlarga mos keladi</span></li>
  <li><b>at a constant rate</b><span>bir xil tezlikda → odatda chiziqli</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">55 s</span></p>
  <div class="ps-stem__q">
    <p>A table shows the values 4, 12, 36 and 108 for <i>x</i> = 0, 1, 2 and 3.
    Which type of model best fits this data?</p>
  </div>
  <ol class="ps-ch">
    <li>Exponential, because each value is 3 times the one before</li>
    <li>Linear, because each value increases by 8</li>
    <li>Linear, because each value increases by 3</li>
    <li>Neither linear nor exponential</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) Exponential</p>
      <p>Ayirmalar: 8, 24, 72 — bir xil emas. Nisbatlar: 3, 3, 3 — bir xil.</p>
      <p><b>«increases by 8»</b> faqat birinchi qadamda toʻgʻri; keyingi qadamda
      24 qoʻshiladi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">Linear, because each value increases by 8</span>
  <span class="ps-trap__why">Faqat birinchi ikki qiymat tekshirilgan. Chiziqli
  deyish uchun <b>hamma</b> ayirma bir xil boʻlishi kerak.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>The number of members of a club increases by 6% each year. Which type of
    model describes the number of members?</p>
  </div>
  <ol class="ps-ch">
    <li>Exponential growth</li>
    <li>Linear growth</li>
    <li>Exponential decay</li>
    <li>Linear decay</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) Exponential growth</p>
      <p>Foiz — koʻpaytirish. Har yili aʼzolar soni 1.06 ga koʻpayadi
      (SAT-45).</p>
      <p><b>Linear growth</b> — «6 more members each year» boʻlganda toʻgʻri
      boʻlardi. Foiz belgisi butun farqni yaratadi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">Linear growth</span>
  <span class="ps-trap__why">«increases by 6 each year» va «increases by 6%
  each year» oʻrtasidagi farq eʼtibordan qolgan. Foiz belgisini har doim
  qidiring.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Modelni tanlash savolida <b>bitta savol</b> bering: har qadamda nima sodir
  boʻladi?</p>
  <ol>
    <li>Bir xil son <b>qoʻshiladimi</b>? → chiziqli;</li>
    <li>Bir xil songa <b>koʻpaytiriladimi</b>? → koʻrsatkichli;</li>
    <li>Matnda foiz, «doubles», «halves» bormi? → koʻrsatkichli.</li>
  </ol>
  <p>Jadvalda esa avval ayiring, keyin boʻling — bu tartib hech qachon
  adashtirmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">4, 12, 36 → chiziqli, chunki 8 qoʻshilyapti</p>
  <p class="pe-good">Koʻrsatkichli — har safar 3 ga koʻpayyapti</p>
  <p class="pe-fix__why">Ikkinchi qadamda 24 qoʻshiladi, 8 emas. Hamma ayirmani
  tekshiring.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">«8% oshadi» → har yili 8 qoʻshiladi</p>
  <p class="pe-good">Har yili 1.08 ga koʻpayadi</p>
  <p class="pe-fix__why">Foiz oʻsha yilgi miqdordan olinadi, shuning uchun
  qoʻshiladigan son har yili oʻsadi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Kamayish ham xuddi shunday ishlaydi: «har yili 500 dan tushadi» — chiziqli,
  «har yili 15 foizga tushadi» — koʻrsatkichli. Ikkinchisida narx nolga
  <b>yaqinlashadi, lekin hech qachon yetmaydi</b>.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ehtiyot boʻling: koʻrsatkichli grafik boshida <b>deyarli tekis</b> koʻrinadi va
  chiziqli grafikdan sekinroq oʻsayotgandek tuyuladi. Rasmning chap tomoniga
  qarab xulosa chiqarmang — modelni jadval yoki matn hal qiladi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Is 5, 10, 20, 40 linear or exponential?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Koʻrsatkichli — har safar 2 ga koʻpayadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Is 5, 10, 15, 20 linear or exponential?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Chiziqli — har safar 5 qoʻshiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A phone loses 20% of its value each year. Which model is this?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Koʻrsatkichli kamayish — foiz koʻpaytirishni
  bildiradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  A taxi charges 10,000 som plus 3,000 som per kilometre. Which model is this?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Chiziqli — har kilometrga bir xil miqdor
  qoʻshiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Is 100, 90, 81, 72.9 linear or exponential?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Koʻrsatkichli — har safar 0.9 ga koʻpayadi, yaʼni 10
  foizdan tushadi.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>linear growth</b><span>chiziqli oʻsish</span></li>
  <li><b>exponential growth</b><span>koʻrsatkichli oʻsish</span></li>
  <li><b>exponential decay</b><span>koʻrsatkichli kamayish</span></li>
  <li><b>constant amount</b><span>oʻzgarmas miqdor</span></li>
  <li><b>constant percentage</b><span>oʻzgarmas foiz</span></li>
  <li><b>common difference</b><span>umumiy ayirma (chiziqli)</span></li>
  <li><b>common ratio</b><span>umumiy nisbat (koʻrsatkichli)</span></li>
  <li><b>doubles / halves</b><span>ikki barobar oshadi / yarmiga tushadi</span></li>
  <li><b>best fits the data</b><span>maʼlumotlarga eng mos keladi</span></li>
  <li><b>eventually exceeds</b><span>oxir-oqibat ortda qoldiradi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Qoʻshish — chiziqli, koʻpaytirish — koʻrsatkichli.</b></li>
    <li>Jadvalda avval <b>ayiring</b>, keyin <b>boʻling</b>.</li>
    <li><b>Foiz</b> deyarli har doim koʻrsatkichli modelni bildiradi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-45 — writing exponential functions
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-45: Writing Exponential Functions (y = ab^x) from Word Problems",
        "category": "math",
        "order": 45,
        "summary": (
            "a — boshlangʻich qiymat, b — har qadamdagi koeffitsient. Oʻsishda "
            "b = 1 + foiz, kamayishda b = 1 − foiz."
        ),
        "stories": ["Only Three Percent a Month"],
        "content": """
<h2>SAT-45: Writing Exponential Functions from Word Problems</h2>

<p>SAT-44 da modelni <em>tanidik</em>. Endi uni <mark>yozamiz</mark>, va bunda
faqat ikkita son kerak: qayerdan boshlangan va har qadamda nechaga koʻpayadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>a va b ni matndan toʻgʻridan-toʻgʻri olasiz;</li>
    <li>foizni koeffitsientga aylantirasiz;</li>
    <li>oʻsish va kamayishni ishoradan ajratasiz;</li>
    <li>«har 3 soatda» kabi boshqa davrni koʻrsatkichda hisobga olasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The model</span>
  <span class="pe-chip pe-chip--v">a = boshlangʻich qiymat</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">b = har qadamdagi koeffitsient</span>
</div>

<h3>Foizni koeffitsientga aylantirish</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Matnda</th><th>b</th><th>Nima uchun</th></tr>
  <tr><td>increases by 5%</td><td class="pm-word__sym">1.05</td><td>eskisi (1) + qoʻshilgani (0.05)</td></tr>
  <tr><td>increases by 30%</td><td class="pm-word__sym">1.3</td><td>1 + 0.3</td></tr>
  <tr><td>decreases by 15%</td><td class="pm-word__sym">0.85</td><td>1 − 0.15</td></tr>
  <tr><td>doubles</td><td class="pm-word__sym">2</td><td>ikki barobar</td></tr>
  <tr><td>loses half</td><td class="pm-word__sym">0.5</td><td>yarmi qoladi</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  «Increases by 5%» uchun b = <b>1.05</b>, 0.05 emas. 0.05 ni qoʻysangiz model har
  yili 95 foizni yoʻqotadigan boʻlib qoladi — bu SAT'dagi eng koʻp uchraydigan
  bitta xato.
</div>

<h3>Uchta misol</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">500 bakteriya, har soatda ikki barobar</span>
    <span class="pm-solve__why">a = 500, b = 2</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">20,000 dollarlik mashina, har yili 15% tushadi</span>
    <span class="pm-solve__why">a = 20,000, b = 0.85</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">8,000 aholi, har yili 3% oʻsadi</span>
    <span class="pm-solve__why">a = 8,000, b = 1.03</span>
  </div>
</div>

<p>Uchinchisida ikki yildan keyingi aholi:
8,000 × 1.03 × 1.03 = <b>8,487.2</b> kishi. Uch yildan keyin
8,741.816. Har yili qoʻshiladigan son oʻsib boradi — 240, keyin 247.2 — chunki
foiz har safar kattaroq miqdordan olinadi.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Yozgan modelingizni <b>x = 0 da tekshiring</b>. Har qanday son nol darajada 1 ga
  teng, shuning uchun javob a ga teng chiqishi kerak — yaʼni matndagi boshlangʻich
  qiymat. Chiqmasa, model notoʻgʻri.
</div>

<h3>Davr bir yilga teng boʻlmasa</h3>

<p>«500 bakteriya <b>har 3 soatda</b> ikki barobar oshadi» — bu holda soatlar sonini
3 ga boʻlish kerak, chunki koʻpayish har soatda emas, har uchinchi soatda sodir
boʻladi. 9 soatdan keyin uch marta ikkilanadi: 500 → 1,000 → 2,000 → 4,000.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Buni yodlash shart emas — <b>sanab koʻring</b>. Har 3 soatda bir marta
  ikkilansa, 12 soatda toʻrt marta ikkilanadi. Koʻrsatkichga vaqtni davrga boʻlib
  qoʻyish shuni qisqa yozadi, xolos.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>which function models the situation</b><span>qaysi funksiya vaziyatni ifodalaydi</span></li>
  <li><b>the initial value</b><span>boshlangʻich qiymat (a)</span></li>
  <li><b>where t is the number of years</b><span>bunda t — yillar soni</span></li>
  <li><b>decreases by 15% each year</b><span>har yili 15% ga kamayadi → 0.85</span></li>
  <li><b>doubles every three hours</b><span>har uch soatda ikki barobar oshadi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>A car is worth 20,000 dollars and loses 15% of its value each year. Which
    function gives its value after <i>t</i> years?</p>
  </div>
  <ol class="ps-ch">
    <li>20,000(0.85)<sup>t</sup></li>
    <li>20,000(1.15)<sup>t</sup></li>
    <li>20,000(0.15)<sup>t</sup></li>
    <li>20,000 − 15<i>t</i></li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 20,000(0.85)<sup>t</sup></p>
      <p>Har yili 85 foizi qoladi, demak b = 1 − 0.15 = 0.85.</p>
      <p>Tekshiruv: bir yildan keyin 17,000 — bu 20,000 ning 15 foizi
      kamaygani ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">20,000(0.15)<sup>t</sup></span>
  <span class="ps-trap__why">Foiz koeffitsient sifatida shundoq qoʻyilgan. Bu
  model bir yildan keyin 3,000 beradi — mashina qiymatining 85 foizini
  yoʻqotgan boʻlardi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>A town has 8,000 people and its population grows by 3% each year. To the
    nearest whole number, what will the population be after 2 years?</p>
  </div>
  <ol class="ps-ch">
    <li>8,487</li>
    <li>8,480</li>
    <li>8,240</li>
    <li>8,600</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 8,487</p>
      <p>8,000 × 1.03 = 8,240, keyin 8,240 × 1.03 = 8,487.2.</p>
      <p><b>8,480</b> — har yili 240 qoʻshilgan, yaʼni chiziqli hisoblangan.
      Ikkinchi yilda 247.2 qoʻshilishi kerak edi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">8,480</span>
  <span class="ps-trap__why">Birinchi yilning qoʻshimchasi ikkinchi yilga ham
  koʻchirilgan — bu chiziqli oʻsish (SAT-44). Foizda har yilgi qoʻshimcha
  oʻsib boradi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Javoblar funksiya boʻlsa, hisoblamang — <b>bitta yilni sanang</b>:</p>
  <ol>
    <li>Matndan bir yildan keyingi qiymatni ogʻzaki toping;</li>
    <li>Har bir javobga <i>t</i> = 1 qoʻying;</li>
    <li>Mos kelmaganini oʻchiring — odatda bitta variant qoladi.</li>
  </ol>
  <p><i>t</i> = 0 ham foydali: u a ni tekshiradi va notoʻgʻri boshlangʻich
  qiymatli variantlarni darrov oʻchiradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">«increases by 5%» → b = 0.05</p>
  <p class="pe-good">b = 1.05</p>
  <p class="pe-fix__why">Eskisi ham qoladi: 1 (butun) + 0.05 (qoʻshimcha).</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">8,000 aholi, 3% → 2 yildan keyin 8,480</p>
  <p class="pe-good">8,487</p>
  <p class="pe-fix__why">Ikkinchi yilda foiz 8,240 dan olinadi, 8,000 dan
  emas.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>b ning qiymati javobni darrov aytadi:</b> b birdan katta boʻlsa oʻsish,
  birdan kichik boʻlsa kamayish. Shuning uchun kamayish masalasida javobingizda
  0 va 1 orasidagi son turishi shart.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Koʻrsatkichli kamayish <b>hech qachon nolga yetmaydi</b>. 20,000 ning 85 foizi,
  keyin uning 85 foizi… har safar kichrayadi, lekin musbat qoladi. Shuning uchun
  «qachon mashina bepul boʻladi» degan savolning javobi yoʻq.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Write a function for 300 bacteria that double every hour.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">300(2)<sup>t</sup> — a = 300, b = 2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Write a function for a 1,200-dollar laptop losing 20% of its value each
  year.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">1,200(0.8)<sup>t</sup> — b = 1 − 0.2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  What is that laptop worth after 3 years?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">614.40 dollar — 1,200 × 0.8 × 0.8 × 0.8.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  A savings account holds 50 dollars and grows by 10% a year. Write the
  function.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">50(1.1)<sup>t</sup>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  400 bacteria double every 3 hours. How many are there after 9 hours?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">3,200 — uch marta ikkilanadi: 800, 1,600,
  3,200.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>initial value</b><span>boshlangʻich qiymat (a)</span></li>
  <li><b>growth factor</b><span>oʻsish koeffitsienti (b)</span></li>
  <li><b>models the situation</b><span>vaziyatni ifodalaydi</span></li>
  <li><b>each year / per year</b><span>har yili</span></li>
  <li><b>loses value</b><span>qiymatini yoʻqotadi</span></li>
  <li><b>depreciates</b><span>qadrsizlanadi</span></li>
  <li><b>to the nearest whole number</b><span>eng yaqin butun songacha</span></li>
  <li><b>doubles every three hours</b><span>har uch soatda ikki barobar</span></li>
  <li><b>rate of growth</b><span>oʻsish sur'ati</span></li>
  <li><b>compounded</b><span>ustiga qoʻshilib boradigan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>a</b> — boshlangʻich qiymat, <b>b</b> — har qadamdagi
        koʻpaytuvchi.</li>
    <li>Oʻsishda <b>b = 1 + foiz</b>, kamayishda <b>b = 1 − foiz</b>.</li>
    <li>Modelni <b>x = 0 va x = 1</b> da tekshiring — 20 soniyada barcha
        notoʻgʻri variant oʻchadi.</li>
  </ul>
</div>
""",
    },
]
