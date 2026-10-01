# -*- coding: utf-8 -*-
"""Prime GMAT — GMAT-1 … GMAT-5 (pilot): the Quant section, arithmetic without a
calculator, integers and factors, primes / GCD / LCM, odd–even and signs, percentages.

Written with STYLE_GUIDE_PRIME_GMAT.md · lesson list in toc_prime_gmat.txt.
Exam English in the stems, Uzbek for the teaching. Numbers the American way (3.5, 1,200).
Five answer choices, as on the GMAT; no calculator, so no Desmos blocks.

Facts about the test (mba.com / gmac.com, checked 2026-10-01): GMAT Focus Edition —
Quantitative Reasoning 21 questions / 45 minutes, Problem Solving only, five choices,
arithmetic and algebra (no geometry, no data sufficiency — that moved to Data Insights),
no calculator; section scores 60–90, total 205–805 across three equally weighted
sections; sections in any order, an optional 10-minute break, and up to three answers
edited per section.

Import:
    python manage.py import_tutorials tutorial/management/commands/_tutorials_prime_gmat_01_05.py --author=prime
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

GMAT1 = """
<h2>GMAT-1: The Quant Section and Arithmetic Without a Calculator</h2>

<p>GMAT'ning Quant boʻlimida <mark>kalkulyator yoʻq</mark> — va bu bitta qoida butun
tayyorgarlikni oʻzgartiradi. Savollar murakkab hisob talab qilmaydi; ular <b>aqlli
hisob</b>ni talab qiladi. Bu dars boʻlimning qanday ishlashini va qoʻlda tez
hisoblashning bir nechta usulini beradi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>Quant boʻlimining tuzilishini va vaqtini bilasiz;</li>
    <li>har bir savolga qancha vaqt ketishi kerakligini sezasiz;</li>
    <li>25, 5 va 12 ga koʻpaytirishni ogʻzaki bajarasiz;</li>
    <li>javob variantlariga qarab taxmin qilib, keraksizini chiqarib tashlaysiz (<i>estimate and eliminate</i>).</li>
  </ul>
</div>

<h3>Boʻlim qanday tuzilgan</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Nima</th><th>GMAT Focus Edition</th></tr>
  <tr><td>Savollar</td><td>21 ta, hammasi <i>Problem Solving</i>, har birida 5 ta javob</td></tr>
  <tr><td>Vaqt</td><td>45 daqiqa — bir savolga oʻrtacha <b>2 daqiqa 8 soniya</b></td></tr>
  <tr><td>Mazmun</td><td>arifmetika va algebra; geometriya yoʻq</td></tr>
  <tr><td>Kalkulyator</td><td>yoʻq</td></tr>
  <tr><td>Ball</td><td>boʻlim uchun 60–90; umumiy 205–805, uch boʻlim teng hissa qoʻshadi</td></tr>
  <tr><td>Erkinlik</td><td>boʻlimlar tartibini oʻzingiz tanlaysiz; 10 daqiqalik ixtiyoriy tanaffus; har boʻlimda 3 tagacha javobni oʻzgartirish mumkin</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bizda koʻp odam kalkulyatorsiz hisoblashni maktabda qoldirib ketgan. GMAT'da bu
  qobiliyat qaytadan kerak — lekin <b>katta sonlarni koʻpaytirish</b> uchun emas, balki
  sonlarni qulay boʻlaklarga ajratish uchun. Mana shu darsning asosiy gʻoyasi.
</div>

<h3>25 ga koʻpaytirish: 4 ga boʻlib, 100 ga koʻpaytiring</h3>

<p>25 = 100 ÷ 4. Shuning uchun istalgan sonni 25 ga koʻpaytirish uchun uni 4 ga
boʻlib, 100 ga koʻpaytirish kifoya. Xuddi shunday, 5 ga koʻpaytirish — 2 ga boʻlib,
10 ga koʻpaytirish.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">48 × 25</span>
    <span class="pm-solve__why">25 ni 100 ÷ 4 deb oʻqiymiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">48 ÷ 4 = 12</span>
    <span class="pm-solve__why">Avval 4 ga boʻlamiz — oson</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">12 × 100 = 1,200</span>
    <span class="pm-solve__why">Keyin 100 ga — faqat ikki nol</span>
  </div>
</div>

<h3>Boʻlaklarga ajratish: 12 = 10 + 2, 15 = 10 + 5</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">36 × 15 = 36 × 10 + 36 × 5</span>
    <span class="pm-solve__why">15 ni 10 va 5 ga ajratdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">360 + 180</span>
    <span class="pm-solve__why">36 × 5 — bu 360 ning yarmi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">540</span>
    <span class="pm-solve__why">Ikki oson koʻpaytma yigʻindisi</span>
  </div>
</div>

<h3>Yumaloq songa yaqin sonlar: 198 = 200 − 2</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">198 × 25 = 200 × 25 − 2 × 25</span>
    <span class="pm-solve__why">198 ni «200 dan 2 kam» deb yozdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5,000 − 50</span>
    <span class="pm-solve__why">Ikkalasi ham ogʻzaki</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">4,950</span>
    <span class="pm-solve__why">Tuzatishni unutmang: 5,000 — tuzoq</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Kasrlarni ham boʻlish deb oʻqing: 0.125 = 1/8, 0.25 = 1/4, 0.2 = 1/5. Shunda
  0.125 × 64 — bu shunchaki 64 ÷ 8 = 8. Keyingi darslarda shu jadval koʻp kerak boʻladi.
</div>

<h3>Taxmin qiling, keyin chiqarib tashlang</h3>

<p>Beshta javobning hammasi bir-biridan uzoq boʻlsa, aniq hisoblash shart emas.
Sonlarni yaxlitlab, natija qaysi oraliqda ekanini toping va qolganlarini chiqarib
tashlang. Javoblar bir-biriga yaqin boʻlsa — ana shunda aniq hisoblang.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ingliz tilida savol <b>«approximately»</b> yoki <b>«closest to»</b> desa, bu
  taxmin qilishga ruxsat. Bunday savolda aniq hisoblash — vaqtni oʻgʻirlaydi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>what is the value of</b><span>… ning qiymati nechaga teng — bitta son kerak</span></li>
  <li><b>approximately / closest to</b><span>taxminan — taxmin qilish mumkin</span></li>
  <li><b>which of the following is equal to</b><span>quyidagilardan qaysi biri teng</span></li>
  <li><b>in total</b><span>jami</span></li>
  <li><b>each / per</b><span>har biri uchun — koʻpaytirish belgisi</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>What is the value of 25 × 48 − 25 × 8?</p>
  </div>
  <ol class="ps-ch">
    <li>600</li>
    <li>900</li>
    <li>1,000</li>
    <li>1,100</li>
    <li>1,200</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 1,000</p>
      <p>Umumiy koʻpaytuvchini chiqaramiz: 25 × (48 − 8) = 25 × 40 = 1,000. Ikkita
      koʻpaytmani alohida hisoblash shart emas.</p>
      <p><b>1,200</b> — faqat 25 × 48 ni hisoblab, ikkinchi hadni unutgan javob.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">1,200</span>
  <span class="ps-trap__why">Birinchi koʻpaytmaning oʻzi. GMAT yarim yoʻlda toʻxtagan
  javobni deyarli har doim variantlar orasiga qoʻyadi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">90 s</span></p>
  <div class="ps-stem__q">
    <p>A company bought 198 licenses for a software package at $25 per license. What
    was the total cost of the licenses?</p>
  </div>
  <ol class="ps-ch">
    <li>$4,900</li>
    <li>$4,950</li>
    <li>$4,975</li>
    <li>$5,000</li>
    <li>$5,050</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) $4,950</p>
      <p>198 × 25 = 200 × 25 − 2 × 25 = 5,000 − 50 = 4,950.</p>
      <p><b>$5,000</b> — 198 ni 200 ga yaxlitlab, tuzatishni unutgan javob.
      <b>$4,900</b> — tuzatishni ikki marta (2 × 50) ayirgan javob.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">$5,000</span>
  <span class="ps-trap__why">Yaxlitlash — boshlash uchun yaxshi, lekin javoblar bir-biriga
  yaqin boʻlsa, tuzatishni albatta qoʻshing yoki ayiring.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Hisoblashdan oldin <b>javoblarga qarang</b>:</p>
  <ol>
    <li>Javoblar bir-biridan uzoq boʻlsa — yaxlitlab taxmin qiling;</li>
    <li>yaqin boʻlsa — sonni qulay boʻlaklarga ajratib, aniq hisoblang;</li>
    <li>oxirgi raqamni tekshiring: 198 × 25 ning oxiri 0 bilan tugashi kerak.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">198 × 25 ≈ 5,000 — javob</p>
  <p class="pe-good">5,000 − 50 = 4,950</p>
  <p class="pe-fix__why">Yaxlitlagan boʻlsangiz, yaxlitlashning oʻzini qaytarib tuzating.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">48 × 25: 48 × 20 + 48 × 5 = 960 + 200</p>
  <p class="pe-good">48 × 25 = 48 ÷ 4 × 100 = 1,200</p>
  <p class="pe-fix__why">48 × 5 = 240, 200 emas — boʻlaklarga ajratganda har bir boʻlakni alohida tekshiring.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Vaqt boʻyicha eng katta xato — bitta qiyin savolga besh daqiqa sarflash. GMAT'da
  boʻlimni tugatmaslik ballni koʻproq tushiradi, shuning uchun 3 daqiqadan oshgan
  savolda eng ehtimoliy javobni belgilab, keyingisiga oʻting.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> What is 16 × 25?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">400 — 16 ÷ 4 = 4, 4 × 100 = 400.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> What is 999 × 7?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">6,993 — 1,000 × 7 − 7 = 7,000 − 7.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> What is 35 × 12?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">420 — 35 × 10 + 35 × 2 = 350 + 70.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> What is 0.125 × 64?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">8 — 0.125 = 1/8, demak 64 ÷ 8.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> A firm buys 24 train tickets at
  $45 each. What is the total cost?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">$1,080 — 24 × 45 = 24 × 40 + 24 × 5 = 960 + 120.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Problem Solving</b><span>besh variantli masala — Quant'ning yagona savol turi</span></li>
  <li><b>value</b><span>qiymat</span></li>
  <li><b>approximately</b><span>taxminan</span></li>
  <li><b>closest to</b><span>eng yaqin</span></li>
  <li><b>product</b><span>koʻpaytma</span></li>
  <li><b>sum</b><span>yigʻindi</span></li>
  <li><b>difference</b><span>ayirma</span></li>
  <li><b>per</b><span>har biri uchun</span></li>
  <li><b>license</b><span>litsenziya</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>21 savol, 45 daqiqa, 5 variant, kalkulyator yoʻq — bir savolga ~2 daqiqa.</li>
    <li>25 ga koʻpaytirish = 4 ga boʻlish va 100 ga koʻpaytirish.</li>
    <li>Qiyin sonni qulay boʻlaklarga ajrating: 15 = 10 + 5, 198 = 200 − 2.</li>
    <li>Avval javoblarga qarang: uzoq — taxmin qiling, yaqin — aniq hisoblang.</li>
    <li>Boʻlimni tugatish muhim: qotib qolgan savolda taxmin qilib, oldinga yuring.</li>
  </ul>
</div>
"""

GMAT2 = """
<h2>GMAT-2: Number Properties — Integers, Factors and Multiples</h2>

<p><i>Number properties</i> — GMAT Quant'ning eng koʻp sinaladigan mavzularidan biri.
Bu savollar hisoblashni emas, <mark>sonlar qanday tuzilganini</mark> tushunishni
tekshiradi: nimaga boʻlinadi, nimaning karralisi, nima <b>har doim</b> toʻgʻri.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li><i>factor</i> va <i>multiple</i> ni adashtirmaysiz;</li>
    <li>boʻlinish belgilarini (2, 3, 4, 5, 6, 8, 9, 10) bir qarashda qoʻllaysiz;</li>
    <li>sonning barcha boʻluvchilarini juftlab topasiz;</li>
    <li>oraliqdagi karralilar sonini sanaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Factor and multiple</span>
  <span class="pe-chip pe-chip--s">a</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--v">k</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">n</span>
</div>

<p>Agar <i>n</i> = <i>a</i> × <i>k</i> boʻlsa (hammasi butun son), <i>a</i> — <i>n</i>
ning <b>boʻluvchisi</b> (<i>factor</i>), <i>n</i> esa <i>a</i> ning <b>karralisi</b>
(<i>multiple</i>). 3 — 12 ning boʻluvchisi; 12 — 3 ning karralisi.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Eslab qolish usuli: boʻluvchi <b>kichik</b>, karrali <b>katta</b>. Sonning boʻluvchilari
  chekli (12 niki — 6 ta), karralilari esa cheksiz (12, 24, 36, …).
</div>

<h3>Boʻlinish belgilari</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Boʻluvchi</th><th>Belgi</th><th>Misol</th></tr>
  <tr><td>2</td><td class="pm-word__sym">oxirgi raqam juft</td><td>3,458</td></tr>
  <tr><td>3</td><td class="pm-word__sym">raqamlar yigʻindisi 3 ga boʻlinadi</td><td>4,521 (4+5+2+1 = 12)</td></tr>
  <tr><td>4</td><td class="pm-word__sym">oxirgi ikki raqam 4 ga boʻlinadi</td><td>7,316 (16)</td></tr>
  <tr><td>5</td><td class="pm-word__sym">oxiri 0 yoki 5</td><td>2,345</td></tr>
  <tr><td>6</td><td class="pm-word__sym">ham 2 ga, ham 3 ga</td><td>1,242</td></tr>
  <tr><td>8</td><td class="pm-word__sym">oxirgi uch raqam 8 ga boʻlinadi</td><td>5,120 (120)</td></tr>
  <tr><td>9</td><td class="pm-word__sym">raqamlar yigʻindisi 9 ga boʻlinadi</td><td>8,163 (18)</td></tr>
  <tr><td>10</td><td class="pm-word__sym">oxiri 0</td><td>4,560</td></tr>
</table></div>

<h3>Barcha boʻluvchilarni topish — juftlab</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">36 = 1 × 36 = 2 × 18 = 3 × 12 = 4 × 9 = 6 × 6</span>
    <span class="pm-solve__why">1 dan boshlab juftlarni yozamiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5 × ? — 36 ga boʻlinmaydi</span>
    <span class="pm-solve__why">6 × 6 dan keyin juftlar takrorlanadi — toʻxtaymiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">1, 2, 3, 4, 6, 9, 12, 18, 36 — 9 ta</span>
    <span class="pm-solve__why">6 ikki marta sanalmaydi, shuning uchun toq son</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Boʻluvchilar soni <b>toq</b> boʻlsa, son — toʻliq kvadrat (36, 49, 100). Qolgan barcha
  sonlarning boʻluvchilari juft-juft keladi.
</div>

<h3>Oraliqdagi karralilarni sanash</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">How many multiples of 7 are less than 100?</span>
    <span class="pm-solve__why">Eng katta karralini topamiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">100 ÷ 7 = 14.28… → 14 × 7 = 98</span>
    <span class="pm-solve__why">Butun qismini olamiz: 14</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">7, 14, …, 98 → 14 ta</span>
    <span class="pm-solve__why">Yuqoriga yaxlitlamang — 105 > 100</span>
  </div>
</div>

<h3>«Must be» — har doim toʻgʻri boʻlishi kerak</h3>

<p>«If <i>n</i> is divisible by both 6 and 4» degan shart <i>n</i> haqida faqat bitta
narsani kafolatlaydi: u 6 va 4 ning <b>eng kichik umumiy karralisi</b> — 12 ga boʻlinadi.
24 ga emas: <i>n</i> = 12 ham shartni bajaradi, lekin 24 ga boʻlinmaydi.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Must be true» savolida bitta <b>qarshi misol</b> variantni yoʻq qiladi. Eng kichik
  mos sonni (bu yerda 12) sinab koʻring — u koʻp variantni darrov chiqarib tashlaydi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>is divisible by</b><span>… ga qoldiqsiz boʻlinadi</span></li>
  <li><b>is a factor of</b><span>… ning boʻluvchisi</span></li>
  <li><b>is a multiple of</b><span>… ning karralisi</span></li>
  <li><b>must be a factor of n</b><span>har doim n ning boʻluvchisi boʻlishi shart</span></li>
  <li><b>positive integer</b><span>musbat butun son (1, 2, 3, …)</span></li>
  <li><b>how many … are there</b><span>nechta … bor — sanash savoli</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>How many positive integers less than 100 are multiples of 7?</p>
  </div>
  <ol class="ps-ch">
    <li>7</li>
    <li>13</li>
    <li>14</li>
    <li>15</li>
    <li>16</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 14</p>
      <p>100 ÷ 7 = 14.28…; eng katta karrali 14 × 7 = 98. Demak 7 dan 98 gacha 14 ta.</p>
      <p><b>15</b> — 14.28 ni yuqoriga yaxlitlagan javob; lekin 15 × 7 = 105, u 100 dan katta.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">15</span>
  <span class="ps-trap__why">Boʻlinmani yuqoriga yaxlitlash. Karralilarni sanaganda har doim
  pastga — butun qismini oling.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">90 s</span></p>
  <div class="ps-stem__q">
    <p>If <i>n</i> is a positive integer that is divisible by both 6 and 4, which of the
    following must be a factor of <i>n</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>8</li>
    <li>9</li>
    <li>12</li>
    <li>18</li>
    <li>24</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 12</p>
      <p>Eng kichik mos son: 6 va 4 ning EKUKi = 12. <i>n</i> = 12 ni sinaymiz: 12 ga
      boʻlinadi, 8, 9, 18, 24 ga esa boʻlinmaydi — ular «must be» emas.</p>
      <p><b>24</b> — 6 × 4 ni olgan javob. Koʻpaytma ikkalasiga boʻlinadi, lekin bu
      <i>n</i> haqida kafolat emas.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">24</span>
  <span class="ps-trap__why">Ikki sonning koʻpaytmasi — umumiy karrali, lekin eng kichigi
  emas. «Must» savolida eng kichik mos sonni sinang.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>«Must be» savolida <b>eng kichik mos sonni</b> sinang:</p>
  <ol>
    <li>shartni bajaradigan eng kichik sonni toping (bu yerda 12);</li>
    <li>har bir variantni shu son bilan tekshiring;</li>
    <li>bitta qarshi misol variantni yoʻq qiladi.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">12 is a factor of 3</p>
  <p class="pe-good">3 is a factor of 12</p>
  <p class="pe-fix__why">Boʻluvchi kichik son; katta son — karrali.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">36 ning boʻluvchilari: 10 ta (6 ni ikki marta sanab)</p>
  <p class="pe-good">9 ta</p>
  <p class="pe-fix__why">Toʻliq kvadratda oʻrtadagi juft (6 × 6) bitta boʻluvchi beradi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Integer» — butun son: manfiy, nol va musbat. Savolda «positive» soʻzi boʻlmasa,
  manfiy sonlar va 0 ham hisobga kiradi — buni keyingi darslarda koʻp ishlatamiz.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> How many positive factors does 48 have?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">10 — 1, 2, 3, 4, 6, 8, 12, 16, 24, 48.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> Is 4,512 divisible by 4?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ha — oxirgi ikki raqam 12, u 4 ga boʻlinadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> What is the smallest multiple of 9 that is greater than 100?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">108 — 9 × 11 = 99 hali 100 dan kichik, 9 × 12 = 108.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> How many multiples of 5 are there from 20 to 60, inclusive?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">9 — (60 − 20) ÷ 5 + 1. «Inclusive» — ikkala chet ham sanaladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> A shop packs 150 items into boxes
  of 12. How many full boxes does it fill?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">12 — 12 × 12 = 144; qolgan 6 ta mahsulot qutini toʻldirmaydi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>integer</b><span>butun son (manfiy, 0, musbat)</span></li>
  <li><b>positive integer</b><span>musbat butun son</span></li>
  <li><b>factor / divisor</b><span>boʻluvchi</span></li>
  <li><b>multiple</b><span>karrali</span></li>
  <li><b>divisible by</b><span>… ga qoldiqsiz boʻlinadi</span></li>
  <li><b>perfect square</b><span>toʻliq kvadrat</span></li>
  <li><b>inclusive</b><span>chetlari bilan birga</span></li>
  <li><b>must be</b><span>har doim boʻlishi shart</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Boʻluvchi kichik, karrali katta; boʻluvchilar chekli, karralilar cheksiz.</li>
    <li>Boʻlinish belgilari: 3 va 9 — raqamlar yigʻindisi, 4 — oxirgi ikki raqam, 8 — oxirgi uch.</li>
    <li>Boʻluvchilarni juftlab toping; toq son boʻlsa — toʻliq kvadrat.</li>
    <li>Karralilarni sanashda boʻlinmaning butun qismini oling, yuqoriga yaxlitlamang.</li>
    <li>«Must be» savolida eng kichik mos sonni sinang.</li>
  </ul>
</div>
"""

GMAT3 = """
<h2>GMAT-3: Primes, Prime Factorization, GCD and LCM</h2>

<p>Har bir butun son — tub sonlardan qurilgan. Sonni <mark>tub koʻpaytuvchilarga</mark>
ajratsangiz, uning boʻluvchilari, EKUBi va EKUKi bir necha soniyada koʻrinadi. GMAT bu
gʻoyani jadval, avtobus va qadoqlash masalalariga oʻrab beradi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>30 gacha boʻlgan tub sonlarni yoddan bilasiz;</li>
    <li>sonni tub koʻpaytuvchilarga ajratasiz (<i>prime factorization</i>);</li>
    <li>boʻluvchilar sonini formula bilan topasiz;</li>
    <li>EKUB (<i>GCD</i>) va EKUK (<i>LCM</i>) ni masalada tanib olasiz.</li>
  </ul>
</div>

<h3>Tub son nima</h3>

<p><b>Tub son</b> (<i>prime number</i>) — aynan ikkita musbat boʻluvchisi bor son: 1 va
oʻzi. 30 gacha: <b>2, 3, 5, 7, 11, 13, 17, 19, 23, 29</b> — 10 ta.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikki tuzoq: <b>1 tub son emas</b> (uning bitta boʻluvchisi bor), <b>2 — yagona juft tub
  son</b>. GMAT «sum of two primes is odd» kabi savollarda aynan 2 ni yashiradi.
</div>

<h3>Tub koʻpaytuvchilarga ajratish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">360 = 36 × 10</span>
    <span class="pm-solve__why">Qulay boʻlaklarga ajratamiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= (2 × 2 × 3 × 3) × (2 × 5)</span>
    <span class="pm-solve__why">Har bir boʻlakni oxirigacha</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">360 = 2<sup>3</sup> × 3<sup>2</sup> × 5</span>
    <span class="pm-solve__why">Bir xil tub sonlarni daraja qilib yigʻamiz</span>
  </div>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Number of factors</span>
  <span class="pe-chip pe-chip--s">(a + 1)</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--v">(b + 1)</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--o">(c + 1)</span>
</div>

<p>Agar <i>n</i> = <i>p</i><sup>a</sup> × <i>q</i><sup>b</sup> × <i>r</i><sup>c</sup>
boʻlsa, uning musbat boʻluvchilari soni (a + 1)(b + 1)(c + 1). 360 uchun:
(3 + 1)(2 + 1)(1 + 1) = 24 ta boʻluvchi — bittalab sanamasdan.</p>

<h3>EKUB va EKUK</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">84 = 2<sup>2</sup> × 3 × 7; 120 = 2<sup>3</sup> × 3 × 5</span>
    <span class="pm-solve__why">Ikkalasini ajratamiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">GCD = 2<sup>2</sup> × 3 = 12</span>
    <span class="pm-solve__why">Umumiy tub sonlar, <b>kichik</b> darajasi bilan</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">LCM = 2<sup>3</sup> × 3 × 5 × 7 = 840</span>
    <span class="pm-solve__why">Barcha tub sonlar, <b>katta</b> darajasi bilan</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Tekshiruv: <b>GCD × LCM = ikki sonning koʻpaytmasi</b>. 12 × 840 = 10,080 va
  84 × 120 = 10,080 ✓. Bu tenglik faqat ikki son uchun ishlaydi.
</div>

<h3>Masalada qaysi biri kerak?</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Masala nimani soʻraydi</th><th>Kerakli</th></tr>
  <tr><td>«next time together», «at the same time again», «every … and every …»</td><td class="pm-word__sym">LCM</td></tr>
  <tr><td>«largest equal groups», «biggest square tile», «split evenly into the most»</td><td class="pm-word__sym">GCD</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Savol <b>vaqtda takrorlanish</b> haqida boʻlsa — EKUK; <b>boʻlib tashlash</b> haqida
  boʻlsa — EKUB. «Qachon yana birga» katta son beradi, «eng katta teng boʻlak» kichik son beradi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>prime number</b><span>tub son</span></li>
  <li><b>prime factorization</b><span>tub koʻpaytuvchilarga ajratish</span></li>
  <li><b>greatest common divisor (GCD)</b><span>eng katta umumiy boʻluvchi (EKUB)</span></li>
  <li><b>least common multiple (LCM)</b><span>eng kichik umumiy karrali (EKUK)</span></li>
  <li><b>distinct prime factors</b><span>turli tub boʻluvchilar — har biri bir marta sanaladi</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>What is the greatest common divisor of 84 and 120?</p>
  </div>
  <ol class="ps-ch">
    <li>6</li>
    <li>12</li>
    <li>24</li>
    <li>42</li>
    <li>840</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 12</p>
      <p>84 = 2<sup>2</sup> × 3 × 7, 120 = 2<sup>3</sup> × 3 × 5. Umumiy: 2<sup>2</sup> × 3 = 12.</p>
      <p><b>24</b> — 2 ning <i>katta</i> darajasini (2<sup>3</sup>) olgan javob; 24 esa 84 ni
      boʻlmaydi. <b>840</b> — EKUK.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">840</span>
  <span class="ps-trap__why">EKUB oʻrniga EKUK. EKUB ikki sonning kichigidan katta
  boʻlolmaydi — 840 darrov chiqarib tashlanadi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">90 s</span></p>
  <div class="ps-stem__q">
    <p>Two shuttle buses leave a terminal at 8:00 a.m. One returns to the terminal every
    12 minutes and the other every 18 minutes. At what time will both buses next be at
    the terminal at the same time?</p>
  </div>
  <ol class="ps-ch">
    <li>8:30 a.m.</li>
    <li>8:36 a.m.</li>
    <li>8:54 a.m.</li>
    <li>9:00 a.m.</li>
    <li>11:36 a.m.</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 8:36 a.m.</p>
      <p>«At the same time» — EKUK. 12 = 2<sup>2</sup> × 3, 18 = 2 × 3<sup>2</sup>;
      EKUK = 2<sup>2</sup> × 3<sup>2</sup> = 36 daqiqa. 8:00 + 36 daqiqa = 8:36.</p>
      <p><b>11:36</b> — 12 × 18 = 216 daqiqani olgan javob: umumiy karrali, lekin eng
      kichigi emas.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">11:36 a.m.</span>
  <span class="ps-trap__why">Ikki sonni koʻpaytirish faqat ularning umumiy boʻluvchisi
  boʻlmasa EKUK beradi. 12 va 18 ning umumiy boʻluvchisi 6.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>EKUK/EKUB savolida:</p>
  <ol>
    <li>har bir sonni tub koʻpaytuvchilarga ajrating;</li>
    <li>EKUB — umumiylarini kichik daraja bilan, EKUK — hammasini katta daraja bilan oling;</li>
    <li>javobni mantiq bilan tekshiring: EKUB ≤ kichik son, EKUK ≥ katta son.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">1 — eng kichik tub son</p>
  <p class="pe-good">2 — eng kichik tub son</p>
  <p class="pe-fix__why">Tub sonning aynan ikkita boʻluvchisi bor; 1 ning bittasi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">LCM(12, 18) = 12 × 18 = 216</p>
  <p class="pe-good">LCM(12, 18) = 36</p>
  <p class="pe-fix__why">Umumiy koʻpaytuvchi (6) ikki marta hisobga kirib ketdi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Distinct prime factors» — <b>turli</b> tub boʻluvchilar. 360 da ular uchta: 2, 3 va 5.
  2 uch marta qatnashsa ham, bir marta sanaladi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> What is the prime factorization of 90?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">2 × 3<sup>2</sup> × 5.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> How many prime numbers are between 20 and 40?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">4 — 23, 29, 31, 37.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> How many positive factors does 72 have?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">12 — 72 = 2<sup>3</sup> × 3<sup>2</sup>, (3 + 1)(2 + 1) = 12.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> What is the LCM of 8 and 14?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">56 — 2<sup>3</sup> × 7.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> A floor measures 24 by 36 feet and will be
  covered with identical square tiles, none cut. What is the largest possible side length of a tile?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">12 feet — EKUB(24, 36) = 12. «Eng katta teng boʻlak» — EKUB.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>prime number</b><span>tub son</span></li>
  <li><b>composite number</b><span>murakkab son</span></li>
  <li><b>prime factorization</b><span>tub koʻpaytuvchilarga ajratish</span></li>
  <li><b>distinct</b><span>turli, takrorlanmaydigan</span></li>
  <li><b>greatest common divisor</b><span>EKUB</span></li>
  <li><b>least common multiple</b><span>EKUK</span></li>
  <li><b>exponent</b><span>daraja koʻrsatkichi</span></li>
  <li><b>terminal</b><span>bekat, terminal</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>30 gacha tub sonlar: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29; 1 tub emas, 2 — yagona juft tub.</li>
    <li>Boʻluvchilar soni: darajalarga 1 qoʻshib, koʻpaytiring.</li>
    <li>EKUB — umumiy, kichik daraja; EKUK — hammasi, katta daraja.</li>
    <li>«Yana birga» — EKUK; «eng katta teng boʻlak» — EKUB.</li>
    <li>GCD × LCM = ikki sonning koʻpaytmasi — tekshirish uchun.</li>
  </ul>
</div>
"""

GMAT4 = """
<h2>GMAT-4: Odd and Even, Positive and Negative</h2>

<p>Bu mavzudagi savollarda koʻpincha <mark>bitta ham son berilmaydi</mark>: faqat
«<i>n</i> is odd», «<i>xy</i> &lt; 0». Javob hisobdan emas, qoidalardan chiqadi — va
qoidalarni bilsangiz, bunday savol 40 soniyada yechiladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>juft/toq sonlar qoʻshilganda va koʻpaytirilganda nima boʻlishini bilasiz;</li>
    <li>ishoralar qoidasini koʻpaytma va boʻlinmada qoʻllaysiz;</li>
    <li>«must be» savolini sonlar qoʻyib tekshirasiz — jumladan 0 va manfiy sonlar bilan;</li>
    <li>0 juft son ekanini unutmaysiz.</li>
  </ul>
</div>

<h3>Juft va toq — qoʻshish va koʻpaytirish</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Amal</th><th>Natija</th><th>Misol</th></tr>
  <tr><td>juft ± juft</td><td class="pm-word__sym">juft</td><td>4 + 6 = 10</td></tr>
  <tr><td>toq ± toq</td><td class="pm-word__sym">juft</td><td>3 + 5 = 8</td></tr>
  <tr><td>juft ± toq</td><td class="pm-word__sym">toq</td><td>4 + 5 = 9</td></tr>
  <tr><td>juft × istalgan</td><td class="pm-word__sym">juft</td><td>4 × 7 = 28</td></tr>
  <tr><td>toq × toq</td><td class="pm-word__sym">toq</td><td>3 × 5 = 15</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Koʻpaytmada bitta juft son boʻlsa, butun koʻpaytma juft. Shuning uchun <b>2<i>n</i> har
  doim juft, 2<i>n</i> + 1 har doim toq</b> — <i>n</i> qanday butun son boʻlmasin.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>0 — juft son</b>: u 2 ga qoldiqsiz boʻlinadi. Bizda koʻpchilik 0 ni «na juft, na toq»
  deb oʻylaydi — GMAT shu xatoga ishonib savol tuzadi.
</div>

<h3>Musbat va manfiy — ishoralar qoidasi</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Koʻpaytma yoki boʻlinma</th><th>Natija</th></tr>
  <tr><td>(+)(+), (−)(−)</td><td class="pm-word__sym">musbat</td></tr>
  <tr><td>(+)(−)</td><td class="pm-word__sym">manfiy</td></tr>
  <tr><td>manfiy koʻpaytuvchilar soni juft</td><td class="pm-word__sym">musbat</td></tr>
  <tr><td>manfiy koʻpaytuvchilar soni toq</td><td class="pm-word__sym">manfiy</td></tr>
</table></div>

<p>Bundan ikki muhim xulosa: <i>xy</i> &lt; 0 boʻlsa, <i>x</i> va <i>y</i> <b>qarama-qarshi
ishorali</b>; <i>x</i><sup>2</sup> esa hech qachon manfiy emas (<i>x</i><sup>2</sup> ≥ 0).</p>

<h3>Sonlar qoʻyib tekshirish — barcha turdagi sonlar bilan</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">«If n is an integer, is n<sup>2</sup> &gt; n?»</span>
    <span class="pm-solve__why">Faqat musbat sonni sinash yetmaydi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">n = 3: 9 &gt; 3 ✓; n = −2: 4 &gt; −2 ✓</span>
    <span class="pm-solve__why">Musbat va manfiy — ikkalasida ham ha</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">n = 0 yoki 1: 0 = 0, 1 = 1 ✗</span>
    <span class="pm-solve__why">0 va 1 qoidani buzdi — «har doim» emas</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Tekshirish roʻyxati: <b>manfiy son, 0, 1, kasr</b>. Koʻp oʻquvchi faqat 2 va 3 ni sinab,
  «har doim toʻgʻri» deb xulosa qiladi. GMAT ataylab 0 yoki manfiy sonda buziladigan
  variant qoʻyadi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Ketma-ket butun sonlar</b> (<i>consecutive integers</i>) juft va toq navbat bilan keladi:
  ikkita ketma-ket sonning koʻpaytmasi har doim juft, uchtasiniki esa har doim 6 ga
  boʻlinadi. «n(n + 1)» koʻrsangiz — bu juft son.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>which of the following must be odd</b><span>qaysi biri har doim toq</span></li>
  <li><b>could be even</b><span>juft boʻlishi mumkin — bitta misol yetarli</span></li>
  <li><b>xy &lt; 0</b><span>x va y qarama-qarshi ishorali</span></li>
  <li><b>nonnegative</b><span>manfiy emas: 0 yoki musbat</span></li>
  <li><b>consecutive integers</b><span>ketma-ket butun sonlar</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>If <i>n</i> is an integer, which of the following must be odd?</p>
  </div>
  <ol class="ps-ch">
    <li>3<i>n</i></li>
    <li><i>n</i> + 1</li>
    <li><i>n</i><sup>2</sup></li>
    <li>2<i>n</i> + 1</li>
    <li>2<i>n</i> + 2</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: D) 2<i>n</i> + 1</p>
      <p>2<i>n</i> har doim juft, juft + 1 — toq. Qolganlarini <i>n</i> = 2 (yoki 1) buzadi:
      3 × 2 = 6, 1 + 1 = 2, 2<sup>2</sup> = 4 — juft. 2<i>n</i> + 2 esa har doim juft.</p>
      <p><b>n<sup>2</sup></b> — faqat toq <i>n</i> ni sinagan oʻquvchining javobi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">3<i>n</i></span>
  <span class="ps-trap__why">3 toq, lekin koʻpaytma <i>n</i> ga bogʻliq: <i>n</i> juft boʻlsa,
  3<i>n</i> ham juft. «Must» — har qanday <i>n</i> da.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">90 s</span></p>
  <div class="ps-stem__q">
    <p>If <i>xy</i> &lt; 0 and <i>yz</i> &gt; 0, which of the following must be true?</p>
  </div>
  <ol class="ps-ch">
    <li><i>x</i> &gt; 0</li>
    <li><i>y</i> &lt; 0</li>
    <li><i>xz</i> &lt; 0</li>
    <li><i>xyz</i> &gt; 0</li>
    <li><i>x</i> + <i>z</i> = 0</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) <i>xz</i> &lt; 0</p>
      <p><i>yz</i> &gt; 0 — <i>y</i> va <i>z</i> bir xil ishorali. <i>xy</i> &lt; 0 — <i>x</i>
      ning ishorasi <i>y</i> ga, demak <i>z</i> ga ham qarama-qarshi. Shuning uchun
      <i>xz</i> &lt; 0.</p>
      <p>Tekshiruv: <i>x</i> = 1, <i>y</i> = −1, <i>z</i> = −2 — A) toʻgʻri, lekin <i>x</i> = −1,
      <i>y</i> = 1, <i>z</i> = 2 boʻlsa A) notoʻgʻri. «Must» faqat C).</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val"><i>x</i> &gt; 0</span>
  <span class="ps-trap__why">Bitta misolda toʻgʻri chiqqan variant. Ishoralar savolida faqat
  <b>nisbiy</b> ishora maʼlum, haqiqiy ishora emas.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>«Must be» savolida <b>buzishga</b> urining:</p>
  <ol>
    <li>har variant uchun uni notoʻgʻri qiladigan son qidiring;</li>
    <li>roʻyxat boʻyicha sinang: juft, toq, manfiy, 0, 1;</li>
    <li>hech qanday son buzolmagan variant — javob.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">0 — na juft, na toq</p>
  <p class="pe-good">0 — juft</p>
  <p class="pe-fix__why">0 = 2 × 0: u 2 ga qoldiqsiz boʻlinadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">n<sup>2</sup> &gt; n — har doim (2 va 3 da toʻgʻri)</p>
  <p class="pe-good">n = 0 va n = 1 da notoʻgʻri</p>
  <p class="pe-fix__why">Faqat «qulay» sonlarni sinash — eng koʻp uchraydigan xato.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> Is the sum of two odd integers odd or even?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Even — toq + toq = juft (3 + 5 = 8).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> Is the product of an even integer and an odd integer odd or even?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Even — bitta juft koʻpaytuvchi yetarli.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> Is the product of five negative numbers positive or negative?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Negative — manfiy koʻpaytuvchilar soni toq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> If <i>a</i> &lt; 0, is <i>a</i><sup>3</sup> positive or negative?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Negative — uchta manfiy koʻpaytuvchi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> A team scored an odd number of points
  in each of 4 games. Is its total for the 4 games odd or even?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Even — toʻrtta toq sonni ikki juftga boʻlib qoʻshing: toq + toq = juft.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>odd</b><span>toq</span></li>
  <li><b>even</b><span>juft</span></li>
  <li><b>positive</b><span>musbat</span></li>
  <li><b>negative</b><span>manfiy</span></li>
  <li><b>nonnegative</b><span>manfiy emas (0 yoki musbat)</span></li>
  <li><b>consecutive</b><span>ketma-ket</span></li>
  <li><b>must be true</b><span>har doim toʻgʻri</span></li>
  <li><b>could be true</b><span>toʻgʻri boʻlishi mumkin</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Bitta juft koʻpaytuvchi — koʻpaytma juft; 2n juft, 2n + 1 toq.</li>
    <li>0 — juft son.</li>
    <li>Manfiylar soni juft — musbat, toq — manfiy; x<sup>2</sup> ≥ 0.</li>
    <li>xy &lt; 0 — qarama-qarshi ishora; yz &gt; 0 — bir xil ishora.</li>
    <li>«Must be» — variantni manfiy son, 0 va 1 bilan buzishga urining.</li>
  </ul>
</div>
"""

GMAT5 = """
<h2>GMAT-5: Percentages and Percent Change</h2>

<p>Foizlar — GMAT'ning biznes tili: narx, daromad, chegirma, oʻsish. Mexanikasi oddiy,
lekin savollar ikki joyda tuzoq qoʻyadi: <mark>foiz qaysi sondan olinayotgani</mark> va
<mark>ketma-ket oʻzgarishlar</mark>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>qism, foiz va butunni bitta tenglama bilan topasiz;</li>
    <li>foiz oʻzgarishini <b>eski</b> qiymatga nisbatan hisoblaysiz;</li>
    <li>ketma-ket oʻzgarishlarni koʻpaytirasiz, qoʻshmaysiz;</li>
    <li>oʻzgarishdan keyingi qiymatdan boshlangʻichini topasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Percent change</span>
  <span class="pe-chip pe-chip--s">change</span>
  <span class="pe-op">÷</span>
  <span class="pe-chip pe-chip--v">original</span>
  <span class="pe-op">× 100</span>
</div>

<h3>Bitta tenglama: qism = foiz × butun</h3>

<p>«15% of 260» — 0.15 × 260 = 39. «45 is what percent of 250» — 45 ÷ 250 = 0.18 = 18%.
Foizni har doim <b>oʻnli kasrga</b> aylantirib ishlang: 15% → 0.15, 120% → 1.2.</p>

<h3>Foiz oʻzgarishi — eski qiymatga nisbatan</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Price: $800 → $1,000</span>
    <span class="pm-solve__why">Eski 800, yangi 1,000</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">change = 1,000 − 800 = 200</span>
    <span class="pm-solve__why">Avval oʻzgarishni topamiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">200 ÷ 800 = 0.25 → 25% increase</span>
    <span class="pm-solve__why">Eski qiymatga boʻlamiz, yangisiga emas</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  800 dan 1,000 ga — 25% oʻsish; 1,000 dan 800 ga — 20% kamayish. Bir xil 200, lekin
  <b>baza boshqa</b>. «Increase by» va «decrease by» savolida har doim boshlangʻich
  qiymatga boʻling.
</div>

<h3>Ketma-ket oʻzgarishlar — koʻpaytiring</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">−20%, keyin +20%</span>
    <span class="pm-solve__why">Har biri koʻpaytuvchi: 0.8 va 1.2</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">0.8 × 1.2 = 0.96</span>
    <span class="pm-solve__why">Ikkinchi foiz yangi bazadan olinadi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">96% of the original → 4% decrease</span>
    <span class="pm-solve__why">«Qaytib 100% boʻldi» — tuzoq</span>
  </div>
</div>

<h3>Teskari foiz: oʻzgargandan keyin — boshlangʻichi</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">After a 25% increase, the price is $150</span>
    <span class="pm-solve__why">Yangi = 1.25 × eski</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">eski = 150 ÷ 1.25 = 120</span>
    <span class="pm-solve__why">Boʻlamiz; 150 ning 25% ini ayirish (112.5) — xato</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Foiz va foiz punkti</b> boshqa narsa: stavka 5% dan 6% ga chiqsa, bu 1 foiz punktga
  (<i>percentage point</i>) oʻsish, lekin 20% oʻsish (1 ÷ 5). GMAT ikkalasini ham ishlatadi.
</div>

<h3>Foyda, xarajat va foizning foizi</h3>

<p>Biznes savollarida foiz koʻpincha <b>ikki bosqichli</b> boʻladi: «40% of the employees
work remotely; 30% of them live outside the city». Ikkinchi foiz birinchi guruhdan olinadi:
0.4 × 0.3 = 0.12, yaʼni jami xodimlarning 12%. Foyda (<i>profit</i>) masalasida esa savol
qaysi bazani nazarda tutganini aniqlang: «profit as a percent of cost» — foyda ÷ xarajat,
«as a percent of revenue» — foyda ÷ tushum. $15 ga olib $18 ga sotilgan mahsulotda foyda
xarajatning 20% i, lekin tushumning atigi 16⅔% i.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Of them», «of those», «of the remaining» — bu soʻzlar bazani <b>oʻzgartiradi</b>. Ular
  koʻrinsa, oldingi natija yangi butun boʻladi. Har bir foizni oʻnli kasrga aylantirib,
  ketma-ket koʻpaytiring — bu ikki bosqichli savolni bir qatorga aylantiradi. Javobni esa doim asl savol soʻragan baza bilan solishtirib tekshiring.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>by what percent did … increase</b><span>necha foizga oshdi — eski qiymatga boʻling</span></li>
  <li><b>is what percent of</b><span>… ning necha foizi</span></li>
  <li><b>was what percent of its value at the start</b><span>boshlangʻich qiymatning necha foizi — yangi ÷ eski</span></li>
  <li><b>percentage point</b><span>foiz punkti — ikki foiz orasidagi ayirma</span></li>
  <li><b>marked up / discounted</b><span>narx oshirilgan / chegirma qilingan</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>The price of a laptop rose from $800 to $1,000. By what percent did the price
    increase?</p>
  </div>
  <ol class="ps-ch">
    <li>20%</li>
    <li>25%</li>
    <li>80%</li>
    <li>120%</li>
    <li>125%</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 25%</p>
      <p>200 ÷ 800 = 0.25.</p>
      <p><b>20%</b> — yangi qiymatga (1,000) boʻlingan. <b>125%</b> — yangi narx eskisining
      necha foizi ekanini topgan javob, oʻsish emas.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">20%</span>
  <span class="ps-trap__why">Oʻzgarishni <b>yangi</b> qiymatga boʻlish. Oʻsish savolida
  har doim eski qiymat — baza.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>The value of a stock fell by 20% in January and then rose by 20% in February. Its
    value at the end of February was what percent of its value at the start of January?</p>
  </div>
  <ol class="ps-ch">
    <li>80%</li>
    <li>96%</li>
    <li>100%</li>
    <li>104%</li>
    <li>120%</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 96%</p>
      <p>0.8 × 1.2 = 0.96. 100 dan boshlab tekshiring: 100 → 80 → 80 × 1.2 = 96 ✓</p>
      <p><b>100%</b> — −20% va +20% ni qoʻshib, nolga tenglagan javob. Ikkinchi 20%
      kichikroq bazadan (80) olingan.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">100%</span>
  <span class="ps-trap__why">Ketma-ket foizlar qoʻshilmaydi. Har bir oʻzgarish oldingisining
  natijasiga qoʻllanadi — koʻpaytiring.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Foiz masalasida boshlangʻich qiymatni <b>100</b> deb oling:</p>
  <ol>
    <li>har bir oʻzgarishni shu 100 ga ketma-ket qoʻllang;</li>
    <li>oxirgi son — boshlangʻichning necha foizi ekanini darrov koʻrsatadi;</li>
    <li>sonlar haqiqiy boʻlmasa ham, foizlar oʻzgarmaydi.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">$800 → $1,000: 200 ÷ 1,000 = 20%</p>
  <p class="pe-good">200 ÷ 800 = 25%</p>
  <p class="pe-fix__why">Oʻsish eski qiymatga nisbatan oʻlchanadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">After +25% the price is $150, so the original was 150 − 37.5 = $112.50</p>
  <p class="pe-good">150 ÷ 1.25 = $120</p>
  <p class="pe-fix__why">25% yangi narxdan emas, eski narxdan olingan edi — boʻlish kerak.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> What is 15% of 260?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">39 — 10% = 26, 5% = 13.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> 45 is what percent of 250?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">18% — 45 ÷ 250 = 0.18.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> A $70 jacket is discounted by 10%. What is the sale price?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">$63 — 0.9 × 70.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> After a 25% increase, a price is $150. What was the original price?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">$120 — 150 ÷ 1.25.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> A company's revenue rose from
  $2.5 million to $3 million. By what percent did revenue increase?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">20% — 0.5 ÷ 2.5 = 0.2.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>percent change</b><span>foiz oʻzgarishi</span></li>
  <li><b>original value</b><span>boshlangʻich qiymat</span></li>
  <li><b>increase / decrease</b><span>oshish / kamayish</span></li>
  <li><b>discount</b><span>chegirma</span></li>
  <li><b>markup</b><span>narx ustamasi</span></li>
  <li><b>revenue</b><span>tushum, daromad</span></li>
  <li><b>percentage point</b><span>foiz punkti</span></li>
  <li><b>successive</b><span>ketma-ket</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Qism = foiz × butun; foizni oʻnli kasr bilan yozing.</li>
    <li>Foiz oʻzgarishi = oʻzgarish ÷ <b>eski</b> qiymat.</li>
    <li>Ketma-ket foizlar koʻpaytiriladi: −20% va +20% → 96%.</li>
    <li>Oʻzgargandan keyingi qiymatdan boshlangʻichi — boʻlish bilan topiladi.</li>
    <li>Boshlangʻich qiymatni 100 deb olish — foiz masalasining eng tez usuli.</li>
  </ul>
</div>
"""

TUTORIALS = [
    {
        "title": "GMAT-1: The Quant Section and Arithmetic Without a Calculator",
        "category": "math", "order": 1,
        "summary": "GMAT Quant boʻlimining tuzilishi va kalkulyatorsiz tez hisoblash: 25 ga koʻpaytirish, sonni boʻlaklarga ajratish, javoblarga qarab taxmin qilish.",
        "stories": ["The Invoice Nobody Checked"],
        "content": GMAT1,
    },
    {
        "title": "GMAT-2: Number Properties — Integers, Factors and Multiples",
        "category": "math", "order": 2,
        "summary": "Boʻluvchi va karrali, boʻlinish belgilari, boʻluvchilarni juftlab topish va «must be» savollarini eng kichik mos son bilan yechish.",
        "stories": ["Twelve to a Carton"],
        "content": GMAT2,
    },
    {
        "title": "GMAT-3: Primes, Prime Factorization, GCD and LCM",
        "category": "math", "order": 3,
        "summary": "Tub sonlar, tub koʻpaytuvchilarga ajratish, boʻluvchilar soni formulasi va masalada EKUB yoki EKUK kerakligini tanib olish.",
        "stories": ["When the Two Machines Stop Together"],
        "content": GMAT3,
    },
    {
        "title": "GMAT-4: Odd and Even, Positive and Negative",
        "category": "math", "order": 4,
        "summary": "Juft-toq va ishoralar qoidalari, 0 ning juftligi va «must be» savolini manfiy son, 0 va 1 bilan buzib tekshirish.",
        "stories": ["Red Numbers on the Ledger"],
        "content": GMAT4,
    },
    {
        "title": "GMAT-5: Percentages and Percent Change",
        "category": "math", "order": 5,
        "summary": "Foiz oʻzgarishini eski qiymatga nisbatan hisoblash, ketma-ket foizlarni koʻpaytirish va oʻzgargan narxdan boshlangʻichini topish.",
        "stories": ["Up Twenty, Down Twenty"],
        "content": GMAT5,
    },
]
