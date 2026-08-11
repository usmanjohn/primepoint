# -*- coding: utf-8 -*-
"""Prime Math — Blok C yakuni: darslar 40–42 (tengsizlik, modul, daraja qonunlari).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt

Uchta oyoq birga yoziladi:
  mashqlar — practice/management/commands/_practice_pm_40_42.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_40_42.py

⚠️ Kumulyativ chegaralar:
  • PM-40 — tengsizlik tenglama kabi yechiladi, BITTA farq bilan: manfiy
    songa koʻpaytirilsa yoki boʻlinsa, ishora teskari boʻladi. Qoʻsh
    tengsizlik (a < x < b) faqat son oʻqida koʻrsatiladi, yechilmaydi;
  • PM-41 — modul masofa sifatida. |x| = a koʻrinishidagi eng sodda
    tenglamalar bor; modulli TENGSIZLIK yoʻq (u ancha keyin);
  • PM-42 — daraja qonunlari va standart koʻrinish (3 × 10^8). Manfiy
    koʻrsatkich boʻlish qonunidan chiqariladi. Ildiz qonunlari (PM-13 dan
    keyingi darajada) bu yerda yoʻq;
  • koʻphadlar (PM-43) va qisqa koʻpaytirish formulalari (PM-44) keyingi
    batchda.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_40_42.py --author=prime
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
    # PM-40 — tengsizlik
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-40: Tengsizlik va uni son oʻqida koʻrsatish",
        "category": "math",
        "order": 40,
        "summary": (
            "«Kamida», «koʻpi bilan», «oshmasin» degan soʻzlar belgiga aylanadi. "
            "Tengsizlikni tenglama kabi yechish va manfiy songa boʻlganda ishora "
            "nega teskari boʻlishi."
        ),
        "stories": ["Kamida qancha kerak"],
        "content": """
<h2>PM-40: Tengsizlik va uni son oʻqida koʻrsatish</h2>

<p>Hayotdagi savollarning koʻpi «roppa-rosa qancha?» emas, «<b>kamida</b> qancha?»
yoki «<b>koʻpi bilan</b> qancha?» deb beriladi. Avtobusga chiqish uchun kamida
2000 soʻm kerak; sumkaga koʻpi bilan 20 kilogramm solish mumkin; imtihondan oʻtish
uchun kamida 60 ball. Bunday shartlar tenglik bilan emas, <b>tengsizlik</b> bilan
yoziladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>toʻrtta tengsizlik belgisini oʻqiysiz va yozasiz;</li>
    <li>soʻzni belgiga aylantirasiz: «kamida» → ≥;</li>
    <li>tengsizlikni tenglama kabi yechasiz;</li>
    <li>manfiy songa boʻlganda ishorani teskari qilasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Toʻrtta belgi</span>
  <span class="pe-chip pe-chip--o">&lt; kichik</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">&gt; katta</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">≤ katta emas</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">≥ kichik emas</span>
</div>

<h3>1. Belgilarni oʻqish</h3>

<p><b>x &lt; 7</b> — «x yettidan kichik». <b>x ≤ 7</b> — «x yettidan katta emas»,
yaʼni x yetti ham boʻlishi mumkin. Kichkina chiziqcha butun bir soʻzni bildiradi:
<b>yoki teng</b>.</p>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Belgi ochiq tomoni bilan kattaga qaraydi</p>
  <p>&lt; va &gt; belgilarining uchi ingichka, ogʻzi keng. Ogʻzi doim <b>kattaroq</b>
  tomonga qaraydi: 3 &lt; 8 da ogʻiz sakkiz tomonda. Adashsangiz shu qoidani
  eslang.</p>
</div>

<h3>2. Soʻzdan belgiga</h3>

<p>PM-30 dagi lugʻatning davomi. Matnli masalalarda aynan shu soʻzlar tengsizlikni
boshlab beradi.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Matnda shunday deyiladi</th><th>Belgisi</th><th>Misol</th></tr>
  <tr><td>…dan kichik, …dan kam</td><td class="pm-word__sym">&lt;</td>
      <td>x &lt; 10</td></tr>
  <tr><td>…dan katta, …dan koʻp</td><td class="pm-word__sym">&gt;</td>
      <td>x &gt; 10</td></tr>
  <tr><td>kamida, …dan kam emas</td><td class="pm-word__sym">≥</td>
      <td>x ≥ 60</td></tr>
  <tr><td>koʻpi bilan, oshmasin</td><td class="pm-word__sym">≤</td>
      <td>x ≤ 20</td></tr>
  <tr><td>yetarli</td><td class="pm-word__sym">≥</td><td>pul ≥ narx</td></tr>
  <tr><td>sigʻadi, joylashadi</td><td class="pm-word__sym">≤</td>
      <td>ogʻirlik ≤ 20</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">«Kamida» va «koʻpi bilan» — eng koʻp adashtiradigan juftlik</p>
  <p>«Kamida 60 ball» degani 60 <b>ham boʻladi</b>, 59 esa yoʻq: <b>≥ 60</b>.
  «Koʻpi bilan 20 kg» degani 20 boʻlsa mayli, 21 boʻlsa yoʻq: <b>≤ 20</b>. Ikkalasida
  ham chegaraning oʻzi hisobga kiradi — shuning uchun ostiga chiziqcha qoʻyiladi.</p>
</div>

<h3>3. Son oʻqida koʻrsatish</h3>

<p>Tengsizlikning javobi bitta son emas, <b>sonlar toʻplami</b>. Uni son oʻqida
boʻyalgan qism bilan koʻrsatamiz. Chegara nuqtasi javobga kirsa — <b>toʻla</b>
doiracha, kirmasa — <b>ichi boʻsh</b> doiracha.</p>

<div class="pm-num">
  <div class="pm-num__track">
    <span class="pm-num__band" style="left:60%;width:40%"></span>
    <span class="pm-num__tick" style="left:0%"><i>0</i></span>
    <span class="pm-num__tick" style="left:30%"><i>3</i></span>
    <span class="pm-num__tick" style="left:100%"><i>10</i></span>
    <span class="pm-num__dot pm-num__dot--open" style="left:60%"><i>6</i></span>
  </div>
</div>

<p>Yuqoridagi rasm <b>x &gt; 6</b> ni koʻrsatadi: oltidan oʻngdagi hamma son javob,
oltining oʻzi esa yoʻq — shuning uchun doiracha ichi boʻsh. Agar <b>x ≥ 6</b> boʻlsa,
doiracha toʻla boʻyalardi.</p>

<h3>4. Yechish — tenglamadagidek</h3>

<p>Yaxshi xabar: tengsizlik ham xuddi tenglama kabi yechiladi. Ikki tomonga bir xil
son qoʻshamiz, ayiramiz, koʻpaytiramiz yoki boʻlamiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + 3 &lt; 15</span>
    <span class="pm-solve__why">Berilgan tengsizlik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x &lt; 12</span>
    <span class="pm-solve__why">Ikki tomondan 3 ni ayirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x &lt; 6</span>
    <span class="pm-solve__why">Ikki tomonni 2 ga boʻldik — ishora oʻzgarmadi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Javob toʻplam boʻlgani uchun ikkita sonni sinaymiz. x = 5 (javob ichida):
  2 × 5 + 3 = 13 &lt; 15 ✓ x = 7 (javobdan tashqarida): 2 × 7 + 3 = 17 &lt; 15
  emas ✓ <b>Tengsizlikni shunday tekshiring:</b> bittasi ichkaridan, bittasi
  tashqaridan.</p>
</div>

<h3>5. Manfiy songa boʻlsangiz — ishora teskari</h3>

<p>Mana bu — butun darsdagi yagona yangi qoida va u juda muhim. Nega shunday
boʻlishini bir misolda koʻramiz.</p>

<p><b>3 &lt; 5</b> — bu rost. Endi ikkala tomonni <b>−1</b> ga koʻpaytiramiz:
chapda −3, oʻngda −5 chiqadi. Ammo <b>−3 &gt; −5</b>! Manfiy sonlarda tartib
teskari (PM-9): son oʻqida −3 oʻngroqda turadi.</p>

<div class="pm-num">
  <div class="pm-num__track">
    <span class="pm-num__tick" style="left:0%"><i>−5</i></span>
    <span class="pm-num__tick" style="left:25%"><i>−3</i></span>
    <span class="pm-num__tick" style="left:50%"><i>0</i></span>
    <span class="pm-num__tick" style="left:75%"><i>3</i></span>
    <span class="pm-num__tick" style="left:100%"><i>5</i></span>
  </div>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Faqat MANFIY songa koʻpaytirish yoki boʻlishda</p>
  <p>Musbat songa koʻpaytirsangiz ham, boʻlsangiz ham ishora oʻzgarmaydi. Qoʻshish
  va ayirishda ham hech nima oʻzgarmaydi. Ishora <b>faqat</b> manfiy songa
  koʻpaytirilganda yoki boʻlinganda teskari aylanadi.</p>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">−2x &lt; 6</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x &gt; −3</span>
    <span class="pm-solve__why">Ikki tomonni −2 ga boʻldik — ishora aylandi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Javob: x &gt; −3</span>
    <span class="pm-solve__why">Tekshirish: x = 0 → 0 &lt; 6 ✓; x = −4 → 8 &lt; 6 ✗</span>
  </div>
</div>

<h3>Matnli masala</h3>

<p><b>Sayohat byudjeti.</b> Sherbekning jami <b>200 000</b> soʻmi bor. Borish-kelish
yoʻl kirasi <b>45 000</b> soʻm, har bir kun uchun esa ovqat va boshqa xarajatga
<b>20 000</b> soʻm ketadi.</p>

<p><b>Savol:</b> u koʻpi bilan necha kun qolishi mumkin?</p>

<p><b>Reja:</b> kunlar sonini k deb olamiz. Xarajat pulidan oshmasligi kerak —
demak «≤» belgisi ishlatiladi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">45 000 + 20 000k ≤ 200 000</span>
    <span class="pm-solve__why">Xarajat butun puldan oshmasin</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">20 000k ≤ 155 000</span>
    <span class="pm-solve__why">Ikki tomondan 45 000 ni ayirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">k ≤ 7,75</span>
    <span class="pm-solve__why">Ikki tomonni 20 000 ga boʻldik (musbat — ishora
      oʻzgarmadi)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">k = 7 kun</span>
    <span class="pm-solve__why">Kun butun son — 7,75 dan pastga yaxlitlanadi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>7 kun: 45 000 + 140 000 = 185 000 ≤ 200 000 ✓ 8 kun: 45 000 + 160 000 =
  205 000 — bu 200 000 dan koʻp ✗ Demak koʻpi bilan 7 kun.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Yaxlitlash yoʻnalishi masalaga bogʻliq</p>
  <p>Bu yerda 7,75 ni <b>pastga</b> yaxlitladik, chunki 8 kun pulga yetmaydi. Agar
  savol «kamida nechta avtobus kerak?» boʻlganida va 7,75 chiqqanida, javob
  <b>8</b> boʻlardi — chunki 7 ta avtobusga hamma sigʻmaydi. Kalkulyator emas,
  <b>maʼno</b> yaxlitlash yoʻnalishini tanlaydi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">−3x &lt; 12 → x &lt; −4</p>
  <p class="pe-fix__good">−3x &lt; 12 → x &gt; −4</p>
  <p class="pe-fix__why">Manfiy songa boʻlinganda ishora teskari boʻladi. Tekshirish:
  x = 0 olsak, 0 &lt; 12 rost — demak nol javob ichida boʻlishi kerak, x &lt; −4
  esa uni tashqarida qoldiradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">«Kamida 60 ball» → ball &gt; 60</p>
  <p class="pe-fix__good">ball ≥ 60</p>
  <p class="pe-fix__why">«Kamida» degani chegaraning oʻzi ham mumkin. 60 ball olgan
  oʻquvchi oʻtadi, shuning uchun belgi ostida chiziqcha boʻlishi shart.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">2x + 3 &lt; 15 → x &lt; 9</p>
  <p class="pe-fix__good">2x &lt; 12 → x &lt; 6</p>
  <p class="pe-fix__why">Faqat 3 ayirilib, ikkiga boʻlish unutilgan. Tekshirish:
  x = 7 olsak 17 chiqadi va u 15 dan kichik emas.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. x + 5 &gt; 12 tengsizlikni yeching.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>x &gt; 7.</b> Ikki tomondan 5 ni ayirdik. Tekshirish: x = 8 → 13 &gt; 12 ✓;
    x = 7 → 12 &gt; 12 emas ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 3x ≤ 21 tengsizlikni yeching.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>x ≤ 7.</b> Ikki tomonni 3 ga boʻldik; 3 musbat — ishora oʻzgarmadi.
    x = 7 ham javob ichida.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. −4x ≥ 20 tengsizlikni yeching.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>x ≤ −5.</b> Manfiy songa boʻldik — ishora teskari aylandi. Tekshirish:
    x = −6 → 24 ≥ 20 ✓; x = 0 → 0 ≥ 20 ✗</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «Sumkaga koʻpi bilan 20 kg yuk solish mumkin. Unda
  allaqachon 12 kg bor». Yana qancha solish mumkinligini tengsizlik bilan yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>12 + m ≤ 20, demak m ≤ 8 kg.</b> «Koʻpi bilan» — ≤ belgisi. Roppa-rosa
    8 kilogramm ham mumkin.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Bir daftar 6000 soʻm. Afsonada 50 000 soʻm bor va u
  10 000 soʻmlik ruchka ham olmoqchi. Koʻpi bilan nechta daftar ola oladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>6 ta.</b> 10 000 + 6000d ≤ 50 000 → 6000d ≤ 40 000 → d ≤ 6,66…
    Daftar butun boʻlgani uchun 6 ta. Tekshirish: 10 000 + 36 000 = 46 000 ≤
    50 000 ✓; 7 ta boʻlsa 52 000 — yetmaydi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Tengsizlik</b><span>ikki ifoda orasidagi katta-kichik munosabat; ingl.
    inequality</span></li>
  <li><b>Qatʼiy tengsizlik</b><span>&lt; yoki &gt;, chegara kirmaydi; ingl. strict
    inequality</span></li>
  <li><b>Qatʼiy boʻlmagan</b><span>≤ yoki ≥, chegara kiradi; ingl. non-strict</span></li>
  <li><b>Yechimlar toʻplami</b><span>tengsizlikni rost qiladigan hamma son; ingl.
    solution set</span></li>
  <li><b>Chegara nuqta</b><span>toʻplamning boshi yoki oxiri; ingl. boundary</span></li>
  <li><b>Son oʻqi</b><span>sonlar tartib bilan joylashgan chiziq; ingl. number
    line</span></li>
  <li><b>Kamida</b><span>shu qiymat yoki undan koʻp, ≥; ingl. at least</span></li>
  <li><b>Koʻpi bilan</b><span>shu qiymat yoki undan kam, ≤; ingl. at most</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>«Kamida» → ≥, «koʻpi bilan» → ≤</b> — chegaraning oʻzi ham kiradi.</li>
    <li><b>Tengsizlik tenglama kabi yechiladi</b>, faqat manfiy songa koʻpaytirish
      yoki boʻlishda ishora teskari boʻladi.</li>
    <li><b>Javob — toʻplam:</b> uni son oʻqida koʻrsating va ikki son bilan
      tekshiring.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-41 — modul
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-41: Modul: sondan noldan masofagacha",
        "category": "math",
        "order": 41,
        "summary": (
            "|−5| nima uchun 5 ga teng. Modul — noldan masofa, shuning uchun u "
            "hech qachon manfiy boʻlmaydi. Ikki son orasidagi masofa va |x| = a "
            "koʻrinishidagi tenglamalar."
        ),
        "stories": ["Noldan qancha uzoq"],
        "content": """
<h2>PM-41: Modul: sondan noldan masofagacha</h2>

<p>Kecha havo −5 gradus edi, bugun +5. Qaysi kun noldan uzoqroq? Ikkalasi ham
<b>bir xil</b> — beshtadan. Biri sovuq tomonga, ikkinchisi issiq tomonga, lekin
noldan masofasi teng. Mana shu «noldan masofa» degan tushunchaning nomi —
<b>modul</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>modulni masofa sifatida tushunasiz;</li>
    <li>musbat va manfiy sonning modulini topasiz;</li>
    <li>ikki son orasidagi masofani modul bilan yozasiz;</li>
    <li>|x| = a koʻrinishidagi tenglamani yechasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Modul</span>
  <span class="pe-chip pe-chip--o">|5| = 5</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">|−5| = 5</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">|0| = 0</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--neg">modul hech qachon manfiy emas</span>
</div>

<h3>1. Modul — masofa, yoʻnalish emas</h3>

<p>Son oʻqida nolni markaz deb olamiz. Har bir sonning noldan qancha uzoqda turishi
— uning moduli. Yoʻnalish (oʻngdami, chapdami) hisobga olinmaydi.</p>

<div class="pm-num">
  <div class="pm-num__track">
    <span class="pm-num__band" style="left:25%;width:25%"></span>
    <span class="pm-num__tick" style="left:0%"><i>−10</i></span>
    <span class="pm-num__tick" style="left:25%"><i>−5</i></span>
    <span class="pm-num__tick" style="left:50%"><i>0</i></span>
    <span class="pm-num__tick" style="left:75%"><i>5</i></span>
    <span class="pm-num__tick" style="left:100%"><i>10</i></span>
    <span class="pm-num__dot" style="left:25%"></span>
    <span class="pm-num__dot" style="left:75%"></span>
  </div>
</div>

<p>Ikkala nuqta ham noldan besh qadam narida turibdi. Shuning uchun
<b>|−5| = 5</b> va <b>|5| = 5</b>.</p>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Modul minusni «yeb yubormaydi» — u masofani oʻlchaydi</p>
  <p>«Modul minusni tashlab yuboradi» degan qoida natijani toʻgʻri beradi, lekin
  sababini yashiradi. Toʻgʻri fikr shu: modul <b>qancha uzoq</b> degan savolga javob
  beradi, <b>qaysi tomonda</b> degan savolga emas. Masofa esa manfiy boʻlmaydi —
  «minus uch qadam yurdim» degan gap yoʻq.</p>
</div>

<h3>2. Modulning uchta oddiy xossasi</h3>

<div class="pe-table-wrap"><table>
  <tr><th>Xossa</th><th>Misol</th><th>Nega</th></tr>
  <tr><td>|a| ≥ 0 doim</td><td>|−7| = 7</td><td>masofa manfiy boʻlmaydi</td></tr>
  <tr><td>|a| = |−a|</td><td>|3| = |−3| = 3</td>
      <td>qarama-qarshi sonlar noldan teng uzoqlikda</td></tr>
  <tr><td>|0| = 0</td><td>—</td><td>nol nolning oʻzida turibdi</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Modul ichida avval hisoblanadi</p>
  <p>|3 − 8| ni hisoblash uchun avval qavs ichidagidek ish qilamiz: 3 − 8 = −5,
  keyin modul olamiz — javob <b>5</b>. Alohida-alohida modul olib |3| − |8| = −5
  qilish <b>xato</b>: modul chizigʻi qavs vazifasini ham bajaradi.</p>
</div>

<h3>3. Ikki son orasidagi masofa</h3>

<p>Modulning eng foydali qoʻllanishi shu: <b>|a − b|</b> — bu a va b orasidagi
masofa. Qaysi birini birinchi yozganingiz ahamiyatsiz, chunki javob baribir
musbat chiqadi.</p>

<div class="pe-ex">
  <p class="pe-ex__math">|7 − 3| = |4| = 4 va |3 − 7| = |−4| = 4</p>
  <p class="pe-ex__uz">Uch bilan yetti orasidagi masofa — toʻrt qadam.</p>
  <p class="pe-ex__why">Tartib almashsa ayirmaning ishorasi almashadi, lekin masofa
  oʻzgarmaydi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">|8 − (−5)| = |13| = 13</p>
  <p class="pe-ex__uz">Sakkiz gradus issiq bilan besh gradus sovuq orasida 13 gradus
  farq bor.</p>
  <p class="pe-ex__why">Nolning ikki tomonidagi sonlar orasidagi masofa ularning
  modullari yigʻindisiga teng: 8 + 5 = 13.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Katta sondan kichigini ayiring — modul kerak boʻlmaydi</p>
  <p>Ikki son orasidagi masofani hisoblayotganda kattasini birinchi yozsangiz,
  ayirma allaqachon musbat chiqadi va modulni yozib oʻtirmasangiz ham boʻladi.
  Modul esa tartibni oʻylab oʻtirmaslik imkonini beradi — ayniqsa harflar bilan
  ishlaganda, qaysi biri katta ekani nomaʼlum boʻlsa.</p>
</div>

<h3>4. |x| = a tenglamasi</h3>

<p>«Moduli 5 ga teng son qaysi?» degan savolga <b>ikkita</b> javob bor: 5 va −5.
Ikkalasi ham noldan besh qadam narida.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">|x| = 5</span>
    <span class="pm-solve__why">Noldan masofasi 5 ga teng sonlar</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 5 yoki x = −5</span>
    <span class="pm-solve__why">Oʻngda ham, chapda ham bittadan</span>
  </div>
</div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">|x| = 0</p>
    <p>Faqat bitta yechim: <b>x = 0</b>. Noldan nol qadam uzoqlikda turgan yagona
    son — nolning oʻzi.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">|x| = −3</p>
    <p><b>Yechimi yoʻq.</b> Masofa manfiy boʻlolmaydi, shuning uchun bunday x
    mavjud emas.</p>
  </div>
</div>

<h3>Matnli masala</h3>

<p><b>Harorat farqi.</b> Yanvar oyida bir kunda kunduzi harorat <b>+8</b> gradus,
kechasi esa <b>−5</b> gradus boʻldi. Ertasi kuni kunduzi <b>+3</b>, kechasi
<b>−1</b> gradus.</p>

<p><b>Savol:</b> qaysi kunning kunduzi bilan kechasi orasidagi farq katta va
qanchaga katta?</p>

<p><b>Reja:</b> har kun uchun ikki harorat orasidagi masofani modul bilan
hisoblaymiz, keyin ularni taqqoslaymiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">1-kun: |8 − (−5)| = |13| = 13</span>
    <span class="pm-solve__why">Manfiyni ayirish — qoʻshish (PM-10)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2-kun: |3 − (−1)| = |4| = 4</span>
    <span class="pm-solve__why">Ikkinchi kunning farqi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">13 − 4 = 9</span>
    <span class="pm-solve__why">Birinchi kunning farqi 9 gradusga katta</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Son oʻqida sanaymiz: −5 dan 0 gacha 5 qadam, 0 dan 8 gacha 8 qadam; jami
  13 ✓ Ikkinchi kun: 1 + 3 = 4 ✓ Modulsiz ham shu javob chiqdi — modul bu
  sanashning qisqa yozuvi.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Birinchi kun harorat noldan ancha narigacha borgan, ikkinchisida esa nolga
  yaqin turgan. Demak birinchi kunning farqi kattaroq boʻlishi kerak edi.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">|−5| = −5</p>
  <p class="pe-fix__good">|−5| = 5</p>
  <p class="pe-fix__why">Modul — masofa, u manfiy boʻlolmaydi. «Minus besh qadam
  uzoqlikda» degan gap maʼnosiz.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">|3 − 8| = |3| − |8| = −5</p>
  <p class="pe-fix__good">|3 − 8| = |−5| = 5</p>
  <p class="pe-fix__why">Modul chizigʻi qavs vazifasini bajaradi: avval ichidagi
  hisoblanadi. Va javob baribir musbat chiqishi kerak edi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">|x| = 7 → x = 7</p>
  <p class="pe-fix__good">x = 7 yoki x = −7</p>
  <p class="pe-fix__why">Ikkinchi yechim tushirib qoldirilgan. Noldan yetti qadam
  narida ikkita nuqta bor — biri oʻngda, biri chapda.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. |−12| ni hisoblang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>12.</b> Noldan oʻn ikki qadam uzoqlikda.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. |4 − 9| ni hisoblang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5.</b> Avval ichidagi: 4 − 9 = −5; keyin modul: |−5| = 5.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. |−6| + |−4| ni hisoblang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>10.</b> Har bir modul alohida olinadi: 6 + 4 = 10.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. |x| = 9 tenglamani yeching.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>x = 9 yoki x = −9.</b> Ikkala son ham noldan toʻqqiz qadam narida.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Muzxonada harorat −18 gradus, xonada +22 gradus. Ular
  orasidagi farq necha gradus?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>40 gradus.</b> |22 − (−18)| = |40| = 40. Nolning ikki tomonidagi sonlar
    boʻlgani uchun modullar qoʻshiladi: 22 + 18 = 40.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Modul</b><span>sonning noldan masofasi, |a|; ingl. absolute value</span></li>
  <li><b>Masofa</b><span>ikki nuqta orasidagi uzunlik; ingl. distance</span></li>
  <li><b>Qarama-qarshi sonlar</b><span>5 va −5 kabi juftlik; ingl. opposite
    numbers</span></li>
  <li><b>Manfiy son</b><span>noldan kichik son; ingl. negative number</span></li>
  <li><b>Musbat son</b><span>noldan katta son; ingl. positive number</span></li>
  <li><b>Ishora</b><span>sonning plyus yoki minusi; ingl. sign</span></li>
  <li><b>Son oʻqi</b><span>sonlar tartib bilan joylashgan chiziq; ingl. number
    line</span></li>
  <li><b>Farq</b><span>ikki qiymat orasidagi ayirma; ingl. difference</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Modul — noldan masofa</b>, shuning uchun u hech qachon manfiy
      boʻlmaydi.</li>
    <li><b>|a − b| — ikki son orasidagi masofa;</b> tartib ahamiyatsiz.</li>
    <li><b>|x| = a tenglamasining ikkita yechimi bor</b> (a &gt; 0 boʻlsa): a va
      −a.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-42 — daraja qonunlari
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-42: Daraja qonunlari",
        "category": "math",
        "order": 42,
        "summary": (
            "Bir xil asosli darajalarni koʻpaytirganda koʻrsatkichlar qoʻshiladi. "
            "Beshta qonun, a⁰ = 1 ning sababi va ulkan sonlarni 3 × 10⁸ "
            "koʻrinishida yozish."
        ),
        "stories": ["Koinot masofalarini yozishning qisqa yoʻli"],
        "content": """
<h2>PM-42: Daraja qonunlari</h2>

<p>PM-12 da darajani takroriy koʻpaytirishning qisqa yozuvi sifatida koʻrgan edik:
2<sup>3</sup> = 2 × 2 × 2. Endi savol boshqa: <b>darajalarni bir-biri bilan
qanday hisoblaymiz?</b> Javob shunchalik sodda va foydali ekanki, uni bilgan odam
Yerdan Quyoshgacha boʻlgan masofani bir qatorga sigʻdiradi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>bir xil asosli darajalarni koʻpaytirasiz va boʻlasiz;</li>
    <li>darajani darajaga koʻtarasiz;</li>
    <li>a<sup>0</sup> = 1 nima uchun ekanini tushunasiz;</li>
    <li>ulkan sonlarni standart koʻrinishda yozasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Asosiy qonunlar</span>
  <span class="pe-chip pe-chip--o">a<sup>m</sup> · a<sup>n</sup> = a<sup>m+n</sup></span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">a<sup>m</sup> ÷ a<sup>n</sup> = a<sup>m−n</sup></span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">(a<sup>m</sup>)<sup>n</sup> = a<sup>m·n</sup></span>
</div>

<h3>1. Koʻpaytirishda koʻrsatkichlar qoʻshiladi</h3>

<p>Qonunni yodlashning keragi yoʻq — uni har safar yozib chiqarish mumkin.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2<sup>3</sup> · 2<sup>4</sup></span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(2·2·2) · (2·2·2·2)</span>
    <span class="pm-solve__why">Har darajani yozib chiqdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 2<sup>7</sup> = 128</span>
    <span class="pm-solve__why">Jami yettita ikkilik: 3 + 4 = 7</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">ASOSLAR bir xil boʻlishi shart</p>
  <p>2<sup>3</sup> · 2<sup>4</sup> = 2<sup>7</sup>, lekin 2<sup>3</sup> ·
  3<sup>4</sup> ni bunday qisqartirib boʻlmaydi — asoslar har xil. Va koʻrsatkichlar
  faqat <b>koʻpaytirishda</b> qoʻshiladi: 2<sup>3</sup> + 2<sup>4</sup> = 8 + 16 = 24,
  bu 2<sup>7</sup> emas.</p>
</div>

<h3>2. Boʻlishda koʻrsatkichlar ayiriladi</h3>

<div class="pe-ex">
  <p class="pe-ex__math">3<sup>5</sup> ÷ 3<sup>2</sup> = 3<sup>3</sup> = 27</p>
  <p class="pe-ex__uz">Beshta uchlikdan ikkitasi qisqardi, uchtasi qoldi.</p>
  <p class="pe-ex__why">243 ÷ 9 = 27 — oddiy hisob ham shu javobni beradi.</p>
</div>

<h3>3. Darajani darajaga koʻtarish</h3>

<div class="pe-ex">
  <p class="pe-ex__math">(2<sup>3</sup>)<sup>2</sup> = 2<sup>3</sup> · 2<sup>3</sup>
    = 2<sup>6</sup> = 64</p>
  <p class="pe-ex__uz">Sakkizning kvadrati — oltmish toʻrt.</p>
  <p class="pe-ex__why">Koʻrsatkichlar bu safar koʻpaytiriladi: 3 × 2 = 6.</p>
</div>

<p>Yana ikkita foydali qonun: koʻpaytmani darajaga koʻtarganda har bir koʻpaytuvchi
darajaga koʻtariladi — <b>(ab)<sup>n</sup> = a<sup>n</sup>b<sup>n</sup></b>.
Masalan (2 × 5)<sup>3</sup> = 10<sup>3</sup> = 1000, va 2<sup>3</sup> ×
5<sup>3</sup> = 8 × 125 = 1000 ✓</p>

<h3>4. a<sup>0</sup> = 1 — nega shunday?</h3>

<p>Bu qoida sunʼiy koʻrinadi, lekin u boʻlish qonunidan <b>oʻzi kelib chiqadi</b>.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2<sup>3</sup> ÷ 2<sup>3</sup></span>
    <span class="pm-solve__why">Bir xil sonni oʻziga boʻlyapmiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">8 ÷ 8 = 1</span>
    <span class="pm-solve__why">Oddiy hisob shuni beradi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2<sup>3−3</sup> = 2<sup>0</sup></span>
    <span class="pm-solve__why">Qonun bilan hisoblasak shu chiqadi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2<sup>0</sup> = 1</span>
    <span class="pm-solve__why">Ikki yoʻl bir xil javob berishi uchun shunday
      boʻlishi shart</span>
  </div>
</div>

<p>Xuddi shu mulohaza manfiy koʻrsatkichni ham tushuntiradi: 2<sup>2</sup> ÷
2<sup>5</sup> = 4 ÷ 32 = 1/8, qonun bilan esa 2<sup>−3</sup>. Demak
<b>2<sup>−3</sup> = 1/8</b> — manfiy koʻrsatkich «pastga», maxrajga tushishni
bildiradi.</p>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Qonunni unutsangiz — yozib chiqing</p>
  <p>Imtihonda qaysi qonunda qoʻshish, qaysinisida koʻpaytirish ekanini
  chalkashtirsangiz, kichik sonlarda tekshiring: 2<sup>2</sup> · 2<sup>3</sup> ni
  4 × 8 = 32 deb hisoblang va 32 = 2<sup>5</sup> ekanini koʻring. Uch sekund vaqt,
  toʻliq ishonch.</p>
</div>

<h3>5. Standart koʻrinish — ulkan sonlarni yozish</h3>

<p>Yorugʻlik sekundiga 300 000 kilometr yuradi. Yerdan Quyoshgacha 150 000 000
kilometr. Bunday sonlarni yozishda nollarni sanash oson emas, shuning uchun ular
<b>standart koʻrinish</b>da yoziladi: <b>1 dan 10 gacha boʻlgan son × 10 ning
darajasi</b>.</p>

<div class="pe-table-wrap"><table>
  <tr><th>Oddiy yozuv</th><th>Standart koʻrinish</th><th>Nima bu</th></tr>
  <tr><td>1000</td><td>10<sup>3</sup></td><td>uchta nol</td></tr>
  <tr><td>300 000</td><td>3 × 10<sup>5</sup></td><td>yorugʻlik tezligi, km/s</td></tr>
  <tr><td>150 000 000</td><td>1,5 × 10<sup>8</sup></td>
      <td>Yer–Quyosh masofasi, km</td></tr>
  <tr><td>0,001</td><td>10<sup>−3</sup></td><td>mingdan bir</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">10 ning darajasi — nollar soni</p>
  <p>10<sup>5</sup> = 100 000, yaʼni beshta nol. Shuning uchun standart koʻrinishga
  oʻtish oson: vergulni birinchi raqamdan keyin qoʻying va vergul necha xona
  surilganini sanang — oʻsha son koʻrsatkich boʻladi.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Quyosh nuri qancha vaqtda yetib keladi?</b> Yorugʻlik sekundiga
<b>3 × 10<sup>5</sup></b> kilometr yuradi. Yerdan Quyoshgacha
<b>1,5 × 10<sup>8</sup></b> kilometr.</p>

<p><b>Savol:</b> Quyoshdan chiqqan nur Yerga necha daqiqada yetib keladi?</p>

<p><b>Reja:</b> PM-35 dagi formula ishlaydi — t = S ÷ v. Standart koʻrinishdagi
sonlarni boʻlishda koʻrsatkichlar ayiriladi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">t = (1,5 × 10<sup>8</sup>) ÷ (3 × 10<sup>5</sup>)</span>
    <span class="pm-solve__why">Masofani tezlikka boʻldik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= (1,5 ÷ 3) × 10<sup>8−5</sup></span>
    <span class="pm-solve__why">Sonlar alohida, darajalar alohida</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= 0,5 × 10<sup>3</sup> = 500 sekund</span>
    <span class="pm-solve__why">Yarim ming — besh yuz sekund</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">500 ÷ 60 ≈ 8 daqiqa 20 sekund</span>
    <span class="pm-solve__why">Sekundlarni daqiqaga aylantirdik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Teskari yoʻl: 3 × 10<sup>5</sup> × 500 = 1500 × 10<sup>5</sup> =
  1,5 × 10<sup>8</sup> ✓ Va 8 daqiqa 20 sekund — 8 × 60 + 20 = 500 sekund ✓
  Bu haqiqiy qiymat: quyosh nuri bizga taxminan sakkiz yarim daqiqada yetib
  keladi.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>10<sup>8</sup> ni 10<sup>5</sup> ga boʻlsak 10<sup>3</sup>, yaʼni ming
  atrofida chiqadi. Oldidagi 1,5 ÷ 3 esa yarimga teng — demak javob ming emas,
  besh yuz atrofida.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">2<sup>3</sup> · 2<sup>4</sup> = 2<sup>12</sup></p>
  <p class="pe-fix__good">2<sup>3</sup> · 2<sup>4</sup> = 2<sup>7</sup></p>
  <p class="pe-fix__why">Koʻpaytirishda koʻrsatkichlar <b>qoʻshiladi</b>, koʻpaytmaydi.
  Tekshirish: 8 × 16 = 128 va 2<sup>7</sup> = 128 ✓, 2<sup>12</sup> esa 4096.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">3<sup>2</sup> · 4<sup>2</sup> = 12<sup>4</sup></p>
  <p class="pe-fix__good">3<sup>2</sup> · 4<sup>2</sup> = 12<sup>2</sup> = 144</p>
  <p class="pe-fix__why">Koʻrsatkichlar bir xil boʻlsa, asoslar koʻpaytiriladi,
  koʻrsatkich esa oʻzgarmaydi. Tekshirish: 9 × 16 = 144 ✓</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">5<sup>0</sup> = 0</p>
  <p class="pe-fix__good">5<sup>0</sup> = 1</p>
  <p class="pe-fix__why">Nolinchi daraja bir beradi, chunki 5<sup>2</sup> ÷
  5<sup>2</sup> = 25 ÷ 25 = 1 va u qonun boʻyicha 5<sup>0</sup> ga teng.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 3<sup>2</sup> · 3<sup>4</sup> ni daraja koʻrinishida
  yozing va hisoblang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3<sup>6</sup> = 729.</b> 2 + 4 = 6. Tekshirish: 9 × 81 = 729 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 5<sup>7</sup> ÷ 5<sup>5</sup> ni hisoblang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5<sup>2</sup> = 25.</b> 7 − 5 = 2.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. (10<sup>2</sup>)<sup>3</sup> ni hisoblang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>10<sup>6</sup> = 1 000 000.</b> Koʻrsatkichlar koʻpaytiriladi:
    2 × 3 = 6.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 7 000 000 ni standart koʻrinishda yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>7 × 10<sup>6</sup>.</b> Yettidan keyin oltita nol bor.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Bir bakteriya har soatda ikkiga boʻlinadi. Boshida bitta
  bakteriya bor edi. 10 soatdan keyin nechta boʻladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>2<sup>10</sup> = 1024 ta.</b> Har soat soni ikki barobar oshadi:
    1 → 2 → 4 → 8… Oʻn soatdan keyin 2<sup>10</sup>. Bu — mingdan koʻp: daraja
    shunchalik tez oʻsadi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Daraja</b><span>takroriy koʻpaytirishning qisqa yozuvi; ingl. power</span></li>
  <li><b>Asos</b><span>koʻpaytiriladigan son, 2<sup>3</sup> dagi 2; ingl. base</span></li>
  <li><b>Koʻrsatkich</b><span>necha marta koʻpaytirilishi, 2<sup>3</sup> dagi 3;
    ingl. exponent</span></li>
  <li><b>Standart koʻrinish</b><span>a × 10<sup>n</sup> shakli; ingl. standard
    form</span></li>
  <li><b>Nolinchi daraja</b><span>har qanday sonning nolinchi darajasi 1; ingl. zero
    power</span></li>
  <li><b>Manfiy koʻrsatkich</b><span>maxrajga tushishni bildiradi; ingl. negative
    exponent</span></li>
  <li><b>Kvadrat</b><span>ikkinchi daraja; ingl. square</span></li>
  <li><b>Kub</b><span>uchinchi daraja; ingl. cube</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Koʻpaytirishda qoʻshiladi, boʻlishda ayiriladi</b>, darajaga
      koʻtarilganda koʻpaytiriladi — asoslar bir xil boʻlsa.</li>
    <li><b>a<sup>0</sup> = 1</b>, chunki a<sup>n</sup> ÷ a<sup>n</sup> = 1.</li>
    <li><b>Standart koʻrinish:</b> 150 000 000 = 1,5 × 10<sup>8</sup> — nollarni
      sanash oʻrniga koʻrsatkichni oʻqing.</li>
  </ul>
</div>
""",
    },
]
