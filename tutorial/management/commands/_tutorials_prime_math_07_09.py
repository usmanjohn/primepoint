# -*- coding: utf-8 -*-
"""Prime Math — Block A, darslar 7–9 (tub sonlar, EKUB/EKUK, manfiy sonlar).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt

Uchta oyoq birga yoziladi:
  mashqlar — practice/management/commands/_practice_pm_07_09.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_07_09.py

⚠️ Kumulyativ: kvadrat ildiz (PM-13), daraja (PM-12), kasr (PM-15) va manfiy
sonlar bilan amallar (PM-10, PM-11) hali oʻrgatilmagan — ishlatilmaydi.
PM-9 da faqat manfiy sonning MAʼNOSI va tartibi beriladi, amallar emas.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_math_07_09.py --author=prime
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
    # PM-7 — tub va murakkab sonlar
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-7: Tub va murakkab sonlar; tub koʻpaytuvchilarga ajratish",
        "category": "math",
        "order": 7,
        "summary": (
            "Nega baʼzi sonlarni teng qatorlarga tiza olmaymiz? Tub va murakkab sonlar, "
            "Eratosfen gʻalviri va har qanday sonni tub koʻpaytuvchilarga ajratish."
        ),
        "stories": ["Tub sonlar sirni qanday saqlaydi"],
        "content": """
<h2>PM-7: Tub va murakkab sonlar; tub koʻpaytuvchilarga ajratish</h2>

<p>Sinfga <b>12</b> ta stul keltirildi. Ularni teng qatorlarga tizish kerak. Bekzod bir
necha xil qildi: 2 qatorda 6 tadan, 3 qatorda 4 tadan, 4 qatorda 3 tadan. Ertasi kuni
<b>13</b> ta stul keltirishdi — va hech narsa chiqmadi. Qanday urinmasin, yo bitta uzun
qator, yo bittadan turgan 13 ta qator. 13 soni «singishni» xohlamadi. Bunday sonlar
matematikaning eng qiziq mavzularidan biri — <b>tub sonlar</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>tub va murakkab sonni ajrata olasiz;</li>
    <li>1 nega tub son emasligini tushunasiz;</li>
    <li>Eratosfen gʻalviri bilan tub sonlarni topasiz;</li>
    <li>har qanday sonni tub koʻpaytuvchilarga ajratasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Boʻluvchilar soni boʻyicha</span>
  <span class="pe-chip pe-chip--s">1 — na tub, na murakkab</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">tub: 2 ta boʻluvchi</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">murakkab: 3 ta va undan koʻp</span>
</div>

<h3>Boʻluvchilarni sanaymiz</h3>

<p>Har bir sonning kamida ikkita boʻluvchisi bor: <b>1</b> va <b>sonning oʻzi</b>. Butun
farq shundan keyin boshlanadi.</p>

<div class="pe-table-wrap"><table>
  <tr><th>Son</th><th>Boʻluvchilari</th><th>Nechta</th><th>Turi</th></tr>
  <tr><td>12</td><td>1, 2, 3, 4, 6, 12</td><td>6 ta</td><td>murakkab</td></tr>
  <tr><td>13</td><td>1, 13</td><td>2 ta</td><td><b>tub</b></td></tr>
  <tr><td>9</td><td>1, 3, 9</td><td>3 ta</td><td>murakkab</td></tr>
  <tr><td>2</td><td>1, 2</td><td>2 ta</td><td><b>tub</b></td></tr>
  <tr><td>1</td><td>1</td><td>1 ta</td><td>na tub, na murakkab</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
<b>Tub son</b> — roppa-rosa ikkita boʻluvchisi bor son: 1 va oʻzi.
<b>Murakkab son</b> — undan koʻp boʻluvchisi bor son.
<b>1</b> esa na u, na bu: uning bitta boʻluvchisi bor.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
«Nega 1 ni tub deb hisoblamaymiz?» Chunki har bir sonni tub koʻpaytuvchilarga <b>faqat
bitta usulda</b> ajratish mumkin boʻlishi kerak. Agar 1 tub boʻlganda edi, 6 = 2 × 3
ham, 1 × 2 × 3 ham, 1 × 1 × 2 × 3 ham boʻlar edi — cheksiz koʻp yoʻl. Shuning uchun 1 ni
roʻyxatga kiritmaymiz.</div>

<h3>Eratosfen gʻalviri</h3>

<p>Ikki ming yildan koʻproq oldin yunon olimi Eratosfen tub sonlarni topishning oddiy
usulini oʻylab topdi: <em>murakkablarini oʻchirib tashlash</em>. Qolgani — tub.</p>

<ol class="pe-steps">
  <li>1 ni oʻchiring — u tub emas.</li>
  <li>2 ni qoldiring, keyin har ikkinchi sonni oʻchiring: 4, 6, 8, 10…</li>
  <li>3 ni qoldiring, keyin har uchinchi sonni oʻchiring: 6, 9, 12, 15…</li>
  <li>5 va 7 bilan ham shunday qiling. Qolgani — tub sonlar.</li>
</ol>

<p>50 gacha boʻlgan tub sonlar shunday topiladi va ular bor-yoʻgʻi <b>15 ta</b>:</p>

<div class="pe-ex">
  <p class="pe-ex__math">2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47</p>
  <p class="pe-ex__uz">Roʻyxatdagi yagona juft son — 2. Boshqa har qanday juft son 2 ga
     boʻlinadi, demak uchinchi boʻluvchisi bor.</p>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Son tubmi yoʻqmi — tekshirish uchun uni tub sonlarga navbat bilan boʻling: 2, 3, 5, 7…
Boʻlinma boʻluvchidan kichik boʻlib qolgan zahoti toʻxtang, keyingisini tekshirish
shart emas. Masalan <b>91</b>: 2 ga boʻlinmaydi, 3 ga boʻlinmaydi (9 + 1 = 10),
5 ga boʻlinmaydi, <b>7 ga boʻlinadi</b> — 91 = 7 × 13. Demak murakkab.</div>

<h3>Tub koʻpaytuvchilarga ajratish</h3>

<p>Har qanday murakkab sonni tub sonlarning koʻpaytmasi koʻrinishida yozish mumkin — va
bu yoʻl yagona. Buni <b>tub koʻpaytuvchilarga ajratish</b> deymiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">60 = 2 × 30</span>
    <span class="pm-solve__why">Eng kichik tub boʻluvchidan boshlaymiz: 60 juft</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= 2 × 2 × 15</span>
    <span class="pm-solve__why">30 ham juft</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= 2 × 2 × 3 × 5</span>
    <span class="pm-solve__why">15 = 3 × 5, ikkalasi ham tub — toʻxtaymiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">60 = 2 × 2 × 3 × 5</span>
    <span class="pm-solve__why">Tekshirish: 2 × 2 = 4, 4 × 3 = 12, 12 × 5 = 60 ✓</span>
  </div>
</div>

<p>Yana bitta: <b>84</b>. Juft → 84 = 2 × 42. 42 ham juft → 2 × 2 × 21. 21 = 3 × 7.
Demak <b>84 = 2 × 2 × 3 × 7</b>. Tekshiring: 4 × 21 = 84 ✓</p>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Ajratishni <b>faqat tub sonlar</b> qolguncha davom ettiring. 60 = 4 × 15 — bu hali javob
emas, chunki 4 ham, 15 ham murakkab. Boshlash tartibi esa ahamiyatsiz: 60 = 6 × 10 dan
boshlasangiz ham, oxirida oʻsha 2 × 2 × 3 × 5 chiqadi.</div>

<h3>Matnli masala</h3>

<p>Bogʻbonda <b>60</b> ta koʻchat bor. U ularni <b>teng qatorlarga</b> ekmoqchi — har
qatorda bir xil sondan. <b>Necha xil variant bor?</b></p>

<p><em>Nima soʻralyapti?</em> 60 ning barcha boʻluvchilari soni: har bir boʻluvchi —
bitta variant.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">60 = 2 × 2 × 3 × 5</span>
    <span class="pm-solve__why">Tub koʻpaytuvchilar — barcha boʻluvchilarning «gʻishtlari»</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60</span>
    <span class="pm-solve__why">Boʻluvchilarni juftlab yozamiz: 1×60, 2×30, 3×20, 4×15, 5×12, 6×10</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">12 xil variant</span>
    <span class="pm-solve__why">Oltita juftlik, har biri ikki xil joylashuv beradi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Masalan 4 qatorda 15 tadan: 4 × 15 = 60 ✓ · 6 qatorda 10 tadan: 6 × 10 = 60 ✓</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">«<s>1 — eng kichik tub son</s>»</p>
  <p class="pe-good">Eng kichik tub son — <b>2</b>. 1 na tub, na murakkab</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">«9 toq, demak <s>tub son</s>»</p>
  <p class="pe-good">9 = 3 × 3 — <b>murakkab</b>. Toqlik tublikni bildirmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">60 = <s>4 × 15</s> — tub koʻpaytuvchilarga ajratildi</p>
  <p class="pe-good">60 = <b>2 × 2 × 3 × 5</b> — 4 va 15 hali murakkab edi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     17 tub sonmi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Ha.</strong> 2 ga boʻlinmaydi (toq), 3 ga
    boʻlinmaydi (1 + 7 = 8), 5 ga boʻlinmaydi. Keyingi tub 7 boʻlar edi, lekin
    7 × 7 = 49 — 17 dan katta, demak tekshirishni toʻxtatamiz. Boʻluvchilari faqat
    1 va 17.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     51 tub sonmi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Yoʻq.</strong> Raqamlar yigʻindisi 5 + 1 = 6 —
    uchga boʻlinadi (PM-6), demak <b>51 = 3 × 17</b>. Bu klassik tuzoq: 51 tub
    koʻrinadi, lekin uchga boʻlinadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     84 ni tub koʻpaytuvchilarga ajrating.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>84 = 2 × 2 × 3 × 7.</strong> 84 juft →
    2 × 42; 42 juft → 2 × 21; 21 = 3 × 7. Tekshirish: 2 × 2 × 3 × 7 = 84 ✓</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     2 dan boshqa yana qanday juft tub son bor?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Yoʻq.</strong> Har qanday juft son 2 ga
    boʻlinadi, demak uning kamida uchta boʻluvchisi bor: 1, 2 va oʻzi. Shuning uchun
    <b>2 — yagona juft tub son</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     13 ta stulni teng qatorlarga tizish mumkinmi — har qatorda bittadan koʻp va bitta
     qatordan koʻp boʻlsin?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Mumkin emas.</strong> 13 — tub son, uning
    boʻluvchilari faqat 1 va 13. Demak yo bitta qatorda 13 ta, yo 13 qatorda bittadan.
    12 ta stul bilan esa beshta boshqa variant chiqar edi: 2×6, 3×4, 4×3, 6×2 va
    boshqalar.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Tub son</b><span>faqat 1 va oʻziga boʻlinadi; ingl. prime number</span></li>
  <li><b>Murakkab son</b><span>ikkitadan koʻp boʻluvchisi bor; ingl. composite number</span></li>
  <li><b>Boʻluvchi</b><span>sonni qoldiqsiz boʻladigan son; ingl. divisor, factor</span></li>
  <li><b>Tub koʻpaytuvchi</b><span>ajratmadagi tub son; ingl. prime factor</span></li>
  <li><b>Ajratma</b><span>2 × 2 × 3 × 5 koʻrinishidagi yozuv; ingl. prime factorisation</span></li>
  <li><b>Eratosfen gʻalviri</b><span>tub sonlarni topish usuli; ingl. sieve of Eratosthenes</span></li>
  <li><b>Juft tub son</b><span>faqat 2; ingl. the only even prime</span></li>
  <li><b>Oʻzaro tub sonlar</b><span>umumiy boʻluvchisi 1 dan boshqa boʻlmagan sonlar; ingl. coprime</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda tuting</p>
  <ul>
    <li><b>Tub son</b> — roppa-rosa ikkita boʻluvchisi bor son; <b>1</b> tub emas.</li>
    <li><b>2</b> — yagona juft tub son.</li>
    <li>Har qanday sonni tub koʻpaytuvchilarga ajratish yoʻli <b>yagona</b>.</li>
    <li>Ajratishni tub sonlar qolguncha davom ettiring: 60 = 2 × 2 × 3 × 5.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-8 — EKUB va EKUK
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-8: EKUB va EKUK — va ular qayerda kerak boʻladi",
        "category": "math",
        "order": 8,
        "summary": (
            "Eng katta umumiy boʻluvchi va eng kichik umumiy karrali: tub "
            "koʻpaytuvchilar orqali topish, ikkalasini adashtirmaslik va hayotdagi "
            "masalalarda qoʻllash."
        ),
        "stories": ["Ikki avtobus qachon bir vaqtda keladi"],
        "content": """
<h2>PM-8: EKUB va EKUK — va ular qayerda kerak boʻladi</h2>

<p>Dilnozada <b>24</b> ta olma va <b>36</b> ta nok bor. U ularni bir xil sovgʻa
paketlariga solmoqchi: har paketda olma ham, nok ham teng miqdorda boʻlsin va hech narsa
ortib qolmasin. <b>Eng koʻpi bilan nechta paket chiqadi?</b> Bu savolning javobi
<b>EKUB</b> deb ataladigan tushunchada. Uning egizagi <b>EKUK</b> esa butunlay boshqa
savolga javob beradi: «ikki hodisa qachon yana bir vaqtda takrorlanadi?»</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>EKUB va EKUK nima ekanini va ularning farqini bilib olasiz;</li>
    <li>ikkalasini tub koʻpaytuvchilar orqali topasiz;</li>
    <li>qaysi masalada qaysi biri kerakligini ajratasiz;</li>
    <li>javobni tez tekshirish usulini oʻrganasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki savol</span>
  <span class="pe-chip pe-chip--s">EKUB: eng katta umumiy boʻluvchi</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">EKUK: eng kichik umumiy karrali</span>
</div>

<h3>EKUB — «eng koʻpi bilan nechta guruh?»</h3>

<p>Umumiy boʻluvchi — ikkala sonni ham qoldiqsiz boʻladigan son. Ularning eng kattasi
EKUB deyiladi. Tub koʻpaytuvchilarga ajratsak (PM-7), javob koʻzga koʻrinib qoladi:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">24 = 2 × 2 × 2 × 3</span>
    <span class="pm-solve__why">Birinchi sonning ajratmasi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">36 = 2 × 2 × 3 × 3</span>
    <span class="pm-solve__why">Ikkinchi sonning ajratmasi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">umumiylari: 2, 2 va 3</span>
    <span class="pm-solve__why">Ikkala roʻyxatda ham bor boʻlganlarini olamiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">EKUB(24, 36) = 2 × 2 × 3 = 12</span>
    <span class="pm-solve__why">Demak eng koʻpi bilan 12 ta paket</span>
  </div>
</div>

<h3>EKUK — «qachon yana uchrashadi?»</h3>

<p>Karrali — songa qoldiqsiz boʻlinadigan son: 12 ning karralilari 12, 24, 36, 48…
Ikkala sonning ham karralisi boʻlgan eng kichik son — EKUK. Bu safar
<b>hamma</b> koʻpaytuvchilarni olamiz, umumiylarini esa <b>bir marta</b>:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">24 = 2 × 2 × 2 × 3 · 36 = 2 × 2 × 3 × 3</span>
    <span class="pm-solve__why">Oʻsha ajratmalar</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2 × 2 × 3 (umumiy qism) × 2 (24 dan ortiq) × 3 (36 dan ortiq)</span>
    <span class="pm-solve__why">Har bir sonning «yetishmagan» qismini qoʻshamiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">EKUK(24, 36) = 72</span>
    <span class="pm-solve__why">72 ÷ 24 = 3 ✓ va 72 ÷ 36 = 2 ✓</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>EKUB × EKUK = ikki sonning koʻpaytmasi: 12 × 72 = 864 va 24 × 36 = 864 ✓ — bu
  qoida har doim ishlaydi va javobni bir zumda tekshiradi.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Nomlarning oʻzi hammasini aytib turibdi: <b>EKUB</b> — eng katta umumiy
<em>boʻluvchi</em>, demak u sonlardan <b>kichik</b> yoki teng. <b>EKUK</b> — eng kichik
umumiy <em>karrali</em>, demak u sonlardan <b>katta</b> yoki teng. Javobingiz shu
chegaralarga sigʻmasa, xato qilgansiz.</div>

<h3>Qaysi biri kerak? Savolga qarang</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">EKUB kerak</p>
    <p>Bor narsani <b>boʻlib</b> tashlaymiz: eng koʻpi bilan nechta paket, eng katta
    qanday kvadrat kafel, nechta bir xil guruh.</p>
    <p><em>Javob sonlardan kichik chiqadi.</em></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">EKUK kerak</p>
    <p>Takrorlanadigan narsalar <b>qachon uchrashadi</b>: avtobuslar, navbatchilik,
    ikki xil qadamdagi hodisa.</p>
    <p><em>Javob sonlardan katta chiqadi.</em></p>
  </div>
</div>

<h3>Ikkita maxsus holat</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Biri ikkinchisiga boʻlinsa</p>
    <p>EKUB(5, 15) = 5, EKUK(5, 15) = 15. Kichik son katta sonning boʻluvchisi
    boʻlsa, javoblar shu sonlarning oʻzi.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Oʻzaro tub sonlar</p>
    <p>EKUB(7, 13) = 1, EKUK(7, 13) = 91. Umumiy tub koʻpaytuvchisi yoʻq sonlarning
    EKUK i — koʻpaytmasining oʻzi.</p>
  </div>
</div>

<h3>Matnli masala</h3>

<p>Dilnozada <b>24</b> ta olma va <b>36</b> ta nok bor. Har bir paketda olma ham, nok ham
teng miqdorda boʻlishi va hech narsa ortmasligi kerak. <b>Eng koʻpi bilan nechta paket
chiqadi va har birida nechtadan meva boʻladi?</b></p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">EKUB(24, 36) = 12</span>
    <span class="pm-solve__why">Paketlar soni — ikkala sonni ham boʻlishi shart</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">24 ÷ 12 = 2 ta olma</span>
    <span class="pm-solve__why">Har paketga tegadigan olma</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">36 ÷ 12 = 3 ta nok</span>
    <span class="pm-solve__why">Har paketda 2 olma va 3 nok, jami 12 ta paket</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>12 × 2 = 24 ✓ va 12 × 3 = 36 ✓ — hech narsa ortib qolmadi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">EKUB(24, 36) = <s>72</s></p>
  <p class="pe-good">EKUB(24, 36) = <b>12</b> — boʻluvchi sonlardan katta boʻlolmaydi
  (72 — bu EKUK)</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">EKUK(24, 36) = <s>24 × 36 = 864</s></p>
  <p class="pe-good">EKUK(24, 36) = <b>72</b> — koʻpaytma faqat oʻzaro tub sonlarda
  EKUK boʻladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">EKUB uchun umumiy koʻpaytuvchilar <s>qoʻshiladi</s>: 2 + 2 + 3 = 7</p>
  <p class="pe-good">Ular <b>koʻpaytiriladi</b>: 2 × 2 × 3 = <b>12</b></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     EKUB(18, 24) = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>6.</strong> 18 = 2 × 3 × 3, 24 = 2 × 2 × 2 × 3.
    Umumiylari: 2 va 3 → 2 × 3 = 6. Tekshirish: 18 ÷ 6 = 3 ✓, 24 ÷ 6 = 4 ✓</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     EKUK(4, 6) = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>12.</strong> 4 ning karralilari: 4, 8, 12…
    6 niki: 6, 12… Birinchi uchrashuv — 12. Tekshirish: EKUB(4, 6) = 2 va
    2 × 12 = 24 = 4 × 6 ✓</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     EKUB(7, 13) = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>1.</strong> Ikkalasi ham tub son va bir-biriga
    teng emas, demak umumiy boʻluvchisi faqat 1. Bunday sonlar <b>oʻzaro tub</b>
    deyiladi, ularning EKUK i esa koʻpaytmasi: 91.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     EKUK(5, 15) = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>15.</strong> 15 allaqachon 5 ga boʻlinadi,
    demak u ikkalasining ham karralisi. Kichik son katta sonning boʻluvchisi boʻlsa,
    EKUK — katta sonning oʻzi, EKUB esa kichigining oʻzi (bu yerda 5).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bekatga birinchi avtobus har 12 daqiqada, ikkinchisi har 18 daqiqada keladi. Ular
     soat 8:00 da birga keldi. Keyingi safar qachon birga keladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Soat 8:36 da.</strong> Kerak boʻlgani —
    EKUK(12, 18). 12 = 2 × 2 × 3, 18 = 2 × 3 × 3 → EKUK = 2 × 2 × 3 × 3 = <b>36</b>
    daqiqa. Tekshirish: 36 ÷ 12 = 3 ✓, 36 ÷ 18 = 2 ✓ Bu yerda EKUB (6) kerak emas —
    savol «qachon uchrashadi» degan savol.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Umumiy boʻluvchi</b><span>ikkala sonni ham boʻladigan son; ingl. common divisor</span></li>
  <li><b>EKUB</b><span>eng katta umumiy boʻluvchi; ingl. GCD, HCF</span></li>
  <li><b>Karrali</b><span>songa qoldiqsiz boʻlinadigan son; ingl. multiple</span></li>
  <li><b>Umumiy karrali</b><span>ikkala sonning ham karralisi; ingl. common multiple</span></li>
  <li><b>EKUK</b><span>eng kichik umumiy karrali; ingl. LCM</span></li>
  <li><b>Oʻzaro tub</b><span>EKUB i 1 ga teng sonlar; ingl. coprime</span></li>
  <li><b>Tub koʻpaytuvchi</b><span>ajratmadagi tub son; ingl. prime factor</span></li>
  <li><b>Qoldiqsiz</b><span>teng, ortmasdan; ingl. without remainder</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda tuting</p>
  <ul>
    <li><b>EKUB</b> — umumiy tub koʻpaytuvchilarning koʻpaytmasi; sonlardan <b>kichik</b> yoki teng.</li>
    <li><b>EKUK</b> — hamma koʻpaytuvchilar, umumiylari bir marta; sonlardan <b>katta</b> yoki teng.</li>
    <li>Tekshiruv: <b>EKUB × EKUK = a × b</b>.</li>
    <li>«Boʻlib tashlaymiz» → EKUB. «Qachon uchrashadi» → EKUK.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-9 — manfiy sonlar va son oʻqi
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-9: Manfiy sonlar va son oʻqi",
        "category": "math",
        "order": 9,
        "summary": (
            "Noldan pastdagi sonlar: harorat, qavatlar va qarz. Son oʻqi, qarama-qarshi "
            "sonlar va manfiy sonlarni taqqoslashning yagona ishonchli usuli."
        ),
        "stories": ["Qish kundaligi"],
        "content": """
<h2>PM-9: Manfiy sonlar va son oʻqi</h2>

<p>Yanvar oyi. Ertalab termometr <b>−7°</b> koʻrsatdi, tushga borib <b>−2°</b> boʻldi.
Jasur dedi: «Sovuq kuchaydi, minus yetti — minus ikkidan katta-ku». Aslida esa havo
<em>isidi</em>. Manfiy sonlar bilan ishlaganda odatiy sezgi ishlamay qoladi, shuning
uchun bizga <b>son oʻqi</b> kerak — u hech qachon aldamaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>manfiy son nimani anglatishini hayotdagi uch misolda koʻrasiz;</li>
    <li>son oʻqida istalgan sonni joylashtirasiz;</li>
    <li>qarama-qarshi sonlarni topasiz;</li>
    <li>manfiy sonlarni xatosiz taqqoslaysiz va tartiblaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Son oʻqi</span>
  <span class="pe-chip pe-chip--neg">manfiy: … −3, −2, −1</span>
  <span class="pe-op">|</span>
  <span class="pe-chip pe-chip--aux">0</span>
  <span class="pe-op">|</span>
  <span class="pe-chip pe-chip--o">musbat: 1, 2, 3 …</span>
</div>

<h3>Manfiy son qayerda uchraydi?</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Harorat</p>
    <p>0° — muz eriydigan nuqta. −7° esa undan yetti daraja sovuq.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Qavatlar</p>
    <p>Liftda −1 va −2 — yerto'la qavatlari. 0 — kirish qavati.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Pul</p>
    <p>Hisobda −50 000 soʻm — bu pul emas, <b>qarz</b>.</p>
  </div>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Manfiy son — bu <b>nolning boshqa tomonidagi</b> son. Nolning oʻzi na musbat, na manfiy:
u — chegara, sanoq boshlanadigan joy.</div>

<h3>Son oʻqi — ishonchli qurol</h3>

<p>Sonlarni chapdan oʻngga qarab tartib bilan joylaymiz. Oʻngga siljisak — son ortadi,
chapga siljisak — kamayadi. Manfiylar noldan chapda turadi.</p>

<div class="pm-num">
  <div class="pm-num__track">
    <span class="pm-num__tick" style="left:0%"><i>−5</i></span>
    <span class="pm-num__tick" style="left:25%"><i>−2</i></span>
    <span class="pm-num__tick" style="left:50%"><i>0</i></span>
    <span class="pm-num__tick" style="left:75%"><i>2</i></span>
    <span class="pm-num__tick" style="left:100%"><i>5</i></span>
    <span class="pm-num__dot" style="left:16.6%"><i>−3</i></span>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Eng koʻp uchraydigan xato: «−7 sonida yetti bor, −2 sonida ikki bor, demak −7 katta».
Bu yerda sezgi aldaydi. <b>Minus belgisi «noldan qancha uzoq» degani emas, «qaysi
tomonda» degani.</b> Son oʻqiga qarasangiz: −7 chaproqda, demak kichikroq.</div>

<h3>Qarama-qarshi sonlar</h3>

<p>Har bir sonning juftligi bor: noldan bir xil uzoqlikda, lekin boshqa tomonda.
5 ning qarama-qarshisi −5, −12 niki 12. Nolning qarama-qarshisi — nolning oʻzi.</p>

<div class="pe-ex">
  <p class="pe-ex__math">−6 va 6 — ikkalasi ham noldan 6 qadam uzoqda</p>
  <p class="pe-ex__uz">Biri chapda, ikkinchisi oʻngda. Qarzingiz 6 000 soʻm boʻlsa,
     6 000 soʻm topsangiz nolga qaytasiz.</p>
</div>

<h3>Taqqoslash: bitta qoida yetarli</h3>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
<b>Son oʻqida oʻngdagi son har doim katta.</b> Shundan kelib chiqadi:
har qanday musbat son har qanday manfiydan katta · nol har qanday manfiydan katta ·
ikki manfiy sondan <b>nolga yaqinrogʻi</b> katta.</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">−7 va −2</span>
    <span class="pm-solve__why">Ikkalasi ham noldan chapda</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">−2 nolga yaqinroq</span>
    <span class="pm-solve__why">Demak u son oʻqida oʻngroqda</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">−7 &lt; −2</span>
    <span class="pm-solve__why">Ertalabdan tushga havo isigan ekan</span>
  </div>
</div>

<h3>Matnli masala</h3>

<p>Dilnoza bir haftalik ertalabki haroratni yozib bordi:
<b>dushanba −3°, seshanba −8°, chorshanba 0°, payshanba +2°, juma −5°.</b></p>
<p><b>Eng sovuq kun qaysi? Kunlarni sovuqdan issiqqa qarab tartiblang.</b></p>

<div class="pm-num">
  <div class="pm-num__track">
    <span class="pm-num__tick" style="left:0%"><i>−8</i></span>
    <span class="pm-num__tick" style="left:30%"><i>−5</i></span>
    <span class="pm-num__tick" style="left:50%"><i>−3</i></span>
    <span class="pm-num__tick" style="left:80%"><i>0</i></span>
    <span class="pm-num__tick" style="left:100%"><i>+2</i></span>
  </div>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">−8 eng chapda</span>
    <span class="pm-solve__why">Eng sovuq kun — seshanba</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">−8 &lt; −5 &lt; −3 &lt; 0 &lt; +2</span>
    <span class="pm-solve__why">Seshanba → juma → dushanba → chorshanba → payshanba</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Roʻyxatdagi har bir son oʻzidan keyingisidan chaproqda turibdi ✓ Sanoq oʻsib
  boryapti, demak tartib toʻgʻri.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>−7 &gt; −2</s>, chunki yetti ikkidan katta</p>
  <p class="pe-good"><b>−7 &lt; −2</b> — son oʻqida −7 chaproqda</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>0 &lt; −3</s>, chunki nol «hech narsa»</p>
  <p class="pe-good"><b>0 &gt; −3</b> — nol har qanday manfiy sondan katta</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">«−5 ning qarama-qarshisi — <s>−5 ning oʻzi</s>»</p>
  <p class="pe-good">−5 ning qarama-qarshisi — <b>5</b>; faqat nol oʻziga
  qarama-qarshi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Qaysi son katta: −3 yoki −9?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>−3.</strong> U nolga yaqinroq, demak son oʻqida
    oʻngroqda. Harorat tilida: −3° −9° dan issiqroq.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Sonlarni oʻsish tartibida yozing: −5, 2, −1, 0.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>−5, −1, 0, 2.</strong> Avval manfiylar (eng
    chapdagisi eng kichik), keyin nol, keyin musbat. Son oʻqiga chizib koʻrsangiz,
    tartib oʻz-oʻzidan koʻrinadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     −6 ning qarama-qarshi soni qaysi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>6.</strong> Ikkalasi ham noldan olti qadam
    uzoqda, lekin turli tomonlarda.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Lift 3-qavatda turibdi va besh qavat pastga tushdi. U qaysi qavatda?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>−2-qavatda</strong> (ikkinchi yerto'la).
    Son oʻqida 3 dan chapga besh qadam sanang: 2, 1, 0, −1, −2. Nol — kirish qavati,
    uni ham sanashni unutmang.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Uch shaharda harorat: Toshkentda −2°, Nukusda −11°, Termizda +4°. Eng sovuq shahar
     qaysi va Termiz Nukusdan necha daraja issiq?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Eng sovugʻi — Nukus; Termiz undan 15 daraja
    issiq.</strong> Son oʻqida −11 dan +4 gacha sanaymiz: −11 dan 0 gacha 11 qadam,
    0 dan 4 gacha yana 4 qadam, jami <b>15</b>. Sanashda nolni ikki marta hisoblab
    yubormang.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Manfiy son</b><span>noldan kichik son; ingl. negative number</span></li>
  <li><b>Musbat son</b><span>noldan katta son; ingl. positive number</span></li>
  <li><b>Son oʻqi</b><span>sonlar tartib bilan joylashgan chiziq; ingl. number line</span></li>
  <li><b>Qarama-qarshi son</b><span>noldan bir xil uzoqlikdagi juft; ingl. opposite number</span></li>
  <li><b>Nol</b><span>musbat ham, manfiy ham emas — chegara; ingl. zero</span></li>
  <li><b>Butun sonlar</b><span>manfiy, nol va musbatlar birgalikda; ingl. integers</span></li>
  <li><b>Oʻsish tartibi</b><span>kichikdan kattaga; ingl. ascending order</span></li>
  <li><b>Daraja (harorat)</b><span>haroratning oʻlchov birligi; ingl. degree</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda tuting</p>
  <ul>
    <li>Manfiy son — nolning <b>boshqa tomonidagi</b> son: sovuq, yerto'la, qarz.</li>
    <li>Son oʻqida <b>oʻngdagi har doim katta</b> — bu yagona kerakli qoida.</li>
    <li>Ikki manfiydan <b>nolga yaqinrogʻi</b> katta: −2 &gt; −7.</li>
    <li>Qarama-qarshi sonlar noldan bir xil uzoqlikda turadi.</li>
  </ul>
</div>
""",
    },
]
