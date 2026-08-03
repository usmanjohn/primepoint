# -*- coding: utf-8 -*-
"""Prime Korean — Block E, darslar 59–61.

59. 아/어 놓다 va 아/어 두다 — holatni saqlash
60. Koʻchirma gap 1: -다고 하다 (darak), -냐고 하다 (soʻroq)
61. Koʻchirma gap 2: -라고 하다 (buyruq), -자고 하다 (taklif)

Uchalasining ham oʻzbekcha kaliti bor:
  아/어 놓다  = "qili-B QOʻYDIM" (tayyor turibdi) — 버리다 dan farqi shu
  -다고 하다  = "…-DI DEB aytdi"  — oʻzbekchadagi DEB aynan koreyscha 고
  -라고/자고  = "bor DEB aytdi" / "boraylik DEB taklif qildi"

60-61 birga oʻqilishi shart: bitta mashina, toʻrtta gap turi.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

Oʻqish matnlari: corner/management/commands/_stories_prime_korean_59_61.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_59_61.py --author=prime
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
        "title": "PK-59: 아/어 놓다 va 아/어 두다 — holatni saqlash",
        "category": "korean",
        "order": 59,
        "summary": (
            "“Ochib qoʻydim” — ochdim va ochiq turibdi. Oʻzbekchadagi “-b qoʻymoq” "
            "koreys tilida ikkiga boʻlinadi: 버리다 va 놓다."
        ),
        "stories": ["열어 놓은 창문"],
        "content": """
<h2>PK-59: 아/어 놓다 va 아/어 두다 — holatni saqlash</h2>

<p>Mehmon keladi. Siz ovqatni pishirdingiz, stolni tayyorladingiz,
derazani ochdingiz — va hammasi <em>shu holda turibdi</em>. Oʻzbekchada
buni bir soʻz bilan aytamiz: “pishirib <b>qoʻydim</b>”, “ochib
<b>qoʻydim</b>”. Ish tugadi, lekin natijasi qolib turibdi. Koreys
tilida bu ishni <b>놓다</b> va <b>두다</b> bajaradi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>아/어 놓다</b> bilan “qilib qoʻydim” deysiz</li>
    <li><b>아/어 두다</b> ning farqini bilib olasiz</li>
    <li>Uni oʻtgan darsdagi <b>아/어 버리다</b> dan ajratasiz</li>
    <li>PK-42 dagi <b>아/어 있다</b> bilan solishtirasiz</li>
    <li>Kundalik qisqargan shakl <b>해 놨어요</b> ni oʻrganasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">Feʼl</span>
  <span class="pe-chip pe-chip--v">아/어</span>
  <span class="pe-chip pe-chip--v">놓다 / 두다</span>
  <span class="pe-chip pe-chip--adv">= qilib qoʻymoq (tayyor turibdi)</span>
</div>

<h3>1. 놓다 ning oʻzi — “qoʻymoq”</h3>

<p><b>놓다</b> oddiy feʼl sifatida “qoʻymoq” degani: 책을 책상 위에
놓았어요 (kitobni stol ustiga qoʻydim). Koʻmakchi boʻlganda maʼnosi
mantiqan oʻsib chiqadi: <em>ishni qildim va shu holda qoʻyib
turdim</em>.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>아/어 shakli</th><th>Koʻmakchi</th><th>Natija</th>
      <th>Maʼnosi</th></tr>
  <tr><td>열다</td><td class="pk-stem">열어</td><td class="pk-end">놓다</td>
      <td class="pk-res">열어 놓다</td><td class="pk-uz">ochib qoʻymoq</td></tr>
  <tr><td>만들다</td><td class="pk-stem">만들어</td><td class="pk-end">놓다</td>
      <td class="pk-res">만들어 놓다</td><td class="pk-uz">tayyorlab qoʻymoq</td></tr>
  <tr><td>사다</td><td class="pk-stem">사</td><td class="pk-end">놓다</td>
      <td class="pk-res">사 놓다</td><td class="pk-uz">sotib qoʻymoq</td></tr>
  <tr><td>하다</td><td class="pk-stem">해</td><td class="pk-end">놓다</td>
      <td class="pk-res">해 놓다</td><td class="pk-uz">qilib qoʻymoq</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">더워서 창문을 <span class="pe-hl pe-hl--v">열어
     놓았어요</span>.</p>
  <p class="pe-ex__uz">Issiq boʻlgani uchun derazani ochib qoʻydim.</p>
  <p class="pe-ex__why">Deraza hozir ham ochiq — natija turibdi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">손님이 오니까 음식을 미리
     <span class="pe-hl pe-hl--v">만들어 놓았어요</span>.</p>
  <p class="pe-ex__uz">Mehmon kelayotgani uchun ovqatni oldindan
  tayyorlab qoʻydim.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchadagi bitta soʻz koreyschada ikkiga boʻlinadi.</b>
  Biz “-b qoʻymoq” ni ikki xil maʼnoda ishlatamiz:<br>
  “Tortni ye<b>b qoʻydi</b>” — tugadi, endi yoʻq → <b>아/어 버리다</b>
  (PK-58)<br>
  “Ovqatni pishiri<b>b qoʻydi</b>” — tayyor turibdi → <b>아/어 놓다</b><br>
  Oʻzbek tilida farqni kontekst aytadi, koreys tilida esa <em>boshqa
  soʻz</em> aytadi. Shuning uchun bu ikki darsni yonma-yon eslang: biri
  <b>yoʻq qiladi</b>, ikkinchisi <b>saqlab turadi</b>.</p>
</div>

<h3>2. Ikki vazifasi: tayyorgarlik va saqlash</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Tayyorgarlik</p>
    <p>Keyin kerak boʻladi — <b>oldindan</b> qilib qoʻyaman.</p>
    <p><small>표를 미리 사 놓았어요. — Chiptani oldindan olib
    qoʻydim.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Holatni saqlash</p>
    <p>Qildim va <b>shu holda qoldirdim</b>.</p>
    <p><small>문을 열어 놓았어요. — Eshikni ochib qoʻydim (ochiq
    turibdi).</small></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">시험이 있으니까 단어를 미리
     <span class="pe-hl pe-hl--v">외워 놓았어요</span>.</p>
  <p class="pe-ex__uz">Imtihon boʻlgani uchun soʻzlarni oldindan yodlab
  qoʻydim.</p>
</div>

<h3>3. 놓다 va 두다 — farqi bormi?</h3>

<p>Koʻp holatda ikkalasi ham toʻgʻri va koreyslar ikkalasini ham
ishlatadi. Kichik ohang farqi bor:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h">아/어 놓다</p>
    <p>Koʻproq <b>qisqa muddat</b> va koʻzga koʻrinadigan holat.</p>
    <p><small>창문을 열어 놓았어요.</small></p></div>
  <div class="pe-card"><p class="pe-card__h">아/어 두다</p>
    <p>Koʻproq <b>uzoq muddat</b> — “shunday turaversin” degan ohang.</p>
    <p><small>돈을 은행에 넣어 두었어요.</small></p></div>
</div>

<div class="pe-call pe-tip">
  <p><b>두다</b> baʼzi iboralarda qotib qolgan — bu yerda 놓다
  ishlatilmaydi:<br>
  <b>알아 두다</b> — bilib qoʻymoq (“shuni bilib qoʻying”)<br>
  <b>기억해 두다</b> — esda saqlab qoʻymoq<br>
  이 단어를 <b>알아 두세요</b>. — Bu soʻzni bilib qoʻying.</p>
</div>

<h3>4. 아/어 있다 (PK-42) bilan solishtiring</h3>

<p>Ikkalasi ham “holat” haqida, lekin kim haqida gapirayotganingiz
boshqa:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">문이 열려 있어요</p>
    <p><b>Narsa</b> haqida. Eshik ochiq turibdi.</p>
    <p>Kim ochgani muhim emas — majhul (PK-56) + 있다.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">문을 열어 놓았어요</p>
    <p><b>Odam</b> haqida. Men ochdim va shunday qoldirdim.</p>
    <p>Bajaruvchi bor, shuning uchun toʻldiruvchi 문<b>을</b>.</p>
  </div>
</div>

<div class="pe-call pe-rule">
  <p><b>Belgisi — qoʻshimcha.</b> 문<b>이</b> 열려 있어요 (이/가 — holat).
  문<b>을</b> 열어 놓았어요 (을/를 — men qilgan ish). Qoʻshimchaga
  qarang, adashmaysiz.</p>
</div>

<h3>5. Kundalik nutqda: 놨어요</h3>

<p>놓았어요 tez gapirganda qisqaradi: 놓았 → <b>놨</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">숙제를 벌써 <span class="pe-hl pe-hl--v">해
     놨어요</span>.</p>
  <p class="pe-ex__uz">Uy vazifasini allaqachon qilib qoʻyganman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">불을 <span class="pe-hl pe-hl--v">켜 놨어요</span>.</p>
  <p class="pe-ex__uz">Chiroqni yoqib qoʻydim.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>날씨가 좋아 놓았어요.</s></p>
  <p class="pe-good">날씨가 <b>좋아졌어요</b>.</p>
  <p><small>놓다 faqat <b>harakat feʼllari</b> bilan. 좋다 — sifat,
  unga 아/어지다 (PK-56) kerak.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>문을 열어 놓아 있어요.</s></p>
  <p class="pe-good">문을 <b>열어 놓았어요</b>. (yoki 문이 <b>열려
    있어요</b>)</p>
  <p><small>놓다 va 있다 birga kelmaydi — bittasini tanlang.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>음식을 만들 놓았어요.</s></p>
  <p class="pe-good">음식을 <b>만들어</b> 놓았어요.</p>
  <p><small>놓다 dan oldin feʼl <b>아/어 shaklida</b> turishi
  shart.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>지갑을 잃어 놓았어요.</s></p>
  <p class="pe-good">지갑을 <b>잃어버렸어요</b>.</p>
  <p><small>Yoʻqolgan narsa saqlanib turmaydi — bu 버리다 ning
  ishi.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 더워서 창문을
  <span class="pe-blank"></span> 놓았어요. (열다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>열어</b> — 놓다 dan oldin feʼl 아/어 shaklida turadi:
    열어 놓았어요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Farqini ayting:
  케이크를 먹어 버렸어요 / 케이크를 만들어 놓았어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Birinchisi — <b>tort tugadi, endi yoʻq</b>. Ikkinchisi —
    <b>tort tayyor turibdi</b>. Oʻzbekchada ikkalasi ham “-b qoʻydim”,
    koreyschada esa boshqa-boshqa soʻz.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Qaysi biri toʻgʻri va nega?
  문이 열려 있어요 / 문을 열어 놓았어요 — “eshik ochiq turibdi, kim
  ochgani nomaʼlum”.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>문이 열려 있어요</b> — bu narsaning holati (majhul + 있다).
    문<b>을</b> 열어 놓았어요 boʻlsa bajaruvchi bor boʻlardi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> 해 놓았어요 ning kundalik
  qisqargan shakli qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>해 놨어요.</b> 놓았 → <b>놨</b> boʻlib qisqaradi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> “Bu soʻzni bilib qoʻying” —
  koreyschada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>이 단어를 알아 두세요.</b> 알아 두다 — qotib qolgan ibora,
    bu yerda 놓다 ishlatilmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Xatoni toping:
  <s>표를 미리 사 놓아 있어요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>표를 미리 사 놓았어요.</b> 놓다 va 있다 birga
    kelmaydi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>아/어 놓다</b> — qilib qoʻymoq (natija turibdi)</li>
  <li><b>아/어 두다</b> — qilib qoʻymoq (uzoqroq muddatga)</li>
  <li><b>놓다</b> — qoʻymoq · <b>두다</b> — qoldirmoq</li>
  <li><b>알아 두다</b> — bilib qoʻymoq</li>
  <li><b>미리</b> — oldindan</li>
  <li><b>표</b> — chipta</li>
  <li><b>손님</b> — mehmon</li>
  <li><b>외우다</b> — yodlamoq</li>
  <li><b>켜다</b> — yoqmoq (chiroq)</li>
  <li><b>넣다</b> — solmoq, qoʻymoq (ichiga)</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>아/어 놓다</b> = ishni qildim va <b>natijasi turibdi</b>.</li>
    <li>Ikki vazifasi: <b>tayyorgarlik</b> (미리 사 놓다) va
      <b>holatni saqlash</b> (열어 놓다).</li>
    <li><b>두다</b> — deyarli bir xil, uzoqroq muddat ohangi;
      <b>알아 두다</b>, <b>기억해 두다</b> qotib qolgan.</li>
    <li>Qisqargan shakli: 놓았어요 → <b>놨어요</b>.</li>
    <li>Faqat harakat feʼllari bilan — sifat uchun 아/어지다.</li>
    <li><b>문이 열려 있어요</b> (narsa holati) va <b>문을 열어 놓았어요</b>
      (men qildim) — qoʻshimchaga qarang.</li>
    <li>Oʻzbekchadagi “-b qoʻymoq” koreyschada ikkiga boʻlinadi:
      <b>버리다</b> (yoʻq boʻldi) va <b>놓다</b> (turibdi).</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-60: Koʻchirma gap 1 — -다고 하다 (darak), -냐고 하다 (soʻroq)",
        "category": "korean",
        "order": 60,
        "summary": (
            "“Boraman DEB aytdi” — oʻzbekchadagi DEB koreys tilida 고. Boshqa "
            "odamning gapini oʻz gapingiz ichida aytishni oʻrganasiz."
        ),
        "stories": ["소문"],
        "content": """
<h2>PK-60: Koʻchirma gap 1 — -다고 하다 (darak), -냐고 하다 (soʻroq)</h2>

<p>Doʻstingiz “men ertaga boraman” dedi. Endi siz buni uchinchi odamga
yetkazyapsiz. Oʻzbekchada nima deysiz? — “U ertaga boraman <b>deb</b>
aytdi”. Mana shu kichkina <b>deb</b> — butun darsning kaliti. Koreys
tilida uning aynan oʻrnida <b>고</b> turadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Boshqaning <b>darak gapini</b> -다고 하다 bilan yetkazasiz</li>
    <li>Feʼl, sifat va ot uchun uchta boshqa shaklni ajratasiz</li>
    <li><b>Soʻroq gapni</b> -냐고 하다 bilan yetkazasiz</li>
    <li>Oʻtgan va kelasi zamonni koʻchirma gapga qoʻyasiz</li>
    <li>하다 oʻrniga 말하다, 묻다, 물어보다 ishlatasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">Boshqaning gapi</span>
  <span class="pe-chip pe-chip--v">다고 / 냐고</span>
  <span class="pe-chip pe-chip--v">하다</span>
  <span class="pe-chip pe-chip--adv">= … deb aytdi / soʻradi</span>
</div>

<h3>1. Oʻzbekchadagi “deb” = koreyschadagi 고</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">민수 씨가 내일 <span class="pe-hl pe-hl--v">간다고
     했어요</span>.</p>
  <p class="pe-ex__uz">Minsu ertaga boradi <b>deb</b> aytdi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu dars oʻzbek oʻquvchi uchun sovgʻa.</b> Ingliz tilida
  koʻchirma gap butun jumlani buzadi: “I will go” → “he said <em>that
  he would</em> go” — olmosh oʻzgaradi, zamon orqaga suriladi, tartib
  aralashadi. Oʻzbek tilida esa hech narsa buzilmaydi: gapni aytasiz,
  orqasiga <b>deb</b> qoʻyasiz, keyin “aytdi” deysiz. Koreys tili ham
  aynan shunday ishlaydi:<br>
  <span class="pk-stem">내일 간다</span> +
  <span class="pk-end">고</span> +
  <span class="pk-res">했어요</span><br>
  <span class="pk-stem">ertaga boradi</span> +
  <span class="pk-end">deb</span> +
  <span class="pk-res">aytdi</span><br>
  Yaʼni sizga faqat <em>gapning oxirgi shakli</em> yangi — fikr esa
  allaqachon tanish.</p>
</div>

<h3>2. Darak gap: uch xil shakl</h3>

<p>고 dan oldingi shakl gapning turiga qarab oʻzgaradi. Bu darsning
yagona qiyin joyi — shuning uchun jadvalni yaxshilab koʻring:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Nima</th><th>Shakl</th><th>Misol</th><th>Natija</th></tr>
  <tr><td><b>Feʼl</b>, 받침 yoʻq</td><td class="pk-end">ㄴ다고</td>
      <td class="pk-stem">가다</td><td class="pk-res">간다고 해요</td></tr>
  <tr><td><b>Feʼl</b>, 받침 bor</td><td class="pk-end">는다고</td>
      <td class="pk-stem">먹다</td><td class="pk-res">먹는다고 해요</td></tr>
  <tr><td><b>Sifat</b></td><td class="pk-end">다고</td>
      <td class="pk-stem">좋다</td><td class="pk-res">좋다고 해요</td></tr>
  <tr><td><b>Ot</b> (이다)</td><td class="pk-end">(이)라고</td>
      <td class="pk-stem">학생이다</td><td class="pk-res">학생이라고 해요</td></tr>
  <tr><td><b>Oʻtgan zamon</b></td><td class="pk-end">았/었다고</td>
      <td class="pk-stem">갔다</td><td class="pk-res">갔다고 해요</td></tr>
  <tr><td><b>Kelasi zamon</b></td><td class="pk-end">(으)ㄹ 거라고</td>
      <td class="pk-stem">갈 거예요</td><td class="pk-res">갈 거라고 해요</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Eng koʻp adashiladigan joy — feʼl va sifat.</b> Faqat
  <em>feʼl</em> ㄴ다/는다 oladi. Sifat esa oddiy <b>다고</b> boʻlib
  qoladi:<br>
  가다 (feʼl) → <b>간다고</b> · 먹다 (feʼl) → <b>먹는다고</b><br>
  좋다 (sifat) → <b>좋다고</b> · 바쁘다 (sifat) → <b>바쁘다고</b><br>
  있다/없다 ham sifat kabi: <b>있다고</b>, <b>없다고</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">지영 씨가 요즘 <span class="pe-hl pe-hl--v">바쁘다고
     했어요</span>.</p>
  <p class="pe-ex__uz">Jiyon oxirgi paytda band <b>deb</b> aytdi.</p>
  <p class="pe-ex__why">바쁘다 — sifat, shuning uchun 바쁜다고 emas.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">아프소나 씨가 <span class="pe-hl pe-hl--v">학생이라고
     했어요</span>.</p>
  <p class="pe-ex__uz">Afsona oʻzini talaba <b>deb</b> aytdi.</p>
  <p class="pe-ex__why">Ot bilan 이다 → <b>(이)라고</b>. 받침 yoʻq
  boʻlsa 이 tushadi: 친구<b>라고</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">베크조드 씨가 어제 영화를
     <span class="pe-hl pe-hl--v">봤다고 했어요</span>.</p>
  <p class="pe-ex__uz">Bekzod kecha kino koʻrdim <b>deb</b> aytdi.</p>
</div>

<h3>3. Soʻroq gap: -냐고 하다</h3>

<p>Kimdir savol bergan boʻlsa, 고 dan oldin <b>냐</b> turadi. Bu yerda
feʼl va sifat farqi <em>yoʻq</em> — ikkalasi ham 냐고:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Asl savol</th><th>Koʻchirma shakli</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-stem">어디에 가요?</td><td class="pk-res">어디에 가냐고 했어요</td>
      <td class="pk-uz">qayerga borasiz deb soʻradi</td></tr>
  <tr><td class="pk-stem">맛있어요?</td><td class="pk-res">맛있냐고 했어요</td>
      <td class="pk-uz">mazalimi deb soʻradi</td></tr>
  <tr><td class="pk-stem">학생이에요?</td><td class="pk-res">학생이냐고 했어요</td>
      <td class="pk-uz">talabamisiz deb soʻradi</td></tr>
  <tr><td class="pk-stem">밥을 먹었어요?</td><td class="pk-res">밥을 먹었냐고 했어요</td>
      <td class="pk-uz">ovqat yedingizmi deb soʻradi</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">선생님이 숙제를 <span class="pe-hl pe-hl--v">했냐고
     물어봤어요</span>.</p>
  <p class="pe-ex__uz">Oʻqituvchi uy vazifasini qildingmi <b>deb</b>
  soʻradi.</p>
  <p class="pe-ex__why">Savol boʻlgani uchun 하다 emas, <b>묻다 /
  물어보다</b> tabiiyroq.</p>
</div>

<div class="pe-call pe-tip">
  <p>Kitoblarda <b>느냐고</b> (feʼl) va <b>(으)냐고</b> (sifat) shakllari
  ham uchraydi: 가느냐고, 좋으냐고. Ular notoʻgʻri emas — biroz eski va
  rasmiy. Kundalik nutqda hamma <b>냐고</b> deydi, siz ham shuni
  ishlating.</p>
</div>

<h3>4. 하다 ning oʻrniga boshqa feʼllar</h3>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h">고 하다</p>
    <p>eng keng — “dedi”</p></div>
  <div class="pe-card"><p class="pe-card__h">고 말하다</p>
    <p>“gapirdi, aytdi” — biroz rasmiyroq</p></div>
  <div class="pe-card"><p class="pe-card__h">고 묻다 / 물어보다</p>
    <p>faqat savol uchun — “soʻradi”</p></div>
  <div class="pe-card"><p class="pe-card__h">고 들었어요</p>
    <p>“…ekan deb eshitdim”</p></div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">내일 시험이 <span class="pe-hl pe-hl--v">없다고
     들었어요</span>.</p>
  <p class="pe-ex__uz">Ertaga imtihon yoʻq <b>deb</b> eshitdim.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>민수 씨가 내일 가다고 했어요.</s></p>
  <p class="pe-good">민수 씨가 <b>간다고</b> 했어요.</p>
  <p><small>Feʼl 받침siz boʻlsa <b>ㄴ다고</b>: 가 + ㄴ다고 =
  간다고.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>날씨가 춥는다고 했어요.</s></p>
  <p class="pe-good">날씨가 <b>춥다고</b> 했어요.</p>
  <p><small>춥다 — sifat. Sifat ㄴ다/는다 olmaydi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>아프소나 씨가 학생이다고 했어요.</s></p>
  <p class="pe-good">아프소나 씨가 <b>학생이라고</b> 했어요.</p>
  <p><small>Ot + 이다 → <b>(이)라고</b>, 이다고 emas.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>어디에 가냐고 했어요? (soʻrayotgan boʻlsangiz)</s></p>
  <p class="pe-good">어디에 <b>가요?</b></p>
  <p><small>냐고 하다 — <em>boshqaning</em> savolini yetkazish uchun.
  Oʻzingiz soʻrayotgan boʻlsangiz oddiy savol shakli kerak.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Koʻchirma gapga aylantiring:
  민수: “저는 내일 가요.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>민수 씨가 내일 간다고 했어요.</b> 가다 — feʼl, 받침 yoʻq →
    ㄴ다고.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Koʻchirma gapga aylantiring:
  지영: “요즘 바빠요.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>지영 씨가 요즘 바쁘다고 했어요.</b> 바쁘다 — sifat, shuning
    uchun oddiy <b>다고</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Toʻldiring: 아프소나 씨가
  <span class="pe-blank"></span> 했어요. (“men talabaman”)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>학생이라고</b> — ot + 이다 → (이)라고.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Koʻchirma gapga aylantiring:
  선생님: “숙제를 했어요?”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>선생님이 숙제를 했냐고 물어봤어요.</b> Savol → 냐고, va
    묻다/물어보다 tabiiyroq.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Xatoni toping:
  <s>날씨가 춥는다고 했어요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>날씨가 춥다고 했어요.</b> 춥다 sifat, ㄴ다/는다
    olmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> “Ertaga imtihon yoʻq deb
  eshitdim” — koreyschada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>내일 시험이 없다고 들었어요.</b> 없다 sifat kabi ishlaydi →
    없다고.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>-다고 하다</b> — … deb aytmoq (darak gap)</li>
  <li><b>-냐고 하다</b> — … deb soʻramoq (soʻroq gap)</li>
  <li><b>(이)라고 하다</b> — … deb aytmoq (ot bilan)</li>
  <li><b>말하다</b> — gapirmoq, aytmoq</li>
  <li><b>묻다 / 물어보다</b> — soʻramoq</li>
  <li><b>듣다</b> — eshitmoq · <b>들었어요</b> — eshitdim</li>
  <li><b>요즘</b> — oxirgi paytda</li>
  <li><b>바쁘다</b> — band</li>
  <li><b>소문</b> — mish-mish, gap</li>
  <li><b>사실</b> — haqiqat, aslida</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>고</b> = oʻzbekchadagi <b>deb</b>. Gap buzilmaydi, orqasiga
      qoʻshimcha qoʻshiladi.</li>
    <li>Feʼl: 받침 yoʻq → <b>ㄴ다고</b> (간다고) · 받침 bor →
      <b>는다고</b> (먹는다고).</li>
    <li>Sifat: oddiy <b>다고</b> (좋다고, 바쁘다고). 있다/없다 ham
      shunday.</li>
    <li>Ot: <b>(이)라고</b> (학생이라고, 친구라고).</li>
    <li>Oʻtgan zamon: <b>았/었다고</b> (갔다고). Kelasi:
      <b>(으)ㄹ 거라고</b>.</li>
    <li>Soʻroq: <b>냐고</b> — bu yerda feʼl/sifat farqi yoʻq.</li>
    <li>하다 oʻrniga <b>말하다 · 묻다 · 물어보다 · 들었어요</b>.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-61: Koʻchirma gap 2 — -라고 하다 (buyruq), -자고 하다 (taklif)",
        "category": "korean",
        "order": 61,
        "summary": (
            "“Bor DEB aytdi”, “boraylik DEB taklif qildi” — oʻtgan darsdagi "
            "mashinaning qolgan ikki tugmasi: buyruq va taklif."
        ),
        "stories": ["산에 가자고 했어요 — 일기"],
        "content": """
<h2>PK-61: Koʻchirma gap 2 — -라고 하다 (buyruq), -자고 하다 (taklif)</h2>

<p>Oʻtgan darsda ikkita gap turini oʻrgandingiz: kimdir nimadir
<em>aytdi</em> (다고) va kimdir nimadir <em>soʻradi</em> (냐고). Lekin
odamlar yana ikki xil gapiradi: ular <b>buyuradi</b> (“eshikni
yoping!”) va <b>taklif qiladi</b> (“birga boraylik!”). Bugun shu ikkita
tugma qoʻshiladi — va mashina tugallanadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Buyruqni</b> -(으)라고 하다 bilan yetkazasiz</li>
    <li><b>Taqiqni</b> -지 말라고 하다 bilan yetkazasiz</li>
    <li><b>Taklifni</b> -자고 하다 bilan yetkazasiz</li>
    <li><b>달라고</b> va <b>주라고</b> farqini bilib olasiz</li>
    <li>Toʻrtta gap turini bitta jadvalda koʻrasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">Feʼl oʻzagi</span>
  <span class="pe-chip pe-chip--v">(으)라고 / 자고</span>
  <span class="pe-chip pe-chip--v">하다</span>
  <span class="pe-chip pe-chip--adv">= … deb aytdi / taklif qildi</span>
</div>

<h3>1. Buyruq: -(으)라고 하다</h3>

<p>Asl gap <b>(으)세요</b> yoki buyruq shaklida boʻlsa, koʻchirma
gapda <b>(으)라고</b> boʻladi. Bu yerda tanish 받침 ayrisi ishlaydi:</p>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">라고</span></p>
    <p>가다 → 가<b>라고</b> 했어요</p>
    <p>하다 → 하<b>라고</b> 했어요</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">으라고</span></p>
    <p>먹다 → 먹<b>으라고</b> 했어요</p>
    <p>읽다 → 읽<b>으라고</b> 했어요</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">선생님이 일찍 <span class="pe-hl pe-hl--v">오라고
     했어요</span>.</p>
  <p class="pe-ex__uz">Oʻqituvchi erta kel <b>deb</b> aytdi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">어머니가 약을 <span class="pe-hl pe-hl--v">먹으라고
     했어요</span>.</p>
  <p class="pe-ex__uz">Onam dorini ich <b>deb</b> aytdi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham ayni shu tuzilish bor.</b> “Erta kel <b>deb</b>
  aytdi”, “dorini ich <b>deb</b> aytdi” — biz buyruqni oʻzgartirmaymiz,
  shundayligicha qoldirib, orqasiga <b>deb</b> qoʻyamiz. Koreys tili
  ham xuddi shunday: buyruq oʻz shaklida qoladi, faqat oxiriga
  <b>(으)라고</b> ulanadi. Ingliz tilida esa buyruq butunlay boshqa
  qurilmaga aylanadi (“told me <em>to</em> come”) — u yerda oʻrganish
  qiyinroq.</p>
</div>

<h3>2. Taqiq: -지 말라고 하다</h3>

<p>PK-29 dagi <b>지 마세요</b> koʻchirma gapda <b>지 말라고</b>
boʻladi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">선생님이 교실에서 <span class="pe-hl pe-hl--neg">뛰지
     말라고 했어요</span>.</p>
  <p class="pe-ex__uz">Oʻqituvchi sinfda yugurmang <b>deb</b> aytdi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>말라고</b>, <s>마라고</s> emas. 말다 ning oʻzagi <b>말</b> —
  unga 라고 qoʻshiladi. Bu eng koʻp uchraydigan xatolardan biri.</p>
</div>

<h3>3. Taklif: -자고 하다</h3>

<p>Asl gap “birga qilaylik” maʼnosida boʻlsa — <b>자고</b>. Bu yerda
받침 ayrisi <em>yoʻq</em>, hamma feʼlga bir xil qoʻshiladi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Asl gap</th><th>Koʻchirma shakli</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-stem">같이 가요!</td><td class="pk-res">같이 가자고 했어요</td>
      <td class="pk-uz">birga boraylik dedi</td></tr>
  <tr><td class="pk-stem">밥을 먹어요!</td><td class="pk-res">밥을 먹자고 했어요</td>
      <td class="pk-uz">ovqat yeylik dedi</td></tr>
  <tr><td class="pk-stem">사진을 찍어요!</td><td class="pk-res">사진을 찍자고 했어요</td>
      <td class="pk-uz">rasmga tushaylik dedi</td></tr>
  <tr><td class="pk-stem">가지 마요!</td><td class="pk-res">가지 말자고 했어요</td>
      <td class="pk-uz">bormaylik dedi</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">자스루르 씨가 주말에 산에
     <span class="pe-hl pe-hl--v">가자고 했어요</span>.</p>
  <p class="pe-ex__uz">Jasur dam olish kuni togʻga chiqaylik <b>deb</b>
  taklif qildi.</p>
</div>

<div class="pe-call pe-tip">
  <p>Taklif boʻlgani uchun 하다 oʻrniga <b>제안하다</b> (taklif qilmoq)
  yoki 말하다 ham ishlatiladi. Lekin kundalik nutqda oddiy
  <b>했어요</b> eng koʻp uchraydi.</p>
</div>

<h3>4. 달라고 va 주라고 — kimga beriladi?</h3>

<p>PK-31 dagi <b>주다</b> koʻchirma gapda ikkiga boʻlinadi, va bu farq
juda muhim:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">달라고 하다</p>
    <p>Soʻrayotgan odam <b>oʻziga</b> soʻraydi.</p>
    <p><small>친구가 돈을 <b>달라고</b> 했어요. — Doʻstim mendan pul
    soʻradi (oʻziga).</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">주라고 하다</p>
    <p>Boshqa <b>uchinchi odamga</b> berilsin.</p>
    <p><small>친구가 동생에게 돈을 <b>주라고</b> 했어요. — Doʻstim ukamga
    pul ber dedi.</small></p>
  </div>
</div>

<div class="pe-call pe-uz">
  <p>Oʻzbek tilida bu farqni <em>olmosh</em> aytadi: “men<b>ga</b> ber”
  va “un<b>ga</b> ber”. Koreys tilida esa <em>feʼlning oʻzi</em>
  oʻzgaradi: <b>달라고</b> va <b>주라고</b>. Yaʼni koreyscha bu
  maʼlumotni feʼl ichiga yashiradi — shuning uchun olmoshni aytish
  shart emas.</p>
</div>

<h3>5. Toʻrtta gap turi — bitta jadval</h3>

<p>PK-60 va PK-61 birga bitta tizim. Mana butun mashina:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Gap turi</th><th>Qoʻshimcha</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td>Darak (평서문)</td><td class="pk-end">다고</td>
      <td class="pk-res">간다고 했어요</td>
      <td class="pk-uz">boradi deb aytdi</td></tr>
  <tr><td>Soʻroq (의문문)</td><td class="pk-end">냐고</td>
      <td class="pk-res">가냐고 했어요</td>
      <td class="pk-uz">boradimi deb soʻradi</td></tr>
  <tr><td>Buyruq (명령문)</td><td class="pk-end">(으)라고</td>
      <td class="pk-res">가라고 했어요</td>
      <td class="pk-uz">bor deb aytdi</td></tr>
  <tr><td>Taklif (청유문)</td><td class="pk-end">자고</td>
      <td class="pk-res">가자고 했어요</td>
      <td class="pk-uz">boraylik deb taklif qildi</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Buyruq va taklifda zamon yoʻq.</b> “Bor dedi” gapida buyruqning
  oʻzi oʻtgan zamonga tushmaydi — faqat <b>했어요</b> oʻtgan zamonda
  boʻladi. Shuning uchun <s>갔라고</s>, <s>갔자고</s> degan shakllar
  mavjud emas.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>어머니가 약을 먹라고 했어요.</s></p>
  <p class="pe-good">어머니가 약을 <b>먹으라고</b> 했어요.</p>
  <p><small>먹 da 받침 bor → <b>으라고</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>선생님이 뛰지 마라고 했어요.</s></p>
  <p class="pe-good">선생님이 뛰지 <b>말라고</b> 했어요.</p>
  <p><small>말다 + 라고 = <b>말라고</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>친구가 같이 갔자고 했어요.</s></p>
  <p class="pe-good">친구가 같이 <b>가자고</b> 했어요.</p>
  <p><small>Taklifda zamon boʻlmaydi — oʻtgan zamon faqat
  했어요 da.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>친구가 돈을 주라고 했어요. (“mendan soʻradi”
    maʼnosida)</s></p>
  <p class="pe-good">친구가 돈을 <b>달라고</b> 했어요.</p>
  <p><small>Oʻziga soʻrasa — <b>달라고</b>. Uchinchi odamga berilsin
  desa — 주라고.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Koʻchirma gapga aylantiring:
  선생님: “일찍 오세요.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>선생님이 일찍 오라고 했어요.</b> 오다 — 받침 yoʻq →
    라고.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 어머니가 약을
  <span class="pe-blank"></span> 했어요. (먹다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>먹으라고</b> — 먹 da 받침 bor, shuning uchun 으라고.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Koʻchirma gapga aylantiring:
  자스루르: “주말에 같이 산에 가요!”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>자스루르 씨가 주말에 같이 산에 가자고 했어요.</b> Taklif →
    <b>자고</b>, 받침 ayrisi yoʻq.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Farqini ayting:
  달라고 했어요 / 주라고 했어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>달라고</b> — soʻrayotgan odam oʻziga soʻradi.
    <b>주라고</b> — uchinchi odamga berilsin dedi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Xatoni toping:
  <s>선생님이 뛰지 마라고 했어요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>뛰지 말라고 했어요.</b> 말다 ning oʻzagi 말,
    unga 라고 qoʻshiladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Bu toʻrt gapni ajrating:
  간다고 · 가냐고 · 가라고 · 가자고.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>간다고</b> — “boradi” dedi (darak).
    <b>가냐고</b> — “boradimi?” deb soʻradi (soʻroq).
    <b>가라고</b> — “bor” dedi (buyruq).
    <b>가자고</b> — “boraylik” dedi (taklif).</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>-(으)라고 하다</b> — … deb buyurmoq</li>
  <li><b>-지 말라고 하다</b> — … qilmang deb aytmoq</li>
  <li><b>-자고 하다</b> — … qilaylik deb taklif qilmoq</li>
  <li><b>달라고 하다</b> — oʻziga berishni soʻramoq</li>
  <li><b>주라고 하다</b> — boshqaga berishni aytmoq</li>
  <li><b>제안하다</b> — taklif qilmoq</li>
  <li><b>약</b> — dori · <b>뛰다</b> — yugurmoq</li>
  <li><b>산</b> — togʻ · <b>등산</b> — togʻga chiqish</li>
  <li><b>일찍</b> — erta</li>
  <li><b>준비물</b> — olib boriladigan narsalar</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li>Buyruq: <b>(으)라고 하다</b> — 받침 yoʻq → 라고, bor →
      으라고.</li>
    <li>Taqiq: <b>지 말라고 하다</b> (마라고 emas!).</li>
    <li>Taklif: <b>자고 하다</b> — hamma feʼlga bir xil, ayri yoʻq.</li>
    <li>Inkor taklif: <b>지 말자고 하다</b>.</li>
    <li><b>달라고</b> (menga ber) va <b>주라고</b> (unga ber) —
      koreyscha bu farqni feʼl ichiga yashiradi.</li>
    <li>Buyruq va taklifda <b>zamon boʻlmaydi</b> — oʻtgan zamon faqat
      했어요 da.</li>
    <li>Toʻrtta tugma: <b>다고 · 냐고 · (으)라고 · 자고</b> —
      va hammasining oʻzbekchasi bitta <b>deb</b>.</li>
  </ul>
</div>
""",
    },
]
