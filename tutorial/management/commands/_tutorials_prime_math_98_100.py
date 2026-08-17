# -*- coding: utf-8 -*-
"""Prime Math — darslar 98–100. **KURSNING YAKUNI.**

**Blok H ni va butun 100 darslik kursni YOPADI.**
Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md

  mashqlar — practice/management/commands/_practice_pm_98_100.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_98_100.py

⚠️ PM-98 va PM-99 — Blok H ning oxirgi ikki usuli:
     PM-98  javob maʼlum, boshlanish nomaʼlum → amallarni TESKARI
            tartibda va TESKARI maʼnoda bajarish. Bu PM-87 dagi oʻq
            sxemasining davomi: oʻsha yerda sxema chapdan oʻngga
            yechilgan edi, bu yerda oʻngdan chapga;
     PM-99  kichik hollarni hisoblab, NAMUNA topish va uni n orqali
            yozish. Kursda birinchi marta pupil oʻzi formula chiqaradi
            — shuning uchun darsda «namuna isbot emas» ogohlantirishi
            majburiy (1, 2, 4, 8, 16, 31 misoli).

⚠️ PM-100 — YAKUNIY DARS. Unda birorta ham yangi matematika YOʻQ va
   boʻlmasligi ham kerak. Uning vazifasi boshqa: 100 darsni bitta
   xaritaga yigʻish, kursning oʻzagidagi bir necha gʻoyani ochiq
   aytish (bir xil uchlik uch marta; toʻrt qadam; «javob mantiqiymi?»;
   ikki marta hisoblash), oʻquvchiga u endi nimalarni qila olishini
   koʻrsatish va keyingi yoʻlni — SAT Math, Corner javonlari,
   Matematika chempionati — koʻrsatish. Ohangi: iliq, shaxsiy, xat
   kabi. Bu oʻquvchi kursda oʻqiydigan oxirgi sahifa.

⚠️ Kumulyativ: PM-100 butun kursga tayanadi va shuning uchun undagi
   har bir havola tekshirilgan — quyidagi xarita jadvalidagi barcha
   dars raqamlari toc_prime_math.txt bilan solishtirilgan.

⚠️ Arifmetika darvozasi: scratchpad/verify_pm_98_100.py
   • PM-98 — har bir teskari yechim OLDINGA yurib tasdiqlanadi
     (boshlangʻich songa amallar ketma-ket qoʻllanadi va oxirida
     masaladagi son chiqishi talab qilinadi);
   • PM-99 — har bir namuna formulasi kichik n larda BEVOSITA sanab
     tekshiriladi (formula emas, taʼrif boʻyicha);
   • PM-100 — takroriy testdagi har bir javob oʻz darsining usuli
     bilan qayta hisoblanadi.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_98_100.py --author=prime
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
    # PM-98 — teskaridan yurish
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-98: Teskaridan yurish",
        "category": "math",
        "order": 98,
        "summary": (
            "Baʼzi masalalarda oxiri maʼlum, boshi nomaʼlum. Unda "
            "oxiridan boshlab, har bir amalni teskarisiga almashtirib "
            "orqaga yuriladi — va boshlanish oʻzi chiqadi."
        ),
        "stories": ["Qopdagi yongʻoq"],
        "content": """
<h2>PM-98: Teskaridan yurish</h2>

<p>«Bir son oʻyladim. Uni 3 ga koʻpaytirdim, keyin 8 qoʻshdim va 35
chiqdi. Qanday son oʻylagandim?»</p>

<p>Oldinga yurish qiyin: qaysi sondan boshlashni bilmaymiz. Lekin
oxiri maʼlum — <b>35</b>. Va agar biz 8 <i>qoʻshgan</i> boʻlsak,
orqaga qaytishda 8 ni <b>ayirish</b> kerak. Agar 3 ga
<i>koʻpaytirgan</i> boʻlsak, orqaga qaytishda 3 ga <b>boʻlish</b>
kerak.</p>

<p>35 − 8 = 27, keyin 27 ÷ 3 = <b>9</b>. Tamom.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>qachon teskaridan yurish kerakligini bilib olasiz;</li>
    <li>har bir amalning teskarisini topasiz;</li>
    <li>amallarni teskari tartibda bajarasiz;</li>
    <li>javobni oldinga yurib tekshirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Teskaridan yurish</span>
  <span class="pe-chip pe-chip--v">oxirgi son</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">teskari amallar</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">boshlangʻich son</span>
</div>

<h3>1. Qachon bu usul kerak</h3>

<p>PM-87 da oʻq sxemasini oʻrgangan edik. Oʻshanda biz sxemani chapdan
oʻngga oʻqib, tenglama tuzgandik. Endi <b>teskari tomonga</b> yuramiz —
va koʻpincha tenglamaning ham hojati qolmaydi.</p>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Belgi</p>
  <p>Masalada <b>oxirgi natija berilgan</b>, boshlangʻich miqdor esa
  soʻralgan boʻlsa — teskaridan yurish deyarli har doim eng qisqa
  yoʻl. «…va oxirida 5 ta qoldi», «…natijada 35 chiqdi», «…qopda
  12 tasi qoldi» degan gaplar shu usulni chaqiradi.</p>
</div>

<h3>2. Teskari amallar jadvali</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Oldinga yurganda</th><th>Orqaga qaytganda</th><th>Misol</th></tr>
  <tr><td>+ 8 qoʻshildi</td><td class="pm-word__sym">− 8</td><td>35 → 27</td></tr>
  <tr><td>− 6 ayirildi</td><td class="pm-word__sym">+ 6</td><td>14 → 20</td></tr>
  <tr><td>× 3 koʻpaytirildi</td><td class="pm-word__sym">÷ 3</td><td>27 → 9</td></tr>
  <tr><td>÷ 5 boʻlindi</td><td class="pm-word__sym">× 5</td><td>9 → 45</td></tr>
  <tr><td>yarmi olindi</td><td class="pm-word__sym">× 2</td><td>10 → 20</td></tr>
  <tr><td>uchdan biri olindi</td><td class="pm-word__sym">× <sup>3</sup>/<sub>2</sub></td><td>20 → 30</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">«Yarmi olindi» ning teskarisi ÷ 2 EMAS</p>
  <p>Yarmi olinsa, <b>qolgani</b> ham yarmi. Demak orqaga qaytishda
  qolganini <b>ikkiga koʻpaytiramiz</b>. Bu eng koʻp uchraydigan
  xato: «olindi» degan soʻzni koʻrib, orqaga qaytishda ham kamaytirib
  yuborish.</p>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Tartib ham teskari boʻladi</p>
  <p>Amallarni teskarisiga almashtirish yarim ish. Ularni
  <b>oxirgisidan boshlab</b> bajarish kerak. Oldinga «×3, keyin +8»
  boʻlsa, orqaga «−8, keyin ÷3» boʻladi — koʻpaytirish emas, qoʻshish
  birinchi qaytariladi.</p>
</div>

<h3>3. Birinchi misollar</h3>

<div class="pe-formula">
  <span class="pe-chip pe-chip--s">x</span>
  <span class="pe-op">→ ×3 →</span>
  <span class="pe-chip pe-chip--o">3x</span>
  <span class="pe-op">→ +8 →</span>
  <span class="pe-chip pe-chip--v">35</span>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">35 − 8 = 27</span>
    <span class="pm-solve__why">Oxirgi amal «+8» edi — uni qaytardik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">27 ÷ 3 = 9</span>
    <span class="pm-solve__why">Undan oldingisi «×3» edi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Oldinga yurib tekshiramiz</p>
  <p>9 → ×3 → 27 → +8 → 35 ✓ — masaladagi son roppa-rosa chiqdi.</p>
</div>

<p><b>Ikkinchi misol.</b> Bir songa 12 qoʻshildi, keyin natija 4 ga
boʻlindi va 9 chiqdi. Bu son qanday?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">9 × 4 = 36</span>
    <span class="pm-solve__why">Oxirgi amal «÷4» edi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">36 − 12 = 24</span>
    <span class="pm-solve__why">Undan oldingisi «+12»</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>24 + 12 = 36, keyin 36 ÷ 4 = 9 ✓</p>
</div>

<h3>4. Ulushlar bilan orqaga yurish</h3>

<p><b>Masala.</b> Savatda olmalar bor edi. Birinchi bolaga yarmini
berdi. Keyin ikkinchi bolaga <b>qolganning</b> yarmini berdi. Savatda
5 ta olma qoldi. Boshida nechta edi?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">5 × 2 = 10</span>
    <span class="pm-solve__why">Ikkinchi bolaga berishdan oldin</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">10 × 2 = 20</span>
    <span class="pm-solve__why">Birinchi bolaga berishdan oldin</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Oldinga yurib tekshiramiz</p>
  <p>20 → yarmi berildi → 10 → qolganning yarmi berildi → 5 ✓
  <br><b>Javob:</b> boshida 20 ta olma bor edi.</p>
</div>

<p><b>Endi qiyinrogʻi.</b> Savatda olma bor edi. Bolaga
<b>yarmini va yana 1 tasini</b> berdi, savatda 7 ta qoldi. Boshida
nechta edi?</p>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Ikkita amalni ajrating</p>
  <p>«Yarmini va yana 1 tasini berdi» — bu <b>ikkita</b> qadam: avval
  yarmi olindi, keyin yana 1 ta olindi. Orqaga qaytishda ular teskari
  tartibda qaytariladi: avval 1 ni qaytaramiz, keyin ikkiga
  koʻpaytiramiz.</p>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">7 + 1 = 8</span>
    <span class="pm-solve__why">Oxirgi amal «−1» edi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">8 × 2 = 16</span>
    <span class="pm-solve__why">Undan oldin yarmi olingan edi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>16 ning yarmi 8 ta, yana 1 tasi — jami 9 ta berildi.
  16 − 9 = 7 ✓</p>
</div>

<h3>Matnli masala</h3>

<p>Bekzod bozorga pul bilan bordi. Avval pulining <b>yarmini</b>
sarfladi. Keyin <b>qolganining uchdan bir qismini</b> sarfladi. Soʻng
5 000 soʻmga choy oldi va choʻntagida 15 000 soʻm qoldi.</p>

<p><b>Bekzod bozorga qancha pul bilan borgan edi?</b></p>

<p><b>Reja:</b> uchta qadam bor. Oxiridan boshlaymiz va har birini
teskarisiga almashtiramiz.</p>

<div class="pe-formula">
  <span class="pe-chip pe-chip--s">?</span>
  <span class="pe-op">→ yarmi →</span>
  <span class="pe-chip pe-chip--o">?</span>
  <span class="pe-op">→ uchdan biri →</span>
  <span class="pe-chip pe-chip--o">?</span>
  <span class="pe-op">→ −5 000 →</span>
  <span class="pe-chip pe-chip--v">15 000</span>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">15 000 + 5 000 = 20 000</span>
    <span class="pm-solve__why">Choydan oldin shuncha bor edi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Uchdan biri sarflangan → 20 000 bu <sup>2</sup>/<sub>3</sub> qism</span>
    <span class="pm-solve__why">Qolgani uchdan ikki (PM-87)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">20 000 ÷ 2 × 3 = 30 000</span>
    <span class="pm-solve__why">Butunni tikladik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">30 000 × 2 = 60 000 soʻm</span>
    <span class="pm-solve__why">Undan oldin yarmi sarflangan edi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Oldinga yurib tekshiramiz</p>
  <p>60 000 → yarmi sarflandi → 30 000 → uchdan biri (10 000)
  sarflandi → 20 000 → choy (5 000) → <b>15 000</b> ✓
  <br><b>Javob:</b> Bekzod 60 000 soʻm bilan borgan.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Yarmi ketdi, keyin qolganining uchdan biri ketdi — demak
  boshlangʻich puldan taxminan uchdan biri qolgan. 15 000 ning uch
  barobari 45 000 atrofida, ustiga choy puli — 60 000 mantiqiy ✓</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Orqaga yurildi, lekin amallar oʻzgartirilmadi:
  35 ÷ 3 − 8</p>
  <p class="pe-fix__good">35 − 8, keyin ÷ 3</p>
  <p class="pe-fix__why">Orqaga qaytishda har bir amal
  <b>teskarisiga</b> almashadi: qoʻshish ayirishga, koʻpaytirish
  boʻlishga.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Amallar teskari, lekin tartib oʻsha: ÷3, keyin
  −8</p>
  <p class="pe-fix__good">−8, keyin ÷3</p>
  <p class="pe-fix__why">Tartib ham teskari boʻladi. Eng oxirgi
  bajarilgan amal — birinchi qaytariladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">«Yarmi olindi, 5 qoldi» → 5 ÷ 2</p>
  <p class="pe-fix__good">5 × 2 = 10</p>
  <p class="pe-fix__why">Orqaga qaytganda son <b>kattalashadi</b> —
  axir biz kamayishni bekor qilyapmiz.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Javob topildi, tekshirilmadi</p>
  <p class="pe-fix__good">Javobni boshiga qoʻyib, oldinga yurish</p>
  <p class="pe-fix__why">Bu usulda tekshirish deyarli bepul: sxema
  boʻylab oldinga yurasiz va oxirida masaladagi son chiqishi
  kerak.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Bir songa 5 qoʻshilsa, 12 chiqadi. Bu son
  qanday?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>7.</b> 12 − 5 = 7. Tekshirish: 7 + 5 = 12 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Bir son 4 ga koʻpaytirilsa, 24 chiqadi. Bu
  son qanday?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>6.</b> 24 ÷ 4 = 6. Tekshirish: 6 × 4 = 24 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Bir sondan 3 ayirildi, keyin natija 2 ga
  koʻpaytirildi va 14 chiqdi. Bu son qanday?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>10.</b> Orqaga: 14 ÷ 2 = 7, keyin 7 + 3 = 10. Tekshirish:
    10 − 3 = 7, 7 × 2 = 14 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Bir son 5 ga boʻlindi, keyin 2 qoʻshildi va
  11 chiqdi. Bu son qanday?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>45.</b> Orqaga: 11 − 2 = 9, keyin 9 × 5 = 45. Tekshirish:
    45 ÷ 5 = 9, 9 + 2 = 11 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Qutidagi qalamlarning yarmi olindi va 8 tasi
  qoldi. Boshida nechta edi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>16 ta.</b> 8 × 2 = 16. Yarmi olinsa, qolgani ham yarmi —
    shuning uchun ikkiga koʻpaytiriladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Savatdagi mevaning yarmi va yana 2 tasi
  olindi, 10 tasi qoldi. Boshida nechta edi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>24 ta.</b> Orqaga: 10 + 2 = 12, keyin 12 × 2 = 24.
    Tekshirish: 24 ning yarmi 12, yana 2 tasi — jami 14 ta olindi;
    24 − 14 = 10 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">7. Bir son 2 ga koʻpaytirildi, keyin 7 ayirildi,
  soʻng 3 ga boʻlindi va 5 chiqdi. Bu son qanday?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>11.</b> Orqaga uchta qadam: 5 × 3 = 15, keyin 15 + 7 = 22,
    keyin 22 ÷ 2 = 11. Tekshirish oldinga: 11 × 2 = 22, 22 − 7 = 15,
    15 ÷ 3 = 5 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Teskaridan yurish</b><span>oxirgi natijadan boshlanishga
    qaytish; ingl. working backwards</span></li>
  <li><b>Teskari amal</b><span>bajarilgan amalni bekor qiluvchi amal;
    ingl. inverse operation</span></li>
  <li><b>Boshlangʻich qiymat</b><span>izlanayotgan dastlabki miqdor;
    ingl. starting value</span></li>
  <li><b>Oxirgi natija</b><span>hamma amaldan keyingi son; ingl. final
    result</span></li>
  <li><b>Qadam</b><span>sxemadagi bitta amal; ingl. step</span></li>
  <li><b>Sxema</b><span>amallarning oʻq bilan bogʻlangan zanjiri; ingl.
    flow diagram</span></li>
  <li><b>Tartib</b><span>amallarning bajarilish ketma-ketligi; ingl.
    order</span></li>
  <li><b>Bekor qilish</b><span>amalni teskarisi bilan yoʻqqa
    chiqarish; ingl. undoing</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Oxiri maʼlum, boshi nomaʼlum boʻlsa — teskaridan yuring.</li>
    <li>Har bir amal teskarisiga almashadi: + ↔ −, × ↔ ÷.</li>
    <li>Tartib ham teskari: oxirgi amal birinchi qaytariladi.</li>
    <li>«Yarmi olindi» ning teskarisi — ikkiga koʻpaytirish.</li>
    <li>«Yarmini va yana 1 tasini» — bu ikkita alohida qadam.</li>
    <li>Tekshirish bepul: javobni boshiga qoʻyib, oldinga yuring.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-99 — namuna izlash va umumlashtirish
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-99: Namuna izlash va umumlashtirish",
        "category": "math",
        "order": 99,
        "summary": (
            "Kichik hollarni hisoblang, namunani koʻring va uni n orqali "
            "yozing — shunda bitta formula cheksiz koʻp savolga javob "
            "beradi. Lekin namuna taxmin beradi, isbot emas."
        ),
        "stories": ["Gaussning bolaligi — 1 dan 100 gacha"],
        "content": """
<h2>PM-99: Namuna izlash va umumlashtirish</h2>

<p>1 dan 100 gacha boʻlgan hamma sonni qoʻshing. Qoʻlda.</p>

<p>Bu masalani bundan ikki asr oldin bir maktab oʻqituvchisi sinfga
bergan — bolalarni bir soatga band qilish uchun. Bir bola javobni
bir necha soniyada aytgan.</p>

<p>U <b>tezroq qoʻshmagan</b>. U boshqa narsa qilgan: <b>namuna</b>
koʻrgan. Bu darsda biz ham shuni qilamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>kichik hollarni hisoblab, namunani topasiz;</li>
    <li>namunani n harfi orqali yozasiz;</li>
    <li>formulani kichik hollarda tekshirasiz;</li>
    <li>namuna qachon aldashini bilib olasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Umumlashtirish yoʻli</span>
  <span class="pe-chip pe-chip--o">kichik hollar</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">namuna</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">n orqali formula</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--adv">tekshirish</span>
</div>

<h3>1. Gaussning hiylasi</h3>

<p>Sonlarni ikki uchidan juftlaymiz:</p>

<div class="pe-ex">
  <p class="pe-ex__math">1 + 100 = 101 · 2 + 99 = 101 · 3 + 98 = 101 …</p>
  <p class="pe-ex__uz">Har bir juftlik roppa-rosa 101 beradi.</p>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">100 ta son → 50 ta juftlik</span>
    <span class="pm-solve__why">Har juftlikda ikkita son</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">50 × 101 = 5050</span>
    <span class="pm-solve__why">Har juftlik 101 ga teng</span>
  </div>
</div>

<p>Endi buni <b>istalgan</b> n uchun yozamiz. n ta son bor, juftlik
soni n ÷ 2, har juftlik n + 1 ga teng:</p>

<div class="pe-formula">
  <span class="pe-formula__label">1 dan n gacha yigʻindi</span>
  <span class="pe-chip pe-chip--s">S</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">n × (n + 1)</span>
  <span class="pe-op">÷</span>
  <span class="pe-chip pe-chip--o">2</span>
</div>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>n</th><th>Formula boʻyicha</th><th>Bevosita qoʻshib</th></tr>
  <tr><td>4</td><td class="pm-word__sym">4 × 5 ÷ 2 = 10</td><td>1+2+3+4 = 10 ✓</td></tr>
  <tr><td>5</td><td class="pm-word__sym">5 × 6 ÷ 2 = 15</td><td>1+2+3+4+5 = 15 ✓</td></tr>
  <tr><td>10</td><td class="pm-word__sym">10 × 11 ÷ 2 = 55</td><td>55 ✓</td></tr>
  <tr><td>100</td><td class="pm-word__sym">100 × 101 ÷ 2 = 5050</td><td>Gaussning javobi ✓</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Formulani har doim kichik hollarda tekshiring</p>
  <p>n = 1, 2, 3 kabi kichik sonlar bilan sinash bir necha soniya vaqt
  oladi va notoʻgʻri formulani darrov fosh qiladi. n = 1 uchun:
  1 × 2 ÷ 2 = 1 ✓</p>
</div>

<h3>2. Toq sonlar va kvadratlar</h3>

<p>Endi oʻzingiz namuna toping. Ketma-ket toq sonlarni qoʻshamiz:</p>

<div class="pe-ex">
  <p class="pe-ex__math">1 = 1 · 1 + 3 = 4 · 1 + 3 + 5 = 9 · 1 + 3 + 5 + 7 = 16</p>
  <p class="pe-ex__uz">1, 4, 9, 16 — bular aniq kvadratlar (PM-13).</p>
</div>

<figure class="pm-fig">
  <svg viewBox="0 0 320 120" role="img" aria-label="Toq sonlar yigʻindisi kvadrat hosil qiladi">
    <circle class="pm-pt" cx="45" cy="55" r="5"/>
    <text class="pm-lbl" x="45" y="100" text-anchor="middle">1 = 1²</text>
    <circle class="pm-pt" cx="110" cy="45" r="5"/>
    <circle class="pm-pt" cx="132" cy="45" r="5"/>
    <circle class="pm-pt" cx="110" cy="67" r="5"/>
    <circle class="pm-pt" cx="132" cy="67" r="5"/>
    <text class="pm-lbl" x="121" y="100" text-anchor="middle">1+3 = 2²</text>
    <circle class="pm-pt" cx="215" cy="35" r="5"/>
    <circle class="pm-pt" cx="237" cy="35" r="5"/>
    <circle class="pm-pt" cx="259" cy="35" r="5"/>
    <circle class="pm-pt" cx="215" cy="57" r="5"/>
    <circle class="pm-pt" cx="237" cy="57" r="5"/>
    <circle class="pm-pt" cx="259" cy="57" r="5"/>
    <circle class="pm-pt" cx="215" cy="79" r="5"/>
    <circle class="pm-pt" cx="237" cy="79" r="5"/>
    <circle class="pm-pt" cx="259" cy="79" r="5"/>
    <text class="pm-lbl" x="237" y="100" text-anchor="middle">1+3+5 = 3²</text>
  </svg>
  <figcaption>Har safar qoʻshilgan toq son kvadratning chetiga bitta
  «burchak» qoʻshadi va yana kvadrat hosil boʻladi. Shuning uchun
  birinchi n ta toq sonning yigʻindisi n².</figcaption>
</figure>

<div class="pe-formula">
  <span class="pe-formula__label">Birinchi n ta toq son</span>
  <span class="pe-chip pe-chip--o">1 + 3 + 5 + … + (2n − 1)</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">n<sup>2</sup></span>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>n = 5: 1 + 3 + 5 + 7 + 9 = 25 va 5² = 25 ✓
  <br>n = 10 uchun javob 10² = 100 — yuzta son qoʻshmasdan.</p>
</div>

<h4>Nega shunday? Kvadratdan kvadratga oʻtish qoidasi</h4>

<p>Yuqoridagi chizmada har safar kvadratga bitta <b>burchak</b> qoʻshildi.
Endi oʻsha burchakda nechta nuqta borligini sanaymiz.</p>

<p>n × n kvadratni (n + 1) × (n + 1) ga aylantirish uchun: oʻng
tomonga <b>n</b> ta nuqta, tepaga yana <b>n</b> ta, va burchakka
<b>1</b> ta qoʻshiladi.</p>

<div class="pe-formula">
  <span class="pe-formula__label">Burchakdagi nuqtalar</span>
  <span class="pe-chip pe-chip--o">n</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">n</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">1</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">2n + 1</span>
</div>

<p>Va <b>2n + 1</b> har doim toq son. Mana nima uchun qoʻshiladigan
sonlar aynan toq boʻlib chiqadi — bu tasodif emas, kvadratning
shaklidan kelib chiqadi.</p>

<div class="pe-formula">
  <span class="pe-formula__label">Kvadratdan keyingi kvadratga</span>
  <span class="pe-chip pe-chip--o">n<sup>2</sup></span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">(2n + 1)</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">(n + 1)<sup>2</sup></span>
</div>

<p>Buni algebra bilan ham koʻrsatish mumkin. Qisqa koʻpaytirish
formulasiga koʻra (PM-44):</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">(n + 1)<sup>2</sup> = n<sup>2</sup> + 2n + 1</span>
    <span class="pm-solve__why">Qavsni ochdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">demak (n + 1)<sup>2</sup> − n<sup>2</sup> = 2n + 1</span>
    <span class="pm-solve__why">Ikki qoʻshni kvadratning farqi</span>
  </div>
</div>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Kvadrat</th><th>Qoʻshiladigan 2n + 1</th><th>Keyingi kvadrat</th></tr>
  <tr><td>1<sup>2</sup> = 1</td><td class="pm-word__sym">2 × 1 + 1 = 3</td><td>1 + 3 = 4 = 2<sup>2</sup></td></tr>
  <tr><td>2<sup>2</sup> = 4</td><td class="pm-word__sym">2 × 2 + 1 = 5</td><td>4 + 5 = 9 = 3<sup>2</sup></td></tr>
  <tr><td>3<sup>2</sup> = 9</td><td class="pm-word__sym">2 × 3 + 1 = 7</td><td>9 + 7 = 16 = 4<sup>2</sup></td></tr>
  <tr><td>9<sup>2</sup> = 81</td><td class="pm-word__sym">2 × 9 + 1 = 19</td><td>81 + 19 = 100 = 10<sup>2</sup></td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Bu qoida ogʻzaki hisobda ish beradi</p>
  <p>Kvadratni bilsangiz, keyingisini yodlash shart emas — uni
  <b>chiqarib olasiz</b>. 30<sup>2</sup> = 900 ekanini bilsangiz,
  31<sup>2</sup> = 900 + (2 × 30 + 1) = 900 + 61 = <b>961</b>.
  Xuddi shunday orqaga ham: 29<sup>2</sup> = 900 − (2 × 29 + 1) =
  900 − 59 = <b>841</b>.</p>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Ikki qarash, bitta haqiqat</p>
  <p>Chizma «har safar burchak qoʻshiladi» deydi. Algebra
  «(n + 1)² − n² = 2n + 1» deydi. Bu bir gapning ikki tili — va
  ikkalasi ham nima uchun toq sonlar yigʻindisi kvadrat berishini
  tushuntiradi.</p>
</div>

<h3>3. Ketma-ketlikdan formulaga</h3>

<p>Namuna izlashning eng koʻp uchraydigan turi: qator berilgan,
n-hadini toping.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Qator</th><th>Har qadamda</th><th>n-hadi</th></tr>
  <tr><td>2, 5, 8, 11, …</td><td class="pm-word__sym">+3</td><td>3n − 1</td></tr>
  <tr><td>3, 7, 11, 15, …</td><td class="pm-word__sym">+4</td><td>4n − 1</td></tr>
  <tr><td>5, 10, 15, 20, …</td><td class="pm-word__sym">+5</td><td>5n</td></tr>
  <tr><td>1, 4, 9, 16, …</td><td class="pm-word__sym">kvadratlar</td><td>n<sup>2</sup></td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Qadam formulani aytib turadi</p>
  <p>Har qadamda +3 boʻlsa, formulada <b>3n</b> boʻladi. Qolgani —
  toʻgʻrilash: n = 1 da 3 chiqadi, bizga esa 2 kerak, demak «− 1».
  Shunday qilib 3n − 1. Tekshiramiz: n = 4 → 3 × 4 − 1 = 11 ✓</p>
</div>

<h3>4. Shakldan formulaga</h3>

<p>Gugurt choʻplaridan qator qilib kvadratlar yasaymiz.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 110" role="img" aria-label="Uchta kvadrat oʻn tayoqchadan yasalgan">
    <line class="pm-ln pm-ln--hl" x1="100" y1="35" x2="100" y2="65"/>
    <line class="pm-ln pm-ln--hl" x1="130" y1="35" x2="130" y2="65"/>
    <line class="pm-ln pm-ln--hl" x1="160" y1="35" x2="160" y2="65"/>
    <line class="pm-ln pm-ln--hl" x1="190" y1="35" x2="190" y2="65"/>
    <line class="pm-ln" x1="100" y1="35" x2="130" y2="35"/>
    <line class="pm-ln" x1="130" y1="35" x2="160" y2="35"/>
    <line class="pm-ln" x1="160" y1="35" x2="190" y2="35"/>
    <line class="pm-ln" x1="100" y1="65" x2="130" y2="65"/>
    <line class="pm-ln" x1="130" y1="65" x2="160" y2="65"/>
    <line class="pm-ln" x1="160" y1="65" x2="190" y2="65"/>
    <text class="pm-lbl" x="145" y="90" text-anchor="middle">3 ta kvadrat — 10 ta tayoqcha</text>
    <text class="pm-lbl" x="145" y="22" text-anchor="middle">4 ta tik tayoqcha (qalin)</text>
  </svg>
  <figcaption>Har bir kvadrat ustiga bitta tik tayoqcha va ikkita
  yotiq tayoqcha qoʻshadi; boshida esa bitta qoʻshimcha tik tayoqcha
  turadi.</figcaption>
</figure>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Kvadratlar</th><th>Tayoqchalar</th><th>Farq</th></tr>
  <tr><td>1</td><td class="pm-word__sym">4</td><td>—</td></tr>
  <tr><td>2</td><td class="pm-word__sym">7</td><td>+3</td></tr>
  <tr><td>3</td><td class="pm-word__sym">10</td><td>+3</td></tr>
  <tr><td>n</td><td class="pm-word__sym">3n + 1</td><td>+3</td></tr>
</table></div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>n = 1: 3 × 1 + 1 = 4 ✓ n = 3: 3 × 3 + 1 = 10 ✓
  <br>n = 10 uchun: 3 × 10 + 1 = 31 ta tayoqcha — chizmasdan.</p>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Formulaning maʼnosini oʻqing</p>
  <p>3n + 1 shunchaki son emas — u shaklni tushuntiradi: har bir
  kvadrat <b>3 ta</b> yangi tayoqcha qoʻshadi, ustiga boshida
  <b>1 ta</b> qoʻshimcha turadi. Formulani maʼnosi bilan tushunsangiz,
  uni hech qachon unutmaysiz.</p>
</div>

<h3>5. Namuna aldashi ham mumkin</h3>

<p>Endi darsning eng muhim ogohlantirishi.</p>

<p>Aylana chizib, uning chetiga nuqtalar qoʻyamiz va har bir nuqtani
qolganlari bilan chiziq orqali tutashtiramiz. Aylana nechta boʻlakka
boʻlinadi?</p>

<div class="pe-ex">
  <p class="pe-ex__math">1, 2, 4, 8, 16, …</p>
  <p class="pe-ex__uz">Har safar ikki barobar — namuna aniq
  koʻrinyapti.</p>
</div>

<p>Keyingisi 32 boʻlishi kerak-ku? Sanab koʻrilsa, u
<strong>31</strong> chiqadi.</p>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Namuna — taxmin, isbot emas</p>
  <p>Beshta hol toʻgʻri chiqqani formulaning rost ekanini
  <b>bildirmaydi</b>. Namuna sizga nima izlash kerakligini aytadi;
  uning rostligini esa <b>sabab</b> koʻrsatib isbotlash kerak —
  masalan juftlash (Gauss) yoki chizma (toq sonlar va kvadratlar)
  orqali.</p>
</div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Namuna koʻrish</p>
    <p>Kichik hollarni hisoblab, qonuniyatni sezish. Tez, foydali —
    lekin ishonchsiz.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Sababni koʻrsatish</p>
    <p>Nega shunday boʻlishini tushuntirish. Sekinroq — lekin shundan
    keyin shubha qolmaydi.</p>
  </div>
</div>

<h3>Matnli masala</h3>

<p>Kafeda kvadrat stollar qatorga qoʻyiladi. Bitta stolga 4 kishi
oʻtiradi. Ikkita stol yonma-yon qoʻyilsa, 6 kishi oʻtiradi (tegib
turgan tomonlarga oʻtirib boʻlmaydi). Uchta stolga 8 kishi
oʻtiradi.</p>

<p><b>20 ta stol qatorga qoʻyilsa, necha kishi oʻtiradi?</b></p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Stollar</th><th>Kishilar</th><th>Farq</th></tr>
  <tr><td>1</td><td class="pm-word__sym">4</td><td>—</td></tr>
  <tr><td>2</td><td class="pm-word__sym">6</td><td>+2</td></tr>
  <tr><td>3</td><td class="pm-word__sym">8</td><td>+2</td></tr>
</table></div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Har qadamda +2 → formulada 2n</span>
    <span class="pm-solve__why">Har yangi stol 2 ta joy qoʻshadi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">n = 1 da 2 chiqadi, kerak 4 → «+2»</span>
    <span class="pm-solve__why">Toʻgʻrilash qoʻshimchasi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Formula: 2n + 2</span>
    <span class="pm-solve__why">Ikki uchidagi joylar — oʻsha «+2»</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2 × 20 + 2 = 42 kishi</span>
    <span class="pm-solve__why">Yigirmata stol uchun</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Uchala kichik holni ham tekshiramiz</p>
  <p>n = 1: 2 + 2 = 4 ✓ n = 2: 4 + 2 = 6 ✓ n = 3: 6 + 2 = 8 ✓
  <br><b>Javob:</b> 42 kishi oʻtiradi.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Sababni ham koʻring</p>
  <p>Har bir stol yuqoriga bitta va pastga bitta joy beradi — bu
  <b>2n</b>. Qatorning ikki uchida esa yana bittadan joy qoladi — bu
  <b>+2</b>. Endi formula shunchaki topilgan emas,
  <b>tushunilgan</b>.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Namuna topildi → «demak formula isbotlandi»</p>
  <p class="pe-fix__good">Namuna taxmin beradi; sabab isbot beradi</p>
  <p class="pe-fix__why">1, 2, 4, 8, 16 dan keyin 31 kelishi mumkin.
  Bir necha hol yetarli dalil emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">2, 5, 8, 11 → n-hadi «3n»</p>
  <p class="pe-fix__good">3n − 1</p>
  <p class="pe-fix__why">Qadam toʻgʻri topilgan, lekin toʻgʻrilash
  unutilgan. n = 1 da 3 chiqadi, kerak esa 2.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Formula yozildi, kichik hollarda
  tekshirilmadi</p>
  <p class="pe-fix__good">n = 1, 2, 3 bilan sinash</p>
  <p class="pe-fix__why">Bir necha soniya vaqt oladi va notoʻgʻri
  formulani darrov fosh qiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">1 + 2 + … + 100 = 100 × 101 = 10 100</p>
  <p class="pe-fix__good">100 × 101 ÷ 2 = 5050</p>
  <p class="pe-fix__why">Juftlaganda har bir son <b>ikki marta</b>
  sanaladi — shuning uchun 2 ga boʻlinadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 1 + 2 + 3 + … + 20 yigʻindisini toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>210.</b> 20 × 21 ÷ 2 = 210.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Birinchi 10 ta toq sonning yigʻindisi
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>100.</b> 10² = 100. Yaʼni 1 + 3 + 5 + … + 19 = 100.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 3, 7, 11, 15, … qatorining 8-hadi qanday?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>31.</b> Har qadamda +4 → 4n; n = 1 da 4 chiqadi, kerak 3 →
    4n − 1. Demak 4 × 8 − 1 = 31. Tekshirish: n = 2 → 7 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 1, 4, 9, 16, … qatorining 7-hadi qanday?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>49.</b> Bular aniq kvadratlar: n². 7² = 49.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Gugurt choʻplaridan qatorga uchburchaklar
  yasaladi: 1 tasi — 3 ta choʻp, 2 tasi — 5 ta, 3 tasi — 7 ta.
  10 ta uchburchak uchun nechta choʻp kerak?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>21 ta.</b> Har qadamda +2 → 2n; n = 1 da 2 chiqadi, kerak
    3 → 2n + 1. Demak 2 × 10 + 1 = 21. Tekshirish: n = 3 →
    7 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. 8 kishi bir-biri bilan bir martadan qoʻl
  berdi. Nechta qoʻl berish boʻlgan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>28 ta.</b> Har biri qolgan 7 kishi bilan: 8 × 7 = 56, lekin
    har bir qoʻl berish ikki marta sanaldi (PM-96), demak 56 ÷ 2 = 28.
    Umumiy formula: n(n − 1) ÷ 2.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">7. 40<sup>2</sup> = 1600 ekani maʼlum.
  41<sup>2</sup> ni yodlamasdan toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>1681.</b> n<sup>2</sup> + (2n + 1) = (n + 1)<sup>2</sup>
    qoidasi bilan: 1600 + (2 × 40 + 1) = 1600 + 81 = 1681.
    Tekshirish: 41 × 41 = 1681 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">8. 1 dan 50 gacha boʻlgan sonlar yigʻindisi
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>1275.</b> 50 × 51 ÷ 2 = 1275. Juftlash bilan: 25 ta juftlik,
    har biri 51 ga teng: 25 × 51 = 1275 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Namuna</b><span>takrorlanadigan qonuniyat; ingl.
    pattern</span></li>
  <li><b>Umumlashtirish</b><span>bir necha holdan umumiy qoida
    chiqarish; ingl. generalisation</span></li>
  <li><b>Ketma-ketlik</b><span>maʼlum qoida boʻyicha kelgan sonlar
    qatori; ingl. sequence</span></li>
  <li><b>Had</b><span>ketma-ketlikdagi bitta son; ingl. term</span></li>
  <li><b>n-hadi</b><span>istalgan oʻrindagi hadni beruvchi ifoda; ingl.
    nth term</span></li>
  <li><b>Formula</b><span>qoidaning harflar bilan yozuvi; ingl.
    formula</span></li>
  <li><b>Aniq kvadrat</b><span>butun sonning kvadrati: 1, 4, 9, 16;
    ingl. perfect square</span></li>
  <li><b>Juftlash</b><span>sonlarni ikki uchidan qoʻshib hisoblash;
    ingl. pairing</span></li>
  <li><b>Isbot</b><span>sabab koʻrsatib, shubhani yoʻqotish; ingl.
    proof</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Kichik hollarni hisoblang — namuna oʻzi koʻrinadi.</li>
    <li>Har qadamdagi farq formulaning koeffitsiyentini beradi.</li>
    <li>Keyin toʻgʻrilang: n = 1 da kerakli son chiqsin.</li>
    <li>Formulani n = 1, 2, 3 bilan albatta tekshiring.</li>
    <li>1 + 2 + … + n = n(n + 1) ÷ 2.</li>
    <li>Birinchi n ta toq sonning yigʻindisi n².</li>
    <li><b>n² + (2n + 1) = (n + 1)²</b> — kvadratdan keyingi kvadratga
      oʻtish; shuning uchun qoʻshiladigan sonlar toq.</li>
    <li><b>Namuna taxmin beradi, isbot emas</b> — sababni ham
      koʻrsating.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-100 — YAKUNIY DARS
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-100: Yakuniy dars — siz qayerdasiz va endi nima qilasiz",
        "category": "math",
        "order": 100,
        "summary": (
            "Yuz dars ortda qoldi. Bu darsda yangi qoida yoʻq: bu — "
            "butun kursning xaritasi, uning oʻzagidagi bir necha gʻoya "
            "va bundan keyingi yoʻl."
        ),
        "stories": ["Yuz darsdan keyin — oʻquvchiga xat"],
        "content": """
<h2>PM-100: Yakuniy dars — siz qayerdasiz va endi nima qilasiz</h2>

<p>PM-1 da biz bitta oddiy savoldan boshlagandik: <i>nega 25 dagi
2 ikkita emas, yigirmata?</i></p>

<p>Bugun siz tenglama yechasiz, grafik oʻqiysiz, uchburchakning
tomonini topasiz, diagrammaning aldayotganini koʻrasiz va nima uchun
oʻn beshta stakanni ikkitadan agʻdarib toʻgʻrilab boʻlmasligini
<b>isbotlay olasiz</b>.</p>

<p>Bu darsda yangi qoida yoʻq. Bu — orqaga qarash, va oldinga
koʻrsatish.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda</p>
  <ul>
    <li>butun kursning xaritasini koʻrasiz;</li>
    <li>uni bir-biriga bogʻlab turgan gʻoyalarni bilib olasiz;</li>
    <li>endi nimalarni qila olishingizni tekshirasiz;</li>
    <li>keyin qayerga borishni tanlaysiz.</li>
  </ul>
</div>

<h3>1. Yuz darsning xaritasi</h3>

<p>Kurs sakkizta blokdan iborat edi. Har birining oʻz asosiy gʻoyasi
bor — va aynan shu gʻoya esda qolishi kerak.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Blok</th><th>Darslar</th><th>Asosiy gʻoya</th></tr>
  <tr><td><b>A.</b> Sonlar va amallar</td><td class="pm-word__sym">1–14</td>
    <td>Raqamning oʻrni uning qiymatini belgilaydi</td></tr>
  <tr><td><b>B.</b> Kasr, foiz, nisbat</td><td class="pm-word__sym">15–28</td>
    <td>Foiz — son emas, <b>nimadandir</b> olingan ulush</td></tr>
  <tr><td><b>C.</b> Algebra tili</td><td class="pm-word__sym">29–44</td>
    <td>Harf — nomaʼlum emas, <b>gapni yozish usuli</b></td></tr>
  <tr><td><b>D.</b> Funksiya va grafik</td><td class="pm-word__sym">45–56</td>
    <td>Grafik — rasm emas, <b>maʼlumot</b></td></tr>
  <tr><td><b>E.</b> Geometriya</td><td class="pm-word__sym">57–74</td>
    <td>Chizmani oʻlchash emas, undan <b>xulosa chiqarish</b></td></tr>
  <tr><td><b>F.</b> Maʼlumot va ehtimollik</td><td class="pm-word__sym">75–84</td>
    <td>Rost sonlar ham notoʻgʻri taassurot berishi mumkin</td></tr>
  <tr><td><b>G.</b> Matnli masalalar</td><td class="pm-word__sym">85–94</td>
    <td>Masala hisobdan emas, <b>oʻqishdan</b> boshlanadi</td></tr>
  <tr><td><b>H.</b> Mantiq va fikrlash</td><td class="pm-word__sym">95–100</td>
    <td>«Bilaman» bilan <b>«isbotlay olaman»</b> — ikki har xil gap</td></tr>
</table></div>

<h3>2. Kursni bir-biriga bogʻlab turgan gʻoyalar</h3>

<p>Yuz dars — yuzta alohida mavzu emas. Ular orasidan bir necha ip
oʻtadi. Mana ular.</p>

<h4>Bitta uchlik — uch marta</h4>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Dars</th><th>Formula</th><th>Oʻrtadagi kattalik</th></tr>
  <tr><td>PM-88 — harakat</td><td class="pm-word__sym">S = v × t</td>
    <td>bir soatda bosilgan masofa</td></tr>
  <tr><td>PM-90 — ish</td><td class="pm-word__sym">ish = u × t</td>
    <td>bir kunda bajarilgan ish</td></tr>
  <tr><td>PM-92 — savdo</td><td class="pm-word__sym">qiymat = narx × miqdor</td>
    <td>bir kilogrammning narxi</td></tr>
</table></div>

<p>Uchalasida oʻrtadagi kattalik bir xil maʼnoda: <b>bitta birlikka
toʻgʻri keladigan miqdor</b>. Va uchalasida bir xil xato uchraydi —
oʻrtadagi ustunni qoʻshib yuborish. Tezliklar ham, unumdorliklar ham
(bir jism uchun), narxlar ham qoʻshilmaydi.</p>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Toʻrt qadam — har qanday masala uchun</p>
  <p><b>Oʻqi → reja tuz → yech → tekshir</b> (PM-85). Bu toʻrt qadam
  matnli masala uchun yozilgan edi, lekin u geometriyada ham,
  ehtimollikda ham, mantiqda ham ishlaydi. Birinchi qadam eng uzun,
  uchinchisi eng qisqa boʻlishi kerak.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">«Javob mantiqiymi?» — kursning eng foydali savoli</p>
  <p>Velosipedda 120 km/soat. Sof tuz eritmadan ogʻir. Ehtimollik 1,2.
  Birga ishlaganda ish sekinlashdi. Bularning hammasini bitta savol
  ushlaydi va u hech qanday hisob talab qilmaydi.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Ikki marta hisoblang — boshqa yoʻldan</p>
  <p>Bir xil yoʻldan ikki marta yurish xatoni takrorlaydi.
  <b>Boshqa</b> yoʻldan yurish esa uni ushlaydi: plitkani metrda ham,
  santimetrda ham sanang (PM-94); javobni sxema boshiga qoʻyib
  oldinga yuring (PM-98); aralashmani sof modda balansi bilan
  tekshiring (PM-91).</p>
</div>

<h3>3. Siz endi nimalarni qila olasiz</h3>

<p>Bu roʻyxatni oʻqing va har biriga «ha» yoki «hali yoʻq» deb javob
bering. «Hali yoʻq» boʻlsa — oʻsha darsga qayting, u hech qayoqqa
ketmaydi.</p>

<div class="pe-steps">
  <ol>
    <li>Kasr, oʻnlik kasr va foizni bir-biriga oʻgira olaman
      (PM-22).</li>
    <li>Chegirmani va narx oʻzgarishini hisoblay olaman
      (PM-25, PM-26).</li>
    <li>Matndan tenglama tuza olaman va uni yecha olaman
      (PM-30, PM-36).</li>
    <li>Grafikdan tarifni oʻqiy olaman va qaysi biri foydali ekanini
      ayta olaman (PM-51, PM-52).</li>
    <li>Pifagor teoremasi bilan uchinchi tomonni topa olaman
      (PM-64).</li>
    <li>Yuza va perimetrni chalkashtirmayman (PM-67, PM-68).</li>
    <li>Oʻrtacha bilan medianani farqlay olaman va qaysi biri
      haqiqatni yaxshiroq aytishini bilaman (PM-79).</li>
    <li>Aldamchi diagrammani tanib olaman (PM-81).</li>
    <li>Harakat, ish va savdo masalalarini yecha olaman
      (PM-88…92).</li>
    <li>Birliklarni moslay olaman va 1 m² = 10 000 sm² ekanini
      bilaman (PM-94).</li>
    <li>Nimadir <b>mumkin emasligini</b> isbotlay olaman
      (PM-96).</li>
    <li>Nimadir <b>borligini</b> — uni topmasdan turib — isbotlay
      olaman (PM-97).</li>
  </ol>
</div>

<h3>4. Endi qayerga borish mumkin</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">SAT Math kursi</p>
    <p>Oʻsha matematikaning imtihon koʻrinishi — lekin
    <b>ingliz tilida</b>. Har bir darsning oxiridagi «Kalit soʻzlar»
    roʻyxati aynan shu koʻprik uchun yozilgan edi. Siz uni bilmasdan
    tayyorlab qoʻygansiz.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Matematika olami</p>
    <p>Corner javonidagi matnlar: al-Xorazmiy va Beruniy, tabiatdagi
    matematika, jumboqlar. Darsga bogʻlanmagan — shunchaki
    oʻqish uchun.</p>
  </div>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Va yana ikkita yoʻl</p>
  <p><b>Matematika chempionati</b> — tez hisoblash oʻyini; kurs
  bergan tezlikni shu yerda sinang.
  <br><b>Qaytib oʻqish</b> — eng kam baholangan usul. Ikkinchi marta
  oʻqilgan dars birinchisidan butunlay boshqacha koʻrinadi, chunki
  endi siz undan keyingisini ham bilasiz.</p>
</div>

<h3>Oxirgi soʻz</h3>

<p>Bu kursda biz koʻp marta bir gapni takrorladik: <b>qoidani
yodlash yetarli emas, uning nega ishlashini tushunish kerak</b>.</p>

<p>Sababi oddiy. Yodlangan qoida bir oyda unutiladi. Tushunilgan
qoida esa unutilsa ham — qayta chiqariladi. Kasrni boʻlishda nega
teskarisiga koʻpaytirilishini bilsangiz, formulani esdan chiqarganda
uni oʻzingiz tiklay olasiz.</p>

<p>Va yana bir narsa. Bu kursda «bilmadim» degan javob koʻp marta
toʻgʻri javob boʻldi — masalada maʼlumot yetmaganda (PM-94), Dirixle
odamlarning kimligini aytmaganda (PM-97), namuna isbot boʻlmaganda
(PM-99).</p>

<p>Nimani bilmasligini aniq bilish — bu ham matematika. Balki uning
eng qiyin qismidir.</p>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Yuz dars nima berdi</p>
  <p>Siz endi tezroq hisoblaysiz — bu rost. Lekin asosiysi boshqa:
  siz endi <b>savol bera olasiz</b>. «Bu son qayerdan chiqdi?»
  «Oʻq noldan boshlanganmi?» «Buni qanday bilamiz?» «Javob
  mantiqiymi?»
  <br>Bu savollarni beradigan odamni aldash qiyin — matematikada
  ham, undan tashqarida ham.</p>
</div>

<div class="pe-recap">
  <p class="pe-recap__t">Yoʻlning oxiri va boshi</p>
  <ul>
    <li>Sakkiz blok, yuz dars, ikki mingdan ortiq mashq savoli —
      ortda qoldi.</li>
    <li>Uchta bir xil uchlik, toʻrt qadam va bitta savol: «javob
      mantiqiymi?»</li>
    <li>Har bir qoidaning sababi bor edi — shuning uchun ular
      qayta tiklanadi.</li>
    <li>«Bilmadim» ni aniq aytish ham koʻnikma.</li>
    <li>Keyingi yoʻl: SAT Math, Matematika olami, chempionat — yoki
      shu kursning oʻzini qaytadan.</li>
    <li><b>Rahmat.</b> Yuz darsni oxirigacha oʻqib chiqish — oson
      ish emas edi.</li>
  </ul>
</div>
""",
    },
]
