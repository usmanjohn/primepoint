# -*- coding: utf-8 -*-
"""Prime Korean — Block D, darslar 38–40.

38. 기 전에 / (으)ㄴ 후에 — oldin va keyin
39. (으)면서 — bir vaqtda ikki ish
40. (으)려고 하다 — niyat va reja

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

Oʻqish matnlari: corner/management/commands/_stories_prime_korean_38_40.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_38_40.py --author=prime
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
        "title": "PK-38: 기 전에 / (으)ㄴ 후에 — oldin va keyin",
        "category": "korean",
        "order": 38,
        "summary": (
            "Ikki ishning tartibini aytish. 기 전에 — “…dan oldin”, (으)ㄴ 후에 — "
            "“…dan keyin”. Nega ikkisi ikki xil shaklda va zamon qayerda turadi."
        ),
        "stories": ["자기 전에 무엇을 해요?"],
        "content": """
<h2>PK-38: 기 전에 / (으)ㄴ 후에 — oldin va keyin</h2>

<p>Kun tartibingizni koreyscha aytib bermoqchisiz: “Nonushta qilish<b>dan oldin</b>
yuzimni yuvaman, dars tugagan<b>dan keyin</b> doʻstim bilan uchrashaman.” Oʻzbek tilida
ikkalasi ham bir xil ishlaydi — soʻzga “-dan oldin” yoki “-dan keyin” qoʻshasiz, xolos.
Koreys tilida esa <b>ikkita boshqa-boshqa shakl</b> bor: “oldin” uchun <b>기 전에</b>,
“keyin” uchun <b>(으)ㄴ 후에</b>. Bu bejiz emas — buning ichida juda chiroyli mantiq
yashiringan, va shu mantiqni tushunsangiz, ikkalasini hech qachon aralashtirmaysiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>기 전에</b> bilan “…dan oldin” deyishni oʻrganasiz</li>
    <li><b>(으)ㄴ 후에</b> bilan “…dan keyin” deyishni — 받침 ayrisi bilan birga</li>
    <li>Ot bilan ishlatiladigan <b>전에 / 후에</b> shaklini koʻrasiz</li>
    <li>Zamon qayerda turishini bir marta va butunlay hal qilasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Oldin</span>
  <span class="pe-chip pe-chip--s">A oʻzak</span>
  <span class="pe-chip pe-chip--v">기 전에</span>
  <span class="pe-chip pe-chip--opt">+</span>
  <span class="pe-chip pe-chip--o">B</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Keyin</span>
  <span class="pe-chip pe-chip--s">A oʻzak</span>
  <span class="pe-chip pe-chip--v">(으)ㄴ 후에</span>
  <span class="pe-chip pe-chip--opt">+</span>
  <span class="pe-chip pe-chip--o">B</span>
</div>

<h3>1. 기 전에 — hech qanday ayri yoʻq</h3>

<p>Yaxshi xabar bilan boshlaymiz. <b>기 전에</b> eng oson qoʻshimchalardan biri: feʼl
oʻzagiga shundoq qoʻshiladi, tamom. 받침 bor-yoʻqligi ahamiyatsiz, notoʻgʻri feʼllar
ham oʻzgarmaydi.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Oʻzak</th><th>Qoʻshimcha</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>가다</td><td class="pk-stem">가</td><td class="pk-end">기 전에</td>
      <td class="pk-res">가기 전에</td><td class="pk-uz">borishdan oldin</td></tr>
  <tr><td>먹다</td><td class="pk-stem">먹</td><td class="pk-end">기 전에</td>
      <td class="pk-res">먹기 전에</td><td class="pk-uz">yeyishdan oldin</td></tr>
  <tr><td>듣다</td><td class="pk-stem">듣</td><td class="pk-end">기 전에</td>
      <td class="pk-res">듣기 전에</td><td class="pk-uz">tinglashdan oldin</td></tr>
  <tr><td>덥다</td><td class="pk-stem">덥</td><td class="pk-end">기 전에</td>
      <td class="pk-res">덥기 전에</td><td class="pk-uz">isishdan oldin</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Nega 듣다 va 덥다 oʻzgarmadi?</b> PK-32 dagi qoidani eslang: notoʻgʻri tuslanish
  faqat <b>unli bilan boshlanadigan</b> qoʻshimcha oldida ishlaydi. <b>기</b> esa ㄱ —
  undosh. Shuning uchun oʻzak joyida qoladi. Bu qoida butun kurs boʻyicha ishlaydi va
  shu darsning ikkinchi yarmida yana kerak boʻladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--o">밥을</span>
     <span class="pe-hl pe-hl--v">먹기 전에</span> 손을 씻어요.</p>
  <p class="pe-ex__uz">Ovqat yeyishdan oldin qoʻlimni yuvaman.</p>
  <p class="pe-ex__why">기 전에 — birinchi ish hali boʻlmagan; asosiy kesim oxirda.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 <span class="pe-hl pe-hl--v">자기 전에</span> 한국어를
     공부해요.</p>
  <p class="pe-ex__uz">Men uxlashdan oldin koreys tilini oʻrganaman.</p>
</div>

<h3>2. Ot + 전에</h3>

<p>Agar “oldin” dan oldin feʼl emas, <b>ot</b> tursa, 기 kerak emas — ot toʻgʻridan
toʻgʻri <b>전에</b> ni oladi.</p>

<ul>
  <li>수업 <b>전에</b> — darsdan oldin</li>
  <li>식사 <b>전에</b> — ovqatdan oldin</li>
  <li>여행 <b>전에</b> — sayohatdan oldin</li>
  <li>시험 <b>전에</b> — imtihondan oldin</li>
</ul>

<p>Vaqt bildiruvchi soʻz bilan esa <b>전에</b> “…burun / …oldin” maʼnosini beradi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--adv">두 시간 전에</span> 지영 씨를
     만났어요.</p>
  <p class="pe-ex__uz">Ikki soat oldin Chiyongni uchratdim.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tili bilan solishtiring.</b> “Ikki soat oldin” — 두 시간 전에. Soʻz
  tartibi <b>bir xil</b>: son → oʻlchov soʻzi → “oldin”. Ingliz tilida bu teskari
  (“two hours <em>ago</em>”), oʻzbek tilida esa aynan koreyschadek. Shuning uchun bu
  qismni yodlashning hojati yoʻq — oʻzbekcha oʻylang, koreyscha chiqadi.</p>
</div>

<h3>3. (으)ㄴ 후에 — bu yerda 받침 ayrisi bor</h3>

<p>“Keyin” tomoni biroz jiddiyroq: qoʻshimcha <b>(으)</b> bilan boshlanadi, demak
받침 ga qaraymiz.</p>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">ㄴ 후에</span></p>
    <p>가다 → 간 후에 · 보다 → 본 후에 · 오다 → 온 후에</p>
    <p>Oʻzak unli bilan tugasa, ㄴ shundoq ustiga oʻtiradi.</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">은 후에</span></p>
    <p>먹다 → 먹은 후에 · 읽다 → 읽은 후에 · 씻다 → 씻은 후에</p>
    <p>Oʻzak undosh bilan tugasa, orasiga 으 kiradi.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--o">숙제를</span>
     <span class="pe-hl pe-hl--v">한 후에</span> 게임을 해요.</p>
  <p class="pe-ex__uz">Uy vazifasini qilgandan keyin oʻyin oʻynayman.</p>
  <p class="pe-ex__why">하다 → 하 (받침 yoʻq) → 한 후에.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">점심을 <span class="pe-hl pe-hl--v">먹은 후에</span>
     커피를 마셨어요.</p>
  <p class="pe-ex__uz">Tushlik qilgandan keyin qahva ichdim.</p>
</div>

<h3>4. Notoʻgʻri feʼllar bu yerda ishlaydi</h3>

<p>Yuqorida aytdik: 기 undosh, shuning uchun hech nima oʻzgarmadi. Ammo <b>(으)ㄴ</b>
unli bilan boshlanadi — demak PK-32 dagi oʻzgarishlar bu yerda <b>albatta</b> ishlaydi.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>기 전에 <small>(undosh — oʻzgarmaydi)</small></th>
      <th>(으)ㄴ 후에 <small>(unli — oʻzgaradi)</small></th></tr>
  <tr><td>듣다</td><td class="pk-uz">듣기 전에</td><td class="pk-res">들은 후에</td></tr>
  <tr><td>걷다</td><td class="pk-uz">걷기 전에</td><td class="pk-res">걸은 후에</td></tr>
  <tr><td>돕다</td><td class="pk-uz">돕기 전에</td><td class="pk-res">도운 후에</td></tr>
</table></div>

<p>Yana bitta kichik guruh — <b>ㄹ</b> bilan tugaydigan oʻzaklar. Ular ㄴ oldida
ㄹ ni <b>yoʻqotadi</b>:</p>

<ul>
  <li>놀다 → <b>논 후에</b> (oʻynagandan keyin)</li>
  <li>만들다 → <b>만든 후에</b> (yasagandan keyin)</li>
  <li>살다 → <b>산 후에</b> (yashagandan keyin)</li>
</ul>

<div class="pe-call pe-uz">
  <p><b>Gap tuzilishi ham bir xil.</b> 밥을 먹은 후에 커피를 마셨어요 —
  “ovqat yegandan keyin qahva ichdim”. Ikkala tilda ham ergash gap <b>oldinda</b>,
  asosiy kesim <b>oxirida</b> turadi. Ingliz tilida esa teskari boʻlishi mumkin
  (“I drank coffee after…”). Yaʼni koreyscha gapni tuzayotganda oʻzbekcha jumlani
  soʻzma-soʻz ketma-ketlikda tarjima qilsangiz, tartib deyarli har doim toʻgʻri
  chiqadi — faqat qoʻshimchalarni almashtirasiz.</p>
</div>

<h3>5. 후에 = 다음에 = 뒤에</h3>

<p>Koreyslar bir xil maʼnoda uchta soʻzni ishlatadi. Ular <b>toʻliq oʻrin almashadi</b>:</p>

<div class="pe-grid">
  <div class="pe-card"><b>(으)ㄴ 후에</b><br><small>Eng rasmiy, yozma nutqda koʻp</small></div>
  <div class="pe-card"><b>(으)ㄴ 다음에</b><br><small>Kundalik suhbatda eng koʻp</small></div>
  <div class="pe-card"><b>(으)ㄴ 뒤에</b><br><small>Ham yozma, ham ogʻzaki</small></div>
</div>

<p>밥을 먹은 후에 = 밥을 먹은 다음에 = 밥을 먹은 뒤에 — uchalasi ham “ovqat yegandan
keyin”. Ot bilan ham xuddi shunday: 수업 후에 = 수업 다음에.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">한국에 <span class="pe-hl pe-hl--v">간 다음에</span>
     친구를 만날 거예요.</p>
  <p class="pe-ex__uz">Koreyaga borganimdan keyin doʻstim bilan uchrashaman.</p>
</div>

<h3>6. Zamon qayerda turadi?</h3>

<p>Bu — butun darsning eng muhim qoidasi, va u tanish boʻlishi kerak: <b>아/어서</b>
(PK-35) va <b>(으)면</b> (PK-36) da ham xuddi shunday edi.</p>

<div class="pe-call pe-rule">
  <p><b>기 전에 va (으)ㄴ 후에 dan OLDIN zamon qoʻyilmaydi.</b> Butun gapning zamoni
  faqat <b>oxirgi feʼlda</b> turadi va u orqaga — birinchi qismga ham — tarqaladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>밥을 먹었기 전에 손을 씻었어요.</s></p>
  <p class="pe-good">밥을 <b>먹기 전에</b> 손을 씻었어요.</p>
  <p><small>Oxiridagi 씻었어요 allaqachon “oʻtgan zamon” deb aytdi.
  Buni ikki marta aytish shart emas.</small></p>
</div>

<div class="pe-call pe-uz">
  <p><b>Yaxshi xabar.</b> Oʻzbek tilida ham biz “ovqat <em>yedim</em>dan oldin” demaymiz —
  “ovqat <em>yeyishdan</em> oldin” deymiz, zamonni esa oxirgi feʼlga qoʻyamiz: “…yuvdim”.
  Yaʼni koreyscha qoida oʻzbekcha odat bilan aynan bir xil. Bu xatoni koʻproq ingliz
  tilidan oʻrganganlar qiladi, siz emas.</p>
</div>

<h3>7. Nega ikki xil shakl? — esda qoladigan mantiq</h3>

<p>Endi darsning boshidagi savolga qaytamiz. Nega “oldin” uchun 기, “keyin” uchun (으)ㄴ?</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">기 전에</p>
    <p>Siz gapirayotgan paytda birinchi ish <b>hali boʻlmagan</b>.</p>
    <p>Shuning uchun <b>tugallanmagan</b> shakl — 기.</p>
    <p>밥을 먹<b>기</b> 전에 — ovqat hali yeyilmagan.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">(으)ㄴ 후에</p>
    <p>Siz gapirayotgan paytda birinchi ish <b>tugagan</b>.</p>
    <p>Shuning uchun <b>tugallangan</b> shakl — (으)ㄴ.</p>
    <p>밥을 먹<b>은</b> 후에 — ovqat allaqachon yeyilgan.</p>
  </div>
</div>

<div class="pe-call pe-tip">
  <p><b>Yodlash oʻrniga:</b> 전에 — ish oldinda, hali boʻlmagan → 기. 후에 — ish orqada,
  boʻlib boʻlgan → (으)ㄴ. Bir necha kun shu jumlani takrorlang, keyin oʻzi keladi.
  Aytgancha, bu <b>(으)ㄴ</b> — koreys tilining “tugagan ish” belgisi; PK-44 da uni
  toʻliq oʻrganasiz. Hozircha 후에 bilan birga bitta boʻlak sifatida yod oling.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>밥을 먹은 전에 손을 씻어요.</s></p>
  <p class="pe-good">밥을 <b>먹기</b> 전에 손을 씻어요.</p>
  <p><small>Shakllar almashib ketgan. 전에 doim <b>기</b> bilan yuradi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>숙제를 하기 후에 잤어요.</s></p>
  <p class="pe-good">숙제를 <b>한</b> 후에 잤어요.</p>
  <p><small>후에 doim <b>(으)ㄴ</b> bilan yuradi. 기 후에 degan shakl yoʻq.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>음악을 듣은 후에 공부했어요.</s></p>
  <p class="pe-good">음악을 <b>들은</b> 후에 공부했어요.</p>
  <p><small>듣다 — ㄷ notoʻgʻri feʼli. (으)ㄴ unli bilan boshlanadi,
  demak ㄷ → ㄹ oʻzgarishi ishlaydi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>친구를 만들은 후에 …</s></p>
  <p class="pe-good">친구를 <b>만든</b> 후에 …</p>
  <p><small>ㄹ bilan tugagan oʻzak ㄴ oldida ㄹ ni yoʻqotadi:
  만들 + ㄴ → 만든.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>수업하기 전에 → “darsdan oldin” demoqchi boʻlsangiz</s></p>
  <p class="pe-good"><b>수업 전에</b></p>
  <p><small>수업 — ot. Ot bilan 기 kerak emas, 전에 shundoq qoʻshiladi.
  (수업하기 전에 — “dars <em>oʻtishdan</em> oldin”, yaʼni oʻqituvchi haqida.)</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 학교에 <span class="pe-blank"></span>
  (가다) 전에 아침을 먹어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>가기</b> — 학교에 가기 전에 아침을 먹어요. 전에 doim 기 bilan; 받침 ham,
    notoʻgʻri feʼl ham bu yerda ahamiyatsiz.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 책을 <span class="pe-blank"></span>
  (읽다) 후에 잤어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>읽은</b> — 책을 읽은 후에 잤어요. 읽 da 받침 bor (ㄺ), shuning uchun 은 후에.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Xatoni toping: <s>운동을 했기 전에 물을
  마셨어요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>운동을 하기 전에 물을 마셨어요.</b> 기 전에 dan oldin zamon
    qoʻyilmaydi; oxiridagi 마셨어요 butun gapni oʻtmishga oladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Koreyschaga oʻgiring: “Musiqa tinglagandan keyin
  uy vazifasini qildim.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>음악을 들은 후에 숙제를 했어요.</b> Diqqat: 듣다 → 들은 (ㄷ → ㄹ), chunki
    (으)ㄴ unli bilan boshlanadi. 후에 oʻrniga 다음에 yoki 뒤에 ham boʻladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Qaysi biri toʻgʻri va nega?
  (a) 시험 전에 &nbsp; (b) 시험하기 전에</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>(a) 시험 전에</b> — “imtihondan oldin”. 시험 — ot, shuning uchun 기 kerak emas.
    시험하기 전에 boshqa maʼno beradi: “imtihon <em>oʻtkazishdan</em> oldin”.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Ikki gapni bittaga birlashtiring:
  한국에 갔어요. + 한국어를 배웠어요. (avval Koreyaga bordi)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>한국에 간 후에 한국어를 배웠어요.</b> Birinchi ish tugagan, shuning uchun
    (으)ㄴ 후에. 갔 emas, <b>간</b> — zamon faqat oxirgi feʼlda.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>기 전에</b> — …dan oldin (feʼl bilan)</li>
  <li><b>전에</b> — …dan oldin (ot yoki vaqt bilan)</li>
  <li><b>(으)ㄴ 후에</b> — …dan keyin</li>
  <li><b>(으)ㄴ 다음에</b> — …dan keyin (suhbatda eng koʻp)</li>
  <li><b>(으)ㄴ 뒤에</b> — …dan keyin</li>
  <li><b>수업</b> — dars</li>
  <li><b>식사</b> — ovqatlanish, taom</li>
  <li><b>시험</b> — imtihon</li>
  <li><b>씻다</b> — yuvmoq</li>
  <li><b>만들다</b> — yasamoq, tayyorlamoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>기 전에</b> — hech qanday ayri yoʻq, oʻzakka shundoq qoʻshiladi.</li>
    <li><b>(으)ㄴ 후에</b> — 받침 yoʻq → ㄴ 후에, 받침 bor → 은 후에.</li>
    <li>(으) unli, shuning uchun notoʻgʻri feʼllar bu yerda ishlaydi: 듣다 → 들은 후에.</li>
    <li>ㄹ oʻzak ㄴ oldida ㄹ ni yoʻqotadi: 만들다 → 만든 후에.</li>
    <li>Ot bilan 기 kerak emas: 수업 전에, 시험 후에.</li>
    <li>후에 = 다음에 = 뒤에 — toʻliq oʻrin almashadi.</li>
    <li>Ikkalasidan ham <b>oldin zamon qoʻyilmaydi</b> — zamon oxirgi feʼlda.</li>
    <li>Mantiq: 전에 → ish hali boʻlmagan → 기 · 후에 → ish tugagan → (으)ㄴ.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-39: (으)면서 — bir vaqtda ikki ish",
        "category": "korean",
        "order": 39,
        "summary": (
            "“Musiqa tinglab dars qilaman.” (으)면서 ikki ishni bir vaqtga qoʻyadi. "
            "받침 ayrisi, ega bir xil boʻlishi sharti va 고 bilan farqi."
        ),
        "stories": ["음악을 들으면서 공부해요"],
        "content": """
<h2>PK-39: (으)면서 — bir vaqtda ikki ish</h2>

<p>“Men <b>musiqa tinglab</b> dars qilaman.” Oʻzbek tilida bu juda oddiy gap. Lekin
oʻtgan darslardagi qoliplarning hech biri buni ayta olmaydi: <b>고</b> (PK-33) ikki ishni
navbat bilan sanaydi, <b>아/어서</b> (PK-35) esa biri ikkinchisiga sabab boʻlganda
ishlatiladi. Bizga kerak boʻlgani boshqa narsa — ikkala ish <b>ayni bir paytda</b>
sodir boʻlyapti. Bu qolipning nomi — <b>(으)면서</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)면서</b> ni 받침 ga qarab toʻgʻri yasaysiz</li>
    <li>Uning bitta qatʼiy shartini oʻrganasiz: <b>ega bir xil boʻlishi kerak</b></li>
    <li><b>고</b> va <b>(으)면서</b> ni ishonch bilan ajratasiz</li>
    <li>“ham …, ham …” degan ikkinchi maʼnosini koʻrasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">A oʻzak</span>
  <span class="pe-chip pe-chip--v">(으)면서</span>
  <span class="pe-chip pe-chip--opt">+</span>
  <span class="pe-chip pe-chip--o">B</span>
  <span class="pe-chip pe-chip--adv">= A qilib turib B</span>
</div>

<h3>1. Yasalishi — 받침 ayrisi</h3>

<p>Qoʻshimcha <b>(으)</b> bilan boshlanadi, demak birinchi savol doim bitta:
oʻzak undosh bilan tugadimi?</p>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">면서</span></p>
    <p>보다 → 보면서 · 마시다 → 마시면서 · 하다 → 하면서</p>
    <p>Oʻzak unli bilan tugasa, 으 kerak emas.</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">으면서</span></p>
    <p>먹다 → 먹으면서 · 읽다 → 읽으면서 · 웃다 → 웃으면서</p>
    <p>Oʻzak undosh bilan tugasa, orasiga 으 kiradi.</p>
  </div>
</div>

<div class="pe-call pe-tip">
  <p>Bu aynan <b>(으)면</b> (PK-36) ning ayrisi — ustiga faqat <b>서</b> qoʻshilgan.
  Yaʼni yangi qoida yodlashning hojati yoʻq: 먹으면 → 먹으면서, 가면 → 가면서.
  Faqat maʼnosi butunlay boshqa: (으)면 — shart, (으)면서 — bir vaqtdalik.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 <span class="pe-hl pe-hl--o">커피를</span>
     <span class="pe-hl pe-hl--v">마시면서</span> 신문을 읽어요.</p>
  <p class="pe-ex__uz">Men qahva ichib gazeta oʻqiyman.</p>
  <p class="pe-ex__why">Ikkala ish ham ayni bir daqiqada sodir boʻlyapti.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">아프소나 씨는 <span class="pe-hl pe-hl--v">웃으면서</span>
     인사했어요.</p>
  <p class="pe-ex__uz">Afsona kulib salomlashdi.</p>
</div>

<h3>2. ㄹ bilan tugagan oʻzaklar</h3>

<p>PK-36 dagidek, <b>ㄹ</b> oʻzaklar 으 ni olmaydi, lekin ㄹ ham tushmaydi — u
joyida qoladi:</p>

<ul>
  <li>살다 → <b>살면서</b> (yashab turib)</li>
  <li>만들다 → <b>만들면서</b> (yasab turib)</li>
  <li>놀다 → <b>놀면서</b> (oʻynab turib)</li>
</ul>

<h3>3. Notoʻgʻri feʼllar bu yerda ishlaydi</h3>

<p>(으) unli bilan boshlanadi — demak PK-32 dagi oʻzgarishlar yana ishga tushadi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Oʻzak</th><th>Oʻzgarish</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>듣다</td><td class="pk-stem">듣</td><td class="pk-end">ㄷ → ㄹ</td>
      <td class="pk-res">들으면서</td><td class="pk-uz">tinglab turib</td></tr>
  <tr><td>걷다</td><td class="pk-stem">걷</td><td class="pk-end">ㄷ → ㄹ</td>
      <td class="pk-res">걸으면서</td><td class="pk-uz">yurib turib</td></tr>
  <tr><td>돕다</td><td class="pk-stem">돕</td><td class="pk-end">ㅂ → 우</td>
      <td class="pk-res">도우면서</td><td class="pk-uz">yordam berib turib</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 음악을 <span class="pe-hl pe-hl--v">들으면서</span>
     공부해요.</p>
  <p class="pe-ex__uz">Men musiqa tinglab dars qilaman.</p>
  <p class="pe-ex__why">듣 + 으면서 → 들으면서. <s>듣으면서</s> emas!</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida buning aniq juftligi bor.</b> Biz “yur<em>a</em>-yur<em>a</em>
  gapirdi”, “kul<em>a</em>-kul<em>a</em> aytdi” deymiz — feʼlni ikki marta takrorlab,
  ikki ishni bir vaqtga qoʻyamiz. <b>(으)면서</b> aynan shu ishni qiladi:
  걸으면서 말했어요, 웃으면서 말했어요. Shuning uchun oʻzbekcha “-a-…-a” shaklini
  koʻrsangiz, koreyschada bu deyarli har doim (으)면서 boʻladi.</p>
</div>

<h3>4. Bitta qatʼiy shart: ega bir xil boʻlishi kerak</h3>

<p>Bu (으)면서 ning eng muhim qoidasi va uni buzish — eng koʻp uchraydigan xato.</p>

<div class="pe-call pe-rule">
  <p><b>(으)면서 ning ikki tomonidagi ishni AYNI BIR ODAM bajarishi shart.</b>
  Ikki xil odam boʻlsa, (으)면서 ni ishlatib boʻlmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>제가 공부하면서 동생이 텔레비전을 봐요.</s></p>
  <p class="pe-good">저는 공부하<b>고</b> 동생은 텔레비전을 봐요.</p>
  <p><small>Bir odam oʻqiyapti, boshqasi televizor koʻryapti — ikki xil
  ega. Bunday holda <b>고</b> ishlatiladi.</small></p>
</div>

<p>Toʻgʻri ishlatilishida esa ega bitta, va uni odatda faqat bir marta aytamiz:</p>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--s">지영 씨는</span> 노래를
     <span class="pe-hl pe-hl--v">부르면서</span> 요리해요.</p>
  <p class="pe-ex__uz">Chiyong qoʻshiq aytib ovqat pishiradi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu qoida oʻzbek tilida ham bor — faqat biz uni sezmaymiz.</b> “Men gapirib
  u ketdi” degan gap oʻzbekchada ham gʻalati eshitiladi, chunki “-ib” ham ikkala
  tomonni bir odamga bogʻlaydi. Toʻgʻrisi — “men gapirdim, u ketdi”. Koreys tili
  shu tuygʻuni qatʼiy qoidaga aylantirgan, xolos. Yaʼni bu yerda yangi narsa
  oʻrganmayapsiz — bilganingizni rasmiylashtiryapsiz.</p>
</div>

<h3>5. Zamon (으)면서 dan oldin qoʻyilmaydi</h3>

<p>Tanish qoida — <b>아/어서</b>, <b>(으)면</b> va <b>기 전에</b> dagi bilan bir xil:</p>

<div class="pe-fix">
  <p class="pe-bad"><s>어제 음악을 들었으면서 공부했어요.</s></p>
  <p class="pe-good">어제 음악을 <b>들으면서</b> 공부했어요.</p>
  <p><small>Oxiridagi 공부했어요 butun gapni oʻtmishga oladi. Zamonni
  ikki marta aytish shart emas.</small></p>
</div>

<h3>6. (으)면서 va 고 — asosiy farq</h3>

<p>Bu ikkisi ingliz yoki oʻzbek tiliga koʻpincha bir xil tarjima qilinadi, shuning
uchun ularni <b>maʼnosi</b> bilan emas, <b>vaqti</b> bilan ajratish kerak.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">밥을 먹<b>고</b> 텔레비전을 봐요</p>
    <p>Avval ovqat, <b>keyin</b> televizor.</p>
    <p>Ikki ish — ketma-ket, alohida-alohida.</p>
    <p><small>Ovqatni tugatib, keyin oʻtirib televizor koʻrdi.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">밥을 먹<b>으면서</b> 텔레비전을 봐요</p>
    <p>Ovqat ham, televizor ham — <b>bir paytda</b>.</p>
    <p>Ikki ish bir-birining ustiga tushgan.</p>
    <p><small>Ovqat yeb oʻtirib, ekranga qarab turibdi.</small></p>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Nima uchun oʻzbek oʻquvchiga bu qiyin.</b> Oʻzbek tilida ikkalasi ham
  “-b / -ib” bilan chiqadi: “ovqat <em>yeb</em> televizor koʻrdim”. Bu gap oʻzbekchada
  <b>ikki xil</b> tushunilishi mumkin — ovqatni tugatib, yoki ovqat yeb oʻtirib.
  Koreys tili esa buni aralashtirmaydi. Shuning uchun tarjimaga emas,
  <b>bitta savolga</b> tayaning: <em>ikkala ish bir daqiqada birga sodir
  boʻlyaptimi?</em> Ha boʻlsa — 면서, yoʻq boʻlsa — 고.</p>
</div>

<h3>7. Ikkinchi maʼnosi: “ham …, ham …”</h3>

<p>Sifatlar bilan ishlatilganda <b>(으)면서</b> vaqtni emas, <b>ikki xususiyatni</b>
birlashtiradi. Bu TOPIK matnlarida tez-tez uchraydi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">그 식당은 <span class="pe-hl pe-hl--adv">싸면서</span>
     맛있어요.</p>
  <p class="pe-ex__uz">U oshxona ham arzon, ham mazali.</p>
  <p class="pe-ex__why">Bu yerda “bir vaqtda” emas — bir narsaning ikki yaxshi tomoni.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">한국어는 <span class="pe-hl pe-hl--adv">어려우면서</span>
     재미있어요.</p>
  <p class="pe-ex__uz">Koreys tili ham qiyin, ham qiziqarli.</p>
  <p class="pe-ex__why">어렵다 → 어려우면서 (ㅂ notoʻgʻri feʼli).</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>밥을 먹면서 텔레비전을 봐요.</s></p>
  <p class="pe-good">밥을 <b>먹으면서</b> 텔레비전을 봐요.</p>
  <p><small>먹 da 받침 bor, shuning uchun 으 tushib qolmasligi kerak.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>음악을 듣으면서 공부해요.</s></p>
  <p class="pe-good">음악을 <b>들으면서</b> 공부해요.</p>
  <p><small>듣다 — ㄷ notoʻgʻri feʼli, (으) unli oldida ㄷ → ㄹ.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>어머니가 요리하면서 저는 숙제를 해요.</s></p>
  <p class="pe-good">어머니는 요리하<b>고</b> 저는 숙제를 해요.</p>
  <p><small>Ega ikki xil — onam va men. (으)면서 buni koʻtarmaydi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>커피를 마셨으면서 이야기했어요.</s></p>
  <p class="pe-good">커피를 <b>마시면서</b> 이야기했어요.</p>
  <p><small>(으)면서 dan oldin zamon qoʻyilmaydi.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 저는 신문을
  <span class="pe-blank"></span> (읽다) 커피를 마셔요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>읽으면서</b> — 읽 da 받침 bor (ㄺ), shuning uchun 으면서.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 지영 씨는 <span class="pe-blank"></span>
  (걷다) 전화해요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>걸으면서</b> — 걷다 ㄷ notoʻgʻri feʼli; 으 unli oldida ㄷ → ㄹ.
    <s>걷으면서</s> notoʻgʻri.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> 고 yoki (으)면서? “Avval dushga tushdim,
  keyin uxladim.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>고</b> — 샤워하고 잤어요. Ikki ish ketma-ket, bir vaqtda emas.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Xatoni toping:
  <s>제가 노래하면서 친구가 춤을 춰요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Ega ikki xil (men va doʻstim). Toʻgʻrisi — <b>저는 노래하고 친구는 춤을 춰요.</b>
    Agar bitta odam qilsa, unda (으)면서 boʻladi: <b>저는 노래하면서 춤을 춰요.</b></p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Koreyschaga oʻgiring: “Ukam televizor koʻrib
  ovqat yeydi.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>동생은 텔레비전을 보면서 밥을 먹어요.</b> 보 da 받침 yoʻq → 보면서.
    Ega bitta, shuning uchun (으)면서 mumkin.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Bu gapda (으)면서 qaysi maʼnoda?
  이 가방은 가벼우면서 튼튼해요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>“Ham …, ham …” maʼnosida: <b>Bu sumka ham yengil, ham mustahkam.</b>
    Sifatlar bilan (으)면서 vaqtni emas, ikki xususiyatni birlashtiradi.
    (가볍다 → 가벼우면서 — ㅂ notoʻgʻri feʼli.)</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)면서</b> — …ib turib, bir vaqtda</li>
  <li><b>신문</b> — gazeta</li>
  <li><b>웃다</b> — kulmoq</li>
  <li><b>노래를 부르다</b> — qoʻshiq aytmoq</li>
  <li><b>요리하다</b> — ovqat pishirmoq</li>
  <li><b>춤을 추다</b> — raqsga tushmoq</li>
  <li><b>가볍다</b> — yengil</li>
  <li><b>튼튼하다</b> — mustahkam, baquvvat</li>
  <li><b>싸다</b> — arzon</li>
  <li><b>전화하다</b> — telefon qilmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>(으)면서</b> = ikki ish bir vaqtda sodir boʻladi.</li>
    <li>받침 yoʻq → 면서 · 받침 bor → 으면서 · ㄹ oʻzak → 면서 (ㄹ joyida qoladi).</li>
    <li>(으) unli, shuning uchun notoʻgʻri feʼllar ishlaydi: 듣다 → 들으면서.</li>
    <li><b>Ega ikkala tomonda bir xil boʻlishi shart.</b> Boʻlmasa — 고.</li>
    <li>Zamon (으)면서 dan oldin qoʻyilmaydi — u oxirgi feʼlda.</li>
    <li>고 — ketma-ket · (으)면서 — bir vaqtda. Savol: bir daqiqada birga boʻlyaptimi?</li>
    <li>Sifatlar bilan (으)면서 “ham …, ham …” degani: 싸면서 맛있어요.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-40: (으)려고 하다 — niyat va reja",
        "category": "korean",
        "order": 40,
        "summary": (
            "“…moqchiman”. Koʻnglingizdagi niyatni aytish, uni (으)ㄹ 거예요 dan "
            "ajratish va 려고 ni maqsad bogʻlovchisi sifatida ishlatish."
        ),
        "stories": ["방학에 뭐 하려고 해요?"],
        "content": """
<h2>PK-40: (으)려고 하다 — niyat va reja</h2>

<p>PK-27 da siz <b>(으)ㄹ 거예요</b> ni oʻrgandingiz — kelasi zamon. Lekin oʻylab koʻring:
“Ertaga kutubxonaga <b>boraman</b>” bilan “Ertaga kutubxonaga <b>bormoqchiman</b>”
orasida farq bor. Birinchisi — qaror qilingan ish, ikkinchisi — hali koʻngildagi niyat.
Koreys tili bu farqni juda aniq koʻrsatadi, va niyat tomonining nomi —
<b>(으)려고 하다</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)려고 하다</b> bilan niyat va rejani aytasiz</li>
    <li>Uni <b>(으)ㄹ 거예요</b> dan ajratasiz</li>
    <li><b>…려고 했어요</b> bilan “…moqchi edim, lekin…” deysiz</li>
    <li>하다siz <b>(으)려고</b> ni maqsad bogʻlovchisi sifatida ishlatasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">Feʼl oʻzagi</span>
  <span class="pe-chip pe-chip--v">(으)려고</span>
  <span class="pe-chip pe-chip--v">하다</span>
  <span class="pe-chip pe-chip--adv">= …moqchiman</span>
</div>

<h3>1. Yasalishi</h3>

<p>Yana oʻsha tanish ayri: qoʻshimcha <b>(으)</b> bilan boshlanadi.</p>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">려고 하다</span></p>
    <p>가다 → 가려고 해요 · 보다 → 보려고 해요 · 하다 → 하려고 해요</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">으려고 하다</span></p>
    <p>먹다 → 먹으려고 해요 · 읽다 → 읽으려고 해요 · 찾다 → 찾으려고 해요</p>
  </div>
</div>

<p><b>ㄹ</b> bilan tugagan oʻzaklar 으 ni olmaydi, ㄹ esa joyida qoladi:
만들다 → <b>만들려고 해요</b>, 살다 → <b>살려고 해요</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 <span class="pe-hl pe-hl--o">한국에</span>
     <span class="pe-hl pe-hl--v">가려고 해요</span>.</p>
  <p class="pe-ex__uz">Men Koreyaga bormoqchiman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">주말에 책을 <span class="pe-hl pe-hl--v">읽으려고 해요</span>.</p>
  <p class="pe-ex__uz">Dam olish kunlari kitob oʻqimoqchiman.</p>
  <p class="pe-ex__why">읽 da 받침 bor → 으려고.</p>
</div>

<h3>2. Notoʻgʻri feʼllar</h3>

<p>(으) unli — demak PK-32 dagi oʻzgarishlar bu yerda ham ishlaydi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Oʻzgarish</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>듣다</td><td class="pk-end">ㄷ → ㄹ</td>
      <td class="pk-res">들으려고 해요</td><td class="pk-uz">tinglamoqchiman</td></tr>
  <tr><td>걷다</td><td class="pk-end">ㄷ → ㄹ</td>
      <td class="pk-res">걸으려고 해요</td><td class="pk-uz">yurmoqchiman</td></tr>
  <tr><td>돕다</td><td class="pk-end">ㅂ → 우</td>
      <td class="pk-res">도우려고 해요</td><td class="pk-uz">yordam bermoqchiman</td></tr>
</table></div>

<h3>3. Faqat harakat feʼllari bilan</h3>

<div class="pe-call pe-rule">
  <p><b>(으)려고 하다 — bu niyat.</b> Niyat qilish uchun harakat kerak. Shuning uchun
  u <b>faqat feʼllar</b> bilan ishlatiladi, sifatlar bilan emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>저는 예쁘려고 해요.</s></p>
  <p class="pe-good">저는 <b>공부하려고 해요</b>.</p>
  <p><small>예쁘다 — sifat. “Chiroyli boʻlishni niyat qilish” degan gap
  koreyschada bunday tuzilmaydi.</small></p>
</div>

<h3>4. (으)려고 하다 va (으)ㄹ 거예요 — farqi</h3>

<p>Ikkalasi ham kelajak haqida, lekin ular bir xil emas. Farqni koʻrish uchun eng
oson yoʻl — <b>qaror qilinganmi yoki yoʻqmi</b> deb soʻrash.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">(으)ㄹ 거예요</p>
    <p><b>Qaror qilingan reja</b> yoki oddiy kelasi zamon.</p>
    <p>내일 부산에 <b>갈 거예요</b>.<br><small>Ertaga Pusanga boraman — chipta olingan,
    ish tayyor.</small></p>
    <p>Boshqa odam haqida ham aytish mumkin:<br>지영 씨는 안 <b>올 거예요</b>.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">(으)려고 하다</p>
    <p><b>Koʻngildagi niyat</b> — hali oʻzgarishi mumkin.</p>
    <p>내일 부산에 <b>가려고 해요</b>.<br><small>Ertaga Pusanga bormoqchiman —
    shunday oʻylab turibman.</small></p>
    <p>Odatda oʻzingiz yoki yaqin biror kishi haqida.</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha koʻprik.</b> (으)ㄹ 거예요 ≈ “<em>boraman</em>”, (으)려고 하다 ≈
  “<em>bormoqchiman</em>”. Oʻzbek tilida ham “-moqchi” aynan shu ishni qiladi: u
  niyatni bildiradi, kafolatni emas. Shuning uchun oʻzbekchada “-moqchi” deyayotgan
  boʻlsangiz, koreyschada deyarli har doim <b>(으)려고 하다</b> boʻladi.</p>
</div>

<h3>5. 려고 했어요 — “…moqchi edim, lekin…”</h3>

<p>하다 ni oʻtgan zamonga qoʻysangiz, juda foydali maʼno chiqadi: niyat bor edi,
lekin amalga oshmadi. Koreyslar buni juda koʻp ishlatadi.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">어제 공부<span class="pe-hl pe-hl--v">하려고 했어요</span>.
     하지만 너무 피곤해서 잤어요.</p>
  <p class="pe-ex__uz">Kecha dars qilmoqchi edim. Lekin juda charchaganim uchun uxlab
  qoldim.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">전화<span class="pe-hl pe-hl--v">하려고 했어요</span>.
     그런데 시간이 없어서 못 했어요.</p>
  <p class="pe-ex__uz">Telefon qilmoqchi edim. Lekin vaqtim boʻlmagani uchun qila
  olmadim.</p>
</div>

<div class="pe-call pe-tip">
  <p>Diqqat: zamon <b>하다</b> ga qoʻyiladi, 려고 ga emas. <s>갔으려고 해요</s> notoʻgʻri —
  toʻgʻrisi <b>가려고 했어요</b>. Bu bilan siz butun kurs boʻyicha takrorlanayotgan
  qoidani yana bir marta koʻryapsiz: <b>zamon oxirida turadi</b>.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham xuddi shunday.</b> Biz “bor<em>moqchi edim</em>” deymiz —
  “-moqchi” niyatni bildiradi, “edi” esa zamonni. Ikkalasi <b>alohida</b> boʻlaklar,
  va zamon oxirida turadi. 가려고 했어요 da ham shunday: 려고 = “-moqchi”,
  했어요 = “edim”. Yaʼni bu shakl siz uchun butunlay yangi emas — oʻzbekcha
  jumlani ikkiga boʻlib qarasangiz, tuzilishi bir xil.</p>
</div>

<h3>6. 하다siz (으)려고 — maqsad bogʻlovchisi</h3>

<p>하다 ni olib tashlasangiz, <b>(으)려고</b> ikki gapni bogʻlaydi va “…<b>maqsadida</b>,
…<b>uchun</b>” degan maʼno beradi.</p>

<div class="pe-formula">
  <span class="pe-formula__label">Maqsad</span>
  <span class="pe-chip pe-chip--s">Maqsad</span>
  <span class="pe-chip pe-chip--v">(으)려고</span>
  <span class="pe-chip pe-chip--o">shu uchun qilinayotgan ish</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">한국에 <span class="pe-hl pe-hl--adv">가려고</span>
     한국어를 배워요.</p>
  <p class="pe-ex__uz">Koreyaga borish uchun koreys tilini oʻrganaman.</p>
  <p class="pe-ex__why">Maqsad — birinchi qismda, unga erishish yoʻli — ikkinchi qismda.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">선물을 <span class="pe-hl pe-hl--adv">사려고</span>
     시장에 갔어요.</p>
  <p class="pe-ex__uz">Sovgʻa sotib olish uchun bozorga bordim.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Soʻz tartibi oʻzbekchadek.</b> “Sovgʻa sotib ol<em>ish uchun</em> bozorga
  bordim” — maqsad oldinda, harakat orqada. 선물을 <b>사려고</b> 시장에 갔어요 —
  aynan shu tartib. Ingliz tilida esa teskari (“I went to the market <em>to buy</em>
  a gift”). Shuning uchun bu qolipni oʻzbekchadan oʻylab tuzing, ingliz tilidan
  emas — koʻchirish deyarli avtomatik boʻladi.</p>
</div>

<p>Bu shaklning ham ikkita sharti bor, va ikkalasi ham tanish:</p>

<div class="pe-call pe-warn">
  <p><b>1. Ega bir xil boʻlishi kerak</b> — maqsadni ham, harakatni ham bir odam
  bajaradi.<br>
  <b>2. Keyingi qismda buyruq boʻlmaydi.</b> <s>한국에 가려고 한국어를 배우세요.</s>
  — bunday deyilmaydi. Bu <b>아/어서</b> (PK-35) dagi taqiqning aynan oʻzi.</p>
</div>

<h3>7. Uchinchi maʼno: “boʻlay deb turibdi”</h3>

<p>Jonsiz narsalar bilan ishlatilganda (으)려고 하다 niyatni emas, <b>yaqin
kelajakni</b> bildiradi — “hozir boʻladi”:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">비가 <span class="pe-hl pe-hl--v">오려고 해요</span>.</p>
  <p class="pe-ex__uz">Yomgʻir yogʻay deb turibdi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">버스가 <span class="pe-hl pe-hl--v">출발하려고 해요</span>.</p>
  <p class="pe-ex__uz">Avtobus joʻnay deb turibdi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>밥을 먹려고 해요.</s></p>
  <p class="pe-good">밥을 <b>먹으려고</b> 해요.</p>
  <p><small>먹 da 받침 bor → 으려고. Bu eng koʻp uchraydigan xato.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>어제 갔으려고 해요.</s></p>
  <p class="pe-good">어제 <b>가려고 했어요</b>.</p>
  <p><small>Zamon 려고 ga emas, 하다 ga qoʻyiladi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>저는 키가 크려고 해요.</s></p>
  <p class="pe-good">저는 <b>운동하려고 해요</b>.</p>
  <p><small>크다 — sifat. (으)려고 하다 faqat harakat feʼllari bilan.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>사진을 찍으려고 카메라를 사세요.</s></p>
  <p class="pe-good">사진을 찍으려고 카메라를 <b>샀어요</b>.</p>
  <p><small>(으)려고 dan keyin buyruq kelmaydi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>음악을 듣으려고 해요.</s></p>
  <p class="pe-good">음악을 <b>들으려고</b> 해요.</p>
  <p><small>듣다 — ㄷ notoʻgʻri feʼli, (으) unli oldida ㄷ → ㄹ.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 내일 친구를
  <span class="pe-blank"></span> (만나다) 해요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>만나려고</b> — 만나 da 받침 yoʻq, shuning uchun 려고. Toʻliq gap:
    내일 친구를 만나려고 해요 (Ertaga doʻstim bilan uchrashmoqchiman).</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 김치를 <span class="pe-blank"></span>
  (만들다) 해요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>만들려고</b> — ㄹ oʻzak: 으 qoʻshilmaydi, ㄹ ham tushmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Qaysi biri toʻgʻriroq va nega?
  “Ertaga imtihonim bor, shuning uchun ertaga qatʼiy dars qilaman.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>공부할 거예요</b> — qaror qilingan, aniq reja. 공부하려고 해요 desangiz,
    “dars qilmoqchiman” degan yumshoqroq, hali qatʼiy boʻlmagan maʼno chiqadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Xatoni toping:
  <s>선물을 사려고 시장에 가세요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>(으)려고 dan keyin buyruq kelmaydi. Toʻgʻrisi — <b>선물을 사려고 시장에
    갔어요</b> (yoki 가요). Buyruq aytmoqchi boʻlsangiz, gapni boshqacha tuzish kerak.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Koreyschaga oʻgiring: “Kecha kitob oʻqimoqchi
  edim, lekin vaqtim boʻlmadi.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>어제 책을 읽으려고 했어요. 하지만 시간이 없었어요.</b> Zamon 하다 da:
    했어요. 읽 da 받침 bor → 으려고.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Bu gap nima degani?
  버스가 출발하려고 해요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>Avtobus joʻnay deb turibdi.</b> Avtobusning “niyati” yoʻq — jonsiz narsalar
    bilan (으)려고 하다 yaqin kelajakni bildiradi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)려고 하다</b> — …moqchi boʻlmoq</li>
  <li><b>(으)려고</b> — …maqsadida, …uchun</li>
  <li><b>주말</b> — dam olish kunlari</li>
  <li><b>선물</b> — sovgʻa</li>
  <li><b>시장</b> — bozor</li>
  <li><b>찾다</b> — qidirmoq, topmoq</li>
  <li><b>출발하다</b> — joʻnamoq</li>
  <li><b>피곤하다</b> — charchagan</li>
  <li><b>그런데</b> — lekin, ammo (suhbatda)</li>
  <li><b>사진을 찍다</b> — surat olmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>(으)려고 하다</b> = “…moqchiman” — koʻngildagi niyat.</li>
    <li>받침 yoʻq → 려고 · 받침 bor → 으려고 · ㄹ oʻzak → 려고.</li>
    <li>(으) unli, shuning uchun notoʻgʻri feʼllar ishlaydi: 듣다 → 들으려고.</li>
    <li>Faqat <b>harakat feʼllari</b> bilan — sifatlar bilan emas.</li>
    <li>(으)ㄹ 거예요 — qaror qilingan reja · (으)려고 하다 — hali niyat.</li>
    <li>Zamon <b>하다</b> ga qoʻyiladi: 가려고 했어요 = “bormoqchi edim, lekin…”.</li>
    <li>하다siz <b>(으)려고</b> — maqsad bogʻlovchisi. Ega bir xil, keyin buyruq yoʻq.</li>
    <li>Jonsiz narsa bilan — “boʻlay deb turibdi”: 비가 오려고 해요.</li>
  </ul>
</div>
""",
    },
]
