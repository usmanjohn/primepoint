# -*- coding: utf-8 -*-
"""Prime Math — darslar 66–68 (toʻrtburchaklar oilasi, perimetr, yuza 1).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt
**Blok E: Geometriya** — har bir darsda SVG chizma SHART.

  mashqlar — practice/management/commands/_practice_pm_66_68.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_66_68.py

⚠️ Chizmalar QOʻLDA hisoblanmagan: _svgkit.py + scratchpad/gen_pm66_68.py
   bilan generatsiya qilingan, verify_pm_66_68.py esa ularni qaytadan
   oʻlchaydi (parallelogrammning qarama-qarshi tomonlari haqiqatan teng va
   burchaklari 65/115 mi, trapetsiya teng yonlimi, L shaklning perimetri
   40 mi, uchburchak oʻrovchi toʻrtburchakning aynan yarmimi).

⚠️ Kumulyativ chegaralar — bu blokda tartib juda muhim:
  • PM-66 — faqat TAʼRIF va BURCHAK: toʻrtburchak 360°, parallelogramm
    xossalari, oila daraxti, trapetsiya. ⛔ PERIMETR (PM-67) va YUZA
    (PM-68) bu darsda YOʻQ — na matnda, na mashqda;
  • PM-67 — perimetr. ⛔ Yuza hali yoʻq: «ichi» haqida faqat bitta
    oldinga qarash jumlasi bor, hisob yoʻq;
  • PM-68 — yuza: toʻgʻri toʻrtburchak va uchburchak. Uchburchak yuzasi
    OʻROVCHI TOʻRTBURCHAKNING YARMI orqali isbotlanadi (balandlik uni
    ikkita toʻgʻri toʻrtburchakka boʻladi va uchburchak har birining
    yarmini egallaydi) — ⛔ parallelogramm yuzasi (PM-69) ISHLATILMAYDI.
  • ⛔ Aylana va π (PM-70), oʻxshashlik (PM-72), hajm (PM-74) YOʻQ.
  • Faol ishlatiladi: parallel chiziqlar va bir tomonli ichki burchaklar
    (PM-60) — parallelogrammning qoʻshni burchaklari nega 180° berishi
    aynan shundan; uchburchak burchaklari 180° (PM-61); teng yonli
    uchburchak (PM-63); Pifagor (PM-64/65); oʻnlik kasr (PM-20/21);
    foiz (PM-23); yaxlitlash (PM-14).

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_66_68.py --author=prime
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
    # PM-66 — toʻrtburchaklar oilasi
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-66: Toʻrtburchaklar oilasi: kvadrat, romb, parallelogramm, trapetsiya",
        "category": "math",
        "order": 66,
        "summary": (
            "Toʻrtburchaklarning hammasi bitta oila: burchaklari yigʻindisi "
            "360°. Parallelogramm, toʻgʻri toʻrtburchak, romb, kvadrat va "
            "trapetsiya bir-biridan qanday shart bilan ajraladi."
        ),
        "stories": ["Gilam naqshidagi shakllar"],
        "content": """
<h2>PM-66: Toʻrtburchaklar oilasi: kvadrat, romb, parallelogramm, trapetsiya</h2>

<p>Xonangizga qarang: deraza, eshik, stol usti, kitob, ekran, gilamdagi
naqsh. Deyarli hammasi toʻrt tomonli. Lekin ularning nomi har xil — biri
kvadrat, biri toʻgʻri toʻrtburchak, gilamdagi naqsh esa romb.</p>

<p>Farq qayerda va kim kimga qarindosh? Bu dars — shakllarning oilaviy
daraxti.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>toʻrtburchakning burchaklari nega 360° berishini isbotlaysiz;</li>
    <li>parallelogrammning xossalarini bilib, nomaʼlum burchakni
      topasiz;</li>
    <li>kvadrat, romb va toʻgʻri toʻrtburchakni bir-biridan ajratasiz;</li>
    <li>trapetsiya nima bilan boshqalardan farq qilishini aytasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Har qanday toʻrtburchakda</span>
  <span class="pe-chip pe-chip--o">∠1 + ∠2 + ∠3 + ∠4</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">360°</span>
</div>

<h3>1. Nega 360°?</h3>

<p>Uchburchakda burchaklar yigʻindisi 180° edi (PM-61). Toʻrtburchakda
qancha? Yodlash shart emas — bir chizib koʻrsak, oʻzi chiqadi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 205" role="img"
       aria-label="Toʻrtburchak diagonal bilan ikkita uchburchakka boʻlinadi">
    <polygon class="pm-fill" points="40,40 272,28 286,168 58,186"/>
    <polyline class="pm-ln" points="40,40 272,28 286,168 58,186 40,40" fill="none"/>
    <line class="pm-ln pm-ln--hl" x1="40" y1="40" x2="286" y2="168"/>
    <path class="pm-ln" d="M 42.9 63.8 A 24 24 0 0 0 64 38.8" fill="none"/>
    <path class="pm-ln" d="M 248 29.2 A 24 24 0 0 0 274.4 51.9" fill="none"/>
    <path class="pm-ln" d="M 283.6 144.1 A 24 24 0 0 0 262.1 169.9" fill="none"/>
    <path class="pm-ln" d="M 81.9 184.1 A 24 24 0 0 0 55.1 162.2" fill="none"/>
    <text class="pm-lbl pm-lbl--hl" x="183.3" y="82.7">180°</text>
    <text class="pm-lbl pm-lbl--hl" x="112" y="135.3">180°</text>
  </svg>
  <figcaption>Bitta diagonal toʻrtburchakni ikkita uchburchakka boʻladi.
  Har birida 180°, demak toʻrtburchakda 180 + 180 = 360°.</figcaption>
</figure>

<p>Qarama-qarshi ikki uchni <b>diagonal</b> bilan tutashtiramiz. Toʻrtburchak
ikkita uchburchakka boʻlinadi. Ularning burchaklari birgalikda aynan
toʻrtburchakning burchaklarini tashkil qiladi — bittasi ham qoʻshilmadi,
bittasi ham yoʻqolmadi.</p>

<div class="pm-solve">
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">180 + 180 = 360°</span>
    <span class="pm-solve__why">Har qanday toʻrtburchakda, hatto qiyshigʻida
    ham</span>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">Uch burchagi 90°, 85° va 100° → 360 − 275 = 85°</p>
  <p class="pe-ex__uz">Toʻrtinchi burchak 85 gradus.</p>
  <p class="pe-ex__why">Uchtasini qoʻshib, 360 dan ayirdik: 90 + 85 + 100 =
  275.</p>
</div>

<h3>2. Parallelogramm</h3>

<p><b>Parallelogramm</b> — qarama-qarshi tomonlari juft-juft <b>parallel</b>
boʻlgan toʻrtburchak (PM-60).</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 205" role="img"
       aria-label="Parallelogramm: qarama-qarshi burchaklar 65 va 115 gradus">
    <polygon class="pm-fill" points="55,160 195,160 241.5,60.3 101.5,60.3"/>
    <polyline class="pm-ln" points="55,160 195,160 241.5,60.3 101.5,60.3 55,160" fill="none"/>
    <polyline class="pm-ln" points="119,166 131,160 119,154" fill="none"/>
    <polyline class="pm-ln" points="165.5,66.3 177.5,60.3 165.5,54.3" fill="none"/>
    <line class="pm-ln" x1="72.8" y1="107.6" x2="83.7" y2="112.7"/>
    <line class="pm-ln" x1="212.8" y1="107.6" x2="223.7" y2="112.7"/>
    <path class="pm-ln pm-ln--hl" d="M 89 160 A 34 34 0 0 0 69.4 129.2" fill="none"/>
    <path class="pm-ln" d="M 207.7 132.8 A 30 30 0 0 0 165 160" fill="none"/>
    <path class="pm-ln pm-ln--hl" d="M 207.5 60.3 A 34 34 0 0 0 227.1 91.1" fill="none"/>
    <path class="pm-ln" d="M 88.8 87.5 A 30 30 0 0 0 131.5 60.3" fill="none"/>
    <text class="pm-lbl pm-lbl--hl" x="88.1" y="136.6">65°</text>
    <text class="pm-lbl" x="155.9" y="125.7">115°</text>
    <text class="pm-lbl pm-lbl--hl" x="186.8" y="92.7">65°</text>
    <text class="pm-lbl" x="111.8" y="103.6">115°</text>
    <text class="pm-lbl" x="39" y="176">A</text>
    <text class="pm-lbl" x="203" y="176">B</text>
    <text class="pm-lbl" x="249.5" y="54.3">C</text>
    <text class="pm-lbl" x="85.5" y="54.3">D</text>
  </svg>
  <figcaption>Qarama-qarshi burchaklar teng (65° va 65°, 115° va 115°),
  qoʻshni burchaklar esa 180° ni beradi: 65 + 115 = 180.</figcaption>
</figure>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Parallelogrammning xossalari</p>
  <p>1. Qarama-qarshi tomonlar <b>teng</b>.
  <br>2. Qarama-qarshi burchaklar <b>teng</b>.
  <br>3. Qoʻshni burchaklar yigʻindisi <b>180°</b>.
  <br>4. Diagonallari kesishib, bir-birini <b>teng ikkiga</b> boʻladi.</p>
</div>

<p>Uchinchi xossa bizga tanish joydan keladi. AB va DC parallel, AD esa
ularni kesib oʻtuvchi (PM-60). ∠A va ∠D — <b>bir tomonli ichki
burchaklar</b>, ularning yigʻindisi esa 180°:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">∠A = 65°</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">∠D = 180 − 65 = 115°</span>
    <span class="pm-solve__why">Bir tomonli ichki burchaklar (PM-60)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">∠C = 65°, ∠B = 115°</span>
    <span class="pm-solve__why">Qarama-qarshilari teng</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>65 + 115 + 65 + 115 = 360 ✓ — toʻrtburchakning qoidasi bajarildi.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Qarama-qarshi va qoʻshni — bu ikki boshqa narsa</p>
  <p><b>Qarama-qarshi</b> burchaklar roʻparama-roʻpara turadi va ular
  <b>teng</b>. <b>Qoʻshni</b> burchaklar bitta tomonni baham koʻradi va
  ular <b>180°</b> ni beradi. Chalkashtirsangiz, 65° oʻrniga 115° yozib
  qoʻyasiz. Chizmada barmoq bilan koʻrsatib tekshiring.</p>
</div>

<h3>3. Uchta maxsus parallelogramm</h3>

<p>Parallelogrammga qoʻshimcha shart qoʻysak, u alohida nom oladi.</p>

<div class="pe-table-wrap"><table>
  <tr><th>Nomi</th><th>Qoʻshimcha shart</th><th>Nima kelib chiqadi</th></tr>
  <tr><td>Toʻgʻri toʻrtburchak</td><td>burchaklari 90°</td>
      <td>diagonallari teng</td></tr>
  <tr><td>Romb</td><td>tomonlari teng</td>
      <td>diagonallari perpendikulyar</td></tr>
  <tr><td>Kvadrat</td><td>ikkala shart ham</td>
      <td>ikkalasining hamma xossasi</td></tr>
</table></div>

<p><b>Kvadrat</b> — oiladagi eng «boy» aʼzo: u ayni paytda parallelogramm
ham, toʻgʻri toʻrtburchak ham, romb ham. Shuning uchun yuqoridagi hamma
xossa unga tegishli.</p>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Bitta burchak yetadi</p>
  <p>Parallelogrammning <b>bitta</b> burchagi 90° boʻlsa, qolgan uchtasi
  ham 90° boʻlib qoladi: qoʻshnisi 180 − 90 = 90, qarama-qarshisi ham 90.
  Shuning uchun usta xonaning faqat bitta burchagini tekshiradi.</p>
</div>

<h3>4. Trapetsiya — oiladan tashqaridagi qarindosh</h3>

<figure class="pm-fig">
  <svg viewBox="0 0 320 200" role="img"
       aria-label="Teng yonli trapetsiya: faqat bitta juft tomoni parallel">
    <polygon class="pm-fill" points="45,165 275,165 215,70 105,70"/>
    <polyline class="pm-ln" points="45,165 275,165 215,70 105,70 45,165" fill="none"/>
    <polyline class="pm-ln" points="154,171 166,165 154,159" fill="none"/>
    <polyline class="pm-ln" points="154,76 166,70 154,64" fill="none"/>
    <line class="pm-ln pm-ln--hl" x1="69.9" y1="114.3" x2="80.1" y2="120.7"/>
    <line class="pm-ln pm-ln--hl" x1="239.9" y1="120.7" x2="250.1" y2="114.3"/>
    <text class="pm-lbl" x="122" y="186">katta asos</text>
    <text class="pm-lbl" x="128" y="62">kichik asos</text>
    <text class="pm-lbl pm-lbl--hl" x="16" y="112">yon</text>
    <text class="pm-lbl pm-lbl--hl" x="268" y="112">yon</text>
  </svg>
  <figcaption>Trapetsiyada faqat <b>bitta</b> juft tomon parallel. Yon
  tomonlari teng boʻlsa, u teng yonli trapetsiya deyiladi.</figcaption>
</figure>

<p><b>Trapetsiya</b> — faqat <b>bitta</b> juft tomoni parallel boʻlgan
toʻrtburchak. Parallel tomonlar <b>asoslar</b>, qolgan ikkitasi <b>yon
tomonlar</b> deyiladi.</p>

<p>Yon tomonlari teng boʻlsa — <b>teng yonli trapetsiya</b>. Unda bitta
asosdagi ikki burchak ham teng boʻladi, xuddi teng yonli uchburchakdagidek
(PM-63).</p>

<div class="pe-ex">
  <p class="pe-ex__math">Trapetsiyaning katta asosidagi burchaklari 70° va 70°</p>
  <p class="pe-ex__uz">Kichik asosdagi burchaklar: 180 − 70 = 110° va 110°.</p>
  <p class="pe-ex__why">Yon tomon ikki parallel asosni kesib oʻtadi, demak
  yuqori va quyi burchaklar bir tomonli ichki burchaklar — yigʻindisi 180°
  (PM-60). Tekshiruv: 70 + 70 + 110 + 110 = 360 ✓</p>
</div>

<h3>5. Oila daraxti</h3>

<figure class="pm-fig">
  <svg viewBox="0 0 320 240" role="img"
       aria-label="Toʻrtburchaklar oilasi: toʻrtburchakdan parallelogramm va trapetsiya, undan toʻgʻri toʻrtburchak va romb, ikkalasidan kvadrat">
    <line class="pm-ln pm-ln--dash" x1="160" y1="34" x2="80" y2="74"/>
    <line class="pm-ln pm-ln--dash" x1="160" y1="34" x2="238" y2="74"/>
    <line class="pm-ln pm-ln--dash" x1="80" y1="100" x2="60" y2="140"/>
    <line class="pm-ln pm-ln--dash" x1="80" y1="100" x2="174" y2="140"/>
    <line class="pm-ln pm-ln--dash" x1="60" y1="180" x2="110" y2="206"/>
    <line class="pm-ln pm-ln--dash" x1="174" y1="166" x2="110" y2="206"/>
    <rect class="pm-ln" x="110" y="8" width="100" height="26" fill="none"/>
    <text class="pm-lbl" x="119.2" y="25.5">Toʻrtburchak</text>
    <rect class="pm-ln" x="14" y="74" width="132" height="26" fill="none"/>
    <text class="pm-lbl" x="32.4" y="91.5">Parallelogramm</text>
    <rect class="pm-ln" x="186" y="74" width="104" height="26" fill="none"/>
    <text class="pm-lbl" x="204" y="91.5">Trapetsiya</text>
    <rect class="pm-ln" x="8" y="140" width="104" height="40" fill="none"/>
    <text class="pm-lbl" x="36.2" y="157">Toʻgʻri</text>
    <text class="pm-lbl" x="19.2" y="173">toʻrtburchak</text>
    <rect class="pm-ln" x="136" y="140" width="76" height="26" fill="none"/>
    <text class="pm-lbl" x="160.4" y="157.5">Romb</text>
    <rect class="pm-ln" x="66" y="206" width="88" height="26" fill="none"/>
    <text class="pm-lbl" x="86.2" y="223.5">Kvadrat</text>
  </svg>
  <figcaption>Pastga tushgan sari shart koʻpayadi. Kvadrat ikkala yoʻldan
  ham chiqadi: u ham toʻgʻri toʻrtburchak, ham romb.</figcaption>
</figure>

<p>Daraxtni <b>pastdan yuqoriga</b> oʻqing: har bir shakl oʻzidan
yuqoridagining hamma xossasiga ega. Kvadrat — romb, demak tomonlari teng.
Kvadrat — toʻgʻri toʻrtburchak, demak burchaklari 90°.</p>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Yuqoriga qarab ishlaydi, pastga qarab yoʻq</p>
  <p>«Har bir kvadrat — romb» — <b>toʻgʻri</b>. «Har bir romb — kvadrat» —
  <b>notoʻgʻri</b>: gilamdagi qiyshiq romblarning burchagi 90° emas.
  Xuddi shunday, har bir kvadrat toʻgʻri toʻrtburchak, lekin har bir
  toʻgʻri toʻrtburchak kvadrat emas.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Darvoza paneli.</b> Karim aka darvozaga naqshli panel yasayapti.
Panel parallelogramm shaklida va uning bitta burchagi <b>72</b>°.</p>

<p><b>Nima soʻralyapti:</b> panelning qolgan uchta burchagi.</p>

<p><b>Reja:</b> parallelogrammda qarama-qarshi burchaklar teng, qoʻshnilari
esa 180° ni beradi. Bitta burchakdan hammasi chiqadi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Qarama-qarshisi = 72°</span>
    <span class="pm-solve__why">Qarama-qarshi burchaklar teng</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Qoʻshnisi = 180 − 72 = 108°</span>
    <span class="pm-solve__why">Qoʻshni burchaklar 180° ni beradi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">72°, 108°, 72°, 108°</span>
    <span class="pm-solve__why">Toʻrtala burchak</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>72 + 108 + 72 + 108 = 360 ✓
  <br><b>Javob:</b> qolgan burchaklar 108°, 72° va 108°.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>72° — toʻgʻri burchakdan kichik, demak panel biroz qiyshiq
  boʻladi. Agar 90° chiqqanida panel toʻgʻri toʻrtburchak boʻlar edi.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Har bir romb — kvadrat</p>
  <p class="pe-fix__good">Har bir <b>kvadrat</b> — romb, teskarisi emas</p>
  <p class="pe-fix__why">Rombda faqat tomonlar teng. Burchaklari ham 90°
  boʻlsagina u kvadratga aylanadi. Daraxtni pastdan yuqoriga oʻqing.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Parallelogrammning bitta burchagi 65° → qoʻshnisi
    ham 65°</p>
  <p class="pe-fix__good">Qoʻshnisi 180 − 65 = 115°, teng boʻlgani
    <b>qarama-qarshisi</b></p>
  <p class="pe-fix__why">Teng boʻlgan burchaklar roʻparama-roʻpara turadi.
  Yonma-yon turganlari 180° ni beradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Trapetsiya — parallelogrammning bir turi</p>
  <p class="pe-fix__good">Trapetsiyada <b>faqat bitta</b> juft tomon
    parallel</p>
  <p class="pe-fix__why">Parallelogrammda ikkala juft ham parallel. Shuning
  uchun daraxtda ular yonma-yon turadi, biri ikkinchisining tagida
  emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Toʻrtburchakning burchaklari yigʻindisi 180°</p>
  <p class="pe-fix__good">360° — chunki u ikkita uchburchakdan iborat</p>
  <p class="pe-fix__why">180° — uchburchakniki. Diagonal chizib koʻring:
  ikkita uchburchak, demak ikki barobar.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Toʻrtburchakning uch burchagi 80°, 95° va 100°.
  Toʻrtinchisi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>85°.</b> 80 + 95 + 100 = 275, keyin 360 − 275 = 85.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Parallelogrammning bitta burchagi 48°. Qolgan
  uchtasi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>132°, 48°, 132°.</b> Qarama-qarshisi 48°, qoʻshnilari
    180 − 48 = 132°. Tekshirish: 48 + 132 + 48 + 132 = 360 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Rombning bitta burchagi 60°. Qolganlari-chi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>120°, 60°, 120°.</b> Romb — parallelogramm, demak unga ham oʻsha
    qoida ishlaydi: qarama-qarshisi 60°, qoʻshnisi 180 − 60 = 120°.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Qaysi gap toʻgʻri: «har bir kvadrat toʻgʻri
  toʻrtburchak» yoki «har bir toʻgʻri toʻrtburchak kvadrat»?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Birinchisi.</b> Kvadratning burchaklari 90°, demak u toʻgʻri
    toʻrtburchak shartini bajaradi. Lekin tomonlari 8 va 3 boʻlgan toʻgʻri
    toʻrtburchak kvadrat emas — tomonlari teng emas.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Teng yonli trapetsiyaning katta asosidagi
  burchaklari 75° dan. Kichik asosdagi burchaklar qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>105° dan.</b> Yon tomon ikki parallel asosni kesadi, demak yuqori
    va quyi burchaklar bir tomonli ichki burchaklar: 180 − 75 = 105.
    Tekshirish: 75 + 75 + 105 + 105 = 360 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Dilnoza gilamdagi naqshni oʻlchadi: shaklning
  toʻrtala tomoni ham 12 sm, burchaklaridan biri esa 90°. Bu qanday
  shakl?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Kvadrat.</b> Toʻrtala tomoni teng — demak romb. Bitta burchagi
    90° boʻlsa, parallelogrammda qolgan uchtasi ham 90° boʻladi — demak
    toʻgʻri toʻrtburchak ham. Ikkalasi birga — kvadrat.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Toʻrtburchak</b><span>toʻrt tomonli shakl, burchaklari 360°; ingl.
    quadrilateral</span></li>
  <li><b>Parallelogramm</b><span>qarama-qarshi tomonlari parallel
    toʻrtburchak; ingl. parallelogram</span></li>
  <li><b>Toʻgʻri toʻrtburchak</b><span>burchaklari 90° boʻlgan
    parallelogramm; ingl. rectangle</span></li>
  <li><b>Romb</b><span>tomonlari teng boʻlgan parallelogramm; ingl.
    rhombus</span></li>
  <li><b>Kvadrat</b><span>ham romb, ham toʻgʻri toʻrtburchak; ingl.
    square</span></li>
  <li><b>Trapetsiya</b><span>faqat bitta juft tomoni parallel toʻrtburchak;
    ingl. trapezium</span></li>
  <li><b>Asos</b><span>trapetsiyaning parallel tomonlaridan biri; ingl.
    base</span></li>
  <li><b>Diagonal</b><span>qarama-qarshi uchlarni tutashtiruvchi kesma;
    ingl. diagonal</span></li>
  <li><b>Qarama-qarshi burchaklar</b><span>roʻparama-roʻpara turgan, teng
    burchaklar; ingl. opposite angles</span></li>
  <li><b>Qoʻshni burchaklar</b><span>bitta tomonni baham koʻrgan, 180°
    beruvchi burchaklar; ingl. adjacent angles</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Har qanday toʻrtburchakda burchaklar yigʻindisi 360° — chunki u
      ikkita uchburchak.</li>
    <li>Parallelogramm: qarama-qarshi tomonlar va burchaklar teng, qoʻshni
      burchaklar 180°.</li>
    <li>Toʻgʻri toʻrtburchak = burchaklari 90° boʻlgan parallelogramm.</li>
    <li>Romb = tomonlari teng boʻlgan parallelogramm.</li>
    <li>Kvadrat = ikkalasi birga.</li>
    <li>Trapetsiyada faqat bitta juft tomon parallel — u parallelogramm
      emas.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-67 — perimetr
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-67: Perimetr — chegaraning uzunligi",
        "category": "math",
        "order": 67,
        "summary": (
            "Perimetr — shaklni oʻrab turgan chiziqning uzunligi. Toʻgʻri "
            "toʻrtburchak va kvadrat formulalari, murakkab shaklning "
            "yetishmayotgan tomonlari va teskari masala."
        ),
        "stories": ["Bogʻga panjara"],
        "content": """
<h2>PM-67: Perimetr — chegaraning uzunligi</h2>

<p>Bogʻni panjara bilan oʻrab olmoqchisiz. Doʻkonchi bitta savol beradi:
«Necha metr?» Bogʻning kattaligi emas — aynan uni <b>oʻrab</b> turgan
chiziqning uzunligi kerak.</p>

<p>Shu uzunlikning nomi bor: <b>perimetr</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>istalgan koʻpburchakning perimetrini topasiz;</li>
    <li>toʻgʻri toʻrtburchak va kvadrat uchun qisqa formulani
      ishlatasiz;</li>
    <li>murakkab shaklning yetishmayotgan tomonini oʻzingiz
      tiklaysiz;</li>
    <li>teskari masalani yechasiz: perimetr maʼlum, tomon nomaʼlum.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Toʻgʻri toʻrtburchak</span>
  <span class="pe-chip pe-chip--s">P</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">2 × (a + b)</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--aux">kvadrat: P = 4 × a</span>
</div>

<h3>1. Perimetr nima</h3>

<p><b>Perimetr</b> — shaklning hamma tomonlari uzunligining yigʻindisi.
Uni topish uchun chegara boʻylab bir marta aylanib chiqing va bosib
oʻtgan yoʻlingizni sanang.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 190" role="img"
       aria-label="Toʻgʻri toʻrtburchak bogʻ: tomonlari 15 va 9 metr">
    <rect class="pm-fill" x="55" y="30" width="210" height="126"/>
    <rect class="pm-ln pm-ln--hl" x="55" y="30" width="210" height="126" fill="none"/>
    <text class="pm-lbl" x="144" y="22">15 m</text>
    <text class="pm-lbl" x="144" y="176">15 m</text>
    <text class="pm-lbl" x="15" y="98">9 m</text>
    <text class="pm-lbl" x="275" y="98">9 m</text>
  </svg>
  <figcaption>Perimetr — shaklni <b>oʻrab</b> turgan chiziqning uzunligi.
  Bu yerda ikkita 15 va ikkita 9 metr.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">15 + 9 + 15 + 9</span>
    <span class="pm-solve__why">Chegara boʻylab yurib, hamma tomonni
    qoʻshdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 48 m</span>
    <span class="pm-solve__why">Bogʻning perimetri</span>
  </div>
</div>

<p>Toʻgʻri toʻrtburchakda qarama-qarshi tomonlar teng (PM-66), demak har bir
uzunlik <b>ikki marta</b> uchraydi. Shundan qisqa yoʻl chiqadi:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">P = 2 × 15 + 2 × 9 = 30 + 18 = 48</span>
    <span class="pm-solve__why">Har birini ikkilantirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">P = 2 × (15 + 9) = 2 × 24 = 48</span>
    <span class="pm-solve__why">Yoki avval qoʻshib, keyin ikkilantirdik —
    javob bir xil</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Ikkala yoʻl ham toʻgʻri</p>
  <p>2 × 15 + 2 × 9 va 2 × (15 + 9) — bu bitta narsa: qavsdan chiqarish
  (PM-34). Ogʻzaki hisoblashda ikkinchisi qulayroq, chunki avval kichik
  qoʻshishni bajarasiz.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">Kvadrat, tomoni 7 sm → P = 4 × 7 = 28 sm</p>
  <p class="pe-ex__uz">Kvadratning toʻrtala tomoni teng, shuning uchun
  toʻrtga koʻpaytiriladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">Uchburchak, tomonlari 6, 8 va 10 → P = 6 + 8 + 10 = 24</p>
  <p class="pe-ex__uz">Formula shart emas: hamma tomonni qoʻshsangiz
  boʻldi.</p>
  <p class="pe-ex__why">Perimetr <b>har qanday</b> koʻpburchakda shunday
  topiladi. Formulalar — faqat qisqartma.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Ikkilantirishni unutish</p>
  <p>Eng koʻp uchraydigan xato — 15 + 9 = 24 deb toʻxtab qolish. Bu faqat
  <b>ikkita</b> tomon. Bogʻning atrofi esa toʻrtta tomondan iborat: javob
  48. Chizmaga qarab, har bir tomonni barmoq bilan sanab chiqing.</p>
</div>

<h3>2. Murakkab shakl: yetishmayotgan tomonni tiklash</h3>

<p>Hamma maydon ham toʻgʻri toʻrtburchak emas. Mana L shaklidagi bir
maydon.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 205" role="img"
       aria-label="L shaklli maydon: tomonlari 12, 3, 7, 5, 5 va 8 metr">
    <polygon class="pm-fill" points="50,175 266,175 266,121 140,121 140,31 50,31"/>
    <polyline class="pm-ln pm-ln--hl" points="50,175 266,175 266,121 140,121 140,31 50,31 50,175" fill="none"/>
    <text class="pm-lbl" x="142" y="195">12 m</text>
    <text class="pm-lbl" x="274" y="153">3 m</text>
    <text class="pm-lbl" x="191" y="113">7 m</text>
    <text class="pm-lbl" x="148" y="81">5 m</text>
    <text class="pm-lbl" x="83" y="23">5 m</text>
    <text class="pm-lbl" x="16" y="108">8 m</text>
  </svg>
  <figcaption>Chegara boʻylab yuring va hamma tomonni qoʻshing. Gorizontal
  tomonlar: 12 = 7 + 5, vertikal tomonlar: 8 = 3 + 5.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">12 + 3 + 7 + 5 + 5 + 8</span>
    <span class="pm-solve__why">Oltita tomon, chegara boʻylab tartib
    bilan</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 40 m</span>
    <span class="pm-solve__why">L shaklli maydonning perimetri</span>
  </div>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Yetishmayotgan tomonni topish qoidasi</p>
  <p>Bunday «zinapoyali» shaklda <b>gorizontal tomonlarning yigʻindisi
  pastdagi eng uzun tomonga teng</b>, vertikallariniki esa yondagi eng
  uzuniga:
  <br>7 + 5 = 12 ✓ &nbsp;&nbsp; 3 + 5 = 8 ✓
  <br>Shuning uchun bitta tomon berilmagan boʻlsa ham, uni ayirish bilan
  tiklaysiz.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">P = 2 × (12 + 8) = 2 × 20 = 40</p>
  <p class="pe-ex__uz">Xuddi shu javob — uni oʻrab turgan toʻgʻri
  toʻrtburchakning perimetri.</p>
  <p class="pe-ex__why">Oʻyiq shaklning ichiga «botib» kirdi, lekin
  chegaraning umumiy uzunligini oʻzgartirmadi: har bir ichkariga burilish
  keyin xuddi shuncha tashqariga burilish bilan qoplanadi. Bu esa javobni
  tekshirishning tez yoʻli.</p>
</div>

<h3>3. Teskari masala: perimetr maʼlum, tomon nomaʼlum</h3>

<p>Toʻgʻri toʻrtburchakning perimetri <b>36</b> sm, uzunligi esa
<b>12</b> sm. Eni qancha?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2 × (12 + b) = 36</span>
    <span class="pm-solve__why">Formulaga qoʻydik (PM-36)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">12 + b = 18</span>
    <span class="pm-solve__why">Ikki tomonni 2 ga boʻldik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">b = 18 − 12 = 6 sm</span>
    <span class="pm-solve__why">12 ni ayirdik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>2 × (12 + 6) = 2 × 18 = 36 ✓ — berilgan perimetr chiqdi.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Birliklar bir xil boʻlsin</p>
  <p>Tomonlari 80 <b>sm</b> va 1,2 <b>m</b> boʻlgan shaklning perimetrini
  qoʻshishdan oldin bir birlikka keltiring: 80 sm = 0,8 m, keyin
  2 × (0,8 + 1,2) = 4 m. Aralash qoʻshilsa, javob mutlaqo maʼnosiz
  chiqadi.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Bogʻga panjara.</b> Sherbekning oilasi toʻgʻri toʻrtburchak shaklidagi
bogʻni panjara bilan oʻramoqchi. Bogʻning uzunligi <b>15</b> metr, eni
<b>9</b> metr. Bir joyda <b>3</b> metrlik darvoza qoldiriladi — u yerga
panjara kerak emas. Panjaraning bir metri <b>25 000</b> soʻm turadi.</p>

<p><b>Nima soʻralyapti:</b> panjara uchun jami qancha pul kerak.</p>

<p><b>Reja:</b> avval butun chegarani (perimetrni) topamiz, undan darvozani
ayiramiz, qolganini narxga koʻpaytiramiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">P = 2 × (15 + 9) = 48 m</span>
    <span class="pm-solve__why">Bogʻning butun chegarasi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">48 − 3 = 45 m</span>
    <span class="pm-solve__why">Darvoza oʻrniga panjara qoʻyilmaydi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">45 × 25 000 = 1 125 000 soʻm</span>
    <span class="pm-solve__why">Panjaraning umumiy narxi</span>
  </div>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>45 ≈ 50 va 50 × 25 000 = 1 250 000. Javob shundan bir oz kam
  boʻlishi kerak — 1 125 000 mos keladi.</span>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>45 × 25 000 = 45 × 25 × 1000 = 1125 × 1000 = 1 125 000 ✓
  <br><b>Javob:</b> 45 metr panjara, 1 125 000 soʻm.</p>
</div>

<p>Eʼtibor bering: bogʻning <b>ichi</b> haqida hech narsa soʻralmadi.
Panjara faqat chegara boʻylab yuradi. Ichini oʻlchash — butunlay boshqa
savol, va u keyingi darsda.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Tomonlari 15 va 9 → P = 15 + 9 = 24 m</p>
  <p class="pe-fix__good">P = 2 × (15 + 9) = 48 m</p>
  <p class="pe-fix__why">Toʻrtta tomon bor, ikkita emas. Qarama-qarshi
  tomonlar teng boʻlgani uchun har bir son ikki marta qoʻshiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Kvadrat, tomoni 7 → P = 7 × 7 = 49</p>
  <p class="pe-fix__good">P = 4 × 7 = 28</p>
  <p class="pe-fix__why">Tomonni oʻziga koʻpaytirish perimetr bermaydi —
  perimetr uchun toʻrtta tomon qoʻshiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">P = 36, a = 12 → b = 36 − 12 = 24</p>
  <p class="pe-fix__good">2 × (12 + b) = 36 → b = 6</p>
  <p class="pe-fix__why">36 — butun chegara, bitta tomonlar juftligi emas.
  Avval 2 ga boʻling, keyin ayiring.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Tomonlari 80 sm va 1,2 m → P = 2 × (80 + 1,2)</p>
  <p class="pe-fix__good">80 sm = 0,8 m → P = 2 × (0,8 + 1,2) = 4 m</p>
  <p class="pe-fix__why">Har xil birlikdagi sonlarni qoʻshib boʻlmaydi.
  Birinchi qadam — hammasini bir birlikka keltirish.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Toʻgʻri toʻrtburchakning tomonlari 14 sm va
  6 sm. Perimetri qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>40 sm.</b> P = 2 × (14 + 6) = 2 × 20 = 40.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Kvadratning tomoni 9 m. Perimetri qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>36 m.</b> P = 4 × 9 = 36.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Kvadratning perimetri 52 sm. Tomoni qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>13 sm.</b> Toʻrtala tomon teng, demak 52 ÷ 4 = 13.
    Tekshirish: 4 × 13 = 52 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Toʻgʻri toʻrtburchakning perimetri 30 m, eni
  4 m. Uzunligi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>11 m.</b> 2 × (a + 4) = 30 → a + 4 = 15 → a = 11.
    Tekshirish: 2 × (11 + 4) = 30 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. L shaklidagi maydonning eng uzun gorizontal
  tomoni 9 m, eng uzun vertikal tomoni esa 7 m. Uning perimetri
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>32 m.</b> Qolgan gorizontal tomonlar birgalikda ham 9 m, qolgan
    vertikallar ham 7 m beradi (yuqoridagi qoida). Demak perimetr uni
    oʻrab turgan 9 × 7 toʻrtburchaknikiga teng:
    P = 2 × (9 + 7) = 32 m. Oʻyiqning qayerdaligi javobga taʼsir
    qilmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Afsona kvadrat shaklidagi rasmga ramka
  qoʻymoqchi. Rasmning tomoni 30 sm, ramkaning bir metri 18 000 soʻm.
  Ramka necha soʻm turadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>21 600 soʻm.</b> Perimetr: 4 × 30 = 120 sm. Birlikni keltiramiz:
    120 sm = 1,2 m. Narxi: 1,2 × 18 000 = 21 600 soʻm. Birlikni
    almashtirmasangiz, javob yuz barobar katta chiqadi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Perimetr</b><span>shaklni oʻrab turgan chiziqning uzunligi; ingl.
    perimeter</span></li>
  <li><b>Chegara</b><span>shaklning tashqi konturi; ingl. boundary</span></li>
  <li><b>Tomon</b><span>koʻpburchakni hosil qiluvchi kesma; ingl.
    side</span></li>
  <li><b>Uzunlik</b><span>toʻgʻri toʻrtburchakning katta oʻlchovi; ingl.
    length</span></li>
  <li><b>En</b><span>toʻgʻri toʻrtburchakning kichik oʻlchovi; ingl.
    width</span></li>
  <li><b>Koʻpburchak</b><span>kesmalardan tuzilgan yopiq shakl; ingl.
    polygon</span></li>
  <li><b>Murakkab shakl</b><span>bir nechta toʻrtburchakdan tuzilgan
    shakl; ingl. compound shape</span></li>
  <li><b>Teskari masala</b><span>natija maʼlum, boshlangʻich son
    izlanadi; ingl. inverse problem</span></li>
  <li><b>Birliklarni keltirish</b><span>sm va m ni bir xil qilish; ingl.
    unit conversion</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Perimetr — hamma tomonlarning yigʻindisi, chegara boʻylab bir
      aylanish.</li>
    <li>Toʻgʻri toʻrtburchak: P = 2 × (a + b). Kvadrat: P = 4 × a.</li>
    <li>Murakkab shaklda gorizontal tomonlar yigʻindisi eng uzun
      gorizontalga, vertikallariniki eng uzun vertikalga teng.</li>
    <li>Teskari masalada avval 2 ga boʻling, keyin ayiring.</li>
    <li>Qoʻshishdan oldin birliklarni bir xil qiling.</li>
    <li>Perimetr — faqat chegara. Ichi haqidagi savol keyingi darsda.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-68 — yuza 1: toʻgʻri toʻrtburchak va uchburchak
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-68: Yuza 1: toʻgʻri toʻrtburchak va uchburchak",
        "category": "math",
        "order": 68,
        "summary": (
            "Yuza — shakl ichiga sigʻadigan birlik kvadratlar soni. "
            "Toʻgʻri toʻrtburchakda a × b, uchburchakda esa aynan yarmi — "
            "va nega yarmi ekani chizmada koʻrinadi."
        ),
        "stories": ["Sinf polini qoplash"],
        "content": """
<h2>PM-68: Yuza 1: toʻgʻri toʻrtburchak va uchburchak</h2>

<p>Oʻtgan darsda bogʻni panjara bilan oʻradik. Endi boshqa savol: oʻsha
bogʻning <b>ichiga</b> qancha oʻt urugʻi kerak? Yoki sinfning poliga necha
dona plitka ketadi?</p>

<p>Bu safar chegara emas, <b>ichi</b> oʻlchanadi. Uning nomi —
<b>yuza</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>yuza nima ekanini birlik kvadratlar orqali tushunasiz;</li>
    <li>toʻgʻri toʻrtburchak va kvadratning yuzasini topasiz;</li>
    <li>uchburchak yuzasi nega ikkiga boʻlinishini isbotlaysiz;</li>
    <li>murakkab shaklni boʻlaklarga ajratib hisoblaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Yuza</span>
  <span class="pe-chip pe-chip--v">S = a × b</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">uchburchak: S = (a × h) ÷ 2</span>
</div>

<h3>1. Yuza — bu sanoq</h3>

<p>Tomoni <b>1</b> sm boʻlgan kvadratni <b>birlik kvadrat</b> deymiz.
Uning yuzasi <b>1 sm<sup>2</sup></b> («bir kvadrat santimetr»). Shaklning
yuzasi — uning ichiga sigʻadigan shunday kvadratlar soni.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 200" role="img"
       aria-label="Toʻgʻri toʻrtburchak birlik kvadratlarga boʻlingan: 6 ta ustun, 4 ta qator">
    <rect class="pm-fill" x="60" y="45" width="180" height="120"/>
    <line class="pm-ln pm-ln--dash" x1="60" y1="45" x2="60" y2="165"/>
    <line class="pm-ln pm-ln--dash" x1="90" y1="45" x2="90" y2="165"/>
    <line class="pm-ln pm-ln--dash" x1="120" y1="45" x2="120" y2="165"/>
    <line class="pm-ln pm-ln--dash" x1="150" y1="45" x2="150" y2="165"/>
    <line class="pm-ln pm-ln--dash" x1="180" y1="45" x2="180" y2="165"/>
    <line class="pm-ln pm-ln--dash" x1="210" y1="45" x2="210" y2="165"/>
    <line class="pm-ln pm-ln--dash" x1="240" y1="45" x2="240" y2="165"/>
    <line class="pm-ln pm-ln--dash" x1="60" y1="45" x2="240" y2="45"/>
    <line class="pm-ln pm-ln--dash" x1="60" y1="75" x2="240" y2="75"/>
    <line class="pm-ln pm-ln--dash" x1="60" y1="105" x2="240" y2="105"/>
    <line class="pm-ln pm-ln--dash" x1="60" y1="135" x2="240" y2="135"/>
    <line class="pm-ln pm-ln--dash" x1="60" y1="165" x2="240" y2="165"/>
    <rect class="pm-ln pm-ln--hl" x="60" y="45" width="180" height="120" fill="none"/>
    <rect class="pm-fill--hl" x="60" y="135" width="30" height="30"/>
    <text class="pm-lbl" x="116" y="35">6 ta ustun</text>
    <text class="pm-lbl" x="14" y="110">4 ta</text>
    <text class="pm-lbl" x="14" y="126">qator</text>
    <text class="pm-lbl pm-lbl--hl" x="106" y="189">6 × 4 = 24 ta katak</text>
  </svg>
  <figcaption>Yuza — shaklning <b>ichiga</b> sigʻadigan birlik kvadratlar
  soni. Sanamasdan ham boʻladi: bir qatorda 6 ta, qator esa 4 ta.</figcaption>
</figure>

<p>Kataklarni bittalab sanash shart emas. Bir qatorda <b>6</b> ta katak
bor, qatorlar soni esa <b>4</b> ta. Demak koʻpaytirish yetadi (PM-3).</p>

<div class="pm-solve">
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">S = 6 × 4 = 24 sm<sup>2</sup></span>
    <span class="pm-solve__why">Bir qatordagi kataklar × qatorlar soni</span>
  </div>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Toʻgʻri toʻrtburchak va kvadratning yuzasi</p>
  <p><b>S = a × b</b> — uzunligini eniga koʻpaytiring.
  <br>Kvadratda tomonlar teng, shuning uchun <b>S = a × a = a<sup>2</sup></b>
  — bu esa PM-12 dagi darajaning oʻzi. «Kvadrat» soʻzi ham shundan.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">Xona 5 m × 4 m → S = 5 × 4 = 20 m<sup>2</sup></p>
  <p class="pe-ex__uz">Xonaning poli yigirma kvadrat metr.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">Kvadrat, tomoni 8 sm → S = 8<sup>2</sup> = 64 sm<sup>2</sup></p>
  <p class="pe-ex__uz">Oltmish toʻrtta birlik kvadrat sigʻadi.</p>
  <p class="pe-ex__why">PM-13 dagi teskari savol shu yerdan chiqqan edi:
  yuzasi 81 boʻlsa, tomoni √81 = 9.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">1 m<sup>2</sup> — bu 100 sm<sup>2</sup> emas</p>
  <p>1 m = 100 sm, lekin yuza <b>ikki</b> tomonga oʻsadi:
  <br>1 m<sup>2</sup> = 100 × 100 = <b>10 000</b> sm<sup>2</sup>.
  <br>Uzunlik birligini almashtirganda 100 ga, yuza birligini
  almashtirganda 10 000 ga koʻpaytiriladi. Bu — mavzudagi eng qimmat
  xato.</p>
</div>

<h3>2. Uchburchak: nega aynan yarmi?</h3>

<p>Uchburchakning yuzasini topish uchun uni <b>oʻrab turgan</b> toʻgʻri
toʻrtburchakka joylashtiramiz.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 200" role="img"
       aria-label="Uchburchak uni oʻrab turgan toʻgʻri toʻrtburchakning aynan yarmi">
    <rect class="pm-ln pm-ln--dash" x="50" y="60" width="200" height="110" fill="none"/>
    <polygon class="pm-fill--hl" points="50,170 250,170 140,60"/>
    <polyline class="pm-ln" points="50,170 250,170 140,60 50,170" fill="none"/>
    <line class="pm-ln pm-ln--dash" x1="140" y1="60" x2="140" y2="170"/>
    <polyline class="pm-ln" points="152,170 152,158 140,158" fill="none"/>
    <text class="pm-lbl" x="120" y="192">asos a</text>
    <text class="pm-lbl" x="148" y="120">balandlik h</text>
    <text class="pm-lbl pm-lbl--hl" x="70" y="156">yarmi</text>
    <text class="pm-lbl" x="70" y="80">yarmi</text>
    <text class="pm-lbl" x="184" y="80">yarmi</text>
    <text class="pm-lbl pm-lbl--hl" x="184" y="156">yarmi</text>
  </svg>
  <figcaption>Balandlik chizmani ikkita toʻgʻri toʻrtburchakka boʻladi va
  uchburchak har birining aynan yarmini egallaydi. Demak butun uchburchak —
  butun toʻrtburchakning yarmi.</figcaption>
</figure>

<p>Uchburchakning uchidan asosga <b>balandlik</b> tushiramiz (PM-65 da
tomning balandligini shunday topgan edik). U chizmani ikkiga boʻladi.</p>

<div class="pe-steps">
  <ol>
    <li>Chap tomonda kichik toʻgʻri toʻrtburchak hosil boʻldi. Uning
      <b>diagonali</b> — uchburchakning chap tomoni. Diagonal esa har
      qanday toʻgʻri toʻrtburchakni ikkita teng boʻlakka boʻladi.</li>
    <li>Demak uchburchakning chap qismi — oʻsha kichik toʻrtburchakning
      <b>yarmi</b>.</li>
    <li>Oʻng tomonda ham xuddi shunday: yarmi.</li>
    <li>Yarim + yarim = butun chizmaning yarmi.</li>
  </ol>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Uchburchakning yuzasi</p>
  <p><b>S = (a × h) ÷ 2</b>, bunda a — asos, h — oʻsha asosga tushirilgan
  balandlik. Avval oʻrab turgan toʻrtburchakning yuzasini toping, keyin
  ikkiga boʻling.</p>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">a = 10 sm, h = 6 sm</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">10 × 6 = 60</span>
    <span class="pm-solve__why">Oʻrab turgan toʻrtburchakning yuzasi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">S = 60 ÷ 2 = 30 sm<sup>2</sup></span>
    <span class="pm-solve__why">Uchburchak uning yarmi</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Balandlik — yon tomon emas</p>
  <p>Balandlik asosga <b>perpendikulyar</b> tushadi. Qiya turgan yon tomon
  esa undan uzunroq (u gipotenuza, PM-64). Masalada ikkalasi ham berilgan
  boʻlsa, formulaga <b>balandlikni</b> qoʻying — chizmadagi 90° belgisini
  qidiring.</p>
</div>

<h3>3. Murakkab shakl: boʻlaklarga ajratish</h3>

<p>PM-67 da perimetrini topgan L shaklli maydonni eslaysizmi? Endi uning
ichini oʻlchaymiz.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 205" role="img"
       aria-label="L shaklli maydon ikkita toʻgʻri toʻrtburchakka boʻlingan: 12 ga 3 va 5 ga 5">
    <rect class="pm-fill--hl" x="50" y="121" width="216" height="54"/>
    <rect class="pm-fill" x="50" y="31" width="90" height="90"/>
    <line class="pm-ln pm-ln--dash" x1="50" y1="121" x2="140" y2="121"/>
    <polyline class="pm-ln" points="50,175 266,175 266,121 140,121 140,31 50,31 50,175" fill="none"/>
    <text class="pm-lbl pm-lbl--hl" x="118" y="153">12 × 3 = 36</text>
    <text class="pm-lbl" x="61" y="81">5 × 5 = 25</text>
    <text class="pm-lbl" x="142" y="195">12 m</text>
    <text class="pm-lbl" x="16" y="108">8 m</text>
  </svg>
  <figcaption>Murakkab shaklni ikkita toʻgʻri toʻrtburchakka boʻlamiz va
  yuzalarini qoʻshamiz: 36 + 25 = 61 m².</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Pastki qism: 12 × 3 = 36 m<sup>2</sup></span>
    <span class="pm-solve__why">Butun eni boʻylab choʻzilgan boʻlak</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Yuqori qism: 5 × 5 = 25 m<sup>2</sup></span>
    <span class="pm-solve__why">Chapdagi ustun</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">S = 36 + 25 = 61 m<sup>2</sup></span>
    <span class="pm-solve__why">Boʻlaklarning yigʻindisi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Boshqa yoʻl bilan tekshiramiz</p>
  <p>Oʻrab turgan toʻrtburchak: 12 × 8 = 96 m<sup>2</sup>. Yetishmayotgan
  oʻyiq: 7 × 5 = 35 m<sup>2</sup>. Ayiramiz: 96 − 35 = 61 ✓ — bir xil
  javob.</p>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Perimetr va yuza — ikki boshqa savol</p>
  <p>Xuddi shu L shaklli maydonning perimetri <b>40 m</b> (PM-67), yuzasi
  esa <b>61 m<sup>2</sup></b>. Bittasi chegara, ikkinchisi ichi. Birligi
  ham har xil: perimetr <b>m</b> da, yuza <b>m<sup>2</sup></b> da
  oʻlchanadi. Javobingizning birligiga qarab, qaysi savolga javob
  berganingizni darrov bilasiz.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Sinf polini qoplash.</b> Sinf xonasi toʻgʻri toʻrtburchak: uzunligi
<b>8</b> metr, eni <b>6</b> metr. Polga kvadrat plitka yotqiziladi,
plitkaning tomoni <b>40</b> santimetr. Usta sindirib qoʻyish ehtimoli
uchun hisobdan <b>5</b> foiz koʻp olishni maslahat berdi.</p>

<p><b>Nima soʻralyapti:</b> jami nechta plitka sotib olish kerak.</p>

<p><b>Reja:</b> xonaning yuzasini topamiz, bitta plitkaning yuzasini
topamiz (birliklarni tenglashtirib), boʻlamiz, keyin 5 foiz qoʻshamiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">8 × 6 = 48 m<sup>2</sup></span>
    <span class="pm-solve__why">Xonaning yuzasi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">40 sm = 0,4 m</span>
    <span class="pm-solve__why">Birliklarni tenglashtirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">0,4 × 0,4 = 0,16 m<sup>2</sup></span>
    <span class="pm-solve__why">Bitta plitkaning yuzasi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">48 ÷ 0,16 = 300 ta</span>
    <span class="pm-solve__why">Nazariy jihatdan yetarli plitka</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">300 × 1,05 = 315 ta</span>
    <span class="pm-solve__why">Ustaning 5 foizlik zaxirasi bilan
    (PM-23)</span>
  </div>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Bitta plitka kvadrat metrning oltidan biriga yaqin, demak har bir
  kvadrat metrga taxminan 6 tadan ketadi: 48 × 6 ≈ 288. Javob 300
  atrofida — mos keladi.</span>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>300 × 0,16 = 48 m<sup>2</sup> ✓ — aynan xonaning yuzasi.
  <br>5 foiz: 300 ÷ 100 × 5 = 15, va 300 + 15 = 315 ✓
  <br><b>Javob:</b> 315 ta plitka.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Xona 5 m × 4 m → yuzasi 2 × (5 + 4) = 18</p>
  <p class="pe-fix__good">S = 5 × 4 = 20 m<sup>2</sup></p>
  <p class="pe-fix__why">Bu perimetr formulasi (PM-67). Yuza uchun
  tomonlar <b>koʻpaytiriladi</b>, qoʻshilmaydi. Birlikka qarang: yuza
  m<sup>2</sup> da boʻladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">1 m<sup>2</sup> = 100 sm<sup>2</sup></p>
  <p class="pe-fix__good">1 m<sup>2</sup> = 10 000 sm<sup>2</sup></p>
  <p class="pe-fix__why">Kvadratning ikkala tomoni ham 100 marta oʻsadi:
  100 × 100. Chizib koʻring — 1 m<sup>2</sup> ichiga yuzta emas, oʻn
  mingta kichik kvadrat sigʻadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Uchburchak: asosi 10, yon tomoni 8 → S = 10 × 8 ÷ 2 = 40</p>
  <p class="pe-fix__good">Balandlikni qoʻying, yon tomonni emas</p>
  <p class="pe-fix__why">Yon tomon qiya turadi va balandlikdan uzun.
  Formulada faqat asosga <b>perpendikulyar</b> boʻlgan balandlik
  ishlaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Uchburchak: 12 × 5 = 60 sm<sup>2</sup></p>
  <p class="pe-fix__good">(12 × 5) ÷ 2 = 30 sm<sup>2</sup></p>
  <p class="pe-fix__why">Ikkiga boʻlish qadami tushib qolgan. 60 —
  uchburchakni oʻrab turgan toʻrtburchakning yuzasi, uchburchakniki
  emas.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Toʻgʻri toʻrtburchakning tomonlari 9 sm va
  7 sm. Yuzasi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>63 sm<sup>2</sup>.</b> S = 9 × 7 = 63. Diqqat: perimetri esa
    2 × (9 + 7) = 32 sm — butunlay boshqa son va boshqa birlik.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Kvadratning tomoni 12 m. Yuzasi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>144 m<sup>2</sup>.</b> S = 12<sup>2</sup> = 144.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Uchburchakning asosi 14 sm, balandligi 6 sm.
  Yuzasi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>42 sm<sup>2</sup>.</b> (14 × 6) ÷ 2 = 84 ÷ 2 = 42.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Toʻgʻri toʻrtburchakning yuzasi 72 sm<sup>2</sup>,
  eni 8 sm. Uzunligi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>9 sm.</b> S = a × b, demak a = 72 ÷ 8 = 9. Tekshirish:
    9 × 8 = 72 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Kvadratning yuzasi 49 m<sup>2</sup>. Uning
  perimetri qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>28 m.</b> Ikki qadam kerak: avval tomonini toping —
    √49 = 7 m (PM-13), keyin perimetrni — 4 × 7 = 28 m.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Bekzodning hovlisi 20 m × 15 m. Uning bir
  burchagida 6 m × 5 m gulzor bor, qolgan joyga oʻt ekiladi. Oʻt ekiladigan
  yuza qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>270 m<sup>2</sup>.</b> Butun hovli: 20 × 15 = 300 m<sup>2</sup>.
    Gulzor: 6 × 5 = 30 m<sup>2</sup>. Ayiramiz: 300 − 30 = 270
    m<sup>2</sup>. Murakkab shaklda «qoʻshish» ham, «ayirish» ham
    ishlaydi — qaysi biri qulay boʻlsa.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Yuza</b><span>shakl ichiga sigʻadigan birlik kvadratlar soni;
    ingl. area</span></li>
  <li><b>Birlik kvadrat</b><span>tomoni 1 boʻlgan kvadrat; ingl. unit
    square</span></li>
  <li><b>Kvadrat santimetr</b><span>sm<sup>2</sup> — yuza birligi; ingl.
    square centimetre</span></li>
  <li><b>Kvadrat metr</b><span>m<sup>2</sup>, 10 000 sm<sup>2</sup> ga
    teng; ingl. square metre</span></li>
  <li><b>Asos</b><span>uchburchakning balandlik tushirilgan tomoni; ingl.
    base</span></li>
  <li><b>Balandlik</b><span>asosga perpendikulyar kesma; ingl.
    height</span></li>
  <li><b>Oʻrab turgan toʻrtburchak</b><span>shaklni ichiga olgan eng
    kichik toʻgʻri toʻrtburchak; ingl. bounding rectangle</span></li>
  <li><b>Boʻlaklarga ajratish</b><span>murakkab shaklni oddiy shakllarga
    boʻlish; ingl. decomposition</span></li>
  <li><b>Perimetr</b><span>chegara uzunligi — yuza bilan adashtirmang;
    ingl. perimeter</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Yuza — ichiga sigʻadigan birlik kvadratlar soni, m<sup>2</sup> yoki
      sm<sup>2</sup> da.</li>
    <li>Toʻgʻri toʻrtburchak: S = a × b. Kvadrat: S = a<sup>2</sup>.</li>
    <li>Uchburchak: S = (a × h) ÷ 2 — chunki u oʻrab turgan
      toʻrtburchakning yarmi.</li>
    <li>Balandlik asosga perpendikulyar; yon tomon emas.</li>
    <li>Murakkab shaklni boʻlaklarga ajrating yoki ortiqchasini
      ayiring.</li>
    <li>1 m<sup>2</sup> = 10 000 sm<sup>2</sup>, 100 emas.</li>
  </ul>
</div>
""",
    },
]
