# -*- coding: utf-8 -*-
"""Prime Math — Blok C, darslar 31–33 (qiymat, oʻxshash hadlar, qavs ochish).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt

Uchta oyoq birga yoziladi:
  mashqlar — practice/management/commands/_practice_pm_31_33.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_31_33.py

⚠️ Kumulyativ chegaralar:
  • PM-31 — oʻrniga qoʻyish. Ixchamlash hali yoʻq: ifoda qanday berilgan
    boʻlsa, shundayligicha hisoblanadi. Manfiy sonni qoʻyishda qavs
    ishlatiladi (PM-11 ustiga quriladi);
  • PM-32 — oʻxshash hadlarni ixchamlash. Qavs ochilmaydi (PM-33);
  • PM-33 — qavs ochish va ishoralar; oxirida PM-32 bilan birlashtiriladi
    (avval ochamiz, keyin ixchamlaymiz);
  • umumiy koʻpaytuvchini qavsdan CHIQARISH (PM-34), formula (PM-35) va
    tenglama (PM-36) bu uch darsda yoʻq.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_31_33.py --author=prime
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
    # PM-31 — ifodaning qiymatini hisoblash
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-31: Ifodaning qiymatini hisoblash va oʻrniga qoʻyish",
        "category": "math",
        "order": 31,
        "summary": (
            "Harf oʻrniga son qoʻysak, algebra yana arifmetikaga aylanadi. "
            "Oʻrniga qoʻyish tartibi, manfiy son qoʻyilganda qavsning roli va "
            "qiymatlar jadvali."
        ),
        "stories": ["Qaysi tarif arzon?"],
        "content": """
<h2>PM-31: Ifodaning qiymatini hisoblash va oʻrniga qoʻyish</h2>

<p>PM-30 da gapni ifodaga aylantirdik: taksi narxi — 8000 + 3000k. Lekin ifodaning
oʻzi hali pul emas. U <b>retsept</b>: k ni bilsangiz, narxni chiqaradi. Retseptni
ishga solish esa bitta harakat — harf oʻrniga son qoʻyish.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>ifodaga son qoʻyib qiymatini hisoblaysiz;</li>
    <li>amallar tartibini toʻgʻri saqlaysiz;</li>
    <li>manfiy sonni qavs bilan qoʻyasiz;</li>
    <li>qiymatlar jadvalini tuzib, ifodalarni taqqoslaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uch qadam</span>
  <span class="pe-chip pe-chip--s">1. harf oʻrniga son</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">2. amallar tartibi bilan hisobla</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">3. birlikni yoz</span>
</div>

<h3>1. Oʻrniga qoʻyish — eng oddiy amal</h3>

<p>Harf sonning nomi edi (PM-29). Demak nomni koʻrsatib, uning oʻrniga sonni qoʻyish
kifoya. Faqat bir shart: <b>koʻpaytirish belgisi qaytib keladi</b>. 3a degani 3 × a
edi, shuning uchun a = 4 boʻlsa, 3 × 4 boʻladi — 34 emas.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3a + 5, a = 4</span>
    <span class="pm-solve__why">Berilgan ifoda va harfning qiymati</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 × 4 + 5</span>
    <span class="pm-solve__why">a oʻrniga 4 ni qoʻydik, belgi qaytdi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">12 + 5</span>
    <span class="pm-solve__why">Avval koʻpaytirish — amallar tartibi (PM-5)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 17</span>
    <span class="pm-solve__why">Ifodaning a = 4 dagi qiymati</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Qiymat harfga bogʻliq — bitta ifoda, koʻp javob</p>
  <p>3a + 5 ning «javobi» yoʻq. a = 4 boʻlsa 17, a = 10 boʻlsa 35, a = 0 boʻlsa 5.
  Shuning uchun javobni yozganda doim aytib qoʻying: «a = 4 boʻlganda qiymati 17».
  Bu odat keyingi darslarda funksiyani tushunishni osonlashtiradi.</p>
</div>

<h3>2. Ikki harfli ifodalar</h3>

<p>Harf nechta boʻlsa ham qoida bir xil: har birining oʻrniga oʻz sonini qoʻyamiz.</p>

<div class="pe-ex">
  <p class="pe-ex__math">2a + 3b, a = 4, b = 5 → 2 × 4 + 3 × 5 = 8 + 15 = 23</p>
  <p class="pe-ex__uz">Ikkita a va uchta b — jami yigirma uch.</p>
  <p class="pe-ex__why">Ikkala koʻpaytirish qoʻshishdan oldin bajariladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">ab, a = 6, b = 7 → 6 × 7 = 42</p>
  <p class="pe-ex__uz">Yonma-yon turgan harflar koʻpaytiriladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">(a + b)/2, a = 7, b = 9 → (7 + 9)/2 = 16/2 = 8</p>
  <p class="pe-ex__uz">Yettining va toʻqqizning oʻrtasi — sakkiz.</p>
  <p class="pe-ex__why">Kasr chizigʻi qavs vazifasini bajaradi: avval yigʻindi.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Qoʻyishdan oldin ifodani koʻchirib yozing</p>
  <p>Imtihonda vaqt tejayman deb ifodani xayolda almashtirmang. Avval ifodani
  koʻchiring, keyin harflarning tagiga qiymatini yozib chiqing, undan soʻng
  hisoblang. Uch qadam uch sekund oladi va yarim ballni saqlab qoladi.</p>
</div>

<h3>3. Manfiy son qoʻyilsa — qavs shart</h3>

<p>Mana bu joyda eng koʻp ball yoʻqoladi. Manfiy sonni ifodaga qoʻyayotganda uni
<b>qavsga oling</b>. Aks holda minus qayerga tegishli ekani chalkashadi (PM-11).</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3a<sup>2</sup>, a = −2</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 × (−2)<sup>2</sup></span>
    <span class="pm-solve__why">Manfiy son qavsda — daraja butun songa tegishli</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 × 4</span>
    <span class="pm-solve__why">(−2) × (−2) = 4 — ikki minus plyus beradi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 12</span>
    <span class="pm-solve__why">Javob musbat</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">3a<sup>2</sup> va (3a)<sup>2</sup> — ikki boshqa ifoda</p>
  <p>3a<sup>2</sup> da faqat <b>a</b> kvadratga koʻtariladi: a = 2 boʻlsa 3 × 4 = 12.
  (3a)<sup>2</sup> da esa butun koʻpaytma: (3 × 2)<sup>2</sup> = 36. Daraja faqat oʻzi
  turgan narsaga tegishli — qavs boʻlmasa, bitta belgiga.</p>
</div>

<h3>4. Qiymatlar jadvali</h3>

<p>Bitta ifodani bir necha qiymatda hisoblab jadvalga yozsak, uning <b>xulqi</b>
koʻrinadi. Bu — keyingi bloklardagi grafikning bevosita otasi.</p>

<div class="pe-table-wrap"><table>
  <tr><th>n</th><th>0</th><th>1</th><th>2</th><th>5</th><th>10</th></tr>
  <tr><td>4n</td><td>0</td><td>4</td><td>8</td><td>20</td><td>40</td></tr>
  <tr><td>4n + 6</td><td>6</td><td>10</td><td>14</td><td>26</td><td>46</td></tr>
  <tr><td>100 − 4n</td><td>100</td><td>96</td><td>92</td><td>80</td><td>60</td></tr>
</table></div>

<p>Jadvalni oʻqing: 4n har qadamda 4 taga oʻsadi; 4n + 6 ham shunday oʻsadi, faqat
doim 6 taga yuqorida turadi; 100 − 4n esa aksincha, har qadamda 4 taga <b>kamayadi</b>.
Harf oldidagi son — oʻsish tezligi, harfsiz son — boshlangʻich holat.</p>

<h3>Matnli masala</h3>

<p><b>Elektr hisobi.</b> Har oy abonent toʻlovi 15 000 soʻm olinadi, ustiga har bir
kilovatt-soat uchun 450 soʻm qoʻshiladi. Oylik toʻlov ifodasi: <b>15 000 + 450k</b>,
bu yerda k — sarflangan kilovatt-soat.</p>

<p><b>Savol:</b> oilada 120 kilovatt-soat sarflandi. Toʻlov qancha? Keyingi oy sarf
160 ga chiqsa-chi?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">k = 120: 15 000 + 450 × 120</span>
    <span class="pm-solve__why">Harf oʻrniga sonni qoʻydik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">450 × 120 = 54 000</span>
    <span class="pm-solve__why">Avval koʻpaytirish</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">15 000 + 54 000 = 69 000 soʻm</span>
    <span class="pm-solve__why">Birinchi oyning toʻlovi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">k = 160: 15 000 + 72 000 = 87 000 soʻm</span>
    <span class="pm-solve__why">Sarf 40 ga oshdi — toʻlov 18 000 ga oshdi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Farqni alohida hisoblaymiz: 40 kilovatt-soat × 450 = 18 000 soʻm ✓ Va
  69 000 + 18 000 = 87 000 ✓ Ikki yoʻl bir xil javob berdi.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>450 taxminan 500; 120 × 500 = 60 000. Ustiga abonent toʻlovi — javob 70 000
  atrofida chiqishi kerak edi.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">3a, a = 4 → 34</p>
  <p class="pe-fix__good">3a, a = 4 → 3 × 4 = 12</p>
  <p class="pe-fix__why">Harf oʻrniga son qoʻyilganda koʻpaytirish belgisi qaytadi.
  Yonma-yon yozish faqat harf bilan ishlaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">2 + 3a, a = 5 → 5 × 5 = 25</p>
  <p class="pe-fix__good">2 + 3 × 5 = 2 + 15 = 17</p>
  <p class="pe-fix__why">Amallar tartibi buzilgan: avval qoʻshib, keyin koʻpaytirilgan.
  Koʻpaytirish har doim oldin bajariladi (PM-5).</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">a<sup>2</sup>, a = −3 → −9</p>
  <p class="pe-fix__good">(−3)<sup>2</sup> = 9</p>
  <p class="pe-fix__why">Manfiy son qavsga olinmagan. (−3) × (−3) = 9 — ikki manfiyning
  koʻpaytmasi musbat (PM-11). Minus qavssiz qolsa, u darajadan tashqarida qoladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 5a − 3 ifodasining a = 4 dagi qiymatini toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>17.</b> 5 × 4 = 20, keyin 20 − 3 = 17.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 4a + 2b ifodasining a = 3, b = 6 dagi qiymatini toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>24.</b> 4 × 3 = 12 va 2 × 6 = 12; 12 + 12 = 24.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. a<sup>2</sup> + 1 ifodasining a = 7 dagi qiymatini toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>50.</b> 7 × 7 = 49, keyin 49 + 1 = 50.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 10 − 2x ifodasining x = −3 dagi qiymatini toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>16.</b> 10 − 2 × (−3) = 10 − (−6) = 10 + 6 = 16. Manfiyni ayirish —
    qoʻshish (PM-10).</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Sinf ekskursiyaga chiqmoqchi. Avtobus 400 000 soʻm turadi,
  har bir oʻquvchining chiptasi esa 25 000 soʻm. Xarajat ifodasi: 400 000 + 25 000n.
  24 oʻquvchi borsa, jami qancha boʻladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>1 000 000 soʻm.</b> 25 000 × 24 = 600 000; 400 000 + 600 000 = 1 000 000.
    Tekshirish: avtobus barcha uchun bitta, shuning uchun u n ga koʻpaytirilmaydi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Oʻrniga qoʻyish</b><span>harf oʻrniga son yozish; ingl. substitution</span></li>
  <li><b>Ifodaning qiymati</b><span>hisoblab chiqilgan natija; ingl. value of an
    expression</span></li>
  <li><b>Amallar tartibi</b><span>qaysi amal avval bajarilishi; ingl. order of
    operations</span></li>
  <li><b>Qavs</b><span>avval bajariladigan qismni ajratadi; ingl. brackets</span></li>
  <li><b>Daraja</b><span>takroriy koʻpaytirish; ingl. power</span></li>
  <li><b>Qiymatlar jadvali</b><span>ifodaning bir necha qiymati; ingl. table of
    values</span></li>
  <li><b>Manfiy son</b><span>noldan kichik son; ingl. negative number</span></li>
  <li><b>Birlik</b><span>javobning oʻlchovi: soʻm, kg, km; ingl. unit</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Harf oʻrniga son — koʻpaytirish belgisi qaytadi:</b> 3a, a = 4 → 3 × 4.</li>
    <li><b>Amallar tartibi saqlanadi:</b> avval daraja va qavs, keyin koʻpaytirish,
      oxirida qoʻshish.</li>
    <li><b>Manfiy sonni qavsga oling:</b> a = −3 boʻlsa a<sup>2</sup> = (−3)<sup>2</sup>
      = 9.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-32 — oʻxshash hadlarni ixchamlash
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-32: Oʻxshash hadlarni ixchamlash",
        "category": "math",
        "order": 32,
        "summary": (
            "Uzun ifodani qisqartirish: oʻxshash hadlar nima, ular qanday "
            "qoʻshiladi va nima uchun 3a bilan 5b ni birlashtirib boʻlmaydi."
        ),
        "stories": ["Omborni tartibga solish"],
        "content": """
<h2>PM-32: Oʻxshash hadlarni ixchamlash</h2>

<p>Karim akaning omborida shunday roʻyxat turibdi: «5 quti, 3 qop, 2 quti, 1 qop».
Hech kim bunday yozmaydi — normal odam avval qutilarni bir joyga, qoplarni bir joyga
yigʻadi: <b>7 quti va 4 qop</b>. Algebrada bu ish <b>ixchamlash</b> deb ataladi va
u xuddi shunday oddiy.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>ifodaning hadlarini ajratasiz;</li>
    <li>oʻxshash hadlarni tanib olasiz;</li>
    <li>ularni qoʻshib ifodani qisqartirasiz;</li>
    <li>nima uchun 3a + 5b ni ixchamlab boʻlmasligini tushunasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Oʻxshash hadlar</span>
  <span class="pe-chip pe-chip--o">harf qismi bir xil</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">koeffitsientlar qoʻshiladi</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">3a + 5a = 8a</span>
</div>

<h3>1. Had nima</h3>

<p>Ifoda qoʻshish va ayirish belgilari bilan boʻlaklarga ajraladi. Har bir boʻlak —
<b>had</b>. <b>4a + 3b − a + 2b</b> ifodasida toʻrtta had bor: 4a, +3b, −a, +2b.</p>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Ishora hadning oʻziga tegishli</p>
  <p>Hadni ajratganda undan oldingi belgini ham birga olasiz. −a — bu «minus a»
  degan had, «a» emas. Shu odat butun algebrani xatodan saqlaydi.</p>
</div>

<h3>2. Qaysi hadlar oʻxshash</h3>

<p>Ikki had <b>harf qismi bir xil</b> boʻlsa, ular oʻxshash. Koeffitsient (harf
oldidagi son) har xil boʻlsa ham mayli — u faqat nechtaligini aytadi.</p>

<div class="pe-table-wrap"><table>
  <tr><th>Hadlar</th><th>Oʻxshashmi?</th><th>Nega</th></tr>
  <tr><td>3a va 5a</td><td>ha</td><td>ikkalasida ham harf qismi a</td></tr>
  <tr><td>7x va −2x</td><td>ha</td><td>ishora farqi ahamiyatsiz</td></tr>
  <tr><td>4m va m</td><td>ha</td><td>m — bu 1m</td></tr>
  <tr><td>3a va 5b</td><td>yoʻq</td><td>harflar boshqa</td></tr>
  <tr><td>a<sup>2</sup> va a</td><td>yoʻq</td><td>darajalar boshqa</td></tr>
  <tr><td>6 va 9</td><td>ha</td><td>ikkalasi ham harfsiz — ozod hadlar</td></tr>
</table></div>

<h3>3. Ixchamlash — sanashning oʻzi</h3>

<p>Oʻxshash hadlarni qoʻshish uchun <b>koeffitsientlarni qoʻshamiz</b>, harf qismi
oʻzgarmaydi. Sababi juda oddiy: 3a + 5a degani «uchta a va yana beshta a».</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">3a</span>
    <span class="pm-model__bar" style="width:30%">a a a</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">5a</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:50%">a a a a a</span>
  </div>
  <p class="pm-model__tot">Jami sakkizta a — yaʼni 8a</p>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">4a + 3b − a + 2b</span>
    <span class="pm-solve__why">Berilgan ifoda</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(4a − a) + (3b + 2b)</span>
    <span class="pm-solve__why">Oʻxshashlarni yonma-yon toʻpladik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 3a + 5b</span>
    <span class="pm-solve__why">Toʻrtta haddan ikkitasi qoldi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Ikkala ifodaga bir xil sonlarni qoʻyamiz (PM-31). a = 2, b = 3:
  boshlangʻich ifoda 8 + 9 − 2 + 6 = 21; qisqargani 6 + 15 = 21 ✓ <b>Ixchamlash
  qiymatni oʻzgartirmaydi</b> — u faqat yozuvni qisqartiradi. Bu tekshiruvni har
  safar qiling.</p>
</div>

<h3>4. Nega 3a + 5b ixchamlanmaydi</h3>

<p>Chunki ular <b>har xil narsa</b>. Uchta quti va besh qopni qoʻshib «sakkizta» deb
boʻlmaganidek. Javob shunchaki <b>3a + 5b</b> boʻlib qolaveradi — va bu toʻliq javob,
tugallanmagan emas.</p>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Javob bitta had boʻlishi shart emas</p>
  <p>Koʻp oʻquvchi «javob bitta son yoki bitta had boʻlishi kerak» deb oʻylaydi va
  3a + 5b ni zoʻrlab 8ab ga aylantiradi. Bu xato. Ixchamlangan ifodada nechta har xil
  harf qismi boʻlsa, shuncha had qoladi.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Javobni tartib bilan yozing</p>
  <p>Ixchamlangan javobda avval harfli hadlar (alifbo tartibida), oxirida ozod had
  yoziladi: <b>3a + 5b + 7</b>. Bu shart emas, lekin shunday yozilgan javobni
  tekshirish ham, oʻqish ham osonroq — va keyingi qadamda xato kamayadi.</p>
</div>

<h3>5. Uzunroq ifodalar</h3>

<p>Hadlar koʻp boʻlsa, avval ularni turlarga ajratib chiqing — xuddi omborda.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">5x + 3 − 2x + 7</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(5x − 2x) + (3 + 7)</span>
    <span class="pm-solve__why">x li hadlar va ozod hadlar alohida</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 3x + 10</span>
    <span class="pm-solve__why">Har guruh oʻzi qoʻshildi</span>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">6y − 2y + 3y = 7y</p>
  <p class="pe-ex__uz">Oltita y dan ikkitasi ketdi, uchtasi qoʻshildi — yettita y.</p>
  <p class="pe-ex__why">Koeffitsientlar: 6 − 2 + 3 = 7.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">7m − m = 6m</p>
  <p class="pe-ex__uz">Yettita m dan bittasi ayirildi.</p>
  <p class="pe-ex__why">m — bu 1m. Koʻrinmayotgan koeffitsient har doim 1.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Omborda hisob.</b> Karim akaning omborida ikki xil idish bor: quti va qop. Bitta
qutida a kilogramm, bitta qopda b kilogramm un boʻladi. Ertalab omborga 5 quti va
3 qop keldi. Kun davomida 2 quti va 1 qop sotildi. Kechqurun yana 4 quti keltirildi.</p>

<p><b>Savol:</b> ombordagi unni bitta ifoda bilan yozing. Quti 15 kg, qop 50 kg
boʻlsa, ombordagi un necha kilogramm?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">5a + 3b − 2a − b + 4a</span>
    <span class="pm-solve__why">Har harakatni oʻz ishorasi bilan yozdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(5a − 2a + 4a) + (3b − b)</span>
    <span class="pm-solve__why">Qutilar bir guruh, qoplar boshqa guruh</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= 7a + 2b</span>
    <span class="pm-solve__why">Yetti quti va ikki qop qolibdi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">7 × 15 + 2 × 50 = 105 + 100 = 205 kg</span>
    <span class="pm-solve__why">Oʻrniga qoʻyish (PM-31) — omborda 205 kg un bor</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Ixchamlamasdan sanaymiz: 5 × 15 + 3 × 50 − 2 × 15 − 50 + 4 × 15 =
  75 + 150 − 30 − 50 + 60 = 205 ✓ Bir xil javob, lekin ikki barobar koʻp ish.
  Ixchamlash aynan shuning uchun kerak.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">3a + 5b = 8ab</p>
  <p class="pe-fix__good">3a + 5b — ixchamlanmaydi</p>
  <p class="pe-fix__why">Har xil harf qismli hadlar qoʻshilmaydi. Tekshirish: a = 1,
  b = 1 boʻlsa chapda 8 chiqadi, lekin a = 2, b = 1 boʻlsa chapda 11, oʻngda esa 16 —
  teng emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">4a + 3a = 7a<sup>2</sup></p>
  <p class="pe-fix__good">4a + 3a = 7a</p>
  <p class="pe-fix__why">Qoʻshganda harf qismi <b>oʻzgarmaydi</b>. Daraja faqat
  koʻpaytirishda oʻsadi. Tekshirish: a = 2 boʻlsa 8 + 6 = 14, 7a esa 14 ✓,
  7a<sup>2</sup> esa 28 ✗</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">6x − x = 6</p>
  <p class="pe-fix__good">6x − x = 5x</p>
  <p class="pe-fix__why">x butunlay yoʻqolib ketmaydi: undan bittasi ayirildi, xolos.
  Koʻrinmayotgan koeffitsient 1 ni unutmang.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 7a + 2a ni ixchamlang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>9a.</b> Koeffitsientlar qoʻshiladi: 7 + 2 = 9.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 8x − 3x + x ni ixchamlang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>6x.</b> 8 − 3 + 1 = 6. Oxirgi hadning koeffitsienti 1.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 5m + 4n − 2m + n ni ixchamlang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3m + 5n.</b> m li hadlar: 5 − 2 = 3; n li hadlar: 4 + 1 = 5. Ikki xil harf
    qoldi — bu toʻliq javob.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 2a + 7 + 3a − 4 ni ixchamlang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5a + 3.</b> Harfli hadlar 2 + 3 = 5; ozod hadlar 7 − 4 = 3.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Doʻkonda bitta daftar a soʻm, bitta ruchka b soʻm. Afsona
  4 daftar va 2 ruchka oldi, keyin yana 3 daftar oldi, lekin bitta ruchkani qaytardi.
  Xarajatini ixchamlang va a = 6000, b = 4000 boʻlsa hisoblang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>7a + b = 46 000 soʻm.</b> Daftarlar: 4 + 3 = 7 ta; ruchkalar: 2 − 1 = 1 ta.
    Keyin 7 × 6000 + 4000 = 42 000 + 4000 = 46 000 soʻm.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Had</b><span>ifodaning qoʻshish belgilari bilan ajratilgan boʻlagi; ingl.
    term</span></li>
  <li><b>Oʻxshash hadlar</b><span>harf qismi bir xil hadlar; ingl. like terms</span></li>
  <li><b>Koeffitsient</b><span>harf oldidagi son; ingl. coefficient</span></li>
  <li><b>Harf qismi</b><span>haddagi harflar va ularning darajalari; ingl. literal
    part</span></li>
  <li><b>Ozod had</b><span>harfsiz son; ingl. constant term</span></li>
  <li><b>Ixchamlash</b><span>oʻxshash hadlarni qoʻshib yozuvni qisqartirish; ingl.
    collecting like terms</span></li>
  <li><b>Ishora</b><span>hadning plyus yoki minusi; ingl. sign</span></li>
  <li><b>Teng ifodalar</b><span>hamma qiymatda bir xil natija beruvchi ifodalar; ingl.
    equivalent expressions</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Oʻxshash hadlar — harf qismi bir xil boʻlganlari.</b> a<sup>2</sup> va a
      oʻxshash emas.</li>
    <li><b>Ixchamlashda koeffitsientlar qoʻshiladi</b>, harf qismi oʻzgarmaydi.</li>
    <li><b>Ishorani had bilan birga oling</b> va tekshirish uchun son qoʻyib
      koʻring.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-33 — qavslarni ochish va ishoralar
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-33: Qavslarni ochish va ishoralar",
        "category": "math",
        "order": 33,
        "summary": (
            "Taqsimot qonuni: 3(x + 4) = 3x + 12. Qavs oldidagi minus nima uchun "
            "hamma ishorani almashtiradi va qavs ochilgach ifoda qanday "
            "ixchamlanadi."
        ),
        "stories": ["Toʻrt qutida nechta?"],
        "content": """
<h2>PM-33: Qavslarni ochish va ishoralar</h2>

<p>Toʻrtta bir xil paket bor. Har birida <b>n</b> ta kitob va yana 3 ta daftar. Jami
nechta narsa? Ikki xil sanash mumkin: «toʻrtta paket, har birida n + 3 ta» —
<b>4(n + 3)</b>; yoki «toʻrtta n va oʻn ikkita daftar» — <b>4n + 12</b>. Ikkala
javob ham toʻgʻri, chunki ular bir xil. Shu tenglikning nomi — taqsimot qonuni.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>qavsni koʻpaytuvchi bilan ochasiz;</li>
    <li>qavs oldidagi minus bilan ishlaysiz;</li>
    <li>ochilgan ifodani ixchamlaysiz;</li>
    <li>javobni son qoʻyib tekshirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Taqsimot qonuni</span>
  <span class="pe-chip pe-chip--o">a(b + c) = ab + ac</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">−(b + c) = −b − c</span>
</div>

<h3>1. Koʻpaytuvchi har bir hadga tarqaladi</h3>

<p>Qavs oldidagi son ichkaridagi <b>har bir hadga</b> koʻpaytiriladi — bittasiga
emas, hammasiga. Shuning uchun qonun «taqsimot» deb ataladi.</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">1-paket</span>
    <span class="pm-model__bar" style="width:25%">n + 3</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">2-paket</span>
    <span class="pm-model__bar" style="width:25%">n + 3</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">3-paket</span>
    <span class="pm-model__bar" style="width:25%">n + 3</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">4-paket</span>
    <span class="pm-model__bar" style="width:25%">n + 3</span>
  </div>
  <p class="pm-model__tot">4(n + 3) = 4n + 12 — toʻrtta n va toʻrtta uchlik</p>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3(x + 4)</span>
    <span class="pm-solve__why">Berilgan ifoda</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 × x + 3 × 4</span>
    <span class="pm-solve__why">Uchni ikkala hadga ham koʻpaytirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 3x + 12</span>
    <span class="pm-solve__why">Qavs ochildi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>x = 5 qoʻyamiz: 3 × (5 + 4) = 3 × 9 = 27; ochilgan koʻrinishda 15 + 12 = 27 ✓
  <b>Qavs ochish qiymatni oʻzgartirmaydi.</b></p>
</div>

<h3>2. Ichkarida ayirish boʻlsa</h3>

<p>Qoida oʻzgarmaydi: koʻpaytuvchi ikkala hadga ham tarqaladi, ishoralar esa oʻz
joyida qoladi.</p>

<div class="pe-ex">
  <p class="pe-ex__math">2(a − 5) = 2a − 10</p>
  <p class="pe-ex__uz">Ikkitasi a dan va ikkitasi beshlikdan.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">−3(a − 2) = −3a + 6</p>
  <p class="pe-ex__uz">Manfiy koʻpaytuvchi ikkala hadning ham ishorasini oʻzgartiradi.</p>
  <p class="pe-ex__why">(−3) × (−2) = +6 — ikki manfiyning koʻpaytmasi musbat
  (PM-11).</p>
</div>

<h3>3. Qavs oldidagi minus — eng koʻp xato qilinadigan joy</h3>

<p>Qavs oldida yolgʻiz minus tursa, u aslida <b>−1</b> ga koʻpaytirish degani. Demak
qavs ichidagi <b>hamma ishora</b> almashadi.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Qavs oldida plyus</p>
    <p><b>5 + (x − 3) = 5 + x − 3</b><br>Ishoralar oʻzgarmaydi — qavsni shunchaki
    oʻchirsangiz boʻladi.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Qavs oldida minus</p>
    <p><b>5 − (x − 3) = 5 − x + 3</b><br>Ikkala ishora ham almashdi: x manfiy boʻldi,
    −3 esa +3 boʻldi.</p>
  </div>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">5 − (x − 3)</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5 + (−1) × x + (−1) × (−3)</span>
    <span class="pm-solve__why">Minusni −1 deb yozdik va taqsimladik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5 − x + 3</span>
    <span class="pm-solve__why">Ikkala ishora ham almashdi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 8 − x</span>
    <span class="pm-solve__why">Ozod hadlarni ixchamladik (PM-32)</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Minusdan keyin faqat birinchi had emas, HAMMASI oʻzgaradi</p>
  <p>5 − (x − 3) = 5 − x − 3 degan javob — bu darsdagi eng koʻp uchraydigan xato.
  Tekshirib koʻring: x = 4 boʻlsa, asl ifoda 5 − 1 = 4 beradi; notoʻgʻri javob esa
  5 − 4 − 3 = −2. Butunlay boshqa son.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Qavsni «oʻchirib» boʻlmaydi</p>
  <p>Qavs oldida son tursa, uni shunchaki oʻchirib tashlash mumkin emas: 3(x + 4)
  hech qachon x + 4 ga teng emas. Qavs faqat <b>koʻpaytirish bajarilgandan keyin</b>
  yoʻqoladi. Oldida plyus tursa esa (masalan 5 + (x − 3)) — u haqiqatan ham
  shunchaki oʻchiriladi.</p>
</div>

<h3>4. Ochish va ixchamlash birga</h3>

<p>Odatda masala ikki qadamdan iborat: avval hamma qavs ochiladi, keyin oʻxshash
hadlar yigʻiladi. Tartibni buzmang — bu keyingi darslarda tenglama yechishning
tayyorgarligi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2(x + 3) + 3(x − 1)</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + 6 + 3x − 3</span>
    <span class="pm-solve__why">Ikkala qavs ochildi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 5x + 3</span>
    <span class="pm-solve__why">2x + 3x = 5x; 6 − 3 = 3</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>x = 2: boshlangʻich ifoda 2 × 5 + 3 × 1 = 13; javob 5 × 2 + 3 = 13 ✓</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">4(2a + 1) − 3(a − 2) = 8a + 4 − 3a + 6 = 5a + 10</p>
  <p class="pe-ex__uz">Ikkinchi qavs oldida minus — uning ichidagi ishoralar almashdi.</p>
  <p class="pe-ex__why">a = 3 da tekshiruv: 4 × 7 − 3 × 1 = 25 va 5 × 3 + 10 = 25 ✓</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Javobni bir son bilan tekshiring — 10 sekund</p>
  <p>Qavs ochgandan keyin ifodaga istalgan sonni qoʻying (x = 2 qulay) va boshlangʻich
  ifodaga ham oʻsha sonni qoʻying. Ikkalasi bir xil chiqsa — ochish toʻgʻri. Bu odat
  ishoralar bilan bogʻliq xatolarning deyarli hammasini tutadi.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Kutubxonaga kitob.</b> Kutubxonaga toʻrtta bir xil paket keldi. Har bir paketda
n ta kitob va 3 ta daftar bor. Kutubxonachi paketlardan ikkitasidan bittadan kitobni
tekshirish uchun oldi.</p>

<p><b>Savol:</b> kutubxonada qolgan narsalar sonini ifoda bilan yozing va n = 12
boʻlsa hisoblang.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">4(n + 3) − 2</span>
    <span class="pm-solve__why">Toʻrt paket, ulardan ikkita kitob olindi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4n + 12 − 2</span>
    <span class="pm-solve__why">Qavsni ochdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= 4n + 10</span>
    <span class="pm-solve__why">Ozod hadlar ixchamlandi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">n = 12: 48 + 10 = 58 ta</span>
    <span class="pm-solve__why">Kutubxonada 58 ta narsa qoldi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Boshqa yoʻl: har paketda 12 + 3 = 15 ta narsa; toʻrt paket — 60 ta; ikkita kitob
  olindi — 58 ta ✓ Ikkala hisob ham bir xil.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Har paketda oʻn beshtaga yaqin narsa, toʻrt paket — oltmishga yaqin. Javob
  60 atrofida chiqishi kerak edi.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">3(x + 4) = 3x + 4</p>
  <p class="pe-fix__good">3(x + 4) = 3x + 12</p>
  <p class="pe-fix__why">Koʻpaytuvchi faqat birinchi hadga tarqatilgan. U <b>har bir</b>
  hadga koʻpaytiriladi. Tekshirish: x = 1 da asl ifoda 15, notoʻgʻri javob 7.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">10 − (a − 4) = 10 − a − 4</p>
  <p class="pe-fix__good">10 − (a − 4) = 10 − a + 4 = 14 − a</p>
  <p class="pe-fix__why">Qavs oldidagi minus <b>ikkala</b> ishorani almashtiradi.
  Tekshirish: a = 6 da asl ifoda 10 − 2 = 8, toʻgʻri javob 14 − 6 = 8 ✓</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">−2(a − 3) = −2a − 6</p>
  <p class="pe-fix__good">−2(a − 3) = −2a + 6</p>
  <p class="pe-fix__why">(−2) × (−3) = +6. Ikki manfiyning koʻpaytmasi musbat —
  ishoralar qoidasi (PM-11) qavs ochishda ham xuddi shunday ishlaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 5(x + 2) qavsini oching.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5x + 10.</b> Beshlik ikkala hadga ham koʻpaytiriladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 3(2a − 4) qavsini oching.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>6a − 12.</b> 3 × 2a = 6a va 3 × (−4) = −12.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 12 − (x − 5) ni soddalashtiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>17 − x.</b> Minus ikkala ishorani almashtiradi: 12 − x + 5, keyin ozod
    hadlar qoʻshiladi. Tekshirish: x = 3 da 12 − (−2) = 14 va 17 − 3 = 14 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 3(x + 2) + 2(x − 1) ni soddalashtiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5x + 4.</b> 3x + 6 + 2x − 2; keyin 3x + 2x = 5x va 6 − 2 = 4.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Uchta bir xil sovgʻa xalta tayyorlandi. Har xaltada a soʻmlik
  shirinlik va 5000 soʻmlik oʻyinchoq bor. Xarajatni ifoda bilan yozing, qavsni oching
  va a = 20 000 boʻlsa hisoblang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3(a + 5000) = 3a + 15 000 = 75 000 soʻm.</b> a = 20 000 boʻlsa
    3 × 20 000 = 60 000, ustiga 15 000 — jami 75 000. Tekshirish: bitta xalta
    25 000 soʻm, uchtasi 75 000 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Qavs ochish</b><span>koʻpaytuvchini hadlarga tarqatish; ingl. expanding
    brackets</span></li>
  <li><b>Taqsimot qonuni</b><span>a(b + c) = ab + ac; ingl. distributive law</span></li>
  <li><b>Koʻpaytuvchi</b><span>qavs oldidagi son yoki harf; ingl. factor</span></li>
  <li><b>Ishora</b><span>hadning plyus yoki minusi; ingl. sign</span></li>
  <li><b>Soddalashtirish</b><span>qavsni ochib, oʻxshash hadlarni yigʻish; ingl.
    simplify</span></li>
  <li><b>Ozod had</b><span>harfsiz son; ingl. constant term</span></li>
  <li><b>Teng ifodalar</b><span>hamma qiymatda bir xil natija beradigan ifodalar;
    ingl. equivalent expressions</span></li>
  <li><b>Ichki ifoda</b><span>qavs ichidagi qism; ingl. inner expression</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Koʻpaytuvchi har bir hadga tarqaladi:</b> 3(x + 4) = 3x + 12.</li>
    <li><b>Qavs oldidagi minus hamma ishorani almashtiradi:</b> 5 − (x − 3) =
      8 − x.</li>
    <li><b>Avval ochamiz, keyin ixchamlaymiz</b> — va javobni son qoʻyib
      tekshiramiz.</li>
  </ul>
</div>
""",
    },
]
