# -*- coding: utf-8 -*-
"""Prime Math — darslar 60–62 (parallel chiziqlar, uchburchak, tengsizlik).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt
**Blok E: Geometriya** — har bir darsda SVG chizma SHART.

  mashqlar — practice/management/commands/_practice_pm_60_62.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_60_62.py

⚠️ Chizmalar QOʻLDA hisoblanmagan: burchak yoylari va uchburchak uchlari
   scratchpad/svgkit.py + gen_pm60.py / gen_pm61_62.py bilan generatsiya
   qilingan va verify_pm_60_62.py ularni qaytadan tekshiradi (yoy uchlari
   nurlar ustida yotishi, uchburchak turi haqiqatan oʻsha tur ekani).

⚠️ Kumulyativ chegaralar:
  • PM-60 — parallel + kesuvchi: mos (F), almashinuvchi ichki (Z), bir tomonli
    ichki (U); teskari xulosa (burchaklarga qarab parallellikni aniqlash);
  • PM-61 — uchburchak turlari (burchagi va tomoni boʻyicha) + burchaklar
    yigʻindisi 180° va uning ISBOTI (PM-60 dagi almashinuvchi burchaklar
    orqali — PM-59 da boshlangan isbot yoʻlining davomi);
  • PM-62 — uchburchak tengsizligi va tomon↔burchak bogʻliqligi.
  • ⛔ Teng yonli uchburchak xossalari (PM-63) YOʻQ; Pifagor (PM-64) YOʻQ;
    perimetr (PM-67) va yuza (PM-68) YOʻQ; aylana va π (PM-70) YOʻQ.
  • Faol ishlatiladi: burchak juftliklari (PM-59), burchak oʻlchash (PM-58),
    kesma (PM-57), nisbat (PM-27), tenglama (PM-36), sistema (PM-54),
    tengsizlik (PM-40).

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_60_62.py --author=prime
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
    # PM-60 — parallel chiziqlar va kesuvchi
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-60: Parallel chiziqlar va kesuvchi hosil qilgan burchaklar",
        "category": "math",
        "order": 60,
        "summary": (
            "Ikki parallel chiziqni kesuvchi kesib oʻtganda sakkizta burchak "
            "hosil boʻladi — lekin ularning bor-yoʻgʻi ikkita qiymati bor. "
            "Mos (F), almashinuvchi (Z) va bir tomonli (U) juftliklar."
        ),
        "stories": ["Poyezd derazasidan — relslar qayerda tutashadi?"],
        "content": """
<h2>PM-60: Parallel chiziqlar va kesuvchi hosil qilgan burchaklar</h2>

<p>Daftaringizni oching. Undagi chiziqlar hech qachon uchrashmaydi — ular
<b>parallel</b>. Endi ular ustidan bitta qiya chiziq torting. Sakkizta burchak
paydo boʻldi. Ularning nechtasini oʻlchash kerak?</p>

<p>Javob sizni ajablantiradi: <b>bittasini</b>. Qolgan yettitasi oʻz-oʻzidan
kelib chiqadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>parallel chiziq va kesuvchini taniysiz;</li>
    <li>mos, almashinuvchi va bir tomonli burchaklarni ajratasiz;</li>
    <li>bitta burchakdan sakkiztasini ham topasiz;</li>
    <li>burchaklarga qarab chiziqlar parallel ekanini aniqlaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uch juftlik</span>
  <span class="pe-chip pe-chip--o">mos (F) — teng</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">almashinuvchi (Z) — teng</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">bir tomonli (U) — 180°</span>
</div>

<h3>Parallel chiziq nima?</h3>

<p>Bitta tekislikdagi ikki toʻgʻri chiziq <b>hech qachon</b> kesishmasa, ular
parallel deyiladi. Yozuvi: <b>a ∥ b</b>. Ular orasidagi masofa hamma joyda
bir xil — temir yoʻl relslari, daftar chiziqlari, zinapoya panjaralari.</p>

<p><b>Kesuvchi</b> — ikkala parallel chiziqni ham kesib oʻtuvchi uchinchi
chiziq. U ikkita kesishish nuqtasi va sakkizta burchak hosil qiladi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 215" role="img"
       aria-label="Ikki parallel chiziq va kesuvchi hosil qilgan sakkiz burchak">
    <line class="pm-ln" x1="20" y1="60" x2="288" y2="60"/>
    <line class="pm-ln" x1="20" y1="170" x2="288" y2="170"/>
    <line class="pm-ln" x1="40" y1="205" x2="250" y2="10"/>
    <circle class="pm-pt" cx="196.2" cy="60" r="4"/>
    <circle class="pm-pt" cx="77.7" cy="170" r="4"/>
    <text class="pm-lbl" x="294" y="54">a</text>
    <text class="pm-lbl" x="294" y="164">b</text>
    <text class="pm-lbl pm-lbl--hl" x="180.1" y="32.9">1</text>
    <text class="pm-lbl pm-lbl--hl" x="224.2" y="52.1">2</text>
    <text class="pm-lbl pm-lbl--hl" x="160.9" y="76.9">3</text>
    <text class="pm-lbl pm-lbl--hl" x="205" y="96.1">4</text>
    <text class="pm-lbl pm-lbl--hl" x="61.7" y="142.9">5</text>
    <text class="pm-lbl pm-lbl--hl" x="105.7" y="162.1">6</text>
    <text class="pm-lbl pm-lbl--hl" x="42.4" y="186.9">7</text>
    <text class="pm-lbl pm-lbl--hl" x="86.5" y="206.1">8</text>
  </svg>
  <figcaption>Sakkizta burchak, ikkita kesishish nuqtasi. Yuqorida 1–4,
  pastda 5–8.</figcaption>
</figure>

<p>PM-59 dan bittasini allaqachon bilamiz: <b>har bir kesishish nuqtasida</b>
vertikal burchaklar teng, qoʻshnilari esa 180° beradi. Demak yuqoridagi
toʻrttadan bittasini bilsak, oʻsha toʻrttasini bilamiz.</p>

<p>Yangi savol boshqa: yuqoridagi burchaklar <b>pastdagilari bilan</b> qanday
bogʻlangan? Mana shu yerda parallellik ish boshlaydi.</p>

<h3>1-juftlik: mos burchaklar — «F» harfi</h3>

<p>Ikkala kesishishda ham <b>bir xil oʻrinda</b> turgan burchaklar mos
burchaklar deyiladi: ikkalasi ham chiziqning ostida va kesuvchining oʻng
tomonida. Chizmada ular <b>F</b> harfini hosil qiladi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 215" role="img" aria-label="Mos burchaklar — F shakli">
    <line class="pm-ln" x1="20" y1="60" x2="288" y2="60"/>
    <line class="pm-ln" x1="20" y1="170" x2="288" y2="170"/>
    <line class="pm-ln" x1="40" y1="205" x2="250" y2="10"/>
    <circle class="pm-pt" cx="196.2" cy="60" r="4"/>
    <circle class="pm-pt" cx="77.7" cy="170" r="4"/>
    <text class="pm-lbl" x="294" y="54">a</text>
    <text class="pm-lbl" x="294" y="164">b</text>
    <path class="pm-ln pm-ln--hl" d="M 177.1 77.7 A 26 26 0 0 0 222.2 60" fill="none"/>
    <path class="pm-ln pm-ln--hl" d="M 58.6 187.7 A 26 26 0 0 0 103.7 170" fill="none"/>
  </svg>
  <figcaption>∠4 va ∠8 — mos burchaklar. Parallel chiziqlarda ular
  <b>teng</b>.</figcaption>
</figure>

<h3>2-juftlik: almashinuvchi ichki burchaklar — «Z» harfi</h3>

<p>Ikki parallel chiziq <b>orasida</b> yotgan va kesuvchining <b>har xil</b>
tomonlarida turgan burchaklar. Chizmada ular <b>Z</b> harfini beradi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 215" role="img"
       aria-label="Almashinuvchi ichki burchaklar — Z shakli">
    <line class="pm-ln" x1="20" y1="60" x2="288" y2="60"/>
    <line class="pm-ln" x1="20" y1="170" x2="288" y2="170"/>
    <line class="pm-ln" x1="40" y1="205" x2="250" y2="10"/>
    <circle class="pm-pt" cx="196.2" cy="60" r="4"/>
    <circle class="pm-pt" cx="77.7" cy="170" r="4"/>
    <text class="pm-lbl" x="294" y="54">a</text>
    <text class="pm-lbl" x="294" y="164">b</text>
    <path class="pm-ln pm-ln--hl" d="M 170.2 60 A 26 26 0 0 0 177.1 77.7" fill="none"/>
    <path class="pm-ln pm-ln--hl" d="M 103.7 170 A 26 26 0 0 0 96.7 152.3" fill="none"/>
  </svg>
  <figcaption>∠3 va ∠6 — almashinuvchi ichki burchaklar. Ular ham
  <b>teng</b>.</figcaption>
</figure>

<h3>3-juftlik: bir tomonli ichki burchaklar — «U» harfi</h3>

<p>Ikki chiziq orasida, lekin kesuvchining <b>bitta</b> tomonida yotgan
burchaklar. Bular teng emas — ularning <b>yigʻindisi 180°</b>.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 215" role="img"
       aria-label="Bir tomonli ichki burchaklar — U shakli">
    <line class="pm-ln" x1="20" y1="60" x2="288" y2="60"/>
    <line class="pm-ln" x1="20" y1="170" x2="288" y2="170"/>
    <line class="pm-ln" x1="40" y1="205" x2="250" y2="10"/>
    <circle class="pm-pt" cx="196.2" cy="60" r="4"/>
    <circle class="pm-pt" cx="77.7" cy="170" r="4"/>
    <text class="pm-lbl" x="294" y="54">a</text>
    <text class="pm-lbl" x="294" y="164">b</text>
    <path class="pm-ln pm-ln--hl" d="M 177.1 77.7 A 26 26 0 0 0 222.2 60" fill="none"/>
    <path class="pm-ln pm-ln--hl" d="M 103.7 170 A 26 26 0 0 0 96.7 152.3" fill="none"/>
  </svg>
  <figcaption>∠4 va ∠6 — bir tomonli ichki burchaklar: 180° beradi.</figcaption>
</figure>

<div class="pe-call pe-tip">
  <p class="pe-call__t">F, Z, U — uchta harf, uchta qoida</p>
  <p>Chizmada shaklni koʻring: <b>F</b> boʻlsa teng, <b>Z</b> boʻlsa teng,
  <b>U</b> boʻlsa 180°. Harflar teskari yoki agʻdarilgan boʻlishi mumkin —
  qoida oʻzgarmaydi.</p>
</div>

<h3>Bitta burchakdan sakkiztasi</h3>

<p>Chizmada ∠2 = <b>70°</b> deb berilgan boʻlsin. Qolganini yozib chiqamiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">∠2 = 70°</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">∠1 = 110°</span>
    <span class="pm-solve__why">∠2 ga qoʻshni: 180 − 70 (PM-59)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">∠3 = 70°, ∠4 = 110°</span>
    <span class="pm-solve__why">Vertikal burchaklar — teng</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">∠6 = 70°</span>
    <span class="pm-solve__why">∠3 ga almashinuvchi ichki (Z) — teng</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">∠5 = 110°, ∠7 = 110°, ∠8 = 70°</span>
    <span class="pm-solve__why">Pastki nuqtada yana qoʻshni va vertikal</span>
  </div>
</div>

<figure class="pm-fig">
  <svg viewBox="0 0 320 215" role="img"
       aria-label="Sakkizta burchakning hammasi topilgan">
    <line class="pm-ln" x1="20" y1="60" x2="288" y2="60"/>
    <line class="pm-ln" x1="20" y1="170" x2="288" y2="170"/>
    <line class="pm-ln" x1="40" y1="205" x2="250" y2="10"/>
    <circle class="pm-pt" cx="196.2" cy="60" r="4"/>
    <circle class="pm-pt" cx="77.7" cy="170" r="4"/>
    <text class="pm-lbl" x="294" y="54">a</text>
    <text class="pm-lbl" x="294" y="164">b</text>
    <text class="pm-lbl" x="170.1" y="34.7">110°</text>
    <text class="pm-lbl pm-lbl--hl" x="215.1" y="52.8">70°</text>
    <text class="pm-lbl pm-lbl--hl" x="155.6" y="76.2">70°</text>
    <text class="pm-lbl" x="193.5" y="94.3">110°</text>
    <text class="pm-lbl" x="51.6" y="144.7">110°</text>
    <text class="pm-lbl pm-lbl--hl" x="96.7" y="162.8">70°</text>
    <text class="pm-lbl pm-lbl--hl" x="37.1" y="186.2">70°</text>
    <text class="pm-lbl" x="75" y="204.3">110°</text>
  </svg>
  <figcaption>Faqat ikkita qiymat bor: 70° va 110°. Ularning yigʻindisi —
  180°.</figcaption>
</figure>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Har bir nuqtada toʻrtta burchak: 110 + 70 + 70 + 110 = 360° ✓
  <br>Har bir qoʻshni juftlik: 70 + 110 = 180° ✓</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Chiziqlar parallel boʻlmasa, bu qoidalar ishlamaydi</p>
  <p>«Mos burchaklar teng» degani faqat <b>parallel</b> chiziqlar uchun
  toʻgʻri. Chiziqlar parallel boʻlmasa, sakkizta burchakning hammasi har xil
  chiqishi mumkin. Masala shartida «a ∥ b» yozilganini tekshiring — u yerda
  boʻlmasa, qoidani ishlatib boʻlmaydi.</p>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Nega faqat ikkita qiymat boʻladi</p>
  <p>Parallel chiziqlar kesuvchi bilan <b>bir xil</b> burchak ostida uchrashadi
  — shuning uchun pastki kesishish yuqorigisining aniq nusxasi. Har bir
  nuqtada esa faqat ikkita qiymat bor (burchak va uning qoʻshnisi), demak
  butun chizmada ham ikkitasi.</p>
</div>

<h3>Teskarisi ham toʻgʻri</h3>

<p>Qoidani teskari tomonga ham oʻqish mumkin, va bu amalda juda foydali:
<b>agar mos burchaklar teng chiqsa, demak chiziqlar parallel.</b></p>

<p>Duradgor ikki taxtaning parallel ekanini shunday tekshiradi: bitta qiya
chiziq chizib, ikkita mos burchakni oʻlchaydi. Teng chiqsa — parallel.</p>

<h3>Matnli masala</h3>

<p><b>Duradgorning kesimi.</b> Taxtaning ikki cheti parallel. Duradgor uni
qiya kesdi. Kesim chizigʻi yuqorigi chet bilan <b>62°</b> burchak hosil
qildi.</p>

<p><b>Nima soʻralyapti:</b> kesim chizigʻi pastki chet bilan qanday burchaklar
hosil qiladi?</p>

<p><b>Reja:</b> taxtaning chetlari — parallel chiziqlar, kesim — kesuvchi.
Demak F, Z va U qoidalari ishlaydi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">yuqorida: 62°</span>
    <span class="pm-solve__why">Berilgan burchak</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">pastda mos burchak = 62°</span>
    <span class="pm-solve__why">F qoidasi — mos burchaklar teng</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">pastda bir tomonli ichki = 118°</span>
    <span class="pm-solve__why">U qoidasi: 180 − 62</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>62 + 118 = 180° ✓ — qoʻshni burchaklar. Kesim ikkala chet bilan ham
  <b>bir xil</b> burchaklar hosil qiladi: 62° va 118°.
  <br><b>Javob:</b> pastki chetda ham 62° va 118°.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>62° oʻtkir, demak uning yonidagi burchak albatta oʻtmas boʻlishi
  kerak — 118° shu talabga javob beradi.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Bir tomonli ichki burchaklar teng</p>
  <p class="pe-fix__good">Bir tomonli ichki burchaklarning yigʻindisi 180°</p>
  <p class="pe-fix__why">Faqat <b>F</b> va <b>Z</b> juftliklari teng.
  <b>U</b> juftligi qoʻshni burchakka oʻxshab 180° beradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Chiziqlar parallelmi-yoʻqmi — farqi yoʻq, mos
    burchaklar baribir teng</p>
  <p class="pe-fix__good">Bu qoidalar <b>faqat</b> parallel chiziqlarda
    ishlaydi</p>
  <p class="pe-fix__why">Parallellik — qoidaning sharti. Shartsiz xulosa
  chiqarish geometriyadagi eng jiddiy xato.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">∠3 va ∠5 — almashinuvchi ichki burchaklar</p>
  <p class="pe-fix__good">∠3 va ∠6 — almashinuvchi ichki burchaklar</p>
  <p class="pe-fix__why">Almashinuvchi juftlik kesuvchining <b>har xil</b>
  tomonlarida boʻlishi shart. ∠3 bilan ∠5 esa bitta tomonda.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Sakkizta burchakni bilish uchun sakkizta oʻlchov
    kerak</p>
  <p class="pe-fix__good">Bitta oʻlchov yetadi</p>
  <p class="pe-fix__why">Parallel chiziqlarda faqat <b>ikkita</b> har xil
  qiymat boʻladi, ular esa 180° ga toʻldiradi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. a ∥ b va mos burchaklardan biri 55°. Ikkinchisi
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>55°.</b> Mos burchaklar (F qoidasi) parallel chiziqlarda teng
    boʻladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Bir tomonli ichki burchaklardan biri 105°.
  Ikkinchisi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>75°.</b> U qoidasi: yigʻindisi 180°, demak 180 − 105 = 75.
    Tekshirish: 105 + 75 = 180 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. a ∥ b va ∠2 = 130°. ∠6 va ∠3 qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>∠3 = 50°, ∠6 = 50°.</b> ∠3 — ∠2 ga qoʻshni: 180 − 130 = 50.
    ∠6 — ∠3 ga almashinuvchi ichki (Z), demak teng: 50°.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Kesuvchi ikki chiziqni kesib oʻtdi. Mos
  burchaklar 68° va 74° chiqdi. Chiziqlar parallelmi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Yoʻq, parallel emas.</b> Parallel boʻlganida mos burchaklar teng
    chiqishi shart edi. 68 ≠ 74, demak chiziqlar kesishadi — faqat
    chizmadan tashqarida.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. a ∥ b va bir tomonli ichki burchaklardan biri
  ikkinchisidan 40° katta. Ularni toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>110° va 70°.</b> x + y = 180 va x − y = 40. Qoʻshamiz (PM-54):
    2x = 220, x = 110, keyin y = 70. Tekshirish: 110 + 70 = 180 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Zinapoyaning ikki panjarasi parallel. Ularni bitta
  qiya tayanch kesib oʻtadi va yuqori panjara bilan 35° burchak hosil qiladi.
  Tayanch pastki panjara bilan qanday burchaklar hosil qiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>35° va 145°.</b> Mos burchak (F) teng: 35°. Uning qoʻshnisi esa
    180 − 35 = 145°. Parallel chiziqlarda kesuvchi ikkala chiziq bilan ham
    <b>bir xil</b> burchaklarni hosil qiladi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Parallel chiziqlar</b><span>hech qachon kesishmaydigan chiziqlar,
    a ∥ b; ingl. parallel lines</span></li>
  <li><b>Kesuvchi</b><span>ikkala chiziqni ham kesib oʻtuvchi chiziq; ingl.
    transversal</span></li>
  <li><b>Mos burchaklar</b><span>bir xil oʻrindagi teng burchaklar (F); ingl.
    corresponding angles</span></li>
  <li><b>Almashinuvchi ichki burchaklar</b><span>orada, qarama-qarshi
    tomonlarda; teng (Z); ingl. alternate interior angles</span></li>
  <li><b>Bir tomonli ichki burchaklar</b><span>orada, bitta tomonda;
    yigʻindisi 180° (U); ingl. co-interior angles</span></li>
  <li><b>Ichki burchaklar</b><span>ikki parallel chiziq orasidagilari; ingl.
    interior angles</span></li>
  <li><b>Tashqi burchaklar</b><span>parallel chiziqlardan tashqaridagilari;
    ingl. exterior angles</span></li>
  <li><b>Teskari xulosa</b><span>qoidani teskari tomonga oʻqish; ingl.
    converse</span></li>
  <li><b>Shart</b><span>qoida ishlashi uchun bajarilishi kerak boʻlgan talab;
    ingl. condition</span></li>
  <li><b>Vertikal burchaklar</b><span>PM-59 dagi teng juftlik; ingl. vertical
    angles</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>F — teng, Z — teng, U — 180°.</b> Uchta shakl, uchta qoida.</li>
    <li><b>Bitta burchak yetadi:</b> parallel chiziqlarda faqat ikkita har xil
      qiymat boʻladi.</li>
    <li><b>Parallellik — shart.</b> U boʻlmasa, hech bir qoida ishlamaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-61 — uchburchak turlari va burchaklar yigʻindisi
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-61: Uchburchak turlari va burchaklar yigʻindisi",
        "category": "math",
        "order": 61,
        "summary": (
            "Uchburchaklarni burchagi va tomoni boʻyicha turkumlash, va "
            "geometriyaning eng mashhur qoidasi: uchta burchakning yigʻindisi "
            "har doim 180°. Qoida isbot bilan keladi."
        ),
        "stories": ["Nega uchburchak eng mustahkam shakl"],
        "content": """
<h2>PM-61: Uchburchak turlari va burchaklar yigʻindisi</h2>

<p>Qogʻozdan uchburchak qirqib oling. Uchta burchagini yirtib, uchalasini
bitta chiziq ustiga yonma-yon qoʻying. Ular aynan <b>yoyiq burchak</b>ni
toʻldiradi — 180°.</p>

<p>Qanday uchburchak olsangiz ham shunday chiqadi: yassisini ham, choʻzigʻini
ham. Bu tasodif emas — buni <b>isbotlash</b> mumkin. PM-59 da birinchi
isbotimizni koʻrgan edik; bu ikkinchisi va u PM-60 dagi parallel chiziqlarga
tayanadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>uchburchakni burchagi boʻyicha uch turga ajratasiz;</li>
    <li>tomoni boʻyicha ham uch turga ajratasiz;</li>
    <li>ikki burchagidan uchinchisini topasiz;</li>
    <li>180° qoidasining isbotini tushuntirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Asosiy qoida</span>
  <span class="pe-chip pe-chip--s">∠A</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">∠B</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">∠C</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--adv">180°</span>
</div>

<h3>Burchaklari boʻyicha uch tur</h3>

<figure class="pm-fig">
  <svg viewBox="0 0 320 125" role="img"
       aria-label="Oʻtkir, toʻgʻri va oʻtmas burchakli uchburchaklar">
    <polygon class="pm-fill" points="18,90 78,90 44,34"/>
    <polyline class="pm-ln" points="18,90 78,90 44,34 18,90" fill="none"/>
    <path class="pm-ln pm-ln--hl" d="M 33 90 A 15 15 0 0 0 24.3 76.4" fill="none"/>
    <text class="pm-lbl" x="26.3" y="115">oʻtkir</text>
    <polygon class="pm-fill" points="126,90 186,90 126,36"/>
    <polyline class="pm-ln" points="126,90 186,90 126,36 126,90" fill="none"/>
    <polyline class="pm-ln" points="137,90 137,79 126,79" fill="none"/>
    <text class="pm-lbl" x="122.2" y="115">toʻgʻri</text>
    <polygon class="pm-fill" points="222,90 300,90 215,58"/>
    <polyline class="pm-ln" points="222,90 300,90 215,58 222,90" fill="none"/>
    <path class="pm-ln pm-ln--hl" d="M 237 90 A 15 15 0 0 0 218.8 75.3" fill="none"/>
    <text class="pm-lbl" x="225.3" y="115">oʻtmas</text>
  </svg>
  <figcaption>Chapdagida hamma burchak 90° dan kichik; oʻrtadagida bittasi
  aniq 90°; oʻngdagida bittasi 90° dan katta.</figcaption>
</figure>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Turi</th><th>Sharti</th><th>Nechtasi shunday</th></tr>
  <tr><td>Oʻtkir burchakli</td><td class="pm-word__sym">hammasi &lt; 90°</td>
    <td>uchalasi</td></tr>
  <tr><td>Toʻgʻri burchakli</td><td class="pm-word__sym">bittasi = 90°</td>
    <td>faqat bittasi</td></tr>
  <tr><td>Oʻtmas burchakli</td><td class="pm-word__sym">bittasi &gt; 90°</td>
    <td>faqat bittasi</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Nega ikkita toʻgʻri burchak boʻlolmaydi?</p>
  <p>Chunki 90 + 90 = 180 boʻlib, uchinchi burchakka <b>hech narsa
  qolmaydi</b>. Xuddi shu sabab bilan bitta uchburchakda ikkita oʻtmas burchak
  ham boʻlolmaydi. Har bir uchburchakda kamida <b>ikkita</b> oʻtkir burchak
  bor.</p>
</div>

<h3>Tomonlari boʻyicha uch tur</h3>

<figure class="pm-fig">
  <svg viewBox="0 0 320 122" role="img"
       aria-label="Turli tomonli, teng yonli va teng tomonli uchburchaklar">
    <polygon class="pm-fill" points="12,88 68,88 60,40"/>
    <polyline class="pm-ln" points="12,88 68,88 60,40 12,88" fill="none"/>
    <text class="pm-lbl" x="2.5" y="112">turli tomonli</text>
    <polygon class="pm-fill" points="120,88 168,88 144,26"/>
    <polyline class="pm-ln" points="120,88 168,88 144,26 120,88" fill="none"/>
    <line class="pm-ln" x1="126.4" y1="54.8" x2="137.6" y2="59.2"/>
    <line class="pm-ln" x1="150.4" y1="59.2" x2="161.6" y2="54.8"/>
    <text class="pm-lbl" x="110" y="112">teng yonli</text>
    <polygon class="pm-fill" points="222,88 290,88 256,29.1"/>
    <polyline class="pm-ln" points="222,88 290,88 256,29.1 222,88" fill="none"/>
    <line class="pm-ln" x1="233.8" y1="55.6" x2="244.2" y2="61.5"/>
    <line class="pm-ln" x1="267.8" y1="61.5" x2="278.2" y2="55.6"/>
    <line class="pm-ln" x1="256" y1="82" x2="256" y2="94"/>
    <text class="pm-lbl" x="215.2" y="112">teng tomonli</text>
  </svg>
  <figcaption>Tomondagi kichik chiziqcha «bu tomonlar teng» degani — chizmada
  shunday belgilanadi.</figcaption>
</figure>

<p><b>Turli tomonli</b> — uchala tomoni ham har xil. <b>Teng yonli</b> —
ikkita tomoni teng. <b>Teng tomonli</b> — uchalasi ham teng (va uning har bir
burchagi 60°, chunki 180 ÷ 3 = 60).</p>

<h3>Yigʻindi nega aynan 180°?</h3>

<p>Uchburchak ABC ni olamiz va uning B uchidan <b>AC tomoniga parallel</b>
chiziq oʻtkazamiz. Endi PM-60 ishga tushadi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 200" role="img"
       aria-label="Uchburchak burchaklari yigʻindisining isboti">
    <polygon class="pm-fill" points="50,170 270,170 140,50"/>
    <polyline class="pm-ln" points="50,170 270,170 140,50 50,170" fill="none"/>
    <line class="pm-ln pm-ln--dash" x1="55" y1="50" x2="245" y2="50"/>
    <path class="pm-ln pm-ln--hl" d="M 80 170 A 30 30 0 0 0 68 146" fill="none"/>
    <text class="pm-lbl pm-lbl--hl" x="85.8" y="154.8">1</text>
    <path class="pm-ln pm-ln--hl" d="M 248 149.7 A 30 30 0 0 0 240 170" fill="none"/>
    <text class="pm-lbl pm-lbl--hl" x="225.4" y="158.5">2</text>
    <path class="pm-ln pm-ln--hl" d="M 114 50 A 26 26 0 0 0 124.4 70.8" fill="none"/>
    <text class="pm-lbl pm-lbl--hl" x="100.6" y="72.4">1</text>
    <path class="pm-ln" d="M 119.6 77.2 A 34 34 0 0 0 165 73.1" fill="none"/>
    <text class="pm-lbl" x="140.9" y="104.3">3</text>
    <path class="pm-ln pm-ln--hl" d="M 159.1 67.6 A 26 26 0 0 0 166 50" fill="none"/>
    <text class="pm-lbl pm-lbl--hl" x="173.7" y="69.1">2</text>
    <text class="pm-lbl" x="36" y="186">A</text>
    <text class="pm-lbl" x="136" y="38">B</text>
    <text class="pm-lbl" x="276" y="186">C</text>
    <text class="pm-lbl" x="216" y="44">AC ga parallel</text>
  </svg>
  <figcaption>B uchidagi uchta burchak toʻgʻri chiziqni toʻldiradi — va ular
  uchburchakning oʻz burchaklari.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">B dan AC ga parallel chiziq</span>
    <span class="pm-solve__why">Yordamchi chiziq — isbotning butun hiylasi
    shu</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">∠1 (B da) = ∠A</span>
    <span class="pm-solve__why">AB kesuvchi; almashinuvchi ichki burchaklar
    (Z) — teng</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">∠2 (B da) = ∠C</span>
    <span class="pm-solve__why">BC kesuvchi; yana almashinuvchi ichki (Z)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">∠1 + ∠3 + ∠2 = 180°</span>
    <span class="pm-solve__why">Uchalasi B da yoyiq burchakni toʻldiradi
    (PM-58)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">∠A + ∠B + ∠C = 180°</span>
    <span class="pm-solve__why">Tenglarni oʻrniga qoʻydik</span>
  </div>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Isbot nima berdi</p>
  <p>Biz bitta ham burchakni oʻlchamadik. Shuning uchun bu xulosa <b>hamma</b>
  uchburchaklar uchun toʻgʻri — hatto chizib boʻlmaydigan darajada katta yoki
  kichiklari uchun ham. Qogʻoz yirtish gʻoyani <b>koʻrsatadi</b>, isbot esa
  uni <b>kafolatlaydi</b>.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Javobni har doim qoʻshib tekshiring</p>
  <p>Uchta burchakni topganingizdan keyin ularni qoʻshing. Yigʻindi 180°
  chiqmasa — hisobda xato bor. Bu butun blokdagi eng tez ishlaydigan
  nazorat, va u bir sekund oladi.</p>
</div>

<h3>Uchinchi burchakni topish</h3>

<div class="pe-ex">
  <p class="pe-ex__math">∠A = 47°, ∠B = 65° → ∠C = 180 − 47 − 65 = 68°</p>
  <p class="pe-ex__uz">Ikkitasini bilsak, uchinchisi 180 dan ayirish bilan
  topiladi.</p>
  <p class="pe-ex__why">Tekshirish: 47 + 65 + 68 = 180 ✓</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">Toʻgʻri burchakli uchburchak, ∠A = 90°, ∠B = 35°
  → ∠C = 55°</p>
  <p class="pe-ex__uz">Toʻgʻri burchakli uchburchakda qolgan ikki burchak
  birgalikda 90° beradi.</p>
  <p class="pe-ex__why">180 − 90 = 90, keyin 90 − 35 = 55 ✓</p>
</div>

<h3>Matnli masala</h3>

<p><b>Uchburchak shaklidagi bogʻ.</b> Mahalladagi kichik bogʻ uchburchak
shaklida. Loyihachining chizmasida burchaklar <b>2 : 3 : 4</b> nisbatda
koʻrsatilgan.</p>

<p><b>Nima soʻralyapti:</b> uchala burchak va bogʻning turi.</p>

<p><b>Reja:</b> nisbat degani ulushlar (PM-27). Bitta ulushni x deb olamiz;
ulushlar yigʻindisi 180° ni beradi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + 3x + 4x = 180</span>
    <span class="pm-solve__why">Burchaklar yigʻindisi 180°</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">9x = 180</span>
    <span class="pm-solve__why">Oʻxshash hadlar (PM-32)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = 20</span>
    <span class="pm-solve__why">Bitta ulush 20°</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">40°, 60°, 80°</span>
    <span class="pm-solve__why">2 × 20, 3 × 20, 4 × 20</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>40 + 60 + 80 = 180 ✓ va 40 : 60 : 80 = 2 : 3 : 4 ✓
  <br>Eng katta burchak 80°, u 90 dan kichik — demak bogʻ <b>oʻtkir
  burchakli</b> uchburchak. Uchala burchak har xil, demak <b>turli
  tomonli</b>.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Toʻqqizta ulush 180° ni boʻlsa, bitta ulush 20° atrofida boʻlishi
  kerak — 180 ÷ 9 = 20 aynan shunday chiqdi.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Uchburchakda burchaklar 90°, 60° va 40°</p>
  <p class="pe-fix__good">Bunday uchburchak mavjud emas</p>
  <p class="pe-fix__why">90 + 60 + 40 = 190 ≠ 180. Har qanday javobni
  qoʻshib tekshiring.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Katta uchburchakning burchaklari yigʻindisi
    kattaroq</p>
  <p class="pe-fix__good">Yigʻindi har doim 180°, oʻlchamdan qatʼi nazar</p>
  <p class="pe-fix__why">Burchak <b>burilish</b>ni oʻlchaydi (PM-58) —
  tomonlarni choʻzish burchakni oʻzgartirmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Teng tomonli uchburchakning burchaklari 90° dan</p>
  <p class="pe-fix__good">Teng tomonli uchburchakning har bir burchagi 60°</p>
  <p class="pe-fix__why">180 ÷ 3 = 60. Uchta 90° li burchak 270° beradi —
  bu mumkin emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Nisbat 2 : 3 : 4 → burchaklar 2°, 3°, 4°</p>
  <p class="pe-fix__good">Nisbat ulushni bildiradi: 2x + 3x + 4x = 180</p>
  <p class="pe-fix__why">2 + 3 + 4 = 9 boʻlib, 180° emas. Nisbat sonlarning
  <b>oʻzi</b> emas, ularning <b>nisbati</b> (PM-27).</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Uchburchakning ikki burchagi 52° va 61°. Uchinchisi
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>67°.</b> 180 − 52 − 61 = 67. Tekshirish: 52 + 61 + 67 = 180 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Toʻgʻri burchakli uchburchakning oʻtkir
  burchaklaridan biri 28°. Ikkinchisi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>62°.</b> Toʻgʻri burchak 90° ni oladi, qolgan ikkitasiga 90° qoladi:
    90 − 28 = 62. Tekshirish: 90 + 28 + 62 = 180 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Teng tomonli uchburchakning burchaklari qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Har biri 60°.</b> Uchala tomoni teng boʻlgani uchun uchala burchagi
    ham teng: 180 ÷ 3 = 60.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Uchburchakda 100° li burchak bor. Bu qanday
  uchburchak va qolgan ikki burchak haqida nima deyish mumkin?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Oʻtmas burchakli; qolgan ikkitasi birgalikda 80°.</b> 180 − 100 = 80,
    demak ikkalasi ham albatta oʻtkir. Uchburchakda ikkita oʻtmas burchak
    boʻlishi mumkin emas.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Uchburchakning burchaklari 1 : 2 : 3 nisbatda.
  Ularni toping va turini ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>30°, 60°, 90° — toʻgʻri burchakli.</b> x + 2x + 3x = 180, 6x = 180,
    x = 30. Tekshirish: 30 + 60 + 90 = 180 ✓ Eng kattasi aniq 90°, demak
    toʻgʻri burchakli uchburchak.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Tom yopayotgan usta uchburchak shaklidagi ferma
  yasadi. Pastki ikki burchak teng va har biri 35°. Yuqoridagi burchak
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>110°.</b> Pastki ikkitasi birga 35 + 35 = 70°, demak yuqoridagisi
    180 − 70 = 110°. Tekshirish: 35 + 35 + 110 = 180 ✓ Bu oʻtmas burchakli
    uchburchak — tom yassi boʻladi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Uchburchak</b><span>uchta tomoni va uchta burchagi bor shakl; ingl.
    triangle</span></li>
  <li><b>Oʻtkir burchakli</b><span>hamma burchagi 90° dan kichik; ingl. acute
    triangle</span></li>
  <li><b>Toʻgʻri burchakli</b><span>bitta burchagi 90°; ingl. right
    triangle</span></li>
  <li><b>Oʻtmas burchakli</b><span>bitta burchagi 90° dan katta; ingl. obtuse
    triangle</span></li>
  <li><b>Turli tomonli</b><span>uchala tomoni har xil; ingl. scalene</span></li>
  <li><b>Teng yonli</b><span>ikki tomoni teng; ingl. isosceles</span></li>
  <li><b>Teng tomonli</b><span>uchala tomoni teng, burchaklari 60°; ingl.
    equilateral</span></li>
  <li><b>Burchaklar yigʻindisi</b><span>har doim 180°; ingl. angle sum</span></li>
  <li><b>Yordamchi chiziq</b><span>isbot uchun qoʻshimcha chizilgan chiziq;
    ingl. auxiliary line</span></li>
  <li><b>Nisbat</b><span>ulushlarning oʻzaro munosabati, 2 : 3 : 4; ingl.
    ratio</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Uchta burchak har doim 180° beradi</b> — uchburchak qanchalik
      katta yoki kichik boʻlishidan qatʼi nazar.</li>
    <li><b>Ikkitasini bilsangiz, uchinchisi ayirish bilan topiladi.</b></li>
    <li><b>Isbot yordamchi chiziqdan tugʻildi:</b> uchidan asosga parallel
      chiziq oʻtkazish yetarli boʻldi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-62 — uchburchak tengsizligi
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-62: Uchburchak tengsizligi: tomon va burchak bogʻliqligi",
        "category": "math",
        "order": 62,
        "summary": (
            "Har uchta uzunlikdan uchburchak yasab boʻlmaydi: ikki tomonning "
            "yigʻindisi uchinchisidan katta boʻlishi shart. Va uchburchak "
            "ichida katta burchak har doim katta tomonning qarshisida turadi."
        ),
        "stories": ["Uch tayoq — uchburchak chiqadimi?"],
        "content": """
<h2>PM-62: Uchburchak tengsizligi: tomon va burchak bogʻliqligi</h2>

<p>Uchta tayoq oling: 3 sm, 4 sm va 8 sm. Ulardan uchburchak yasashga urinib
koʻring. Qanday burasangiz ham chiqmaydi — qisqa ikkitasi uzunining ikki
uchini <b>tutashtira olmaydi</b>.</p>

<p>Endi uzunini 6 sm ga almashtiring. Darrov chiqadi. Farq qayerda? Mana shu
darsning savoli.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>berilgan uch uzunlikdan uchburchak chiqadimi-yoʻqmi, aniqlaysiz;</li>
    <li>uchinchi tomon qaysi oraliqda boʻlishini topasiz;</li>
    <li>katta burchak qaysi tomon qarshisida turishini bilasiz;</li>
    <li>«toʻgʻri yoʻl eng qisqa» degan gapni matematik isbotlaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uchburchak tengsizligi</span>
  <span class="pe-chip pe-chip--s">a + b</span>
  <span class="pe-op">&gt;</span>
  <span class="pe-chip pe-chip--o">c</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--aux">har uch juftlik uchun</span>
</div>

<h3>Nega yopilmaydi?</h3>

<figure class="pm-fig">
  <svg viewBox="0 0 320 145" role="img"
       aria-label="3 va 4 uzunlikdagi tayoqlar 8 uzunlikni tutashtira olmaydi">
    <line class="pm-ln" x1="40" y1="115" x2="280" y2="115"/>
    <circle class="pm-pt" cx="40" cy="115" r="4"/>
    <circle class="pm-pt" cx="280" cy="115" r="4"/>
    <text class="pm-lbl" x="152" y="134">8</text>
    <line class="pm-ln pm-ln--hl" x1="40" y1="75" x2="130" y2="75"/>
    <text class="pm-lbl pm-lbl--hl" x="80" y="66">3</text>
    <line class="pm-ln pm-ln--hl" x1="280" y1="75" x2="160" y2="75"/>
    <text class="pm-lbl pm-lbl--hl" x="216" y="66">4</text>
    <line class="pm-ln pm-ln--dash" x1="130" y1="75" x2="160" y2="75"/>
    <text class="pm-lbl" x="112" y="52">yetmaydi</text>
  </svg>
  <figcaption>3 + 4 = 7, bu esa 8 dan kichik. Tayoqlarni toʻgʻri yotqizsak
  ham bir birlik yetmaydi.</figcaption>
</figure>

<figure class="pm-fig">
  <svg viewBox="0 0 320 170" role="img"
       aria-label="3, 4 va 6 uzunlikdagi tayoqlardan uchburchak chiqadi">
    <polygon class="pm-fill" points="70,140 250,140 142.5,86.7"/>
    <polyline class="pm-ln" points="70,140 250,140 142.5,86.7 70,140" fill="none"/>
    <text class="pm-lbl" x="156" y="158">6</text>
    <text class="pm-lbl pm-lbl--hl" x="92.2" y="113.3">3</text>
    <text class="pm-lbl pm-lbl--hl" x="202.2" y="113.3">4</text>
  </svg>
  <figcaption>3 + 4 = 7 &gt; 6 — endi tayoqlar yetadi va uchburchak
  yopiladi.</figcaption>
</figure>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Uchburchak tengsizligi</p>
  <p>Uchburchakning <b>har ikki tomoni yigʻindisi uchinchi tomonidan
  katta</b>:
  <br>a + b &gt; c, &nbsp; a + c &gt; b, &nbsp; b + c &gt; a.
  <br>Uchala shart ham bajarilishi kerak.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Amalda faqat bitta tekshiruv yetadi</p>
  <p>Uchta shartni yozib oʻtirmang: <b>eng qisqa ikki tomonni qoʻshib, eng
  uzuniga taqqoslang.</b> Agar shu shart bajarilsa, qolgan ikkitasi
  avtomatik bajariladi — chunki eng uzun tomonga kichikroq son qoʻshilganda
  yigʻindi baribir katta chiqadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">5, 9, 13 → 5 + 9 = 14 &gt; 13 ✓</p>
  <p class="pe-ex__uz">Uchburchak chiqadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">4, 6, 10 → 4 + 6 = 10, bu 10 dan <b>katta emas</b></p>
  <p class="pe-ex__uz">Uchburchak chiqmaydi — tayoqlar aynan yopishadi va
  yassi chiziq hosil boʻladi.</p>
  <p class="pe-ex__why">Tenglik ham yetmaydi: qatʼiy <b>katta</b> boʻlishi
  shart.</p>
</div>

<h3>Uchinchi tomon qaysi oraliqda?</h3>

<p>Ikki tomoni 5 va 7 boʻlgan uchburchakning uchinchi tomoni qanday
boʻlishi mumkin? Ikkita chegara bor.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x &lt; 5 + 7 = 12</span>
    <span class="pm-solve__why">Ikki tomon yigʻindisidan kichik boʻlishi
    kerak</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x &gt; 7 − 5 = 2</span>
    <span class="pm-solve__why">Farqidan katta: aks holda 5 + x &gt; 7 sharti
    buziladi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2 &lt; x &lt; 12</span>
    <span class="pm-solve__why">Oraliq (PM-40 dagi qoʻsh tengsizlik)</span>
  </div>
</div>

<div class="pm-num">
  <div class="pm-num__track">
    <span class="pm-num__band" style="left:14.3%;width:71.4%"></span>
    <span class="pm-num__tick" style="left:0%"><i>0</i></span>
    <span class="pm-num__tick" style="left:14.3%"><i>2</i></span>
    <span class="pm-num__tick" style="left:85.7%"><i>12</i></span>
    <span class="pm-num__tick" style="left:100%"><i>14</i></span>
    <span class="pm-num__dot" style="left:50%"><i>x</i></span>
  </div>
</div>

<p>Boʻyalgan oraliq — mumkin boʻlgan qiymatlar. Chetlarining oʻzi kirmaydi:
x = 2 yoki x = 12 boʻlsa, uchburchak yassilanib qoladi.</p>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Chegaraning oʻzi javobga kirmaydi</p>
  <p>«2 dan 12 gacha» degan gap ikki xil tushuniladi. Bu yerda 2 ning oʻzi
  ham, 12 ning oʻzi ham <b>boʻlmaydi</b> — ularda uchburchak yassilanib
  qoladi. Shuning uchun belgi <b>&lt;</b>, hech qachon <b>≤</b> emas.</p>
</div>

<h3>Katta tomon — katta burchak</h3>

<p>Uchburchak ichida tomonlar bilan burchaklar bogʻlangan: <b>eng uzun tomon
qarshisida eng katta burchak turadi</b>, eng qisqa tomon qarshisida esa eng
kichigi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 195" role="img"
       aria-label="Katta burchak katta tomonning qarshisida turadi">
    <polygon class="pm-fill" points="40,160 280,160 90,50"/>
    <polyline class="pm-ln" points="40,160 280,160 90,50 40,160" fill="none"/>
    <path class="pm-ln pm-ln--hl" d="M 79.2 73.7 A 26 26 0 0 0 112.5 63" fill="none"/>
    <path class="pm-ln" d="M 254 145 A 30 30 0 0 0 250 160" fill="none"/>
    <text class="pm-lbl pm-lbl--hl" x="100" y="92">eng katta</text>
    <text class="pm-lbl" x="212" y="146">eng kichik</text>
    <text class="pm-lbl pm-lbl--hl" x="122" y="180">eng uzun tomon</text>
    <text class="pm-lbl" x="4" y="112">eng qisqa</text>
    <text class="pm-lbl" x="24" y="174">A</text>
    <text class="pm-lbl" x="288" y="174">B</text>
    <text class="pm-lbl" x="84" y="38">C</text>
  </svg>
  <figcaption>AB eng uzun tomon — uning qarshisidagi ∠C eng katta. AC eng
  qisqa — qarshisidagi ∠B eng kichik.</figcaption>
</figure>

<div class="pe-ex">
  <p class="pe-ex__math">Tomonlari 6, 9, 11 → eng katta burchak 11 ning
  qarshisida</p>
  <p class="pe-ex__uz">Tomonlarni tartiblab chiqsangiz, burchaklar ham oʻsha
  tartibda joylashadi.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Doʻkon orqali yoki toʻgʻri?</b> Sherbekning uyidan maktabgacha toʻgʻri
yoʻl bilan <b>800</b> metr. Doʻkon orqali yursa, uydan doʻkongacha
<b>500</b> metr, doʻkondan maktabgacha esa <b>400</b> metr.</p>

<p><b>Nima soʻralyapti:</b> qaysi yoʻl qisqa va nechchi metrga.</p>

<p><b>Reja:</b> uch nuqta — uy, doʻkon, maktab — uchburchak hosil qiladi.
Doʻkon orqali yurish ikki tomonni bosib oʻtish, toʻgʻri yurish esa
uchinchisini.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">500 + 400 = 900 m</span>
    <span class="pm-solve__why">Doʻkon orqali</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">800 m</span>
    <span class="pm-solve__why">Toʻgʻri yoʻl</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">900 − 800 = 100 m</span>
    <span class="pm-solve__why">Toʻgʻri yoʻl 100 metrga qisqa</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz — uchburchak haqiqiymi?</p>
  <p>500 + 400 = 900 &gt; 800 ✓, 800 + 400 = 1200 &gt; 500 ✓,
  800 + 500 = 1300 &gt; 400 ✓ — uchala shart bajarildi, demak bunday uch
  nuqta haqiqatan mavjud.
  <br><b>Javob:</b> toʻgʻri yoʻl 100 metrga qisqa.</p>
</div>

<p>Eʼtibor bering: bu tasodif emas. Uchburchak tengsizligi aynan shuni
aytadi — <b>ikki nuqta orasidagi eng qisqa yoʻl toʻgʻri chiziq</b>. Uchinchi
nuqtaga burilib borish har doim uzunroq.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">4, 6, 10 — uchburchak chiqadi, chunki 4 + 6 = 10</p>
  <p class="pe-fix__good">Chiqmaydi: yigʻindi <b>qatʼiy katta</b> boʻlishi
    kerak</p>
  <p class="pe-fix__why">Teng boʻlsa, tayoqlar uzun tayoq ustiga yotib
  qoladi va uchburchak yassilanadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">3, 4, 8: 3 + 8 = 11 &gt; 4, demak chiqadi</p>
  <p class="pe-fix__good">Eng qisqa ikkitasini tekshiring: 3 + 4 = 7 &lt; 8 ✗</p>
  <p class="pe-fix__why">Bitta shart bajarilgani yetarli emas — <b>uchalasi
  ham</b> bajarilishi kerak, va faqat eng qisqa ikkitasi tekshiruvga
  arziydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Tomonlari 5 va 7 → uchinchisi 2 dan 12 gacha,
    chegaralari bilan</p>
  <p class="pe-fix__good">2 &lt; x &lt; 12, chegaralarsiz</p>
  <p class="pe-fix__why">x = 2 va x = 12 da uchburchak yassilanib qoladi.
  Belgi <b>&lt;</b>, <b>≤</b> emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Eng katta burchak eng uzun tomonning yonida</p>
  <p class="pe-fix__good">Eng katta burchak eng uzun tomonning
    <b>qarshisida</b></p>
  <p class="pe-fix__why">Burchak oʻzi turgan tomonga emas, <b>roʻparasidagi</b>
  tomonga bogʻlangan. Chizmada barmoq bilan koʻrsatib tekshiring.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 7, 10 va 15 uzunlikdagi tayoqlardan uchburchak
  chiqadimi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Ha.</b> Eng qisqa ikkitasi: 7 + 10 = 17, bu 15 dan katta ✓
    Demak uchburchak yopiladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 2, 3 va 6 uzunlikdagi tayoqlardan uchburchak
  chiqadimi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Yoʻq.</b> 2 + 3 = 5, bu 6 dan kichik. Ikki qisqa tayoq uzunining
    uchlarini tutashtira olmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Uchburchakning ikki tomoni 8 va 3. Uchinchi tomon
  qaysi oraliqda boʻlishi mumkin?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5 &lt; x &lt; 11.</b> Yuqori chegara: 8 + 3 = 11. Quyi chegara:
    8 − 3 = 5. Masalan 6, 7 yoki 10 boʻlishi mumkin, 5 yoki 11 esa yoʻq.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Uchburchakning tomonlari 6, 9 va 11. Eng katta
  burchak qaysi tomonning qarshisida?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>11 uzunlikdagi tomonning qarshisida.</b> Eng uzun tomon qarshisida
    eng katta burchak turadi. Eng kichik burchak esa 6 ning qarshisida.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Uchburchakning ikki tomoni 9 va 9. Uchinchi tomon
  butun son boʻlsa, u eng koʻpi bilan qancha boʻlishi mumkin?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>17.</b> Shart: x &lt; 9 + 9 = 18, demak eng katta butun son 17.
    Quyi chegara esa x &gt; 9 − 9 = 0, yaʼni x kamida 1 boʻlishi kerak.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Uch qishloq uchburchak hosil qiladi. A dan B gacha
  12 km, B dan C gacha 9 km. Dilnoza A dan C ga toʻgʻri bordi. Uning yoʻli
  eng koʻpi bilan va eng kami bilan qancha boʻlishi mumkin?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3 km dan koʻp, 21 km dan kam.</b> 12 + 9 = 21 va 12 − 9 = 3, demak
    3 &lt; AC &lt; 21. Masalan 15 km boʻlishi mumkin, 22 km esa hech qachon —
    aks holda A dan B va C orqali borish toʻgʻri yoʻldan qisqa chiqib
    qolardi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Uchburchak tengsizligi</b><span>ikki tomon yigʻindisi uchinchisidan
    katta; ingl. triangle inequality</span></li>
  <li><b>Tomon</b><span>uchburchakning kesmalaridan biri; ingl. side</span></li>
  <li><b>Qarshisidagi burchak</b><span>tomonga tegmaydigan burchak; ingl.
    opposite angle</span></li>
  <li><b>Oraliq</b><span>qiymat tushishi mumkin boʻlgan chegaralar; ingl.
    range</span></li>
  <li><b>Qoʻsh tengsizlik</b><span>2 &lt; x &lt; 12 koʻrinishi; ingl.
    compound inequality</span></li>
  <li><b>Qatʼiy tengsizlik</b><span>&lt; belgisi, chegara kirmaydi; ingl.
    strict inequality</span></li>
  <li><b>Yassilangan uchburchak</b><span>uchala uchi bitta chiziqda; ingl.
    degenerate triangle</span></li>
  <li><b>Eng qisqa yoʻl</b><span>ikki nuqta orasidagi toʻgʻri chiziq; ingl.
    shortest path</span></li>
  <li><b>Chegara</b><span>oraliqning eng chetki qiymati; ingl. bound</span></li>
  <li><b>Shart</b><span>bajarilishi kerak boʻlgan talab; ingl.
    condition</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Eng qisqa ikkita tomonni qoʻshib, eng uzuniga taqqoslang.</b>
      Katta chiqsa — uchburchak bor.</li>
    <li><b>Uchinchi tomon farq bilan yigʻindi orasida yotadi:</b>
      |a − b| &lt; x &lt; a + b.</li>
    <li><b>Katta burchak katta tomonning qarshisida</b> — yonida emas.</li>
  </ul>
</div>
""",
    },
]
