# -*- coding: utf-8 -*-
"""Prime GMAT — GMAT-16 … GMAT-20: overlapping sets, then the algebra block —
linear equations and systems, inequalities and absolute value, quadratics, functions.

Written with STYLE_GUIDE_PRIME_GMAT.md (on top of STYLE_GUIDE_PRIME_SAT.md) ·
lesson list in toc_prime_gmat.txt. Exam English in the stems, Uzbek for the teaching.
Five answer choices, no calculator, no geometry, no data sufficiency.

Import:
    python manage.py import_tutorials tutorial/management/commands/_tutorials_prime_gmat_16_20.py --author=prime
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

GMAT16 = """
<h2>GMAT-16: Overlapping Sets and Venn Tables</h2>

<p>«60 xodim ingliz tilini, 45 tasi rus tilini biladi, 20 tasi ikkalasini» — bu
kesishuvchi toʻplamlar masalasi. Asosiy xavf — <mark>ikki marta sanash</mark>: ikkala
tilni biladiganlar ham 60 ning ichida, ham 45 ning ichida. Bu darsda shu ikki marta
sanalganlarni bitta formula va bitta jadval bilan toʻgʻri hisoblashni oʻrganamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>ikki toʻplam formulasini qoʻllaysiz: jami = A + B − ikkalasi + hech biri;</li>
    <li>ikki xususiyatli masalani 2 × 2 jadval (<i>double-set matrix</i>) bilan yechasiz;</li>
    <li>kesishmaning eng kichik va eng katta qiymatini topasiz;</li>
    <li>uch toʻplamli masalada «aynan ikkitasi» va «uchalasi»ni farqlaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Two sets</span>
  <span class="pe-chip pe-chip--o">total</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">A + B</span>
  <span class="pe-op">−</span>
  <span class="pe-chip pe-chip--v">both</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">neither</span>
</div>

<h3>Ikki toʻplam — formula</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">100 xodim: ingliz 60, rus 45, ikkalasi 20</span>
    <span class="pm-solve__why">Hech birini bilmaydiganlar nechta?</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Kamida bittasini biladi: 60 + 45 − 20 = 85</span>
    <span class="pm-solve__why">«Ikkalasi» ikki marta sanaldi — bir marta ayiramiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Hech biri: 100 − 85 = 15</span>
    <span class="pm-solve__why">Jamidan birlashmani ayiramiz</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Faqat ingliz tili» (<i>only English</i>) va «ingliz tili» — har xil son. 60 kishining 20 tasi
  rus tilini ham biladi, demak <b>faqat</b> ingliz tilini biladiganlar 60 − 20 = 40. Savolda
  «only» soʻzini koʻrsangiz, kesishmani ayiring.
</div>

<h3>Ikki xususiyat — 2 × 2 jadval</h3>

<p>200 nomzodning 120 tasida ish tajribasi bor, 90 tasida magistr diplomi bor, 50 tasida
ikkalasi bor. Jadvalda har bir katak — bitta guruh, har bir qator va ustun yigʻindisi —
chetdagi «Jami»:</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th></th><th>Diplom bor</th><th>Diplom yoʻq</th><th>Jami</th></tr>
  <tr><td>Tajriba bor</td><td class="pm-word__sym">50</td><td class="pm-word__sym">70</td><td>120</td></tr>
  <tr><td>Tajriba yoʻq</td><td class="pm-word__sym">40</td><td class="pm-word__sym">40</td><td>80</td></tr>
  <tr><td>Jami</td><td>90</td><td>110</td><td>200</td></tr>
</table></div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Maʼlum: 50, jami 120, jami 90, umumiy 200</span>
    <span class="pm-solve__why">Toʻrtta son jadvalni toʻliq aniqlaydi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">120 − 50 = 70; 90 − 50 = 40; 200 − 120 = 80</span>
    <span class="pm-solve__why">Har bir qator va ustun oʻz yigʻindisiga teng boʻlishi kerak</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Ikkalasi ham yoʻq: 80 − 40 = 40</span>
    <span class="pm-solve__why">Formula bilan ham: 200 − (120 + 90 − 50) = 40 ✓</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Ikki xil <b>ha/yoʻq</b> xususiyat boʻlsa (erkak/ayol va MBA bor/yoʻq, savdo boʻlimi va
  masofadan ishlash) — jadval chizing. Formula «ikkalasi» va «hech biri» uchun qulay,
  jadval esa «MBA'si yoʻq erkaklar» kabi har qanday katakni beradi.
</div>

<h3>Kesishmaning eng kichik va eng katta qiymati</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">100 kishi: A — 65, B — 55. Ikkalasi?</span>
    <span class="pm-solve__why">Aniq son yoʻq — oraliq bor</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Eng kami: 65 + 55 − 100 = 20</span>
    <span class="pm-solve__why">Hamma kamida bittasida, «hech biri» = 0 boʻlganda</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Eng koʻpi: 55</span>
    <span class="pm-solve__why">Kichik toʻplam butunlay kattasining ichida boʻlganda</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Uch toʻplam</b> uchun: jami = A + B + C − (aynan ikkitasidagilar) − 2 × (uchalasidagilar)
  + hech biri. Nega 2 marta? Uchala toʻplamdagi odam A + B + C da <b>uch marta</b> sanalgan —
  bir marta qolishi uchun ikki marta ayiriladi. 100 kishi: 50, 40, 30; aynan ikkitasida 15,
  uchalasida 5 → kamida bittasida 120 − 15 − 10 = 95, hech birida 5.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Toʻplam savollarida «or» soʻziga ehtiyot boʻling: «speak English or Russian» odatda
  <b>kamida bittasi</b> degani — ikkalasini biladiganlar ham kiradi. «Either … or …, but not both»
  desa — <b>aynan bittasi</b>. Bu farq javobni kesishma hajmicha oʻzgartiradi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>both … and …</b><span>ikkalasi ham — kesishma</span></li>
  <li><b>neither … nor …</b><span>hech biri — ikkalasidan tashqarida</span></li>
  <li><b>only</b><span>faqat bittasi — kesishmani ayiring</span></li>
  <li><b>exactly two of the three</b><span>uchtadan aynan ikkitasi</span></li>
  <li><b>at least one</b><span>kamida bittasi — birlashma</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>Of the 100 employees at a firm, 60 speak English, 45 speak Russian, and 20 speak both
    English and Russian. How many of the employees speak neither language?</p>
  </div>
  <ol class="ps-ch">
    <li>5</li>
    <li>15</li>
    <li>20</li>
    <li>25</li>
    <li>35</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 15</p>
      <p>100 − (60 + 45 − 20) = 15.</p>
      <p><b>35</b> — «ikkalasi»ni ikki marta ayirgan javob: 100 − (60 + 45 − 40).</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">35</span>
  <span class="ps-trap__why">Kesishma A + B da <b>ikki</b> marta sanalgan — uni faqat
  <b>bir</b> marta ayirish kerak, shunda u toʻgʻri bir marta qoladi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>In a survey of 80 managers, 50 said they read a business newspaper and 40 said they
    read a business magazine. What is the least possible number of managers who read both?</p>
  </div>
  <ol class="ps-ch">
    <li>0</li>
    <li>5</li>
    <li>10</li>
    <li>30</li>
    <li>40</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 10</p>
      <p>50 + 40 = 90, lekin odamlar atigi 80 ta — kamida 10 kishi ikki marta sanalgan.</p>
      <p><b>0</b> — toʻplamlar bir-biriga tegmasligi mumkin deb oʻylagan javob; 90 kishiga joy yoʻq.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">0</span>
  <span class="ps-trap__why">Ikki toʻplam yigʻindisi umumiy sondan oshsa, kesishma nol
  boʻlolmaydi: ortiqchasi — eng kichik kesishma.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Toʻplam savolida avval <b>shaklni</b> tanlang:</p>
  <ol>
    <li>bitta xususiyat, ikki guruh (ingliz/rus) — formula;</li>
    <li>ikki xil ha/yoʻq xususiyat (erkak/ayol × MBA bor/yoʻq) — 2 × 2 jadval;</li>
    <li>«least / greatest possible» — chegaralarni tekshiring: hech biri = 0 va kichik toʻplam ichkarida.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">60 speak English, 20 of them also Russian → only English = 60</p>
  <p class="pe-good">Only English = 60 − 20 = 40</p>
  <p class="pe-fix__why">«Ingliz tili»ga ikkalasini biladiganlar ham kiradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Three sets: subtract the triple overlap once</p>
  <p class="pe-good">With «exactly two», subtract the triple overlap twice</p>
  <p class="pe-fix__why">Uchala toʻplamdagi odam uch marta sanalgan — bir marta qolishi uchun ikkisi olib tashlanadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> Set A has 30 members, set B has 25, and 10
  are in both. How many are in at least one of the sets?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">45 — 30 + 25 − 10.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> Of 50 people, 30 drink tea, 25 drink coffee and
  5 drink neither. How many drink both?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">10 — 30 + 25 + 5 − 50.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> Of 40 students, 18 play chess, 15 play football
  and 12 play neither. How many play both?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">5 — 18 + 15 + 12 − 40.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> Of 100 people, 70 use app A and 50 use app B.
  What is the greatest possible number who use both?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">50 — B toʻliq A ning ichida boʻlsa.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> Of 300 clients, 180 bought product X, 150 bought
  product Y and 60 bought both. How many bought only X?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">120 — 180 − 60.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>set</b><span>toʻplam</span></li>
  <li><b>overlap</b><span>kesishma</span></li>
  <li><b>both</b><span>ikkalasi ham</span></li>
  <li><b>neither</b><span>hech biri</span></li>
  <li><b>at least one</b><span>kamida bittasi</span></li>
  <li><b>exactly two</b><span>aynan ikkitasi</span></li>
  <li><b>Venn diagram</b><span>Venn diagrammasi</span></li>
  <li><b>survey</b><span>soʻrovnoma</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Jami = A + B − ikkalasi + hech biri.</li>
    <li>«Only A» = A − ikkalasi.</li>
    <li>Ikki xil ha/yoʻq xususiyat — 2 × 2 jadval; qator va ustun yigʻindilari tekshiruv.</li>
    <li>Eng kichik kesishma = A + B − jami (manfiy boʻlsa, 0); eng kattasi = kichik toʻplam.</li>
    <li>Uch toʻplam: «aynan ikkitasi» bir marta, «uchalasi» ikki marta ayiriladi.</li>
  </ul>
</div>
"""

GMAT17 = """
<h2>GMAT-17: Linear Equations and Systems</h2>

<p>Algebra blokining birinchi darsi. Chiziqli tenglama — maktabdan tanish, lekin GMAT uni
ikki xil tekshiradi: <mark>matnni tenglamaga aylantirish</mark> va <mark>kerakli narsani
toʻgʻridan-toʻgʻri topish</mark>. Koʻpincha savol <i>x</i> ni emas, <i>x</i> + <i>y</i> ni
soʻraydi — va uni har bir oʻzgaruvchini alohida topmasdan olish mumkin.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>bir oʻzgaruvchili tenglamani ikki qadamda yechasiz;</li>
    <li>ikki tenglamali sistemani qoʻshish yoki oʻrniga qoʻyish bilan yechasiz;</li>
    <li>savol soʻragan ifodani (<i>x</i> + <i>y</i>, <i>x</i> − <i>y</i>) toʻgʻridan-toʻgʻri topasiz;</li>
    <li>chiptalar, narxlar va yoshlar haqidagi matnni ikki tenglamaga aylantirasiz.</li>
  </ul>
</div>

<h3>Bir oʻzgaruvchi — ikki tomonni muvozanatda saqlang</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3<i>x</i> − 7 = 2<i>x</i> + 5</span>
    <span class="pm-solve__why"><i>x</i> larni bir tomonga yigʻamiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3<i>x</i> − 2<i>x</i> = 5 + 7</span>
    <span class="pm-solve__why">Har bir had boshqa tomonga oʻtganda ishorasi oʻzgaradi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step"><i>x</i> = 12</span>
    <span class="pm-solve__why">Tekshiruv: 36 − 7 = 29 = 24 + 5 ✓</span>
  </div>
</div>

<h3>Ikki tenglama — qoʻshish usuli</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step"><i>x</i> + <i>y</i> = 20, <i>x</i> − <i>y</i> = 6</span>
    <span class="pm-solve__why"><i>y</i> qarama-qarshi ishorali — qoʻshsak yoʻqoladi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2<i>x</i> = 26 → <i>x</i> = 13</span>
    <span class="pm-solve__why">Ikkala tenglamani qoʻshdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step"><i>y</i> = 20 − 13 = 7</span>
    <span class="pm-solve__why">Topilganini birinchi tenglamaga qoʻyamiz</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikki usul bor: <b>qoʻshish</b> (bir oʻzgaruvchining koeffitsiyentlari teng yoki qarama-qarshi
  boʻlsa) va <b>oʻrniga qoʻyish</b> (bitta tenglamada oʻzgaruvchi yolgʻiz turgan boʻlsa,
  masalan <i>x</i> = 2<i>y</i>). Qaysi biri tezroq — tenglamalarning koʻrinishi aytadi.
</div>

<h3>Matndan tenglamaga</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">50 chipta, kattalar $12, bolalar $8, jami $520</span>
    <span class="pm-solve__why">Ikki nomaʼlum — ikki tenglama</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step"><i>a</i> + <i>c</i> = 50; 12<i>a</i> + 8<i>c</i> = 520</span>
    <span class="pm-solve__why">Biri — soni, ikkinchisi — puli</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Hammasi bolalar boʻlsa: 400; har bir katta +4 → (520 − 400) ÷ 4 = 30</span>
    <span class="pm-solve__why">Kattalar 30, bolalar 20 — tekshiruv: 360 + 160 = 520 ✓</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  «Hammasi arzon boʻlsa» usuli — ikki narxli har qanday masalada tenglamasiz yoʻl: barchasini
  arzon narxda hisoblang, ortiqcha pulni narxlar farqiga boʻling. Bu qimmat mahsulot sonini
  bir qatorda beradi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Savol <b>nimani</b> soʻrayotganini oxirida emas, boshida oʻqing. «2<i>x</i> + 3<i>y</i> = 17
  va 3<i>x</i> + 2<i>y</i> = 18 boʻlsa, <i>x</i> + <i>y</i> ni toping» — ikkalasini qoʻshsangiz,
  5<i>x</i> + 5<i>y</i> = 35, yaʼni <i>x</i> + <i>y</i> = 7. <i>x</i> va <i>y</i> ni alohida topish shart emas.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bizda maktabda koʻpincha faqat oʻrniga qoʻyish usuli oʻrgatiladi. GMAT'da qoʻshish
  usuli ancha tez: koeffitsiyentlarga qarang — biror oʻzgaruvchi ikkala tenglamada bir xil
  yoki qarama-qarshi koeffitsiyent bilan tursa, tenglamalarni qoʻshing yoki ayiring. Bitta
  qator yozuv — va bitta oʻzgaruvchi yoʻqoladi. Koeffitsiyentlar har xil boʻlsa (2 va 3),
  avval bir tenglamani mos songa koʻpaytirib, ularni tenglashtiring.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>what is the value of x + y</b><span>x + y ning qiymati — koʻpincha birdaniga topiladi</span></li>
  <li><b>is twice as old as</b><span>… dan ikki baravar katta</span></li>
  <li><b>more than twice</b><span>ikki baravaridan … koʻp</span></li>
  <li><b>a total of</b><span>jami</span></li>
  <li><b>in terms of</b><span>… orqali ifodalang</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>If 2<i>x</i> + 3<i>y</i> = 17 and 3<i>x</i> + 2<i>y</i> = 18, what is the value of
    <i>x</i> + <i>y</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>5</li>
    <li>6</li>
    <li>7</li>
    <li>8</li>
    <li>35</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 7</p>
      <p>Qoʻshamiz: 5<i>x</i> + 5<i>y</i> = 35, demak <i>x</i> + <i>y</i> = 7. (Aslida <i>x</i> = 4, <i>y</i> = 3.)</p>
      <p><b>35</b> — 5 ga boʻlishni unutgan javob.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">35</span>
  <span class="ps-trap__why">Yarim yoʻlda toʻxtash: 5(<i>x</i> + <i>y</i>) topildi, lekin savol
  <i>x</i> + <i>y</i> ning oʻzini soʻradi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>A shop sells pens for $3 each and notebooks for $5 each. A customer buys 14 items
    and pays $54. How many notebooks does the customer buy?</p>
  </div>
  <ol class="ps-ch">
    <li>4</li>
    <li>6</li>
    <li>7</li>
    <li>8</li>
    <li>10</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 6</p>
      <p>Hammasi ruchka boʻlsa: 42; ortiqcha 12 dollar, har bir daftar +2 → 6 ta daftar.</p>
      <p><b>8</b> — ruchkalar soni; savol daftarlarni soʻradi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">8</span>
  <span class="ps-trap__why">Ikkinchi nomaʼlum. GMAT ikkala nomaʼlumni ham variantlarga qoʻyadi —
  oxirida savolni qayta oʻqing.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Sistemani yechishdan oldin <b>soʻralgan ifodaga</b> qarang:</p>
  <ol>
    <li><i>x</i> + <i>y</i> yoki <i>x</i> − <i>y</i> soʻralsa — tenglamalarni qoʻshing yoki ayiring;</li>
    <li>bitta oʻzgaruvchi soʻralsa — ikkinchisini yoʻqotadigan amalni tanlang;</li>
    <li>javobni ikkala tenglamaga qoʻyib tekshiring.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">3(<i>x</i> + 2) = 21 → 3<i>x</i> + 2 = 21</p>
  <p class="pe-good">3<i>x</i> + 6 = 21 → <i>x</i> = 5</p>
  <p class="pe-fix__why">Qavs ochilganda har bir had koʻpaytiriladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">«L is $200 more than twice S» → L = 2(S + 200)</p>
  <p class="pe-good">L = 2S + 200</p>
  <p class="pe-fix__why">«Ikki baravaridan 200 koʻp» — avval ikkiga koʻpaytiriladi, keyin 200 qoʻshiladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> If 5<i>x</i> + 4 = 29, what is <i>x</i>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">5 — 5<i>x</i> = 25.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> If <i>x</i>/3 − 2 = 4, what is <i>x</i>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">18 — <i>x</i>/3 = 6.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> If <i>x</i> + <i>y</i> = 10 and <i>x</i> − <i>y</i> = 4, what is <i>x</i>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">7 — qoʻshsak 2<i>x</i> = 14.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> If 2<i>x</i> + <i>y</i> = 11 and <i>x</i> + <i>y</i> = 7, what is <i>x</i>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">4 — ayirsak <i>x</i> = 4.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> Two numbers add up to 45, and one is four times
  the other. What is the larger number?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">36 — 5 qism = 45, bir qism 9.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>equation</b><span>tenglama</span></li>
  <li><b>system of equations</b><span>tenglamalar sistemasi</span></li>
  <li><b>variable</b><span>oʻzgaruvchi</span></li>
  <li><b>coefficient</b><span>koeffitsiyent</span></li>
  <li><b>solve for x</b><span>x ni toping</span></li>
  <li><b>substitute</b><span>oʻrniga qoʻymoq</span></li>
  <li><b>eliminate</b><span>yoʻqotmoq (oʻzgaruvchini)</span></li>
  <li><b>in terms of</b><span>… orqali</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Had boshqa tomonga oʻtsa, ishorasi oʻzgaradi; qavsda har bir had koʻpaytiriladi.</li>
    <li>Qoʻshish usuli — koeffitsiyentlar teng yoki qarama-qarshi boʻlsa.</li>
    <li>Soʻralgan ifodani (x + y) toʻgʻridan-toʻgʻri qidiring.</li>
    <li>Ikki narxli masala: hammasini arzon narxda hisoblang, ortiqchasini farqqa boʻling.</li>
    <li>Javobni ikkala tenglamaga qoʻyib tekshiring.</li>
  </ul>
</div>
"""

GMAT18 = """
<h2>GMAT-18: Inequalities and Absolute Value</h2>

<p>Tengsizlik tenglamaga oʻxshab yechiladi — bitta istisno bilan: <mark>manfiy songa
koʻpaytirish yoki boʻlishda belgi teskarisiga oʻgiriladi</mark>. Modul (<i>absolute value</i>)
esa masofa: |<i>x</i> − 3| — <i>x</i> dan 3 gacha boʻlgan masofa. Bu ikki gʻoya bilan GMAT'ning
tengsizlik savollarining deyarli hammasi yechiladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>chiziqli tengsizlikni yechib, belgi qachon oʻgirilishini bilasiz;</li>
    <li>qoʻsh tengsizlikni (−3 &lt; 2<i>x</i> + 1 &lt; 9) bir yoʻla yechasiz;</li>
    <li>modulni masofa sifatida oʻqiysiz: |<i>x</i> − 3| &lt; 5;</li>
    <li>tengsizlikni qanoatlantiradigan butun sonlarni sanaysiz.</li>
  </ul>
</div>

<h3>Belgi oʻgiriladigan yagona holat</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">−2<i>x</i> + 5 &gt; 11</span>
    <span class="pm-solve__why">Avval 5 ni oʻtkazamiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">−2<i>x</i> &gt; 6</span>
    <span class="pm-solve__why">Endi −2 ga boʻlish kerak — manfiy son</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step"><i>x</i> &lt; −3</span>
    <span class="pm-solve__why">Belgi &gt; dan &lt; ga oʻgirildi. Tekshiruv: <i>x</i> = −4 → 13 &gt; 11 ✓</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Nega oʻgiriladi? 2 &lt; 5 toʻgʻri, lekin ikkalasini −1 ga koʻpaytirsak, −2 va −5 chiqadi —
  endi −2 <b>katta</b>. Manfiy koʻpaytuvchi sonlar tartibini teskari qiladi. Musbat songa
  koʻpaytirish yoki istalgan son qoʻshish esa belgini oʻzgartirmaydi.
</div>

<h3>Qoʻsh tengsizlik — uchala qismga bir xil amal</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">−3 &lt; 2<i>x</i> + 1 &lt; 9</span>
    <span class="pm-solve__why">Har bir qismdan 1 ni ayiramiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">−4 &lt; 2<i>x</i> &lt; 8</span>
    <span class="pm-solve__why">Har bir qismni 2 ga boʻlamiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">−2 &lt; <i>x</i> &lt; 4 → butun: −1, 0, 1, 2, 3 (5 ta)</span>
    <span class="pm-solve__why">Qatʼiy belgi — chetlar kirmaydi</span>
  </div>
</div>

<h3>Modul — masofa</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">|<i>x</i> − 3| &lt; 5</span>
    <span class="pm-solve__why"><i>x</i> 3 dan 5 birlikdan kamroq uzoqlikda</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">−5 &lt; <i>x</i> − 3 &lt; 5 → −2 &lt; <i>x</i> &lt; 8</span>
    <span class="pm-solve__why">Markaz 3, har ikki tomonga 5</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Butun yechimlar: −1 dan 7 gacha — 9 ta</span>
    <span class="pm-solve__why">7 − (−1) + 1 = 9</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Uch shaklni eslab qoling: |<i>x</i> − <i>a</i>| = <i>d</i> — ikki nuqta (<i>a</i> ± <i>d</i>);
  |<i>x</i> − <i>a</i>| &lt; <i>d</i> — oraliq ichi; |<i>x</i> − <i>a</i>| &gt; <i>d</i> — oraliqdan tashqari
  (ikki boʻlak). |<i>x</i> + 1| — bu |<i>x</i> − (−1)|, markaz −1.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Biznesda modul — <b>ruxsat etilgan chetlanish</b>: «500 ml dan koʻpi bilan 4 ml farq qilsin»
  = |hajm − 500| ≤ 4. «Within», «no more than … from», «tolerance» soʻzlarini koʻrsangiz —
  bu modul.
</div>

<h3>Butun yechimlarni sanash</h3>

<p>Tez yoʻl: <i>a</i> ≤ <i>x</i> ≤ <i>b</i> oraligʻidagi butun sonlar soni <b><i>b</i> − <i>a</i> + 1</b>.
Qatʼiy belgilarda avval chetlarni ichkariga suring: −2 &lt; <i>x</i> &lt; 8 — bu −1 ≤ <i>x</i> ≤ 7,
demak 7 − (−1) + 1 = 9. Chet butun son boʻlmasa (−2.5 &lt; <i>x</i>), eng yaqin ichkaridagi
butun sonni oling (−2).</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Kvadrat tengsizlik</b> ham modulga aylanadi: <i>x</i><sup>2</sup> &lt; 16 — bu |<i>x</i>| &lt; 4,
  yaʼni −4 &lt; <i>x</i> &lt; 4. Koʻpchilik ikkala tomondan ildiz olib «<i>x</i> &lt; 4» deb yozadi va
  manfiy tomonni yoʻqotadi: <i>x</i> = −5 da 25 &gt; 16. Kvadratni koʻrsangiz, modul haqida oʻylang.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>at most / no more than</b><span>koʻpi bilan — ≤</span></li>
  <li><b>at least / no less than</b><span>kamida — ≥</span></li>
  <li><b>within 5 of 3</b><span>3 dan 5 birlikdan oshmagan masofada</span></li>
  <li><b>how many integers satisfy</b><span>nechta butun son qanoatlantiradi</span></li>
  <li><b>which must be true</b><span>qaysi biri har doim toʻgʻri</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>How many integers <i>x</i> satisfy |<i>x</i> − 3| &lt; 5?</p>
  </div>
  <ol class="ps-ch">
    <li>7</li>
    <li>8</li>
    <li>9</li>
    <li>10</li>
    <li>11</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 9</p>
      <p>−2 &lt; <i>x</i> &lt; 8: butun sonlar −1, 0, …, 7 — 9 ta.</p>
      <p><b>11</b> — chetlarni (−2 va 8) ham qoʻshgan javob; belgi qatʼiy.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">11</span>
  <span class="ps-trap__why">&lt; va ≤ farqi. Qatʼiy belgi boʻlsa, chetdagi nuqtalar sanalmaydi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>If −2<i>x</i> + 5 &gt; 11, which of the following must be true?</p>
  </div>
  <ol class="ps-ch">
    <li><i>x</i> &lt; −3</li>
    <li><i>x</i> &gt; −3</li>
    <li><i>x</i> &lt; 3</li>
    <li><i>x</i> &gt; 3</li>
    <li><i>x</i> &lt; −8</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) <i>x</i> &lt; −3</p>
      <p>−2<i>x</i> &gt; 6; −2 ga boʻlganda belgi oʻgiriladi.</p>
      <p><b>x &gt; −3</b> — belgini oʻgirishni unutgan javob.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val"><i>x</i> &gt; −3</span>
  <span class="ps-trap__why">Manfiy songa boʻlganda belgi oʻgiriladi. Tekshiring: <i>x</i> = 0 da
  5 &gt; 11 — notoʻgʻri, demak <i>x</i> = 0 yechim emas.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Tengsizlik javobini <b>bitta son bilan</b> tekshiring:</p>
  <ol>
    <li>javob oraligʻidan son oling (masalan, <i>x</i> = −4) — u asl tengsizlikni qanoatlantirishi kerak;</li>
    <li>oraliqdan tashqaridagi sonni oling (<i>x</i> = 0) — u qanoatlantirmasligi kerak;</li>
    <li>ikkalasi mos kelsa, belgi toʻgʻri tomonga qaragan.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">−3<i>x</i> ≥ 12 → <i>x</i> ≥ −4</p>
  <p class="pe-good"><i>x</i> ≤ −4</p>
  <p class="pe-fix__why">Manfiy songa boʻlindi — belgi oʻgiriladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">|<i>x</i> − 4| = 6 → <i>x</i> = 10</p>
  <p class="pe-good"><i>x</i> = 10 yoki <i>x</i> = −2</p>
  <p class="pe-fix__why">Markazdan ikki tomonga ham 6 birlik — ikki yechim.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> Solve 3<i>x</i> − 4 &gt; 11.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">5 dan katta sonlar: <i>x</i> &gt; 5.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> How many values of <i>x</i> satisfy |<i>x</i>| = 7?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">2 ta — 7 va −7.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> How many integers satisfy −3 &lt; 2<i>x</i> + 1 &lt; 9?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">5 ta — −1, 0, 1, 2, 3.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> What is the sum of the solutions of |2<i>x</i> − 6| = 10?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">6 — yechimlar 8 va −2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> A taxi charges $3 plus $0.50 per kilometer. With
  $15, what is the greatest distance you can ride?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">24 km — 3 + 0.5<i>k</i> ≤ 15.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>inequality</b><span>tengsizlik</span></li>
  <li><b>absolute value</b><span>modul, mutlaq qiymat</span></li>
  <li><b>at most</b><span>koʻpi bilan</span></li>
  <li><b>at least</b><span>kamida</span></li>
  <li><b>strict inequality</b><span>qatʼiy tengsizlik (&lt;, &gt;)</span></li>
  <li><b>range</b><span>oraliq</span></li>
  <li><b>tolerance</b><span>ruxsat etilgan chetlanish</span></li>
  <li><b>reverse the sign</b><span>belgini oʻgirmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Manfiy songa koʻpaytirish yoki boʻlishda belgi oʻgiriladi.</li>
    <li>Qoʻsh tengsizlikda uchala qismga bir xil amal.</li>
    <li>|x − a| — x dan a gacha masofa; = d ikki nuqta, &lt; d ichkari, &gt; d tashqari.</li>
    <li>Qatʼiy belgida chetlar sanalmaydi.</li>
    <li>Javobni oraliq ichidagi va tashqarisidagi bitta son bilan tekshiring.</li>
  </ul>
</div>
"""

GMAT19 = """
<h2>GMAT-19: Quadratics and Factoring</h2>

<p>Kvadrat tenglama — GMAT algebrasining markazi. Kalkulyatorsiz imtihonda diskriminant
formulasi deyarli kerak boʻlmaydi: tenglamalar <mark>koʻpaytuvchilarga ajraladigan</mark>
qilib tuziladi. Uch narsani bilish yetarli: ikki sonni topib ajratish, nol koʻpaytma
qoidasi va uchta maxsus koʻpaytma.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li><i>x</i><sup>2</sup> + <i>bx</i> + <i>c</i> ni ikki son bilan koʻpaytuvchilarga ajratasiz;</li>
    <li>nol koʻpaytma qoidasi bilan ildizlarni topasiz;</li>
    <li>kvadratlar ayirmasi va toʻla kvadrat formulalarini ikki tomonga qoʻllaysiz;</li>
    <li>ildizlar yigʻindisi va koʻpaytmasini tenglamani yechmasdan aytasiz.</li>
  </ul>
</div>

<h3>Koʻpaytuvchilarga ajratish — ikki son</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step"><i>x</i><sup>2</sup> − 5<i>x</i> + 6 = 0</span>
    <span class="pm-solve__why">Koʻpaytmasi 6, yigʻindisi −5 boʻlgan ikki son</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">−2 va −3 → (<i>x</i> − 2)(<i>x</i> − 3) = 0</span>
    <span class="pm-solve__why">(−2)(−3) = 6, (−2) + (−3) = −5</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step"><i>x</i> = 2 yoki <i>x</i> = 3</span>
    <span class="pm-solve__why">Koʻpaytma nol — koʻpaytuvchilardan biri nol</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Nol koʻpaytma qoidasi</b> faqat oʻng tomon <b>nol</b> boʻlganda ishlaydi. (<i>x</i> − 2)(<i>x</i> − 3) = 6
  dan «<i>x</i> − 2 = 6» deb boʻlmaydi — avval hamma hadlarni bir tomonga oʻtkazing, keyin ajrating.
</div>

<h3>Uchta maxsus koʻpaytma</h3>

<ul>
  <li><b>(<i>a</i> + <i>b</i>)<sup>2</sup> = <i>a</i><sup>2</sup> + 2<i>ab</i> + <i>b</i><sup>2</sup></b> — masalan,
  (<i>x</i> + 3)<sup>2</sup> = <i>x</i><sup>2</sup> + 6<i>x</i> + 9;</li>
  <li><b>(<i>a</i> − <i>b</i>)<sup>2</sup> = <i>a</i><sup>2</sup> − 2<i>ab</i> + <i>b</i><sup>2</sup></b> — masalan,
  (<i>x</i> − 5)<sup>2</sup> = <i>x</i><sup>2</sup> − 10<i>x</i> + 25;</li>
  <li><b><i>a</i><sup>2</sup> − <i>b</i><sup>2</sup> = (<i>a</i> + <i>b</i>)(<i>a</i> − <i>b</i>)</b> — masalan,
  <i>x</i><sup>2</sup> − 9 = (<i>x</i> + 3)(<i>x</i> − 3).</li>
</ul>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">51<sup>2</sup> − 49<sup>2</sup></span>
    <span class="pm-solve__why">Kalkulyatorsiz kvadratlash — uzoq yoʻl</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">(51 + 49)(51 − 49) = 100 × 2 = 200</span>
    <span class="pm-solve__why">Kvadratlar ayirmasi formulasi</span>
  </div>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step"><i>x</i> + <i>y</i> = 7, <i>xy</i> = 10 → <i>x</i><sup>2</sup> + <i>y</i><sup>2</sup> = ?</span>
    <span class="pm-solve__why">(<i>x</i> + <i>y</i>)<sup>2</sup> = <i>x</i><sup>2</sup> + 2<i>xy</i> + <i>y</i><sup>2</sup></span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">49 = <i>x</i><sup>2</sup> + <i>y</i><sup>2</sup> + 20 → 29</span>
    <span class="pm-solve__why"><i>x</i> va <i>y</i> ni topish shart emas</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  <i>x</i><sup>2</sup> + <i>bx</i> + <i>c</i> = 0 da ildizlar <b>yigʻindisi −<i>b</i></b>, <b>koʻpaytmasi <i>c</i></b>.
  <i>x</i><sup>2</sup> − 5<i>x</i> + 6 = 0 → yigʻindi 5, koʻpaytma 6. «Sum of the possible values»
  savolida tenglamani yechmasdan javob berish mumkin.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <i>x</i><sup>2</sup> = 4<i>x</i> ni <i>x</i> ga boʻlib, «<i>x</i> = 4» deyish — klassik xato: <i>x</i> = 0 ham
  yechim. Hech qachon nomaʼlumga boʻlmang; hammasini bir tomonga oʻtkazib ajrating:
  <i>x</i>(<i>x</i> − 4) = 0 → 0 yoki 4.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bizning maktab dasturida kvadrat tenglama koʻpincha diskriminant bilan yechiladi.
  GMAT'da bu uzoq yoʻl: deyarli har bir tenglama butun ildizli qilib tuziladi. Avval ozod
  hadning boʻluvchilari juftlarini sinang — 6 uchun (1, 6) va (2, 3). Faqat hech biri mos
  kelmasa, formulaga oʻting.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>the sum of all possible values of x</b><span>x ning barcha mumkin qiymatlari yigʻindisi</span></li>
  <li><b>factor / factored form</b><span>koʻpaytuvchilarga ajratilgan koʻrinish</span></li>
  <li><b>roots / solutions</b><span>ildizlar / yechimlar</span></li>
  <li><b>consecutive positive integers</b><span>ketma-ket musbat butun sonlar</span></li>
  <li><b>which of the following could be</b><span>qaysi biri boʻlishi mumkin</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>If <i>x</i><sup>2</sup> − 5<i>x</i> + 6 = 0, what is the sum of all possible values of <i>x</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>−5</li>
    <li>−1</li>
    <li>1</li>
    <li>5</li>
    <li>6</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: D) 5</p>
      <p>Ildizlar 2 va 3; yigʻindi 5.</p>
      <p><b>6</b> — ildizlar koʻpaytmasi; <b>−5</b> — ishorani adashtirgan javob.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">−5</span>
  <span class="ps-trap__why">Yigʻindi −<i>b</i>: koeffitsiyent −5 boʻlsa, yigʻindi +5. Ishonch hosil
  qilish uchun ildizlarni topib qoʻshing: 2 + 3.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>If <i>a</i> + <i>b</i> = 10 and <i>a</i> − <i>b</i> = 4, what is the value of
    <i>a</i><sup>2</sup> − <i>b</i><sup>2</sup>?</p>
  </div>
  <ol class="ps-ch">
    <li>14</li>
    <li>24</li>
    <li>40</li>
    <li>84</li>
    <li>100</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: C) 40</p>
      <p><i>a</i><sup>2</sup> − <i>b</i><sup>2</sup> = (<i>a</i> + <i>b</i>)(<i>a</i> − <i>b</i>) = 10 × 4.</p>
      <p><b>14</b> — yigʻindi va ayirmani qoʻshgan javob.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">14</span>
  <span class="ps-trap__why">Yigʻindi va ayirmani qoʻshish. Kvadratlar ayirmasi — ularning
  <b>koʻpaytmasi</b>: 10 × 4. <i>a</i> va <i>b</i> ni alohida topish ham shart emas.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Kvadratli ifodani koʻrsangiz, <b>maxsus koʻpaytmani</b> qidiring:</p>
  <ol>
    <li>ikki kvadrat ayirmasi — (<i>a</i> + <i>b</i>)(<i>a</i> − <i>b</i>);</li>
    <li><i>x</i><sup>2</sup> + <i>y</i><sup>2</sup> va <i>xy</i> birga — (<i>x</i> + <i>y</i>)<sup>2</sup>;</li>
    <li>katta sonlarning kvadratlari ayirmasi — hech qachon kvadratlamang.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">(<i>x</i> + 3)<sup>2</sup> = <i>x</i><sup>2</sup> + 9</p>
  <p class="pe-good">(<i>x</i> + 3)<sup>2</sup> = <i>x</i><sup>2</sup> + 6<i>x</i> + 9</p>
  <p class="pe-fix__why">Oʻrta had 2<i>ab</i> yoʻqolmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><i>x</i><sup>2</sup> = 4<i>x</i> → <i>x</i> = 4</p>
  <p class="pe-good"><i>x</i>(<i>x</i> − 4) = 0 → <i>x</i> = 0 yoki 4</p>
  <p class="pe-fix__why"><i>x</i> ga boʻlish <i>x</i> = 0 yechimni yoʻqotadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> Factor <i>x</i><sup>2</sup> + 7<i>x</i> + 12.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">(<i>x</i> + 3)(<i>x</i> + 4) — 3 × 4 = 12, 3 + 4 = 7.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> How many solutions does <i>x</i><sup>2</sup> = 49 have?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">2 ta — 7 va −7.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> What is 51<sup>2</sup> − 49<sup>2</sup>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">200 — 100 × 2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> If (<i>x</i> + <i>y</i>)<sup>2</sup> = 50 and <i>xy</i> = 12,
  what is <i>x</i><sup>2</sup> + <i>y</i><sup>2</sup>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">26 — 50 − 2 × 12.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> A price of <i>p</i> dollars brings revenue
  <i>p</i>(100 − <i>p</i>). For which prices is revenue $2,100?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">30 va 70 dollar — <i>p</i><sup>2</sup> − 100<i>p</i> + 2,100 = (<i>p</i> − 30)(<i>p</i> − 70).</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>quadratic equation</b><span>kvadrat tenglama</span></li>
  <li><b>factor</b><span>koʻpaytuvchilarga ajratmoq</span></li>
  <li><b>root / solution</b><span>ildiz / yechim</span></li>
  <li><b>difference of squares</b><span>kvadratlar ayirmasi</span></li>
  <li><b>perfect square</b><span>toʻla kvadrat</span></li>
  <li><b>expand</b><span>qavsni ochmoq</span></li>
  <li><b>zero product</b><span>nol koʻpaytma</span></li>
  <li><b>revenue</b><span>tushum</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Ajratish: koʻpaytmasi <i>c</i>, yigʻindisi <i>b</i> boʻlgan ikki son.</li>
    <li>Nol koʻpaytma — faqat oʻng tomon nol boʻlganda.</li>
    <li>(a ± b)<sup>2</sup> = a<sup>2</sup> ± 2ab + b<sup>2</sup>; a<sup>2</sup> − b<sup>2</sup> = (a + b)(a − b).</li>
    <li>Ildizlar yigʻindisi −b, koʻpaytmasi c.</li>
    <li>Hech qachon nomaʼlumga boʻlmang — yechim yoʻqoladi.</li>
  </ul>
</div>
"""

GMAT20 = """
<h2>GMAT-20: Functions and Custom Operations</h2>

<p><i>f</i>(<i>x</i>) yozuvi koʻpchilikni choʻchitadi, lekin gʻoyasi oddiy: <mark>funksiya —
qoida</mark>, qavs ichidagi narsa shu qoidaga qoʻyiladi. GMAT'da yana bir tur bor —
oʻylab topilgan belgilar (★, ◆, Δ): «<i>a</i> ★ <i>b</i> = <i>ab</i> − <i>a</i> + <i>b</i>». Bu ham
funksiya, faqat boshqa kiyimda. Har ikkisida bitta koʻnikma tekshiriladi — ehtiyotkorlik
bilan oʻrniga qoʻyish.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li><i>f</i>(−2), <i>f</i>(3<i>x</i>), <i>f</i>(<i>a</i> + 1) kabi qiymatlarni xatosiz hisoblaysiz;</li>
    <li>kompozitsiyani (<i>f</i>(<i>g</i>(<i>x</i>))) ichkaridan tashqariga yechasiz;</li>
    <li>oʻylab topilgan amal belgilarini qoidaga qarab bajarasiz;</li>
    <li>xarajat, tushum va tarif formulalarini funksiya sifatida oʻqiysiz.</li>
  </ul>
</div>

<h3>Oʻrniga qoʻyish — qavslar bilan</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step"><i>f</i>(<i>x</i>) = 3<i>x</i><sup>2</sup> − 2<i>x</i>; <i>f</i>(−2) = ?</span>
    <span class="pm-solve__why">Har bir <i>x</i> oʻrniga (−2) — qavs bilan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3(−2)<sup>2</sup> − 2(−2) = 3 × 4 + 4</span>
    <span class="pm-solve__why">(−2)<sup>2</sup> = 4; −2 × (−2) = +4</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">16</span>
    <span class="pm-solve__why">Qavssiz yozilsa, ikkala ishora ham xato chiqadi</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <i>f</i>(3<i>x</i>) — bu «<i>f</i>(<i>x</i>) × 3» emas. <i>f</i>(<i>x</i>) = 2<i>x</i><sup>2</sup> boʻlsa,
  <i>f</i>(3<i>x</i>) = 2(3<i>x</i>)<sup>2</sup> = 18<i>x</i><sup>2</sup>. Qavs ichidagi <b>butun ifoda</b> <i>x</i>
  oʻrniga qoʻyiladi va kvadratga koʻtariladi.
</div>

<h3>Kompozitsiya — ichkaridan tashqariga</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step"><i>f</i>(<i>x</i>) = <i>x</i> + 1, <i>g</i>(<i>x</i>) = <i>x</i><sup>2</sup>; <i>f</i>(<i>g</i>(3))</span>
    <span class="pm-solve__why">Avval ichkaridagi: <i>g</i>(3)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step"><i>g</i>(3) = 9 → <i>f</i>(9) = 10</span>
    <span class="pm-solve__why">Natija tashqi funksiyaga kiradi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step"><i>g</i>(<i>f</i>(3)) = <i>g</i>(4) = 16</span>
    <span class="pm-solve__why">Tartib almashsa — javob boshqa</span>
  </div>
</div>

<h3>Oʻylab topilgan belgilar</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step"><i>a</i> ★ <i>b</i> = <i>ab</i> − <i>a</i> + <i>b</i>; 3 ★ (2 ★ 4)</span>
    <span class="pm-solve__why">Avval qavs ichidagi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2 ★ 4 = 8 − 2 + 4 = 10</span>
    <span class="pm-solve__why"><i>a</i> = 2, <i>b</i> = 4 — tartib muhim</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3 ★ 10 = 30 − 3 + 10 = 37</span>
    <span class="pm-solve__why">Endi <i>a</i> = 3, <i>b</i> = 10</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Belgi qoidasini qogʻozga <b>boʻsh joylar</b> bilan koʻchiring: ▢ ★ ○ = ▢○ − ▢ + ○. Keyin
  sonlarni katakchalarga qoʻying. Bu <i>a</i> va <i>b</i> ni almashtirib qoʻyish xatosidan saqlaydi —
  belgilar koʻpincha <b>simmetrik emas</b>: 2 ★ 4 = 10, lekin 4 ★ 2 = 6.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Biznes formulalari ham funksiya: xarajat <i>C</i>(<i>n</i>) = 800 + 15<i>n</i> — 800 doimiy
  xarajat, 15 bir dona narxi. «<i>C</i>(200) ni toping» — <i>n</i> oʻrniga 200 ni qoʻying. «Qachon
  <i>C</i>(<i>n</i>) = 5,300?» — teskari savol, tenglama yechiladi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Funksiya savolining yana bir koʻrinishi — <b>teskari savol</b>: «<i>g</i>(<i>x</i>) = 4
  boʻlsa, <i>x</i> nechaga teng?» Bunda son <i>x</i> oʻrniga emas, natija oʻrniga qoʻyiladi va
  tenglama yechiladi: 10 − 2<i>x</i> = 4 → <i>x</i> = 3. Son qavs ichida turibdimi yoki tenglikning
  oʻng tomonidami — shunga qarang.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>is defined by</b><span>… bilan aniqlanadi — qoida</span></li>
  <li><b>for all numbers a and b</b><span>barcha a va b sonlar uchun</span></li>
  <li><b>f(g(x))</b><span>avval g, keyin f</span></li>
  <li><b>is undefined</b><span>aniqlanmagan — nolga boʻlish</span></li>
  <li><b>the function C gives the cost of</b><span>C funksiyasi … xarajatini beradi</span></li>
</ul>

<h3>GMAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>If <i>f</i>(<i>x</i>) = 3<i>x</i><sup>2</sup> − 2<i>x</i>, what is the value of <i>f</i>(−2)?</p>
  </div>
  <ol class="ps-ch">
    <li>−16</li>
    <li>−8</li>
    <li>8</li>
    <li>12</li>
    <li>16</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: E) 16</p>
      <p>3 × 4 − 2 × (−2) = 12 + 4.</p>
      <p><b>8</b> — ikkinchi hadning ishorasini adashtirgan javob (12 − 4).</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">8</span>
  <span class="ps-trap__why">−2<i>x</i> da <i>x</i> = −2: minus × minus = plyus. Qavslar bu xatoni
  oldini oladi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>For all numbers <i>a</i> and <i>b</i>, the operation ★ is defined by
    <i>a</i> ★ <i>b</i> = <i>ab</i> − <i>a</i> + <i>b</i>. What is the value of 3 ★ (2 ★ 4)?</p>
  </div>
  <ol class="ps-ch">
    <li>10</li>
    <li>19</li>
    <li>27</li>
    <li>37</li>
    <li>43</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: D) 37</p>
      <p>2 ★ 4 = 10; 3 ★ 10 = 30 − 3 + 10 = 37.</p>
      <p><b>19</b> — chapdan oʻngga (3 ★ 2) ★ 4 deb hisoblagan javob; qavs tartibni belgilaydi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">19</span>
  <span class="ps-trap__why">Qavsni eʼtiborsiz qoldirish. Oʻylab topilgan belgilarda ham avval qavs
  ichidagi amal bajariladi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Funksiya savolida <b>uch qadam</b>:</p>
  <ol>
    <li>qoidani boʻsh joylar bilan qayta yozing;</li>
    <li>har bir qiymatni qavs ichida qoʻying — ayniqsa manfiy sonlar va ifodalar;</li>
    <li>kompozitsiya va ichma-ich belgilarda ichkaridan boshlang.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad"><i>f</i>(<i>x</i>) = 2<i>x</i><sup>2</sup> → <i>f</i>(3<i>x</i>) = 6<i>x</i><sup>2</sup></p>
  <p class="pe-good"><i>f</i>(3<i>x</i>) = 2(3<i>x</i>)<sup>2</sup> = 18<i>x</i><sup>2</sup></p>
  <p class="pe-fix__why">3<i>x</i> butunligicha kvadratga koʻtariladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><i>f</i>(<i>g</i>(3)) — avval <i>f</i>(3)</p>
  <p class="pe-good">Avval <i>g</i>(3), keyin uning natijasiga <i>f</i></p>
  <p class="pe-fix__why">Kompozitsiya ichkaridan tashqariga hisoblanadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span> If <i>f</i>(<i>x</i>) = 2<i>x</i> + 5, what is <i>f</i>(3)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">11 — 6 + 5.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span> If <i>f</i>(<i>x</i>) = <i>x</i> + 1 and <i>g</i>(<i>x</i>) = <i>x</i><sup>2</sup>, what is <i>f</i>(<i>g</i>(3))?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">10 — <i>g</i>(3) = 9.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span> With the same functions, what is <i>g</i>(<i>f</i>(3))?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">16 — <i>f</i>(3) = 4.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span> If <i>a</i> # <i>b</i> = <i>a</i><sup>2</sup> − <i>b</i>, what is 4 # 7?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">9 — 16 − 7.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span> A cost function is <i>C</i>(<i>n</i>) = 500 + 12<i>n</i>
  dollars. What is <i>C</i>(50)?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">$1,100 — 500 + 600.</p></details>
</div>

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>function</b><span>funksiya</span></li>
  <li><b>input / output</b><span>kirish qiymati / natija</span></li>
  <li><b>composite function</b><span>murakkab funksiya, kompozitsiya</span></li>
  <li><b>operation</b><span>amal</span></li>
  <li><b>defined by</b><span>… bilan aniqlangan</span></li>
  <li><b>undefined</b><span>aniqlanmagan</span></li>
  <li><b>cost function</b><span>xarajat funksiyasi</span></li>
  <li><b>substitute</b><span>oʻrniga qoʻymoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Funksiya — qoida; qavs ichidagini butunligicha, qavs bilan qoʻying.</li>
    <li>f(3x) ≠ 3·f(x); f(a + 1) — har bir x oʻrniga (a + 1).</li>
    <li>f(g(x)) — avval g, keyin f; tartib almashsa, javob boshqa.</li>
    <li>Oʻylab topilgan belgi: qoidani boʻsh joylar bilan yozing; belgi simmetrik boʻlmasligi mumkin.</li>
    <li>Biznes formulasi ham funksiya: doimiy qism + bir dona narxi × soni.</li>
  </ul>
</div>
"""

TUTORIALS = [
    {
        "title": "GMAT-16: Overlapping Sets and Venn Tables",
        "category": "math", "order": 16,
        "summary": "Ikki toʻplam formulasi, 2 × 2 jadval, kesishmaning eng kichik va eng katta qiymati, uch toʻplamda «aynan ikkitasi» va «uchalasi».",
        "stories": ["Two Lists, One Customer Base"],
        "content": GMAT16,
    },
    {
        "title": "GMAT-17: Linear Equations and Systems",
        "category": "math", "order": 17,
        "summary": "Chiziqli tenglama, ikki tenglamali sistema, soʻralgan ifodani toʻgʻridan-toʻgʻri topish va matnni tenglamaga aylantirish.",
        "stories": ["The Price of a Ticket"],
        "content": GMAT17,
    },
    {
        "title": "GMAT-18: Inequalities and Absolute Value",
        "category": "math", "order": 18,
        "summary": "Tengsizliklar va belgi oʻgirilishi, qoʻsh tengsizlik, modul — masofa sifatida, butun yechimlarni sanash.",
        "stories": ["Within Four Millilitres"],
        "content": GMAT18,
    },
    {
        "title": "GMAT-19: Quadratics and Factoring",
        "category": "math", "order": 19,
        "summary": "Kvadrat uchhadni koʻpaytuvchilarga ajratish, nol koʻpaytma qoidasi, maxsus koʻpaytmalar va ildizlar yigʻindisi.",
        "stories": ["The Price That Earns the Most"],
        "content": GMAT19,
    },
    {
        "title": "GMAT-20: Functions and Custom Operations",
        "category": "math", "order": 20,
        "summary": "Funksiyaga qiymat qoʻyish, kompozitsiya, oʻylab topilgan amal belgilari va biznes formulalari funksiya sifatida.",
        "stories": ["A Formula for the Fare"],
        "content": GMAT20,
    },
]
