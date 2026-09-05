# -*- coding: utf-8 -*-
"""Prime SAT Math — lessons 86–90 (Blok E: chizma, baho, vaqt, tuzoq, grid-in).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_SAT.md
Lesson list: tutorial/management/commands/toc_prime_sat_math.txt

⚠️ SARLAVHALAR BAZADAN OLINGAN, aynan.

⚠️ BLOK E QOIDASI: matematika oʻrgatilmaydi — testni yechish usuli
   oʻrgatiladi; har bir darsda usul QACHON ishlamasligi ham aytiladi.

⚠️ BU BATCHDA KOMPONENTLAR TOʻGʻRI MARKUP BILAN:
     .ps-desmos → __t + <ol class="ps-desmos__keys"> + __read
     .ps-gridin → <figure> + __boxes + figcaption, --ok / --no
   (oldingi batchlarda ps-desmos ichida oddiy <p> ishlatilgan edi).

⚠️ Chizmalar inline SVG va gate ularni oʻlchaydi (burchaklar, uzunliklar).

⚠️ TEST HAQIDAGI FAKTLAR (STYLE_GUIDE §0.2): matematika — 2 modul,
   har birida 22 savol va 35 daqiqa; ikkinchi modul birinchisiga qarab
   moslashadi; xato javob uchun jarima YOʻQ; chizmalar «not drawn to
   scale» deyilmagan boʻlsa masshtabda; grid-in javobi 5 belgigacha
   (manfiyda 6). ⛔ Narx, sana, markaz nomlari OʻYLAB TOPILMAYDI.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_sat_86_90.py \\
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
    # SAT-86 — eyeballing diagrams
    # ══════════════════════════════════════════════════════════════════
    {
        "title": 'SAT-86: The "Eyeballing" Strategy for Geometry Diagrams',
        "category": "math",
        "order": 86,
        "summary": (
            "SAT chizmalari masshtabda chizilgan — bitta jumla bundan mustasno "
            "deyilmasa. Oʻsha jumla butun strategiyani yoqadi yoki oʻchiradi."
        ),
        "stories":  ["The Map That Tells the Truth Sideways"],
        "content": """
<h2>SAT-86: The "Eyeballing" Strategy for Geometry Diagrams</h2>

<p>Geometriya savolining ostida baʼzan bitta kichkina qator turadi:
<b>Note: Figure not drawn to scale.</b> Koʻpchilik oʻquvchi uni
oʻqimaydi. Aslida bu qator <mark>butun savolni ikkiga ajratadigan
kalit</mark> — u boʻlmasa chizmaga ishonish mumkin, u boʻlsa
chizma sizni ataylab aldaydi.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Testning oʻz qoidasi</span>
  <p>SAT chizmalari <b>masshtabda</b> chiziladi — savol boshqacha
  aytmasa. Demak burchak va uzunliklarni koʻz bilan taqqoslash
  <b>ruxsat etilgan</b>, faqat u javobni <b>tanlash</b> uchun emas,
  variantlarni <b>chiqarib tashlash</b> uchun ishlatiladi.</p>
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>chizmaga ishonish mumkinmi-yoʻqmi, birinchi soniyada bilasiz;</li>
    <li>chizmadagi maʼlum uzunlikni «lineyka» qilib ishlatasiz;</li>
    <li>toʻgʻri burchakni etalon qilib burchaklarni chamalaysiz;</li>
    <li>«not to scale» boʻlsa chizmani <b>oʻzingiz qayta</b> chizasiz.</li>
  </ul>
</div>

<h3>Birinchi holat — chizma rost gapiryapti</h3>

<div class="pm-fig">
<svg viewBox="0 0 320 220" role="img" aria-label="Toʻgʻri burchakli uchburchak, bir burchagi 30 daraja">
  <polygon class="pm-fill" points="80,190 260,190 80,86.1"
           fill="#dbeafe" fill-opacity="0.5" stroke="#2563eb" stroke-width="2.5"/>
  <polyline points="80,176 94,176 94,190" fill="none" stroke="#0f172a" stroke-width="1.6"/>
  <text class="pm-lbl" x="222" y="181" font-size="13">30°</text>
  <text class="pm-lbl" x="88" y="106" font-size="13">x°</text>
  <text class="pm-lbl" x="62" y="198" font-size="12">C</text>
  <text class="pm-lbl" x="264" y="198" font-size="12">B</text>
  <text class="pm-lbl" x="66" y="82" font-size="12">A</text>
</svg>
</div>

<p>Savol A burchagini soʻrasa, hisoblashdan <b>oldin</b> qarang: u
toʻgʻri burchakdan kichik, lekin 30 dan sezilarli katta. Demak 90 ham,
120 ham, 30 ham javob boʻla olmaydi — bitta variant qoladi va u
hisoblanmasdan tanlanadi.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Koʻz bilan oʻlchashning uchta asbobi</span>
  <ol>
    <li><b>Toʻgʻri burchak — etalon.</b> Chizmadagi 90° dan koʻrinib
        turib kichik burchak oʻtkir, katta boʻlsa oʻtmas.</li>
    <li><b>Maʼlum tomon — lineyka.</b> «Bu tomon 6» deyilgan boʻlsa,
        boshqa tomon undan taxminan ikki barobar uzunmi, teng
        yarmimi — shu yetadi.</li>
    <li><b>Yuza — kvadratchalar.</b> Shakl atrofiga toʻgʻri toʻrtburchak
        tasavvur qiling: ichidagi shaklning yuzasi undan kichik
        boʻlishi shart.</li>
  </ol>
</div>

<h3>Ikkinchi holat — chizma yolgʻon gapiryapti</h3>

<div class="pm-fig">
<svg viewBox="0 0 320 150" role="img" aria-label="Masshtabda chizilmagan kesma, B nuqta oʻrtada koʻrinadi">
  <line class="pm-ln" x1="60" y1="80" x2="260" y2="80" stroke="#0f172a" stroke-width="2.5"/>
  <circle cx="60" cy="80" r="4" fill="#0f172a"/>
  <circle cx="160" cy="80" r="4" fill="#0f172a"/>
  <circle cx="260" cy="80" r="4" fill="#0f172a"/>
  <text class="pm-lbl" x="55" y="70" font-size="13">A</text>
  <text class="pm-lbl" x="155" y="70" font-size="13">B</text>
  <text class="pm-lbl" x="255" y="70" font-size="13">C</text>
  <text class="pm-lbl" x="100" y="100" font-size="13">2</text>
  <text class="pm-lbl" x="200" y="100" font-size="13">6</text>
  <text class="pm-lbl" x="72" y="132" font-size="11">Note: Figure not drawn to scale.</text>
</svg>
</div>

<p>Koʻz B ni oʻrtada koʻradi va miya darrov «AB = BC» deb qoʻyadi.
Yorliqlar esa boshqa narsa aytadi: 2 va 6. <strong>Bu yerda chizma
dalil emas, bezak.</strong></p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  «Not drawn to scale» yozuvi <b>tasodifiy emas</b>. U deyarli har doim
  aynan shu joyda turadi: chizma sizni bir xil deb oʻylashga
  undayotgan joyda. Bu jumlani koʻrsangiz, chizmani chetga suring va
  faqat <b>yorliqlar</b> bilan ishlang.
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Eng yaxshi javob — chizmani <b>qayta chizish</b>. Qora qogʻozda AB ni
  bir dyuym, BC ni uch dyuym qilib chizing. Toʻgʻri chizma savolning
  yarmini oʻzi hal qiladi.
</div>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">30 s</span></p>
  <div class="ps-stem__q">
    <p>In the triangle above, angle <i>C</i> is a right angle and angle
    <i>B</i> measures 30°. What is the measure of angle <i>A</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>60°</li>
    <li>30°</li>
    <li>90°</li>
    <li>120°</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 60°</p>
      <p>Hisob: 180 − 90 − 30 = 60 (SAT-66).</p>
      <p>Koʻz bilan: A toʻgʻri burchakdan kichik va 30 dan katta —
      bitta variant qoladi. Chizma masshtabda, demak bunga ishonish
      mumkin.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">120°</span>
  <span class="ps-trap__why">180 − 60 hisoblangan yoki oʻtmas burchak
  deb oʻylangan. Chizmaga bir marta qarash buni darrov rad etadi:
  A burchagi toʻgʻri burchakdan <b>kichik</b> koʻrinadi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>In the figure above, point <i>B</i> lies on segment <i>AC</i>,
    <i>AB</i> = 2 and <i>BC</i> = 6. What is the length of
    <i>AC</i>? (Note: Figure not drawn to scale.)</p>
  </div>
  <ol class="ps-ch">
    <li>8</li>
    <li>4</li>
    <li>12</li>
    <li>3</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 8</p>
      <p>B kesma ustida yotibdi, demak AC = AB + BC = 2 + 6 = 8.</p>
      <p>Bu yerda koʻz bilan oʻlchash <b>taqiqlangan</b> — chizma
      masshtabda emas.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">4</span>
  <span class="ps-trap__why">Chizmaga ishonib B ni oʻrta nuqta deb
  olgan: 2 + 2 = 4. Aynan shu xato uchun rasm shunday chizilgan va
  aynan shu sababdan «not drawn to scale» yozib qoʻyilgan.</span>
</div>

<h3>Qachon ishlatmaslik kerak</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Uchta «yoʻq»</span>
  <ol>
    <li><b>«Not drawn to scale»</b> yozilgan boʻlsa — chizma
        dalil emas.</li>
    <li><b>Chizma umuman berilmagan</b> boʻlsa — oʻzingiz chizasiz,
        lekin oʻz chizmangizni ham oʻlchamaysiz.</li>
    <li><b>Ikki variant yaqin</b> boʻlsa (58° va 60°) — koʻz ularni
        ajrata olmaydi, hisoblash kerak.</li>
  </ol>
</div>

<h3>Exam English</h3>

<ul class="ps-phrase">
  <li><b>Note: Figure not drawn to scale</b><span>chizma masshtabda emas — koʻzga ishonmang</span></li>
  <li><b>in the figure above</b><span>yuqoridagi chizmada</span></li>
  <li><b>lies on segment AC</b><span>AC kesmasi ustida yotadi</span></li>
  <li><b>the measure of angle A</b><span>A burchagining kattaligi</span></li>
  <li><b>is a right angle</b><span>toʻgʻri burchak</span></li>
</ul>

<div class="pe-fix">
  <p class="pe-bad">B oʻrtada koʻrinyapti → AB = BC</p>
  <p class="pe-good">Yorliqlar 2 va 6 deyapti</p>
  <p class="pe-fix__why">Masshtabda emas — koʻrinish emas, yozuv
  hukmron.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Koʻz bilan «taxminan 60» → belgiladim</p>
  <p class="pe-good">Koʻz bilan uchtasini oʻchiring, keyin hisoblang</p>
  <p class="pe-fix__why">Chamalash tanlash uchun emas, chiqarib
  tashlash uchun.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ekranda chizma turadi, qoʻlingizda esa qoralama qogʻoz. Uzunlikni
  qogʻoz qirrasi bilan emas, <b>chizmaning oʻzidagi maʼlum tomon</b>
  bilan solishtiring: «bu tomon anavinikidan ikki barobar uzun» degan
  xulosa ekran oʻlchamidan mustaqil va shuning uchun ishonchli.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Chamalash <b>yakuniy nazorat</b> sifatida ham qimmatli. Hisoblab
  javob 140° chiqdi, chizmada esa burchak oʻtkir koʻrinadi — demak
  qayerdadir xato bor. Bu tekshiruv bir soniya oladi.
</div>

<h3>Maʼlum tomonni lineyka qilish</h3>

<p>Ekranda oʻlchash uchun hech narsa yoʻq — lekin chizmaning ichida
bor. Bitta tomon yorliq bilan berilgan boʻlsa, u <b>birlik</b>ga
aylanadi va qolgan hamma narsa unga solishtiriladi.</p>

<div class="pm-fig">
<svg viewBox="0 0 320 200" role="img" aria-label="Toʻgʻri toʻrtburchak, eni 6, boʻyi soʻralgan">
  <rect class="pm-fill" x="70" y="60" width="180" height="90"
        fill="#dcfce7" fill-opacity="0.6" stroke="#16a34a" stroke-width="2.5"/>
  <text class="pm-lbl" x="155" y="172" font-size="14">6</text>
  <text class="pm-lbl" x="48" y="110" font-size="14">?</text>
</svg>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Eni 6 deb berilgan</span>
    <span class="pm-solve__why">Bu bizning birligimiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Boʻyi enining yarmicha koʻrinadi</span>
    <span class="pm-solve__why">Ikki marta qoʻysa, en chiqadi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Demak boʻyi ≈ 3</span>
    <span class="pm-solve__why">5 yoki 8 degan variant darrov chiqadi</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  «Yarmi», «ikki barobar», «deyarli teng» — koʻz ishonch bilan
  aytadigan uchta xulosa shu. Undan nozikroq farqni (1.4 barobarmi
  yoki 1.6 barobarmi) koʻz ajratmaydi va urinmang ham.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  A figure carries no note. Are the lengths in proportion?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ha — SAT chizmalari boshqacha aytilmasa
  masshtabda.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  An angle looks a little smaller than a right angle. Which choices can
  you drop: 45°, 88°, 95°, 130°?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">95° va 130° — ular 90 dan katta. 88° eng
  ehtimolli.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  <i>B</i> is on <i>AC</i>, <i>AB</i> = 5, <i>BC</i> = 9. Find
  <i>AC</i>.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">14 — chizma qanday koʻrinishidan qatʼi
  nazar.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Two choices are 58° and 60°. Can eyeballing decide?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — juda yaqin; hisoblash kerak.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  What is the first thing to read under a geometry figure?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">«Not drawn to scale» yozuvi bor-yoʻqligi.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>figure</b><span>chizma</span></li>
  <li><b>not drawn to scale</b><span>masshtabda chizilmagan</span></li>
  <li><b>segment</b><span>kesma</span></li>
  <li><b>lies on</b><span>ustida yotadi</span></li>
  <li><b>the measure of</b><span>… ning kattaligi</span></li>
  <li><b>right angle</b><span>toʻgʻri burchak</span></li>
  <li><b>acute / obtuse</b><span>oʻtkir / oʻtmas</span></li>
  <li><b>in proportion</b><span>nisbatlari saqlangan</span></li>
  <li><b>estimate</b><span>chamalamoq</span></li>
  <li><b>eliminate</b><span>chiqarib tashlamoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Avval <b>yozuvni</b> oʻqing: «not drawn to scale» bormi?</li>
    <li>Masshtabda boʻlsa — koʻz bilan <b>oʻchiring</b>, tanlamang.</li>
    <li>Masshtabda boʻlmasa — chizmani <b>qayta chizing</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-87 — estimation
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-87: The Art of Estimation",
        "category": "math",
        "order": 87,
        "summary": (
            "Aniq javobni topishdan oldin taxminiy javobni toping — u koʻpincha "
            "toʻrtta variantdan uchtasini oʻchiradi."
        ),
        "stories":  ["How to Count a Crowd You Cannot Count"],
        "content": """
<h2>SAT-87: The Art of Estimation</h2>

<p>Testda ikki xil savol bor: javobni <b>hisoblash</b> kerak boʻlgani va
javobni <b>tanib olish</b> kerak boʻlgani. Ikkinchisi birinchisidan
ancha koʻp, chunki toʻrtta variant allaqachon berilgan.
<mark>Taxminiy javob koʻpincha uchtasini bir zumda oʻchiradi</mark>, va
qolgan bittasini hisoblashning hojati ham qolmaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>sonlarni «qulay» songa yaxlitlab bir necha soniyada
        chamalaysiz;</li>
    <li>foizlarni oddiy kasrga aylantirasiz;</li>
    <li>ildizni ikki butun son orasiga joylaysiz;</li>
    <li>javobning <b>imkonsiz</b> boʻlishini uch xil nazorat bilan
        tutasiz.</li>
  </ul>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">The move</span>
  <ol>
    <li><b>Yaxlitlang</b> — har bir sonni yaqin qulay songa.</li>
    <li><b>Hisoblang</b> — boshda, qogʻozsiz.</li>
    <li><b>Oʻchiring</b> — taxminiy javobdan uzoq variantlarni.</li>
    <li><b>Qolganini</b> aniq hisoblang, agar bittadan koʻp qolsa.</li>
  </ol>
</div>

<h3>Foiz — eng foydali joyi</h3>

<p>SAT'da foiz koʻp, va foizni chamalash oson: <b>19 foiz ≈ 20 foiz =
beshdan bir</b>. Yaxlitlash javobni bir necha foizga suradi, variantlar
esa odatda bir necha barobarga farq qiladi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">19 percent of 412 soʻralgan</span>
    <span class="pm-solve__why">Aniq hisob 30 soniya oladi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">≈ 20 foizi 400 dan</span>
    <span class="pm-solve__why">Ikkalasini ham yaxlitladik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 400 ÷ 5 = 80</span>
    <span class="pm-solve__why">Haqiqiy qiymat 78.28 — yetarlicha yaqin</span>
  </div>
</div>

<table class="pe-table">
  <tr><th>Foiz</th><th>Kasr</th><th>Nima qilinadi</th></tr>
  <tr><td>10%</td><td>1/10</td><td>Vergulni bir xona chapga</td></tr>
  <tr><td>20%</td><td>1/5</td><td>Beshga boʻling</td></tr>
  <tr><td>25%</td><td>1/4</td><td>Toʻrtga boʻling</td></tr>
  <tr><td>33%</td><td>≈ 1/3</td><td>Uchga boʻling</td></tr>
  <tr><td>50%</td><td>1/2</td><td>Ikkiga boʻling</td></tr>
</table>

<h3>Ildizlarni ikki son orasiga qoʻyish</h3>

<p>√50 ni hisoblash shart emas. 7² = 49 va 8² = 64, demak √50 —
7 dan sal katta. Variantlar orasida 5 ham, 25 ham boʻlsa, ular
darrov chiqib ketadi.</p>

<div class="pm-check">
  <p class="pm-check__t">Yodda turadigan uchta ildiz</p>
  <p>√2 ≈ 1.4 · √3 ≈ 1.7 · √5 ≈ 2.2. Bu uchtasi bilan koʻpchilik
  SAT ildizini chamalash mumkin: 5√2 ≈ 7, 3√3 ≈ 5.2.</p>
</div>

<h3>Uchta imkonsizlik nazorati</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Javob shunday boʻla olmaydi</span>
  <ol>
    <li><b>Oʻrtacha</b> eng kichik va eng katta son <b>orasida</b>
        boʻlishi shart.</li>
    <li><b>Ehtimollik</b> 0 bilan 1 orasida; foizda 0 bilan 100
        orasida.</li>
    <li><b>Chegirma</b> narxni oshira olmaydi; <b>qoʻshimcha</b> uni
        kamaytira olmaydi.</li>
  </ol>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu uchtasi «taxmin» emas, <b>qonun</b>. 12, 15 va 48 ning oʻrtachasi
  hech qachon 8 ham, 60 ham boʻla olmaydi — hisoblamasdan turib ikkita
  variantni oʻchirasiz. Haqiqiy javob 25.
</div>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">35 s</span></p>
  <div class="ps-stem__q">
    <p>What is 19 percent of 412?</p>
  </div>
  <ol class="ps-ch">
    <li>78.28</li>
    <li>41.2</li>
    <li>8.24</li>
    <li>782.8</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 78.28</p>
      <p>Chamalash: 400 ning beshdan biri 80. Faqat bitta variant
      80 atrofida.</p>
      <p>Boshqalari 10 foiz, 2 foiz va 190 foizga mos keladi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">41.2</span>
  <span class="ps-trap__why">Bu 10 foiz — vergul bir xona surilgan,
  keyin toʻxtab qolingan. Chamalash bunga yoʻl qoʻymaydi: 19 foiz
  10 foizdan deyarli ikki barobar katta.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">40 s</span></p>
  <div class="ps-stem__q">
    <p>A jacket priced at $84 is on sale for 25 percent off. What is the
    sale price?</p>
  </div>
  <ol class="ps-ch">
    <li>$63</li>
    <li>$21</li>
    <li>$105</li>
    <li>$59</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) $63</p>
      <p>Chorak chegirma — demak toʻrtdan uchi qoladi. 84 ning choragi
      21, va 84 − 21 = 63.</p>
      <p>Nazorat: chegirmali narx asl narxdan kichik, lekin uning
      yarmidan katta boʻlishi kerak — faqat 63 shunday.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">$21</span>
  <span class="ps-trap__why">Bu <b>chegirmaning oʻzi</b>, yangi narx
  emas. Imkonsizlik nazorati buni darrov tutadi: 25 foiz chegirma
  narxni toʻrt barobar kamaytirmaydi.</span>
</div>

<h3>Qachon ishlatmaslik kerak</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Uchta «yoʻq»</span>
  <ol>
    <li><b>Variantlar yaqin</b> boʻlsa (78.28 va 78.32) — chamalash
        ularni ajratmaydi.</li>
    <li><b>Grid-in</b> boʻlsa — aniq javob talab qilinadi.</li>
    <li>Savol <b>«exactly»</b> yoki «to the nearest hundredth»
        desa — yaxlitlash javobni buzadi.</li>
  </ol>
</div>

<h3>Exam English</h3>

<ul class="ps-phrase">
  <li><b>approximately</b><span>taxminan — chamalashga ruxsat</span></li>
  <li><b>closest to</b><span>eng yaqini — javob aniq boʻlmasligi mumkin</span></li>
  <li><b>to the nearest tenth</b><span>oʻndan bir aniqlikda</span></li>
  <li><b>which is greater</b><span>qaysi biri katta — hisoblash shart emas</span></li>
  <li><b>at least / at most</b><span>eng kamida / koʻpi bilan</span></li>
</ul>

<div class="pe-fix">
  <p class="pe-bad">Chegirma soʻralganda chegirmaning oʻzini belgilash</p>
  <p class="pe-good">Yangi narx = asl narx − chegirma</p>
  <p class="pe-fix__why">Savolning oxirgi jumlasini qayta oʻqing.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">«Taxminan 80» → 78.28 oʻrniga 82 tanlandi</p>
  <p class="pe-good">Chamalash <b>oʻchiradi</b>, tanlamaydi</p>
  <p class="pe-fix__why">Ikki variant yaqin qolsa, aniq hisoblang.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Chamalash tezlik uchun emas, <b>xavfsizlik</b> uchun ham kerak.
  Kalkulyatorga notoʻgʻri son kiritilsa, natija ishonarli koʻrinadi —
  faqat boshda turgan taxminiy javob uni ushlaydi.
</div>

<h3>Avval variantlarga qarang — ular qanchalik uzoq?</h3>

<p>Chamalashning qanchalik qoʻpol boʻlishi mumkinligini savol emas,
<b>variantlar</b> aytadi. Ular bir-biridan barobarlab farq qilsa,
juda qoʻpol chamalash ham yetadi; oʻnlik xonasida farq qilsa,
chamalash umuman ishlamaydi.</p>

<table class="pe-table">
  <tr><th>Variantlar</th><th>Farqi</th><th>Nima qilinadi</th></tr>
  <tr><td>8, 80, 800, 8000</td><td>10 barobar</td>
      <td>Faqat kattalik tartibini toping</td></tr>
  <tr><td>12, 18, 24, 30</td><td>sezilarli</td>
      <td>Qoʻpol chamalash yetadi</td></tr>
  <tr><td>4.71, 4.79, 4.83, 4.90</td><td>yuzdan bir</td>
      <td>Chamalamang — aniq hisoblang</td></tr>
</table>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu odat bir soniya oladi va butun strategiyani tanlaydi: savolni
  oʻqigach <b>koʻzingizni variantlarga tashlang</b>. Ular sizga qaysi
  quroldan foydalanishni aytadi — chamalash, son qoʻyish, backsolving
  yoki toʻgʻridan-toʻgʻri hisob.
</div>

<div class="ps-desmos">
  <p class="ps-desmos__t">Chamalashni Desmosda tasdiqlash</p>
  <ol class="ps-desmos__keys">
    <li>0.19*412</li>
    <li>84*0.75</li>
    <li>sqrt(50)</li>
  </ol>
  <p class="ps-desmos__read">78.28 · 63 · 7.0711 — uchtasi ham boshda
  chiqarilgan taxminga mos. Desmos chamalashni almashtirmaydi:
  chamalash <b>oldin</b> qilinadi va aynan u kalkulyatorga notoʻgʻri
  son kiritilganini tutadi.</p>
</div>

<h3>Kattalik tartibi — eng qoʻpol va eng foydali nazorat</h3>

<p>Baʼzan javobning aniq qiymati emas, <b>nechta xonali</b> ekani
yetadi. 38 × 21 ni hisoblamang: 40 × 20 = 800, demak javob
yuzlarda. 800 ga yaqin bitta variant boʻlsa, ish tugadi.</p>

<div class="pm-check">
  <p class="pm-check__t">Uch misol, uch soniya</p>
  <p>38 × 21 ≈ 800 (aniq 798) · 612 ÷ 29 ≈ 20 (aniq 21.1) ·
  4.8 × 5.2 ≈ 25 (aniq 24.96).</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Estimate 21 percent of 396.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">≈ 20 foizi 400 dan = 80. Aniq qiymat
  83.16.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Between which two whole numbers does √30 lie?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">5 va 6 (25 va 36 orasida).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Could the average of 4, 9 and 20 be 25?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — oʻrtacha 4 bilan 20 orasida boʻlishi
  shart. U 11.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  A $60 coat is 30 percent off. Estimate the sale price.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Chegirma 18, narx 42.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Two choices are 4.71 and 4.79. Is estimating enough?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — juda yaqin, aniq hisoblang.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>estimate</b><span>chamalamoq</span></li>
  <li><b>approximately</b><span>taxminan</span></li>
  <li><b>round</b><span>yaxlitlamoq</span></li>
  <li><b>closest to</b><span>eng yaqin</span></li>
  <li><b>sale price</b><span>chegirmali narx</span></li>
  <li><b>discount</b><span>chegirma</span></li>
  <li><b>average</b><span>oʻrtacha</span></li>
  <li><b>probability</b><span>ehtimollik</span></li>
  <li><b>reasonable</b><span>maʼqul, ishonarli</span></li>
  <li><b>order of magnitude</b><span>kattalik tartibi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Yaxlitlang, boshda hisoblang, <b>oʻchiring</b>.</li>
    <li>Foizni <b>kasrga</b> aylantiring: 20% = 1/5.</li>
    <li>Oʻrtacha, ehtimollik va chegirma — <b>imkonsizlik</b>
        nazoratlari.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-88 — guessing and the clock
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-88: Strategic Guessing and Time Management",
        "category": "math",
        "order": 88,
        "summary": (
            "Har bir savolga oʻrtacha 95 soniya bor va xato javob uchun jarima "
            "yoʻq. Shu ikki fakt butun strategiyani belgilaydi."
        ),
        "stories":  ["The Ten Minutes She Should Not Have Saved"],
        "content": """
<h2>SAT-88: Strategic Guessing and Time Management</h2>

<p>Bu dars bitta matematik amal ham oʻrgatmaydi. U <mark>testni
tugatib chiqish</mark> haqida — chunki bilgan savoliga yetib
bormagan oʻquvchi bilmagan oʻquvchi bilan bir xil ball oladi.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Testning oʻz raqamlari</span>
  <ul>
    <li>Matematika — <b>ikkita modul</b>, har birida <b>22 savol</b> va
        <b>35 daqiqa</b>.</li>
    <li>Demak bitta savolga oʻrtacha <b>95 soniya</b>.</li>
    <li>Jami: <b>44 savol</b> va <b>70 daqiqa</b> matematika.</li>
    <li>Ikkinchi modulning qiyinligi birinchisidagi natijaga qarab
        <b>moslashadi</b>.</li>
    <li>Xato javob uchun <b>jarima yoʻq</b> — boʻsh qoldirishning
        maʼnosi ham yoʻq.</li>
    <li>Modul <b>ichida</b> savollar orasida erkin yurish va belgilab
        qoʻyish mumkin; <b>oldingi modulga qaytib boʻlmaydi</b>.</li>
  </ul>
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>vaqtni ikki oʻtishga boʻlasiz;</li>
    <li>bitta savolga qancha vaqt «qarz» berish mumkinligini
        bilasiz;</li>
    <li>taxmin qilishdan oldin <b>oʻchirasiz</b>;</li>
    <li>hech qachon boʻsh qoldirmaysiz.</li>
  </ul>
</div>

<h3>Ikki oʻtish qoidasi</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">The move</span>
  <ol>
    <li><b>Birinchi oʻtish:</b> boshdan oxirigacha yuring va faqat
        <b>90 soniyada</b> yechiladiganini yeching.</li>
    <li>Qiyin savolni <b>belgilab</b> qoldiring — lekin bitta javob
        <b>hozir</b> belgilang, chunki qaytib kelolmasligingiz
        mumkin.</li>
    <li><b>Ikkinchi oʻtish:</b> belgilanganlarga qayting. Endi qancha
        vaqt qolganini bilasiz va uni bilib taqsimlaysiz.</li>
  </ol>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Uch daqiqalik savol — eng qimmat xato</span>
  Bitta savolga uch daqiqa sarflash — bu <b>ikkita</b> boshqa savolni
  yoʻqotish. Ular oson boʻlishi ham mumkin edi. Test hamma savolni bir
  xil baholaydi: qiyini ham, osoni ham bitta.
</div>

<table class="pe-table">
  <tr><th>Holat</th><th>Qolgan vaqt</th><th>Qolgan savol</th><th>Har biriga</th></tr>
  <tr><td>Boshida</td><td>35 daqiqa</td><td>22</td><td>95 soniya</td></tr>
  <tr><td>Yarmida</td><td>17 daqiqa</td><td>11</td><td>93 soniya</td></tr>
  <tr><td>Kechikkan</td><td>12 daqiqa</td><td>9</td><td>80 soniya</td></tr>
  <tr><td>Oxirida</td><td>2 daqiqa</td><td>4</td><td>30 soniya — taxmin</td></tr>
</table>

<h3>Taxmin qilish — lekin avval oʻchirib</h3>

<p>Toʻrtta variantdan koʻr-koʻrona tanlash — toʻrtdan bir imkoniyat.
Bitta variantni ishonch bilan oʻchirsangiz uchdan bir, ikkitasini
oʻchirsangiz <b>yarmi</b> boʻladi. Oʻchirish taxminni ikki barobar
kuchaytiradi va u koʻpincha butun savolni yechishdan tez.</p>

<table class="pe-table">
  <tr><th>Oʻchirilgan</th><th>Qolgan variant</th><th>Toʻgʻri chiqish ehtimoli</th></tr>
  <tr><td>0</td><td>4</td><td>25%</td></tr>
  <tr><td>1</td><td>3</td><td>≈ 33%</td></tr>
  <tr><td>2</td><td>2</td><td>50%</td></tr>
</table>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻchirishning eng arzon uchta usuli allaqachon oʻrganilgan:
  <b>chamalash</b> (SAT-87), <b>chizmaga qarash</b> (SAT-86) va
  <b>imkonsizlik nazorati</b> — manfiy uzunlik, birdan katta ehtimollik,
  chegaradan tashqaridagi oʻrtacha. Uchtasi ham 10 soniya oladi.
</div>

<h3>Grid-in savollarda taxmin</h3>

<p>Matematika savollarining taxminan <b>choragi</b> — javobi yoziladigan
grid-in savollar. U yerda variant yoʻq, demak koʻr-koʻrona taxminning
qiymati deyarli nol. Lekin jarima ham yoʻq, shuning uchun
<b>baribir biror son yozing</b>: chamalab topilgan son nolga qaraganda
har doim koʻproq imkoniyat beradi.</p>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">25 s</span></p>
  <div class="ps-stem__q">
    <p>A student has 12 minutes left and 9 questions unanswered. On
    average, how many seconds can be spent on each?</p>
  </div>
  <ol class="ps-ch">
    <li>80</li>
    <li>95</li>
    <li>60</li>
    <li>108</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 80</p>
      <p>12 daqiqa — 720 soniya, va 720 ÷ 9 = 80.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">95</span>
  <span class="ps-trap__why">Bu <b>umumiy oʻrtacha</b> (2,100 ÷ 22),
  qolgan vaqt uchun emas. Oʻquvchi kechikkan holatda hisobni qaytadan
  qilishi kerak.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">30 s</span></p>
  <div class="ps-stem__q">
    <p>On a four-choice question, a student confidently eliminates two
    choices and then guesses. What is the probability of answering
    correctly?</p>
  </div>
  <ol class="ps-ch">
    <li>1/2</li>
    <li>1/4</li>
    <li>1/3</li>
    <li>0</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 1/2</p>
      <p>Ikkita variant qoldi, ikkalasi teng imkoniyatga ega.</p>
      <p>Oʻchirmasdan taxmin qilinganda bu 1/4 edi — oʻchirish
      imkoniyatni ikki barobar oshirdi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">1/4</span>
  <span class="ps-trap__why">Oʻchirish hisobga olinmagan. Savol
  <b>oʻchirilgandan keyingi</b> ehtimollikni soʻrayapti.</span>
</div>

<h3>Qachon bu reja buziladi</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Uchta «yoʻq»</span>
  <ol>
    <li><b>Har bir savolga aynan 95 soniya sanash</b> — soatga qarash
        savol yechishdan koʻproq vaqt oladi. Vaqtni savol emas,
        <b>bosqich</b> boʻyicha tekshiring (11-savolda yarmi
        oʻtgan boʻlsin).</li>
    <li><b>Belgilab qoldirish</b> — javob belgilamasdan. Vaqt tugasa,
        boʻsh savol nolga teng.</li>
    <li><b>Oxirgi daqiqada hammasini qaytadan tekshirish</b> — bu
        deyarli har doim javob almashtirishga va ball
        yoʻqotishga olib keladi.</li>
  </ol>
</div>

<h3>Exam English</h3>

<ul class="ps-phrase">
  <li><b>mark for review</b><span>keyin qaytish uchun belgilab qoʻymoq</span></li>
  <li><b>on average</b><span>oʻrtacha</span></li>
  <li><b>unanswered</b><span>javobsiz qolgan</span></li>
  <li><b>eliminate a choice</b><span>variantni chiqarib tashlamoq</span></li>
  <li><b>time remaining</b><span>qolgan vaqt</span></li>
</ul>

<div class="pe-fix">
  <p class="pe-bad">Qiyin savolni boʻsh qoldirib ketish</p>
  <p class="pe-good">Bitta javob belgilab, keyin belgilab qoʻyish</p>
  <p class="pe-fix__why">Jarima yoʻq — boʻsh javobning qiymati nol.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Bitta savolga 4 daqiqa</p>
  <p class="pe-good">90 soniyadan keyin belgilab, oldinga</p>
  <p class="pe-fix__why">Bitta qiyin savol ikkita osonini yeydi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikkinchi modul birinchisiga qarab moslashadi, shuning uchun birinchi
  modulni <b>toʻliq</b> tugatish ayniqsa muhim. Lekin ikkinchi modul
  yengilroq chiqsa ham, u <b>hisobga olinadi</b> — «oson boʻldi, demak
  yomon yozdim» deb ruhingizni tushirmang: qiyinlik darajasi ballga
  allaqachon kiritilgan.
</div>

<h3>Ikkinchi modul: moslashuv qanday ishlaydi</h3>

<p>Birinchi modul hammaga bir xil keladi. Ikkinchisining qiyinlik
darajasi esa birinchisidagi natijaga qarab tanlanadi. Bundan uchta
amaliy xulosa chiqadi:</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Amaliy xulosalar</span>
  <ol>
    <li><b>Birinchi modulni toʻliq tugating.</b> U nafaqat ball
        beradi, balki ikkinchi modulning ostonasini ham
        belgilaydi.</li>
    <li><b>Ikkinchi modul osonroq tuyulsa, xafa boʻlmang</b> — va
        qiyin tuyulsa, ruhingizni tushirmang. Qiyinlik ballning
        hisobiga allaqachon kiritilgan.</li>
    <li><b>Orqaga qaytib boʻlmaydi.</b> Birinchi modul yopilgach,
        u yerdagi boʻsh savol abadiy boʻsh qoladi — shuning uchun
        belgilab qoldirishdan oldin bitta javob tanlang.</li>
  </ol>
</div>

<h3>Oxirgi oltmish soniya</h3>

<p>Vaqt tugashiga bir daqiqa qolganda strategiya bitta: <b>boʻsh
javoblarni toʻldirish</b>. Yechishga urinmang, oʻqishga ham
urinmang — shunchaki har bir boʻsh savolga bitta variant tanlang.
Toʻrtta boʻsh savolda bu oʻrtacha bitta toʻgʻri javob demakdir,
va u bepul.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha — oʻz suratingizni oʻlchang</span>
  95 soniya — <b>oʻrtacha</b>, meʼyor emas. Uyda mashq qilganda
  vaqtni yozib boring: koʻpchilikda oson savol 40 soniya, oʻrtachasi
  90, qiyini 150 soniya oladi. Shu uchta sonni bilsangiz, imtihonda
  soatga qarash kerak boʻlmaydi — savolning oʻzi qancha
  turishini bilasiz.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  How many seconds per question does 35 minutes for 22 questions give?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">2,100 ÷ 22 ≈ 95 soniya.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  You eliminate one of four choices and guess. What are your odds?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">1/3 — taxminan 33 foiz.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Should you ever leave a question blank?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Hech qachon — xato javob uchun jarima
  yoʻq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  You have 6 minutes and 4 questions left. How long each?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">360 ÷ 4 = 90 soniya.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Can you return to module one during module two?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — modul yopilgach qaytib
  boʻlmaydi.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>module</b><span>modul (test boʻlimi)</span></li>
  <li><b>adaptive</b><span>moslashuvchi</span></li>
  <li><b>penalty</b><span>jarima</span></li>
  <li><b>blank</b><span>boʻsh qoldirilgan</span></li>
  <li><b>mark for review</b><span>keyin qaytish uchun belgilash</span></li>
  <li><b>on average</b><span>oʻrtacha</span></li>
  <li><b>odds</b><span>imkoniyat, ehtimol</span></li>
  <li><b>pace</b><span>sur'at, tezlik</span></li>
  <li><b>remaining</b><span>qolgan</span></li>
  <li><b>confidently</b><span>ishonch bilan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>95 soniya</b> — oʻrtacha; 90 dan oshsa, oldinga yuring.</li>
    <li>Taxmindan oldin <b>oʻchiring</b>: 25% → 50%.</li>
    <li><b>Hech qachon boʻsh qoldirmang</b> — jarima yoʻq.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-89 — trap answers (the course's capstone claim)
    # ══════════════════════════════════════════════════════════════════
    {
        "title": 'SAT-89: Avoiding the "Trap Answers"',
        "category": "math",
        "order": 89,
        "summary": (
            "Har bir notoʻgʻri variant — kimningdir halol xatosi. Xatoni "
            "nomlash javobni nomlashdan qimmatroq."
        ),
        "stories":  ["The List That Was Written After the Crash"],
        "content": """
<h2>SAT-89: Avoiding the "Trap Answers"</h2>

<p>Bu dars — butun kursning asosiy daʼvosini bir joyga yigʻadi:
<mark>SAT'ning notoʻgʻri variantlari tasodifiy sonlar emas</mark>.
Ularning har biri — koʻp uchraydigan bitta aniq xatoning natijasi.
Testni tuzuvchilar bu xatolarni biladi va ularni ataylab
sahifaga qoʻyadi.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha — nega bu yaxshi xabar</span>
  Agar variantlar tasodifiy boʻlganida, xatoni tuzatish mumkin
  boʻlmasdi. Ular <b>tizimli</b> boʻlgani uchun oʻrganish mumkin: yetti
  xil tuzoq bor, va ularni tanigan oʻquvchi oʻz xatosini javobni
  belgilashdan <b>oldin</b> koʻradi.
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>yettita tuzoq turini nom bilan taniysiz;</li>
    <li>oʻzingiz koʻproq tushadigan turini bilasiz;</li>
    <li>javobni belgilashdan oldin bitta nazorat savolini
        berasiz;</li>
    <li>«juda oson chiqib qolgan» javobga shubha qilasiz.</li>
  </ul>
</div>

<h3>Yettita tuzoq</h3>

<table class="pe-table">
  <tr><th>#</th><th>Tuzoq</th><th>Qanday tugʻiladi</th><th>Qaerda koʻrgansiz</th></tr>
  <tr><td>1</td><td>Boshqa savolning javobi</td>
      <td>x topildi, x + y soʻralgan edi</td><td>SAT-83</td></tr>
  <tr><td>2</td><td>Yarim yoʻlda toʻxtash</td>
      <td>r² topildi, r soʻralgan edi</td><td>SAT-80</td></tr>
  <tr><td>3</td><td>Ishora almashishi</td>
      <td>(x − 3) dan −3 koʻchirilgan</td><td>SAT-79</td></tr>
  <tr><td>4</td><td>Birlik oʻgirilmagan</td>
      <td>daqiqa soat oʻrniga qolgan</td><td>SAT-55</td></tr>
  <tr><td>5</td><td>Ikkinchi ildiz</td>
      <td>manfiysi tanlangan, musbati soʻralgan</td><td>SAT-83</td></tr>
  <tr><td>6</td><td>Oʻrtacha ↔ chekka</td>
      <td>yigʻindi uchga boʻlingan, eng kichigi kerak edi</td><td>SAT-81</td></tr>
  <tr><td>7</td><td>Bitta ishonchli notoʻgʻri amal</td>
      <td>13 − 5 = 8, ammo √(169 − 25) = 12 edi</td><td>SAT-76</td></tr>
</table>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Bu jadvalni bir marta oʻqib qoʻyish yetarli emas. <b>Oʻz
  xatolaringizni</b> shu yettita qatorga taqsimlang: mashq tugagach,
  har bir xato qaysi qatorga tushishini yozing. Bir necha testdan
  keyin sizning shaxsiy tuzogʻingiz — koʻpincha bittasi — ayon
  boʻladi.
</div>

<h3>Himoya: ikki soniyalik odat</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">The move</span>
  <ol>
    <li>Yechishdan <b>oldin</b> savolning <b>oxirgi jumlasini</b>
        ajratib qoʻying: nima soʻralyapti?</li>
    <li>Yeching.</li>
    <li>Javobni belgilashdan oldin oʻsha jumlaga <b>qayting</b> va
        ovoz chiqarmasdan takrorlang: «u <i>buni</i> soʻragan
        edi».</li>
  </ol>
</div>

<p>Bu uchinchi qadam ikki soniya oladi va yettita tuzoqning
<b>toʻrttasini</b> (1, 2, 5, 6) butunlay yoʻq qiladi. Qolgan uchtasi —
ishora, birlik va notoʻgʻri amal — hisobning ichida, va ularni
SAT-87 dagi chamalash tutadi.</p>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>A rectangle's length is 4 more than its width, and its perimeter
    is 36. What is the length of the rectangle?</p>
  </div>
  <ol class="ps-ch">
    <li>11</li>
    <li>7</li>
    <li>18</li>
    <li>36</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 11</p>
      <p>En 7, uzunlik 11, perimetr 2(7 + 11) = 36 ✓</p>
      <p>Savolning oxirgi jumlasi <b>uzunlikni</b> soʻragan.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob — 1-tur</span>
  <span class="ps-trap__val">7</span>
  <span class="ps-trap__why">Bu <b>en</b>. Masala toʻliq va toʻgʻri
  yechilgan, keyin notoʻgʻri son belgilangan. SAT'ning eng koʻp
  ishlatadigan tuzogʻi shu.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">70 s</span></p>
  <div class="ps-stem__q">
    <p>A train travels 150 kilometres in 90 minutes. What is its average
    speed, in kilometres per hour?</p>
  </div>
  <ol class="ps-ch">
    <li>100</li>
    <li>1.67</li>
    <li>135</li>
    <li>60</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 100</p>
      <p>90 daqiqa — bu 1.5 soat, va 150 ÷ 1.5 = 100.</p>
      <p>Nazorat (SAT-87): 60 daqiqa — 90 daqiqaning uchdan ikkisi,
      demak bir soatda masofaning ham uchdan ikkisi bosiladi:
      150 ning uchdan ikkisi 100.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob — 4-tur</span>
  <span class="ps-trap__val">1.67</span>
  <span class="ps-trap__why">150 ni 90 ga boʻlgan — yaʼni birlikni
  oʻgirmagan. Javob kilometr/daqiqada chiqdi, savol esa
  kilometr/soatni soʻragan. Imkonsizlik nazorati buni darrov tutadi:
  poyezd soatiga 1.67 km yurmaydi.</span>
</div>

<h3>«Juda oson chiqdi» hissi</h3>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Modulning oxirgi savollari odatda qiyinroq. Agar 20-savol bir amalda
  yechilib qolsa va javob variantlar orasida chiroyli turgan boʻlsa —
  <b>bir marta qayta oʻqing</b>. Koʻpincha bitta qadam tushib
  qolgan boʻladi. Boshidagi savollarda esa bu shubha oʻrinsiz: ular
  <b>haqiqatan</b> oson.
</div>

<h3>Qachon bu dars ishlamaydi</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Ikkita «yoʻq»</span>
  <ol>
    <li><b>Grid-in</b> savolda tuzoq variant yoʻq — u yerda faqat
        oʻz xatongiz bor, va uni chamalash tutadi.</li>
    <li>Tuzoqni tanish <b>matematikaning oʻrnini bosmaydi</b>. Yechimni
        bilmasangiz, «bu tuzoqqa oʻxshaydi» degan tuygʻu javob
        bermaydi.</li>
  </ol>
</div>

<h3>Exam English</h3>

<ul class="ps-phrase">
  <li><b>what is the length of</b><span>uzunligi nechaga teng — oxirgi jumla</span></li>
  <li><b>in kilometres per hour</b><span>kilometr/soatda — birlik talabi</span></li>
  <li><b>the positive solution</b><span>musbat yechim</span></li>
  <li><b>the value of x + y</b><span>x + y ning qiymati, x emas</span></li>
  <li><b>rounded to the nearest</b><span>… gacha yaxlitlangan</span></li>
</ul>

<div class="pe-fix">
  <p class="pe-bad">En topildi → belgilandi</p>
  <p class="pe-good">Oxirgi jumla: «the length» edi</p>
  <p class="pe-fix__why">1-tur tuzoq — eng koʻp uchraydigani.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">150 ÷ 90 = 1.67</p>
  <p class="pe-good">90 daqiqa = 1.5 soat → 100</p>
  <p class="pe-fix__why">4-tur: birlik oʻgirilmagan.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu darsning eng qimmat jumlasi: <b>notoʻgʻri variant — dushman
  emas, maʼlumot</b>. U sizga qanday xato qilish mumkinligini
  koʻrsatib turibdi. Mashqni tekshirayotganda faqat toʻgʻri javobga
  emas, oʻzingiz tanlagan notoʻgʻri variantga ham qarang: u qaysi
  turdan edi?
</div>

<h3>Tuzoqni oldindan aytish mashqi</h3>

<p>Bu darsning eng foydali mashqi gʻalati koʻrinadi: savolni
yechishdan <b>oldin</b> tuzoqni bashorat qiling. «Bu masalada en va
uzunlik bor — demak birinchi tur tuzoq boʻlishi kerak» degan bir
jumla, va siz uni belgilaganingizda tanib olasiz.</p>

<table class="pe-table">
  <tr><th>Savolda koʻrsangiz</th><th>Kutiladigan tuzoq</th></tr>
  <tr><td>Ikkita nomaʼlum (en va uzunlik, kattalar va bolalar)</td>
      <td>1-tur: boshqasining javobi</td></tr>
  <tr><td>Kvadrat, ildiz yoki aylana tenglamasi</td>
      <td>2-tur: yarim yoʻlda toʻxtash</td></tr>
  <tr><td>Qavs ichida qoʻshuv: (x + 3)</td>
      <td>3-tur: ishora</td></tr>
  <tr><td>Daqiqa, sent, gramm, santimetr</td>
      <td>4-tur: birlik</td></tr>
  <tr><td>«the positive solution», «which is greater»</td>
      <td>5-tur: ikkinchi ildiz</td></tr>
</table>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Bashorat qilish savolni sekinlashtirmaydi — u savolning
  <b>oxirgi jumlasini</b> oʻqishga majbur qiladi, va aynan shu
  narsa kerak edi. Bir necha haftadan keyin bashorat ovozsiz va
  avtomatik boʻlib qoladi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  You solve for <i>x</i> but the question asks for 2<i>x</i>. Which trap
  is that?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">1-tur — boshqa savolning javobi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  You find <i>r</i>² = 49 and answer 49. Which trap?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">2-tur — yarim yoʻlda toʻxtash; javob 7.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A width is 7 and a length is 11. The question asks for the perimeter.
  What is it?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">2(7 + 11) = 36.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  A car covers 120 km in 90 minutes. Speed in km per hour?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">120 ÷ 1.5 = 80.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  What single habit removes four of the seven traps?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Belgilashdan oldin savolning oxirgi
  jumlasini qayta oʻqish.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>trap answer</b><span>tuzoq javob</span></li>
  <li><b>distractor</b><span>chalgʻituvchi variant</span></li>
  <li><b>plausible</b><span>ishonarli koʻringan</span></li>
  <li><b>convert</b><span>oʻgirmoq (birlikni)</span></li>
  <li><b>perimeter</b><span>perimetr</span></li>
  <li><b>average speed</b><span>oʻrtacha tezlik</span></li>
  <li><b>per hour</b><span>soatiga</span></li>
  <li><b>halfway</b><span>yarim yoʻlda</span></li>
  <li><b>double-check</b><span>qayta tekshirmoq</span></li>
  <li><b>systematic</b><span>tizimli</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Har bir notoʻgʻri variant — <b>nomlanadigan</b> bitta xato.</li>
    <li>Oxirgi jumlani qayta oʻqish <b>yettitadan toʻrttasini</b>
        yoʻq qiladi.</li>
    <li>Oʻz xatolaringizni <b>turlarga ajratib</b> yozing.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-90 — grid-ins
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-90: The Grid-In Blueprint (Student-Produced Responses)",
        "category": "math",
        "order": 90,
        "summary": (
            "Javobi yoziladigan savollar matematikada emas, formatda "
            "yoʻqotiladi. Qutining oʻz qoidalari bor."
        ),
        "stories":  ["The Last Digit Is Not a Digit"],
        "content": """
<h2>SAT-90: The Grid-In Blueprint (Student-Produced Responses)</h2>

<p>Matematika savollarining taxminan <b>choragida</b> variant yoʻq:
javob qutiga yoziladi. Bu savollarda ball
<mark>koʻpincha matematikada emas, formatda yoʻqoladi</mark> — javob
toʻgʻri topilib, notoʻgʻri yozilgani uchun. Bu dars butunlay shu
quti haqida.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Qutining qoidalari</span>
  <ol>
    <li>Musbat javob <b>5 belgigacha</b>; manfiy javob <b>6 belgigacha</b>
        (minus ham belgi hisoblanadi).</li>
    <li><b>Kasr ham, oʻnli son ham</b> qabul qilinadi.</li>
    <li><b>Aralash son yozilmaydi.</b> Ikki butun yarim — 5/2 yoki 2.5.</li>
    <li>Mingliklarda <b>vergul qoʻyilmaydi</b>.</li>
    <li><b>Dollar va foiz belgisi yozilmaydi.</b></li>
    <li>Javob bittadan koʻp boʻlsa, <b>faqat bittasini</b> yozing.</li>
    <li>Davriy oʻnli son <b>qutini toʻldirishi</b> kerak.</li>
  </ol>
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>kasrni oʻnliga aylantirish kerakmi-yoʻqmi, hal qilasiz;</li>
    <li>davriy sonni qanday yozishni bilasiz;</li>
    <li>aralash son tuzogʻiga tushmaysiz;</li>
    <li>manfiy javobning belgilar sonini sanaysiz.</li>
  </ul>
</div>

<h3>Ikki yarim — uch xil yozuv, ikkitasi toʻgʻri</h3>

<figure class="ps-gridin ps-gridin--ok">
  <div class="ps-gridin__boxes"><span>5</span><span>/</span><span>2</span></div>
  <figcaption>Toʻgʻri — kasr qabul qilinadi (3 belgi).</figcaption>
</figure>

<figure class="ps-gridin ps-gridin--ok">
  <div class="ps-gridin__boxes"><span>2</span><span>.</span><span>5</span></div>
  <figcaption>Toʻgʻri — oʻnli son ham qabul qilinadi.</figcaption>
</figure>

<figure class="ps-gridin ps-gridin--no">
  <div class="ps-gridin__boxes"><span>2</span><span>1</span><span>/</span><span>2</span></div>
  <figcaption>Notoʻgʻri — mashina buni 21/2 deb oʻqiydi.</figcaption>
</figure>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Aralash son — eng qimmat format xatosi</span>
  Qutida boʻsh joy yoʻq, shuning uchun «2» va «1/2» yonma-yon tursa,
  ular <b>yigʻilib ketadi</b>. Yigirma bir yarim — mutlaqo boshqa son.
  Qoida sodda: <b>aralash sonni hech qachon yozmang</b>, uni notoʻgʻri
  kasrga yoki oʻnli songa aylantiring.
</div>

<h3>Davriy son — qutini toʻldiring</h3>

<p>Uchdan ikki 0.6666… boʻladi va u hech qachon tugamaydi. Qoida:
<b>qutida joy borligicha yozing</b>. Qisqartirilgan javob
<b>qabul qilinmaydi</b>.</p>

<figure class="ps-gridin ps-gridin--ok">
  <div class="ps-gridin__boxes"><span>.</span><span>6</span><span>6</span><span>6</span><span>6</span></div>
  <figcaption>Toʻgʻri — beshta belgi, quti toʻla.</figcaption>
</figure>

<figure class="ps-gridin ps-gridin--ok">
  <div class="ps-gridin__boxes"><span>0</span><span>.</span><span>6</span><span>6</span><span>7</span></div>
  <figcaption>Toʻgʻri ham — yaxlitlangan, lekin quti toʻla.</figcaption>
</figure>

<figure class="ps-gridin ps-gridin--no">
  <div class="ps-gridin__boxes"><span>0</span><span>.</span><span>6</span><span>6</span></div>
  <figcaption>Notoʻgʻri — yetarlicha aniq emas.</figcaption>
</figure>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Eng xavfsiz yoʻl — <b>kasrni kasrligicha qoldirish</b>. 2/3 deb yozish
  uch belgi oladi, hech qanday yaxlitlash talab qilmaydi va aniq
  toʻgʻri. Oʻnliga faqat kasr qutiga sigʻmasa oʻting.
</div>

<h3>Yozilmaydigan belgilar</h3>

<figure class="ps-gridin ps-gridin--no">
  <div class="ps-gridin__boxes"><span>1</span><span>,</span><span>2</span><span>0</span><span>0</span></div>
  <figcaption>Notoʻgʻri — mingliklar vergulisiz yoziladi.</figcaption>
</figure>

<figure class="ps-gridin ps-gridin--ok">
  <div class="ps-gridin__boxes"><span>1</span><span>2</span><span>0</span><span>0</span></div>
  <figcaption>Toʻgʻri — vergulsiz, toʻrt belgi.</figcaption>
</figure>

<p>Xuddi shunday: savol dollarda soʻrasa ham <b>$</b> yozilmaydi, foizda
soʻrasa ham <b>%</b> yozilmaydi. Faqat son.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha — bu qoida nega borligini bilib qoʻying</span>
  SAT sonlarni amerikacha yozadi: <b>oʻnli kasr — nuqta, mingliklar —
  vergul</b>. Bizda odat teskarisi. Qutiga vergul yozilsa, mashina uni
  oʻnli belgisi deb ham, ajratgich deb ham qabul qilmaydi — javob
  shunchaki notoʻgʻri boʻladi. Butun kurs boʻyi <b>3.5</b> va
  <b>1,200</b> deb yozilayotganining sababi shu.
</div>

<h3>Manfiy javob va belgilar soni</h3>

<figure class="ps-gridin ps-gridin--ok">
  <div class="ps-gridin__boxes"><span>−</span><span>3</span><span>/</span><span>4</span></div>
  <figcaption>Toʻgʻri — toʻrt belgi, manfiyda oltitagacha ruxsat.</figcaption>
</figure>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">30 s</span></p>
  <div class="ps-stem__q">
    <p>A student's answer to a grid-in question is two and a half. Which
    entry is acceptable?</p>
  </div>
  <ol class="ps-ch">
    <li>2.5</li>
    <li>2 1/2</li>
    <li>2½</li>
    <li>two and a half</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 2.5</p>
      <p>5/2 ham toʻgʻri boʻlar edi. Aralash son, maxsus belgi va soʻz
      qabul qilinmaydi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">2 1/2</span>
  <span class="ps-trap__why">Qogʻozda toʻgʻri, qutida esa 21/2 boʻlib
  oʻqiladi — yaʼni 10.5. Matematika toʻgʻri, ball yoʻq.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">35 s</span></p>
  <div class="ps-stem__q">
    <p>A grid-in answer is one thousand two hundred. Which entry is
    acceptable?</p>
  </div>
  <ol class="ps-ch">
    <li>1200</li>
    <li>1,200</li>
    <li>$1200</li>
    <li>1200.00</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 1200</p>
      <p>Vergul va dollar belgisi qabul qilinmaydi. 1200.00 esa yetti
      belgi — qutiga sigʻmaydi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">1,200</span>
  <span class="ps-trap__why">Aynan biz oʻrgangan amerikacha yozuv —
  lekin u <b>matn ichida</b> toʻgʻri, qutida emas. Ikki joyning ikki
  qoidasi bor.</span>
</div>

<h3>Qachon ehtiyot boʻlish kerak</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Uchta oxirgi nazorat</span>
  <ol>
    <li><b>Belgilarni sanang.</b> Javob 5 tadan oshsa, kasrga
        oʻting yoki yaxlitlang.</li>
    <li><b>Birlikni tekshiring.</b> Savol daqiqada soʻragan boʻlsa,
        soatda yozilgan son notoʻgʻri.</li>
    <li><b>Bittasini yozing.</b> «Ikkita yechimdan birini kiriting»
        deganda ikkalasini yozishga urinmang.</li>
  </ol>
</div>

<h3>Exam English</h3>

<ul class="ps-phrase">
  <li><b>student-produced response</b><span>javobi yoziladigan savol (grid-in)</span></li>
  <li><b>enter your answer</b><span>javobingizni kiriting</span></li>
  <li><b>if more than one answer is possible</b><span>javob bittadan koʻp boʻlsa</span></li>
  <li><b>do not enter symbols</b><span>belgilar yozmang</span></li>
  <li><b>as a fraction or a decimal</b><span>kasr yoki oʻnli son sifatida</span></li>
</ul>

<div class="pe-fix">
  <p class="pe-bad">2 1/2</p>
  <p class="pe-good">5/2 yoki 2.5</p>
  <p class="pe-fix__why">Aralash son qutida yigʻilib ketadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">0.66</p>
  <p class="pe-good">.6666 yoki 0.667</p>
  <p class="pe-fix__why">Davriy son qutini toʻldirishi kerak.</p>
</div>

<h3>Kasrmi yoki oʻnli son? Belgilarni sanang</h3>

<p>Ikkalasi ham qabul qilinadi, lekin ular <b>bir xil xavfsiz emas</b>.
Kasr deyarli har doim qisqaroq va hech qanday yaxlitlash talab
qilmaydi. Quyidagi jadval buni ochiq koʻrsatadi.</p>

<table class="pe-table">
  <tr><th>Javob</th><th>Kasr</th><th>Belgi</th><th>Oʻnli</th><th>Belgi</th></tr>
  <tr><td>yarim</td><td>1/2</td><td>3</td><td>.5</td><td>2</td></tr>
  <tr><td>sakkizdan bir</td><td>1/8</td><td>3</td><td>.125</td><td>4</td></tr>
  <tr><td>uchdan ikki</td><td>2/3</td><td>3</td><td>.6666</td><td>5</td></tr>
  <tr><td>oʻn olttidan besh</td><td>5/16</td><td>4</td><td>.3125</td><td>5</td></tr>
  <tr><td>yigirma ikkidan yetti</td><td>22/7</td><td>4</td>
      <td>3.1428</td><td>6 — sigʻmaydi</td></tr>
</table>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Oxirgi qatorga qarang: oʻnli koʻrinish qutiga <b>sigʻmaydi</b> va
  yaxlitlashga majbur qiladi, kasr esa toʻrtta belgida aniq turibdi.
  Qoida: <b>kasr chiqqan boʻlsa, kasrligicha yozing.</b> Oʻnliga faqat
  javob oʻzi oʻnli boʻlib chiqqanda oʻting.
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Bitta istisno</span>
  Agar savol <b>«rounded to the nearest hundredth»</b> yoki shunga
  oʻxshash aniq talab qoʻysa, kasr emas, aynan soʻralgan oʻnli son
  yoziladi. Savolning talabi har doim bu darsning umumiy
  maslahatidan ustun.
</div>

<h3>«Bittasini kiriting» qoidasi</h3>

<p>Baʼzi grid-in savollarda javob bittadan koʻp boʻladi — masalan
kvadrat tenglamaning ikkala ildizi ham toʻgʻri. Bunday savolda
matnda <b>«if more than one answer is possible, enter only one»</b>
degan jumla turadi. Ikkalasini yozishga urinish javobni buzadi.</p>

<figure class="ps-gridin ps-gridin--ok">
  <div class="ps-gridin__boxes"><span>3</span></div>
  <figcaption>Toʻgʻri — ikki ildizdan biri.</figcaption>
</figure>

<figure class="ps-gridin ps-gridin--no">
  <div class="ps-gridin__boxes"><span>3</span><span>,</span><span>5</span></div>
  <figcaption>Notoʻgʻri — ikkitasi birga yozilgan.</figcaption>
</figure>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu qoida sizga <b>foyda</b> keltiradi: ikkita ildizdan qaysi biri
  osonroq boʻlsa, oʻshani yozing. Musbat ildiz odatda arifmetikasi
  soddaroq — manfiy ishorani yozish ham, sanash ham shart
  boʻlmaydi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  How would you enter three quarters?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">3/4 yoki .75 — ikkalasi ham toʻgʻri.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  How would you enter one third?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">1/3 eng xavfsiz; .3333 ham boʻladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Is 1,050 an acceptable entry?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — vergulsiz: 1050.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  How many characters may a negative answer use?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Oltitagacha — minus belgisi ham
  sanaladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  The question says two values are possible. What do you enter?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Faqat bittasini.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>grid-in</b><span>javobi yoziladigan savol</span></li>
  <li><b>student-produced response</b><span>oʻquvchi yozadigan javob</span></li>
  <li><b>enter</b><span>kiritmoq</span></li>
  <li><b>character</b><span>belgi</span></li>
  <li><b>mixed number</b><span>aralash son</span></li>
  <li><b>improper fraction</b><span>notoʻgʻri kasr</span></li>
  <li><b>repeating decimal</b><span>davriy oʻnli son</span></li>
  <li><b>truncate</b><span>kesib qoldirmoq</span></li>
  <li><b>acceptable</b><span>qabul qilinadigan</span></li>
  <li><b>symbol</b><span>belgi ($ yoki %)</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Aralash son yoʻq</b> — 5/2 yoki 2.5.</li>
    <li>Davriy son <b>qutini toʻldiradi</b>.</li>
    <li><b>Vergul, dollar, foiz yozilmaydi</b> — faqat son.</li>
  </ul>
</div>
""",
    },
]
