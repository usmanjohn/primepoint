# -*- coding: utf-8 -*-
"""Prime GMAT — GMAT-11 … GMAT-15: the word-problem block, part one — averages,
mixtures, rates and work, profit and discount, simple and compound interest.

Written with STYLE_GUIDE_PRIME_GMAT.md (on top of STYLE_GUIDE_PRIME_SAT.md) ·
lesson list in toc_prime_gmat.txt. Exam English in the stems, Uzbek for the teaching.
Five answer choices, no calculator, no geometry, no data sufficiency.

Import:
    python manage.py import_tutorials tutorial/management/commands/_tutorials_prime_gmat_11_15.py --author=prime
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

GMAT11 = """
<h2>GMAT-11: Averages and Weighted Averages</h2>

<p>Oʻrtacha qiymat — GMAT matnli masalalarining eng koʻp uchraydigan mavzusi. Lekin
deyarli hech bir savol «oʻrtachani toping» deb soʻramaydi. U <mark>yigʻindi bilan
ishlashni</mark> soʻraydi: bir son qoʻshilsa yoki olib tashlansa nima boʻladi, ikki guruh
birlashsa umumiy oʻrtacha qayerga tushadi. Shu darsning kaliti bitta qayta yozish:
oʻrtacha × soni = yigʻindi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>oʻrtachadan yigʻindiga va yigʻindidan oʻrtachaga bir qadamda oʻtasiz;</li>
    <li>son qoʻshilgan yoki olib tashlangan masalani yigʻindilar farqi bilan yechasiz;</li>
    <li>ikki guruhning tortilgan oʻrtachasini (<i>weighted average</i>) hisoblaysiz;</li>
    <li>teng oraliqli sonlarning oʻrtachasini birinchi va oxirgisidan topasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Average</span>
  <span class="pe-chip pe-chip--o">sum</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">average</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--v">number of values</span>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻrtacha bilan toʻgʻridan-toʻgʻri hisoblash qiyin, yigʻindi bilan — oson. Shuning uchun
  har bir oʻrtachani darrov <b>yigʻindiga aylantiring</b>: «5 ta sonning oʻrtachasi 80» —
  demak yigʻindi 400. Keyingi barcha qadamlar yigʻindilar ustida bajariladi.
</div>

<h3>Son qoʻshilsa yoki olib tashlansa</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">5 ta son, oʻrtacha 80 → yigʻindi 400</span>
    <span class="pm-solve__why">Oʻrtachani yigʻindiga aylantirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">6 ta son, oʻrtacha 82 → yigʻindi 492</span>
    <span class="pm-solve__why">Yangi holat ham yigʻindiga</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Oltinchi son = 492 − 400 = 92</span>
    <span class="pm-solve__why">Ikki yigʻindining farqi — qoʻshilgan son</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Tez tekshiruv: oltinchi son oʻrtachani 2 ga koʻtardi, demak u eski 5 ta songa 2 tadan
  «ulashib» bergan (5 × 2 = 10) va oʻzi ham yangi oʻrtachaga teng boʻlib qolgan: 82 + 10 = 92 ✓.
</div>

<h3>Tortilgan oʻrtacha — ikki guruhni birlashtirish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">20 xodim — $3,000; 30 xodim — $4,000</span>
    <span class="pm-solve__why">Guruhlar teng emas</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">20 × 3,000 + 30 × 4,000 = 60,000 + 120,000 = 180,000</span>
    <span class="pm-solve__why">Har bir guruhning yigʻindisi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">180,000 ÷ 50 = $3,600</span>
    <span class="pm-solve__why">Umumiy yigʻindi ÷ umumiy son</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikki oʻrtachaning oddiy oʻrtachasi ($3,500) — faqat guruhlar <b>teng</b> boʻlganda toʻgʻri.
  Umumiy oʻrtacha har doim <b>kattaroq guruh tomonga</b> siljiydi: bu yerda 30 kishilik
  guruh $4,000 ga yaqin, shuning uchun javob $3,500 dan katta boʻlishi kerak.
</div>

<h3>Teng oraliqli sonlar</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">20, 21, 22, …, 40 — oʻrtachasi?</span>
    <span class="pm-solve__why">Sonlar bir xil qadam bilan oʻsadi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">(20 + 40) ÷ 2 = 30</span>
    <span class="pm-solve__why">Birinchi va oxirgisining oʻrtachasi — butun toʻplamning oʻrtachasi</span>
  </div>
</div>

<p>Bu qoida faqat <b>teng oraliqli</b> (<i>evenly spaced</i>) toʻplamlar uchun ishlaydi:
ketma-ket sonlar, ketma-ket juft sonlar, 5 ning karralilari. Bunday toʻplamda oʻrtacha va
mediana bir xil boʻladi. Masalan, 5, 10, 15, 20, 25 ning oʻrtachasi (5 + 25) ÷ 2 = 15 — oʻrtadagi son bilan bir xil.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻrtacha tezlik ham tortilgan oʻrtacha, lekin vaqt boʻyicha tortilgan. Bir xil masofani
  60 km/soat bilan borib, 40 km/soat bilan qaytsangiz, oʻrtacha tezlik 50 emas, <b>48</b>:
  sekin yoʻlda koʻproq vaqt oʻtadi. Buni GMAT-13 da batafsil koʻramiz.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>average (arithmetic mean)</b><span>oʻrtacha arifmetik qiymat</span></li>
  <li><b>the average of the remaining numbers</b><span>qolgan sonlarning oʻrtachasi</span></li>
  <li><b>weighted average</b><span>tortilgan oʻrtacha — guruh hajmi hisobga olinadi</span></li>
  <li><b>raise the average to</b><span>oʻrtachani … gacha koʻtarmoq</span></li>
  <li><b>evenly spaced</b><span>teng oraliqli</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>The average (arithmetic mean) of five numbers is 80. When a sixth number is added,
    the average of the six numbers is 82. What is the sixth number?</p>
  </div>
  <ol class="ps-ch">
    <li>82</li>
    <li>84</li>
    <li>90</li>
    <li>92</li>
    <li>94</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: D) 92</p>
      <p>6 × 82 − 5 × 80 = 492 − 400 = 92.</p>
      <p><b>82</b> — yangi oʻrtachaning oʻzi. Oʻrtachani 2 ga koʻtarish uchun yangi son
      oʻrtachadan ancha katta boʻlishi kerak.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">82</span>
  <span class="ps-trap__why">Oʻrtachaga teng son qoʻshilsa, oʻrtacha oʻzgarmaydi. Oʻrtachani
  koʻtargan son undan kattaroq boʻlishi shart.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>At a company, 20 employees earn an average monthly salary of $3,000 and 30 other
    employees earn an average monthly salary of $4,000. What is the average monthly salary
    of all 50 employees?</p>
  </div>
  <ol class="ps-ch">
    <li>$3,400</li>
    <li>$3,500</li>
    <li>$3,600</li>
    <li>$3,700</li>
    <li>$3,800</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) $3,600</p>
      <p>(60,000 + 120,000) ÷ 50 = 3,600.</p>
      <p><b>$3,500</b> — ikki oʻrtachaning oddiy oʻrtachasi; guruhlar teng emas.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">$3,500</span>
  <span class="ps-trap__why">Oʻrtachalarni oʻrtachalash. Guruhlar hajmi har xil boʻlsa,
  har birining yigʻindisini toping.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Tortilgan oʻrtachada <b>javob qayerda boʻlishini</b> oldindan biling:</p>
  <ol>
    <li>u har doim ikki guruh oʻrtachasi orasida;</li>
    <li>kattaroq guruh tomonga yaqinroq;</li>
    <li>guruhlar 2 : 3 boʻlsa, javob oraliqni 3 : 2 nisbatda boʻladi — 3,000 dan 600 yuqori, 4,000 dan 400 past.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">Average of 3,000 (20 people) and 4,000 (30 people) = 3,500</p>
  <p class="pe-good">(20 × 3,000 + 30 × 4,000) ÷ 50 = 3,600</p>
  <p class="pe-fix__why">Guruh hajmlari oʻrtachaga taʼsir qiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Each of 10 numbers rises by 5, so the average rises by 50</p>
  <p class="pe-good">The average rises by 5</p>
  <p class="pe-fix__why">Yigʻindi 50 ga oshadi, lekin 10 ta songa boʻlinadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> What is the average of 12, 15, 18 and 23?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">17 — yigʻindi 68, 4 ga boʻlamiz.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> The average of four numbers is 25. What is their sum?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">100 — 4 × 25.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> What is the average of the integers from 20 to 40, inclusive?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">30 — (20 + 40) ÷ 2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> The average of three numbers is 10. A fourth
  number, 30, is added. What is the new average?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">15 — (30 + 30) ÷ 4.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> A shop made 40 sales of $50 and 10 sales of
  $100. What was the average sale?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">$60 — (2,000 + 1,000) ÷ 50.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>average / arithmetic mean</b><span>oʻrtacha arifmetik</span></li>
  <li><b>sum</b><span>yigʻindi</span></li>
  <li><b>weighted average</b><span>tortilgan oʻrtacha</span></li>
  <li><b>median</b><span>mediana — oʻrtadagi qiymat</span></li>
  <li><b>evenly spaced</b><span>teng oraliqli</span></li>
  <li><b>consecutive</b><span>ketma-ket</span></li>
  <li><b>salary</b><span>maosh</span></li>
  <li><b>remaining</b><span>qolgan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Yigʻindi = oʻrtacha × soni — har bir oʻrtachani darrov yigʻindiga aylantiring.</li>
    <li>Qoʻshilgan yoki olib tashlangan son = ikki yigʻindining farqi.</li>
    <li>Tortilgan oʻrtacha kattaroq guruh tomonga siljiydi.</li>
    <li>Teng oraliqli toʻplamda oʻrtacha = (birinchi + oxirgi) ÷ 2.</li>
    <li>Har bir songa 5 qoʻshilsa, oʻrtacha ham 5 ga oshadi.</li>
  </ul>
</div>
"""

GMAT12 = """
<h2>GMAT-12: Mixtures and Concentrations</h2>

<p>Aralashma masalalari — tortilgan oʻrtachaning bir koʻrinishi. Choy, sharbat, kislota yoki
qotishma — gʻoya bitta: <mark>sof moddaning miqdorini kuzating</mark>. Suv qoʻshilsa yoki
bugʻlansa, sof modda oʻzgarmaydi; faqat umumiy hajm oʻzgaradi. Shu bitta kuzatuv
aralashma savollarining koʻpini bir qatorda yechadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>konsentratsiyadan sof modda miqdorini topasiz;</li>
    <li>ikki aralashmani qoʻshganda yangi foizni hisoblaysiz;</li>
    <li>suv qoʻshish yoki bugʻlatish masalasini sof modda orqali yechasiz;</li>
    <li>aralashtirish nisbatini «chalishtirish» usuli bilan bir zumda topasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Amount of substance</span>
  <span class="pe-chip pe-chip--o">pure amount</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">concentration</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--v">total volume</span>
</div>

<h3>Ikki aralashmani qoʻshish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">10 L of 20% + 30 L of 40%</span>
    <span class="pm-solve__why">Har biridagi sof moddani topamiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2 L + 12 L = 14 L; jami 40 L</span>
    <span class="pm-solve__why">Sof moddalar va hajmlar alohida qoʻshiladi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">14 ÷ 40 = 0.35 → 35%</span>
    <span class="pm-solve__why">Foizlar qoʻshilmaydi va oʻrtachalanmaydi</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  20% va 40% ning oʻrtachasi 30%, lekin javob 35%: 40% li eritma uch baravar koʻp. Bu
  avvalgi darsdagi tuzoqning aynan oʻzi — <b>foizlarni hajm bilan tortib</b> oʻrtachalang
  yoki toʻgʻridan-toʻgʻri sof modda bilan hisoblang.
</div>

<h3>Suv qoʻshish — sof modda oʻzgarmaydi</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">20 L of 30% salt solution → 20% ?</span>
    <span class="pm-solve__why">Necha litr suv qoʻshish kerak</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Tuz: 0.3 × 20 = 6 L</span>
    <span class="pm-solve__why">Suv qoʻshilganda tuz miqdori oʻzgarmaydi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">6 L — yangi hajmning 20% i → hajm = 6 ÷ 0.2 = 30 L</span>
    <span class="pm-solve__why">Yangi umumiy hajmni topdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">30 − 20 = 10 L suv</span>
    <span class="pm-solve__why">Qoʻshiladigan suv — hajmlar farqi</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Bugʻlanish — teskari jarayon: suv ketadi, modda qoladi. 50 L 10% li shakar suvidan
  10 L suv bugʻlansa, shakar 5 L ligicha qoladi, hajm 40 L boʻladi: 5 ÷ 40 = 12.5%.
</div>

<h3>Chalishtirish — aralashtirish nisbati</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">$4/kg va $10/kg yongʻoq → $6/kg aralashma</span>
    <span class="pm-solve__why">Qaysi nisbatda aralashtirish kerak</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">10 − 6 = 4; 6 − 4 = 2</span>
    <span class="pm-solve__why">Har bir narxning maqsaddan uzoqligi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">arzon : qimmat = 4 : 2 = 2 : 1</span>
    <span class="pm-solve__why">Uzoqliklar <b>chalishtirib</b> qoʻyiladi: arzonga qimmatning uzoqligi</span>
  </div>
</div>

<p>Tekshiruv: 20 kg arzon (80 dollar) va 10 kg qimmat (100 dollar) — 30 kg uchun 180 dollar,
yaʼni kilogrami 6 dollar ✓. Maqsad narx arzonga yaqin, demak arzon mahsulot koʻproq boʻladi —
bu mantiq bilan ham mos.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Chalishtirishda eng koʻp xato — nisbatni <b>teskari</b> yozish (1 : 2). Mantiq tekshiruvi:
  aralashma narxi qaysi narxga yaqin boʻlsa, oʻsha mahsulot <b>koʻproq</b>. $6 — $4 ga yaqin,
  demak arzon yongʻoq koʻp.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Suv — 0% li, sof modda — 100% li eritma.</b> Bu qarash har bir aralashma savolini bitta
  turga keltiradi: «sof spirt qoʻshildi» — 100% li eritma qoʻshildi, «suv qoʻshildi» — 0% li
  eritma qoʻshildi. Keyin oddiy tortilgan oʻrtacha: sof moddalar yigʻindisi ÷ hajmlar
  yigʻindisi. Qoʻshilgan modda <b>hajmni ham oshiradi</b> — buni unutish eng koʻp uchraydigan xato.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>a 30% salt solution</b><span>30% i tuz boʻlgan eritma</span></li>
  <li><b>how many liters of water must be added</b><span>necha litr suv qoʻshish kerak</span></li>
  <li><b>evaporates</b><span>bugʻlanadi</span></li>
  <li><b>pure alcohol</b><span>sof spirt — 100% li</span></li>
  <li><b>cost per kilogram of the mixture</b><span>aralashmaning bir kilogrami narxi</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>How many liters of water must be added to 20 liters of a 30% salt solution to
    produce a 20% salt solution?</p>
  </div>
  <ol class="ps-ch">
    <li>5</li>
    <li>10</li>
    <li>15</li>
    <li>20</li>
    <li>30</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 10</p>
      <p>Tuz 6 L; 20% li eritmada u 30 L ga toʻgʻri keladi; 30 − 20 = 10.</p>
      <p><b>30</b> — yangi umumiy hajm; savol qoʻshiladigan suvni soʻradi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">30</span>
  <span class="ps-trap__why">Yarim yoʻlda toʻxtagan javob: yangi hajm topildi, lekin undan
  eski hajm ayirilmadi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>A merchant mixes 20 kilograms of tea that costs $6 per kilogram with 30 kilograms of
    tea that costs $11 per kilogram. What is the cost per kilogram of the mixture?</p>
  </div>
  <ol class="ps-ch">
    <li>$8.00</li>
    <li>$8.50</li>
    <li>$9.00</li>
    <li>$9.50</li>
    <li>$10.00</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) $9.00</p>
      <p>(120 + 330) ÷ 50 = 450 ÷ 50 = 9.</p>
      <p><b>$8.50</b> — narxlarning oddiy oʻrtachasi; qimmat choy koʻproq.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">$8.50</span>
  <span class="ps-trap__why">Ikki narxni oʻrtachalash — miqdorlar teng boʻlgandagina toʻgʻri.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Aralashma savolida jadvalsiz ham <b>uch qatorli</b> hisob yetarli:</p>
  <ol>
    <li>har bir aralashmadagi sof moddani yozing;</li>
    <li>sof moddalarni va hajmlarni alohida qoʻshing (suv — 0% li modda, sof modda — 100% li);</li>
    <li>sof modda ÷ hajm = yangi foiz; savol boshqa narsa soʻrasa, shu tenglamadan toping.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">10 L of 20% + 30 L of 40% → 30%</p>
  <p class="pe-good">(2 + 12) ÷ 40 = 35%</p>
  <p class="pe-fix__why">Foizlar hajmlar bilan tortiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Water added, so the salt also changes</p>
  <p class="pe-good">Salt stays at 6 liters; only the total grows</p>
  <p class="pe-fix__why">Suv qoʻshilganda yoki bugʻlanganda sof modda oʻzgarmaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> How many liters of salt are in 40 liters of a 15% salt solution?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">6 — 0.15 × 40.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> 10 liters of a 20% solution are mixed with 10
  liters of a 40% solution. What is the concentration of the mixture?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">30% — hajmlar teng, shuning uchun bu safar oddiy oʻrtacha toʻgʻri.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> 10 liters of water evaporate from 50 liters of a
  10% sugar solution. What is the new concentration?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">12.5% — 5 ÷ 40.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> 4 liters of water are added to 6 liters of a
  50% juice drink. What percent of the new drink is juice?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">30% — 3 ÷ 10.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> How many kilograms of $4 nuts must be mixed with
  10 kilograms of $10 nuts to make a mixture worth $6 per kilogram?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">20 — nisbat 2 : 1, qimmati 10 kg.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>mixture</b><span>aralashma</span></li>
  <li><b>solution</b><span>eritma</span></li>
  <li><b>concentration</b><span>konsentratsiya, ulush</span></li>
  <li><b>pure</b><span>sof</span></li>
  <li><b>dilute</b><span>suyultirmoq</span></li>
  <li><b>evaporate</b><span>bugʻlanmoq</span></li>
  <li><b>alloy</b><span>qotishma</span></li>
  <li><b>blend</b><span>aralashtirilgan mahsulot</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Sof modda = konsentratsiya × hajm — har doim shundan boshlang.</li>
    <li>Aralashtirishda sof moddalar va hajmlar alohida qoʻshiladi.</li>
    <li>Suv qoʻshilsa yoki bugʻlansa, sof modda oʻzgarmaydi.</li>
    <li>Chalishtirish: nisbat — maqsaddan uzoqliklarning teskarisi.</li>
    <li>Aralashma narxi qaysi narxga yaqin boʻlsa, oʻsha mahsulot koʻproq.</li>
  </ul>
</div>
"""

GMAT13 = """
<h2>GMAT-13: Rates, Work and Distance</h2>

<p>Tezlik, ish va masofa masalalari bitta formulaga tayanadi: <mark>miqdor = tezlik ×
vaqt</mark>. Masofa = tezlik × vaqt; bajarilgan ish = ish unumi × vaqt. GMAT bu formulani
uch xil tuzoq bilan beradi: oʻrtacha tezlik, bir-biriga qarab yurish va birgalikdagi ish.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>masofa, tezlik va vaqtdan istalganini qolgan ikkitasidan topasiz;</li>
    <li>oʻrtacha tezlikni umumiy masofa ÷ umumiy vaqt deb hisoblaysiz;</li>
    <li>bir-biriga qarab va bir yoʻnalishda harakatda nisbiy tezlikni qoʻllaysiz;</li>
    <li>birgalikdagi ishni unumlarni qoʻshish bilan yechasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Rate formula</span>
  <span class="pe-chip pe-chip--o">distance (or work)</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">rate</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--v">time</span>
</div>

<h3>Oʻrtacha tezlik — umumiy masofa ÷ umumiy vaqt</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">120 km — 2 soatda, keyin 180 km — 3 soatda</span>
    <span class="pm-solve__why">Ikki boʻlakli safar</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Jami: 300 km, 5 soat</span>
    <span class="pm-solve__why">Masofalar va vaqtlar alohida qoʻshiladi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">300 ÷ 5 = 60 km/h</span>
    <span class="pm-solve__why">Tezliklar oʻrtachalanmaydi</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bir xil masofani 60 va 40 km/soat bilan bossangiz, oʻrtacha tezlik <b>48</b>, 50 emas:
  sekin yoʻlda koʻproq vaqt oʻtadi, va oʻrtacha unga qarab tortiladi. Tez formula:
  2 × 60 × 40 ÷ (60 + 40) = 48. Lekin har doim xavfsiz yoʻl — masofani oʻzingiz tanlang
  (masalan, 120 km) va vaqtlarni hisoblang.
</div>

<h3>Nisbiy tezlik</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">300 km oraliq, 70 va 80 km/h, bir-biriga qarab</span>
    <span class="pm-solve__why">Oraliq har soatda 70 + 80 = 150 km qisqaradi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">300 ÷ 150 = 2 soat</span>
    <span class="pm-solve__why">Qarama-qarshi yoʻnalishda — tezliklar qoʻshiladi</span>
  </div>
</div>

<p>Bir yoʻnalishda harakatda esa tezliklar <b>ayiriladi</b>: yuk mashinasi 60 km/soat bilan
chiqib, bir soatdan keyin orqasidan 80 km/soat bilan avtomobil chiqsa, oradagi 60 km
har soatda 20 km dan qisqaradi — avtomobil 3 soatda yetib oladi.</p>

<h3>Birgalikdagi ish — unumlar qoʻshiladi</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">A — 6 soat, B — 3 soat</span>
    <span class="pm-solve__why">Vaqtlar emas, unumlar qoʻshiladi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">1/6 + 1/3 = 1/6 + 2/6 = 1/2</span>
    <span class="pm-solve__why">Birgalikda soatiga ishning yarmi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2 soat</span>
    <span class="pm-solve__why">Birgalikdagi unumning teskarisi</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Mantiqiy tekshiruv: birgalikdagi vaqt <b>eng tez ishchining vaqtidan kam</b> boʻlishi
  shart. B yolgʻiz 3 soatda bajarsa, yordamchi bilan 3 soatdan koʻp ketishi mumkin emas —
  4.5 kabi variantlar darrov chiqib ketadi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Quvur masalasida toʻldiruvchi quvur — musbat unum, boʻshatuvchi — <b>manfiy</b> unum.
  5 soatda toʻldiradigan va 10 soatda boʻshatadigan quvurlar birga ochilsa: 1/5 − 1/10 =
  1/10, yaʼni hovuz 10 soatda toʻladi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Birliklar — eng jim xato. Tezlik soatda, vaqt daqiqada berilsa, daqiqani 60 ga boʻling:
  15 daqiqa = 0.25 soat, 20 daqiqa = 1/3, 40 daqiqa = 2/3 soat. «2 hours 15 minutes» —
  bu <b>2.25</b> soat, 2.15 emas. GMAT bu xatoga atayin variant tayyorlab qoʻyadi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>at a constant rate</b><span>bir xil tezlikda</span></li>
  <li><b>working together</b><span>birgalikda ishlab</span></li>
  <li><b>toward each other</b><span>bir-biriga qarab</span></li>
  <li><b>round trip</b><span>borib-kelish</span></li>
  <li><b>catch up with</b><span>quvib yetmoq</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>Working alone at a constant rate, machine A can complete a job in 6 hours. Machine B,
    working alone at a constant rate, can complete the same job in 3 hours. How many hours
    will it take the two machines, working together, to complete the job?</p>
  </div>
  <ol class="ps-ch">
    <li>1.5</li>
    <li>2</li>
    <li>2.5</li>
    <li>4.5</li>
    <li>9</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 2</p>
      <p>1/6 + 1/3 = 1/2 ish soatiga, demak 2 soat.</p>
      <p><b>4.5</b> — vaqtlarni oʻrtachalagan javob; u B ning yolgʻiz vaqtidan ham koʻp.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">4.5</span>
  <span class="ps-trap__why">Vaqtlarni oʻrtachalash. Yordamchi qoʻshilsa, ish tezlashadi —
  javob 3 soatdan kam boʻlishi shart.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>Two trains are 300 kilometers apart and travel toward each other on parallel tracks,
    one at 70 kilometers per hour and the other at 80 kilometers per hour. In how many hours
    will they meet?</p>
  </div>
  <ol class="ps-ch">
    <li>1</li>
    <li>1.5</li>
    <li>2</li>
    <li>4</li>
    <li>30</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 2</p>
      <p>Bir-biriga qarab: 70 + 80 = 150 km/soat; 300 ÷ 150 = 2.</p>
      <p><b>30</b> — tezliklarni ayirgan javob (300 ÷ 10); bu bir yoʻnalishdagi harakat uchun.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">30</span>
  <span class="ps-trap__why">Yoʻnalishni adashtirish. Bir-biriga qarab — qoʻshiladi, bir tomonga
  — ayiriladi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Har bir tezlik savolida <b>birliklarni</b> tekshiring:</p>
  <ol>
    <li>tezlik km/soatda, vaqt esa daqiqada berilsa — daqiqani soatga oʻtkazing (40 min = 2/3 soat);</li>
    <li>ish masalasida «1 ish» deb oling, unum = 1 ÷ vaqt;</li>
    <li>javobni mantiq bilan tekshiring: birgalikdagi vaqt eng tez ishchinikidan kam.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">60 km/h there, 40 km/h back → average 50 km/h</p>
  <p class="pe-good">Average = total distance ÷ total time = 48 km/h</p>
  <p class="pe-fix__why">Tezliklar vaqt bilan tortiladi, masofa bilan emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">A takes 6 h, B takes 3 h → together 9 h</p>
  <p class="pe-good">1/6 + 1/3 = 1/2 → 2 h</p>
  <p class="pe-fix__why">Vaqtlar emas, unumlar qoʻshiladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> How many hours does it take to drive 240
  kilometers at 60 kilometers per hour?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">4 — 240 ÷ 60.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> A car travels 120 km in 2 hours and then 180 km
  in 3 hours. What is its average speed in km per hour?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">60 — 300 ÷ 5.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> A can do a job in 4 hours and B in 12 hours.
  How many hours do they need together?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">3 — 1/4 + 1/12 = 4/12 = 1/3.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> How far does a car travel in 45 minutes at 80
  kilometers per hour?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">60 km — 45 daqiqa = 3/4 soat, 80 × 3/4.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> One pipe fills a tank in 5 hours and a drain
  empties it in 10 hours. With both open, how many hours does it take to fill the empty tank?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">10 — 1/5 − 1/10 = 1/10.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>rate</b><span>tezlik, unum</span></li>
  <li><b>constant rate</b><span>oʻzgarmas tezlik</span></li>
  <li><b>average speed</b><span>oʻrtacha tezlik</span></li>
  <li><b>round trip</b><span>borib-kelish</span></li>
  <li><b>toward each other</b><span>bir-biriga qarab</span></li>
  <li><b>catch up</b><span>quvib yetmoq</span></li>
  <li><b>pipe / drain</b><span>quvur / chiqarish quvuri</span></li>
  <li><b>output</b><span>mahsulot hajmi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Masofa (yoki ish) = tezlik × vaqt.</li>
    <li>Oʻrtacha tezlik = umumiy masofa ÷ umumiy vaqt; tezliklar oʻrtachalanmaydi.</li>
    <li>Bir-biriga qarab — tezliklar qoʻshiladi, bir tomonga — ayiriladi.</li>
    <li>Birgalikdagi ish: unumlar (1 ÷ vaqt) qoʻshiladi; boʻshatuvchi — ayiriladi.</li>
    <li>Birgalikdagi vaqt eng tez ishchinikidan kam boʻlishi shart.</li>
  </ul>
</div>
"""

GMAT14 = """
<h2>GMAT-14: Profit, Cost, Markup and Discount</h2>

<p>Bu dars — MBA'ga tayyorlanayotgan odam uchun eng «oʻz» mavzusi: tannarx, ustama,
chegirma, foyda va zararsizlik nuqtasi. Matematikasi GMAT-5 dagi foizlar; yangi narsa —
<mark>har bir foiz qaysi narxdan olinayotganini</mark> kuzatish. Ustama tannarxdan,
chegirma belgilangan narxdan, foyda foizi esa koʻpincha tannarxdan olinadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>tannarx, belgilangan narx va sotish narxini ajratasiz;</li>
    <li>ustama va chegirmani ketma-ket koʻpaytuvchilar bilan qoʻllaysiz;</li>
    <li>foyda foizidan tannarxni teskari topasiz;</li>
    <li>zararsizlik nuqtasini (<i>break-even</i>) hisoblaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Profit</span>
  <span class="pe-chip pe-chip--o">profit</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">revenue</span>
  <span class="pe-op">−</span>
  <span class="pe-chip pe-chip--v">cost</span>
</div>

<h3>Uch narx — uch xil baza</h3>

<p><b>Tannarx</b> (<i>cost</i>) — doʻkon mahsulotni qanchaga olgani. <b>Belgilangan narx</b>
(<i>marked price, list price</i>) — tannarx ustiga ustama qoʻyilgani. <b>Sotish narxi</b>
(<i>selling price</i>) — chegirmadan keyin xaridor toʻlagani. Ustama tannarxdan, chegirma
belgilangan narxdan olinadi — shuning uchun «50% ustama va 50% chegirma» narxni joyiga
qaytarmaydi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Cost $80, marked up 50%</span>
    <span class="pm-solve__why">80 × 1.5</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Marked price $120, discount 20%</span>
    <span class="pm-solve__why">120 × 0.8 = 96</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Profit = 96 − 80 = $16 (20% of cost)</span>
    <span class="pm-solve__why">1.5 × 0.8 = 1.2 — sof natija +20%</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «+50%, keyin −20%» = <b>+30%</b> emas. Har bir oʻzgarish — koʻpaytuvchi: 1.5 × 0.8 = 1.2,
  yaʼni +20%. Bu GMAT-5 dagi «ketma-ket foizlar koʻpaytiriladi» qoidasining doʻkondagi
  koʻrinishi.
</div>

<h3>Foyda foizidan tannarxga</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Sold for $120 at a 20% profit on cost</span>
    <span class="pm-solve__why">Sotish narxi = 1.2 × tannarx</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Cost = 120 ÷ 1.2 = $100</span>
    <span class="pm-solve__why">Boʻlamiz; 120 × 0.8 = 96 — xato</span>
  </div>
</div>

<h3>Zararsizlik nuqtasi</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Fixed costs $12,000; price $25; cost per unit $10</span>
    <span class="pm-solve__why">Har bir dona 25 − 10 = $15 qoldiradi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">12,000 ÷ 15 = 800 units</span>
    <span class="pm-solve__why">Doimiy xarajat qoplanadigan miqdor</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Har bir donadan qoladigan farq — <b>marjinal daromad</b> (<i>contribution per unit</i>).
  Zararsizlik nuqtasi = doimiy xarajat ÷ shu farq. Foyda maqsadi ham qoʻshilsa:
  (doimiy xarajat + maqsad foyda) ÷ farq.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Profit as a percent of cost» va «as a percent of revenue» — har xil savol. $200 ga olib,
  $250 ga sotilgan mahsulotda foyda tannarxning 25% i, tushumning esa 20% i. Savolda
  «of» dan keyingi soʻzni toping — u bazani aytadi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Zarar ham foiz bilan oʻlchanadi va u ham <b>tannarxdan</b> olinadi: $90 ga sotilib, 20% zarar
  koʻrilgan boʻlsa, tannarx 90 ÷ 0.8 = $112.50, 90 × 1.2 = $108 emas. Qoida bitta: foiz qaysi
  narxdan olingan boʻlsa, oʻsha narxni nomaʼlum deb oling va mos koʻpaytuvchiga boʻling. Bu
  foyda, zarar, ustama va chegirma uchun bir xil ishlaydi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>marked up by 40%</b><span>tannarx ustiga 40% ustama qoʻyildi</span></li>
  <li><b>sold at a 20% discount</b><span>20% chegirma bilan sotildi</span></li>
  <li><b>profit as a percent of cost</b><span>foyda — tannarxning necha foizi</span></li>
  <li><b>break even</b><span>zararsiz ishlamoq — foyda nolga teng</span></li>
  <li><b>fixed costs / variable cost per unit</b><span>doimiy xarajatlar / bir donaning oʻzgaruvchan xarajati</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>A retailer buys a jacket for $80, marks the price up by 50%, and then sells the
    jacket at a 20% discount from the marked price. What is the retailer's profit on the
    jacket?</p>
  </div>
  <ol class="ps-ch">
    <li>$8</li>
    <li>$12</li>
    <li>$16</li>
    <li>$24</li>
    <li>$40</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) $16</p>
      <p>80 × 1.5 = 120; 120 × 0.8 = 96; 96 − 80 = 16.</p>
      <p><b>$24</b> — +50% va −20% ni qoʻshib, +30% deb hisoblagan javob.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">$24</span>
  <span class="ps-trap__why">Foizlarni qoʻshish. Chegirma kattaroq narxdan (120) olinadi —
  koʻpaytiring: 1.5 × 0.8.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>A company has fixed costs of $12,000 per month. Each unit it sells brings in $25 and
    costs $10 to produce. How many units must the company sell in a month to break even?</p>
  </div>
  <ol class="ps-ch">
    <li>480</li>
    <li>800</li>
    <li>1,000</li>
    <li>1,200</li>
    <li>1,500</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 800</p>
      <p>Har bir donadan 25 − 10 = 15 dollar qoladi; 12,000 ÷ 15 = 800.</p>
      <p><b>480</b> — 12,000 ni butun narxga (25) boʻlgan javob; ishlab chiqarish xarajati unutilgan.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">480</span>
  <span class="ps-trap__why">Narxning hammasi doimiy xarajatni qoplamaydi — avval har bir
  donaning oʻz xarajati ayiriladi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Narx zanjirini <b>koʻpaytuvchilar</b> bilan yozing:</p>
  <ol>
    <li>ustama 40% → × 1.4; chegirma 25% → × 0.75; zarar 20% → × 0.8;</li>
    <li>zanjirni bitta koʻpaytuvchiga yigʻing (1.4 × 0.75 = 1.05 → +5%);</li>
    <li>oxirgi narx berilib, boshlangʻichi soʻralsa — shu koʻpaytuvchiga boʻling.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">Marked up 50%, then 20% off → profit 30%</p>
  <p class="pe-good">1.5 × 0.8 = 1.2 → profit 20%</p>
  <p class="pe-fix__why">Ketma-ket foizlar koʻpaytiriladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Sold for $120 at 20% profit → cost = 120 × 0.8 = $96</p>
  <p class="pe-good">Cost = 120 ÷ 1.2 = $100</p>
  <p class="pe-fix__why">20% foyda tannarxdan olingan — boʻling, sotish narxidan 20% ayirmang.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> An item bought for $200 is sold for $250. What
  is the profit as a percent of cost?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">25% — 50 ÷ 200.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> A $60 item is discounted by 15%. What is the sale price?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">$51 — 60 × 0.85.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> Successive discounts of 20% and 10% equal what
  single discount?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">28% — 0.8 × 0.9 = 0.72.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> An item sold for $120 earned a 20% profit on
  cost. What was the cost?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">$100 — 120 ÷ 1.2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> Fixed costs are $6,000. A product sells for $40
  and costs $25 to make. How many units must be sold to break even?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">400 — 6,000 ÷ 15.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>cost price</b><span>tannarx</span></li>
  <li><b>marked price / list price</b><span>belgilangan narx</span></li>
  <li><b>selling price</b><span>sotish narxi</span></li>
  <li><b>markup</b><span>ustama</span></li>
  <li><b>discount</b><span>chegirma</span></li>
  <li><b>revenue</b><span>tushum</span></li>
  <li><b>fixed costs</b><span>doimiy xarajatlar</span></li>
  <li><b>break-even point</b><span>zararsizlik nuqtasi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Ustama — tannarxdan, chegirma — belgilangan narxdan.</li>
    <li>Narx zanjirini koʻpaytuvchilar bilan yozing: 1.5 × 0.8 = 1.2.</li>
    <li>Foyda foizidan tannarxga — boʻlish bilan.</li>
    <li>Zararsizlik = doimiy xarajat ÷ (narx − bir dona xarajati).</li>
    <li>«Of cost» va «of revenue» — har xil baza.</li>
  </ul>
</div>
"""

GMAT15 = """
<h2>GMAT-15: Simple and Compound Interest</h2>

<p>Foiz daromadi — moliyaning asosi va GMAT'ning sevimli mavzusi. Ikki turi bor:
<mark>oddiy foiz</mark> har yili bir xil summa qoʻshadi, <mark>murakkab foiz</mark> esa
foizga ham foiz hisoblaydi. Kalkulyatorsiz imtihonda savollar shunday tuziladiki, sonlar
qoʻlda hisoblanadigan boʻladi — 10%, 2 yil, yumaloq summa.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>oddiy foizni summa × stavka × vaqt bilan hisoblaysiz;</li>
    <li>murakkab foizni har yili koʻpaytirib topasiz;</li>
    <li>yillik va yarim yillik kapitallashuvni farqlaysiz;</li>
    <li>«72 qoidasi» bilan ikki baravar oshish vaqtini taxmin qilasiz.</li>
  </ul>
</div>

<h3>Oddiy foiz</h3>

<div class="pe-formula">
  <span class="pe-formula__label">Simple interest</span>
  <span class="pe-chip pe-chip--o">interest</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">principal</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--v">rate</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--s">time</span>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">$5,000 at 6% simple interest for 3 years</span>
    <span class="pm-solve__why">Har yili bir xil foiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5,000 × 0.06 = $300 a year</span>
    <span class="pm-solve__why">Bir yillik foiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">300 × 3 = $900</span>
    <span class="pm-solve__why">Uch yil — uch marta bir xil summa</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Vaqtni har doim <b>yillarda</b> yozing: 6 oy = 0.5 yil, 18 oy = 1.5 yil. Stavka «per year»
  boʻlib, vaqt oylarda berilsa, eng koʻp xato shu yerda chiqadi — 6 oyni 6 yil deb hisoblash.
</div>

<h3>Murakkab foiz — har yili koʻpaytiring</h3>

<div class="pe-formula">
  <span class="pe-formula__label">Compound interest</span>
  <span class="pe-chip pe-chip--o">amount</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">principal</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--v">(1 + rate)<sup>years</sup></span>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">$10,000 at 10% compounded annually, 2 years</span>
    <span class="pm-solve__why">Har yil × 1.1</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">1-yil: 10,000 × 1.1 = 11,000</span>
    <span class="pm-solve__why">Birinchi yil oddiy foiz bilan bir xil</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2-yil: 11,000 × 1.1 = 12,100</span>
    <span class="pm-solve__why">Foiz endi 11,000 dan — 1,100, 1,000 emas</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Ikki yillik murakkab va oddiy foiz farqi — <b>foizning foizi</b>: summa × stavka<sup>2</sup>.
  10,000 da 10% bilan: 10,000 × 0.01 = 100 (12,100 va 12,000 farqi). Bu formula
  hisoblashni bir qatorga qisqartiradi.
</div>

<h3>Yarim yillik kapitallashuv</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">8% a year, compounded semiannually, $1,000, 1 year</span>
    <span class="pm-solve__why">Har yarim yilda 8 ÷ 2 = 4%</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">1,000 × 1.04 × 1.04 = $1,081.60</span>
    <span class="pm-solve__why">Ikki davr — yillik 8% dan (1,080) biroz koʻp</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Compounded semiannually» — stavka ikkiga boʻlinadi, davrlar soni ikki baravar oshadi.
  «Quarterly» — toʻrtga boʻlinadi, davrlar toʻrt baravar. Kapitallashuv qanchalik tez-tez
  boʻlsa, natija shunchalik biroz katta — lekin farq kichik.
</div>

<p><b>72 qoidasi</b> — tez taxmin: murakkab foizda pul taxminan 72 ÷ stavka yilda ikki baravar
oshadi. 8% da — taxminan 9 yil, 6% da — 12 yil. Bu aniq formula emas, lekin «approximately»
deb soʻralgan savolda yetarli.</p>

<h3>Teskari savol — stavkani topish</h3>

<p>Baʼzan summa va natija beriladi, stavka esa soʻraladi. Ikki yilda 40,000 dan 48,400 ga
oʻsgan boʻlsa: 48,400 ÷ 40,000 = 1.21. Bu 1.1 ning kvadrati, demak stavka 10%. 21% ni
ikkiga boʻlib 10.5% deyish — oddiy foiz fikri; murakkab foizda koʻpaytuvchidan <b>ildiz</b>
olinadi. Shuning uchun 1.21, 1.44, 1.69 kabi kvadratlarni tanib olish foydali.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bizning banklarning omonat shartnomalarida «kapitallashuv bilan» degan ibora — aynan
  <i>compounded</i>. Kapitallashuvsiz omonatda foiz har oy kartaga tushadi va oʻzi yangi foiz
  olib kelmaydi — bu oddiy foiz. Bir xil stavkada kapitallashuvli omonat har doim biroz
  koʻproq beradi, va muddat uzaygan sari farq tezroq oʻsadi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>principal</b><span>asosiy summa — dastlab qoʻyilgan pul</span></li>
  <li><b>simple annual interest</b><span>yillik oddiy foiz</span></li>
  <li><b>compounded annually</b><span>har yili kapitallashtiriladi — murakkab foiz</span></li>
  <li><b>compounded semiannually / quarterly</b><span>yarim yilda / choraklik</span></li>
  <li><b>the amount in the account</b><span>hisobdagi jami summa — asosiy summa + foiz</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>How much interest does $5,000 earn in 3 years at 6% simple annual interest?</p>
  </div>
  <ol class="ps-ch">
    <li>$300</li>
    <li>$900</li>
    <li>$955.08</li>
    <li>$5,900</li>
    <li>$9,000</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) $900</p>
      <p>5,000 × 0.06 × 3 = 900.</p>
      <p><b>$955.08</b> — murakkab foiz bilan hisoblangan javob; savol oddiy foiz deydi.
      <b>$5,900</b> — jami summa, faqat foiz emas.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">$5,900</span>
  <span class="ps-trap__why">«Interest» — faqat foiz daromadi. «Amount» yoki «balance» desa,
  asosiy summa ham qoʻshiladi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>An investor deposits $10,000 in an account that pays 10% annual interest, compounded
    annually. What is the amount in the account after 2 years?</p>
  </div>
  <ol class="ps-ch">
    <li>$11,000</li>
    <li>$12,000</li>
    <li>$12,100</li>
    <li>$12,200</li>
    <li>$20,000</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) $12,100</p>
      <p>10,000 × 1.1 × 1.1 = 12,100.</p>
      <p><b>$12,000</b> — oddiy foiz bilan hisoblangan javob.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">$12,000</span>
  <span class="ps-trap__why">Ikkinchi yilning foizi oʻsgan summadan (11,000) olinadi — bu
  «compounded» soʻzining butun maʼnosi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Foiz savolida avval <b>uchta narsani</b> belgilang:</p>
  <ol>
    <li>oddiymi yoki murakkab («compounded» soʻzi bormi);</li>
    <li>vaqt yillarda nechaga teng, kapitallashuv davri qancha;</li>
    <li>savol foizni («interest») soʻrayaptimi yoki jami summani («amount», «balance»).</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">10% compounded annually for 2 years → 20% growth</p>
  <p class="pe-good">1.1 × 1.1 = 1.21 → 21% growth</p>
  <p class="pe-fix__why">Murakkab foizda foizlar koʻpaytiriladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">8% compounded semiannually → 1,000 × 1.08 × 1.08</p>
  <p class="pe-good">1,000 × 1.04 × 1.04</p>
  <p class="pe-fix__why">Yarim yillik davrda stavka ikkiga boʻlinadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> What is the simple interest on $2,000 at 5% per
  year for 4 years?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">$400 — 2,000 × 0.05 × 4.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> What does $1,000 grow to in 3 years at 10%
  compounded annually?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">$1,331 — 1,000 → 1,100 → 1,210 → 1,331.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> How much interest does $8,000 earn in 2 years at
  5% compounded annually?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">$820 — 8,000 × 1.1025 = 8,820.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> What does $1,000 grow to in 1 year at 8% a year
  compounded semiannually?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">$1,081.60 — 1,000 × 1.04 × 1.04.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> By the rule of 72, about how many years does money
  take to double at 8% compounded annually?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">9 — 72 ÷ 8.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>principal</b><span>asosiy summa</span></li>
  <li><b>interest</b><span>foiz daromadi</span></li>
  <li><b>interest rate</b><span>foiz stavkasi</span></li>
  <li><b>simple interest</b><span>oddiy foiz</span></li>
  <li><b>compound interest</b><span>murakkab foiz</span></li>
  <li><b>compounded semiannually</b><span>yarim yilda bir kapitallashtiriladi</span></li>
  <li><b>deposit / loan</b><span>omonat / kredit</span></li>
  <li><b>balance</b><span>hisobdagi qoldiq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Oddiy foiz = summa × stavka × yillar.</li>
    <li>Murakkab: har davrda (1 + stavka) ga koʻpaytiring.</li>
    <li>Yarim yillik — stavka ÷ 2, davrlar × 2.</li>
    <li>Ikki yillik farq: summa × stavka<sup>2</sup>.</li>
    <li>«Interest» — faqat foiz; «amount» — summa + foiz. 72 ÷ stavka — ikki baravar oshish vaqti.</li>
  </ul>
</div>
"""

TUTORIALS = [
    {
        "title": "GMAT-11: Averages and Weighted Averages",
        "category": "math", "order": 11,
        "summary": "Oʻrtachani yigʻindiga aylantirish, son qoʻshilgan yoki olib tashlangan masalalar, tortilgan oʻrtacha va teng oraliqli toʻplamlar.",
        "stories": ["The Average That Hid a Branch"],
        "content": GMAT11,
    },
    {
        "title": "GMAT-12: Mixtures and Concentrations",
        "category": "math", "order": 12,
        "summary": "Sof modda miqdori, ikki aralashmani qoʻshish, suv qoʻshish va bugʻlatish, chalishtirish bilan aralashtirish nisbatini topish.",
        "stories": ["The Tea Blender"],
        "content": GMAT12,
    },
    {
        "title": "GMAT-13: Rates, Work and Distance",
        "category": "math", "order": 13,
        "summary": "Masofa = tezlik × vaqt, oʻrtacha tezlik, nisbiy tezlik, birgalikdagi ish va quvur masalalari.",
        "stories": ["Two Printers, One Deadline"],
        "content": GMAT13,
    },
    {
        "title": "GMAT-14: Profit, Cost, Markup and Discount",
        "category": "math", "order": 14,
        "summary": "Tannarx, belgilangan narx va sotish narxi, ustama va chegirma zanjiri, foyda foizidan tannarxga, zararsizlik nuqtasi.",
        "stories": ["The Sale That Lost Money"],
        "content": GMAT14,
    },
    {
        "title": "GMAT-15: Simple and Compound Interest",
        "category": "math", "order": 15,
        "summary": "Oddiy va murakkab foiz, yarim yillik kapitallashuv, ikki yillik farq formulasi va 72 qoidasi.",
        "stories": ["Simple or Compound?"],
        "content": GMAT15,
    },
]
