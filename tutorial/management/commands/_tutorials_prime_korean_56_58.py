# -*- coding: utf-8 -*-
"""Prime Korean — Block E, darslar 56–58.

56. Majhul nisbat: -이/히/리/기- va 아/어지다
57. Orttirma nisbat: -이/히/리/기/우/구/추- va 게 하다
58. 아/어 버리다 — tugallanish va his-tuygʻu

Uchalasida ham oʻzbek tilida tayyor juftlik bor — bu darslarning kaliti:
  majhul nisbat   = "yoz-IL-di", "och-IL-di"      → 이/히/리/기
  orttirma nisbat = "oʻqi-T-di", "ye-DIR-di"      → 이/히/리/기/우/구/추
  아/어 버리다     = "yeb QOʻYDI", "ketib QOLDI"   → koʻmakchi feʼl

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

Oʻqish matnlari: corner/management/commands/_stories_prime_korean_56_58.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_56_58.py --author=prime
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
        "title": "PK-56: Majhul nisbat — -이/히/리/기- va 아/어지다",
        "category": "korean",
        "order": 56,
        "summary": (
            "“Eshikni ochdim” va “eshik ochildi” — oʻzbek tilida bitta qoʻshimcha "
            "farq qiladi. Koreys tilida ham xuddi shunday: 열다 → 열리다."
        ),
        "stories": ["문이 안 열려요"],
        "content": """
<h2>PK-56: Majhul nisbat — -이/히/리/기- va 아/어지다</h2>

<p>Sinfga kirdingiz, eshik oʻz-oʻzidan yopildi. Kim yopdi? Hech kim —
shamol boʻlishi mumkin. Shunday paytda oʻzbek tilida biz “eshikni
<b>yopdim</b>” demaymiz, “eshik <b>yopildi</b>” deymiz. Ish bajaruvchisi
emas, <em>ishning oʻzi</em> muhim boʻlgan gap — bu <b>majhul nisbat</b>.
Koreys tilida ham xuddi shu narsa bor, va uni yasash usuli sizga tanish
tuyuladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>-이/히/리/기-</b> qoʻshimchalari bilan majhul feʼl yasaysiz</li>
    <li>Gapdagi qoʻshimchalar qanday oʻzgarishini koʻrasiz (을/를 → 이/가)</li>
    <li><b>아/어지다</b> bilan majhul yasashni oʻrganasiz</li>
    <li><b>하다 → 되다</b> yoʻlini bilib olasiz</li>
    <li>Kundalik nutqdagi 걸리다, 막히다, 들리다 kabi gaplarni tushunasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">Feʼl oʻzagi</span>
  <span class="pe-chip pe-chip--v">이 / 히 / 리 / 기</span>
  <span class="pe-chip pe-chip--adv">= …ildi / …indi</span>
</div>

<h3>1. Oʻzbekcha juftlik — darsning kaliti</h3>

<p>Oʻzbek tilida majhul nisbat feʼlga <b>-il-</b> yoki <b>-in-</b>
qoʻshimchasini qoʻshib yasaladi. Bir qarang:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Oddiy feʼl</th><th>Majhul (oʻzbekcha)</th><th>Koreyscha</th>
      <th>Majhul (koreyscha)</th></tr>
  <tr><td>ochmoq</td><td class="pk-uz">ochildi</td>
      <td class="pk-stem">열다</td><td class="pk-res">열리다</td></tr>
  <tr><td>yopmoq</td><td class="pk-uz">yopildi</td>
      <td class="pk-stem">닫다</td><td class="pk-res">닫히다</td></tr>
  <tr><td>sotmoq</td><td class="pk-uz">sotildi</td>
      <td class="pk-stem">팔다</td><td class="pk-res">팔리다</td></tr>
  <tr><td>tutmoq</td><td class="pk-uz">tutildi</td>
      <td class="pk-stem">잡다</td><td class="pk-res">잡히다</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Shuning uchun bu dars siz uchun yarim tayyor.</b> Ingliz tilida
  majhul nisbat butunlay boshqa mashina — “was opened”, yaʼni yordamchi
  feʼl + sifatdosh, uch soʻz. Oʻzbek va koreys tilida esa bitta
  <em>qoʻshimcha</em> feʼlning ichiga kiradi: och-<b>il</b>-di ·
  열-<b>리</b>-다. Ikkala til ham agglutinativ — qoʻshimchalarni
  oʻzakka yopishtiradi. Sizga faqat qaysi qoʻshimcha qaysi feʼlga
  yopishishini yodlash qoladi.</p>
</div>

<h3>2. Toʻrtta qoʻshimcha va ularni tanlash</h3>

<p>Koreyschada toʻrtta majhul qoʻshimchasi bor: <b>이 · 히 · 리 · 기</b>.
Qaysi biri qaysi feʼlga qoʻshilishi 100% qoidaga boʻysunmaydi — yodlash
kerak. Lekin oʻzakning oxirgi tovushi juda yaxshi maslahatchi:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h">-이-</p>
    <p>oʻzak ㅎ, ㄱ, unli bilan tugasa</p>
    <p><small>보다 → 보<b>이</b>다 · 놓다 → 놓<b>이</b>다 ·
      쌓다 → 쌓<b>이</b>다 · 바꾸다 → 바<b>뀌</b>다</small></p></div>
  <div class="pe-card"><p class="pe-card__h">-히-</p>
    <p>oʻzak ㄱ, ㄷ, ㅂ bilan tugasa</p>
    <p><small>먹다 → 먹<b>히</b>다 · 닫다 → 닫<b>히</b>다 ·
      잡다 → 잡<b>히</b>다 · 막다 → 막<b>히</b>다</small></p></div>
  <div class="pe-card"><p class="pe-card__h">-리-</p>
    <p>oʻzak ㄹ bilan tugasa</p>
    <p><small>열다 → 열<b>리</b>다 · 팔다 → 팔<b>리</b>다 ·
      걸다 → 걸<b>리</b>다 · 듣다 → 들<b>리</b>다</small></p></div>
  <div class="pe-card"><p class="pe-card__h">-기-</p>
    <p>oʻzak ㄴ, ㅁ, ㅅ, ㅊ bilan tugasa</p>
    <p><small>안다 → 안<b>기</b>다 · 끊다 → 끊<b>기</b>다 ·
      씻다 → 씻<b>기</b>다 · 쫓다 → 쫓<b>기</b>다</small></p></div>
</div>

<div class="pe-call pe-rule">
  <p><b>Diqqat: bu roʻyxat yopiq.</b> Majhul nisbat koreys tilida faqat
  <em>maʼlum feʼllarda</em> bor. Istagan feʼlga 이/히/리/기 qoʻshib
  boʻlmaydi — koreyslar bunday soʻzni tushunmaydi. Shuning uchun bu
  darsda yangi qoida emas, <b>yangi soʻzlar</b> yodlanadi. Qolganlari
  uchun 3-boʻlimdagi 아/어지다 bor.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--s">문이</span>
     <span class="pe-hl pe-hl--v">열렸어요</span>.</p>
  <p class="pe-ex__uz">Eshik ochildi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">밖에서 <span class="pe-hl pe-hl--s">음악 소리가</span>
     <span class="pe-hl pe-hl--v">들려요</span>.</p>
  <p class="pe-ex__uz">Tashqaridan musiqa ovozi eshitilyapti.</p>
  <p class="pe-ex__why">듣다 → 들리다. “Men eshitaman” emas — ovoz
  <em>oʻzi</em> eshitiladi.</p>
</div>

<h3>3. Gapdagi qoʻshimchalar qanday oʻzgaradi</h3>

<p>Majhul nisbat — bu faqat feʼlning oʻzgarishi emas. Gapning ichi ham
qayta joylashadi: <b>toʻldiruvchi ega boʻlib qoladi</b>.</p>

<div class="pe-steps">
  <div class="pe-step">
    <p><b>1. Oddiy gap.</b> Bajaruvchi — ega, ish — toʻldiruvchi.<br>
    <span class="pe-hl pe-hl--s">고양이가</span>
    <span class="pe-hl pe-hl--o">쥐를</span>
    <span class="pe-hl pe-hl--v">잡았어요</span>. — Mushuk sichqonni tutdi.</p>
  </div>
  <div class="pe-step">
    <p><b>2. 을/를 → 이/가.</b> Toʻldiruvchi egaga aylanadi.<br>
    <span class="pe-hl pe-hl--s">쥐가</span> … — Sichqon…</p>
  </div>
  <div class="pe-step">
    <p><b>3. Eski ega → 에게 / 한테 (jonli), 에 (jonsiz).</b><br>
    쥐가 <span class="pe-hl pe-hl--adv">고양이에게</span>
    <span class="pe-hl pe-hl--v">잡혔어요</span>. — Sichqon mushukka tutildi.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">창문이 <span class="pe-hl pe-hl--adv">바람에</span>
     <span class="pe-hl pe-hl--v">닫혔어요</span>.</p>
  <p class="pe-ex__uz">Deraza shamoldan yopildi.</p>
  <p class="pe-ex__why">바람 — jonsiz, shuning uchun 에게 emas,
  <b>에</b>.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu ham oʻzbekchaga oʻxshaydi.</b> “Sichqon mushuk<b>ka</b> tutildi”
  — biz ham bajaruvchini <em>joʻnalish kelishigi</em>ga qoʻyamiz.
  Koreysning 에게/한테 si aynan shu vazifada turibdi. Faqat bitta farq
  bor: koreys tili jonli va jonsizni ajratadi — odam yoki hayvon boʻlsa
  <b>에게/한테</b>, shamol, yomgʻir, qor boʻlsa <b>에</b>.</p>
</div>

<h3>4. 아/어지다 — hamma feʼl uchun ochiq yoʻl</h3>

<p>Feʼlda 이/히/리/기 shakli boʻlmasa, majhul <b>아/어 + 지다</b> bilan
yasaladi. Yasalishi PK-18 dagi 아/어요 bilan bir xil — oʻzakning
oxirgi unlisiga qarang:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Oʻzak</th><th>Qoʻshimcha</th><th>Natija</th>
      <th>Maʼnosi</th></tr>
  <tr><td>만들다</td><td class="pk-stem">만들</td><td class="pk-end">어지다</td>
      <td class="pk-res">만들어지다</td><td class="pk-uz">yasaladi</td></tr>
  <tr><td>켜다</td><td class="pk-stem">켜</td><td class="pk-end">지다</td>
      <td class="pk-res">켜지다</td><td class="pk-uz">yonadi (chiroq)</td></tr>
  <tr><td>끄다</td><td class="pk-stem">끄</td><td class="pk-end">어지다</td>
      <td class="pk-res">꺼지다</td><td class="pk-uz">oʻchadi</td></tr>
  <tr><td>쓰다</td><td class="pk-stem">쓰</td><td class="pk-end">어지다</td>
      <td class="pk-res">써지다</td><td class="pk-uz">yoziladi</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">이 빵은 우유로 <span class="pe-hl pe-hl--v">만들어져요</span>.</p>
  <p class="pe-ex__uz">Bu non sutdan tayyorlanadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">갑자기 <span class="pe-hl pe-hl--s">불이</span>
     <span class="pe-hl pe-hl--v">꺼졌어요</span>.</p>
  <p class="pe-ex__uz">Toʻsatdan chiroq oʻchdi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>지다</b> sifatlar bilan ham ishlaydi, lekin u yerda maʼnosi
  boshqa — “…lashmoq, …bormoq”: 좋다 → <b>좋아지다</b> (yaxshilanmoq),
  춥다 → <b>추워지다</b> (sovib bormoq), 예쁘다 → <b>예뻐지다</b>
  (chiroyli boʻlib bormoq). Feʼl bilan — majhul, sifat bilan —
  oʻzgarish. Ikkalasini ham eslab qoling.</p>
</div>

<h3>5. 하다 feʼllari uchun: 되다</h3>

<p>하다 bilan tugaydigan feʼllar (PK darslarida koʻp uchragan
공부하다, 시작하다, 준비하다…) majhulga <b>되다</b> bilan oʻtadi:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h">시작하다 → 시작되다</p>
    <p>boshlamoq → boshlanmoq</p></div>
  <div class="pe-card"><p class="pe-card__h">준비하다 → 준비되다</p>
    <p>tayyorlamoq → tayyorlanmoq</p></div>
  <div class="pe-card"><p class="pe-card__h">사용하다 → 사용되다</p>
    <p>ishlatmoq → ishlatilmoq</p></div>
  <div class="pe-card"><p class="pe-card__h">걱정하다 → 걱정되다</p>
    <p>xavotirlanmoq → xavotir tugʻilmoq</p></div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">수업이 아홉 시에 <span class="pe-hl pe-hl--v">시작돼요</span>.</p>
  <p class="pe-ex__uz">Dars soat toʻqqizda boshlanadi.</p>
  <p class="pe-ex__why">되다 → 돼요 (PK-18 dagi 되어요 qisqargani).</p>
</div>

<h3>6. Har kuni eshitiladigan majhul gaplar</h3>

<p>Baʼzi majhul feʼllar shu qadar koʻp ishlatiladiki, ularni alohida
soʻz sifatida yodlagan maʼqul:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">길이 많이 <span class="pe-hl pe-hl--v">막혔어요</span>.</p>
  <p class="pe-ex__uz">Yoʻl juda tiqilib qoldi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">학교까지 삼십 분 <span class="pe-hl pe-hl--v">걸려요</span>.</p>
  <p class="pe-ex__uz">Maktabgacha oʻttiz daqiqa ketadi.</p>
  <p class="pe-ex__why">걸리다 — vaqt haqida ham, kasal haqida ham:
  감기에 <b>걸렸어요</b> (shamollab qoldim).</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">이 책은 서점에서 잘 <span class="pe-hl pe-hl--v">팔려요</span>.</p>
  <p class="pe-ex__uz">Bu kitob doʻkonda yaxshi sotiladi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>문을 열렸어요.</s></p>
  <p class="pe-good"><b>문이</b> 열렸어요.</p>
  <p><small>Majhul feʼlda toʻldiruvchi qolmaydi — 을/를 <b>이/가</b>ga
  aylanadi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>쥐가 고양이가 잡혔어요.</s></p>
  <p class="pe-good">쥐가 <b>고양이에게</b> 잡혔어요.</p>
  <p><small>Ish bajaruvchisi — 에게/한테. Bitta gapda ikkita 가
  boʻlmaydi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>산이 보여져요.</s></p>
  <p class="pe-good">산이 <b>보여요</b>.</p>
  <p><small>보이다 <em>allaqachon</em> majhul. Ustiga yana 아/어지다
  qoʻshilmaydi — bu ikki qavat majhul boʻladi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>수업이 시작해요 (“dars boshlanadi” maʼnosida)</s></p>
  <p class="pe-good">수업이 <b>시작돼요</b>.</p>
  <p><small>Kim boshlaydi demoqchi boʻlsangiz 시작하다, ishning oʻzi
  boshlansa — 시작되다.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> 열다 ning majhul shakli qaysi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>열리다</b> — oʻzak ㄹ bilan tugagani uchun <b>리</b>:
    문이 열려요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 쥐가 고양이
  <span class="pe-blank"></span> 잡혔어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>에게</b> (yoki 한테) — mushuk jonli, shuning uchun 에 emas.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Bu gapni majhulga oʻtkazing:
  누가 창문을 닫았어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>창문이 닫혔어요.</b> 을 → 이, 닫다 → 닫히다. Kim yopgani
    endi aytilmaydi — majhul nisbatning butun maqsadi shu.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> 만들다 ning majhuli qaysi va
  nega 이/히/리/기 emas?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>만들어지다.</b> 만들다 ning 이/히/리/기 shakli yoʻq —
    bunday feʼllar uchun <b>아/어지다</b> yoʻli ishlatiladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Xatoni toping:
  <s>수업이 아홉 시에 시작해요.</s> (“dars boshlanadi”)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>수업이 아홉 시에 시작돼요.</b> 하다 feʼllari
    majhulga <b>되다</b> bilan oʻtadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> 감기에 걸렸어요 nima degani?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>“Shamollab qoldim.”</b> 걸리다 — 걸다 ning majhuli, lekin bu
    iborada “kasallikka ilinmoq” maʼnosida qotib qolgan. Bitta soʻz
    sifatida yodlang.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>열리다</b> — ochilmoq (열다 dan)</li>
  <li><b>닫히다</b> — yopilmoq (닫다 dan)</li>
  <li><b>들리다</b> — eshitilmoq (듣다 dan)</li>
  <li><b>보이다</b> — koʻrinmoq (보다 dan)</li>
  <li><b>잡히다</b> — tutilmoq (잡다 dan)</li>
  <li><b>막히다</b> — tiqilib qolmoq (막다 dan)</li>
  <li><b>팔리다</b> — sotilmoq (팔다 dan)</li>
  <li><b>걸리다</b> — (vaqt) ketmoq; (kasallikka) ilinmoq</li>
  <li><b>꺼지다</b> — oʻchmoq · <b>켜지다</b> — yonmoq</li>
  <li><b>시작되다</b> — boshlanmoq · <b>바람</b> — shamol</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li>Majhul nisbat = ish bajaruvchisi emas, <b>ishning oʻzi</b> muhim.</li>
    <li>Toʻrtta qoʻshimcha: <b>이 · 히 · 리 · 기</b> — yopiq roʻyxat,
      feʼl bilan birga yodlanadi.</li>
    <li>Oʻzakning oxiri maslahat beradi: ㄹ → 리, ㄱ/ㄷ/ㅂ → 히,
      ㄴ/ㅁ/ㅅ → 기, ㅎ/unli → 이.</li>
    <li>Gap qayta joylashadi: <b>을/를 → 이/가</b>, eski ega →
      <b>에게/한테</b> (jonli) yoki <b>에</b> (jonsiz).</li>
    <li>Shakli yoʻq feʼllar uchun — <b>아/어지다</b> (만들어지다, 꺼지다).</li>
    <li>하다 feʼllari uchun — <b>되다</b> (시작되다, 준비되다).</li>
    <li>Oʻzbekcha juftligi: och-<b>il</b>-di · yop-<b>il</b>-di —
      ikkala tilda ham qoʻshimcha feʼl ichiga kiradi.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-57: Orttirma nisbat — -이/히/리/기/우/구/추- va 게 하다",
        "category": "korean",
        "order": 57,
        "summary": (
            "“Yedi” va “yediRdi”, “oʻqidi” va “oʻqiTdi” — oʻzbek tilidagi shu "
            "qoʻshimchaning koreyscha aynan aksi: 먹다 → 먹이다, 읽다 → 읽히다."
        ),
        "stories": ["동생을 깨우고 밥을 먹여요"],
        "content": """
<h2>PK-57: Orttirma nisbat — -이/히/리/기/우/구/추- va 게 하다</h2>

<p>Ukangiz uxlab yotibdi, siz uni turgʻizdingiz. Oʻzbekchada “u
<b>uygʻondi</b>” demaysiz — “men uni <b>uygʻotdim</b>” deysiz. Ish
oʻzidan boʻlgani yoʻq: <em>siz qildirdingiz</em>. Bu — <b>orttirma
nisbat</b>, va oʻzbek tilida u -tir-, -dir-, -t- qoʻshimchalari bilan
yasaladi. Koreys tili buni oʻtgan darsdagi mashinaning aynan aksi bilan
qiladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Yettita qoʻshimcha bilan orttirma feʼl yasaysiz</li>
    <li>Gapda kim kimga nima qildirayotganini toʻgʻri belgilaysiz</li>
    <li>Har qanday feʼl uchun ishlaydigan <b>게 하다</b> ni oʻrganasiz</li>
    <li>하다 feʼllari uchun <b>시키다</b> ni koʻrasiz</li>
    <li>보이다, 읽히다 kabi ikki maʼnoli feʼllarni chalkashtirmaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">Feʼl oʻzagi</span>
  <span class="pe-chip pe-chip--v">이 / 히 / 리 / 기 / 우 / 구 / 추</span>
  <span class="pe-chip pe-chip--adv">= …tirdi / …dirdi</span>
</div>

<h3>1. Yana oʻzbekcha juftlik</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Oddiy</th><th>Orttirma (oʻzbekcha)</th><th>Koreyscha</th>
      <th>Orttirma (koreyscha)</th></tr>
  <tr><td>yemoq</td><td class="pk-uz">yedirmoq</td>
      <td class="pk-stem">먹다</td><td class="pk-res">먹이다</td></tr>
  <tr><td>kiymoq</td><td class="pk-uz">kiydirmoq</td>
      <td class="pk-stem">입다</td><td class="pk-res">입히다</td></tr>
  <tr><td>bilmoq</td><td class="pk-uz">bildirmoq</td>
      <td class="pk-stem">알다</td><td class="pk-res">알리다</td></tr>
  <tr><td>kulmoq</td><td class="pk-uz">kuldirmoq</td>
      <td class="pk-stem">웃다</td><td class="pk-res">웃기다</td></tr>
  <tr><td>uxlamoq</td><td class="pk-uz">uxlatmoq</td>
      <td class="pk-stem">자다</td><td class="pk-res">재우다</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Ikki dars — bitta joydan.</b> Oʻtgan darsdagi majhul qoʻshimchalari
  ham 이/히/리/기 edi. Bugungi orttirma qoʻshimchalari ham 이/히/리/기,
  ustiga yana 우/구/추. Bu tasodif emas: koreys tilida ikkala nisbat ham
  <em>bir xil joydan</em> — feʼlning ichidan — oʻsib chiqadi.
  Oʻzbekchada ham shunday: “och-<b>il</b>-di” va “och-<b>tir</b>-di”
  — ikkalasi ham oʻzak bilan zamon orasiga tiqiladi. Farqni <b>maʼno</b>
  va <b>gapdagi qoʻshimchalar</b> aytadi, shakl emas.</p>
</div>

<h3>2. Yettita qoʻshimcha</h3>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h">-이-</p>
    <p>먹다 → 먹<b>이</b>다 (yedirmoq)<br>
      보다 → 보<b>이</b>다 (koʻrsatmoq)<br>
      죽다 → 죽<b>이</b>다 (oʻldirmoq)</p></div>
  <div class="pe-card"><p class="pe-card__h">-히-</p>
    <p>입다 → 입<b>히</b>다 (kiydirmoq)<br>
      앉다 → 앉<b>히</b>다 (oʻtqazmoq)<br>
      읽다 → 읽<b>히</b>다 (oʻqitmoq)</p></div>
  <div class="pe-card"><p class="pe-card__h">-리-</p>
    <p>알다 → 알<b>리</b>다 (bildirmoq)<br>
      울다 → 울<b>리</b>다 (yigʻlatmoq)<br>
      살다 → 살<b>리</b>다 (tiriltirmoq)</p></div>
  <div class="pe-card"><p class="pe-card__h">-기-</p>
    <p>웃다 → 웃<b>기</b>다 (kuldirmoq)<br>
      씻다 → 씻<b>기</b>다 (yuvintirmoq)<br>
      남다 → 남<b>기</b>다 (qoldirmoq)</p></div>
  <div class="pe-card"><p class="pe-card__h">-우-</p>
    <p>자다 → 재<b>우</b>다 (uxlatmoq)<br>
      깨다 → 깨<b>우</b>다 (uygʻotmoq)<br>
      타다 → 태<b>우</b>다 (mindirmoq)</p></div>
  <div class="pe-card"><p class="pe-card__h">-구- / -추-</p>
    <p>낮다 → 낮<b>추</b>다 (pasaytirmoq)<br>
      늦다 → 늦<b>추</b>다 (kechiktirmoq)<br>
      맞다 → 맞<b>추</b>다 (moslashtirmoq)</p></div>
</div>

<div class="pe-call pe-rule">
  <p>Bu ham <b>yopiq roʻyxat</b> — istagan feʼlga 우 yoki 히 qoʻshib
  boʻlmaydi. Yuqoridagi yigirmatacha feʼl eng koʻp ishlatiladiganlari;
  ularni yodlang, qolganini <b>게 하다</b> hal qiladi.</p>
</div>

<h3>3. Gapdagi qoʻshimchalar</h3>

<p>Orttirma nisbat gapga <b>yangi bajaruvchi</b> qoʻshadi. Shuning uchun
eski ega bir pogʻona pastga tushadi:</p>

<div class="pe-steps">
  <div class="pe-step">
    <p><b>1. Oddiy gap.</b><br>
    <span class="pe-hl pe-hl--s">아이가</span>
    <span class="pe-hl pe-hl--o">밥을</span>
    <span class="pe-hl pe-hl--v">먹어요</span>. — Bola ovqat yeydi.</p>
  </div>
  <div class="pe-step">
    <p><b>2. Yangi bajaruvchi keladi</b> va egani egallaydi.<br>
    <span class="pe-hl pe-hl--s">엄마가</span> … — Onasi…</p>
  </div>
  <div class="pe-step">
    <p><b>3. Eski ega → 에게 / 한테.</b><br>
    엄마가 <span class="pe-hl pe-hl--adv">아이에게</span>
    <span class="pe-hl pe-hl--o">밥을</span>
    <span class="pe-hl pe-hl--v">먹여요</span>. — Onasi bolaga ovqat yediradi.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">언니가 동생<span class="pk-par">을</span>
     <span class="pe-hl pe-hl--v">깨웠어요</span>.</p>
  <p class="pe-ex__uz">Opa ukasini uygʻotdi.</p>
  <p class="pe-ex__why">Toʻldiruvchi yoʻq feʼlda (자다, 깨다, 앉다)
  odam <b>을/를</b> oladi, 에게 emas.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">어머니가 아이에게 옷을
     <span class="pe-hl pe-hl--v">입혀요</span>.</p>
  <p class="pe-ex__uz">Ona bolaga kiyim kiydiradi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Oddiy qoida:</b> asl feʼlda toʻldiruvchi <em>bor</em> boʻlsa
  (밥을 먹다, 옷을 입다) — odam <b>에게/한테</b> oladi. Asl feʼlda
  toʻldiruvchi <em>yoʻq</em> boʻlsa (자다, 앉다, 웃다) — odam
  <b>을/를</b> oladi.</p>
</div>

<h3>4. 게 하다 — hamma feʼl uchun</h3>

<p>Feʼlning orttirma shakli boʻlmasa yoki “majburladi / ruxsat berdi”
degan maʼno kerak boʻlsa — <b>-게 하다</b>. Bu qolipda hech qanday
ayri yoʻq: oʻzakka 게 qoʻshiladi, tamom.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">선생님이 학생들<span class="pk-par">을</span>
     <span class="pe-hl pe-hl--v">공부하게 했어요</span>.</p>
  <p class="pe-ex__uz">Oʻqituvchi oʻquvchilarni oʻqishga majbur qildi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">어머니가 자스루르<span class="pk-par">에게</span>
     방을 <span class="pe-hl pe-hl--v">청소하게 했어요</span>.</p>
  <p class="pe-ex__uz">Onasi Jasurga xonani tozalattirdi.</p>
</div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">먹이다</p>
    <p><b>Bevosita</b> — oʻzi qoʻli bilan qildi.</p>
    <p><small>엄마가 아이에게 밥을 먹여요 — onasi qoshiq bilan
    yediradi.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">먹게 하다</p>
    <p><b>Bilvosita</b> — aytdi, ruxsat berdi, majbur qildi.</p>
    <p><small>엄마가 아이에게 밥을 먹게 했어요 — “ovqatni ye” dedi,
    bola oʻzi yedi.</small></p>
  </div>
</div>

<h3>5. 하다 feʼllari uchun: 시키다</h3>

<p>Oʻtgan darsda 하다 → <b>되다</b> edi. Orttirma tomonida esa
하다 → <b>시키다</b>:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">선생님이 아프소나를
     <span class="pe-hl pe-hl--v">공부시켰어요</span>.</p>
  <p class="pe-ex__uz">Oʻqituvchi Afsonani oʻqitdi (oʻqishga majbur qildi).</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Uchta juftlikni yonma-yon koʻring:</b><br>
  공부하다 (oʻqimoq) → 공부<b>되다</b> (oʻqilmoq) → 공부<b>시키다</b>
  (oʻqitmoq)<br>
  Oʻzbekchada ham xuddi shu uchlik bor: oʻqi<b>moq</b> · oʻqi<b>l</b>moq ·
  oʻqi<b>t</b>moq. Yaʼni siz allaqachon uchta nisbat bilan gapirasiz —
  bugun faqat ularning koreyscha nomini oʻrganyapsiz.</p>
</div>

<h3>6. Ikki maʼnoli feʼllar — ehtiyot boʻling</h3>

<p>Bir nechta feʼlda majhul va orttirma shakli <b>bir xil</b> koʻrinadi.
Qaysi biri ekanini faqat gapdagi qoʻshimchalar aytadi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--s">산이</span>
     <span class="pe-hl pe-hl--v">보여요</span>.</p>
  <p class="pe-ex__uz">Togʻ koʻrinadi. <em>(majhul)</em></p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--s">제가</span> 친구에게
     <span class="pe-hl pe-hl--o">사진을</span>
     <span class="pe-hl pe-hl--v">보여요</span>.</p>
  <p class="pe-ex__uz">Men doʻstimga rasm koʻrsataman. <em>(orttirma)</em></p>
  <p class="pe-ex__why">Toʻldiruvchi (을/를) bor boʻlsa — orttirma.
  Faqat ega boʻlsa — majhul.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>엄마가 아이를 밥을 먹여요.</s></p>
  <p class="pe-good">엄마가 <b>아이에게</b> 밥을 먹여요.</p>
  <p><small>Bitta gapda ikkita 을/를 boʻlmaydi. 밥 toʻldiruvchi boʻlsa,
  odam 에게 oladi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>동생이 깨웠어요 (“ukamni uygʻotdim” maʼnosida)</s></p>
  <p class="pe-good"><b>동생을</b> 깨웠어요.</p>
  <p><small>깨우다 — orttirma feʼl, uning toʻldiruvchisi bor.
  동생<b>이</b> 깼어요 boʻlsa “ukam oʻzi uygʻondi” degani.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>선생님이 학생들을 공부시키게 했어요.</s></p>
  <p class="pe-good">선생님이 학생들을 <b>공부하게 했어요</b>.
    (yoki <b>공부시켰어요</b>)</p>
  <p><small>Ikki qavat orttirma boʻlmaydi — bittasini tanlang.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>아기를 재요.</s></p>
  <p class="pe-good">아기를 <b>재워요</b>.</p>
  <p><small>자다 ning orttirmasi 재우다 — 우 qoʻshimchasi tushib
  qolmaydi.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> 입다 ning orttirma shakli qaysi
  va nima degani?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>입히다</b> — “kiydirmoq”. 옷을 입다 (kiyim kiymoq) →
    아이에게 옷을 입히다 (bolaga kiyim kiydirmoq).</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 엄마가 아이
  <span class="pe-blank"></span> 밥을 먹여요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>에게</b> (yoki 한테) — 밥 allaqachon 을 olgan, shuning uchun
    odam 을/를 ololmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Farqini ayting:
  동생이 잤어요 / 동생을 재웠어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Birinchisi — <b>“ukam uxladi”</b> (oʻzi). Ikkinchisi —
    <b>“ukamni uxlatdim”</b> (men qildirdim). 자다 → 재우다.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> 청소하다 feʼliga orttirma
  qoʻshimchasi yoʻq. “Xonani tozalattirdi” qanday aytiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>청소하게 했어요</b> yoki <b>청소시켰어요</b>. 하다 feʼllarida
    ikkala yoʻl ham ochiq.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Bu gap majhulmi yoki orttirma?
  제가 친구에게 사진을 보여요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>Orttirma</b> — “rasm koʻrsataman”. Belgisi: 사진<b>을</b>,
    yaʼni toʻldiruvchi bor. 산이 보여요 da toʻldiruvchi yoʻq —
    u majhul.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Xatoni toping:
  <s>선생님이 아프소나를 밥을 먹였어요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>선생님이 아프소나에게 밥을 먹였어요.</b>
    Bitta gapda ikkita 을/를 boʻlmaydi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>먹이다</b> — yedirmoq (먹다 dan)</li>
  <li><b>입히다</b> — kiydirmoq (입다 dan)</li>
  <li><b>앉히다</b> — oʻtqazmoq (앉다 dan)</li>
  <li><b>알리다</b> — bildirmoq, xabar bermoq (알다 dan)</li>
  <li><b>웃기다</b> — kuldirmoq (웃다 dan)</li>
  <li><b>깨우다</b> — uygʻotmoq (깨다 dan)</li>
  <li><b>재우다</b> — uxlatmoq (자다 dan)</li>
  <li><b>태우다</b> — mindirmoq (타다 dan)</li>
  <li><b>늦추다</b> — kechiktirmoq · <b>낮추다</b> — pasaytirmoq</li>
  <li><b>시키다</b> — qildirmoq, buyurmoq · <b>게 하다</b> — …tirmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li>Orttirma nisbat = ishni <b>boshqa odam qildiradi</b>.</li>
    <li>Yettita qoʻshimcha: <b>이 · 히 · 리 · 기 · 우 · 구 · 추</b> —
      majhul bilan bir joydan chiqadi, shuning uchun shakli oʻxshaydi.</li>
    <li>Gapga yangi ega qoʻshiladi, eskisi <b>에게/한테</b> yoki
      <b>을/를</b> ga tushadi.</li>
    <li>Asl feʼlda toʻldiruvchi bor → odam <b>에게</b>; yoʻq → odam
      <b>을/를</b>.</li>
    <li>Har qanday feʼl uchun — <b>-게 하다</b> (bilvosita, “aytdi,
      ruxsat berdi”).</li>
    <li>하다 feʼllari uchun — <b>시키다</b> (공부시키다).</li>
    <li>보이다, 읽히다, 씻기다 ikki maʼnoli: <b>을/를 bor boʻlsa
      orttirma</b>, yoʻq boʻlsa majhul.</li>
    <li>Oʻzbekcha juftligi: ye-<b>dir</b>-di · kiy-<b>dir</b>-di ·
      oʻqi-<b>t</b>-di.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-58: 아/어 버리다 — tugallanish va his-tuygʻu",
        "category": "korean",
        "order": 58,
        "summary": (
            "“Yeb qoʻydim”, “ketib qoldi” — oʻzbekchadagi koʻmakchi feʼllar. "
            "Koreys tilida ularning oʻrnini 버리다 egallaydi."
        ),
        "stories": ["숙제를 다 해 버렸어요"],
        "content": """
<h2>PK-58: 아/어 버리다 — tugallanish va his-tuygʻu</h2>

<p>Muzlatgichda bitta tort qolgan edi. Kelsangiz — yoʻq. Oʻzbekchada
“ukam tortni <b>yedi</b>” demaysiz, “tortni <b>yeb qoʻyibdi</b>”
deysiz. Ikkinchi gapda faqat maʼlumot emas, <em>his</em> ham bor:
tugadi, endi yoʻq, va bu sizga yoqmadi. Koreys tilida bu ishni
<b>버리다</b> bajaradi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>아/어 버리다</b> ni toʻgʻri yasaysiz</li>
    <li>Uning ikki tuygʻusini — yengillik va afsus — ajratasiz</li>
    <li>Oddiy oʻtgan zamondan farqini bilasiz</li>
    <li>잃어버리다, 잊어버리다 kabi qotib qolgan soʻzlarni oʻrganasiz</li>
    <li>Qachon <b>ishlatmaslik</b> kerakligini bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">Feʼl</span>
  <span class="pe-chip pe-chip--v">아/어</span>
  <span class="pe-chip pe-chip--v">버리다</span>
  <span class="pe-chip pe-chip--adv">= …b qoʻydi / …b yubordi</span>
</div>

<h3>1. 버리다 ning oʻzi</h3>

<p><b>버리다</b> — “tashlamoq” degan oddiy feʼl: 쓰레기를 버려요
(axlatni tashlayman). Boshqa feʼlning orqasiga koʻmakchi boʻlib
tursa esa maʼnosi oʻzgaradi: <em>ish butunlay tugadi, orqaga yoʻl
yoʻq</em>. Xuddi qilingan ishni tashlab yuborgandek.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>아/어 shakli</th><th>Koʻmakchi</th><th>Natija</th>
      <th>Maʼnosi</th></tr>
  <tr><td>먹다</td><td class="pk-stem">먹어</td><td class="pk-end">버리다</td>
      <td class="pk-res">먹어 버리다</td><td class="pk-uz">yeb qoʻymoq</td></tr>
  <tr><td>가다</td><td class="pk-stem">가</td><td class="pk-end">버리다</td>
      <td class="pk-res">가 버리다</td><td class="pk-uz">ketib qolmoq</td></tr>
  <tr><td>하다</td><td class="pk-stem">해</td><td class="pk-end">버리다</td>
      <td class="pk-res">해 버리다</td><td class="pk-uz">qilib boʻlmoq</td></tr>
  <tr><td>쓰다</td><td class="pk-stem">써</td><td class="pk-end">버리다</td>
      <td class="pk-res">써 버리다</td><td class="pk-uz">sarflab yubormoq</td></tr>
</table></div>

<p>Yasalishi PK-18 dagi 아/어요 bilan bir xil — oʻzakning oxirgi unlisi
ㅏ yoki ㅗ boʻlsa <b>아</b>, boshqa boʻlsa <b>어</b>, 하다 esa
<b>해</b>.</p>

<div class="pe-call pe-uz">
  <p><b>Bu darsning eng katta yordami oʻzbek tilidan keladi.</b>
  Oʻzbekchada koʻmakchi feʼllar tizimi bor: “yeb <b>qoʻydi</b>”,
  “ketib <b>qoldi</b>”, “aytib <b>yubordi</b>”, “ichib <b>boʻldi</b>”.
  Har birida asosiy feʼl <em>-b</em> shaklida turadi va orqasidan
  koʻmakchi keladi. Koreysning <b>아/어 + 버리다</b> si aynan shu
  qurilma: 먹<b>어</b> 버리다 = “ye<b>b</b> qoʻymoq”. Ingliz tilida
  bunday narsa yoʻq — shuning uchun bu qolip inglizzabon oʻquvchi uchun
  qiyin, siz uchun esa tanish.</p>
</div>

<h3>2. Birinchi tuygʻu: yengillik (시원함)</h3>

<p>Ogʻir ish tugadi, yelkangizdan yuk tushdi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">숙제를 다 <span class="pe-hl pe-hl--v">해 버렸어요</span>!</p>
  <p class="pe-ex__uz">Uy vazifasini qilib boʻldim!</p>
  <p class="pe-ex__why">Faqat “qildim” emas — <em>tugadi, endi
  ozodman</em>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">어려운 책이었지만 어제
     <span class="pe-hl pe-hl--v">다 읽어 버렸어요</span>.</p>
  <p class="pe-ex__uz">Qiyin kitob edi, lekin kecha oʻqib tashladim.</p>
</div>

<h3>3. Ikkinchi tuygʻu: afsus (아쉬움)</h3>

<p>Ish tugadi, lekin siz buni istamagansiz:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">동생이 케이크를 다
     <span class="pe-hl pe-hl--v">먹어 버렸어요</span>.</p>
  <p class="pe-ex__uz">Ukam tortni yeb qoʻyibdi (hammasini).</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">친구가 인사도 안 하고
     <span class="pe-hl pe-hl--v">가 버렸어요</span>.</p>
  <p class="pe-ex__uz">Doʻstim xayrlashmasdan ketib qoldi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">용돈을 하루 만에
     <span class="pe-hl pe-hl--v">다 써 버렸어요</span>.</p>
  <p class="pe-ex__uz">Choʻntak puligni bir kunda sarflab yubordim.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Qaysi tuygʻu ekanini qanday bilish mumkin?</b> Faqat kontekstdan.
  Ish <em>sizga kerak</em> edimi — yengillik. Ish <em>sizga qarshi</em>
  boʻldimi — afsus. Oʻzbekchada ham shunday: “yeb qoʻydim” xursand ham,
  afsus ham boʻlishi mumkin — ohang va vaziyat hal qiladi.</p>
</div>

<h3>4. 았/었어요 dan farqi</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">먹었어요</p>
    <p><b>Maʼlumot.</b> Yedim — tamom.</p>
    <p><small>점심을 먹었어요. — Tushlik qildim.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">먹어 버렸어요</p>
    <p><b>Maʼlumot + tuygʻu.</b> Hammasi tugadi, va bu menga taʼsir qildi.</p>
    <p><small>케이크를 다 먹어 버렸어요. — Tortni yeb qoʻydim
    (endi yoʻq).</small></p>
  </div>
</div>

<div class="pe-call pe-rule">
  <p>버리다 koʻpincha <b>다</b> (“hammasi, butunlay”) bilan birga
  keladi: 다 먹어 버렸어요, 다 써 버렸어요, 다 읽어 버렸어요.
  Ikkalasi bir-birini kuchaytiradi — “hammasini” + “tugatib”.</p>
</div>

<h3>5. Qotib qolgan soʻzlar: 잃어버리다, 잊어버리다</h3>

<p>Ikkita feʼl 버리다 bilan shu qadar birikib ketganki, ular
<b>bitta soʻz</b> boʻlib yoziladi va 버리다siz deyarli
ishlatilmaydi:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h">잃어버리다</p>
    <p>yoʻqotib qoʻymoq</p>
    <p><small>지갑을 잃어버렸어요. — Hamyonimni yoʻqotib qoʻydim.</small></p></div>
  <div class="pe-card"><p class="pe-card__h">잊어버리다</p>
    <p>esdan chiqarib qoʻymoq</p>
    <p><small>이름을 잊어버렸어요. — Ismini esdan chiqaribman.</small></p></div>
</div>

<div class="pe-call pe-warn">
  <p><b>버리다 sifatlar bilan ishlamaydi.</b> Faqat harakat feʼllari
  bilan: <s>예뻐 버렸어요</s> ✗, <s>추워 버렸어요</s> ✗.
  Sifat oʻzgarishi uchun PK-56 dagi <b>아/어지다</b> bor:
  예뻐졌어요, 추워졌어요.</p>
</div>

<h3>6. Doʻstlar orasida: qisqargan shakli</h3>

<p>반말 da (PK-11) 아/어 va 버리다 bitta soʻzday qoʻshilib ketadi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">야, 내 빵 <span class="pe-hl pe-hl--v">먹어버렸어</span>?</p>
  <p class="pe-ex__uz">Hoy, nonimni yeb qoʻydingmi?</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>숙제를 하 버렸어요.</s></p>
  <p class="pe-good">숙제를 <b>해</b> 버렸어요.</p>
  <p><small>버리다 dan oldin feʼl <b>아/어 shaklida</b> turishi shart.
  하다 → 해.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>동생이 케이크를 먹어 버려었어요.</s></p>
  <p class="pe-good">동생이 케이크를 먹어 <b>버렸어요</b>.</p>
  <p><small>Zamon <b>버리다</b> ga qoʻshiladi: 버리 + 었 → 버렸.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>날씨가 추워 버렸어요.</s></p>
  <p class="pe-good">날씨가 <b>추워졌어요</b>.</p>
  <p><small>춥다 — sifat. Sifat uchun 버리다 emas, 아/어지다.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>지갑을 잃어 버렸어요 (ikki soʻz)</s></p>
  <p class="pe-good">지갑을 <b>잃어버렸어요</b>.</p>
  <p><small>잃어버리다 va 잊어버리다 — qoʻshib yoziladigan bitta
  soʻz.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 숙제를 다
  <span class="pe-blank"></span> 버렸어요. (하다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>해</b> — 하다 ning 아/어 shakli 해. 해 버렸어요 = “qilib
    boʻldim”.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Farqini ayting:
  케이크를 먹었어요 / 케이크를 먹어 버렸어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Birinchisi — oddiy maʼlumot: <b>“tort yedim”</b>. Ikkinchisi —
    <b>“tortni yeb qoʻydim”</b>: hammasi tugadi, va gapiruvchida
    tuygʻu bor (afsus yoki yengillik).</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Bu gapda qaysi tuygʻu bor?
  친구가 인사도 안 하고 가 버렸어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>Afsus / xafalik.</b> “Xayrlashmasdan ketib qoldi” —
    soʻzlovchi buni istamagan.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Nima uchun
  <s>날씨가 더워 버렸어요</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>덥다 — <b>sifat</b>, harakat feʼli emas. 버리다 faqat harakat
    feʼllari bilan keladi. Toʻgʻrisi — <b>더워졌어요</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> “Hamyonimni yoʻqotib qoʻydim” —
  koreyschada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>지갑을 잃어버렸어요.</b> 잃어버리다 bitta soʻz boʻlib
    yoziladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Xatoni toping:
  <s>용돈을 다 써 버려었어요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>용돈을 다 써 버렸어요.</b> Zamon qoʻshimchasi
    버리다 ning oʻzagiga qoʻshiladi: 버리 + 었 → <b>버렸</b>.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>아/어 버리다</b> — …b qoʻymoq, …b yubormoq</li>
  <li><b>버리다</b> — tashlamoq</li>
  <li><b>잃어버리다</b> — yoʻqotib qoʻymoq</li>
  <li><b>잊어버리다</b> — esdan chiqarib qoʻymoq</li>
  <li><b>다</b> — hammasi, butunlay</li>
  <li><b>용돈</b> — choʻntak puli</li>
  <li><b>지갑</b> — hamyon</li>
  <li><b>케이크</b> — tort</li>
  <li><b>인사하다</b> — salomlashmoq, xayrlashmoq</li>
  <li><b>쓰레기</b> — axlat</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>아/어 버리다</b> = ish butunlay tugadi + gapiruvchining
      tuygʻusi.</li>
    <li>Ikki tuygʻu: <b>yengillik</b> (숙제를 다 해 버렸어요) va
      <b>afsus</b> (케이크를 다 먹어 버렸어요).</li>
    <li>Yasalishi 아/어요 bilan bir xil: 먹어 · 가 · 해 · 써.</li>
    <li>Zamon <b>버리다</b> ga qoʻshiladi: 먹어 <b>버렸</b>어요.</li>
    <li>Koʻpincha <b>다</b> bilan yuradi.</li>
    <li>Faqat harakat feʼllari bilan — sifat uchun <b>아/어지다</b>.</li>
    <li><b>잃어버리다 · 잊어버리다</b> — qoʻshib yoziladigan bitta soʻz.</li>
    <li>Oʻzbekcha juftligi: ye<b>b qoʻydi</b> · keti<b>b qoldi</b> ·
      ayti<b>b yubordi</b>.</li>
  </ul>
</div>
""",
    },
]
