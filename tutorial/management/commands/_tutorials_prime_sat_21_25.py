# -*- coding: utf-8 -*-
"""Prime SAT Math — lessons 21–25 (Block A yakuni + Advanced Math boshlanishi).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_SAT.md
Lesson list: tutorial/management/commands/toc_prime_sat_math.txt

  mashqlar — practice/management/commands/_practice_ps_21_25.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_sat_readings_21_25.py

⚠️ ESKI SAT-21 … SAT-25 ustiga yoziladi (--republish).
⚠️ Til: sarlavha va test savollari inglizcha, tushuntirish oʻzbekcha. Son: 3.5 va 1,200.

⚠️ Kumulyativ (SAT-1…20 erkin: ifoda, tenglama, matndan tenglama, modul tenglamasi,
   qiyalik va uning barcha shakllari, chizish, kontekst, parallel/perpendikulyar,
   tengsizliklar va ularning grafigi, sistemalar va uchala natija):
  • SAT-21 — tengsizliklar sistemasi: yechim ikki shtrixlangan sohaning KESISHMASI.
    Blok A ning grafik qismini yopadi.
  • SAT-22 — modulli tengsizlik: «kichik» → oraliq (VA), «katta» → ikki tomon (YOKI).
    Blok A ning yakuni; SAT-4 va SAT-13 ni birlashtiradi.
  • SAT-23 — daraja qonunlari. ⚠️ Bu yerdan Blok B (Advanced Math) boshlanadi.
  • SAT-24 — manfiy va kasr koʻrsatkichlar; ildiz bilan bogʻlanish.
  • SAT-25 — ildizli ifodalarni soddalashtirish.
  • ⛔ Koʻphad koʻpaytmasi (SAT-28) YOʻQ; maxrajni ratsionallash (SAT-26) YOʻQ;
    kvadrat tenglama (SAT-31+) YOʻQ; ps-desmos SAT-83 dan.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_sat_21_25.py \\
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
    # SAT-21 — systems of inequalities
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-21: Systems of Linear Inequalities and Bounded Regions",
        "category": "math",
        "order": 21,
        "summary": (
            "Ikki tengsizlik birga berilsa, yechim ikki shtrixlangan sohaning "
            "umumiy qismi boʻladi. Nuqtani ikkala shartga qoʻyib tekshirish va "
            "byudjet + minimal talab modeli."
        ),
        "stories": ["Two Boxes on the Form"],
        "content": """
<h2>SAT-21: Systems of Linear Inequalities and Bounded Regions</h2>

<p>SAT-14 da bitta tengsizlikning grafigi tekislikning yarmi ekanini koʻrdik. Endi ikkita
tengsizlik birga beriladi — va yechim <mark>ikkalasining umumiy qismi</mark>, yaʼni ikki
shtrixlangan sohaning kesishmasi boʻladi. Hayotda bu juda tanish narsa: byudjetdan
chiqmaslik <u>va</u> kerakli miqdorni olish.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>tengsizliklar sistemasining yechimi nima ekanini bilasiz;</li>
    <li>nuqtani <u>ikkala</u> shartga qoʻyib 20 soniyada tekshirasiz;</li>
    <li>chegaralangan (<em>bounded</em>) va chegaralanmagan sohani farqlaysiz;</li>
    <li>«byudjet + minimal talab» modelini tengsizliklar sistemasi sifatida yozasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Solution region</span>
  <span class="pe-chip pe-chip--s">soha 1</span>
  <span class="pe-op">∩</span>
  <span class="pe-chip pe-chip--v">soha 2</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">umumiy qism</span>
</div>

<h3>Yechim — ikki sohaning kesishmasi</h3>

<p>Har bir tengsizlik oʻz yarim tekisligini beradi. Sistemaning yechimi esa faqat
<strong>ikkalasiga ham</strong> tegishli nuqtalardan iborat. Grafikda bu ikki shtrixning
ustma-ust tushgan joyi — koʻpincha uni qoraroq yoki boshqa rang bilan belgilashadi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 200" role="img" aria-label="Ikki tengsizlikning kesishgan sohasi">
    <polygon class="pm-fill pm-fill--hl" points="60,150 200,150 60,50"/>
    <line class="pm-ln" x1="20" y1="150" x2="300" y2="150"/>
    <line class="pm-ln" x1="60" y1="15" x2="60" y2="190"/>
    <line class="pm-ln pm-ln--hl" x1="35" y1="175" x2="250" y2="20"/>
    <line class="pm-ln pm-ln--hl pm-ln--dash" x1="30" y1="50" x2="300" y2="50"/>
    <text class="pm-lbl pm-lbl--hl" x="96" y="122">umumiy soha</text>
    <text class="pm-lbl" x="252" y="44">y = 4</text>
    <text class="pm-lbl" x="286" y="168">x</text>
  </svg>
  <figcaption>Boʻyalgan uchburchak — ikkala shart bir vaqtda bajariladigan yagona joy.</figcaption>
</figure>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Sistemadagi ikki tengsizlik «<b>va</b>» bilan bogʻlangan, «yoki» bilan emas. Bitta
  shartni qanoatlantirgan nuqta yechim boʻlmaydi — xuddi tenglamalar sistemasidagi
  kabi (SAT-16).
</div>

<h3>Nuqtani tekshirish — testdagi asosiy savol</h3>

<p>SAT bu mavzuni deyarli har doim bitta shaklda soʻraydi: <em>«which point is a solution
to the system?»</em> Chizish shart emas — har bir nuqtani ikkala tengsizlikka qoʻying.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">y ≥ x − 1  va  y &lt; 4;  nuqta (0, 0)</span>
    <span class="pm-solve__why">Tekshiramiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">0 ≥ 0 − 1 ✓</span>
    <span class="pm-solve__why">Birinchi shart bajarildi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">0 &lt; 4 ✓  →  (0, 0) yechim</span>
    <span class="pm-solve__why">Ikkinchisi ham bajarildi — demak nuqta umumiy sohada</span>
  </div>
</div>

<p>Bitta shart buzilsa, nuqta darhol chiqib ketadi. (5, 3) nuqtasi
<em>x</em> + <em>y</em> ≤ 6 shartini buzadi (8 ≤ 6 yolgʻon), shuning uchun boshqa shart
qanday boʻlishidan qatʼi nazar u yechim emas.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Chegara chizigʻining turi (uzuq yoki uzluksiz) har bir tengsizlik uchun
  <b>alohida</b> hal qilinadi. Bitta sistemada bir chiziq uzuq, ikkinchisi uzluksiz
  boʻlishi mutlaqo normal — SAT-14 dagi qoida har biriga oʻz-oʻzicha qoʻllanadi.
</div>

<h3>Chegaralangan va chegaralanmagan soha</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Bounded</p>
    <p>Soha hamma tomondan yopilgan — koʻpburchak hosil boʻladi. Uning
    <b>burchak nuqtalari</b> bor va amaliy masalalarda eng yaxshi yechim odatda
    oʻsha burchaklarda boʻladi.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Unbounded</p>
    <p>Soha bir tomonga cheksiz davom etadi. Masalan <em>y</em> ≥ 2 va
    <em>y</em> ≥ <em>x</em> — yuqoriga hech narsa chegara qoʻymaydi.</p>
  </div>
</div>

<h3>Hayotdagi model: byudjet va minimal talab</h3>

<p><em>A club buys pens at $2 each and notebooks at $5 each. It has at most $40 to spend and
needs at least 12 items in total.</em></p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2p + 5n ≤ 40</span>
    <span class="pm-solve__why">Byudjet — «at most» degani ≤ (SAT-15)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">p + n ≥ 12</span>
    <span class="pm-solve__why">Miqdor — «at least» degani ≥</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>12 ta ruchka va 2 ta daftar: narxi 24 + 10 = $34 ≤ 40 ✓, soni 14 ≥ 12 ✓ — ikkala
  shart ham bajarildi.</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Bunday savolda javoblar odatda toʻrtta juftlik boʻladi. Ularni <b>tezroq buziladigan</b>
  shartdan boshlab tekshiring — koʻpincha byudjet — va uch tanlov bir zumda oʻchadi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>which point is a solution to the system</b><span>qaysi nuqta sistemaning yechimi</span></li>
  <li><b>satisfies both inequalities</b><span>ikkala tengsizlikni ham qanoatlantiradi</span></li>
  <li><b>the shaded region</b><span>shtrixlangan soha — umumiy qism</span></li>
  <li><b>could be the number of</b><span>… soni boʻlishi mumkin (butun son va manfiy emas)</span></li>
  <li><b>at most … and at least …</b><span>koʻpi bilan … va kamida … — ikkita shart</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p><i>y</i> &gt; 2<i>x</i> − 3</p>
    <p><i>y</i> ≤ <i>x</i> + 1</p>
    <p>Which of the following points is a solution to the system above?</p>
  </div>
  <ol class="ps-ch">
    <li>(0, 0)</li>
    <li>(1, −2)</li>
    <li>(2, 5)</li>
    <li>(4, 2)</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) (0, 0)</p>
      <p>0 &gt; 2(0) − 3 = −3 ✓ va 0 ≤ 0 + 1 = 1 ✓ — ikkalasi ham rost.</p>
      <p>Qolganlari: (1, −2) → −2 &gt; −1 ✗; (2, 5) → 5 ≤ 3 ✗; (4, 2) → 2 &gt; 5 ✗.
      Har bir nuqta uchun ikki qator hisob — bu savol turi shunday yechiladi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">(2, 5)</span>
  <span class="ps-trap__why">Birinchi tengsizlikni qanoatlantiradi (5 &gt; 1), lekin
  ikkinchisini emas. <b>Bitta</b> shartni tekshirib toʻxtash — bu mavzudagi asosiy
  xato.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">90 s</span></p>
  <div class="ps-stem__q">
    <p>A club buys pens at $2 each and notebooks at $5 each. It can spend at most $40 and
    must buy at least 12 items in total. Which of the following combinations is
    possible?</p>
  </div>
  <ol class="ps-ch">
    <li>5 pens and 5 notebooks</li>
    <li>10 pens and 5 notebooks</li>
    <li>12 pens and 2 notebooks</li>
    <li>15 pens and 3 notebooks</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 12 pens and 2 notebooks</p>
      <p>Narxi: 24 + 10 = $34 ≤ 40 ✓. Soni: 14 ≥ 12 ✓.</p>
      <p>Qolganlari: 5 va 5 → atigi 10 ta narsa, 12 dan kam ✗; 10 va 5 → $45 ✗;
      15 va 3 → $45 ✗.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">10 pens and 5 notebooks</span>
  <span class="ps-trap__why">Miqdor sharti bajarildi (15 ≥ 12), lekin narxi $45 — byudjetdan
  $5 oshadi. Ikkala shartni ham hisoblamasdan javob tanlab boʻlmaydi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Tengsizliklar sistemasi savolida hech qachon chizmang:</p>
  <ol>
    <li>Nuqtani <b>birinchi</b> tengsizlikka qoʻying. Yolgʻon boʻlsa — tashlang,
        ikkinchisini hisoblamang.</li>
    <li>Rost boʻlsa, <b>ikkinchisini</b> tekshiring.</li>
    <li>Ikkalasi ham rost boʻlgan yagona nuqta — javob.</li>
  </ol>
  <p>Bir nuqta uchun oʻrtacha 10 soniya ketadi va toʻrttasi ham 40 soniyada tugaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Nuqta bitta tengsizlikni qanoatlantirsa — yechim.</p>
  <p class="pe-good">Ikkalasini ham qanoatlantirishi shart.</p>
  <p class="pe-fix__why">Yechim — sohalarning <b>kesishmasi</b>, yigʻindisi emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">«At least 12 items» → p + n ≤ 12</p>
  <p class="pe-good">p + n ≥ 12</p>
  <p class="pe-fix__why">«At least» — kamida, yaʼni pastki chegara (SAT-15). Bitta belgi
  butun sohani teskari tomonga oʻgiradi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Amaliy masalada yana ikkita «yashirin» shart bor: <b>p ≥ 0</b> va <b>n ≥ 0</b> —
  manfiy sonda ruchka sotib boʻlmaydi. SAT buni koʻpincha aytmaydi, lekin javoblarni
  tanlashda hisobga oladi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Is (0, 0) a solution to <i>y</i> ≥ <i>x</i> − 1 and <i>y</i> &lt; 4?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ha — 0 ≥ −1 ✓ va 0 &lt; 4 ✓. Ikkala shart ham bajarildi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Is (5, 3) a solution to <i>x</i> + <i>y</i> ≤ 6 and <i>y</i> ≥ 2?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — ikkinchi shart bajariladi (3 ≥ 2), lekin birinchisi
  buziladi: 5 + 3 = 8, va 8 ≤ 6 yolgʻon.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Is (1, 3) a solution to <i>x</i> + <i>y</i> ≤ 6 and <i>y</i> ≥ 2?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ha — 1 + 3 = 4 ≤ 6 ✓ va 3 ≥ 2 ✓.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Write the system for: «at most $50 spent on tickets costing $6 each and programmes
  costing $4 each, with at least 8 items bought».</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">6<i>t</i> + 4<i>p</i> ≤ 50 va <i>t</i> + <i>p</i> ≥ 8 —
  «at most» pul uchun ≤, «at least» soni uchun ≥.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Using that system, is 5 tickets and 4 programmes possible?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ha — narxi 30 + 16 = $46 ≤ 50 ✓ va soni 9 ≥ 8 ✓.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>system of inequalities</b><span>tengsizliklar sistemasi</span></li>
  <li><b>satisfies both</b><span>ikkalasini ham qanoatlantiradi</span></li>
  <li><b>the shaded region</b><span>shtrixlangan soha</span></li>
  <li><b>overlap</b><span>ustma-ust tushgan qism</span></li>
  <li><b>bounded / unbounded</b><span>chegaralangan / chegaralanmagan</span></li>
  <li><b>vertex (corner point)</b><span>burchak nuqtasi</span></li>
  <li><b>combination</b><span>juftlik, kombinatsiya</span></li>
  <li><b>constraint</b><span>shart, chegara</span></li>
  <li><b>at most / at least</b><span>koʻpi bilan / kamida</span></li>
  <li><b>possible</b><span>mumkin boʻlgan (ikkala shartga mos)</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Yechim — ikki sohaning <b>kesishmasi</b>: nuqta <b>ikkala</b> shartni ham
        qanoatlantirishi kerak.</li>
    <li>Chizmang — nuqtani <b>qoʻyib</b> tekshiring; bitta yolgʻon yetarli.</li>
    <li>«At most» → ≤ (byudjet), «at least» → ≥ (miqdor). Bitta soʻz sohani
        oʻgiradi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-22 — absolute value inequalities  (Block A closer)
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-22: Absolute Value Inequalities on the Number Line",
        "category": "math",
        "order": 22,
        "summary": (
            "«Kichik» modul oraliq beradi, «katta» modul esa ikki tomonni. Bitta "
            "belgi butun rasmni oʻzgartiradi — va bu Blok A ning oxirgi darsi."
        ),
        "stories": ["One Hertz Either Way"],
        "content": """
<h2>SAT-22: Absolute Value Inequalities on the Number Line</h2>

<p>SAT-4 da modulni <em>uzoqlik</em> deb oʻqigan edik va |<em>x</em>| = 7 ikki javob
bergan edi. Endi tenglik oʻrniga tengsizlik qoʻyamiz — va uzoqlik gʻoyasi darrov ish
beradi: <mark>«7 dan yaqin» butunlay boshqa rasm, «7 dan uzoq» esa yana boshqa</mark>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>|<em>x</em>| &lt; <em>a</em> ni oraliq (VA) deb oʻqiysiz;</li>
    <li>|<em>x</em>| &gt; <em>a</em> ni ikki tomon (YOKI) deb oʻqiysiz;</li>
    <li>modulni avval yolgʻiz qoldirasiz;</li>
    <li>meʼyor va chetlanish masalasini tengsizlik bilan yozasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The two shapes</span>
  <span class="pe-chip pe-chip--v">|x| &lt; a → −a &lt; x &lt; a</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--neg">|x| &gt; a → x &lt; −a yoki x &gt; a</span>
</div>

<h3>Kichik — oraliq, katta — ikki tomon</h3>

<p>|<em>x</em>| &lt; 5 degani «noldan uzoqligi 5 dan kichik». Bunday sonlar nolning
<u>atrofida</u> yotadi: −5 dan 5 gacha. Bu <strong>bitta oraliq</strong>, va u
«va» bilan bogʻlanadi: <em>x</em> &gt; −5 <b>va</b> <em>x</em> &lt; 5.</p>

<p>|<em>x</em>| &gt; 5 degani esa «noldan uzoqligi 5 dan katta» — bunday sonlar nolning
<u>chekkasida</u>: yo −5 dan chapda, yo 5 dan oʻngda. Bu <strong>ikki alohida
nur</strong>, va ular «yoki» bilan bogʻlanadi.</p>

<div class="pm-num">
  <div class="pm-num__track">
    <span class="pm-num__band" style="left:14.3%;width:71.4%"></span>
    <span class="pm-num__tick" style="left:0%"><i>−4</i></span>
    <span class="pm-num__tick" style="left:14.3%"><i>−2</i></span>
    <span class="pm-num__tick" style="left:50%"><i>3</i></span>
    <span class="pm-num__tick" style="left:85.7%"><i>8</i></span>
    <span class="pm-num__tick" style="left:100%"><i>10</i></span>
  </div>
</div>

<p>Yuqoridagi oraliq — |<em>x</em> − 3| &lt; 5 ning yechimi: 3 dan besh qadamdan
<b>yaqin</b> hamma sonlar, yaʼni −2 dan 8 gacha.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Yodlash uchun ikki soʻz yetadi: «<b>less</b> — <b>between</b>» va
  «<b>greater</b> — <b>outside</b>». Kichik boʻlsa markazga yaqin, katta boʻlsa
  markazdan uzoq. Boshqa hech narsani yodlash shart emas.
</div>

<h3>Misol 1 (oson) — oraliq</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">|x − 3| &lt; 5</span>
    <span class="pm-solve__why">«Kichik» — demak oraliq</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">−5 &lt; x − 3 &lt; 5</span>
    <span class="pm-solve__why">Ichkaridagi ifodani ikki chegara orasiga qoʻydik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">−2 &lt; x &lt; 8</span>
    <span class="pm-solve__why">Uchala qismga 3 ni qoʻshdik</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Uch qismli tengsizlikda amal <b>uchala</b> qismga bir vaqtda qoʻllanadi. Bu qulay
  yozuv: bitta qatorda ikkita tengsizlikni yechasiz.
</div>

<h3>Misol 2 (oʻrta) — ikki tomon</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">|2x + 1| ≥ 7</span>
    <span class="pm-solve__why">«Katta yoki teng» — demak ikki tomon</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + 1 ≥ 7  yoki  2x + 1 ≤ −7</span>
    <span class="pm-solve__why">Ikkinchi holda belgi ham agʻdariladi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x ≥ 3  yoki  x ≤ −4</span>
    <span class="pm-solve__why">Har birini alohida yechdik</span>
  </div>
</div>

<div class="pm-num">
  <div class="pm-num__track">
    <span class="pm-num__band" style="left:0%;width:26.7%"></span>
    <span class="pm-num__band" style="left:73.3%;width:26.7%"></span>
    <span class="pm-num__tick" style="left:0%"><i>−8</i></span>
    <span class="pm-num__tick" style="left:26.7%"><i>−4</i></span>
    <span class="pm-num__tick" style="left:53.3%"><i>0</i></span>
    <span class="pm-num__tick" style="left:73.3%"><i>3</i></span>
    <span class="pm-num__tick" style="left:100%"><i>7</i></span>
  </div>
</div>

<p>Eʼtibor bering: oʻrtadagi qism — <em>x</em> = 0 ni oʻz ichiga olgan boʻshliq —
yechim <b>emas</b>. Tekshiring: <em>x</em> = 0 da |2(0) + 1| = 1, va 1 ≥ 7 yolgʻon ✓</p>

<h3>Misol 3 (SAT darajasi) — avval izolyatsiya</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3|x| + 2 &lt; 14</span>
    <span class="pm-solve__why">Modul yolgʻiz emas</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3|x| &lt; 12  →  |x| &lt; 4</span>
    <span class="pm-solve__why">2 ni ayirdik, 3 ga boʻldik (musbat — agʻdarish yoʻq)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">−4 &lt; x &lt; 4</span>
    <span class="pm-solve__why">Endi «kichik» qoidasini qoʻlladik</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Modul <b>yolgʻiz qolmaguncha</b> ikkiga ajratmang. 3|<i>x</i>| + 2 &lt; 14 ni birdan
  −14 &lt; 3<i>x</i> + 2 &lt; 14 deb yozish — bu butunlay boshqa tengsizlik.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Katta» holatda javob <b>ikki qismdan</b> iborat va ular orasida «yoki» turadi.
  Ularni bitta zanjirga yozib boʻlmaydi: 3 &lt; <i>x</i> &lt; −4 degan yozuv
  maʼnosiz, chunki hech bir son bir vaqtda 3 dan katta va −4 dan kichik boʻlolmaydi.
</div>

<h3>Hayotdagi maʼnosi: meʼyor va chetlanish</h3>

<p>SAT-4 dagi suv shishasini eslang: hajm 500 millilitrdan 8 dan koʻp farq qilsa,
shisha rad etilardi. Tengsizlik tilida <em>qabul qilinadigan</em> shishalar shunday
yoziladi: |<em>v</em> − 500| ≤ 8, yaʼni <strong>492 ≤ v ≤ 508</strong>.</p>

<div class="pe-ex">
  <p class="pe-ex__math">|v − 500| ≤ 8  →  492 ≤ v ≤ 508</p>
  <p class="pe-ex__uz">Meʼyor 500, ruxsat etilgan chetlanish 8 — natija oraliq.</p>
  <p class="pe-ex__why">Modul ichidagi son — markaz; oʻng tomondagi son — ruxsat etilgan uzoqlik.</p>
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>which describes all values of x</b><span>x ning barcha qiymatlari qaysi javobda</span></li>
  <li><b>within 8 of 500</b><span>500 dan 8 dan uzoq emas — ≤ oraligʻi</span></li>
  <li><b>differs from … by more than</b><span>…dan koʻproq farq qiladi — ikki tomon</span></li>
  <li><b>the solution set</b><span>yechimlar toʻplami</span></li>
  <li><b>on the number line</b><span>sonlar oʻqida</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>Which of the following describes all values of <i>x</i> for which
    |<i>x</i> − 4| ≤ 6?</p>
  </div>
  <ol class="ps-ch">
    <li>−10 ≤ <i>x</i> ≤ 10</li>
    <li>−2 ≤ <i>x</i> ≤ 10</li>
    <li><i>x</i> ≤ −2 or <i>x</i> ≥ 10</li>
    <li><i>x</i> ≤ 2 or <i>x</i> ≥ 6</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) −2 ≤ x ≤ 10</p>
      <p>«Kichik yoki teng» — demak oraliq: −6 ≤ x − 4 ≤ 6, uchala qismga 4 ni
      qoʻshamiz.</p>
      <p>Tekshiruv: x = 0 → |0 − 4| = 4 ≤ 6 ✓ va 0 haqiqatan −2 bilan 10 orasida.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">x ≤ −2 or x ≥ 10</span>
  <span class="ps-trap__why">Sonlar toʻgʻri topilgan, lekin rasm teskari: «kichik» oraliq
  beradi, ikki tomon emas. Bitta son qoʻyib tekshiring — x = 0 javobni hal qiladi.</span>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">−10 ≤ x ≤ 10</span>
  <span class="ps-trap__why">Markaz 0 deb olingan. Modul ichida <b>x − 4</b> turibdi,
  demak markaz 4 — chegaralar 4 dan olti qadam narida.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>Which of the following describes all values of <i>x</i> for which
    |2<i>x</i> − 5| &gt; 3?</p>
  </div>
  <ol class="ps-ch">
    <li>1 &lt; <i>x</i> &lt; 4</li>
    <li><i>x</i> &lt; 1 or <i>x</i> &gt; 4</li>
    <li><i>x</i> &lt; −4 or <i>x</i> &gt; 1</li>
    <li><i>x</i> &gt; 4</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) x &lt; 1 or x &gt; 4</p>
      <div class="pm-solve">
        <div class="pm-solve__row">
          <span class="pm-solve__step">2x − 5 &gt; 3  →  x &gt; 4</span>
          <span class="pm-solve__why">Birinchi tomon</span>
        </div>
        <div class="pm-solve__row pm-solve__row--ans">
          <span class="pm-solve__step">2x − 5 &lt; −3  →  x &lt; 1</span>
          <span class="pm-solve__why">Ikkinchi tomon, belgi agʻdarilgan holda</span>
        </div>
      </div>
      <p><b>x &gt; 4</b> — yarim javob: u faqat bitta tomonni beradi. «Katta» modul
      <b>har doim</b> ikki qismdan iborat.</p>
    </div>
  </details>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Modulli tengsizlik savolida javoblarni son qoʻyib oʻchiring:</p>
  <ol>
    <li>Modul ichidagini nolga aylantiradigan sonni toping (markaz).</li>
    <li><b>Markazning oʻzini</b> asl tengsizlikka qoʻying. «Kichik» boʻlsa u rost
        chiqadi — demak javob oraliq; «katta» boʻlsa yolgʻon — demak ikki tomon.</li>
    <li>Qolgan ikki javobni chegara soni bilan ajrating.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">|x| &gt; 5  →  −5 &lt; x &lt; 5</p>
  <p class="pe-good">x &lt; −5 yoki x &gt; 5</p>
  <p class="pe-fix__why">«Katta» — markazdan <b>uzoq</b>, demak ikki chekka; oraliq
  esa «kichik»ning javobi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">|x − 4| ≤ 6  →  −6 ≤ x ≤ 6</p>
  <p class="pe-good">−2 ≤ x ≤ 10</p>
  <p class="pe-fix__why">Uchala qismga 4 ni qoʻshish unutilgan. Markaz — 0 emas,
  <b>4</b>.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu dars bilan Blok A tugadi. Ifodadan (SAT-1) boshlab tenglama, chiziq, tengsizlik va
  sistemagacha yetib keldik — SAT Math'ning taxminan uchdan biri shu 22 darsda.
  Keyingi dars boshqa dunyo: <b>daraja va ildiz</b>.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Solve: |<i>x</i>| &lt; 5</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">−5 &lt; <i>x</i> &lt; 5 — «kichik» oraliq beradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Solve: |<i>x</i>| ≥ 3</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> ≤ −3 yoki <i>x</i> ≥ 3 — «katta» ikki tomonni
  beradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Solve: |<i>x</i> + 2| &lt; 6</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">−8 &lt; <i>x</i> &lt; 4 — −6 &lt; x + 2 &lt; 6, keyin uchala
  qismdan 2 ni ayiramiz.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Solve: 2|<i>x</i>| − 1 &gt; 9</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> &lt; −5 yoki <i>x</i> &gt; 5 — avval izolyatsiya:
  2|x| &gt; 10 → |x| &gt; 5, keyin «katta» qoidasi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A machine fills bottles to 500 millilitres. A bottle is accepted if its volume differs
  from 500 by no more than 8 millilitres. Write this as an inequality and give the
  accepted range.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">|<i>v</i> − 500| ≤ 8, demak 492 ≤ <i>v</i> ≤ 508. «No more
  than» — oraliq beradi.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>absolute value inequality</b><span>modulli tengsizlik</span></li>
  <li><b>between</b><span>orasida (oraliq javob)</span></li>
  <li><b>or</b><span>yoki (ikki tomonli javob)</span></li>
  <li><b>within … of …</b><span>…dan … dan uzoq emas</span></li>
  <li><b>differs by more than</b><span>…dan koʻproq farq qiladi</span></li>
  <li><b>solution set</b><span>yechimlar toʻplami</span></li>
  <li><b>number line</b><span>sonlar oʻqi</span></li>
  <li><b>tolerance</b><span>ruxsat etilgan chetlanish</span></li>
  <li><b>isolate the absolute value</b><span>modulni yolgʻiz qoldirish</span></li>
  <li><b>compound inequality</b><span>uch qismli tengsizlik</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Less → between</b> (bitta oraliq), <b>greater → outside</b> (ikki tomon).</li>
    <li>Modulni <b>yolgʻiz qoldiring</b>, keyin ikkiga ajrating.</li>
    <li>Markaz — modul ichidagini nolga aylantiruvchi son; chegaralar undan teng
        uzoqlikda.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-23 — laws of exponents  (Block B opener)
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-23: Laws of Exponents: Multiplication, Division, and Power-to-Power",
        "category": "math",
        "order": 23,
        "summary": (
            "Daraja qonunlari: koʻpaytirganda koʻrsatkichlar qoʻshiladi, boʻlganda "
            "ayriladi, darajaning darajasida koʻpaytiriladi. Advanced Math blokining "
            "birinchi darsi."
        ),
        "stories": ["The Chessboard and the Rice"],
        "content": """
<h2>SAT-23: Laws of Exponents: Multiplication, Division, and Power-to-Power</h2>

<p>Bu yerdan SAT'ning ikkinchi katta bloki — <strong>Advanced Math</strong> — boshlanadi.
U testning yana taxminan 35 foizini tashkil qiladi va deyarli hammasi bitta poydevorga
tayanadi: <mark>daraja qonunlari</mark>. Ular uchta, ular qisqa, va ularni chalkashtirish
Blok B dagi eng koʻp uchraydigan xato.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>bir xil asosli darajalarni koʻpaytirasiz va boʻlasiz;</li>
    <li>darajaning darajasini hisoblaysiz;</li>
    <li>koeffitsientni ham darajaga koʻtarishni unutmaysiz;</li>
    <li>«qoʻshish» va «koʻpaytirish» qonunlarini adashtirmaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Three laws</span>
  <span class="pe-chip pe-chip--v">x<sup>a</sup> · x<sup>b</sup> = x<sup>a+b</sup></span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">x<sup>a</sup> ÷ x<sup>b</sup> = x<sup>a−b</sup></span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">(x<sup>a</sup>)<sup>b</sup> = x<sup>ab</sup></span>
</div>

<h3>Nega qoʻshiladi — sanab koʻring</h3>

<p>Qonunni yodlashdan oldin bir marta ochib koʻring. <em>x</em><sup>3</sup> ·
<em>x</em><sup>2</sup> degani (<em>x</em>·<em>x</em>·<em>x</em>) · (<em>x</em>·<em>x</em>) —
jami beshta <em>x</em>. Shuning uchun natija <em>x</em><sup>5</sup>, va shuning uchun
koʻrsatkichlar <b>qoʻshiladi</b>, koʻpaytirilmaydi.</p>

<div class="pe-ex">
  <p class="pe-ex__math">3<sup>4</sup> · 3<sup>2</sup> = 3<sup>6</sup> = 729</p>
  <p class="pe-ex__uz">Toʻrtta uchlik va ikkita uchlik — jami oltita uchlik.</p>
  <p class="pe-ex__why">Asos oʻzgarmaydi: javob 9<sup>6</sup> emas, 3<sup>6</sup>.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Qonun faqat <b>asoslar bir xil</b> boʻlganda ishlaydi. 2<sup>3</sup> · 5<sup>2</sup>
  ni bitta darajaga birlashtirib boʻlmaydi — uni faqat hisoblash mumkin: 8 × 25 = 200.
</div>

<h3>Boʻlish — ayirish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x<sup>7</sup> ÷ x<sup>3</sup></span>
    <span class="pm-solve__why">Yettita x ni uchta x ga boʻlyapmiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x<sup>4</sup></span>
    <span class="pm-solve__why">Uchtasi qisqardi, toʻrttasi qoldi: 7 − 3 = 4</span>
  </div>
</div>

<h3>Darajaning darajasi — koʻpaytirish</h3>

<p>(<em>x</em><sup>3</sup>)<sup>5</sup> degani <em>x</em><sup>3</sup> ni oʻzini besh marta
koʻpaytirish. Har birida uchta <em>x</em> bor, jami 3 × 5 = 15 ta. Demak
<strong><em>x</em><sup>15</sup></strong>.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Koʻpaytirish</p>
    <p><i>x</i><sup>3</sup> · <i>x</i><sup>5</sup> = <i>x</i><sup>8</sup></p>
    <p>Koʻrsatkichlar <b>qoʻshiladi</b>.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Darajaning darajasi</p>
    <p>(<i>x</i><sup>3</sup>)<sup>5</sup> = <i>x</i><sup>15</sup></p>
    <p>Koʻrsatkichlar <b>koʻpaytiriladi</b>.</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu ikkisini ajratishning eng oson yoʻli — <b>qavsga qarash</b>. Qavs boʻlsa
  (<i>x</i><sup>3</sup>)<sup>5</sup> — koʻpaytiring. Qavs boʻlmasa va nuqta (yoki yonma-yon
  yozuv) boʻlsa — qoʻshing. SAT ikkisini bitta savolning javoblari qilib qoʻyadi.
</div>

<h3>Koeffitsient ham darajaga koʻtariladi</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">(2x<sup>2</sup>)<sup>3</sup></span>
    <span class="pm-solve__why">Qavs ichida <b>ikkita</b> narsa bor: 2 va x<sup>2</sup></span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2<sup>3</sup> · (x<sup>2</sup>)<sup>3</sup></span>
    <span class="pm-solve__why">Har biri alohida darajaga koʻtariladi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">8x<sup>6</sup></span>
    <span class="pm-solve__why">2<sup>3</sup> = 8 va 2 × 3 = 6</span>
  </div>
</div>

<p>Bu — SAT'da eng koʻp yoʻqotiladigan bir ochko. Koʻpchilik <em>x</em> ni toʻgʻri
hisoblaydi va 2 ni <u>tegmasdan</u> qoldiradi: 2<em>x</em><sup>6</sup> deb yozadi.
Javoblar orasida bu variant har doim turadi.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Daraja qonunlari <b>qoʻshishga qoʻllanmaydi</b>:
  <i>x</i><sup>2</sup> + <i>x</i><sup>3</sup> ni <i>x</i><sup>5</sup> deb yozib
  boʻlmaydi. Qonunlar faqat koʻpaytirish, boʻlish va darajaga koʻtarish uchun —
  qoʻshiluvchi darajalar oʻxshash hadlar boʻlmasa, shundayligicha qoladi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>which expression is equivalent to</b><span>qaysi ifoda teng kuchli</span></li>
  <li><b>simplify the expression</b><span>ifodani soddalashtiring</span></li>
  <li><b>in terms of x</b><span>x orqali ifodalangan holda</span></li>
  <li><b>where x &gt; 0</b><span>x musbat — ildiz va boʻlish uchun shart</span></li>
  <li><b>the base / the exponent</b><span>asos / koʻrsatkich</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>Which expression is equivalent to (2<i>x</i><sup>3</sup>)<sup>4</sup>?</p>
  </div>
  <ol class="ps-ch">
    <li>8<i>x</i><sup>7</sup></li>
    <li>8<i>x</i><sup>12</sup></li>
    <li>16<i>x</i><sup>7</sup></li>
    <li>16<i>x</i><sup>12</sup></li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: D) 16x<sup>12</sup></p>
      <p>Qavs ichidagi <b>har bir</b> koʻpaytuvchi toʻrtinchi darajaga koʻtariladi:
      2<sup>4</sup> = 16, va (<i>x</i><sup>3</sup>)<sup>4</sup> = <i>x</i><sup>12</sup>.</p>
      <p>Tekshirish uchun <i>x</i> = 1 qoʻying: (2)<sup>4</sup> = 16, va faqat ikki javob
      16 bilan boshlanadi — qolganini koʻrsatkich hal qiladi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">8x<sup>12</sup></span>
  <span class="ps-trap__why">Koeffitsient notoʻgʻri: 2<sup>4</sup> = 16, 8 emas
  (8 — bu 2<sup>3</sup>). Koʻrsatkich toʻgʻri, lekin son yarim yoʻlda qolgan.</span>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">16x<sup>7</sup></span>
  <span class="ps-trap__why">Koʻrsatkichlar qoʻshilgan (3 + 4), lekin qavs bor —
  demak ular <b>koʻpaytirilishi</b> kerak edi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>For <i>x</i> &gt; 0, which expression is equivalent to
    (<i>x</i><sup>5</sup> · <i>x</i><sup>3</sup>) ÷ <i>x</i><sup>2</sup>?</p>
  </div>
  <ol class="ps-ch">
    <li><i>x</i><sup>6</sup></li>
    <li><i>x</i><sup>10</sup></li>
    <li><i>x</i><sup>13</sup></li>
    <li><i>x</i><sup>15</sup></li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) x<sup>6</sup></p>
      <p>Avval koʻpaytirish: 5 + 3 = 8. Keyin boʻlish: 8 − 2 = 6.</p>
      <p><b>x<sup>10</sup></b> — boʻlishda ayirish oʻrniga qoʻshgan javob;
      <b>x<sup>15</sup></b> — koʻpaytirishda 5 × 3 qilgan javob.</p>
    </div>
  </details>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Daraja savolida ikkilanib qolsangiz, <b>kichik son qoʻying</b>:</p>
  <ol>
    <li><i>x</i> = 2 ni asl ifodaga qoʻyib, bitta son chiqaring.</li>
    <li>Har bir javobga ham <i>x</i> = 2 ni qoʻying.</li>
    <li>Mos kelgani — javob.</li>
  </ol>
  <p><i>x</i> = 1 ni tanlamang: u koʻrsatkichlar orasidagi farqni yashiradi. 2 yoki 3
  eng qulayi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">x<sup>3</sup> · x<sup>5</sup> = x<sup>15</sup></p>
  <p class="pe-good">x<sup>8</sup></p>
  <p class="pe-fix__why">Koʻpaytirganda koʻrsatkichlar <b>qoʻshiladi</b>. Koʻpaytirish
  faqat qavs boʻlganda (darajaning darajasida) boʻladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">(3x<sup>2</sup>)<sup>2</sup> = 3x<sup>4</sup></p>
  <p class="pe-good">9x<sup>4</sup></p>
  <p class="pe-fix__why">Koeffitsient ham qavs ichida: 3<sup>2</sup> = 9. Uni tegmasdan
  qoldirish — bu mavzudagi eng qimmat xato.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Koʻrsatkich <b>faqat</b> oʻzi turgan belgiga tegishli. 3<i>x</i><sup>2</sup> da kvadratga
  koʻtarilgan narsa — faqat <i>x</i>, 3 emas. Lekin (3<i>x</i>)<sup>2</sup> da qavs
  ikkalasini ham qamrab oladi va natija 9<i>x</i><sup>2</sup> boʻladi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Simplify: <i>x</i><sup>4</sup> · <i>x</i><sup>6</sup></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i><sup>10</sup> — asos bir xil, koʻrsatkichlar
  qoʻshiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Simplify: <i>y</i><sup>9</sup> ÷ <i>y</i><sup>4</sup></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>y</i><sup>5</sup> — boʻlganda koʻrsatkichlar
  ayriladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Simplify: (<i>x</i><sup>4</sup>)<sup>3</sup></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i><sup>12</sup> — qavs bor, demak koʻrsatkichlar
  koʻpaytiriladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Simplify: (3<i>x</i><sup>2</sup><i>y</i>)<sup>2</sup></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">9<i>x</i><sup>4</sup><i>y</i><sup>2</sup> — qavs ichidagi
  uchala koʻpaytuvchi ham kvadratga koʻtariladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A single bacterium doubles every hour. Written as a power of 2, how many are there
  after 10 hours — and how many is that?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">2<sup>10</sup> = 1,024 ta. Har soat ikkiga koʻpayish —
  har safar bitta 2 qoʻshilishi demak.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>exponent / power</b><span>koʻrsatkich / daraja</span></li>
  <li><b>base</b><span>asos (pastdagi son)</span></li>
  <li><b>equivalent expression</b><span>teng kuchli ifoda</span></li>
  <li><b>simplify</b><span>soddalashtirish</span></li>
  <li><b>coefficient</b><span>koeffitsient (harf oldidagi son)</span></li>
  <li><b>squared / cubed</b><span>kvadrat / kub</span></li>
  <li><b>raised to the power of</b><span>… darajaga koʻtarilgan</span></li>
  <li><b>the same base</b><span>bir xil asos — qonunlar faqat shunda ishlaydi</span></li>
  <li><b>product / quotient</b><span>koʻpaytma / boʻlinma</span></li>
  <li><b>doubles</b><span>ikki barobar ortadi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Koʻpaytirsa <b>qoʻsh</b>, boʻlsa <b>ayir</b>, qavs boʻlsa
        <b>koʻpaytir</b>.</li>
    <li>Qavs ichidagi <b>koeffitsient ham</b> darajaga koʻtariladi:
        (2x<sup>3</sup>)<sup>4</sup> = 16x<sup>12</sup>.</li>
    <li>Qonunlar faqat <b>bir xil asos</b> uchun. Ikkilansangiz — x = 2 qoʻyib
        tekshiring.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-24 — negative and fractional exponents
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-24: Negative and Fractional Exponents",
        "category": "math",
        "order": 24,
        "summary": (
            "Nol daraja nega 1 ga teng, manfiy koʻrsatkich nega kasr beradi va "
            "kasr koʻrsatkich nega ildizdan boshqa narsa emas."
        ),
        "stories": ["Why A4 Is That Shape"],
        "content": """
<h2>SAT-24: Negative and Fractional Exponents</h2>

<p>Koʻrsatkich butun va musbat boʻlsa, hammasi tushunarli: 2<sup>3</sup> — bu uchta ikkilik.
Lekin 2<sup>0</sup>, 2<sup>−3</sup> va 8<sup>2/3</sup> nima degani? Ular
<mark>bir xil qonunlarning davomi</mark> — va SAT ularni juda yaxshi koʻradi, chunki
qoidani tushunmasdan yodlaganlar bu yerda albatta adashadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>nol darajaning nega 1 ekanini tushuntirasiz;</li>
    <li>manfiy koʻrsatkichni kasrga aylantirasiz;</li>
    <li>kasr koʻrsatkichni ildiz sifatida oʻqiysiz;</li>
    <li>8<sup>2/3</sup> kabi ifodani hisoblab, javobni butun songa keltirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Three rules</span>
  <span class="pe-chip pe-chip--v">x<sup>0</sup> = 1</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--neg">x<sup>−n</sup> = 1 ÷ x<sup>n</sup></span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">x<sup>m/n</sup> = (<sup>n</sup>√x)<sup>m</sup></span>
</div>

<h3>Nega nol daraja 1 ga teng</h3>

<p>Yodlash shart emas — SAT-23 dagi boʻlish qonunidan chiqadi.
<em>x</em><sup>3</sup> ÷ <em>x</em><sup>3</sup> ni ikki xil hisoblang: bir tomondan har
qanday son oʻziga boʻlinganda <b>1</b>; ikkinchi tomondan qonun boʻyicha
<em>x</em><sup>3−3</sup> = <em>x</em><sup>0</sup>. Demak <em>x</em><sup>0</sup> = 1.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu 5<sup>0</sup> uchun ham, 1000<sup>0</sup> uchun ham, hatto
  (−7)<sup>0</sup> uchun ham toʻgʻri: hammasi <b>1</b>. Yagona istisno — 0<sup>0</sup>,
  lekin SAT'da u hech qachon uchramaydi.
</div>

<h3>Manfiy koʻrsatkich — «pastga tush» degani</h3>

<p>Xuddi shu boʻlish qonunini davom ettiring: <em>x</em><sup>2</sup> ÷ <em>x</em><sup>5</sup>
qonun boʻyicha <em>x</em><sup>−3</sup>, lekin ochib yozsak
1 ÷ <em>x</em><sup>3</sup> chiqadi. Demak <strong>manfiy koʻrsatkich ifodani maxrajga
tushiradi</strong> — u sonni <u>manfiy qilmaydi</u>.</p>

<div class="pe-ex">
  <p class="pe-ex__math">2<sup>−3</sup> = 1 ÷ 2<sup>3</sup> = 1/8</p>
  <p class="pe-ex__uz">Javob musbat va birdan kichik — manfiy emas.</p>
  <p class="pe-ex__why">Minus «pastga», yaʼni maxrajga koʻchishni bildiradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">2<sup>−3</sup> = −8</p>
  <p class="pe-good">2<sup>−3</sup> = 1/8</p>
  <p class="pe-fix__why">Manfiy koʻrsatkich <b>ishorani</b> emas, <b>oʻrinni</b>
  oʻzgartiradi: son maxrajga tushadi.</p>
</div>

<h3>Kasr koʻrsatkich — bu ildiz</h3>

<blockquote><em>x</em><sup>1/2</sup> = √<em>x</em>, va umuman
<em>x</em><sup>1/n</sup> — bu <em>n</em>-darajali ildiz. Maxraj ildizni,
surat esa darajani bildiradi.</blockquote>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Yozuv</th><th>Maʼnosi</th><th>Qiymati</th></tr>
  <tr><td>16<sup>1/2</sup></td><td class="pm-word__sym">√16</td><td>4</td></tr>
  <tr><td>27<sup>1/3</sup></td><td class="pm-word__sym"><sup>3</sup>√27</td><td>3</td></tr>
  <tr><td>8<sup>2/3</sup></td><td class="pm-word__sym">(<sup>3</sup>√8)<sup>2</sup></td><td>4</td></tr>
  <tr><td>9<sup>−1/2</sup></td><td class="pm-word__sym">1 ÷ √9</td><td>1/3</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Kasr koʻrsatkichda <b>avval ildizni</b> oling, keyin darajaga koʻtaring. 8<sup>2/3</sup>
  uchun avval ∛8 = 2, keyin 2<sup>2</sup> = 4 — sonlar kichik boʻlib qoladi. Teskari
  tartibda 8<sup>2</sup> = 64 chiqadi va ∛64 ni hisoblash kerak boʻladi.
</div>

<h3>Misol (SAT darajasi)</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">16<sup>3/4</sup></span>
    <span class="pm-solve__why">Maxraj 4 — toʻrtinchi darajali ildiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step"><sup>4</sup>√16 = 2</span>
    <span class="pm-solve__why">2 × 2 × 2 × 2 = 16</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2<sup>3</sup> = 8</span>
    <span class="pm-solve__why">Surat 3 — natijani kubga koʻtaramiz</span>
  </div>
</div>

<h3>Uchtasi birga: manfiy kasr koʻrsatkich</h3>

<p>SAT ba'zan uchala qoidani bitta ifodaga yigʻadi. Tartib doim bir xil: avval ildiz,
keyin daraja, oxirida minus.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">27<sup>−2/3</sup></span>
    <span class="pm-solve__why">Uchta belgi: minus, surat 2, maxraj 3</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step"><sup>3</sup>√27 = 3</span>
    <span class="pm-solve__why">Maxraj — ildizning darajasi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3<sup>2</sup> = 9</span>
    <span class="pm-solve__why">Surat — daraja</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">1/9</span>
    <span class="pm-solve__why">Minus natijani maxrajga tushirdi</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Minusni <b>oxirida</b> qoʻllash odat qiling. Uni boshida qoʻllasangiz, kasr bilan
  ildiz olishga toʻgʻri keladi va hisob keraksiz ogʻirlashadi — javob esa oʻsha.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>what is the value of</b><span>qiymati qancha — javob son</span></li>
  <li><b>which is equivalent to</b><span>qaysi ifoda teng kuchli</span></li>
  <li><b>expressed as a fraction</b><span>kasr koʻrinishida</span></li>
  <li><b>the cube root of</b><span>kub ildiz (uchinchi darajali)</span></li>
  <li><b>for x &gt; 0</b><span>x musbat — kasr koʻrsatkich uchun shart</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>What is the value of 8<sup>2/3</sup>?</p>
  </div>
  <ol class="ps-ch">
    <li>2</li>
    <li>4</li>
    <li>16</li>
    <li>512</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 4</p>
      <p>Maxraj 3 — kub ildiz: ∛8 = 2. Surat 2 — kvadratga koʻtaramiz: 2<sup>2</sup> = 4.</p>
      <p><b>2</b> — faqat ildiz olingan, daraja qoʻllanmagan. <b>512</b> — 8<sup>3</sup>,
      yaʼni kasrni butunlay teskari oʻqigan javob.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">16</span>
  <span class="ps-trap__why">8 ni 2 ga koʻpaytirgan javob (kasrni «2 marta» deb
  oʻqigan). Kasr koʻrsatkich koʻpaytirish emas — u ildiz va daraja.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>What is the value of 16<sup>3/4</sup>?</p>
  </div>
  <ol class="ps-ch">
    <li>8</li>
    <li>12</li>
    <li>48</li>
    <li>64</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 8</p>
      <p>Toʻrtinchi darajali ildiz: <sup>4</sup>√16 = 2, chunki 2<sup>4</sup> = 16.
      Keyin 2<sup>3</sup> = 8.</p>
      <p><b>64</b> — kvadrat ildiz olingan (√16 = 4), keyin kubga koʻtarilgan: maxraj
      4 edi, 2 emas. <b>48</b> — 16 × 3 hisoblangan javob.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">64</span>
  <span class="ps-trap__why">Maxrajni 2 deb oʻqigan: √16 = 4, keyin 4<sup>3</sup> = 64.
  Maxraj <b>ildizning darajasini</b> aytadi — bu yerda toʻrtinchi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Kasr koʻrsatkichni uch soʻz bilan oʻqing: «<b>maxraj — ildiz, surat — daraja</b>».</p>
  <ol>
    <li>Maxrajga qarang va ildizni oling — son kichrayadi.</li>
    <li>Suratga qarang va shu darajaga koʻtaring.</li>
    <li>Old tomonda minus boʻlsa, oxirida javobni <b>maxrajga</b> tushiring.</li>
  </ol>
  <p>Masalan 27<sup>−2/3</sup>: ∛27 = 3, 3<sup>2</sup> = 9, minus tufayli javob 1/9.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">x<sup>0</sup> = 0</p>
  <p class="pe-good">x<sup>0</sup> = 1</p>
  <p class="pe-fix__why">Har qanday son oʻziga boʻlinganda 1 chiqadi — nol daraja
  aynan shundan kelib chiqadi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Kasrning oʻzi manfiy koʻrsatkich bilan <b>agʻdariladi</b>:
  (1/2)<sup>−2</sup> = 2<sup>2</sup> = 4. Bu qoida SAT'da tez-tez chiqadi va uni
  bilgan oʻquvchi savolni bir qatorda yopadi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  What is the value of 3<sup>−2</sup>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">1/9 — manfiy koʻrsatkich maxrajga tushiradi:
  1 ÷ 3<sup>2</sup>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  What is the value of 25<sup>1/2</sup>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">5 — 1/2 koʻrsatkichi kvadrat ildizni bildiradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  What is the value of 27<sup>2/3</sup>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">9 — avval ∛27 = 3, keyin 3<sup>2</sup> = 9.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Write <i>x</i><sup>−4</sup> as a fraction.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">1 ÷ <i>x</i><sup>4</sup> — koʻrsatkich musbat boʻlib
  maxrajga oʻtadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  What is the value of 32<sup>1/5</sup>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">2 — beshinchi darajali ildiz, chunki
  2<sup>5</sup> = 32.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>negative exponent</b><span>manfiy koʻrsatkich</span></li>
  <li><b>fractional exponent</b><span>kasr koʻrsatkich</span></li>
  <li><b>square root / cube root</b><span>kvadrat ildiz / kub ildiz</span></li>
  <li><b>reciprocal</b><span>teskari son (1 boʻlingan son)</span></li>
  <li><b>numerator / denominator</b><span>surat / maxraj</span></li>
  <li><b>zero exponent</b><span>nol daraja</span></li>
  <li><b>equivalent form</b><span>teng kuchli koʻrinish</span></li>
  <li><b>evaluate</b><span>qiymatini hisoblang</span></li>
  <li><b>radical</b><span>ildiz belgisi bilan yozilgan ifoda</span></li>
  <li><b>perfect cube</b><span>toʻliq kub (8, 27, 64…)</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>x<sup>0</sup> = 1</b> — har doim, har qanday asos uchun (0 dan tashqari).</li>
    <li>Manfiy koʻrsatkich <b>maxrajga tushiradi</b>, sonni manfiy qilmaydi.</li>
    <li>Kasrda <b>maxraj — ildiz, surat — daraja</b>; avval ildizni oling.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-25 — simplifying radicals
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-25: Simplifying Radical Expressions",
        "category": "math",
        "order": 25,
        "summary": (
            "Ildiz ostidan toʻliq kvadratni chiqarish, oʻxshash ildizlarni qoʻshish "
            "va ikki ildizni koʻpaytirish — SAT javoblari deyarli har doim "
            "soddalashtirilgan koʻrinishda beriladi."
        ),
        "stories": ["Two Hundred Square Metres"],
        "content": """
<h2>SAT-25: Simplifying Radical Expressions</h2>

<p>SAT javoblari orasida √50 ni koʻrmaysiz — u yerda <strong>5√2</strong> turadi. Ikkalasi
bir xil son, lekin test har doim <mark>soddalashtirilgan koʻrinishni</mark> talab qiladi.
Shuning uchun toʻgʻri hisoblab, javobni javoblar orasidan topa olmaslik — bu mavzudagi
eng koʻp uchraydigan yoʻqotish.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>ildiz ostidan toʻliq kvadratni chiqarasiz;</li>
    <li>qaysi ildizlarni qoʻshish mumkinligini bilasiz;</li>
    <li>ikki ildizni koʻpaytirasiz va natija butun son boʻlishini koʻrasiz;</li>
    <li>javobni SAT kutgan koʻrinishga keltirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The one rule</span>
  <span class="pe-chip pe-chip--s">√(a · b)</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">√a</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">√b</span>
</div>

<h3>Toʻliq kvadratni ajratib oling</h3>

<p>Soddalashtirish bitta savolga tayanadi: <em>ildiz ostidagi sonning toʻliq kvadrat
boʻluvchisi bormi?</em> Toʻliq kvadratlar: 4, 9, 16, 25, 36, 49, 64, 81, 100 — ularni
yod bilish kerak.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">√50</span>
    <span class="pm-solve__why">50 = 25 × 2, va 25 — toʻliq kvadrat</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">√25 · √2</span>
    <span class="pm-solve__why">Koʻpaytmaning ildizi — ildizlarning koʻpaytmasi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">5√2</span>
    <span class="pm-solve__why">√25 = 5 chiqib ketdi, √2 qoldi</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  <b>Eng katta</b> toʻliq kvadratni qidiring. √72 uchun 4 ni olsangiz 2√18 chiqadi va
  yana soddalashtirish kerak boʻladi; 36 ni olsangiz darrov <b>6√2</b> chiqadi.
</div>

<h3>Faqat oʻxshash ildizlar qoʻshiladi</h3>

<p>Ildiz ostidagi son bir xil boʻlsa, ular <em>x</em> va <em>y</em> kabi hadlar sifatida
qoʻshiladi (SAT-1):</p>

<div class="pe-ex">
  <p class="pe-ex__math">3√2 + 5√2 = 8√2</p>
  <p class="pe-ex__uz">Uchta «ildiz ikki» va beshta «ildiz ikki» — sakkizta.</p>
  <p class="pe-ex__why">√2 + √3 esa qoʻshilmaydi — ular oʻxshash hadlar emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">√9 + √16 = √25 = 5</p>
  <p class="pe-good">√9 + √16 = 3 + 4 = 7</p>
  <p class="pe-fix__why">Ildiz <b>qoʻshishga</b> taqsimlanmaydi. Qoida faqat
  koʻpaytirish uchun.</p>
</div>

<h3>Koʻpaytirish — koʻpincha butun son beradi</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">√3 · √12</span>
    <span class="pm-solve__why">Ikki ildizni bitta ildiz ostiga yigʻamiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">√36 = 6</span>
    <span class="pm-solve__why">3 × 12 = 36 — toʻliq kvadrat, ildiz butunlay yoʻqoldi</span>
  </div>
</div>

<h3>Misol (SAT darajasi) — avval soddalashtiring, keyin qoʻshing</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2√18 + √8</span>
    <span class="pm-solve__why">Ildiz ostidagi sonlar har xil — hozircha qoʻshib boʻlmaydi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2 · 3√2 + 2√2</span>
    <span class="pm-solve__why">√18 = 3√2 va √8 = 2√2</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">6√2 + 2√2 = 8√2</span>
    <span class="pm-solve__why">Endi ikkalasi ham «ildiz ikki» — qoʻshildi</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ildizlarni qoʻshish mumkinmi yoki yoʻqmi degan savolga javob berish uchun
  <b>avval ikkalasini ham soddalashtiring</b>. Koʻpincha «qoʻshib boʻlmaydigan»
  koʻringan ikki ildiz soddalashtirilgach bir xil boʻlib chiqadi.
</div>

<h3>Ildizning qiymatini chamalash</h3>

<p>Javobni tekshirish uchun ildizning taxminiy qiymatini bilish kifoya. Ikki sonni yod
oling: <strong>√2 ≈ 1.41</strong> va <strong>√3 ≈ 1.73</strong>. Ular bilan koʻp javobni
bir necha soniyada solishtirish mumkin.</p>

<div class="pe-ex">
  <p class="pe-ex__math">5√3 ≈ 5 × 1.73 = 8.65</p>
  <p class="pe-ex__uz">Va √75 ham taxminan 8.66 — demak javob toʻgʻri.</p>
  <p class="pe-ex__why">Boshqa yoʻl: 75 soni 64 (8<sup>2</sup>) bilan 81 (9<sup>2</sup>) orasida, demak √75 ham 8 bilan 9 orasida.</p>
</div>

<p>Bu chamalash usuli geometriyada ham asqotadi: tomoni 10√2 boʻlgan kvadratning tomoni
taxminan 14.1 metr ekanini bilish — chizmani tasavvur qilish uchun yetarli.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ildiz ostidagi son <b>toʻliq kvadrat</b> boʻlsa, ildiz butunlay yoʻqoladi: √49 = 7.
  Javoblar orasida ildizli va ildizsiz variantlar birga tursa, avval shuni tekshiring —
  ba'zan savol umuman ildizsiz javobga olib boradi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>in simplest radical form</b><span>eng sodda ildizli koʻrinishda</span></li>
  <li><b>which is equivalent to</b><span>qaysi ifoda teng kuchli</span></li>
  <li><b>where a is a positive integer</b><span>a — musbat butun son</span></li>
  <li><b>the square root of</b><span>…ning kvadrat ildizi</span></li>
  <li><b>rounded to the nearest tenth</b><span>oʻndan biriga yaxlitlangan (kalkulyator savoli)</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>Which expression is equivalent to √75?</p>
  </div>
  <ol class="ps-ch">
    <li>3√5</li>
    <li>5√3</li>
    <li>15</li>
    <li>25√3</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 5√3</p>
      <p>75 = 25 × 3, va √25 = 5. Demak √75 = 5√3.</p>
      <p>Tekshirish: 5√3 ≈ 5 × 1.73 = 8.66, va √75 ≈ 8.66 ✓ — kalkulyatorda 10
      soniyada tasdiqlanadi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">3√5</span>
  <span class="ps-trap__why">Koʻpaytuvchilar oʻrin almashgan: ildizdan chiqadigan son
  <b>toʻliq kvadratning ildizi</b> — √25 = 5, √3 emas.</span>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">25√3</span>
  <span class="ps-trap__why">Toʻliq kvadrat ildiz ostidan <b>ildizsiz</b> chiqarilgan.
  25 ning oʻzi emas, uning ildizi (5) chiqadi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>Which expression is equivalent to 2√18 + √8?</p>
  </div>
  <ol class="ps-ch">
    <li>6√2</li>
    <li>8√2</li>
    <li>10√2</li>
    <li>√80</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 8√2</p>
      <p>√18 = 3√2, demak 2√18 = 6√2. Va √8 = 2√2. Yigʻindi: 6√2 + 2√2 = 8√2.</p>
      <p><b>√80</b> — ildiz ostidagi sonlarni qoʻshgan javob (72 + 8). Ildiz
      qoʻshishga taqsimlanmaydi.</p>
    </div>
  </details>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Ildizli javoblarni <b>oʻnli kasrga aylantirib</b> solishtiring:</p>
  <ol>
    <li>Asl ifodani kalkulyatorda hisoblang: 2√18 + √8 ≈ 11.31.</li>
    <li>Javoblarni ham hisoblang: 8√2 ≈ 11.31 ✓, 6√2 ≈ 8.49 ✗.</li>
    <li>Mos kelgani — javob, soddalashtirish qadamlarisiz.</li>
  </ol>
  <p>Bu usul soddalashtirishdan koʻra sekinroq, lekin xatoga umuman joy qoldirmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">√2 + √3 = √5</p>
  <p class="pe-good">√2 + √3 — soddalashtirib boʻlmaydi.</p>
  <p class="pe-fix__why">Ildiz ostidagi sonlar har xil, demak ular oʻxshash hadlar
  emas. Tekshiring: 1.41 + 1.73 = 3.14, √5 esa 2.24.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ildizni <b>oʻxshash hadlar</b> deb oʻylang (SAT-1): √2 — bu bir turdagi «narsa»,
  √3 — boshqasi. 3√2 + 5√2 xuddi 3x + 5x kabi qoʻshiladi, √2 + √3 esa
  x + y kabi qoʻshilmaydi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Simplify: √48</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">4√3 — 48 = 16 × 3, va √16 = 4.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Simplify: √32</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">4√2 — 32 = 16 × 2. (8 × 4 ni olsangiz 2√8 chiqadi va yana
  soddalashtirish kerak boʻladi.)</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Simplify: 2√5 + 7√5</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">9√5 — ildiz ostidagi son bir xil, demak koeffitsientlar
  qoʻshiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Simplify: √2 · √8</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">4 — √16 = 4. Ikki irratsional son koʻpaytirilib butun son
  bergani bu mavzudagi eng chiroyli natija.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A square field has an area of 200 square metres. Write the length of one side in
  simplest radical form.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">10√2 metr — tomoni √200, va 200 = 100 × 2. Taxminan
  14.1 metr.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>radical</b><span>ildizli ifoda</span></li>
  <li><b>simplest radical form</b><span>eng sodda ildizli koʻrinish</span></li>
  <li><b>perfect square</b><span>toʻliq kvadrat (4, 9, 16, 25…)</span></li>
  <li><b>factor</b><span>koʻpaytuvchi</span></li>
  <li><b>like radicals</b><span>oʻxshash ildizlar (ostidagi son bir xil)</span></li>
  <li><b>irrational</b><span>irratsional (kasr bilan aniq yozilmaydi)</span></li>
  <li><b>under the radical</b><span>ildiz ostida</span></li>
  <li><b>approximately</b><span>taxminan</span></li>
  <li><b>side length</b><span>tomonning uzunligi</span></li>
  <li><b>area</b><span>yuza</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Eng katta toʻliq kvadratni</b> ajrating va uning ildizini tashqariga
        chiqaring.</li>
    <li>Faqat <b>oʻxshash ildizlar</b> qoʻshiladi — xuddi oʻxshash hadlar kabi.</li>
    <li>Ildiz <b>koʻpaytirishga</b> taqsimlanadi, <b>qoʻshishga</b> emas:
        √9 + √16 = 7, √25 emas.</li>
  </ul>
</div>
""",
    },
]
