# -*- coding: utf-8 -*-
"""Prime SAT Math — lessons 76–80 (Blok D ning yakuni: aylana).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_SAT.md
Lesson list: tutorial/management/commands/toc_prime_sat_math.txt

⚠️ SARLAVHALAR BAZADAN OLINGAN, aynan.

⚠️ BLOK D QOIDASI: har bir darsda formula varagʻida NIMA BOR va NIMA YOʻQ.
   Bu batchda:
     SAT-77 — aylanada 360 daraja va 2π radian BOR; yoy uzunligi formulasi YOʻQ.
     SAT-78 — aylana yuzasi πr² BOR; sektor formulasi YOʻQ.
     SAT-76, SAT-79, SAT-80 — hech biri varaqda YOʻQ.

⚠️ Chizmalar inline SVG va gate ularni oʻlchaydi.

  • SAT-76 — sin(x) = cos(90 − x) va Pifagor ayniyati.
  • SAT-77 — radian va daraja; yoy uzunligi ulush sifatida.
  • SAT-78 — sektor yuzasi: aynan oʻsha ulush.
  • SAT-79 — aylana tenglamasi va markaz/radius.
  • SAT-80 — toʻliq kvadratga toʻldirib markazni topish.
  • ⛔ Blok E taktikalari (SAT-81 dan) YOʻQ.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_sat_76_80.py \\
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
    # SAT-76 — trig identities
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-76: Trigonometric Identities — sin(x) = cos(90° − x)",
        "category": "math",
        "order": 76,
        "summary": (
            "Toʻgʻri burchakli uchburchakda ikki oʻtkir burchak 90 ga toʻldiradi — "
            "va shundan birining sinusi ikkinchisining kosinusiga teng."
        ),
        "stories":  ["Two Ways to Say the Same Roof"],
        "content": """
<h2>SAT-76: Trigonometric Identities — sin(x) = cos(90° − x)</h2>

<p>SAT-75 ning oxirida bir narsa koʻrindi: 3-4-5 uchburchagida bitta
burchakning sinusi ikkinchisining kosinusiga teng chiqdi. Bu tasodif emas —
<mark>bu ayniyat, va uni chizmadan bir qatorda koʻrish mumkin</mark>.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Formula varagʻi</span>
  <p><b>VARAQDA YOʻQ:</b> hech qanday trigonometrik ayniyat. Lekin bu
  darsdagi ikkala ayniyat ham <b>chiqarib olinadi</b> — biri burchaklar
  yigʻindisidan, ikkinchisi Pifagordan.</p>
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>toʻldiruvchi burchak ayniyatini yozasiz;</li>
    <li>uni chizmadan chiqarib olasiz, yodlamasdan;</li>
    <li>sin² + cos² = 1 ni Pifagordan olasiz;</li>
    <li>SAT'ning «if sin A = …, what is cos B» savolini bir qadamda
        yechasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The identity</span>
  <span class="pe-chip pe-chip--v">sin(x)</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">cos(90° − x)</span>
</div>

<h3>Nima uchun toʻgʻri</h3>

<p>Toʻgʻri burchakli uchburchakda ikki oʻtkir burchak 90 ga toʻldiradi
(SAT-66). Endi bitta tomonga qarang: u <b>bir burchakka qarshi</b>, ikkinchi
burchakka esa <b>yondosh</b>. Gipotenuza ikkalasi uchun ham oʻsha-oʻsha.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3-4-5 uchburchagi, burchaklar A va B</span>
    <span class="pm-solve__why">A + B = 90</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">sin A = 3 ÷ 5</span>
    <span class="pm-solve__why">3 — A ga qarshi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">cos B = 3 ÷ 5</span>
    <span class="pm-solve__why">Oʻsha 3 — B ga yondosh; kasr aynan bir xil</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ayniyatni yodlashning hojati yoʻq. <b>Uchburchak chizing</b>, ikki oʻtkir
  burchakni belgilang va bitta tomonga ikki tomondan qarang. «Qarshi» va
  «yondosh» soʻzlari oʻrin almashadi, kasr esa oʻzgarmaydi.
</div>

<h3>Ikkinchi ayniyat</h3>

<p>Pifagor teoremasini gipotenuzaning kvadratiga boʻling: qarshi va yondosh
tomonlarning gipotenuzaga nisbatlari — bu sinus va kosinus. Demak
<b>sin² + cos² = 1</b>, har doim.</p>

<div class="pm-check">
  <p class="pm-check__t">3-4-5 da tekshiramiz</p>
  <p>(3 ÷ 5)² + (4 ÷ 5)² = 9/25 + 16/25 = 25/25 = 1 ✓</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Bu ayniyat <b>bitta burchakning</b> sinusi va kosinusiga tegishli. Bir
  burchakning sinusi bilan boshqasining kosinusini qoʻshib boʻlmaydi — u
  1 bermaydi.
</div>

<h3>SAT savolining shakli</h3>

<p>Savol deyarli har doim shunday keladi: «If sin A = 0.6 and A + B = 90,
what is cos B?» Javob toʻgʻridan-toʻgʻri 0.6 — hech narsa hisoblanmaydi.
Bu savol atigi 10 soniya oladi, agar ayniyat tanilsa.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Savolda <b>ikki burchakning yigʻindisi 90</b> ekani aytilgan boʻlsa, bu
  ayniyat kerakligining belgisi. «In a right triangle» degan ibora ham
  shuni bildiradi — chunki oʻtkir burchaklar avtomatik 90 ga toʻldiradi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>complementary angles</b><span>yigʻindisi 90 boʻlgan burchaklar</span></li>
  <li><b>if x + y = 90</b><span>x va y toʻldiruvchi boʻlsa</span></li>
  <li><b>in terms of x</b><span>x orqali ifodalang</span></li>
  <li><b>which is equivalent to</b><span>qaysi biri teng kuchli</span></li>
  <li><b>the acute angles of a right triangle</b><span>toʻgʻri burchakli uchburchakning oʻtkir burchaklari</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">35 s</span></p>
  <div class="ps-stem__q">
    <p>If sin <i>A</i> = 0.6 and <i>A</i> + <i>B</i> = 90°, what is cos
    <i>B</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>0.6</li>
    <li>0.8</li>
    <li>0.4</li>
    <li>1.6</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 0.6</p>
      <p>Ayniyat boʻyicha sin A = cos(90 − A) = cos B.</p>
      <p>Hech narsa hisoblanmaydi — bu 10 soniyalik savol.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">0.8</span>
  <span class="ps-trap__why">Bu <b>cos A</b> — oʻsha burchakning kosinusi
  (sin² + cos² = 1 dan). Savol esa B burchagini soʻragan.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">55 s</span></p>
  <div class="ps-stem__q">
    <p>In a right triangle, cos <i>A</i> = 5/13. What is sin <i>A</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>12/13</li>
    <li>5/13</li>
    <li>13/5</li>
    <li>8/13</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 12/13</p>
      <p>Yondosh 5, gipotenuza 13, demak qarshi tomon 12 (5-12-13 uchligi,
      SAT-70).</p>
      <p>Yoki ayniyat bilan: sin² = 1 − 25/169 = 144/169.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">8/13</span>
  <span class="ps-trap__why">13 − 5 = 8 deb olingan. Uchinchi tomon
  <b>ayirish</b> bilan emas, Pifagor bilan topiladi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Savolni koʻrgach ikki narsani ajrating:</p>
  <ol>
    <li><b>Ikki burchak</b> haqidami? → sin(x) = cos(90 − x);</li>
    <li><b>Bitta burchak</b> haqidami? → sin² + cos² = 1, yoki
        uchburchakni chizing;</li>
    <li>Ikkinchi holda uchlikni tanish koʻpincha tezroq.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">sin A = 0.6 → cos B = 0.8</p>
  <p class="pe-good">cos B = 0.6</p>
  <p class="pe-fix__why">0.8 — bu cos A, boshqa burchakniki emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">cos A = 5/13 → sin A = 8/13</p>
  <p class="pe-good">12/13</p>
  <p class="pe-fix__why">Uchinchi tomon 13 − 5 emas; u √(169 − 25).</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ayniyat tangens uchun ham ishlaydi, faqat boshqacha: bir burchakning
  tangensi ikkinchisining tangensiga <b>teskari</b> boʻladi. 3-4-5 da bir
  burchak uchun 3/4, ikkinchisi uchun 4/3.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Maxsus burchaklarda</b> ayniyat oʻz-oʻzidan koʻrinadi: sin 30° va
  cos 60° ikkalasi ham 1/2; sin 45° va cos 45° ikkalasi ham √2/2 — chunki
  45 oʻzining toʻldiruvchisi.
</div>

<h3>Tangens ham juftlashadi</h3>

<p>Sinus va kosinus oʻrin almashadi. Tangens esa <b>agʻdariladi</b>:
qarshi va yondosh joyini almashtirsa, kasr teskarisiga aylanadi.</p>

<div class="pe-formula">
  <span class="pe-formula__label">Tangent pair</span>
  <span class="pe-chip pe-chip--v">tan(90° − x)</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">1 / tan(x)</span>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3-4-5 uchburchagi, burchaklar A va B</span>
    <span class="pm-solve__why">A + B = 90</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">tan A = 3 ÷ 4</span>
    <span class="pm-solve__why">qarshi ÷ yondosh</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">tan B = 4 ÷ 3</span>
    <span class="pm-solve__why">Oʻsha ikki tomon, teskari tartibda</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tez tekshiruv</p>
  <p>tan 45° = 1, chunki 45 oʻzining toʻldiruvchisi va 1 ning teskarisi
  yana 1. Bu ayniyatning eng qisqa isboti.</p>
</div>

<div class="ps-desmos">
  <span class="ps-desmos__t">Desmos</span>
  <p>Ayniyatni bir marta oʻz koʻzingiz bilan koʻring: <code>sin(30)</code>
  va <code>cos(60)</code> ni kiriting — ikkalasi ham 0.5 beradi.
  <b>Muhim:</b> avval Desmosni <i>degrees</i> rejimiga oʻtkazing
  (sozlamalar tugmasi), aks holda u 30 ni radian deb oʻqiydi va
  butunlay boshqa son chiqaradi.</p>
</div>

<h3>Chegaraviy qiymatlar</h3>

<p>Uchburchak chizib boʻlmaydigan ikki burchak — 0° va 90° — SAT'da
baʼzan javob variantlarini tekshirishga yordam beradi: sin 0° = 0,
cos 0° = 1, sin 90° = 1, cos 90° = 0. Ayniyat bu yerda ham ishlaydi:
sin 0° = cos 90° ✓</p>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  If sin 25° = 0.42, what is cos 65°?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">0.42 — 25 va 65 toʻldiruvchi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  If cos <i>x</i> = 0.28, what is sin(90° − <i>x</i>)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">0.28 — ayniyat teskari yoʻnalishda ham
  ishlaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  In a right triangle, sin <i>A</i> = 8/17. What is cos <i>A</i>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">15/17 — 8-15-17 uchligi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Verify that sin² + cos² = 1 for the 5-12-13 triangle.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">25/169 + 144/169 = 169/169 = 1 ✓</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Why is sin 45° equal to cos 45°?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">45 oʻzining toʻldiruvchisi: 90 − 45 = 45.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>identity</b><span>ayniyat</span></li>
  <li><b>complementary</b><span>toʻldiruvchi (yigʻindisi 90)</span></li>
  <li><b>equivalent to</b><span>teng kuchli</span></li>
  <li><b>in terms of</b><span>… orqali</span></li>
  <li><b>acute angles</b><span>oʻtkir burchaklar</span></li>
  <li><b>reciprocal</b><span>teskari (nisbat)</span></li>
  <li><b>holds for all x</b><span>barcha x uchun oʻrinli</span></li>
  <li><b>Pythagorean identity</b><span>Pifagor ayniyati</span></li>
  <li><b>substitute</b><span>oʻrniga qoʻymoq</span></li>
  <li><b>right triangle</b><span>toʻgʻri burchakli uchburchak</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>sin(x) = cos(90 − x)</b> — chizmadan bir qatorda chiqadi.</li>
    <li><b>sin² + cos² = 1</b> — bu Pifagorning oʻzi.</li>
    <li>Ikki burchak haqidami yoki bittasi haqidami — avval shuni
        aniqlang.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-77 — radians and arc length
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-77: Radians vs. Degrees and Arc Length",
        "category": "math",
        "order": 77,
        "summary": (
            "Radian — burchakni oʻlchashning ikkinchi usuli, va yoy uzunligi "
            "aylananing shunchaki bir ulushi."
        ),
        "stories":  ["The Wheel That Counts the Road"],
        "content": """
<h2>SAT-77: Radians vs. Degrees and Arc Length</h2>

<p>Bu darsdan boshlab test <b>aylanaga</b> oʻtadi. Va birinchi qiyinchilik
matematik emas, tildagi: SAT burchakni ikki xil birlikda beradi —
<b>degrees</b> va <b>radians</b>. Ikkalasi ham bitta narsani oʻlchaydi,
xuddi metr va fut kabi.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Formula varagʻi</span>
  <p><b>VARAQDA BOR:</b> «The number of degrees of arc in a circle is 360»
  va «The number of radians of arc in a circle is 2π». Yaʼni almashtirish
  uchun kerak boʻlgan yagona fakt varaqda turibdi.</p>
  <p><b>VARAQDA YOʻQ:</b> yoy uzunligi formulasi. Uni oʻzingiz
  quryapsiz — pastdagi ulush gʻoyasi bilan.</p>
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>darajani radianga va aksincha oʻgirasiz;</li>
    <li>eng koʻp uchraydigan oltita burchakni tanib olasiz;</li>
    <li>yoy uzunligini ulush sifatida topasiz;</li>
    <li>radianda esa uni <b>rθ</b> bilan bir qadamda olasiz.</li>
  </ul>
</div>

<h3>Bitta koʻprik</h3>

<p>Toʻliq aylana 360 daraja va 2π radian. Ikkalasini ikkiga boʻlsak, yarim
aylana: <b>180° = π radian</b>. Butun mavzu shu bitta tenglikdan chiqadi.</p>

<div class="pe-formula">
  <span class="pe-formula__label">Bridge</span>
  <span class="pe-chip pe-chip--s">180°</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">π rad</span>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Daraja → radian: × π/180</span>
    <span class="pm-solve__why">180 ni π ga almashtiryapmiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Radian → daraja: × 180/π</span>
    <span class="pm-solve__why">Teskari yoʻnalish</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">135° = 135 × π/180 = 3π/4</span>
    <span class="pm-solve__why">135/180 qisqarib 3/4</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Koʻpaytirmang — <b>qisqartiring</b>. 135 × π/180 ni hisoblab oʻtirish
  shart emas: 135/180 = 3/4, demak javob 3π/4. Aksariyat SAT javoblari
  π ni ichida saqlagan holda beriladi.
</div>

<h3>Oltita burchak — bularni tanib olish kifoya</h3>

<table class="pe-table">
  <tr><th>Degrees</th><th>Radians</th><th>Aylananing ulushi</th></tr>
  <tr><td>30°</td><td>π/6</td><td>1/12</td></tr>
  <tr><td>45°</td><td>π/4</td><td>1/8</td></tr>
  <tr><td>60°</td><td>π/3</td><td>1/6</td></tr>
  <tr><td>90°</td><td>π/2</td><td>1/4</td></tr>
  <tr><td>180°</td><td>π</td><td>1/2</td></tr>
  <tr><td>360°</td><td>2π</td><td>1</td></tr>
</table>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Uchinchi ustunga qarang: <b>radian aslida ulushning oʻzi</b>. π/6 —
  yarim aylananing oltidan biri, yaʼni butun aylananing 1/12 qismi. Radian
  gʻalati koʻrinadi, lekin u aylanani darajadan koʻra sodda tasvirlaydi.
</div>

<h3>Yoy uzunligi</h3>

<p>Yoy (<b>arc</b>) — aylana chizigʻining bir boʻlagi. Markaziy burchak
aylananing qanchasini egallasa, yoy ham aylana uzunligining shunchasini
egallaydi. Boshqa hech narsa yoʻq.</p>

<div class="pm-fig">
<svg viewBox="0 0 320 200" role="img" aria-label="Markaziy burchagi 60 daraja boʻlgan sektor">
  <circle cx="160" cy="105" r="70" fill="none" stroke="#94a3b8" stroke-width="2"/>
  <path class="pm-fill" d="M 160,105 L 230,105 A 70,70 0 0 0 195,44.4 Z"
        fill="#bfdbfe" fill-opacity="0.55" stroke="#2563eb" stroke-width="2"/>
  <circle cx="160" cy="105" r="3" fill="#0f172a"/>
  <text class="pm-lbl" x="196" y="118" font-size="13">r = 12</text>
  <text class="pm-lbl" x="186" y="92" font-size="13">60°</text>
  <text class="pm-lbl" x="240" y="52" font-size="13">arc</text>
</svg>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Ulush = 60 ÷ 360 = 1/6</span>
    <span class="pm-solve__why">Burchak aylananing oltidan biri</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Aylana uzunligi = 2π × 12 = 24π</span>
    <span class="pm-solve__why">C = 2πr, varaqda bor</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Yoy = (1/6) × 24π = 4π</span>
    <span class="pm-solve__why">≈ 12.57</span>
  </div>
</div>

<p>Agar burchak <b>radianda</b> berilgan boʻlsa, yoʻl yanada qisqaradi:
yoy uzunligi = <b>r × θ</b>. Bu alohida formula emas — bu oʻsha ulushning
soddalashgani, chunki radian ulushni oʻzida olib yuradi.</p>

<div class="pm-check">
  <p class="pm-check__t">Ikki yoʻl bir xil javob beradimi</p>
  <p>r = 12, θ = π/3 (yaʼni 60°). rθ = 12 × π/3 = 4π ✓ — yuqoridagi
  javobning aynan oʻzi.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  <b>rθ faqat radianda ishlaydi.</b> Burchak darajada boʻlsa, 12 × 60 =
  720 chiqadi — bu hech narsa emas. Formulani ishlatishdan oldin
  birlikka qarang.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>central angle</b><span>markaziy burchak</span></li>
  <li><b>arc length</b><span>yoy uzunligi</span></li>
  <li><b>minor arc AB</b><span>qisqa yoy (burchak ichidagi)</span></li>
  <li><b>in radians</b><span>radianda</span></li>
  <li><b>subtends</b><span>tortib turadi (burchak yoyni)</span></li>
  <li><b>in terms of π</b><span>π ni saqlagan holda</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">40 s</span></p>
  <div class="ps-stem__q">
    <p>An angle measures 135°. What is its measure in radians?</p>
  </div>
  <ol class="ps-ch">
    <li>3π/4</li>
    <li>4π/3</li>
    <li>2π/3</li>
    <li>3π/2</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 3π/4</p>
      <p>135 × π/180. 135/180 ni 45 ga qisqartiring: 3/4.</p>
      <p>Nazorat: 135° toʻgʻri burchakdan kattaroq, lekin 180° dan kichik —
      demak javob π/2 va π orasida. 3π/4 aynan shunday.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">4π/3</span>
  <span class="ps-trap__why">3/4 ni agʻdarib yuborgan. 4π/3 π dan katta,
  yaʼni 180° dan katta burchak — bu 135° boʻla olmaydi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">55 s</span></p>
  <div class="ps-stem__q">
    <p>In a circle with radius 9, a central angle measures 2π/3 radians.
    What is the length of the arc it subtends?</p>
  </div>
  <ol class="ps-ch">
    <li>6π</li>
    <li>3π</li>
    <li>12π</li>
    <li>18π</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 6π</p>
      <p>Burchak radianda, demak s = rθ = 9 × 2π/3 = 6π.</p>
      <p>Ulush bilan tekshirish: 2π/3 — bu 120°, yaʼni uchdan bir.
      Aylana uzunligi 18π; uning uchdan biri 6π ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">18π</span>
  <span class="ps-trap__why">Butun aylana uzunligi. Savol yoyni soʻragan,
  aylanani emas — burchakni ishlatishni unutgan.</span>
</div>

<div class="ps-desmos">
  <span class="ps-desmos__t">Desmos</span>
  <p>Radianni tekshirish uchun eng tez yoʻl: Desmosga <code>135*pi/180</code>
  deb yozing — u 2.356 beradi. Soʻng javoblarni ham shunday hisoblang.
  <b>Lekin ehtiyot boʻling:</b> Desmos burchaklarni sukut boʻyicha radianda
  oladi, shuning uchun sin(30) — 30 daraja emas, 30 radian.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">yoy = 12 × 60 = 720</p>
  <p class="pe-good">yoy = 12 × π/3 = 4π</p>
  <p class="pe-fix__why">rθ formulasi burchakni radianda talab qiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">90° = π radian</p>
  <p class="pe-good">90° = π/2</p>
  <p class="pe-fix__why">π — bu yarim aylana, 180°. Chorak aylana π/2.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Radian nima ekanini bir marta tushunib olish arziydi: bu <b>radiusga
  teng uzunlikdagi yoy</b> tortib turgan burchak. Shuning uchun s = rθ
  formulasi shunchalik sodda — θ shunchaki «nechta radius uzunligi»
  degani.
</div>

<h3>Qisqa yoy va uzun yoy</h3>

<p>Ikki nuqta aylanani ikkiga boʻladi: <b>minor arc</b> (qisqasi, burchak
ichidagi) va <b>major arc</b> (uzuni, qolgani). SAT deyarli har doim
qisqasini soʻraydi, lekin «major» soʻzini koʻrsangiz burchakni
360 dan ayirishingiz kerak.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Radius 5, markaziy burchak 144°</span>
    <span class="pm-solve__why">Aylana uzunligi 10π</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Minor arc = (144/360) × 10π = 4π</span>
    <span class="pm-solve__why">144/360 = 2/5</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Major arc = (216/360) × 10π = 6π</span>
    <span class="pm-solve__why">360 − 144 = 216, yaʼni 3/5</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Nazorat</p>
  <p>Ikkala yoy qoʻshilib butun aylanani berishi kerak: 4π + 6π = 10π ✓
  Bu tekshiruvni har safar bajaring — u bir soniya oladi va yoʻnalish
  xatosini darrov koʻrsatadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Convert 45° to radians.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">45/180 = 1/4, demak π/4.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Convert 5π/6 radians to degrees.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(5/6) × 180 = 150°.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A circle has radius 10. Find the arc length for a 36° central angle.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">36/360 = 1/10; aylana 20π; yoy = 2π.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  A circle has radius 4 and a central angle of π/2. Find the arc length.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">rθ = 4 × π/2 = 2π.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  An arc of length 5π lies on a circle of radius 15. Find the central
  angle in radians.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">θ = s ÷ r = 5π ÷ 15 = π/3.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>radian</b><span>radian</span></li>
  <li><b>degree</b><span>daraja</span></li>
  <li><b>central angle</b><span>markaziy burchak</span></li>
  <li><b>arc</b><span>yoy</span></li>
  <li><b>arc length</b><span>yoy uzunligi</span></li>
  <li><b>circumference</b><span>aylana uzunligi</span></li>
  <li><b>subtend</b><span>tortib turmoq</span></li>
  <li><b>convert</b><span>oʻgirmoq</span></li>
  <li><b>in terms of π</b><span>π orqali</span></li>
  <li><b>fraction of the circle</b><span>aylananing ulushi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>180° = π</b> — butun mavzuning yagona koʻprigi.</li>
    <li>Yoy — aylana uzunligining <b>oʻsha ulushi</b>.</li>
    <li><b>s = rθ</b> faqat radianda; birlikka har doim qarang.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-78 — sector area
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-78: Area of a Sector of a Circle",
        "category": "math",
        "order": 78,
        "summary": (
            "Sektor yuzasi — aylana yuzasining oʻsha ulushi. SAT-77 dagi "
            "ulush, faqat uzunlik oʻrniga yuza."
        ),
        "stories":  ["The Green Circles You See From a Plane"],
        "content": """
<h2>SAT-78: Area of a Sector of a Circle</h2>

<p>Bu dars SAT-77 ning egizagi. U yerda aylana <b>chizigʻining</b> bir
boʻlagi olindi; bu yerda aylana <b>ichining</b> bir boʻlagi olinadi.
<mark>Ulush esa aynan oʻsha</mark> — shuning uchun ikkala mavzuni birga
oʻrganish ikki barobar tez.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Formula varagʻi</span>
  <p><b>VARAQDA BOR:</b> A = πr² (aylana yuzasi) va C = 2πr.</p>
  <p><b>VARAQDA YOʻQ:</b> sektor yuzasi formulasi. Lekin u kerak
  emas — varaqdagi πr² ni ulushga koʻpaytirasiz, tamom.</p>
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>sektor yuzasini ulush orqali topasiz;</li>
    <li>yoy va sektor bitta ulushdan chiqishini koʻrasiz;</li>
    <li>teskari savolni yechasiz: yuza berilgan, burchak soʻralgan;</li>
    <li>sektor bilan uchburchakni chalkashtirmaysiz.</li>
  </ul>
</div>

<h3>Bitta ulush, ikkita savol</h3>

<div class="pe-formula">
  <span class="pe-formula__label">The whole idea</span>
  <span class="pe-chip pe-chip--s">burchak / 360</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--v">2πr yoki πr²</span>
</div>

<p>Chapdagi ulush ikkala savolda bir xil. Faqat oʻngdagi «butun» oʻzgaradi:
yoy uchun aylana uzunligi, sektor uchun aylana yuzasi.</p>

<div class="pm-fig">
<svg viewBox="0 0 320 200" role="img" aria-label="Markaziy burchagi 120 daraja boʻlgan sektor">
  <circle cx="160" cy="105" r="70" fill="none" stroke="#94a3b8" stroke-width="2"/>
  <path class="pm-fill" d="M 160,105 L 230,105 A 70,70 0 0 0 125,44.4 Z"
        fill="#fde68a" fill-opacity="0.65" stroke="#d97706" stroke-width="2"/>
  <circle cx="160" cy="105" r="3" fill="#0f172a"/>
  <text class="pm-lbl" x="192" y="120" font-size="13">r = 9</text>
  <text class="pm-lbl" x="168" y="88" font-size="13">120°</text>
  <text class="pm-lbl" x="150" y="30" font-size="13">sector</text>
</svg>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Ulush = 120 ÷ 360 = 1/3</span>
    <span class="pm-solve__why">Aylananing uchdan biri</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Aylana yuzasi = π × 9² = 81π</span>
    <span class="pm-solve__why">A = πr², varaqda bor</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Sektor = (1/3) × 81π = 27π</span>
    <span class="pm-solve__why">≈ 84.8</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu — pizza. 120 gradusli boʻlak butun pizzaning uchdan biri: xamiri
  ham uchdan bir (yuza), qirrasi ham uchdan bir (yoy). Bitta ulush
  hamma narsani boshqaradi.
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Yuzada radius <b>kvadratga</b> koʻtariladi. Radiusni ikki barobar
  qilsangiz, yoy ikki barobar, sektor esa <b>toʻrt barobar</b> ortadi
  (SAT-74 dagi masshtab qoidasi — aylanada ham oʻsha).
</div>

<h3>Teskari savol</h3>

<p>SAT koʻpincha uni agʻdarib beradi: sektor yuzasi va radius maʼlum,
burchak soʻralgan. Yoʻl bir xil — faqat ulushni <b>topasiz</b>,
qoʻymaysiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Sektor 8π, radius 6</span>
    <span class="pm-solve__why">Burchak soʻralyapti</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Butun yuza = π × 36 = 36π</span>
    <span class="pm-solve__why">πr²</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Ulush = 8π ÷ 36π = 2/9</span>
    <span class="pm-solve__why">π qisqaradi — har doim shunday</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Burchak = (2/9) × 360 = 80°</span>
    <span class="pm-solve__why">Nazorat: (80/360)·36π = 8π ✓</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Teskari savolda π ni hech qachon songa aylantirmang. 8π ni 36π ga
  boʻlganda π oʻz-oʻzidan qisqaradi va toza kasr qoladi. 25.13 ni
  113.10 ga boʻlish — vaqt yoʻqotish va xato manbai.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>sector</b><span>sektor (aylana boʻlagi)</span></li>
  <li><b>the shaded region</b><span>boʻyalgan soha</span></li>
  <li><b>the area of sector AOB</b><span>AOB sektorining yuzasi</span></li>
  <li><b>what fraction of the circle</b><span>aylananing qanchasi</span></li>
  <li><b>O is the center</b><span>O — markaz</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>In a circle with center O and radius 10, sector AOB has a central
    angle of 72°. What is the area of sector AOB?</p>
  </div>
  <ol class="ps-ch">
    <li>20π</li>
    <li>4π</li>
    <li>25π</li>
    <li>100π</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 20π</p>
      <p>72/360 = 1/5. Butun yuza π × 100 = 100π. Beshdan biri 20π.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">4π</span>
  <span class="ps-trap__why">Bu <b>yoy uzunligi</b>: (1/5) × 20π. Toʻgʻri
  ulush, notoʻgʻri «butun» — uzunlik oʻrniga yuza kerak edi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">70 s</span></p>
  <div class="ps-stem__q">
    <p>A sector of a circle of radius 6 has area 8π. What is the measure,
    in degrees, of its central angle?</p>
  </div>
  <ol class="ps-ch">
    <li>80</li>
    <li>60</li>
    <li>120</li>
    <li>40</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 80</p>
      <p>Butun yuza 36π. Ulush 8π/36π = 2/9. Burchak (2/9) × 360 = 80°.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">40</span>
  <span class="ps-trap__why">Ulush toʻgʻri topilgan (2/9), lekin 360 ga
  emas, <b>180</b> ga koʻpaytirilgan: (2/9) × 180 = 40. Toʻliq aylana
  360, yarmi emas.</span>
</div>

<div class="ps-desmos">
  <span class="ps-desmos__t">Desmos</span>
  <p>Sektor javobini tekshirish uchun ikkala tomonni songa aylantiring:
  <code>8pi</code> → 25.13, <code>(80/360)*pi*36</code> → 25.13. Bir xil
  chiqsa, ulush toʻgʻri.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">sektor = (72/360) × 2π × 10 = 4π</p>
  <p class="pe-good">(72/360) × π × 10² = 20π</p>
  <p class="pe-fix__why">Yuza soʻralganda «butun» πr² boʻlishi kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">radius 2 barobar → sektor 2 barobar</p>
  <p class="pe-good">sektor 4 barobar</p>
  <p class="pe-fix__why">Yuza uzunlikning kvadratiga qarab oʻsadi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Chizmada <b>«shaded region»</b> yozilgan boʻlsa, avval u nima ekanini
  aniqlang: baʼzan bu sektorning oʻzi, baʼzan esa «aylana minus sektor».
  Ikkinchi holda javob 360 dan burchakni ayirib olingan ulush bilan
  topiladi.
</div>

<h3>«Shaded region» — sektor emas, qolgani</h3>

<p>SAT chizmada koʻpincha sektorning oʻzini emas, undan <b>qolgan</b>
qismini boʻyaydi. Usul oʻzgarmaydi: ulushni qolgan burchakdan hisoblang.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Radius 8; 45° lik sektor olib tashlandi</span>
    <span class="pm-solve__why">Qolgan soha soʻralyapti</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Qolgan burchak = 360 − 45 = 315°</span>
    <span class="pm-solve__why">Ulush 315/360 = 7/8</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Yuza = (7/8) × 64π = 56π</span>
    <span class="pm-solve__why">Nazorat: 8π + 56π = 64π ✓</span>
  </div>
</div>

<h3>Ikkalasi yonma-yon</h3>

<table class="pe-table">
  <tr><th>r = 6</th><th>Yoy</th><th>Sektor</th></tr>
  <tr><td>Butun</td><td>12π</td><td>36π</td></tr>
  <tr><td>90° (1/4)</td><td>3π</td><td>9π</td></tr>
  <tr><td>60° (1/6)</td><td>2π</td><td>6π</td></tr>
  <tr><td>30° (1/12)</td><td>π</td><td>3π</td></tr>
</table>

<p>Har bir qatorda chapdagi ulush bir xil — oʻngdagi ikki ustun faqat
nimaga koʻpaytirilgani bilan farq qiladi.</p>

<h3>Sektorning perimetri — uchinchi savol turi</h3>

<p>Baʼzan «the perimeter of the sector» soʻraladi. Bu yuza ham emas, yoy
ham emas: bu <b>ikkita radius plyus yoy</b> — pizza boʻlagining butun
cheti.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Radius 6, burchak 60°</span>
    <span class="pm-solve__why">Perimetr soʻralyapti</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Yoy = (1/6) × 12π = 2π</span>
    <span class="pm-solve__why">Egri qism</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Perimetr = 6 + 6 + 2π = 12 + 2π</span>
    <span class="pm-solve__why">Ikki toʻgʻri chet + yoy</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Javob <b>aralash</b> koʻrinishda qoladi: 12 + 2π. Uni bitta songa
  yigʻishga urinmang — SAT javob variantlarini aynan shu shaklda beradi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Radius 6, central angle 60°. Find the sector area.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(1/6) × 36π = 6π.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Radius 6, central angle 60°. Find the arc length.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(1/6) × 12π = 2π — oʻsha ulush, boshqa
  «butun».</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A sector of a circle of radius 4 has area 2π. Find the central angle.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">2π ÷ 16π = 1/8; (1/8) × 360 = 45°.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  What fraction of a circle is a sector with a central angle of π/6
  radians?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">π/6 ÷ 2π = 1/12.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A circle of radius 10 has a 90° sector removed. Find the area of what
  remains.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Qolgani 270°, yaʼni 3/4: (3/4) × 100π = 75π.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>sector</b><span>sektor</span></li>
  <li><b>shaded region</b><span>boʻyalgan soha</span></li>
  <li><b>center</b><span>markaz</span></li>
  <li><b>radius</b><span>radius</span></li>
  <li><b>area</b><span>yuza</span></li>
  <li><b>fraction</b><span>ulush, kasr</span></li>
  <li><b>remaining</b><span>qolgan</span></li>
  <li><b>removed</b><span>olib tashlangan</span></li>
  <li><b>in terms of π</b><span>π orqali</span></li>
  <li><b>central angle</b><span>markaziy burchak</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Ulush = <b>burchak ÷ 360</b> — yoyda ham, sektorda ham.</li>
    <li>Yoy uchun 2πr ga, sektor uchun <b>πr²</b> ga koʻpaytiring.</li>
    <li>Teskari savolda π ni qisqartiring, hisoblamang.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-79 — circle equations
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-79: Circle Equations in the Coordinate Plane",
        "category": "math",
        "order": 79,
        "summary": (
            "Aylana tenglamasi markazni va radiusni ochiq aytib turadi — "
            "faqat ishoralarni toʻgʻri oʻqish kerak."
        ),
        "stories":  ["Three Stations and One Earthquake"],
        "content": """
<h2>SAT-79: Circle Equations in the Coordinate Plane</h2>

<p>SAT-13 da toʻgʻri chiziq tenglamasi ogʻish va kesishmani ochiq aytib
turgan edi. Aylana tenglamasi ham xuddi shunday ishlaydi:
<mark>markaz va radius tenglamaning ichida yozib qoʻyilgan</mark>. Butun
qiyinchilik — ularni notoʻgʻri oʻqib olmaslikda.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Formula varagʻi</span>
  <p><b>VARAQDA YOʻQ:</b> aylana tenglamasi. Buni yodlash kerak — Blok D
  da SOH-CAH-TOA dan keyingi ikkinchi majburiy formula.</p>
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>tenglamadan markaz va radiusni bir qarashda olasiz;</li>
    <li>markaz va radiusdan tenglama yozasiz;</li>
    <li>minus/plyus tuzogʻiga tushmaysiz;</li>
    <li>nuqta aylana ichidami yoki tashqarisidami — aniqlaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The circle</span>
  <span class="pe-chip pe-chip--v">(x − h)²</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">(y − k)²</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">r²</span>
</div>

<p>Markaz — <b>(h, k)</b>, radius — <b>r</b>. Tenglama aslida Pifagor
teoremasi: markazdan har qanday nuqtagacha boʻlgan masofa doim bir xil,
yaʼni r.</p>

<div class="pm-fig">
<svg viewBox="0 0 300 250" role="img" aria-label="Markazi (2, 1) va radiusi 3 boʻlgan aylana">
  <line class="pm-ln" x1="20" y1="150" x2="290" y2="150" stroke="#94a3b8" stroke-width="1.5"/>
  <line class="pm-ln" x1="100" y1="20" x2="100" y2="235" stroke="#94a3b8" stroke-width="1.5"/>
  <circle cx="140" cy="130" r="60" fill="none" stroke="#2563eb" stroke-width="2.5"/>
  <line x1="140" y1="130" x2="200" y2="130" stroke="#d97706" stroke-width="2"/>
  <circle cx="140" cy="130" r="3.5" fill="#0f172a"/>
  <text class="pm-lbl" x="112" y="122" font-size="13">(2, 1)</text>
  <text class="pm-lbl" x="158" y="146" font-size="13">r = 3</text>
  <text class="pm-lbl" x="278" y="166" font-size="12">x</text>
  <text class="pm-lbl" x="86" y="30" font-size="12">y</text>
  <text class="pm-lbl" x="88" y="166" font-size="12">O</text>
</svg>
</div>

<p>Chizmadagi aylananing tenglamasi: <b>(x − 2)² + (y − 1)² = 9</b>.</p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling — ikkita tuzoq</span>
  <ol>
    <li>Formulada <b>minus</b> turadi. Demak (y + 2)² aslida
        (y − (−2))², yaʼni k = <b>−2</b>, +2 emas.</li>
    <li>Oʻng tomonda <b>r²</b> turadi. 25 yozilgan boʻlsa, radius 25
        emas, <b>5</b>.</li>
  </ol>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">(x − 3)² + (y + 2)² = 25</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(y + 2)² = (y − (−2))²</span>
    <span class="pm-solve__why">Formulaga moslash uchun qayta yozamiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Markaz (3, −2), radius 5</span>
    <span class="pm-solve__why">Ishoralar teskari, radius — ildiz</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qoidani soʻz bilan aytish osonroq: <b>qavs ichidagi sonning ishorasini
  agʻdaring</b>. (x − 3) → 3; (y + 2) → −2. Bu xuddi SAT-33 dagi
  parabola tepasi bilan bir xil qoida — va SAT uni ikkala mavzuda ham
  bir xil sinaydi.
</div>

<h3>Teskari yoʻnalish</h3>

<p>Markaz va radius berilib, tenglama soʻralishi ham xuddi shunchalik
tez-tez uchraydi. Ishoralar yana agʻdariladi.</p>

<div class="pm-check">
  <p class="pm-check__t">Markaz (−4, 6), radius 3</p>
  <p>(x + 4)² + (y − 6)² = 9. Nazorat: h = −4 boʻlgani uchun x − (−4) =
  x + 4 ✓, va oʻng tomon 3² = 9 ✓</p>
</div>

<h3>Nuqta qayerda</h3>

<p>Nuqtaning koordinatalarini tenglamaning chap tomoniga qoʻying va
natijani r² bilan solishtiring: kichik boʻlsa ichida, teng boʻlsa
ustida, katta boʻlsa tashqarisida.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Bu savolda ildiz olish shart emas. 9 ni 25 bilan solishtirish, 3 ni 5
  bilan solishtirish bilan bir xil javob beradi — kvadratga koʻtarish
  tartibni buzmaydi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>in the xy-plane</b><span>xy tekisligida</span></li>
  <li><b>the equation of a circle</b><span>aylana tenglamasi</span></li>
  <li><b>the center of the circle</b><span>aylananing markazi</span></li>
  <li><b>lies on the circle</b><span>aylana ustida yotadi</span></li>
  <li><b>which of the following is an equation of</b><span>quyidagilardan qaysi biri … tenglamasi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">40 s</span></p>
  <div class="ps-stem__q">
    <p>In the xy-plane, the equation of a circle is
    (<i>x</i> − 3)² + (<i>y</i> + 2)² = 25. What is the center of the
    circle?</p>
  </div>
  <ol class="ps-ch">
    <li>(3, −2)</li>
    <li>(−3, 2)</li>
    <li>(3, 2)</li>
    <li>(−3, −2)</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) (3, −2)</p>
      <p>Qavslardagi ishoralarni agʻdaring: −3 → 3, +2 → −2.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">(−3, 2)</span>
  <span class="ps-trap__why">Ishoralarni umuman agʻdarmagan — qavsda
  nima yozilgan boʻlsa, oʻshani koʻchirgan. Bu eng koʻp uchraydigan
  xato.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">55 s</span></p>
  <div class="ps-stem__q">
    <p>A circle in the xy-plane has center (−4, 6) and radius 3. Which of
    the following is an equation of the circle?</p>
  </div>
  <ol class="ps-ch">
    <li>(<i>x</i> + 4)² + (<i>y</i> − 6)² = 9</li>
    <li>(<i>x</i> − 4)² + (<i>y</i> + 6)² = 9</li>
    <li>(<i>x</i> + 4)² + (<i>y</i> − 6)² = 3</li>
    <li>(<i>x</i> − 4)² + (<i>y</i> + 6)² = 3</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) (x + 4)² + (y − 6)² = 9</p>
      <p>h = −4 → x − (−4) = x + 4. k = 6 → y − 6. Oʻng tomon 3² = 9.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">(x + 4)² + (y − 6)² = 3</span>
  <span class="ps-trap__why">Ishoralar toʻgʻri, lekin oʻng tomonga
  radiusning oʻzi yozilgan. U yerda <b>r²</b> turishi kerak.</span>
</div>

<div class="ps-desmos">
  <span class="ps-desmos__t">Desmos</span>
  <p>Aylana tenglamasini Desmosga <b>xuddi qanday berilgan boʻlsa,
  shundayligicha</b> kiriting — u aylanani chizadi va markazni koʻz
  bilan koʻrasiz. Javob variantlarini ham kiritsangiz, notoʻgʻrilari
  boshqa joyda turadi. Bu savol turida Desmos deyarli hech qanday xato
  qoldirmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">(x − 3)² + (y + 2)² = 25 → radius 25</p>
  <p class="pe-good">radius 5</p>
  <p class="pe-fix__why">Oʻng tomonda r² turadi, r emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">markaz (−4, 6) → (x − 4)²</p>
  <p class="pe-good">(x + 4)²</p>
  <p class="pe-fix__why">x − h da h = −4, demak x − (−4) = x + 4.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Nega tenglama shunday? Markaz (h, k) va aylanadagi nuqta (x, y)
  orasidagi masofani Pifagor bilan yozing: gorizontal farq (x − h),
  vertikal farq (y − k), gipotenuza r. Kvadratga koʻtarsangiz — aynan
  shu tenglama chiqadi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Find the center and radius of (<i>x</i> + 1)² + (<i>y</i> − 7)² = 36.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Markaz (−1, 7), radius 6.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Write the equation of the circle with center (0, −5) and radius 2.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">x² + (y + 5)² = 4.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Does the point (6, 1) lie on the circle
  (<i>x</i> − 2)² + (<i>y</i> − 1)² = 16?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">16 + 0 = 16 ✓ — ha, aylana ustida.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Is (0, 0) inside or outside (<i>x</i> − 3)² + (<i>y</i> − 4)² = 20?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">9 + 16 = 25 > 20, demak tashqarisida.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A circle has center (2, 2) and passes through (2, 7). Find its radius.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Nuqtalar bir vertikalda: radius 7 − 2 = 5.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>circle</b><span>aylana</span></li>
  <li><b>center</b><span>markaz</span></li>
  <li><b>radius</b><span>radius</span></li>
  <li><b>xy-plane</b><span>xy tekisligi</span></li>
  <li><b>lies on</b><span>ustida yotadi</span></li>
  <li><b>passes through</b><span>… dan oʻtadi</span></li>
  <li><b>inside / outside</b><span>ichida / tashqarisida</span></li>
  <li><b>coordinates</b><span>koordinatalar</span></li>
  <li><b>distance</b><span>masofa</span></li>
  <li><b>an equation of</b><span>… ning tenglamasi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>(x − h)² + (y − k)² = r²</b> — varaqda yoʻq, yodlang.</li>
    <li>Qavsdagi ishorani <b>agʻdaring</b>: (y + 2) → k = −2.</li>
    <li>Oʻng tomon <b>r²</b>; radius uning ildizi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-80 — completing the square for a circle
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-80: Completing the Square to Find a Circle's Center and Radius",
        "category": "math",
        "order": 80,
        "summary": (
            "Aylana tenglamasi yoyilgan holda berilsa — uni toʻliq kvadratga "
            "toʻldirib, markaz va radiusni koʻrinadigan qilamiz."
        ),
        "stories":  ["The Square That al-Khwarizmi Completed"],
        "content": """
<h2>SAT-80: Completing the Square to Find a Circle's Center and Radius</h2>

<p>SAT-79 da aylana tayyor holda berildi. Endi test uni <b>yashiradi</b>:
qavslar ochilib, hamma narsa bitta qatorga yoyilgan. Markaz ham, radius
ham koʻrinmaydi. <mark>Vazifa — qavslarni qaytadan yopish</mark>, va bu
Blok D dagi eng koʻp qadamli savol.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Formula varagʻi</span>
  <p><b>VARAQDA YOʻQ:</b> na aylana tenglamasi, na toʻliq kvadratga
  toʻldirish. Bu dars butunlay xotira va usulga tayanadi — shuning
  uchun Blok D ni u yakunlaydi.</p>
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>yoyilgan tenglamani standart koʻrinishga keltirasiz;</li>
    <li>«yarmini ol, kvadratga koʻtar, ikkala tomonga qoʻsh» usulini
        avtomatik bajarasiz;</li>
    <li>x va y ni alohida-alohida toʻldirasiz;</li>
    <li>Desmos bilan javobni 10 soniyada tekshirasiz.</li>
  </ul>
</div>

<h3>Usul — uch qadam</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">The move</span>
  <ol>
    <li><b>Guruhlang:</b> x lar birga, y lar birga, ozod had oʻng
        tomonga.</li>
    <li><b>Toʻldiring:</b> har bir guruhda koeffitsiyentning yarmini
        oling, kvadratga koʻtaring, <b>ikkala tomonga</b> qoʻshing.</li>
    <li><b>Yozing:</b> qavslarni yoping va oʻng tomondagi sonni r² deb
        oʻqing.</li>
  </ol>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x² + y² − 6x + 4y − 12 = 0</span>
    <span class="pm-solve__why">Berilgan — markaz koʻrinmaydi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(x² − 6x) + (y² + 4y) = 12</span>
    <span class="pm-solve__why">Guruhladik, −12 ni oʻngga oʻtkazdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">−6 ning yarmi −3, kvadrati 9</span>
    <span class="pm-solve__why">x guruhiga 9 kerak</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4 ning yarmi 2, kvadrati 4</span>
    <span class="pm-solve__why">y guruhiga 4 kerak</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(x² − 6x + 9) + (y² + 4y + 4) = 12 + 9 + 4</span>
    <span class="pm-solve__why">Ikkala tomonga ham qoʻshdik — muvozanat</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">(x − 3)² + (y + 2)² = 25</span>
    <span class="pm-solve__why">Markaz (3, −2), radius 5</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling — asosiy xato</span>
  9 va 4 ni faqat chap tomonga qoʻshib qoʻyish. Tenglamaning ikkala
  tomoniga ham qoʻshilmasa, u <b>boshqa aylanaga</b> aylanadi va radius
  notoʻgʻri chiqadi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qavs ichidagi son — bu <b>yarmi</b>, kvadrati emas. x² − 6x + 9 dan
  (x − 3)² chiqadi: 3 — bu 6 ning yarmi. Oʻquvchilar tez-tez 9 ni
  qavsga yozib yuborishadi.
</div>

<div class="pm-check">
  <p class="pm-check__t">Ikkinchi misol</p>
  <p>x² + y² + 10x − 2y + 17 = 0 → (x² + 10x) + (y² − 2y) = −17.</p>
  <p>10 ning yarmi 5, kvadrati 25. −2 ning yarmi −1, kvadrati 1.</p>
  <p>(x + 5)² + (y − 1)² = −17 + 25 + 1 = <b>9</b>. Markaz (−5, 1),
  radius 3 ✓</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Oʻng tomon manfiy sondan boshlansa ham qoʻrqmang — qoʻshib
  borilganda u odatda musbatga aylanadi. Yuqorida −17 dan 9 chiqdi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>completing the square</b><span>toʻliq kvadratga toʻldirish</span></li>
  <li><b>standard form</b><span>standart koʻrinish</span></li>
  <li><b>the length of the radius</b><span>radiusning uzunligi</span></li>
  <li><b>the graph of the equation</b><span>tenglamaning grafigi</span></li>
  <li><b>what are the coordinates of the center</b><span>markazning koordinatalari</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">80 s</span></p>
  <div class="ps-stem__q">
    <p>The graph of <i>x</i>² + <i>y</i>² − 4<i>x</i> − 10<i>y</i> + 20 = 0
    in the xy-plane is a circle. What is the length of the radius?</p>
  </div>
  <ol class="ps-ch">
    <li>3</li>
    <li>9</li>
    <li>5</li>
    <li>2</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 3</p>
      <p>(x² − 4x) + (y² − 10y) = −20.</p>
      <p>−4 ning yarmi −2 → 4; −10 ning yarmi −5 → 25.</p>
      <p>(x − 2)² + (y − 5)² = −20 + 4 + 25 = 9. Radius = √9 = 3.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">9</span>
  <span class="ps-trap__why">Toʻldirish toʻgʻri bajarilgan, lekin oxirgi
  qadam unutilgan: 9 — bu r², radius esa uning ildizi. SAT bu tuzoqni
  deyarli har safar qoʻyadi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>In the xy-plane, the graph of <i>x</i>² + <i>y</i>² − 8<i>x</i> +
    6<i>y</i> = 0 is a circle. What are the coordinates of its center?</p>
  </div>
  <ol class="ps-ch">
    <li>(4, −3)</li>
    <li>(−4, 3)</li>
    <li>(8, −6)</li>
    <li>(−8, 6)</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) (4, −3)</p>
      <p>−8 ning yarmi −4 → 16; 6 ning yarmi 3 → 9.</p>
      <p>(x − 4)² + (y + 3)² = 0 + 16 + 9 = 25. Markaz (4, −3),
      radius 5.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">(8, −6)</span>
  <span class="ps-trap__why">Koeffitsiyentlarning <b>yarmi</b> emas,
  oʻzi olingan. Toʻldirishda har doim yarmi qavsga tushadi.</span>
</div>

<div class="ps-desmos">
  <span class="ps-desmos__t">Desmos — bu savolda deyarli aldov darajasida foydali</span>
  <p>Yoyilgan tenglamani Desmosga <code>x^2+y^2-4x-10y+20=0</code> deb
  toʻgʻridan-toʻgʻri kiriting: u aylanani chizadi. Markazni koʻz bilan
  oʻqiysiz, radiusni esa markazdan chetgacha sanaysiz. Toʻldirish umuman
  bajarilmaydi.</p>
  <p><b>Lekin usulni baribir biling:</b> savol «in terms of <i>a</i>»
  koʻrinishida, harflar bilan berilsa, Desmos chizolmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">x² − 6x + 9 = (x − 9)²</p>
  <p class="pe-good">(x − 3)²</p>
  <p class="pe-fix__why">Qavsga koeffitsiyentning yarmi tushadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">(x − 2)² + (y − 5)² = 9 → radius 9</p>
  <p class="pe-good">radius 3</p>
  <p class="pe-fix__why">Oʻng tomon r²; oxirgi qadam — ildiz olish.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha — Blok D yakuni</span>
  Geometriya bloki shu bilan tugadi. Undan uchta narsa qoladi:
  <b>formula varagʻi</b> (unda nima borligini bilish yarim ish),
  <b>SOH-CAH-TOA</b> va <b>aylana tenglamasi</b> — varaqda yoʻq, lekin
  har testda uchraydigan ikki formula. Qolgani chizmani diqqat bilan
  oʻqishga borib taqaladi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Find the center and radius of <i>x</i>² + <i>y</i>² − 2<i>x</i> − 8 = 0.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(x − 1)² + y² = 8 + 1 = 9. Markaz (1, 0),
  radius 3.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Find the center and radius of <i>x</i>² + <i>y</i>² + 6<i>y</i> + 5 = 0.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">x² + (y + 3)² = −5 + 9 = 4. Markaz (0, −3),
  radius 2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Find the radius of <i>x</i>² + <i>y</i>² − 12<i>x</i> + 4<i>y</i> + 15 = 0.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(x − 6)² + (y + 2)² = −15 + 36 + 4 = 25.
  Radius 5.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Why must the added number go on both sides?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Aks holda tenglik buziladi va boshqa aylana
  hosil boʻladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  What does <i>x</i>² + <i>y</i>² − 2<i>x</i> + 2<i>y</i> + 2 = 0
  describe?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(x − 1)² + (y + 1)² = −2 + 1 + 1 = 0 — radiusi
  nol, yaʼni bitta nuqta: (1, −1).</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>completing the square</b><span>toʻliq kvadratga toʻldirish</span></li>
  <li><b>standard form</b><span>standart koʻrinish</span></li>
  <li><b>expand</b><span>qavsni ochmoq</span></li>
  <li><b>coefficient</b><span>koeffitsiyent</span></li>
  <li><b>constant term</b><span>ozod had</span></li>
  <li><b>both sides</b><span>ikkala tomon</span></li>
  <li><b>the graph of</b><span>… ning grafigi</span></li>
  <li><b>coordinates</b><span>koordinatalar</span></li>
  <li><b>length of the radius</b><span>radius uzunligi</span></li>
  <li><b>rewrite</b><span>qayta yozmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Yarmi, kvadrati, ikkala tomonga</b> — usulning oʻzi shu.</li>
    <li>Qavsga <b>yarmi</b> tushadi: x² − 6x → (x − 3)².</li>
    <li>Oxirgi qadamni unutmang: <b>radius = √r²</b>.</li>
  </ul>
</div>
""",
    },
]
