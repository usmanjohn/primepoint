# -*- coding: utf-8 -*-
"""Prime SAT Math — lessons 31–35 (kvadrat uchhad: ajratishdan uchigacha).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_SAT.md
Lesson list: tutorial/management/commands/toc_prime_sat_math.txt

  mashqlar — practice/management/commands/_practice_ps_31_35.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_sat_readings_31_35.py

⚠️ ESKI SAT-31 … SAT-35 ustiga yoziladi (--republish).
⚠️ Til: sarlavha va test savollari inglizcha, tushuntirish oʻzbekcha.

⚠️ Kumulyativ (SAT-1…30 erkin: butun Blok A, daraja va ildiz, koʻphadlar,
   koʻpaytirish, GCF/guruhlash, kvadratlar ayirmasi va toʻliq kvadrat):
  • SAT-31 — x² + bx + c ni ajratish va nollarini topish (koʻpaytma nol qoidasi).
  • SAT-32 — ax² + bx + c: AC usuli va guruhlash (SAT-29 ning davomi).
  • SAT-33 — kvadrat tenglama formulasi; diskriminant tanishtiriladi.
  • SAT-34 — diskriminant boʻyicha ildizlar soni va turi; grafik bilan bogʻlash.
  • SAT-35 — uchi shakli y = a(x − h)² + k va uchning koordinatalari.
  • ⛔ Parabola grafigini toʻliq chizish (SAT-37) YOʻQ; maksimum/minimum masalalari
    (SAT-36) YOʻQ; kompleks sonlar YOʻQ; ps-desmos SAT-83 dan.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_sat_31_35.py \\
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
    # SAT-31 — factoring x² + bx + c
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-31: Factoring Standard Quadratics (x² + bx + c)",
        "category": "math",
        "order": 31,
        "summary": (
            "Ikki son toping: koʻpaytmasi c ga, yigʻindisi b ga teng. Keyin "
            "koʻpaytma nol qoidasi bilan tenglamaning ildizlarini oling."
        ),
        "stories": ["The Stage That Had To Fit"],
        "content": """
<h2>SAT-31: Factoring Standard Quadratics (x² + bx + c)</h2>

<p>SAT-28 da (<em>x</em> + 3)(<em>x</em> + 4) ni ochib <em>x</em><sup>2</sup> + 7<em>x</em> +
12 olgan edik. Endi teskari savol: <mark>x<sup>2</sup> + 7x + 12 berilgan, qavslarni
qanday topamiz?</mark> Javob bitta jumlada: koʻpaytmasi 12 ga, yigʻindisi 7 ga teng ikki
sonni izlaymiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>ikki sonni koʻpaytma va yigʻindi boʻyicha topasiz;</li>
    <li>ishoralarni <em>c</em> ning ishorasiga qarab darrov aniqlaysiz;</li>
    <li>koʻpaytma nol qoidasi bilan tenglamani yechasiz;</li>
    <li>«ajratish» va «yechish» bir xil narsa emasligini bilasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The search</span>
  <span class="pe-chip pe-chip--v">koʻpaytmasi = c</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">yigʻindisi = b</span>
</div>

<h3>Ikki son izlash</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x<sup>2</sup> + 7x + 12</span>
    <span class="pm-solve__why">c = 12, b = 7</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">12 = 1·12, 2·6, 3·4</span>
    <span class="pm-solve__why">Koʻpaytuvchi juftlarini yozib chiqdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3 + 4 = 7 ✓  →  (x + 3)(x + 4)</span>
    <span class="pm-solve__why">Yigʻindisi mos kelgan juftlik — javob</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Juftlarni <b>tartib bilan</b> yozing: 1 dan boshlab. Tasodifiy urinish uch marta koʻp
  vaqt oladi va bitta juftlikni tashlab ketish ehtimolini oshiradi.
</div>

<h3>Ishoralarni oldindan bilish</h3>

<p>Qavslardagi ishoralarni topishdan oldin <u>aniqlash</u> mumkin — faqat
<em>c</em> va <em>b</em> ning ishorasiga qarang:</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>c</th><th>b</th><th>Qavslardagi ishoralar</th><th>Misol</th></tr>
  <tr><td>musbat</td><td>musbat</td><td class="pm-word__sym">ikkalasi ham +</td><td>(x + 3)(x + 4)</td></tr>
  <tr><td>musbat</td><td>manfiy</td><td class="pm-word__sym">ikkalasi ham −</td><td>(x − 2)(x − 3)</td></tr>
  <tr><td>manfiy</td><td>—</td><td class="pm-word__sym">bittasi +, bittasi −</td><td>(x + 5)(x − 3)</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>c manfiy boʻlsa</b>, ishoralar har xil — va kattaroq son <em>b</em> ning
  ishorasini oladi. x<sup>2</sup> + 2x − 15 da 5 va 3 kerak, va b musbat boʻlgani uchun
  <b>+5</b> va −3: (x + 5)(x − 3).
</div>

<h3>Misol 2 — ikkala ishora ham manfiy</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x<sup>2</sup> − 5x + 6</span>
    <span class="pm-solve__why">c musbat, b manfiy → ikkala son ham manfiy</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">(x − 2)(x − 3)</span>
    <span class="pm-solve__why">(−2)(−3) = 6 ✓ va −2 + (−3) = −5 ✓</span>
  </div>
</div>

<h3>Ajratishdan yechishga: koʻpaytma nol qoidasi</h3>

<blockquote>Agar ikki sonning koʻpaytmasi nolga teng boʻlsa, ulardan <u>kamida
bittasi</u> nolga teng. Boshqa yoʻli yoʻq.</blockquote>

<p>Shuning uchun tenglamani yechish uchun avval bir tomonni <b>nolga</b> keltiramiz,
keyin ajratamiz, keyin har bir qavsni alohida nolga tenglashtiramiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x<sup>2</sup> + 7x + 12 = 0</span>
    <span class="pm-solve__why">Oʻng tomon allaqachon nol</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(x + 3)(x + 4) = 0</span>
    <span class="pm-solve__why">Ajratdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = −3  yoki  x = −4</span>
    <span class="pm-solve__why">Har bir qavs nolga tenglashtirildi — ishora almashadi</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Ildizlar qavsdagi sonlarning <b>qarama-qarshisi</b>: (x + 3) qavsi x = <b>−3</b> ni
  beradi. Bu SAT'dagi eng koʻp uchraydigan bir belgilik xato, va tuzoq javob har doim
  variantlar orasida turadi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>factor the expression</b><span>ifodani ajrating — javob koʻpaytma</span></li>
  <li><b>the solutions to the equation</b><span>tenglamaning yechimlari (ildizlari)</span></li>
  <li><b>the zeros of the function</b><span>funksiyaning nollari — bir xil narsa</span></li>
  <li><b>which is a factor of</b><span>qaysi biri koʻpaytuvchi</span></li>
  <li><b>the sum of the solutions</b><span>yechimlar yigʻindisi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>Which expression is equivalent to <i>x</i><sup>2</sup> + 9<i>x</i> + 20?</p>
  </div>
  <ol class="ps-ch">
    <li>(<i>x</i> + 2)(<i>x</i> + 10)</li>
    <li>(<i>x</i> + 4)(<i>x</i> + 5)</li>
    <li>(<i>x</i> − 4)(<i>x</i> − 5)</li>
    <li>(<i>x</i> + 9)(<i>x</i> + 20)</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) (x + 4)(x + 5)</p>
      <p>20 = 4 × 5, va 4 + 5 = 9 ✓</p>
      <p><b>(x + 2)(x + 10)</b> — koʻpaytmasi 20, lekin yigʻindisi 12. <b>Ikkala</b>
      shart ham bajarilishi kerak.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">(x + 2)(x + 10)</span>
  <span class="ps-trap__why">Faqat koʻpaytma tekshirilgan. Ochib koʻring:
  x<sup>2</sup> + 12x + 20 — oʻrtadagi had mos emas.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>What are the solutions to <i>x</i><sup>2</sup> − 3<i>x</i> − 10 = 0?</p>
  </div>
  <ol class="ps-ch">
    <li><i>x</i> = −5 and <i>x</i> = 2</li>
    <li><i>x</i> = −2 and <i>x</i> = 5</li>
    <li><i>x</i> = 2 and <i>x</i> = 5</li>
    <li><i>x</i> = −2 and <i>x</i> = −5</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) x = −2 va x = 5</p>
      <p>c = −10 manfiy, demak ishoralar har xil; kerakli juftlik −5 va +2? Tekshiramiz:
      (−5)(2) = −10 ✓ lekin −5 + 2 = −3 ✓ — demak qavslar (x − 5)(x + 2).</p>
      <p>Nollar: x = 5 va x = −2 — qavsdagi sonlarning <b>qarama-qarshisi</b>.</p>
      <p>Tekshiruv: 25 − 15 − 10 = 0 ✓ va 4 + 6 − 10 = 0 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">x = −5 and x = 2</span>
  <span class="ps-trap__why">Ishoralar almashtirilmagan: qavslar (x − 5)(x + 2) edi,
  demak ildizlar +5 va −2. Har doim asl tenglamaga qoʻyib tekshiring.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Ildizlar soʻralganda ajratishga urinmasangiz ham boʻladi:</p>
  <ol>
    <li>Javoblardagi sonlarni <b>asl tenglamaga qoʻying</b>.</li>
    <li>Nol chiqsa — u ildiz.</li>
    <li>Ikkala soni ham nol beradigan variant — javob.</li>
  </ol>
  <p>Bu koʻpincha ajratishdan tezroq va ishora xatosini butunlay chetlab
  oʻtadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">(x + 3)(x + 4) = 0 → x = 3 va x = 4</p>
  <p class="pe-good">x = −3 va x = −4</p>
  <p class="pe-fix__why">Qavsni nolga tenglashtiring: x + 3 = 0 → x = −3.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">x<sup>2</sup> + 5x = 14 → (x + 7)(x − 2) = 14</p>
  <p class="pe-good">Avval nolga keltiring: x<sup>2</sup> + 5x − 14 = 0</p>
  <p class="pe-fix__why">Koʻpaytma nol qoidasi faqat <b>nol</b> uchun ishlaydi. 14 ni
  koʻp xil yoʻl bilan koʻpaytmaga ajratish mumkin.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Ajratish» va «yechish» bir xil emas. <b>Ajratish</b> — ifodani koʻpaytmaga aylantirish;
  <b>yechish</b> — tenglamaning ildizlarini topish. SAT ikkalasini ham soʻraydi va
  javoblari boshqa-boshqa: (x + 3)(x + 4) va x = −3, −4.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ajratishni <b>teskari tekshirish</b> odat qiling: javobni oching va asl ifoda chiqishiga ishonch hosil qiling. Bu 10 soniya oladi va SAT'dagi eng koʻp yoʻqotiladigan ballarni saqlab qoladi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Factor: <i>x</i><sup>2</sup> + 8<i>x</i> + 15</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(<i>x</i> + 3)(<i>x</i> + 5) — 3 × 5 = 15 va 3 + 5 = 8.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Factor: <i>x</i><sup>2</sup> − 7<i>x</i> + 10</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(<i>x</i> − 2)(<i>x</i> − 5) — c musbat, b manfiy, demak
  ikkala son ham manfiy.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Factor: <i>x</i><sup>2</sup> + 3<i>x</i> − 18</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(<i>x</i> + 6)(<i>x</i> − 3) — c manfiy, demak ishoralar har
  xil; kattarogʻi (+6) b ning ishorasini oladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Solve: <i>x</i><sup>2</sup> − 2<i>x</i> − 8 = 0</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> = 4 yoki <i>x</i> = −2 — (x − 4)(x + 2) = 0.
  Tekshiruv: 16 − 8 − 8 = 0 ✓</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A rectangle has an area of 40 square metres and a perimeter of 26 metres. What are its
  side lengths?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">5 va 8 metr — yarim perimetr 13, demak yigʻindisi 13,
  koʻpaytmasi 40 boʻlgan ikki son kerak.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>quadratic</b><span>kvadrat (ikkinchi darajali)</span></li>
  <li><b>factor</b><span>koʻpaytuvchilarga ajratmoq</span></li>
  <li><b>solutions / roots</b><span>yechimlar / ildizlar</span></li>
  <li><b>zeros of the function</b><span>funksiyaning nollari</span></li>
  <li><b>zero product property</b><span>koʻpaytma nol qoidasi</span></li>
  <li><b>factor pairs</b><span>koʻpaytuvchi juftliklari</span></li>
  <li><b>set equal to zero</b><span>nolga tenglashtirmoq</span></li>
  <li><b>opposite sign</b><span>qarama-qarshi ishora</span></li>
  <li><b>substitute to check</b><span>tekshirish uchun oʻrniga qoʻymoq</span></li>
  <li><b>sum of the solutions</b><span>yechimlar yigʻindisi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Ikki son izlang: <b>koʻpaytmasi c</b>, <b>yigʻindisi b</b>.</li>
    <li>Ishoralarni <em>c</em> hal qiladi: musbat → bir xil, manfiy → har xil.</li>
    <li>Ildizlar qavsdagi sonlarning <b>qarama-qarshisi</b>, va tenglama avval
        <b>nolga</b> keltiriladi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-32 — factoring ax² + bx + c
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-32: Factoring Advanced Quadratics (ax² + bx + c)",
        "category": "math",
        "order": 32,
        "summary": (
            "x² oldida son turganda AC usuli ishlatiladi: a·c ni koʻpaytiring, "
            "shu koʻpaytmani beradigan va b ni yigʻadigan ikki sonni toping, "
            "keyin guruhlang."
        ),
        "stories": ["Sixty and Seventeen"],
        "content": """
<h2>SAT-32: Factoring Advanced Quadratics (ax² + bx + c)</h2>

<p>SAT-31 da <em>x</em><sup>2</sup> oldida hech narsa yoʻq edi, va ikki son izlash yetardi.
Endi u yerda son paydo boʻladi: 2<em>x</em><sup>2</sup> + 7<em>x</em> + 3. Taxmin qilish
bilan ham topish mumkin, lekin <mark>tartibli usul</mark> bor — va u har safar
ishlaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>AC usulini bosqichma-bosqich qoʻllaysiz;</li>
    <li>oʻrtadagi hadni ikkiga boʻlib, guruhlash bilan ajratasiz (SAT-29);</li>
    <li>manfiy koeffitsientlarda ham adashmaysiz;</li>
    <li>javobni qavsni ochib tekshirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The AC method</span>
  <span class="pe-chip pe-chip--v">a · c</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">koʻpaytmasi ac, yigʻindisi b</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">guruhlash</span>
</div>

<h3>Toʻrt qadam</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x<sup>2</sup> + 7x + 3</span>
    <span class="pm-solve__why">a = 2, b = 7, c = 3</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">a · c = 6</span>
    <span class="pm-solve__why">1-qadam: chekkadagi ikki sonni koʻpaytirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">6 = 6 × 1, va 6 + 1 = 7 ✓</span>
    <span class="pm-solve__why">2-qadam: koʻpaytmasi 6, yigʻindisi 7 boʻlgan juftlik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x<sup>2</sup> + 6x + x + 3</span>
    <span class="pm-solve__why">3-qadam: oʻrtadagi hadni shu ikki songa boʻldik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2x(x + 3) + 1(x + 3) = (x + 3)(2x + 1)</span>
    <span class="pm-solve__why">4-qadam: guruhlash (SAT-29)</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Uchinchi qadamda ikki sonni <b>qaysi tartibda</b> yozish ahamiyatsiz: 2x² + x + 6x + 3
  ham xuddi shu javobni beradi. Guruhlashda qavs ichidagilar baribir bir xil chiqadi.
</div>

<h3>Manfiy koeffitsient bilan</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x<sup>2</sup> − 10x + 8</span>
    <span class="pm-solve__why">a · c = 24; b manfiy, c musbat → ikkala son ham manfiy</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(−6)(−4) = 24 ✓ va −6 + (−4) = −10 ✓</span>
    <span class="pm-solve__why">Juftlik topildi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x<sup>2</sup> − 6x − 4x + 8</span>
    <span class="pm-solve__why">Oʻrtadagi had boʻlindi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3x(x − 2) − 4(x − 2) = (x − 2)(3x − 4)</span>
    <span class="pm-solve__why">Ikkinchi guruhdan <b>−4</b> chiqarildi, +4 emas</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Ikkinchi guruh manfiy had bilan boshlansa, undan <b>manfiy</b> koʻpaytuvchi chiqaring.
  Aks holda qavs ichidagilar mos kelmaydi va guruhlash toʻxtab qoladi.
</div>

<h3>Misol (SAT darajasi) — katta sonlar</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">6x<sup>2</sup> + 11x − 10</span>
    <span class="pm-solve__why">a · c = −60; ishoralar har xil boʻladi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">15 × (−4) = −60 ✓ va 15 + (−4) = 11 ✓</span>
    <span class="pm-solve__why">Juftlikni tartib bilan izladik: 1·60, 2·30, 3·20, 4·15</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">6x<sup>2</sup> + 15x − 4x − 10</span>
    <span class="pm-solve__why">Oʻrtadagi had boʻlindi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3x(2x + 5) − 2(2x + 5) = (2x + 5)(3x − 2)</span>
    <span class="pm-solve__why">Tekshiruv: qavslarni oching — 6x<sup>2</sup> + 11x − 10 ✓</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Har doim <b>GCF dan boshlang</b> (SAT-29). 6x<sup>2</sup> + 15x + 6 da avval 3 ni
  chiqaring: 3(2x<sup>2</sup> + 5x + 2). Kichikroq sonlar bilan AC usuli ancha
  tez ishlaydi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>factor completely</b><span>toʻliq ajrating</span></li>
  <li><b>which is a factor of</b><span>qaysi biri koʻpaytuvchi</span></li>
  <li><b>the solutions to the equation</b><span>tenglamaning yechimlari</span></li>
  <li><b>where a, b and c are integers</b><span>a, b va c — butun sonlar</span></li>
  <li><b>rewrite the middle term</b><span>oʻrtadagi hadni qayta yozing</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>Which expression is equivalent to 2<i>x</i><sup>2</sup> + 7<i>x</i> + 3?</p>
  </div>
  <ol class="ps-ch">
    <li>(2<i>x</i> + 1)(<i>x</i> + 3)</li>
    <li>(2<i>x</i> + 3)(<i>x</i> + 1)</li>
    <li>(2<i>x</i> + 7)(<i>x</i> + 3)</li>
    <li>(<i>x</i> + 1)(<i>x</i> + 3)</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) (2x + 1)(x + 3)</p>
      <p>Oching: 2x<sup>2</sup> + 6x + x + 3 = 2x<sup>2</sup> + 7x + 3 ✓</p>
      <p><b>(2x + 3)(x + 1)</b> ochilganda 2x<sup>2</sup> + 5x + 3 beradi — sonlar
      oʻrin almashganda oʻrta had oʻzgaradi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">(2x + 3)(x + 1)</span>
  <span class="ps-trap__why">Toʻgʻri sonlar, notoʻgʻri joyda. <em>a</em> ≠ 1 boʻlganda
  sonlarning oʻrni oʻrta hadni oʻzgartiradi — javobni albatta oching.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">80 s</span></p>
  <div class="ps-stem__q">
    <p>Which expression is equivalent to 6<i>x</i><sup>2</sup> + 11<i>x</i> − 10?</p>
  </div>
  <ol class="ps-ch">
    <li>(2<i>x</i> − 5)(3<i>x</i> + 2)</li>
    <li>(3<i>x</i> − 2)(2<i>x</i> + 5)</li>
    <li>(6<i>x</i> − 5)(<i>x</i> + 2)</li>
    <li>(3<i>x</i> + 2)(2<i>x</i> − 5)</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) (3x − 2)(2x + 5)</p>
      <p>Oching: 6x<sup>2</sup> + 15x − 4x − 10 = 6x<sup>2</sup> + 11x − 10 ✓</p>
      <p><b>(2x − 5)(3x + 2)</b> — oʻsha sonlar, lekin ishoralar boshqa qavsda:
      u 6x<sup>2</sup> − 11x − 10 beradi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">(2x − 5)(3x + 2)</span>
  <span class="ps-trap__why">Minus notoʻgʻri qavsda: natija oʻrta hadning ishorasini
  teskari qiladi. Bitta koʻpaytmani (Outer + Inner) hisoblab tekshirish yetadi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Javoblar qavs boʻlsa, ajratmang — <b>oching</b>:</p>
  <ol>
    <li>Har bir javobning <b>oxirgi sonini</b> tekshiring (Last): mos kelmasa
        oʻchiring.</li>
    <li>Qolganlarining <b>oʻrta hadini</b> hisoblang (Outer + Inner).</li>
    <li>Yoki bitta son qoʻying: <i>x</i> = 1 koʻpincha ikki javobni ajratadi.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">2x<sup>2</sup> + 7x + 3 = (2x + 3)(x + 1)</p>
  <p class="pe-good">(2x + 1)(x + 3)</p>
  <p class="pe-fix__why">Sonlar oʻrin almashgan: birinchi variant 5x beradi, 7x
  emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">3x<sup>2</sup> − 6x − 4x + 8 = 3x(x − 2) + 4(x − 2)</p>
  <p class="pe-good">3x(x − 2) − 4(x − 2)</p>
  <p class="pe-fix__why">Ikkinchi guruh −4x bilan boshlanadi, demak chiqariladigan
  koʻpaytuvchi ham manfiy.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  AC usulining eng qimmatli tomoni — u <b>taxminga oʻrin qoldirmaydi</b>. Katta sonlarda
  (masalan 6 va −10) taxmin qilish oʻnlab urinish talab qiladi; AC esa uch qadamda
  javobga olib boradi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  a ≠ 1 boʻlgan ifodada javob qavslarining <b>tartibi</b> ahamiyatsiz: (x + 3)(2x + 1) va (2x + 1)(x + 3) bir xil javob. SAT ikkalasini ham toʻgʻri deb hisoblaydi, shuning uchun variantlar orasida ikkalasi boʻlmaydi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Factor: 2<i>x</i><sup>2</sup> + 5<i>x</i> + 2</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(2<i>x</i> + 1)(<i>x</i> + 2) — ac = 4, juftlik 4 va 1.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Factor: 3<i>x</i><sup>2</sup> + 7<i>x</i> + 2</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(3<i>x</i> + 1)(<i>x</i> + 2) — ac = 6, juftlik 6 va 1.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Factor: 2<i>x</i><sup>2</sup> − 7<i>x</i> + 6</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(2<i>x</i> − 3)(<i>x</i> − 2) — ac = 12, juftlik −3 va −4.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Factor: 5<i>x</i><sup>2</sup> + 11<i>x</i> + 2</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(5<i>x</i> + 1)(<i>x</i> + 2) — ac = 10, juftlik 10 va 1.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A rectangle has an area of 2<i>x</i><sup>2</sup> + 7<i>x</i> + 3 square metres. Write
  its possible dimensions.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(2<i>x</i> + 1) va (<i>x</i> + 3) metr. Ajratish — yuzadan
  tomonlarni topish demakdir.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>leading coefficient</b><span>bosh koeffitsient (a)</span></li>
  <li><b>the AC method</b><span>AC usuli</span></li>
  <li><b>rewrite the middle term</b><span>oʻrtadagi hadni qayta yozish</span></li>
  <li><b>grouping</b><span>guruhlash</span></li>
  <li><b>factor pair</b><span>koʻpaytuvchi juftligi</span></li>
  <li><b>expand to check</b><span>tekshirish uchun ochish</span></li>
  <li><b>integers</b><span>butun sonlar</span></li>
  <li><b>dimensions</b><span>oʻlchamlar</span></li>
  <li><b>trial and error</b><span>taxmin qilib koʻrish</span></li>
  <li><b>systematic</b><span>tartibli, tizimli</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>a · c ni koʻpaytiring</b>, keyin koʻpaytmasi ac va yigʻindisi b boʻlgan
        juftlikni toping.</li>
    <li>Oʻrtadagi hadni ikkiga boʻlib, <b>guruhlang</b> — ikkinchi guruh manfiy
        boʻlsa, manfiy koʻpaytuvchi chiqaring.</li>
    <li>Javoblar qavs boʻlsa, ajratmang — <b>oching va solishtiring</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-33 — the quadratic formula
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-33: The Quadratic Formula and the Discriminant",
        "category": "math",
        "order": 33,
        "summary": (
            "Ajratib boʻlmaydigan kvadrat tenglama ham yechiladi: formula har doim "
            "ishlaydi. Ildiz ostidagi ifoda — diskriminant — javobning shaklini "
            "oldindan aytadi."
        ),
        "stories": ["The Man from Khwarazm"],
        "content": """
<h2>SAT-33: The Quadratic Formula and the Discriminant</h2>

<p>SAT-31 va SAT-32 dagi usullar butun sonli koʻpaytuvchilar mavjud boʻlgandagina
ishlaydi. Koʻp tenglamada ular yoʻq — masalan <em>x</em><sup>2</sup> − 4<em>x</em> + 1 = 0
ni hech qanday butun son juftligi ajratmaydi. Shunday hollar uchun
<mark>har doim ishlaydigan formula</mark> bor.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>formulani xotiradan yozasiz (u <em>reference sheet</em>da YOʻQ);</li>
    <li>a, b va c ni ishorasi bilan toʻgʻri qoʻyasiz;</li>
    <li>ildiz ostidagi ifodani — diskriminantni — alohida hisoblaysiz;</li>
    <li>javobni soddalashtirasiz (SAT-25) va tekshirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The quadratic formula</span>
  <span class="pe-chip pe-chip--s">x</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">(−b ± √(b<sup>2</sup> − 4ac))</span>
  <span class="pe-op">÷</span>
  <span class="pe-chip pe-chip--o">2a</span>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Bu formula ekrandagi <em>reference sheet</em> da <b>yoʻq</b>. U yerda faqat yuza, hajm,
  aylana va maxsus uchburchaklar bor. Formulani yod olish — SAT-5 dagi qiyalik formulasi
  kabi majburiy.
</div>

<h3>Uch qadam, har safar</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x<sup>2</sup> + 5x − 3 = 0</span>
    <span class="pm-solve__why">a = 2, b = 5, c = −3 — <b>ishorasi bilan</b></span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">b<sup>2</sup> − 4ac = 25 − 4(2)(−3) = 25 + 24 = 49</span>
    <span class="pm-solve__why">Diskriminantni alohida hisobladik; −4ac musbat chiqdi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = (−5 ± 7) ÷ 4</span>
    <span class="pm-solve__why">√49 = 7</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 1/2  yoki  x = −3</span>
    <span class="pm-solve__why">(−5 + 7) ÷ 4 = 1/2 va (−5 − 7) ÷ 4 = −3</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>x = 1/2: 2(0.25) + 2.5 − 3 = 0 ✓. x = −3: 18 − 15 − 3 = 0 ✓</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>c manfiy boʻlsa −4ac musbat boʻladi</b> va diskriminantni <u>kattalashtiradi</u>.
  Bu yerda ikki minus koʻpaytmasi plyus bergani uchun 25 + 24 chiqdi. Shu bitta ishorani
  eʼtiborsiz qoldirish — formuladagi eng koʻp uchraydigan xato.
</div>

<h3>Ildiz butun chiqmaganda</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x<sup>2</sup> − 4x + 1 = 0</span>
    <span class="pm-solve__why">a = 1, b = −4, c = 1</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">16 − 4 = 12</span>
    <span class="pm-solve__why">Diskriminant toʻliq kvadrat emas — demak ajratilmaydi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = (4 ± √12) ÷ 2 = (4 ± 2√3) ÷ 2</span>
    <span class="pm-solve__why">√12 = 2√3 (SAT-25)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 2 ± √3</span>
    <span class="pm-solve__why">Hamma hadni 2 ga qisqartirdik</span>
  </div>
</div>

<p>Eʼtibor bering: qisqartirishda <u>uchala</u> qismni boʻlish kerak — 4 ni ham,
2√3 ni ham. Faqat bittasini boʻlish javobni buzadi.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Diskriminantni <b>har doim alohida</b> hisoblang va yozib qoʻying. Shunda ishora
  xatosi bitta qatorda qoladi, va u toʻliq kvadratmi yoʻqmi degan savolga ham darrov
  javob berasiz.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>the solutions to the equation</b><span>tenglamaning yechimlari</span></li>
  <li><b>in the form a ± √b</b><span>a ± √b koʻrinishida</span></li>
  <li><b>the discriminant</b><span>diskriminant: b² − 4ac</span></li>
  <li><b>where a, b and c are constants</b><span>a, b va c — sonlar</span></li>
  <li><b>the positive solution</b><span>musbat yechim — ikkitasidan bittasi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>What are the solutions to 2<i>x</i><sup>2</sup> + 5<i>x</i> − 3 = 0?</p>
  </div>
  <ol class="ps-ch">
    <li><i>x</i> = −3 and <i>x</i> = 1/2</li>
    <li><i>x</i> = 3 and <i>x</i> = −1/2</li>
    <li><i>x</i> = −3 and <i>x</i> = 2</li>
    <li><i>x</i> = −5 and <i>x</i> = 3</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) x = −3 va x = 1/2</p>
      <p>Diskriminant: 25 + 24 = 49, demak x = (−5 ± 7) ÷ 4.</p>
      <p>Tekshiruv: x = −3 da 18 − 15 − 3 = 0 ✓. Javoblarni tenglamaga qoʻyish bu
      savolda formuladan ham tezroq.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">x = 3 and x = −1/2</span>
  <span class="ps-trap__why">Ikkala ildizning ishorasi almashtirilgan. Bitta son qoʻyib
  koʻring: x = 3 da 18 + 15 − 3 = 30, nol emas.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">90 s</span></p>
  <div class="ps-stem__q">
    <p>What are the solutions to <i>x</i><sup>2</sup> − 6<i>x</i> + 4 = 0?</p>
  </div>
  <ol class="ps-ch">
    <li><i>x</i> = 3 ± √5</li>
    <li><i>x</i> = 6 ± √5</li>
    <li><i>x</i> = 3 ± √20</li>
    <li><i>x</i> = −3 ± √5</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) x = 3 ± √5</p>
      <p>Diskriminant: 36 − 16 = 20. x = (6 ± √20) ÷ 2 = (6 ± 2√5) ÷ 2 = 3 ± √5.</p>
      <p><b>3 ± √20</b> — faqat 6 ni 2 ga boʻlgan javob: qisqartirishda <b>uchala</b>
      qism boʻlinadi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">x = 3 ± √20</span>
  <span class="ps-trap__why">Faqat 6 ni 2 ga boʻlgan javob — ildiz qismi
  qisqartirilmagan. Boʻlish kasrning <b>butun suratiga</b> qoʻllanadi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Javoblar son boʻlsa, formulani umuman ishlatmasangiz ham boʻladi:</p>
  <ol>
    <li>Javobdagi bitta sonni tenglamaga qoʻying.</li>
    <li>Nol chiqsa — u ildiz; chiqmasa — variant oʻchadi.</li>
    <li>Ikkala soni ham nol beradigan variant — javob.</li>
  </ol>
  <p>Javoblar ildizli boʻlsa, kalkulyatorda taxminiy qiymatini hisoblang: 3 + √5 ≈ 5.24,
  va uni tenglamaga qoʻying.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">2x<sup>2</sup> + 5x − 3 = 0 uchun b<sup>2</sup> − 4ac = 25 − 24 = 1</p>
  <p class="pe-good">25 + 24 = 49</p>
  <p class="pe-fix__why">c = −3 manfiy, demak −4ac = −4(2)(−3) = <b>+24</b>. Ikki minus
  plyus beradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">(4 ± 2√3) ÷ 2 = 2 ± 2√3</p>
  <p class="pe-good">2 ± √3</p>
  <p class="pe-fix__why">Boʻlish <b>ikkala</b> hadga qoʻllanadi: 4 ÷ 2 = 2 va
  2√3 ÷ 2 = √3.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Formulani yozishdan oldin tenglamani <b>standart koʻrinishga</b> keltiring:
  x<sup>2</sup> + 5x = 3 emas, x<sup>2</sup> + 5x − 3 = 0. Aks holda c ning qiymati
  notoʻgʻri olinadi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Formula <b>har doim</b> ishlaydi — ajratiladigan tenglamalarda ham. Vaqtingiz boʻlmasa yoki juftlikni topa olmasangiz, ikkilanmasdan formulaga oʻting: u bir oz sekinroq, lekin hech qachon adashtirmaydi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Solve using the formula: <i>x</i><sup>2</sup> + 3<i>x</i> + 2 = 0</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> = −1 yoki −2 — diskriminant 9 − 8 = 1, demak
  x = (−3 ± 1) ÷ 2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  What is the discriminant of 3<i>x</i><sup>2</sup> + 2<i>x</i> − 1 = 0?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">16 — 4 − 4(3)(−1) = 4 + 12 = 16. Toʻliq kvadrat, demak
  tenglama ajratiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Solve: 3<i>x</i><sup>2</sup> + 2<i>x</i> − 1 = 0</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> = 1/3 yoki −1 — x = (−2 ± 4) ÷ 6.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Solve: <i>x</i><sup>2</sup> + 4<i>x</i> + 2 = 0</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> = −2 ± √2 — diskriminant 16 − 8 = 8, va
  (−4 ± 2√2) ÷ 2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Solve: <i>x</i><sup>2</sup> − 2<i>x</i> − 1 = 0</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> = 1 ± √2 — diskriminant 4 + 4 = 8, va
  (2 ± 2√2) ÷ 2.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>quadratic formula</b><span>kvadrat tenglama formulasi</span></li>
  <li><b>discriminant</b><span>diskriminant (b² − 4ac)</span></li>
  <li><b>standard form</b><span>standart koʻrinish (bir tomoni nol)</span></li>
  <li><b>plus or minus</b><span>plyus-minus (±)</span></li>
  <li><b>simplify the radical</b><span>ildizni soddalashtirish</span></li>
  <li><b>substitute</b><span>oʻrniga qoʻymoq</span></li>
  <li><b>solutions / roots</b><span>yechimlar / ildizlar</span></li>
  <li><b>perfect square</b><span>toʻliq kvadrat</span></li>
  <li><b>reference sheet</b><span>formula varagʻi (bu formula unda YOʻQ)</span></li>
  <li><b>exact form</b><span>aniq koʻrinish (ildiz bilan)</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Formulani <b>yod oling</b> — u formula varagʻida yoʻq — va tenglamani avval
        nolga keltiring.</li>
    <li>Diskriminantni <b>alohida</b> hisoblang; c manfiy boʻlsa −4ac musbat
        boʻladi.</li>
    <li>Qisqartirishda <b>uchala qism</b> boʻlinadi: (4 ± 2√3) ÷ 2 = 2 ± √3.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-34 — the discriminant: how many roots
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-34: Determining Number and Type of Roots using the Discriminant",
        "category": "math",
        "order": 34,
        "summary": (
            "b² − 4ac ni hisoblab, tenglamani yechmasdan turib ildizlar sonini "
            "ayting: musbat — ikkita, nol — bitta, manfiy — haqiqiy ildiz yoʻq."
        ),
        "stories": ["Will It Reach the Window?"],
        "content": """
<h2>SAT-34: Determining Number and Type of Roots using the Discriminant</h2>

<p>SAT-33 da diskriminantni formulaning bir qismi sifatida hisobladik. Endi u mustaqil
qurol boʻladi: <mark>tenglamani yechmasdan turib nechta ildizi borligini aytish
mumkin</mark>. SAT bu savolni juda koʻp beradi, chunki javob bir necha soniyada
topiladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>diskriminantning uchta holatini ajratasiz;</li>
    <li>uni parabolaning grafigi bilan bogʻlaysiz;</li>
    <li>toʻliq kvadrat ekanini koʻrib, ajratiladimi-yoʻqmi deb aytasiz;</li>
    <li>«exactly one solution» turidagi <em>k</em> ni topish savollarini yechasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The discriminant</span>
  <span class="pe-chip pe-chip--s">D = b<sup>2</sup> − 4ac</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">nechta ildiz</span>
</div>

<h3>Uchta holat — hammasi shu</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Diskriminant</th><th>Ildizlar</th><th>Grafik (parabola)</th><th>Misol</th></tr>
  <tr><td>D &gt; 0</td><td class="pm-word__sym">ikkita haqiqiy</td>
      <td>x oʻqini <b>ikki nuqtada</b> kesadi</td><td>x<sup>2</sup> − 5x + 6</td></tr>
  <tr><td>D = 0</td><td class="pm-word__sym">bitta (takrorlanuvchi)</td>
      <td>x oʻqiga <b>urinadi</b></td><td>x<sup>2</sup> − 6x + 9</td></tr>
  <tr><td>D &lt; 0</td><td class="pm-word__sym">haqiqiy ildiz yoʻq</td>
      <td>x oʻqini <b>kesmaydi</b></td><td>x<sup>2</sup> + 4x + 5</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Sababi oddiy: formulada <b>√D</b> turadi. D musbat boʻlsa ildiz chiqadi va ± ikkita
  javob beradi; D = 0 boʻlsa ± hech narsani oʻzgartirmaydi va bitta javob qoladi;
  D manfiy boʻlsa manfiy sondan kvadrat ildiz chiqmaydi — haqiqiy yechim yoʻq.
</div>

<h3>Uchta misol</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x<sup>2</sup> + 4x + 5 = 0  →  16 − 20 = −4</span>
    <span class="pm-solve__why">D &lt; 0 → haqiqiy yechim yoʻq</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x<sup>2</sup> − 6x + 9 = 0  →  36 − 36 = 0</span>
    <span class="pm-solve__why">D = 0 → bitta yechim (x = 3)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2x<sup>2</sup> + 3x − 2 = 0  →  9 + 16 = 25</span>
    <span class="pm-solve__why">D &gt; 0 va 25 toʻliq kvadrat → ikkita <b>ratsional</b> ildiz</span>
  </div>
</div>

<h3>Toʻliq kvadrat — qoʻshimcha maʼlumot</h3>

<p>Diskriminant faqat <u>nechta</u> emas, <u>qanday</u> ildiz ekanini ham aytadi:</p>

<ul>
  <li><b>D toʻliq kvadrat</b> (25, 49, 4…) → ildizlar kasr yoki butun son, va tenglama
      butun sonlar bilan <b>ajratiladi</b>;</li>
  <li><b>D musbat, lekin toʻliq kvadrat emas</b> (12, 20, 8…) → ildizlarda √ qoladi,
      demak ajratishga urinmang — formulani ishlating.</li>
</ul>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Ajratishga urinishdan oldin diskriminantni hisoblash koʻpincha vaqtni tejaydi.
  D = 20 chiqsa, siz butun sonli juftlikni behuda izlayotganingizni bilib olasiz.
</div>

<h3><em>k</em> ni topish — SAT'ning sevimli savoli</h3>

<p>«exactly one solution» iborasi bevosita <b>D = 0</b> degani. Bu savolni koʻrgan
zahoti diskriminantni yozing va nolga tenglashtiring.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x<sup>2</sup> + kx + 25 = 0, aynan bitta yechim</span>
    <span class="pm-solve__why">a = 1, b = k, c = 25</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">k<sup>2</sup> − 100 = 0</span>
    <span class="pm-solve__why">D = 0 deb yozdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">k = 10  yoki  k = −10</span>
    <span class="pm-solve__why">Ikkala ishora ham ishlaydi — savol qaysinisini soʻrayotganini oʻqing</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  k<sup>2</sup> = 100 dan <b>ikkita</b> javob chiqadi. SAT koʻpincha «the positive value
  of k» deb soʻraydi — bu holda 10. Faqat bittasini yozib qoʻyish keng tarqalgan xato.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>how many real solutions</b><span>nechta haqiqiy yechim</span></li>
  <li><b>exactly one solution</b><span>aynan bitta yechim → D = 0</span></li>
  <li><b>no real solutions</b><span>haqiqiy yechim yoʻq → D &lt; 0</span></li>
  <li><b>two distinct real solutions</b><span>ikkita turli haqiqiy yechim → D &gt; 0</span></li>
  <li><b>the positive value of k</b><span>k ning musbat qiymati</span></li>
  <li><b>x-intercepts of the graph</b><span>grafikning x oʻqi bilan kesishishi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>How many real solutions does 3<i>x</i><sup>2</sup> − 2<i>x</i> + 5 = 0 have?</p>
  </div>
  <ol class="ps-ch">
    <li>Zero</li>
    <li>One</li>
    <li>Two</li>
    <li>Infinitely many</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) Zero</p>
      <p>D = (−2)<sup>2</sup> − 4(3)(5) = 4 − 60 = −56 &lt; 0 → haqiqiy ildiz yoʻq.</p>
      <p>Grafik tilida: bu parabola x oʻqidan butunlay yuqorida turadi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">Two</span>
  <span class="ps-trap__why">(−2)<sup>2</sup> ni −4 deb hisoblagan javob: 4 va 60 ning
  ishorasi chalkashsa D musbat chiqib qoladi. Kvadrat har doim musbat.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>In the equation <i>x</i><sup>2</sup> + <i>kx</i> + 25 = 0, <i>k</i> is a constant.
    If the equation has exactly one real solution, what is the positive value of
    <i>k</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>5</li>
    <li>10</li>
    <li>25</li>
    <li>50</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 10</p>
      <p>«Exactly one solution» → D = 0 → k<sup>2</sup> − 4(1)(25) = 0 →
      k<sup>2</sup> = 100 → k = ±10.</p>
      <p>Tekshiruv: x<sup>2</sup> + 10x + 25 = (x + 5)<sup>2</sup> — toʻliq kvadrat,
      bitta ildiz x = −5 ✓ (SAT-30)</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">5</span>
  <span class="ps-trap__why">√25 = 5 deb toʻxtab qolgan javob. Kerakli tenglama
  k<sup>2</sup> = 4ac = 100 edi, k<sup>2</sup> = 25 emas.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Uchta iborani uchta amalga bogʻlab qoʻying — savolni oʻqishning oʻzi javobni
  boshlaydi:</p>
  <ol>
    <li>«exactly one» / «only one» → <b>D = 0</b> deb yozing;</li>
    <li>«no real solutions» → <b>D &lt; 0</b> tengsizligini yozing;</li>
    <li>«two distinct» / «two x-intercepts» → <b>D &gt; 0</b>.</li>
  </ol>
  <p>Ildizlarni topishga umuman hojat yoʻq — bu savollar yechim emas, <b>son</b>
  soʻraydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">3x<sup>2</sup> − 2x + 5 → D = −2<sup>2</sup> − 60 = −64</p>
  <p class="pe-good">D = (−2)<sup>2</sup> − 60 = 4 − 60 = −56</p>
  <p class="pe-fix__why">b ni kvadratga koʻtarishda qavs qoʻying: (−2)² = +4.
  (Bu savolda javob oʻzgarmadi, lekin koʻp savolda oʻzgaradi.)</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">D = 0 → yechim yoʻq</p>
  <p class="pe-good">D = 0 → aynan <b>bitta</b> yechim</p>
  <p class="pe-fix__why">Yechim yoʻq boʻlishi uchun D <b>manfiy</b> boʻlishi kerak.
  D = 0 da parabola x oʻqiga urinadi — bir marta tegadi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Diskriminantni hisoblashdan oldin tenglama <b>standart koʻrinishda</b>ekaniga ishonch
  hosil qiling. x<sup>2</sup> = 4x − 5 koʻrinishida a, b, c ni oʻqib boʻlmaydi; avval
  x<sup>2</sup> − 4x + 5 = 0 qilib yozing.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Diskriminant tengsizlik bilan ham soʻralishi mumkin: «for what values of k does the equation have two real solutions» — bunda D &gt; 0 tengsizligini yechasiz. Amal oʻsha-oʻsha, faqat tenglik oʻrniga tengsizlik yoziladi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  How many real solutions does <i>x</i><sup>2</sup> − 5<i>x</i> + 7 = 0 have?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Bittasi ham yoʻq — D = 25 − 28 = −3 &lt; 0.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  How many real solutions does 4<i>x</i><sup>2</sup> − 12<i>x</i> + 9 = 0 have?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Bitta — D = 144 − 144 = 0. Bu (2x − 3)<sup>2</sup>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Is <i>x</i><sup>2</sup> + 2<i>x</i> − 6 = 0 factorable with integers?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — D = 4 + 24 = 28, toʻliq kvadrat emas. Formulani
  ishlating.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  For what value of <i>k</i> does <i>x</i><sup>2</sup> + 6<i>x</i> + <i>k</i> = 0 have
  exactly one solution?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>k</i> = 9 — D = 36 − 4k = 0. Natija (x + 3)<sup>2</sup>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  The graph of a quadratic does not cross the <i>x</i>-axis. What can you say about its
  discriminant?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">U manfiy (D &lt; 0) — x oʻqi bilan kesishish nuqtasi
  yoʻq.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>discriminant</b><span>diskriminant</span></li>
  <li><b>real solutions</b><span>haqiqiy yechimlar</span></li>
  <li><b>distinct</b><span>turli, har xil</span></li>
  <li><b>repeated root</b><span>takrorlanuvchi ildiz</span></li>
  <li><b>x-intercept</b><span>x oʻqi bilan kesishish nuqtasi</span></li>
  <li><b>tangent to the x-axis</b><span>x oʻqiga urinuvchi</span></li>
  <li><b>perfect square</b><span>toʻliq kvadrat</span></li>
  <li><b>rational roots</b><span>ratsional ildizlar</span></li>
  <li><b>constant k</b><span>k oʻzgarmas soni</span></li>
  <li><b>factorable</b><span>ajratiladigan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>D &gt; 0</b> ikkita, <b>D = 0</b> bitta, <b>D &lt; 0</b> hech qanday haqiqiy
        ildiz yoʻq.</li>
    <li>«exactly one solution» degan ibora — bu <b>D = 0</b> ning inglizchasi.</li>
    <li>D toʻliq kvadrat boʻlsa tenglama <b>ajratiladi</b>; boʻlmasa formulani
        ishlating.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-35 — vertex form
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-35: Vertex Form of a Quadratic",
        "category": "math",
        "order": 35,
        "summary": (
            "y = a(x − h)² + k koʻrinishi uchni (h, k) toʻgʻridan-toʻgʻri koʻrsatadi. "
            "Standart koʻrinishdan uchni x = −b ÷ (2a) formulasi bilan toping."
        ),
        "stories": ["The Fountain in the Square"],
        "content": """
<h2>SAT-35: Vertex Form of a Quadratic</h2>

<p>Bir xil parabolani uch xil yozish mumkin, va <mark>har bir koʻrinish boshqa narsani
darrov koʻrsatadi</mark>. Ajratilgan koʻrinish nollarni beradi (SAT-31), standart
koʻrinish y oʻqi bilan kesishishni beradi, uchi shakli esa parabolaning eng yuqori yoki
eng past nuqtasini beradi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>y = a(x − h)² + k dan uchni bir qarashda oʻqiysiz;</li>
    <li>h ning ishorasi bilan adashmaysiz;</li>
    <li>x = −b ÷ (2a) bilan standart koʻrinishdan uchni topasiz;</li>
    <li>a ning ishorasidan maksimummi yoki minimummi ekanini aytasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Vertex form</span>
  <span class="pe-chip pe-chip--s">y = a(x − h)<sup>2</sup> + k</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">uchi = (h, k)</span>
</div>

<h3>Ishora — bu darsdagi asosiy tuzoq</h3>

<p>Formulada <b>minus</b> yozilgan: (x − h). Shuning uchun qavs ichidagi son bilan
uchning koordinatasi <u>qarama-qarshi ishorada</u> boʻladi.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Tenglama</th><th>h</th><th>k</th><th>Uchi</th></tr>
  <tr><td>y = (x − 3)<sup>2</sup> + 2</td><td>3</td><td>2</td><td class="pm-word__sym">(3, 2)</td></tr>
  <tr><td>y = (x + 4)<sup>2</sup> − 1</td><td>−4</td><td>−1</td><td class="pm-word__sym">(−4, −1)</td></tr>
  <tr><td>y = 2(x + 1)<sup>2</sup> + 5</td><td>−1</td><td>5</td><td class="pm-word__sym">(−1, 5)</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  (x <b>+</b> 4)<sup>2</sup> ni (x <b>−</b> (−4))<sup>2</sup> deb oʻqing — shunda h = −4
  ekani oʻz-oʻzidan koʻrinadi. <b>k</b> esa qavsdan tashqarida, ishorasi
  oʻzgarmaydi.
</div>

<h3>a nima qiladi</h3>

<ul>
  <li><b>a &gt; 0</b> → parabola yuqoriga ochiladi, uchi eng <b>past</b> nuqta →
      <em>minimum</em>;</li>
  <li><b>a &lt; 0</b> → pastga ochiladi, uchi eng <b>yuqori</b> nuqta →
      <em>maximum</em>;</li>
  <li>|a| katta boʻlsa parabola torroq, kichik boʻlsa kengroq boʻladi.</li>
</ul>

<p>Demak y = −2(x − 1)<sup>2</sup> + 8 ning <b>maksimal qiymati 8</b>, va u x = 1 da
erishiladi. Savol «maximum value» deb soʻrasa javob 8; «where does it occur» deb
soʻrasa javob 1. Ikkalasi boshqa-boshqa son.</p>

<h3>Standart koʻrinishdan uchni topish</h3>

<div class="pe-formula">
  <span class="pe-formula__label">Axis of symmetry</span>
  <span class="pe-chip pe-chip--s">x</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">−b ÷ (2a)</span>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">y = x<sup>2</sup> − 6x + 5</span>
    <span class="pm-solve__why">a = 1, b = −6</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = −(−6) ÷ 2 = 3</span>
    <span class="pm-solve__why">Uchning x koordinatasi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">y = 9 − 18 + 5 = −4</span>
    <span class="pm-solve__why">x = 3 ni tenglamaga qoʻydik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Uchi (3, −4), yaʼni y = (x − 3)<sup>2</sup> − 4</span>
    <span class="pm-solve__why">Tekshiruv: (x−3)² − 4 = x² − 6x + 9 − 4 ✓</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Nollari maʼlum boʻlsa, undan ham tez yoʻl bor: uch <b>ikki nolning oʻrtasida</b>
  turadi. x = 1 va x = 5 boʻlsa, uchning x koordinatasi (1 + 5) ÷ 2 = 3. Parabola
  simmetrik shakl.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>the vertex of the parabola</b><span>parabolaning uchi</span></li>
  <li><b>the minimum value of the function</b><span>funksiyaning eng kichik qiymati (k)</span></li>
  <li><b>the maximum value</b><span>eng katta qiymat</span></li>
  <li><b>the axis of symmetry</b><span>simmetriya oʻqi (x = h)</span></li>
  <li><b>displays the vertex as constants</b><span>uchni son sifatida koʻrsatadi</span></li>
  <li><b>at what value of x does it occur</b><span>x ning qaysi qiymatida sodir boʻladi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">40 s</span></p>
  <div class="ps-stem__q">
    <p>What is the vertex of the parabola <i>y</i> = (<i>x</i> + 4)<sup>2</sup> − 1?</p>
  </div>
  <ol class="ps-ch">
    <li>(4, −1)</li>
    <li>(−4, −1)</li>
    <li>(−4, 1)</li>
    <li>(4, 1)</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) (−4, −1)</p>
      <p>(x + 4)<sup>2</sup> = (x − (−4))<sup>2</sup>, demak h = −4. k = −1 qavsdan
      tashqarida turibdi va oʻzgarmaydi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">(4, −1)</span>
  <span class="ps-trap__why">Qavs ichidagi son shundoq koʻchirilgan. h ning ishorasi
  <b>har doim</b> almashadi; k niki hech qachon almashmaydi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">70 s</span></p>
  <div class="ps-stem__q">
    <p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = <i>x</i><sup>2</sup>
    − 8<i>x</i> + 11. What is the minimum value of <i>f</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>−5</li>
    <li>4</li>
    <li>11</li>
    <li>−4</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) −5</p>
      <p>x = −(−8) ÷ 2 = 4, keyin f(4) = 16 − 32 + 11 = −5.</p>
      <p>Yaʼni f(x) = (x − 4)<sup>2</sup> − 5, uchi (4, −5) ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">4</span>
  <span class="ps-trap__why">Bu uchning <b>x</b> koordinatasi — qayerda sodir boʻlishi.
  «Minimum value» esa <b>y</b> ni soʻraydi: −5.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>«Which equation displays the vertex as constants?» turidagi savolda hisoblamang —
  <b>javoblarni oching</b>:</p>
  <ol>
    <li>Har bir variantdagi qavsni ochib, asl tenglama bilan solishtiring.</li>
    <li>Yoki bitta son qoʻying: x = 0 da ikkala tomon bir xil qiymat berishi kerak.</li>
    <li>Uch soʻralganda esa x = −b ÷ (2a) — ikki soniyalik ish.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">y = (x + 4)<sup>2</sup> − 1 → uchi (4, −1)</p>
  <p class="pe-good">Uchi (−4, −1)</p>
  <p class="pe-fix__why">Formulada (x − h) turadi, demak qavsdagi +4 h = −4 degani.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Minimum value of x<sup>2</sup> − 8x + 11 is 4</p>
  <p class="pe-good">Minimum qiymat −5, va u x = 4 da erishiladi</p>
  <p class="pe-fix__why">«Value» — funksiyaning qiymati, yaʼni y. Topilgan x ni
  tenglamaga qaytarib qoʻying.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  a manfiy boʻlsa uchi <b>maksimum</b> boʻladi, minimum emas — va bunday funksiyaning
  minimal qiymati umuman yoʻq. Savolni oʻqiyotganda a ning ishorasiga eʼtibor bering.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Uch koʻrinishni bir jadvalda saqlang: <b>ajratilgan</b> — nollar koʻrinadi;
  <b>standart</b> — y oʻqidagi nuqta (c) koʻrinadi; <b>uchi shakli</b> — eng yuqori
  yoki eng past nuqta koʻrinadi. SAT «which form displays…» deb aynan shuni soʻraydi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Uchi shakliga oʻtish uchun <b>toʻliq kvadratga toʻldirish</b> usuli ham bor, lekin SAT uchun x = −b ÷ (2a) deyarli har doim tezroq: bitta boʻlish va bitta qoʻyish, xolos.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  What is the vertex of <i>y</i> = (<i>x</i> − 5)<sup>2</sup> − 3?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(5, −3).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  What is the vertex of <i>y</i> = (<i>x</i> + 2)<sup>2</sup> + 7?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(−2, 7) — qavsdagi ishora almashadi, tashqaridagisi
  yoʻq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Find the vertex of <i>y</i> = <i>x</i><sup>2</sup> + 4<i>x</i> + 1.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(−2, −3) — x = −4 ÷ 2 = −2, keyin y = 4 − 8 + 1 = −3.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  What is the minimum value of <i>y</i> = 2(<i>x</i> − 3)<sup>2</sup> + 5?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">5 — kvadrat hech qachon manfiy boʻlmaydi, demak eng kichik
  qiymat x = 3 da.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A ball's height is <i>h</i> = −5(<i>t</i> − 2)<sup>2</sup> + 20. What is its greatest
  height, and when does it happen?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">20 metr, 2 soniyada — a manfiy, demak uchi maksimum.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>vertex</b><span>uch (parabolaning burilish nuqtasi)</span></li>
  <li><b>vertex form</b><span>uchi shakli</span></li>
  <li><b>parabola</b><span>parabola</span></li>
  <li><b>axis of symmetry</b><span>simmetriya oʻqi</span></li>
  <li><b>minimum / maximum value</b><span>eng kichik / eng katta qiymat</span></li>
  <li><b>opens upward</b><span>yuqoriga ochiladi</span></li>
  <li><b>displays as constants</b><span>son sifatida koʻrsatadi</span></li>
  <li><b>equivalent forms</b><span>teng kuchli koʻrinishlar</span></li>
  <li><b>occurs at</b><span>… da sodir boʻladi</span></li>
  <li><b>coordinates</b><span>koordinatalar</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>y = a(x − h)<sup>2</sup> + k da uch <b>(h, k)</b>, va <b>h ning ishorasi
        almashadi</b>.</li>
    <li>Standart koʻrinishdan: <b>x = −b ÷ (2a)</b>, keyin uni qaytarib qoʻyib y ni
        toping.</li>
    <li>a &gt; 0 → minimum, a &lt; 0 → maksimum; «value» y ni, «occurs at» x ni
        soʻraydi.</li>
  </ul>
</div>
""",
    },
]
