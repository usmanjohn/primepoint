# -*- coding: utf-8 -*-
"""Prime Math — darslar 87–89 (chizma; harakat 1; harakat 2).

**Blok G: Matnli masalalar ustaxonasi (85–94).**
Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md

  mashqlar — practice/management/commands/_practice_pm_87_89.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_87_89.py

⚠️ Uchlikning ichki mantigʻi: PM-87 CHIZISHNI oʻrgatadi, PM-88 va
   PM-89 esa oʻsha chizmani ishga soladi. Harakat masalalari kursda
   birinchi marta sxemasiz yechilmaydigan turdagi masala — shuning
   uchun chizma darsi ulardan oldin turadi.

⚠️ Kumulyativ chegaralar:
  • PM-87 — tasma model, kesma chizma va oʻq sxemasi. Faqat CHIZISH
    usuli; harakat formulasi bu darsda oʻrgatilmaydi (bitta misolda
    yoʻl boʻlaklarga ajratiladi, lekin tezlik ishlatilmaydi).
    ⛔ «Teskaridan yurish» ATAMA sifatida YOʻQ — u PM-98 niki; bu
    yerda sxema tuzilib, tenglama bilan yechiladi;
  • PM-88 — S = v·t uchligi, birliklarni moslash, oʻrtacha tezlik.
    S = v·t PM-35 da formula sifatida koʻrilgan — bu yerda u masala
    yechish quroliga aylanadi. ⛔ Ikki harakatlanuvchi YOʻQ (PM-89);
  • PM-89 — uchrashuv (v₁ + v₂) va quvish (v₁ − v₂). ⛔ Oqim boʻylab
    harakat (qayiq/daryo) kursda umuman yoʻq; ish va unumdorlik PM-90 da.
  • Faol ishlatiladi: S = v·t (PM-35), tenglama (PM-36/37), nomaʼlum
    tanlash va jadval (PM-86), kasr va oʻnlik kasr (PM-15…21),
    oʻrtacha arifmetik (PM-78).

⚠️ Arifmetika darvozasi: scratchpad/verify_pm_87_89.py hamma sonni
   qayta hisoblaydi (34/50, 100/200/300, 50/100/30, 150 km, 80 km/soat,
   1,5 soat, 40 km/soat, 16 km, 3 soat, 1 soat, 50 km/soat, 12:00).

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_87_89.py --author=prime
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
    # PM-87 — chizma va sxema
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-87: Chizma va sxema — masalani koʻrish",
        "category": "math",
        "order": 87,
        "summary": (
            "Chizma masalani osonlashtirmaydi — uni koʻrinadigan qiladi. "
            "Tasma model, kesma chizma va oʻq sxemasi: uchta chizma turi "
            "va ularning har biri qaysi masalaga mos kelishi."
        ),
        "stories": ["Chizib yechilgan masala"],
        "content": """
<h2>PM-87: Chizma va sxema — masalani koʻrish</h2>

<p>«Ikki doʻst 96 000 soʻm yigʻdi, biri ikkinchisidan 12 000 soʻm koʻp
yigʻdi». Bu gapni oʻqib, javobni darrov aytolmaysiz.</p>

<p>Endi shu gapni ikkita tasma qilib chizing — biri sal uzunroq. Uzun
tasmaning ortiqcha uchini qirqib tashlang. Qolgani ikkita <b>teng</b>
tasma. Javob koʻrinib qoldi.</p>

<p>Chizma masalani osonlashtirmaydi. U masalani <b>koʻrinadigan</b>
qiladi — bogʻlanishlar uzunlikka aylanadi va koʻz ular bilan
ishlay boshlaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>uchta chizma turini va ularning oʻrnini bilib olasiz;</li>
    <li>tasma modelda «ortiqchani qirqish» usulini qoʻllaysiz;</li>
    <li>yoʻl yoki uzunlikni kesma chizma bilan boʻlasiz;</li>
    <li>oʻzgarishli masalani oʻq sxemasi bilan yozasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uchta chizma</span>
  <span class="pe-chip pe-chip--o">tasma model</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">kesma chizma</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">oʻq sxemasi</span>
</div>

<h3>1. Qaysi masalaga qaysi chizma</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Masalada shu bor</th><th>Chizma</th><th>Misol</th></tr>
  <tr><td>Butun va uning boʻlaklari</td><td class="pm-word__sym">tasma model</td>
    <td>ikki doʻst pulni boʻlishdi</td></tr>
  <tr><td>Uzunlik, yoʻl, vaqt oraligʻi</td><td class="pm-word__sym">kesma chizma</td>
    <td>yoʻlning uchdan biri avtobusda</td></tr>
  <tr><td>Bosqichma-bosqich oʻzgarish</td><td class="pm-word__sym">oʻq sxemasi</td>
    <td>yarmi olindi, keyin yana 6 tasi</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Chizma qoidasi</p>
  <p>Chizmadagi <b>uzunlik nisbatni koʻrsatishi shart</b>. 2x deb
  belgilangan tasma x tasmadan roppa-rosa ikki barobar uzun boʻlsin.
  Aks holda chizma yordam bermaydi — u shunchaki bezak boʻlib
  qoladi.</p>
</div>

<h3>2. Tasma model va «ortiqchani qirqish»</h3>

<p><b>Masala.</b> Afsona va Bekzod birgalikda 96 000 soʻm yigʻishdi.
Afsona Bekzoddan 12 000 soʻm koʻp yigʻdi. Har biri qancha yigʻdi?</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">Bekzod</span>
    <span class="pm-model__bar" style="width:44%">x</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">Afsona</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:56%">x + 12 000</span>
  </div>
  <p class="pm-model__tot">Jami: 96 000 soʻm</p>
</div>

<p>Chizma bitta gʻoyani sovgʻa qiladi: Afsonaning tasmasidan
<b>ortiqcha 12 000 ni qirqib tashlasak</b>, ikkita bir xil tasma
qoladi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">96 000 − 12 000 = 84 000</span>
    <span class="pm-solve__why">Ortiqchani jamidan olib tashladik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">84 000 ÷ 2 = 42 000</span>
    <span class="pm-solve__why">Qolgani ikkita teng tasma</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Bekzod 42 000, Afsona 54 000</span>
    <span class="pm-solve__why">42 000 ga ortiqcha 12 000 ni qaytardik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>42 000 + 54 000 = 96 000 ✓ va 54 000 − 42 000 = 12 000 ✓
  <br><b>Javob:</b> Bekzod 42 000 soʻm, Afsona 54 000 soʻm yigʻdi.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Tenglama bilan ham xuddi shunday</p>
  <p>x + (x + 12 000) = 96 000 → 2x = 84 000 → x = 42 000. Chizma
  tenglamaning oʻrnini bosmaydi — u tenglamani <b>topib beradi</b>.
  Qaysi biri qulay boʻlsa, oʻshanisini yozing.</p>
</div>

<h3>3. Kesma chizma — yoʻlni boʻlaklarga ajratish</h3>

<p><b>Masala.</b> Sherbek bir shahardan boshqasiga bordi. Yoʻlning
uchdan bir qismini avtobusda, qolganini poyezdda bosdi. Poyezdda
avtobusdagidan 100 km koʻp yurdi. Jami yoʻl necha kilometr?</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 130" role="img" aria-label="Yoʻl uch teng boʻlakka ajratilgan: bir boʻlagi avtobusda, ikkitasi poyezdda">
    <rect class="pm-fill" x="30" y="38" width="86.7" height="28"/>
    <rect class="pm-fill pm-fill--hl" x="116.7" y="38" width="173.3" height="28"/>
    <polyline class="pm-ln" points="30,38 290,38 290,66 30,66 30,38" fill="none"/>
    <line class="pm-ln pm-ln--dash" x1="116.7" y1="38" x2="116.7" y2="66"/>
    <line class="pm-ln pm-ln--dash" x1="203.3" y1="38" x2="203.3" y2="66"/>
    <text class="pm-lbl" x="73" y="32" text-anchor="middle">avtobus</text>
    <text class="pm-lbl pm-lbl--hl" x="203" y="32" text-anchor="middle">poyezd</text>
    <line class="pm-ln pm-ln--hl" x1="203.3" y1="80" x2="290" y2="80"/>
    <text class="pm-lbl pm-lbl--hl" x="246" y="95" text-anchor="middle">farq = 100 km</text>
    <line class="pm-ln" x1="30" y1="110" x2="290" y2="110"/>
    <text class="pm-lbl" x="160" y="125" text-anchor="middle">jami yoʻl = ?</text>
  </svg>
  <figcaption>Yoʻl uchta teng boʻlakka boʻlingan. Poyezd ikkitasini,
  avtobus bittasini bosgan — demak farq ham roppa-rosa bitta
  boʻlak.</figcaption>
</figure>

<p>Chizmani koʻrgach masala tugadi. Avtobus — bitta boʻlak, poyezd —
ikkita boʻlak, ularning farqi esa <b>bitta boʻlak</b>. Demak bitta
boʻlak 100 km ekan.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">1 boʻlak = 100 km</span>
    <span class="pm-solve__why">Farq bitta boʻlakka teng</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3 boʻlak = 300 km</span>
    <span class="pm-solve__why">Butun yoʻl uchta boʻlakdan iborat</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Avtobus: 300 ÷ 3 = 100 km. Poyezd: 300 − 100 = 200 km. Farq:
  200 − 100 = 100 km ✓
  <br><b>Javob:</b> jami yoʻl 300 km.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">«Qolgani» degan soʻz</p>
  <p>Uchdan bir qism avtobusda boʻlsa, poyezdda <b>uchdan ikki</b>
  qism qoladi — uchdan bir emas. Bu eng koʻp uchraydigan xato:
  «qolgani» soʻzi butundan ayirishni talab qiladi, 1 −
  <sup>1</sup>/<sub>3</sub> = <sup>2</sup>/<sub>3</sub>.</p>
</div>

<h3>4. Oʻq sxemasi — bosqichma-bosqich oʻzgarish</h3>

<p><b>Masala.</b> Qutida bir nechta olma bor edi. Avval yarmi olindi,
keyin yana 6 tasi olindi va qutida 9 ta olma qoldi. Boshida nechta
olma bor edi?</p>

<p>Bunday masalada tasma yordam bermaydi — bu yerda <b>voqealar
ketma-ketligi</b> bor. Uni oʻq bilan yozamiz:</p>

<div class="pe-formula">
  <span class="pe-chip pe-chip--s">x</span>
  <span class="pe-op">→ yarmi olindi →</span>
  <span class="pe-chip pe-chip--o">x ÷ 2</span>
  <span class="pe-op">→ 6 ta olindi →</span>
  <span class="pe-chip pe-chip--v">9</span>
</div>

<p>Sxemaning oxirgi ikkita boʻgʻini tenglamani oʻzi yozib beradi:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x ÷ 2 − 6 = 9</span>
    <span class="pm-solve__why">Sxemaning oxiridan olindi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x ÷ 2 = 15</span>
    <span class="pm-solve__why">Ikki tomonga 6 ni qoʻshdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 30</span>
    <span class="pm-solve__why">Ikki tomonni 2 ga koʻpaytirdik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz — sxema boʻylab oldinga yuramiz</p>
  <p>30 → yarmi olindi → 15 → 6 tasi olindi → 9 ✓
  <br><b>Javob:</b> boshida 30 ta olma bor edi.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Sxema tekshirishni ham bepul beradi</p>
  <p>Javobni sxemaning boshiga qoʻyib, oʻqlar boʻylab oxirigacha
  yuring. Oxirida masaladagi son chiqsa, javob toʻgʻri. Bu — eng tez
  va eng ishonchli tekshirish usuli.</p>
</div>

<h3>Matnli masala</h3>

<p>Sinf kutubxonasida 180 ta kitob bor. Badiiy kitoblar darsliklardan
2 marta koʻp, lugʻatlar esa darsliklardan 20 ta kam.</p>

<p><b>Har bir turdan nechtadan bor?</b></p>

<p><b>Reja:</b> hamma narsa darsliklarga qarab aytilgan (PM-86), demak
x — darsliklar soni. Uchta miqdor bor — tasma model chizamiz.</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">Darslik</span>
    <span class="pm-model__bar" style="width:28%">x</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">Badiiy</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:56%">2x</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">Lugʻat</span>
    <span class="pm-model__bar" style="width:17%">x − 20</span>
  </div>
  <p class="pm-model__tot">Jami: x + 2x + (x − 20) = 180</p>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + 2x + x − 20 = 180</span>
    <span class="pm-solve__why">Qavsni ochdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4x − 20 = 180</span>
    <span class="pm-solve__why">Oʻxshash hadlar: x + 2x + x = 4x</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4x = 200</span>
    <span class="pm-solve__why">Ikki tomonga 20 ni qoʻshdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 50</span>
    <span class="pm-solve__why">4 ga boʻldik</span>
  </div>
</div>

<p>Darsliklar 50 ta, badiiy kitoblar 2 × 50 = 100 ta, lugʻatlar
50 − 20 = 30 ta.</p>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>50 + 100 + 30 = 180 ✓ Badiiy darslikdan 2 marta koʻp:
  100 ÷ 50 = 2 ✓ Lugʻat darslikdan 20 ta kam: 50 − 30 = 20 ✓
  <br><b>Javob:</b> 50 ta darslik, 100 ta badiiy kitob, 30 ta
  lugʻat.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Agar lugʻatlar ham darsliklarcha boʻlganda, jami toʻrtta teng
  boʻlak — 180 dan sal koʻproq. Demak bitta boʻlak 45–50 atrofida.
  Javob 50 chiqdi — mantiqiy.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">x va 2x tasmalari bir xil uzunlikda chizilgan</p>
  <p class="pe-fix__good">2x tasmasi roppa-rosa ikki barobar uzun</p>
  <p class="pe-fix__why">Chizmaning butun kuchi nisbatni koʻrsatishida.
  Nisbatsiz chizma xato javobni ham «toʻgʻri» qilib koʻrsatadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Yoʻlning <sup>1</sup>/<sub>3</sub> qismi
  avtobusda → qolgani ham <sup>1</sup>/<sub>3</sub></p>
  <p class="pe-fix__good">Qolgani <sup>2</sup>/<sub>3</sub></p>
  <p class="pe-fix__why">Butun 1 ga teng: 1 − <sup>1</sup>/<sub>3</sub>
  = <sup>2</sup>/<sub>3</sub>. Chizmada uchta boʻlakdan ikkitasi
  qolgani darrov koʻrinadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">96 000 ÷ 2 = 48 000, demak har biri 48 000</p>
  <p class="pe-fix__good">(96 000 − 12 000) ÷ 2 = 42 000</p>
  <p class="pe-fix__why">Teng boʻlish 12 000 lik farqni yoʻqotadi.
  Avval ortiqcha qirqiladi, keyin qolgani teng boʻlinadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Tasmalar chizilgan, lekin jami qayerdaligi
  yozilmagan</p>
  <p class="pe-fix__good">Tasmalar yonida «Jami: 96 000» turibdi</p>
  <p class="pe-fix__why">Chizmada har bir son oʻz oʻrnida boʻlishi
  kerak. Yozuvsiz chizma bir necha daqiqadan keyin oʻzingizga ham
  tushunarsiz boʻlib qoladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Ikki son yigʻindisi 70, farqi 10. Chizma
  chizib, sonlarni toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>30 va 40.</b> Ortiqchani qirqamiz: (70 − 10) ÷ 2 = 30 —
    kichigi. Kattasi 30 + 10 = 40. Tekshirish: 30 + 40 = 70 ✓,
    40 − 30 = 10 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Bogʻning beshdan bir qismiga olma, qolganiga
  oʻrik ekilgan. Oʻrik olmadan qancha koʻp qismni egallagan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Uchdan besh qism koʻp.</b> Olma —
    <sup>1</sup>/<sub>5</sub>, oʻrik — <sup>4</sup>/<sub>5</sub>.
    Farq: <sup>4</sup>/<sub>5</sub> − <sup>1</sup>/<sub>5</sub> =
    <sup>3</sup>/<sub>5</sub>. Chizmada beshta boʻlakdan uchtasi
    ortiqcha.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Bir sonni 3 ga koʻpaytirib, 8 ni qoʻshsak,
  35 chiqadi. Oʻq sxemasi tuzib, sonni toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>9.</b> Sxema: x → ×3 → 3x → +8 → 35. Demak 3x + 8 = 35 →
    3x = 27 → x = 9. Tekshirish: 9 × 3 = 27, 27 + 8 = 35 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Ikki qutida jami 48 ta ruchka. Birinchi
  qutida ikkinchisidan 3 marta koʻp. Chizma chizib, har birini
  toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>12 va 36.</b> Chizmada jami toʻrtta teng boʻlak (1 + 3):
    48 ÷ 4 = 12 — ikkinchi quti. Birinchisi 3 × 12 = 36. Tekshirish:
    12 + 36 = 48 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Dilnozada bir necha marka bor edi. U
  ularning yarmini singlisiga berdi, keyin 4 tasini yoʻqotdi va 11 tasi
  qoldi. Boshida nechta marka bor edi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>30 ta.</b> Sxema: x → yarmi berildi → x ÷ 2 → 4 tasi
    yoʻqoldi → 11. Demak x ÷ 2 − 4 = 11 → x ÷ 2 = 15 → x = 30.
    Tekshirish: 30 → 15 → 11 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Yoʻlning toʻrtdan bir qismi asfalt, qolgani
  tuproq yoʻl. Tuproq yoʻl asfaltdan 60 km uzun. Jami yoʻl necha
  km?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>120 km.</b> Asfalt — 1 boʻlak, tuproq — 3 boʻlak, farq —
    2 boʻlak. Demak 2 boʻlak = 60 km, 1 boʻlak = 30 km, jami 4 boʻlak
    = 120 km. Tekshirish: asfalt 30, tuproq 90, farq 60 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">7. Uch doʻst 155 ta yongʻoq terishdi. Jasur
  Afsonadan 2 marta koʻp, Sherbek Afsonadan 5 ta kam terdi. Har biri
  nechtadan terdi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Afsona 40, Jasur 80, Sherbek 35.</b> Hamma narsa Afsonaga
    qarab aytilgan, demak x — Afsona tergani. Chizmada toʻrtta boʻlak
    va bittasidan qirqilgan 5 ta koʻrinadi:
    x + 2x + (x − 5) = 155 → 4x − 5 = 155 → 4x = 160 → x = 40.
    Tekshirish: 40 + 80 + 35 = 155 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Chizma</b><span>masaladagi miqdorlarning rasm koʻrinishi;
    ingl. diagram</span></li>
  <li><b>Tasma model</b><span>miqdorlarni toʻgʻri toʻrtburchaklar bilan
    koʻrsatish; ingl. bar model</span></li>
  <li><b>Kesma chizma</b><span>uzunlik yoki yoʻlni boʻlaklarga ajratish;
    ingl. line diagram</span></li>
  <li><b>Sxema</b><span>bosqichlarni oʻq bilan bogʻlangan yozuvi; ingl.
    flow diagram</span></li>
  <li><b>Boʻlak</b><span>chizmaning teng qismlaridan biri; ingl.
    unit</span></li>
  <li><b>Butun</b><span>hamma boʻlaklarning yigʻindisi; ingl.
    whole</span></li>
  <li><b>Nisbat</b><span>miqdorlarning bir-biriga solishtirilishi; ingl.
    ratio</span></li>
  <li><b>Ortiqcha</b><span>tasmaning tenglikdan oshgan qismi; ingl.
    excess</span></li>
  <li><b>Bosqich</b><span>sxemadagi bitta oʻzgarish qadami; ingl.
    step</span></li>
  <li><b>Miqyos</b><span>chizmada uzunlik nisbatga mos boʻlishi; ingl.
    scale</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Butun va boʻlaklar — tasma model; yoʻl va uzunlik — kesma
      chizma; bosqichli oʻzgarish — oʻq sxemasi.</li>
    <li>Chizmadagi uzunlik nisbatga mos boʻlishi shart.</li>
    <li>«Ortiqchani qirqish»: jamidan farqni ayirib, qolganini teng
      boʻling.</li>
    <li>«Qolgani» — butundan ayirish: 1 − <sup>1</sup>/<sub>3</sub> =
      <sup>2</sup>/<sub>3</sub>.</li>
    <li>Sxema boʻylab oldinga yurish — eng tez tekshirish usuli.</li>
    <li>Chizma tenglamaning oʻrnini bosmaydi, uni topib beradi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-88 — harakat masalalari 1
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-88: Harakat masalalari 1: tezlik, vaqt, masofa",
        "category": "math",
        "order": 88,
        "summary": (
            "S = v · t va uning ikki burilishi. Eng koʻp xato formulada "
            "emas, birliklarda: 30 minut — 0,5 soat. Oʻrtacha tezlik esa "
            "tezliklarning oʻrtachasi emas."
        ),
        "stories": ["Maktabga velosipedda"],
        "content": """
<h2>PM-88: Harakat masalalari 1: tezlik, vaqt, masofa</h2>

<p>«Velosipedda 12 km/soat bilan 45 minut yurdim. Qancha yoʻl
bosdim?»</p>

<p>Koʻpchilik 12 × 45 = 540 deb yozadi va 540 km chiqadi — Toshkentdan
Nukusgacha. Formulada xato yoʻq. Xato <b>birlikda</b>: tezlik soatda,
vaqt esa minutda berilgan.</p>

<p>Harakat masalalarida formulalar oson, birliklar esa shafqatsiz. Shu
darsda ikkalasini ham joyiga qoʻyamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>bitta formuladan uchtasini chiqarasiz;</li>
    <li>minutni soatga, km/soatni m/s ga oʻgirasiz;</li>
    <li>koʻp boʻlakli yoʻlni jadval bilan yechasiz;</li>
    <li>oʻrtacha tezlikni toʻgʻri hisoblaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Harakat uchligi</span>
  <span class="pe-chip pe-chip--s">S</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">v</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--o">t</span>
</div>

<h3>1. Bitta formula, uchta savol</h3>

<p>PM-35 da S = v · t formulasi bilan tanishgan edingiz. Uni qayta
yodlashning hojati yoʻq — tenglamani yechish qoidasi (PM-36) qolgan
ikkitasini oʻzi beradi.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Nima soʻralgan</th><th>Formula</th><th>Misol</th></tr>
  <tr><td>Masofa</td><td class="pm-word__sym">S = v × t</td>
    <td>60 × 2,5 = 150 km</td></tr>
  <tr><td>Tezlik</td><td class="pm-word__sym">v = S ÷ t</td>
    <td>240 ÷ 3 = 80 km/soat</td></tr>
  <tr><td>Vaqt</td><td class="pm-word__sym">t = S ÷ v</td>
    <td>18 ÷ 12 = 1,5 soat</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__math">S = 60 × 2,5 = 150 km</p>
  <p class="pe-ex__uz">Soatiga 60 km yurgan mashina 2,5 soatda 150 km
  bosadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">v = 240 ÷ 3 = 80 km/soat</p>
  <p class="pe-ex__uz">240 kilometrni 3 soatda bosgan boʻlsa, har
  soatda 80 km yurgan.</p>
  <p class="pe-ex__why">Tezlik — bir soatga toʻgʻri keladigan masofa.
  Shuning uchun masofa vaqtga boʻlinadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">t = 18 ÷ 12 = 1,5 soat</p>
  <p class="pe-ex__uz">18 kilometrni soatiga 12 km tezlik bilan
  1 soat 30 minutda bosadi.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Formulani unutsangiz, birlikka qarang</p>
  <p>Tezlik <b>km/soat</b> deb oʻqiladi — «kilometr <b>boʻlingan</b>
  soat». Birlikning oʻzi formulani aytib turibdi: v = S ÷ t. Qolgan
  ikkitasi shundan chiqadi.</p>
</div>

<h3>2. Birliklar — asosiy xato shu yerda</h3>

<p>Formulaga qoʻyishdan oldin tezlik va vaqt <b>bir xil birlikda</b>
boʻlishi shart. Soatga oʻgirish jadvali:</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Vaqt</th><th>Soatda</th><th>Nega</th></tr>
  <tr><td>15 minut</td><td class="pm-word__sym">0,25 soat</td><td>15 ÷ 60</td></tr>
  <tr><td>20 minut</td><td class="pm-word__sym">1/3 soat</td><td>20 ÷ 60</td></tr>
  <tr><td>30 minut</td><td class="pm-word__sym">0,5 soat</td><td>30 ÷ 60</td></tr>
  <tr><td>45 minut</td><td class="pm-word__sym">0,75 soat</td><td>45 ÷ 60</td></tr>
  <tr><td>1 soat 30 minut</td><td class="pm-word__sym">1,5 soat</td><td>60 + 30 = 90; 90 ÷ 60</td></tr>
</table></div>

<p>Endi boshidagi masala toʻgʻri yechiladi:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">45 minut = 45 ÷ 60 = 0,75 soat</span>
    <span class="pm-solve__why">Tezlik soatda berilgan — vaqt ham soatda boʻlsin</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">S = 12 × 0,75 = 9 km</span>
    <span class="pm-solve__why">Endi ikkalasi ham soat birligida</span>
  </div>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>45 minut — bir soatdan sal kam. Soatiga 12 km yursa, javob
  12 dan sal kam boʻlishi kerak. 9 km — mantiqiy. 540 km esa darrov
  koʻzga tashlanadigan bemaʼnilik edi.</span>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">km/soat va m/s</p>
  <p>Bir soat — 3600 sekund, bir kilometr — 1000 metr. Shuning uchun
  km/soatdan m/s ga oʻtish uchun <b>3,6 ga boʻlinadi</b>:
  <br>36 km/soat = 36 ÷ 3,6 = 10 m/s.
  <br>Teskarisiga — 3,6 ga koʻpaytiriladi: 5 m/s = 18 km/soat.</p>
</div>

<h3>3. Koʻp boʻlakli yoʻl — jadval bilan</h3>

<p>Yoʻl bir necha boʻlakdan iborat boʻlsa, PM-86 dagi jadval yana
ishga tushadi: har bir boʻlak — bitta qator.</p>

<p><b>Masala.</b> Mashina 2 soat davomida 80 km/soat bilan, keyin
1,5 soat davomida 60 km/soat bilan yurdi. Jami qancha yoʻl bosdi?</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Boʻlak</th><th>v × t</th><th>Masofa</th></tr>
  <tr><td>Birinchi</td><td class="pm-word__sym">80 × 2</td><td>160 km</td></tr>
  <tr><td>Ikkinchi</td><td class="pm-word__sym">60 × 1,5</td><td>90 km</td></tr>
  <tr><td>Jami</td><td class="pm-word__sym">160 + 90</td><td>250 km</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Masofalar qoʻshiladi, tezliklar — yoʻq</p>
  <p>Jadvalning oxirgi ustunini qoʻshish mumkin. Oʻrtadagi ustunni
  qoʻshib boʻlmaydi: 80 + 60 = 140 km/soat degan tezlik bu safarda
  hech qachon boʻlmagan.</p>
</div>

<h3>4. Oʻrtacha tezlik</h3>

<div class="pe-formula">
  <span class="pe-formula__label">Oʻrtacha tezlik</span>
  <span class="pe-chip pe-chip--s">v<sub>oʻrt</sub></span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">jami masofa</span>
  <span class="pe-op">÷</span>
  <span class="pe-chip pe-chip--o">jami vaqt</span>
</div>

<p><b>Masala.</b> Bekzod uyidan bogʻgacha 60 km yoʻlni 60 km/soat
bilan bordi, qaytishda esa oʻsha 60 km ni 30 km/soat bilan bosdi.
Butun safar davomida oʻrtacha tezligi qancha?</p>

<p>Koʻpchilik darrov (60 + 30) ÷ 2 = 45 deb javob beradi. Bu
<b>notoʻgʻri</b>.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Borish: t = 60 ÷ 60 = 1 soat</span>
    <span class="pm-solve__why">t = S ÷ v</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Qaytish: t = 60 ÷ 30 = 2 soat</span>
    <span class="pm-solve__why">Sekinroq — demak uzoqroq vaqt</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Jami: 120 km, 3 soat</span>
    <span class="pm-solve__why">Masofalar va vaqtlar qoʻshildi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">v<sub>oʻrt</sub> = 120 ÷ 3 = 40 km/soat</span>
    <span class="pm-solve__why">45 emas, 40</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Nega 45 emas?</p>
  <p>Chunki sekin tezlikda <b>koʻproq vaqt</b> oʻtkazilgan — 2 soat,
  tez tezlikda esa atigi 1 soat. Oʻrtacha tezlik vaqtga qarab
  ogʻadi, shuning uchun u har doim sekinroq tomonga tortiladi. Ikki
  tezlikning oddiy oʻrtachasini olish faqat <b>vaqtlar teng</b>
  boʻlgandagina toʻgʻri boʻladi.</p>
</div>

<h3>Matnli masala</h3>

<p>Bekzod ertalab velosipedda yoʻlga chiqdi. Avval 12 km/soat tezlik
bilan 1 soat yurdi. Keyin 30 minut dam oldi. Soʻng 8 km/soat bilan
yana 30 minut yurdi.</p>

<p><b>Jami qancha yoʻl bosdi va butun safar davomida oʻrtacha tezligi
qancha boʻldi?</b></p>

<p><b>Reja:</b> har bir boʻlakni jadvalga solamiz. Dam olish
masofaga hech narsa qoʻshmaydi, lekin <b>vaqtga qoʻshiladi</b> —
chunki savol butun safar haqida.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Boʻlak</th><th>Masofa</th><th>Vaqt</th></tr>
  <tr><td>Birinchi yurish</td><td class="pm-word__sym">12 × 1 = 12 km</td><td>1 soat</td></tr>
  <tr><td>Dam olish</td><td class="pm-word__sym">0 km</td><td>0,5 soat</td></tr>
  <tr><td>Ikkinchi yurish</td><td class="pm-word__sym">8 × 0,5 = 4 km</td><td>0,5 soat</td></tr>
  <tr><td>Jami</td><td class="pm-word__sym">16 km</td><td>2 soat</td></tr>
</table></div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">S = 12 × 1 + 8 × 0,5 = 12 + 4 = 16 km</span>
    <span class="pm-solve__why">Ikki yurish boʻlagining masofasi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">t = 1 + 0,5 + 0,5 = 2 soat</span>
    <span class="pm-solve__why">Dam olish ham safar vaqtiga kiradi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">v<sub>oʻrt</sub> = 16 ÷ 2 = 8 km/soat</span>
    <span class="pm-solve__why">Jami masofa ÷ jami vaqt</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Agar Bekzod butun 2 soat davomida 8 km/soat bilan tekis yurganda,
  8 × 2 = 16 km bosardi — xuddi shuncha ✓ Oʻrtacha tezlikning maʼnosi
  ham aynan shu.
  <br><b>Javob:</b> 16 km yoʻl, oʻrtacha tezlik 8 km/soat.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Savolni diqqat bilan oʻqing</p>
  <p>«Butun safar davomida» deyilsa, dam olish vaqti ham hisobga
  olinadi. «Harakat davomida» deyilsa esa faqat 1,5 soat olinardi va
  javob 16 ÷ 1,5 ≈ 10,7 km/soat boʻlardi. Bitta soʻz javobni
  oʻzgartiradi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">12 km/soat × 45 minut = 540 km</p>
  <p class="pe-fix__good">12 × 0,75 = 9 km</p>
  <p class="pe-fix__why">Tezlik soatda, vaqt minutda olingan. Avval
  45 minut = 0,75 soat qilinadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">1 soat 30 minut = 1,30 soat</p>
  <p class="pe-fix__good">1 soat 30 minut = 1,5 soat</p>
  <p class="pe-fix__why">Vaqt oʻnlik sanoqda emas: soatda 100 emas,
  <b>60</b> minut bor. 30 ÷ 60 = 0,5.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">60 km/soat va 30 km/soat → oʻrtacha
  (60 + 30) ÷ 2 = 45</p>
  <p class="pe-fix__good">120 ÷ 3 = 40 km/soat</p>
  <p class="pe-fix__why">Sekin boʻlakda koʻproq vaqt oʻtgan. Oʻrtacha
  tezlik — jami masofa ÷ jami vaqt, tezliklarning oʻrtachasi emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Ikki boʻlakda 80 va 60 km/soat → tezlik
  140 km/soat</p>
  <p class="pe-fix__good">Masofalar qoʻshiladi: 160 + 90 = 250 km</p>
  <p class="pe-fix__why">Tezliklar qoʻshilmaydi. Bitta jismning
  tezligi boʻlaklarda alohida-alohida boʻladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Mashina 70 km/soat bilan 3 soat yurdi.
  Qancha yoʻl bosdi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>210 km.</b> S = v × t = 70 × 3 = 210.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Piyoda 12 km yoʻlni 3 soatda bosdi. Tezligi
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>4 km/soat.</b> v = S ÷ t = 12 ÷ 3 = 4 km/soat — odatdagi
    piyoda tezligi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 150 km yoʻlni 50 km/soat bilan bosishga
  qancha vaqt ketadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3 soat.</b> t = S ÷ v = 150 ÷ 50 = 3.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Velosipedchi 16 km/soat bilan 45 minut
  yurdi. Qancha yoʻl bosdi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>12 km.</b> 45 minut = 0,75 soat. S = 16 × 0,75 = 12 km.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. 54 km/soat necha m/s ga teng?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>15 m/s.</b> 54 ÷ 3,6 = 15. Tekshirish: 15 m/s × 3600 s =
    54 000 m = 54 km ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Poyezd 2 soat 100 km/soat bilan, keyin
  3 soat 80 km/soat bilan yurdi. Oʻrtacha tezligi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>88 km/soat.</b> Masofa: 200 + 240 = 440 km. Vaqt: 5 soat.
    440 ÷ 5 = 88. Diqqat: (100 + 80) ÷ 2 = 90 emas — uzoqroq vaqt
    sekinroq tezlikda oʻtgan.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">7. Afsona maktabgacha 1,8 km yoʻlni 24 minutda
  piyoda bosadi. Tezligi necha km/soat?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>4,5 km/soat.</b> 24 minut = 24 ÷ 60 = 0,4 soat.
    v = 1,8 ÷ 0,4 = 4,5 km/soat. Tekshirish: 4,5 × 0,4 = 1,8 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Tezlik</b><span>bir vaqt birligida bosilgan masofa; ingl.
    speed</span></li>
  <li><b>Masofa</b><span>bosib oʻtilgan yoʻl uzunligi; ingl.
    distance</span></li>
  <li><b>Vaqt</b><span>harakat davom etgan muddat; ingl. time</span></li>
  <li><b>Oʻrtacha tezlik</b><span>jami masofa ÷ jami vaqt; ingl. average
    speed</span></li>
  <li><b>Birlik</b><span>oʻlchov nomi: km, soat, m/s; ingl.
    unit</span></li>
  <li><b>km/soat</b><span>bir soatda bosiladigan kilometrlar; ingl.
    km per hour</span></li>
  <li><b>Tekis harakat</b><span>tezligi oʻzgarmaydigan harakat; ingl.
    uniform motion</span></li>
  <li><b>Boʻlak</b><span>yoʻlning bir xil tezlikdagi qismi; ingl.
    stage</span></li>
  <li><b>Dam olish</b><span>masofaga emas, faqat vaqtga qoʻshiladigan
    tanaffus; ingl. rest</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>S = v × t; v = S ÷ t; t = S ÷ v — bitta formulaning uch
      qiyofasi.</li>
    <li>Formulaga qoʻyishdan oldin birliklarni moslang.</li>
    <li>1 soat 30 minut = 1,5 soat, 1,30 emas.</li>
    <li>km/soatdan m/s ga — 3,6 ga boʻlinadi.</li>
    <li>Koʻp boʻlakli yoʻl — jadval; masofalar qoʻshiladi, tezliklar
      qoʻshilmaydi.</li>
    <li>Oʻrtacha tezlik = jami masofa ÷ jami vaqt, hech qachon
      tezliklarning oʻrtachasi emas.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-89 — harakat masalalari 2
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-89: Harakat masalalari 2: uchrashuv va quvish",
        "category": "math",
        "order": 89,
        "summary": (
            "Ikki jism harakatlanganda muhimi ularning tezligi emas, "
            "orasidagi masofa qanchalik tez kamayishi. Qarshi yursa "
            "tezliklar qoʻshiladi, quvsa — ayiriladi."
        ),
        "stories": ["Ikki avtobus, bitta yoʻl"],
        "content": """
<h2>PM-89: Harakat masalalari 2: uchrashuv va quvish</h2>

<p>Ikki avtobus bir-biriga qarab kelyapti. Biri 60, ikkinchisi
40 km/soat. Ular orasidagi masofa har soatda qancha kamayadi?</p>

<p>Har soatda birinchisi 60 km, ikkinchisi 40 km yaqinlashadi. Demak
oradagi masofa soatiga <b>100 km</b> ga qisqaradi. Mana shu son — butun
darsning kaliti.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>yaqinlashish tezligini topasiz (v₁ + v₂);</li>
    <li>quvish masalasida farq tezligini qoʻllaysiz (v₁ − v₂);</li>
    <li>bir vaqtda chiqmagan harakatni sxema bilan yechasiz;</li>
    <li>uchrashuv joyini ham, vaqtini ham hisoblaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qarama-qarshi harakat</span>
  <span class="pe-chip pe-chip--s">t</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">oradagi masofa</span>
  <span class="pe-op">÷</span>
  <span class="pe-chip pe-chip--v">v₁ + v₂</span>
</div>

<h3>1. Uchrashuv — tezliklar qoʻshiladi</h3>

<p><b>Masala.</b> Ikki shahar orasi 300 km. Ulardan bir vaqtda
bir-biriga qarab ikkita mashina chiqdi: biri 60 km/soat, ikkinchisi
40 km/soat. Necha soatdan keyin uchrashadi?</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 130" role="img" aria-label="Ikki mashina bir-biriga qarab harakatlanmoqda, oralari 300 km">
    <line class="pm-ln" x1="30" y1="70" x2="290" y2="70"/>
    <circle class="pm-pt" cx="30" cy="70" r="4"/>
    <circle class="pm-pt" cx="290" cy="70" r="4"/>
    <text class="pm-lbl" x="30" y="90" text-anchor="middle">A</text>
    <text class="pm-lbl" x="290" y="90" text-anchor="middle">B</text>
    <line class="pm-ln pm-ln--hl" x1="40" y1="52" x2="110" y2="52"/>
    <polyline class="pm-ln pm-ln--hl" points="102,48 110,52 102,56" fill="none"/>
    <text class="pm-lbl pm-lbl--hl" x="75" y="42" text-anchor="middle">60 km/soat</text>
    <line class="pm-ln pm-ln--hl" x1="280" y1="52" x2="210" y2="52"/>
    <polyline class="pm-ln pm-ln--hl" points="218,48 210,52 218,56" fill="none"/>
    <text class="pm-lbl pm-lbl--hl" x="245" y="42" text-anchor="middle">40 km/soat</text>
    <line class="pm-ln pm-ln--dash" x1="186" y1="60" x2="186" y2="100"/>
    <text class="pm-lbl" x="186" y="112" text-anchor="middle">uchrashuv</text>
    <text class="pm-lbl" x="160" y="24" text-anchor="middle">300 km</text>
  </svg>
  <figcaption>Har soatda oradagi masofa 60 + 40 = 100 km ga kamayadi.
  Uchrashuv joyi oʻrtada emas — tez mashina koʻproq yoʻl bosadi.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Yaqinlashish tezligi: 60 + 40 = 100 km/soat</span>
    <span class="pm-solve__why">Har soatda ora shuncha qisqaradi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">t = 300 ÷ 100 = 3 soat</span>
    <span class="pm-solve__why">Butun ora shu tezlikda yopiladi</span>
  </div>
</div>

<p>Uchrashuv joyini ham topamiz: birinchi mashina 60 × 3 = 180 km,
ikkinchisi 40 × 3 = 120 km yurgan.</p>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>180 + 120 = 300 ✓ — ikkalasi birgalikda butun yoʻlni bosgan.
  <br><b>Javob:</b> 3 soatdan keyin, A shahardan 180 km narida
  uchrashadi.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Uchrashuv joyi oʻrtada emas</p>
  <p>Vaqt ikkalasi uchun bir xil — ular bir vaqtda chiqib, bir vaqtda
  uchrashdi. Masofa esa har xil: tez yurgan koʻproq bosadi. «Uchrashuv
  yoʻlning oʻrtasida boʻladi» degan fikr faqat tezliklar
  <b>teng</b> boʻlgandagina toʻgʻri.</p>
</div>

<h3>2. Quvish — tezliklar ayiriladi</h3>

<div class="pe-formula">
  <span class="pe-formula__label">Bir yoʻnalishdagi harakat</span>
  <span class="pe-chip pe-chip--s">t</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">oradagi masofa</span>
  <span class="pe-op">÷</span>
  <span class="pe-chip pe-chip--v">v₁ − v₂</span>
</div>

<p><b>Masala.</b> Bekzod uydan piyoda chiqdi va 5 km/soat bilan ketdi.
2 soatdan keyin Jasur velosipedda oʻsha yoʻldan 15 km/soat bilan uning
ortidan chiqdi. Jasur Bekzodni necha soatdan keyin quvib yetadi?</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 155" role="img" aria-label="Jasur Bekzodni quvmoqda, oralari 10 km">
    <line class="pm-ln" x1="20" y1="70" x2="300" y2="70"/>
    <circle class="pm-pt" cx="40" cy="70" r="4"/>
    <circle class="pm-pt" cx="140" cy="70" r="4"/>
    <line class="pm-ln pm-ln--hl" x1="140" y1="50" x2="210" y2="50"/>
    <polyline class="pm-ln pm-ln--hl" points="202,46 210,50 202,54" fill="none"/>
    <text class="pm-lbl" x="175" y="40" text-anchor="middle">Bekzod 5 km/soat</text>
    <line class="pm-ln pm-ln--dash" x1="40" y1="70" x2="40" y2="92"/>
    <line class="pm-ln pm-ln--dash" x1="140" y1="70" x2="140" y2="92"/>
    <line class="pm-ln pm-ln--hl" x1="40" y1="92" x2="140" y2="92"/>
    <text class="pm-lbl pm-lbl--hl" x="90" y="108" text-anchor="middle">10 km oldinda</text>
    <line class="pm-ln pm-ln--hl" x1="40" y1="126" x2="110" y2="126"/>
    <polyline class="pm-ln pm-ln--hl" points="102,122 110,126 102,130" fill="none"/>
    <text class="pm-lbl pm-lbl--hl" x="75" y="145" text-anchor="middle">Jasur 15 km/soat</text>
  </svg>
  <figcaption>Jasur yoʻlga chiqqan payt Bekzod allaqachon 10 km
  narida. Har soatda bu ora 10 km ga kamayadi.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Bekzodning boshlangʻich ustunligi: 5 × 2 = 10 km</span>
    <span class="pm-solve__why">Jasur chiqquncha 2 soat yurgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Farq tezligi: 15 − 5 = 10 km/soat</span>
    <span class="pm-solve__why">Jasur har soatda 10 km yaqinlashadi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">t = 10 ÷ 10 = 1 soat</span>
    <span class="pm-solve__why">Ora shu tezlikda yopiladi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Jasur chiqqanidan 1 soat oʻtdi. Bekzod jami 3 soat yurgan:
  5 × 3 = 15 km. Jasur 1 soat yurgan: 15 × 1 = 15 km. Ikkalasi ham
  uydan 15 km narida ✓
  <br><b>Javob:</b> Jasur 1 soatdan keyin, uydan 15 km narida quvib
  yetadi.</p>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Ayirish tartibi</p>
  <p>Farq tezligi <b>quvuvchining tezligidan qochuvchiniki
  ayiriladi</b>: 15 − 5. Teskarisi manfiy chiqadi va bu shuni
  bildiradiki, quvuvchi sekinroq — u hech qachon yetib ololmaydi.
  Javob manfiy chiqsa, masalani qayta oʻqing.</p>
</div>

<h3>3. Ikkisini yonma-yon qoʻyamiz</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Qarama-qarshi</p>
    <p>Ora <b>kamayadi</b> soatiga v₁ + v₂ ga.
    <br>t = ora ÷ (v₁ + v₂)</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Bir yoʻnalishda</p>
    <p>Ora <b>kamayadi</b> soatiga v₁ − v₂ ga.
    <br>t = ora ÷ (v₁ − v₂)</p>
  </div>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Bitta savol ikkalasini hal qiladi</p>
  <p>Formulani yodlashning oʻrniga shu savolni bering: <b>ora har
  soatda qanchaga kamayadi?</b> Qarshi yursa qoʻshiladi, birga ketsa
  ayiriladi. Keyin masofani shu songa boʻlasiz — vaqt chiqadi.</p>
</div>

<h3>Matnli masala</h3>

<p>A va B shaharlari orasi 530 km. Soat 08:00 da A dan poyezd chiqdi
va 80 km/soat bilan B tomonga yoʻl oldi. Soat 09:00 da B dan qarshi
poyezd chiqdi va 70 km/soat bilan yurdi.</p>

<p><b>Ular soat nechada uchrashadi?</b></p>

<p><b>Reja:</b> poyezdlar bir vaqtda chiqmagan, demak avval 09:00
holatini aniqlaymiz. Shu paytdan boshlab masala oddiy uchrashuvga
aylanadi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">08:00 → 09:00: birinchi poyezd 80 × 1 = 80 km yurdi</span>
    <span class="pm-solve__why">Bir soat yolgʻiz harakatlandi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">09:00 dagi ora: 530 − 80 = 450 km</span>
    <span class="pm-solve__why">Endi ikkalasi ham yoʻlda</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Yaqinlashish tezligi: 80 + 70 = 150 km/soat</span>
    <span class="pm-solve__why">Qarama-qarshi harakat</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">t = 450 ÷ 150 = 3 soat</span>
    <span class="pm-solve__why">09:00 dan boshlab</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">09:00 + 3 soat = 12:00</span>
    <span class="pm-solve__why">Savol vaqtni soʻragan edi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Birinchi poyezd 08:00 dan 12:00 gacha 4 soat yurgan:
  80 × 4 = 320 km. Ikkinchisi 09:00 dan 12:00 gacha 3 soat:
  70 × 3 = 210 km. Jami 320 + 210 = 530 km ✓ — roppa-rosa shaharlar
  orasidagi masofa.
  <br><b>Javob:</b> poyezdlar soat 12:00 da uchrashadi.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Bir vaqtda chiqmagan boʻlsa</p>
  <p>Har doim <b>ikkinchisi yoʻlga chiqqan paytga</b> oʻting: oradan
  birinchisi bosgan yoʻlni ayiring. Shundan keyin masala oddiy
  uchrashuvga aylanadi. Javobni esa oʻsha paytga qoʻshib yozing —
  09:00 + 3 soat.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">300 km, tezliklar 60 va 40 → t = 300 ÷ 60 = 5
  soat</p>
  <p class="pe-fix__good">t = 300 ÷ (60 + 40) = 3 soat</p>
  <p class="pe-fix__why">Faqat bitta tezlik olingan. Ora ikkala
  mashina hisobiga kamayadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Quvishda: t = 10 ÷ (15 + 5) = 0,5 soat</p>
  <p class="pe-fix__good">t = 10 ÷ (15 − 5) = 1 soat</p>
  <p class="pe-fix__why">Bir yoʻnalishda ketishayotgan boʻlsa,
  tezliklar <b>ayiriladi</b>: qochuvchi ham oldinga siljib boradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Uchrashuv yoʻlning oʻrtasida — 150 km da</p>
  <p class="pe-fix__good">A dan 180 km, B dan 120 km narida</p>
  <p class="pe-fix__why">Vaqt teng, masofa esa tezlikka mutanosib.
  Oʻrtada uchrashish faqat tezliklar teng boʻlganda.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">09:00 da chiqqan poyezd uchun ham 530 km
  olinadi</p>
  <p class="pe-fix__good">09:00 dagi ora — 450 km</p>
  <p class="pe-fix__why">Birinchi poyezd bir soat davomida 80 km yurib
  boʻlgan. Bir vaqtda chiqmagan masalada avval shu «boshlangʻich
  ustunlik» hisoblanadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Ikki qishloq orasi 24 km. Ikki piyoda
  bir-biriga qarab chiqdi: 5 va 3 km/soat. Necha soatdan keyin
  uchrashadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3 soat.</b> Yaqinlashish tezligi 5 + 3 = 8 km/soat.
    t = 24 ÷ 8 = 3. Tekshirish: 15 + 9 = 24 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Oldingi masalada har biri qancha yoʻl
  bosgan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>15 km va 9 km.</b> 5 × 3 = 15 va 3 × 3 = 9. Tez yurgan
    koʻproq bosgan — uchrashuv oʻrtada emas.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Ikki shahar orasi 480 km. Ikki poyezd
  qarshi chiqib, 4 soatda uchrashdi. Biri 70 km/soat bilan yurgan.
  Ikkinchisining tezligi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>50 km/soat.</b> Yaqinlashish tezligi 480 ÷ 4 = 120 km/soat.
    Demak 120 − 70 = 50. Tekshirish: 280 + 200 = 480 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Mashina 40 km/soat bilan ketmoqda. Uning
  ortidan 20 km naridan 60 km/soat bilan ikkinchi mashina chiqdi.
  Qachon quvib yetadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>1 soatdan keyin.</b> Farq tezligi 60 − 40 = 20 km/soat.
    t = 20 ÷ 20 = 1 soat. Tekshirish: birinchisi 40, ikkinchisi 60 km
    yurdi; 20 + 40 = 60 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Afsona 4 km/soat bilan piyoda ketdi.
  30 minutdan keyin Dilnoza 12 km/soat bilan velosipedda ortidan
  chiqdi. Qachon quvib yetadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>15 minutdan keyin.</b> Ustunlik: 4 × 0,5 = 2 km. Farq
    tezligi 12 − 4 = 8 km/soat. t = 2 ÷ 8 = 0,25 soat = 15 minut.
    Tekshirish: Afsona 0,75 soatda 3 km, Dilnoza 0,25 soatda 3 km ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Ikki velosipedchi bir joydan qarama-qarshi
  tomonga chiqdi: 14 va 16 km/soat. 2 soatdan keyin oralari qancha
  boʻladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>60 km.</b> Bu safar ora <b>ortadi</b>: uzoqlashish tezligi
    14 + 16 = 30 km/soat. 30 × 2 = 60 km. Qoʻshish qoidasi
    uzoqlashishda ham ishlaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">7. Ikki shahar orasi 460 km. Soat 06:00 da
  birinchisidan 50 km/soat bilan avtobus chiqdi. Soat 08:00 da
  ikkinchisidan 70 km/soat bilan qarshi avtobus chiqdi. Soat nechada
  uchrashadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>11:00 da.</b> 08:00 gacha birinchisi 50 × 2 = 100 km yurdi,
    demak ora 460 − 100 = 360 km. Yaqinlashish tezligi
    50 + 70 = 120 km/soat. t = 360 ÷ 120 = 3 soat, 08:00 dan boshlab —
    yaʼni 11:00. Tekshirish: birinchisi 5 soatda 250 km, ikkinchisi
    3 soatda 210 km; 250 + 210 = 460 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Uchrashuv</b><span>ikki jismning bir nuqtada toʻqnash kelishi;
    ingl. meeting</span></li>
  <li><b>Qarama-qarshi harakat</b><span>bir-biriga qarab yurish; ingl.
    opposite directions</span></li>
  <li><b>Yaqinlashish tezligi</b><span>orani kamaytirish tezligi,
    v₁ + v₂; ingl. closing speed</span></li>
  <li><b>Quvish</b><span>bir yoʻnalishda tezroq harakatlanib yetib
    olish; ingl. catching up</span></li>
  <li><b>Farq tezligi</b><span>bir yoʻnalishdagi v₁ − v₂; ingl. relative
    speed</span></li>
  <li><b>Boshlangʻich ustunlik</b><span>oldin chiqqanning bosib ulgurgan
    yoʻli; ingl. head start</span></li>
  <li><b>Uzoqlashish</b><span>oraning ortib borishi; ingl. moving
    apart</span></li>
  <li><b>Ora</b><span>ikki jism orasidagi masofa; ingl. gap</span></li>
  <li><b>Bir vaqtda</b><span>ikkalasi ayni paytda yoʻlga chiqishi; ingl.
    simultaneously</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Asosiy savol: <b>ora har soatda qanchaga kamayadi?</b></li>
    <li>Qarama-qarshi: v₁ + v₂. Bir yoʻnalishda: v₁ − v₂.</li>
    <li>t = ora ÷ (yaqinlashish tezligi).</li>
    <li>Uchrashuvda vaqt ikkalasi uchun bir xil, masofa esa har
      xil.</li>
    <li>Uchrashuv joyi oʻrtada emas — tezliklar teng boʻlsagina
      oʻrtada.</li>
    <li>Bir vaqtda chiqmagan boʻlsa, avval boshlangʻich ustunlikni
      oradan ayiring.</li>
    <li>Uzoqlashishda ham tezliklar qoʻshiladi — faqat ora ortadi.</li>
  </ul>
</div>
""",
    },
]
