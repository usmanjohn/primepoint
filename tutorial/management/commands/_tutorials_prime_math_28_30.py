# -*- coding: utf-8 -*-
"""Prime Math — PM-28 (Blok B yakuni) va PM-29–30 (Blok C boshlanishi).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt

Uchta oyoq birga yoziladi:
  mashqlar — practice/management/commands/_practice_pm_28_30.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_28_30.py

⚠️ Kumulyativ chegaralar (Blok C juda zich, shuning uchun aniq boʻlinadi):
  • PM-28 — nisbat (PM-27) ustiga quriladi. HARF YOʻQ: nomaʼlum had «?» bilan
    belgilanadi, chunki harf PM-29 da kiritiladi;
  • PM-29 — harfning oʻzi: nomaʼlum va oʻzgaruvchi, yozuv qoidalari (3a, a²,
    a/2). Eng sodda ifodalar tuziladi (12n), lekin murakkab soʻz oʻgirishlari
    («dan 3 marta koʻp», qavsli iboralar) PM-30 ning ishi;
  • PM-30 — matndan ifoda tuzish, pm-word jadvali bilan. Ifodaga son qoʻyib
    qiymat hisoblash PM-31 da toʻliq ochiladi — bu yerda faqat bir-ikki
    bevosita hisob bor;
  • oʻxshash hadlarni ixchamlash (PM-32), qavs ochish (PM-33), formula (PM-35)
    va tenglama yechish (PM-36) bu uch darsda YOʻQ. PM-30 da qavs faqat
    YOZILADI, ochilmaydi.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_28_30.py --author=prime
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
    # PM-28 — proporsiya, masshtab, toʻgʻri va teskari proporsionallik
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-28: Proporsiya, masshtab, toʻgʻri va teskari proporsionallik",
        "category": "math",
        "order": 28,
        "summary": (
            "Ikki teng nisbat — proporsiya, va uning asosiy xossasi. Xaritadagi "
            "masshtabni oʻqish, toʻgʻri proporsionallikni teskarisidan ajratish va "
            "«bir birlik» usuli bilan hisoblash."
        ),
        "stories": ["Xaritadagi ikki santimetr"],
        "content": """
<h2>PM-28: Proporsiya, masshtab, toʻgʻri va teskari proporsionallik</h2>

<p>Bozorda 5 kilogramm olma 60 000 soʻm turibdi. Sizga 8 kilogramm kerak. Sotuvchi
kalkulyator qidirguncha javobni topsa boʻladi — chunki bu yerda ikki miqdor
<b>bir-biriga bogʻlangan</b>: olma koʻpaysa, pul ham xuddi shuncha marta koʻpayadi.
Shu bogʻlanishning nomi — proporsionallik.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>proporsiyani yozasiz va uning asosiy xossasini qoʻllaysiz;</li>
    <li>nomaʼlum hadni «bir birlik» usuli bilan topasiz;</li>
    <li>xaritadagi masshtabni kilometrga aylantirasiz;</li>
    <li>toʻgʻri proporsionallikni teskarisidan ajratasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Proporsiya</span>
  <span class="pe-chip pe-chip--o">a : b = c : d</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">a × d = b × c</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">teskarisi: a × b = c × d</span>
</div>

<h3>1. Proporsiya — ikki teng nisbat</h3>

<p>PM-27 da koʻrdik: 12 : 18 va 2 : 3 — bitta nisbatning ikki koʻrinishi. Ikki teng
nisbat yonma-yon yozilsa, u <b>proporsiya</b> deyiladi:</p>

<div class="pe-ex">
  <p class="pe-ex__math">12 : 18 = 2 : 3</p>
  <p class="pe-ex__uz">Oʻn ikkining oʻn sakkizga nisbati ikkining uchga nisbatiday.</p>
  <p class="pe-ex__why">Ikkala nisbat ham qisqartirilganda bir xil boʻladi.</p>
</div>

<p>Proporsiyani kasr koʻrinishida yozish qulayroq — shunda tekshirish oson boʻladi:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">12/18 = 2/3</span>
    <span class="pm-solve__why">Nisbat — aslida kasr (PM-15)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">12 × 3 = 36 va 18 × 2 = 36</span>
    <span class="pm-solve__why">Kesishma koʻpaytmalar teng chiqdi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">36 = 36 ✓</span>
    <span class="pm-solve__why">Demak bu haqiqatan ham proporsiya</span>
  </div>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Proporsiyaning asosiy xossasi</p>
  <p>Chetdagi ikki sonning koʻpaytmasi oʻrtadagi ikki sonning koʻpaytmasiga teng.
  Kasr koʻrinishida bu <b>krest-nakrest koʻpaytirish</b> boʻlib koʻrinadi: yuqoridagi
  birinchi son pastdagi ikkinchisiga, pastdagi birinchi son yuqoridagi ikkinchisiga.</p>
</div>

<h3>2. Nomaʼlum hadni topish</h3>

<p>Proporsiyaning uchta hadi maʼlum, bittasi nomaʼlum boʻlsa, uni topsa boʻladi.
Nomaʼlumni hozircha <b>?</b> bilan belgilaymiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3/4 = ?/20</span>
    <span class="pm-solve__why">Berilgan proporsiya</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4 → 20: 20 ÷ 4 = 5 marta oshdi</span>
    <span class="pm-solve__why">Maxraj necha marta kattalashganini koʻramiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">? = 3 × 5 = 15</span>
    <span class="pm-solve__why">Surat ham xuddi shuncha marta kattalashishi kerak</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Asosiy xossa bilan: 3 × 20 = 60 va 4 × 15 = 60 ✓ Ikki yoʻl bir xil javob berdi.</p>
</div>

<h3>3. «Bir birlik» usuli — eng ishonchli yoʻl</h3>

<p>Bozordagi savolga qaytamiz. 5 kg olma 60 000 soʻm boʻlsa, 8 kg qancha? Avval
<b>bitta kilogramm</b>ning narxini topamiz — bu PM-24 dagi «bir foiz» usulining
oʻsha oʻzi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">60 000 ÷ 5 = 12 000</span>
    <span class="pm-solve__why">Bir kilogramm olmaning narxi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">12 000 × 8 = 96 000</span>
    <span class="pm-solve__why">Sakkiz kilogramm 96 000 soʻm turadi</span>
  </div>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>8 kg — 5 kg dan koʻp, lekin ikki baravar emas. Demak javob 60 000 dan katta,
  120 000 dan kichik boʻlishi kerak. 96 000 — mos.</span>
</div>

<h3>4. Masshtab — xarita ham proporsiya</h3>

<p><b>Masshtab</b> xaritadagi uzunlik haqiqiy uzunlikdan necha marta kichik ekanini
aytadi. <b>1 : 100 000</b> degani: xaritadagi 1 santimetr yerda 100 000 santimetrga
toʻgʻri keladi. Endi santimetrni kilometrga aylantiramiz:</p>

<div class="pe-ex">
  <p class="pe-ex__math">100 000 sm = 1000 m = 1 km</p>
  <p class="pe-ex__uz">Bir yuz ming santimetr — bir kilometr.</p>
  <p class="pe-ex__why">100 sm — 1 metr; 1000 m — 1 km. Demak 1 km = 100 000 sm.</p>
</div>

<figure class="pm-fig">
  <svg viewBox="0 0 320 150" role="img" aria-label="Xaritadagi ikki santimetr va uning haqiqiy uzunligi">
    <text class="pm-lbl" x="20" y="30">Xaritada</text>
    <line class="pm-ln pm-ln--hl" x1="20" y1="50" x2="100" y2="50"/>
    <line class="pm-ln" x1="20" y1="42" x2="20" y2="58"/>
    <line class="pm-ln" x1="100" y1="42" x2="100" y2="58"/>
    <text class="pm-lbl pm-lbl--hl" x="35" y="72">2 sm</text>
    <text class="pm-lbl" x="20" y="105">Haqiqatda</text>
    <line class="pm-ln pm-ln--hl" x1="20" y1="125" x2="300" y2="125"/>
    <line class="pm-ln" x1="20" y1="117" x2="20" y2="133"/>
    <line class="pm-ln" x1="300" y1="117" x2="300" y2="133"/>
    <text class="pm-lbl pm-lbl--hl" x="140" y="147">10 km</text>
    <text class="pm-lbl" x="150" y="60">masshtab 1 : 500 000</text>
  </svg>
  <figcaption>1 : 500 000 masshtabda xaritadagi har santimetr — yerdagi 5 kilometr.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">1 : 500 000 → 1 sm = 500 000 sm</span>
    <span class="pm-solve__why">Masshtabni soʻzma-soʻz oʻqidik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">500 000 sm = 5 km</span>
    <span class="pm-solve__why">100 000 sm bir kilometr edi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2 sm × 5 = 10 km</span>
    <span class="pm-solve__why">Xaritadagi ikki santimetr — oʻn kilometr yoʻl</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Masshtabda birlik yozilmaydi — chunki u ikkala tomonda bir xil</p>
  <p>1 : 500 000 degani «bir santimetrga besh yuz ming santimetr», «bir millimetrga
  besh yuz ming millimetr» ham degani. Nisbat birlikka bogʻliq emas. Kilometrga
  faqat <b>oxirida</b> oʻtasiz.</p>
</div>

<h3>5. Toʻgʻri va teskari proporsionallik</h3>

<p>Hamma bogʻlanish ham «biri oshsa, ikkinchisi oshadi» degani emas. Ikki xili bor va
ularni ajratish bu darsning eng muhim koʻnikmasi.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Toʻgʻri proporsionallik</p>
    <p>Biri necha marta oshsa, ikkinchisi ham shuncha marta oshadi. <b>Boʻlinmasi
    oʻzgarmaydi.</b><br>Olma va pul, vaqt va bosib oʻtilgan yoʻl, kishilar soni va
    kerakli guruch.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Teskari proporsionallik</p>
    <p>Biri necha marta oshsa, ikkinchisi shuncha marta <b>kamayadi</b>.
    <b>Koʻpaytmasi oʻzgarmaydi.</b><br>Tezlik va vaqt, ishchilar soni va kunlar,
    quti hajmi va qutilar soni.</p>
  </div>
</div>

<p>Teskari proporsionallikka misol. <b>4 ishchi ishni 12 kunda</b> bajaradi. Xuddi
shu ishni <b>6 ishchi</b> necha kunda bajaradi?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">4 × 12 = 48</span>
    <span class="pm-solve__why">Ish hajmi — 48 ishchi-kun, u oʻzgarmaydi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">48 ÷ 6 = 8 kun</span>
    <span class="pm-solve__why">Ishchi koʻpaydi — kun kamaydi</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Bu yerda proporsiya tuzib boʻlmaydi</p>
  <p>Agar 4/12 = 6/? deb yozsangiz, 18 kun degan mantiqsiz javob chiqadi: ishchi
  koʻpaygani bilan ish uzoqroq davom etarmidi? Teskari bogʻlanishda <b>koʻpaytiriladi</b>,
  proporsiya esa faqat toʻgʻri bogʻlanishga yaraydi. Javobni yozishdan oldin oʻzingizga
  bitta savol bering: <b>biri oshsa, ikkinchisi oshadimi yoki kamayadimi?</b></p>
</div>

<h3>Matnli masala</h3>

<p><b>Toshkentdan Samarqandga yoʻl.</b> Bekzod xaritada ikki shahar orasini oʻlchadi —
28 santimetr chiqdi. Xarita masshtabi 1 : 1 000 000. Mashina soatiga 80 kilometr
tezlik bilan yuradi.</p>

<p><b>Savol:</b> yoʻl necha kilometr va u necha soat davom etadi? Tezlik 70 km/soatga
tushsa-chi?</p>

<p><b>Reja:</b> avval masshtab bilan masofani topamiz, keyin masofani tezlikka
boʻlamiz. Tezlik va vaqt — teskari proporsional, shuning uchun tezlik kamaysa vaqt
ortishi kerak.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">1 : 1 000 000 → 1 sm = 10 km</span>
    <span class="pm-solve__why">1 000 000 sm = 10 000 m = 10 km</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">28 × 10 = 280 km</span>
    <span class="pm-solve__why">Xaritadagi 28 sm — 280 kilometr</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">280 ÷ 80 = 3,5 soat</span>
    <span class="pm-solve__why">Uch yarim soat — 3 soat 30 daqiqa</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">280 ÷ 70 = 4 soat</span>
    <span class="pm-solve__why">Tezlik kamaydi — vaqt ortdi ✓</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Koʻpaytma oʻzgarmasligi kerak edi: 80 × 3,5 = 280 ✓ va 70 × 4 = 280 ✓ Ikkala
  holatda ham yoʻl bir xil — demak hisob toʻgʻri.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">1 : 100 000 masshtabda 1 sm = 100 000 km</p>
  <p class="pe-fix__good">1 sm = 100 000 sm = 1 km</p>
  <p class="pe-fix__why">Birlik almashtirilmagan. Masshtabdagi son <b>santimetr</b>ni
  bildiradi; kilometrga oʻtish uchun 100 000 ga boʻlish kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">4 ishchi 12 kun → 6 ishchi 18 kun</p>
  <p class="pe-fix__good">4 × 12 = 48; 48 ÷ 6 = 8 kun</p>
  <p class="pe-fix__why">Teskari bogʻlanishga proporsiya qoʻllangan. Nazorat: ishchi
  koʻpaysa ish tezroq tugaydi, demak javob 12 dan <b>kichik</b> boʻlishi shart edi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">5 kg 60 000 boʻlsa, 8 kg = 60 000 × 8 = 480 000</p>
  <p class="pe-fix__good">60 000 ÷ 5 = 12 000; 12 000 × 8 = 96 000</p>
  <p class="pe-fix__why">Avval bir birlikning narxi topilmagan. 480 000 — bu 40
  kilogramm olmaning puli.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Proporsiyadagi nomaʼlumni toping: 2/5 = 6/?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>15.</b> Surat 3 marta oshdi (2 → 6), demak maxraj ham: 5 × 3 = 15.
    Tekshirish: 2 × 15 = 30 va 5 × 6 = 30 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 4 kishi uchun 600 gramm guruch kerak. 6 kishiga qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>900 gramm.</b> Bir kishiga 600 ÷ 4 = 150 g; 150 × 6 = 900 g. Toʻgʻri
    proporsionallik: odam koʻpaysa guruch ham koʻpayadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Masshtab 1 : 25 000. Xaritadagi 4 sm yerda necha metr?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>1000 metr, yaʼni 1 km.</b> 1 sm = 25 000 sm = 250 m; 250 × 4 = 1000 m.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Mashina 60 km/soat tezlikda 4 soat yurdi. Xuddi shu yoʻlni
  80 km/soat tezlikda necha soatda bosib oʻtadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3 soat.</b> Yoʻl 60 × 4 = 240 km; 240 ÷ 80 = 3. Tezlik va vaqt teskari
    proporsional — tezlik oshdi, vaqt kamaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Uch nafar usta hovlini 8 kunda gʻishtlaydi. Ish muddatini 6
  kunga qisqartirish uchun nechta usta kerak?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>4 usta.</b> Ish hajmi 3 × 8 = 24 usta-kun; 24 ÷ 6 = 4. Kun kamaydi — usta
    koʻpaydi, demak bogʻlanish teskari.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Proporsiya</b><span>ikki teng nisbatning tengligi; ingl. proportion</span></li>
  <li><b>Had</b><span>proporsiyadagi har bir son; ingl. term</span></li>
  <li><b>Asosiy xossa</b><span>chetdagilar koʻpaytmasi oʻrtadagilarnikiga teng; ingl.
    cross product</span></li>
  <li><b>Masshtab</b><span>xaritadagi va haqiqiy uzunlik nisbati; ingl. scale</span></li>
  <li><b>Toʻgʻri proporsionallik</b><span>birga oshadigan bogʻlanish; ingl. direct
    proportion</span></li>
  <li><b>Teskari proporsionallik</b><span>biri oshsa, ikkinchisi kamayadigan
    bogʻlanish; ingl. inverse proportion</span></li>
  <li><b>Bir birlik usuli</b><span>avval bittasining qiymatini topish; ingl. unitary
    method</span></li>
  <li><b>Tezlik</b><span>bir soatda bosib oʻtilgan yoʻl; ingl. speed</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Proporsiya — ikki teng nisbat.</b> Asosiy xossasi: krest-nakrest
      koʻpaytmalar teng.</li>
    <li><b>Masshtabdagi son — santimetrda.</b> 1 : 100 000 → 1 sm = 1 km.</li>
    <li><b>Avval bogʻlanish turini aniqlang:</b> toʻgʻrisida boʻlinma, teskarisida
      koʻpaytma oʻzgarmaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-29 — harf nega kerak
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-29: Harf nega kerak: nomaʼlum va oʻzgaruvchi",
        "category": "math",
        "order": 29,
        "summary": (
            "Algebra shu yerdan boshlanadi. Harf nimani anglatadi, nomaʼlum bilan "
            "oʻzgaruvchining farqi va matematikaning yozuv qoidalari: 3a, ab, a², "
            "a/2."
        ),
        "stories": ["X kim? — sinfdagi topishmoq"],
        "content": """
<h2>PM-29: Harf nega kerak: nomaʼlum va oʻzgaruvchi</h2>

<p>Buvijon har safar bir xil gapni aytadi: «Har kosa unga ikki kosa suv». U bu gapni
bir marta aytadi, lekin u <i>hamma</i> holat uchun ishlaydi — bir kosa un uchun ham,
oʻn kosa un uchun ham. Matematika ham xuddi shunday gapirishni xohlaydi: bir marta
yozib, hamma holatga yaraydigan qilib. Buning uchun unga <b>harf</b> kerak.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>harf nima uchun kerakligini tushunasiz;</li>
    <li>nomaʼlum bilan oʻzgaruvchini ajratasiz;</li>
    <li>yozuv qoidalarini bilasiz: 3a, ab, a², a/2;</li>
    <li>eng sodda ifodalarni oʻzingiz yozasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Yozuv qoidalari</span>
  <span class="pe-chip pe-chip--o">3 × a = 3a</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">a × b = ab</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">a × a = a<sup>2</sup></span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--aux">a ÷ 2 = a/2</span>
</div>

<h3>1. Harf — bu «hozircha bilmayman» degan soʻz</h3>

<p>Bir qutida 12 ta qalam bor. Qutilar nechta ekanini bilmaymiz. Jami qalamlar sonini
qanday yozamiz? Sonlar bilan yozib boʻlmaydi — chunki bitta son yetishmaydi. Ammo
oʻsha yetishmayotgan sonni <b>nom bilan chaqirsak</b>, hammasi joyiga tushadi.</p>

<p>Qutilar sonini <b>n</b> deb ataymiz. Unda jami qalamlar — <b>12n</b>.</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">1 quti</span>
    <span class="pm-model__bar" style="width:20%">12 ta</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">n quti</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:80%">12n ta</span>
  </div>
  <p class="pm-model__tot">n — nechta quti borligi; 12n — jami qalamlar</p>
</div>

<p>Endi bu yozuv <b>hamma</b> holatga yaraydi. Qutilar 7 ta boʻlsa, 12 × 7 = 84 ta
qalam; 20 ta boʻlsa, 12 × 20 = 240 ta. Bitta qisqa yozuv — cheksiz koʻp holat.</p>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Harf — sehrli narsa emas, shunchaki nom</p>
  <p>Koʻp oʻquvchi algebradan aynan shu joyda qoʻrqadi: «harf nimani anglatadi?»
  Javob juda oddiy — u <b>sonning oʻrnida turadi</b>. Xuddi «Afsona» degan soʻz odam
  oʻrnida turgani kabi. Harf oʻrniga son qoʻysangiz, oddiy arifmetika qoladi.</p>
</div>

<h3>2. Nomaʼlum va oʻzgaruvchi — ikki xil vazifa</h3>

<p>Harf ikki xil ish qiladi va ularni ajratish foydali.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Nomaʼlum</p>
    <p>Qiymati <b>bitta</b>, lekin biz uni hali bilmaymiz. «Afsona bir necha daftar
    oldi» — daftarlar soni aniq bir son, faqat bizga aytilmagan.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Oʻzgaruvchi</p>
    <p>Qiymati <b>har xil</b> boʻlishi mumkin va u haqiqatan ham oʻzgaradi. Taksida
    bosib oʻtilgan kilometr har safar boshqacha.</p>
  </div>
</div>

<p>Yozuvi bir xil, mazmuni boshqa. Shuning uchun harfni koʻrganda birinchi savol doim
bitta: <b>bu harf nimani bildiryapti?</b> Javobni yozib qoʻying — «n — qutilar soni»,
«k — bosib oʻtilgan kilometr». Bu odat keyingi darslarda koʻp vaqt tejaydi.</p>

<h3>3. Yozuv qoidalari — matematikaning imlosi</h3>

<p>Algebrada koʻpaytirish belgisi deyarli yozilmaydi. Sabab oddiy: <b>×</b> belgisi
<b>x</b> harfiga juda oʻxshaydi va chalkashlik chiqadi.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Oʻqiladi</th><th>Yoziladi</th><th>Nega shunday</th></tr>
  <tr><td>3 marta a</td><td class="pm-word__sym">3a</td>
      <td>son doim harfdan oldin turadi</td></tr>
  <tr><td>a marta b</td><td class="pm-word__sym">ab</td>
      <td>belgi yozilmaydi</td></tr>
  <tr><td>a marta a</td><td class="pm-word__sym">a<sup>2</sup></td>
      <td>daraja — takroriy koʻpaytirish (PM-12)</td></tr>
  <tr><td>a ni 2 ga boʻlish</td><td class="pm-word__sym">a/2</td>
      <td>boʻlish kasr chizigʻi bilan</td></tr>
  <tr><td>bir marta a</td><td class="pm-word__sym">a</td>
      <td>1 yozilmaydi: 1a — a ning oʻzi</td></tr>
  <tr><td>a ni qarama-qarshisi</td><td class="pm-word__sym">−a</td>
      <td>ishora harf oldida turadi (PM-9)</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Son oldinda, harf ketida</p>
  <p><b>3a</b> deb yoziladi, <b>a3</b> deb emas. Bu shunchaki kelishuv, lekin uni
  buzsangiz yozuvingizni boshqalar oʻqiy olmaydi. Bir necha harf boʻlsa, ular alifbo
  tartibida yoziladi: <b>3ab</b>, <b>2xy</b>.</p>
</div>

<h3>4. Ifoda — harf va sonlardan tuzilgan gap</h3>

<p>Harf, son va amal belgilaridan tuzilgan yozuv <b>ifoda</b> deyiladi: 12n, 3a + 5,
2(x + 1). Ifodani <b>hisoblab boʻlmaydi</b> — chunki harfning qiymati nomaʼlum. U
javob emas, javobning <i>retsepti</i>.</p>

<div class="pe-ex">
  <p class="pe-ex__math">3a + 5</p>
  <p class="pe-ex__uz">a ni uchga koʻpaytirib, natijaga 5 ni qoʻshish kerak.</p>
  <p class="pe-ex__why">Bu ketma-ketlik — amallar tartibi (PM-5): avval koʻpaytirish,
  keyin qoʻshish.</p>
</div>

<p>Agar ifodaning ikki tomoni tenglik belgisi bilan bogʻlansa — <b>3a + 5 = 20</b> —
bu boshqa narsa, u <b>tenglama</b> deyiladi. Tenglamalarni yechishni PM-36 da
oʻrganamiz; hozircha ularni shunchaki tanib olish yetarli.</p>

<h3>Matnli masala</h3>

<p><b>Sinf kassasi.</b> Sinfdagi har bir oʻquvchi bayramga 5000 soʻmdan qoʻshdi.
Bundan tashqari sinf rahbari 20 000 soʻm qoʻshdi. Sinfda nechta oʻquvchi borligi
har yili oʻzgaradi.</p>

<p><b>Savol:</b> yigʻilgan pulni bitta yozuv bilan qanday ifodalaymiz? 24 oʻquvchi
boʻlsa, qancha yigʻiladi?</p>

<p><b>Reja:</b> oʻzgaradigan miqdorga nom beramiz, keyin gapni yozuvga aylantiramiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">n — oʻquvchilar soni</span>
    <span class="pm-solve__why">Oʻzgaruvchini eʼlon qildik va nima ekanini yozdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5000n</span>
    <span class="pm-solve__why">Har biri 5000 dan — koʻpaytirish</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5000n + 20 000</span>
    <span class="pm-solve__why">Rahbarning ulushi qoʻshiladi — u oʻzgarmaydi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">n = 24: 5000 × 24 + 20 000 = 140 000</span>
    <span class="pm-solve__why">Harf oʻrniga son qoʻysak, oddiy arifmetika qoldi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>24 oʻquvchi 5000 dan qoʻshsa — 120 000 soʻm, ustiga 20 000 qoʻshilsa —
  140 000 soʻm ✓ Yozuv boshqa sinfga ham yaraydi: 30 oʻquvchi boʻlsa,
  5000 × 30 + 20 000 = 170 000 soʻm.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">a + a = a<sup>2</sup></p>
  <p class="pe-fix__good">a + a = 2a</p>
  <p class="pe-fix__why">Qoʻshish bilan koʻpaytirish adashtirilgan. a<sup>2</sup> —
  bu a × a. Tekshirish: a = 3 boʻlsa, 3 + 3 = 6, 3<sup>2</sup> esa 9.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">3a degani «3 va a yonma-yon», yaʼni 3 dan keyin a</p>
  <p class="pe-fix__good">3a degani 3 × a</p>
  <p class="pe-fix__why">Algebrada yonma-yon turish <b>koʻpaytirish</b>ni bildiradi.
  Bu sonlardagi razryad yozuvidan farq qiladi: 35 — oʻttiz besh, lekin 3a — uchga
  koʻpaytirilgan a.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">a ning yarmi = 2a</p>
  <p class="pe-fix__good">a ning yarmi = a/2</p>
  <p class="pe-fix__why">Yarim — bu boʻlish, koʻpaytirish emas. 2a aksincha, a ni ikki
  baravar kattalashtiradi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 5 × b ni qisqa yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5b.</b> Koʻpaytirish belgisi tushiriladi, son harfdan oldin turadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. x × x × x ni qisqa yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>x<sup>3</sup>.</b> Uchta bir xil koʻpaytuvchi — uchinchi daraja (PM-12).</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. m + m + m + m qanday yoziladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>4m.</b> Bir xil qoʻshiluvchi toʻrt marta — bu koʻpaytirish (PM-3).</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «t — bir kunda oʻqilgan bet soni» boʻlsa, bir haftada
  oʻqilgan betlar sonini yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>7t.</b> Haftada 7 kun, har kuni t betdan.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Bir quti sharbat 9000 soʻm. Jasur k quti oldi va yana
  15 000 soʻmlik non oldi. Uning xarajatini yozing va k = 4 boʻlsa hisoblang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>9000k + 15 000; k = 4 boʻlsa 51 000 soʻm.</b> Sharbatlar 9000 × 4 = 36 000,
    ustiga non 15 000 — jami 51 000 soʻm.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Harf (belgi)</b><span>sonning oʻrnida turuvchi nom; ingl. letter</span></li>
  <li><b>Nomaʼlum</b><span>qiymati bitta, lekin bizga maʼlum boʻlmagan son; ingl.
    unknown</span></li>
  <li><b>Oʻzgaruvchi</b><span>qiymati oʻzgarib turadigan miqdor; ingl. variable</span></li>
  <li><b>Ifoda</b><span>harf, son va amallardan tuzilgan yozuv; ingl. expression</span></li>
  <li><b>Koeffitsient</b><span>harf oldidagi son, masalan 3a dagi 3; ingl.
    coefficient</span></li>
  <li><b>Had</b><span>ifodadagi qoʻshish belgilari bilan ajratilgan boʻlak; ingl.
    term</span></li>
  <li><b>Daraja</b><span>bir xil koʻpaytuvchilarning qisqa yozuvi; ingl. power</span></li>
  <li><b>Tenglama</b><span>ikki ifoda tenglik bilan bogʻlangan yozuv; ingl.
    equation</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Harf — sonning nomi.</b> U bir marta yozilgan yozuvni cheksiz koʻp holatga
      yaratadi.</li>
    <li><b>Yozuv qoidalari:</b> 3 × a = 3a, a × b = ab, a × a = a<sup>2</sup>,
      a ÷ 2 = a/2.</li>
    <li><b>Harfni eʼlon qiling:</b> «n — qutilar soni» deb yozib qoʻyish yarim
      yechim.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-30 — matndan ifoda tuzish
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-30: Matndan ifoda tuzish — soʻzni belgiga aylantirish",
        "category": "math",
        "order": 30,
        "summary": (
            "Matnli masalaning eng qiyin qadami — gapni ifodaga aylantirish. Soʻz "
            "va belgi jadvali, «nechtaga koʻp» bilan «necha marta koʻp» farqi va "
            "qavs qachon kerakligi."
        ),
        "stories": ["Taksi hisobi"],
        "content": """
<h2>PM-30: Matndan ifoda tuzish — soʻzni belgiga aylantirish</h2>

<p>Matnli masalani yecha olmaydigan oʻquvchilarning koʻpi hisobdan qiynalmaydi. Ular
<b>gapni yozuvga aylantira olmaydi</b> — masala oʻzbekcha, matematika esa belgilarda
gapiradi. Bu dars aynan shu tarjima haqida, va u butun kursdagi eng foydali
koʻnikma.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>soʻz birikmasini amal belgisiga aylantirasiz;</li>
    <li>«nechtaga koʻp» bilan «necha marta koʻp»ni ajratasiz;</li>
    <li>ayirishda tartibni toʻgʻri tanlaysiz;</li>
    <li>qavs qachon kerakligini bilasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Tarjimaning uch qadami</span>
  <span class="pe-chip pe-chip--s">1. nomaʼlumga nom bering</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">2. gapni boʻlaklarga ajrating</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">3. har boʻlakni belgiga yozing</span>
</div>

<h3>1. Soʻzlar lugʻati</h3>

<p>Oʻzbek tilidagi har bir ibora aniq bir amalga toʻgʻri keladi. Bu jadvalni bir marta
yodda saqlasangiz, matnli masalalar yarmiga qisqaradi.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Matnda shunday deyiladi</th><th>Matematikada</th><th>Misol</th></tr>
  <tr><td>…dan 5 ta koʻp</td><td class="pm-word__sym">+ 5</td><td>a + 5</td></tr>
  <tr><td>…dan 5 ta kam</td><td class="pm-word__sym">− 5</td><td>a − 5</td></tr>
  <tr><td>…dan 3 marta koʻp</td><td class="pm-word__sym">× 3</td><td>3a</td></tr>
  <tr><td>…dan 3 marta kam</td><td class="pm-word__sym">÷ 3</td><td>a/3</td></tr>
  <tr><td>…ning yarmi</td><td class="pm-word__sym">÷ 2</td><td>a/2</td></tr>
  <tr><td>…ning uchdan biri</td><td class="pm-word__sym">÷ 3</td><td>a/3</td></tr>
  <tr><td>…lar yigʻindisi</td><td class="pm-word__sym">+</td><td>a + b</td></tr>
  <tr><td>…lar koʻpaytmasi</td><td class="pm-word__sym">×</td><td>ab</td></tr>
  <tr><td>…ning kvadrati</td><td class="pm-word__sym">daraja</td>
      <td>a<sup>2</sup></td></tr>
  <tr><td>jami, hammasi boʻlib</td><td class="pm-word__sym">+</td><td>a + b + c</td></tr>
  <tr><td>qoldi, farqi</td><td class="pm-word__sym">−</td><td>a − b</td></tr>
</table></div>

<h3>2. Ikki ibora, ikki xil amal</h3>

<p>Mana bu farq — butun kursdagi eng koʻp xato qilinadigan joy, va u aslida
matematika emas, <b>til</b> masalasi.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">«5 ta koʻp»</p>
    <p>Ustiga beshta qoʻshiladi: <b>a + 5</b>.<br>a = 10 boʻlsa, javob 15.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">«5 marta koʻp»</p>
    <p>Beshga koʻpaytiriladi: <b>5a</b>.<br>a = 10 boʻlsa, javob 50.</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">«Marta» soʻzini qidiring</p>
  <p>Gapda <b>marta</b>, <b>barobar</b>, <b>baravar</b> soʻzlari boʻlsa — koʻpaytirish
  yoki boʻlish. Ular yoʻq boʻlsa — qoʻshish yoki ayirish. Masalani oʻqiyotganda shu
  soʻzlarning tagiga chizib qoʻying: bitta soʻz butun yechimni hal qiladi.</p>
</div>

<h3>3. Ayirishda tartib muhim</h3>

<p>Qoʻshishda tartib ahamiyatsiz: a + 5 va 5 + a bir xil. Ayirishda esa yoʻq —
a − 5 va 5 − a butunlay boshqa sonlar (PM-10).</p>

<div class="pe-ex">
  <p class="pe-ex__math">«a dan 5 ni ayirish» → a − 5</p>
  <p class="pe-ex__uz">a birinchi turadi, chunki undan ayiryapmiz.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">«5 dan a ni ayirish» → 5 − a</p>
  <p class="pe-ex__uz">Bu safar 5 birinchi: kamayuvchi — beshlik.</p>
  <p class="pe-ex__why">a = 8 boʻlsa, birinchisi 3, ikkinchisi −3. Ishorasi ham
  boshqacha!</p>
</div>

<h3>4. Qavs qachon kerak</h3>

<p>Qavs — «avval shuni bajar» degan buyruq (PM-5). Agar amal butun bir <b>guruh</b>
ustidan bajarilsa, guruh qavsga olinadi.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">3(a + 2)</p>
    <p>«a va 2 ning yigʻindisi uch barobar». Avval qoʻshiladi, keyin uchga
    koʻpaytiriladi.<br>a = 4: 3 × 6 = <b>18</b>.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">3a + 2</p>
    <p>«a ning uch barobariga 2 qoʻshildi». Avval koʻpaytiriladi.<br>
    a = 4: 12 + 2 = <b>14</b>.</p>
  </div>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">«…ning» qayerda turibdi?</p>
  <p>«<b>Yigʻindining</b> uch barobari» — qavs kerak: 3(a + b). «Uch barobarining
  <b>ustiga</b> yigʻindi» — kerak emas. Gapni ovoz chiqarib oʻqing va qayerda pauza
  borligini eshiting: pauza — qavsning oʻrni.</p>
</div>

<h3>5. Teskari tarjima ham foydali</h3>

<p>Ifodani koʻrib, unga mos hikoya oʻylab topish — tarjimani mustahkamlaydigan eng
yaxshi mashq. <b>4a + 2000</b> nimani anglatishi mumkin?</p>

<div class="pe-ex">
  <p class="pe-ex__math">4a + 2000</p>
  <p class="pe-ex__uz">Afsona har biri a soʻmdan 4 ta daftar oldi va yana 2000 soʻmlik
  ruchka oldi. Jami xarajati — shu.</p>
  <p class="pe-ex__why">Bitta ifoda — koʻp hikoya: 4 kunlik 2000 soʻmlik yoʻl puli
  ham xuddi shunday yoziladi.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Taksi tarifi.</b> Taksiga oʻtirganingiz uchun darrov 8000 soʻm yoziladi, keyin
har bir kilometr uchun 3000 soʻmdan qoʻshiladi.</p>

<p><b>Savol:</b> yoʻl narxini ifoda bilan yozing va 6 kilometrlik yoʻl qancha
turishini toping.</p>

<p><b>Reja:</b> oʻzgaradigan miqdor — kilometr. Unga nom beramiz, keyin gapni ikki
boʻlakka ajratamiz: oʻzgarmaydigan qism va kilometrga bogʻliq qism.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">k — bosib oʻtilgan kilometr</span>
    <span class="pm-solve__why">Oʻzgaruvchini eʼlon qildik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3000k</span>
    <span class="pm-solve__why">Har kilometr uchun 3000 dan — koʻpaytirish</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">8000 + 3000k</span>
    <span class="pm-solve__why">Oʻtirish haqi doim qoʻshiladi, u k ga bogʻliq emas</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">k = 6: 8000 + 18 000 = 26 000</span>
    <span class="pm-solve__why">Olti kilometrlik yoʻl 26 000 soʻm turadi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Boshqa yoʻl bilan sanaymiz: 6 km × 3000 = 18 000, ustiga 8000 — 26 000 ✓
  Nazorat: k = 0 boʻlsa (mashina qimirlamadi) ifoda 8000 beradi — mantiqan
  toʻgʻri, oʻtirish haqi baribir olinadi.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Har kilometr 3000 dan, olti kilometr — taxminan 18 000; ustiga oʻtirish haqi.
  Javob 25 000 atrofida chiqishi kerak edi.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">«a dan 4 marta koʻp» → a + 4</p>
  <p class="pe-fix__good">«a dan 4 marta koʻp» → 4a</p>
  <p class="pe-fix__why">«Marta» soʻzi koʻpaytirishni bildiradi. Tekshirish: a = 10
  boʻlsa, «toʻrt marta koʻp» 40 boʻlishi kerak, 14 emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">«12 dan x ni ayirish» → x − 12</p>
  <p class="pe-fix__good">12 − x</p>
  <p class="pe-fix__why">«…dan» qoʻshimchasi <b>kamayuvchi</b>ni koʻrsatadi — ayirish
  oʻshandan boshlanadi. Tartib almashsa, javobning ishorasi ham almashadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">«a va b yigʻindisining 5 barobari» → 5a + b</p>
  <p class="pe-fix__good">5(a + b)</p>
  <p class="pe-fix__why">Besh barobar butun <b>yigʻindi</b>ga tegishli, yolgʻiz a ga
  emas. Tekshirish: a = 1, b = 2 boʻlsa, toʻgʻri javob 15, notoʻgʻrisi esa 7.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «x dan 7 ta koʻp» ni yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>x + 7.</b> «Marta» soʻzi yoʻq — demak qoʻshish.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «m ning uchdan biri» ni yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>m/3.</b> Uchdan bir — uchga boʻlish.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «a va b yigʻindisining yarmi» ni yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>(a + b)/2.</b> Yarim butun yigʻindiga tegishli, shuning uchun qavs kerak.
    a = 4, b = 6 boʻlsa: 10 ÷ 2 = 5.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «p dan 2 marta kam» ni yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>p/2.</b> «Marta kam» — boʻlish. «2 ta kam» boʻlganda p − 2 boʻlar edi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Telefon tarifi: oyiga 25 000 soʻm abonent toʻlovi va har
  bir gigabayt uchun 5000 soʻm. Oylik toʻlovni ifoda bilan yozing va 8 gigabayt
  ishlatilganda toʻlovni toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>25 000 + 5000g; g = 8 boʻlsa 65 000 soʻm.</b> g — ishlatilgan gigabayt.
    5000 × 8 = 40 000, ustiga abonent toʻlovi 25 000 — jami 65 000 soʻm.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Ifoda tuzish</b><span>matnni matematik yozuvga aylantirish; ingl. form an
    expression</span></li>
  <li><b>Oʻzgaruvchi</b><span>qiymati oʻzgaradigan miqdor; ingl. variable</span></li>
  <li><b>Koeffitsient</b><span>harf oldidagi son; ingl. coefficient</span></li>
  <li><b>Ozod had</b><span>harfsiz son, masalan 8000; ingl. constant term</span></li>
  <li><b>Qavs</b><span>avval bajariladigan qismni ajratadi; ingl. brackets</span></li>
  <li><b>Kamayuvchi</b><span>ayirishda birinchi son; ingl. minuend</span></li>
  <li><b>Ayiruvchi</b><span>ayirishda ikkinchi son; ingl. subtrahend</span></li>
  <li><b>Yigʻindi</b><span>qoʻshish natijasi; ingl. sum</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>«Marta» boʻlsa — koʻpaytirish</b>, boʻlmasa — qoʻshish. Bitta soʻz butun
      yechimni hal qiladi.</li>
    <li><b>«…dan» kamayuvchini koʻrsatadi:</b> «12 dan x ni ayirish» — 12 − x.</li>
    <li><b>Amal butun guruhga tegishli boʻlsa, qavs qoʻying:</b> yigʻindining besh
      barobari — 5(a + b).</li>
  </ul>
</div>
""",
    },
]
