# -*- coding: utf-8 -*-
"""Prime Math — BLOK C YAKUNI: darslar 43–44 (koʻphadlar, qisqa koʻpaytirish).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt

Bu batch IKKI darsdan iborat — Blok C (algebra tili, 29–44) shu yerda tugaydi.
  mashqlar — practice/management/commands/_practice_pm_43_44.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_43_44.py

⚠️ Kumulyativ chegaralar:
  • PM-43 — koʻphadlarni qoʻshish, ayirish va koʻpaytirish. Ikki qavsni
    koʻpaytirish shu yerda ochiladi. Boʻlish (koʻphadni koʻphadga) yoʻq;
  • PM-44 — uchta qisqa koʻpaytirish formulasi va ular bilan koʻpaytuvchilarga
    ajratish. Kvadrat tenglama yechish YOʻQ (u Blok D da), uchhadni
    ajratishning umumiy usuli ham yoʻq — faqat toʻliq kvadrat va ayirmalar
    farqi;
  • daraja qonunlari (PM-42) va qavsdan chiqarish (PM-34) faol ishlatiladi.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_43_44.py --author=prime
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
    # PM-43 — koʻphadlar
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-43: Koʻphadlar: qoʻshish, ayirish, koʻpaytirish",
        "category": "math",
        "order": 43,
        "summary": (
            "Bir had, ikki had, koʻphad — nomlari va darajasi. Koʻphadlarni "
            "qoʻshish va ayirish (minusga eʼtibor!) hamda ikki qavsni "
            "koʻpaytirishning toʻrt koʻpaytma qoidasi."
        ),
        "stories": ["Bogʻ maydonini hisoblash"],
        "content": """
<h2>PM-43: Koʻphadlar: qoʻshish, ayirish, koʻpaytirish</h2>

<p>PM-32 da hadlarni ixchamlashni, PM-33 da qavs ochishni oʻrgandik. Endi ularni
birlashtiramiz va butun boshli <b>koʻphad</b>lar bilan ishlaymiz — masalan
3x<sup>2</sup> + 2x − 5. Bu Blok C ning eng «algebracha» darsi, lekin unda bironta
ham yangi qoida yoʻq: hammasi tanish narsalarning birikmasi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>koʻphadning hadlarini va darajasini aniqlaysiz;</li>
    <li>koʻphadlarni qoʻshasiz va ayirasiz;</li>
    <li>bir hadni koʻphadga koʻpaytirasiz;</li>
    <li>ikki qavsni koʻpaytirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki qavsni koʻpaytirish</span>
  <span class="pe-chip pe-chip--o">har had</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--s">har had</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">toʻrtta koʻpaytma</span>
</div>

<h3>1. Nomlari va darajasi</h3>

<p>Hadlar soniga qarab nom beriladi, eng katta koʻrsatkich esa koʻphadning
<b>darajasi</b> deyiladi.</p>

<div class="pe-table-wrap"><table>
  <tr><th>Yozuv</th><th>Nomi</th><th>Darajasi</th></tr>
  <tr><td>5x</td><td>bir had</td><td>1</td></tr>
  <tr><td>x<sup>2</sup> + 3</td><td>ikki had</td><td>2</td></tr>
  <tr><td>3x<sup>2</sup> + 2x − 5</td><td>uch had (koʻphad)</td><td>2</td></tr>
  <tr><td>7</td><td>bir had (ozod)</td><td>0</td></tr>
</table></div>

<p>Koʻphad odatda <b>darajalari kamayib borish</b> tartibida yoziladi:
3x<sup>2</sup> + 2x − 5, teskarisi emas. Bu shart emas, lekin shunday yozilgan
koʻphadlarni qoʻshish ham, taqqoslash ham osonroq.</p>

<h3>2. Qoʻshish — oʻxshash hadlarni yigʻish</h3>

<p>Yangi narsa yoʻq: qavslarni ochamiz va oʻxshash hadlarni qoʻshamiz (PM-32).
Qavs oldida plyus turgani uchun ishoralar oʻzgarmaydi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">(3x<sup>2</sup> + 2x − 5) + (x<sup>2</sup> − 4x + 7)</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x<sup>2</sup> + 2x − 5 + x<sup>2</sup> − 4x + 7</span>
    <span class="pm-solve__why">Qavslar shunchaki oʻchirildi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 4x<sup>2</sup> − 2x + 2</span>
    <span class="pm-solve__why">x<sup>2</sup> lar, x lar va sonlar alohida
      qoʻshildi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>x = 2 qoʻyamiz. Boshlangʻich: (12 + 4 − 5) + (4 − 8 + 7) = 11 + 3 = 14.
  Javob: 16 − 4 + 2 = 14 ✓ <b>Koʻphadlar bilan ishlaganda son qoʻyib tekshirish —
  eng tez va eng ishonchli usul.</b></p>
</div>

<h3>3. Ayirish — bu yerda ehtiyot boʻling</h3>

<p>Qavs oldida minus tursa, <b>ichkaridagi hamma ishora almashadi</b> (PM-33). Bu —
butun darsdagi eng koʻp xato qilinadigan joy.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">(5x<sup>2</sup> − 3x + 4) − (2x<sup>2</sup> + x − 6)</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5x<sup>2</sup> − 3x + 4 − 2x<sup>2</sup> − x + 6</span>
    <span class="pm-solve__why">Ikkinchi qavsdagi UCHALA ishora ham almashdi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 3x<sup>2</sup> − 4x + 10</span>
    <span class="pm-solve__why">Oʻxshash hadlar yigʻildi</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Uchinchi ishora ham almashadi</p>
  <p>Koʻpchilik birinchi hadning ishorasini almashtiradi, keyin esa eski ishoralarni
  koʻchirib yozib yuboradi. Yozishdan oldin ikkinchi qavsning <b>har bir hadi</b>ni
  barmoq bilan koʻrsatib chiqing: −2x<sup>2</sup>, −x, +6. Uchtasi ham
  oʻzgarishi shart.</p>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>x = 2: boshlangʻich (20 − 6 + 4) − (8 + 2 − 6) = 18 − 4 = 14; javob
  12 − 8 + 10 = 14 ✓</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Faqat oʻxshash hadlar qoʻshiladi</p>
  <p>x<sup>2</sup> va x — <b>oʻxshash emas</b>, ular hech qachon birlashmaydi.
  Shuning uchun 4x<sup>2</sup> − 2x + 2 javobi uch hadligicha qoladi va bu toʻliq
  javob. «Yana soddalashtirishim kerakmi?» degan savolga javob: yoʻq, har xil
  darajali hadlar shundayligicha yoziladi.</p>
</div>

<h3>4. Bir hadni koʻphadga koʻpaytirish</h3>

<p>Bu PM-33 dagi taqsimot qonunining oʻzi — faqat endi hadlar darajali. Daraja
qonuni (PM-42) ham shu yerda ishlaydi: x · x = x<sup>2</sup>.</p>

<div class="pe-ex">
  <p class="pe-ex__math">3x(2x − 5) = 6x<sup>2</sup> − 15x</p>
  <p class="pe-ex__uz">3x ni ikkala hadga ham koʻpaytirdik.</p>
  <p class="pe-ex__why">3x · 2x = 6x<sup>2</sup> (sonlar koʻpaytiriladi,
  koʻrsatkichlar qoʻshiladi); 3x · (−5) = −15x.</p>
</div>

<h3>5. Ikki qavsni koʻpaytirish — toʻrtta koʻpaytma</h3>

<p>Birinchi qavsning <b>har bir hadi</b> ikkinchi qavsning <b>har bir hadi</b>ga
koʻpaytiriladi. Ikki hadli qavslar boʻlsa, toʻrtta koʻpaytma chiqadi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 200" role="img" aria-label="Toʻrtburchak yuzasi toʻrtta boʻlakka ajratilgan">
    <rect class="pm-fill" x="40" y="30" width="240" height="140"/>
    <line class="pm-ln" x1="200" y1="30" x2="200" y2="170"/>
    <line class="pm-ln" x1="40" y1="120" x2="280" y2="120"/>
    <rect class="pm-ln" x="40" y="30" width="240" height="140" fill="none"/>
    <text class="pm-lbl" x="120" y="20" text-anchor="middle">x</text>
    <text class="pm-lbl" x="240" y="20" text-anchor="middle">2</text>
    <text class="pm-lbl" x="28" y="80" text-anchor="middle">x</text>
    <text class="pm-lbl" x="28" y="150" text-anchor="middle">3</text>
    <text class="pm-lbl pm-lbl--hl" x="120" y="80" text-anchor="middle">x²</text>
    <text class="pm-lbl" x="240" y="80" text-anchor="middle">2x</text>
    <text class="pm-lbl" x="120" y="150" text-anchor="middle">3x</text>
    <text class="pm-lbl" x="240" y="150" text-anchor="middle">6</text>
  </svg>
  <figcaption>Tomonlari (x + 2) va (x + 3) boʻlgan toʻrtburchak toʻrtta boʻlakka
  ajraladi: x² + 2x + 3x + 6.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">(x + 2)(x + 3)</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x·x + x·3 + 2·x + 2·3</span>
    <span class="pm-solve__why">Toʻrtta koʻpaytma — hech biri tushib
      qolmasin</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x<sup>2</sup> + 3x + 2x + 6</span>
    <span class="pm-solve__why">Har koʻpaytma hisoblandi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= x<sup>2</sup> + 5x + 6</span>
    <span class="pm-solve__why">Oʻrtadagi ikki had oʻxshash — yigʻildi</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Rasm — bu yuza</p>
  <p>Yuqoridagi chizmada toʻrtburchakning yuzasi ikki xil yoʻl bilan yozildi: butun
  holda (x + 2)(x + 3), boʻlaklab esa x<sup>2</sup> + 5x + 6. Ular teng, chunki
  bitta yuza. Formulani unutsangiz, shu rasmni chizing.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">(2x − 1)(x + 4) = 2x<sup>2</sup> + 8x − x − 4 =
    2x<sup>2</sup> + 7x − 4</p>
  <p class="pe-ex__uz">Manfiy had ham xuddi shunday koʻpaytiriladi.</p>
  <p class="pe-ex__why">x = 2 da tekshiruv: 3 × 6 = 18 va 8 + 14 − 4 = 18 ✓</p>
</div>

<h3>Matnli masala</h3>

<p><b>Bogʻ maydoni.</b> Toʻgʻri toʻrtburchak shaklidagi bogʻning eni <b>x</b> metr,
boʻyi esa enidan <b>5 metr</b> uzun. Egasi bogʻni har tomondan <b>3 metr</b>ga
kengaytirmoqchi emas — u faqat <b>eni tomonga</b> 3 metr qoʻshadi.</p>

<p><b>Savol:</b> yangi bogʻning yuzasini koʻphad koʻrinishida yozing. x = 10 metr
boʻlsa, yuza qancha?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Yangi eni: x + 3; boʻyi: x + 5</span>
    <span class="pm-solve__why">Faqat eni oʻzgardi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">S = (x + 3)(x + 5)</span>
    <span class="pm-solve__why">Yuza — tomonlar koʻpaytmasi (PM-35)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= x<sup>2</sup> + 5x + 3x + 15</span>
    <span class="pm-solve__why">Toʻrtta koʻpaytma</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= x<sup>2</sup> + 8x + 15; x = 10 → 195 m<sup>2</sup></span>
    <span class="pm-solve__why">100 + 80 + 15 = 195</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Toʻgʻridan-toʻgʻri: eni 13 m, boʻyi 15 m; 13 × 15 = 195 m<sup>2</sup> ✓
  Ikkala yoʻl bir xil javob berdi. Eski bogʻning yuzasi esa 10 × 15 = 150
  m<sup>2</sup> edi — kengaytirish 45 m<sup>2</sup> qoʻshdi.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Tomonlari 13 va 15 — ikkalasi ham 14 atrofida, demak yuza 14 × 14 = 196
  ga yaqin boʻlishi kerak. 195 — mos.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">(5x<sup>2</sup> − 3x) − (2x<sup>2</sup> + x) =
    5x<sup>2</sup> − 3x − 2x<sup>2</sup> + x</p>
  <p class="pe-fix__good">= 5x<sup>2</sup> − 3x − 2x<sup>2</sup> − x</p>
  <p class="pe-fix__why">Ikkinchi hadning ishorasi almashmagan. Qavs oldidagi minus
  ichkaridagi <b>hamma</b> hadga tegishli.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">(x + 2)(x + 3) = x<sup>2</sup> + 6</p>
  <p class="pe-fix__good">= x<sup>2</sup> + 5x + 6</p>
  <p class="pe-fix__why">Faqat ikkita koʻpaytma olingan, oʻrtadagi ikkitasi tushib
  qolgan. Tekshirish: x = 1 da chapda 3 × 4 = 12, notoʻgʻri javobda esa 7.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">3x · 2x = 6x</p>
  <p class="pe-fix__good">3x · 2x = 6x<sup>2</sup></p>
  <p class="pe-fix__why">Sonlar koʻpaytiriladi, koʻrsatkichlar esa qoʻshiladi
  (PM-42): x · x = x<sup>2</sup>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. (2x<sup>2</sup> + 3x) + (x<sup>2</sup> − x) ni
  ixchamlang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3x<sup>2</sup> + 2x.</b> x<sup>2</sup> lar: 2 + 1 = 3; x lar:
    3 − 1 = 2.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. (4x<sup>2</sup> − 2x + 1) − (x<sup>2</sup> − 5x + 3) ni
  ixchamlang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3x<sup>2</sup> + 3x − 2.</b> Ishoralar: −x<sup>2</sup>, +5x, −3.
    Tekshirish x = 1 da: (4 − 2 + 1) − (1 − 5 + 3) = 3 − (−1) = 4 va
    3 + 3 − 2 = 4 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 2x(3x + 4) qavsini oching.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>6x<sup>2</sup> + 8x.</b> 2x · 3x = 6x<sup>2</sup> va 2x · 4 = 8x.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. (x + 4)(x + 2) ni koʻpaytiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>x<sup>2</sup> + 6x + 8.</b> Toʻrtta koʻpaytma: x<sup>2</sup>, 2x, 4x, 8;
    oʻrtadagilar yigʻiladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Xonaning eni x metr, boʻyi undan 2 metr uzun. Gilam uchun
  har tomondan 1 metrdan boʻsh joy qoldirilsa, gilamning yuzasi qanday yoziladi?
  x = 5 boʻlsa hisoblang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>(x − 2)(x) = x<sup>2</sup> − 2x; x = 5 da 15 m<sup>2</sup>.</b> Har
    tomondan 1 metr qoldirilsa, eni x − 2, boʻyi (x + 2) − 2 = x boʻladi.
    Tekshirish: 3 × 5 = 15 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Koʻphad</b><span>bir necha haddan tuzilgan ifoda; ingl. polynomial</span></li>
  <li><b>Bir had</b><span>yolgʻiz had, masalan 5x; ingl. monomial</span></li>
  <li><b>Ikki had</b><span>ikkita hadli ifoda; ingl. binomial</span></li>
  <li><b>Daraja (koʻphadning)</b><span>eng katta koʻrsatkich; ingl. degree</span></li>
  <li><b>Ozod had</b><span>harfsiz son; ingl. constant term</span></li>
  <li><b>Bosh koeffitsient</b><span>eng katta darajali haddagi son; ingl. leading
    coefficient</span></li>
  <li><b>Taqsimot qonuni</b><span>a(b + c) = ab + ac; ingl. distributive law</span></li>
  <li><b>Standart koʻrinish</b><span>darajalar kamayib borish tartibi; ingl.
    standard form</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Qoʻshishda qavs shunchaki oʻchadi</b>, ayirishda esa hamma ishora
      almashadi.</li>
    <li><b>Ikki qavs — toʻrtta koʻpaytma:</b> har had har hadga.</li>
    <li><b>Javobni son qoʻyib tekshiring</b> — x = 1 yoki x = 2 yetarli.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-44 — qisqa koʻpaytirish formulalari
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-44: Qisqa koʻpaytirish formulalari va koʻpaytuvchilarga ajratish",
        "category": "math",
        "order": 44,
        "summary": (
            "Uchta formula: yigʻindining kvadrati, ayirmaning kvadrati va "
            "kvadratlar ayirmasi. Ular bilan ogʻzaki hisoblash va koʻphadni "
            "koʻpaytuvchilarga ajratish."
        ),
        "stories": ["Ustaning tez hisoblash hiylasi"],
        "content": """
<h2>PM-44: Qisqa koʻpaytirish formulalari va koʻpaytuvchilarga ajratish</h2>

<p>102 ni kvadratga koʻtaring. Ustunda koʻpaytirsangiz bir daqiqa ketadi. Formulani
bilsangiz — besh sekund: 10 000 + 400 + 4 = <b>10 404</b>. Bu darsdagi uchta
formula ana shunday ishlaydi: ular hech qanday yangi matematika emas, faqat
<b>oldindan bajarilgan</b> koʻpaytirish.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>uchta qisqa koʻpaytirish formulasini bilasiz;</li>
    <li>ularni ogʻzaki hisobda ishlatasiz;</li>
    <li>teskari yoʻnalishda — koʻpaytuvchilarga ajratasiz;</li>
    <li>(a + b)<sup>2</sup> nima uchun a<sup>2</sup> + b<sup>2</sup> emasligini
      tushunasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uchta formula</span>
  <span class="pe-chip pe-chip--o">(a + b)<sup>2</sup> = a<sup>2</sup> + 2ab +
    b<sup>2</sup></span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">(a − b)<sup>2</sup> = a<sup>2</sup> − 2ab +
    b<sup>2</sup></span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">(a − b)(a + b) = a<sup>2</sup> −
    b<sup>2</sup></span>
</div>

<h3>1. Formulalar qayerdan chiqadi</h3>

<p>Hech narsani yodlash shart emas — uchalasi ham PM-43 dagi «toʻrtta koʻpaytma»
qoidasidan chiqadi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">(a + b)<sup>2</sup> = (a + b)(a + b)</span>
    <span class="pm-solve__why">Kvadrat — oʻziga koʻpaytirish</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= a<sup>2</sup> + ab + ba + b<sup>2</sup></span>
    <span class="pm-solve__why">Toʻrtta koʻpaytma</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= a<sup>2</sup> + 2ab + b<sup>2</sup></span>
    <span class="pm-solve__why">Oʻrtadagi ikkitasi bir xil — ular 2ab beradi</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">(a + b)<sup>2</sup> hech qachon a<sup>2</sup> +
    b<sup>2</sup> emas</p>
  <p>Bu — butun maktab algebrasidagi eng mashhur xato. Oʻrtadagi <b>2ab</b> hadi
  yoʻqolib qoladi. Sonlar bilan tekshiring: (3 + 4)<sup>2</sup> = 49, lekin
  3<sup>2</sup> + 4<sup>2</sup> = 25. Farq 24 — bu aynan 2 × 3 × 4.</p>
</div>

<p>Uchinchi formula esa eng chiroylisi, chunki unda oʻrta had <b>qisqarib
ketadi</b>:</p>

<div class="pe-ex">
  <p class="pe-ex__math">(a − b)(a + b) = a<sup>2</sup> + ab − ba −
    b<sup>2</sup> = a<sup>2</sup> − b<sup>2</sup></p>
  <p class="pe-ex__uz">Kvadratlar ayirmasi — faqat ikkita had qoladi.</p>
  <p class="pe-ex__why">+ab va −ba bir-birini yoʻq qiladi.</p>
</div>

<h3>2. Formulalarni qoʻllash</h3>

<div class="pe-table-wrap"><table>
  <tr><th>Ifoda</th><th>Formula</th><th>Natija</th></tr>
  <tr><td>(x + 3)<sup>2</sup></td><td>yigʻindining kvadrati</td>
      <td>x<sup>2</sup> + 6x + 9</td></tr>
  <tr><td>(x − 4)<sup>2</sup></td><td>ayirmaning kvadrati</td>
      <td>x<sup>2</sup> − 8x + 16</td></tr>
  <tr><td>(x − 5)(x + 5)</td><td>kvadratlar ayirmasi</td>
      <td>x<sup>2</sup> − 25</td></tr>
  <tr><td>(2x + 1)<sup>2</sup></td><td>yigʻindining kvadrati</td>
      <td>4x<sup>2</sup> + 4x + 1</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Oʻrta had — ikkitasining koʻpaytmasi, ikki barobar</p>
  <p>(x + 3)<sup>2</sup> da oʻrta had 2 × x × 3 = 6x. (2x + 1)<sup>2</sup> da esa
  2 × 2x × 1 = 4x. Chetdagi ikki hadni koʻpaytiring va ikkilang — oʻrta had shu.</p>
</div>

<h3>3. Ogʻzaki hisob — formulaning eng shirin qoʻllanishi</h3>

<p>Bu formulalar harflar uchun emas, <b>sonlar</b> uchun ham ishlaydi. Va aynan shu
yerda ular ajoyib hiylaga aylanadi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">102<sup>2</sup> = (100 + 2)<sup>2</sup></span>
    <span class="pm-solve__why">Yumaloq son va kichik qoʻshimchaga ajratdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= 10 000 + 2·100·2 + 4</span>
    <span class="pm-solve__why">a<sup>2</sup> + 2ab + b<sup>2</sup></span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 10 404</span>
    <span class="pm-solve__why">Hammasi ogʻzaki — qogʻoz kerak boʻlmadi</span>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">98<sup>2</sup> = (100 − 2)<sup>2</sup> = 10 000 − 400 + 4
    = 9604</p>
  <p class="pe-ex__uz">Ayirmaning kvadrati — oʻrta had manfiy.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">51 × 49 = (50 + 1)(50 − 1) = 2500 − 1 = 2499</p>
  <p class="pe-ex__uz">Ikki son bir yumaloq sondan teng uzoqlikda boʻlsa,
  kvadratlar ayirmasi ishlaydi.</p>
  <p class="pe-ex__why">Bu — usta va sotuvchilarning eng mashhur hisob hiylasi.</p>
</div>

<h3>4. Teskari yoʻnalish — koʻpaytuvchilarga ajratish</h3>

<p>Formulalarni <b>oʻngdan chapga</b> oʻqisangiz, koʻphadni koʻpaytmaga
aylantirasiz. Bu PM-34 dagi qavsdan chiqarishning davomi.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Kvadratlar ayirmasi</p>
    <p>x<sup>2</sup> − 9 = x<sup>2</sup> − 3<sup>2</sup> =
    <b>(x − 3)(x + 3)</b><br>Ikki had, ikkalasi ham kvadrat, orasida minus.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Toʻliq kvadrat</p>
    <p>x<sup>2</sup> + 6x + 9 = <b>(x + 3)<sup>2</sup></b><br>Chetdagilar kvadrat,
    oʻrta had esa ularning ikkilangan koʻpaytmasi.</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Avval kvadratlar ayirmasini qidiring</p>
  <p>Ikki hadli ifodada minus tursa va ikkala had ham kvadrat boʻlsa — bu deyarli
  har doim kvadratlar ayirmasi: x<sup>2</sup> − 25, 4x<sup>2</sup> − 1,
  a<sup>2</sup> − 100. Plyus turgan boʻlsa (x<sup>2</sup> + 9) esa bu formula
  <b>ishlamaydi</b> — bunday ifoda oddiy yoʻl bilan ajratilmaydi.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Kvadrat maydonni kengaytirish.</b> Tomoni <b>a</b> metr boʻlgan kvadrat
maydon bor. Uni bir tomondan <b>3 metr</b>ga uzaytirib, ikkinchi tomondan
<b>3 metr</b>ga qisqartirishdi.</p>

<p><b>Savol:</b> yangi maydonning yuzasi eskisidan katta boʻldimi yoki kichik?
a = 20 boʻlsa, farq qancha?</p>

<p><b>Reja:</b> yangi yuza (a + 3)(a − 3) koʻrinishida — bu kvadratlar ayirmasi
formulasining aynan oʻzi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Eski yuza: a<sup>2</sup></span>
    <span class="pm-solve__why">Kvadratning yuzasi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Yangi yuza: (a + 3)(a − 3) = a<sup>2</sup> − 9</span>
    <span class="pm-solve__why">Kvadratlar ayirmasi formulasi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Farq: a<sup>2</sup> − (a<sup>2</sup> − 9) =
      9 m<sup>2</sup></span>
    <span class="pm-solve__why">Yangi maydon doim 9 m² ga KICHIK</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>a = 20: eski yuza 400 m<sup>2</sup>; yangisi 23 × 17 = 391 m<sup>2</sup>;
  farq 9 ✓ Endi a = 50 ni sinang: 2500 va 53 × 47 = 2491 — yana 9. <b>Tomon
  qancha boʻlishidan qatʼi nazar, yoʻqotish har doim 9 m²</b> — chunki formulada
  a butunlay yoʻqoladi.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Bir tomonga qoʻshib, ikkinchisidan olsangiz, shakl choʻziladi. Choʻzilgan
  toʻrtburchakning yuzasi esa kvadratnikidan doim kichik — javob manfiy tomonga
  chiqishi kerak edi.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">(x + 5)<sup>2</sup> = x<sup>2</sup> + 25</p>
  <p class="pe-fix__good">(x + 5)<sup>2</sup> = x<sup>2</sup> + 10x + 25</p>
  <p class="pe-fix__why">Oʻrta had 2 × x × 5 = 10x tushib qolgan. Tekshirish:
  x = 1 da chapda 36, notoʻgʻri javobda esa 26.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">(x − 4)<sup>2</sup> = x<sup>2</sup> − 8x − 16</p>
  <p class="pe-fix__good">= x<sup>2</sup> − 8x + 16</p>
  <p class="pe-fix__why">Oxirgi had <b>musbat</b>: (−4) × (−4) = +16. Minus faqat
  oʻrta hadda qoladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">x<sup>2</sup> + 9 = (x + 3)(x + 3)</p>
  <p class="pe-fix__good">x<sup>2</sup> + 9 ajratilmaydi; (x + 3)<sup>2</sup> =
    x<sup>2</sup> + 6x + 9</p>
  <p class="pe-fix__why">Kvadratlar <b>ayirmasi</b> ajraladi, yigʻindisi emas.
  Tekshirish: x = 1 da chapda 10, oʻngda esa 16.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. (x + 2)<sup>2</sup> ni yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>x<sup>2</sup> + 4x + 4.</b> Oʻrta had 2 × x × 2 = 4x.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. (x − 6)<sup>2</sup> ni yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>x<sup>2</sup> − 12x + 36.</b> Oxirgi had musbat, oʻrtadagisi manfiy.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. (x − 7)(x + 7) ni yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>x<sup>2</sup> − 49.</b> Kvadratlar ayirmasi — oʻrta had qisqaradi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. x<sup>2</sup> − 16 ni koʻpaytuvchilarga ajrating.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>(x − 4)(x + 4).</b> 16 = 4<sup>2</sup>, orada minus — demak kvadratlar
    ayirmasi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. 103 × 97 ni formuladan foydalanib ogʻzaki hisoblang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>9991.</b> (100 + 3)(100 − 3) = 10 000 − 9 = 9991. Ikki son yuzdan teng
    uzoqlikda turibdi — kvadratlar ayirmasi aynan shu holat uchun.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Qisqa koʻpaytirish formulasi</b><span>oldindan bajarilgan koʻpaytirish;
    ingl. algebraic identity</span></li>
  <li><b>Yigʻindining kvadrati</b><span>(a + b)<sup>2</sup>; ingl. square of a
    sum</span></li>
  <li><b>Ayirmaning kvadrati</b><span>(a − b)<sup>2</sup>; ingl. square of a
    difference</span></li>
  <li><b>Kvadratlar ayirmasi</b><span>a<sup>2</sup> − b<sup>2</sup>; ingl.
    difference of squares</span></li>
  <li><b>Oʻrta had</b><span>2ab — chetdagilarning ikkilangan koʻpaytmasi; ingl.
    middle term</span></li>
  <li><b>Koʻpaytuvchilarga ajratish</b><span>yigʻindini koʻpaytma qilib yozish;
    ingl. factorising</span></li>
  <li><b>Toʻliq kvadrat</b><span>(x + 3)<sup>2</sup> koʻrinishiga keladigan uchhad;
    ingl. perfect square</span></li>
  <li><b>Ayniyat</b><span>har qanday qiymatda rost boʻladigan tenglik; ingl.
    identity</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>(a ± b)<sup>2</sup> da oʻrta had 2ab</b> — uni hech qachon
      unutmang.</li>
    <li><b>Kvadratlar AYIRMASI ajraladi</b>, yigʻindisi ajralmaydi.</li>
    <li><b>Formulalar sonlar uchun ham ishlaydi:</b> 102<sup>2</sup> = 10 404,
      51 × 49 = 2499 — hammasi ogʻzaki.</li>
  </ul>
</div>
""",
    },
]
