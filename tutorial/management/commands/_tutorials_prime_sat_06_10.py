# -*- coding: utf-8 -*-
"""Prime SAT Math — lessons 6–10 (the line, from every angle).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_SAT.md
Lesson list: tutorial/management/commands/toc_prime_sat_math.txt

  mashqlar — practice/management/commands/_practice_ps_06_10.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_sat_readings_06_10.py

⚠️ Bu darslar ESKI SAT-6 … SAT-10 darslarining ustiga yoziladi (--republish).
⚠️ Til: sarlavha va test savollari inglizcha, tushuntirish hammasi oʻzbekcha.
   Son: 3.5 va 1,200 (SAT konvensiyasi).

⚠️ Kumulyativ chegaralar (SAT-1…5 erkin: ifoda, chiziqli tenglama, matndan tenglama,
   modul, qiyalik tushunchasi):
  • SAT-6  — ikki nuqtadan qiyalik formulasi, manfiy koordinata, 0 va undefined
    formulaning oʻzidan, nomaʼlum koordinatani topish.
  • SAT-7  — y = mx + b: m va b ni oʻqish, tenglama tuzish, y ga yechish.
    Standart shakl SAT-8 da — bu yerda faqat «y ga yeching» taktikasi sifatida.
  • SAT-8  — point-slope va standart shakl, kesishmalar, m = −A/B.
  • SAT-9  — tez chizish va tenglamani grafikka moslash.
  • SAT-10 — kontekstdagi maʼno: m «har bir birlik uchun», b «boshida».
  • ⛔ Parallel/perpendikulyar (SAT-11, 12) YOʻQ; tengsizlik (SAT-13…15) YOʻQ;
    sistema (SAT-16…18) YOʻQ; ps-desmos bloklari SAT-83 dan boshlanadi — bu yerda YOʻQ.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_sat_06_10.py \\
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
    # SAT-6 — slope from two points
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-6: Calculating Slope from Two Points",
        "category": "math",
        "order": 6,
        "summary": (
            "Ikki nuqta berilsa, qiyalikni formuladan chiqarish: y larning ayirmasi "
            "x larning ayirmasiga boʻlinadi. Manfiy koordinatalar, nol va aniqlanmagan "
            "qiyalik, hamda nomaʼlum koordinatani topish."
        ),
        "stories": ["The Ramp at the Side Door"],
        "content": """
<h2>SAT-6: Calculating Slope from Two Points</h2>

<p>SAT-5 da qiyalikni chizmadan sanadik: oʻngga necha qadam, yuqoriga necha qadam. Testda
esa chizma koʻpincha boʻlmaydi — faqat ikkita nuqta beriladi, xolos. Shuning uchun bu
darsda oʻsha sanashni <mark>formulaga</mark> aylantiramiz. Formula qisqa, lekin uni notoʻgʻri
tartibda yozgan oʻquvchi har safar bitta tayyor tuzoq javobga tushadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>ikki nuqtadan qiyalikni formula bilan topasiz;</li>
    <li>manfiy koordinatalar bilan ishlaganda ishorada adashmaysiz;</li>
    <li>nol va <em>undefined</em> qiyalikni formulaning oʻzidan koʻrasiz;</li>
    <li>qiyalik berilganda yoʻqolgan koordinatani (<em>k</em>) topasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Slope formula</span>
  <span class="pe-chip pe-chip--s">m</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">y<sub>2</sub> − y<sub>1</sub></span>
  <span class="pe-op">÷</span>
  <span class="pe-chip pe-chip--o">x<sub>2</sub> − x<sub>1</sub></span>
  <span class="pe-chip pe-chip--opt">reference sheetda YOʻQ</span>
</div>

<h3>Formula — bu oʻsha «rise ÷ run»ning oʻzi</h3>

<p>Ikkita nuqtani (<em>x</em><sub>1</sub>, <em>y</em><sub>1</sub>) va
(<em>x</em><sub>2</sub>, <em>y</em><sub>2</sub>) deb belgilaymiz. Pastdagi indekslar
«birinchi nuqta» va «ikkinchi nuqta» degani, boshqa hech narsa emas. <strong>Rise</strong>
— bu <em>y</em> larning ayirmasi, <strong>run</strong> — <em>x</em> larning ayirmasi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 210" role="img" aria-label="Ikki nuqta va ular orasidagi rise va run">
    <line class="pm-ln" x1="30" y1="180" x2="310" y2="180"/>
    <line class="pm-ln" x1="45" y1="20" x2="45" y2="195"/>
    <line class="pm-ln pm-ln--hl" x1="70" y1="165" x2="270" y2="35"/>
    <line class="pm-ln pm-ln--dash" x1="100" y1="146" x2="240" y2="146"/>
    <line class="pm-ln pm-ln--dash" x1="240" y1="146" x2="240" y2="54"/>
    <circle class="pm-pt" cx="100" cy="146" r="4"/>
    <circle class="pm-pt" cx="240" cy="54" r="4"/>
    <text class="pm-lbl" x="66" y="166">(x<tspan dy="3" font-size="9">1</tspan><tspan dy="-3">, y</tspan><tspan dy="3" font-size="9">1</tspan><tspan dy="-3">)</tspan></text>
    <text class="pm-lbl" x="212" y="45">(x<tspan dy="3" font-size="9">2</tspan><tspan dy="-3">, y</tspan><tspan dy="3" font-size="9">2</tspan><tspan dy="-3">)</tspan></text>
    <text class="pm-lbl pm-lbl--hl" x="140" y="164">run</text>
    <text class="pm-lbl pm-lbl--hl" x="248" y="105">rise</text>
  </svg>
  <figcaption>Ustidagi ayirma — rise, pastdagisi — run. Ikkalasi ham <b>bir xil nuqtadan</b> boshlanadi.</figcaption>
</figure>

<blockquote>Muhimi tartib emas, <u>izchillik</u>: qaysi nuqtani birinchi deb olsangiz,
uni <b>ham</b> yuqorida, <b>ham</b> pastda birinchi qoldiring.</blockquote>

<p>Nega? Chunki ikkala ayirmani ham teskari olsangiz, ikkala ishora ham almashadi va
natija oʻzgarmaydi: (3 − 11) ÷ (2 − 6) = (−8) ÷ (−4) = 2 — yuqoridagi bilan bir xil.
Faqat <b>bittasini</b> teskari olsangiz, javob manfiy chiqadi va u albatta javoblar
orasida turadi.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Eng ishonchli usul: nuqtalarni bir-birining <b>ostiga</b> yozing va ustunlab ayiring.
  Koʻz bilan «qaysi qayerda edi» deb izlash — aynan shu yerda xato tugʻiladi.
</div>

<h3>Misol 1 (oson)</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">(2, 3) va (6, 11)</span>
    <span class="pm-solve__why">Birinchi nuqtani chapga, ikkinchisini oʻngga yozdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">m = (11 − 3) ÷ (6 − 2)</span>
    <span class="pm-solve__why">Ustida y lar, pastda x lar — ikkalasi ham ikkinchi nuqtadan boshlandi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">m = 8 ÷ 4 = 2</span>
    <span class="pm-solve__why">SAT-5 dagi chizmadagi qiyalikning oʻzi</span>
  </div>
</div>

<h3>Misol 2 (oʻrta) — manfiy koordinatalar</h3>

<p>(−3, 4) va (5, −2). Bu yerda butun savol bitta narsaga bogʻliq: <em>ayirishda</em>
minusning ikki marta kelishi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">m = (−2 − 4) ÷ (5 − (−3))</span>
    <span class="pm-solve__why">Qiymatlarni oʻz oʻrniga qoʻydik, qavslar bilan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">m = (−6) ÷ (5 + 3)</span>
    <span class="pm-solve__why">Manfiy sonni ayirish — qoʻshish: 5 − (−3) = 8</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">m = −6 ÷ 8 = −3/4</span>
    <span class="pm-solve__why">Qisqartirdik; qiyalik manfiy, demak chiziq pasaymoqda</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Manfiy koordinatani formulaga <b>qavs bilan</b> qoʻying: 5 − (−3), 5 − −3 emas.
  Qavs yozilmaganda oʻquvchining qoʻli avtomatik ravishda 5 − 3 = 2 deb yozib yuboradi.
</div>

<h3>Nol va undefined — formuladan koʻrinadi</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">m = 0 — gorizontal</p>
    <p>(2, 5) va (9, 5): m = (5 − 5) ÷ (9 − 2) = 0 ÷ 7 = <b>0</b>.</p>
    <p>Ustida nol turibdi. Nolni songa boʻlish mumkin — javob 0.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">undefined — vertikal</p>
    <p>(4, 1) va (4, 7): m = (7 − 1) ÷ (4 − 4) = 6 ÷ 0 — <b>aniqlanmagan</b>.</p>
    <p>Pastda nol turibdi. Nolga boʻlish mumkin emas.</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qaysi biri qaysi ekanini yodlashning eng oson yoʻli: <b>nol qayerda turibdi</b> —
  ustidami yoki pastida. Ustida nol → javob 0. Pastida nol → <em>undefined</em>.
</div>

<h3>Misol 3 (SAT darajasi) — yoʻqolgan koordinata</h3>

<p>Ba'zan qiyalik <em>berilgan</em>, koordinatalardan biri esa harf bilan yozilgan.
Formulani teskari yoʻnalishda ishlatamiz.</p>

<p>The line through (2, 3) and (8, <em>k</em>) has a slope of 1/2. What is <em>k</em>?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">run = 8 − 2 = 6</span>
    <span class="pm-solve__why">Avval oson tomonini — x larning ayirmasini — hisobladik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">rise = 1/2 × 6 = 3</span>
    <span class="pm-solve__why">Qiyalik «har bir qadamga qancha» degani: 6 qadam × 1/2</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">k = 3 + 3 = 6</span>
    <span class="pm-solve__why">Boshlangʻich y ga koʻtarilishni qoʻshdik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>(6 − 3) ÷ (8 − 2) = 3 ÷ 6 = 1/2 ✓</p>
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>the line passes through</b><span>chiziq shu nuqtalardan oʻtadi</span></li>
  <li><b>in the xy-plane</b><span>koordinata tekisligida</span></li>
  <li><b>what is the value of k</b><span>k ning qiymati qancha — javob koordinata</span></li>
  <li><b>the slope is undefined</b><span>qiyalik aniqlanmagan — chiziq vertikal</span></li>
  <li><b>which of the following points</b><span>quyidagi nuqtalarning qaysi biri</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>In the <i>xy</i>-plane, a line passes through the points (−1, 6) and (3, −2).
    What is the slope of this line?</p>
  </div>
  <ol class="ps-ch">
    <li>−2</li>
    <li>−1/2</li>
    <li>1/2</li>
    <li>2</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) −2</p>
      <div class="pm-solve">
        <div class="pm-solve__row">
          <span class="pm-solve__step">rise = −2 − 6 = −8</span>
          <span class="pm-solve__why">y larning ayirmasi</span>
        </div>
        <div class="pm-solve__row">
          <span class="pm-solve__step">run = 3 − (−1) = 4</span>
          <span class="pm-solve__why">Manfiy sonni ayirdik — natija qoʻshildi</span>
        </div>
        <div class="pm-solve__row pm-solve__row--ans">
          <span class="pm-solve__step">m = −8 ÷ 4 = −2</span>
          <span class="pm-solve__why">Chiziq oʻngga qarab pasayadi</span>
        </div>
      </div>
      <p>Ikki nuqtaning y qiymati 6 dan −2 ga tushdi — javob manfiy boʻlishini
      hisoblashdan <b>oldin</b> bilsa boʻlardi. Bu 5 soniyalik tekshiruv.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">2</span>
  <span class="ps-trap__why">Ishora yoʻqolgan: −8 ÷ 4 ni 8 ÷ 4 deb olgan javob. Chiziq
  pasayayotgan boʻlsa, qiyalik <b>albatta</b> manfiy — bu qarashning oʻzi bir ochko.</span>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">−1/2</span>
  <span class="ps-trap__why">Nisbat teskari olingan: run ÷ rise = 4 ÷ (−8). Ustida
  har doim <b>y</b> lar turadi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>A line passes through the points (3, <i>k</i>) and (7, 15). The slope of the line
    is 3. What is the value of <i>k</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>3</li>
    <li>5</li>
    <li>12</li>
    <li>27</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 3</p>
      <div class="pm-solve">
        <div class="pm-solve__row">
          <span class="pm-solve__step">run = 7 − 3 = 4</span>
          <span class="pm-solve__why">x larning ayirmasi</span>
        </div>
        <div class="pm-solve__row">
          <span class="pm-solve__step">rise = 3 × 4 = 12</span>
          <span class="pm-solve__why">Har qadamga 3 birlik, qadamlar soni 4 ta</span>
        </div>
        <div class="pm-solve__row pm-solve__row--ans">
          <span class="pm-solve__step">k = 15 − 12 = 3</span>
          <span class="pm-solve__why">15 — <b>oʻngdagi</b> nuqta, demak koʻtarilishni ayiramiz</span>
        </div>
      </div>
      <p>Tekshirish: (15 − 3) ÷ (7 − 3) = 12 ÷ 4 = 3 ✓</p>
    </div>
  </details>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Qiyalik savolida hisoblashdan oldin <b>ikki soniyalik bashorat</b> qiling:</p>
  <ol>
    <li>y qiymati oshdimi yoki kamaydimi? Kamaygan boʻlsa — javob manfiy.</li>
    <li>Koʻtarilish qadamdan kattami? Katta boʻlsa — javob 1 dan katta.</li>
  </ol>
  <p>Shu ikki savol javoblarning yarmini darhol oʻchiradi va ishora xatosini imkonsiz
  qiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">(−3, 4) va (5, −2) uchun run = 5 − 3 = 2</p>
  <p class="pe-good">run = 5 − (−3) = 8</p>
  <p class="pe-fix__why">Birinchi nuqtaning x koordinatasi <b>−3</b>, 3 emas. Manfiy
  koordinatani qavs bilan qoʻying.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">m = (x<sub>2</sub> − x<sub>1</sub>) ÷ (y<sub>2</sub> − y<sub>1</sub>)</p>
  <p class="pe-good">m = (y<sub>2</sub> − y<sub>1</sub>) ÷ (x<sub>2</sub> − x<sub>1</sub>)</p>
  <p class="pe-fix__why">«y avval» — ustida y lar. Teskari yozilgani javoblar orasida
  har doim turadi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qiyalik formulasi <em>reference sheet</em>da <b>yoʻq</b>. U yerda yuza, hajm, aylana va
  maxsus uchburchaklar bor. Slope, kvadrat tenglama formulasi va oʻrta arifmetik —
  yod olinadi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  What is the slope of the line through (0, 0) and (4, 10)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">2.5 — rise = 10, run = 4, 10 ÷ 4 = 2.5 (yoki 5/2). SAT'da
  kasr ham, oʻnli kasr ham qabul qilinadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  What is the slope of the line through (−2, −5) and (2, 3)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">2 — rise = 3 − (−5) = 8, run = 2 − (−2) = 4, 8 ÷ 4 = 2.
  Ikkala ayirmada ham manfiy sondan ayirdik.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  What is the slope of the line through (5, 2) and (5, 9)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Undefined — run = 5 − 5 = 0, nolga boʻlish aniqlanmagan.
  Chiziq vertikal. Javob «0» emas!</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  What is the slope of the line through (1, 8) and (6, 3)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">−1 — rise = 3 − 8 = −5, run = 6 − 1 = 5, −5 ÷ 5 = −1.
  y kamaydi, demak ishora manfiy.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A line through (2, 7) and (10, <i>k</i>) has a slope of 1/4. What is <i>k</i>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">9 — run = 10 − 2 = 8, rise = 1/4 × 8 = 2, k = 7 + 2 = 9.
  Bu yerda k <b>oʻngdagi</b> nuqtada, shuning uchun qoʻshamiz.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>slope formula</b><span>qiyalik formulasi</span></li>
  <li><b>subscript</b><span>pastki indeks (x<sub>1</sub>, y<sub>2</sub>)</span></li>
  <li><b>passes through</b><span>…dan oʻtadi</span></li>
  <li><b>xy-plane</b><span>koordinata tekisligi</span></li>
  <li><b>coordinates</b><span>koordinatalar</span></li>
  <li><b>difference</b><span>ayirma</span></li>
  <li><b>undefined</b><span>aniqlanmagan (nolga boʻlish)</span></li>
  <li><b>horizontal / vertical</b><span>gorizontal / vertikal</span></li>
  <li><b>reference sheet</b><span>formula varagʻi (qiyalik formulasi unda YOʻQ)</span></li>
  <li><b>value of k</b><span>k ning qiymati</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Ustida y lar, pastda x lar</b>, va ikkala ayirma ham bir xil nuqtadan
        boshlanadi.</li>
    <li>Manfiy koordinatani <b>qavs bilan</b> qoʻying: 5 − (−3) = 8.</li>
    <li>Nol ustida boʻlsa qiyalik <b>0</b>, pastida boʻlsa <b>undefined</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-7 — slope-intercept form
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-7: Slope-Intercept Form (y = mx + b) in Depth",
        "category": "math",
        "order": 7,
        "summary": (
            "y = mx + b — SAT'dagi eng koʻp ishlaydigan bitta shakl. m va b ni bir "
            "qarashda oʻqish, nuqta va qiyalikdan tenglama tuzish, ikki nuqtadan "
            "tenglama chiqarish va tenglamani «y ga yechish» taktikasi."
        ),
        "stories": ["Forty Dollars and Three More"],
        "content": """
<h2>SAT-7: Slope-Intercept Form (y = mx + b) in Depth</h2>

<p>Agar SAT Math'dan bitta shaklni tanlash kerak boʻlsa, bu — <mark>y = mx + b</mark>.
U testda chiziqli tenglama, grafik, jadval va matnli masalada bir xil koʻrinishda
chiqadi va deyarli har doim ikkita savolga javob beradi: <em>qanchalik tez oʻzgaradi</em>
va <em>qayerdan boshlandi</em>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>tenglamadan <em>m</em> va <em>b</em> ni bir qarashda oʻqiysiz;</li>
    <li>nuqta va qiyalikdan tenglama tuzasiz;</li>
    <li>ikki nuqtadan tenglamaga oʻtasiz (avval m, keyin b);</li>
    <li>chalkash koʻrinishdagi tenglamani «y ga yechib», qiyalikni koʻrinadigan qilasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Slope-intercept form</span>
  <span class="pe-chip pe-chip--s">y</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">m</span>
  <span class="pe-chip pe-chip--s">x</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">b</span>
  <span class="pe-chip pe-chip--opt">m = slope · b = y-intercept</span>
</div>

<h3>b — chiziq y oʻqini qayerda kesadi</h3>

<p><strong>y-intercept</strong> — chiziqning <em>y</em> oʻqi bilan kesishgan nuqtasi.
U yerda <em>x</em> har doim <b>0</b> ga teng, shuning uchun tenglamada <em>mx</em>
yoʻqoladi va <em>y</em> = <em>b</em> boʻlib qoladi. Mana shuning uchun <em>b</em> ni
«boshlangʻich qiymat» deb oʻqiymiz.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 210" role="img" aria-label="y = 2x + 3 chizigʻi, y oʻqini 3 da kesadi">
    <line class="pm-ln" x1="20" y1="150" x2="310" y2="150"/>
    <line class="pm-ln" x1="60" y1="15" x2="60" y2="195"/>
    <line class="pm-ln pm-ln--hl" x1="30" y1="180" x2="250" y2="35"/>
    <circle class="pm-pt" cx="60" cy="160" r="4"/>
    <line class="pm-ln pm-ln--dash" x1="120" y1="120" x2="180" y2="120"/>
    <line class="pm-ln pm-ln--dash" x1="180" y1="120" x2="180" y2="80"/>
    <text class="pm-lbl pm-lbl--hl" x="66" y="176">b = 3</text>
    <text class="pm-lbl" x="132" y="138">1 ga</text>
    <text class="pm-lbl" x="186" y="104">2 ga</text>
    <text class="pm-lbl" x="296" y="168">x</text>
    <text class="pm-lbl" x="42" y="22">y</text>
  </svg>
  <figcaption>y = 2<i>x</i> + 3: chiziq y oʻqini 3 da kesadi va har bir qadamda 2 ga koʻtariladi.</figcaption>
</figure>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>y-intercept</b> va <b>x-intercept</b> — ikki xil narsa. Birinchisi <em>y</em> oʻqidagi
  nuqta (u yerda x = 0), ikkinchisi <em>x</em> oʻqidagi nuqta (u yerda y = 0). SAT ikkalasini
  bitta savolning javoblari qilib qoʻyadi, shuning uchun soʻzning boshiga qarang.
</div>

<h3>Tenglamadan oʻqish</h3>

<div class="pe-ex">
  <p class="pe-ex__math">y = 3x − 5</p>
  <p class="pe-ex__uz">Qiyalik 3, y-intercept −5. Ishora <b>b bilan birga</b> keladi.</p>
  <p class="pe-ex__why">«− 5» degani b = −5, b = 5 emas.</p>
</div>

<p>Ehtiyot boʻling: shakl <u>tayyor</u> boʻlmasa, oʻqib boʻlmaydi. 2<em>y</em> = 6<em>x</em> + 8
tenglamasida qiyalik 6 emas: avval ikkala tomonni 2 ga boʻlish kerak, shunda
<em>y</em> = 3<em>x</em> + 4 chiqadi va qiyalik <b>3</b> ekani koʻrinadi.</p>

<h3>Misol 1 (oson) — nuqta va qiyalikdan</h3>

<p>A line has a slope of 1/2 and passes through (4, 5). Write its equation.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">y = (1/2)x + b</span>
    <span class="pm-solve__why">m maʼlum, faqat b nomaʼlum</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5 = (1/2)(4) + b</span>
    <span class="pm-solve__why">Nuqtani qoʻydik: x = 4, y = 5</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5 = 2 + b  →  b = 3</span>
    <span class="pm-solve__why">Oddiy chiziqli tenglama (SAT-2)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">y = (1/2)x + 3</span>
    <span class="pm-solve__why">m va b joyiga qoʻyildi</span>
  </div>
</div>

<h3>Misol 2 (oʻrta) — ikki nuqtadan</h3>

<p>Through (2, 3) and (6, 11). Ikki qadam: avval qiyalik (SAT-6), keyin b.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">m = (11 − 3) ÷ (6 − 2) = 2</span>
    <span class="pm-solve__why">Qiyalik formulasi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 = 2(2) + b  →  b = −1</span>
    <span class="pm-solve__why">Ikki nuqtadan <b>istalgan birini</b> qoʻysa boʻladi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">y = 2x − 1</span>
    <span class="pm-solve__why">Tekshiruv: 2(6) − 1 = 11 ✓ ikkinchi nuqta ham toʻgʻri</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  b ni topgach, <b>ikkinchi</b> nuqtani ham qoʻyib koʻring. Bu 5 soniya oladi va ikkala
  qadamni bir yoʻla tekshiradi.
</div>

<h3>Misol 3 (SAT darajasi) — «y ga yeching»</h3>

<p>Testda tenglama koʻpincha boshqa koʻrinishda beriladi va savol qiyalikni soʻraydi.
Qiyalikni koʻrish uchun <em>y</em> ni yolgʻiz qoldiring.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + 3y = 12</span>
    <span class="pm-solve__why">Berilgan koʻrinish (bu «standart shakl», SAT-8)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3y = −2x + 12</span>
    <span class="pm-solve__why">2x ni oʻng tomonga oʻtkazdik — ishorasi almashdi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">y = −(2/3)x + 4</span>
    <span class="pm-solve__why">Hamma hadni 3 ga boʻldik: qiyalik −2/3, b = 4</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Boʻlishda <b>hamma had</b> boʻlinadi, faqat birinchisi emas. 3y = −2x + 12 dan
  y = −2x + 4 chiqmaydi — bu eng koʻp uchraydigan xato. Har bir hadga alohida qarang.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <em>y</em>-intercept ikki xil soʻraladi: «<em>what is the y-intercept</em>» — javob
  odatda <b>son</b> (4), «<em>what is the y-intercept of the graph</em>» yoki javoblar
  qavsli boʻlsa — <b>nuqta</b> (0, 4). Javob variantlarining koʻrinishiga qarang: ular
  qaysi shakl kutilayotganini oʻzi aytib turadi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>slope-intercept form</b><span>y = mx + b koʻrinishi</span></li>
  <li><b>the y-intercept of the line</b><span>chiziqning y oʻqini kesish nuqtasi (x = 0 da)</span></li>
  <li><b>which equation represents the line</b><span>qaysi tenglama shu chiziqni ifodalaydi</span></li>
  <li><b>in the form y = mx + b</b><span>javob shu koʻrinishda boʻlsin</span></li>
  <li><b>the graph of the line</b><span>chiziqning grafigi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">40 s</span></p>
  <div class="ps-stem__q">
    <p>A line in the <i>xy</i>-plane has a slope of −4 and passes through the point
    (0, 9). Which equation represents this line?</p>
  </div>
  <ol class="ps-ch">
    <li><i>y</i> = −4<i>x</i> − 9</li>
    <li><i>y</i> = −4<i>x</i> + 9</li>
    <li><i>y</i> = 4<i>x</i> + 9</li>
    <li><i>y</i> = 9<i>x</i> − 4</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) y = −4x + 9</p>
      <p>Nuqtaning x koordinatasi <b>0</b> — demak bu nuqtaning oʻzi y-intercept, hech
      narsa hisoblash kerak emas: b = 9. Qiyalik berilgan: m = −4.</p>
      <p>Shuning uchun y = −4<i>x</i> + 9.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">y = 9x − 4</span>
  <span class="ps-trap__why">m va b oʻrin almashgan. Savolda 9 keyin aytilgani uchun uni
  oxiriga qoʻyib yuborish oson: <b>x oldidagi son — qiyalik</b>, yolgʻiz turgani — b.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>A line has a slope of 2 and passes through the point (3, 10). What is the
    <i>y</i>-intercept of the line?</p>
  </div>
  <ol class="ps-ch">
    <li>4</li>
    <li>6</li>
    <li>10</li>
    <li>16</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 4</p>
      <div class="pm-solve">
        <div class="pm-solve__row">
          <span class="pm-solve__step">10 = 2(3) + b</span>
          <span class="pm-solve__why">Nuqtani y = mx + b ga qoʻydik</span>
        </div>
        <div class="pm-solve__row pm-solve__row--ans">
          <span class="pm-solve__step">10 = 6 + b  →  b = 4</span>
          <span class="pm-solve__why">Ikkala tomondan 6 ni ayirdik</span>
        </div>
      </div>
      <p>Boshqacha oʻylash: (3, 10) dan y oʻqigacha 3 qadam chapga yurish kerak, har
      qadamda 2 birlik pastga — 10 − 6 = 4.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">16</span>
  <span class="ps-trap__why">Ayirish oʻrniga qoʻshgan: 10 + 6. Chapga yurilganda musbat
  qiyalikda qiymat <b>kamayadi</b> — chizmani tasavvur qilish shu xatoni oʻldiradi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Javoblar tenglama boʻlsa, uzun hisobga kirishmang — <b>ikki filtr</b> yetadi.</p>
  <ol>
    <li><b>Ishora filtri:</b> qiyalik musbatmi yoki manfiy? Yarim javob oʻchadi.</li>
    <li><b>b filtri:</b> berilgan nuqtalardan biri (0, …) koʻrinishida boʻlsa, b darhol
        maʼlum; boʻlmasa, bitta nuqtani har bir javobga qoʻyib koʻring.</li>
  </ol>
  <p>Nuqtani qoʻyib tekshirish deyarli har doim tenglama tuzishdan tezroq.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">2y = 6x + 8 → qiyalik 6</p>
  <p class="pe-good">y = 3x + 4 → qiyalik 3</p>
  <p class="pe-fix__why">Shakl «tayyor» boʻlmaguncha m ni oʻqib boʻlmaydi: chap tomonda
  <b>yolgʻiz y</b> turishi shart.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">y = 3x − 5 → b = 5</p>
  <p class="pe-good">y = 3x − 5 → b = −5</p>
  <p class="pe-fix__why">Ishora had bilan birga yuradi. b = −5, shuning uchun chiziq
  y oʻqini <b>nol ostida</b> kesadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  What is the slope of the line <i>y</i> = −<i>x</i> + 8?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">−1 — x oldida son koʻrinmasa, u yerda 1 turadi; minus bilan
  birga −1. Qiyalik 8 emas: 8 — bu b.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Write the equation of the line with slope 5 that passes through (0, −2).</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>y</i> = 5<i>x</i> − 2 — nuqtaning x koordinatasi 0, demak
  u nuqtaning oʻzi y-intercept: b = −2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A line with slope 3 passes through (2, 9). What is <i>b</i>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">3 — 9 = 3(2) + b → 9 = 6 + b → b = 3. Tekshiruv:
  y = 3x + 3 da x = 2 boʻlsa y = 9 ✓</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  What is the slope of the line 4<i>x</i> + 2<i>y</i> = 10?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">−2 — y ga yechamiz: 2y = −4x + 10 → y = −2x + 5. Qiyalik
  −2, y-intercept 5.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A summer pass costs $40, and each visit to the pool costs $3 more. Write an equation
  for the total cost <i>y</i> after <i>x</i> visits, and find the cost of 12 visits.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>y</i> = 3<i>x</i> + 40, va 12 marta borilganda
  3(12) + 40 = $76. Bir martalik $40 — bu b, har safargi $3 — bu m.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>slope-intercept form</b><span>y = mx + b koʻrinishi</span></li>
  <li><b>y-intercept</b><span>y oʻqini kesish nuqtasi (x = 0 da)</span></li>
  <li><b>x-intercept</b><span>x oʻqini kesish nuqtasi (y = 0 da)</span></li>
  <li><b>coefficient of x</b><span>x oldidagi son — qiyalik</span></li>
  <li><b>solve for y</b><span>y ni yolgʻiz qoldirish</span></li>
  <li><b>represents</b><span>ifodalaydi</span></li>
  <li><b>initial value</b><span>boshlangʻich qiymat — b</span></li>
  <li><b>substitute</b><span>oʻrniga qoʻyish</span></li>
  <li><b>graph of the line</b><span>chiziqning grafigi</span></li>
  <li><b>equation of the line</b><span>chiziqning tenglamasi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>m</b> — x oldidagi son, <b>b</b> — yolgʻiz turgan son, va ikkalasi ham
        ishorasi bilan olinadi.</li>
    <li>Shakl tayyor boʻlmasa, avval <b>y ga yeching</b> — hamma hadni boʻling.</li>
    <li>Nuqta (0, …) koʻrinishida boʻlsa, <b>b darhol maʼlum</b>: hech narsa
        hisoblamang.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-8 — point-slope and standard form
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-8: Point-Slope Form and Standard Form",
        "category": "math",
        "order": 8,
        "summary": (
            "Chiziqning yana ikki koʻrinishi: nuqta-qiyalik shakli (b ni topmasdan "
            "tenglama yozish) va standart shakl Ax + By = C (kesishmalarni bir "
            "zumda beradi). Qaysi biri qachon tezroq."
        ),
        "stories": ["Sixty Minutes, Two Kinds of Minute"],
        "content": """
<h2>SAT-8: Point-Slope Form and Standard Form</h2>

<p>Bitta chiziqni uch xil yozish mumkin, va uchalasi ham <u>bir xil chiziq</u>ni bildiradi.
Ular oʻrtasidagi farq — <mark>qaysi maʼlumot koʻrinib turishi</mark>. SAT buni biladi va
savolni ataylab «notoʻgʻri» shaklda beradi, chunki shaklni almashtira olmagan oʻquvchi
vaqtini yoʻqotadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>nuqta va qiyalikdan darhol tenglama yozasiz — <em>b</em> ni topmasdan;</li>
    <li>standart shakldan ikkala kesishmani bir amalda topasiz;</li>
    <li>standart shaklning qiyaligini hisoblamasdan aytasiz;</li>
    <li>uch shakl orasida erkin oʻtasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Point-slope form</span>
  <span class="pe-chip pe-chip--s">y − y<sub>1</sub></span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">m</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">(x − x<sub>1</sub>)</span>
</div>

<h3>Nuqta-qiyalik shakli — nega u umuman bor</h3>

<p>SAT-7 da nuqta va qiyalikdan tenglama tuzish uchun avval <em>b</em> ni topdik.
<strong>Point-slope</strong> shakli shu qadamni tashlab ketadi: nuqta va qiyalik bor ekan,
tenglamani <u>toʻgʻridan-toʻgʻri</u> yozasiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">nuqta (2, 7), m = −3</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">y − 7 = −3(x − 2)</span>
    <span class="pm-solve__why">Formulaga qoʻydik — tugadi, javob shu</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">y = −3x + 13</span>
    <span class="pm-solve__why">Agar y = mx + b soʻralsa: qavs ochildi va 7 qoʻshildi</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Formulada <b>minus</b> turibdi, shuning uchun manfiy koordinata ikki minusni beradi:
  nuqta (5, −1) uchun <em>y − (−1)</em> = <em>y</em> <b>+</b> 1. Javoblar orasida
  <em>y</em> − 1 ham albatta boʻladi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Minus <b>qavs ichida ham</b> ishlaydi. Nuqta (−3, 8) boʻlsa,
  <em>x</em> − (−3) = <em>x</em> <b>+</b> 3 boʻladi. Yaʼni manfiy koordinata formulada
  har doim <b>qoʻshuvga</b> aylanadi — ikkala tomonda ham.
</div>

<h3>Standart shakl — Ax + By = C</h3>

<p>Bu shaklda <em>x</em> va <em>y</em> bir tomonda, son ikkinchi tomonda turadi. Uning
kuchli tomoni — <strong>kesishmalar</strong>. Kesishmani topish uchun qarama-qarshi
harfni nolga tenglashtiring:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">x-intercept</p>
    <p>y = 0 qoʻying. 4<i>x</i> + 3(0) = 24 → 4<i>x</i> = 24 → <b>x = 6</b>.</p>
    <p>Nuqta: (6, 0).</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">y-intercept</p>
    <p>x = 0 qoʻying. 4(0) + 3<i>y</i> = 24 → 3<i>y</i> = 24 → <b>y = 8</b>.</p>
    <p>Nuqta: (0, 8).</p>
  </div>
</div>

<figure class="pm-fig">
  <svg viewBox="0 0 320 210" role="img" aria-label="4x + 3y = 24 chizigʻi va uning ikki kesishmasi">
    <line class="pm-ln" x1="20" y1="160" x2="310" y2="160"/>
    <line class="pm-ln" x1="55" y1="15" x2="55" y2="195"/>
    <line class="pm-ln pm-ln--hl" x1="55" y1="40" x2="235" y2="160"/>
    <circle class="pm-pt" cx="55" cy="40" r="4"/>
    <circle class="pm-pt" cx="235" cy="160" r="4"/>
    <text class="pm-lbl pm-lbl--hl" x="62" y="36">(0, 8)</text>
    <text class="pm-lbl pm-lbl--hl" x="214" y="178">(6, 0)</text>
    <text class="pm-lbl" x="296" y="178">x</text>
    <text class="pm-lbl" x="38" y="22">y</text>
  </svg>
  <figcaption>Ikki kesishma topilsa, chiziq chizilgan boʻladi — uchinchi nuqta kerak emas.</figcaption>
</figure>

<h3>Standart shaklning qiyaligi — hisoblamasdan</h3>

<blockquote><em>Ax</em> + <em>By</em> = <em>C</em> koʻrinishidagi chiziqning qiyaligi
har doim <strong>−A ÷ B</strong> ga teng.</blockquote>

<p>Tekshiramiz: 4<em>x</em> + 3<em>y</em> = 24 ni y ga yechsak,
<em>y</em> = −(4/3)<em>x</em> + 8 — haqiqatan ham qiyalik −4/3, yaʼni −A ÷ B.
Bu qoidani bilgan oʻquvchi «qiyaligi qancha?» degan savolga 3 soniyada javob beradi.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>−A ÷ B</b> dagi minusni unutmang. 4<i>x</i> + 3<i>y</i> = 24 ning qiyaligi
  4/3 emas, <b>−4/3</b>. Ikkala koeffitsient ham musbat boʻlsa, chiziq albatta
  pasayadi — buni chizmadan ham koʻrish mumkin.
</div>

<h3>Shakldan shaklga oʻtish</h3>

<div class="pe-ex">
  <p class="pe-ex__math">y = 2x − 5  →  2x − y = 5</p>
  <p class="pe-ex__uz">Standart shaklga: x va y ni bir tomonga, sonni ikkinchi tomonga.</p>
  <p class="pe-ex__why">Ikkala tomondan y ni ayirdik va 5 ni qoʻshdik.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  SAT'da standart shakl koʻpincha <b>matnli masalada</b> chiqadi: «3 dollarlik va
  5 dollarlik chiptalardan jami 60 dollarga sotildi» — bu 3<i>x</i> + 5<i>y</i> = 60.
  Bunday holatda <i>x</i> va <i>y</i> narsalarning <b>soni</b>, demak javob butun son
  va manfiy boʻlolmaydi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>point-slope form</b><span>nuqta-qiyalik shakli: y − y₁ = m(x − x₁)</span></li>
  <li><b>standard form</b><span>standart shakl: Ax + By = C</span></li>
  <li><b>the x-intercept of the graph</b><span>grafikning x oʻqini kesish nuqtasi (y = 0)</span></li>
  <li><b>where A, B, and C are constants</b><span>A, B va C — sonlar</span></li>
  <li><b>an equivalent equation</b><span>teng kuchli tenglama — oʻsha chiziq, boshqa shakl</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>A line passes through the point (5, −1) and has a slope of 2. Which equation
    represents this line in point-slope form?</p>
  </div>
  <ol class="ps-ch">
    <li><i>y</i> + 1 = 2(<i>x</i> − 5)</li>
    <li><i>y</i> + 5 = 2(<i>x</i> − 1)</li>
    <li><i>y</i> − 1 = 2(<i>x</i> + 5)</li>
    <li><i>y</i> − 1 = 2(<i>x</i> − 5)</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) y + 1 = 2(x − 5)</p>
      <p>Formulaga qoʻyamiz: <i>y</i> − (−1) = 2(<i>x</i> − 5). Chap tomonda ikki minus
      qoʻshiluvga aylandi: <i>y</i> <b>+</b> 1.</p>
      <p>Tekshirish: x = 5 qoʻyilsa oʻng tomon 0 boʻladi, demak y + 1 = 0 va y = −1 —
      berilgan nuqtaning oʻzi ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">y − 1 = 2(x − 5)</span>
  <span class="ps-trap__why">Nuqtaning y koordinatasi <b>−1</b> ekani eʼtiborsiz
  qoldirilgan. Formulada minus turgani uchun manfiy koordinata ishorani almashtiradi.</span>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">y + 5 = 2(x − 1)</span>
  <span class="ps-trap__why">Koordinatalar oʻrin almashgan: 5 — bu <i>x</i>, −1 — bu
  <i>y</i>. Formulaga qoʻyishdan oldin nuqtani ovoz chiqarib oʻqing.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>3<i>x</i> + 5<i>y</i> = 45</p>
    <p>What is the <i>x</i>-intercept of the graph of the equation above in the
    <i>xy</i>-plane?</p>
  </div>
  <ol class="ps-ch">
    <li>5</li>
    <li>9</li>
    <li>15</li>
    <li>45</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 15</p>
      <div class="pm-solve">
        <div class="pm-solve__row">
          <span class="pm-solve__step">3x + 5(0) = 45</span>
          <span class="pm-solve__why">x-intercept — bu x oʻqidagi nuqta, u yerda y = 0</span>
        </div>
        <div class="pm-solve__row pm-solve__row--ans">
          <span class="pm-solve__step">3x = 45  →  x = 15</span>
          <span class="pm-solve__why">Kesishma nuqtasi: (15, 0)</span>
        </div>
      </div>
      <p><b>9</b> — bu <i>y</i>-intercept (45 ÷ 5). Ikkalasi ham javoblar orasida
      turibdi: savol qaysi kesishmani soʻraganini oʻqing.</p>
    </div>
  </details>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Chiziq savolida <b>shaklga qarab</b> qurol tanlang:</p>
  <ol>
    <li>Nuqta + qiyalik berilgan → <b>point-slope</b>, bir qatorda tugaydi.</li>
    <li>Ax + By = C berilgan va kesishma soʻralgan → qarama-qarshi harfga <b>0</b> qoʻying.</li>
    <li>Ax + By = C berilgan va qiyalik soʻralgan → <b>−A ÷ B</b>, hisob yoʻq.</li>
    <li>Grafik yoki y-intercept soʻralgan → <b>y ga yeching</b> (SAT-7).</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">3x + 5y = 45 ning qiyaligi 3/5</p>
  <p class="pe-good">qiyaligi −3/5</p>
  <p class="pe-fix__why">Qoida <b>−A ÷ B</b>. Minus tushib qolsa, javob teskari
  yoʻnalishdagi chiziqni bildiradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">x-intercept uchun x = 0 qoʻyish</p>
  <p class="pe-good">x-intercept uchun <b>y</b> = 0 qoʻyish</p>
  <p class="pe-fix__why">x-intercept — <b>x oʻqidagi</b> nuqta, va x oʻqida y nolga teng.
  Nomi bilan qoʻyiladigan nol qarama-qarshi harfda.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Write, in point-slope form, the equation of the line through (0, 4) with slope −2.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>y</i> − 4 = −2(<i>x</i> − 0), yaʼni <i>y</i> = −2<i>x</i> + 4.
  Nuqta y oʻqida turgani uchun ikkala shakl ham oson chiqadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  What is the slope of the line 2<i>x</i> − <i>y</i> = 8?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">2 — qoida boʻyicha −A ÷ B = −2 ÷ (−1) = 2. Tekshiruv:
  y = 2x − 8 ✓</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  What is the <i>x</i>-intercept of 6<i>x</i> + 2<i>y</i> = 18?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">3 — y = 0 qoʻyamiz: 6x = 18 → x = 3. Nuqta (3, 0).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  What is the <i>y</i>-intercept of the same line, 6<i>x</i> + 2<i>y</i> = 18?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">9 — x = 0 qoʻyamiz: 2y = 18 → y = 9. Nuqta (0, 9). Eʼtibor
  bering, bitta tenglama ikki xil javob beradi — savolga qarab.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A 60-minute radio show is filled with songs of 2 minutes each and interviews of
  5 minutes each. If the show has 4 interviews, how many songs does it have?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">20 ta — model 2<i>s</i> + 5<i>i</i> = 60 (standart shakl).
  i = 4 boʻlsa: 2s + 20 = 60 → 2s = 40 → s = 20.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>point-slope form</b><span>nuqta-qiyalik shakli</span></li>
  <li><b>standard form</b><span>standart shakl: Ax + By = C</span></li>
  <li><b>intercept</b><span>kesishma nuqtasi</span></li>
  <li><b>equivalent equation</b><span>teng kuchli tenglama</span></li>
  <li><b>rearrange</b><span>shaklni oʻzgartirish</span></li>
  <li><b>constants A, B, C</b><span>A, B, C — sonlar</span></li>
  <li><b>set y equal to zero</b><span>y ni nolga tenglashtiring</span></li>
  <li><b>expand the brackets</b><span>qavsni oching</span></li>
  <li><b>whole number</b><span>butun son (sanaladigan miqdorlarda)</span></li>
  <li><b>in the xy-plane</b><span>koordinata tekisligida</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Nuqta va qiyalik bor ekan, <b>point-slope</b> bir qatorda tenglama beradi —
        b ni izlash shart emas.</li>
    <li>Standart shaklda kesishma uchun <b>qarama-qarshi harfga 0</b> qoʻying.</li>
    <li>Standart shaklning qiyaligi — <b>−A ÷ B</b>, minus bilan.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-9 — graphing linear equations quickly
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-9: Graphing Linear Equations Quickly",
        "category": "math",
        "order": 9,
        "summary": (
            "Chiziqni 20 soniyada chizishning uch yoʻli va — testda undan ham "
            "muhimrogʻi — chizmasdan turib tenglamani grafikka moslash: ishora, "
            "kesishma va tiklik boʻyicha filtrlash."
        ),
        "stories": ["The Coach Who Drew Two Dots"],
        "content": """
<h2>SAT-9: Graphing Linear Equations Quickly</h2>

<p>SAT sizdan chiroyli grafik chizishni soʻramaydi. U <mark>tenglama bilan rasmni
bir-biriga moslashni</mark> soʻraydi: «qaysi grafik shu tenglamani ifodalaydi?»,
«qaysi tenglama shu chiziqni beradi?». Bunday savolni hisoblab emas, <u>filtrlab</u>
yechish kerak — va bu bir necha soniya oladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>chiziqni ikki nuqtada chizasiz va qaysi ikki nuqta qulayligini bilasiz;</li>
    <li>standart shakldan kesishmalar orqali darhol chizasiz;</li>
    <li>tenglamani grafikka <u>chizmasdan</u> moslaysiz;</li>
    <li>chiziq qaysi choraklardan oʻtishini bir qarashda aytasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Two points are enough</span>
  <span class="pe-chip pe-chip--o">nuqta 1</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">nuqta 2</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">bitta chiziq</span>
</div>

<h3>Uch yoʻl — va qachon qaysi biri</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span> b dan boshlash</p>
    <p><em>y</em> = <em>mx</em> + <em>b</em> uchun. <em>b</em> ni y oʻqiga qoʻying, keyin
    qiyalik boʻyicha bir qadam yuring: oʻngga 1, yuqoriga <em>m</em>.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span> Ikki kesishma</p>
    <p><em>Ax</em> + <em>By</em> = <em>C</em> uchun eng tez yoʻl (SAT-8): y = 0 qoʻying,
    keyin x = 0 qoʻying — ikki nuqta tayyor.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span> Kichik jadval</p>
    <p>Shakl notanish boʻlsa: ikkita qulay <em>x</em> tanlang (masalan 0 va 3) va
    <em>y</em> ni hisoblang.</p>
  </div>
</div>

<h3>Misol 1 (oson) — kesishmalar bilan</h3>

<p>Graph <em>y</em> = −2<em>x</em> + 6.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = 0  →  y = 6</span>
    <span class="pm-solve__why">y-intercept: (0, 6)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">y = 0  →  0 = −2x + 6  →  x = 3</span>
    <span class="pm-solve__why">x-intercept: (3, 0)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">(0, 6) va (3, 0) ni tutashtiring</span>
    <span class="pm-solve__why">Uchinchi nuqta kerak emas — ikki nuqta chiziqni belgilaydi</span>
  </div>
</div>

<h3>Misol 2 (oʻrta) — standart shakl</h3>

<p>Graph 5<em>x</em> + 2<em>y</em> = 20. Bu shaklni y ga yechish shart emas.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">y = 0  →  5x = 20  →  x = 4</span>
    <span class="pm-solve__why">(4, 0)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 0  →  2y = 20  →  y = 10</span>
    <span class="pm-solve__why">(0, 10) — ikki nuqta, chiziq tayyor</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Kesishmalar usuli faqat chiziq boshning oʻzidan oʻtmaganda ishlaydi. Agar
  <em>C</em> = 0 boʻlsa (masalan 3<i>x</i> + 4<i>y</i> = 0), ikkala kesishma ham
  <b>bitta</b> nuqtada — (0, 0) da — chiqadi va ikkinchi nuqtani boshqacha topish kerak.
</div>

<h3>Chizmasdan moslash — testdagi asosiy koʻnikma</h3>

<p>Javoblar toʻrtta grafik boʻlsa, hech narsa chizmang. Uch filtrni ketma-ket qoʻllang:</p>

<ol>
  <li><strong>Ishora.</strong> <em>m</em> musbatmi? Chiziq koʻtariladi. Manfiymi? Pasayadi.
      Odatda shuning oʻzi ikkitasini oʻchiradi.</li>
  <li><strong>b.</strong> Chiziq y oʻqini nolning tepasidami yoki pastidami kesadi?</li>
  <li><strong>Tiklik.</strong> Qiyalik 1 dan kattami (tik) yoki kichikmi (yotiq)?</li>
</ol>

<figure class="pm-fig">
  <svg viewBox="0 0 320 210" role="img" aria-label="y oʻqini 4 da kesib, pasayib boruvchi chiziq">
    <line class="pm-ln" x1="20" y1="150" x2="310" y2="150"/>
    <line class="pm-ln" x1="60" y1="15" x2="60" y2="195"/>
    <line class="pm-ln pm-ln--hl" x1="20" y1="18" x2="180" y2="194"/>
    <circle class="pm-pt" cx="60" cy="62" r="4"/>
    <circle class="pm-pt" cx="140" cy="150" r="4"/>
    <text class="pm-lbl pm-lbl--hl" x="68" y="56">(0, 4)</text>
    <text class="pm-lbl pm-lbl--hl" x="146" y="168">(2, 0)</text>
    <text class="pm-lbl" x="296" y="168">x</text>
    <text class="pm-lbl" x="42" y="22">y</text>
  </svg>
  <figcaption>Pasayuvchi chiziq, y oʻqini 4 da kesadi va 2 da x oʻqiga tushadi.</figcaption>
</figure>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «<b>Steeper</b>» (tikroq) va «<b>greater slope</b>» (kattaroq qiyalik) bir narsa emas.
  Tiklik — ishorasiz kattalik, shuning uchun −7 qiyalikli chiziq 5 qiyalikli chiziqdan
  <b>tikroq</b>; lekin qiyalik sifatida −7 <b>kichikroq</b>. Savol qaysi soʻzni
  ishlatganiga qarang.
</div>

<h3>Qaysi choraklardan oʻtadi</h3>

<p>Har bir chiziq (vertikal va gorizontaldan tashqari) <u>uchta</u> chorakdan oʻtadi —
demak bittasidan oʻtmaydi. Qaysi biridan oʻtmasligini qiyalik va <em>b</em> hal qiladi:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">m &gt; 0, b &lt; 0</p>
    <p>Koʻtariladi, y oʻqini nol ostida kesadi. II chorakka umuman kirmaydi.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">m &lt; 0, b &gt; 0</p>
    <p>Pasayadi, y oʻqini nol ustida kesadi. III chorakka kirmaydi.</p>
  </div>
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>which graph could represent</b><span>qaysi grafik shu tenglamani ifodalashi mumkin</span></li>
  <li><b>the graph shown</b><span>koʻrsatilgan grafik</span></li>
  <li><b>quadrant</b><span>chorak (I — oʻng yuqori, soat strelkasiga teskari sanaladi)</span></li>
  <li><b>which of the following is NOT</b><span>qaysi biri EMAS — javob «notoʻgʻri» variant</span></li>
  <li><b>note: figure not drawn to scale</b><span>chizma miqyosda emas — koʻz bilan oʻlchamang</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>A line in the <i>xy</i>-plane passes through the points (0, 4) and (2, 0).
    Which equation represents this line?</p>
  </div>
  <ol class="ps-ch">
    <li><i>y</i> = −2<i>x</i> − 4</li>
    <li><i>y</i> = −2<i>x</i> + 4</li>
    <li><i>y</i> = −(1/2)<i>x</i> + 4</li>
    <li><i>y</i> = 2<i>x</i> + 4</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) y = −2x + 4</p>
      <p><b>b filtri:</b> chiziq y oʻqini 4 da kesadi, demak b = 4 — birinchi javob
      oʻchdi.</p>
      <p><b>Ishora filtri:</b> chiziq pasaymoqda, demak m manfiy — toʻrtinchisi oʻchdi.</p>
      <p><b>Tiklik:</b> qiyalik = (0 − 4) ÷ (2 − 0) = −2. Qolgan ikkitadan −2 toʻgʻri
      keladi; −1/2 juda yotiq boʻlardi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">y = −(1/2)x + 4</span>
  <span class="ps-trap__why">Qiyalik teskari olingan: run ÷ rise. Chizmaga qarang —
  chiziq bitta qadamda ikki birlik tushmoqda, yarim birlik emas.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>The line <i>y</i> = 3<i>x</i> − 7 is graphed in the <i>xy</i>-plane. Through
    which quadrant does the line <b>NOT</b> pass?</p>
  </div>
  <ol class="ps-ch">
    <li>Quadrant I</li>
    <li>Quadrant II</li>
    <li>Quadrant III</li>
    <li>Quadrant IV</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) Quadrant II</p>
      <p>II chorak — <i>x</i> manfiy, <i>y</i> musbat boʻlgan joy. Lekin <i>x</i>
      manfiy boʻlsa, 3<i>x</i> ham manfiy va undan yana 7 ayriladi: <i>y</i> har doim
      −7 dan kichik boʻladi. Demak chiziq u yerga umuman chiqmaydi.</p>
      <p>Qolganlari: b = −7 (IV chorak), chap tomon pastda (III), x &gt; 7/3 dan keyin
      yuqorida (I).</p>
      <p>Tez usul: musbat qiyalik + manfiy b — <b>har doim</b> II chorakdan oʻtmaydi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">Quadrant III</span>
  <span class="ps-trap__why">«b manfiy, demak chap tomonga tushmaydi» degan notoʻgʻri
  mulohaza. Aksincha: <i>x</i> manfiy boʻlganda 3<i>x</i> − 7 yanada kichrayadi, demak
  chiziq III chorakdan <b>albatta</b> oʻtadi. Bitta son qoʻyib koʻring: x = −1 da
  y = −10.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Javoblar <b>grafik</b> boʻlsa, hisoblamang — oʻchiring:</p>
  <ol>
    <li>ishoraga qarang (koʻtariladimi yoki pasayadimi);</li>
    <li>y oʻqidagi nuqtaga qarang (nolning tepasidami yoki pastida);</li>
    <li>qolgan ikkitasini tiklik bilan ajrating.</li>
  </ol>
  <p>Agar hali ham ikkitasi qolsa, bitta qulay <em>x</em> ni (masalan 1 ni) tenglamaga
  qoʻying va nuqta qaysi grafikda yotishini koʻring.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">y = −2x + 6 uchun x-intercept = 6</p>
  <p class="pe-good">x-intercept = 3, y-intercept = 6</p>
  <p class="pe-fix__why">6 — bu <b>b</b>, yaʼni y oʻqidagi nuqta. x oʻqidagi nuqta uchun
  y = 0 qoʻyish kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Chizmadan qiyalikni «koʻzda chamalab» aytish</p>
  <p class="pe-good">Ikkita <b>aniq belgilangan</b> nuqtani olib, rise ÷ run hisoblash</p>
  <p class="pe-fix__why">SAT grafikning oʻqlarini turli masshtabda chizadi. Faqat
  belgilangan nuqtalarga ishoning.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Choraklar soat strelkasiga <b>teskari</b> sanaladi: I — oʻng yuqori, II — chap yuqori,
  III — chap past, IV — oʻng past. Bu tartibni bir marta yodlab qoʻysangiz,
  «quadrant» savollari bepul ochkoga aylanadi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Where does the line <i>y</i> = −4<i>x</i> + 9 cross the <i>y</i>-axis?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(0, 9) — y oʻqida x = 0, demak y = 9. Javob nuqta koʻrinishida
  yozilsa yanada aniq boʻladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Find both intercepts of 3<i>x</i> + 4<i>y</i> = 12.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(4, 0) va (0, 3) — y = 0 qoʻysak 3x = 12 → x = 4;
  x = 0 qoʻysak 4y = 12 → y = 3.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Which line is steeper: <i>y</i> = 3<i>x</i> + 1 or <i>y</i> = 0.5<i>x</i> + 6?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>y</i> = 3<i>x</i> + 1 — tiklikni <b>qiyalik</b> hal qiladi,
  b emas. 6 kattaroq boʻlsa ham, u chiziqni faqat yuqoriroqqa koʻchiradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Describe the graph of <i>y</i> = −<i>x</i> + 5 in two words about direction and
  one about its <i>y</i>-intercept.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Pasayadi (qiyalik −1), y oʻqini 5 da kesadi. Har bir qadam
  oʻngga — bir birlik pastga.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A cyclist rides 20 kilometres in week 0 and adds 6 kilometres every week. Which point
  lies on the graph of her weekly distance at week 5?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(5, 50) — model y = 6x + 20, va 6(5) + 20 = 50. Boshlangʻich
  20 — bu b, haftalik 6 — bu m.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>graph the line</b><span>chiziqni chizing</span></li>
  <li><b>plot a point</b><span>nuqtani belgilang</span></li>
  <li><b>quadrant</b><span>chorak</span></li>
  <li><b>steeper</b><span>tikroq</span></li>
  <li><b>crosses the y-axis</b><span>y oʻqini kesadi</span></li>
  <li><b>lies on the line</b><span>chiziqda yotadi</span></li>
  <li><b>could represent</b><span>ifodalashi mumkin</span></li>
  <li><b>not drawn to scale</b><span>miqyosda chizilmagan</span></li>
  <li><b>axis / axes</b><span>oʻq / oʻqlar</span></li>
  <li><b>origin</b><span>koordinata boshi (0, 0)</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Chiziq uchun <b>ikki nuqta</b> yetarli; standart shaklda eng qulaylari —
        ikki kesishma.</li>
    <li>Javoblar grafik boʻlsa: <b>ishora → b → tiklik</b> filtri, hisob yoʻq.</li>
    <li>Chizmaning oʻzidan qiyalikni chamalamang — faqat <b>belgilangan nuqtalarga</b>
        ishoning.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-10 — interpreting slope and intercept in context
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-10: Interpreting the Meaning of Slopes and Intercepts in Real-World Contexts",
        "category": "math",
        "order": 10,
        "summary": (
            "SAT'ning eng sevimli savol turi: «bu son kontekstda nimani bildiradi?» "
            "Qiyalik — «har bir birlik uchun», kesishma — «boshida». Hisoblash yoʻq, "
            "faqat toʻgʻri oʻqish."
        ),
        "stories": ["What Does the 62 Cents Mean?"],
        "content": """
<h2>SAT-10: Interpreting the Meaning of Slopes and Intercepts in Real-World Contexts</h2>

<p>Bu darsda bitta ham murakkab hisob yoʻq — va aynan shuning uchun u Blok A dagi eng
qimmatli darslardan biri. Har bir SAT'da <mark>ikki-toʻrtta</mark> savol shunday yangraydi:
<em>«Which of the following is the best interpretation of the number 12 in this
context?»</em> Matematikasi nol, ochkosi toʻliq. Yoʻqotadigan oʻquvchi ularni hisoblab
yoʻqotmaydi — <u>notoʻgʻri oʻqib</u> yoʻqotadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>modeldagi har bir sonning vazifasini bir qarashda aniqlaysiz;</li>
    <li>qiyalikni <em>birligi bilan</em> aytasiz («dollar, har bir soat uchun»);</li>
    <li>kesishmani «boshida / hech narsa boʻlmaganda» deb oʻqiysiz;</li>
    <li>eng koʻp uchraydigan tuzoqni — «bir birlik uchun jami» bilan «har bir qoʻshimcha
        birlik uchun» ni — ajratasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Reading a model</span>
  <span class="pe-chip pe-chip--v">m</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--opt">har bir birlik uchun oʻzgarish</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">b</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--opt">x = 0 boʻlgandagi qiymat</span>
</div>

<h3>Ikki savol, har doim bir xil</h3>

<p>Modelni koʻrganingizda oʻzingizga ikki savol bering:</p>

<ol>
  <li><strong>Bu son harf bilan turibdimi?</strong> Ha boʻlsa — u <b>qiyalik</b>. Uni
      «har bir … uchun shuncha» deb oʻqing.</li>
  <li><strong>Yolgʻiz turibdimi?</strong> Unda u <b>boshlangʻich qiymat</b>. Uni
      «hech narsa boʻlmaganda ham shuncha» deb oʻqing.</li>
</ol>

<div class="pe-ex">
  <p class="pe-ex__math">C = 0.62m + 45</p>
  <p class="pe-ex__uz">Mashina ijarasi: har bir mil uchun $0.62, ustiga bir martalik $45.</p>
  <p class="pe-ex__why">0.62 — m bilan turibdi, demak qiyalik; 45 — yolgʻiz, demak boshlangʻich.</p>
</div>

<h3>Birlikni ham ayting — bu tekshiruvning oʻzi</h3>

<p>Qiyalikning birligi har doim <mark>«y ning birligi / x ning birligi»</mark> koʻrinishida
boʻladi: dollar <u>har bir mil uchun</u>, litr <u>har bir daqiqada</u>, kitob
<u>har bir haftada</u>. Agar aytgan gapingizni birlik bilan takrorlab boʻlmasa, siz
notoʻgʻri sonni tanlagansiz.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada bu «bittasiga qancha» degan savol. Aynan shu tarzda oʻqing:
  «bir mil<b>ga</b> 62 sent», «bir daqiqa<b>da</b> 9 litr». Bu birgina soʻz
  (<em>-ga</em>, <em>-da</em>) qiyalikni boshlangʻich qiymatdan ajratib turadi.
</div>

<h3>Manfiy qiyalik — kamayish</h3>

<div class="pe-ex">
  <p class="pe-ex__math">L = 450 − 9m</p>
  <p class="pe-ex__uz">Bakda boshida 450 litr bor edi; har daqiqada 9 litr kamayadi.</p>
  <p class="pe-ex__why">Minus «kamayadi» degani, «manfiy suv» degani emas.</p>
</div>

<h3>Eng qimmat tuzoq: «bittaga jami» ≠ «har bir qoʻshimcha»</h3>

<p>Tikuvchi har metr uchun $12 oladi va ustiga bir martalik $25 xizmat haqi qoʻyadi:
jami = 12<em>m</em> + 25.</p>

<div class="pe-fix">
  <p class="pe-bad">12 — bir metr tikish narxi $12.</p>
  <p class="pe-good">12 — har bir <b>qoʻshimcha</b> metr narxni $12 ga oshiradi.</p>
  <p class="pe-fix__why">Bir metrning haqiqiy narxi 12 + 25 = <b>$37</b>. Qiyalik jamini
  emas, <b>oʻzgarishni</b> oʻlchaydi.</p>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>1 metr: 12(1) + 25 = 37. 2 metr: 12(2) + 25 = 49. Farqi 12 ✓ — demak 12 aynan
  <b>oʻzgarish</b>, jami emas.</p>
</div>

<h3>b maʼnosiz boʻlishi ham mumkin</h3>

<p>Model odam boʻyini yoshiga qarab bashorat qilsa, <em>b</em> — bu «tugʻilgandagi boʻyi»
boʻlib chiqadi va u haqiqatga toʻgʻri kelmasligi mumkin. SAT buni biladi va ba'zan
<em>«does not make sense in this context»</em> degan javobni toʻgʻri javob qilib qoʻyadi.
Shuning uchun <em>b</em> ni avtomatik ravishda «boshlangʻich» deb emas, <b>«x nolga teng
boʻlganda»</b> deb oʻqing va bu maʼnoli yoki maʼnosiz ekaniga qarang.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>the best interpretation of the number</b><span>bu son nimani bildiradi — hisob kerak emas</span></li>
  <li><b>for each additional …</b><span>har bir qoʻshimcha … uchun — bu qiyalik</span></li>
  <li><b>when no … have been sold</b><span>hech narsa sotilmaganda — bu b (x = 0)</span></li>
  <li><b>increases / decreases by</b><span>…ga ortadi / kamayadi — oʻzgarish miqdori</span></li>
  <li><b>in this context</b><span>shu vaziyatda — javob birligi bilan mos boʻlsin</span></li>
  <li><b>estimated / modeled by</b><span>taxminan shu tenglama bilan ifodalanadi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>The number of liters of water in a tank after <i>m</i> minutes of draining is
    given by <i>L</i> = 450 − 9<i>m</i>. Which of the following is the best
    interpretation of the number 450 in this context?</p>
  </div>
  <ol class="ps-ch">
    <li>The tank drains 450 liters each minute.</li>
    <li>The tank contained 450 liters before draining began.</li>
    <li>The tank is empty after 450 minutes.</li>
    <li>The tank holds 450 liters when it is full.</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) The tank contained 450 liters before draining began.</p>
      <p>450 yolgʻiz turibdi — demak u <i>m</i> = 0 boʻlgandagi qiymat, yaʼni
      quyish boshlanishidan oldingi hajm.</p>
      <p><b>D</b> juda yaqin, lekin matn bakning <em>sigʻimi</em> haqida hech narsa
      demaydi — u faqat boshlangʻich miqdorni beradi. SAT aynan shunday «deyarli
      toʻgʻri» javobni qoʻyadi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">450 liters each minute</span>
  <span class="ps-trap__why">Qiyalik bilan kesishma almashtirilgan. «Har bir daqiqada»
  degan javob faqat <b>m bilan turgan</b> songa — 9 ga — tegishli.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>A tailor's total charge, in dollars, for <i>m</i> metres of fabric is given by
    12<i>m</i> + 25. Which of the following is the best interpretation of the number 12?</p>
  </div>
  <ol class="ps-ch">
    <li>The total charge for one metre of fabric is $12.</li>
    <li>The charge increases by $12 for each additional metre.</li>
    <li>The tailor charges a fixed fee of $12.</li>
    <li>The tailor can sew at most 12 metres.</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) The charge increases by $12 for each additional metre.</p>
      <p>12 soni <i>m</i> bilan turibdi, demak u oʻzgarish tezligi.</p>
      <p><b>A</b> — eng koʻp tanlanadigan notoʻgʻri javob. Bir metrning <b>jami</b>
      narxi 12(1) + 25 = <b>$37</b>, chunki $25 baribir qoʻshiladi. Qiyalik jamini emas,
      <b>farqni</b> bildiradi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">$12 for one metre</span>
  <span class="ps-trap__why">«Bir birlik uchun jami» bilan «har bir qoʻshimcha birlik
  uchun oʻzgarish» aralashtirilgan. Ikkitasi faqat b = 0 boʻlgandagina teng boʻladi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Interpretatsiya savolida hech narsa hisoblamang. Uch qadam, 15 soniya:</p>
  <ol>
    <li>Soʻralgan son <b>harf bilanmi</b> yoki yolgʻizmi — aniqlang.</li>
    <li>Uni birligi bilan ovoz chiqarib oʻqing: «dollar, har bir metrga».</li>
    <li>Javoblarni oʻsha jumlaga solishtiring; «total», «fixed», «at most» kabi soʻzlar
        boshqa sonning javobi ekanini koʻrsatadi.</li>
  </ol>
  <p>Agar ikkita javob qolsa, <em>x</em> = 1 va <em>x</em> = 2 ni qoʻyib, farqni
  hisoblang — u har doim qiyalikka teng.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">P = 120 − 8t da 8 «har daqiqada −8» degani.</p>
  <p class="pe-good">8 — har bir daqiqada <b>8 birlik kamayadi</b> (minus modelda turibdi).</p>
  <p class="pe-fix__why">Ishorani tushuntirishga <b>soʻz bilan</b> qoʻshing: kamayadi.
  «Manfiy 8 ta» degan javob hech qanday maʼno bermaydi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Javob variantlarida «<b>at most</b>» (koʻpi bilan) yoki «<b>at least</b>» (kamida)
  soʻzi turgan boʻlsa, ehtiyot boʻling: bu tengsizlik tili (SAT-13…15), chiziqli model
  esa hech qanday chegara belgilamaydi. Bunday javob deyarli har doim notoʻgʻri.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Interpretatsiya savolida <b>toʻrtala javobni ham oxirigacha oʻqing</b>. Ular koʻpincha
  bitta soʻz bilan farq qiladi: <em>total</em> / <em>additional</em>, <em>each</em> /
  <em>at first</em>. Birinchi maʼqul koʻringan javobni belgilash — bu savol turida eng
  koʻp yoʻqotiladigan ochko.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  A worker's pay, in dollars, is <i>P</i> = 8<i>h</i> + 30. What does 8 represent?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Har bir soat uchun toʻlanadigan $8 — yaʼni har qoʻshimcha soat
  toʻlovni $8 ga oshiradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  In the same model, what does 30 represent?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Hech qanday soat ishlanmaganda ham toʻlanadigan $30 — doimiy
  (bir martalik) toʻlov.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A phone's battery level is <i>W</i> = 60 − 0.5<i>d</i>, where <i>d</i> is minutes of
  video. What does −0.5 mean?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Har bir daqiqa video zaryadni 0.5 foizga kamaytiradi.
  Minus — kamayish, «manfiy zaryad» emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Using <i>P</i> = 8<i>h</i> + 30, what is the pay for 5 hours — and is it 5 times the
  pay for one hour?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">$70 (8 × 5 + 30). Bir soatlik toʻlov $38, va 5 × 38 = $190 —
  teng emas, chunki $30 faqat <b>bir marta</b> qoʻshiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A model predicts a tree's height in metres as <i>H</i> = 0.4<i>y</i> + 1.2, where
  <i>y</i> is years since planting. What does 1.2 mean, and is it sensible?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ekilgan paytdagi (y = 0) balandligi 1.2 metr — koʻchat
  shunday boʻyda ekilgan. Bu maʼnoli. Lekin agar model 0.4<i>y</i> + 12 desa, 12 metrlik
  koʻchat maʼnosiz boʻlardi — SAT ba'zan aynan shuni soʻraydi.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>interpretation</b><span>maʼnosi, talqini</span></li>
  <li><b>in this context</b><span>shu vaziyatda</span></li>
  <li><b>for each additional</b><span>har bir qoʻshimcha … uchun</span></li>
  <li><b>fixed fee</b><span>doimiy (bir martalik) toʻlov</span></li>
  <li><b>rate of change</b><span>oʻzgarish tezligi</span></li>
  <li><b>initial amount</b><span>boshlangʻich miqdor</span></li>
  <li><b>is modeled by</b><span>… tenglamasi bilan ifodalanadi</span></li>
  <li><b>estimate</b><span>taxmin qilmoq</span></li>
  <li><b>per unit</b><span>bir birlikka</span></li>
  <li><b>does not make sense</b><span>maʼnoga ega emas</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Harf bilan turgan son — qiyalik</b> («har bir … uchun»), yolgʻiz turgani —
        boshlangʻich qiymat («x nolga teng boʻlganda»).</li>
    <li>Qiyalikni har doim <b>birligi bilan</b> ayting; birlik mos kelmasa, son
        notoʻgʻri tanlangan.</li>
    <li>«Bir birlik uchun <b>jami</b>» ≠ qiyalik. Farqni <em>x</em> = 1 va <em>x</em> = 2
        bilan tekshiring.</li>
  </ul>
</div>
""",
    },
]
