# -*- coding: utf-8 -*-
"""Prime Korean — Block D, darslar 44–46.

44. Aniqlovchi 2: 동사 + (으)ㄴ (oʻtgan), (으)ㄹ (kelasi)
45. Aniqlovchi 3: 형용사 + (으)ㄴ
46. Otlashtirish: 는 것, 기, (으)ㅁ

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

Oʻqish matnlari: corner/management/commands/_stories_prime_korean_44_46.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_44_46.py --author=prime
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
        "title": "PK-44: Aniqlovchi 2: 동사 + (으)ㄴ (oʻtgan), (으)ㄹ (kelasi)",
        "category": "korean",
        "order": 44,
        "summary": (
            "“Kecha koʻrgan kino” va “ertaga koʻradigan kino”. Feʼl aniqlovchisining "
            "qolgan ikki zamoni — va nega siz ularni allaqachon ishlatib yurgansiz."
        ),
        "stories": ["어제 본 영화"],
        "content": """
<h2>PK-44: Aniqlovchi 2: 동사 + (으)ㄴ (oʻtgan), (으)ㄹ (kelasi)</h2>

<p>Oʻtgan darsda siz “<b>oʻqiydigan</b> odam” — 읽<b>는</b> 사람 — deyishni oʻrgandingiz.
Lekin hayotda koʻpincha boshqa narsa kerak boʻladi: “kecha <b>oʻqigan</b> kitob”,
“ertaga <b>oʻqiydigan</b> kitob”. Feʼl aniqlovchisining uchta zamoni bor, va bugun
qolgan ikkitasini olamiz. Eng qizigʻi shundaki — siz ularning ikkalasini ham
allaqachon ishlatib yuribsiz, faqat nomini bilmagansiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)ㄴ</b> bilan oʻtgan zamon aniqlovchisini yasaysiz</li>
    <li><b>(으)ㄹ</b> bilan kelasi zamon aniqlovchisini yasaysiz</li>
    <li>Uchta zamonni bitta jadvalda koʻrasiz</li>
    <li>PK-38 va PK-27 dagi qoliplarning ichida nima borligini bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Oʻtgan</span>
  <span class="pe-chip pe-chip--s">Feʼl oʻzagi</span>
  <span class="pe-chip pe-chip--v">(으)ㄴ</span>
  <span class="pe-chip pe-chip--o">Ot</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Kelasi</span>
  <span class="pe-chip pe-chip--s">Feʼl oʻzagi</span>
  <span class="pe-chip pe-chip--v">(으)ㄹ</span>
  <span class="pe-chip pe-chip--o">Ot</span>
</div>

<h3>1. Uchta zamon — bitta jadval</h3>

<p>Bu jadval butun darsning yuragi. Uni bir marta yod olsangiz, koreys grammatikasining
katta qismi ochiladi.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Oʻtgan <small>(으)ㄴ</small></th>
      <th>Hozirgi <small>는</small></th><th>Kelasi <small>(으)ㄹ</small></th></tr>
  <tr><td>먹다</td><td class="pk-res">먹은 음식</td>
      <td class="pk-uz">먹는 음식</td><td class="pk-res">먹을 음식</td></tr>
  <tr><td></td><td><small>yegan taom</small></td>
      <td><small>yeydigan taom</small></td><td><small>yeydigan (hali yemagan) taom</small></td></tr>
  <tr><td>가다</td><td class="pk-res">간 사람</td>
      <td class="pk-uz">가는 사람</td><td class="pk-res">갈 사람</td></tr>
  <tr><td>보다</td><td class="pk-res">본 영화</td>
      <td class="pk-uz">보는 영화</td><td class="pk-res">볼 영화</td></tr>
  <tr><td>읽다</td><td class="pk-res">읽은 책</td>
      <td class="pk-uz">읽는 책</td><td class="pk-res">읽을 책</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">어제 <span class="pe-hl pe-hl--v">본</span> 영화가 재미있었어요.</p>
  <p class="pe-ex__uz">Kecha koʻrgan kino qiziq boʻldi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">내일 <span class="pe-hl pe-hl--v">볼</span> 영화를 정했어요.</p>
  <p class="pe-ex__uz">Ertaga koʻradigan kinoni belgilab qoʻydim.</p>
</div>

<h3>2. 받침 ayrisi — ikkalasida ham bor</h3>

<p><b>(으)ㄴ</b> ham, <b>(으)ㄹ</b> ham (으) bilan boshlanadi, demak ikkalasida ham
oʻsha tanish savol: oʻzak undosh bilan tugadimi?</p>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">ㄴ</span> /
       <span class="pk-par">ㄹ</span></p>
    <p>가다 → 간 · 갈</p>
    <p>보다 → 본 · 볼</p>
    <p>하다 → 한 · 할</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">은</span> /
       <span class="pk-par">을</span></p>
    <p>먹다 → 먹은 · 먹을</p>
    <p>읽다 → 읽은 · 읽을</p>
    <p>찾다 → 찾은 · 찾을</p>
  </div>
</div>

<h3>3. Notoʻgʻri feʼllar va ㄹ oʻzaklar</h3>

<p>(으) unli bilan boshlanadi — demak PK-32 dagi oʻzgarishlar ikkalasida ham ishlaydi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Oʻtgan</th><th>Hozirgi</th><th>Kelasi</th></tr>
  <tr><td>듣다</td><td class="pk-res">들은</td>
      <td class="pk-uz">듣는</td><td class="pk-res">들을</td></tr>
  <tr><td>걷다</td><td class="pk-res">걸은</td>
      <td class="pk-uz">걷는</td><td class="pk-res">걸을</td></tr>
  <tr><td>돕다</td><td class="pk-res">도운</td>
      <td class="pk-uz">돕는</td><td class="pk-res">도울</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p>Oʻrtadagi ustunga qarang: <b>듣는</b>, <b>걷는</b>, <b>돕는</b> — hech nima
  oʻzgarmagan. 는 undosh, (으)ㄴ va (으)ㄹ esa unli. Bu — kursning eng koʻp
  takrorlanadigan qoidasi, va bu darsda u bir jadvalda koʻrinib turibdi.</p>
</div>

<p><b>ㄹ</b> oʻzaklar: oʻtganda ㄹ tushadi, kelasida esa bitta ㄹ boʻlib qoladi.</p>

<ul>
  <li>살다 → <b>산</b> 집 (yashagan uy) · <b>살</b> 집 (yashaydigan uy)</li>
  <li>만들다 → <b>만든</b> 음식 (tayyorlangan taom) · <b>만들</b> 음식</li>
  <li>알다 → <b>안</b> 사실 (bilib olingan haqiqat) · <b>알</b> 사실</li>
</ul>

<h3>4. Siz buni allaqachon ishlatgansiz</h3>

<p>Endi eng yoqimli qismi. Eslang, PK-38 da nima oʻrgandingiz?</p>

<div class="pe-ex">
  <p class="pe-ex__ko">밥을 <span class="pe-hl pe-hl--v">먹은</span> 후에
     커피를 마셔요.</p>
  <p class="pe-ex__uz">Ovqat yegandan keyin qahva ichaman.</p>
  <p class="pe-ex__why">후 — bu ot, “keyin” degani. Yaʼni 먹은 후 = “yegan
  keyin(gi payt)”. Bugungi (으)ㄴ ning aynan oʻzi!</p>
</div>

<p>Xuddi shunday, PK-27 dagi <b>(으)ㄹ 거예요</b> ham shu qolipdan yasalgan:
<b>거</b> — ot (“narsa”), demak 갈 거예요 = “boradigan narsa(m) bor”, yaʼni
“boraman”. U otning toʻliq shakli <b>것</b> boʻlib, uni <b>PK-46</b> da
oʻrganasiz.</p>

<div class="pe-call pe-rule">
  <p><b>Xulosa:</b> koreys tilida juda koʻp “grammatika qoliplari” aslida
  <em>aniqlovchi + ot</em> dan iborat. Aniqlovchini bilsangiz, ular bir-bir
  ochiladi va yodlash kerak boʻlgan narsa keskin kamayadi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha juftliklari.</b> (으)ㄴ ≈ “-<em>gan</em>” (koʻr<b>gan</b> kino,
  oʻqi<b>gan</b> kitob) — deyarli mukammal moslik. 는 ≈ “-<em>adigan</em> /
  -<em>yotgan</em>”. (으)ㄹ ≈ “-<em>adigan</em>” (hali boʻlmagan ish haqida) yoki
  “-<em>ajak</em>”. Diqqat qiling: oʻzbekchada “-adigan” ikki joyda chiqadi —
  hozirgi odat va kelasi zamon uchun. Koreyschada ular ikki xil: 는 va (으)ㄹ.
  Shuning uchun oʻzbekchadan tarjima qilayotganda oʻzingizga savol bering:
  <em>bu ish allaqachon boʻlyaptimi yoki hali boʻlmaganmi?</em></p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu yerda oʻzbek tili sizga tayyor kalit beradi.</b> “Ovqat ye<em>gan</em>dan
  keyin” — bu jumlaning ichida ham aniqlovchi bor: “ye<b>gan</b>”. Yaʼni oʻzbekchada
  ham “keyin” otga yopishgan, oldida esa “-gan” shakli turibdi. Koreyscha 먹은 후에
  bilan tuzilishi <b>bir xil</b>. Shuning uchun koreyscha qolipni yodlash oʻrniga uni
  boʻlaklarga ajrating — oʻzbekcha ham xuddi shunday ajraladi.</p>
</div>

<h3>5. (으)ㄹ ning oʻz maʼnosi</h3>

<p><b>(으)ㄹ</b> faqat kelasi zamon emas — u umuman <em>hali sodir boʻlmagan</em>
ishni bildiradi. Shuning uchun u koʻp foydali iboralarda uchraydi:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h">할 일</p>
    <p>qilinadigan ish, vazifa</p></div>
  <div class="pe-card"><p class="pe-card__h">먹을 것</p>
    <p>yeydigan narsa, yegulik</p></div>
  <div class="pe-card"><p class="pe-card__h">읽을 책</p>
    <p>oʻqiladigan kitob</p></div>
  <div class="pe-card"><p class="pe-card__h">만날 사람</p>
    <p>uchrashiladigan odam</p></div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">오늘 <span class="pe-hl pe-hl--v">할</span> 일이 많아요.</p>
  <p class="pe-ex__uz">Bugun qiladigan ishim koʻp.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>할 일 · 먹을 것 — oʻzbekchada ham ikki boʻlak.</b> “Qil<em>adigan</em> ish”,
  “ye<em>ydigan</em> narsa” — aniqlovchi + ot. Koreyschada 할 + 일, 먹을 + 것.
  Soʻz tartibi ham, tuzilishi ham bir xil, faqat qoʻshimchalar boshqa. Bu iboralar
  kundalik nutqda juda koʻp uchraydi, shuning uchun ularni oʻzbekchadan
  koʻchirib oʻrganing — tez esda qoladi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>어제 봤은 영화</s></p>
  <p class="pe-good">어제 <b>본</b> 영화</p>
  <p><small>Aniqlovchi ichiga zamon qoʻshimchasi qoʻyilmaydi. Zamonni
  aniqlovchining <b>oʻz shakli</b> bildiradi: (으)ㄴ.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad">음악을 <s>듣은</s> 후에 커피를 마셨어요.</p>
  <p class="pe-good">음악을 <b>들은</b> 후에 커피를 마셨어요.</p>
  <p><small>듣다 — ㄷ notoʻgʻri feʼli. (으)ㄴ unli bilan boshlanadi, shuning
  uchun ㄷ → ㄹ.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>서울에 살은 친구</s></p>
  <p class="pe-good">서울에 <b>산</b> 친구</p>
  <p><small>ㄹ oʻzak ㄴ oldida ㄹ ni yoʻqotadi: 살 + ㄴ → 산.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>내일 먹은 음식을 샀어요.</s></p>
  <p class="pe-good">내일 <b>먹을</b> 음식을 샀어요.</p>
  <p><small>Ish hali boʻlmagan → (으)ㄹ. 먹은 음식 “yeb boʻlingan taom”
  degani.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 어제 <span class="pe-blank"></span>
  (읽다) 책이 재미있었어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>읽은</b> — 읽 da 받침 bor → 은. Ish tugagan → oʻtgan zamon aniqlovchisi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 내일 <span class="pe-blank"></span>
  (만나다) 사람이 누구예요?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>만날</b> — 만나 da 받침 yoʻq → ㄹ. Ish hali boʻlmagan → (으)ㄹ.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Uchta shaklni ayting: 듣다 + 음악.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>들은 음악</b> (tinglangan) · <b>듣는 음악</b> (tinglanadigan, hozirgi) ·
    <b>들을 음악</b> (tinglanadigan, hali tinglanmagan). Oʻrtadagisi
    oʻzgarmaydi — 는 undosh.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Xatoni toping:
  <s>어제 갔은 식당이 좋았어요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>어제 간 식당이 좋았어요.</b> Aniqlovchi ichiga 았/었
    qoʻyilmaydi; 가 da 받침 yoʻq → 간.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Koreyschaga oʻgiring: “Bugun qiladigan
  ishim koʻp.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>오늘 할 일이 많아요.</b> 하다 → 할 (받침 yoʻq), 일 — “ish”.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> 먹은 후에 dagi 은 — bu nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Bu — bugungi <b>oʻtgan zamon aniqlovchisi</b>. 후 esa “keyin” degan ot.
    Yaʼni PK-38 da siz aniqlovchini nomini bilmasdan ishlatgansiz.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>동사 + (으)ㄴ</b> — …gan (oʻtgan zamon aniqlovchisi)</li>
  <li><b>동사 + (으)ㄹ</b> — …adigan (hali boʻlmagan ish)</li>
  <li><b>할 일</b> — qilinadigan ish, vazifa</li>
  <li><b>먹을 것</b> — yegulik</li>
  <li><b>영화</b> — kino</li>
  <li><b>정하다</b> — belgilamoq, qaror qilmoq</li>
  <li><b>사실</b> — haqiqat, fakt</li>
  <li><b>식당</b> — oshxona, restoran</li>
  <li><b>일</b> — ish; kun</li>
  <li><b>찾다</b> — qidirmoq, topmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li>Feʼl aniqlovchisining uch zamoni: <b>(으)ㄴ</b> (oʻtgan) · <b>는</b>
      (hozirgi) · <b>(으)ㄹ</b> (hali boʻlmagan).</li>
    <li>받침 yoʻq → ㄴ / ㄹ · 받침 bor → 은 / 을.</li>
    <li>(으) unli, shuning uchun notoʻgʻri feʼllar ishlaydi: 들은, 들을 —
      lekin 듣는 oʻzgarmaydi.</li>
    <li>ㄹ oʻzak: 살다 → 산 (oʻtgan), 살 (kelasi).</li>
    <li>Aniqlovchi ichiga <b>았/었</b> qoʻyilmaydi: <s>봤은</s> emas, <b>본</b>.</li>
    <li>PK-38 dagi <b>(으)ㄴ 후에</b> va PK-27 dagi <b>(으)ㄹ 거예요</b> — aynan
      shu aniqlovchilar.</li>
    <li>Oʻzbekcha: (으)ㄴ ≈ “-gan”, 는 ≈ “-yotgan/-adigan”, (으)ㄹ ≈ hali
      boʻlmagan “-adigan”.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-45: Aniqlovchi 3: 형용사 + (으)ㄴ",
        "category": "korean",
        "order": 45,
        "summary": (
            "“Yaxshi odam”, “issiq choy”, “achchiq taom”. Sifatlar otdan oldin "
            "turishi uchun (으)ㄴ oladi — va nega bu feʼlning oʻtgan zamoni bilan "
            "bir xil koʻrinadi."
        ),
        "stories": ["우리 동네에서 제일 좋은 곳"],
        "content": """
<h2>PK-45: Aniqlovchi 3: 형용사 + (으)ㄴ</h2>

<p>“Yaxshi odam.” “Katta uy.” “Issiq choy.” Oʻzbek tilida sifat otning oldiga
shundoq turib oladi — hech qanday qoʻshimcha kerak emas. Koreys tilida esa
kerak. 좋다 (“yaxshi boʻlmoq”) — bu aslida <em>feʼlga oʻxshash</em> soʻz, va
otni aniqlash uchun u <b>(으)ㄴ</b> shaklini olishi shart: 좋<b>은</b> 사람.
Bu — modda aniqlovchi tizimining oxirgi qismi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Sifatlarni <b>(으)ㄴ</b> bilan aniqlovchiga aylantirasiz</li>
    <li>ㅂ notoʻgʻri sifatlarini toʻgʻri yasaysiz — ular juda koʻp</li>
    <li>Feʼlning oʻtgan zamoni bilan aralashtirmaslikni oʻrganasiz</li>
    <li><b>어떤</b> bilan “qanaqa?” deb soʻraysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">Sifat oʻzagi</span>
  <span class="pe-chip pe-chip--v">(으)ㄴ</span>
  <span class="pe-chip pe-chip--o">Ot</span>
</div>

<h3>1. Yasalishi</h3>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">ㄴ</span></p>
    <p>예쁘다 → 예쁜 · 크다 → 큰 · 바쁘다 → 바쁜</p>
    <p>비싸다 → 비싼 · 싸다 → 싼</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">은</span></p>
    <p>좋다 → 좋은 · 작다 → 작은 · 많다 → 많은</p>
    <p>넓다 → 넓은 · 높다 → 높은</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 <span class="pe-hl pe-hl--adv">작은</span> 카페를
     좋아해요.</p>
  <p class="pe-ex__uz">Men kichkina kafelarni yaxshi koʻraman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">이 식당은 <span class="pe-hl pe-hl--adv">싼</span> 음식이
     많아요.</p>
  <p class="pe-ex__uz">Bu oshxonada arzon taomlar koʻp.</p>
</div>

<h3>2. 하다 sifatlari — eng oson guruh</h3>

<p>Koreys tilidagi sifatlarning katta qismi <b>하다</b> bilan tugaydi. Ularning
hammasi bir xil ishlaydi: 하 → <b>한</b>.</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h">조용하다 → 조용한</p>
    <p>tinch, sokin</p></div>
  <div class="pe-card"><p class="pe-card__h">깨끗하다 → 깨끗한</p>
    <p>toza</p></div>
  <div class="pe-card"><p class="pe-card__h">따뜻하다 → 따뜻한</p>
    <p>issiq, iliq</p></div>
  <div class="pe-card"><p class="pe-card__h">유명하다 → 유명한</p>
    <p>mashhur</p></div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--adv">조용한</span> 카페에서
     공부하고 있어요.</p>
  <p class="pe-ex__uz">Tinch kafeda dars qilyapman.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Rostini aytamiz: bu yerda koreys tili oʻzbekchadan qiyinroq.</b> Oʻzbekchada
  sifat otning oldiga hech qanday qoʻshimchasiz turadi — “<em>yaxshi</em> odam”,
  “<em>katta</em> uy”, “<em>sovuq</em> havo”. Koreyschada esa har safar (으)ㄴ
  qoʻshish kerak: 좋<b>은</b> 사람, 큰 집, 추<b>운</b> 날씨. Bu — oʻzbek oʻquvchi
  eng koʻp unutadigan qoʻshimcha, chunki ona tilida uning oʻrni boʻsh. Shuning
  uchun yangi sifat oʻrganganingizda uni <b>darrov aniqlovchi shaklida</b> ham
  yodlang: 춥다 / 추운, 맵다 / 매운.</p>
</div>

<h3>3. ㅂ notoʻgʻri sifatlari — bu yerda ular juda koʻp</h3>

<p>PK-32 da oʻrgangan ㅂ oʻzgarishi eng koʻp aynan sifatlarda uchraydi.
Quyidagi jadval — kundalik nutqning yarmi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Sifat</th><th>Maʼnosi</th><th>Aniqlovchi</th><th>Misol</th></tr>
  <tr><td>춥다</td><td class="pk-uz">sovuq</td>
      <td class="pk-res">추운</td><td>추운 날씨</td></tr>
  <tr><td>덥다</td><td class="pk-uz">issiq</td>
      <td class="pk-res">더운</td><td>더운 여름</td></tr>
  <tr><td>맵다</td><td class="pk-uz">achchiq</td>
      <td class="pk-res">매운</td><td>매운 음식</td></tr>
  <tr><td>쉽다</td><td class="pk-uz">oson</td>
      <td class="pk-res">쉬운</td><td>쉬운 문제</td></tr>
  <tr><td>어렵다</td><td class="pk-uz">qiyin</td>
      <td class="pk-res">어려운</td><td>어려운 시험</td></tr>
  <tr><td>가볍다</td><td class="pk-uz">yengil</td>
      <td class="pk-res">가벼운</td><td>가벼운 가방</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p>Qoida bitta: <b>ㅂ → 우</b>, keyin ㄴ qoʻshiladi. 춥 → 추우 → <b>추운</b>.
  Buni bir marta tushunsangiz, oltitasini ham alohida yodlashning hojati yoʻq.</p>
</div>

<p><b>ㄹ</b> bilan tugagan sifatlar ㄹ ni yoʻqotadi: 길다 → <b>긴</b> (uzun),
멀다 → <b>먼</b> (uzoq), 달다 → <b>단</b> (shirin).</p>

<h3>4. Eng muhim chalkashlik: 좋은 사람 va 먹은 사람</h3>

<p>Diqqat qiling — ikkalasi ham <b>(으)ㄴ</b>. Lekin maʼnolari butunlay boshqa:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">먹<b>은</b> 사람 — FEʼL</p>
    <p>먹다 — <em>harakat</em>.</p>
    <p>(으)ㄴ bu yerda <b>oʻtgan zamon</b> bildiradi.</p>
    <p>“Ye<b>gan</b> odam” — ish tugagan.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">좋<b>은</b> 사람 — SIFAT</p>
    <p>좋다 — <em>xususiyat</em>.</p>
    <p>(으)ㄴ bu yerda <b>hozirgi zamon</b> bildiradi.</p>
    <p>“Yaxshi odam” — doimiy holat.</p>
  </div>
</div>

<div class="pe-call pe-rule">
  <p><b>Qoida:</b> shakl bir xil, maʼnoni <em>soʻzning turi</em> hal qiladi.
  Feʼl boʻlsa — oʻtgan zamon. Sifat boʻlsa — hozirgi zamon. Shuning uchun
  koreys tilida yangi soʻz oʻrganayotganda uning <b>feʼlmi yoki sifatmi</b>
  ekanini ham yodlab qoʻying.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Tekshirishning oson yoʻli — oʻzbekcha tarjima.</b> Agar soʻz
  oʻzbekchada <em>sifat</em> boʻlib chiqsa (yaxshi, katta, chiroyli, sovuq,
  achchiq) — u koreyschada ham 형용사. Agar <em>harakat</em> boʻlsa (yemoq,
  bormoq, oʻqimoq) — 동사. Bu tekshiruv deyarli har doim toʻgʻri ishlaydi, va
  bu yerda oʻzbek tili sizga ingliz tilidan koʻra koʻproq yordam beradi:
  ingliz tilida “good” va “ate” orasida hech qanday umumiy shakl yoʻq, shuning
  uchun ingliz tilidan oʻrganuvchi bu chalkashlikni umuman koʻrmaydi va keyin
  xato qiladi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>ㅂ sifatlari nega shunchalik muhim?</b> Yuqoridagi oltitasiga qarang:
  sovuq, issiq, achchiq, oson, qiyin, yengil. Bular — ob-havo, taom va dars
  haqidagi gaplarning yuragi, yaʼni siz ular haqida <em>har kuni</em> gapirasiz.
  Oʻzbekchada ham bu soʻzlar eng koʻp ishlatiladiganlar qatorida. Shuning uchun
  bitta qoida (ㅂ → 우) sizga darhol foyda beradi — uni bilmasangiz, eng oddiy
  gaplaringiz ham notoʻgʻri chiqadi.</p>
</div>

<h3>5. Sifat 는 olmaydi</h3>

<p>PK-43 da siz <b>는</b> ni oʻrgandingiz. U <b>faqat feʼllar</b> uchun.
Sifat hech qachon 는 olmaydi:</p>

<div class="pe-fix">
  <p class="pe-bad"><s>예쁘는 사람</s></p>
  <p class="pe-good"><b>예쁜</b> 사람</p>
  <p><small>예쁘다 — sifat, shuning uchun (으)ㄴ.</small></p>
</div>

<p>Bitta istisno bor va u tanish: <b>있다 / 없다</b> ichida boʻlgan soʻzlar
(재미있다, 맛있다, 멋있다) <b>는</b> oladi — 재미있는 책, 맛있는 음식.
Chunki ularning ichida feʼl turibdi.</p>

<h3>6. 어떤 — “qanaqa?”</h3>

<p>Endi sifat aniqlovchisi bor ekan, uni soʻraydigan soʻz ham kerak:</p>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--adv">어떤</span> 음식을
     좋아해요?</p>
  <p class="pe-ex__uz">Qanaqa taomlarni yaxshi koʻrasiz?</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">— <span class="pe-hl pe-hl--adv">매운</span> 음식을
     좋아해요.</p>
  <p class="pe-ex__uz">— Achchiq taomlarni yaxshi koʻraman.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>추울 날씨</s></p>
  <p class="pe-good"><b>추운</b> 날씨</p>
  <p><small>Sifat aniqlovchisi — (으)ㄴ, (으)ㄹ emas. 춥 → 추우 → 추운.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>맵은 음식</s></p>
  <p class="pe-good"><b>매운</b> 음식</p>
  <p><small>맵다 — ㅂ notoʻgʻri sifati: ㅂ → 우.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>길은 머리</s></p>
  <p class="pe-good"><b>긴</b> 머리</p>
  <p><small>ㄹ oʻzak ㄴ oldida ㄹ ni yoʻqotadi: 길 + ㄴ → 긴.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>재미있은 영화</s></p>
  <p class="pe-good"><b>재미있는</b> 영화</p>
  <p><small>재미있다 ichida 있다 (feʼl) bor → 는 oladi.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: <span class="pe-blank"></span>
  (조용하다) 곳에서 공부하고 싶어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>조용한</b> — 하다 sifatlari 한 boʻladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 오늘은 <span class="pe-blank"></span>
  (춥다) 날씨예요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>추운</b> — ㅂ → 우, keyin ㄴ: 춥 → 추우 → 추운.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Farqini ayting: 먹은 사람 va 좋은 사람.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>먹은 사람</b> — “yegan odam” (먹다 feʼl → oʻtgan zamon).
    <b>좋은 사람</b> — “yaxshi odam” (좋다 sifat → hozirgi zamon).
    Shakl bir xil, soʻzning turi hal qiladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Xatoni toping: <s>예쁘는 옷을 샀어요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>예쁜 옷을 샀어요.</b> 는 faqat feʼllar uchun; 예쁘다 —
    sifat, (으)ㄴ oladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Koreyschaga oʻgiring: “Men achchiq
  taomlarni yaxshi koʻraman.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>저는 매운 음식을 좋아해요.</b> 맵다 → 매운 (ㅂ → 우).</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Nega 맛있는 emas, 맛있은 emas?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>맛있다 = 맛 + 있다, yaʼni ichida <b>있다</b> — feʼl bor. Feʼllar
    hozirgi zamonda <b>는</b> oladi. Shuning uchun <b>맛있는 음식</b>.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>형용사 + (으)ㄴ</b> — sifat aniqlovchisi</li>
  <li><b>어떤</b> — qanaqa, qanday</li>
  <li><b>춥다 / 덥다</b> — sovuq / issiq</li>
  <li><b>맵다</b> — achchiq</li>
  <li><b>쉽다 / 어렵다</b> — oson / qiyin</li>
  <li><b>조용하다 / 깨끗하다</b> — tinch / toza</li>
  <li><b>유명하다</b> — mashhur</li>
  <li><b>길다 / 멀다</b> — uzun / uzoq</li>
  <li><b>비싸다 / 싸다</b> — qimmat / arzon</li>
  <li><b>날씨</b> — ob-havo</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li>Sifat otdan oldin turishi uchun <b>(으)ㄴ</b> oladi: 좋은 사람.</li>
    <li>받침 yoʻq → ㄴ · 받침 bor → 은 · 하다 sifatlari → 한.</li>
    <li>ㅂ sifatlari: ㅂ → 우 → ㄴ. 춥다 → 추운, 맵다 → 매운, 어렵다 → 어려운.</li>
    <li>ㄹ oʻzak ㄹ ni yoʻqotadi: 길다 → 긴, 멀다 → 먼.</li>
    <li><b>Sifat 는 olmaydi</b> — 는 faqat feʼllar uchun.</li>
    <li>Istisno: 재미있다 / 맛있다 / 멋있다 — ichida 있다 bor, 는 oladi.</li>
    <li>먹은 사람 (feʼl → oʻtgan) va 좋은 사람 (sifat → hozirgi) — shakl bir xil,
      soʻz turi hal qiladi.</li>
    <li><b>어떤</b> bilan soʻralsa, javobda sifat aniqlovchisi keladi.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-46: Otlashtirish: 는 것, 기, (으)ㅁ",
        "category": "korean",
        "order": 46,
        "summary": (
            "TOPIK varaqasidagi 읽기 · 듣기 · 쓰기 · 말하기 — bular nima? Feʼlni "
            "otga aylantirishning uch yoʻli va qaysi biri qachon ishlatiladi."
        ),
        "stories": ["한국어 배우는 것이 재미있어요"],
        "content": """
<h2>PK-46: Otlashtirish: 는 것, 기, (으)ㅁ</h2>

<p>TOPIK imtihonining varaqasiga qarasangiz, toʻrtta soʻz koʻrasiz:
<b>읽기 · 듣기 · 쓰기 · 말하기</b>. Bu — “oʻqish · tinglash · yozish · gapirish”.
Eʼtibor bering: 읽다 “oʻqimoq” feʼl edi, 읽<b>기</b> esa ot boʻlib qoldi — xuddi
oʻzbekcha “oʻqi<em>moq</em>” → “oʻqi<b>sh</b>” kabi. Feʼlni otga aylantirish
<b>otlashtirish</b> deyiladi, va koreys tilida buning uchta yoʻli bor. Bugun
uchalasini ham koʻramiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>는 것</b> bilan butun gapni otga aylantirasiz</li>
    <li><b>기</b> ning qayerda ishlatilishini bilib olasiz</li>
    <li><b>(으)ㅁ</b> ni tanib olasiz</li>
    <li><b>것 → 게 / 걸</b> qisqarishlarini oʻqiy olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Eng koʻp</span>
  <span class="pe-chip pe-chip--s">Aniqlovchi</span>
  <span class="pe-chip pe-chip--o">것</span>
  <span class="pe-chip pe-chip--adv">= “…adigan narsa / …ish”</span>
</div>

<h3>1. 것 — bu shunchaki ot</h3>

<p><b>것</b> “narsa” degan oddiy ot. Uning kuchi shundaki, oldiga <em>istalgan
aniqlovchi</em> qoʻyish mumkin — va PK-43, PK-44 dan siz aniqlovchining uchala
zamonini ham bilasiz.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Shakl</th><th>Zamoni</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-res">먹는 것</td><td class="pk-uz">hozirgi</td>
      <td>yeyish; yeyiladigan narsa</td></tr>
  <tr><td class="pk-res">먹은 것</td><td class="pk-uz">oʻtgan</td>
      <td>yegan narsa</td></tr>
  <tr><td class="pk-res">먹을 것</td><td class="pk-uz">hali boʻlmagan</td>
      <td>yegulik, yeyiladigan narsa</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">한국어를 <span class="pe-hl pe-hl--v">배우는 것</span>이
     재미있어요.</p>
  <p class="pe-ex__uz">Koreys tilini oʻrganish qiziqarli.</p>
  <p class="pe-ex__why">배우는 것 — butun bir gap otga aylandi va ega boʻlib
  turibdi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">제가 <span class="pe-hl pe-hl--v">좋아하는 것</span>은
     음악이에요.</p>
  <p class="pe-ex__uz">Men yaxshi koʻradigan narsa — musiqa.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha ikki xil tarjima qilinadi.</b> 배우는 것 baʼzan
  “oʻrgan<em>ish</em>” (ish-harakat), baʼzan “oʻrgan<em>adigan narsa</em>”
  (predmet) boʻladi. Qaysi biri ekanini gap oʻzi koʻrsatadi: 배우는 것이
  재미있어요 → “oʻrganish qiziqarli”; 배우는 것이 많아요 → “oʻrganadigan narsa
  koʻp”. Oʻzbek tilida ham “oʻqish” soʻzi shunday ikki maʼnoli — “oʻqish
  foydali” va “oʻqishga bordi”. Yaʼni bu ikki maʼnolilik siz uchun yangi emas.</p>
</div>

<h3>2. 것 → 게 · 걸 (qisqargan shakllar)</h3>

<p>Ogʻzaki nutqda 것 qoʻshimchalar bilan qoʻshilib qisqaradi. Bu shakllarni
albatta tanib olishingiz kerak — koreyslar deyarli har doim shunday gapiradi:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h">것이 → 게</p>
    <p>먹는 것이 → 먹는 <b>게</b></p></div>
  <div class="pe-card"><p class="pe-card__h">것을 → 걸</p>
    <p>먹는 것을 → 먹는 <b>걸</b></p></div>
  <div class="pe-card"><p class="pe-card__h">것은 → 건</p>
    <p>먹는 것은 → 먹는 <b>건</b></p></div>
  <div class="pe-card"><p class="pe-card__h">것이에요 → 거예요</p>
    <p>갈 것이에요 → 갈 <b>거예요</b></p></div>
</div>

<div class="pe-call pe-rule">
  <p><b>Oxirgi katakka qarang.</b> PK-27 da siz <b>(으)ㄹ 거예요</b> ni tayyor
  qolip sifatida yodladingiz. Endi uning ichi koʻrinib turibdi:
  <b>갈 것이에요</b> = “boradigan narsa(m) bor” = “boraman”. Koreys tilida
  yodlash kerak boʻlgan “qolip”larning koʻpchiligi shunday — aniqlovchi + ot +
  qoʻshimcha.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Qisqarishdan qoʻrqmang — oʻzbekchada ham shunday.</b> Biz yozganda “nima
  qilyapsan” deymiz, gapirganda esa “nima qivossan”. Darslikda 것이 yozilgani bilan
  koreyslar 게 deb gapiradi — bu xuddi shu farq. Yozma shaklni <b>tanib olish</b>
  uchun, ogʻzaki shaklni esa <b>eshitib tushunish</b> uchun biling. Oʻzingiz
  gapirganda ikkalasi ham toʻgʻri, lekin 게 · 걸 tabiiyroq eshitiladi.</p>
</div>

<h3>3. 기 — TOPIK varaqasidagi shakl</h3>

<p><b>기</b> feʼlni sof otga aylantiradi. U 것 dan farqli oʻlaroq <em>butun
gapni</em> emas, koʻproq <em>ish-harakatning nomini</em> beradi:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h">읽기</p><p>oʻqish</p></div>
  <div class="pe-card"><p class="pe-card__h">듣기</p><p>tinglash</p></div>
  <div class="pe-card"><p class="pe-card__h">쓰기</p><p>yozish</p></div>
  <div class="pe-card"><p class="pe-card__h">말하기</p><p>gapirish</p></div>
</div>

<p><b>기</b> ayniqsa quyidagi soʻzlar bilan mustahkam birikadi. Bularni bitta
boʻlak sifatida yod oling:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Qolip</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pk-res">기 쉽다</td><td class="pk-uz">…ish oson</td>
      <td>이 책은 읽기 쉬워요</td></tr>
  <tr><td class="pk-res">기 어렵다</td><td class="pk-uz">…ish qiyin</td>
      <td>한국어는 배우기 어려워요</td></tr>
  <tr><td class="pk-res">기 좋다</td><td class="pk-uz">…ish uchun yaxshi</td>
      <td>여기는 공부하기 좋아요</td></tr>
  <tr><td class="pk-res">기 시작하다</td><td class="pk-uz">…ishni boshlamoq</td>
      <td>비가 오기 시작했어요</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">이 카페는 <span class="pe-hl pe-hl--v">공부하기</span>
     좋아요.</p>
  <p class="pe-ex__uz">Bu kafe dars qilish uchun yaxshi.</p>
</div>

<div class="pe-call pe-tip">
  <p>Va yana bir tanish yuz: PK-38 dagi <b>기 전에</b>. 전 — “oldin” degan ot,
  기 esa aynan shu otlashtiruvchi. 먹<b>기</b> 전에 = “yeyish oldidan”.
  Demak siz 기 ni sakkiz dars oldin ishlatgansiz.</p>
</div>

<h3>4. (으)ㅁ — yozma va rasmiy</h3>

<p>Uchinchi yoʻl — <b>(으)ㅁ</b>. U kundalik suhbatda deyarli ishlatilmaydi;
uni koʻproq <em>lugʻat soʻzlari</em> va <em>eʼlonlar</em>da koʻrasiz.</p>

<ul>
  <li>웃다 (kulmoq) → <b>웃음</b> (kulgi)</li>
  <li>돕다 (yordam bermoq) → <b>도움</b> (yordam)</li>
  <li>있다 → <b>있음</b> · 없다 → <b>없음</b> (eʼlonlarda: “bor / yoʻq”)</li>
  <li>죽다 (oʻlmoq) → <b>죽음</b> (oʻlim)</li>
</ul>

<div class="pe-call pe-warn">
  <p>Yangi soʻz yasash uchun (으)ㅁ ni <b>oʻzingiz ishlatmang</b> — u faqat
  tayyor soʻzlarda uchraydi. Gapirganda <b>는 것</b> yoki <b>기</b> ni tanlang.</p>
</div>

<h3>5. Qaysi birini tanlash kerak?</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">는 것</p>
    <p>Eng koʻp ishlatiladigan, eng xavfsiz tanlov.</p>
    <p>Butun gapni otga aylantiradi.</p>
    <p>Zamoni bor: 는 / (으)ㄴ / (으)ㄹ 것.</p>
    <p><small>제가 좋아하는 것은…</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">기</p>
    <p>Ish-harakatning nomi.</p>
    <p>Zamoni yoʻq.</p>
    <p>Maʼlum soʻzlar bilan mustahkam birikadi.</p>
    <p><small>읽기 쉬워요 · 공부하기 좋아요</small></p>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha koʻprik: 기 ≈ “-ish”.</b> 읽기 = “oʻqi<b>sh</b>”,
  쓰기 = “yozi<b>sh</b>”, 말하기 = “gapiri<b>sh</b>”. Oʻzbek tilidagi “-ish”
  qoʻshimchasi ham aynan shu ishni qiladi: feʼldan ot yasaydi. Shuning uchun
  TOPIK varaqasidagi 읽기/듣기/쓰기/말하기 ni koʻrsangiz, ularni oʻzbekchaga
  soʻzma-soʻz koʻchiring — mos tushadi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>한국어를 배우기가 재미있어요.</s></p>
  <p class="pe-good">한국어를 <b>배우는 것이</b> 재미있어요.</p>
  <p><small>Umumiy fikr bildirayotganda 는 것 tabiiyroq. 기 maʼlum soʻzlar
  bilan (쉽다, 어렵다, 좋다, 시작하다) birikadi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>이 책은 읽는 것 쉬워요.</s></p>
  <p class="pe-good">이 책은 <b>읽기</b> 쉬워요.</p>
  <p><small>쉽다 / 어렵다 bilan doim <b>기</b> keladi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>제가 좋아하은 것</s></p>
  <p class="pe-good">제가 <b>좋아하는</b> 것</p>
  <p><small>좋아하다 — feʼl, hozirgi zamonda 는 oladi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>먹기 것이 많아요.</s></p>
  <p class="pe-good"><b>먹을 것이</b> 많아요.</p>
  <p><small>것 oldiga aniqlovchi keladi, 기 emas. “Yegulik koʻp” — 먹을 것.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 한국 노래를
  <span class="pe-blank"></span> (듣다) 것을 좋아해요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>듣는</b> — 는 undosh, shuning uchun 듣 oʻzgarmaydi: <b>듣는 것을</b>
    (ogʻzaki nutqda 듣는 걸).</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 이 문제는
  <span class="pe-blank"></span> (풀다) 쉬워요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>풀기</b> — 쉽다 bilan doim <b>기</b> keladi. (풀다 — yechmoq.)</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> 갈 거예요 ning toʻliq shakli qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>갈 것이에요.</b> 것 + 이에요 → 거예요. Yaʼni PK-27 dagi qolip aslida
    aniqlovchi + ot + 이다 dan iborat.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Xatoni toping:
  <s>이 책은 읽는 것 어려워요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>이 책은 읽기 어려워요.</b> 어렵다 bilan 기 keladi.
    (어렵다 → 어려워요, ㅂ notoʻgʻri feʼli.)</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Koreyschaga oʻgiring: “Yegulik koʻp.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>먹을 것이 많아요.</b> (Ogʻzaki: 먹을 게 많아요.) Hali yeyilmagan narsa
    → (으)ㄹ 것.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> TOPIK varaqasidagi 쓰기 va 말하기 —
  bular qanday yasalgan?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>쓰다 (yozmoq) + 기 = <b>쓰기</b> (yozish). 말하다 (gapirmoq) + 기 =
    <b>말하기</b> (gapirish). Oʻzbekchadagi “-ish” qoʻshimchasining aynan
    juftligi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>는 것</b> — …ish; …adigan narsa</li>
  <li><b>게 / 걸 / 건</b> — 것이 / 것을 / 것은 ning qisqargan shakli</li>
  <li><b>기</b> — otlashtiruvchi qoʻshimcha (“-ish”)</li>
  <li><b>기 쉽다 / 기 어렵다</b> — …ish oson / qiyin</li>
  <li><b>기 시작하다</b> — …ishni boshlamoq</li>
  <li><b>(으)ㅁ</b> — yozma otlashtirish (도움, 웃음)</li>
  <li><b>문제</b> — masala, muammo</li>
  <li><b>풀다</b> — yechmoq</li>
  <li><b>도움</b> — yordam</li>
  <li><b>말하다</b> — gapirmoq, aytmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>것</b> — oddiy ot (“narsa”). Oldiga aniqlovchi qoʻyiladi:
      먹는/먹은/먹을 것.</li>
    <li><b>는 것</b> — eng koʻp ishlatiladigan, butun gapni otga aylantiradi.</li>
    <li>Qisqarishlar: 것이 → <b>게</b>, 것을 → <b>걸</b>, 것은 → <b>건</b>,
      것이에요 → <b>거예요</b>.</li>
    <li><b>기</b> — ish-harakatning nomi: 읽기, 쓰기, 말하기 (oʻzbekcha “-ish”).</li>
    <li>기 mustahkam birikmalari: 기 쉽다 · 기 어렵다 · 기 좋다 · 기 시작하다 ·
      기 전에.</li>
    <li><b>(으)ㅁ</b> — faqat tayyor soʻzlar va eʼlonlarda: 도움, 웃음, 있음.</li>
    <li>PK-27 dagi <b>(으)ㄹ 거예요</b> = (으)ㄹ + 것 + 이에요.</li>
  </ul>
</div>
""",
    },
]
