# -*- coding: utf-8 -*-
"""Prime Korean — Block E, darslar 62–64.

62. Koʻchirma gapning qisqargan shakllari: -대요, -냬요, -래요, -재요
63. (으)ㄹ 뻔하다 — "sal boʻlmasa…"
64. (으)ㄹ 테니까 — soʻzlovchi irodasiga asoslangan sabab

Oʻzbekcha kalitlar:
  -대요        = "…emish / …ekan"  — eshitgan gapni yetkazish
  (으)ㄹ 뻔했다 = "yiqil-AYOZ-dim", "sal boʻlmasa yiqilardim"
  (으)ㄹ 테니까 = "men qilaman, SHUNING UCHUN siz…"

63 va 64 yana bitta tanish mashina: aniqlovchi + ot (뻔, 터) — PK-52
dagi 것, PK-53 dagi 줄 bilan bir oila.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

Oʻqish matnlari: corner/management/commands/_stories_prime_korean_62_64.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_62_64.py --author=prime
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
        "title": "PK-62: Koʻchirma gapning qisqargan shakllari — -대요, -냬요, -래요, -재요",
        "category": "korean",
        "order": 62,
        "summary": (
            "Koreyslar 간다고 해요 demaydi — 간대요 deydi. Oʻzbekchadagi “emish, "
            "ekan” kabi, eshitgan gapni bir soʻzda yetkazadigan shakl."
        ),
        "stories": ["아프소나의 편지"],
        "content": """
<h2>PK-62: Koʻchirma gapning qisqargan shakllari — -대요, -냬요, -래요, -재요</h2>

<p>Oʻtgan ikki darsda koʻchirma gapning butun mashinasini qurdingiz:
다고 · 냐고 · (으)라고 · 자고. Endi bitta yomon xabar bor — koreyslar
kundalik gapda bu shakllarni <em>toʻliq aytmaydi</em>. Va bitta yaxshi
xabar: qisqartirish qoidasi juda oddiy, va uni oʻrgansangiz, koreys
seriallaridagi gaplarning yarmi birdan ochiladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Toʻrtta qisqargan shaklni yasaysiz: <b>대요 · 냬요 · 래요 · 재요</b></li>
    <li>Ularni toʻliq shakldan bir soniyada chiqarasiz</li>
    <li>Zamon va ot bilan qanday ishlashini koʻrasiz</li>
    <li>Qachon toʻliq, qachon qisqa shakl ishlatilishini bilasiz</li>
    <li>Koreyslar gapirganda eshitadigan narsangizni tushunasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">다고/냐고/라고/자고</span>
  <span class="pe-chip pe-chip--opt">해요</span>
  <span class="pe-chip pe-chip--v">→ 대요 / 냬요 / 래요 / 재요</span>
</div>

<h3>1. Qoida bitta: 고 해 tushib qoladi</h3>

<p>Qisqartirish mexanik. <b>고 해</b> qismini olib tashlaysiz, qolgan
ikki tovush qoʻshilib ketadi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Gap turi</th><th>Toʻliq shakl</th><th>Qisqargan</th><th>Maʼnosi</th></tr>
  <tr><td>Darak</td><td class="pk-stem">간다고 해요</td>
      <td class="pk-res">간대요</td><td class="pk-uz">boradi emish</td></tr>
  <tr><td>Soʻroq</td><td class="pk-stem">가냐고 해요</td>
      <td class="pk-res">가냬요</td><td class="pk-uz">boradimi deb soʻrayapti</td></tr>
  <tr><td>Buyruq</td><td class="pk-stem">가라고 해요</td>
      <td class="pk-res">가래요</td><td class="pk-uz">bor deyapti</td></tr>
  <tr><td>Taklif</td><td class="pk-stem">가자고 해요</td>
      <td class="pk-res">가재요</td><td class="pk-uz">boraylik deyapti</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida ham xuddi shunday narsa bor.</b> Biz eshitgan
  gapni yetkazganda uzun jumla qurmaymiz — kichkina qoʻshimcha
  ishlatamiz:<br>
  “Ertaga imtihon yoʻq <b>emish</b>.” · “U kelmas <b>ekan</b>.”<br>
  Bu — aynan <b>대요</b> ning ishi. Yaʼni oʻzbek tili ham “eshitdim,
  lekin oʻzim koʻrmadim” degan maʼnoni bitta qoʻshimchaga
  yigʻadi. Shuning uchun 간대요 ni “boradi <em>emish</em>” deb
  tarjima qilsangiz, ohangi ham, maʼnosi ham toʻgʻri chiqadi.</p>
</div>

<h3>2. Darak: -대요 (eng koʻp ishlatiladigani)</h3>

<p>Bu yerda PK-60 dagi feʼl/sifat farqi <b>saqlanadi</b> — faqat oxiri
qisqaradi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Nima</th><th>Toʻliq</th><th>Qisqargan</th></tr>
  <tr><td>Feʼl, 받침 yoʻq</td><td class="pk-stem">간다고 해요</td>
      <td class="pk-res">간대요</td></tr>
  <tr><td>Feʼl, 받침 bor</td><td class="pk-stem">먹는다고 해요</td>
      <td class="pk-res">먹는대요</td></tr>
  <tr><td>Sifat</td><td class="pk-stem">좋다고 해요</td>
      <td class="pk-res">좋대요</td></tr>
  <tr><td>Ot (이다)</td><td class="pk-stem">학생이라고 해요</td>
      <td class="pk-res">학생이래요</td></tr>
  <tr><td>Oʻtgan zamon</td><td class="pk-stem">갔다고 해요</td>
      <td class="pk-res">갔대요</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">지영 씨가 내일 <span class="pe-hl pe-hl--v">간대요</span>.</p>
  <p class="pe-ex__uz">Jiyon ertaga boradi emish.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">그 카페 커피가 정말
     <span class="pe-hl pe-hl--v">맛있대요</span>.</p>
  <p class="pe-ex__uz">U kafening kofesi juda mazali ekan.</p>
  <p class="pe-ex__why">맛있다 — sifat kabi, shuning uchun 맛있는대요
  emas.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">그 사람이 새 <span class="pe-hl pe-hl--v">선생님이래요</span>.</p>
  <p class="pe-ex__uz">U odam yangi oʻqituvchi ekan.</p>
  <p class="pe-ex__why">Ot + 이다 → 이라고 해요 → <b>이래요</b>.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Kim aytgani muhim emas.</b> 대요 koʻpincha “odamlar shunday
  deyapti”, “eshitdim” maʼnosida ishlatiladi — gapiruvchi manbani
  aytishi shart emas. Xuddi oʻzbekchadagi “emish” kabi.</p>
</div>

<h3>3. Buyruq va taklif: -래요 va -재요</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">선생님이 내일 일찍 <span class="pe-hl pe-hl--v">오래요</span>.</p>
  <p class="pe-ex__uz">Oʻqituvchi ertaga erta kelinglar deyapti.</p>
  <p class="pe-ex__why">오라고 해요 → <b>오래요</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">자스루르 씨가 같이 밥을
     <span class="pe-hl pe-hl--v">먹재요</span>.</p>
  <p class="pe-ex__uz">Jasur birga ovqatlanaylik deyapti.</p>
  <p class="pe-ex__why">먹자고 해요 → <b>먹재요</b>.</p>
</div>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h">지 말라고 해요</p>
    <p>→ <b>지 말래요</b></p>
    <p><small>뛰지 말래요 — yugurmang deyapti.</small></p></div>
  <div class="pe-card"><p class="pe-card__h">달라고 해요</p>
    <p>→ <b>달래요</b></p>
    <p><small>돈을 달래요 — pul ber deyapti.</small></p></div>
  <div class="pe-card"><p class="pe-card__h">지 말자고 해요</p>
    <p>→ <b>지 말재요</b></p>
    <p><small>가지 말재요 — bormaylik deyapti.</small></p></div>
  <div class="pe-card"><p class="pe-card__h">아니라고 해요</p>
    <p>→ <b>아니래요</b></p>
    <p><small>사실이 아니래요 — rost emas ekan.</small></p></div>
</div>

<h3>4. Soʻroq: -냬요</h3>

<p>Eng kam uchraydigani, lekin qoidasi bir xil:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">어머니가 숙제를 <span class="pe-hl pe-hl--v">했냬요</span>.</p>
  <p class="pe-ex__uz">Onam uy vazifasini qildingmi deb soʻrayapti.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Ehtiyot boʻling: 가래요 va 갈래요 — boshqa narsa.</b><br>
  <b>가래요</b> = 가라고 해요 — <em>boshqa odam</em> “bor” dedi.<br>
  <b>갈래요</b> = “men boraman / borasizmi?” — bu butunlay boshqa
  qolip, uni keyinroq oʻrganasiz.<br>
  Farqi bitta harfda: <b>ㄹ</b> bor-yoʻqligida. Eshitganda diqqat
  qiling.</p>
</div>

<h3>5. Qachon toʻliq, qachon qisqa?</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Toʻliq shakl (다고 했어요)</p>
    <p>Yozma matn, rasmiy nutq, aniq bir odamning gapi.</p>
    <p><small>선생님이 시험이 있다고 했어요.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Qisqargan (대요)</p>
    <p>Kundalik gap, doʻstlar orasida, “eshitdim” ohangi.</p>
    <p><small>시험이 있대요!</small></p>
  </div>
</div>

<div class="pe-call pe-tip">
  <p>Yozma ishda (TOPIK 쓰기 ham) <b>toʻliq shakl</b> xavfsizroq.
  Lekin 듣기 (tinglash) va seriallarda deyarli <em>faqat</em> qisqargan
  shakl eshitiladi — shuning uchun uni tanish shart.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>지영 씨가 내일 가대요.</s></p>
  <p class="pe-good">지영 씨가 내일 <b>간대요</b>.</p>
  <p><small>Feʼlning ㄴ다/는다 qismi qisqarganda ham
  <b>qoladi</b>: 간다고 → 간대요.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>그 카페가 좋는대요.</s></p>
  <p class="pe-good">그 카페가 <b>좋대요</b>.</p>
  <p><small>좋다 — sifat, ㄴ다/는다 olmaydi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>그 사람이 선생님이대요.</s></p>
  <p class="pe-good">그 사람이 <b>선생님이래요</b>.</p>
  <p><small>Ot + 이다 → 이라고 해요 → <b>이래요</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>선생님이 일찍 왔래요.</s></p>
  <p class="pe-good">선생님이 일찍 <b>오래요</b>.</p>
  <p><small>Buyruqda zamon boʻlmaydi (PK-61) — qisqargan shaklda
  ham shunday.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Qisqartiring: 민수 씨가 내일
  간다고 해요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>민수 씨가 내일 간대요.</b> 고 해 tushadi, ㄴ다 qoladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Qisqartiring: 그 영화가 재미있다고
  해요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>그 영화가 재미있대요.</b> 재미있다 sifat kabi ishlaydi →
    있대요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Toʻldiring: 선생님이 일찍
  <span class="pe-blank"></span>. (“erta kelinglar” deyapti)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>오래요</b> — 오라고 해요 ning qisqargani (buyruq).</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Bu toʻrttasini ajrating:
  간대요 · 가냬요 · 가래요 · 가재요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>간대요</b> — boradi emish (darak).
    <b>가냬요</b> — boradimi deb soʻrayapti (soʻroq).
    <b>가래요</b> — bor deyapti (buyruq).
    <b>가재요</b> — boraylik deyapti (taklif).</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Xatoni toping:
  <s>그 사람이 새 학생이대요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>학생이래요</b>. Ot bilan 이라고 해요 →
    이래요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> 가래요 va 갈래요 farqi nimada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>가래요</b> — boshqa odam “bor” dedi (가라고 해요).
    <b>갈래요</b> — “men boraman / borasizmi” degan butunlay boshqa
    qolip. Farqi <b>ㄹ</b> da.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>-대요</b> — …emish, …ekan (darak)</li>
  <li><b>-냬요</b> — …mi deb soʻrayapti (soʻroq)</li>
  <li><b>-래요</b> — … deyapti (buyruq)</li>
  <li><b>-재요</b> — …aylik deyapti (taklif)</li>
  <li><b>(이)래요</b> — …ekan (ot bilan)</li>
  <li><b>아니래요</b> — …emas ekan</li>
  <li><b>달래요</b> — bering deyapti</li>
  <li><b>지 말래요</b> — qilmang deyapti</li>
  <li><b>소식</b> — xabar</li>
  <li><b>들리다</b> — eshitilmoq (PK-56)</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li>Qoida bitta: <b>고 해</b> tushadi, qolgani qoʻshiladi.</li>
    <li><b>다고 해요 → 대요</b> · <b>냐고 해요 → 냬요</b> ·
      <b>라고 해요 → 래요</b> · <b>자고 해요 → 재요</b>.</li>
    <li>Feʼl/sifat farqi saqlanadi: 간대요 · 먹는대요 · 좋대요.</li>
    <li>Ot bilan — <b>(이)래요</b>, 이대요 emas.</li>
    <li>Buyruq va taklifda zamon yoʻq: <b>오래요</b>, 왔래요 emas.</li>
    <li>Yozma ishda toʻliq shakl, kundalik nutqda qisqargani.</li>
    <li>Oʻzbekcha juftligi: “…<b>emish</b>”, “…<b>ekan</b>”.</li>
    <li><b>가래요 ≠ 갈래요</b> — bittasi boshqaning gapi, ikkinchisi
      butunlay boshqa qolip.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-63: (으)ㄹ 뻔하다 — “sal boʻlmasa…”",
        "category": "korean",
        "order": 63,
        "summary": (
            "“Yiqilayozdim”, “sal boʻlmasa kechikardim” — boʻlishiga oz qolgan, "
            "lekin boʻlmagan ish. Koreyschada 넘어질 뻔했어요."
        ),
        "stories": ["어제는 정말 위험했어요"],
        "content": """
<h2>PK-63: (으)ㄹ 뻔하다 — “sal boʻlmasa…”</h2>

<p>Avtobusga yugurdingiz. Zinapoyada oyogʻingiz sirpandi — lekin
ushlab qoldingiz. Uyga kelib nima deysiz? “<b>Yiqilayozdim!</b>” yoki
“<b>Sal boʻlmasa yiqilardim!</b>”. Ish boʻlmadi, lekin boʻlishiga
juda oz qoldi — va aynan shuning uchun aytishga arziydi. Koreys tilida
bu <b>(으)ㄹ 뻔하다</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)ㄹ 뻔하다</b> bilan “sal boʻlmasa…” deysiz</li>
    <li>Nega u <b>doim oʻtgan zamonda</b> ekanini bilib olasiz</li>
    <li><b>하마터면</b> soʻzi bilan kuchaytirasiz</li>
    <li>Qaysi feʼllar bilan tabiiy eshitilishini koʻrasiz</li>
    <li>Yana bir “aniqlovchi + ot” mashinasini tanib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">Feʼl oʻzagi</span>
  <span class="pe-chip pe-chip--v">(으)ㄹ 뻔</span>
  <span class="pe-chip pe-chip--v">했어요</span>
  <span class="pe-chip pe-chip--adv">= sal boʻlmasa …ardim</span>
</div>

<h3>1. Oʻzbek tilida buning uchun alohida qoʻshimcha bor</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">계단에서 <span class="pe-hl pe-hl--v">넘어질
     뻔했어요</span>.</p>
  <p class="pe-ex__uz">Zinapoyada yiqilayozdim.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu dars oʻzbek oʻquvchi uchun deyarli bepul.</b> Oʻzbek tilida
  aynan shu maʼno uchun <b>-(a)yoz-</b> qoʻshimchasi bor:
  “yiqil<b>ayoz</b>dim”, “oʻl<b>ayoz</b>dim”, “yigʻl<b>ayoz</b>dim”.
  Yaʼni bizda ham bu — <em>grammatik</em> shakl, shunchaki ibora emas.
  Ingliz tilida esa bunday qoʻshimcha yoʻq, faqat “almost” degan
  qoʻshimcha soʻz bor. Siz uchun fikr tayyor: “boʻlishiga oz qoldi,
  lekin boʻlmadi”. Faqat koreyscha shaklni yodlang.</p>
</div>

<h3>2. Yasalishi — tanish 받침 ayrisi</h3>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">ㄹ 뻔했어요</span></p>
    <p>가다 → 갈 뻔했어요</p>
    <p>다치다 → 다칠 뻔했어요</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">을 뻔했어요</span></p>
    <p>죽다 → 죽을 뻔했어요</p>
    <p>늦다 → 늦을 뻔했어요</p>
  </div>
</div>

<div class="pe-call pe-rule">
  <p><b>뻔 — yana bitta ot.</b> PK-52 da 것, PK-53 da 줄, PK-59 da
  놓다 — hammasi bitta mashina edi: <em>aniqlovchi + ot</em>. Bugungi
  <b>뻔</b> ham shu — “holat, daraja” degan ot. Shuning uchun oldida
  (으)ㄹ turadi: <b>hali boʻlmagan</b> ish haqida gapiryapmiz.</p>
</div>

<h3>3. Doim oʻtgan zamonda</h3>

<p>Bu qolipning eng qatʼiy qoidasi. Ish <em>boʻlmagan</em>, lekin
xavf <em>oʻtib ketgan</em> — shuning uchun 뻔하다 har doim
<b>뻔했어요</b> boʻladi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">버스를 <span class="pe-hl pe-hl--v">놓칠
     뻔했어요</span>. 그런데 <span class="pe-hl pe-hl--adv">겨우</span>
     탔어요.</p>
  <p class="pe-ex__uz">Avtobusni oʻtkazib yuborayozdim. Lekin
  arang mindim.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">시험에 <span class="pe-hl pe-hl--v">늦을
     뻔했어요</span>.</p>
  <p class="pe-ex__uz">Imtihonga kechikayozdim.</p>
  <p class="pe-ex__why">Demak kechikmadim — ish <b>boʻlmadi</b>.</p>
</div>

<div class="pe-call pe-warn">
  <p><s>넘어질 뻔해요</s> ✗ — hozirgi zamonda ishlatilmaydi.<br>
  <s>넘어졌을 뻔했어요</s> ✗ — oldida zamon qoʻshimchasi
  boʻlmaydi.<br>
  Faqat <b>(으)ㄹ 뻔했어요</b>.</p>
</div>

<h3>4. 하마터면 bilan kuchaytirish</h3>

<p><b>하마터면</b> — “sal boʻlmasa, oz qoldiki” degan ravish. U bu
qolip bilan juftlik boʻlib yuradi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--adv">하마터면</span>
     지갑을 <span class="pe-hl pe-hl--v">잃어버릴 뻔했어요</span>.</p>
  <p class="pe-ex__uz">Sal boʻlmasa hamyonimni yoʻqotib qoʻyardim.</p>
  <p class="pe-ex__why">잃어버리다 (PK-58) + 뻔하다 — ikki dars
  birga.</p>
</div>

<h3>5. Koʻpincha yomon ishlar haqida</h3>

<p>Bu qolip <em>xavf</em> haqida: yaxshi hodisa emas, balki
<b>boʻlmagani yaxshi</b> boʻlgan hodisa haqida gapiradi.</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h">넘어질 뻔했어요</p>
    <p>yiqilayozdim</p></div>
  <div class="pe-card"><p class="pe-card__h">다칠 뻔했어요</p>
    <p>jarohat olayozdim</p></div>
  <div class="pe-card"><p class="pe-card__h">늦을 뻔했어요</p>
    <p>kechikayozdim</p></div>
  <div class="pe-card"><p class="pe-card__h">울 뻔했어요</p>
    <p>yigʻlayozdim</p></div>
</div>

<div class="pe-call pe-tip">
  <p><b>죽을 뻔했어요</b> soʻzma-soʻz “oʻlayozdim” degani, lekin
  kundalik nutqda koʻpincha mubolagʻa: “juda qiynaldim”, “joyim
  qoldi”. Oʻzbekchada ham xuddi shunday deymiz — <em>“oʻlay
  dedim”</em>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">어제 너무 더워서 <span class="pe-hl pe-hl--v">죽을
     뻔했어요</span>.</p>
  <p class="pe-ex__uz">Kecha shunday issiq ediki, oʻlay dedim.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>계단에서 넘어질 뻔해요.</s></p>
  <p class="pe-good">계단에서 넘어질 <b>뻔했어요</b>.</p>
  <p><small>Bu qolip <b>doim oʻtgan zamonda</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>버스를 놓쳤을 뻔했어요.</s></p>
  <p class="pe-good">버스를 <b>놓칠</b> 뻔했어요.</p>
  <p><small>뻔 dan oldin faqat <b>(으)ㄹ</b> — ish hali
  boʻlmagan.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>날씨가 좋을 뻔했어요.</s></p>
  <p class="pe-good">날씨가 <b>좋았어요</b>. (yoki 좋을 것 같았어요)</p>
  <p><small>뻔하다 sifat bilan kelmaydi — u <b>hodisa</b> haqida,
  holat haqida emas.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>늦을 뻔 했지만 안 늦었어요, 그래서 늦었어요.</s></p>
  <p class="pe-good">늦을 뻔했어요. 하지만 <b>안 늦었어요</b>.</p>
  <p><small>뻔했다 aytilgan boʻlsa, ish <b>boʻlmagan</b> — keyin
  “boʻldi” deyish mantiqan qarama-qarshi.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 계단에서
  <span class="pe-blank"></span> 뻔했어요. (넘어지다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>넘어질</b> — 넘어지 da 받침 yoʻq → ㄹ 뻔했어요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 시험에
  <span class="pe-blank"></span> 뻔했어요. (늦다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>늦을</b> — 늦 da 받침 bor → 을 뻔했어요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> 버스를 놓칠 뻔했어요 — avtobusga
  mindimmi yoki yoʻqmi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>Mindim.</b> 뻔했어요 = boʻlishiga oz qoldi, lekin
    <em>boʻlmadi</em>. Avtobusni oʻtkazib yubormadim.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Xatoni toping:
  <s>지갑을 잃어버렸을 뻔했어요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>지갑을 잃어버릴 뻔했어요.</b> 뻔 dan oldin
    zamon qoʻshimchasi kelmaydi, faqat (으)ㄹ.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> “Sal boʻlmasa kechikardim” —
  하마터면 bilan ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>하마터면 늦을 뻔했어요.</b> 하마터면 bu qolip bilan
    juftlik boʻlib yuradi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Nega <s>날씨가 좋을 뻔했어요</s>
  notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>좋다 — <b>sifat</b>. 뻔하다 esa boʻlishi mumkin boʻlgan
    <em>hodisa</em> haqida, holat haqida emas.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)ㄹ 뻔하다</b> — sal boʻlmasa …moq</li>
  <li><b>하마터면</b> — sal boʻlmasa, oz qoldiki</li>
  <li><b>넘어지다</b> — yiqilmoq</li>
  <li><b>다치다</b> — jarohat olmoq</li>
  <li><b>놓치다</b> — oʻtkazib yubormoq, qoʻldan chiqarmoq</li>
  <li><b>계단</b> — zinapoya</li>
  <li><b>겨우</b> — arang</li>
  <li><b>위험하다</b> — xavfli</li>
  <li><b>미끄럽다</b> — sirpanchiq</li>
  <li><b>조심하다</b> — ehtiyot boʻlmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>(으)ㄹ 뻔했어요</b> = boʻlishiga oz qoldi, lekin
      <b>boʻlmadi</b>.</li>
    <li>받침 yoʻq → <b>ㄹ 뻔</b> · 받침 bor → <b>을 뻔</b>.</li>
    <li><b>Doim oʻtgan zamonda</b>: 뻔해요 ham, 뻔했을 ham emas.</li>
    <li>뻔 dan oldin <b>faqat (으)ㄹ</b> — zamon qoʻshimchasi
      qoʻyilmaydi.</li>
    <li>Koʻpincha <b>hodisa</b> va koʻpincha <b>yomon</b> hodisa
      haqida; sifat bilan kelmaydi.</li>
    <li><b>하마터면</b> bilan juftlik boʻlib yuradi.</li>
    <li>Oʻzbekcha juftligi: “yiqil<b>ayoz</b>dim”, “sal boʻlmasa
      yiqilardim”.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-64: (으)ㄹ 테니까 — soʻzlovchi irodasiga asoslangan sabab",
        "category": "korean",
        "order": 64,
        "summary": (
            "“Men qilaman, shuning uchun siz…” — sabab faktdan emas, "
            "soʻzlovchining niyati yoki kuchli taxminidan chiqadi."
        ),
        "stories": ["학교 축제 준비"],
        "content": """
<h2>PK-64: (으)ㄹ 테니까 — soʻzlovchi irodasiga asoslangan sabab</h2>

<p>Doʻstingiz bilan ish boʻlishyapsiz. “<b>Men</b> stolni tayyorlayman,
<b>shuning uchun sen</b> ovqatni olib kel” deysiz. Bu yerdagi “shuning
uchun” <em>fakt</em> emas — u sizning <b>vaʼdangiz</b>. PK-48 dagi
(으)니까 buni ayta olmaydi, chunki u boʻlib oʻtgan narsaga tayanadi.
Kelajakdagi niyatga tayanadigan sabab uchun koreys tilida alohida
qolip bor: <b>(으)ㄹ 테니까</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)ㄹ 테니까</b> bilan “men qilaman, shuning uchun…” deysiz</li>
    <li>Uning ikkinchi maʼnosini — <b>kuchli taxmin</b> — koʻrasiz</li>
    <li>Keyingi gapda nima kelishini bilib olasiz (buyruq yoki taklif)</li>
    <li>Uni <b>(으)니까</b> va <b>기 때문에</b> dan ajratasiz</li>
    <li>Oʻtgan zamon shakli <b>았/었을 테니까</b> ni oʻrganasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">Feʼl oʻzagi</span>
  <span class="pe-chip pe-chip--v">(으)ㄹ 테니까</span>
  <span class="pe-chip pe-chip--adv">= men …aman, shuning uchun</span>
</div>

<h3>1. Birinchi maʼnosi: soʻzlovchining niyati</h3>

<p>Ega <b>men</b> boʻlganda bu qolip vaʼda beradi: “men buni oʻz
zimmamga olaman”.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">제가 <span class="pe-hl pe-hl--v">준비할 테니까</span>
     걱정하지 마세요.</p>
  <p class="pe-ex__uz">Men tayyorlayman, shuning uchun xavotir olmang.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">제가 <span class="pe-hl pe-hl--v">도와줄 테니까</span>
     같이 해요.</p>
  <p class="pe-ex__uz">Men yordam beraman, shuning uchun birga qilaylik.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida bu farq ohangda yashiringan.</b> Biz ikkalasini
  ham “shuning uchun” deymiz:<br>
  “Yomgʻir yogʻ<b>di</b>, shuning uchun uyda qoldik” — bu <em>fakt</em>
  → koreyschada <b>(으)니까</b>.<br>
  “Men boraman, shuning uchun sen kutib tur” — bu <em>vaʼda</em>
  → koreyschada <b>(으)ㄹ 테니까</b>.<br>
  Yaʼni koreys tili oʻzbek tili ohang bilan aytadigan narsani
  <em>grammatika</em> bilan aytadi. Gapni tarjima qilishdan oldin
  soʻrang: bu sabab <b>boʻlib oʻtganmi</b> yoki <b>men vaʼda
  beryapmanmi?</b></p>
</div>

<h3>2. Yasalishi</h3>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">ㄹ 테니까</span></p>
    <p>가다 → 갈 테니까</p>
    <p>하다 → 할 테니까</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">을 테니까</span></p>
    <p>먹다 → 먹을 테니까</p>
    <p>읽다 → 읽을 테니까</p>
  </div>
</div>

<div class="pe-call pe-rule">
  <p><b>테 — yana bitta ot.</b> U <b>터</b> (“niyat, reja”) soʻzidan
  kelib chiqqan. Demak bu ham oʻsha tanish mashina: <em>aniqlovchi +
  ot</em> — PK-52 dagi 것, PK-53 dagi 줄, PK-63 dagi 뻔 bilan bir
  oila. Oldida (으)ㄹ turishi bejiz emas: gap <b>hali
  boʻlmagan</b> ish haqida.</p>
</div>

<h3>3. Ikkinchi maʼnosi: kuchli taxmin</h3>

<p>Ega <b>boshqa odam</b> yoki <b>narsa</b> boʻlsa, maʼno vaʼdadan
taxminga oʻzgaradi: “shunday boʻlsa kerak”.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">밖에 비가 <span class="pe-hl pe-hl--v">올 테니까</span>
     우산을 가져가세요.</p>
  <p class="pe-ex__uz">Tashqarida yomgʻir yogʻsa kerak, shuning uchun
  soyabon olib boring.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">자스루르 씨가 <span class="pe-hl pe-hl--v">바쁠
     테니까</span> 나중에 전화하세요.</p>
  <p class="pe-ex__uz">Jasur band boʻlsa kerak, shuning uchun keyinroq
  qoʻngʻiroq qiling.</p>
  <p class="pe-ex__why">Sifat bilan ham ishlaydi — bu <b>taxmin</b>
  maʼnosida.</p>
</div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Ega = men</p>
    <p><b>Niyat / vaʼda</b></p>
    <p><small>제가 할 테니까… — men qilaman, shuning uchun…</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Ega = boshqa</p>
    <p><b>Kuchli taxmin</b></p>
    <p><small>비가 올 테니까… — yomgʻir yogʻsa kerak, shuning
    uchun…</small></p>
  </div>
</div>

<h3>4. Keyingi gapda nima keladi?</h3>

<p>Bu qolipning eng muhim cheklovi. <b>(으)ㄹ 테니까</b> dan keyin
odatda <b>buyruq</b> ((으)세요) yoki <b>taklif</b> (아/어요)
keladi — chunki siz suhbatdoshdan <em>biror ish qilishini</em>
kutyapsiz.</p>

<div class="pe-steps">
  <div class="pe-step">
    <p><b>Toʻgʻri — buyruq bilan.</b><br>
    제가 갈 테니까 <span class="pe-hl pe-hl--v">기다리세요</span>.
    — Men boraman, kutib turing.</p>
  </div>
  <div class="pe-step">
    <p><b>Toʻgʻri — taklif bilan.</b><br>
    제가 도와줄 테니까 <span class="pe-hl pe-hl--v">같이 해요</span>.
    — Men yordam beraman, birga qilaylik.</p>
  </div>
  <div class="pe-step">
    <p><b>Gʻalati — oddiy darak gap bilan.</b><br>
    <s>제가 갈 테니까 동생이 집에 있었어요.</s> — bu qolip bunday
    ishlatilmaydi.</p>
  </div>
</div>

<div class="pe-call pe-warn">
  <p><b>Yana bir cheklov:</b> ega “men” boʻlganda, keyingi gapning
  egasi <b>boshqa odam</b> boʻlishi kerak. “Men qilaman, shuning uchun
  <em>men</em>…” degan gap mantiqan boʻsh — <s>제가 갈 테니까 제가
  준비할게요</s> ✗.</p>
</div>

<h3>5. (으)니까 va 기 때문에 bilan solishtiring</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Qolip</th><th>Sabab qayerdan</th><th>Keyingi gap</th><th>Misol</th></tr>
  <tr><td class="pk-stem">(으)니까 <small>PK-48</small></td>
      <td>boʻlib oʻtgan fakt</td><td>buyruq ham, darak ham</td>
      <td class="pk-res">비가 오니까 우산을 가져가세요</td></tr>
  <tr><td class="pk-stem">기 때문에 <small>PK-49</small></td>
      <td>obyektiv sabab</td><td>koʻpincha darak</td>
      <td class="pk-res">비가 오기 때문에 못 갔어요</td></tr>
  <tr><td class="pk-stem">(으)ㄹ 테니까</td>
      <td>niyat yoki taxmin</td><td>buyruq / taklif</td>
      <td class="pk-res">비가 올 테니까 우산을 가져가세요</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p>Yuqoridagi ikkita yomgʻir gapini solishtiring: <b>비가 오니까</b>
  — yomgʻir <em>hozir yogʻyapti</em>, men koʻrib turibman.
  <b>비가 올 테니까</b> — yomgʻir <em>hali yogʻmagan</em>, lekin
  yogʻsa kerak. Bitta soʻz butun vaziyatni oʻzgartiradi.</p>
</div>

<h3>6. Oʻtgan zamon: 았/었을 테니까</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">지영 씨가 벌써 <span class="pe-hl pe-hl--v">갔을
     테니까</span> 전화하지 마세요.</p>
  <p class="pe-ex__uz">Jiyon allaqachon ketgan boʻlsa kerak, shuning
  uchun qoʻngʻiroq qilmang.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>제가 준비하니까 걱정하지 마세요.</s></p>
  <p class="pe-good">제가 <b>준비할 테니까</b> 걱정하지 마세요.</p>
  <p><small>Hali qilmadingiz — bu <b>vaʼda</b>. (으)니까 boʻlib
  oʻtgan narsa uchun.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>비가 올 테니까 집에 있었어요.</s></p>
  <p class="pe-good">비가 <b>왔으니까</b> 집에 있었어요.</p>
  <p><small>(으)ㄹ 테니까 dan keyin oʻtgan zamon darak gapi
  kelmaydi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>제가 갈 테니까 제가 표를 사요.</s></p>
  <p class="pe-good">제가 <b>갈 테니까</b> <b>기다리세요</b>.</p>
  <p><small>Keyingi gapning egasi boshqa odam boʻlishi
  kerak.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>먹를 테니까 기다리세요.</s></p>
  <p class="pe-good"><b>먹을 테니까</b> 기다리세요.</p>
  <p><small>받침 bor → <b>을 테니까</b>.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 제가
  <span class="pe-blank"></span> 테니까 걱정하지 마세요. (준비하다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>준비할</b> — 하 da 받침 yoʻq → ㄹ 테니까.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 자스루르 씨가
  <span class="pe-blank"></span> 테니까 나중에 전화하세요. (바쁘다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>바쁠</b> — 바쁘 da 받침 yoʻq → ㄹ 테니까. Bu yerda maʼnosi
    <b>taxmin</b>: “band boʻlsa kerak”.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Farqini ayting:
  비가 오니까 / 비가 올 테니까.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>비가 오니까</b> — yomgʻir hozir yogʻyapti (fakt).
    <b>비가 올 테니까</b> — yomgʻir yogʻsa kerak (taxmin, hali
    yogʻmagan).</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Bu gapni tugating:
  제가 표를 살 테니까 …</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Masalan <b>… 자스루르 씨는 음식을 사세요.</b> Keyingi gapda
    <b>buyruq yoki taklif</b> keladi, va egasi boshqa odam
    boʻladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Xatoni toping:
  <s>비가 올 테니까 집에 있었어요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>비가 왔으니까 집에 있었어요.</b> Boʻlib oʻtgan
    ish uchun (으)니까 kerak.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> “Jiyon allaqachon ketgan boʻlsa
  kerak, qoʻngʻiroq qilmang” — koreyschada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>지영 씨가 벌써 갔을 테니까 전화하지 마세요.</b> Oʻtgan
    zamon — <b>았/었을 테니까</b>.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)ㄹ 테니까</b> — men …aman, shuning uchun; …sa kerak</li>
  <li><b>았/었을 테니까</b> — …gan boʻlsa kerak</li>
  <li><b>준비하다</b> — tayyorlamoq</li>
  <li><b>도와주다</b> — yordam bermoq</li>
  <li><b>걱정하다</b> — xavotirlanmoq</li>
  <li><b>나중에</b> — keyinroq</li>
  <li><b>벌써</b> — allaqachon</li>
  <li><b>축제</b> — bayram, festival</li>
  <li><b>맡다</b> — zimmasiga olmoq</li>
  <li><b>정하다</b> — belgilamoq, kelishmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>(으)ㄹ 테니까</b> = sabab faktdan emas, <b>niyat</b> yoki
      <b>taxmin</b>dan chiqadi.</li>
    <li>Ega <b>men</b> → vaʼda. Ega <b>boshqa</b> → kuchli taxmin.</li>
    <li>받침 yoʻq → <b>ㄹ 테니까</b> · 받침 bor → <b>을 테니까</b>.</li>
    <li>Keyingi gapda <b>buyruq yoki taklif</b> keladi, va uning egasi
      boshqa odam boʻladi.</li>
    <li>Oʻtgan zamon: <b>았/었을 테니까</b>.</li>
    <li><b>비가 오니까</b> (yogʻyapti) va <b>비가 올 테니까</b> (yogʻsa
      kerak) — bittasi fakt, ikkinchisi taxmin.</li>
    <li><b>테</b> ← 터 (“niyat”) — yana bitta aniqlovchi + ot: 것 ·
      줄 · 뻔 · 테.</li>
  </ul>
</div>
""",
    },
]
