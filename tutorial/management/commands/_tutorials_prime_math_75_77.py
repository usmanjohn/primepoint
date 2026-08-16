# -*- coding: utf-8 -*-
"""Prime Math — darslar 75–77 (maʼlumot, diagramma turlari, diagramma oʻqish).

**Blok F: Maʼlumot va ehtimollik (75–84) ning boshi.**
Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt

  mashqlar — practice/management/commands/_practice_pm_75_77.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_75_77.py

⚠️ Blok F chizmalarni oʻzgartiradi: geometriya figuralari oʻrniga
   DIAGRAMMALAR. Ular uchun style.css ga `pm-ch__*` kiti qoʻshildi va
   STYLE_GUIDE_PRIME_MATH.md 5-boʻlimiga «Diagrammalar» yozildi.
   RANG QOIDASI hisoblangan, tanlanmagan:
     • ustunli/chiziqli — bitta seriya, bitta rang (ustun uzunligi sonni
       allaqachon koʻrsatadi; qiymatga qarab boʻyash legenda talab qiladi
       va identiflik kanalini behuda sarflaydi);
     • doiraviy — bitta hue ning 4 ta yorqinlik bosqichi, boʻlaklar
       kattaligi boʻyicha tartiblangan. Toʻrt xil hue rang koʻrligida
       ajralmaydi, yorqinlik esa ajraladi — va A5 kitob oq-qora chiqadi;
     • har bir ustun va boʻlak YOZUV bilan belgilangan, shuning uchun
       hech bir diagrammaga legenda kerak emas.
   Chizmalar generatsiya qilingan: scratchpad/gen_pm75_77.py, va
   verify_pm_75_77.py har bir ustun balandligini hamda har bir
   sektor burchagini maʼlumotdan qayta oʻlchaydi.

⚠️ Kumulyativ chegaralar — bu uchlikda juda muhim:
  • PM-75 — faqat maʼlumot yigʻish va JADVAL. ⛔ DIAGRAMMA YOʻQ:
    na darsda, na mashqda, na matnda (diagramma PM-76 da kiradi);
  • PM-76 — uchta diagramma turi va qaysi birini tanlash.
    ⛔ Diagrammani chuqur OʻQISH (farq, jami, sakrash) PM-77 da;
  • PM-77 — diagrammani oʻqish. ⛔ Oʻrta arifmetik (PM-78), mediana
    (PM-79), tarqoqlik (PM-80) va aldamchi diagrammalar (PM-81) YOʻQ —
    «oʻrtacha» soʻzi atama sifatida ishlatilmaydi.
  • Faol ishlatiladi: foiz (PM-23), foiz oʻzgarishi (PM-25), doira va
    burchak (PM-58, PM-70), yaxlitlash (PM-14), jadval bilan ishlash.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_75_77.py --author=prime
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
    # PM-75 — maʼlumot yigʻish va jadval
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-75: Maʼlumot yigʻish va uni jadvalga solish",
        "category": "math",
        "order": 75,
        "summary": (
            "Har qanday statistika bitta savoldan boshlanadi. Maʼlumotni "
            "qanday yigʻish, chiziqcha bilan sanash va chastota jadvaliga "
            "solishni — hamda savolning oʻzi javobni qanday buzishini koʻrasiz."
        ),
        "stories": ["Sinfda kim nima yeydi — soʻrovnoma hisoboti"],
        "content": """
<h2>PM-75: Maʼlumot yigʻish va uni jadvalga solish</h2>

<p>Ertaga yomgʻir yogʻishini ob-havo xizmati qayerdan biladi? Doʻkon
qaysi nonni koʻproq keltirishni qayerdan biladi? Ikkalasi ham bitta
narsadan: <b>yigʻilgan maʼlumot</b>dan.</p>

<p>Bu boʻlim — matematikaning hayotga eng yaqin qismi. Va u har doim
bitta savoldan boshlanadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>aniq javob beradigan savol tuzasiz;</li>
    <li>maʼlumot yigʻishning toʻrt yoʻlini ajratasiz;</li>
    <li>chiziqcha bilan tez va xatosiz sanaysiz;</li>
    <li>chastota jadvalini toʻldirib, foizini topasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Toʻrt qadam</span>
  <span class="pe-chip pe-chip--s">savol</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">yigʻish</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">jadval</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">xulosa</span>
</div>

<h3>1. Hammasi savoldan boshlanadi</h3>

<p><b>Maʼlumot</b> — bu yigʻilgan faktlar: sonlar, javoblar, oʻlchov
natijalari. Lekin maʼlumot oʻz-oʻzidan yigʻilmaydi. Avval nimani bilmoqchi
ekaningizni <b>aniq</b> aytishingiz kerak.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Yomon savol</p>
    <p>«Oʻquvchilar sogʻlom ovqatlanadimi?» — «sogʻlom» degani nima?
    Kimni soʻraymiz? Nima bilan oʻlchaymiz?</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Yaxshi savol</p>
    <p>«6-A sinfning 20 oʻquvchisidan har biri qaysi mevani eng koʻp
    yoqtiradi?» — kim, nechta va nima soʻralishi aniq.</p>
  </div>
</div>

<h3>2. Maʼlumotni qanday yigʻish mumkin</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Usul</th><th>Nima qilinadi</th><th>Misol</th></tr>
  <tr><td>Soʻrovnoma</td>
    <td class="pm-word__sym">soʻraymiz</td>
    <td>sevimli meva, qaysi transportda kelasiz</td></tr>
  <tr><td>Kuzatish</td>
    <td class="pm-word__sym">sanaymiz</td>
    <td>bir soatda darvozadan nechta mashina oʻtdi</td></tr>
  <tr><td>Oʻlchash</td>
    <td class="pm-word__sym">oʻlchaymiz</td>
    <td>har kuni soat 12 dagi harorat</td></tr>
  <tr><td>Tayyor manba</td>
    <td class="pm-word__sym">olamiz</td>
    <td>sinf jurnali, doʻkon daftari</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Kimdan soʻraganingiz javobni oʻzgartiradi</p>
  <p>«Maktabda futbolni kim yoqtiradi?» degan savolni <b>futbol
  toʻgaragida</b> soʻrasangiz, javob 100% chiqadi — lekin bu butun
  maktab haqida hech nima demaydi. Kimdan soʻralganini har doim yozib
  qoʻying: <em>«6-A sinfning 20 oʻquvchisi»</em>. Bu son javobning bir
  qismi.</p>
</div>

<h3>3. Chiziqcha bilan sanash</h3>

<p>Yigʻayotganda javoblarni darrov sonlarga aylantirmang — <b>chiziqcha
qoʻying</b>. Har beshinchisi qiya tortiladi, shunda beshtadan sanash
oson boʻladi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 200" role="img" aria-label="Chiziqcha bilan sanash: olma 8, uzum 5, shaftoli 4, anor 3">
    <text class="pm-ch__lbl" x="12" y="47">olma</text>
    <line class="pm-ch__ax" x1="96" y1="31" x2="96" y2="53"/>
    <line class="pm-ch__ax" x1="103" y1="31" x2="103" y2="53"/>
    <line class="pm-ch__ax" x1="110" y1="31" x2="110" y2="53"/>
    <line class="pm-ch__ax" x1="117" y1="31" x2="117" y2="53"/>
    <line class="pm-ch__ax" x1="92" y1="53" x2="121" y2="31"/>
    <line class="pm-ch__ax" x1="140" y1="31" x2="140" y2="53"/>
    <line class="pm-ch__ax" x1="147" y1="31" x2="147" y2="53"/>
    <line class="pm-ch__ax" x1="154" y1="31" x2="154" y2="53"/>
    <text class="pm-ch__val" x="300" y="47" text-anchor="end">8</text>
    <text class="pm-ch__lbl" x="12" y="85">uzum</text>
    <line class="pm-ch__ax" x1="96" y1="69" x2="96" y2="91"/>
    <line class="pm-ch__ax" x1="103" y1="69" x2="103" y2="91"/>
    <line class="pm-ch__ax" x1="110" y1="69" x2="110" y2="91"/>
    <line class="pm-ch__ax" x1="117" y1="69" x2="117" y2="91"/>
    <line class="pm-ch__ax" x1="92" y1="91" x2="121" y2="69"/>
    <text class="pm-ch__val" x="300" y="85" text-anchor="end">5</text>
    <text class="pm-ch__lbl" x="12" y="123">shaftoli</text>
    <line class="pm-ch__ax" x1="96" y1="107" x2="96" y2="129"/>
    <line class="pm-ch__ax" x1="103" y1="107" x2="103" y2="129"/>
    <line class="pm-ch__ax" x1="110" y1="107" x2="110" y2="129"/>
    <line class="pm-ch__ax" x1="117" y1="107" x2="117" y2="129"/>
    <text class="pm-ch__val" x="300" y="123" text-anchor="end">4</text>
    <text class="pm-ch__lbl" x="12" y="161">anor</text>
    <line class="pm-ch__ax" x1="96" y1="145" x2="96" y2="167"/>
    <line class="pm-ch__ax" x1="103" y1="145" x2="103" y2="167"/>
    <line class="pm-ch__ax" x1="110" y1="145" x2="110" y2="167"/>
    <text class="pm-ch__val" x="300" y="161" text-anchor="end">3</text>
    <text class="pm-ch__cap" x="300" y="20" text-anchor="end">jami 20</text>
  </svg>
  <figcaption>Beshinchi chiziqcha qiya tortiladi. Endi sanash uchun
  guruhlarni 5 dan sanab chiqish kifoya.</figcaption>
</figure>

<p>Olmani sanaymiz: bitta toʻliq guruh (5) va yana uchta chiziqcha —
5 + 3 = <b>8</b>. Bittalab sanaganda odam adashadi, beshtalab
sanaganda adashmaydi.</p>

<h3>4. Chastota jadvali</h3>

<p>Endi hammasini bitta jadvalga solamiz. Nechta marta uchraganini
<b>chastota</b> deymiz.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Meva</th><th>Chastota</th><th>Foizi</th></tr>
  <tr><td>Olma</td><td class="pm-word__sym">8</td><td>40%</td></tr>
  <tr><td>Uzum</td><td class="pm-word__sym">5</td><td>25%</td></tr>
  <tr><td>Shaftoli</td><td class="pm-word__sym">4</td><td>20%</td></tr>
  <tr><td>Anor</td><td class="pm-word__sym">3</td><td>15%</td></tr>
  <tr><td><b>Jami</b></td><td class="pm-word__sym">20</td>
    <td><b>100%</b></td></tr>
</table></div>

<p>Foiz PM-23 dagidek topiladi — ulushni jamiga boʻlib, 100 ga
koʻpaytiramiz:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">8 ÷ 20 = 0,4</span>
    <span class="pm-solve__why">Olmaning ulushi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">0,4 × 100 = 40%</span>
    <span class="pm-solve__why">Foizga oʻgirdik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Chastotalar: 8 + 5 + 4 + 3 = 20 ✓ — soʻralganlar soniga teng.
  <br>Foizlar: 40 + 25 + 20 + 15 = 100% ✓
  <br>Ikkalasi ham mos kelmasa — sanashda xato bor.</p>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Ikkita tekshiruv, har safar</p>
  <p>1. Chastotalar yigʻindisi = soʻralganlar soni.
  <br>2. Foizlar yigʻindisi = 100%.
  <br>Bu ikkisi jadvalni imzolashdan oldingi oxirgi qadam.</p>
</div>

<h3>Matnli masala</h3>

<p>Afsona maktab bufeti uchun soʻrov oʻtkazdi. U 50 oʻquvchidan
«Tanaffusda nima olasiz?» deb soʻradi. Javoblar: somsa 20 ta, patir
15 ta, pirog 10 ta, boshqalar 5 ta.</p>

<p>Bufetchi har kuni 100 dona pishiriq tayyorlaydi.</p>

<p><b>Har turdan nechtadan qilgani maʼqul?</b></p>

<p><b>Reja:</b> avval jadvalni tekshiramiz, foizlarni topamiz, keyin shu
foizlarni 100 donaga qoʻllaymiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">20 + 15 + 10 + 5 = 50</span>
    <span class="pm-solve__why">Soʻralganlar soniga toʻgʻri keldi ✓</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">20 ÷ 50 × 100 = 40%</span>
    <span class="pm-solve__why">Somsa</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">15 ÷ 50 × 100 = 30%</span>
    <span class="pm-solve__why">Patir</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">10 ÷ 50 × 100 = 20%; 5 ÷ 50 × 100 = 10%</span>
    <span class="pm-solve__why">Pirog va boshqalar</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">40, 30, 20 va 10 dona</span>
    <span class="pm-solve__why">100 donaning oʻsha foizlari</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>40 + 30 + 20 + 10 = 100 ✓ va foizlar 40 + 30 + 20 + 10 = 100% ✓
  <br>100 dona 50 kishiga soʻralganidan ikki barobar koʻp, va har bir
  son ham roppa-rosa ikki barobar (20 → 40, 15 → 30…) ✓
  <br><b>Javob:</b> 40 somsa, 30 patir, 20 pirog, 10 boshqasi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">«Maktabda sport yaxshimi?» — soʻrovnoma
  savoli</p>
  <p class="pe-fix__good">«Haftada necha marta sport bilan
  shugʻullanasiz?»</p>
  <p class="pe-fix__why">Birinchi savolga hamma «ha» deydi va hech
  qanday maʼlumot chiqmaydi. Savol <b>sanab boʻladigan</b> javob
  berishi kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Chastotalar: 8, 5, 4, 3 — jami 21</p>
  <p class="pe-fix__good">8 + 5 + 4 + 3 = 20</p>
  <p class="pe-fix__why">Yigʻindi soʻralganlar soniga teng chiqmasa,
  kimdir ikki marta sanalgan yoki bittasi tushib qolgan. Jadvalni
  tekshirmasdan xulosa chiqarmang.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Foizlar: 40 + 25 + 20 + 10 = 95%</p>
  <p class="pe-fix__good">40 + 25 + 20 + 15 = 100%</p>
  <p class="pe-fix__why">Foizlar yigʻindisi har doim 100 boʻlishi
  kerak. 95 chiqsa, bitta ulush notoʻgʻri hisoblangan.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">«Sinfimizda 8 kishi olmani yoqtiradi, demak
  maktabda ham 8 kishi»</p>
  <p class="pe-fix__good">«20 kishidan 8 tasi, yaʼni 40%»</p>
  <p class="pe-fix__why">Yalangʻoch son hech nima demaydi — u
  <b>nechtadan</b> ekanini bilish shart. Katta guruhga oʻtishda son emas,
  <b>foiz</b> koʻchiriladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Chiziqchalarda ikkita toʻliq guruh va yana
  toʻrtta chiziqcha bor. Bu nechta?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>14 ta.</b> 5 + 5 + 4 = 14.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 25 oʻquvchidan 10 tasi avtobusda keladi. Bu
  necha foiz?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>40%.</b> 10 ÷ 25 = 0,4, va 0,4 × 100 = 40%.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Jadvalda chastotalar 12, 9, 6 va 3. Jami
  nechta javob yigʻilgan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>30 ta.</b> 12 + 9 + 6 + 3 = 30.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Oʻsha jadvalda 12 chastota necha foiz
  boʻladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>40%.</b> 12 ÷ 30 = 0,4 → 40%.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Uchta ulushning foizi 45%, 30% va 15%.
  Toʻrtinchisi necha foiz?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>10%.</b> Foizlar 100 ni berishi kerak:
    100 − (45 + 30 + 15) = 100 − 90 = 10%.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Jasur 40 oʻquvchidan qaysi transportda
  kelishini soʻradi: piyoda 18, avtobus 14, velosiped 8. Piyoda
  keladiganlar necha foiz va ular avtobusdagilardan nechtaga koʻp?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>45%, va 4 taga koʻp.</b> Avval tekshiramiz:
    18 + 14 + 8 = 40 ✓ Foiz: 18 ÷ 40 = 0,45 → 45%. Farq:
    18 − 14 = 4 ta. Diqqat: «nechtaga koʻp» — ayirish, «necha marta
    koʻp» boʻlganda boʻlish boʻlardi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Maʼlumot</b><span>yigʻilgan faktlar va sonlar; ingl.
    data</span></li>
  <li><b>Soʻrovnoma</b><span>savol berib maʼlumot yigʻish; ingl.
    survey</span></li>
  <li><b>Kuzatish</b><span>sanab yoki qarab maʼlumot yigʻish; ingl.
    observation</span></li>
  <li><b>Chastota</b><span>bir javob necha marta uchragani; ingl.
    frequency</span></li>
  <li><b>Chastota jadvali</b><span>javob va uning soni yozilgan jadval;
    ingl. frequency table</span></li>
  <li><b>Chiziqcha bilan sanash</b><span>beshtadan guruhlab sanash
    usuli; ingl. tally</span></li>
  <li><b>Ulush</b><span>butunning bir qismi; ingl. share</span></li>
  <li><b>Foiz</b><span>yuzdan boʻlak, %; ingl. percentage</span></li>
  <li><b>Jami</b><span>hamma chastotalarning yigʻindisi; ingl.
    total</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Savol → yigʻish → jadval → xulosa. Savol aniq boʻlmasa,
      qolgani ham foydasiz.</li>
    <li>Kimdan soʻralgani javobning bir qismi — uni yozib qoʻying.</li>
    <li>Chiziqchani beshtadan guruhlang: shunda sanashda
      adashmaysiz.</li>
    <li>Chastota — bir javob necha marta uchragani.</li>
    <li>Foiz = ulush ÷ jami × 100.</li>
    <li>Ikkita tekshiruv: chastotalar jamiga teng, foizlar 100 ga
      teng.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-76 — diagramma turlari
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-76: Diagramma turlari: ustunli, chiziqli, doiraviy",
        "category": "math",
        "order": 76,
        "summary": (
            "Bitta jadvalni uch xil chizish mumkin, lekin har biri boshqa "
            "savolga javob beradi. Ustunli, chiziqli va doiraviy "
            "diagrammalarni qurish va toʻgʻrisini tanlashni oʻrganasiz."
        ),
        "stories": ["Qaysi diagramma toʻgʻri gapiradi"],
        "content": """
<h2>PM-76: Diagramma turlari: ustunli, chiziqli, doiraviy</h2>

<p>Oʻtgan darsda jadval tuzdik. Jadval aniq, lekin sekin: undagi eng
katta sonni topish uchun hamma qatorni oʻqib chiqish kerak.</p>

<p>Diagramma esa buni bir qarashda koʻrsatadi. Faqat bitta shart bor —
<b>toʻgʻri turini tanlash</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>ustunli diagramma qurasiz va oʻqiysiz;</li>
    <li>chiziqli diagramma bilan oʻzgarishni koʻrsatasiz;</li>
    <li>doiraviy diagramma uchun sektor burchagini hisoblaysiz;</li>
    <li>maʼlumotga qarab toʻgʻri turini tanlaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Sektor burchagi</span>
  <span class="pe-chip pe-chip--o">ulush</span>
  <span class="pe-op">÷</span>
  <span class="pe-chip pe-chip--o">jami</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--v">360°</span>
</div>

<h3>1. Ustunli diagramma — nimani nima bilan solishtirish</h3>

<p>Oʻtgan darsdagi meva jadvalini olamiz. Har bir mevaga bitta ustun,
ustunning <b>balandligi</b> — uning chastotasi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 195" role="img" aria-label="Sevimli meva — ustunli diagramma">
    <line class="pm-ch__ax" x1="46" y1="160" x2="302" y2="160"/>
    <text class="pm-ch__cap" x="40" y="164" text-anchor="end">0</text>
    <line class="pm-ch__grid" x1="46" y1="136" x2="302" y2="136"/>
    <text class="pm-ch__cap" x="40" y="140" text-anchor="end">2</text>
    <line class="pm-ch__grid" x1="46" y1="112" x2="302" y2="112"/>
    <text class="pm-ch__cap" x="40" y="116" text-anchor="end">4</text>
    <line class="pm-ch__grid" x1="46" y1="88" x2="302" y2="88"/>
    <text class="pm-ch__cap" x="40" y="92" text-anchor="end">6</text>
    <line class="pm-ch__grid" x1="46" y1="64" x2="302" y2="64"/>
    <text class="pm-ch__cap" x="40" y="68" text-anchor="end">8</text>
    <line class="pm-ch__grid" x1="46" y1="40" x2="302" y2="40"/>
    <text class="pm-ch__cap" x="40" y="44" text-anchor="end">10</text>
    <rect class="pm-ch__bar" x="82" y="64" width="38" height="96" rx="3"/>
    <text class="pm-ch__val" x="101" y="57" text-anchor="middle">8</text>
    <text class="pm-ch__lbl" x="101" y="178" text-anchor="middle">olma</text>
    <rect class="pm-ch__bar" x="132.7" y="100" width="38" height="60" rx="3"/>
    <text class="pm-ch__val" x="151.7" y="93" text-anchor="middle">5</text>
    <text class="pm-ch__lbl" x="151.7" y="178" text-anchor="middle">uzum</text>
    <rect class="pm-ch__bar" x="183.3" y="112" width="38" height="48" rx="3"/>
    <text class="pm-ch__val" x="202.3" y="105" text-anchor="middle">4</text>
    <text class="pm-ch__lbl" x="202.3" y="178" text-anchor="middle">shaftoli</text>
    <rect class="pm-ch__bar" x="234" y="124" width="38" height="36" rx="3"/>
    <text class="pm-ch__val" x="253" y="117" text-anchor="middle">3</text>
    <text class="pm-ch__lbl" x="253" y="178" text-anchor="middle">anor</text>
  </svg>
  <figcaption>Eng baland ustun darrov koʻrinadi. Jadvalda buni topish
  uchun toʻrtta sonni oʻqish kerak edi.</figcaption>
</figure>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Ustunli diagrammaning uchta qoidasi</p>
  <p>1. Hamma ustun <b>bir xil enda</b> va oralari teng.
  <br>2. Oʻq <b>noldan</b> boshlanadi — aks holda diagramma yolgʻon
  gapiradi.
  <br>3. Har bir ustun nomlanadi va soni yoziladi.</p>
</div>

<p>Diqqat qiling: hamma ustun <b>bitta rangda</b>. Ustunning balandligi
sonni allaqachon koʻrsatib turibdi — uni yana rang bilan takrorlash
ortiqcha. Rang faqat bitta ustunni ajratib koʻrsatish kerak boʻlganda
oʻzgaradi.</p>

<h3>2. Chiziqli diagramma — vaqt oʻtishi bilan nima oʻzgardi</h3>

<p>Agar maʼlumot <b>vaqt boʻyicha</b> yigʻilgan boʻlsa — har kuni, har
oy, har yili — nuqtalarni chiziq bilan tutashtiramiz.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 195" role="img" aria-label="Bir haftalik harorat — chiziqli diagramma">
    <line class="pm-ch__ax" x1="46" y1="160" x2="302" y2="160"/>
    <text class="pm-ch__cap" x="40" y="164" text-anchor="end">14</text>
    <line class="pm-ch__grid" x1="46" y1="130" x2="302" y2="130"/>
    <text class="pm-ch__cap" x="40" y="134" text-anchor="end">18</text>
    <line class="pm-ch__grid" x1="46" y1="100" x2="302" y2="100"/>
    <text class="pm-ch__cap" x="40" y="104" text-anchor="end">22</text>
    <line class="pm-ch__grid" x1="46" y1="70" x2="302" y2="70"/>
    <text class="pm-ch__cap" x="40" y="74" text-anchor="end">26</text>
    <line class="pm-ch__grid" x1="46" y1="40" x2="302" y2="40"/>
    <text class="pm-ch__cap" x="40" y="44" text-anchor="end">30</text>
    <polyline class="pm-ch__line" points="62,130 100.3,107.5 138.7,85 177,100 215.3,70 253.7,62.5 292,92.5"/>
    <circle class="pm-ch__dot" cx="62" cy="130" r="4"/>
    <text class="pm-ch__lbl" x="62" y="178" text-anchor="middle">Du</text>
    <circle class="pm-ch__dot" cx="100.3" cy="107.5" r="4"/>
    <text class="pm-ch__lbl" x="100.3" y="178" text-anchor="middle">Se</text>
    <circle class="pm-ch__dot" cx="138.7" cy="85" r="4"/>
    <text class="pm-ch__lbl" x="138.7" y="178" text-anchor="middle">Ch</text>
    <circle class="pm-ch__dot" cx="177" cy="100" r="4"/>
    <text class="pm-ch__lbl" x="177" y="178" text-anchor="middle">Pa</text>
    <circle class="pm-ch__dot" cx="215.3" cy="70" r="4"/>
    <text class="pm-ch__lbl" x="215.3" y="178" text-anchor="middle">Ju</text>
    <circle class="pm-ch__dot" cx="253.7" cy="62.5" r="4"/>
    <text class="pm-ch__lbl" x="253.7" y="178" text-anchor="middle">Sh</text>
    <circle class="pm-ch__dot" cx="292" cy="92.5" r="4"/>
    <text class="pm-ch__lbl" x="292" y="178" text-anchor="middle">Ya</text>
    <text class="pm-ch__val" x="62" y="120" text-anchor="middle">18°</text>
    <text class="pm-ch__val" x="253.7" y="52.5" text-anchor="middle">27°</text>
  </svg>
  <figcaption>Bir haftalik harorat. Chiziqning koʻtarilishi va tushishi
  — bu haftaning hikoyasi.</figcaption>
</figure>

<p>Bu yerda chiziq maʼnoga ega: u kunlar <b>ketma-ket</b> kelishini
koʻrsatadi. Shuning uchun mevalarni chiziq bilan tutashtirib boʻlmaydi —
olma bilan uzum orasida «oraliq» yoʻq.</p>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Har nuqtaga son yozilmaydi</p>
  <p>Chiziqli diagrammada odatda faqat <b>eng baland va eng past</b>
  nuqta belgilanadi. Qolganini oʻq boʻyicha oʻqish mumkin, hammasini
  yozib chiqsangiz esa diagramma sonlar toʻdasiga aylanadi va chiziq
  koʻrinmay qoladi.</p>
</div>

<h3>3. Doiraviy diagramma — butunning boʻlaklari</h3>

<p>Agar savol «kim koʻp?» emas, <b>«butundan qanchasi?»</b> boʻlsa,
doiraviy diagramma ishlatiladi. Butun doira — 100%, yaʼni 360°.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 200" role="img" aria-label="Sevimli meva — doiraviy diagramma">
    <path class="pm-ch__s1" d="M 160 100 L 160 38 A 62 62 0 0 1 196.4 150.2 Z"/>
    <text class="pm-ch__lbl" x="238" y="74.7" text-anchor="start">olma 40%</text>
    <path class="pm-ch__s2" d="M 160 100 L 196.4 150.2 A 62 62 0 0 1 109.8 136.4 Z"/>
    <text class="pm-ch__lbl" x="147.2" y="181" text-anchor="end">uzum 25%</text>
    <path class="pm-ch__s3" d="M 160 100 L 109.8 136.4 A 62 62 0 0 1 109.8 63.6 Z"/>
    <text class="pm-ch__lbl" x="78" y="100" text-anchor="end">shaftoli 20%</text>
    <path class="pm-ch__s4" d="M 160 100 L 109.8 63.6 A 62 62 0 0 1 160 38 Z"/>
    <text class="pm-ch__lbl" x="122.8" y="26.9" text-anchor="end">anor 15%</text>
  </svg>
  <figcaption>Xuddi oʻsha yigirmata javob. Endi savol boshqa: har bir
  meva butun sinfning qanchasini egallaydi.</figcaption>
</figure>

<p>Har bir boʻlakning burchagini hisoblaymiz. Doira 360° (PM-58), demak
har bir ulushga oʻz ulushicha burchak tegadi:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">8 ÷ 20 × 360 = 144°</span>
    <span class="pm-solve__why">Olma</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5 ÷ 20 × 360 = 90°</span>
    <span class="pm-solve__why">Uzum — roppa-rosa chorak doira</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4 ÷ 20 × 360 = 72°</span>
    <span class="pm-solve__why">Shaftoli</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3 ÷ 20 × 360 = 54°</span>
    <span class="pm-solve__why">Anor</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>144 + 90 + 72 + 54 = 360° ✓ — doira toʻliq yopildi.
  <br>Bu tekshiruv majburiy: yigʻindi 360 chiqmasa, diagramma
  notoʻgʻri.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Doiraviy diagramma vaqt uchun ishlamaydi</p>
  <p>«Bir haftalik harorat»ni doiraviy diagrammada koʻrsatib boʻlmaydi:
  harorat butunning boʻlagi emas, va 18 + 21 + 24 + … ning hech qanday
  maʼnosi yoʻq. Doiraviy diagramma faqat <b>bir butun boʻlinadigan</b>
  narsalar uchun: pul, vaqt, odamlar soni.</p>
</div>

<h3>4. Qaysi birini tanlash</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Savol qanday</th><th>Diagramma</th><th>Misol</th></tr>
  <tr><td>Kim koʻp, kim kam?</td>
    <td class="pm-word__sym">ustunli</td>
    <td>sinfdagi sevimli meva</td></tr>
  <tr><td>Vaqt oʻtishi bilan qanday oʻzgardi?</td>
    <td class="pm-word__sym">chiziqli</td>
    <td>haftalik harorat, oylik savdo</td></tr>
  <tr><td>Butundan qanchasi?</td>
    <td class="pm-word__sym">doiraviy</td>
    <td>oylik nimaga sarflandi</td></tr>
</table></div>

<h3>Matnli masala</h3>

<p>Bekzod bir oyda 600 000 soʻm sarfladi: kitobga 150 000, transportga
180 000, ovqatga 210 000, jamgʻarmaga 60 000 soʻm.</p>

<p><b>Qaysi diagramma toʻgʻri keladi va boʻlaklarning burchaklari
qancha?</b></p>

<p><b>Reja:</b> savolning turini aniqlaymiz, keyin har bir ulushning
burchagini hisoblab, yigʻindisini tekshiramiz.</p>

<p>Savol — «pulning qanchasi qayerga ketdi», yaʼni <b>butunning
boʻlaklari</b>. Demak <b>doiraviy</b> diagramma.</p>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Ovqat 210 000 — bu 600 000 ning uchdan biridan sal koʻproq,
  demak uning burchagi 120° dan sal katta chiqishi kerak.</span>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">150 000 ÷ 600 000 × 360 = 90°</span>
    <span class="pm-solve__why">Kitob — 25%</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">180 000 ÷ 600 000 × 360 = 108°</span>
    <span class="pm-solve__why">Transport — 30%</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">210 000 ÷ 600 000 × 360 = 126°</span>
    <span class="pm-solve__why">Ovqat — 35%</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">60 000 ÷ 600 000 × 360 = 36°</span>
    <span class="pm-solve__why">Jamgʻarma — 10%</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Burchaklar: 90 + 108 + 126 + 36 = 360° ✓
  <br>Foizlar: 25 + 30 + 35 + 10 = 100% ✓
  <br>Ovqatning 126° — taxminimizdagi «120 dan sal katta» ✓
  <br><b>Javob:</b> doiraviy diagramma; 90°, 108°, 126° va 36°.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Haftalik harorat — doiraviy diagrammada</p>
  <p class="pe-fix__good">Chiziqli diagrammada</p>
  <p class="pe-fix__why">Harorat butunning boʻlagi emas. Doiraviy
  diagramma faqat boʻlinadigan bir butun uchun ishlaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Sektor burchagi: 8 ÷ 20 × 100 = 40°</p>
  <p class="pe-fix__good">8 ÷ 20 × 360 = 144°</p>
  <p class="pe-fix__why">40 — bu foiz, burchak emas. Butun doira 100 emas,
  <b>360°</b>. Foizni burchakka aylantirish uchun 3,6 ga koʻpaytiring:
  40 × 3,6 = 144 ✓</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Ustunli diagrammaning oʻqi 3 dan boshlanadi</p>
  <p class="pe-fix__good">Oʻq noldan boshlanadi</p>
  <p class="pe-fix__why">Noldan boshlanmagan oʻq kichik farqni katta
  koʻrsatadi — ustunlarning balandligi endi sonlarga mos kelmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Sektorlar yigʻindisi 350° chiqdi — mayli</p>
  <p class="pe-fix__good">Har doim roppa-rosa 360°</p>
  <p class="pe-fix__why">Doira boʻsh joy qoldirmaydi. 350 chiqdi
  degani — bitta ulush notoʻgʻri hisoblangan yoki bittasi tushib
  qolgan.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 40 kishidan 10 tasi sport toʻgaragiga
  boradi. Doiraviy diagrammada bu sektorning burchagi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>90°.</b> 10 ÷ 40 × 360 = 0,25 × 360 = 90° — chorak
    doira.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Bir ulush butunning yarmi. Uning burchagi
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>180°.</b> Yarim doira: 360 ÷ 2 = 180°.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Uch yil davomida maktabdagi oʻquvchilar soni
  qanday oʻzgarganini koʻrsatmoqchimiz. Qaysi diagramma?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Chiziqli.</b> Maʼlumot vaqt boʻyicha yigʻilgan, savol esa
    «qanday oʻzgardi» — bu chiziqli diagrammaning ishi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Sektorning burchagi 72°. Bu butunning necha
  foizi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>20%.</b> 72 ÷ 360 = 0,2 → 20%. Tez yoʻl: burchakni 3,6 ga
    boʻling.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Doiraviy diagrammada uchta sektor 120°, 150°
  va 45°. Toʻrtinchisi necha gradus?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>45°.</b> 360 − (120 + 150 + 45) = 360 − 315 = 45°.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Dilnoza 30 kunlik kundaligida qancha vaqt
  nimaga ketganini koʻrsatmoqchi: uyqu 9 soat, maktab 6 soat, dars
  tayyorlash 3 soat, boshqasi 6 soat (bir kunda). Qaysi diagramma va
  uyquning burchagi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Doiraviy; 135°.</b> Bir kun — 24 soat, va
    9 + 6 + 3 + 6 = 24 ✓ — bu butunning boʻlaklari, demak doiraviy.
    Uyqu: 9 ÷ 24 × 360 = 0,375 × 360 = 135°.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Diagramma</b><span>maʼlumotning chizmadagi koʻrinishi; ingl.
    chart</span></li>
  <li><b>Ustunli diagramma</b><span>toifalarni solishtiruvchi
    diagramma; ingl. bar chart</span></li>
  <li><b>Chiziqli diagramma</b><span>vaqt boʻyicha oʻzgarishni
    koʻrsatadi; ingl. line graph</span></li>
  <li><b>Doiraviy diagramma</b><span>butunning boʻlaklarini koʻrsatadi;
    ingl. pie chart</span></li>
  <li><b>Sektor</b><span>doiraviy diagrammaning bir boʻlagi; ingl.
    sector</span></li>
  <li><b>Oʻq</b><span>diagrammaning sonlar yozilgan chizigʻi; ingl.
    axis</span></li>
  <li><b>Shkala</b><span>oʻqdagi boʻlinishlar tartibi; ingl.
    scale</span></li>
  <li><b>Sarlavha</b><span>diagramma nima haqidaligi; ingl.
    title</span></li>
  <li><b>Ulush</b><span>butundan tegishli qism; ingl. share</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Ustunli — solishtirish uchun; oʻq noldan boshlanadi.</li>
    <li>Chiziqli — vaqt boʻyicha oʻzgarish uchun.</li>
    <li>Doiraviy — butunning boʻlaklari uchun.</li>
    <li>Sektor burchagi = ulush ÷ jami × 360°.</li>
    <li>Burchaklar yigʻindisi har doim roppa-rosa 360°.</li>
    <li>Foizdan burchakka: × 3,6. Burchakdan foizga: ÷ 3,6.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-77 — diagrammani oʻqish
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-77: Diagrammani oʻqish — raqamlar ichidagi hikoya",
        "category": "math",
        "order": 77,
        "summary": (
            "Diagramma qurishdan koʻra uni oʻqish koʻproq kerak boʻladi. "
            "Sarlavha, oʻq va birlikdan boshlab, farq, jami va eng katta "
            "sakrashni topishgacha — toʻrt qadamlik odat."
        ),
        "stories": ["Bir yillik yomgʻir"],
        "content": """
<h2>PM-77: Diagrammani oʻqish — raqamlar ichidagi hikoya</h2>

<p>Umringizda diagramma qurishingizga bir necha marta toʻgʻri keladi.
Lekin <b>oʻqishingizga</b> — har kuni: yangiliklar, telefon tarifi,
imtihon natijalari, oʻquv jadvali.</p>

<p>Diagramma raqamlarni koʻrsatadi. Ularning ichidagi hikoyani esa
oʻqiydigan odam topadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>diagrammani toʻrt qadamda oʻqiysiz;</li>
    <li>eng katta, eng kichik va farqni topasiz;</li>
    <li>chiziqli diagrammada eng katta sakrashni aniqlaysiz;</li>
    <li>diagramma nima demasligini ham bilib olasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Oʻqish tartibi</span>
  <span class="pe-chip pe-chip--s">sarlavha</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">oʻq va birlik</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">qiymatlar</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">xulosa</span>
</div>

<h3>1. Toʻrt qadam</h3>

<div class="pe-steps">
  <ol>
    <li><b>Sarlavhani oʻqing.</b> Diagramma nima haqida va kim
      haqida?</li>
    <li><b>Oʻqlarga qarang.</b> Pastda nima turibdi, chapda nima?
      Birligi nima — dona, metr, soʻm, gradus?</li>
    <li><b>Qiymatlarni oʻqing.</b> Eng katta, eng kichik, kerakli
      qiymat.</li>
    <li><b>Xulosa chiqaring.</b> Bu maʼlumot nima deyapti?</li>
  </ol>
</div>

<p>Uchinchi qadamgacha yetmasdan xulosa chiqarish — eng koʻp
uchraydigan xato. Avval oʻqing, keyin gapiring.</p>

<h3>2. Ustunli diagrammani oʻqish</h3>

<figure class="pm-fig">
  <svg viewBox="0 0 320 195" role="img" aria-label="Kutubxonadan olingan kitoblar — ustunli diagramma">
    <line class="pm-ch__ax" x1="46" y1="160" x2="302" y2="160"/>
    <text class="pm-ch__cap" x="40" y="164" text-anchor="end">0</text>
    <line class="pm-ch__grid" x1="46" y1="120" x2="302" y2="120"/>
    <text class="pm-ch__cap" x="40" y="124" text-anchor="end">20</text>
    <line class="pm-ch__grid" x1="46" y1="80" x2="302" y2="80"/>
    <text class="pm-ch__cap" x="40" y="84" text-anchor="end">40</text>
    <line class="pm-ch__grid" x1="46" y1="40" x2="302" y2="40"/>
    <text class="pm-ch__cap" x="40" y="44" text-anchor="end">60</text>
    <rect class="pm-ch__bar" x="69.3" y="80" width="34" height="80" rx="3"/>
    <text class="pm-ch__val" x="86.3" y="73" text-anchor="middle">40</text>
    <text class="pm-ch__lbl" x="86.3" y="178" text-anchor="middle">Sen</text>
    <rect class="pm-ch__bar" x="114.7" y="50" width="34" height="110" rx="3"/>
    <text class="pm-ch__val" x="131.7" y="43" text-anchor="middle">55</text>
    <text class="pm-ch__lbl" x="131.7" y="178" text-anchor="middle">Okt</text>
    <rect class="pm-ch__bar" x="160" y="90" width="34" height="70" rx="3"/>
    <text class="pm-ch__val" x="177" y="83" text-anchor="middle">35</text>
    <text class="pm-ch__lbl" x="177" y="178" text-anchor="middle">Noy</text>
    <rect class="pm-ch__bar--hl" x="205.3" y="40" width="34" height="120" rx="3"/>
    <text class="pm-ch__val" x="222.3" y="33" text-anchor="middle">60</text>
    <text class="pm-ch__lbl" x="222.3" y="178" text-anchor="middle">Dek</text>
    <rect class="pm-ch__bar" x="250.7" y="70" width="34" height="90" rx="3"/>
    <text class="pm-ch__val" x="267.7" y="63" text-anchor="middle">45</text>
    <text class="pm-ch__lbl" x="267.7" y="178" text-anchor="middle">Yan</text>
  </svg>
  <figcaption>Maktab kutubxonasidan olingan kitoblar. Dekabr ustuni
  ajratib koʻrsatilgan — u eng balandi.</figcaption>
</figure>

<p>Toʻrt qadamni bajaramiz. <b>Sarlavha:</b> kutubxonadan olingan
kitoblar. <b>Oʻqlar:</b> pastda oylar, chapda kitoblar soni (dona).
<b>Qiymatlar:</b> 40, 55, 35, 60, 45. Endi savollarga javob beramiz:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Eng koʻp: 60 (Dekabr)</span>
    <span class="pm-solve__why">Eng baland ustun</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Eng kam: 35 (Noyabr)</span>
    <span class="pm-solve__why">Eng past ustun</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Farqi: 60 − 35 = 25 ta</span>
    <span class="pm-solve__why">Ayirish — «nechtaga koʻp»</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Jami: 40 + 55 + 35 + 60 + 45 = 235 ta</span>
    <span class="pm-solve__why">Besh oyda</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">«Nechtaga koʻp» va «necha marta koʻp»</p>
  <p>Dekabrda Noyabrga nisbatan <b>25 taga</b> koʻp (60 − 35 = 25).
  Lekin <b>necha marta</b> koʻp deyilsa, boʻlish kerak boʻlardi:
  60 ÷ 35 ≈ 1,7 marta. Bu ikki savol har xil amal talab qiladi va
  ularni chalkashtirish — imtihondagi klassik xato.</p>
</div>

<h3>3. Chiziqli diagrammani oʻqish: sakrashni topish</h3>

<figure class="pm-fig">
  <svg viewBox="0 0 320 195" role="img" aria-label="Niholning boʻyi — chiziqli diagramma">
    <line class="pm-ch__ax" x1="46" y1="160" x2="302" y2="160"/>
    <text class="pm-ch__cap" x="40" y="164" text-anchor="end">0</text>
    <line class="pm-ch__grid" x1="46" y1="120" x2="302" y2="120"/>
    <text class="pm-ch__cap" x="40" y="124" text-anchor="end">6</text>
    <line class="pm-ch__grid" x1="46" y1="80" x2="302" y2="80"/>
    <text class="pm-ch__cap" x="40" y="84" text-anchor="end">12</text>
    <line class="pm-ch__grid" x1="46" y1="40" x2="302" y2="40"/>
    <text class="pm-ch__cap" x="40" y="44" text-anchor="end">18</text>
    <polyline class="pm-ch__line" points="62,146.7 108,126.7 154,100 200,66.7 246,53.3 292,46.7"/>
    <circle class="pm-ch__dot" cx="62" cy="146.7" r="4"/>
    <text class="pm-ch__lbl" x="62" y="178" text-anchor="middle">1</text>
    <circle class="pm-ch__dot" cx="108" cy="126.7" r="4"/>
    <text class="pm-ch__lbl" x="108" y="178" text-anchor="middle">2</text>
    <circle class="pm-ch__dot" cx="154" cy="100" r="4"/>
    <text class="pm-ch__lbl" x="154" y="178" text-anchor="middle">3</text>
    <circle class="pm-ch__dot" cx="200" cy="66.7" r="4"/>
    <text class="pm-ch__lbl" x="200" y="178" text-anchor="middle">4</text>
    <circle class="pm-ch__dot" cx="246" cy="53.3" r="4"/>
    <text class="pm-ch__lbl" x="246" y="178" text-anchor="middle">5</text>
    <circle class="pm-ch__dot" cx="292" cy="46.7" r="4"/>
    <text class="pm-ch__lbl" x="292" y="178" text-anchor="middle">6</text>
    <text class="pm-ch__val" x="62" y="136.7" text-anchor="middle">2 sm</text>
    <text class="pm-ch__val" x="292" y="36.7" text-anchor="middle">17 sm</text>
  </svg>
  <figcaption>Niholning boʻyi, hafta boʻyicha: 2, 5, 9, 14, 16, 17 sm.
  Pastdagi oʻq — hafta raqami.</figcaption>
</figure>

<p>Chiziqli diagrammada eng qiziq savol — <b>qachon eng tez
oʻsgan?</b> Buning uchun qoʻshni haftalarning farqiga qaraymiz.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Hafta</th><th>Oʻsish</th><th>Hisob</th></tr>
  <tr><td>1 → 2</td><td class="pm-word__sym">3 sm</td><td>5 − 2</td></tr>
  <tr><td>2 → 3</td><td class="pm-word__sym">4 sm</td><td>9 − 5</td></tr>
  <tr><td>3 → 4</td><td class="pm-word__sym">5 sm</td><td>14 − 9</td></tr>
  <tr><td>4 → 5</td><td class="pm-word__sym">2 sm</td><td>16 − 14</td></tr>
  <tr><td>5 → 6</td><td class="pm-word__sym">1 sm</td><td>17 − 16</td></tr>
</table></div>

<p>Eng katta sakrash — <b>3-haftadan 4-haftaga</b>, 5 santimetr. Buni
diagrammadan hisoblamasdan ham koʻrish mumkin: oʻsha yerda chiziq eng
tik koʻtarilgan.</p>

<div class="pm-solve">
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">17 − 2 = 15 sm</span>
    <span class="pm-solve__why">Olti haftadagi umumiy oʻsish</span>
  </div>
</div>

<p>Yana bir xulosa: oxirgi haftalarda chiziq deyarli tekislandi. Nihol
oʻsishdan toʻxtayapti — buni sonlar emas, <b>chiziqning shakli</b>
aytib turibdi.</p>

<h3>4. Diagramma nima demaydi</h3>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Diagramma sababni aytmaydi</p>
  <p>Dekabrda kitob koʻp olingani koʻrinib turibdi. <b>Nega</b> koʻp
  olingani esa koʻrinmaydi — qish taʼtilimi, yangi kitoblar keldimi,
  yoki oʻqituvchi topshiriq berdimi? Diagramma <em>nima</em> boʻlganini
  koʻrsatadi, <em>nega</em> boʻlganini emas. Sababni aytmoqchi
  boʻlsangiz, qoʻshimcha maʼlumot kerak.</p>
</div>

<h3>Matnli masala</h3>

<p>Kutubxonachi hisobot yozmoqchi. Yuqoridagi diagrammaga qarang:
Sentabr 40, Oktabr 55, Noyabr 35, Dekabr 60, Yanvar 45 ta kitob.</p>

<p><b>Besh oyda jami nechta kitob olingan va Yanvarda Dekabrga
nisbatan necha foizga kam olingan?</b></p>

<p><b>Reja:</b> jamini qoʻshamiz; keyin kamayishni topib, uni
<b>Dekabr</b> soniga nisbatan foizga oʻgiramiz (PM-25).</p>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Har oyda taxminan 45–50 tadan, besh oyda 250 ga yaqin
  boʻlishi kerak.</span>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">40 + 55 = 95</span>
    <span class="pm-solve__why">Sentabr va Oktabr</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">95 + 35 + 60 + 45 = 235 ta</span>
    <span class="pm-solve__why">Besh oyda jami</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">60 − 45 = 15 ta</span>
    <span class="pm-solve__why">Yanvarda shuncha kam</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">15 ÷ 60 × 100 = 25%</span>
    <span class="pm-solve__why">Asos — Dekabrning soni, chunki
    undan kamaydi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>235 — taxminimizdagi 250 ga yaqin ✓
  <br>60 ning 25 foizi: 60 ÷ 100 × 25 = 15 ✓ va 60 − 15 = 45 ✓
  <br><b>Javob:</b> 235 ta kitob; 25 foizga kam.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Kamayish foizi: 15 ÷ 45 × 100 ≈ 33%</p>
  <p class="pe-fix__good">15 ÷ 60 × 100 = 25%</p>
  <p class="pe-fix__why">Foiz <b>nimadan</b> kamayganiga nisbatan
  olinadi — bu yerda Dekabrning 60 tasidan (PM-25). Yangi songa
  boʻlish — foizdagi eng qimmat xato.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">«Ustun ikki barobar baland, demak soni ikki
  barobar»</p>
  <p class="pe-fix__good">Avval oʻqdagi sonlarni oʻqing</p>
  <p class="pe-fix__why">Bu faqat oʻq noldan boshlansa toʻgʻri. Oʻqni
  oʻqimasdan balandlikka qarab xulosa chiqarish — diagramma bilan
  aldashning eng oson yoʻli.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Nihol 3-haftada eng baland edi</p>
  <p class="pe-fix__good">3-haftadan 4-haftaga eng tez oʻsdi</p>
  <p class="pe-fix__why">«Eng baland» va «eng tez oʻsgan» — ikki xil
  savol. Birinchisi nuqtaning oʻzi, ikkinchisi qoʻshni ikki nuqtaning
  farqi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">«Dekabrda kitob koʻp olingan, chunki bolalar
  koʻproq oʻqishni yoqtirib qolgan»</p>
  <p class="pe-fix__good">«Dekabrda eng koʻp — 60 ta kitob olingan»</p>
  <p class="pe-fix__why">Diagramma sonni koʻrsatadi, sababni emas.
  Sababni aytish uchun boshqa maʼlumot kerak.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Kitoblar diagrammasida Oktabr va Noyabrning
  farqi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>20 ta.</b> 55 − 35 = 20.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Sentabr, Oktabr va Noyabrda jami nechta
  kitob olingan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>130 ta.</b> 40 + 55 + 35 = 130.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Nihol 2-haftadan 3-haftaga necha santimetr
  oʻsdi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>4 sm.</b> 9 − 5 = 4.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Nihol qaysi haftada eng sekin oʻsgan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5-haftadan 6-haftaga.</b> Oʻsish atigi 17 − 16 = 1 sm —
    diagrammada chiziq oʻsha yerda deyarli tekis.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Sentabrda 40 ta, Oktabrda 55 ta kitob
  olingan. Oktabrda necha foizga koʻp olingan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>37,5%.</b> Farq: 55 − 40 = 15. Asos — Sentabrning 40 tasi:
    15 ÷ 40 × 100 = 37,5%.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Sherbek diagrammaga qarab «Noyabrda hech kim
  kitob oʻqimagan» dedi. U haqmi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Yoʻq.</b> Noyabrda ham 35 ta kitob olingan — bu eng kam, lekin
    nol emas. «Eng kam» bilan «yoʻq» ni chalkashtirmang: ustun past
    boʻlishi hali boʻsh degani emas.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">7. Kutubxonaga Fevralda 45 ta kitob olingan
  boʻlsa, olti oydagi jami nechta boʻladi va Fevral Dekabrdan necha
  foizga kam?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>280 ta va 25% kam.</b> Jami: 235 + 45 = 280 ta. Kamayish:
    60 − 45 = 15, va 15 ÷ 60 × 100 = 25%. Fevral ham Yanvar bilan bir
    xil ekan.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Sarlavha</b><span>diagramma nima haqidaligi; ingl.
    title</span></li>
  <li><b>Oʻq</b><span>sonlar va nomlar yozilgan chiziq; ingl.
    axis</span></li>
  <li><b>Birlik</b><span>nima bilan oʻlchangani — dona, sm, soʻm;
    ingl. unit</span></li>
  <li><b>Shkala</b><span>oʻqdagi boʻlinishlar qadami; ingl.
    scale</span></li>
  <li><b>Farq</b><span>ikki qiymatning ayirmasi; ingl.
    difference</span></li>
  <li><b>Sakrash</b><span>qoʻshni ikki qiymat orasidagi keskin oʻzgarish;
    ingl. jump</span></li>
  <li><b>Oʻsish</b><span>qiymatning ortishi; ingl. increase</span></li>
  <li><b>Kamayish</b><span>qiymatning tushishi; ingl.
    decrease</span></li>
  <li><b>Xulosa</b><span>maʼlumotdan chiqarilgan fikr; ingl.
    conclusion</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Sarlavha → oʻq va birlik → qiymatlar → xulosa. Tartibni
      buzmang.</li>
    <li>Eng katta va eng kichikni topib, farqini ayiring.</li>
    <li>Chiziqli diagrammada sakrash — qoʻshni ikki qiymatning
      farqi; eng tik joy eng katta sakrash.</li>
    <li>«Nechtaga koʻp» — ayirish, «necha marta koʻp» — boʻlish.</li>
    <li>Foizga oʻgirganda asos <b>eski</b> son boʻladi.</li>
    <li>Diagramma nima boʻlganini aytadi, nega boʻlganini emas.</li>
  </ul>
</div>
""",
    },
]
