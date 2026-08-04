# -*- coding: utf-8 -*-
"""Prime Korean — Block G, darslar 92–94.

92. 다면서요, 냐면서요 — eshitilgan gapni tasdiqlash
93. 다니, 라니 — hayrat va taajjub
94. (으)려니 하다 — oʻz-oʻzicha taxmin qilish

Oʻzbekcha kalitlar:
  -다면서요?     = "…emish-ku, rostmi?"      (eshitganini tekshirish)
  -다면서 왜…?   = "…deb aytgan edingiz-ku"  (taʼna)
  -다니!         = "…emish-a!"               (hayrat)
  -다니요!       = "nima deganingiz?!"        (eʼtiroz)
  (으)려니 하다  = "…deb oʻylab qoʻya qolmoq" (oʻz-oʻzicha taxmin)
  그러려니 하다  = "shunday ekan deb qoʻyaverish"

Uchala dars ham bitta ildizdan — **koʻchirma gap** (PK-60, 61, 62):
  -다고 하 + 면서  → -다면서   (PK-39 dagi 면서 shu yerda!)
  -다고 하 + 니    → -다니
Yaʼni oʻquvchi yangi qolip yodlamaydi, tanish blokning yangi
qoʻshilishini koʻradi. PK-92 ni PK-62 (대요/냬요/래요/재요) bilan
jadval qilib solishtirish SHART: 62 = eshitganini BOSHQAGA aytish,
92 = eshitganini EGASIDAN tekshirish. Bir xil toʻrtlik, ikki vazifa.

PK-94 esa 려 oilasini yopadi: PK-40 (으)려고 하다 = niyat,
PK-90 (으)려던 참 = niyat + ayni payt, PK-94 (으)려니 하다 = TAXMIN.
Bitta harf, uch xil ish — buni ochiq aytmasak, oʻquvchi adashadi.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_92_94.py --author=prime
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
    # PK-92
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-92: 다면서요, 냐면서요 — eshitilgan gapni tasdiqlash",
        "category": "korean",
        "order": 92,
        "summary": (
            "“Koreyaga borarkansiz-a?” — eshitgan gapingizni uning "
            "egasidan tekshirish. PK-62 dagi toʻrtlikning ikkinchi "
            "yuzi, va taʼna aytishning eng koreyscha yoʻli."
        ),
        "stories": ["열 사람을 지나면"],
        "content": """
<h2>PK-92: 다면서요, 냐면서요 — eshitilgan gapni tasdiqlash</h2>

<p>Doʻstingizdan eshitdingiz: Jasur kelasi oy Koreyaga ketarkan.
Ertasi kuni Jasurning oʻzini koʻrib qoldingiz. Nima deysiz?
Oʻzbekchada bu juda tabiiy chiqadi: <em>“Koreyaga borarkansiz-a?”</em>
Yaʼni siz yangilik aytmayapsiz — <b>eshitganingizni tekshiryapsiz</b>.
Koreys tilida buning aniq qolipi bor.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>-다면서요?</b> bilan eshitgan gapingizni tasdiqlaysiz</li>
    <li>Toʻrtta shaklni oʻrganasiz: <b>다 · 냐 · 라 · 자</b> + 면서요</li>
    <li>Buni PK-62 dagi <b>대요/냬요/래요/재요</b> bilan yonma-yon
      qoʻyasiz</li>
    <li>Qolipning ikkinchi vazifasini — <b>taʼna</b> aytishni —
      koʻrasiz</li>
    <li>Nega bu qolipni oʻzingiz haqingizda ishlata olmasligingizni
      bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--v">koʻchirma shakl</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">면서요?</span>
  <span class="pe-chip pe-chip--adv">= …emish-ku, rostmi?</span>
</div>

<h3>1. Qolip qayerdan kelgan</h3>

<p>Yangi narsa deyarli yoʻq. PK-60 va PK-61 da koʻchirma gapni,
PK-39 da esa <b>(으)면서</b> (“…b turib”) ni oʻrgangansiz. Ikkalasi
qoʻshilib qisqargan:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Toʻliq shakl</th><th>Qisqarishi</th><th>Natija</th></tr>
  <tr><td class="pk-stem">간다고 하면서</td><td class="pk-end">하 tushadi</td>
      <td class="pk-res">간다면서</td></tr>
  <tr><td class="pk-stem">먹는다고 하면서</td><td class="pk-end">하 tushadi</td>
      <td class="pk-res">먹는다면서</td></tr>
  <tr><td class="pk-stem">학생이라고 하면서</td><td class="pk-end">하 tushadi</td>
      <td class="pk-res">학생이라면서</td></tr>
</table></div>

<p>Oxiriga <b>요</b> qoʻshsangiz — hurmat shakli, va gap
<em>soʻroq</em> boʻlib qoladi: <b>간다면서요?</b></p>

<h3>2. Toʻrtta shakl — PK-62 bilan yonma-yon</h3>

<p>PK-62 da eshitganingizni <em>boshqa odamga</em> aytishni
oʻrgandingiz. Bugun xuddi shu toʻrtlik, lekin ikkinchi vazifada:
eshitganingizni <em>gapning egasidan</em> tekshirasiz.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Turi</th><th>PK-62 — boshqaga aytish</th>
      <th>PK-92 — egasidan soʻrash</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pk-stem">darak</td><td class="pk-end">간대요</td>
      <td class="pk-res">간다면서요?</td>
      <td class="pk-uz">borarkansiz-a?</td></tr>
  <tr><td class="pk-stem">soʻroq</td><td class="pk-end">가냬요</td>
      <td class="pk-res">가냐면서요?</td>
      <td class="pk-uz">“borasanmi” deb soʻragan ekansiz-a?</td></tr>
  <tr><td class="pk-stem">buyruq</td><td class="pk-end">가래요</td>
      <td class="pk-res">가라면서요?</td>
      <td class="pk-uz">“bor” degan ekansiz-a?</td></tr>
  <tr><td class="pk-stem">taklif</td><td class="pk-end">가재요</td>
      <td class="pk-res">가자면서요?</td>
      <td class="pk-uz">“boraylik” degan ekansiz-a?</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Butun farq — kimga qarab turganingizda.</b><br>
  <b>대요</b> — men uchinchi odamga xabar beryapman.<br>
  <b>다면서요?</b> — men <em>gapning egasiga</em> qarab, uni
  tekshiryapman.<br>
  Shuning uchun 다면서요 deyarli doim <b>siz/sen</b> haqida.</p>
</div>

<h3>3. Shakllar jadvali</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Nima bilan</th><th>Shakl</th><th>Misol</th></tr>
  <tr><td class="pk-stem">feʼl, 받침 yoʻq</td>
      <td class="pk-end">ㄴ다면서요</td>
      <td class="pk-res">한국에 <b>간다면서요</b>?</td></tr>
  <tr><td class="pk-stem">feʼl, 받침 bor</td>
      <td class="pk-end">는다면서요</td>
      <td class="pk-res">매일 <b>읽는다면서요</b>?</td></tr>
  <tr><td class="pk-stem">sifat</td>
      <td class="pk-end">다면서요</td>
      <td class="pk-res">시험이 <b>어렵다면서요</b>?</td></tr>
  <tr><td class="pk-stem">oʻtgan zamon</td>
      <td class="pk-end">았/었다면서요</td>
      <td class="pk-res">어제 <b>갔다면서요</b>?</td></tr>
  <tr><td class="pk-stem">ot</td>
      <td class="pk-end">(이)라면서요</td>
      <td class="pk-res">의사<b>라면서요</b>?</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Bu — PK-62 dagi jadvalning aynan oʻzi.</b> Feʼl hozirgi
  zamonda 받침 ga qarab <b>ㄴ다 / 는다</b> ga boʻlinadi, sifat
  oddiy <b>다</b> oladi, ot esa <b>(이)라</b>. Bir marta oʻrganilgan
  bu tarmoq koʻchirma gapning hamma qoliplarida takrorlanadi —
  shuning uchun 92 va 93 sizga oson keladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">다음 달에 한국에
     <span class="pe-hl pe-hl--v">간다면서요</span>? 축하해요!</p>
  <p class="pe-ex__uz">Kelasi oy Koreyaga borarkansiz-a? Tabriklayman!</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">그 식당 음식이 정말
     <span class="pe-hl pe-hl--v">맛있다면서요</span>?</p>
  <p class="pe-ex__uz">Oʻsha oshxonaning ovqati juda mazali
  ekan-a?</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">어제 시험을 <span class="pe-hl pe-hl--v">봤다면서요</span>?
     어땠어요?</p>
  <p class="pe-ex__uz">Kecha imtihon topshiribsiz-a? Qanday oʻtdi?</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida bu — “-ekan” va “-ibdi”.</b>
  “Borar<b>kan</b>siz-a?”, “Imtihon topshir<b>ibsiz</b>-a?” —
  ikkala tilda ham gapning ichida <em>“men buni oʻzim koʻrmadim,
  eshitdim”</em> degan maʼno bor. Bu — oʻzbek oʻquvchisi uchun katta
  yordam: ingliz tilida bunday shakl yoʻq, shuning uchun ingliz
  oʻquvchisi 다면서요 ni uzoq oʻrganadi. Sizga esa faqat qaysi
  koreyscha shakl qaysi oʻzbekcha qoʻshimchaga toʻgʻri kelishini
  eslab qolish qoladi.</p>
</div>

<h3>4. Ikkinchi vazifasi: taʼna</h3>

<p>Endi eng qiziq joyi. Agar eshitgan gapingiz <em>bajarilmagan</em>
boʻlsa, xuddi shu qolip taʼnaga aylanadi. Bunda u gap oxirida emas,
<b>gap oʻrtasida</b> turadi va ketidan savol keladi.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">공부한다면서 왜 게임을 해요?</p>
  <p class="pe-ex__uz">Oʻqiyman deb aytgan edingiz-ku, nega oʻyin
  oʻynayapsiz?</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">일찍 온다면서 왜 이렇게 늦었어요?</p>
  <p class="pe-ex__uz">Erta kelaman degan edingiz-ku, nega bunchalik
  kechikdingiz?</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Ohangga eʼtibor bering.</b> Bu ikkinchi maʼnoda qolip
  <em>yoqimli emas</em> — u yumshoq taʼna. Ustozga yoki oʻzingizdan
  kattaga qarata ishlatmang. Doʻstlar orasida esa juda tabiiy.</p>
</div>

<h3>5. Qisqargan shakl: 다며(요)</h3>

<p>Nutqda <b>면서</b> koʻpincha <b>며</b> ga qisqaradi. Maʼnosi
oʻzgarmaydi:</p>

<div class="pk-level">
  <div class="pk-level__row pk-level__row--1">
    <span class="pk-level__name">반말</span>
    <span class="pk-level__ko">간다며?</span>
    <span class="pk-level__who">yaqin doʻst</span>
  </div>
  <div class="pk-level__row pk-level__row--3">
    <span class="pk-level__name">해요체</span>
    <span class="pk-level__ko">간다면서요? / 간다며요?</span>
    <span class="pk-level__who">kundalik hurmat</span>
  </div>
</div>

<h3>6. Kim haqida gapira olamiz?</h3>

<p>Qolip “men buni <em>sizdan</em> eshitgan edim, rostmi?” degani.
Demak:</p>

<div class="pe-steps">
  <p><b>Ha</b> — suhbatdosh haqida: 간다면서요?</p>
  <p><b>Ha</b> — uchinchi shaxs haqida, agar suhbatdosh bilsa:
  민수가 간다면서요?</p>
  <p><b>Yoʻq</b> — <em>oʻzim</em> haqimda. ❌ 제가 간다면서요.
  Oʻz niyatimni men eshitmayman — bilaman.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>제가 다음 달에 간다면서요.</s></p>
  <p class="pe-good">저는 다음 달에 <b>가요</b>. / 간<b>대요</b>?</p>
  <p><small>Oʻz rejangizni eshitib bilmaysiz. Qolip faqat
  <em>boshqadan</em> eshitilgan gap uchun.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>한국에 가다면서요?</s></p>
  <p class="pe-good">한국에 <b>간다면서요</b>?</p>
  <p><small>Feʼl hozirgi zamonda <b>ㄴ다/는다</b> oladi — xuddi
  PK-60 dagidek. 가다 → 간다 → 간다면서요.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>시험이 어렵는다면서요?</s></p>
  <p class="pe-good">시험이 <b>어렵다면서요</b>?</p>
  <p><small>어렵다 — <b>sifat</b>. Sifat 는다 olmaydi, oddiy
  <b>다</b> qoʻshiladi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>의사이라면서요?</s></p>
  <p class="pe-good">의사<b>라면서요</b>?</p>
  <p><small>의사 da 받침 yoʻq → <b>라면서요</b>. 받침 bor boʻlsa:
  학생<b>이라면서요</b>?</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 다음 달에 한국에
  <span class="pe-blank"></span>? (가다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>간다면서요</b> — feʼl, 받침 yoʻq → ㄴ다면서요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 시험이 정말
  <span class="pe-blank"></span>? (어렵다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>어렵다면서요</b> — sifat, oddiy 다면서요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Toʻldiring: 그분이
  <span class="pe-blank"></span>? (의사)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>의사라면서요</b> — ot, 받침 yoʻq → 라면서요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> 간대요 va 간다면서요 farqi
  nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>간대요</b> — uchinchi odamga xabar beraman.
    <b>간다면서요?</b> — gapning <b>egasiga</b> qarab tekshiraman.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Bu gapning maʼnosi nima?<br>
  <b>공부한다면서 왜 게임을 해요?</b></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>“Oʻqiyman <b>deb aytgan edingiz-ku</b>, nega oʻyin
    oʻynayapsiz?” — qolipning taʼna maʼnosi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Nega
  <s>제가 간다면서요</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Qolip <b>eshitilgan</b> gapni tekshiradi. Oʻz niyatimni men
    eshitmayman — bilaman.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">7</span> 다면서요 ning qisqargan
  shakli qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>다며요</b> (hurmat) · <b>다며</b> (반말). Maʼnosi
    oʻzgarmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">8</span> Koreyschaga oʻgiring:
  “Kecha imtihon topshiribsiz-a? Qanday oʻtdi?”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>어제 시험을 봤다면서요? 어땠어요?</b></p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>-다면서요?</b> — …emish-ku, rostmi?</li>
  <li><b>-냐면서요?</b> — “…mi” deb soʻragan ekansiz-a?</li>
  <li><b>-라면서요?</b> — “…” deb buyurgan ekansiz-a?</li>
  <li><b>-자면서요?</b> — “…aylik” degan ekansiz-a?</li>
  <li><b>소문</b> — mish-mish, ovoza</li>
  <li><b>듣다</b> — eshitmoq</li>
  <li><b>확인하다</b> — tasdiqlamoq, tekshirmoq</li>
  <li><b>축하하다</b> — tabriklamoq</li>
  <li><b>사실</b> — haqiqat, rost</li>
  <li><b>퍼지다</b> — tarqalmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>-다면서요?</b> = eshitgan gapni <em>egasidan</em>
      tekshirish.</li>
    <li>Kelib chiqishi: <b>-다고 하 + 면서</b> → <b>-다면서</b>.</li>
    <li>Toʻrtlik: <b>다 · 냐 · 라 · 자</b> + 면서요 — PK-62 dagi
      대요/냬요/래요/재요 ning ikkinchi yuzi.</li>
    <li>Feʼl → <b>ㄴ다/는다면서요</b> · sifat → <b>다면서요</b> ·
      ot → <b>(이)라면서요</b>.</li>
    <li>Gap oʻrtasida kelsa — <b>taʼna</b>: 공부한다면서 왜
      게임을 해요?</li>
    <li>Qisqargan shakli: <b>다며(요)</b>.</li>
    <li>❌ Oʻzingiz haqingizda ishlatilmaydi.</li>
    <li>Oʻzbekcha juftligi: “<b>-ekan / -ibdi</b> + -a?”.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-93
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-93: 다니, 라니 — hayrat va taajjub",
        "category": "korean",
        "order": 93,
        "summary": (
            "“Allaqachon qish boʻlibdi-ya!” — eshitgan yoki bilib "
            "qolgan narsangizga hayron qolish. Koʻchirma gapdan "
            "tugʻilgan eng hissiyotli qolip."
        ),
        "stories": ["어머니의 공책"],
        "content": """
<h2>PK-93: 다니, 라니 — hayrat va taajjub</h2>

<p>Kalendarga qaraysiz — dekabr. <em>“Voy, allaqachon qish
boʻlibdi-ya!”</em> Yoki doʻstingiz aytadi: “Men oʻsha imtihondan
oʻtdim.” Siz: <em>“Oʻtibsan-a! Ishonolmayapman.”</em></p>

<p>Bu — yangilik aytish emas. Bu — <b>hayrat</b>. Koreys tilida
uning oʻz qolipi bor, va u kechagi darsning yaqin qarindoshi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>-다니 / -라니</b> bilan hayratni bildirasiz</li>
    <li>Uni gap oxirida ham, gap oʻrtasida ham ishlatasiz</li>
    <li><b>-다니요!</b> bilan eʼtiroz bildirishni oʻrganasiz</li>
    <li>PK-92 dagi <b>-다면서요?</b> dan farqini koʻrasiz</li>
    <li>Oʻzbekcha <b>“-ibdi-ya!”</b> bilan juftlaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--v">koʻchirma shakl</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">니</span>
  <span class="pe-chip pe-chip--adv">= …emish-a! …ekan-a!</span>
</div>

<h3>1. Yana oʻsha ildiz</h3>

<p>Kecha <b>-다고 하 + 면서</b> ni koʻrdingiz. Bugun xuddi shu
joyga boshqa qoʻshimcha keladi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Toʻliq shakl</th><th>Qisqarishi</th><th>Natija</th></tr>
  <tr><td class="pk-stem">끝났다고 하니</td><td class="pk-end">하 tushadi</td>
      <td class="pk-res">끝났다니</td></tr>
  <tr><td class="pk-stem">춥다고 하니</td><td class="pk-end">하 tushadi</td>
      <td class="pk-res">춥다니</td></tr>
  <tr><td class="pk-stem">겨울이라고 하니</td><td class="pk-end">하 tushadi</td>
      <td class="pk-res">겨울이라니</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Uch dars, bitta ildiz:</b><br>
  <b>-다고 하다</b> (PK-60) → xabar berish<br>
  <b>-다면서요?</b> (PK-92) → tekshirish<br>
  <b>-다니!</b> (PK-93) → hayron qolish<br>
  Koʻchirma gapni bir marta yaxshi oʻrgansangiz, butun bir oila
  qolip oʻz-oʻzidan ochiladi.</p>
</div>

<h3>2. Shakllar</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Nima bilan</th><th>Shakl</th><th>Misol</th>
      <th>Maʼnosi</th></tr>
  <tr><td class="pk-stem">feʼl, 받침 yoʻq</td><td class="pk-end">ㄴ다니</td>
      <td class="pk-res">간다니</td><td class="pk-uz">borarkan-a</td></tr>
  <tr><td class="pk-stem">feʼl, 받침 bor</td><td class="pk-end">는다니</td>
      <td class="pk-res">먹는다니</td><td class="pk-uz">yer ekan-a</td></tr>
  <tr><td class="pk-stem">sifat</td><td class="pk-end">다니</td>
      <td class="pk-res">춥다니</td><td class="pk-uz">sovuq ekan-a</td></tr>
  <tr><td class="pk-stem">oʻtgan zamon</td><td class="pk-end">았/었다니</td>
      <td class="pk-res">끝났다니</td><td class="pk-uz">tugabdi-ya</td></tr>
  <tr><td class="pk-stem">ot</td><td class="pk-end">(이)라니</td>
      <td class="pk-res">겨울이라니</td><td class="pk-uz">qish boʻlibdi-ya</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha juftligi juda aniq: “-ibdi-ya!”, “-ekan-a!”</b><br>
  “Allaqachon tuga<b>bdi-ya</b>!” = <b>벌써 끝났다니!</b><br>
  “Qish boʻl<b>ibdi-ya</b>!” = <b>겨울이라니!</b><br>
  Oʻzbek tilida <b>-ibdi</b> qoʻshimchasi aynan shu ishni qiladi:
  “men buni oʻzim koʻrmagan edim, endi bilib hayron
  boʻlyapman”. Koreys tilida bu maʼno feʼlga emas,
  <em>koʻchirma gapga</em> yuklangan — lekin his bir xil.</p>
</div>

<h3>3. Ikkita oʻrni</h3>

<p><b>a) Gap oxirida — sof hayrat.</b> Ketidan hech narsa
kelmaydi, faqat undov.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">벌써 <span class="pe-hl pe-hl--v">겨울이라니</span>!</p>
  <p class="pe-ex__uz">Allaqachon qish boʻlibdi-ya!</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">이렇게 <span class="pe-hl pe-hl--v">어렵다니</span>!</p>
  <p class="pe-ex__uz">Shunchalik qiyin ekan-a!</p>
</div>

<p><b>b) Gap oʻrtasida — hayrat + izoh.</b> Ketidan his-tuygʻu
bildiruvchi kesim keladi: 기쁘다, 놀랍다, 슬프다, 믿을 수 없다…</p>

<div class="pe-ex">
  <p class="pe-ex__ko">그 사람이 <span class="pe-hl pe-hl--v">온다니</span>
     정말 기쁘다.</p>
  <p class="pe-ex__uz">U kelarkan — juda xursandman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">어머니가 쉰 살에 글자를
     <span class="pe-hl pe-hl--v">배웠다니</span> 믿을 수 없었다.</p>
  <p class="pe-ex__uz">Onam ellik yoshida harf oʻrganibdi — ishonib
  boʻlmasdi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Ikkinchi shakl yozma matnning qoliplaridan biri.</b>
  한다체 da yozilgan hikoyada qahramonning ichki hayratini
  koʻrsatishning eng qisqa yoʻli — <b>…다니 믿을 수 없었다</b>.
  Buni eslab qoling: TOPIK oʻqish matnlarida u tez-tez
  uchraydi.</p>
</div>

<h3>4. 다니요! — eʼtiroz</h3>

<p>Oxiriga <b>요</b> qoʻshsangiz, qolip boshqa ish qiladi: siz
suhbatdoshning gapini <em>qabul qilmaysiz</em>. Bu — hayratning
norozilikka aylangan shakli.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 이번 일은 민수 씨 잘못이에요.<br>
     나: <span class="pe-hl pe-hl--neg">제 잘못이라니요</span>?
     저는 그 자리에 없었어요.</p>
  <p class="pe-ex__uz">— Bu safargi ish Minsuning aybi.<br>
  — Mening aybim deganingiz nimasi? Men u yerda boʻlmaganman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 이제 그만두려고 해요.<br>
     나: <span class="pe-hl pe-hl--neg">그만두다니요</span>!
     거의 다 끝난 것이나 다름없어요.</p>
  <p class="pe-ex__uz">— Endi tashlamoqchiman.<br>
  — Tashlash deganingiz nimasi! Deyarli tugagan bilan
  barobar-ku.</p>
</div>

<h3>5. PK-92 bilan yonma-yon</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">-다면서요? <small>PK-92</small></p>
    <p><b>Savol.</b> Javob kutaman.</p>
    <p>Kimga qarab turibman? — <em>gapning egasiga</em>.</p>
    <p><small>한국에 <b>간다면서요</b>? (rostmi?)</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">-다니! <small>PK-93</small></p>
    <p><b>Undov.</b> Javob kutmayman.</p>
    <p>Kimga qarab turibman? — <em>hech kimga</em>, oʻzimga.</p>
    <p><small>한국에 <b>간다니</b>! (ishonolmayman!)</small></p>
  </div>
</div>

<div class="pe-call pe-warn">
  <p><b>Hayrat — ijobiy ham, salbiy ham boʻlishi mumkin.</b>
  <b>합격했다니 정말 기쁘다</b> (oʻtibsan — xursandman) va
  <b>벌써 갔다니 너무 아쉽다</b> (ketibdi — juda afsus). Qolip his
  turini belgilamaydi, faqat “<em>kutmagan edim</em>” deydi.
  Turini ketidagi soʻz aytadi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>벌써 겨울다니!</s></p>
  <p class="pe-good">벌써 겨울<b>이라니</b>!</p>
  <p><small>Ot bilan <b>(이)라니</b> ishlatiladi. 겨울 da 받침 bor
  → 이라니. 받침 yoʻq boʻlsa: 가수<b>라니</b>!</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>그 사람이 가다니 기쁘다.</s></p>
  <p class="pe-good">그 사람이 <b>간다니</b> 기쁘다.</p>
  <p><small>Feʼl hozirgi zamonda <b>ㄴ다/는다</b> oladi — koʻchirma
  gapning oʻsha tanish qoidasi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>시험이 어렵는다니!</s></p>
  <p class="pe-good">시험이 <b>어렵다니</b>!</p>
  <p><small>어렵다 — sifat. Sifat 는다 olmaydi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>한국에 간다니? 축하해요!</s></p>
  <p class="pe-good">한국에 <b>간다면서요</b>? 축하해요!</p>
  <p><small>Tasdiqlash — savol, demak <b>다면서요?</b> (PK-92).
  다니 javob kutmaydi.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 벌써
  <span class="pe-blank"></span>! (겨울)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>겨울이라니</b> — ot, 받침 bor → 이라니.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 이렇게
  <span class="pe-blank"></span>! (어렵다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>어렵다니</b> — sifat, oddiy 다니.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Toʻldiring: 그 사람이
  <span class="pe-blank"></span> 정말 기쁘다. (오다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>온다니</b> — feʼl, 받침 yoʻq → ㄴ다니.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Toʻldiring: 벌써
  <span class="pe-blank"></span> 믿을 수 없다. (끝나다, oʻtgan zamon)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>끝났다니</b> — 았/었다니.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> <b>다니</b> va
  <b>다면서요</b> farqi nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>다면서요?</b> — savol, javob kutaman.
    <b>다니!</b> — undov, javob kutmayman.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> <b>제 잘못이라니요?</b> —
  bu nimani bildiradi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>Eʼtiroz</b>: “Mening aybim deganingiz nimasi?” —
    suhbatdoshning gapini qabul qilmayapman.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">7</span> Bu qolip faqat yomon
  yangilik uchunmi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Yoʻq. U faqat “<b>kutmagan edim</b>” deydi.
    합격했다니 기쁘다 (ijobiy) · 벌써 갔다니 아쉽다 (salbiy).</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">8</span> Koreyschaga oʻgiring
  (한다체): “Onam ellik yoshida harf oʻrganibdi — ishonib
  boʻlmasdi.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>어머니가 쉰 살에 글자를 배웠다니 믿을 수 없었다.</b></p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>-다니</b> — …emish-a! …ekan-a!</li>
  <li><b>-(이)라니</b> — ot bilan shu maʼno</li>
  <li><b>-다니요!</b> — “deganingiz nimasi?!”</li>
  <li><b>벌써</b> — allaqachon</li>
  <li><b>놀랍다</b> — hayratlanarli</li>
  <li><b>아쉽다</b> — afsuslanarli</li>
  <li><b>믿다</b> — ishonmoq</li>
  <li><b>글자</b> — harf, yozuv</li>
  <li><b>공책</b> — daftar</li>
  <li><b>잘못</b> — ayb, xato</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>-다니 / -(이)라니</b> = hayrat, taajjub.</li>
    <li>Kelib chiqishi: <b>-다고 하 + 니</b> → <b>-다니</b>.</li>
    <li>Feʼl → <b>ㄴ다니/는다니</b> · sifat → <b>다니</b> ·
      oʻtgan → <b>았/었다니</b> · ot → <b>(이)라니</b>.</li>
    <li>Gap oxirida — sof undov. Gap oʻrtasida — hayrat +
      izoh (기쁘다, 믿을 수 없다…).</li>
    <li><b>-다니요!</b> — eʼtiroz, gapni qabul qilmaslik.</li>
    <li>Ijobiy ham, salbiy ham. Qolip faqat “kutmagan edim”
      deydi.</li>
    <li><b>다면서요?</b> savol · <b>다니!</b> undov.</li>
    <li>Oʻzbekcha juftligi: “<b>-ibdi-ya! -ekan-a!</b>”.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-94
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-94: (으)려니 하다 — oʻz-oʻzicha taxmin qilish",
        "category": "korean",
        "order": 94,
        "summary": (
            "“Shunchaki band ekan deb oʻylagandim” — tekshirmasdan, "
            "ichimizda qilingan taxmin. Va koreyslarning eng "
            "sevimli hayotiy maslahati: 그러려니 해."
        ),
        "stories": ["그러려니 하는 힘"],
        "content": """
<h2>PK-94: (으)려니 하다 — oʻz-oʻzicha taxmin qilish</h2>

<p>Doʻstingiz uch kun javob bermadi. Siz soʻramadingiz, xafa ham
boʻlmadingiz — shunchaki <em>“band ekan-da”</em> deb oʻylab
qoʻyaqoldingiz. Keyin maʼlum boʻldi: telefoni buzilgan ekan.</p>

<p>Mana shu — tekshirmasdan, ichimizda qilingan taxmin. Koreys
tilida uning qolipi bor, va u koreyslarning eng koʻp aytadigan
hayotiy maslahatining ichida yashaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)려니 하다</b> bilan “…deb oʻylab qoʻyaqoldim”
      deysiz</li>
    <li><b>그러려니 하다</b> iborasini oʻrganasiz</li>
    <li>Buni <b>(으)ㄹ 것 같다</b> (PK-52) dan ajratasiz</li>
    <li><b>려</b> oilasini yopasiz: niyat, payt va taxmin</li>
    <li>Nega bu qolip koʻpincha <em>xato</em> taxmin haqida
      ekanini koʻrasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--v">feʼl oʻzagi</span>
  <span class="pe-chip pe-chip--o">(으)려니</span>
  <span class="pe-chip pe-chip--s">하다 / 생각하다</span>
  <span class="pe-chip pe-chip--adv">= …deb oʻylab qoʻyaqolmoq</span>
</div>

<h3>1. Shakli</h3>

<div class="pk-batchim">
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">으려니 하다</span></p>
    <p>먹<b>으려니</b> · 늦<b>으려니</b> · 없<b>으려니</b></p>
  </div>
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">려니 하다</span></p>
    <p>바쁘<b>려니</b> · 오<b>려니</b> · 그러<b>려니</b></p>
  </div>
</div>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Asos</th><th>Shakl</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-stem">바쁘다</td><td class="pk-end">려니 했다</td>
      <td class="pk-res">바쁘려니 했다</td>
      <td class="pk-uz">band ekan-da deb oʻyladim</td></tr>
  <tr><td class="pk-stem">늦다</td><td class="pk-end">으려니 했다</td>
      <td class="pk-res">늦으려니 했다</td>
      <td class="pk-uz">kechikadi deb oʻyladim</td></tr>
  <tr><td class="pk-stem">그렇다</td><td class="pk-end">려니 하다</td>
      <td class="pk-res">그러려니 하다</td>
      <td class="pk-uz">shunday ekan deb qoʻyaverish</td></tr>
  <tr><td class="pk-stem">처음이다</td><td class="pk-end">려니 했다</td>
      <td class="pk-res">처음이려니 했다</td>
      <td class="pk-uz">birinchi marta ekan deb oʻyladim</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">답장이 없어서 그냥
     <span class="pe-hl pe-hl--v">바쁘려니 했다</span>.</p>
  <p class="pe-ex__uz">Javob boʻlmagani uchun shunchaki band ekan-da
  deb oʻylab qoʻyaqoldim.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">버스가 또 안 와서 오늘도
     <span class="pe-hl pe-hl--v">늦으려니 했다</span>.</p>
  <p class="pe-ex__uz">Avtobus yana kelmagani uchun bugun ham
  kechikaman deb oʻyladim.</p>
</div>

<h3>2. Qolipning ichidagi maʼno</h3>

<p>Bu shunchaki “oʻyladim” emas. Uning ichida uchta narsa bor:</p>

<div class="pe-steps">
  <p><b>1.</b> Taxmin <em>ichimda</em> qilingan — men buni hech
  kimga aytmadim.</p>
  <p><b>2.</b> Men uni <em>tekshirmadim</em> — soʻramadim,
  qaramadim.</p>
  <p><b>3.</b> Koʻpincha taxmin <em>notoʻgʻri</em> chiqadi — yoki
  ataylab tekshirmayman, chunki shunisi tinchroq.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Shuning uchun bu qolip deyarli doim oʻtgan zamonda —
  했다 shaklida — keladi.</b> Chunki hikoya qilayotgan odam
  allaqachon haqiqatni bilib boʻlgan: “<em>shunday deb oʻylagan
  edim… lekin</em>”. Keyingi jumla koʻpincha <b>그런데</b> yoki
  <b>알고 보니</b> (“bilsam…”) bilan boshlanadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">그냥 <span class="pe-hl pe-hl--v">바쁘려니 했다</span>.
     그런데 휴대폰이 고장 났었다.</p>
  <p class="pe-ex__uz">Shunchaki band ekan-da deb oʻylagandim. Bilsam,
  telefoni buzilgan ekan.</p>
  <p class="pe-ex__why">Bu — qolipning eng tipik ishlatilishi:
  taxmin + uning notoʻgʻri chiqishi.</p>
</div>

<h3>3. 그러려니 하다 — darsning eng muhim iborasi</h3>

<p><b>그렇다</b> (“shunday”) + 려니 하다 = <b>그러려니 하다</b>.
Maʼnosi: “<em>shunday ekan-da</em> deb qoʻyaverish”, yaʼni jahl
qilmaslik, tortishmaslik, qabul qilib qoʻya qolish.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">버스가 늦어도 <span class="pe-hl pe-hl--v">그러려니 한다</span>.</p>
  <p class="pe-ex__uz">Avtobus kechiksa ham, shunday ekan-da deb
  qoʻyaveraman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">세상일은 다
     <span class="pe-hl pe-hl--v">그러려니 해야 한다</span>.</p>
  <p class="pe-ex__uz">Dunyoning ishlariga shunday ekan-da deb
  qarash kerak.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu iboraning oʻzbekchasi bor, va u juda yaqin.</b>
  “<b>Shunday ekan-da</b>”, “<b>boʻlaveradi-da</b>”,
  “<b>koʻnglingizga olmang</b>”. Uzoq navbatda turganda, avtobus
  kechikkanda, notanish odam qoʻpol gapirganda — oʻzbek ham,
  koreys ham xuddi shu narsani aytadi. Farq shundaki, koreys tilida
  bu <em>bitta grammatik qolipga</em> siqilgan: <b>그러려니 해</b>.
  Ikki soʻz — butun bir hayotiy pozitsiya.</p>
</div>

<h3>4. (으)ㄹ 것 같다 bilan farqi</h3>

<p>Ikkalasi ham taxmin. Lekin ular boshqa-boshqa joyda yashaydi.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">(으)ㄹ 것 같다 <small>PK-52</small></p>
    <p><b>Ovoz chiqarib</b> aytiladigan taxmin. Dalilga
    asoslangan.</p>
    <p>Suhbatdosh eshitadi va javob berishi mumkin.</p>
    <p><small>비가 <b>올 것 같아요</b>. (osmonga qarab)</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">(으)려니 하다 <small>PK-94</small></p>
    <p><b>Ichimda</b> qilingan taxmin. Tekshirilmagan.</p>
    <p>Hech kim eshitmaydi — bu mening oʻz xulosam.</p>
    <p><small>그냥 <b>바쁘려니 했다</b>. (soʻramadim)</small></p>
  </div>
</div>

<div class="pe-call pe-warn">
  <p><b>Shuning uchun bu qolip suhbatda kam ishlatiladi.</b>
  Uni siz odamga qarab aytmaysiz — uni siz <em>hikoya
  qilasiz</em>. Kundalik gapda “menimcha…” demoqchi boʻlsangiz,
  <b>(으)ㄹ 것 같다</b> yoki <b>(으)ㄹ지도 모르다</b> (PK-73)
  ishlating.</p>
</div>

<h3>5. 려 oilasini yopamiz</h3>

<p>Kursda <b>려</b> uchta boshqa-boshqa qolipda uchradi. Ular
bir-biriga oʻxshaydi, lekin butunlay boshqa ish qiladi. Mana
hammasi bir joyda:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Qolip</th><th>Dars</th><th>Vazifasi</th><th>Misol</th></tr>
  <tr><td class="pk-stem">(으)려고 하다</td><td class="pk-end">PK-40</td>
      <td class="pk-uz">niyat</td><td class="pk-res">가려고 해요</td></tr>
  <tr><td class="pk-stem">(으)려던 참이다</td><td class="pk-end">PK-90</td>
      <td class="pk-uz">niyat + ayni payt</td>
      <td class="pk-res">가려던 참이었어요</td></tr>
  <tr><td class="pk-stem">(으)려니 하다</td><td class="pk-end">PK-94</td>
      <td class="pk-uz"><b>taxmin</b></td>
      <td class="pk-res">가려니 했어요</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Ajratuvchi belgi — ketidagi feʼl.</b><br>
  ketida <b>하다</b> va oldida <b>고</b> boʻlsa → niyat (려<b>고</b>
  하다).<br>
  ketida <b>참</b> boʻlsa → ayni payt.<br>
  ketida <b>니 하다</b> boʻlsa → taxmin.<br>
  Yaʼni 려 ning oʻzi hech narsa demaydi — maʼnoni undan
  <em>keyingi</em> qism beradi. Bu koreys grammatikasining
  umumiy qoidasi: eng muhim maʼno hamisha oxirida.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>내일 비가 오려니 해요.</s></p>
  <p class="pe-good">내일 비가 <b>올 것 같아요</b>.</p>
  <p><small>Suhbatdoshga aytilayotgan taxmin → <b>(으)ㄹ 것 같다</b>.
  려니 하다 — ichki, tekshirilmagan taxmin, va u odatda
  <em>oʻtgan zamonda</em> hikoya qilinadi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>그냥 바쁘려고 했다.</s></p>
  <p class="pe-good">그냥 <b>바쁘려니</b> 했다.</p>
  <p><small>려<b>고</b> 하다 = niyat. Lekin “band boʻlish” — niyat
  emas. Taxmin uchun <b>려니</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>늦려니 했다.</s></p>
  <p class="pe-good"><b>늦으려니</b> 했다.</p>
  <p><small>늦 da 받침 bor → <b>으려니</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>그렇려니 해.</s></p>
  <p class="pe-good"><b>그러려니</b> 해.</p>
  <p><small>그렇다 — ㅎ notoʻgʻri feʼli (PK-47). ㅎ tushadi:
  그렇 → 그러 + 려니.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 답장이 없어서 그냥
  <span class="pe-blank"></span> 했다. (바쁘다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>바쁘려니</b> — 받침 yoʻq → 려니.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 오늘도
  <span class="pe-blank"></span> 했다. (늦다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>늦으려니</b> — 받침 bor → 으려니.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> 그렇다 ni bu qolipga ulang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>그러려니 하다</b> — ㅎ notoʻgʻri feʼli (PK-47): ㅎ
    tushadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> <b>그러려니 해</b> nima
  degani?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>“<b>Shunday ekan-da deb qoʻyaver</b>” — jahl qilma,
    koʻnglingga olma.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Nega bu qolip deyarli doim
  <b>했다</b> shaklida keladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Chunki hikoya qiluvchi haqiqatni allaqachon biladi:
    “shunday deb <b>oʻylagan edim</b>… lekin”.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Qaysi biri toʻgʻri?<br>
  (a) 내일 비가 오려니 해요.<br>
  (b) 내일 비가 올 것 같아요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>(b)</b>. Suhbatdoshga aytilayotgan taxmin →
    <b>(으)ㄹ 것 같다</b> (PK-52).</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">7</span> 려고 하다 · 려던 참이다 ·
  려니 하다 — qaysi biri taxmin?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>려니 하다</b>. Birinchisi niyat (PK-40), ikkinchisi
    niyat + ayni payt (PK-90).</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">8</span> Koreyschaga oʻgiring
  (한다체): “Shunchaki band ekan-da deb oʻylagandim. Bilsam,
  telefoni buzilgan ekan.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>그냥 바쁘려니 했다. 그런데 휴대폰이 고장 났었다.</b></p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)려니 하다</b> — …deb oʻylab qoʻyaqolmoq</li>
  <li><b>그러려니 하다</b> — shunday ekan-da deb qoʻyaverish</li>
  <li><b>그냥</b> — shunchaki</li>
  <li><b>답장</b> — javob (xat, xabar)</li>
  <li><b>알고 보니</b> — bilsam, maʼlum boʻlishicha</li>
  <li><b>고장 나다</b> — buzilmoq</li>
  <li><b>세상일</b> — dunyoning ishlari</li>
  <li><b>참다</b> — chidamoq, sabr qilmoq</li>
  <li><b>여유</b> — xotirjamlik, keng koʻngillik</li>
  <li><b>짜증</b> — asabiylashish</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>(으)려니 하다</b> = ichimda qilingan, tekshirilmagan
      taxmin.</li>
    <li>받침 bor → <b>으려니</b> · yoʻq → <b>려니</b>.</li>
    <li>Deyarli doim <b>했다</b> shaklida — keyin koʻpincha
      <b>그런데 / 알고 보니</b>.</li>
    <li><b>그러려니 하다</b> — “shunday ekan-da deb qoʻyaverish”.
      Butun bir hayotiy pozitsiya.</li>
    <li>그렇다 → <b>그러려니</b> (ㅎ tushadi, PK-47).</li>
    <li>Ovoz chiqarib aytiladigan taxmin — <b>(으)ㄹ 것 같다</b>
      (PK-52), bu emas.</li>
    <li>려 oilasi: <b>려고 하다</b> niyat · <b>려던 참</b> ayni
      payt · <b>려니 하다</b> taxmin.</li>
    <li>Maʼnoni 려 emas, <em>undan keyingi qism</em> beradi.</li>
  </ul>
</div>
""",
    },
]
