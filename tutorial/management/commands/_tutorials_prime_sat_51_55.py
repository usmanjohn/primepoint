# -*- coding: utf-8 -*-
"""Prime SAT Math — lessons 51–55 (Blok C ning oʻzagi: foiz, jadval, grafik).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_SAT.md
Lesson list: tutorial/management/commands/toc_prime_sat_math.txt

⚠️ SARLAVHALAR BAZADAN OLINGAN, aynan.

⚠️ Blok C: matematikasi eng yengil, ingliz tili eng ogʻir. Har darsda kamida
   bitta INTERPRETATSIYA savoli — hisoblash emas, jumlani va oʻqni oʻqish.

⚠️ Kumulyativ (SAT-1…50 erkin, jumladan nisbat, proporsiya, birlik almashtirish):
  • SAT-51 — foizning uch shakli: qism, butun, foizning oʻzi.
  • SAT-52 — foiz oʻzgarishi; ketma-ket oʻzgarishlar qoʻshilmaydi.
  • SAT-53 — jadval, chiziqli grafik va ustunli diagrammani oʻqish.
  • SAT-54 — sochilma diagramma, eng mos chiziq, qoldiq va sabab-oqibat.
  • SAT-55 — oʻrta arifmetik va mediana; chetdagi qiymat qaysinisini tortadi.
  • ⛔ Moda va oraliq (SAT-56) YOʻQ; standart ogʻish (SAT-57) YOʻQ;
    ehtimollik (SAT-58) YOʻQ.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_sat_51_55.py \\
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
    # SAT-51 — percentages: part, whole, base
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-51: Percentages — Part, Whole, and Base",
        "category": "math",
        "order": 51,
        "summary": (
            "Foiz savolining uch shakli bor, va uchalasi bitta tenglamadan chiqadi: "
            "qism = foiz × butun. Qiyin qismi butunni topish."
        ),
        "stories": ["Sixty Percent of Whom?"],
        "content": """
<h2>SAT-51: Percentages — Part, Whole, and Base</h2>

<p>Foiz — SAT'da eng koʻp uchraydigan mavzu, va uning butun mexanikasi
<mark>bitta tenglamada</mark> joylashgan. Uchta savol shakli bor, chunki shu
tenglamaning uchta harfidan biri nomaʼlum boʻlishi mumkin.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>uch shaklni bir-biridan ajratasiz;</li>
    <li>«of» soʻzini koʻpaytirish deb oʻqiysiz;</li>
    <li>butunni topish uchun boʻlasiz, koʻpaytirmaysiz;</li>
    <li>foiz <b>qaysi</b> sondan olinayotganini har safar aniqlaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The one equation</span>
  <span class="pe-chip pe-chip--s">qism</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">foiz</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--o">butun</span>
</div>

<h3>Uch shakl</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Savol</th><th>Nomaʼlum</th><th>Amal</th><th>Javob</th></tr>
  <tr><td>What is 15% of 80?</td><td>qism</td>
      <td class="pm-word__sym">0.15 × 80</td><td>12</td></tr>
  <tr><td>12 is 15% of what?</td><td>butun</td>
      <td class="pm-word__sym">12 ÷ 0.15</td><td>80</td></tr>
  <tr><td>12 is what percent of 80?</td><td>foiz</td>
      <td class="pm-word__sym">12 ÷ 80</td><td>15%</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Uchalasi bir xil vaziyat — faqat savol boshqa tomondan berilgan. Qaysi son
  qayerda turganini aniqlash uchun <b>«of» soʻzidan keyingi son butun</b> ekanini
  eslang: «15% <u>of 80</u>» da butun 80.
</div>

<h3>Butunni topish — eng koʻp adashiladigan shakl</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">18 is 30% of what number?</span>
    <span class="pm-solve__why">Qism 18, foiz 30, butun nomaʼlum</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">18 = 0.30 × butun</span>
    <span class="pm-solve__why">Tenglamani shunchaki yozdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">butun = 18 ÷ 0.30 = 60</span>
    <span class="pm-solve__why">Tekshiruv: 30 foizi 18 ✓</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Bu yerda <b>boʻlish</b> kerak, koʻpaytirish emas. 18 × 0.30 = 5.4 — bu javob
  18 dan <u>kichik</u>, holbuki butun qismdan katta boʻlishi shart. Javobning
  kattaligiga qarab tekshiring.
</div>

<h3>Baza — foiz qaysi sondan olinadi</h3>

<p>20 foizning oʻzi hech narsani anglatmaydi; u qaysi sondan olinayotganiga
bogʻliq. 50 ning 20 foizi 10, 200 ning 20 foizi 40. SAT bu farqni ataylab
ishlatadi: bir savolda ikkita boshqa-boshqa baza boʻlishi mumkin.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Foizni <b>oʻnli kasrga</b> aylantirib ishlang: 15% → 0.15, 7% → 0.07,
  120% → 1.2. Kasr bilan ishlash kalkulyatorda ham, ogʻzaki ham tezroq, va
  «100 ga boʻlishni unutdim» degan xatoni yoʻq qiladi.
</div>

<h3>Foizdan foiz</h3>

<p>«60 foiz oʻquvchining 25 foizi» degan ibora ikki bosqichli koʻpaytirish
demakdir: 0.25 × 0.60 = 0.15, yaʼni hammaning 15 foizi. Bu SAT'da tez-tez
uchraydi va ikki foizni <b>qoʻshib</b> yuborish keng tarqalgan xato.</p>

<h3>Foizni ogʻzaki hisoblash</h3>

<p>Kalkulyator bor, lekin oson foizlarni ogʻzaki olish vaqtni tejaydi va
javobni tekshirishga imkon beradi. Uchta tayanch yetadi:</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Foiz</th><th>Qanday olinadi</th><th>Misol: 240</th></tr>
  <tr><td>10%</td><td class="pm-word__sym">oʻnga boʻling</td><td>24</td></tr>
  <tr><td>1%</td><td class="pm-word__sym">yuzga boʻling</td><td>2.4</td></tr>
  <tr><td>50%</td><td class="pm-word__sym">yarmini oling</td><td>120</td></tr>
</table></div>

<p>Qolganini shulardan yigʻish mumkin: 35 foiz — bu 10 + 10 + 10 + 1 + 1 + 1 + 1 + 1,
yoki qisqaroq: 50 foizdan 15 foizni ayirish. 240 uchun 35 foiz = 120 − 36 = 84.
Tekshiruv: 0.35 × 240 = 84 ✓</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Foizning muhim xossasi: <b>«A ning B foizi» va «B ning A foizi» teng</b>.
  4 ning 75 foizini hisoblash qiyin koʻrinadi; 75 ning 4 foizi esa 3 — va javob
  oʻsha. SAT'da bu almashtirish baʼzan butun savolni ogʻzaki qiladi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>what is 15 percent of 80</b><span>80 ning 15 foizi nechaga teng</span></li>
  <li><b>18 is 30 percent of what number</b><span>18 — qaysi sonning 30 foizi</span></li>
  <li><b>what percent of 80 is 12</b><span>12 — 80 ning necha foizi</span></li>
  <li><b>of the remaining students</b><span>qolgan oʻquvchilarning … — baza oʻzgardi</span></li>
  <li><b>rounded to the nearest percent</b><span>butun foizgacha yaxlitlangan</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>The number 18 is 30% of what number?</p>
  </div>
  <ol class="ps-ch">
    <li>60</li>
    <li>5.4</li>
    <li>54</li>
    <li>48</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 60</p>
      <p>18 ÷ 0.30 = 60. Tekshiruv: 60 ning 30 foizi 18 ✓</p>
      <p><b>5.4</b> — koʻpaytirilgan. Butun har doim qismdan katta boʻlishi
      kerak edi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">5.4</span>
  <span class="ps-trap__why">Koʻpaytirish va boʻlish almashtirilgan. Javob
  berilgan sondan kichik chiqsa, «butunni topish» savolida bu darrov
  xato.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>In a school, 60% of the students study a foreign language. Of those
    students, 25% study Korean. What percent of all the students study
    Korean?</p>
  </div>
  <ol class="ps-ch">
    <li>15%</li>
    <li>85%</li>
    <li>35%</li>
    <li>25%</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 15%</p>
      <p>0.25 × 0.60 = 0.15. «Of those students» — baza endi butun maktab emas,
      chet tili oʻqiydiganlar.</p>
      <p>100 kishilik maktab bilan tekshiring: 60 kishi til oʻqiydi, ularning
      25 foizi 15 kishi ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">85%</span>
  <span class="ps-trap__why">Ikki foiz <b>qoʻshilgan</b>. Foizlar faqat bir xil
  bazadan olinganda qoʻshiladi; bu yerda ikkinchisi birinchisining ichida.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Foiz savolida <b>100 ta narsani tasavvur qiling</b>:</p>
  <ol>
    <li>Maktabda 100 oʻquvchi bor deb faraz qiling;</li>
    <li>Har bir foizni odam soniga aylantiring;</li>
    <li>Javobni qaytadan foizga oʻgiring.</li>
  </ol>
  <p>Bu usul foizdan foiz masalalarini deyarli ogʻzaki yechadi va bazani
  adashtirishga yoʻl qoʻymaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">18 is 30% of what → 18 × 0.3 = 5.4</p>
  <p class="pe-good">18 ÷ 0.3 = 60</p>
  <p class="pe-fix__why">Butun izlanayotganda boʻlinadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">60% ning 25% i → 85%</p>
  <p class="pe-good">15%</p>
  <p class="pe-fix__why">«Of» koʻpaytirishni bildiradi, qoʻshishni emas.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  100 dan katta foiz ham boʻladi: «150 foiz» degani 1.5 barobar. Narx 200 dan
  300 ga chiqsa, yangi narx eskisining <b>150 foizi</b>, lekin oʻsish
  <b>50 foiz</b> (SAT-52). Bu ikki jumlani aralashtirmang.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Blok C da savolning <b>oxirgi jumlasi</b> eng muhim: «what percent of all the
  students» va «what percent of those students» butunlay boshqa savollar.
  Bazani belgilab qoʻying, keyin hisoblang.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  What is 25% of 64?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">16.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  9 is what percent of 45?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">20% — 9 ÷ 45 = 0.2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  21 is 30% of what number?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">70 — 21 ÷ 0.3.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  40% of a class of 30 are girls. How many boys are there?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">18 — qizlar 12, demak oʻgʻillar 30 − 12.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  80% of the workers are full-time, and 50% of those are women. What percent of
  all workers are full-time women?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">40% — 0.5 × 0.8.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>percent of</b><span>… ning foizi</span></li>
  <li><b>the whole / the base</b><span>butun / asos</span></li>
  <li><b>the part</b><span>qism</span></li>
  <li><b>of those</b><span>ulardan (baza oʻzgaradi)</span></li>
  <li><b>the remaining</b><span>qolgan</span></li>
  <li><b>rounded to the nearest percent</b><span>butun foizgacha</span></li>
  <li><b>what percent</b><span>necha foiz</span></li>
  <li><b>full-time</b><span>toʻliq stavkada</span></li>
  <li><b>at least</b><span>kamida</span></li>
  <li><b>approximately</b><span>taxminan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Bitta tenglama: <b>qism = foiz × butun</b>.</li>
    <li>Butun izlansa — <b>boʻling</b>; javob qismdan katta boʻlishi kerak.</li>
    <li><b>«Of»</b> koʻpaytirishdir, va undan keyingi son bazani belgilaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-52 — percent change
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-52: Percent Change — Increase, Decrease, and Successive Changes",
        "category": "math",
        "order": 52,
        "summary": (
            "Oʻzgarish har doim ESKI qiymatga boʻlinadi. Ketma-ket oʻzgarishlar "
            "esa qoʻshilmaydi — koʻpaytiriladi."
        ),
        "stories": ["Down Forty, Up Forty"],
        "content": """
<h2>SAT-52: Percent Change — Increase, Decrease, and Successive Changes</h2>

<p>Foiz oʻzgarishida bitta qoida hamma narsani hal qiladi: <mark>oʻzgarish
eskisiga boʻlinadi</mark>. Va bundan ikkinchi, kutilmaganroq fakt kelib chiqadi:
20 foiz oshirib, keyin 20 foiz kamaytirsangiz, boshlangʻich holatga
<b>qaytmaysiz</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>oʻsish va kamayish foizini bir formuladan topasiz;</li>
    <li>maxrajga har doim <b>eski</b> qiymatni qoʻyasiz;</li>
    <li>ketma-ket oʻzgarishlarni koʻpaytirasiz, qoʻshmaysiz;</li>
    <li>«increased by» va «increased to» ni ajratasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Percent change</span>
  <span class="pe-chip pe-chip--v">(yangi − eski)</span>
  <span class="pe-op">÷</span>
  <span class="pe-chip pe-chip--s">eski</span>
  <span class="pe-op">× 100</span>
</div>

<h3>Ikki yoʻnalish, bitta formula</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">50 dan 65 ga</span>
    <span class="pm-solve__why">Oʻzgarish +15</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">15 ÷ 50 = 0.30</span>
    <span class="pm-solve__why">Maxrajda <b>50</b>, 65 emas</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">30 foiz oʻsish</span>
    <span class="pm-solve__why">Tekshiruv: 50 × 1.30 = 65 ✓</span>
  </div>
</div>

<p>Kamayish ham xuddi shunday: 80 dan 60 ga tushsa, oʻzgarish −20 va
20 ÷ 80 = 0.25 — yaʼni 25 foizga kamaygan.</p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Maxrajga <b>eski</b> qiymat qoʻyiladi. 80 dan 60 ga tushishni 20 ÷ 60 deb
  hisoblasangiz 33 foiz chiqadi — va bu javob variantlar orasida albatta
  turadi.
</div>

<h3>Ketma-ket oʻzgarishlar qoʻshilmaydi</h3>

<p>Narx 20 foizga oshdi, keyin 20 foizga tushdi. Koʻpchilik «demak oʻsha-oʻsha»
deb oʻylaydi. Sanab koʻramiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">100 × 1.20 = 120</span>
    <span class="pm-solve__why">20 foiz oshdi — 20 qoʻshildi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">120 × 0.80 = 96</span>
    <span class="pm-solve__why">20 foiz tushdi — lekin endi <b>120</b> dan, 24 ayirildi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">96 — yaʼni 4 foizga kamaygan</span>
    <span class="pm-solve__why">1.20 × 0.80 = 0.96</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Sabab bitta jumlada: <b>ikkinchi foiz boshqa sondan olinadi</b>. Oshganda 100
  dan 20 olinadi, tushganda 120 dan 24. Shuning uchun ketma-ket oʻzgarishlarni
  <b>koʻpaytiring</b>: 1.20 × 0.80 = 0.96, demak 4 foiz kamaygan.
</div>

<h3>«By» va «to» — ikki boshqa jumla</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Jumla</th><th>Maʼnosi</th><th>200 uchun natija</th></tr>
  <tr><td>increased <b>by</b> 30%</td><td class="pm-word__sym">×1.30</td><td>260</td></tr>
  <tr><td>increased <b>to</b> 130%</td><td class="pm-word__sym">×1.30</td><td>260</td></tr>
  <tr><td>increased <b>to</b> 30%</td><td class="pm-word__sym">×0.30</td><td>60</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Ikki soʻzli qoida: <b>«by» — oʻzgarish, «to» — yangi qiymat</b>. Ingliz
  tilida bu bitta harflik farq, matematikada esa butunlay boshqa amal. Blok C
  savollarini oʻqiyotganda shu ikki soʻzni belgilab qoʻying.
</div>

<h3>Teskari savol — dastlabki narxni topish</h3>

<p>SAT koʻpincha yakuniy narxni berib, dastlabkisini soʻraydi. Bu SAT-51 dagi
«butunni topish» shaklining oʻzi: koʻpaytirish emas, <b>boʻlish</b> kerak.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">20 foiz chegirmadan keyin narx 48</span>
    <span class="pm-solve__why">48 — dastlabkining 80 foizi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">48 ÷ 0.80 = 60</span>
    <span class="pm-solve__why">Tekshiruv: 60 ning 20 foizi 12, va 60 − 12 = 48 ✓</span>
  </div>
</div>

<p>Eng koʻp uchraydigan xato — 48 ga 20 foiz qoʻshish (57.6). Chegirma
<b>60</b> dan olingan edi, 48 dan emas: baza yana boshqa.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>percent increase</b><span>foizdagi oʻsish</span></li>
  <li><b>percent decrease</b><span>foizdagi kamayish</span></li>
  <li><b>increased by 30%</b><span>30 foizga oshdi (×1.3)</span></li>
  <li><b>increased to 130% of</b><span>… ning 130 foiziga yetdi</span></li>
  <li><b>a discount of 20%, then a further 10%</b><span>20 foiz chegirma, keyin yana 10</span></li>
  <li><b>the original price</b><span>dastlabki narx — maxrajga shu tushadi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">55 s</span></p>
  <div class="ps-stem__q">
    <p>The number of members of a club fell from 80 to 60 over a year. What was the
    percent decrease?</p>
  </div>
  <ol class="ps-ch">
    <li>25%</li>
    <li>33%</li>
    <li>20%</li>
    <li>75%</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 25%</p>
      <p>Oʻzgarish 20, va u <b>eski</b> qiymatga boʻlinadi: 20 ÷ 80 = 0.25.</p>
      <p><b>33%</b> — 20 ÷ 60 hisoblangan, yaʼni yangi qiymatga boʻlingan.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">33%</span>
  <span class="ps-trap__why">Maxrajda yangi qiymat turgan. Foiz oʻzgarishi har
  doim <b>boshlangʻich</b> holatdan oʻlchanadi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>A price is increased by 10% and then decreased by 10%. Compared with the
    original price, the final price is</p>
  </div>
  <ol class="ps-ch">
    <li>1% lower</li>
    <li>the same</li>
    <li>1% higher</li>
    <li>10% lower</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 1% lower</p>
      <p>1.10 × 0.90 = 0.99, yaʼni dastlabkining 99 foizi.</p>
      <p>100 bilan tekshiring: 110, keyin 110 dan 11 ayiriladi → 99.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">the same</span>
  <span class="ps-trap__why">Ikki foiz bir-birini yoʻqqa chiqaradi deb
  oʻylangan. Ular boshqa-boshqa sondan olingani uchun tenglashmaydi —
  natija har doim dastlabkidan <b>past</b>.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Ketma-ket foiz savolida <b>100 dan boshlang</b>:</p>
  <ol>
    <li>Dastlabki qiymat 100 deb oling;</li>
    <li>Har bir oʻzgarishni koeffitsient bilan qoʻllang (1.2, 0.8, 1.05…);</li>
    <li>Oxirgi sonni 100 bilan solishtiring — farqi toʻgʻridan-toʻgʻri
        foizda chiqadi.</li>
  </ol>
  <p>Bu usul har qanday ketma-ket oʻzgarishni 20 soniyada hal qiladi va tartib
  masalasini ham koʻrsatadi: koʻpaytirish tartibi natijaga taʼsir qilmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">80 dan 60 ga → 20 ÷ 60 = 33%</p>
  <p class="pe-good">20 ÷ 80 = 25%</p>
  <p class="pe-fix__why">Maxrajda eski qiymat turadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">+20% keyin −20% → oʻzgarmaydi</p>
  <p class="pe-good">4 foizga kamayadi</p>
  <p class="pe-fix__why">1.2 × 0.8 = 0.96 — ikkinchi foiz kattaroq sondan
  olinadi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ketma-ket oʻzgarishlar natijasi <b>har doim</b> dastlabkidan past boʻladi,
  agar ikkala foiz teng boʻlsa — oshirish oldinmi yoki keyinmi, farqi yoʻq.
  Koʻpaytirish tartibi natijani oʻzgartirmaydi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Chegirmalar ham shunday: «20 foiz, keyin yana 10 foiz» degani 30 foiz emas.
  0.80 × 0.90 = 0.72, yaʼni jami 28 foiz chegirma. Doʻkonlar bu farqni yaxshi
  biladi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  A price rises from 40 to 50. What is the percent increase?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">25% — 10 ÷ 40.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  A number falls from 200 to 150. What is the percent decrease?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">25% — 50 ÷ 200.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A value is increased by 50% and then decreased by 50%. What fraction of the
  original remains?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">75% — 1.5 × 0.5 = 0.75, yaʼni 25 foiz
  yoʻqolgan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  A coat costs 200. It is discounted 20%, then a further 10% off the sale price.
  What is the final price?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">144 — 200 × 0.8 × 0.9. Jami chegirma 28 foiz, 30
  emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A number is increased to 130% of itself. By what percent did it increase?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">30% — «to 130%» va «by 30%» bir xil narsa.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>percent increase</b><span>foizdagi oʻsish</span></li>
  <li><b>percent decrease</b><span>foizdagi kamayish</span></li>
  <li><b>the original value</b><span>dastlabki qiymat (maxraj)</span></li>
  <li><b>increased by / increased to</b><span>… ga oshdi / … gacha yetdi</span></li>
  <li><b>successive changes</b><span>ketma-ket oʻzgarishlar</span></li>
  <li><b>a further discount</b><span>qoʻshimcha chegirma</span></li>
  <li><b>the sale price</b><span>chegirmadan keyingi narx</span></li>
  <li><b>net change</b><span>yakuniy oʻzgarish</span></li>
  <li><b>compared with</b><span>… bilan solishtirganda</span></li>
  <li><b>marked up</b><span>narxi koʻtarilgan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Oʻzgarish har doim <b>eskisiga</b> boʻlinadi.</li>
    <li>Ketma-ket oʻzgarishlar <b>koʻpaytiriladi</b>, qoʻshilmaydi.</li>
    <li><b>«By»</b> oʻzgarishni, <b>«to»</b> yangi qiymatni bildiradi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-53 — tables, graphs and bar charts
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-53: Interpreting Tables, Graphs, and Bar Charts",
        "category": "math",
        "order": 53,
        "summary": (
            "Bu darsda hisoblash deyarli yoʻq. Butun ish — oʻq nomlarini, "
            "birliklarni va savolning oxirgi jumlasini toʻgʻri oʻqish."
        ),
        "stories": ["The Chart on the Wall"],
        "content": """
<h2>SAT-53: Interpreting Tables, Graphs, and Bar Charts</h2>

<p>Bu Blok C ning eng sof darsi: <mark>matematika deyarli yoʻq, oʻqish esa
hammasi</mark>. Bu yerda ball yoʻqotgan oʻquvchi hisoblay olmagani uchun emas,
grafikning oʻqiga yoki savolning oxirgi jumlasiga eʼtibor bermagani uchun
yoʻqotadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>grafikni oʻqishdan oldin uchta narsani tekshirasiz;</li>
    <li>ikki tomonlama jadvaldan qism va jamini olasiz;</li>
    <li>ustunli diagrammadan farq va nisbatni oʻqiysiz;</li>
    <li>savol qaysi ustunni yoki qaysi qatorni soʻrayotganini belgilaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Before you read anything</span>
  <span class="pe-chip pe-chip--v">oʻq nomlari</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">birliklar</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">shkala</span>
</div>

<h3>Uchta tekshiruv</h3>

<p><b>Oʻq nomlari.</b> Gorizontal oʻq nimani sanaydi — yilnimi, kategoriyanimi?
<b>Birliklar.</b> «Sales (thousands)» degan yozuv bor boʻlsa, ustun balandligi
40 emas, 40,000 degani. <b>Shkala.</b> Vertikal oʻq har doim ham noldan
boshlanmaydi, va shu sababli ikki ustun orasidagi farq koʻzga aslidagidan
kattaroq koʻrinadi.</p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Nolldan boshlanmaydigan shkala — diagrammadagi eng keng tarqalgan chalgʻituvchi
  narsa. Ikki ustun balandligi ikki barobar farq qilsa ham, sonlar 95 va 100
  boʻlishi mumkin. <b>Sonni oʻqing, balandlikni emas.</b>
</div>

<figure class="pm-fig">
  <svg viewBox="0 0 320 220" role="img"
       aria-label="Bar chart of books borrowed: Monday 30, Tuesday 45,
                   Wednesday 25, Thursday 50, Friday 40">
    <line class="pm-ln" x1="40" y1="180" x2="300" y2="180"/>
    <line class="pm-ln" x1="40" y1="20" x2="40" y2="180"/>
    <rect class="pm-fill" x="56"  y="90"  width="32" height="90"/>
    <rect class="pm-fill" x="104" y="45"  width="32" height="135"/>
    <rect class="pm-fill" x="152" y="105" width="32" height="75"/>
    <rect class="pm-fill" x="200" y="30"  width="32" height="150"/>
    <rect class="pm-fill" x="248" y="60"  width="32" height="120"/>
    <text class="pm-lbl" x="60"  y="196">Mon</text>
    <text class="pm-lbl" x="108" y="196">Tue</text>
    <text class="pm-lbl" x="156" y="196">Wed</text>
    <text class="pm-lbl" x="204" y="196">Thu</text>
    <text class="pm-lbl" x="252" y="196">Fri</text>
    <text class="pm-lbl" x="62"  y="84">30</text>
    <text class="pm-lbl" x="110" y="39">45</text>
    <text class="pm-lbl" x="158" y="99">25</text>
    <text class="pm-lbl" x="206" y="24">50</text>
    <text class="pm-lbl" x="254" y="54">40</text>
    <text class="pm-lbl" x="4" y="100">books</text>
  </svg>
  <figcaption>Books borrowed from a school library, Monday to Friday.
  Jami 190 ta kitob.</figcaption>
</figure>

<p>Bu diagrammadan uch xil savol chiqadi: <b>qiymat</b> (payshanbada nechta?),
<b>farq</b> (payshanba seshanbadan nechtaga koʻp?) va <b>ulush</b> (jamining
necha foizi juma kuni?).</p>

<h3>Ikki tomonlama jadval</h3>

<p>Ikki tomonlama jadval har bir katakda <b>ikkita shart</b> bajarilgan
sonni beradi. Yigʻindilarni chetga yozib qoʻying — savollarning yarmi
aynan ular haqida boʻladi.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th></th><th>Walk</th><th>Bus</th><th>Total</th></tr>
  <tr><td>Grade 9</td><td>24</td><td>16</td><td class="pm-word__sym">40</td></tr>
  <tr><td>Grade 10</td><td>18</td><td>22</td><td class="pm-word__sym">40</td></tr>
  <tr><td>Total</td><td class="pm-word__sym">42</td><td class="pm-word__sym">38</td>
      <td class="pm-word__sym">80</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Jadval savolining butun qiyinligi <b>maxrajda</b>: «9-sinfning necha foizi
  piyoda yuradi?» — 24 ÷ 40. «Piyoda yuradiganlarning necha foizi 9-sinf?» —
  24 ÷ 42. «Hammaning necha foizi 9-sinf va piyoda?» — 24 ÷ 80. Surat bir xil,
  javob uch xil.
</div>

<h3>Chiziqli grafik — qiymat va oʻzgarish</h3>

<p>Ustunli diagramma kategoriyalarni taqqoslaydi; chiziqli grafik esa
<b>vaqt boʻyicha oʻzgarishni</b> koʻrsatadi. Undan ikki xil savol chiqadi va
ular tez-tez aralashtiriladi.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Savol</th><th>Grafikda nimaga qarash kerak</th></tr>
  <tr><td>eng katta qiymat qaysi yilda?</td>
      <td class="pm-word__sym">eng baland nuqta</td></tr>
  <tr><td>eng katta oʻsish qaysi yilda?</td>
      <td class="pm-word__sym">eng tik koʻtarilgan qism</td></tr>
  <tr><td>qachon kamaydi?</td>
      <td class="pm-word__sym">pastga ketgan har qanday qism</td></tr>
</table></div>

<p>Chiziq pastga ketayotgan boʻlsa ham, qiymat hali katta boʻlishi mumkin —
kamayish va kichiklik bir xil narsa emas. Shuningdek, chiziq koʻtarilishdan
toʻxtasa, bu qiymat tushdi degani emas: u shunchaki oʻsishdan toʻxtagan.</p>

<h3>Jadvaldan bir necha qadamli savol</h3>

<p>Blok C ning eng qimmatli savollari ikki bosqichli boʻladi: jadvaldan son
oling, keyin u bilan biror amal bajaring. Yuqoridagi jadvaldan misol: «Agar
har bir avtobusda 30 oʻrin boʻlsa, 10-sinf oʻquvchilari uchun nechta avtobus
kerak?» Jadvaldan 22 ni olamiz, va 22 &lt; 30 boʻlgani uchun javob bitta
avtobus.</p>

<p>Bunday savolda ikkita xato yashiringan: notoʻgʻri katakni olish va
javobni yaxlitlashni unutish. Oʻrin soni yetmasa, javob har doim
<b>yuqoriga</b> yaxlitlanadi — 31 oʻquvchi uchun ikkita avtobus kerak,
1.03 ta emas.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>according to the graph</b><span>grafikka koʻra</span></li>
  <li><b>how many more … than …</b><span>… dan nechtaga koʻp (farq)</span></li>
  <li><b>what fraction of</b><span>… ning qanday ulushi</span></li>
  <li><b>of those who walk</b><span>piyoda yuradiganlar orasida — maxraj oʻzgardi</span></li>
  <li><b>the greatest increase</b><span>eng katta oʻsish (farq, qiymat emas)</span></li>
  <li><b>in thousands</b><span>ming hisobida</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>According to the bar chart, how many more books were borrowed on Thursday
    than on Wednesday?</p>
  </div>
  <ol class="ps-ch">
    <li>25</li>
    <li>50</li>
    <li>75</li>
    <li>2</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 25</p>
      <p>50 − 25 = 25.</p>
      <p><b>50</b> — payshanbaning qiymati. «How many more» farqni
      soʻraydi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">50</span>
  <span class="ps-trap__why">Grafikdan bitta son shundoq koʻchirilgan. Blok C
  da eng koʻp yoʻqotiladigan ball shu: toʻgʻri oʻqib, notoʻgʻri savolga javob
  berish.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">70 s</span></p>
  <div class="ps-stem__q">
    <p>Using the two-way table, what percent of the students who walk are in
    Grade 9?</p>
  </div>
  <ol class="ps-ch">
    <li>About 57%</li>
    <li>60%</li>
    <li>30%</li>
    <li>About 53%</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) About 57%</p>
      <p>24 ÷ 42 ≈ 0.571. Maxraj — piyoda yuradiganlar soni, 42.</p>
      <p><b>60%</b> — 24 ÷ 40 hisoblangan, yaʼni 9-sinfning ulushi. Savol
      teskari tomondan soʻragan.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">60%</span>
  <span class="ps-trap__why">Maxraj almashtirilgan: 40 (9-sinf) oʻrniga 42
  (piyodalar) turishi kerak edi. «Of the students who walk» iborasi maxrajni
  belgilaydi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Grafik yoki jadval savolida shu tartibda ishlang:</p>
  <ol>
    <li>Savolni <b>oxirigacha</b> oʻqing va soʻralayotgan narsani belgilang;</li>
    <li>Maxrajni aniqlang — «of» dan keyingi guruh;</li>
    <li>Sonlarni oʻqing (balandlikni emas) va hisoblang.</li>
  </ol>
  <p>Grafikka birinchi qarashda emas, <b>savolni oʻqigandan keyin</b> qarang —
  shunda koʻzingiz kerakli qatorni izlaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">«How many more on Thursday than Wednesday» → 50</p>
  <p class="pe-good">25</p>
  <p class="pe-fix__why">«More than» — ayirish soʻzi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">«What percent of those who walk are in Grade 9» → 24 ÷ 40</p>
  <p class="pe-good">24 ÷ 42</p>
  <p class="pe-fix__why">Maxrajda «of» dan keyingi guruh turadi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Chiziqli grafikda <b>eng tik qism</b> eng katta oʻzgarishni koʻrsatadi, eng
  baland nuqta esa eng katta qiymatni. «The greatest increase» va «the greatest
  value» — ikki boshqa savol, va ular koʻpincha bir xil yilga toʻgʻri
  kelmaydi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Jadvalning chekka yigʻindilarini <b>oʻzingiz hisoblab</b> yozib qoʻying, agar
  ular berilmagan boʻlsa. Bu 15 soniyalik ish va keyingi uch savolni ochib
  beradi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  From the bar chart, how many books were borrowed on Tuesday?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">45.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  What fraction of the week's books were borrowed on Friday?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">40 ÷ 190, taxminan 21 foiz.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  From the two-way table, how many Grade 10 students take the bus?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">22.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  What percent of all 80 students are Grade 10 students who walk?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">22.5% — 18 ÷ 80.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  What percent of bus riders are in Grade 9?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">About 42% — 16 ÷ 38.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>according to the graph</b><span>grafikka koʻra</span></li>
  <li><b>bar chart</b><span>ustunli diagramma</span></li>
  <li><b>two-way table</b><span>ikki tomonlama jadval</span></li>
  <li><b>horizontal / vertical axis</b><span>gorizontal / vertikal oʻq</span></li>
  <li><b>scale</b><span>shkala, boʻlinish</span></li>
  <li><b>in thousands</b><span>ming hisobida</span></li>
  <li><b>how many more</b><span>nechtaga koʻp</span></li>
  <li><b>what fraction of</b><span>… ning qanday ulushi</span></li>
  <li><b>the greatest increase</b><span>eng katta oʻsish</span></li>
  <li><b>total</b><span>jami</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Oʻqishdan oldin <b>oʻq nomlari, birliklar va shkala</b>ni
        tekshiring.</li>
    <li>Jadval savolining qiyinligi <b>maxrajda</b> — «of» dan keyingi
        guruh.</li>
    <li>«How many more» — <b>farq</b>, bitta ustunning qiymati emas.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-54 — scatterplots
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-54: Scatterplots — Lines of Best Fit and Trends",
        "category": "math",
        "order": 54,
        "summary": (
            "Eng mos chiziqning qiyaligi va kesishishi kontekstda maʼnoga ega. "
            "Va bogʻliqlik hech qachon sababni isbotlamaydi."
        ),
        "stories": ["Breakfast and the Third Thing"],
        "content": """
<h2>SAT-54: Scatterplots — Lines of Best Fit and Trends</h2>

<p>Sochilma diagramma ikki oʻlchov orasidagi bogʻliqlikni koʻrsatadi, va SAT
undan uch narsani soʻraydi: <mark>bogʻliqlik qanday, chiziq nima deydi va bitta
nuqta chiziqdan qancha uzoq</mark>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>musbat, manfiy va bogʻliqliksiz holatlarni ajratasiz;</li>
    <li>qiyalik va kesishishni <b>kontekst tilida</b> tushuntirasiz;</li>
    <li>bashorat qilasiz va qoldiqni hisoblaysiz;</li>
    <li>bogʻliqlikni sabab deb aytmaysiz.</li>
  </ul>
</div>

<figure class="pm-fig">
  <svg viewBox="0 0 320 220" role="img"
       aria-label="Scatterplot of study hours against test score, with a rising
                   line of best fit">
    <line class="pm-ln" x1="40" y1="180" x2="300" y2="180"/>
    <line class="pm-ln" x1="40" y1="20" x2="40" y2="180"/>
    <line class="pm-ln" x1="40" y1="160" x2="300" y2="40" stroke-dasharray="5 4"/>
    <circle cx="70"  cy="150" r="4"/>
    <circle cx="100" cy="140" r="4"/>
    <circle cx="120" cy="120" r="4"/>
    <circle cx="150" cy="118" r="4"/>
    <circle cx="175" cy="95"  r="4"/>
    <circle cx="200" cy="100" r="4"/>
    <circle cx="225" cy="70"  r="4"/>
    <circle cx="255" cy="62"  r="4"/>
    <circle cx="280" cy="45"  r="4"/>
    <circle cx="150" cy="70"  r="4"/>
    <text class="pm-lbl" x="118" y="64">far above the line</text>
    <text class="pm-lbl" x="150" y="200">hours studied</text>
    <text class="pm-lbl" x="2"   y="100">score</text>
  </svg>
  <figcaption>Har bir nuqta bitta oʻquvchi. Uzuq chiziq — eng mos chiziq;
  undan yuqoridagi nuqta bashoratdan koʻproq ball olgan.</figcaption>
</figure>

<h3>Bogʻliqlikning uch turi</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Rasm</th><th>Nomi</th><th>Maʼnosi</th></tr>
  <tr><td>nuqtalar yuqoriga ketadi</td><td class="pm-word__sym">positive</td>
      <td>biri oshsa, ikkinchisi ham oshadi</td></tr>
  <tr><td>nuqtalar pastga ketadi</td><td class="pm-word__sym">negative</td>
      <td>biri oshsa, ikkinchisi kamayadi</td></tr>
  <tr><td>nuqtalar tarqoq</td><td class="pm-word__sym">no association</td>
      <td>hech qanday yoʻnalish yoʻq</td></tr>
</table></div>

<h3>Qiyalik va kesishish — kontekstda</h3>

<p>Aytaylik eng mos chiziq <b>score = 3 × hours + 20</b>. SAT bu ikki sonning
maʼnosini soʻraydi, va javob har doim birlik bilan aytiladi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Qiyalik 3</span>
    <span class="pm-solve__why">Har qoʻshimcha soat uchun ball 3 taga oshadi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Kesishish 20</span>
    <span class="pm-solve__why">Umuman oʻqimagan oʻquvchining bashorat qilingan bali</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">10 soat → 3(10) + 20 = 50</span>
    <span class="pm-solve__why">Bu <b>bashorat</b>, haqiqiy ball emas</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qiyalikning maʼnosini aytishda <b>ikkala birlikni ham</b> qoʻshing: «har
  qoʻshimcha <u>soat</u> uchun <u>ball</u> uchtaga oshadi». Faqat «3 ga oshadi»
  deyish javobni chala qiladi va SAT variantlarida shunday chala javob
  turadi.
</div>

<h3>Qoldiq — nuqta chiziqdan qancha uzoq</h3>

<p>Bir oʻquvchi 10 soat oʻqib 56 ball olgan boʻlsa, chiziq 50 ni bashorat
qilgan edi. Farqi <b>+6</b> — bu qoldiq. Musbat qoldiq nuqta chiziqdan
<u>yuqorida</u> ekanini bildiradi.</p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Qoldiq — <b>haqiqiy minus bashorat</b>, teskarisi emas. Ishorani almashtirsangiz
  javob toʻgʻri son, notoʻgʻri belgi bilan chiqadi — va u variantlar orasida
  albatta turadi.
</div>

<h3>Bogʻliqlik sabab emas</h3>

<p>Bu SAT'ning eng sevimli interpretatsiya savoli. Ikki narsa birga oʻzgarishi
ularning biri ikkinchisini <u>keltirib chiqaradi</u> degani emas. Yozda
muzqaymoq savdosi ham, suvda choʻkish hodisalari ham oshadi — sababi
muzqaymoq emas, issiq havo.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  «Which conclusion is supported by the data?» degan savolda <b>sabab
  bildiradigan feʼllarni</b> qidiring: <em>causes</em>, <em>leads to</em>,
  <em>makes</em>. Bunday variant deyarli har doim notoʻgʻri. Toʻgʻri javob
  odatda <em>is associated with</em> yoki <em>tends to</em> deb yozilgan
  boʻladi.
</div>

<h3>Bogʻliqlikning kuchi</h3>

<p>Nuqtalar chiziq atrofida qanchalik zich toʻplansa, bogʻliqlik shunchalik
kuchli — va bashorat shunchalik ishonchli. Tarqoq nuqtalarda esa chiziq
mavjud boʻlsa ham, undan olingan bashorat kam maʼnoga ega.</p>

<p>SAT buni odatda soʻz bilan soʻraydi: «which scatterplot shows the strongest
association?» Javob eng tik chiziqli emas, <b>eng zich</b> tarqalgan grafik
boʻladi. Qiyalikning kattaligi bogʻliqlikning kuchi haqida hech narsa
aytmaydi — u faqat oʻzgarish tezligini koʻrsatadi.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>line of best fit</b><span>eng mos chiziq</span></li>
  <li><b>positive association</b><span>musbat bogʻliqlik</span></li>
  <li><b>what does the slope represent</b><span>qiyalik nimani anglatadi</span></li>
  <li><b>predicted value</b><span>bashorat qilingan qiymat</span></li>
  <li><b>is associated with</b><span>… bilan bogʻliq (sabab emas)</span></li>
  <li><b>the data support the conclusion that</b><span>maʼlumotlar shu xulosani tasdiqlaydi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>A line of best fit is given by <i>score</i> = 3(<i>hours</i>) + 20. What
    does the number 3 represent?</p>
  </div>
  <ol class="ps-ch">
    <li>The predicted increase in score for each additional hour studied</li>
    <li>The score of a student who studies no hours</li>
    <li>The number of students in the study</li>
    <li>The total increase in score</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A</p>
      <p>Qiyalik — bir birlik kirishga toʻgʻri keladigan oʻzgarish, va ikkala
      birlik ham javobda turishi kerak.</p>
      <p><b>B</b> — bu kesishish, yaʼni 20.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">The score of a student who studies no hours</span>
  <span class="ps-trap__why">Qiyalik va kesishish almashtirilgan. Qiyalik
  <b>oʻzgarish</b> haqida, kesishish esa <b>boshlangʻich</b> qiymat
  haqida.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">70 s</span></p>
  <div class="ps-stem__q">
    <p>Using that line, a student who studied 10 hours actually scored 56. What
    is the residual for that student?</p>
  </div>
  <ol class="ps-ch">
    <li>6</li>
    <li>−6</li>
    <li>50</li>
    <li>56</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 6</p>
      <p>Bashorat 3(10) + 20 = 50, haqiqiy 56, demak qoldiq 56 − 50 = 6.</p>
      <p>Musbat qoldiq — nuqta chiziqdan yuqorida.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">−6</span>
  <span class="ps-trap__why">Ayirish teskari tomonga qilingan: bashoratdan
  haqiqiy ayirilgan. Qoldiq — <b>haqiqiy minus bashorat</b>.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Xulosa savolida javoblarni <b>feʼliga qarab</b> saralang:</p>
  <ol>
    <li><em>causes</em>, <em>proves</em>, <em>guarantees</em> — deyarli har doim
        notoʻgʻri;</li>
    <li><em>is associated with</em>, <em>tends to</em>, <em>on average</em> —
        odatda toʻgʻri;</li>
    <li>Maʼlumot chegarasidan tashqaridagi bashorat ham shubhali.</li>
  </ol>
  <p>Bu saralash matematikasiz ishlaydi va Blok C da bir necha ball
  qutqaradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Qoldiq = bashorat − haqiqiy</p>
  <p class="pe-good">haqiqiy − bashorat</p>
  <p class="pe-fix__why">Nuqta chiziqdan yuqorida boʻlsa qoldiq musbat
  boʻlishi kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Koʻproq oʻqish yuqori ball keltirib chiqaradi</p>
  <p class="pe-good">Koʻproq oʻqish yuqori ball bilan bogʻliq</p>
  <p class="pe-fix__why">Sochilma diagramma sababni koʻrsata olmaydi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Eng mos chiziq <b>maʼlumot toʻplangan oraliqda</b> ishonchli. Diagrammada
  eng koʻpi 12 soat boʻlsa, 40 soat uchun bashorat qilish — chiziqni bilmagan
  joyiga choʻzish demakdir. SAT bunday variantni ham qoʻyadi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Nuqtalar chiziq atrofida qanchalik zich boʻlsa, bogʻliqlik shunchalik kuchli.
  Lekin «kuchli bogʻliqlik» ham sababni isbotlamaydi — u faqat bashoratni
  aniqroq qiladi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  As temperature rises, heating costs fall. What type of association is this?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Manfiy bogʻliqlik.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  For <i>cost</i> = 5(<i>items</i>) + 30, what does 30 represent?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Hech qanday buyum olinmaganda ham toʻlanadigan
  boshlangʻich haq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Using <i>score</i> = 3(<i>hours</i>) + 20, what is the predicted score for
  6 hours?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">38.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  A student studied 6 hours and scored 35. What is the residual?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">−3 — 35 − 38. Nuqta chiziqdan pastda.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Ice cream sales and sunburn cases both rise in summer. What can we conclude?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ular bogʻliq, lekin biri ikkinchisining sababi emas —
  ikkalasining sababi issiq havo.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>scatterplot</b><span>sochilma diagramma</span></li>
  <li><b>line of best fit</b><span>eng mos chiziq</span></li>
  <li><b>positive / negative association</b><span>musbat / manfiy bogʻliqlik</span></li>
  <li><b>residual</b><span>qoldiq (haqiqiy minus bashorat)</span></li>
  <li><b>predicted value</b><span>bashorat qilingan qiymat</span></li>
  <li><b>is associated with</b><span>… bilan bogʻliq</span></li>
  <li><b>causation</b><span>sababiylik</span></li>
  <li><b>outlier</b><span>chetdagi nuqta</span></li>
  <li><b>on average</b><span>oʻrtacha hisobda</span></li>
  <li><b>supported by the data</b><span>maʼlumotlar bilan tasdiqlangan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Qiyalikni <b>ikkala birlik bilan</b> tushuntiring; kesishish —
        boshlangʻich qiymat.</li>
    <li>Qoldiq = <b>haqiqiy − bashorat</b>; musbat boʻlsa nuqta chiziq
        ustida.</li>
    <li><b>Bogʻliqlik sabab emas</b> — «causes» degan variantdan
        ehtiyot boʻling.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-55 — mean and median
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-55: Descriptive Statistics — Mean and Median",
        "category": "math",
        "order": 55,
        "summary": (
            "Oʻrta arifmetik hamma sonni his qiladi, mediana esa faqat tartibni. "
            "Shuning uchun chetdagi bitta qiymat birinchisini tortadi."
        ),
        "stories": ["The Average Nobody Is In"],
        "content": """
<h2>SAT-55: Descriptive Statistics — Mean and Median</h2>

<p>Ikkala son ham «oʻrtacha» deb tarjima qilinadi, lekin ular boshqa savolga
javob beradi. <mark>Oʻrta arifmetik har bir qiymatni hisobga oladi; mediana
faqat oʻrtada turgan qiymatga qaraydi</mark> — va bu farq butun mavzuni hal
qiladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>ikkalasini toʻgʻri hisoblaysiz (mediana uchun avval tartiblaysiz);</li>
    <li>chetdagi qiymat qaysinisini tortishini aytasiz;</li>
    <li>qaysi biri vaziyatni yaxshiroq ifodalashini tanlaysiz;</li>
    <li>yigʻindi orqali teskari savollarni yechasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Two averages</span>
  <span class="pe-chip pe-chip--v">mean = yigʻindi ÷ soni</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">median = oʻrtadagi qiymat</span>
</div>

<h3>Hisoblash</h3>

<p>Maʼlumot: 4, 7, 7, 9, 13. Yigʻindi 40, soni 5, demak oʻrta arifmetik 8.
Tartiblangan qatorda oʻrtadagi son — uchinchisi, yaʼni 7.</p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Mediana topishdan oldin sonlarni <b>albatta tartiblang</b>. SAT maʼlumotni
  ataylab aralash beradi, va tartiblamasdan oʻrtadagi sonni olish eng koʻp
  uchraydigan xato. Sonlar juft boʻlsa, oʻrtadagi ikkitasining oʻrta arifmetigi
  olinadi.
</div>

<h3>Chetdagi qiymat nima qiladi</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Maʼlumot</th><th>Mean</th><th>Median</th></tr>
  <tr><td>2, 3, 4, 5, 6</td><td class="pm-word__sym">4</td><td>4</td></tr>
  <tr><td>2, 3, 4, 5, 100</td><td class="pm-word__sym">22.8</td><td>4</td></tr>
</table></div>

<p>Bitta sonni 6 dan 100 ga oʻzgartirdik. Oʻrta arifmetik 4 dan 22.8 ga
sakradi; mediana <b>umuman qimirlamadi</b>. Sabab oddiy: mediana faqat
oʻrtadagi qiymat qayerda turganini biladi, sonning kattaligini emas.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Shuning uchun maosh, uy narxi va shunga oʻxshash maʼlumotlarda
  <b>mediana</b> ishlatiladi. Bir nechta juda katta qiymat oʻrta arifmetikni
  koʻtarib yuboradi va «oʻrtacha» son hech kimga toʻgʻri kelmay qoladi.
</div>

<h3>Teskari savol — yigʻindi orqali</h3>

<p>SAT koʻpincha oʻrtachani berib, yetishmayotgan qiymatni soʻraydi. Kalit
bitta: <b>oʻrta arifmetik × soni = yigʻindi</b>.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Beshta sonning oʻrtachasi 12</span>
    <span class="pm-solve__why">Demak yigʻindisi 60</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Toʻrttasi maʼlum: 8, 10, 15, 12 — yigʻindisi 45</span>
    <span class="pm-solve__why">Qolgani 60 − 45</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Beshinchi son 15</span>
    <span class="pm-solve__why">Tekshiruv: 60 ÷ 5 = 12 ✓</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  «Yangi qiymat qoʻshilganda oʻrtacha qanday oʻzgaradi?» degan savolda
  yigʻindini yangilang, keyin yangi songa boʻling. Yangi qiymat eski
  oʻrtachadan katta boʻlsa, oʻrtacha oshadi; kichik boʻlsa tushadi; teng boʻlsa
  oʻzgarmaydi.
</div>

<h3>Chastota jadvalidan oʻrtacha</h3>

<p>Maʼlumot roʻyxat emas, jadval koʻrinishida berilishi mumkin: qiymat va u
necha marta uchragani. Bunda har bir qiymatni <b>chastotasiga koʻpaytirib</b>
qoʻshasiz.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Bolalar soni</th><th>Oilalar soni</th><th>Hissa</th></tr>
  <tr><td>1</td><td>4</td><td class="pm-word__sym">4</td></tr>
  <tr><td>2</td><td>6</td><td class="pm-word__sym">12</td></tr>
  <tr><td>3</td><td>2</td><td class="pm-word__sym">6</td></tr>
</table></div>

<p>Jami 12 oila va 22 bola, demak oʻrtacha 22 ÷ 12 ≈ 1.83. Mediana esa 12 ta
qiymatning oʻrtasi — 6 va 7-oʻrindagi qiymatlar, ikkalasi ham 2.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>the mean (arithmetic mean)</b><span>oʻrta arifmetik</span></li>
  <li><b>the median</b><span>mediana</span></li>
  <li><b>which measure better represents</b><span>qaysi oʻlchov yaxshiroq ifodalaydi</span></li>
  <li><b>an outlier</b><span>chetdagi qiymat</span></li>
  <li><b>skewed by</b><span>… tomonidan qiyshaytirilgan</span></li>
  <li><b>remains unchanged</b><span>oʻzgarishsiz qoladi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>What is the median of the data set 9, 3, 7, 15, 5?</p>
  </div>
  <ol class="ps-ch">
    <li>7</li>
    <li>7.8</li>
    <li>9</li>
    <li>5</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 7</p>
      <p>Tartiblang: 3, 5, 7, 9, 15. Oʻrtadagi son 7.</p>
      <p><b>7.8</b> — oʻrta arifmetik (39 ÷ 5). <b>9</b> — tartiblamasdan
      oʻrtadan olingan son.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">9</span>
  <span class="ps-trap__why">Berilgan qatorning oʻrtasidagi son olingan,
  tartiblanmagan holda. Mediana faqat <b>tartiblangan</b> qatorda maʼnoga
  ega.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">65 s</span></p>
  <div class="ps-stem__q">
    <p>Nine workers earn between 4 and 6 million som a month. The owner earns
    60 million. Which measure better represents a typical worker's pay?</p>
  </div>
  <ol class="ps-ch">
    <li>The median, because the owner's pay is an outlier</li>
    <li>The mean, because it uses every value</li>
    <li>The mean, because there are ten people</li>
    <li>Neither can be used</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) The median</p>
      <p>Bitta juda katta qiymat oʻrta arifmetikni koʻtarib yuboradi va u hech
      bir ishchining maoshiga oʻxshamay qoladi.</p>
      <p><b>«uses every value»</b> — bu rost, lekin aynan shu sababdan u bu
      yerda yaroqsiz.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">The mean, because it uses every value</span>
  <span class="ps-trap__why">Sababi toʻgʻri aytilgan, xulosasi notoʻgʻri.
  Chetdagi qiymat borligida «hamma sonni hisobga olish» — kamchilik,
  afzallik emas.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Oʻrtacha savolida uchta savol bering:</p>
  <ol>
    <li>Maʼlumotda <b>chetdagi qiymat</b> bormi? Boʻlsa — mediana;</li>
    <li>Yetishmayotgan qiymat soʻralyaptimi? — <b>yigʻindi</b> orqali
        ishlang;</li>
    <li>Mediana soʻralganmi? — avval <b>tartiblang</b>.</li>
  </ol>
  <p>Bu uch tekshiruv Blok C ning statistika savollarining koʻpini
  qamrab oladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">9, 3, 7, 15, 5 → mediana 7 (tartiblanmagan holda oʻrtadagi)</p>
  <p class="pe-good">Avval tartiblang: 3, 5, 7, 9, 15 — mediana 7</p>
  <p class="pe-fix__why">Bu safar javob toʻgʻri chiqdi, lekin usul notoʻgʻri:
  boshqa qatorda u xato beradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Beshta sonning oʻrtachasi 12 → yigʻindi 12</p>
  <p class="pe-good">Yigʻindi 60</p>
  <p class="pe-fix__why">Oʻrtacha × soni = yigʻindi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Sonlar soni <b>juft</b> boʻlsa mediana oʻrtadagi ikkitasining oʻrtasi boʻladi
  va u <u>roʻyxatda boʻlmasligi</u> mumkin: 4, 6, 8, 10 uchun mediana 7.
  Bu SAT'da tez-tez uchraydi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Chetdagi qiymat medianani <b>butunlay qimirlatmaydi</b> deb aytish
  notoʻgʻri boʻlardi: u medianani bir pogʻona surishi mumkin. Toʻgʻri gap —
  mediana chetdagi qiymatning <b>kattaligiga</b> sezgir emas.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  What is the mean of 4, 7, 7, 9, 13?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">8 — 40 ÷ 5.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  What is the median of 4, 6, 8, 10?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">7 — oʻrtadagi ikkitasining oʻrtasi. U roʻyxatda
  yoʻq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  The mean of 6 numbers is 10. What is their sum?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">60.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Four numbers have a mean of 20. Three of them are 15, 18 and 25. What is the
  fourth?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">22 — yigʻindi 80, maʼlumlari 58.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A value of 200 is added to the set 2, 3, 4, 5, 6. Which changes more, the mean
  or the median?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Oʻrta arifmetik — 4 dan 36.67 ga; mediana esa 4 dan
  4.5 ga.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>mean / arithmetic mean</b><span>oʻrta arifmetik</span></li>
  <li><b>median</b><span>mediana</span></li>
  <li><b>data set</b><span>maʼlumotlar toʻplami</span></li>
  <li><b>outlier</b><span>chetdagi qiymat</span></li>
  <li><b>in ascending order</b><span>oʻsish tartibida</span></li>
  <li><b>typical value</b><span>tipik qiymat</span></li>
  <li><b>better represents</b><span>yaxshiroq ifodalaydi</span></li>
  <li><b>the sum of the values</b><span>qiymatlar yigʻindisi</span></li>
  <li><b>remains unchanged</b><span>oʻzgarishsiz qoladi</span></li>
  <li><b>skewed</b><span>qiyshaygan, bir tomonga tortilgan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Mediana uchun avval tartiblang</b>; juft sonda oʻrtadagi
        ikkitasining oʻrtasi.</li>
    <li>Chetdagi qiymat <b>oʻrta arifmetikni tortadi</b>, medianani deyarli
        yoʻq.</li>
    <li>Yetishmayotgan qiymat savollarida <b>yigʻindi</b> orqali ishlang.</li>
  </ul>
</div>
""",
    },
]
