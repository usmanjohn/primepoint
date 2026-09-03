# -*- coding: utf-8 -*-
"""Prime SAT Math — lessons 11–15 (parallel, perpendicular, and inequalities).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_SAT.md
Lesson list: tutorial/management/commands/toc_prime_sat_math.txt

  mashqlar — practice/management/commands/_practice_ps_11_15.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_sat_readings_11_15.py

⚠️ ESKI SAT-11 … SAT-15 ustiga yoziladi (--republish). Sarlavhalar toc'dagidek.
⚠️ Til: sarlavha va test savollari inglizcha, tushuntirish oʻzbekcha. Son: 3.5 va 1,200.

⚠️ Kumulyativ (SAT-1…10 erkin: ifoda, tenglama, matndan tenglama, modul, qiyalik,
   ikki nuqtadan qiyalik, y = mx + b, point-slope va standart shakl, tez chizish,
   kontekstdagi maʼno):
  • SAT-11 — parallel: qiyaliklar teng, b lar har xil; bir xil b — bitta chiziq.
  • SAT-12 — perpendikulyar: teskari agʻdarib, ishorani almashtirish (m₁ · m₂ = −1);
    gorizontal ⊥ vertikal — qoida ishlamaydigan yagona hol.
  • SAT-13 — tengsizlik yechish; manfiy songa boʻlganda ishora agʻdariladi.
  • SAT-14 — tekislikda tengsizlik grafigi: chiziq uzuq/uzluksiz va shtrixlash.
  • SAT-15 — matndan tengsizlik va butun songa yaxlitlash tomoni.
  • ⛔ Sistema (SAT-16…18) YOʻQ; modulli tengsizlik (SAT-22) YOʻQ; ps-desmos SAT-83 dan.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_sat_11_15.py \\
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
    # SAT-11 — parallel lines
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-11: Parallel Lines and Equal Slopes",
        "category": "math",
        "order": 11,
        "summary": (
            "Parallel chiziqlar — bir xil qiyalik, boshqa y-intercept. Berilgan "
            "chiziqqa parallel tenglama tuzish, standart shakldagi parallellik va "
            "«bir xil qiyalik, bir xil b» degan tuzoq."
        ),
        "stories": ["Two Canals, One Fall"],
        "content": """
<h2>SAT-11: Parallel Lines and Equal Slopes</h2>

<p>Ikki chiziq hech qachon kesishmasligi uchun ular <mark>bir xil tiklikda</mark> borishi
kerak — bitta ham oʻzidan tezroq koʻtarilmasligi kerak, aks holda ular baribir uchrashadi.
SAT'da bu bitta jumlaga siqiladi va har testda bir-ikki savol beradi, koʻpincha eng
qisqa savollar qatorida.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>ikki tenglamaga qarab ular parallel yoki yoʻqligini aytasiz;</li>
    <li>berilgan chiziqqa parallel va berilgan nuqtadan oʻtuvchi tenglama tuzasiz;</li>
    <li>standart shakldagi chiziqlar uchun ham buni qila olasiz;</li>
    <li>«parallel» va «aynan bitta chiziq» ni farqlaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Parallel</span>
  <span class="pe-chip pe-chip--s">m<sub>1</sub></span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">m<sub>2</sub></span>
  <span class="pe-op">va</span>
  <span class="pe-chip pe-chip--o">b<sub>1</sub></span>
  <span class="pe-op">≠</span>
  <span class="pe-chip pe-chip--o">b<sub>2</sub></span>
</div>

<h3>Bitta shart yetarli emas</h3>

<p>Koʻpchilik «parallel = bir xil qiyalik» deb yodlaydi va yarim javob oladi. Toʻliq
taʼrif ikkita shartdan iborat: <strong>qiyaliklar teng</strong> va
<strong>y-interceptlar har xil</strong>. Agar ikkalasi ham teng boʻlsa, bu ikki chiziq
emas — bu <u>bitta chiziqning ikki marta yozilgani</u>.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Parallel</p>
    <p><i>y</i> = 3<i>x</i> + 1 va <i>y</i> = 3<i>x</i> − 4</p>
    <p>Qiyalik bir xil, b boshqa. Hech qachon kesishmaydi — sistemasining
    <b>yechimi yoʻq</b> (SAT-2 dagi «no solution» aynan shu).</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Bitta chiziq</p>
    <p><i>y</i> = 3<i>x</i> + 1 va 2<i>y</i> = 6<i>x</i> + 2</p>
    <p>Ikkinchisini 2 ga boʻlsangiz, birinchisi chiqadi. Ular <b>ustma-ust</b> tushadi —
    cheksiz koʻp umumiy nuqta.</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Shuning uchun tenglamani <b>solishtirishdan oldin</b> ikkalasini ham
  <i>y</i> = <i>mx</i> + <i>b</i> koʻrinishiga keltiring. 2<i>y</i> = 6<i>x</i> + 2
  tenglamasiga qarab «qiyaligi 6» deb aytish — shu mavzudagi eng koʻp uchraydigan xato.
</div>

<h3>Misol 1 (oson) — parallel tenglama tuzish</h3>

<p>Write the equation of the line parallel to <em>y</em> = 3<em>x</em> − 4 that passes
through (2, 5).</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">m = 3</span>
    <span class="pm-solve__why">Parallel — qiyalik <b>koʻchiriladi</b>, hisoblanmaydi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5 = 3(2) + b</span>
    <span class="pm-solve__why">Nuqtani qoʻydik (SAT-7)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">b = −1  →  y = 3x − 1</span>
    <span class="pm-solve__why">Yangi b eskisidan farq qiladi — demak haqiqatan parallel</span>
  </div>
</div>

<h3>Misol 2 (oʻrta) — standart shakl</h3>

<p>2<em>x</em> + 3<em>y</em> = 12 chizigʻiga parallel va (3, 1) dan oʻtuvchi chiziq.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">m = −A ÷ B = −2/3</span>
    <span class="pm-solve__why">Standart shaklning qiyaligi (SAT-8), hisob shart emas</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">1 = −(2/3)(3) + b  →  1 = −2 + b</span>
    <span class="pm-solve__why">Nuqtani qoʻydik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">b = 3  →  y = −(2/3)x + 3</span>
    <span class="pm-solve__why">Yoki standart shaklda: 2x + 3y = 9</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Standart shaklda parallel chiziqlarning <b>chap tomoni bir xil</b> boʻladi, faqat oʻng
  tomondagi son oʻzgaradi: 2<i>x</i> + 3<i>y</i> = 12 va 2<i>x</i> + 3<i>y</i> = 9.
  Javoblar standart shaklda berilsa, shu bitta qarash yetadi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Savol «<em>which line is parallel to…</em>» desa, javob <b>boshqa</b> chiziq boʻlishi
  kerak — berilganining oʻzi javoblar orasida turgan boʻlsa, u toʻgʻri emas. Chiziq oʻz-oʻziga
  parallel deb hisoblanmaydi.
</div>

<h3>Misol 3 (SAT darajasi) — nomaʼlum koeffitsient</h3>

<p>For what value of <em>k</em> are the lines <em>y</em> = 4<em>x</em> + 1 and
<em>y</em> = (<em>k</em> − 2)<em>x</em> − 5 parallel?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">k − 2 = 4</span>
    <span class="pm-solve__why">Parallellik sharti: qiyaliklar teng</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">k = 6</span>
    <span class="pm-solve__why">b lar (1 va −5) turlicha — demak haqiqatan parallel</span>
  </div>
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>parallel to the line</b><span>shu chiziqqa parallel</span></li>
  <li><b>which line is parallel to</b><span>qaysi chiziq parallel — qiyaliklarni solishtiring</span></li>
  <li><b>the system has no solution</b><span>sistemaning yechimi yoʻq — chiziqlar parallel</span></li>
  <li><b>infinitely many solutions</b><span>cheksiz koʻp yechim — bu bitta chiziq, parallel emas</span></li>
  <li><b>where k is a constant</b><span>k — nomaʼlum son, koʻpincha aynan u soʻraladi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">40 s</span></p>
  <div class="ps-stem__q">
    <p>Which of the following lines is parallel to the line
    <i>y</i> = −2<i>x</i> + 7?</p>
  </div>
  <ol class="ps-ch">
    <li><i>y</i> = −7<i>x</i> + 2</li>
    <li><i>y</i> = −2<i>x</i> − 3</li>
    <li><i>y</i> = (1/2)<i>x</i> + 7</li>
    <li><i>y</i> = 2<i>x</i> + 7</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) y = −2x − 3</p>
      <p>Qiyaligi ham −2, lekin b boshqa (7 emas, −3) — ikkala shart ham bajarildi.</p>
      <p><b>y = 2x + 7</b> bir xil b ga ega, lekin qiyaligi boshqa: b ning tengligi
      parallellikka <u>hech qanday</u> aloqasi yoʻq.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">y = 2x + 7</span>
  <span class="ps-trap__why">Bir xil <b>b</b> ni parallellik deb olgan javob. Parallellikni
  faqat qiyalik hal qiladi; b esa aksincha — <b>har xil</b> boʻlishi kerak.</span>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">y = −7x + 2</span>
  <span class="ps-trap__why">Sonlar oʻrin almashgan (−2 va 7 → −7 va 2). SAT bunday
  «tanish sonlar, notoʻgʻri joyda» javobini deyarli har doim qoʻyadi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>Line <i>k</i> passes through the point (1, 4) and is parallel to the line
    <i>y</i> = 5<i>x</i> − 2. What is the <i>y</i>-intercept of line <i>k</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>−1</li>
    <li>3</li>
    <li>4</li>
    <li>9</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) −1</p>
      <div class="pm-solve">
        <div class="pm-solve__row">
          <span class="pm-solve__step">m = 5</span>
          <span class="pm-solve__why">Parallel chiziqning qiyaligi bir xil</span>
        </div>
        <div class="pm-solve__row pm-solve__row--ans">
          <span class="pm-solve__step">4 = 5(1) + b  →  b = −1</span>
          <span class="pm-solve__why">Nuqtani qoʻydik va b ni topdik</span>
        </div>
      </div>
      <p><b>9</b> — ayirish oʻrniga qoʻshgan javob (4 + 5). <b>4</b> — nuqtaning
      <i>y</i> qiymati: u faqat nuqta x = 0 boʻlgandagina b boʻlardi.</p>
    </div>
  </details>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Parallellik savolida uch qadam, hisobsiz:</p>
  <ol>
    <li>Ikkala tenglamani ham <b>y ga yeching</b> (kerak boʻlsa).</li>
    <li>Faqat <em>x</em> oldidagi sonlarni solishtiring — qolgani ahamiyatsiz.</li>
    <li>Ular teng boʻlsa, b larga qarang: teng boʻlsa bu <b>bitta chiziq</b>, parallel
        emas.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">2y = 6x + 2 va y = 3x + 1 parallel.</p>
  <p class="pe-good">Ular <b>bitta va oʻsha</b> chiziq.</p>
  <p class="pe-fix__why">Birinchisini 2 ga boʻlsangiz ikkinchisi chiqadi. Parallel
  chiziqlar <b>hech qachon</b> umumiy nuqtaga ega emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">y = 4x + 3 va y = 4x + 3 parallel.</p>
  <p class="pe-good">Parallel emas — bir xil chiziq (b lar ham teng).</p>
  <p class="pe-fix__why">Parallellik uchun b lar <b>har xil</b> boʻlishi shart.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Parallel chiziqlar sistemasining <b>yechimi yoʻq</b>, ustma-ust tushgan chiziqlarniki esa
  <b>cheksiz koʻp</b>. SAT-2 dagi ikki maxsus hol aynan shu ikki rasmning tenglamadagi
  koʻrinishi edi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  What is the slope of any line parallel to <i>y</i> = −6<i>x</i> + 11?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">−6 — parallel chiziqning qiyaligi aynan oʻsha. 11 hech qanday
  rol oʻynamaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Write the equation of the line parallel to <i>y</i> = 2<i>x</i> + 9 through (0, −4).</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>y</i> = 2<i>x</i> − 4 — nuqtaning x koordinatasi 0, demak
  b darhol maʼlum.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Is the line 4<i>x</i> + 2<i>y</i> = 10 parallel to <i>y</i> = −2<i>x</i> + 1?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ha, parallel — y ga yechamiz: 2<i>y</i> = −4<i>x</i> + 10, demak
  <i>y</i> = −2<i>x</i> + 5. Qiyaliklar teng (−2 = −2), b lar esa har xil (5 va 1) —
  ikkala shart ham bajarildi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  For what value of <i>k</i> are <i>y</i> = 7<i>x</i> − 1 and
  <i>y</i> = (<i>k</i> + 3)<i>x</i> + 2 parallel?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>k</i> = 4 — qiyaliklar teng boʻlishi kerak: k + 3 = 7.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Two roads are drawn on a plan as <i>y</i> = 0.5<i>x</i> + 2 and <i>y</i> = 0.5<i>x</i> + 6.
  Will they ever meet?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — qiyaliklari teng, b lari har xil, demak parallel. Ular
  har doim 4 birlik masofada yonma-yon boradi.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>parallel</b><span>parallel; hech qachon kesishmaydi</span></li>
  <li><b>equal slopes</b><span>teng qiyaliklar</span></li>
  <li><b>distinct / different</b><span>har xil (b lar haqida)</span></li>
  <li><b>coincide</b><span>ustma-ust tushmoq — bitta chiziq</span></li>
  <li><b>no solution</b><span>yechimi yoʻq (parallel sistema)</span></li>
  <li><b>infinitely many solutions</b><span>cheksiz koʻp yechim (bitta chiziq)</span></li>
  <li><b>where k is a constant</b><span>k — nomaʼlum son</span></li>
  <li><b>intersect</b><span>kesishmoq</span></li>
  <li><b>rearrange</b><span>shaklni oʻzgartirish</span></li>
  <li><b>slope of any line parallel to</b><span>parallel chiziqning qiyaligi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Parallel = <b>qiyaliklar teng</b> VA <b>b lar har xil</b>. Ikkinchi shart ham
        shart.</li>
    <li>Solishtirishdan oldin ikkala tenglamani ham <b>y ga yeching</b>.</li>
    <li>Parallel sistemaning <b>yechimi yoʻq</b>; ustma-ust tushgani cheksiz koʻp
        yechim beradi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-12 — perpendicular lines
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-12: Perpendicular Lines and Negative Reciprocal Slopes",
        "category": "math",
        "order": 12,
        "summary": (
            "Perpendikulyar chiziqlarning qiyaliklari koʻpaytmasi −1 ga teng: kasrni "
            "agʻdarib, ishorani almashtiramiz. Gorizontal va vertikal — qoida "
            "ishlamaydigan yagona juftlik."
        ),
        "stories": ["The Carpenter's Diagonal"],
        "content": """
<h2>SAT-12: Perpendicular Lines and Negative Reciprocal Slopes</h2>

<p>Parallel chiziqlar bir xil qiyalikka ega edi. <mark>Perpendikulyar</mark> chiziqlar
esa — toʻgʻri burchak ostida kesishadiganlari — bir-biriga eng qarama-qarshi qiyaliklarga
ega. Qoida bitta amalda: <strong>agʻdaring va ishorani almashtiring</strong>. SAT buni
har testda soʻraydi va deyarli har doim javoblar orasiga «faqat agʻdarilgan» va «faqat
ishorasi almashgan» variantlarni qoʻyadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>berilgan qiyalikning perpendikulyarini bir soniyada aytasiz;</li>
    <li>tekshiruvni koʻpaytirish orqali qilasiz: m<sub>1</sub> · m<sub>2</sub> = −1;</li>
    <li>berilgan chiziqqa perpendikulyar va nuqtadan oʻtuvchi tenglama tuzasiz;</li>
    <li>gorizontal va vertikal juftlikni istisno sifatida bilasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Perpendicular</span>
  <span class="pe-chip pe-chip--s">m<sub>1</sub></span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">m<sub>2</sub></span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--neg">−1</span>
  <span class="pe-chip pe-chip--opt">m<sub>2</sub> = −1 ÷ m<sub>1</sub></span>
</div>

<h3>Agʻdaring va ishorani almashtiring</h3>

<p><strong>Negative reciprocal</strong> — «manfiy teskari son». Ikki amal, tartibi
ahamiyatsiz:</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Berilgan qiyalik</th><th>Agʻdaring</th><th>Ishorani almashtiring</th></tr>
  <tr><td>4 (yaʼni 4/1)</td><td class="pm-word__sym">1/4</td><td>−1/4</td></tr>
  <tr><td>−2/3</td><td class="pm-word__sym">−3/2</td><td>3/2</td></tr>
  <tr><td>1/5</td><td class="pm-word__sym">5</td><td>−5</td></tr>
  <tr><td>−1</td><td class="pm-word__sym">−1</td><td>1</td></tr>
</table></div>

<p>Tekshirish har doim bir xil: ikkalasini koʻpaytiring va <b>−1</b> chiqishi kerak.
4 × (−1/4) = −1 ✓ va (−2/3) × (3/2) = −1 ✓</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Butun son ham kasr: 4 — bu 4/1. Agʻdarilganda 1/4 boʻladi. Oʻquvchilar butun sonni
  «agʻdarib boʻlmaydi» deb oʻylab, faqat ishorani almashtiradi va −4 deb javob beradi —
  bu javoblar orasidagi eng qadimiy tuzoq.
</div>

<h3>Misol 1 (oson)</h3>

<p>What is the slope of a line perpendicular to <em>y</em> = 4<em>x</em> + 1?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">m<sub>1</sub> = 4 = 4/1</span>
    <span class="pm-solve__why">Butun sonni kasr koʻrinishida yozdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">m<sub>2</sub> = −1/4</span>
    <span class="pm-solve__why">Agʻdardik (1/4), ishorani almashtirdik. Tekshiruv: 4 × (−1/4) = −1 ✓</span>
  </div>
</div>

<h3>Misol 2 (oʻrta) — nuqta bilan birga</h3>

<p>Line <em>m</em> is perpendicular to <em>y</em> = 4<em>x</em> + 1 and passes through
(8, 3). Write its equation.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">m = −1/4</span>
    <span class="pm-solve__why">Misol 1 dan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 = −(1/4)(8) + b  →  3 = −2 + b</span>
    <span class="pm-solve__why">Nuqtani qoʻydik; −(1/4) × 8 = −2</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">b = 5  →  y = −(1/4)x + 5</span>
    <span class="pm-solve__why">Tekshiruv: −(1/4)(8) + 5 = −2 + 5 = 3 ✓</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Nuqtani <b>qulay</b> tanlashadi: 8 soni 1/4 ga boʻlinadi. Agar hisob chirkin chiqsa,
  koʻpincha qiyalikni notoʻgʻri agʻdargan boʻlasiz — bir qadam orqaga qayting.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <em>Reciprocal</em> — «teskari son», yaʼni 1 ni shu songa boʻlgani: 4 ning teskarisi
  1/4. <em>Negative reciprocal</em> esa uning ustiga minus qoʻyadi. Ikki soʻz — ikki amal;
  savolda ikkalasi ham aytilgan.
</div>

<h3>Bitta istisno: gorizontal va vertikal</h3>

<p>Gorizontal chiziqning qiyaligi <strong>0</strong>, vertikalniki
<strong>undefined</strong>. Ular bir-biriga perpendikulyar — buni koʻz bilan koʻrish
mumkin — lekin koʻpaytmasi −1 emas, chunki <u>aniqlanmagan songa koʻpaytirib boʻlmaydi</u>.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 180" role="img" aria-label="Gorizontal va vertikal chiziq toʻgʻri burchak hosil qiladi">
    <line class="pm-ln pm-ln--hl" x1="30" y1="110" x2="290" y2="110"/>
    <line class="pm-ln pm-ln--hl" x1="150" y1="20" x2="150" y2="165"/>
    <rect class="pm-ln" x="150" y="92" width="18" height="18" fill="none"/>
    <text class="pm-lbl" x="240" y="100">m = 0</text>
    <text class="pm-lbl" x="158" y="36">undefined</text>
  </svg>
  <figcaption>Toʻgʻri burchak bor, lekin «koʻpaytmasi −1» qoidasi bu juftlikka qoʻllanmaydi.</figcaption>
</figure>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Savol «<em>perpendicular to the line x = 3</em>» desa, javob qiyalik <b>0</b> boʻlgan
  gorizontal chiziq, yaʼni <em>y</em> = son. Bu yerda formula bilan urinmang.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>perpendicular to</b><span>…ga perpendikulyar; toʻgʻri burchak ostida kesishadi</span></li>
  <li><b>negative reciprocal</b><span>manfiy teskari son: agʻdar va ishorani almashtir</span></li>
  <li><b>the product of the slopes</b><span>qiyaliklarning koʻpaytmasi (= −1)</span></li>
  <li><b>at a right angle</b><span>toʻgʻri burchak ostida</span></li>
  <li><b>which of the following could be</b><span>qaysi biri boʻlishi mumkin</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">40 s</span></p>
  <div class="ps-stem__q">
    <p>What is the slope of a line perpendicular to the line
    <i>y</i> = (3/5)<i>x</i> − 2?</p>
  </div>
  <ol class="ps-ch">
    <li>−5/3</li>
    <li>−3/5</li>
    <li>3/5</li>
    <li>5/3</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) −5/3</p>
      <p>3/5 ni agʻdaramiz → 5/3, ishorani almashtiramiz → −5/3.</p>
      <p>Tekshiruv: (3/5) × (−5/3) = −1 ✓ — bu koʻpaytirish har doim 5 soniya oladi va
      javobni tasdiqlaydi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">−3/5</span>
  <span class="ps-trap__why">Faqat ishora almashtirilgan, kasr agʻdarilmagan. Tekshiring:
  (3/5) × (−3/5) = −9/25, bu −1 emas.</span>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">5/3</span>
  <span class="ps-trap__why">Faqat agʻdarilgan, ishora almashtirilmagan. Ikkala amal ham
  kerak — nomining oʻzida turibdi: <b>negative</b> reciprocal.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">80 s</span></p>
  <div class="ps-stem__q">
    <p>Line <i>n</i> passes through the point (4, −1) and is perpendicular to the line
    <i>y</i> = 2<i>x</i> + 9. Which equation represents line <i>n</i>?</p>
  </div>
  <ol class="ps-ch">
    <li><i>y</i> = −(1/2)<i>x</i> − 3</li>
    <li><i>y</i> = −(1/2)<i>x</i> + 1</li>
    <li><i>y</i> = (1/2)<i>x</i> + 1</li>
    <li><i>y</i> = 2<i>x</i> − 9</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) y = −(1/2)x + 1</p>
      <div class="pm-solve">
        <div class="pm-solve__row">
          <span class="pm-solve__step">m = −1/2</span>
          <span class="pm-solve__why">2 ni agʻdardik va ishorani almashtirdik</span>
        </div>
        <div class="pm-solve__row pm-solve__row--ans">
          <span class="pm-solve__step">−1 = −(1/2)(4) + b  →  −1 = −2 + b  →  b = 1</span>
          <span class="pm-solve__why">Nuqtani qoʻydik</span>
        </div>
      </div>
      <p>Ikki javob bir xil qiyalikka ega — ularni faqat <b>b</b> ajratadi, shuning uchun
      nuqtani qoʻyish qadamini tashlab boʻlmaydi.</p>
    </div>
  </details>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Qiyalik savollarida ikki filtr javoblarning yarmini darhol oʻchiradi:</p>
  <ol>
    <li><b>Ishora:</b> perpendikulyar qiyalikning ishorasi berilganiga <u>qarama-qarshi</u>
        boʻlishi shart.</li>
    <li><b>Kattalik:</b> berilgani 1 dan katta boʻlsa, javob 1 dan kichik boʻladi
        (va aksincha).</li>
  </ol>
  <p>Keyin qolganini koʻpaytirib tekshiring: −1 chiqmasa, javob emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">y = 3x ga perpendikulyar chiziqning qiyaligi −3.</p>
  <p class="pe-good">Qiyaligi −1/3.</p>
  <p class="pe-fix__why">Faqat ishora almashtirilgan. 3 × (−3) = −9, −1 emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Perpendikulyar chiziqlarning qiyaliklari yigʻindisi −1.</p>
  <p class="pe-good">Ularning <b>koʻpaytmasi</b> −1.</p>
  <p class="pe-fix__why">2 va −1/2 uchun yigʻindi 1.5, koʻpaytma esa −1. Qoida
  koʻpaytirish haqida.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Perpendikulyar chiziqlar har doim <b>kesishadi</b> — demak ularning sistemasi
  bitta yechimga ega. Parallel chiziqlar bilan aynan shu joyda farq qiladi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  What is the slope of a line perpendicular to <i>y</i> = −5<i>x</i> + 2?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">1/5 — −5 ni agʻdarsak −1/5, ishorani almashtirsak +1/5.
  Tekshiruv: −5 × 1/5 = −1 ✓</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Two lines have slopes 2/7 and −7/2. Are they perpendicular?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ha — (2/7) × (−7/2) = −14/14 = −1. Koʻpaytma −1, demak toʻgʻri
  burchak ostida kesishadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  What is the slope of a line perpendicular to <i>y</i> = 6?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Undefined — <i>y</i> = 6 gorizontal, unga perpendikulyar chiziq
  vertikal. Formula bilan emas, rasm bilan hal qilinadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  A line perpendicular to <i>y</i> = −(1/3)<i>x</i> passes through (0, 7). Write its
  equation.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>y</i> = 3<i>x</i> + 7 — −1/3 ni agʻdarsak −3, ishorani
  almashtirsak 3; nuqta y oʻqida, demak b = 7.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A path meets a straight canal at a right angle. The canal has a slope of 2/5.
  What is the slope of the path?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">−5/2 — agʻdaramiz (5/2) va ishorani almashtiramiz.
  Tekshiruv: (2/5) × (−5/2) = −1 ✓</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>perpendicular</b><span>perpendikulyar; toʻgʻri burchak ostida</span></li>
  <li><b>negative reciprocal</b><span>manfiy teskari son</span></li>
  <li><b>reciprocal</b><span>teskari son (kasrni agʻdarish)</span></li>
  <li><b>the product of</b><span>…ning koʻpaytmasi</span></li>
  <li><b>right angle</b><span>toʻgʻri burchak</span></li>
  <li><b>horizontal / vertical</b><span>gorizontal / vertikal</span></li>
  <li><b>undefined slope</b><span>aniqlanmagan qiyalik (vertikal chiziq)</span></li>
  <li><b>intersect at</b><span>… nuqtada kesishadi</span></li>
  <li><b>flip the fraction</b><span>kasrni agʻdarish</span></li>
  <li><b>opposite sign</b><span>qarama-qarshi ishora</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Agʻdaring va ishorani almashtiring</b> — ikkala amal ham, birdan.</li>
    <li>Tekshiruv bir soniya: qiyaliklar koʻpaytmasi <b>−1</b> boʻlishi shart.</li>
    <li>Gorizontal (0) va vertikal (undefined) — istisno: perpendikulyar, lekin
        koʻpaytma qoidasi ularga qoʻllanmaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-13 — multi-step linear inequalities
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-13: Solving Multi-Step Linear Inequalities",
        "category": "math",
        "order": 13,
        "summary": (
            "Tengsizlik tenglama kabi yechiladi — bitta yangi qoida bilan: manfiy songa "
            "koʻpaytirilganda yoki boʻlinganda belgi agʻdariladi. Javob son emas, "
            "sonlar toʻplami."
        ),
        "stories": ["Eighty-Five Percent"],
        "content": """
<h2>SAT-13: Solving Multi-Step Linear Inequalities</h2>

<p>Yaxshi yangilik: tengsizlikni yechish tenglamani yechish bilan deyarli bir xil —
SAT-2 dagi hamma qadam oʻz oʻrnida qoladi. Yomon yangilik: bitta qoʻshimcha qoida bor,
va uni unutgan oʻquvchi <mark>toʻgʻri sonni topib, notoʻgʻri tomonni belgilaydi</mark>.
Bu dars aynan oʻsha bitta qoida haqida.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>toʻrtta belgini (&lt; ≤ &gt; ≥) va ularning inglizcha nomlarini bilasiz;</li>
    <li>koʻp qadamli tengsizlikni yechasiz;</li>
    <li>manfiy songa boʻlganda belgini <u>agʻdarasiz</u>;</li>
    <li>javobni sonlar oʻqida koʻrsatasiz va «eng katta butun son» savoliga javob berasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The one new rule</span>
  <span class="pe-chip pe-chip--neg">× yoki ÷ manfiy songa</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">belgi agʻdariladi</span>
  <span class="pe-chip pe-chip--opt">&lt; ↔ &gt; · ≤ ↔ ≥</span>
</div>

<h3>Toʻrtta belgi va ularning tili</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Belgi</th><th>Inglizcha</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pm-word__sym">&lt;</td><td>less than</td><td>…dan kichik</td></tr>
  <tr><td class="pm-word__sym">≤</td><td>at most · no more than</td><td>koʻpi bilan; …dan oshmaydi</td></tr>
  <tr><td class="pm-word__sym">&gt;</td><td>more than · greater than</td><td>…dan katta</td></tr>
  <tr><td class="pm-word__sym">≥</td><td>at least · no less than</td><td>kamida; …dan kam emas</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <em>At least</em> — «kamida», yaʼni <b>≥</b>. <em>At most</em> — «koʻpi bilan», yaʼni
  <b>≤</b>. Bu ikkisini adashtirish SAT-15 dagi matnli masalalarda toʻgʻridan-toʻgʻri
  notoʻgʻri javobga olib boradi, shuning uchun ularni hozir yod oling.
</div>

<h3>Nega manfiy son belgini agʻdaradi</h3>

<p>Oddiy misolga qarang: <strong>3 &lt; 5</strong>, rost. Endi ikkala tomonni −1 ga
koʻpaytiring: −3 va −5. Lekin −3 <u>kattaroq</u>, −5 esa kichikroq. Demak
<strong>−3 &gt; −5</strong> — belgi agʻdarildi.</p>

<div class="pm-num">
  <div class="pm-num__track">
    <span class="pm-num__tick" style="left:0%"><i>−6</i></span>
    <span class="pm-num__tick" style="left:25%"><i>−3</i></span>
    <span class="pm-num__tick" style="left:50%"><i>0</i></span>
    <span class="pm-num__tick" style="left:75%"><i>3</i></span>
    <span class="pm-num__tick" style="left:100%"><i>6</i></span>
    <span class="pm-num__dot" style="left:8.3%"><i>−5</i></span>
    <span class="pm-num__dot" style="left:75%"><i>3</i></span>
  </div>
</div>

<p>Manfiy tomonda tartib teskari boʻladi — mana shuning uchun qoida bor. Qoʻshish va
ayirishda hech narsa oʻzgarmaydi; faqat <b>manfiy songa koʻpaytirish yoki boʻlish</b>
belgini agʻdaradi.</p>

<h3>Misol 1 (oson)</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x + 7 &lt; 22</span>
    <span class="pm-solve__why">Berilgan tengsizlik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x &lt; 15</span>
    <span class="pm-solve__why">7 ni ayirdik — belgi oʻzgarmaydi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x &lt; 5</span>
    <span class="pm-solve__why">3 ga boʻldik; 3 musbat, demak belgi oʻsha</span>
  </div>
</div>

<h3>Misol 2 (oʻrta) — agʻdarish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">−2x + 5 ≥ 11</span>
    <span class="pm-solve__why">Berilgan tengsizlik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">−2x ≥ 6</span>
    <span class="pm-solve__why">5 ni ayirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x ≤ −3</span>
    <span class="pm-solve__why">−2 ga boʻldik — <b>manfiy</b>, shuning uchun ≥ belgisi ≤ ga aylandi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>x = −4 olamiz (u −3 dan kichik): −2(−4) + 5 = 8 + 5 = 13 ≥ 11 ✓. Endi x = 0 olamiz:
  5 ≥ 11 ✗ — demak toʻplam haqiqatan chap tomonda.</p>
</div>

<h3>Misol 3 (SAT darajasi)</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">4(x − 3) &gt; 2x + 6</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4x − 12 &gt; 2x + 6</span>
    <span class="pm-solve__why">Qavs ochildi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2x &gt; 18  →  x &gt; 9</span>
    <span class="pm-solve__why">2x ni ayirdik, 12 ni qoʻshdik, 2 ga boʻldik — musbat, agʻdarish yoʻq</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Agʻdarishdan qochishning oson yoʻli bor: harfli hadni <b>kattaroq</b> tomonga yigʻing.
  −2x ≥ 6 oʻrniga tenglamani boshidan boshqa tomonga yigʻsangiz, manfiy koeffitsient
  umuman paydo boʻlmaydi.
</div>

<h3>Javob — son emas, toʻplam</h3>

<p>Tenglamaning javobi bitta son edi. Tengsizlikning javobi — <strong>cheksiz koʻp
son</strong>. Shuning uchun SAT koʻpincha oxirgi qadamni qoʻshadi: <em>«what is the
greatest integer value of x?»</em> Bunda javobingizni yana bir marta oʻqing:
<em>x</em> &lt; 6 boʻlsa, eng katta <b>butun</b> son 6 emas, <b>5</b>.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Tengsizlikning javobini <b>har doim</b> bitta son bilan tekshirish mumkin — bu
  tenglamada yoʻq imkoniyat. Javob <em>x</em> ≥ −5 boʻlsa, x = 0 ni asl tengsizlikka
  qoʻying: rost chiqishi kerak. Notoʻgʻri tomonni belgilagan boʻlsangiz, shu yerda
  bilinadi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>which describes all possible values of x</b><span>x ning barcha qiymatlari qaysi javobda</span></li>
  <li><b>the greatest integer value</b><span>eng katta butun son — chegaradan bittaga kichik boʻlishi mumkin</span></li>
  <li><b>the least possible value</b><span>eng kichik mumkin boʻlgan qiymat</span></li>
  <li><b>satisfies the inequality</b><span>tengsizlikni qanoatlantiradi</span></li>
  <li><b>solution set</b><span>yechimlar toʻplami</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>Which of the following describes all values of <i>x</i> for which
    −3<i>x</i> + 4 ≤ 19?</p>
  </div>
  <ol class="ps-ch">
    <li><i>x</i> ≤ −5</li>
    <li><i>x</i> ≥ −5</li>
    <li><i>x</i> ≤ 5</li>
    <li><i>x</i> ≥ 5</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) x ≥ −5</p>
      <div class="pm-solve">
        <div class="pm-solve__row">
          <span class="pm-solve__step">−3x ≤ 15</span>
          <span class="pm-solve__why">4 ni ayirdik</span>
        </div>
        <div class="pm-solve__row pm-solve__row--ans">
          <span class="pm-solve__step">x ≥ −5</span>
          <span class="pm-solve__why">−3 ga boʻldik — belgi agʻdarildi</span>
        </div>
      </div>
      <p>Tekshiruv: x = 0 olamiz. −3(0) + 4 = 4 ≤ 19 ✓, va 0 haqiqatan −5 dan katta.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">x ≤ −5</span>
  <span class="ps-trap__why">Son toʻgʻri, tomon notoʻgʻri: manfiy songa boʻlganda belgi
  agʻdarilishi unutilgan. Bitta son qoʻyib tekshirish (x = 0) shu xatoni har safar
  fosh qiladi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>What is the greatest integer value of <i>x</i> that satisfies 5<i>x</i> − 3 &lt; 27?</p>
  </div>
  <ol class="ps-ch">
    <li>4.8</li>
    <li>5</li>
    <li>6</li>
    <li>30</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 5</p>
      <p>5<i>x</i> &lt; 30, demak <i>x</i> &lt; 6. Belgi <b>qatʼiy</b> (&lt;), shuning
      uchun 6 ning oʻzi yaramaydi va eng katta butun son — <b>5</b>.</p>
      <p>Tekshiruv: 5(5) − 3 = 22 &lt; 27 ✓, 5(6) − 3 = 27, bu 27 dan kichik emas ✗</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">6</span>
  <span class="ps-trap__why">Chegaraning oʻzi belgilangan. &lt; va ≤ farqi aynan shu
  yerda pul turadi: qatʼiy belgida chegara <b>ichkariga kirmaydi</b>.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Tengsizlik javoblari toʻrtta oraliq boʻlsa, yechmasdan ham boʻladi:</p>
  <ol>
    <li>Bitta oson son tanlang (koʻpincha <b>0</b>).</li>
    <li>Uni berilgan tengsizlikka qoʻying — rostmi yoki yolgʻon?</li>
    <li>Shu natijaga mos kelmagan javoblarni oʻchiring; odatda bittasi qoladi.</li>
  </ol>
  <p>Bu usul agʻdarish xatosini butunlay chetlab oʻtadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">−x &gt; 5  →  x &gt; −5</p>
  <p class="pe-good">−x &gt; 5  →  x &lt; −5</p>
  <p class="pe-fix__why">Ikkala tomon −1 ga boʻlindi — bu manfiy son, demak belgi
  agʻdariladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">x &lt; 6 boʻlsa, eng katta butun son 6.</p>
  <p class="pe-good">Eng katta butun son <b>5</b>.</p>
  <p class="pe-fix__why">6 ning oʻzi toʻplamga kirmaydi, chunki belgi &lt;, ≤ emas.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qoʻshish va ayirish belgini <b>hech qachon</b> agʻdarmaydi. Faqat manfiy songa
  koʻpaytirish yoki boʻlish. Koʻp oʻquvchi «manfiy son koʻrsam agʻdaraman» deb yodlab,
  −5 ni ayirganda ham agʻdarib yuboradi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Solve: <i>x</i> + 6 &gt; 10</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> &gt; 4 — 6 ni ayirdik; qoʻshish/ayirish belgini
  oʻzgartirmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Solve: 4<i>x</i> ≤ −12</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> ≤ −3 — 4 ga boʻldik. 4 musbat, demak belgi oʻsha
  qoladi, javobning oʻzi manfiy boʻlsa ham.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Solve: −<i>x</i> &gt; 5</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> &lt; −5 — ikkala tomonni −1 ga boʻldik, belgi
  agʻdarildi. Tekshiruv: x = −6 boʻlsa, −(−6) = 6 &gt; 5 ✓</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Solve: 2(<i>x</i> + 3) ≥ 4<i>x</i> − 2</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> ≤ 4 — 2x + 6 ≥ 4x − 2 → 8 ≥ 2x → 4 ≥ x. Harfni
  oʻngda qoldirsangiz agʻdarish umuman kerak boʻlmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A taxi charges $5 plus $3 per kilometre. A passenger has at most $26. What is the
  greatest number of whole kilometres they can travel?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">7 km — 3<i>n</i> + 5 ≤ 26 → 3<i>n</i> ≤ 21 → <i>n</i> ≤ 7.
  Bu yerda 7 ning oʻzi ham mumkin, chunki belgi ≤.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>inequality</b><span>tengsizlik</span></li>
  <li><b>at least</b><span>kamida (≥)</span></li>
  <li><b>at most / no more than</b><span>koʻpi bilan (≤)</span></li>
  <li><b>greater than / less than</b><span>…dan katta / kichik</span></li>
  <li><b>flip / reverse the sign</b><span>belgini agʻdarish</span></li>
  <li><b>solution set</b><span>yechimlar toʻplami</span></li>
  <li><b>satisfies</b><span>qanoatlantiradi</span></li>
  <li><b>greatest integer value</b><span>eng katta butun qiymat</span></li>
  <li><b>strict inequality</b><span>qatʼiy tengsizlik (&lt; yoki &gt;)</span></li>
  <li><b>all possible values</b><span>barcha mumkin boʻlgan qiymatlar</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Faqat <b>manfiy songa koʻpaytirish yoki boʻlish</b> belgini agʻdaradi —
        qoʻshish va ayirish emas.</li>
    <li>Javob bitta son emas, <b>toʻplam</b>. Bitta son qoʻyib tekshirish 5 soniya.</li>
    <li>«Eng katta butun son» soʻralganda <b>qatʼiy belgiga</b> qarang: x &lt; 6 uchun
        javob 5.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-14 — graphing linear inequalities
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-14: Graphing Linear Inequalities on the Coordinate Plane",
        "category": "math",
        "order": 14,
        "summary": (
            "Tengsizlikning grafigi — chiziq emas, tekislikning yarmi. Chiziq uzluksiz "
            "yoki uzuq boʻlishi, qaysi tomon shtrixlanishi va sinov nuqtasi bilan "
            "tekshirish."
        ),
        "stories": ["Where You May Camp"],
        "content": """
<h2>SAT-14: Graphing Linear Inequalities on the Coordinate Plane</h2>

<p>Tenglamaning grafigi — chiziq. Tengsizlikning grafigi — <mark>tekislikning butun bir
yarmi</mark>, chunki shartni cheksiz koʻp nuqta qanoatlantiradi. SAT bu mavzuni ikki
koʻrinishda soʻraydi: «qaysi grafik shu tengsizlikni ifodalaydi» va «qaysi nuqta
yechim boʻladi». Ikkalasi ham ikki qadamda hal qilinadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>chegara chizigʻini toʻgʻri chizasiz — uzluksiz yoki uzuq;</li>
    <li>qaysi tomonni shtrixlashni sinov nuqtasi bilan aniqlaysiz;</li>
    <li>berilgan nuqta yechim yoki yoʻqligini 10 soniyada tekshirasiz;</li>
    <li>«y &gt; …» va «y &lt; …» ni yuqori/quyi tomon bilan bogʻlaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Two decisions</span>
  <span class="pe-chip pe-chip--s">chiziq</span>
  <span class="pe-op">:</span>
  <span class="pe-chip pe-chip--opt">≤ ≥ uzluksiz · &lt; &gt; uzuq</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">tomon</span>
  <span class="pe-op">:</span>
  <span class="pe-chip pe-chip--opt">sinov nuqtasi</span>
</div>

<h3>Qadam 1 — chegara chizigʻi</h3>

<p>Tengsizlik belgisini vaqtincha <b>tenglik</b> deb oʻqing va shu chiziqni chizing
(SAT-9 dagi usullar bilan). Keyin chiziqning turini belgi hal qiladi:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">≤ yoki ≥ — uzluksiz</p>
    <p>Chiziqning oʻzidagi nuqtalar ham yechim, chunki tenglik ruxsat etilgan.
    <b>Solid line.</b></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">&lt; yoki &gt; — uzuq</p>
    <p>Chiziqning oʻzi yechim emas — u faqat chegara. <b>Dashed line.</b></p>
  </div>
</div>

<h3>Qadam 2 — qaysi tomon</h3>

<p>Eng ishonchli usul — <strong>sinov nuqtasi</strong>. Chiziq ustida yotmagan istalgan
nuqtani oling (deyarli har doim <b>(0, 0)</b> eng qulayi), uni tengsizlikka qoʻying va
soʻrang: rostmi?</p>

<ul>
  <li><strong>Rost</strong> → oʻsha nuqta turgan tomon shtrixlanadi.</li>
  <li><strong>Yolgʻon</strong> → boshqa tomon shtrixlanadi.</li>
</ul>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">y ≥ 2x − 3</span>
    <span class="pm-solve__why">Chegara: y = 2x − 3, belgi ≥ — chiziq <b>uzluksiz</b></span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(0, 0): 0 ≥ 2(0) − 3</span>
    <span class="pm-solve__why">Sinov nuqtasini qoʻydik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">0 ≥ −3 — rost</span>
    <span class="pm-solve__why">Demak (0, 0) turgan tomon, yaʼni chiziqning ustki tomoni shtrixlanadi</span>
  </div>
</div>

<figure class="pm-fig">
  <svg viewBox="0 0 320 200" role="img" aria-label="Uzuq chegara chizigʻi va shtrixlangan yarim tekislik">
    <polygon class="pm-fill pm-fill--hl" points="30,30 250,30 30,160"/>
    <line class="pm-ln" x1="20" y1="160" x2="300" y2="160"/>
    <line class="pm-ln" x1="55" y1="15" x2="55" y2="190"/>
    <line class="pm-ln pm-ln--hl pm-ln--dash" x1="30" y1="30" x2="255" y2="172"/>
    <circle class="pm-pt" cx="100" cy="90" r="4"/>
    <text class="pm-lbl pm-lbl--hl" x="108" y="86">sinov nuqtasi</text>
    <text class="pm-lbl" x="196" y="52">shtrixlangan</text>
    <text class="pm-lbl" x="284" y="178">x</text>
  </svg>
  <figcaption>Uzuq chiziq — chegara yechimga kirmaydi; shtrixlangan yarim tekislik esa kiradi.</figcaption>
</figure>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Sinov nuqtasi sifatida <b>(0, 0)</b> ni oling — hisob deyarli oʻz-oʻzidan chiqadi.
  Yagona istisno: chiziq aynan boshdan oʻtsa (b = 0). Unda (1, 0) yoki (0, 1) ni oling.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Uzuq chiziq «bu yergacha, lekin bu chiziqning oʻzi emas» degani. Oʻzbekchada buni
  «chegara ichkariga kirmaydi» deb oʻqing — xuddi SAT-13 dagi qatʼiy belgi kabi.
  Ikkalasi bir xil gʻoya, ikki xil rasm.
</div>

<h3>Tez usul: y ga yechilgan boʻlsa</h3>

<p>Agar tengsizlik allaqachon <em>y</em> ga yechilgan boʻlsa, sinov nuqtasi ham kerak
emas:</p>

<div class="pe-ex">
  <p class="pe-ex__math">y &gt; mx + b  →  chiziqning USTKI tomoni</p>
  <p class="pe-ex__uz">«y kattaroq» — demak yuqoriroq nuqtalar.</p>
  <p class="pe-ex__why">y &lt; mx + b esa pastki tomon. Bu faqat y yolgʻiz qolganda ishlaydi.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Bu tez usul <b>faqat</b> <i>y</i> chap tomonda yolgʻiz turganda toʻgʻri. −2<i>y</i> &gt; 4
  koʻrinishida boʻlsa, avval yeching (belgi agʻdariladi, SAT-13) va keyingina «yuqori/quyi»
  deb ayting.
</div>

<h3>Misol (SAT darajasi) — standart shakl</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + 3y &lt; 12</span>
    <span class="pm-solve__why">Chegara: 2x + 3y = 12; belgi &lt; — chiziq <b>uzuq</b></span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Kesishmalar: (6, 0) va (0, 4)</span>
    <span class="pm-solve__why">SAT-8 dagi usul — chiziq shu ikki nuqtadan chiziladi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">(0, 0): 0 &lt; 12 — rost</span>
    <span class="pm-solve__why">Boshni oʻz ichiga olgan tomon shtrixlanadi</span>
  </div>
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>which graph represents the inequality</b><span>qaysi grafik shu tengsizlikni ifodalaydi</span></li>
  <li><b>a solid / dashed boundary line</b><span>uzluksiz / uzuq chegara chizigʻi</span></li>
  <li><b>the shaded region</b><span>shtrixlangan soha — yechimlar toʻplami</span></li>
  <li><b>which point is a solution</b><span>qaysi nuqta yechim boʻladi</span></li>
  <li><b>lies in the solution set</b><span>yechimlar toʻplamiga tegishli</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>Which of the following describes the graph of <i>y</i> &lt; −<i>x</i> + 4 in the
    <i>xy</i>-plane?</p>
  </div>
  <ol class="ps-ch">
    <li>A dashed line with the region below it shaded</li>
    <li>A dashed line with the region above it shaded</li>
    <li>A solid line with the region below it shaded</li>
    <li>A solid line with the region above it shaded</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) uzuq chiziq, pastki tomon shtrixlangan</p>
      <p>Belgi <b>&lt;</b> — qatʼiy, demak chegara chizigʻi <b>uzuq</b>. <i>y</i> yolgʻiz
      turibdi va «kichik» deyilgan — demak chiziqning <b>pastki</b> tomoni.</p>
      <p>Tekshiruv: (0, 0) → 0 &lt; 4 rost, va boshlangʻich nuqta haqiqatan chiziqdan
      pastda.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">solid line, below</span>
  <span class="ps-trap__why">Tomon toʻgʻri, chiziq notoʻgʻri. Uzluksiz chiziq faqat
  ≤ va ≥ da boʻladi; qatʼiy belgida chegara yechim emas.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>Which of the following points is a solution to the inequality
    <i>y</i> ≥ 2<i>x</i> − 6?</p>
  </div>
  <ol class="ps-ch">
    <li>(0, −7)</li>
    <li>(1, −5)</li>
    <li>(2, −3)</li>
    <li>(3, 1)</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: D) (3, 1)</p>
      <p>Har bir nuqtani qoʻyib chiqamiz — bu savol turi har doim shunday yechiladi:</p>
      <div class="pm-solve">
        <div class="pm-solve__row">
          <span class="pm-solve__step">(3, 1): 2(3) − 6 = 0, va 1 ≥ 0</span>
          <span class="pm-solve__why">Rost ✓</span>
        </div>
        <div class="pm-solve__row">
          <span class="pm-solve__step">(0, −7): −7 ≥ −6</span>
          <span class="pm-solve__why">Yolgʻon — −7 kichikroq</span>
        </div>
        <div class="pm-solve__row">
          <span class="pm-solve__step">(2, −3): −3 ≥ −2</span>
          <span class="pm-solve__why">Yolgʻon</span>
        </div>
      </div>
      <p>Manfiy sonlarni taqqoslashda ehtiyot boʻling: −7 −6 dan <b>kichik</b>.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">(2, −3)</span>
  <span class="ps-trap__why">Hisob toʻgʻri (2 × 2 − 6 = −2), lekin manfiy sonlar
  taqqoslanganda adashilgan: −3 −2 dan <b>kichik</b>, demak −3 ≥ −2 yolgʻon. Manfiy
  tomonda «kattaroq» nolga yaqinroq degani.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>«Qaysi nuqta yechim?» savolida hech narsa chizmang:</p>
  <ol>
    <li>Har bir nuqtaning koordinatalarini tengsizlikka qoʻying.</li>
    <li>Chap va oʻng tomonni hisoblang, keyin belgini tekshiring.</li>
    <li>Rost chiqqani — javob. Odatda ikkinchi yoki uchinchi urinishda topiladi.</li>
  </ol>
  <p>Grafik savolida esa teskarisi: avval <b>chiziq turi</b> (uzuq/uzluksiz) bilan yarmini
  oʻchiring, keyin (0, 0) bilan tomonni tanlang.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">y &gt; 2x + 1 uchun chiziq uzluksiz chiziladi.</p>
  <p class="pe-good">Uzuq (dashed) chiziladi.</p>
  <p class="pe-fix__why">&gt; qatʼiy belgi — chegaradagi nuqtalar yechim emas. Uzluksiz
  chiziq faqat ≥ va ≤ da.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">−2y &gt; 4  →  chiziqning ustki tomoni</p>
  <p class="pe-good">Avval yeching: y &lt; −2 → <b>pastki</b> tomon.</p>
  <p class="pe-fix__why">«Yuqori/quyi» qoidasi faqat <i>y</i> yolgʻiz qolganda ishlaydi,
  va bu yerda boʻlishda belgi ham agʻdarildi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Shtrixlangan soha — bu <b>yechimlar toʻplami</b>: undagi har bir nuqta tengsizlikni
  qanoatlantiradi. Shuning uchun «qaysi nuqta yechim» savoli aslida «qaysi nuqta
  shtrixlangan sohada yotadi» degani.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Is the boundary line of <i>y</i> ≤ 3<i>x</i> + 2 solid or dashed?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Uzluksiz (solid) — ≤ belgisi tenglikni ham qamrab oladi,
  demak chiziqning oʻzi ham yechim.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Is (0, 0) a solution of <i>y</i> &gt; <i>x</i> + 1?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — 0 &gt; 0 + 1 yaʼni 0 &gt; 1, bu yolgʻon. Demak
  shtrixlash boshning <b>boshqa</b> tomonida.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Is (5, 2) a solution of 2<i>x</i> + <i>y</i> ≤ 12?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ha — 2(5) + 2 = 12, va 12 ≤ 12 rost. Chegaradagi nuqta ham
  yechim, chunki belgi ≤.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  For <i>y</i> &lt; 4, which region is shaded and what kind of line is drawn?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Uzuq gorizontal chiziq <i>y</i> = 4, va uning <b>pastki</b>
  tomoni shtrixlanadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A shop's delivery zone is described by <i>y</i> ≤ 8 − <i>x</i>, where the numbers are
  kilometres east and north of the shop. Is a house at (3, 6) inside the zone?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — 8 − 3 = 5, va 6 ≤ 5 yolgʻon. Uy chegaradan tashqarida
  qoladi.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>boundary line</b><span>chegara chizigʻi</span></li>
  <li><b>solid line</b><span>uzluksiz chiziq (≤, ≥)</span></li>
  <li><b>dashed line</b><span>uzuq chiziq (&lt;, &gt;)</span></li>
  <li><b>shaded region</b><span>shtrixlangan soha</span></li>
  <li><b>test point</b><span>sinov nuqtasi</span></li>
  <li><b>half-plane</b><span>yarim tekislik</span></li>
  <li><b>solution set</b><span>yechimlar toʻplami</span></li>
  <li><b>above / below the line</b><span>chiziqning ustida / ostida</span></li>
  <li><b>lies in</b><span>… ichida yotadi</span></li>
  <li><b>strict inequality</b><span>qatʼiy tengsizlik</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Belgi chiziqni hal qiladi: <b>≤ ≥ uzluksiz</b>, <b>&lt; &gt; uzuq</b>.</li>
    <li>Tomonni <b>(0, 0)</b> bilan tekshiring — rost boʻlsa, oʻsha tomon.</li>
    <li>«Qaysi nuqta yechim» — chizmasdan, har bir nuqtani <b>qoʻyib</b> koʻring.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-15 — modelling with inequalities
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-15: Modeling Real-World Scenarios with Inequalities",
        "category": "math",
        "order": 15,
        "summary": (
            "Byudjet, chegara, minimal talab — matndan tengsizlik tuzish va javobni "
            "toʻgʻri tomonga yaxlitlash. SAT'ning sevimli oxirgi qadami aynan shu "
            "yaxlitlash."
        ),
        "stories": ["Nine Boxes and a Coach"],
        "content": """
<h2>SAT-15: Modeling Real-World Scenarios with Inequalities</h2>

<p>Hayotda «roppa-rosa» degan narsa kam: pul <em>yetadi yoki yetmaydi</em>, yuk
<em>sigʻadi yoki sigʻmaydi</em>, ball <em>yetarli yoki yetarli emas</em>. Shuning uchun
SAT'ning matnli masalalarida tengsizlik tenglamadan kam uchramaydi. Va bu savollarning
deyarli hammasida oxirgi qadam bir xil: <mark>javobni butun songa toʻgʻri tomonga
yaxlitlash</mark>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>«at least», «at most», «no more than» iboralarini belgiga aylantirasiz;</li>
    <li>byudjet va chegara masalalarining tengsizligini tuzasiz;</li>
    <li>javobni <u>qaysi tomonga</u> yaxlitlashni bilasiz;</li>
    <li>javobni vaziyatga qaytarib tekshirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The budget model</span>
  <span class="pe-chip pe-chip--o">boshlangʻich</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">narx</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">soni</span>
  <span class="pe-op">≤</span>
  <span class="pe-chip pe-chip--o">chegara</span>
</div>

<h3>Ibora → belgi</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Testda shunday deyiladi</th><th>Belgi</th><th>Maʼnosi</th></tr>
  <tr><td>at most · no more than · cannot exceed</td><td class="pm-word__sym">≤</td><td>koʻpi bilan</td></tr>
  <tr><td>at least · no less than · a minimum of</td><td class="pm-word__sym">≥</td><td>kamida</td></tr>
  <tr><td>more than · exceeds</td><td class="pm-word__sym">&gt;</td><td>…dan koʻp</td></tr>
  <tr><td>fewer than · under</td><td class="pm-word__sym">&lt;</td><td>…dan kam</td></tr>
  <tr><td>a budget of · up to</td><td class="pm-word__sym">≤</td><td>shuncha pulgacha</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <em>Exceed</em> — «oshib ketmoq». <em>Cannot exceed 850</em> degani 850 <b>ham
  mumkin</b>, yaʼni ≤ 850. Aksincha <em>exceeds 850</em> — 850 dan qatʼiy koʻp, &gt; 850.
  Bitta «cannot» butun belgini oʻzgartiradi.
</div>

<h3>Misol 1 (oson) — byudjet</h3>

<p><em>A club has $200 for T-shirts. Each shirt costs $12, and the printer charges a
one-time $25 setup fee. What is the greatest number of shirts the club can buy?</em></p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">12n + 25 ≤ 200</span>
    <span class="pm-solve__why">n — futbolkalar soni; «has $200» — pul yetishi kerak</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">12n ≤ 175</span>
    <span class="pm-solve__why">Bir martalik $25 ni ayirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">n ≤ 14.58…</span>
    <span class="pm-solve__why">12 ga boʻldik (musbat — agʻdarish yoʻq)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">n = 14</span>
    <span class="pm-solve__why">Yarim futbolka boʻlmaydi, va 15 ta pulga sigʻmaydi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>14 ta: 12 × 14 + 25 = 168 + 25 = 193 ≤ 200 ✓. 15 ta: 180 + 25 = 205 &gt; 200 ✗ —
  demak 14 haqiqatan chegara.</p>
</div>

<h3>⚠️ Yaxlitlash tomoni — SAT shu yerda kutadi</h3>

<blockquote>Javob <strong>≤</strong> bilan chiqsa (byudjet, sigʻim, chegara) —
<b>pastga</b> yaxlitlang. Javob <strong>≥</strong> bilan chiqsa (kamida, minimal talab) —
<b>yuqoriga</b> yaxlitlang. Odatdagi «0.5 dan katta boʻlsa yuqoriga» qoidasi bu yerda
<u>ishlamaydi</u>.</blockquote>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">n ≤ 14.58 → 14</p>
    <p>15 ta olish uchun pul yetmaydi. Pastga yaxlitlanadi, garchi 0.58 «yarimdan koʻp»
    boʻlsa ham.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">t ≥ 11.7 → 12</p>
    <p>11 ta yetmaydi — talab bajarilmaydi. Yuqoriga yaxlitlanadi, garchi 0.7 ni tashlab
    yuborgingiz kelsa ham.</p>
  </div>
</div>

<h3>Misol 2 (oʻrta) — minimal talab</h3>

<p><em>A student has 62 points and needs at least 90 to pass. Each extra task is worth
4 points. How many tasks must the student complete?</em></p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">62 + 4t ≥ 90</span>
    <span class="pm-solve__why">«at least 90» → ≥</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4t ≥ 28</span>
    <span class="pm-solve__why">62 ni ayirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">t ≥ 7</span>
    <span class="pm-solve__why">Bu safar aniq chiqdi — kamida 7 ta topshiriq</span>
  </div>
</div>

<h3>Misol 3 (SAT darajasi) — chirkin son bilan</h3>

<p><em>A student has 18 points and needs at least 100. Each game is worth 7 points.
What is the least number of games?</em></p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">18 + 7g ≥ 100  →  7g ≥ 82</span>
    <span class="pm-solve__why">18 ni ayirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">g ≥ 11.71…</span>
    <span class="pm-solve__why">7 ga boʻldik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">g = 12</span>
    <span class="pm-solve__why">11 ta yetmaydi (18 + 77 = 95), 12 ta yetadi (18 + 84 = 102)</span>
  </div>
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>the greatest number of</b><span>eng koʻpi bilan nechta — ≤ va pastga yaxlitlash</span></li>
  <li><b>the least number of</b><span>kamida nechta — ≥ va yuqoriga yaxlitlash</span></li>
  <li><b>cannot exceed</b><span>oshib ketmasligi kerak (≤)</span></li>
  <li><b>which inequality represents</b><span>qaysi tengsizlik shu vaziyatni ifodalaydi</span></li>
  <li><b>has a budget of</b><span>byudjeti shuncha — pul undan oshmasligi kerak</span></li>
  <li><b>whole number of</b><span>butun sonda — yaxlitlash shart</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>A club has $200 to spend on T-shirts. Each shirt costs $12, and the printer
    charges a one-time setup fee of $25. What is the greatest number of shirts the club
    can buy?</p>
  </div>
  <ol class="ps-ch">
    <li>14</li>
    <li>15</li>
    <li>16</li>
    <li>18</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 14</p>
      <p>12<i>n</i> + 25 ≤ 200 → 12<i>n</i> ≤ 175 → <i>n</i> ≤ 14.58…</p>
      <p>Futbolka butun sonda sotiladi va pul chegara — demak <b>pastga</b>
      yaxlitlanadi.</p>
      <p><b>15</b> — 14.58 ni odatdagidek yuqoriga yaxlitlagan javob, lekin
      15 ta $205 turadi. <b>16</b> — bir martalik $25 ni umuman hisobga olmagan javob
      (200 ÷ 12 = 16.67 → 16).</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">15</span>
  <span class="ps-trap__why">Odatdagi yaxlitlash qoidasi qoʻllangan (0.58 &gt; 0.5).
  Byudjet masalasida yaxlitlash <b>har doim pastga</b>: 15 ta olishga pul yetmaydi.</span>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">16</span>
  <span class="ps-trap__why">Bir martalik $25 ni ayirmagan javob. «One-time» soʻzi
  bitta ayirishni buyuradi (SAT-3).</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">80 s</span></p>
  <div class="ps-stem__q">
    <p>A van can carry a total load of at most 850 kilograms. The driver weighs
    80 kilograms and each box weighs 23 kilograms. What is the greatest number of boxes
    the van can carry?</p>
  </div>
  <ol class="ps-ch">
    <li>33</li>
    <li>34</li>
    <li>36</li>
    <li>37</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 33</p>
      <div class="pm-solve">
        <div class="pm-solve__row">
          <span class="pm-solve__step">80 + 23b ≤ 850</span>
          <span class="pm-solve__why">«at most 850» → ≤; haydovchi ham yukning bir qismi</span>
        </div>
        <div class="pm-solve__row">
          <span class="pm-solve__step">23b ≤ 770  →  b ≤ 33.47…</span>
          <span class="pm-solve__why">80 ni ayirdik, 23 ga boʻldik</span>
        </div>
        <div class="pm-solve__row pm-solve__row--ans">
          <span class="pm-solve__step">b = 33</span>
          <span class="pm-solve__why">33 ta: 759 + 80 = 839 ✓; 34 ta: 782 + 80 = 862 ✗</span>
        </div>
      </div>
      <p><b>36</b> — haydovchining ogʻirligini hisobga olmagan javob
      (850 ÷ 23 = 36.9 → 36).</p>
    </div>
  </details>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Javoblar ketma-ket sonlar boʻlsa (14, 15, 16…), tengsizlik tuzmasangiz ham boʻladi:</p>
  <ol>
    <li>Eng katta javobni oling va vaziyatga qoʻying.</li>
    <li>Chegaradan oshsa — bittaga pastga tushing va yana sinang.</li>
    <li>Birinchi «sigʻgan» son — javob.</li>
  </ol>
  <p>Bu <b>backsolving</b> (SAT-82) ning shu mavzudagi koʻrinishi va yaxlitlash xatosini
  butunlay yoʻq qiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">n ≤ 14.58 → javob 15 (odatdagi yaxlitlash).</p>
  <p class="pe-good">Javob <b>14</b>.</p>
  <p class="pe-fix__why">Chegara masalasida yaxlitlash matematik emas, <b>mantiqiy</b>:
  15 ta pulga sigʻmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">g ≥ 11.71 → javob 11.</p>
  <p class="pe-good">Javob <b>12</b>.</p>
  <p class="pe-fix__why">«Kamida» talabida 11 ta yetmaydi. ≥ har doim <b>yuqoriga</b>
  yaxlitlanadi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Yaxlitlashdan keyin javobni <b>vaziyatga qaytarib</b> tekshiring: chegaraga eng yaqin
  ikki sonni ham sinang. Bu 10 soniya oladi va bu mavzudagi barcha xatolarni tutadi.
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Ba'zan savol sonini emas, <b>pulni</b> yoki <b>vaqtni</b> soʻraydi — u holda
  yaxlitlash umuman kerak emas. Oxirgi jumlani oʻqing: «how many boxes» va «how much
  money» butunlay boshqa javoblar.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Tengsizlik tuzishdan oldin <b>harf nimani bildirishini yozib qoʻying</b> — birligi
  bilan: «b = qutilar soni», «h = soatlar soni». SAT-3 dagi oʻsha qoida bu yerda ikki
  barobar muhim, chunki oxirida yaxlitlash ham shu birlikka bogʻliq.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Write an inequality: «a team needs at least 5 more points».</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>p</i> ≥ 5 — «at least» kamida degani, demak 5 ning oʻzi
  ham mumkin.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Write an inequality: «the bus carries no more than 40 passengers».</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>n</i> ≤ 40 — «no more than» = koʻpi bilan, 40 ta ham
  mumkin.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Notebooks cost $8 each. With $100, what is the greatest whole number that can be
  bought?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">12 ta — 8<i>n</i> ≤ 100 → <i>n</i> ≤ 12.5, va chegara
  masalasi pastga yaxlitlanadi. 13 ta $104 turadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  A worker earns $15 for showing up and $6 per hour. How many hours must they work to
  earn at least $51?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">6 soat — 15 + 6<i>h</i> ≥ 51 → 6<i>h</i> ≥ 36 → <i>h</i> ≥ 6.
  Aniq chiqdi, yaxlitlash kerak emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A garage charges $4 to enter plus $2.50 per hour. With $20, what is the greatest whole
  number of hours a driver can park?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">6 soat — 4 + 2.50<i>h</i> ≤ 20 → 2.50<i>h</i> ≤ 16 →
  <i>h</i> ≤ 6.4, pastga yaxlitlaymiz. Tekshiruv: 6 soat $19, 7 soat $21.50.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>at most / at least</b><span>koʻpi bilan (≤) / kamida (≥)</span></li>
  <li><b>cannot exceed</b><span>oshib ketmasligi kerak (≤)</span></li>
  <li><b>budget</b><span>byudjet; pul chegarasi</span></li>
  <li><b>the greatest number of</b><span>eng koʻp nechta</span></li>
  <li><b>the least number of</b><span>eng kam nechta</span></li>
  <li><b>capacity / load</b><span>sigʻim / yuk</span></li>
  <li><b>whole number</b><span>butun son</span></li>
  <li><b>round down / round up</b><span>pastga / yuqoriga yaxlitlash</span></li>
  <li><b>setup fee</b><span>bir martalik toʻlov</span></li>
  <li><b>per hour / per box</b><span>bir soatga / bir quti uchun</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>at most → ≤</b>, <b>at least → ≥</b>. Bitta soʻz butun masalani hal qiladi.</li>
    <li>Yaxlitlash <b>mantiq boʻyicha</b>: ≤ da pastga, ≥ da yuqoriga — 0.5 qoidasi
        emas.</li>
    <li>Javobni chegaraga qaytarib <b>tekshiring</b>: qoʻshni ikki sonni ham sinang.</li>
  </ul>
</div>
""",
    },
]
