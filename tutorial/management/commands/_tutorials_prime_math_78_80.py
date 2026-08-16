# -*- coding: utf-8 -*-
"""Prime Math — darslar 78–80 (oʻrta arifmetik, mediana va moda, tarqoqlik).

**Blok F: Maʼlumot va ehtimollik (75–84).**
Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md

  mashqlar — practice/management/commands/_practice_pm_78_80.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_78_80.py

⚠️ Bu uchlik — Blok F ning yuragi va u BITTA gʻoya atrofida qurilgan:
   yagona son maʼlumotni toʻliq tasvirlay olmaydi.
     PM-78 oʻrtachani beradi → PM-78 ning oxirida uni bitta katta son
     buzib qoʻyadi → PM-79 medianani beradi → PM-80 esa ikkala jamoaning
     oʻrtachasi bir xil boʻlsa ham ular bir xil emasligini koʻrsatadi.
   Shuning uchun chiziqli ketma-ketlikni buzmang.

⚠️ Chizmalar generatsiya qilingan: scratchpad/gen_pm78_80.py.
   Yangi komponent `.pm-ch__ref` (taqqoslash chizigʻi) style.css ga va
   STYLE_GUIDE ga qoʻshildi. verify_pm_78_80.py SVG ni qayta oʻqib,
   har bir ustun balandligini, har bir nuqta oʻrnini va oʻrtacha
   chizigʻining joyini maʼlumotdan qaytadan hisoblaydi.

⚠️ Kumulyativ chegaralar:
  • PM-78 — faqat oʻrta arifmetik. ⛔ MEDIANA va MODA yoʻq: darsning
    oxirida chetki son muammosi KOʻRSATILADI, lekin yechilmaydi —
    bitta jumla bilan keyingi darsga havola qilinadi;
  • PM-79 — mediana va moda, uchalasini taqqoslash;
  • PM-80 — tarqoqlik. Oʻrtacha va mediana bemalol ishlatiladi.
  • ⛔ Aldamchi diagrammalar (PM-81), sanash (PM-82) va ehtimollik
    (PM-83/84) YOʻQ.
  • Faol ishlatiladi: maʼlumot va jadval (PM-75), diagramma turlari
    (PM-76), diagrammani oʻqish (PM-77), foiz (PM-23), oʻnlik kasr
    (PM-20/21), manfiy son (PM-9).

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_78_80.py --author=prime
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
    # PM-78 — oʻrta arifmetik
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-78: Oʻrta arifmetik",
        "category": "math",
        "order": 78,
        "summary": (
            "Oʻrtacha — bu «agar hammaga baravar boʻlinganda» degani. Uni "
            "topishni, teskari masalani yechishni va nega bitta katta son "
            "oʻrtachani buzib qoʻyishini koʻrasiz."
        ),
        "stories": ["Oʻrtacha baho — kundalik daftar"],
        "content": """
<h2>PM-78: Oʻrta arifmetik</h2>

<p>«Oʻrtacha bahom qancha?» «Oʻrtacha necha soat uxlaysan?» «Bu oyda
oʻrtacha qancha sarfladik?»</p>

<p>Bu savollarning hammasi bitta amalga olib keladi. Va u juda oddiy:
<b>hammasini qoʻsh, keyin nechta ekaniga boʻl</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>oʻrta arifmetikni topasiz va uning maʼnosini tushuntirasiz;</li>
    <li>oʻrtacha maʼlum boʻlganda yigʻindini tiklaysiz;</li>
    <li>yetishmayotgan qiymatni topasiz;</li>
    <li>bitta chetki son oʻrtachani qanday buzishini koʻrasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Oʻrta arifmetik</span>
  <span class="pe-chip pe-chip--s">oʻrtacha</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">yigʻindi</span>
  <span class="pe-op">÷</span>
  <span class="pe-chip pe-chip--o">sonlar soni</span>
</div>

<h3>1. Oʻrtacha — bu «baravar boʻlinganda»</h3>

<p>Afsonaning matematikadan beshta bahosi bor: 5, 4, 5, 3, 4.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 195" role="img" aria-label="Besh baho va ularning oʻrta arifmetigi">
    <line class="pm-ch__ax" x1="46" y1="160" x2="302" y2="160"/>
    <text class="pm-ch__cap" x="40" y="164" text-anchor="end">0</text>
    <line class="pm-ch__grid" x1="46" y1="120" x2="302" y2="120"/>
    <text class="pm-ch__cap" x="40" y="124" text-anchor="end">2</text>
    <line class="pm-ch__grid" x1="46" y1="80" x2="302" y2="80"/>
    <text class="pm-ch__cap" x="40" y="84" text-anchor="end">4</text>
    <line class="pm-ch__grid" x1="46" y1="40" x2="302" y2="40"/>
    <text class="pm-ch__cap" x="40" y="44" text-anchor="end">6</text>
    <rect class="pm-ch__bar" x="69.3" y="60" width="34" height="100" rx="3"/>
    <text class="pm-ch__val" x="86.3" y="53" text-anchor="middle">5</text>
    <text class="pm-ch__lbl" x="86.3" y="178" text-anchor="middle">1</text>
    <rect class="pm-ch__bar" x="114.7" y="80" width="34" height="80" rx="3"/>
    <text class="pm-ch__val" x="131.7" y="73" text-anchor="middle">4</text>
    <text class="pm-ch__lbl" x="131.7" y="178" text-anchor="middle">2</text>
    <rect class="pm-ch__bar" x="160" y="60" width="34" height="100" rx="3"/>
    <text class="pm-ch__val" x="177" y="53" text-anchor="middle">5</text>
    <text class="pm-ch__lbl" x="177" y="178" text-anchor="middle">3</text>
    <rect class="pm-ch__bar" x="205.3" y="100" width="34" height="60" rx="3"/>
    <text class="pm-ch__val" x="222.3" y="93" text-anchor="middle">3</text>
    <text class="pm-ch__lbl" x="222.3" y="178" text-anchor="middle">4</text>
    <rect class="pm-ch__bar" x="250.7" y="80" width="34" height="80" rx="3"/>
    <text class="pm-ch__val" x="267.7" y="73" text-anchor="middle">4</text>
    <text class="pm-ch__lbl" x="267.7" y="178" text-anchor="middle">5</text>
    <line class="pm-ch__ref" x1="46" y1="76" x2="302" y2="76"/>
    <text class="pm-ch__val" x="302" y="32" text-anchor="end">oʻrtacha 4,2</text>
  </svg>
  <figcaption>Punktir chiziq — oʻrtacha. Baland ustunlardan olib, past
  ustunlarga qoʻshsak, hammasi shu chiziqqa tekislanadi.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">5 + 4 + 5 + 3 + 4 = 21</span>
    <span class="pm-solve__why">Yigʻindi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">21 ÷ 5 = 4,2</span>
    <span class="pm-solve__why">Beshta baho boʻlgani uchun 5 ga boʻldik</span>
  </div>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Oʻrtachaning maʼnosi</p>
  <p>Oʻrtacha 4,2 degani: <b>agar bahoning hammasi bir xil boʻlganida,
  har biri 4,2 boʻlardi</b>. Yigʻindi oʻzgarmaydi — u faqat baravar
  taqsimlanadi.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Oʻrtacha maʼlumotdagi sonlardan biri boʻlishi
  shart emas</p>
  <p>Afsonada 4,2 degan baho yoʻq — bunday baho umuman boʻlmaydi. Xuddi
  shunday, oilada «oʻrtacha 2,5 ta bola» boʻlishi mumkin, lekin hech
  bir oilada yarim bola yoʻq. Oʻrtacha — bu <b>hisob natijasi</b>, roʻyxatdan
  olingan son emas.</p>
</div>

<h3>2. Teskari masala: oʻrtachadan yigʻindiga</h3>

<p>Formulani teskari oʻgirsak, juda foydali qoida chiqadi:</p>

<div class="pe-formula">
  <span class="pe-formula__label">Yigʻindini tiklash</span>
  <span class="pe-chip pe-chip--o">yigʻindi</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">oʻrtacha</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--o">sonlar soni</span>
</div>

<p>Afsonaning toʻrtta bahosining oʻrtachasi 4 edi. Beshinchi bahodan
keyin oʻrtacha 4,2 boʻldi. Beshinchi baho qanday?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">4 × 4 = 16</span>
    <span class="pm-solve__why">Toʻrtta bahoning yigʻindisi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4,2 × 5 = 21</span>
    <span class="pm-solve__why">Beshta bahoning yigʻindisi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">21 − 16 = 5</span>
    <span class="pm-solve__why">Yangi baho — farqning oʻzi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Bahosi 4, 4, 4, 4 va 5 boʻlsa: yigʻindi 21, va 21 ÷ 5 = 4,2 ✓</p>
</div>

<h3>3. Bitta katta son hammasini buzadi</h3>

<p>Beshta oʻquvchining bir kunlik choʻntak puli (ming soʻmda): 5, 6, 5,
4 va 30.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 195" role="img" aria-label="Choʻntak puli: bitta katta son oʻrtachani tortib ketadi">
    <line class="pm-ch__ax" x1="46" y1="160" x2="302" y2="160"/>
    <text class="pm-ch__cap" x="40" y="164" text-anchor="end">0</text>
    <line class="pm-ch__grid" x1="46" y1="120" x2="302" y2="120"/>
    <text class="pm-ch__cap" x="40" y="124" text-anchor="end">10</text>
    <line class="pm-ch__grid" x1="46" y1="80" x2="302" y2="80"/>
    <text class="pm-ch__cap" x="40" y="84" text-anchor="end">20</text>
    <line class="pm-ch__grid" x1="46" y1="40" x2="302" y2="40"/>
    <text class="pm-ch__cap" x="40" y="44" text-anchor="end">30</text>
    <rect class="pm-ch__bar" x="69.3" y="140" width="34" height="20" rx="3"/>
    <text class="pm-ch__val" x="86.3" y="133" text-anchor="middle">5</text>
    <text class="pm-ch__lbl" x="86.3" y="178" text-anchor="middle">1</text>
    <rect class="pm-ch__bar" x="114.7" y="136" width="34" height="24" rx="3"/>
    <text class="pm-ch__val" x="131.7" y="129" text-anchor="middle">6</text>
    <text class="pm-ch__lbl" x="131.7" y="178" text-anchor="middle">2</text>
    <rect class="pm-ch__bar" x="160" y="140" width="34" height="20" rx="3"/>
    <text class="pm-ch__val" x="177" y="133" text-anchor="middle">5</text>
    <text class="pm-ch__lbl" x="177" y="178" text-anchor="middle">3</text>
    <rect class="pm-ch__bar" x="205.3" y="144" width="34" height="16" rx="3"/>
    <text class="pm-ch__val" x="222.3" y="137" text-anchor="middle">4</text>
    <text class="pm-ch__lbl" x="222.3" y="178" text-anchor="middle">4</text>
    <rect class="pm-ch__bar" x="250.7" y="40" width="34" height="120" rx="3"/>
    <text class="pm-ch__val" x="267.7" y="33" text-anchor="middle">30</text>
    <text class="pm-ch__lbl" x="267.7" y="178" text-anchor="middle">5</text>
    <line class="pm-ch__ref" x1="46" y1="120" x2="302" y2="120"/>
    <text class="pm-ch__val" x="52" y="113" text-anchor="start">oʻrtacha 10</text>
  </svg>
  <figcaption>Beshtadan toʻrttasi oʻrtacha chizigʻidan pastda qolgan.
  Bitta katta son oʻrtachani yuqoriga tortib ketdi.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">5 + 6 + 5 + 4 + 30 = 50</span>
    <span class="pm-solve__why">Yigʻindi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">50 ÷ 5 = 10 ming soʻm</span>
    <span class="pm-solve__why">Oʻrtacha</span>
  </div>
</div>

<p>Endi diqqat qiling: <b>beshtadan toʻrttasining puli oʻrtachadan
kam</b>. «Oʻrtacha 10 ming» degan jumla toʻgʻri, lekin u sinf haqida
notoʻgʻri taassurot qoldiradi.</p>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Bu muammoni keyingi darsda hal qilamiz</p>
  <p>Oʻrtacha — kuchli, lekin yagona qurol emas. Bunday hollarda
  haqiqatni toʻgʻriroq aytadigan boshqa son bor; u bilan PM-79 da
  tanishasiz.</p>
</div>

<h3>Matnli masala</h3>

<p>Karim aka taksi haydaydi. Besh ish kunidagi daromadi (ming soʻmda):
90, 120, 80, 150 va 110.</p>

<p><b>Bir kunlik oʻrtacha daromadi qancha va shu tezlikda ishlasa, toʻrt
haftada (20 ish kunida) qancha topadi?</b></p>

<p><b>Reja:</b> oʻrtachani topamiz, keyin uni ish kunlari soniga
koʻpaytiramiz.</p>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Sonlar 80 bilan 150 orasida, koʻpchiligi 100 atrofida — demak
  oʻrtacha ham 100–120 orasida boʻlishi kerak.</span>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">90 + 120 + 80 + 150 + 110 = 550</span>
    <span class="pm-solve__why">Besh kunlik yigʻindi (ming soʻm)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">550 ÷ 5 = 110</span>
    <span class="pm-solve__why">Bir kunlik oʻrtacha</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">110 × 20 = 2200 ming = 2 200 000 soʻm</span>
    <span class="pm-solve__why">Yigʻindi = oʻrtacha × kunlar soni</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>110 — taxminimizdagi 100–120 oraligʻida ✓
  <br>Boshqa yoʻl: bir haftada 550 ming, toʻrt haftada 550 × 4 =
  2200 ming ✓ — javob mos keldi.
  <br><b>Javob:</b> kuniga 110 000 soʻm, oyiga 2 200 000 soʻm.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">5 + 4 + 5 + 3 + 4 = 21, demak oʻrtacha 21</p>
  <p class="pe-fix__good">21 ÷ 5 = 4,2</p>
  <p class="pe-fix__why">Boʻlish qadami tushib qolgan. Oʻrtacha har doim
  eng katta son bilan eng kichik son <b>orasida</b> boʻladi — 21 esa
  hammasidan katta, demak u javob boʻlolmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Oʻrtacha 4,2 chiqdi — 4 deb yozamiz</p>
  <p class="pe-fix__good">4,2 — javobning oʻzi</p>
  <p class="pe-fix__why">Oʻrtacha butun son boʻlishi shart emas. Uni
  yaxlitlash faqat masala shuni soʻraganda qilinadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Toʻrtta sonning oʻrtachasi 6 → yigʻindi 6 ÷ 4 =
  1,5</p>
  <p class="pe-fix__good">Yigʻindi = 6 × 4 = 24</p>
  <p class="pe-fix__why">Teskari masalada <b>koʻpaytiriladi</b>. Yigʻindi
  har doim oʻrtachadan katta boʻladi (sonlar bittadan koʻp
  boʻlganda).</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Uch kunda 20 sahifa, toʻrt kunda 28 sahifa →
  oʻrtacha (20 + 28) ÷ 2 = 24</p>
  <p class="pe-fix__good">(20 + 28) ÷ 7 ≈ 6,9 sahifa</p>
  <p class="pe-fix__why">Oʻrtachani ikkita <em>oʻrtachadan</em> emas,
  butun yigʻindidan hisoblang: hammasi 48 sahifa, kunlar esa 7 ta.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 3, 7 va 5 sonlarining oʻrta arifmetigi
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5.</b> 3 + 7 + 5 = 15, va 15 ÷ 3 = 5.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 10, 12, 14 va 8 sonlarining oʻrtachasi
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>11.</b> 10 + 12 + 14 + 8 = 44, va 44 ÷ 4 = 11.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Toʻrtta sonning oʻrtachasi 6. Ularning
  yigʻindisi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>24.</b> Yigʻindi = oʻrtacha × soni = 6 × 4 = 24.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Toʻrtta oilada 2, 3, 2 va 3 tadan bola bor.
  Oʻrtacha nechta?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>2,5 ta.</b> 2 + 3 + 2 + 3 = 10, va 10 ÷ 4 = 2,5. Hech bir
    oilada 2,5 ta bola yoʻq — bu oddiy hol, oʻrtacha shunday
    boʻlaveradi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Beshta sonning oʻrtachasi 8. Ulardan toʻrttasi
  6, 7, 9 va 10. Beshinchisi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>8.</b> Butun yigʻindi: 8 × 5 = 40. Maʼlum toʻrttasi:
    6 + 7 + 9 + 10 = 32. Beshinchisi: 40 − 32 = 8.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Sherbek toʻrt kun kitob oʻqidi: 20, 35, 25 va
  40 sahifa. Oʻrtacha kuniga necha sahifa oʻqidi? Beshinchi kuni necha
  sahifa oʻqisa, oʻrtachasi 32 boʻladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>30 sahifa; keyin 40 sahifa.</b> Yigʻindi:
    20 + 35 + 25 + 40 = 120, va 120 ÷ 4 = 30 sahifa. Beshta kunning
    yigʻindisi 32 × 5 = 160 boʻlishi kerak, demak beshinchi kuni
    160 − 120 = 40 sahifa oʻqishi kerak.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Oʻrta arifmetik</b><span>yigʻindini sonlar soniga boʻlish; ingl.
    mean</span></li>
  <li><b>Oʻrtacha</b><span>oʻrta arifmetikning qisqa nomi; ingl.
    average</span></li>
  <li><b>Yigʻindi</b><span>hamma sonning qoʻshilgani; ingl.
    sum</span></li>
  <li><b>Sonlar soni</b><span>maʼlumotda nechta qiymat borligi; ingl.
    count</span></li>
  <li><b>Maʼlumot toʻplami</b><span>birga qaraladigan sonlar roʻyxati;
    ingl. data set</span></li>
  <li><b>Chetki son</b><span>qolganlaridan keskin farq qiladigan qiymat;
    ingl. outlier</span></li>
  <li><b>Tekislash</b><span>hammasini baravar qilib taqsimlash; ingl.
    levelling</span></li>
  <li><b>Teskari masala</b><span>natijadan berilganni topish; ingl.
    inverse problem</span></li>
  <li><b>Yaxlitlash</b><span>sonni qulay koʻrinishga keltirish; ingl.
    rounding</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Oʻrtacha = yigʻindi ÷ sonlar soni.</li>
    <li>Maʼnosi: «agar hammasi baravar boʻlinganda».</li>
    <li>Yigʻindi = oʻrtacha × sonlar soni — teskari masalaning
      kaliti.</li>
    <li>Oʻrtacha butun son boʻlishi ham, maʼlumotdagi sonlardan biri
      boʻlishi ham shart emas.</li>
    <li>U har doim eng kichik va eng katta son orasida yotadi — javobni
      shu bilan tekshiring.</li>
    <li>Bitta chetki son oʻrtachani oʻziga tortib ketadi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-79 — mediana va moda
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-79: Mediana va moda — qaysi biri haqiqatni toʻgʻriroq aytadi",
        "category": "math",
        "order": 79,
        "summary": (
            "Oʻrtachani bitta katta son buzib qoʻyadi. Mediana — saralangan "
            "qatordagi oʻrtadagi son — bunga berilmaydi. Moda esa eng koʻp "
            "uchraganini aytadi va hatto sonsiz maʼlumotda ham ishlaydi."
        ),
        "stories": ["«Oʻrtacha maosh» qanday aldaydi"],
        "content": """
<h2>PM-79: Mediana va moda — qaysi biri haqiqatni toʻgʻriroq aytadi</h2>

<p>Oʻtgan darsni bitta muammo bilan tugatgan edik: beshta oʻquvchining
choʻntak puli 5, 6, 5, 4 va 30 ming soʻm. Oʻrtacha 10 ming chiqdi —
lekin beshtadan toʻrttasida bundan kam pul bor.</p>

<p>Demak «oʻrtacha 10 ming» degan jumla rost, lekin haqiqatni
koʻrsatmaydi. Uni koʻrsatadigan ikkita boshqa son bor.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>medianani topasiz — sonlar juft va toq boʻlganda ham;</li>
    <li>modani topasiz va u sonsiz maʼlumotda ham ishlashini
      koʻrasiz;</li>
    <li>uchala oʻlchovni bir maʼlumotda taqqoslaysiz;</li>
    <li>qaysi biri qachon toʻgʻriroq gapirishini bilib olasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Mediana</span>
  <span class="pe-chip pe-chip--v">saralang</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">oʻrtadagi son</span>
</div>

<h3>1. Mediana — qatorning oʻrtasi</h3>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Ikki qadam, tartibi muhim</p>
  <p>1. Sonlarni <b>oʻsish tartibida saralang</b>.
  <br>2. Roppa-rosa <b>oʻrtadagi</b> sonni oling.
  <br>Saralamasdan oʻrtadagini olish — bu darsdagi eng koʻp uchraydigan
  xato.</p>
</div>

<p>Choʻntak pullarini saralaymiz: 4, 5, 5, 6, 30. Beshta son bor, demak
uchinchisi oʻrtada turadi — <b>5</b>.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 158" role="img" aria-label="Bir katta son oʻrtachani tortadi, mediana joyida qoladi">
    <line class="pm-ch__ax" x1="76" y1="100" x2="304" y2="100"/>
    <line class="pm-ch__ax" x1="84" y1="100" x2="84" y2="105"/>
    <text class="pm-ch__cap" x="84" y="118" text-anchor="middle">0</text>
    <line class="pm-ch__ax" x1="119.3" y1="100" x2="119.3" y2="105"/>
    <text class="pm-ch__cap" x="119.3" y="118" text-anchor="middle">5</text>
    <line class="pm-ch__ax" x1="154.7" y1="100" x2="154.7" y2="105"/>
    <text class="pm-ch__cap" x="154.7" y="118" text-anchor="middle">10</text>
    <line class="pm-ch__ax" x1="190" y1="100" x2="190" y2="105"/>
    <text class="pm-ch__cap" x="190" y="118" text-anchor="middle">15</text>
    <line class="pm-ch__ax" x1="225.3" y1="100" x2="225.3" y2="105"/>
    <text class="pm-ch__cap" x="225.3" y="118" text-anchor="middle">20</text>
    <line class="pm-ch__ax" x1="260.7" y1="100" x2="260.7" y2="105"/>
    <text class="pm-ch__cap" x="260.7" y="118" text-anchor="middle">25</text>
    <line class="pm-ch__ax" x1="296" y1="100" x2="296" y2="105"/>
    <text class="pm-ch__cap" x="296" y="118" text-anchor="middle">30</text>
    <circle class="pm-ch__dot" cx="112.3" cy="91" r="5"/>
    <circle class="pm-ch__dot" cx="119.3" cy="91" r="5"/>
    <circle class="pm-ch__dot" cx="119.3" cy="78" r="5"/>
    <circle class="pm-ch__dot" cx="126.4" cy="91" r="5"/>
    <circle class="pm-ch__dot" cx="296" cy="91" r="5"/>
    <text class="pm-ch__lbl" x="70" y="95" text-anchor="end">maosh</text>
    <line class="pm-ch__ref" x1="119.3" y1="54" x2="119.3" y2="106"/>
    <text class="pm-ch__val" x="119.3" y="44" text-anchor="middle">mediana 5</text>
    <line class="pm-ch__ref" x1="154.7" y1="30" x2="154.7" y2="106"/>
    <text class="pm-ch__val" x="154.7" y="20" text-anchor="middle">oʻrtacha 10</text>
  </svg>
  <figcaption>Toʻrtta nuqta chapda gavjum, bittasi esa uzoqda. Mediana
  gavjum joyda qoldi, oʻrtacha esa chetki songa tortildi.</figcaption>
</figure>

<p>Mana asosiy farq: agar oʻsha 30 ming 300 ming boʻlganida ham,
<b>mediana baribir 5 boʻlib qolardi</b> — chunki oʻrtadagi son
oʻzgarmaydi. Oʻrtacha esa 70 mingga sakrardi.</p>

<h3>2. Sonlar juft boʻlsa</h3>

<p>Agar sonlar soni juft boʻlsa, oʻrtada bittasi emas, <b>ikkitasi</b>
turadi. Unda ularning oʻrta arifmetigi olinadi (PM-78).</p>

<div class="pe-ex">
  <p class="pe-ex__math">3, 5, 8, 10 → (5 + 8) ÷ 2 = 6,5</p>
  <p class="pe-ex__uz">Toʻrtta son bor, oʻrtadagilari 5 va 8; mediana —
  6,5.</p>
  <p class="pe-ex__why">Mediana ham maʼlumotdagi sonlardan biri boʻlishi
  shart emas.</p>
</div>

<h3>3. Moda — eng koʻp uchragani</h3>

<p><b>Moda</b> — maʼlumotda eng koʻp marta takrorlangan qiymat. Choʻntak
pullarida 5 ikki marta uchradi, qolganlari bir martadan — demak moda
<b>5</b>.</p>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Moda sonsiz maʼlumotda ham ishlaydi</p>
  <p>«Sinfda eng koʻp uchraydigan sevimli meva» yoki «doʻkonda eng koʻp
  sotiladigan oʻlcham» — bularning oʻrtachasini ham, medianasini ham
  hisoblab boʻlmaydi. Modani esa topsa boʻladi, chunki u faqat sanashni
  talab qiladi. Doʻkonchi uchun aynan shu son kerak.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Moda boʻlmasligi ham, bir nechta boʻlishi ham
  mumkin</p>
  <p>Agar hamma son bir martadan uchrasa, moda <b>yoʻq</b>. Agar ikkita
  qiymat bir xil marta takrorlansa, <b>ikkalasi ham</b> moda boʻladi. Bu
  xato emas — shunchaki maʼlumotning xossasi.</p>
</div>

<h3>4. Uchalasini yonma-yon qoʻyamiz</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Oʻlchov</th><th>Qanday topiladi</th><th>Chetki songa</th></tr>
  <tr><td>Oʻrta arifmetik</td>
    <td class="pm-word__sym">yigʻindi ÷ soni</td>
    <td>juda sezgir</td></tr>
  <tr><td>Mediana</td>
    <td class="pm-word__sym">saralab, oʻrtadagi</td>
    <td>deyarli sezgir emas</td></tr>
  <tr><td>Moda</td>
    <td class="pm-word__sym">eng koʻp uchragani</td>
    <td>sezgir emas</td></tr>
</table></div>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Qachon ishlatiladi</th><th>Qaysi biri</th></tr>
  <tr><td>Sonlar bir-biriga yaqin, chetki son yoʻq</td>
    <td class="pm-word__sym">oʻrtacha</td></tr>
  <tr><td>Bitta-ikkita son juda katta yoki juda kichik</td>
    <td class="pm-word__sym">mediana</td></tr>
  <tr><td>Maʼlumot son emas (rang, oʻlcham, meva)</td>
    <td class="pm-word__sym">moda</td></tr>
</table></div>

<h3>Matnli masala</h3>

<p>Kichik korxonada yetti kishi ishlaydi. Oylik maoshlari (million
soʻmda): 5, 3, 26, 3, 4, 5 va 3.</p>

<p><b>Uchala oʻlchovni ham toping. Ish qidirayotgan odamga qaysi birini
aytish halolroq?</b></p>

<p><b>Reja:</b> avval saralaymiz — mediana ham, moda ham shundan
koʻrinadi. Keyin oʻrtachani hisoblaymiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3, 3, 3, 4, 5, 5, 26</span>
    <span class="pm-solve__why">Saraladik — birinchi qadam har
    doim shu</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3+3+3+4+5+5+26 = 49; 49 ÷ 7 = 7</span>
    <span class="pm-solve__why">Oʻrta arifmetik — 7 million</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Toʻrtinchi son = 4</span>
    <span class="pm-solve__why">Mediana: yettita sonning oʻrtasi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3 uch marta uchradi → moda 3</span>
    <span class="pm-solve__why">Eng koʻp takrorlangani</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Yettitadan <b>oltitasi</b> 7 milliondan kam oladi — demak
  «oʻrtacha maosh 7 million» degan gap odamni chalgʻitadi.
  <br>Mediana 4: yarmi bundan koʻp, yarmi kam oladi — bu halol son.
  <br><b>Javob:</b> oʻrtacha 7, mediana 4, moda 3 million. Ish
  qidirayotgan odamga <b>medianani</b> aytish toʻgʻriroq.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">7, 2, 9, 4, 5 → mediana 9 (oʻrtada turibdi)</p>
  <p class="pe-fix__good">Saralaymiz: 2, 4, 5, 7, 9 → mediana 5</p>
  <p class="pe-fix__why">Saralashsiz mediana topib boʻlmaydi. «Oʻrtadagi»
  degani roʻyxatdagi emas, <b>saralangan qatordagi</b> oʻrtadagi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">2, 4, 6, 8 → mediana 4 yoki 6</p>
  <p class="pe-fix__good">(4 + 6) ÷ 2 = 5</p>
  <p class="pe-fix__why">Sonlar juft boʻlganda oʻrtada ikkita son
  qoladi va ularning oʻrta arifmetigi olinadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">3, 3, 3, 7, 9 → moda 3 marta</p>
  <p class="pe-fix__good">Moda — 3</p>
  <p class="pe-fix__why">Moda — <b>qiymatning oʻzi</b>, u necha marta
  uchragani emas. «Necha marta» degani chastota (PM-75).</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Mediana har doim oʻrtachadan kichik</p>
  <p class="pe-fix__good">Qaysi tomonda chetki son boʻlsa, oʻrtacha
  oʻsha tomonga siljiydi</p>
  <p class="pe-fix__why">Katta chetki son oʻrtachani yuqoriga, kichik
  chetki son pastga tortadi. Chetki son boʻlmasa, ikkalasi deyarli teng
  chiqadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 3, 7, 5, 9, 1 sonlarining medianasi
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5.</b> Saralaymiz: 1, 3, 5, 7, 9. Beshta son, oʻrtadagisi
    uchinchisi — 5.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 4, 8, 6, 2 sonlarining medianasi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5.</b> Saralaymiz: 2, 4, 6, 8. Juft son, oʻrtadagilari 4 va 6:
    (4 + 6) ÷ 2 = 5.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 2, 3, 3, 5, 7 sonlarining modasi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3.</b> U ikki marta uchradi, qolganlari bir martadan.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 1, 2, 3, 4 va 100 sonlarining oʻrtachasi va
  medianasini toping. Qaysi biri maʼlumotni yaxshiroq tasvirlaydi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Oʻrtacha 22, mediana 3; mediana yaxshiroq.</b> Yigʻindi
    1 + 2 + 3 + 4 + 100 = 110, va 110 ÷ 5 = 22. Mediana — saralangan
    qatorning oʻrtasi, yaʼni 3. Beshta sondan toʻrttasi 22 dan kichik,
    demak oʻrtacha bu yerda chalgʻitadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Doʻkonda shu oʻlchamdagi tuflilar sotildi:
  38, 39, 39, 40, 41, 39. Doʻkonchi keyingi safar qaysi oʻlchamdan
  koʻproq keltirishi kerak?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>39 — bu moda.</b> U uch marta sotilgan. Bu yerda oʻrtachaning
    maʼnosi yoʻq: «oʻrtacha oʻlcham 39,3» degan tufli sotilmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Sinfda oltita oʻquvchining nazorat ishi
  bahosi: 5, 3, 4, 5, 2, 5. Oʻrtacha, mediana va modani toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Oʻrtacha 4, mediana 4,5, moda 5.</b> Yigʻindi:
    5 + 3 + 4 + 5 + 2 + 5 = 24, va 24 ÷ 6 = 4. Saralaymiz:
    2, 3, 4, 5, 5, 5 — oʻrtadagilari 4 va 5, demak mediana
    (4 + 5) ÷ 2 = 4,5. Moda — 5 (uch marta).</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Mediana</b><span>saralangan qatorning oʻrtasidagi son; ingl.
    median</span></li>
  <li><b>Moda</b><span>eng koʻp uchragan qiymat; ingl. mode</span></li>
  <li><b>Saralash</b><span>oʻsish tartibida joylashtirish; ingl.
    sorting</span></li>
  <li><b>Oʻrta arifmetik</b><span>yigʻindi ÷ soni; ingl. mean</span></li>
  <li><b>Chetki son</b><span>qolganlaridan keskin farq qiladigan qiymat;
    ingl. outlier</span></li>
  <li><b>Markaziy oʻlchov</b><span>maʼlumotni bitta son bilan
    tasvirlovchi kattalik; ingl. measure of centre</span></li>
  <li><b>Chastota</b><span>qiymat necha marta uchragani; ingl.
    frequency</span></li>
  <li><b>Maʼlumot toʻplami</b><span>birga qaraladigan qiymatlar; ingl.
    data set</span></li>
  <li><b>Vakillik</b><span>sonning maʼlumotni toʻgʻri ifodalashi; ingl.
    representativeness</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Mediana: avval <b>saralang</b>, keyin oʻrtadagini oling.</li>
    <li>Sonlar juft boʻlsa — oʻrtadagi ikkitasining oʻrta
      arifmetigi.</li>
    <li>Moda — eng koʻp uchragan <b>qiymat</b>, uning soni emas.</li>
    <li>Moda yoʻq boʻlishi ham, bir nechta boʻlishi ham mumkin.</li>
    <li>Chetki son bor joyda mediana haqiqatni toʻgʻriroq aytadi.</li>
    <li>Maʼlumot son boʻlmasa, faqat moda ishlaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-80 — tarqoqlik
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-80: Tarqoqlik: eng katta va eng kichik orasidagi farq",
        "category": "math",
        "order": 80,
        "summary": (
            "Ikki jamoaning oʻrtachasi bir xil boʻlishi mumkin, lekin ular "
            "umuman bir xil emas. Tarqoqlik — maʼlumot qanchalik yoyilganini "
            "koʻrsatadigan ikkinchi son."
        ),
        "stories": ["Ikki jamoa, bir xil oʻrtacha"],
        "content": """
<h2>PM-80: Tarqoqlik: eng katta va eng kichik orasidagi farq</h2>

<p>Ikki futbol jamoasi bir mavsumda beshta oʻyin oʻynadi. Ikkalasi ham
oʻrtacha 3 tadan gol urdi.</p>

<p>Demak ular bir xil jamoa? Aslo. Bitta son maʼlumotni toʻliq
tasvirlay olmaydi — bu Blok F ning asosiy darsi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>tarqoqlikni topasiz;</li>
    <li>bir xil oʻrtachali ikki toʻplamni ajratasiz;</li>
    <li>kichik va katta tarqoqlik nimani anglatishini aytasiz;</li>
    <li>tarqoqlikning zaif joyini ham koʻrasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Tarqoqlik</span>
  <span class="pe-chip pe-chip--s">tarqoqlik</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">eng katta</span>
  <span class="pe-op">−</span>
  <span class="pe-chip pe-chip--o">eng kichik</span>
</div>

<h3>1. Bir xil oʻrtacha, boshqacha jamoa</h3>

<p>A jamoaning gollari: 2, 3, 3, 3, 4. B jamoaniki: 0, 1, 3, 5, 6.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 210" role="img" aria-label="Ikki jamoa: bir xil oʻrtacha, har xil tarqoqlik">
    <line class="pm-ch__ax" x1="76" y1="72" x2="304" y2="72"/>
    <line class="pm-ch__ax" x1="84" y1="72" x2="84" y2="77"/>
    <text class="pm-ch__cap" x="84" y="90" text-anchor="middle">0</text>
    <line class="pm-ch__ax" x1="110.5" y1="72" x2="110.5" y2="77"/>
    <text class="pm-ch__cap" x="110.5" y="90" text-anchor="middle">1</text>
    <line class="pm-ch__ax" x1="137" y1="72" x2="137" y2="77"/>
    <text class="pm-ch__cap" x="137" y="90" text-anchor="middle">2</text>
    <line class="pm-ch__ax" x1="163.5" y1="72" x2="163.5" y2="77"/>
    <text class="pm-ch__cap" x="163.5" y="90" text-anchor="middle">3</text>
    <line class="pm-ch__ax" x1="190" y1="72" x2="190" y2="77"/>
    <text class="pm-ch__cap" x="190" y="90" text-anchor="middle">4</text>
    <line class="pm-ch__ax" x1="216.5" y1="72" x2="216.5" y2="77"/>
    <text class="pm-ch__cap" x="216.5" y="90" text-anchor="middle">5</text>
    <line class="pm-ch__ax" x1="243" y1="72" x2="243" y2="77"/>
    <text class="pm-ch__cap" x="243" y="90" text-anchor="middle">6</text>
    <line class="pm-ch__ax" x1="269.5" y1="72" x2="269.5" y2="77"/>
    <text class="pm-ch__cap" x="269.5" y="90" text-anchor="middle">7</text>
    <line class="pm-ch__ax" x1="296" y1="72" x2="296" y2="77"/>
    <text class="pm-ch__cap" x="296" y="90" text-anchor="middle">8</text>
    <circle class="pm-ch__dot" cx="137" cy="63" r="5"/>
    <circle class="pm-ch__dot" cx="163.5" cy="63" r="5"/>
    <circle class="pm-ch__dot" cx="163.5" cy="50" r="5"/>
    <circle class="pm-ch__dot" cx="163.5" cy="37" r="5"/>
    <circle class="pm-ch__dot" cx="190" cy="63" r="5"/>
    <text class="pm-ch__lbl" x="70" y="67" text-anchor="end">A jamoa</text>
    <line class="pm-ch__ref" x1="163.5" y1="26" x2="163.5" y2="78"/>
    <text class="pm-ch__val" x="163.5" y="16" text-anchor="middle">oʻrtacha 3</text>
    <line class="pm-ch__ax" x1="76" y1="164" x2="304" y2="164"/>
    <line class="pm-ch__ax" x1="84" y1="164" x2="84" y2="169"/>
    <text class="pm-ch__cap" x="84" y="182" text-anchor="middle">0</text>
    <line class="pm-ch__ax" x1="110.5" y1="164" x2="110.5" y2="169"/>
    <text class="pm-ch__cap" x="110.5" y="182" text-anchor="middle">1</text>
    <line class="pm-ch__ax" x1="137" y1="164" x2="137" y2="169"/>
    <text class="pm-ch__cap" x="137" y="182" text-anchor="middle">2</text>
    <line class="pm-ch__ax" x1="163.5" y1="164" x2="163.5" y2="169"/>
    <text class="pm-ch__cap" x="163.5" y="182" text-anchor="middle">3</text>
    <line class="pm-ch__ax" x1="190" y1="164" x2="190" y2="169"/>
    <text class="pm-ch__cap" x="190" y="182" text-anchor="middle">4</text>
    <line class="pm-ch__ax" x1="216.5" y1="164" x2="216.5" y2="169"/>
    <text class="pm-ch__cap" x="216.5" y="182" text-anchor="middle">5</text>
    <line class="pm-ch__ax" x1="243" y1="164" x2="243" y2="169"/>
    <text class="pm-ch__cap" x="243" y="182" text-anchor="middle">6</text>
    <line class="pm-ch__ax" x1="269.5" y1="164" x2="269.5" y2="169"/>
    <text class="pm-ch__cap" x="269.5" y="182" text-anchor="middle">7</text>
    <line class="pm-ch__ax" x1="296" y1="164" x2="296" y2="169"/>
    <text class="pm-ch__cap" x="296" y="182" text-anchor="middle">8</text>
    <circle class="pm-ch__dot" cx="84" cy="155" r="5"/>
    <circle class="pm-ch__dot" cx="110.5" cy="155" r="5"/>
    <circle class="pm-ch__dot" cx="163.5" cy="155" r="5"/>
    <circle class="pm-ch__dot" cx="216.5" cy="155" r="5"/>
    <circle class="pm-ch__dot" cx="243" cy="155" r="5"/>
    <text class="pm-ch__lbl" x="70" y="159" text-anchor="end">B jamoa</text>
    <line class="pm-ch__ref" x1="163.5" y1="118" x2="163.5" y2="170"/>
    <text class="pm-ch__val" x="163.5" y="108" text-anchor="middle">oʻrtacha 3</text>
  </svg>
  <figcaption>Ikkala jamoaning oʻrtachasi ham 3. Lekin A ning nuqtalari
  bir joyda tiqilgan, B niki esa butun oʻqqa yoyilgan.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">A: 2+3+3+3+4 = 15; 15 ÷ 5 = 3</span>
    <span class="pm-solve__why">Oʻrtacha (PM-78)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">B: 0+1+3+5+6 = 15; 15 ÷ 5 = 3</span>
    <span class="pm-solve__why">Aynan oʻsha oʻrtacha</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">A: 4 − 2 = 2</span>
    <span class="pm-solve__why">A ning tarqoqligi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">B: 6 − 0 = 6</span>
    <span class="pm-solve__why">B ning tarqoqligi — uch barobar
    katta</span>
  </div>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Ikkita son — ikkita savol</p>
  <p><b>Oʻrtacha</b> maʼlumot <em>qayerda</em> turganini aytadi.
  <b>Tarqoqlik</b> u <em>qanchalik yoyilganini</em> aytadi. Maʼlumotni
  tasvirlash uchun ikkalasi ham kerak.</p>
</div>

<h3>2. Kichik tarqoqlik nimani anglatadi</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Kichik tarqoqlik</p>
    <p>Barqaror, oldindan aytsa boʻladigan. A jamoa har oʻyinda 2–4 gol
    uradi — undan nima kutishni bilasiz.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Katta tarqoqlik</p>
    <p>Notinch, kutilmagan. B jamoa 6 gol ham uradi, hech gol ham
    urmaydi. Undan nima kutishni bilmaysiz.</p>
  </div>
</div>

<p>Qaysi biri yaxshiroq? <b>Savolga bogʻliq.</b> Muhim oʻyinda ishonchli
natija kerak boʻlsa — A. Kuchli raqibni yengish uchun katta natija kerak
boʻlsa — B ning imkoniyati bor.</p>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Tarqoqlik 0 boʻlishi mumkin</p>
  <p>Agar hamma qiymat bir xil boʻlsa (3, 3, 3, 3), tarqoqlik
  3 − 3 = <b>0</b>. Bu «xato» emas: maʼlumot umuman yoyilmagan degani.
  Tarqoqlik hech qachon manfiy boʻlmaydi, chunki eng kattadan eng
  kichigini ayiramiz.</p>
</div>

<h3>3. Tarqoqlikning zaif joyi</h3>

<p>Tarqoqlik faqat <b>ikkita</b> songa — eng kattasi va eng kichigiga —
qaraydi. Oʻrtadagi hamma narsani koʻrmaydi.</p>

<div class="pe-ex">
  <p class="pe-ex__math">3, 3, 3, 3, 20 → tarqoqlik 20 − 3 = 17</p>
  <p class="pe-ex__uz">Beshta sondan toʻrttasi bir xil, lekin tarqoqlik
  «maʼlumot juda yoyilgan» deb turibdi.</p>
  <p class="pe-ex__why">Chetki son tarqoqlikni ham xuddi oʻrtachani
  buzgandek buzadi (PM-79). Shuning uchun diagrammaga qarash shart.</p>
</div>

<h3>Matnli masala</h3>

<p>Maktabdan matematika olimpiadasiga bitta oʻquvchi yuboriladi.
Ikki nomzodning beshta sinov ishidagi ballari:</p>

<p>Afsona: 78, 80, 80, 82, 80. Jasur: 55, 70, 80, 95, 100.</p>

<p><b>Har birining oʻrtachasi va tarqoqligini toping. Barqaror natija
kerak boʻlsa, kimni yuborish kerak?</b></p>

<p><b>Reja:</b> ikkalasining oʻrtachasini hisoblaymiz, keyin
tarqoqligini topamiz va solishtiramiz.</p>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Afsonaning ballari 80 atrofida tiqilgan, Jasurniki 55 dan
  100 gacha yoyilgan. Oʻrtachasi yaqin chiqishi mumkin, lekin tarqoqligi
  keskin farq qiladi.</span>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">78+80+80+82+80 = 400; 400 ÷ 5 = 80</span>
    <span class="pm-solve__why">Afsonaning oʻrtachasi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">55+70+80+95+100 = 400; 400 ÷ 5 = 80</span>
    <span class="pm-solve__why">Jasurning oʻrtachasi — aynan
    oʻsha</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">82 − 78 = 4</span>
    <span class="pm-solve__why">Afsonaning tarqoqligi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">100 − 55 = 45</span>
    <span class="pm-solve__why">Jasurning tarqoqligi — 11 barobar
    katta</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Ikkala yigʻindi ham 400 ✓ — oʻrtachalar haqiqatan teng.
  <br>Afsonaning eng past bali (78) Jasurning eng past balidan (55)
  ancha yuqori.
  <br><b>Javob:</b> ikkalasining oʻrtachasi 80. Barqarorlik kerak
  boʻlsa — <b>Afsona</b>: uning eng yomon kuni ham 78 ball. Jasurda esa
  100 ball ham, 55 ball ham chiqishi mumkin.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Tarqoqlik = 2 + 3 + 3 + 3 + 4 = 15</p>
  <p class="pe-fix__good">4 − 2 = 2</p>
  <p class="pe-fix__why">Tarqoqlik qoʻshish emas, <b>ayirish</b>. Unga
  faqat ikkita son kerak: eng kattasi va eng kichigi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Eng kichikdan eng kattani ayiramiz: 2 − 4 = −2</p>
  <p class="pe-fix__good">4 − 2 = 2</p>
  <p class="pe-fix__why">Tarqoqlik hech qachon manfiy boʻlmaydi.
  Manfiy chiqsa — tartib teskari (PM-9).</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Oʻrtachalari teng, demak toʻplamlar bir xil</p>
  <p class="pe-fix__good">Tarqoqligini ham tekshiring</p>
  <p class="pe-fix__why">A (2,3,3,3,4) va B (0,1,3,5,6) ning oʻrtachasi
  bir xil, lekin ular umuman boshqa jamoalar. Bitta son yetarli
  emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Tarqoqlik katta — demak maʼlumot bir tekis
  yoyilgan</p>
  <p class="pe-fix__good">Tarqoqlik faqat chekkalarni koʻradi</p>
  <p class="pe-fix__why">3, 3, 3, 3, 20 da tarqoqlik 17, lekin
  maʼlumot yoyilmagan — bitta chetki son bor xolos. Diagrammani
  koʻrmasdan xulosa chiqarmang.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 3, 8, 5, 12, 7 sonlarining tarqoqligi
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>9.</b> Eng katta 12, eng kichik 3: 12 − 3 = 9.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Haroratlar: −5, 0, 3, 8. Tarqoqlik qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>13.</b> 8 − (−5) = 8 + 5 = 13 (PM-10). Manfiy sondan ayirganda
    ishora almashadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Beshta sonning hammasi 7 ga teng. Tarqoqlik
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>0.</b> 7 − 7 = 0. Maʼlumot umuman yoyilmagan.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 4, 6, 5, 7 toʻplamiga 20 soni qoʻshildi.
  Tarqoqlik qanday oʻzgaradi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3 dan 16 ga oshadi.</b> Avval: 7 − 4 = 3. Keyin:
    20 − 4 = 16. Bitta chetki son tarqoqlikni besh barobardan koʻproq
    kattalashtirdi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Ikki doʻkonda nonning narxi bir hafta
  davomida kuzatildi. Birinchisida 4000–4200 soʻm, ikkinchisida
  3500–5000 soʻm. Qaysi doʻkonning narxi barqarorroq?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Birinchisi.</b> Tarqoqligi 4200 − 4000 = 200 soʻm, ikkinchisida
    esa 5000 − 3500 = 1500 soʻm. Kichik tarqoqlik — oldindan aytsa
    boʻladigan narx.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Bekzodning beshta bahosi: 3, 5, 4, 5, 3.
  Oʻrtachasi, medianasi va tarqoqligini toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Oʻrtacha 4, mediana 4, tarqoqlik 2.</b> Yigʻindi:
    3 + 5 + 4 + 5 + 3 = 20, va 20 ÷ 5 = 4. Saralaymiz: 3, 3, 4, 5, 5 —
    oʻrtadagisi 4. Tarqoqlik: 5 − 3 = 2.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Tarqoqlik</b><span>eng katta va eng kichik qiymat farqi; ingl.
    range</span></li>
  <li><b>Eng katta qiymat</b><span>maʼlumotdagi eng yuqori son; ingl.
    maximum</span></li>
  <li><b>Eng kichik qiymat</b><span>maʼlumotdagi eng past son; ingl.
    minimum</span></li>
  <li><b>Barqarorlik</b><span>natijalarning bir-biriga yaqinligi; ingl.
    consistency</span></li>
  <li><b>Yoyilganlik</b><span>qiymatlarning bir-biridan uzoqligi; ingl.
    spread</span></li>
  <li><b>Nuqtali diagramma</b><span>har bir qiymat nuqta bilan
    belgilangan chizma; ingl. dot plot</span></li>
  <li><b>Chetki son</b><span>qolganlaridan keskin farq qiladigan qiymat;
    ingl. outlier</span></li>
  <li><b>Oʻrta arifmetik</b><span>yigʻindi ÷ soni; ingl. mean</span></li>
  <li><b>Mediana</b><span>saralangan qatorning oʻrtasi; ingl.
    median</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Tarqoqlik = eng katta − eng kichik.</li>
    <li>U hech qachon manfiy boʻlmaydi; 0 boʻlsa — hamma qiymat bir
      xil.</li>
    <li>Oʻrtacha maʼlumot qayerdaligini, tarqoqlik esa qanchalik
      yoyilganini aytadi.</li>
    <li>Bir xil oʻrtachali ikki toʻplam butunlay boshqacha boʻlishi
      mumkin.</li>
    <li>Kichik tarqoqlik — barqarorlik; katta tarqoqlik —
      kutilmaganlik.</li>
    <li>Tarqoqlik faqat ikkita chekka songa qaraydi, shuning uchun
      chetki son uni ham buzadi.</li>
  </ul>
</div>
""",
    },
]
