# -*- coding: utf-8 -*-
"""Prime SAT Math — lessons 96–100. THE LAST BATCH. Kurs shu yerda tugaydi.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_SAT.md
Lesson list: tutorial/management/commands/toc_prime_sat_math.txt

⚠️ SARLAVHALAR BAZADAN OLINGAN, aynan.

⚠️ SAT-100 — KURSNING YAKUNI, oddiy dars emas. Unda:
     • 30 soniyalik yakuniy nazorat (toʻrtta savol);
     • BUTUN KURSNING XARITASI — beshta blok, har biri nima bergani;
     • yodlanadigan uchta formula va varaqda bor narsalar roʻyxati;
     • oxirgi soʻz.
   Kurs 100 ta darsdan iborat va bu oxirgisi — u shunday tugashi kerak.

⚠️ TEST HAQIDAGI FAKTLAR (STYLE_GUIDE §0.2). Formula varagʻida BOR:
   aylana yuzasi va uzunligi, toʻgʻri toʻrtburchak va uchburchak yuzasi,
   Pifagor teoremasi, ikkita maxsus uchburchak, beshta hajm formulasi
   (parallelepiped, silindr, shar, konus, piramida), 360 daraja / 2π
   radian, uchburchak burchaklari yigʻindisi 180.
   VARAQDA YOʻQ: qiyalik, kvadrat tenglama formulasi, aylana tenglamasi,
   SOH-CAH-TOA, oʻrtacha, foiz oʻzgarishi, progressiyalar.
   ⛔ Ball, narx, sana, markaz nomi OʻYLAB TOPILMAYDI.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_sat_96_100.py \\
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
    # SAT-96 — domain and range by testing the edges
    # ══════════════════════════════════════════════════════════════════
    {
        "title": 'SAT-96: The "Testing the Boundaries" Tactic (Domain and Range)',
        "category": "math",
        "order": 96,
        "summary": (
            "Funksiya nimani qabul qiladi va nimani qaytaradi — javob deyarli "
            "har doim chekkalarda yotadi."
        ),
        "stories":  ["The Window Between Too Little and Too Much"],
        "content": """
<h2>SAT-96: The "Testing the Boundaries" Tactic (Domain and Range)</h2>

<p>SAT-93 da chekka qiymatlar daʼvoni sinash uchun kerak edi. Bu darsda
ular boshqa ish qiladi: <mark>funksiyaning chegarasini topadi</mark>.
Ikkala savolda ham qoida bir xil — <b>oʻrtaga qarama, chetiga qara</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>domain va range ni ajratasiz;</li>
    <li>kiritishni taqiqlaydigan uchta narsani darrov topasiz;</li>
    <li>parabolaning chegarasini uchidan oʻqiysiz;</li>
    <li>hayotiy masalada «bu son mumkin emas» deya olasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki soʻz</span>
  <span class="pe-chip pe-chip--v">domain</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">nima kiritish mumkin</span>
</div>

<p><b>Range</b> esa aksi: nima chiqishi mumkin. Ingliz tilida ular
koʻpincha «the set of all possible values of x» va «… of y» deb
yoziladi.</p>

<h3>Kiritishni taqiqlaydigan uchta narsa</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Faqat shu uchtasi</span>
  <ol>
    <li><b>Nolga boʻlish.</b> Maxrajni nolga aylantiradigan son
        domainda yoʻq.</li>
    <li><b>Manfiy sondan kvadrat ildiz.</b> Ildiz ostidagi ifoda
        manfiy boʻlmasligi kerak.</li>
    <li><b>Hayotiy maʼno.</b> Odamlar soni manfiy boʻlmaydi, vaqt
        orqaga oqmaydi, kitoblar kasr boʻlmaydi.</li>
  </ol>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">1 ÷ (<i>x</i> − 3) berilgan</span>
    <span class="pm-solve__why">Domain soʻralyapti</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Maxraj qachon nol?</span>
    <span class="pm-solve__why"><i>x</i> − 3 = 0 → <i>x</i> = 3</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3 dan boshqa hamma son</span>
    <span class="pm-solve__why">Faqat bitta son taqiqlangan</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Domain savolida <b>butun ifodaga qaramang</b> — faqat maxrajga va
  ildiz ostiga qarang. Qolgan hamma narsa har qanday sonni qabul
  qiladi.
</div>

<h3>Range — chegara uchda turadi</h3>

<p>Parabola uchidan pastga tushmaydi (agar u yuqoriga qaragan boʻlsa).
Demak <b>range uchning y koordinatasidan boshlanadi</b> — bu SAT-84
dagi bilim, faqat boshqa savol shaklida.</p>

<div class="pm-check">
  <p class="pm-check__t">Ikkita misol</p>
  <p><i>y</i> = <i>x</i>² + 4 — eng past nuqta (0, 4), demak
  <b>y ≥ 4</b>.</p>
  <p><i>y</i> = <i>x</i>² − 4 — eng past nuqta (0, −4), demak
  <b>y ≥ −4</b>.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Parabola <b>pastga</b> qaragan boʻlsa (bosh koeffitsiyent manfiy),
  chegara yuqoridan boʻladi: y ≤ uchning qiymati. Ishoraga
  qarang.
</div>

<h3>Hayotiy domain</h3>

<p>SAT'ning eng koʻp uchraydigan domain savoli formulasiz keladi:
«Which value of <i>n</i> would not make sense in this context?»
Javob har doim uchtasining biri — manfiy son, kasr son yoki
haddan tashqari katta son.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu savolda matematika umuman kerak emas — faqat <b>oʻqish</b>.
  Chiptalar soni, odamlar soni, avtobuslar soni butun va manfiy
  boʻlmagan son boʻlishi kerak. Javobda −2 yoki 3.5 koʻrsangiz,
  hisoblamasdan tanlang.
</div>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">35 s</span></p>
  <div class="ps-stem__q">
    <p>Which value of <i>x</i> is NOT in the domain of the function
    <i>f</i>(<i>x</i>) = 1 ÷ (<i>x</i> − 3)?</p>
  </div>
  <ol class="ps-ch">
    <li>3</li>
    <li>0</li>
    <li>−3</li>
    <li>1</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 3</p>
      <p>x = 3 da maxraj nolga aylanadi.</p>
      <p>Qolgan uchtasi mutlaqo mumkin: 0 da javob −1/3, −3 da −1/6,
      1 da −1/2.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">−3</span>
  <span class="ps-trap__why">Ifodada 3 turgani uchun uning manfiysi
  tanlanadi. Lekin taqiqlaydigan narsa <b>maxrajni nolga
  aylantirish</b>, va buni faqat +3 qiladi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>What is the range of the function
    <i>g</i>(<i>x</i>) = <i>x</i>² − 4?</p>
  </div>
  <ol class="ps-ch">
    <li><i>y</i> ≥ −4</li>
    <li><i>y</i> ≥ 0</li>
    <li><i>y</i> ≥ 4</li>
    <li>all real numbers</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) y ≥ −4</p>
      <p>x² eng kichik qiymati 0 (x = 0 da), demak butun ifoda
      eng kam −4 boʻladi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">all real numbers</span>
  <span class="ps-trap__why">Bu <b>domain</b> ning javobi — x har qanday
  boʻlishi mumkin. Savol esa chiqadigan qiymatlarni soʻragan. Ikki
  soʻzni chalkashtirish bu mavzudagi asosiy xato.</span>
</div>

<h3>Qachon bu tactic kerak emas</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Uchta «yoʻq»</span>
  <ol>
    <li><b>Maxraj ham, ildiz ham yoʻq</b> boʻlsa — domain barcha
        haqiqiy sonlar, tekshiradigan narsa yoʻq.</li>
    <li><b>Chiziqli funksiyada</b> — range ham barcha haqiqiy
        sonlar.</li>
    <li><b>Grafik berilgan</b> boʻlsa — chegarani oʻqing, hisoblamang
        (SAT-83).</li>
  </ol>
</div>

<h3>Exam English</h3>

<ul class="ps-phrase">
  <li><b>the domain of the function</b><span>funksiyaning aniqlanish sohasi</span></li>
  <li><b>the range</b><span>qiymatlar sohasi</span></li>
  <li><b>is NOT in the domain</b><span>domainga kirmaydi</span></li>
  <li><b>would not make sense in this context</b><span>bu vaziyatda maʼnosiz</span></li>
  <li><b>all real numbers</b><span>barcha haqiqiy sonlar</span></li>
</ul>

<div class="pe-fix">
  <p class="pe-bad">Range soʻralganda «all real numbers»</p>
  <p class="pe-good">Uchdan boshlab: y ≥ −4</p>
  <p class="pe-fix__why">Domain — kirish, range — chiqish.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">1 ÷ (x − 3) da x = −3 taqiqlangan</p>
  <p class="pe-good">x = 3 taqiqlangan</p>
  <p class="pe-fix__why">Maxrajni nolga aylantiradigan son
  qidiriladi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikki soʻzni bir marta va butunlay ajratib oling: <b>domain — eshik,
  range — natija</b>. Eshikdan kim kira oladi, va ichkaridan nima
  chiqadi. SAT bu ikkalasini bir savolda ataylab yonma-yon
  qoʻyadi.
</div>

<h3>Chegarani sinash — tengsizlik bilan berilganda</h3>

<p>Domain baʼzan tayyor tengsizlik koʻrinishida keladi: «for
<i>x</i> ≥ 2». Bunday savolda <b>chegaraning oʻzini</b> va undan
<b>bir oz naridagi</b> qiymatni sinang — javob deyarli har doim
shu ikkisida ajraladi.</p>

<table class="pe-table">
  <tr><th>Ifoda</th><th>Taqiq</th><th>Domain</th></tr>
  <tr><td>1 ÷ <i>x</i></td><td>nolga boʻlish</td>
      <td>0 dan boshqa hamma son</td></tr>
  <tr><td>1 ÷ (<i>x</i> − 3)</td><td>nolga boʻlish</td>
      <td>3 dan boshqa hamma son</td></tr>
  <tr><td>√<i>x</i></td><td>manfiy ildiz</td><td><i>x</i> ≥ 0</td></tr>
  <tr><td>√(<i>x</i> − 2)</td><td>manfiy ildiz</td><td><i>x</i> ≥ 2</td></tr>
  <tr><td>3<i>x</i> + 1</td><td>yoʻq</td><td>barcha haqiqiy sonlar</td></tr>
</table>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Oxirgi qatorga eʼtibor bering: koʻpchilik funksiyada
  <b>hech qanday taqiq yoʻq</b>. Domain savoli berilgan ekan,
  demak ifodada maxraj yoki ildiz bor — birinchi navbatda oʻsha
  yerga qarang, chunki savol boshqa joyda boʻlishi mumkin emas.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  What is the domain of 1 ÷ (<i>x</i> + 5)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">−5 dan boshqa hamma son.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  What is the range of <i>y</i> = <i>x</i>² + 7?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">y ≥ 7.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A shop sells <i>n</i> tickets. Which value of <i>n</i> makes no
  sense: 0, 4, 12 or 3.5?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">3.5 — chipta kasr boʻlmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  What is the domain of √(<i>x</i> − 2)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">x ≥ 2 — ildiz ostidagi ifoda manfiy
  boʻlmasligi kerak.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  What is the range of <i>y</i> = 3<i>x</i> + 1?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Barcha haqiqiy sonlar — chiziqli funksiya
  hamma qiymatga yetadi.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>domain</b><span>aniqlanish sohasi (kirish)</span></li>
  <li><b>range</b><span>qiymatlar sohasi (chiqish)</span></li>
  <li><b>denominator</b><span>maxraj</span></li>
  <li><b>undefined</b><span>aniqlanmagan</span></li>
  <li><b>square root</b><span>kvadrat ildiz</span></li>
  <li><b>in this context</b><span>bu vaziyatda</span></li>
  <li><b>make sense</b><span>maʼnoga ega boʻlmoq</span></li>
  <li><b>all real numbers</b><span>barcha haqiqiy sonlar</span></li>
  <li><b>vertex</b><span>uch (chegara shu yerda)</span></li>
  <li><b>boundary</b><span>chegara</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Domain — eshik, range — natija.</b></li>
    <li>Faqat uch narsa taqiqlaydi: nolga boʻlish, manfiy ildiz,
        hayotiy maʼno.</li>
    <li>Parabolaning range'i <b>uchidan</b> boshlanadi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-97 — reading a table
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-97: Data Table Extraction",
        "category": "math",
        "order": 97,
        "summary": (
            "Jadval savolining butun qiyinligi bitta joyda: qaysi jamini "
            "maxraj qilib olish."
        ),
        "stories":  ["Both Numbers Were True"],
        "content": """
<h2>SAT-97: Data Table Extraction</h2>

<p>Jadvalli savollarda matematika deyarli yoʻq — bitta boʻlish, xolos.
<mark>Xato esa har doim bitta joyda</mark>: oʻquvchi notoʻgʻri
jamini maxraj qilib oladi. Bu dars aynan shu haqda.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>jadvalni savoldan <b>oldin</b> oʻqiysiz;</li>
    <li>qator jami, ustun jami va umumiy jamini ajratasiz;</li>
    <li>«of the students who…» iborasini maxrajga aylantirasiz;</li>
    <li>birlik tuzogʻini (mingliklar) sezasiz.</li>
  </ul>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">The move — toʻrt qarash</span>
  <ol>
    <li><b>Qatorlar</b> nimani bildiradi?</li>
    <li><b>Ustunlar</b> nimani bildiradi?</li>
    <li><b>Birlik</b> nima — dona, foiz, mingta?</li>
    <li>Savol qaysi <b>katak</b>ni va qaysi <b>jami</b>ni soʻrayapti?</li>
  </ol>
</div>

<h3>Bitta jadval, uchta boshqa savol</h3>

<table class="pe-table">
  <tr><th></th><th>Korean</th><th>Russian</th><th>Total</th></tr>
  <tr><td><b>Grade 9</b></td><td>18</td><td>22</td><td>40</td></tr>
  <tr><td><b>Grade 10</b></td><td>12</td><td>28</td><td>40</td></tr>
  <tr><td><b>Total</b></td><td>30</td><td>50</td><td>80</td></tr>
</table>

<p>Bu 80 oʻquvchi tanlagan ikkita til. Endi diqqat qiling — quyidagi
uchta savolning <b>surati bir xil</b> boʻlishi mumkin, maxraji esa
har xil.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">"What fraction of all students chose Korean?"</span>
    <span class="pm-solve__why">30 ÷ 80 = 3/8 — umumiy jami</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">"Of those who chose Korean, what fraction are in Grade 9?"</span>
    <span class="pm-solve__why">18 ÷ 30 = 3/5 — ustun jami</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">"What fraction of Grade 9 chose Korean?"</span>
    <span class="pm-solve__why">18 ÷ 40 = 9/20 — qator jami</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling — bu darsning yuragi</span>
  Ikkinchi va uchinchi savol bir xil koʻrinadi va ikkalasida ham surat
  <b>18</b>. Lekin javoblar butunlay boshqa: 3/5 va 9/20. Farqni
  faqat bitta ibora yaratadi — <b>«of those who…»</b>. U maxrajni
  belgilaydi.
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Savolni oʻqiyotganda <b>«of» soʻzidan keyingi guruhni</b> ajratib
  qoʻying. Oʻsha guruh — maxraj. «Of the students who chose Korean» →
  maxraj 30. «Of the Grade 9 students» → maxraj 40. Bitta ibora, bitta
  son.
</div>

<h3>Foiz soʻralganda</h3>

<p>Kasr topilgach, foizga oʻtish bir qadam: yuzga koʻpaytiring.
28 ÷ 40 = 0.7, demak 70 foiz. Chamalash bilan tekshiring (SAT-87):
28 — 40 ning yarmidan sezilarli koʻp, demak javob 50 dan katta
boʻlishi shart.</p>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">55 s</span></p>
  <div class="ps-stem__q">
    <p>Using the table above: of the students who chose Korean, what
    fraction are in Grade 9?</p>
  </div>
  <ol class="ps-ch">
    <li>3/5</li>
    <li>9/20</li>
    <li>3/8</li>
    <li>9/40</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 3/5</p>
      <p>Koreys tilini tanlaganlar — 30 ta. Ulardan 9-sinfda 18 ta.
      18 ÷ 30 = 3/5.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">9/20</span>
  <span class="ps-trap__why">Bu 18 ÷ 40 — yaʼni maxrajga
  <b>9-sinfning jami</b> olingan. Savol esa koreys tilini
  tanlaganlarni maxraj qilishni soʻragan. Surat toʻgʻri, maxraj
  notoʻgʻri.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>Using the table above: what percent of the Grade 10 students
    chose Russian?</p>
  </div>
  <ol class="ps-ch">
    <li>70%</li>
    <li>56%</li>
    <li>35%</li>
    <li>28%</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 70%</p>
      <p>10-sinfda 40 ta oʻquvchi, ulardan 28 tasi rus tilini tanladi:
      28 ÷ 40 = 0.7.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">56%</span>
  <span class="ps-trap__why">28 ÷ 50 — maxrajga <b>rus tilini
  tanlaganlarning jami</b> olingan. Yana oʻsha xato, boshqa
  yoʻnalishda.</span>
</div>

<h3>Ikkinchi tuzoq: birlik</h3>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Jadval sarlavhasida baʼzan <b>«in thousands»</b> yoki «in millions»
  yozilgan boʻladi. Katakdagi 24 — bu 24 000. Bu yozuv jadvalning
  ustida, kichkina harflarda turadi va oʻquvchilar uni deyarli
  oʻqimaydi. Javob variantlarida ham 24, ham 24 000 boʻlsa —
  demak savol aynan shuni sinayapti.
</div>

<h3>Qachon jadval qiyin emas</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Uchta «yoʻq»</span>
  <ol>
    <li><b>Savol bitta katakni</b> soʻrasa — oʻqing va yozing,
        hisoblash yoʻq.</li>
    <li><b>Jadvalning yarmi keraksiz</b> boʻlsa — hammasini
        oʻqib chiqishga urinmang.</li>
    <li><b>«Of» iborasi yoʻq</b> boʻlsa — maxraj umumiy jami.</li>
  </ol>
</div>

<h3>Exam English</h3>

<ul class="ps-phrase">
  <li><b>of the students who chose X</b><span>X ni tanlaganlar ichida (maxraj!)</span></li>
  <li><b>what fraction of all</b><span>hammasining qanchasi</span></li>
  <li><b>the table above shows</b><span>yuqoridagi jadval koʻrsatadi</span></li>
  <li><b>in thousands</b><span>ming birlikda</span></li>
  <li><b>rounded to the nearest percent</b><span>butun foizgacha yaxlitlangan</span></li>
</ul>

<div class="pe-fix">
  <p class="pe-bad">18 ÷ 40 «of those who chose Korean» uchun</p>
  <p class="pe-good">18 ÷ 30</p>
  <p class="pe-fix__why">«Of» dan keyingi guruh maxrajni belgilaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Jadvaldagi 24 → javob 24</p>
  <p class="pe-good">Sarlavhaga qarang: «in thousands» → 24 000</p>
  <p class="pe-fix__why">Birlik jadvalning ustida yozilgan.</p>
</div>

<h3>Grafikda ham xuddi shu toʻrt qarash</h3>

<p>Jadval oʻrniga tarqoq nuqtalar (scatterplot) yoki ustunli
diagramma berilishi mumkin. Usul oʻzgarmaydi: oʻqlarni oʻqing,
birlikni oʻqing, keyin savol qaysi nuqtani soʻrayotganini
aniqlang.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Grafikning uchta savoli</span>
  <ol>
    <li><b>Oʻqing:</b> «Bu nuqtaning qiymati qancha?» — javob
        oʻqlardan koʻchiriladi, hisoblanmaydi.</li>
    <li><b>Bashorat qiling:</b> «Chiziqqa koʻra, 12 da qancha
        boʻladi?» — moslashtirilgan chiziqni (line of best fit)
        davom ettiring, nuqtalarni emas.</li>
    <li><b>Xulosa tanlang:</b> «Which statement is supported by the
        data?» — bu matematik emas, <b>mantiqiy</b> savol.</li>
  </ol>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Bashorat savolida <b>chiziqqa</b> qarang, eng yaqin nuqtaga emas.
  Moslashtirilgan chiziq aynan shuning uchun chizilgan: alohida
  nuqtalar undan chetga chiqishi mumkin, va SAT javob variantiga
  koʻpincha oʻsha chetdagi nuqtaning qiymatini qoʻyadi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha — «supported by the data»</span>
  Bu ibora bitta narsani soʻraydi: <b>qaysi jumla jadval yoki
  grafikdan bevosita kelib chiqadi?</b> Rost boʻlgan, lekin
  maʼlumotda koʻrinmaydigan jumla — notoʻgʻri javob. Sabab haqidagi
  jumla («chunki oʻquvchilar koreys tilini yaxshi koʻradi») ham
  notoʻgʻri: maʼlumot sonlarni koʻrsatadi, sababni emas.
</div>

<h3>Yetishmayotgan katak</h3>

<p>SAT tez-tez jadvalning bitta katagini boʻsh qoldiradi va uni
jamilardan topishni soʻraydi. Bu bir ayirish, lekin qaysi jamidan
ayirishni tanlash kerak.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">9-sinf jami 40, ulardan rus tilida 22</span>
    <span class="pm-solve__why">Koreys tilidagilar soʻralyapti</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">40 − 22 = 18</span>
    <span class="pm-solve__why"><b>Qator</b> jamidan ayirildi</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Boʻsh katak <b>qator jamidan ham, ustun jamidan ham</b>
  topilishi mumkin — ikkalasi ham bir xil javob berishi kerak.
  Ikkisini ham hisoblang: mos kelmasa, jadvalni notoʻgʻri
  oʻqigansiz. Bu tekshiruv besh soniya oladi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  What fraction of all 80 students chose Russian?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">50 ÷ 80 = 5/8.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Of those who chose Russian, what fraction are in Grade 10?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">28 ÷ 50 = 14/25.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  What percent of Grade 9 chose Korean?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">18 ÷ 40 = 0.45, demak 45 foiz.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  How many students in total chose Korean?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">30 — ustun jami.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Which phrase in a question tells you the denominator?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">«Of the …» — undan keyingi guruh.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>table</b><span>jadval</span></li>
  <li><b>row / column</b><span>qator / ustun</span></li>
  <li><b>total</b><span>jami</span></li>
  <li><b>fraction</b><span>ulush, kasr</span></li>
  <li><b>numerator / denominator</b><span>surat / maxraj</span></li>
  <li><b>of those who</b><span>… qilganlar ichida</span></li>
  <li><b>in thousands</b><span>ming birlikda</span></li>
  <li><b>survey</b><span>soʻrov</span></li>
  <li><b>category</b><span>toifa</span></li>
  <li><b>respondents</b><span>soʻrovda qatnashganlar</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Butun qiyinlik <b>maxrajda</b>.</li>
    <li><b>«Of the …»</b> dan keyingi guruh — maxraj.</li>
    <li>Sarlavhadagi <b>birlikni</b> oʻqing.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-98 — the reference sheet
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-98: The Formula Sheet Hack",
        "category": "math",
        "order": 98,
        "summary": (
            "Formula varagʻi har bir savolda ochiq turadi. Demak asosiy "
            "bilim — unda NIMA YOʻQligi."
        ),
        "stories":  ["The Chart on the Classroom Wall"],
        "content": """
<h2>SAT-98: The Formula Sheet Hack</h2>

<p>Testda formula varagʻi bor va u <b>har bir savolda</b> bir bosishda
ochiladi. Koʻpchilik oʻquvchi undagi formulalarni yodlaydi va
undagilarni <b>emas</b>. <mark>Aynan teskarisi kerak</mark>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>varaqda nima borligini roʻyxat bilan bilasiz;</li>
    <li>varaqda <b>yoʻq</b> formulalarni ajratasiz;</li>
    <li>yodlash shart boʻlgan uchtasini aniqlaysiz;</li>
    <li>varaqni <b>maslahatchi</b> sifatida ishlatasiz.</li>
  </ul>
</div>

<h3>Varaqning ikki ustuni</h3>

<table class="pe-table">
  <tr><th>VARAQDA BOR — yodlamang</th><th>VARAQDA YOʻQ — yodlang</th></tr>
  <tr><td>Aylana yuzasi va uzunligi</td><td>Qiyalik formulasi</td></tr>
  <tr><td>Toʻrtburchak va uchburchak yuzasi</td>
      <td>Kvadrat tenglama formulasi</td></tr>
  <tr><td>Pifagor teoremasi</td><td>Aylana tenglamasi</td></tr>
  <tr><td>Ikkita maxsus uchburchak</td><td>SOH-CAH-TOA</td></tr>
  <tr><td>Beshta hajm formulasi</td><td>Oʻrtacha = yigʻindi ÷ soni</td></tr>
  <tr><td>360 daraja · 2π radian</td><td>Foiz oʻzgarishi</td></tr>
  <tr><td>Uchburchak burchaklari 180</td><td>Progressiyalar</td></tr>
</table>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha — bu jadvalni oʻqishning toʻgʻri yoʻli</span>
  Chap ustunni <b>umuman yodlamang</b>. U bir bosish naridagi joyda
  turibdi va imtihon davomida hech qayerga ketmaydi. Oʻng ustun esa
  sizning xotirangizda boʻlishi shart — chunki unga qaraydigan joy
  yoʻq.
</div>

<h3>Yodlash majburiy boʻlgan uchtasi</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Uchta formula</span>
  <ol>
    <li><b>Qiyalik</b> — ikki nuqtadan: y farqi ÷ x farqi (SAT-12).</li>
    <li><b>SOH-CAH-TOA</b> — sin, cos, tan (SAT-75).</li>
    <li><b>Aylana tenglamasi</b> — markaz va radius (SAT-79).</li>
  </ol>
  <p>Uchalasi ham varaqda yoʻq va uchalasi ham deyarli har testda
  uchraydi. Boshqa hech narsani majburan yodlash shart emas.</p>
</div>

<h3>Varaq — maslahatchi sifatida</h3>

<p>Ikkinchi hack kamdan-kam aytiladi: varaq <b>savol nima haqda
ekanini</b> ham koʻrsatib beradi. Jismning hajmi soʻralgan va qaysi
formula kerakligini bilmayapsizmi — beshta hajm formulasini
koʻring va rasmga mos kelganini oling. Yodlash emas, <b>tanish</b>.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Konus: radius 3, balandlik 4</span>
    <span class="pm-solve__why">Varaqdan: hajm = (1/3)πr²h</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">π × 9 × 4 = 36π</span>
    <span class="pm-solve__why">Bu silindrning hajmi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Uchdan biri: 12π</span>
    <span class="pm-solve__why">Konusda 1/3 bor — varaq buni yozib turibdi</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Konus va piramidada <b>1/3</b> bor, silindr va parallelepipedda
  yoʻq. Varaqdan koʻchirayotganda uchdan birni tushirib qoldirish —
  bu mavzudagi eng koʻp uchraydigan xato.
</div>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">55 s</span></p>
  <div class="ps-stem__q">
    <p>A cone has a radius of 3 and a height of 4. What is its
    volume?</p>
  </div>
  <ol class="ps-ch">
    <li>12π</li>
    <li>36π</li>
    <li>4π</li>
    <li>48π</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 12π</p>
      <p>Varaqdan: konus hajmi = (1/3)πr²h = (1/3)(π)(9)(4) = 12π.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">36π</span>
  <span class="ps-trap__why">Uchdan bir tushirib qoldirilgan — bu
  <b>silindr</b>ning hajmi. Varaq ochiq turgan holda ham xato
  qilinadi, chunki oʻquvchi formulani oxirigacha
  koʻchirmaydi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">30 s</span></p>
  <div class="ps-stem__q">
    <p>Which of the following is NOT provided on the test's reference
    sheet?</p>
  </div>
  <ol class="ps-ch">
    <li>The slope formula</li>
    <li>The area of a circle</li>
    <li>The Pythagorean theorem</li>
    <li>The volume of a sphere</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) The slope formula</p>
      <p>Qolgan uchtasi varaqda bor. Qiyalik esa yoʻq — va u
      Blok A ning eng koʻp ishlatiladigan formulasi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">The volume of a sphere</span>
  <span class="ps-trap__why">U murakkab koʻringani uchun «bu boʻlmasa
  kerak» deb tanlanadi. Aslida shar hajmi varaqda bor —
  murakkabligi bilan emas, roʻyxat bilan hal qilinadi.</span>
</div>

<h3>Qachon varaqqa qaramaslik kerak</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Uchta «yoʻq»</span>
  <ol>
    <li><b>Qiyalik, trigonometriya yoki aylana tenglamasi</b>
        kerak boʻlsa — u yerda yoʻq, vaqt yoʻqotmang.</li>
    <li><b>Formulani bilsangiz</b> — ochish uch soniya oladi,
        va oʻsha uch soniya har savolda takrorlanadi.</li>
    <li><b>Savol formula haqida emas</b> boʻlsa — Blok E dagi
        savollarning koʻpchiligida umuman formula yoʻq.</li>
  </ol>
</div>

<h3>Exam English</h3>

<ul class="ps-phrase">
  <li><b>reference sheet</b><span>formula varagʻi</span></li>
  <li><b>is provided</b><span>berilgan, taqdim etilgan</span></li>
  <li><b>the volume of a cone</b><span>konusning hajmi</span></li>
  <li><b>right circular cylinder</b><span>toʻgʻri doiraviy silindr</span></li>
  <li><b>in terms of π</b><span>π ni saqlagan holda</span></li>
</ul>

<div class="pe-fix">
  <p class="pe-bad">Konus hajmi = πr²h</p>
  <p class="pe-good">(1/3)πr²h</p>
  <p class="pe-fix__why">Konus va piramidada uchdan bir bor.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Varaqdagi formulalarni yodlash</p>
  <p class="pe-good">Varaqda YOʻQlarini yodlash</p>
  <p class="pe-fix__why">Varaq har savolda ochiq turadi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Varaqni imtihondan oldin <b>bir marta toʻliq oʻqib chiqing</b> — besh
  daqiqa. Maqsad yodlash emas: u yerda nimalar borligini bilish. Test
  paytida «bu varaqda bormidi?» degan savol tugʻilmasligi kerak, chunki
  bu savolning oʻzi oʻn soniya yeydi.
</div>

<h3>Beshta hajm formulasi — varaqdagi eng foydali qism</h3>

<table class="pe-table">
  <tr><th>Jism</th><th>Hajm</th><th>Uchdan bir bormi</th></tr>
  <tr><td>Rectangular box</td><td><i>lwh</i></td><td>yoʻq</td></tr>
  <tr><td>Cylinder</td><td>π<i>r</i>²<i>h</i></td><td>yoʻq</td></tr>
  <tr><td>Sphere</td><td>(4/3)π<i>r</i>³</td><td>—</td></tr>
  <tr><td>Cone</td><td>(1/3)π<i>r</i>²<i>h</i></td><td><b>ha</b></td></tr>
  <tr><td>Pyramid</td><td>(1/3)<i>lwh</i></td><td><b>ha</b></td></tr>
</table>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha — jadvaldagi qonuniyat</span>
  Uchinchi ustunga qarang: <b>uchi teppa boʻlgan jismlarda</b> —
  konus va piramidada — uchdan bir bor, tekis usti borlarida yoʻq.
  Buni bir marta tushunib olsangiz, formulani varaqdan koʻchirayotganda
  uchdan birni unutmaysiz: konus silindrning uchdan bir qismini
  egallaydi, xolos.
</div>

<h3>Maxsus uchburchaklar ham varaqda</h3>

<p>SAT-71 va SAT-72 dagi ikkita nisbat — 45-45-90 va 30-60-90 —
chizma bilan birga varaqda turadi. Demak ularni ham yodlash shart
emas; <b>tanish</b> yetadi. Savolda 30 daraja koʻrsangiz, varaqni
oching va nisbatni koʻchiring.</p>

<div class="pm-check">
  <p class="pm-check__t">Nimani tanish kerak</p>
  <p>45-45-90 → 1 : 1 : √2 · 30-60-90 → 1 : √3 : 2. Varaqda ular
  chizma sifatida berilgan, demak qaysi tomon qaysi burchakka
  qarshi ekanini ham koʻrsatib turadi (SAT-72 dagi asosiy
  qiyinchilik).</p>
</div>

<h3>Savolning ikki shakli</h3>

<p>Hajm formulasi ikki yoʻnalishda soʻraladi, va ikkinchisi ancha
koʻp ball yeydi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Toʻgʻri: radius 3, balandlik 4 → hajm?</span>
    <span class="pm-solve__why">(1/3)π(9)(4) = 12π</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Teskari: hajm 12π, radius 3 → balandlik?</span>
    <span class="pm-solve__why">(1/3)π(9)<i>h</i> = 12π</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3<i>h</i> = 12, demak <i>h</i> = 4</span>
    <span class="pm-solve__why">π qisqardi — har doim shunday</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Teskari savolda <b>π ni songa aylantirmang</b>. U ikkala tomonda
  ham turadi va oʻz-oʻzidan qisqaradi (SAT-78 dagi bilan bir xil
  qoida). 12π ni 37.7 ga aylantirish faqat vaqt yoʻqotadi va
  yaxlitlash xatosini kiritadi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  A cone has radius 6 and height 5. Find its volume.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(1/3)π(36)(5) = 60π.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  A sphere has radius 3. Find its volume.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(4/3)π(27) = 36π.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Is the quadratic formula on the reference sheet?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  A cylinder has radius 2 and height 7. Find its volume.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">π(4)(7) = 28π — bu yerda uchdan bir
  yoʻq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Name the three formulas you must memorise.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Qiyalik, SOH-CAH-TOA, aylana
  tenglamasi.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>reference sheet</b><span>formula varagʻi</span></li>
  <li><b>provided</b><span>berilgan</span></li>
  <li><b>volume</b><span>hajm</span></li>
  <li><b>cone</b><span>konus</span></li>
  <li><b>cylinder</b><span>silindr</span></li>
  <li><b>sphere</b><span>shar</span></li>
  <li><b>pyramid</b><span>piramida</span></li>
  <li><b>slope formula</b><span>qiyalik formulasi</span></li>
  <li><b>memorise</b><span>yodlamoq</span></li>
  <li><b>look up</b><span>qarab olmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Varaqdagini <b>yodlamang</b>; varaqda yoʻqlarini yodlang.</li>
    <li>Majburiy uchta: <b>qiyalik · SOH-CAH-TOA · aylana
        tenglamasi</b>.</li>
    <li>Konus va piramidada <b>uchdan bir</b> bor.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-99 — the adaptive second module
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-99: Pacing for Module 2 (The Adaptive Test)",
        "category": "math",
        "order": 99,
        "summary": (
            "Birinchi modul ikkinchisini tanlaydi. Shu bitta fakt imtihon "
            "kunining butun rejasini belgilaydi."
        ),
        "stories":  ["The Bar Rises Until It Finds You"],
        "content": """
<h2>SAT-99: Pacing for Module 2 (The Adaptive Test)</h2>

<p>Raqamli SAT eski qogʻoz testdan bitta muhim narsa bilan farq qiladi:
u <b>moslashadi</b>. Birinchi modul hammaga bir xil keladi, ikkinchisi
esa <mark>sizning birinchi moduldagi natijangizga qarab
tanlanadi</mark>. Bu dars shu bitta faktning amaliy oqibatlari
haqida.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Testning tuzilishi</span>
  <ul>
    <li>Matematika — <b>ikkita modul</b>, har birida 22 savol,
        35 daqiqa.</li>
    <li><b>1-modul</b> hammaga bir xil.</li>
    <li><b>2-modul</b> 1-moduldagi natijaga qarab tanlanadi.</li>
    <li><b>Ikkalasi ham</b> ballga kiradi — jami <b>44 savol</b> va
        <b>70 daqiqa</b>.</li>
    <li>Modul yopilgach, unga <b>qaytib boʻlmaydi</b>.</li>
  </ul>
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>1-modulni nega toʻliq tugatish kerakligini bilasiz;</li>
    <li>ikkala modul uchun alohida surʼat rejasini tuzasiz;</li>
    <li>2-modul qiyin chiqqanda ruhingiz tushmaydi;</li>
    <li>2-modul oson chiqqanda eʼtiborni pasaytirmaysiz.</li>
  </ul>
</div>

<h3>Nega 1-modul alohida ogʻirlikka ega</h3>

<p>1-moduldagi har bir javob ikki ish qiladi: ballga qoʻshiladi
<b>va</b> keyingi modulni tanlaydi. Shuning uchun u yerda
<b>aniqlik tezlikdan muhimroq</b> — ayniqsa dastlabki savollarda,
ular odatda osonroq va ularni shoshib yoʻqotish eng achinarli
yoʻqotish.</p>

<table class="pe-table">
  <tr><th>Modul</th><th>Asosiy maqsad</th><th>Surʼat</th></tr>
  <tr><td>1-modul, 1–11-savollar</td><td>xatosiz yurish</td>
      <td>tez, lekin shoshmasdan</td></tr>
  <tr><td>1-modul, 12–22</td><td>hammasiga javob belgilash</td>
      <td>90 soniya, keyin belgilab qoldiring</td></tr>
  <tr><td>2-modul</td><td>boshlangan ishni tugatish</td>
      <td>bir xil 95 soniya, koʻproq belgilash</td></tr>
</table>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling — eng qimmat xato</span>
  1-modulda vaqt tugab, uch-toʻrtta savol <b>boʻsh</b> qolishi. Jarima
  yoʻq (SAT-88), demak boʻsh qoldirishning hech qanday sababi yoʻq —
  va bu yerda u ikki barobar qimmat, chunki boʻsh javob keyingi
  modulni ham pasaytiradi.
</div>

<h3>2-modul qiyin chiqdi — bu yaxshi xabar</h3>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha — imtihon kunidagi eng muhim jumla</span>
  Agar ikkinchi modul birinchisidan sezilarli qiyin tuyulsa, bu
  <b>birinchi modulni yaxshi yozganingizni</b> bildiradi. Koʻp
  oʻquvchi buni teskari tushunadi va tushkunlikka tushib, qolgan
  savollarni ham yoʻqotadi. Qiyinlik darajasi ballning hisobiga
  <b>allaqachon kiritilgan</b> — qiyin modulda kamroq toʻgʻri javob
  ham yuqori ball berishi mumkin.
</div>

<p>Teskarisi ham rost: modul oson tuyulsa, bu eʼtiborni pasaytirish
uchun sabab emas. Har bir savol baribir hisobga olinadi, va oson
savolni yoʻqotish qiyinini yoʻqotishdan koʻra achinarliroq.</p>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">25 s</span></p>
  <div class="ps-stem__q">
    <p>What determines which second module a student receives?</p>
  </div>
  <ol class="ps-ch">
    <li>Their performance on the first module</li>
    <li>The order in which they answered</li>
    <li>The test date</li>
    <li>Nothing — it is the same for everyone</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) Their performance on the first
      module</p>
      <p>Shuning uchun 1-modulni toʻliq tugatish alohida
      muhim.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">Nothing — it is the same for everyone</span>
  <span class="ps-trap__why">Bu <b>birinchi</b> modul haqida rost.
  Ikkinchisi haqida emas — va aynan shu farq butun strategiyani
  yaratadi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">40 s</span></p>
  <div class="ps-stem__q">
    <p>A student finishes 22 questions in 30 minutes of a 35-minute
    module. How many seconds per question is that, on average?</p>
  </div>
  <ol class="ps-ch">
    <li>About 82</li>
    <li>About 95</li>
    <li>About 65</li>
    <li>About 110</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) About 82</p>
      <p>30 daqiqa — 1,800 soniya, va 1,800 ÷ 22 ≈ 82.</p>
      <p>Qolgan 5 daqiqa tekshirish uchun — bu yaxshi surʼat.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">About 95</span>
  <span class="ps-trap__why">Bu <b>toʻliq 35 daqiqa</b> uchun oʻrtacha.
  Savol esa 30 daqiqada tugatgan oʻquvchi haqida — hisobni qaytadan
  qilish kerak edi.</span>
</div>

<h3>Nima qilib boʻlmaydi</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Uchta «yoʻq»</span>
  <ol>
    <li><b>1-modulga qaytib boʻlmaydi</b> — yopilgach, u
        yopiq.</li>
    <li><b>2-modulni ataylab sekinlashtirib boʻlmaydi</b> —
        qiyinlik allaqachon tanlangan.</li>
    <li><b>Modul qiyinligidan ball taxmin qilib boʻlmaydi</b> —
        va bu taxmin faqat asabni buzadi.</li>
  </ol>
</div>

<h3>Exam English</h3>

<ul class="ps-phrase">
  <li><b>adaptive</b><span>moslashuvchi</span></li>
  <li><b>module</b><span>modul (test boʻlimi)</span></li>
  <li><b>performance</b><span>natija, koʻrsatkich</span></li>
  <li><b>on average</b><span>oʻrtacha</span></li>
  <li><b>receives</b><span>oladi</span></li>
</ul>

<div class="pe-fix">
  <p class="pe-bad">1-modulda uch savol boʻsh qoldi</p>
  <p class="pe-good">Har biriga bitta javob belgilang</p>
  <p class="pe-fix__why">Jarima yoʻq, va boʻsh javob keyingi modulni
  ham pasaytiradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">«2-modul qiyin — demak yomon yozdim»</p>
  <p class="pe-good">«2-modul qiyin — demak yaxshi yozdim»</p>
  <p class="pe-fix__why">Qiyin modul birinchi moduldagi yaxshi
  natijadan keladi.</p>
</div>

<h3>1-modul uchun aniq reja</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Vaqt banki</span>
  <ol>
    <li><b>0–15 daqiqa:</b> 1–11-savollar. Bular odatda osonroq —
        maqsad ularni <b>xatosiz</b> olish, tez emas.</li>
    <li><b>15–30 daqiqa:</b> 12–22-savollar. Har biriga 90 soniya;
        oshsa, javob belgilab, belgilab qoldiring.</li>
    <li><b>30–33 daqiqa:</b> belgilanganlarga qayting.</li>
    <li><b>33–35 daqiqa:</b> boʻsh javob qolmasin. Faqat shu.</li>
  </ol>
</div>

<div class="pm-check">
  <p class="pm-check__t">Reja ishlayaptimi — bitta nazorat nuqtasi</p>
  <p>11-savolga yetganingizda soatga bir marta qarang. 15 daqiqadan
  kam sarflangan boʻlsa — surʼat yaxshi. 20 daqiqadan koʻp boʻlsa —
  qolgan savollarda belgilab qoldirishni koʻpaytiring, chunki
  yetib bormaslik xavfi bor.</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Soatga <b>bir marta</b> qarang, oʻn marta emas. Har bir qarash
  eʼtiborni uzadi va qaytadan yigʻish oʻn soniya oladi. Bitta
  nazorat nuqtasi (11-savol) butun modul uchun yetarli.
</div>

<h3>Oxirgi uch daqiqa</h3>

<p>Modulning oxirgi uch daqiqasi <b>yangi savol yechish uchun
emas</b>. Tartib qatʼiy:</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Uch daqiqalik tartib</span>
  <ol>
    <li>Boʻsh javoblarni toʻldiring — hammasini.</li>
    <li>Belgilangan savollardan <b>eng oson koʻringanini</b>
        oling.</li>
    <li>Vaqt qolsa — SAT-100 dagi toʻrtta nazoratni ikki-uchta
        javobga qoʻllang.</li>
  </ol>
  <p>⛔ Bu daqiqalarda <b>javobni almashtirmang</b>, agar yangi
  sabab topmagan boʻlsangiz. Shoshib almashtirilgan javob
  koʻpincha toʻgʻrisi edi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha — modullar orasida nima oʻtadi</span>
  <b>Hech narsa.</b> Belgilangan savollar, qoralama fikrlar,
  oʻchirilgan variantlar — hammasi oʻsha modul bilan qoladi. Shuning
  uchun modul tugashiga bir daqiqa qolganda «keyingisida qaytaman»
  degan fikr xato: qaytish yoʻq. Har bir modulni <b>alohida imtihon</b>
  deb qarang.
</div>

<h3>Moslashuv ballga qanday kiradi</h3>

<p>Ikkinchi modul qiyinroq boʻlsa, undagi savollar
<b>koʻproq ogʻirlikka ega</b> — shuning uchun qiyin moduldagi
kamroq toʻgʻri javob osonroq moduldagi koʻproq toʻgʻri javobdan
yuqori ball berishi mumkin. Bu adolatsizlik emas, tizimning
maqsadi: ikkala oʻquvchi ham <b>oʻz darajasida</b> sinaladi.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Amaliy xulosa bitta: <b>modul qiyinligini baholashga urinmang</b>.
  U sizga hech qanday foydali maʼlumot bermaydi va faqat qolgan
  savollarga toʻsqinlik qiladi. Savolni yeching, keyingisiga
  oʻting.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  How many math modules are there, and how long is each?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ikkita, har biri 35 daqiqa.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Does the second module count towards the score?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ha — ikkalasi ham hisobga olinadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A student finishes 22 questions in 33 minutes. Seconds per
  question?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">1,980 ÷ 22 = 90 soniya.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  The second module feels much harder. What does that suggest?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Birinchi modul yaxshi yozilgan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  May a student return to module one during module two?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>adaptive test</b><span>moslashuvchi test</span></li>
  <li><b>module</b><span>modul</span></li>
  <li><b>performance</b><span>natija</span></li>
  <li><b>difficulty</b><span>qiyinlik darajasi</span></li>
  <li><b>counts towards</b><span>… ga hisobga olinadi</span></li>
  <li><b>flag</b><span>belgilab qoʻymoq</span></li>
  <li><b>pace</b><span>surʼat</span></li>
  <li><b>accuracy</b><span>aniqlik</span></li>
  <li><b>closed</b><span>yopilgan</span></li>
  <li><b>on average</b><span>oʻrtacha</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>1-modul ikkinchisini <b>tanlaydi</b> — uni toʻliq
        tugating.</li>
    <li><b>Hech qachon boʻsh qoldirmang</b> — ayniqsa 1-modulda.</li>
    <li>Qiyin 2-modul — <b>yaxshi xabar</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-100 — THE FINALE
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-100: The Final Review Protocol (30-Second Double-Check)",
        "category": "math",
        "order": 100,
        "summary": (
            "Kursning oxirgi darsi: javobni belgilashdan oldingi toʻrtta "
            "savol, va yuz darsning bitta xaritasi."
        ),
        "stories":  ["The Mountain Is Not Finished at the Top"],
        "content": """
<h2>SAT-100: The Final Review Protocol (30-Second Double-Check)</h2>

<p>Yuzinchi dars. U yangi matematika keltirmaydi —
<mark>u qolgan toʻqson toʻqqiztasini bitta odatga bogʻlaydi</mark>:
javobni belgilashdan oldin oʻttiz soniya. Bu oʻttiz soniya butun
kursdagi eng arzon ball manbayi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>toʻrtta yakuniy savolni avtomatik berasiz;</li>
    <li>butun kursning xaritasini koʻrasiz;</li>
    <li>nima yodlash kerakligini aniq bilasiz;</li>
    <li>imtihonga nima olib borishingizni bilasiz.</li>
  </ul>
</div>

<h3>Toʻrtta savol</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">The 30-second protocol</span>
  <ol>
    <li><b>Savolga javob berdimmi?</b> Oxirgi jumlani qayta oʻqing.
        <i>x</i> mi, <i>x</i> + <i>y</i> mi, kattalar soni mi?
        (SAT-89, 1-tur)</li>
    <li><b>Birlik toʻgʻrimi?</b> Soat, daqiqa, sent, santimetr.
        (SAT-89, 4-tur)</li>
    <li><b>Kattaligi maʼqulmi?</b> Chegirmali narx aslidan kichik,
        ehtimollik birdan kichik, oʻrtacha chekkalar orasida.
        (SAT-87)</li>
    <li><b>Shakli toʻgʻrimi?</b> Grid-in boʻlsa: belgilar soni,
        vergul yoʻq, aralash son yoʻq. (SAT-90)</li>
  </ol>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha — nega aynan toʻrtta</span>
  Bu toʻrttasi tasodifiy tanlanmagan. Ular SAT-89 dagi yettita
  tuzoqning <b>oltitasini</b> qamrab oladi. Yettinchisi — notoʻgʻri
  amal — bu yerda tutilmaydi, uni faqat matematikani bilish tutadi.
  Shuning uchun taktika oxirida, matematika esa boshida turibdi.
</div>

<h3>Yuz darsning xaritasi</h3>

<table class="pe-table">
  <tr><th>Blok</th><th>Darslar</th><th>Nima berdi</th></tr>
  <tr><td><b>A · The Heart of Algebra</b></td><td>1–22</td>
      <td>ifoda → tenglama → chiziq → sistema → tengsizlik</td></tr>
  <tr><td><b>B · Advanced Math</b></td><td>23–48</td>
      <td>daraja, koʻphad, kvadrat tenglama, ildiz, funksiya</td></tr>
  <tr><td><b>C · Problem-Solving &amp; Data</b></td><td>49–65</td>
      <td>nisbat, foiz, birlik, jadval, statistika, ehtimollik</td></tr>
  <tr><td><b>D · Geometry &amp; Trigonometry</b></td><td>66–80</td>
      <td>burchak, uchburchak, oʻxshashlik, aylana, trigonometriya</td></tr>
  <tr><td><b>E · Tactics &amp; Desmos</b></td><td>81–100</td>
      <td>son qoʻyish, backsolving, Desmos, tuzoq, format, vaqt</td></tr>
</table>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Bu jadvalni mashq testidan keyin ishlating: har bir yoʻqotilgan
  savolni <b>blokka</b> yozing. Uch-toʻrt testdan keyin bitta blok
  aniq ajralib turadi, va takrorlashni aynan oʻsha yerdan boshlash
  kerak. «Hammasini qaytadan oʻqish» — eng samarasiz reja.
</div>

<h3>Imtihonga nima olib borasiz</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Xotirada boʻlishi shart</span>
  <ol>
    <li><b>Uchta formula:</b> qiyalik · SOH-CAH-TOA · aylana
        tenglamasi (SAT-98).</li>
    <li><b>Ikkita taktika belgisi:</b> javoblarda harf boʻlsa son
        qoʻying, son boʻlsa javobni qoʻying (SAT-81 va SAT-82).</li>
    <li><b>Ikkita chekka odat:</b> «must be true» da qarshi misol,
        chizmada «not drawn to scale» yozuvi (SAT-93 va SAT-86).</li>
    <li><b>Bitta qolip:</b> MAQSAD · BERILGAN · ISH · JAVOB
        (SAT-95).</li>
    <li><b>Bitta jumla:</b> «u nimani soʻragan edi?»</li>
  </ol>
</div>

<h3>SAT savollari — protokolni qoʻllash</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>A jacket costs $80 and is reduced by 25 percent. A student
    computes 20 and marks it. What should the final check have
    caught?</p>
  </div>
  <ol class="ps-ch">
    <li>20 is the discount, not the sale price</li>
    <li>The units are wrong</li>
    <li>The answer should be negative</li>
    <li>The percent was applied twice</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 20 is the discount, not the sale
      price</p>
      <p>Birinchi savol — «savolga javob berdimmi?». Chegirma 20,
      yangi narx esa 60.</p>
      <p>Uchinchi savol ham buni tutardi: chegirmali narx asl narxning
      choragi boʻla olmaydi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">The units are wrong</span>
  <span class="ps-trap__why">Birlik bu yerda toʻgʻri — ikkalasi ham
  dollar. Protokolning toʻrtta savoli <b>tartib bilan</b> beriladi,
  va birinchisi allaqachon javobni topgan edi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>A grid-in answer works out to two and a half. A student types
    2 1/2. Which check should have caught it?</p>
  </div>
  <ol class="ps-ch">
    <li>The form of the answer</li>
    <li>The question that was asked</li>
    <li>The unit</li>
    <li>The size of the answer</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) The form of the answer</p>
      <p>Matematika toʻgʻri, savol toʻgʻri, birlik toʻgʻri, kattaligi
      toʻgʻri. Faqat shakl notoʻgʻri: qutida 2 1/2 → 21/2 boʻlib
      oʻqiladi (SAT-90). Javob 2.5 yoki 5/2 boʻlishi kerak edi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">The size of the answer</span>
  <span class="ps-trap__why">Ikki yarim — mutlaqo maʼqul kattalik.
  Bu savol nimani sinayotganini koʻrsatadi: <b>toʻrtta nazorat
  toʻrt xil xatoni</b> tutadi, va ularni chalkashtirmaslik kerak.</span>
</div>

<h3>Protokol qachon oʻtkazib yuboriladi</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Ikkita «yoʻq»</span>
  <ol>
    <li><b>Vaqt tugayotgan boʻlsa</b> — boʻsh savolni toʻldirish
        tekshirishdan muhimroq (SAT-88).</li>
    <li><b>Javob bitta oʻqishda olingan boʻlsa</b> — «What is 10
        percent of 50?» uchun toʻrtta savol ortiqcha. Protokol
        <b>koʻp qadamli</b> savollar uchun.</li>
  </ol>
</div>

<h3>Exam English — oxirgi roʻyxat</h3>

<ul class="ps-phrase">
  <li><b>which of the following</b><span>quyidagilardan qaysi biri</span></li>
  <li><b>the value of</b><span>… ning qiymati</span></li>
  <li><b>in terms of</b><span>… orqali</span></li>
  <li><b>must be true</b><span>har doim toʻgʻri</span></li>
  <li><b>not drawn to scale</b><span>masshtabda emas</span></li>
  <li><b>to the nearest</b><span>… gacha yaxlitlab</span></li>
</ul>

<div class="pe-fix">
  <p class="pe-bad">Hisob tugadi → belgiladim</p>
  <p class="pe-good">Hisob tugadi → toʻrtta savol → belgiladim</p>
  <p class="pe-fix__why">Oʻttiz soniya yettita tuzoqning oltitasini
  tutadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Vaqt tugayapti → tekshiraman</p>
  <p class="pe-good">Vaqt tugayapti → boʻshlarni toʻldiraman</p>
  <p class="pe-fix__why">Boʻsh javobning qiymati aniq nol.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oxirgi soʻz</span>
  Yuzta dars tugadi. Ular sizga ikki narsa bergan boʻlishi kerak edi:
  <b>matematika</b> — birinchi sakson darsda, va <b>testni yechish
  usuli</b> — oxirgi yigirmasida. Ikkalasi ham kerak, lekin tartib
  muhim: taktika bilimni tezlashtiradi, uning oʻrnini bosmaydi.
  <br><br>
  Endi qolgani mashq. Har bir mashq testidan keyin xatolaringizni
  blokka va tuzoq turiga ajratib yozing — bu ikkita roʻyxat sizga
  qaysi darsga qaytish kerakligini aytib turadi. Kurs shuning uchun
  yuzta darsdan iborat: <b>u boshdan oxirigacha bir marta oʻqiladigan
  kitob emas, qaytib kelinadigan javon</b>.
  <br><br>
  Omad tilaymiz — va imtihon kuni oʻsha oxirgi jumlani unutmang:
  <b>«u nimani soʻragan edi?»</b>
</div>

<h3>Yettita tuzoq — oxirgi eslatma</h3>

<p>SAT-89 dagi roʻyxat imtihondan oldingi kechada bir marta oʻqib
chiqishga arziydi. Mana u qisqartirilgan holda:</p>

<table class="pe-table">
  <tr><th>#</th><th>Tuzoq</th><th>Qaysi nazorat tutadi</th></tr>
  <tr><td>1</td><td>Boshqa savolning javobi</td><td>1-nazorat</td></tr>
  <tr><td>2</td><td>Yarim yoʻlda toʻxtash</td><td>1-nazorat</td></tr>
  <tr><td>3</td><td>Ishora almashishi</td><td>3-nazorat</td></tr>
  <tr><td>4</td><td>Birlik oʻgirilmagan</td><td>2-nazorat</td></tr>
  <tr><td>5</td><td>Ikkinchi ildiz</td><td>1-nazorat</td></tr>
  <tr><td>6</td><td>Oʻrtacha ↔ chekka</td><td>1-nazorat</td></tr>
  <tr><td>7</td><td>Notoʻgʻri amal</td><td>faqat matematika</td></tr>
</table>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Oxirgi qatorga eʼtibor bering</span>
  Yettinchi tuzoqni hech qanday protokol tutmaydi. Uni faqat
  <b>bilim</b> tutadi — va aynan shuning uchun bu kursda taktika
  yigirmata dars, matematika esa saksonta.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Name the four checks in order.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Savol · birlik · kattalik · shakl.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  A speed comes out as 1.67 for a train. Which check catches it?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Kattalik — va birlik: javob km/daqiqada
  chiqqan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Which block covers ratios, percentages and tables?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Blok C, 49–65-darslar.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Which three formulas must you memorise?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Qiyalik, SOH-CAH-TOA, aylana
  tenglamasi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  With ten seconds left and one blank question, what do you do?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Bitta variant belgilaysiz — tekshirmaysiz.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>protocol</b><span>tartib, qoida</span></li>
  <li><b>double-check</b><span>qayta tekshirish</span></li>
  <li><b>catch a mistake</b><span>xatoni tutmoq</span></li>
  <li><b>plausible</b><span>maʼqul, ishonarli</span></li>
  <li><b>the form of the answer</b><span>javobning shakli</span></li>
  <li><b>skip</b><span>oʻtkazib yubormoq</span></li>
  <li><b>review</b><span>qayta koʻrib chiqmoq</span></li>
  <li><b>in order</b><span>tartib bilan</span></li>
  <li><b>habit</b><span>odat</span></li>
  <li><b>revise</b><span>takrorlamoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Yuz darsdan uch jumla</p>
  <ul>
    <li>Javobni belgilashdan oldin: <b>savol · birlik · kattalik ·
        shakl</b>.</li>
    <li>Xatolaringizni <b>blokka va tuzoq turiga</b> ajratib
        yozing.</li>
    <li>Va oxirgi jumla, har safar: <b>«u nimani soʻragan
        edi?»</b></li>
  </ul>
</div>
""",
    },
]
