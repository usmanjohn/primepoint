# -*- coding: utf-8 -*-
"""Prime SAT Math — lessons 71–75 (maxsus uchburchaklar, oʻxshashlik, trigonometriya).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_SAT.md
Lesson list: tutorial/management/commands/toc_prime_sat_math.txt

⚠️ SARLAVHALAR BAZADAN OLINGAN, aynan.

⚠️ BLOK D QOIDASI: har bir darsda formula varagʻida NIMA BOR va NIMA YOʻQ.
   Bu batchda taqsimot ayniqsa muhim:
     SAT-71, SAT-72 — maxsus uchburchaklar VARAQDA BOR (chizmasi bilan).
     SAT-73, SAT-74, SAT-75 — hech biri varaqda YOʻQ. SOH-CAH-TOA yodda
     boʻlishi shart.

⚠️ Chizmalar inline SVG — hech qachon rasm fayli emas. Har bir chizma
   haqiqiy geometriyaga mos boʻlishi shart (gate uni oʻlchaydi).

  • SAT-71 — 45-45-90 nisbati 1 : 1 : √2.
  • SAT-72 — 30-60-90 nisbati 1 : √3 : 2.
  • SAT-73 — uchburchak tengsizligi va oʻxshashlik (AA, SAS).
  • SAT-74 — tenglik, va masshtabda perimetr ×k, yuza ×k².
  • SAT-75 — sinus, kosinus, tangens; SOH-CAH-TOA.
  • ⛔ Trigonometrik ayniyat (SAT-76) YOʻQ; radian (SAT-77) YOʻQ.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_sat_71_75.py \\
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
    # SAT-71 — 45-45-90
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-71: Special Right Triangles — 45-45-90",
        "category": "math",
        "order": 71,
        "summary": (
            "Teng yonli toʻgʻri burchakli uchburchak: katetlar teng, gipotenuza "
            "esa katetning √2 barobari. Bu nisbat varaqda bor."
        ),
        "stories": ["The Diagonal That Broke the Rule"],
        "content": """
<h2>SAT-71: Special Right Triangles — 45-45-90</h2>

<p>Bu uchburchakni siz allaqachon koʻrgansiz: SAT-69 dagi teng yonli
uchburchakning uchidagi burchagi toʻgʻri burchak boʻlsa, aynan shu chiqadi.
Va uning nisbati <mark>formula varagʻida chizma bilan berilgan</mark>.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Formula varagʻi</span>
  <p><b>VARAQDA BOR:</b> 45-45-90 uchburchagi, tomonlari
  <em>x</em>, <em>x</em>, <em>x</em>√2 deb belgilangan chizma bilan.</p>
  <p>Demak nisbatni yodlash <b>shart emas</b> — lekin uni chizmaga toʻgʻri
  qoʻyish kerak, va varaqni ochib qarash vaqt oladi. Tanib olgan
  oʻquvchi 20 soniya tejaydi.</p>
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>ikki katet teng ekanini darrov koʻrasiz;</li>
    <li>katetdan gipotenuzani <b>koʻpaytirib</b> topasiz;</li>
    <li>gipotenuzadan katetni <b>boʻlib</b> topasiz;</li>
    <li>kvadrat diagonalini bir qadamda yozasiz.</li>
  </ul>
</div>

<figure class="pm-fig">
  <svg viewBox="0 0 320 180" role="img"
       aria-label="A right isosceles triangle: the right angle at the bottom
                   left, two equal legs, and two 45 degree angles">
    <line class="pm-ln" x1="80" y1="140" x2="200" y2="140"/>
    <line class="pm-ln" x1="80" y1="140" x2="80" y2="20"/>
    <line class="pm-ln" x1="200" y1="140" x2="80" y2="20"/>
    <line class="pm-ln" x1="80" y1="128" x2="92" y2="128"/>
    <line class="pm-ln" x1="92" y1="128" x2="92" y2="140"/>
    <text class="pm-lbl" x="176" y="132">45°</text>
    <text class="pm-lbl" x="86"  y="42">45°</text>
    <text class="pm-lbl" x="130" y="156">x</text>
    <text class="pm-lbl" x="60"  y="84">x</text>
    <text class="pm-lbl" x="146" y="80">x√2</text>
  </svg>
  <figcaption>Ikki katet teng va ikki burchak 45°. Gipotenuza katetning
  √2 barobari — taxminan 1.414 marta uzun.</figcaption>
</figure>

<div class="pe-formula">
  <span class="pe-formula__label">The ratio</span>
  <span class="pe-chip pe-chip--v">x</span>
  <span class="pe-op">:</span>
  <span class="pe-chip pe-chip--v">x</span>
  <span class="pe-op">:</span>
  <span class="pe-chip pe-chip--s">x√2</span>
</div>

<h3>Ikki yoʻnalish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Katet 7 → gipotenuza 7√2</span>
    <span class="pm-solve__why">Katetdan gipotenuzaga: <b>koʻpaytiriladi</b></span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Gipotenuza 10 → katet 10 ÷ √2</span>
    <span class="pm-solve__why">Gipotenuzadan katetga: <b>boʻlinadi</b></span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">10 ÷ √2 = 5√2</span>
    <span class="pm-solve__why">Maxrajdagi ildizdan qutuldik (SAT-26)</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Gipotenuza katetdan <b>uzunroq</b> boʻlishi shart. Javobingiz gipotenuza
  uchun katetdan kichik chiqsa, koʻpaytirish va boʻlishni almashtirgansiz —
  bu darsdagi asosiy xato.
</div>

<h3>Kvadrat diagonali</h3>

<p>Kvadratning diagonali uni ikkita 45-45-90 uchburchagiga boʻladi, va
tomonlar katet boʻlib qoladi. Demak <b>diagonal = tomon × √2</b>. Tomoni 6
boʻlgan kvadratning diagonali 6√2, taxminan 8.49.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu Pifagorning oʻzi (SAT-70), faqat tayyor koʻrinishda: 6² + 6² = 72, va
  √72 = 6√2. Maxsus uchburchak nisbati shu hisobni <b>bir qadamga</b>
  qisqartiradi — natija bir xil.
</div>

<h3>Kvadrat ichidagi uchburchak</h3>

<p>SAT bu uchburchakni koʻpincha yolgʻiz bermaydi. U kvadrat, toʻgʻri
toʻrtburchak yoki teng yonli uchburchak ichida yashiringan boʻladi, va
birinchi ish uni <b>koʻrish</b>.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Shakl</th><th>45-45-90 qayerda</th></tr>
  <tr><td>kvadrat</td><td class="pm-word__sym">diagonal ikkita hosil qiladi</td></tr>
  <tr><td>teng yonli toʻgʻri burchakli uchburchak</td>
      <td class="pm-word__sym">shaklning oʻzi</td></tr>
  <tr><td>toʻgʻri toʻrtburchak</td>
      <td class="pm-word__sym">faqat kvadrat boʻlganda</td></tr>
</table></div>

<p>Uchinchi qator eʼtiborni talab qiladi: har qanday toʻrtburchakning
diagonali 45-45-90 bermaydi — faqat tomonlari teng boʻlganda.</p>

<h3>Yuza va perimetr</h3>

<p>Bu uchburchakning yuzasi ham oson: ikki katet teng, va toʻgʻri burchakli
uchburchakda ular asos va balandlik boʻlib xizmat qiladi. Katet 6 boʻlsa,
yuza 6 marta 6 ning yarmi — yaʼni 18.</p>

<p>Perimetri esa ikki katet va gipotenuza: 6 + 6 + 6√2, yaʼni 12 + 6√2 ≈
20.49. SAT baʼzan perimetrni ildiz koʻrinishida qoldirishni soʻraydi, va
javob variantlari aynan shu shaklda beriladi.</p>

<p>Nihoyat, bu uchburchak <b>yarim kvadrat</b> ekanini eslang. Kvadratni
diagonal boʻylab kessangiz ikkita bir xil 45-45-90 hosil boʻladi, va
ularning yuzasi kvadratning yarmi. Shuning uchun tomoni 8 boʻlgan kvadrat
kesilganda har bir uchburchakning yuzasi 32 boʻladi — 64 ning yarmi.</p>

<p>Va bir amaliy eslatma: √2 ni oʻnli kasrga aylantirish kerak boʻlsa,
1.41 yetarli. Kalkulyator aniqroq beradi, lekin SAT javob variantlari
odatda bir-biridan ancha uzoq turadi — 7√2 ni 9.9 deb baholash toʻgʻri
variantni tanlash uchun kifoya.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>an isosceles right triangle</b><span>teng yonli toʻgʻri burchakli uchburchak</span></li>
  <li><b>the diagonal of a square</b><span>kvadratning diagonali</span></li>
  <li><b>in simplest radical form</b><span>eng sodda ildiz koʻrinishida</span></li>
  <li><b>the legs are congruent</b><span>katetlar teng</span></li>
  <li><b>to the nearest tenth</b><span>oʻndan bir aniqlikda</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>In a 45-45-90 triangle, each leg measures 7. What is the length of the
    hypotenuse?</p>
  </div>
  <ol class="ps-ch">
    <li>7√2</li>
    <li>14</li>
    <li>7 ÷ √2</li>
    <li>49√2</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 7√2</p>
      <p>Nisbat x : x : x√2, demak gipotenuza katetning √2 barobari.</p>
      <p>Tekshiruv: 49 + 49 = 98, va √98 = 7√2 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">14</span>
  <span class="ps-trap__why">Katetlar qoʻshilgan. Gipotenuza har doim
  katetlar yigʻindisidan <b>kichik</b> (SAT-70): 7√2 ≈ 9.9.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>A square has a diagonal of length 8. What is the length of each side?</p>
  </div>
  <ol class="ps-ch">
    <li>4√2</li>
    <li>8√2</li>
    <li>4</li>
    <li>16</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 4√2</p>
      <p>Diagonal gipotenuza: 8 ÷ √2 = 4√2 ≈ 5.66.</p>
      <p>Tekshiruv: 4√2 kvadratga koʻtarilsa 32; ikkitasi 64, va √64 = 8 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">8√2</span>
  <span class="ps-trap__why">Boʻlish oʻrniga koʻpaytirilgan. Tomon
  diagonaldan <b>qisqa</b> boʻlishi kerak, 8√2 ≈ 11.3 esa uzunroq.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Har safar bitta savol bering: <b>izlanayotgani gipotenuzami?</b></p>
  <ol>
    <li>Ha boʻlsa — katetni <b>√2 ga koʻpaytiring</b>;</li>
    <li>Yoʻq boʻlsa — gipotenuzani <b>√2 ga boʻling</b>;</li>
    <li>Javobni oʻlchamga qarab tekshiring: gipotenuza uzunroq.</li>
  </ol>
  <p>√2 ≈ 1.41 ni yodda tuting — u javob variantlarini taqqoslashda
  yordam beradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Katet 7 → gipotenuza 14</p>
  <p class="pe-good">7√2 ≈ 9.9</p>
  <p class="pe-fix__why">Katetlar qoʻshilmaydi; nisbat √2 barobar.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Diagonal 8 → tomon 8√2</p>
  <p class="pe-good">8 ÷ √2 = 4√2</p>
  <p class="pe-fix__why">Gipotenuzadan katetga oʻtganda boʻlinadi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Javob koʻpincha <b>ildiz koʻrinishida</b> qoldiriladi: 4√2, 7√2. Uni oʻnli
  kasrga aylantirmang — SAT variantlari aniq koʻrinishda beriladi, va
  yaxlitlangan javob ular orasida boʻlmaydi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu uchburchak <b>teng yonli</b> (SAT-69) va <b>toʻgʻri burchakli</b>
  (SAT-70) — ikki dars bir shaklda uchrashadi. Shuning uchun uning ikki
  burchagi albatta 45 dan: 180 − 90 ni ikkiga boʻlish.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  A 45-45-90 triangle has legs of 5. What is the hypotenuse?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">5√2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  A 45-45-90 triangle has a hypotenuse of 6√2. What is each leg?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">6 — √2 ga boʻlinadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A square has side 9. What is its diagonal?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">9√2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  A square has diagonal 10. What is its area?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">50 — tomoni 10 ÷ √2 = 5√2, va uning kvadrati
  50.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Why are the two acute angles in this triangle always 45°?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Katetlar teng, demak ularga qarshi burchaklar teng;
  180 − 90 ni ikkiga boʻling.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>isosceles right triangle</b><span>teng yonli toʻgʻri burchakli</span></li>
  <li><b>leg</b><span>katet</span></li>
  <li><b>hypotenuse</b><span>gipotenuza</span></li>
  <li><b>diagonal</b><span>diagonal</span></li>
  <li><b>congruent legs</b><span>teng katetlar</span></li>
  <li><b>simplest radical form</b><span>eng sodda ildiz koʻrinishi</span></li>
  <li><b>the ratio of the sides</b><span>tomonlar nisbati</span></li>
  <li><b>reference sheet</b><span>formula varagʻi</span></li>
  <li><b>rationalize</b><span>maxrajni ildizdan tozalash</span></li>
  <li><b>approximately</b><span>taxminan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Nisbat <b>x : x : x√2</b> — va u varaqda bor.</li>
    <li>Katetdan gipotenuzaga <b>koʻpaytiring</b>, teskarisiga
        <b>boʻling</b>.</li>
    <li>Kvadrat diagonali = <b>tomon × √2</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-72 — 30-60-90
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-72: Special Right Triangles — 30-60-90",
        "category": "math",
        "order": 72,
        "summary": (
            "Nisbat 1 : √3 : 2, va tartib muhim — qaysi tomon qaysi burchakka "
            "qarshi turganini aniqlash butun savolni hal qiladi."
        ),
        "stories": ["Six Triangles in Every Cell"],
        "content": """
<h2>SAT-72: Special Right Triangles — 30-60-90</h2>

<p>Ikkinchi maxsus uchburchak. U ham <mark>formula varagʻida bor</mark>, va
uning yagona qiyinligi bitta: <b>uch tomon uch xil</b>, demak qaysi biri
berilganini aniqlash kerak.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Formula varagʻi</span>
  <p><b>VARAQDA BOR:</b> 30-60-90 uchburchagi, tomonlari <em>x</em>,
  <em>x</em>√3, 2<em>x</em> deb belgilangan chizma bilan.</p>
  <p>Chizma ham berilgani muhim: u qaysi tomon qaysi burchakka qarshi
  turishini koʻrsatadi. Yodlangan nisbat esa tartibsiz qolishi mumkin.</p>
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>uch tomonni burchagiga qarab joylashtirasiz;</li>
    <li>qaysi tomon berilganini aniqlab, qolganini bir qadamda topasiz;</li>
    <li>teng tomonli uchburchak balandligini chiqarasiz;</li>
    <li>ikki maxsus uchburchakni bir-biridan ajratasiz.</li>
  </ul>
</div>

<figure class="pm-fig">
  <svg viewBox="0 0 320 180" role="img"
       aria-label="A 30-60-90 triangle: the right angle at the bottom left, the
                   short side vertical, the long side horizontal, and the
                   hypotenuse joining them">
    <line class="pm-ln" x1="100" y1="150" x2="221" y2="150"/>
    <line class="pm-ln" x1="100" y1="150" x2="100" y2="80"/>
    <line class="pm-ln" x1="100" y1="80" x2="221" y2="150"/>
    <line class="pm-ln" x1="100" y1="138" x2="112" y2="138"/>
    <line class="pm-ln" x1="112" y1="138" x2="112" y2="150"/>
    <text class="pm-lbl" x="196" y="142">30°</text>
    <text class="pm-lbl" x="106" y="100">60°</text>
    <text class="pm-lbl" x="78"  y="118">x</text>
    <text class="pm-lbl" x="152" y="166">x√3</text>
    <text class="pm-lbl" x="164" y="106">2x</text>
  </svg>
  <figcaption>Eng qisqa tomon 30° ga qarshi, oʻrtacha tomon 60° ga qarshi,
  gipotenuza esa 90° ga qarshi turadi.</figcaption>
</figure>

<div class="pe-formula">
  <span class="pe-formula__label">The ratio, in angle order</span>
  <span class="pe-chip pe-chip--v">30° → x</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">60° → x√3</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">90° → 2x</span>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Nisbatni <b>burchaklar tartibida</b> yodlang, tomonlar tartibida emas.
  Har bir tomon oʻzining qarshisidagi burchak bilan bogʻlangan: eng kichik
  burchakka eng qisqa tomon (SAT-69).
</div>

<h3>Uch yoʻnalish</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Berilgani</th><th>Qanday topiladi</th><th>Misol: berilgan 4</th></tr>
  <tr><td>qisqa tomon (x)</td><td class="pm-word__sym">boshqalari darrov</td>
      <td>4, 4√3, 8</td></tr>
  <tr><td>gipotenuza (2x)</td><td class="pm-word__sym">ikkiga boʻling</td>
      <td>2, 2√3, 4</td></tr>
  <tr><td>uzun tomon (x√3)</td><td class="pm-word__sym">√3 ga boʻling</td>
      <td>4÷√3, 4, 8÷√3</td></tr>
</table></div>

<p>Eng oson yoʻl har doim bitta: <b>avval x ni toping</b>, keyin qolgan
ikkitasini yozing. Qaysi tomon berilganidan qatʼi nazar, x topilgach ish
tugaydi.</p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Bu uchburchakda tomonlar <b>teng emas</b> — 45-45-90 dan asosiy farqi shu.
  «Gipotenuza katetning ikki barobari» degan qoida faqat <b>qisqa</b> katet
  uchun toʻgʻri; uzun katet uchun emas.
</div>

<h3>Teng tomonli uchburchakning balandligi</h3>

<p>Teng tomonli uchburchakni balandlik bilan ikkiga boʻlsangiz, aynan ikkita
30-60-90 hosil boʻladi. Asos yarmiga boʻlinadi va u qisqa tomon boʻladi;
tomonning oʻzi gipotenuza; balandlik esa uzun tomon.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Teng tomonli uchburchak tomoni 10</span>
    <span class="pm-solve__why">Gipotenuza 10, demak x = 5</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Balandlik = 5√3 ≈ 8.66</span>
    <span class="pm-solve__why">Tekshiruv: 25 + 75 = 100 ✓</span>
  </div>
</div>

<h3>Ikki maxsus uchburchakni taqqoslash</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th></th><th>45-45-90</th><th>30-60-90</th></tr>
  <tr><td>katetlar</td><td class="pm-word__sym">teng</td><td>har xil</td></tr>
  <tr><td>nisbat</td><td class="pm-word__sym">1 : 1 : √2</td><td>1 : √3 : 2</td></tr>
  <tr><td>qayerdan chiqadi</td><td class="pm-word__sym">kvadrat</td>
      <td>teng tomonli uchburchak</td></tr>
</table></div>

<p>Ikkalasi ham varaqda bor va ikkalasi ham yonma-yon chizilgan — shuning
uchun ularni <b>notoʻgʻri tanlash</b> xavfi yodlashdan koʻra kattaroq.
Burchakka qarang, keyin varaqqa.</p>

<h3>Yuzasi</h3>

<p>Bu uchburchakning ikki kateti bir-biriga perpendikulyar, demak ular asos
va balandlik. Qisqa katet x, uzuni x√3 boʻlsa, yuza ularning
koʻpaytmasining yarmi.</p>

<p>Masalan x = 4 boʻlsa, katetlar 4 va 4√3, va yuza 8√3 ≈ 13.86. Gipotenuza
(bu yerda 8) yuzaga umuman kirmaydi — u asos ham, balandlik ham emas.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>the side opposite the 30° angle</b><span>30° ga qarshi turgan tomon</span></li>
  <li><b>the shorter leg</b><span>qisqa katet</span></li>
  <li><b>the altitude of an equilateral triangle</b><span>teng tomonli uchburchak balandligi</span></li>
  <li><b>in simplest radical form</b><span>eng sodda ildiz koʻrinishida</span></li>
  <li><b>half of an equilateral triangle</b><span>teng tomonli uchburchakning yarmi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>In a 30-60-90 triangle, the side opposite the 30° angle measures 4. What
    is the length of the hypotenuse?</p>
  </div>
  <ol class="ps-ch">
    <li>8</li>
    <li>4√3</li>
    <li>2</li>
    <li>4√2</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 8</p>
      <p>30° ga qarshi turgani qisqa tomon, demak x = 4 va gipotenuza 2x.</p>
      <p><b>4√3</b> — bu uzun katet, gipotenuza emas.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">4√2</span>
  <span class="ps-trap__why">45-45-90 nisbati qoʻllangan. Ikki maxsus
  uchburchakni chalkashtirmang: bu yerda √3 va 2 ishlaydi, √2 emas.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">65 s</span></p>
  <div class="ps-stem__q">
    <p>An equilateral triangle has sides of length 12. What is its altitude?</p>
  </div>
  <ol class="ps-ch">
    <li>6√3</li>
    <li>12√3</li>
    <li>6</li>
    <li>6√2</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 6√3</p>
      <p>Balandlik uchburchakni ikkita 30-60-90 ga boʻladi. Gipotenuza 12,
      demak x = 6, va balandlik x√3.</p>
      <p>Tekshiruv: 36 + 108 = 144 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">6</span>
  <span class="ps-trap__why">Bu asosning yarmi — qisqa tomon, balandlik
  emas. Balandlik 60° ga qarshi turadi va u uzunroq.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Uch qadam, har safar bir xil:</p>
  <ol>
    <li>Berilgan tomon <b>qaysi burchakka qarshi</b> turibdi?</li>
    <li>Undan <b>x ni toping</b> (qisqa tomonni);</li>
    <li>Qolgan ikkitasini yozing: x√3 va 2x.</li>
  </ol>
  <p>√3 ≈ 1.73 ni yodda tuting — javoblarni taqqoslashda kerak
  boʻladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Uzun katet 4 → gipotenuza 8</p>
  <p class="pe-good">Avval x = 4 ÷ √3, keyin gipotenuza 2x</p>
  <p class="pe-fix__why">«Ikki barobar» qoidasi faqat <b>qisqa</b> katetga
  tegishli.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">30-60-90 da gipotenuza katet × √2</p>
  <p class="pe-good">√2 — bu 45-45-90 niki</p>
  <p class="pe-fix__why">Bu uchburchakda √3 va 2 ishlaydi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikki maxsus uchburchakni ajratishning eng tez belgisi — <b>burchaklar</b>.
  45 koʻrsangiz √2 ni oling; 30 yoki 60 koʻrsangiz √3 va 2 ni. Chizmada
  burchak yozilmagan boʻlsa, tomonlarga qarang: ikkitasi teng boʻlsa —
  45-45-90.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Teng tomonli uchburchakning yuzasi ham shundan chiqadi: tomoni <em>a</em>
  boʻlsa, balandligi <em>a</em>√3 ÷ 2, va yuzasi asos-marta-balandlikning
  yarmi. Formulani yodlash shart emas — balandlikni topib, oddiy yuza
  formulasini ishlating (u varaqda bor).
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  In a 30-60-90 triangle, the short leg is 6. What are the other two sides?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">6√3 va 12.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  The hypotenuse of a 30-60-90 triangle is 14. What is the short leg?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">7 — gipotenuza ikkiga boʻlinadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  An equilateral triangle has sides of 8. What is its altitude?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">4√3.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  In a 30-60-90 triangle the long leg is 9√3. What is the short leg?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">9 — √3 ga boʻlinadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Which is longer in a 30-60-90 triangle: the side opposite 60° or the
  hypotenuse?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Gipotenuza — 2 va √3 ≈ 1.73 ni solishtiring.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>the shorter leg</b><span>qisqa katet</span></li>
  <li><b>the longer leg</b><span>uzun katet</span></li>
  <li><b>opposite the angle</b><span>burchakka qarshi turgan</span></li>
  <li><b>altitude</b><span>balandlik</span></li>
  <li><b>equilateral</b><span>teng tomonli</span></li>
  <li><b>bisects</b><span>teng ikkiga boʻladi</span></li>
  <li><b>the ratio 1 to √3 to 2</b><span>1 : √3 : 2 nisbati</span></li>
  <li><b>half of an equilateral triangle</b><span>teng tomonlining yarmi</span></li>
  <li><b>simplest radical form</b><span>eng sodda ildiz koʻrinishi</span></li>
  <li><b>reference sheet</b><span>formula varagʻi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Nisbatni <b>burchak tartibida</b>: 30 → x, 60 → x√3, 90 → 2x.</li>
    <li>Avval <b>x ni toping</b>, keyin qolgan ikkitasini yozing.</li>
    <li>Teng tomonli uchburchakning balandligi <b>ikkita 30-60-90</b>
        hosil qiladi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-73 — triangle inequality and similarity
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-73: Triangle Inequality and Similarity (AA, SAS)",
        "category": "math",
        "order": 73,
        "summary": (
            "Uchburchak mavjud boʻlishi uchun ikki tomon uchinchisidan uzun "
            "boʻlishi kerak. Oʻxshashlik esa shakl bir xil, oʻlcham boshqa."
        ),
        "stories": ["Measuring a Pyramid With a Stick"],
        "content": """
<h2>SAT-73: Triangle Inequality and Similarity (AA, SAS)</h2>

<p>Bu darsda ikki mavzu birga keladi, chunki SAT ikkalasini ham
<mark>«mumkinmi?»</mark> degan shaklda soʻraydi: bunday uchburchak mavjud
boʻla oladimi, va bu ikki uchburchak oʻxshashmi.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Formula varagʻi</span>
  <p><b>VARAQDA YOʻQ:</b> uchburchak tengsizligi ham, oʻxshashlik belgilari
  ham. Ikkalasini bilish kerak — lekin ikkalasi ham qisqa.</p>
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>uchta uzunlik uchburchak hosil qiladimi — bir qadamda aytasiz;</li>
    <li>uchinchi tomon qanday oraliqda boʻlishini topasiz;</li>
    <li>ikki uchburchak oʻxshashligini AA bilan tekshirasiz;</li>
    <li>oʻxshash uchburchaklarda nomaʼlum tomonni proporsiya bilan
        topasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Triangle inequality</span>
  <span class="pe-chip pe-chip--v">ikki qisqa tomon yigʻindisi</span>
  <span class="pe-op">&gt;</span>
  <span class="pe-chip pe-chip--s">eng uzun tomon</span>
</div>

<h3>Uchburchak mavjudmi</h3>

<p>Tekshirish oson: ikki qisqa tomonni qoʻshing va eng uzuni bilan
solishtiring. Yigʻindi kattaroq boʻlsa — uchburchak bor.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Tomonlar</th><th>Tekshiruv</th><th>Xulosa</th></tr>
  <tr><td>3, 4, 5</td><td>3 + 4 = 7 &gt; 5</td><td class="pm-word__sym">mavjud</td></tr>
  <tr><td>2, 3, 9</td><td>2 + 3 = 5 &lt; 9</td><td class="pm-word__sym">mavjud emas</td></tr>
  <tr><td>4, 6, 10</td><td>4 + 6 = 10, katta emas</td><td class="pm-word__sym">mavjud emas</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Uchinchi qator muhim: yigʻindi eng uzun tomonga <b>teng</b> boʻlsa ham
  uchburchak hosil boʻlmaydi — uchta nuqta bir toʻgʻri chiziqda yotadi.
  Shart qatʼiy tengsizlik: <b>katta</b>, katta yoki teng emas.
</div>

<h3>Uchinchi tomonning oraliqi</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Ikki tomon 5 va 7</span>
    <span class="pm-solve__why">Uchinchisi qanday boʻlishi mumkin?</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Eng kattasi 5 + 7 = 12 dan kichik</span>
    <span class="pm-solve__why">Aks holda uchburchak yopilmaydi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2 dan katta va 12 dan kichik</span>
    <span class="pm-solve__why">Quyi chegara — ayirma: 7 − 5</span>
  </div>
</div>

<h3>Oʻxshashlik</h3>

<p>Ikki uchburchak <b>oʻxshash</b> boʻlsa, ularning burchaklari bir xil va
tomonlari bir xil nisbatda. Shakl bir xil, oʻlcham boshqa — fotosuratning
kattalashtirilgani kabi.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Belgi</th><th>Nima yetarli</th></tr>
  <tr><td>AA</td><td class="pm-word__sym">ikki burchak teng</td></tr>
  <tr><td>SAS</td><td class="pm-word__sym">ikki tomon nisbati teng va oradagi burchak teng</td></tr>
  <tr><td>SSS</td><td class="pm-word__sym">uchala tomon nisbati teng</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  SAT'da deyarli har doim <b>AA</b> ishlatiladi, va koʻpincha uchinchi
  burchak ham teng ekanini aytish shart emas: ikkitasi teng boʻlsa, uchinchisi
  180 qoidasidan avtomatik teng chiqadi (SAT-68).
</div>

<h3>Nomaʼlum tomonni topish</h3>

<p>Oʻxshash uchburchaklarda mos tomonlar bir xil nisbatda. Kichik uchburchak
tomonlari 3 va 4, kattasining mos tomoni 9 boʻlsa, nisbat 3 — demak
ikkinchi tomon 12.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Proporsiya yozganda <b>mos tomonlarni</b> juftlashtiring: eng qisqasini eng
  qisqasi bilan, eng uzunini eng uzuni bilan. Chizmada burchaklarga qarang —
  teng burchaklarga qarshi turgan tomonlar mos keladi.
</div>

<h3>Oʻxshashlikni koʻrsatuvchi eng koʻp uchraydigan chizma</h3>

<p>Katta uchburchak ichida, bir tomonga parallel chiziq oʻtkazilsa, kichik
uchburchak hosil boʻladi. Ular <b>har doim</b> oʻxshash.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Parallel chiziq mos burchaklarni teng qiladi</span>
    <span class="pm-solve__why">SAT-67</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Uchidagi burchak umumiy</span>
    <span class="pm-solve__why">Ikkala uchburchakda ham bir xil</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Ikki burchak teng → AA boʻyicha oʻxshash</span>
    <span class="pm-solve__why">Uchinchisi 180 qoidasidan avtomatik teng</span>
  </div>
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>could be the length of the third side</b><span>uchinchi tomon boʻla oladimi</span></li>
  <li><b>similar triangles</b><span>oʻxshash uchburchaklar</span></li>
  <li><b>corresponding sides</b><span>mos tomonlar</span></li>
  <li><b>the scale factor</b><span>masshtab koeffitsienti</span></li>
  <li><b>which must be true</b><span>qaysi biri albatta toʻgʻri</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>Two sides of a triangle measure 5 and 7. Which of the following could
    <u>not</u> be the length of the third side?</p>
  </div>
  <ol class="ps-ch">
    <li>12</li>
    <li>3</li>
    <li>9</li>
    <li>11</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 12</p>
      <p>Uchinchi tomon 2 dan katta va 12 dan kichik boʻlishi kerak.</p>
      <p>Aynan 12 boʻlsa, 5 + 7 = 12 — uchta nuqta bir chiziqda yotadi va
      uchburchak yopilmaydi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">11</span>
  <span class="ps-trap__why">11 <b>mumkin</b> — u 12 dan kichik. Chegaraga
  yaqin qiymat mumkin boʻlmagan qiymat degani emas.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">65 s</span></p>
  <div class="ps-stem__q">
    <p>Triangles ABC and DEF are similar, with AB corresponding to DE. If
    AB = 6, DE = 15 and BC = 8, what is EF?</p>
  </div>
  <ol class="ps-ch">
    <li>20</li>
    <li>17</li>
    <li>3.2</li>
    <li>10</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 20</p>
      <p>Nisbat 15 ÷ 6 = 2.5, va 8 × 2.5 = 20.</p>
      <p>Tekshiruv: 6 ÷ 15 = 8 ÷ 20 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">17</span>
  <span class="ps-trap__why">Farq qoʻshilgan: 15 − 6 = 9, va 8 + 9 = 17.
  Oʻxshashlikda tomonlar <b>koʻpaytiriladi</b>, qoʻshilmaydi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Ikki savol turi, ikki qisqa yoʻl:</p>
  <ol>
    <li>«Uchinchi tomon» — <b>ayirmadan yigʻindigacha</b>, chegaralar
        kirmaydi;</li>
    <li>«Oʻxshash» — <b>nisbatni toping</b>, keyin koʻpaytiring;</li>
    <li>Javobni tekshiring: katta uchburchakda hamma tomon kattaroq.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">Tomonlar 4, 6, 10 → uchburchak mavjud</p>
  <p class="pe-good">Mavjud emas — 4 + 6 = 10, katta emas</p>
  <p class="pe-fix__why">Shart qatʼiy: yigʻindi <b>katta</b> boʻlishi
  kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Oʻxshash uchburchaklarda 6 → 15 boʻlsa, 8 → 17</p>
  <p class="pe-good">8 × 2.5 = 20</p>
  <p class="pe-fix__why">Nisbat koʻpaytiriladi, farq qoʻshilmaydi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻxshash va <b>teng</b> (congruent) uchburchakni chalkashtirmang: teng —
  bu nisbat aynan 1 boʻlgan oʻxshashlik. Har bir teng uchburchak
  oʻxshash, lekin aksi notoʻgʻri (SAT-74).
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  SAT'da oʻxshashlik koʻpincha <b>ichma-ich uchburchaklar</b> koʻrinishida
  keladi: katta uchburchak ichida, tomonga parallel chiziq kichik
  uchburchak hosil qiladi. Parallellik mos burchaklarni teng qiladi
  (SAT-67), demak ular AA boʻyicha oʻxshash.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Can a triangle have sides 3, 5 and 9?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — 3 + 5 = 8, bu 9 dan kichik.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Two sides are 8 and 11. Between what values must the third side lie?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">3 dan katta va 19 dan kichik.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Two triangles have angles 40° and 75°. Are they similar?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ha — AA belgisi; uchinchi burchak ham 65° dan
  boʻladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Similar triangles have corresponding sides 4 and 10. If another side of the
  small one is 6, what is its match?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">15 — nisbat 2.5.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Are all equilateral triangles similar to each other?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ha — hammasining burchagi 60° dan.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>triangle inequality</b><span>uchburchak tengsizligi</span></li>
  <li><b>similar</b><span>oʻxshash</span></li>
  <li><b>congruent</b><span>teng</span></li>
  <li><b>corresponding sides</b><span>mos tomonlar</span></li>
  <li><b>scale factor</b><span>masshtab koeffitsienti</span></li>
  <li><b>proportional</b><span>proporsional</span></li>
  <li><b>could be the length</b><span>uzunlik boʻla oladimi</span></li>
  <li><b>strictly greater</b><span>qatʼiy katta</span></li>
  <li><b>degenerate</b><span>aynigan (bir chiziqqa tushgan)</span></li>
  <li><b>nested triangles</b><span>ichma-ich uchburchaklar</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Uchburchak mavjud boʻlishi uchun ikki qisqa tomon yigʻindisi
        <b>qatʼiy katta</b> boʻlsin.</li>
    <li>Uchinchi tomon <b>ayirmadan yigʻindigacha</b> oraliqda.</li>
    <li>Oʻxshashlikda tomonlar <b>koʻpaytiriladi</b>, qoʻshilmaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-74 — congruence and scaling
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-74: Congruent Triangles and Area/Perimeter Scaling",
        "category": "math",
        "order": 74,
        "summary": (
            "Oʻlchamni k barobar oshirsangiz, perimetr k barobar, yuza esa "
            "k kvadrat barobar oshadi. Bu farq SAT'ning sevimli tuzogʻi."
        ),
        "stories": ["Why the Elephant Has Thick Legs"],
        "content": """
<h2>SAT-74: Congruent Triangles and Area/Perimeter Scaling</h2>

<p>SAT-73 da oʻxshashlikni koʻrdik. Endi undan chiqadigan eng foydali natija:
<mark>shaklni ikki barobar kattalashtirsangiz, yuzasi toʻrt barobar
oshadi</mark>. Bu bir qarashda gʻalati tuyuladi, va SAT shundan tuzoq
yasaydi.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Formula varagʻi</span>
  <p><b>VARAQDA YOʻQ:</b> tenglik belgilari ham, masshtab qoidalari ham.
  Varaqda faqat oddiy yuza formulalari bor — masshtab bilan nima
  boʻlishini bilish kerak.</p>
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>tenglik va oʻxshashlikni ajratasiz;</li>
    <li>perimetr va yuza masshtabda qanday oʻzgarishini aytasiz;</li>
    <li>yuzalar nisbatidan uzunliklar nisbatini chiqarasiz;</li>
    <li>hajm uchun ham qoidani qoʻllaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Scale by k</span>
  <span class="pe-chip pe-chip--v">uzunlik × k</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">yuza × k<sup>2</sup></span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">hajm × k<sup>3</sup></span>
</div>

<h3>Nima uchun kvadrat</h3>

<p>Yuza ikkita uzunlikni koʻpaytirish orqali chiqadi. Ikkalasi ham k barobar
oshsa, koʻpaytma k × k barobar oshadi. Hajmda uchta uzunlik bor, shuning
uchun u k<sup>3</sup> barobar oshadi.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Masshtab</th><th>Perimetr</th><th>Yuza</th><th>Hajm</th></tr>
  <tr><td>2 barobar</td><td class="pm-word__sym">×2</td><td class="pm-word__sym">×4</td><td>×8</td></tr>
  <tr><td>3 barobar</td><td class="pm-word__sym">×3</td><td class="pm-word__sym">×9</td><td>×27</td></tr>
  <tr><td>yarmiga</td><td class="pm-word__sym">×0.5</td><td class="pm-word__sym">×0.25</td><td>×0.125</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Buni ogʻzaki tekshirish oson: tomoni 2 boʻlgan kvadratning yuzasi 4;
  tomoni 4 boʻlganiniki 16. Tomon ikki barobar oshdi, yuza esa toʻrt
  barobar. Har safar shubhalansangiz shu misolni chizing.
</div>

<h3>Teskari yoʻnalish</h3>

<p>Yuzalar nisbati berilib, uzunliklar nisbati soʻralishi mumkin. U holda
<b>ildiz olinadi</b>: yuzalar nisbati 25 boʻlsa, uzunliklar nisbati 5.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Ikki oʻxshash shakl, yuzalari 9 va 144</span>
    <span class="pm-solve__why">Yuzalar nisbati 16</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Uzunliklar nisbati 4</span>
    <span class="pm-solve__why">√16 = 4; perimetrlar ham 4 barobar farq qiladi</span>
  </div>
</div>

<h3>Tenglik</h3>

<p>Ikki uchburchak <b>teng</b> (congruent) boʻlsa, ular bir xil shakl va bir
xil oʻlchamda — masshtab koeffitsienti 1. Ular burilgan yoki aks ettirilgan
boʻlishi mumkin, lekin hamma tomon va burchak mos keladi.</p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  <b>SSA tenglik belgisi emas.</b> Ikki tomon va ular orasida <u>boʻlmagan</u>
  burchak berilsa, ikki xil uchburchak hosil boʻlishi mumkin. Ishlaydigan
  belgilar: SSS, SAS, ASA va AAS.
</div>

<h3>Xarita va model masshtabi</h3>

<p>Qoida kundalik hayotda ham ishlaydi. Xaritada masofa 1 dan 50,000 gacha
kichraytirilgan boʻlsa, <b>yuza</b> 1 dan 2,500,000,000 gacha kichraygan.
Shuning uchun kichkina xaritada juda katta maydon sigʻadi.</p>

<p>Model uchun ham shunday: haqiqiy samolyotning 1 dan 100 gacha modeli
uzunligi yuz barobar kichik, sirti oʻn ming barobar kichik va hajmi bir
million barobar kichik. SAT bu savolni «how many times» shaklida beradi va
javob deyarli har doim kvadrat yoki kub boʻladi.</p>

<h3>Nima oʻzgarmaydi</h3>

<p>Masshtab hamma narsani oʻzgartirmaydi. <b>Burchaklar oʻsha-oʻsha
qoladi</b> — shakl bir xil boʻlgani uchun. Shuningdek, ikki tomonning
oʻzaro nisbati ham saqlanadi: 3 ga 4 nisbat kattalashtirilganda ham 3 ga 4
boʻlib qoladi.</p>

<p>Shuning uchun oʻxshash shakllarda sinus, kosinus va tangens ham
oʻzgarmaydi (SAT-75) — ular nisbat, va nisbat masshtabga bogʻliq
emas.</p>

<p>Bir ogohlantirish: qoida <b>oʻxshash</b> shakllarga tegishli. Bir
toʻrtburchakning faqat eni ikki barobar oshirilsa, u oldingisiga oʻxshash
emas — shakl oʻzgargan. Bunday holda yuza atigi ikki barobar oshadi, toʻrt
emas. Masshtab degani <b>hamma</b> oʻlchamni bir xil koeffitsientga
koʻpaytirish.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>congruent</b><span>teng (bir xil shakl va oʻlcham)</span></li>
  <li><b>the scale factor</b><span>masshtab koeffitsienti</span></li>
  <li><b>the ratio of their areas</b><span>yuzalari nisbati</span></li>
  <li><b>is enlarged by a factor of 3</b><span>3 barobar kattalashtirilgan</span></li>
  <li><b>how many times greater</b><span>necha barobar katta</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>A rectangle is enlarged by a scale factor of 3. How many times greater is
    its area?</p>
  </div>
  <ol class="ps-ch">
    <li>9</li>
    <li>3</li>
    <li>6</li>
    <li>27</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 9</p>
      <p>Yuza k<sup>2</sup> barobar oshadi: 3<sup>2</sup>.</p>
      <p>Tekshiruv: 2 ga 5 toʻrtburchak yuzasi 10; 6 ga 15 niki 90 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">3</span>
  <span class="ps-trap__why">Uzunlik koeffitsienti javob deb olingan. Yuza
  ikki oʻlchovli — u <b>kvadrat</b> boʻyicha oshadi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">65 s</span></p>
  <div class="ps-stem__q">
    <p>Two similar triangles have areas of 16 and 144. What is the ratio of
    their perimeters?</p>
  </div>
  <ol class="ps-ch">
    <li>1 to 3</li>
    <li>1 to 9</li>
    <li>1 to 12</li>
    <li>1 to 128</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 1 to 3</p>
      <p>Yuzalar nisbati 9, demak uzunliklar nisbati √9 = 3.</p>
      <p>Perimetr uzunlik — u ham 3 barobar farq qiladi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">1 to 9</span>
  <span class="ps-trap__why">Yuzalar nisbati shundoq koʻchirilgan. Perimetr
  uzunlik boʻlgani uchun <b>ildiz</b> olinadi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Har safar bitta savol: <b>soʻralayotgani necha oʻlchovli?</b></p>
  <ol>
    <li>Uzunlik, perimetr, balandlik — bir oʻlchovli, <b>k</b>;</li>
    <li>Yuza, sirt — ikki oʻlchovli, <b>k<sup>2</sup></b>;</li>
    <li>Hajm — uch oʻlchovli, <b>k<sup>3</sup></b>.</li>
  </ol>
  <p>Teskari savolda esa mos ildizni oling: yuzadan uzunlikka kvadrat
  ildiz, hajmdan uzunlikka kub ildiz.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Masshtab 3 → yuza 3 barobar</p>
  <p class="pe-good">9 barobar</p>
  <p class="pe-fix__why">Yuza ikkita uzunlikdan tuzilgan.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Yuzalar nisbati 9 → perimetrlar nisbati 9</p>
  <p class="pe-good">3</p>
  <p class="pe-fix__why">Perimetr uzunlik — ildiz olinadi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu qoida uchburchakka emas, <b>har qanday shaklga</b> tegishli — doira,
  koʻpburchak, hatto notoʻgʻri shaklga ham. Muhimi shakl bir xil qolib,
  faqat oʻlcham oʻzgarishi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Kundalik natija: idishning oʻlchamini ikki barobar oshirsangiz, unga
  <b>sakkiz</b> barobar koʻp suyuqlik sigʻadi, lekin uni yasashga faqat
  <b>toʻrt</b> barobar koʻp material ketadi. Katta idishlar shuning uchun
  arzonroq tushadi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  A shape is enlarged by a factor of 4. How many times greater is its area?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">16 barobar.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Two similar shapes have areas 4 and 100. What is the ratio of their
  lengths?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">1 dan 5 gacha — √25.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A cube's side is doubled. How many times greater is its volume?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">8 barobar.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Two similar triangles have perimeters 12 and 30. What is the ratio of their
  areas?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">4 dan 25 gacha — uzunliklar nisbati 2.5, va uning
  kvadrati 6.25.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Is SSA a valid test for congruence?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — ikki xil uchburchak hosil boʻlishi
  mumkin.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>congruent</b><span>teng</span></li>
  <li><b>scale factor</b><span>masshtab koeffitsienti</span></li>
  <li><b>enlarged by a factor of</b><span>… barobar kattalashtirilgan</span></li>
  <li><b>the ratio of the areas</b><span>yuzalar nisbati</span></li>
  <li><b>surface area</b><span>sirt yuzasi</span></li>
  <li><b>volume</b><span>hajm</span></li>
  <li><b>how many times greater</b><span>necha barobar katta</span></li>
  <li><b>corresponding parts</b><span>mos qismlar</span></li>
  <li><b>reflected / rotated</b><span>aks ettirilgan / burilgan</span></li>
  <li><b>square root</b><span>kvadrat ildiz</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Uzunlik <b>k</b>, yuza <b>k<sup>2</sup></b>, hajm
        <b>k<sup>3</sup></b>.</li>
    <li>Teskari yoʻnalishda <b>ildiz</b> oling.</li>
    <li><b>SSA</b> tenglik belgisi emas.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-75 — right triangle trigonometry
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-75: Right Triangle Trigonometry — Sine, Cosine, Tangent",
        "category": "math",
        "order": 75,
        "summary": (
            "SOH-CAH-TOA formula varagʻida YOʻQ va yodda boʻlishi shart. "
            "Uchta nisbat, uchta harf — boshqa hech narsa kerak emas."
        ),
        "stories": ["The Angle to the Star"],
        "content": """
<h2>SAT-75: Right Triangle Trigonometry — Sine, Cosine, Tangent</h2>

<p>Trigonometriya nomi qoʻrqinchli, mazmuni esa oddiy: <mark>toʻgʻri
burchakli uchburchakda ikki tomonning nisbati</mark>. Uchta nisbat bor va
ularning nomlari bor, xolos.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Formula varagʻi</span>
  <p><b>VARAQDA YOʻQ:</b> sinus, kosinus va tangens taʼriflari. Ular u yerda
  umuman yozilmagan.</p>
  <p>Demak <b>SOH-CAH-TOA yodda boʻlishi shart</b> — bu Blok D dagi yagona
  majburiy yodlash. Qolgan hamma narsa varaqda yoki chiqarib olinadi.</p>
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>qarshi, yondosh va gipotenuzani ajratasiz;</li>
    <li>uchta nisbatni yozasiz;</li>
    <li>berilgan burchak va tomondan nomaʼlum tomonni topasiz;</li>
    <li>nisbatlarning oʻlchov birligi yoʻqligini bilasiz.</li>
  </ul>
</div>

<figure class="pm-fig">
  <svg viewBox="0 0 320 180" role="img"
       aria-label="A 3-4-5 right triangle with the angle theta at the bottom
                   right, the side of 3 opposite it, the side of 4 adjacent,
                   and the hypotenuse of 5">
    <line class="pm-ln" x1="90" y1="150" x2="210" y2="150"/>
    <line class="pm-ln" x1="90" y1="150" x2="90" y2="60"/>
    <line class="pm-ln" x1="90" y1="60" x2="210" y2="150"/>
    <line class="pm-ln" x1="90" y1="138" x2="102" y2="138"/>
    <line class="pm-ln" x1="102" y1="138" x2="102" y2="150"/>
    <text class="pm-lbl" x="184" y="142">θ</text>
    <text class="pm-lbl" x="70"  y="108">3</text>
    <text class="pm-lbl" x="146" y="166">4</text>
    <text class="pm-lbl" x="156" y="98">5</text>
  </svg>
  <figcaption>θ burchagiga qarshi turgan tomon 3, yondosh tomon 4,
  gipotenuza 5. Demak sinus 3/5, kosinus 4/5, tangens 3/4.</figcaption>
</figure>

<div class="pe-formula">
  <span class="pe-formula__label">SOH-CAH-TOA</span>
  <span class="pe-chip pe-chip--v">sin = qarshi ÷ gipotenuza</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">cos = yondosh ÷ gipotenuza</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">tan = qarshi ÷ yondosh</span>
</div>

<h3>Uch tomonni nomlash</h3>

<p>Ikki tomonning nomi <b>qaysi burchakka qaraganingizga bogʻliq</b>.
Gipotenuza har doim bir xil — toʻgʻri burchakka qarshi turgan eng uzun
tomon. Qolgan ikkitasi esa oʻrin almashadi: bitta burchakka qarshi turgan
tomon boshqasiga yondosh boʻladi.</p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Nisbatni yozishdan oldin <b>qaysi burchak haqida gapirilayotganini</b>
  aniqlang. Yuqoridagi uchburchakda θ uchun sinus 3/5; ikkinchi oʻtkir
  burchak uchun esa sinus 4/5. Tomon oʻsha-oʻsha, javob boshqa.
</div>

<h3>Nomaʼlum tomonni topish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Burchak 30°, gipotenuza 10, qarshi tomon nomaʼlum</span>
    <span class="pm-solve__why">Qarshi va gipotenuza — sinus kerak</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">sin 30° = qarshi ÷ 10</span>
    <span class="pm-solve__why">Taʼrifni shundoq yozdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Qarshi tomon = 10 × sin 30° = 5</span>
    <span class="pm-solve__why">Bu 30-60-90 nisbatiga mos (SAT-72) ✓</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Qaysi nisbatni tanlashni <b>berilgan va soʻralgan tomonlarga qarab</b>
  hal qiling: gipotenuza aralashsa sinus yoki kosinus, aralashmasa tangens.
  Uchala nisbatni yozib chiqib, keraklisini tanlash ham ishlaydi.
</div>

<h3>Nisbatda birlik yoʻq</h3>

<p>Sinus, kosinus va tangens — <b>ikki uzunlikning nisbati</b>, demak
santimetr yoki metr ularda qisqarib ketadi. Shuning uchun javob hech qachon
«0.6 metr» boʻlmaydi — u shunchaki 0.6.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Teskari savol ham boʻladi: nisbat berilib, <b>burchak</b> soʻraladi.
  Bunda kalkulyatordagi teskari funksiyalar ishlatiladi. SAT buni kamdan-kam
  beradi va deyarli har doim maxsus uchburchak qiymatlari bilan — masalan
  tangens 1 boʻlsa, burchak 45°.
</div>

<h3>Koʻtarilish va pasayish burchagi</h3>

<p>Matnli masalalarda burchak koʻpincha shu ikki nom bilan keladi.
<b>Angle of elevation</b> — pastdan yuqoriga qarash burchagi;
<b>angle of depression</b> — yuqoridan pastga. Ikkalasi ham gorizontal
chiziqdan oʻlchanadi, va ular bir-biriga teng (SAT-67: almashinuvchi
burchaklar).</p>

<h3>Ikki oʻtkir burchak orasidagi bogʻlanish</h3>

<p>Toʻgʻri burchakli uchburchakda ikki oʻtkir burchak 90 ga toʻldiradi
(SAT-66). Bundan chiroyli natija chiqadi: <b>biridagi sinus ikkinchisidagi
kosinusga teng</b>.</p>

<p>Yuqoridagi 3-4-5 uchburchakda buni koʻrish oson: θ uchun sinus 3/5, va
ikkinchi burchak uchun kosinus ham 3/5 — ikkalasi ham oʻsha 3 va 5 ni
ishlatadi, faqat boshqa nomlar bilan. Bu SAT-76 ning mavzusi, va u shu
yerdan chiqadi.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>the side opposite the angle</b><span>burchakka qarshi turgan tomon</span></li>
  <li><b>the side adjacent to the angle</b><span>burchakka yondosh tomon</span></li>
  <li><b>what is sin of angle A</b><span>A burchagining sinusi</span></li>
  <li><b>the angle of elevation</b><span>koʻtarilish burchagi</span></li>
  <li><b>to the nearest tenth</b><span>oʻndan bir aniqlikda</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>In a right triangle, the side opposite angle <i>A</i> is 3, the side
    adjacent is 4, and the hypotenuse is 5. What is cos <i>A</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>4/5</li>
    <li>3/5</li>
    <li>3/4</li>
    <li>5/4</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 4/5</p>
      <p>Kosinus — yondosh boʻlingan gipotenuzaga.</p>
      <p><b>3/5</b> — bu sinus; <b>3/4</b> — tangens.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">3/5</span>
  <span class="ps-trap__why">Sinus va kosinus almashtirilgan. SOH-CAH-TOA
  ni tartib bilan yozing: <b>C</b>osine — <b>A</b>djacent —
  <b>H</b>ypotenuse.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">70 s</span></p>
  <div class="ps-stem__q">
    <p>A ramp rises at an angle of 30° and its length along the slope is 10
    metres. How high is the top of the ramp?</p>
  </div>
  <ol class="ps-ch">
    <li>5 metres</li>
    <li>10 metres</li>
    <li>5√3 metres</li>
    <li>20 metres</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 5 metres</p>
      <p>Balandlik 30° ga qarshi turadi, va 10 gipotenuza:
      10 × sin 30° = 5.</p>
      <p>Yoki 30-60-90 nisbati bilan (SAT-72): gipotenuza 2x, demak
      x = 5.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">5√3 metres</span>
  <span class="ps-trap__why">Uzun katet hisoblangan — u 60° ga qarshi
  turadi. Balandlik esa 30° ga qarshi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Har bir trigonometriya savolida uch qadam:</p>
  <ol>
    <li>Chizmada burchakni belgilang;</li>
    <li>Uch tomonni <b>oʻsha burchakka nisbatan</b> nomlang;</li>
    <li>Berilgan va soʻralgan ikkisini qamragan nisbatni tanlang.</li>
  </ol>
  <p>Va eslang: bu uchta taʼrif varaqda yoʻq — ularni yozib kelish
  kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">cos A = qarshi ÷ gipotenuza</p>
  <p class="pe-good">yondosh ÷ gipotenuza</p>
  <p class="pe-fix__why">CAH: Cosine, Adjacent, Hypotenuse.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">tan A = qarshi ÷ gipotenuza</p>
  <p class="pe-good">qarshi ÷ yondosh</p>
  <p class="pe-fix__why">Tangensda gipotenuza umuman ishtirok etmaydi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Maxsus uchburchaklar (SAT-71, 72) trigonometriyaning tayyor
  qiymatlarini beradi: sin 30° = 1/2, sin 45° = √2/2, sin 60° = √3/2.
  Ularni yodlash shart emas — uchburchakni chizib nisbatni oʻqing.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Sinus va kosinus har doim <b>1 dan kichik</b> (yoki teng), chunki qarshi
  va yondosh tomon gipotenuzadan uzun boʻla olmaydi. Javobingiz sinus uchun
  1 dan katta chiqsa, nisbatni teskari yozgansiz.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  In a 3-4-5 right triangle, what is sin of the angle opposite the side of 3?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">3/5.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  In that triangle, what is tan of the same angle?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">3/4 — gipotenuza ishtirok etmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A 5-12-13 triangle: what is cos of the angle opposite the side of 5?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">12/13 — yondosh boʻlingan gipotenuzaga.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Can sin of an angle be 1.4?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — qarshi tomon gipotenuzadan uzun boʻla
  olmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A ladder 8 metres long leans at 60° to the ground. How high does it
  reach?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">4√3 metr — 8 × sin 60°.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>sine / cosine / tangent</b><span>sinus / kosinus / tangens</span></li>
  <li><b>opposite</b><span>qarshi turgan</span></li>
  <li><b>adjacent</b><span>yondosh</span></li>
  <li><b>hypotenuse</b><span>gipotenuza</span></li>
  <li><b>ratio</b><span>nisbat</span></li>
  <li><b>angle of elevation</b><span>koʻtarilish burchagi</span></li>
  <li><b>angle of depression</b><span>pasayish burchagi</span></li>
  <li><b>ramp / slope</b><span>qiyalik</span></li>
  <li><b>to the nearest tenth</b><span>oʻndan bir aniqlikda</span></li>
  <li><b>unitless</b><span>oʻlchov birligisiz</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>SOH-CAH-TOA varaqda yoʻq</b> — yodda boʻlishi shart.</li>
    <li>Tomon nomi <b>qaysi burchakka qaraganingizga</b> bogʻliq.</li>
    <li>Sinus va kosinus <b>1 dan katta boʻlmaydi</b>; nisbatda birlik
        yoʻq.</li>
  </ul>
</div>
""",
    },
]
