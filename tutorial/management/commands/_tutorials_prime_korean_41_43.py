# -*- coding: utf-8 -*-
"""Prime Korean — Block D, darslar 41–43.

41. 아/어 보다 — sinab koʻrish va tajriba
42. 고 있다 va 아/어 있다 — davom etayotgan ish va holat
43. Aniqlovchi 1: 동사 + 는 (hozirgi zamon)

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

Oʻqish matnlari: corner/management/commands/_stories_prime_korean_41_43.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_41_43.py --author=prime
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
        "title": "PK-41: 아/어 보다 — sinab koʻrish va tajriba",
        "category": "korean",
        "order": 41,
        "summary": (
            "“Yeb koʻring” — oʻzbekcha bilan soʻzma-soʻz bir xil qolip. Bir ishni "
            "sinab koʻrish, tavsiya berish va “…qilib koʻrganman” deyish."
        ),
        "stories": ["한국 음식을 먹어 보세요"],
        "content": """
<h2>PK-41: 아/어 보다 — sinab koʻrish va tajriba</h2>

<p>Doʻstingiz sizga notanish taomni uzatib turibdi va: “Bir <b>yeb koʻring</b>!” —
deydi. Endi diqqat qiling: oʻzbek tilida biz “yeb <b>koʻrmoq</b>” deymiz, garchi
koʻz bilan hech qanday aloqasi boʻlmasa ham. Koreys tili ham aynan shunday qiladi —
<b>보다</b> “koʻrmoq” degani, va u ham “sinab koʻrmoq” maʼnosida ishlatiladi.
Bu darsdagi qolip — <b>아/어 보다</b> — oʻzbekchadagi qolipning soʻzma-soʻz aynan
oʻzi. Kursdagi eng oson darslardan biri boʻladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>아/어 보다</b> ni yasashni oʻrganasiz</li>
    <li><b>아/어 보세요</b> bilan tavsiya berasiz — eng koʻp ishlatiladigan shakl</li>
    <li><b>아/어 봤어요</b> bilan tajriba haqida gapirasiz</li>
    <li>Uni <b>고 싶다</b> bilan birga ishlatishni koʻrasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">Feʼl oʻzagi</span>
  <span class="pe-chip pe-chip--v">아/어</span>
  <span class="pe-chip pe-chip--v">보다</span>
  <span class="pe-chip pe-chip--adv">= …ib koʻrmoq</span>
</div>

<h3>1. Yasalishi — 아/어요 shaklidan</h3>

<p>Yangi qoida yodlash shart emas. <b>아/어요</b> shaklini oling (PK-18), <b>요</b> ni
olib tashlang, oʻrniga <b>보다</b> qoʻying. Tamom.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>아/어요</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>가다</td><td class="pk-stem">가요</td>
      <td class="pk-res">가 보다</td><td class="pk-uz">borib koʻrmoq</td></tr>
  <tr><td>먹다</td><td class="pk-stem">먹어요</td>
      <td class="pk-res">먹어 보다</td><td class="pk-uz">yeb koʻrmoq</td></tr>
  <tr><td>하다</td><td class="pk-stem">해요</td>
      <td class="pk-res">해 보다</td><td class="pk-uz">qilib koʻrmoq</td></tr>
  <tr><td>마시다</td><td class="pk-stem">마셔요</td>
      <td class="pk-res">마셔 보다</td><td class="pk-uz">ichib koʻrmoq</td></tr>
  <tr><td>듣다</td><td class="pk-stem">들어요</td>
      <td class="pk-res">들어 보다</td><td class="pk-uz">tinglab koʻrmoq</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p>Oxirgi qatorga eʼtibor bering: 듣다 → <b>들어</b> 보다. 아/어 unli bilan
  boshlanadi, shuning uchun PK-32 dagi notoʻgʻri tuslanish bu yerda ishlaydi.
  Xuddi shunday: 돕다 → <b>도와</b> 보다, 쓰다 → <b>써</b> 보다.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu darsning eng katta sovgʻasi.</b> 보다 = “koʻrmoq”. 먹어 보다 = “yeb
  <b>koʻrmoq</b>”. 가 보다 = “borib <b>koʻrmoq</b>”. 해 보다 = “qilib
  <b>koʻrmoq</b>”. Yaʼni oʻzbek tili va koreys tili bir xil obrazdan foydalangan:
  “sinab koʻrmoq” degan maʼnoni ikkalasi ham “koʻrish” feʼli bilan yasagan.
  Ingliz tilida bunday emas (“try to eat” — u yerda “see” yoʻq). Shuning uchun bu
  qolipni yodlamang — oʻzbekcha “-ib koʻrmoq” deb oʻylang, koreyschasi oʻzi chiqadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 김치를 <span class="pe-hl pe-hl--v">먹어 봤어요</span>.</p>
  <p class="pe-ex__uz">Men kimchini yeb koʻrganman.</p>
</div>

<h3>2. 아/어 보세요 — eng koʻp ishlatiladigan shakl</h3>

<p>Koreyaga borsangiz, bu iborani kuniga oʻn marta eshitasiz. Doʻkonda, oshxonada,
darsda — kimdir sizga biror narsani tavsiya qilmoqchi boʻlsa, aynan shuni aytadi.</p>

<div class="pe-formula">
  <span class="pe-formula__label">Tavsiya</span>
  <span class="pe-chip pe-chip--opt">한번</span>
  <span class="pe-chip pe-chip--s">Feʼl oʻzagi</span>
  <span class="pe-chip pe-chip--v">아/어 보세요</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">이 김밥을 <span class="pe-hl pe-hl--v">먹어 보세요</span>.
     정말 맛있어요.</p>
  <p class="pe-ex__uz">Bu kimbapni yeb koʻring. Rostdan ham mazali.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--adv">한번</span> 한국 노래를
     <span class="pe-hl pe-hl--v">들어 보세요</span>.</p>
  <p class="pe-ex__uz">Bir marta koreys qoʻshiqlarini tinglab koʻring.</p>
  <p class="pe-ex__why">한번 — “bir marta”. 아/어 보세요 bilan juda koʻp yuradi.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Nega shunchaki 먹으세요 emas?</b> 먹으세요 — “yeng” degan koʻrsatma.
  먹어 보세요 esa yumshoqroq: “bir sinab koʻring, yoqmasa qoʻying”. Shuning uchun
  notanish narsani tavsiya qilganda koreyslar deyarli har doim
  <b>아/어 보세요</b> ni tanlaydi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>한번 ham oʻzbekchadan tanish.</b> 한번 = “bir marta”, lekin bu yerda u
  sanoq emas — yumshatuvchi soʻz. Oʻzbekchada ham xuddi shunday qilamiz:
  “<em>bir</em> yeb koʻring”, “<em>bir</em> aytib koʻring”. Bu “bir” hech qanday
  sonni bildirmaydi, u shunchaki taklifni muloyim qiladi. 한번 먹어 보세요 —
  soʻzma-soʻz “bir yeb koʻring”. Ikki tilda bir xil odat.</p>
</div>

<h3>3. 아/어 봤어요 — tajriba</h3>

<p>Oʻtgan zamonda bu qolip “…qilib koʻrganman”, yaʼni <b>hayotdagi tajriba</b>ni
bildiradi. Tanishuvda eng koʻp beriladigan savollardan biri shu:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">한국에 <span class="pe-hl pe-hl--v">가 봤어요</span>?</p>
  <p class="pe-ex__uz">Koreyaga borib koʻrganmisiz?</p>
</div>

<p>Javoblari:</p>

<ul>
  <li>네, <b>가 봤어요</b>. — Ha, borganman.</li>
  <li>아니요, <b>안 가 봤어요</b>. — Yoʻq, hech borgan emasman.</li>
  <li>아니요, <b>못 가 봤어요</b>. — Yoʻq, bora olmaganman (xohlardim, lekin
    imkon boʻlmadi).</li>
</ul>

<div class="pe-call pe-uz">
  <p><b>안 va 못 orasidagi farq bu yerda ham ishlaydi</b> (PK-21, PK-22).
  안 가 봤어요 — shunchaki bormaganman. 못 가 봤어요 — bora olmaganman, yaʼni
  ichida biroz afsus bor. Oʻzbekchada ham xuddi shu farq bor: “borganim yoʻq”
  va “bora olmadim” bir xil gap emas.</p>
</div>

<h3>4. 아/어 보고 싶어요 — “sinab koʻrgim keladi”</h3>

<p>PK-28 dagi <b>고 싶다</b> bilan birlashtirsangiz, juda tabiiy va koʻp
ishlatiladigan gap chiqadi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">한국 음식을 <span class="pe-hl pe-hl--v">먹어 보고
     싶어요</span>.</p>
  <p class="pe-ex__uz">Koreys taomlarini yeb koʻrgim keladi.</p>
  <p class="pe-ex__why">먹어 보다 + 고 싶다 → 먹어 보고 싶어요.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">제주도에 <span class="pe-hl pe-hl--v">가 보고 싶어요</span>.</p>
  <p class="pe-ex__uz">Chechu oroliga borib koʻrgim keladi.</p>
</div>

<h3>5. Ikkita cheklov</h3>

<div class="pe-call pe-warn">
  <p><b>1. Sifatlar bilan ishlatilmaydi.</b> Sinab koʻrish uchun harakat kerak.
  <s>예뻐 보다</s>, <s>더워 보다</s> — bunday deyilmaydi.<br>
  <b>2. 보다 ning oʻzi bilan takrorlanmaydi.</b> “Koʻrib koʻring” demoqchi
  boʻlsangiz, <s>봐 보세요</s> emas, shunchaki <b>보세요</b> yoki
  <b>한번 보세요</b> deyiladi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>김치를 먹고 보세요.</s></p>
  <p class="pe-good">김치를 <b>먹어 보세요</b>.</p>
  <p><small>Qolip 고 emas, <b>아/어</b> bilan yasaladi. 먹고 보다 butunlay boshqa
  narsa.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>음악을 듣어 보세요.</s></p>
  <p class="pe-good">음악을 <b>들어 보세요</b>.</p>
  <p><small>듣다 — ㄷ notoʻgʻri feʼli. 아/어 unli, shuning uchun ㄷ → ㄹ.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>이 옷은 예뻐 보세요.</s></p>
  <p class="pe-good">이 옷을 <b>입어 보세요</b>.</p>
  <p><small>예쁘다 — sifat, sinab koʻrib boʻlmaydi. Sinaladigan narsa —
  kiyib koʻrish, yaʼni 입어 보다.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>한국에 갔어 봤어요.</s></p>
  <p class="pe-good">한국에 <b>가 봤어요</b>.</p>
  <p><small>Zamon faqat <b>보다</b> ga qoʻyiladi: 가 <b>봤</b>어요. Birinchi
  feʼlga qoʻyilmaydi.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 이 차를 <span class="pe-blank"></span>
  (마시다) 보세요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>마셔</b> — 마시다 → 마셔요 → <b>마셔 보세요</b> (“bu choyni ichib
    koʻring”).</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 한국 노래를
  <span class="pe-blank"></span> (듣다) 봤어요?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>들어</b> — 듣다 → 들어요 → <b>들어 봤어요</b>? (“koreys qoʻshiqlarini
    tinglab koʻrganmisiz?”)</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Farqini ayting: 먹으세요 va 먹어 보세요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>먹으세요</b> — “yeng” (koʻrsatma). <b>먹어 보세요</b> — “bir yeb koʻring”
    (yumshoq tavsiya). Notanish taomni taklif qilayotganda ikkinchisi tabiiyroq.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Xatoni toping:
  <s>저는 한국에 갔어 봤어요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Zamon ikki marta qoʻyilgan. Toʻgʻrisi — <b>저는 한국에 가 봤어요.</b>
    Oʻtgan zamon faqat 보다 da: 봤어요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Koreyschaga oʻgiring: “Koreys taomlarini
  yeb koʻrgim keladi.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>한국 음식을 먹어 보고 싶어요.</b> 먹어 보다 (sinab koʻrmoq) +
    고 싶다 (xohlamoq) birga kelgan.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Bu ikki javob orasida qanday farq bor?
  “안 가 봤어요” va “못 가 봤어요”.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>안 가 봤어요</b> — bormaganman (shunchaki). <b>못 가 봤어요</b> —
    bora olmaganman (imkon boʻlmadi). PK-21 va PK-22 dagi 안/못 farqi bu yerda
    ham xuddi shunday ishlaydi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>아/어 보다</b> — …ib koʻrmoq, sinab koʻrmoq</li>
  <li><b>아/어 보세요</b> — …ib koʻring (tavsiya)</li>
  <li><b>아/어 봤어요</b> — …ib koʻrganman (tajriba)</li>
  <li><b>한번</b> — bir marta</li>
  <li><b>김밥</b> — kimbap (koreyscha taom)</li>
  <li><b>입다</b> — kiymoq</li>
  <li><b>쓰다</b> — yozmoq; ishlatmoq</li>
  <li><b>제주도</b> — Chechu oroli</li>
  <li><b>음식</b> — taom, ovqat</li>
  <li><b>노래</b> — qoʻshiq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>아/어 보다</b> = “…ib koʻrmoq” — oʻzbekchadagi qolipning aynan oʻzi.</li>
    <li>Yasalishi: 아/어요 shakli → 요 oʻrniga 보다.</li>
    <li>아/어 unli, shuning uchun notoʻgʻri feʼllar ishlaydi: 듣다 → 들어 보다.</li>
    <li><b>아/어 보세요</b> — yumshoq tavsiya, 한번 bilan koʻp yuradi.</li>
    <li><b>아/어 봤어요</b> — hayotdagi tajriba. Inkori: 안 / 못 가 봤어요.</li>
    <li>고 싶다 bilan birlashadi: 먹어 보고 싶어요.</li>
    <li>Sifatlar bilan ishlatilmaydi; 보다 ning oʻzi takrorlanmaydi.</li>
    <li>Zamon faqat <b>보다</b> da turadi: 가 봤어요.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-42: 고 있다 va 아/어 있다 — davom etayotgan ish va holat",
        "category": "korean",
        "order": 42,
        "summary": (
            "“Ovqat yeyapman” va “oʻtiribman” — ikki xil davomiylik. 고 있다 harakat "
            "davom etayotganini, 아/어 있다 esa tugagan ishning natijasini koʻrsatadi."
        ),
        "stories": ["지금 뭐 하고 있어요?"],
        "content": """
<h2>PK-42: 고 있다 va 아/어 있다 — davom etayotgan ish va holat</h2>

<p>Doʻstingiz telefon qildi: “Hozir nima qilyapsan?” Siz javob berasiz: “Ovqat
<b>yeyapman</b>.” Endi boshqa vaziyat: siz kutubxonaga kirdingiz va doʻstingiz
u yerda <b>oʻtiribdi</b>. “Yeyapman” va “oʻtiribdi” — ikkalasi ham hozirgi paytga
tegishli, lekin ular bir xil emas. Birinchisi — <em>davom etayotgan harakat</em>,
ikkinchisi — <em>tugagan harakatdan qolgan holat</em>. Koreys tili bu ikkisini
ikki xil qolip bilan ajratadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>고 있다</b> bilan davom etayotgan ishni aytasiz</li>
    <li><b>아/어 있다</b> bilan holatni aytasiz</li>
    <li>Ikkalasining farqini bitta savol bilan hal qilasiz</li>
    <li><b>아/어 있다</b> qaysi feʼllar bilan kelishini bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Harakat</span>
  <span class="pe-chip pe-chip--s">Feʼl oʻzagi</span>
  <span class="pe-chip pe-chip--v">고 있다</span>
  <span class="pe-chip pe-chip--adv">= …yapman</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Holat</span>
  <span class="pe-chip pe-chip--s">Feʼl oʻzagi</span>
  <span class="pe-chip pe-chip--v">아/어 있다</span>
  <span class="pe-chip pe-chip--adv">= …ib turibdi</span>
</div>

<h3>1. 고 있다 — harakat davom etyapti</h3>

<p>Yasalishi eng osoni: oʻzakka shundoq <b>고 있다</b> qoʻshiladi. 받침 ayrisi yoʻq,
notoʻgʻri feʼllar ham oʻzgarmaydi — chunki <b>고</b> undosh bilan boshlanadi
(PK-32 ning qoidasi).</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Oʻzak</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>먹다</td><td class="pk-stem">먹</td>
      <td class="pk-res">먹고 있어요</td><td class="pk-uz">yeyapman</td></tr>
  <tr><td>공부하다</td><td class="pk-stem">공부하</td>
      <td class="pk-res">공부하고 있어요</td><td class="pk-uz">dars qilyapman</td></tr>
  <tr><td>듣다</td><td class="pk-stem">듣</td>
      <td class="pk-res">듣고 있어요</td><td class="pk-uz">tinglayapman</td></tr>
  <tr><td>돕다</td><td class="pk-stem">돕</td>
      <td class="pk-res">돕고 있어요</td><td class="pk-uz">yordam beryapman</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p>Uchinchi va toʻrtinchi qatorlarga qarang: <b>듣고</b>, <b>돕고</b> — hech nima
  oʻzgarmadi. Oʻtgan darsda <b>들어 보다</b>, <b>도와 보다</b> edi. Farq faqat bitta
  narsada: 아/어 unli, 고 esa undosh. Shu bitta qoida butun kursni ushlab
  turadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 지금 밥을 <span class="pe-hl pe-hl--v">먹고
     있어요</span>.</p>
  <p class="pe-ex__uz">Men hozir ovqat yeyapman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">어제 저녁에 뭐 <span class="pe-hl pe-hl--v">하고
     있었어요</span>?</p>
  <p class="pe-ex__uz">Kecha kechqurun nima qilib turgan edingiz?</p>
  <p class="pe-ex__why">Oʻtgan zamon 있다 ga qoʻyiladi: 있었어요.</p>
</div>

<h3>2. 아/어 있다 — ish tugadi, holat qoldi</h3>

<p>Bu qolip <b>아/어 보다</b> dagidek yasaladi: 아/어요 shaklidan 요 ni olib,
oʻrniga <b>있다</b> qoʻyiladi.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>아/어요</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>앉다</td><td class="pk-stem">앉아요</td>
      <td class="pk-res">앉아 있어요</td><td class="pk-uz">oʻtiribdi</td></tr>
  <tr><td>서다</td><td class="pk-stem">서요</td>
      <td class="pk-res">서 있어요</td><td class="pk-uz">turibdi</td></tr>
  <tr><td>눕다</td><td class="pk-stem">누워요</td>
      <td class="pk-res">누워 있어요</td><td class="pk-uz">yotibdi</td></tr>
  <tr><td>오다</td><td class="pk-stem">와요</td>
      <td class="pk-res">와 있어요</td><td class="pk-uz">kelib boʻlgan, shu yerda</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">지영 씨는 의자에 <span class="pe-hl pe-hl--v">앉아
     있어요</span>.</p>
  <p class="pe-ex__uz">Chiyong stulda oʻtiribdi.</p>
  <p class="pe-ex__why">Oʻtirish harakati tugagan; qolgani — oʻtirgan holat.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">아프소나 씨가 벌써 학교에 <span class="pe-hl pe-hl--v">와
     있어요</span>.</p>
  <p class="pe-ex__uz">Afsona allaqachon maktabda (kelib boʻlgan).</p>
</div>

<h3>3. Farqni bitta savol hal qiladi</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">앉<b>고</b> 있어요</p>
    <p>Harakat <b>hozir sodir boʻlyapti</b>.</p>
    <p>Odam stulga <em>oʻtirayotgan</em> paytda — tanasi hali harakatda.</p>
    <p><small>Oʻzbekcha: “oʻtir<b>yapti</b>”.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">앉<b>아</b> 있어요</p>
    <p>Harakat <b>tugagan</b>, natijasi turibdi.</p>
    <p>Odam allaqachon stulda — oʻtirgan holatda.</p>
    <p><small>Oʻzbekcha: “oʻtir<b>ibdi</b>”.</small></p>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida bu farq bor — faqat boshqa qoʻshimchada.</b>
  “Oʻtir<em>yapti</em>” (harakat ketyapti) va “oʻtir<em>ibdi</em>” (allaqachon
  oʻtirgan) — bu ikkalasi bir xil emas, va siz buni oʻylamasdan ajratasiz.
  Koreyschada esa: 앉<b>고</b> 있어요 va 앉<b>아</b> 있어요. Yaʼni yangi tushuncha
  emas, yangi kiyim. Ingliz tilida ikkalasi ham “is sitting” — shuning uchun bu
  qoida ingliz tilidan oʻrganayotganlarga qiyin, sizga esa oson.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Tekshirish savoli:</b> <em>Odam hali harakat qilyaptimi, yoki harakat
  tugab, natijasi turibdimi?</em> Harakat ketyapti → <b>고 있다</b>.
  Natija turibdi → <b>아/어 있다</b>.</p>
</div>

<h3>4. 아/어 있다 hamma feʼl bilan kelmaydi</h3>

<p>Bu — darsning eng muhim cheklovi. <b>아/어 있다</b> faqat toʻldiruvchi
talab qilmaydigan feʼllar bilan ishlatiladi: 앉다, 서다, 눕다, 오다, 가다,
남다 kabi.</p>

<div class="pe-fix">
  <p class="pe-bad"><s>밥을 먹어 있어요.</s></p>
  <p class="pe-good">밥을 <b>먹고 있어요</b>.</p>
  <p><small>먹다 toʻldiruvchi oladi (밥<b>을</b>), shuning uchun 아/어 있다 bilan
  kelmaydi.</small></p>
</div>

<p>Amalda buni yodlashning oson yoʻli bor: <b>아/어 있다</b> bilan kelib
qoladigan feʼllar juda kam, va ular deyarli hammasi <b>joy va holat</b>
haqida. Quyidagi beshtasini yod olsangiz, kundalik nutqning katta qismini
qoplaysiz:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>앉아 있다</p>
    <p>oʻtirgan holatda</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>서 있다</p>
    <p>tik turgan holatda</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>누워 있다</p>
    <p>yotgan holatda</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">4</span>와 있다</p>
    <p>kelib boʻlgan, shu yerda</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">5</span>남아 있다</p>
    <p>qolgan, ortib turgan</p></div>
</div>

<div class="pe-call pe-tip">
  <p>Ikkinchi bir guruh ham bor — 문이 <b>열려 있어요</b> (“eshik ochiq”),
  불이 <b>켜져 있어요</b> (“chiroq yoniq”). Bular majhul nisbatdan yasalgan va
  siz ularni <b>PK-56</b> da toʻliq oʻrganasiz. Hozircha shu ikkitasini tayyor
  ibora sifatida yod olsangiz kifoya.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Nega bu roʻyxat shunchalik kichkina?</b> Chunki oʻzbekchada ham shunday.
  “Oʻtirib turibdi”, “turib turibdi”, “yotib turibdi” — bemalol aytamiz. Lekin
  “non yeb turibdi” desangiz, bu <em>holat</em> emas, <em>harakat</em> boʻlib
  eshitiladi. Yaʼni oʻzbek tilida ham bu qurilma faqat <b>gavda holati</b> va
  <b>joyda boʻlish</b> feʼllari bilan ishlaydi. Koreys tili shu chegarani qatʼiy
  qoidaga aylantirgan, xolos — yodlash uchun oʻzbekcha tuygʻungizga ishoning.</p>
</div>

<h3>5. 입고 있다 — ikki maʼnoli holat</h3>

<p>Kiyim feʼllari koreys tilida alohida turadi. <b>입고 있어요</b> ikki xil
tushunilishi mumkin:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">아프소나 씨는 티셔츠를
     <span class="pe-hl pe-hl--v">입고 있어요</span>.</p>
  <p class="pe-ex__uz">Afsona oq futbolka kiygan. <em>(yoki:</em> kiyayapti.<em>)</em></p>
  <p class="pe-ex__why">Vaziyat qaysi maʼno ekanini koʻrsatadi. Odamning
  koʻrinishini taʼriflayotgan boʻlsangiz — “kiygan”.</p>
</div>

<p>Xuddi shunday: 신발을 <b>신고 있어요</b> (oyoq kiyim kiygan),
모자를 <b>쓰고 있어요</b> (shapka kiygan).</p>

<div class="pe-call pe-uz">
  <p><b>Kiyim feʼllarida oʻzbekcha ham ikki maʼnoli.</b> “Afsona koʻylak
  <em>kiygan</em>” va “Afsona koʻylak <em>kiyyapti</em>” — biz bu ikkisini
  ajratamiz, lekin “kiygan” soʻzining oʻzi ham holat, ham tugagan ish haqida
  gapiradi. Koreyschada 입고 있어요 aynan shu ikki maʼnoni bitta shaklda
  saqlaydi. Odamning koʻrinishini taʼriflayotgan boʻlsangiz — “kiygan”,
  kiyinish jarayonini aytayotgan boʻlsangiz — “kiyyapti”. Vaziyat hal qiladi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>음악을 들고 있어요 (“musiqa tinglayapman” maʼnosida).</s></p>
  <p class="pe-good">음악을 <b>듣고 있어요</b>.</p>
  <p><small>고 undosh — oʻzak oʻzgarmaydi. 들고 있다 boshqa gap: “qoʻlida
  ushlab turibdi”.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>책을 읽어 있어요.</s></p>
  <p class="pe-good">책을 <b>읽고 있어요</b>.</p>
  <p><small>읽다 toʻldiruvchi oladi → 아/어 있다 bilan kelmaydi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>지영 씨는 의자에 앉고 있어요 (“stulda oʻtiribdi”
  maʼnosida).</s></p>
  <p class="pe-good">지영 씨는 의자에 <b>앉아 있어요</b>.</p>
  <p><small>앉고 있어요 — hozir oʻtirayotgan payt. Holatni aytmoqchi boʻlsangiz —
  앉아 있어요.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>어제 공부했고 있었어요.</s></p>
  <p class="pe-good">어제 <b>공부하고 있었어요</b>.</p>
  <p><small>Zamon faqat <b>있다</b> ga qoʻyiladi: 있<b>었</b>어요.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 저는 지금 한국어를
  <span class="pe-blank"></span> (공부하다).</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>공부하고 있어요</b> — davom etayotgan harakat.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 수진 씨가 문 앞에
  <span class="pe-blank"></span> (서다).</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>서 있어요</b> — “eshik oldida turibdi”. Bu harakat emas, holat.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Qaysi biri toʻgʻri va nega?
  (a) 밥을 먹어 있어요 &nbsp; (b) 밥을 먹고 있어요</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>(b)</b> — 먹다 toʻldiruvchi oladi (밥을), shuning uchun faqat
    <b>고 있다</b> bilan keladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Farqini ayting: 앉고 있어요 va 앉아 있어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>앉고 있어요</b> — hozir oʻtirayotgan payt (“oʻtiryapti”).
    <b>앉아 있어요</b> — allaqachon oʻtirgan (“oʻtiribdi”). Oʻzbekchadagi
    “-yapti / -ibdi” farqining aynan oʻzi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Koreyschaga oʻgiring: “Kecha kechqurun
  televizor koʻrib turgan edim.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>어제 저녁에 텔레비전을 보고 있었어요.</b> Zamon 있다 ga qoʻyiladi:
    있었어요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Bu gap nima degani?
  베크조드 씨가 벌써 교실에 와 있어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>Bekzod allaqachon sinfda (kelib boʻlgan).</b> 오다 harakati tugagan,
    natijasi — u shu yerda. 오고 있어요 desangiz, “kelayapti, hali yoʻlda”
    degan boshqa maʼno chiqadi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>고 있다</b> — …yapman (davom etayotgan harakat)</li>
  <li><b>아/어 있다</b> — …ib turibdi (tugagan ishning holati)</li>
  <li><b>앉다</b> — oʻtirmoq</li>
  <li><b>서다</b> — turmoq, tik turmoq</li>
  <li><b>눕다</b> — yotmoq</li>
  <li><b>남다</b> — qolmoq, ortib qolmoq</li>
  <li><b>의자</b> — stul</li>
  <li><b>벌써</b> — allaqachon</li>
  <li><b>입다 / 신다 / 쓰다</b> — kiymoq (ust / oyoq / bosh)</li>
  <li><b>티셔츠</b> — futbolka</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>고 있다</b> — harakat hozir davom etyapti. Oʻzak oʻzgarmaydi
      (고 undosh): 듣고 있어요.</li>
    <li><b>아/어 있다</b> — harakat tugadi, natijasi turibdi. 아/어요 shaklidan
      yasaladi.</li>
    <li>Tekshirish savoli: harakat ketyaptimi yoki natija turibdimi?</li>
    <li>Oʻzbekcha juftligi: “oʻtiryapti” (고 있다) va “oʻtiribdi” (아/어 있다).</li>
    <li><b>아/어 있다</b> toʻldiruvchi oladigan feʼllar bilan kelmaydi:
      <s>밥을 먹어 있어요</s>.</li>
    <li>Yod olinadigan beshtalik: 앉아·서·누워·와·남아 있다.</li>
    <li>입고/신고/쓰고 있다 — vaziyatga qarab “kiygan” yoki “kiyayapti”.</li>
    <li>Zamon faqat <b>있다</b> da: 하고 있었어요.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-43: Aniqlovchi 1: 동사 + 는 (hozirgi zamon)",
        "category": "korean",
        "order": 43,
        "summary": (
            "“Kitob oʻqiydigan bola” — butun gapni otning oldiga qoʻyish. 동사 + 는 "
            "aniqlovchisi, ㄹ oʻzaklar va 있는/없는."
        ),
        "stories": ["제가 자주 가는 카페"],
        "content": """
<h2>PK-43: Aniqlovchi 1: 동사 + 는 (hozirgi zamon)</h2>

<p>“Kitob oʻqiydigan bola.” Bu oddiy oʻzbekcha ibora ichida katta bir ish bor:
butun bir gap (“bola kitob oʻqiydi”) siqilib, <b>otni aniqlovchi</b>ga aylandi
va otning oldiga oʻtdi. Koreys tili ham aynan shunday qiladi — va aynan shu
tartibda. Bu qolipning nomi — <b>aniqlovchi (관형사형)</b>, va bugun uning
birinchi shakli bilan tanishasiz: <b>동사 + 는</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Feʼlni <b>는</b> bilan aniqlovchiga aylantirasiz</li>
    <li>Butun bir gapni otning oldiga qoʻyishni oʻrganasiz</li>
    <li>ㄹ oʻzaklar bilan nima boʻlishini koʻrasiz</li>
    <li>Nihoyat <b>재미있는</b>, <b>맛있는</b> deb ayta olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">Feʼl oʻzagi</span>
  <span class="pe-chip pe-chip--v">는</span>
  <span class="pe-chip pe-chip--o">Ot</span>
</div>

<h3>1. Yasalishi — yana ayri yoʻq</h3>

<p><b>는</b> undosh bilan boshlanadi, demak 받침 ayrisi ham, notoʻgʻri feʼl
oʻzgarishi ham yoʻq. Oʻzakka shundoq qoʻshiladi.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Oʻzak</th><th>Aniqlovchi</th><th>Ot bilan</th><th>Maʼnosi</th></tr>
  <tr><td>먹다</td><td class="pk-stem">먹</td><td class="pk-end">먹는</td>
      <td class="pk-res">먹는 사람</td><td class="pk-uz">yeydigan odam</td></tr>
  <tr><td>가다</td><td class="pk-stem">가</td><td class="pk-end">가는</td>
      <td class="pk-res">가는 버스</td><td class="pk-uz">boradigan avtobus</td></tr>
  <tr><td>읽다</td><td class="pk-stem">읽</td><td class="pk-end">읽는</td>
      <td class="pk-res">읽는 책</td><td class="pk-uz">oʻqiydigan kitob</td></tr>
  <tr><td>듣다</td><td class="pk-stem">듣</td><td class="pk-end">듣는</td>
      <td class="pk-res">듣는 음악</td><td class="pk-uz">tinglaydigan musiqa</td></tr>
  <tr><td>공부하다</td><td class="pk-stem">공부하</td><td class="pk-end">공부하는</td>
      <td class="pk-res">공부하는 학생</td><td class="pk-uz">oʻqiydigan talaba</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p>Toʻrtinchi qatorda yana <b>듣는</b> — oʻzgarishsiz. Bu darsgacha siz buni
  uch marta koʻrdingiz: 듣기 전에 (PK-38), 듣고 있어요 (PK-42), 듣는 음악 (bugun).
  Undosh bilan boshlanadigan har qanday qoʻshimcha oldida notoʻgʻri feʼl
  tinch turadi.</p>
</div>

<h3>2. ㄹ oʻzaklar — ㄹ tushadi</h3>

<p>Bitta istisno bor, va u ham tanish: <b>ㄹ</b> bilan tugagan oʻzak
<b>ㄴ</b> tovushi oldida ㄹ ni yoʻqotadi. PK-38 dagi 만들다 → 만든 후에 bilan
bir xil qoida.</p>

<ul>
  <li>살다 → <b>사는</b> 사람 — yashaydigan odam</li>
  <li>만들다 → <b>만드는</b> 음식 — tayyorlanadigan taom</li>
  <li>알다 → <b>아는</b> 사람 — tanish odam</li>
  <li>놀다 → <b>노는</b> 아이 — oʻynayotgan bola</li>
</ul>

<h3>3. 있다 va 없다 → 있는 / 없는</h3>

<p>Va mana, uzoq kutilgan lahza. Shu paytgacha siz “qiziqarli kitob” deb ayta
olmasdingiz — endi aytasiz:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h">재미<b>있는</b> 책</p>
    <p>qiziqarli kitob</p></div>
  <div class="pe-card"><p class="pe-card__h">맛<b>있는</b> 음식</p>
    <p>mazali taom</p></div>
  <div class="pe-card"><p class="pe-card__h">재미<b>없는</b> 영화</p>
    <p>qiziq boʻlmagan kino</p></div>
  <div class="pe-card"><p class="pe-card__h">맛<b>없는</b> 커피</p>
    <p>bemaza qahva</p></div>
</div>

<div class="pe-call pe-rule">
  <p><b>Nega 재미있다 sifat emas?</b> Chunki uning ichida <b>있다</b> bor, va
  있다 — feʼl. Shuning uchun 재미있다, 맛있다, 멋있다 kabi soʻzlar sifatlar
  qatorida emas, feʼllar qatorida turadi va <b>는</b> ni oladi. Haqiqiy
  sifatlar (예쁘다, 크다, 좋다) boshqa shakl oladi — uni <b>PK-45</b> da
  oʻrganasiz.</p>
</div>

<h3>4. Butun gap otning oldiga oʻtadi</h3>

<p>Endi eng qiziq qismi. Aniqlovchiga faqat feʼl emas, <b>butun gap</b>
aylanishi mumkin. Toʻldiruvchi, joy, payt — hammasi ichida qoladi va oʻz
tartibida turadi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--o">한국어를</span>
     <span class="pe-hl pe-hl--v">공부하는</span>
     <span class="pe-hl pe-hl--s">학생</span></p>
  <p class="pe-ex__uz">koreys tilini oʻrganadigan talaba</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--adv">매일</span>
     <span class="pe-hl pe-hl--o">신문을</span>
     <span class="pe-hl pe-hl--v">읽는</span>
     <span class="pe-hl pe-hl--s">사람</span></p>
  <p class="pe-ex__uz">har kuni gazeta oʻqiydigan odam</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">제가 자주 <span class="pe-hl pe-hl--v">가는</span>
     카페는 학교 앞에 있어요.</p>
  <p class="pe-ex__uz">Men tez-tez boradigan kafe maktab oldida.</p>
  <p class="pe-ex__why">Aniqlovchi ichidagi ega <b>제가</b> shaklida turadi —
  제는 emas.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu darsdagi eng katta yordam.</b> Oʻzbek tilida ham aniqlovchi
  <b>otning oldida</b> turadi va ichidagi toʻldiruvchi ham oʻz joyida qoladi:
  “<em>kitob oʻqiydigan bola</em>”. Koreyschada: “<em>책을 읽는 아이</em>”.
  Soʻzma-soʻz bir xil tartib — kitob → oʻqiydigan → bola. Ingliz tilida esa
  bu butunlay teskari qurilma kerak (“the child <em>who reads</em> books”),
  va aynan shu sabab ingliz tilidan oʻrganayotgan oʻquvchilar bu darsda
  qiynaladi. Siz esa oʻzbekcha jumlani soʻz tartibini oʻzgartirmasdan
  koʻchira olasiz.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>는 ikkita oʻzbekcha qoʻshimchani qoplaydi.</b> Oʻzbek tilida
  “oʻqi<em>ydigan</em> bola” (odat) va “oʻqi<em>yotgan</em> bola” (hozir) —
  ikki xil shakl. Koreyschada ikkalasi ham <b>읽는 아이</b>. Yaʼni bu yerda
  koreys tili oʻzbekchadan <em>soddaroq</em>: bitta shakl yetadi, maʼnoni
  vaziyat aytadi. Tarjima qilayotganda esa jumlaga qarab tanlang —
  매일 읽는 사람 “har kuni oʻqiydigan odam”, 지금 읽는 사람 “hozir oʻqiyotgan
  odam”.</p>
</div>

<h3>5. Aniqlovchi ichida ega — 이/가 bilan</h3>

<p>Aniqlovchi ichidagi ega odatda <b>은/는</b> emas, <b>이/가</b> qoʻshimchasini
oladi. Buni bir marta yodlab qoʻysangiz, gaplaringiz darrov tabiiy chiqadi:</p>

<div class="pe-fix">
  <p class="pe-bad"><s>제는 좋아하는 음식</s></p>
  <p class="pe-good"><b>제가</b> 좋아하는 음식</p>
  <p><small>“Men yaxshi koʻradigan taom”. Aniqlovchi ichida — 제가.</small></p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu yerda oʻzbek tili sizni chalgʻitishi mumkin.</b> “Qiziqarli” —
  oʻzbekchada <em>sifat</em>, shuning uchun 재미있다 ni ham sifat deb oʻylash
  tabiiy. Lekin koreyschada u <b>재미 + 있다</b>, yaʼni “qiziqish <em>bor</em>”
  degan gap. Ichida 있다 (feʼl) turibdi. Xuddi shunday: 맛있다 = “mazasi bor”,
  멋있다 = “koʻrki bor”. Shuning uchun ular 는 oladi. Oʻzbekcha tarjimaga emas,
  <b>koreyscha tarkibga</b> qarang — shunda xato qilmaysiz.</p>
</div>

<h3>6. 는 — faqat hozirgi zamon</h3>

<p><b>는</b> ning ichiga zamon qoʻshimchasi qoʻyilmaydi. U doim hozirgi zamon
yoki odat maʼnosini beradi: <em>hozir qilayotgan</em> yoki <em>doim
qiladigan</em>.</p>

<div class="pe-fix">
  <p class="pe-bad"><s>어제 읽었는 책</s></p>
  <p class="pe-good">어제 <b>읽은</b> 책</p>
  <p><small>Oʻtgan zamon aniqlovchisi boshqa shakl oladi — uni PK-44 da
  oʻrganasiz. Bugungi 는 faqat hozirgi zamon uchun.</small></p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>먹은 사람 (“yeydigan odam” maʼnosida)</s></p>
  <p class="pe-good"><b>먹는</b> 사람</p>
  <p><small>Hozirgi zamon aniqlovchisi — <b>는</b>. 먹은 사람 “yegan odam”
  degani (PK-44).</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>서울에 살는 친구</s></p>
  <p class="pe-good">서울에 <b>사는</b> 친구</p>
  <p><small>ㄹ oʻzak ㄴ oldida ㄹ ni yoʻqotadi: 살 + 는 → 사는.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>재미있은 책</s></p>
  <p class="pe-good"><b>재미있는</b> 책</p>
  <p><small>재미있다 ichida 있다 — feʼl bor, shuning uchun 는 oladi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>사람 읽는 책 (“odam oʻqiydigan kitob”)</s></p>
  <p class="pe-good"><b>사람이 읽는</b> 책</p>
  <p><small>Aniqlovchi ichidagi ega qoʻshimchasiz qolmaydi — 이/가 oladi.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 지금 음악을
  <span class="pe-blank"></span> (듣다) 사람은 제 동생이에요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>듣는</b> — 는 undosh bilan boshlanadi, shuning uchun 듣 oʻzgarmaydi:
    <b>듣는 사람</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 부산에 <span class="pe-blank"></span>
  (살다) 친구가 있어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>사는</b> — ㄹ oʻzak ㄴ oldida ㄹ ni yoʻqotadi: 살 + 는 → <b>사는</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Koreyschaga oʻgiring: “qiziqarli kitob”.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>재미있는 책.</b> 재미있다 ichida 있다 (feʼl) bor, shuning uchun 는
    oladi — <s>재미있은</s> emas.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Ikki gapni bittaga birlashtiring:
  학생이 한국어를 공부해요. + 그 학생은 제 친구예요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>한국어를 공부하는 학생은 제 친구예요.</b> Birinchi gap butunligicha
    aniqlovchiga aylandi va 학생 ning oldiga oʻtdi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Xatoni toping:
  <s>제는 자주 가는 카페가 있어요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Aniqlovchi ichidagi ega 이/가 oladi. Toʻgʻrisi — <b>제가 자주 가는
    카페가 있어요.</b></p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Farqini ayting: 먹는 사람 va 먹은 사람.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>먹는 사람</b> — “yeydigan / yeb turgan odam” (hozirgi zamon).
    <b>먹은 사람</b> — “yegan odam” (oʻtgan zamon). Ikkinchi shaklni PK-44 da
    toʻliq oʻrganasiz.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>동사 + 는</b> — …adigan, …yotgan (hozirgi zamon aniqlovchisi)</li>
  <li><b>관형사형</b> — aniqlovchi shakl</li>
  <li><b>재미있는 / 재미없는</b> — qiziqarli / qiziq boʻlmagan</li>
  <li><b>맛있는 / 맛없는</b> — mazali / bemaza</li>
  <li><b>자주</b> — tez-tez</li>
  <li><b>알다</b> — bilmoq, tanimoq</li>
  <li><b>영화</b> — kino</li>
  <li><b>카페</b> — kafe</li>
  <li><b>앞</b> — old, oldida</li>
  <li><b>매일</b> — har kuni</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>동사 + 는 + 명사</b> — “…adigan ot”. Hozirgi zamon aniqlovchisi.</li>
    <li>는 undosh, shuning uchun ayri ham, notoʻgʻri oʻzgarish ham yoʻq:
      듣는, 돕는.</li>
    <li>ㄹ oʻzak ㄴ oldida ㄹ ni yoʻqotadi: 살다 → 사는, 알다 → 아는.</li>
    <li>있다/없다 → <b>있는 / 없는</b>: 재미있는 책, 맛없는 커피.</li>
    <li>Butun gap aniqlovchiga aylanadi va otning <b>oldiga</b> oʻtadi —
      oʻzbekchadagidek.</li>
    <li>Aniqlovchi ichidagi ega <b>이/가</b> oladi: 제가 가는 카페.</li>
    <li>는 ichiga zamon qoʻyilmaydi — u faqat hozirgi zamon va odat uchun.</li>
    <li>Sifatlar 는 olmaydi (PK-45), lekin 재미있다/맛있다 oladi — ular feʼl.</li>
  </ul>
</div>
""",
    },
]
