# -*- coding: utf-8 -*-
"""Prime SAT Math — lessons 46–50 (Blok B ning yakuni va Blok C ning boshlanishi).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_SAT.md
Lesson list: tutorial/management/commands/toc_prime_sat_math.txt

⚠️ SARLAVHALAR BAZADAN OLINGAN, aynan (2026-09-04 da toc bazaga moslandi).

⚠️ SAT-49 dan Blok C boshlanadi: matematikasi eng yengil, ingliz tili eng ogʻir.
   Har bir darsda kamida bitta INTERPRETATSIYA savoli boʻlishi shart — pupil
   hisoblashni emas, jumlani oʻqishni oʻrganadi.

⚠️ Kumulyativ (SAT-1…45 erkin, jumladan koʻrsatkichli model y = ab^x):
  • SAT-46 — murakkab foiz; davr yiliga bir marta boʻlmasa nima oʻzgaradi.
  • SAT-47 — funksiya belgilanishi, aniqlanish sohasi va qiymatlar sohasi.
  • SAT-48 — grafik siljishlari va aks ettirishlari.
  • SAT-49 — nisbat, tezlik va proporsiya (Blok C ning boshi).
  • SAT-50 — birliklarni almashtirish; birliklar qisqaradi.
  • ⛔ Foizning oʻzi (SAT-51) YOʻQ; jadval/grafik oʻqish (SAT-53) YOʻQ;
    statistika YOʻQ.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_sat_46_50.py \\
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
    # SAT-46 — compound interest
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-46: Compound Interest and Percent Growth",
        "category": "math",
        "order": 46,
        "summary": (
            "Foiz oldingi foizning ustiga qoʻshilsa — murakkab foiz. Davr yiliga "
            "bir marta boʻlmasa, stavka boʻlinadi va koʻrsatkich koʻpayadi."
        ),
        "stories": ["The Passbook in the Drawer"],
        "content": """
<h2>SAT-46: Compound Interest and Percent Growth</h2>

<p>SAT-45 da har yili bir marta koʻpaytirdik. Endi bank yiliga toʻrt marta yoki oʻn
ikki marta hisoblaydi, va <mark>ikkita son bir vaqtda oʻzgaradi</mark>: stavka
kichrayadi, koʻrsatkich esa kattalashadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>oddiy va murakkab foizni ajratasiz;</li>
    <li>davr yiliga bir necha marta boʻlganda modelni toʻgʻri yozasiz;</li>
    <li>stavkani boʻlish va koʻrsatkichni koʻpaytirishni <b>birga</b> qilasiz;</li>
    <li>tez-tez hisoblash nima uchun koʻproq pul berishini tushuntirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Compounded n times a year</span>
  <span class="pe-chip pe-chip--v">stavka ÷ n</span>
  <span class="pe-op">va</span>
  <span class="pe-chip pe-chip--s">koʻrsatkich × n</span>
</div>

<h3>Oddiy va murakkab foiz</h3>

<p>1,000 dollar, yiliga 5 foiz, uch yil. Ikki xil hisob:</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Yil</th><th>Oddiy foiz (har yili 50)</th><th>Murakkab foiz (har yili ×1.05)</th></tr>
  <tr><td>1</td><td>1,050</td><td class="pm-word__sym">1,050</td></tr>
  <tr><td>2</td><td>1,100</td><td class="pm-word__sym">1,102.50</td></tr>
  <tr><td>3</td><td>1,150</td><td class="pm-word__sym">1,157.625</td></tr>
</table></div>

<p>Farq 7.625 dollar — kichik koʻrinadi, lekin u faqat uch yildan keyin. Yigirma
yilda oddiy foiz 2,000 beradi, murakkab foiz esa 2,653 dan koʻp.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Farqning sababi bitta jumlada: <b>oddiy foiz har doim 1,000 dan olinadi,
  murakkab foiz esa oʻsha yilgi summadan.</b> Ikkinchi yilda 5 foiz 1,050 dan
  olinadi — 50 emas, 52.50.
</div>

<h3>Yiliga bir necha marta</h3>

<p>Bank «8 foiz, choraklab hisoblanadi» desa, u yiliga toʻrt marta hisoblaydi va
har safar yillik stavkaning <b>toʻrtdan biri</b>ni qoʻshadi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">8 foiz ÷ 4 = 2 foiz</span>
    <span class="pm-solve__why">Bir chorakdagi stavka</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2 yil × 4 = 8 chorak</span>
    <span class="pm-solve__why">Necha marta koʻpaytiriladi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">1,000 × 1.02 sakkiz marta ≈ 1,171.66</span>
    <span class="pm-solve__why">Yiliga bir marta boʻlganda 1,166.40 boʻlardi</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Ikkala oʻzgarish <b>birga</b> boʻladi. Faqat stavkani boʻlib, koʻrsatkichni
  oʻsha holicha qoldirish — bu mavzudagi asosiy xato, va tuzoq javob har doim
  shunday hisoblangan son boʻladi.
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Tekshiruv oson: <b>bir yildan keyin</b> qiymat yillik stavkadan bir oz koʻproq
  boʻlishi kerak. 8 foiz choraklab hisoblanganda bir yilda 8.24 foiz beradi —
  8 dan sal koʻp, 8 dan kam emas va ikki barobar ham emas.
</div>

<h3>Kamayish ham xuddi shunday</h3>

<p>Model bir xil, faqat koeffitsient birdan kichik boʻladi (SAT-45). 30,000
dollarlik mashina yiliga 20 foizdan qadrsizlansa: 24,000, keyin 19,200, keyin
15,360. Har yili yoʻqotiladigan pul <b>kamayib boradi</b>, chunki foiz
kichrayayotgan summadan olinadi.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>compounded annually</b><span>yiliga bir marta hisoblanadi</span></li>
  <li><b>compounded quarterly</b><span>choraklab — yiliga toʻrt marta</span></li>
  <li><b>compounded monthly</b><span>oylik — yiliga oʻn ikki marta</span></li>
  <li><b>simple interest</b><span>oddiy foiz — har doim boshlangʻich summadan</span></li>
  <li><b>the initial deposit</b><span>boshlangʻich qoʻyilma</span></li>
  <li><b>to the nearest cent</b><span>eng yaqin sentgacha</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">70 s</span></p>
  <div class="ps-stem__q">
    <p>An account holds 1,000 dollars and earns 5% interest compounded annually.
    To the nearest cent, how much is in the account after 3 years?</p>
  </div>
  <ol class="ps-ch">
    <li>1,157.63 dollars</li>
    <li>1,150.00 dollars</li>
    <li>1,102.50 dollars</li>
    <li>1,215.51 dollars</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 1,157.63 dollars</p>
      <p>1,000 → 1,050 → 1,102.50 → 1,157.625, va yaxlitlanadi.</p>
      <p><b>1,150</b> — oddiy foiz: har yili 50 dan. Savol «compounded»
      degan.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">1,150.00 dollars</span>
  <span class="ps-trap__why">Oddiy foiz hisoblangan. «Compounded» soʻzi
  boʻlgan joyda har yili yangi summadan hisoblanadi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>A deposit of 1,000 dollars earns 8% annual interest compounded quarterly.
    Which expression gives its value after <i>t</i> years?</p>
  </div>
  <ol class="ps-ch">
    <li>1,000(1.02)<sup>4<i>t</i></sup></li>
    <li>1,000(1.08)<sup>4<i>t</i></sup></li>
    <li>1,000(1.02)<sup><i>t</i></sup></li>
    <li>1,000(1.32)<sup><i>t</i></sup></li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 1,000(1.02)<sup>4t</sup></p>
      <p>Stavka toʻrtga boʻlinadi (2 foiz), koʻrsatkich toʻrtga koʻpaytiriladi.</p>
      <p>Tekshiruv t = 1 da: 1,000 × 1.02 toʻrt marta ≈ 1,082.43 — yillik
      8 foizdan bir oz koʻp ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">1,000(1.02)<sup>t</sup></span>
  <span class="ps-trap__why">Stavka boʻlingan, lekin koʻrsatkich oʻzgarmagan.
  Bu model bir yilda atigi 2 foiz beradi — bank sizga 8 foiz vaʼda qilgan
  edi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Javoblar ifoda boʻlsa, <b>bir yilni sanang</b>:</p>
  <ol>
    <li><i>t</i> = 1 qoʻying va har bir variantni hisoblang;</li>
    <li>Yillik stavkadan biroz koʻproq beradigani — toʻgʻri javob;</li>
    <li>Ikki barobar yoki juda kam beradigani darrov oʻchadi.</li>
  </ol>
  <p>«Compounded» soʻzi qaysi ekanini oʻqing: annually 1, quarterly 4,
  monthly 12, daily 365.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">8 foiz choraklab → 1,000(1.02)<sup>t</sup></p>
  <p class="pe-good">1,000(1.02)<sup>4t</sup></p>
  <p class="pe-fix__why">Stavka boʻlinsa, koʻrsatkich shuncha marta
  koʻpayadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">5 foiz, 3 yil → 1,000 + 3(50) = 1,150</p>
  <p class="pe-good">1,157.63</p>
  <p class="pe-fix__why">Ikkinchi yilda foiz 1,050 dan olinadi, 1,000 dan
  emas.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Nima uchun tez-tez hisoblash koʻproq beradi? Chunki <b>qoʻshilgan foiz
  darrov oʻzi ham foiz keltira boshlaydi</b>. Choraklab hisoblanganda birinchi
  chorakning 2 foizi qolgan uch chorak davomida ishlaydi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ustunlik cheksiz emas: 8 foiz kunlik hisoblansa ham yillik natija taxminan
  8.33 foizga yetadi va shu yerda toʻxtaydi. SAT bu chegarani soʻramaydi, lekin
  «kunlik hisoblansa ikki barobar boʻladi» degan javobni ataylab qoʻyadi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  5,000 dollars at 6% compounded annually. How much after 2 years?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">5,618 dollar — 5,300, keyin 5,618.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  The same 5,000 dollars at 6% <i>simple</i> interest for 2 years?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">5,600 dollar — har yili 300 dan. Farqi 18 dollar.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Write the model for 2,000 dollars at 4% compounded quarterly, after <i>t</i>
  years.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">2,000(1.01)<sup>4t</sup> — 4 ÷ 4 = 1 foiz har
  chorakda.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Write the model for 800 dollars at 12% compounded monthly, after <i>t</i>
  years.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">800(1.01)<sup>12t</sup> — 12 ÷ 12 = 1 foiz har
  oyda.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A 30,000-dollar car loses 20% of its value each year. What is it worth after
  3 years?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">15,360 dollar — 24,000, 19,200, 15,360.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>compound interest</b><span>murakkab foiz</span></li>
  <li><b>simple interest</b><span>oddiy foiz</span></li>
  <li><b>compounded annually</b><span>yiliga bir marta hisoblanadi</span></li>
  <li><b>quarterly / monthly</b><span>choraklab / oylik</span></li>
  <li><b>principal / initial deposit</b><span>asosiy summa / boshlangʻich qoʻyilma</span></li>
  <li><b>interest rate</b><span>foiz stavkasi</span></li>
  <li><b>to the nearest cent</b><span>eng yaqin sentgacha</span></li>
  <li><b>depreciates</b><span>qadrsizlanadi</span></li>
  <li><b>accrues</b><span>toʻplanadi, oʻsib boradi</span></li>
  <li><b>balance</b><span>hisobdagi qoldiq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Murakkab foiz <b>oʻsha yilgi summadan</b> olinadi, boshlangʻichdan
        emas.</li>
    <li>Yiliga n marta hisoblansa: <b>stavka ÷ n va koʻrsatkich × n</b> —
        ikkalasi birga.</li>
    <li>Tekshiruv: bir yildan keyingi natija yillik stavkadan <b>bir oz</b>
        koʻp boʻlishi kerak.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-47 — functions: domain, range, evaluation
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-47: Functions — Domain, Range, and Evaluation",
        "category": "math",
        "order": 47,
        "summary": (
            "f(3) — bu «x oʻrniga 3 qoʻying» degani, boshqa hech narsa emas. "
            "Aniqlanish sohasi — ruxsat etilgan kirishlar, qiymatlar sohasi — chiqishlar."
        ),
        "stories": ["What the Machine Will Not Accept"],
        "content": """
<h2>SAT-47: Functions — Domain, Range, and Evaluation</h2>

<p>Funksiya belgilanishi oʻquvchilarni koʻp qoʻrqitadi, lekin unda hech qanday
yangi amal yoʻq. <mark>f(3) — bu «x oʻrniga 3 qoʻying» degani</mark>, va f harfi
koʻpaytuvchi emas.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>f(a) ni bir qadamda hisoblaysiz;</li>
    <li>aniqlanish sohasini ikki narsadan topasiz: maxraj va ildiz;</li>
    <li>qiymatlar sohasini grafik yoki uchdan oʻqiysiz;</li>
    <li>jadval yoki grafikdan f(a) ni topasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Notation</span>
  <span class="pe-chip pe-chip--s">domain = ruxsat etilgan x</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">range = chiqadigan y</span>
</div>

<h3>Qiymatni hisoblash</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">f(x) = 3x<sup>2</sup> − x,  f(−2) = ?</span>
    <span class="pm-solve__why">Har bir x oʻrniga −2 qoʻyamiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3(−2)<sup>2</sup> − (−2)</span>
    <span class="pm-solve__why">Qavs shart: (−2)<sup>2</sup> = +4</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">12 + 2 = 14</span>
    <span class="pm-solve__why">Ikkinchi minus ayirishni qoʻshishga aylantirdi</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Manfiy son qoʻyilganda <b>qavs</b> ishlating. −2<sup>2</sup> va (−2)<sup>2</sup>
  boshqa-boshqa sonlar: birinchisi −4, ikkinchisi +4. Kalkulyator ham shu farqni
  qiladi.
</div>

<h3>Aniqlanish sohasi — faqat ikki narsani qidiring</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Ifodada nima bor</th><th>Shart</th><th>Misol</th></tr>
  <tr><td>maxraj</td><td class="pm-word__sym">nolga teng boʻlmasin</td>
      <td>1 ÷ (x − 2) → x ≠ 2</td></tr>
  <tr><td>kvadrat ildiz</td><td class="pm-word__sym">ichi manfiy boʻlmasin</td>
      <td>√(x − 3) → x ≥ 3</td></tr>
  <tr><td>koʻphad</td><td class="pm-word__sym">hech qanday cheklov yoʻq</td>
      <td>x<sup>2</sup> + 5x → barcha sonlar</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  SAT'da aniqlanish sohasi savoli deyarli har doim shu ikki narsadan biri
  haqida boʻladi. Ifodada na maxraj, na ildiz boʻlmasa — javob «all real
  numbers», va bu ham toʻliq javob hisoblanadi.
</div>

<h3>Qiymatlar sohasi</h3>

<p>Qiymatlar sohasi — funksiya <u>chiqara oladigan</u> sonlar. Uni koʻpincha
uchdan oʻqish mumkin (SAT-35): y = x<sup>2</sup> − 4 ning eng past qiymati −4,
demak qiymatlar sohasi «−4 va undan katta». y = x<sup>2</sup> uchun esa «0 va
undan katta», chunki kvadrat manfiy boʻlmaydi.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Kontekstli masalada aniqlanish sohasini <b>hayot</b> belgilaydi, formula emas.
  «t — soatlar soni» boʻlsa, t manfiy boʻlmaydi; «n — oʻquvchilar soni» boʻlsa,
  n butun va manfiy emas. SAT bu farqni ataylab soʻraydi.
</div>

<h3>Jadval va grafikdan oʻqish</h3>

<p>Jadvalda x va f(x) ustunlari berilsa, f(3) ni topish uchun x = 3 qatorini
qidiring. Grafikda esa x = 3 nuqtasidan yuqoriga chiqib, egri chiziqni
kesgan joyning balandligini oʻqing. Ikkalasi ham hisoblashsiz ish.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>what is the value of f(3)</b><span>f(3) nechaga teng</span></li>
  <li><b>the domain of the function</b><span>aniqlanish sohasi — ruxsat etilgan x</span></li>
  <li><b>the range of the function</b><span>qiymatlar sohasi — chiqadigan y</span></li>
  <li><b>all real numbers except</b><span>… dan tashqari barcha haqiqiy sonlar</span></li>
  <li><b>for which value of x is f(x) = 0</b><span>x ning qaysi qiymatida f(x) nolga teng</span></li>
  <li><b>in the context of the problem</b><span>masala sharoitida</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = 3<i>x</i><sup>2</sup>
    − <i>x</i>. What is the value of <i>f</i>(−2)?</p>
  </div>
  <ol class="ps-ch">
    <li>14</li>
    <li>10</li>
    <li>−14</li>
    <li>−10</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 14</p>
      <p>3(−2)<sup>2</sup> − (−2) = 12 + 2 = 14.</p>
      <p><b>10</b> — ikkinchi minus eʼtibordan qolgan: 12 − 2. Ayirilayotgan son
      manfiy boʻlsa, natija qoʻshiladi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">10</span>
  <span class="ps-trap__why">−(−2) ni −2 deb olgan javob. Ikki minus plyus
  beradi — bu SAT'da eng koʻp yoʻqotiladigan bitta belgi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">55 s</span></p>
  <div class="ps-stem__q">
    <p>What is the domain of <i>g</i>(<i>x</i>) = √(2<i>x</i> − 6)?</p>
  </div>
  <ol class="ps-ch">
    <li><i>x</i> ≥ 3</li>
    <li><i>x</i> ≥ 6</li>
    <li><i>x</i> ≠ 3</li>
    <li>All real numbers</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) x ≥ 3</p>
      <p>Ildiz ostidagi ifoda manfiy boʻlmasligi kerak: 2x − 6 ≥ 0 → x ≥ 3.</p>
      <p>Tekshiruv: x = 3 da √0 = 0 ✓ va x = 2 da √(−2) — haqiqiy son emas ✗</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">x ≥ 6</span>
  <span class="ps-trap__why">Tengsizlik yechilmagan: 6 shundoq koʻchirilgan.
  2x − 6 ≥ 0 dan x ≥ 3 chiqadi, x ≥ 6 emas.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Aniqlanish sohasi savolida ifodaga <b>bir marta</b> qarang:</p>
  <ol>
    <li>Maxraj bormi? → uni nolga tenglashtiring, u qiymat taqiqlanadi;</li>
    <li>Ildiz bormi? → ichini nolga teng yoki katta deb yozing;</li>
    <li>Ikkalasi ham yoʻqmi? → javob «all real numbers».</li>
  </ol>
  <p>Javoblarni tekshirish ham tez: chegaradagi sonni qoʻying va ifoda
  ishlaydimi koʻring.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">f(−2) = 3(−4) + 2 = −10</p>
  <p class="pe-good">3(+4) + 2 = 14</p>
  <p class="pe-fix__why">(−2)<sup>2</sup> = +4. Manfiy sonni qavsga oling.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">√(2x − 6) → x ≥ 6</p>
  <p class="pe-good">x ≥ 3</p>
  <p class="pe-fix__why">2x − 6 ≥ 0 tengsizligini oxirigacha yeching.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>f(x) — koʻpaytma emas.</b> f(3) «f ni 3 ga koʻpaytirish» degani emas, balki
  «funksiyaga 3 ni berish» degani. Bu belgilanish shunchaki qisqartma: har
  safar «x oʻrniga qoʻying» deb oʻqing.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ichma-ich funksiyada — f(g(2)) — <b>ichkaridan boshlang</b>: avval g(2) ni
  hisoblang, chiqqan sonni f ga bering. Tashqaridan boshlash SAT'da doim
  notoʻgʻri javob beradi va u variantlar orasida turadi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  If <i>f</i>(<i>x</i>) = 2<i>x</i> + 1, what is <i>f</i>(3)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">7.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  If <i>f</i>(<i>x</i>) = <i>x</i><sup>2</sup> − 4, what is <i>f</i>(−2)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">0 — (−2)<sup>2</sup> − 4 = 4 − 4.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  What is the domain of <i>h</i>(<i>x</i>) = 1 ÷ (<i>x</i> + 5)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">−5 dan tashqari barcha haqiqiy sonlar.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  What is the range of <i>f</i>(<i>x</i>) = <i>x</i><sup>2</sup> + 1?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">1 va undan katta sonlar — uch (0, 1) da.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  If <i>f</i>(<i>x</i>) = <i>x</i> + 3 and <i>g</i>(<i>x</i>) = 2<i>x</i>, what is
  <i>f</i>(<i>g</i>(2))?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">7 — avval g(2) = 4, keyin f(4) = 7. Ichkaridan
  boshlang.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>function</b><span>funksiya</span></li>
  <li><b>domain</b><span>aniqlanish sohasi</span></li>
  <li><b>range</b><span>qiymatlar sohasi</span></li>
  <li><b>evaluate</b><span>qiymatini hisoblamoq</span></li>
  <li><b>input / output</b><span>kirish / chiqish</span></li>
  <li><b>is defined by</b><span>… bilan berilgan</span></li>
  <li><b>all real numbers</b><span>barcha haqiqiy sonlar</span></li>
  <li><b>undefined</b><span>aniqlanmagan</span></li>
  <li><b>in the context of the problem</b><span>masala sharoitida</span></li>
  <li><b>non-negative</b><span>manfiy boʻlmagan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>f(a) — bu <b>«x oʻrniga a qoʻying»</b>, koʻpaytirish emas.</li>
    <li>Aniqlanish sohasi uchun faqat <b>maxraj va ildiz</b>ni qidiring.</li>
    <li>Manfiy sonni qoʻyganda <b>qavs</b> ishlating.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-48 — transformations
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-48: Function Transformations — Shifts and Reflections",
        "category": "math",
        "order": 48,
        "summary": (
            "Qavs ichidagi oʻzgarish gorizontal va teskari ishlaydi; qavsdan "
            "tashqaridagisi vertikal va kutilganidek."
        ),
        "stories": ["Ten Minutes Later, Every Day"],
        "content": """
<h2>SAT-48: Function Transformations — Shifts and Reflections</h2>

<p>Bitta grafikni bilsangiz, uning oʻnlab qarindoshini chizmasdan tasvirlash
mumkin. Bitta qoida hammasini boshqaradi: <mark>qavs ichidagi oʻzgarish
gorizontal va teskari, qavsdan tashqaridagisi vertikal va toʻgʻri</mark>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>toʻrtta asosiy siljishni ajratasiz;</li>
    <li>ikkita aks ettirishni belgidan aniqlaysiz;</li>
    <li>bir nechta oʻzgarishni ketma-ket qoʻllaysiz;</li>
    <li>gorizontal siljish nima uchun teskari ekanini tushuntirasiz.</li>
  </ul>
</div>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Yozuv</th><th>Nima boʻladi</th><th>Yoʻnalish</th></tr>
  <tr><td>f(x) + 3</td><td class="pm-word__sym">3 birlik yuqoriga</td><td>vertikal, toʻgʻri</td></tr>
  <tr><td>f(x) − 3</td><td class="pm-word__sym">3 birlik pastga</td><td>vertikal, toʻgʻri</td></tr>
  <tr><td>f(x − 3)</td><td class="pm-word__sym">3 birlik <b>oʻngga</b></td><td>gorizontal, teskari</td></tr>
  <tr><td>f(x + 3)</td><td class="pm-word__sym">3 birlik <b>chapga</b></td><td>gorizontal, teskari</td></tr>
  <tr><td>−f(x)</td><td class="pm-word__sym">x oʻqiga nisbatan aks</td><td>yuqori-past agʻdariladi</td></tr>
  <tr><td>f(−x)</td><td class="pm-word__sym">y oʻqiga nisbatan aks</td><td>chap-oʻng agʻdariladi</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  f(x − 3) grafikni <b>oʻngga</b> suradi, chapga emas. Bu darsdagi yagona
  qiyin narsa, va SAT undan tuzoq javob yasaydi.
</div>

<h3>Nima uchun gorizontal siljish teskari</h3>

<p>Sabab bir jumlada. y = f(x − 3) da xuddi oʻsha qiymatni olish uchun x ni
<b>3 ga kattaroq</b> qilish kerak: eski grafikda f(0) qayerda boʻlsa, yangi
grafikda u x = 3 da paydo boʻladi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Eski: f(0) — grafikning 0 dagi qiymati</span>
    <span class="pm-solve__why">Boshlangʻich nuqta</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Yangi: f(x − 3) qavs ichi 0 boʻlishi uchun x = 3</span>
    <span class="pm-solve__why">x − 3 = 0 → x = 3</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Oʻsha qiymat 3 ta oʻngda paydo boʻldi</span>
    <span class="pm-solve__why">Demak grafik oʻngga surildi</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Buni SAT-35 dagi uchi shakli bilan solishtiring: y = (x − 3)<sup>2</sup> ning
  uchi x = 3 da edi — aynan oʻsha qoida, faqat boshqa nom bilan. Ikki dars
  bitta faktni oʻrgatadi.
</div>

<h3>Bir nechta oʻzgarish birga</h3>

<p>g(x) = f(x − 3) + 2 ikkita ish qiladi: 3 birlik oʻngga va 2 birlik yuqoriga.
Tartib ahamiyatsiz, chunki biri gorizontal, ikkinchisi vertikal — ular
bir-biriga aralashmaydi.</p>

<p>h(x) = −f(x) + 1 esa avval agʻdaradi, keyin 1 birlik koʻtaradi. Bu yerda
tartib <b>muhim</b>: ikkala amal ham vertikal.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Adashsangiz, <b>bitta nuqtani kuzating</b>. Eski grafikda (2, 5) nuqta boʻlsa,
  f(x − 3) + 2 da u (5, 7) ga koʻchadi: x ga 3 qoʻshiladi, y ga 2. Bir nuqta
  butun javobni hal qiladi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>shifted 3 units to the right</b><span>3 birlik oʻngga surilgan</span></li>
  <li><b>translated up 2 units</b><span>2 birlik yuqoriga koʻchirilgan</span></li>
  <li><b>reflected across the x-axis</b><span>x oʻqiga nisbatan aks ettirilgan</span></li>
  <li><b>reflected across the y-axis</b><span>y oʻqiga nisbatan aks ettirilgan</span></li>
  <li><b>the graph of y = f(x) is transformed</b><span>grafik oʻzgartirilgan</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>The graph of <i>y</i> = <i>f</i>(<i>x</i>) is transformed to
    <i>y</i> = <i>f</i>(<i>x</i> − 4) + 1. How is the graph moved?</p>
  </div>
  <ol class="ps-ch">
    <li>4 units right and 1 unit up</li>
    <li>4 units left and 1 unit up</li>
    <li>4 units right and 1 unit down</li>
    <li>1 unit right and 4 units up</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 4 units right and 1 unit up</p>
      <p>Qavs ichidagi −4 gorizontal va teskari → oʻngga. Tashqaridagi +1
      vertikal va toʻgʻri → yuqoriga.</p>
      <p>Nuqta bilan tekshiring: (0, 0) → (4, 1).</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">4 units left and 1 unit up</span>
  <span class="ps-trap__why">Minus belgisi «chapga» deb oʻqilgan. Qavs
  <b>ichidagi</b> harakat har doim kutilganning teskarisi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">55 s</span></p>
  <div class="ps-stem__q">
    <p>Which equation gives the graph of <i>y</i> = <i>f</i>(<i>x</i>) reflected
    across the <i>x</i>-axis?</p>
  </div>
  <ol class="ps-ch">
    <li><i>y</i> = −<i>f</i>(<i>x</i>)</li>
    <li><i>y</i> = <i>f</i>(−<i>x</i>)</li>
    <li><i>y</i> = <i>f</i>(<i>x</i>) − 1</li>
    <li><i>y</i> = 1 ÷ <i>f</i>(<i>x</i>)</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) y = −f(x)</p>
      <p>Butun chiqish qiymati manfiyga aylanadi, demak har bir nuqta x oʻqidan
      narigi tomonga oʻtadi: (2, 5) → (2, −5).</p>
      <p><b>f(−x)</b> esa kirishni oʻzgartiradi — u chap-oʻng agʻdaradi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">y = f(−x)</span>
  <span class="ps-trap__why">Minus qavs ichida — bu <b>y</b> oʻqiga nisbatan
  aks. Qaysi oʻq soʻralganini oʻqing.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Har qanday oʻzgartirish savolida <b>bitta nuqta tanlang</b>:</p>
  <ol>
    <li>Eski grafikdan oson nuqta oling, masalan uch yoki kesishish;</li>
    <li>Yangi tenglamada oʻsha qiymat qaysi x da chiqishini toping;</li>
    <li>Nuqtaning qayerga koʻchganini javoblar bilan solishtiring.</li>
  </ol>
  <p>Bu qoidalarni yodlashdan koʻra ishonchli: bir nuqta hech qachon
  adashtirmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">f(x − 4) → 4 birlik chapga</p>
  <p class="pe-good">4 birlik oʻngga</p>
  <p class="pe-fix__why">Qavs ichi nol boʻlishi uchun x = 4 kerak — qiymat
  oʻngda paydo boʻladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">−f(x) → y oʻqiga nisbatan aks</p>
  <p class="pe-good">x oʻqiga nisbatan aks</p>
  <p class="pe-fix__why">Minus qavsdan tashqarida — u chiqishni, yaʼni y ni
  oʻzgartiradi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikki aks ettirishni ajratishning eng qisqa yoʻli: <b>minus qayerda?</b>
  Qavsdan tashqarida boʻlsa y oʻzgaradi (yuqori-past agʻdariladi); qavs ichida
  boʻlsa x oʻzgaradi (chap-oʻng agʻdariladi).
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Baʼzi grafiklarda aks ettirish <b>hech narsani oʻzgartirmaydi</b>:
  y = x<sup>2</sup> ning y oʻqiga nisbatan aksi oʻzi bilan bir xil, chunki u
  allaqachon simmetrik. SAT bunday savolni «which transformation leaves the
  graph unchanged» deb beradi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  How does the graph of <i>y</i> = <i>f</i>(<i>x</i>) + 5 differ from
  <i>y</i> = <i>f</i>(<i>x</i>)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">5 birlik yuqoriga surilgan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  How does the graph of <i>y</i> = <i>f</i>(<i>x</i> + 2) differ from
  <i>y</i> = <i>f</i>(<i>x</i>)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">2 birlik chapga — qavs ichi teskari ishlaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  The point (1, 6) is on <i>y</i> = <i>f</i>(<i>x</i>). Which point is on
  <i>y</i> = <i>f</i>(<i>x</i> − 2) + 3?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(3, 9) — x ga 2 qoʻshiladi, y ga 3.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  The point (4, −2) is on <i>y</i> = <i>f</i>(<i>x</i>). Which point is on
  <i>y</i> = −<i>f</i>(<i>x</i>)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(4, 2) — x oʻzgarmaydi, y ning ishorasi
  almashadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Which transformation leaves the graph of <i>y</i> = <i>x</i><sup>2</sup>
  unchanged?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">y oʻqiga nisbatan aks ettirish — grafik allaqachon
  simmetrik.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>transformation</b><span>oʻzgartirish</span></li>
  <li><b>shift / translate</b><span>surmoq / koʻchirmoq</span></li>
  <li><b>reflect across</b><span>… ga nisbatan aks ettirmoq</span></li>
  <li><b>units to the right</b><span>birlik oʻngga</span></li>
  <li><b>horizontal / vertical</b><span>gorizontal / vertikal</span></li>
  <li><b>the parent function</b><span>asosiy funksiya</span></li>
  <li><b>leaves it unchanged</b><span>oʻzgarishsiz qoldiradi</span></li>
  <li><b>corresponding point</b><span>mos nuqta</span></li>
  <li><b>symmetric</b><span>simmetrik</span></li>
  <li><b>flipped</b><span>agʻdarilgan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Qavs ichi — gorizontal va teskari</b>; qavsdan tashqarisi —
        vertikal va toʻgʻri.</li>
    <li><b>−f(x)</b> x oʻqiga, <b>f(−x)</b> y oʻqiga nisbatan aks ettiradi.</li>
    <li>Ishonchli usul — <b>bitta nuqtani kuzatish</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-49 — ratios, rates and proportions  (Blok C boshlanadi)
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-49: Ratios, Rates, and Proportions",
        "category": "math",
        "order": 49,
        "summary": (
            "Blok C ochiladi: matematikasi yengil, jumlasi ogʻir. Nisbat qismlarni "
            "sanaydi, proporsiya esa ikki nisbatni tenglashtiradi."
        ),
        "stories": ["One, Two, Three"],
        "content": """
<h2>SAT-49: Ratios, Rates, and Proportions</h2>

<p>Shu darsdan <b>Blok C</b> boshlanadi, va uning tabiati boshqacha:
<mark>matematikasi butun testdagi eng yengili, ingliz tili esa eng ogʻiri</mark>.
Bu yerda ball yoʻqotadigan oʻquvchi hisoblashni bilmaganidan emas, jumlani
notoʻgʻri oʻqiganidan yoʻqotadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>nisbatni qismlar soni sifatida oʻqiysiz;</li>
    <li>«qismga qism» va «qismga butun» nisbatlarini ajratasiz;</li>
    <li>proporsiyani krest koʻpaytirish bilan yechasiz;</li>
    <li>savol nimani soʻrayotganini javob berishdan oldin belgilaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">A ratio counts parts</span>
  <span class="pe-chip pe-chip--s">3 : 5</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">jami 8 qism</span>
</div>

<h3>Nisbat — qismlarni sanash</h3>

<p>Bir sinfda oʻgʻil va qizlar nisbati 3 : 5 boʻlsa, bu 3 oʻgʻil va 5 qiz bor
degani <u>emas</u>. Bu sinf <b>8 teng qismga</b> boʻlinadi degani: 3 tasi
oʻgʻillar, 5 tasi qizlar.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Sinfda 40 oʻquvchi, nisbat 3 : 5</span>
    <span class="pm-solve__why">Jami 3 + 5 = 8 qism</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">40 ÷ 8 = 5</span>
    <span class="pm-solve__why">Bir qismda 5 oʻquvchi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">15 oʻgʻil, 25 qiz</span>
    <span class="pm-solve__why">3 × 5 va 5 × 5; tekshiruv: 15 + 25 = 40 ✓</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  <b>«3 to 5» va «3 out of 5» bir xil emas.</b> Birinchisi qismga qism (jami 8),
  ikkinchisi qismga butun (jami 5). Bitta soʻz butun javobni oʻzgartiradi, va
  SAT ikkalasini ham ishlatadi.
</div>

<h3>Proporsiya — ikki nisbat teng</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 ÷ 4 = x ÷ 20</span>
    <span class="pm-solve__why">Ikki nisbat teng deb yozildi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 × 20 = 4x</span>
    <span class="pm-solve__why">Krest koʻpaytirish (SAT-40)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 15</span>
    <span class="pm-solve__why">Tekshiruv: 15 ÷ 20 = 0.75 va 3 ÷ 4 = 0.75 ✓</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Proporsiya yozganda <b>birliklarni ustma-ust qoʻying</b>: kilometr ustida
  kilometr, soat ustida soat. Birliklar chalkashsa javob ham chalkashadi, va
  bu xatoni keyin topib boʻlmaydi.
</div>

<h3>Tezlik — birlikka nisbatan</h3>

<p>Tezlik ham nisbat, faqat maxraji bir birlik. 240 km ni 3 soatda bosib
oʻtgan mashina soatiga 80 km yuradi. SAT bunday savolni koʻpincha teskari
tomonga beradi: tezlik va vaqt berilib, masofa soʻraladi.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>the ratio of A to B is 3 to 5</b><span>A ning B ga nisbati 3 : 5 (jami 8 qism)</span></li>
  <li><b>3 out of every 5</b><span>har 5 tadan 3 tasi (jami 5)</span></li>
  <li><b>for every 2 cups of flour</b><span>har 2 stakan un uchun</span></li>
  <li><b>at this rate</b><span>shu tezlikda davom etsa</span></li>
  <li><b>directly proportional</b><span>toʻgʻri proporsional</span></li>
  <li><b>how many more</b><span>nechtaga koʻp — farq soʻralyapti</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>In a class of 40 students, the ratio of boys to girls is 3 to 5. How many
    more girls than boys are there?</p>
  </div>
  <ol class="ps-ch">
    <li>10</li>
    <li>2</li>
    <li>25</li>
    <li>15</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 10</p>
      <p>8 qism, har biri 5 ta: 15 oʻgʻil va 25 qiz. Farqi 25 − 15 = 10.</p>
      <p><b>2</b> — nisbatdagi qismlar farqi (5 − 3), oʻquvchilar farqi emas.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">25</span>
  <span class="ps-trap__why">Qizlar soni yozilgan, savol esa <b>farqni</b>
  soʻragan. «How many more» degan ibora har doim ayirishni bildiradi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">70 s</span></p>
  <div class="ps-stem__q">
    <p>A recipe uses 2 cups of flour for every 3 cups of milk. If a baker uses
    18 cups of milk, how many cups of flour are needed?</p>
  </div>
  <ol class="ps-ch">
    <li>12</li>
    <li>27</li>
    <li>9</li>
    <li>36</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 12</p>
      <p>2 ÷ 3 = x ÷ 18 → 3x = 36 → x = 12.</p>
      <p>Aql bilan tekshiring: sut 6 barobar oshdi (3 dan 18 ga), demak un
      ham 6 barobar: 2 × 6 = 12 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">27</span>
  <span class="ps-trap__why">Proporsiya teskari yozilgan: 3 ÷ 2 = x ÷ 18.
  Un sutdan <b>kam</b> boʻlishi kerak edi — javob mantiqan ham notoʻgʻri.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Blok C ning birinchi qoidasi: <b>savolni oxirigacha oʻqing va nima
  soʻralganini belgilang</b>.</p>
  <ol>
    <li>Soʻralayotgan narsani <b>doira ichiga oling</b>: qizlar soni? farq?
        jami?</li>
    <li>Hisoblang;</li>
    <li>Javobni belgilashdan oldin doiraga qayting.</li>
  </ol>
  <p>Bu blokda yoʻqotilgan ballarning koʻpchiligi hisob xatosi emas —
  toʻgʻri hisoblab, notoʻgʻri sonni belgilash.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Nisbat 3 : 5, jami 40 → 3 oʻgʻil va 5 qiz</p>
  <p class="pe-good">15 oʻgʻil va 25 qiz</p>
  <p class="pe-fix__why">Nisbat qismlarni beradi, sonlarni emas: 40 ni 8 qismga
  boʻling.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">2 stakan un, 3 stakan sut → 18 sutga 27 un</p>
  <p class="pe-good">12 stakan un</p>
  <p class="pe-fix__why">Proporsiya teskari yozilgan. Un har doim sutdan kam
  boʻlishi kerak.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Javob chiqqach, uni <b>aql bilan tekshiring</b>. Nisbatda un kamroq boʻlsa,
  javob ham kamroq chiqishi shart. Bu bir soniyalik tekshiruv teskari yozilgan
  proporsiyani har safar tutadi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Nisbat <b>qisqartirilgan</b> boʻlishi mumkin: 6 : 10 va 3 : 5 bir xil nisbat.
  Shuning uchun «nisbati 3 : 5» degan jumla sinfda 8 kishi borligini
  anglatmaydi — u faqat ulushni aytadi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Blok C da har bir savolda <b>birliklar</b> bor: stakan, kilometr, soat,
  oʻquvchi. Javobingizning birligi savoldagi birlik bilan bir xilmi — shuni
  tekshirish SAT-50 dagi asosiy koʻnikmaning boshlanishi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  The ratio of red to blue marbles is 2 to 7. If there are 63 marbles in total,
  how many are blue?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">49 — 9 qism, har biri 7 ta; 7 × 7 = 49.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Solve: 5 ÷ 8 = <i>x</i> ÷ 32</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> = 20 — 8 ga 4 koʻpaytirildi, demak 5 ga
  ham.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A car travels 240 kilometres in 3 hours. At this rate, how far does it travel
  in 5 hours?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">400 km — soatiga 80 km.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  In a bag the ratio of apples to pears is 4 to 3, and there are 12 pears. How
  many apples are there?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">16 — 3 qism 12 ta boʻlsa, bir qism 4 ta.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  In a group, 3 out of every 5 people wear glasses. In a group of 45, how many
  wear glasses?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">27 — «out of» qismga butun: 45 ÷ 5 = 9, va
  3 × 9 = 27.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>ratio</b><span>nisbat</span></li>
  <li><b>proportion</b><span>proporsiya (ikki nisbat tengligi)</span></li>
  <li><b>rate</b><span>tezlik, birlikka nisbat</span></li>
  <li><b>for every</b><span>har … uchun</span></li>
  <li><b>out of every</b><span>har … tadan (qismga butun)</span></li>
  <li><b>at this rate</b><span>shu tezlikda</span></li>
  <li><b>how many more</b><span>nechtaga koʻp (farq)</span></li>
  <li><b>directly proportional</b><span>toʻgʻri proporsional</span></li>
  <li><b>in total</b><span>jami</span></li>
  <li><b>per</b><span>… ga, har biriga</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Nisbat <b>qismlarni</b> sanaydi: 3 : 5 degani jami 8 qism.</li>
    <li><b>«to» va «out of»</b> boshqa-boshqa: qismga qism va qismga butun.</li>
    <li>Javob berishdan oldin <b>nima soʻralganiga</b> qayting — Blok C
        ballari shu yerda yoʻqoladi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-50 — unit conversions
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-50: Unit Conversions and Dimensional Analysis",
        "category": "math",
        "order": 50,
        "summary": (
            "Birlikni almashtirish — birga koʻpaytirish. Kerakli birlik yuqorida, "
            "keraksizi pastda tursa, u qisqaradi."
        ),
        "stories": ["The Orbiter That Came In Too Low"],
        "content": """
<h2>SAT-50: Unit Conversions and Dimensional Analysis</h2>

<p>Bu darsda hisoblash oson, va shuning uchun SAT uni chalkashtirish orqali
qiyinlashtiradi: koʻpaytirish kerakmi yoki boʻlish? Javob esa hech qachon
taxminga qolmaydi — <mark>birliklarning oʻzi qaysi tomonga yozishni
aytadi</mark>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>almashtirishni kasr koʻrinishida yozasiz;</li>
    <li>keraksiz birlikni qisqartirasiz;</li>
    <li>ketma-ket bir necha almashtirishni bir qatorda bajarasiz;</li>
    <li>javobning birligini tekshirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The trick</span>
  <span class="pe-chip pe-chip--v">keraksiz birlik pastga</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">qisqaradi</span>
</div>

<h3>Asosiy gʻoya</h3>

<p>1,000 metr va 1 kilometr bir xil uzunlik. Demak «1,000 metr ÷ 1 kilometr»
kasri <b>birga teng</b>, va birga koʻpaytirish hech narsani oʻzgartirmaydi —
faqat birlikni almashtiradi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">5 kilometr × (1,000 metr ÷ 1 kilometr)</span>
    <span class="pm-solve__why">Kilometr yuqorida ham, pastda ham — qisqaradi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">5,000 metr</span>
    <span class="pm-solve__why">Faqat metr qoldi — javobning birligi toʻgʻri</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Koʻpaytirish yoki boʻlish haqida <b>oʻylamang</b>. Kasrni shunday yozingki,
  keraksiz birlik pastda tursin — u qisqaradi va toʻgʻri amal oʻz-oʻzidan
  chiqadi. Bu usul «dimensional analysis» deyiladi.
</div>

<h3>Ketma-ket almashtirish</h3>

<p>Soatiga 90 kilometr — bu sekundiga necha metr? Ikki almashtirish kerak:
kilometrni metrga va soatni sekundga.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">90 km ÷ soat</span>
    <span class="pm-solve__why">Boshlangʻich holat</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">× (1,000 metr ÷ 1 km)</span>
    <span class="pm-solve__why">Kilometr qisqardi → 90,000 metr ÷ soat</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">× (1 soat ÷ 3,600 sekund)</span>
    <span class="pm-solve__why">Soat qisqarishi uchun u <b>yuqorida</b> yozildi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">90,000 ÷ 3,600 = 25 metr ÷ sekund</span>
    <span class="pm-solve__why">Faqat metr va sekund qoldi ✓</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Ikkinchi kasrda soat <b>yuqorida</b> turibdi. Sababi: birinchi ifodada soat
  pastda edi, va qisqarishi uchun u qarama-qarshi tomonda boʻlishi kerak.
  Kasrni notoʻgʻri tomonga yozsangiz javob 3,600 barobar xato chiqadi.
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  SAT kerakli almashtirish sonlarini <b>savolning oʻzida beradi</b> (masalan
  «1 mile = 5,280 feet»). Ularni yodlash shart emas — kerak boʻlgani faqat
  qaysi tomonga yozishni bilish.
</div>

<h3>Yuza va hajm — koʻrsatkichga eʼtibor</h3>

<p>1 metr = 100 santimetr, lekin 1 kvadrat metr = 10,000 kvadrat santimetr,
chunki koeffitsient <b>ikki marta</b> qoʻllanadi. Kub metr uchun esa uch
marta: 1,000,000 kub santimetr.</p>

<h3>Ifoda koʻrinishidagi savol</h3>

<p>SAT bu mavzuni koʻpincha hisoblatmaydi, balki toʻgʻri <b>ifodani</b>
tanlatadi. Bunday savolda javob variantlarining faqat birlik tomonini
tekshirish yetarli — sonlarni umuman hisoblamaysiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">45 daqiqada 12 litr. Soatiga necha litr?</span>
    <span class="pm-solve__why">Daqiqani soatga aylantirish kerak</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(12 litr ÷ 45 daqiqa) × (60 daqiqa ÷ 1 soat)</span>
    <span class="pm-solve__why">Daqiqa yuqorida ham, pastda ham — qisqaradi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">720 ÷ 45 = 16 litr har soatda</span>
    <span class="pm-solve__why">Qolgan birlik: litr ÷ soat ✓</span>
  </div>
</div>

<p>Diqqat: bu yerda 60 <b>yuqorida</b> turibdi, chunki daqiqa boshida pastda
edi. Agar kasr teskari yozilsa, javob 9 barobar kichik chiqadi va birligi ham
notoʻgʻri boʻladi.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>convert to</b><span>… ga aylantiring</span></li>
  <li><b>1 mile = 5,280 feet</b><span>beriladigan almashtirish sherti</span></li>
  <li><b>in metres per second</b><span>sekundiga metr hisobida</span></li>
  <li><b>rounded to the nearest tenth</b><span>oʻndan bir aniqlikda</span></li>
  <li><b>which expression gives</b><span>qaysi ifoda beradi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>A car travels at 90 kilometres per hour. What is its speed in metres per
    second? (1 kilometre = 1,000 metres)</p>
  </div>
  <ol class="ps-ch">
    <li>25</li>
    <li>90</li>
    <li>1.5</li>
    <li>324</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 25</p>
      <p>90,000 metr har soatda, va bir soatda 3,600 sekund bor:
      90,000 ÷ 3,600 = 25.</p>
      <p><b>1.5</b> — faqat daqiqaga aylantirilgan (90 ÷ 60), sekundga
      emas.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">324</span>
  <span class="ps-trap__why">3,600 ga boʻlish oʻrniga koʻpaytirilgan va keyin
  qayta boʻlingan. Birliklarni yozib qoʻysangiz, bu xato koʻrinib
  qoladi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">70 s</span></p>
  <div class="ps-stem__q">
    <p>A runner moves at 60 miles per hour. What is this speed in feet per
    second? (1 mile = 5,280 feet)</p>
  </div>
  <ol class="ps-ch">
    <li>88</li>
    <li>60</li>
    <li>5,280</li>
    <li>1,320</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 88</p>
      <p>60 × 5,280 = 316,800 fut har soatda, va 316,800 ÷ 3,600 = 88.</p>
      <p>Foydali fakt: soatiga 60 milya — bu sekundiga 88 fut, va u har doim
      shunday.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">1,320</span>
  <span class="ps-trap__why">Faqat daqiqaga boʻlingan (316,800 ÷ 60 ÷ 4 emas,
  balki 5,280 ÷ 4). Ikkala almashtirish ham bajarilishi shart.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Har bir almashtirishda <b>birliklarni yozing</b> — sonlarnigina emas:</p>
  <ol>
    <li>Boshlangʻich miqdorni birligi bilan yozing;</li>
    <li>Har bir kasrni keraksiz birlik qisqaradigan tomonga yozing;</li>
    <li>Oxirida qolgan birlik savoldagi birlik bilan bir xilmi — tekshiring.</li>
  </ol>
  <p>Uchinchi qadam bu mavzudagi deyarli har qanday xatoni tutadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">90 km/soat → 90 × 3,600 metr/sekund</p>
  <p class="pe-good">90,000 ÷ 3,600 = 25</p>
  <p class="pe-fix__why">Sekund soatdan <b>kichik</b>, demak sekunddagi masofa
  ham kichikroq boʻlishi kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">1 kvadrat metr = 100 kvadrat santimetr</p>
  <p class="pe-good">10,000 kvadrat santimetr</p>
  <p class="pe-fix__why">Yuzada koeffitsient ikki marta qoʻllanadi:
  100 × 100.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Javobni <b>aql bilan tekshiring</b>: katta birlikdan kichigiga oʻtsangiz son
  oshadi (kilometrdan metrga), kichigidan kattasiga oʻtsangiz kamayadi
  (sekunddan soatga). Bu bir soniyalik tekshiruv teskari amalni har safar
  tutadi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  SAT'da bu savol koʻpincha <b>ifoda</b> koʻrinishida beriladi: «which
  expression converts…». Bunday holda hisoblamang — faqat qaysi variantda
  keraksiz birlik qisqarishini koʻring.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Amerika birliklari (milya, fut, dyuym, funt, gallon) SAT'da uchraydi, lekin
  <b>almashtirish soni har doim savolda beriladi</b>. Ularni yodlashga vaqt
  sarflamang.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Convert 7 kilometres to metres.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">7,000 metr.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Convert 180 minutes to hours.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">3 soat — kichik birlikdan kattasiga, demak son
  kamayadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A tap fills 3 litres per minute. How many litres in 2 hours?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">360 litr — 3 × 60 × 2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Convert 36 kilometres per hour to metres per second.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">10 — 36,000 ÷ 3,600.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  How many square centimetres are in 3 square metres?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">30,000 — har kvadrat metrda 10,000.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>convert</b><span>aylantirmoq</span></li>
  <li><b>unit</b><span>birlik</span></li>
  <li><b>conversion factor</b><span>almashtirish koeffitsienti</span></li>
  <li><b>cancel</b><span>qisqarmoq</span></li>
  <li><b>per</b><span>… ga (har biriga)</span></li>
  <li><b>metres per second</b><span>sekundiga metr</span></li>
  <li><b>dimensional analysis</b><span>birliklar tahlili</span></li>
  <li><b>square metre</b><span>kvadrat metr</span></li>
  <li><b>cubic centimetre</b><span>kub santimetr</span></li>
  <li><b>rounded to the nearest tenth</b><span>oʻndan bir aniqlikda</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Almashtirish — <b>birga koʻpaytirish</b>; kasrni keraksiz birlik
        qisqaradigan tomonga yozing.</li>
    <li>Har bir qadamda <b>birlikni yozing</b>, sonnigina emas.</li>
    <li>Yuzada koeffitsient <b>ikki marta</b>, hajmda <b>uch marta</b>
        qoʻllanadi.</li>
  </ul>
</div>
""",
    },
]
