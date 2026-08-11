# -*- coding: utf-8 -*-
"""Prime Math — Blok C, darslar 37–39 (ikki tomonli tenglama, matnli masala 1 va 2).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt

Uchta oyoq birga yoziladi:
  mashqlar — practice/management/commands/_practice_pm_37_39.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_37_39.py

⚠️ Kumulyativ chegaralar:
  • PM-37 — nomaʼlum ikki tomonda. PM-36 dagi muvozanat qoidasining oʻzi,
    faqat endi nomaʼlumni ham koʻchiramiz;
  • PM-38 — matnli masalani tenglama bilan yechishning BEShTA qadami;
    bu yerda bogʻlanish sodda (yigʻindi, ayirma, «marta koʻp»);
  • PM-39 — murakkabroq bogʻlanishlar: uch qism, quyish (almashish) va
    perimetr masalalari. Ikki nomaʼlumli sistemalar bu kursda ancha keyin —
    bu yerda hammasi BITTA harf bilan yoziladi;
  • tengsizlik (PM-40) va modul (PM-41) hali yoʻq.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_37_39.py --author=prime
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
    # PM-37 — ikki tomonida ham nomaʼlumi bor tenglamalar
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-37: Ikki tomonida ham nomaʼlumi bor tenglamalar",
        "category": "math",
        "order": 37,
        "summary": (
            "Nomaʼlum ikkala pallada boʻlsa nima qilamiz: harfli hadlarni bir "
            "tomonga, sonlarni ikkinchisiga yigʻish, qavsli tenglamalar va "
            "yechimi yoʻq tenglamalar."
        ),
        "stories": ["Ikki doʻkon, bitta narx"],
        "content": """
<h2>PM-37: Ikki tomonida ham nomaʼlumi bor tenglamalar</h2>

<p>Oʻtgan darsda tarozining bir pallasida nomaʼlum, ikkinchisida sonlar turgan edi.
Hayotda esa koʻpincha boshqacha boʻladi: ikkita sport klubi, ikkita doʻkon, ikkita
tarif — va savol doim bitta: <b>ular qachon tenglashadi?</b> Bunday savol
nomaʼlumi ikkala tomonda boʻlgan tenglamaga olib keladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>harfli hadlarni bir tomonga yigʻasiz;</li>
    <li>qaysi tomonga yigʻish qulayligini tanlaysiz;</li>
    <li>qavsli tenglamalarni yechasiz;</li>
    <li>yechimi yoʻq tenglamani tanib olasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Tartib</span>
  <span class="pe-chip pe-chip--o">1. qavslarni och</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">2. harflar bir tomonga</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">3. sonlar ikkinchisiga</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--aux">4. boʻl</span>
</div>

<h3>1. Nomaʼlumni ham koʻchirsa boʻladi</h3>

<p>Muvozanat qoidasi (PM-36) hech oʻzgarmaydi: ikki tomonga bir xil amal. Yangi narsa
shuki, endi biz <b>son</b>ni emas, <b>harfli hadni</b> ham ayirishimiz mumkin.</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">Chap palla</span>
    <span class="pm-model__bar" style="width:75%">5x</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">Oʻng palla</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:75%">2x + 12</span>
  </div>
  <p class="pm-model__tot">Ikki palla teng: 5x = 2x + 12</p>
</div>

<p>Ikkala palladan ham <b>2x</b> ni olib tashlaymiz — tarozi baribir muvozanatda
qoladi, chunki teng miqdor olindi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">5x = 2x + 12</span>
    <span class="pm-solve__why">Berilgan tenglama</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5x − 2x = 2x + 12 − 2x</span>
    <span class="pm-solve__why">Ikki tomondan 2x ni ayirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x = 12</span>
    <span class="pm-solve__why">Oʻxshash hadlar ixchamlandi (PM-32)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 4</span>
    <span class="pm-solve__why">Ikki tomonni 3 ga boʻldik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Chap tomon: 5 × 4 = 20. Oʻng tomon: 2 × 4 + 12 = 20 ✓ <b>Ikki tomonli
  tenglamada tekshiruv ayniqsa muhim</b> — ikkala tomonni ham alohida hisoblab,
  teng chiqqanini koʻrasiz.</p>
</div>

<h3>2. Harflar bir tomonga, sonlar ikkinchisiga</h3>

<p>Ikkala tomonda ham harf va son boʻlsa, ish ikki qadamda boradi. Tartib muhim
emas, lekin bir tartibga oʻrganib qolgan maʼqul.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">4x + 3 = 2x + 11</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + 3 = 11</span>
    <span class="pm-solve__why">Ikki tomondan 2x ni ayirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x = 8</span>
    <span class="pm-solve__why">Ikki tomondan 3 ni ayirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 4</span>
    <span class="pm-solve__why">Ikki tomonni 2 ga boʻldik</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Katta koeffitsient qaysi tomonda boʻlsa, oʻsha tomonga yigʻing</p>
  <p>4x va 2x dan kichigini — 2x ni — ayirdik. Shunda chap tomonda musbat 2x qoldi.
  Agar teskarisini qilsak, −2x = −8 chiqadi: javob baribir 4, lekin manfiy ishora
  bilan ishlashga toʻgʻri keladi. Har qadamni osonlashtirish ham koʻnikma.</p>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Tenglikning ikki tomonini almashtirsa boʻladi</p>
  <p>9 = 3x va 3x = 9 — bir xil tenglama. Nomaʼlum oʻng tomonda qolib ketsa
  qoʻrqmang, xohlasangiz tomonlarni almashtiring. Muhimi — <b>tenglik</b>ning
  oʻzi, nomaʼlumning qaysi tomonda turishi emas.</p>
</div>

<h3>3. Qavsli tenglamalar</h3>

<p>Qavs boʻlsa, birinchi qadam doim bitta: <b>qavsni ochish</b> (PM-33). Undan keyin
tenglama tanish koʻrinishga tushadi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3(x + 2) = x + 10</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x + 6 = x + 10</span>
    <span class="pm-solve__why">Qavs ochildi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + 6 = 10</span>
    <span class="pm-solve__why">Ikki tomondan x ni ayirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2x = 4 → x = 2</span>
    <span class="pm-solve__why">Oltini ayirib, ikkiga boʻldik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Chap: 3(2 + 2) = 3 × 4 = 12. Oʻng: 2 + 10 = 12 ✓</p>
</div>

<h3>4. Baʼzan yechim yoʻq — va bu ham javob</h3>

<p>Mana bunga eʼtibor bering: <b>2x + 5 = 2x + 9</b>. Ikki tomondan 2x ni ayiraylik.
Qoladi: <b>5 = 9</b>. Bu yolgʻon! Demak bunday x umuman mavjud emas.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Yechimi yoʻq</p>
    <p>2x + 5 = 2x + 9 → 5 = 9<br>Yolgʻon tenglik chiqdi. Hech qanday son bu
    tenglamani rost qilmaydi.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Har qanday son yechim</p>
    <p>2x + 6 = 2(x + 3) → 6 = 6<br>Har doim rost. Bu tenglama emas, <b>ayniyat</b> —
    istalgan x toʻgʻri keladi.</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Harf yoʻqolib ketsa — toʻxtab, chiqqan tenglikka qarang</p>
  <p>Yechish jarayonida x butunlay yoʻqolsa, xato qilgan boʻlishingiz shart emas.
  Qolgan tenglik <b>rost</b> boʻlsa (6 = 6) — har qanday son yechim; <b>yolgʻon</b>
  boʻlsa (5 = 9) — yechim yoʻq. Ikkala holat ham toʻliq javob hisoblanadi.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Ikki sport klubi.</b> «Olimp» klubi oyiga 100 000 soʻm abonent toʻlovi oladi va
har bir mashgʻulot uchun yana 15 000 soʻm. «Chempion» klubida abonent toʻlovi
40 000 soʻm, lekin har mashgʻulot 20 000 soʻm turadi.</p>

<p><b>Savol:</b> oyiga necha marta borganda ikkala klub bir xil pul chiqaradi?</p>

<p><b>Reja:</b> mashgʻulotlar sonini n deb olamiz, ikkala klub uchun ifoda tuzamiz
(PM-30) va ularni tenglashtiramiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">100 000 + 15 000n = 40 000 + 20 000n</span>
    <span class="pm-solve__why">Ikki klubning toʻlovi teng deb qoʻydik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">100 000 = 40 000 + 5000n</span>
    <span class="pm-solve__why">Ikki tomondan 15 000n ni ayirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">60 000 = 5000n</span>
    <span class="pm-solve__why">Ikki tomondan 40 000 ni ayirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">n = 12</span>
    <span class="pm-solve__why">Oyiga 12 marta borganda toʻlovlar tenglashadi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>«Olimp»: 100 000 + 15 000 × 12 = 100 000 + 180 000 = <b>280 000</b>.
  «Chempion»: 40 000 + 20 000 × 12 = 40 000 + 240 000 = <b>280 000</b> ✓
  Ikkalasi ham 280 000 soʻm.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>«Olimp» boshida 60 000 soʻm qimmat, lekin har mashgʻulotda 5000 soʻm arzon.
  60 000 ni 5000 ga boʻlsak — 12. Farq oʻn ikkinchi mashgʻulotda yopiladi.</span>
</div>

<p>Javobni oʻqishni ham bilish kerak: <b>12 martadan kam</b> borsangiz «Chempion»
arzon, <b>koʻp</b> borsangiz «Olimp». Tenglama sizga faqat chegara nuqtasini beradi,
qarorni esa siz qabul qilasiz.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">5x = 2x + 12 → 5x + 2x = 12 → 7x = 12</p>
  <p class="pe-fix__good">5x − 2x = 12 → 3x = 12</p>
  <p class="pe-fix__why">Ikkinchi tomondagi 2x ni yoʻqotish uchun uni <b>ayirish</b>
  kerak, qoʻshish emas. Tekshirish: 7x = 12 dan x ≈ 1,7 chiqadi va u tenglamani
  toʻgʻri qilmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">4x + 3 = 2x + 11 → 2x + 3 = 11 → 2x = 14</p>
  <p class="pe-fix__good">2x + 3 = 11 → 2x = 8</p>
  <p class="pe-fix__why">Uchni yoʻqotish uchun uni ayirish kerak edi, qoʻshish emas.
  Har qadamda «qaysi amal turibdi, uning teskarisi nima?» deb soʻrang.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">3(x + 2) = x + 10 → 3x + 2 = x + 10</p>
  <p class="pe-fix__good">3x + 6 = x + 10</p>
  <p class="pe-fix__why">Qavs notoʻgʻri ochilgan: koʻpaytuvchi ikkinchi hadga ham
  tarqaladi (PM-33). Bitta eʼtiborsizlik butun yechimni buzadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 6x = 4x + 10 tenglamani yeching.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>x = 5.</b> Ikki tomondan 4x ni ayiramiz: 2x = 10. Tekshirish:
    30 = 20 + 10 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 5x + 2 = 3x + 12 tenglamani yeching.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>x = 5.</b> 2x + 2 = 12 → 2x = 10. Tekshirish: 27 = 27 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 7x − 4 = 4x + 8 tenglamani yeching.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>x = 4.</b> 3x − 4 = 8 → 3x = 12. Tekshirish: 24 = 24 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 2(x + 5) = 4x − 2 tenglamani yeching.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>x = 6.</b> Qavsni ochamiz: 2x + 10 = 4x − 2; ikki tomondan 2x ni ayiramiz:
    10 = 2x − 2; 12 = 2x. Tekshirish: 2 × 11 = 22 va 24 − 2 = 22 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Bir taksi xizmati 10 000 soʻm oʻtirish haqi va har kilometr
  uchun 4000 soʻm oladi. Ikkinchisi 25 000 soʻm oʻtirish haqi va har kilometr uchun
  1000 soʻm. Necha kilometrda narx tenglashadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5 kilometrda.</b> 10 000 + 4000k = 25 000 + 1000k → 3000k = 15 000 → k = 5.
    Tekshirish: 10 000 + 20 000 = 30 000 va 25 000 + 5000 = 30 000 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Tenglama</b><span>ikki ifodaning tengligi; ingl. equation</span></li>
  <li><b>Yechim (ildiz)</b><span>tenglamani rost qiladigan son; ingl. solution</span></li>
  <li><b>Harfli had</b><span>nomaʼlumi bor had, masalan 5x; ingl. variable term</span></li>
  <li><b>Ozod had</b><span>harfsiz son; ingl. constant term</span></li>
  <li><b>Yigʻish</b><span>oʻxshash hadlarni bir tomonga toʻplash; ingl.
    collecting</span></li>
  <li><b>Ayniyat</b><span>har qanday qiymatda rost boʻladigan tenglik; ingl.
    identity</span></li>
  <li><b>Yechimi yoʻq</b><span>hech qanday son toʻgʻri kelmaydigan holat; ingl. no
    solution</span></li>
  <li><b>Chegara nuqta</b><span>ikki variant tenglashadigan qiymat; ingl. break-even
    point</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Harflarni bir tomonga, sonlarni ikkinchisiga</b> — muvozanat qoidasi bilan.</li>
    <li><b>Avval qavsni oching</b>, keyin yigʻing.</li>
    <li><b>Harf yoʻqolsa toʻxtang:</b> rost tenglik — har qanday son yechim,
      yolgʻon tenglik — yechim yoʻq.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-38 — matnli masalani tenglama bilan yechish 1
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-38: Matnli masalani tenglama bilan yechish 1: nomaʼlumni tanlash",
        "category": "math",
        "order": 38,
        "summary": (
            "Matnli masalaning beshta qadami: nimani x deb olish, qolganini x orqali "
            "yozish, tenglama tuzish, yechish va savolga qaytish. Eng koʻp ball "
            "yoʻqotiladigan joy — oxirgi qadam."
        ),
        "stories": ["Jasur va Afsona necha yigʻdi"],
        "content": """
<h2>PM-38: Matnli masalani tenglama bilan yechish 1: nomaʼlumni tanlash</h2>

<p>Endi hamma qism joyida. PM-30 da gapni ifodaga aylantirdik, PM-36 va PM-37 da
tenglamani yechishni oʻrgandik. Qoldi eng qimmatli koʻnikma: <b>matnli masalani
tenglamaga aylantirish</b>. Bu — imtihonlarda eng koʻp ball turadigan va eng koʻp
ball yoʻqotiladigan joy.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>masalada nimani x deb olishni tanlaysiz;</li>
    <li>qolgan miqdorlarni x orqali yozasiz;</li>
    <li>tenglamani tuzasiz va yechasiz;</li>
    <li>javobni masalaning savoliga qaytarasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Beshta qadam</span>
  <span class="pe-chip pe-chip--s">1. x ni tanla</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">2. qolganini x orqali yoz</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">3. tenglama tuz</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--aux">4. yech</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--adv">5. savolga javob ber</span>
</div>

<h3>1. Nimani x deb olamiz</h3>

<p>Qoida oddiy: <b>eng kichik yoki eng sodda miqdorni</b> x deb oling. Odatda u
«…dan koʻp», «…dan katta» degan gapdagi <i>tayanch</i> miqdor boʻladi.</p>

<div class="pe-ex">
  <p class="pe-ex__math">«Jasur Afsonadan 12 ta koʻp yigʻdi»</p>
  <p class="pe-ex__uz">Afsona — tayanch, chunki Jasur unga nisbatan oʻlchanyapti.</p>
  <p class="pe-ex__why">x — Afsona yigʻgan soni; unda Jasurniki x + 12 boʻladi.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">x nimani bildirishini YOZIB qoʻying</p>
  <p>«x — Afsona yigʻgan olma soni» degan bitta qatorni yozmaslik — matnli masalada
  eng koʻp uchraydigan xatoning ildizi. Oxirida javob chiqqanda, u <b>nimaning</b>
  javobi ekanini bilmay qolasiz. Bir qator yozuv — yarim yechim.</p>
</div>

<h3>2. Ikki miqdor, bitta harf</h3>

<p>Masaladagi hamma miqdorni <b>bitta</b> harf orqali yozish kerak. Ikkinchi harf
kiritsangiz, tenglama yechilmaydigan boʻlib qoladi.</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">Afsona</span>
    <span class="pm-model__bar" style="width:40%">x</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">Jasur</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:60%">x + 12</span>
  </div>
  <p class="pm-model__tot">Jami: x + (x + 12) = 60</p>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + (x + 12) = 60</span>
    <span class="pm-solve__why">Ikkalasi birga 60 ta yigʻdi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + 12 = 60</span>
    <span class="pm-solve__why">Oʻxshash hadlar ixchamlandi (PM-32)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x = 48</span>
    <span class="pm-solve__why">Ikki tomondan 12 ni ayirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 24</span>
    <span class="pm-solve__why">Afsona 24 ta, Jasur 24 + 12 = 36 ta</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Ikki shartni ham tekshiramiz: 24 + 36 = 60 ✓ va 36 − 24 = 12 ✓ <b>Matnli
  masalada tekshiruv tenglamaga emas, MASALANING oʻziga qilinadi</b> — chunki
  tenglamani notoʻgʻri tuzgan boʻlishingiz ham mumkin.</p>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Chizmani chizing — bir daqiqa, ammo hammasini koʻrsatadi</p>
  <p>Ikki miqdorni ustma-ust ikkita chiziqcha qilib chizsangiz, qaysi biri uzun
  ekani va farq qayerda ekani darrov koʻrinadi. Tenglama shu chizmadan oʻzi
  chiqadi. Imtihonda ham shunday qiling — vaqt yoʻqotmaysiz, aksincha
  tejaysiz.</p>
</div>

<h3>3. «Marta koʻp» boʻlsa</h3>

<p>«…dan 3 marta koʻp» degan gapda qoʻshish emas, koʻpaytirish bor (PM-30). Tayanch
miqdor yana x boʻladi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + 3x = 60</span>
    <span class="pm-solve__why">Afsona x, Jasur undan 3 marta koʻp</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4x = 60</span>
    <span class="pm-solve__why">Oʻxshash hadlar qoʻshildi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 15 → Jasur 45 ta</span>
    <span class="pm-solve__why">Tekshirish: 15 + 45 = 60 va 45 = 3 × 15 ✓</span>
  </div>
</div>

<h3>4. Oxirgi qadamni unutmang</h3>

<p>Masala «Jasur nechta yigʻdi?» deb soʻragan boʻlsa, javob <b>36</b>, x ning oʻzi
emas. Bu — bu darsdagi eng qimmat gap.</p>

<div class="pe-call pe-warn">
  <p class="pe-call__t">x ni topish — yechimning oxiri emas, oʻrtasi</p>
  <p>Imtihonda toʻgʻri tenglama tuzib, uni toʻgʻri yechib, keyin 24 deb yozib
  chiqadigan oʻquvchi juda koʻp. Savol esa Jasur haqida edi. Yechishni tugatgach,
  <b>savolni qaytadan oʻqing</b> va javobingiz oʻsha savolga mos ekaniga ishonch
  hosil qiling.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Ikki son.</b> Ikki sonning yigʻindisi 90 ga teng. Birinchi son ikkinchisidan
14 taga katta.</p>

<p><b>Savol:</b> bu sonlarni toping.</p>

<p><b>Reja:</b> kichik sonni x deb olamiz — shunda kattasi x + 14 boʻladi va ikkala
son ham bitta harf orqali yozildi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x — kichik son, x + 14 — kattasi</span>
    <span class="pm-solve__why">1 va 2-qadam: nomaʼlumni tanlab, yozib oldik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + (x + 14) = 90</span>
    <span class="pm-solve__why">3-qadam: yigʻindi 90 ga teng</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + 14 = 90 → 2x = 76</span>
    <span class="pm-solve__why">4-qadam: ixchamlab, 14 ni ayirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 38; sonlar 38 va 52</span>
    <span class="pm-solve__why">5-qadam: savol IKKALA sonni soʻragan edi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>38 + 52 = 90 ✓ va 52 − 38 = 14 ✓ Masalaning ikkala sharti ham bajarildi.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Sonlar teng boʻlganda har biri 45 boʻlardi. Farq 14 boʻlgani uchun biri
  45 dan pastroq, ikkinchisi balandroq — 38 va 52 shu atrofda.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Jasur Afsonadan 12 ta koʻp: x + 12x = 60</p>
  <p class="pe-fix__good">x + (x + 12) = 60</p>
  <p class="pe-fix__why">«12 ta koʻp» — qoʻshish, «12 marta koʻp» — koʻpaytirish
  (PM-30). Bitta soʻz butun tenglamani oʻzgartiradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Afsona x, Jasur y; x + y = 60</p>
  <p class="pe-fix__good">Afsona x, Jasur x + 12; x + (x + 12) = 60</p>
  <p class="pe-fix__why">Ikkinchi harf kiritilgan va tenglama yechilmaydigan boʻlib
  qolgan. Bitta nomaʼlum — bitta harf: ikkinchi miqdorni birinchisi orqali
  yozing.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">x = 24, demak javob: Jasur 24 ta yigʻdi</p>
  <p class="pe-fix__good">x = 24 — bu Afsona; Jasur 24 + 12 = 36 ta</p>
  <p class="pe-fix__why">Oxirgi qadam bajarilmagan. x nimani bildirishini boshida
  yozib qoʻysangiz, bunday xato boʻlmaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Ikki sonning yigʻindisi 50, biri ikkinchisidan 8 taga
  katta. Kichik sonni toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>21.</b> x + (x + 8) = 50 → 2x = 42 → x = 21. Kattasi 29. Tekshirish:
    21 + 29 = 50 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Sherbek Bekzoddan 2 marta koʻp kitob oʻqidi. Ikkalasi
  birga 27 ta kitob oʻqidi. Sherbek nechta oʻqigan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>18 ta.</b> Bekzod x, Sherbek 2x: x + 2x = 27 → 3x = 27 → x = 9.
    Sherbek 2 × 9 = 18 ta. Savol Sherbek haqida edi!</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Sinfda qizlar oʻgʻillardan 4 taga koʻp. Jami 28 oʻquvchi.
  Nechta oʻgʻil bola bor?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>12 ta.</b> Oʻgʻillar x, qizlar x + 4: 2x + 4 = 28 → 2x = 24 → x = 12.
    Qizlar 16 ta. Tekshirish: 12 + 16 = 28 va 16 − 12 = 4 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Bir daftar qalamdan 3000 soʻm qimmat. Ikkalasi birga
  17 000 soʻm turadi. Daftar necha soʻm?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>10 000 soʻm.</b> Qalam x, daftar x + 3000: 2x + 3000 = 17 000 →
    2x = 14 000 → x = 7000. Daftar 7000 + 3000 = 10 000 soʻm.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Dilnoza kitobning bir qismini oʻqidi, qolgani oʻqilganidan
  3 marta koʻp. Kitobda 120 bet bor. Necha bet oʻqigan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>30 bet.</b> Oʻqilgani x, qolgani 3x: x + 3x = 120 → 4x = 120 → x = 30.
    Tekshirish: qolgani 90 bet; 30 + 90 = 120 va 90 = 3 × 30 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Matnli masala</b><span>soʻz bilan berilgan masala; ingl. word problem</span></li>
  <li><b>Nomaʼlumni tanlash</b><span>qaysi miqdorni x deb olish; ingl. choosing the
    unknown</span></li>
  <li><b>Tayanch miqdor</b><span>boshqalari oʻlchanadigan miqdor; ingl. reference
    quantity</span></li>
  <li><b>Tenglama tuzish</b><span>shartni tenglik koʻrinishida yozish; ingl. forming
    an equation</span></li>
  <li><b>Shart</b><span>masalada berilgan maʼlumot; ingl. condition</span></li>
  <li><b>Savolga qaytish</b><span>topilgan x dan soʻralgan javobni chiqarish; ingl.
    answering the question</span></li>
  <li><b>Yigʻindi</b><span>qoʻshish natijasi; ingl. sum</span></li>
  <li><b>Ayirma</b><span>ayirish natijasi; ingl. difference</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Tayanch miqdorni x deb oling</b> va u nimani bildirishini yozib
      qoʻying.</li>
    <li><b>Bitta harf yetadi:</b> ikkinchi miqdorni x orqali yozing.</li>
    <li><b>Oxirida savolga qayting</b> va javobni masalaning shartlariga
      tekshiring.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-39 — matnli masalani tenglama bilan yechish 2
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-39: Matnli masalani tenglama bilan yechish 2: bir bogʻlanish, ikki miqdor",
        "category": "math",
        "order": 39,
        "summary": (
            "Murakkabroq shakllar: uch qismli taqsimot, «quyib teng qilish» "
            "masalalari va perimetr masalasi — hammasi bitta harf va bitta "
            "tenglama bilan."
        ),
        "stories": ["Ikki chelak suv"],
        "content": """
<h2>PM-39: Matnli masalani tenglama bilan yechish 2: bir bogʻlanish, ikki miqdor</h2>

<p>Oʻtgan darsdagi beshta qadam oʻzgarmaydi. Oʻzgaradigani — <b>bogʻlanish</b>ning
murakkabligi. Endi uchta miqdor, «quyib teng qilish» yoki geometrik shart uchraydi.
Yaxshi xabar: bularning hammasi baribir <b>bitta harf</b> bilan yoziladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>uch miqdorni bitta harf orqali yozasiz;</li>
    <li>«quyib teng qilish» masalalarini yechasiz;</li>
    <li>perimetr shartidan tenglama tuzasiz;</li>
    <li>javobni masalaning hamma shartiga tekshirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Tayanchni tanlash</span>
  <span class="pe-chip pe-chip--s">eng kichik miqdor = x</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">qolganlari x orqali</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">shart tenglamaga aylanadi</span>
</div>

<h3>1. Uch miqdor, bitta harf</h3>

<p>Uchta bogʻcha 115 ta koʻchat oldi. Ikkinchisi birinchisidan <b>2 marta koʻp</b>,
uchinchisi esa birinchisidan <b>15 taga koʻp</b> oldi.</p>

<p>Tayanch — birinchi bogʻcha, chunki qolgan ikkalasi unga nisbatan aytilgan.</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">1-bogʻcha</span>
    <span class="pm-model__bar" style="width:25%">x</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">2-bogʻcha</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:50%">2x</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">3-bogʻcha</span>
    <span class="pm-model__bar" style="width:40%">x + 15</span>
  </div>
  <p class="pm-model__tot">Jami: x + 2x + (x + 15) = 115</p>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + 2x + x + 15 = 115</span>
    <span class="pm-solve__why">Uchala bogʻcha birga 115 ta oldi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4x + 15 = 115</span>
    <span class="pm-solve__why">Oʻxshash hadlar ixchamlandi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4x = 100 → x = 25</span>
    <span class="pm-solve__why">15 ni ayirib, 4 ga boʻldik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">25, 50 va 40 ta koʻchat</span>
    <span class="pm-solve__why">Har uchala bogʻchaning javobi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>25 + 50 + 40 = 115 ✓ Ikkinchisi birinchisidan 2 marta koʻp: 50 = 2 × 25 ✓
  Uchinchisi 15 taga koʻp: 40 − 25 = 15 ✓ <b>Uchala shart ham tekshirildi.</b></p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Tayanchni notoʻgʻri tanlash — xato emas, faqat uzunroq yoʻl</p>
  <p>Yuqoridagi masalada ikkinchi bogʻchani x deb olsangiz ham javob oʻsha chiqadi,
  lekin qolganlari x/2 va x/2 + 15 koʻrinishida — kasrli boʻlib ketadi. Shuning
  uchun <b>eng kichik</b> miqdorni tanlash odat qilinadi.</p>
</div>

<h3>2. «Quyib teng qilish» masalalari</h3>

<p>Bu tur alohida oʻrganishga arziydi, chunki unda <b>bir tomondan olingan miqdor
ikkinchisiga qoʻshiladi</b> — yaʼni ikki marta hisobga olinadi.</p>

<p>Ikki chelakda jami <b>30 litr</b> suv bor. Birinchisidan ikkinchisiga <b>5 litr</b>
quyilsa, ular <b>teng</b> boʻlib qoladi.</p>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Quyish farqni IKKI baravar kamaytiradi</p>
  <p>5 litr quyilganda birinchisi 5 taga kamaydi, ikkinchisi 5 taga koʻpaydi — demak
  ular orasidagi farq <b>10 litr</b>ga qisqardi. Ular tenglashgani uchun boshlangʻich
  farq roppa-rosa 10 litr boʻlgan. Bu masalalarda eng koʻp shu joyda adashadilar:
  farqni 5 deb olib qoʻyishadi.</p>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x — ikkinchi chelak, x + 10 — birinchisi</span>
    <span class="pm-solve__why">Boshlangʻich farq 10 litr (yuqoridagi mulohaza)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + (x + 10) = 30</span>
    <span class="pm-solve__why">Jami 30 litr</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x = 20 → x = 10</span>
    <span class="pm-solve__why">Ikkinchi chelakda 10 litr</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Birinchisida 20, ikkinchisida 10 litr</span>
    <span class="pm-solve__why">Javob ikkala chelak uchun</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Jami: 20 + 10 = 30 ✓ Quyib koʻramiz: 20 − 5 = 15 va 10 + 5 = 15 — <b>teng</b> ✓
  Masalaning ikkala sharti ham bajarildi.</p>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Javob hayotiy boʻlishi ham shart</p>
  <p>Odam soni, olma soni yoki chelakdagi litr kasr chiqsa — masalani qaytadan
  oʻqing. 12,5 nafar oʻquvchi boʻlmaydi. Bunday javob koʻpincha shartni
  notoʻgʻri tushunganingizni bildiradi, hisobdagi xatoni emas.</p>
</div>

<h3>3. Geometrik shartdan tenglama</h3>

<p>Toʻgʻri toʻrtburchakning boʻyi enidan <b>5 sm uzun</b>, perimetri esa
<b>46 sm</b>. Tomonlarini topamiz. Bu yerda PM-35 dagi formula tenglamaga
aylanadi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 180" role="img" aria-label="Toʻgʻri toʻrtburchak, eni x, boʻyi x plyus besh">
    <rect class="pm-fill" x="50" y="40" width="220" height="100"/>
    <rect class="pm-ln" x="50" y="40" width="220" height="100" fill="none"/>
    <text class="pm-lbl pm-lbl--hl" x="160" y="30" text-anchor="middle">x + 5</text>
    <text class="pm-lbl pm-lbl--hl" x="30" y="95" text-anchor="middle">x</text>
    <text class="pm-lbl" x="160" y="95" text-anchor="middle">P = 46 sm</text>
  </svg>
  <figcaption>Eni x, boʻyi undan 5 sm uzun. Perimetr — barcha tomonlar yigʻindisi.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2(x + x + 5) = 46</span>
    <span class="pm-solve__why">P = 2(en + boʻy) formulasi (PM-35)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2(2x + 5) = 46</span>
    <span class="pm-solve__why">Qavs ichi ixchamlandi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + 5 = 23</span>
    <span class="pm-solve__why">Ikki tomonni 2 ga boʻldik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2x = 18 → x = 9; boʻyi 14 sm</span>
    <span class="pm-solve__why">Eni 9 sm, boʻyi 14 sm</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>P = 2(9 + 14) = 2 × 23 = 46 ✓ va 14 − 9 = 5 ✓ Yuzasi ham hisoblanadi:
  9 × 14 = 126 sm<sup>2</sup>.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Ota va oʻgʻil.</b> Otasi oʻgʻlidan 28 yosh katta. Ikkalasining yoshi
yigʻindisi 46.</p>

<p><b>Savol:</b> har biri necha yoshda?</p>

<p><b>Reja:</b> oʻgʻilning yoshini x deb olamiz — u kichik miqdor, demak tayanch
oʻsha.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x — oʻgʻil, x + 28 — otasi</span>
    <span class="pm-solve__why">Ikkala yosh bitta harf orqali</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + (x + 28) = 46</span>
    <span class="pm-solve__why">Yoshlar yigʻindisi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + 28 = 46 → 2x = 18</span>
    <span class="pm-solve__why">28 ni ayirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 9; oʻgʻil 9 yoshda, otasi 37 yoshda</span>
    <span class="pm-solve__why">Ikkalasining javobi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>9 + 37 = 46 ✓ va 37 − 9 = 28 ✓ Javob hayotiy ham koʻrinadi — bu ham nazorat:
  agar otaning yoshi 15 chiqqanida, yechimni qayta koʻrib chiqish kerak boʻlardi.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Yoshlar teng boʻlganda har biri 23 boʻlardi. Farq katta — 28 yil — demak
  oʻgʻil ancha kichkina, ota esa 23 dan ancha katta.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">5 litr quyilsa teng boʻladi → farq 5 litr</p>
  <p class="pe-fix__good">Farq 10 litr — quyilgan miqdorning ikki barobari</p>
  <p class="pe-fix__why">Quyilgan suv bir tomondan kamayib, ikkinchisiga qoʻshiladi:
  farq har ikki tomondan qisqaradi. Tekshirish: 15 va 15 boʻlishi uchun 20 va 10
  boʻlishi kerak edi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Perimetr: x + (x + 5) = 46</p>
  <p class="pe-fix__good">2(x + x + 5) = 46</p>
  <p class="pe-fix__why">Toʻgʻri toʻrtburchakning toʻrtta tomoni bor — har tomondan
  ikkitadan. Faqat ikkita tomonni qoʻshish yarim perimetrni beradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Uchinchi bogʻcha «15 taga koʻp» → 15x</p>
  <p class="pe-fix__good">x + 15</p>
  <p class="pe-fix__why">«Taga koʻp» — qoʻshish (PM-30). Tekshirish: 15x yozilsa,
  yigʻindi 115 dan ancha oshib ketadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Uch qutida jami 102 ta olma bor. Ikkinchisida birinchisidan
  2 marta koʻp, uchinchisida birinchisidan 6 taga koʻp. Har qutida nechtadan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>24, 48 va 30 ta.</b> x + 2x + (x + 6) = 102 → 4x + 6 = 102 → 4x = 96 →
    x = 24. Tekshirish: 24 + 48 + 30 = 102 ✓ Javob butun son chiqdi — olma sonida
    shunday boʻlishi ham kerak edi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Ikki savatda jami 40 ta non bor. Birinchisidan ikkinchisiga
  4 ta non olib qoʻyilsa, ular teng boʻladi. Har savatda nechtadan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>24 ta va 16 ta.</b> Farq — quyilganning ikki barobari, yaʼni 8 ta.
    x + (x + 8) = 40 → 2x = 32 → x = 16; kattasi 24. Tekshirish: 24 − 4 = 20 va
    16 + 4 = 20 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Toʻgʻri toʻrtburchakning boʻyi enidan 3 sm uzun, perimetri
  26 sm. Tomonlarini toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5 sm va 8 sm.</b> 2(x + x + 3) = 26 → 2x + 3 = 13 → 2x = 10 → x = 5.
    Tekshirish: 2(5 + 8) = 26 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Onasi qizidan 24 yosh katta, ikkalasining yoshi yigʻindisi
  50. Qiz necha yoshda?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>13 yoshda.</b> x + (x + 24) = 50 → 2x = 26 → x = 13. Onasi 37 yoshda.
    Tekshirish: 13 + 37 = 50 va 37 − 13 = 24 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Uch doʻst 150 000 soʻm topdi. Jasur Afsonadan 2 marta koʻp,
  Sherbek esa Afsonadan 20 000 soʻm koʻp oldi. Har biri qancha oldi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Afsona 32 500, Jasur 65 000, Sherbek 52 500 soʻm.</b>
    x + 2x + (x + 20 000) = 150 000 → 4x = 130 000 → x = 32 500. Tekshirish:
    32 500 + 65 000 + 52 500 = 150 000 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Bogʻlanish</b><span>miqdorlar orasidagi munosabat; ingl. relationship</span></li>
  <li><b>Tayanch miqdor</b><span>x deb olinadigan asosiy miqdor; ingl. reference
    quantity</span></li>
  <li><b>Taqsimot</b><span>butunni qismlarga boʻlish; ingl. distribution</span></li>
  <li><b>Farq</b><span>ikki miqdor orasidagi ayirma; ingl. difference</span></li>
  <li><b>Perimetr</b><span>shaklning atrofi uzunligi; ingl. perimeter</span></li>
  <li><b>Shart</b><span>masalada berilgan maʼlumot; ingl. condition</span></li>
  <li><b>Hayotiylik nazorati</b><span>javob mantiqan mumkinmi degan tekshiruv; ingl.
    reasonableness check</span></li>
  <li><b>Yechim</b><span>masalaning javobi; ingl. solution</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Nechta miqdor boʻlsa ham bitta harf yetadi</b> — hammasini tayanch
      orqali yozing.</li>
    <li><b>Quyish farqni ikki baravar kamaytiradi:</b> 5 litr quyilsa, farq 10
      litr edi.</li>
    <li><b>Javobni hamma shartga tekshiring</b> va hayotiy ekanini ham
      oʻylab koʻring.</li>
  </ul>
</div>
""",
    },
]
