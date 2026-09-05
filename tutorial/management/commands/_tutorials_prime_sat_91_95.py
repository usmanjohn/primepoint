# -*- coding: utf-8 -*-
"""Prime SAT Math — lessons 91–95 (Blok E: tarjima, tuzilma, chekka qiymatlar).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_SAT.md
Lesson list: tutorial/management/commands/toc_prime_sat_math.txt

⚠️ SARLAVHALAR BAZADAN OLINGAN, aynan.

⚠️ BLOK E QOIDASI: matematika oʻrgatilmaydi — usul oʻrgatiladi, va har
   bir darsda usul QACHON ishlamasligi aytiladi.

⚠️ SAT-91 — BUTUN KURSNING TEZISI. Kurs shu daʼvo ustiga qurilgan:
   oʻzbek oʻquvchisining SAT muammosi matematika emas, matematikani
   oʻrab turgan inglizcha jumla. Shuning uchun bu dars eng katta
   lugʻat jadvalini olib yuradi va uni ps-phrase emas, pe-table
   qiladi (chunki u yodlanadigan roʻyxat, oʻqiladigan izoh emas).

⚠️ SAT-93 SAT-81 GA QARSHI TURADI, va bu ataylab:
     «which expression is equivalent» → 0 va 1 dan QOCHING (SAT-81);
     «which must be true»            → 0, 1, manfiy, kasrni QOʻYING.
   Ikkala darsda ham bu farq ochiq aytilgan.

⚠️ Ismlar — foydalanuvchining oʻz oʻquvchilari (memory: pupil-names).

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_sat_91_95.py \\
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
    # SAT-91 — the dictionary (the course's thesis)
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-91: Translating English into Math (Key Terms Dictionary)",
        "category": "math",
        "order": 91,
        "summary": (
            "Bu kursning eng muhim darsi: SAT savolining qiyinligi "
            "matematikada emas, jumlada. Mana oʻsha jumlaning lugʻati."
        ),
        "stories":  ["The Comma That Was Worth Five Million"],
        "content": """
<h2>SAT-91: Translating English into Math (Key Terms Dictionary)</h2>

<p>Toʻqson dars oʻtdi va endi kursning asosiy daʼvosini ochiq aytish
mumkin: <mark>siz bu testda matematikadan emas, inglizchadan
yiqilasiz</mark>. Tenglamani yecha olasiz. Uni <b>tuzish</b> —
inglizcha jumlani belgilarga oʻgirish — mana shu joyda ball
yoʻqoladi.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha — nega bu shunday</span>
  Amerikalik oʻquvchi «three less than twice a number» degan iborani
  oʻylab oʻtirmasdan tushunadi, chunki u shu tilda oʻsgan. Siz uni
  <b>tarjima qilasiz</b>, va tarjimada bitta ibora — aynan «less
  than» — teskari yoʻnalishda ishlaydi. Shuning uchun bu dars
  lugʻatdan iborat.
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>oltmishga yaqin SAT iborasini belgiga oʻgirasiz;</li>
    <li>ikkita <b>teskari</b> iborani xatosiz yozasiz;</li>
    <li>«of» va «is» ni koʻrgan zahoti tenglama tuzasiz;</li>
    <li>foiz savolining qaysi turi ekanini ajratasiz.</li>
  </ul>
</div>

<h3>Lugʻat — yodlanadigan qism</h3>

<table class="pe-table">
  <tr><th>Ingliz tilida</th><th>Belgi</th><th>Misol</th></tr>
  <tr><td>is · are · was · equals · the result is</td><td>=</td>
      <td>the result is 12 → … = 12</td></tr>
  <tr><td>of (kasr yoki foiz bilan)</td><td>×</td>
      <td>half of 20 → 20 ÷ 2</td></tr>
  <tr><td>sum · total · more than · increased by</td><td>+</td>
      <td>the sum of 5 and n → 5 + n</td></tr>
  <tr><td>difference · decreased by · minus</td><td>−</td>
      <td>the difference of 9 and 4 → 9 − 4</td></tr>
  <tr><td>product · times · twice · double</td><td>×</td>
      <td>twice a number → 2n</td></tr>
  <tr><td>quotient · per · for each · divided by</td><td>÷</td>
      <td>miles per hour → masofa ÷ vaqt</td></tr>
  <tr><td>at least</td><td>≥</td><td>at least 8 → ≥ 8</td></tr>
  <tr><td>at most · no more than</td><td>≤</td><td>at most 40 → ≤ 40</td></tr>
  <tr><td>what · a number</td><td>nomaʼlum</td><td>what percent → nomaʼlum foiz</td></tr>
  <tr><td>consecutive integers</td><td>n, n+1, n+2</td>
      <td>three consecutive → n, n+1, n+2</td></tr>
</table>

<h3>Ikkita teskari ibora — darsning eng qimmat qismi</h3>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Ingliz tilida ikkita ibora sonlarni <b>teskari tartibda</b> yozishga
  majbur qiladi. Ular SAT'da juda koʻp uchraydi va ularning tuzoq
  varianti har doim tayyor turadi.
</div>

<table class="pe-table">
  <tr><th>Ingliz tilida</th><th>Toʻgʻri</th><th>Tuzoq</th></tr>
  <tr><td>5 less than <i>x</i></td><td><i>x</i> − 5</td><td>5 − <i>x</i></td></tr>
  <tr><td>5 subtracted from <i>x</i></td><td><i>x</i> − 5</td><td>5 − <i>x</i></td></tr>
  <tr><td><i>x</i> subtracted from 5</td><td>5 − <i>x</i></td><td><i>x</i> − 5</td></tr>
  <tr><td>5 less <i>x</i></td><td>5 − <i>x</i></td><td><i>x</i> − 5</td></tr>
</table>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Qoidani bitta soʻz bilan eslang: <b>«than» — burilish belgisi</b>.
  «Less than» va «more than» dan keyin turgan narsa tenglamada
  <b>oldinga</b> chiqadi. «More than» da tartib muhim emas (qoʻshuv
  oʻrin almashtiradi), «less than» da esa hal qiluvchi.
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">"three less than twice a number"</span>
    <span class="pm-solve__why">Boʻlaklarga ajratamiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">"twice a number" → 2n</span>
    <span class="pm-solve__why">Bu asosiy qism</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">"three less than" u → 2n − 3</span>
    <span class="pm-solve__why">3 − 2n EMAS</span>
  </div>
</div>

<h3>Foizning uch turi</h3>

<p>SAT foizni uch xil savol qilib beradi va ularni chalkashtirish
oson. Farqi <b>qaysi son nomaʼlum</b> ekanida.</p>

<table class="pe-table">
  <tr><th>Savol</th><th>Nomaʼlum</th><th>Yoʻli</th></tr>
  <tr><td>What is 25% of 80?</td><td>natija</td><td>80 ÷ 4 = 20</td></tr>
  <tr><td>12 is 25% of what number?</td><td>butun</td><td>12 × 4 = 48</td></tr>
  <tr><td>12 is what percent of 48?</td><td>foiz</td><td>12 ÷ 48 = 25%</td></tr>
</table>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Uchalasida ham bir xil uchta son bor: 12, 25 va 48. Faqat qaysi biri
  yashiringani oʻzgaradi. Savolni oʻqiganda <b>«of» dan keyingi son
  butun</b>, <b>«is» oldidagi son qism</b> — shu ikkita joyni
  belgilasangiz, tur oʻz-oʻzidan aniqlanadi.
</div>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>Three less than twice a number is 11. What is the number?</p>
  </div>
  <ol class="ps-ch">
    <li>7</li>
    <li>−4</li>
    <li>4</li>
    <li>28</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 7</p>
      <p>Tarjima: 2n − 3 = 11, demak 2n = 14 va n = 7.</p>
      <p>Tekshiruv: 7 ning ikki barobari 14, undan uch kam — 11 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">−4</span>
  <span class="ps-trap__why">«Three less than» ni <b>3 − 2n</b> deb
  yozgan: 3 − 2n = 11 dan n = −4 chiqadi. Bu darsdagi birinchi
  teskari ibora — va SAT uni deyarli har testda ishlatadi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">55 s</span></p>
  <div class="ps-stem__q">
    <p>12 is 25 percent of what number?</p>
  </div>
  <ol class="ps-ch">
    <li>48</li>
    <li>3</li>
    <li>37</li>
    <li>300</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 48</p>
      <p>«of» dan keyingi son — butun, va u yerda «what number»
      turibdi, demak butun nomaʼlum. 12 — uning choragi, demak butun
      12 × 4 = 48.</p>
      <p>Tekshiruv: 48 ning 25 foizi 12 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">3</span>
  <span class="ps-trap__why">Savolni «what is 25 percent of 12» deb
  oʻqigan — yaʼni nomaʼlumni notoʻgʻri joyga qoʻygan. Javob butundan
  <b>kichik</b> chiqdi, holbuki 12 allaqachon qism edi: imkonsizlik
  nazorati (SAT-87) buni tutadi.</span>
</div>

<h3>Qachon lugʻat yetarli emas</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Uchta «yoʻq»</span>
  <ol>
    <li><b>«of» har doim koʻpaytirish emas.</b> «The length of the
        rectangle» — bu shunchaki egalik, amal emas.</li>
    <li><b>«per» baʼzan boʻlish emas.</b> «$5 per person» tenglamada
        koʻpaytiruvchi boʻlib turadi: 5 × odamlar soni.</li>
    <li><b>Uzun jumlani bitta oʻqishda tarjima qilmang.</b> Uni
        boʻlaklarga ajrating va har bir boʻlakni alohida yozing —
        SAT-94 shu haqda.</li>
  </ol>
</div>

<h3>Exam English — koʻp uchraydigan qoliplar</h3>

<ul class="ps-phrase">
  <li><b>a number</b><span>bir son — nomaʼlum kiritish belgisi</span></li>
  <li><b>is increased by 8</b><span>8 ga oshiriladi</span></li>
  <li><b>is 3 less than</b><span>… dan 3 kam (teskari!)</span></li>
  <li><b>the sum of a and b</b><span>a va b ning yigʻindisi</span></li>
  <li><b>what percent of</b><span>… ning necha foizi</span></li>
  <li><b>for every</b><span>har bir … uchun</span></li>
</ul>

<div class="pe-fix">
  <p class="pe-bad">"5 less than x" → 5 − x</p>
  <p class="pe-good">x − 5</p>
  <p class="pe-fix__why">«than» dan keyingi narsa oldinga chiqadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">"12 is 25% of what" → 12 × 0.25</p>
  <p class="pe-good">12 ÷ 0.25 = 48</p>
  <p class="pe-fix__why">Nomaʼlum «of» dan keyin, yaʼni butun.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha — bu lugʻatni qanday yodlash kerak</span>
  Yodlab oʻtirmang: <b>yozib boring</b>. Har bir mashqdan keyin
  tushunmagan iborangizni daftaringizning oxirgi sahifasiga koʻchiring
  va yoniga tarjimasini yozing. Ikki oyda oʻsha sahifa sizning shaxsiy
  lugʻatingiz boʻladi — va u har qanday tayyor roʻyxatdan foydaliroq,
  chunki unda aynan <b>sizni</b> toʻxtatgan iboralar turadi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Write "7 less than a number" in symbols.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">n − 7.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Write "the sum of a number and 4 is 19".</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">n + 4 = 19, demak n = 15.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  What is 40 percent of 65?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">26.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  9 is what percent of 36?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">9 ÷ 36 = 0.25, demak 25 foiz.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Write "four more than three times a number is 25".</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">3n + 4 = 25, demak n = 7.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>translate</b><span>oʻgirmoq, tarjima qilmoq</span></li>
  <li><b>expression</b><span>ifoda</span></li>
  <li><b>sum</b><span>yigʻindi</span></li>
  <li><b>difference</b><span>ayirma</span></li>
  <li><b>product</b><span>koʻpaytma</span></li>
  <li><b>quotient</b><span>boʻlinma</span></li>
  <li><b>less than</b><span>… dan kam (teskari yoziladi)</span></li>
  <li><b>subtracted from</b><span>… dan ayirilgan</span></li>
  <li><b>consecutive</b><span>ketma-ket</span></li>
  <li><b>what percent of</b><span>necha foizi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>«than» — burilish belgisi</b>: undan keyingisi oldinga
        chiqadi.</li>
    <li><b>«of» dan keyingi son — butun</b>, «is» oldidagisi — qism.</li>
    <li>Oʻz lugʻatingizni <b>yozib boring</b>; u tayyor roʻyxatdan
        foydaliroq.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-92 — structure
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-92: Recognizing Structure (Treating a Group as One Variable)",
        "category": "math",
        "order": 92,
        "summary": (
            "Baʼzi savollarda nomaʼlumni topish shart emas — butun bir "
            "boʻlakni bitta narsa deb qarash yetadi."
        ),
        "stories":  ["What the Chess Master Actually Sees"],
        "content": """
<h2>SAT-92: Recognizing Structure (Treating a Group as One Variable)</h2>

<p>SAT'ning eng chiroyli savollari shunday tuzilgan: ular
nomaʼlumni topishni <b>soʻramaydi</b>, lekin oʻquvchi odat boʻyicha
uni topishga tushadi va vaqtni yoʻqotadi.
<mark>Baʼzan qavs ichidagi butun boʻlak — bitta son</mark>, va uni
ochmaslik kerak.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>«nomaʼlumni topish shart emas» degan savolni taniysiz;</li>
    <li>takrorlangan boʻlakni bitta narsa deb belgilaysiz;</li>
    <li>kvadratlar ayirmasi va yigʻindining kvadratini
        tuzilma sifatida koʻrasiz;</li>
    <li>qavsni qachon ochmaslik kerakligini bilasiz.</li>
  </ul>
</div>

<h3>Belgisi: savolda boʻlakning oʻzi soʻralgan</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3(<i>m</i> + <i>n</i>) = 21 berilgan</span>
    <span class="pm-solve__why">m + n soʻralgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">m ni ham, n ni ham topib boʻlmaydi</span>
    <span class="pm-solve__why">Bitta tenglama, ikkita nomaʼlum</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Lekin m + n = 21 ÷ 3 = 7</span>
    <span class="pm-solve__why">Boʻlakning oʻzi bir qadamda chiqdi</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu savolda m va n ni topish <b>mumkin emas</b> — cheksiz koʻp juftlik
  toʻgʻri keladi (3 va 4, 10 va −3, 0.5 va 6.5). Oʻquvchi «yetarli
  maʼlumot yoʻq» deb oʻylab yuboradi. Aslida savol ularni soʻramagan
  ham — u faqat <b>yigʻindini</b> soʻragan, va yigʻindi bitta.
</div>

<h3>Uchta tanish tuzilma</h3>

<table class="pe-table">
  <tr><th>Koʻrsangiz</th><th>Yozing</th><th>Nima uchun foydali</th></tr>
  <tr><td>(<i>x</i> + <i>y</i>)²</td><td><i>x</i>² + 2<i>xy</i> + <i>y</i>²</td>
      <td>x² + y² va xy alohida berilgan boʻlishi mumkin</td></tr>
  <tr><td><i>a</i>² − <i>b</i>²</td><td>(<i>a</i> − <i>b</i>)(<i>a</i> + <i>b</i>)</td>
      <td>ayirma va yigʻindi alohida berilgan boʻladi</td></tr>
  <tr><td>takrorlangan qavs</td><td>uni bitta harf deb oling</td>
      <td>savol oddiy kvadrat tenglamaga aylanadi</td></tr>
</table>

<div class="pm-check">
  <p class="pm-check__t">Ikkinchi qatorning kuchi</p>
  <p><i>a</i> − <i>b</i> = 3 va <i>a</i> + <i>b</i> = 7 berilgan boʻlsa,
  <i>a</i>² − <i>b</i>² = 3 × 7 = 21. a va b topilmadi ham —
  aslida ular 5 va 2, lekin bu kerak boʻlmadi.</p>
</div>

<h3>Takrorlangan boʻlakni bitta harf qilish</h3>

<p>Agar bir xil qavs ifodada bir necha marta uchrasa, uni
<b>vaqtincha bitta narsa</b> deb belgilang. Ifoda darrov tanish
koʻrinishga tushadi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">(<i>x</i>+1)² + 3(<i>x</i>+1) − 4 = 0</span>
    <span class="pm-solve__why">Qoʻrqinchli koʻrinadi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(<i>x</i>+1) ni bitta narsa deb ataymiz</span>
    <span class="pm-solve__why">Uni <i>u</i> deylik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step"><i>u</i>² + 3<i>u</i> − 4 = 0</span>
    <span class="pm-solve__why">Oddiy kvadrat tenglama (SAT-35)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step"><i>u</i> = 1 yoki <i>u</i> = −4</span>
    <span class="pm-solve__why">Demak x = 0 yoki x = −5</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Oxirgi qadamni unutmang. <i>u</i> topildi — lekin savol <b>x</b> ni
  soʻragan. Bu SAT-89 dagi <b>ikkinchi tur</b> tuzoq: yarim yoʻlda
  toʻxtash.
</div>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">30 s</span></p>
  <div class="ps-stem__q">
    <p>If <i>a</i> + <i>b</i> = 9, what is the value of
    4<i>a</i> + 4<i>b</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>36</li>
    <li>13</li>
    <li>9</li>
    <li>It cannot be determined</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 36</p>
      <p>4a + 4b = 4(a + b) = 4 × 9.</p>
      <p>a va b ning oʻzi kerak emas — va topib ham boʻlmaydi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">It cannot be determined</span>
  <span class="ps-trap__why">Eng koʻp tanlanadigan notoʻgʻri javob.
  Oʻquvchi a va b ni topolmagani uchun shunday deydi — lekin savol
  ularni emas, <b>boʻlakni</b> soʻragan edi, va boʻlak
  aniq.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>If <i>x</i>² + <i>y</i>² = 20 and <i>xy</i> = 8, what is the
    value of (<i>x</i> + <i>y</i>)²?</p>
  </div>
  <ol class="ps-ch">
    <li>36</li>
    <li>28</li>
    <li>160</li>
    <li>6</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 36</p>
      <p>(x + y)² = x² + 2xy + y² = 20 + 2(8) = 36.</p>
      <p>x va y ni topish shart emas.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">28</span>
  <span class="ps-trap__why">20 + 8 hisoblangan — yaʼni oʻrtadagi
  had <b>ikkilanmagan</b>. Yoyilmada 2xy turadi, xy emas.</span>
</div>

<h3>Qachon bu usul ishlamaydi</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Uchta «yoʻq»</span>
  <ol>
    <li><b>Savol nomaʼlumning oʻzini soʻrasa</b> — tuzilma yordam
        bermaydi, tenglamani yechish kerak.</li>
    <li><b>Boʻlak takrorlanmasa</b> — koʻrinmagan tuzilmani
        qidirib vaqt yoʻqotmang.</li>
    <li><b>Yoyish tezroq boʻlsa</b> — masalan (x+1)² ni ochish uch
        soniya oladi. Tuzilma qoida emas, imkoniyat.</li>
  </ol>
</div>

<h3>Exam English — tuzilma savolining belgilari</h3>

<ul class="ps-phrase">
  <li><b>what is the value of</b><span>… ning qiymati (koʻpincha boʻlak)</span></li>
  <li><b>in terms of a + b</b><span>a + b orqali</span></li>
  <li><b>it cannot be determined</b><span>aniqlab boʻlmaydi — koʻpincha tuzoq</span></li>
  <li><b>expressions are equivalent</b><span>ifodalar teng kuchli</span></li>
  <li><b>rewrite the expression</b><span>ifodani qayta yozing</span></li>
</ul>

<div class="pe-fix">
  <p class="pe-bad">a + b = 9 → «a va b ni topolmayman» → aniqlab boʻlmaydi</p>
  <p class="pe-good">4(a + b) = 36</p>
  <p class="pe-fix__why">Savol boʻlakni soʻragan, nomaʼlumlarni emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">(x + y)² = x² + y²</p>
  <p class="pe-good">x² + 2xy + y²</p>
  <p class="pe-fix__why">Oʻrtadagi had ikkilanadi (SAT-29).</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «It cannot be determined» degan variant SAT'da <b>kamdan-kam</b>
  toʻgʻri boʻladi. U koʻpincha shu darsdagi tuzilmani koʻrmagan
  oʻquvchi uchun qoʻyilgan. Bu variantni tanlashdan oldin oʻzingizga
  bitta savol bering: savol haqiqatan har bir nomaʼlumni
  soʻrayaptimi, yoki ularning <b>birikmasini</b>?
</div>

<h3>Daraja va nisbat ham tuzilma</h3>

<p>Tuzilma faqat qavslarda emas. Daraja qonunlari (SAT-23) butun bir
ifodani bir qadamda oʻzgartirishga imkon beradi — nomaʼlumni topmasdan
turib.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2<sup><i>x</i></sup> = 5 berilgan</span>
    <span class="pm-solve__why">x ni topib boʻlmaydi (u butun emas)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2<sup><i>x</i>+1</sup> soʻralgan</span>
    <span class="pm-solve__why">Bu 2<sup>x</sup> × 2</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 5 × 2 = 10</span>
    <span class="pm-solve__why">x umuman kerak boʻlmadi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Yana ikkita</p>
  <p>3<sup><i>x</i></sup> = 4 boʻlsa, 3<sup>2<i>x</i></sup> =
  (3<sup><i>x</i></sup>)² = 16.</p>
  <p><i>a</i> ÷ <i>b</i> = 3 boʻlsa, <i>b</i> ÷ <i>a</i> = 1/3 —
  a va b ning oʻzi kerak emas.</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Savolda <b>topib boʻlmaydigan</b> nomaʼlum koʻrsangiz (masalan
  2<sup>x</sup> = 5), bu tuzilma savoli ekanining eng ishonchli
  belgisi. Test sizdan x ni kutmayapti — u sizdan ifodani
  <b>qayta yozishni</b> kutyapti.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  If <i>x</i> + <i>y</i> = 5, what is 2<i>x</i> + 2<i>y</i>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">10.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  If 5(<i>p</i> + <i>q</i>) = 40, what is <i>p</i> + <i>q</i>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">8.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  If <i>a</i> − <i>b</i> = 4 and <i>a</i> + <i>b</i> = 10, what is
  <i>a</i>² − <i>b</i>²?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">4 × 10 = 40.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  If <i>x</i>² + <i>y</i>² = 13 and <i>xy</i> = 6, what is
  (<i>x</i> + <i>y</i>)²?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">13 + 12 = 25.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  If 2(<i>m</i> + 3) = 14, what is <i>m</i> + 3?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">7 — m ni topish shart emas.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>structure</b><span>tuzilma</span></li>
  <li><b>expression</b><span>ifoda</span></li>
  <li><b>the value of</b><span>… ning qiymati</span></li>
  <li><b>cannot be determined</b><span>aniqlab boʻlmaydi</span></li>
  <li><b>factor</b><span>koʻpaytuvchi; koʻpaytuvchilarga ajratmoq</span></li>
  <li><b>expand</b><span>qavsni ochmoq</span></li>
  <li><b>substitute</b><span>oʻrniga qoʻymoq</span></li>
  <li><b>equivalent</b><span>teng kuchli</span></li>
  <li><b>difference of squares</b><span>kvadratlar ayirmasi</span></li>
  <li><b>group</b><span>boʻlak, guruh</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Savol <b>boʻlakni</b> soʻrasa, nomaʼlumni topmang.</li>
    <li>(x+y)² va a²−b² — tayyor koʻprik: bittasi berilsa, ikkinchisi
        chiqadi.</li>
    <li><b>«Cannot be determined» — koʻpincha tuzoq.</b></li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-93 — extreme values (the deliberate contrast with SAT-81)
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-93: The Extreme Plug-In Technique (0, 1, Negatives)",
        "category": "math",
        "order": 93,
        "summary": (
            "SAT-81 da 0 va 1 dan qochgan edik. Bu darsda ular aynan "
            "kerakli quroldir — chunki savol boshqacha."
        ),
        "stories":  ["They Bend the Wing Until It Breaks"],
        "content": """
<h2>SAT-93: The Extreme Plug-In Technique (0, 1, Negatives)</h2>

<p>SAT-81 da qatʼiy qoida bor edi: <b>0 va 1 ni qoʻymang</b>. Bu darsda
biz aynan ularni qoʻyamiz. Bu ziddiyat emas —
<mark>savolning turi boshqa</mark>, va usul ham shunga qarab
almashadi.</p>

<table class="pe-table">
  <tr><th>Savol</th><th>Nima izlanyapti</th><th>Qanday son</th></tr>
  <tr><td>which expression is equivalent</td><td>bitta toʻgʻri javob</td>
      <td>oddiy, lekin oʻziga xos emas: 2, 3, 10</td></tr>
  <tr><td>which must be true</td><td>bitta <b>qarshi misol</b></td>
      <td>chekka qiymatlar: 0, 1, −1, kasr</td></tr>
</table>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha — farqni bir jumlada</span>
  Birinchi turda siz javobni <b>topmoqchisiz</b>, shuning uchun
  tasodifiy mos tushishdan qochasiz. Ikkinchi turda siz javobni
  <b>buzmoqchisiz</b>, shuning uchun eng buzuvchi sonlarni tanlaysiz.
  Bitta qarshi misol variantni oʻldiradi.
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>«must be true» savolini uzoqdan taniysiz;</li>
    <li>beshta chekka qiymatni tartib bilan sinaysiz;</li>
    <li>bitta qarshi misol yetarli ekanini bilasiz;</li>
    <li>faqat musbat butun sonlarni sinash odatidan qutulasiz.</li>
  </ul>
</div>

<h3>Sinaladigan beshta son</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Tartib</span>
  <ol>
    <li><b>0</b> — koʻpaytmani nolga aylantiradi, boʻlishni
        buzadi.</li>
    <li><b>1</b> — daraja va koʻpaytirish farqini yoʻqotadi.</li>
    <li><b>−1</b> yoki boshqa manfiy — ishorani agʻdaradi, kvadratni
        musbat qiladi.</li>
    <li><b>1/2</b> kabi kasr — kvadratga koʻtarilganda
        <b>kichrayadi</b>.</li>
    <li><b>katta son</b> — chegaraviy holatni koʻrsatadi.</li>
  </ol>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Uchinchi va toʻrtinchi qatorlar eng koʻp ball keltiradi. Oʻquvchilar
  deyarli har doim <b>faqat musbat butun sonlarni</b> sinaydi, va SAT
  buni biladi: notoʻgʻri variantlar aynan musbat butun sonlarda
  toʻgʻri koʻrinadigan qilib tanlanadi.
</div>

<h3>Birinchi misol — kasr va manfiyning kuchi</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Daʼvo: «agar x &gt; y boʻlsa, x² &gt; y²»</span>
    <span class="pm-solve__why">Musbat sonlarda toʻgʻri koʻrinadi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = 3, y = 2 → 9 &gt; 4 ✓</span>
    <span class="pm-solve__why">Hali hech narsa isbotlanmadi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 1, y = −2 → 1 &gt; 4 ✗</span>
    <span class="pm-solve__why">Bitta qarshi misol — daʼvo oʻldi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Kasr ham xuddi shunday ishlaydi</p>
  <p>«Har qanday sonning kvadrati oʻzidan katta» — 1/2 ni qoʻying:
  kvadrati 1/4, va u kichikroq. Bitta son butun daʼvoni yiqitdi.</p>
</div>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">70 s</span></p>
  <div class="ps-stem__q">
    <p>If <i>x</i> &gt; <i>y</i>, which of the following must be
    true?</p>
  </div>
  <ol class="ps-ch">
    <li><i>x</i> − <i>y</i> &gt; 0</li>
    <li><i>x</i>² &gt; <i>y</i>²</li>
    <li><i>x</i>/<i>y</i> &gt; 1</li>
    <li><i>xy</i> &gt; 0</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) x − y &gt; 0</p>
      <p>x = 1, y = −2 ni qoʻying: x² = 1 va y² = 4, demak ikkinchi
      variant yiqildi. x/y = −0.5, uchinchisi yiqildi. xy = −2,
      toʻrtinchisi yiqildi.</p>
      <p>Birinchisi esa taʼrifning oʻzi: x &gt; y degani aynan
      x − y musbat degani.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val"><i>x</i>² &gt; <i>y</i>²</span>
  <span class="ps-trap__why">Musbat sonlarda har doim toʻgʻri chiqadi,
  shuning uchun faqat 2, 3, 5 ni sinagan oʻquvchi buni tanlaydi.
  Manfiy son qoʻyilgan zahoti u yiqiladi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>If <i>n</i> is an integer, which of the following must be
    even?</p>
  </div>
  <ol class="ps-ch">
    <li>2<i>n</i></li>
    <li><i>n</i> + 2</li>
    <li><i>n</i>²</li>
    <li>3<i>n</i></li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 2n</p>
      <p>n = 1 ni qoʻying: n + 2 = 3 toq, n² = 1 toq, 3n = 3 toq.
      Uchtasi bir sinovda yiqildi.</p>
      <p>2n esa taʼrifi boʻyicha juft — n qanday boʻlishidan qatʼi
      nazar.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val"><i>n</i> + 2</span>
  <span class="ps-trap__why">n <b>juft</b> boʻlsa toʻgʻri. Lekin savol
  «must be» degan — yaʼni <b>hamma</b> butun son uchun. Bitta toq son
  yetarli.</span>
</div>

<h3>Qachon bu usul ishlamaydi</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Uchta «yoʻq»</span>
  <ol>
    <li><b>Savol «could be true» desa</b> — bunda bitta misol
        <b>tasdiqlaydi</b>, rad etmaydi. Yoʻnalish teskari.</li>
    <li><b>Shartlar sonni cheklasa</b> — «if n is a positive
        integer» deyilgan boʻlsa, manfiy son sinash mumkin emas.</li>
    <li><b>Hech qaysi variant yiqilmasa</b> — demak qarshi misolni
        yaxshi tanlamadingiz; kasr va manfiyga qayting.</li>
  </ol>
</div>

<h3>Exam English — turni ajratadigan iboralar</h3>

<ul class="ps-phrase">
  <li><b>must be true</b><span>har doim toʻgʻri — qarshi misol qidiring</span></li>
  <li><b>could be true</b><span>toʻgʻri boʻlishi mumkin — bitta misol yetadi</span></li>
  <li><b>for all values of x</b><span>x ning barcha qiymatlari uchun</span></li>
  <li><b>is a positive integer</b><span>musbat butun son (chegara!)</span></li>
  <li><b>which of the following is NOT</b><span>qaysi biri EMAS</span></li>
</ul>

<div class="pe-fix">
  <p class="pe-bad">Faqat 2, 3, 5 sinaldi → «hammasi toʻgʻri»</p>
  <p class="pe-good">0, 1, −1 va 1/2 ni ham sinang</p>
  <p class="pe-fix__why">Tuzoqlar musbat butun sonlarda yashiringan.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">«n juft boʻlsa toʻgʻri» → tanlandi</p>
  <p class="pe-good">«must be» — hamma n uchun boʻlishi kerak</p>
  <p class="pe-fix__why">Bitta qarshi misol variantni oʻldiradi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Diqqat qiling: agar savolda <b>«if n is a positive integer»</b>
  deyilgan boʻlsa, manfiy son va nol <b>taqiqlangan</b> — ularni
  sinash notoʻgʻri xulosa beradi. Chekka qiymatlarni sinashdan oldin
  savol qanday chegara qoʻyganini oʻqing.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu usul <b>tezroq</b> ham: toʻrtta variantni algebra bilan tekshirish
  bir necha daqiqa oladi, x = 1 va y = −2 ni qoʻyish esa oʻn besh
  soniya. Bitta yaxshi tanlangan juftlik uchta variantni birdan
  yiqitdi.
</div>

<h3>Rost koʻrinadigan beshta yolgʻon</h3>

<p>Quyidagi daʼvolar musbat butun sonlarda tekshirilsa toʻgʻri chiqadi
va aynan shuning uchun tuzoq javob boʻlib qoʻyiladi. Oʻng ustunda
ularning har birini bir zumda oʻldiradigan son turibdi.</p>

<table class="pe-table">
  <tr><th>Daʼvo</th><th>Qarshi misol</th><th>Nima boʻladi</th></tr>
  <tr><td><i>x</i>² ≥ <i>x</i></td><td><i>x</i> = 1/2</td>
      <td>1/4 &lt; 1/2</td></tr>
  <tr><td><i>x</i>² &gt; 0</td><td><i>x</i> = 0</td><td>0 &gt; 0 emas</td></tr>
  <tr><td>1 ÷ <i>x</i> &lt; <i>x</i></td><td><i>x</i> = 1/2</td>
      <td>2 &gt; 1/2</td></tr>
  <tr><td><i>x</i> &gt; <i>y</i> → <i>x</i>² &gt; <i>y</i>²</td>
      <td><i>x</i> = 1, <i>y</i> = −2</td><td>1 &lt; 4</td></tr>
  <tr><td><i>x</i> &gt; 0 → 1 ÷ <i>x</i> &lt; 1</td><td><i>x</i> = 1/2</td>
      <td>2 &gt; 1</td></tr>
</table>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha — jadvaldagi qonuniyat</span>
  Beshta qatordan uchtasini bitta son — <b>1/2</b> — oʻldirdi.
  Sababi oddiy: birdan kichik musbat kasr kvadratga koʻtarilganda
  <b>kichrayadi</b>, teskarisiga aylanganda esa <b>kattalashadi</b>.
  Faqat butun sonlarda oʻylagan miya buni hech qachon
  koʻrmaydi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Is "<i>x</i>² &gt; <i>x</i>" always true?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — x = 1/2 da 1/4 chiqadi, va u
  kichikroq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  If <i>a</i> &lt; <i>b</i>, must <i>a</i> − <i>b</i> be negative?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ha — bu tengsizlikning taʼrifi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  If <i>n</i> is an integer, must 3<i>n</i> be odd?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — n = 2 da 6 chiqadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Which number kills the claim "<i>x</i>³ &gt; <i>x</i>"?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">0 (0 &gt; 0 emas) yoki 1/2 (1/8
  kichikroq).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A question says "<i>n</i> is a positive integer". May you test −1?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — shart uni taqiqlaydi.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>must be true</b><span>har doim toʻgʻri</span></li>
  <li><b>could be true</b><span>toʻgʻri boʻlishi mumkin</span></li>
  <li><b>counterexample</b><span>qarshi misol</span></li>
  <li><b>integer</b><span>butun son</span></li>
  <li><b>even / odd</b><span>juft / toq</span></li>
  <li><b>positive / negative</b><span>musbat / manfiy</span></li>
  <li><b>fraction</b><span>kasr</span></li>
  <li><b>for all values</b><span>barcha qiymatlar uchun</span></li>
  <li><b>eliminate</b><span>chiqarib tashlamoq</span></li>
  <li><b>constraint</b><span>cheklov, shart</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>«Must be true» → qarshi misol qidiring</b>, javob
        emas.</li>
    <li>0, 1, −1, 1/2 — tuzoqlar aynan shu yerda ochiladi.</li>
    <li>Savolning <b>chegarasini</b> avval oʻqing.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-94 — direct translation of word problems
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-94: The Direct Translation Method for Word Problems",
        "category": "math",
        "order": 94,
        "summary": (
            "Matnli masalani boshdan oxirigacha oʻqib, keyin oʻylamang — "
            "har bir jumlani oʻqigan zahoti belgiga oʻgiring."
        ),
        "stories":  ["Cooking for Three Hundred"],
        "content": """
<h2>SAT-94: The Direct Translation Method for Word Problems</h2>

<p>SAT-91 alohida iboralarni oʻgirishni oʻrgatdi. Bu dars ularni
<b>ketma-ket</b> qoʻyishni oʻrgatadi. Matnli masala qoʻrqinchli
koʻrinadi, chunki u bir necha jumladan iborat —
<mark>lekin har bir jumla alohida qisqa va oson</mark>. Xato deyarli
har doim ularni birga oʻqishga urinishdan chiqadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>nomaʼlumni <b>soʻz bilan</b> nomlaysiz;</li>
    <li>har bir jumlani alohida qatorga oʻgirasiz;</li>
    <li>sonlar yoniga <b>birlik</b> yozasiz;</li>
    <li>oxirida savolning oʻz jumlasiga qaytasiz.</li>
  </ul>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">The move — toʻrt qadam</span>
  <ol>
    <li><b>Nomlang.</b> «n — Jasurning kitoblari soni». Harf emas,
        <b>jumla</b> yozing.</li>
    <li><b>Oʻgiring.</b> Matnni jumlama-jumla yuring va har birini
        oʻz qatoriga yozing.</li>
    <li><b>Yeching.</b> Endi bu shunchaki tenglama.</li>
    <li><b>Qayting.</b> Savol nimani soʻragan edi? Aynan oʻsha
        sonni belgilang.</li>
  </ol>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha — nega birinchi qadam soʻz bilan</span>
  «n = 8» degan javob hech narsa aytmaydi. «Jasurda 8 ta kitob» degan
  javob esa oʻzini oʻzi tekshiradi: siz uni ovoz chiqarib
  aytganingizda toʻgʻri yoki notoʻgʻri ekani darrov sezilib qoladi.
  Nomaʼlumni soʻz bilan nomlash — SAT-89 dagi <b>birinchi tur</b>
  tuzoqqa qarshi eng arzon himoya.
</div>

<h3>Birinchi misol — bosqichma-bosqich</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">"A gym charges a $40 joining fee"</span>
    <span class="pm-solve__why">Bir martalik: 40</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">"plus $15 a month"</span>
    <span class="pm-solve__why">Har oy: 15 × oylar</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">"the total is $175"</span>
    <span class="pm-solve__why">"is" → tenglik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">40 + 15<i>m</i> = 175</span>
    <span class="pm-solve__why">Uch qator birlashdi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">15<i>m</i> = 135, demak <i>m</i> = 9 oy</span>
    <span class="pm-solve__why">Birlik bilan: «9 oy»</span>
  </div>
</div>

<h3>Ikkinchi misol — ikki kishi, bitta tenglama</h3>

<p>SAT'ning eng koʻp uchraydigan matnli masalasi: ikki miqdor
bir-biriga bogʻlangan va yigʻindisi berilgan. Yoʻl har doim bir xil:
<b>ikkalasini ham bitta nomaʼlum orqali yozing</b>.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step"><i>j</i> — Jasurning kitoblari</span>
    <span class="pm-solve__why">Kichikroq miqdorni tanlang</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">"Afsona has 3 more than twice as many as Jasur"</span>
    <span class="pm-solve__why">Afsonaniki: 2<i>j</i> + 3</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">"Together they have 27"</span>
    <span class="pm-solve__why"><i>j</i> + (2<i>j</i> + 3) = 27</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3<i>j</i> = 24</span>
    <span class="pm-solve__why">Ochib, soddalashtirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Jasurda 8 ta, Afsonada 19 ta</span>
    <span class="pm-solve__why">Tekshiruv: 8 + 19 = 27 ✓</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling — yoʻnalish</span>
  «Afsona has twice as many as Jasur» degani <b>Afsona = 2 × Jasur</b>.
  Oʻquvchilar buni tez-tez teskari yozadi. Nazorat oddiy: gapda
  <b>kimning</b> nomi oldin turgan boʻlsa, u kattaroq tomonda —
  «twice as many» iborasi shu tartibda ishlaydi.
</div>

<h3>Birlik yozish odati</h3>

<p>Har bir sonning yoniga uning birligini yozing: <b>9 oy</b>,
<b>8 kitob</b>, <b>145 dollar</b>. Bu ikki soniya oladi va SAT-89 dagi
<b>toʻrtinchi tur</b> tuzoqni — birlik xatosini — deyarli butunlay
yoʻq qiladi.</p>

<div class="pm-check">
  <p class="pm-check__t">Birlik nazorati ish beradi</p>
  <p>«150 km ÷ 90 daqiqa» yozilsa, javobning birligi
  <b>km/daqiqa</b> boʻlib chiqadi va koʻzga tashlanadi. Savol esa
  km/soat soʻragan edi.</p>
</div>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">65 s</span></p>
  <div class="ps-stem__q">
    <p>A gym charges a joining fee of $40 plus $15 for each month of
    membership. After how many months will a member have paid a total
    of $175?</p>
  </div>
  <ol class="ps-ch">
    <li>9</li>
    <li>12</li>
    <li>11</li>
    <li>135</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 9</p>
      <p>40 + 15m = 175 → 15m = 135 → m = 9 oy.</p>
      <p>Tekshiruv: 40 + 135 = 175 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">12</span>
  <span class="ps-trap__why">175 ni 15 ga boʻlgan — yaʼni <b>40
  dollarlik kirish toʻlovini unutgan</b>. Bu matnli masalaning eng
  koʻp uchraydigan xatosi: bir martalik toʻlovni har oylik bilan
  chalkashtirish.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">80 s</span></p>
  <div class="ps-stem__q">
    <p>Afsona has 3 more than twice as many books as Jasur. Together
    they have 27 books. How many books does Jasur have?</p>
  </div>
  <ol class="ps-ch">
    <li>8</li>
    <li>19</li>
    <li>12</li>
    <li>9</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 8</p>
      <p>Jasurniki j, Afsonaniki 2j + 3. Yigʻindi 3j + 3 = 27, demak
      j = 8.</p>
      <p>Tekshiruv: Afsonada 19, va 8 + 19 = 27 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">19</span>
  <span class="ps-trap__why">Bu <b>Afsonaniki</b>. Masala toʻliq va
  toʻgʻri yechilgan — faqat notoʻgʻri odam belgilangan. Toʻrtinchi
  qadam («qayting») aynan shu uchun bor.</span>
</div>

<h3>Qachon bu usul kerak emas</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Uchta «yoʻq»</span>
  <ol>
    <li><b>Bir qadamli savolda</b> — «What is 15% of 60?» uchun
        tenglama tuzish ortiqcha.</li>
    <li><b>Javoblar son boʻlsa</b> — sinash tezroq boʻlishi
        mumkin (SAT-82).</li>
    <li><b>Jadval yoki grafik berilgan boʻlsa</b> — javob koʻpincha
        oʻqib olinadi, tuzilmaydi.</li>
  </ol>
</div>

<h3>Exam English</h3>

<ul class="ps-phrase">
  <li><b>a joining fee of</b><span>kirish toʻlovi — bir martalik</span></li>
  <li><b>for each month</b><span>har bir oy uchun — takrorlanadigan</span></li>
  <li><b>twice as many as</b><span>… dan ikki barobar koʻp</span></li>
  <li><b>together they have</b><span>ikkalasida jami</span></li>
  <li><b>after how many</b><span>necha … dan keyin</span></li>
  <li><b>a total of</b><span>jami</span></li>
</ul>

<div class="pe-fix">
  <p class="pe-bad">175 ÷ 15 = 11.67 → 12</p>
  <p class="pe-good">(175 − 40) ÷ 15 = 9</p>
  <p class="pe-fix__why">Bir martalik toʻlov avval ayiriladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Jasur = 2 × Afsona</p>
  <p class="pe-good">Afsona = 2 × Jasur + 3</p>
  <p class="pe-fix__why">«A has twice as many as B» → A kattaroq.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikki kishili masalada <b>kichikroq miqdorni</b> nomaʼlum qilib
  oling. Shunda ikkinchisi qoʻshuv bilan yoziladi (2j + 3), ayirish
  bilan emas — va kasr ham, manfiy son ham chiqmaydi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  A club charges $25 to join and $8 a visit. Write the cost of
  <i>v</i> visits.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">25 + 8v.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  With that club, how many visits cost $105?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">105 − 25 = 80, va 80 ÷ 8 = 10 ta
  tashrif.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Sherbek has 5 more than three times as many pens as Iroda. Together
  they have 29. How many does Iroda have?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">i + 3i + 5 = 29 → 4i = 24 → Irodada 6 ta
  (Sherbekda 23).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Same question — how many does Sherbek have?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">23. Savol kimni soʻraganiga qarang.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Why write the unit next to every number?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Birlik xatosi javobning oʻzida koʻrinib
  qoladi.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>word problem</b><span>matnli masala</span></li>
  <li><b>joining fee</b><span>kirish toʻlovi</span></li>
  <li><b>membership</b><span>aʼzolik</span></li>
  <li><b>per month</b><span>oyiga</span></li>
  <li><b>twice as many</b><span>ikki barobar koʻp</span></li>
  <li><b>altogether</b><span>jami, birgalikda</span></li>
  <li><b>one-time</b><span>bir martalik</span></li>
  <li><b>define a variable</b><span>nomaʼlumni belgilash</span></li>
  <li><b>unit</b><span>birlik</span></li>
  <li><b>set up an equation</b><span>tenglama tuzmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Nomaʼlumni <b>jumla</b> bilan nomlang, harf bilan emas.</li>
    <li>Jumlama-jumla oʻgiring — birdaniga emas.</li>
    <li>Har bir son yoniga <b>birlik</b> yozing.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-95 — the scratchpad
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-95: Using the Scratchpad Effectively",
        "category": "math",
        "order": 95,
        "summary": (
            "Qoralama qogʻoz — xotira emas, tartib. Toʻrt qatorlik "
            "qolip butun blokdagi xatolarning yarmini tutadi."
        ),
        "stories":  ["The Notebook You May Not Erase"],
        "content": """
<h2>SAT-95: Using the Scratchpad Effectively</h2>

<p>Imtihonda qoralama qogʻoz beriladi, va koʻpchilik uni ikki xil
notoʻgʻri ishlatadi: yo umuman ishlatmaydi (hammasini boshda
qiladi), yo hamma joyni tartibsiz sonlar bilan toʻldiradi.
<mark>Qogʻozning vazifasi hisoblash emas — tartib</mark>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>toʻrt qatorlik qolipni har bir savolga qoʻllaysiz;</li>
    <li>savolni koʻchirib yozmaysiz;</li>
    <li>savollarni bir-biridan chiziq bilan ajratasiz;</li>
    <li>javobni birligi bilan doira ichiga olasiz.</li>
  </ul>
</div>

<h3>Toʻrt qator</h3>

<table class="pe-table">
  <tr><th>Qator</th><th>Nima yoziladi</th><th>Misol</th></tr>
  <tr><td><b>MAQSAD</b></td><td>savol nimani soʻragan</td>
      <td>Jasurning kitoblari?</td></tr>
  <tr><td><b>BERILGAN</b></td><td>sonlar, birligi bilan</td>
      <td>jami 27 kitob; A = 2J + 3</td></tr>
  <tr><td><b>ISH</b></td><td>tenglama va yechim</td>
      <td>3J + 3 = 27 → J = 8</td></tr>
  <tr><td><b>JAVOB</b></td><td>son + birlik, doira ichida</td>
      <td>8 kitob</td></tr>
</table>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha — birinchi qator eng muhimi</span>
  «MAQSAD» qatori atigi uch-toʻrt soʻz oladi, lekin u SAT-89 dagi
  <b>birinchi tur</b> tuzoqni butunlay yopadi. Javobni belgilashdan
  oldin koʻzingiz oʻsha qatorga tushadi va «men nimani soʻrayotgan
  edim?» degan savol oʻz-oʻzidan tugʻiladi.
</div>

<h3>Nima yozilmaydi</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Uchta vaqt yeyuvchi odat</span>
  <ol>
    <li><b>Savolni koʻchirish.</b> U ekranda turibdi. Koʻchirish
        30 soniya oladi va hech narsa qoʻshmaydi.</li>
    <li><b>Har bir qadamni toʻliq yozish.</b> Ikki xonali qoʻshuvni
        yozib oʻtirish shart emas — qogʻoz <b>tuzilma</b> uchun,
        arifmetika uchun emas.</li>
    <li><b>Bir joyga hammasini yigʻish.</b> Ikki savolning ishi
        aralashib ketsa, tekshirish imkonsiz boʻladi.</li>
  </ol>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Har bir savoldan keyin <b>gorizontal chiziq</b> torting va yoniga
  savol raqamini yozing. Ikkinchi oʻtishda (SAT-88) belgilangan
  savolga qaytganingizda, ishingiz tayyor turadi va noldan
  boshlamaysiz. Bu bitta chiziq ikkinchi oʻtishni ikki barobar
  tezlashtiradi.
</div>

<h3>Geometriyada — qayta chizish</h3>

<p>SAT-86 da koʻrgan edik: «not drawn to scale» yozilgan chizmani
oʻzingiz qayta chizish kerak. Qoralama qogʻozning eng kuchli
ishlatilishi shu. Yorliqlarni <b>oʻz</b> chizmangizga koʻchiring va
ekrandagi rasmni butunlay unuting.</p>

<div class="pm-check">
  <p class="pm-check__t">Qayta chizishda nimalar yoziladi</p>
  <p>Har bir maʼlum uzunlik va burchak; toʻgʻri burchak belgisi;
  soʻralayotgan tomon savol belgisi bilan. Uchtasi ham chizmada
  koʻrinib tursa, formula oʻzi tanlanadi.</p>
</div>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">70 s</span></p>
  <div class="ps-stem__q">
    <p>A printer produces 24 pages a minute. A job of 900 pages is
    started at 10:00. At what time does it finish, to the nearest
    minute?</p>
  </div>
  <ol class="ps-ch">
    <li>10:38</li>
    <li>10:24</li>
    <li>11:15</li>
    <li>10:15</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 10:38</p>
      <p><b>MAQSAD:</b> tugash vaqti. <b>BERILGAN:</b> 24 bet/daqiqa,
      900 bet, boshlanish 10:00.</p>
      <p><b>ISH:</b> 900 ÷ 24 = 37.5 daqiqa → 38 daqiqa.</p>
      <p><b>JAVOB:</b> 10:38.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">10:24</span>
  <span class="ps-trap__why">Berilgan sonlardan biri javob sifatida
  qaytarilgan — 24 bu tezlik, vaqt emas. «BERILGAN» va «JAVOB»
  qatorlarini ajratib yozish aynan shuning oldini oladi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>A recipe for 4 people needs 300 grams of rice. Davron is cooking
    for 10 people. How many grams of rice does he need?</p>
  </div>
  <ol class="ps-ch">
    <li>750</li>
    <li>600</li>
    <li>1,200</li>
    <li>120</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 750</p>
      <p><b>MAQSAD:</b> gramm guruch. <b>BERILGAN:</b> 4 kishi →
      300 g.</p>
      <p><b>ISH:</b> bir kishiga 75 g, va 10 × 75 = 750.</p>
      <p><b>JAVOB:</b> 750 gramm.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">600</span>
  <span class="ps-trap__why">4 dan 10 ga oʻtishni «ikki barobar» deb
  olgan. Nisbat 2.5 barobar, 2 emas — «BERILGAN» qatorida
  <b>4 kishi</b> deb yozilgan boʻlsa, bu xato koʻzga
  tashlanadi.</span>
</div>

<h3>Qachon qogʻoz kerak emas</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Ikkita «yoʻq»</span>
  <ol>
    <li><b>Bir qadamli savolda</b> — yozish qilishdan uzoqroq
        davom etadi.</li>
    <li><b>Desmos yechadigan savolda</b> — sistemani qogʻozda
        yechish 90 soniya, ekranda 20 (SAT-83). Bunda qogʻozga faqat
        <b>maqsad</b> qatori yoziladi.</li>
  </ol>
</div>

<h3>Exam English</h3>

<ul class="ps-phrase">
  <li><b>to the nearest minute</b><span>daqiqagacha yaxlitlab</span></li>
  <li><b>a recipe for 4 people</b><span>4 kishiga moʻljallangan retsept</span></li>
  <li><b>produces 24 pages a minute</b><span>daqiqasiga 24 bet chiqaradi</span></li>
  <li><b>at what time</b><span>soat nechada</span></li>
  <li><b>how many grams</b><span>necha gramm</span></li>
</ul>

<div class="pe-fix">
  <p class="pe-bad">Savolni qogʻozga koʻchirish</p>
  <p class="pe-good">Faqat maqsad va berilganlarni yozish</p>
  <p class="pe-fix__why">Savol ekranda turibdi — koʻchirish vaqt
  yoʻqotish.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Javob: 38</p>
  <p class="pe-good">Javob: 10:38 (vaqt)</p>
  <p class="pe-fix__why">Birliksiz son savolga javob bermaydi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu qolipni <b>uyda mashq qilganda</b> ham ishlating. Imtihon kuni
  yangi odat tugʻilmaydi — u faqat allaqachon avtomatik boʻlgan
  narsani qaytaradi. Yigirmata mashq testidan keyin toʻrt qator
  oʻz-oʻzidan yoziladi va hech qanday vaqt olmaydi.
</div>

<h3>Toʻldirilgan qolip — bitta savolda</h3>

<p>Mana oʻsha toʻrt qator haqiqiy savolda qanday koʻrinadi. Hammasi
oʻn beshta soʻzdan kam.</p>

<table class="pe-table">
  <tr><th>Qator</th><th>Qogʻozda</th></tr>
  <tr><td>MAQSAD</td><td>tugash vaqti?</td></tr>
  <tr><td>BERILGAN</td><td>24 bet/daq · 900 bet · start 10:00</td></tr>
  <tr><td>ISH</td><td>900 ÷ 24 = 37.5 → 38 daq</td></tr>
  <tr><td>JAVOB</td><td><b>10:38</b></td></tr>
</table>

<p>Uchinchi qatordagi <b>37.5 → 38</b> yozuvi ayniqsa qimmatli: u
yaxlitlash qilinganini koʻrsatib turadi. Ikkinchi oʻtishda qaytib
kelganingizda «yaxlitladimmi yoki yoʻqmi?» degan savol
tugʻilmaydi.</p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Beshinchi qator — faqat kerak boʻlganda</span>
  Agar savol koʻp qadamli boʻlsa, oxiriga <b>NAZORAT</b> qatorini
  qoʻshing: topilgan javobni boshlangʻich shartga qaytarib qoʻying.
  Yuqoridagi misolda bu «38 × 24 ≈ 912 bet, 900 dan sal koʻp — mos»
  degan bir qator.
</div>

<h3>Ekrandagi qoralama: variantlarni oʻchirish asbobi</h3>

<p>Qogʻoz yagona vosita emas. Test dasturida <b>javob variantlarini
chizib tashlash</b> asbobi bor — uni bir marta yoqib qoʻysangiz, har
bir savolda variant yonida kichkina tugma turadi va bosilganda oʻsha
variant chizib tashlanadi.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Nima uchun bu muhim</span>
  <ol>
    <li>SAT-88 dagi ehtimolliklar shu asbob bilan <b>koʻrinadigan</b>
        boʻladi: ikkita variant chizib tashlangan boʻlsa, ekranda
        ikkitasi qoladi va tanlov 50 foizga aylanadi.</li>
    <li>Belgilab qoldirilgan savolga qaytganingizda,
        <b>oldin nimani oʻchirganingiz</b> saqlanib turadi — ish
        qaytadan boshlanmaydi.</li>
    <li>Koʻz allaqachon rad etilgan variantga qaytmaydi, va bu
        chalgʻishni kamaytiradi.</li>
  </ol>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Bu asbobni <b>mashq testlarida yoqib oʻrganing</b>. Imtihon kuni
  uni birinchi marta koʻrish — vaqt yoʻqotish va asabiylashish.
  Yoqilgan holat saqlanib qoladi, shuning uchun buni bir marta
  qilish kifoya.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  What goes on the first line of the layout?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Maqsad — savol nimani soʻragan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  A printer does 30 pages a minute. How long for 450 pages?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">450 ÷ 30 = 15 daqiqa.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A recipe for 4 needs 300 g. How much for 6?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Bir kishiga 75 g, demak 450 g.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Why draw a line between questions?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ikkinchi oʻtishda ishni topish uchun.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Should you copy the question onto the paper?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — u ekranda turibdi.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>scratch paper</b><span>qoralama qogʻoz</span></li>
  <li><b>layout</b><span>qolip, joylashuv</span></li>
  <li><b>label</b><span>belgilamoq, yorliq</span></li>
  <li><b>circle the answer</b><span>javobni doira ichiga olmoq</span></li>
  <li><b>cross out</b><span>chizib tashlamoq</span></li>
  <li><b>redraw</b><span>qayta chizmoq</span></li>
  <li><b>per minute</b><span>daqiqasiga</span></li>
  <li><b>to the nearest</b><span>… gacha yaxlitlab</span></li>
  <li><b>keep track of</b><span>kuzatib bormoq</span></li>
  <li><b>habit</b><span>odat</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>MAQSAD · BERILGAN · ISH · JAVOB</b> — toʻrt qator.</li>
    <li>Savolni <b>koʻchirmang</b>; savollarni chiziq bilan
        ajrating.</li>
    <li>Javobni <b>birligi bilan</b> yozing.</li>
  </ul>
</div>
""",
    },
]
