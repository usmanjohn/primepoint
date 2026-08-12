# -*- coding: utf-8 -*-
"""Prime Math — darslar 54–56 (qoʻshish usuli, sistemali matnli masala, parabola).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt

  mashqlar — practice/management/commands/_practice_pm_54_56.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_54_56.py

⚠️ Kumulyativ chegaralar:
  • PM-54 — qoʻshish (yoʻqotish) usuli: qarama-qarshi koeffitsient → qoʻshish;
    bir xil koeffitsient → ayirish; kerak boʻlsa bitta yoki ikkala tenglamani
    koʻpaytirish. Ikki maxsus hol (0 = son → yechim yoʻq, 0 = 0 → cheksiz koʻp)
    PM-52 dan qaytariladi;
  • PM-55 — matndan sistema tuzish: belgila → ikki jumla, ikki tenglama →
    qulay usulni tanla → matnga qaytar. Oilalar: yigʻindi va farq, soni va puli,
    yosh, harakat (S = v·t, PM-35);
  • PM-56 — y = x² bilan tanishuv: jadval, parabola, uchi, simmetriya oʻqi,
    tarmoqlari; y = x² + c va y = −x². Kvadrat tenglama YECHILMAYDI, diskriminant
    YOʻQ, uchining formulasi YOʻQ — bu keyingi bloklar.
  • ⛔ Perimetr/yuza formulalari (PM-67, PM-68) YOʻQ; Pifagor (PM-64) YOʻQ;
    oʻrta arifmetik (PM-78) YOʻQ.
  • Faol ishlatiladi: sistema (PM-52), oʻrniga qoʻyish (PM-53), tenglama
    (PM-36, PM-37), matndan ifoda (PM-30, PM-38, PM-39), qavs ochish (PM-33),
    daraja (PM-12), ildiz (PM-13), manfiy son (PM-9…11), koordinata (PM-45),
    jadvaldan grafik (PM-48), y = kx + b (PM-49, PM-50), tezlik (PM-35).

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_54_56.py --author=prime
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
    # PM-54 — sistemani qoʻshish usuli bilan yechish
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-54: Sistemani qoʻshish usuli bilan yechish",
        "category": "math",
        "order": 54,
        "summary": (
            "Ikki tenglamani bir-biriga qoʻshib yoki ayirib, bitta nomaʼlumni "
            "butunlay yoʻqotish. Koeffitsientlar qarama-qarshi boʻlsa qoʻshamiz, "
            "bir xil boʻlsa ayiramiz, boʻlmasa avval koʻpaytirib olamiz."
        ),
        "stories": ["Ikki xil chipta"],
        "content": """
<h2>PM-54: Sistemani qoʻshish usuli bilan yechish</h2>

<p>Doʻkonda ikkita chek qoldi. Birinchisida: 4 ta daftar va 3 ta ruchka —
26 000 soʻm. Ikkinchisida: 4 ta daftar va 5 ta ruchka — 34 000 soʻm. Bitta
daftar necha pul?</p>

<p>PM-53 da bunday sistemani <b>oʻrniga qoʻyish</b> bilan yechardik: bir
nomaʼlumni ifodalab, ikkinchisiga tiqardik. Bu chekda esa ancha qisqa yoʻl bor.
Ikkala chekda ham <b>4 ta daftar</b> turibdi. Demak ikki chekning farqi faqat
ruchkalarniki: 2 ta ruchka — 8 000 soʻm. Mana shu — <b>qoʻshish usuli</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>ikki tenglamani qoʻshib yoki ayirib, bitta nomaʼlumni yoʻqotasiz;</li>
    <li>koeffitsientlar mos kelmasa, tenglamani butunlay koʻpaytirasiz;</li>
    <li>qaysi nomaʼlumni yoʻqotish qulayroq ekanini tanlaysiz;</li>
    <li>qoʻshish bilan oʻrniga qoʻyishning qay birini olishni bilasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Toʻrt qadam</span>
  <span class="pe-chip pe-chip--o">tenglashtir</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">qoʻsh (yoki ayir)</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">bitta nomaʼlumni yech</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--adv">qaytar va tekshir</span>
</div>

<h3>Nega ikki tenglamani qoʻshsa boʻladi?</h3>

<p>Tarozini eslang (PM-36). <b>x + y = 12</b> degani — chap tovoqchada x va y,
oʻng tovoqchada 12 turibdi va tarozi muvozanatda. <b>x − y = 4</b> — bu ikkinchi,
alohida muvozanatdagi tarozi.</p>

<p>Endi ikkinchi tarozining chap tovoqchasidagi hamma narsani birinchi tarozining
chap tovoqchasiga, oʻng tovoqchasidagini esa oʻng tovoqchasiga qoʻysak nima
boʻladi? Ikkala tomonga <b>teng ogʻirlik</b> qoʻshilgani uchun tarozi baribir
muvozanatda qoladi. Yaʼni:</p>

<div class="pe-ex">
  <p class="pe-ex__math">(x + y) + (x − y) = 12 + 4</p>
  <p class="pe-ex__uz">Ikki tenglamaning chap tomonlarini qoʻshdik, oʻng
  tomonlarini ham qoʻshdik.</p>
  <p class="pe-ex__why">Teng narsaga teng narsa qoʻshilsa, tenglik buzilmaydi —
  bu tenglamaning eng asosiy qoidasi.</p>
</div>

<p>Chap tomonda esa sehr boʻladi: <b>+y</b> va <b>−y</b> bir-birini yoʻq qiladi
(PM-10: <b>y − y = 0</b>). Qoladi <b>2x = 16</b>. Ikki nomaʼlumli sistemadan bir
nomaʼlumli oddiy tenglama chiqdi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 170" role="img" aria-label="Ikki tenglamani qoʻshish">
    <text class="pm-lbl" x="60" y="40">x</text>
    <text class="pm-lbl pm-lbl--hl" x="85" y="40">+ y</text>
    <text class="pm-lbl" x="140" y="40">=</text>
    <text class="pm-lbl" x="175" y="40">12</text>

    <text class="pm-lbl" x="60" y="78">x</text>
    <text class="pm-lbl pm-lbl--hl" x="85" y="78">− y</text>
    <text class="pm-lbl" x="140" y="78">=</text>
    <text class="pm-lbl" x="175" y="78">4</text>

    <line class="pm-ln" x1="81" y1="42" x2="115" y2="28"/>
    <line class="pm-ln" x1="81" y1="80" x2="115" y2="66"/>

    <text class="pm-lbl" x="30" y="78">+</text>
    <line class="pm-ln" x1="45" y1="95" x2="215" y2="95"/>

    <text class="pm-lbl pm-lbl--hl" x="60" y="125">2x</text>
    <text class="pm-lbl" x="140" y="125">=</text>
    <text class="pm-lbl pm-lbl--hl" x="175" y="125">16</text>

    <text class="pm-lbl" x="230" y="125">x = 8</text>
  </svg>
  <figcaption>+y va −y bir-birini yoʻq qildi. Qolgani — bitta nomaʼlumli
  tenglama.</figcaption>
</figure>

<h3>1-hol: koeffitsientlar qarama-qarshi — qoʻshamiz</h3>

<p>Eng oson hol. Bir nomaʼlum oldida <b>+</b>, ikkinchisida shuncha <b>−</b>
tursa, hech narsa tayyorlash kerak emas — toʻgʻridan qoʻshaveramiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + y = 12 <br> x − y = 4</span>
    <span class="pm-solve__why">Berilgan sistema. y oldida +1 va −1 —
    qarama-qarshi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x = 16</span>
    <span class="pm-solve__why">Ikki tenglamani qoʻshdik; y yoʻqoldi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = 8</span>
    <span class="pm-solve__why">Ikki tomonni 2 ga boʻldik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">8 + y = 12 → y = 4</span>
    <span class="pm-solve__why">x ni birinchi tenglamaga qaytardik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>8 + 4 = 12 ✓ va 8 − 4 = 4 ✓ — juftlik (8; 4) <b>ikkala</b> tenglamani ham
  bajardi.</p>
</div>

<h3>2-hol: koeffitsientlar bir xil — ayiramiz</h3>

<p>Chek masalasi aynan shunday edi: ikkala tenglamada ham <b>+2y</b> yoki
<b>4 ta daftar</b> turibdi. Bir xil narsani yoʻqotish uchun qoʻshish emas,
<b>ayirish</b> kerak.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x + 2y = 31 <br> x + 2y = 17</span>
    <span class="pm-solve__why">y oldida ikkalasida ham +2</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(3x + 2y) − (x + 2y) = 31 − 17</span>
    <span class="pm-solve__why">Ikkinchi tenglamani birinchisidan ayirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x = 14</span>
    <span class="pm-solve__why">3x − x = 2x, 2y − 2y = 0</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = 7</span>
    <span class="pm-solve__why">Ikki tomonni 2 ga boʻldik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">7 + 2y = 17 → y = 5</span>
    <span class="pm-solve__why">x ni ikkinchi (soddaroq) tenglamaga qoʻydik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>3 × 7 + 2 × 5 = 21 + 10 = 31 ✓ va 7 + 2 × 5 = 17 ✓</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Ayirishda <b>hamma</b> had ishorasini oʻzgartiradi</p>
  <p>Qavsni ayirayotganda ichidagi har bir had ishorasi almashadi (PM-33):
  <br>−(x + 2y) = <b>−x − 2y</b>, faqat −x + 2y emas.
  <br>Oʻng tomonni ham unutmang: 31 − 17 = 14, «31 − 17 = 24» emas. Eng koʻp xato
  aynan shu ikki joyda tugʻiladi.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Ayirishni yoqtirmasangiz</p>
  <p>Ayirish oʻrniga ikkinchi tenglamani <b>−1</b> ga koʻpaytirib, keyin
  qoʻshsangiz ham boʻladi: x + 2y = 17 dan −x − 2y = −17 chiqadi. Natija bir xil,
  lekin ishoralarni bir marta, xotirjam oʻzgartirasiz.</p>
</div>

<h3>3-hol: koeffitsientlar mos emas — avval koʻpaytiramiz</h3>

<p>Koʻpincha na qarama-qarshi, na bir xil koeffitsient boʻladi. Unda biz uni
<b>oʻzimiz yasaymiz</b>: tenglamani butunlay biror songa koʻpaytiramiz. Tenglama
oʻzgarmaydi — 2x + 6y = 24 bilan x + 3y = 12 bir xil narsani aytadi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + 3y = 12 <br> 4x − y = 22</span>
    <span class="pm-solve__why">y oldida +3 va −1 — mos emas</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4x − y = 22 | × 3</span>
    <span class="pm-solve__why">Ikkinchi tenglamani 3 ga koʻpaytiramiz, chunki
    −1 × 3 = −3</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">12x − 3y = 66</span>
    <span class="pm-solve__why">Har bir had koʻpaydi — oʻng tomon ham!</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">13x = 78</span>
    <span class="pm-solve__why">Birinchi tenglama bilan qoʻshdik: +3y va −3y
    yoʻqoldi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = 6</span>
    <span class="pm-solve__why">78 ÷ 13 = 6</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">6 + 3y = 12 → y = 2</span>
    <span class="pm-solve__why">x ni birinchi tenglamaga qaytardik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>6 + 3 × 2 = 12 ✓ va 4 × 6 − 2 = 24 − 2 = 22 ✓</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Koʻpaytirilsa — <b>butun</b> tenglama koʻpayadi</p>
  <p>«4x − y = 22 ni 3 ga koʻpaytiraman» degani 12x − 3y = <b>66</b> degani,
  12x − 3y = 22 emas. Tarozining faqat bitta tovoqchasini uch barobar
  ogʻirlashtirib boʻlmaydi — ikkalasi ham ogʻirlashadi.</p>
</div>

<h3>4-hol: ikkala tenglamani ham koʻpaytirish kerak</h3>

<p>Baʼzida bittasini koʻpaytirish yetmaydi. Unda ikkala koeffitsientning
<b>umumiy karralisini</b> olamiz (PM-8 dagi EKUK).</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x + 2y = 14 <br> 2x + 5y = 13</span>
    <span class="pm-solve__why">y oldida 2 va 5. EKUK = 10</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">15x + 10y = 70 <br> 4x + 10y = 26</span>
    <span class="pm-solve__why">Birinchisini 5 ga, ikkinchisini 2 ga
    koʻpaytirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">11x = 44</span>
    <span class="pm-solve__why">Ikkalasida ham +10y — demak <b>ayiramiz</b></span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = 4</span>
    <span class="pm-solve__why">44 ÷ 11 = 4</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3 × 4 + 2y = 14 → y = 1</span>
    <span class="pm-solve__why">12 + 2y = 14, demak 2y = 2</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>2 × 4 + 5 × 1 = 8 + 5 = 13 ✓ — ikkinchi tenglama ham bajarildi.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Qaysi nomaʼlumni yoʻqotgan qulay?</p>
  <p>Koeffitsientlarga qarang va <b>kichik umumiy karralini</b> tanlang.
  3x + 2y = 14 va 2x + 5y = 13 da x uchun EKUK 6, y uchun 10 — demak x ni
  yoʻqotgan biroz qulayroq. Agar biror nomaʼlum oldida <b>1</b> tursa, koʻpincha
  oʻrniga qoʻyish (PM-53) yanada tez boʻladi.</p>
</div>

<h3>Ikki maxsus hol — PM-52 ni eslaymiz</h3>

<p>Qoʻshgandan keyin <b>ikkala</b> nomaʼlum ham yoʻqolib qolsa, sistema bizga
javob emas, xabar bermoqda.</p>

<div class="pe-grid">
  <div class="pe-ex">
    <p class="pe-ex__math">x + y = 5 <br> x + y = 8 <br> ayiramiz: 0 = 3</p>
    <p class="pe-ex__uz">Yolgʻon tenglik. <b>Yechim yoʻq</b> — chiziqlar
    parallel.</p>
  </div>
  <div class="pe-ex">
    <p class="pe-ex__math">x + y = 5 <br> 2x + 2y = 10 <br> ayiramiz: 0 = 0</p>
    <p class="pe-ex__uz">Har doim toʻgʻri. <b>Cheksiz koʻp yechim</b> — bitta
    chiziq ikki marta yozilgan.</p>
  </div>
</div>

<h3>Matnli masala</h3>

<p><b>Doʻkondagi ikki chek.</b> Afsona 4 ta daftar va 3 ta ruchka uchun
26 000 soʻm toʻladi. Jasur oʻsha doʻkonda 4 ta daftar va 5 ta ruchka uchun
34 000 soʻm toʻladi. Bitta daftar va bitta ruchka necha soʻm turadi?</p>

<p><b>Nima soʻralyapti:</b> ikkita narx — bitta daftarniki va bitta ruchkaniki.</p>

<p><b>Reja:</b> daftar narxini <b>d</b>, ruchka narxini <b>r</b> deb belgilaymiz
(ikkalasi ham soʻmda). Har bir chek — bitta tenglama. Ikkala chekda ham
4 ta daftar bor, demak ayiramiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">4d + 3r = 26 000 <br> 4d + 5r = 34 000</span>
    <span class="pm-solve__why">Birinchi chek va ikkinchi chek</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2r = 8 000</span>
    <span class="pm-solve__why">Ikkinchisidan birinchisini ayirdik: 4d yoʻqoldi,
    34 000 − 26 000 = 8 000</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">r = 4 000</span>
    <span class="pm-solve__why">Bitta ruchka — 4 000 soʻm</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4d + 3 × 4 000 = 26 000</span>
    <span class="pm-solve__why">r ni birinchi chekka qaytardik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4d = 14 000</span>
    <span class="pm-solve__why">26 000 − 12 000 = 14 000</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">d = 3 500</span>
    <span class="pm-solve__why">Bitta daftar — 3 500 soʻm</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz — matnga qaytamiz</p>
  <p>Jasurning cheki: 4 × 3 500 + 5 × 4 000 = 14 000 + 20 000 = 34 000 ✓
  <br>Afsonaning cheki: 4 × 3 500 + 3 × 4 000 = 14 000 + 12 000 = 26 000 ✓
  <br><b>Javob:</b> daftar 3 500 soʻm, ruchka 4 000 soʻm.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Ikki chekning farqi 8 000 soʻm va farq atigi 2 ta ruchka — demak ruchka
  4 000 atrofida. Javob shu taxminga tushdi.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">4x − y = 22 | × 3 → 12x − 3y = 22</p>
  <p class="pe-fix__good">4x − y = 22 | × 3 → 12x − 3y = 66</p>
  <p class="pe-fix__why">Oʻng tomon koʻpaytirilmagan. Tenglamaning
  <b>ikkala</b> tomoni bir xil songa koʻpayadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">3x + 2y = 31 va x + 2y = 17 → qoʻshamiz: 4x + 4y = 48</p>
  <p class="pe-fix__good">3x + 2y = 31 va x + 2y = 17 → ayiramiz: 2x = 14</p>
  <p class="pe-fix__why">Koeffitsientlar <b>bir xil</b> boʻlsa qoʻshish hech
  narsani yoʻqotmaydi. Bir xil — ayiramiz, qarama-qarshi — qoʻshamiz.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">(3x + 2y) − (x + 2y) = 2x + 4y</p>
  <p class="pe-fix__good">(3x + 2y) − (x + 2y) = 2x</p>
  <p class="pe-fix__why">Ayirishda qavs ichidagi <b>har bir</b> hadning ishorasi
  almashadi: −x <b>−</b> 2y. Shunda 2y − 2y = 0 boʻladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">2x = 16 → x = 8. Javob: 8</p>
  <p class="pe-fix__good">x = 8, keyin y = 4. Javob: (8; 4)</p>
  <p class="pe-fix__why">Sistemaning yechimi — <b>juftlik</b>. Bitta nomaʼlumni
  topib toʻxtash — yarim ish.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Yeching: x + y = 10 va x − y = 2.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>(6; 4).</b> Qoʻshamiz: 2x = 12, x = 6. Keyin 6 + y = 10, y = 4.
    Tekshirish: 6 − 4 = 2 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Yeching: 2x + y = 13 va 3x − y = 12.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>(5; 3).</b> y oldida +1 va −1 — qoʻshamiz: 5x = 25, x = 5.
    2 × 5 + y = 13, demak y = 3. Tekshirish: 3 × 5 − 3 = 12 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Yeching: 4x + 3y = 23 va 4x − y = 3.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>(2; 5).</b> x oldida ikkalasida ham 4 — ayiramiz:
    3y − (−y) = 4y va 23 − 3 = 20, demak 4y = 20, y = 5. Keyin
    4x − 5 = 3, 4x = 8, x = 2. Tekshirish: 4 × 2 + 3 × 5 = 23 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Yeching: 3x + y = 14 va 2x − 3y = 2.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>(4; 2).</b> Birinchisini 3 ga koʻpaytiramiz: 9x + 3y = 42.
    Ikkinchisi bilan qoʻshamiz: 11x = 44, x = 4. Keyin 3 × 4 + y = 14,
    y = 2. Tekshirish: 2 × 4 − 3 × 2 = 2 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Yeching: 2x + 3y = 16 va 5x − 2y = 2.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>(2; 4).</b> y ning EKUK i 6: birinchisini 2 ga, ikkinchisini 3 ga
    koʻpaytiramiz — 4x + 6y = 32 va 15x − 6y = 6. Qoʻshamiz: 19x = 38, x = 2.
    Keyin 2 × 2 + 3y = 16, 3y = 12, y = 4. Tekshirish: 5 × 2 − 2 × 4 = 2 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Bozorda 2 kg olma va 3 kg nok 46 000 soʻm turadi.
  4 kg olma va 3 kg nok esa 62 000 soʻm. Bir kilogramm olma va bir kilogramm
  nok qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Olma 8 000 soʻm, nok 10 000 soʻm.</b> Ikkala hisobda ham 3 kg nok bor,
    demak ayiramiz: 2 kg olma = 62 000 − 46 000 = 16 000, yaʼni 1 kg olma
    8 000 soʻm. Keyin 2 × 8 000 + 3n = 46 000, 3n = 30 000, n = 10 000.
    Tekshirish: 4 × 8 000 + 3 × 10 000 = 32 000 + 30 000 = 62 000 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Tenglamalar sistemasi</b><span>bir vaqtda bajarilishi kerak boʻlgan
    tenglamalar; ingl. system of equations</span></li>
  <li><b>Qoʻshish usuli</b><span>tenglamalarni qoʻshib nomaʼlumni yoʻqotish;
    ingl. elimination method</span></li>
  <li><b>Nomaʼlumni yoʻqotish</b><span>uni tenglamadan butunlay chiqarib
    yuborish; ingl. to eliminate</span></li>
  <li><b>Koeffitsient</b><span>nomaʼlum oldidagi son; ingl. coefficient</span></li>
  <li><b>Qarama-qarshi sonlar</b><span>+3 va −3 kabi, yigʻindisi nol; ingl.
    opposite numbers</span></li>
  <li><b>Ekvivalent tenglama</b><span>koʻpaytirilgandan keyin ham xuddi shuni
    aytadigan tenglama; ingl. equivalent equation</span></li>
  <li><b>EKUK</b><span>eng kichik umumiy karrali; ingl. least common
    multiple</span></li>
  <li><b>Yechim juftligi</b><span>sistemani bajaradigan (x; y); ingl. solution
    pair</span></li>
  <li><b>Oʻrniga qoʻyish usuli</b><span>PM-53 dagi ikkinchi usul; ingl.
    substitution method</span></li>
  <li><b>Tekshirish</b><span>javobni ikkala tenglamaga qaytarib qoʻyish; ingl.
    check</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Bir xil — ayiramiz, qarama-qarshi — qoʻshamiz.</b> Maqsad bitta:
      nomaʼlumlardan biri yoʻqolsin.</li>
    <li><b>Koʻpaytirsangiz, butun tenglamani koʻpaytiring</b> — oʻng tomonni
      ham.</li>
    <li><b>Javob — juftlik (x; y)</b> va u <b>ikkala</b> tenglamani ham
      bajarishi shart.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-55 — sistema bilan yechiladigan matnli masalalar
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-55: Sistema bilan yechiladigan matnli masalalar",
        "category": "math",
        "order": 55,
        "summary": (
            "Matnda ikkita nomaʼlum boʻlsa, unda ikkita jumla ham bor. Har bir "
            "jumlani tenglamaga aylantirib, sistema tuzish va uni qulay usul "
            "bilan yechib, javobni matn tiliga qaytarish."
        ),
        "stories": ["Tovuq va quyon — qadimiy masala"],
        "content": """
<h2>PM-55: Sistema bilan yechiladigan matnli masalalar</h2>

<p>«Sinfda 28 oʻquvchi bor. Qizlar oʻgʻillardan 4 ta koʻp. Nechta qiz bor?»
Bu masalada bitta emas, <b>ikkita</b> nomaʼlum bor: qizlar soni ham, oʻgʻillar
soni ham nomaʼlum. Bitta harf bilan qiynalib boʻladi — ikkitasi bilan esa masala
oʻzi yechiladi.</p>

<p>PM-52 sistemaning nimaligini, PM-53 va PM-54 esa uni yechishning ikki usulini
oʻrgatdi. Endi eng muhim qismi: <b>matnni sistemaga aylantirish</b>. Yechish
texnika, tuzish esa — mahorat.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>ikki nomaʼlumni nomi va birligi bilan belgilaysiz;</li>
    <li>matndagi har bir jumlani bitta tenglamaga aylantirasiz;</li>
    <li>qoʻshish yoki oʻrniga qoʻyish — qulayrogʻini tanlaysiz;</li>
    <li>javobni sonlar bilan emas, <b>soʻzlar</b> bilan aytasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Toʻrt qadam</span>
  <span class="pe-chip pe-chip--s">belgila</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">ikki tenglama tuz</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">yech</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--adv">matnga qaytar</span>
</div>

<h3>1-qadam: belgilash — bu yerda yarim ish bajariladi</h3>

<p>Belgilash shunchaki «x deb olamiz» emas. Uchta narsa yozilishi kerak:
<b>nima</b>, <b>qanday birlikda</b>, va <b>nechta</b> nomaʼlum bor.</p>

<div class="pe-ex">
  <p class="pe-ex__math">q — qizlar soni (ta), oʻ — oʻgʻillar soni (ta)</p>
  <p class="pe-ex__uz">«Qizlar soni» — bu son, «qizlar» emas. Birligi — ta.</p>
  <p class="pe-ex__why">Birlik yozilmasa, keyinroq soʻm bilan ming soʻm, km bilan
  metr aralashib ketadi.</p>
</div>

<h3>2-qadam: har bir jumla — bitta tenglama</h3>

<p>Matnni jumlama-jumla oʻqing. Sonlar bor jumla — deyarli har doim tenglama.
Quyidagi jadval matn tilini matematika tiliga oʻgiradi (PM-30 ning davomi).</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Matnda shunday deyiladi</th><th>Matematikada</th><th>Misol</th></tr>
  <tr><td>jami 28 ta</td><td class="pm-word__sym">x + y = 28</td><td>ikki turdagi
    narsaning soni</td></tr>
  <tr><td>hammasi boʻlib 140 000 soʻm</td><td class="pm-word__sym">15 000x + 7 000y
    = 140 000</td><td>soni × narxi</td></tr>
  <tr><td>x, y dan 4 ta koʻp</td><td class="pm-word__sym">x − y = 4</td>
    <td>farq</td></tr>
  <tr><td>x, y dan 3 marta katta</td><td class="pm-word__sym">x = 3y</td>
    <td>karrali</td></tr>
  <tr><td>ikkalasining yigʻindisi 48</td><td class="pm-word__sym">x + y = 48</td>
    <td>yigʻindi</td></tr>
  <tr><td>bir-biriga qarab yurib uchrashdi</td>
    <td class="pm-word__sym">(v<sub>1</sub> + v<sub>2</sub>) × t = S</td>
    <td>harakat</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">«4 ta koʻp» va «4 marta koʻp» — butunlay boshqa narsa</p>
  <p>«4 ta koʻp» — <b>qoʻshish</b>: q = oʻ + 4. «4 marta koʻp» —
  <b>koʻpaytirish</b>: q = 4oʻ. Bu matematika xatosi emas, <b>oʻqish</b> xatosi —
  va imtihonda eng koʻp ochko shu yerda yoʻqoladi. Jumlani ovoz chiqarib oʻqing.</p>
</div>

<h3>1-masala: yigʻindi va farq</h3>

<p><b>Sinfda 28 oʻquvchi bor. Qizlar oʻgʻillardan 4 ta koʻp. Nechta qiz va nechta
oʻgʻil bor?</b></p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">Oʻgʻillar</span>
    <span class="pm-model__bar" style="width:42%">oʻ</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">Qizlar</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:56%">oʻ + 4</span>
  </div>
  <p class="pm-model__tot">Jami: oʻ + (oʻ + 4) = 28</p>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">q + oʻ = 28 <br> q − oʻ = 4</span>
    <span class="pm-solve__why">Birinchi jumla va ikkinchi jumla</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2q = 32</span>
    <span class="pm-solve__why">Qoʻshdik (PM-54): oʻ yoʻqoldi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">q = 16</span>
    <span class="pm-solve__why">32 ÷ 2 = 16</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">16 + oʻ = 28 → oʻ = 12</span>
    <span class="pm-solve__why">q ni birinchi tenglamaga qaytardik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Matnga qaytamiz</p>
  <p>16 + 12 = 28 ✓ va 16 − 12 = 4 ✓ <br><b>Javob:</b> sinfda 16 ta qiz va
  12 ta oʻgʻil bor. Faqat «16 va 12» emas — <b>nima</b> 16 ta ekanini ayting.</p>
</div>

<h3>2-masala: soni va puli — eng koʻp uchraydigan tur</h3>

<p><b>Teatrga 12 ta chipta olindi. Katta odam chiptasi 15 000 soʻm, bola
chiptasi 7 000 soʻm. Hammasiga 140 000 soʻm toʻlandi. Nechta katta va nechta
bola chiptasi olingan?</b></p>

<p>Bunday masalada har doim ikkita mutlaqo turli jumla boʻladi: bittasi
<b>sonlar</b> haqida, ikkinchisi <b>pullar</b> haqida. Ularni aralashtirmang.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">k + b = 12</span>
    <span class="pm-solve__why">Chiptalar <b>soni</b>: 12 ta</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">15 000k + 7 000b = 140 000</span>
    <span class="pm-solve__why">Chiptalar <b>puli</b>: soni × narxi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">b = 12 − k</span>
    <span class="pm-solve__why">Birinchi tenglamada koeffitsient 1 — oʻrniga
    qoʻyish qulay (PM-53)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">15 000k + 7 000(12 − k) = 140 000</span>
    <span class="pm-solve__why">b ning oʻrniga qoʻydik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">15 000k + 84 000 − 7 000k = 140 000</span>
    <span class="pm-solve__why">Qavsni ochdik (PM-33)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">8 000k = 56 000</span>
    <span class="pm-solve__why">Oʻxshash hadlar; 140 000 − 84 000 = 56 000</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">k = 7, b = 5</span>
    <span class="pm-solve__why">56 000 ÷ 8 000 = 7; keyin 12 − 7 = 5</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Matnga qaytamiz</p>
  <p>7 × 15 000 = 105 000 soʻm, 5 × 7 000 = 35 000 soʻm.
  <br>105 000 + 35 000 = 140 000 ✓ va 7 + 5 = 12 ✓
  <br><b>Javob:</b> 7 ta katta chipta va 5 ta bola chiptasi.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Soni va puli bitta tenglamaga sigʻmaydi</p>
  <p>«k + b = 140 000» degan tenglama koʻp yoziladi — bu <b>chiptalar sonini
  soʻmga tenglashtirish</b>. 12 ta chipta 140 000 soʻmga teng emas: 12 ta chipta
  140 000 soʻm <b>turadi</b>. Soni alohida tenglama, puli alohida tenglama.</p>
</div>

<h3>3-masala: yosh — «necha marta» ishlaydigan joy</h3>

<p><b>Otasi bilan Bekzodning yoshi birgalikda 48 ni tashkil qiladi. Otasi
Bekzoddan 3 marta katta. Ular necha yoshda?</b></p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">o + b = 48 <br> o = 3b</span>
    <span class="pm-solve__why">Yigʻindi va «3 marta katta»</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3b + b = 48</span>
    <span class="pm-solve__why">o ning oʻrniga 3b qoʻydik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4b = 48</span>
    <span class="pm-solve__why">Oʻxshash hadlarni ixchamladik (PM-32)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">b = 12, o = 36</span>
    <span class="pm-solve__why">48 ÷ 4 = 12; keyin 3 × 12 = 36</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Matnga qaytamiz</p>
  <p>12 + 36 = 48 ✓ va 36 ÷ 12 = 3 ✓ — otasi haqiqatan 3 marta katta.
  <br><b>Javob:</b> Bekzod 12 yoshda, otasi 36 yoshda.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Ota oʻgʻildan 3 marta katta boʻlsa, ularning yoshi 4 ta bola yoshiga
  teng. 48 ni 4 ga boʻlsak, bola 12 atrofida chiqadi — javob mantiqiy.</span>
</div>

<h3>4-masala: harakat — bir-biriga qarab</h3>

<p><b>A va B shaharlari orasi 240 km. Ikki mashina bir vaqtda bir-biriga qarab
yoʻlga chiqdi va 2 soatdan keyin uchrashdi. Birinchi mashinaning tezligi
ikkinchisinikidan 10 km/soat ortiq. Har birining tezligi qancha?</b></p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 140" role="img" aria-label="Ikki mashina bir-biriga qarab">
    <line class="pm-ln pm-ln--dash" x1="30" y1="40" x2="290" y2="40"/>
    <text class="pm-lbl pm-lbl--hl" x="135" y="32">240 km</text>

    <line class="pm-ln" x1="30" y1="90" x2="290" y2="90"/>
    <circle class="pm-pt" cx="30" cy="90" r="5"/>
    <circle class="pm-pt" cx="290" cy="90" r="5"/>

    <line class="pm-ln pm-ln--hl" x1="55" y1="70" x2="108" y2="70"/>
    <polygon class="pm-pt" points="108,64 120,70 108,76"/>
    <text class="pm-lbl" x="48" y="60">tezroq</text>

    <line class="pm-ln pm-ln--hl" x1="265" y1="70" x2="212" y2="70"/>
    <polygon class="pm-pt" points="212,64 200,70 212,76"/>
    <text class="pm-lbl" x="215" y="60">sekinroq</text>

    <line class="pm-ln pm-ln--dash" x1="160" y1="55" x2="160" y2="105"/>
    <text class="pm-lbl" x="22" y="112">A</text>
    <text class="pm-lbl" x="282" y="112">B</text>
    <text class="pm-lbl pm-lbl--hl" x="108" y="128">2 soatda uchrashdi</text>
  </svg>
  <figcaption>Ikkalasi birgalikda 240 km ni bosdi — demak soatiga 120 km.</figcaption>
</figure>

<p>Kalit gʻoya: bir-biriga qarab yurganda ikkalasi birgalikda butun masofani
bosib oʻtadi. 2 soatda 240 km bosilgan boʻlsa, bir soatda ikkalasi birga
240 ÷ 2 = 120 km bosgan — bu ikki tezlikning <b>yigʻindisi</b> (PM-35).</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">v<sub>1</sub> + v<sub>2</sub> = 120</span>
    <span class="pm-solve__why">240 ÷ 2 = 120 — soatlik umumiy yaqinlashish</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">v<sub>1</sub> − v<sub>2</sub> = 10</span>
    <span class="pm-solve__why">«10 km/soat ortiq»</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2v<sub>1</sub> = 130</span>
    <span class="pm-solve__why">Qoʻshdik — v<sub>2</sub> yoʻqoldi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">v<sub>1</sub> = 65, v<sub>2</sub> = 55</span>
    <span class="pm-solve__why">130 ÷ 2 = 65; keyin 120 − 65 = 55</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Matnga qaytamiz</p>
  <p>2 soatda birinchisi 65 × 2 = 130 km, ikkinchisi 55 × 2 = 110 km bosdi.
  130 + 110 = 240 ✓ va 65 − 55 = 10 ✓
  <br><b>Javob:</b> tezliklar 65 km/soat va 55 km/soat.</p>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Ikkinchi tenglama <b>yangi</b> maʼlumot bermasa</p>
  <p>«Jami 20 ta» va «ikkalasining soni birga 20 ta» — bu bitta jumlaning ikki
  xil aytilishi. Bunday ikki tenglamadan sistema chiqmaydi (PM-52 dagi «cheksiz
  koʻp yechim» holi). Har bir tenglama matndan <b>boshqa</b> jumlani olishi
  kerak.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">x — chiptalar</p>
  <p class="pe-fix__good">k — katta odam chiptalari <b>soni</b> (ta)</p>
  <p class="pe-fix__why">«Chiptalar» — narsa, tenglamaga narsa emas, <b>son</b>
  yoziladi. Nomi va birligi boʻlmagan belgilash keyin albatta adashtiradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Qizlar oʻgʻillardan 4 ta koʻp → q = 4oʻ</p>
  <p class="pe-fix__good">Qizlar oʻgʻillardan 4 ta koʻp → q = oʻ + 4</p>
  <p class="pe-fix__why">«4 ta koʻp» — qoʻshish. Koʻpaytirish «4 <b>marta</b>
  koʻp» deganda boʻladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">12 ta chipta, jami 140 000 soʻm → k + b = 140 000</p>
  <p class="pe-fix__good">k + b = 12 va 15 000k + 7 000b = 140 000</p>
  <p class="pe-fix__why">Chiptalar <b>soni</b> soʻmga teng boʻlolmaydi. Soni —
  bitta tenglama, puli — boshqa tenglama.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Javob: 7 va 5</p>
  <p class="pe-fix__good">Javob: 7 ta katta chipta va 5 ta bola chiptasi</p>
  <p class="pe-fix__why">Masala soʻz bilan soʻralgan — javob ham soʻz bilan
  beriladi. Aks holda qaysi son nimaligi noaniq qoladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Ikki sonning yigʻindisi 54, farqi 12. Bu sonlarni
  toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>33 va 21.</b> x + y = 54, x − y = 12. Qoʻshamiz: 2x = 66, x = 33.
    Keyin y = 54 − 33 = 21. Tekshirish: 33 − 21 = 12 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Sherbek 9 ta narsa oldi: daftar 2 500 soʻmdan,
  ruchka 1 500 soʻmdan. Hammasiga 19 500 soʻm toʻladi. Nechta daftar oldi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>6 ta daftar va 3 ta ruchka.</b> d + r = 9 va 2 500d + 1 500r = 19 500.
    r = 9 − d ni qoʻysak: 2 500d + 13 500 − 1 500d = 19 500, 1 000d = 6 000,
    d = 6. Tekshirish: 6 × 2 500 + 3 × 1 500 = 15 000 + 4 500 = 19 500 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Dilnoza onasidan 24 yosh kichik. Ikkalasining yoshi
  birgalikda 58. Ular necha yoshda?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Dilnoza 17 yoshda, onasi 41 yoshda.</b> o + d = 58, o − d = 24.
    Qoʻshamiz: 2o = 82, o = 41. Keyin d = 58 − 41 = 17.
    Tekshirish: 41 − 17 = 24 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Ikki shahar orasi 300 km. Ikki poyezd bir-biriga
  qarab yoʻlga chiqdi va 3 soatdan keyin uchrashdi. Biri ikkinchisidan
  20 km/soat tez yurgan. Tezliklarini toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>60 km/soat va 40 km/soat.</b> Birgalikda soatiga 300 ÷ 3 = 100 km
    yaqinlashadi, demak v₁ + v₂ = 100 va v₁ − v₂ = 20. Qoʻshamiz: 2v₁ = 120,
    v₁ = 60, v₂ = 40. Tekshirish: (60 + 40) × 3 = 300 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Bekzod 30 ta konvert oldi. Kattasi 900 soʻmdan,
  kichigi 500 soʻmdan. Hammasiga 19 400 soʻm ketdi. Nechtadan olgan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>11 ta katta va 19 ta kichik konvert.</b> k + s = 30 va
    900k + 500s = 19 400. s = 30 − k ni qoʻysak: 900k + 15 000 − 500k = 19 400,
    400k = 4 400, k = 11. Tekshirish: 11 × 900 + 19 × 500 = 9 900 + 9 500
    = 19 400 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Sinf kassasiga 24 oʻquvchi pul toʻpladi: oʻgʻillar
  3 000 soʻmdan, qizlar 2 000 soʻmdan. Jami 58 000 soʻm yigʻildi. Sinfda nechta
  oʻgʻil bor?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>10 ta oʻgʻil va 14 ta qiz.</b> oʻ + q = 24 va 3 000oʻ + 2 000q
    = 58 000. q = 24 − oʻ ni qoʻysak: 3 000oʻ + 48 000 − 2 000oʻ = 58 000,
    1 000oʻ = 10 000, oʻ = 10. Tekshirish: 10 × 3 000 + 14 × 2 000 = 30 000
    + 28 000 = 58 000 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Matnli masala</b><span>soʻz bilan berilgan masala; ingl. word
    problem</span></li>
  <li><b>Belgilash</b><span>nomaʼlumga harf va birlik berish; ingl. defining the
    variables</span></li>
  <li><b>Sistema tuzish</b><span>matndan ikki tenglama yozish; ingl. setting up a
    system</span></li>
  <li><b>Shart</b><span>masaladagi berilgan maʼlumot; ingl. condition</span></li>
  <li><b>Yigʻindi</b><span>qoʻshish natijasi; ingl. sum</span></li>
  <li><b>Farq</b><span>ayirish natijasi; ingl. difference</span></li>
  <li><b>…marta koʻp</b><span>koʻpaytirish; ingl. times as many</span></li>
  <li><b>…ta koʻp</b><span>qoʻshish; ingl. more than</span></li>
  <li><b>Umumiy qiymat</b><span>soni × narxi; ingl. total cost</span></li>
  <li><b>Yaqinlashish tezligi</b><span>qarama-qarshi harakatda tezliklar
    yigʻindisi; ingl. closing speed</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Ikki nomaʼlum — ikki tenglama.</b> Har bir tenglama matnning
      <b>boshqa</b> jumlasidan chiqadi.</li>
    <li><b>Soni bilan puli aralashmaydi.</b> Bittasi «nechta», ikkinchisi
      «qancha soʻm».</li>
    <li><b>Javob soʻz bilan aytiladi</b> va matnning oʻziga qaytarib
      tekshiriladi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-56 — parabola bilan tanishuv
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-56: Parabola bilan tanishuv: y = x²",
        "category": "math",
        "order": 56,
        "summary": (
            "Birinchi toʻgʻri chiziq boʻlmagan grafik: y = x². Jadval tuzish, "
            "parabolani chizish, uchi va simmetriya oʻqini topish, y = x² + c va "
            "y = −x² ni farqlash."
        ),
        "stories": ["Toʻpning yoʻli"],
        "content": """
<h2>PM-56: Parabola bilan tanishuv: y = x²</h2>

<p>Bolakay toʻpni tepdi. Toʻp yuqoriga koʻtarildi, bir lahza havoda turdi va
pastga tushdi. Uning yoʻlini havoda chizib koʻrsangiz — toʻgʻri chiziq emas,
silliq egri chiziq chiqadi. Favvora suvi ham, tashlangan tosh ham xuddi shu
shaklda uchadi.</p>

<p>PM-49 dan beri biz faqat <b>toʻgʻri chiziq</b>lar bilan ishladik: y = kx + b.
Bu darsda birinchi marta chiziq egiladi. Uning nomi — <b>parabola</b>, va eng
sodda tenglamasi bor-yoʻgʻi <b>y = x²</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>y = x² uchun jadval tuzib, parabolani chizasiz;</li>
    <li>uchi, simmetriya oʻqi va tarmoqlarini nomlaysiz;</li>
    <li>y hech qachon manfiy boʻlmasligini tushuntirasiz;</li>
    <li>y = x² + c va y = −x² grafikni qanday oʻzgartirishini bilasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qoida</span>
  <span class="pe-chip pe-chip--s">x</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">kvadratga koʻtar</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">y = x²</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--adv">y ≥ 0 har doim</span>
</div>

<h3>Jadvaldan boshlaymiz</h3>

<p>PM-48 dagi tartib oʻzgarmaydi: x ni tanlaymiz, qoidani qoʻllaymiz, y ni
yozamiz. Faqat endi qoida «×3 qilib 1 qoʻsh» emas, «oʻzini oʻziga koʻpaytir».</p>

<div class="pe-table-wrap"><table>
  <tr><th>x</th><td>−3</td><td>−2</td><td>−1</td><td>0</td><td>1</td><td>2</td>
    <td>3</td></tr>
  <tr><th>y = x²</th><td>9</td><td>4</td><td>1</td><td>0</td><td>1</td><td>4</td>
    <td>9</td></tr>
</table></div>

<p>Jadvalda darrov ikkita narsa koʻzga tashlanadi.</p>

<p><b>Birinchisi:</b> pastki qatorda bitta ham manfiy son yoʻq. Chunki manfiy
sonni manfiyga koʻpaytirsak musbat chiqadi (PM-11): (−3)² = (−3) × (−3) = 9.</p>

<p><b>Ikkinchisi:</b> jadval oʻrtasidan <b>koʻzgudek</b> takrorlanadi. −2 ham,
+2 ham 4 ni beradi. −3 ham, +3 ham 9 ni beradi. Demak grafik ham simmetrik
boʻlishi kerak.</p>

<div class="pe-call pe-uz">
  <p class="pe-call__t">(−3)² = 9, «−9» emas</p>
  <p>Kvadrat butun songa tegishli: (−3)² degani (−3) × (−3). Agar minus kvadratdan
  <b>tashqarida</b> tursa — −3² — u holda avval 3² = 9 hisoblanadi va javob −9
  boʻladi. Qavs bor-yoʻqligi butun javobni oʻzgartiradi.</p>
</div>

<h3>Nuqtalarni qoʻyamiz — va chiziq egiladi</h3>

<p>Jadvaldagi yettita juftlikni koordinata tekisligiga qoʻyamiz (PM-45):
(−3; 9), (−2; 4), (−1; 1), (0; 0), (1; 1), (2; 4), (3; 9).</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 252" role="img" aria-label="y = x kvadrat parabolasi">
    <line class="pm-ln" x1="30" y1="210" x2="305" y2="210"/>
    <line class="pm-ln" x1="160" y1="225" x2="160" y2="20"/>
    <line class="pm-ln pm-ln--dash" x1="160" y1="225" x2="160" y2="20"/>

    <polyline class="pm-ln pm-ln--hl" fill="none"
      points="40,30 60,85 80,130 100,165 120,190 140,205 160,210 180,205
              200,190 220,165 240,130 260,85 280,30"/>

    <circle class="pm-pt" cx="40" cy="30" r="4"/>
    <circle class="pm-pt" cx="80" cy="130" r="4"/>
    <circle class="pm-pt" cx="120" cy="190" r="4"/>
    <circle class="pm-pt" cx="160" cy="210" r="4"/>
    <circle class="pm-pt" cx="200" cy="190" r="4"/>
    <circle class="pm-pt" cx="240" cy="130" r="4"/>
    <circle class="pm-pt" cx="280" cy="30" r="4"/>

    <text class="pm-lbl" x="34" y="225">−3</text>
    <text class="pm-lbl" x="74" y="225">−2</text>
    <text class="pm-lbl" x="114" y="225">−1</text>
    <text class="pm-lbl" x="196" y="225">1</text>
    <text class="pm-lbl" x="236" y="225">2</text>
    <text class="pm-lbl" x="276" y="225">3</text>
    <text class="pm-lbl" x="166" y="135">4</text>
    <text class="pm-lbl" x="166" y="35">9</text>
    <text class="pm-lbl pm-lbl--hl" x="290" y="45">y = x²</text>
    <text class="pm-lbl pm-lbl--hl" x="128" y="246">uchi (0; 0)</text>
  </svg>
  <figcaption>Nuqtalarni silliq egri chiziq bilan tutashtiramiz — parabola
  chiqadi. y oʻqi uni ikkiga teng boʻladi.</figcaption>
</figure>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Ikki nuqta yetmaydi</p>
  <p>Toʻgʻri chiziq uchun ikkita nuqta yetardi (PM-49). Parabola uchun
  <b>kamida beshta</b>, uchidan ikki tomonga bir xil miqdorda, kerak. Ikki nuqta
  qoʻyib chizgʻich bilan tutashtirsangiz, parabola oʻrniga notoʻgʻri toʻgʻri
  chiziq chiqadi.</p>
</div>

<h3>Parabolaning uch qismi</h3>

<div class="pe-grid">
  <div class="pe-ex">
    <p class="pe-ex__math">Uchi</p>
    <p class="pe-ex__uz">Eng past nuqta — (0; 0). Egri chiziq shu yerda burilib,
    yana koʻtariladi.</p>
  </div>
  <div class="pe-ex">
    <p class="pe-ex__math">Simmetriya oʻqi</p>
    <p class="pe-ex__uz">y oʻqi. Grafikni shu chiziq boʻylab buklasangiz, ikki
    yarmi ustma-ust tushadi.</p>
  </div>
  <div class="pe-ex">
    <p class="pe-ex__math">Tarmoqlari</p>
    <p class="pe-ex__uz">Uchidan yuqoriga ketgan ikkita qanot. Ikkalasi ham
    yuqoriga qaragan.</p>
  </div>
</div>

<p>Yana bir muhim kuzatish: parabola <b>tik boʻlib boradi</b>. x ni 1 dan 2 ga
oshirsak y 1 dan 4 ga (3 ga) oʻsadi; 2 dan 3 ga oshirsak y 4 dan 9 ga (5 ga)
oʻsadi. Toʻgʻri chiziqda oʻsish har doim bir xil edi (PM-49 dagi k), bu yerda esa
oʻsish ham oʻsib boradi. Kvadratning butun mohiyati shunda.</p>

<h3>y = x² + c: grafik yuqoriga koʻchadi</h3>

<p>Endi har bir y ga 2 ni qoʻshamiz: <b>y = x² + 2</b>.</p>

<div class="pe-table-wrap"><table>
  <tr><th>x</th><td>−2</td><td>−1</td><td>0</td><td>1</td><td>2</td></tr>
  <tr><th>y = x²</th><td>4</td><td>1</td><td>0</td><td>1</td><td>4</td></tr>
  <tr><th>y = x² + 2</th><td>6</td><td>3</td><td>2</td><td>3</td><td>6</td></tr>
</table></div>

<p>Har bir nuqta aynan <b>2 birlik yuqoriga</b> koʻchdi. Shakli oʻzgarmadi,
faqat oʻrni oʻzgardi — uchi endi (0; 2) da. Bu PM-50 dagi <b>b</b> ning aynan
oʻzi: qoʻshimcha son grafikni koʻtaradi, <b>−3</b> boʻlsa tushiradi.</p>

<h3>y = −x²: parabola agʻdariladi</h3>

<p>Endi har bir y ning ishorasini almashtiramiz: <b>y = −x²</b>. x = 2 boʻlsa
y = −4, x = −3 boʻlsa y = −9. Endi bitta ham musbat y yoʻq.</p>

<p>Grafik xuddi oʻsha parabola, lekin x oʻqi boʻylab agʻdarilgan: tarmoqlari
<b>pastga</b> qaraydi va uchi (0; 0) endi eng past emas, eng <b>baland</b>
nuqta.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 200" role="img" aria-label="Toʻpning yoʻli — pastga qaragan parabola">
    <line class="pm-ln" x1="20" y1="170" x2="300" y2="170"/>
    <polyline class="pm-ln pm-ln--hl" fill="none"
      points="40,170 70,113 100,72 130,48 160,40 190,48 220,72 250,113 280,170"/>
    <circle class="pm-pt" cx="40" cy="170" r="5"/>
    <circle class="pm-pt" cx="160" cy="40" r="5"/>
    <circle class="pm-pt" cx="280" cy="170" r="5"/>
    <line class="pm-ln pm-ln--dash" x1="160" y1="40" x2="160" y2="170"/>
    <text class="pm-lbl" x="22" y="188">tepildi</text>
    <text class="pm-lbl pm-lbl--hl" x="118" y="30">eng baland nuqta</text>
    <text class="pm-lbl" x="250" y="188">tushdi</text>
  </svg>
  <figcaption>Toʻpning yoʻli — pastga qaragan parabola. Koʻtarilish va tushish
  bir xil shaklda.</figcaption>
</figure>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Ishoraga qarab shaklni aytish</p>
  <p>x² oldida <b>musbat</b> son tursa (y = x², y = 2x²) — tarmoqlar
  <b>yuqoriga</b>, uchi eng past nuqta. <b>Manfiy</b> tursa (y = −x²) —
  tarmoqlar <b>pastga</b>, uchi eng baland nuqta. Grafikni chizmasdan turib ham
  shuni ayta olasiz.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Tormoz yoʻli.</b> Haydovchilik qoidalarida oddiy taxminiy qoida bor:
mashinaning tormoz yoʻli (metrda) tezlikning oʻndan biri kvadratiga teng.
Yaʼni <b>s = (v ÷ 10)²</b>, bunda v — km/soatdagi tezlik.</p>

<p>Sherbekning otasi shahar ichida 40 km/soat bilan ketyapti. Yoʻlda esa
80 km/soat bilan. Ikki holda tormoz yoʻli qancha va u necha marta farq
qiladi?</p>

<p><b>Nima soʻralyapti:</b> ikkita masofa va ularning necha marta farq qilishi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">s = (40 ÷ 10)² = 4² = 16</span>
    <span class="pm-solve__why">40 km/soatda tormoz yoʻli 16 metr</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">s = (80 ÷ 10)² = 8² = 64</span>
    <span class="pm-solve__why">80 km/soatda tormoz yoʻli 64 metr</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">64 ÷ 16 = 4</span>
    <span class="pm-solve__why">Tezlik 2 marta oshdi, tormoz yoʻli 4 marta
    oshdi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>16 × 4 = 64 ✓. Sabab kvadratda: (2v ÷ 10)² — ichidagi son 2 marta katta
  boʻlsa, kvadrati 2 × 2 = 4 marta katta boʻladi.</p>
</div>

<p>Mana shuning uchun tezlikni «bir oz» oshirish xavfli. Chiziqli boʻlganda
16 dan 32 ga chiqardi; parabolada esa 64 ga chiqadi. <b>y = x² chiziqdan
tezroq oʻsadi</b> — va bu grafikda ochiq koʻrinib turibdi.</p>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>100 km/soatda? (100 ÷ 10)² = 10² = 100 metr — bir futbol maydonining
  uzunligi.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">(−4)² = −16</p>
  <p class="pe-fix__good">(−4)² = 16</p>
  <p class="pe-fix__why">Manfiy son manfiyga koʻpaysa musbat chiqadi (PM-11).
  Shuning uchun y = x² grafigi hech qachon x oʻqidan pastga tushmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">y = x² grafigi — toʻgʻri chiziq</p>
  <p class="pe-fix__good">y = x² grafigi — parabola, egri chiziq</p>
  <p class="pe-fix__why">Toʻgʻri chiziq faqat y = kx + b da chiqadi. Bu yerda
  oʻsish teng emas: 1, 3, 5 — shuning uchun chiziq egiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">y = x² da y = 25 boʻlsa, x = 5</p>
  <p class="pe-fix__good">y = 25 boʻlsa, x = 5 <b>yoki</b> x = −5</p>
  <p class="pe-fix__why">Parabola simmetrik: bitta y ga ikkita x toʻgʻri keladi.
  Faqat uchida — y = 0 da — bitta x boʻladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">x 2 marta oshsa, y ham 2 marta oshadi</p>
  <p class="pe-fix__good">x 2 marta oshsa, y <b>4</b> marta oshadi</p>
  <p class="pe-fix__why">3² = 9, 6² = 36 — 4 marta. Kvadratda oʻsish ham
  kvadratga koʻtariladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. y = x² boʻlsa, x = −5 da y qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>25.</b> (−5)² = (−5) × (−5) = 25. Manfiy son kvadratga koʻtarilganda
    musbat boʻladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Quyidagi nuqtalardan qaysilari y = x² grafigida
  yotadi: (3; 9), (−4; 16), (2; −4), (5; 10)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>(3; 9) va (−4; 16).</b> 3² = 9 ✓ va (−4)² = 16 ✓. (2; −4) yotmaydi,
    chunki 2² = 4, −4 emas — parabolada manfiy y yoʻq. (5; 10) ham yotmaydi:
    5² = 25, 10 emas (bu yerda kvadrat oʻrniga 2 ga koʻpaytirilgan).</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. y = x² grafigida y = 49 boʻlgan nuqtalarni toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>(7; 49) va (−7; 49).</b> 7² = 49 va (−7)² = 49. Simmetriya tufayli
    ikkita nuqta boʻladi — biri y oʻqining oʻng tomonida, biri chapida.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. y = x² + 3 grafigining uchi qayerda va x = 2 da y
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Uchi (0; 3), x = 2 da y = 7.</b> Har bir nuqta 3 birlik yuqoriga
    koʻchgan. x = 2 da: 2² + 3 = 4 + 3 = 7.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. y = −x² grafigining tarmoqlari qayoqqa qaraydi va
  x = 3 da y qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Pastga qaraydi; y = −9.</b> Avval 3² = 9 hisoblanadi, keyin minus
    qoʻyiladi: −9. Uchi (0; 0) endi eng baland nuqta.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Tormoz yoʻli s = (v ÷ 10)² formulasi bilan
  hisoblanadi. Mashina 30 km/soat va 90 km/soat bilan ketganda tormoz yoʻli
  qancha boʻladi va necha marta farq qiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>9 metr va 81 metr, 9 marta farq qiladi.</b> (30 ÷ 10)² = 3² = 9 va
    (90 ÷ 10)² = 9² = 81. 81 ÷ 9 = 9. Tezlik 3 marta oshdi, tormoz yoʻli esa
    3 × 3 = 9 marta oshdi. Tekshirish: 9 × 9 = 81 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Parabola</b><span>y = x² koʻrinishidagi funksiyaning egri grafigi;
    ingl. parabola</span></li>
  <li><b>Kvadrat funksiya</b><span>x kvadratga koʻtariladigan qoida; ingl.
    quadratic function</span></li>
  <li><b>Uchi</b><span>parabolaning burilish nuqtasi; ingl. vertex</span></li>
  <li><b>Simmetriya oʻqi</b><span>grafikni ikki teng yarimga boʻladigan chiziq;
    ingl. axis of symmetry</span></li>
  <li><b>Tarmoqlar</b><span>uchidan ketgan ikki qanot; ingl. branches</span></li>
  <li><b>Egri chiziq</b><span>toʻgʻri boʻlmagan chiziq; ingl. curve</span></li>
  <li><b>Kvadratga koʻtarish</b><span>sonni oʻziga koʻpaytirish; ingl.
    squaring</span></li>
  <li><b>Koʻchish</b><span>grafikning yuqoriga yoki pastga siljishi; ingl.
    shift</span></li>
  <li><b>Chiziqli funksiya</b><span>y = kx + b, grafigi toʻgʻri chiziq; ingl.
    linear function</span></li>
  <li><b>Tormoz yoʻli</b><span>tormozdan toʻxtaguncha bosilgan masofa; ingl.
    braking distance</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>y = x² grafigi — parabola, toʻgʻri chiziq emas.</b> Kamida beshta
      nuqta qoʻyib, silliq tutashtiring.</li>
    <li><b>y hech qachon manfiy emas</b> va grafik y oʻqiga nisbatan
      simmetrik — bitta y ga ikkita x.</li>
    <li><b>x² oldidagi ishora shaklni aytadi:</b> musbat — tarmoqlar yuqoriga,
      manfiy — pastga.</li>
  </ul>
</div>
""",
    },
]
