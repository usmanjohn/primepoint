# -*- coding: utf-8 -*-
"""Prime Korean — Block A, darslar 6–8 (Hangul bloki yakuni).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_06_08.py --author=prime
"""

PLAYLIST = {
    "title": "Prime Korean",
    "category": "korean",
    "description": (
        "Koreys tili noldan TOPIK II gacha — 100 ta dars. Hangul, grammatika qoliplari, "
        "oʻzbekcha tushuntirish va oʻzingiz tekshiradigan mashqlar."
    ),
}

TUTORIALS = [
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-6: Undoshlar 3: qattiq ㄲ ㄸ ㅃ ㅆ ㅉ",
        "category": "korean",
        "order": 6,
        "summary": (
            "Koreys tilida har bir undosh uch xil boʻladi: oddiy, nafasli va qattiq. "
            "Uchinchi qatorni oʻrganib, 14+5 undoshni toʻliq yopasiz."
        ),
        "content": """
<h2>PK-6: Undoshlar 3: qattiq ㄲ ㄸ ㅃ ㅆ ㅉ</h2>

<p>Uchta soʻzni ketma-ket ayting: <b>달</b> — "oy", <b>탈</b> — "niqob", <b>딸</b> —
"qiz". Uchalasining unlisi bir xil, 받침i bir xil, faqat birinchi undoshi farq qiladi.
Oʻzbek tilida bunday <em>uchlik</em> yoʻq — bizda koʻpi bilan ikkita (t / d). Koreys
tilida esa uchtasi ham alohida maʼno. Bugun uchinchisini — <b>qattiq undoshlarni</b>
oʻrganamiz va shu bilan Hangulning butun undosh tizimi yopiladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Beshta qattiq undoshni yozasiz: ㄲ ㄸ ㅃ ㅆ ㅉ</li>
    <li>Koreys undoshlarining uchlik tizimini toʻliq koʻrasiz</li>
    <li>Qattiq tovushni oʻzbekcha "ikki" soʻzi orqali topasiz</li>
    <li>달 / 탈 / 딸 kabi uchliklarni ajratib aytasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Koreys undoshi — uch qator</span>
  <span class="pe-chip pe-chip--s">oddiy ㄷ</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--aux">nafasli ㅌ</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--neg">qattiq ㄸ</span>
</div>

<h3>1. Yozilishi — harf ikki marta</h3>

<p>Yaxshi xabar: bu yerda <b>yangi shakl yoʻq</b>. Qattiq undosh — oddiy undoshning ikki
marta yozilgani, xolos.</p>

<div class="pk-hangul">
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㄲ</span>
    <span class="pk-hangul__rom">kk</span>
    <span class="pk-hangul__uz">ㄱ + ㄱ</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㄸ</span>
    <span class="pk-hangul__rom">tt</span>
    <span class="pk-hangul__uz">ㄷ + ㄷ</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㅃ</span>
    <span class="pk-hangul__rom">pp</span>
    <span class="pk-hangul__uz">ㅂ + ㅂ</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㅆ</span>
    <span class="pk-hangul__rom">ss</span>
    <span class="pk-hangul__uz">ㅅ + ㅅ</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㅉ</span>
    <span class="pk-hangul__rom">jj</span>
    <span class="pk-hangul__uz">ㅈ + ㅈ</span></div>
</div>

<h3>2. Qanday aytiladi — nafasni <em>toʻxtating</em></h3>

<p>PK-5 da qogʻoz sinovini qilgan edingiz: <b>바</b> da qogʻoz sal qimirlaydi,
<b>파</b> da uchib ketadi. Endi <b>빠</b> deng — qogʻoz <em>umuman</em> qimirlamaydi.</p>

<p>Qattiq undoshni aytish uchun <b>tomoqni tarang qiling va nafasni chiqarmang</b>.
Tovush kuchli, keskin va quruq boʻladi — go'yo uni siqib chiqargandek.</p>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu tovush sizda <b>allaqachon bor</b>. Oʻzbekcha <em>ikki</em>, <em>akka</em>,
<em>tappa</em> soʻzlarini ayting — ikkilangan undosh keskin va tarang chiqadi. Mana shu
— koreys qattiq undoshi. Faqat koreyschada u soʻz <b>boshida</b> ham keladi:
<b>까</b>, <b>따</b>, <b>빠</b>. "Ikki" ni ayting, keyin faqat "kki" qismini soʻz boshida
takrorlang — 끼 chiqadi.</div>

<h3>3. Uchlik tizimi — toʻliq jadval</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Oddiy</th><th>Nafasli</th><th>Qattiq</th><th>Nafas</th><th>Tomoq</th></tr>
  <tr><td class="pk-stem">ㄱ</td><td class="pk-end">ㅋ</td><td class="pk-res">ㄲ</td>
      <td class="pk-uz">oz — koʻp — yoʻq</td><td class="pk-uz">boʻsh — boʻsh — tarang</td></tr>
  <tr><td class="pk-stem">ㄷ</td><td class="pk-end">ㅌ</td><td class="pk-res">ㄸ</td>
      <td class="pk-uz">oz — koʻp — yoʻq</td><td class="pk-uz">boʻsh — boʻsh — tarang</td></tr>
  <tr><td class="pk-stem">ㅂ</td><td class="pk-end">ㅍ</td><td class="pk-res">ㅃ</td>
      <td class="pk-uz">oz — koʻp — yoʻq</td><td class="pk-uz">boʻsh — boʻsh — tarang</td></tr>
  <tr><td class="pk-stem">ㅈ</td><td class="pk-end">ㅊ</td><td class="pk-res">ㅉ</td>
      <td class="pk-uz">oz — koʻp — yoʻq</td><td class="pk-uz">boʻsh — boʻsh — tarang</td></tr>
  <tr><td class="pk-stem">ㅅ</td><td class="pk-end">—</td><td class="pk-res">ㅆ</td>
      <td class="pk-uz">ㅅ ning nafasli jufti yoʻq</td><td class="pk-uz">boʻsh — tarang</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Qattiq undosh <b>hech qachon jaranglashmaydi</b>. PK-4 dagi qoida (unlilar orasida
ㄱ → "g") faqat oddiy undoshlarga tegishli. 아까 har doim [akka], hech qachon
[aga] emas.</div>

<h3>4. Uchta minimal juftlik — farqni eshiting</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Oddiy</th><th>Nafasli</th><th>Qattiq</th></tr>
  <tr><td class="pk-res">달 <span class="pk-uz">— oy</span></td>
      <td class="pk-res">탈 <span class="pk-uz">— niqob</span></td>
      <td class="pk-res">딸 <span class="pk-uz">— qiz (farzand)</span></td></tr>
  <tr><td class="pk-res">불 <span class="pk-uz">— olov</span></td>
      <td class="pk-res">풀 <span class="pk-uz">— oʻt, yelim</span></td>
      <td class="pk-res">뿔 <span class="pk-uz">— shox</span></td></tr>
  <tr><td class="pk-res">자다 <span class="pk-uz">— uxlamoq</span></td>
      <td class="pk-res">차다 <span class="pk-uz">— sovuq boʻlmoq</span></td>
      <td class="pk-res">짜다 <span class="pk-uz">— sho'r boʻlmoq</span></td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Uchalasini ketma-ket, sekin ayting: <b>달 — 탈 — 딸</b>. Birinchisida ogʻiz bemalol,
ikkinchisida nafas otiladi, uchinchisida tomoq siqiladi. Har kuni bir daqiqa shu uchlikni
takrorlasangiz, bir haftada quloq oʻzi ajrata boshlaydi.</div>

<h3>5. Soʻzlar</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">아빠 — 오빠</p>
  <p class="pe-ex__rom">[appa] — [oppa]</p>
  <p class="pe-ex__uz">dada — aka (qiz bola uchun)</p>
  <p class="pe-ex__why">Ikkalasi ham eng koʻp ishlatiladigan soʻzlardan, ikkalasi ham
     qattiq ㅃ bilan.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">꽃</p>
  <p class="pe-ex__rom">[kkot]</p>
  <p class="pe-ex__uz">gul</p>
  <p class="pe-ex__why">Boshda qattiq ㄲ. Oxiridagi ㅊ nega [t] boʻlib oʻqilishini
     PK-7 da koʻramiz.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">빵이 싸요</p>
  <p class="pe-ex__rom">[ppangi ssayo]</p>
  <p class="pe-ex__uz">Non arzon.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">또 만나요</p>
  <p class="pe-ex__rom">[tto mannayo]</p>
  <p class="pe-ex__uz">Yana koʻrishamiz.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">빠 ni nafas bilan aytish (파 kabi).</p>
  <p class="pe-good">Qattiq undoshda <b>nafas yoʻq</b>. Qogʻoz umuman qimirlamasligi
     kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">아빠 ni "aba" deb, ㅃ ni jaranglatib aytish.</p>
  <p class="pe-good">Qattiq undosh <b>hech qachon jaranglashmaydi</b>:
     <b>[appa]</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">딸 va 달 ni bir xil aytish.</p>
  <p class="pe-good">딸 = tomoq tarang ("qiz"), 달 = tomoq boʻsh ("oy"). Oʻzbekcha
     <em>ikki</em> dagi keskinlikni eslang.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">ㄲ ni yangi, mustaqil harf deb yodlash.</p>
  <p class="pe-good">Bu shunchaki <b>ㄱ ikki marta</b>. Yangi shakl yoʻq — yangi faqat
     tomoqning holati.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     ㅂ ning nafasli va qattiq juftlarini yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Nafasli — <strong>ㅍ</strong>, qattiq —
    <strong>ㅃ</strong>. Uchlik: ㅂ (oddiy) · ㅍ (nafas koʻp) · ㅃ (nafas yoʻq, tomoq
    tarang).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Qaysi undoshning nafasli jufti yoʻq?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>ㅅ</strong>. Uning faqat qattiq jufti bor —
    <b>ㅆ</b>. Shuning uchun koreys tilida 19 ta undosh: 14 asosiy + 5 qattiq.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>딸</b>, <b>탈</b>, <b>달</b> — qaysi biri "qiz" degani?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>딸</strong> — qattiq ㄸ bilan. 탈 = "niqob"
    (nafasli), 달 = "oy" (oddiy). Uchalasining farqi faqat birinchi undoshda.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Nega <b>아까</b> hech qachon [aga] deb oʻqilmaydi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki <strong>qattiq undosh jaranglashmaydi</strong>.
    PK-4 dagi "unlilar orasida ㄱ → g" qoidasi faqat <em>oddiy</em> undoshlarga tegishli.
    아까 har doim <b>[akka]</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bekzod <b>오빠</b> ni "opa" deb aytdi va koreys doʻsti tushunmadi. Nega?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Bekzod <strong>ㅃ oʻrniga oddiy ㅂ</strong> aytdi va
    tomogʻini taranglashtirmadi. 오빠 [oppa] — "aka", 오바 esa boshqa narsa. Qattiq
    undoshda tovush keskin va quruq boʻlishi kerak — oʻzbekcha <em>akka</em> dagi
    kabi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>아빠</b><span>dada</span></li>
  <li><b>오빠</b><span>aka (qiz bola uchun)</span></li>
  <li><b>딸</b><span>qiz (farzand)</span></li>
  <li><b>꽃</b><span>gul</span></li>
  <li><b>빵</b><span>non</span></li>
  <li><b>싸다</b><span>arzon boʻlmoq</span></li>
  <li><b>짜다</b><span>sho'r boʻlmoq</span></li>
  <li><b>또</b><span>yana</span></li>
  <li><b>꿈</b><span>tush, orzu</span></li>
  <li><b>때</b><span>vaqt, payt</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li>Koreys undoshi <b>uch qatorli</b>: oddiy (ㄷ) · nafasli (ㅌ) · qattiq (ㄸ).</li>
    <li>Qattiq undosh — harfning <b>ikki marta yozilgani</b>, yangi shakl emas.</li>
    <li>Aytishda <b>nafas yoʻq, tomoq tarang</b>. Qogʻoz umuman qimirlamaydi.</li>
    <li>Oʻzbekcha <em>ikki</em>, <em>akka</em> dagi ikkilangan undosh — aynan shu
        tovush.</li>
    <li>Qattiq undosh <b>hech qachon jaranglashmaydi</b>: 아까 = [akka].</li>
    <li>ㅅ ning nafasli jufti yoʻq — faqat ㅆ. Jami 19 ta undosh.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-7: Boʻgʻin bloklari va 받침 (batchim)",
        "category": "korean",
        "order": 7,
        "summary": (
            "Boʻgʻin blokining toʻrt shakli va koreys talaffuzidagi eng muhim qoida: "
            "받침 oʻrnida qancha harf turmasin, faqat 7 xil tovush eshitiladi."
        ),
        "content": """
<h2>PK-7: Boʻgʻin bloklari va 받침 (batchim)</h2>

<p>Uchta soʻzni yozib qoʻying: <b>옷</b> (kiyim), <b>낮</b> (kunduz), <b>꽃</b> (gul).
Oxirgi harflari uch xil — ㅅ, ㅈ, ㅊ. Endi ularni ovoz chiqarib oʻqing: <b>[옫]</b>,
<b>[낟]</b>, <b>[꼳]</b> — uchalasi ham <em>bir xil</em> tugaydi. Bu xato emas va
istisno ham emas: koreys tilida <b>받침 oʻrnida faqat yettita tovush bor</b>. Bugun shu
qoidani oʻrganamiz — Hangul talaffuzidagi eng muhim narsa shu.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Boʻgʻin blokining toʻrtta shaklini koʻrasiz</li>
    <li>받침 nima va u qanday yoziladi — bittalik va qoʻshaloq</li>
    <li>Yetti tovush qoidasini oʻrganasiz: 27 ta harf → 7 ta tovush</li>
    <li>받침ni "portlatmasdan" aytishni mashq qilasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">받침 tovushlari</span>
  <span class="pe-chip pe-chip--v">ㄱ</span>
  <span class="pe-chip pe-chip--v">ㄴ</span>
  <span class="pe-chip pe-chip--v">ㄷ</span>
  <span class="pe-chip pe-chip--v">ㄹ</span>
  <span class="pe-chip pe-chip--v">ㅁ</span>
  <span class="pe-chip pe-chip--v">ㅂ</span>
  <span class="pe-chip pe-chip--v">ㅇ</span>
  <span class="pe-chip pe-chip--opt">boshqasi yoʻq</span>
</div>

<h3>1. Blokning toʻrtta shakli</h3>

<p>PK-1 da ikkitasini koʻrgan edingiz. 받침 qoʻshilsa, toʻrttaga chiqadi:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>Undosh + tik unli</p>
    <p><em>가 · 너 · 시 · 피</em> — unli oʻngda.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>Undosh + yotiq unli</p>
    <p><em>고 · 무 · 그 · 쿠</em> — unli tagida.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>Shakl 1 + 받침</p>
    <p><em>간 · 물 · 십 · 밥</em> — 받침 eng pastda.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">4</span>Shakl 2 + 받침</p>
    <p><em>곰 · 국 · 문 · 손</em> — 받침 yana eng pastda.</p></div>
</div>

<div class="pk-block">
  <span class="pk-block__cell pk-block__cell--i">ㅁ<small>초성</small></span>
  <span class="pk-block__cell pk-block__cell--m">ㅜ<small>중성</small></span>
  <span class="pk-block__cell pk-block__cell--f">ㄴ<small>종성</small></span>
  <span class="pk-block__eq">=</span>
  <span class="pk-block__out">문</span>
</div>

<p><b>받침</b> soʻzining oʻzi "tayanch, ostidan tutib turuvchi" degani — blokni pastdan
koʻtarib turgan harf. Rasmiy nomi <b>종성</b>.</p>

<h3>2. Qoʻshaloq 받침 (겹받침)</h3>

<p>Ba'zan pastda <em>ikkita</em> harf turadi: <b>값</b> (narx), <b>앉다</b> (oʻtirmoq),
<b>읽다</b> (oʻqimoq), <b>없다</b> (yoʻq boʻlmoq).</p>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Qoʻshaloq 받침da odatda <b>faqat bittasi</b> oʻqiladi: 값 → [갑], 없다 → [업따],
읽다 → [익따], 앉다 → [안따]. Ikkalasini ham aytmang.</div>

<p>Qaysi biri oʻqilishi soʻzga qarab oʻzgaradi va bu ilgʻorroq mavzu — hozircha shuni
bilib qoʻying: <b>koʻrsangiz, bittasini tanlang</b>. Har bir yangi soʻzda qaysi biri
oʻqilishini alohida eslab qolasiz.</p>

<h3>3. Yetti tovush qoidasi</h3>

<p>Mana darsning yuragi. 받침 oʻrnida 27 xil harf turishi mumkin, lekin ular
<b>faqat 7 xil tovush</b> beradi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Yozilishi mumkin</th><th>Oʻqiladi</th><th>Misol</th></tr>
  <tr><td class="pk-stem">ㄱ ㅋ ㄲ</td><td class="pk-end">[ㄱ]</td>
      <td class="pk-uz">밖 → [박], 부엌 → [부억]</td></tr>
  <tr><td class="pk-stem">ㄴ</td><td class="pk-end">[ㄴ]</td>
      <td class="pk-uz">눈 → [눈]</td></tr>
  <tr><td class="pk-stem">ㄷ ㅌ ㅅ ㅆ ㅈ ㅊ ㅎ</td><td class="pk-end">[ㄷ]</td>
      <td class="pk-uz">옷 → [옫], 낮 → [낟], 꽃 → [꼳]</td></tr>
  <tr><td class="pk-stem">ㄹ</td><td class="pk-end">[ㄹ]</td>
      <td class="pk-uz">물 → [물]</td></tr>
  <tr><td class="pk-stem">ㅁ</td><td class="pk-end">[ㅁ]</td>
      <td class="pk-uz">밤 → [밤]</td></tr>
  <tr><td class="pk-stem">ㅂ ㅍ</td><td class="pk-end">[ㅂ]</td>
      <td class="pk-uz">앞 → [압], 밥 → [밥]</td></tr>
  <tr><td class="pk-stem">ㅇ</td><td class="pk-end">[ㅇ] "ng"</td>
      <td class="pk-uz">강 → [강]</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Nega shunday? Chunki 받침 <b>oxirigacha aytilmaydi</b> — ogʻiz tovushni boshlaydi-yu,
uni chiqarmay toʻxtaydi. Toʻxtatilgan ㅅ, ㅈ, ㅊ, ㅌ — hammasi bir xil eshitiladi,
chunki farq aynan <em>chiqarishda</em> edi. Yozuv esa soʻzning asl shaklini saqlaydi:
꽃 hamisha ㅊ bilan yoziladi, chunki 꽃이 ("gul + qoʻshimcha") da u yana
[꼬치] boʻlib tiriladi.</div>

<h3>4. 받침ni "portlatmang"</h3>

<p>Oʻzbekcha "kitob" deganda oxirgi <em>b</em> ni chiqarib aytamiz — lab ochiladi, ozgina
havo chiqadi. Koreyschada esa <b>lab yopiq qoladi</b>.</p>

<ol class="pe-steps">
  <li><b>밥</b> ("guruch, ovqat") deng — lablarni yumib, shu holatda toʻxtang.</li>
  <li>Oxirida "pı" degan qoʻshimcha tovush chiqmasin.</li>
  <li>Xuddi shunday: <b>국</b> da til tanglayda qoladi, <b>옷</b> da til tishda qoladi.</li>
</ol>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Bu eng koʻp sezilib turadigan "chet ellik talaffuzi" belgisi. 한국 ni "hanguku" deb
aytmang — oxirgi ㄱ da til tanglayga tegib, shu yerda <b>toʻxtaydi</b>.</div>

<h3>5. 받침 tirilib qoladigan joy</h3>

<p>받침 doim jim turmaydi. Agar keyingi boʻgʻin <b>ㅇ bilan</b> boshlansa (ya'ni unli
bilan), 받침 oʻsha yoqqa <b>koʻchib oʻtadi</b> va toʻliq oʻz tovushi bilan aytiladi:</p>

<div class="pk-say">
  <span class="pk-say__from">꽃</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[꼳]</span>
  <span class="pk-say__why">yolgʻiz turganda — toʻxtaydi</span>
</div>

<div class="pk-say">
  <span class="pk-say__from">꽃이</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[꼬치]</span>
  <span class="pk-say__why">unli kelsa — ㅊ tiriladi va koʻchadi</span>
</div>

<p>Bu hodisa <b>연음화</b> deb ataladi va PK-8 ning asosiy mavzusi. Hozircha shuni koʻrib
qoʻying: 받침 yoʻqolmaydi, u faqat <em>kutadi</em>.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">옷 ni [os] deb oʻqish.</p>
  <p class="pe-good">받침 holatidagi ㅅ toʻxtaydi: <b>[옫]</b>. "s" tovushi
     chiqmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">한국 ni "han-gu-ku" deb, oxiriga unli qoʻshib aytish.</p>
  <p class="pe-good">Oxirgi ㄱ <b>portlatilmaydi</b>: <b>[한국]</b>, til tanglayda
     toʻxtaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">값 ni "kaps" deb, ikkala harfni ham aytish.</p>
  <p class="pe-good">Qoʻshaloq 받침da odatda bittasi oʻqiladi: <b>[갑]</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">꽃 ni ㅅ bilan yozish, chunki [꼳] deb eshitiladi.</p>
  <p class="pe-good">Talaffuz [꼳] boʻlsa ham, <b>imlo ㅊ bilan</b>: 꽃. 꽃이 =
     [꼬치] shuni isbotlaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     받침 oʻrnida nechta <em>tovush</em> boʻlishi mumkin? Ularni sanang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Yettita: ㄱ, ㄴ, ㄷ, ㄹ, ㅁ, ㅂ, ㅇ.</strong>
    Yozilishi mumkin boʻlgan harf esa 27 ta — lekin ular shu yettitaga
    yigʻiladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>앞</b> qanday oʻqiladi va nega?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>[압]</strong>. 받침 holatidagi <b>ㅍ → [ㅂ]</b>
    ga aylanadi, chunki toʻxtatilgan tovushda nafas farqi eshitilmay qoladi. Maʼnosi —
    "old, oldi".</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>옷</b>, <b>낮</b>, <b>꽃</b> — nega uchalasi bir xil tugaydi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki <strong>ㅅ, ㅈ, ㅊ ning uchalasi ham 받침da
    [ㄷ] boʻladi</strong>: [옫], [낟], [꼳]. Ularning farqi tovushni <em>chiqarishda</em>
    edi, 받침 esa chiqarilmaydi — shuning uchun farq yoʻqoladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Agar 꽃 [꼳] deb oʻqilsa, nega uni 꼳 deb <em>yozmaymiz</em>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki koreys imlosi soʻzning <strong>asl shaklini
    saqlaydi</strong>. Unli qoʻshilishi bilan ㅊ tiriladi: <b>꽃이 → [꼬치]</b>. Agar
    꼳 deb yozilsa, bu bogʻlanish yoʻqolardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Sherbek <b>밥</b> ni "pabı" deb aytdi. Nimani tuzatish kerak?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>U <strong>받침ni portlatib yubordi</strong> — oxiriga
    ortiqcha unli qoʻshdi. Toʻgʻrisi: lablar <b>yumilgan holda toʻxtaydi</b>, hech qanday
    havo chiqmaydi — <b>[밥]</b>. Bu chet ellik talaffuzining eng sezilarli
    belgisi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>받침</b><span>boʻgʻin ostidagi undosh</span></li>
  <li><b>겹받침</b><span>qoʻshaloq 받침</span></li>
  <li><b>옷</b><span>kiyim</span></li>
  <li><b>꽃</b><span>gul</span></li>
  <li><b>밥</b><span>guruch, ovqat</span></li>
  <li><b>앞</b><span>old, oldi</span></li>
  <li><b>밖</b><span>tashqari</span></li>
  <li><b>값</b><span>narx</span></li>
  <li><b>문</b><span>eshik</span></li>
  <li><b>손</b><span>qoʻl</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li>받침 — blokning eng pastidagi undosh; bitta yoki qoʻshaloq boʻladi.</li>
    <li><b>Yetti tovush qoidasi</b>: 27 ta harf → faqat ㄱ, ㄴ, ㄷ, ㄹ, ㅁ, ㅂ, ㅇ.</li>
    <li>ㅅ ㅆ ㅈ ㅊ ㅌ ㅎ → hammasi <b>[ㄷ]</b>. ㅋ ㄲ → [ㄱ]. ㅍ → [ㅂ].</li>
    <li>받침 <b>portlatilmaydi</b> — ogʻiz tovushni boshlab, shu holatda toʻxtaydi.</li>
    <li>Qoʻshaloq 받침da odatda <b>bittasi</b> oʻqiladi: 값 → [갑].</li>
    <li>Imlo asl shaklni saqlaydi: 꽃 → [꼳], lekin 꽃이 → [꼬치].</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-8: Talaffuz qoidalari: 연음화, 격음화, 경음화, 비음화",
        "category": "korean",
        "order": 8,
        "summary": (
            "Nega 한국어 [한구거], 학교 [학꾜], 입니다 [임니다] deb oʻqiladi — toʻrtta "
            "qoida koreys talaffuzidagi deyarli barcha “gʻalatilikni” tushuntiradi."
        ),
        "content": """
<h2>PK-8: Talaffuz qoidalari: 연음화, 격음화, 경음화, 비음화</h2>

<p>Siz endi har qanday koreyscha soʻzni harflab oʻqiy olasiz. Lekin bir muammo bor:
<b>학교</b> yozilgan joyda koreys <b>[학꾜]</b> deydi, <b>입니다</b> yozilgan joyda
<b>[임니다]</b> deydi. Bu qoidasizlik emas. Toʻrtta oddiy qoida bor va ular deyarli
barcha farqni tushuntiradi. Bugun ularni oʻrganamiz — shundan keyin Hangul bloki
yopiladi va PK-9 dan haqiqiy koreys tili boshlanadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>연음화 — 받침ning keyingi boʻgʻinga koʻchishini oʻrganasiz</li>
    <li>격음화 — ㅎ bilan uchrashgan undoshning nafasliga aylanishini koʻrasiz</li>
    <li>경음화 — undoshning qattiqlashishini tushunasiz</li>
    <li>비음화 — 입니다 nega [임니다] boʻlishini bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Asosiy tamoyil</span>
  <span class="pe-chip pe-chip--s">imlo soʻzni saqlaydi</span>
  <span class="pe-op">≠</span>
  <span class="pe-chip pe-chip--v">talaffuz ogʻizga moslashadi</span>
</div>

<h3>1. 연음화 — 받침 koʻchadi</h3>

<p>Eng koʻp uchraydigan va eng foydali qoida. Agar keyingi boʻgʻin <b>ㅇ bilan</b>
boshlansa — ya'ni unli bilan — <b>받침 oʻsha boʻgʻinga koʻchib oʻtadi</b>:</p>

<div class="pk-say">
  <span class="pk-say__from">한국어</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[한구거]</span>
  <span class="pk-say__why">국 ning ㄱ si 어 ga koʻchdi</span>
</div>

<div class="pk-say">
  <span class="pk-say__from">음악</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[으막]</span>
  <span class="pk-say__why">음 ning ㅁ si 악 ga koʻchdi</span>
</div>

<div class="pk-say">
  <span class="pk-say__from">밥이</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[바비]</span>
  <span class="pk-say__why">qoʻshimcha qoʻshilganda ham shunday</span>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu siz uchun tabiiy narsa. Oʻzbekchada ham "kitob + im" deganda <em>b</em> keyingi
boʻgʻinga oʻtib ketadi: <em>ki-to-bim</em>. Koreysda ham xuddi shu — ogʻiz qulay yoʻlni
tanlaydi. Farq shundaki, <b>yozuvda bu koʻrinmaydi</b>.</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
연음화 grammatikani oʻrganishda juda muhim: har bir qoʻshimcha unli bilan boshlanadi
(이, 을, 에, 은…), demak <b>deyarli har gapda</b> ishlaydi. PK-12 dan boshlab buni har
kuni koʻrasiz.</div>

<h3>2. 격음화 — ㅎ nafas qoʻshadi</h3>

<p>ㅎ oddiy undosh bilan uchrashsa, ikkalasi birikib <b>nafasli undosh</b> beradi. Qaysi
tartibda turishi ahamiyatsiz:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Birikma</th><th>Natija</th><th>Misol</th></tr>
  <tr><td class="pk-stem">ㄱ + ㅎ</td><td class="pk-end">ㅋ</td>
      <td class="pk-uz">축하 → [추카] — tabrik</td></tr>
  <tr><td class="pk-stem">ㄷ + ㅎ</td><td class="pk-end">ㅌ</td>
      <td class="pk-uz">좋다 → [조타] — yaxshi</td></tr>
  <tr><td class="pk-stem">ㅂ + ㅎ</td><td class="pk-end">ㅍ</td>
      <td class="pk-uz">입학 → [이팍] — oʻqishga kirish</td></tr>
  <tr><td class="pk-stem">ㅈ + ㅎ</td><td class="pk-end">ㅊ</td>
      <td class="pk-uz">맞히다 → [마치다] — topmoq</td></tr>
  <tr><td class="pk-stem">ㄶ + ㄷ</td><td class="pk-end">ㅌ</td>
      <td class="pk-uz">많다 → [만타] — koʻp</td></tr>
</table></div>

<p>PK-5 dagi qoida esingizdami — "chiziq qoʻshsang, nafas qoʻshiladi"? Mana shu qoida
endi <em>talaffuzda</em> ham ishlaydi: ㅎ — nafasning oʻzi, u yonidagi undoshga
qoʻshiladi.</p>

<h3>3. 경음화 — undosh qattiqlashadi</h3>

<p>Toʻxtovchi 받침dan (ㄱ, ㄷ, ㅂ tovushlaridan) keyin kelgan oddiy undosh
<b>qattiq</b> boʻlib qoladi:</p>

<div class="pk-say">
  <span class="pk-say__from">학교</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[학꾜]</span>
  <span class="pk-say__why">받침 ㄱ dan keyin ㄱ → ㄲ</span>
</div>

<div class="pk-say">
  <span class="pk-say__from">먹다</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[먹따]</span>
  <span class="pk-say__why">받침 ㄱ dan keyin ㄷ → ㄸ</span>
</div>

<div class="pk-say">
  <span class="pk-say__from">입다</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[입따]</span>
  <span class="pk-say__why">받침 ㅂ dan keyin ㄷ → ㄸ</span>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Buni <b>yodlash shart emas</b> — ogʻiz oʻzi shunday qiladi. 받침da toʻxtagan tomoq hali
tarang, keyingi undosh shu tarang holatda chiqadi. 학교 ni [학교] deb aytishga urinib
koʻring — qiyin boʻladi.</div>

<h3>4. 비음화 — burun tovushiga aylanish</h3>

<p>Bu qoida eng "kutilmagan" koʻrinadi, lekin siz uni <em>har kuni</em> ishlatasiz.
Toʻxtovchi 받침dan keyin <b>ㄴ yoki ㅁ</b> kelsa, 받침 burun tovushiga aylanadi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>받침</th><th>Aylanadi</th><th>Misol</th></tr>
  <tr><td class="pk-stem">ㄱ</td><td class="pk-end">ㅇ</td>
      <td class="pk-uz">한국말 → [한궁말] — koreyscha</td></tr>
  <tr><td class="pk-stem">ㄷ</td><td class="pk-end">ㄴ</td>
      <td class="pk-uz">몇 명 → [면 명] — necha kishi</td></tr>
  <tr><td class="pk-stem">ㅂ</td><td class="pk-end">ㅁ</td>
      <td class="pk-uz">입니다 → [임니다] — …dir</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>입니다 → [임니다]</b> — buni hozirdanoq yodlang. Bu koreys tilidagi eng koʻp
ishlatiladigan shakl (PK-10 va PK-19 darslari butunlay shunga bagʻishlangan) va deyarli
har bir yangi oʻquvchi uni "ip-ni-da" deb aytadi. Toʻgʻrisi — <b>[im-ni-da]</b>.</div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 학생입니다.</p>
  <p class="pe-ex__rom">[저는 학쌩임니다]</p>
  <p class="pe-ex__uz">Men talabaman.</p>
  <p class="pe-ex__why">Bitta gapda ikkita qoida: 학생 → [학쌩] (경음화),
     입니다 → [임니다] (비음화).</p>
</div>

<h3>5. Yana ikkita kichik qoida</h3>

<p><b>ㅎ tushib qolishi.</b> Unlilar orasida qolgan ㅎ deyarli aytilmaydi:</p>

<div class="pk-say">
  <span class="pk-say__from">좋아요</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[조아요]</span>
  <span class="pk-say__why">ㅎ yoʻqoladi</span>
</div>

<p><b>유음화 — ㄴ va ㄹ uchrashganda</b> ikkalasi ham [ㄹ] boʻladi:</p>

<div class="pk-say">
  <span class="pk-say__from">신라</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[실라]</span>
  <span class="pk-say__why">ㄴ + ㄹ → ㄹㄹ</span>
</div>

<div class="pk-say">
  <span class="pk-say__from">설날</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[설랄]</span>
  <span class="pk-say__why">ㄹ + ㄴ → ㄹㄹ</span>
</div>

<h3>6. Nega imlo oʻzgarmaydi</h3>

<p>Savol tugʻilishi tabiiy: agar [임니다] deb aytilsa, nega 임니다 deb yozilmaydi?</p>

<p>Chunki koreys imlosi <b>maʼno boʻlaklarini saqlaydi</b>. 입 — bu 입니다 shaklining
oʻzagi, u boshqa shakllarda ham qatnashadi. Agar talaffuzga qarab yozilsa, bir soʻz oʻnta
koʻrinishda yozilardi va oʻqish qiyinlashardi. Shuning uchun: <b>yozuv barqaror,
talaffuz esa moslashuvchan</b>.</p>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada ham shunday: "ketdi" deb yozamiz, lekin tez gapirganda [ketti] deb aytamiz.
Yozuv soʻzning tuzilishini koʻrsatadi, talaffuz esa ogʻizga qulayini tanlaydi. Koreysda
bu farq shunchaki kattaroq va qoidalari aniqroq.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">입니다 ni "ip-ni-da" deb aytish.</p>
  <p class="pe-good">비음화: ㅂ + ㄴ → ㅁ. Toʻgʻrisi <b>[임니다]</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">한국어 ni "han-guk-eo" deb boʻgʻinlab aytish.</p>
  <p class="pe-good">연음화: 받침 koʻchadi — <b>[한구거]</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">학교 ni [학교] deb, yumshoq ㄱ bilan aytish.</p>
  <p class="pe-good">경음화: toʻxtovchi 받침dan keyin qattiqlashadi —
     <b>[학꾜]</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Talaffuzga qarab 임니다 deb yozish.</p>
  <p class="pe-good">Imlo hech qachon oʻzgarmaydi: <b>입니다</b>. Faqat oʻqilishi
     boshqacha.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>음악</b> qanday oʻqiladi va bu qaysi qoida?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>[으막] — 연음화</strong>. Keyingi boʻgʻin ㅇ
    bilan boshlangani uchun 음 ning 받침i (ㅁ) oʻsha yoqqa koʻchdi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>축하</b> nega [추카] boʻladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>격음화</strong>: 받침 ㄱ keyingi ㅎ bilan
    birikib <b>nafasli ㅋ</b> beradi. ㅎ — nafasning oʻzi, shuning uchun u yonidagi
    undoshga "yopishadi".</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>먹다</b> ni oʻqing va qaysi qoida ishlaganini ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>[먹따] — 경음화</strong>. Toʻxtovchi 받침 ㄱ dan
    keyin oddiy ㄷ qattiq ㄸ ga aylandi. Tomoq hali tarang boʻlgani uchun bu
    oʻz-oʻzidan sodir boʻladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>한국말</b> qanday oʻqiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>[한궁말]</strong> — 비음화. 받침 ㄱ dan keyin
    ㅁ kelgani uchun ㄱ burun tovushi <b>ㅇ</b> ga aylandi. Maʼnosi — "koreys
    tili".</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Afsona <b>저는 학생입니다</b> ni "cho-nin hak-seng ip-ni-da" deb oʻqidi. Ikkita
     xatoni toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchisi: <strong>학생 → [학쌩]</strong> — 받침 ㄱ dan
    keyin ㅅ qattiq ㅆ ga aylanadi (경음화). Ikkinchisi:
    <strong>입니다 → [임니다]</strong> — ㅂ dan keyin ㄴ kelgani uchun ㅂ burun tovushi
    ㅁ ga aylanadi (비음화). Toʻgʻrisi: <b>[저는 학쌩임니다]</b>.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>연음화</b><span>받침ning keyingi boʻgʻinga koʻchishi</span></li>
  <li><b>격음화</b><span>ㅎ bilan nafasliga aylanish</span></li>
  <li><b>경음화</b><span>qattiqlashish</span></li>
  <li><b>비음화</b><span>burun tovushiga aylanish</span></li>
  <li><b>유음화</b><span>ㄴ va ㄹ ning ㄹㄹ boʻlishi</span></li>
  <li><b>음악</b><span>musiqa</span></li>
  <li><b>학교</b><span>maktab</span></li>
  <li><b>학생</b><span>oʻquvchi, talaba</span></li>
  <li><b>축하</b><span>tabrik</span></li>
  <li><b>설날</b><span>Yangi yil (oy taqvimi boʻyicha)</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li><b>연음화</b>: keyingi boʻgʻin unli bilan boshlansa, 받침 koʻchadi —
        한국어 [한구거].</li>
    <li><b>격음화</b>: ㅎ yonidagi oddiy undoshni nafasliga aylantiradi —
        축하 [추카].</li>
    <li><b>경음화</b>: toʻxtovchi 받침dan keyin undosh qattiqlashadi —
        학교 [학꾜].</li>
    <li><b>비음화</b>: ㄴ/ㅁ oldidan 받침 burun tovushiga aylanadi —
        <b>입니다 [임니다]</b>.</li>
    <li>ㅎ unlilar orasida tushib qoladi: 좋아요 [조아요].</li>
    <li><b>Imlo hech qachon oʻzgarmaydi.</b> Yozuv soʻzni saqlaydi, talaffuz ogʻizga
        moslashadi.</li>
  </ul>
</div>
""",
    },
]
