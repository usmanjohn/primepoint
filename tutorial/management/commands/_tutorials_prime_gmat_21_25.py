# -*- coding: utf-8 -*-
"""Prime GMAT — GMAT-21 … GMAT-25: sequences, counting, probability, statistics, and the
section-strategy lesson that closes the Quant block.

Written with STYLE_GUIDE_PRIME_GMAT.md (on top of STYLE_GUIDE_PRIME_SAT.md) ·
lesson list in toc_prime_gmat.txt. Exam English in the stems, Uzbek for the teaching.
Five answer choices, no calculator, no geometry, no data sufficiency.

GMAT-25's facts (mba.com, checked 2026-10-01): 21 Quant questions in 45 minutes; the
candidate may bookmark questions and, with time left, use Question Review & Edit to change
up to three answers per section. Unanswered questions cost score, so never leave blanks.

Import:
    python manage.py import_tutorials tutorial/management/commands/_tutorials_prime_gmat_21_25.py --author=prime
"""

PLAYLIST = {
    "title": "Prime GMAT",
    "category": "math",
    "description": (
        "GMAT Focus Edition'ning Quant boʻlimi — biznes maktabiga yoʻl. Savollar ingliz "
        "tilida, chunki imtihon shunday; tushuntirish oʻzbek tilida. Har bir darsda "
        "haqiqiy GMAT uslubidagi savollar, tuzoq javoblar va 20 savollik mashq."
    ),
}

GMAT21 = """
<h2>GMAT-21: Sequences and Series</h2>

<p>Ketma-ketlik — maʼlum qoida bilan yozilgan sonlar qatori. GMAT'da ikki turi ustun:
<mark>arifmetik</mark> (har safar bir xil son qoʻshiladi) va <mark>geometrik</mark> (har safar
bir xil songa koʻpaytiriladi). Biznes tilida bular — har yili bir xil summaga oshadigan
maosh va har yili bir xil foizga oʻsadigan tushum. Savollar uch narsani soʻraydi:
<i>n</i>-hadni, hadlar sonini va yigʻindini.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>arifmetik va geometrik ketma-ketlikning istalgan hadini topasiz;</li>
    <li>teng qadamli qatordagi hadlar sonini xatosiz sanaysiz;</li>
    <li>arifmetik qator yigʻindisini «oʻrtacha × soni» bilan hisoblaysiz;</li>
    <li>rekursiv (oldingi hadga tayangan) qoidani qadam-baqadam yozasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Arithmetic sequence</span>
  <span class="pe-chip pe-chip--o">n-th term</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">first</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">(n − 1) × step</span>
</div>

<h3>Arifmetik ketma-ketlik</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3, 7, 11, … — 10-had?</span>
    <span class="pm-solve__why">Qadam 4, birinchi had 3</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 + (10 − 1) × 4</span>
    <span class="pm-solve__why">Birinchidan oʻninchigacha <b>9</b> ta qadam bor, 10 ta emas</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3 + 36 = 39</span>
    <span class="pm-solve__why">Tekshiruv: 3, 7, 11, 15, 19, 23, 27, 31, 35, 39 ✓</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Panjara va ustunlar» xatosi: 10 ta ustun orasida 9 ta panjara bor. Xuddi shunday,
  10-hadgacha 9 ta qadam bor. Shuning uchun formulada (<i>n</i> − 1) turadi. Hadlar sonini
  sanashda esa teskarisi: 12 dan 96 gacha 4 lik qadam bilan (96 − 12) ÷ 4 = 21 ta qadam,
  demak <b>22 ta</b> had.
</div>

<h3>Yigʻindi — oʻrtacha × soni</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">1 + 2 + … + 50</span>
    <span class="pm-solve__why">Teng qadamli qator — oʻrtacha birinchi va oxirgining oʻrtachasi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Oʻrtacha (1 + 50) ÷ 2 = 25.5; soni 50</span>
    <span class="pm-solve__why">GMAT-11 dagi teng oraliqli toʻplam qoidasi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">25.5 × 50 = 1,275</span>
    <span class="pm-solve__why">Yigʻindi = oʻrtacha × hadlar soni</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Ikki tayyor natijani yodlang: birinchi <i>n</i> ta musbat butun son yigʻindisi
  <i>n</i>(<i>n</i> + 1) ÷ 2, birinchi <i>n</i> ta toq son yigʻindisi <i>n</i><sup>2</sup>.
  1 + 3 + 5 + … + 29 — bu 15 ta toq son, yigʻindisi 225.
</div>

<h3>Geometrik ketma-ketlik va rekursiv qoida</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2, 6, 18, … — 6-had?</span>
    <span class="pm-solve__why">Har safar × 3; 6-hadgacha 5 ta koʻpaytirish</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2 × 3<sup>5</sup> = 2 × 243 = 486</span>
    <span class="pm-solve__why">Bu yerda ham daraja (<i>n</i> − 1)</span>
  </div>
</div>

<p>Rekursiv qoida keyingi hadni <b>oldingisi orqali</b> beradi: «<i>a</i><sub>1</sub> = 1 va har bir
keyingi had oldingisining ikki baravaridan bitta koʻp». Formula izlamang — hadlarni bittalab
yozing: 1, 3, 7, 15, 31. GMAT odatda 4–6 ta haddan uzoqqa bormaydi.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Biznes tilida: «maosh har yili $2,500 ga oshadi» — arifmetik, «tushum har yili 10% ga
  oshadi» — geometrik. Birinchisi chiziq boʻylab, ikkinchisi tobora tezlashib oʻsadi. Uzoq
  muddatda geometrik oʻsish har qanday arifmetik oʻsishdan oʻzib ketadi — bu foiz va
  investitsiya savollarining asosi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Inclusive» va «between» farqiga eʼtibor bering: «from 10 to 100, inclusive» — 10 ham, 100 ham
  kiradi; «between 10 and 100» — odatda chetlar kirmaydi. Hadlar sonini sanashdan oldin chetlar
  kirish-kirmasligini aniqlang — javob aynan shunga qarab bittaga farq qiladi, va GMAT ikkala
  javobni ham variantlarga qoʻyadi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>each term after the first</b><span>birinchisidan keyingi har bir had — qoida</span></li>
  <li><b>the nth term</b><span>n-had</span></li>
  <li><b>consecutive terms</b><span>ketma-ket hadlar</span></li>
  <li><b>the sum of the first 20 terms</b><span>dastlabki 20 ta had yigʻindisi</span></li>
  <li><b>is defined recursively</b><span>oldingi had orqali aniqlanadi</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>What is the sum of the integers from 1 to 50, inclusive?</p>
  </div>
  <ol class="ps-ch">
    <li>1,250</li>
    <li>1,275</li>
    <li>1,300</li>
    <li>2,500</li>
    <li>2,550</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 1,275</p>
      <p>50 × 51 ÷ 2 = 1,275.</p>
      <p><b>2,550</b> — ikkiga boʻlishni unutgan javob: 50 × 51.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">2,550</span>
  <span class="ps-trap__why">Juftlab qoʻshish usulida har bir juft (1 + 50, 2 + 49, …) 51 beradi, lekin
  juftlar soni 50 emas, <b>25</b>.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>In a sequence, the first term is 2 and each term after the first is 3 times the
    preceding term. What is the sixth term of the sequence?</p>
  </div>
  <ol class="ps-ch">
    <li>162</li>
    <li>243</li>
    <li>486</li>
    <li>729</li>
    <li>1,458</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 486</p>
      <p>2, 6, 18, 54, 162, 486 — 2 × 3<sup>5</sup>.</p>
      <p><b>1,458</b> — 2 × 3<sup>6</sup>: bitta ortiqcha koʻpaytirish.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">1,458</span>
  <span class="ps-trap__why">Oltinchi hadgacha <b>beshta</b> qadam bor. Shubha boʻlsa, hadlarni
  yozib chiqing — oltita son bir zumda yoziladi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Ketma-ketlik savolida <b>avval 3–4 hadni yozing</b>:</p>
  <ol>
    <li>qoida aniq koʻrinadi — qadammi yoki koʻpaytuvchimi;</li>
    <li>(<i>n</i> − 1) xatosi tekshiriladi;</li>
    <li>katta had kerak boʻlsa, endi formulaga oʻting: birinchi + (<i>n</i> − 1) × qadam.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">Terms from 12 to 96 in steps of 4: (96 − 12) ÷ 4 = 21</p>
  <p class="pe-good">(96 − 12) ÷ 4 + 1 = 22</p>
  <p class="pe-fix__why">Qadamlar soni + 1 = hadlar soni.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">10th term = 3 + 10 × 4 = 43</p>
  <p class="pe-good">3 + 9 × 4 = 39</p>
  <p class="pe-fix__why">Birinchi haddan oʻninchigacha 9 ta qadam.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> What is the 10th term of 3, 7, 11, …?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">39 — 3 + 9 × 4.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> What is the sum of the first 20 positive even integers?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">420 — 2 × (1 + 2 + … + 20) = 2 × 210.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> How many terms are in the sequence 12, 16, 20, …, 96?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">22 — 21 ta qadam va yana bitta.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> If <i>a</i><sub>1</sub> = 1 and each later term is 1 more
  than twice the term before it, what is the fifth term?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">31 — 1, 3, 7, 15, 31.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> A salary starts at $40,000 and rises by $2,500
  each year. What is it in the sixth year?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">$52,500 — 40,000 + 5 × 2,500.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>sequence</b><span>ketma-ketlik</span></li>
  <li><b>term</b><span>had</span></li>
  <li><b>arithmetic sequence</b><span>arifmetik progressiya</span></li>
  <li><b>geometric sequence</b><span>geometrik progressiya</span></li>
  <li><b>common difference</b><span>ayirma, qadam</span></li>
  <li><b>common ratio</b><span>maxraj, koʻpaytuvchi</span></li>
  <li><b>series / sum</b><span>yigʻindi</span></li>
  <li><b>recursive</b><span>rekursiv — oldingi had orqali</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>n-had: birinchi + (n − 1) × qadam; geometrikda birinchi × koʻpaytuvchi<sup>n − 1</sup>.</li>
    <li>Hadlar soni = (oxirgi − birinchi) ÷ qadam + 1.</li>
    <li>Arifmetik yigʻindi = (birinchi + oxirgi) ÷ 2 × hadlar soni.</li>
    <li>1 dan n gacha: n(n + 1) ÷ 2; birinchi n ta toq son: n<sup>2</sup>.</li>
    <li>Rekursiv qoida — hadlarni bittalab yozing.</li>
  </ul>
</div>
"""

GMAT22 = """
<h2>GMAT-22: Counting — Permutations and Combinations</h2>

<p>«Nechta usul bilan?» — kombinatorika savoli. Javoblar tez kattalashadi, shuning uchun
ularni sanab chiqib boʻlmaydi; <mark>koʻpaytirish qoidasi</mark> va bitta muhim savol kerak:
<b>tartib muhimmi?</b> Muhim boʻlsa — oʻrin almashtirish (<i>permutation</i>), muhim
boʻlmasa — guruhlash (<i>combination</i>). Shu bitta farq GMAT kombinatorikasining yarmini
hal qiladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>bir nechta mustaqil tanlovni koʻpaytirish qoidasi bilan sanaysiz;</li>
    <li>tartib muhim yoki muhim emasligini savol matnidan aniqlaysiz;</li>
    <li>kombinatsiyalar sonini kalkulyatorsiz hisoblaysiz;</li>
    <li>takrorlanuvchi harflar va «yonma-yon oʻtirsin» shartlarini hisobga olasiz.</li>
  </ul>
</div>

<h3>Koʻpaytirish qoidasi</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 ta harf (A–E, takrorlanmasin) + 1 ta raqam</span>
    <span class="pm-solve__why">Har bir oʻrin uchun tanlovlar soni</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5 × 4 × 3 × 10</span>
    <span class="pm-solve__why">Har bir ishlatilgan harf keyingi oʻrindan chiqib ketadi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">600 ta kod</span>
    <span class="pm-solve__why">Mustaqil tanlovlar koʻpaytiriladi</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Va» — koʻpaytirish, «yoki» — qoʻshish. Non <b>va</b> ichimlik tanlansa: 4 × 3. Qahva
  <b>yoki</b> choy (bittasi) tanlansa: 5 + 3. Bizda koʻpchilik hamma narsani koʻpaytiradi —
  tanlov bitta boʻlsa, variantlar qoʻshiladi.
</div>

<h3>Oʻrin almashtirish — tartib muhim</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">8 ta yuguruvchi — oltin, kumush, bronza</span>
    <span class="pm-solve__why">Oltin va kumush — har xil oʻrin, tartib muhim</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">8 × 7 × 6 = 336</span>
    <span class="pm-solve__why">Uchta oʻrin, har birida bittadan kam tanlov</span>
  </div>
</div>

<h3>Guruhlash — tartib muhim emas</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">7 kishidan 3 kishilik qoʻmita</span>
    <span class="pm-solve__why">Qoʻmitada oʻrinlar yoʻq — tartib muhim emas</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">7 × 6 × 5 = 210 tartiblangan uchlik</span>
    <span class="pm-solve__why">Har bir guruh 3! = 6 marta sanaldi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">210 ÷ 6 = 35</span>
    <span class="pm-solve__why">C(7, 3) = 7! ÷ (3! × 4!)</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  C(<i>n</i>, 2) = <i>n</i>(<i>n</i> − 1) ÷ 2 — eng koʻp uchraydigan holat (juftlar, qoʻl
  siqishlar, ikki kishilik jamoa). C(<i>n</i>, <i>k</i>) = C(<i>n</i>, <i>n</i> − <i>k</i>): 10 tadan 8 tasini tanlash —
  bu 2 tasini tashlab qoldirish, C(10, 2) = 45.
</div>

<h3>Takrorlanuvchi harflar va «birga» sharti</h3>

<p>«LEVEL» soʻzining harflarini necha xil tartibda yozish mumkin? 5 ta harf — 5! = 120, lekin
ikkita L va ikkita E oʻz oʻrnini almashtirsa, yangi soʻz chiqmaydi. Shuning uchun 120 ni
2! × 2! = 4 ga boʻlamiz: <b>30</b>. «Ikki kishi yonma-yon oʻtirsin» shartida esa ularni bitta
«blok» deb hisoblang, keyin blok ichidagi 2 xil tartibni koʻpaytiring.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Tartib muhimligini aniqlash uchun bitta savol bering: <b>ikki kishining oʻrnini almashtirsam,
  natija oʻzgaradimi?</b> Prezident va oʻrinbosar almashsa — boshqa natija (tartib muhim).
  Qoʻmitaning ikki aʼzosi almashsa — oʻsha qoʻmita (tartib muhim emas).
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Kamida bittasi» kombinatorikada ham teskari yoʻl bilan oson: hammasi minus hech biri.
  5 erkak va 3 ayoldan 4 kishilik qoʻmitada kamida bitta ayol: C(8, 4) − C(5, 4) = 70 − 5 = 65.
  Toʻgʻridan-toʻgʻri sanash (1, 2 yoki 3 ayol) uchta alohida hisob talab qiladi — teskari yoʻl
  bitta ayirma bilan tugaydi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>in how many different ways</b><span>necha xil usulda</span></li>
  <li><b>arrangements</b><span>tartiblar — oʻrin muhim</span></li>
  <li><b>a committee / a group / a team of 3</b><span>qoʻmita / guruh — tartib muhim emas</span></li>
  <li><b>without repetition</b><span>takrorlanmasdan</span></li>
  <li><b>must sit next to each other</b><span>yonma-yon oʻtirishi shart</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>In how many different ways can a committee of 3 people be chosen from a group of 7 people?</p>
  </div>
  <ol class="ps-ch">
    <li>21</li>
    <li>35</li>
    <li>42</li>
    <li>210</li>
    <li>343</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 35</p>
      <p>7 × 6 × 5 ÷ (3 × 2 × 1) = 35.</p>
      <p><b>210</b> — tartibni hisobga olgan javob; qoʻmitada oʻrinlar yoʻq.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">210</span>
  <span class="ps-trap__why">Oʻrin almashtirish. Bir xil uch kishi 6 xil tartibda sanaldi — 3! ga boʻling.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>A product code consists of 3 different letters chosen from A, B, C, D and E, followed
    by a single digit from 0 to 9. How many different codes are possible?</p>
  </div>
  <ol class="ps-ch">
    <li>60</li>
    <li>125</li>
    <li>600</li>
    <li>1,250</li>
    <li>6,000</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 600</p>
      <p>5 × 4 × 3 × 10 = 600.</p>
      <p><b>1,250</b> — harflar takrorlanishi mumkin deb hisoblangan javob (5 × 5 × 5 × 10).</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">1,250</span>
  <span class="ps-trap__why">«Different letters» — har bir ishlatilgan harf keyingi oʻrindan chiqadi:
  5, keyin 4, keyin 3.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Har bir sanash savolida <b>ikki savol</b> bering:</p>
  <ol>
    <li>takrorlanish mumkinmi? (mumkin — har oʻrinda bir xil son; mumkin emas — kamayib boradi);</li>
    <li>tartib muhimmi? (muhim emas — tartiblar soniga boʻling);</li>
    <li>javobni kichik misolda tekshiring: 3 kishidan 2 kishilik guruh — AB, AC, BC, yaʼni 3 = C(3, 2).</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">Team of 2 from 10: 10 × 9 = 90</p>
  <p class="pe-good">10 × 9 ÷ 2 = 45</p>
  <p class="pe-fix__why">Jamoada AB va BA — bitta jamoa.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Arrangements of LEVEL: 5! = 120</p>
  <p class="pe-good">5! ÷ (2! × 2!) = 30</p>
  <p class="pe-fix__why">Bir xil harflarning oʻrin almashishi yangi soʻz bermaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> A man has 4 shirts and 3 pairs of trousers.
  How many different outfits can he make?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">12 — 4 × 3.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> What is 5! (5 factorial)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">120 — 5 × 4 × 3 × 2 × 1.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> In how many ways can 2 people be chosen from 6?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">15 — 6 × 5 ÷ 2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> How many different arrangements of the letters
  of LEVEL are there?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">30 — 120 ÷ 4.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> In how many ways can gold, silver and bronze
  medals be awarded among 8 runners?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">336 — 8 × 7 × 6.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>permutation</b><span>oʻrin almashtirish — tartib muhim</span></li>
  <li><b>combination</b><span>guruhlash — tartib muhim emas</span></li>
  <li><b>factorial</b><span>faktorial</span></li>
  <li><b>arrangement</b><span>tartib, joylashuv</span></li>
  <li><b>committee</b><span>qoʻmita</span></li>
  <li><b>without repetition</b><span>takrorlanmasdan</span></li>
  <li><b>outcome</b><span>natija</span></li>
  <li><b>code</b><span>kod</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>«Va» — koʻpaytirish, «yoki» — qoʻshish.</li>
    <li>Takrorlanmasa — har oʻrinda tanlov bittaga kamayadi.</li>
    <li>Tartib muhim emas — tartiblar soniga (k!) boʻling: C(7, 3) = 35.</li>
    <li>C(n, 2) = n(n − 1) ÷ 2; C(n, k) = C(n, n − k).</li>
    <li>Bir xil harflar — har bir guruh faktorialiga boʻling; «birga» — blok deb oling.</li>
  </ul>
</div>
"""

GMAT23 = """
<h2>GMAT-23: Probability</h2>

<p>Ehtimollik — kombinatorikaning davomi: <mark>qulay natijalar ÷ barcha natijalar</mark>.
GMAT'dagi ehtimollik savollari uch gʻoyaga tayanadi: «kamida bittasi» uchun teskari
hodisa, mustaqil hodisalar uchun koʻpaytirish va qaytarmasdan olishda maxrajning
kamayishi. Bu dars uchalasini biznes misollari bilan koʻrsatadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>oddiy ehtimollikni qulay ÷ jami deb hisoblaysiz;</li>
    <li>«kamida bittasi» savolini 1 − «hech biri» bilan yechasiz;</li>
    <li>mustaqil hodisalarda koʻpaytirasiz, bir-birini istisno qiluvchilarda qoʻshasiz;</li>
    <li>qaytarmasdan olishda har qadamda maxrajni kamaytirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Probability</span>
  <span class="pe-chip pe-chip--o">P</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">favourable outcomes</span>
  <span class="pe-op">÷</span>
  <span class="pe-chip pe-chip--v">all outcomes</span>
</div>

<h3>Qaytarmasdan olish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 qizil, 5 koʻk shar; ikkitasi qaytarmasdan olinadi</span>
    <span class="pm-solve__why">Ikkalasi qizil boʻlish ehtimoli</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Birinchisi qizil: 3/8; keyin 7 ta shar, 2 tasi qizil: 2/7</span>
    <span class="pm-solve__why">Olingan shar qaytarilmaydi — ikkinchi qadamda maxraj kamaydi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3/8 × 2/7 = 6/56 = 3/28</span>
    <span class="pm-solve__why">Ketma-ket hodisalar koʻpaytiriladi</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Without replacement» — olingan narsa qaytarilmaydi, shuning uchun ikkinchi qadamda
  ham qulay, ham jami bittaga kamayadi. «With replacement» desa — har safar bir xil: 3/8 × 3/8.
  GMAT ikkala javobni ham variantlarga qoʻyadi.
</div>

<h3>Kamida bittasi — teskari hodisa</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 marta tanga — kamida bitta «gerb»</span>
    <span class="pm-solve__why">Toʻgʻridan-toʻgʻri: 1, 2 yoki 3 ta gerb — uchta holat</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Hech bir gerb yoʻq: 1/2 × 1/2 × 1/2 = 1/8</span>
    <span class="pm-solve__why">Teskarisi bitta holat — uni hisoblash oson</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">1 − 1/8 = 7/8</span>
    <span class="pm-solve__why">Kamida bittasi = 1 − hech biri</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  «At least one» soʻzini koʻrsangiz — avtomatik ravishda teskari hodisaga oʻting. Ehtimollarni
  qoʻshish (1/2 + 1/2 + 1/2 = 3/2) bir zumda 1 dan oshib ketadi — bu notoʻgʻri yoʻl ekanining
  eng aniq belgisi.
</div>

<h3>Koʻpaytirish yoki qoʻshish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">P(A) = 0.6, P(B) = 0.5, mustaqil</span>
    <span class="pm-solve__why">Bir-biriga taʼsir qilmaydi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Ikkalasi: 0.6 × 0.5 = 0.3</span>
    <span class="pm-solve__why">«Va» — koʻpaytirish</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Kamida bittasi: 1 − 0.4 × 0.5 = 0.8</span>
    <span class="pm-solve__why">0.6 + 0.5 = 1.1 — imkonsiz, chunki ikkalasi birga ham roʻy beradi</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qoʻshish faqat hodisalar <b>bir vaqtda roʻy bera olmasa</b> ishlaydi: zarda 1 yoki 2 chiqishi
  — 1/6 + 1/6. Ikki xil sotuvchining savdo qilishi esa bir vaqtda boʻlishi mumkin — ularni
  qoʻshib boʻlmaydi, teskari hodisa orqali hisoblang.
</div>

<h3>Ehtimollik va kombinatorika — ikki yoʻl, bir javob</h3>

<p>Qaytarmasdan olishni kombinatsiyalar bilan ham hisoblash mumkin. 3 qizil va 5 koʻk shardan
2 tasini olishning jami C(8, 2) = 28 usuli bor; ikkalasi qizil boʻladigan usullar C(3, 2) = 3.
Ehtimollik 3/28 — ketma-ket koʻpaytirish bilan aynan bir xil natija. Qaysi yoʻl qulayroq boʻlsa,
oʻshani tanlang; ikkinchisi tekshiruv boʻlib xizmat qiladi. «Aynan bittasi nuqsonli» kabi
savollarda kombinatsiya yoʻli ayniqsa qulay, chunki tartibni alohida oʻylash shart emas: 2 ta nuqsonli va 8 ta yaroqli chipdan 2 tasini olsak, mos juftlar 2 × 8 = 16, jami C(10, 2) = 45, yaʼni 16/45.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Biznesda ehtimollik koʻpincha foiz bilan beriladi: «30% of visitors add an item, and 40% of
  those buy» — bu ketma-ket hodisa: 0.3 × 0.4 = 12%. «Of those» soʻzi ikkinchi foiz birinchi
  guruhdan olinishini bildiradi — bu GMAT-5 dagi «foizning foizi» bilan aynan bir xil.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>at random</b><span>tasodifiy ravishda</span></li>
  <li><b>without replacement</b><span>qaytarmasdan</span></li>
  <li><b>at least one</b><span>kamida bittasi — 1 − hech biri</span></li>
  <li><b>independent events</b><span>mustaqil hodisalar — koʻpaytiriladi</span></li>
  <li><b>mutually exclusive</b><span>bir-birini istisno qiladi — qoʻshiladi</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>A bag contains 3 red balls and 5 blue balls. If two balls are drawn at random without
    replacement, what is the probability that both are red?</p>
  </div>
  <ol class="ps-ch">
    <li>3/64</li>
    <li>3/28</li>
    <li>9/64</li>
    <li>3/16</li>
    <li>3/8</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 3/28</p>
      <p>3/8 × 2/7 = 3/28.</p>
      <p><b>9/64</b> — sharni qaytarib olgan deb hisoblangan javob (3/8 × 3/8).</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">9/64</span>
  <span class="ps-trap__why">«Without replacement» eʼtiborsiz qoldirilgan. Ikkinchi olishda shar ham,
  qizil shar ham bittaga kam.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>A fair coin is tossed 3 times. What is the probability of getting at least one head?</p>
  </div>
  <ol class="ps-ch">
    <li>1/8</li>
    <li>3/8</li>
    <li>1/2</li>
    <li>3/4</li>
    <li>7/8</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: E) 7/8</p>
      <p>1 − (1/2)<sup>3</sup> = 7/8.</p>
      <p><b>3/8</b> — aynan bitta gerb chiqish ehtimoli; «at least» ikki va uch gerbni ham oʻz ichiga oladi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">3/8</span>
  <span class="ps-trap__why">«Exactly one» va «at least one» — har xil savol.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Ehtimollik javobini <b>mantiq bilan</b> tekshiring:</p>
  <ol>
    <li>javob har doim 0 va 1 orasida;</li>
    <li>«ikkalasi ham» har bir alohida ehtimoldan kichik;</li>
    <li>«kamida bittasi» har bir alohida ehtimoldan katta.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">P(at least one 6 in two rolls) = 1/6 + 1/6 = 1/3</p>
  <p class="pe-good">1 − (5/6)<sup>2</sup> = 11/36</p>
  <p class="pe-fix__why">Ikkala zarda ham 6 chiqishi ikki marta sanaldi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Two without replacement: 3/8 × 3/8</p>
  <p class="pe-good">3/8 × 2/7</p>
  <p class="pe-fix__why">Ikkinchi olishda jami ham, qulay ham kamayadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> What is the probability of rolling a number
  greater than 4 on a fair die?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">1/3 — 5 yoki 6: 2/6.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> Two fair dice are rolled. What is the
  probability that the sum is 7?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">1/6 — 36 natijadan 6 tasi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> The probability of rain is 0.3. What is the
  probability of no rain?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">0.7 — 1 − 0.3.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> Independent events A and B have probabilities
  0.5 and 0.4. What is the probability that both occur?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">0.2 — 0.5 × 0.4.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> 20% of invoices contain an error. Two are
  checked independently. What is the probability that neither contains an error?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">0.64 — 0.8 × 0.8.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>probability</b><span>ehtimollik</span></li>
  <li><b>outcome</b><span>natija</span></li>
  <li><b>event</b><span>hodisa</span></li>
  <li><b>independent</b><span>mustaqil</span></li>
  <li><b>mutually exclusive</b><span>bir-birini istisno qiluvchi</span></li>
  <li><b>complement</b><span>teskari hodisa</span></li>
  <li><b>at random</b><span>tasodifiy</span></li>
  <li><b>fair coin / fair die</b><span>toʻgʻri tanga / toʻgʻri zar</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Ehtimollik = qulay ÷ jami; har doim 0 dan 1 gacha.</li>
    <li>Kamida bittasi = 1 − hech biri.</li>
    <li>Mustaqil hodisalar — koʻpaytiriladi; bir vaqtda boʻlolmaydiganlar — qoʻshiladi.</li>
    <li>Qaytarmasdan olishda har qadamda maxraj (va qulay) kamayadi.</li>
    <li>«Exactly one» ≠ «at least one».</li>
  </ul>
</div>
"""

GMAT24 = """
<h2>GMAT-24: Statistics — Median, Range and Standard Deviation</h2>

<p>Statistika savollari kam hisob, koʻp tushuncha talab qiladi. GMAT oʻrtacha, mediana,
moda va oraliqni hisoblashni soʻraydi, lekin standart chetlanishni (<i>standard deviation</i>)
deyarli hech qachon formula bilan hisoblatmaydi — u <mark>tarqoqlikni his qilishni</mark>
tekshiradi: qaysi toʻplam koʻproq yoyilgan, son qoʻshilsa nima oʻzgaradi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>mediana, moda va oraliqni toʻgʻri topasiz — avval tartiblab;</li>
    <li>juft sonli toʻplamda medianani ikki oʻrta sonning oʻrtachasi deb olasiz;</li>
    <li>standart chetlanishni hisoblamasdan solishtirasiz;</li>
    <li>barcha qiymatlarga son qoʻshilsa yoki koʻpaytirilsa, nima oʻzgarishini bilasiz.</li>
  </ul>
</div>

<h3>Mediana — avval tartiblang</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">11, 2, 9, 5, 14, 6 — mediana?</span>
    <span class="pm-solve__why">Yozilgan tartibda oʻrtadagilar (9 va 5) — xato yoʻl</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2, 5, 6, 9, 11, 14</span>
    <span class="pm-solve__why">Avval oʻsish tartibida yozamiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">(6 + 9) ÷ 2 = 7.5</span>
    <span class="pm-solve__why">Juft sonli toʻplam — ikki oʻrta sonning oʻrtachasi</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Mediana — tartiblangan qatorning <b>oʻrtasi</b>, oʻrtacha esa — yigʻindi ÷ soni. Bitta juda
  katta son (masalan, direktorning maoshi) oʻrtachani yuqoriga tortadi, medianani esa deyarli
  qimirlatmaydi. Shuning uchun «typical» (odatiy) qiymat soʻralsa, koʻpincha mediana toʻgʻriroq.
</div>

<h3>Moda va oraliq</h3>

<p><b>Moda</b> (<i>mode</i>) — eng koʻp takrorlanadigan qiymat: 3, 5, 5, 8, 9, 9, 9 da moda 9.
<b>Oraliq</b> (<i>range</i>) — eng katta minus eng kichik: 4, 17, 9, 23, 11 da 23 − 4 = 19. Oraliq
faqat ikki chetga qaraydi, shuning uchun bitta gʻayrioddiy qiymat uni keskin oʻzgartiradi.</p>

<h3>Standart chetlanish — hisoblamasdan</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">{10, 10, 10, 10} va {1, 10, 19, 10}</span>
    <span class="pm-solve__why">Ikkalasining oʻrtachasi 10</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Birinchisida hamma qiymat oʻrtachada — chetlanish 0</span>
    <span class="pm-solve__why">Standart chetlanish — qiymatlarning oʻrtachadan tipik uzoqligi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Ikkinchisida 1 va 19 — 9 birlik uzoqda → katta chetlanish</span>
    <span class="pm-solve__why">Qiymatlar oʻrtachadan qancha uzoq — chetlanish shuncha katta</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Ikki qoida: barcha qiymatlarga <b>bir xil son qoʻshilsa</b>, standart chetlanish va oraliq
  oʻzgarmaydi (hamma birga suriladi); barcha qiymatlar <b>3 ga koʻpaytirilsa</b>, chetlanish va
  oraliq ham 3 baravar oshadi. Oʻrtacha va mediana esa ikkala holatda ham oʻzgaradi.
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">{10, 20, 30} ga 20 qoʻshiladi</span>
    <span class="pm-solve__why">20 — oʻrtachaga teng qiymat</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Oʻrtacha 20, mediana 20, oraliq 20 — oʻzgarmaydi; chetlanish kamayadi</span>
    <span class="pm-solve__why">Oʻrtachadagi yangi qiymat «tipik uzoqlikni» kichraytiradi</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Katta sonlar katta chetlanish degani emas: {100, 101, 102} ning chetlanishi {1, 10, 19}
  nikidan ancha kichik. Sonlarning <b>kattaligiga</b> emas, ularning bir-biridan <b>qanchalik
  uzoqligiga</b> qarang.
</div>

<p>Standart chetlanish haqida yana uchta fakt. U <b>hech qachon manfiy</b> boʻlmaydi. U
<b>nolga</b> faqat barcha qiymatlar bir xil boʻlganda teng: {7, 7, 7}. Va u oʻrtachadan uzoq
qiymatga juda sezgir: {1, 10, 19} toʻplamiga 100 soni qoʻshilsa, chetlanish keskin oshadi,
mediana esa 10 dan atigi 14.5 ga siljiydi.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbek darsliklarida mediana baʼzan «oʻrta qiymat», standart chetlanish esa «oʻrtacha
  kvadratik chetlanish» deb ataladi. GMAT'da formula kerak emas — faqat qaysi toʻplam koʻproq
  yoyilganini koʻrish va qiymatlar oʻzgarganda chetlanish nima boʻlishini aytish kifoya.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>median</b><span>mediana — tartiblangan qatorning oʻrtasi</span></li>
  <li><b>mode</b><span>moda — eng koʻp uchraydigan qiymat</span></li>
  <li><b>range</b><span>oraliq — eng katta minus eng kichik</span></li>
  <li><b>standard deviation</b><span>standart chetlanish — tarqoqlik oʻlchovi</span></li>
  <li><b>data set</b><span>maʼlumotlar toʻplami</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>What is the median of the data set 11, 2, 9, 5, 14, 6?</p>
  </div>
  <ol class="ps-ch">
    <li>6</li>
    <li>7</li>
    <li>7.5</li>
    <li>9</li>
    <li>12</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 7.5</p>
      <p>Tartiblangan: 2, 5, 6, 9, 11, 14; (6 + 9) ÷ 2.</p>
      <p><b>7</b> — tartiblamasdan oʻrtadagi 9 va 5 ni olgan javob.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">7</span>
  <span class="ps-trap__why">Mediana faqat <b>tartiblangan</b> qatorda maʼnoga ega.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>Which of the following data sets has the greatest standard deviation?</p>
  </div>
  <ol class="ps-ch">
    <li>10, 10, 10, 10</li>
    <li>9, 10, 11, 10</li>
    <li>1, 10, 19, 10</li>
    <li>5, 10, 15, 10</li>
    <li>100, 101, 102, 101</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 1, 10, 19, 10</p>
      <p>Hamma toʻplamda qiymatlar oʻrtacha atrofida; 1 va 19 oʻrtachadan eng uzoqda (9 birlik).</p>
      <p><b>100, 101, 102, 101</b> — sonlar katta, lekin bir-biriga juda yaqin.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">100, 101, 102, 101</span>
  <span class="ps-trap__why">Katta sonlar — katta chetlanish emas. Bu toʻplam 9, 10, 11, 10 ning
  91 ga surilgani, chetlanishi aynan bir xil.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Statistika savolida <b>birinchi harakat — tartiblash</b>:</p>
  <ol>
    <li>qiymatlarni oʻsish tartibida qayta yozing;</li>
    <li>mediana, oraliq va moda shu qatordan bir qarashda chiqadi;</li>
    <li>chetlanish savolida oʻrtachani toping va qiymatlarning undan uzoqligini solishtiring.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">Median of 7, 3, 9, 1 = (3 + 9) ÷ 2 = 6</p>
  <p class="pe-good">1, 3, 7, 9 → (3 + 7) ÷ 2 = 5</p>
  <p class="pe-fix__why">Avval tartiblash kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Every value + 10 → standard deviation + 10</p>
  <p class="pe-good">Standard deviation unchanged</p>
  <p class="pe-fix__why">Hamma qiymat birga surilsa, ularning bir-biridan uzoqligi oʻzgarmaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> What is the range of 4, 17, 9, 23, 11?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">19 — 23 − 4.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> What is the mode of 3, 5, 5, 8, 9, 9, 9?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">9 — uch marta uchraydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> What is the median of 2, 8, 5, 11, 7?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">7 — 2, 5, 7, 8, 11.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> If 10 is added to every value in a data set, by
  how much does the standard deviation change?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">0 — hamma qiymat birga suriladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> Five salaries are $3,000, $3,200, $3,500, $4,000
  and $15,000. What is the median salary?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">$3,500 — oʻrtacha esa $5,740: bitta katta maosh uni tortib ketgan.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>mean</b><span>oʻrtacha</span></li>
  <li><b>median</b><span>mediana</span></li>
  <li><b>mode</b><span>moda</span></li>
  <li><b>range</b><span>oraliq</span></li>
  <li><b>standard deviation</b><span>standart chetlanish</span></li>
  <li><b>spread</b><span>tarqoqlik</span></li>
  <li><b>outlier</b><span>gʻayrioddiy (chetdagi) qiymat</span></li>
  <li><b>data set</b><span>maʼlumotlar toʻplami</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Mediana — avval tartiblang; juft sonda ikki oʻrta sonning oʻrtachasi.</li>
    <li>Oraliq = eng katta − eng kichik; moda — eng koʻp uchraydigani.</li>
    <li>Chetlanish — oʻrtachadan tipik uzoqlik; hisoblamasdan solishtiring.</li>
    <li>Hammaga son qoʻshilsa — chetlanish oʻzgarmaydi; koʻpaytirilsa — shuncha marta oʻzgaradi.</li>
    <li>Bitta katta qiymat oʻrtachani tortadi, medianani deyarli yoʻq.</li>
  </ul>
</div>
"""

GMAT25 = """
<h2>GMAT-25: Strategy — Pacing, Guessing and Question Review &amp; Edit</h2>

<p>Bu — Quant blokining oxirgi darsi, va unda yangi matematika yoʻq. Yigirma toʻrt darsda
oʻrgangan narsalaringiz 45 daqiqalik bitta boʻlimda ishlashi uchun <mark>vaqtni boshqarish</mark>
kerak. Koʻp nomzod bilmagani uchun emas, vaqt yetmagani uchun ball yoʻqotadi. Bu dars —
21 savol va 45 daqiqa uchun reja.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>boʻlim davomida vaqtni nazorat nuqtalari bilan tekshirasiz;</li>
    <li>qachon taxmin qilib, keyingi savolga oʻtishni bilasiz;</li>
    <li>belgilash (<i>bookmark</i>) va Question Review &amp; Edit imkoniyatidan toʻgʻri foydalanasiz;</li>
    <li>javoblardan orqaga yechish va qulay son tanlash usullarini qoʻllaysiz.</li>
  </ul>
</div>

<h3>Vaqt rejasi — nazorat nuqtalari</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">45 daqiqa ÷ 21 savol ≈ 2 daqiqa 8 soniya</span>
    <span class="pm-solve__why">Bir savolga oʻrtacha vaqt</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">15-daqiqa — 7-savol; 30-daqiqa — 14-savol</span>
    <span class="pm-solve__why">Boʻlimni uchga boʻlamiz: har uchdan birida 7 ta savol</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Ortda qolsangiz — keyingi qiyin savolda tezroq taxmin qiling</span>
    <span class="pm-solve__why">Vaqtni bitta joyda emas, bir necha savolda asta-sekin qaytaring</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Eng qimmat xato — bitta savolga 6–7 daqiqa berish. Bu uchta savolning vaqti. Va oxirida
  javobsiz qolgan savollar ballni tushiradi — GMAT boʻlimni tugatmaganlarni jazolaydi.
  Shuning uchun qoida qatʼiy: <b>hech qachon javobsiz qoldirmang</b>, vaqt tugayotgan boʻlsa,
  qolgan savollarni taxmin bilan belgilang.
</div>

<h3>Taxmin qilish — aqlli taxmin</h3>

<p>Beshta variantdan koʻr-koʻrona taxmin — 1/5, yaʼni 20% imkoniyat. Ikkitasini chiqarib
tashlasangiz — 1/3, uchtasini — 1/2. Koʻp variantni bir qarashda yoʻq qilish mumkin: javob
manfiy boʻlishi mumkin emas; ehtimollik 1 dan oshmaydi; birgalikdagi ish vaqti eng tez
ishchinikidan kam; tortilgan oʻrtacha ikki oʻrtacha orasida. Bular — oldingi darslardagi
«mantiqiy tekshiruvlar», endi ular taxmin quroli.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">5 variant, koʻr-koʻrona taxmin: 1/5 = 20%</span>
    <span class="pm-solve__why">Hech narsa bilmasangiz ham — boʻsh joydan yaxshi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2 tasi chiqarib tashlandi: 1/3 ≈ 33%</span>
    <span class="pm-solve__why">Mantiqiy tekshiruvlar bilan (manfiy emas, 1 dan oshmaydi…)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3 tasi chiqarib tashlandi: 1/2 = 50%</span>
    <span class="pm-solve__why">Har bir chiqarilgan variant imkoniyatni oshiradi</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  «Ikki daqiqa qoidasi»: savolga 2 daqiqa qarab, yechimga yoʻl koʻrinmasa — variantlarni
  chiqarib tashlang, eng ehtimoliysini belgilang, savolni <b>bookmark</b> qiling va davom eting.
  Oxirida vaqt qolsa, qaytasiz.
</div>

<h3>Question Review &amp; Edit</h3>

<p>GMAT Focus'da boʻlim davomida savollarni belgilab qoʻyish mumkin, va oxirgi savoldan keyin
vaqt qolsa, belgilangan savollarga qaytib, boʻlim boʻyicha <b>koʻpi bilan 3 ta</b> javobni
oʻzgartirish mumkin. Bu — xavfsizlik tarmogʻi, reja emas: unga vaqt qolishi uchun asosiy
qism rejaga muvofiq oʻtishi kerak.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Javobni oʻzgartirishdan oldin oʻzingizdan soʻrang: <b>yangi dalil topdimmi</b> yoki shunchaki
  shubha qilyapmanmi? Faqat aniq xatoni (hisobdagi slip, notoʻgʻri oʻqilgan soʻz) topgan
  boʻlsangiz, oʻzgartiring. Uchta tahrir — oz; ularni eng ishonchli tuzatishlarga saqlang.
</div>

<h3>Javoblardan orqaga yechish va qulay son</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">«(n + 18) ÷ 4 = n − 3», variantlar: 6, 8, 10, 12, 14</span>
    <span class="pm-solve__why">Variantlar oʻsish tartibida — oʻrtadagisidan boshlang</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">n = 10: (10 + 18) ÷ 4 = 7 = 10 − 3 ✓</span>
    <span class="pm-solve__why">Birinchi urinishda topildi; kichik chiqsa — kattaroqni, katta chiqsa — kichikroqni sinang</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">«x — y ning 25%, y — z ning 40%»: z = 100 deb oling</span>
    <span class="pm-solve__why">y = 40, x = 10 → x — z ning 10% i. Foiz savolida 100 eng qulay son</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Boʻlimlar tartibini <b>oʻzingiz tanlaysiz</b> (Quant, Verbal va Data Insights — istalgan
  tartibda), va ular orasida bitta ixtiyoriy 10 daqiqalik tanaffus bor. Koʻpchilikka eng kuchli
  boʻlimdan boshlash ishonch beradi — bizning nomzodlar uchun bu koʻpincha Quant. Sinov
  imtihonlarida ikki xil tartibni sinab koʻring va qaysi birida natija yaxshi ekanini yozib boring.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>bookmark</b><span>keyinroq qaytish uchun belgilash</span></li>
  <li><b>Question Review &amp; Edit</b><span>savollarni koʻrib chiqish va tahrirlash — boʻlimga 3 ta</span></li>
  <li><b>time remaining</b><span>qolgan vaqt</span></li>
  <li><b>which of the following could be</b><span>qaysi biri boʻlishi mumkin — variantlarni sinang</span></li>
  <li><b>in terms of</b><span>… orqali — qulay son qoʻyish uchun yaxshi savol</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>When 18 is added to a number and the result is divided by 4, the answer is 3 less than
    the number. What is the number?</p>
  </div>
  <ol class="ps-ch">
    <li>6</li>
    <li>8</li>
    <li>10</li>
    <li>12</li>
    <li>14</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 10</p>
      <p>Orqaga yechish: 10 + 18 = 28, 28 ÷ 4 = 7, va 7 = 10 − 3 ✓. Tenglama bilan:
      <i>n</i> + 18 = 4<i>n</i> − 12 → <i>n</i> = 10.</p>
      <p><b>6</b> — (6 + 18) ÷ 4 = 6 chiqqani uchun tanlangan javob; natija sonning oʻzidan 3 kam boʻlishi kerak edi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">6</span>
  <span class="ps-trap__why">Orqaga yechishda shartning <b>hammasini</b> tekshiring — «3 less than the
  number» qismi ham.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>If <i>x</i> is 25% of <i>y</i> and <i>y</i> is 40% of <i>z</i>, then <i>x</i> is what percent of <i>z</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>10%</li>
    <li>15%</li>
    <li>25%</li>
    <li>40%</li>
    <li>65%</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 10%</p>
      <p><i>z</i> = 100: <i>y</i> = 40, <i>x</i> = 10.</p>
      <p><b>65%</b> — foizlarni qoʻshgan javob; «of» koʻpaytirishni bildiradi: 0.25 × 0.4.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">65%</span>
  <span class="ps-trap__why">Foizning foizi koʻpaytiriladi. Qulay son (100) bu xatoni bir zumda koʻrsatadi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Boʻlim boshida <b>uchta raqamni</b> qogʻozga yozing:</p>
  <ol>
    <li>15 — 7-savolgacha, 30 — 14-savolgacha, 45 — oxiri;</li>
    <li>har nazorat nuqtasida taymerga qarang: ortdami, oldindami;</li>
    <li>oxirgi 3 daqiqada qolgan har bir savolga javob belgilang — boʻsh joy qoldirmang.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">Spend 7 minutes on question 6 because «I almost have it»</p>
  <p class="pe-good">Guess after about 2–3 minutes, bookmark, move on</p>
  <p class="pe-fix__why">Bitta savolga ketgan 7 daqiqa — uchta oson savolning vaqti.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Leave the last 4 questions blank</p>
  <p class="pe-good">Mark an answer for every question, even a blind guess</p>
  <p class="pe-fix__why">Javobsiz savol ballni tushiradi; taxminda kamida 20% imkoniyat bor.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> With five answer choices, what is the chance
  that a blind guess is right?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">20% — 1/5.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> After you eliminate three of the five choices,
  what is the chance that a guess is right?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">50% — ikkitadan bittasi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> How many answers can you change per section in
  Question Review &amp; Edit?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">3 tagacha.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> About how many questions should you have finished
  after 30 minutes?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">14 — boʻlimning uchdan ikkisi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> A price rises by 25%. By what percent must it fall
  to return to the original price? (Use 100.)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">20% — 100 → 125 → 100: 25 ÷ 125.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>pacing</b><span>vaqtni taqsimlash</span></li>
  <li><b>checkpoint</b><span>nazorat nuqtasi</span></li>
  <li><b>educated guess</b><span>aqlli taxmin</span></li>
  <li><b>eliminate</b><span>chiqarib tashlamoq</span></li>
  <li><b>bookmark</b><span>belgilab qoʻymoq</span></li>
  <li><b>backsolve</b><span>javoblardan orqaga yechmoq</span></li>
  <li><b>pick numbers</b><span>qulay son qoʻymoq</span></li>
  <li><b>timer</b><span>taymer</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>21 savol, 45 daqiqa: 7-savol — 15-daqiqada, 14-savol — 30-daqiqada.</li>
    <li>Ikki-uch daqiqada yoʻl koʻrinmasa — chiqarib tashlang, taxmin qiling, belgilang.</li>
    <li>Hech qachon javobsiz qoldirmang.</li>
    <li>Question Review &amp; Edit — boʻlimga 3 ta tahrir; faqat aniq xatoni tuzating.</li>
    <li>Variantlardan orqaga yeching (oʻrtadagisidan); foizda 100 ni qoʻying.</li>
  </ul>
</div>
"""

TUTORIALS = [
    {
        "title": "GMAT-21: Sequences and Series",
        "category": "math", "order": 21,
        "summary": "Arifmetik va geometrik ketma-ketlik, n-had, hadlar sonini sanash, yigʻindi va rekursiv qoidalar.",
        "stories": ["Two Salary Offers"],
        "content": GMAT21,
    },
    {
        "title": "GMAT-22: Counting — Permutations and Combinations",
        "category": "math", "order": 22,
        "summary": "Koʻpaytirish qoidasi, tartib muhim boʻlgan va boʻlmagan tanlovlar, takrorlanuvchi harflar va «birga» sharti.",
        "stories": ["How Many Lunches?"],
        "content": GMAT22,
    },
    {
        "title": "GMAT-23: Probability",
        "category": "math", "order": 23,
        "summary": "Qulay ÷ jami, «kamida bittasi» uchun teskari hodisa, mustaqil hodisalar va qaytarmasdan olish.",
        "stories": ["The Two Alarms"],
        "content": GMAT23,
    },
    {
        "title": "GMAT-24: Statistics — Median, Range and Standard Deviation",
        "category": "math", "order": 24,
        "summary": "Mediana, moda, oraliq, standart chetlanishni hisoblamasdan solishtirish va qiymatlar oʻzgarganda nima boʻlishi.",
        "stories": ["The Average Salary"],
        "content": GMAT24,
    },
    {
        "title": "GMAT-25: Strategy — Pacing, Guessing and Question Review & Edit",
        "category": "math", "order": 25,
        "summary": "45 daqiqa va 21 savol uchun vaqt rejasi, aqlli taxmin, belgilash va 3 ta tahrir, orqaga yechish va qulay son.",
        "stories": ["Twenty-One Questions, Forty-Five Minutes"],
        "content": GMAT25,
    },
]
