# -*- coding: utf-8 -*-
"""Prime Math — BLOK D BOSHI: darslar 45–47 (koordinata, masofa, funksiya).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt

  mashqlar — practice/management/commands/_practice_pm_45_47.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_45_47.py

⚠️ Kumulyativ chegaralar:
  • PM-45 — koordinata tekisligi, abssissa/ordinata, toʻrt chorak, oʻqlardagi
    nuqtalar. Grafik chizish YOʻQ (u PM-48 dan boshlanadi);
  • PM-46 — faqat GORIZONTAL va VERTIKAL kesmaning uzunligi (|x₂ − x₁|,
    modul PM-41 dan) hamda kesmaning oʻrtasi. ⛔ QIYA kesma uzunligining
    formulasi Pifagor teoremasiga tayanadi, u esa PM-64 — shuning uchun bu
    darsda faqat «PM-64 da oʻrganamiz» deb aytiladi va ishlatilmaydi;
  • PM-47 — funksiya gʻoyasi, jadval va formula bilan yozish, f(x) belgisi,
    teskari savol (tenglama, PM-36). Grafik YOʻQ — u PM-48;
  • tenglama (PM-36), amallar tartibi (PM-5), modul (PM-41), manfiy sonlar
    (PM-9…11) va S = a·b formulasi (PM-35) faol ishlatiladi.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_45_47.py --author=prime
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
    # PM-45 — koordinata tekisligi
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-45: Koordinata tekisligi: nuqtaning manzili",
        "category": "math",
        "order": 45,
        "summary": (
            "Ikkita son bilan tekislikdagi har qanday nuqtani topish: abssissa va "
            "ordinata, koordinata boshi, toʻrt chorak va oʻqlar ustidagi "
            "nuqtalar."
        ),
        "stories": ["Kemadagi manzil — xarita katakchalari"],
        "content": """
<h2>PM-45: Koordinata tekisligi: nuqtaning manzili</h2>

<p>Kinoteatr chiptasida ikkita son yozilgan: <b>7-qator, 12-oʻrin</b>. Faqat
«7-qator» deyilsa, oʻrningizni topolmaysiz — qatorda oʻttizta kursi bor. Faqat
«12-oʻrin» deyilsa ham topolmaysiz. Ikkalasi birga esa zalda bitta, aniq bitta
kursini koʻrsatadi.</p>

<p>Matematika ham xuddi shunday ishlaydi. PM-9 da biz son oʻqini koʻrgan edik: u
yerda bitta son bitta nuqtani belgilaydi. Lekin son oʻqi — chiziq. Tekislikda esa
chapga-oʻngga ham, yuqoriga-pastga ham yurish mumkin, shuning uchun bitta son
yetmaydi. Ikkita kerak.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>koordinata tekisligini chizasiz va uning qismlarini nomlaysiz;</li>
    <li>chizmadagi nuqtaning koordinatalarini oʻqiysiz;</li>
    <li>berilgan koordinatalar boʻyicha nuqtani qoʻyasiz;</li>
    <li>nuqta qaysi chorakda ekanini ishoralariga qarab aytasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Nuqtaning manzili</span>
  <span class="pe-chip pe-chip--o">A</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">avval x</span>
  <span class="pe-op">;</span>
  <span class="pe-chip pe-chip--v">keyin y</span>
</div>

<h3>1. Ikkita oʻq</h3>

<p>Ikkita son oʻqini olamiz va ularni <b>perpendikulyar</b> qilib, nollari ustma-ust
tushadigan qilib joylashtiramiz.</p>

<ul>
  <li><b>Ox</b> — gorizontal oʻq, <b>abssissalar oʻqi</b>. Oʻngga qarab sonlar
    oʻsadi, chapga qarab manfiy boʻladi.</li>
  <li><b>Oy</b> — vertikal oʻq, <b>ordinatalar oʻqi</b>. Yuqoriga qarab oʻsadi,
    pastga qarab manfiy boʻladi.</li>
  <li>Ular kesishgan joy — <b>koordinata boshi</b>, <b>O</b> harfi bilan
    belgilanadi. Uning manzili: <b>O(0; 0)</b>.</li>
</ul>

<p>Shu ikki oʻq bilan jihozlangan tekislik <b>koordinata tekisligi</b> deyiladi.
Katakli daftar buning uchun tayyor qurol: bitta katak — bitta birlik.</p>

<h3>2. Nuqtaning koordinatalari</h3>

<p>Har qanday nuqtaning manzili ikkita sondan iborat va u qavs ichida, nuqtali
vergul bilan yoziladi: <b>A(3; 2)</b>.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 260" role="img" aria-label="Koordinata tekisligida A(3; 2) nuqtasi">
    <line class="pm-ln" x1="20" y1="140" x2="308" y2="140"/>
    <line class="pm-ln" x1="150" y1="248" x2="150" y2="18"/>
    <polygon class="pm-fill" points="312,140 300,135 300,145"/>
    <polygon class="pm-fill" points="150,14 145,26 155,26"/>
    <line class="pm-ln" x1="180" y1="136" x2="180" y2="144"/>
    <line class="pm-ln" x1="210" y1="136" x2="210" y2="144"/>
    <line class="pm-ln" x1="240" y1="136" x2="240" y2="144"/>
    <line class="pm-ln" x1="120" y1="136" x2="120" y2="144"/>
    <line class="pm-ln" x1="90" y1="136" x2="90" y2="144"/>
    <line class="pm-ln" x1="146" y1="110" x2="154" y2="110"/>
    <line class="pm-ln" x1="146" y1="80" x2="154" y2="80"/>
    <line class="pm-ln" x1="146" y1="170" x2="154" y2="170"/>
    <line class="pm-ln pm-ln--dash" x1="240" y1="140" x2="240" y2="80"/>
    <line class="pm-ln pm-ln--dash" x1="150" y1="80" x2="240" y2="80"/>
    <circle class="pm-pt" cx="240" cy="80" r="5"/>
    <text class="pm-lbl" x="298" y="160">x</text>
    <text class="pm-lbl" x="160" y="30">y</text>
    <text class="pm-lbl" x="138" y="158">O</text>
    <text class="pm-lbl" x="180" y="158" text-anchor="middle">1</text>
    <text class="pm-lbl" x="240" y="158" text-anchor="middle">3</text>
    <text class="pm-lbl" x="90" y="158" text-anchor="middle">−2</text>
    <text class="pm-lbl" x="136" y="114" text-anchor="end">1</text>
    <text class="pm-lbl" x="136" y="84" text-anchor="end">2</text>
    <text class="pm-lbl" x="136" y="174" text-anchor="end">−1</text>
    <text class="pm-lbl pm-lbl--hl" x="250" y="70">A(3; 2)</text>
  </svg>
  <figcaption>A nuqtasiga borish uchun: koordinata boshidan 3 katak oʻngga, keyin
  2 katak yuqoriga.</figcaption>
</figure>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Tartib muhim</p>
  <p>Birinchi son — <b>doim</b> abssissa (x, chapga-oʻngga), ikkinchisi — <b>doim</b>
  ordinata (y, yuqoriga-pastga). Shuning uchun A(3; 2) va B(2; 3) — bitta nuqta
  emas, ikkita har xil nuqta. Alifboda ham «x» «y» dan oldin keladi — shu esda
  tursin.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">B(−4; 1)</p>
  <p class="pe-ex__uz">Koordinata boshidan 4 katak chapga, soʻng 1 katak
  yuqoriga.</p>
  <p class="pe-ex__why">Abssissa manfiy — demak chapga; ordinata musbat — demak
  yuqoriga.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">C(2; −5)</p>
  <p class="pe-ex__uz">2 katak oʻngga, keyin 5 katak pastga.</p>
  <p class="pe-ex__why">Ordinatasi manfiy boʻlgani uchun nuqta Ox oʻqidan
  pastda.</p>
</div>

<h3>3. Toʻrt chorak</h3>

<p>Ikki oʻq tekislikni toʻrt boʻlakka ajratadi. Ular <b>chorak</b> deyiladi va
oʻng yuqoridan boshlab, <b>soat mili yoʻnalishiga teskari</b> raqamlanadi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 240" role="img" aria-label="Koordinata tekisligining toʻrt choragi">
    <line class="pm-ln" x1="20" y1="120" x2="300" y2="120"/>
    <line class="pm-ln" x1="160" y1="225" x2="160" y2="15"/>
    <text class="pm-lbl pm-lbl--hl" x="235" y="60" text-anchor="middle">I</text>
    <text class="pm-lbl" x="235" y="82" text-anchor="middle">(+ ; +)</text>
    <text class="pm-lbl pm-lbl--hl" x="85" y="60" text-anchor="middle">II</text>
    <text class="pm-lbl" x="85" y="82" text-anchor="middle">(− ; +)</text>
    <text class="pm-lbl pm-lbl--hl" x="85" y="170" text-anchor="middle">III</text>
    <text class="pm-lbl" x="85" y="192" text-anchor="middle">(− ; −)</text>
    <text class="pm-lbl pm-lbl--hl" x="235" y="170" text-anchor="middle">IV</text>
    <text class="pm-lbl" x="235" y="192" text-anchor="middle">(+ ; −)</text>
    <text class="pm-lbl" x="292" y="140">x</text>
    <text class="pm-lbl" x="170" y="26">y</text>
  </svg>
  <figcaption>Chorakni ishoralar aytib beradi: (−; +) — faqat II chorak.</figcaption>
</figure>

<div class="pe-table-wrap"><table>
  <tr><th>Chorak</th><th>x</th><th>y</th><th>Misol</th></tr>
  <tr><td>I</td><td>musbat</td><td>musbat</td><td>(3; 2)</td></tr>
  <tr><td>II</td><td>manfiy</td><td>musbat</td><td>(−4; 1)</td></tr>
  <tr><td>III</td><td>manfiy</td><td>manfiy</td><td>(−2; −6)</td></tr>
  <tr><td>IV</td><td>musbat</td><td>manfiy</td><td>(2; −5)</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Chorakni yodlash shart emas</p>
  <p>Koʻpchilik choraklarni yodlashga urinadi va adashadi. Yodlash kerak emas —
  <b>ishoralarga qarang</b>. Birinchi son manfiy boʻlsa, nuqta chapda; ikkinchisi
  manfiy boʻlsa, pastda. «Chapda va pastda» — bu III chorak. Bir soniyada
  chiqadi.</p>
</div>

<h3>4. Oʻqlar ustidagi nuqtalar</h3>

<p>Oʻqning oʻzida yotgan nuqtalar hech qaysi chorakka tegishli emas — ular chegarada
turadi. Ularni bittagina belgisidan tanish mumkin: <b>nolga qarang</b>.</p>

<div class="pe-table-wrap"><table>
  <tr><th>Nuqta</th><th>Qayerda</th><th>Nega</th></tr>
  <tr><td>(5; 0)</td><td>Ox oʻqida</td><td>Yuqoriga ham, pastga ham koʻtarilmadi</td></tr>
  <tr><td>(0; −3)</td><td>Oy oʻqida</td><td>Chapga ham, oʻngga ham yurmadi</td></tr>
  <tr><td>(0; 0)</td><td>Koordinata boshi</td><td>Hech qayerga yurmadi</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Qoidani bir gapga siqamiz</p>
  <p><b>Ordinatasi nol</b> boʻlgan hamma nuqtalar gorizontal oʻqda yotadi.
  <b>Abssissasi nol</b> boʻlganlari esa vertikal oʻqda. Nolning oʻrni qaysi
  yoʻnalishda <b>umuman</b> yurmaganingizni aytadi.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Maktab hovlisidagi gulzor.</b> Sherbek maktab hovlisining chizmasini katakli
daftarga tushirdi. Darvozani koordinata boshi qilib oldi, har bir katakni
<b>1 metr</b> deb belgiladi. Toʻgʻri toʻrtburchak shaklidagi gulzorning uchta
burchagi chizmada shunday chiqdi: <b>A(−2; 1)</b>, <b>B(4; 1)</b>,
<b>C(4; 5)</b>.</p>

<p><b>Savol:</b> toʻrtinchi burchak qayerda va gulzorning yuzasi necha
m<sup>2</sup>?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">A(−2; 1) va B(4; 1)</span>
    <span class="pm-solve__why">Ordinatalari teng — demak AB gorizontal
      tomon</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">B(4; 1) va C(4; 5)</span>
    <span class="pm-solve__why">Abssissalari teng — demak BC vertikal tomon</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">D(−2; 5)</span>
    <span class="pm-solve__why">D — A ning ustida (x = −2) va C ning yonida
      (y = 5)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">AB = 6 m, BC = 4 m</span>
    <span class="pm-solve__why">−2 dan 4 gacha 6 katak; 1 dan 5 gacha 4 katak</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">S = 6 × 4 = 24 m<sup>2</sup></span>
    <span class="pm-solve__why">Toʻgʻri toʻrtburchakning yuzasi — tomonlar
      koʻpaytmasi (PM-35)</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Toʻrtta burchakni chizmaga qoʻyib koʻring: (−2; 1), (4; 1), (4; 5), (−2; 5).
  Qarama-qarshi tomonlar teng, hamma burchak toʻgʻri — haqiqatan toʻgʻri
  toʻrtburchak ✓ Gulzor darvozadan chapga ham chiqib turibdi, chunki A va D ning
  abssissasi manfiy.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Gulzor 6 metrga 4 metr — bir xonaning yarmicha. 24 m<sup>2</sup> mantiqiy;
  240 m<sup>2</sup> chiqsa, birlikda xato qilingan boʻlardi.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">A(3; 2) va B(2; 3) — bitta nuqta</p>
  <p class="pe-fix__good">Bular har xil ikkita nuqta</p>
  <p class="pe-fix__why">Birinchi son <b>doim</b> abssissa. A ga 3 katak oʻngga va
  2 katak yuqoriga borilsa, B ga 2 katak oʻngga va 3 katak yuqoriga boriladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">(−4; 5) nuqtasi IV chorakda</p>
  <p class="pe-fix__good">(−4; 5) nuqtasi II chorakda</p>
  <p class="pe-fix__why">Chorakni ishoralar aytadi: (−; +) faqat II chorakda
  boʻladi. IV chorakda esa aksincha, (+; −).</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">(0; −3) nuqtasi Ox oʻqida yotadi</p>
  <p class="pe-fix__good">(0; −3) nuqtasi Oy oʻqida yotadi</p>
  <p class="pe-fix__why">Abssissasi nol — demak chapga ham, oʻngga ham
  yurilmagan, nuqta vertikal oʻqda qolgan.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. A(4; −3) nuqtasi qaysi chorakda?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>IV chorakda.</b> Abssissa musbat (oʻngda), ordinata manfiy (pastda) —
    oʻng past burchak.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. (0; −5) nuqtasi qayerda joylashgan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Oy oʻqida, koordinata boshidan 5 katak pastda.</b> Abssissasi nol
    boʻlgani uchun u hech qaysi chorakka kirmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. B(−3; 2) va C(2; −3) bir xil nuqtami?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Yoʻq.</b> B — II chorakda (chapda va yuqorida), C — IV chorakda (oʻngda
    va pastda). Sonlar bir xil, lekin oʻrinlari almashgan.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Ordinatasi 0 ga teng boʻlgan barcha nuqtalar qayerda
  yotadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Ox oʻqida.</b> Masalan (7; 0), (−1; 0), (0; 0) — hammasi gorizontal
    oʻqning ustida.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Katakli xaritada Bekzodning uyi (−3; 2), maktab esa
  (4; 2) nuqtada. Har bir katak 100 metr. Bekzod maktabgacha qaysi tomonga va necha
  metr yurishi kerak?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Oʻngga 7 katak, yaʼni 700 metr.</b> Ikkala nuqtaning ordinatasi bir xil
    (2), demak yoʻl gorizontal. −3 dan 4 gacha 7 katak: −3 → 0 uchta, 0 → 4
    toʻrtta.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Koordinata tekisligi</b><span>ikki oʻq bilan jihozlangan tekislik; ingl.
    coordinate plane</span></li>
  <li><b>Abssissa</b><span>birinchi koordinata, x; ingl. x-coordinate</span></li>
  <li><b>Ordinata</b><span>ikkinchi koordinata, y; ingl. y-coordinate</span></li>
  <li><b>Koordinata boshi</b><span>oʻqlar kesishgan nuqta O(0; 0); ingl.
    origin</span></li>
  <li><b>Abssissalar oʻqi (Ox)</b><span>gorizontal oʻq; ingl. x-axis</span></li>
  <li><b>Ordinatalar oʻqi (Oy)</b><span>vertikal oʻq; ingl. y-axis</span></li>
  <li><b>Chorak</b><span>tekislikning toʻrtdan bir qismi; ingl. quadrant</span></li>
  <li><b>Tartiblangan juftlik</b><span>(x; y) — tartibi muhim boʻlgan ikki son;
    ingl. ordered pair</span></li>
  <li><b>Birlik kesma</b><span>bitta katakning uzunligi; ingl. unit</span></li>
  <li><b>Perpendikulyar</b><span>toʻgʻri burchak ostida kesishuvchi; ingl.
    perpendicular</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Nuqtaning manzili — ikkita son:</b> avval x (chapga-oʻngga), keyin y
      (yuqoriga-pastga).</li>
    <li><b>Chorakni ishoralar aytadi</b> — (−; +) faqat II chorak boʻladi,
      yodlash shart emas.</li>
    <li><b>Nol — chegara belgisi:</b> koordinatalardan biri nol boʻlsa, nuqta
      oʻqning ustida yotadi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-46 — masofa va kesmaning oʻrtasi
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-46: Nuqtalar orasidagi masofa va kesmaning oʻrtasi",
        "category": "math",
        "order": 46,
        "summary": (
            "Gorizontal va vertikal kesmaning uzunligini modul bilan topish "
            "hamda kesmaning oʻrtasini koordinatalarning yarim yigʻindisi orqali "
            "hisoblash."
        ),
        "stories": ["Ikki uy orasidagi yoʻl"],
        "content": """
<h2>PM-46: Nuqtalar orasidagi masofa va kesmaning oʻrtasi</h2>

<p>«Oʻrtada uchrashamiz» — telefonda aytish oson. Xaritaga qarasangiz esa darrov
savol tugʻiladi: qayeri aynan oʻrtasi? Va umuman, ikki uy orasi qancha? PM-45 da
har bir nuqtaga manzil berdik. Endi shu manzillardan <b>masofa</b>ni ham,
<b>oʻrta nuqta</b>ni ham hisoblab chiqaramiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>son oʻqidagi ikki nuqta orasidagi masofani topasiz;</li>
    <li>gorizontal va vertikal kesmaning uzunligini hisoblaysiz;</li>
    <li>kesmaning oʻrtasini koordinatalari bilan aytasiz;</li>
    <li>oʻrta maʼlum boʻlganda ikkinchi uchni topasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Masofa va oʻrta</span>
  <span class="pe-chip pe-chip--v">|x<sub>2</sub> − x<sub>1</sub>|</span>
  <span class="pe-op">va</span>
  <span class="pe-chip pe-chip--s">(x<sub>1</sub> + x<sub>2</sub>) ÷ 2</span>
</div>

<h3>1. Bitta oʻqda: masofa — bu modul</h3>

<p>Son oʻqida −3 va 5 turibdi. Ular orasi qancha? Sanab chiqish mumkin: −3 dan 0
gacha 3 qadam, 0 dan 5 gacha 5 qadam — jami <b>8</b>.</p>

<div class="pm-num">
  <div class="pm-num__track">
    <span class="pm-num__band" style="left:25%;width:66.7%"></span>
    <span class="pm-num__tick" style="left:0%"><i>−6</i></span>
    <span class="pm-num__tick" style="left:50%"><i>0</i></span>
    <span class="pm-num__tick" style="left:100%"><i>6</i></span>
    <span class="pm-num__dot" style="left:25%"><i>−3</i></span>
    <span class="pm-num__dot" style="left:91.7%"><i>5</i></span>
  </div>
</div>

<p>Sanamasdan ham boʻladi: <b>ayirmani oling va modulini oling</b> (PM-41).</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">|5 − (−3)|</span>
    <span class="pm-solve__why">Ikki sonning ayirmasi, moduli bilan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= |5 + 3| = |8|</span>
    <span class="pm-solve__why">Manfiyni ayirish — qoʻshish (PM-10)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 8</span>
    <span class="pm-solve__why">Masofa — 8 birlik</span>
  </div>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Nega aynan modul?</p>
  <p>Chunki masofa hech qachon manfiy boʻlmaydi. Agar teskari tartibda olsak,
  |−3 − 5| = |−8| = 8 — javob oʻzgarmaydi. <b>Modul qaysi sondan qaysi sonni
  ayirganingizni ahamiyatsiz qiladi</b>, va bu juda qulay: hech narsani
  taqqoslab oʻtirmaysiz.</p>
</div>

<h3>2. Gorizontal kesma</h3>

<p>Tekislikda ikki nuqtaning <b>ordinatalari teng</b> boʻlsa, ular bir xil
balandlikda turadi va kesma gorizontal boʻladi. Bunda faqat x lar farq qiladi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 220" role="img" aria-label="A(−3; 2) va B(5; 2) nuqtalari orasidagi gorizontal masofa">
    <line class="pm-ln" x1="20" y1="150" x2="308" y2="150"/>
    <line class="pm-ln" x1="150" y1="205" x2="150" y2="20"/>
    <polygon class="pm-fill" points="312,150 300,145 300,155"/>
    <line class="pm-ln pm-ln--hl" x1="75" y1="100" x2="275" y2="100"/>
    <circle class="pm-pt" cx="75" cy="100" r="5"/>
    <circle class="pm-pt" cx="275" cy="100" r="5"/>
    <circle class="pm-pt" cx="175" cy="100" r="4"/>
    <line class="pm-ln pm-ln--dash" x1="75" y1="100" x2="75" y2="150"/>
    <line class="pm-ln pm-ln--dash" x1="275" y1="100" x2="275" y2="150"/>
    <text class="pm-lbl" x="70" y="90" text-anchor="middle">A(−3; 2)</text>
    <text class="pm-lbl" x="278" y="90" text-anchor="middle">B(5; 2)</text>
    <text class="pm-lbl pm-lbl--hl" x="175" y="88" text-anchor="middle">M(1; 2)</text>
    <text class="pm-lbl" x="75" y="168" text-anchor="middle">−3</text>
    <text class="pm-lbl" x="275" y="168" text-anchor="middle">5</text>
    <text class="pm-lbl" x="140" y="168">O</text>
    <text class="pm-lbl" x="298" y="170">x</text>
    <text class="pm-lbl" x="160" y="32">y</text>
  </svg>
  <figcaption>AB = |5 − (−3)| = 8 birlik. Oʻrtasi M — har ikki uchdan 4 birlik
  narida.</figcaption>
</figure>

<div class="pe-ex">
  <p class="pe-ex__math">A(−3; 2), B(5; 2) → AB = |5 − (−3)| = 8</p>
  <p class="pe-ex__uz">Ikki nuqta bir xil balandlikda, ular orasi 8 birlik.</p>
  <p class="pe-ex__why">Ordinatalar bir xil boʻlgani uchun y lar hisobga
  qatnashmaydi.</p>
</div>

<h3>3. Vertikal kesma</h3>

<p>Endi <b>abssissalari teng</b> boʻlsin — nuqtalar bir vertikal chiziqda turadi va
endi faqat y lar farq qiladi.</p>

<div class="pe-ex">
  <p class="pe-ex__math">C(2; −1), D(2; 6) → CD = |6 − (−1)| = 7</p>
  <p class="pe-ex__uz">Ikkalasi ham 2 katak oʻngda, biri pastda, biri
  yuqorida.</p>
  <p class="pe-ex__why">−1 dan 0 gacha 1, 0 dan 6 gacha 6 — jami 7 birlik.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Qaysi koordinatani olish kerak?</p>
  <p>Eng koʻp uchraydigan chalkashlik shu. Qoida sodda: <b>oʻzgargan koordinatani
  oling</b>. Gorizontal kesmada y lar bir xil, demak x lar bilan ishlaysiz.
  Vertikal kesmada aksincha. Bir xil boʻlgan koordinata hech qachon masofani
  bermaydi — u faqat kesma qaysi chiziqda turganini aytadi.</p>
</div>

<h3>4. Kesmaning oʻrtasi</h3>

<p>Oʻrta nuqta ikki uchdan teng uzoqlikda turadi. Uni topish uchun hech narsani
sanash kerak emas: <b>har bir koordinatani alohida olib, yarim yigʻindisini
hisoblang</b>.</p>

<div class="pe-formula">
  <span class="pe-formula__label">Oʻrta nuqta</span>
  <span class="pe-chip pe-chip--o">M</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">(x<sub>1</sub> + x<sub>2</sub>) ÷ 2</span>
  <span class="pe-op">;</span>
  <span class="pe-chip pe-chip--v">(y<sub>1</sub> + y<sub>2</sub>) ÷ 2</span>
</div>

<p>Nega yigʻindining yarmi? Chunki ikki sonning roppa-rosa oʻrtasidagi son —
ularning yigʻindisining yarmi. 2 va 8 ning oʻrtasi 5 ekanini bilasiz;
(2 + 8) ÷ 2 = 5 aynan shuni beradi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 230" role="img" aria-label="A(1; 2) va B(7; 6) kesmasining oʻrtasi M(4; 4)">
    <line class="pm-ln" x1="30" y1="200" x2="308" y2="200"/>
    <line class="pm-ln" x1="40" y1="215" x2="40" y2="20"/>
    <line class="pm-ln pm-ln--hl" x1="70" y1="140" x2="250" y2="20"/>
    <circle class="pm-pt" cx="70" cy="140" r="5"/>
    <circle class="pm-pt" cx="250" cy="20" r="5"/>
    <circle class="pm-pt" cx="160" cy="80" r="5"/>
    <line class="pm-ln pm-ln--dash" x1="70" y1="140" x2="70" y2="200"/>
    <line class="pm-ln pm-ln--dash" x1="160" y1="80" x2="160" y2="200"/>
    <line class="pm-ln pm-ln--dash" x1="250" y1="20" x2="250" y2="200"/>
    <text class="pm-lbl" x="66" y="132" text-anchor="end">A(1; 2)</text>
    <text class="pm-lbl pm-lbl--hl" x="168" y="72">M(4; 4)</text>
    <text class="pm-lbl" x="246" y="16" text-anchor="end">B(7; 6)</text>
    <text class="pm-lbl" x="70" y="218" text-anchor="middle">1</text>
    <text class="pm-lbl" x="160" y="218" text-anchor="middle">4</text>
    <text class="pm-lbl" x="250" y="218" text-anchor="middle">7</text>
    <text class="pm-lbl" x="298" y="218">x</text>
    <text class="pm-lbl" x="50" y="30">y</text>
  </svg>
  <figcaption>Oʻrta nuqtaning abssissasi ham 1 va 7 ning oʻrtasida: (1 + 7) ÷ 2 = 4.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">A(1; 2), B(7; 6)</span>
    <span class="pm-solve__why">Kesmaning uchlari</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x: (1 + 7) ÷ 2 = 4</span>
    <span class="pm-solve__why">Abssissalarning yarim yigʻindisi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">y: (2 + 6) ÷ 2 = 4</span>
    <span class="pm-solve__why">Ordinatalarning yarim yigʻindisi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">M(4; 4)</span>
    <span class="pm-solve__why">Kesmaning oʻrtasi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>A dan M gacha gorizontal boʻyicha 4 − 1 = 3, M dan B gacha 7 − 4 = 3 ✓
  Vertikal boʻyicha 4 − 2 = 2 va 6 − 4 = 2 ✓ Ikki tomonga ham bir xil qadam
  tashlandi — demak M haqiqatan oʻrtada.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Qiya kesmaning uzunligi-chi?</p>
  <p>Yuqoridagi chizmada AB kesmasi qiya. Uning <b>oʻrtasini</b> topdik, lekin
  <b>uzunligini</b> hali topa olmaymiz — buning uchun Pifagor teoremasi kerak, u
  esa <b>PM-64</b> darsida boʻladi. Hozircha qiya masofani ikki qismga boʻlib
  baholang: gorizontal 6, vertikal 4 — demak toʻgʻri masofa 6 dan katta, lekin
  6 + 4 = 10 dan kichik.</p>
</div>

<h3>5. Teskari savol: oʻrta maʼlum, uchi nomaʼlum</h3>

<p>Baʼzan oʻrta nuqta beriladi va ikkinchi uchni topish kerak boʻladi. Bunda
oʻylash oson: <b>uchdan oʻrtagacha qancha yurilgan boʻlsa, oʻrtadan ikkinchi
uchgacha ham xuddi shuncha yuriladi.</b></p>

<div class="pe-ex">
  <p class="pe-ex__math">A(−6; 2), M(−1; 2) → B(4; 2)</p>
  <p class="pe-ex__uz">A dan M gacha 5 katak oʻngga yurildi, demak M dan B gacha
  yana 5 katak oʻngga.</p>
  <p class="pe-ex__why">Tekshirish: (−6 + 4) ÷ 2 = −1 ✓ va (2 + 2) ÷ 2 = 2 ✓</p>
</div>

<h3>Matnli masala</h3>

<p><b>Uchrashuv joyi.</b> Shahar koʻchalari katak boʻlib joylashgan. Xaritada
Afsonaning uyi <b>(−3; 4)</b>, Dilnozaning uyi esa <b>(5; 4)</b> nuqtada. Bitta
katakning tomoni — <b>150 metr</b>. Ikkalasi teng masofa yurib uchrashmoqchi.</p>

<p><b>Savol:</b> uchrashuv joyi qaysi nuqtada va har biri necha metr yuradi? Shu
joyga (1; −2) da yashaydigan Jasur ham kelmoqchi — u necha metr yuradi?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Ordinatalar teng: 4 va 4</span>
    <span class="pm-solve__why">Ikkala uy bir koʻchada — yoʻl gorizontal</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">|5 − (−3)| = 8 katak</span>
    <span class="pm-solve__why">Uylar orasidagi masofa</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">M: (−3 + 5) ÷ 2 = 1; (4 + 4) ÷ 2 = 4 → M(1; 4)</span>
    <span class="pm-solve__why">Uchrashuv joyi — kesmaning oʻrtasi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">8 ÷ 2 = 4 katak → 4 × 150 = 600 m</span>
    <span class="pm-solve__why">Har biri yarim yoʻlni bosadi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Jasur: |4 − (−2)| = 6 katak → 900 m</span>
    <span class="pm-solve__why">Uning abssissasi ham 1 — yoʻli vertikal</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Afsona (−3; 4) dan (1; 4) gacha: 4 katak ✓ Dilnoza (5; 4) dan (1; 4) gacha:
  4 katak ✓ Ikkalasi 600 metrdan, jami 1200 metr — bu uylar orasidagi 8 × 150 =
  1200 metrga teng ✓ Jasur esa (1; −2) dan (1; 4) gacha 6 katak, yaʼni 900
  metr.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Bir katak 150 metr, uylar orasi 8 katak — taxminan 8 × 150 ≈ 1200 metr,
  yaʼni bir kilometrdan sal koʻproq. Piyoda 15 daqiqalik yoʻl: mantiqiy.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">A(−3; 2), B(5; 2): AB = 5 − 3 = 2</p>
  <p class="pe-fix__good">AB = |5 − (−3)| = |5 + 3| = 8</p>
  <p class="pe-fix__why">Manfiy sonning minusi tushirib qoldirilgan. Manfiy sonni
  ayirish — uni qoʻshish demakdir (PM-10).</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">A(1; 2), B(7; 6) ning oʻrtasi: ((7 − 1) ÷ 2; (6 − 2) ÷ 2) = (3; 2)</p>
  <p class="pe-fix__good">M = ((1 + 7) ÷ 2; (2 + 6) ÷ 2) = (4; 4)</p>
  <p class="pe-fix__why">Ayirmaning yarmi — bu kesmaning <b>yarim uzunligi</b>,
  oʻrta nuqtaning manzili emas. Oʻrta uchun <b>yigʻindi</b> olinadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">A(1; 5), B(7; 5): AB = |5 − 5| = 0</p>
  <p class="pe-fix__good">AB = |7 − 1| = 6</p>
  <p class="pe-fix__why">Bir xil boʻlgan koordinata olingan. Gorizontal kesmada
  masofani <b>abssissalar</b> beradi, ordinatalar esa faqat balandlikni.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. A(−5; 3) va B(4; 3) orasidagi masofani toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>9 birlik.</b> Ordinatalar teng, demak |4 − (−5)| = |4 + 5| = 9.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. C(−2; −7) va D(−2; −1) orasidagi masofani toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>6 birlik.</b> Abssissalar teng — kesma vertikal:
    |−1 − (−7)| = |−1 + 7| = 6.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. A(2; 3) va B(8; 11) kesmasining oʻrtasini toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>M(5; 7).</b> x: (2 + 8) ÷ 2 = 5; y: (3 + 11) ÷ 2 = 7. Tekshirish:
    5 − 2 = 3 va 8 − 5 = 3 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. AB kesmasining oʻrtasi M(−1; 2), bitta uchi esa
  A(−6; 2). Ikkinchi uchi qayerda?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>B(4; 2).</b> A dan M gacha 5 katak oʻngga yurildi, oʻrtadan ham
    xuddi shuncha: −1 + 5 = 4. Tekshirish: (−6 + 4) ÷ 2 = −1 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Bekzodning uyi xaritada (−4; −2), maktab esa (−4; 6)
  nuqtada. Har katak 50 metr. Yoʻlning roppa-rosa yarmida buloq bor. Buloqning
  koordinatasi qanday va Bekzod unga qadar necha metr yuradi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Buloq (−4; 2) da, unga qadar 200 metr.</b> Yoʻl vertikal:
    |6 − (−2)| = 8 katak. Oʻrtasi: x oʻzgarmaydi (−4), y: (−2 + 6) ÷ 2 = 2.
    Uygacha 4 katak, yaʼni 4 × 50 = 200 metr.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Masofa</b><span>ikki nuqta orasidagi uzunlik, hech qachon manfiy emas;
    ingl. distance</span></li>
  <li><b>Kesma</b><span>ikki uchi bor toʻgʻri chiziq boʻlagi; ingl.
    segment</span></li>
  <li><b>Kesmaning uchlari</b><span>uni chegaralovchi ikki nuqta; ingl.
    endpoints</span></li>
  <li><b>Kesmaning oʻrtasi</b><span>uchlardan teng uzoqlikdagi nuqta; ingl.
    midpoint</span></li>
  <li><b>Modul</b><span>sonning noldan uzoqligi, |a|; ingl. absolute
    value</span></li>
  <li><b>Gorizontal</b><span>ufqqa parallel, chapdan oʻngga; ingl.
    horizontal</span></li>
  <li><b>Vertikal</b><span>tik, pastdan yuqoriga; ingl. vertical</span></li>
  <li><b>Koordinatalar ayirmasi</b><span>x<sub>2</sub> − x<sub>1</sub>; ingl.
    difference of coordinates</span></li>
  <li><b>Yarim yigʻindi</b><span>ikki sonning yigʻindisining yarmi; ingl.
    half-sum</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Masofa — ayirmaning moduli:</b> |x<sub>2</sub> − x<sub>1</sub>|. Qaysi
      sondan qaysinisini ayirish farq qilmaydi.</li>
    <li><b>Oʻrta — yigʻindining yarmi</b>, ayirmaning emas; har bir koordinata
      alohida hisoblanadi.</li>
    <li><b>Oʻzgargan koordinatani oling:</b> gorizontal kesmada x lar, vertikal
      kesmada y lar ishlaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-47 — funksiya gʻoyasi
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-47: Funksiya gʻoyasi: kirish → qoida → chiqish",
        "category": "math",
        "order": 47,
        "summary": (
            "Funksiya — ishonchli mashina: har bir kirishga faqat bitta chiqish. "
            "Uni soʻz, jadval va formula bilan yozish, f(x) belgisi va teskari "
            "savol."
        ),
        "stories": ["Mashina qanday ishlaydi: kirish va chiqish"],
        "content": """
<h2>PM-47: Funksiya gʻoyasi: kirish → qoida → chiqish</h2>

<p>Suv avtomatiga 2000 soʻm tashlaysiz — bir litr suv tushadi. Yana 2000 soʻm
tashlaysiz — yana bir litr. Har safar. Agar bir kuni 2000 soʻmga yarim litr
tushsa, siz avtomatni <b>buzilgan</b> deysiz.</p>

<p>Mana shu «buzilmagan» degan talab matematikada eng koʻp ishlatiladigan
gʻoyalardan biriga aylangan. U <b>funksiya</b> deyiladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>funksiyani kirish–qoida–chiqish sifatida tushunasiz;</li>
    <li>uni jadval va formula bilan yozasiz;</li>
    <li>f(x) belgisini oʻqiysiz va qiymatini hisoblaysiz;</li>
    <li>chiqish maʼlum boʻlganda kirishni topasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Funksiya</span>
  <span class="pe-chip pe-chip--s">kirish x</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">qoida</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">chiqish y</span>
</div>

<h3>1. Mashina obrazi</h3>

<p>Funksiyani mashina deb tasavvur qiling. Unga bitta son kiritasiz, u oʻzining
qoidasini bajaradi va bitta son qaytaradi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 150" role="img" aria-label="Funksiya mashinasi: kirish 4, qoida 2x plus 3, chiqish 11">
    <line class="pm-ln pm-ln--hl" x1="20" y1="75" x2="98" y2="75"/>
    <polygon class="pm-fill--hl" points="110,75 96,69 96,81"/>
    <rect class="pm-fill" x="112" y="35" width="96" height="80"/>
    <rect class="pm-ln" x="112" y="35" width="96" height="80" fill="none"/>
    <line class="pm-ln pm-ln--hl" x1="210" y1="75" x2="288" y2="75"/>
    <polygon class="pm-fill--hl" points="300,75 286,69 286,81"/>
    <text class="pm-lbl" x="60" y="60" text-anchor="middle">kirish</text>
    <text class="pm-lbl pm-lbl--hl" x="60" y="100" text-anchor="middle">x = 4</text>
    <text class="pm-lbl" x="160" y="70" text-anchor="middle">qoida:</text>
    <text class="pm-lbl pm-lbl--hl" x="160" y="92" text-anchor="middle">2x + 3</text>
    <text class="pm-lbl" x="255" y="60" text-anchor="middle">chiqish</text>
    <text class="pm-lbl pm-lbl--hl" x="255" y="100" text-anchor="middle">y = 11</text>
  </svg>
  <figcaption>4 kiradi, mashina uni 2 ga koʻpaytirib 3 qoʻshadi, 11 chiqadi.</figcaption>
</figure>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Funksiyaning yagona sharti</p>
  <p><b>Har bir kirishga faqat va faqat bitta chiqish toʻgʻri kelishi kerak.</b>
  Bir xil sonni ikki marta kiritganda ikki xil javob chiqsa, bu funksiya emas —
  buzilgan avtomat. Butun matematika shu ishonchlilikka tayanadi.</p>
</div>

<h3>2. Funksiyani uch xil yozish mumkin</h3>

<p>Bitta qoidani uch xil koʻrinishda yozib boʻladi. Uchalasi bir narsa haqida
gapiradi.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Soʻz bilan</p>
    <p>«Sonni ikkiga koʻpaytir, ustiga uch qoʻsh.»</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Formula bilan</p>
    <p>y = 2x + 3</p>
  </div>
</div>

<p>Uchinchisi — <b>jadval</b>. Bir nechta kirishni tanlaymiz va har biriga
javobni hisoblaymiz.</p>

<div class="pe-table-wrap"><table>
  <tr><th>x (kirish)</th><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr>
  <tr><th>y (chiqish)</th><td>3</td><td>5</td><td>7</td><td>9</td><td>11</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__math">x = 3 → y = 2 × 3 + 3 = 6 + 3 = 9</p>
  <p class="pe-ex__uz">Uchni ikkiga koʻpaytirdik, keyin uch qoʻshdik.</p>
  <p class="pe-ex__why">Avval koʻpaytirish, keyin qoʻshish — amallar tartibi
  (PM-5).</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Qavs yoʻq joyga qavs qoʻymang</p>
  <p>y = 2x + 3 da x = 4 boʻlsa, javob 2 × 4 + 3 = <b>11</b>. Koʻpchilik
  2 × (4 + 3) = 14 deb yozadi — bu boshqa mashina, boshqa qoida. Formulada qavs
  yoʻq ekan, demak avval koʻpaytiriladi.</p>
</div>

<h3>3. f(x) belgisi</h3>

<p>Mashinaga nom berish qulay. Odatda uni <b>f</b> deb atashadi va shunday
yozishadi:</p>

<div class="pe-formula">
  <span class="pe-formula__label">Yozuvni oʻqish</span>
  <span class="pe-chip pe-chip--o">f(4) = 11</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--aux">«f mashinasiga 4 kirsa, 11 chiqadi»</span>
</div>

<p>Bu yerda <b>x</b> — <b>argument</b> (kirish), <b>f(x)</b> esa
<b>funksiyaning qiymati</b> (chiqish). Demak y = f(x) — bir xil narsaning ikki
xil yozuvi.</p>

<div class="pe-ex">
  <p class="pe-ex__math">f(x) = x<sup>2</sup> + 1 boʻlsa, f(−3) = (−3)<sup>2</sup> + 1 = 9 + 1 = 10</p>
  <p class="pe-ex__uz">Manfiy uchni kvadratga koʻtardik va bir qoʻshdik.</p>
  <p class="pe-ex__why">(−3)<sup>2</sup> = 9, chunki ikkita manfiyning koʻpaytmasi
  musbat (PM-11).</p>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">f(4) — koʻpaytma emas</p>
  <p>f(4) yozuvi «f ni 4 ga koʻpaytir» degani <b>emas</b>. Bu — mashinaning nomi va
  unga kiritilgan son. Xuddi telefon raqamiga oʻxshaydi: qavs ichidagi son kimga
  qoʻngʻiroq qilinayotganini emas, nima kiritilganini koʻrsatadi.</p>
</div>

<h3>4. Teskari savol: chiqish maʼlum, kirish nomaʼlum</h3>

<p>Koʻpincha aksincha soʻraladi: «chiqish 23 boʻlishi uchun nima kiritish kerak?»
Bunda formulani qayta qoʻllash emas, <b>tenglama yechish</b> kerak (PM-36).</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + 3 = 23</span>
    <span class="pm-solve__why">Chiqishni formulaga tenglashtirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x = 20</span>
    <span class="pm-solve__why">Ikki tomondan 3 ni ayirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 10</span>
    <span class="pm-solve__why">Ikki tomonni 2 ga boʻldik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>x = 10 ni mashinaga kiritamiz: 2 × 10 + 3 = 23 ✓ Javob toʻgʻri.
  <b>Funksiya masalasida tekshirish har doim shunday</b> — topilgan kirishni
  qoidaga qoʻyib koʻring.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Bosmaxona hisobi.</b> Bosmaxona har bir buyurtma uchun <b>15 000 soʻm</b>
tayyorgarlik haqi oladi, ustiga har bir nusxa uchun <b>500 soʻm</b> qoʻshadi.</p>

<p><b>Savol:</b> narxni funksiya koʻrinishida yozing. 40 nusxa necha soʻm turadi?
Sinf 60 000 soʻm ajratgan boʻlsa, nechta nusxa buyurtma qilish mumkin?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x — nusxalar soni</span>
    <span class="pm-solve__why">Kirish nima ekanini aniqladik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">N(x) = 15 000 + 500x</span>
    <span class="pm-solve__why">Oʻzgarmas haq va nusxaga bogʻliq qism</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">N(40) = 15 000 + 500 × 40 = 35 000</span>
    <span class="pm-solve__why">40 nusxa 35 000 soʻm</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">15 000 + 500x = 60 000</span>
    <span class="pm-solve__why">Endi teskari savol — tenglama</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">500x = 45 000 → x = 90</span>
    <span class="pm-solve__why">60 000 soʻmga 90 nusxa chiqadi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>90 nusxa: 15 000 + 500 × 90 = 15 000 + 45 000 = 60 000 ✓ Roppa-rosa
  budjetga toʻgʻri keldi. 100 nusxa boʻlsa 65 000 soʻm boʻlardi — bu esa pul
  yetmasligini bildiradi.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Tayyorgarlikni hisobga olmasak, 60 000 ÷ 500 = 120 nusxa chiqadi. Demak
  javob 120 dan kichik boʻlishi shart. 90 — mos; 130 chiqsa, xato qilingan
  boʻlardi.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">y = 2x + 3, x = 4 → y = 2 × (4 + 3) = 14</p>
  <p class="pe-fix__good">y = 2 × 4 + 3 = 11</p>
  <p class="pe-fix__why">Formulada qavs yoʻq. Amallar tartibi boʻyicha avval
  koʻpaytirish bajariladi (PM-5).</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">f(4) = f × 4</p>
  <p class="pe-fix__good">f(4) — funksiyaning x = 4 dagi qiymati</p>
  <p class="pe-fix__why">f — mashinaning nomi, koʻpaytuvchi emas. Qavs bu yerda
  koʻpaytirishni emas, kiritishni bildiradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">y = 2x + 3 da y = 25 boʻlsa, x = 2 × 25 + 3 = 53</p>
  <p class="pe-fix__good">2x + 3 = 25 → 2x = 22 → x = 11</p>
  <p class="pe-fix__why">Teskari savolda qoida qayta qoʻllanmaydi — tenglama
  yechiladi (PM-36). Tekshirish: 2 × 11 + 3 = 25 ✓</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. y = 3x − 1 boʻlsa, x = 5 da y nechaga teng?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>14.</b> 3 × 5 = 15, keyin 15 − 1 = 14.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. f(x) = x<sup>2</sup> + 1 boʻlsa, f(−3) nechaga teng?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>10.</b> (−3)<sup>2</sup> = 9 (ikkita manfiyning koʻpaytmasi musbat),
    keyin 9 + 1 = 10.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. y = 10 − 2x jadvalini x = 0, 1, 2, 3, 4 uchun
  toʻldiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>10, 8, 6, 4, 2.</b> Har safar x bir birlikka oʻssa, y ikki birlikka
    kamayadi — chunki oldida −2 turibdi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. y = 4x + 2 boʻlsa, y = 30 boʻlishi uchun x qanday
  boʻlishi kerak?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>x = 7.</b> 4x + 2 = 30 → 4x = 28 → x = 7. Tekshirish:
    4 × 7 + 2 = 30 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Sport zali oyiga 80 000 soʻm obuna haqi oladi, ustiga
  har bir mashgʻulot uchun 5 000 soʻm. Bir oyda 12 marta borgan Dilnoza qancha
  toʻlaydi? Bekzod 175 000 soʻm toʻlagan boʻlsa, u necha marta borgan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Dilnoza 140 000 soʻm; Bekzod 19 marta borgan.</b> Qoida:
    T(x) = 80 000 + 5 000x. T(12) = 80 000 + 60 000 = 140 000. Teskari savol:
    80 000 + 5 000x = 175 000 → 5 000x = 95 000 → x = 19. Tekshirish:
    80 000 + 95 000 = 175 000 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Funksiya</b><span>har bir kirishga bitta chiqish beruvchi qoida; ingl.
    function</span></li>
  <li><b>Argument</b><span>kirish soni, x; ingl. argument, input</span></li>
  <li><b>Funksiyaning qiymati</b><span>chiqish soni, f(x); ingl. value,
    output</span></li>
  <li><b>Oʻzgaruvchi</b><span>qiymati oʻzgarib turadigan harf; ingl.
    variable</span></li>
  <li><b>Erkli oʻzgaruvchi</b><span>biz tanlaydigan x; ingl. independent
    variable</span></li>
  <li><b>Erksiz oʻzgaruvchi</b><span>x ga bogʻliq boʻlgan y; ingl. dependent
    variable</span></li>
  <li><b>Qoida</b><span>kirishdan chiqishga oʻtish usuli; ingl. rule</span></li>
  <li><b>Qiymatlar jadvali</b><span>x va y juftliklari roʻyxati; ingl. table of
    values</span></li>
  <li><b>Oʻzgarmas had</b><span>kirishga bogʻliq boʻlmagan qism; ingl. constant
    term</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Funksiya — ishonchli mashina:</b> bitta kirishga bitta chiqish, har
      safar bir xil.</li>
    <li><b>f(4) — bu koʻpaytma emas</b>, bu 4 kiritilgandagi javob.</li>
    <li><b>Toʻgʻri savolga toʻgʻri amal:</b> kirish maʼlum boʻlsa qoʻyib
      hisoblaysiz, chiqish maʼlum boʻlsa tenglama yechasiz.</li>
  </ul>
</div>
""",
    },
]
