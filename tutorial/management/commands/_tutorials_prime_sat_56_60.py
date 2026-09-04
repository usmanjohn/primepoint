# -*- coding: utf-8 -*-
"""Prime SAT Math — lessons 56–60 (tarqalish, ehtimollik, tanlanma).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_SAT.md
Lesson list: tutorial/management/commands/toc_prime_sat_math.txt

⚠️ SARLAVHALAR BAZADAN OLINGAN, aynan.

⚠️ Blok C: matematikasi yengil, jumlasi ogʻir. Har darsda interpretatsiya
   savoli. SAT-57 butunlay interpretatsiya — standart ogʻish HISOBLANMAYDI,
   faqat TAQQOSLANADI.

⚠️ Kumulyativ (SAT-1…55 erkin, jumladan foiz, jadval, oʻrtacha va mediana):
  • SAT-56 — moda, oraliq va chetdagi qiymat; qaysi oʻlchov nimaga sezgir.
  • SAT-57 — standart ogʻish: faqat taqqoslash, hisoblash emas.
  • SAT-58 — sodda va bogʻliqsiz hodisalar ehtimoli.
  • SAT-59 — shartli ehtimollik: «given that» maxrajni oʻzgartiradi.
  • SAT-60 — tanlanma soʻrovlar va tasodifiy tanlash; xulosa kimga tegishli.
  • ⛔ Tanlanma xatosi (SAT-61) va tajriba dizayni (SAT-62) YOʻQ.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_sat_56_60.py \\
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
    # SAT-56 — mode, range, outliers
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-56: Mode, Range, and Outliers",
        "category": "math",
        "order": 56,
        "summary": (
            "Moda — eng koʻp uchragan qiymat, oraliq — eng kattadan eng kichigini "
            "ayirish. Chetdagi qiymat oraliqni buzadi, modaga tegmaydi."
        ),
        "stories": ["The Day the Needle Moved"],
        "content": """
<h2>SAT-56: Mode, Range, and Outliers</h2>

<p>SAT-55 da markazni oʻlchadik. Endi <mark>tarqalishni</mark> oʻlchaymiz — va bu
yerda ikkita juda oddiy son bor, ularning har biri butunlay boshqa narsaga
sezgir.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>modani topasiz va u bir nechta yoki umuman boʻlmasligini bilasiz;</li>
    <li>oraliqni <b>bitta son</b> sifatida yozasiz;</li>
    <li>chetdagi qiymat qaysi oʻlchovni buzishini aytasiz;</li>
    <li>toʻrtta oʻlchovni bitta jadvalda solishtirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Two simple numbers</span>
  <span class="pe-chip pe-chip--v">mode = eng koʻp uchragan</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">range = eng katta − eng kichik</span>
</div>

<h3>Moda</h3>

<p>3, 5, 5, 7, 9 qatorida moda 5 — u ikki marta uchraydi, qolganlari bir
martadan. Modaning ikki gʻalati xossasi bor, va SAT ikkalasini ham soʻraydi:</p>

<ul>
  <li>moda <b>bir nechta</b> boʻlishi mumkin: 2, 2, 5, 5, 9 da ikkita moda bor;</li>
  <li>moda <b>umuman boʻlmasligi</b> mumkin: 1, 2, 3, 4 da hamma qiymat bir
      martadan uchraydi.</li>
</ul>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Moda — yagona oʻlchov boʻlib, u <b>son boʻlmagan</b> maʼlumotda ham
  ishlaydi. Eng koʻp sotilgan rang yoki eng koʻp tanlangan javob — bular ham
  moda. Oʻrtacha rangni hisoblab boʻlmaydi.
</div>

<h3>Oraliq</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3, 5, 5, 7, 9</span>
    <span class="pm-solve__why">Eng katta 9, eng kichik 3</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Oraliq = 9 − 3 = 6</span>
    <span class="pm-solve__why">Bu <b>bitta son</b>, «3 dan 9 gacha» emas</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Oraliq — ayirmaning natijasi, oraliqning oʻzi emas. Javob variantlarida
  «from 3 to 9» degan variant turishi mumkin va u <b>notoʻgʻri</b>: SAT'da
  «range» bitta son.
</div>

<h3>Chetdagi qiymat nimani buzadi</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Maʼlumot</th><th>Mean</th><th>Median</th><th>Mode</th><th>Range</th></tr>
  <tr><td>3, 5, 5, 7, 9</td><td>5.8</td><td>5</td><td class="pm-word__sym">5</td><td>6</td></tr>
  <tr><td>3, 5, 5, 7, 90</td><td class="pm-word__sym">22</td><td>5</td>
      <td class="pm-word__sym">5</td><td class="pm-word__sym">87</td></tr>
</table></div>

<p>Bitta sonni 9 dan 90 ga oʻzgartirdik. <b>Oʻrta arifmetik</b> va
<b>oraliq</b> keskin oʻzgardi; <b>mediana</b> va <b>moda</b> umuman
qimirlamadi.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Sababi bitta jumlada: oʻrta arifmetik va oraliq <b>qiymatlarning
  kattaligini</b> ishlatadi, mediana va moda esa faqat <b>tartib va
  takrorlanishni</b>. Shu farqni bilsangiz, «which measure is unaffected»
  turidagi savollarni hisoblamasdan yechasiz.
</div>

<h3>Chetdagi qiymatni olib tashlash</h3>

<p>SAT koʻpincha «chetdagi qiymat olib tashlansa nima oʻzgaradi?» deb soʻraydi.
Yuqoridagi ikkinchi qatordan 90 ni olib tashlasak: oʻrta arifmetik 22 dan
5 ga tushadi, oraliq 87 dan 4 ga, mediana esa 5 dan 5 ga — yaʼni deyarli
oʻzgarmaydi.</p>

<h3>Toʻrtta oʻlchov bitta maʼlumotda</h3>

<p>SAT baʼzan bitta qatordan toʻrttala oʻlchovni ham soʻraydi. Ularni tartib
bilan hisoblash odat qiling — chalkashlik shu yerda tugaydi.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Qadam</th><th>Nima qilinadi</th><th>2, 4, 4, 6, 9 uchun</th></tr>
  <tr><td>1</td><td>tartiblang</td><td class="pm-word__sym">2, 4, 4, 6, 9</td></tr>
  <tr><td>2</td><td>oʻrtadagi qiymat</td><td class="pm-word__sym">mediana 4</td></tr>
  <tr><td>3</td><td>yigʻindi ÷ soni</td><td class="pm-word__sym">oʻrtacha 5</td></tr>
  <tr><td>4</td><td>eng koʻp uchragani</td><td class="pm-word__sym">moda 4</td></tr>
  <tr><td>5</td><td>chekkalar ayirmasi</td><td class="pm-word__sym">oraliq 7</td></tr>
</table></div>

<p>Eʼtibor bering: bu qatorda oʻrtacha medianadan katta. Sababi — 9 boshqa
qiymatlardan ancha uzoq va u oʻrtachani yuqoriga tortmoqda.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>the mode of the data</b><span>maʼlumotning modasi</span></li>
  <li><b>the range of the data</b><span>oraliq — bitta son</span></li>
  <li><b>an outlier</b><span>chetdagi qiymat</span></li>
  <li><b>which measure is unaffected</b><span>qaysi oʻlchov oʻzgarmaydi</span></li>
  <li><b>if the outlier is removed</b><span>chetdagi qiymat olib tashlansa</span></li>
  <li><b>bimodal</b><span>ikki modali</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>What is the range of the data set 12, 7, 19, 7, 15?</p>
  </div>
  <ol class="ps-ch">
    <li>12</li>
    <li>7</li>
    <li>From 7 to 19</li>
    <li>60</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 12</p>
      <p>19 − 7 = 12.</p>
      <p><b>7</b> — bu moda (ikki marta uchraydi), oraliq emas.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">From 7 to 19</span>
  <span class="ps-trap__why">Kundalik nutqda «range» oraliqni bildiradi, SAT'da
  esa <b>bitta son</b> — ayirma. Bu variant ataylab qoʻyiladi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>The value 90 is added to the data set 3, 5, 5, 7, 9. Which measure remains
    unchanged?</p>
  </div>
  <ol class="ps-ch">
    <li>The mode</li>
    <li>The mean</li>
    <li>The range</li>
    <li>None of them</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) The mode</p>
      <p>Moda 5 boʻlib qoladi — 90 faqat bir marta uchraydi.</p>
      <p>Oʻrta arifmetik 5.8 dan 19.83 ga, oraliq esa 6 dan 87 ga oʻzgaradi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">The range</span>
  <span class="ps-trap__why">Oraliq chetdagi qiymatga <b>eng sezgir</b>
  oʻlchov: u faqat ikki chekka qiymatdan tuzilgan, va 90 aynan chekkaga
  tushdi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Toʻrt oʻlchovni ikki guruhga ajratib yodlang:</p>
  <ol>
    <li><b>Kattalikka sezgir</b>: oʻrta arifmetik va oraliq;</li>
    <li><b>Kattalikka sezgir emas</b>: mediana va moda;</li>
    <li>«Unaffected» soʻrasa — ikkinchi guruhdan tanlang.</li>
  </ol>
  <p>Bu ikki qatorli jadval Blok C dagi statistika savollarining koʻpini
  hisoblashsiz hal qiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Range = «7 dan 19 gacha»</p>
  <p class="pe-good">Range = 12</p>
  <p class="pe-fix__why">SAT'da oraliq — ayirma, bitta son.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">1, 2, 3, 4 ning modasi 1</p>
  <p class="pe-good">Modasi yoʻq</p>
  <p class="pe-fix__why">Hamma qiymat bir martadan uchrasa, moda mavjud
  emas.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Chetdagi qiymatni <b>oʻz-oʻzidan xato deb hisoblamang</b>. U yozuv xatosi ham
  boʻlishi mumkin, haqiqiy va muhim hodisa ham. Uni tashlab yuborishdan oldin
  nima uchun paydo boʻlganini soʻrash kerak.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oraliq faqat <b>ikkita</b> sondan tuzilgan — eng katta va eng kichik.
  Oʻrtadagi yuzta qiymat qanday joylashganini u umuman koʻrsatmaydi. Shuning
  uchun tarqalishning jiddiy oʻlchovi keyingi darsda keladi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  What is the mode of 4, 6, 6, 8, 11?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">6.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  What is the range of 4, 6, 6, 8, 11?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">7 — 11 − 4.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  What is the mode of 2, 3, 4, 5?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Moda yoʻq — hamma qiymat bir martadan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  A data set has range 0. What can you say about it?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Barcha qiymatlar teng — eng katta va eng kichik bir
  xil.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Which measure is most affected by a single very large value?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Oraliq — u faqat chekka qiymatlardan
  tuzilgan.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>mode</b><span>moda</span></li>
  <li><b>range</b><span>oraliq (ayirma)</span></li>
  <li><b>outlier</b><span>chetdagi qiymat</span></li>
  <li><b>bimodal</b><span>ikki modali</span></li>
  <li><b>occurs most often</b><span>eng koʻp uchraydi</span></li>
  <li><b>unaffected by</b><span>… ga bogʻliq emas</span></li>
  <li><b>the greatest value</b><span>eng katta qiymat</span></li>
  <li><b>categorical data</b><span>toifaviy maʼlumot (son emas)</span></li>
  <li><b>data entry error</b><span>yozuvdagi xato</span></li>
  <li><b>spread</b><span>tarqalish</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Oraliq — bitta son</b>: eng katta minus eng kichik.</li>
    <li>Moda <b>bir nechta yoki umuman boʻlmasligi</b> mumkin.</li>
    <li>Chetdagi qiymat <b>oʻrta arifmetik va oraliqni</b> buzadi, mediana va
        modaga tegmaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-57 — standard deviation
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-57: Standard Deviation — Measuring Data Spread",
        "category": "math",
        "order": 57,
        "summary": (
            "SAT sizdan standart ogʻishni HISOBLASHNI hech qachon soʻramaydi — "
            "faqat taqqoslashni. Demak bu dars butunlay tushunish haqida."
        ),
        "stories": ["Two Thermometers"],
        "content": """
<h2>SAT-57: Standard Deviation — Measuring Data Spread</h2>

<p>Bu darsda ajoyib xabar bor: <mark>SAT sizdan standart ogʻishni hisoblashni
hech qachon soʻramaydi</mark>. Formula testda uchramaydi. Soʻraladigani faqat
bitta narsa — <b>qaysi maʼlumotda tarqalish kattaroq</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>standart ogʻish nimani oʻlchashini bir jumlada aytasiz;</li>
    <li>ikki maʼlumot toʻplamini hisoblashsiz taqqoslaysiz;</li>
    <li>markaz va tarqalish bogʻliq emasligini bilasiz;</li>
    <li>gistogrammadan tarqalishni koʻz bilan oʻqiysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">In one sentence</span>
  <span class="pe-chip pe-chip--v">qiymatlar oʻrtachadan</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">oʻrtacha qancha uzoq</span>
</div>

<h3>Nimani oʻlchaydi</h3>

<p>Standart ogʻish — qiymatlarning oʻrtachadan <b>oʻrtacha uzoqligi</b>.
Qiymatlar oʻrtacha atrofida zich toʻplansa u kichik, keng tarqalsa katta
boʻladi. Eng chekka hol: barcha qiymatlar teng boʻlsa, standart ogʻish
aynan <b>nol</b>.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Maʼlumot</th><th>Oʻrtacha</th><th>Tarqalish</th></tr>
  <tr><td>4, 5, 6, 7, 8</td><td>6</td><td class="pm-word__sym">kichik</td></tr>
  <tr><td>1, 3, 6, 9, 11</td><td>6</td><td class="pm-word__sym">katta</td></tr>
  <tr><td>6, 6, 6, 6, 6</td><td>6</td><td class="pm-word__sym">nol</td></tr>
</table></div>

<p>Uchala qatorning oʻrtachasi bir xil — 6. Demak <b>markaz tarqalish haqida
hech narsa aytmaydi</b>, va bu darsdagi asosiy gʻoya.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Taqqoslashda oʻrtachani umuman hisoblamang. Faqat qarang: qaysi qatorda
  sonlar bir-biriga <b>yaqinroq</b>? Oʻsha qatorda standart ogʻish kichikroq.
  SAT'dagi savolning butun mazmuni shu.
</div>

<h3>Ikkita muhim xossa</h3>

<p><b>Barcha qiymatga bir xil son qoʻshsangiz, standart ogʻish
oʻzgarmaydi.</b> 10, 20, 30 va 110, 120, 130 — ikkala qatorda ham sonlar
bir-biridan oʻn birlik uzoqda. Oʻrtacha 20 dan 120 ga koʻchdi, tarqalish
esa oʻsha-oʻsha.</p>

<p><b>Katta sonlar katta tarqalish degani emas.</b> 1000, 1000, 1000
qatorining standart ogʻishi nolga teng, 1, 5, 9 niki esa emas — sonlari
ancha kichik boʻlsa ham.</p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Bu ikki xossa SAT'ning ikki sevimli tuzogʻi. «Ikkinchi toʻplamdagi sonlar
  kattaroq, demak ogʻish ham kattaroq» degan javob deyarli har doim
  notoʻgʻri: <b>ogʻish joylashuvga emas, tarqoqlikka bogʻliq</b>.
</div>

<h3>Gistogrammadan oʻqish</h3>

<p>Gistogramma berilsa, qoida bir qarashda ishlaydi: <b>tor va baland</b>
shakl — kichik ogʻish; <b>keng va past</b> shakl — katta ogʻish. Ikki
gistogramma bir xil kenglikda boʻlsa, chetlarida koʻproq maʼlumot boʻlgani
kattaroq ogʻishga ega.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Taqqoslash savolida <b>chetlarga qarang</b>. Oʻrtadagi ustunlar ogʻishga kam
  hissa qoʻshadi; oʻrtachadan uzoqdagi bir nechta qiymat esa uni sezilarli
  koʻtaradi — chunki uzoqlik ogʻishga kvadratik taʼsir qiladi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>standard deviation</b><span>standart ogʻish</span></li>
  <li><b>which data set has the greater standard deviation</b><span>qaysida ogʻish kattaroq</span></li>
  <li><b>more tightly clustered</b><span>zichroq toʻplangan</span></li>
  <li><b>more spread out</b><span>kengroq tarqalgan</span></li>
  <li><b>the same mean but different spread</b><span>oʻrtachasi bir xil, tarqalishi boshqa</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>Data set A is 4, 5, 6, 7, 8 and data set B is 1, 3, 6, 9, 11. Which has
    the greater standard deviation?</p>
  </div>
  <ol class="ps-ch">
    <li>B, because its values are more spread out from the mean</li>
    <li>A, because it has more values close together</li>
    <li>They are equal, because the means are equal</li>
    <li>It cannot be determined without calculating</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) B</p>
      <p>Ikkalasining oʻrtachasi 6, lekin B ning qiymatlari oʻrtachadan
      ancha uzoq: 5 birlikkacha, A da esa 2 birlikkacha.</p>
      <p>Hisoblash shart emas — koʻz bilan koʻrinadi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">They are equal, because the means are equal</span>
  <span class="ps-trap__why">Markaz va tarqalish — ikki boshqa narsa. Bir xil
  oʻrtachali cheksiz koʻp toʻplam bor, va ularning ogʻishi butunlay har
  xil.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">55 s</span></p>
  <div class="ps-stem__q">
    <p>Data set C is 10, 20, 30 and data set D is 110, 120, 130. Which statement
    is true?</p>
  </div>
  <ol class="ps-ch">
    <li>They have the same standard deviation</li>
    <li>D has a greater standard deviation because its values are larger</li>
    <li>C has a greater standard deviation</li>
    <li>D has a standard deviation ten times greater</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) Bir xil</p>
      <p>D — bu C ning har bir qiymatiga 100 qoʻshilgani. Sonlar oʻrtasidagi
      masofalar oʻzgarmagan.</p>
      <p>Oʻrtacha 20 dan 120 ga koʻchdi; tarqalish esa oʻsha-oʻsha.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">D has a greater standard deviation because its values are larger</span>
  <span class="ps-trap__why">Kattalik va tarqoqlik chalkashtirilgan. Ogʻish
  sonlarning <b>oʻzaro masofasini</b> oʻlchaydi, ularning qanchaligini
  emas.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Standart ogʻish savolida hech qachon hisoblamang:</p>
  <ol>
    <li>Ikki toʻplamdagi sonlar bir-biriga qanchalik yaqin — shunga qarang;</li>
    <li>Bir xil son qoʻshilgan boʻlsa — ogʻish teng;</li>
    <li>Barcha qiymat teng boʻlsa — ogʻish nol.</li>
  </ol>
  <p>«It cannot be determined without calculating» degan variant deyarli har
  doim notoʻgʻri — SAT sizdan aynan hisoblashsiz qaror qilishni kutadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Oʻrtachalari teng → ogʻishlari ham teng</p>
  <p class="pe-good">Markaz tarqalish haqida hech narsa aytmaydi</p>
  <p class="pe-fix__why">6, 6, 6 va 1, 6, 11 — bir xil oʻrtacha, butunlay
  boshqa ogʻish.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Sonlar kattaroq → ogʻish kattaroq</p>
  <p class="pe-good">1000, 1000, 1000 ning ogʻishi nol</p>
  <p class="pe-fix__why">Ogʻish qiymatlarning oʻzaro uzoqligini oʻlchaydi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Standart ogʻish maʼlumot bilan <b>bir xil birlikda</b> boʻladi: maosh
  somda oʻlchansa, ogʻish ham somda. Shuning uchun uni «oʻrtachadan odatiy
  chetlanish» deb oʻqish mumkin — va bu SAT savollarida yetarli.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ogʻish <b>hech qachon manfiy boʻlmaydi</b>. Javob variantlarida manfiy son
  turgan boʻlsa, u darrov oʻchadi — bu bepul tekshiruv.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Which has the greater standard deviation: 5, 5, 5, 5 or 2, 5, 5, 8?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ikkinchisi — birinchisining ogʻishi nol.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Data set E is 3, 4, 5. Set F is 53, 54, 55. Compare their standard
  deviations.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Teng — F ga 50 qoʻshilgan, masofalar
  oʻzgarmagan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A data set has a standard deviation of 0. What does this tell you?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Barcha qiymatlar bir xil.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Two histograms have the same mean. One is tall and narrow, the other short and
  wide. Which has the greater standard deviation?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Keng va past boʻlgani — maʼlumot kengroq
  tarqalgan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Can a standard deviation be negative?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — u masofani oʻlchaydi, masofa esa manfiy
  boʻlmaydi.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>standard deviation</b><span>standart ogʻish</span></li>
  <li><b>spread</b><span>tarqalish</span></li>
  <li><b>clustered</b><span>toʻplangan, zich</span></li>
  <li><b>spread out</b><span>kengroq tarqalgan</span></li>
  <li><b>deviation from the mean</b><span>oʻrtachadan chetlanish</span></li>
  <li><b>histogram</b><span>gistogramma</span></li>
  <li><b>identical values</b><span>bir xil qiymatlar</span></li>
  <li><b>greater / smaller</b><span>kattaroq / kichikroq</span></li>
  <li><b>tightly clustered</b><span>zich toʻplangan</span></li>
  <li><b>cannot be determined</b><span>aniqlab boʻlmaydi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>SAT ogʻishni <b>hisoblatmaydi</b> — faqat taqqoslatadi.</li>
    <li>Har bir qiymatga bir xil son qoʻshilsa <b>ogʻish oʻzgarmaydi</b>.</li>
    <li>Barcha qiymat teng boʻlsa ogʻish <b>nol</b>; u manfiy boʻlmaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-58 — probability
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-58: Probability — Simple and Independent Events",
        "category": "math",
        "order": 58,
        "summary": (
            "Ehtimollik — qulay hollarni jamiga boʻlish. Ikki bogʻliqsiz hodisa "
            "birga sodir boʻlishi uchun ehtimollar koʻpaytiriladi."
        ),
        "stories": ["Twenty-Six Times"],
        "content": """
<h2>SAT-58: Probability — Simple and Independent Events</h2>

<p>Ehtimollik SAT'da murakkab emas: <mark>qulay hollar soni jami hollar
soniga boʻlinadi</mark>. Qiyinligi faqat ikkita joyda — «yoki» va «va»
soʻzlarini ajratishda, hamda jamining nima ekanini toʻgʻri sanashda.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>oddiy ehtimollikni kasr yoki foizda yozasiz;</li>
    <li>«sodir boʻlmaslik» ehtimolini bir qadamda topasiz;</li>
    <li>bogʻliqsiz hodisalar uchun koʻpaytirasiz;</li>
    <li>qaytarish bor yoki yoʻqligini farqlaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Probability</span>
  <span class="pe-chip pe-chip--v">qulay hollar</span>
  <span class="pe-op">÷</span>
  <span class="pe-chip pe-chip--s">jami hollar</span>
</div>

<h3>Oddiy ehtimollik</h3>

<p>Xaltada 5 qizil, 3 koʻk va 2 yashil sharcha bor — jami 10 ta. Bittasi
tasodifiy olinadi.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Savol</th><th>Hisob</th><th>Javob</th></tr>
  <tr><td>qizil chiqishi</td><td>5 ÷ 10</td><td class="pm-word__sym">1/2</td></tr>
  <tr><td>koʻk chiqishi</td><td>3 ÷ 10</td><td class="pm-word__sym">3/10</td></tr>
  <tr><td>qizil <b>chiqmasligi</b></td><td>1 − 1/2</td><td class="pm-word__sym">1/2</td></tr>
  <tr><td>qizil <b>yoki</b> koʻk</td><td>(5 + 3) ÷ 10</td><td class="pm-word__sym">4/5</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ehtimollik har doim <b>0 va 1 orasida</b>. Javobingiz birdan katta chiqsa,
  albatta xato bor — koʻpincha qoʻshish oʻrniga koʻpaytirilgan yoki maxrajga
  notoʻgʻri son qoʻyilgan.
</div>

<h3>«Yoki» qoʻshadi, «va» koʻpaytiradi</h3>

<p>Bitta tanlovda ikki natijadan biri boʻlishi kerak boʻlsa — <b>qoʻshing</b>
(yuqoridagi oxirgi qator). Ikki <u>alohida</u> tanlov birga sodir boʻlishi
kerak boʻlsa — <b>koʻpaytiring</b>.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Tanga ikki marta tashlanadi</span>
    <span class="pm-solve__why">Ikki alohida tashlash — bogʻliqsiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Har birida gerb ehtimoli 1/2</span>
    <span class="pm-solve__why">Birinchi tashlash ikkinchisiga taʼsir qilmaydi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Ikkalasi ham gerb: 1/2 × 1/2 = 1/4</span>
    <span class="pm-solve__why">Toʻrt teng holdan bittasi</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Tanga «xotirasi yoʻq». Ketma-ket besh marta gerb tushgan boʻlsa ham, oltinchi
  tashlashda gerb ehtimoli hali ham 1/2. SAT bu savolni ataylab beradi va
  «endi raqam tushishi kerak» degan variantni qoʻyadi.
</div>

<h3>Qaytarishsiz olish</h3>

<p>Agar olingan narsa qaytarilmasa, ikkinchi qadamda <b>ikkala son ham</b>
oʻzgaradi. Xaltada 5 qizil va 5 koʻk boʻlsin, ikkita ketma-ket olamiz:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Birinchisi qizil: 5 ÷ 10 = 1/2</span>
    <span class="pm-solve__why">Jami 10 ta</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Ikkinchisi ham qizil: 4 ÷ 9</span>
    <span class="pm-solve__why">Bitta qizil ketdi, jami ham bittaga kamaydi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">1/2 × 4/9 = 2/9</span>
    <span class="pm-solve__why">Qaytarish boʻlganda 1/2 × 1/2 = 1/4 boʻlardi</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Savolda «<b>replaced</b>» soʻzini qidiring. «The marble is replaced» boʻlsa
  maxraj oʻzgarmaydi; «without replacement» yoki hech narsa aytilmagan boʻlsa
  koʻpincha qaytarilmaydi — jumlani diqqat bilan oʻqing.
</div>

<h3>«Kamida bitta» — teskarisidan boring</h3>

<p>«At least one» degan ibora koʻrinsa, toʻgʻridan-toʻgʻri sanash uzoq yoʻl.
Qisqasi — <b>teskari hodisani</b> hisoblash: «kamida bitta» ning teskarisi
«bittasi ham emas».</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Tanga uch marta tashlanadi</span>
    <span class="pm-solve__why">Kamida bitta gerb ehtimoli soʻralgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Bittasi ham gerb emas: 1/2 × 1/2 × 1/2 = 1/8</span>
    <span class="pm-solve__why">Uchala tashlashda ham raqam</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">1 − 1/8 = 7/8</span>
    <span class="pm-solve__why">Sakkiz holdan yettitasida kamida bitta gerb bor</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Toʻgʻridan-toʻgʻri sanasangiz uchta holni qoʻshishingiz kerak: aynan bitta,
  aynan ikkita va uchtasi ham. Teskari yoʻl esa bitta koʻpaytma. SAT «at least
  one» ni aynan shu sababdan tez-tez beradi.
</div>

<p>Ehtimollikni <b>foizda</b> ham soʻrashadi: 1/4 — bu 25 foiz, 2/9 esa
taxminan 22 foiz. Javob variantlari qaysi koʻrinishda berilganiga qarang va
oʻsha koʻrinishga oʻting; kasrni oʻnli kasrga faqat oxirida aylantiring.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>at random</b><span>tasodifiy</span></li>
  <li><b>what is the probability that</b><span>… ehtimoli qanday</span></li>
  <li><b>with replacement</b><span>qaytarib qoʻyib</span></li>
  <li><b>without replacement</b><span>qaytarmasdan</span></li>
  <li><b>independent events</b><span>bogʻliqsiz hodisalar</span></li>
  <li><b>at least one</b><span>kamida bitta</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>A bag contains 5 red, 3 blue and 2 green marbles. One marble is chosen at
    random. What is the probability that it is <i>not</i> red?</p>
  </div>
  <ol class="ps-ch">
    <li>1/2</li>
    <li>5/10</li>
    <li>3/10</li>
    <li>1/5</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 1/2</p>
      <p>Qizil boʻlmaganlar 5 ta (3 koʻk va 2 yashil), jami 10 — demak
      5 ÷ 10.</p>
      <p>Yoki qisqaroq: 1 − 1/2. Bu yerda ikkala javob ham teng chiqdi,
      chunki qizillar aynan yarmi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">3/10</span>
  <span class="ps-trap__why">Faqat koʻklar sanalgan; yashillar ham «qizil
  emas». «Not red» degani <b>qolgan hammasi</b>.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>Two fair six-sided dice are rolled. What is the probability that both show
    a 6?</p>
  </div>
  <ol class="ps-ch">
    <li>1/36</li>
    <li>1/3</li>
    <li>1/6</li>
    <li>1/12</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 1/36</p>
      <p>Hodisalar bogʻliqsiz: 1/6 × 1/6.</p>
      <p>Yoki sanang: 36 ta teng juftlik bor, ulardan faqat bittasi
      ikkita olti.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">1/3</span>
  <span class="ps-trap__why">Ehtimollar <b>qoʻshilgan</b>: 1/6 + 1/6 = 1/3.
  «Va» koʻpaytirishni bildiradi, va koʻpaytma har doim kichikroq
  chiqadi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Ehtimollik savolida uch qadam:</p>
  <ol>
    <li><b>Jamini</b> sanang — savoldagi barcha narsalar;</li>
    <li>Soʻralayotgan hollarni sanang;</li>
    <li>Javobni tekshiring: u 0 va 1 orasidami?</li>
  </ol>
  <p>«Kamida bitta» degan savolda <b>teskarisidan</b> boring: 1 minus
  «bittasi ham emas» ehtimoli — bu deyarli har doim tezroq.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Ikkita olti: 1/6 + 1/6</p>
  <p class="pe-good">1/6 × 1/6 = 1/36</p>
  <p class="pe-fix__why">«Va» — koʻpaytirish; qoʻshish «yoki» uchun.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Qaytarmasdan ikkita qizil: 5/10 × 5/10</p>
  <p class="pe-good">5/10 × 4/9</p>
  <p class="pe-fix__why">Bitta olingandan keyin surat ham, maxraj ham
  kamayadi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ehtimollikni <b>kasr</b> holida qoldiring va faqat oxirida yaxlitlang.
  Oʻrtada oʻnli kasrga oʻtish (0.1667 kabi) xatoni toʻplaydi va SAT javob
  variantlari koʻpincha aynan kasr koʻrinishida beriladi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  A fair die is rolled. What is the probability of getting an even number?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">1/2 — uchta juft son (2, 4, 6) oltitadan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  A bag has 4 white and 6 black balls. What is the probability of drawing
  white?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">2/5 — 4 ÷ 10.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A coin is flipped three times. What is the probability of three heads?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">1/8 — 1/2 uch marta koʻpaytiriladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  A coin has landed heads five times. What is the probability of heads on the
  sixth flip?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">1/2 — tangada xotira yoʻq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A bag has 5 red and 5 blue balls. Two are drawn without replacement. What is
  the probability both are red?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">2/9 — 5/10 × 4/9.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>probability</b><span>ehtimollik</span></li>
  <li><b>at random</b><span>tasodifiy</span></li>
  <li><b>fair die</b><span>toʻgʻri (bir xil ehtimolli) zar</span></li>
  <li><b>outcome</b><span>natija</span></li>
  <li><b>favourable outcomes</b><span>qulay hollar</span></li>
  <li><b>independent</b><span>bogʻliqsiz</span></li>
  <li><b>with / without replacement</b><span>qaytarib / qaytarmasdan</span></li>
  <li><b>at least one</b><span>kamida bitta</span></li>
  <li><b>complement</b><span>teskari hodisa</span></li>
  <li><b>equally likely</b><span>bir xil ehtimolli</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Qulay ÷ jami</b>, va javob 0 bilan 1 orasida.</li>
    <li><b>«Yoki» qoʻshadi, «va» koʻpaytiradi.</b></li>
    <li>Qaytarilmasa, ikkinchi qadamda <b>ikkala son ham</b> kamayadi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-59 — conditional probability
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-59: Conditional Probability from Two-Way Tables",
        "category": "math",
        "order": 59,
        "summary": (
            "«Given that» degan ikki soʻz butun jadvalni emas, faqat bitta "
            "qatorni yoki ustunni maxrajga aylantiradi."
        ),
        "stories": ["The Test Came Back Positive"],
        "content": """
<h2>SAT-59: Conditional Probability from Two-Way Tables</h2>

<p>Bu dars SAT-53 va SAT-58 ni birlashtiradi, va uning butun mazmuni ikki
soʻzda: <mark>«given that» maxrajni oʻzgartiradi</mark>. Surat oʻsha-oʻsha
qoladi, javob esa butunlay boshqa chiqadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>shartli ehtimollikda maxrajni bir zumda topasiz;</li>
    <li>«A given B» va «B given A» ni ajratasiz;</li>
    <li>jadvalning qatorimi yoki ustunimi kerakligini aniqlaysiz;</li>
    <li>butun jadvaldan olinadigan ehtimollikdan farqlaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Given that…</span>
  <span class="pe-chip pe-chip--v">shart</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">maxraj</span>
</div>

<h3>Jadval</h3>

<p>150 kishidan choy yoki qahvani afzal koʻrishi soʻralgan:</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th></th><th>Tea</th><th>Coffee</th><th>Total</th></tr>
  <tr><td>Men</td><td>30</td><td>45</td><td class="pm-word__sym">75</td></tr>
  <tr><td>Women</td><td>50</td><td>25</td><td class="pm-word__sym">75</td></tr>
  <tr><td>Total</td><td class="pm-word__sym">80</td><td class="pm-word__sym">70</td>
      <td class="pm-word__sym">150</td></tr>
</table></div>

<h3>Uchta savol, bitta katak</h3>

<p>Uchala savolda ham surat <b>30</b> — erkak va choy tanlaganlar soni. Farq
faqat maxrajda:</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Savol</th><th>Maxraj</th><th>Javob</th></tr>
  <tr><td>a man, given tea</td><td>choy tanlaganlar, 80</td>
      <td class="pm-word__sym">30 ÷ 80 = 0.375</td></tr>
  <tr><td>tea, given a man</td><td>erkaklar, 75</td>
      <td class="pm-word__sym">30 ÷ 75 = 0.4</td></tr>
  <tr><td>a man and tea</td><td>hammasi, 150</td>
      <td class="pm-word__sym">30 ÷ 150 = 0.2</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  «A given B» va «B given A» <b>teng emas</b>. Yuqorida 0.375 va 0.4 — yaqin,
  lekin boshqa sonlar, va SAT ikkalasini ham javob variantiga qoʻyadi. Qaysi
  biri soʻralganini jumladan oʻqing.
</div>

<h3>Maxrajni topishning bir qadamli usuli</h3>

<p>«Given that» yoki «of those who» iborasidan <b>keyingi</b> guruh — maxraj.
Shu guruhning jadvaldagi yigʻindisini oling, va boshqa hech narsaga
qaramang.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">«…given that the person is a woman»</span>
    <span class="pm-solve__why">Shart — ayol; maxraj 75</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">«…prefers coffee»</span>
    <span class="pm-solve__why">Surat — ayol va qahva: 25</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">25 ÷ 75 = 1/3</span>
    <span class="pm-solve__why">Butun jadvaldan olsak 25 ÷ 150 boʻlardi — notoʻgʻri</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Shartni <b>jadvalning bir qismini yopib qoʻyish</b> deb tasavvur qiling.
  «Given a woman» degani — erkaklar qatorini qogʻoz bilan yoping. Qolgan
  qatorda 50 ta choy va 25 ta qahva bor, jami 75. Boshqa hech narsa mavjud
  emas.
</div>

<h3>Foizda soʻralganda</h3>

<p>SAT bir xil savolni ehtimollik oʻrniga <b>foizda</b> ham soʻraydi. Amal
oʻzgarmaydi — faqat javob 100 ga koʻpaytiriladi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">«What percent of the men prefer tea?»</span>
    <span class="pm-solve__why">Shart erkaklar — maxraj 75</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">30 ÷ 75 = 0.4 → 40 foiz</span>
    <span class="pm-solve__why">«Of the men» iborasi maxrajni belgiladi</span>
  </div>
</div>

<p>Diqqat qiling: «what percent of the men» va «what percent of tea drinkers
are men» — bir xil katakdan chiqadigan ikki boshqa savol. Birinchisi 40 foiz,
ikkinchisi 37.5 foiz. Jumlaning oxirini oʻqish shu yerda ballni hal
qiladi.</p>

<p>Yana bir foydali tekshiruv: bitta shart ostidagi barcha ehtimollar
yigʻindisi <b>birga teng</b> boʻlishi kerak. Erkaklar orasida choy 30/75 va
qahva 45/75 — yigʻindisi 75/75, yaʼni 1. Javobingiz bu tekshiruvdan oʻtmasa,
maxrajni notoʻgʻri olgansiz.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>given that the person is a man</b><span>agar u erkak boʻlsa — maxraj erkaklar</span></li>
  <li><b>of those who prefer tea</b><span>choy tanlaganlar orasida</span></li>
  <li><b>among the women</b><span>ayollar orasida</span></li>
  <li><b>selected at random from all respondents</b><span>hamma javob berganlardan tasodifiy</span></li>
  <li><b>is a woman and prefers coffee</b><span>ayol VA qahva — maxraj hammasi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>Using the table, a person is selected at random from those who prefer tea.
    What is the probability that the person is a man?</p>
  </div>
  <ol class="ps-ch">
    <li>30/80</li>
    <li>30/75</li>
    <li>30/150</li>
    <li>80/150</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 30/80</p>
      <p>«From those who prefer tea» — maxraj choy tanlaganlar, 80.</p>
      <p>Bu 0.375 ga teng.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">30/75</span>
  <span class="ps-trap__why">Bu teskari savolning javobi — «given that the
  person is a man». Shart qaysi guruhni belgilayotganini jumladan
  oʻqing.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">65 s</span></p>
  <div class="ps-stem__q">
    <p>Using the table, a person is selected at random from all 150 respondents.
    What is the probability that the person is a woman who prefers coffee?</p>
  </div>
  <ol class="ps-ch">
    <li>25/150</li>
    <li>25/75</li>
    <li>25/70</li>
    <li>70/150</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 25/150</p>
      <p>Bu yerda shart yoʻq — tanlov butun guruhdan, demak maxraj 150.</p>
      <p>Qisqartirilsa 1/6.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">25/75</span>
  <span class="ps-trap__why">Shart yoʻq joyda shart qoʻllangan. «From all
  respondents» degani maxraj butun jadval yigʻindisi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Har bir shartli savolda ikki qadam:</p>
  <ol>
    <li>Jumlada <b>«given that», «of those», «among»</b> soʻzlarini
        belgilang;</li>
    <li>Ulardan keyingi guruhning yigʻindisini maxrajga yozing;</li>
    <li>Suratga ikkala shart ham bajarilgan katakni qoʻying.</li>
  </ol>
  <p>Bunday soʻz umuman boʻlmasa — maxraj butun jadval jami.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">«Of those who prefer tea, what is the probability of a man» → 30/75</p>
  <p class="pe-good">30/80</p>
  <p class="pe-fix__why">Shart choy tanlaganlarni belgilaydi, erkaklarni
  emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">«A woman who prefers coffee» (shartsiz) → 25/75</p>
  <p class="pe-good">25/150</p>
  <p class="pe-fix__why">Shart yoʻq — maxraj butun guruh.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Va» bilan «given» ni chalkashtirmang. <b>«Ayol va qahva»</b> — ikkala
  shart ham bajarilgan, maxraj hammasi. <b>«Qahva, agar ayol boʻlsa»</b> —
  maxraj faqat ayollar. Ingliz tilida farq bitta soʻzda, matematikada esa ikki
  barobar.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Jadval savolida yigʻindilar berilmagan boʻlsa, <b>ularni oʻzingiz hisoblab
  yozib qoʻying</b>. Bir marta 15 soniya sarflaysiz va keyingi uchta savol
  tayyor boʻladi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Using the table, what is the probability that a randomly chosen person prefers
  tea?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">80/150, yaʼni 8/15.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Given that a person is a man, what is the probability he prefers coffee?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">45/75, yaʼni 3/5.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Of those who prefer coffee, what is the probability the person is a woman?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">25/70, yaʼni 5/14.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  What is the probability that a randomly chosen person is a man who prefers
  tea?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">30/150, yaʼni 1/5.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Given that a person prefers tea, what is the probability the person is a
  woman?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">50/80, yaʼni 5/8.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>conditional probability</b><span>shartli ehtimollik</span></li>
  <li><b>given that</b><span>agar … boʻlsa (shart)</span></li>
  <li><b>of those who</b><span>… qilganlar orasida</span></li>
  <li><b>among</b><span>orasida</span></li>
  <li><b>respondents</b><span>soʻrovda qatnashganlar</span></li>
  <li><b>row / column total</b><span>qator / ustun yigʻindisi</span></li>
  <li><b>selected at random</b><span>tasodifiy tanlangan</span></li>
  <li><b>and</b><span>va — ikkala shart ham</span></li>
  <li><b>prefers</b><span>afzal koʻradi</span></li>
  <li><b>in simplest form</b><span>eng sodda koʻrinishda</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>«Given that» maxrajni belgilaydi</b> — undan keyingi guruh.</li>
    <li><b>«A given B» va «B given A» teng emas.</b></li>
    <li>Shart yoʻq boʻlsa, maxraj <b>butun jadval jami</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-60 — sample surveys
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-60: Sample Surveys and Random Sampling",
        "category": "math",
        "order": 60,
        "summary": (
            "Xulosa faqat tanlanma OLINGAN guruhga tegishli. Tasodifiylik shu "
            "huquqni beradi, katta hajm esa aniqlikni oshiradi."
        ),
        "stories": ["Two Million Wrong Answers"],
        "content": """
<h2>SAT-60: Sample Surveys and Random Sampling</h2>

<p>Bu darsda hisoblash umuman yoʻq. Bitta savol bor, va SAT uni har bir mock
testda beradi: <mark>bu natijani kimga nisbatan aytish mumkin?</mark></p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>xulosa qaysi guruhga tegishli ekanini aytasiz;</li>
    <li>tasodifiy tanlash nima berishini bilasiz;</li>
    <li>hajm va aniqlik bogʻliqligini tushuntirasiz;</li>
    <li>«margin of error» iborasini toʻgʻri oʻqiysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The one question</span>
  <span class="pe-chip pe-chip--v">tanlanma qayerdan olindi?</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">xulosa oʻsha guruhga tegishli</span>
</div>

<h3>Tasodifiylik nima beradi</h3>

<p>Tanlanma tasodifiy olinsa, u olingan guruhni <b>vakillik qiladi</b> — yaʼni
undagi nisbatlar butun guruhdagi nisbatlarga yaqin boʻladi. Tanlanma
tasodifiy boʻlmasa, natija faqat oʻsha tanlanmaning oʻzini tasvirlaydi va
undan nariga oʻtmaydi.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Tanlanma</th><th>Xulosa kimga tegishli</th></tr>
  <tr><td>maktabning barcha oʻquvchilaridan tasodifiy 100 ta</td>
      <td class="pm-word__sym">butun maktabga</td></tr>
  <tr><td>faqat 11-sinflardan tasodifiy 100 ta</td>
      <td class="pm-word__sym">faqat 11-sinflarga</td></tr>
  <tr><td>kutubxonada oʻtirganlardan 100 ta</td>
      <td class="pm-word__sym">deyarli hech kimga</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Uchinchi qator eng muhimi. Kutubxonadagilar <b>oʻzlarini tanlagan</b>, va
  ular oʻqishni yaxshi koʻradiganlar boʻlishi ehtimoli katta. Bunday
  tanlanmadan chiqqan natija butun maktab haqida hech narsa aytmaydi —
  qancha koʻp odam soʻralsa ham.
</div>

<h3>Hajm nima beradi</h3>

<p>Tanlanma <b>kattaroq</b> boʻlsa, natija haqiqiy qiymatga yaqinroq turadi va
<b>margin of error</b> — xatolik chegarasi — kichrayadi. Lekin hajm
tanlanmaning yomon olinganini <u>tuzatmaydi</u>: yomon tanlangan katta
tanlanma ham xato javob beradi.</p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Bu SAT'ning eng sevimli tuzogʻi: «tanlanma katta edi, demak natijaga
  ishonish mumkin». Yoʻq — avval <b>qanday</b> tanlangani, keyin
  <b>qancha</b> ekani muhim.
</div>

<h3>Xatolik chegarasini oʻqish</h3>

<p>«52 percent, with a margin of error of 3 percent» degan jumla bitta son
emas, <b>oraliq</b> beradi: haqiqiy qiymat taxminan 49 va 55 foiz orasida.
Ikki natijaning oraliqlari kesishsa, ular orasidagi farq ishonchli
hisoblanmaydi.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Javob variantlarida <b>«all students in the country»</b> yoki
  <b>«all people»</b> kabi juda keng guruh koʻrsatilgan boʻlsa, u deyarli har
  doim notoʻgʻri. Toʻgʻri javob tanlanma olingan guruhning aynan oʻzini
  nomlaydi.
</div>

<h3>Ikki xil tasodifiylik</h3>

<p>SAT ikki narsani ajratadi, va ularning maʼnosi butunlay boshqa:</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Nima</th><th>Nima beradi</th></tr>
  <tr><td>tasodifiy <b>tanlash</b></td>
      <td class="pm-word__sym">natijani guruhga umumlashtirish huquqi</td></tr>
  <tr><td>tasodifiy <b>taqsimlash</b></td>
      <td class="pm-word__sym">sabab haqida xulosa chiqarish huquqi</td></tr>
</table></div>

<p>Soʻrovnomada faqat birinchisi bor. Shuning uchun tanlanma soʻrovi
«kimda nima bor» degan savolga javob beradi, «nima nimani keltirib
chiqaradi» degan savolga esa yoʻq.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>a random sample of</b><span>… dan tasodifiy tanlanma</span></li>
  <li><b>which conclusion is most appropriate</b><span>qaysi xulosa eng oʻrinli</span></li>
  <li><b>the population</b><span>bosh toʻplam — tanlanma olingan guruh</span></li>
  <li><b>margin of error</b><span>xatolik chegarasi</span></li>
  <li><b>generalize to</b><span>… ga umumlashtirmoq</span></li>
  <li><b>volunteers</b><span>ixtiyoriy qatnashganlar — tasodifiy emas</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>A random sample of 200 students was selected from the 1,400 students at
    one school. Of those sampled, 62% said they walk to school. Which conclusion
    is most appropriate?</p>
  </div>
  <ol class="ps-ch">
    <li>About 62% of the students at this school walk to school</li>
    <li>About 62% of students in the country walk to school</li>
    <li>Exactly 62% of the students at this school walk to school</li>
    <li>No conclusion can be drawn from a sample</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A</p>
      <p>Tanlanma <b>shu maktabdan</b> tasodifiy olingan, demak xulosa shu
      maktabga tegishli — va u «taxminan».</p>
      <p><b>Exactly</b> — tanlanma hech qachon aniq songa kafolat
      bermaydi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">About 62% of students in the country</span>
  <span class="ps-trap__why">Guruh kengaytirilgan. Tanlanma bitta maktabdan
  olingan, shuning uchun xulosa ham shu maktab bilan chegaralanadi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">55 s</span></p>
  <div class="ps-stem__q">
    <p>A researcher surveys 500 people who volunteered by replying to an online
    advertisement. Which statement is true?</p>
  </div>
  <ol class="ps-ch">
    <li>The sample is not random, so the results may not represent any wider group</li>
    <li>The sample is large, so the results are reliable</li>
    <li>The results apply to everyone online</li>
    <li>The margin of error is zero</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A</p>
      <p>Odamlar oʻzlarini tanlagan — bu tasodifiy tanlanma emas.</p>
      <p>Besh yuz kishi koʻp koʻrinadi, lekin hajm tanlash usulidagi
      kamchilikni tuzatmaydi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">The sample is large, so the results are reliable</span>
  <span class="ps-trap__why">Hajm ishonchlilikni <b>tasodifiy tanlanmada</b>
  oshiradi. Yomon tanlangan tanlanmada u faqat notoʻgʻri javobni aniqroq
  qiladi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Har bir xulosa savolida ikki narsani tekshiring:</p>
  <ol>
    <li>Tanlanma <b>tasodifiymi</b>? Boʻlmasa — hech qanday keng xulosa
        yoʻq;</li>
    <li>Javobdagi guruh tanlanma olingan guruh bilan <b>aynan</b> bir
        xilmi?</li>
  </ol>
  <p>«Exactly», «all», «proves», «causes» soʻzli variantlar deyarli har doim
  oʻchadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Bir maktabdan tasodifiy tanlanma → butun mamlakat haqida xulosa</p>
  <p class="pe-good">Faqat shu maktab haqida</p>
  <p class="pe-fix__why">Xulosa tanlanma olingan guruhdan nariga
  oʻtmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Tanlanma katta → natija ishonchli</p>
  <p class="pe-good">Avval tasodifiy boʻlishi kerak</p>
  <p class="pe-fix__why">Hajm aniqlikni oshiradi, ogʻishni tuzatmaydi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Tanlanma soʻrovi <b>sababni</b> ham koʻrsata olmaydi (SAT-54). U faqat
  guruhda nima borligini tasvirlaydi. Sabab uchun tajriba va tasodifiy
  taqsimlash kerak — bu SAT-62 ning mavzusi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Margin of error» kichrayishi uchun tanlanma hajmi <b>sezilarli</b>
  oshishi kerak — ikki barobar emas, koʻp barobar. SAT bu tafsilotni
  soʻramaydi, lekin «kattaroq tanlanma → kichikroq xatolik» yoʻnalishini
  biladi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  A random sample of 300 residents of one city is surveyed. To whom can the
  results be generalized?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Faqat oʻsha shahar aholisiga.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  A survey is taken only of people leaving a sports stadium. What is the
  problem?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Tanlanma tasodifiy emas — sport bilan
  qiziqadiganlar ortiqcha vakillik qiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A poll reports 48% with a margin of error of 4%. What is the plausible
  range?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">44% dan 52% gacha.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Two candidates poll at 47% and 50%, each with a margin of error of 4%. Can we
  say who leads?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — oraliqlar kesishadi (43–51 va 46–54).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Does increasing a non-random sample from 100 to 10,000 fix its problem?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — hajm ogʻishni tuzatmaydi.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>sample</b><span>tanlanma</span></li>
  <li><b>population</b><span>bosh toʻplam</span></li>
  <li><b>random sample</b><span>tasodifiy tanlanma</span></li>
  <li><b>representative</b><span>vakillik qiluvchi</span></li>
  <li><b>generalize to</b><span>… ga umumlashtirmoq</span></li>
  <li><b>margin of error</b><span>xatolik chegarasi</span></li>
  <li><b>plausible range</b><span>ehtimoliy oraliq</span></li>
  <li><b>volunteers</b><span>ixtiyoriy qatnashganlar</span></li>
  <li><b>biased</b><span>ogʻishgan, xolis emas</span></li>
  <li><b>most appropriate</b><span>eng oʻrinli</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Xulosa <b>tanlanma olingan guruhga</b> tegishli, undan nariga
        emas.</li>
    <li><b>Avval tasodifiylik</b>, keyin hajm — hajm ogʻishni
        tuzatmaydi.</li>
    <li>«Margin of error» bitta son emas, <b>oraliq</b> beradi.</li>
  </ul>
</div>
""",
    },
]
