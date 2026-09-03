# -*- coding: utf-8 -*-
"""Prime SAT Math — lessons 1–5 (variable & like terms, linear equations,
word-problem setup, absolute value, slope).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_SAT.md
Lesson list: tutorial/management/commands/toc_prime_sat_math.txt

  mashqlar — practice/management/commands/_practice_ps_01_05.py (20 savoldan)

⚠️ Bu darslar ESKI SAT-1 … SAT-5 darslarining ustiga yoziladi (--republish).
   Sarlavhalar toc'dagidek, soʻzma-soʻz — oʻzgartirilsa dublikat paydo boʻladi.

⚠️ Til: sarlavha va test savollari inglizcha, tushuntirish hammasi oʻzbekcha.
   Son: 3.5 va 1,200 (SAT konvensiyasi), Prime Math'dagidek 3,5 EMAS.

⚠️ Kumulyativ chegaralar (bu birinchi batch — deyarli hech narsa "maʼlum" emas):
  • SAT-1 — faqat ifoda: had, koeffitsient, oʻxshash hadlar, qavs ochish.
    Tenglama YECHILMAYDI (SAT-2), grafik YOʻQ.
  • SAT-2 — bir nomaʼlumli chiziqli tenglama, ikki tomonda x, kasrli tenglama,
    yechimsiz / cheksiz koʻp yechim. Sistema YOʻQ (SAT-16…18), kvadrat YOʻQ.
  • SAT-3 — matndan tenglama tuzish, faqat BITTA nomaʼlum bilan.
  • SAT-4 — modul: |x| = a, ichini izolyatsiya qilish, yechimsiz hol.
    Modulli TENGSIZLIK YOʻQ (SAT-22).
  • SAT-5 — qiyalik tushunchasi: rise/run, ishora, jadval va grafikdan, maʼnosi.
    Ikki nuqta formulasi SAT-6, y = mx + b esa SAT-7 — bu darsda faqat tushuncha.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_sat_01_05.py \\
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
    # SAT-1 — variable & combining like terms
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-1: Introduction to the Variable and Combining Like Terms",
        "category": "math",
        "order": 1,
        "summary": (
            "Harf nima uchun kerakligi, had va koeffitsient, oʻxshash hadlarni "
            "qoʻshish va qavs ochish — SAT'dagi har uchinchi algebra savoli aynan "
            "shu bir necha soniyalik ishdan boshlanadi."
        ),
        "content": """
<h2>SAT-1: Introduction to the Variable and Combining Like Terms</h2>

<p>SAT'da <em>Algebra</em> boʻlimi savollarning taxminan 35 foizini tashkil qiladi va
ularning koʻpi bitta bir xil harakat bilan boshlanadi: ifodani <strong>soddalashtirish</strong>.
Uzun koʻringan ifoda ikki qatordan keyin qisqarib qoladi va savol birdan oson boʻlib qoladi.
Shu ikki qatorni tez va xatosiz yozishni oʻrgansangiz, testning eng arzon ochkolari qoʻlingizda.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>harf (<em>variable</em>) nimani anglatishini va nega undan qoʻrqmaslik kerakligini bilasiz;</li>
    <li>ifodani hadlarga (<em>terms</em>) ajratasiz va koeffitsientni (<em>coefficient</em>) ajrata olasiz;</li>
    <li>oʻxshash hadlarni (<em>like terms</em>) qoʻshib, ifodani bir qatorga tushirasiz;</li>
    <li>qavsni toʻgʻri ochasiz — ayniqsa oldida minus turganda.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">A term</span>
  <span class="pe-chip pe-chip--o">3</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">x</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">coefficient × variable</span>
</div>

<h3>Harf — bu jumboq emas, bu shunchaki son</h3>

<p><strong>Variable</strong> (oʻzgaruvchi) — qiymati hozircha nomaʼlum yoki oʻzgarib turadigan
son uchun qoʻyilgan harf. <mark>x</mark> — bu sirli belgi emas; agar <em>x</em> = 4 boʻlsa,
3<em>x</em> shunchaki 12 degani. Harf sonning oʻrnida turadi, demak son bilan qilinadigan
hamma amal harf bilan ham qilinadi.</p>

<p>Ifodani <strong>had</strong>larga (<em>terms</em>) ajratamiz. Hadlar bir-biridan
<strong>+</strong> va <strong>−</strong> belgilari bilan ajraladi. Masalan
5<em>x</em> + 3<em>y</em> − 7 ifodasida uchta had bor: 5<em>x</em>, 3<em>y</em> va −7.</p>

<ul>
  <li><strong>Coefficient</strong> (koeffitsient) — harf oldidagi son. 5<em>x</em> da u 5 ga teng.</li>
  <li>Agar harf oldida son koʻrinmasa, u yerda <strong>1</strong> turibdi: <em>x</em> = 1<em>x</em>.</li>
  <li><strong>Constant</strong> (oʻzgarmas) — harfsiz had, masalan −7. U hech qachon oʻzgarmaydi.</li>
  <li>Hadning ishorasi <em>oldidagi</em> belgi bilan birga yuradi: 5<em>x</em> <strong>−</strong> 7
      da ikkinchi had −7, 7 emas.</li>
</ul>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <em>Term</em> — «had», <em>coefficient</em> — «koeffitsient», <em>constant</em> — «oʻzgarmas son».
  SAT savoli koʻpincha <em>«where a and b are constants»</em> deb yozadi: bu «a va b — sonlar,
  faqat qiymati aytilmagan» degani, qoʻrqadigan joyi yoʻq.
</div>

<h3>Oʻxshash hadlar — nimani nima bilan qoʻshish mumkin</h3>

<blockquote>Ikki had <strong>oʻxshash</strong> (<em>like terms</em>) deyiladi, agar ularning
harf qismi <u>butunlay bir xil</u> boʻlsa — bir xil harf va bir xil daraja.</blockquote>

<p>3<em>x</em> va 5<em>x</em> — oʻxshash. 3<em>x</em> va 5<em>y</em> — yoʻq.
3<em>x</em> va 5<em>x</em><sup>2</sup> ham — yoʻq, chunki darajalari boshqa. Nega? Chunki
<em>x</em> ta olma va <em>x</em><sup>2</sup> ta olma turli miqdorlar; ularni bitta songa
qoʻshib boʻlmaydi.</p>

<p>Qoʻshganda faqat <strong>koeffitsientlar</strong> qoʻshiladi, harf qismi qanday boʻlsa
shundayligicha qoladi:</p>

<div class="pe-ex">
  <p class="pe-ex__math">3x + 5x = 8x</p>
  <p class="pe-ex__uz">Uchta «x» ustiga beshta «x» — sakkizta «x». Daraja oʻzgarmaydi.</p>
  <p class="pe-ex__why">Bu 3 × x + 5 × x = (3 + 5) × x degani — qavsdan chiqarish qoidasi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">3x + 5x = 8x<sup>2</sup></p>
  <p class="pe-good">3x + 5x = 8x</p>
  <p class="pe-fix__why">Qoʻshganda daraja koʻtarilmaydi. Daraja faqat <b>koʻpaytirganda</b>
  oʻzgaradi: 3x · 5x = 15x<sup>2</sup>.</p>
</div>

<h3>Qavs ochish — va oldidagi minus</h3>

<p>Qavs oldidagi son ichidagi <u>har bir</u> hadga koʻpaytiriladi
(<em>the distributive property</em>):</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">4(2x + 5)</span>
    <span class="pm-solve__why">Berilgan ifoda</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4 · 2x + 4 · 5</span>
    <span class="pm-solve__why">4 ni ikkala hadga ham koʻpaytirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">8x + 20</span>
    <span class="pm-solve__why">Koʻpaytmalarni hisobladik</span>
  </div>
</div>

<p>Eng koʻp xato qavs oldida <strong>minus</strong> turganda qilinadi. Minus ham ichidagi
hamma hadga tegadi — birinchisiga emas, hammasiga:</p>

<div class="pe-fix">
  <p class="pe-bad">4 − (2x − 3) = 4 − 2x − 3 = 1 − 2x</p>
  <p class="pe-good">4 − (2x − 3) = 4 − 2x + 3 = 7 − 2x</p>
  <p class="pe-fix__why">Qavs oldidagi minus = «−1 ga koʻpaytirish». −1 × (−3) = <b>+3</b>,
  demak −3 emas, +3 boʻlib chiqadi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qavs oldida minus tursa, oʻzingizga ovoz chiqarib ayting: «<b>ichkaridagi hamma ishora
  almashadi</b>». SAT bu xatoni biladi va uni har doim javoblar orasiga qoʻyadi.
</div>

<h3>Uchta ishlangan misol</h3>

<p><strong>Misol 1 (oson).</strong> Simplify: 5<em>x</em> + 3 − 2<em>x</em> + 7</p>
<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">5x − 2x + 3 + 7</span>
    <span class="pm-solve__why">Oʻxshash hadlarni yonma-yon yigʻdik (ishoralari bilan)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3x + 10</span>
    <span class="pm-solve__why">5 − 2 = 3 va 3 + 7 = 10</span>
  </div>
</div>

<p><strong>Misol 2 (oʻrta).</strong> Simplify: 4(2<em>x</em> − 3) + 5<em>x</em></p>
<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">8x − 12 + 5x</span>
    <span class="pm-solve__why">Avval qavsni ochdik: 4 · 2x = 8x, 4 · (−3) = −12</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">13x − 12</span>
    <span class="pm-solve__why">8x + 5x = 13x; −12 yolgʻiz qoladi, unga qoʻshadigan son yoʻq</span>
  </div>
</div>

<p><strong>Misol 3 (SAT darajasi).</strong> Simplify: 3(<em>x</em> + 2) − 2(4 − <em>x</em>)</p>
<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x + 6 − 2(4 − x)</span>
    <span class="pm-solve__why">Birinchi qavs ochildi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x + 6 − 8 + 2x</span>
    <span class="pm-solve__why">−2 · 4 = −8 va −2 · (−x) = <b>+2x</b> — ikkinchi ishoraga eʼtibor</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">5x − 2</span>
    <span class="pm-solve__why">3x + 2x = 5x va 6 − 8 = −2</span>
  </div>
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>simplify</b><span>soddalashtiring — oʻxshash hadlarni qoʻshib, bir qatorga tushiring</span></li>
  <li><b>equivalent to</b><span>teng kuchli — har qanday x uchun bir xil qiymat beradigan ifoda</span></li>
  <li><b>in terms of x</b><span>javob x orqali ifodalansin: son emas, <em>ifoda</em> kutilyapti</span></li>
  <li><b>where a and b are constants</b><span>a va b — shunchaki sonlar, qiymati aytilmagan</span></li>
  <li><b>the sum of</b><span>yigʻindisi — qoʻshish; <em>the difference of</em> esa ayirma</span></li>
</ul>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Expression</b> (ifoda) va <b>equation</b> (tenglama) — boshqa narsa. Ifodada tenglik
  belgisi yoʻq, shuning uchun uni «yechib» boʻlmaydi — faqat soddalashtiriladi. Savol
  <em>«which expression is equivalent…»</em> desa, javob ham <b>ifoda</b> boʻladi, son emas.
</div>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>Which expression is equivalent to 7<i>x</i> + 3 − 2(<i>x</i> − 4)?</p>
  </div>
  <ol class="ps-ch">
    <li>5<i>x</i> − 5</li>
    <li>5<i>x</i> + 7</li>
    <li>5<i>x</i> + 11</li>
    <li>9<i>x</i> + 11</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 5x + 11</p>
      <div class="pm-solve">
        <div class="pm-solve__row">
          <span class="pm-solve__step">7x + 3 − 2x + 8</span>
          <span class="pm-solve__why">−2 · x = −2x va −2 · (−4) = <b>+8</b></span>
        </div>
        <div class="pm-solve__row pm-solve__row--ans">
          <span class="pm-solve__step">5x + 11</span>
          <span class="pm-solve__why">7x − 2x = 5x va 3 + 8 = 11</span>
        </div>
      </div>
      <p>Butun savol bitta ishoraga bogʻliq: qavs oldidagi −2 ichkaridagi −4 bilan
      koʻpaytirilganda <b>musbat</b> 8 beradi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">5x − 5</span>
  <span class="ps-trap__why">Minusni ichkariga olib kirib, 3 − 8 = −5 deb hisoblagan javob.
  Yaʼni −2 × (−4) ni −8 deb olgan. Bu SAT'dagi eng koʻp uchraydigan bitta xato.</span>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">9x + 11</span>
  <span class="ps-trap__why">Ayirish oʻrniga qoʻshgan: 7x + 2x = 9x. Qavs oldidagi belgi
  koʻpaytuvchining ham belgisi ekanini unutganda shunday boʻladi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>The expression 5(2<i>x</i> + 3) − 3(<i>x</i> − 1) is equivalent to
    <i>ax</i> + <i>b</i>, where <i>a</i> and <i>b</i> are constants.
    What is the value of <i>a</i> + <i>b</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>7</li>
    <li>18</li>
    <li>22</li>
    <li>25</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: D) 25</p>
      <div class="pm-solve">
        <div class="pm-solve__row">
          <span class="pm-solve__step">10x + 15 − 3x + 3</span>
          <span class="pm-solve__why">Ikkala qavs ochildi; −3 · (−1) = <b>+3</b></span>
        </div>
        <div class="pm-solve__row">
          <span class="pm-solve__step">7x + 18</span>
          <span class="pm-solve__why">10x − 3x = 7x va 15 + 3 = 18</span>
        </div>
        <div class="pm-solve__row pm-solve__row--ans">
          <span class="pm-solve__step">a + b = 7 + 18 = 25</span>
          <span class="pm-solve__why">a — x oldidagi son, b — oʻzgarmas had</span>
        </div>
      </div>
      <p>Savol <b>a</b> ni ham, <b>b</b> ni ham emas, <b>ularning yigʻindisini</b> soʻradi.
      Ish tugagach, savolni yana bir marta oʻqing — bu SAT'da yoʻqotiladigan ochkolarning
      eng katta manbai.</p>
    </div>
  </details>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Javoblar <b>ifoda</b> boʻlsa (son emas), qavs ochish bilan ovora boʻlmasangiz ham
  boʻladi: <em>x</em> ning oʻrniga qulay son qoʻying va tekshiring.</p>
  <ol>
    <li>Berilgan ifodaga <em>x</em> = 2 ni qoʻying va bitta son chiqaring.</li>
    <li>Har bir javobga ham <em>x</em> = 2 ni qoʻying.</li>
    <li>Bir xil son bergani — javob. (0 va 1 ni tanlamang: ular koʻp xatoni yashiradi.)</li>
  </ol>
  <p>Bu usul <em>plugging in numbers</em> deb ataladi va SAT-81 darsida toʻliq oʻrgatiladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Simplify: 8<i>x</i> − 3 + 2<i>x</i> + 11</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">10<i>x</i> + 8 — 8x + 2x = 10x, keyin −3 + 11 = 8.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Simplify: 6 − (3<i>x</i> − 5)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">11 − 3<i>x</i> — qavs oldidagi minus ikkala hadning ishorasini
  almashtiradi: −3x va +5, keyin 6 + 5 = 11.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Which expression is equivalent to 2(3<i>x</i> + 4) − 5<i>x</i>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> + 8 — 6x + 8 − 5x = x + 8. Koeffitsienti 1 boʻlgan had
  «1x» deb emas, shunchaki «x» deb yoziladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  If 4<i>x</i> + 9 − <i>x</i> + 1 is written as <i>ax</i> + <i>b</i>, what is
  <i>a</i> · <i>b</i>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">30 — ifoda 3<i>x</i> + 10 ga teng, demak a = 3, b = 10 va
  3 × 10 = 30. Savol yigʻindini emas, <b>koʻpaytmani</b> soʻradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A rectangle has a length of (2<i>x</i> + 5) and a width of (<i>x</i> − 1). Which expression
  represents its perimeter?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">6<i>x</i> + 8 — perimetr = 2(uzunlik + eni) =
  2((2x + 5) + (x − 1)) = 2(3x + 4) = 6x + 8. Yuza (<em>area</em>) soʻralmagan: ularni
  adashtirmang.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>variable</b><span>oʻzgaruvchi; son oʻrnida turgan harf</span></li>
  <li><b>term</b><span>had; + yoki − bilan ajralgan boʻlak</span></li>
  <li><b>coefficient</b><span>koeffitsient; harf oldidagi son</span></li>
  <li><b>constant</b><span>oʻzgarmas son; harfsiz had</span></li>
  <li><b>like terms</b><span>oʻxshash hadlar; harf qismi bir xil</span></li>
  <li><b>expression</b><span>ifoda; tenglik belgisi yoʻq</span></li>
  <li><b>equivalent</b><span>teng kuchli; har doim bir xil qiymat beradi</span></li>
  <li><b>simplify</b><span>soddalashtirish</span></li>
  <li><b>distribute</b><span>qavsni ochish; har bir hadga koʻpaytirish</span></li>
  <li><b>perimeter</b><span>perimetr; <em>area</em> esa yuza</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Faqat <b>oʻxshash hadlar</b> qoʻshiladi, va faqat koeffitsientlar qoʻshiladi:
        3x + 5x = 8x, x<sup>2</sup> ga aylanmaydi.</li>
    <li>Qavs oldidagi <b>minus ichkaridagi hamma ishorani almashtiradi</b>. Testdagi
        tuzoq javoblarning yarmi shu yerdan.</li>
    <li>Ish tugagach <b>savolni qayta oʻqing</b>: u <em>a</em> ni emas, <em>a + b</em> ni
        soʻragan boʻlishi mumkin.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-2 — solving single-variable linear equations
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-2: Solving Single-Variable Linear Equations",
        "category": "math",
        "order": 2,
        "summary": (
            "Tarozi qoidasi, teskari amallar, ikki tomonida ham x boʻlgan tenglama, "
            "kasrdan qutulish va SAT juda yaxshi koʻradigan ikki maxsus hol: "
            "yechim yoʻq va cheksiz koʻp yechim."
        ),
        "content": """
<h2>SAT-2: Solving Single-Variable Linear Equations</h2>

<p>SAT'ning Math boʻlimida <em>chiziqli tenglama</em> eng koʻp uchraydigan bitta mavzu.
Uni yechish bir necha soniyalik ish, lekin test buni bilgani uchun savolni chalgʻituvchi
qilib yozadi: qavs qoʻshadi, x ni ikkala tomonga tarqatadi yoki oxirida <em>x</em> ning
oʻzini emas, <em>x</em> + 4 ni soʻraydi. Qadamlar oʻzgarmaydi — faqat intizom kerak.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>tenglamani tarozi kabi koʻrasiz: bir tomonga qilingan amal ikkinchisiga ham qilinadi;</li>
    <li>x ni bir tomonga, sonlarni ikkinchi tomonga toʻgʻri tartibda oʻtkazasiz;</li>
    <li>kasrli tenglamani kesishtirib (<em>cross-multiplying</em>) bir zumda toza koʻrinishga keltirasiz;</li>
    <li><em>no solution</em> va <em>infinitely many solutions</em> savollarini bir qarashda tanib olasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Linear equation</span>
  <span class="pe-chip pe-chip--v">a</span>
  <span class="pe-chip pe-chip--s">x</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">b</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">c</span>
  <span class="pe-chip pe-chip--opt">a ≠ 0</span>
</div>

<h3>Tarozi qoidasi</h3>

<p>Tenglik belgisi — tarozining oʻqi. Chap tomon oʻng tomonga <u>teng</u> turibdi. Agar bir
tomondan biror narsa olsangiz, muvozanat buziladi — shuning uchun <mark>xuddi shu amalni
ikkinchi tomonga ham qilasiz</mark>. Butun algebra shu bitta gapdan iborat.</p>

<p>Harfni yolgʻiz qoldirish uchun <strong>teskari amal</strong> (<em>inverse operation</em>)
ishlatiladi va u <u>teskari tartibda</u> qoʻllanadi: avval qoʻshish/ayirishdan qutulamiz,
keyin koʻpaytirish/boʻlishdan.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x + 7 = 22</span>
    <span class="pm-solve__why">Berilgan tenglama</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x = 15</span>
    <span class="pm-solve__why">Ikkala tomondan 7 ni ayirdik (qoʻshishning teskarisi)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 5</span>
    <span class="pm-solve__why">Ikkala tomonni 3 ga boʻldik (koʻpaytirishning teskarisi)</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Javobni topgach, uni asl tenglamaga qoʻyib koʻring: 3 × 5 + 7 = 22 ✓. Bu 5 soniya oladi
  va SAT'da bir necha ochkoni saqlab qoladi. Tekshirish — hisoblashning bir qismi.
</div>

<h3>x ikkala tomonda boʻlsa</h3>

<p>Barcha <em>x</em> li hadlarni bir tomonga, barcha sonlarni ikkinchi tomonga yigʻamiz.
Qaysi tomonga? <mark>Koeffitsienti kattaroq boʻlgan tomonga</mark> — shunda manfiy son
bilan ishlamaysiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">5x − 4 = 2x + 11</span>
    <span class="pm-solve__why">Berilgan tenglama</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x − 4 = 11</span>
    <span class="pm-solve__why">Ikkala tomondan 2x ni ayirdik (5 > 2, shuning uchun chapga yigʻdik)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x = 15</span>
    <span class="pm-solve__why">Ikkala tomonga 4 ni qoʻshdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 5</span>
    <span class="pm-solve__why">Ikkala tomonni 3 ga boʻldik</span>
  </div>
</div>

<h3>Qavs va kasr — avval ularni yoʻqoting</h3>

<p><strong>Misol (SAT darajasi).</strong> Solve for <em>x</em>:
<span class="pm-frac"><span class="pm-frac__n">x + 3</span><span class="pm-frac__d">4</span></span>
=
<span class="pm-frac"><span class="pm-frac__n">2x − 1</span><span class="pm-frac__d">3</span></span></p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3(x + 3) = 4(2x − 1)</span>
    <span class="pm-solve__why">Kesishtirib koʻpaytirdik: har bir surat qarama-qarshi maxrajga</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x + 9 = 8x − 4</span>
    <span class="pm-solve__why">Ikkala qavs ochildi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">13 = 5x</span>
    <span class="pm-solve__why">3x ni va −4 ni oʻtkazdik: 9 + 4 = 13, 8x − 3x = 5x</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 13/5 = 2.6</span>
    <span class="pm-solve__why">Ikkala tomonni 5 ga boʻldik</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Javob 2.6 — <b>nuqta bilan</b>, 2,6 emas. SAT javob katagiga vergul yozib boʻlmaydi;
  vergul yozgan oʻquvchining toʻgʻri javobi ham nol ball oladi. Shu kursda ham har doim
  nuqta ishlatamiz — odat test kunida emas, hozir shakllanadi (SAT-90 ga qarang).
</div>

<h3>Ikki maxsus hol — SAT ularni juda yaxshi koʻradi</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">No solution</p>
    <p>2(x + 3) = 2x + 5 → 2x + 6 = 2x + 5 → <b>6 = 5</b>, yolgʻon.</p>
    <p>Ikki tomonda x lar bir xil, sonlar boshqa. Grafik tilida: <u>parallel</u> chiziqlar,
    hech qachon kesishmaydi.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Infinitely many solutions</p>
    <p>2(x + 3) = 2x + 6 → 2x + 6 = 2x + 6 → <b>6 = 6</b>, har doim rost.</p>
    <p>Ikki tomon butunlay bir xil. Grafik tilida: bitta chiziqning oʻzi.</p>
  </div>
</div>

<blockquote>Qoida: <em>x</em> qisqarib ketdi, natijada <u>yolgʻon</u> tenglik qoldi →
<strong>no solution</strong>. <u>Rost</u> tenglik qoldi → <strong>infinitely many
solutions</strong>.</blockquote>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>«Yechimi yoʻq»</b> va <b>«yechimi nol»</b> — butunlay boshqa javoblar.
  <em>x</em> = 0 — bu haqiqiy yechim (tenglamani rost qiladi). <em>No solution</em> esa
  hech qanday son toʻgʻri kelmasligi. SAT ikkalasini bitta savolning javoblari qilib
  qoʻyadi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>solve for x</b><span>x ni toping — javob son boʻladi</span></li>
  <li><b>what is the value of 2x</b><span>x emas, 2x soʻralyapti — topib boʻlib, yana ikkiga koʻpaytiring</span></li>
  <li><b>no solution</b><span>yechimi yoʻq — x qisqaradi, yolgʻon tenglik qoladi</span></li>
  <li><b>infinitely many solutions</b><span>cheksiz koʻp yechim — ikki tomon aynan bir xil</span></li>
  <li><b>where c is a constant</b><span>c — nomaʼlum son; koʻpincha aynan shu c soʻraladi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>If 5(<i>x</i> − 3) = 2<i>x</i> + 9, what is the value of <i>x</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>−2</li>
    <li>4</li>
    <li>8</li>
    <li>24</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 8</p>
      <div class="pm-solve">
        <div class="pm-solve__row">
          <span class="pm-solve__step">5x − 15 = 2x + 9</span>
          <span class="pm-solve__why">Qavs ochildi: 5 · x va 5 · (−3)</span>
        </div>
        <div class="pm-solve__row">
          <span class="pm-solve__step">3x = 24</span>
          <span class="pm-solve__why">2x ni ayirdik, 15 ni qoʻshdik: 9 + 15 = 24</span>
        </div>
        <div class="pm-solve__row pm-solve__row--ans">
          <span class="pm-solve__step">x = 8</span>
          <span class="pm-solve__why">Ikkala tomonni 3 ga boʻldik</span>
        </div>
      </div>
      <p>Tekshirish: 5(8 − 3) = 25 va 2 · 8 + 9 = 25 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">24</span>
  <span class="ps-trap__why">Bitta qadam yetmay toʻxtagan javob: 3x = 24 topilgan, lekin
  3 ga boʻlinmagan. SAT deyarli har doim «yarim yoʻldagi» sonni javoblar orasiga qoʻyadi.</span>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">4</span>
  <span class="ps-trap__why">Qavsni faqat birinchi hadga ochgan: 5x − 3 = 2x + 9 →
  3x = 12 → x = 4. Qavs oldidagi son <b>ichidagi hamma hadga</b> koʻpaytiriladi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">90 s</span></p>
  <div class="ps-stem__q">
    <p>3(2<i>x</i> + <i>c</i>) = 6<i>x</i> + 15</p>
    <p>In the equation above, <i>c</i> is a constant. If the equation has infinitely many
    solutions, what is the value of <i>c</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>3</li>
    <li>5</li>
    <li>12</li>
    <li>15</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 5</p>
      <p>«Cheksiz koʻp yechim» degani — ikki tomon <b>aynan bir xil ifoda</b> boʻlishi kerak.</p>
      <div class="pm-solve">
        <div class="pm-solve__row">
          <span class="pm-solve__step">6x + 3c = 6x + 15</span>
          <span class="pm-solve__why">Chap tomonda qavs ochildi</span>
        </div>
        <div class="pm-solve__row">
          <span class="pm-solve__step">3c = 15</span>
          <span class="pm-solve__why">6x ikkala tomonda bir xil — qisqaradi</span>
        </div>
        <div class="pm-solve__row pm-solve__row--ans">
          <span class="pm-solve__step">c = 5</span>
          <span class="pm-solve__why">Ikkala tomonni 3 ga boʻldik</span>
        </div>
      </div>
      <p>Agar 3<i>c</i> ≠ 15 boʻlganda, tenglama <b>no solution</b> boʻlardi — masalan
      <i>c</i> = 4 boʻlsa, 12 = 15 degan yolgʻon qolardi.</p>
    </div>
  </details>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p><b>Backsolving</b> — javoblar son boʻlsa, tenglamani yechmasdan javoblarni sinab
  koʻrish mumkin.</p>
  <ol>
    <li>Oʻrtadagi javobdan boshlang (B yoki C) — sonlar oʻsish tartibida yozilgan.</li>
    <li>Uni tenglamaga qoʻying. Toʻgʻri chiqsa — tugadi.</li>
    <li>Kichik chiqsa yuqoriga, katta chiqsa pastga yuring: koʻpi bilan ikki urinish.</li>
  </ol>
  <p>Tenglama qavsli va chalkash boʻlsa, bu koʻpincha yechishdan tezroq. Toʻliq usul —
  SAT-82.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">3x = 24 → x = 21</p>
  <p class="pe-good">3x = 24 → x = 8</p>
  <p class="pe-fix__why">3<i>x</i> — bu «3 <b>koʻpaytiruv</b> x», shuning uchun teskari amal
  <b>boʻlish</b>, ayirish emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">−x = 7 → x = 7</p>
  <p class="pe-good">−x = 7 → x = −7</p>
  <p class="pe-fix__why">Chapdagi harf <b>−1x</b>. Ikkala tomonni −1 ga boʻlish kerak;
  ishorani unutish — SAT'dagi eng qimmat bir belgilik xato.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <em>«What is the value of x + 4?»</em> degan savol <b>x + 4</b> ni soʻrayapti. x = 5 ni
  topib, javoblar orasidan 5 ni belgilash — SAT'da eng koʻp uchraydigan yoʻqotish. Savolning
  oxirgi jumlasini doim ikki marta oʻqing.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Solve for <i>x</i>: 4<i>x</i> − 9 = 19</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> = 7 — ikkala tomonga 9 qoʻshdik (4x = 28), keyin 4 ga
  boʻldik.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Solve for <i>x</i>: 7<i>x</i> + 2 = 3<i>x</i> + 18</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> = 4 — 3x ni ayirdik (4x + 2 = 18), 2 ni ayirdik
  (4x = 16), 4 ga boʻldik.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  If 2(<i>x</i> − 4) = 3<i>x</i> − 11, what is the value of <i>x</i>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> = 3 — 2x − 8 = 3x − 11 → 3 = x. Manfiy sondan qoʻrqmang:
  2x ni ayirsak −8 = x − 11, keyin 11 ni qoʻshsak 3 = x.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  If 6<i>x</i> − 5 = 13, what is the value of <i>x</i> + 2?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">5 — avval 6x = 18, demak x = 3; savol esa <b>x + 2</b> ni
  soʻradi: 3 + 2 = 5. Javoblar orasida 3 ham albatta boʻladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A membership costs $30 plus $12 for each class. If a member paid $102 in total, how many
  classes did they take?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">6 ta — 30 + 12<i>c</i> = 102 → 12<i>c</i> = 72 → <i>c</i> = 6.
  Tekshiring: 30 + 12 × 6 = 102 ✓</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>equation</b><span>tenglama; ifodadan farqi — tenglik belgisi bor</span></li>
  <li><b>solve for x</b><span>x ni topish</span></li>
  <li><b>solution</b><span>yechim; tenglamani rost qiladigan qiymat</span></li>
  <li><b>inverse operation</b><span>teskari amal (+ ↔ −, × ↔ ÷)</span></li>
  <li><b>both sides</b><span>ikkala tomon</span></li>
  <li><b>no solution</b><span>yechimi yoʻq</span></li>
  <li><b>infinitely many solutions</b><span>cheksiz koʻp yechim</span></li>
  <li><b>cross-multiply</b><span>kesishtirib koʻpaytirish (kasrli tenglamada)</span></li>
  <li><b>substitute</b><span>oʻrniga qoʻyish; tekshirishda ishlatiladi</span></li>
  <li><b>constant</b><span>oʻzgarmas son (c, k kabi harflar bilan beriladi)</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Bir tomonga qilingan amal <b>ikkinchi tomonga ham</b> qilinadi. Boshqa qoida yoʻq.</li>
    <li>x qisqarib ketsa: yolgʻon tenglik → <b>no solution</b>, rost tenglik →
        <b>infinitely many solutions</b>.</li>
    <li>Javobni topib boʻlib, <b>savolni qayta oʻqing</b> — u x ni emas, x + 2 ni soʻragan
        boʻlishi mumkin.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-3 — setting up linear equations from word problems
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-3: Setting Up Linear Equations from Word Problems",
        "category": "math",
        "order": 3,
        "summary": (
            "Inglizcha jumlani tenglamaga aylantirish: harfni nimaga qoʻyish, "
            "«5 less than x» tuzogʻi, boshlangʻich toʻlov va har birlik uchun narx "
            "modeli — SAT matnli masalalarining asosi."
        ),
        "content": """
<h2>SAT-3: Setting Up Linear Equations from Word Problems</h2>

<p>SAT'da matematikani biladigan, lekin ball ololmaydigan oʻquvchi koʻp. Sababi deyarli
har doim bitta: <mark>jumlani tenglamaga aylantira olmaslik</mark>. Tenglama tuzilgandan
keyin qolgani — SAT-2 dagi bir necha qadam. Shuning uchun bu dars butunlay bitta koʻnikmaga
bagʻishlangan: inglizcha jumlani oʻqib, uni matematika tiliga koʻchirish.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>harfni <em>nimaga</em> qoʻyish kerakligini aniqlaysiz va uni yozib qoʻyasiz;</li>
    <li>inglizcha iboralarni amallarga aylantirasiz (<em>more than, less than, per, twice</em>);</li>
    <li>«boshlangʻich toʻlov + har birlik uchun narx» modelini tanib olasiz;</li>
    <li><em>«5 less than x»</em> tartib tuzogʻiga tushmaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The most common SAT model</span>
  <span class="pe-chip pe-chip--o">start-up fee</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">rate</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">number of units</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">total</span>
</div>

<h3>Uch qadamli tartib</h3>

<ol>
  <li><strong>Define.</strong> Harfni nimaga qoʻyayotganingizni <u>yozib qoʻying</u>:
      «<em>m</em> = number of months». Bu bir soniya oladi va yarim xatoni oldini oladi.</li>
  <li><strong>Translate.</strong> Jumlani boʻlaklarga boʻlib, har bir boʻlakni belgiga
      aylantiring. Ingliz tilida gap tartibi matematikadagi tartib bilan har doim ham
      mos kelmaydi — pastdagi jadvalga qarang.</li>
  <li><strong>Answer the question.</strong> Tenglamani yeching va <u>soʻralgan narsani</u>
      bering: koʻpincha bu <em>x</em> ning oʻzi emas.</li>
</ol>

<h3>Ibora → belgi jadvali</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Testda shunday deyiladi</th><th>Matematikada</th><th>Misol</th></tr>
  <tr><td>the sum of x and 5</td><td class="pm-word__sym">+</td><td>x + 5</td></tr>
  <tr><td>5 more than x</td><td class="pm-word__sym">+ 5</td><td>x + 5</td></tr>
  <tr><td><b>5 less than x</b></td><td class="pm-word__sym">− 5</td><td><b>x − 5</b> (5 − x emas!)</td></tr>
  <tr><td>twice a number</td><td class="pm-word__sym">× 2</td><td>2x</td></tr>
  <tr><td>the product of 3 and x</td><td class="pm-word__sym">×</td><td>3x</td></tr>
  <tr><td>$4 per item</td><td class="pm-word__sym">× 4</td><td>4n</td></tr>
  <tr><td>is / will be / results in</td><td class="pm-word__sym">=</td><td>3x = 12</td></tr>
  <tr><td>half of x</td><td class="pm-word__sym">÷ 2</td><td>x/2</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <em>«5 less than x»</em> — «x dan 5 ta kam», yaʼni <b>x − 5</b>. Ingliz tilida son oldin
  aytiladi, lekin ayirishda u <b>keyin</b> turadi. <em>«5 minus x»</em> esa haqiqatan
  5 − x. Bu ikkisini adashtirish — SAT'dagi eng qadimiy tuzoq.
</div>

<h3>Misol 1 (oson) — start-up fee + rate</h3>

<p><em>A gym charges a one-time fee of $25 plus $15 per month. What is the total cost after
8 months?</em></p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">m = number of months</span>
    <span class="pm-solve__why">Avval harfni aniqladik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">C = 15m + 25</span>
    <span class="pm-solve__why">Har oy uchun 15 — koʻpayadi; 25 — bir marta toʻlanadi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">C = 15 · 8 + 25 = 145</span>
    <span class="pm-solve__why">m = 8 ni qoʻydik: jami $145</span>
  </div>
</div>

<p>Bu modelni yodda tuting: <strong>bir marta toʻlanadigan son harfsiz turadi, har safar
takrorlanadigan son harf bilan koʻpayadi.</strong> SAT buni telefon tarifi, taksi, sport
zali, ijara, dostavka koʻrinishida yuzlab marta soʻraydi.</p>

<h3>Misol 2 (oʻrta) — ikki miqdor, bitta harf</h3>

<p><em>Ann has 4 more books than twice as many as Bo. Together they have 34 books. How many
books does Bo have?</em></p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">b = Bo's books</span>
    <span class="pm-solve__why">Harfni <b>kichik</b> miqdorga qoʻyish qulayroq</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Ann = 2b + 4</span>
    <span class="pm-solve__why">«twice as many as Bo» = 2b, «4 more» = +4</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">b + (2b + 4) = 34</span>
    <span class="pm-solve__why">«Together» — ikkalasining yigʻindisi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3b = 30</span>
    <span class="pm-solve__why">Oʻxshash hadlar qoʻshildi, 4 ayirildi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">b = 10</span>
    <span class="pm-solve__why">Bo — 10 ta, Ann — 24 ta kitob</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>10 + 24 = 34 ✓ va 24 = 2 × 10 + 4 ✓ — ikkala shart ham bajarildi.</p>
</div>

<h3>Misol 3 (SAT darajasi) — javob butun son emas</h3>

<p><em>A taxi charges a flat fee of $3.50 plus $0.75 per mile. A ride cost $14.75. How many
miles was the ride?</em></p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3.50 + 0.75m = 14.75</span>
    <span class="pm-solve__why">m = number of miles</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">0.75m = 11.25</span>
    <span class="pm-solve__why">Ikkala tomondan 3.50 ni ayirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">m = 15</span>
    <span class="pm-solve__why">11.25 ÷ 0.75 = 15</span>
  </div>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>0.75 ≈ 0.75, 11.25 ≈ 11 → 11 ÷ 0.75 ≈ 15. Javob 15 atrofida boʻlishi kerak edi —
  agar 150 yoki 1.5 chiqqanida, oʻnli kasrda xato bor demakdir.</span>
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>which equation represents…</b><span>qaysi tenglama shu vaziyatni ifodalaydi — yechish shart emas</span></li>
  <li><b>a one-time fee / flat fee</b><span>bir martalik toʻlov — harfsiz turadigan son</span></li>
  <li><b>per month / per mile</b><span>har oy / har mil uchun — harf bilan koʻpayadigan son</span></li>
  <li><b>twice as many as</b><span>ikki barobar koʻp — × 2</span></li>
  <li><b>how many … did she have at first</b><span>boshida nechta edi — javob boshlangʻich qiymat</span></li>
  <li><b>at this rate</b><span>shu tezlikda davom etsa — chiziqli model saqlanadi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>A phone plan costs $20 per month plus $0.10 for each text message sent. Which
    equation gives the total cost <i>C</i>, in dollars, for one month in which
    <i>t</i> text messages are sent?</p>
  </div>
  <ol class="ps-ch">
    <li><i>C</i> = 0.10 + 20<i>t</i></li>
    <li><i>C</i> = 20 + 0.10<i>t</i></li>
    <li><i>C</i> = 20<i>t</i> + 0.10<i>t</i></li>
    <li><i>C</i> = 20(0.10<i>t</i>)</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) C = 20 + 0.10t</p>
      <p>$20 — oyiga bir marta toʻlanadi, demak u <b>yolgʻiz</b> turadi. $0.10 esa
      <b>har bir</b> xabar uchun, demak xabarlar soni <i>t</i> ga koʻpayadi.</p>
      <p>Tekshirishning eng tez yoʻli: 10 ta xabar yozilsa, hisob $21 boʻlishi kerak.
      B) 20 + 0.10 × 10 = 21 ✓, A) 0.10 + 200 = 200.10 ✗.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">C = 0.10 + 20t</span>
  <span class="ps-trap__why">Ikki son oʻrin almashgan. Jumlada $20 birinchi aytilgani uchun
  uni harf yoniga qoʻyib yuborish oson. Qaysi son <b>takrorlanadi</b> — oʻsha harf bilan
  koʻpayadi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>The sum of a number and 12 is equal to 5 times that number. What is the number?</p>
  </div>
  <ol class="ps-ch">
    <li>2</li>
    <li>3</li>
    <li>4</li>
    <li>6</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 3</p>
      <div class="pm-solve">
        <div class="pm-solve__row">
          <span class="pm-solve__step">n + 12 = 5n</span>
          <span class="pm-solve__why">«the sum of a number and 12» = n + 12; «is» = «=»</span>
        </div>
        <div class="pm-solve__row">
          <span class="pm-solve__step">12 = 4n</span>
          <span class="pm-solve__why">Ikkala tomondan n ni ayirdik: 5n − n = 4n</span>
        </div>
        <div class="pm-solve__row pm-solve__row--ans">
          <span class="pm-solve__step">n = 3</span>
          <span class="pm-solve__why">12 ÷ 4 = 3. Tekshirish: 3 + 12 = 15 = 5 × 3 ✓</span>
        </div>
      </div>
      <p>Bu savolni backsolving bilan ham yechish mumkin: B) 3 → 3 + 12 = 15 va 5 × 3 = 15 ✓
      — bitta urinishda tugadi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">2</span>
  <span class="ps-trap__why">n ni ayirish oʻrniga <b>qoʻshgan</b>: 12 = 6n → n = 2.
  5n − n = 4n, 6n emas: harfli hadni oʻtkazganda ishoraga qarang.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Javoblar <b>tenglama</b> boʻlsa (son emas), tenglama tuzib ovora boʻlmang — bitta
  qulay son bilan sinang.</p>
  <ol>
    <li>Oʻzingiz oson sonni tanlang (10 ta xabar, 2 oy, 1 mil).</li>
    <li>Vaziyatdan javobni <em>qoʻlda</em> hisoblang: «$20 + 10 ta × $0.10 = $21».</li>
    <li>Shu sonni har bir javobga qoʻying; $21 bergani — javob.</li>
  </ol>
  <p>Bu 20 soniya oladi va ishorada yoki tartibda adashish ehtimolini nolga tushiradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">«7 less than 3 times a number» → 7 − 3n</p>
  <p class="pe-good">«7 less than 3 times a number» → 3n − 7</p>
  <p class="pe-fix__why"><em>less than</em> ayirmani <b>teskari</b> tartibda yozadi:
  nimadan kam boʻlsa, oʻsha oldin turadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">«$15 per month for m months» → 15 + m</p>
  <p class="pe-good">«$15 per month for m months» → 15m</p>
  <p class="pe-fix__why"><em>per</em> — har doim koʻpaytirish. Har oy takrorlanadigan
  toʻlov oylar soniga koʻpayadi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ingliz tilidagi masalada <b>birlik</b>ni doim yozib qoʻying: «m = <u>oylar</u> soni»,
  «C = <u>dollarda</u> jami». SAT birlikni jumla ichida almashtiradi (minutes ↔ hours,
  per week ↔ per year) va faqat birlik yozib qoʻygan oʻquvchi buni sezadi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <em>«How many»</em> — nechta (sanaladigan narsa: kitob, oy, xabar).
  <em>«How much»</em> — qancha (oʻlchanadigan narsa: pul, suv, vaqt). Tenglamani tuzib
  boʻlgach, savolning shu ikki soʻzidan biri javob <b>nima</b> ekanini aytadi: masalan
  soatlar sonimi yoki toʻlangan pulmi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Write an expression: «8 less than twice a number <i>n</i>».</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">2<i>n</i> − 8 — avval «twice a number» = 2n, keyin «8 less than»
  uni 8 ga kamaytiradi. 8 − 2n emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  A plumber charges $60 for a visit plus $45 per hour. Write an equation for the total
  cost <i>C</i> of a job lasting <i>h</i> hours.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>C</i> = 45<i>h</i> + 60 — 60 bir marta, 45 esa har soat uchun,
  demak soatlar soniga koʻpayadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Three consecutive integers add up to 48. What is the smallest one?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">15 — <i>n</i> + (<i>n</i> + 1) + (<i>n</i> + 2) = 48 →
  3<i>n</i> + 3 = 48 → <i>n</i> = 15. Sonlar: 15, 16, 17.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  A store sells a shirt for $24, which is $6 less than twice what it paid for the shirt.
  How much did the store pay?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">$15 — 2<i>p</i> − 6 = 24 → 2<i>p</i> = 30 → <i>p</i> = 15.
  Tekshiring: 2 × 15 − 6 = 24 ✓</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A tank holds 500 liters and is draining at 12 liters per minute. After how many minutes
  will it hold 320 liters?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">15 daqiqa — 500 − 12<i>m</i> = 320 → 12<i>m</i> = 180 →
  <i>m</i> = 15. «Draining» = kamayish, shuning uchun <b>minus</b>: 500 + 12m emas.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>less than</b><span>…dan kam; ayirishni teskari tartibda yozadi</span></li>
  <li><b>more than</b><span>…dan koʻp; qoʻshish</span></li>
  <li><b>twice / three times</b><span>ikki barobar / uch barobar</span></li>
  <li><b>per</b><span>har biri uchun; har doim koʻpaytirish</span></li>
  <li><b>flat fee / one-time fee</b><span>bir martalik toʻlov; harfsiz son</span></li>
  <li><b>total</b><span>jami; odatda tenglamaning oʻng tomoni</span></li>
  <li><b>consecutive integers</b><span>ketma-ket butun sonlar: n, n + 1, n + 2</span></li>
  <li><b>at first / initially</b><span>boshida; boshlangʻich qiymat</span></li>
  <li><b>represents</b><span>ifodalaydi; «qaysi tenglama toʻgʻri» savoli</span></li>
  <li><b>remaining</b><span>qolgan; koʻpincha ayirish</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Harfni nimaga qoʻyganingizni yozing</b> — birligi bilan. Bu bir soniya, lekin
        yarim xatoni yoʻq qiladi.</li>
    <li>Bir marta toʻlanadigan son <b>yolgʻiz</b>, har safar takrorlanadigan son
        <b>harf bilan</b> turadi.</li>
    <li><em>«5 less than x»</em> = <b>x − 5</b>. Ingliz tilining tartibi matematikaning
        tartibi emas.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-4 — absolute value equations
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-4: Understanding Absolute Value Equations",
        "category": "math",
        "order": 4,
        "summary": (
            "Modul — noldan uzoqlik. Shuning uchun |x| = 7 ning ikkita yechimi bor. "
            "Modulni izolyatsiya qilish, ikki holatga ajratish va SAT juda yaxshi "
            "koʻradigan «yechimlar yigʻindisi» savoli."
        ),
        "content": """
<h2>SAT-4: Understanding Absolute Value Equations</h2>

<p>Modul (<em>absolute value</em>) — SAT'da har testda bir-ikki marta uchraydigan, oʻrganish
oson va xato qilish undan ham oson mavzu. Butun sir bitta jumlada: <mark>modul — sonning
noldan uzoqligi, uzoqlik esa hech qachon manfiy boʻlmaydi</mark>. Shundan «ikki yechim»
qoidasi ham, «yechim yoʻq» holati ham oʻz-oʻzidan kelib chiqadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>|<em>x</em>| ni «noldan uzoqlik» deb oʻqiysiz va nega ikkita javob borligini tushunasiz;</li>
    <li>|<em>ax</em> + <em>b</em>| = <em>c</em> ni ikki oddiy tenglamaga ajratasiz;</li>
    <li>modulni avval <u>yolgʻiz qoldirishni</u> (izolyatsiya) unutmaysiz;</li>
    <li>yechimi yoʻq holatni bir qarashda tanib olasiz va vaqt tejaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The rule</span>
  <span class="pe-chip pe-chip--s">|A| = c</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">A = c</span>
  <span class="pe-op">yoki</span>
  <span class="pe-chip pe-chip--neg">A = −c</span>
  <span class="pe-chip pe-chip--opt">c ≥ 0 boʻlsa</span>
</div>

<h3>Modul — uzoqlik, ishora emas</h3>

<p>|7| = 7 va |−7| = 7. Ikkalasi ham noldan yetti qadam uzoqlikda. Shuning uchun
«|<em>x</em>| = 7» degan savol aslida shuni soʻraydi: <em>«qaysi sonlar noldan yetti qadam
uzoqlikda?»</em> Javob ikkita: <strong>7 va −7</strong>.</p>

<p>Xuddi shu mantiq ichkarida ifoda turganda ham ishlaydi. |<em>x</em> − 4| = 6 —
«<em>x</em> soni <strong>4</strong> dan olti qadam uzoqlikda» degani. Chapga ham, oʻngga
ham olti qadam:</p>

<div class="pm-num">
  <div class="pm-num__track">
    <span class="pm-num__band" style="left:12.5%;width:37.5%"></span>
    <span class="pm-num__band" style="left:50%;width:37.5%"></span>
    <span class="pm-num__tick" style="left:0%"><i>−4</i></span>
    <span class="pm-num__tick" style="left:25%"><i>0</i></span>
    <span class="pm-num__tick" style="left:50%"><i>4</i></span>
    <span class="pm-num__tick" style="left:75%"><i>8</i></span>
    <span class="pm-num__tick" style="left:100%"><i>12</i></span>
    <span class="pm-num__dot" style="left:12.5%"><i>−2</i></span>
    <span class="pm-num__dot" style="left:87.5%"><i>10</i></span>
  </div>
</div>

<p>Ikkala nuqta ham 4 dan aynan 6 qadam narida: 4 − 6 = −2 va 4 + 6 = 10. Demak yechimlar
<strong>x = −2</strong> va <strong>x = 10</strong>.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Modul <b>ichidagi</b> ifoda bemalol manfiy boʻlishi mumkin — cheklanadigan narsa
  natijaning oʻzi. |−9| = 9 da ichkarida −9 turibdi va bu mutlaqo normal. Shuning uchun
  ikkinchi holda «A = −c» deb yozishdan qoʻrqmang.
</div>

<h3>Usul: ikki tenglamaga ajratish</h3>

<blockquote>|<em>A</em>| = <em>c</em> koʻrinishidagi tenglama <u>ikkita</u> oddiy tenglamaga
ajraladi: <em>A</em> = <em>c</em> va <em>A</em> = −<em>c</em>. Har birini alohida yechasiz.</blockquote>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">|2x + 1| = 9</span>
    <span class="pm-solve__why">Berilgan tenglama</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + 1 = 9  →  x = 4</span>
    <span class="pm-solve__why">Birinchi hol: ichkaridagi ifoda musbat 9 ga teng</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2x + 1 = −9  →  x = −5</span>
    <span class="pm-solve__why">Ikkinchi hol: ichkaridagi ifoda −9 ga teng</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>|2 · 4 + 1| = |9| = 9 ✓ va |2 · (−5) + 1| = |−9| = 9 ✓ — ikkala yechim ham toʻgʻri.</p>
</div>

<h3>Avval modulni yolgʻiz qoldiring</h3>

<p>Agar modul oldida son yoki yonida qoʻshiluvchi boʻlsa, ikkiga ajratishdan <u>oldin</u>
uni yolgʻiz qoldirish kerak. Bu — eng koʻp yoʻqotiladigan qadam.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3|x − 2| + 4 = 16</span>
    <span class="pm-solve__why">Berilgan tenglama</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3|x − 2| = 12</span>
    <span class="pm-solve__why">Ikkala tomondan 4 ni ayirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">|x − 2| = 4</span>
    <span class="pm-solve__why">Ikkala tomonni 3 ga boʻldik — endi modul yolgʻiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 6  yoki  x = −2</span>
    <span class="pm-solve__why">x − 2 = 4 va x − 2 = −4</span>
  </div>
</div>

<div class="pe-fix">
  <p class="pe-bad">3|x − 2| + 4 = 16 → 3(x − 2) + 4 = 16 <b>va</b> 3(x − 2) + 4 = −16</p>
  <p class="pe-good">Avval izolyatsiya: |x − 2| = 4, keyin x − 2 = ±4</p>
  <p class="pe-fix__why">Ikkiga ajratish qoidasi faqat modul <b>yolgʻiz</b> turganda
  ishlaydi. Aks holda ikkinchi tenglama butunlay notoʻgʻri chiqadi.</p>
</div>

<h3>Qachon yechim yoʻq</h3>

<p>|<em>x</em> + 3| = −5 — bu savolni yechishning hojati yoʻq. Uzoqlik manfiy boʻlmaydi,
demak <strong>no solution</strong>. SAT bu holatni tez javob beriladigan «sovgʻa» savol
sifatida ishlatadi: modul <u>yolgʻiz qolgach</u> oʻng tomonda manfiy son tursa, javob shu.</p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  |<em>x</em> + 3| − 5 = 0 tenglamasida oʻng tomonda 0 turibdi, lekin bu «yechim yoʻq»
  degani emas! Avval izolyatsiya qiling: |<em>x</em> + 3| = 5. Manfiy son
  <b>izolyatsiyadan keyin</b> paydo boʻlishi kerak.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  |<em>x</em>| = 0 boʻlsa, yechim <b>bitta</b>: <em>x</em> = 0 (nol noldan nol qadam
  uzoqlikda). Demak modulli tenglamada yechimlar soni 0, 1 yoki 2 boʻlishi mumkin —
  SAT aynan shuni «<em>how many solutions</em>» deb soʻraydi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Inglizcha <em>«the distance between x and 4 is 6»</em> jumlasi — bu aynan
  |<em>x</em> − 4| = 6. SAT modulni koʻpincha <b>belgisiz</b>, faqat «distance» soʻzi bilan
  soʻraydi. «Distance» soʻzini koʻrsangiz, modulni oʻylang.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>the positive solution</b><span>musbat yechim — ikkitasidan musbatini yozing</span></li>
  <li><b>the sum of the solutions</b><span>yechimlar yigʻindisi — ikkalasini qoʻshing</span></li>
  <li><b>how many solutions</b><span>nechta yechim bor — 0, 1 yoki 2</span></li>
  <li><b>the distance between x and 4 is 6</b><span>|x − 4| = 6 ning soʻz bilan aytilishi</span></li>
  <li><b>which value of x satisfies</b><span>qaysi qiymat tenglamani qanoatlantiradi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>If |2<i>x</i> − 5| = 11, what is the positive value of <i>x</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>−3</li>
    <li>3</li>
    <li>8</li>
    <li>16</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 8</p>
      <div class="pm-solve">
        <div class="pm-solve__row">
          <span class="pm-solve__step">2x − 5 = 11  →  2x = 16  →  x = 8</span>
          <span class="pm-solve__why">Birinchi hol</span>
        </div>
        <div class="pm-solve__row">
          <span class="pm-solve__step">2x − 5 = −11  →  2x = −6  →  x = −3</span>
          <span class="pm-solve__why">Ikkinchi hol</span>
        </div>
        <div class="pm-solve__row pm-solve__row--ans">
          <span class="pm-solve__step">x = 8</span>
          <span class="pm-solve__why">Savol <b>musbat</b> yechimni soʻradi</span>
        </div>
      </div>
      <p>Ikkala yechim ham javoblar orasida turibdi — savolning oxirgi soʻzi qaysi birini
      belgilashni hal qiladi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">16</span>
  <span class="ps-trap__why">2<i>x</i> = 16 topilgan, lekin 2 ga boʻlinmagan — bir qadam
  yetmay toʻxtagan javob.</span>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">−3</span>
  <span class="ps-trap__why">Toʻgʻri hisoblangan, lekin <b>notoʻgʻri yechim</b> belgilangan:
  savol musbat qiymatni soʻradi. Ikki yechimli savolda oxirgi jumla eng muhim jumla.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>In the equation |<i>x</i> − 4| = 6, what is the sum of all possible values
    of <i>x</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>−2</li>
    <li>8</li>
    <li>10</li>
    <li>12</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 8</p>
      <p>x − 4 = 6 → <b>x = 10</b>; x − 4 = −6 → <b>x = −2</b>.
      Yigʻindi: 10 + (−2) = <b>8</b>.</p>
      <p>Yuqoridagi sonlar oʻqiga qarang: ikki yechim 4 dan bir xil uzoqlikda turibdi,
      demak ularning oʻrtasi — aynan 4. Shuning uchun yigʻindi har doim 2 × 4 = 8 ga teng
      boʻladi, ichkaridagi 6 qanday boʻlishidan qatʼi nazar.</p>
    </div>
  </details>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>|<em>x</em> − <em>a</em>| = <em>b</em> koʻrinishidagi tenglamada:</p>
  <ol>
    <li>yechimlar <b>yigʻindisi</b> har doim 2<em>a</em> — hisoblamasdan yozish mumkin;</li>
    <li>yechimlar orasidagi <b>masofa</b> har doim 2<em>b</em>;</li>
    <li>yechimlarning <b>oʻrtasi</b> — <em>a</em> ning oʻzi.</li>
  </ol>
  <p>SAT «sum of the solutions» ni tez-tez soʻraydi; bu uch qatorni bilgan oʻquvchi
  savolni 10 soniyada yopadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">|x| = 7 → x = 7</p>
  <p class="pe-good">|x| = 7 → x = 7 <b>yoki</b> x = −7</p>
  <p class="pe-fix__why">Bitta javob bilan toʻxtash — bu mavzudagi eng koʻp uchraydigan
  xato. Modul bor joyda «ikkita» deb oʻylang.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Solve: |<i>x</i> + 2| = 9</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> = 7 yoki <i>x</i> = −11 — x + 2 = 9 va x + 2 = −9.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Solve: |3<i>x</i>| = 12</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> = 4 yoki <i>x</i> = −4 — 3x = 12 va 3x = −12.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  How many solutions does |<i>x</i> − 1| = −4 have?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Bittasi ham yoʻq (<em>no solution</em>) — modul manfiy qiymat
  qabul qilmaydi, chunki u uzoqlikni bildiradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Solve: 2|<i>x</i> + 1| − 3 = 7</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a"><i>x</i> = 4 yoki <i>x</i> = −6 — avval izolyatsiya:
  2|x + 1| = 10 → |x + 1| = 5, keyin x + 1 = ±5.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A machine fills bottles with 500 ml. A bottle passes inspection if the difference between
  its volume <i>v</i> and 500 ml is at most 8 ml, written |<i>v</i> − 500| = 8 at the limit.
  What are the two limit volumes?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">492 ml va 508 ml — v − 500 = 8 va v − 500 = −8. Modul real
  hayotda deyarli har doim «meʼyordan chetlanish» maʼnosida keladi.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>absolute value</b><span>modul; noldan uzoqlik</span></li>
  <li><b>distance from zero</b><span>noldan uzoqlik — modulning taʼrifi</span></li>
  <li><b>solution(s)</b><span>yechim(lar); modulda odatda ikkita</span></li>
  <li><b>the sum of the solutions</b><span>yechimlar yigʻindisi</span></li>
  <li><b>positive / negative</b><span>musbat / manfiy</span></li>
  <li><b>no solution</b><span>yechimi yoʻq</span></li>
  <li><b>isolate</b><span>yolgʻiz qoldirish (modulni bir tomonda)</span></li>
  <li><b>satisfies the equation</b><span>tenglamani qanoatlantiradi</span></li>
  <li><b>at most</b><span>koʻpi bilan; ≤ (tengsizlik — SAT-22)</span></li>
  <li><b>difference</b><span>ayirma</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Modul — <b>uzoqlik</b>. Shuning uchun |A| = c ikkita tenglamaga ajraladi:
        A = c va A = −c.</li>
    <li>Ikkiga ajratishdan <b>oldin</b> modulni yolgʻiz qoldiring.</li>
    <li>Modul yolgʻiz qolgach oʻng tomonda manfiy son tursa — <b>no solution</b>,
        hisoblashning hojati yoʻq.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-5 — the concept of slope
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-5: The Concept of Slope: Steepness and Direction",
        "category": "math",
        "order": 5,
        "summary": (
            "Qiyalik — chiziqning tikligi va yoʻnalishi: rise ÷ run. Grafikdan, "
            "jadvaldan va tenglamadan oʻqish, ishorasining maʼnosi va SAT'ning eng "
            "sevimli savoli: «bu son kontekstda nimani bildiradi?»"
        ),
        "content": """
<h2>SAT-5: The Concept of Slope: Steepness and Direction</h2>

<p>Qiyalik (<em>slope</em>) — SAT Math'dagi eng koʻp «ishlaydigan» bitta tushuncha. U
chiziqli grafiklarda ham, matnli masalalarda ham, jadvalli savollarda ham chiqadi va
deyarli har testda kamida bitta savol shunday yangraydi: <em>«What does the 15 represent
in this context?»</em> Bu darsda formulani emas, avvalo <mark>maʼnosini</mark> oʻrnatamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>qiyalikni «bir qadam oʻngga yurganda necha qadam koʻtarilamiz» deb oʻqiysiz;</li>
    <li>grafikdan va jadvaldan qiyalikni sanaysiz;</li>
    <li>ishorasidan chiziqning yoʻnalishini aytasiz (musbat, manfiy, nol, aniqlanmagan);</li>
    <li>qiyalikning <u>kontekstdagi maʼnosini</u> tushuntirasiz — SAT'ning sevimli savoli.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Slope</span>
  <span class="pe-chip pe-chip--s">m</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">rise</span>
  <span class="pe-op">÷</span>
  <span class="pe-chip pe-chip--o">run</span>
  <span class="pe-chip pe-chip--opt">y ning oʻzgarishi ÷ x ning oʻzgarishi</span>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Qiyalik formulasi test ekranidagi <em>reference sheet</em> da <b>YOʻQ</b>. U yerda faqat
  yuza, hajm, aylana va maxsus uchburchaklar bor. Slope, kvadrat tenglama formulasi va
  oʻrta arifmetik — yod olinadi.
</div>

<h3>Qiyalik nimani bildiradi</h3>

<p><strong>Rise</strong> — yuqoriga koʻtarilish (<em>y</em> ning oʻzgarishi),
<strong>run</strong> — oʻngga yurish (<em>x</em> ning oʻzgarishi). Qiyalik — bu ikkisining
nisbati, yaʼni <mark>bir qadam oʻngga yurganda <em>y</em> qancha oʻzgaradi</mark>.
Pastdagi chiziqda oʻngga 4 qadam yurganda 8 birlik koʻtarildik, demak har bir qadamga
2 birlik: <em>m</em> = 8 ÷ 4 = 2.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 220" role="img" aria-label="Ikki nuqtadan oʻtgan chiziq, rise va run koʻrsatilgan">
    <line class="pm-ln" x1="30" y1="190" x2="310" y2="190"/>
    <line class="pm-ln" x1="40" y1="20" x2="40" y2="200"/>
    <line class="pm-ln pm-ln--hl" x1="72" y1="183" x2="268" y2="21"/>
    <line class="pm-ln pm-ln--dash" x1="105" y1="150" x2="235" y2="150"/>
    <line class="pm-ln pm-ln--dash" x1="235" y1="150" x2="235" y2="43"/>
    <circle class="pm-pt" cx="105" cy="150" r="4"/>
    <circle class="pm-pt" cx="235" cy="43" r="4"/>
    <text class="pm-lbl" x="78" y="168">(2, 3)</text>
    <text class="pm-lbl" x="212" y="35">(6, 11)</text>
    <text class="pm-lbl pm-lbl--hl" x="140" y="168">run = 4</text>
    <text class="pm-lbl pm-lbl--hl" x="242" y="100">rise = 8</text>
    <text class="pm-lbl" x="298" y="205">x</text>
    <text class="pm-lbl" x="26" y="26">y</text>
  </svg>
  <figcaption>Oʻngga 4, yuqoriga 8 → qiyalik 8 ÷ 4 = 2. Har bir qadam oʻngga — ikki birlik yuqoriga.</figcaption>
</figure>

<h3>Ishora — chiziqning yoʻnalishi</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Positive slope (m &gt; 0)</p>
    <p>Chap tomondan oʻngga qarab <b>koʻtariladi</b>. Kontekstda: miqdor ortib boradi —
    tejalgan pul, oʻsgan boʻy, yigʻilgan ochko.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Negative slope (m &lt; 0)</p>
    <p>Oʻngga qarab <b>pasayadi</b>. Kontekstda: kamayish — bakdagi suv, qolgan masofa,
    sovuyotgan choy.</p>
  </div>
</div>

<ul>
  <li><strong>m = 0</strong> — gorizontal chiziq. <em>y</em> hech oʻzgarmaydi
      (<em>«remains constant»</em>).</li>
  <li><strong>Undefined slope</strong> — vertikal chiziq. Run = 0 boʻladi, nolga boʻlish
      esa mumkin emas. Shuning uchun «qiyaligi 0» emas, «<em>undefined</em>».</li>
</ul>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Gorizontal chiziqning qiyaligi <b>0</b>, vertikal chiziqniki <b>aniqlanmagan</b>
  (<em>undefined</em>). Bu ikkisi doim adashtiriladi. Esda saqlang: nol — «tekis yoʻl»,
  aniqlanmagan — «devor, unga chiqib boʻlmaydi».
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qiyalikni oʻzbekchada «bir qadamga qancha» deb oʻqing. <em>m</em> = 3 — «har bir qadam
  oʻngga, uch birlik yuqoriga». Shu bitta jumla keyinchalik <em>y</em> = <em>mx</em> +
  <em>b</em> ni ham (SAT-7), parallel va perpendikulyar chiziqlarni ham (SAT-11, SAT-12)
  osonlashtiradi.
</div>

<h3>Jadvaldan qiyalikni topish</h3>

<p>Jadval berilganda ikkita ustunning <u>oʻzgarishini</u> qaraymiz. Muhim shart: <em>x</em>
qadami teng boʻlishi shart emas, lekin nisbat har doim bir xil chiqishi kerak — aks holda
bogʻlanish chiziqli emas.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>x</th><th>0</th><th>2</th><th>4</th><th>6</th></tr>
  <tr><td>y</td><td>5</td><td>11</td><td>17</td><td>23</td></tr>
</table></div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x: 0 → 2,  y: 5 → 11</span>
    <span class="pm-solve__why">Ikki ustunni tanladik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">rise = 6,  run = 2</span>
    <span class="pm-solve__why">y 6 ga ortdi, x 2 ga ortdi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">m = 6 ÷ 2 = 3</span>
    <span class="pm-solve__why">Boshqa ustunlarda ham 6 ÷ 2 = 3 — demak chiziqli</span>
  </div>
</div>

<h3>Kontekstdagi maʼnosi — SAT'ning sevimli savoli</h3>

<p>Amaliy masalada qiyalik har doim bitta narsani bildiradi: <mark>bir birlik uchun necha
birlik</mark> — «per» soʻzi bilan aytiladigan son. Agar
<em>C</em> = 6<em>h</em> + 10 boʻlsa, 6 — har bir qoʻshimcha soat uchun toʻlanadigan
$6; 10 esa boshlangʻich toʻlov (<em>y</em>-intercept, SAT-7).</p>

<div class="pe-ex">
  <p class="pe-ex__math">C = 6h + 10</p>
  <p class="pe-ex__uz">Har qoʻshimcha soat uchun $6, ustiga bir martalik $10.</p>
  <p class="pe-ex__why">Diqqat: bir soatlik ijara $6 emas, $16. Qiyalik — <b>oʻzgarish</b>,
  boshlangʻich qiymat emas.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikki nuqtaning ayirmasini olayotganda <b>tartibni buzmang</b>: agar yuqorida
  11 − 3 desangiz, pastda ham xuddi shu nuqtadan boshlab 6 − 2 boʻlishi kerak.
  Bittasini teskari olsangiz, ishora notoʻgʻri chiqadi va javob tuzoqqa tushadi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>what is the slope of the line</b><span>chiziqning qiyaligi qancha</span></li>
  <li><b>which is the best interpretation of 6</b><span>6 soni kontekstda nimani bildiradi</span></li>
  <li><b>for each additional hour</b><span>har bir qoʻshimcha soat uchun — bu qiyalik</span></li>
  <li><b>increases at a constant rate</b><span>oʻzgarmas tezlikda ortadi — chiziqli model</span></li>
  <li><b>remains constant</b><span>oʻzgarmaydi — qiyaligi 0</span></li>
  <li><b>rate of change</b><span>oʻzgarish tezligi — qiyalikning boshqacha nomi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>A line in the <i>xy</i>-plane passes through the points (2, 3) and (6, 11).
    What is the slope of the line?</p>
  </div>
  <ol class="ps-ch">
    <li>1/2</li>
    <li>2</li>
    <li>4</li>
    <li>8</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 2</p>
      <div class="pm-solve">
        <div class="pm-solve__row">
          <span class="pm-solve__step">rise = 11 − 3 = 8</span>
          <span class="pm-solve__why">y larning ayirmasi</span>
        </div>
        <div class="pm-solve__row">
          <span class="pm-solve__step">run = 6 − 2 = 4</span>
          <span class="pm-solve__why">x larning ayirmasi, <b>xuddi shu tartibda</b></span>
        </div>
        <div class="pm-solve__row pm-solve__row--ans">
          <span class="pm-solve__step">m = 8 ÷ 4 = 2</span>
          <span class="pm-solve__why">Yuqoridagi chizmadagi chiziqning oʻzi</span>
        </div>
      </div>
      <p>Ikki nuqtadan qiyalik topishning rasmiy formulasi SAT-6 da, lekin u aynan shu
      ikki ayirmaning nisbati.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">1/2</span>
  <span class="ps-trap__why">Nisbat teskari olingan: run ÷ rise. Tartib har doim
  <b>rise ustida, run pastda</b> — «y avval».</span>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">8</span>
  <span class="ps-trap__why">Faqat rise hisoblangan, run ga boʻlinmagan. Qiyalik —
  koʻtarilishning oʻzi emas, <b>nisbati</b>.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>The total cost <i>C</i>, in dollars, of renting a bike for <i>h</i> hours is given
    by <i>C</i> = 6<i>h</i> + 10. Which of the following is the best interpretation of the
    number 6 in this context?</p>
  </div>
  <ol class="ps-ch">
    <li>The initial cost of renting the bike is $6.</li>
    <li>The cost increases by $6 for each additional hour.</li>
    <li>The bike can be rented for a maximum of 6 hours.</li>
    <li>The total cost of renting the bike for one hour is $6.</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) The cost increases by $6 for each additional hour.</p>
      <p>6 — <i>h</i> ning oldida turibdi, demak u <b>qiyalik</b>: har bir qoʻshimcha soat
      narxni $6 ga oshiradi. Hisoblash kerak emas — faqat maʼnosini oʻqish kerak.</p>
      <p>A) notoʻgʻri: boshlangʻich narx 10 (u harfsiz turibdi).
      D) notoʻgʻri: bir soatlik ijara 6 × 1 + 10 = $16.</p>
    </div>
  </details>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>«Interpretation» savolida hech narsa hisoblamang. Ikki savol bering:</p>
  <ol>
    <li>Bu son <b>harf bilanmi</b> turibdi? Ha boʻlsa — u qiyalik: «har bir … uchun».</li>
    <li>Yolgʻiz turibdimi? Unda u boshlangʻich qiymat: «boshida», «bir martalik».</li>
  </ol>
  <p>Bu savollar 15 soniya oladi, lekin SAT'da har testda 2–4 marta uchraydi — eng foydali
  15 soniya.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">(2, 3) va (6, 11) uchun m = (6 − 2) ÷ (11 − 3)</p>
  <p class="pe-good">m = (11 − 3) ÷ (6 − 2)</p>
  <p class="pe-fix__why">Ustida <b>y</b> lar, pastda <b>x</b> lar. Teskari yozilsa javob
  har doim javoblar orasidagi tuzoqqa tushadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Vertikal chiziqning qiyaligi 0.</p>
  <p class="pe-good">Vertikal chiziqning qiyaligi <b>undefined</b>; gorizontalniki 0.</p>
  <p class="pe-fix__why">Vertikal chiziqda run = 0, nolga boʻlish esa aniqlanmagan.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  What is the slope of the line through (1, 2) and (5, 14)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">3 — rise = 14 − 2 = 12, run = 5 − 1 = 4, m = 12 ÷ 4 = 3.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  A line passes through (0, 9) and (3, 0). Is its slope positive or negative, and what
  is it?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Manfiy, m = −3 — rise = 0 − 9 = −9, run = 3 − 0 = 3.
  Chiziq oʻngga qarab pasaymoqda.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  In a table, <i>x</i> goes 1, 3, 5 and <i>y</i> goes 20, 14, 8. What is the slope?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">−3 — har safar x 2 ga ortganda y 6 ga kamayadi: −6 ÷ 2 = −3.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  The number of liters in a tank is <i>L</i> = 500 − 12<i>m</i>, where <i>m</i> is minutes.
  What does −12 represent?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Har daqiqada bakdan 12 litr kamayadi. Manfiy qiyalik —
  kamayish; 500 esa boshlangʻich hajm.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A worker's pay is <i>P</i> = 18<i>h</i> + 40. Which is bigger: the pay for one hour of
  work, or the number 18? Explain.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Bir soatlik toʻlov kattaroq: 18 × 1 + 40 = $58, 18 esa faqat
  <b>har qoʻshimcha soat</b> uchun. Qiyalik — oʻzgarish, jami emas. SAT aynan shu farqni
  sinaydi.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>slope</b><span>qiyalik; tiklik va yoʻnalish</span></li>
  <li><b>rise</b><span>koʻtarilish; y ning oʻzgarishi</span></li>
  <li><b>run</b><span>oʻngga yurish; x ning oʻzgarishi</span></li>
  <li><b>rate of change</b><span>oʻzgarish tezligi — qiyalikning ikkinchi nomi</span></li>
  <li><b>constant rate</b><span>oʻzgarmas tezlik; chiziqli model</span></li>
  <li><b>xy-plane</b><span>koordinata tekisligi</span></li>
  <li><b>undefined</b><span>aniqlanmagan (vertikal chiziq)</span></li>
  <li><b>interpretation</b><span>maʼnosi; «bu son nimani bildiradi»</span></li>
  <li><b>per additional hour</b><span>har bir qoʻshimcha soat uchun</span></li>
  <li><b>initial value</b><span>boshlangʻich qiymat; harfsiz turgan son</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Qiyalik = <b>rise ÷ run</b> — ustida y lar, pastda x lar. Teskarisi — tuzoq javob.</li>
    <li>Musbat — koʻtariladi, manfiy — pasayadi, 0 — gorizontal,
        <b>undefined</b> — vertikal.</li>
    <li>Kontekstda qiyalik har doim «<b>har bir … uchun</b>» degan son. Boshlangʻich qiymat
        emas — u harfsiz turadi.</li>
  </ul>
</div>
""",
    },
]
