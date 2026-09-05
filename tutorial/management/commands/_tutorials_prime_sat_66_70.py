# -*- coding: utf-8 -*-
"""Prime SAT Math — lessons 66–70 (Blok D boshlanadi: geometriya).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_SAT.md
Lesson list: tutorial/management/commands/toc_prime_sat_math.txt

⚠️ SARLAVHALAR BAZADAN OLINGAN, aynan.

⚠️ BLOK D QOIDASI (toc header): har bir darsda FORMULA VARAGʻIDA NIMA BOR va
   NIMA YOʻQ aytilishi shart. Bu blokdagi eng koʻp yoʻqotiladigan ball —
   varaqda bor formulani yodlashga vaqt sarflash yoki unda YOʻQ formulani
   varaqdan izlash.

⚠️ Kumulyativ (SAT-1…65 erkin). Blok D da chizmalar inline SVG — hech qachon
   rasm fayli emas.
  • SAT-66 — vertikal, qoʻshni va toʻldiruvchi burchaklar (varaqda YOʻQ).
  • SAT-67 — parallel chiziqlar va kesuvchi (varaqda YOʻQ).
  • SAT-68 — uchburchak burchaklari yigʻindisi (VARAQDA BOR) va tashqi
    burchak teoremasi (varaqda YOʻQ).
  • SAT-69 — teng yonli va teng tomonli uchburchak (varaqda YOʻQ).
  • SAT-70 — Pifagor teoremasi (VARAQDA BOR) va masofa formulasi (YOʻQ).
  • ⛔ Maxsus uchburchaklar (SAT-71, 72) YOʻQ; trigonometriya (SAT-75) YOʻQ.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_sat_66_70.py \\
        --author=prime --republish
"""

PLAYLIST = {
    "title": "Prime SAT Math",
    "category": "math",
    "description": (
        "Digital SAT matematikasi noldan — 100 dars. Savollar ingliz tilida, "
        "chunki test shunday; tushuntirish oʻzbek tilida, chunki oʻqituvchi shunday. "
        "Har bir darsda haqiqiy SAT savollari, tuzoq javoblar va 20 savollik mashq."
    ),
}

TUTORIALS = [

    # ══════════════════════════════════════════════════════════════════
    # SAT-66 — lines and angles
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-66: Lines and Angles — Vertical, Supplementary, and Complementary",
        "category": "math",
        "order": 66,
        "summary": (
            "Blok D ochiladi. Toʻgʻri chiziq 180 daraja, toʻliq burilish 360. "
            "Qolgan hamma narsa shu ikki fakt bilan chiqadi."
        ),
        "stories": ["The Check That Closes"],
        "content": """
<h2>SAT-66: Lines and Angles — Vertical, Supplementary, and Complementary</h2>

<p>Shu darsdan <b>Blok D</b> boshlanadi — geometriya va trigonometriya. Bu
blokda muvozanat teskari tomonga siljiydi: jumla osonlashadi, hisob
qaytadi. Va birinchi savol har safar bitta boʻladi:
<mark>bu formula varaqda bormi?</mark></p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Formula varagʻi</span>
  <p><b>Varaqda BOR:</b> aylana yuzasi va uzunligi, toʻgʻri toʻrtburchak va
  uchburchak yuzasi, Pifagor teoremasi, maxsus uchburchaklar, hajmlar,
  aylanada 360 daraja, uchburchak burchaklari yigʻindisi 180.</p>
  <p><b>Varaqda YOʻQ:</b> bu darsdagi hamma narsa. Vertikal burchaklar,
  qoʻshni burchaklar, toʻldiruvchi burchaklar — hech biri yozilmagan.
  Ularni bilish kerak.</p>
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>toʻgʻri chiziqdagi burchaklarni 180 ga toʻldirasiz;</li>
    <li>vertikal burchaklar teng ekanini ishlatasiz;</li>
    <li>«supplementary» va «complementary» ni ajratasiz;</li>
    <li>chizmadagi bitta burchakdan qolganini topasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Two facts, everything else follows</span>
  <span class="pe-chip pe-chip--v">toʻgʻri chiziq = 180°</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">toʻliq burilish = 360°</span>
</div>

<h3>Uch atama</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Atama</th><th>Yigʻindisi</th><th>Qayerda uchraydi</th></tr>
  <tr><td>complementary</td><td class="pm-word__sym">90°</td>
      <td>toʻgʻri burchak ikkiga boʻlinganda</td></tr>
  <tr><td>supplementary</td><td class="pm-word__sym">180°</td>
      <td>toʻgʻri chiziqda yonma-yon</td></tr>
  <tr><td>vertical angles</td><td class="pm-word__sym">teng</td>
      <td>ikki chiziq kesishganda qarama-qarshi</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ingliz tilidagi bu ikki soʻz oʻzbekchaga oʻxshash tarjima qilinadi va tez-tez
  aralashtiriladi. Yodlash usuli: <b>C</b>omplementary — <b>C</b>orner, yaʼni
  toʻgʻri burchak (90); <b>S</b>upplementary — <b>S</b>traight, yaʼni toʻgʻri
  chiziq (180).
</div>

<h3>Kesishgan ikki chiziq</h3>

<figure class="pm-fig">
  <svg viewBox="0 0 320 180" role="img"
       aria-label="Two lines crossing at a point, forming four angles: one
                   marked 130 degrees, the one opposite also 130, and the two
                   adjacent angles 50 degrees each">
    <line class="pm-ln" x1="30" y1="90" x2="290" y2="90"/>
    <line class="pm-ln" x1="105" y1="155" x2="215" y2="25"/>
    <circle cx="160" cy="90" r="3"/>
    <text class="pm-lbl" x="186" y="80">130°</text>
    <text class="pm-lbl" x="118" y="108">130°</text>
    <text class="pm-lbl" x="150" y="66">50°</text>
    <text class="pm-lbl" x="152" y="122">50°</text>
  </svg>
  <figcaption>Ikki chiziq kesishganda toʻrt burchak hosil boʻladi. Qarama-qarshi
  turganlari teng; yonma-yon turganlari 180 ga toʻldiradi.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Bitta burchak 130°</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Qarama-qarshisi ham 130°</span>
    <span class="pm-solve__why">Vertikal burchaklar teng</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Qolgan ikkitasi 50° dan</span>
    <span class="pm-solve__why">180 − 130; tekshiruv: 130 + 130 + 50 + 50 = 360 ✓</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Chizmada bitta burchak berilgan boʻlsa, <b>hamma burchakni yozib chiqing</b>.
  Bu 15 soniyalik ish va savol qaysi burchakni soʻrayotganini topishni
  osonlashtiradi — SAT ataylab eng uzoqdagisini soʻraydi.
</div>

<h3>Chizmaga ishonmang</h3>

<p>SAT chizmalari «not drawn to scale» deb belgilanishi mumkin, va u holda
koʻzga toʻgʻri burchakdek koʻringan burchak 89 ham, 91 ham boʻlishi mumkin.
<b>Faqat yozilgan sonlar va belgilar</b> ishonchli.</p>

<h3>Bir nuqtadan chiqqan burchaklar</h3>

<p>SAT tez-tez shunday chizma beradi: bitta nuqtadan bir necha nur chiqadi va
burchaklar harflar bilan belgilanadi. Bu yerda faqat ikkita savol bor —
<b>ular toʻgʻri chiziqni tashkil qiladimi yoki toʻliq burilishni?</b></p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Toʻgʻri chiziqda uchta burchak: 40°, x, 70°</span>
    <span class="pm-solve__why">Yigʻindisi 180</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 180 − 110 = 70°</span>
    <span class="pm-solve__why">Toʻliq burilish boʻlganda 360 dan ayirilardi</span>
  </div>
</div>

<p>Bu ikkisini ajratish uchun chizmaga qarang: burchaklar
<b>bitta toʻgʻri chiziqning ustidami</b>, yoki nuqta atrofini
<b>toʻliq aylanib chiqadimi</b>?</p>

<p>Yana bir tez-tez uchraydigan koʻrinish — <b>perpendikulyar</b> chiziqlar.
Ular kesishganda toʻrtala burchak ham 90 boʻladi, va chizmada kichik kvadrat
belgisi bilan koʻrsatiladi. Bu belgi boʻlmasa, burchak toʻgʻri deb faraz
qilib boʻlmaydi — hatto shundoq koʻrinsa ham.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>supplementary angles</b><span>yigʻindisi 180 boʻlgan burchaklar</span></li>
  <li><b>complementary angles</b><span>yigʻindisi 90 boʻlgan burchaklar</span></li>
  <li><b>vertical angles</b><span>qarama-qarshi (vertikal) burchaklar</span></li>
  <li><b>the measure of angle ABC</b><span>ABC burchagining kattaligi</span></li>
  <li><b>not drawn to scale</b><span>masshtabsiz chizilgan</span></li>
  <li><b>a straight line</b><span>toʻgʻri chiziq — 180 daraja</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>Two lines intersect. One of the four angles formed measures 130°. What is
    the measure of an adjacent angle?</p>
  </div>
  <ol class="ps-ch">
    <li>50°</li>
    <li>130°</li>
    <li>230°</li>
    <li>40°</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 50°</p>
      <p>Yonma-yon turgan burchaklar toʻgʻri chiziqni tashkil qiladi:
      180 − 130 = 50.</p>
      <p><b>130°</b> — bu qarama-qarshi burchak, qoʻshni emas.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">40°</span>
  <span class="ps-trap__why">90 dan ayirilgan — «complementary» qoidasi
  ishlatilgan. Ikki chiziq kesishganda 180 ishlaydi, 90 emas.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>Angles measuring (3<i>x</i> + 10)° and (2<i>x</i> − 5)° are supplementary.
    What is the value of <i>x</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>35</li>
    <li>17</li>
    <li>19</li>
    <li>60</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 35</p>
      <p>(3x + 10) + (2x − 5) = 180 → 5x + 5 = 180 → x = 35.</p>
      <p>Tekshiruv: 115° va 65°, yigʻindisi 180 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">17</span>
  <span class="ps-trap__why">Yigʻindi 90 deb olingan: 5x + 5 = 90 → x = 17.
  «Supplementary» 180 ni bildiradi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Burchak savolida shu tartibda ishlang:</p>
  <ol>
    <li>Chizmadagi <b>hamma</b> burchakni yozing;</li>
    <li>Toʻgʻri chiziqlarni belgilang — ular 180 beradi;</li>
    <li>Javobni tekshiring: butun kesishmada yigʻindi 360 boʻlishi
        kerak.</li>
  </ol>
  <p>Va har doim eslang: bu darsdagi hech bir qoida formula varagʻida
  yoʻq.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Kesishgan chiziqlarda 180 − 130 oʻrniga 90 − 130</p>
  <p class="pe-good">180 − 130 = 50</p>
  <p class="pe-fix__why">Toʻgʻri chiziq 180 daraja beradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Chizmada burchak toʻgʻri burchakdek koʻrinadi → 90 deb olamiz</p>
  <p class="pe-good">Faqat belgilangan boʻlsa 90</p>
  <p class="pe-fix__why">«Not drawn to scale» — koʻrinishga ishonib
  boʻlmaydi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bir nuqtadan chiqqan bir necha burchak berilgan boʻlsa, ularning yigʻindisi
  <b>toʻgʻri chiziqda 180</b>, <b>toʻliq aylanada 360</b>. SAT bu ikki holatni
  bir savolda ham beradi — chizmaga qarab qaysi biri ekanini aniqlang.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Burchak <b>90 dan katta</b> boʻlsa unga toʻldiruvchi (complementary) burchak
  umuman mavjud emas — chunki qolgani manfiy chiqadi. Javobda manfiy burchak
  chiqsa, qoidani notoʻgʻri tanlagansiz.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Two angles are complementary and one is 35°. What is the other?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">55° — 90 − 35.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Two angles are supplementary and one is 112°. What is the other?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">68° — 180 − 112.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Two lines cross and one angle is 74°. What are the other three?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">74°, 106°, 106°.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Three angles on a straight line are <i>x</i>, 2<i>x</i> and 3<i>x</i>. Find
  <i>x</i>.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">30 — 6x = 180.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Can an angle of 105° have a complement?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — 90 dan katta, qolgani manfiy chiqadi.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>supplementary</b><span>yigʻindisi 180°</span></li>
  <li><b>complementary</b><span>yigʻindisi 90°</span></li>
  <li><b>vertical angles</b><span>vertikal (qarama-qarshi) burchaklar</span></li>
  <li><b>adjacent</b><span>qoʻshni, yonma-yon</span></li>
  <li><b>intersect</b><span>kesishmoq</span></li>
  <li><b>the measure of</b><span>… ning kattaligi</span></li>
  <li><b>not drawn to scale</b><span>masshtabsiz</span></li>
  <li><b>right angle</b><span>toʻgʻri burchak</span></li>
  <li><b>straight angle</b><span>yoyiq burchak (180°)</span></li>
  <li><b>reference sheet</b><span>formula varagʻi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Toʻgʻri chiziq 180, toʻliq burilish 360</b> — qolgani shundan
        chiqadi.</li>
    <li><b>Vertikal burchaklar teng</b>; yonma-yon turganlari 180 ga
        toʻldiradi.</li>
    <li>Bu darsdagi hech bir qoida <b>formula varagʻida yoʻq</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-67 — parallel lines
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-67: Parallel Lines Cut by a Transversal",
        "category": "math",
        "order": 67,
        "summary": (
            "Ikki parallel chiziq kesuvchi bilan kesilganda faqat IKKI xil "
            "burchak hosil boʻladi — va ular 180 ga toʻldiradi."
        ),
        "stories": ["The Thread That Crosses"],
        "content": """
<h2>SAT-67: Parallel Lines Cut by a Transversal</h2>

<p>Bu mavzu murakkab koʻrinadi, chunki darsliklarda oltita atama beriladi.
Aslida bitta fakt yetarli: <mark>sakkizta burchak hosil boʻladi, lekin
ularning faqat ikki xil qiymati bor</mark>, va ikkalasi 180 ga
toʻldiradi.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Formula varagʻi</span>
  <p><b>Varaqda YOʻQ:</b> bu darsdagi qoidalarning hech biri. Parallel
  chiziqlar haqida u yerda bir soʻz ham yozilmagan — hammasi yodda
  boʻlishi kerak.</p>
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>sakkiz burchakni ikki guruhga ajratasiz;</li>
    <li>bitta burchakdan qolgan yettitasini topasiz;</li>
    <li>atamalarni tanimasangiz ham savolni yechasiz;</li>
    <li>chiziqlar parallelligini tekshirish savolini yechasiz.</li>
  </ul>
</div>

<figure class="pm-fig">
  <svg viewBox="0 0 320 200" role="img"
       aria-label="Two parallel horizontal lines cut by a slanting transversal,
                   forming eight angles; one is marked 70 degrees">
    <line class="pm-ln" x1="30" y1="60" x2="290" y2="60"/>
    <line class="pm-ln" x1="30" y1="140" x2="290" y2="140"/>
    <line class="pm-ln" x1="90" y1="170" x2="230" y2="30"/>
    <circle cx="200" cy="60" r="3"/>
    <circle cx="120" cy="140" r="3"/>
    <text class="pm-lbl" x="208" y="52">70°</text>
    <text class="pm-lbl" x="168" y="52">110°</text>
    <text class="pm-lbl" x="206" y="78">110°</text>
    <text class="pm-lbl" x="166" y="78">70°</text>
    <text class="pm-lbl" x="128" y="132">70°</text>
    <text class="pm-lbl" x="88"  y="132">110°</text>
    <text class="pm-lbl" x="126" y="158">110°</text>
    <text class="pm-lbl" x="86"  y="158">70°</text>
  </svg>
  <figcaption>Sakkiz burchak, ikki xil qiymat: 70° va 110°. Ular 180 ga
  toʻldiradi, va bir xil qiymatlilari toʻrttadan.</figcaption>
</figure>

<h3>Ikki guruh</h3>

<p>Rasmga qarang: <b>oʻtkir</b> burchaklarning hammasi 70°,
<b>oʻtmas</b> burchaklarning hammasi 110°. Boshqa qiymat yoʻq. Shuning
uchun savolda bitta burchak berilgan boʻlsa, qolgan yettitasi
darrov maʼlum.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Atamalarni yodlashdan koʻra shu ikki guruhni koʻrish osonroq:
  <b>hamma tor burchak teng, hamma keng burchak teng</b>, va bir tordan
  bir keng 180 beradi. SAT savollarining koʻpi shu bilan yechiladi.
</div>

<h3>Atamalar — bilish foydali</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Atama</th><th>Shakli</th><th>Munosabati</th></tr>
  <tr><td>corresponding</td><td>F harfi</td><td class="pm-word__sym">teng</td></tr>
  <tr><td>alternate interior</td><td>Z harfi</td><td class="pm-word__sym">teng</td></tr>
  <tr><td>co-interior (same-side)</td><td>C harfi</td><td class="pm-word__sym">yigʻindisi 180</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Bu qoidalar faqat chiziqlar <b>parallel</b> boʻlganda ishlaydi. Chizmada
  parallellik strelkalar bilan belgilanadi yoki matnda aytiladi. Belgi
  boʻlmasa, chiziqlar parallel deb faraz qilib boʻlmaydi.
</div>

<h3>Teskari savol</h3>

<p>SAT baʼzan teskari tomonga soʻraydi: burchaklar berilib, chiziqlar
parallelmi deb tekshiriladi. Qoida oʻsha-oʻsha, faqat teskari yoʻnalishda —
mos burchaklar teng boʻlsa, chiziqlar parallel.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Mos burchaklar 68° va 68°</span>
    <span class="pm-solve__why">Teng</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Chiziqlar parallel</span>
    <span class="pm-solve__why">Agar 68° va 72° boʻlsa — parallel emas</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Chizmada bitta burchak berilgan boʻlsa, <b>sakkiztasini ham yozib
  chiqing</b> — ikki xil son, toʻrttadan. Bu 20 soniyalik ish va savol
  qaysi burchakni soʻrayotganini izlashni tugatadi.
</div>

<h3>Uchburchakka ulanish</h3>

<p>SAT bu mavzuni koʻpincha yolgʻiz bermaydi — parallel chiziqlar
uchburchak bilan birga chiziladi. Yoʻl bittada: parallel qoidalari bilan
bitta burchakni koʻchiring, keyin uchburchakda 180 qoidasini ishlating
(SAT-68).</p>

<p>Masalan, kesuvchi bilan hosil boʻlgan 70° burchak almashinuvchi burchak
sifatida uchburchakning ichiga koʻchadi; uchburchakning ikkinchi burchagi
50° boʻlsa, uchinchisi 60° chiqadi. Ikki dars bitta chizmada ishlaydi, va
Blok D ning koʻp savoli aynan shunday tuzilgan.</p>

<p>Nihoyat, savol baʼzan <b>x uchun tenglama</b> koʻrinishida beriladi:
ikki burchak ifoda bilan yozilib, munosabat aytiladi. Bunda ish ikki
qadamda: munosabatni tanlang (teng yoki 180 ga toʻldiradi), keyin
tenglamani yeching. Chizmani oʻqish qismi shu bilan tugaydi.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>a transversal</b><span>kesuvchi chiziq</span></li>
  <li><b>corresponding angles</b><span>mos burchaklar</span></li>
  <li><b>alternate interior angles</b><span>ichki almashinuvchi burchaklar</span></li>
  <li><b>line m is parallel to line n</b><span>m chizigʻi n ga parallel</span></li>
  <li><b>which must be true</b><span>qaysi biri albatta toʻgʻri</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>Two parallel lines are cut by a transversal. One angle measures 70°. Which
    of the following is <u>not</u> a possible measure of another angle in the
    figure?</p>
  </div>
  <ol class="ps-ch">
    <li>90°</li>
    <li>70°</li>
    <li>110°</li>
    <li>Both 70° and 110° are possible</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 90°</p>
      <p>Faqat ikki qiymat hosil boʻladi: 70° va 110°.</p>
      <p>90° faqat kesuvchi perpendikulyar boʻlganda paydo boʻlardi — u
      holda hamma burchak 90 boʻlardi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">110°</span>
  <span class="ps-trap__why">110° <b>mumkin</b> — u 70 ning toʻldiruvchisi.
  Savol «not possible» degan; inkorni oʻqib qoʻyish oson.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">65 s</span></p>
  <div class="ps-stem__q">
    <p>Lines <i>m</i> and <i>n</i> are parallel and cut by a transversal. One
    angle measures (2<i>x</i> + 20)° and its co-interior angle measures
    (3<i>x</i> + 10)°. What is the value of <i>x</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>30</li>
    <li>10</li>
    <li>14</li>
    <li>50</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 30</p>
      <p>Co-interior burchaklar 180 ga toʻldiradi:
      (2x + 20) + (3x + 10) = 180 → 5x + 30 = 180 → x = 30.</p>
      <p>Tekshiruv: 80° va 100°, yigʻindisi 180 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">10</span>
  <span class="ps-trap__why">Burchaklar <b>teng</b> deb olingan:
  2x + 20 = 3x + 10 → x = 10. Co-interior burchaklar teng emas, ular
  180 ga toʻldiradi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Atamani tanimasangiz ham savolni yeching:</p>
  <ol>
    <li>Ikki burchak <b>bir xil tomonda</b> va ikkalasi ham tor (yoki
        ikkalasi ham keng) boʻlsa — teng;</li>
    <li>Biri tor, ikkinchisi keng boʻlsa — 180 ga toʻldiradi;</li>
    <li>Chizmadan qarang: qaysi ikkitasi oʻxshash koʻrinadi.</li>
  </ol>
  <p>Bu usul atamalarni yodlashdan koʻra ishonchliroq.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Co-interior burchaklar teng</p>
  <p class="pe-good">Ular 180 ga toʻldiradi</p>
  <p class="pe-fix__why">Bir xil tomonda turgan ichki burchaklar — biri tor,
  biri keng.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Chiziqlar parallel koʻrinyapti → qoidalarni ishlatamiz</p>
  <p class="pe-good">Parallellik aytilgan yoki belgilangan boʻlishi kerak</p>
  <p class="pe-fix__why">Chizma masshtabsiz boʻlishi mumkin (SAT-66).</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Kesuvchi parallel chiziqlarga <b>perpendikulyar</b> boʻlsa, sakkizta
  burchakning hammasi 90 boʻladi — ikki guruh bitta qiymatga qoʻshilib
  ketadi. Bu qoidaning istisnosi emas, aksincha, xususiy holi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Uchta yoki undan koʻp parallel chiziq berilsa ham hech narsa oʻzgarmaydi:
  qiymat baribir ikkitadan oshmaydi. SAT baʼzan uchta chiziq chizib
  savolni murakkabroq koʻrsatadi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Parallel lines are cut by a transversal and one angle is 55°. What are the two
  possible angle measures in the figure?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">55° va 125°.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Corresponding angles measure 82° and (<i>x</i> + 12)°. Find <i>x</i>.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">70 — mos burchaklar teng.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Co-interior angles measure 65° and <i>y</i>°. Find <i>y</i>.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">115 — ular 180 ga toʻldiradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  A transversal makes corresponding angles of 63° and 67°. Are the lines
  parallel?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — mos burchaklar teng emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A transversal is perpendicular to two parallel lines. How many different angle
  measures appear?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Bittasi — hammasi 90°.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>parallel</b><span>parallel</span></li>
  <li><b>transversal</b><span>kesuvchi</span></li>
  <li><b>corresponding angles</b><span>mos burchaklar</span></li>
  <li><b>alternate interior</b><span>ichki almashinuvchi</span></li>
  <li><b>co-interior / same-side</b><span>bir tomonli ichki burchaklar</span></li>
  <li><b>acute / obtuse</b><span>oʻtkir / oʻtmas</span></li>
  <li><b>perpendicular</b><span>perpendikulyar</span></li>
  <li><b>which must be true</b><span>qaysi biri albatta toʻgʻri</span></li>
  <li><b>congruent</b><span>teng, mos</span></li>
  <li><b>the figure shows</b><span>chizmada koʻrsatilgan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Sakkiz burchak, <b>ikki xil qiymat</b> — toʻrttadan.</li>
    <li>Hamma tor teng, hamma keng teng, tor + keng = <b>180</b>.</li>
    <li>Qoidalar faqat <b>parallellik aytilganda</b> ishlaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-68 — triangle angles
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-68: Triangles — Interior and Exterior Angle Theorems",
        "category": "math",
        "order": 68,
        "summary": (
            "Uchburchak burchaklari yigʻindisi 180 — bu VARAQDA BOR. Tashqi "
            "burchak qoidasi esa yoʻq, lekin u shundan chiqadi."
        ),
        "stories": ["A Triangle With Three Right Angles"],
        "content": """
<h2>SAT-68: Triangles — Interior and Exterior Angle Theorems</h2>

<p>Bu darsda birinchi marta <mark>formula varagʻida haqiqatan bor</mark>
narsa uchraydi. Va undan ikkinchi, varaqda boʻlmagan qoida bir qatorda
chiqariladi.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Formula varagʻi</span>
  <p><b>BOR:</b> «The sum of the measures in degrees of the angles of a
  triangle is 180.» Bu jumla varaqda aynan yozilgan.</p>
  <p><b>YOʻQ:</b> tashqi burchak teoremasi. Lekin uni yodlash shart emas —
  u 180 dan ikki qatorda chiqadi.</p>
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>uchinchi burchakni ikkitasidan topasiz;</li>
    <li>tashqi burchak qoidasini oʻzingiz chiqarasiz;</li>
    <li>bir necha uchburchakli chizmada zanjir bilan ishlaysiz;</li>
    <li>tashqi burchak har doim kattaroq ekanini bilasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">On the sheet</span>
  <span class="pe-chip pe-chip--v">uchta ichki burchak</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">180°</span>
</div>

<h3>Tashqi burchakni oʻzingiz chiqaring</h3>

<figure class="pm-fig">
  <svg viewBox="0 0 320 180" role="img"
       aria-label="A triangle with interior angles 50 and 60 degrees, a third
                   interior angle of 70, and an exterior angle of 110 degrees
                   beside it on the extended base">
    <line class="pm-ln" x1="40" y1="140" x2="280" y2="140"/>
    <line class="pm-ln" x1="60" y1="140" x2="158" y2="24"/>
    <line class="pm-ln" x1="158" y1="24" x2="200" y2="140"/>
    <circle cx="60"  cy="140" r="3"/>
    <circle cx="200" cy="140" r="3"/>
    <circle cx="158" cy="24"  r="3"/>
    <text class="pm-lbl" x="70"  y="132">50°</text>
    <text class="pm-lbl" x="170" y="132">70°</text>
    <text class="pm-lbl" x="148" y="46">60°</text>
    <text class="pm-lbl" x="212" y="132">110°</text>
  </svg>
  <figcaption>Ichki burchaklar 50, 60 va 70 — yigʻindisi 180. Asos davom
  ettirilgan; tashqi burchak 110, yaʼni 50 + 60.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">50 + 60 + uchinchi = 180</span>
    <span class="pm-solve__why">Varaqdagi qoida</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Uchinchi burchak = 70°</span>
    <span class="pm-solve__why">180 − 110</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Tashqi burchak = 180 − 70 = 110 = 50 + 60</span>
    <span class="pm-solve__why">Toʻgʻri chiziq 180 beradi (SAT-66)</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Tashqi burchak <b>uzoqdagi ikki ichki burchakning yigʻindisiga</b> teng.
  Sababi yuqorida koʻrinib turibdi: ikkalasi ham 180 dan uchinchi burchakni
  ayirish orqali chiqadi. Yodlash mumkin, lekin chiqarish ikki qator.
</div>

<h3>Foydali natija</h3>

<p>Tashqi burchak har doim <b>uzoqdagi har bir ichki burchakdan katta</b>,
chunki u ikkalasining yigʻindisi. SAT baʼzan aynan shu taqqoslashni
soʻraydi va hisoblash umuman kerak boʻlmaydi.</p>

<h3>Zanjirli chizmalar</h3>

<p>Ikki yoki uch uchburchak bir chizmada berilsa, ular odatda bitta burchak
orqali bogʻlangan boʻladi. Yoʻl bittada: <b>bilganingizdan boshlang</b> va
har bir uchburchakda 180 qoidasini qoʻllang, birin-ketin.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Har topgan burchagingizni <b>darrov chizmaga yozing</b>. Zanjirli
  savollarda uchinchi qadamda ikkinchi qadamning natijasi kerak boʻladi, va
  yozilmagan son yodda qolmaydi.
</div>

<h3>Uchburchak turlari va burchaklar</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Turi</th><th>Burchaklari</th><th>Nomi inglizcha</th></tr>
  <tr><td>hammasi 90 dan kichik</td><td class="pm-word__sym">oʻtkir</td><td>acute</td></tr>
  <tr><td>bittasi aynan 90</td><td class="pm-word__sym">toʻgʻri</td><td>right</td></tr>
  <tr><td>bittasi 90 dan katta</td><td class="pm-word__sym">oʻtmas</td><td>obtuse</td></tr>
</table></div>

<p>Uchinchi qatordagi «bittasi» soʻzi muhim: 90 dan katta burchak
<b>koʻpi bilan bitta</b> boʻladi. Shuning uchun «ikkita oʻtmas burchakli
uchburchak» degan narsa mavjud emas, va SAT bu savolni beradi.</p>

<p>Uchburchak burchaklari haqidagi qoida <b>faqat uchburchakka</b>
tegishli. Toʻrtburchakda yigʻindi 360, beshburchakda 540 — har bir yangi
tomon 180 qoʻshadi. SAT toʻrtburchak burchaklarini ham soʻraydi, va u
yerda 180 emas, 360 ishlaydi.</p>

<p>Bir savolda ikki uchburchak berilib, ular bitta burchakni
<b>baham koʻrsa</b>, oʻsha burchak ikkalasida ham bir xil. Bu koʻpincha
zanjirning bogʻlovchi halqasi boʻladi: birinchi uchburchakdan topilgan
burchak ikkinchisiga oʻtadi va u yerda 180 qoidasi yana ishlaydi.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>the interior angles of a triangle</b><span>uchburchakning ichki burchaklari</span></li>
  <li><b>an exterior angle</b><span>tashqi burchak</span></li>
  <li><b>the remote interior angles</b><span>uzoqdagi ichki burchaklar</span></li>
  <li><b>side BC is extended</b><span>BC tomoni davom ettirilgan</span></li>
  <li><b>what is the value of x</b><span>x nechaga teng</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>In a triangle, two angles measure 50° and 60°. What is the measure of the
    exterior angle at the third vertex?</p>
  </div>
  <ol class="ps-ch">
    <li>110°</li>
    <li>70°</li>
    <li>120°</li>
    <li>130°</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 110°</p>
      <p>Tashqi burchak uzoqdagi ikki ichki burchakning yigʻindisi:
      50 + 60.</p>
      <p>Yoki: uchinchi ichki burchak 70, va 180 − 70 = 110.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">70°</span>
  <span class="ps-trap__why">Bu uchinchi <b>ichki</b> burchak. Savol tashqi
  burchakni soʻragan, va ikkalasi 180 ga toʻldiradi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">70 s</span></p>
  <div class="ps-stem__q">
    <p>In a triangle the angles measure <i>x</i>°, (2<i>x</i>)° and
    (3<i>x</i> − 30)°. What is the value of <i>x</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>35</li>
    <li>30</li>
    <li>25</li>
    <li>60</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 35</p>
      <p>x + 2x + 3x − 30 = 180 → 6x = 210 → x = 35.</p>
      <p>Tekshiruv: 35°, 70°, 75° — yigʻindisi 180 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">30</span>
  <span class="ps-trap__why">−30 unutilgan: 6x = 180 → x = 30. U holda
  burchaklar 30, 60, 60 boʻlib, yigʻindisi 150 chiqadi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Uchburchak savolida ikki qoidadan boshqasi kerak emas:</p>
  <ol>
    <li>Ichki burchaklar yigʻindisi <b>180</b> (varaqda bor);</li>
    <li>Toʻgʻri chiziqdagi burchaklar ham <b>180</b> (SAT-66);</li>
    <li>Ikkovi birga tashqi burchak qoidasini beradi.</li>
  </ol>
  <p>Javobni tekshirish ham oson: uchta burchakni qoʻshib 180 chiqishi
  kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Tashqi burchak = uchinchi ichki burchak</p>
  <p class="pe-good">Ular 180 ga toʻldiradi</p>
  <p class="pe-fix__why">Tashqi burchak uzoqdagi <b>ikki</b> burchakning
  yigʻindisi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">x + 2x + 3x − 30 = 180 → 6x = 180</p>
  <p class="pe-good">6x = 210</p>
  <p class="pe-fix__why">−30 ni oʻng tomonga oʻtkazganda u qoʻshiladi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Uchburchakda <b>koʻpi bilan bitta</b> burchak 90 dan katta boʻlishi
  mumkin — chunki ikkitasi allaqachon 180 dan oshib ketardi. Bu javobni
  tekshirishning tez usuli.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Har bir uchdan ikkita tashqi burchak chiqadi va ular teng — vertikal
  burchaklar (SAT-66). Shuning uchun «the exterior angle» degan ibora
  noaniq emas: qaysi tomonga chizilsa ham kattaligi bir xil.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Two angles of a triangle are 45° and 65°. What is the third?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">70°.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Two angles of a triangle are 40° and 85°. What is the exterior angle at the
  third vertex?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">125° — 40 + 85.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A triangle's angles are <i>x</i>, <i>x</i> + 20 and <i>x</i> + 40. Find
  <i>x</i>.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">40 — 3x + 60 = 180.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Can a triangle have two angles of 95°?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — ikkitasi allaqachon 190, bu 180 dan
  koʻp.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  An exterior angle is 100°. What is the interior angle beside it?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">80° — ular toʻgʻri chiziqda.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>interior angle</b><span>ichki burchak</span></li>
  <li><b>exterior angle</b><span>tashqi burchak</span></li>
  <li><b>remote interior angles</b><span>uzoqdagi ichki burchaklar</span></li>
  <li><b>vertex</b><span>uch (burchak nuqtasi)</span></li>
  <li><b>is extended</b><span>davom ettirilgan</span></li>
  <li><b>the sum of the measures</b><span>kattaliklar yigʻindisi</span></li>
  <li><b>obtuse angle</b><span>oʻtmas burchak</span></li>
  <li><b>acute triangle</b><span>oʻtkir burchakli uchburchak</span></li>
  <li><b>in the figure above</b><span>yuqoridagi chizmada</span></li>
  <li><b>at most one</b><span>koʻpi bilan bitta</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Ichki burchaklar yigʻindisi <b>180 — varaqda bor</b>.</li>
    <li>Tashqi burchak = <b>uzoqdagi ikki ichki burchak yigʻindisi</b>.</li>
    <li>U 180 dan uchinchi burchakni ayirish orqali <b>ikki qatorda</b>
        chiqadi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-69 — isosceles and equilateral
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-69: Isosceles and Equilateral Triangles",
        "category": "math",
        "order": 69,
        "summary": (
            "Teng tomonlarga teng burchaklar qarshi turadi — va aksincha. "
            "Bitta belgi butun uchburchakni ochadi."
        ),
        "stories": ["Why the Kite Flies Straight"],
        "content": """
<h2>SAT-69: Isosceles and Equilateral Triangles</h2>

<p>Bu darsda bitta gʻoya bor va u ikki tomonga ham ishlaydi:
<mark>teng tomonlarga teng burchaklar qarshi turadi</mark>. SAT chizmaga
ikkita kichkina chiziqcha qoʻyadi, va shu belgi butun savolni
ochadi.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Formula varagʻi</span>
  <p><b>Varaqda YOʻQ:</b> teng yonli va teng tomonli uchburchak haqida
  hech narsa. Faqat 180 qoidasi bor (SAT-68) — qolganini bilish
  kerak.</p>
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>chizmadagi teng tomon belgisini oʻqiysiz;</li>
    <li>uch burchakni bittasidan topasiz;</li>
    <li>qoidani teskari yoʻnalishda ham ishlatasiz;</li>
    <li>teng tomonli uchburchakning har bir burchagi 60 ekanini
        chiqarasiz.</li>
  </ul>
</div>

<figure class="pm-fig">
  <svg viewBox="0 0 320 170" role="img"
       aria-label="An isosceles triangle with apex angle 40 degrees and two
                   equal base angles of 70 degrees each; the two equal sides
                   are marked with small ticks">
    <line class="pm-ln" x1="116" y1="140" x2="204" y2="140"/>
    <line class="pm-ln" x1="116" y1="140" x2="160" y2="20"/>
    <line class="pm-ln" x1="160" y1="20" x2="204" y2="140"/>
    <line class="pm-ln" x1="133" y1="76" x2="143" y2="82"/>
    <line class="pm-ln" x1="177" y1="82" x2="187" y2="76"/>
    <text class="pm-lbl" x="150" y="44">40°</text>
    <text class="pm-lbl" x="124" y="132">70°</text>
    <text class="pm-lbl" x="180" y="132">70°</text>
  </svg>
  <figcaption>Ikkita kichik chiziqcha teng tomonlarni bildiradi. Ularga
  qarshi turgan burchaklar ham teng: 70° va 70°.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Uchidagi burchak 40°</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Qolgan ikkitasi teng: 180 − 40 = 140</span>
    <span class="pm-solve__why">Teng tomonlarga teng burchaklar qarshi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Har biri 70°</span>
    <span class="pm-solve__why">140 ÷ 2; tekshiruv: 40 + 70 + 70 = 180 ✓</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikki qadam har doim bir xil: <b>180 dan berilganini ayiring, qolganini
  ikkiga boʻling</b>. Va teskari holatda: asos burchagi berilgan boʻlsa, uni
  ikkiga koʻpaytirib 180 dan ayiring.
</div>

<h3>Teng tomonli uchburchak</h3>

<p>Uchala tomon teng boʻlsa, uchala burchak ham teng. Yigʻindisi 180
boʻlgani uchun har biri <b>60°</b>. Bu yodlanadigan fakt emas — u bir
boʻlishdan chiqadi.</p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  «Ikki tomoni teng» degani <b>uchinchisi ham teng</b> degani emas. Teng
  yonli uchburchakda ikki tomon teng; teng tomonlida uchtasi. Har bir teng
  tomonli uchburchak teng yonli, lekin aksi notoʻgʻri.
</div>

<h3>Teskari yoʻnalish</h3>

<p>Qoida ikki tomonga ham ishlaydi: <b>ikki burchak teng boʻlsa, ularga
qarshi turgan tomonlar ham teng</b>. SAT bu koʻrinishni ham beradi —
burchaklar berilib, tomonlar haqida savol soʻraladi.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Chizmada belgi qidiring: <b>tomondagi kichik chiziqchalar</b> teng
  tomonlarni, <b>burchakdagi kichik yoylar</b> teng burchaklarni bildiradi.
  Bir xil sondagi chiziqcha — bir xil uzunlik. Bu belgilar savolning yarmini
  aytib beradi.
</div>

<h3>Tomon va burchak birga berilganda</h3>

<p>SAT baʼzan tomonlar uzunligini ham beradi. Qoida oʻsha-oʻsha, faqat
teskari tomondan oʻqiladi: <b>eng uzun tomonga eng katta burchak</b>
qarshi turadi, eng qisqasiga esa eng kichigi.</p>

<p>Uchburchakda tomonlar 5, 5 va 8 boʻlsa, teng tomonlarga qarshi turgan ikki
burchak teng, va 8 ga qarshi turgani ulardan katta. Uchburchak teng yonli,
va eng katta burchak asosga qarshi turadi.</p>

<p>Teng yonli uchburchakning yana bir xossasi: uchidan asosga tushirilgan
balandlik uni <b>ikkita bir xil</b> toʻgʻri burchakli uchburchakka boʻladi
va asosni teng ikkiga ajratadi. Bu SAT-70 dagi Pifagor bilan birga
ishlatiladi — masalan, teng yonli uchburchakning balandligini topishda.</p>

<p>Nihoyat, teng yonli uchburchak <b>simmetrik</b>: uchidan tushirilgan
chiziq shaklni ikkiga buklaganda ustma-ust tushadi. Shuning uchun unda
teng burchak, teng tomon va teng masofa — hammasi bitta simmetriyadan
kelib chiqadi.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>an isosceles triangle</b><span>teng yonli uchburchak</span></li>
  <li><b>an equilateral triangle</b><span>teng tomonli uchburchak</span></li>
  <li><b>the base angles</b><span>asos burchaklari — teng boʻlganlari</span></li>
  <li><b>AB = AC</b><span>ikki tomon teng</span></li>
  <li><b>congruent sides</b><span>teng tomonlar</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>In triangle ABC, AB = AC and the angle at A measures 40°. What is the
    measure of the angle at B?</p>
  </div>
  <ol class="ps-ch">
    <li>70°</li>
    <li>40°</li>
    <li>140°</li>
    <li>100°</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 70°</p>
      <p>AB = AC, demak B va C dagi burchaklar teng. 180 − 40 = 140, va
      140 ÷ 2 = 70.</p>
      <p><b>140°</b> — ikkiga boʻlish unutilgan.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">140°</span>
  <span class="ps-trap__why">Bu ikki burchakning <b>yigʻindisi</b>. Oxirgi
  qadam — ikkiga boʻlish — bajarilmagan.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">65 s</span></p>
  <div class="ps-stem__q">
    <p>In an isosceles triangle, one of the equal angles measures 55°. What is
    the measure of the third angle?</p>
  </div>
  <ol class="ps-ch">
    <li>70°</li>
    <li>55°</li>
    <li>125°</li>
    <li>62.5°</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 70°</p>
      <p>Ikkita teng burchak 55° dan, demak 110°. Uchinchisi
      180 − 110 = 70.</p>
      <p>Diqqat: bu safar berilgani <b>teng</b> burchaklardan biri, uchidagi
      emas.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">62.5°</span>
  <span class="ps-trap__why">55° uchidagi burchak deb olingan:
  (180 − 55) ÷ 2. Savolni oʻqing — u <b>teng</b> burchaklardan birini
  bergan.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Har safar bitta savol bering: <b>berilgan burchak qaysi biri?</b></p>
  <ol>
    <li>Uchidagi (teng boʻlmagani) boʻlsa: 180 − u, keyin ikkiga
        boʻling;</li>
    <li>Teng burchaklardan biri boʻlsa: uni ikkiga koʻpaytiring, 180 dan
        ayiring;</li>
    <li>Javobni tekshiring: uchtasi 180 berishi kerak.</li>
  </ol>
  <p>SAT ikkala koʻrinishni ham beradi, va ular boshqa javob chiqaradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">180 − 40 = 140 → burchak 140°</p>
  <p class="pe-good">140 ÷ 2 = 70°</p>
  <p class="pe-fix__why">140 — ikki teng burchakning yigʻindisi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Teng burchak 55° → (180 − 55) ÷ 2</p>
  <p class="pe-good">180 − 2(55) = 70°</p>
  <p class="pe-fix__why">Berilgan burchak allaqachon teng juftlikdan
  biri.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Teng yonli uchburchakda uchidagi burchak <b>toʻgʻri burchak</b> boʻlsa,
  asos burchaklari 45 dan boʻladi. Bu SAT-71 dagi 45-45-90 uchburchagining
  oʻzi — u shu darsdan kelib chiqadi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Teng tomonli uchburchak <b>har doim</b> oʻtkir burchakli: uchala burchak
  60 dan. Shuning uchun «teng tomonli va toʻgʻri burchakli» degan
  uchburchak mavjud emas.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  An isosceles triangle has an apex angle of 80°. What are the base angles?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">50° dan — (180 − 80) ÷ 2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  An isosceles triangle has base angles of 65°. What is the apex angle?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">50° — 180 − 130.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  What is each angle of an equilateral triangle?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">60° — 180 ÷ 3.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  In triangle PQR, the angles at P and Q are both 48°. Which sides are
  equal?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">P va Q ga qarshi turgan tomonlar — QR va PR.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Can an equilateral triangle contain a right angle?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — uning har bir burchagi 60°.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>isosceles</b><span>teng yonli</span></li>
  <li><b>equilateral</b><span>teng tomonli</span></li>
  <li><b>base angles</b><span>asos burchaklari</span></li>
  <li><b>apex angle</b><span>uchidagi burchak</span></li>
  <li><b>congruent</b><span>teng, mos</span></li>
  <li><b>opposite the side</b><span>tomonga qarshi turgan</span></li>
  <li><b>tick marks</b><span>teng tomon belgilari</span></li>
  <li><b>scalene</b><span>turli tomonli</span></li>
  <li><b>AB = AC</b><span>AB va AC tomonlari teng</span></li>
  <li><b>acute</b><span>oʻtkir burchakli</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Teng tomonlarga teng burchaklar</b> qarshi turadi — ikki
        tomonga ham.</li>
    <li>Berilgan burchak <b>uchidagimi yoki teng juftlikdanmi</b> — avval
        shuni aniqlang.</li>
    <li>Teng tomonlida har bir burchak <b>60°</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-70 — Pythagoras and distance
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-70: Pythagorean Theorem and the Distance Formula",
        "category": "math",
        "order": 70,
        "summary": (
            "Pifagor teoremasi varaqda bor. Masofa formulasi yoʻq — lekin u "
            "koordinata tekisligidagi Pifagorning oʻzi."
        ),
        "stories": ["Twelve Knots"],
        "content": """
<h2>SAT-70: Pythagorean Theorem and the Distance Formula</h2>

<p>Bu dars Blok D dagi eng koʻp ishlatiladigan qurolni beradi. Va u
<mark>formula varagʻida bor</mark> — demak yodlash shart emas, lekin
qachon ishlatishni bilish shart.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Formula varagʻi</span>
  <p><b>BOR:</b> Pifagor teoremasi, toʻgʻri burchakli uchburchak chizmasi
  bilan.</p>
  <p><b>YOʻQ:</b> masofa formulasi va oʻrta nuqta formulasi. Lekin masofani
  yodlash shart emas — ikki nuqta orasiga toʻgʻri burchakli uchburchak
  chizsangiz, Pifagor ishlaydi.</p>
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>gipotenuzani va katetni ajratasiz;</li>
    <li>tez uchraydigan uchliklarni tanib olasiz;</li>
    <li>koordinata tekisligida masofani Pifagor bilan topasiz;</li>
    <li>teskari savolni — katetni topishni — yechasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">On the sheet</span>
  <span class="pe-chip pe-chip--v">a<sup>2</sup> + b<sup>2</sup></span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">c<sup>2</sup></span>
</div>

<p><b>c har doim gipotenuza</b> — toʻgʻri burchakka qarshi turgan, eng uzun
tomon. Bu darsdagi eng koʻp uchraydigan xato: kateti gipotenuza oʻrniga
qoʻyish.</p>

<h3>Tez uchliklar</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Uchlik</th><th>Tekshiruv</th><th>Karralilari</th></tr>
  <tr><td>3, 4, 5</td><td class="pm-word__sym">9 + 16 = 25</td><td>6-8-10, 9-12-15</td></tr>
  <tr><td>5, 12, 13</td><td class="pm-word__sym">25 + 144 = 169</td><td>10-24-26</td></tr>
  <tr><td>8, 15, 17</td><td class="pm-word__sym">64 + 225 = 289</td><td>16-30-34</td></tr>
  <tr><td>7, 24, 25</td><td class="pm-word__sym">49 + 576 = 625</td><td>14-48-50</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Uchliklarni tanib olish vaqt tejaydi, lekin ularni yodlash
  <b>majburiy emas</b> — formula varaqda turibdi. Ikkita sonni koʻrgach avval
  uchlikmi deb qarang; boʻlmasa hisoblang.
</div>

<h3>Koordinata tekisligida masofa</h3>

<figure class="pm-fig">
  <svg viewBox="0 0 320 200" role="img"
       aria-label="Two points on a grid joined by a slanting segment, with a
                   horizontal leg of 3 and a vertical leg of 4 forming a right
                   triangle; the segment has length 5">
    <line class="pm-ln" x1="40" y1="160" x2="290" y2="160"/>
    <line class="pm-ln" x1="40" y1="160" x2="40" y2="30"/>
    <circle cx="90" cy="140" r="4"/>
    <circle cx="180" cy="60" r="4"/>
    <line class="pm-ln" x1="90" y1="140" x2="180" y2="60"/>
    <line class="pm-ln" x1="90" y1="140" x2="180" y2="140" stroke-dasharray="4 4"/>
    <line class="pm-ln" x1="180" y1="140" x2="180" y2="60" stroke-dasharray="4 4"/>
    <text class="pm-lbl" x="126" y="156">3</text>
    <text class="pm-lbl" x="188" y="104">4</text>
    <text class="pm-lbl" x="118" y="94">5</text>
    <text class="pm-lbl" x="60"  y="150">(1, 2)</text>
    <text class="pm-lbl" x="190" y="50">(4, 6)</text>
  </svg>
  <figcaption>Ikki nuqta orasidagi kesma — toʻgʻri burchakli uchburchakning
  gipotenuzasi. Katetlar 3 va 4, demak masofa 5.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">(1, 2) va (4, 6)</span>
    <span class="pm-solve__why">Ikki nuqta</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Gorizontal farq 3, vertikal farq 4</span>
    <span class="pm-solve__why">4 − 1 va 6 − 2</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Masofa = 5</span>
    <span class="pm-solve__why">9 + 16 = 25 — bu 3-4-5 uchligi</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Masofa formulasini yodlashning hojati yoʻq: <b>ikki nuqtani chizing, bittasidan
  gorizontal, ikkinchisidan vertikal chiziq oʻtkazing</b> — toʻgʻri burchakli
  uchburchak hosil boʻladi, va uning gipotenuzasi izlanayotgan masofa.
  Ishoralar ham muhim emas, chunki farqlar kvadratga koʻtariladi.
</div>

<h3>Katetni topish</h3>

<p>Gipotenuza va bitta katet berilsa, formulani teskari ishlatasiz:
c<sup>2</sup> − a<sup>2</sup> = b<sup>2</sup>. Masalan 13 va 5 berilsa:
169 − 25 = 144, demak b = 12.</p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Bu holda <b>ayirish</b> kerak, qoʻshish emas. 13 va 5 ni qoʻshib
  koʻtarsangiz 194 chiqadi — va javob variantlarida taxminan 14 turadi.
  Eng uzun tomon qaysi ekanini aniqlang.
</div>

<h3>Toʻgʻri toʻrtburchakning diagonali</h3>

<p>SAT'da eng koʻp uchraydigan qoʻshimcha shakl — toʻgʻri toʻrtburchak
diagonali. Diagonal uni ikkita toʻgʻri burchakli uchburchakka boʻladi, va
tomonlar katetga aylanadi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Toʻrtburchak 9 ga 12</span>
    <span class="pm-solve__why">Tomonlar — katetlar</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Diagonal = 15</span>
    <span class="pm-solve__why">81 + 144 = 225; bu 3-4-5 ning uch barobari</span>
  </div>
</div>

<p>Uch oʻlchovli shakllarda ham xuddi shu qoida ishlaydi, faqat ikki marta:
qutining eng uzun diagonali uchun avval asos diagonalini toping, keyin uni
balandlik bilan birga ikkinchi uchburchakka qoʻying. SAT bu savolni kamdan-kam
beradi, lekin bergan paytda usul aynan shu.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>the hypotenuse</b><span>gipotenuza — eng uzun tomon</span></li>
  <li><b>a leg of the triangle</b><span>katet</span></li>
  <li><b>the distance between the points</b><span>nuqtalar orasidagi masofa</span></li>
  <li><b>in the xy-plane</b><span>koordinata tekisligida</span></li>
  <li><b>to the nearest tenth</b><span>oʻndan bir aniqlikda</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>In the <i>xy</i>-plane, what is the distance between the points (1, 2) and
    (4, 6)?</p>
  </div>
  <ol class="ps-ch">
    <li>5</li>
    <li>7</li>
    <li>25</li>
    <li>√7</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 5</p>
      <p>Katetlar 3 va 4: 9 + 16 = 25, va √25 = 5.</p>
      <p><b>25</b> — ildiz olish unutilgan; bu masofaning kvadrati.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">7</span>
  <span class="ps-trap__why">Katetlar shunchaki qoʻshilgan: 3 + 4. Gipotenuza
  har doim katetlar yigʻindisidan <b>kichik</b> va har biridan
  katta.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">55 s</span></p>
  <div class="ps-stem__q">
    <p>A right triangle has a hypotenuse of 13 and one leg of 5. What is the
    length of the other leg?</p>
  </div>
  <ol class="ps-ch">
    <li>12</li>
    <li>14</li>
    <li>18</li>
    <li>8</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 12</p>
      <p>169 − 25 = 144, va √144 = 12.</p>
      <p>Bu 5-12-13 uchligi — uni tanigan oʻquvchi hisoblamaydi ham.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">14</span>
  <span class="ps-trap__why">Qoʻshilgan: 169 + 25 = 194, va √194 ≈ 13.9.
  Gipotenuza berilganda <b>ayiriladi</b>.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Har safar birinchi savol bitta: <b>gipotenuza qaysi?</b></p>
  <ol>
    <li>U toʻgʻri burchakka qarshi turadi va eng uzun;</li>
    <li>U izlanayotgan boʻlsa — <b>qoʻshing</b>;</li>
    <li>U berilgan boʻlsa — <b>ayiring</b>.</li>
  </ol>
  <p>Javobni tekshiring: gipotenuza har bir katetdan katta, lekin
  ikkalasining yigʻindisidan kichik boʻlishi shart.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Masofa (1,2) dan (4,6) gacha: 3 + 4 = 7</p>
  <p class="pe-good">5</p>
  <p class="pe-fix__why">Katetlar qoʻshilmaydi — kvadratlari
  qoʻshiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Gipotenuza 13, katet 5 → 169 + 25</p>
  <p class="pe-good">169 − 25 = 144</p>
  <p class="pe-fix__why">Gipotenuza berilgan boʻlsa ayiriladi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Uch tomon berilib «bu toʻgʻri burchakli uchburchakmi?» deb soʻralsa,
  <b>eng uzunini gipotenuza deb oling</b> va tekshiring. 6, 8, 10 uchun
  36 + 64 = 100 ✓ — ha; 6, 8, 11 uchun 36 + 64 = 100 ≠ 121 ✗ — yoʻq.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Javob koʻpincha <b>ildiz koʻrinishida</b> qoladi: √13, 2√5 kabi. Uni
  soddalashtiring (SAT-25), lekin oʻnli kasrga aylantirmang — SAT javob
  variantlari odatda aniq koʻrinishda beriladi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  A right triangle has legs 6 and 8. What is the hypotenuse?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">10 — 3-4-5 ning ikki barobari.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  A right triangle has hypotenuse 25 and one leg 7. Find the other leg.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">24 — 625 − 49 = 576.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  What is the distance between (0, 0) and (5, 12)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">13.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  What is the distance between (−1, 3) and (2, 7)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">5 — katetlar 3 va 4; ishoralar muhim emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Is a triangle with sides 9, 12 and 15 a right triangle?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ha — 81 + 144 = 225, bu 3-4-5 ning uch
  barobari.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>hypotenuse</b><span>gipotenuza</span></li>
  <li><b>leg</b><span>katet</span></li>
  <li><b>right triangle</b><span>toʻgʻri burchakli uchburchak</span></li>
  <li><b>Pythagorean triple</b><span>Pifagor uchligi</span></li>
  <li><b>the distance between</b><span>… orasidagi masofa</span></li>
  <li><b>in the xy-plane</b><span>koordinata tekisligida</span></li>
  <li><b>opposite the right angle</b><span>toʻgʻri burchakka qarshi</span></li>
  <li><b>in simplest radical form</b><span>eng sodda ildiz koʻrinishida</span></li>
  <li><b>to the nearest tenth</b><span>oʻndan bir aniqlikda</span></li>
  <li><b>diagonal</b><span>diagonal</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Pifagor <b>varaqda bor</b>; masofa formulasi yoʻq, lekin u
        oʻshaning oʻzi.</li>
    <li><b>c — gipotenuza</b>: izlansa qoʻshing, berilsa ayiring.</li>
    <li>Uchliklarni taning: <b>3-4-5, 5-12-13, 8-15-17, 7-24-25</b>.</li>
  </ul>
</div>
""",
    },
]
