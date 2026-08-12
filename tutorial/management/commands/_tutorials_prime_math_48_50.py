# -*- coding: utf-8 -*-
"""Prime Math — darslar 48–50 (jadvaldan grafikka, y = kx + b, k va b).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt

  mashqlar — practice/management/commands/_practice_pm_48_50.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_48_50.py

⚠️ Kumulyativ chegaralar:
  • PM-48 — jadval → nuqtalar → chiziq; grafikdan qiymat oʻqish; uzluksiz va
    diskret maʼlumot farqi. Chiziqning tenglamasi bu darsda soʻralmaydi;
  • PM-49 — y = kx + b, b = boshlangʻich qiymat, k = qadam; chiziqni ikki
    nuqta yoki «b dan boshlab k boʻyicha yurish» bilan chizish;
  • PM-50 — k va b ning real maʼnosi, parallel chiziqlar, kamayuvchi chiziq.
    ⛔ Ikki chiziqning KESISHISHINI algebra bilan yechish YOʻQ — u PM-52
    (sistema). Kesishgan nuqta faqat jadvaldan/grafikdan oʻqiladi va
    «PM-52 da oʻrganamiz» deb aytiladi;
  • parabola (PM-56), Pifagor (PM-64) va oʻrta arifmetik (PM-78) YOʻQ;
  • funksiya (PM-47), koordinata (PM-45), tenglama (PM-36), manfiy sonlar
    (PM-9…11) va modul (PM-41) faol ishlatiladi.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_48_50.py --author=prime
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
    # PM-48 — jadvaldan grafikka
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-48: Jadvaldan grafikka",
        "category": "math",
        "order": 48,
        "summary": (
            "Funksiyaning qiymatlar jadvalini nuqtalarga, nuqtalarni esa grafikka "
            "aylantirish; grafikdan qiymat oʻqish va qaysi maʼlumotni chiziq bilan "
            "bogʻlash mumkinligini bilish."
        ),
        "stories": ["Bir haftalik harorat"],
        "content": """
<h2>PM-48: Jadvaldan grafikka</h2>

<p>Shifokorning qoʻlidagi harorat qogʻoziga qarang: u yerda sonlar emas, egri
chiziq turadi. Sabab oddiy — <b>koʻz sonlarni emas, shaklni tez oʻqiydi</b>.
Yigirmata sonni oʻqib chiqquncha ancha vaqt ketadi, koʻtarilib borayotgan
chiziqni esa bir soniyada koʻrasiz.</p>

<p>PM-47 da funksiyani jadval bilan yozgan edik. Endi shu jadvalni rasmga
aylantiramiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>funksiyaning qiymatlar jadvalini tuzasiz;</li>
    <li>jadvaldagi juftliklarni koordinata tekisligiga nuqta qilib qoʻyasiz;</li>
    <li>grafikdan istalgan qiymatni oʻqiysiz;</li>
    <li>qaysi maʼlumotni chiziq bilan bogʻlash mumkinligini ajratasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uch qadam</span>
  <span class="pe-chip pe-chip--o">jadval</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">nuqtalar</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">chiziq</span>
</div>

<h3>1. Grafik nima?</h3>

<p>Funksiyaning <b>grafigi</b> — uning barcha (x; y) juftliklari koordinata
tekisligiga qoʻyilganda hosil boʻladigan shakl. Har bir nuqta bitta hisobning
natijasi: chapga-oʻngga borish — kirish, yuqoriga-pastga borish — chiqish.</p>

<h3>2. Birinchi qadam — jadval</h3>

<p>y = x + 2 funksiyasini olamiz. Bir necha x tanlaymiz va har biriga y ni
hisoblaymiz. Manfiy sonlarni ham olish shart, aks holda chiziqning yarmini
koʻrmaysiz.</p>

<div class="pe-table-wrap"><table>
  <tr><th>x</th><td>−2</td><td>−1</td><td>0</td><td>1</td><td>2</td><td>3</td></tr>
  <tr><th>y</th><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__math">x = −2 → y = −2 + 2 = 0</p>
  <p class="pe-ex__uz">Minus ikki kiritildi, nol chiqdi.</p>
  <p class="pe-ex__why">Manfiy songa ikki qoʻshilganda natija nolga yaqinlashadi
  (PM-10).</p>
</div>

<h3>3. Ikkinchi qadam — nuqtalar</h3>

<p>Jadvalning har bir ustuni bitta nuqta beradi: (−2; 0), (−1; 1), (0; 2),
(1; 3), (2; 4), (3; 5). Ularni PM-45 dagidek qoʻyamiz.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 300 260" role="img" aria-label="y = x + 2 funksiyasining grafigi">
    <line class="pm-ln pm-ln--dash" x1="30" y1="30" x2="30" y2="240"/>
    <line class="pm-ln pm-ln--dash" x1="60" y1="30" x2="60" y2="240"/>
    <line class="pm-ln pm-ln--dash" x1="90" y1="30" x2="90" y2="240"/>
    <line class="pm-ln pm-ln--dash" x1="150" y1="30" x2="150" y2="240"/>
    <line class="pm-ln pm-ln--dash" x1="180" y1="30" x2="180" y2="240"/>
    <line class="pm-ln pm-ln--dash" x1="210" y1="30" x2="210" y2="240"/>
    <line class="pm-ln pm-ln--dash" x1="240" y1="30" x2="240" y2="240"/>
    <line class="pm-ln pm-ln--dash" x1="270" y1="30" x2="270" y2="240"/>
    <line class="pm-ln pm-ln--dash" x1="30" y1="30" x2="270" y2="30"/>
    <line class="pm-ln pm-ln--dash" x1="30" y1="60" x2="270" y2="60"/>
    <line class="pm-ln pm-ln--dash" x1="30" y1="90" x2="270" y2="90"/>
    <line class="pm-ln pm-ln--dash" x1="30" y1="120" x2="270" y2="120"/>
    <line class="pm-ln pm-ln--dash" x1="30" y1="150" x2="270" y2="150"/>
    <line class="pm-ln pm-ln--dash" x1="30" y1="180" x2="270" y2="180"/>
    <line class="pm-ln pm-ln--dash" x1="30" y1="240" x2="270" y2="240"/>
    <line class="pm-ln" x1="20" y1="210" x2="288" y2="210"/>
    <line class="pm-ln" x1="120" y1="252" x2="120" y2="22"/>
    <line class="pm-ln pm-ln--hl" x1="30" y1="240" x2="240" y2="30"/>
    <circle class="pm-pt" cx="60" cy="210" r="4"/>
    <circle class="pm-pt" cx="90" cy="180" r="4"/>
    <circle class="pm-pt" cx="120" cy="150" r="4"/>
    <circle class="pm-pt" cx="150" cy="120" r="4"/>
    <circle class="pm-pt" cx="180" cy="90" r="4"/>
    <circle class="pm-pt" cx="210" cy="60" r="4"/>
    <text class="pm-lbl" x="60" y="228" text-anchor="middle">−2</text>
    <text class="pm-lbl" x="180" y="228" text-anchor="middle">2</text>
    <text class="pm-lbl" x="112" y="228" text-anchor="end">O</text>
    <text class="pm-lbl" x="112" y="154" text-anchor="end">2</text>
    <text class="pm-lbl" x="112" y="94" text-anchor="end">4</text>
    <text class="pm-lbl" x="280" y="228">x</text>
    <text class="pm-lbl" x="130" y="32">y</text>
    <text class="pm-lbl pm-lbl--hl" x="218" y="52">y = x + 2</text>
  </svg>
  <figcaption>Oltita nuqta bitta toʻgʻri chiziqda yotdi — shuning uchun ularni
  chiziq bilan tutashtiramiz.</figcaption>
</figure>

<h3>4. Uchinchi qadam — chiziq</h3>

<p>Nuqtalar bir chiziqda yotgani koʻrinib turibdi. Chizgʻich bilan ularni
tutashtiramiz va ikki tomonga davom ettiramiz.</p>

<p>Nega davom ettiriladi? Chunki jadvalga faqat oltita x tushdi, funksiya esa
<b>hamma</b> sonni qabul qiladi. Masalan x = 1,5 boʻlsa, y = 3,5 — bu nuqta ham
oʻsha chiziqda yotadi.</p>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Chiziq — cheksiz koʻp nuqta</p>
  <p>Grafikdagi chiziq — bu chizilgan oltita nuqta emas, ular orasidagi va
  ulardan naridagi <b>barcha</b> nuqtalar. Shuning uchun grafik jadvaldan
  kuchliroq: jadvalda oltita javob bor, grafikda esa cheksiz koʻp.</p>
</div>

<h3>5. Grafikdan qiymat oʻqish</h3>

<p>Grafik chizilgach, hisoblash shart emas — oʻqib olsa boʻladi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = 2 da y ni topamiz</span>
    <span class="pm-solve__why">Savol: kirish 2 boʻlsa, chiqish qancha?</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x oʻqida 2 ni topib, tik yuqoriga yuramiz</span>
    <span class="pm-solve__why">Chiziqqa yetguncha</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Chapga burilib, y oʻqida 4 ni oʻqiymiz</span>
    <span class="pm-solve__why">Demak y = 4</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Formula bilan: y = 2 + 2 = 4 ✓ Grafik va formula bir xil javob berdi.
  <b>Har doim shunday boʻlishi kerak</b> — grafik formulaning rasmi, xolos.</p>
</div>

<p>Teskarisi ham ishlaydi: y = 1 boʻlgan x ni topish uchun y oʻqida 1 dan oʻngga
yurib, chiziqqa yetamiz va pastga tushamiz — x = −1.</p>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Shkalaga qarang</p>
  <p>Eng koʻp uchraydigan xato — har bir katakni 1 birlik deb oʻylash. Real
  grafiklarda bitta katak 5, 10 yoki 1000 birlik boʻlishi mumkin. Grafikni
  oʻqishdan oldin <b>doim oʻqlardagi sonlarga qarang</b> va bir katak necha
  birlik ekanini aniqlab oling.</p>
</div>

<h3>6. Har doim ham chiziq chizilmaydi</h3>

<p>Bitta muhim shart bor. Nuqtalarni faqat <b>oraliq qiymatlar maʼnoga ega
boʻlganda</b> tutashtiramiz.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Chiziq mumkin</p>
    <p>Harorat, masofa, vaqt, suv miqdori. Yarim daqiqa ham, 2,7 litr ham
    bor.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Faqat nuqtalar</p>
    <p>Daftarlar soni, oʻquvchilar soni, chiptalar soni. Yarim daftar
    boʻlmaydi.</p>
  </div>
</div>

<figure class="pm-fig">
  <svg viewBox="0 0 300 220" role="img" aria-label="Daftarlar soni va narx — faqat nuqtalar">
    <line class="pm-ln" x1="40" y1="180" x2="285" y2="180"/>
    <line class="pm-ln" x1="50" y1="196" x2="50" y2="20"/>
    <circle class="pm-pt" cx="90" cy="150" r="4"/>
    <circle class="pm-pt" cx="130" cy="120" r="4"/>
    <circle class="pm-pt" cx="170" cy="90" r="4"/>
    <circle class="pm-pt" cx="210" cy="60" r="4"/>
    <circle class="pm-pt" cx="250" cy="30" r="4"/>
    <text class="pm-lbl" x="90" y="196" text-anchor="middle">1</text>
    <text class="pm-lbl" x="130" y="196" text-anchor="middle">2</text>
    <text class="pm-lbl" x="170" y="196" text-anchor="middle">3</text>
    <text class="pm-lbl" x="210" y="196" text-anchor="middle">4</text>
    <text class="pm-lbl" x="250" y="196" text-anchor="middle">5</text>
    <text class="pm-lbl" x="44" y="154" text-anchor="end">6</text>
    <text class="pm-lbl" x="44" y="94" text-anchor="end">18</text>
    <text class="pm-lbl" x="44" y="34" text-anchor="end">30</text>
    <text class="pm-lbl" x="150" y="214" text-anchor="middle">daftarlar soni</text>
    <text class="pm-lbl" x="60" y="18">ming soʻm</text>
  </svg>
  <figcaption>Bitta daftar 6 000 soʻm. Nuqtalar bogʻlanmagan — chunki 2,5 ta
  daftar sotib boʻlmaydi.</figcaption>
</figure>

<h3>Matnli masala</h3>

<p><b>Suv baki.</b> Bakda boshida <b>5 litr</b> suv bor edi. Jomrat ochildi va bak
har daqiqada <b>3 litr</b>dan toʻla boshladi.</p>

<p><b>Savol:</b> jadval tuzing, grafikning shakli qanday boʻladi va bakda 26 litr
suv boʻlishi uchun necha daqiqa kerak?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x — daqiqalar, y — litrlar</span>
    <span class="pm-solve__why">Kirish va chiqishni aniqladik (PM-47)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">y = 3x + 5</span>
    <span class="pm-solve__why">Boshidagi 5 litr va har daqiqada 3 litr</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">0 → 5; 1 → 8; 2 → 11; 3 → 14; 4 → 17; 5 → 20</span>
    <span class="pm-solve__why">Qiymatlar jadvali</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x + 5 = 26 → 3x = 21</span>
    <span class="pm-solve__why">Teskari savol — tenglama (PM-36)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 7 daqiqa</span>
    <span class="pm-solve__why">Yettinchi daqiqada bakda 26 litr boʻladi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>3 × 7 + 5 = 21 + 5 = 26 ✓ Jadvaldagi qadam ham buni tasdiqlaydi: har
  daqiqada y aynan 3 birlikka oʻsyapti (5, 8, 11, 14…) — demak nuqtalar bir
  toʻgʻri chiziqda yotadi. Suv uzluksiz oqadi, shuning uchun bu yerda nuqtalarni
  chiziq bilan tutashtirsa <b>boʻladi</b>.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Boshidagi 5 litrni hisobga olmasak, 26 ÷ 3 ≈ 8,7 daqiqa chiqadi. Demak
  javob 8,7 dan kichik boʻlishi kerak. 7 — mos.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Jadvalda x = 2, y = 5 → nuqta (5; 2) ga qoʻyildi</p>
  <p class="pe-fix__good">Nuqta (2; 5) ga qoʻyiladi</p>
  <p class="pe-fix__why">Grafikda gorizontal yoʻnalish — <b>doim</b> kirish (x),
  vertikal — chiqish (y). Jadvalning yuqori qatori x oʻqiga tushadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Sotilgan chiptalar soni nuqtalari chiziq bilan
    tutashtirildi</p>
  <p class="pe-fix__good">Nuqtalar shundayligicha qoldiriladi</p>
  <p class="pe-fix__why">Chiziq «orada ham qiymat bor» deganini bildiradi. 2,5 ta
  chipta esa yoʻq — demak chiziq yolgʻon gapirgan boʻlardi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Har katak 5 birlik boʻlgan grafikda 3 katak = 3 birlik</p>
  <p class="pe-fix__good">3 katak = 15 birlik</p>
  <p class="pe-fix__why">Shkala oʻqilmagan. Grafikni oʻqishdan oldin oʻqdagi
  sonlarga qarab, bitta katakning qiymatini aniqlang.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. y = x − 3 funksiyasi uchun x = 0, 1, 2, 3 da jadval
  tuzing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>−3, −2, −1, 0.</b> Har safar x dan 3 ayriladi. Nuqtalar: (0; −3),
    (1; −2), (2; −1), (3; 0).</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. (2; 7) nuqtasi y = 3x + 1 grafigida yotadimi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Ha.</b> 3 × 2 + 1 = 7 ✓ Nuqta grafikda yotishini tekshirish — uning
    koordinatalarini formulaga qoʻyib koʻrish demakdir.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. y = 5 − x grafigi Oy oʻqini qaysi nuqtada kesadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>(0; 5).</b> Oy oʻqida abssissa nol (PM-45), demak x = 0 qoʻyamiz:
    y = 5 − 0 = 5.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Quyidagi maʼlumotlardan qaysi birining nuqtalarini
  chiziq bilan bogʻlash mumkin emas: (a) kun davomidagi harorat, (b) sotilgan
  chiptalar soni, (c) bosib oʻtilgan masofa?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>(b) sotilgan chiptalar soni.</b> Chipta butun sonda sanaladi — 2,5 ta
    chipta yoʻq. Harorat ham, masofa ham uzluksiz oʻzgaradi, ular chiziq bilan
    bogʻlanadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Shamning uzunligi boshida 20 sm edi va u har soatda
  4 sm dan qisqaradi. Jadval tuzing va shamning butunlay yonib bitishiga necha
  soat kerakligini toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5 soat.</b> Qoida: y = 20 − 4x. Jadval: 0 → 20; 1 → 16; 2 → 12;
    3 → 8; 4 → 4; 5 → 0. Grafik pastga tushuvchi toʻgʻri chiziq boʻladi.
    Tekshirish: 20 − 4 × 5 = 0 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Grafik</b><span>funksiyaning barcha (x; y) nuqtalari; ingl.
    graph</span></li>
  <li><b>Qiymatlar jadvali</b><span>x va y juftliklari roʻyxati; ingl. table of
    values</span></li>
  <li><b>Nuqtani qoʻyish</b><span>juftlikni tekislikda belgilash; ingl.
    plotting</span></li>
  <li><b>Shkala</b><span>bitta katakning qiymati; ingl. scale</span></li>
  <li><b>Uzluksiz miqdor</b><span>oraliq qiymatlari ham bor (vaqt, suv); ingl.
    continuous</span></li>
  <li><b>Diskret miqdor</b><span>faqat butun sonlarda (chipta, daftar); ingl.
    discrete</span></li>
  <li><b>Oʻqni kesish nuqtasi</b><span>grafikning oʻq bilan uchrashgan joyi;
    ingl. intercept</span></li>
  <li><b>Kirish va chiqish</b><span>x va y, gorizontal va vertikal; ingl. input
    and output</span></li>
  <li><b>Toʻgʻri chiziq</b><span>bir tekis oʻsuvchi grafik shakli; ingl. straight
    line</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Jadval → nuqtalar → chiziq.</b> Uchta qadam, har doim shu tartibda.</li>
    <li><b>Grafik jadvaldan boy:</b> unda oraliqdagi qiymatlar ham bor.</li>
    <li><b>Shkalani oʻqing va chiziqni oʻrinli chizing</b> — diskret maʼlumot
      nuqtaligicha qoladi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-49 — chiziqli funksiya y = kx + b
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-49: Chiziqli funksiya y = kx + b",
        "category": "math",
        "order": 49,
        "summary": (
            "Grafigi toʻgʻri chiziq boʻlgan funksiya: b — boshlangʻich qiymat va "
            "Oy oʻqining kesilish nuqtasi, k — har bir qadamdagi oʻzgarish. "
            "Chiziqni ikki nuqtada chizish."
        ),
        "stories": ["Taksi hisobi grafikda"],
        "content": """
<h2>PM-49: Chiziqli funksiya y = kx + b</h2>

<p>PM-48 dagi hamma misolimizda nuqtalar bitta toʻgʻri chiziqda yotdi. Bu
tasodif emas edi. Ularning formulasi bir xil qolipda edi: <b>bitta son x ga
koʻpaytiriladi, ustiga yana bitta son qoʻshiladi</b>.</p>

<p>Shunday funksiya <b>chiziqli funksiya</b> deyiladi va uning grafigi har doim
toʻgʻri chiziq boʻladi. Butun matematikadagi eng koʻp ishlatiladigan qolip —
taksi hisobidan tortib ish haqigacha.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>y = kx + b qolipini tanib olasiz;</li>
    <li>k va b ni formuladan ajratasiz (ishorasi bilan);</li>
    <li>chiziqni ikki nuqta yordamida chizasiz;</li>
    <li>b dan boshlab k boʻyicha yurib grafik qurasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Chiziqli funksiya</span>
  <span class="pe-chip pe-chip--o">y</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">k</span>
  <span class="pe-chip pe-chip--s">x</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">b</span>
</div>

<h3>1. b — boshlangʻich qiymat</h3>

<p>x = 0 qoʻyib koʻring: y = k × 0 + b = <b>b</b>. Demak b — funksiyaning
<b>hech narsa boʻlmasdan turibgi</b> qiymati.</p>

<p>Grafikda esa bu Oy oʻqining kesilish nuqtasi: chiziq har doim <b>(0; b)</b>
nuqtasidan oʻtadi.</p>

<div class="pe-ex">
  <p class="pe-ex__math">y = 2x + 1 → b = 1, chiziq (0; 1) dan oʻtadi</p>
  <p class="pe-ex__uz">Boshlangʻich qiymat — bir.</p>
  <p class="pe-ex__why">x = 0 da faqat qoʻshiluvchi qoladi.</p>
</div>

<h3>2. k — qadam</h3>

<p>Endi x ni bir birlikka oshiramiz va y ga nima boʻlishini koʻramiz.</p>

<div class="pe-table-wrap"><table>
  <tr><th>x</th><td>0</td><td>1</td><td>2</td><td>3</td></tr>
  <tr><th>y = 2x + 1</th><td>1</td><td>3</td><td>5</td><td>7</td></tr>
  <tr><th>oʻzgarish</th><td>—</td><td>+2</td><td>+2</td><td>+2</td></tr>
</table></div>

<p>Har safar y aynan <b>2</b> ga oʻsdi — bu k ning oʻzi. Demak:</p>

<div class="pe-call pe-rule">
  <p class="pe-call__t">k nimani aytadi</p>
  <p><b>x bir birlikka oshganda y k birlikka oʻzgaradi.</b> k musbat boʻlsa y
  oʻsadi (chiziq koʻtariladi), manfiy boʻlsa kamayadi (chiziq tushadi), nolga
  teng boʻlsa umuman oʻzgarmaydi (chiziq gorizontal).</p>
</div>

<figure class="pm-fig">
  <svg viewBox="0 0 280 240" role="img" aria-label="y = 2x + 1 grafigi, b va k koʻrsatilgan">
    <line class="pm-ln pm-ln--dash" x1="50" y1="30" x2="50" y2="212"/>
    <line class="pm-ln pm-ln--dash" x1="130" y1="30" x2="130" y2="212"/>
    <line class="pm-ln pm-ln--dash" x1="170" y1="30" x2="170" y2="212"/>
    <line class="pm-ln pm-ln--dash" x1="210" y1="30" x2="210" y2="212"/>
    <line class="pm-ln" x1="30" y1="190" x2="262" y2="190"/>
    <line class="pm-ln" x1="90" y1="225" x2="90" y2="22"/>
    <line class="pm-ln pm-ln--hl" x1="50" y1="212" x2="210" y2="36"/>
    <line class="pm-ln pm-ln--dash" x1="90" y1="168" x2="130" y2="168"/>
    <line class="pm-ln pm-ln--dash" x1="130" y1="168" x2="130" y2="124"/>
    <circle class="pm-pt" cx="90" cy="168" r="5"/>
    <circle class="pm-pt" cx="130" cy="124" r="4"/>
    <circle class="pm-pt" cx="170" cy="80" r="4"/>
    <circle class="pm-pt" cx="210" cy="36" r="4"/>
    <text class="pm-lbl pm-lbl--hl" x="84" y="164" text-anchor="end">b = 1</text>
    <text class="pm-lbl" x="110" y="184" text-anchor="middle">1</text>
    <text class="pm-lbl pm-lbl--hl" x="136" y="150">k = 2</text>
    <text class="pm-lbl" x="130" y="206" text-anchor="middle">1</text>
    <text class="pm-lbl" x="210" y="206" text-anchor="middle">3</text>
    <text class="pm-lbl" x="82" y="206" text-anchor="end">O</text>
    <text class="pm-lbl" x="252" y="208">x</text>
    <text class="pm-lbl" x="100" y="32">y</text>
  </svg>
  <figcaption>(0; 1) dan boshlaymiz. Bir katak oʻngga, ikki katak yuqoriga —
  yangi nuqta. Shuni takrorlab, butun chiziqni chiqaramiz.</figcaption>
</figure>

<h3>3. Chiziqni chizishning ikki usuli</h3>

<p><b>Birinchi usul — ikki nuqta.</b> Toʻgʻri chiziqni ikkita nuqta toʻliq
belgilaydi. Ikkita qulay x tanlang, y ni hisoblang, chizgʻich qoʻying. Uchinchi
nuqtani tekshirish uchun olish — yaxshi odat.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">y = −3x + 6</span>
    <span class="pm-solve__why">Berilgan funksiya</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = 0 → y = 6</span>
    <span class="pm-solve__why">Birinchi nuqta: (0; 6)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = 2 → y = −6 + 6 = 0</span>
    <span class="pm-solve__why">Ikkinchi nuqta: (2; 0)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">(0; 6) va (2; 0) orqali chiziq</span>
    <span class="pm-solve__why">Tekshiruv: x = 1 → 3, chindan ham oʻrtada</span>
  </div>
</div>

<p><b>Ikkinchi usul — b dan boshlab k boʻyicha yurish.</b> (0; b) ni qoʻying,
soʻng bir katak oʻngga va k katak yuqoriga (k manfiy boʻlsa — pastga) yuring.
Chizmadagi zinapoya aynan shu.</p>

<div class="pe-call pe-uz">
  <p class="pe-call__t">b ni ishorasi bilan oling</p>
  <p>y = 4x <b>−</b> 6 da b = <b>−6</b>, 6 emas. Qolipda qoʻshuv turibdi
  (kx <b>+</b> b), demak minusni ham b ning oʻziga qoʻshib olasiz. Xuddi
  shunday, y = <b>−</b>3x + 6 da k = −3.</p>
</div>

<h3>4. k va b nolga teng boʻlsa</h3>

<div class="pe-table-wrap"><table>
  <tr><th>Holat</th><th>Misol</th><th>Grafik</th></tr>
  <tr><td>b = 0</td><td>y = 2x</td><td>Koordinata boshidan oʻtadi</td></tr>
  <tr><td>k = 0</td><td>y = 5</td><td>Gorizontal chiziq</td></tr>
  <tr><td>k &gt; 0</td><td>y = x + 1</td><td>Oʻngga qarab koʻtariladi</td></tr>
  <tr><td>k &lt; 0</td><td>y = −x + 1</td><td>Oʻngga qarab tushadi</td></tr>
</table></div>

<figure class="pm-fig">
  <svg viewBox="0 0 280 220" role="img" aria-label="k musbat, manfiy va nolga teng boʻlgan uchta chiziq">
    <line class="pm-ln" x1="20" y1="110" x2="266" y2="110"/>
    <line class="pm-ln" x1="140" y1="205" x2="140" y2="20"/>
    <line class="pm-ln pm-ln--hl" x1="40" y1="185" x2="190" y2="35"/>
    <line class="pm-ln" x1="90" y1="35" x2="240" y2="185"/>
    <line class="pm-ln pm-ln--dash" x1="40" y1="85" x2="240" y2="85"/>
    <circle class="pm-pt" cx="140" cy="85" r="4"/>
    <text class="pm-lbl pm-lbl--hl" x="196" y="34">k &gt; 0</text>
    <text class="pm-lbl" x="246" y="188">k &lt; 0</text>
    <text class="pm-lbl" x="246" y="80">k = 0</text>
    <text class="pm-lbl" x="134" y="80" text-anchor="end">b</text>
    <text class="pm-lbl" x="258" y="128">x</text>
    <text class="pm-lbl" x="150" y="30">y</text>
  </svg>
  <figcaption>Uchala chiziq ham (0; b) dan oʻtadi — farq faqat k da.</figcaption>
</figure>

<h3>Matnli masala</h3>

<p><b>Taksi hisobi.</b> Taksiga oʻtirganingizda hisoblagich darrov
<b>8 000 soʻm</b>ni koʻrsatadi — bu oʻtirish haqi. Keyin har bir kilometr uchun
<b>3 000 soʻm</b> qoʻshiladi.</p>

<p><b>Savol:</b> narxni chiziqli funksiya koʻrinishida yozing. 12 km yoʻl qancha
turadi? Bekzod 29 000 soʻm toʻlagan boʻlsa, u necha kilometr yurgan?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x — kilometrlar, y — narx</span>
    <span class="pm-solve__why">Kirish va chiqish</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">y = 3 000x + 8 000</span>
    <span class="pm-solve__why">k = 3 000 (har km), b = 8 000 (oʻtirish
      haqi)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">y = 3 000 × 12 + 8 000 = 44 000</span>
    <span class="pm-solve__why">12 km — 44 000 soʻm</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 000x + 8 000 = 29 000 → 3 000x = 21 000</span>
    <span class="pm-solve__why">Teskari savol — tenglama (PM-36)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 7 km</span>
    <span class="pm-solve__why">Bekzod 7 kilometr yurgan</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>3 000 × 7 + 8 000 = 21 000 + 8 000 = 29 000 ✓ Grafik nuqtai nazaridan:
  chiziq (0; 8 000) dan boshlanadi va har kilometrda 3 000 ga koʻtariladi.
  <b>Chiziq nolda emas, 8 000 da boshlanishi</b> — oʻtirish haqining oʻzi.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Oʻtirish haqisiz 29 000 ÷ 3 000 ≈ 9,7 km chiqardi. Oʻtirish haqi bor
  ekan, javob undan kichik boʻlishi shart. 7 — mos.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">y = 4x − 6 da b = 6</p>
  <p class="pe-fix__good">b = −6</p>
  <p class="pe-fix__why">Qolip y = kx + b, yaʼni qoʻshuv. Ayirish turgan
  boʻlsa, minus b ning oʻziga tegishli: 4x + (−6).</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">y = 2x + 3 grafigi (0; 2) dan boshlanadi</p>
  <p class="pe-fix__good">(0; 3) dan boshlanadi</p>
  <p class="pe-fix__why">Oy oʻqini kesish nuqtasini <b>b</b> beradi, k emas. k —
  bu qiyalik, boshlanish emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">y = 5x + 2 va y = 2x + 5 — bir xil chiziq</p>
  <p class="pe-fix__good">Ular butunlay boshqa ikki chiziq</p>
  <p class="pe-fix__why">Birinchisining qadami 5, boshlanishi 2; ikkinchisiniki
  aksincha. x = 1 da: 7 va 7 — bir xil; x = 2 da esa 12 va 9 — allaqachon har
  xil.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. y = 3x + 5 da k va b nechaga teng?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>k = 3, b = 5.</b> Har qadamda y uch birlikka oʻsadi, chiziq (0; 5)
    dan oʻtadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. y = −2x + 7 grafigi Oy oʻqini qayerda kesadi va u
  koʻtariladimi yoki tushadimi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>(0; 7) da kesadi va tushadi.</b> b = 7 — boshlangʻich qiymat;
    k = −2 manfiy, demak har qadamda y ikki birlikka kamayadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Chiziq (0; −4) da Oy oʻqini kesadi va har qadamda
  3 birlikka koʻtariladi. Formulasini yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>y = 3x − 4.</b> Qadam — k = 3, boshlanish — b = −4. Tekshirish:
    x = 2 da y = 6 − 4 = 2.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. y = 2x + 6 grafigi Ox oʻqini qaysi nuqtada kesadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>(−3; 0).</b> Ox oʻqida ordinata nol (PM-45), demak y = 0 qoʻyamiz:
    2x + 6 = 0 → 2x = −6 → x = −3.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Sport zali obunasi oyiga 90 000 soʻm, ustiga har bir
  mashgʻulot 6 000 soʻm. Chiziqli funksiyani yozing, 15 marta borgan Afsona
  qancha toʻlashini toping va 210 000 soʻm toʻlagan odam necha marta
  borganini hisoblang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>y = 6 000x + 90 000; Afsona 180 000 soʻm; ikkinchisi 20 marta.</b>
    k = 6 000, b = 90 000. 6 000 × 15 + 90 000 = 90 000 + 90 000 = 180 000.
    Teskari savol: 6 000x = 210 000 − 90 000 = 120 000 → x = 20. Tekshirish:
    90 000 + 120 000 = 210 000 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Chiziqli funksiya</b><span>grafigi toʻgʻri chiziq boʻlgan funksiya;
    ingl. linear function</span></li>
  <li><b>k — burchak koeffitsienti</b><span>har qadamdagi oʻzgarish, qiyalik;
    ingl. slope</span></li>
  <li><b>b — ozod had</b><span>boshlangʻich qiymat, x = 0 dagi y; ingl.
    y-intercept</span></li>
  <li><b>Qiyalik</b><span>chiziqning tikligi; ingl. gradient</span></li>
  <li><b>Oy oʻqini kesish</b><span>(0; b) nuqtasi; ingl. y-intercept</span></li>
  <li><b>Ox oʻqini kesish</b><span>y = 0 boʻlgan nuqta; ingl.
    x-intercept</span></li>
  <li><b>Oʻsuvchi funksiya</b><span>k musbat boʻlgani; ingl. increasing</span></li>
  <li><b>Kamayuvchi funksiya</b><span>k manfiy boʻlgani; ingl.
    decreasing</span></li>
  <li><b>Gorizontal chiziq</b><span>k = 0 boʻlgan grafik; ingl. horizontal
    line</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>y = kx + b ning grafigi — har doim toʻgʻri chiziq.</b></li>
    <li><b>b — qayerdan boshlanadi, k — qanchadan yuradi.</b></li>
    <li><b>Ikki nuqta yetarli</b> — uchinchisi faqat tekshirish uchun.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-50 — k va b ning real maʼnosi
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-50: k va b nimani bildiradi — grafikning real maʼnosi",
        "category": "math",
        "order": 50,
        "summary": (
            "k — bir birlik uchun qancha (tarif, tezlik, sarf), b — hech narsa "
            "qilmasdan turibgi qiymat. Ikki chiziqni taqqoslash va parallel "
            "chiziqlarning maʼnosi."
        ),
        "stories": ["Ikki tarif, ikki chiziq"],
        "content": """
<h2>PM-50: k va b nimani bildiradi — grafikning real maʼnosi</h2>

<p>PM-49 da k va b ni formuladan ajratishni oʻrgandik. Endi eng qiziq savol:
<b>ular hayotda nimani anglatadi?</b></p>

<p>Javobi qisqa. <b>b</b> — hech narsa qilmasdan turib toʻlanadigan yoki mavjud
boʻlgan miqdor. <b>k</b> — har bir qoʻshimcha birlik uchun qancha qoʻshiladi
(yoki ayriladi). Shu ikki soʻzni bilsangiz, har qanday tarifni bir qarashda
oʻqiysiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>k va b ni real vaziyatning soʻzlariga tarjima qilasiz;</li>
    <li>kamayuvchi jarayonni manfiy k bilan yozasiz;</li>
    <li>ikki chiziqni taqqoslaysiz va parallel boʻlishining maʼnosini
      aytasiz;</li>
    <li>grafikning shakliga qarab vaziyatni tasvirlaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Tarjima</span>
  <span class="pe-chip pe-chip--aux">b = boshida qancha</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">k = har birlik uchun qancha</span>
</div>

<h3>1. Soʻzdan formulaga, formuladan soʻzga</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Vaziyat</th><th>Formula</th><th>k va b nimani bildiradi</th></tr>
  <tr><td>Taksi: oʻtirish 8 000, har km 3 000</td>
      <td class="pm-word__sym">y = 3 000x + 8 000</td>
      <td>b — oʻtirish haqi, k — kilometr narxi</td></tr>
  <tr><td>Ish haqi: 1 200 000 doimiy, har mahsulot 15 000</td>
      <td class="pm-word__sym">y = 15 000x + 1 200 000</td>
      <td>b — oylik maosh, k — mukofot</td></tr>
  <tr><td>Bakda 200 litr, har soatda 25 litr sarflanadi</td>
      <td class="pm-word__sym">y = −25x + 200</td>
      <td>b — boshidagi suv, k — sarf (manfiy!)</td></tr>
  <tr><td>Yoʻlovchi 60 km/soat tezlikda ketyapti</td>
      <td class="pm-word__sym">y = 60x</td>
      <td>b = 0 — noldan boshlagan, k — tezlik</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Kamayish — manfiy k</p>
  <p>«Har soatda 25 litr kamayadi» degani k = <b>−25</b> demakdir. Grafik oʻngga
  qarab tushadi. Miqdor kamayishi — bu «minus», sonning oʻzi emas: 25 litr
  hamon 25 litr, faqat u <b>ketyapti</b>.</p>
</div>

<h3>2. Kamayuvchi chiziq — bak misoli</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">y = 200 − 25x</span>
    <span class="pm-solve__why">b = 200 litr, k = −25 litr/soat</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = 5 → 200 − 125 = 75</span>
    <span class="pm-solve__why">Besh soatdan keyin 75 litr qolgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">200 − 25x = 0 → 25x = 200</span>
    <span class="pm-solve__why">«Bak qachon boʻshaydi?» — tenglama</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 8 soat</span>
    <span class="pm-solve__why">Sakkizinchi soatda bak boʻshaydi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>200 − 25 × 8 = 200 − 200 = 0 ✓ Grafik (0; 200) dan boshlanib, (8; 0) da Ox
  oʻqiga tegadi. <b>Ox oʻqini kesish nuqtasi bu masalada «bak boʻshadi» degani</b>
  — grafikning har bir joyi vaziyatda oʻz maʼnosiga ega.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Grafikning davomi maʼnosizmi?</p>
  <p>Formula boʻyicha x = 10 da y = −50 chiqadi. Lekin bakda −50 litr suv
  boʻlmaydi! Real masalalarda grafikning <b>maʼnoli qismi</b> chegaralangan: bu
  yerda 0 dan 8 soatgacha. Formulaga koʻr-koʻrona ishonmang — javobning
  vaziyatga mos kelishini har doim tekshiring.</p>
</div>

<h3>3. Ikki chiziqni taqqoslash</h3>

<p>Telefon operatorida ikkita tarif bor:</p>

<ul>
  <li><b>A tarif:</b> abonent haqi 20 000 soʻm, daqiqasi 200 soʻm →
    y = 200x + 20 000</li>
  <li><b>B tarif:</b> abonent haqi 50 000 soʻm, daqiqasi 100 soʻm →
    y = 100x + 50 000</li>
</ul>

<div class="pe-table-wrap"><table>
  <tr><th>Daqiqa</th><td>100</td><td>200</td><td>300</td><td>400</td><td>500</td></tr>
  <tr><th>A tarif</th><td>40 000</td><td>60 000</td><td>80 000</td><td>100 000</td><td>120 000</td></tr>
  <tr><th>B tarif</th><td>60 000</td><td>70 000</td><td>80 000</td><td>90 000</td><td>100 000</td></tr>
</table></div>

<figure class="pm-fig">
  <svg viewBox="0 0 320 240" role="img" aria-label="Ikki tarifning grafigi va ularning kesishishi">
    <line class="pm-ln pm-ln--dash" x1="194" y1="30" x2="194" y2="200"/>
    <line class="pm-ln pm-ln--dash" x1="50" y1="88" x2="194" y2="88"/>
    <line class="pm-ln" x1="40" y1="200" x2="305" y2="200"/>
    <line class="pm-ln" x1="50" y1="215" x2="50" y2="20"/>
    <line class="pm-ln pm-ln--hl" x1="50" y1="172" x2="290" y2="32"/>
    <line class="pm-ln" x1="50" y1="130" x2="290" y2="60"/>
    <circle class="pm-pt" cx="194" cy="88" r="5"/>
    <text class="pm-lbl pm-lbl--hl" x="286" y="26" text-anchor="end">A tarif</text>
    <text class="pm-lbl" x="286" y="78" text-anchor="end">B tarif</text>
    <text class="pm-lbl" x="44" y="176" text-anchor="end">20</text>
    <text class="pm-lbl" x="44" y="134" text-anchor="end">50</text>
    <text class="pm-lbl" x="44" y="92" text-anchor="end">80</text>
    <text class="pm-lbl" x="194" y="216" text-anchor="middle">300</text>
    <text class="pm-lbl" x="290" y="216" text-anchor="middle">500</text>
    <text class="pm-lbl" x="150" y="234" text-anchor="middle">daqiqa</text>
    <text class="pm-lbl" x="58" y="18">ming soʻm</text>
  </svg>
  <figcaption>A tarif pastdan boshlanadi, lekin tikroq koʻtariladi. 300 daqiqada
  ikkalasi ham 80 000 soʻm boʻladi.</figcaption>
</figure>

<p>Jadval hammasini aytib turibdi. <b>Kam gaplashadiganga A foydali</b> (past b),
<b>koʻp gaplashadiganga B</b> (kichik k). 300 daqiqada esa ikkalasi teng.</p>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Kesishgan nuqtani hisoblab topish</p>
  <p>Biz uni jadvaldan koʻrdik, chunki 300 — yumaloq son. Har doim ham shunday
  boʻlavermaydi. Ikki chiziqning kesishgan nuqtasini <b>hisoblab</b> topish
  usulini <b>PM-52</b> darsida oʻrganamiz — u yerda bu «sistema» deb ataladi.</p>
</div>

<h3>4. Parallel chiziqlar</h3>

<p>Ikki chiziqning k si bir xil boʻlsa, ular <b>hech qachon kesishmaydi</b> —
parallel boʻladi. Chunki ikkalasi ham bir xil tiklikda koʻtariladi, faqat biri
doim ikkinchisidan yuqorida turadi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 260 220" role="img" aria-label="Bir xil k, har xil b: ikkita parallel chiziq">
    <line class="pm-ln" x1="30" y1="190" x2="240" y2="190"/>
    <line class="pm-ln" x1="60" y1="205" x2="60" y2="15"/>
    <line class="pm-ln pm-ln--hl" x1="60" y1="170" x2="220" y2="10"/>
    <line class="pm-ln" x1="60" y1="110" x2="160" y2="10"/>
    <circle class="pm-pt" cx="60" cy="170" r="4"/>
    <circle class="pm-pt" cx="60" cy="110" r="4"/>
    <text class="pm-lbl" x="54" y="174" text-anchor="end">1</text>
    <text class="pm-lbl" x="54" y="114" text-anchor="end">4</text>
    <text class="pm-lbl pm-lbl--hl" x="224" y="24">y = 2x + 1</text>
    <text class="pm-lbl" x="164" y="24">y = 2x + 4</text>
    <text class="pm-lbl" x="232" y="208">x</text>
    <text class="pm-lbl" x="70" y="22">y</text>
  </svg>
  <figcaption>k bir xil (2), b har xil (1 va 4) — chiziqlar parallel. Real
  maʼnosi: bir xil tarif, boshlangʻich haqi har xil.</figcaption>
</figure>

<div class="pe-call pe-uz">
  <p class="pe-call__t">«k katta — chiziq yuqorida» degani emas</p>
  <p>Koʻpchilik k katta boʻlsa chiziq hamma joyda yuqorida turadi deb oʻylaydi.
  Bu notoʻgʻri: yuqoridagi tariflarda A ning k si kattaroq, lekin 100 daqiqada
  A <b>arzonroq</b>. <b>k tiklikni, b esa boshlanishni belgilaydi</b> — kim
  yuqorida ekani qaysi x da qaraganingizga bogʻliq.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Sherbekning ish haqi.</b> Sherbek doʻkonga ishga kirdi. Shartnomaga koʻra u
oyiga <b>1 200 000 soʻm</b> doimiy maosh oladi, ustiga har bir sotilgan mahsulot
uchun <b>15 000 soʻm</b> mukofot beriladi.</p>

<p><b>Savol:</b> k va b nimani bildiradi? 40 ta mahsulot sotsa qancha oladi? Va
2 100 000 soʻm olish uchun nechta sotishi kerak?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">y = 15 000x + 1 200 000</span>
    <span class="pm-solve__why">x — sotilgan mahsulotlar soni</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">b = 1 200 000 — hech nima sotmasa ham oladi</span>
    <span class="pm-solve__why">Grafikning boshlanish nuqtasi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">k = 15 000 — har bir mahsulot qoʻshadigan pul</span>
    <span class="pm-solve__why">Chiziqning qiyaligi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = 40 → 600 000 + 1 200 000 = 1 800 000</span>
    <span class="pm-solve__why">Qirq mahsulotda 1 800 000 soʻm</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">15 000x = 900 000 → x = 60</span>
    <span class="pm-solve__why">2 100 000 uchun 60 ta mahsulot</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>15 000 × 60 + 1 200 000 = 900 000 + 1 200 000 = 2 100 000 ✓ Eʼtibor bering:
  bu masalada x — <b>diskret</b> miqdor (59,5 ta mahsulot sotilmaydi), shuning
  uchun grafik chizsangiz nuqtalar bogʻlanmaydi (PM-48).</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Doimiy maoshdan tashqari 900 000 soʻm kerak. Har biri 15 000 dan —
  taxminan 900 000 ÷ 15 000 = 60. Aniq javob ham shu.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">«Har soatda 25 litr kamayadi» → y = 25x + 200</p>
  <p class="pe-fix__good">y = −25x + 200</p>
  <p class="pe-fix__why">Kamayish manfiy k bilan yoziladi. Musbat k bilan bak
  toʻlib borardi — masalaning teskarisi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">k kattaroq boʻlgan tarif hamma vaqt qimmat</p>
  <p class="pe-fix__good">Kichik x larda kichik b li tarif arzonroq boʻlishi
    mumkin</p>
  <p class="pe-fix__why">100 daqiqada A tarif (k = 200) 40 000, B tarif
  (k = 100) esa 60 000 soʻm. b ni unutmang.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Bak masalasida x = 10 → y = −50 litr</p>
  <p class="pe-fix__good">Bak 8-soatda boʻshaydi; undan keyin formula
    ishlamaydi</p>
  <p class="pe-fix__why">Real masalada grafikning faqat maʼnoli qismi ishlaydi.
  Manfiy suv miqdori boʻlmaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. y = 2 000x + 5 000 formulasida x — soatlar soni.
  5 000 nimani bildiradi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Boshlangʻich, oʻzgarmas haq</b> — birinchi soat boshlanmasdan turib
    ham toʻlanadigan pul. 2 000 esa har bir soat uchun qoʻshiladigan miqdor.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Bakda 200 litr suv bor, har soatda 25 litr
  sarflanadi. 6 soatdan keyin qancha qoladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>50 litr.</b> y = 200 − 25x; 200 − 25 × 6 = 200 − 150 = 50.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Ikki chiziqning k si bir xil, b si har xil. Ular
  qanday joylashgan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Parallel — hech qachon kesishmaydi.</b> Bir xil tiklikda
    koʻtariladi, faqat biri doim ikkinchisidan yuqorida turadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. A tarifda 250 daqiqa gaplashish qancha turadi
  (y = 200x + 20 000)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>70 000 soʻm.</b> 200 × 250 = 50 000, ustiga abonent haqi 20 000:
    jami 70 000.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Ikki usta devor suvaydi. Karim aka kelgani uchun
  40 000 soʻm oladi va har kvadrat metr uchun 30 000 soʻm. Anvar aka kelish haqi
  olmaydi, lekin har kvadrat metr uchun 35 000 soʻm soʻraydi. 10 m² devor uchun
  kim arzon va qancha farq bilan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Karim aka arzon, 10 000 soʻm farq bilan.</b> Karim aka:
    30 000 × 10 + 40 000 = 300 000 + 40 000 = 340 000. Anvar aka:
    35 000 × 10 = 350 000. Farq: 350 000 − 340 000 = 10 000 soʻm.</p>
    <p>Lekin bu «Karim aka har doim arzon» degani emas — b ni unutmang.
    4 m² da Karim aka 40 000 + 120 000 = 160 000, Anvar aka esa 140 000 soʻm
    oladi: kichik ishda kelish haqisiz usta afzal. Ikkalasi 8 m² da tenglashadi
    (280 000 soʻm).</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Boshlangʻich qiymat (b)</b><span>x = 0 dagi miqdor; ingl. initial
    value</span></li>
  <li><b>Oʻzgarish tezligi (k)</b><span>bir birlikka qancha; ingl. rate of
    change</span></li>
  <li><b>Abonent haqi</b><span>foydalanmasa ham toʻlanadigan pul; ingl. fixed
    fee</span></li>
  <li><b>Tarif</b><span>bir birlik xizmatning narxi; ingl. rate</span></li>
  <li><b>Parallel chiziqlar</b><span>k si bir xil, kesishmaydi; ingl. parallel
    lines</span></li>
  <li><b>Kesishish nuqtasi</b><span>ikki chiziq uchrashgan joy; ingl. point of
    intersection</span></li>
  <li><b>Kamayuvchi jarayon</b><span>manfiy k bilan yoziladi; ingl. decreasing
    process</span></li>
  <li><b>Maʼnoli soha</b><span>grafikning masalaga mos qismi; ingl. valid
    domain</span></li>
  <li><b>Qiyalik</b><span>chiziqning tikligi, k; ingl. slope</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>b — boshida qancha, k — har birlik uchun qancha.</b> Har qanday
      tarifni shu ikki soʻz bilan oʻqing.</li>
    <li><b>Kamayish — manfiy k.</b> Grafik oʻngga qarab tushadi.</li>
    <li><b>Katta k qimmat degani emas</b> — kim arzon ekani qaysi x da
      qaraganingizga bogʻliq.</li>
  </ul>
</div>
""",
    },
]
