# -*- coding: utf-8 -*-
"""Prime Math — darslar 95–97 (mantiqiy jadval; juftlik; Dirixle).

**Blok H ni OCHADI: Mantiq va fikrlash usullari (95–100).**
Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md

  mashqlar — practice/management/commands/_practice_pm_95_97.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_95_97.py

⚠️ BLOK H BOSHQACHA. Bu yerda birorta ham hisoblash formulasi yoʻq.
   Uchala dars ham bitta savolga javob beradi: «buni qanday BILAMIZ?»
   Shuning uchun pm-solve ladderlari son emas, XULOSA zanjirini
   koʻrsatadi — har qatorning oʻng ustuni «bu qaysi shartdan chiqdi»
   degan javobni beradi.

⚠️ Uchtasining ichki mantigʻi — isbotlashning uch turi:
     PM-95  hamma variantni koʻrib chiqib, ortiqchasini oʻchirish
            (jadval usuli — chiqarib tashlash yoʻli bilan isbot);
     PM-96  oʻzgarmas xossa topib, maqsad unga zid ekanini koʻrsatish
            (invariant — IMKONSIZLIKNI isbotlash);
     PM-97  eng yomon holni sanab, undan keyin muqarrarlikni koʻrsatish
            (Dirixle — MAVJUDLIKNI isbotlash, kimligini aytmasdan).

⚠️ Kumulyativ chegaralar:
  • PM-95 — 3×3 va 4×4 mantiqiy jadval. ⛔ «Yolgʻonchi va rostgoʻy»
    turidagi masalalar kursda yoʻq;
  • PM-96 — juft-toq va invariant. Shaxmat doskasi boʻyash usuli
    4×4 da koʻrsatiladi. ⛔ Boshqa invariantlar (yigʻindi mod 3 va h.k.)
    YOʻQ;
  • PM-97 — Dirixle prinsipi va «eng yomon hol» mulohazasi.
    ⛔ Umumlashgan Dirixlening geometrik shakli YOʻQ.
  • Faol ishlatiladi: jadval (PM-86), sanash (PM-82), boʻlinish
    alomatlari va juft-toq (PM-6), yaxlitlash (PM-14), teskari hodisa
    (PM-84), yuza (PM-68).

⚠️ Arifmetika darvozasi: scratchpad/verify_pm_95_97.py mantiqiy
   masalalarni HAMMA JOYLASHTIRISHNI koʻrib chiqib yechadi
   (itertools.permutations) va yechim YAGONA ekanini tekshiradi;
   juftlik masalalarida invariant hamma yoʻldan saqlanishini,
   Dirixlede esa eng yomon holni bevosita quradi.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_95_97.py --author=prime
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
    # PM-95 — mantiqiy masalalar va jadval usuli
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-95: Mantiqiy masalalar va jadval usuli",
        "category": "math",
        "order": 95,
        "summary": (
            "Mantiqiy masalada hisoblanadigan narsa yoʻq — faqat "
            "chiqarib tashlash bor. Jadval har bir variantni koʻz "
            "oldiga qoʻyadi va imkonsizlarini birma-bir oʻchiradi."
        ),
        "stories": ["Kim qaysi kasb egasi?"],
        "content": """
<h2>PM-95: Mantiqiy masalalar va jadval usuli</h2>

<p>Blok H boshlandi. Oldingi toʻqson toʻrt darsda biz <b>hisoblashni</b>
oʻrgandik. Qolgan olti darsda esa boshqa savolga javob beramiz: buni
qanday <b>bilamiz</b>?</p>

<p>Mana bir masala. Bekzod, Dilnoza va Sherbek — shifokor, oʻqituvchi
va muhandis. Bekzod shifokor emas. Dilnoza oʻqituvchi emas. Sherbek na
muhandis, na shifokor. Kim kim?</p>

<p>Bu yerda qoʻshiladigan yoki koʻpaytiriladigan hech narsa yoʻq. Bor
narsa — <b>chiqarib tashlash</b>. Va buning uchun eng yaxshi asbob
jadval.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>mantiqiy jadval tuzasiz va uni belgilar bilan toʻldirasiz;</li>
    <li>bitta ✓ dan keyin butun qator va ustunni oʻchirasiz;</li>
    <li>shartlarni «bu emas» koʻrinishiga oʻgirasiz;</li>
    <li>javobni hamma shart boʻyicha tekshirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Jadval qoidasi</span>
  <span class="pe-chip pe-chip--s">har qatorda bitta ✓</span>
  <span class="pe-op">va</span>
  <span class="pe-chip pe-chip--s">har ustunda bitta ✓</span>
</div>

<h3>1. Jadval nima uchun kerak</h3>

<p>Uchta odam va uchta kasb — jami 6 xil joylashtirish mumkin
(PM-82: 3 × 2 × 1). Ularning beshtasi notoʻgʻri, bittasi toʻgʻri.
Boshda saqlab turish qiyin, qogʻozda esa oson.</p>

<p>Jadval tuzamiz: qatorlar — odamlar, ustunlar — kasblar. Har bir
katakka <b>✗</b> (boʻlishi mumkin emas) yoki <b>✓</b> (roppa-rosa shu)
qoʻyiladi.</p>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Ikki oltin qoida</p>
  <p><b>1.</b> Qatorda bitta katakdan boshqa hammasi ✗ boʻlsa, oʻsha
  katak ✓.
  <br><b>2.</b> Katakka ✓ qoʻysangiz, oʻsha qatorning va oʻsha
  ustunning qolgan hamma kataklariga darrov ✗ qoʻying.</p>
</div>

<h3>2. Birinchi misol — qadam-baqadam</h3>

<p><b>Shartlar:</b> (1) Bekzod shifokor emas. (2) Dilnoza oʻqituvchi
emas. (3) Sherbek muhandis emas. (4) Sherbek shifokor emas.</p>

<p>Avval faqat shartlarni belgilaymiz — hech qanday xulosa
chiqarmasdan:</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th></th><th>shifokor</th><th>oʻqituvchi</th><th>muhandis</th></tr>
  <tr><td>Bekzod</td><td class="pm-word__sym">✗ (1)</td><td></td><td></td></tr>
  <tr><td>Dilnoza</td><td></td><td class="pm-word__sym">✗ (2)</td><td></td></tr>
  <tr><td>Sherbek</td><td class="pm-word__sym">✗ (4)</td><td></td><td class="pm-word__sym">✗ (3)</td></tr>
</table></div>

<p>Endi qarang: Sherbek qatorida ikkita ✗ bor va bitta katak
boʻsh qoldi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Sherbek — oʻqituvchi ✓</span>
    <span class="pm-solve__why">Qatorida boshqa varianti qolmadi (1-qoida)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Bekzod va Dilnoza oʻqituvchi emas</span>
    <span class="pm-solve__why">Ustunni oʻchirdik (2-qoida)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Dilnoza — shifokor ✓</span>
    <span class="pm-solve__why">Uning qatorida faqat shifokor qoldi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Bekzod — muhandis ✓</span>
    <span class="pm-solve__why">Oxirgi boʻsh katak</span>
  </div>
</div>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th></th><th>shifokor</th><th>oʻqituvchi</th><th>muhandis</th></tr>
  <tr><td>Bekzod</td><td class="pm-word__sym">✗</td><td>✗</td><td>✓</td></tr>
  <tr><td>Dilnoza</td><td class="pm-word__sym">✓</td><td>✗</td><td>✗</td></tr>
  <tr><td>Sherbek</td><td class="pm-word__sym">✗</td><td>✓</td><td>✗</td></tr>
</table></div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz — har bir shart boʻyicha</p>
  <p>(1) Bekzod muhandis, shifokor emas ✓
  <br>(2) Dilnoza shifokor, oʻqituvchi emas ✓
  <br>(3) Sherbek oʻqituvchi, muhandis emas ✓
  <br>(4) Sherbek shifokor emas ✓
  <br><b>Javob:</b> Dilnoza — shifokor, Sherbek — oʻqituvchi,
  Bekzod — muhandis.</p>
</div>

<h3>3. Shartni «bu emas» koʻrinishiga oʻgirish</h3>

<p>Masalalarda shart koʻpincha bevosita aytilmaydi. Uni avval
oʻgirish kerak.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Matnda shunday deyiladi</th><th>Jadvalda nima qilinadi</th><th>Nega</th></tr>
  <tr><td>«Oʻqituvchi Dilnozaning qoʻshnisi»</td>
    <td class="pm-word__sym">Dilnoza — oʻqituvchi emas</td>
    <td>Odam oʻzining qoʻshnisi boʻlmaydi</td></tr>
  <tr><td>«Jasur shifokordan yosh»</td>
    <td class="pm-word__sym">Jasur — shifokor emas</td>
    <td>Odam oʻzidan yosh boʻlmaydi</td></tr>
  <tr><td>«Dasturchi bilan Afsona birga keldi»</td>
    <td class="pm-word__sym">Afsona — dasturchi emas</td>
    <td>Ular ikki har xil odam</td></tr>
  <tr><td>«Nodira 7-sinfda emas»</td>
    <td class="pm-word__sym">toʻgʻridan-toʻgʻri ✗</td>
    <td>Shart allaqachon tayyor</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Eng koʻp uchraydigan xato</p>
  <p>«Oʻqituvchi Dilnozaning qoʻshnisi» degan gapni oʻqib, jadvalga
  «Dilnoza — oʻqituvchi ✓» deb qoʻyish. Gap buning <b>aksini</b>
  aytyapti: agar oʻqituvchi Dilnozaning qoʻshnisi boʻlsa, demak
  oʻqituvchi Dilnozaning oʻzi emas.</p>
</div>

<h3>4. Tartib haqidagi shartlar</h3>

<p><b>Masala.</b> Afsona, Jasur va Nodira 5, 7 va 9-sinflarda oʻqiydi.
Jasur Afsonadan katta sinfda. Nodira 7-sinfda emas. Afsona 5-sinfda
emas. Kim qaysi sinfda?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Afsona — 7 yoki 9-sinf</span>
    <span class="pm-solve__why">5-sinf emas (3-shart)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Afsona 9-sinf boʻlolmaydi</span>
    <span class="pm-solve__why">Undan katta sinf kerak (1-shart)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Afsona — 7-sinf ✓, Jasur — 9-sinf ✓</span>
    <span class="pm-solve__why">Jasur Afsonadan katta</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Nodira — 5-sinf ✓</span>
    <span class="pm-solve__why">Qolgan yagona sinf</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Jasur (9) Afsonadan (7) katta ✓ Nodira 5-sinfda, 7 da emas ✓
  Afsona 5-sinfda emas ✓
  <br><b>Javob:</b> Nodira — 5, Afsona — 7, Jasur — 9-sinf.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">«Kattaroq» degan shart ikkita ✗ beradi</p>
  <p>«Jasur Afsonadan katta sinfda» degani: Jasur eng kichik sinfda
  emas <b>va</b> Afsona eng katta sinfda emas. Bitta gapdan ikkita
  belgi chiqadi — bunday shartlar eng foydalisi.</p>
</div>

<h3>Matnli masala</h3>

<p>Toʻrt doʻst — Bekzod, Dilnoza, Sherbek va Afsona — bozordan toʻrt
xil meva olishdi: olma, nok, uzum va anor. Har biri bittadan
oldi.</p>

<p><b>Shartlar:</b> (1) Bekzod na olma, na nok oldi. (2) Dilnoza anor
oldi. (3) Sherbek uzum olmadi. (4) Afsona nok olmadi.</p>

<p><b>Kim qaysi mevani olgan?</b></p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th></th><th>olma</th><th>nok</th><th>uzum</th><th>anor</th></tr>
  <tr><td>Bekzod</td><td class="pm-word__sym">✗ (1)</td><td>✗ (1)</td><td></td><td></td></tr>
  <tr><td>Dilnoza</td><td class="pm-word__sym"></td><td></td><td></td><td>✓ (2)</td></tr>
  <tr><td>Sherbek</td><td class="pm-word__sym"></td><td></td><td>✗ (3)</td><td></td></tr>
  <tr><td>Afsona</td><td class="pm-word__sym"></td><td>✗ (4)</td><td></td><td></td></tr>
</table></div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Anor ustuni yopildi</span>
    <span class="pm-solve__why">Dilnoza anor oldi (2) — qolganlarga ✗</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Bekzod — uzum ✓</span>
    <span class="pm-solve__why">Olma ✗, nok ✗, anor ✗ — bittasi qoldi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Sherbek — nok yoki olma</span>
    <span class="pm-solve__why">Uzum endi Bekzodniki</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Afsona — olma ✓</span>
    <span class="pm-solve__why">Nok ✗ (4), uzum va anor band</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Sherbek — nok ✓</span>
    <span class="pm-solve__why">Oxirgi qolgan meva</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz — toʻrt shart ham</p>
  <p>(1) Bekzod uzum oldi — olma ham, nok ham emas ✓
  <br>(2) Dilnoza anor oldi ✓
  <br>(3) Sherbek nok oldi, uzum emas ✓
  <br>(4) Afsona olma oldi, nok emas ✓
  <br><b>Javob:</b> Bekzod — uzum, Dilnoza — anor, Sherbek — nok,
  Afsona — olma.</p>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Yechim yagona ekanini ham tekshiring</p>
  <p>Yaxshi mantiqiy masalada javob <b>bitta</b> boʻladi. Agar
  jadvalni toʻldirib boʻlgach ikkita boʻsh katak qolsa va ikkalasi
  ham mumkin boʻlsa — demak shartlardan birini ishlatmagansiz.
  Qaytib oʻqing.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Jadvalsiz, boshda saqlab yechishga urinish</p>
  <p class="pe-fix__good">Avval qator va ustunlarni chizish</p>
  <p class="pe-fix__why">Uchta odam uchun 6 ta variant, toʻrttasi
  uchun 24 ta. Ularni boshda saqlab boʻlmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✓ qoʻyildi, lekin qator va ustun
  oʻchirilmadi</p>
  <p class="pe-fix__good">✓ qoʻyilgan zahoti butun qator va ustunga ✗</p>
  <p class="pe-fix__why">Har bir kasb bitta odamda, har bir odamda
  bitta kasb. Oʻchirmasangiz keyingi qadam koʻrinmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">«Oʻqituvchi Dilnozaning qoʻshnisi» → Dilnoza
  oʻqituvchi</p>
  <p class="pe-fix__good">Dilnoza oʻqituvchi <b>emas</b></p>
  <p class="pe-fix__why">Ikki har xil odam haqida gap ketyapti. Bunday
  gaplar har doim ✗ beradi, ✓ emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">«Bekzod muhandis boʻlsa kerak» deb yozib
  qoʻyish</p>
  <p class="pe-fix__good">Faqat shartdan chiqqan xulosani yozish</p>
  <p class="pe-fix__why">Taxmin bilan xulosa aralashib ketsa, jadval
  ishonchsiz boʻlib qoladi. Har bir belgining yonida u qaysi shartdan
  chiqqanini yozib qoʻying.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Uchta odam va uchta kasb bor. Jami nechta
  joylashtirish mumkin?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>6 ta.</b> 3 × 2 × 1 = 6 (PM-82: koʻpaytirish prinsipi).
    Shartlar shu oltitadan beshtasini oʻchirib tashlaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «Shifokor Bekzoddan yosh» degan shart
  jadvalga qanday tushadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Bekzod — shifokor emas ✗.</b> Odam oʻzidan yosh boʻla
    olmaydi, demak shifokor boshqa odam.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Jadvalda bir ustunda ikkita ✓ paydo boʻldi.
  Bu nimani bildiradi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Xato qilingan.</b> Har bir kasb (yoki meva, sinf) faqat
    bitta odamga tegishli. Qaytib tekshirish kerak.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Karim, Nodira va Bekzod — 5, 6 va 7-sinfda.
  Karim 5-sinfda. Nodira Bekzoddan katta sinfda. Kim qayerda?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Karim 5, Bekzod 6, Nodira 7.</b> Karim 5-sinfda ekan,
    Nodira bilan Bekzodga 6 va 7 qoladi. Nodira Bekzoddan katta
    boʻlgani uchun Nodira — 7, Bekzod — 6 ✓ Ikkita shart uchala
    oʻrinni ham aniqladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Uchta qiz — Afsona, Dilnoza, Nodira — qizil,
  koʻk va yashil koʻylak kiygan. Dilnoza na koʻk, na yashil kiygan.
  Nodira yashil kiymagan. Kim nima kiygan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Dilnoza qizil, Nodira koʻk, Afsona yashil.</b> Dilnozaga
    faqat qizil qoldi ✓ Qizil ustuni yopilgach, Nodira koʻk yoki
    yashil; yashil emas, demak koʻk ✓ Afsonaga yashil qoladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Uchta bola — Jasur, Bekzod, Sherbek —
  futbol, shaxmat va suzish bilan shugʻullanadi. Jasur shaxmat
  oʻynamaydi. Shaxmatchi Bekzodning doʻsti. Bekzod suzmaydi. Kim
  nima bilan shugʻullanadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Sherbek — shaxmat, Bekzod — futbol, Jasur — suzish.</b>
    «Shaxmatchi Bekzodning doʻsti» → Bekzod shaxmatchi emas. Jasur
    ham emas, demak Sherbek — shaxmatchi ✓ Shaxmat ustuni yopildi.
    Bekzod suzmaydi, demak Bekzod — futbol ✓ Jasurga suzish
    qoladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">7. Toʻrt bola — Afsona, Bekzod, Sherbek va
  Dilnoza — toʻrt xil hayvon boqadi: mushuk, it, tovuq, quyon. Bekzod
  mushuk boqadi. Sherbek na tovuq, na quyon boqadi. Dilnoza quyon
  boqmaydi. Kim nimani boqadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Bekzod — mushuk, Sherbek — it, Dilnoza — tovuq,
    Afsona — quyon.</b> Bekzod mushuk ✓ — ustun yopildi. Sherbek
    tovuq ham, quyon ham emas, mushuk band — demak it ✓ Dilnoza
    quyon emas, it va mushuk band — demak tovuq ✓ Afsonaga quyon
    qoladi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Mantiqiy masala</b><span>hisob emas, mulohaza bilan
    yechiladigan masala; ingl. logic puzzle</span></li>
  <li><b>Shart</b><span>masalada berilgan har bir maʼlumot; ingl.
    clue</span></li>
  <li><b>Xulosa</b><span>shartlardan kelib chiqadigan yangi bilim;
    ingl. deduction</span></li>
  <li><b>Taxmin</b><span>hali isbotlanmagan fikr; ingl.
    assumption</span></li>
  <li><b>Chiqarib tashlash</b><span>imkonsiz variantlarni oʻchirish;
    ingl. elimination</span></li>
  <li><b>Mantiqiy jadval</b><span>qatorlar va ustunlar kesishmasidagi
    belgilar jadvali; ingl. logic grid</span></li>
  <li><b>Yagona yechim</b><span>shartlarni qanoatlantiruvchi bitta
    javob; ingl. unique solution</span></li>
  <li><b>Ziddiyat</b><span>bir-biriga qarama-qarshi ikki xulosa; ingl.
    contradiction</span></li>
  <li><b>Joylashtirish</b><span>hamma variantlardan biri; ingl.
    arrangement</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Mantiqiy masalada hisoblash yoʻq — chiqarib tashlash bor.</li>
    <li>Qatorlar va ustunlardan jadval tuzing.</li>
    <li>Qatorda bitta boʻsh katak qolsa — u ✓.</li>
    <li>✓ qoʻyilsa, qator va ustunning qolgani darrov ✗.</li>
    <li>«X bilan Y birga keldi» kabi gaplar ✗ beradi, ✓ emas.</li>
    <li>Har bir belgining yonida u qaysi shartdan chiqqanini
      yozing.</li>
    <li>Oxirida javobni <b>hamma</b> shart boʻyicha tekshiring.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-96 — juftlik (juft-toq) gʻoyasi
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-96: Juftlik (juft-toq) gʻoyasi",
        "category": "math",
        "order": 96,
        "summary": (
            "Baʼzi masalalarda javob «mumkin emas» boʻladi — va buni "
            "isbotlash mumkin. Buning uchun oʻzgarmaydigan xossa "
            "topiladi: koʻpincha bu juft-toqlik."
        ),
        "stories": ["Oʻn beshta stakan"],
        "content": """
<h2>PM-96: Juftlik (juft-toq) gʻoyasi</h2>

<p>Stolda 9 ta stakan turibdi va hammasi agʻdarib qoʻyilgan. Bir
harakatda roppa-rosa <b>2 tasini</b> agʻdarish mumkin. Hammasini
toʻgʻri holatga keltirish mumkinmi?</p>

<p>Urinib koʻrsangiz — boʻlmaydi. Yana urinsangiz — yana boʻlmaydi.
Lekin «men koʻp urindim» degan gap isbot emas. Ehtimol yoʻlni
topolmagandirsiz?</p>

<p>Bu darsda biz buni <b>isbotlaymiz</b>. Va isbot uchun bitta gʻoya
kifoya: oʻzgarmaydigan xossa topish.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>juft va toq sonlarning qoʻshilish qoidalarini eslaysiz;</li>
    <li>oʻzgarmas xossa — invariant — nima ekanini bilib olasiz;</li>
    <li>«mumkin emas» degan javobni isbotlaysiz;</li>
    <li>doskani boʻyash usulini koʻrasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Imkonsizlik isboti</span>
  <span class="pe-chip pe-chip--o">oʻzgarmas xossa</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--neg">maqsad unga zid</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">mumkin emas</span>
</div>

<h3>1. Juft va toq — qoidalarni eslaymiz</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Amal</th><th>Natija</th><th>Nega</th></tr>
  <tr><td>juft + juft</td><td class="pm-word__sym">juft</td>
    <td>2a + 2b = 2(a + b)</td></tr>
  <tr><td>toq + toq</td><td class="pm-word__sym">juft</td>
    <td>(2a+1) + (2b+1) = 2(a+b+1)</td></tr>
  <tr><td>juft + toq</td><td class="pm-word__sym">toq</td>
    <td>2a + 2b + 1</td></tr>
  <tr><td>juft × istalgan son</td><td class="pm-word__sym">juft</td>
    <td>2a × n = 2(an)</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Ikkita toq son qoʻshilsa JUFT chiqadi</p>
  <p>Bu qoida koʻpchilikni ajablantiradi: 3 + 5 = 8, 7 + 9 = 16,
  11 + 13 = 24. Har bir toq sonda «bitta ortiqcha» bor; ikkitasi
  qoʻshilganda oʻsha ikkita ortiqcha juftlashadi.</p>
</div>

<h3>2. Stakanlar masalasi — isbot</h3>

<p>Endi boshdagi masalaga qaytamiz. Kuzatib boradigan narsani
tanlaymiz: <b>agʻdarilgan stakanlar soni</b>.</p>

<p>Boshida u <strong>9</strong> ta — <b>toq</b> son.</p>

<p>Bir harakatda ikkita stakan agʻdariladi. Uch xil hol boʻlishi
mumkin:</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Qanday ikkita stakan olindi</th><th>Agʻdarilganlar soni</th><th>Oʻzgarish</th></tr>
  <tr><td>Ikkalasi ham agʻdarilgan edi</td>
    <td class="pm-word__sym">2 taga kamaydi</td><td>−2</td></tr>
  <tr><td>Ikkalasi ham toʻgʻri edi</td>
    <td class="pm-word__sym">2 taga ortdi</td><td>+2</td></tr>
  <tr><td>Biri agʻdarilgan, biri toʻgʻri</td>
    <td class="pm-word__sym">oʻzgarmadi</td><td>0</td></tr>
</table></div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Har bir harakatda oʻzgarish: −2, 0 yoki +2</span>
    <span class="pm-solve__why">Uchala hol ham juft son</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Toq songa juft son qoʻshilsa, toq qoladi</span>
    <span class="pm-solve__why">Yuqoridagi jadval</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Demak son har doim TOQ boʻlib qoladi</span>
    <span class="pm-solve__why">Nechta harakat qilinsa ham</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Maqsad esa 0 — juft son. Mumkin emas.</span>
    <span class="pm-solve__why">Toq son hech qachon 0 boʻlmaydi</span>
  </div>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Invariant — oʻzgarmas xossa</p>
  <p>Biz «agʻdarilganlar sonining juft-toqligi» degan xossani topdik
  va u <b>hech qanday harakatda oʻzgarmasligini</b> koʻrsatdik.
  Shunday xossa <b>invariant</b> deyiladi. Agar boshlangʻich holatning
  invarianti maqsadnikidan farq qilsa — maqsadga yetib boʻlmaydi.
  Bu — imkonsizlikni isbotlashning eng oddiy va eng kuchli
  usuli.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Agar 3 tadan agʻdarilsa nima boʻladi?</p>
  <p>Unda har bir harakat sonni ±3 yoki ±1 ga oʻzgartiradi — hammasi
  <b>toq</b>. Demak juft-toqlik har safar almashadi va maqsadga yetish
  mumkin boʻlib qoladi. Qoida oʻzgarmadi, faqat harakat
  oʻzgardi.</p>
</div>

<h3>3. Ikkinchi misol — belgilar bilan</h3>

<p><b>Masala.</b> 1 dan 10 gacha boʻlgan sonlar oldiga «+» yoki «−»
belgilarini qoʻyib, natijani 0 ga tenglashtirish mumkinmi?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">1 + 2 + … + 10 = 55</span>
    <span class="pm-solve__why">Hammasi «+» boʻlganda</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Bitta «+» ni «−» ga almashtirsak, yigʻindi 2k ga kamayadi</span>
    <span class="pm-solve__why">+k oʻrniga −k → farq 2k, yaʼni juft</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Demak yigʻindining juft-toqligi oʻzgarmaydi</span>
    <span class="pm-solve__why">Invariant topildi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">55 toq, 0 juft → mumkin emas</span>
    <span class="pm-solve__why">Toqni juftga aylantirib boʻlmaydi</span>
  </div>
</div>

<h3>4. Doskani boʻyash</h3>

<p>Juftlik gʻoyasi faqat sonlarda emas. Mana uning eng chiroyli
koʻrinishi.</p>

<p><b>Masala.</b> 4 × 4 doskadan ikkita qarama-qarshi burchak kesib
olindi. Qolgan qismni 2 × 1 oʻlchamli domino toshlari bilan toʻliq
qoplash mumkinmi?</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 175" role="img" aria-label="Toʻrtga toʻrt doska, ikkita qarama-qarshi burchagi olib tashlangan">
    <rect class="pm-ln pm-ln--dash" x="100" y="20" width="32" height="32" fill="none"/>
    <rect class="pm-fill" x="132" y="20" width="32" height="32"/>
    <rect class="pm-fill pm-fill--hl" x="164" y="20" width="32" height="32"/>
    <rect class="pm-fill" x="196" y="20" width="32" height="32"/>
    <rect class="pm-fill" x="100" y="52" width="32" height="32"/>
    <rect class="pm-fill pm-fill--hl" x="132" y="52" width="32" height="32"/>
    <rect class="pm-fill" x="164" y="52" width="32" height="32"/>
    <rect class="pm-fill pm-fill--hl" x="196" y="52" width="32" height="32"/>
    <rect class="pm-fill pm-fill--hl" x="100" y="84" width="32" height="32"/>
    <rect class="pm-fill" x="132" y="84" width="32" height="32"/>
    <rect class="pm-fill pm-fill--hl" x="164" y="84" width="32" height="32"/>
    <rect class="pm-fill" x="196" y="84" width="32" height="32"/>
    <rect class="pm-fill" x="100" y="116" width="32" height="32"/>
    <rect class="pm-fill pm-fill--hl" x="132" y="116" width="32" height="32"/>
    <rect class="pm-fill" x="164" y="116" width="32" height="32"/>
    <rect class="pm-ln pm-ln--dash" x="196" y="116" width="32" height="32" fill="none"/>
    <rect class="pm-ln" x="100" y="20" width="128" height="128" fill="none"/>
    <text class="pm-lbl pm-lbl--hl" x="116" y="165" text-anchor="middle">6 ta sariq</text>
    <text class="pm-lbl" x="212" y="165" text-anchor="middle">8 ta koʻk</text>
  </svg>
  <figcaption>Kataklar shaxmatdagidek navbatma-navbat boʻyalgan.
  Kesib olingan ikkala burchak ham <b>sariq</b> edi — shuning
  uchun sariq kataklar 6 ta, koʻk kataklar esa 8 ta qoldi.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Domino har doim 2 ta qoʻshni katakni qoplaydi</span>
    <span class="pm-solve__why">Qoʻshni kataklar har doim har xil rangda</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Demak har bir domino — 1 ta sariq va 1 ta koʻk</span>
    <span class="pm-solve__why">Bu ham invariant</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Toʻliq qoplash uchun ranglar soni teng boʻlishi kerak</span>
    <span class="pm-solve__why">Har dominoda bittadan</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">6 ≠ 8 → qoplab boʻlmaydi</span>
    <span class="pm-solve__why">Nechta urinilsa ham</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Kataklar soni yetarli boʻlishi kifoya emas</p>
  <p>Qolgan 14 ta katak va 7 ta domino — sonlar mos keladi. Shunga
  qaramay qoplab boʻlmaydi. Bu — juftlik gʻoyasining eng kuchli
  tomoni: u sonlar «toʻgʻri» boʻlganda ham imkonsizlikni
  koʻrsata oladi.</p>
</div>

<h3>Matnli masala</h3>

<p>Sinfda 25 oʻquvchi bor. Bayram kuni ular bir-biri bilan qoʻl berib
koʻrishishdi.</p>

<p><b>Har bir oʻquvchi roppa-rosa 3 kishi bilan qoʻl berishi
mumkinmi?</b></p>

<p><b>Reja:</b> qoʻl berishlar sonini ikki xil yoʻl bilan sanaymiz.
Ikkala hisob bir xil chiqishi shart — aks holda bunday holat
mumkin emas.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Har bir oʻquvchi 3 marta qoʻl berdi</span>
    <span class="pm-solve__why">Masalaning sharti</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Jami: 25 × 3 = 75</span>
    <span class="pm-solve__why">Hamma oʻquvchilar boʻyicha yigʻindi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Lekin har bir qoʻl berish IKKI marta sanaldi</span>
    <span class="pm-solve__why">Unda ikki kishi qatnashadi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Demak qoʻl berishlar soni: 75 ÷ 2 = 37,5</span>
    <span class="pm-solve__why">Butun son chiqmadi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Mumkin emas</span>
    <span class="pm-solve__why">Qoʻl berishlar soni butun boʻlishi shart</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Boshqacha aytganda</p>
  <p>Yigʻindi 25 × 3 = 75 — <b>toq</b> son. Lekin u har doim juft
  boʻlishi kerak, chunki u qoʻl berishlar sonining ikki barobari.
  Toq ≠ juft, demak bunday holat mavjud emas.
  <br><b>Javob:</b> yoʻq, mumkin emas.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Bu qoida har doim ishlaydi</p>
  <p>Istalgan guruhda «har kim necha kishi bilan qoʻl berdi» degan
  sonlarning yigʻindisi <b>har doim juft</b> boʻladi. Shuning uchun
  toq sondagi odam toq marta qoʻl berishi mumkin emas. 25 ta odam
  4 marta qoʻl berishi esa mumkin: 25 × 4 = 100, juft ✓</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">«Men koʻp urindim, boʻlmadi — demak mumkin
  emas»</p>
  <p class="pe-fix__good">Invariant topib, isbotlash</p>
  <p class="pe-fix__why">Urinishlar isbot emas. Balki yoʻl bor, siz
  topmagandirsiz. Invariant esa hamma yoʻlni bir yoʻla yopadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">toq + toq = toq</p>
  <p class="pe-fix__good">toq + toq = juft</p>
  <p class="pe-fix__why">3 + 5 = 8, 7 + 7 = 14. Ikkita «ortiqcha
  bir» qoʻshilib juftlashadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Ikkita stakan agʻdarilsa, juftlik
  oʻzgaradi</p>
  <p class="pe-fix__good">±2 yoki 0 — juftlik oʻzgarmaydi</p>
  <p class="pe-fix__why">Uchala hol ham juft son bilan oʻzgartiradi,
  demak toqlik saqlanadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">25 × 3 = 75 ta qoʻl berish boʻlgan</p>
  <p class="pe-fix__good">75 — bu ikki barobar sanalgan son</p>
  <p class="pe-fix__why">Har bir qoʻl berishda ikki kishi qatnashadi,
  shuning uchun yigʻindi qoʻl berishlar sonining ikki
  barobari.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Toq son bilan toq sonning yigʻindisi qanday
  boʻladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Juft.</b> (2a + 1) + (2b + 1) = 2(a + b + 1). Misol:
    9 + 7 = 16.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Uchta toq sonning yigʻindisi qanday
  boʻladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Toq.</b> Ikkitasi qoʻshilib juft beradi, uchinchisi uni
    yana toq qiladi: 3 + 5 + 7 = 15.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Stolda 7 ta stakan agʻdarilgan. Har safar
  2 tasi agʻdariladi. Hammasini toʻgʻrilash mumkinmi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Yoʻq.</b> 7 — toq son, har bir harakat esa juft son bilan
    oʻzgartiradi (−2, 0, +2). Demak agʻdarilganlar soni har doim toq
    qoladi va hech qachon 0 boʻlmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Stolda 8 ta stakan agʻdarilgan. Har safar
  2 tasi agʻdariladi. Endi-chi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Ha, mumkin.</b> 8 — juft son, maqsad 0 ham juft. Toʻrt marta
    ikkitadan agʻdarish yetadi. Invariant bu safar toʻsiq
    boʻlmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. 1 dan 9 gacha sonlar oldiga «+» va «−»
  qoʻyib, 0 chiqarish mumkinmi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Yoʻq.</b> 1 + 2 + … + 9 = 45 — toq. Belgi almashtirish
    yigʻindini juft songa oʻzgartiradi, demak toqlik saqlanadi.
    0 esa juft.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Sinfda 15 oʻquvchi bor. Har biri roppa-rosa
  5 kishi bilan qoʻl berishi mumkinmi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Yoʻq.</b> 15 × 5 = 75 — toq son. Lekin bu yigʻindi qoʻl
    berishlar sonining ikki barobari boʻlishi, yaʼni juft boʻlishi
    kerak edi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">7. Sinfda 10 oʻquvchi bor. Har biri roppa-rosa
  3 kishi bilan qoʻl berishi mumkinmi? Nechta qoʻl berish boʻladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Ha, mumkin. 15 ta qoʻl berish.</b> 10 × 3 = 30 — juft son,
    demak toʻsiq yoʻq. Qoʻl berishlar soni 30 ÷ 2 = 15. Diqqat:
    juftlik faqat <b>imkonsizlikni</b> isbotlaydi; juft chiqishi esa
    mumkinligini kafolatlamaydi, faqat toʻsiq yoʻqligini
    koʻrsatadi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Juft son</b><span>2 ga qoldiqsiz boʻlinadigan son; ingl. even
    number</span></li>
  <li><b>Toq son</b><span>2 ga boʻlinmaydigan son; ingl. odd
    number</span></li>
  <li><b>Juftlik</b><span>sonning juft yoki toqligi; ingl.
    parity</span></li>
  <li><b>Invariant</b><span>hech qanday harakatda oʻzgarmaydigan xossa;
    ingl. invariant</span></li>
  <li><b>Imkonsizlik isboti</b><span>maqsadga yetib boʻlmasligini
    koʻrsatish; ingl. impossibility proof</span></li>
  <li><b>Harakat</b><span>holatni oʻzgartiradigan bitta qadam; ingl.
    move</span></li>
  <li><b>Holat</b><span>obyektlarning ayni paytdagi joylashuvi; ingl.
    state</span></li>
  <li><b>Boʻyash usuli</b><span>kataklarni navbatma-navbat rangga
    ajratish; ingl. colouring argument</span></li>
  <li><b>Domino</b><span>ikkita qoʻshni katakni qoplovchi tosh; ingl.
    domino</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>toq + toq = juft; juft + toq = toq.</li>
    <li>Invariant — hech qanday harakatda oʻzgarmaydigan xossa.</li>
    <li>Boshlangʻich holat bilan maqsadning invarianti farq qilsa —
      mumkin emas.</li>
    <li>«Urinib koʻrdim, boʻlmadi» isbot emas; invariant esa
      isbot.</li>
    <li>Doskani boʻyash — juftlikning geometrik koʻrinishi.</li>
    <li>Qoʻl berishlar yigʻindisi har doim juft boʻladi.</li>
    <li>Juftlik imkonsizlikni isbotlaydi; mumkinligini esa yoʻlni
      koʻrsatib isbotlash kerak.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-97 — Dirixle prinsipi
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-97: Dirixle prinsipi — kaptarxona qoidasi",
        "category": "math",
        "order": 97,
        "summary": (
            "Agar kaptarlar uyalardan koʻp boʻlsa, kamida bitta uyada "
            "ikkita kaptar bor. Juda oddiy koʻrinadigan bu gap "
            "kutilmagan narsalarni isbotlaydi."
        ),
        "stories": ["Toshkentda ikki kishining sochi bir xil"],
        "content": """
<h2>PM-97: Dirixle prinsipi — kaptarxona qoidasi</h2>

<p>Sinfda 13 oʻquvchi bor. Ularning kamida ikkitasi <b>bir oyda</b>
tugʻilgan.</p>

<p>Bu gapni hech kimning tugʻilgan kunini bilmasdan aytdik. Va u
shunchaki ehtimol emas — <b>kafolat</b>. Chunki yilda 12 oy bor,
oʻquvchilar esa 13 ta.</p>

<p>Bu — Dirixle prinsipi. U juda oddiy, lekin uning yordamida ajablanarli
narsalarni isbotlash mumkin.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>kaptarxona qoidasini oʻrganasiz;</li>
    <li>«eng yomon hol» mulohazasini qoʻllaysiz;</li>
    <li>kuchaytirilgan shaklini (kamida nechta) hisoblaysiz;</li>
    <li>prinsip nimani isbotlamasligini bilib olasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Dirixle prinsipi</span>
  <span class="pe-chip pe-chip--o">n + 1 ta kaptar</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">n ta uya</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">kamida bittasida 2 ta</span>
</div>

<h3>1. Qoida va uning isboti</h3>

<figure class="pm-fig">
  <svg viewBox="0 0 320 125" role="img" aria-label="Besh kaptar toʻrt uyaga joylashtirilgan: bir uyada ikkitasi">
    <rect class="pm-ln" x="30" y="45" width="50" height="45" fill="none"/>
    <rect class="pm-ln" x="100" y="45" width="50" height="45" fill="none"/>
    <rect class="pm-ln" x="170" y="45" width="50" height="45" fill="none"/>
    <rect class="pm-ln" x="240" y="45" width="50" height="45" fill="none"/>
    <circle class="pm-pt" cx="44" cy="68" r="7"/>
    <circle class="pm-pt" cx="66" cy="68" r="7"/>
    <circle class="pm-pt" cx="125" cy="68" r="7"/>
    <circle class="pm-pt" cx="195" cy="68" r="7"/>
    <circle class="pm-pt" cx="265" cy="68" r="7"/>
    <text class="pm-lbl pm-lbl--hl" x="55" y="35" text-anchor="middle">2 ta</text>
    <text class="pm-lbl" x="125" y="35" text-anchor="middle">1 ta</text>
    <text class="pm-lbl" x="195" y="35" text-anchor="middle">1 ta</text>
    <text class="pm-lbl" x="265" y="35" text-anchor="middle">1 ta</text>
    <text class="pm-lbl" x="160" y="112" text-anchor="middle">5 ta kaptar, 4 ta uya</text>
  </svg>
  <figcaption>Beshta kaptarni toʻrtta uyaga qanday joylashtirmang,
  kamida bitta uyada ikkitasi boʻladi.</figcaption>
</figure>

<p><b>Nega shunday?</b> Teskarisini faraz qilaylik: har bir uyada
koʻpi bilan bitta kaptar boʻlsin. Unda jami kaptarlar soni koʻpi
bilan 4 ta boʻlardi. Lekin bizda 5 ta. Ziddiyat — demak faraz
notoʻgʻri.</p>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Prinsipning umumiy koʻrinishi</p>
  <p>Agar <b>n</b> ta obyekt <b>k</b> ta guruhga boʻlinsa va n &gt; k
  boʻlsa, kamida bitta guruhda <b>2 ta</b> obyekt boʻladi.
  <br>Kuchaytirilgan shakli: kamida bitta guruhda <b>n ÷ k dan kam
  boʻlmagan</b> (yuqoriga yaxlitlangan) obyekt boʻladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">13 oʻquvchi, 12 oy → kamida 2 tasi bir oyda</p>
  <p class="pe-ex__uz">Oʻn uch kaptar, oʻn ikki uya.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">400 oʻquvchi, 365 kun → kamida 2 tasi bir kunda</p>
  <p class="pe-ex__uz">Katta maktabda ikki kishining tugʻilgan kuni
  albatta bir xil.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">25 oʻquvchi, 12 oy → 25 ÷ 12 = 2,08 → kamida 3 tasi bir oyda</p>
  <p class="pe-ex__uz">Yaxlitlash yuqoriga qilinadi (PM-14): odam
  soni butun boʻlishi kerak.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Nega yuqoriga yaxlitlanadi?</p>
  <p>Agar har bir oyda koʻpi bilan 2 ta oʻquvchi boʻlsa, jami
  12 × 2 = 24 ta boʻlardi. Bizda esa 25 ta. Demak biror oyda kamida
  3 ta bor. 2,08 ni pastga yaxlitlash mantiqni buzadi.</p>
</div>

<h3>2. Eng yomon hol — asosiy mulohaza</h3>

<p>Dirixle masalalarining koʻpchiligi shu savol bilan yechiladi:
<b>eng omadsiz holda nima boʻladi?</b></p>

<p><b>Masala.</b> Qorongʻi xonada qutida 10 ta qora va 10 ta oq
paypoq bor. Koʻrmasdan kamida nechta paypoq olish kerakki, ular
orasida bir xil rangdagi juft albatta boʻlsin?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Eng yomon hol: 1 ta qora va 1 ta oq</span>
    <span class="pm-solve__why">Ikkita olganda juft chiqmasligi mumkin</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Uchinchi paypoq — yo qora, yo oq</span>
    <span class="pm-solve__why">Uchinchi rang yoʻq</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Javob: 3 ta</span>
    <span class="pm-solve__why">3 ta kaptar, 2 ta uya (rang)</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">«Kafolatlansin» degan soʻz muhim</p>
  <p>Ikkita paypoq olganda ham juft chiqishi <b>mumkin</b> — omad
  kelsa. Lekin savol omad haqida emas: javob <b>har qanday</b> holda
  ishlashi kerak. Shuning uchun har doim eng omadsiz holni
  hisoblang.</p>
</div>

<h3>3. Prinsip nimani AYTMAYDI</h3>

<p>Bu — darsning eng muhim yarim sahifasi.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Prinsip aytadi</p>
    <p>Bunday ikki kishi <b>bor</b>.
    <br>Ular albatta mavjud.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Prinsip aytmaydi</p>
    <p>Ular <b>kimligi</b>.
    <br>Qaysi oyda ekani.
    <br>Nechtaligi (aniq).</p>
  </div>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Mavjudlik isboti</p>
  <p>Dirixle prinsipi <b>mavjudlikni</b> isbotlaydi, topib bermaydi.
  «Sinfda bir oyda tugʻilgan ikki kishi bor» — rost. «Ular Bekzod
  bilan Afsona» — buni prinsip aytmaydi, buning uchun roʻyxatni
  koʻrish kerak. PM-96 dagi juftlik esa aksincha —
  <b>imkonsizlikni</b> isbotlardi. Ikki dars, isbotlashning ikki
  turi.</p>
</div>

<h3>Matnli masala</h3>

<p>Qutida 5 xil rangdagi sharlar bor va har bir rangdan koʻp miqdorda
mavjud. Bekzod koʻzini yumib shar olmoqda.</p>

<p><b>Kamida nechta shar olsa, ular orasida bir xil rangdagi 3 ta
shar boʻlishi kafolatlanadi?</b></p>

<p><b>Reja:</b> eng yomon holni quramiz — Bekzodga imkon qadar uzoq
vaqt «uchtalik» chiqmasin.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Eng yomon hol: har rangdan 2 tadan</span>
    <span class="pm-solve__why">Uchtalik hali yoʻq, lekin koʻproq olib boʻlmaydi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5 × 2 = 10 ta shar</span>
    <span class="pm-solve__why">Beshta rang, har biridan ikkitadan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">11-shar qaysi rang boʻlmasin…</span>
    <span class="pm-solve__why">Beshta rangdan biriga tushadi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">…oʻsha rang 3 taga yetadi. Javob: 11 ta</span>
    <span class="pm-solve__why">10 ta yetarli emas, 11 ta kafolatlaydi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Ikki tomondan tekshiramiz</p>
  <p><b>10 ta yetarli emasmi?</b> Ha — har rangdan 2 tadan olingan
  boʻlishi mumkin, unda uchtalik yoʻq.
  <br><b>11 ta yetarlimi?</b> Ha — agar har rangdan koʻpi bilan
  2 tadan boʻlsa, jami 10 tadan oshmasdi. 11 ta bor ekan, demak biror
  rangdan kamida 3 ta bor ✓
  <br><b>Javob:</b> 11 ta shar.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Umumiy qoida</span>
  <span>k xil rangdan m tadan kafolatlash uchun
  <b>k × (m − 1) + 1</b> ta olish kerak. Bu yerda:
  5 × (3 − 1) + 1 = 11 ✓ Paypoq masalasida:
  2 × (2 − 1) + 1 = 3 ✓</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">«13 oʻquvchidan ikkitasi bir oyda tugʻilgan
  boʻlishi mumkin»</p>
  <p class="pe-fix__good">Albatta tugʻilgan — bu kafolat</p>
  <p class="pe-fix__why">Dirixle prinsipi ehtimol haqida emas. U hech
  qanday istisnosiz ishlaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Paypoq masalasida javob 2 ta</p>
  <p class="pe-fix__good">3 ta</p>
  <p class="pe-fix__why">Ikkita olganda bittasi qora, bittasi oq
  chiqishi mumkin. «Kafolatlansin» degani eng yomon holni ham
  qoplashi kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">25 ÷ 12 = 2,08 → kamida 2 ta</p>
  <p class="pe-fix__good">Kamida 3 ta</p>
  <p class="pe-fix__why">Yuqoriga yaxlitlanadi. Har oyda koʻpi bilan
  2 ta boʻlsa, jami 24 ta boʻlardi — 25 ta emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">«Demak Bekzod bilan Afsona bir oyda
  tugʻilgan»</p>
  <p class="pe-fix__good">«Bunday ikki kishi bor» — kimligi
  nomaʼlum</p>
  <p class="pe-fix__why">Prinsip mavjudlikni isbotlaydi, aniq
  odamlarni koʻrsatmaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Sinfda 8 oʻquvchi bor, hafta esa 7 kundan
  iborat. Nima deyish mumkin?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Kamida ikkitasi haftaning bir kunida tugʻilgan.</b> 8 ta
    kaptar, 7 ta uya.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Qutida 3 xil rangdagi qalam bor. Kamida
  nechta olsa, ikkitasi bir xil rangda boʻlishi kafolatlanadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>4 ta.</b> Eng yomon hol — har rangdan bittadan (3 ta).
    Toʻrtinchisi albatta takrorlanadi. Formula:
    3 × (2 − 1) + 1 = 4.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 30 oʻquvchi bor, yilda 12 oy. Kamida
  nechtasi bir oyda tugʻilgan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Kamida 3 tasi.</b> 30 ÷ 12 = 2,5 → yuqoriga yaxlitlab 3.
    Tekshirish: har oyda koʻpi bilan 2 ta boʻlsa, jami 24 ta
    boʻlardi — 30 ta emas.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Qutida 4 xil rangdagi shar bor. Kamida
  nechta olsa, bir xil rangdagi 2 ta shar kafolatlanadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5 ta.</b> 4 × (2 − 1) + 1 = 5. Eng yomon hol — har rangdan
    bittadan, yaʼni 4 ta; beshinchisi takrorlaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Qutida 3 xil rangdagi shar bor. Bir xil
  rangdagi 4 ta shar kafolatlanishi uchun kamida nechta olish
  kerak?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>10 ta.</b> 3 × (4 − 1) + 1 = 10. Eng yomon hol — har
    rangdan 3 tadan (9 ta), oʻninchisi biror rangni 4 taga
    yetkazadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. 100 ta son berilgan. Ularning kamida
  nechtasi bir xil qoldiq beradi 7 ga boʻlinganda?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Kamida 15 tasi.</b> 7 ga boʻlganda qoldiq 0 dan 6 gacha —
    jami 7 xil (uyalar). 100 ÷ 7 ≈ 14,3 → yuqoriga yaxlitlab 15.
    Tekshirish: har qoldiqdan koʻpi bilan 14 ta boʻlsa, jami
    98 ta boʻlardi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">7. Dirixle prinsipi yordamida «sinfda Bekzod
  bilan Afsona bir oyda tugʻilgan» deb aytish mumkinmi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Yoʻq.</b> Prinsip faqat <b>bunday ikki kishi borligini</b>
    isbotlaydi, ularning kimligini emas. Aniq odamlarni bilish uchun
    tugʻilgan kunlar roʻyxatini koʻrish kerak.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Dirixle prinsipi</b><span>kaptarxona qoidasi; ingl. pigeonhole
    principle</span></li>
  <li><b>Uya</b><span>obyektlar taqsimlanadigan guruh; ingl.
    hole</span></li>
  <li><b>Eng yomon hol</b><span>maqsadga eng uzoq turadigan holat;
    ingl. worst case</span></li>
  <li><b>Kafolat</b><span>har qanday holda bajariladigan xulosa; ingl.
    guarantee</span></li>
  <li><b>Mavjudlik isboti</b><span>obyekt borligini koʻrsatish, uni
    topmasdan; ingl. existence proof</span></li>
  <li><b>Ziddiyat</b><span>farazdan kelib chiqqan qarama-qarshilik;
    ingl. contradiction</span></li>
  <li><b>Teskari faraz</b><span>isbot uchun aksini taxmin qilish; ingl.
    assumption for contradiction</span></li>
  <li><b>Qoldiq</b><span>boʻlishdan keyin qoladigan son; ingl.
    remainder</span></li>
  <li><b>Yuqoriga yaxlitlash</b><span>butun songacha oshirish; ingl.
    rounding up</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>n + 1 ta kaptar n ta uyaga → kamida bittasida 2 ta.</li>
    <li>Kuchaytirilgan shakli: kamida n ÷ k (yuqoriga yaxlitlangan)
      ta.</li>
    <li>«Kafolatlansin» deganda eng yomon holni hisoblang.</li>
    <li>k xil turdan m tadan kafolatlash: k × (m − 1) + 1 ta.</li>
    <li>Prinsip mavjudlikni isbotlaydi, kimligini aytmaydi.</li>
    <li>Isbot teskari faraz bilan boradi: aksini faraz qilib,
      ziddiyatga kelinadi.</li>
    <li>PM-96 imkonsizlikni isbotlardi, PM-97 esa mavjudlikni.</li>
  </ul>
</div>
""",
    },
]
