# -*- coding: utf-8 -*-
"""Prime Math — darslar 81–83 (aldamchi diagrammalar, sanash, ehtimollik).

**Blok F: Maʼlumot va ehtimollik (75–84).**
Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md

  mashqlar — practice/management/commands/_practice_pm_81_83.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_81_83.py

⚠️ PM-81 — butun blokning hosilasi: 75–80 da oʻrgangan hamma narsa shu
   yerda qurolga aylanadi. Darsning markazida BIR XIL maʼlumotning
   ikkita chizmasi turadi (48, 50, 52): oʻqi noldan boshlanganida C
   ustuni A dan atigi 1,08 marta baland, oʻqi 46 dan boshlanganida esa
   roppa-rosa 3 marta. Sonlar bir xil, xulosa boshqa.

⚠️ Chizmalar generatsiya qilingan: scratchpad/gen_pm81_83.py.
   verify_pm_81_83.py ikkala ustunli diagrammani BITTA maʼlumotdan
   qayta hisoblaydi va aldov nisbatini (3,00) tekshiradi.

⚠️ Kumulyativ chegaralar:
  • PM-81 — aldamchi diagrammalar. Oʻrtacha/mediana (PM-78/79) va
    diagramma oʻqish (PM-77) faol ishlatiladi;
  • PM-82 — koʻpaytirish prinsipi. ⛔ EHTIMOLLIK YOʻQ: bu dars faqat
    variantlarni SANASH haqida;
  • PM-83 — ehtimollik gʻoyasi va 0–1 shkalasi. Oddiy hollar uchun
    P = qulay ÷ jami kiritiladi, chunki hodisani shkalaga qoʻyishning
    boshqa yoʻli yoʻq. ⛔ Murakkab sanash bilan hisoblash, teskari
    hodisa qoidasi va TAJRIBA (chastota → ehtimollik) PM-84 da.
  • ⛔ Blok G (matnli masala usullari, 85–94) YOʻQ.
  • Faol ishlatiladi: foiz va foiz oʻzgarishi (PM-23/25), kasr↔foiz
    (PM-22), diagramma turlari (PM-76), diagrammani oʻqish (PM-77),
    oʻrtacha va mediana (PM-78/79), yuza k² (PM-72).

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_81_83.py --author=prime
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
    # PM-81 — aldamchi diagrammalar
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-81: Aldamchi diagrammalar — statistika qanday yolgʻon gapiradi",
        "category": "math",
        "order": 81,
        "summary": (
            "Diagramma yolgʻon son koʻrsatmasdan ham aldashi mumkin. Oʻqni "
            "noldan boshlamaslik, belgi yuzasini kattalashtirish va kerakli "
            "oyni tanlab olish — uchta eng keng tarqalgan hiyla."
        ),
        "stories": ["Reklamadagi ustunlar"],
        "content": """
<h2>PM-81: Aldamchi diagrammalar — statistika qanday yolgʻon gapiradi</h2>

<p>Reklamada shunday yozuv bor: «Bizning natijamiz 3 barobar yuqori!»
Yonida esa diagramma turibdi va ustunlar haqiqatan uch barobar farq
qiladi.</p>

<p>Hamma son rost. Diagramma ham toʻgʻri chizilgan. Va shunga qaramay bu
— <b>yolgʻon</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>oʻqi noldan boshlanmagan diagrammani tanib olasiz;</li>
    <li>belgi yuzasi bilan aldashni fosh qilasiz;</li>
    <li>tanlab olingan davr hiylasini koʻrasiz;</li>
    <li>har qanday diagrammaga beriladigan besh savolni oʻrganasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Birinchi savol, har doim</span>
  <span class="pe-chip pe-chip--s">Oʻq</span>
  <span class="pe-op">qayerdan boshlangan?</span>
</div>

<h3>1. Eng koʻp uchraydigan hiyla: oʻq noldan boshlanmagan</h3>

<p>Uchta doʻkonning savdosi: A — 48, B — 50, C — 52 million soʻm.
Quyida <b>bir xil</b> sonlarning ikkita diagrammasi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 195" role="img" aria-label="Halol diagramma: oʻq noldan boshlangan">
    <line class="pm-ch__ax" x1="46" y1="160" x2="302" y2="160"/>
    <text class="pm-ch__cap" x="40" y="164" text-anchor="end">0</text>
    <line class="pm-ch__grid" x1="46" y1="120" x2="302" y2="120"/>
    <text class="pm-ch__cap" x="40" y="124" text-anchor="end">20</text>
    <line class="pm-ch__grid" x1="46" y1="80" x2="302" y2="80"/>
    <text class="pm-ch__cap" x="40" y="84" text-anchor="end">40</text>
    <line class="pm-ch__grid" x1="46" y1="40" x2="302" y2="40"/>
    <text class="pm-ch__cap" x="40" y="44" text-anchor="end">60</text>
    <rect class="pm-ch__bar" x="96.3" y="64" width="44" height="96" rx="3"/>
    <text class="pm-ch__val" x="118.3" y="57" text-anchor="middle">48</text>
    <text class="pm-ch__lbl" x="118.3" y="178" text-anchor="middle">A</text>
    <rect class="pm-ch__bar" x="155" y="60" width="44" height="100" rx="3"/>
    <text class="pm-ch__val" x="177" y="53" text-anchor="middle">50</text>
    <text class="pm-ch__lbl" x="177" y="178" text-anchor="middle">B</text>
    <rect class="pm-ch__bar" x="213.7" y="56" width="44" height="104" rx="3"/>
    <text class="pm-ch__val" x="235.7" y="49" text-anchor="middle">52</text>
    <text class="pm-ch__lbl" x="235.7" y="178" text-anchor="middle">C</text>
  </svg>
  <figcaption>Halol diagramma: oʻq noldan boshlangan. Uch doʻkon
  deyarli teng savdo qilgan.</figcaption>
</figure>

<figure class="pm-fig">
  <svg viewBox="0 0 320 195" role="img" aria-label="Aldamchi diagramma: oʻq 46 dan boshlangan">
    <line class="pm-ch__ax" x1="46" y1="160" x2="302" y2="160"/>
    <text class="pm-ch__cap" x="40" y="164" text-anchor="end">46</text>
    <line class="pm-ch__grid" x1="46" y1="130" x2="302" y2="130"/>
    <text class="pm-ch__cap" x="40" y="134" text-anchor="end">48</text>
    <line class="pm-ch__grid" x1="46" y1="100" x2="302" y2="100"/>
    <text class="pm-ch__cap" x="40" y="104" text-anchor="end">50</text>
    <line class="pm-ch__grid" x1="46" y1="70" x2="302" y2="70"/>
    <text class="pm-ch__cap" x="40" y="74" text-anchor="end">52</text>
    <line class="pm-ch__grid" x1="46" y1="40" x2="302" y2="40"/>
    <text class="pm-ch__cap" x="40" y="44" text-anchor="end">54</text>
    <rect class="pm-ch__bar" x="96.3" y="130" width="44" height="30" rx="3"/>
    <text class="pm-ch__val" x="118.3" y="123" text-anchor="middle">48</text>
    <text class="pm-ch__lbl" x="118.3" y="178" text-anchor="middle">A</text>
    <rect class="pm-ch__bar" x="155" y="100" width="44" height="60" rx="3"/>
    <text class="pm-ch__val" x="177" y="93" text-anchor="middle">50</text>
    <text class="pm-ch__lbl" x="177" y="178" text-anchor="middle">B</text>
    <rect class="pm-ch__bar" x="213.7" y="70" width="44" height="90" rx="3"/>
    <text class="pm-ch__val" x="235.7" y="63" text-anchor="middle">52</text>
    <text class="pm-ch__lbl" x="235.7" y="178" text-anchor="middle">C</text>
  </svg>
  <figcaption>Aynan oʻsha sonlar, lekin oʻq 46 dan boshlangan. Endi C
  ustuni A dan uch barobar baland koʻrinadi.</figcaption>
</figure>

<p>Ikkinchi chizmada C ning ustuni A nikidan roppa-rosa <b>3 marta</b>
uzun. Lekin sonlarga qarang: 52 va 48. Haqiqiy farq nechchi foiz?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">52 − 48 = 4</span>
    <span class="pm-solve__why">Farq</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">4 ÷ 48 × 100 ≈ 8,3%</span>
    <span class="pm-solve__why">Asos — A ning 48 tasi (PM-25)</span>
  </div>
</div>

<p>Sakkiz foiz. Diagramma esa uch barobarni koʻrsatdi. Yolgʻon son
yoʻq — yolgʻon <b>oʻqda</b>.</p>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Nega bu ishlaydi</p>
  <p>Odam ustunning uzunligiga qaraydi, oʻqdagi mayda raqamlarga emas.
  Oʻqni 46 dan boshlaganda 48 ning «ustunidan» 46 tasi kesib
  tashlanadi — qolgan ikkitagina koʻrinadi. Shuning uchun
  <b>ustunli diagrammada oʻq har doim noldan boshlanadi</b>
  (PM-76).</p>
</div>

<h3>2. Ikkinchi hiyla: belgining yuzasi</h3>

<p>Baʼzan ustun oʻrniga rasm qoʻyiladi: qop, odam, uy. Va rasmni ikki
marta kattalashtirishadi — ikkala tomonidan.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 205" role="img" aria-label="Belgining tomoni ikki marta katta, yuzasi esa toʻrt marta">
    <rect class="pm-ch__bar" x="52" y="112" width="40" height="40" rx="2"/>
    <text class="pm-ch__lbl" x="72" y="170" text-anchor="middle">1 dona</text>
    <rect class="pm-ch__bar" x="168" y="72" width="80" height="80" rx="2"/>
    <line class="pm-ch__grid" x1="208" y1="72" x2="208" y2="152"/>
    <line class="pm-ch__grid" x1="168" y1="112" x2="248" y2="112"/>
    <text class="pm-ch__lbl" x="208" y="170" text-anchor="middle">2 dona?</text>
    <text class="pm-ch__val" x="208" y="192" text-anchor="middle">aslida 4 marta katta</text>
    <text class="pm-ch__cap" x="52" y="30">Tomoni 2 marta, yuzasi esa 2² = 4 marta</text>
  </svg>
  <figcaption>Ichidagi chiziqlar koʻrsatib turibdi: katta kvadratga
  kichigidan toʻrttasi sigʻadi.</figcaption>
</figure>

<p>Bu aynan PM-72 dagi qoida: tomonlar k marta oshsa, yuza
<b>k<sup>2</sup></b> marta oshadi. Koʻz esa uzunlikni emas,
<b>yuzani</b> baholaydi — shuning uchun «ikki barobar» degan rasm toʻrt
barobar taassurot qoldiradi.</p>

<h3>3. Uchinchi hiyla: kerakli davrni tanlab olish</h3>

<p>Doʻkonning olti oylik savdosi: 100, 95, 90, 92, 95, 88 million
soʻm.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Reklama koʻrsatadi</p>
    <p>3–5-oylar: 90 → 92 → 95.
    <br>«Savdo oʻsmoqda!» — 5,6% oʻsish.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Butun manzara</p>
    <p>1–6-oylar: 100 → 88.
    <br>Aslida savdo 12 foizga tushgan.</p>
  </div>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">(95 − 90) ÷ 90 × 100 ≈ 5,6%</span>
    <span class="pm-solve__why">Tanlangan uch oy — oʻsish</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">(88 − 100) ÷ 100 × 100 = −12%</span>
    <span class="pm-solve__why">Butun davr — pasayish</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Har doim soʻrang: nega aynan shu davr?</p>
  <p>Agar diagramma gʻalati davrni koʻrsatsa — masalan «mart–may» yoki
  «2019–2021» — sababi bor. Toʻliq maʼlumotni soʻrang. Yolgʻon aytish
  uchun soxta son kerak emas; kerakli qismini koʻrsatib, qolganini
  yashirish kifoya.</p>
</div>

<h3>4. Toʻrtinchi hiyla: qaysi «oʻrtacha»?</h3>

<p>Buni PM-79 da koʻrgan edik. «Oʻrtacha maosh 10 million» degan jumla
rost boʻlishi va shu bilan birga chalgʻitishi mumkin — agar bitta juda
katta maosh oʻrtachani koʻtarib turgan boʻlsa. Mediana esa haqiqatni
aytadi.</p>

<p>Yana bir yaqin qarindoshi: <b>foiz, lekin asossiz</b>. «50 foizga
koʻp!» degan yozuv 2 tadan 3 taga oʻsishni ham bildirishi mumkin.</p>

<h3>5. Diagrammaga beriladigan besh savol</h3>

<div class="pe-steps">
  <ol>
    <li><b>Oʻq noldan boshlanganmi?</b> Yoʻq boʻlsa, ustunlarning
      uzunligi yolgʻon gapiradi.</li>
    <li><b>Birlik qanday?</b> Dona, foiz, million — buni bilmasdan hech
      nima demang.</li>
    <li><b>Qaysi davr olingan va nega?</b> Undan oldin va keyin nima
      boʻlgan?</li>
    <li><b>Rasm ishlatilganmi?</b> Ishlatilgan boʻlsa, uning yuzasiga
      emas, songa qarang.</li>
    <li><b>«Oʻrtacha» deganda nima nazarda tutilgan?</b> Va foiz
      nimadan hisoblangan?</li>
  </ol>
</div>

<h3>Matnli masala</h3>

<p>Sharbat reklamasida yozuv bor: «Bizning sharbatimizda C vitamini
3 barobar koʻp!» Yonidagi diagrammada ikkita ustun: raqib mahsuloti 92,
oʻzimizniki 96 (milligrammda). Diagrammaning oʻqi 90 dan boshlangan.</p>

<p><b>Ustunlar necha marta farq qiladi va haqiqiy farq necha
foiz?</b></p>

<p><b>Reja:</b> avval ustunlarning balandligini hisoblaymiz (oʻq 90 dan
boshlangani uchun), keyin haqiqiy foizni topamiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">92 − 90 = 2 va 96 − 90 = 6</span>
    <span class="pm-solve__why">Oʻqdan yuqoridagi qism — koʻzga
    koʻringani</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">6 ÷ 2 = 3 marta</span>
    <span class="pm-solve__why">Ustunlar haqiqatan uch barobar farq
    qiladi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">96 − 92 = 4</span>
    <span class="pm-solve__why">Haqiqiy farq</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">4 ÷ 92 × 100 ≈ 4,3%</span>
    <span class="pm-solve__why">Asos — raqibning 92 tasi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Agar oʻq noldan boshlanganida ustunlar 92 va 96 boʻlardi — koʻz
  bilan deyarli farqsiz.
  <br><b>Javob:</b> ustunlar 3 marta farq qiladi, mahsulotlar esa atigi
  4,3 foizga. Reklamadagi «3 barobar» — ustunlarning, sharbatning
  emas.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">«Ustun ikki barobar baland, demak soni ikki
  barobar koʻp»</p>
  <p class="pe-fix__good">Avval oʻqning boshlanishini tekshiring</p>
  <p class="pe-fix__why">Oʻq noldan boshlanmagan boʻlsa, ustunlarning
  nisbati sonlarning nisbatiga umuman toʻgʻri kelmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Rasm ikki marta kattaroq → miqdor ikki barobar</p>
  <p class="pe-fix__good">Yuzasi 2<sup>2</sup> = 4 marta katta</p>
  <p class="pe-fix__why">Koʻz uzunlikni emas, yuzani baholaydi (PM-72).
  Shuning uchun rasmli diagrammada songa qarash shart.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">«Mart–mayda oʻsdi, demak yil davomida oʻsgan»</p>
  <p class="pe-fix__good">Butun davrni soʻrang</p>
  <p class="pe-fix__why">Uch oyda 5,6% oʻsish olti oylik 12% pasayish
  ichida boʻlishi mumkin. Tanlangan qism butunni ifodalamaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">«50 foizga koʻp» — demak juda koʻp</p>
  <p class="pe-fix__good">Nimadan 50 foiz?</p>
  <p class="pe-fix__why">2 tadan 3 taga oʻtish ham 50 foiz. Foiz har
  doim <b>asos</b> bilan birga aytiladi (PM-23).</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Ustunli diagrammaning sonlar oʻqi qayerdan
  boshlanishi kerak?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Noldan.</b> Faqat shunda ustunlarning uzunligi sonlarning
    nisbatini toʻgʻri koʻrsatadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Oʻqi 40 dan boshlangan diagrammada ikkita
  ustun: 44 va 48. Ular necha marta farq qilib koʻrinadi va haqiqiy farq
  necha foiz?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>2 marta koʻrinadi; haqiqiy farq ≈ 9,1%.</b> Oʻqdan yuqorisi:
    4 va 8, yaʼni 8 ÷ 4 = 2 marta. Haqiqiy farq: (48 − 44) ÷ 44 × 100 =
    9,09…%</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Reklamadagi rasmning tomoni 3 marta
  kattalashtirildi. Yuzasi necha marta oshdi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>9 marta.</b> 3<sup>2</sup> = 9 (PM-72). Koʻzga u toʻqqiz
    barobar katta boʻlib koʻrinadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Doʻkonning savdosi 200 dan 210 mln soʻmga
  oshdi. Reklamada «oʻsish!» deb yozildi. Bu necha foiz?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5%.</b> (210 − 200) ÷ 200 × 100 = 5%. Oʻsish bor, lekin u
    kichkina — «oʻsish!» degan yozuv buni yashiradi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Nima uchun diagrammada faqat uchta oy
  koʻrsatilgan boʻlsa, ehtiyot boʻlish kerak?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Chunki qolgan oylar boshqa manzara koʻrsatishi mumkin.</b>
    Tanlangan davr butun maʼlumotni ifodalamasligi mumkin — toʻliq
    maʼlumotni soʻrash kerak.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Ikki maktabning imtihon natijasi
  koʻrsatilgan: A maktabda oʻrtacha 78 ball, B maktabda 76 ball.
  Diagrammaning oʻqi 75 dan boshlangan. Ustunlar necha marta farq qilib
  koʻrinadi va haqiqiy farq necha foiz?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3 marta koʻrinadi; haqiqiy farq ≈ 2,6%.</b> Oʻqdan yuqorisi:
    78 − 75 = 3 va 76 − 75 = 1, demak 3 ÷ 1 = 3 marta. Haqiqiy farq esa
    (78 − 76) ÷ 76 × 100 = 2,63…% — deyarli sezilmaydigan farq uch
    barobarga aylantirilgan.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Aldamchi diagramma</b><span>rost sonlar bilan notoʻgʻri
    taassurot qoldiradigan chizma; ingl. misleading graph</span></li>
  <li><b>Kesilgan oʻq</b><span>noldan boshlanmagan sonlar oʻqi; ingl.
    truncated axis</span></li>
  <li><b>Shkala</b><span>oʻqdagi boʻlinishlar qadami; ingl.
    scale</span></li>
  <li><b>Asos</b><span>foiz nimadan hisoblanayotgani; ingl.
    base</span></li>
  <li><b>Tanlangan davr</b><span>maʼlumotning koʻrsatilgan qismi; ingl.
    cherry-picked range</span></li>
  <li><b>Belgi</b><span>ustun oʻrniga qoʻyilgan rasm; ingl.
    pictogram</span></li>
  <li><b>Yuza</b><span>rasmning egallagan joyi, k<sup>2</sup> qoidasi;
    ingl. area</span></li>
  <li><b>Manba</b><span>maʼlumot qayerdan olingani; ingl.
    source</span></li>
  <li><b>Xolislik</b><span>maʼlumotni buzmasdan koʻrsatish; ingl.
    objectivity</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Diagramma yolgʻon son koʻrsatmasdan ham aldashi mumkin.</li>
    <li>Eng koʻp uchraydigani — oʻq noldan boshlanmagani.</li>
    <li>Rasmning tomoni k marta oshsa, koʻzga k<sup>2</sup> marta
      koʻrinadi.</li>
    <li>Tanlangan qisqa davr butunni ifodalamasligi mumkin.</li>
    <li>«Oʻrtacha» va «foiz» deyilganda: qaysi oʻrtacha, nimadan
      foiz?</li>
    <li>Besh savolni bering — keyin xulosa chiqaring.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-82 — sanash: koʻpaytirish prinsipi
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-82: Sanash: koʻpaytirish prinsipi",
        "category": "math",
        "order": 82,
        "summary": (
            "Nechta variant bor? Har bir tanlovni bittalab sanash shart emas: "
            "bosqichlarning imkoniyatlari koʻpaytiriladi. Daraxt diagrammasi "
            "bu qoida nega ishlashini koʻrsatadi."
        ),
        "stories": ["Necha xil kiyim tanlash mumkin"],
        "content": """
<h2>PM-82: Sanash: koʻpaytirish prinsipi</h2>

<p>Shkafingizda uchta koʻylak va ikkita shim bor. Necha xil kiyinishingiz
mumkin?</p>

<p>Bittalab sanab chiqsa boʻladi. Lekin koʻylak yigirmata boʻlsa-chi?
Shuning uchun matematikada boshqa yoʻl bor va u bitta amaldan
iborat.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>koʻpaytirish prinsipini qoʻllaysiz;</li>
    <li>daraxt diagrammasi chizib, qoidani isbotlaysiz;</li>
    <li>uch va undan koʻp bosqichli tanlovni sanaysiz;</li>
    <li>kod va parollar sonini hisoblaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Koʻpaytirish prinsipi</span>
  <span class="pe-chip pe-chip--o">1-bosqich</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--o">2-bosqich</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--o">…</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">variantlar soni</span>
</div>

<h3>1. Daraxt chizamiz</h3>

<p>Uchta koʻylak: oq, koʻk, yashil. Ikkita shim: qora, jinsi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 200" role="img" aria-label="Daraxt diagrammasi: uchta koʻylak va ikkita shim">
    <circle class="pm-ch__dot" cx="34" cy="106" r="5"/>
    <line class="pm-ch__line" x1="34" y1="106" x2="132" y2="46"/>
    <text class="pm-ch__cap" x="79" y="68" text-anchor="middle">oq</text>
    <circle class="pm-ch__dot" cx="132" cy="46" r="5"/>
    <line class="pm-ch__line" x1="132" y1="46" x2="236" y2="24"/>
    <circle class="pm-ch__dot" cx="236" cy="24" r="5"/>
    <text class="pm-ch__cap" x="245" y="28">qora</text>
    <line class="pm-ch__line" x1="132" y1="46" x2="236" y2="68"/>
    <circle class="pm-ch__dot" cx="236" cy="68" r="5"/>
    <text class="pm-ch__cap" x="245" y="72">jinsi</text>
    <line class="pm-ch__line" x1="34" y1="106" x2="132" y2="106"/>
    <text class="pm-ch__cap" x="79" y="98" text-anchor="middle">koʻk</text>
    <circle class="pm-ch__dot" cx="132" cy="106" r="5"/>
    <line class="pm-ch__line" x1="132" y1="106" x2="236" y2="84"/>
    <circle class="pm-ch__dot" cx="236" cy="84" r="5"/>
    <text class="pm-ch__cap" x="245" y="88">qora</text>
    <line class="pm-ch__line" x1="132" y1="106" x2="236" y2="128"/>
    <circle class="pm-ch__dot" cx="236" cy="128" r="5"/>
    <text class="pm-ch__cap" x="245" y="132">jinsi</text>
    <line class="pm-ch__line" x1="34" y1="106" x2="132" y2="166"/>
    <text class="pm-ch__cap" x="79" y="152" text-anchor="middle">yashil</text>
    <circle class="pm-ch__dot" cx="132" cy="166" r="5"/>
    <line class="pm-ch__line" x1="132" y1="166" x2="236" y2="144"/>
    <circle class="pm-ch__dot" cx="236" cy="144" r="5"/>
    <text class="pm-ch__cap" x="245" y="148">qora</text>
    <line class="pm-ch__line" x1="132" y1="166" x2="236" y2="188"/>
    <circle class="pm-ch__dot" cx="236" cy="188" r="5"/>
    <text class="pm-ch__cap" x="245" y="192">jinsi</text>
    <text class="pm-ch__val" x="160" y="20" text-anchor="middle">3 × 2 = 6 ta variant</text>
  </svg>
  <figcaption>Har bir koʻylakdan ikkita yoʻl chiqadi. Uchta koʻylak,
  har birida ikkitadan — jami oltita uch.</figcaption>
</figure>

<p>Daraxtning oxiridagi nuqtalarni sanang: <b>6</b> ta. Va endi qarang
nega: uchta koʻylakning <b>har biriga</b> ikkitadan shim mos keladi,
demak 2 + 2 + 2, yaʼni <b>3 × 2</b>.</p>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Koʻpaytirish prinsipi</p>
  <p>Agar birinchi tanlovni <b>m</b> xil, ikkinchisini <b>n</b> xil
  qilish mumkin boʻlsa, ikkalasini birga <b>m × n</b> xil qilish
  mumkin. Bosqich qancha koʻp boʻlsa, shuncha koʻpaytiruvchi
  qoʻshiladi.</p>
</div>

<h3>2. Jadval bilan tekshirish</h3>

<p>Endi toʻrtta shim boʻlsin. Jadval tuzamiz: qatorlar — koʻylaklar,
ustunlar — shimlar.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Koʻylak \\ Shim</th><th>qora</th><th>jinsi</th><th>kulrang</th>
    <th>oq</th></tr>
  <tr><td>oq</td><td class="pm-word__sym">1</td><td class="pm-word__sym">2</td>
    <td class="pm-word__sym">3</td><td class="pm-word__sym">4</td></tr>
  <tr><td>koʻk</td><td class="pm-word__sym">5</td><td class="pm-word__sym">6</td>
    <td class="pm-word__sym">7</td><td class="pm-word__sym">8</td></tr>
  <tr><td>yashil</td><td class="pm-word__sym">9</td><td class="pm-word__sym">10</td>
    <td class="pm-word__sym">11</td><td class="pm-word__sym">12</td></tr>
</table></div>

<p>Jadvalda 3 qator va 4 ustun bor, katakchalar soni esa
3 × 4 = <b>12</b>. Bu — oʻsha koʻpaytirish prinsipining boshqa
koʻrinishi.</p>

<h3>3. Uchinchi bosqich qoʻshamiz</h3>

<p>Ikkita poyabzal ham boʻlsin. Endi har bir variantdan yana ikkitaga
tarmoqlanadi:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 × 4 = 12</span>
    <span class="pm-solve__why">Koʻylak va shim</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">12 × 2 = 24</span>
    <span class="pm-solve__why">Poyabzal ham qoʻshildi</span>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">3 × 4 × 2 = 24</p>
  <p class="pe-ex__uz">Uchta koʻylak, toʻrtta shim va ikkita poyabzal
  bilan yigirma toʻrt xil kiyinish mumkin.</p>
  <p class="pe-ex__why">Bosqichlarni ketma-ket koʻpaytirib boraverasiz —
  tartibning ahamiyati yoʻq.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Qoʻshish emas, koʻpaytirish</p>
  <p>3 + 4 + 2 = 9 emas! Qoʻshish «yo koʻylak, yo shim, yo poyabzal
  tanlayman» degan boshqa savolga javob berardi. Bu yerda esa
  <b>hammasi birga</b> tanlanadi — har bir koʻylak har bir shim bilan
  keladi. «Va» — koʻpaytirish, «yoki» — qoʻshish.</p>
</div>

<h3>4. Kodlar va parollar</h3>

<p>Velosiped qulfida uchta gʻildirak bor, har birida 0 dan 9 gacha
raqam. Nechta kod boʻlishi mumkin?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Har bir gʻildirakda 10 ta raqam</span>
    <span class="pm-solve__why">0, 1, 2, …, 9</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">10 × 10 × 10 = 1000 ta kod</span>
    <span class="pm-solve__why">000 dan 999 gacha</span>
  </div>
</div>

<p>Diqqat: bu yerda raqamlar <b>takrorlanishi mumkin</b> — 777 ham
haqiqiy kod. Shuning uchun har bir bosqichda baribir 10 ta imkoniyat
qoladi.</p>

<h3>Matnli masala</h3>

<p>Maktab bufetida tushlik uchun: 3 xil birinchi taom, 4 xil ikkinchi
taom va 2 xil ichimlik bor. Tushlik — har biridan bittadan.</p>

<p><b>Necha xil tushlik boʻlishi mumkin? Va toʻrt haftalik oyda (20 ta
oʻquv kuni) har kuni boshqacha tushlik qilish mumkinmi?</b></p>

<p><b>Reja:</b> bosqichlarni koʻpaytiramiz, keyin natijani oʻquv kunlari
soni bilan solishtiramiz.</p>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Uchta va toʻrtta allaqachon 12 beradi, ikkita ichimlik uni
  ikkilantiradi — 20 dan koʻp chiqishi kerak.</span>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 × 4 = 12</span>
    <span class="pm-solve__why">Birinchi va ikkinchi taom</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">12 × 2 = 24 xil tushlik</span>
    <span class="pm-solve__why">Ichimlik ham qoʻshildi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">24 &gt; 20 — ha, mumkin</span>
    <span class="pm-solve__why">Hatto toʻrtta variant ortib ham
    qoladi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>24 — taxminimizdagi «20 dan koʻp» ✓
  <br>Boshqa yoʻl: har bir ichimlik uchun 12 tadan variant bor, yaʼni
  12 + 12 = 24 ✓
  <br><b>Javob:</b> 24 xil tushlik; 20 kunga yetadi va yana 4 ta ortadi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">3 koʻylak va 4 shim → 3 + 4 = 7 variant</p>
  <p class="pe-fix__good">3 × 4 = 12 variant</p>
  <p class="pe-fix__why">Har bir koʻylak <b>har bir</b> shim bilan
  kiyiladi. Qoʻshish «faqat bittasini tanlayman» degan boshqa
  savolga javob beradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Uchta bosqich: 3 × 4 + 2 = 14</p>
  <p class="pe-fix__good">3 × 4 × 2 = 24</p>
  <p class="pe-fix__why">Har bir bosqich <b>koʻpaytiruvchi</b> boʻlib
  qoʻshiladi. Amallar tartibi ham buni buzadi: qoʻshish oxirida
  bajarilib, javob butunlay boshqa chiqadi (PM-5).</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Uch xonali kod, har xonada 10 raqam →
  10 × 3 = 30</p>
  <p class="pe-fix__good">10 × 10 × 10 = 1000</p>
  <p class="pe-fix__why">Bosqichlar soni koʻpaytiruvchi emas,
  <b>koʻpaytiruvchilar soni</b>. Uchta bosqich — uchta oʻnlik
  koʻpaytiriladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Daraxtdagi hamma nuqtani sanash: 1 + 3 + 6 = 10</p>
  <p class="pe-fix__good">Faqat oxirgi nuqtalarni sanang: 6</p>
  <p class="pe-fix__why">Variant — bu daraxtning <b>uchi</b>, yaʼni
  toʻliq bir yoʻl. Oraliq tugunlar tugallanmagan tanlovlar.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 4 xil muzqaymoq va 5 xil qoʻshimcha bor. Necha
  xil kombinatsiya?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>20 ta.</b> 4 × 5 = 20.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 2 xil non, 3 xil pishloq va 4 xil sabzavot.
  Necha xil buterbrod?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>24 ta.</b> 2 × 3 × 4 = 24.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Ikkita zar tashlandi. Nechta natija boʻlishi
  mumkin?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>36 ta.</b> Har bir zarda 6 tadan natija: 6 × 6 = 36.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Uch xonali kod tuziladi, har xonaga 4 ta
  harfdan biri qoʻyiladi. Nechta kod boʻlishi mumkin?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>64 ta.</b> 4 × 4 × 4 = 64. Harflar takrorlanishi mumkin,
    shuning uchun har xonada baribir 4 ta imkoniyat qoladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Tanga uch marta tashlandi. Nechta natija
  boʻlishi mumkin?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>8 ta.</b> Har tashlashda 2 ta natija: 2 × 2 × 2 = 8.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Afsona 5 ta koʻylak, 3 ta yubka va 2 ta
  sharfdan iborat kiyimlarni almashtirib kiyadi. Har kuni boshqacha
  kiyinsa, necha kunga yetadi? Bu ikki oydan koʻpmi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>30 kunga; ikki oyga yetmaydi.</b> 5 × 3 × 2 = 30 ta variant,
    demak 30 kun. Ikki oy taxminan 60 kun, shuning uchun yarmigagina
    yetadi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Koʻpaytirish prinsipi</b><span>bosqichlarning imkoniyatlari
    koʻpaytiriladi; ingl. multiplication principle</span></li>
  <li><b>Variant</b><span>mumkin boʻlgan bir tanlov; ingl.
    outcome</span></li>
  <li><b>Bosqich</b><span>tanlovning bir qadami; ingl. stage</span></li>
  <li><b>Daraxt diagrammasi</b><span>tanlovlarni shoxlar bilan
    koʻrsatuvchi chizma; ingl. tree diagram</span></li>
  <li><b>Kombinatsiya</b><span>bir nechta tanlovning birgalikdagi
    natijasi; ingl. combination</span></li>
  <li><b>Kod</b><span>belgilar ketma-ketligi; ingl. code</span></li>
  <li><b>Takrorlanish</b><span>bir belgini qayta ishlatish imkoni; ingl.
    repetition</span></li>
  <li><b>Sanash</b><span>variantlar sonini aniqlash; ingl.
    counting</span></li>
  <li><b>Jadval usuli</b><span>variantlarni qator va ustunga joylash;
    ingl. table method</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Koʻpaytirish prinsipi: m × n × … = variantlar soni.</li>
    <li>«Va» — koʻpaytirish, «yoki» — qoʻshish.</li>
    <li>Daraxt diagrammasi qoidani koʻrsatadi: variant — daraxtning
      uchi.</li>
    <li>Jadval ikki bosqich uchun qulay: qatorlar × ustunlar.</li>
    <li>Har bir yangi bosqich yangi koʻpaytiruvchi qoʻshadi.</li>
    <li>Kodlarda belgilar takrorlanishi mumkin, shuning uchun har
      xonada imkoniyatlar soni kamaymaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-83 — ehtimollik gʻoyasi
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-83: Ehtimollik gʻoyasi: 0 dan 1 gacha",
        "category": "math",
        "order": 83,
        "summary": (
            "«Ehtimol», «boʻlishi mumkin», «aniq» — bu soʻzlarni son bilan "
            "almashtirish mumkin. Har qanday hodisaning ehtimolligi 0 bilan "
            "1 orasida yotadi va uni hisoblab topsa boʻladi."
        ),
        "stories": ["Tanga, zar va ob-havo bashorati"],
        "content": """
<h2>PM-83: Ehtimollik gʻoyasi: 0 dan 1 gacha</h2>

<p>«Ertaga yomgʻir yogʻishi mumkin.» «Bu jamoa gʻalaba qozonsa
kerak.» «Menimcha, imtihon oson boʻladi.»</p>

<p>Bu jumlalarning hammasi noaniq. Matematika esa ularni <b>songa</b>
aylantirishni oʻrgatadi — va oʻsha son har doim 0 bilan 1 orasida
boʻladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>ehtimollikni 0 dan 1 gacha boʻlgan shkalada joylashtirasiz;</li>
    <li>teng imkoniyatli hollarda ehtimollikni hisoblaysiz;</li>
    <li>uni kasr, oʻnlik kasr va foiz koʻrinishida yozasiz;</li>
    <li>imkonsiz va aniq hodisalarni ajratasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Teng imkoniyatli hollarda</span>
  <span class="pe-chip pe-chip--s">P</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">qulay hollar</span>
  <span class="pe-op">÷</span>
  <span class="pe-chip pe-chip--o">jami hollar</span>
</div>

<h3>1. Shkala: 0 dan 1 gacha</h3>

<p><b>Ehtimollik</b> — hodisaning roʻy berish imkoniyatini
oʻlchaydigan son. U hech qachon 0 dan kichik va 1 dan katta
boʻlmaydi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 168" role="img" aria-label="Ehtimollik shkalasi: 0 dan 1 gacha">
    <line class="pm-ch__ax" x1="40" y1="108" x2="288" y2="108"/>
    <line class="pm-ch__ax" x1="40" y1="108" x2="40" y2="114"/>
    <text class="pm-ch__cap" x="40" y="128" text-anchor="middle">0</text>
    <line class="pm-ch__ax" x1="102" y1="108" x2="102" y2="114"/>
    <text class="pm-ch__cap" x="102" y="128" text-anchor="middle">0,25</text>
    <line class="pm-ch__ax" x1="164" y1="108" x2="164" y2="114"/>
    <text class="pm-ch__cap" x="164" y="128" text-anchor="middle">0,5</text>
    <line class="pm-ch__ax" x1="226" y1="108" x2="226" y2="114"/>
    <text class="pm-ch__cap" x="226" y="128" text-anchor="middle">0,75</text>
    <line class="pm-ch__ax" x1="288" y1="108" x2="288" y2="114"/>
    <text class="pm-ch__cap" x="288" y="128" text-anchor="middle">1</text>
    <line class="pm-ch__ref" x1="40" y1="62" x2="40" y2="108"/>
    <text class="pm-ch__val" x="40" y="54" text-anchor="start">zarda 7</text>
    <line class="pm-ch__ref" x1="81.3" y1="86" x2="81.3" y2="108"/>
    <text class="pm-ch__val" x="81.3" y="78" text-anchor="middle">zarda 6</text>
    <line class="pm-ch__ref" x1="164" y1="62" x2="164" y2="108"/>
    <text class="pm-ch__val" x="164" y="54" text-anchor="middle">tanga — gerb</text>
    <line class="pm-ch__ref" x1="288" y1="86" x2="288" y2="108"/>
    <text class="pm-ch__val" x="288" y="78" text-anchor="end">zar ≤ 6</text>
    <text class="pm-ch__cap" x="40" y="152" text-anchor="start">imkonsiz</text>
    <text class="pm-ch__cap" x="164" y="152" text-anchor="middle">teng ehtimol</text>
    <text class="pm-ch__cap" x="288" y="152" text-anchor="end">aniq</text>
  </svg>
  <figcaption>Zarda 7 tushishi imkonsiz (0), 6 tushishi kam ehtimol,
  tangada gerb — teng ehtimol (0,5), zarda 6 dan katta boʻlmagan son
  esa aniq (1).</figcaption>
</figure>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Shkalaning ikki chekkasi</p>
  <p><b>P = 0</b> — hodisa <b>hech qachon</b> roʻy bermaydi (imkonsiz).
  <br><b>P = 1</b> — hodisa <b>har doim</b> roʻy beradi (aniq).
  <br>Qolgan hamma narsa shu ikkisining orasida.</p>
</div>

<h3>2. Hisoblash: qulay hollarni jamiga boʻlish</h3>

<p>Agar hamma natija <b>teng imkoniyatli</b> boʻlsa — tanga
yasama emas, zar toʻgʻri — ehtimollik oddiy boʻlinma bilan
topiladi.</p>

<div class="pe-ex">
  <p class="pe-ex__math">P(gerb) = 1 ÷ 2 = 0,5 = 50%</p>
  <p class="pe-ex__uz">Tangada ikkita natija bor, gerb esa ulardan
  bittasi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">P(zarda 6) = 1 ÷ 6 ≈ 0,17 ≈ 17%</p>
  <p class="pe-ex__uz">Zarda oltita yoq bor, olti esa bittasi.</p>
  <p class="pe-ex__why">1 ÷ 6 = 0,1666… — bu yerda oʻnlik kasr
  yaxlitlanadi (PM-14), kasr koʻrinishi esa aniq.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">P(zarda juft son) = 3 ÷ 6 = 0,5 = 50%</p>
  <p class="pe-ex__uz">Juft sonlar 2, 4 va 6 — uchtasi qulay hol.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Uch xil libos, bitta son</p>
  <p>Ehtimollikni <b>kasr</b>, <b>oʻnlik kasr</b> yoki <b>foiz</b>
  bilan yozish mumkin — bu PM-22 dagi oʻsha uchlik.
  <sup>1</sup>/<sub>2</sub> = 0,5 = 50%. Masala qaysi koʻrinishni
  soʻrasa, oʻshanisini yozing.</p>
</div>

<h3>3. Imkonsiz va aniq</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Hodisa</th><th>Qulay ÷ jami</th><th>P</th></tr>
  <tr><td>Zarda 7 tushadi</td><td class="pm-word__sym">0 ÷ 6</td>
    <td>0 — imkonsiz</td></tr>
  <tr><td>Zarda 6 tushadi</td><td class="pm-word__sym">1 ÷ 6</td>
    <td>≈ 0,17</td></tr>
  <tr><td>Tangada gerb</td><td class="pm-word__sym">1 ÷ 2</td>
    <td>0,5</td></tr>
  <tr><td>Zarda 6 dan katta boʻlmagan son</td>
    <td class="pm-word__sym">6 ÷ 6</td><td>1 — aniq</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">P hech qachon 1 dan katta boʻlmaydi</p>
  <p>Qulay hollar jami hollardan koʻp boʻlishi mumkin emas — shuning
  uchun boʻlinma ham 1 dan oshmaydi. Agar javobingiz 1,5 yoki 120%
  chiqsa, xato bor: koʻpincha qulay hollar notoʻgʻri sanalgan yoki
  boʻlish teskari qilingan.</p>
</div>

<h3>4. Qaysi hodisa ehtimolliroq?</h3>

<p>Ikki hodisani solishtirish uchun ularning ehtimolligini bir xil
koʻrinishga keltiring.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Zarda 5 yoki 6</p>
    <p>P = 2 ÷ 6 = <sup>1</sup>/<sub>3</sub> ≈ 0,33</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Tangada gerb</p>
    <p>P = 1 ÷ 2 = 0,5</p>
  </div>
</div>

<p>0,5 &gt; 0,33 — demak tangada gerb tushishi ehtimolliroq. Kasrlarni
solishtirish qiyin boʻlsa, ikkalasini oʻnlik kasrga oʻgiring
(PM-22).</p>

<h3>Matnli masala</h3>

<p>Qopchada 10 ta shar bor: 3 tasi qizil, 7 tasi koʻk. Qopchaga
qaramasdan bitta shar olinadi.</p>

<p><b>Qizil shar chiqish ehtimolligi qancha? Va nechta qizil shar
qoʻshilsa, ehtimollik 0,5 boʻladi?</b></p>

<p><b>Reja:</b> avval hozirgi ehtimollikni topamiz. Keyin qizil sharlar
qoʻshilganda ham qulay hollar, ham jami hollar oʻsishini hisobga
olamiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">P(qizil) = 3 ÷ 10 = 0,3 = 30%</span>
    <span class="pm-solve__why">Uchta qulay hol, jami oʻnta</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">P = 0,5 boʻlsin, qizil = koʻk</span>
    <span class="pm-solve__why">Yarmi qizil boʻlishi kerak</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Koʻk sharlar 7 ta, ular oʻzgarmaydi</span>
    <span class="pm-solve__why">Faqat qizil qoʻshiladi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">7 − 3 = 4 ta qizil shar qoʻshiladi</span>
    <span class="pm-solve__why">Shunda 7 qizil va 7 koʻk boʻladi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Qoʻshgandan keyin: 7 qizil, 7 koʻk, jami 14 ta shar.
  <br>P(qizil) = 7 ÷ 14 = 0,5 ✓
  <br><b>Javob:</b> hozir 0,3 (30%); toʻrtta qizil shar qoʻshilsa,
  0,5 boʻladi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">P(zarda 6) = 6</p>
  <p class="pe-fix__good">P = 1 ÷ 6 ≈ 0,17</p>
  <p class="pe-fix__why">Ehtimollik hech qachon 1 dan katta boʻlmaydi.
  6 — bu yoqning raqami, ehtimollik emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">P(zarda juft) = 6 ÷ 3 = 2</p>
  <p class="pe-fix__good">3 ÷ 6 = 0,5</p>
  <p class="pe-fix__why">Boʻlish teskari qilingan. Yuqorida
  <b>qulay</b> hollar, pastda <b>jami</b> hollar turadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Qopchada 3 qizil va 7 koʻk → P(qizil) =
  3 ÷ 7</p>
  <p class="pe-fix__good">3 ÷ 10</p>
  <p class="pe-fix__why">Maxrajda <b>hamma</b> sharlar turadi, faqat
  boshqa rangdagilar emas: 3 + 7 = 10.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">«Ertaga yo yomgʻir yogʻadi, yo yogʻmaydi —
  demak P = 0,5»</p>
  <p class="pe-fix__good">Ikkita natija teng imkoniyatli boʻlgandagina
  0,5</p>
  <p class="pe-fix__why">Formula faqat <b>teng imkoniyatli</b> hollarda
  ishlaydi. Yomgʻir yogʻishi va yogʻmasligi teng imkoniyatli emas —
  buni oʻlchash uchun kuzatuv maʼlumoti kerak.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Tanga tashlandi. Gerb tushish ehtimolligi
  qancha? Uch xil koʻrinishda yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b><sup>1</sup>/<sub>2</sub> = 0,5 = 50%.</b> Ikkita teng
    imkoniyatli natijadan bittasi qulay.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Zar tashlandi. 3 tushish ehtimolligi
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b><sup>1</sup>/<sub>6</sub> ≈ 0,17.</b> Oltita yoqdan
    bittasi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Zarda 4 dan katta son tushish ehtimolligi
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b><sup>1</sup>/<sub>3</sub> ≈ 0,33.</b> Qulay hollar 5 va 6 —
    ikkitasi: 2 ÷ 6 = <sup>1</sup>/<sub>3</sub>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Qopchada 4 ta qizil va 6 ta koʻk shar bor.
  Koʻk shar chiqish ehtimolligi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>0,6 yoki 60%.</b> Jami sharlar: 4 + 6 = 10. Qulay hollar 6 ta:
    6 ÷ 10 = 0,6.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Ehtimolligi 0 va ehtimolligi 1 boʻlgan
  bittadan hodisa ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Masalan:</b> P = 0 — oddiy zarda 7 tushishi (imkonsiz).
    P = 1 — zarda 1 dan 6 gacha boʻlgan sonlardan biri tushishi
    (aniq).</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Qaysi biri ehtimolliroq: zarda juft son
  tushishimi yoki zarda 5 dan kichik son tushishimi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5 dan kichik son.</b> Juft: 2, 4, 6 → 3 ÷ 6 = 0,5. Beshdan
    kichik: 1, 2, 3, 4 → 4 ÷ 6 ≈ 0,67. 0,67 &gt; 0,5.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">7. Lotereyada 20 ta bilet bor, ulardan 5 tasi
  yutuqli. Bitta bilet olindi. Yutish ehtimolligi qancha (foizda)? Va
  yutmaslik ehtimolligi-chi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Yutish 25%, yutmaslik 75%.</b> Yutish: 5 ÷ 20 = 0,25 = 25%.
    Yutuqsiz biletlar 20 − 5 = 15 ta, demak 15 ÷ 20 = 0,75 = 75%.
    Ikkalasining yigʻindisi 100% — bu tasodif emas.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Ehtimollik</b><span>hodisaning roʻy berish imkoniyati oʻlchovi;
    ingl. probability</span></li>
  <li><b>Hodisa</b><span>roʻy berishi mumkin boʻlgan natija; ingl.
    event</span></li>
  <li><b>Qulay hol</b><span>bizni qiziqtirgan natija; ingl. favourable
    outcome</span></li>
  <li><b>Jami hollar</b><span>hamma mumkin boʻlgan natijalar; ingl.
    total outcomes</span></li>
  <li><b>Teng imkoniyatli</b><span>hamma natijaning imkoniyati bir xil;
    ingl. equally likely</span></li>
  <li><b>Imkonsiz hodisa</b><span>P = 0 boʻlgan hodisa; ingl. impossible
    event</span></li>
  <li><b>Aniq hodisa</b><span>P = 1 boʻlgan hodisa; ingl. certain
    event</span></li>
  <li><b>Tasodif</b><span>oldindan aytib boʻlmaydigan natija; ingl.
    chance</span></li>
  <li><b>Shkala</b><span>0 dan 1 gacha boʻlgan oʻlchov chizigʻi; ingl.
    scale</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Ehtimollik har doim 0 bilan 1 orasida.</li>
    <li>P = 0 — imkonsiz, P = 1 — aniq, P = 0,5 — teng ehtimol.</li>
    <li>Teng imkoniyatli hollarda P = qulay ÷ jami.</li>
    <li>Maxrajda hamma natijalar turadi, faqat qolganlari emas.</li>
    <li>Uni kasr, oʻnlik kasr yoki foiz bilan yozish mumkin.</li>
    <li>Formula faqat natijalar teng imkoniyatli boʻlganda
      ishlaydi.</li>
  </ul>
</div>
""",
    },
]
