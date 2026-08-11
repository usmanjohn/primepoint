# -*- coding: utf-8 -*-
"""Prime Math — darslar 13–15 (kvadrat ildiz, yaxlitlash, kasr).

PM-13 va PM-14 Blok A ni yakunlaydi, PM-15 Blok B ni ochadi.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt

Uchta oyoq birga yoziladi:
  mashqlar — practice/management/commands/_practice_pm_13_15.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_13_15.py

⚠️ Kumulyativ:
  • oʻnlik kasr PM-20 da oʻrgatiladi — bu uch darsda vergulli son YOʻQ.
    Shuning uchun PM-13 da √50 ning taqribiy qiymati berilmaydi, faqat u qaysi
    ikki butun son orasida ekani koʻrsatiladi; PM-14 esa faqat butun sonlarni
    yaxlitlaydi.
  • kasrni qisqartirish PM-16 da — PM-15 da 3/6 = 1/2 kabi qisqartirish yoʻq.
  • kasrlarni koʻpaytirish PM-18 da — PM-15 da «sonning kasr qismi» faqat
    boʻlish va koʻpaytirish orqali topiladi (24 ning toʻrtdan biri = 24 ÷ 4).

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_13_15.py --author=prime
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
    # PM-13 — kvadrat ildiz va aniq kvadratlar
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-13: Kvadrat ildiz va aniq kvadratlar",
        "category": "math",
        "order": 13,
        "summary": (
            "Yuzasi maʼlum, tomoni nomaʼlum. Kvadrat ildiz — darajaning teskarisi: "
            "aniq kvadratlar, √ belgisi, ildizni baholash va usta hisobi."
        ),
        "stories": ["Kvadrat maydonning tomoni"],
        "content": """
<h2>PM-13: Kvadrat ildiz va aniq kvadratlar</h2>

<p>Usta hovliga kvadrat shaklidagi supa quradi. Loyihada bitta son yozilgan:
<b>yuzasi 81 m<sup>2</sup></b>. Ammo ustaga yuza kerak emas — unga <b>tomoni</b> kerak,
chunki u ip tortadi, gʻisht sanaydi. Oʻtgan darsda biz tomondan yuzaga borgan edik:
9 × 9 = 81. Endi teskari yoʻlga tushamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>kvadrat ildiz nima ekanini va u nega darajaning teskarisi ekanini bilasiz;</li>
    <li>√ belgisini oʻqiysiz va yozasiz;</li>
    <li>aniq kvadratlarni tanib olasiz (1, 4, 9 … 400);</li>
    <li>aniq boʻlmagan ildizni ikki butun son orasiga joylaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Taʼrif</span>
  <span class="pe-chip pe-chip--o">√a = b</span>
  <span class="pe-op">⟺</span>
  <span class="pe-chip pe-chip--v">b × b = a</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">b manfiy emas</span>
</div>

<h3>1. Teskari savol</h3>

<p>PM-12 da savol bunday edi: «Tomoni 9 boʻlsa, yuzasi qancha?» — 9<sup>2</sup> = 81.
Bugungi savol teskari: «Yuzasi 81 boʻlsa, tomoni qancha?» Javob — <b>9</b>, chunki
aynan 9 ni oʻziga koʻpaytirsak 81 chiqadi. Shu javobni topish amali
<b>kvadrat ildiz chiqarish</b> deyiladi va u shunday yoziladi:</p>

<div class="pe-ex">
  <p class="pe-ex__math"><span class="pm-root">81</span> = 9</p>
  <p class="pe-ex__uz">«Sakson birning kvadrat ildizi toʻqqizga teng.»</p>
  <p class="pe-ex__why">Tekshirish oson: 9 × 9 = 81 ✓ Har bir ildizni shu yoʻl bilan
  bir soniyada tekshirsa boʻladi.</p>
</div>

<figure class="pm-fig">
  <svg viewBox="0 0 340 170" role="img" aria-label="Yuzasi 81 boʻlgan kvadrat">
    <rect class="pm-fill pm-fill--hl" x="40" y="20" width="120" height="120"/>
    <rect class="pm-ln" x="40" y="20" width="120" height="120" fill="none"/>
    <text class="pm-lbl pm-lbl--hl" x="72" y="88">81 m²</text>
    <text class="pm-lbl" x="92" y="158">? m</text>
    <text class="pm-lbl" x="14" y="85">? m</text>
    <text class="pm-lbl" x="185" y="70">yuza berilgan</text>
    <text class="pm-lbl pm-lbl--hl" x="185" y="100">tomon izlanmoqda</text>
  </svg>
  <figcaption>Daraja tomondan yuzaga olib boradi, ildiz esa yuzadan tomonga qaytaradi.</figcaption>
</figure>

<h3>2. Aniq kvadratlar</h3>

<p>Ildizi butun son chiqadigan sonlar <b>aniq kvadratlar</b> deyiladi. Ular PM-12 dagi
jadvalning oʻzi, faqat teskari tomondan oʻqiladi.</p>

<div class="pe-table-wrap"><table>
  <tr><th>n</th><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td>
      <td>7</td><td>8</td><td>9</td><td>10</td></tr>
  <tr><th>n<sup>2</sup></th><td>1</td><td>4</td><td>9</td><td>16</td><td>25</td>
      <td>36</td><td>49</td><td>64</td><td>81</td><td>100</td></tr>
</table></div>

<p>Roʻyxat shu yerda tugamaydi. Keyingi oʻntasi ham koʻp kerak boʻladi:</p>

<div class="pe-table-wrap"><table>
  <tr><th>n</th><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td>
      <td>17</td><td>18</td><td>19</td><td>20</td></tr>
  <tr><th>n<sup>2</sup></th><td>121</td><td>144</td><td>169</td><td>196</td><td>225</td>
      <td>256</td><td>289</td><td>324</td><td>361</td><td>400</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Bir qarashda tanish</p>
  <p>Aniq kvadratning oxirgi raqami hech qachon <b>2, 3, 7 yoki 8</b> boʻlmaydi. Demak
  4 372 ni koʻrsangiz — hisoblamasdan bilasiz: bu aniq kvadrat emas.</p>
</div>

<h3>3. Nollar bilan ishlash</h3>

<p>Oʻnning darajalari ildiz ostida ham chiroyli ishlaydi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">√100 = 10</span>
    <span class="pm-solve__why">Ikkita nol — ildizda bitta nol</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">√900 = 30</span>
    <span class="pm-solve__why">9 → 3, keyin bitta nol</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">√10 000 = 100</span>
    <span class="pm-solve__why">Toʻrtta nol — ildizda ikkita nol</span>
  </div>
</div>

<p>Sabab oddiy: 30 × 30 = 900, ikkita oʻnlik koʻpaytirilganda bitta yuzlik hosil
boʻladi. Shuning uchun ildiz nollarni <b>ikkitadan bittaga</b> qisqartiradi.</p>

<h3>4. Ildiz aniq chiqmasa</h3>

<p>Har qanday son aniq kvadrat emas. Masalan, √50 ni butun son bilan yozib boʻlmaydi.
Bunday holda uni <b>ikki butun son orasiga</b> joylaymiz — bu maktabda ham,
hayotda ham koʻpincha yetarli.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">√50 = ?</span>
    <span class="pm-solve__why">Aniq kvadrat emas</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">49 &lt; 50 &lt; 64</span>
    <span class="pm-solve__why">Eng yaqin aniq kvadratlar</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">7 &lt; √50 &lt; 8</span>
    <span class="pm-solve__why">Va 50 aynan 49 ga yaqin — javob 7 ga yaqin</span>
  </div>
</div>

<div class="pm-num">
  <div class="pm-num__track">
    <span class="pm-num__band" style="left:0%;width:20%"></span>
    <span class="pm-num__tick" style="left:0%"><i>√49 = 7</i></span>
    <span class="pm-num__tick" style="left:100%"><i>√64 = 8</i></span>
    <span class="pm-num__dot" style="left:20%"><i>√50</i></span>
  </div>
</div>

<h3>5. Ildiz — qavs kabi</h3>

<p>Ildiz belgisining ostidagi hamma narsa <b>avval</b> hisoblanadi, xuddi qavs
ichidagidek.</p>

<div class="pe-ex">
  <p class="pe-ex__math">√(16 × 9) = √144 = 12</p>
  <p class="pe-ex__uz">Avval ildiz ostini hisobladik, keyin ildiz chiqardik.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">√36 + √9 = 6 + 3 = 9</p>
  <p class="pe-ex__uz">Bu yerda ikkita alohida ildiz bor — har birini alohida
  hisoblaymiz, keyin qoʻshamiz.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Eng koʻp uchraydigan xato</p>
  <p><b>√(9 + 16) — bu √9 + √16 emas!</b><br>
  Chapdagi: √(9 + 16) = √25 = <b>5</b>.<br>
  Oʻngdagi: 3 + 4 = <b>7</b>.<br>
  Ildiz qoʻshishni «ichkariga kiritmaydi». Avval ildiz ostini yigʻing, keyin ildiz
  chiqaring.</p>
</div>

<h3>6. Matnli masala</h3>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Masala</p>
  <p>Fermerning kvadrat shaklidagi yeri bor, yuzasi <b>225 m<sup>2</sup></b>. U yerning
  atrofini panjara bilan oʻrab chiqmoqchi. Panjaraning har metri <b>25 000 soʻm</b>
  turadi. Panjaraga qancha pul ketadi?</p>
</div>

<p><b>Nima soʻralyapti?</b> Umumiy narx. <b>Reja:</b> yuzadan tomonni topamiz (ildiz),
tomondan perimetrni (4 marta), perimetrdan narxni (koʻpaytirish).</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">√225 = 15 m</span>
    <span class="pm-solve__why">Kvadratning tomoni: 15 × 15 = 225 ✓</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4 × 15 = 60 m</span>
    <span class="pm-solve__why">Kvadratning toʻrtta tomoni teng — perimetr</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">60 × 25 000 = 1 500 000 soʻm</span>
    <span class="pm-solve__why">Har metr 25 000 soʻmdan</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Boshqa yoʻl: bir tomon 15 × 25 000 = 375 000 soʻm turadi. Toʻrtta tomon:
  4 × 375 000 = <b>1 500 000</b> soʻm ✓</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>60 metrga yaqin panjara, har metri 25 000 dan — 60 × 25 000, yaʼni taxminan
  bir yarim million. Javob shu darajada.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">√36 = 18</p>
  <p class="pe-fix__good">√36 = 6</p>
  <p class="pe-fix__why">Ildiz — yarmini olish emas. 6 × 6 = 36 boʻlgani uchun javob 6.
  18 × 18 esa 324 chiqadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">√(9 + 16) = 3 + 4 = 7</p>
  <p class="pe-fix__good">√(9 + 16) = √25 = 5</p>
  <p class="pe-fix__why">Ildiz belgisi qavs vazifasini bajaradi: avval ichkarisi
  hisoblanadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">√400 = 200</p>
  <p class="pe-fix__good">√400 = 20</p>
  <p class="pe-fix__why">Nollar ikkitadan bittaga qisqaradi: 20 × 20 = 400.
  200 × 200 esa 40 000 boʻlardi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. √64 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>8.</b> 8 × 8 = 64.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. √121 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>11.</b> 11 × 11 = 121 — jadvalning oʻn birinchi qatori.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. √(25 × 4) = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>10.</b> Avval ildiz ostini hisoblaymiz: 25 × 4 = 100. Keyin √100 = 10.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. √30 qaysi ikki butun son orasida?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5 va 6 orasida.</b> 25 &lt; 30 &lt; 36, demak 5 &lt; √30 &lt; 6. 30 soni
    36 dan koʻra 25 ga yaqinroq, shuning uchun javob 5 ga yaqinroq.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Kvadrat shaklidagi xonaning poliga 196 ta kvadrat plitka
  terildi va ular xonani toʻliq qopladi. Bir qatorda nechta plitka bor?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>14 ta.</b> Plitkalar kvadrat shaklida terilgan, demak qatorlar soni va bir
    qatordagi plitkalar soni teng: √196 = 14, chunki 14 × 14 = 196.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Kvadrat ildiz</b><span>oʻziga koʻpaytirilganda berilgan sonni beradigan
    manfiy boʻlmagan son; ingl. square root</span></li>
  <li><b>Ildiz ostidagi ifoda</b><span>√ belgisi ostida turgan son yoki hisob;
    ingl. radicand</span></li>
  <li><b>Aniq kvadrat</b><span>butun sonning kvadrati boʻlgan son; ingl. perfect
    square</span></li>
  <li><b>Daraja</b><span>takroriy koʻpaytirish yozuvi; ingl. power</span></li>
  <li><b>Teskari amal</b><span>bajarilgan amalni bekor qiladigan amal;
    ingl. inverse operation</span></li>
  <li><b>Yuza</b><span>shakl ichidagi joy oʻlchovi; ingl. area</span></li>
  <li><b>Perimetr</b><span>shakl chegarasining umumiy uzunligi; ingl. perimeter</span></li>
  <li><b>Tomon</b><span>koʻpburchakning bir cheti; ingl. side</span></li>
  <li><b>Baholash</b><span>aniq javob oʻrniga uning qaysi oraliqda ekanini aytish;
    ingl. estimation</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Ildiz — darajaning teskarisi.</b> √a = b degani b × b = a degani, va javobni
      har doim koʻpaytirib tekshirish mumkin.</li>
    <li><b>Aniq kvadratlarni yodda tuting</b> — 1 dan 400 gacha yigirmata son butun
      maktabga yetadi.</li>
    <li><b>Ildiz qavs kabi ishlaydi:</b> √(9 + 16) = 5, √9 + √16 esa 7. Ular teng emas.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-14 — yaxlitlash va taqribiy hisob
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-14: Yaxlitlash va taqribiy hisob — «javob mantiqiymi?»",
        "category": "math",
        "order": 14,
        "summary": (
            "Bozorda kalkulyator yoʻq. Yaxlitlash qoidasi, ogʻzaki taxmin va imtihonda "
            "eng koʻp ball qutqaradigan odat: javobning kattaligini tekshirish."
        ),
        "stories": ["Buvijonning bozordagi taxmini"],
        "content": """
<h2>PM-14: Yaxlitlash va taqribiy hisob — «javob mantiqiymi?»</h2>

<p>Buvijon bozorda uch narsa oldi: <b>3 800</b>, <b>2 100</b> va <b>1 450</b> soʻmlik.
Sotuvchi hisoblab ulgurmasidan, buvijon hamyonini ochib qoʻydi: «Yetti mingdan sal
oshadi». U hech narsani daftarga yozmadi, kalkulyator ham ishlatmadi. U shunchaki
<b>yaxlitladi</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>sonni oʻnlik, yuzlik va mingliklarga yaxlitlaysiz;</li>
    <li>ogʻzaki taxmin qilib, javobni oldindan bilasiz;</li>
    <li>«javob mantiqiymi?» degan savolni har hisobdan keyin berishni odat qilasiz;</li>
    <li>yaxlitlashda qilinadigan ikki asosiy xatodan qutulasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Yaxlitlash qoidasi</span>
  <span class="pe-chip pe-chip--s">keyingi raqamga qara</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">0, 1, 2, 3, 4 → pastga</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">5, 6, 7, 8, 9 → yuqoriga</span>
</div>

<h3>1. Qaysi razryadga yaxlitlaymiz?</h3>

<p>Yaxlitlashdan oldin doim bitta savol beriladi: <b>qaysi razryadgacha?</b> Javob
shunga qarab oʻzgaradi. Keyin faqat <b>bitta</b> raqamga — undan keyingisiga —
qaraladi.</p>

<div class="pe-table-wrap"><table>
  <tr><th>Son</th><th>Razryad</th><th>Qaysi raqamga qaraymiz</th><th>Natija</th></tr>
  <tr><td>3 472</td><td>oʻnliklar</td><td>2 (birlik)</td><td>3 470</td></tr>
  <tr><td>3 472</td><td>yuzliklar</td><td>7 (oʻnlik)</td><td>3 500</td></tr>
  <tr><td>3 472</td><td>mingliklar</td><td>4 (yuzlik)</td><td>3 000</td></tr>
</table></div>

<p>Bitta sondan uchta turli javob chiqdi — va uchalasi ham toʻgʻri. Chunki savol har
safar boshqacha edi.</p>

<div class="pm-num">
  <div class="pm-num__track">
    <span class="pm-num__band" style="left:0%;width:47%"></span>
    <span class="pm-num__tick" style="left:0%"><i>3 000</i></span>
    <span class="pm-num__tick" style="left:50%"><i>3 500</i></span>
    <span class="pm-num__tick" style="left:100%"><i>4 000</i></span>
    <span class="pm-num__dot" style="left:47%"><i>3 472</i></span>
  </div>
</div>

<p>Son oʻqi qoidani koʻrsatib turibdi: 3 472 mingliklar orasida <b>3 000 ga yaqinroq</b>
turibdi, shuning uchun mingliklarga yaxlitlanganda 3 000 boʻladi. Yaxlitlash — aslida
«qaysi belgiga yaqinroq turibsan?» degan savol.</p>

<h3>2. Ikkita jiddiy xato</h3>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Xato 1 — ketma-ket yaxlitlash</p>
  <p><b>2 449</b> ni yuzliklarga yaxlitlaymiz. Baʼzi oʻquvchilar zinapoyadan
  koʻtariladi: avval 2 449 → 2 450, keyin 2 450 → 2 500. Bu <b>notoʻgʻri</b>.<br>
  Yuzliklarga yaxlitlaganda faqat <b>oʻnliklar raqamiga</b> qaraladi, u esa 4 —
  demak pastga: <b>2 400</b>.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Xato 2 — beshni pastga tushirish</p>
  <p><b>6 500</b> ni mingliklarga yaxlitlasak, 6 000 emas, <b>7 000</b> boʻladi.
  Maktab qoidasi qatʼiy: 5 ham yuqoriga koʻtariladi.</p>
</div>

<h3>3. Taqribiy hisob — bozor matematikasi</h3>

<p>Yaxlitlashning asosiy foydasi — <b>ogʻzaki hisob</b>. Aniq javob keyin ham
topiladi, lekin taxmin darrov kerak: pul yetadimi, avtobusga ulguramizmi, buyurtma
sigʻadimi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 800 + 2 100 + 1 450</span>
    <span class="pm-solve__why">Buvijonning xaridi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">≈ 4 000 + 2 000 + 1 000</span>
    <span class="pm-solve__why">Har birini mingliklarga yaxlitladik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">≈ 7 000 soʻm</span>
    <span class="pm-solve__why">Ogʻzaki, bir soniyada</span>
  </div>
</div>

<p>Aniq javob esa <b>7 350</b> soʻm. Taxmin 350 soʻmga farq qildi — hamyondagi pul
yetishini bilish uchun bu mutlaqo yetarli.</p>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Belgi</p>
  <p>Taxminiy javob <b>≈</b> belgisi bilan yoziladi, tenglik belgisi bilan emas:
  198 × 4 <b>≈</b> 800. Aniq javob esa 792.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">198 × 4 ≈ 200 × 4 = 800</p>
  <p class="pe-ex__uz">198 ni 200 ga yaxlitladik — hisob bir zumda bajarildi.</p>
  <p class="pe-ex__why">Biz 2 tadan koʻp oldik, har biri 4 marta takrorlandi, demak
  taxmin aniq javobdan 8 taga katta: 800 − 8 = 792.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">1 234 ÷ 6 ≈ 1 200 ÷ 6 = 200</p>
  <p class="pe-ex__uz">Boʻlishda qulay sonni tanlaymiz: 1 200 oltiga butun boʻlinadi.</p>
</div>

<h3>4. «Javob mantiqiymi?»</h3>

<p>Bu darsning eng foydali odati. Har qanday hisobdan keyin javobga qarab, uning
<b>kattaligi</b> toʻgʻrimi deb soʻrang. Bir soniyalik tekshiruv oʻnlab xatoni
ushlaydi.</p>

<div class="pe-table-wrap"><table>
  <tr><th>Javob</th><th>Mantiqiymi?</th><th>Nega</th></tr>
  <tr><td>Non 45 000 000 soʻm</td><td>Yoʻq</td><td>Razryad adashgan — nollar ortiqcha</td></tr>
  <tr><td>Oʻquvchi boʻyi 17 m</td><td>Yoʻq</td><td>Birlik adashgan: 17 m emas, 170 sm</td></tr>
  <tr><td>Piyoda tezligi 90 km/soat</td><td>Yoʻq</td><td>Bu mashina tezligi</td></tr>
  <tr><td>Sinfda 28 oʻquvchi</td><td>Ha</td><td>Kutilgan darajada</td></tr>
</table></div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Imtihonda vaqt kam boʻlsa ham, taxminga 5 soniya ajrating. Javobingiz taxmindan
  10 barobar farq qilsa — deyarli har doim razryad yoki birlikda xato bor.</span>
</div>

<h3>5. Matnli masala</h3>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Masala</p>
  <p>7-sinfning <b>38 oʻquvchisi</b> ekskursiyaga chiqmoqchi. Avtobus
  <b>1 900 000 soʻm</b>, har bir oʻquvchining ovqati <b>25 000 soʻm</b>, muzey
  chiptasi esa <b>12 000 soʻm</b>. Har bir oʻquvchi qancha pul olib kelishi kerak?</p>
</div>

<p><b>Avval taxmin qilamiz.</b> 38 ≈ 40 deb olaylik: avtobus ≈ 2 000 000, ovqat
≈ 40 × 25 000 = 1 000 000, muzey ≈ 40 × 12 000 = 480 000. Jami ≈ 3 480 000 soʻm,
bir kishiga ≈ 3 480 000 ÷ 40 ≈ 87 000 soʻm. <b>Endi aniq hisoblaymiz.</b></p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">38 × 25 000 = 950 000</span>
    <span class="pm-solve__why">Hamma oʻquvchining ovqati</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">38 × 12 000 = 456 000</span>
    <span class="pm-solve__why">Hamma chiptalar</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">1 900 000 + 950 000 + 456 000 = 3 306 000</span>
    <span class="pm-solve__why">Umumiy xarajat</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3 306 000 ÷ 38 = 87 000 soʻm</span>
    <span class="pm-solve__why">Har bir oʻquvchiga</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>38 × 87 000 = 3 306 000 ✓ Taxminimiz 87 000 atrofida edi — mos keldi.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Diqqat</p>
  <p>Taxmin <b>87 000 dan sal koʻproq</b> chiqishi kerak edi, chunki biz oʻquvchilar
  sonini ham, avtobus narxini ham yuqoriga yaxlitlagandik. Aniq javob shu tomonda —
  demak hisobimizda katta xato yoʻq.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">2 449 → 2 500 (yuzliklarga)</p>
  <p class="pe-fix__good">2 449 → 2 400</p>
  <p class="pe-fix__why">Faqat oʻnliklar raqamiga (4 ga) qaraladi. Avval 2 450 ga
  yaxlitlab, keyin yana yaxlitlash — ketma-ket yaxlitlash xatosi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">6 500 → 6 000</p>
  <p class="pe-fix__good">6 500 → 7 000</p>
  <p class="pe-fix__why">5 raqami yuqoriga koʻtariladi. «Oʻrtada turibdi, pastga
  tushiraman» degan tanlov qoidada yoʻq.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">198 × 4 = 800</p>
  <p class="pe-fix__good">198 × 4 ≈ 800, aniq javob 792</p>
  <p class="pe-fix__why">Taxminni javob deb yozib boʻlmaydi. Taxmin — tekshiruv
  vositasi, natija emas.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 3 748 ni yuzliklarga yaxlitlang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3 700.</b> Oʻnliklar raqami 4 — pastga tushamiz. Diqqat: 8 raqamiga
    qaralmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 8 500 ni mingliklarga yaxlitlang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>9 000.</b> Yuzliklar raqami 5 — yuqoriga koʻtariladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 497 × 6 ni ogʻzaki baholang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>≈ 3 000.</b> 497 ≈ 500, 500 × 6 = 3 000. Aniq javob 2 982 — taxmin 18 taga
    katta, chunki har bir 497 ni 3 taga oshirgandik: 3 × 6 = 18.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Oʻquvchi masalani yechib, sinfdagi partalar sonini
  <b>4 200</b> ta deb topdi. Javob mantiqiymi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Yoʻq.</b> Bitta sinfda 15–20 ta parta boʻladi. 4 200 — butun bir shaharning
    partalari. Deyarli aniq razryad xatosi: javob 42 boʻlishi kerak edi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Doʻkonda daftar 2 800 soʻm turadi. Sherbek 12 ta daftar
  olmoqchi va choʻntagida 30 000 soʻm bor. Puli yetadimi? Avval taxmin qiling, keyin
  aniq hisoblang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Yetmaydi.</b> Taxmin: 2 800 ≈ 3 000, 3 000 × 12 = 36 000 — 30 000 dan
    koʻp. Aniq hisob: 2 800 × 12 = 33 600 soʻm. Sherbekka yana 3 600 soʻm kerak.
    Diqqat qiling: taxmin yuqoriga chiqarilgan boʻlsa ham, aniq javob baribir
    30 000 dan katta — demak xulosa ishonchli.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Yaxlitlash</b><span>sonni yaqin yumaloq songa almashtirish;
    ingl. rounding</span></li>
  <li><b>Taqribiy qiymat</b><span>aniq emas, lekin yetarlicha yaqin javob;
    ingl. approximate value</span></li>
  <li><b>Razryad</b><span>raqamning sondagi oʻrni: birlik, oʻnlik, yuzlik;
    ingl. place value</span></li>
  <li><b>Baholash</b><span>hisoblashdan oldin javobning kattaligini aytish;
    ingl. estimation</span></li>
  <li><b>Ogʻzaki hisob</b><span>qogʻozsiz, xayolan bajariladigan hisob;
    ingl. mental arithmetic</span></li>
  <li><b>Xatolik</b><span>taxmin bilan aniq javob orasidagi farq; ingl. error</span></li>
  <li><b>Taxminan (≈)</b><span>«teng» emas, «yaqin» degan belgi;
    ingl. approximately</span></li>
  <li><b>Aniq javob</b><span>toʻliq hisoblangan natija; ingl. exact answer</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Faqat bitta raqamga qarang</b> — yaxlitlanayotgan razryaddan keyingisiga.
      Ketma-ket yaxlitlash xato javob beradi.</li>
    <li><b>5 har doim yuqoriga.</b></li>
    <li><b>Har javobdan keyin soʻrang: «mantiqiymi?»</b> Taxmin bilan javob 10 barobar
      farq qilsa, xato bor.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-15 — kasr nima
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-15: Kasr nima: butunning boʻlagi",
        "category": "math",
        "order": 15,
        "summary": (
            "Bitta non, olti kishi — har kimga qancha? Surat va maxraj, teng boʻlaklar "
            "sharti, kasrni son oʻqida koʻrish va sonning kasr qismini topish."
        ),
        "stories": ["Bitta non, olti kishi"],
        "content": """
<h2>PM-15: Kasr nima: butunning boʻlagi</h2>

<p>Dasturxonda olti kishi oʻtiribdi, oldilarida bitta non. Boʻlishish kerak. Bu yerda
butun sonlar yetmay qoladi: har kimga «bir» ham, «nol» ham tegmaydi. Javob ikkalasining
orasida turibdi. Shu oraliqni yozish uchun matematikada <b>kasr</b> bor. Bugundan
boshlab kursning yangi boʻlimi — kasrlar dunyosi — ochiladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>surat va maxrajni farqlaysiz va nima uchun kerakligini bilasiz;</li>
    <li>boʻlaklar <b>teng</b> boʻlishi shartligini tushunasiz;</li>
    <li>kasrni son oʻqida koʻrasiz;</li>
    <li>sonning kasr qismini topasiz: 24 ning toʻrtdan uchi qancha?</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Kasrning ikki qavati</span>
  <span class="pe-chip pe-chip--s">surat — nechtasini oldik</span>
  <span class="pe-op">/</span>
  <span class="pe-chip pe-chip--o">maxraj — nechta teng boʻlakka boʻlindi</span>
</div>

<h3>1. Ikki qavatli son</h3>

<p>Nonni olti teng boʻlakka boʻldik va bittasini oldik. Buni shunday yozamiz:</p>

<div class="pe-ex">
  <p class="pe-ex__math"><span class="pm-frac pm-frac--big"><span class="pm-frac__n">1</span><span class="pm-frac__d">6</span></span></p>
  <p class="pe-ex__uz">«Oltidan bir». Pastdagi 6 — non nechta boʻlakka boʻlingani,
  yuqoridagi 1 — bizga nechtasi tekkani.</p>
</div>

<p>Pastdagi son — <b>maxraj</b>. U boʻlakning <i>kattaligini</i> belgilaydi. Yuqoridagi
son — <b>surat</b>. U boʻlaklar <i>sonini</i> aytadi. Maxraj oʻzgarsa, boʻlakning
oʻzi oʻzgaradi; surat oʻzgarsa, faqat nechtasi olingani oʻzgaradi.</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">Butun non</span>
    <span class="pm-model__bar" style="width:96%">1</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">Bir boʻlak</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:16%">1/6</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">Uch boʻlak</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:48%">3/6</span>
  </div>
  <p class="pm-model__tot">Olti boʻlakning hammasi — yana butun non</p>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Qoida</p>
  <p>Surat maxrajga teng boʻlsa, kasr <b>butunga</b> teng:
  6/6 = 1, 8/8 = 1, 100/100 = 1. Chunki hamma boʻlaklar yigʻilsa, butun qaytadi.</p>
</div>

<h3>2. Boʻlaklar teng boʻlishi SHART</h3>

<p>Nonni koʻz bilan chamalab, katta-kichik boʻlaklarga boʻlsangiz — bu kasr emas.
Kasrning butun mantigʻi <b>teng boʻlish</b>ga tayanadi.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">✅ Kasr</p>
    <p>Non oltita <b>teng</b> boʻlakka boʻlindi. Har biri — 1/6, va har kimga bir xil
    ulush tegadi.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">❌ Kasr emas</p>
    <p>Non oltita <b>har xil</b> boʻlakka boʻlindi. Boʻlaklar teng emas, shuning uchun
    «oltidan bir» degan nom ularga toʻgʻri kelmaydi.</p>
  </div>
</div>

<h3>3. Qanday oʻqiladi</h3>

<p>Oʻzbek tilida kasr <b>pastdan yuqoriga</b> oʻqiladi: avval maxraj, keyin surat.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Yozuv</th><th>Oʻqilishi</th><th>Maʼnosi</th></tr>
  <tr><td>1/2</td><td class="pm-word__sym">ikkidan bir</td><td>yarmi</td></tr>
  <tr><td>1/4</td><td class="pm-word__sym">toʻrtdan bir</td><td>chorak</td></tr>
  <tr><td>3/4</td><td class="pm-word__sym">toʻrtdan uch</td><td>uchta chorak</td></tr>
  <tr><td>2/5</td><td class="pm-word__sym">beshdan ikki</td><td>besh boʻlakdan ikkitasi</td></tr>
</table></div>

<h3>4. Kasr son oʻqida</h3>

<p>Kasrlar sonlar orasidagi boʻsh joyni toʻldiradi. 0 bilan 1 orasi endi boʻsh emas.</p>

<div class="pm-num">
  <div class="pm-num__track">
    <span class="pm-num__band" style="left:0%;width:75%"></span>
    <span class="pm-num__tick" style="left:0%"><i>0</i></span>
    <span class="pm-num__tick" style="left:25%"><i>1/4</i></span>
    <span class="pm-num__tick" style="left:50%"><i>2/4</i></span>
    <span class="pm-num__tick" style="left:75%"><i>3/4</i></span>
    <span class="pm-num__tick" style="left:100%"><i>1</i></span>
  </div>
</div>

<p>Chiziq toʻrtta teng boʻlakka boʻlindi — xuddi nonday. 3/4 nuqtasi 1 ga yaqin, 1/4
esa 0 ga yaqin. Kasrni <b>joy</b> deb koʻrish uni taqqoslashni osonlashtiradi.</p>

<h3>5. Maxraj katta — boʻlak kichik</h3>

<p>Bu darsning eng kutilmagan qismi. Odatda katta son «koʻproq» degani, kasrda esa
teskarisi ishlaydi.</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">1/2</span>
    <span class="pm-model__bar" style="width:50%">yarmi</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">1/4</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:25%">choragi</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">1/8</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:12%">sakkizdan bir</span>
  </div>
  <p class="pm-model__tot">Maxraj oshgani sari boʻlak kichrayadi</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Nega shunday?</p>
  <p>Bitta tortni <b>2</b> kishiga boʻlsangiz, ulush katta. Xuddi shu tortni
  <b>8</b> kishiga boʻlsangiz, ulush kichkina. Kishilar koʻp — boʻlak kichik. Shuning
  uchun <b>1/8 &lt; 1/6 &lt; 1/4 &lt; 1/2</b>.</p>
  <p>Suratlar teng boʻlganda esa qoida oddiy: maxraji kichik kasr kattaroq.</p>
</div>

<p>Maxrajlar bir xil boʻlsa, taqqoslash butunlay oson boʻladi — boʻlaklar bir xil,
faqat sonini solishtiramiz: <b>3/7 &lt; 5/7</b>.</p>

<h3>6. Sonning kasr qismini topish</h3>

<p>Amalda eng koʻp kerak boʻladigan koʻnikma shu. Ikki qadamda bajariladi:</p>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki qadam</span>
  <span class="pe-chip pe-chip--v">1. maxrajga boʻl</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">2. suratga koʻpaytir</span>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">24 ning 3/4 qismi</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">24 ÷ 4 = 6</span>
    <span class="pm-solve__why">Bitta chorak nechta ekanini topdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">6 × 3 = 18</span>
    <span class="pm-solve__why">Uchta chorak kerak edi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Toʻrtta chorak butunni berishi kerak: 6 × 4 = 24 ✓ Va 18 soni 24 dan kichik —
  toʻgʻri, chunki 3/4 butundan kam.</p>
</div>

<h3>7. Matnli masala</h3>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Masala</p>
  <p>Sinfda <b>30 oʻquvchi</b> bor. Ularning <b>2/5</b> qismi sport toʻgaragiga
  qatnaydi. Nechta oʻquvchi sport toʻgaragiga bormaydi?</p>
</div>

<p><b>Diqqat:</b> savol qatnaydiganlar haqida emas, <b>qatnamaydiganlar</b> haqida.
Matnli masalada eng koʻp ball shu joyda yoʻqoladi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">30 ÷ 5 = 6</span>
    <span class="pm-solve__why">Beshdan bir qism — 6 oʻquvchi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">6 × 2 = 12</span>
    <span class="pm-solve__why">Beshdan ikki qism — 12 oʻquvchi qatnaydi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">30 − 12 = 18 oʻquvchi</span>
    <span class="pm-solve__why">Qolganlari qatnamaydi — soʻralgani shu</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Ikkinchi yoʻl</p>
  <p>Butun sinf — 5/5. Qatnaydiganlar 2/5, demak qatnamaydiganlar 3/5.
  30 ÷ 5 = 6, keyin 6 × 3 = <b>18</b>. Xuddi shu javob, bitta amal kamroq.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">1/8 &gt; 1/6, chunki 8 &gt; 6</p>
  <p class="pe-fix__good">1/8 &lt; 1/6</p>
  <p class="pe-fix__why">Maxraj boʻlakning kattaligini belgilaydi. Nonni sakkizga
  boʻlsangiz, boʻlak oltiga boʻlgandan kichik chiqadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">«Beshdan ikki» → 5/2</p>
  <p class="pe-fix__good">«Beshdan ikki» → 2/5</p>
  <p class="pe-fix__why">Oʻqilishida maxraj oldin aytiladi, yozuvda esa u pastda
  turadi. Avval «nechta boʻlakka» — pastga, keyin «nechtasi» — yuqoriga.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Nonni koʻz bilan boʻlib, «bu 1/6» deyish</p>
  <p class="pe-fix__good">Avval teng boʻlish, keyin nomlash</p>
  <p class="pe-fix__why">Teng boʻlmagan boʻlaklarga kasr nomi berilmaydi. Teng
  boʻlish — kasrning asosiy sharti.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 3/8 kasrida maxraj qaysi son va u nimani bildiradi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>8 — maxraj.</b> U butun sakkizta teng boʻlakka boʻlinganini bildiradi.
    3 esa surat: shu boʻlaklardan uchtasi olingan.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 1/3 va 1/5 dan qaysi biri katta?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>1/3.</b> Uchga boʻlingan boʻlak beshga boʻlingandan katta — kishilar kam
    boʻlsa, ulush katta boʻladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 7/7 nimaga teng?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>1 ga.</b> Yettita boʻlakning hammasi yigʻilsa, butun qaytadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 45 ning 2/9 qismi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>10.</b> 45 ÷ 9 = 5 (toʻqqizdan bir qism), keyin 5 × 2 = 10. Tekshiruv:
    5 × 9 = 45 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Buvijon 36 ta somsa pishirdi. Uning 1/4 qismini qoʻshnilarga
  berdi, 1/3 qismini esa nabiralari yedi. Nechta somsa qoldi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>15 ta.</b> Qoʻshnilarga: 36 ÷ 4 = 9 ta. Nabiralarga: 36 ÷ 3 = 12 ta.
    Ketgani 9 + 12 = 21 ta. Qolgani 36 − 21 = 15 ta. Javob mantiqiy: yarmidan sal
    kamrogʻi qolgan.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Kasr</b><span>butunning teng boʻlaklaridan biri yoki bir nechtasi;
    ingl. fraction</span></li>
  <li><b>Surat</b><span>kasrning yuqorigi soni — nechta boʻlak olingani;
    ingl. numerator</span></li>
  <li><b>Maxraj</b><span>kasrning pastki soni — nechta teng boʻlakka boʻlingani;
    ingl. denominator</span></li>
  <li><b>Butun</b><span>boʻlinmagan bir dona; ingl. whole</span></li>
  <li><b>Teng boʻlaklar</b><span>bir xil kattalikdagi qismlar; ingl. equal parts</span></li>
  <li><b>Yarim</b><span>1/2 qism; ingl. half</span></li>
  <li><b>Chorak</b><span>1/4 qism; ingl. quarter</span></li>
  <li><b>Birlik kasr</b><span>surati 1 boʻlgan kasr: 1/3, 1/8; ingl. unit
    fraction</span></li>
  <li><b>Taqqoslash</b><span>qaysi biri katta yoki kichikligini aniqlash;
    ingl. comparison</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Maxraj — boʻlakning kattaligi, surat — boʻlaklar soni.</b> Pastdagi son
      butun nechaga boʻlinganini aytadi.</li>
    <li><b>Maxraj katta boʻlsa, boʻlak kichik:</b> 1/8 &lt; 1/6 &lt; 1/4 &lt; 1/2.</li>
    <li><b>Kasr qismini topish — ikki qadam:</b> maxrajga boʻl, suratga koʻpaytir.</li>
  </ul>
</div>
""",
    },
]
