# -*- coding: utf-8 -*-
"""Prime Math — darslar 69–71 (yuza 2, doira va π, aylana uzunligi va yuza).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt
**Blok E: Geometriya** — har bir darsda SVG chizma SHART.

  mashqlar — practice/management/commands/_practice_pm_69_71.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_69_71.py

⚠️ Chizmalar QOʻLDA hisoblanmagan: _svgkit.py + scratchpad/gen_pm69_71.py
   bilan generatsiya qilingan va qlmanage bilan koʻz bilan tekshirilgan.
   verify_pm_69_71.py ularni qaytadan oʻlchaydi (parallelogrammning
   koʻchirilgan uchburchagi haqiqatan toʻgʻri toʻrtburchak beradimi,
   trapetsiyaning ikki uchburchagi 20 va 12 mi, doiraning boʻlaklari
   terilganda eni π × r ga yaqinmi).

⚠️ Kumulyativ chegaralar:
  • PM-69 — parallelogramm, romb, trapetsiya va murakkab shakl yuzasi.
    ⛔ Aylana, doira va π (PM-70/71) bu darsda YOʻQ;
  • PM-70 — faqat DOIRANING QISMLARI va π ning maʼnosi (π = L ÷ d).
    ⛔ L = 2πr va S = πr² formulalari sifatida PM-71 da beriladi; bu
    darsda faqat taʼrifning oʻzi ishlatiladi (arqonni oʻlchab, d ni
    topish). Doira YUZASI bu darsda umuman yoʻq;
  • PM-71 — ikkala formula ham. S = πr² sektorlarga kesish orqali
    tushuntiriladi (eni π × r, boʻyi r).
  • ⛔ Oʻxshashlik (PM-72), simmetriya (PM-73), hajm (PM-74) YOʻQ.
  • ⛔ Oʻrta arifmetik ATAMASI yoʻq (PM-78) — trapetsiyada «ikkala
    asosning yigʻindisini ikkiga boʻlamiz» deyiladi, «oʻrtachasi» emas.
  • Faol ishlatiladi: yuza 1 (PM-68) — parallelogramm ham, trapetsiya
    ham unga qaytariladi; perimetr (PM-67); toʻrtburchaklar oilasi
    (PM-66); oʻnlik kasr (PM-20/21); yaxlitlash (PM-14); foiz (PM-23);
    kvadrat va ildiz (PM-13); tenglama (PM-36).

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_69_71.py --author=prime
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
    # PM-69 — yuza 2: parallelogramm, trapetsiya, murakkab shakllar
    # ══════════════════════════════════════════════════════════════════
    {
        "title": ("PM-69: Yuza 2: parallelogramm, trapetsiya va murakkab "
                  "shakllar"),
        "category": "math",
        "order": 69,
        "summary": (
            "Har qanday shaklning yuzasi oxir-oqibat toʻgʻri toʻrtburchakka "
            "qaytariladi. Parallelogramm, romb va trapetsiya yuzasi qayerdan "
            "chiqqanini koʻrasiz va murakkab shaklni boʻlaklarga ajratasiz."
        ),
        "stories": ["Notekis dala"],
        "content": """
<h2>PM-69: Yuza 2: parallelogramm, trapetsiya va murakkab shakllar</h2>

<p>Dalalar toʻgʻri toʻrtburchak boʻlmaydi. Tomorqaning bir tomoni ariqqa
qarab qiyshayadi, ikkinchisi yoʻlga tekkan joyida torayadi. Shunday
yerning yuzasini qanday hisoblaymiz?</p>

<p>Javob bitta va u juda chiroyli: <b>har qanday shaklni kesib, siljitib,
toʻgʻri toʻrtburchakka aylantiramiz</b>. Yuza esa kesish-siljitishdan
oʻzgarmaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>parallelogramm yuzasi nega S = a × h ekanini isbotlaysiz;</li>
    <li>trapetsiya formulasini yoddan emas, chizmadan chiqarasiz;</li>
    <li>rombni diagonallari orqali hisoblaysiz;</li>
    <li>murakkab shaklni boʻlaklarga ajratib yoki ortiqchasini ayirib
      topasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Parallelogramm</span>
  <span class="pe-chip pe-chip--s">S</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">a</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--o">h</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Trapetsiya</span>
  <span class="pe-chip pe-chip--s">S</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">(a + b)</span>
  <span class="pe-op">÷ 2 ×</span>
  <span class="pe-chip pe-chip--o">h</span>
</div>

<h3>1. Parallelogramm: bitta uchburchakni koʻchirsak boʻldi</h3>

<p>Parallelogrammning qarama-qarshi tomonlari parallel va teng (PM-66).
Uning yuzasini topish uchun hech qanday yangi gʻoya kerak emas — faqat
qaychi kerak.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 205" role="img" aria-label="Parallelogrammning chap uchburchagi kesilib oʻng tomonga koʻchiriladi">
    <polygon class="pm-fill" points="60,175 220,175 260,75 100,75"/>
    <polyline class="pm-ln" points="60,175 220,175 260,75 100,75 60,175" fill="none"/>
    <line class="pm-ln pm-ln--dash" x1="100" y1="75" x2="100" y2="175"/>
    <polyline class="pm-ln pm-ln--dash" points="220,175 260,175 260,75" fill="none"/>
    <polyline class="pm-ln" points="100,162 113,162 113,175" fill="none"/>
    <polygon class="pm-pt" points="208,140 196.9,144.5 196.9,135.5"/>
    <line class="pm-ln pm-ln--dash" x1="118" y1="140" x2="205" y2="140"/>
    <text class="pm-lbl" x="128" y="196">a = 8 sm</text>
    <text class="pm-lbl pm-lbl--hl" x="106" y="118">h = 5 sm</text>
    <text class="pm-lbl" x="136" y="161">koʻchirdik</text>
  </svg>
  <figcaption>Chap tomondagi uchburchakni kesib olib, oʻng tomonga
  qoʻysak, aynan shu yuzali toʻgʻri toʻrtburchak hosil boʻladi.</figcaption>
</figure>

<p>Chizmadagi uchburchakni kesib, oʻng tomonga koʻchirdik. Shakl
oʻzgardi, lekin <b>yuza oʻzgarmadi</b> — hech nima qoʻshilmadi va hech
nima yoʻqolmadi. Qolgani esa oddiy toʻgʻri toʻrtburchak (PM-68):</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">S = a × h</span>
    <span class="pm-solve__why">Hosil boʻlgan toʻgʻri toʻrtburchakning
    tomonlari</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">S = 8 × 5 = 40 sm<sup>2</sup></span>
    <span class="pm-solve__why">Asos 8 sm, balandlik 5 sm</span>
  </div>
</div>

<p>Bu yerda <b>h</b> — <b>balandlik</b>, yaʼni asosdan qarama-qarshi
tomongacha boʻlgan <b>perpendikulyar</b> masofa. Chizmada u punktir
chiziq bilan koʻrsatilgan.</p>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Yon tomon — balandlik EMAS</p>
  <p>Parallelogrammning qiya yon tomoni har doim balandlikdan
  <b>uzunroq</b>, chunki u qiya turadi. Agar yon tomonni formulaga
  qoʻysangiz, yuza haqiqatdan katta chiqadi. Chizmadagi shaklning yon
  tomoni taxminan 6 sm, balandligi esa 5 sm: 8 × 6 = 48 emas,
  8 × 5 = <b>40</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">S = 12 × 4,5 = 54 sm<sup>2</sup></p>
  <p class="pe-ex__uz">Asosi 12 santimetr, balandligi 4,5 santimetr
  boʻlgan parallelogrammning yuzasi — 54 kvadrat santimetr.</p>
  <p class="pe-ex__why">12 × 4 = 48 va 12 × 0,5 = 6; 48 + 6 = 54
  (PM-21).</p>
</div>

<p>Teskari masala ham xuddi shunday ishlaydi — formula tenglamaga
aylanadi (PM-36):</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">S = 60 sm<sup>2</sup>, a = 12 sm</span>
    <span class="pm-solve__why">Berilgan; balandlik nomaʼlum</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">12 × h = 60</span>
    <span class="pm-solve__why">Formulani qoʻydik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">h = 60 ÷ 12 = 5 sm</span>
    <span class="pm-solve__why">Ikki tomonni 12 ga boʻldik</span>
  </div>
</div>

<h3>2. Romb: diagonallar orqali</h3>

<p>Romb ham parallelogramm (PM-66), demak unga ham S = a × h ishlaydi.
Lekin rombning balandligini oʻlchash noqulay — uning oʻrniga
<b>diagonallari</b> beriladi.</p>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Rombning yuzasi</p>
  <p>S = d<sub>1</sub> × d<sub>2</sub> ÷ 2 — diagonallarining
  koʻpaytmasining yarmi.</p>
</div>

<p>Nega yarmi? Rombni tashqaridan oʻrab turgan toʻgʻri toʻrtburchakni
tasavvur qiling: uning tomonlari aynan d<sub>1</sub> va d<sub>2</sub>.
Romb esa oʻsha toʻrtburchakning roppa-rosa yarmini egallaydi — xuddi
uchburchak oʻzini oʻragan toʻrtburchakning yarmini egallagani kabi
(PM-68).</p>

<div class="pe-ex">
  <p class="pe-ex__math">S = 8 × 6 ÷ 2 = 24 sm<sup>2</sup></p>
  <p class="pe-ex__uz">Diagonallari 8 va 6 santimetr boʻlgan rombning
  yuzasi — 24 kvadrat santimetr.</p>
</div>

<h3>3. Trapetsiya: bitta diagonal hamma ishni qiladi</h3>

<p>Trapetsiyada faqat bitta juft tomon parallel (PM-66). Ularni
<b>asoslar</b> deymiz va a hamda b deb belgilaymiz. Formulani yodlash
shart emas — diagonal chizsak, oʻzi chiqadi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 205" role="img" aria-label="Trapetsiya diagonal bilan ikkita uchburchakka boʻlinadi">
    <polygon class="pm-fill" points="50,170 250,170 210,90"/>
    <polygon class="pm-fill pm-fill--hl" points="50,170 210,90 90,90"/>
    <polyline class="pm-ln" points="50,170 250,170 210,90 90,90 50,170" fill="none"/>
    <line class="pm-ln pm-ln--hl" x1="50" y1="170" x2="210" y2="90"/>
    <line class="pm-ln pm-ln--dash" x1="90" y1="90" x2="90" y2="170"/>
    <polyline class="pm-ln" points="90,157 103,157 103,170" fill="none"/>
    <text class="pm-lbl" x="128" y="82">b = 6</text>
    <text class="pm-lbl" x="126" y="192">a = 10</text>
    <text class="pm-lbl pm-lbl--hl" x="95" y="124">h = 4</text>
    <text class="pm-lbl" x="158" y="152">20</text>
    <text class="pm-lbl" x="118" y="116">12</text>
  </svg>
  <figcaption>Diagonal trapetsiyani ikkita uchburchakka boʻladi.
  Ikkalasining balandligi bir xil — h.</figcaption>
</figure>

<p>Diagonal trapetsiyani ikkita uchburchakka boʻldi. Diqqat qiling:
<b>ikkalasining balandligi ham bir xil</b> — asoslar parallel boʻlgani
uchun ular orasidagi masofa hamma joyda bitta (PM-60).</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Pastki uchburchak: (10 × 4) ÷ 2 = 20</span>
    <span class="pm-solve__why">Asosi a = 10, balandligi h = 4
    (PM-68)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Yuqori uchburchak: (6 × 4) ÷ 2 = 12</span>
    <span class="pm-solve__why">Asosi b = 6, balandligi oʻsha h = 4</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">S = 20 + 12 = 32 sm<sup>2</sup></span>
    <span class="pm-solve__why">Ikkalasini qoʻshdik</span>
  </div>
</div>

<p>Endi xuddi shu hisobni harflar bilan yozamiz va qavsdan umumiy
narsani chiqaramiz (PM-34):</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">S = (a × h) ÷ 2 + (b × h) ÷ 2</span>
    <span class="pm-solve__why">Ikkita uchburchak</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">S = (a + b) ÷ 2 × h</span>
    <span class="pm-solve__why">h ham, ikkiga boʻlish ham ikkalasida bor
    edi</span>
  </div>
</div>

<p>Yaʼni: <b>ikkala asosni qoʻshamiz, ikkiga boʻlamiz, balandlikka
koʻpaytiramiz</b>. Tekshiramiz: (10 + 6) ÷ 2 × 4 = 8 × 4 = 32 ✓ —
chizmadagi javobning oʻzi.</p>

<div class="pe-ex">
  <p class="pe-ex__math">(14 + 10) ÷ 2 × 6 = 12 × 6 = 72 m<sup>2</sup></p>
  <p class="pe-ex__uz">Asoslari 14 va 10 metr, balandligi 6 metr boʻlgan
  trapetsiyaning yuzasi — 72 kvadrat metr.</p>
  <p class="pe-ex__why">Avval qavs ichi, keyin boʻlish, oxirida
  koʻpaytirish — amallar tartibi (PM-5).</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Trapetsiyada balandlik — yon tomon emas</p>
  <p>Trapetsiyaning qiya yon tomoni koʻpincha berilgan boʻladi va u
  odamni chalgʻitadi. Formulaga faqat <b>ikkita parallel tomon orasidagi
  perpendikulyar masofa</b> qoʻyiladi. Chizmada u punktir bilan
  tushirilgan va uning ostida toʻgʻri burchak belgisi turadi — shuni
  qidiring.</p>
</div>

<h3>4. Murakkab shakllar: boʻlaklarga ajrating</h3>

<p>Hayotdagi shakllarning nomi boʻlmaydi. Lekin ularni deyarli har doim
tanish boʻlaklarga ajratish mumkin.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 215" role="img" aria-label="Toʻgʻri toʻrtburchak ustiga trapetsiya qoʻyilgan murakkab shakl">
    <polygon class="pm-fill" points="60,190 260,190 260,110 60,110"/>
    <polygon class="pm-fill pm-fill--hl" points="60,110 260,110 220,50 100,50"/>
    <polyline class="pm-ln" points="60,190 260,190 260,110 220,50 100,50 60,110 60,190" fill="none"/>
    <line class="pm-ln pm-ln--dash" x1="60" y1="110" x2="260" y2="110"/>
    <line class="pm-ln pm-ln--dash" x1="100" y1="50" x2="100" y2="110"/>
    <polyline class="pm-ln" points="100,97 113,97 113,110" fill="none"/>
    <polyline class="pm-ln" points="60,177 73,177 73,190" fill="none"/>
    <text class="pm-lbl" x="139" y="209">10 sm</text>
    <text class="pm-lbl" x="18" y="155">4 sm</text>
    <text class="pm-lbl" x="140" y="42">6 sm</text>
    <text class="pm-lbl pm-lbl--hl" x="107" y="86">3 sm</text>
    <text class="pm-lbl" x="176" y="156">40</text>
    <text class="pm-lbl" x="176" y="90">24</text>
  </svg>
  <figcaption>Bitta gorizontal chiziq shaklni tanish ikkita boʻlakka
  ajratdi: toʻgʻri toʻrtburchak va trapetsiya.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Pastki qism: 10 × 4 = 40 sm<sup>2</sup></span>
    <span class="pm-solve__why">Toʻgʻri toʻrtburchak (PM-68)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Yuqori qism: (10 + 6) ÷ 2 × 3 = 24 sm<sup>2</sup></span>
    <span class="pm-solve__why">Trapetsiya: asoslari 10 va 6, balandligi
    3</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">S = 40 + 24 = 64 sm<sup>2</sup></span>
    <span class="pm-solve__why">Boʻlaklarni qoʻshdik</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Ikki yoʻl bor</p>
  <p><b>Qoʻshish:</b> shaklni boʻlaklarga ajratib, yuzalarini
  qoʻshasiz. <b>Ayirish:</b> shaklni katta toʻgʻri toʻrtburchak ichiga
  joylab, ortiqcha qismni ayirasiz. Ikkalasi ham toʻgʻri javob beradi —
  qaysi biri kamroq hisob talab qilsa, oʻshanisini tanlang.</p>
</div>

<h3>Matnli masala</h3>

<p>Karim akaning dalasi toʻgʻri toʻrtburchak emas. Uning ikkita tomoni
parallel: biri yoʻlga qaragan va uzunligi 40 metr, ikkinchisi ariqqa
qaragan va uzunligi 24 metr. Ular orasidagi masofa 30 metr. Dalaga
bugʻdoy ekiladi va har 100 kvadrat metrga 2 kilogramm urugʻ ketadi.
Urugʻ 5 kilogrammli qoplarda sotiladi.</p>

<p><b>Nechta qop urugʻ sotib olish kerak?</b></p>

<p><b>Reja:</b> dala trapetsiya — yuzasini topamiz, urugʻ miqdorini
hisoblaymiz, keyin qoplar soniga oʻtamiz.</p>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Agar dala 40 × 30 boʻlganida 1200 m<sup>2</sup> chiqardi. Ikkinchi
  tomoni qisqaroq, demak javob 1200 dan kam boʻlishi kerak — 900–1000
  atrofida.</span>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">40 + 24 = 64</span>
    <span class="pm-solve__why">Ikkala asosni qoʻshdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">64 ÷ 2 = 32</span>
    <span class="pm-solve__why">Ikkiga boʻldik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">32 × 30 = 960 m<sup>2</sup></span>
    <span class="pm-solve__why">Balandlikka koʻpaytirdik — dalaning
    yuzasi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">960 ÷ 100 × 2 = 19,2 kg</span>
    <span class="pm-solve__why">Har 100 m<sup>2</sup> ga 2 kg</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">19,2 ÷ 5 = 3,84 → 4 qop</span>
    <span class="pm-solve__why">Qopni boʻlib sotib boʻlmaydi — yuqoriga
    yaxlitladik (PM-14)</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>960 m<sup>2</sup> — taxminimizdagi 900–1000 oraligʻida ✓
  <br>4 qop = 4 × 5 = 20 kg, bu 19,2 kg dan koʻp ✓ (3 qop = 15 kg
  boʻlardi va yetmasdi)
  <br><b>Javob:</b> 4 qop urugʻ.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Parallelogramm: asosi 8, yon tomoni 6 →
  S = 8 × 6 = 48</p>
  <p class="pe-fix__good">S = 8 × 5 = 40 sm<sup>2</sup></p>
  <p class="pe-fix__why">Yon tomon qiya turadi va balandlikdan uzun.
  Formulaga faqat <b>perpendikulyar</b> balandlik qoʻyiladi — chizmada
  toʻgʻri burchak belgisi turgan joy.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Trapetsiya: (10 + 6) × 4 = 64</p>
  <p class="pe-fix__good">(10 + 6) ÷ 2 × 4 = 32 sm<sup>2</sup></p>
  <p class="pe-fix__why">Ikkiga boʻlish qadami tushib qolgan. 64 —
  trapetsiyani ikki nusxada olib yasalgan parallelogrammning yuzasi,
  yaʼni javobdan aynan ikki barobar katta.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Trapetsiya: 10 × 4 = 40</p>
  <p class="pe-fix__good">(10 + 6) ÷ 2 × 4 = 32 sm<sup>2</sup></p>
  <p class="pe-fix__why">Faqat bitta asos ishlatilgan. Trapetsiyaning
  eni pastda va tepada har xil — shuning uchun <b>ikkalasi</b> ham
  hisobga olinadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Murakkab shakl: 10 × 4 + 6 × 3 = 40 + 18 = 58</p>
  <p class="pe-fix__good">40 + 24 = 64 sm<sup>2</sup></p>
  <p class="pe-fix__why">Yuqoridagi boʻlak toʻgʻri toʻrtburchak emas,
  trapetsiya. Uning pastki eni 10, yuqorigisi 6 — ikkalasi ham
  kerak.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Parallelogrammning asosi 9 sm, balandligi
  6 sm. Yuzasi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>54 sm<sup>2</sup>.</b> S = 9 × 6 = 54.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Parallelogrammning yuzasi 84 sm<sup>2</sup>,
  balandligi 7 sm. Asosi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>12 sm.</b> a × 7 = 84, demak a = 84 ÷ 7 = 12. Tekshirish:
    12 × 7 = 84 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Trapetsiyaning asoslari 12 sm va 8 sm,
  balandligi 5 sm. Yuzasi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>50 sm<sup>2</sup>.</b> (12 + 8) ÷ 2 × 5 = 20 ÷ 2 × 5 =
    10 × 5 = 50.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Rombning diagonallari 10 sm va 7 sm. Yuzasi
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>35 sm<sup>2</sup>.</b> S = 10 × 7 ÷ 2 = 70 ÷ 2 = 35.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Shakl pastdan 8 m × 5 m toʻgʻri toʻrtburchak,
  uning ustida esa asoslari 8 m va 4 m, balandligi 3 m boʻlgan
  trapetsiya. Butun shaklning yuzasi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>58 m<sup>2</sup>.</b> Pastki qism: 8 × 5 = 40 m<sup>2</sup>.
    Yuqori qism: (8 + 4) ÷ 2 × 3 = 6 × 3 = 18 m<sup>2</sup>. Jami:
    40 + 18 = 58 m<sup>2</sup>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Dilnozaning bogʻi trapetsiya shaklida: parallel
  tomonlari 18 m va 12 m, ular orasidagi masofa 10 m. Bogʻga koʻchat oʻt
  yotqiziladi, har kvadrat metri 12 000 soʻm. Hammasi necha soʻm
  boʻladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>1 800 000 soʻm.</b> Avval yuza: (18 + 12) ÷ 2 × 10 =
    15 × 10 = 150 m<sup>2</sup>. Keyin narx: 150 × 12 000 =
    1 800 000 soʻm. Diqqat: 18 × 10 = 180 m<sup>2</sup> deb hisoblasangiz,
    360 000 soʻm ortiqcha toʻlaysiz.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Parallelogramm</b><span>qarama-qarshi tomonlari parallel
    toʻrtburchak; ingl. parallelogram</span></li>
  <li><b>Asos</b><span>yuzani hisoblashda tayanch qilib olingan tomon;
    ingl. base</span></li>
  <li><b>Balandlik</b><span>asosga perpendikulyar masofa; ingl.
    height</span></li>
  <li><b>Trapetsiya</b><span>faqat bitta juft tomoni parallel
    toʻrtburchak; ingl. trapezium</span></li>
  <li><b>Trapetsiyaning asoslari</b><span>uning parallel ikki tomoni;
    ingl. parallel sides</span></li>
  <li><b>Romb</b><span>toʻrtala tomoni teng parallelogramm; ingl.
    rhombus</span></li>
  <li><b>Diagonal</b><span>qarama-qarshi uchlarni tutashtiruvchi kesma;
    ingl. diagonal</span></li>
  <li><b>Murakkab shakl</b><span>bir nechta oddiy shakldan tuzilgan
    shakl; ingl. composite shape</span></li>
  <li><b>Boʻlaklarga ajratish</b><span>shaklni tanish qismlarga boʻlish
    usuli; ingl. decomposition</span></li>
  <li><b>Perpendikulyar</b><span>toʻgʻri burchak ostida turgan; ingl.
    perpendicular</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Kesish va siljitish yuzani oʻzgartirmaydi — hamma formula
      shundan chiqadi.</li>
    <li>Parallelogramm: S = a × h. Balandlik — yon tomon emas.</li>
    <li>Romb: S = d<sub>1</sub> × d<sub>2</sub> ÷ 2.</li>
    <li>Trapetsiya: S = (a + b) ÷ 2 × h — ikkala asos ham kerak.</li>
    <li>Murakkab shaklni boʻlaklarga ajrating yoki ortiqchasini
      ayiring.</li>
    <li>Javobni har doim taxmin bilan solishtiring: yuza oʻzini oʻragan
      toʻgʻri toʻrtburchakdan katta boʻlolmaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-70 — doira va aylana; π qayerdan chiqqan
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-70: Doira va aylana; π qayerdan chiqqan",
        "category": "math",
        "order": 70,
        "summary": (
            "Aylana bilan doira bir narsa emas. Markaz, radius, diametr, "
            "vatar va yoy nima ekanini, hamda dunyodagi har qanday aylanada "
            "bir xil chiqadigan sirli son — π ni koʻrasiz."
        ),
        "stories": ["Arqon, gʻildirak va π ning tarixi"],
        "content": """
<h2>PM-70: Doira va aylana; π qayerdan chiqqan</h2>

<p>Gʻildirak, tarelka, non, soat, tanga, quduq ogʻzi. Odam yasagan
narsalarning eng foydalisi — dumaloq narsa. Uni oʻlchash uchun esa
butun bir son kifoya qilmaydi.</p>

<p>Bu darsda biz shu sonni topamiz. U taxminan 3,14 ga teng va uning
tarixi toʻrt ming yil davom etadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>aylana bilan doirani bir-biridan ajratasiz;</li>
    <li>markaz, radius, diametr, vatar va yoyni nomlaysiz;</li>
    <li>d = 2r munosabatini ikki tomonga ham ishlatasiz;</li>
    <li>π nima ekanini va u qayerdan chiqqanini bilib olasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Doirada</span>
  <span class="pe-chip pe-chip--o">d</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">2 ×</span>
  <span class="pe-chip pe-chip--o">r</span>
  <span class="pe-op">va</span>
  <span class="pe-chip pe-chip--s">π</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">L ÷ d</span>
  <span class="pe-op">≈</span>
  <span class="pe-chip pe-chip--s">3,14</span>
</div>

<h3>1. Aylana va doira — bir narsa emas</h3>

<p>Ikkalasi ham dumaloq, lekin ular boshqa-boshqa narsalar. Farqi
xuddi perimetr bilan yuzaning farqi kabi (PM-67, PM-68).</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 170" role="img" aria-label="Chapda aylana, oʻngda boʻyalgan doira">
    <circle class="pm-ln pm-ln--hl" cx="85" cy="78" r="55" fill="none"/>
    <circle class="pm-fill--hl" cx="235" cy="78" r="55"/>
    <circle class="pm-ln" cx="235" cy="78" r="55" fill="none"/>
    <text class="pm-lbl pm-lbl--hl" x="42" y="158">Aylana — chiziq</text>
    <text class="pm-lbl" x="184" y="158">Doira — chiziq va ichi</text>
  </svg>
  <figcaption>Aylana — faqat chegara chizigʻi. Doira — oʻsha chiziq va
  uning ichidagi hamma nuqta.</figcaption>
</figure>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Ikki taʼrif</p>
  <p><b>Aylana</b> — markazdan bir xil uzoqlikda turgan nuqtalardan
  tuzilgan <b>chiziq</b>.
  <br><b>Doira</b> — aylana va uning <b>ichidagi hamma joy</b>.</p>
</div>

<p>Hovlini tasavvur qiling: panjara — aylana, hovlining oʻzi — doira.
Panjara metrlab oʻlchanadi, hovli esa kvadrat metrlab.</p>

<h3>2. Doiraning qismlari</h3>

<figure class="pm-fig">
  <svg viewBox="0 0 320 215" role="img" aria-label="Doira: markaz, radius, diametr, vatar va yoy">
    <circle class="pm-ln" cx="160" cy="105" r="78" fill="none"/>
    <path class="pm-ln pm-ln--hl" d="M 204.7 41.1 A 78 78 0 0 0 115.3 41.1" fill="none"/>
    <line class="pm-ln" x1="82" y1="105" x2="238" y2="105"/>
    <line class="pm-ln pm-ln--hl" x1="160" y1="105" x2="204.7" y2="41.1"/>
    <line class="pm-ln" x1="96.1" y1="149.7" x2="223.9" y2="149.7"/>
    <circle class="pm-pt" cx="160" cy="105" r="3.5"/>
    <text class="pm-lbl" x="149" y="122">O</text>
    <text class="pm-lbl pm-lbl--hl" x="193" y="63">r</text>
    <text class="pm-lbl" x="96" y="98">d = 2r</text>
    <text class="pm-lbl" x="140" y="167">vatar</text>
    <text class="pm-lbl pm-lbl--hl" x="148" y="18">yoy</text>
  </svg>
  <figcaption>Markaz O, radius r, diametr d, vatar va yoy — doiraning
  besh atamasi.</figcaption>
</figure>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Atama</th><th>Bu nima</th><th>Belgisi</th></tr>
  <tr><td>Markaz</td><td>hamma nuqtadan bir xil uzoqlikdagi nuqta</td>
    <td class="pm-word__sym">O</td></tr>
  <tr><td>Radius</td><td>markazdan aylanagacha boʻlgan kesma</td>
    <td class="pm-word__sym">r</td></tr>
  <tr><td>Diametr</td><td>markazdan oʻtib, aylanani kesib oʻtuvchi kesma</td>
    <td class="pm-word__sym">d</td></tr>
  <tr><td>Vatar</td><td>aylananing ikki nuqtasini tutashtiruvchi kesma</td>
    <td class="pm-word__sym">—</td></tr>
  <tr><td>Yoy</td><td>aylananing bir boʻlagi</td>
    <td class="pm-word__sym">—</td></tr>
</table></div>

<p>Diametr — eng uzun vatar, chunki u markazdan oʻtadi. Va u aynan
ikkita radiusdan iborat:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">d = 2 × r</span>
    <span class="pm-solve__why">Diametr ikkita radius</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">r = d ÷ 2</span>
    <span class="pm-solve__why">Teskarisi ham shunday</span>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">r = 7 sm → d = 2 × 7 = 14 sm</p>
  <p class="pe-ex__uz">Radiusi 7 santimetr boʻlgan doiraning diametri —
  14 santimetr.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">d = 30 sm → r = 30 ÷ 2 = 15 sm</p>
  <p class="pe-ex__uz">Diametri 30 santimetr boʻlgan tarelkaning radiusi —
  15 santimetr.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Radiusni diametr bilan chalkashtirmang</p>
  <p>Masalada koʻpincha bittasi berilib, ikkinchisi soʻraladi. Yozib
  qoʻying: <b>radius kichik, diametr katta</b> — diametr ikki barobar.
  Agar javobingiz berilgan sondan kichik chiqishi kerak boʻlsa-yu, katta
  chiqsa, ikkalasini almashtirib yuborgansiz.</p>
</div>

<h3>3. Tajriba: har doim uch yarim marta emas, uch butun oʻn toʻrt</h3>

<p>Oddiy tajriba. Uch xil dumaloq narsani oling. Har birining
<b>diametrini</b> chizgʻich bilan, <b>aylanasining uzunligini</b> esa ip
bilan oʻlchang (ipni oʻrab chiqib, keyin uni yozib oʻlchang). Soʻng
uzunlikni diametrga boʻling.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Buyum</th><th>Diametr d</th><th>Aylana uzunligi L</th>
    <th>L ÷ d</th></tr>
  <tr><td>Stakan</td><td>8 sm</td><td>25,1 sm</td>
    <td class="pm-word__sym">3,14</td></tr>
  <tr><td>Tarelka</td><td>24 sm</td><td>75,4 sm</td>
    <td class="pm-word__sym">3,14</td></tr>
  <tr><td>Gʻildirak</td><td>60 sm</td><td>188,5 sm</td>
    <td class="pm-word__sym">3,14</td></tr>
</table></div>

<p>Buyumlar butunlay boshqa, oʻlchamlari boshqa — lekin oxirgi ustun
bir xil. Bu tasodif emas.</p>

<div class="pe-call pe-rule">
  <p class="pe-call__t">π ning taʼrifi</p>
  <p>Dunyodagi <b>har qanday</b> aylananing uzunligi oʻz diametridan
  necha marta katta boʻlsa, oʻsha son — <b>π</b> (pi deb oʻqiladi).
  <br>π = L ÷ d ≈ <b>3,14</b></p>
</div>

<p>Demak har qanday dumaloq narsaning atrofi uning enidan biroz
kamroq uch yarim marta uzun. Ipni gʻildirakka oʻrasangiz, u
diametrning uch nusxasidan sal koʻproq ketadi.</p>

<h3>4. π ning tarixi</h3>

<p>Bu son biror kishi tomonidan oʻylab topilmagan — u <b>topilgan</b>,
va uni topishga toʻrt ming yil ketgan.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Qachon</th><th>Kim</th><th>π uchun olingan qiymat</th></tr>
  <tr><td>~1800-yil m.a.</td><td>Bobil</td>
    <td class="pm-word__sym">3,125</td></tr>
  <tr><td>~1650-yil m.a.</td><td>Misr, Ahmes papirusi</td>
    <td class="pm-word__sym">3,16</td></tr>
  <tr><td>~250-yil m.a.</td><td>Arximed</td>
    <td class="pm-word__sym">3,1408 … 3,1429</td></tr>
  <tr><td>1424-yil</td><td>Jamshid al-Koshiy, Samarqand</td>
    <td class="pm-word__sym">16 xonagacha aniq</td></tr>
</table></div>

<p>Arximed hiyla ishlatgan: aylananing ichiga va tashqarisiga koʻp
tomonli shakllar chizgan. Ichkaridagi shaklning perimetri aylanadan
kichik, tashqaridagisiniki katta — demak π shu ikkisining orasida.
Tomonlar sonini 96 taga yetkazib, u π ni ikki tomondan siqib
qoʻygan.</p>

<p>Eng hayratlanarlisi bizga yaqin joyda boʻlgan. <b>Jamshid
al-Koshiy</b> Samarqandda, Ulugʻbek rasadxonasida ishlagan va 1424-yilda
π ni 16 xona aniqlikda hisoblab chiqqan. Bu rekord dunyoda qariyb 180
yil buzilmagan.</p>

<div class="pe-call pe-tip">
  <p class="pe-call__t">π hech qachon tugamaydi</p>
  <p>π = 3,14159265… — uning oʻnlik yozuvi cheksiz va hech qachon
  takrorlanmaydi. Uni hech qanday kasr bilan aniq yozib boʻlmaydi.
  Shuning uchun uni harf bilan belgilashadi: yozib boʻlmaydigan sonning
  nomi.</p>
</div>

<h3>5. Amalda qanday ishlatiladi</h3>

<p>Hisobda π oʻrniga <b>3,14</b> olinadi — maktab uchun ham, usta uchun
ham shu kifoya. Baʼzan <sup>22</sup>/<sub>7</sub> ham ishlatiladi:
22 ÷ 7 = 3,142857… — u ham 3,14 ga juda yaqin.</p>

<p>π = L ÷ d degani shuni ham bildiradi: agar aylananing uzunligini
bilsak, <b>diametrni topa olamiz</b> — buning uchun uzunlikni π ga
boʻlish kerak.</p>

<div class="pe-ex">
  <p class="pe-ex__math">L = 157 sm, d = 157 ÷ 3,14 = 50 sm</p>
  <p class="pe-ex__uz">Atrofi 157 santimetr boʻlgan doiraning diametri —
  50 santimetr.</p>
  <p class="pe-ex__why">Tekshirish: 50 × 3,14 = 157 ✓</p>
</div>

<h3>Matnli masala</h3>

<p>Maktabga dumaloq stol sovgʻa qilishdi. Uni oʻlchash uchun Sherbek
stolning chetidan ip oʻrab chiqdi va ipni yozib oʻlchadi: 314
santimetr. Sinf eshigining eni 90 santimetr.</p>

<p><b>Stol eshikdan tik holatda oʻtadimi?</b></p>

<p><b>Reja:</b> ip — aylananing uzunligi. Undan diametrni topamiz va
eshikning eni bilan solishtiramiz.</p>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Atrofi diametrdan taxminan 3 marta uzun, demak diametr 314 ning
  uchdan biri atrofida — 100 ga yaqin.</span>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">L = 314 sm</span>
    <span class="pm-solve__why">Ip — aylananing uzunligi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">d = L ÷ π = 314 ÷ 3,14</span>
    <span class="pm-solve__why">π = L ÷ d munosabatini teskari
    oʻgirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">d = 100 sm</span>
    <span class="pm-solve__why">Stolning eni bir metr</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">100 &gt; 90 — oʻtmaydi</span>
    <span class="pm-solve__why">Stol eshikdan 10 santimetrga keng</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>100 × 3,14 = 314 ✓ — ipning uzunligi joyida.
  <br><b>Javob:</b> tik holatda oʻtmaydi; stolni yonboshlatib kiritish
  kerak. Uning radiusi esa 100 ÷ 2 = 50 sm.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">d = 10 sm, demak r = 20 sm</p>
  <p class="pe-fix__good">r = 10 ÷ 2 = 5 sm</p>
  <p class="pe-fix__why">Diametr — kattasi, radius — kichigi. Diametr
  ikkita radiusdan iborat, teskarisi emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">π = 3,14 — aniq shuncha</p>
  <p class="pe-fix__good">π ≈ 3,14</p>
  <p class="pe-fix__why">3,14 — bu faqat yaxlitlangan qiymat (PM-14).
  π ning oʻzi cheksiz: 3,14159265… Shuning uchun javoblar ham
  taxminiy chiqadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Doiraning uzunligi 157 sm</p>
  <p class="pe-fix__good">Aylananing uzunligi 157 sm</p>
  <p class="pe-fix__why">Uzunlik chiziqqa tegishli, yaʼni aylanaga.
  Doira — yuzasi bor shakl. Panjara uzun boʻladi, hovli emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">L = 157, d = 50 → π = 50 ÷ 157 = 0,32</p>
  <p class="pe-fix__good">π = 157 ÷ 50 = 3,14</p>
  <p class="pe-fix__why">Boʻlish teskari qilingan. π 1 dan katta:
  aylana har doim diametrdan uzun, aksincha emas.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Doiraning radiusi 9 sm. Diametri qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>18 sm.</b> d = 2 × 9 = 18.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Doiraning diametri 26 m. Radiusi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>13 m.</b> r = 26 ÷ 2 = 13.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Aylananing uzunligi 157 sm, diametri 50 sm.
  L ni d ga boʻlsangiz nima chiqadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3,14 — yaʼni π.</b> 157 ÷ 50 = 3,14. Qanday aylana olsangiz
    ham, natija oʻsha boʻladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <sup>22</sup>/<sub>7</sub> ni oʻnlik kasrga
  aylantiring. U π ga yaqinmi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3,142857… — ha, juda yaqin.</b> 22 ÷ 7 = 3,142857…, π esa
    3,141592… Farqi mingdan bir ulushdan ham kam, shuning uchun uni
    qadimda π oʻrnida ishlatishgan.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Quduq ogʻzining atrofi 219,8 sm. Uning
  diametri qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>70 sm.</b> d = 219,8 ÷ 3,14 = 70. Tekshirish:
    70 × 3,14 = 219,8 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Bekzod dumaloq gilam sotib olmoqchi. Sotuvchi
  «radiusi 80 sm» dedi. Xonaning boʻsh joyi esa 1,5 metr. Gilam bu joyga
  sigʻadimi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Sigʻmaydi.</b> Gilam qancha joy egallashini radius emas,
    <b>diametr</b> koʻrsatadi: d = 2 × 80 = 160 sm. Boʻsh joy esa
    1,5 m = 150 sm. 160 &gt; 150, demak 10 santimetrga sigʻmaydi.
    Faqat radiusga qarab «80 &lt; 150, sigʻadi» deyish — eng koʻp
    uchraydigan xato.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Aylana</b><span>markazdan bir xil uzoqlikdagi nuqtalar chizigʻi;
    ingl. circle</span></li>
  <li><b>Doira</b><span>aylana va uning ichi; ingl. disc</span></li>
  <li><b>Markaz</b><span>doiraning oʻrtasidagi nuqta; ingl.
    centre</span></li>
  <li><b>Radius</b><span>markazdan aylanagacha masofa; ingl.
    radius</span></li>
  <li><b>Diametr</b><span>markazdan oʻtgan eng uzun kesma, d = 2r; ingl.
    diameter</span></li>
  <li><b>Vatar</b><span>aylananing ikki nuqtasini tutashtiruvchi kesma;
    ingl. chord</span></li>
  <li><b>Yoy</b><span>aylananing bir boʻlagi; ingl. arc</span></li>
  <li><b>Aylana uzunligi</b><span>aylananing atrofi, L; ingl.
    circumference</span></li>
  <li><b>π (pi)</b><span>aylana uzunligining diametrga nisbati, ≈ 3,14;
    ingl. pi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Aylana — chiziq, doira — chiziq va uning ichi.</li>
    <li>d = 2r va r = d ÷ 2.</li>
    <li>Har qanday aylanada L ÷ d bir xil son beradi — bu π.</li>
    <li>π ≈ 3,14 (yoki <sup>22</sup>/<sub>7</sub>), lekin aniq emas:
      uning oʻnlik yozuvi cheksiz.</li>
    <li>Aylananing uzunligi bilinsa, diametr topiladi: d = L ÷ π.</li>
    <li>π ni Bobildan Samarqandgacha boʻlgan olimlar toʻrt ming yil
      aniqlashgan; al-Koshiyning 16 xonalik rekordi 180 yil
      turgan.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-71 — aylana uzunligi va doira yuzasi
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-71: Aylana uzunligi va doira yuzasi",
        "category": "math",
        "order": 71,
        "summary": (
            "Ikkita formula: L = 2πr va S = πr². Ikkalasi ham qayerdan "
            "chiqqani koʻrsatiladi — doirani boʻlaklarga kesib, toʻgʻri "
            "toʻrtburchakka aylantirib."
        ),
        "stories": ["Gʻildirak necha marta aylanadi"],
        "content": """
<h2>PM-71: Aylana uzunligi va doira yuzasi</h2>

<p>Oʻtgan darsda π ni topdik: har qanday aylananing uzunligi diametridan
π marta katta. Endi shu bitta jumladan ikkita formula chiqaramiz — biri
chegara uchun, ikkinchisi ichi uchun.</p>

<p>Bu ikki formula bilan gʻildirakning yoʻli, gulzorning tuprogʻi, quduq
ogʻzining qopqogʻi va hatto pitsaning qaysi biri arzon ekani
hisoblanadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>aylana uzunligini L = 2 × π × r bilan topasiz;</li>
    <li>doira yuzasi nega S = π × r<sup>2</sup> ekanini koʻrasiz;</li>
    <li>teskari masalani — uzunlikdan radiusni — yechasiz;</li>
    <li>radius ikki marta oshsa, yuza nega toʻrt marta oshishini
      tushuntirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Aylana uzunligi</span>
  <span class="pe-chip pe-chip--s">L</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">2 × π ×</span>
  <span class="pe-chip pe-chip--o">r</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">π ×</span>
  <span class="pe-chip pe-chip--o">d</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Doira yuzasi</span>
  <span class="pe-chip pe-chip--s">S</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">π ×</span>
  <span class="pe-chip pe-chip--o">r<sup>2</sup></span>
</div>

<figure class="pm-fig">
  <svg viewBox="0 0 320 175" role="img" aria-label="Chapda aylana uzunligi, oʻngda doira yuzasi">
    <circle class="pm-ln pm-ln--hl" cx="85" cy="80" r="56" fill="none"/>
    <line class="pm-ln pm-ln--dash" x1="85" y1="80" x2="141" y2="80"/>
    <circle class="pm-pt" cx="85" cy="80" r="3"/>
    <text class="pm-lbl" x="106" y="74">r</text>
    <circle class="pm-fill--hl" cx="235" cy="80" r="56"/>
    <circle class="pm-ln" cx="235" cy="80" r="56" fill="none"/>
    <line class="pm-ln pm-ln--dash" x1="235" y1="80" x2="291" y2="80"/>
    <circle class="pm-pt" cx="235" cy="80" r="3"/>
    <text class="pm-lbl" x="256" y="74">r</text>
    <text class="pm-lbl pm-lbl--hl" x="36" y="162">L = 2 × π × r</text>
    <text class="pm-lbl pm-lbl--hl" x="196" y="162">S = π × r × r</text>
  </svg>
  <figcaption>Chapda — chegara chizigʻining uzunligi (metrlarda).
  Oʻngda — ichining yuzasi (kvadrat metrlarda).</figcaption>
</figure>

<h3>1. Aylana uzunligi</h3>

<p>π = L ÷ d edi (PM-70). Bu tenglikni L ga nisbatan yechsak, formula
oʻzi chiqadi:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">π = L ÷ d</span>
    <span class="pm-solve__why">π ning taʼrifi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">L = π × d</span>
    <span class="pm-solve__why">Ikki tomonni d ga koʻpaytirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">L = 2 × π × r</span>
    <span class="pm-solve__why">Chunki d = 2r</span>
  </div>
</div>

<p>Ikkala koʻrinish ham bitta formula. Masalada <b>diametr</b> berilsa
π × d ni, <b>radius</b> berilsa 2 × π × r ni oling.</p>

<div class="pe-ex">
  <p class="pe-ex__math">r = 5 sm → L = 2 × 3,14 × 5 = 31,4 sm</p>
  <p class="pe-ex__uz">Radiusi 5 santimetr boʻlgan aylananing uzunligi —
  31,4 santimetr.</p>
  <p class="pe-ex__why">Avval 2 × 5 = 10, keyin 10 × 3,14 = 31,4. Shu
  tartib qulayroq.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">d = 8 m → L = 3,14 × 8 = 25,12 m</p>
  <p class="pe-ex__uz">Diametri 8 metr boʻlgan quduq ogʻzining atrofi —
  25,12 metr.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Har safar bitta savol bering: bu radiusmi yoki
  diametr?</p>
  <p>Ikkala formula ham toʻgʻri, lekin ular <b>boshqa-boshqa songa</b>
  qoʻyiladi. 2 × π × r ga radius tushadi, π × d ga esa diametr. Ularni
  aralashtirib yuborsangiz, javob ikki barobar katta yoki ikki barobar
  kichik chiqadi. Masala shartida «radiusi» soʻzi bormi yoki «diametri»
  — hisobni boshlashdan oldin shuni ustiga chizib qoʻying.</p>
</div>

<p>Teskari masala — uzunlikdan radiusni topish:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">L = 62,8 m</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">d = 62,8 ÷ 3,14 = 20 m</span>
    <span class="pm-solve__why">Avval diametr (PM-70)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">r = 20 ÷ 2 = 10 m</span>
    <span class="pm-solve__why">Radius — diametrning yarmi</span>
  </div>
</div>

<h3>2. Doira yuzasi: doirani kesib, toʻgʻri toʻrtburchak yasaymiz</h3>

<p>Yuzani topishning yoʻli oʻtgan darsdagidek (PM-69): shaklni kesib,
tanish shaklga aylantiramiz. Doirani markazidan boshlab tortga
boʻlingandek boʻlaklarga kesamiz va ularni navbatma-navbat terib
chiqamiz.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 145" role="img" aria-label="Doira oʻn ikki boʻlakka kesilib, toʻgʻri toʻrtburchakka terilgan">
    <path class="pm-fill" d="M 46 25 L 27.9 92.6 A 70 70 0 0 0 64.1 92.6 Z"/>
    <path class="pm-ln" fill="none" d="M 46 25 L 27.9 92.6 A 70 70 0 0 0 64.1 92.6 Z"/>
    <path class="pm-fill" d="M 82.2 25 L 64.1 92.6 A 70 70 0 0 0 100.4 92.6 Z"/>
    <path class="pm-ln" fill="none" d="M 82.2 25 L 64.1 92.6 A 70 70 0 0 0 100.4 92.6 Z"/>
    <path class="pm-fill" d="M 118.5 25 L 100.4 92.6 A 70 70 0 0 0 136.6 92.6 Z"/>
    <path class="pm-ln" fill="none" d="M 118.5 25 L 100.4 92.6 A 70 70 0 0 0 136.6 92.6 Z"/>
    <path class="pm-fill" d="M 154.7 25 L 136.6 92.6 A 70 70 0 0 0 172.8 92.6 Z"/>
    <path class="pm-ln" fill="none" d="M 154.7 25 L 136.6 92.6 A 70 70 0 0 0 172.8 92.6 Z"/>
    <path class="pm-fill" d="M 190.9 25 L 172.8 92.6 A 70 70 0 0 0 209.1 92.6 Z"/>
    <path class="pm-ln" fill="none" d="M 190.9 25 L 172.8 92.6 A 70 70 0 0 0 209.1 92.6 Z"/>
    <path class="pm-fill" d="M 227.2 25 L 209.1 92.6 A 70 70 0 0 0 245.3 92.6 Z"/>
    <path class="pm-ln" fill="none" d="M 227.2 25 L 209.1 92.6 A 70 70 0 0 0 245.3 92.6 Z"/>
    <path class="pm-fill pm-fill--hl" d="M 64.1 95 L 82.2 27.4 A 70 70 0 0 0 46 27.4 Z"/>
    <path class="pm-ln" fill="none" d="M 64.1 95 L 82.2 27.4 A 70 70 0 0 0 46 27.4 Z"/>
    <path class="pm-fill pm-fill--hl" d="M 100.4 95 L 118.5 27.4 A 70 70 0 0 0 82.2 27.4 Z"/>
    <path class="pm-ln" fill="none" d="M 100.4 95 L 118.5 27.4 A 70 70 0 0 0 82.2 27.4 Z"/>
    <path class="pm-fill pm-fill--hl" d="M 136.6 95 L 154.7 27.4 A 70 70 0 0 0 118.5 27.4 Z"/>
    <path class="pm-ln" fill="none" d="M 136.6 95 L 154.7 27.4 A 70 70 0 0 0 118.5 27.4 Z"/>
    <path class="pm-fill pm-fill--hl" d="M 172.8 95 L 190.9 27.4 A 70 70 0 0 0 154.7 27.4 Z"/>
    <path class="pm-ln" fill="none" d="M 172.8 95 L 190.9 27.4 A 70 70 0 0 0 154.7 27.4 Z"/>
    <path class="pm-fill pm-fill--hl" d="M 209.1 95 L 227.2 27.4 A 70 70 0 0 0 190.9 27.4 Z"/>
    <path class="pm-ln" fill="none" d="M 209.1 95 L 227.2 27.4 A 70 70 0 0 0 190.9 27.4 Z"/>
    <path class="pm-fill pm-fill--hl" d="M 245.3 95 L 263.4 27.4 A 70 70 0 0 0 227.2 27.4 Z"/>
    <path class="pm-ln" fill="none" d="M 245.3 95 L 263.4 27.4 A 70 70 0 0 0 227.2 27.4 Z"/>
    <line class="pm-ln pm-ln--dash" x1="261.3" y1="25" x2="261.3" y2="95"/>
    <text class="pm-lbl pm-lbl--hl" x="266.3" y="64">r</text>
    <line class="pm-ln pm-ln--dash" x1="27.9" y1="113" x2="245.3" y2="113"/>
    <text class="pm-lbl pm-lbl--hl" x="112.6" y="133">π × r</text>
  </svg>
  <figcaption>Oʻn ikkita boʻlak navbatma-navbat terildi. Qancha koʻp
  kesilsa, shakl toʻgʻri toʻrtburchakka shuncha oʻxshaydi.</figcaption>
</figure>

<p>Hosil boʻlgan shaklni oʻlchaymiz:</p>

<ul>
  <li>uning <b>boʻyi</b> — har bir boʻlakning uchidan yoyigacha, yaʼni
    <b>r</b>;</li>
  <li>uning <b>eni</b> — yoylarning yarmi tepada, yarmi pastda. Demak
    eni butun aylananing yarmi: L ÷ 2 = (2 × π × r) ÷ 2 =
    <b>π × r</b>.</li>
</ul>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">S = eni × boʻyi</span>
    <span class="pm-solve__why">Toʻgʻri toʻrtburchakning yuzasi
    (PM-68)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">S = (π × r) × r</span>
    <span class="pm-solve__why">Eni π × r, boʻyi r</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">S = π × r<sup>2</sup></span>
    <span class="pm-solve__why">r × r = r<sup>2</sup> (PM-12)</span>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">r = 5 sm → S = 3,14 × 25 = 78,5 sm<sup>2</sup></p>
  <p class="pe-ex__uz">Radiusi 5 santimetr boʻlgan doiraning yuzasi —
  78,5 kvadrat santimetr.</p>
  <p class="pe-ex__why">Avval r<sup>2</sup> = 25, keyin π ga
  koʻpaytiriladi — tartib shu (PM-5).</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">d = 12 sm → r = 6 → S = 3,14 × 36 =
  113,04 sm<sup>2</sup></p>
  <p class="pe-ex__uz">Diametri 12 santimetr boʻlgan tarelkaning yuzasi —
  113,04 kvadrat santimetr.</p>
  <p class="pe-ex__why">Diametr berilsa, avval radiusga oʻting. Yuzada
  har doim <b>radius</b> ishlaydi.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Uchta eng qimmat xato</p>
  <p>1. Yuzaga diametrni qoʻyish: S = π × 12<sup>2</sup> ✗. Avval
  r = d ÷ 2.
  <br>2. Yuza oʻrniga uzunlikni hisoblash: 2 × π × r ✗. Birlikka
  qarang — yuza m<sup>2</sup> da.
  <br>3. π ni ham kvadratga koʻtarish: (3,14 × 5)<sup>2</sup> ✗.
  Kvadratga faqat <b>radius</b> koʻtariladi.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">π ni oxirida koʻpaytiring</p>
  <p>Avval r<sup>2</sup> ni hisoblang — u butun son boʻladi va xatolashish
  qiyin. π ga koʻpaytirishni esa eng oxiriga qoldiring. Yaʼni
  3,14 × 7 × 7 emas, <b>49 × 3,14</b>. Shu tartib bilan oraliq javoblar
  toza qoladi va xatoni topish osonlashadi.</p>
</div>

<h3>3. Halqa: kattadan kichigini ayiring</h3>

<p>Doiraviy hovuzning atrofiga yoʻlka quyiladi. Hovuzning radiusi 6 m,
yoʻlkaning eni esa 4 m. Yoʻlkaning yuzasi qancha?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Tashqi radius: 6 + 4 = 10 m</span>
    <span class="pm-solve__why">Hovuz va yoʻlka birgalikda</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Katta doira: 3,14 × 100 = 314 m<sup>2</sup></span>
    <span class="pm-solve__why">10<sup>2</sup> = 100</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Hovuz: 3,14 × 36 = 113,04 m<sup>2</sup></span>
    <span class="pm-solve__why">6<sup>2</sup> = 36</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">314 − 113,04 = 200,96 m<sup>2</sup></span>
    <span class="pm-solve__why">Ortiqchasini ayirdik (PM-69)</span>
  </div>
</div>

<h3>4. Radius ikki marta oshsa, yuza toʻrt marta oshadi</h3>

<p>Bu doiraning eng ajablantiradigan xossasi va u har kuni ish
beradi.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">r = 5 sm</p>
    <p>S = 3,14 × 5<sup>2</sup> = 3,14 × 25 = 78,5 sm<sup>2</sup></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">r = 10 sm</p>
    <p>S = 3,14 × 10<sup>2</sup> = 3,14 × 100 = 314 sm<sup>2</sup></p>
  </div>
</div>

<p>Radius 2 marta oshdi, yuza esa 314 ÷ 78,5 = <b>4 marta</b> oshdi.
Sababi formulada: r kvadratga koʻtariladi, demak 2 marta oshgan radius
2<sup>2</sup> = 4 marta koʻp yuza beradi. Xuddi shunday, 3 marta oshsa —
9 marta.</p>

<h3>Matnli masala</h3>

<p>Afsona pitsa buyurtma qilmoqchi. Ikki xil taklif bor: ikkita kichik
pitsa (har birining diametri 20 sm) — 60 000 soʻm, yoki bitta katta
pitsa (diametri 30 sm) — 55 000 soʻm.</p>

<p><b>Qaysi biri koʻproq pitsa beradi va u qimmatroqmi?</b></p>

<p><b>Reja:</b> ikkala taklifning ham yuzasini hisoblaymiz va narxlarni
solishtiramiz.</p>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Katta pitsaning diametri 1,5 marta katta, demak yuzasi
  1,5<sup>2</sup> = 2,25 marta katta boʻlishi kerak. Ikkita kichik
  pitsa esa atigi 2 marta beradi. Katta pitsa yutadiganga
  oʻxshaydi.</span>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Kichik: r = 20 ÷ 2 = 10 sm</span>
    <span class="pm-solve__why">Diametrdan radiusga oʻtdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3,14 × 100 = 314 sm<sup>2</sup></span>
    <span class="pm-solve__why">Bitta kichik pitsaning yuzasi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">314 × 2 = 628 sm<sup>2</sup></span>
    <span class="pm-solve__why">Ikkitasi birgalikda, 60 000 soʻmga</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Katta: r = 30 ÷ 2 = 15 sm</span>
    <span class="pm-solve__why">Yana radiusga oʻtdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3,14 × 225 = 706,5 sm<sup>2</sup></span>
    <span class="pm-solve__why">Bitta katta pitsa, 55 000 soʻmga</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>314 × 2,25 = 706,5 ✓ — taxminimiz aynan toʻgʻri chiqdi.
  <br>706,5 &gt; 628, yaʼni katta pitsa 78,5 sm<sup>2</sup> koʻproq
  beradi — <b>va 5000 soʻm arzon</b>.
  <br><b>Javob:</b> bitta katta pitsa foydaliroq. Koʻz bilan qaraganda
  ikkita 20 sm bitta 30 sm dan koʻproqdek koʻrinadi — bu aldanish
  kvadratning ishi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">d = 10 sm → S = 3,14 × 10<sup>2</sup> = 314</p>
  <p class="pe-fix__good">r = 5 → S = 3,14 × 25 = 78,5 sm<sup>2</sup></p>
  <p class="pe-fix__why">Formulada radius turadi, diametr emas. Diametrni
  qoʻysangiz, javob roppa-rosa 4 marta katta chiqadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">r = 5 → S = 2 × 3,14 × 5 = 31,4 sm<sup>2</sup></p>
  <p class="pe-fix__good">S = 3,14 × 25 = 78,5 sm<sup>2</sup></p>
  <p class="pe-fix__why">Bu aylananing uzunligi formulasi. Uzunlik
  santimetrda, yuza esa kvadrat santimetrda — birlik xatoni darrov
  koʻrsatadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">r = 5 → S = (3,14 × 5)<sup>2</sup> = 246,49</p>
  <p class="pe-fix__good">S = 3,14 × 5<sup>2</sup> = 78,5</p>
  <p class="pe-fix__why">Kvadratga faqat radius koʻtariladi, π emas.
  Amallar tartibiga koʻra daraja koʻpaytirishdan oldin bajariladi
  (PM-5).</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Halqa: (10 − 6)<sup>2</sup> × 3,14 = 50,24</p>
  <p class="pe-fix__good">3,14 × 100 − 3,14 × 36 = 200,96</p>
  <p class="pe-fix__why">Radiuslarni ayirib boʻlmaydi — <b>yuzalar</b>
  ayiriladi. Avval ikkala doirani hisoblang, keyin ayiring.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Radiusi 3 sm boʻlgan aylananing uzunligi
  qancha? (π ≈ 3,14)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>18,84 sm.</b> L = 2 × 3,14 × 3 = 6,28 × 3 = 18,84.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Diametri 10 m boʻlgan doiraviy hovuzning
  atrofi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>31,4 m.</b> L = π × d = 3,14 × 10 = 31,4. Radiusga oʻtish
    shart emas — diametr berilganda π × d qulayroq.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Radiusi 4 sm boʻlgan doiraning yuzasi
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>50,24 sm<sup>2</sup>.</b> S = 3,14 × 4<sup>2</sup> =
    3,14 × 16 = 50,24.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Diametri 20 sm boʻlgan tarelkaning yuzasi
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>314 sm<sup>2</sup>.</b> Avval radius: r = 20 ÷ 2 = 10 sm.
    Keyin: S = 3,14 × 100 = 314 sm<sup>2</sup>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Aylananing uzunligi 43,96 sm. Diametri
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>14 sm.</b> d = L ÷ π = 43,96 ÷ 3,14 = 14. Tekshirish:
    14 × 3,14 = 43,96 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Halqa: tashqi radiusi 5 m, ichki radiusi 3 m.
  Halqaning yuzasi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>50,24 m<sup>2</sup>.</b> Katta doira: 3,14 × 25 =
    78,5 m<sup>2</sup>. Kichik doira: 3,14 × 9 = 28,26 m<sup>2</sup>.
    Ayiramiz: 78,5 − 28,26 = 50,24 m<sup>2</sup>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">7. Jasurning hovlisida doiraviy gulzor bor,
  radiusi 3 m. Gulzorning atrofiga past panjara qoʻyiladi va ichiga
  tuproq solinadi. Panjara necha metr kerak (butun metrgacha yuqoriga
  yaxlitlang) va tuproq necha kvadrat metr joyga solinadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Panjara — 19 m, tuproq — 28,26 m<sup>2</sup>.</b> Panjara
    chegara boʻylab ketadi, demak aylana uzunligi: L = 2 × 3,14 × 3 =
    18,84 m → 19 m (PM-14). Tuproq esa ichga solinadi, demak yuza:
    S = 3,14 × 9 = 28,26 m<sup>2</sup>. Birliklarga qarang — biri
    metrda, ikkinchisi kvadrat metrda.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Aylana uzunligi</b><span>aylananing atrofi, L = 2πr; ingl.
    circumference</span></li>
  <li><b>Doira yuzasi</b><span>doira egallagan joy, S = πr<sup>2</sup>;
    ingl. area of a circle</span></li>
  <li><b>Radius</b><span>markazdan aylanagacha masofa; ingl.
    radius</span></li>
  <li><b>Diametr</b><span>d = 2r; ingl. diameter</span></li>
  <li><b>π (pi)</b><span>≈ 3,14 — aylana uzunligining diametrga nisbati;
    ingl. pi</span></li>
  <li><b>Halqa</b><span>ikkita doira orasidagi soha; ingl.
    annulus</span></li>
  <li><b>Sektor</b><span>doiraning ikki radius orasidagi boʻlagi; ingl.
    sector</span></li>
  <li><b>Kvadrat</b><span>sonning oʻziga koʻpaytirilgani,
    r<sup>2</sup>; ingl. square</span></li>
  <li><b>Kvadrat metr</b><span>m<sup>2</sup> — yuza birligi; ingl.
    square metre</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>L = 2 × π × r = π × d — chegara uchun, oddiy metrda.</li>
    <li>S = π × r<sup>2</sup> — ichi uchun, kvadrat metrda.</li>
    <li>S = πr<sup>2</sup> doirani boʻlaklarga kesib terishdan chiqadi:
      eni π × r, boʻyi r.</li>
    <li>Diametr berilsa, yuzadan oldin radiusga oʻting.</li>
    <li>Halqa = katta doira − kichik doira, radiuslar emas, yuzalar
      ayiriladi.</li>
    <li>Radius 2 marta oshsa, yuza 4 marta oshadi — kvadratning
      ishi.</li>
  </ul>
</div>
""",
    },
]
