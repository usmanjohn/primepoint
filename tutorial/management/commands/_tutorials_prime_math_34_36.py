# -*- coding: utf-8 -*-
"""Prime Math — Blok C, darslar 34–36 (qavsdan chiqarish, formula, tenglama).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt

Uchta oyoq birga yoziladi:
  mashqlar — practice/management/commands/_practice_pm_34_36.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_34_36.py

⚠️ Kumulyativ chegaralar:
  • PM-34 — PM-33 ning teskarisi. EKUB (PM-8) shu yerda qayta ishlaydi;
  • PM-35 — formula: S = v·t oilasi teskari amal bilan chiqariladi,
    tenglama yechish bilan EMAS (u keyingi darsda);
  • PM-36 — BIRINCHI TENGLAMA. Nomaʼlum faqat BIR tomonda; ikki tomonida
    ham nomaʼlumi bor tenglamalar PM-37 da, matnli masalani tenglama bilan
    yechish esa PM-38 da toʻliq ochiladi. Bu darsdagi matnli masala eng
    sodda koʻrinishda (bevosita tenglama beriladi).

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_34_36.py --author=prime
"""

PLAYLIST = {
    "title": "Prime Math",
    "category": "math",
    "description": (
        "Maktab matematikasi noldan — 100 ta dars. Sonlar, kasr va foiz, algebra, "
        "grafik, geometriya, statistika va matnli masalalar. Hammasi oʻzbek tilida, "
        "har bir qoida nega ishlashi tushuntirilgan."
    ),
}

TUTORIALS = [
    # ══════════════════════════════════════════════════════════════════
    # PM-34 — umumiy koʻpaytuvchini qavsdan chiqarish
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-34: Umumiy koʻpaytuvchini qavsdan chiqarish",
        "category": "math",
        "order": 34,
        "summary": (
            "Qavs ochishning teskarisi: 4n + 12 dan 4(n + 3) ga qaytish. Umumiy "
            "koʻpaytuvchini EKUB orqali topish va bu amal ogʻzaki hisobda qanday "
            "yordam berishi."
        ),
        "stories": ["Sinf sovgʻasi"],
        "content": """
<h2>PM-34: Umumiy koʻpaytuvchini qavsdan chiqarish</h2>

<p>Oʻtgan darsda qavsni ochdik: 4(n + 3) = 4n + 12. Endi teskari yoʻlga qaytamiz —
4n + 12 ni koʻrib, undan 4(n + 3) ni yasaymiz. Nega kerak? Chunki qavsli koʻrinish
koʻpincha <b>qisqaroq</b>, <b>tushunarliroq</b> va koʻp hollarda hisoblash ancha
oson boʻladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>hadlarning umumiy koʻpaytuvchisini topasiz;</li>
    <li>uni qavsdan tashqariga chiqarasiz;</li>
    <li>javobni qavsni ochib tekshirasiz;</li>
    <li>bu amalni ogʻzaki hisobda ishlatasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki tomonlama yoʻl</span>
  <span class="pe-chip pe-chip--o">ochish: a(b + c) → ab + ac</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">chiqarish: ab + ac → a(b + c)</span>
</div>

<h3>1. Umumiy koʻpaytuvchi nima</h3>

<p><b>4n + 12</b> ifodasiga qaraymiz. Birinchi had 4 × n, ikkinchisi 4 × 3. Ikkalasida
ham <b>4</b> bor — u <b>umumiy koʻpaytuvchi</b>. Uni qavsdan tashqariga chiqaramiz,
qavs ichida esa har hadning «qolgani» yoziladi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">4n + 12</span>
    <span class="pm-solve__why">Berilgan ifoda</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4 × n + 4 × 3</span>
    <span class="pm-solve__why">Har hadni umumiy koʻpaytuvchi bilan yozdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 4(n + 3)</span>
    <span class="pm-solve__why">Toʻrtni tashqariga, qolganini qavsga</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Qavsni ochamiz (PM-33): 4 × n = 4n va 4 × 3 = 12 ✓ Boshlangʻich ifoda qaytdi.
  <b>Har safar shunday tekshiring</b> — chiqarishning tekshiruvi ochishdir.</p>
</div>

<h3>2. Qaysi sonni chiqaramiz — EKUB</h3>

<p><b>6x + 9</b> da 6 va 9 ning ikkalasi ham 3 ga boʻlinadi. Demak umumiy koʻpaytuvchi
3. Uni topish uchun PM-8 dagi <b>EKUB</b> kerak boʻladi — eng katta umumiy boʻluvchi.</p>

<div class="pe-table-wrap"><table>
  <tr><th>Ifoda</th><th>Koeffitsientlar</th><th>EKUB</th><th>Javob</th></tr>
  <tr><td>6x + 9</td><td>6 va 9</td><td>3</td><td>3(2x + 3)</td></tr>
  <tr><td>10a − 15</td><td>10 va 15</td><td>5</td><td>5(2a − 3)</td></tr>
  <tr><td>8m + 12n</td><td>8 va 12</td><td>4</td><td>4(2m + 3n)</td></tr>
  <tr><td>14x − 21</td><td>14 va 21</td><td>7</td><td>7(2x − 3)</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Eng KATTA umumiy koʻpaytuvchini chiqaring</p>
  <p>8m + 12n ni 2(4m + 6n) deb yozish ham xato emas, lekin ish tugallanmagan: qavs
  ichida yana 2 qolib ketdi. Toʻliq javob — 4(2m + 3n). Qavs ichidagi sonlarning
  umumiy boʻluvchisi qolmasligi kerak.</p>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Qavs ichida hech narsa yoʻqolmaydi</p>
  <p>Har bir hadni umumiy koʻpaytuvchiga boʻlib, natijani qavs ichiga yozasiz. Agar
  had umumiy koʻpaytuvchining oʻziga teng boʻlsa, qavs ichida <b>1</b> qoladi:
  5x + 5 = 5(x + 1). Bir yoʻqolib qolsa, ifoda buziladi.</p>
</div>

<h3>3. Harf ham umumiy boʻlishi mumkin</h3>

<p>Umumiy koʻpaytuvchi faqat son emas — harf ham boʻladi. <b>2a + ab</b> da ikkala
hadda ham <b>a</b> bor.</p>

<div class="pe-ex">
  <p class="pe-ex__math">2a + ab = a(2 + b)</p>
  <p class="pe-ex__uz">Ikkala hadda ham a bor — uni tashqariga chiqardik.</p>
  <p class="pe-ex__why">Tekshirish: a × 2 = 2a va a × b = ab ✓</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">5x + x<sup>2</sup> = x(5 + x)</p>
  <p class="pe-ex__uz">x<sup>2</sup> — bu x × x, demak unda ham bitta x bor.</p>
</div>

<h3>4. Nega bu amal foydali</h3>

<p>Birinchidan, ogʻzaki hisobda. Quyidagini kalkulyatorsiz hisoblang:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">7 × 98 + 7 × 2</span>
    <span class="pm-solve__why">Ikkala hadda ham 7 bor</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= 7(98 + 2)</span>
    <span class="pm-solve__why">Yettini qavsdan chiqardik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 7 × 100 = 700</span>
    <span class="pm-solve__why">Qavs ichi yumaloq songa aylandi</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Bu usul bozorda ham ishlaydi</p>
  <p>Bir kilogramm olma 12 000 soʻm. 8 kg olib, keyin yana 2 kg olsangiz:
  12 000 × 8 + 12 000 × 2 = 12 000 × 10 = <b>120 000</b> soʻm. Ikkita koʻpaytirish
  oʻrniga bitta — va u ham eng osoni.</p>
</div>

<p>Ikkinchidan, keyingi darslarda: qavsli koʻrinish tenglamani yechishni, kasrni
qisqartirishni va formulani oʻzgartirishni osonlashtiradi.</p>

<h3>Matnli masala</h3>

<p><b>Sinf sovgʻasi.</b> 25 nafar oʻquvchi oʻqituvchiga sovgʻa olmoqchi. Har biri
gul uchun a soʻmdan va kitob uchun b soʻmdan qoʻshadi.</p>

<p><b>Savol:</b> yigʻilgan pulni ikki xil koʻrinishda yozing. a = 12 000, b = 8000
boʻlsa, qaysi yoʻl bilan hisoblash qulayroq?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">25a + 25b</span>
    <span class="pm-solve__why">Gulga yigʻilgani va kitobga yigʻilgani</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= 25(a + b)</span>
    <span class="pm-solve__why">25 umumiy koʻpaytuvchi — chiqardik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">a + b = 12 000 + 8000 = 20 000</span>
    <span class="pm-solve__why">Avval bir kishining ulushi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">25 × 20 000 = 500 000 soʻm</span>
    <span class="pm-solve__why">Bitta koʻpaytirish yetdi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Uzun yoʻl: 25 × 12 000 = 300 000 va 25 × 8000 = 200 000; jami 500 000 ✓
  Bir xil javob, lekin ikkita koʻpaytirish. Qavsli koʻrinish nafaqat qisqaroq —
  u <b>hisobning oʻzini</b> osonlashtirdi.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Har kishidan yigirma mingdan, yigirma besh kishi — yarim millionga yaqin.
  Javob mos.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">4x + 12 = 4(x + 12)</p>
  <p class="pe-fix__good">4x + 12 = 4(x + 3)</p>
  <p class="pe-fix__why">Ikkinchi had ham 4 ga boʻlinishi kerak: 12 ÷ 4 = 3. Tekshirish:
  4(x + 12) ochilsa 4x + 48 chiqadi — boshlangʻich ifoda emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">8m + 12n = 2(4m + 6n)</p>
  <p class="pe-fix__good">8m + 12n = 4(2m + 3n)</p>
  <p class="pe-fix__why">Ish yarim qolgan: qavs ichidagi 4 va 6 hali ham 2 ga
  boʻlinadi. Eng katta umumiy koʻpaytuvchini — EKUB(8, 12) = 4 ni chiqaring.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">5x + 10 = 5(x)</p>
  <p class="pe-fix__good">5x + 10 = 5(x + 2)</p>
  <p class="pe-fix__why">Ikkinchi had butunlay yoʻqolib ketgan. Qavsdan chiqarish
  hech nimani yoʻqotmaydi: 10 ÷ 5 = 2 qavs ichida qoladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 3a + 9 dan umumiy koʻpaytuvchini chiqaring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3(a + 3).</b> Tekshirish: 3 × a + 3 × 3 = 3a + 9 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 6x − 15 dan umumiy koʻpaytuvchini chiqaring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3(2x − 5).</b> EKUB(6, 15) = 3; 6 ÷ 3 = 2 va 15 ÷ 3 = 5. Ishora
    saqlanadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 12 + 18y dan umumiy koʻpaytuvchini chiqaring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>6(2 + 3y).</b> EKUB(12, 18) = 6.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 3b + b<sup>2</sup> dan umumiy koʻpaytuvchini chiqaring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>b(3 + b).</b> b<sup>2</sup> — bu b × b, demak ikkala hadda ham b bor.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Bir kishilik chipta 45 000 soʻm. Ertalab 6 ta, kechqurun
  4 ta chipta sotildi. Umumiy koʻpaytuvchini chiqarib, tushumni ogʻzaki hisoblang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>450 000 soʻm.</b> 45 000 × 6 + 45 000 × 4 = 45 000(6 + 4) =
    45 000 × 10 = 450 000. Qavs ichi oʻnga aylandi — hisob bir zumda tugadi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Umumiy koʻpaytuvchi</b><span>hamma hadda uchraydigan koʻpaytuvchi; ingl.
    common factor</span></li>
  <li><b>Qavsdan chiqarish</b><span>umumiy koʻpaytuvchini tashqariga olish; ingl.
    factorising</span></li>
  <li><b>EKUB</b><span>eng katta umumiy boʻluvchi; ingl. greatest common divisor</span></li>
  <li><b>Koʻpaytuvchi</b><span>koʻpaytirishda qatnashuvchi son; ingl. factor</span></li>
  <li><b>Had</b><span>ifodaning qoʻshish belgilari bilan ajratilgan boʻlagi; ingl.
    term</span></li>
  <li><b>Teskari amal</b><span>ochishga — chiqarish; ingl. inverse operation</span></li>
  <li><b>Koʻpaytmaga ajratish</b><span>yigʻindini koʻpaytma koʻrinishida yozish; ingl.
    factorisation</span></li>
  <li><b>Ogʻzaki hisob</b><span>qogʻozsiz hisoblash; ingl. mental arithmetic</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Chiqarish — ochishning teskarisi:</b> ab + ac = a(b + c).</li>
    <li><b>Eng KATTA umumiy koʻpaytuvchini oling</b> — qavs ichida umumiy boʻluvchi
      qolmasin.</li>
    <li><b>Javobni qavsni ochib tekshiring</b> — boshlangʻich ifoda qaytishi
      shart.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-35 — formula bilan ishlash
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-35: Formula bilan ishlash: S = v·t va boshqalar",
        "category": "math",
        "order": 35,
        "summary": (
            "Formula — harflar bilan yozilgan qoida. S = v·t oilasi, uning uchta "
            "koʻrinishi, perimetr va yuza formulalari hamda birliklarni "
            "moslashtirish."
        ),
        "stories": ["Poyezd jadvali va tezlik"],
        "content": """
<h2>PM-35: Formula bilan ishlash: S = v·t va boshqalar</h2>

<p>«Mashina soatiga 80 kilometr yuradi. Uch soatda qancha yoʻl bosadi?» Bu savolga
javob berish uchun hech qanday yangi bilim kerak emas — 80 × 3 = 240. Lekin shu
oddiy hisobni bir marta harflar bilan yozib qoʻysak, u <b>hamma</b> shunday savolga
javob beradigan qoidaga aylanadi. Bunday qoida <b>formula</b> deyiladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>formulaning nima ekanini va nimasi bilan ifodadan farq qilishini bilasiz;</li>
    <li>S = v·t oilasining uchta koʻrinishini ishlatasiz;</li>
    <li>perimetr va yuza formulalarini qoʻllaysiz;</li>
    <li>birliklarni formulaga moslashtirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Yoʻl oilasi</span>
  <span class="pe-chip pe-chip--o">S = v · t</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">v = S ÷ t</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">t = S ÷ v</span>
</div>

<h3>1. Formula — bir marta yozilgan qoida</h3>

<p>Formulada har harf aniq bir <b>miqdor</b>ni bildiradi va u har doim aytib qoʻyiladi.
S — yoʻl (masofa), v — tezlik, t — vaqt. Formulani oʻqish oddiy: <b>yoʻl tezlikni
vaqtga koʻpaytirganga teng</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__math">S = v · t; v = 80 km/soat, t = 3 soat → S = 240 km</p>
  <p class="pe-ex__uz">Soatiga sakson kilometrdan uch soat — ikki yuz qirq kilometr.</p>
  <p class="pe-ex__why">Bu PM-31 dagi oʻrniga qoʻyishning oʻzi, faqat yozuv nomi
  boshqa.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Ifoda, formula va tenglama — uchtasi uch narsa</p>
  <p><b>Ifoda</b> — 3a + 5, u shunchaki yozuv. <b>Formula</b> — S = v·t, u ikki
  miqdor orasidagi doimiy qoida. <b>Tenglama</b> — 3x + 5 = 20, unda nomaʼlum bor va
  uni topish kerak (keyingi dars). Formulada tenglik belgisi bor, lekin u
  «yechiladigan» narsa emas — u <i>ishlatiladi</i>.</p>
</div>

<h3>2. Bitta oila, uchta savol</h3>

<p>S = v · t formulasi uchta savolga javob beradi. Qaysi miqdor nomaʼlum boʻlsa,
oʻshanisini topamiz — buning uchun <b>teskari amal</b> ishlatiladi (PM-4).</p>

<figure class="pm-fig">
  <svg viewBox="0 0 240 200" role="img" aria-label="Yoʻl, tezlik va vaqt uchburchagi">
    <polygon class="pm-fill" points="120,20 20,180 220,180"/>
    <polyline class="pm-ln" points="120,20 20,180 220,180 120,20" fill="none"/>
    <line class="pm-ln pm-ln--dash" x1="60" y1="115" x2="180" y2="115"/>
    <line class="pm-ln pm-ln--dash" x1="120" y1="115" x2="120" y2="180"/>
    <text class="pm-lbl pm-lbl--hl" x="120" y="90" text-anchor="middle">S</text>
    <text class="pm-lbl" x="85" y="160" text-anchor="middle">v</text>
    <text class="pm-lbl" x="160" y="160" text-anchor="middle">t</text>
  </svg>
  <figcaption>Yuqorida S, pastda v va t. Nomaʼlumni yopsangiz, qolgani hisobni
  koʻrsatadi: S yopilsa v × t, v yopilsa S ÷ t.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">S = 240 km, t = 3 soat, v = ?</span>
    <span class="pm-solve__why">Tezlik nomaʼlum</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">v = S ÷ t = 240 ÷ 3</span>
    <span class="pm-solve__why">Koʻpaytirishning teskarisi — boʻlish</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 80 km/soat</span>
    <span class="pm-solve__why">Har soatda 80 kilometr</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Topilgan tezlikni asl formulaga qoʻyamiz: 80 × 3 = 240 ✓ <b>Formula bilan
  ishlaganda tekshiruv har doim shu:</b> javobni asl formulaga qaytaring.</p>
</div>

<h3>3. Boshqa formulalar</h3>

<p>Formulalar hamma joyda. Ularni yodlashdan koʻra <b>oʻqishni</b> bilish muhim.</p>

<div class="pe-table-wrap"><table>
  <tr><th>Formula</th><th>Nimani beradi</th><th>Misol</th></tr>
  <tr><td>S = v · t</td><td>bosib oʻtilgan yoʻl</td><td>80 × 3 = 240 km</td></tr>
  <tr><td>P = 2(a + b)</td><td>toʻgʻri toʻrtburchak perimetri</td>
      <td>2(8 + 5) = 26 sm</td></tr>
  <tr><td>S = a · b</td><td>toʻgʻri toʻrtburchak yuzasi</td>
      <td>8 × 5 = 40 sm<sup>2</sup></td></tr>
  <tr><td>narx = n · p</td><td>n dona mahsulot puli</td>
      <td>6 × 12 000 = 72 000 soʻm</td></tr>
  <tr><td>haq = s · r</td><td>s soat ishlagan ish haqi</td>
      <td>6 × 25 000 = 150 000 soʻm</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Perimetr va yuza — bir shakl, ikki savol</p>
  <p>P = 2(a + b) shaklning <b>atrofi</b>ni beradi va santimetrda oʻlchanadi.
  S = a · b esa <b>ichi</b>ni beradi va santimetr kvadratda oʻlchanadi. Imtihonda
  bu ikkisini almashtirib yuborish eng koʻp uchraydigan geometriya xatosi.</p>
</div>

<h3>4. Birliklar mos kelishi shart</h3>

<p>Formula sonlarni emas, <b>miqdorlarni</b> bogʻlaydi. Tezlik km/soatda boʻlsa, vaqt
ham soatda boʻlishi kerak. Daqiqa berilgan boʻlsa, avval uni soatga aylantiring
(PM-19 dagi kasrlar shu yerda ish beradi).</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">v = 60 km/soat, t = 90 daqiqa</span>
    <span class="pm-solve__why">Birliklar mos emas</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">90 daqiqa = 1,5 soat</span>
    <span class="pm-solve__why">90 ÷ 60 = 1,5 — endi ikkalasi ham soatda</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">S = 60 × 1,5 = 90 km</span>
    <span class="pm-solve__why">Toʻgʻri javob</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Birlikni ham yozib boring</p>
  <p>Hisobda birlikni yonida olib yursangiz, xato oʻzini koʻrsatadi: «60 km/soat × 90
  daqiqa» degan yozuv gʻalati eshitiladi va sizni toʻxtatadi. Javobda birlik boʻlmasa,
  javob ham toʻliq emas.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Poyezd jadvali.</b> Toshkentdan chiqqan tezyurar poyezd 240 kilometrlik yoʻlni
3 soatda bosib oʻtdi. Keyingi bekatgacha yana 400 kilometr bor va poyezd oʻsha
tezlikda yuradi.</p>

<p><b>Savol:</b> poyezdning tezligi qancha va keyingi bekatga necha soatda yetadi?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">v = S ÷ t = 240 ÷ 3</span>
    <span class="pm-solve__why">Avval tezlikni topamiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">v = 80 km/soat</span>
    <span class="pm-solve__why">Har soatda 80 kilometr</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">t = S ÷ v = 400 ÷ 80</span>
    <span class="pm-solve__why">Endi vaqt nomaʼlum — yana teskari amal</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 5 soat</span>
    <span class="pm-solve__why">Keyingi bekatga besh soatda yetadi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>80 × 5 = 400 ✓ Va butun yoʻl: 240 + 400 = 640 km, jami vaqt 3 + 5 = 8 soat;
  640 ÷ 8 = 80 km/soat ✓ Tezlik oʻzgarmagani uchun oʻrtacha tezlik ham oʻsha.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>400 — 240 dan qariyb ikki barobar koʻp, demak vaqt ham 3 soatdan ikki
  barobardan koʻproq boʻlishi kerak. 5 soat — mos.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">S = 240 km, t = 3 soat → v = 240 × 3 = 720</p>
  <p class="pe-fix__good">v = 240 ÷ 3 = 80 km/soat</p>
  <p class="pe-fix__why">Nomaʼlum tezlik boʻlganda boʻlish kerak. Nazorat: tezlik
  butun yoʻldan katta boʻlishi mumkin emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">v = 60 km/soat, t = 30 daqiqa → S = 60 × 30 = 1800 km</p>
  <p class="pe-fix__good">30 daqiqa = 0,5 soat; S = 60 × 0,5 = 30 km</p>
  <p class="pe-fix__why">Birliklar moslashtirilmagan. Yarim soatda 1800 kilometr yurish
  mumkin emas — javobning oʻzi xato ekanini aytib turibdi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Tomonlari 8 va 5 sm: perimetr 8 × 5 = 40 sm</p>
  <p class="pe-fix__good">P = 2(8 + 5) = 26 sm; 40 sm<sup>2</sup> esa yuza</p>
  <p class="pe-fix__why">Yuza formulasi perimetr oʻrniga ishlatilgan. Perimetr —
  atrofi, yuza — ichi; birliklari ham har xil.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. v = 90 km/soat, t = 4 soat. Yoʻlni toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>360 km.</b> S = 90 × 4 = 360.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. S = 270 km, t = 3 soat. Tezlikni toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>90 km/soat.</b> v = 270 ÷ 3 = 90. Tekshirish: 90 × 3 = 270 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. S = 150 km, v = 50 km/soat. Vaqtni toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3 soat.</b> t = 150 ÷ 50 = 3.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Tomonlari 12 sm va 7 sm boʻlgan toʻgʻri toʻrtburchakning
  perimetri va yuzasini toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>P = 38 sm, S = 84 sm<sup>2</sup>.</b> P = 2(12 + 7) = 2 × 19 = 38;
    S = 12 × 7 = 84. Birliklarga eʼtibor bering: biri sm, ikkinchisi sm<sup>2</sup>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Velosipedchi soatiga 15 kilometr tezlik bilan 40 daqiqa
  yurdi. Qancha yoʻl bosdi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>10 km.</b> 40 daqiqa = 40/60 = 2/3 soat; S = 15 × 2/3 = 10 km. Birlikni
    avval moslashtirmasa, 600 degan mantiqsiz javob chiqadi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Formula</b><span>harflar bilan yozilgan doimiy qoida; ingl. formula</span></li>
  <li><b>Miqdor</b><span>oʻlchanadigan kattalik: yoʻl, vaqt, tezlik; ingl.
    quantity</span></li>
  <li><b>Tezlik</b><span>bir soatda bosib oʻtilgan yoʻl; ingl. speed</span></li>
  <li><b>Masofa (yoʻl)</b><span>bosib oʻtilgan uzunlik; ingl. distance</span></li>
  <li><b>Perimetr</b><span>shaklning atrofi uzunligi; ingl. perimeter</span></li>
  <li><b>Yuza</b><span>shaklning ichki oʻlchami; ingl. area</span></li>
  <li><b>Birlik</b><span>oʻlchov nomi: km, soat, sm<sup>2</sup>; ingl. unit</span></li>
  <li><b>Teskari amal</b><span>koʻpaytirishga — boʻlish; ingl. inverse
    operation</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>S = v·t oilasi bitta:</b> nomaʼlum qaysi boʻlsa, teskari amal bilan
      topiladi.</li>
    <li><b>Birliklar mos boʻlsin:</b> km/soat bilan daqiqa ishlamaydi.</li>
    <li><b>Javobni asl formulaga qaytarib tekshiring</b> va birlikni yozing.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-36 — bir nomaʼlumli tenglama
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-36: Bir nomaʼlumli tenglama — muvozanat gʻoyasi",
        "category": "math",
        "order": 36,
        "summary": (
            "Tenglama — tarozi. Ikki tomonga bir xil amal qilib nomaʼlumni yolgʻiz "
            "qoldirish, javobni tekshirish va PM-29 dan beri yozib kelgan "
            "ifodalarni nihoyat yechish."
        ),
        "stories": ["Tarozi muvozanati"],
        "content": """
<h2>PM-36: Bir nomaʼlumli tenglama — muvozanat gʻoyasi</h2>

<p>PM-29 dan beri nomaʼlumni harf bilan yozib kelyapmiz, PM-30 da gapni ifodaga
aylantirdik, PM-31 da unga son qoʻydik. Faqat bitta narsa qolgan edi: <b>nomaʼlumning
oʻzini topish</b>. Mana shu ish tenglama yechish deyiladi — va u kutilganidan ancha
oddiy, chunki uning ortida bitta oddiy narsa turadi: <b>tarozi</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>tenglamani ifodadan ajratasiz;</li>
    <li>muvozanat qoidasini tushunasiz: ikki tomonga bir xil amal;</li>
    <li>bir qadamli va ikki qadamli tenglamalarni yechasiz;</li>
    <li>javobni tenglamaga qoʻyib tekshirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Muvozanat qoidasi</span>
  <span class="pe-chip pe-chip--s">chap tomonga nima qilsang</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">oʻng tomonga ham shuni qil</span>
</div>

<h3>1. Tenglama — muvozanatdagi tarozi</h3>

<p><b>x + 5 = 12</b> yozuvini tarozi deb tasavvur qiling. Chap pallada nomaʼlum ogʻirlik
va 5 kilogramm tosh, oʻng pallada 12 kilogramm. Tarozi tinch turibdi — demak ikki
tomon <b>teng</b>.</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">Chap palla</span>
    <span class="pm-model__bar" style="width:60%">x + 5</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">Oʻng palla</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:60%">12</span>
  </div>
  <p class="pm-model__tot">Ikki palla teng — tenglama shuni bildiradi</p>
</div>

<p>Endi x ni topish uchun uni <b>yolgʻiz qoldirish</b> kerak. Chap palladan 5 kilogramm
toshni olib tashlaymiz. Lekin shunda tarozi ogʻadi! Muvozanatni saqlash uchun
<b>oʻng palladan ham</b> 5 ni olamiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + 5 = 12</span>
    <span class="pm-solve__why">Berilgan tenglama</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + 5 − 5 = 12 − 5</span>
    <span class="pm-solve__why">Ikki tomondan ham 5 ni ayirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 7</span>
    <span class="pm-solve__why">Nomaʼlum yolgʻiz qoldi — yechim topildi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Topilgan sonni asl tenglamaga qoʻyamiz: 7 + 5 = 12 ✓ <b>Tenglama yechilgach
  tekshirish shart emas — u BEPUL.</b> Bir necha sekundda javobingiz toʻgʻri ekaniga
  ishonch hosil qilasiz. Bu odatni birinchi kundan boshlang.</p>
</div>

<h3>2. Teskari amal bilan yolgʻizlash</h3>

<p>Nomaʼlum yonidagi har bir amalni <b>teskarisi</b> bilan yoʻqotamiz. PM-4 dan
bilamiz: qoʻshishning teskarisi — ayirish, koʻpaytirishning teskarisi — boʻlish.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Tenglamada shunday</th><th>Ikki tomonga</th><th>Misol</th></tr>
  <tr><td>x + 5 = 12</td><td class="pm-word__sym">− 5</td><td>x = 7</td></tr>
  <tr><td>x − 3 = 10</td><td class="pm-word__sym">+ 3</td><td>x = 13</td></tr>
  <tr><td>3x = 21</td><td class="pm-word__sym">÷ 3</td><td>x = 7</td></tr>
  <tr><td>x/4 = 3</td><td class="pm-word__sym">× 4</td><td>x = 12</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">«Koʻchirib oʻtkazish» degan qoidani hozircha unuting</p>
  <p>Kattalar koʻpincha «sonni ikkinchi tomonga oʻtkaz, ishorasi almashadi» deb
  oʻrgatadi. Bu qoida toʻgʻri, lekin u <b>natija</b> — muvozanat qoidasining qisqargan
  koʻrinishi. Avval nima uchun shunday boʻlishini tushuning: ikki tomonga bir xil amal
  qilinadi. Shunda hech qachon ishorada adashmaysiz.</p>
</div>

<h3>3. Ikki qadamli tenglamalar</h3>

<p>Nomaʼlum yonida ikkita amal boʻlsa, ularni <b>teskari tartibda</b> yoʻqotamiz:
avval qoʻshish-ayirish, keyin koʻpaytirish-boʻlish. Yaʼni amallar tartibiga
(PM-5) teskari yoʻnalishda yuramiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x + 5 = 20</span>
    <span class="pm-solve__why">Berilgan tenglama</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x = 15</span>
    <span class="pm-solve__why">Ikki tomondan 5 ni ayirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 5</span>
    <span class="pm-solve__why">Ikki tomonni 3 ga boʻldik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>3 × 5 + 5 = 15 + 5 = 20 ✓</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">2x − 7 = 9 → 2x = 16 → x = 8</p>
  <p class="pe-ex__uz">Avval ikki tomonga 7 qoʻshdik, keyin ikkiga boʻldik.</p>
  <p class="pe-ex__why">Tekshirish: 2 × 8 − 7 = 16 − 7 = 9 ✓</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">x/3 + 2 = 6 → x/3 = 4 → x = 12</p>
  <p class="pe-ex__uz">Avval 2 ni ayirdik, keyin ikki tomonni 3 ga koʻpaytirdik.</p>
  <p class="pe-ex__why">Tekshirish: 12 ÷ 3 + 2 = 4 + 2 = 6 ✓</p>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Yechim — bitta son, tenglamani rost qiladigan</p>
  <p>3x + 5 = 20 tenglamasining yechimi 5. Boshqa hech qanday son bu tenglamani
  toʻgʻri qilmaydi: 4 ni qoʻysangiz 17, 6 ni qoʻysangiz 23 chiqadi. Shuning uchun
  yechimni <b>ildiz</b> ham deyishadi — u tenglamaning yagona toʻgʻri qiymati.</p>
</div>

<h3>4. Qavsli tenglama</h3>

<p>Qavs boʻlsa, ikki yoʻl bor va ikkalasi ham toʻgʻri: qavsni ochish (PM-33) yoki ikki
tomonni qavs oldidagi songa boʻlish.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">1-yoʻl: ochamiz</p>
    <p>2(x + 3) = 16<br>2x + 6 = 16<br>2x = 10<br><b>x = 5</b></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">2-yoʻl: boʻlamiz</p>
    <p>2(x + 3) = 16<br>x + 3 = 8<br><b>x = 5</b></p>
  </div>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Oʻng tomon qavs oldidagi songa boʻlinsa — ikkinchi yoʻl qisqa</p>
  <p>16 ÷ 2 = 8 butun chiqdi, shuning uchun boʻlish qulay. Agar 2(x + 3) = 17 boʻlsa,
  ochgan maʼqul — aks holda kasr bilan ishlashga toʻgʻri keladi.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Sinf kassasi.</b> PM-29 da shu ifodani yozgan edik: har bir oʻquvchi 5000
soʻmdan qoʻshadi, sinf rahbari esa 20 000 soʻm qoʻshadi, yaʼni yigʻiladigan pul —
<b>5000n + 20 000</b>. Bugun kassada <b>140 000</b> soʻm bor.</p>

<p><b>Savol:</b> sinfda nechta oʻquvchi bor?</p>

<p><b>Reja:</b> ifodani yigʻilgan pulga tenglashtiramiz — tenglama hosil boʻladi.
Keyin n ni yolgʻizlaymiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">5000n + 20 000 = 140 000</span>
    <span class="pm-solve__why">Ifoda kassadagi pulga teng</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5000n = 120 000</span>
    <span class="pm-solve__why">Ikki tomondan 20 000 ni ayirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">n = 24</span>
    <span class="pm-solve__why">Ikki tomonni 5000 ga boʻldik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>5000 × 24 + 20 000 = 120 000 + 20 000 = 140 000 ✓ Sinfda 24 oʻquvchi bor.
  Diqqat: javob <b>butun son</b> chiqdi — bu ham nazorat, chunki oʻquvchi soni
  kasr boʻlolmaydi.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Rahbarning ulushini olib tashlasak 120 000 qoladi. Har kishi 5000 dan
  qoʻshgan, demak 20 dan koʻproq oʻquvchi bor. 24 — mos.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">x + 5 = 12 → x = 17</p>
  <p class="pe-fix__good">x = 12 − 5 = 7</p>
  <p class="pe-fix__why">Teskari amal oʻrniga oʻsha amal bajarilgan. Yolgʻizlash uchun
  qoʻshishni <b>ayirish</b> bilan yoʻqotamiz. Tekshirish darrov tutadi:
  17 + 5 = 22 ≠ 12.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">3x + 5 = 20 → 3x + 5 − 5 = 20</p>
  <p class="pe-fix__good">3x + 5 − 5 = 20 − 5</p>
  <p class="pe-fix__why">Amal faqat bir tomonga qilingan — tarozi ogʻib ketdi.
  Muvozanat qoidasi buzilsa, tenglik ham buziladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">3x = 21 → x = 21 − 3 = 18</p>
  <p class="pe-fix__good">x = 21 ÷ 3 = 7</p>
  <p class="pe-fix__why">3x — bu 3 × x, demak teskari amal <b>boʻlish</b>. Qoʻshish
  boʻlmagan joyda ayirishning ishi yoʻq.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. x + 8 = 15 tenglamani yeching.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>x = 7.</b> Ikki tomondan 8 ni ayirdik. Tekshirish: 7 + 8 = 15 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 4x = 36 tenglamani yeching.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>x = 9.</b> Ikki tomonni 4 ga boʻldik. Tekshirish: 4 × 9 = 36 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 5x − 4 = 31 tenglamani yeching.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>x = 7.</b> Avval 4 ni qoʻshdik: 5x = 35; keyin 5 ga boʻldik.
    Tekshirish: 5 × 7 − 4 = 31 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 3(x − 2) = 18 tenglamani yeching.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>x = 8.</b> Ikki tomonni 3 ga boʻlamiz: x − 2 = 6, demak x = 8. Yoki qavsni
    ochib: 3x − 6 = 18 → 3x = 24 → x = 8. Tekshirish: 3 × 6 = 18 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Afsona 3 ta bir xil daftar oldi va 24 000 soʻm toʻladi.
  Bitta daftarning narxini tenglama bilan toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>8000 soʻm.</b> Bitta daftar narxi x boʻlsin: 3x = 24 000. Ikki tomonni
    3 ga boʻlamiz: x = 8000. Tekshirish: 3 × 8000 = 24 000 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Tenglama</b><span>ikki ifoda tenglik bilan bogʻlangan yozuv; ingl.
    equation</span></li>
  <li><b>Nomaʼlum</b><span>topilishi kerak boʻlgan son; ingl. unknown</span></li>
  <li><b>Yechim (ildiz)</b><span>tenglamani toʻgʻri qiladigan qiymat; ingl.
    solution</span></li>
  <li><b>Muvozanat</b><span>ikki tomonning tengligi; ingl. balance</span></li>
  <li><b>Yolgʻizlash</b><span>nomaʼlumni bir tomonda yolgʻiz qoldirish; ingl.
    isolating</span></li>
  <li><b>Teskari amal</b><span>qoʻshishga — ayirish, koʻpaytirishga — boʻlish; ingl.
    inverse operation</span></li>
  <li><b>Tenglamani yechish</b><span>nomaʼlumni topish; ingl. solving</span></li>
  <li><b>Tekshirish</b><span>javobni tenglamaga qoʻyib sinash; ingl.
    verification</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Tenglama — tarozi:</b> bir tomonga qilingan amal ikkinchisiga ham
      qilinadi.</li>
    <li><b>Teskari amal bilan yolgʻizlang:</b> avval qoʻshish-ayirish, keyin
      koʻpaytirish-boʻlish.</li>
    <li><b>Javobni har doim tekshiring</b> — bu bir necha sekund va toʻliq
      ishonch.</li>
  </ul>
</div>
""",
    },
]
