# -*- coding: utf-8 -*-
"""Prime SAT Math — lessons 36–40 (kvadratning tepasi, grafigi va kasrli tenglamalar).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_SAT.md
Lesson list: tutorial/management/commands/toc_prime_sat_math.txt

⚠️ SARLAVHALAR BAZADAN OLINGAN, aynan. Bitta harf oʻzgarsa --republish dublikat
   yaratadi. (2026-09-04: toc dagi 45 ta sarlavha bazadan farq qilardi, tuzatildi.)

⚠️ Kumulyativ (SAT-1…35 erkin: butun Blok A, darajalar, koʻphadlar, ajratish,
   kvadrat formulasi, diskriminant, uchi shakli):
  • SAT-36 — maksimum/minimum matnli masalalarda (daromad, devor, otilgan jism).
  • SAT-37 — parabola grafigi: kesishishlar, uch, simmetriya; qaysi shakl nimani
    koʻrsatadi (SAT-31 nollar, SAT-35 uch).
  • SAT-38 — chiziq va parabola sistemasi; nechta kesishish — diskriminant (SAT-34).
  • SAT-39 — ildizli tenglamalar va begona ildiz; TEKSHIRISH majburiy qadam.
  • SAT-40 — kasrli tenglamalar va aniqlanish sohasi; maxraj nolga aylanmasligi.
  • ⛔ Koʻphadlarni boʻlish (SAT-41) YOʻQ; koʻrsatkichli funksiya (SAT-44) YOʻQ.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_sat_36_40.py \\
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
    # SAT-36 — maximum and minimum values
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-36: Finding Maximum and Minimum Values of a Quadratic",
        "category": "math",
        "order": 36,
        "summary": (
            "«Eng koʻp daromad», «eng katta maydon», «eng baland nuqta» — hammasi "
            "bitta narsani soʻraydi: parabolaning uchini. Qiyin qismi tenglamani "
            "matndan tuzish."
        ),
        "stories": ["The Price of Apricots"],
        "content": """
<h2>SAT-36: Finding Maximum and Minimum Values of a Quadratic</h2>

<p>SAT-35 da uchni tenglamadan topdik. Endi tenglama berilmaydi — <mark>uni matndan
oʻzingiz tuzasiz</mark>. Bu SAT'ning eng qadrli koʻnikmasi: hisoblash oson, jumlani
tenglamaga aylantirish qiyin.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>matnli masaladan kvadrat model tuzasiz;</li>
    <li>uchni topib, savol x ni yoki y ni soʻrayotganini ajratasiz;</li>
    <li>daromad, maydon va balandlik masalalarini bir xil yoʻl bilan yechasiz;</li>
    <li>javobning maʼnosini kontekstda tekshirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Every max/min problem</span>
  <span class="pe-chip pe-chip--v">model tuzing</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">x = −b ÷ (2a)</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">savol nimani soʻradi?</span>
</div>

<h3>1-tur — daromad (revenue)</h3>

<p>Doʻkon choynakni 20 dollardan sotadi va haftasiga 300 dona ketadi. Narxni har
1 dollarga oshirsa, 10 tadan kam sotiladi. Eng koʻp daromad qaysi narxda?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">narx = 20 + x,  soni = 300 − 10x</span>
    <span class="pm-solve__why">x — necha dollarga oshirilgani</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">R = (20 + x)(300 − 10x) = 6000 + 100x − 10x<sup>2</sup></span>
    <span class="pm-solve__why">Daromad = narx × soni (SAT-28)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = −100 ÷ (−20) = 5</span>
    <span class="pm-solve__why">Uchning x koordinatasi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Narx 25 dollar, soni 250, daromad 6250</span>
    <span class="pm-solve__why">x — oshirish, narx esa 20 + 5</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  x = 5 javob <b>emas</b>. x — oshirish miqdori; savol narxni soʻrasa javob 25,
  daromadni soʻrasa 6250. SAT bu uch sonni bir savolda aralashtiradi.
</div>

<h3>2-tur — maydon (area), devor bilan</h3>

<p>Fermerda 40 metr toʻr bor. U devorga tegib turgan toʻrtburchak qafas qurmoqchi,
demak toʻr faqat <b>uch</b> tomonga kerak. Eng katta maydon qancha?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2w + L = 40  →  L = 40 − 2w</span>
    <span class="pm-solve__why">Devor toʻrtinchi tomon — unga toʻr ketmaydi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">A = w(40 − 2w) = 40w − 2w<sup>2</sup></span>
    <span class="pm-solve__why">Maydon = eni × uzunligi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">w = −40 ÷ (−4) = 10</span>
    <span class="pm-solve__why">Uch</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">w = 10, L = 20, A = 200 m<sup>2</sup></span>
    <span class="pm-solve__why">Tekshiruv: 10 + 10 + 20 = 40 metr toʻr ✓</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Devorli masalada javob <b>kvadrat emas</b>: 10 × 20. Toʻrt tomon toʻrlanganda eng
  katta maydonni kvadrat beradi, uch tomon toʻrlanganda esa uzunlik enidan ikki
  barobar katta boʻladi. Shuning uchun masalani oʻqiganda «necha tomon» degan
  savolni birinchi bering.
</div>

<h3>3-tur — balandlik (height)</h3>

<p>h = −5t<sup>2</sup> + 30t + 10 boʻlsa, uch t = −30 ÷ (−10) = 3 soniyada, va
h = −45 + 90 + 10 = 55 metr. Yana oʻsha ikki savol: <em>qachon</em> — 3, <em>qancha
baland</em> — 55.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Modelni tuzganingizdan keyin <b>bitta oson qiymat</b> qoʻyib tekshiring. Yuqoridagi
  daromadda x = 0: narx 20, soni 300, daromad 6000 — matndagi boshlangʻich holat ✓
  Model shu tekshiruvdan oʻtmasa, hisoblashni boshlamang.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>maximum revenue</b><span>eng koʻp daromad — y qiymati</span></li>
  <li><b>the price that maximizes revenue</b><span>daromadni maksimal qiladigan narx — x</span></li>
  <li><b>the greatest possible area</b><span>eng katta mumkin boʻlgan maydon</span></li>
  <li><b>reaches its maximum height after … seconds</b><span>… soniyadan keyin eng baland nuqtaga chiqadi</span></li>
  <li><b>for what value of x</b><span>x ning qaysi qiymatida</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">90 s</span></p>
  <div class="ps-stem__q">
    <p>A shop sells a teapot for 20 dollars and sells 300 of them each week. For every
    1 dollar increase in price, it sells 10 fewer teapots. What price gives the greatest
    weekly revenue?</p>
  </div>
  <ol class="ps-ch">
    <li>5 dollars</li>
    <li>25 dollars</li>
    <li>250 dollars</li>
    <li>6,250 dollars</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 25 dollars</p>
      <p>R = (20 + x)(300 − 10x) = 6000 + 100x − 10x<sup>2</sup>, uch x = 5 da.
      Narx = 20 + 5 = 25.</p>
      <p>Tekshiruv: 25 × 250 = 6,250, va 24 × 260 = 6,240, 26 × 240 = 6,240 —
      ikkala tomonda ham kamroq ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">5 dollars</span>
  <span class="ps-trap__why">Bu x — <b>oshirish</b> miqdori, narx emas. Har doim
  x nimani anglatishini yozib qoʻying va oxirida unga qayting.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">90 s</span></p>
  <div class="ps-stem__q">
    <p>A farmer has 40 metres of fencing to build a rectangular pen against a long
    wall. The wall forms one side, so fencing is needed for only three sides. What is
    the greatest possible area of the pen?</p>
  </div>
  <ol class="ps-ch">
    <li>100 square metres</li>
    <li>200 square metres</li>
    <li>400 square metres</li>
    <li>160 square metres</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 200 square metres</p>
      <p>A = w(40 − 2w), uch w = 10 da → 10 × 20 = 200.</p>
      <p><b>100</b> — 10 × 10 kvadrat deb hisoblangan javob; u toʻrt tomon
      toʻrlanganda toʻgʻri boʻlardi, bu yerda emas.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">100 square metres</span>
  <span class="ps-trap__why">«Eng katta maydon — kvadrat» qoidasi yodda qolgan, lekin
  u faqat toʻrtala tomon ham toʻrlanganda ishlaydi. Devor qoidani buzadi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Har bir max/min masalasida uchta qatorni yozing:</p>
  <ol>
    <li><b>x = …</b> (x nimani anglatadi — dollarmi, metrmi, soniyami);</li>
    <li>model (daromad = narx × soni, maydon = eni × uzunligi);</li>
    <li>savol <b>x</b> ni soʻradimi yoki <b>y</b> ni.</li>
  </ol>
  <p>Uchinchi qator ballning yarmini saqlaydi: toʻgʻri hisoblab, notoʻgʻri sonni
  belgilash bu yerdagi eng koʻp uchraydigan yoʻqotish.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Uch x = 5 da → javob 5 dollar</p>
  <p class="pe-good">Narx = 20 + 5 = 25 dollar</p>
  <p class="pe-fix__why">x — oʻzgarish, narxning oʻzi emas. Modelni tuzganda buni
  yozib qoʻying.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">40 metr toʻr → tomoni 10 m boʻlgan kvadrat</p>
  <p class="pe-good">10 m × 20 m, maydoni 200 m<sup>2</sup></p>
  <p class="pe-fix__why">Devor tufayli toʻr uch tomonga ketadi: 2w + L = 40.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Kvadrat model <b>har doim</b> ikkita son beradi — uchning x va y koordinatalari — va
  matnli masalada ular butunlay boshqa narsalar: biri narx, ikkinchisi pul; biri
  soniya, ikkinchisi metr. Javobni belgilashdan oldin oʻlchov birligiga qarang.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  a manfiy boʻlsa maksimum bor, minimum yoʻq — va aksincha. Daromad va balandlik
  masalalarida a deyarli har doim manfiy (narx juda oshsa daromad tushadi, jism
  qaytib tushadi), maydon masalalarida ham shunday.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  A rectangle has a perimeter of 40 metres. What is its greatest possible area?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">100 m<sup>2</sup> — bu yerda toʻrtala tomon ham hisobga
  olingan, demak javob 10 × 10 kvadrat.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  A ball's height is <i>h</i> = −5<i>t</i><sup>2</sup> + 20<i>t</i> + 15 metres. What
  is its greatest height?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">35 metr — t = 2 da: −20 + 40 + 15 = 35.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  For the same ball, after how many seconds does it reach that height?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">2 soniya — t = −20 ÷ (−10) = 2. Bir masala, ikki
  boshqa javob.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Two numbers add to 12. What is their greatest possible product?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">36 — P = x(12 − x), uch x = 6 da, demak 6 × 6.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A club charges 10 dollars and has 60 members. Each 1 dollar rise loses 4 members.
  What fee gives the greatest income?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">12.50 dollar — I = (10 + x)(60 − 4x), uch x = 2.5 da.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>revenue</b><span>daromad (narx × soni)</span></li>
  <li><b>maximize</b><span>eng katta qiymatga yetkazmoq</span></li>
  <li><b>greatest possible</b><span>eng katta mumkin boʻlgan</span></li>
  <li><b>fencing</b><span>toʻr, panjara</span></li>
  <li><b>pen / enclosure</b><span>qafas, oʻralgan joy</span></li>
  <li><b>dimensions</b><span>oʻlchamlar</span></li>
  <li><b>model the situation</b><span>vaziyatni tenglama bilan ifodalash</span></li>
  <li><b>income</b><span>tushum, kirim</span></li>
  <li><b>per unit increase</b><span>har bir birlik oshganda</span></li>
  <li><b>reaches its maximum</b><span>eng yuqori nuqtasiga chiqadi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Avval <b>x nimani anglatishini</b> yozing, keyin modelni tuzing.</li>
    <li>Uch — <b>x = −b ÷ (2a)</b>; qiymat uchun uni modelga qaytarib qoʻying.</li>
    <li>Savol <b>x</b> ni soʻradimi (narx, vaqt) yoki <b>y</b> ni (daromad,
        balandlik) — javobni belgilashdan oldin shuni tekshiring.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-37 — graphing parabolas
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-37: Graphing Parabolas — Intercepts, Vertex, and Symmetry",
        "category": "math",
        "order": 37,
        "summary": (
            "Parabolani chizish uchun toʻrt narsa yetadi: y oʻqidagi nuqta, nollar, "
            "uch va simmetriya. Har bir koʻrinish ulardan bittasini bepul beradi."
        ),
        "stories": ["The Broken Arch"],
        "content": """
<h2>SAT-37: Graphing Parabolas — Intercepts, Vertex, and Symmetry</h2>

<p>SAT parabolani chizishni deyarli soʻramaydi — lekin <mark>grafikni oʻqishni</mark>
juda koʻp soʻraydi. Grafikning har bir belgisi tenglamada oʻz joyiga ega, va uchta
koʻrinish uchta boshqa narsani bepul koʻrsatadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>y oʻqidagi nuqtani bir qarashda aytasiz;</li>
    <li>nollarni ajratilgan koʻrinishdan oʻqiysiz;</li>
    <li>uchni topib, simmetriyadan foydalanasiz;</li>
    <li>«qaysi koʻrinish nimani koʻrsatadi» savoliga javob berasiz.</li>
  </ul>
</div>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Koʻrinish</th><th>Yozilishi</th><th>Bepul beradigan narsa</th></tr>
  <tr><td>standart</td><td>y = ax<sup>2</sup> + bx + c</td>
      <td class="pm-word__sym">y oʻqidagi nuqta: (0, c)</td></tr>
  <tr><td>ajratilgan</td><td>y = a(x − p)(x − q)</td>
      <td class="pm-word__sym">nollar: x = p va x = q</td></tr>
  <tr><td>uchi shakli</td><td>y = a(x − h)<sup>2</sup> + k</td>
      <td class="pm-word__sym">uch: (h, k)</td></tr>
</table></div>

<h3>Bitta parabola, toʻrtta belgi</h3>

<p>y = x<sup>2</sup> − 4x − 5 ni koʻrib chiqamiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = 0  →  y = −5</span>
    <span class="pm-solve__why">y oʻqidagi nuqta (0, −5) — bu c ning oʻzi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(x − 5)(x + 1) = 0  →  x = 5, x = −1</span>
    <span class="pm-solve__why">Nollar (SAT-31)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = (5 + (−1)) ÷ 2 = 2</span>
    <span class="pm-solve__why">Uch nollarning aynan oʻrtasida</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">y = 4 − 8 − 5 = −9  →  uch (2, −9)</span>
    <span class="pm-solve__why">a musbat, demak bu eng past nuqta</span>
  </div>
</div>

<figure class="pm-fig">
  <svg viewBox="0 0 320 240" role="img"
       aria-label="Parabola y = x squared minus 4x minus 5, crossing the x-axis at
                   minus 1 and 5, the y-axis at minus 5, vertex at 2, minus 9">
    <line class="pm-ln" x1="20" y1="104" x2="310" y2="104"/>
    <line class="pm-ln" x1="90" y1="14"  x2="90"  y2="230"/>
    <polyline class="pm-fill" fill="none"
      points="20,20 55,104 90,164 125,200 160,212 195,200 230,164 265,104 300,20"/>
    <circle cx="55"  cy="104" r="4"/>
    <circle cx="265" cy="104" r="4"/>
    <circle cx="90"  cy="164" r="4"/>
    <circle cx="160" cy="212" r="4"/>
    <line class="pm-ln" x1="160" y1="104" x2="160" y2="212"
          stroke-dasharray="4 4"/>
    <text class="pm-lbl" x="34"  y="96">(−1, 0)</text>
    <text class="pm-lbl" x="246" y="96">(5, 0)</text>
    <text class="pm-lbl" x="96"  y="160">(0, −5)</text>
    <text class="pm-lbl" x="140" y="230">(2, −9)</text>
    <text class="pm-lbl" x="166" y="130">x = 2</text>
  </svg>
  <figcaption>y = x<sup>2</sup> − 4x − 5. Nollar oʻqda −1 va 5; uch ularning
  oʻrtasida, x = 2 chizigʻida.</figcaption>
</figure>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Uch <b>nollarning oʻrtasida</b> turadi — bu grafikdagi eng foydali fakt. Ikkita
  kesishish nuqtasi berilgan boʻlsa, uchning x koordinatasini hisoblamasdan, faqat
  ularning oʻrtasini olib topasiz.
</div>

<h3>Simmetriya nima beradi</h3>

<p>Parabolaning har bir nuqtasining <b>juftligi</b> bor: uchdan bir xil masofada,
bir xil balandlikda. Yuqoridagi grafikda (0, −5) nuqtaning juftligi (4, −5) — chunki
0 va 4 x = 2 dan bir xil uzoqlikda.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Jadval berilgan savollarda simmetriyani ishlating. Agar jadvalda ikkita <b>bir xil
  y</b> qiymat boʻlsa, ularning x lari orasidagi oʻrta — uchning x koordinatasi.
  Bu SAT'da tez-tez uchraydigan bepul yoʻl.
</div>

<h3>a nima qiladi</h3>

<ul>
  <li><b>a &gt; 0</b> — yuqoriga ochiladi, uchi minimum;</li>
  <li><b>a &lt; 0</b> — pastga ochiladi, uchi maksimum;</li>
  <li>nollar soni — diskriminantdan (SAT-34): ikkita, bitta yoki hech qanday.</li>
</ul>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>the y-intercept</b><span>y oʻqi bilan kesishish — x = 0 dagi qiymat</span></li>
  <li><b>the x-intercepts / the zeros</b><span>x oʻqi bilan kesishish / nollar</span></li>
  <li><b>opens downward</b><span>pastga ochiladi (a manfiy)</span></li>
  <li><b>which equation displays the zeros as constants</b><span>qaysi tenglama nollarni son sifatida koʻrsatadi</span></li>
  <li><b>the graph is symmetric about the line</b><span>grafik shu chiziqqa nisbatan simmetrik</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>The graph of <i>y</i> = <i>x</i><sup>2</sup> − 6<i>x</i> + 8 crosses the
    <i>y</i>-axis at which point?</p>
  </div>
  <ol class="ps-ch">
    <li>(0, 8)</li>
    <li>(8, 0)</li>
    <li>(0, −6)</li>
    <li>(0, 3)</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) (0, 8)</p>
      <p>x = 0 qoʻying: y = 8. Standart koʻrinishda erkin had — bu har doim y
      oʻqidagi qiymat.</p>
      <p><b>(8, 0)</b> — koordinatalar oʻrin almashgan; bu x oʻqidagi nuqta
      boʻlardi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">(8, 0)</span>
  <span class="ps-trap__why">y-intercept da <b>x</b> nolga teng, y emas. Ikki
  iborani ajratib qoʻying: y-intercept → (0, y); x-intercept → (x, 0).</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">70 s</span></p>
  <div class="ps-stem__q">
    <p>The graph of a parabola crosses the <i>x</i>-axis at <i>x</i> = −3 and
    <i>x</i> = 7. What is the <i>x</i>-coordinate of its vertex?</p>
  </div>
  <ol class="ps-ch">
    <li>2</li>
    <li>5</li>
    <li>−5</li>
    <li>4</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 2</p>
      <p>Uch nollarning oʻrtasida: (−3 + 7) ÷ 2 = 2.</p>
      <p>Tenglamani umuman tuzish shart emas — simmetriya yetadi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">5</span>
  <span class="ps-trap__why">Ikki nolning <b>ayirmasining yarmi</b> hisoblangan
  (10 ÷ 2), oʻrtasi emas. Oʻrta — yigʻindining yarmi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Grafik savollarida shu tartibda qarang:</p>
  <ol>
    <li>Parabola qaysi tomonga ochilgan — <b>a</b> ning ishorasi;</li>
    <li>x oʻqini necha marta kesgan — <b>diskriminant</b> (SAT-34);</li>
    <li>y oʻqidagi nuqta — <b>c</b>;</li>
    <li>uch — nollarning oʻrtasi yoki −b ÷ (2a).</li>
  </ol>
  <p>Toʻrt javobning uchtasi koʻpincha shu toʻrt tekshiruvning bittasida
  oʻchadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">y = x<sup>2</sup> − 6x + 8 ning y-intercepti (8, 0)</p>
  <p class="pe-good">(0, 8)</p>
  <p class="pe-fix__why">y oʻqida turgan nuqtaning x koordinatasi nolga teng.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Nollari −3 va 7 → uch x = 5 da</p>
  <p class="pe-good">x = 2</p>
  <p class="pe-fix__why">Oʻrta nuqta (−3 + 7) ÷ 2; ayirmani boʻlish emas.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Uch (2, −9) — <b>ikkita</b> son. «What is the minimum value» soʻrasa javob −9;
  «at what value of x» soʻrasa javob 2. SAT-35 dagi oʻsha tuzoq bu yerda grafik
  koʻrinishida qaytadi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Uchta koʻrinish bir xil parabolani chizadi — ular <b>teng kuchli</b>. Savol
  «qaysi tenglama nollarni koʻrsatadi» desa, u sizdan hisoblashni emas, qaysi
  yozuvda javob <u>allaqachon koʻrinib turganini</u> soʻrayapti.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Grafik savolida <b>chizmani oʻlchamang</b>. SAT'ning parabolalari koʻpincha masshtabsiz chiziladi va koʻzga toʻgʻri koʻringan javob notoʻgʻri boʻlishi mumkin. Tenglamadan hisoblang — bu bir necha soniyalik ish.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  What is the <i>y</i>-intercept of <i>y</i> = <i>x</i><sup>2</sup> + 3<i>x</i> − 10?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(0, −10) — erkin had.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  What are the <i>x</i>-intercepts of <i>y</i> = (<i>x</i> − 4)(<i>x</i> + 6)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">x = 4 va x = −6 — qavsdagi sonlarning
  qarama-qarshisi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A parabola has zeros at <i>x</i> = 1 and <i>x</i> = 9. Where is its axis of
  symmetry?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">x = 5 — (1 + 9) ÷ 2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  On the graph of <i>y</i> = <i>x</i><sup>2</sup> − 4<i>x</i> − 5, the point
  (0, −5) lies on the curve. Which other point has the same <i>y</i>-value?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(4, −5) — uch x = 2 da, va 0 bilan 4 undan bir xil
  masofada.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Does the graph of <i>y</i> = <i>x</i><sup>2</sup> + 2<i>x</i> + 5 cross the
  <i>x</i>-axis?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — diskriminant 4 − 20 = −16, manfiy (SAT-34).</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>parabola</b><span>parabola</span></li>
  <li><b>y-intercept</b><span>y oʻqi bilan kesishish nuqtasi</span></li>
  <li><b>x-intercepts / zeros</b><span>x oʻqi bilan kesishish / nollar</span></li>
  <li><b>vertex</b><span>uch</span></li>
  <li><b>axis of symmetry</b><span>simmetriya oʻqi</span></li>
  <li><b>opens upward / downward</b><span>yuqoriga / pastga ochiladi</span></li>
  <li><b>midpoint</b><span>oʻrta nuqta</span></li>
  <li><b>equivalent forms</b><span>teng kuchli koʻrinishlar</span></li>
  <li><b>displays as constants</b><span>son sifatida koʻrsatadi</span></li>
  <li><b>lies on the curve</b><span>egri chiziqda yotadi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Standart <b>c</b> ni, ajratilgan <b>nollarni</b>, uchi shakli <b>uchni</b>
        bepul beradi.</li>
    <li>Uch — <b>nollarning oʻrtasida</b>; oʻrta yigʻindining yarmi.</li>
    <li>Bir xil y qiymatli ikki nuqta uchdan <b>bir xil masofada</b> turadi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-38 — linear-quadratic systems
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-38: Systems of Non-Linear Equations (Linear–Quadratic)",
        "category": "math",
        "order": 38,
        "summary": (
            "Chiziqni parabolaga qoʻying: qolgani oddiy kvadrat tenglama. "
            "Necha marta kesishishini diskriminant aytadi."
        ),
        "stories": ["The Ridge on the Approach"],
        "content": """
<h2>SAT-38: Systems of Non-Linear Equations (Linear–Quadratic)</h2>

<p>SAT-19 da ikkita chiziqning kesishishini topgan edik. Endi bittasi parabola.
<mark>Usul aynan oʻsha — oʻrniga qoʻyish</mark> — faqat natija chiziqli emas, kvadrat
tenglama boʻladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>chiziqni parabolaga qoʻyib, bitta kvadrat tenglama hosil qilasiz;</li>
    <li>x ni topib, <b>y ni ham</b> topasiz — javob nuqta;</li>
    <li>kesishishlar sonini diskriminant bilan aytasiz;</li>
    <li>«tangent» soʻzini D = 0 deb oʻqiysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The method</span>
  <span class="pe-chip pe-chip--s">y ni tenglashtiring</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">nolga keltiring</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">yeching, y ni toping</span>
</div>

<h3>Uch qadam</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">y = x<sup>2</sup>  va  y = x + 2</span>
    <span class="pm-solve__why">Ikkala tenglamada ham y yolgʻiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x<sup>2</sup> = x + 2  →  x<sup>2</sup> − x − 2 = 0</span>
    <span class="pm-solve__why">Tenglashtirib, nolga keltirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(x − 2)(x + 1) = 0  →  x = 2, x = −1</span>
    <span class="pm-solve__why">SAT-31</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">(2, 4) va (−1, 1)</span>
    <span class="pm-solve__why">y ni <b>chiziqqa</b> qoʻyib topdik — u osonroq</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Sistema yechimi — <b>nuqta</b>, yaʼni ikkita son. x ni topib toʻxtash bu mavzudagi
  eng koʻp uchraydigan yoʻqotish; javob variantlari deyarli har doim
  (x, y) koʻrinishida beriladi.
</div>

<h3>Ikkinchi misol</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">y = x<sup>2</sup> − 3  va  y = 2x</span>
    <span class="pm-solve__why">Tenglashtiramiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x<sup>2</sup> − 2x − 3 = 0  →  (x − 3)(x + 1) = 0</span>
    <span class="pm-solve__why">x = 3 va x = −1</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">(3, 6) va (−1, −2)</span>
    <span class="pm-solve__why">y = 2x ga qoʻydik</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  y ni topish uchun har doim <b>chiziqli</b> tenglamani ishlating. y = 2x bir
  koʻpaytirish, y = x<sup>2</sup> − 3 esa kvadratga koʻtarish va ayirish —
  ikkinchisida xato qilish ehtimoli ikki barobar.
</div>

<h3>Nechta kesishish nuqtasi bor?</h3>

<p>Bu savolga yechmasdan javob berish mumkin — hosil boʻlgan kvadrat tenglamaning
<b>diskriminanti</b> yetadi (SAT-34):</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Diskriminant</th><th>Kesishish</th><th>Grafik</th></tr>
  <tr><td>D &gt; 0</td><td class="pm-word__sym">ikkita nuqta</td>
      <td>chiziq parabolani kesib oʻtadi</td></tr>
  <tr><td>D = 0</td><td class="pm-word__sym">bitta nuqta</td>
      <td>chiziq parabolaga <b>urinadi</b> (tangent)</td></tr>
  <tr><td>D &lt; 0</td><td class="pm-word__sym">yoʻq</td>
      <td>chiziq parabolaga tegmaydi</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ingliz tilidagi <b>tangent</b> soʻzi «urinuvchi» degani va SAT'da u
  <b>D = 0</b> ning boshqa nomi. «The line is tangent to the parabola» degan jumlani
  koʻrsangiz, darrov diskriminantni yozib, nolga tenglashtiring.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>the solution to the system</b><span>sistemaning yechimi — nuqta (x, y)</span></li>
  <li><b>how many points of intersection</b><span>nechta kesishish nuqtasi</span></li>
  <li><b>is tangent to</b><span>urinadi → D = 0</span></li>
  <li><b>the graphs intersect at</b><span>grafiklar … nuqtada kesishadi</span></li>
  <li><b>what is the value of x + y</b><span>x + y nechaga teng (yechimdan keyin)</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">80 s</span></p>
  <div class="ps-stem__q">
    <p>If <i>y</i> = <i>x</i><sup>2</sup> and <i>y</i> = <i>x</i> + 2, which ordered
    pair is a solution to the system?</p>
  </div>
  <ol class="ps-ch">
    <li>(2, 4)</li>
    <li>(2, 2)</li>
    <li>(4, 2)</li>
    <li>(−1, −1)</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) (2, 4)</p>
      <p>x<sup>2</sup> − x − 2 = 0 → x = 2 yoki −1. x = 2 da y = 4.</p>
      <p>Tekshiruv: 4 = 2<sup>2</sup> ✓ va 4 = 2 + 2 ✓ — <b>ikkala</b> tenglamani
      ham qanoatlantirishi shart.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">(2, 2)</span>
  <span class="ps-trap__why">x toʻgʻri topilgan, y esa xayolan koʻchirilgan. Nuqtani
  <b>ikkala</b> tenglamaga qoʻyib tekshiring: 2 ≠ 2<sup>2</sup>.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">70 s</span></p>
  <div class="ps-stem__q">
    <p>How many points of intersection do the graphs of <i>y</i> =
    <i>x</i><sup>2</sup> + 1 and <i>y</i> = <i>x</i> − 1 have?</p>
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
      <p>x<sup>2</sup> + 1 = x − 1 → x<sup>2</sup> − x + 2 = 0, va D = 1 − 8 = −7.</p>
      <p>Manfiy diskriminant — chiziq parabolaga umuman tegmaydi. Parabola
      y oʻqida 1 da, chiziq esa −1 da: chiziq juda past qolgan.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">Two</span>
  <span class="ps-trap__why">«Parabola va chiziq har doim ikki marta kesishadi»
  degan taxmin. Diskriminantni hisoblang — bu 15 soniyalik ish.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Javoblar nuqta boʻlsa, yechmang — <b>qoʻying</b>:</p>
  <ol>
    <li>Har bir nuqtani <b>chiziqli</b> tenglamaga qoʻying (osonroq);</li>
    <li>Oʻtganlarini parabolaga qoʻying;</li>
    <li>Ikkalasidan ham oʻtgani — javob.</li>
  </ol>
  <p>Bu koʻpincha 20 soniya, yechish esa 80 — va ishora xatosi umuman
  boʻlmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">x<sup>2</sup> = x + 2 → x = 2, javob 2</p>
  <p class="pe-good">Javob (2, 4)</p>
  <p class="pe-fix__why">Sistemaning yechimi — nuqta. x ni topgach, y ni ham
  toping.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">x<sup>2</sup> + 1 = x − 1 → x<sup>2</sup> + x + 2 = 0</p>
  <p class="pe-good">x<sup>2</sup> − x + 2 = 0</p>
  <p class="pe-fix__why">x ni chapga oʻtkazganda ishorasi almashadi. Bu yerda
  diskriminantning qiymati oʻzgarmaydi, lekin koʻp savolda oʻzgaradi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikkala tenglamada ham y yolgʻiz turgani uchun ularni <b>bevosita</b>
  tenglashtirdik. Agar chiziq 2x + y = 5 koʻrinishida berilsa, avval uni
  y = 5 − 2x qilib yozing — usul oʻzgarmaydi, faqat bir qadam qoʻshiladi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Chiziq va parabola <b>ikki martadan koʻp</b> kesisha olmaydi. Sababi: hosil boʻlgan tenglama kvadrat, va kvadrat tenglamaning koʻpi bilan ikkita ildizi bor. «Uchta kesishish nuqtasi» degan variant har doim notoʻgʻri.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Solve the system: <i>y</i> = <i>x</i><sup>2</sup> and <i>y</i> = 4</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(2, 4) va (−2, 4) — x<sup>2</sup> = 4 ning
  <b>ikkita</b> ildizi bor.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Solve the system: <i>y</i> = <i>x</i><sup>2</sup> − 3 and <i>y</i> = 2<i>x</i></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(3, 6) va (−1, −2).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  How many points of intersection do <i>y</i> = <i>x</i><sup>2</sup> and
  <i>y</i> = −2 have?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Hech qanday — x<sup>2</sup> = −2 ning haqiqiy yechimi
  yoʻq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Solve the system: <i>y</i> = <i>x</i><sup>2</sup> + 2<i>x</i> and
  <i>y</i> = 3<i>x</i> + 6</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(3, 15) va (−2, 0) — x<sup>2</sup> − x − 6 = 0.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  For what value of <i>c</i> is the line <i>y</i> = <i>c</i> tangent to
  <i>y</i> = <i>x</i><sup>2</sup> − 4<i>x</i> + 7?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">c = 3 — uch (2, 3) da, va gorizontal chiziq parabolaga
  faqat uchida urinadi.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>system of equations</b><span>tenglamalar sistemasi</span></li>
  <li><b>non-linear</b><span>chiziqli boʻlmagan</span></li>
  <li><b>ordered pair</b><span>tartiblangan juftlik (x, y)</span></li>
  <li><b>point of intersection</b><span>kesishish nuqtasi</span></li>
  <li><b>tangent to</b><span>urinuvchi (D = 0)</span></li>
  <li><b>substitution</b><span>oʻrniga qoʻyish usuli</span></li>
  <li><b>satisfies both equations</b><span>ikkala tenglamani ham qanoatlantiradi</span></li>
  <li><b>solve the system</b><span>sistemani yeching</span></li>
  <li><b>graphs intersect</b><span>grafiklar kesishadi</span></li>
  <li><b>no real solution</b><span>haqiqiy yechim yoʻq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Tenglashtiring, <b>nolga keltiring</b>, kvadrat tenglamani yeching.</li>
    <li>Javob — <b>nuqta</b>: y ni chiziqli tenglamadan toping.</li>
    <li>Nechta kesishish — <b>diskriminant</b>; «tangent» degani D = 0.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-39 — radical equations and extraneous solutions
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-39: Radical Equations and Extraneous Solutions",
        "category": "math",
        "order": 39,
        "summary": (
            "Ikkala tomonni kvadratga koʻtarish yechim qoʻshib yuborishi mumkin. "
            "Shuning uchun tekshirish — qoʻshimcha emas, yechimning bir qismi."
        ),
        "stories": ["Two Answers, One Road"],
        "content": """
<h2>SAT-39: Radical Equations and Extraneous Solutions</h2>

<p>Ildizli tenglamani yechish oson: ikkala tomonni kvadratga koʻtaring. Lekin bu
amalning <mark>xavfli tomoni bor</mark> — u tenglamaga asli unda boʻlmagan yechim
qoʻshib yuborishi mumkin. Shuning uchun bu darsda tekshirish ixtiyoriy emas.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>ildizni yolgʻiz qoldirib, kvadratga koʻtarasiz;</li>
    <li>hosil boʻlgan kvadrat tenglamani yechasiz;</li>
    <li><b>har bir</b> ildizni asl tenglamaga qoʻyib tekshirasiz;</li>
    <li>begona ildiz nima uchun paydo boʻlishini tushuntirasiz.</li>
  </ul>
</div>

<h3>Nima uchun begona ildiz paydo boʻladi</h3>

<p>Sabab bitta va juda oddiy. <b>−2 va 2 har xil sonlar, lekin ularning kvadrati bir
xil.</b> Kvadratga koʻtarganda bu farq yoʻqoladi, va tenglama endi ikkalasini ham
qabul qiladi.</p>

<div class="pe-formula">
  <span class="pe-formula__label">The lost information</span>
  <span class="pe-chip pe-chip--s">−2 ≠ 2</span>
  <span class="pe-op">lekin</span>
  <span class="pe-chip pe-chip--v">(−2)<sup>2</sup> = 2<sup>2</sup></span>
</div>

<p>Yana bir narsa: <b>√</b> belgisi har doim <u>manfiy boʻlmagan</u> sonni bildiradi.
√9 = 3, va faqat 3. Shuning uchun √(biror narsa) manfiy songa teng boʻla olmaydi —
qanday hisoblasangiz ham.</p>

<h3>Toʻliq yechim, tekshiruv bilan</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">√(x + 6) = x</span>
    <span class="pm-solve__why">Ildiz allaqachon yolgʻiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + 6 = x<sup>2</sup></span>
    <span class="pm-solve__why">Ikkala tomon kvadratga koʻtarildi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x<sup>2</sup> − x − 6 = 0  →  (x − 3)(x + 2) = 0</span>
    <span class="pm-solve__why">x = 3 va x = −2</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Faqat x = 3</span>
    <span class="pm-solve__why">√9 = 3 ✓, lekin √4 = 2, va 2 ≠ −2 ✗</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz — bu qadam majburiy</p>
  <p>x = 3: chap tomon √(3 + 6) = 3, oʻng tomon 3 ✓</p>
  <p>x = −2: chap tomon √(−2 + 6) = √4 = <b>2</b>, oʻng tomon <b>−2</b> ✗</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  x = −2 hisoblashdagi xato emas — hamma qadam toʻgʻri bajarilgan. U
  <b>kvadratga koʻtarish</b> tufayli paydo boʻlgan begona ildiz. Uni faqat
  tekshirish topadi.
</div>

<h3>Chap tomonda ikki had boʻlsa</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">√(x + 7) = x + 1</span>
    <span class="pm-solve__why">Oʻng tomon ikki hadli</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + 7 = x<sup>2</sup> + 2x + 1</span>
    <span class="pm-solve__why">(x + 1)<sup>2</sup> — toʻliq kvadrat (SAT-30), x<sup>2</sup> + 1 emas</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x<sup>2</sup> + x − 6 = 0  →  (x + 3)(x − 2) = 0</span>
    <span class="pm-solve__why">x = 2 va x = −3</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Faqat x = 2</span>
    <span class="pm-solve__why">x = 2: √9 = 3 va 2 + 1 = 3 ✓; x = −3: √4 = 2, −3 + 1 = −2 ✗</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Eng koʻp uchraydigan hisob xatosi shu qadamda: (x + 1)<sup>2</sup> ni
  x<sup>2</sup> + 1 deb yozish. Kvadratga koʻtarish qavsni ochish demakdir —
  oʻrtadagi 2x ni unutmang.
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Tez tekshiruv: <b>oʻng tomon manfiy chiqadigan ildiz darrov oʻchadi.</b>
  √(narsa) hech qachon manfiy boʻlmaydi, shuning uchun x = −2 ni hisoblab
  oʻtirmasdan ham tashlab yuborish mumkin.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>extraneous solution</b><span>begona ildiz — tekshiruvdan oʻtmaydigani</span></li>
  <li><b>which value satisfies the equation</b><span>qaysi qiymat tenglamani qanoatlantiradi</span></li>
  <li><b>the sum of all solutions</b><span>barcha yechimlar yigʻindisi (faqat haqiqiylarniki)</span></li>
  <li><b>square both sides</b><span>ikkala tomonni kvadratga koʻtaring</span></li>
  <li><b>no solution</b><span>yechim yoʻq — hammasi begona chiqqan hol</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>What is the solution to √(2<i>x</i> + 3) = <i>x</i>?</p>
  </div>
  <ol class="ps-ch">
    <li><i>x</i> = 3</li>
    <li><i>x</i> = 3 and <i>x</i> = −1</li>
    <li><i>x</i> = −1</li>
    <li>There is no solution</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) x = 3</p>
      <p>2x + 3 = x<sup>2</sup> → x<sup>2</sup> − 2x − 3 = 0 → x = 3 yoki −1.</p>
      <p>Tekshiruv: x = 3 da √9 = 3 ✓. x = −1 da √1 = 1, lekin oʻng tomon −1 ✗ —
      begona ildiz.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">x = 3 and x = −1</span>
  <span class="ps-trap__why">Kvadrat tenglamaning ikkala ildizi ham yozilgan,
  tekshiruvsiz. Bu variant har doim javoblar orasida turadi — chunki koʻpchilik
  aynan shu yerda toʻxtaydi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">85 s</span></p>
  <div class="ps-stem__q">
    <p>How many solutions does the equation √(<i>x</i> + 5) = <i>x</i> − 1 have?</p>
  </div>
  <ol class="ps-ch">
    <li>One</li>
    <li>Two</li>
    <li>Zero</li>
    <li>Infinitely many</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) One</p>
      <p>x + 5 = x<sup>2</sup> − 2x + 1 → x<sup>2</sup> − 3x − 4 = 0 → x = 4 yoki −1.</p>
      <p>x = 4: √9 = 3 va 4 − 1 = 3 ✓. x = −1: √4 = 2, lekin −1 − 1 = −2 ✗</p>
      <p>Demak bitta yechim — savol «nechta» deb soʻragani bejiz emas.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">Two</span>
  <span class="ps-trap__why">Kvadrat tenglamada ikkita ildiz bor — lekin savol
  <b>ildizli</b> tenglama haqida. Ikkalasidan bittasi tekshiruvdan oʻtmaydi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Ildiz belgisi koʻringan zahoti uch qadamni yozing:</p>
  <ol>
    <li>Kvadratga koʻtaring va yeching;</li>
    <li>Har bir ildizni <b>asl</b> tenglamaga qoʻying — soddalashtirilganiga
        emas;</li>
    <li>Oʻng tomoni manfiy chiqqanini oʻchiring.</li>
  </ol>
  <p>Javoblar son boʻlsa, ulardan boshlang: bitta qoʻyish 60 soniya
  yechishdan tez.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">√(x + 6) = x → x = 3 va x = −2</p>
  <p class="pe-good">Faqat x = 3</p>
  <p class="pe-fix__why">x = −2 tekshiruvdan oʻtmaydi: √4 = 2, −2 emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">√(x + 7) = x + 1 → x + 7 = x<sup>2</sup> + 1</p>
  <p class="pe-good">x + 7 = x<sup>2</sup> + 2x + 1</p>
  <p class="pe-fix__why">(x + 1)<sup>2</sup> = x<sup>2</sup> + 2x + 1 — oʻrtadagi
  had tushib qolgan (SAT-30).</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Begona ildiz — <b>matematikaning oʻzida bor hodisa</b>, sizning xatoyingiz emas.
  Kvadratga koʻtarish ishorani yoʻqotadi, va yoʻqolgan maʼlumot qaytib kelmaydi.
  Shuning uchun tekshirish bu mavzuda yechimning oxirgi qadami hisoblanadi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Baʼzan <b>ikkala</b> ildiz ham oʻchadi — u holda javob «no solution». SAT bu
  variantni ataylab qoʻyadi, chunki koʻpchilik «yechim topdim, demak bor» deb
  oʻylaydi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Solve: √(<i>x</i> + 2) = <i>x</i></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> = 2 — x = −1 begona: √1 = 1, −1 emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Solve: √(3<i>x</i> + 4) = <i>x</i></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> = 4 — x = −1 tekshiruvdan oʻtmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  How many solutions does √<i>x</i> = −3 have?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Hech qanday — √ belgisi manfiy son bermaydi. Kvadratga
  koʻtarsangiz x = 9 chiqadi, lekin √9 = 3 ≠ −3.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Solve: √(<i>x</i> + 5) = <i>x</i> − 1</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> = 4 — x = −1 begona.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Why must every solution of a radical equation be checked?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Kvadratga koʻtarish ishorani yoʻqotadi, shuning uchun
  tenglama asli unda boʻlmagan ildizni qabul qilishi mumkin.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>radical equation</b><span>ildizli tenglama</span></li>
  <li><b>extraneous solution</b><span>begona ildiz</span></li>
  <li><b>square both sides</b><span>ikkala tomonni kvadratga koʻtarmoq</span></li>
  <li><b>isolate the radical</b><span>ildizni yolgʻiz qoldirmoq</span></li>
  <li><b>satisfies the equation</b><span>tenglamani qanoatlantiradi</span></li>
  <li><b>check each solution</b><span>har bir yechimni tekshirmoq</span></li>
  <li><b>the principal square root</b><span>asosiy (manfiy boʻlmagan) kvadrat ildiz</span></li>
  <li><b>discard</b><span>tashlab yubormoq, oʻchirmoq</span></li>
  <li><b>no solution</b><span>yechim yoʻq</span></li>
  <li><b>original equation</b><span>asl tenglama</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Kvadratga koʻtarish <b>yechim qoʻshadi</b>, chunki u ishorani
        yoʻqotadi.</li>
    <li>Har bir ildizni <b>asl</b> tenglamaga qoʻying — bu yechimning bir
        qismi.</li>
    <li>√(narsa) manfiy boʻlmaydi: oʻng tomoni manfiy chiqqan ildiz darrov
        oʻchadi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-40 — rational equations and domain restrictions
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-40: Rational Equations and Domain Restrictions",
        "category": "math",
        "order": 40,
        "summary": (
            "Maxraj hech qachon nolga teng boʻlmaydi. Taqiqlangan qiymatlarni "
            "yechishdan oldin yozing — javob aynan oʻsha son chiqishi mumkin."
        ),
        "stories": ["The Journey That Cannot Be Averaged"],
        "content": """
<h2>SAT-40: Rational Equations and Domain Restrictions</h2>

<p>Kasrli tenglamada bitta yangi qoida bor, va u butun mavzuni belgilaydi:
<mark>maxraj nolga teng boʻla olmaydi</mark>. Nolga boʻlish aniqlanmagan, shuning
uchun baʼzi x qiymatlari tenglamaga umuman kirmaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>taqiqlangan qiymatlarni <b>yechishdan oldin</b> yozasiz;</li>
    <li>krest koʻpaytirish bilan kasrdan qutulasiz;</li>
    <li>javobni taqiq roʻyxati bilan solishtirasiz;</li>
    <li>«no solution» qachon toʻgʻri javob ekanini bilasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Always first</span>
  <span class="pe-chip pe-chip--v">maxraj = 0 deb yeching</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">bu qiymatlar TAQIQLANGAN</span>
</div>

<h3>Taqiqlangan qiymatlar</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Ifoda</th><th>Maxraj nol boʻladi</th><th>Taqiq</th></tr>
  <tr><td>1 ÷ (x − 3)</td><td>x − 3 = 0</td><td class="pm-word__sym">x ≠ 3</td></tr>
  <tr><td>x ÷ (x + 5)</td><td>x + 5 = 0</td><td class="pm-word__sym">x ≠ −5</td></tr>
  <tr><td>5 ÷ (x<sup>2</sup> − 9)</td><td>(x − 3)(x + 3) = 0</td>
      <td class="pm-word__sym">x ≠ 3 va x ≠ −3</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Maxrajni <b>ajratib</b> qarang — x<sup>2</sup> − 9 bitta emas, <b>ikkita</b>
  taqiq beradi. Kvadrat maxrajni koʻrganda SAT-30 ni eslang: kvadratlar ayirmasi
  ikki qavsga ajraladi.
</div>

<h3>Yechish — krest koʻpaytirish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">1 ÷ (x − 3) = 2 ÷ (x + 1)</span>
    <span class="pm-solve__why">Taqiqlar: x ≠ 3 va x ≠ −1 — <b>avval</b> yozdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + 1 = 2(x − 3)</span>
    <span class="pm-solve__why">Krest koʻpaytirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + 1 = 2x − 6</span>
    <span class="pm-solve__why">Qavsni ochdik — 2 ikkala hadga ham tegadi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 7</span>
    <span class="pm-solve__why">7 taqiq roʻyxatida yoʻq ✓ Tekshiruv: 1/4 = 2/8 ✓</span>
  </div>
</div>

<h3>Javob taqiqlangan chiqqanda</h3>

<p>Endi eng muhim hol. Hamma qadam toʻgʻri bajariladi, javob chiqadi — va u
taqiqlangan qiymat boʻlib chiqadi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x ÷ (x − 3) = 3 ÷ (x − 3) + 2</span>
    <span class="pm-solve__why">Taqiq: x ≠ 3</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = 3 + 2(x − 3)</span>
    <span class="pm-solve__why">Hamma hadni (x − 3) ga koʻpaytirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = 3 + 2x − 6 = 2x − 3</span>
    <span class="pm-solve__why">Soddalashtirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 3  →  <b>no solution</b></span>
    <span class="pm-solve__why">3 taqiqlangan edi — tenglamaning yechimi yoʻq</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  x = 3 ni javob deb belgilash — bu mavzudagi asosiy tuzoq. Uni asl tenglamaga
  qoʻysangiz maxraj nolga aylanadi, yaʼni ifoda maʼnosini yoʻqotadi. Toʻgʻri javob
  «no solution».
</div>

<h3>Soddalashgan bilan asl bir xil emas</h3>

<p>(x<sup>2</sup> − 4) ÷ (x − 2) ni qisqartirsak x + 2 chiqadi (SAT-30). Lekin bu
ikki ifoda <u>butunlay</u> bir xil emas: x + 2 hamma joyda aniqlangan, asl ifoda esa
x = 2 da <b>emas</b>. Qisqartirish taqiqni oʻchirmaydi.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Taqiqlarni sahifaning chetiga <b>doira ichiga olib</b> yozing va yechim tugagach
  ularga qayting. Bu 5 soniyalik odat, va u aynan SAT ataylab qoʻygan tuzoqdan
  saqlaydi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>is undefined when</b><span>… boʻlganda aniqlanmagan</span></li>
  <li><b>for what value of x is the expression undefined</b><span>x ning qaysi qiymatida ifoda aniqlanmagan</span></li>
  <li><b>domain restriction</b><span>aniqlanish sohasi cheklovi</span></li>
  <li><b>no solution</b><span>yechim yoʻq</span></li>
  <li><b>all real numbers except</b><span>… dan tashqari barcha haqiqiy sonlar</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>For what value of <i>x</i> is the expression 5 ÷ (<i>x</i><sup>2</sup> − 9)
    undefined?</p>
  </div>
  <ol class="ps-ch">
    <li><i>x</i> = 3 and <i>x</i> = −3</li>
    <li><i>x</i> = 9</li>
    <li><i>x</i> = 3 only</li>
    <li><i>x</i> = 0</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) x = 3 va x = −3</p>
      <p>x<sup>2</sup> − 9 = (x − 3)(x + 3), demak maxraj ikkita qiymatda nolga
      aylanadi.</p>
      <p><b>x = 3 only</b> — kvadrat ildiz olinib, manfiy variant unutilgan.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">x = 3 only</span>
  <span class="ps-trap__why">x<sup>2</sup> = 9 ning <b>ikkita</b> yechimi bor.
  Maxrajni ajratib yozish bu xatoni butunlay yoʻq qiladi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">85 s</span></p>
  <div class="ps-stem__q">
    <p>What is the solution to <i>x</i> ÷ (<i>x</i> − 3) = 3 ÷ (<i>x</i> − 3) + 2?</p>
  </div>
  <ol class="ps-ch">
    <li>There is no solution</li>
    <li><i>x</i> = 3</li>
    <li><i>x</i> = 0</li>
    <li><i>x</i> = 6</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) There is no solution</p>
      <p>Yechim x = 3 beradi, lekin x = 3 da maxraj nolga aylanadi — u
      taqiqlangan.</p>
      <p>Shuning uchun taqiqlarni <b>yechishdan oldin</b> yozib qoʻyish kerak: aks
      holda 3 ni javob deb belgilaysiz.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">x = 3</span>
  <span class="ps-trap__why">Barcha algebraik qadamlar toʻgʻri — javob shundan
  chiqadi. Uni faqat taqiq roʻyxati oʻchiradi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Kasr koʻrgan zahoti, hisoblashdan oldin:</p>
  <ol>
    <li>Har bir maxrajni <b>nolga tenglashtiring</b> va taqiqlarni yozing;</li>
    <li>Kasrdan qutuling (krest koʻpaytirish yoki umumiy maxrajga
        koʻpaytirish);</li>
    <li>Javobni taqiq roʻyxati bilan solishtiring.</li>
  </ol>
  <p>Javoblar orasida «no solution» boʻlsa, uchinchi qadam deyarli har doim
  kerak boʻladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">5 ÷ (x<sup>2</sup> − 9) aniqlanmagan: x = 9</p>
  <p class="pe-good">x = 3 va x = −3</p>
  <p class="pe-fix__why">Maxraj nolga aylanadigan qiymat kerak, maxrajning oʻzi
  emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">x + 1 = 2(x − 3) → x + 1 = 2x − 3</p>
  <p class="pe-good">x + 1 = 2x − 6</p>
  <p class="pe-fix__why">2 qavs ichidagi <b>ikkala</b> hadga koʻpayadi:
  2 × (−3) = −6.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu dars SAT-39 bilan bitta oilada: ikkalasida ham <b>toʻgʻri bajarilgan amal
  notoʻgʻri javob berishi mumkin</b>. Ildizli tenglamada kvadratga koʻtarish yechim
  qoʻshadi, kasrli tenglamada maxrajga koʻpaytirish taqiqni yashiradi. Ikkalasida
  ham davo bitta: oxirida asl tenglamaga qaytish.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Taqiqni topish uchun tenglamani yechish shart emas — faqat <b>maxrajga</b> qarang. Bu savolning oʻzi ham alohida beriladi: «for what value of x is the expression undefined» — u yerda umuman hisoblash yoʻq.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  For what value of <i>x</i> is 1 ÷ (<i>x</i> − 7) undefined?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> = 7.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  For what values of <i>x</i> is 2 ÷ (<i>x</i><sup>2</sup> − 16) undefined?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> = 4 va <i>x</i> = −4 — maxraj
  (x − 4)(x + 4).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Solve: 1 ÷ (<i>x</i> − 2) = 3 ÷ (<i>x</i> + 4)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> = 5 — x + 4 = 3(x − 2) → x + 4 = 3x − 6.
  5 taqiqlanmagan ✓</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Solve: <i>x</i> ÷ (<i>x</i> − 5) = 5 ÷ (<i>x</i> − 5)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yechim yoʻq — x = 5 chiqadi, lekin u
  taqiqlangan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Is (<i>x</i><sup>2</sup> − 4) ÷ (<i>x</i> − 2) the same as <i>x</i> + 2?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Deyarli — x = 2 dan tashqari hamma joyda. Asl ifoda
  x = 2 da aniqlanmagan, x + 2 esa aniqlangan.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>rational equation</b><span>kasrli tenglama</span></li>
  <li><b>denominator</b><span>maxraj</span></li>
  <li><b>undefined</b><span>aniqlanmagan</span></li>
  <li><b>domain restriction</b><span>aniqlanish sohasi cheklovi</span></li>
  <li><b>excluded value</b><span>taqiqlangan (chiqarib tashlangan) qiymat</span></li>
  <li><b>cross-multiply</b><span>krest koʻpaytirish</span></li>
  <li><b>common denominator</b><span>umumiy maxraj</span></li>
  <li><b>no solution</b><span>yechim yoʻq</span></li>
  <li><b>simplify</b><span>soddalashtirmoq</span></li>
  <li><b>all real numbers except</b><span>… dan tashqari barcha sonlar</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Maxrajni nolga tenglashtirib, <b>taqiqlarni avval</b> yozing.</li>
    <li>Javob taqiqlangan chiqsa — toʻgʻri javob <b>«no solution»</b>.</li>
    <li>Kvadrat maxraj <b>ikkita</b> taqiq beradi; qisqartirish taqiqni
        oʻchirmaydi.</li>
  </ul>
</div>
""",
    },
]
